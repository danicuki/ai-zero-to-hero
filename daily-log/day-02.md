# Day NN — <title>

**Date:** 2026-07-21 · **Hours:** 8 · **Streak:** 2/30

## 🎯 Objective (one sentence)
Create my own nanogpt in Python using a char tokenizer

## 🧠 Theory — notes in my own words
 - remove the masked fill made model to cheat (know the 'invented' future and predict using its own 'invented' prediction): loss went to zero, but quality was terrible. So, loss = 0 sometimes doesn't mean good.
 - pytorch has all different tooling available to compose neural networks in an 'easy' way. 
 - matrix multiplication needs GPU + memory speed. CPU makes it slower, low memory bandwidth also.
 - multiple heads don't help at this small scale amount of data. 

## 🔨 Build — what I made
- Repo/artifact: `projects/nanogpt/...`
- What works:
  - run `python3 nanogpt_v3.py` and you get my poetry catalog as a training data for the model, which generates a nice Portuguese poetry-like text with a few imperfections, but much better than random text. It actually learned from the training data.
- What I cut/skipped:
  - I got the whole picture but still strugling to memorize some details, too much information for a single day, so I will revisit things in future to fixate
- **Numbers** (tokens / cost / latency / eval score):
  - See '../projects/nanogpt/ABRATIONS.md' for more

## ✅ Definition of Done
- [x] Met today's DoD (see the day's plan)
- [x] Committed & pushed
- [x] Log written

## 😵 What confused me / where I got stuck
 - Python doesn't have tail recursion like Elixir. In Python, use for loops instead of recursion.
 - everything was new and confusing: batches, generate function, torch, nn, embedding table, (B, T, C), logits, Bigram, so many new jargons an conventions. 
 - Python variable scopes are function-wide, not branch wide like Elixir. Another lesson
 - So many different concepts to absorb. 

## ❓ Questions for my mentor
1. All learnings above were questioned to the mentor along the lesson 
2. 'forward' has nothing to do with 'forward deploy engineer'
3. How much of this will I need in future weeks? 
4. Is this foundation enough for getting an AI Engineer job (given I already have experience in other areas and can learn fast)?  

## ➡️ Carry-forward / tomorrow
 - almost the whole less will need revisiting. This is dense

## 💡 One insight I don't want to forget
 - bigram is interestion and enough to create Portuguese-like text, but it is still nonsense text, because it looks only at last char, with no broader context memory.
 - memory bandthwidth is usually the bottleneck for ML training speed. It doesn't help to add more CPUs or GPU if your memory is slow. Go for faster memory bus instead of faster GPU if you want performance. 
 - torch is a nice library to build neural networks. I learned that it is just simple a composition of different kinds of nn that you can compose, like pieces of a Lego, in the end you have a "black-boxed" software that takes input in and sends outputs out.
 - loss = 0 doesn't mean quality
