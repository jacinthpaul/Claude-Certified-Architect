#!/usr/bin/env python3
"""Audit CLAUDE.md memory files at every level. Stdlib only, read-only.

Discovers managed, user, ancestor, project, local, rules and subdirectory memory
files, measures them, resolves @imports, checks rule globs and flags mechanical
smells. Findings are leads for the reviewer, not verdicts.

    python3 audit_claude_md.py [--root DIR] [--json] [--no-user] [--no-managed]
"""

import argparse
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

MAX_LINES = 200          # per-file size guidance
MAX_IMPORT_DEPTH = 5     # Claude Code stops expanding @imports after 5 hops
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist",
             "build", "_site", ".next", "target", ".tox", ".mypy_cache"}

IMPORT_RE = re.compile(r"(?<![\w`])@((?:~|\.{1,2})?/?[\w.\-/~]+\.\w+)")
FAKE_IMPORT_RE = re.compile(r"^\s*@import\b", re.M)
SECRET_RE = re.compile(
    r"(?i)(api[_-]?key|secret|password|passwd|token|bearer)\s*[:=]\s*['\"]?[A-Za-z0-9_\-./+]{12,}"
    r"|sk-[A-Za-z0-9_\-]{20,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}")
VAGUE_RE = re.compile(
    r"(?i)\b(best practices|clean code|be careful|as needed|where appropriate|"
    r"high[- ]quality|maintainable code|make sure to write good|properly)\b")
EMPHASIS_RE = re.compile(r"\b(IMPORTANT|MUST|NEVER|ALWAYS|CRITICAL)\b")


def managed_paths():
    system = platform.system()
    if system == "Darwin":
        return [Path("/Library/Application Support/ClaudeCode/CLAUDE.md")]
    if system == "Windows":
        return [Path(r"C:\Program Files\ClaudeCode\CLAUDE.md")]
    return [Path("/etc/claude-code/CLAUDE.md")]


