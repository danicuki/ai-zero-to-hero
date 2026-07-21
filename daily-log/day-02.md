# Day NN — <title>

**Date:** 2026-07-21 · **Hours:** 8 · **Streak:** 2/30

## 🎯 Objective (one sentence)
Create my own nanogpt in Python using a char tokenizer

## 🧠 Theory — notes in my own words
<the 3–5 things I want to remember. If I can't explain it simply, I don't get it yet.>

## 🔨 Build — what I made
- Repo/artifact: `projects/nanogpt/...`
- What works:
- What I cut/skipped:
- **Numbers** (tokens / cost / latency / eval score):

## ✅ Definition of Done
- [ ] Met today's DoD (see the day's plan)
  - [x] write the initial version of model, looking only at bigram (only uses last char to predict next) 
- [x] Committed & pushed
- [x] Log written

## 😵 What confused me / where I got stuck
 - Python doesn't have tail recursion like Elixir. In Python, use for loops instead of recursion.
 - everything was new and confusing: batches, generate function, torch, nn, embedding table, (B, T, C), logits, Bigram, so many new jargons an conventions. 
 - Python variable scopes are function-wide, not branch wide like Elixir. Another lesson

## ❓ Questions for my mentor
1. All learnings above were questioned to the mentor along the lesson 
2. 'forward' has nothing to do with 'forward deploy engineer'

## ➡️ Carry-forward / tomorrow
<anything unfinished or to revisit>

## 💡 One insight I don't want to forget
 - bigram is interestion and enough to create Portuguese-like text, but it is still nonsense text, because it looks only at last char, with no broader context memory.
<the keeper>
