"""
associate/content/questions.py — lesson quiz pool for the CCAO-F console
========================================================================
OFFICIAL_SAMPLES: the 3 illustrative items published verbatim in Section 8 of
the official Claude Certified Associate – Foundations Exam Guide (with their
published rationale, reworded letter-free so options can be shuffled).

PRACTICE: 27 authored, exam-style questions — one for each blueprint objective
the official samples do not cover, so every lesson has a completion question.
Scenario-framed, one best answer, three plausible distractors mirroring the
exam's recurring traps (trust the model's confidence, skip verification,
over- or under-use the tool, bypass policy). Study aids, NOT official items.

The console gives officials ids q1..q3 and practice p1..p27.
"""

# Each: task, domain, q, options A-D, answer letter, why (letter-free).

OFFICIAL_SAMPLES = [
    dict(task="2.3", domain="d2",
         q="An associate asks Claude to summarize a new regulation, and Claude produces a "
           "confident summary citing a specific subsection number. Before sending the summary "
           "to the compliance team, what is the most appropriate action?",
         options={
             "A": "Send it as-is, since Claude expressed high confidence.",
             "B": "Verify the cited subsection against the official regulation text before sharing.",
             "C": "Ask Claude to rate its own confidence and send it if the rating is high.",
             "D": "Reword the summary to sound more formal, then send it.",
         },
         answer="B",
         why="Language models can fabricate specific-looking details such as citation numbers — "
             "a hallucination. Validating factual claims, especially citations bound for a "
             "compliance audience, against an authoritative source is the diligence step "
             "required. Self-reported confidence is not a reliable accuracy signal, and "
             "reformatting does not address correctness."),
    dict(task="3.3", domain="d3",
         q="An associate needs to generate a high volume of short customer-reply drafts where "
           "speed and cost matter more than deep reasoning. Which choice best fits the task?",
         options={
             "A": "Use the most capable, highest-cost model for every reply to maximize quality.",
             "B": "Use a faster, lower-cost model suited to straightforward, high-volume tasks.",
             "C": "Disable all product features to reduce cost.",
             "D": "Switch to a different AI platform.",
         },
         answer="B",
         why="Aligning model selection with task requirements means matching a faster, "
             "lower-cost model to straightforward, high-volume work, reserving the most "
             "capable model for complex reasoning. Always using the top model wastes the cost "
             "and latency budget; disabling features or switching platforms does not address "
             "the trade-off."),
    dict(task="6.2", domain="d6",
         q="A project manager wants to upload a spreadsheet containing customer names and "
           "account numbers so Claude can analyze trends. Organizational policy restricts "
           "sharing regulated personal data. What is the most appropriate action?",
         options={
             "A": "Upload the file as-is, since the analysis is internal.",
             "B": "Remove or anonymize the personal identifiers before uploading, consistent with policy.",
             "C": "Upload the file but instruct Claude not to retain it.",
             "D": "Skip the analysis entirely.",
         },
         answer="B",
         why="Applying data-sensitivity and privacy safeguards means redacting or anonymizing "
             "regulated identifiers before use, so the analysis can proceed without exposing "
             "protected data. Uploading as-is violates policy; instructing the model not to "
             "retain data does not satisfy the policy control; and abandoning the task is "
             "unnecessary when anonymization enables it."),
]

