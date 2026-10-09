---
name: claude-md-review
description: Review and optimise CLAUDE.md memory files at every level (managed/enterprise, user, project, local, subdirectory, .claude/rules, @imports). Use when asked to audit, review, clean up, slim down, restructure, or improve CLAUDE.md / memory files, when Claude seems to ignore instructions or behaves inconsistently across sessions or teammates, or before adding new standing instructions.
argument-hint: "Optional: a path, a level (user|project|local|subdir|rules|managed|all), and --apply to edit after review"
---

# CLAUDE.md review & optimisation

CLAUDE.md files are loaded into context on every session, so each line costs
tokens on every turn and competes for attention with every other line. The
goal of a review is **fewer, sharper, correctly placed instructions**: each
rule lives at the level whose audience it is meant for, says something Claude
could not infer from the code, and is concrete enough to act on.

## Inputs

- `$ARGUMENTS` may name a path, a level, or `--apply`. Default scope is `all`
  levels reachable from the current working directory; default mode is
  **review only** (report, no edits).
- Never edit the user-level (`~/.claude/…`) or managed-policy files without
  the user explicitly asking; they affect every project on the machine or in
  the organisation. Propose diffs for them instead.

## Workflow

1. **Discover and measure.** Run the audit script from the repo root:

   ```bash
   python3 .claude/skills/claude-md-review/scripts/audit_claude_md.py            # human report
   python3 .claude/skills/claude-md-review/scripts/audit_claude_md.py --json     # machine-readable
   python3 .claude/skills/claude-md-review/scripts/audit_claude_md.py --root path/to/repo --no-user
   ```

   It lists every memory file by level, its lines and approximate tokens,
   resolves `@imports` (flags broken or too-deep ones), checks `.claude/rules/`
   frontmatter, and flags mechanical smells (possible secrets, vague
   wording, duplicates across levels, oversized files). Treat its findings as
   leads to verify, not verdicts.

2. **Read every file it found, in full**, in load order (managed → user →
   project ancestors → project → local → rules → subdirectories). Also run
   `/memory` mentally against the list: anything the user expects to be loaded
   but is missing is a finding.

3. **Review each file against its level.** Use
   [references/levels.md](references/levels.md) for what belongs where and the
   per-level checklist. The most common, highest-impact defects:
   - **Wrong level.** Team conventions in `~/.claude/CLAUDE.md` (teammates
     never get them); personal preferences in the committed project file;
     package-specific rules in the root file instead of that package's
     subdirectory or a path-scoped rule.
   - **Prose where enforcement is needed.** "Never run X / never touch Y"
     that must hold every time belongs in `settings.json` permissions or a
     hook, with at most a one-line pointer in CLAUDE.md.
   - **Workflows that should be skills.** Long multi-step procedures used
     occasionally (release steps, migration recipes) belong in a skill or
     slash command, loaded on demand, not in always-on memory.
   - **Contradictions** within a file or across levels. Claude gets all
     levels concatenated; conflicting rules resolve unpredictably.

4. **Score the file(s)** with [references/rubric.md](references/rubric.md)
   (six dimensions, 0–3 each) and collect findings using its anti-pattern
   catalogue.

5. **Report** using the template below. Lead with the 3–5 changes that buy
   the most (wrong-level moves, contradictions, enforcement gaps, big token
   cuts), then the rest.

6. **Optimise (only with `--apply` or explicit approval).** Apply the
   optimisation playbook in [references/rubric.md](references/rubric.md#optimisation-playbook):
   move, cut, sharpen, split, then re-run the audit and report before/after
   lines and tokens. Preserve every instruction whose intent you are not sure
   is obsolete: ask instead of deleting. Keep the file's existing voice and
   structure where it works; this is an edit, not a rewrite.

## Report template

```markdown
## CLAUDE.md review: <scope>

**Loaded set** (load order): <level> <path> (<lines> lines, ~<tokens> tok) …
**Total always-on cost:** ~<tokens> tokens · **Score:** <n>/18

### Top changes
1. <change>: <why, 1 line> (<level> → <level> | −<n> lines | fixes conflict)

### Findings by file
#### <path> (<level>, <score>/18)
- [severity] <finding>: <evidence quote or line ref> → <proposed fix>

### Proposed edits
<unified diffs or moved-block listings, grouped by destination file>

### Left as is
- <instruction that looks odd but is intentional, and why>
```

Severity: **high** = wrong behaviour or leaked secret (wrong level for team
rules, contradiction, missing enforcement, credentials); **medium** = wasted
context or ambiguity (duplication, vague rule, stale command, workflow that
should be a skill); **low** = style and structure.

## Guardrails

- Verify before cutting: if a rule names a command, path or script, check it
  still exists (`ls`, `grep`) before calling it stale.
- Do not cut a rule only because it seems obvious to you; cut it when the
  repo itself makes it obvious (linters, formatters, config, code patterns).
- Never paste secrets into the report; quote the line number only.
- Keep project-specific invariants (non-obvious architecture rules, generator
  or build steps, legal/disclaimer requirements) even if long; they are what
  CLAUDE.md is for.
