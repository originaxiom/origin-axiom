# Card W-F12: the doublets' class index at the odd levels, extended to level 7

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free). **Committed before any work of it.** It takes up one of
the structural items W-F10 left open: the class index n(V) − n(V* ⊗ w) is zero on every doublet at golden levels 1, 3
and 5 (W-C8 part 2a, post hoc 2), but it is not proved, and level 7 was not computed.

## The computation

- **Golden level 7** (fibre torsion 29, 1,682 characters with t-values the 2e-th roots), and every non-split doublet
  [[α, cβ], [0, β]].
- By W-F6's gap law, the extension characters ℓ = α/β with a non-coboundary class are the trivial one and the 28
  fibre-non-trivial ones with ℓ(μ) = −1. That gives 29 × 1,682 = 48,778 doublets. The law is also checked on all 1,682
  characters.
- For each doublet: the class index, and the h¹ gap h¹(V) − h¹(V* ⊗ w).
- **Control:** levels 3 and 5 must reproduce post hoc 2's counts (64 and 2,662 doublets; index 0 on all; the h¹-gap
  census).

## Method

Own code, exact ranks over a prime field; part 2a's helpers taken by text. Expectations in the script's header, sha256
recorded, committed and pushed before the one run.
