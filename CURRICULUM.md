# Curriculum: design, gap analysis & philosophy

## 1. Who this was built for

A senior engineer with **~25 years** of experience — PhD in CS, Google Developer Expert, distributed systems / cloud / scaling / DevOps, and a track record leading large engineering teams and founding companies. In other words: **elite generalist fundamentals, rusty on the modern ML/LLM stack** after years in CTO/founder seats.

That profile is a gift and a trap:
- **Gift:** systems thinking, production instincts, ability to learn fast, taste for architecture. We can move *very* fast and skip the beginner scaffolding.
- **Trap:** "I know a bit of everything" masks the fact that none of the *specific* AI-engineering muscles have been trained. The cure is depth-by-construction, not more tutorials.

## 2. The target competency (reverse-engineered from the role)

The plan is anchored to a real, hard "Core AI Engineer" job. Its explicit requirements:

1. **Own the agent harness** — the runtime that orchestrates LLM calls, tool use, context construction, memory and guardrails, and make it reliable in production.
2. **Evaluation as a first-class discipline** — eval pipelines, golden datasets, LLM-as-judge, human eval, A/B testing; track performance, regressions, failure modes; turn production failures into systematic improvement.
3. **Prompt & behaviour engineering + RAG at scale.**
4. **Applied LLM/ML + AI infra** — model serving, vector databases, cost & latency.
5. **Host & improve small models** — serving/inference of open-source LLMs, fine-tuning & post-training (SFT / DPO / RL), and **document-extraction models** (IDP/OCR over invoices, receipts, financial docs) — for performance, cost and **sovereignty**.
6. **Very strong Python**, production reliability mindset ("not just calling a model API").

The domain is **accounting/finance**: agents completing complex, multi-step workflows *end to end*. The stack named in the role: **Python, agentic frameworks, evaluation tooling, model serving, AWS, MCP, multiple model providers**. Every day of this program traces back to one of these six competencies.

> **Interview alignment:** the target role's process includes a **75-minute case-study interview** on a real priority. The Week-4 capstone is deliberately designed to double as case-study prep — build the thing, then be able to whiteboard it.

## 3. Gap analysis (self-declared + inferred)

| # | Gap you named | Where we close it |
|---|----------------|-------------------|
| G1 | "I use Claude to code but don't use all its features" | W1 D5–6 (Claude Code mastery), used daily thereafter |
| G2 | "I use an open-source agent but don't understand its internals" | W2 (build your own harness; reverse-engineer a real one) |
| G3 | "Never built a production-level AI product" | W3–W4 + Capstone (ship, observe, guardrail, deploy) |
| G4 | "Don't know RAG / graph DBs for token efficiency" | W3 D15–18 (vector + graph RAG, context engineering) |
| G5 | "Can't create custom models on my own data" | W4 D22–25 (SFT, LoRA/QLoRA, DPO, doc-extraction, data prep) |
| G6 | "Lost the technical path" (confidence) | The whole thing: 30 green squares + a shipped product |

Inferred gaps the role exposes that you *didn't* name (we cover them too):
- **Evaluation rigor** (the #2 differentiator of senior AI engineers — most people skip it).
- **Cost/latency/token economics** as an engineering discipline.
- **Serving & quantization / on-device** (aligns with your stated interest in sovereign, on-device intelligence).
- **AI safety & prompt-injection defense** for production agents.

## 4. Philosophy: depth by construction

Five principles the whole program obeys:

1. **Build the primitive before the framework.** You will hand-roll the agent loop, a retriever, an eval runner, and a training loop *before* touching LangGraph, LlamaIndex, Ragas, or TRL. Frameworks then become obvious instead of magic.
2. **Reverse-engineer what you use.** The fastest way to understand a tool's internals is to clone its core behavior. We rebuild a mini Claude-Code-style agent to demystify the ones you run.
3. **Measure everything.** Tokens, latency, cost, and eval scores on every build. Senior AI engineering is an *economics* discipline, not just a correctness one.
4. **Evaluation is the moat.** Anyone can demo. The differentiator is a golden dataset + regression gate that tells you whether a change made things better. We treat evals as production code.
5. **Ship to production, not to a notebook.** Every capstone artifact runs as a service with observability and guardrails.

## 5. Learning outcomes (what "Hero" means)

By Day 30 you can, without hand-waving:

- Explain transformers, attention, tokenization, sampling, context windows, and scaling laws well enough to make architecture decisions and cost estimates.
- Wield the Claude API (tool use, structured output, streaming, prompt caching, extended thinking) and Claude Code (subagents, skills, hooks, MCP, plan mode) at expert level.
- **Build an agent harness from scratch**: agent loop, tool calling, context/memory management, guardrails, retries, state, multi-agent orchestration — and reason about *why* real harnesses make the choices they do.
- Build and operate **RAG at scale**: embeddings, chunking, hybrid search, reranking, and **graph retrieval**, with deliberate token-efficiency.
- Stand up an **evaluation stack**: golden datasets, LLM-as-judge, human eval, A/B, regression tracking in CI, plus tracing/observability.
- **Fine-tune** a model on your own data (SFT + LoRA/QLoRA), apply preference optimization (DPO), build a **document-extraction** pipeline, and know precisely *when not to fine-tune*.
- **Serve** models efficiently (vLLM, quantization, local/on-device), and optimize cost & latency.
- Ship a production agentic product with guardrails, safety, observability, and evals — and **lead** a team building one.

## 6. Prerequisites & assumptions

- Comfortable in a terminal, git, Docker, and at least one language deeply. **Python** is the working language here; if it's rusty, W1 D0 has a fast-refresh path.
- A machine that can run local models is a plus (Apple Silicon / a decent GPU). Cloud GPUs (Modal, Runpod, Colab) cover the fine-tuning days if not.
- Budget: expect **~$50–150** in API + GPU credits across the month. Frugality is part of the curriculum.

## 7. How to adapt the pace

- **Have only ~3h/day?** Do the Build, skim the Theory, stretch each week to ~10 days.
- **Full-time (8h+)?** Add the ⭐ *Stretch* goals each day and compress to ~3 weeks.
- **Already strong in an area?** Don't skip the Build — do it faster and harder. The matrix is your guide: spend your time where your Day-0 scores are lowest.
