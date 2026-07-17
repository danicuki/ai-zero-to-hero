# Projects — the portfolio you'll build

Each day produces a real, committed artifact. By Day 30 this folder *is* your proof of skill — a portfolio you can show, demo, and talk through in an interview. Build everything under `projects/`.

## The build list

| # | Project | Week/Day | What it proves |
|---|---------|----------|----------------|
| 1 | `toktool` | W1 D1 | You understand tokens, context & cost |
| 2 | `nanogpt` | W1 D2 | You understand transformers from the inside |
| 3 | `decoding-lab` | W1 D3 | You understand sampling & hallucination |
| 4 | `askctl` | W1 D4 | You command the Claude API (tools, streaming, caching, structured output) |
| 5 | `prompt-harness` | W1 D7 | You engineer prompts with evidence |
| 6 | `miniagent` | W2 D8–12 | **You built an agent harness from scratch** (loop, memory, guardrails, multi-agent) |
| 7 | `mcp-ledger` | W2 D11 | You author MCP servers, not just consume them |
| 8 | `harness-teardown.md` | W2 D13 | You understand real agent internals |
| 9 | `framework-port` | W2 D14 | You have a defensible build-vs-framework opinion |
| 10 | `rag` | W3 D15–18 | You ship RAG at scale, token-efficiently |
| 11 | `graph-rag` | W3 D17 | You know when graphs beat chunks (and save tokens) |
| 12 | `evals` | W3 D19–20 | **You run evaluation as a discipline** (golden sets, LLM-judge, CI gates) |
| 13 | `finetune` | W4 D22–24 | You make your own models (SFT, LoRA/QLoRA, DPO) |
| 14 | `doc-extraction` | W4 D25 | You build domain document-extraction models |
| 15 | `serving` | W4 D26 | You serve models cheaply & measure the economics |
| 16 | `capstone` | W4 D28–30 | **You ship a production agentic product, end to end** |

## Standards for every project

- A `README.md`: what it is, how to run it, what you learned, and its **token/cost profile**.
- Reproducible: `uv run ...` or a `Makefile` target. Someone else can run it.
- Committed the day it's built. No "I'll clean it up later" limbo.
- Where relevant, a number: latency, tokens, cost, or an eval score. Senior AI work is measured.

## The capstone is the headline

Projects 1–15 are the muscles; the **capstone (project 16)** is the performance. Treat its `DESIGN.md` and `SHOWCASE.md` as portfolio centerpieces — they're what a hiring manager reads and what you'd whiteboard in a case-study interview. Spec is in [`../plan/week-4-training-serving-capstone.md`](../plan/week-4-training-serving-capstone.md).
