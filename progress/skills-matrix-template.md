# Skills Matrix — Day 0 vs Day 30

The scoreboard for the whole program. Score each competency **1–5** on Day 0 (before) and Day 30 (after). Be brutally honest on Day 0 — a low score is a target, not a failure. The **delta** is your proof.

**Scale:** 1 = never touched · 2 = read about it · 3 = can do it with heavy hand-holding/docs · 4 = can do it independently · 5 = can design it, teach it, and lead others building it.

**Success bar:** the program worked if you reach **4–5 on every core competency**, and can point to a shipped artifact for each.

| # | Competency (mapped to the target role) | Day 0 | Day 30 | Proof (artifact) |
|---|------------------------------------------|:-----:|:------:|------------------|
| **LLM foundations** |
| 1 | Tokens, context windows, cost/latency economics | _ | _ | `toktool` |
| 2 | Transformers, attention, KV-cache (enough to decide architecture) | _ | _ | `nanogpt` |
| 3 | Sampling, decoding, hallucination causes & mitigations | _ | _ | `decoding-lab` |
| **API & tooling** |
| 4 | Claude API mastery (tools, streaming, structured output, caching, thinking) | _ | _ | `askctl` |
| 5 | Claude Code power use (subagents, skills, hooks, MCP, plan mode) | _ | _ | `.claude/` config |
| 6 | Prompt & behaviour engineering (versioned, tested) | _ | _ | `prompt-harness` |
| **Agents & harness** |
| 7 | Build an agent harness from scratch (loop, tools, state, reliability) | _ | _ | `miniagent` |
| 8 | Context construction & memory (compaction, persistence) | _ | _ | `miniagent` memory |
| 9 | Guardrails & failure handling for production agents | _ | _ | `miniagent` tools |
| 10 | MCP — author servers & wire clients | _ | _ | `mcp-ledger` |
| 11 | Multi-agent orchestration (and knowing when *not* to) | _ | _ | orchestrator mode |
| 12 | Understand real agent-runtime internals | _ | _ | `harness-teardown.md` |
| 13 | Agent frameworks in perspective (LangGraph/PydanticAI/Agent SDK) | _ | _ | `framework-port` |
| **Retrieval & data** |
| 14 | Embeddings & vector search (incl. from scratch) | _ | _ | `rag` |
| 15 | RAG at scale (chunking, hybrid, rerank, failure modes) | _ | _ | `rag` |
| 16 | Graph RAG / knowledge graphs for token efficiency | _ | _ | `graph-rag` |
| 17 | Context engineering / token budgeting | _ | _ | `TOKEN-BUDGET.md` |
| **Evaluation** |
| 18 | Golden datasets & metrics design | _ | _ | `evals` |
| 19 | LLM-as-judge (+ validating the judge) | _ | _ | `evals` |
| 20 | Regression gates in CI, A/B, tracing/observability | _ | _ | CI + traces |
| **Models: train & serve** |
| 21 | Fine-tuning (SFT, LoRA/QLoRA) & when *not* to | _ | _ | `finetune` |
| 22 | Preference optimization (DPO) & RL literacy | _ | _ | `finetune/dpo` |
| 23 | Document extraction / IDP models | _ | _ | `doc-extraction` |
| 24 | Model serving, quantization, cost/latency (vLLM, local/on-device) | _ | _ | `serving` |
| **Production & leadership** |
| 25 | Safety, prompt-injection defense, guardrails | _ | _ | `SECURITY.md` |
| 26 | Deploy & operate an AI service (AWS, observability, cost caps) | _ | _ | deployed endpoint |
| 27 | Ship an end-to-end production agentic product | _ | _ | `capstone` |
| 28 | Architect & *lead* an AI initiative (design, trade-offs, "what good looks like") | _ | _ | `DESIGN.md` |

## Totals

| | Day 0 | Day 30 |
|-|:-----:|:------:|
| **Sum (max 140)** | _ | _ |
| **Avg** | _ | _ |

## The honest verdict (write on Day 30)

> Re-read the role's requirements. For each, can you name a build that proves you can do it? Do you *feel* you could architect and lead any AI initiative? Write the answer here, unflinchingly. That sentence is what the whole month was for.
