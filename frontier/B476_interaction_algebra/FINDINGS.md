# B476 — the "critical interaction algebra = SM gauge algebra" claim: refuted on all four numbers; the true structure is the parity-block arithmetic of the level

**Status: banked (frontier). Firewalled. Incoming: seat-1's 2026-07-08 claim ("36 = 4 × 9
= gl(2) ⊗ gl(3) ⊃ su(3)⊕su(2)⊕u(1) — the SM gauge algebra as a CONSEQUENCE"), flagged by
its author as needing exact verification. Verified same-hour: REFUTED. Ninth float-kill.
No H1.**

## The four numbers (exact SVD ranks, gaps ≥ 10⁻¹ → ≤ 10⁻¹⁵; `span_verify.py`)

| claim | exact |
|---|---|
| dim span{W₁ʲW₂ˡ} at level 15 = 36 | **49** |
| mod-3 factor = 4 = gl(2) | **5** = ℂ ⊕ M₂ (the parity blocks 1⊕2 of the level-3 Weil rep: scalar line on even, full 2×2 on odd) |
| mod-5 factor = 9 = gl(3) | **13** = M₂ ⊕ M₃ (parity blocks 2⊕3) |
| tensor factorization 4×9 = 36 | 5 × 13 = 65 ≠ 49 — **does not factor** (correlated exponents) |

The "rank 36 previously confirmed" was the MASTER-THEOREM divisor-cell count (36 = 6·6
gcd-classes, B474) — a count of cells, not an algebra dimension, and its factorization is
6×6, not 4×9.

## The kernel of truth, and why it launders

su(2) and su(3) DO sit inside the two CRT factors — as the odd parity blocks. But the
parity decomposition of the metaplectic representation at level N = pq has blocks of
dimensions (p±1)/2 and (q±1)/2 for ANY operators at that level: at 15 these are {1,2}
and {2,3}. **Finding 2- and 3-dimensional blocks at level 15 is the arithmetic of the
primes 3 and 5 — unavoidable, pair-independent, criticality-independent.** "The SM gauge
algebra emerges at the critical point" reduces to "the level is 15" — the
equivariance-inversion trap (B428-family) in its purest form: a structure you cannot
fail to find cannot fire. The su(3)×su(2)×u(1)-shaped naming is HELD-and-closed.

## Recorded as data

dim span at level 15 = 49; with Par-translates = 96; mod-3 with-Par = 8 (= the full
ℂ⊕M₂ ⊕ odd-parity extension), mod-5 with-Par = 23. The 49 < 65 deficit measures the
exponent correlation of the pair — unexamined, recorded without interpretation.

## Reproduce
```
python3 span_verify.py    # ALL CHECKS PASS
```

## Addendum (2026-07-08, the deep dive): locally full, globally locked

The parity-sector analysis (session log): the span's PROJECTION onto each of the four
parity sectors is the FULL block algebra (36, 16, 9, 4 — sum 65), while the span itself
is 49-dimensional: **the pair's algebra is full in every sector shadow but carries 16
exact linear correlations locking the sectors together.** The deficit is not a sterile
sector — it is inter-sector entanglement of the pair's exponents. Two notes: (i) the
sectors are not W-invariant in the theta convention because T₋ⱼ = Tⱼ + j — the B469
two-world (+j) obstruction in a third register; (ii) whether the 16 relations are
pair-specific or level-forced needs the (1,3)/(2,3) controls — the named follow-up.
