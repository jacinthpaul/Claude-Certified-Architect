"""
associate/content/scenarios.py — 6 end-to-end business scenarios for the CCAO-F console
========================================================================================
Fuller workflows that compose the lesson concepts, mirroring how the exam frames
its scenario questions. Each step links to the lesson (task id) that teaches it.
"""

SCENARIOS = [
    {"id": "s1", "n": 1, "title": "Product Launch Content Pipeline", "domains": ["d1", "d2", "d3"],
     "summary": "A marketing team turns one launch brief into a full content suite — decomposed "
                "into steps, drafted per audience, fact-checked before anything ships, and "
                "delivered in the right formats.",
     "steps": [
        {"t": "Brief as prompt", "d": "Audience, tone, constraints, and format stated up front.", "task": "1.1"},
        {"t": "Decompose the suite", "d": "Blog → email → social → FAQ as sequenced, reviewed steps.", "task": "1.2"},
        {"t": "Audience variants", "d": "One fact set adapted for execs, customers, and press.", "task": "2.5"},
        {"t": "Verify the claims", "d": "Every stat and product claim checked against the fact sheet.", "task": "2.3"},
        {"t": "Right formats", "d": "Artifacts for the evolving docs, tables for the channel plan.", "task": "2.6"},
        {"t": "Right model", "d": "Fast model for social variants; capable model for the launch post.", "task": "3.3"}]},
    {"id": "s2", "n": 2, "title": "Ops Process Redesign with a Claude Project", "domains": ["d4", "d5", "d7"],
     "summary": "An operations lead maps a slow onboarding process, uses Claude to find the "
                "bottlenecks, validates with the process owners, and ships the redesign backed "
                "by a maintained Project.",
     "steps": [
        {"t": "Analyze the process", "d": "Bottlenecks, redundancies, and handoff risks from the step map.", "task": "4.2"},
        {"t": "Validate with owners", "d": "Documented process ≠ real process — humans confirm dependencies.", "task": "4.1"},
        {"t": "Project setup", "d": "SOPs and templates become instructions + knowledge.", "task": "5.1"},
        {"t": "Integrate the steps", "d": "AI drafts and summarizes; humans keep approval gates.", "task": "4.4"},
        {"t": "Measure and adjust", "d": "Before/after cycle time; feedback drives the next iteration.", "task": "7.2"}]},
    {"id": "s3", "n": 3, "title": "Compliance-Safe Customer Data Analysis", "domains": ["d6", "d2", "d1"],
     "summary": "A PM needs churn insights from a spreadsheet full of regulated personal data — "
                "the analysis proceeds through minimization, policy compliance, verified findings, "
                "and a clean escalation boundary.",
     "steps": [
        {"t": "Classify the data", "d": "Names and account numbers are regulated — policy decides handling.", "task": "6.2"},
        {"t": "Minimize, then upload", "d": "Identifiers stripped; sequential IDs preserve repeat-analysis.", "task": "6.2"},
        {"t": "Policy check", "d": "Approved tool, permitted data class, documented approach.", "task": "6.3"},
        {"t": "Analysis prompt", "d": "Explicit criteria: patterns by region, plan, and stated reason.", "task": "1.4"},
        {"t": "Verify the findings", "d": "Spot-check claimed patterns against the raw rows.", "task": "2.1"},
        {"t": "Escalate re-identification", "d": "Contacting flagged customers happens in controlled systems.", "task": "2.4"}]},
    {"id": "s4", "n": 4, "title": "Executive Communications Pipeline", "domains": ["d1", "d2", "d5"],
     "summary": "A chief-of-staff workflow: one incident, three audiences, zero unverified claims — "
                "powered by a comms Project with standing instructions and iterated to the "
                "executive's voice.",
     "steps": [
        {"t": "Comms Project", "d": "Voice guide, org facts, and format rules configured once.", "task": "5.3"},
        {"t": "Draft by task type", "d": "Analysis mode for the briefing; drafting mode for the notes.", "task": "1.4"},
        {"t": "Audience adaptation", "d": "Exec summary, all-hands note, and board line from one source.", "task": "2.5"},
        {"t": "No added claims", "d": "Adaptation never invents reassurance the source doesn't support.", "task": "2.2"},
        {"t": "Iterate to voice", "d": "Anchored feedback: keep structure, match the exec's register.", "task": "1.3"}]},
    {"id": "s5", "n": 5, "title": "Competitive Research with Research Mode", "domains": ["d3", "d2", "d4"],
     "summary": "A strategy associate builds a competitor briefing on current, cited information — "
                "research mode for freshness, source verification before circulation, and a "
                "stakeholder-ready synthesis.",
     "steps": [
        {"t": "Feature fit", "d": "Current events need research mode, not training-data recall.", "task": "3.1"},
        {"t": "Scoped research prompt", "d": "Named competitors, time window, and sourcing requirements.", "task": "1.1"},
        {"t": "Verify citations", "d": "Claimed announcements checked at the cited sources.", "task": "2.3"},
        {"t": "Synthesize for decision", "d": "Findings organized into a comparison the exec team can act on.", "task": "2.6"},
        {"t": "Value and limits", "d": "Briefing states freshness bounds and what wasn't verifiable.", "task": "4.5"}]},
    {"id": "s6", "n": 6, "title": "Rescuing an Underperforming Workflow", "domains": ["d7", "d3", "d5"],
     "summary": "A once-good reporting workflow has degraded — diagnosis separates prompt, "
                "knowledge, and context failures; targeted fixes and a feedback loop bring it "
                "back cheaper than it started.",
     "steps": [
        {"t": "Reproduce and classify", "d": "Fabricated targets → context gap; scope drift → underspecification.", "task": "7.1"},
        {"t": "Fix the knowledge", "d": "Stale snapshot replaced; update triggers assigned an owner.", "task": "5.4"},
        {"t": "Restart the context", "d": "Summarize the mega-chat; durable constraints move to the Project.", "task": "3.4"},
        {"t": "Adjust from feedback", "d": "Edit-rate patterns prioritized over loud anecdotes.", "task": "7.2"},
        {"t": "Optimize the flow", "d": "Batching, templates, and right-sized models — quality gauge on.", "task": "7.3"}]},
]
