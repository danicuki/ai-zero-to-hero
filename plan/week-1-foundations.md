# Week 1 — Foundations & Fluency

**Goal:** rebuild rock-solid mental models of how LLMs work (tokens → attention → sampling → context → cost), and become *dangerous* with the two tools you'll live in: the Claude API and Claude Code. By Friday you can reason about any LLM behavior from first principles and estimate its cost.

**Maps to role:** prompt & behaviour engineering, "not just calling a model API", Python fluency.

> Format of each day: **Objective → Theory → 🔨 Build → Deliverable → Definition of Done → ⭐ Stretch**. Copy `daily-log/TEMPLATE.md` to `daily-log/day-NN.md` before you start.

---

## Day 0 — Setup & baseline (½ day)

**Objective:** zero friction for the next 30 days, and an honest baseline.

- [ ] Accounts & keys: **Anthropic API**, OpenAI (for comparison), a **Hugging Face** account, and one GPU option (Google Colab / Modal / Runpod). Put keys in a `.env`, never commit them.
- [ ] Python env: install **`uv`** (fast package manager). `uv init`, Python 3.12, and a `sandbox/` scratch dir.
- [ ] Install/upgrade **Claude Code**. Confirm you can run it in this repo.
- [ ] Local models: install **Ollama**, pull `llama3.2` and `qwen2.5:7b`. Confirm `ollama run` works.
- [ ] If Python is rusty: 90-min speed-refresh — type hints, `dataclasses`, `async`/`await`, `httpx`, `pydantic`. You know how to program; just reload the idioms.
- [ ] Fill **Day-0 column** of [`progress/skills-matrix.md`](../progress/skills-matrix.md). Be brutally honest — low scores now are the point.

**DoD:** `python -c "import anthropic; print('ok')"` works; matrix Day-0 committed; first green square pushed.

---

## Day 1 — Tokens, tokenization & the cost of everything

**Objective:** internalize that an LLM sees *tokens*, not text — and that tokens are money and latency.

**Theory (~1.5h):** Byte-Pair Encoding; why tokenization causes "how many r's in strawberry" failures; context windows; the difference between input/output/cached tokens and their prices. Read: Karpathy "Let's build the GPT Tokenizer" (first half), Anthropic pricing & token-counting docs.

**🔨 Build — `toktool` (a token/cost explorer CLI):**
- Takes text or a file, shows the token count for Claude (via the token-counting API) and for a local tokenizer (`tiktoken` / HF `tokenizers`), and visualizes the actual token boundaries (colorized).
- Prints estimated cost for a given model at N input + M output tokens, including a **prompt-caching** scenario.
- A `--compare` mode showing how the same text tokenizes differently across 2–3 tokenizers.

**Deliverable:** `projects/toktool/` + a short README with 3 surprising things you learned about tokenization.
**DoD:** you can answer, for any prompt, "how many tokens and how many cents is this?" in under 10 seconds.
**⭐ Stretch:** implement BPE training yourself on a small corpus (merge loop) so you've *built* a tokenizer once.

---

## Day 2 — How a transformer actually works

**Objective:** demystify attention deeply enough to make architecture and cost decisions (why context is O(n²), why KV-cache matters, why long context is expensive).

**Theory (~2h):** Read/skim **"Attention Is All You Need"**; watch Karpathy "Let's build GPT: from scratch" (nanoGPT). Focus on: self-attention, Q/K/V, positional encodings, multi-head, the residual stream, why decoder-only, KV-cache, and why inference is memory-bandwidth bound.

**🔨 Build — nano-GPT, by your own hands:**
- Follow Karpathy's build but **type every line yourself** and add comments explaining *why* in your own words. Train a tiny char-level model on a text you care about (your own writing / poems / a codebase).
- Then **ablate**: remove positional encodings, shrink heads to 1, and observe what breaks. Write down what each component *does*.

**Deliverable:** `projects/nanogpt/` with your annotated model + an `ABLATIONS.md`.
**DoD:** you can draw the transformer forward pass on a whiteboard and explain KV-cache to a non-ML engineer.
**⭐ Stretch:** implement a rudimentary KV-cache in your nano-GPT and measure the speedup.

---

## Day 3 — Sampling, decoding & why models "hallucinate"

**Objective:** understand what happens *after* the forward pass — logits → probabilities → tokens — and how temperature/top-p/penalties shape behavior.

**Theory (~1h):** temperature, top-k, top-p/nucleus, repetition penalty, greedy vs. sampling, logprobs; why hallucination is the default behavior of a next-token predictor, and what actually reduces it (grounding, not scolding).

**🔨 Build — a decoding playground:**
- Using logprobs from an API (or your nano-GPT), build a small tool that shows, for a given prompt, the **top-k next tokens with probabilities**, and lets you sweep temperature/top-p and watch the distribution change.
- Reproduce a hallucination on purpose, then kill it three ways (lower temp, grounding context, asking for "I don't know"). Log which worked and why.

