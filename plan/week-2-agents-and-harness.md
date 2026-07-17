# Week 2 — Agents & the Harness

**Goal:** build an **agent harness from scratch** — the exact artifact the target role is built around — then understand real ones by rebuilding their core. By Friday you have your own mini coding agent and can explain, defend, and debug every design choice inside an agent runtime.

**Maps to role:** *"Build and maintain the agent harness — the core runtime that orchestrates LLM calls, tool use, context construction, memory and guardrails — and make it reliable in production."* This is the single most important week for the role.

**Prereq:** `askctl` from Day 4 (your instrumented API client).

---

## Day 8 — The agent loop from zero

**Objective:** understand that an "agent" is a `while` loop around an LLM with tools. No framework. No magic.

**Theory (~1h):** ReAct (reason + act); the agent loop (observe → think → act → observe); the tool-use protocol you learned Day 4; stop conditions; the difference between a chatbot, a workflow, and an agent.

**🔨 Build — `miniagent` v0:**
- A pure-Python agent loop over `askctl`: system prompt → model proposes a tool call → you execute it → feed the result back → repeat until the model returns a final answer.
- Start with 3 tools: `read_file`, `list_dir`, `run_python` (sandboxed). No framework allowed.
- Add a hard **max-iterations** guard and a per-run **token/cost budget** that halts the loop.

**Deliverable:** `projects/miniagent/` running a task like "find the largest file in this repo and summarize it".
**DoD:** you wrote the loop yourself and can point to the exact line where a tool result re-enters the context.
**⭐ Stretch:** add streaming so you *watch* the agent think and act in real time.

---

## Day 9 — Context construction & memory

**Objective:** context engineering is where agents live or die (and where tokens are won or lost). Build real memory.

**Theory (~1.5h):** context window budgeting; the "context rot" problem; short-term (conversation) vs long-term (persistent) memory; summarization/compaction; retrieval-as-memory; scratchpads/working memory; how Claude Code and others manage a shrinking window.

**🔨 Build — give `miniagent` a memory system:**
- **Compaction:** when the conversation nears a token budget, summarize old turns into a compact memory and continue (measure tokens before/after).
- **Persistent memory:** a `memory/` store the agent can write facts to and recall across sessions (mirrors how good agents remember).
- **Working scratchpad:** a tool the agent uses to jot intermediate results instead of holding them in context.

**Deliverable:** memory subsystem + a demo where the agent survives a conversation longer than its raw context window.
**DoD:** you can show a graph of context tokens staying bounded while the task runs long.

---

## Day 10 — Tool design, guardrails & reliability

**Objective:** production agents fail on tools and edge cases, not on the model. Engineer for failure ("handling failure, state and reliability — not just calling a model API").

**Theory (~1h):** good tool schemas (names, descriptions, params the model won't misuse); idempotency; validation; retries with backoff; timeouts; the difference between a *recoverable* tool error (feed back to model) and a *fatal* one (halt); guardrails (input/output validation, allow-lists, human-in-the-loop for dangerous actions).

**🔨 Build — harden `miniagent`:**
- Wrap every tool with: input validation (Pydantic), timeouts, retries, and structured error results the model can reason about and recover from.
- Add a **guardrail layer:** a dangerous-action gate (e.g. any shell/write action requires confirmation), and output validation before a tool result is trusted.
- Inject faults (make a tool randomly fail) and prove the agent recovers.

**Deliverable:** a `tools/` framework with a `Tool` base class + fault-injection test.
**DoD:** with a tool failing 30% of the time, your agent still completes the task or fails *gracefully and loudly*.

---

## Day 11 — Build your own MCP server

**Objective:** go from MCP *user* (Week 1) to MCP *author*. This is explicitly in the role's stack.

**Theory (~1h):** MCP server anatomy — tools, resources, prompts; the stdio/HTTP transports; how a client discovers and calls capabilities.

**🔨 Build — an MCP server for a real domain:**
- Build an MCP server (Python SDK) exposing tools over a real dataset — e.g. a **finance/accounting** toy: `list_invoices`, `get_invoice`, `search_transactions`, `flag_anomaly` over a local SQLite of fake accounting data (leans into the target domain).
- Connect it to **both** Claude Code **and** your `miniagent`. Same server, two clients — that's the point of the protocol.

**Deliverable:** `projects/mcp-ledger/` server + a demo of an agent answering "which invoices look anomalous this month?".
**DoD:** your own agent and Claude Code both call your server successfully.
**⭐ Stretch:** add an MCP **resource** and a **prompt** template, not just tools.

---

## Day 12 — Multi-agent orchestration

**Objective:** when to split into multiple agents, and the patterns for coordinating them (orchestrator/worker, planner/executor, debate, routing).

**Theory (~1.5h):** multi-agent patterns and their costs (context isolation vs. coordination overhead); orchestrator-worker; planner→executor→critic; parallel sub-agents (like Claude Code's subagents); when multi-agent is *worse* than one good agent. Read Anthropic's "Building effective agents".

**🔨 Build — a multi-agent workflow:**
- Turn `miniagent` into an **orchestrator** that spawns specialized sub-agents (each with its own context and tools) and merges their results — e.g. a "research a topic" task fanned out to 3 workers + a synthesizer.
- Measure: does multi-agent actually beat a single agent here on quality *and* cost? Record the honest answer.

**Deliverable:** `projects/miniagent/` orchestrator mode + a `WHEN-MULTIAGENT.md` with your findings.
**DoD:** you can state, from data, when multi-agent paid off and when it just burned tokens.

---

## Day 13 — Reverse-engineer a real harness (understand what you run)

**Objective:** close the "I use an open-source agent but don't understand its internals" gap directly, by reading real source with your now-trained eyes.

**Theory/hands-on (~3h):** pick one open-source agent runtime you actually use or admire (e.g. the open-source coding agent you run, or a well-known one) and **read its core loop**. Map its code onto the primitives you built: where's *its* agent loop? tool protocol? context/compaction? guardrails? memory? Write it up.

**🔨 Build — a comparison + a contribution:**
- Write `projects/harness-teardown.md`: a side-by-side of your `miniagent` vs the real one — what they do the same, what the real one does better, and *why*.
- Bonus: fix a small bug or open a well-scoped issue/PR on that project. Nothing teaches internals like touching them.

**Deliverable:** the teardown doc (+ optional PR link).
**DoD:** you can explain the internals of a tool you previously used as a black box, and name 3 design decisions and their trade-offs.

---

## Day 14 — Frameworks, in perspective + Week 2 retro

**Objective:** *now* meet the frameworks — from a position of understanding, so they're conveniences, not crutches.

**Theory (~1.5h):** survey **LangGraph** (graph/state-machine agents), **PydanticAI**, and the **Claude Agent SDK**. Map their abstractions onto what you built by hand (nodes = your loop steps, state = your context, etc.).

**🔨 Build — port + judge:**
- Reimplement one of your `miniagent` tasks in **LangGraph** (or PydanticAI). Then write an honest verdict: what the framework bought you, what it hid, and when you'd choose raw vs. framework in production.

**Deliverable:** `projects/framework-port/` + a `VERDICT.md`.
**DoD:** you have a defensible opinion on build-vs-framework for agents, grounded in having done both.

### 🔁 Week 2 retro
- Update the skills matrix (agent/harness rows should be jumping).
- `daily-log/week-2-retro.md`: the harness diagram you can now draw from memory; what surprised you in the real-harness teardown.
- **Gut check:** could you sit in an interview and whiteboard "how would you build an agent harness for production"? If yes, this week worked. If shaky, list the fuzzy parts and revisit before Week 3.
