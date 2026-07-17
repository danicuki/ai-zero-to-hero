# AI Zero to Hero 🚀

> A 30-day intensive to turn a **senior generalist engineer / CTO** into a **hands-on, top-tier Agentic AI Engineer** — one who can build *and lead* any AI initiative with confidence.

This repo is a full, opinionated study program: daily routine, theory, and **hard hands-on builds**. It was designed for one person (see [`CURRICULUM.md`](CURRICULUM.md)) but is written so **anyone can walk the same path**.

**The bet:** You don't truly understand a tool until you've built a worse version of it. So we don't just *use* agents, RAG, evals, and fine-tuning — we **rebuild the core of each from scratch**, then rebuild it *well*, then ship it to production.

---

## The success criterion (non-negotiable)

> After 30 days you should be able to **architect, build, evaluate, ship, and lead ANY AI initiative** — an agent harness, a RAG system, an eval stack, a fine-tuned model, a production agentic product — without hand-waving. If you can't, the program failed.

We measure this concretely with the [Skills Matrix](progress/skills-matrix.md): self-score 1–5 on Day 0 and Day 30 across every competency the target role demands. The delta is the proof.

---

## Who this is for

The "**duck problem**": you know a bit of everything, nothing deeply. You *use* Claude Code but don't exploit half its power. You run an open-source coding agent but don't understand its internals. You've never shipped a production-grade AI product. You don't know RAG/graph retrieval for token efficiency, and you've never trained a model on your own data.

If that's you — and you learn fast — this is built for you.

---

## The North Star

The program is anchored to a real, demanding role — a **"Core AI Engineer"** who owns:
1. the **agent harness** (LLM orchestration, tool use, context construction, memory, guardrails, production reliability);
2. the **evaluation stack** (golden datasets, LLM-as-judge, human eval, A/B, regression tracking);
3. **prompt/behaviour engineering + RAG at scale** over a real domain (here: accounting/finance workflows);
4. **hosting & improving small models** (serving open-source LLMs, SFT/DPO/RL, and **document-extraction** models) for performance, cost & **sovereignty**.

Every day traces back to one of those. Full mapping in [`CURRICULUM.md`](CURRICULUM.md).

---

## The 4-week arc

| Week | Theme | You will be able to... | Capstone build |
|------|-------|------------------------|----------------|
| **1** | [Foundations & Fluency](plan/week-1-foundations.md) | Reason about LLMs from tokens up; wield the Claude API and Claude Code like a surgeon | A from-scratch chat CLI + your own tokenizer/cost explorer |
| **2** | [Agents & the Harness](plan/week-2-agents-and-harness.md) | Build an agent harness from zero: agent loop, tools, memory, guardrails, MCP | A mini coding agent (your own "Claude Code") |
| **3** | [Retrieval, Data & Evaluation](plan/week-3-rag-eval-data.md) | Ship RAG at scale (vector **and** graph), and run evaluation as a discipline | Production RAG over your own data + a CI eval harness |
| **4** | [Training, Serving & Production](plan/week-4-training-serving-capstone.md) | Fine-tune (SFT/LoRA/DPO), serve models cheaply, ship safely | **Capstone:** a production agentic product, end-to-end |

---

## Daily routine (the default shape of a day)

Target **~6 focused hours**. Adjust the block sizes, never skip the *Build* or the *Log*.

| Block | Time | What |
|-------|------|------|
| 🧠 **Theory** | ~1.5h | Read the day's material. Take notes *in your own words*. No passive watching. |
| 🔨 **Build** | ~3.5h | The day's hands-on challenge. This is where the learning actually happens. |
| 🚢 **Ship** | ~0.5h | Commit, push, tick the "Definition of Done". Public repo = accountability. |
| ✍️ **Log** | ~0.5h | Fill the [daily log](daily-log/TEMPLATE.md): what I built, what confused me, what I'll ask my mentor. |

**Rules of engagement**
1. **Build first, framework second.** Reach for LangGraph/LlamaIndex *only after* you've built the primitive by hand.
2. **Everything is committed.** Green squares are your streak. A day without a push didn't happen.
3. **Write to understand.** Every day ends with a log entry. Confusion logged today is a question for tomorrow.
4. **Ship ugly, then refine.** A working ugly thing beats a beautiful plan.
5. **Measure tokens & cost.** Every build reports its token usage and $ cost. Frugality is a skill here.

---

## The mentor protocol (how we work together)

This program assumes a mentor (human or an AI agent acting as one). Cadence:

- **Daily:** mentor reviews your commits + daily log, answers your logged questions, adjusts tomorrow if you're stuck or ahead.
- **Weekly retro:** score the week, review the capstone build, re-plan the next week based on reality.
- **Escalation:** if you're blocked >90 min, log it and move to the next task — don't grind silently.

> Working with Claude Code as your mentor? At the start of a day, point it at your latest `daily-log/` entry and this repo, and ask it to coach you through the day's build. It can pair-program, review your code, and quiz you Socratically.

---

## Quickstart

```bash
git clone git@github.com:danicuki/ai-zero-to-hero.git
cd ai-zero-to-hero

# 1. Do the Day 0 setup (accounts, keys, environment)
open plan/week-1-foundations.md   # → "Day 0" section

# 2. Baseline yourself — be brutally honest
open progress/skills-matrix.md

# 3. Start Day 1. Copy the log template for each day.
cp daily-log/TEMPLATE.md daily-log/day-01.md
```

---

## Repo map

```
README.md                     ← you are here
CURRICULUM.md                 ← gap analysis, philosophy, learning outcomes
plan/
  week-1-foundations.md       ← Day 0–7
  week-2-agents-and-harness.md← Day 8–14
  week-3-rag-eval-data.md     ← Day 15–21
  week-4-training-serving-capstone.md ← Day 22–30
projects/
  README.md                   ← the portfolio of builds + capstone spec
resources/
  papers.md                   ← the canon (read these)
  tools.md                    ← the stack (learn these)
  reading.md                  ← courses, blogs, docs
daily-log/
  TEMPLATE.md                 ← copy this each day
progress/
  skills-matrix.md            ← Day 0 vs Day 30 self-assessment
```

---

## License

MIT. Take it, fork it, walk the path. If it helps you, star it and pay it forward.