**Deliverable:** `projects/decoding-lab/` + notes on 3 anti-hallucination techniques you validated.
**DoD:** you can explain to a PM *why* the model made something up and what to change.

---

## Day 4 — The Claude API, deeply (the real workhorse)

**Objective:** move from "I call a model" to "I command the model": messages, system prompts, streaming, **tool use**, **structured outputs**, **extended thinking**, **prompt caching**, stop reasons, token accounting.

**Theory (~1h):** Read the Anthropic Messages API, tool use, and prompt-caching docs end to end. Note the exact shapes of tool-use / tool-result blocks — you'll rebuild these next week.

**🔨 Build — `askctl`, a proper API client library (no SDK sugar hidden from you):**
- Wrap the Messages API with: streaming to the terminal, a **tool-use loop** (define 2 tools — a calculator and a `get_weather` mock — and handle the request/result round-trip yourself), **structured output** via a Pydantic schema, and **prompt caching** on a large system prompt.
- Instrument it: every call logs input/output/cache tokens and computed cost to a local `runs.jsonl`.

**Deliverable:** `projects/askctl/` — a reusable client you'll build on all month.
**DoD:** you've completed a full tool-use round-trip *by hand*, and your logs show a cache hit reducing cost on a repeat call.
**⭐ Stretch:** add the same interface for OpenAI and a local Ollama model behind one abstraction (a `Provider` protocol). This becomes your multi-provider layer for later.

---

## Day 5 — Claude Code mastery, part 1 (stop leaving power on the table)

**Objective:** exploit the tool you already use daily. Most people use 20% of it.

**Theory/hands-on (~2h):** work through the Claude Code docs deliberately, trying each feature in *this* repo:
- **Plan mode**, thinking, and when to use each.
- **Custom slash commands** and **skills** — write one that scaffolds a new daily-log entry.
- **Subagents** — spawn an Explore agent to map a codebase; understand context isolation.
- **Hooks** — add a hook that runs your linter/formatter on stop.
- **`CLAUDE.md`** memory & project config; `settings.json` permissions.
- **Headless / SDK mode** (`claude -p`) for scripting.

**🔨 Build — automate your own workflow:**
- A custom **skill** or slash command that starts your day: creates `daily-log/day-NN.md` from the template, opens the day's plan, and prints today's objective.
- A **hook** that blocks a commit if the daily log wasn't updated (accountability as code).

**Deliverable:** `.claude/` commands/skills/hooks committed + a `resources/claude-code-cheatsheet.md` in your own words.
**DoD:** you can list 8 Claude Code features you weren't using a week ago, and 3 are now part of your routine.

---

## Day 6 — Claude Code mastery, part 2 + MCP first contact

**Objective:** understand **MCP** (Model Context Protocol) as a user before you build servers next week; wire Claude Code to real tools.

**Theory (~1h):** What MCP is and why it matters (a universal protocol for tools/resources/prompts); the difference between MCP servers, tools, and resources; transport (stdio vs HTTP).

**🔨 Build — connect and use MCP:**
- Add 2 existing MCP servers to Claude Code (e.g. a filesystem server and a GitHub or Playwright server). Use them to complete a real task in this repo (e.g. have Claude drive a browser or query GitHub).
- Write `resources/mcp-notes.md`: how a tool call flows from the model → MCP client → server → back.

**Deliverable:** working MCP config + notes.
**DoD:** you've completed a task Claude *could not do without a tool*, and you understand the round-trip. (You'll build your own server on Day 10–11.)
**⭐ Stretch:** read the source of one small open-source MCP server to see how thin it really is.

---

## Day 7 — Prompt & behaviour engineering + Week 1 retro

**Objective:** treat prompting as engineering (versioned, tested, measured), not vibes — this is a named responsibility of the role.

**Theory (~1h):** Anthropic prompt engineering guide; structured/XML prompting; role prompting; few-shot vs zero-shot; chain-of-thought vs extended thinking; when to decompose vs. one-shot; prompt injection basics (preview of safety week).

**🔨 Build — a prompt harness with a mini eval (seed of Week 3):**
- Pick a real task (e.g. "extract structured data from a messy invoice-like text" — foreshadows the doc-extraction track). Write 3 prompt variants.
- Build a tiny runner that executes all variants over ~10 hand-made examples and scores them against expected outputs (exact match / field-level). Produce a comparison table.

**Deliverable:** `projects/prompt-harness/` with a versioned prompts file + results table.
**DoD:** you picked a winning prompt *because the numbers said so*, not because it "felt better".

### 🔁 Week 1 retro (do this, don't skip)
- Update the **skills matrix** mid-point notes.
- Write `daily-log/week-1-retro.md`: what clicked, what's still fuzzy, what to carry forward.
- Confirm: 8 green squares, `toktool`, `nanogpt`, `decoding-lab`, `askctl`, `prompt-harness` all pushed.
- **Gut check:** you should now feel *fluent*, not fluent-ish, about how LLMs work and how to drive them. If not, flag the specific gap for Week 2 and spend a stretch evening on it.
