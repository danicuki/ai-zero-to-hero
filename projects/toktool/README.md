# Learnings and answers
1 - strawberry is 3 tokens for gpt models and 2 tokens for gemini. That explains why model can't count 'r's, because some tokens have 2 r's on it, so it counts only one when it should count 2.
2 - hello has only 1 token on gpt and 2 tokens on gemini, no matter if it has space before or not. 
3 - 1234567 is 3 tokens for gpt models and 8 tokens for gemini. GPT2 and GPT-O200k_base separate numbers differently. 
4 - comparing stories in different languages:
 EN: gemini 820, o200k 805, gpt2 843 / avg: 823.33
 PT: gemini 927, o200k 893, gpt2 1412 / avg: 1077.33
 FR: gemini 929, o200k 874, gpt2 1354 / avg: 1052.33

 means english has less tokens to represent the same amount of chars.
 gpt2 uses much more tokens for pt and fr.
5 - analysing code:  identation takes some token space
6 - comparing json and yaml and toml:
 - JSON:
   - Gemini: 301
   - O200k: 256
   - GPT2: 367
   - avg: 308
 - YAML:
   - Gemini: 233
   - O200k: 202
   - GPT2: 232
   - avg: 222.33
 - TOML:
   - Gemini: 254
   - O200k: 207
   - GPT2: 267
   - avg: 242.66

  So yaml seems to be the most efficient way to store this data, in terms of token count.
   