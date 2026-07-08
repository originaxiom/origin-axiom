# B477 — the sterile-class table (recon; law OPEN)

**Question (owner's SM deep-dive cell): which SL(2) obstruction classes carry no
representations, and is there a law?** Data assembled from the banked B461 eliminations
(exact, per-class) + fresh introspection of the Ptolemy obstruction cocycles.

| manifold | classes | fertile (dim) | sterile |
|---|---|---|---|
| L6a4 (Borromean) | 8 | 0 (dim 1), 2 (dim 1), 4, 7 (points, ℚ(i)) | 1, 3, 5, 6 |
| s776 (chain control) | 8 | 0, 4, 6 (points, ℚ(√−7)) | 1, 2, 3, 5, 7 |
| m129 (Whitehead) | 4 | 0, 3 (points, ℚ(i)) | 1, 2 |

**Hint (L6a4, from the truncated cocycle window):** each sterile class = a fertile class
with exactly the s_1_1 and s_3_1 signs flipped — sterility looks like ONE ℤ/2 direction
in H²(M,∂M;ℤ/2). **But:** s776 has THREE fertile classes — not a power of 2, so fertility
is NOT a coset of a subgroup there; no linear law survives as stated. The honest state:
a suggestive pairing at L6a4, refuted as a universal linear law by s776's count.

Next (queued): full sign-vector extraction (the window shows 7 of ~30 entries), the
correct group structure on classes (cocycles multiply modulo face identifications), and
the per-cusp evaluation test. Recon only — nothing banked as law; scripts:
`sterile_law.py` (introspection), B461 `rung3_sl2_log.txt` (the exact dims).
