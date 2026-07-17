# Provider strategy — which model, from whom, and why

> **TL;DR:** Pick a **primary** provider for ~90% of your calls (cost & friction), but stay **multi-provider by design**. Provider-agnosticism is a *skill this role explicitly wants* ("model providers", plural), not a nice-to-have. The Day-4 `Provider` protocol is how you get it cheaply.

This program is **provider-agnostic by design**. Every concept — the agent loop, tool use, context construction, RAG, evals, SFT/DPO, serving — transfers across providers. Only the SDK surface changes.

---

## Choosing your primary

| If you have... | Go primary with | Why |
|---|---|---|
| Google credits / GDE / GCP fluency | **Gemini + Gemma** | Covers the whole curriculum end-to-end (see below) |
| Anthropic credits | **Claude** | Best-in-class tool use; the repo's original default |
| A strong GPU / sovereignty focus | **Local (Gemma/Qwen via Ollama)** | Cheapest to iterate; hardest mode; great for W4 |

**Whatever you choose, do not go single-provider.** Reasons below.

---

## The Gemini-first path (fully supported)

Google is one of the few ecosystems that covers **every week** of this program without leaving it:

| Week / Day | Need | Google path |
|---|---|---|
| W1 D1 | Tokenization & cost | `count_tokens` API; Gemini pricing docs |
| W1 D4 | Tool use, structured output, streaming, caching | Gemini **function calling**, `response_schema` (structured output), **implicit context caching** (on by default for 2.5+, up to ~90% input savings) |
| W1 D4 | Thinking | Gemini thinking / thinking budgets |
| W2 | MCP, agents | Gemini SDK supports **MCP**; the agent loop is yours anyway |
| W3 D15 | Embeddings | `gemini-embedding` |
| W3 D19–20 | Eval runs at volume | **Batch API (50% off)**; **Flash-Lite** for cheap judge/synthetic passes |
| W3 | Long-context vs RAG experiment | 1M-token context — run the "just stuff it" baseline against your RAG (see below) |
| W4 D22–24 | **SFT + DPO** | **Vertex AI tuning** — managed, and uses **LoRA** under the hood (so it teaches the real concept) |
| W4 D22–26 | *Open* model to tune & self-host | **Gemma 4** (Apr 2026, **Apache 2.0**) — Unsloth for LoRA/QLoRA, vLLM / Ollama / llama.cpp / MLX for serving |
| W4 D25 | Document extraction | Gemini vision + **Document AI** |
| W4 D26–27 | Serving & deploy | vLLM on **GKE**/Vertex; Colab/Vertex for GPU |

### Model picks (as of mid-2026 — verify, this moves fast)
- **Gemini 3.5 Flash** — the workhorse. ~$1.50/M in, ~$9.00/M out; cached input ~$0.15/M. Default for agents.
- **Gemini 3.1 Pro** — ~$2.00/M in, ~$12.00/M out. For hard reasoning / the judge.
- **Gemini 2.5 Flash-Lite** — ~$0.10/M in, ~$0.40/M out. Bulk work: synthetic data, cheap judge passes.
- **Gemma 4** (Apache 2.0) — your open model for W4 fine-tuning, serving, and on-device/sovereignty.
- ⚠️ **Gemini 2.5 Flash is scheduled for deprecation (Oct 16, 2026)** — build on 3.5 Flash. *Deprecation churn is itself a lesson: your `Provider` abstraction is what makes this a config change instead of a refactor.*

### 🎁 Gemini-specific bonus experiment (W3)
With a 1M-token context, run the honest baseline almost nobody runs: **"just stuff everything into context" vs your RAG pipeline** — on quality, latency, **and cost**. Sometimes long-context wins; knowing exactly *when* it stops winning is a genuinely senior insight, and it's the sharpest possible version of your token-efficiency goal.

---

## Why multi-provider anyway (non-negotiable)

1. **The target role names "model providers" (plural)** and expects routing, fallbacks, and cost/latency trade-offs across them. This *is* the job.
2. **LLM-as-judge self-preference bias (W3 D19).** Judges tend to favor output from their own family. If Gemini generates *and* Gemini judges, your scores quietly flatter you. **Judge with a different family than you generate with** — that's methodology, not purity.
3. **Deprecations and price moves are constant** (see the 2.5 Flash note above). An abstraction turns a migration into a config change.
4. **"Best model" is per-task and per-month.** The skill is *measuring* that, not believing it.

### How to get it for ~$20
Day 4's `Provider` protocol is **mandatory, not stretch**:

```python
class Provider(Protocol):
    def complete(self, messages, tools=None, schema=None) -> Response: ...
    # normalize: tool-call shape, token accounting, cost, streaming
```

Implement **your primary + one other** (a second API, or a local Gemma/Qwen via Ollama — free). Everything downstream (`miniagent`, `rag`, `evals`) targets the interface, never a vendor SDK. Then:
- W3's **A/B harness** has something real to compare.
- Your **judge** can be a different family than your generator.
- W4's **self-host vs API** decision becomes a measurement instead of an opinion.

> **The normalization work is the learning.** Discovering that provider A returns tool calls in a different shape than provider B, with different token accounting and different streaming semantics, teaches you more about how these systems actually work than any blog post will.

---

## What stays fixed regardless of provider

- **Claude Code (W1 D5–6)** stays as your *coding harness*. That's a **tool-mastery** goal (subagents, skills, hooks, MCP, plan mode), not a model choice. Swapping the tool dodges the gap instead of closing it. Use whatever models you like elsewhere.
- **Local models via Ollama** (Day 0) stay, for every provider path — free iteration and the sovereignty story.
- **The concepts.** Nothing in Weeks 2–4 depends on a vendor. That's the point.
