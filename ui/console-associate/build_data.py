#!/usr/bin/env python3
"""
ui/console-associate/build_data.py — regenerate assets/data.js for the CCAO-F console.

Source of truth is associate/content/*.py (domains, lessons, questions, mock bank,
scenarios, cheat sheet), all aligned to the official Claude Certified Associate –
Foundations Exam Guide. This generator validates the content model (coverage,
distribution, answer indices, cross-references), applies the same seeded option
shuffle as the Architect console's builder (stable across regenerations, so the
correct answer isn't always A), and emits window.CCAF.

Run:  python3 ui/console-associate/build_data.py    # rewrites ui/console-associate/assets/data.js
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, REPO)

from associate.content.domains import DOMAINS, THEMES  # noqa: E402
from associate.content.lessons import LESSONS  # noqa: E402
from associate.content.questions import OFFICIAL_SAMPLES, PRACTICE  # noqa: E402
from associate.content.mock_bank import MOCK_BANK  # noqa: E402
from associate.content.scenarios import SCENARIOS  # noqa: E402
from associate.content.cheatsheet import FACTS  # noqa: E402

# Official blueprint: domain weight -> item count on a 60-question exam.
MOCK_DISTRIBUTION = {"d1": 8, "d2": 13, "d3": 7, "d4": 10, "d5": 7, "d6": 9, "d7": 6}
LESSONS_PER_DOMAIN = {"d1": 4, "d2": 6, "d3": 4, "d4": 5, "d5": 4, "d6": 4, "d7": 3}
CHAT_WHO = {"user", "claude", "note"}


def _shuffle_options(options, answer_idx, seed):
    """Deterministically reorder the 4 options so the correct answer isn't always A.
    Seeded by the question id, so the order is stable across regenerations (no churn).
    The explanations are letter-free, so reordering never invalidates them."""
    order = list(range(len(options)))
    random.Random(seed).shuffle(order)
    return [options[i] for i in order], order.index(answer_idx)


def _convert(q, qid, with_ref=False):
    opts, ans = _shuffle_options(
        [q["options"][k] for k in ("A", "B", "C", "D")], "ABCD".index(q["answer"]), qid)
    out = {"id": qid, "task": q["task"], "domain": q["domain"], "prompt": q["q"],
           "options": opts, "answer": ans, "why": q["why"]}
    if with_ref:
        out["ref"] = q["ref"]
    return out


def build_questions():
    out = [_convert(q, f"q{i}") for i, q in enumerate(OFFICIAL_SAMPLES, 1)]
    out += [_convert(q, f"p{i}") for i, q in enumerate(PRACTICE, 1)]
    return out


def build_mock():
    return [_convert(q, f"m{i}", with_ref=True) for i, q in enumerate(MOCK_BANK, 1)]


def build_tasks(questions):
    q_by_task = {}
    for q in questions:
        q_by_task.setdefault(q["task"], []).append(q["id"])
    tasks = []
    for l in LESSONS:
        chat = [{"who": m["who"], **({"label": m["label"]} if m.get("label") else {}),
                 "text": m["text"]} for m in l["chat"]]
        tasks.append({
            "id": l["id"], "d": l["d"], "title": l["title"], "concept": l["concept"],
            "antipattern": l["antipattern"], "right": l["right"], "tip": l["tip"],
            "analogy": l.get("analogy", ""), "pitfall": l.get("pitfall", ""),
            "chat": chat, "q": q_by_task.get(l["id"], []), "links": l.get("links", []),
        })
    return tasks


def build_cheat():
    return [{"d": d, "fact": fact, "task": task} for d, fact, task in FACTS]


def _length_bias(items):
    """(share of items whose correct option is the longest, mean correct/distractor ratio)."""
    longest = sum(1 for q in items
                  if len(q["options"][q["answer"]]) == max(len(o) for o in q["options"]))
    correct = [len(q["options"][q["answer"]]) for q in items]
    others = [len(o) for q in items
              for i, o in enumerate(q["options"]) if i != q["answer"]]
    return longest / len(items), (sum(correct) / len(correct)) / (sum(others) / len(others))


def validate(tasks, questions, mock, cheat):
    errors = []
    warnings = []
    task_ids = {t["id"] for t in tasks}
    domain_ids = {d["id"] for d in DOMAINS}

    if len(tasks) != 30:
        errors.append(f"expected 30 lessons, found {len(tasks)}")
    if len({t["id"] for t in tasks}) != len(tasks):
        errors.append("duplicate lesson ids")
    per_dom = {d: sum(1 for t in tasks if t["d"] == d) for d in domain_ids}
    if per_dom != LESSONS_PER_DOMAIN:
        errors.append(f"lessons per domain {per_dom} != blueprint {LESSONS_PER_DOMAIN}")

    for t in tasks:
        if t["d"] not in domain_ids:
            errors.append(f"lesson {t['id']}: unknown domain {t['d']}")
        if not t["q"]:
            errors.append(f"lesson {t['id']}: no quiz question mapped")
        if not t["chat"]:
            errors.append(f"lesson {t['id']}: empty chat walkthrough")
        for m in t["chat"]:
            if m["who"] not in CHAT_WHO:
                errors.append(f"lesson {t['id']}: bad chat role {m['who']!r}")
        for k in ("concept", "antipattern", "right", "tip"):
            if not t[k]:
                errors.append(f"lesson {t['id']}: empty {k}")
        for link in t["links"]:
            if link not in task_ids:
                errors.append(f"lesson {t['id']}: broken link {link}")

    all_qs = questions + mock
    if len({q["id"] for q in all_qs}) != len(all_qs):
        errors.append("duplicate question ids")
    for q in all_qs:
        if q["task"] not in task_ids:
            errors.append(f"question {q['id']}: unknown task {q['task']}")
        if q["domain"] not in domain_ids:
            errors.append(f"question {q['id']}: unknown domain {q['domain']}")
        if q["domain"] != "d" + q["task"].split(".")[0]:
            errors.append(f"question {q['id']}: domain {q['domain']} mismatches task {q['task']}")
        if len(q["options"]) != 4:
            errors.append(f"question {q['id']}: expected 4 options")
        if not (0 <= q["answer"] < len(q["options"])):
            errors.append(f"question {q['id']}: answer index out of range")

    if len(mock) != 60:
        errors.append(f"expected 60 mock questions, found {len(mock)}")
    mock_dist = {d: sum(1 for q in mock if q["domain"] == d) for d in domain_ids}
    if mock_dist != MOCK_DISTRIBUTION:
        errors.append(f"mock distribution {mock_dist} != blueprint {MOCK_DISTRIBUTION}")

    for c in cheat:
        if c["task"] not in task_ids:
            errors.append(f"cheat fact: unknown task {c['task']}")
        if c["d"] not in domain_ids:
            errors.append(f"cheat fact: unknown domain {c['d']}")

    if sum(d["weight"] for d in DOMAINS) != 100:
        errors.append("domain weights do not sum to 100")

    for s in SCENARIOS:
        for st in s["steps"]:
            if st["task"] not in task_ids:
                errors.append(f"scenario {s['id']}: step references unknown task {st['task']}")
        for d in s["domains"]:
            if d not in domain_ids:
                errors.append(f"scenario {s['id']}: unknown domain {d}")

    # Option length must not give the answer away: a candidate who always picks the
    # longest option should score no better than chance (25%).
    share, ratio = _length_bias(mock)
    if share > 0.45:
        errors.append(f"mock: correct option is the longest in {share:.0%} of items (max 45%) "
                      "— answer length is a tell")
    if ratio > 1.15:
        errors.append(f"mock: correct options average {ratio:.2f}x distractor length (max 1.15x)")
    q_share, q_ratio = _length_bias(questions)
    if q_share > 0.45 or q_ratio > 1.15:
        warnings.append(f"practice quiz: correct option is the longest in {q_share:.0%} of items "
                        f"at {q_ratio:.2f}x distractor length — same tell, not yet rebalanced")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    for w in warnings:
        print(f"  WARNING: {w}")


def js(obj):
    return json.dumps(obj, ensure_ascii=False)


def render(tasks, questions, cheat, mock):
    P = []
    P.append("/* CCAF Exam Prep Console — content model (Claude Certified Associate – Foundations).")
    P.append("   AUTO-GENERATED by ui/console-associate/build_data.py from associate/content/*.")
    P.append("   Do not edit by hand; edit the content modules and regenerate. */")
    P.append("(function () {")
    P.append("  const domains = " + js(DOMAINS) + ";")
    P.append("  const themes = " + js(THEMES) + ";")
    P.append("")
    P.append("  const tasks = [")
    for t in tasks:
        P.append("    " + js(t) + ",")
    P.append("  ];")
    P.append("")
    P.append("  const scenarios = " + js(SCENARIOS) + ";")
    P.append("  const questions = " + js(questions) + ";")
    P.append("  const cheat = " + js(cheat) + ";")
    P.append("  const mock = " + js(mock) + ";")
    P.append("")
    P.append("  window.CCAF = { domains, themes, tasks, scenarios, questions, cheat, mock,")
    P.append("    taskById: Object.fromEntries(tasks.map((t) => [t.id, t])),")
    P.append("    questionById: Object.fromEntries(questions.map((q) => [q.id, q])),")
    P.append("    domainById: Object.fromEntries(domains.map((d) => [d.id, d])),")
    P.append("  };")
    P.append("})();")
    return "\n".join(P) + "\n"


def main():
    questions = build_questions()
    mock = build_mock()
    tasks = build_tasks(questions)
    cheat = build_cheat()
    validate(tasks, questions, mock, cheat)
    out = render(tasks, questions, cheat, mock)
    dest = os.path.join(HERE, "assets", "data.js")
    open(dest, "w", encoding="utf-8").write(out)
    print(f"wrote {os.path.relpath(dest, REPO)}  ({len(out)//1024} KB)")
    print(f"lessons: {len(tasks)} · questions: {len(questions)} · mock: {len(mock)} · "
          f"cheat: {len(cheat)} · scenarios: {len(SCENARIOS)}")


if __name__ == "__main__":
    main()