def strip_code(text):
    """Drop fenced blocks and inline code: @refs there are not imports."""
    text = re.sub(r"^(```|~~~).*?^\1", "", text, flags=re.M | re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def frontmatter_paths(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    block, paths, in_list = m.group(1), [], False
    for line in block.splitlines():
        if re.match(r"^paths\s*:", line):
            inline = line.split(":", 1)[1].strip()
            if inline.startswith("["):
                items = re.split(r",(?![^{]*\})", inline.strip("[]"))  # keep {a,b} intact
                return [p.strip().strip("'\"") for p in items if p.strip()]
            if inline:
                return [inline.strip("'\"")]
            in_list = True
        elif in_list and re.match(r"^\s*-\s+", line):
            paths.append(re.sub(r"^\s*-\s+", "", line).strip().strip("'\""))
        elif in_list and line.strip():
            in_list = False
    return paths


def expand_braces(pattern):
    m = re.search(r"\{([^{}]*)\}", pattern)
    if not m:
        return [pattern]
    out = []
    for alt in m.group(1).split(","):
        out += expand_braces(pattern[:m.start()] + alt + pattern[m.end():])
    return out


def glob_matches(root, pattern):
    for pat in expand_braces(pattern):
        try:
            for p in root.glob(pat):
                if not (set(p.relative_to(root).parts) & SKIP_DIRS):
                    return True
        except (ValueError, NotImplementedError):
            pass
    return False


def resolve_imports(path, depth, seen, findings, chain):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    found = []
    for ref in IMPORT_RE.findall(strip_code(text)):
        target = Path(os.path.expanduser(ref)) if ref.startswith("~") else (
            Path(ref) if ref.startswith("/") else path.parent / ref)
        target = target.resolve()
        if not target.exists():
            findings.append(("high", "A2", f"broken import @{ref} (from {chain[-1]})"))
            continue
        if depth >= MAX_IMPORT_DEPTH:
            findings.append(("medium", "A2", f"@{ref} is beyond {MAX_IMPORT_DEPTH} import hops; not loaded"))
            continue
        if target in seen:
            continue
        seen.add(target)
        found.append({"ref": ref, "path": str(target), "depth": depth + 1,
                      "tokens": approx_tokens(target)})
        found += resolve_imports(target, depth + 1, seen, findings, chain + [ref])
    return found


def approx_tokens(path):
    try:
        return round(len(path.read_text(encoding="utf-8", errors="replace")) / 4)
    except OSError:
        return 0


def git_ignored(root, path):
    try:
        r = subprocess.run(["git", "-C", str(root), "check-ignore", "-q", str(path)],
                           capture_output=True)
        return r.returncode == 0
    except OSError:
        return None


def git_root(start):
    try:
        out = subprocess.run(["git", "-C", str(start), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True)
        if out.returncode == 0:
            return Path(out.stdout.strip())
    except OSError:
        pass
    return start


def discover(root, include_user, include_managed):
    found = []

    def add(level, p):
        if p.is_file() and all(Path(f["path"]) != p.resolve() for f in found):
            found.append({"level": level, "path": str(p.resolve())})

    if include_managed:
        for p in managed_paths():
            add("managed", p)
    if include_user:
        home = Path.home() / ".claude"
        add("user", home / "CLAUDE.md")
        for p in sorted((home / "rules").rglob("*.md")) if (home / "rules").is_dir() else []:
            add("user-rule", p)
    for anc in reversed(root.parents):
        add("ancestor", anc / "CLAUDE.md")
        add("ancestor", anc / ".claude" / "CLAUDE.md")
    add("project", root / "CLAUDE.md")
    add("project", root / ".claude" / "CLAUDE.md")
    add("local", root / "CLAUDE.local.md")
    rules = root / ".claude" / "rules"
    if rules.is_dir():
        for p in sorted(rules.rglob("*.md")):
            add("rule", p)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and d != ".claude")
        if Path(dirpath) != root and "CLAUDE.md" in filenames:
            add("subdirectory", Path(dirpath) / "CLAUDE.md")
    return found


def audit_file(entry, root):
    path = Path(entry["path"])
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    findings = []
    nonblank = [l for l in lines if l.strip()]
    entry.update(lines=len(lines), nonblank=len(nonblank), tokens=round(len(text) / 4))

    if len(lines) > MAX_LINES:
        findings.append(("medium", "economy", f"{len(lines)} lines (> {MAX_LINES}); split into rules/imports/skills"))
    if FAKE_IMPORT_RE.search(strip_code(text)):
        findings.append(("medium", "A2", "'@import' keyword is not import syntax; use '@path/to/file.md'"))
    for i, line in enumerate(lines, 1):
        if SECRET_RE.search(line):
            findings.append(("high", "X1", f"line {i}: possible secret (value not shown)"))
        if VAGUE_RE.search(line):
            findings.append(("low", "S3", f"line {i}: vague wording: {line.strip()[:90]}"))
    emphasis = sum(len(EMPHASIS_RE.findall(l)) for l in lines)
    if nonblank and emphasis > max(5, len(nonblank) // 10):
        findings.append(("low", "S5", f"{emphasis} emphasis words (IMPORTANT/MUST/NEVER…) in {len(nonblank)} lines"))

    if entry["level"] == "local":
        ignored = git_ignored(root, path)
        if ignored is False:
            findings.append(("high", "X2", "CLAUDE.local.md is not gitignored"))
    if entry["level"] in ("rule", "user-rule"):
        globs = frontmatter_paths(text)
        entry["paths"] = globs
        if globs is None:
            findings.append(("low", "L4", "no `paths:` frontmatter: loads always; confirm it is truly global"))
        elif entry["level"] == "rule":
            for g in globs:
                if not glob_matches(root, g):
                    findings.append(("medium", "A3", f"paths glob matches no files: {g}"))

    entry["imports"] = resolve_imports(path, 0, {path.resolve()}, findings, [path.name])
    entry["findings"] = [{"severity": s, "code": c, "detail": d} for s, c, d in findings]
    return lines


def duplicates(entries, texts):
    seen, dups = {}, []
    for e in entries:
        for raw in texts[e["path"]]:
            norm = re.sub(r"[\s*_`>#-]+", " ", raw).strip().lower()
            if len(norm) < 30:
                continue
            if norm in seen and seen[norm] != e["path"]:
                dups.append({"text": raw.strip()[:100], "files": [seen[norm], e["path"]]})
            seen.setdefault(norm, e["path"])
    return dups


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".", help="repo or directory to audit (default: git root of cwd)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--no-user", action="store_true", help="skip ~/.claude files")
    ap.add_argument("--no-managed", action="store_true", help="skip managed-policy file")
    args = ap.parse_args()

    root = git_root(Path(args.root).resolve())
    entries = discover(root, not args.no_user, not args.no_managed)
    texts = {e["path"]: audit_file(e, root) for e in entries}
    dups = duplicates(entries, texts)

    always = [e for e in entries if e["level"] in ("managed", "user", "ancestor", "project", "local")
              or (e["level"] in ("rule", "user-rule") and not e.get("paths"))]
    always_tokens = sum(e["tokens"] + sum(i["tokens"] for i in e["imports"]) for e in always)
    report = {"root": str(root), "files": entries, "duplicates": dups,
              "always_on_tokens": always_tokens}

    if args.json:
        json.dump(report, sys.stdout, indent=2)
        print()
        return

    def rel(p):
        try:
            return str(Path(p).relative_to(root))
        except ValueError:
            return p.replace(str(Path.home()), "~")

    print(f"CLAUDE.md audit: {root}\n")
    if not entries:
        print("No memory files found. Consider /init to bootstrap a project CLAUDE.md.")
        return
    print(f"{'level':<13} {'lines':>5} {'~tok':>6}  path")
    for e in entries:
        print(f"{e['level']:<13} {e['lines']:>5} {e['tokens']:>6}  {rel(e['path'])}")
        for i in e["imports"]:
            print(f"{'  import':<13} {'':>5} {i['tokens']:>6}  {'  ' * i['depth']}@{i['ref']}")
    print(f"\nAlways-on context (no paths-scoped rules, no subdirectories): ~{always_tokens} tokens\n")

    total = 0
    for e in entries:
        if e["findings"]:
            print(f"## {rel(e['path'])} ({e['level']})")
            for f in sorted(e["findings"], key=lambda f: ["high", "medium", "low"].index(f["severity"])):
                print(f"  [{f['severity']}] {f['code']}: {f['detail']}")
                total += 1
            print()
    if dups:
        print("## Duplicated lines across files (C2)")
        for d in dups[:20]:
            print(f"  \"{d['text']}\"\n     in {rel(d['files'][0])} and {rel(d['files'][1])}")
        total += len(dups)
        print()
    print(f"{total} mechanical finding(s). Now read each file and review it against references/levels.md.")


if __name__ == "__main__":
    main()
