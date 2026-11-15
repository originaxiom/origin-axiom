# B1949's card: the lepton–down relation in the frame, derived without data (P-862, step 2), sealed before its runs

*Main, 2026-11-15. Committed before any output is computed. No measured number is compared in this arc.*

## Foreknowledge, disclosed

Main knows that the measured lepton–down split is near a factor of 3 in the second generation: the Georgi–Jarlskog
factor, which the record names (B1729, P-294, P-355). Any later comparison of R4 with the data must count this as
part of a look already made. It must be ruled before any value is compared, and it counts in the look ledger's history.

## The claims to check (derived by hand, before any run)

- **R1, exact.** The frame's coupling depends on a sector only through (q_L·w, q_R·w): the characteristics
  twist_of(q w) = (q a, 2 q b). So for charges proportional by an integer k, Y_{kq}(τ, w) = Y_q(τ, k w), with k w not
  reduced mod 1.
  - The leptons are (−3, 6) = 3·(−1, 2).
  - So Y_lep(τ, w) = Y_{(−1,2)}(τ, 3w) exactly.
  - The sector (−1, 2) is the down sector with the doublet's sign negated. It is not the down sector.
  - **Expectation:** equal to roundoff, at three moduli and six points.
- **R2, exponents.** The cusp exponents depend on each leg's charge only through ‖2q α‖, which ignores the sign
  (B1788's closed form; the tropical rule, through E(q_L α, q_R α)).
  - So e_lep(α) = e_down(3α) for both generations, at every slope α.
  - **Expectation:** it holds for every α of denominator up to 30 in B1788's tropical.predict, and on frame C's cusp
    data (B1945) at orders 5, 10 and 15.
- **R3, levels.**
  - At a level N with 3 not dividing N, w ↦ 3w permutes the points of exact order N, so the lepton and down exponent
    multisets over the level coincide.
  - At 3 | N the leptons see the down exponents of order N/3 (B1942 at N = 15).
  - **Expectation:** holds at N = 5, 10, 15, 20, 30.
- **R4, the frame's Georgi–Jarlskog factor (no prediction).** In the cusp limit, the frame's (σ₂/σ₃)_lep divided by
  (σ₂/σ₃)_down, for frame C's average over the points of each level and for each Higgs reading pair, tends to a constant
  that does not depend on τ.
  - That constant is computed at heights 20, 30 and 40 in extended precision (40 + 3.5 Im τ digits), and its
    convergence is reported.
  - The same for σ₁/σ₃.
  - No value is set beside a measured number.

## What would refute the derivation

- R1 failing beyond roundoff, which would mean the frame depends on a sector through more than q·w.
- R2 failing at any α.
- R3 failing at any level.
