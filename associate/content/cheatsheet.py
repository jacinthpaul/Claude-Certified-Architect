"""
associate/content/cheatsheet.py — high-yield facts for the CCAO-F exam
======================================================================
Grouped by domain; each fact links to the lesson (task id) that teaches it.
Format: (domain_id, fact, task_id)
"""

FACTS = [
    # Exam logistics live on the dashboard/README; these facts map to the blueprint.

    # ---- Domain 1 · Prompting and Task Execution (14%) ----
    ("d1", "Effective prompt = context + role/audience + task + constraints + output format. "
           "The best exam option adds specifics — never just 'be more detailed'.", "1.1"),
    ("d1", "Complex deliverables: decompose into sequenced steps WITH human review between "
           "them — beats both one mega-prompt and blind prompt-chaining.", "1.2"),
    ("d1", "Iterate with anchored, directional feedback (keep X, change Y, because Z). "
           "'Make it better' regenerates the good parts away.", "1.3"),
    ("d1", "Match prompt shape to task type: brainstorm = many unfiltered ideas, judgment "
           "deferred; analysis = explicit criteria + structure; research = scope + sources; "
           "drafting = audience + tone + format.", "1.4"),

    # ---- Domain 2 · Output Evaluation and Validation (21% — heaviest domain) ----
    ("d2", "Evaluate every output on TWO axes: accuracy (check present claims against the "
           "source) and completeness (check coverage against the request — omissions hide).", "2.1"),
    ("d2", "Specificity is not credibility: confident citations, statistics, and section "
           "numbers are exactly what hallucinations look like.", "2.2"),
    ("d2", "Self-reported confidence is NEVER a validation signal. Verify against an "
           "authoritative external source — the official sample answer.", "2.3"),
    ("d2", "Match validation to claim type: citation → open the source; statistic → "
           "recompute/trace; legal-regulated → official text + expert. Effort scales with stakes.", "2.3"),
    ("d2", "Mandatory human review is triggered by CATEGORY (legal, medical, financial, HR, "
           "external, contractual, irreversible), not by how good the output looks.", "2.4"),
    ("d2", "Iterating with Claude ≠ review. Ten refinement rounds is still zero qualified "
           "human eyes.", "2.4"),
    ("d2", "Audience adaptation changes depth and framing but must never ADD claims the "
           "source doesn't support.", "2.5"),
    ("d2", "Format follows downstream use: updated/shared → artifact; imported/analyzed → "
           "structured data (table/CSV); quick answer → inline.", "2.6"),

    # ---- Domain 3 · Product and Model Selection (12%) ----
    ("d3", "Feature cues: recurring context → Project; current/cited info → research mode; "
           "shareable evolving deliverable → artifact; one-off → chat. Features compose.", "3.1"),
    ("d3", "Haiku = fastest/most economical (high-volume, well-defined); Sonnet = balanced "
           "everyday default; Opus = most capable (complex reasoning, highest cost/latency).", "3.2"),
    ("d3", "Official sample: high-volume, speed/cost-sensitive replies → faster, lower-cost "
           "model. 'Most capable everywhere' is always the distractor.", "3.3"),
    ("d3", "Requirements first, then the cheapest model that clears the bar; a human review "
           "step lowers the model-quality floor a task needs.", "3.3"),
    ("d3", "Long chat degrading / early instructions lost = context limit, not model fault: "
           "summarize + fresh chat; durable context → Project instructions/knowledge.", "3.4"),

    # ---- Domain 4 · Workflow Integration and Solution Design (16%) ----
    ("d4", "Vague request? Analysis before artifact: surface requirements, stakeholders, "
           "constraints, and acceptance criteria — then produce.", "4.1"),
    ("d4", "Claude's process recommendations are hypotheses — validate with the people who "
           "run the process before adopting.", "4.2"),
    ("d4", "Solution design arc: options with trade-offs → select by criteria → pilot → "
           "iterate on evidence. Never first-suggestion-to-production.", "4.3"),
    ("d4", "Integrate AI at drudgery steps (draft, summarize, classify, structure); humans "
           "keep judgment steps (approve, decide, hire, settle) and quality gates.", "4.4"),
    ("d4", "Stakeholder credibility = measured value WITH evidence + named limitations WITH "
           "mitigations. Tell the failure story yourself.", "4.5"),

    # ---- Domain 5 · Configuration and Knowledge Management (12%) ----
    ("d5", "Projects: instructions = HOW to work (stable rules); knowledge = WHAT to know "
           "(reference docs). Team repeats context every chat → configure a Project.", "5.1"),
    ("d5", "Uploads are frozen snapshots; connectors (Drive, Gmail) read current content. "
           "Changes weekly → connector, scoped to the needed folder; delete stale uploads.", "5.2"),
    ("d5", "Good instructions are specific and testable: 'answer only from Project docs, cite "
           "doc + section, escalate named categories'. Adjectives are not rules.", "5.3"),
    ("d5", "Stale-Project symptoms need a maintenance system: named owner, event-triggered "
           "updates, periodic sweep, visible versioning — not a bigger model.", "5.4"),

    # ---- Domain 6 · Governance, Risk, and Responsible Use (15%) ----
    ("d6", "Use-case screen: What if it's wrong? Who reviews before impact? Is the data "
           "allowed? Who is accountable? AI assists judgment; it doesn't replace it.", "6.1"),
    ("d6", "Official sample: regulated identifiers → remove/anonymize BEFORE upload, per "
           "policy. 'It's internal', 'tell it not to retain', and 'skip the task' are the "
           "distractors.", "6.2"),
    ("d6", "Minimize by default: share only the fields the task needs; the analysis usually "
           "survives anonymization intact.", "6.2"),
    ("d6", "Policy inconvenient? Comply-then-escalate through governance. Undefined ≠ "
           "approved; personal-account workarounds = shadow AI.", "6.3"),
    ("d6", "Ethics beyond policy: check outputs across groups for bias, disclose AI "
           "involvement where it matters, keep a named human accountable for every "
           "consequential output.", "6.4"),

    # ---- Domain 7 · Troubleshooting and Optimization (10%) ----
    ("d7", "Diagnose before fixing: wrong facts → context/knowledge gap; wrong focus → "
           "ambiguity; wrong shape → format unstated; ignores rules in long chat → context "
           "overflow. Change ONE variable, re-test same input.", "7.1"),
    ("d7", "'Worked for months, now fails' → an INPUT changed (export format, stale doc), "
           "not the model. Find what changed.", "7.1"),
    ("d7", "Triage feedback by frequency × impact: systematic edit-patterns outrank loud "
           "n=1 anecdotes; explicitly protect what already works.", "7.2"),
    ("d7", "Optimize by removing redundancy (Project context, batching, right-sized models, "
           "review focused on flagged risk) — with the quality metric visible BEFORE the "
           "change. Never optimize away the safety net.", "7.3"),
]
