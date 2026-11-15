# Card `X-WALL` — Structural Diagnosis of Frame C's Whole-Surface Readout Wall (Data-Free, `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Following `B1944`'s reading of Frame C (`review-83/read` at `b35eac607`) and `B1938`'s dictionary, `B1944` attributes Frame C's failure to bulk dominance washing out the cusp's mass hierarchy and points toward a cusp-weighted or localized readout. Before any next-frame readout is built, this self-initiated pure-mathematics card tests whether Frame C's operator (`B1656` / `B1724` / `B1906`) can produce a near-identity `3 x 3` unitary overlap matrix even high in the cusp, and isolates the exact algebraic and order-of-operations mechanisms behind the wall.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no script for `X-WALL` has been written or run yet.
- **Empirical Firewall:** `0 of 19.` Zero measured numbers read, imported, or compared.

---

## Section 1 — Pre-Registered Mathematical Claims & Failure Criteria

1. **`W1` — Trace-Zero Chiral Derangement (`|(U_u^dagger U_d)_{i,i}| -> 0` for `i = 1, 2, 3`) Across All `24` Order-`5` Lines in Both Higgs Worlds:**
   - *Claim:* Ordering singular values ascending (`sigma_1 <= sigma_2 <= sigma_3`) in both quark sectors, on **every single one** of the `24` primitive order-`5` torsion lines `c in P_5` and in **both** Higgs worlds (`W_-` and `W_+`, under both Theorem `90` exact and truncated channel weights), **all three diagonal overlaps** `|(U_u^dagger U_d)_{1,1}|`, `|(U_u^dagger U_d)_{2,2}|`, and `|(U_u^dagger U_d)_{3,3}|` converge to **`0`** as `Im(tau) -> infinity` (`|(U_u^dagger U_d)_{3,3}| < 10^{-4}` already by `Im(tau) = 30`, and `< 10^{-10}` by `Im(tau) = 60`).
   - Specifically, in `W_- = (up S~, down S)`, the `3 x 3` modulus matrix `|U_u^dagger U_d|` converges on the `14` lines `a_p in {0, 1/5, 4/5}` to the trace-zero `3`-cycle `P_+` with `(1,3) = (2,1) = (3,2) = 1`, and on the `10` lines `a_p in {2/5, 3/5}` (including `(2/5, 4/5)`) to its transpose `P_- = P_+^T` with `(1,2) = (2,3) = (3,1) = 1`, yielding deep-cusp `P_5` average `(5/12, 5/12, 7/12)` on `(|(1,2)|, |(2,3)|, |(1,3)|)`. In `W_+ = (up S, down S~)`, `P_+` and `P_-` exchange line-by-line, yielding deep-cusp `P_5` average `(7/12, 7/12, 5/12)` on `(|(1,2)|, |(2,3)|, |(1,3)|)` and `0` on all three diagonals.
   - *Consequence if `W1` holds:* Re-weighting or localizing Frame C's `P_5` readout into the cusp (`Im(tau) >= 6`) **cannot** yield small `(2,3)` and `(1,3)` mixing moduli, because `|U_u^dagger U_d|` approaches a trace-zero `3`-cycle permutation matrix rather than the `3 x 3` identity matrix.
   - *Falsifies `W1` if:* Any order-`5` line in either `W_-` or `W_+` has `|(U_u^dagger U_d)_{3,3}|` staying above `1/10` at `Im(tau) = 30`, or if the `P_5` deep-cusp off-diagonal averages fail to match `(5/12, 5/12, 7/12)` in `W_-` and `(7/12, 7/12, 5/12)` in `W_+`.

