"""
associate/content/lessons.py — the 30 CCAO-F lessons (one per blueprint objective)
==================================================================================
Each lesson maps 1:1 to an objective in Section 6 of the official Exam Guide.
The `chat` field is a claude.ai-style walkthrough rendered by the console:
  {"who": "user", "label": "Weak prompt" | "Improved prompt" | ..., "text": ...}
  {"who": "claude", "text": ...}
  {"who": "note",  "text": ...}   <- centered divider commentary

Labels containing weak/vague/risky/before render red; improved/better/after/
fixed/safe render green; anything else renders neutral.

Consumed by ui/console-associate/build_data.py.
"""

LESSONS = [

# ============================== DOMAIN 1 — Prompting and Task Execution (14%) ==============================

{"id": "1.1", "d": "d1",
 "title": "Create effective prompts for business and technical tasks",
 "concept": "An effective prompt gives Claude the same things you'd give a capable new "
            "colleague: context (what's going on), a role or audience, the concrete task, "
            "constraints (length, tone, what to include or avoid), and the output format "
            "you want. Vague in, generic out.",
 "analogy": "Briefing a freelancer. 'Write something about our product' gets you a shrug "
            "and a generic draft. A one-paragraph brief — audience, goal, tone, length, "
            "deadline — gets you work you can actually use.",
 "antipattern": "One-line prompts that hide the real requirements in your head — 'summarize "
                "this report' — then blaming the model when the summary is the wrong length, "
                "tone, or focus for the meeting it was for.",
 "right": "State context, role, task, constraints, and format explicitly. 'Summarize this "
          "Q3 ops report in 5 bullets for the executive team; focus on risks and budget "
          "variance; plain language, no jargon.'",
 "pitfall": "Thinking longer prompts are automatically better. Extra words aren't the goal — "
            "missing *requirements* are the problem. A tight prompt with the five elements "
            "beats a rambling one.",
 "tip": "On the exam, the best-prompt option is the one that adds specific context, audience, "
        "constraints, and format — not the longest option, and never the one that just says "
        "'be more detailed'.",
 "links": ["1.3", "7.1"],
 "chat": [
   {"who": "note", "text": "An operations manager needs a summary of a 30-page vendor report."},
   {"who": "user", "label": "Weak prompt", "text": "Summarize this vendor report."},
   {"who": "claude", "text": "Here's a summary of the vendor report:\n\nThe report covers the vendor's quarterly performance across delivery, quality, and cost dimensions. Overall performance was mixed, with strong on-time delivery offset by…\n\n(continues for ~600 generic words)"},
   {"who": "note", "text": "Accurate but useless for its real purpose — a 5-minute leadership briefing. The requirements were never stated."},
   {"who": "user", "label": "Improved prompt", "text": "You're helping me brief our COO. Summarize the attached vendor report in 5 bullets, max 20 words each. Focus on: contract risks, missed SLAs, and anything affecting the Q4 renewal decision. Plain language — no procurement jargon. End with a one-line recommendation."},
   {"who": "claude", "text": "• Vendor missed the 99.5% uptime SLA twice (July, September); credits not yet claimed — ~$18K recoverable.\n• Support response times degraded 40% quarter-over-quarter; root cause unresolved.\n• Contract auto-renews Nov 30 unless notice is given by Oct 31.\n• Pricing is 12% above the benchmark quote received in August.\n• Data-handling addendum still unsigned — a compliance gap flagged in June.\n\nRecommendation: issue the non-renewal notice by Oct 31 to preserve leverage, then renegotiate pricing and the addendum."},
   {"who": "note", "text": "Context + audience + task + constraints + format = an output ready for the meeting."},
 ]},

{"id": "1.2", "d": "d1",
 "title": "Apply task decomposition techniques to structure complex requests",
 "concept": "Big deliverables fail as single prompts. Decompose them into an explicit "
            "sequence of steps — gather, analyze, draft, refine — and run them one at a "
            "time, reviewing between steps. Each step's output becomes the next step's input.",
 "analogy": "You don't ask a contractor to 'build the house' in one sentence. You sequence "
            "it — foundation, framing, wiring — and inspect between phases, catching "
            "problems while they're still cheap to fix.",
 "antipattern": "One mega-prompt: 'Analyze our churn data, identify causes, propose fixes, "
                "and write the board deck.' Claude produces something for each part, but "
                "shallow everywhere, and one early misunderstanding poisons everything after it.",
 "right": "Break it down and checkpoint: (1) 'List the top churn drivers in this data.' Review. "
          "(2) 'For the top 3, propose remediations with effort estimates.' Review. "
          "(3) 'Draft board slides from the agreed table.' Each step is small enough to verify.",
 "pitfall": "Decomposing but never reviewing between steps — chaining prompts blindly is "
            "the mega-prompt with extra steps. The checkpoint IS the point.",
 "tip": "Exam answers that decompose AND insert a human review between steps beat both "
        "'one detailed mega-prompt' and 'fully automate the chain'.",
 "links": ["1.1", "4.2"],
 "chat": [
   {"who": "note", "text": "A project manager needs a full project kickoff pack: risks, timeline, and comms plan."},
   {"who": "user", "label": "Weak prompt", "text": "Create the complete kickoff pack for our warehouse migration project: risk register, timeline, stakeholder map, and comms plan."},
   {"who": "claude", "text": "Here's a complete kickoff pack:\n\n1. Risk register: (8 generic risks — 'scope creep', 'resource constraints'…)\n2. Timeline: a template Gantt with invented dates\n3. Stakeholder map: placeholder roles\n4. Comms plan: weekly status email…\n\n(plausible-looking, but none of it reflects the actual project)"},
   {"who": "note", "text": "Restart, decomposed — step 1 of 3:"},
   {"who": "user", "label": "Improved prompt", "text": "Step 1 of 3. Here's our project brief and the constraints [pasted]. List the 8 most significant risks specific to THIS migration, each with likelihood, impact, and owner-role. Nothing generic — every risk must trace to something in the brief."},
   {"who": "claude", "text": "Based on your brief:\n\n1. Forklift certification lapse — 4 of 9 operators expire mid-migration (High/High, Ops lead)\n2. WMS cutover conflicts with Black Friday freeze window stated in §2 (Med/High, IT PM)\n3. The 3PL contract requires 90-day notice; brief shows 60 days remaining (High/Med, Procurement)\n…"},
   {"who": "user", "text": "Good — risks 1 and 3 are the real ones. Step 2: build a 12-week timeline that resolves those two risks first. I'll review before we draft the comms plan."},
   {"who": "note", "text": "Each step is grounded in reviewed output, so errors can't cascade into the final pack."},
 ]},

{"id": "1.3", "d": "d1",
 "title": "Iterate prompts to improve output quality",
 "concept": "First outputs are drafts. Iterating means giving specific, directional feedback — "
            "what to keep, what to change, what was wrong — rather than accepting mediocre "
            "output or starting over from scratch each time.",
 "analogy": "Editing with a writer, not a vending machine. You don't re-insert coins hoping "
            "for a better snack — you mark up the draft: 'tighter intro, cut the third "
            "section, more data in the middle'.",
 "antipattern": "Re-running the same prompt hoping for luck, or feedback with no direction — "
                "'make it better', 'try again' — which changes everything, including the "
                "parts that were already right.",
 "right": "Anchor what's good, target what isn't: 'Keep the structure and the opening. "
          "Replace the generic benefits in section 2 with the three metrics I gave you, "
          "and cut the length by half.'",
 "pitfall": "Endless iteration on a prompt that's missing information Claude can't invent. "
            "If two rounds of feedback don't converge, the gap is usually missing context — "
            "add inputs, don't just re-phrase.",
 "tip": "The exam rewards specific, directional feedback ('shorter, keep X, fix Y with this "
        "data') over regenerate-and-hope, and over abandoning the tool after one bad draft.",
 "links": ["1.1", "7.2"],
 "chat": [
   {"who": "note", "text": "A comms specialist is drafting an all-hands announcement about a new expense policy."},
   {"who": "user", "text": "Draft a short announcement: new expense policy starts March 1 — receipts required for everything over $25, approvals move from managers to Finance, reimbursements now weekly."},
   {"who": "claude", "text": "Subject: Important Update to Our Expense Policy\n\nTeam,\n\nWe're excited to announce improvements to our expense process, effective March 1! These changes will streamline operations and improve compliance…\n\n(3 more paragraphs of corporate enthusiasm)"},
   {"who": "user", "label": "Vague feedback", "text": "Make it better."},
   {"who": "claude", "text": "Subject: Exciting Changes Coming to Expenses!\n\n(a different draft — new tone, new structure, but the same core problems, and the parts that worked are gone too)"},
   {"who": "note", "text": "Undirected feedback is a coin re-insert. Try again with anchored, specific feedback:"},
   {"who": "user", "label": "Improved feedback", "text": "Keep the subject line and the three policy points. Cut the length by half and drop the 'excited to announce' tone — people dislike this change, so acknowledge it adds a step and explain why (audit findings). End with a link placeholder for the FAQ."},
   {"who": "claude", "text": "Subject: Important Update to Our Expense Policy\n\nTeam,\n\nStarting March 1, three things change about expenses: receipts are required for anything over $25, approvals move to Finance, and reimbursements run weekly.\n\nWe know the receipt rule adds a step. It comes directly from last quarter's audit findings, and it protects everyone at reimbursement time.\n\nQuestions? See the FAQ: [link]"},
 ]},

{"id": "1.4", "d": "d1",
 "title": "Adapt prompting strategies based on task type",
 "concept": "Analysis, research, drafting, and brainstorming each want a different prompt "
            "shape. Analysis wants criteria and structure; research wants scope and sourcing "
            "requirements; drafting wants audience, tone, and format; brainstorming wants "
            "quantity, wide constraints, and explicitly deferred judgment.",
 "analogy": "A workshop's stations: measuring, cutting, sanding, painting. Same wood, "
            "different technique at each station — sanding with the paint sprayer ends badly.",
 "antipattern": "One habitual prompt shape for everything — asking for '10 creative options' "
                "on a compliance analysis, or demanding a single polished answer during "
                "ideation, which kills the variety brainstorming exists to produce.",
 "right": "Name the mode and shape the prompt for it. Brainstorm: 'Give me 15 raw ideas, "
          "no filtering, include unconventional ones.' Analysis: 'Score each vendor against "
          "these 5 criteria in a table, cite the row in the data for each score.'",
 "pitfall": "Mixing modes in one prompt — 'brainstorm ideas and pick the best one and write "
            "the plan' — collapses divergent and convergent thinking into neither.",
 "tip": "Exam stems often hide the task type in a verb: 'explore options' → brainstorming "
        "breadth; 'assess/score' → analysis with criteria; 'find out' → research with "
        "sources; 'prepare a message' → drafting with audience and tone.",
 "links": ["1.1", "4.2"],
 "chat": [
   {"who": "note", "text": "An HR lead wants ideas for improving onboarding — a brainstorming task prompted like an analysis task."},
   {"who": "user", "label": "Wrong mode", "text": "What is the best way to improve our onboarding process?"},
   {"who": "claude", "text": "The most effective single improvement is typically a structured 30-60-90 day plan, because it addresses the most common failure point: unclear expectations. Here's how to implement one…\n\n(one 'best' answer, prematurely converged)"},
   {"who": "note", "text": "Asking for 'the best' collapses ideation into one safe answer. Re-prompt in brainstorm mode:"},
   {"who": "user", "label": "Improved prompt", "text": "Brainstorm mode: give me 15 distinct ways to improve onboarding for remote engineers. No filtering, no ranking — include cheap quick wins AND unconventional ideas. One line each. We'll evaluate afterwards."},
   {"who": "claude", "text": "1. Buddy assigned before day 1, with a budgeted lunch stipend\n2. 'First PR in week 1' — a curated trivial ticket per new hire\n3. Manager sends a 90-second welcome video before start date\n4. Auto-generated 'who to ask about what' map from the org chart\n5. Reverse onboarding: new hire presents fresh-eyes friction report at day 30\n…\n15. 'Documentation bounty' — new hires get rewards for fixing stale docs they hit"},
   {"who": "user", "text": "Now switch to analysis mode: score ideas 2, 5, and 15 on cost, time-to-impact, and effect on ramp time, in a table, and note what data we'd need to validate each."},
   {"who": "claude", "text": "| Idea | Cost | Time-to-impact | Ramp effect | Validation data needed |\n|---|---|---|---|---|\n| First PR in week 1 | Low | Immediate | High — activates learning by doing | Time-to-first-commit history |\n| Reverse onboarding | Low | 30 days | Medium — improves process, not the individual | Friction themes vs. later attrition |\n| Doc bounty | Med | 2–4 weeks | Medium-high | Doc staleness audit, support-question volume |"},
   {"who": "note", "text": "Divergent first, convergent second — two prompts, two shapes, one good decision."},
 ]},

# ============================== DOMAIN 2 — Output Evaluation and Validation (21%) ==============================

{"id": "2.1", "d": "d2",
 "title": "Evaluate Claude-generated outputs for accuracy and completeness",
 "concept": "Evaluation is a two-question habit applied to every output: Is what's here "
            "correct? And is anything missing? Check claims against the source material, and "
            "check coverage against the original request — fluent, confident text earns no "
            "exemption.",
 "analogy": "Proofreading a new analyst's first report. You don't just read it — you check "
            "the numbers against the spreadsheet and the sections against the assignment. "
            "Polish is not accuracy.",
 "antipattern": "Skimming for tone and shipping it because it 'reads well'. Fluency bias is "
                "the trap: the more confident the prose, the less people check it.",
 "right": "Evaluate against ground truth, not against vibes: verify every number, name, and "
          "date against the source; then re-read the original request and confirm each part "
          "was actually addressed — including what the output silently skipped.",
 "pitfall": "Only checking what's present. Omissions are invisible unless you diff the "
            "output against the request — the costliest errors are often the missing ones.",
 "tip": "Exam answers that verify against the source document or original request beat "
        "answers that rely on Claude's confidence, formatting quality, or a second AI "
        "opinion alone.",
 "links": ["2.2", "2.3"],
 "chat": [
   {"who": "note", "text": "A financial analyst asked Claude to summarize quarterly results from an uploaded spreadsheet."},
   {"who": "user", "text": "Summarize the Q3 results from the attached data for our team update."},
   {"who": "claude", "text": "Q3 Summary:\n\nRevenue grew 14% quarter-over-quarter to $4.2M, led by the enterprise segment. Churn improved to 2.1%. Headcount costs rose 8%, and gross margin held at 71%. Overall, a strong quarter with all key metrics trending positively."},
   {"who": "user", "label": "Evaluation pass", "text": "Before I use this: list every figure in your summary with the exact cell/row in the spreadsheet it came from. Then tell me what from my request — 'results' — your summary did NOT cover."},
   {"who": "claude", "text": "Source check:\n• $4.2M revenue — Sheet 'P&L', row 12 ✓\n• 14% QoQ growth — computed from rows 11–12 ✓\n• 2.1% churn — Sheet 'Retention', row 8 ✓\n• 71% gross margin — ⚠ row 15 shows 68.7%; 71% was Q2. This is an error.\n\nNot covered: the spreadsheet also contains the cash-flow tab (Q3 burn increased 22%) and two customer concentration warnings in the notes column — omitted from my summary.\n\nCorrected summary: …"},
   {"who": "note", "text": "One accuracy error and two material omissions — caught in 60 seconds because the check targeted sources and coverage, not style."},
 ]},

{"id": "2.2", "d": "d2",
 "title": "Identify hallucinations, inconsistencies, and biases in responses",
 "concept": "Hallucinations are fabricated specifics — citations, statistics, quotes, "
            "features — delivered with the same fluent confidence as real facts. "
            "Inconsistencies are internal contradictions between parts of one output. Bias "
            "is systematic skew — in framing, examples, or assumptions. All three are "
            "detected by inspection, never by asking the model how confident it is.",
 "analogy": "A witness who never says 'I don't remember' — every gap in memory gets filled "
            "with a plausible invention, told in the same steady voice as the truth. You "
            "cross-examine the details, not the delivery.",
 "antipattern": "Treating specificity as credibility. 'Section 4.2.1 of the regulation' and "
                "'a 2024 Gartner study found 73%' FEEL verified precisely because they're "
                "specific — that's what makes hallucinated details dangerous.",
 "right": "Red-flag the checkable specifics (citations, numbers, quotes, section references), "
          "verify them externally, scan long outputs for internal contradictions, and ask "
          "'whose perspective is missing?' for bias.",
 "pitfall": "Asking Claude to rate its own confidence and treating a high rating as "
            "verification. Self-assessment is not a reliability signal — the official sample "
            "question tests exactly this.",
 "tip": "Any exam option that verifies against an authoritative external source beats any "
        "option involving self-reported confidence, rewording, or 'it sounded specific'.",
 "links": ["2.3", "2.1"],
 "chat": [
   {"who": "note", "text": "A paralegal asked Claude about a data-retention regulation. (This mirrors official sample question 1.)"},
   {"who": "user", "text": "What does the GDPR say about how long we can keep customer support recordings?"},
   {"who": "claude", "text": "Under GDPR Article 5(1)(e) — the storage limitation principle — personal data may be kept only as long as necessary for the stated purpose. For support recordings, supervisory authorities have commonly endorsed a 6-month retention ceiling, as reflected in the EDPB's 2021 guidance §4.3, which names call recordings specifically."},
   {"who": "user", "label": "Verification pass", "text": "Which parts of that answer are you able to state from the regulation's actual text, and which parts should I independently verify before citing them to our DPO?"},
   {"who": "claude", "text": "Verify before citing:\n• The '6-month ceiling' — I cannot point to a binding source; retention periods are purpose-based, not fixed. Treat this as unverified.\n• 'EDPB 2021 guidance §4.3 names call recordings' — I may be conflating documents; the section number could be wrong or fabricated. Check the EDPB's actual publications.\n\nSolid: Article 5(1)(e) storage limitation exists and applies; the purpose-based principle is correct.\n\nThe safe path: confirm the specific guidance and any numeric period against the official EDPB text before this reaches your DPO."},
   {"who": "note", "text": "The plausible §-references were the hallucination risk. Specific ≠ verified — check specifics against the official source."},
 ]},

{"id": "2.3", "d": "d2",
 "title": "Apply fact-checking and validation techniques",
 "concept": "Validation is a toolkit, matched to the claim: check citations against the "
            "official document, recompute numbers from raw data, cross-check independent "
            "sources for factual claims, and route domain judgments to a human expert. The "
            "effort should scale with the stakes of being wrong.",
 "analogy": "Airport security has different lanes — metal detector for everyone, extra "
            "screening for flagged items. Every output passes a quick scan; high-stakes "
            "claims get the full pat-down.",
 "antipattern": "Validating by asking the same model 'are you sure?' — it will often "
                "double-down fluently — or fact-checking a compliance summary by rewording "
                "it until it sounds more formal.",
 "right": "Match the technique to the claim type: citation → open the cited source; "
          "statistic → recompute or trace to the original dataset; legal/regulated claim → "
          "authoritative text plus expert review; general fact → two independent sources.",
 "pitfall": "Uniform effort — deep-verifying trivia while waving high-stakes claims through "
            "because 'there's no time'. Stakes decide depth, not convenience.",
 "tip": "Official sample question 1 is this lesson: a confident regulatory summary citing a "
        "specific subsection must be verified against the official regulation text before it "
        "goes to compliance. Not confidence ratings, not rewording.",
 "links": ["2.2", "2.4"],
 "chat": [
   {"who": "note", "text": "An associate prepared a market-size estimate with Claude and now validates it before the investment memo."},
   {"who": "user", "text": "Your draft says: 'The EU cold-chain logistics market was €9.8B in 2024 (Statista), growing 12% annually, and new F-Gas rules (Regulation 2024/573, Art. 12) will retire 30% of refrigerated fleets by 2027.' Give me a validation plan for each claim before this goes in the memo."},
   {"who": "claude", "text": "Claim-by-claim validation plan:\n\n1. '€9.8B (Statista)' — a checkable citation. Open the actual Statista page; confirm figure, year, and market definition match. Risk: I may have blended adjacent market reports.\n\n2. '12% annual growth' — a statistic. Trace to a named report and check the period it covers; if it's my synthesis, recompute from primary figures.\n\n3. 'Regulation 2024/573, Art. 12 retires 30% of fleets' — highest stakes. The regulation number is real, but verify Article 12's actual text on EUR-Lex; the '30% by 2027' reads like an industry-analysis projection, not regulatory text. Separate what the LAW says from what analysts predict, and have your compliance contact confirm the interpretation.\n\nStakes ranking: claim 3 (memo's core argument) > claim 1 > claim 2."},
   {"who": "user", "text": "Checked: Statista says €9.1B not €9.8B, and Art. 12 covers labeling — the fleet phase-out is in Annex IV. Update the draft with correct sourcing."},
   {"who": "claude", "text": "Updated: '…was €9.1B in 2024 (Statista, EU cold-chain logistics, retrieved Jul 2026)… the F-Gas Regulation (EU) 2024/573 — Annex IV phase-down schedule — is projected by industry analysts to force replacement of a substantial share of refrigerated fleets by 2027 (projection, not regulatory mandate).'\n\nBoth errors would have survived a confidence check — they only fell to source verification."},
 ]},

{"id": "2.4", "d": "d2",
 "title": "Determine when human review or additional verification is required",
 "concept": "Some outputs must pass through a qualified human regardless of how good they "
            "look: legal, medical, financial, and HR/personnel content; anything public or "
            "contractual; irreversible decisions; and regulated communications. The trigger "
            "is the category and its consequences, not the output's apparent quality.",
 "analogy": "A pharmacist checks every prescription — not because doctors are usually wrong, "
            "but because the cost of the rare error is unacceptable. The check is triggered "
            "by the category 'prescription', not by suspicion.",
 "antipattern": "Quality-gating by impression: 'it looked right, so I sent it.' Or the "
                "opposite failure — routing everything to review, which buries reviewers and "
                "trains them to rubber-stamp.",
 "right": "Define review triggers by category and consequence up front: external + binding + "
          "regulated + irreversible → expert review, always. Routine internal drafts → "
          "self-review. Calibrate so reviewers see the few items that matter.",
 "pitfall": "Assuming iteration substitutes for review — ten rounds of refinement with Claude "
            "is still zero qualified human eyes on a contract clause.",
 "tip": "When an exam scenario mentions compliance, contracts, medical/legal content, or an "
        "external audience, the correct option almost always includes a qualified human "
        "checkpoint before use — and the wrong options ship it because it 'looked accurate'.",
 "links": ["2.3", "6.3"],
 "chat": [
   {"who": "note", "text": "A sales ops associate drafted contract-renewal language with Claude."},
   {"who": "user", "label": "Risky shortcut", "text": "This renewal clause you drafted looks perfect. I'll paste it into the customer's contract — Legal is backed up for a week and the deal closes tomorrow."},
   {"who": "claude", "text": "Before you do — this crosses several mandatory-review triggers at once: it's contractual (binding), external (customer-facing), and it modifies liability language (consequences are irreversible once signed).\n\nMy draft is a starting point written without access to your master services agreement, the customer's negotiated terms, or your jurisdiction's requirements. A clause that 'looks perfect' can still conflict with the MSA's precedence rules or waive protections you rely on.\n\nOptions that keep the deal moving:\n• Send Legal the single clause (not the whole contract) flagged 'one-clause review, closing tomorrow'\n• Use the pre-approved fallback language from your clause library if one exists\n• Close on the current term with a documented amendment window\n\nWhat I can safely do now: produce a redline comparison against your standard template so Legal's review takes minutes instead of hours."},
   {"who": "user", "text": "Fair. Generate the redline against our standard renewal template and a 3-line summary of what changed for Legal."},
   {"who": "claude", "text": "Redline attached. Summary for Legal:\n1. Renewal term extended 12 → 24 months (customer request)\n2. Price escalator capped at 4% (was uncapped) — revenue impact\n3. ⚠ Liability cap wording changed from 'fees paid in prior 12 months' to 'fees paid' — this one needs your judgment.\n\nItem 3 is exactly why this category gets human review."},
 ]},

{"id": "2.5", "d": "d2",
 "title": "Edit, adapt, refine, and compare outputs for the intended audience",
 "concept": "One set of facts, many audiences. Adapting means changing depth, vocabulary, "
            "framing, and emphasis for who's reading — executives want decisions and "
            "impact, engineers want specifics, customers want clarity and reassurance. "
            "Generating variants and comparing them is faster than perfecting one.",
 "analogy": "A doctor explaining one diagnosis three ways: to the patient (plain language, "
            "what happens next), to a colleague (terminology, differentials), to the "
            "insurer (codes and criteria). Same truth, three renderings.",
 "antipattern": "Writing once for everyone — the all-purpose memo that's too technical for "
                "execs and too vague for practitioners — or 'dumbing down' by deleting "
                "content instead of translating it.",
 "right": "Name the audience and what they need to DO with the information, generate "
          "purpose-built variants, and compare side-by-side: 'Rewrite this incident report "
          "as (a) a 3-line exec summary focused on customer impact, (b) a customer notice — "
          "plain, honest, no internal jargon.'",
 "pitfall": "Adaptation that drifts from the facts — simplifying a caveat until it's no "
            "longer true. Every variant must stay faithful to the source; simpler words, "
            "same claims.",
 "tip": "Exam options that specify the audience and adapt framing/depth for it beat options "
        "that shorten, formalize, or 'polish' without an audience in mind.",
 "links": ["1.1", "2.6"],
 "chat": [
   {"who": "note", "text": "An IT manager has a technical incident postmortem and three audiences to inform."},
   {"who": "user", "text": "Here's the postmortem [pasted]: a misconfigured load balancer caused 43 minutes of checkout failures, ~$31K in abandoned carts, fixed by rolling back config change #4471. I need three versions: exec summary, customer status-page notice, and a note for the engineering wiki."},
   {"who": "claude", "text": "1) EXEC SUMMARY (decisions + impact):\n'Checkout was down 43 min on Tue (~$31K est. lost sales). Cause: a config change that skipped review. Fixed same day. We're adding a mandatory review gate for load-balancer changes — no budget ask; process change only.'\n\n2) CUSTOMER STATUS PAGE (clarity + reassurance, no jargon):\n'On Tuesday between 14:02–14:45 UTC, some customers couldn't complete purchases. This was caused by an internal configuration error — no customer data was affected. The issue is fully resolved, and we've added safeguards to prevent recurrence. We're sorry for the disruption.'\n\n3) ENGINEERING WIKI (specifics, reproducibility):\n'Change #4471 modified the LB health-check path without updating the target group, draining all healthy checkout pods… Rollback via `deploy revert 4471`. Action items: health-check config now requires 2-reviewer approval; alert added on >50% target drain.'"},
   {"who": "user", "text": "In the customer notice, 'no customer data was affected' — is that supported by the postmortem, or did adaptation add a claim?"},
   {"who": "claude", "text": "Good catch — the postmortem doesn't address data at all; I added reassurance that isn't sourced. Either verify that claim with the security team before publishing, or drop it:\n\n'…caused by an internal configuration error. The issue is fully resolved…'\n\nAdaptation may change framing and depth, but it must never add claims the source doesn't support."},
 ]},

{"id": "2.6", "d": "d2",
 "title": "Organize and curate information and select appropriate output formats",
 "concept": "Choosing the output format is part of the work: inline chat for quick "
            "back-and-forth, artifacts for documents/tables/code you'll refine, share, or "
            "reuse, and structured data (tables, CSV, JSON) when the output feeds another "
            "tool or needs comparison. Curation — ordering, grouping, cutting — is what "
            "turns information into something usable.",
 "analogy": "The difference between handing someone a shoebox of receipts and a categorized "
            "expense report. Same information; only one is usable. Format and organization "
            "are the deliverable, not decoration.",
 "antipattern": "Everything as one long chat reply — a 40-row comparison buried in prose "
                "paragraphs, a policy document scrolled past in chat instead of maintained "
                "as an artifact, data re-typed by hand because it wasn't structured.",
 "right": "Ask for the format the next step needs: 'as a sortable table with these 6 "
          "columns', 'as an artifact I can iterate on and share', 'as CSV I can paste into "
          "Sheets'. Group, rank, and cut to what the reader will actually use.",
 "pitfall": "Over-formatting trivial answers (a table for two facts) and under-formatting "
            "dense ones. The format serves retrieval and reuse — match it to how the output "
            "will be consumed.",
 "tip": "Exam cue: 'will be updated/shared/reused' → artifact; 'imported/analyzed "
        "elsewhere' → structured data (CSV/JSON/table); 'quick answer in conversation' → "
        "inline. Pick by downstream use, not by looks.",
 "links": ["2.5", "3.1"],
 "chat": [
   {"who": "note", "text": "A procurement analyst is comparing SaaS vendors and will import the result into a tracking sheet."},
   {"who": "user", "label": "Weak prompt", "text": "Compare the three CRM vendors from the docs I uploaded."},
   {"who": "claude", "text": "Vendor A offers strong pipeline management and integrates with your email stack, priced at $45/user/month. Vendor B, at $38/user/month, emphasizes automation but has weaker reporting. Vendor C…\n\n(four paragraphs of prose — informative, impossible to compare or import)"},
   {"who": "user", "label": "Improved prompt", "text": "Redo as a comparison table: rows = the 7 criteria from our RFP doc, columns = the 3 vendors, cells max 8 words, with a ✓/✗/partial verdict per cell. Then give me the same thing as CSV so I can paste it into our tracking sheet. Order criteria by weight from the RFP."},
   {"who": "claude", "text": "| Criterion (RFP weight) | Vendor A | Vendor B | Vendor C |\n|---|---|---|---|\n| SSO/SAML (25%) | ✓ included | ✓ +$6/user | ✗ roadmap only |\n| API limits (20%) | ✓ 100K/day | partial 10K/day | ✓ unlimited |\n| Email integration (15%) | ✓ native | ✓ native | partial via Zapier |\n…\n\nCSV:\ncriterion,weight,vendor_a,vendor_b,vendor_c\nsso_saml,25%,included,paid_addon,roadmap\napi_limits,20%,100k_day,10k_day,unlimited\n…"},
   {"who": "user", "text": "Also make the full comparison an artifact — I'll be updating it as demo calls happen and sharing it with the committee."},
   {"who": "note", "text": "Reused + shared + updated → artifact. Imported → CSV. Quick question → inline. The downstream use picks the format."},
 ]},

# ============================== DOMAIN 3 — Product and Model Selection (12%) ==============================

{"id": "3.1", "d": "d3",
 "title": "Select appropriate Claude product features (Projects, research mode, chat, artifacts)",
 "concept": "Each feature answers a different need: plain chat for one-off tasks; Projects "
            "when the same context (instructions + documents) recurs across many chats; "
            "research mode when the answer must come from current, cited web sources; "
            "artifacts when the deliverable is a document, table, page, or code you will "
            "refine, share, or reuse.",
 "analogy": "Kitchen stations: the cutting board for quick prep (chat), the labeled pantry "
            "you restock once and cook from daily (Projects), sending a runner to the "
            "market for today's prices (research mode), and the plated dish that leaves "
            "the kitchen (artifacts).",
 "antipattern": "Re-pasting the same brand guide and product sheet into every new chat — "
                "or asking plain chat for 'the latest' market figures, which its training "
                "data cannot reliably contain.",
 "right": "Recurring context → set up a Project once. Current sourced facts → research "
          "mode, then verify citations. Shareable deliverable → artifact. Quick one-off → "
          "chat. Combine them: a Project chat can still use research mode and produce artifacts.",
 "pitfall": "Thinking features are exclusive tiers. They compose — the question is what "
            "the task needs: persistent context, live sources, a durable deliverable, or "
            "none of the above.",
 "tip": "Exam cue-words: 'every week / the whole team / same documents' → Projects; "
        "'current / latest / with sources' → research mode; 'share / iterate on a "
        "document' → artifact; 'quick question' → chat.",
 "links": ["5.1", "2.6"],
 "chat": [
   {"who": "note", "text": "A marketing associate produces a weekly competitor newsletter and keeps starting from scratch."},
   {"who": "user", "label": "Weak setup", "text": "(new chat, again) You're a market analyst. Our positioning: [pastes 2 pages]. Our competitors: [pastes list]. Our tone guide: [pastes]. Now write this week's competitor update."},
   {"who": "claude", "text": "Here's this week's competitor update based on the positioning and tone you've provided…\n\n(a decent draft — but this same 10-minute setup happens every single week, and the analysis can't include anything newer than my training data)"},
   {"who": "note", "text": "Two mismatches: recurring context re-pasted weekly, and 'this week's news' requested without live sources."},
   {"who": "user", "label": "Improved setup", "text": "I've created a 'Competitor Newsletter' Project with our positioning doc, competitor list, and tone guide as Project knowledge, plus instructions for the newsletter format. In this Project chat: use research mode to find this week's announcements from our top 3 competitors, then draft the newsletter as an artifact."},
   {"who": "claude", "text": "Using your Project's positioning and tone guide.\n\nResearch (sources cited): Competitor A announced a Salesforce integration Tuesday [1]; Competitor B raised prices 8% on the mid tier [2]; Competitor C published a healthcare case study [3].\n\nDraft newsletter created as an artifact — formatted per your Project instructions, positioning each item against our differentiation. Edit or share it from the panel; next week, just open a new chat in this Project and say 'this week's edition'."},
   {"who": "note", "text": "Project = persistent context · research mode = current cited facts · artifact = the reusable deliverable."},
 ]},

{"id": "3.2", "d": "d3",
 "title": "Differentiate between Claude model types (Haiku, Sonnet, Opus)",
 "concept": "The model families trade capability against speed and cost. Haiku: fastest and "
            "most economical — high-volume, well-defined, straightforward tasks. Sonnet: the "
            "balanced default for everyday professional work. Opus: the most capable — deep "
            "multi-step reasoning, complex analysis, and the hardest problems, at higher "
            "cost and latency.",
 "analogy": "Shipping options: courier bike (Haiku — fast, cheap, small parcels), delivery "
            "van (Sonnet — the everyday workhorse), freight team with an engineer (Opus — "
            "when the cargo is genuinely complex). You don't book the freight team to "
            "deliver an envelope.",
 "antipattern": "'Always use the biggest model to be safe' — paying Opus cost and latency "
                "for thousands of routine replies — or its mirror: forcing the cheapest "
                "model through a dense legal analysis and trusting whatever comes out.",
 "right": "Classify the task first: volume + simple + speed-sensitive → Haiku; standard "
          "drafting/analysis → Sonnet; genuinely complex reasoning where quality dominates "
          "cost → Opus. Re-evaluate when the task changes shape.",
 "pitfall": "Treating model choice as a quality knob only. It's a three-way trade — a "
            "10x-volume task at slightly lower per-item quality is often the better business "
            "outcome, and the exam frames it that way.",
 "tip": "Official sample question 2 is this lesson verbatim: high-volume short replies where "
        "speed and cost matter → the faster, lower-cost model. 'Most capable everywhere' is "
        "always the distractor.",
 "links": ["3.3", "3.1"],
 "chat": [
   {"who": "note", "text": "A support ops lead is sizing models for two very different jobs."},
   {"who": "user", "text": "Two tasks: (1) auto-draft first-reply suggestions for ~2,000 routine support tickets/day — agents review before sending; (2) a quarterly root-cause analysis across 6 months of escalation data for the exec team. Which model for each?"},
   {"who": "claude", "text": "Task 1 → Haiku. The work is high-volume, well-defined (classify + template a first reply), latency-sensitive (agents wait on it), and human-reviewed (a safety net exists). Paying Opus prices here multiplies cost ~2,000×/day for quality differences your reviewers would mostly overwrite anyway.\n\nTask 2 → Opus. It's low-volume (once a quarter), genuinely complex (cross-referencing months of data, causal reasoning, exec-facing conclusions), and the cost of a wrong conclusion dwarfs the model cost. Speed is irrelevant.\n\nIn between — say, drafting the monthly ops report — Sonnet is the default: strong quality at everyday cost."},
   {"who": "user", "text": "Our CFO asked: why not just use the best model for everything, so quality is never a question?"},
   {"who": "claude", "text": "Because 'best' is per-task, not absolute. For task 1, Opus buys marginal quality your review step already provides — while adding real cost (×2,000/day) and latency agents feel on every ticket. Quality, efficiency, and cost are a three-way balance: reserve the most capable model for work that needs its reasoning, and the routine work funds itself. That balancing act — not maximal spend — is what responsible AI usage looks like to an auditor, too."},
 ]},

{"id": "3.3", "d": "d3",
 "title": "Align model selection with task requirements (cost, speed, quality)",
 "concept": "Model selection is requirements engineering: list what the task actually "
            "needs — accuracy floor, latency ceiling, volume, budget, review safety nets — "
            "then pick the cheapest/fastest model that clears the bar. Quality requirements "
            "are set by consequences, not by prestige.",
 "analogy": "Hiring for a role: you don't hire the most senior candidate for every opening — "
            "you write the job requirements first, then hire the person who meets them. "
            "Over-hiring burns budget; under-hiring burns quality.",
 "antipattern": "Choosing the model before stating requirements — by habit, by brand "
                "('always the top model'), or by budget panic ('always the cheapest') — and "
                "never revisiting the choice as volume or stakes change.",
 "right": "Write the requirement sentence first: 'X outputs/day, replies within Y seconds, "
          "error tolerance Z because [review step / audience]'. The model that satisfies it "
          "at lowest cost wins. When requirements change, re-decide.",
 "pitfall": "Ignoring the review structure around the task. A human-reviewed draft tolerates "
            "a faster model; an unreviewed customer-facing answer raises the quality floor — "
            "the workflow, not just the task, sets the requirement.",
 "tip": "Exam options that name the trade-off ('faster, lower-cost model suited to "
        "high-volume straightforward tasks') beat options that disable features, switch "
        "platforms, or maximize capability 'to be safe'.",
 "links": ["3.2", "7.3"],
 "chat": [
   {"who": "note", "text": "An operations manager is budgeting an AI-assisted invoice-processing workflow."},
   {"who": "user", "label": "Requirements first", "text": "Help me pick a model by requirements, not vibes. The task: extract 5 fields from ~800 supplier invoices/day into our AP system. A clerk spot-checks 10%. Wrong extractions cost ~20 min each to fix. Budget matters; each invoice should process in under 10 seconds."},
   {"who": "claude", "text": "Requirements translation:\n• Volume: 800/day → per-unit cost is multiplied ×800×22 workdays — cost sensitivity HIGH\n• Latency: <10s → rules out nothing, but favors faster models\n• Quality floor: 5 well-defined fields from semi-structured documents = a straightforward extraction task; 10% human spot-check exists\n• Error economics: a miss costs 20 min of clerk time — tolerable at low rates, expensive at high rates\n\nRecommendation: start with Haiku. The task is high-volume and well-defined — its profile. Run a 200-invoice pilot, measure field-level accuracy against the clerk's corrections. If accuracy on any field falls below your threshold (say 97%), step that field — or the whole flow — up to Sonnet and re-measure. Opus is not on the table: nothing here needs deep reasoning."},
   {"who": "user", "text": "Pilot ran: 98.6% field accuracy, but the 'payment terms' field only hit 91% — suppliers write it in wildly inconsistent formats."},
   {"who": "claude", "text": "Textbook split decision: keep Haiku for the four fields that clear the bar, and either (a) route just the payment-terms field to Sonnet, or (b) add two examples of the messy formats to the prompt and re-test Haiku first — cheaper if it works. Requirements set the floor per field, not per project; pay for capability only where the task actually demands it."},
 ]},

{"id": "3.4", "d": "d3",
 "title": "Understand and manage context limitations and memory considerations",
 "concept": "A conversation's context window is finite: very long chats slow down, lose "
            "track of early details, and eventually can't fit more. Manage it deliberately — "
            "start fresh chats per task, ask for a summary to carry key decisions forward, "
            "and persist durable context in Project instructions/knowledge instead of "
            "re-explaining it every session.",
 "analogy": "A whiteboard in a long meeting: it fills up. You either photograph the "
            "decisions and wipe it (summarize + restart), or pin the permanent reference "
            "material on the wall next to it (Project knowledge) so the board holds only "
            "today's work.",
 "antipattern": "One eternal mega-chat for everything — week three, Claude 'forgets' the "
                "constraint from day one, responses degrade, and the fix attempted is "
                "typing the constraint again into the same overloaded conversation.",
 "right": "One task, one chat. Before switching or when a chat gets long: 'Summarize the "
          "decisions, constraints, and open items so far' → carry that into a fresh chat. "
          "Anything needed across ALL chats → Project instructions or knowledge, not chat "
          "history.",
 "pitfall": "Confusing chat history with durable memory. A conversation is a workspace, "
            "not a filing cabinet — if it must survive the session, persist it in the "
            "Project (or your own docs), explicitly.",
 "tip": "Exam cue: 'long conversation, quality degrading, early instructions ignored' → "
        "summarize and restart (or move durable context to a Project) — not 'repeat the "
        "instruction louder' and not 'the model is broken'.",
 "links": ["3.1", "5.1"],
 "chat": [
   {"who": "note", "text": "A program manager has run one continuous chat for three weeks of vendor negotiation prep."},
   {"who": "user", "label": "Degrading mega-chat", "text": "Draft the counter-offer email like we discussed. Remember the walk-away price we set at the start."},
   {"who": "claude", "text": "Here's the counter-offer draft…\n\n(the draft cites a $120K ceiling — but the walk-away agreed on day one was $95K; that constraint is buried under three weeks of accumulated conversation and is no longer reliably in view)"},
   {"who": "user", "text": "That's wrong — we said $95K weeks ago. Why did you lose it?"},
   {"who": "claude", "text": "You're right, and the honest answer is a context limitation: this conversation now contains weeks of material, and early details can fall out of my effective working view. Rather than patching this chat, let's fix the structure:\n\n1. I'll produce a NEGOTIATION BRIEF summarizing everything durable — walk-away $95K, agreed terms, open items, decision log.\n2. Save it to your 'Vendor Negotiation' Project as knowledge (or pin it in instructions).\n3. Start each work session as a fresh chat in that Project — it loads the brief automatically, and the chat stays short and sharp.\n\nWant the brief now?"},
   {"who": "user", "label": "Fixed structure", "text": "Yes — generate the brief. I'll add it to the Project and we'll do the counter-offer in a fresh chat."},
   {"who": "claude", "text": "NEGOTIATION BRIEF (v1, carries all durable context):\n• Walk-away: $95K max annual — HARD LIMIT set 2026-06-24\n• Must-haves: 24-mo term, quarterly exit clause, EU data residency\n• Conceded: onboarding fee (waived by them 7/02)\n• Open: SLA credits %, renewal cap\n• Next: counter-offer email\n\nFresh chat + this brief = every future draft starts from the facts, not from fading memory."},
 ]},

# ============================== DOMAIN 4 — Workflow Integration and Solution Design (16%) ==============================

{"id": "4.1", "d": "d4",
 "title": "Apply Claude to analyze requirements and use cases",
 "concept": "Before building anything, use Claude to interrogate the problem: surface "
            "unstated requirements, identify stakeholders and constraints, separate "
            "must-haves from nice-to-haves, and pressure-test whether the stated ask is the "
            "real need. Claude is a structured thinking partner, not just a producer.",
 "analogy": "A good consultant's first meeting: they don't quote a price for 'a new "
            "website' — they ask what the website is supposed to achieve, for whom, by "
            "when, within what constraints. The questions ARE the analysis.",
 "antipattern": "Jumping straight to production — 'build me the rollout plan' — on an "
                "unexamined request, then discovering mid-rollout that the requirement "
                "everyone assumed was never actually agreed.",
 "right": "Make Claude interrogate before it produces: 'Before drafting anything, list the "
          "questions this request leaves unanswered, the stakeholders affected, and the "
          "constraints implied. Then propose acceptance criteria we can validate with the "
          "requester.'",
 "pitfall": "Accepting Claude's inferred requirements as decisions. Its analysis surfaces "
            "candidate requirements — a human confirms them with the actual stakeholders "
            "before they become commitments.",
 "tip": "Exam scenarios about vague requests reward 'clarify requirements / define success "
        "criteria first' over 'produce the deliverable immediately' — analysis before "
        "artifact.",
 "links": ["4.3", "1.2"],
 "chat": [
   {"who": "note", "text": "A department head forwards a one-line request: 'We need an AI chatbot for HR.'"},
   {"who": "user", "label": "Unexamined ask", "text": "Leadership wants an AI chatbot for HR. Draft the project plan."},
   {"who": "claude", "text": "I can draft that — but a plan built on a one-line requirement will encode guesses as commitments. Let me analyze the request first:\n\nUnanswered questions:\n• Who is it for — all employees, HR staff, or candidates?\n• What top tasks? (benefits questions ≠ leave requests ≠ policy lookup — very different builds)\n• What may it answer autonomously vs. must it route to a human? (payroll and personal data raise governance flags)\n• Success metric — deflection rate? response time? HR hours saved?\n\nStakeholders: HR ops, IT/security, works council/employee reps (monitoring concerns), legal (PII).\n\nImplied constraints: must respect data privacy for personnel records; probably needs your existing HR knowledge base as its source.\n\nProposed acceptance criteria to validate with leadership:\n1. Answers top-20 benefits/policy questions from the official handbook, with links\n2. Never discusses individual personnel data; routes those to HR staff\n3. Cuts tier-1 HR email volume 30% in 90 days\n\nShall I turn these into a one-page requirements summary for the leadership meeting?"},
   {"who": "user", "text": "Yes — and add a half-page of use cases ranked by value vs. effort so they can choose scope."},
   {"who": "claude", "text": "Requirements summary + ranked use cases drafted:\n\nHigh value / low effort: benefits FAQ, policy lookup with handbook citations, onboarding checklist guidance\nHigh value / higher effort: leave-request status (needs HRIS integration — escalate to IT)\nOut of scope v1: anything touching individual records (governance review first)\n\nThe leadership decision is now about scope and criteria — not about a guessed plan."},
 ]},

{"id": "4.2", "d": "d4",
 "title": "Leverage Claude for research, planning, and process optimization",
 "concept": "Claude accelerates the thinking work around execution: synthesizing research "
            "into decision-ready comparisons, drafting plans with dependencies and risks, "
            "and analyzing an existing process to find bottlenecks, redundancies, and "
            "automation candidates.",
 "analogy": "A chief of staff: gathers the background, drafts the plan of attack, spots "
            "where the operation wastes motion — so the decision-maker spends their time "
            "deciding, not compiling.",
 "antipattern": "Using Claude only at the final step (write the doc) while doing the "
                "research synthesis and planning manually — or accepting its process "
                "recommendations without validating them against how work actually flows.",
 "right": "Bring Claude the raw material and the decision to be made: 'Here are our 6 "
          "process steps with owners and timings [paste]. Identify bottlenecks, handoff "
          "risks, and steps that could be parallelized or automated; rank by expected time "
          "saved.'",
 "pitfall": "Research without recency awareness — for anything time-sensitive, pair "
            "Claude's synthesis with research mode or your own current sources, and keep "
            "citations attached so claims stay checkable.",
 "tip": "The exam rewards using Claude to structure and synthesize (options, trade-offs, "
        "dependencies, bottleneck analysis) with humans validating — over both manual-only "
        "work and blind delegation.",
 "links": ["1.2", "7.3"],
 "chat": [
   {"who": "note", "text": "An ops lead suspects the employee-onboarding process is bloated."},
   {"who": "user", "text": "Here's our onboarding process, step by step with owners and average durations [pasted: 14 steps, 11 business days total]. Where is it slow and what would you change?"},
   {"who": "claude", "text": "Analysis of your 14 steps:\n\nBOTTLENECK: Steps 4–6 (IT access requests) account for 5 of the 11 days — three sequential tickets that could be one parallel bundle triggered at contract signature instead of day 1.\n\nREDUNDANCY: Steps 8 and 12 both collect emergency-contact data (HR form, then facilities form) — merge.\n\nHANDOFF RISK: Step 9 (manager schedules intro meetings) has no owner-of-record when the manager is on leave — 3 of your last 10 onboardings stalled here per your durations.\n\nAUTOMATION CANDIDATES (ranked by days saved):\n1. Pre-trigger IT bundle at signature: −4 days\n2. Auto-schedule intro meetings from a template calendar: −1 day\n3. Merge duplicate forms: −0.5 day admin time\n\nProjected: 11 days → ~5.5. Caveat: I'm reasoning from your documented process — validate with the people who run steps 4–6 whether the sequential ordering has a real dependency I can't see (e.g., security policy)."},
   {"who": "user", "text": "IT says the sequence exists because badge requests need an employee ID that's only created in step 3. Adjust."},
   {"who": "claude", "text": "Adjusted: trigger step 3 (ID creation) at signature — it has no upstream dependency — then the IT bundle fires the same day. Projection holds at ~6 days. This is exactly why the human check matters: the plan is now grounded in the real constraint, not my inference of it."},
 ]},

{"id": "4.3", "d": "d4",
 "title": "Use Claude to support solution design, development, and iteration",
 "concept": "For a business problem, Claude supports the full design arc: generate solution "
            "options with trade-offs, help select against criteria, draft the chosen design "
            "(process, template, document, rollout), and iterate it against feedback and "
            "pilot results — with the associate steering each turn.",
 "analogy": "An architect's studio process: sketches first (options), then the client picks "
            "a direction (selection), then blueprints (design), then revisions after the "
            "walkthrough (iteration). Nobody builds from the first sketch.",
 "antipattern": "One-shot solutioning: taking Claude's first proposed design straight to "
                "rollout — no alternatives compared, no pilot feedback loop — then patching "
                "in production what a pilot would have caught.",
 "right": "Run the arc explicitly: 'Give me 3 approaches with trade-offs' → pick one "
          "against named criteria → 'draft the full design' → pilot → 'here's what broke "
          "and the feedback [paste]; revise.' Each artifact improves through evidence.",
 "pitfall": "Letting iteration drift from the success criteria set at the start — every "
            "revision should be checked against the same yardstick, or you optimize toward "
            "whoever complained loudest.",
 "tip": "Exam answers that generate options → select by criteria → pilot → iterate beat "
        "both 'implement Claude's first suggestion org-wide' and 'don't use AI for design "
        "work'.",
 "links": ["4.1", "1.3"],
 "chat": [
   {"who": "note", "text": "A customer success manager must fix a broken QBR (quarterly business review) prep process."},
   {"who": "user", "text": "Our CSMs spend 6 hours prepping each QBR deck manually. Design me a better process — but options first, not one answer. Criteria: prep time under 2 hours, data accuracy, works for our 40 CSMs without new software."},
   {"who": "claude", "text": "Three approaches with trade-offs against your criteria:\n\nA) TEMPLATE + CLAUDE DRAFT: Standard deck template; CSM exports account data, Claude drafts commentary per slide. Prep ~1.5h. Accuracy depends on export discipline. No new software. Risk: garbage-in commentary.\n\nB) CLAUDE PROJECT PER SEGMENT: Projects preloaded with playbooks + template; CSMs drop in the account export, get a full draft. Prep ~1h. Higher consistency. Setup effort up front; knowledge must be maintained.\n\nC) FULL AUTOMATION VIA API: Auto-generated decks from the CRM. Prep ~15min but violates your 'no new software' constraint and needs engineering — out of scope for your team (escalation territory).\n\nAgainst your criteria, B wins on time and consistency; A is the fastest to pilot. Recommend: pilot A with 3 CSMs for two weeks; if commentary quality holds, invest in B's Project setup."},
   {"who": "user", "label": "After pilot", "text": "Pilot feedback: prep dropped to 100 min, but two CSMs said the drafts misread declining-usage accounts as healthy because the export omits the usage-trend tab."},
   {"who": "claude", "text": "Root cause is input completeness, not the drafting. Revision to the design:\n1. Export checklist now names the usage-trend tab as REQUIRED — the draft prompt refuses to assess health without it\n2. Added a 'health assessment' rubric to the template: usage trend, support tickets, champion status — so commentary is criteria-driven, not inferred\n3. Re-pilot with the same 3 CSMs against the same yardstick: <2h prep AND zero misread health calls\n\nSame criteria, better evidence, third iteration. That's the arc working."},
 ]},

{"id": "4.4", "d": "d4",
 "title": "Integrate Claude into existing workflows to augment or redesign them",
 "concept": "Integration means deciding where AI sits inside a workflow that already exists: "
            "augment specific steps (draft, summarize, classify) while humans keep "
            "judgment steps, or redesign the flow around what AI makes newly possible. Map "
            "the workflow first; insert AI where it removes real friction; keep humans at "
            "decision and quality gates.",
 "analogy": "Adding a power tool to a workshop that already builds furniture. You don't "
            "bolt it randomly to a bench — you find the step that's slow (rough cutting), "
            "fit the tool there, and keep the craftsman on the finish work.",
 "antipattern": "Bolting AI onto a process nobody mapped ('use Claude for… everything?'), "
                "automating the judgment steps while leaving the drudgery manual, or "
                "leaving no human gate before outputs reach customers.",
 "right": "Map steps → classify each as drudgery (summarize, reformat, first-draft, "
          "classify) vs judgment (approve, decide, negotiate) → augment drudgery with "
          "Claude, keep judgment human, define the handoff points explicitly, measure "
          "before/after.",
 "pitfall": "Skipping change management. A redesigned workflow fails if the team doesn't "
            "know when to trust the AI step, when to override it, and who owns its errors — "
            "write that down as part of the design.",
 "tip": "Exam answers that keep humans at judgment/quality gates and insert AI at "
        "well-defined drudgery steps beat 'automate end-to-end' and 'ban AI from the "
        "workflow' alike.",
 "links": ["4.2", "2.4"],
 "chat": [
   {"who": "note", "text": "A recruiting lead wants AI in the hiring pipeline 'somewhere useful'."},
   {"who": "user", "text": "We want Claude in our recruiting workflow. Current flow: (1) source candidates, (2) screen 200+ CVs/role, (3) phone screens, (4) interview loops, (5) offer decision. Where does it belong — and where does it NOT?"},
   {"who": "claude", "text": "Step-by-step classification:\n\n(2) CV screening — AUGMENT, carefully: Claude can extract and structure each CV against the published role requirements (skills, experience, location) into a comparable summary sheet. But per your jurisdiction's rules and good practice, it should structure information for humans — not auto-reject candidates. A recruiter reviews every 'no'. This is also a bias-risk zone: the criteria must be the posted requirements, never inferred proxies.\n\n(3) Phone screens — AUGMENT the paperwork: draft question guides from the role profile beforehand; summarize recruiter notes into the ATS afterwards. The conversation itself stays human.\n\n(4) Interview loops — AUGMENT logistics: brief packets for interviewers, collate feedback into a structured comparison. The evaluation is human judgment.\n\n(5) Offer decision — HUMAN ONLY. High-stakes, legally sensitive, and irreversible in candidate-experience terms. Claude may compile the data package that informs it; it must not recommend who to hire.\n\nHandoffs to document: recruiter reviews all AI rejections (step 2); hiring manager owns the decision record (step 5). Measure: time-per-screen and candidate-drop-off before vs after."},
   {"who": "user", "text": "HR asked why Claude shouldn't just rank the candidates 1–200 — wouldn't that be faster?"},
   {"who": "claude", "text": "Faster, and exactly the wrong step to automate. A ranking is a hiring judgment: it compounds any bias in the inputs, is hard to explain to a rejected candidate or an auditor, and in several jurisdictions triggers automated-decision rules. Structuring facts FOR human comparison is augmentation; producing the ordering IS the decision. Keep the decision human — that boundary is where responsible integration lives."},
 ]},

{"id": "4.5", "d": "d4",
 "title": "Communicate Claude's value and limitations to stakeholders",
 "concept": "Associates translate between the technology and the business: articulate value "
            "in the stakeholder's terms (hours saved, cycle time, quality lift — with "
            "measured numbers), and state limitations plainly (hallucination risk, "
            "training-data recency, context limits, judgment stays human). Credibility "
            "comes from naming both.",
 "analogy": "A good realtor's walkthrough: here's what the house does well, here's the "
            "foundation crack, here's what maintenance costs. Buyers trust the person who "
            "showed them the crack.",
 "antipattern": "Hype ('it eliminates the work') that shatters on the first hallucination — "
                "or reflexive doom ('it makes things up, avoid it') that forfeits real "
                "value. Both are communication failures, not technology facts.",
 "right": "Pair every value claim with its evidence and every limitation with its "
          "mitigation: 'Drafting time fell 60% in the pilot (n=45 docs). It can fabricate "
          "specifics, so citations are verified before use — that check is built into the "
          "workflow.'",
 "pitfall": "One deck for every audience. Executives need outcomes and risk posture; the "
            "working team needs when-to-trust/when-to-override; legal needs data flows. "
            "Same facts, tailored framing (see lesson 2.5).",
 "tip": "Exam answers that present measured value AND named limitations with mitigations "
        "beat pure advocacy, pure caution, and jargon-heavy technical explanations.",
 "links": ["2.5", "6.1"],
 "chat": [
   {"who": "note", "text": "An associate must brief the executive committee after a successful pilot — including its one embarrassing failure."},
   {"who": "user", "text": "Help me structure the exec briefing on our contract-review pilot. Results: review prep time down from 4.2h to 1.5h across 30 contracts. But in week 2, a draft summary invented a termination clause that wasn't in the contract — caught by the reviewing lawyer. Some execs will want to expand immediately; one is skeptical of AI entirely."},
   {"who": "claude", "text": "Structure that serves both camps — value with evidence, limitation with mitigation:\n\n1. OUTCOME (30 seconds): 'Contract review prep dropped 64% — 2.7 hours saved per contract, ~81 hours over the pilot. Lawyer review time on substance stayed unchanged: the savings came from summarization and clause-location, not from replacing judgment.'\n\n2. THE FAILURE, TOLD BY US (this is the credibility move): 'In week 2 the tool fabricated a clause that didn't exist. Our reviewing lawyer caught it — which is the design working: every AI summary is checked against the source before it informs any decision. We treat the tool as a fast first-pass reader, never as the reader of record.'\n\n3. LIMITS AS OPERATING RULES: fabrication risk → verification step; no current-events knowledge → research mode or provided documents only; long-contract context limits → section-by-section processing.\n\n4. EXPANSION ASK: extend to NDA triage next (similar task shape, lower stakes), NOT to negotiation strategy (judgment work — stays human).\n\nFor your skeptic: lead with the failure story — it shows the safeguards are real, not theoretical."},
   {"who": "user", "text": "Give me the two-sentence version for the CEO who'll read only the summary line."},
   {"who": "claude", "text": "'The pilot cut contract-review prep 64% (81 hours saved / 30 contracts) while keeping every legal judgment with our lawyers. One fabricated clause in week 2 was caught by the built-in verification step — the safeguard we'd scale with it.'"},
 ]},

# ============================== DOMAIN 5 — Configuration and Knowledge Management (12%) ==============================

{"id": "5.1", "d": "d5",
 "title": "Configure Claude Projects with instructions and knowledge sources",
 "concept": "A Project packages durable context — custom instructions (role, tone, rules, "
            "output formats) plus knowledge sources (documents Claude consults in every "
            "chat) — so each new conversation starts already briefed. Instructions define "
            "HOW to work; knowledge defines WHAT to know.",
 "analogy": "A new hire's welcome binder plus their job description. The job description "
            "(instructions) says how to behave and what good output looks like; the binder "
            "(knowledge) holds the reference material. Together they replace re-explaining "
            "the job every morning.",
 "antipattern": "Projects as mere chat folders — no instructions, no knowledge — while "
                "still pasting the style guide into every chat; or dumping 40 documents in "
                "as knowledge 'just in case', drowning the relevant in the redundant.",
 "right": "Instructions: role, audience, tone, format rules, and hard constraints, written "
          "like a brief to a contractor. Knowledge: the curated few documents chats "
          "actually need — style guide, product facts, templates — kept current.",
 "pitfall": "Putting volatile facts in instructions (they belong in swappable knowledge "
            "docs) or durable rules in individual chats (they belong in instructions). "
            "Stable → instructions; changing → knowledge; one-off → the chat.",
 "tip": "Exam cue: 'the team repeats the same context in every conversation' → configure a "
        "Project with instructions + knowledge. Distractors suggest longer prompts, one "
        "shared mega-chat, or retyping context.",
 "links": ["5.3", "3.1"],
 "chat": [
   {"who": "note", "text": "A content team lead sets up a Project for the company blog after months of re-pasting context."},
   {"who": "user", "label": "Before", "text": "(every new chat) You write for our B2B logistics blog. Tone: expert but plain-spoken, no buzzwords. Audience: warehouse ops managers. Always end with one actionable takeaway. Our products are… [pastes 2 pages] Now, draft a post about dock scheduling."},
   {"who": "claude", "text": "Here's a draft blog post on dock scheduling…\n\n(fine — but this setup ritual repeats in every chat, drifts as teammates paste older versions, and new writers don't know it exists)"},
   {"who": "note", "text": "The fix — one Project, configured once, shared with the team:"},
   {"who": "user", "label": "Project setup", "text": "Creating a 'Blog Content' Project. Instructions: 'You write for our B2B logistics blog. Audience: warehouse ops managers. Tone: expert, plain-spoken, no buzzwords. Posts are 800–1200 words, end with one actionable takeaway, and cite only facts from Project knowledge.' Knowledge: brand voice guide (PDF), product fact sheet (current version), two exemplar posts, SEO checklist. First task in this Project: draft a post about dock scheduling."},
   {"who": "claude", "text": "Draft: 'The Hidden Cost of First-Come, First-Served Docks'\n\n(Opens with an ops-manager pain point, plain-spoken per instructions; product mentions match the fact sheet exactly; structure mirrors the exemplar posts; ends with an actionable takeaway; 1,050 words)\n\nEvery future chat in this Project starts from this same footing — teammates included. When the product sheet changes, swap the knowledge file once and every subsequent chat uses the new facts."},
 ]},

{"id": "5.2", "d": "d5",
 "title": "Manage uploaded knowledge and connectors (e.g., Google Drive, Gmail)",
 "concept": "Claude's knowledge about YOUR work arrives two ways: uploads (point-in-time "
            "snapshots — must be re-uploaded when the source changes) and connectors like "
            "Google Drive or Gmail (live access to current content, governed by "
            "permissions). Managing them means choosing the right mechanism, curating what's "
            "connected, and respecting data-sensitivity rules for everything shared.",
 "analogy": "Photocopies versus a keycard to the records room. The photocopy (upload) was "
            "true the day you made it; the keycard (connector) always opens the current "
            "file — and comes with rules about which rooms you're allowed into.",
 "antipattern": "Uploading a pricing sheet once and trusting it for a year — decisions made "
                "on stale snapshots — or connecting an entire Drive 'for convenience', "
                "sweeping confidential folders into scope no one intended.",
 "right": "Stable reference docs → upload, with an owner and a review date. Frequently "
          "changing sources → connector, scoped to the specific folders needed. Before "
          "connecting anything: what's IN there, and is it cleared under your data policy?",
 "pitfall": "Forgetting uploads are frozen. If Claude cites a figure from Project "
            "knowledge, ask when that file was last replaced — 'it's in the Project' is "
            "not the same as 'it's current'.",
 "tip": "Exam cue: 'the document changes weekly' → connector (or a re-upload routine); "
        "'Claude used outdated numbers' → the snapshot went stale; anything with personal "
        "or regulated data in a connector → policy and minimization first.",
 "links": ["5.1", "6.2"],
 "chat": [
   {"who": "note", "text": "A sales ops associate discovers quotes are being drafted from a stale price list."},
   {"who": "user", "text": "A rep just sent a quote with June prices — we raised them August 1. The Project has our price list as knowledge. How is this happening?"},
   {"who": "claude", "text": "Because the price list in Project knowledge is an UPLOAD — a snapshot from the day it was added, June 3 per its content. Uploads don't update themselves; I've been answering from a file that was true eleven weeks ago.\n\nTwo fixes:\n\nA) Re-upload routine: replace the file on a schedule, with a named owner. Works, but depends on a human remembering — the failure you just experienced.\n\nB) Connector: link the Google Drive folder where sales ops maintains the live price sheet. Chats then read the CURRENT file each time. Scope it to that one pricing folder — not the whole Drive — so nothing confidential rides along.\n\nGiven prices change monthly and quotes are money, B is the right mechanism. One governance check first: confirm the pricing folder contains no customer-specific negotiated rates that reps outside those accounts shouldn't see — connector scope is an access decision, not just a convenience."},
   {"who": "user", "text": "Connected the pricing folder only. What should we do with the stale upload?"},
   {"who": "claude", "text": "Delete it from Project knowledge now — if both exist, I may draw from either, and the stale copy can silently win. Then add one line to the Project instructions: 'Pricing comes ONLY from the connected Drive pricing folder; always state the sheet's effective date in any quote.' That last clause makes staleness visible to the rep instead of invisible in the quote."},
 ]},

{"id": "5.3", "d": "d5",
 "title": "Create effective system-level instructions",
 "concept": "System-level instructions (Project instructions and their org-level "
            "equivalents) are standing orders that apply to every conversation: role, "
            "audience, tone, format rules, boundaries, and escalation behavior. Good ones "
            "are specific, testable, and prioritized — they read like a brief, not a wish.",
 "analogy": "A restaurant's standing kitchen rules posted on the wall — 'allergens always "
            "flagged, no substitutions without the chef, plating per the photo book'. They "
            "govern every order without being repeated to every cook every shift.",
 "antipattern": "Vibes-based instructions ('be professional and helpful, keep things "
                "concise-ish') that constrain nothing, contradict each other, or bury the "
                "one hard rule ('never quote prices') in paragraph six where it competes "
                "with fluff.",
 "right": "Write rules a stranger could apply and check: 'Always/Never' for hard "
          "constraints, concrete formats ('answers ≤ 150 words unless asked'), explicit "
          "escalation ('if asked about legal terms, direct to legal@ — do not draft'), "
          "hard rules first.",
 "pitfall": "Instruction sprawl. Every incident adds a rule until they conflict; behavior "
            "gets erratic. Prune on review — few, sharp rules beat many soft ones.",
 "tip": "On the exam, the best instruction option is specific and testable ('cite the "
        "policy doc section for every answer') — not the longest, and never 'tell it to be "
        "accurate and professional'.",
 "links": ["5.1", "1.1"],
 "chat": [
   {"who": "note", "text": "A support team's Project answers agents' policy questions — the instructions need a rewrite."},
   {"who": "user", "label": "Weak instructions", "text": "Current Project instructions: 'You are a helpful assistant for our support team. Be professional, accurate and concise. Try to be consistent with our policies.' Agents complain answers vary wildly and once included a made-up refund exception. Rewrite these properly."},
   {"who": "claude", "text": "The current instructions fail because none of them are checkable — 'accurate' and 'consistent' aren't rules, they're hopes. Rewrite, hard rules first:\n\n---\nROLE: You answer internal policy questions for support agents. You are not customer-facing.\n\nHARD RULES:\n1. Answer ONLY from the policy documents in Project knowledge. If the answer isn't there, say 'Not covered in policy docs' and name the closest section — never infer or invent policy.\n2. Cite the document and section for every answer (e.g., 'Refunds Policy §3.2').\n3. Refund exceptions, legal threats, and anything involving a named customer's data → 'Escalate to your team lead' — do not advise.\n\nFORMAT: ≤120 words. Rule first, citation second, edge cases third.\nTONE: Direct, neutral. No apologies, no filler.\n---\n\nEach rule is testable: an answer either carries a citation or it doesn't; a refund-exception question either got escalated or it didn't. That made-up exception becomes impossible to deliver silently — rule 1 forces 'not covered' instead."},
   {"who": "user", "text": "Two months later: agents keep asking about the new EU return window, which isn't in the docs, and they say the 'no apologies' tone reads as rude in answers that deny a request. Update."},
   {"who": "claude", "text": "Two surgical changes, no sprawl:\n1. Root cause of the EU questions is a KNOWLEDGE gap, not an instruction gap — upload the updated returns policy; the instructions already handle it once the doc exists.\n2. Tone rule amended: 'Direct and neutral; when denying or restricting, add one plain-language sentence explaining why.' Still testable — denial answers either carry the why-sentence or they don't.\n\nAnd prune check: no rules conflict, still 3 hard rules. Instructions stay few and sharp."},
 ]},

{"id": "5.4", "d": "d5",
 "title": "Inform, maintain, and update Claude configurations, knowledge sources, and instructions",
 "concept": "Configuration is a living system: knowledge goes stale, instructions drift "
            "from reality, and quiet failures accumulate. Maintenance means ownership "
            "(someone is responsible), triggers (policy changed → update the Project same "
            "week), review cadence, versioning of key docs, and telling users what changed.",
 "analogy": "First-aid kits in an office: someone owns restocking, checks expiry dates "
            "quarterly, and posts a note when the epinephrine moves. A kit nobody "
            "maintains is worse than none — it promises help it can't deliver.",
 "antipattern": "Set-and-forget: the Project that was excellent in March quietly answering "
                "from March's prices, March's policy, March's org chart in September — "
                "wrong with total confidence, and nobody assigned to notice.",
 "right": "Name an owner per Project. Tie updates to events ('policy revision published → "
          "replace knowledge doc within a week') plus a quarterly sweep: stale docs out, "
          "instructions tested against current reality, changelog note to the team.",
 "pitfall": "Updating documents but not instructions (or vice versa). A new returns policy "
            "PLUS an instruction still citing the old section numbers = confidently mixed "
            "signals. Update both, together.",
 "tip": "Exam scenarios where 'the Project gives outdated answers' are maintenance "
        "questions: the fix is update/replace the knowledge and review instructions — not "
        "'the model degraded' and not 'add a longer prompt'.",
 "links": ["5.2", "7.1"],
 "chat": [
   {"who": "note", "text": "A quarterly review of the customer-support Project, prompted by a bad answer."},
   {"who": "user", "text": "An agent got told our warranty is 12 months — it's been 24 since the July policy change. Audit this Project's setup with me: what's stale and how do we keep this from recurring?"},
   {"who": "claude", "text": "Audit of Project knowledge and instructions:\n\nSTALE:\n• 'Warranty & Returns Policy v3.pdf' — superseded by v4 in July (the 12-month answer came from here)\n• 'Escalation contacts.xlsx' — lists two employees who left in Q2\n• Instructions cite 'Policy §5 for warranty' — v4 moved warranty to §7\n\nCURRENT: product fact sheet (connected via Drive — updates itself), tone rules, format rules.\n\nRecurrence prevention — a maintenance contract for this Project:\n1. OWNER: name one person (you?) accountable for Project accuracy\n2. EVENT TRIGGERS: policy publication → knowledge swap within 5 business days; org changes → contacts file same week\n3. QUARTERLY SWEEP: every doc gets checked or replaced; instructions tested with 5 known-answer questions ('what's the warranty?' should say 24 months, §7)\n4. VERSION VISIBLY: filenames carry version + effective date ('Warranty Policy v4 — eff. 2026-07-01') so staleness is inspectable\n5. CHANGELOG: one-line note to the team channel on every update, so agents know the Project moved with the policy"},
   {"who": "user", "text": "Do the swap and the instruction fix now; I'll take ownership and the quarterly sweep."},
   {"who": "claude", "text": "Done conceptually — v4 replaces v3 in knowledge, instructions now cite §7, contacts file flagged for HR's current list. First test question against the updated setup: 'What's our warranty period?' → '24 months (Warranty Policy v4, §7, effective July 2026).' The citation-with-version habit means the NEXT staleness will announce itself instead of hiding."},
 ]},

# ============================== DOMAIN 6 — Governance, Risk, and Responsible Use (15%) ==============================

{"id": "6.1", "d": "d6",
 "title": "Identify appropriate and inappropriate use cases",
 "concept": "Fit for AI is judged on stakes, reversibility, verifiability, and data "
            "sensitivity. Strong fits: drafting, summarizing, analysis support, ideation — "
            "human-reviewed, low-blast-radius work. Poor fits (without controls): final "
            "decisions about people, unreviewed external/legal/medical output, and anything "
            "your policy or regulation excludes.",
 "analogy": "An intern policy. Interns draft memos, do research, and prepare comparisons — "
            "they don't sign contracts, decide promotions, or speak to the press. Not "
            "because they lack talent; because accountability and stakes sit elsewhere.",
 "antipattern": "Judging fit by capability alone: 'it CAN write performance reviews / "
                "diagnose the symptom / decide the claim, so let it.' Capability is "
                "necessary, never sufficient — consequences and accountability decide.",
 "right": "Screen each use case: What happens if it's wrong? Who reviews before impact? "
          "Is the data allowed here? Is a human accountable for the outcome? Green-light "
          "drafting/summarizing/analyzing under review; gate or refuse autonomous "
          "high-stakes decisions.",
 "pitfall": "The creep from assist to decide. 'Claude drafts the rejection letters' quietly "
            "becomes 'Claude decides the rejections'. Re-screen whenever the AI's role in "
            "a workflow expands.",
 "tip": "Exam options that use AI for drafts/analysis WITH human judgment retained beat "
        "both 'fully automate the decision' and 'never use AI'. Look for who holds "
        "accountability in each option.",
 "links": ["6.3", "2.4"],
 "chat": [
   {"who": "note", "text": "A team lead brainstorms AI use cases for the quarter — some fit, some don't."},
   {"who": "user", "text": "Screen these four use-case ideas: (1) summarize weekly customer feedback into themes, (2) draft performance-review paragraphs for my directs based on my bullet notes, (3) auto-respond to inbound insurance claims under $500, (4) prep first drafts of our RFP responses."},
   {"who": "claude", "text": "Screening on stakes, review, data, and accountability:\n\n(1) Feedback summarization — STRONG FIT. Low stakes, easily spot-checked against raw feedback, no individual decisions. Just anonymize any customer identifiers per policy.\n\n(2) Performance-review drafting — CONDITIONAL. Drafting FROM YOUR assessments (your bullets, your judgments) with you editing and owning every word: acceptable in many orgs. But check policy first — some prohibit AI in personnel evaluation entirely; and personnel data is sensitive. The judgment must remain visibly yours; if the AI starts characterizing performance beyond your notes, that's the creep line.\n\n(3) Auto-responding to claims — POOR FIT as stated. That's an autonomous, binding decision affecting people's money — high stakes, no review before impact, likely regulated (automated-decision rules). Refactor: Claude TRIAGES and drafts, a licensed adjuster approves. The decision stays human.\n\n(4) RFP first drafts — STRONG FIT. Substantial drudgery reduction; inherently reviewed (nobody submits an RFP unread); facts checked against your knowledge base before submission.\n\nPattern: 1 and 4 assist judgment; 3 as stated replaces it. That's the line."},
   {"who": "user", "text": "For (3), sales says competitors auto-settle small claims instantly and we're losing customers to slow payouts."},
   {"who": "claude", "text": "Then solve the speed problem without ceding the decision: Claude pre-processes each claim in seconds — completeness check, policy-coverage lookup, fraud-signal flags, and a recommended disposition with reasons — queued for an adjuster who approves with one click. Payout in minutes, but a human accountably decides. If the business later wants true auto-settlement, that's a formal governance decision with legal review — not a workflow tweak an associate ships."},
 ]},

{"id": "6.2", "d": "d6",
 "title": "Apply data sensitivity, regulatory, and privacy considerations",
 "concept": "Before data goes into any AI tool, classify it: public, internal, "
            "confidential, regulated (PII, PHI, PCI…). Policy determines what each class "
            "permits. The working defaults: minimize (share only what the task needs), "
            "anonymize or redact identifiers when the analysis doesn't need them, and when "
            "policy restricts the data — transform the task, don't sneak the data.",
 "analogy": "Mailing documents: a flyer goes in any envelope; medical records require "
            "sealed, tracked, authorized delivery. The content class — not convenience — "
            "dictates the handling.",
 "antipattern": "Uploading the raw customer spreadsheet 'because the analysis is internal', "
                "or telling the tool 'don't retain this' as if an instruction to the model "
                "satisfied a policy control on data handling.",
 "right": "Check the classification, then minimize: strip names, account numbers, and "
          "contact details when trends are the goal — the analysis usually survives "
          "anonymization intact. If it genuinely needs identifiers, that's an approval "
          "conversation, not a workaround.",
 "pitfall": "Believing anonymization is just deleting the name column. Combinations "
            "(zip + birthdate + role) can re-identify; when stakes are high, involve "
            "whoever owns privacy review.",
 "tip": "Official sample question 3 is this lesson: remove/anonymize regulated identifiers "
        "before uploading, consistent with policy. 'Upload as-is (it's internal)', "
        "'instruct Claude not to retain it', and 'abandon the task' are the three "
        "distractor shapes.",
 "links": ["6.3", "5.2"],
 "chat": [
   {"who": "note", "text": "A project manager wants churn trends from a spreadsheet full of regulated personal data. (This mirrors official sample question 3.)"},
   {"who": "user", "label": "Risky request", "text": "I'm uploading our cancellations spreadsheet — customer names, emails, account numbers, plan, region, cancel date, and stated reason. Find me the churn patterns by region and plan for the ops review."},
   {"who": "claude", "text": "Before you upload: look at what the analysis actually needs. Your question is about patterns by REGION, PLAN, DATE, and REASON — names, emails, and account numbers contribute nothing to it, and they're exactly the fields your data policy likely classifies as regulated personal data.\n\nThe compliant path costs you nothing analytically:\n1. Copy the sheet\n2. Delete the name, email, and account-number columns\n3. If you need to track repeat cancellations, replace account numbers with sequential IDs (C001, C002…) — a mapping only your team keeps, outside this tool\n4. Upload the minimized version\n\nSame patterns, same ops review, zero exposed identifiers. Note what does NOT work as a control: uploading everything and instructing me 'don't retain it' — my instructions aren't a data-handling control your policy recognizes. And abandoning the analysis is unnecessary — minimization enables it."},
   {"who": "user", "label": "Fixed", "text": "Minimized version uploaded — IDs, plan, region, dates, reasons only."},
   {"who": "claude", "text": "Analysis on the minimized data:\n\n• EU-South churn is 2.3× baseline, concentrated in the Starter plan within 60 days of onboarding — reasons cluster on 'missing local-language support'\n• Enterprise churn is flat, but three repeat-cancel IDs (C044, C112, C189) show a downgrade→cancel path worth an outreach play\n• Price-related reasons are stable QoQ — the June increase isn't the driver\n\nEvery finding, no personal data at risk. If ops later needs to contact specific at-risk customers, hand the flagged IDs to the team that holds the mapping — re-identification happens inside your controlled system, not here."},
 ]},

{"id": "6.3", "d": "d6",
 "title": "Follow organizational AI policies and governance standards",
 "concept": "Your organization's AI policy — approved tools, permitted data classes, "
            "required disclosures, mandatory review gates — is the operating boundary. "
            "Associates work within it, route exceptions through the proper channel, and "
            "treat 'the policy is inconvenient' as a reason to engage governance, never a "
            "reason to route around it.",
 "analogy": "Aviation checklists. Pilots don't skip items because today's flight seems "
            "routine — and when a checklist genuinely doesn't fit the aircraft, they file "
            "to change the checklist. They don't freelance at 30,000 feet.",
 "antipattern": "Shadow AI: pasting company data into a personal account on an unapproved "
                "tool because it's faster, assuming 'nobody said I couldn't', or shipping "
                "AI-generated client work without the disclosure the policy requires.",
 "right": "Know the policy before the workflow: which tools are sanctioned, what data may "
          "they touch, what needs human sign-off, what must be disclosed. When a rule "
          "blocks real value, document the case and request an exception through "
          "governance.",
 "pitfall": "Assuming silence means permission. If the policy doesn't address your new use "
            "case, that's a question for the AI governance owner — undefined is not "
            "approved.",
 "tip": "In exam scenarios, options that comply-then-escalate ('follow policy; raise the "
        "gap with governance') beat options that bypass, ignore, or unilaterally "
        "reinterpret the policy — even when the bypass is framed as harmless.",
 "links": ["6.2", "6.4"],
 "chat": [
   {"who": "note", "text": "An analyst hits a policy wall a week before a deadline."},
   {"who": "user", "label": "Tempted", "text": "Our AI policy only approves Claude for internal documents — client deliverables need a senior manager's review of any AI-assisted work, and mine is on leave until after my deadline. Honestly I could just not mention that Claude helped draft it. It's my analysis anyway — I'd review it myself. Thoughts?"},
   {"who": "claude", "text": "Don't do the quiet route — walk through what it actually is: the policy makes AI-assistance in client work a disclosed, reviewed activity. Omitting the disclosure isn't a shortcut, it's a policy violation with your name on it, and it converts a manageable scheduling problem into an integrity problem that surfaces at the worst times (client audit, quality dispute, or a colleague simply asking how you drafted it so fast).\n\nYour actual options, all boring and safe:\n1. The policy names a ROLE, not a person — is there an acting/covering senior manager? Usually yes.\n2. Ask your manager's manager to designate a reviewer — a two-line email, resolved today.\n3. Ask the client-facing deadline owner for 48 hours, citing internal QA.\n4. If none work: deliver the analysis WITHOUT AI assistance on the client-facing artifact, using Claude only for the internal prep the policy already permits.\n\nAnd afterwards, file the real finding: the policy has a single-point-of-failure on one reviewer. That's a governance improvement request — you'd be fixing the rule instead of breaking it."},
   {"who": "user", "text": "Option 2 worked — the director will review it Thursday. Draft the governance suggestion too."},
   {"who": "claude", "text": "To: AI Governance owner\nSubject: Policy gap — reviewer coverage for AI-assisted client work\n\n'Section 4.2 requires senior-manager review of AI-assisted client deliverables but names no backup when the reviewer is unavailable. This week that nearly blocked a client deadline (resolved via ad-hoc designation by the director). Request: amend 4.2 to name a covering-reviewer rule, so compliance never competes with delivery.'\n\nCompliant this week, better policy next quarter — that's how the boundary is supposed to move."},
 ]},

{"id": "6.4", "d": "d6",
 "title": "Understand the ethical implications of AI usage",
 "concept": "Beyond policy compliance sit the questions policy can't fully write down: "
            "bias (whose patterns did the data learn?), transparency (do affected people "
            "know AI was involved?), accountability (a human owns every consequential "
            "output), and honesty about AI's role in your work. Ethical use means asking "
            "'should we?' after 'can we?' — especially where outputs touch people.",
 "analogy": "A powerful lens: it lets you see more, and it distorts at the edges. An "
            "ethical user knows where the distortion lives, tells people they're looking "
            "through a lens, and never blames the lens for what they chose to do with it.",
 "antipattern": "'The AI decided' as an accountability shield; presenting wholly "
                "AI-written analysis as your independent expert judgment; or deploying a "
                "system that quietly disadvantages a group because nobody looked at the "
                "outputs across groups.",
 "right": "Bias: inspect outputs across groups before trusting a people-affecting "
          "workflow. Transparency: disclose AI involvement where it matters (clients, "
          "affected employees, published work). Accountability: every consequential "
          "output has a human owner who reviewed it and answers for it.",
 "pitfall": "Treating ethics as a launch-day checkbox. Bias and drift show up in "
            "operation — revisit outcomes over time, not just intentions at kickoff.",
 "tip": "Exam options embodying disclosure, human accountability, and bias-checking beat "
        "options that hide AI involvement, defer moral judgment to the tool, or treat "
        "'technically allowed' as 'ethically fine'.",
 "links": ["6.1", "4.4"],
 "chat": [
   {"who": "note", "text": "A marketing manager reviews an AI-assisted campaign targeting model before launch."},
   {"who": "user", "text": "We used Claude to help segment customers for our premium credit-card campaign, based on past approval patterns. Before launch — walk me through the ethical review, not just the legal one."},
   {"who": "claude", "text": "Four questions, in order of bite:\n\n1. BIAS — 'past approval patterns' is the loaded phrase. If historical approvals skewed by neighborhood, age, or proxies for protected classes, a segmentation learned from them reproduces that skew with perfect confidence. Check: compare the campaign's include/exclude rates across demographics you're able to observe. If certain groups vanish from 'premium eligible', you've automated yesterday's bias.\n\n2. TRANSPARENCY — would customers be surprised to learn how they were selected (or silently excluded)? Surprise is a decent ethics smoke alarm. Marketing selection is normal; what people don't expect is exclusion from OFFERS of credit via opaque profiling.\n\n3. ACCOUNTABILITY — who signs off on the segment list? If the answer is 'the model produced it', that's the anti-pattern. A named human should review the segmentation logic and own the outcome.\n\n4. HONESTY INTERNALLY — when you present results, the deck should say the segmentation was AI-assisted and how it was checked. Your leadership can't govern what it doesn't know exists.\n\nNote: much of this may ALSO be regulated (credit marketing often is) — but you asked the right question, because 'legal' would only tell you the floor."},
   {"who": "user", "text": "The demographic comparison shows two zip-code clusters almost entirely excluded — both historically underbanked areas."},
   {"who": "claude", "text": "That's the finding that stops a launch. The model has likely learned redlining's echo from the historical data. Path forward: (1) don't ship this segmentation; (2) rebuild on forward-looking, behavior-based criteria (stated interest, product usage) rather than inherited approval patterns; (3) bring compliance in — in credit contexts this pattern can be unlawful, not merely unfair; (4) document the catch — it's the strongest possible case for keeping human ethical review in every AI-assisted workflow that touches people."},
 ]},

# ============================== DOMAIN 7 — Troubleshooting and Optimization (10%) ==============================

{"id": "7.1", "d": "d7",
 "title": "Identify, diagnose, and resolve issues with underperforming prompts or poor outputs",
 "concept": "Debug prompts like a mechanic, not a gambler: reproduce the failure, classify "
            "it (missing context? ambiguous ask? wrong format? stale knowledge? task too "
            "big? wrong tool/model?), fix the diagnosed cause, and re-test on the same "
            "input. Each failure type has a matching repair.",
 "analogy": "A car that won't start. The gambler turns the key harder and buys a new car. "
            "The mechanic asks: fuel, battery, or starter? — because each has a different "
            "fix and checking is cheap.",
 "antipattern": "Re-running the identical prompt hoping for different output, bolting "
                "'be more accurate and detailed!!' onto it, or abandoning the tool — all "
                "without ever naming what KIND of failure occurred.",
 "right": "Triage first: wrong facts → context/knowledge gap (add sources); wrong focus → "
          "ambiguity (state the goal and audience); wrong shape → format unstated "
          "(specify it); ignores instructions in a long chat → context overflow (summarize "
          "+ restart); shallow on hard reasoning → task/model mismatch (decompose or "
          "upgrade).",
 "pitfall": "Fixing two variables at once. Change the prompt OR the knowledge OR the "
            "model, then re-test — simultaneous changes hide which fix worked, so the "
            "lesson is lost for next time.",
 "tip": "Exam troubleshooting stems describe symptoms. Match symptom → cause → minimal "
        "fix. Distractors re-roll, over-engineer, or swap tools without a diagnosis.",
 "links": ["1.3", "3.4"],
 "chat": [
   {"who": "note", "text": "An analyst's weekly KPI commentary prompt started producing junk."},
   {"who": "user", "label": "Symptom report", "text": "My weekly prompt — 'Write the KPI commentary for the ops dashboard from the attached export' — worked fine for months. The last two weeks it invents targets we don't have and comments on metrics that aren't in the export. Diagnose before you fix."},
   {"who": "claude", "text": "Two distinct symptoms — let's classify each:\n\nSYMPTOM 1: 'invents targets we don't have' → fabrication filling a CONTEXT GAP. The prompt says 'commentary' but never provides targets, so plausible ones get invented. It 'worked for months' likely because earlier exports included a target column — did the export format change recently?\n\nSYMPTOM 2: 'comments on metrics not in the export' → same root family: the task is underspecified about scope, so general KPI knowledge leaks in.\n\nDiagnosis test (cheap, one run): re-run last week's export with one added line — 'Comment ONLY on metrics present in the export. Targets are in column D; if column D is empty, write \'no target set\' rather than inferring one.' If both symptoms vanish, confirmed: this was a context + scope-specification failure, not model degradation."},
   {"who": "user", "text": "Confirmed — export format changed 3 weeks ago, the target column was dropped. Your test line fixed both symptoms. Make the fix permanent."},
   {"who": "claude", "text": "Permanent repair, addressing cause not symptom:\n1. Restore targets as INPUT: ask ops to re-include column D, or attach the targets sheet alongside the export\n2. Harden the prompt: 'Scope: ONLY metrics in the export. Targets: ONLY from column D / targets sheet — never inferred. If a target is missing, say so.'\n3. Add a canary: end each run with 'List any metric you commented on that lacks a source row' — an empty list is your weekly health check.\n\nOne diagnosed cause, one targeted fix, re-tested on the same input — and a tripwire so the next format change announces itself."},
 ]},

{"id": "7.2", "d": "d7",
 "title": "Adjust approach based on feedback and results",
 "concept": "Treat AI workflows as feedback systems: collect signals (edit distance from "
            "final versions, user corrections, spot-check results, complaint themes), read "
            "what they say about the setup, and adjust the prompt, knowledge, format, or "
            "process — then keep watching. One-time setup is a myth; calibration is the "
            "job.",
 "analogy": "A thermostat, not a fire-and-forget heater. It works because it keeps "
            "measuring the room and correcting. A heater with no sensor is 'set up "
            "correctly' right until the room is an oven.",
 "antipattern": "Shipping a workflow and never looking at what users do with its outputs — "
                "or the opposite reflex: rebuilding everything after one bad anecdote "
                "instead of checking whether it's a pattern.",
 "right": "Instrument lightly: where do humans edit the drafts most? which questions come "
          "back? what do spot-checks catch? Aggregate before acting — patterns get fixes, "
          "anecdotes get logged. Adjust one lever, re-measure.",
 "pitfall": "Optimizing for the loudest complaint. A senior stakeholder's one-off gripe "
            "and a systematic 30% edit-rate are different classes of signal; rank by "
            "frequency × impact, not volume of the complainer.",
 "tip": "Exam answers that gather feedback, find the pattern, and adjust the specific "
        "failing element beat 'rebuild from scratch', 'ignore it', and 'add a disclaimer'.",
 "links": ["7.1", "4.3"],
 "chat": [
   {"who": "note", "text": "A proposal-drafting workflow has been live for six weeks — time to read the signals."},
   {"who": "user", "text": "Six weeks of our Claude proposal-drafting workflow. Feedback so far: sales edits the pricing section heavily in 9 of 12 proposals; two reps say the tone is 'too formal for startups'; one VP hated one proposal ('unusable') but couldn't say why; the exec summaries are apparently loved. What do we change?"},
   {"who": "claude", "text": "Rank the signals before touching anything:\n\n1. PRICING EDITS — 9/12 is a SYSTEMATIC signal, highest priority. Diagnose the edits: are reps fixing wrong numbers (→ stale pricing knowledge — check when the price file was last updated) or re-structuring how pricing is presented (→ template/instruction gap)? Pull three edited versions and diff them against the drafts; the edits will tell you which.\n\n2. TONE FOR STARTUPS — pattern (two independent reps, same theme). Fix is cheap: add an audience switch to the prompt/Project — 'if prospect is <100 employees, use direct, informal register; drop the compliance boilerplate to an appendix.'\n\n3. VP ANECDOTE — n=1 with no failure description. Don't rebuild anything for it; log it, and ask the VP's team for the specific proposal to inspect. If it matches pattern 1 or 2, it's already covered.\n\n4. EXEC SUMMARIES — positive signal: change NOTHING there, and say so explicitly in any revision notes so nobody 'improves' the part that works.\n\nOne lever at a time: fix pricing first, re-measure the edit rate for two weeks, then tone."},
   {"who": "user", "text": "Diffed the pricing edits — reps are correcting discount tiers that changed in a June sales-ops memo. The Project's pricing doc predates it."},
   {"who": "claude", "text": "So the workflow was drafting from a stale snapshot — a knowledge-maintenance failure surfacing as an editing burden (lesson 5.4's territory). Swap in the current tier sheet, add sales-ops memos to the update-trigger list, and re-measure: pricing edit-rate should collapse from 9/12 toward ~2/12 (genuine deal-specific tailoring). If it doesn't, the diagnosis was incomplete — back to the diffs."},
 ]},

{"id": "7.3", "d": "d7",
 "title": "Optimize workflows for efficiency and effectiveness",
 "concept": "Once a workflow WORKS, make it economical: cut redundant steps and re-pasted "
            "context (Projects/templates), batch similar items instead of one-at-a-time "
            "chats, right-size the model per step, stop over-polishing internal drafts, "
            "and measure end-to-end time — including the human review — not just the AI "
            "seconds.",
 "analogy": "A commercial kitchen during service: same dishes, but mise en place ready "
            "(persistent context), orders fired in batches, the sous-chef on prep and the "
            "head chef only on finishing (model right-sizing). The food isn't better — "
            "it's the same food, sustainably faster.",
 "antipattern": "Optimizing the wrong denominator: shaving AI response seconds while every "
                "output still waits two days for one over-loaded reviewer — or polishing "
                "internal status notes to publication grade at 3× the cost.",
 "right": "Profile the whole flow: where do items wait? what's re-done every time? what "
          "quality level does each output actually need? Then: template the repeated, "
          "batch the similar, downsize models where review nets are strong, and fix the "
          "human bottleneck the numbers point at.",
 "pitfall": "Efficiency that silently drops effectiveness — batching so aggressively or "
            "downsizing so far that error rates climb past what the review step absorbs. "
            "Optimize with the quality metric on the dashboard, not after it.",
 "tip": "Exam optimization answers keep quality safeguards while removing redundancy "
        "(batching, templates, right-sized models, fewer handoffs). Distractors remove "
        "the safeguards or optimize a step that wasn't the bottleneck.",
 "links": ["3.3", "5.1"],
 "chat": [
   {"who": "note", "text": "A team's content-localization workflow works — but costs too much time per item."},
   {"who": "user", "text": "Our product-update localization flow works but feels heavy. Per update: writer drafts in a chat (re-pasting the glossary every time), Claude adapts it for 5 regions one-by-one in 5 separate chats, then our one bilingual reviewer checks all 5 — she's a 2-day bottleneck. ~20 updates/month. Optimize it."},
   {"who": "claude", "text": "Profile first — where the ~non-AI time goes: re-pasted setup (×20/month), five sequential chats per item (×20), and a single human reviewer absorbing 100 region-variants a month. Now the levers:\n\n1. KILL REDUNDANT CONTEXT: 'Localization' Project — glossary, tone rules per region, and banned-terms list as knowledge + instructions. Saves the paste ritual on every one of ~120 chats/month.\n\n2. BATCH THE SIMILAR: one chat per update produces all 5 regional variants in a single structured pass ('output a section per region'). 100 chats → 20.\n\n3. RIGHT-SIZE QUALITY PER OUTPUT: these are product updates (internal-ish, templated), not brand campaigns — a mid-tier model with the Project's glossary is the right spend; save top-tier for the quarterly launch posts.\n\n4. THE REAL BOTTLENECK IS THE REVIEWER: don't remove her — refocus her. Have Claude self-annotate each variant with the 3 riskiest translation choices it made ('idiom replaced', 'regulatory term — verify'). She reviews flagged items deeply and spot-checks the rest, instead of reading everything cold. 2 days → hours, with the safety net intact.\n\nProjected: ~60% cycle-time cut, review quality signal IMPROVES (attention goes where risk is)."},
   {"who": "user", "text": "And how do we make sure the batching and cheaper model don't quietly degrade quality?"},
   {"who": "claude", "text": "Put the quality metric on the dashboard BEFORE switching: track reviewer correction-rate per variant for the current setup (baseline), then run the optimized flow in parallel for two weeks and compare. Accept the change only if corrections stay within the baseline band. Optimization without a quality gauge isn't optimization — it's cost-cutting with the lights off."},
 ]},
]
