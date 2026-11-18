# SM-C22 — every Higgs vector in frame D1: can any give both an aligned cusp mixing and a cusp hierarchy?

*Card of the SM seat, 2026-11-18, on the author's "go", after SM-C21. Committed and pushed before any computation.
Frame-internal structure only. Main's closed form and its gate-5 contraction are imported unchanged. Nothing is set
beside a measured number, and no vector is offered as "the" Higgs.*

## 0. The derivation, before any computation

- **T1. No Higgs vector makes D1 single-valued in the point w.**
  - SM-C18: for odd Δ, moving w by 1 acts on the Higgs index as −Z³ (since (−1)^(i−j+m) = −(−1)^k), and moving it by τ
    acts as X³ (k → k + 3).
  - M = Y·v changes only by a phase under both exactly when v is an eigenvector of both Z³ and X³.
  - But Z³X³ = ζ₆⁹·X³Z³ = −X³Z³: they anticommute, and an eigenvector of one is sent by the other to the opposite
    eigenvalue.
  - So no common eigenvector exists, and no Higgs vector makes the frame's couplings functions of the point.
- **What remains is existence:** whether any v at all gives an aligned cusp mixing together with a hierarchy.
  - Single modes give permutations (B1957).
  - The tick-fixed v± give no hierarchy (SM-C21).
  - A scan maps the whole space between them.

## 1. What is computed

- **T1, numerically:** ‖Z³X³ + X³Z³‖, and the least, over random v, of the larger of the two phase-defects of M(w + 1)
  and M(w + τ) against M(w).
- **The scan.** The tensors Y(ξ_s) are computed once at the 24 points of order 5 (lift (0, 0)), for up and down, at
  heights 8 and 10 (main's Y_mp). They are then contracted with:
  - the 6 single modes;
  - the 6 eigenvectors of U_M;
  - the 3 pair-sums and the 3 pair-differences e_k ± e_(k+3);
  - 5 000 random unit vectors (seed 22).
- **For each v:**
  - the share of points with |V₃₃| > 0.99, the top-aligned share, at height 10;
  - the exponents E(s₂/s₁) and E(s₃/s₁) at the mark, from heights 8 to 10;
  - the median over the 24 points of E(s₃/s₁).
- **"Both":** the top-aligned share ≥ 0.5 and the median E(s₃/s₁) ≥ 0.1.

## 2. Expectations, written before any computation

| | expectation | prior |
|---|---|---|
| T1 | Z³ and X³ anticommute, and no v makes M single-valued (the least defect over random v stays of order 1) | 95% |
| S1 | no vector in the scan has both | 70% |
| S2 | hierarchy appears only for vectors concentrated on few modes, and those vectors' mixing is near a permutation | 60% |

## 3. What it means

- **If S1 holds:** frame D1 cannot give an aligned cusp mixing with a cusp hierarchy for any Higgs vector, and with T1
  it cannot be made single-valued either. D1 is then closed at the cusp in full, not only at its tick-fixed vacuum.
- **If S1 fails:** the vectors that do give both are listed and characterised. None is offered as the Higgs: picking
  one would be a selection after the fact, and the page says so.

## 4. Files

relays/sm_c22/, with its script, output and run. The page will be relays/SM_C22_EVERY_HIGGS_VECTOR_IN_D1.md.
