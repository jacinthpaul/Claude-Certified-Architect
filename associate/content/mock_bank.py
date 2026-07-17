"""
associate/content/mock_bank.py — 60-question blueprint-aligned MOCK EXAM bank (CCAO-F)
======================================================================================
Authored, exam-style scenario questions aligned to the official Claude Certified
Associate – Foundations Exam Guide blueprint. Distribution follows the official
domain weights for a 60-item exam:

  D1 Prompting 14% → 8 · D2 Evaluation 21% → 13 · D3 Products/Models 12% → 7
  D4 Workflows 16% → 10 · D5 Config/Knowledge 12% → 7 · D6 Governance 15% → 9
  D7 Troubleshooting 10% → 6      (total 60)

Each item: task, domain, q, options A–D, answer letter, letter-free why (safe to
shuffle), and a ref line naming the domain/lesson it tests. Tagged M1..M60 by the
builder. Study aids, NOT official exam items.
"""

MOCK_BANK = [

# ================= DOMAIN 1 — Prompting and Task Execution (8) =================

dict(task="1.1", domain="d1",
     q="An associate needs Claude to draft a message announcing a delayed product release "
       "to enterprise customers. Which prompt is most likely to produce a usable draft on "
       "the first attempt?",
     options={
         "A": "\"Write an announcement about the product delay.\"",
         "B": "\"Draft a 150-word email to enterprise customers announcing the Q3 release "
              "moving to November. Tone: candid, no marketing spin. Must include: the new "
              "date, one-sentence reason (quality bar), what happens to existing "
              "commitments, and a named contact.\"",
         "C": "\"Write a very professional, high-quality, detailed announcement about the "
              "product delay. Make sure it is excellent.\"",
         "D": "\"You are the world's best communications expert. Write an announcement "
              "about the product delay.\"",
     },
     answer="B",
     why="The strong prompt supplies audience, length, tone, and the required content "
         "elements — the actual requirements. Quality adjectives and grand persona labels "
         "add no requirements, so both leave the model guessing at the same unknowns as "
         "the bare request.",
     ref="D1 Prompting and Task Execution — Lesson 1.1"),

dict(task="1.1", domain="d1",
     q="A finance associate keeps getting Claude outputs in flowing prose when they need "
       "content they can drop into a slide. What element is their prompt most likely "
       "missing?",
     options={
         "A": "An explicit output-format specification (e.g., '5 bullets, max 12 words each').",
         "B": "A politeness marker, since models respond better to courteous prompts.",
         "C": "A more capable model selection for business content.",
         "D": "Longer, more detailed background about the company.",
     },
     answer="A",
     why="Output shape is a prompt element like any other: if the format isn't stated, the "
         "model defaults to prose. Courtesy, model tier, and extra background don't "
         "communicate the missing requirement — the format specification does.",
     ref="D1 Prompting and Task Execution — Lesson 1.1"),

dict(task="1.2", domain="d1",
     q="A consultant must produce a 40-page client readiness assessment. Asking Claude for "
       "the whole document at once yields shallow, partly inconsistent content. What is the "
       "best restructuring of the work?",
     options={
         "A": "Ask for the document again with 'be thorough and consistent' added.",
         "B": "Decompose it: outline first, then each section drafted in sequence with the "
              "consultant reviewing and correcting before the next section builds on it.",
         "C": "Generate the document five times and merge the strongest chapters.",
         "D": "Split the document across five parallel chats, one per section, and staple "
              "the results together.",
     },
     answer="B",
     why="Sequenced decomposition with review between steps keeps each unit verifiable and "
         "lets corrected output ground the next step. Merging independent generations and "
         "parallel unreviewed chats both reproduce the inconsistency problem; exhortations "
         "to be thorough change nothing structural.",
     ref="D1 Prompting and Task Execution — Lesson 1.2"),

dict(task="1.2", domain="d1",
     q="While decomposing a complex analysis into steps, an associate wonders when to pause "
       "for their own review of Claude's output. What is the guiding principle?",
     options={
         "A": "Review only the final combined deliverable to preserve momentum.",
         "B": "Review after every step whose output feeds the next step — early errors "
              "compound downstream.",
         "C": "Review is unnecessary if each step's prompt was well-written.",
         "D": "Review at random intervals so the checking is unbiased.",
     },
     answer="B",
     why="The value of decomposition comes from checkpoints: an unverified early output "
         "poisons everything built on it. Final-only review discovers compounded errors at "
         "the most expensive moment; good prompts reduce but never remove the need to "
         "verify.",
     ref="D1 Prompting and Task Execution — Lesson 1.2"),

dict(task="1.3", domain="d1",
     q="Claude's draft of a client FAQ has strong answers but the wrong reading level and "
       "several missing topics. Which follow-up gets the best next iteration?",
     options={
         "A": "\"This isn't right, try again.\"",
         "B": "\"Keep all ten answers as written. Rewrite at an 8th-grade reading level, and "
              "add entries for billing disputes, cancellation, and data export — using the "
              "attached policy for those three.\"",
         "C": "\"Make it simpler and more complete.\"",
         "D": "Start a fresh chat with a longer initial prompt and regenerate from scratch.",
     },
     answer="B",
     why="Anchored feedback preserves what works, names the specific changes, and supplies "
         "the missing inputs for the gaps. Undirected retries and vague comparatives "
         "regenerate at random; restarting discards ten good answers the iteration should "
         "have kept.",
     ref="D1 Prompting and Task Execution — Lesson 1.3"),

dict(task="1.3", domain="d1",
     q="After three feedback rounds, Claude still can't produce the right competitive "
       "positioning section — each revision guesses differently at the competitor's "
       "pricing. What does this convergence failure signal?",
     options={
         "A": "The prompt is missing information the model cannot invent — supply the "
              "competitor data instead of re-phrasing the feedback.",
         "B": "The model has reached its capability ceiling for this task.",
         "C": "More forceful feedback wording is needed.",
         "D": "The conversation should be moved to a Project.",
     },
     answer="A",
     why="When iterations keep guessing at the same detail, the gap is missing input, not "
         "phrasing: no amount of feedback conjures facts the model was never given. "
         "Capability, forcefulness, and Project structure don't address an information "
         "deficit.",
     ref="D1 Prompting and Task Execution — Lesson 1.3"),

dict(task="1.4", domain="d1",
     q="A strategy associate has four tasks: score three vendors against criteria, gather "
       "current market entrants, write a board memo, and generate campaign concepts. Which "
       "pairing of task and prompting strategy is correct?",
     options={
         "A": "Vendor scoring → ask for many unfiltered creative options.",
         "B": "Campaign concepts → request a large number of diverse, unjudged ideas; vendor "
              "scoring → explicit criteria and a structured comparison.",
         "C": "Board memo → request maximum idea quantity; market entrants → a single "
              "polished narrative.",
         "D": "All four → one combined prompt so the outputs stay consistent.",
     },
     answer="B",
     why="Brainstorming rewards divergence (quantity, variety, deferred judgment) while "
         "analysis rewards convergence (criteria, structure). Crossing the modes — creative "
         "breadth for scoring, single answers for ideation — or fusing all four tasks "
         "produces the wrong shape for every task.",
     ref="D1 Prompting and Task Execution — Lesson 1.4"),

dict(task="1.4", domain="d1",
     q="An associate researching new privacy legislation for a briefing asks Claude to "
       "'brainstorm what the law probably says.' What is wrong with this approach?",
     options={
         "A": "Nothing — brainstorming surfaces more possibilities than direct questions.",
         "B": "Research tasks need grounding in actual sources (documents or research mode) "
              "and verification — a divergent ideation prompt invites plausible invention "
              "about checkable facts.",
         "C": "The prompt should have requested more ideas to improve coverage.",
         "D": "Legislation can never be discussed with AI tools.",
     },
     answer="B",
     why="Task type dictates strategy: legal content is a research task with verifiable "
         "ground truth, so the prompt should demand sources and scope, not creative "
         "speculation. Brainstorming what facts 'probably' are is a recipe for confident "
         "fabrication.",
     ref="D1 Prompting and Task Execution — Lesson 1.4"),

# ================= DOMAIN 2 — Output Evaluation and Validation (13) =================

dict(task="2.1", domain="d2",
     q="Claude summarizes a 40-page vendor contract for an associate. The summary reads "
       "smoothly and matches everything the associate remembers about the deal. Before the "
       "summary informs a renewal decision, what evaluation is required?",
     options={
         "A": "None — it matches the associate's recollection of the contract.",
         "B": "Check key claims (terms, dates, obligations) against the contract text and "
              "confirm the summary covers the sections the renewal decision depends on.",
         "C": "Ask Claude to re-read the contract and confirm its own summary.",
         "D": "Compare its length against summaries of similar contracts.",
     },
     answer="B",
     why="Memory and fluency are weak evaluators; decisions need claims verified against "
         "the source and coverage checked against the decision's needs — omitted clauses "
         "are as dangerous as wrong ones. A model confirming itself re-runs the same "
         "process that made any error.",
     ref="D2 Output Evaluation and Validation — Lesson 2.1"),

dict(task="2.1", domain="d2",
     q="An associate asked Claude for 'the risks in this supplier proposal' and received "
       "six well-explained risks. The most reliable way to catch what the response MISSED "
       "is to:",
     options={
         "A": "Re-read the proposal against the response, checking each section for risk "
              "content the six items don't cover.",
         "B": "Count whether six risks is typical for proposals of this size.",
         "C": "Check that each of the six risks is well-reasoned.",
         "D": "Ask Claude if it is confident the list is complete.",
     },
     answer="A",
     why="Completeness failures are invisible from inside the output — they're found by "
         "comparing the output against the source material. Verifying only what's present "
         "checks accuracy, not coverage, and self-reported completeness is no more reliable "
         "than self-reported confidence.",
     ref="D2 Output Evaluation and Validation — Lesson 2.1"),

dict(task="2.2", domain="d2",
     q="A Claude-drafted industry overview cites 'the 2025 McKinsey Logistics Outlook, p. "
       "47' for a key statistic. The associate cannot find this report anywhere. What has "
       "most likely happened?",
     options={
         "A": "The report exists but is behind a paywall, so the citation should stand.",
         "B": "The model fabricated a plausible-looking citation — a hallucination — and the "
              "statistic needs a real, verified source or removal.",
         "C": "The model accessed a private database unavailable to the associate.",
         "D": "The page number is wrong but the statistic is trustworthy.",
     },
     answer="B",
     why="Invented citations with realistic titles and page numbers are a classic "
         "hallucination: the model produces the FORM of evidence without the substance. An "
         "unverifiable citation cannot support a claim — assuming paywalls, secret access, "
         "or minor errata extends trust the output hasn't earned.",
     ref="D2 Output Evaluation and Validation — Lesson 2.2"),

dict(task="2.2", domain="d2",
     q="Halfway through a long Claude-generated report, the projected savings figure changes "
       "from $2.1M to $1.6M with no explanation. What kind of defect is this, and what does "
       "it require?",
     options={
         "A": "A rounding convention — pick either number.",
         "B": "An internal inconsistency — trace both figures to the underlying data to "
              "determine which (if either) is right before the report is used.",
         "C": "A hallucinated citation — delete both figures.",
         "D": "Expected model behavior in long outputs — no action needed.",
     },
     answer="B",
     why="Contradictory figures within one output are an inconsistency defect: at least one "
         "number is wrong, and only reconciliation against the source data reveals which. "
         "Picking one arbitrarily or normalizing the defect ships a 24% error either way.",
     ref="D2 Output Evaluation and Validation — Lesson 2.2"),

dict(task="2.2", domain="d2",
     q="Claude drafts interview screening criteria from a team's 'best performer profiles' "
       "and the criteria heavily favor traits of the current team's demographic majority. "
       "What should the associate recognize?",
     options={
         "A": "The criteria are objective because they came from performance data.",
         "B": "The output may encode bias inherited from a skewed sample — the criteria need "
              "review against the actual job requirements before any use.",
         "C": "The model is malfunctioning and should be reported.",
         "D": "Adding more best-performer profiles will balance the criteria.",
     },
     answer="B",
     why="Bias in outputs often arrives via bias in inputs: a homogeneous 'best performer' "
         "sample teaches demographic echo, not job competence. Recognizing systematic skew "
         "and re-grounding criteria in validated requirements is the evaluation skill; more "
         "of the same data deepens the skew.",
     ref="D2 Output Evaluation and Validation — Lesson 2.2"),

dict(task="2.3", domain="d2",
     q="Claude produces a competitive brief containing: (a) a competitor's claimed new "
       "feature, (b) a computed market-share percentage, and (c) a quoted line from a CEO "
       "interview. Which validation mapping is correct?",
     options={
         "A": "(a) press release or product page; (b) recompute from the underlying figures; "
              "(c) locate the original interview.",
         "B": "All three: ask Claude to double-check its work in the same chat.",
         "C": "(a) and (c) need no validation; (b) should be rounded for safety.",
         "D": "All three: accept if at least two other AI tools agree.",
     },
     answer="A",
     why="Validation technique follows claim type: product claims trace to the company's "
         "own announcements, computed statistics get recomputed, quotes get located in the "
         "primary source. Self-checks re-run the same model, agreement between AI tools "
         "isn't ground truth, and rounding doesn't validate anything.",
     ref="D2 Output Evaluation and Validation — Lesson 2.3"),

dict(task="2.3", domain="d2",
     q="An associate has 20 Claude-generated claims to validate before a deadline and "
       "cannot deep-verify all of them. How should validation effort be allocated?",
     options={
         "A": "Equal time per claim, for consistency.",
         "B": "By stakes: deep-verify the claims the decision or audience most depends on "
              "(regulatory, financial, external-facing); spot-check the low-consequence rest.",
         "C": "Validate the ten easiest claims fully and note the rest as unverified.",
         "D": "Skip validation this once and add a general disclaimer.",
     },
     answer="B",
     why="Validation depth scales with the cost of being wrong. Stakes-based triage puts "
         "scarce effort where errors do damage; uniform effort over-checks trivia while "
         "under-checking the material claims, ease-based selection inverts the priority, "
         "and disclaimers don't validate.",
     ref="D2 Output Evaluation and Validation — Lesson 2.3"),

dict(task="2.3", domain="d2",
     q="To validate a Claude-drafted summary of a new tax rule, an associate asks Claude "
       "'Are you sure this is correct?' and receives 'Yes — this reflects the current "
       "rule.' What has the associate learned?",
     options={
         "A": "The summary is validated and safe to circulate.",
         "B": "Essentially nothing — models often reaffirm their own errors fluently; the "
              "rule text itself (or a qualified reviewer) is the validation source.",
         "C": "The summary is now MORE likely correct because it survived a challenge.",
         "D": "The summary is wrong, since honest models express doubt when challenged.",
     },
     answer="B",
     why="Asking the generator to grade itself re-samples the process that produced any "
         "error — confident reaffirmation is common and carries no evidential weight in "
         "either direction. External authoritative verification is the only move that adds "
         "information.",
     ref="D2 Output Evaluation and Validation — Lesson 2.3"),

dict(task="2.4", domain="d2",
     q="Which of these Claude outputs can an associate reasonably use after self-review "
       "alone, without routing to a qualified human reviewer?",
     options={
         "A": "A severance-terms explanation to be sent to a departing employee.",
         "B": "An internal first-draft agenda and discussion notes for the team's weekly sync.",
         "C": "A public statement responding to a customer data-breach rumor.",
         "D": "Dosage-related wording for a medical device's user leaflet.",
     },
     answer="B",
     why="Review triggers are categorical: personnel/legal terms, public crisis statements, "
         "and medical content all carry consequences that mandate qualified review "
         "regardless of draft quality. A routine internal agenda is low-stakes and "
         "reversible — self-review suffices.",
     ref="D2 Output Evaluation and Validation — Lesson 2.4"),

dict(task="2.4", domain="d2",
     q="A team routes every single Claude output — including routine internal drafts — to "
       "the legal team 'to be safe.' Legal now rubber-stamps the queue. What has the team "
       "gotten wrong about human review?",
     options={
         "A": "Nothing — maximum review is maximum safety.",
         "B": "Review must be calibrated to risk categories: flooding reviewers with trivial "
              "items degrades scrutiny of the few outputs where review actually matters.",
         "C": "Legal review should be replaced with a second AI model's review.",
         "D": "Reviews should be sampled randomly at 10% regardless of content.",
     },
     answer="B",
     why="Indiscriminate review is a failure mode, not a safety posture: reviewer attention "
         "is finite, and rubber-stamping means high-stakes items get the same glance as "
         "trivia. Categorical triggers concentrate qualified eyes where consequences live. "
         "AI-reviewing-AI and blind sampling both miss the point of qualified judgment.",
     ref="D2 Output Evaluation and Validation — Lesson 2.4"),

dict(task="2.5", domain="d2",
     q="An associate must deliver quarterly results to the board and to the engineering "
       "all-hands. Claude produced one competent document. What is the right next step?",
     options={
         "A": "Send it to both audiences — the facts don't change.",
         "B": "Generate audience-specific variants: decision- and impact-focused for the "
              "board; specifics and team-relevant detail for engineering — same facts, "
              "different depth and framing.",
         "C": "Send the board a shortened copy with the technical paragraphs deleted.",
         "D": "Send engineering the board version plus a glossary.",
     },
     answer="B",
     why="Adaptation is translation for what each audience must do with the information, "
         "not truncation. Deleting paragraphs loses content the board needs framed "
         "differently (not removed), and glossaries patch vocabulary while leaving the "
         "wrong emphasis. One-document-fits-all serves neither audience.",
     ref="D2 Output Evaluation and Validation — Lesson 2.5"),

dict(task="2.6", domain="d2",
     q="A team lead asks Claude for a quick definition of 'net revenue retention' during a "
       "chat, and separately for a 30-criteria security-questionnaire response matrix that "
       "three teams will fill in over two weeks. Which format pairing is right?",
     options={
         "A": "Definition → inline chat answer; questionnaire matrix → structured "
              "table/artifact the teams can work in and update.",
         "B": "Both inline — chat keeps everything in one place.",
         "C": "Both as artifacts — artifacts look more professional.",
         "D": "Definition → table; matrix → prose so it reads naturally.",
     },
     answer="A",
     why="Downstream use picks the format: a conversational fact needs an inline sentence; "
         "a multi-team, multi-week, updated deliverable needs a structured, durable "
         "artifact. Over-formatting trivia and under-formatting working documents are the "
         "twin failures.",
     ref="D2 Output Evaluation and Validation — Lesson 2.6"),

dict(task="2.6", domain="d2",
     q="Claude returns a 25-item risk assessment as one undifferentiated wall of prose. The "
       "audience needs to act on it in a review meeting. What curation should the associate "
       "request?",
     options={
         "A": "None — the content is complete, and meetings can work through prose.",
         "B": "Group items by category, rank by severity within groups, put the top five in "
              "a summary table, and move the long tail to an appendix.",
         "C": "Cut the assessment to five items so it fits one slide.",
         "D": "Convert every item into its own table for consistency.",
     },
     answer="B",
     why="Curation — grouping, ranking, surfacing the actionable few while preserving the "
         "rest — is what turns complete information into usable information. Deleting 20 "
         "items discards the record; 25 one-row tables is formatting noise; raw prose "
         "forces the meeting to do the organizing.",
     ref="D2 Output Evaluation and Validation — Lesson 2.6"),

# ================= DOMAIN 3 — Product and Model Selection (7) =================

dict(task="3.1", domain="d3",
     q="A consultant answers client questions all day using the same methodology decks and "
       "templates, and today also needs current statistics on a fast-moving regulation. "
       "Which product-feature setup fits?",
     options={
         "A": "A Project containing the methodology decks and templates, with research mode "
              "used inside it when current sourced facts are needed.",
         "B": "Research mode for everything, since it is the most powerful feature.",
         "C": "A plain chat with the decks re-uploaded whenever they seem relevant.",
         "D": "An artifact containing all the methodology content, referenced in each chat.",
     },
     answer="A",
     why="Durable recurring context belongs in Project knowledge and instructions; live "
         "sourced facts are research mode's job; the two compose in the same chat. Research "
         "mode doesn't hold your methodology, re-uploading is the ritual Projects remove, "
         "and artifacts are deliverables, not context stores.",
     ref="D3 Product and Model Selection — Lesson 3.1"),

dict(task="3.1", domain="d3",
     q="An associate asks plain chat (without research mode) for 'this quarter's funding "
       "rounds in our industry' and gets a detailed, dated list. How should they treat this "
       "output?",
     options={
         "A": "As current — the entries carry specific dates and amounts.",
         "B": "As unreliable for recency: training data has a cutoff, so 'this quarter' "
              "claims need research mode (or manual sources) with verified citations.",
         "C": "As current, provided the chat began today.",
         "D": "As reliable after asking the model to confirm the list is up to date.",
     },
     answer="B",
     why="A model without live research answers recency questions from training data and "
         "may present stale or invented specifics with full confidence — today's date on "
         "the chat doesn't update the knowledge, and self-confirmation adds nothing. "
         "Current-events tasks need the feature built for them.",
     ref="D3 Product and Model Selection — Lesson 3.1"),

dict(task="3.2", domain="d3",
     q="Which task assignment correctly matches Claude model tiers to workloads?",
     options={
         "A": "Haiku for a nuanced multi-document legal risk analysis; Opus for tagging "
              "10,000 support tickets.",
         "B": "Haiku for tagging 10,000 support tickets; Sonnet for everyday report "
              "drafting; Opus for the nuanced multi-document legal risk analysis.",
         "C": "Opus for everything, to standardize on one model.",
         "D": "Sonnet for everything, since it balances all trade-offs.",
     },
     answer="B",
     why="Capability should follow task complexity: high-volume classification fits the "
         "fast economical tier, everyday drafting fits the balanced tier, and deep "
         "cross-document reasoning justifies the most capable tier. Inverting the mapping "
         "overpays on volume and underserves complexity; single-model standardization "
         "does one or the other everywhere.",
     ref="D3 Product and Model Selection — Lesson 3.2"),

dict(task="3.2", domain="d3",
     q="A colleague argues: 'Model choice is irrelevant now — just always pick the most "
       "capable one; compute is cheap.' For a 50,000-call/month automated workflow, what is "
       "the strongest counterpoint?",
     options={
         "A": "At volume, per-call cost and latency multiply: paying top-tier prices for "
              "work a faster tier handles adequately burns budget and slows every "
              "interaction, without a quality benefit the workflow's review step doesn't "
              "already provide.",
         "B": "More capable models are actually less accurate on simple tasks.",
         "C": "The most capable model should be reserved for executives' use.",
         "D": "There is no counterpoint — maximum capability is always the safe default.",
     },
     answer="A",
     why="The trade-off is real at scale: cost and latency are per-call taxes multiplied "
         "50,000 times monthly, while marginal quality often disappears behind existing "
         "review nets on straightforward tasks. The counterargument is economic fit, not a "
         "claim that capable models perform worse or belong to a status hierarchy.",
     ref="D3 Product and Model Selection — Lesson 3.2"),

dict(task="3.3", domain="d3",
     q="An associate is choosing a model for extracting five fields from ~800 supplier "
       "invoices daily, with a clerk spot-checking 10%. What is the soundest selection "
       "process?",
     options={
         "A": "Start with the most capable model and downgrade if the budget complains.",
         "B": "State the requirements (volume, latency ceiling, accuracy floor given the "
              "spot-check net), pilot the most economical plausible model against them, and "
              "step up only where measured accuracy misses the bar.",
         "C": "Use the mid-tier model — it's a safe compromise for any task.",
         "D": "Survey which model other companies use for invoices.",
     },
     answer="B",
     why="Requirements first, then the cheapest model that clears them, verified by "
         "measurement — stepping up selectively where evidence demands. Starting expensive "
         "anchors cost without evidence, compromise-by-default ignores this task's actual "
         "profile, and other companies' choices encode other companies' requirements.",
     ref="D3 Product and Model Selection — Lesson 3.3"),

dict(task="3.4", domain="d3",
     q="A month-long support-planning chat has grown enormous. Claude now responds slowly, "
       "misses constraints set early in the conversation, and recently contradicted an "
       "agreed decision. What is happening and what fixes it?",
     options={
         "A": "The model was updated mid-project; wait for the next update.",
         "B": "The conversation is exceeding its practical context window; summarize the "
              "durable decisions, persist them in a Project, and continue in fresh chats.",
         "C": "The prompts have become too polite; firmer language restores compliance.",
         "D": "Nothing is wrong; contradictions are normal model variance to be corrected "
              "case by case.",
     },
     answer="B",
     why="Degradation, lost early constraints, and contradicted decisions in a very long "
         "chat are context-limit symptoms. The structural fix is summarize-and-restart with "
         "durable context persisted where every new chat inherits it. Blaming updates, "
         "tone, or 'variance' misdiagnoses a well-understood limitation.",
     ref="D3 Product and Model Selection — Lesson 3.4"),

dict(task="3.4", domain="d3",
     q="Before closing a long analysis chat for the week, what habit best preserves the "
       "work for future sessions?",
     options={
         "A": "Ask Claude for a structured summary of decisions, constraints, open items, "
              "and next steps — and save it where future chats can use it (e.g., Project "
              "knowledge or the team's docs).",
         "B": "Keep the chat open in a browser tab so the context stays warm.",
         "C": "Nothing — the conversation history is the permanent record.",
         "D": "Copy the entire transcript into the start of next week's chat.",
     },
     answer="A",
     why="A chat is a workspace, not a filing cabinet: durable context survives through "
         "deliberate persistence of the distilled decisions, not through open tabs or raw "
         "transcript re-pasting (which re-creates the overload). The summary-and-persist "
         "habit is what makes restarts cheap.",
     ref="D3 Product and Model Selection — Lesson 3.4"),

# ================= DOMAIN 4 — Workflow Integration and Solution Design (10) =================

dict(task="4.1", domain="d4",
     q="A director asks an associate to 'get Claude to modernize our reporting.' Before any "
       "building, which use of Claude delivers the most value?",
     options={
         "A": "Generating a modern report template to show quick progress.",
         "B": "Analyzing the request: current reports and their consumers, pain points, "
              "constraints, and drafting testable success criteria to confirm with the "
              "director.",
         "C": "Researching reporting-tool vendors and their pricing.",
         "D": "Rebuilding last quarter's report in a new format as a demo.",
     },
     answer="B",
     why="'Modernize' is an unexamined requirement — building against it encodes guesses. "
         "Requirements analysis (who consumes what, what hurts, what success means) turns a "
         "vague mandate into confirmable acceptance criteria; templates, vendors, and demos "
         "come after the problem is defined.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.1"),

dict(task="4.1", domain="d4",
     q="During requirements analysis, Claude infers that a new intake form 'must integrate "
       "with the CRM.' Nobody has actually said this. How should the associate handle "
       "Claude's inferred requirement?",
     options={
         "A": "Include it in the plan — the inference is reasonable.",
         "B": "Treat it as a candidate requirement to validate with the actual stakeholders "
              "before it becomes a commitment.",
         "C": "Discard it — models should not propose requirements.",
         "D": "Ask Claude to rate its confidence in the inference and include it above 80%.",
     },
     answer="B",
     why="Claude's analytical value is surfacing candidate requirements humans might miss — "
         "but candidates become commitments only through stakeholder confirmation. Silently "
         "adopting inferences builds unrequested scope; discarding them wastes the "
         "surfacing value; model self-confidence is not stakeholder confirmation.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.1"),

dict(task="4.2", domain="d4",
     q="An associate wants Claude's help optimizing the invoice-approval process. Which "
       "input to Claude produces the most actionable optimization analysis?",
     options={
         "A": "\"Our invoice process is slow. How do companies usually speed this up?\"",
         "B": "The documented process — steps, owners, durations, volumes, exception rates — "
              "with a request to identify bottlenecks, redundancies, and automation "
              "candidates ranked by expected impact.",
         "C": "\"List the top ten process-optimization frameworks.\"",
         "D": "The org chart, so Claude understands who is involved.",
     },
     answer="B",
     why="Optimization analysis is only as good as the process data provided: concrete "
         "steps, timings, and volumes let the model locate THIS process's bottlenecks and "
         "rank fixes by impact. Generic how-do-companies answers and framework lists "
         "produce advice unmoored from the actual workflow.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.2"),

dict(task="4.2", domain="d4",
     q="Claude's plan for a system rollout schedules staff training in week 2, before the "
       "training environment exists in week 4 — a dependency error an experienced PM spots "
       "immediately. What does this illustrate about Claude-assisted planning?",
     options={
         "A": "AI-generated plans are unusable for project work.",
         "B": "Draft plans accelerate the work, but dependency logic and feasibility need "
              "human validation before the plan is adopted — the reviewer role is part of "
              "the workflow.",
         "C": "The prompt should have said 'do not make dependency errors.'",
         "D": "Planning tasks require the most capable model, which would not err this way.",
     },
     answer="B",
     why="Claude drafts plans fast and covers ground, but it reasons from what it is told — "
         "dependency and feasibility checking against reality is the human's contribution. "
         "Neither exhortations nor bigger models remove that review step; abandoning "
         "AI-assisted planning discards the acceleration.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.2"),

dict(task="4.3", domain="d4",
     q="An associate designing a new client-intake workflow asks Claude for one recommended "
       "design and receives a sensible proposal. What is the main weakness of stopping "
       "here?",
     options={
         "A": "The proposal was produced too quickly to be trustworthy.",
         "B": "No alternatives were compared against the team's criteria, so nobody knows "
              "what trade-offs the single proposal silently made.",
         "C": "Claude's designs must always be discarded and rebuilt by humans.",
         "D": "A single proposal cannot be piloted.",
     },
     answer="B",
     why="Design quality comes from comparing options against explicit criteria — a lone "
         "proposal hides its trade-offs (cost vs. flexibility, speed vs. control) because "
         "there is nothing to contrast them with. Speed isn't the defect, and single "
         "proposals pilot fine; they just shouldn't be chosen blind.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.3"),

dict(task="4.3", domain="d4",
     q="After a two-week pilot of a Claude-assisted reporting design, feedback shows the "
       "drafts misjudge account health because a key data tab is missing from the inputs. "
       "What is the correct iteration response?",
     options={
         "A": "Extend the pilot unchanged to gather more evidence.",
         "B": "Fix the diagnosed cause — make the missing tab a required input and add a "
              "health-assessment rubric — then re-pilot against the same success criteria.",
         "C": "Declare the design failed and return to the manual process.",
         "D": "Lower the success criteria so the current design passes.",
     },
     answer="B",
     why="Iteration means feeding pilot evidence back into the design: the failure traced "
         "to input completeness, so the revision targets that cause and re-tests against "
         "the unchanged yardstick. Prolonging a known-broken pilot, abandoning after one "
         "fixable finding, and moving the goalposts all waste what the pilot taught.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.3"),

dict(task="4.4", domain="d4",
     q="A finance team is adding Claude to its month-end close. Which division of labor "
       "reflects sound workflow integration?",
     options={
         "A": "Claude drafts variance commentary, reconciliation summaries, and flags "
              "anomalies; accountants investigate flags, make judgments, and sign off.",
         "B": "Claude approves journal entries below a threshold to relieve the team.",
         "C": "Claude handles the entire close; accountants audit it quarterly.",
         "D": "Claude is excluded — financial processes cannot include AI assistance.",
     },
     answer="A",
     why="Integration assigns drudgery (drafting, summarizing, anomaly-flagging) to the AI "
         "and keeps judgment, approval, and accountability with qualified humans at the "
         "gates. Auto-approving entries IS a financial judgment; quarterly-audited "
         "automation removes the gate; blanket exclusion forfeits safe value.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.4"),

dict(task="4.4", domain="d4",
     q="Two months after Claude was added to a proposal workflow, usage is near zero: writers "
       "say they don't know when to trust the drafts or who is responsible if an error "
       "ships. What did the integration skip?",
     options={
         "A": "A more capable model that would have earned trust automatically.",
         "B": "Change management: documented guidance on when to trust vs. override the AI "
              "step, error ownership, and training the team on the redesigned flow.",
         "C": "A mandate requiring writers to use the tool.",
         "D": "Nothing — adoption always takes years.",
     },
     answer="B",
     why="A workflow redesign is complete only when the humans in it know their new roles: "
         "trust boundaries, override rights, and error ownership are design artifacts, not "
         "afterthoughts. Mandates force resentful usage of an unclear system, and no model "
         "tier answers 'who owns the mistake?'",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.4"),

dict(task="4.5", domain="d4",
     q="A department head asks an associate whether Claude could 'replace the two analysts "
       "who left.' Which response communicates value and limitations accurately?",
     options={
         "A": "\"Yes — modern models outperform human analysts.\"",
         "B": "\"It can absorb much of their drafting, summarization, and first-pass "
              "analysis, measurably faster. It can't own judgment calls, verify its own "
              "facts, or carry accountability — those transfer to the remaining team, so "
              "let's size that load honestly.\"",
         "C": "\"No — AI tools are unreliable for analytical work.\"",
         "D": "\"That depends entirely on next year's model releases.\"",
     },
     answer="B",
     why="Honest stakeholder communication names what transfers (drafting, synthesis "
         "throughput) and what doesn't (judgment, verification, accountability), letting "
         "the leader plan on real capabilities. Hype creates a staffing hole discovered in "
         "production; doom forfeits the genuine capacity; deferral answers nothing.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.5"),

dict(task="4.5", domain="d4",
     q="Preparing a stakeholder briefing on a new AI workflow, an associate lists "
       "limitations: hallucination risk, training-data recency, and context limits. What "
       "should accompany each limitation to make the briefing effective?",
     options={
         "A": "The mitigation built into the workflow (verification step, research "
              "mode/current sources, summarize-and-restart practices).",
         "B": "A technical explanation of why transformers exhibit each behavior.",
         "C": "A comparison showing competitors' tools share the same flaws.",
         "D": "Nothing — limitations should be listed but not dwelt on.",
     },
     answer="A",
     why="Limitations land as operating rules when paired with the control that manages "
         "them — that's what turns risk disclosure into confidence. Architecture lectures "
         "answer unasked questions, whataboutism reassures no one, and bare lists read as "
         "unmanaged risk.",
     ref="D4 Workflow Integration and Solution Design — Lesson 4.5"),

# ================= DOMAIN 5 — Configuration and Knowledge Management (7) =================

dict(task="5.1", domain="d5",
     q="When configuring a Claude Project, which placement of content is correct?",
     options={
         "A": "Stable rules (role, tone, format, escalation) in instructions; reference "
              "documents (style guide, fact sheets, templates) as knowledge; one-off "
              "details in the individual chat.",
         "B": "Everything in instructions, so nothing is ever missed.",
         "C": "Everything as knowledge documents, including the tone rules.",
         "D": "Everything in the first message of each chat, for transparency.",
     },
     answer="A",
     why="Instructions define how every chat behaves (stable rules); knowledge supplies "
         "what chats consult (documents, swappable as they change); the chat itself holds "
         "only that conversation's specifics. Cramming everything into one layer either "
         "bloats standing orders with volatile facts or buries behavioral rules in "
         "documents.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.1"),

dict(task="5.1", domain="d5",
     q="A team lead 'set up' a shared Project but added no instructions or knowledge — it's "
       "just a folder of chats, and members still paste the style guide into each one. What "
       "is the corrective action?",
     options={
         "A": "Ask members to paste more carefully from the newest version.",
         "B": "Configure the Project properly: the durable behavioral rules as instructions "
              "and the style guide as a knowledge document, so every chat starts briefed.",
         "C": "Create one pinned chat containing the style guide for everyone to reuse.",
         "D": "Replace the Project with a longer prompt template in the team wiki.",
     },
     answer="B",
     why="The Project's value IS its configuration — instructions and knowledge inherited "
         "by every chat, current version, whole team. An unconfigured Project is a folder; "
         "pinned chats hit context limits and drift; wiki templates preserve the exact "
         "paste ritual the feature exists to remove.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.1"),

dict(task="5.2", domain="d5",
     q="Which knowledge source is the right candidate for a CONNECTOR rather than a file "
       "upload?",
     options={
         "A": "The company's brand-voice guide, revised roughly once a year.",
         "B": "The sales team's pipeline tracker in Google Drive, updated many times daily "
              "and queried for current status.",
         "C": "A published industry white paper the team references occasionally.",
         "D": "Last year's annual report, used for historical comparisons.",
     },
     answer="B",
     why="Connectors earn their governance overhead when the source changes faster than "
         "anyone would re-upload and currency matters — a live pipeline tracker is the "
         "textbook case. Slow-changing and static documents are well served by uploads "
         "with a review date.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.2"),

dict(task="5.2", domain="d5",
     q="To 'give Claude full context,' an associate proposes connecting the company's "
       "entire shared drive to a team Project. What is the primary problem?",
     options={
         "A": "Connectors slow down response times proportionally to drive size.",
         "B": "Connector scope is an access decision: a whole-drive connection sweeps in "
              "confidential folders (HR, legal, M&A) nobody intended to expose, and buries "
              "relevant content in noise — scope to the folders the work needs.",
         "C": "Whole drives can only be connected by administrators.",
         "D": "Nothing — more context always improves answers.",
     },
     answer="B",
     why="Connecting a source grants the Project's users indirect reach into everything "
         "connected — data governance, not convenience, sets the boundary. Minimal scoping "
         "both protects sensitive folders and keeps retrieval signal high. 'More is always "
         "better' is exactly the instinct that causes connector incidents.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.2"),

dict(task="5.3", domain="d5",
     q="Which Project instruction is written in the most effective form?",
     options={
         "A": "\"Always be accurate and double-check your work.\"",
         "B": "\"If a question involves pricing exceptions, discounts beyond list, or "
              "contract terms, respond only: 'Escalate to Deal Desk' — do not draft an "
              "answer.\"",
         "C": "\"Try to be consistent with how the team usually handles things.\"",
         "D": "\"Use good judgment about when questions are outside your scope.\"",
     },
     answer="B",
     why="Effective instructions are specific and testable — named categories, exact "
         "required behavior, checkable compliance. Accuracy exhortations, appeals to "
         "unstated team norms, and delegated 'good judgment' all fail the "
         "could-a-stranger-verify-it test.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.3"),

dict(task="5.3", domain="d5",
     q="After every incident, a team adds another rule to its Project instructions. A year "
       "later there are 60+ rules, some contradictory, and behavior is erratic. What "
       "maintenance does this configuration need?",
     options={
         "A": "More rules covering the cases where behavior is erratic.",
         "B": "A pruning review: consolidate overlaps, resolve contradictions, delete "
              "obsolete rules, and prioritize the few hard constraints — few sharp rules "
              "outperform many soft ones.",
         "C": "Splitting into two Projects, each with 30 rules.",
         "D": "Moving all 60 rules into a knowledge document instead.",
     },
     answer="B",
     why="Instruction sprawl is a failure mode: conflicting standing orders produce "
         "erratic compliance, and each incident-driven addition compounds it. The fix is "
         "editorial — prune, consolidate, prioritize. Adding more rules feeds the "
         "pathology; relocating the pile unread just changes where it rots.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.3"),

dict(task="5.4", domain="d5",
     q="Who or what should ensure a business team's Project knowledge stays current after "
       "policies and prices change?",
     options={
         "A": "The model, which should notice its documents have gone stale.",
         "B": "A named owner operating agreed update triggers ('policy published → swap the "
              "doc within a week') plus a periodic review sweep with visible versioning.",
         "C": "Whichever team member next notices a wrong answer.",
         "D": "IT, through an annual archive-and-rebuild of all Projects.",
     },
     answer="B",
     why="No model can detect that reality changed outside its knowledge — currency is an "
         "ownership process: someone accountable, event triggers tied to how the source "
         "documents actually change, and periodic sweeps. 'Whoever notices' means users "
         "absorb the errors first; annual rebuilds guarantee up to a year of staleness.",
     ref="D5 Configuration and Knowledge Management — Lesson 5.4"),

# ================= DOMAIN 6 — Governance, Risk, and Responsible Use (9) =================

dict(task="6.1", domain="d6",
     q="Which of the following is the MOST appropriate Claude use case for a business "
       "associate, as stated and without additional controls?",
     options={
         "A": "Summarizing this week's customer feedback into themes for the product team.",
         "B": "Issuing final approval or denial of employee expense claims.",
         "C": "Sending AI-drafted responses to press inquiries without review.",
         "D": "Determining which employees are selected in a restructuring.",
     },
     answer="A",
     why="Feedback summarization is low-stakes, reversible, easily spot-checked, and "
         "decision-supporting rather than decision-making. The other three are consequential "
         "decisions about people or public statements with no review before impact — "
         "categories where AI may assist analysis but a human must decide.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.1"),

dict(task="6.1", domain="d6",
     q="A workflow began with Claude drafting rejection emails that recruiters personalized "
       "and sent. Over months, recruiters started forwarding the drafts unread, and now a "
       "manager proposes letting the system send them directly. What should an associate "
       "recognize?",
     options={
         "A": "Natural workflow maturation — automation earning trust over time.",
         "B": "Scope creep from assist to decide: the human review that made the use case "
              "appropriate has eroded, and the proposal should trigger a fresh "
              "appropriateness screen before any further automation.",
         "C": "A model upgrade opportunity to improve the drafts.",
         "D": "An efficiency win to implement, since complaints have not increased.",
     },
     answer="B",
     why="Use-case fitness was conditional on human judgment in the loop; when review "
         "decays to rubber-stamping and then removal, the workflow has silently crossed "
         "into autonomous decisions about people. The drift itself is the risk signal — "
         "re-screen before automating further, regardless of complaint volume so far.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.1"),

dict(task="6.2", domain="d6",
     q="An HR associate wants Claude's help analyzing exit-interview themes. The transcripts "
       "contain names, managers' names, and health disclosures. Policy restricts sharing "
       "personal data with AI tools. What is the compliant approach?",
     options={
         "A": "Upload the transcripts unmodified — exit interviews are internal documents.",
         "B": "Redact names, identifying details, and the health disclosures (which get "
              "special-category handling), then analyze the anonymized themes.",
         "C": "Upload everything but add 'treat this as confidential' to the prompt.",
         "D": "Cancel the analysis — exit data is too sensitive for any AI use.",
     },
     answer="B",
     why="Theme analysis survives anonymization intact, and health disclosures carry "
         "heightened protection in most regimes — redaction before upload satisfies policy "
         "while preserving the value. 'Internal' is not a data classification, prompt-level "
         "confidentiality requests are not controls, and abandonment is unnecessary when "
         "minimization works.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.2"),

dict(task="6.2", domain="d6",
     q="An associate removed the name column from a dataset before uploading it, but each "
       "row still contains job title, office location, and start date in a 40-person "
       "company. What should they consider?",
     options={
         "A": "The dataset is anonymized — the names are gone.",
         "B": "Combinations of quasi-identifiers can re-identify individuals in a small "
              "population; aggregate or generalize the fields (or consult the privacy "
              "owner) before treating the data as anonymized.",
         "C": "Anonymization only matters for customer data, not employee data.",
         "D": "Adding a 'do not identify individuals' instruction resolves the residual risk.",
     },
     answer="B",
     why="'Marketing Director, Munich office, started March 2024' identifies one person as "
         "surely as their name in a 40-person firm — anonymization is defeating "
         "re-identification, not deleting one column. Employee data is personal data, and "
         "model instructions are not privacy controls.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.2"),

dict(task="6.2", domain="d6",
     q="A teammate suggests pasting a customer's contract into a personal free-tier AI "
       "account 'since our corporate Claude workspace is at its seat limit this week.' What "
       "is the correct response?",
     options={
         "A": "Agree, provided the contract is deleted from the account afterwards.",
         "B": "Decline: customer contractual data in an unapproved personal tool violates "
              "data-handling policy and likely customer confidentiality terms — resolve the "
              "seat issue or use another approved channel instead.",
         "C": "Agree, but paste only the first half of the contract to reduce exposure.",
         "D": "Agree if the customer's name is replaced with an alias.",
     },
     answer="B",
     why="The violation is the destination, not the volume: unapproved personal tools sit "
         "outside the org's data-processing agreements and controls, and customer "
         "confidentiality clauses typically prohibit exactly this. Post-hoc deletion, "
         "partial pastes, and cosmetic aliases don't change the destination.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.2"),

dict(task="6.3", domain="d6",
     q="An associate's new AI use case — summarizing recorded customer calls — is not "
       "mentioned anywhere in the company's AI policy. How should they proceed?",
     options={
         "A": "Proceed; anything not prohibited is permitted.",
         "B": "Treat 'undefined' as 'not yet approved': ask the AI governance owner, since "
              "call recordings raise consent and personal-data questions the policy's "
              "authors may not have considered.",
         "C": "Proceed quietly and stop if anyone objects.",
         "D": "Wait for the next annual policy revision before doing anything.",
     },
     answer="B",
     why="Policy silence on a novel, data-sensitive use case is a question, not a "
         "permission — recorded calls involve consent and personal data, exactly what "
         "governance exists to evaluate. Silence-as-permission and forgiveness-later create "
         "shadow AI; waiting a year is unnecessary when a governance channel exists.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.3"),

dict(task="6.3", domain="d6",
     q="Company policy requires labeling AI-assisted content in client deliverables. A "
       "manager tells an associate to skip the label 'because clients get nervous about "
       "AI.' What should the associate do?",
     options={
         "A": "Follow the manager's instruction — managers outrank policy in their own area.",
         "B": "Keep the disclosure, tell the manager the policy requires it, and if the "
              "manager insists, route the conflict to the policy owner rather than silently "
              "violating or silently complying.",
         "C": "Skip the label but keep private notes proving AI was used.",
         "D": "Add the label in a font too small to notice.",
     },
     answer="B",
     why="A manager's preference doesn't amend policy — and disclosure rules exist "
         "precisely because omitting them misleads clients. Comply with the policy, "
         "surface the conflict through the channel that owns it. Secret notes and "
         "micro-fonts are bad-faith versions of the same violation.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.3"),

dict(task="6.4", domain="d6",
     q="A published, Claude-assisted market report is found to contain a material factual "
       "error. The associate who produced it says 'the AI generated that section.' What is "
       "the correct accountability position?",
     options={
         "A": "Correct — responsibility lies with the tool that produced the error.",
         "B": "The human who reviewed, approved, and published the content owns the error; "
              "AI assistance never transfers accountability, which is why review exists.",
         "C": "Responsibility is split evenly between the associate and the vendor.",
         "D": "No one is accountable, since the workflow was approved by governance.",
     },
     answer="B",
     why="'The AI did it' is the accountability anti-pattern: tools don't hold "
         "responsibility, publishers do. A human name stands behind every consequential "
         "output — that principle is what makes review non-optional, and approved workflows "
         "assign accountability rather than dissolving it.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.4"),

dict(task="6.4", domain="d6",
     q="Before relying on a Claude-assisted scoring aid that prioritizes which customer "
       "complaints get expedited handling, what bias check is most important?",
     options={
         "A": "Confirm the scoring prompt does not contain any demographic words.",
         "B": "Compare expedite rates across customer groups and regions over a sample "
              "period, looking for systematic skew the scoring may have learned from "
              "historical handling patterns.",
         "C": "Ask the model whether its scoring is fair.",
         "D": "None — complaint routing is operational, not people-affecting.",
     },
     answer="B",
     why="Bias is detected in outcomes, not vocabulary: proxies (product tier, region, "
         "writing style) can skew results without a single demographic term in the prompt. "
         "Prioritization decides whose problems get solved first — that is people-affecting, "
         "and models cannot audit their own fairness.",
     ref="D6 Governance, Risk, and Responsible Use — Lesson 6.4"),

# ================= DOMAIN 7 — Troubleshooting and Optimization (6) =================

dict(task="7.1", domain="d7",
     q="Claude's answers about a team's travel policy are correct on general rules but "
       "consistently wrong about reimbursement limits, which changed last month. What is "
       "the most likely cause and fix?",
     options={
         "A": "The model tier is too low — upgrade and retry the same question.",
         "B": "The Project's policy document predates the change — replace the stale "
              "knowledge source and re-test the failing questions.",
         "C": "The prompt lacks emphasis — add 'pay special attention to limits.'",
         "D": "Context overflow — start a new conversation.",
     },
     answer="B",
     why="Correct-in-general but wrong-on-recent-specifics is the signature of a stale "
         "knowledge source: the model faithfully reports the outdated document it was "
         "given. Model tier, emphasis phrases, and fresh chats all leave the wrong "
         "document in place.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.1"),

dict(task="7.1", domain="d7",
     q="A troubleshooting associate changes the prompt wording, swaps the model, AND "
       "replaces a knowledge file — and the workflow starts working. What is the problem "
       "with this outcome?",
     options={
         "A": "Nothing — working is working.",
         "B": "Three variables changed at once, so nobody knows which fix mattered; the "
              "diagnosis is lost, the two unnecessary changes carry ongoing cost, and the "
              "same failure will take just as long to solve next time.",
         "C": "The model swap was wasteful; the other two changes were free.",
         "D": "Every fix should have been applied twice to confirm it.",
     },
     answer="B",
     why="Change-one-variable-and-re-test is what converts a fix into knowledge: bundled "
         "changes hide the cause, may leave you paying for an unneeded model upgrade, and "
         "teach nothing reusable. 'It works now' without knowing why is a debt, not a "
         "resolution.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.1"),

dict(task="7.2", domain="d7",
     q="A month after launch, an AI-drafting workflow's outputs are consistently edited to "
       "shorten the openings and remove a boilerplate paragraph — the same edits, by many "
       "users. What should the workflow owner do?",
     options={
         "A": "Nothing — editing drafts is what users are supposed to do.",
         "B": "Treat the repeated edit pattern as calibration feedback: update the "
              "prompt/instructions so drafts start where users keep moving them, then "
              "confirm the edit rate drops.",
         "C": "Ask users to stop editing so outputs stay measurable.",
         "D": "Rebuild the workflow on a more capable model.",
     },
     answer="B",
     why="Systematic identical edits are the workflow telling you its default output is "
         "mis-calibrated — encoding the pattern into the configuration removes repeated "
         "manual labor. Ignoring the signal wastes everyone's time forever; suppressing "
         "edits destroys the feedback; the model isn't the variable that's wrong.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.2"),

dict(task="7.2", domain="d7",
     q="An executive sponsor emails: 'My assistant said the AI summaries missed the point "
       "once last week. Shut the pilot down?' Weekly metrics show a 94% acceptance rate "
       "across 300 summaries. How should the associate respond?",
     options={
         "A": "Shut the pilot down — executive concerns override metrics.",
         "B": "Investigate the specific failed summary, report findings alongside the "
              "systematic acceptance data, and recommend continuing while fixing whatever "
              "the single case reveals.",
         "C": "Dismiss the complaint — one failure in 300 is statistically negligible.",
         "D": "Remove the assistant's account from the pilot group.",
     },
     answer="B",
     why="Anecdotes get investigated, not obeyed and not dismissed: the single case may "
         "reveal a real edge case worth fixing, while the systematic evidence (94%/300) is "
         "what decisions should rest on. Killing a measured pilot over unexamined n=1 — or "
         "shooting the messenger — both abandon evidence-based adjustment.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.2"),

dict(task="7.3", domain="d7",
     q="A working AI-assisted report pipeline costs 40 staff-minutes per report: 10 for "
       "drafting with re-pasted context, 25 waiting in a single reviewer's queue, and 5 for "
       "distribution. Where should optimization start?",
     options={
         "A": "The drafting step — AI response speed is the core of an AI workflow.",
         "B": "The review queue — it is 60% of cycle time; restructure it (risk-flagged "
              "deep review + spot-checks) while a Project eliminates the re-pasted context.",
         "C": "Distribution, since it is the final step users see.",
         "D": "All three steps simultaneously, for maximum improvement.",
     },
     answer="B",
     why="Optimization follows the profile: the bottleneck is the human queue, not the AI "
         "seconds — restructuring review attention (and templating the context ritual) "
         "attacks the actual 25 minutes. Polishing the smallest slices or changing "
         "everything at once ignores where the time goes and blurs cause and effect.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.3"),

dict(task="7.3", domain="d7",
     q="To cut costs, a team moves its customer-visible FAQ generation to the fastest, "
       "cheapest model and removes the editorial review 'since quality has been fine for "
       "months.' What optimization principle does this violate?",
     options={
         "A": "None — removing unneeded steps is the definition of optimization.",
         "B": "Efficiency changes must keep the quality safeguard and a visible quality "
              "metric: downsizing the model AND removing the safety net at once, on "
              "customer-facing output, is cost-cutting with no way to see the degradation "
              "it may cause.",
         "C": "Customer-facing content should always use the most capable model.",
         "D": "Editorial review should be replaced by a second model, not removed.",
     },
     answer="B",
     why="The review net is what MADE the historical quality 'fine' — removing it while "
         "simultaneously reducing model capability changes two variables against quality "
         "with zero instrumentation on customer-visible output. Right-sizing models is "
         "legitimate; doing it blind and netless is the classic effectiveness-for-"
         "efficiency trade the exam penalizes.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.3"),
]
