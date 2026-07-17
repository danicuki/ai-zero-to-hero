# The canon — papers & primary sources

You don't need to read all of these cover to cover. **Bold** ones are must-reads for this program; the rest are reference for when a topic comes up. Read for *mental models*, not memorization.

## Foundations (Week 1)
- **"Attention Is All You Need"** (Vaswani et al., 2017) — the transformer. Read it Day 2.
- **Karpathy — "Let's build GPT" / nanoGPT** (video + repo) — the single best way to *build* understanding. Day 2.
- **Karpathy — "Let's build the GPT Tokenizer"** (video) — tokenization, Day 1.
- "Language Models are Few-Shot Learners" (GPT-3, Brown et al., 2020) — in-context learning.
- "Training Compute-Optimal LLMs" (Chinchilla, Hoffmann et al., 2022) — scaling laws / why model+data size trade off.
- "The Illustrated Transformer" (Jay Alammar) — the friendliest visual explainer.

## Alignment & post-training (Week 4)
- **"Training language models to follow instructions with human feedback"** (InstructGPT, Ouyang et al., 2022) — RLHF, the recipe behind chat models.
- **"Direct Preference Optimization"** (Rafailov et al., 2023) — DPO, what you'll run Day 24.
- "LoRA: Low-Rank Adaptation of LLMs" (Hu et al., 2021) — parameter-efficient fine-tuning. Day 22.
- "QLoRA: Efficient Finetuning of Quantized LLMs" (Dettmers et al., 2023) — how you fine-tune on one GPU.
- "DeepSeek-R1" / GRPO (2025) — RL for reasoning; read for the *shape* of modern RL post-training.

## Agents (Week 2)
- **Anthropic — "Building effective agents"** (2024) — the pragmatic patterns (workflows vs agents, orchestrator-worker). Day 12.
- **"ReAct: Synergizing Reasoning and Acting in LLMs"** (Yao et al., 2022) — the reason+act loop you'll build. Day 8.
- "Toolformer" (Schick et al., 2023) — models learning to use tools.
- "Reflexion" (Shinn et al., 2023) — self-critique/iteration.
- Anthropic — "Effective context engineering for AI agents" (2025) — memory/context, Day 9.
- The **Model Context Protocol** spec & docs (modelcontextprotocol.io) — Days 6 & 11.

## Retrieval & RAG (Week 3)
- **"Retrieval-Augmented Generation for Knowledge-Intensive NLP"** (Lewis et al., 2020) — the original RAG.
- **Anthropic — "Introducing Contextual Retrieval"** (2024) — the technique you'll implement Day 18.
- "Dense Passage Retrieval" (Karpukhin et al., 2020) — embeddings-based retrieval.
- Microsoft — "GraphRAG" paper & repo (2024) — graph retrieval for global/multi-hop questions. Day 17.
- "Lost in the Middle" (Liu et al., 2023) — why stuffing context degrades; motivates reranking.
- HNSW paper (Malkov & Yashunin, 2018) — approximate nearest neighbor, skim for intuition.

## Evaluation (Week 3)
- **"Judging LLM-as-a-Judge"** (Zheng et al., 2023, MT-Bench/Chatbot Arena) — LLM-as-judge and its biases. Day 19.
- Ragas paper/docs — RAG-specific metrics. Day 20.
- "Holistic Evaluation of Language Models" (HELM, Liang et al., 2022) — how to think about eval breadth.

## Serving & efficiency (Week 4)
- **"Efficient Memory Management for LLM Serving with PagedAttention"** (vLLM, Kwon et al., 2023) — Day 26.
- "FlashAttention" (Dao et al., 2022) — why attention got fast; skim.
- "GPTQ" / "AWQ" — post-training quantization; reference for Day 26.

## Safety (Week 4)
- "Universal and Transferable Adversarial Attacks on Aligned LMs" (Zou et al., 2023) — jailbreaks.
- OWASP Top 10 for LLM Applications — the practical prod checklist. Day 27.
- Simon Willison's writing on **prompt injection** — the clearest practical treatment. Day 27.

> **How to read a paper fast (you have 25 years of pattern-matching — use it):** abstract → figures → intro's last paragraph (contributions) → conclusion → method only if you'll build it. 20 minutes, not 2 hours.
