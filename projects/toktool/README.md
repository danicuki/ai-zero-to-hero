# Learnings and answers
1 - strawberry is 3 tokens for gpt models and 2 tokens for gemini. That explains why model can't count 'r's, because some tokens have 2 r's on it, so it counts only one when it should count 2. Because there are no tokens for single 'r', all models can't count them.   
2 - hello has only 1 token on gpt and 2 tokens on gemini, no matter if it has space before or not. So counting is the same. But tokens differ. When there are spaces, the space are added to the token. So, for same word with and without space before, there are two different token IDs. So, in practice, the model answer will differ if there is a space on the left or not for the same wording. 

3 - 1234567 is 3 tokens for gpt models and 8 tokens for gemini. GPT2 and GPT-O200k_base separate numbers differently. So probably Gemini is a lot better are arythmetics, since it can recognize individual numbers and digits as separate entities, while GPT probably would fail to do so. 

4 - comparing stories in different languages:
 EN: gemini 820, o200k 805, gpt2 843 / avg: 823.33
 PT: gemini 927, o200k 893, gpt2 1412 / avg: 1077.33
 FR: gemini 929, o200k 874, gpt2 1354 / avg: 1052.33

 means english has less tokens to represent the same amount of chars.
 gpt2 uses much more tokens for pt and fr.

 so, old models (gpt2) are not that good at languages other than English. Modern models tend to have a smaller "non native English" tax compared to older ones.

5 - analysing code:  identation takes some token space
But this is not the most relevant discover. when there are multiple spaces, gpt2 tokenizes each one as separate tokens, while o200k not. For coding, multiple spaces are irrelevant and probable gpt2 will do worse coding.  
  

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

  So yaml seems to be the most efficient way to store this data, in terms of token count because json have so many ponctuation tokesn.  
   