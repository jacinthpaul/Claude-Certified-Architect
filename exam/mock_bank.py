"""
exam/mock_bank.py — 60-question blueprint-aligned MOCK EXAM bank
============================================================================
Verified, exam-style scenario questions cross-checked against the official Claude
Certified Architect – Foundations Exam Guide. Each item carries the correct answer, a
letter-free explanation (so option order can be shuffled in the console), and the
official Domain / Task Statement reference the question tests.

These power the console's Mock Exam (ui/console). Tagged M1..M60.
Not official exam items; a study aid.
"""
import sys
import os
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ccarch import banner, h1, kv, note, right, tip, rule

# Each: task, domain, q (prompt), options A-D, answer letter, why (letter-free), ref.
MOCK_BANK = [
    dict(task='1.1', domain='d1',
         q="You're building an agent that resolves each user request by calling tools in a loop — looking something up, checking a rule, then acting — until the request is fully handled. After every model turn, your control-flow code has to decide whether to run another tool or stop and return the final answer. Which condition should your control-flow code use to make that decision?",
         options={
             'A': 'Parse the assistant’s text each turn for a keyword such as "done" or "complete"',
             'B': 'Continue while stop_reason is "tool_use"; terminate when it is "end_turn"',
             'C': 'Stop after a fixed cap of 10 iterations, regardless of the turn’s state',
             'D': 'Stop as soon as any tool call returns an error instead of a result',
         },
         answer='B',
         why='The stop_reason field is the model\'s explicit control signal: "tool_use" means Claude wants a tool executed and the loop should continue; "end_turn" means it has finished. Parsing text and stopping on any error are anti-patterns the exam guide names explicitly, because they misread the model\'s intent, and a hard iteration cap is a safety backstop, not the primary termination mechanism.',
         ref='Domain 1, Task Statement 1.1 — Design and implement agentic loops for autonomous task execution.'),

    dict(task='1.2', domain='d1',
         q="You're designing a multi-agent system where a coordinator delegates sub-tasks to subagents through the Task tool, and you're deciding how much information to pass into each one. When a coordinator agent spawns a subagent via the Task tool, what does the subagent know about the coordinator's prior conversation?",
         options={
             'A': 'It automatically inherits the full conversation history of the coordinator',
             'B': 'It shares a live memory space with the coordinator and all sibling subagents',
             'C': 'Nothing — it starts isolated and knows only what its prompt passes in',
             'D': "It inherits the coordinator's system prompt but none of its tool results",
         },
         answer='C',
         why="Subagents operate with isolated context; they do not inherit the coordinator's conversation history or share memory between invocations. The coordinator must inject any needed findings directly into the subagent's prompt, which is why explicit context passing is a core design responsibility rather than an automatic behavior.",
         ref='Domain 1, Task Statement 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns (also relates to Task Statement 1.3).'),

    dict(task='1.3', domain='d1',
         q="You're wiring up a coordinator that should delegate sub-topics to specialist subagents, but at runtime its spawn attempts silently do nothing and no subagents ever run, so you start checking its configuration. For a coordinator agent to invoke subagents through the Task tool, what configuration is required?",
         options={
             'A': 'The coordinator’s allowedTools must include "Task"',
             'B': 'Each subagent must be granted tool_choice: "any"',
             'C': 'The .mcp.json file must list every subagent as a server',
             'D': 'The coordinator must be running in plan mode when it spawns',
         },
         answer='A',
         why='The Task tool is the mechanism for spawning subagents, and the exam guide states that allowedTools must include "Task" for a coordinator to invoke them. Without it, the coordinator cannot delegate. The other options confuse tool-choice configuration, MCP server scoping, and Claude Code modes with subagent enablement.',
         ref='Domain 1, Task Statement 1.3 — Configure subagent invocation, context passing, and spawning.'),

    dict(task='1.2', domain='d1',
         q='A multi-agent research system on the topic "impact of AI on creative industries" produces reports covering only visual arts, omitting music, writing, and film. Coordinator logs show it split the topic into "AI in digital art," "AI in graphic design," and "AI in photography." Each subagent completed its assigned task correctly. What is the most likely root cause?',
         options={
             'A': 'The synthesis subagent is filtering out findings that are not visual arts',
             'B': "The coordinator's decomposition was too narrow to cover the full topic",
             'C': "The web-search subagent's queries were not comprehensive enough",
             'D': 'The document-analysis subagent applied overly restrictive relevance criteria',
         },
         answer='B',
         why='The logs show the coordinator decomposed a broad topic into three narrow visual-arts subtasks, so the missing domains were never assigned to any subagent. The downstream agents worked correctly within their scope — the failure is upstream, in decomposition. Blaming synthesis, search, or analysis misattributes a coordinator planning error; the guide calls out the risk of overly narrow decomposition leading to incomplete coverage.',
         ref='Domain 1, Task Statement 1.2 — Orchestrate multi-agent systems with coordinator-subagent patterns. Closely parallels Official Exam Guide Sample Question 7.'),

    dict(task='1.4', domain='d1',
         q='Your customer-support agent must verify a customer\'s identity via get_customer before it is ever allowed to call process_refund. Prompt instructions telling it to "always verify first" still fail in about 12% of cases, causing incorrect refunds. What is the most reliable fix?',
         options={
             'A': 'Add few-shot examples showing the agent always calling get_customer first',
             'B': 'Strengthen the system prompt to state that identity verification is mandatory',
             'C': 'Add a prerequisite gate that blocks process_refund until get_customer returns an ID',
             'D': 'Lower the model temperature so the agent follows the ordering instruction literally',
         },
         answer='C',
         why='When deterministic compliance is required — especially for financial operations — programmatic enforcement via hooks or prerequisite gates provides guarantees that prompt-based approaches cannot, because prompt instructions have a non-zero failure rate. Few-shot examples and stronger prompts remain probabilistic, and temperature does not enforce tool ordering.',
         ref='Domain 1, Task Statement 1.4 — Implement multi-step workflows with enforcement and handoff patterns. Closely parallels Official Exam Guide Sample Question 1.'),

    dict(task='1.5', domain='d1',
         q='An Agent SDK application receives tool results from several MCP tools that report timestamps inconsistently — some as Unix epochs, some as ISO 8601, some as numeric status codes. You want to normalize these before the model reasons over them. Which mechanism is designed for this?',
         options={
             'A': 'A PostToolUse hook that intercepts and transforms tool results',
             'B': 'A tool_choice: "any" setting applied to every tool in the array',
             'C': 'A .claude/rules/ file whose frontmatter globs the tool outputs',
             'D': 'The --resume flag with a named session to carry formats forward',
         },
         answer='A',
         why='PostToolUse hooks intercept tool results after execution and before the model processes them — exactly where heterogeneous data formats are normalized deterministically. This scenario (Unix timestamps, ISO 8601, numeric status codes) appears verbatim in Task Statement 1.5. Tool choice governs which tool is called, path rules apply to Claude Code file conventions, and --resume is for session continuity.',
         ref='Domain 1, Task Statement 1.5 — Apply Agent SDK hooks for tool call interception and data normalization.'),

    dict(task='1.3', domain='d1',
         q='Your research pipeline currently runs its subagents one after another, and end-to-end latency is too high because each one waits for the previous to finish. You want them to run in parallel instead. How does the coordinator achieve parallel execution?',
         options={
             'A': 'It emits multiple Task tool calls in a single coordinator response',
             'B': 'It sets max_tokens to a higher value so more subagents fit per turn',
             'C': 'It issues one Task call per turn across several sequential turns',
             'D': 'It enables fork_session on each subagent it intends to run',
         },
         answer='A',
         why="Spawning parallel subagents is done by emitting multiple Task tool calls in a single coordinator response rather than across separate turns, so total time approaches that of the slowest subagent. Anthropic's multi-agent research system writeup reports large latency reductions from this fan-out pattern. One call per turn is sequential by definition; max_tokens affects output length, and fork_session branches a session for divergent exploration, not parallel fan-out.",
         ref='Domain 1, Task Statement 1.3 — Configure subagent invocation, context passing, and spawning.'),

    dict(task='1.3', domain='d1',
         q="A coordinator prompt for research subagents currently gives rigid step-by-step procedural instructions and produces brittle, low-coverage results. Following Anthropic's guidance, how should the coordinator prompt be written to improve subagent adaptability?",
         options={
             'A': 'Specify research goals and quality criteria rather than procedural steps',
             'B': 'Provide the exact sequence of tool calls each subagent must make, in order',
             'C': "Remove the instructions entirely and rely on the model's own defaults",
             'D': 'Instruct each subagent to route every decision back to the coordinator',
         },
         answer='A',
         why='Task Statement 1.3 calls for coordinator prompts that specify research goals and quality criteria rather than step-by-step procedural instructions, letting subagents adapt to what they discover. Each subagent still needs an objective, an output format, tool guidance, and clear task boundaries. Rigid tool sequences reduce adaptability, no instructions removes needed direction, and routing every decision back creates unnecessary round-trips and latency.',
         ref='Domain 1, Task Statement 1.3 — Configure subagent invocation, context passing, and spawning.'),

    dict(task='2.3', domain='d2',
         q='Your synthesis subagent frequently needs to verify simple facts (dates, names, statistics) while combining findings. Currently each verification routes back through the coordinator to the web-search subagent, adding 2–3 round trips and increasing latency by 40%. Evaluation shows 85% of verifications are simple fact-checks and 15% require deeper investigation. What is the most effective change?',
         options={
             'A': 'Give the synthesis subagent access to all web-search tools so it self-serves',
             'B': 'Give the synthesis subagent a scoped verify_fact tool, leaving complex checks routed',
             'C': 'Batch all verification needs and send them to the coordinator at the end',
             'D': 'Have the search subagent pre-cache extra context around every source it finds',
         },
         answer='B',
         why="A scoped cross-role tool applies least privilege: it gives synthesis exactly what it needs for the common 85% case while preserving coordinator routing for the complex 15% — the guide's own example of a scoped verify_fact tool for high-frequency needs. Full tool access violates separation of concerns, batching breaks dependencies between verified facts, and speculative caching cannot reliably predict what will be needed.",
         ref='Domain 2, Task Statement 2.3 — Distribute tools appropriately across agents and configure tool choice. Closely parallels Official Exam Guide Sample Question 9.'),

    dict(task='1.6', domain='d1',
         q="You're structuring a multi-step workflow and weighing a fixed pipeline of predefined steps against a plan that adapts as it discovers more about the task. When should you choose a fixed sequential pipeline (prompt chaining) over dynamic adaptive decomposition for a workflow?",
         options={
             'A': 'When the task is open-ended investigation whose subtasks depend on discoveries',
             'B': 'When the workflow is a predictable review with known steps (per-file, then cross-file)',
             'C': 'Whenever more than two subagents are involved in producing the result',
             'D': 'Only when the model in use does not support tool calling at all',
         },
         answer='B',
         why="Prompt chaining fits predictable, well-understood multi-step workflows where the steps are known in advance — the guide's example is analyzing each file individually and then running a cross-file integration pass. Open-ended investigation whose next steps depend on what is found calls for dynamic, adaptive decomposition. Subagent count and tool-use support are not the deciding factors.",
         ref='Domain 1, Task Statement 1.6 — Design task decomposition strategies for complex workflows.'),

    dict(task='1.4', domain='d1',
         q='A customer sends a single message containing three distinct issues (a billing error, a shipping delay, and an account lockout). What is the recommended way to handle this multi-concern request?',
         options={
             'A': 'Escalate immediately to a human because multiple issues are too complex to automate',
             'B': 'Handle only the first issue mentioned and ask the customer to resubmit the others',
             'C': 'Decompose it into distinct items, investigate each in parallel, then synthesize one reply',
             'D': 'Pick the highest-priority issue by sentiment score and ignore the remaining two',
         },
         answer='C',
         why='Task Statement 1.4 describes decomposing multi-concern customer requests into distinct items, investigating each in parallel using shared context, then synthesizing a unified resolution. Immediate escalation and handling one issue fail the customer, and sentiment-based prioritization is an unreliable proxy that drops legitimate concerns.',
         ref='Domain 1, Task Statement 1.4 — Implement multi-step workflows with enforcement and handoff patterns.'),

    dict(task='1.5', domain='d1',
         q='Your support agent can issue refunds, and policy requires that any refund over $500 be blocked and redirected to a human — with no way for the model to talk its way past it. You decide to enforce this with an Agent SDK hook. Which hook pattern enforces this deterministically?',
         options={
             'A': 'A PostToolUse hook that logs every refund once it has already executed',
             'B': 'A PreToolUse gate that blocks process_refund above the threshold and escalates',
             'C': 'A system-prompt instruction telling the agent it must never exceed the $500 limit',
             'D': 'Setting tool_choice to "none" for the refund tool on every request',
         },
         answer='B',
         why="A hook that intercepts outgoing tool calls can block policy-violating actions before they execute and redirect them to an alternative workflow — the guide's exact example is blocking refunds exceeding $500 and redirecting to human escalation. A PostToolUse log runs after the refund already happened, a prompt instruction is probabilistic, and disabling the tool entirely prevents legitimate refunds rather than conditionally gating them.",
         ref='Domain 1, Task Statement 1.5 — Apply Agent SDK hooks for tool call interception and data normalization.'),

    dict(task='1.7', domain='d1',
         q='You are resuming a Claude Code investigation session after several analyzed files have been substantially modified. The prior tool results are now stale. What is the most reliable approach?',
         options={
             'A': 'Resume with --resume and rely on the previously captured tool results as they are',
             'B': 'Start a fresh session and inject a structured summary naming the changed files',
             'C': 'Fork the stale session with fork_session and continue along both branches',
             'D': 'Increase max_tokens so the old context still fits alongside the new reads',
         },
         answer='B',
         why='Task Statement 1.7 states that starting a new session with a structured summary is more reliable than resuming with stale tool results, and that a resumed agent should be informed about changes to previously analyzed files. Blind --resume carries stale results forward, forking duplicates the stale context into two branches, and max_tokens does not address context correctness.',
         ref='Domain 1, Task Statement 1.7 — Manage session state, resumption, and forking.'),

    dict(task='1.7', domain='d1',
         q='You want to explore two different refactoring approaches from the same analyzed starting point without one contaminating the other, and while planning you come across fork_session. What is the primary purpose of fork_session in the Agent SDK / Claude Code?',
         options={
             'A': 'To branch from a shared analysis baseline and explore divergent approaches',
             'B': 'To permanently merge two separate sessions into a single combined one',
             'C': 'To compress the context window of the current session in place',
             'D': 'To promote a running subagent into a coordinator of its own',
         },
         answer='A',
         why='fork_session creates independent branches from a shared analysis baseline so you can explore divergent approaches — for example, comparing two testing strategies or refactoring approaches — without cross-contaminating them. It does not merge sessions, compress context (that is what /compact does), or change agent roles.',
         ref='Domain 1, Task Statement 1.7 — Manage session state, resumption, and forking.'),

    dict(task='1.4', domain='d1',
         q='A support agent handling a mid-process escalation must hand off to a human who cannot see the conversation transcript. What should the structured handoff summary include?',
         options={
             'A': "Only the customer's raw message text, copied verbatim from the chat",
             'B': 'The customer ID, root cause, refund amount, and recommended action',
             'C': 'A model-generated confidence score for the case and nothing further',
             'D': 'The full untrimmed tool output from every call made in the session',
         },
         answer='B',
         why='Because the human agent lacks the transcript, the handoff must be a compiled structured summary — customer ID, root cause, relevant amounts, and a recommended action — so the human can act immediately. This exact field list appears in Task Statement 1.4. Raw message text lacks analysis, a lone confidence score is not actionable, and dumping every tool output buries the signal.',
         ref='Domain 1, Task Statement 1.4 — Implement multi-step workflows with enforcement and handoff patterns.'),

    dict(task='1.1', domain='d1',
         q="You're deciding whether a new automation should be built as a model-driven agent or as a hard-coded, pre-configured decision tree. Which of the following is the clearest example of when an agentic architecture (model-driven decision-making) is preferable to a pre-configured decision tree?",
         options={
             'A': 'A workflow whose exact sequence of steps is fixed and known well in advance',
             'B': 'An open-ended task where the next action depends on what each step reveals',
             'C': 'A single-call classification that returns one of three fixed categories',
             'D': 'A deterministic identity-verification gate before a financial transaction',
         },
         answer='B',
         why='Agentic, model-driven control shines when the path cannot be fully specified upfront and Claude must reason about the next tool based on newly discovered context — the core distinction Task Statement 1.1 draws against pre-configured decision trees. Fixed sequences, simple classification, and deterministic compliance gates are better served by pre-configured logic or programmatic enforcement.',
         ref='Domain 1, Task Statement 1.1 — Design and implement agentic loops for autonomous task execution.'),

    dict(task='2.1', domain='d2',
         q='Production logs show your agent often calls get_customer when users ask about orders (e.g., "check my order #12345") instead of lookup_order. Both tools have minimal one-line descriptions and accept similar identifiers. What is the most effective first step?',
         options={
             'A': 'Add 5–8 few-shot examples showing order queries routing to lookup_order',
             'B': "Expand each tool's description with input formats, example queries, and edge cases",
             'C': 'Add a keyword-based routing layer that pre-selects the tool before each turn',
             'D': 'Consolidate both into one lookup_entity tool that guesses the right backend',
         },
         answer='B',
         why="Tool descriptions are the primary mechanism LLMs use for tool selection; minimal descriptions are the root cause of misrouting among similar tools, and enriching them is the low-effort, high-leverage first fix. Few-shot examples add token overhead without addressing the cause, a routing layer is over-engineered and bypasses the model's language understanding, and consolidation is a larger architectural change than a first step warrants.",
         ref='Domain 2, Task Statement 2.1 — Design effective tool interfaces with clear descriptions and boundaries. Closely parallels Official Exam Guide Sample Question 2.'),

    dict(task='2.2', domain='d2',
         q='An MCP tool fails because the backend database is temporarily overloaded. Which structured error response best enables the agent to recover appropriately?',
         options={
             'A': '{ "isError": true, "errorCategory": "transient", "isRetryable": true }',
             'B': 'A generic "Operation failed" string carrying no structured metadata',
             'C': 'An empty result set marked as a success, with isError set to false',
             'D': 'A thrown exception that propagates up and terminates the whole session',
         },
         answer='A',
         why='A structured error with isError: true, an errorCategory of transient, and isRetryable: true tells the agent the request is valid and should succeed on retry — the structured-metadata pattern Task Statement 2.2 prescribes. A generic message hides recovery information, marking failure as success suppresses the error and risks bad decisions, and terminating the session prevents any recovery.',
         ref='Domain 2, Task Statement 2.2 — Implement structured error responses for MCP tools.'),

    dict(task='2.2', domain='d2',
         q="You're designing the structured error responses your MCP tools return so the agent retries only what is safe to retry and stops wasting calls on failures that will never succeed. Which pairing of MCP error category and retry behavior is correct?",
         options={
             'A': 'A business-rule violation (refund exceeds the policy limit) → retryable',
             'B': 'A validation error on malformed input → retryable without any changes',
             'C': 'A transient timeout → retryable; a permission error → not retryable',
             'D': 'Every error category → retryable with exponential backoff applied',
         },
         answer='C',
         why='Transient errors (timeouts, service unavailability) are retryable; permission and business-rule errors are not, because retrying the identical request will keep failing. Business violations are non-retryable policy outcomes that need customer-friendly explanations, validation errors require changed input rather than a blind retry, and treating all errors as retryable wastes attempts on permanent failures.',
         ref='Domain 2, Task Statement 2.2 — Implement structured error responses for MCP tools.'),

    dict(task='2.3', domain='d2',
         q='An agent has access to 18 tools and frequently selects the wrong one, even when instructed to search first. According to CCA-F guidance, what is the most effective architectural change?',
         options={
             'A': 'Rewrite all 18 tool descriptions to be substantially longer and far more detailed',
             'B': 'Combine all 18 capabilities into a single monolithic tool with a mode flag',
             'C': "Cut each agent's tool set to the 4–5 its role needs, spread across specialists",
             'D': 'Add better error handling so the agent recovers after picking the wrong tool',
         },
         answer='C',
         why='Task Statement 2.3 states that giving an agent too many tools (e.g., 18 instead of 4–5) degrades selection reliability by increasing decision complexity; scoping each agent to the tools its role needs, distributed across specialized agents, is the recommended fix. Longer descriptions do not solve decision overload, a monolithic tool hides distinct capabilities, and recovery handling treats the symptom rather than the cause.',
         ref='Domain 2, Task Statement 2.3 — Distribute tools appropriately across agents and configure tool choice.'),

    dict(task='4.3', domain='d4',
         q='You have three extraction schemas (invoice, receipt, contract) and the incoming document type is unknown. You need the model to always produce structured output rather than conversational text, but it may choose which schema fits. Which tool_choice setting fits?',
         options={
             'A': '"auto"',
             'B': '"any"',
             'C': '{"type": "tool", "name": "extract_invoice"}',
             'D': '"none"',
         },
         answer='B',
         why='tool_choice: "any" forces the model to call one of the provided tools but lets it choose which — the guide\'s prescribed setting for guaranteeing structured output when multiple extraction schemas exist and the document type is unknown. "auto" permits a plain-text response, forced selection locks to one schema regardless of document type, and "none" blocks tool calls entirely.',
         ref='Domain 4, Task Statement 4.3 — Enforce structured output using tool use and JSON schemas (also relates to Task Statement 2.3).'),

    dict(task='2.3', domain='d2',
         q="You're assembling a document-processing pipeline where several enrichment tools depend on metadata that another tool produces, so extract_metadata must always run before any enrichment tools. You want to guarantee that ordering rather than hope the model picks it. Which configuration guarantees this ordering on the first call?",
         options={
             'A': 'tool_choice: "auto" on every call in the pipeline',
             'B': 'tool_choice: "any" on every call in the pipeline',
             'C': 'tool_choice: {"type": "tool", "name": "extract_metadata"}, then "auto" after',
             'D': 'Listing extract_metadata first in the tools array and leaving choice to "auto"',
         },
         answer='C',
         why='Forced tool selection guarantees a specific named tool runs first — the guide\'s own example is forcing extract_metadata before enrichment tools — and switching to "auto" in follow-up turns lets the model proceed with the remaining steps. "auto" and "any" do not guarantee which tool is called, and mere ordering in the tools array does not enforce selection.',
         ref='Domain 2, Task Statement 2.3 — Distribute tools appropriately across agents and configure tool choice (also relates to Task Statement 4.3).'),

    dict(task='2.4', domain='d2',
         q='Where should a shared MCP server used by the whole team (e.g., a GitHub server needing a token) be configured, and how should the credential be handled?',
         options={
             'A': 'In user-level ~/.claude.json, with the API token hard-coded in the file',
             'B': 'In project-level .mcp.json, expanding ${GITHUB_TOKEN} from the environment',
             'C': 'In the root CLAUDE.md file, written out as plain text for every teammate to see',
             'D': "In each developer's own shell profile, exported before Claude Code starts",
         },
         answer='B',
         why='Project-scoped.mcp.json is committed to version control so all teammates get the server, and environment-variable expansion (${GITHUB_TOKEN}) manages credentials without committing secrets — both named explicitly in Task Statement 2.4. User-level config is not shared and hard-coding leaks secrets, CLAUDE.md is for instructions rather than server config, and shell-profile-only setup is not shared or reproducible.',
         ref='Domain 2, Task Statement 2.4 — Integrate MCP servers into Claude Code and agent workflows.'),

    dict(task='2.4', domain='d2',
         q='Your agent keeps preferring the built-in Grep tool over a more capable custom MCP tool that could answer the query better. What is the recommended fix?',
         options={
             'A': 'Delete the built-in Grep tool from the environment so that it cannot be chosen',
             'B': "Enhance the MCP tool's description to spell out its capabilities and outputs",
             'C': 'Force tool_choice: "any" on every request the agent makes',
             'D': 'Move the MCP server from project scope to user scope',
         },
         answer='B',
         why='The model routes on tool descriptions; Task Statement 2.4 specifically calls for enhancing MCP tool descriptions to explain capabilities and outputs in detail, preventing the agent from preferring built-in tools like Grep over more capable MCP tools. Removing built-ins is heavy-handed and may break other flows, forcing a tool call does not fix which tool is chosen, and changing scope is irrelevant to selection quality.',
         ref='Domain 2, Task Statement 2.4 — Integrate MCP servers into Claude Code and agent workflows.'),

    dict(task='2.4', domain='d2',
         q="While integrating an MCP server into your workflow, you're deciding whether to expose certain capabilities as tools the model calls or as resources it reads. When should MCP resources (rather than tools) be used?",
         options={
             'A': 'To perform state-changing actions such as processing a customer refund',
             'B': 'To expose content catalogs — issue summaries, docs trees, database schemas',
             'C': 'To enforce workflow ordering between two tools that must always run in sequence',
             'D': 'To normalize timestamps arriving from several different backend services',
         },
         answer='B',
         why="MCP resources expose readable content catalogs — the guide's examples are issue summaries, documentation hierarchies, and database schemas — giving agents visibility into available data and reducing exploratory tool calls. Actions like refunds are tools, ordering enforcement is a tool_choice/hooks concern, and timestamp normalization is a PostToolUse hook task.",
         ref='Domain 2, Task Statement 2.4 — Integrate MCP servers into Claude Code and agent workflows.'),

    dict(task='2.5', domain='d2',
         q='While setting up a test-coverage sweep, a developer needs to find every file matching **/*.test.tsx across a large codebase before editing any of them. Which built-in tool is appropriate for locating them, and why?',
         options={
             'A': 'Grep, because it searches inside file contents for matching patterns',
             'B': 'Glob, because it matches file paths by name and extension patterns',
             'C': 'Read, because it loads the contents of files into the context',
             'D': 'Bash, because only shell commands can enumerate files recursively',
         },
         answer='B',
         why="Glob matches files by path/name patterns — the guide's own example for Glob selection is **/*.test.tsx. Grep searches inside file contents for text such as function names or error messages, Read loads a known file's contents, and while Bash could work, the purpose-built tool is Glob.",
         ref='Domain 2, Task Statement 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively.'),

    dict(task='2.5', domain='d2',
         q="You ask the agent to change one line in a file, but the Edit operation fails because the anchor text it is trying to match appears in more than one place in the file, so the change isn't unique. What is the recommended fallback?",
         options={
             'A': 'Retry the Edit several times until one of the attempts succeeds',
             'B': 'Use Read to load the full file, then Write the modified contents',
             'C': 'Delete the file and recreate it from scratch with the change applied',
             'D': 'Switch to Grep and make the change through its replacement mode',
         },
         answer='B',
         why="When Edit cannot find a unique text match, the guide's recommended fallback is Read + Write: load the full contents, then write back the modification reliably. Blind retries will keep failing on non-unique text, deleting and recreating risks data loss, and Grep only searches — it cannot modify files.",
         ref='Domain 2, Task Statement 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively.'),

    dict(task='2.1', domain='d2',
         q="Your team exposed a single generic analyze_document tool, and the agent keeps misusing it because it does too many unrelated things and its description can't clearly say when to call it. Following tool-design best practices, what is the better structure?",
         options={
             'A': 'Keep the single generic tool but give it a much longer description',
             'B': 'Split it into purpose-specific tools with defined input/output contracts',
             'C': 'Rename it to analyze_content without changing what it actually does',
             'D': 'Give it tool_choice: "any" so the model always calls it',
         },
         answer='B',
         why='Splitting an overloaded generic tool into purpose-specific tools with clear input/output contracts improves selection reliability and predictability — the guide uses exactly this analyze_document split as its example. A longer description does not fix functional overlap, a rename leaves the ambiguity intact, and forcing the tool does not address that it conflates multiple purposes.',
         ref='Domain 2, Task Statement 2.1 — Design effective tool interfaces with clear descriptions and boundaries.'),

    dict(task='2.3', domain='d2',
         q='In your multi-agent pipeline, a synthesis subagent is attempting web searches even though search is outside its role, and the extra freedom is producing poor, unfocused results. What is the best corrective design?',
         options={
             'A': 'Give every subagent access to the full tool set for maximum flexibility',
             'B': "Restrict each subagent's tools to those its own role actually requires",
             'C': "Increase the coordinator's max_tokens so it can supervise more closely",
             'D': 'Move the search tool definition into CLAUDE.md so it is documented',
         },
         answer='B',
         why="Task Statement 2.3 notes that agents with tools outside their specialization tend to misuse them — its example is precisely a synthesis agent attempting web searches — and prescribes restricting each subagent's tool set to its role. Universal tool access makes the problem worse, max_tokens is unrelated, and CLAUDE.md is Claude Code project configuration, not a tool-distribution mechanism.",
         ref='Domain 2, Task Statement 2.3 — Distribute tools appropriately across agents and configure tool choice.'),

    dict(task='2.2', domain='d2',
         q="One of your MCP tools runs a query that legitimately returns no matching records — an empty result, not a malfunction — and you want the agent to treat that differently from an actual error. How should a 'no results' outcome be distinguished from a failure?",
         options={
             'A': 'Return isError: true so the agent knows to retry the query',
             'B': 'Return a valid empty result — isError: false with resultCount: 0',
             'C': 'Throw an exception so the caller can signal "no data" upstream',
             'D': 'Return the string "search unavailable" as the tool result text instead',
         },
         answer='B',
         why='A successful query with zero matches is not an error; it should be reported as a valid empty result (isError: false) so the agent does not waste retries. The guide explicitly requires distinguishing access failures (which need retry decisions) from valid empty results. Marking it as an error triggers pointless recovery, and a generic "unavailable" string conflates a valid empty result with an access failure.',
         ref='Domain 2, Task Statement 2.2 — Implement structured error responses for MCP tools (also relates to Task Statement 5.3).'),

    dict(task='3.2', domain='d3',
         q='You want a custom /review slash command available to every developer automatically when they clone or pull the repository. Where should the command file live?',
         options={
             'A': 'In .claude/commands/ inside the project repository',
             'B': "In ~/.claude/commands/ in each developer's home directory",
             'C': 'In the root CLAUDE.md file, under a commands heading',
             'D': 'In a .claude/config.json file with a commands array',
         },
         answer='A',
         why='Project-scoped commands in.claude/commands/ are version-controlled and automatically available to everyone who clones or pulls the repo. ~/.claude/commands/ is personal and not shared, CLAUDE.md holds instructions and context rather than command definitions, and a config.json commands array is not a real Claude Code mechanism.',
         ref='Domain 3, Task Statement 3.2 — Create and configure custom slash commands and skills. Closely parallels Official Exam Guide Sample Question 4.'),

    dict(task='3.1', domain='d3',
         q='A new team member reports that Claude Code is not applying instructions that the rest of the team relies on. Those instructions were placed in ~/.claude/CLAUDE.md. What is the most likely cause?',
         options={
             'A': 'The instructions were written using the wrong Markdown heading syntax',
             'B': 'User-level ~/.claude/CLAUDE.md is personal and never version-controlled',
             'C': 'The project contains too many CLAUDE.md files for all of them to be loaded',
             'D': "The /memory command is disabled in the new member's configuration",
         },
         answer='B',
         why='Instructions in user-level ~/.claude/CLAUDE.md apply only to that user and are not shared through version control, so a teammate never receives them — this exact diagnosis scenario appears in Task Statement 3.1, and the fix is moving them to project-level configuration. Markdown syntax is not the issue, file count is unrelated, and /memory is a diagnostic command for inspecting loaded memory, not a cause.',
         ref='Domain 3, Task Statement 3.1 — Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization.'),

    dict(task='3.3', domain='d3',
         q='Your codebase has test files (e.g., Button.test.tsx) spread throughout many directories, and you want the same testing conventions applied whenever any test file is edited, regardless of location. What is the most maintainable approach?',
         options={
             'A': 'Put a separate CLAUDE.md in every subdirectory that contains test files',
             'B': 'Create a .claude/rules/ file whose frontmatter globs **/*.test.tsx',
             'C': 'Put every convention in root CLAUDE.md and let Claude infer which apply',
             'D': 'Create a skill and rely on Claude invoking it whenever a test is edited',
         },
         answer='B',
         why='Path-specific rules in.claude/rules/ with glob frontmatter (paths: ["**/*.test.tsx"]) load only when matching files are edited, applying conventions by file type regardless of directory — the guide\'s stated advantage over directory-bound CLAUDE.md files for conventions spanning the codebase. Per-directory files cannot easily cover scattered files, root-file inference is unreliable, and skills require invocation rather than automatic path-based loading.',
         ref='Domain 3, Task Statement 3.3 — Apply path-specific rules for conditional convention loading. Closely parallels Official Exam Guide Sample Question 6.'),

    dict(task='3.2', domain='d3',
         q="You're authoring a skill whose discovery step produces a lot of verbose output, and you don't want that output cluttering the main conversation's context. Which SKILL.md frontmatter option runs a skill in an isolated sub-agent context so its verbose output does not pollute the main conversation?",
         options={
             'A': 'disable-model-invocation: true',
             'B': 'context: fork',
             'C': 'argument-hint: "[module]"',
             'D': 'user-invocable: false',
         },
         answer='B',
         why='context: fork runs the skill in an isolated sub-agent context, preventing verbose or exploratory skill output (e.g., codebase analysis, brainstorming) from polluting the main conversation. disable-model-invocation prevents Claude from invoking the skill automatically, argument-hint prompts developers for required parameters, and user-invocable: false hides a skill from user invocation — none provide context isolation.',
         ref='Domain 3, Task Statement 3.2 — Create and configure custom slash commands and skills.'),

    dict(task='3.4', domain='d3',
         q='You are restructuring a monolithic application into microservices — dozens of files, service-boundary decisions, and multiple valid approaches. Which Claude Code mode should you use?',
         options={
             'A': 'Direct execution, making changes incrementally and letting boundaries emerge',
             'B': 'Plan mode, to explore the codebase and design an approach before making changes',
             'C': 'Direct execution driven by a single comprehensive instruction written in advance',
             'D': 'Start in direct execution and switch to plan mode only if complexity appears',
         },
         answer='B',
         why='Plan mode is designed for complex tasks involving large-scale changes, multiple valid approaches, and architectural decisions — exactly what monolith-to-microservices restructuring requires — and enables safe exploration and design before committing changes. Incremental direct execution risks costly rework when dependencies surface late, one-shot instructions assume the right structure is already known, and ignores that the complexity is already stated upfront.',
         ref='Domain 3, Task Statement 3.4 — Determine when to use plan mode vs direct execution. Closely parallels Official Exam Guide Sample Question 5.'),

    dict(task='3.4', domain='d3',
         q="You're deciding, task by task, whether to jump straight into changes or to explore and plan first. For which task is direct execution (not plan mode) the appropriate choice?",
         options={
             'A': 'Migrating a logging library across 45+ files in a large codebase',
             'B': 'Choosing between two integration approaches with different infrastructure',
             'C': 'Adding one date-validation conditional to a function with a clear trace',
             'D': 'Restructuring a monolith into independently deployable microservices',
         },
         answer='C',
         why="Direct execution suits simple, well-scoped changes — the guide's own examples include adding a date-validation conditional and single-file bug fixes with a clear stack trace. The other options involve large-scale changes, architectural decisions, or dozens of files, all cases where plan mode's explore-then-execute workflow prevents rework.",
         ref='Domain 3, Task Statement 3.4 — Determine when to use plan mode vs direct execution.'),

    dict(task='3.6', domain='d3',
         q='Your CI job runs claude "Analyze this pull request for security issues" and hangs indefinitely, waiting for interactive input. What is the correct fix?',
         options={
             'A': 'Add the -p (--print) flag so the command runs non-interactively',
             'B': 'Set the environment variable CLAUDE_HEADLESS=true in the CI job',
             'C': 'Redirect stdin from /dev/null so the prompt cannot block on input',
             'D': 'Add the --batch flag so the CLI processes the prompt and exits',
         },
         answer='A',
         why="The -p (or --print) flag is the documented way to run Claude Code in non-interactive mode: it processes the prompt, prints the result to stdout, and exits — exactly what CI/CD pipelines require. CLAUDE_HEADLESS and --batch are non-existent features, and redirecting stdin is a Unix workaround that does not properly address the CLI's design.",
         ref='Domain 3, Task Statement 3.6 — Integrate Claude Code into CI/CD pipelines. Closely parallels Official Exam Guide Sample Question 10.'),

    dict(task='3.6', domain='d3',
         q="In a CI pipeline you need Claude Code's review findings as machine-parseable output that can be posted as inline PR comments. Which flags should you use?",
         options={
             'A': '--output-format json together with --json-schema',
             'B': '--verbose together with --color for richer diagnostics',
             'C': '--resume with a named session to carry findings forward',
             'D': '--compact to condense the findings before printing',
         },
         answer='A',
         why='Task Statement 3.6 names --output-format json with --json-schema as the CLI flags for enforcing structured, machine-parseable output in CI contexts, which downstream scripts can post as inline PR comments. Verbose/color flags affect display, --resume is for session continuity, and /compact reduces context usage rather than shaping output.',
         ref='Domain 3, Task Statement 3.6 — Integrate Claude Code into CI/CD pipelines.'),

    dict(task='3.6', domain='d3',
         q="Your CI runs a Claude Code review on every push to a pull request, and reviewers are complaining that each re-run reposts the same comments they've already seen. When re-running an automated code review after new commits, how do you avoid duplicate PR comments?",
         options={
             'A': 'Delete all previously posted comments at the start of every run',
             'B': 'Pass prior findings in context and report only new or unaddressed ones',
             'C': 'Lower the model temperature so its output is more deterministic',
             'D': 'Run the review only on the first push and never re-run it after',
         },
         answer='B',
         why="Supplying the prior review findings in context and instructing Claude to report only new or still-unaddressed issues is the guide's prescribed way to avoid duplicate comments across review runs. Deleting comments loses history and review continuity, temperature does not address duplication, and skipping re-runs defeats iterative review.",
         ref='Domain 3, Task Statement 3.6 — Integrate Claude Code into CI/CD pipelines.'),

    dict(task='3.6', domain='d3',
         q="You're setting up a CI stage where Claude Code first generates code and, later in the pipeline, reviews it, and a colleague asks why the review shouldn't reuse the generating session. Why is it recommended that a code-review pass in CI run in a session independent from the one that generated the code?",
         options={
             'A': 'Independent sessions are cheaper to run than a single combined one',
             'B': 'The generating session is biased toward the decisions it already made',
             'C': 'The same session cannot emit structured JSON output a second time',
             'D': 'Independent sessions are allocated larger context windows by default in CI',
         },
         answer='B',
         why='A session that generated code carries the reasoning and assumptions behind it, making it less likely to challenge its own choices; an independent review instance without that context evaluates the result on its own terms and surfaces more issues. The guide calls this session context isolation. Cost, JSON output, and window size are not the reason.',
         ref='Domain 3, Task Statement 3.6 — Integrate Claude Code into CI/CD pipelines (also relates to Task Statement 4.6).'),

    dict(task='3.5', domain='d3',
         q='You keep getting inconsistent results from Claude when a prose description of a data transformation is interpreted differently each run. Which iterative-refinement technique most directly addresses this?',
         options={
             'A': 'Provide 2–3 concrete input/output examples of the transformation',
             'B': 'Increase max_tokens so the full transformation fits in the response',
             'C': 'Ask Claude to be "more careful" when applying the transformation',
             'D': 'Switch to plan mode so the transformation is designed before it runs',
         },
         answer='A',
         why='Task Statement 3.5 identifies concrete input/output examples as the most effective way to communicate expected transformations when prose descriptions are interpreted inconsistently — 2–3 targeted examples clarify the requirement. Raising max_tokens does not clarify intent, vague instructions like "be careful" are not actionable, and plan mode governs execution flow, not transformation clarity.',
         ref='Domain 3, Task Statement 3.5 — Apply iterative refinement techniques for progressive improvement.'),

    dict(task='3.5', domain='d3',
         q='You are about to build a caching layer in an unfamiliar domain and want to surface design considerations (invalidation strategy, failure modes) you may not have thought of before implementing. Which technique fits best?',
         options={
             'A': 'The interview pattern — let Claude ask you questions before implementing',
             'B': 'Write the implementation immediately and fix the issues that surface',
             'C': 'Run a batch job over the codebase to find comparable caching layers',
             'D': 'Set tool_choice: "any" so the design tools are always exercised',
         },
         answer='A',
         why="The interview pattern has Claude ask clarifying questions to surface design considerations the developer may not have anticipated — the guide's examples are precisely cache invalidation strategies and failure modes — before any code is written, reducing rework in unfamiliar domains. Coding first invites avoidable mistakes, batch processing is for latency-tolerant bulk work, and tool choice is unrelated.",
         ref='Domain 3, Task Statement 3.5 — Apply iterative refinement techniques for progressive improvement.'),

    dict(task='4.1', domain='d4',
         q='A CI code-review prompt says "be conservative and only report high-confidence findings," but false positives remain high and developers are losing trust. What change most reliably improves precision?',
         options={
             'A': 'Repeat "be conservative" more emphatically and in several places',
             'B': 'Replace the vague guidance with explicit categorical criteria for flagging',
             'C': 'Ask the model to self-rate confidence 1–10 and drop anything below 8',
             'D': 'Lower max_tokens to force shorter, more selective review output',
         },
         answer='B',
         why='Task Statement 4.1 states that general instructions like "be conservative" or "only report high-confidence findings" fail to improve precision compared to specific categorical criteria that define what qualifies as an issue. Emphasis does not add signal, self-reported confidence is poorly calibrated, and shorter output does not improve precision. High false-positive rates erode developer trust in accurate categories too.',
         ref='Domain 4, Task Statement 4.1 — Design prompts with explicit criteria to improve precision and reduce false positives.'),

    dict(task='4.2', domain='d4',
         q="You've written a detailed, carefully worded prose spec for the output you want, but the model's formatting still varies from run to run. Which technique is most effective for getting consistently formatted, actionable output when detailed written instructions alone still produce inconsistent results?",
         options={
             'A': 'Few-shot examples showing the exact output shape you want returned',
             'B': 'Increasing the temperature to encourage more varied phrasing',
             'C': 'A longer system prompt that restates the formatting rules three times',
             'D': 'Forcing tool_choice: "none" so the model replies in prose only',
         },
         answer='A',
         why='Task Statement 4.2 identifies few-shot examples as the most effective technique for achieving consistently formatted, actionable output when detailed instructions alone produce inconsistent results — the guide\'s example format is exactly location, issue, severity, and suggested fix. Higher temperature increases variability, restating rules rarely fixes format drift, and tool_choice: "none" blocks tool use and is irrelevant.',
         ref='Domain 4, Task Statement 4.2 — Apply few-shot prompting to improve output consistency and quality.'),

    dict(task='4.3', domain='d4',
         q='You use tool_use with a strict JSON schema for invoice extraction. A response is perfectly valid JSON, yet the line items do not sum to the stated total. What does this illustrate?',
         options={
             'A': 'The schema was not strict enough for the output to count as valid JSON',
             'B': 'Strict schemas eliminate syntax errors but not semantic ones',
             'C': 'Tool use is the wrong approach for structured document extraction',
             'D': 'The model ran out of output tokens partway through the line items',
         },
         answer='B',
         why="Tool use with a JSON schema guarantees structurally valid, schema-compliant output but does not prevent semantic errors — the guide's own examples are line items that don't sum to the total and values placed in wrong fields. It is not a validity failure, tool use remains the most reliable structured-output approach, and there is no evidence of truncation.",
         ref='Domain 4, Task Statement 4.3 — Enforce structured output using tool use and JSON schemas.'),

    dict(task='4.4', domain='d4',
         q='An extraction pipeline outputs JSON where line items sometimes do not match the stated total. What is the best architectural way to catch this semantic error?',
         options={
             'A': 'Automatically rewrite the line items so that they sum to the stated total',
             'B': 'Extract calculated_total beside stated_total and flag any mismatch',
             'C': 'Add more few-shot examples demonstrating correct invoice arithmetic',
             'D': 'Add a second LLM pass that silently reconciles the conflicting math',
         },
         answer='B',
         why='Extracting both a stated and a calculated value and flagging discrepancies is the self-correction validation flow named in Task Statement 4.4 (extracting "calculated_total" alongside "stated_total" and adding conflict flags); it detects inconsistencies deterministically without altering source data. Rewriting values can corrupt the record, few-shot arithmetic cannot guarantee consistency, and silent reconciliation hides genuine source conflicts.',
         ref='Domain 4, Task Statement 4.4 — Implement validation, retry, and feedback loops for extraction quality.'),

    dict(task='4.3', domain='d4',
         q='A document sometimes lacks a "shipping address" field, yet the schema currently marks it as a required string. The model fabricates addresses when the field is absent. What is the best schema fix?',
         options={
             'A': 'Keep the field required and add a few-shot example showing an absent case',
             'B': 'Make the field nullable and not required, so it can return null',
             'C': 'Remove the shipping-address field from the extraction schema entirely',
             'D': 'Set tool_choice: "any" so the model picks a more suitable schema',
         },
         answer='B',
         why='A required string with no source value pushes the model to invent data to satisfy the schema; Task Statement 4.3 prescribes designing fields as optional/nullable when source documents may not contain the information, giving the model a legitimate way to signal absence. A few-shot example does not remove the structural pressure to fabricate, removing the field loses the data when present, and tool choice is unrelated.',
         ref='Domain 4, Task Statement 4.3 — Enforce structured output using tool use and JSON schemas.'),

    dict(task='4.4', domain='d4',
         q='Your extraction pipeline automatically retries whenever validation fails, appending the validation error to the prompt so the model can correct itself. When you retry an extraction with error feedback, in which situation will retrying be ineffective?',
         options={
             'A': 'When the output had a format mismatch you can describe in the error',
             'B': 'When a structural/schema error occurred that the model can correct',
             'C': 'When the required information is simply absent from the source document',
             'D': 'When the returned JSON had a trailing comma the parser rejected',
         },
         answer='C',
         why='Retry-with-error-feedback helps with format and structural errors the model can fix, but the guide states retries are ineffective when the required information is simply absent from the source — no feedback can conjure missing data. Format mismatches, correctable structural errors, and syntax issues are all cases where a feedback-guided retry can succeed.',
         ref='Domain 4, Task Statement 4.4 — Implement validation, retry, and feedback loops for extraction quality.'),

    dict(task='4.5', domain='d4',
         q='Your team wants to cut API costs by moving two workflows to the Message Batches API: (1) a blocking pre-merge check developers wait on, and (2) an overnight technical-debt report. How should you proceed?',
         options={
             'A': 'Move both workflows to the Batches API for the maximum possible cost savings',
             'B': 'Batch only the overnight report; keep the pre-merge check synchronous',
             'C': 'Keep both synchronous to avoid result-ordering issues between them',
             'D': 'Move both to batch, with a real-time fallback if a batch runs long',
         },
         answer='B',
         why='The Message Batches API offers 50% cost savings but has a processing window of up to 24 hours with no guaranteed latency SLA, making it unsuitable for blocking pre-merge checks yet ideal for overnight, latency-tolerant jobs. Batching the blocking check breaks the developer wait experience — "often faster" completion is not a guarantee — and results are correlated via custom_id, so ordering is not a blocker.',
         ref='Domain 4, Task Statement 4.5 — Design efficient batch processing strategies. Closely parallels Official Exam Guide Sample Question 11.'),

    dict(task='4.5', domain='d4',
         q="Documents arrive continuously and results must be guaranteed in under 30 hours of each document's arrival. You use the Message Batches API, whose processing window is up to 24 hours. Which submission schedule guarantees the SLA while minimizing submission overhead?",
         options={
             'A': 'Submit batches every 4 hours',
             'B': 'Submit batches every 6 hours',
             'C': 'Submit one large batch at the end of each day',
             'D': 'Use the synchronous API for all documents instead',
         },
         answer='A',
         why='Worst-case latency equals the submission interval plus the 24-hour processing window. A 4-hour interval yields a 28-hour worst case, guaranteeing the sub-30-hour SLA with margin — the exact calculation the exam guide cites for this skill (4-hour windows to guarantee a 30-hour SLA with 24-hour batch processing). A 6-hour interval gives a 30-hour worst case with zero margin, so it cannot guarantee completion in under 30 hours once retrieval and polling are included. A daily batch can reach 48 hours, and going fully synchronous forfeits the 50% batch savings unnecessarily.',
         ref='Domain 4, Task Statement 4.5 — Design efficient batch processing strategies.'),

    dict(task='4.5', domain='d4',
         q='Your team is evaluating the Message Batches API to cut costs and wants to confirm how it actually behaves before committing to it. Which statement about the Message Batches API is accurate?',
         options={
             'A': 'It supports multi-turn tool calling, executing tools mid-request',
             'B': 'It provides a guaranteed sub-hour latency SLA for every submission',
             'C': 'It offers 50% savings, a 24-hour window, and custom_id correlation',
             'D': 'It is the recommended choice for blocking, real-time review workflows',
         },
         answer='C',
         why="The exam guide's appendix summarizes the Message Batches API as 50% cost savings, an up-to-24-hour processing window, custom_id for request/response correlation, polling for completion, and no multi-turn tool calling support. It cannot execute tools mid-request and return results, has no guaranteed latency SLA, and is inappropriate for blocking real-time workflows.",
         ref='Domain 4, Task Statement 4.5 — Design efficient batch processing strategies.'),

    dict(task='4.6', domain='d4',
         q='A pull request modifies 14 files, and a single-pass review produces inconsistent depth, misses obvious bugs, and even flags a pattern in one file while approving identical code in another. What restructuring best addresses this?',
         options={
             'A': 'Split it into per-file passes for local issues, then a cross-file pass',
             'B': 'Require developers to break the PR into submissions of 3–4 files each',
             'C': 'Switch to a model whose context window fits all 14 files in one pass',
             'D': 'Run three full-PR passes and report only issues appearing in at least two',
         },
         answer='A',
         why="The inconsistency stems from attention dilution when many files are analyzed at once; per-file passes for local issues plus a separate cross-file integration pass restore consistent depth — the guide's prescribed multi-pass review structure. Forcing smaller PRs shifts burden to developers, a bigger context window does not fix attention quality, and consensus voting suppresses real bugs caught only intermittently.",
         ref='Domain 4, Task Statement 4.6 — Design multi-instance and multi-pass review architectures. Closely parallels Official Exam Guide Sample Question 12.'),

    dict(task='4.6', domain='d4',
         q="You're deciding how to review AI-generated code and wondering whether the same session that wrote it can simply review its own work. Why is an independent Claude instance generally better than self-review or extended thinking for catching subtle issues in generated code?",
         options={
             'A': 'Independent instances are always faster than a single combined pass',
             'B': 'The generating instance is biased toward the decisions it just made',
             'C': 'Extended thinking is disabled during any review pass, so it cannot help',
             'D': 'Independent instances are given larger context windows for review',
         },
         answer='B',
         why='Task Statement 4.6 states that a model retains reasoning context from generation, making it less likely to question its own decisions in the same session, and that independent review instances are more effective at catching subtle issues than self-review instructions or extended thinking. Speed, a false claim about extended thinking, and window size are not the underlying reason.',
         ref='Domain 4, Task Statement 4.6 — Design multi-instance and multi-pass review architectures.'),

    dict(task='4.3', domain='d4',
         q="You're designing the output schema for a classifier whose categories aren't fixed — new categories may appear over time, and you don't want the model forced to jam a novel case into an existing bucket. For this extensible categorization field, which schema design best avoids forced misclassification?",
         options={
             'A': 'A free-text string field with no constraints on its contents',
             'B': 'An enum restricted to a fixed, closed set of known category values',
             'C': 'An enum with an "other" value plus a companion detail string',
             'D': 'A boolean field indicating whether the category is a known one',
         },
         answer='C',
         why='An enum with an "other" escape hatch plus a detail field — a pattern the guide names explicitly, alongside "unclear" values for ambiguous cases — lets the model handle unexpected categories without being forced into the closest-but-wrong option, while still constraining known values. Free text loses structure, a closed enum forces misclassification of novel cases, and a boolean cannot represent categories.',
         ref='Domain 4, Task Statement 4.3 — Enforce structured output using tool use and JSON schemas.'),

    dict(task='5.1', domain='d5',
         q='In a long customer-support conversation, progressive summarization is compressing exact figures (refund amounts, order numbers, dates) into vague phrases, causing errors. What is the recommended mitigation?',
         options={
             'A': 'Summarize even more aggressively so fewer tokens are spent on history',
             'B': 'Keep a persistent case-facts block in every prompt, outside the summary',
             'C': 'Disable summarization entirely and always send the full raw transcript instead',
             'D': 'Route the conversation to a human the first time summarization runs',
         },
         answer='B',
         why='Task Statement 5.1 prescribes extracting transactional facts (amounts, dates, order numbers, statuses) into a persistent case-facts block included in each prompt outside the summarized history, preserving precision without keeping the entire transcript. More aggressive summarization worsens the loss, sending the full transcript is token-inefficient and will eventually overflow, and immediate escalation is unwarranted.',
         ref='Domain 5, Task Statement 5.1 — Manage conversation context to preserve critical information across long interactions.'),

    dict(task='5.1', domain='d5',
         q='Findings in the middle of a long aggregated input are being omitted, while those at the start and end are reliably used. This is the "lost in the middle" effect. Which mitigation is recommended?',
         options={
             'A': 'Put key-findings summaries first and use explicit section headers',
             'B': 'Randomly shuffle the aggregated content on each request to the model',
             'C': 'Increase the temperature so the model attends more broadly to the input',
             'D': 'Rely on a larger context window alone to bring the middle into view',
         },
         answer='A',
         why='Models process information at the beginning and end of long inputs most reliably and may omit middle-section findings — the lost-in-the-middle effect documented in long-context research and named in Task Statement 5.1. The prescribed mitigation is placing key-findings summaries at the beginning and organizing detailed results with explicit section headers. Shuffling is not a reliable fix, temperature does not change positional attention, and a larger window alone does not solve attention quality.',
         ref='Domain 5, Task Statement 5.1 — Manage conversation context to preserve critical information across long interactions.'),

    dict(task='5.2', domain='d5',
         q='Mid-conversation, a customer explicitly demands to speak with a human agent about an issue that is actually straightforward and that the agent could resolve on its own. What is the correct behavior?',
         options={
             'A': 'Refuse, and insist on attempting an autonomous resolution first',
             'B': 'Honor the request for a human immediately, without investigating first',
             'C': 'Run sentiment analysis to decide whether the request is genuine',
             'D': 'Ask the customer to justify why they would rather speak to a human',
         },
         answer='B',
         why="An explicit customer request for a human is a valid escalation trigger that Task Statement 5.2 says should be honored immediately, without first attempting investigation — even when the issue seems simple. Refusing ignores a clear signal, sentiment analysis is an unreliable proxy, and demanding justification creates friction and disregards the customer's stated preference.",
         ref='Domain 5, Task Statement 5.2 — Design effective escalation and ambiguity resolution patterns.'),

    dict(task='5.2', domain='d5',
         q="You're writing the escalation rules for a support agent and want to avoid triggers that look useful but actually mislead. Which of the following is an unreliable proxy for deciding when an agent should escalate a case?",
         options={
             'A': 'The customer explicitly asks to be transferred to a human agent',
             'B': "The policy is silent or ambiguous on the customer's specific request",
             'C': "The agent's self-reported confidence score or the detected sentiment",
             'D': 'The agent cannot make meaningful progress on resolving the case',
         },
         answer='C',
         why='Task Statement 5.2 states that sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity — an agent is often confidently wrong precisely on hard cases. Explicit human requests, policy gaps or ambiguity, and inability to make meaningful progress are the appropriate, reliable escalation triggers.',
         ref='Domain 5, Task Statement 5.2 — Design effective escalation and ambiguity resolution patterns.'),

    dict(task='5.3', domain='d5',
         q='In a multi-agent research run, a web-search subagent times out partway through, and the coordinator needs enough information to decide whether to retry, try a different approach, or proceed with what it has. Which error-propagation approach best enables the coordinator to recover intelligently?',
         options={
             'A': 'Return structured context: failure type, attempted query, partial results',
             'B': 'Retry silently with backoff, then return a generic "search unavailable"',
             'C': 'Catch the timeout and return an empty result marked as a success',
             'D': 'Propagate the exception to a top-level handler that terminates the workflow',
         },
         answer='A',
         why='Structured error context — failure type, attempted query, partial results, and alternative approaches — gives the coordinator the information to decide whether to retry with a modified query, try an alternative, or proceed with partial results. A generic status hides valuable context, marking failure as success suppresses the error and risks silently incomplete research, and terminating the workflow is unnecessary when recovery strategies could succeed.',
         ref='Domain 5, Task Statement 5.3 — Implement error propagation strategies across multi-agent systems. Closely parallels Official Exam Guide Sample Question 8.'),

    dict(task='5.6', domain='d5',
         q='While synthesizing a report from several sources, the system finds two credible sources reporting different statistics for the same metric, and it must decide how to present the discrepancy. How should the system handle this?',
         options={
             'A': 'Arbitrarily pick one of the two values and drop the other entirely',
             'B': 'Average the two values silently and present a single figure',
             'C': 'Preserve both with source attribution and dates, annotating the conflict',
             'D': 'Discard both figures and report that no data could be found',
         },
         answer='C',
         why='Task Statement 5.6 prescribes annotating conflicting statistics with source attribution rather than arbitrarily selecting one value, and requiring publication or collection dates so temporal differences are not misinterpreted as contradictions. Arbitrarily choosing, silently averaging, or discarding both destroy provenance and mislead the reader.',
         ref='Domain 5, Task Statement 5.6 — Preserve information provenance and handle uncertainty in multi-source synthesis.'),

]


def main():
    banner("Mock Exam Bank", "60 blueprint-aligned questions — verified, exam-style")
    note("These power the console's 60-question Mock Exam (M1..M60). Study aid, not official items.")
    for i, q in enumerate(MOCK_BANK, 1):
        h1(f"M{i} — Task {q['task']} ({q['domain'].upper()})")
        note(q["q"])
        print()
        for k in ("A", "B", "C", "D"):
            kv(f"  {k}", q["options"][k])
        right(f"Answer: {q['answer']}")
        note("Why: " + q["why"])
        note("Reference: " + q["ref"])
    rule()
    tip("Answer is the simplest mechanism that fixes the root cause; distractors over-prompt, "
        "over-build, or invent features. Use the Reference line to target your weakest task.")


if __name__ == "__main__":
    main()
