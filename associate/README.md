# Claude Certified Associate — Foundations (CCAO-F) course content

Source of truth for the **Associate Foundations Exam Prep Console** hosted at
[/associate-foundations/](https://jacinthpaul.github.io/Claude-Certified-Architect/associate-foundations/)
(code in [`ui/console-associate/`](../ui/console-associate/)).

Everything is aligned to the official **Claude Certified Associate – Foundations
Exam Guide** (v1.0, July 2026 · exam code CCAO-F · 60 items · 120 min ·
scaled 100–1000, pass ≥ 720).

## Layout

| File | Contents |
|---|---|
| `content/domains.py` | The 7 blueprint domains with official weights, plus the 3 cross-cutting themes |
| `content/lessons.py` | 30 lessons — one per blueprint objective — each with a claude.ai **chat walkthrough** (weak prompt → improved prompt), concept, analogy, anti-pattern/right-way, pitfall, and exam tip |
| `content/questions.py` | The 3 official sample questions (verbatim) + 27 authored practice questions, so every lesson has a completion quiz |
| `content/mock_bank.py` | 60 authored mock-exam questions, distributed per blueprint weights (D1:8 D2:13 D3:7 D4:10 D5:7 D6:9 D7:6) |
| `content/scenarios.py` | 6 end-to-end business scenarios; each step links to a lesson |
| `content/cheatsheet.py` | High-yield facts grouped by domain, each linked to its lesson |

## Blueprint → lesson map

| Domain (weight) | Lessons |
|---|---|
| D1 Prompting and Task Execution (14%) | 1.1–1.4 |
| D2 Output Evaluation and Validation (21%) | 2.1–2.6 |
| D3 Product and Model Selection (12%) | 3.1–3.4 |
| D4 Workflow Integration and Solution Design (16%) | 4.1–4.5 |
| D5 Configuration and Knowledge Management (12%) | 5.1–5.4 |
| D6 Governance, Risk, and Responsible Use (15%) | 6.1–6.4 |
| D7 Troubleshooting and Optimization (10%) | 7.1–7.3 |

## Editing content

1. Edit the module(s) in `content/`.
2. Regenerate the console's data file:

   ```bash
   python3 ui/console-associate/build_data.py
   ```

   The builder validates the model (30 lessons, blueprint distribution, every
   lesson quizzed, answer indices, cross-references) and fails loudly on errors.
   It also applies a **seeded option shuffle** per question id, so the correct
   answer isn't always "A" — keep the `why` explanations letter-free.
3. Commit both the content change and the regenerated
   `ui/console-associate/assets/data.js`.

### Chat walkthrough format

```python
"chat": [
    {"who": "note", "text": "scene-setting divider"},
    {"who": "user", "label": "Weak prompt", "text": "..."},   # label renders red
    {"who": "claude", "text": "..."},
    {"who": "user", "label": "Improved prompt", "text": "..."},  # renders green
    {"who": "claude", "text": "..."},
]
```

Labels matching `weak|vague|risky|before` render red; `improved|better|after|
fixed|safe` render green; anything else neutral. A `user` turn without a label
renders as a plain "You" bubble.

> This is an independent, community-made study aid — **not an official Anthropic
> product**. The official Exam Guide is the authoritative source.
