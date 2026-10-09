# CLAUDE.md levels: what belongs where

Claude Code concatenates every memory file that applies to the current
session. More specific levels are read later and win on conflict in practice,
but conflicts are still a defect: resolve them, don't rely on ordering.

| # | Level | Location | Audience | Shared via | Loaded |
|---|---|---|---|---|---|
| 1 | Managed policy | macOS `/Library/Application Support/ClaudeCode/CLAUDE.md` · Linux/WSL `/etc/claude-code/CLAUDE.md` · Windows `C:\Program Files\ClaudeCode\CLAUDE.md` | everyone in the organisation on that machine | IT / MDM | always |
| 2 | User | `~/.claude/CLAUDE.md`, `~/.claude/rules/*.md` | you, in every project | nothing (local only) | always |
| 3 | Project (ancestors) | `CLAUDE.md` / `.claude/CLAUDE.md` in each parent dir from cwd up to `/` | whoever opens a repo below that dir (monorepo root) | VCS | at launch |
| 4 | Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | the whole team in this repo | VCS | at launch |
| 5 | Project rules | `./.claude/rules/**/*.md` (optional `paths:` frontmatter) | team, scoped by topic or glob | VCS | no `paths`: always · with `paths`: when a matching file is touched |
| 6 | Local | `./CLAUDE.local.md` (gitignored) | you, in this repo only | nothing | at launch |
| 7 | Subdirectory | `<subdir>/CLAUDE.md` | team, when working inside that subtree | VCS | on demand, when Claude reads files there |
| — | Imports | `@relative/or/absolute/path.md` inside any of the above | inherits the importer's audience | inherits | with the importer (max 5 hops deep; not expanded inside code spans or fences) |

Useful commands: `/memory` shows the loaded files and opens one for editing;
`/init` bootstraps a project file from the codebase.

---

## 1. Managed policy

**Belongs:** organisation-wide security and compliance rules, approved
tooling, data-handling policy, links to internal standards.
**Doesn't belong:** language/framework style, anything project-specific,
personal preferences.

Checklist:
- [ ] Every rule applies to *every* repo in the org. If not, move it to the
      relevant project files.
- [ ] Hard requirements are also enforced in managed `settings.json`
      (permissions deny, hooks); the CLAUDE.md line explains the why.
- [ ] Short. Every token here is paid in every session by every engineer.
- [ ] No internal hostnames, tokens or credentials in plain text.

## 2. User (`~/.claude/CLAUDE.md`)

**Belongs:** personal working style ("explain trade-offs briefly",
"prefer small commits"), your own tool shortcuts, editor/OS quirks,
communication preferences.
**Doesn't belong:** team conventions (teammates never receive them: the
classic "Claude ignores our conventions for the new hire" bug), project
commands, secrets.

Checklist:
- [ ] Nothing a teammate would need to get the same result in a shared repo.
- [ ] Nothing that conflicts with common project conventions (e.g. "always
      use tabs" will fight every repo that uses spaces). Phrase as defaults:
      "unless the project says otherwise".
- [ ] Language/framework preferences that only matter for some projects live
      in `~/.claude/rules/<topic>.md` with `paths:` globs instead.
- [ ] Under ~50 lines is typical; it loads in every project.

## 3–4. Project (`./CLAUDE.md` or `./.claude/CLAUDE.md`)

**Belongs:** what a strong new teammate would need on day one and could not
infer quickly from the code:
- what the repo is and how it is laid out (only the non-obvious parts);
- build / test / lint / run commands, exactly as typed;
- architecture invariants and "don't do X because Y" decisions;
- generated files and how to regenerate them; files never to hand-edit;
- workflow rules (branching, commit/PR conventions, review requirements);
- gotchas: environment quirks, flaky areas, required env vars (names only).

**Doesn't belong:** generic advice Claude already follows ("write clean
code", "add comments"), things a linter/formatter enforces, full API docs
(link or `@import` them), long procedures used rarely (make a skill),
personal preferences (user or local level), secrets.

Checklist:
- [ ] Opening lines say what the project is in 1–3 sentences.
- [ ] Every command is copy-pasteable and still works.
- [ ] Each rule has a reason when the reason isn't obvious (rules with a
      "because" generalise better to cases they don't name).
- [ ] Headings group rules by when they matter (Build, Testing, Conventions,
      Deploy), so Claude can find the relevant block.
- [ ] Under ~200 lines; beyond that, split into `.claude/rules/` or imports.
- [ ] Monorepo: the root file holds only cross-cutting rules; package rules
      sit in each package's `CLAUDE.md` or a `paths:`-scoped rule.
- [ ] Emphasis (IMPORTANT, MUST, NEVER) is used on at most a handful of
      lines. If everything is important, nothing is.

## 5. Project rules (`.claude/rules/*.md`)

**Belongs:** topic files (testing, API conventions, security, migrations),
especially conventions for files *scattered* across the tree, e.g. tests
next to sources, which a directory CLAUDE.md can't cover.

```markdown
---
paths:
  - "**/*.test.ts"
  - "**/*.test.tsx"
---
# Testing conventions
- Name tests after the behaviour verified.
- Mock network calls; never hit real services.
```

Checklist:
- [ ] One topic per file, descriptive filename.
- [ ] Topic-specific rules have `paths:` globs so they load only when
      relevant; rules without `paths:` are truly global (and then ask whether
      they should just be in CLAUDE.md).
- [ ] Globs actually match files in the repo (the audit script checks this).
- [ ] No rule duplicated in CLAUDE.md as well.

## 6. Local (`CLAUDE.local.md`)

**Belongs:** your personal notes for this repo: local URLs, sandbox account
names, your test data, "I'm working on the payments refactor".
**Doesn't belong:** anything the team needs (move to project level).

Checklist:
- [ ] Listed in `.gitignore` (the audit script checks this).
- [ ] No credentials even so; use env vars or a secret manager.
- [ ] Prune stale task notes; this file rots fastest.

## 7. Subdirectory (`<subdir>/CLAUDE.md`)

**Belongs:** conventions that apply only inside that subtree: a package's
own commands, its framework idioms, generated-code warnings for that folder.
**Doesn't belong:** rules that also apply elsewhere (root file or a rule),
anything Claude needs *before* it reads files there (it loads lazily).

Checklist:
- [ ] Doesn't repeat the root file.
- [ ] Self-contained for its subtree; refers to the root only when needed.
- [ ] If the convention is per-file-type rather than per-folder, prefer a
      `paths:`-scoped rule.

## Imports (`@path`)

- Syntax is `@path/to/file.md` (relative to the importing file, or absolute,
  or `@~/…`). There is no `@import` keyword: `@import ./x.md` is a defect.
- Use imports to share one source of truth (e.g. `@docs/testing.md`) or to
  pull a personal file into a project (`@~/.claude/my-project-notes.md`), the
  multi-worktree alternative to `CLAUDE.local.md`.
- Imported content is always-on, the same as inline text; imports organise,
  they don't save tokens. For on-demand content, use rules with `paths:` or a
  skill.
- Max depth 5; `@` inside code spans/fences is not expanded.

## Choosing the mechanism

| Need | Use |
|---|---|
| Fact or convention Claude needs on most tasks | CLAUDE.md at the right level |
| Convention for certain file types or areas | `.claude/rules/` with `paths:` |
| Long procedure used occasionally | Skill (`.claude/skills/<name>/SKILL.md`) or slash command |
| Must *always* / *never* happen, no exceptions | `settings.json` permissions or a hook |
| Personal, this repo only | `CLAUDE.local.md` or an `@~/…` import |
| Personal, every repo | `~/.claude/CLAUDE.md` |
