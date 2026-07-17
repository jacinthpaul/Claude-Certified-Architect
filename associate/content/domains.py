"""
associate/content/domains.py — the 7 CCAO-F exam domains + cross-cutting themes
===============================================================================
Source of truth: the official Claude Certified Associate – Foundations Exam Guide
(v1.0, July 2026). Weights are the official blueprint weights; blurbs are ours.

Consumed by ui/console-associate/build_data.py.
"""

DOMAINS = [
    {"id": "d1", "n": 1, "title": "Prompting and Task Execution", "short": "Prompting",
     "weight": 14,
     "blurb": "Write prompts that carry context, role, format, and constraints; decompose "
              "big requests into steps; iterate instead of settling; and match the prompting "
              "style to analysis, research, drafting, or brainstorming."},
    {"id": "d2", "n": 2, "title": "Output Evaluation and Validation", "short": "Evaluation",
     "weight": 21,
     "blurb": "The heaviest domain: judge accuracy and completeness, spot hallucinations and "
              "bias, verify claims against authoritative sources, know when a human must "
              "review, adapt outputs for the audience, and pick the right output format."},
    {"id": "d3", "n": 3, "title": "Product and Model Selection", "short": "Products & Models",
     "weight": 12,
     "blurb": "Chat vs Projects vs research mode vs artifacts; Haiku vs Sonnet vs Opus; "
              "balancing cost, speed, and quality; and managing context windows — when to "
              "restart, summarize, or persist."},
    {"id": "d4", "n": 4, "title": "Workflow Integration and Solution Design", "short": "Workflows",
     "weight": 16,
     "blurb": "Use Claude to analyze requirements, research and plan, design and iterate on "
              "solutions, weave AI into existing processes, and explain its value and limits "
              "to stakeholders."},
    {"id": "d5", "n": 5, "title": "Configuration and Knowledge Management", "short": "Projects & Knowledge",
     "weight": 12,
     "blurb": "Configure Claude Projects with instructions and knowledge sources, manage "
              "uploads and connectors like Google Drive and Gmail, write system-level "
              "instructions, and keep all of it current."},
    {"id": "d6", "n": 6, "title": "Governance, Risk, and Responsible Use", "short": "Governance",
     "weight": 15,
     "blurb": "Which use cases are appropriate, how to handle sensitive and regulated data, "
              "following organizational AI policy, and the ethics of using AI at work."},
    {"id": "d7", "n": 7, "title": "Troubleshooting and Optimization", "short": "Troubleshooting",
     "weight": 10,
     "blurb": "Diagnose why a prompt underperforms, fix the actual cause, adjust based on "
              "feedback, and streamline workflows so they stay fast, cheap, and reliable."},
]

THEMES = [
    {"id": "t1", "title": "Trust, but verify",
     "body": "Claude's output is a strong first draft, never a finished fact. Anything that "
             "leaves your desk — numbers, citations, legal or compliance claims — gets checked "
             "against an authoritative source first. Self-reported confidence is not a signal."},
    {"id": "t2", "title": "Match the tool to the task",
     "body": "Model and feature choice is a cost/speed/quality trade-off: fast, cheap models "
             "for high-volume routine work; the most capable models for deep reasoning. Same "
             "for features — chat for one-offs, Projects for recurring context, research mode "
             "for sourced answers, artifacts for shareable deliverables."},
    {"id": "t3", "title": "Know when to escalate",
     "body": "Associates deliver business workflows — and recognize the boundary. Regulated "
             "data follows policy, high-stakes outputs get human review, and API builds, "
             "integrations, and agentic systems go to Claude Architects and Developers."},
]