PRACTICE = [
    # ---------------- Domain 1 — Prompting and Task Execution ----------------
    dict(task="1.1", domain="d1",
         q="A marketing associate asks Claude to 'summarize this report' and receives an "
           "accurate but generic 600-word summary that is useless for their 5-minute "
           "leadership briefing. What is the most effective revision?",
         options={
             "A": "State audience, purpose, focus, length, and format — '5 bullets for the "
                  "COO, on risks.'",
             "B": "Ask Claude to 'be more detailed and professional' and regenerate the "
                  "summary again.",
             "C": "Run the same prompt several times and combine the best parts of each "
                  "summary.",
             "D": "Switch to a more capable model, since the summary quality was clearly "
                  "too low.",
         },
         answer="A",
         why="The output was generic because the requirements — audience, purpose, focus, "
             "length, format — existed only in the associate's head. Effective prompts state "
             "them explicitly. Vague quality adjectives, regenerate-and-hope, and a bigger "
             "model all fail to supply the missing requirements."),
    dict(task="1.2", domain="d1",
         q="An operations lead needs a full analysis-and-recommendation pack for a warehouse "
           "migration: risks, timeline, and comms plan. What is the most reliable way to get "
           "a high-quality result from Claude?",
         options={
             "A": "Write one very detailed prompt requesting all three deliverables at "
                  "once, so nothing is lost.",
             "B": "Sequence the steps — risks, then timeline, then comms — reviewing each "
                  "output.",
             "C": "Ask for all three in one prompt, then regenerate repeatedly until the "
                  "combined output looks right.",
             "D": "Chain the three prompts automatically so each output flows into the next "
                  "without a pause.",
         },
         answer="B",
         why="Complex deliverables degrade in single mega-prompts, and errors in early parts "
             "poison later ones. Decomposition with a human checkpoint between steps keeps "
             "each output verifiable and grounds the next step in reviewed material. Chaining "
             "without review is the mega-prompt failure with extra steps."),
    dict(task="1.3", domain="d1",
         q="Claude's first draft of a policy announcement has the right structure but the "
           "wrong tone and too much length. The associate replies 'make it better' and gets "
           "a completely different draft — losing the structure that worked. What should "
           "they have done instead?",
         options={
             "A": "Anchored feedback: keep the structure, halve the length, shift the tone; "
                  "say why.",
             "B": "Start a fresh chat and rewrite the original prompt from scratch, with "
                  "much more detail.",
             "C": "Regenerate several drafts from the same prompt and pick whichever one of "
                  "them reads best.",
             "D": "Accept the first draft and edit it by hand, since iteration changes too "
                  "much.",
         },
         answer="A",
         why="Effective iteration names what to keep and what to change, with direction. "
             "Undirected feedback ('make it better') changes everything, including the good "
             "parts. Restarting or manual-only editing forfeits the model's ability to "
             "converge quickly when given specific feedback."),
    dict(task="1.4", domain="d1",
         q="An HR lead wants to explore ways to improve onboarding and asks Claude 'What is "
           "the best way to improve our onboarding process?' — getting one safe, generic "
           "recommendation. What went wrong?",
         options={
             "A": "The model is too small for creative work; a more capable one would list "
                  "more options.",
             "B": "The prompt used an analysis shape for a brainstorming task; ask for many "
                  "diverse ideas.",
             "C": "Nothing — a single best-practice answer is the correct output for this "
                  "request.",
             "D": "The prompt was too short; adding company background would have produced "
                  "more ideas.",
         },
         answer="B",
         why="Brainstorming needs divergent prompting — quantity, variety, no premature "
             "filtering — while 'what is the best way' invites convergence to one answer. "
             "Matching prompt shape to task type (analysis, research, drafting, brainstorming) "
             "is the skill being tested; model size and prompt length are not the issue."),

    # ---------------- Domain 2 — Output Evaluation and Validation ----------------
    dict(task="2.1", domain="d2",
         q="Claude produces a fluent, well-formatted summary of a quarterly spreadsheet for a "
           "team update. What is the most appropriate evaluation before using it?",
         options={
             "A": "Check that the tone and formatting are appropriate for the team "
                  "audience.",
             "B": "Verify each figure against the spreadsheet and check the summary covers "
                  "the request.",
             "C": "Ask Claude whether it is confident in the summary, and proceed on the "
                  "strength of that.",
             "D": "Have Claude regenerate the summary and compare whether the two versions "
                  "agree closely.",
         },
         answer="B",
         why="Evaluation is two questions: is what's present accurate (check against the "
             "source), and is anything missing (check against the request)? Fluency and "
             "formatting are not accuracy signals, self-reported confidence is unreliable, "
             "and two generations can agree on the same error."),
    dict(task="2.2", domain="d2",
         q="In a market analysis, Claude writes: 'A 2024 Gartner study found that 73% of "
           "mid-market firms adopted AI assistants.' The associate has never seen this study. "
           "What is the appropriate response to this level of specificity?",
         options={
             "A": "Treat the specificity as a credibility signal — invented numbers are "
                  "rarely that precise.",
             "B": "Treat the citation as a checkable claim: verify the study exists and "
                  "says this.",
             "C": "Round the number to 'about 70%', so the claim is safer to publish "
                  "without a source.",
             "D": "Ask Claude to confirm the source, and keep the claim if it provides "
                  "further details.",
         },
         answer="B",
         why="Hallucinated details are dangerous precisely because they are specific and "
             "fluent — specificity is not verification. Checkable specifics (named studies, "
             "percentages, section numbers) must be verified externally; softening the number "
             "or asking the model to confirm its own claim does not validate anything."),
    dict(task="2.4", domain="d2",
         q="An associate used Claude to draft revised liability wording for a customer "
           "contract. The draft looks excellent and the deal closes tomorrow, but Legal's "
           "review queue is a week long. What should the associate do?",
         options={
             "A": "Send the clause — it was refined over several careful iterations with "
                  "Claude already.",
             "B": "Get qualified human review anyway: contract terms are a mandatory review "
                  "category.",
             "C": "Ask Claude to double-check the clause against common legal standards, "
                  "and then send.",
             "D": "Remove the clause from the contract entirely so that no review is "
                  "needed.",
         },
         answer="B",
         why="Binding, external, irreversible content — contracts, legal, regulated "
             "communications — requires qualified human review triggered by the CATEGORY, not "
             "by apparent quality. Iteration with the model is not review; model self-checks "
             "are not legal judgment; and deleting negotiated terms to dodge review harms the "
             "deal."),
    dict(task="2.5", domain="d2",
         q="A manager has a technical incident postmortem and must inform executives, "
           "customers, and engineers. While adapting the customer version, Claude adds 'no "
           "customer data was affected' — a claim the postmortem never addresses. What does "
           "this illustrate?",
         options={
             "A": "Adaptation may change depth and framing, but never add claims the source "
                  "lacks.",
             "B": "Customer communications should always include reassurance, so the "
                  "addition fits.",
             "C": "The three versions should be merged into one document to avoid "
                  "inconsistencies.",
             "D": "Technical content should not be adapted for non-technical audiences at "
                  "all.",
         },
         answer="A",
         why="Adapting for an audience means translating the same facts, not inventing "
             "friendlier ones. Reassuring claims about data safety are exactly the kind of "
             "addition that must be verified with the source team or cut. One-size-fits-all "
             "documents and refusing adaptation both fail the audiences."),
    dict(task="2.6", domain="d2",
         q="A procurement analyst asks Claude to compare three vendors and receives four "
           "paragraphs of prose. The comparison will be imported into a tracking sheet and "
           "updated after each demo call. What should the analyst request?",
         options={
             "A": "A shorter prose summary that is easier for the team to skim quickly.",
             "B": "A criteria-by-vendor table plus a CSV, kept as an artifact for updating.",
             "C": "The same prose, but with bold headings introducing each of the vendors.",
             "D": "A separate chat for each vendor, to keep the details cleanly organized.",
         },
         answer="B",
         why="Format follows downstream use: comparison → table; import → structured data "
             "(CSV); updated-and-shared deliverable → artifact. Prose in any styling defeats "
             "comparison and import, and splitting vendors across chats makes comparison "
             "harder still."),

    # ---------------- Domain 3 — Product and Model Selection ----------------
    dict(task="3.1", domain="d3",
         q="A marketing associate rebuilds the same setup in every chat — pasting the "
           "positioning doc, competitor list, and tone guide — and also needs each weekly "
           "update to reflect this week's competitor announcements. Which feature combination "
           "fits?",
         options={
             "A": "A saved mega-prompt containing all the context, pasted into each new "
                  "chat.",
             "B": "A Project holding the durable context, with research mode used inside "
                  "it.",
             "C": "One continuous chat that accumulates the context and all the weekly "
                  "updates.",
             "D": "Research mode alone, since current information is the priority every "
                  "week.",
         },
         answer="B",
         why="Recurring context belongs in a Project (instructions + knowledge, set once); "
             "current sourced facts need research mode; the features compose. A pasted "
             "mega-prompt still repeats setup and drifts, an eternal chat hits context "
             "limits, and research mode alone re-loses the durable context weekly."),
    dict(task="3.2", domain="d3",
         q="A support team runs two jobs: drafting first-reply suggestions for ~2,000 routine, "
           "human-reviewed tickets per day, and a quarterly root-cause analysis of six months "
           "of escalation data for executives. How should models be assigned?",
         options={
             "A": "The most capable model for both — support quality should never be "
                  "compromised.",
             "B": "A fast, economical model for the reviewed drafts; the capable one for "
                  "analysis.",
             "C": "The economical model for both, since the reviewed drafts prove it is "
                  "adequate.",
             "D": "A mid-tier model for both, as a compromise between the two workloads' "
                  "needs.",
         },
         answer="B",
         why="Model families trade capability against speed and cost. High-volume, "
             "well-defined, human-reviewed work fits the fast economical tier; low-volume, "
             "genuinely complex, high-stakes reasoning justifies the most capable tier. "
             "One-size assignments overpay on one job or underserve the other."),
    dict(task="3.4", domain="d3",
         q="After three weeks in one continuous chat, Claude drafts a counter-offer using the "
           "wrong walk-away price — a constraint set on day one. Quality has been degrading "
           "for days. What is the appropriate fix?",
         options={
             "A": "Retype the walk-away price into the same chat, in capital letters, and "
                  "carry on.",
             "B": "Summarize the constraints into Project knowledge and continue in fresh "
                  "chats.",
             "C": "Report the model as faulty and switch tools for the rest of the "
                  "negotiation.",
             "D": "Scroll up and quote the original message so that Claude can see it "
                  "again.",
         },
         answer="B",
         why="Long conversations exceed the effective context window: early details drop out "
             "and quality degrades. The structural fix is summarize-and-restart with durable "
             "context persisted in a Project. Re-typing into the overloaded chat treats the "
             "symptom, and the behavior is a context limitation, not a defect."),

    # ---------------- Domain 4 — Workflow Integration and Solution Design ----------------
    dict(task="4.1", domain="d4",
         q="Leadership sends a one-line request: 'We need an AI chatbot for HR.' What is the "
           "most valuable first use of Claude?",
         options={
             "A": "Draft the full project plan immediately, so leadership sees fast "
                  "progress.",
             "B": "Surface the unanswered requirements — users, tasks, boundaries, success "
                  "metrics.",
             "C": "Research which chatbot vendor has the best reviews and pricing on the "
                  "market.",
             "D": "Build a prototype in a Project so stakeholders have something to react "
                  "to.",
         },
         answer="B",
         why="A plan built on a one-line requirement encodes guesses as commitments. Claude's "
             "highest-leverage first use is requirements analysis: surfacing unknowns, "
             "stakeholders, constraints, and testable acceptance criteria for humans to "
             "confirm. Plans, vendors, and prototypes all come after the problem is defined."),
    dict(task="4.2", domain="d4",
         q="An ops lead gives Claude the documented 14-step onboarding process and asks for "
           "bottleneck analysis. Claude proposes re-ordering steps 4–6, projecting five days "
           "saved. What should happen before the change is adopted?",
         options={
             "A": "Adopt it — the analysis was based directly on the official process "
                  "documentation.",
             "B": "Validate it with the people who run those steps; docs omit real "
                  "dependencies.",
             "C": "Ask Claude to redo the analysis on a more capable model, to be "
                  "completely certain.",
             "D": "Pilot the change quietly, to avoid biasing the team's feedback on it.",
         },
         answer="B",
         why="Claude reasons from the documented process; reality often contains undocumented "
             "dependencies (systems, policies, sequencing constraints). Process "
             "recommendations are hypotheses until validated with the people who operate the "
             "process. Re-running with a bigger model re-derives the same blind spot."),
    dict(task="4.3", domain="d4",
         q="A customer success manager asks Claude to fix a slow QBR-prep process. What "
           "engagement pattern best fits solution design work?",
         options={
             "A": "Ask for the single best solution and roll it out across all 40 CSMs at "
                  "once.",
             "B": "Ask for options with trade-offs against criteria, then pilot the chosen "
                  "one.",
             "C": "Ask Claude to automate the process end-to-end so design work is "
                  "unnecessary.",
             "D": "Collect solutions from other companies and adopt whichever is most "
                  "common.",
         },
         answer="B",
         why="Solution design is an arc — options with trade-offs, selection against criteria, "
             "pilot, iteration on evidence. Implementing a first suggestion org-wide skips "
             "the learning loop; full automation often violates constraints and exceeds an "
             "associate's remit; copying others ignores your criteria."),
    dict(task="4.4", domain="d4",
         q="A recruiting lead wants Claude in the hiring pipeline. Which placement follows "
           "sound workflow-integration principles?",
         options={
             "A": "Claude ranks all 200 applicants per role so recruiters interview the top "
                  "ten.",
             "B": "Claude structures CV facts and drafts summaries; recruiters decide every "
                  "case.",
             "C": "Claude conducts the initial screening calls by chat, to save recruiter "
                  "time.",
             "D": "Keep AI out of recruiting entirely, since hiring decisions affect "
                  "people.",
         },
         answer="B",
         why="Sound integration augments drudgery (extraction, structuring, drafting) and "
             "keeps judgment and accountability human — especially in a bias-sensitive, often "
             "regulated domain. Producing the ranking IS the hiring judgment; automating "
             "candidate conversations removes the human where it matters; and a blanket ban "
             "forfeits safe value."),
    dict(task="4.5", domain="d4",
         q="After a successful contract-review pilot (64% prep-time reduction) with one "
           "caught fabrication incident, an associate must brief executives — including an "
           "AI skeptic. What is the strongest communication approach?",
         options={
             "A": "Lead with the time savings and omit the incident, to keep the expansion "
                  "on track.",
             "B": "Present the measured value and the incident with the safeguard that "
                  "caught it.",
             "C": "Focus on the underlying technology, so executives understand how the "
                  "model works.",
             "D": "Let the skeptic present the risks while you present the benefits and "
                  "savings.",
         },
         answer="B",
         why="Credible stakeholder communication pairs every value claim with evidence and "
             "every limitation with its mitigation — the caught failure demonstrates the "
             "safeguards work, which is what a skeptic needs to see. Omitting incidents "
             "destroys trust when they surface; technical deep-dives answer a question "
             "executives didn't ask."),

    # ---------------- Domain 5 — Configuration and Knowledge Management ----------------
    dict(task="5.1", domain="d5",
         q="A content team pastes the same role, tone rules, product facts, and exemplar "
           "posts into every new chat, and drafts drift as teammates paste older versions. "
           "What is the right fix?",
         options={
             "A": "Maintain the setup text in a shared doc that everyone pastes from each "
                  "time.",
             "B": "Configure a Project: durable rules as instructions, documents as "
                  "knowledge.",
             "C": "Use one shared team chat, so the context only has to be pasted in once.",
             "D": "Write a longer, more detailed prompt template for each type of content.",
         },
         answer="B",
         why="Recurring context is what Projects exist for: instructions define how to work, "
             "knowledge defines what to know, and every new chat inherits both — current "
             "version, whole team. Shared paste-docs still drift and repeat; a communal "
             "mega-chat hits context limits; longer templates are the same ritual, longer."),
    dict(task="5.2", domain="d5",
         q="A sales Project answers pricing questions from an uploaded price list. Prices "
           "changed three weeks ago and reps are quoting stale numbers. Prices change "
           "monthly. What is the best correction?",
         options={
             "A": "Add an instruction telling Claude to always use the latest published "
                  "prices.",
             "B": "Replace the upload with a connector scoped to the live price sheet's "
                  "folder.",
             "C": "Re-upload the current price list and consider the problem resolved for "
                  "now.",
             "D": "Tell reps to verify every price manually, since AI data cannot be "
                  "trusted.",
         },
         answer="B",
         why="Uploads are point-in-time snapshots; monthly-changing sources belong behind a "
             "connector that reads current content — scoped to the needed folder, with the "
             "stale snapshot removed so it can't silently win. An instruction cannot conjure "
             "data the Project doesn't have, and a one-time re-upload recreates the same "
             "failure next month."),
    dict(task="5.3", domain="d5",
         q="A support Project's instructions read: 'Be professional, accurate and concise. "
           "Try to be consistent with our policies.' Answers vary wildly and once included an "
           "invented refund exception. What makes replacement instructions effective?",
         options={
             "A": "More adjectives: 'be extremely accurate, very consistent, highly "
                  "professional.'",
             "B": "Testable rules: answer only from the policy docs, citing the section.",
             "C": "A much longer document covering every situation the agents might "
                  "encounter.",
             "D": "Removing the instructions entirely and trusting the model's own "
                  "defaults.",
         },
         answer="B",
         why="Instructions work when a stranger could check compliance: answer-only-from-"
             "knowledge makes invented policy impossible to deliver silently, citations make "
             "accuracy inspectable, and named escalation categories bound the risk. "
             "Adjectives aren't rules, and sprawl creates conflicts rather than control."),
    dict(task="5.4", domain="d5",
         q="A Project configured excellently in March is confidently giving September users "
           "outdated warranty terms, obsolete contacts, and superseded section references. "
           "What does this situation call for?",
         options={
             "A": "A maintenance system: named owner, update triggers, and versioning.",
             "B": "A more capable model that is better at recognizing outdated information.",
             "C": "An instruction telling Claude to warn users its knowledge may be "
                  "outdated.",
             "D": "Recreating the Project from scratch each quarter, to guarantee "
                  "freshness.",
         },
         answer="A",
         why="Configuration is a living system — knowledge staleness is an ownership and "
             "process failure, not a model failure. Owners, update triggers, review cadence, "
             "and versioning keep the Project true. No model can detect that a policy changed "
             "outside its knowledge, blanket warnings train users to ignore them, and "
             "quarterly rebuilds lose accumulated refinement."),

    # ---------------- Domain 6 — Governance, Risk, and Responsible Use ----------------
    dict(task="6.1", domain="d6",
         q="A team proposes letting Claude automatically respond to and settle inbound "
           "insurance claims under $500 to match competitors' payout speed. How should an "
           "associate assess this use case?",
         options={
             "A": "Approve it — small claims are low-stakes and the volume savings are "
                  "large.",
             "B": "Refactor it: Claude triages and drafts, a licensed adjuster approves "
                  "each.",
             "C": "Reject any AI involvement in the claims process, at any claim value.",
             "D": "Approve it with a disclaimer telling claimants that AI processed the "
                  "claim.",
         },
         answer="B",
         why="Fit is judged on stakes, reversibility, and accountability — binding financial "
             "decisions affecting people, unreviewed before impact and likely subject to "
             "automated-decision rules, fail that screen. The refactor keeps the speed value "
             "while a human accountably decides. Blanket rejection forfeits safe value; a "
             "disclaimer doesn't create review."),
    dict(task="6.3", domain="d6",
         q="Company policy requires senior-manager review of AI-assisted client deliverables. "
           "The designated reviewer is on leave and the deadline is this week. The draft is "
           "excellent. What should the associate do?",
         options={
             "A": "Deliver without mentioning the AI assistance — the associate reviewed "
                  "it.",
             "B": "Find a compliant path, then raise the gap with the policy owner.",
             "C": "Deliver with a note that review will follow once the manager is back.",
             "D": "Use a personal AI account, since the policy only covers company tools.",
         },
         answer="B",
         why="Policies bind even when inconvenient; the professional move is comply-then-"
             "escalate — solve delivery within the rules and fix the policy gap through "
             "governance. Hiding AI involvement is a violation with a long tail, retroactive "
             "review isn't review, and personal-account workarounds are shadow AI, the worst "
             "of the options."),
    dict(task="6.4", domain="d6",
         q="A credit-card campaign segmentation built from historical approval patterns "
           "almost entirely excludes two historically underbanked zip-code clusters. What is "
           "the appropriate response?",
         options={
             "A": "Launch anyway — the segmentation only reflects real historical approval "
                  "data.",
             "B": "Halt the launch, rebuild on forward-looking criteria, and involve "
                  "compliance.",
             "C": "Add the excluded zip codes back into the segment manually, then launch.",
             "D": "Launch with a disclosure that the segmentation was AI-assisted "
                  "throughout.",
         },
         answer="B",
         why="A model trained on skewed history reproduces the skew with confidence — this "
             "pattern can be both unethical and, in credit contexts, unlawful. The response "
             "is to stop, rebuild on legitimate criteria, engage compliance, and document. "
             "'The data is the data' launders past bias; manual patching hides the mechanism; "
             "disclosure doesn't repair discrimination."),

    # ---------------- Domain 7 — Troubleshooting and Optimization ----------------
    dict(task="7.1", domain="d7",
         q="A weekly KPI-commentary prompt that worked for months now invents targets and "
           "discusses metrics absent from the attached export. What is the correct "
           "troubleshooting approach?",
         options={
             "A": "Classify the failure first, apply a targeted fix, and re-test on the "
                  "same input.",
             "B": "Add 'be more accurate, do not hallucinate' to the prompt and carry on.",
             "C": "Re-run the prompt a few times and use the best output each week.",
             "D": "Switch to a different model, since this one has started hallucinating.",
         },
         answer="A",
         why="Sudden fabrication after months of success points to a changed input, not a "
             "changed model — the missing target data left a gap that plausible inventions "
             "filled. Diagnosis before remedy: classify the failure type, fix that cause, "
             "verify on the same input. Accuracy exhortations, re-rolls, and model swaps are "
             "all guesses that skip the diagnosis."),
    dict(task="7.2", domain="d7",
         q="Six weeks of feedback on an AI proposal workflow: pricing sections heavily edited "
           "in 9 of 12 proposals; two reps call the tone too formal for startups; one VP "
           "called one proposal 'unusable' with no specifics; exec summaries are praised. "
           "How should the team act?",
         options={
             "A": "Rebuild the workflow — a VP calling the output unusable is a serious "
                  "signal.",
             "B": "Prioritize by pattern strength: the systematic pricing edits come first.",
             "C": "Address all four signals at once, so every stakeholder sees a response.",
             "D": "Add a disclaimer to the drafts saying they may still require editing.",
         },
         answer="B",
         why="Feedback is triaged by frequency and impact, not seniority or volume: a 75% "
             "systematic edit-rate outranks an n=1 anecdote. Diagnose the pattern, fix one "
             "lever at a time, re-measure, and explicitly protect what works. Rebuilds for "
             "anecdotes and simultaneous changes destroy the ability to learn what fixed what."),
    dict(task="7.3", domain="d7",
         q="A working localization flow is heavy: context re-pasted into every chat, five "
           "sequential regional chats per item, and one bilingual reviewer reading everything "
           "— a two-day bottleneck. Which optimization keeps quality while cutting cost?",
         options={
             "A": "Remove the human review step, since the outputs have been reliable for "
                  "months.",
             "B": "Move context into a Project, batch the five variants, refocus review on "
                  "risk.",
             "C": "Upgrade every step to the most capable model so review becomes "
                  "unnecessary.",
             "D": "Ask the reviewer to work faster and set a same-day review SLA for all "
                  "items.",
         },
         answer="B",
         why="Optimization removes redundancy — repeated context, sequential near-duplicate "
             "work, over-provisioned models — while keeping the quality safeguard and aiming "
             "it where risk concentrates. Deleting review removes the safety net, maximal "
             "models don't eliminate the need for review, and pressuring the bottleneck human "
             "changes nothing structural."),
]
