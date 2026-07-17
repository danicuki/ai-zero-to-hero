# Skills Matrix — Day 0 vs Day 30

The scoreboard for the whole program. Score each competency **1–5** on Day 0 (before) and Day 30 (after). Be brutally honest on Day 0 — a low score is a target, not a failure. The **delta** is your proof.

**Scale:** 1 = never touched · 2 = read about it · 3 = can do it with heavy hand-holding/docs · 4 = can do it independently · 5 = can design it, teach it, and lead others building it.

**Success bar:** the program worked if you reach **4–5 on every core competency**, and can point to a shipped artifact for each.

| # | Competency (mapped to the target role) | Day 0 | Day 30 | Proof (artifact) |
|---|------------------------------------------|:-----:|:------:|------------------|
| **LLM foundations** |
| 1 | Tokens, context windows, cost/latency economics | 2 | _ | `toktool` |
| 2 | Transformers, attention, KV-cache (enough to decide architecture) | 1 | _ | `nanogpt` |
| 3 | Sampling, decoding, hallucination causes & mitigations | 1 | _ | `decoding-lab` |
| **API & tooling** |
| 4 | Claude API mastery (tools, streaming, structured output, caching, thinking) | 2 | _ | `askctl` |
| 5 | Claude Code power use (subagents, skills, hooks, MCP, plan mode) | 2 | _ | `.claude/` config |
| 6 | Prompt & behaviour engineering (versioned, tested) | 1 | _ | `prompt-harness` |
| **Agents & harness** |
| 7 | Build an agent harness from scratch (loop, tools, state, reliability) | 2 | _ | `miniagent` |
| 8 | Context construction & memory (compaction, persistence) | 2 | _ | `miniagent` memory |
| 9 | Guardrails & failure handling for production agents | 1 | _ | `miniagent` tools |
| 10 | MCP — author servers & wire clients | 2 | _ | `mcp-ledger` |
| 11 | Multi-agent orchestration (and knowing when *not* to) | 2 | _ | orchestrator mode |
| 12 | Understand real agent-runtime internals | 2 | _ | `harness-teardown.md` |
| 13 | Agent frameworks in perspective (LangGraph/PydanticAI/Agent SDK) | 1 | _ | `framework-port` |
| **Retrieval & data** |
| 14 | Embeddings & vector search (incl. from scratch) | 1 | _ | `rag` |
| 15 | RAG at scale (chunking, hybrid, rerank, failure modes) | 1 | _ | `rag` |
| 16 | Graph RAG / knowledge graphs for token efficiency | 1 | _ | `graph-rag` |
| 17 | Context engineering / token budgeting | 1 | _ | `TOKEN-BUDGET.md` |
| **Evaluation** |
| 18 | Golden datasets & metrics design | 1 | _ | `evals` |
| 19 | LLM-as-judge (+ validating the judge) | 1 | _ | `evals` |
| 20 | Regression gates in CI, A/B, tracing/observability | 1 | _ | CI + traces |
| **Models: train & serve** |
| 21 | Fine-tuning (SFT, LoRA/QLoRA) & when *not* to | 1 | _ | `finetune` |
| 22 | Preference optimization (DPO) & RL literacy | 1 | _ | `finetune/dpo` |
| 23 | Document extraction / IDP models | 1 | _ | `doc-extraction` |
| 24 | Model serving, quantization, cost/latency (vLLM, local/on-device) | 2 | _ | `serving` |
| **Production & leadership** |
| 25 | Safety, prompt-injection defense, guardrails | 2 | _ | `SECURITY.md` |
| 26 | Deploy & operate an AI service (AWS, observability, cost caps) | 3 | _ | deployed endpoint |
| 27 | Ship an end-to-end production agentic product | 1 | _ | `capstone` |
| 28 | Architect & *lead* an AI initiative (design, trade-offs, "what good looks like") | 2 | _ | `DESIGN.md` |

## Totals

| | Day 0 | Day 30 |
|-|:-----:|:------:|
| **Sum (max 140)** | **41** | _ |
| **Avg** | **1.46** | _ |

**Day-0 distribution:** 16 rows at `1`, 11 rows at `2`, 1 row at `3`.

*(Recalibrated from a self-scored 39 on Day 0: row 26 `2→3` and row 28 `1→2`. Rationale: both rows have a transferable half — 25 years of deploy/observability/cost-control, and leading an 80-person org — that "never touched" misrepresents. The AI-specific half is genuinely new; the engineering half is not. Sandbagging the baseline would make the Day-30 delta measure confidence recovering rather than skill growing, and those must stay distinguishable. See [`resources/what-transfers.md`](../resources/what-transfers.md).)*

**Day-0 by block** (avg): LLM foundations 1.33 · API & tooling 1.67 · Agents & harness **1.71** · Retrieval & data **1.00** · Evaluation **1.00** · Models train/serve 1.25 · Production & leadership 2.00

**The diagnostic:** the 2s cluster exactly where you touch tools daily (API, Claude Code, agents) — you *use* them without owning them. The 1s cluster in **Retrieval, Evaluation, and Training** — Weeks 3 and 4. Note that **Evaluation is a clean sweep of 1s and is the target role's #2 headline responsibility.** Your weakest block is the role's most-wanted skill. That's not bad news; that's the highest-leverage 3 days in the program (D19–21).

## The honest verdict (write on Day 30)

> Re-read the role's requirements. For each, can you name a build that proves you can do it? Do you *feel* you could architect and lead any AI initiative? Write the answer here, unflinchingly. That sentence is what the whole month was for.
