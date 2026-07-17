# Week 4 — Training, Serving & Production (+ Capstone)

**Goal:** close the last gaps — **make your own models** (fine-tuning, preference optimization, document extraction), **serve them cheaply and sovereignly**, and then **ship a production agentic product** that ties the whole month together. This is where "duck" becomes "engineer who can lead any AI initiative".

**Maps to role:** *"Host and improve our own small models: serving and inference of open-source LLMs, fine-tuning and post-training (SFT / DPO / RL), and document-extraction models — for performance, cost and sovereignty."* Plus AWS/model-serving/cost-latency.

---

## Day 22 — When (not) to fine-tune + your first SFT

**Objective:** kill the reflex to fine-tune; then do it well when it's right.

**Theory (~1.5h):** the decision tree — prompt → few-shot → RAG → fine-tune (in that order of cost/benefit); what fine-tuning *does* and *doesn't* fix (style/format/latency yes, new knowledge mostly no); **SFT** basics; **LoRA/QLoRA** (why parameter-efficient tuning works); dataset format (instruction/response); overfitting & catastrophic forgetting.

**🔨 Build — your first fine-tune (LoRA/QLoRA):**
- Take a small open model (e.g. **Qwen2.5-3B/7B** or **Llama-3.2-3B**) and SFT it with **LoRA** (Hugging Face `peft`/`trl`, or **Unsloth** for speed) on a small task-specific dataset you build (~200–500 examples) — e.g. "turn a messy transaction line into a structured category+memo" (domain-relevant).
- Run on Colab/Modal/Runpod if no local GPU. Track loss; save adapters.

