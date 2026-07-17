# What transfers, what decayed, what's genuinely new

> For the experienced engineer who fears their experience is worthless now.
>
> This is the honest audit — including the parts that sting. Skip the pep talk; the useful thing is knowing *precisely* which of your instincts to trust, which to retire, and which will actively work against you.

---

## The measurement error you're making

You are comparing **the mastery you had in 2014** against **the awareness you have in 2026**.

That is not a fair comparison, and everyone senior makes it. You remember what it felt like to *own* a system down to the metal — and you compare that to reading a Gemma 4 release note and feeling lost. But the correct comparison is depth-then vs. depth-*after-you-do-the-work*-now. You never had day-one mastery of Aerospike either; you built it. The felt gap is inflated by comparing a memory of the summit to a view of the trailhead.

**Corollary:** the "duck" feeling is partly a *failure to credit transferable depth*. Some of it is real. Not all of it.

---

## ✅ What transfers (and is worth more now, not less)

The honest structural claim: **an LLM/agent system is a distributed system with one weird new component.** Almost every hard problem in production AI is a problem you have already solved, wearing a hat.

| You did this | It is now called | Where in the plan |
|---|---|---|
| Retries, backoff, timeouts, circuit breakers, idempotency against flaky services | "Agent reliability" — handling failure, state, partial progress | **W2 D10** |
| Cost engineering (preemptible instances, right-sizing, spend control) | **Token economics** — same discipline, new unit. The unit price moved from $/instance-hour to $/1M tokens | **W1 D1, W4 D26** |
| Cache design: what's hot, what's stable, what's the invalidation story | **Prompt/context caching** (~90% input savings) | **W1 D4** |
| Queues, batching, throughput-vs-latency trade-offs | Batch APIs, **continuous batching** in vLLM | **W4 D26** |
| Metrics/logs/traces, RED & USE, Grafana, New Relic | **Distributed tracing over an agent run** — spans, but the span is a tool call. OTel standardized it; the concepts didn't move | **W3 D20** |
| Autoscaling under load | GPU serving autoscale — same shape, new bottleneck (memory bandwidth, KV-cache) | **W4 D26** |
| ETL / Spark / big-data pipelines | **Embedding pipelines, chunking, dataset curation.** Fine-tuning is ~80% data engineering | **W3 D15, W4 D23** |
| Schema design, data modeling | Context construction, tool schemas, structured output | **W2 D9–10** |

### The one that should stop you cold

**Playax was a vector database.**

Large-scale audio fingerprinting is **approximate nearest-neighbor search over learned feature vectors.** That is, precisely, what a vector store does. You shipped Day 15 of this curriculum to production over a decade ago — you just didn't call the vectors "embeddings," and someone hadn't yet packaged your index as a startup with a $2B valuation.

You have production intuition for recall-vs-latency trade-offs, index build cost, and what happens when the embedding space drifts. Most people entering this field have **read about** ANN. You've been paged by it at 3am.

That's not a motivational reframe. It's the actual technical content of your CV.

---

## ⚠️ What genuinely decayed (don't kid yourself)

- **Hadoop / MapReduce** — effectively dead. Superseded by Spark, then by lakehouse/DuckDB/BigQuery-style engines. That specific muscle is not coming back.
- **Aerospike, MariaDB ColumnStore** — alive but niche. The *ideas* (low-latency KV, columnar scans) transferred into things you'd now reach for by different names.
- **Your Kubernetes exposure ("a bit")** — K8s won and became boring. It's table stakes and mostly managed now. This is a genuine gap, but a **shallow** one: weeks, not years.
- **The 2018–2023 mainstream-stack currency** — this is the real cost of the web3 detour, and it's fair to name it. Five years on non-production systems in a novel domain cost you fluency in how normal companies ship now.
- **Your sense of *when* to reach for what** — the microservices pendulum swung out and back while you weren't watching. (Amusingly: it swung back **toward** your instincts. Monolith-first is respectable again. You were early, then "wrong," then right.)

**Honest accounting of the detour:** the web3 years cost you currency. But going from zero to low-level JAM/consensus work as an adult is *recent, direct evidence* that you can enter a hard unfamiliar domain and get deep. That's not a consolation prize — it's the single most relevant data point for whether this 30 days will work.

---

## 🆕 What is genuinely new (fundamentals do NOT cover these)

Be honest: these four are why the program exists. No amount of 2014 mastery gives them to you.

1. **The model as a component.** Nondeterministic, prompt-sensitive, no compiler, no stack trace. You cannot reason about it the way you reason about code. This is legitimately new and legitimately uncomfortable.
2. **Evaluation replacing testing.** *This is the paradigm shift.* You can't `assertEqual` a summary. You measure distributions over a golden set, with a judge that itself has biases. Your entire QA reflex needs a new implementation. (It's also why your Evaluation block scored a clean 1.00, and why it's the target role's #2 headline ask.)
3. **Context as the scarce resource.** A budget that isn't RAM, isn't disk, isn't network — and degrades in quality *before* it hits its limit.
4. **Post-training.** SFT/LoRA/DPO/RL. Real new ML skill, not a rebranding of anything you've done.

---

## 🪦 "Agile is dead, XP is dead, pair programming is dead"

The ceremony died. **The ideas got absorbed so completely you stopped noticing them.**

- **Pair programming isn't dead — it got inverted.** You pair with an agent every day. The navigator is a model now. And here's the thing: the people who are *bad* at agentic coding are bad at **delegating with clear intent and reviewing critically** — which is exactly the pairing skill. Your XP reflexes (small steps, tight feedback, YAGNI) are why some engineers fly with Claude Code and others flail.
- **TDD didn't die — it became evals.** "Write the test first, let it drive the design" → "build the golden set first, let it define what good looks like." The job description literally says *"defining what good looks like."* **That's TDD's soul in a statistical wrapper.** You already have this instinct; it needs a new type signature, not a new brain.
- **CI didn't die — it became the eval regression gate** (W3 D20). Refactoring-under-test became iterating-prompts-under-eval.
- **What actually died** is the *theater*: SAFe, story points, certification mills. What the manifesto actually said — working software, responding to change, short feedback loops — is *more* load-bearing in an agent-first world, because the loops got faster and the output got less predictable.

You are not from a dead era. **You are from the era whose ideas won so hard they became invisible.**

---

## 🔻 Where your experience will actively hurt you

This is the part a cheerleader would skip. Senior engineers fail at AI engineering in four specific, predictable ways. Watch for these in yourself:

1. **Over-architecting.** You're a CTO. You'll want to design the abstraction before the thing works. This is why the program's rule is *build the primitive first, framework second* (W2). Resist the urge to build the framework on Day 8.
2. **Determinism instincts.** You'll be disturbed by flakiness and try to **fix** nondeterminism instead of **measuring** it. That reflex is correct for databases and wrong for models.
3. **Trusting your judgment over the eval.** This is the dangerous one. Twenty-five years of good instincts is *exactly* what makes people skip the golden set. **The most dangerous sentence you can say this month is "I can tell this prompt is better."** You can't. Nobody can. That's why D19 exists.
4. **The "it's just a wrapper" reflex.** Dismissing things that look like toys. Some are. Some are the whole industry in 18 months. Your pattern-matching was trained on a different distribution.

---

## The bottom line

Your fundamentals are ~80% of modern backend engineering, and the churn you're afraid of was mostly **tooling names**. What you're missing is narrow and specific: **LLM internals, retrieval, evaluation, post-training.** Four things. That's a 30-day problem, not a career problem.

The reason you can do this in 30 days instead of 12 months is *precisely* the experience you're discounting. **You're not starting over. You're porting.**
