# Week 3 — Retrieval, Data & Evaluation

**Goal:** two big muscles. First, **RAG at scale** — vector *and* graph retrieval, engineered for token efficiency (your stated gap). Second, and just as important, **evaluation as a first-class discipline** — the thing that separates senior AI engineers from demo-builders, and a headline responsibility of the role.

**Maps to role:** *"retrieval/RAG at scale"*, *"vector databases"*, and *"Own the evaluation stack: golden datasets, LLM-as-judge, human-eval, track regressions and failure modes."*

---

## Day 15 — Embeddings & vector search from scratch

**Objective:** understand retrieval at the metal — embeddings, similarity, ANN — before touching a vector DB.

**Theory (~1.5h):** what an embedding is; cosine vs dot vs L2; the curse of dimensionality; exact vs approximate nearest neighbor (HNSW, IVF); embedding models (open vs API) and their trade-offs.

**🔨 Build — a vector store by hand, then a real one:**
- Compute embeddings for a corpus you care about (your blog, the WEB3DEV docs, a set of invoices). Implement cosine-similarity search **in NumPy** — no library. Retrieve top-k.
- Then stand up a real store (**pgvector** or **LanceDB/Qdrant**) and reproduce the same queries. Compare latency and recall.

**Deliverable:** `projects/rag/` with a `naive_search.py` (NumPy) and a `vector_store.py` (real DB).
**DoD:** you can explain HNSW at a high level and why ANN trades recall for speed.

---

## Day 16 — A real RAG pipeline (and its failure modes)

**Objective:** build end-to-end RAG and confront why naive RAG is mediocre.

**Theory (~1h):** chunking strategies (fixed, recursive, semantic, structure-aware); the retrieve→augment→generate flow; the classic failure modes (bad chunks, lost-in-the-middle, irrelevant retrieval, stale index); metadata filtering.

**🔨 Build — `rag` v1 over your own documents:**
- Ingest → chunk → embed → store → retrieve → prompt-assemble → answer, with citations back to source chunks.
- Deliberately break it (huge chunks, tiny chunks, wrong k) and observe. Log what each knob does to answer quality and token cost.

**Deliverable:** a working RAG CLI/service answering questions over your corpus, with citations.
**DoD:** you can point to a concrete retrieval failure and name the fix.
**⭐ Stretch:** add **hybrid search** (BM25 + vector) and a **reranker** (cross-encoder or Cohere/Voyage rerank); measure the quality lift.

---

## Day 17 — Graph RAG & knowledge graphs (the token-efficiency gap)

**Objective:** directly address "graph databases to consume less tokens" — when a graph beats a pile of chunks.

**Theory (~1.5h):** knowledge graphs; entity/relation extraction with an LLM; GraphRAG (community summaries, multi-hop questions); why graphs help on *global* questions and *connected* reasoning where flat RAG dumps too many tokens; vector-vs-graph-vs-hybrid trade-offs.

**🔨 Build — a graph over your domain:**
- Use an LLM to extract entities & relations from your corpus (e.g. invoices → vendors, amounts, dates, categories) into **Neo4j** (or a lightweight graph).
- Answer a **multi-hop** question that flat RAG handles badly (e.g. "which vendors did we pay in categories that grew >20% quarter over quarter?"). Compare token usage: graph query vs stuffing chunks.

**Deliverable:** `projects/graph-rag/` + a token-cost comparison table (graph vs vector on the same questions).
**DoD:** you can articulate, with your own numbers, exactly when graph retrieval saves tokens and when it's overkill.

---

## Day 18 — Context engineering & retrieval quality

**Objective:** squeeze maximum signal per token — the skill behind "cost and sovereignty".

**Theory (~1h):** context compression; prompt/token budgeting; query rewriting & HyDE; contextual retrieval (Anthropic's technique: prepend context to chunks before embedding); reranking; deduplication; the "just add more context" anti-pattern.

**🔨 Build — make `rag` frugal and sharp:**
- Add **query rewriting**, **contextual retrieval**, and **reranking** to your pipeline. Add a context-compression step before generation.
- Target: same-or-better answer quality at **materially fewer tokens**. Prove it with before/after numbers. (This sets up Day 19's eval to make "better" objective.)

**Deliverable:** upgraded `rag` + a `TOKEN-BUDGET.md` showing the reduction.
**DoD:** you cut tokens per answer meaningfully without losing quality — and you can defend the trade-offs.

---

## Day 19 — Evaluation, from zero (the real differentiator)

**Objective:** stop trusting vibes. Build the discipline the role calls first-class: golden datasets, metrics, a repeatable runner.

**Theory (~1.5h):** why eval is hard for open-ended output; **golden datasets** (how to build one, how many examples); metric types (exact/fuzzy match, semantic similarity, task-specific); **LLM-as-judge** (and its biases — position, verbosity, self-preference); reference-free vs reference-based; offline eval vs online.

**🔨 Build — an eval harness from scratch:**
- Create a **golden dataset** (~30–50 examples) for one of your systems (the RAG, or the Day-7 extraction task).
- Build a runner that executes the system over the dataset and scores it with a mix of deterministic metrics **and** an **LLM-as-judge** (with a rubric). Output a scorecard.
- Validate the judge: hand-label ~15 examples and measure judge-vs-human agreement. If the judge disagrees with you, fix the rubric.

**Deliverable:** `projects/evals/` with dataset, runner, rubric, and a scorecard.
**DoD:** you have a number you *trust* for "how good is this system", and evidence your judge agrees with humans.

---

## Day 20 — Eval in production: regressions, A/B, tracing, observability

**Objective:** wire evals into CI and instrument a running system so failures become improvements ("turn production failures into systematic improvements").

**Theory (~1h):** regression testing for prompts/agents; A/B testing LLM changes; **tracing/observability** (spans over an agent run); tools: **promptfoo**, **Ragas**, **Langfuse/Braintrust/Phoenix**; capturing production failures back into the golden set (the data flywheel).

**🔨 Build — a CI regression gate + tracing:**
- Put your eval harness behind a **GitHub Action** that fails the PR if the score drops below a threshold. Change a prompt and watch it catch a regression.
- Add **tracing** (Langfuse or OpenTelemetry) to `miniagent`/`rag` so every run is a inspectable trace (tokens, latency, tool calls, judge score).
- Build a tiny **A/B harness**: run two prompt/model variants over the golden set and report a winner with the cost delta.

**Deliverable:** passing/failing CI runs (screenshots in the log), traces, and an A/B result.
**DoD:** a prompt change that hurts quality is now *blocked automatically*, and you can inspect any run as a trace.

---

## Day 21 — Integrate & Week 3 retro

**Objective:** fuse the week — an *evaluated* RAG agent — and step back.

**🔨 Build — the RAG agent, measured:**
- Give `miniagent` a `retrieve` tool backed by your best RAG/graph pipeline. Now the agent decides *when* to retrieve. Run it through your eval harness end to end and record the scorecard + cost.

**Deliverable:** an agent that retrieves-on-demand with a full evaluation report.
**DoD:** one command runs the agent over the golden set and prints quality + tokens + cost + latency.

### 🔁 Week 3 retro
- Update the skills matrix (RAG + eval rows).
- `daily-log/week-3-retro.md`: your token-efficiency findings; how you'd explain "why evaluation is the moat" in an interview.
- **Gut check:** given a new AI feature, could you define "what good looks like" and build the eval to prove it? That capability is a top reason this role exists.