**Deliverable:** `projects/finetune/` with data prep, training script, and saved LoRA adapters.
**DoD:** you trained a model, and you can state precisely *why* fine-tuning was (or wasn't) the right call vs RAG here.

---

## Day 23 — Evaluate the fine-tune (close the loop) + data quality

**Objective:** prove the fine-tune helped — using Week 3's discipline — and learn that data quality dominates.

**Theory (~1h):** eval for fine-tunes (compare base vs tuned on a held-out set); data-centric AI (garbage in, garbage out); synthetic data generation with a bigger model; deduplication & decontamination; the risk of training on your test set.

**🔨 Build — base vs tuned, measured:**
- Run **base model vs your fine-tuned model** through your Week-3 eval harness on a held-out golden set. Report the delta (quality, and cost/latency vs an API call).
- Improve the dataset once (clean it / add synthetic examples), retrain, and show the eval move. Experience the data flywheel first-hand.

**Deliverable:** an eval report: base vs v1 vs v2, with quality + cost/latency.
**DoD:** you have numbers proving whether your fine-tune beats prompting an API model, and you know why.

---

## Day 24 — Preference optimization (DPO) & a look at RL

**Objective:** go beyond imitation (SFT) to *preferences* — how models are aligned — at least to working literacy (the role asks for "exposure to SFT/DPO/RL").

**Theory (~1.5h):** RLHF pipeline (SFT → reward model → PPO) at a conceptual level; **DPO** as the simpler, popular alternative (no separate reward model); preference-pair datasets; a nod to **GRPO**/RLVR for reasoning models. Understand the *shape* of RL post-training even if you don't run a full PPO loop.

**🔨 Build — a DPO run:**
- Build a small preference dataset (chosen vs rejected responses — can be bootstrapped with an LLM + your judge from Week 3) and run **DPO** (TRL `DPOTrainer`) on your SFT model.
- Evaluate: did aligning to your preferences improve the judge score on the traits you targeted (e.g. concise, correctly-formatted, no hallucinated fields)?

**Deliverable:** `projects/finetune/dpo/` + before/after judge scores.
**DoD:** you can explain SFT vs DPO vs RLHF and when each is worth it — from having run two of them.

---

## Day 25 — Document extraction (the domain model)

**Objective:** build the specific model type the role names — IDP over financial documents — tying training + evaluation + product together.

**Theory (~1h):** document AI / IDP; OCR vs vision-language models; structured extraction with confidence; when to use a VLM (e.g. a Qwen-VL / Claude vision) vs a fine-tuned extractor vs a layout model; evaluation of extraction (field-level precision/recall).

**🔨 Build — an invoice/receipt extractor:**
- Build a pipeline that takes document images/PDFs (grab a public receipts/invoices dataset) and extracts a structured schema (vendor, date, line items, totals, tax) with per-field confidence.
- Evaluate at the **field level** (precision/recall per field) using a golden set. Compare a VLM-prompt approach vs a small fine-tuned/hybrid approach on accuracy **and** cost.

**Deliverable:** `projects/doc-extraction/` + a field-level eval report.
**DoD:** you can quote extraction accuracy per field and make a cost/sovereignty recommendation (API VLM vs self-hosted).

---

## Day 26 — Serving, quantization & cost/latency

**Objective:** make a model actually servable — fast, cheap, and yours (sovereignty).

**Theory (~1.5h):** inference basics (prefill vs decode, batching, KV-cache, throughput vs latency); **vLLM** (paged attention, continuous batching); **quantization** (GGUF/AWQ/GPTQ, int8/int4) and its quality trade-off; local/on-device serving (**Ollama**, **llama.cpp**, MLX on Apple Silicon — aligns with on-device sovereignty); when self-hosting beats an API on cost.

**🔨 Build — serve your model, measure the economics:**
- Serve your fine-tuned/base model with **vLLM** (or llama.cpp/Ollama locally). Hit it with a load test; measure **tokens/sec, p50/p95 latency, and $/1M tokens** at your hardware cost.
- Quantize it (e.g. to int4) and re-measure quality (via your eval harness) vs speed/memory. Plot the trade-off.

**Deliverable:** `projects/serving/` with a benchmark table: latency/throughput/cost, quantized vs full, self-hosted vs API.
**DoD:** you can answer "should we self-host or use an API for X?" with real numbers.

---

## Day 27 — Production concerns: safety, guardrails & AWS deploy

**Objective:** the "make it reliable in production" and "not just calling an API" bar — security, safety, deployment.

**Theory (~1h):** **prompt injection** & tool-abuse (esp. dangerous with agents + tools); output guardrails & PII handling; secrets/keys; rate limits, retries, fallbacks across providers; cost controls & budgets; observability in prod; a pragmatic AWS deployment path (container → ECS/Lambda + a model endpoint, since the role names AWS).

**🔨 Build — harden and deploy:**
- Add a **prompt-injection test suite** to your agent (adversarial inputs trying to make it misuse tools) and defenses (input screening, tool allow-lists, confirmation gates, output validation). Show attacks caught.
- Containerize one system (the RAG agent or extractor) and deploy it to a cloud endpoint (AWS or similar) with health checks, logging, and a cost cap.

**Deliverable:** a deployed endpoint URL + a `SECURITY.md` documenting the injection tests and defenses.
**DoD:** a known prompt-injection attack against your agent is demonstrably blocked, and the service runs in the cloud.

---

## Day 28–30 — 🏆 Capstone: ship a production agentic product

**Objective:** integrate everything into one real, deployed, evaluated product — and be able to whiteboard it (doubles as **case-study interview prep**).

**Build — the capstone.** Pick a project that exercises the full stack (a strong default, domain-aligned):

> **"Accounting Copilot"** — an agent that, over a corpus of invoices/transactions, answers complex multi-step questions and completes a workflow end to end: it **retrieves** (vector + graph), **extracts** structure from documents (Day 25), **calls tools** via **your MCP server** (Day 11), **remembers** across a session (Day 9), is **guarded** against injection (Day 27), can optionally use your **self-hosted fine-tuned model** for the extraction/classification step (Days 22–26), is **fully evaluated** with a golden set + LLM-as-judge in **CI** (Days 19–20), and is **deployed** with tracing and a cost dashboard.

Pick your own domain if you prefer — the requirements below are what matter.

**Day 28 — Architecture & spec.** Write `projects/capstone/DESIGN.md`: problem, users, the agent's task, architecture diagram, the eval plan ("what good looks like"), cost/latency budget, and the build-vs-buy / self-host-vs-API decisions *with reasons*. This doc **is** your interview case study. Review it with your mentor before building.

**Day 29 — Build the core.** Assemble the pieces you already built into one deployable service: harness + retrieval + tools/MCP + guardrails + memory. Get the happy path working end to end with tracing.

**Day 30 — Evaluate, harden, ship, present.** Run the full eval suite; wire the CI gate; deploy; record cost/latency; write the README + a short **demo video or walkthrough**; and write `SHOWCASE.md` — a crisp narrative a hiring manager (or your own future team) could read.

**Capstone Definition of Done (all must be true):**
- [ ] Deployed and reachable; runs the end-to-end workflow.
- [ ] Retrieval (vector and/or graph) with citations, token-budgeted.
- [ ] At least one custom-trained or self-hosted model component, with a *justified* decision to use it (or a documented reason you chose an API instead).
- [ ] A golden dataset + LLM-as-judge eval, gated in CI.
- [ ] Guardrails + a passing prompt-injection test suite.
- [ ] Tracing/observability and a cost/latency report.
- [ ] `DESIGN.md`, `SHOWCASE.md`, and a demo you could present in a 75-min case-study interview.

### 🔁 Final retro & graduation
- Fill the **Day-30 column** of the [skills matrix](../progress/skills-matrix.md). Compute the delta from Day 0.
- Write `daily-log/graduation.md`: the arc, the proudest build, what you'd tell yourself on Day 0.
- **The verdict:** re-read the role's requirements. For each, point to a build that proves you can do it. If every line has a receipt — you're a Hero. 🎓
