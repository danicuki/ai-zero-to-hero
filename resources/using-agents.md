# Using coding agents during this program

> "Should I write every line, or use Claude Code?"

The most important pedagogical question in this curriculum, and both naive answers are wrong.

- **"Hand-write everything"** — absurd. You're training to be an agent-first engineer. Refusing to use agents is LARPing 2015, and the target role is about *building* agents, not typing.
- **"Delegate everything"** — you learn nothing. You end the month exactly where you started: fluent with tools you don't understand. **That is the duck problem with extra steps.**

## The principle

> ### The agent may never write the thing the day is designed to teach.

Every day has exactly one load-bearing concept — it's stated in the **Objective** and measured by the **Definition of Done**. That part is yours. Everything else is scaffolding.

**The checkable version:** *the agent may not write the code that the day's DoD tests.* If the DoD says "you wrote the loop yourself and can point to the line where a tool result re-enters the context" — then the agent writing that loop is not a shortcut, it's a **forfeit**.

---

## The five rules

### 1. Load-bearing code is yours. Scaffolding is free.
| Day | You write (load-bearing) | Delegate freely (scaffolding) |
|---|---|---|
| D1 `toktool` | token counting, cost math, the experiments | CLI plumbing, `rich` colorization, file I/O |
| D2 `nanogpt` | **every line of the model** — attention, the forward pass | plotting the loss curve, data download |
| D8 `miniagent` | the agent loop, the tool-result round-trip | the tool bodies (`read_file`, `list_dir`) |
| D19 `evals` | rubric design, judge validation, metric choice | CSV/JSONL wrangling, the report table |
| D26 `serving` | the benchmark methodology, the trade-off analysis | Dockerfile, load-test harness |

Typing `argparse` boilerplate is not learning. Delegate it and feel nothing.

### 2. First rep by hand. Later reps delegate.
The **first time you meet a concept**, hands on keys. Once you own it, delegate variations without guilt.

Write the agent loop by hand on **D8**. By **D12** (multi-agent) you own the loop — let the agent scaffold the orchestrator while you make the design calls. That's not cheating; that's the actual skill.

### 3. Agent-as-tutor is unlimited — and you underuse it.
This is the highest-value mode and it costs you no learning:
- *"Explain why my attention implementation is wrong — don't fix it."*
- *"Quiz me on KV-cache until I get it right."*
- *"Critique this design. What breaks at 100x scale?"*
- *"Review my code like a hostile staff engineer."*
- *"I think X. Argue the opposite."*

**Rule of thumb:** asking it to *explain, critique, quiz, or review* is always free. Asking it to *produce the day's concept* is always a forfeit.

### 4. The test: can you rewrite it from memory?
After any file lands, ask: **could I delete this and rewrite it from scratch?**
- **Yes** → you learned it. How it got typed is irrelevant.
- **No** → you *supervised* it. You didn't learn it. Go back.

### 5. Days 5–6 are the exception: the agent *is* the curriculum.
Claude Code mastery is the learning objective. Use it maximally, weirdly, and at its limits. That's the point.

---

## The failure mode to actually fear

You're fast, and the agent is good. So the trap isn't laziness — it's **velocity that feels like progress**:

> It works → you approve the diff → you feel productive → you learned nothing. Repeat six times → you cannot explain your own repo.

This is the single highest risk in this program for an experienced engineer, because you're *good enough at reviewing* to make plausible code pass. Plausible is not understood.

**The backstop is the daily quiz.** Your mentor asks you to explain what you built. You cannot fake that, and you cannot delegate it. If you can't answer, the agent wrote it — and the matrix score you give yourself on Day 30 is a lie you'll discover in an interview instead.

---

## The reframe that makes this fun

**You are living inside a reference implementation.**

Every day you use Claude Code, you are using *an agent harness* — the exact artifact you're building in Week 2 and reverse-engineering on Day 13. So use it **observantly**, like a mechanic driving a car:

- When it compacts context — *what did it choose to keep?* (D9)
- When a tool errors — *does it retry, re-plan, or halt?* (D10)
- When it spawns a subagent — *what context crossed the boundary, and what didn't?* (D12)
- When it's slow — *is it prefill or decode?* (D26)
- When it goes wrong — *was that a bad prompt, bad context, or a bad tool schema?* (D7, D9, D10)

Most people use an agent all day and learn nothing about agents. **Your daily tool use is field research for Week 2.** Keep notes; they feed `harness-teardown.md`.
