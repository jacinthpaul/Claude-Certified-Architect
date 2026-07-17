# CLAUDE.md

Guidance for Claude Code (and human contributors) working in this repo.

## What this repo is

One repo hosting **multiple independent exam-prep consoles** for Claude
certifications, deployed together as a single GitHub Pages site:

| Console | Live path | App code | Content source of truth | Data generator |
|---|---|---|---|---|
| Architect – Foundations | `/` | `ui/console/` | `exam/*.py` + `domains/*` runnable demos | `python3 ui/console/build_data.py` |
| Associate – Foundations (CCAO-F) | `/associate/` | `ui/console-associate/` | `associate/content/*.py` | `python3 ui/console-associate/build_data.py` |

More consoles (and a unified hub landing page) are planned — follow the same
pattern: one `ui/console-<name>/` folder + one content package per cert.

Each console is a single-file React app (CDN React + Babel Standalone, no build
step) rendering a generated `assets/data.js`. They are **full forks, not shared
code**: separate `app.jsx`, `styles.css`, JS globals (`CCA` vs `CCAF`), and
localStorage namespaces (`cca-*` vs `ccaf-*`). Editing one console never
affects the other.

## Multi-console change strategy (IMPORTANT)

When asked for an enhancement, first determine the scope — ask if unclear:

1. **Content changes are always per-console.** The courses are different;
   lessons, questions, scenarios, and cheat facts never sync across consoles.
   Edit the content package, rerun that console's `build_data.py`, commit the
   regenerated `data.js` together with the content change. Never hand-edit
   `assets/data.js`.

2. **Single-console UI feature:** edit only that console's `app.jsx` /
   `styles.css`. Do not "helpfully" port it to the other console unless asked.

3. **Shared UI feature (both consoles):** implement and verify it in one
   console first, then port the same diff to the other. The `app.jsx` files
   are kept structurally parallel (same component names and ordering) so the
   port is usually near-verbatim. Verify each console independently after
   porting.

4. **Keep the forks parallel, not identical.** Functional drift is fine
   (chat walkthroughs vs terminal demos); structural/stylistic drift makes
   porting expensive. When touching shared structure, keep names and layout
   aligned across both files.

5. **Never hard-code course identity in app code.** No
   "if this is the associate console…" branches inside `app.jsx` — anything
   course-specific (branding, counts, weights, labels, demo type) belongs in
   the data model or config. This keeps the planned refactor cheap: when the
   unified hub is built (at 3–4 consoles), extract a shared engine
   (`ui/shared/`) that renders any cert's data package, with per-console
   config for branding/namespace/accent. Until then, fork-and-port is the
   deliberate trade-off — do not extract shared code prematurely.

## Build & verify

```bash
# regenerate a console's data.js after editing its content package
python3 ui/console/build_data.py             # architect
python3 ui/console-associate/build_data.py   # associate (validates blueprint
                                             # coverage/distribution, fails loudly)

# repo smoke test (CI runs this on every push)
python3 run_all.py --check
```

Quiz/mock explanations (`why`) must stay **letter-free** ("the correct
option…", never "option B") — generators shuffle options with a per-question
seeded order.

To verify a console end-to-end, stage the site and drive it with the local
Chromium (`/opt/pw-browsers/chromium` in Claude Code remote sessions):

```bash
mkdir -p _site/associate && cp -r ui/console/. _site/ && cp -r ui/console-associate/. _site/associate/
cd _site && python3 -m http.server 8931
```

Note for sandboxed sessions: unpkg.com/github.io may be blocked; vendor
React/Babel locally into the staged copy for testing only — never change the
CDN references in the committed `index.html`.

## Deploy

`.github/workflows/pages.yml` stages BOTH consoles into one Pages artifact
(architect at `/`, associate at `/associate/`) and deploys on push to the
branches listed in its trigger. When adding a new console or deploy branch:

- add the `cp -r` staging line and the trigger branch in `pages.yml`;
- the `github-pages` **environment → Deployment branches** setting must allow
  the branch (repo Settings; a run rejected in ~2s with no runner assigned
  means this rule is missing);
- keep each console's `index.html` cache-bust query (`?v=YYYYMMDDx`) bumped
  when its assets change.

## Content alignment

Course content must track the official exam guides (blueprint domains,
weights, objective lists, official sample questions). The Associate blueprint
map lives in `associate/README.md`. Both consoles are independent community
study aids, not official Anthropic products — keep the footer disclaimers.
