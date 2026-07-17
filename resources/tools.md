# The stack — tools to learn (and why)

Aligned to the target role's named stack: **Python, agentic frameworks, evaluation tooling, model serving, AWS, MCP, multiple model providers.** Learn the **bold** ones hands-on; know the rest exist.

## Language & environment
- **Python 3.12** — the working language. **`uv`** for env/deps (fast, modern). **`pydantic`** for schemas everywhere. **`httpx`** for async HTTP.
- **Ruff** (lint/format), **pytest** (yes, test your AI code), **Docker**.

## Model providers & clients
> **Pick a primary, but stay multi-provider.** See [`providers.md`](providers.md) for the full strategy and the Gemini-first / Claude-first / local-first paths.

- **Google Gemini SDK** (`google-genai`) — function calling, `response_schema` structured output, implicit context caching, thinking budgets, MCP support, Batch API (50% off). **Gemini 3.5 Flash** as the workhorse, **3.1 Pro** for hard reasoning, **2.5 Flash-Lite** for cheap bulk/judge passes.
- **Anthropic SDK / Claude API** — tool use, prompt caching, extended thinking, structured output.
- OpenAI SDK — the third point of comparison.
- **Ollama** — run local models trivially, and your *free* secondary provider (Day 0 onward).
- OpenRouter — one API across many models, handy for cheap comparison.
- ⚠️ **Models get deprecated mid-flight** (e.g. Gemini 2.5 Flash EOL Oct 16, 2026). Your Day-4 `Provider` abstraction is what turns that into a config change.

## Agent building
- **Build-your-own first** (Week 2) — no framework.
- **LangGraph** — graph/state-machine agents; the current default for complex control flow.
- **PydanticAI** — typed, ergonomic agents; pairs well with your pydantic-everywhere habit.
- **Claude Agent SDK** — Anthropic's own harness; study how it structures the loop.
- **MCP (Model Context Protocol)** — the tool/resource protocol. Use it (W1) and author it (W2). Python SDK: `mcp`.

## Retrieval & vector/graph
- **pgvector** (Postgres extension) — production-friendly, you probably already run Postgres.
- **LanceDB** / **Qdrant** — purpose-built vector DBs; LanceDB is great locally.
- **Neo4j** — graph DB for GraphRAG (Day 17). `networkx` for tiny in-memory graphs.
- Embeddings: **`sentence-transformers`** (local), Voyage/Cohere/OpenAI embeddings (API). **Cohere/Voyage rerank** for reranking.
- **LlamaIndex** — batteries-included RAG; meet it *after* you've built RAG by hand.

## Evaluation & observability
- **promptfoo** — declarative prompt/model testing & CI gates. Day 20.
- **Ragas** — RAG-specific metrics. Day 20.
- **Langfuse** (open-source, self-hostable — good for sovereignty) or **Braintrust** / **Arize Phoenix** — tracing + eval dashboards.
- **OpenTelemetry** — vendor-neutral tracing if you want to own it.

## Training & fine-tuning
- **Hugging Face** — `transformers`, `datasets`, `peft` (LoRA), **`trl`** (SFT/DPO trainers). The backbone of Week 4.
- **Unsloth** — ~2x faster / ~70% less memory LoRA fine-tuning on a single GPU; natively supports current Gemma sizes. Great for Days 22–24.
- **Axolotl** — config-driven fine-tuning if you want less code.
- **Vertex AI tuning** — *managed* SFT **and DPO** on Gemini (LoRA under the hood). The "buy" side of Day 22's build-vs-buy comparison.
- Open models to tune: **Gemma 4** (Apache 2.0, Apr 2026), Qwen, Llama.
- GPU compute: **Google Colab** (free-ish), **Modal** (serverless GPU, lovely DX), **Runpod**/**Lambda** (cheap rentals).

## Serving & inference
- **vLLM** — high-throughput serving (PagedAttention). The production default. Day 26.
- **llama.cpp** / **GGUF** — CPU/edge inference; **MLX** for Apple Silicon (on-device sovereignty).
- **Ollama** — easiest local serving.
- Quantization: **AWQ**, **GPTQ**, GGUF int4/int8.

## Deploy & infra (the role names AWS)
- **AWS** — ECS/Fargate or Lambda for the service; **Bedrock** for managed model hosting; SageMaker if you go deep on training/hosting. S3 for artifacts.
- Alternatives to move fast: **Modal** (deploy Python + GPU as functions), Fly.io, Railway.
- **GitHub Actions** — your eval regression gate (Day 20).

## Document AI (Day 25)
- Vision-language models: **Qwen2.5-VL**, Claude vision, for extraction.
- OCR: **docTR**, PaddleOCR, or Tesseract as a baseline.
- Datasets: public receipts/invoices sets (e.g. SROIE, CORD) for practice.

## Knowledge & staying current
- Read: **Anthropic engineering blog**, **Simon Willison's blog**, **Chip Huyen** (ML systems), **Lilian Weng** (deep dives), Latent Space (podcast/newsletter).
- Skim, don't drown. Pick 3 sources, unfollow the rest.

> **Rule:** every tool here is a means to a build. Don't "learn a tool" in the abstract — pull it in the day a project needs it, and delete it from your head if a project never does.