2. **`W2` — Exact Quaternion Chiral-Ladder Mechanism (`S -> S~` Acts as an Order-`3` Family Shift Inside `T_COUP`):**
   - *Claim:* At leading cusp order `q^{-1/8}` (`k = -1` in Serre's weight-`3/2` vector `B[1]`, with exact rational row `(0, +1/24, -i/24)`), the holomorphic Higgs profile approaches the rank-`1` nilpotent `2 x 2` matrix `S_dom proportional to q_j - i q_k = 2 E_{12}` (supported on row `p = 1`), whereas Frame C's conjugate `S~_dom` (`c_alpha -> conj(c_alpha)`) approaches `q_j + i q_k = -2 E_{21}` (supported on row `p = 2`).
   - In the orthonormal chiral generation basis `e_+ = (1, 0, +i)^T / sqrt(2)`, `e_0 = (0, 1, 0)^T`, `e_- = (1, 0, -i)^T / sqrt(2)` of `C^3`, switching `S -> S~` inside `T_COUP` applies the universal order-`3` unitary shift `C: (e_-, e_0, e_+) -> (e_0, e_+, e_-)` (`C^3 = I_3`, `Tr(C) = 0`) to the asymptotic left-singular frame: `U_f(S~) -> C U_f(S)` on every `c in P_5`.
   - Meanwhile, evaluated with the **same** Higgs `S`, `up` `(1, -4)` (`R_1 = 0`, `{j, k}` leading on all `24` lines) and `down` `(1, 2)` (`{j, k}` leading on the `4` lines `a_p = 0`; `{1, i}` leading on the `20` lines `a_p != 0`) share the **identical** ordered asymptotic left-singular frame `U_0(c) = (e_+, e_0, e_-)` on `a_p in {0, 1/5, 4/5}` and `U_0(c) = (e_+, e_-, e_0)` on `a_p in {2/5, 3/5}`. Pairing `(S~, S)` or `(S, S~)` inside `T_COUP` therefore replaces `I_3` by `|U_0(c)^dagger C^{+-1} U_0(c)| in {P_+, P_-}`: weak-isospin conjugation was accidentally applied to the `3`-generation quaternion family space.
   - *Falsifies `W2` if:* Either the leading Serre `k = -1` Higgs row differs from `(0, +1/24, -i/24)`, or the asymptotic left-singular vectors on `P_5` fail to align with `{e_+, e_0, e_-}` and shift by `C` under `S -> S~`.

3. **`W3` — Arithmetic-Mean Outlier Domination & Incoherent Pointwise SVD (`E[SVD(Y)]` vs `SVD(E[Y])`):**
   - *Claim:* Across both closed hyperbolic geodesics (including `L^6 R L R`) and modular fundamental-domain quadrature:
     - **(a) Strict Jensen gap on singular-value ratios:** The linear arithmetic mean of pointwise singular-value ratios `E[sigma_1 / sigma_3]` (`B1924` Section `1`) exceeds the geometric mean `exp(E[ln(sigma_1 / sigma_3)])` by more than an order of magnitude (`> 10` times) on `L^6 R L R` and on the Poincaré area measure.
     - **(b) Horocycle phase cancellation before vs after SVD:** Integrating the gauge-covariant Hermitian operator `H_f(c, y) = int_{-1/2}^{1/2} Y_f(c, x + i y) Y_f(c, x + i y)^dagger dx` along the closed horocycle `x in [-1/2, 1/2]` before diagonalizing differs non-trivially in the bulk (`y = 3/2`) from averaging pointwise `|U_u^dagger U_d|` after SVD, while still converging to the same trace-zero derangement in the cusp because `W1` and `W2` already hold on the `x`-zero mode.
   - *Falsifies `W3` if:* Arithmetic and geometric means agree within a factor of `2` on `L^6 R L R` or Poincaré area, or `H_f` operator averaging equals pointwise SVD averaging at `y = 3/2`.

---

## Section 2 — Pre-Registered Basis-Invariance Gate & Planted Controls

1. **`Gate_Haar` (Gauge-Allowed Unitary Basis-Scrambling Gate):** Apply random common left-handed `U(3)` Haar transformations `U_{L,Q}` and **independent** random right-handed `U(3)` Haar transformations `U_{R,u}, U_{R,d}` (`Y_u -> U_{L,Q} Y_u U_{R,u}^dagger`, `Y_d -> U_{L,Q} Y_d U_{R,d}^dagger`); assert all `9` entries of `|U_u^dagger U_d|` (including `(1,1), (2,2), (3,3)`) and all singular-value ratios are invariant to `< 10^{-13}`.
2. **`PC_WALL_1` (Unshifted Family-Frame Control `(up S, down S)` Keeping Exact `(1, -4)` and `(1, 2)` Charges):** Keeping the exact Frame C charges `up (1, -4)` and `down (1, 2)` and the exact `T_COUP` tensor, evaluating both quark sectors with the **same** family-frame Higgs `S` removes the `C` rung shift and must send `|U_u^dagger U_d| -> I_3` (`|(1,1)|, |(2,2)|, |(3,3)| > 99/100` across all `24` lines at `Im(tau) = 30`) while preserving distinct up and down mass hierarchies.
3. **`PC_WALL_2` (Factorized `SU(2)_L`-Covariant Left-Right Overlap Control):** Constructing a factorized `3 x 3` overlap `Y_f^{fact}(c, tau) = L_{q_L}(c, tau) D_H(tau) R_{q_{R,f}}(c, tau)^dagger` whose left factor depends only on the shared doublet charge `q_L = +1` and whose right factor depends on `q_{R,f} in {-4, +2}` must likewise yield `|(U_u^dagger U_d)_{3,3}| -> 1` and suppressed off-diagonal mixing `(2,3), (1,3) -> 0` in the cusp while preserving distinct up and down hierarchies.

`0 of 19.`
