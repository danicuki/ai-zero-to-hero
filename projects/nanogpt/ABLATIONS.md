# How the model behaves (benchmark)

- run tests comparing different configurations and approaches.
- Benchmark Full Network (2500 steps): 
  - Final loss: 1.96
  - Time to Train: 1m
  - Text Quality: 
      - ✅ dates preserved, city name, 
      - ✅ correct Portuguese words
      - ✅ Portuguese-like words
      - ✅ poetry style preserved (small phrases on each line and strophes of 3-6 phrases)

## Remove residuals
Modification:
```
-        x = x + self.sa_head(self.ln1(x))
-        x = x + self.ffwd(self.ln2(x))
+        x = self.sa_head(self.ln1(x))
+        x = self.ffwd(self.ln2(x))
``` 
  - Final loss: 3.37
  - Time to Train: 1m (same)
  - Text Quality: 
      - ❌ no dates preserved, no city name 
      - ❌ incorrect Portuguese words
      - ❌ Portuguese-like words
      - 🌓  poetry style almost lost (short phrases on each line, no regular strophes)


## Remove Position embeddings
Modification:
```
-        pos_emb = self.position_embedding_table(torch.arange(T, device=device)) # (T, C)
-        x = token_emb + pos_emb # (B, T, C)
+        x = token_emb # (B, T, C)
``` 
  - Final loss: 2.23
  - Time to Train: 1m (same)
  - Text Quality: 
      - 🌓 dates almost preserved (São - 15/19999998?) 
      - ✅ correct Portuguese words
      - ✅ Portuguese-like words
      - ✅ poetry style preserved (small phrases on each line and strophes of 3-6 phrases)

## Drop to 1 head
Modification:
```
-        num_heads = 4
+        num_heads = 1
``` 
  - Final loss: 1.94
  - Time to Train: 41s (faster)
  - Text Quality: 
      - ❌ no dates preserved, no city name 
      - ✅ correct Portuguese words
      - ✅ Portuguese-like words
      - ✅ poetry style preserved (small phrases on each line and strophes of 3-6 phrases)


## Remove the masked fill (triangular matrix of 1s)
Modification:
```
-        wei = wei.masked_fill(self.tril[:T,:T] == 0, float('-inf')) # (B,T,T)
``` 
  - Final loss: 0.04 (curious)
  - Time to Train: 1m (same)
  - Text Quality: 
      - ❌ no dates preserved, no city name 
      - 🌓 rare but a few words
      - 🌓 Portuguese-like words, but words with too many letters 
      - 🌓  poetry style partially preserved (some strophes and lines too long or too short)

## Zero Dropout
Modification:
```
-        dropout = 0.3
+        dropout = 0.0
``` 
  - Final loss: 2.9 (decresed to 2.0 and increased back to 2.95)
  - Time to Train: 1m (same)
  - Text Quality: 
      - ❌ no dates preserved, no city name 
      - ✅ correct Portuguese words (fewer than benchmark but still ok)
      - ✅ Portuguese-like words (with a few aberrations like 'f:adaquela')
      - ✅ poetry style preserved (small phrases on each line and strophes of 3-6 phrases)
