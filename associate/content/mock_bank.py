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
         "A": "\"Write an announcement about the product delay for our enterprise customers "
              "— make it sincere, on-brand, and not too corporate.\"",
         "B": "\"Draft a 150-word candid email to enterprise customers: Q3 release moves to "
              "November, the reason, impact on commitments, a named contact.\"",
         "C": "\"Write a very professional, high-quality, detailed announcement about the "
              "product delay. Tone and accuracy matter enormously, so make it excellent.\"",
         "D": "\"You are the world's best crisis communications expert with 30 years at "
              "Fortune 100 companies. Write our product delay announcement.\"",
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
         "A": "An explicit output-format specification — for example, '5 bullets, max 12 "
              "words each.'",
         "B": "A politeness marker: models are trained on human dialogue and respond better "
              "to courteous phrasing.",
         "C": "A more capable model tier, since slide-ready business content demands "
              "stronger reasoning.",
         "D": "Longer background about the company, so the model can judge what belongs on "
              "the slide.",
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
         "A": "Ask for the whole document again, adding 'be thorough and keep it internally "
              "consistent throughout.'",
         "B": "Decompose it: outline first, then each section drafted in sequence, reviewed "
              "before the next builds on it.",
         "C": "Generate the full document five times and merge the strongest chapters from "
              "the different runs.",
         "D": "Split it across five parallel chats, one per section, with the same brief in "
              "each, and staple the results together.",
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
         "A": "Review only the final combined deliverable, to preserve momentum.",
         "B": "Review after every step whose output feeds the next step.",
         "C": "Review is unnecessary if each step's prompt was well-written.",
         "D": "Review at random intervals, so the checking stays unbiased.",
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
         "A": "\"This isn't right — try again. I need something a lot closer to what our "
              "customers actually ask us about.\"",
         "B": "\"Keep the ten answers. Rewrite at an 8th-grade level; add billing, "
              "cancellation, and data-export entries from the policy.\"",
         "C": "\"Make it simpler and more complete — the reading level is too high and "
              "several topics are still missing entirely.\"",
         "D": "Start a fresh chat with a much longer, more detailed opening prompt and "
              "regenerate all ten answers from scratch.",
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
              "competitor's pricing data.",
         "B": "The model has hit its capability ceiling here; a more capable tier is the "
              "only remaining fix.",
         "C": "The feedback wording is too gentle; firmer, more directive phrasing will "
              "force convergence.",
         "D": "The conversation belongs in a Project, whose instructions would keep the "
              "revisions consistent.",
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
         "A": "Vendor scoring → a large batch of unfiltered creative options; campaign "
              "concepts → one polished recommendation.",
         "B": "Campaign concepts → many diverse, unjudged ideas; vendor scoring → explicit "
              "criteria and a structured table.",
         "C": "Board memo → maximum idea quantity; market entrants → a single polished "
              "narrative written from memory.",
         "D": "All four in one combined prompt, so that the four outputs stay consistent "
              "with each other.",
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
         "A": "Nothing — brainstorming surfaces more possibilities than a narrow, direct "
              "question would.",
         "B": "Research tasks need real sources and verification; ideation prompts invite "
              "plausible invention.",
         "C": "The prompt should have asked for more ideas, since coverage improves with "
              "the number generated.",
         "D": "Legislation is a regulated topic, so drafting anything about it with an AI "
              "tool is prohibited.",
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
         "A": "None needed — it matches the associate's own recollection of how the deal "
              "was negotiated.",
         "B": "Check key terms and dates against the contract, and confirm it covers the "
              "sections the decision needs.",
         "C": "Ask Claude to re-read the contract and confirm its own summary is accurate "
              "and complete.",
         "D": "Compare its length and structure against summaries of similar vendor "
              "contracts from last year.",
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
         "A": "Re-read the proposal, checking each section for risks the six items miss.",
         "B": "Check whether six risks is a typical number for supplier proposals of this "
              "size and complexity.",
         "C": "Check that each of the six risks is well-reasoned and clearly explained in "
              "the response.",
         "D": "Ask Claude whether its list is complete and whether it left anything "
              "material out.",
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
         "A": "The report is probably paywalled or client-only, so the citation can stand "
              "and the statistic holds.",
         "B": "The model fabricated a plausible citation; the statistic needs a real "
              "source.",
         "C": "The model drew on a licensed database that the associate's account cannot "
              "reach.",
         "D": "The page number is slightly wrong, but the statistic itself is still "
              "trustworthy.",
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
         "A": "A rounding or presentation convention — pick whichever figure reads better "
              "and use it throughout.",
         "B": "An internal inconsistency: trace both figures to the source data before the "
              "report is used.",
         "C": "A hallucinated citation — remove both figures and the surrounding paragraph.",
         "D": "Expected behavior in long outputs, where figures drift over length; no "
              "action is needed here.",
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
         "A": "The criteria are objective, since they were derived from the team's real "
              "performance data.",
         "B": "The output may encode bias from a skewed sample; check it against the job "
              "spec.",
         "C": "The model is malfunctioning and the behavior should be reported to the "
              "vendor's support.",
         "D": "Adding more of the team's best-performer profiles to the sample will balance "
              "the criteria out.",
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
         "A": "(a) the competitor's press release; (b) recompute the figure; (c) find the "
              "original interview.",
         "B": "All three: ask Claude to double-check its own work before the brief "
              "circulates.",
         "C": "(a) and (c) need no validation; (b) should be rounded to a safe range before "
              "publication.",
         "D": "All three: accept any claim that at least two other AI assistants "
              "independently agree with.",
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
         "A": "Give every claim equal time, so the validation effort stays consistent and "
              "defensible in an audit.",
         "B": "By stakes: deep-verify what the decision rests on, spot-check the "
              "low-consequence rest.",
         "C": "Fully validate the ten easiest claims and flag the remaining ten as "
              "unverified.",
         "D": "Skip validation this once and add a general disclaimer about AI-assisted "
              "content to the deck.",
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
         "A": "The summary is validated: the model checked its own work and confirmed it is "
              "correct.",
         "B": "Essentially nothing — models reaffirm their own errors; the rule text is the "
              "check.",
         "C": "The summary is now more likely correct, since a wrong answer wouldn't "
              "survive a challenge.",
         "D": "The summary is probably wrong, since an honest model expresses doubt when "
              "challenged.",
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
         "A": "A written explanation of severance terms to be sent to a departing employee "
              "this week.",
         "B": "A first-draft agenda and notes for the team's internal weekly sync.",
         "C": "A public statement responding to a customer's rumor about a data breach at "
              "the company.",
         "D": "Dosage-related wording for the user leaflet of a home medical device.",
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
         "A": "Nothing is wrong — routing every output through legal is the maximally safe "
              "posture.",
         "B": "Review must track risk: flooding reviewers with trivia degrades scrutiny.",
         "C": "Legal review should be replaced by a second model reviewing the first "
              "model's output.",
         "D": "Reviews should be sampled at random, 10% of outputs, regardless of what they "
              "contain.",
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
         "A": "Send the same document to both audiences — the underlying facts don't change "
              "with the reader.",
         "B": "Generate two variants: decisions and impact for the board, specifics for "
              "engineering.",
         "C": "Send the board a shortened copy with the technical paragraphs deleted from "
              "the middle.",
         "D": "Send engineering the board version with a glossary of the business terms "
              "appended.",
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
         "A": "Definition → an inline chat answer; matrix → a structured artifact the teams "
              "update.",
         "B": "Both inline in chat, so the whole thread stays in one searchable place for "
              "everyone.",
         "C": "Both as artifacts, since artifacts are more professional and easier to "
              "share.",
         "D": "Definition → a table for precision; matrix → prose so it reads more "
              "naturally.",
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
         "A": "None — the content is complete, and the meeting can work through the prose "
              "together.",
         "B": "Group by category, rank by severity, put the top five in a table, appendix "
              "the rest.",
         "C": "Cut the assessment down to the five most severe items so that it fits on a "
              "single slide.",
         "D": "Convert every one of the 25 items into its own small table, for consistency.",
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
         "A": "A Project holding the decks and templates, with research mode used in it for "
              "current facts.",
         "B": "Research mode for every question, since it is the most capable feature "
              "available to the team.",
         "C": "A plain chat, with the methodology decks re-uploaded whenever they seem "
              "relevant to a question.",
         "D": "An artifact containing the methodology content, pasted as a reference into "
              "each new chat.",
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
         "A": "As current — the entries carry specific dates, amounts, and named investors.",
         "B": "As unreliable for recency: training data has a cutoff — use research mode.",
         "C": "As current, provided the chat was started today and the question explicitly "
              "named this quarter.",
         "D": "As reliable, once the model has confirmed the list is up to date when asked.",
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
         "A": "Haiku for the nuanced multi-document legal risk analysis; Opus for tagging "
              "the 10,000 tickets.",
         "B": "Haiku for tagging 10,000 tickets; Sonnet for report drafting; Opus for the "
              "legal analysis.",
         "C": "Opus for all three, to standardize the team on one model and simplify "
              "support and billing.",
         "D": "Sonnet for all three, since it balances capability, cost, and latency for "
              "any workload.",
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
         "A": "At 50,000 calls a month, per-call cost and latency multiply with no matching "
              "quality gain.",
         "B": "More capable models are measurably less accurate on simple classification "
              "work.",
         "C": "The most capable model should be reserved for executive and customer-facing "
              "work only.",
         "D": "There is no counterpoint; maximum capability is always the safe default at "
              "any volume.",
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
         "A": "Start with the most capable model and step down only when the budget owner "
              "complains about spend.",
         "B": "State volume, latency, and accuracy requirements; pilot the cheapest model "
              "that could meet them.",
         "C": "Use the mid-tier model — it is a safe compromise for essentially any "
              "extraction task.",
         "D": "Survey which models other companies use for invoice extraction and match "
              "their choice.",
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
         "A": "The model was updated mid-project, so its behavior changed; wait for the "
              "next release to settle.",
         "B": "The chat exceeds its practical context window; summarize into a Project and "
              "restart.",
         "C": "The prompts have grown too polite; firmer, more directive language restores "
              "compliance.",
         "D": "Nothing is wrong — contradictions are normal variance and can be corrected "
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
         "A": "Ask for a structured summary of decisions and next steps, saved into Project "
              "knowledge.",
         "B": "Keep the chat open in a browser tab so that its context stays warm for next "
              "week's session.",
         "C": "Nothing — the conversation history is a permanent record you can scroll back "
              "through.",
         "D": "Copy the whole transcript into the first message of next week's chat to "
              "restore context.",
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
         "A": "Generate a modern report template right away, so the director sees quick, "
              "visible progress.",
         "B": "Analyze the request first: current reports, consumers, pain points, and "
              "success criteria.",
         "C": "Research reporting-tool vendors and their pricing so the options are on the "
              "table early.",
         "D": "Rebuild last quarter's report in a new format as a demo of what modern could "
              "mean.",
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
         "A": "Include it in the plan — the inference is reasonable and CRM integration is "
              "common.",
         "B": "Treat it as a candidate requirement and validate it with stakeholders before "
              "committing.",
         "C": "Discard it outright — a model should never propose requirements no "
              "stakeholder asked for.",
         "D": "Ask Claude to rate its confidence and include the requirement if it exceeds "
              "80%.",
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
         "A": "\"Our invoice process is slow. How do most companies usually speed this "
              "up?\"",
         "B": "The documented process — steps, owners, durations, volumes — with a request "
              "to rank fixes.",
         "C": "\"List the top ten process-optimization frameworks and explain when each one "
              "applies.\"",
         "D": "The org chart, so Claude understands who is involved at each stage of the "
              "approval.",
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
         "A": "AI-generated plans are unusable for real project scheduling and shouldn't be "
              "attempted at all.",
         "B": "Draft plans save time, but dependency logic needs human validation before "
              "adoption.",
         "C": "The prompt should have instructed the model not to make any dependency "
              "errors.",
         "D": "Planning needs the most capable model tier, which would not have made this "
              "mistake.",
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
         "A": "The proposal arrived too quickly to have been thought through and can't be "
              "trusted.",
         "B": "No alternatives were compared against criteria, so its trade-offs stay "
              "invisible.",
         "C": "Claude's designs must always be discarded and rebuilt from scratch by the "
              "humans.",
         "D": "A single proposal cannot be piloted, because there is no comparison to "
              "measure it.",
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
         "A": "Extend the pilot unchanged for another two weeks to gather more evidence "
              "before changing anything.",
         "B": "Fix the diagnosed cause — require the missing tab, add a rubric — then "
              "re-pilot.",
         "C": "Declare the design a failure and return the team to the previous manual "
              "process now.",
         "D": "Lower the success criteria so that the current design passes on the existing "
              "inputs.",
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
         "A": "Claude drafts variance commentary and flags anomalies; accountants judge and "
              "sign off.",
         "B": "Claude approves journal entries below a set threshold, to relieve the team's "
              "workload.",
         "C": "Claude runs the entire close and accountants audit the results once each "
              "quarter.",
         "D": "Claude is excluded entirely — financial close processes cannot involve AI "
              "assistance.",
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
         "A": "A more capable model, which would have earned the writers' trust on its own.",
         "B": "Change management: trust boundaries, error ownership, and training on the "
              "new flow.",
         "C": "A mandate from leadership requiring writers to use the tool on every "
              "proposal they draft.",
         "D": "Nothing — adoption of a new tool always takes years to reach meaningful "
              "usage levels.",
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
         "A": "\"Yes — current models outperform human analysts on most of the day-to-day "
              "analytical work.\"",
         "B": "\"It absorbs the drafting and first-pass analysis; judgment and "
              "accountability don't transfer.\"",
         "C": "\"No — AI tools are far too unreliable to be trusted with analytical work of "
              "this kind.\"",
         "D": "\"That depends entirely on which models ship over the next year, so it is "
              "too early to say.\"",
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
         "A": "The mitigation the workflow builds in: a verification step, current sources, "
              "restarts.",
         "B": "A technical explanation of why transformer architectures exhibit each of "
              "these behaviors.",
         "C": "A comparison showing that competitors' AI tools share exactly the same "
              "weaknesses.",
         "D": "Nothing further — limitations should be stated plainly and not dwelt on in a "
              "briefing.",
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
         "A": "Stable rules as instructions; documents as knowledge; one-off details in "
              "chat.",
         "B": "Everything in the instructions, so that nothing is ever missed by any chat "
              "in the Project.",
         "C": "Everything as knowledge documents, including the tone and escalation rules "
              "for chats.",
         "D": "Everything in the first message of each chat, so the context is visible and "
              "auditable.",
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
         "A": "Ask members to paste the style guide more carefully, from the newest "
              "published version.",
         "B": "Configure it: durable rules as instructions, the style guide as a knowledge "
              "document.",
         "C": "Create one pinned chat holding the style guide that everyone continues from "
              "each time.",
         "D": "Replace the Project with a longer prompt template kept in the team's "
              "internal wiki.",
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
         "A": "The company's brand-voice guide, revised roughly once a year by the "
              "marketing team.",
         "B": "The pipeline tracker in Google Drive, updated many times daily and queried "
              "for status.",
         "C": "A published industry white paper that the team references occasionally "
              "during client work.",
         "D": "Last year's annual report, used as a fixed baseline for historical "
              "comparisons.",
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
         "A": "Connectors slow responses down in proportion to the size of the drive "
              "connected.",
         "B": "Scope is an access decision: a whole drive sweeps in HR, legal, and M&A "
              "material.",
         "C": "Whole drives can only be connected by a workspace administrator, not by an "
              "associate.",
         "D": "Nothing — more available context reliably improves the quality of Claude's "
              "answers.",
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
         "A": "\"Always be accurate, and double-check your work before you give me an "
              "answer.\"",
         "B": "\"For pricing exceptions or contract terms, reply only 'Escalate to Deal "
              "Desk.'\"",
         "C": "\"Try to stay consistent with the way the team usually handles these "
              "requests.\"",
         "D": "\"Use good judgment about when a question falls outside your scope, and say "
              "so.\"",
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
         "A": "Add further rules that cover the specific cases where the behavior has been "
              "erratic lately.",
         "B": "A pruning review: consolidate overlaps, resolve contradictions, keep few "
              "sharp rules.",
         "C": "Split the Project into two, each carrying about thirty of the existing "
              "rules.",
         "D": "Move all sixty rules into a knowledge document and leave the instructions "
              "empty.",
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
         "A": "The model, which should notice when the documents it was given have gone "
              "stale.",
         "B": "A named owner with update triggers and a periodic review sweep, with "
              "versioning.",
         "C": "Whichever team member is the next to notice that an answer has come back "
              "wrong.",
         "D": "IT, through an annual archive-and-rebuild of every Project it maintains.",
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
         "B": "Issuing the final approval or denial decision on employee expense claims.",
         "C": "Sending AI-drafted responses to press inquiries without any human review.",
         "D": "Deciding which employees are selected for redundancy in a restructuring.",
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
         "A": "Natural maturation of the workflow — the automation has steadily earned "
              "trust over time.",
         "B": "Scope creep from assist to decide: re-screen before automating any further.",
         "C": "An opportunity to upgrade the model so the unread drafts come out even "
              "stronger.",
         "D": "An efficiency win worth implementing, since candidate complaints have not "
              "increased.",
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
         "A": "Upload the transcripts unmodified, since exit interviews are internal "
              "documents.",
         "B": "Redact names and the health disclosures, then analyze the anonymized themes.",
         "C": "Upload everything, but add 'treat this as confidential' to the top of the "
              "prompt.",
         "D": "Cancel the analysis — exit interview data is too sensitive for any AI use at "
              "all.",
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
         "A": "The dataset is anonymized — the name column was removed before it was "
              "uploaded.",
         "B": "Quasi-identifiers can re-identify people in a 40-person firm; generalize the "
              "fields.",
         "C": "Anonymization requirements apply only to customer data, not internal "
              "employee records.",
         "D": "Adding a 'do not identify individuals' instruction resolves the residual "
              "risk here.",
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
         "A": "Agree, provided the contract is deleted from the personal account "
              "immediately afterwards.",
         "B": "Decline: customer data in an unapproved personal tool breaches policy.",
         "C": "Agree, but paste only the first half of the contract, to reduce the total "
              "exposure.",
         "D": "Agree if the customer's name and signature block are replaced with a neutral "
              "alias.",
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
         "A": "Proceed — anything the policy does not explicitly prohibit is permitted by "
              "default.",
         "B": "Treat undefined as not yet approved and ask the governance owner about "
              "consent.",
         "C": "Proceed quietly for now, and stop the moment somebody raises an objection to "
              "it.",
         "D": "Wait for the next annual policy revision to address the case before doing "
              "anything.",
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
         "A": "Follow the manager's instruction — managers outrank written policy within "
              "their own area.",
         "B": "Keep the disclosure, cite the policy, and escalate to the policy owner if "
              "pressed.",
         "C": "Skip the label, but keep private notes proving that AI assistance was used.",
         "D": "Add the label in a font small enough that clients are unlikely to notice it.",
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
         "A": "Correct — responsibility sits with the tool that generated the erroneous "
              "section.",
         "B": "The human who reviewed, approved, and published it owns the error; review is "
              "why.",
         "C": "Responsibility is split evenly between the associate and the model's vendor.",
         "D": "Nobody is accountable, since the governance team approved this workflow "
              "already.",
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
         "A": "Confirm the scoring prompt contains no demographic words or protected "
              "attributes.",
         "B": "Compare expedite rates across customer groups over a sample period, looking "
              "for skew.",
         "C": "Ask the model whether its own scoring is fair to all customer groups "
              "equally.",
         "D": "None — complaint routing is an operational process, not a people-affecting "
              "one.",
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
         "A": "The model tier is too low — upgrade to a stronger model and ask the same "
              "question.",
         "B": "The Project's policy document predates the change — replace it and re-test.",
         "C": "The prompt lacks emphasis — add 'pay special attention to reimbursement "
              "limits.'",
         "D": "Context overflow in a long conversation — start a fresh chat and ask again.",
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
         "A": "Nothing is wrong — the workflow works again, which is the point of "
              "troubleshooting.",
         "B": "Three variables changed at once, so the actual cause — and the diagnosis — "
              "is lost.",
         "C": "The model swap was wasteful; the other two changes cost nothing and can "
              "stay.",
         "D": "Each of the three fixes should have been applied twice, to confirm it really "
              "held.",
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
         "A": "Nothing — editing the drafts is exactly what the users are supposed to be "
              "doing.",
         "B": "Treat the repeated edits as calibration feedback and update the "
              "instructions.",
         "C": "Ask users to stop editing the drafts so the outputs stay measurable over "
              "time.",
         "D": "Rebuild the workflow on a more capable model that writes tighter openings.",
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
         "A": "Shut the pilot down — a sponsor's concern outweighs the acceptance metrics.",
         "B": "Investigate the failed summary, report it alongside the 94% data, and "
              "continue.",
         "C": "Dismiss the complaint — one failure in 300 summaries is statistically "
              "negligible.",
         "D": "Remove the assistant's account from the pilot group so the complaints stop "
              "coming.",
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
         "A": "The drafting step — response speed is the core of any AI-assisted workflow.",
         "B": "The review queue — it is 60% of cycle time; restructure it and add a "
              "Project.",
         "C": "Distribution, since it is the final step and the one that users actually "
              "see.",
         "D": "All three steps at once, since that produces the largest total improvement.",
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
         "A": "None — removing steps that no longer earn their keep is exactly what "
              "optimizing is.",
         "B": "Efficiency changes must keep the quality safeguard and a visible quality "
              "metric.",
         "C": "Customer-facing content should always run on the most capable model "
              "available.",
         "D": "Editorial review should have been replaced by a second model, not removed "
              "outright.",
     },
     answer="B",
     why="The review net is what MADE the historical quality 'fine' — removing it while "
         "simultaneously reducing model capability changes two variables against quality "
         "with zero instrumentation on customer-visible output. Right-sizing models is "
         "legitimate; doing it blind and netless is the classic effectiveness-for-"
         "efficiency trade the exam penalizes.",
     ref="D7 Troubleshooting and Optimization — Lesson 7.3"),
]
