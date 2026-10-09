# Scoring rubric, anti-patterns, optimisation playbook

## Rubric (0–3 per dimension, 18 max per file)

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Placement** | Mostly wrong level (team rules in user file, secrets committed) | Several rules at the wrong level | One or two misplaced rules | Every rule at the level of its audience |
| **Signal** | Mostly generic advice Claude already follows | Large share of filler / restated defaults | Some filler | Every line is non-obvious and project-specific |
| **Specificity** | Vague ("be careful", "clean code") | Many rules not actionable | Mostly concrete; a few vague | Concrete commands, paths, names; reasons where non-obvious |
| **Consistency** | Direct contradictions | Conflicts across levels | Minor tension / stale wording | No conflicts, no duplication |
| **Economy** | >400 lines or heavy duplication | 200–400 lines, little structure | <200 lines with some bloat | Lean; detail pushed to rules/imports/skills |
| **Accuracy** | Commands/paths broken | Several stale references | One stale reference | All commands, paths, files verified to exist |

Interpretation for one file: **15–18** keep and polish · **10–14** targeted
edits · **<10** restructure (move, split, rewrite).

## Anti-pattern catalogue

| ID | Anti-pattern | Example | Fix |
|---|---|---|---|
| L1 | Team convention at user level | `~/.claude/CLAUDE.md`: "Use pnpm, not npm" for a team repo | Move to project CLAUDE.md |
| L2 | Personal preference committed | "I like verbose explanations" in `./CLAUDE.md` | Move to user file or `CLAUDE.local.md` |
| L3 | Package rule at root | Root file: "In `apps/web`, use Next.js app router" | `apps/web/CLAUDE.md` or rule with `paths: ["apps/web/**"]` |
| L4 | Scattered-file convention in a dir file | `src/CLAUDE.md` holds test rules for tests everywhere | `.claude/rules/testing.md` with `paths: ["**/*.test.*"]` |
| E1 | Enforcement by prose | "NEVER run `rm -rf`" / "never push to main" | `settings.json` `permissions.deny` or a PreToolUse hook; keep a one-line pointer |
| E2 | Procedure in memory | 40-line release checklist | Skill or slash command, linked by name |
| S1 | Generic filler | "Write clean, maintainable code", "follow best practices" | Delete |
| S2 | Linter-enforced style | "Use 2-space indentation" when Prettier is configured | Delete; mention the format command instead |
| S3 | Vague rule | "Be careful with the database" | Concrete: "Migrations go through `make migrate`; never edit `schema.sql` by hand" |
| S4 | Rule without reason (non-obvious) | "Don't use library X" | Add "because …" so Claude can generalise |
| S5 | Emphasis inflation | IMPORTANT / MUST on most lines | Keep emphasis for the 2–3 rules that truly need it |
| C1 | Contradiction | "Use Jest" (root) vs "Use Vitest" (package) with no scope | Scope explicitly or remove one |
| C2 | Duplication | Same rule in CLAUDE.md and `.claude/rules/x.md` | Single source; import or delete |
| A1 | Stale command/path | `npm run test:e2e` no longer exists | Fix or delete after checking |
| A2 | Broken import / fake syntax | `@import ./x.md`, `@docs/missing.md` | `@docs/x.md`, path verified |
| A3 | Rule glob matches nothing | `paths: ["src/**/*.spec.ts"]` in a Vitest `*.test.ts` repo | Fix the glob |
| X1 | Secret or sensitive value | API key, password, internal token | Remove immediately, rotate, reference env var name |
| X2 | Local file not ignored | `CLAUDE.local.md` tracked by git | Add to `.gitignore`, `git rm --cached` |
| D1 | Docs dump | Pasted README / API reference | Link or `@import` the canonical doc; keep a summary |
| D2 | Task diary | "Today I'm fixing bug #123" in a committed file | Move to `CLAUDE.local.md` or delete when done |

## Optimisation playbook

Apply in this order; each step makes the next one smaller.

1. **Secure.** Remove secrets (X1), ignore local files (X2). Do this even in
   review-only mode by flagging it as the first item.
2. **Move.** Relocate misplaced rules (L1–L4) to their correct level. Moving
   beats rewriting: content is preserved and lands where its audience is.
3. **Enforce.** Convert must-never-fail prose into settings/hooks (E1);
   propose the exact `settings.json` snippet. Keep a short pointer line.
4. **Extract.** Turn long procedures into skills (E2); turn topic blocks into
   `.claude/rules/<topic>.md`, with `paths:` when topic-specific.
5. **Cut.** Delete filler (S1), linter-enforced style (S2), duplicates (C2),
   finished task notes (D2).
6. **Sharpen.** Make vague rules concrete (S3), add reasons (S4), resolve
   contradictions (C1), fix stale references (A1–A3), deflate emphasis (S5).
7. **Structure.** Group under task-oriented headings (Overview, Commands,
   Architecture, Conventions, Workflow, Gotchas); bullets over paragraphs;
   commands in fenced blocks.
8. **Measure.** Re-run `scripts/audit_claude_md.py` and report before/after
   lines and approximate tokens per level, plus the new score.

### Writing a good line

- Imperative and specific: "Run `make check` before committing", not
  "Testing is important".
- One rule per bullet. Put the reason after "because" or an em-dash.
- Name exact files, commands, globs. Quote error messages Claude will see.
- Say what *to do*, not only what to avoid; a "never" without an alternative
  leaves Claude guessing.
