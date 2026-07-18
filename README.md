# Claude Certification Exam Prep — Foundations Consoles

Free, self-paced exam-prep consoles for Claude certifications — one console per
certification, deployed together as a single GitHub Pages site. **No install: open a
link and start studying.**

| Certification | Live console | Study experience |
|---|---|---|
| **Certification Hub** (start here) | [jacinthpaul.github.io/Claude-Certified-Architect](https://jacinthpaul.github.io/Claude-Certified-Architect/) | Landing page routing all four certifications — two consoles live, two coming soon |
| **Claude Certified Architect – Foundations** | […/architect-foundations/](https://jacinthpaul.github.io/Claude-Certified-Architect/architect-foundations/) | 5 domains · 30 lessons with **runnable Python demos** · 6 scenario systems · cheat sheet · 60-question mock exam · progress + certificate |
| **Claude Certified Associate – Foundations (CCAO-F)** | […/associate-foundations/](https://jacinthpaul.github.io/Claude-Certified-Architect/associate-foundations/) | 7 domains · 30 lessons with **claude.ai chat walkthroughs** · 6 business scenarios · cheat sheet · blueprint-weighted 60-question mock exam · progress + certificate |

Both consoles are self-paced courses: a "Start here" page, per-lesson questions you answer
until correct, a timed mock exam scored 100–1000 (pass ≥ 720, like the real exams), and a
completion certificate. Progress is saved in your browser. Two more consoles
(Developer – Foundations and Architect – Professional) are planned — see
[CLAUDE.md](CLAUDE.md) for the multi-console strategy this repo follows.

---

## Claude Certified Architect — Foundations: a runnable teaching codebase

A hands-on companion to the **Claude Certified Architect – Foundations** exam. Every
concept from the study guide is turned into a small, **runnable** Python demo you can
project on a screen, step through, and discuss in a teaching session — the hosted console
above is generated from this codebase.

## 🎥 Video walkthrough

A quick overview of the Architect Foundations Exam topics and exam questions — click to watch on YouTube:

[![Claude Certified Architect — Exam Prep Console walkthrough](https://img.youtube.com/vi/of9PPnuBedU/maxresdefault.jpg)](https://youtu.be/of9PPnuBedU)

It's a **self-paced course**: a "Start here" page, a progress bar, per-lesson questions you
answer until correct, a mock exam, and a completion certificate.

![The course welcome page with a name field and an overview of what each section contains](docs/course-start.png)

![The completion certificate with confetti, shown after all 30 lessons are done](docs/course-certificate.png)

![The browser console running a task demo — sidebar of domains/tasks, the concept banner, and the anti-pattern/fix cards](docs/console-demo.png)

- **5 domains**, all 30 task statements (Tasks 1.1 → 5.6) — one self-explaining demo each.
- **6 scenarios** — fuller, end-to-end runnable systems (a real support agent, a
  multi-agent research pipeline, an extraction pipeline, and more).
- **The 12 official sample questions** — as an interactive, self-grading quiz.
- A **cheat sheet**, the **3 prep exercises**, and a **teaching guide** with a lesson plan.
- Two **web UIs** — a hosted React **Exam Prep Console** (link above) and a zero-dependency
  built-in console — for running demos and the quiz in class.
- **Functional scenario apps** you drive with real input (a chat agent, a live code
  reviewer, a document extractor, and more).

Every demo runs **with zero setup**: with no API key it uses a clearly-labelled
deterministic simulator so the architecture and the teaching points are identical. Set
`ANTHROPIC_API_KEY` to make the model-calling demos hit the real Claude API.

---

## Quick start

Or just open the **[hosted console](https://jacinthpaul.github.io/Claude-Certified-Architect/architect-foundations/)** — no clone, no install. To run locally:

```bash
# nothing to install for the offline (simulated) demos — standard library only
python3 run_all.py ui              # ★ launch the web UI, then open http://127.0.0.1:8000
python3 run_all.py --list          # see everything runnable
python3 run_all.py --check         # smoke-test every demo (prints PASS/FAIL)

# run one concept (with [press ENTER] pauses — ideal for live teaching)
python3 domains/domain1_orchestration/task1_1_agentic_loop.py

# run a whole group, non-stop
python3 run_all.py domain1
python3 run_all.py scenarios
python3 run_all.py exam

# drive a scenario as a functional app (real input → real output)
python3 scenarios/run.py 1 -i      # chat with the support agent
python3 scenarios/run.py 4 -i      # explore this repo with real Grep/Read
```

To run the model-calling demos **live**:

```bash
pip install -r requirements.txt
cp .env.example .env        # then put your key in it, or just export it:
export ANTHROPIC_API_KEY=sk-ant-...
python3 domains/domain4_prompt_output/task4_2_few_shot.py   # now hits the real API
```

> The teaching pauses (`[press ENTER]`) appear only when you run a file directly in a
> terminal. `run_all.py` and CI set `CCARCH_NONSTOP=1` to skip them.

---

## How the codebase maps to the exam

### The five domains (`domains/`)

| Domain | Weight | Folder | Tasks covered |
|---|---|---|---|
| 1 · Agentic Architecture & Orchestration | 27% | `domain1_orchestration/` | 1.1–1.7 |
| 2 · Tool Design & MCP Integration | 18% | `domain2_tools_mcp/` | 2.1–2.5 |
| 3 · Claude Code Configuration & Workflows | 20% | `domain3_claude_code/` | 3.1–3.6 (+ real config artifacts) |
| 4 · Prompt Engineering & Structured Output | 20% | `domain4_prompt_output/` | 4.1–4.6 |
| 5 · Context Management & Reliability | 15% | `domain5_context_reliability/` | 5.1–5.6 |

Each `taskX_Y_*.py` file is a standalone lesson: it states the concept, **demonstrates it
running**, shows the anti-patterns the exam uses as distractors, and ends with the exam tip.

### The six scenarios (`scenarios/`)

| Scenario | Primary domains | What runs |
|---|---|---|
| 1 · Customer Support Resolution Agent | D1 · D2 · D5 | Agent loop + prerequisite gate + interception hook + structured errors + case-facts + escalation |
| 2 · Code Generation with Claude Code | D3 · D5 | Config-scope decisions, plan-vs-direct, path rules, refinement |
| 3 · Multi-Agent Research System | D1 · D2 · D5 | Coordinator + subagents, narrow-decomposition failure + fix, error propagation, provenance |
| 4 · Developer Productivity | D2 · D3 · D1 | Real incremental exploration (Grep→Read) over a sample repo; delegation + scratchpad |
| 5 · Claude Code for CI/CD | D3 · D4 | Non-interactive `-p`, structured output, false-positive control, multi-pass review |
| 6 · Structured Data Extraction | D4 · D5 | Tool-use schema, nullable fields, validation/retry, batch routing, confidence routing |

### The exam (`exam/`)

- `sample_questions.py` — the 12 official sample questions, interactive and self-grading,
  each tagged with the domain/task and the demo that shows the concept.
- `cheatsheet.py` — the high-yield facts to memorize, each pointing to its demo.
- `prep_exercises.py` — the 3 official hands-on exercises, mapped to worked references here.

---

## The three themes that run through everything

1. **Guarantees beat instructions.** Must-follow rules (verify identity before a refund)
   go in **code** (hooks, gates, schemas), not in a prompt. Prompts are probabilistic.
2. **Fix the root cause, proportionately.** Vague tool descriptions → better descriptions,
   not a routing classifier. The exam loves over-engineered distractors.
3. **Context is a scarce, leaky resource.** Extract key facts, trim noise, pass information
   explicitly between agents.

> The exam's underlying question is always: *what is the simplest mechanism that reliably
> fixes the actual root cause?*

---

## Claude Certified Associate — Foundations (CCAO-F) console

A separate, independent prep console for the **Associate Foundations** exam — built for
its non-technical audience (operations, marketing, project management, education,
communications), so lessons show **claude.ai chat walkthroughs** (a weak prompt vs an
improved prompt, with Claude's responses and commentary) instead of terminal demos.

**Open it:** **[https://jacinthpaul.github.io/Claude-Certified-Architect/associate-foundations/](https://jacinthpaul.github.io/Claude-Certified-Architect/associate-foundations/)**

What's inside — all aligned to the official CCAO-F Exam Guide (60 items · 120 min ·
scaled 100–1000 · pass ≥ 720):

- **7 blueprint domains** with the official weights: Prompting 14% · Output Evaluation 21% ·
  Product & Model Selection 12% · Workflow Integration 16% · Configuration & Knowledge 12% ·
  Governance & Responsible Use 15% · Troubleshooting 10%.
- **30 lessons** — one per blueprint objective — each with a chat walkthrough, concept,
  analogy, anti-pattern vs right way, common confusion, exam tip, and a completion question.
- **The 3 official sample questions** (verbatim) + 27 authored practice questions.
- **60-question mock exam** distributed exactly per the blueprint weights, with exam/practice
  modes, a timer, and a per-domain score breakdown.
- **6 end-to-end business scenarios** and a **cheat sheet** of high-yield facts.

Where things live:

| Piece | Path |
|---|---|
| Console app (React, static) | [`ui/console-associate/`](ui/console-associate/) |
| Course content (source of truth) | [`associate/content/`](associate/content/) |
| Blueprint → lesson map + authoring guide | [`associate/README.md`](associate/README.md) |
| Data generator (validates + emits `data.js`) | `python3 ui/console-associate/build_data.py` |

The two consoles are deliberate **independent forks** (separate app code, styles, and
browser storage) — enhancing one never affects the other. The change-scope rules for
maintaining them live in [CLAUDE.md](CLAUDE.md).

---

## Repository layout

```
.
├── README.md                  ← you are here
├── run_all.py                 ← teaching playlist + smoke test
├── requirements.txt           ← only needed for LIVE (API) mode
├── .env.example
├── CLAUDE.md                  ← multi-console maintenance strategy (read before enhancing)
├── ccarch/                    ← shared toolkit (display + Claude client w/ simulator)
├── domains/                   ← Architect: 30 task demos across 5 domains
├── scenarios/                 ← Architect: 6 scenario walkthroughs + functional app.py each
├── exam/                      ← Architect: sample questions, mock bank, cheat sheet
├── associate/                 ← Associate (CCAO-F): course content source + blueprint map
│   └── content/               ← domains, lessons, questions, mock bank, scenarios, cheatsheet
├── teaching/                  ← lesson plan / session guide
├── ui/                        ← built-in zero-dependency web console
│   ├── hub/                   ← Certification Hub landing page (hosted at /)
│   ├── console/               ← Architect React console (hosted at /architect-foundations/)
│   └── console-associate/     ← Associate React console (hosted at /associate-foundations/)
└── .github/workflows/         ← CI smoke test + GitHub Pages deploy (stages hub + consoles)
```

## The web UI

There are two browser consoles; both run the repo's demos and the quiz, and neither needs
`pip install`.

### 1. Exam Prep Console (React) — `ui/console/` · **hosted**

The polished console: a dashboard, domain/task sidebar, **Scenarios** and **Cheat sheet**
views, light/dark themes, "mark covered" progress, and the interactive 12-question quiz.

- **Hosted (zero setup):** **[https://jacinthpaul.github.io/Claude-Certified-Architect/architect-foundations/](https://jacinthpaul.github.io/Claude-Certified-Architect/architect-foundations/)**
  — `.github/workflows/pages.yml` stages the hub at `/`, this console at
  `/architect-foundations/`, and the Associate console at `/associate-foundations/` into
  one Pages site and deploys on every push. As a static page it shows the demo output
  baked into the page; the sidebar, quiz, and cheat sheet are fully interactive.
- **Locally, with live demo runs:** `python3 ui/console/api_server.py` then open
  `http://127.0.0.1:8000` — clicking **Run** executes the actual demo file and streams its
  real output. See `ui/console/README.md`.

### 2. Built-in console — `ui/`

A zero-dependency console on Python's standard-library HTTP server:

```bash
python3 run_all.py ui                      # http://127.0.0.1:8000
python3 ui/server.py --host 0.0.0.0 --port 9000   # share on your network
```

It lists every demo in a sidebar, runs them on click (rendering the ✗/✓/★ blocks as colored
cards), and includes the self-grading quiz. See `ui/README.md`.

![The interactive 12-question quiz — click an answer and it grades instantly with an explanation](docs/console-quiz.png)

*(Screenshots show the built-in console; the hosted Exam Prep Console at the link above has
its own light/dark themed design.)*

> Both consoles cover the **click-through demos + quiz**. The **functional scenario apps**
> (below) read keyboard input and the filesystem, so they run in a terminal, not the browser.

## Functional scenario apps

Beyond the scripted walkthroughs, each scenario has a working `app.py` you drive with real
input — see them in action:

```bash
python3 scenarios/run.py               # list the apps
python3 scenarios/run.py 1 -i          # chat with a gated, hook-guarded support agent
python3 scenarios/run.py 5 ccarch/client.py --json   # review a real file, CI-style
python3 scenarios/run.py 6 "Pd $1,200.50 to Acme Corp on 3/4/25"   # extract → validated JSON
```

They're deterministic and offline (no API key). See `scenarios/README.md`.

See `teaching/teaching_guide.md` for a ready-to-run session plan, and each
`domains/*/README.md` for a per-domain index.

*Both consoles are independent, community-made study and teaching aids based on the
official Exam Guides — not official Anthropic products. Always treat the official Exam
Guide as the authoritative source. For educational use.*
