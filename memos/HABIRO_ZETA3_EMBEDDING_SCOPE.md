# R016 — the zeta-three Habiro correction reproduces, but only finitely

Main B1158 correctly identified outside-bench memo 69's level-15 collapse as a base-embedding
artifact.  The load-bearing computation was not present in B1158's own reproducer, so this cell
performs it exactly.

Let `w` be a primitive root of order `3*p^r`.  The abstract base root `zeta_3` must be embedded
as `w^e`, where `e` is either `p^r` or `2*p^r` and `e = 1 mod 3`.  With that compatible choice,
the exact resultant valuations of the Habiro Taylor remainder satisfy the declared finite
coherence gate at all four tested levels:

```text
level 15:  2,4,6,8,10,12,14,16
level 75:  2,4,6,8,10,12,14,16
level 21:  2,4,6,9,10,13,14,18
level 147: 2,4,6,9,10,13,14,18
```

The negative control deliberately uses the conjugate base root `w^5` at level 15 and reproduces
memo 69's `[2,0,...,0]` collapse through Taylor order 11.  The collapse is therefore an embedding
mismatch, not a Taylor-truncation effect.

The scope fence is essential.  The certificate computes `v_p` of a global resultant/norm on
four levels through order eight; it does not prove uniform transport for all primes, powers and
orders, and it does not by itself identify a normalized valuation at one chosen prime above `p`.
B1158's universal phrases “at every level” and “local v_pi=N” remain stronger than the shipped
computation.

Primary certificate: `certificates/r016_habiro_zeta3_embeddings.py`.
Captured output: `outputs/r016_habiro_zeta3_embeddings.txt`.
