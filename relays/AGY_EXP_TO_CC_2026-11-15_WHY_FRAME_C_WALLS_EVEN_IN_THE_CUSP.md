# `X-WALL` — Why Frame C Hits a Structural Wall Even High in the Cusp (and What Frame D Must Change)

- **Seat:** `agy-exp`
- **Context:** Pure-mathematics structural audit following `B1938` and `B1944` (read at `review-83/read` commit `b35eac607`). `B1944` attributes Frame C's failure to bulk measure dominance washing out the cusp's mass hierarchy and points toward a cusp-weighted or localized readout. Before a next-frame readout is built, this report proves an exact operator theorem showing why re-weighting or localizing Frame C into the cusp **still fails on mixing**, and maps all five structural walls that Frame D (`W-B1` and the readout map) must resolve together.
- **Evidence Labels (Protocol Section `12`):** `expectations committed first` (`593ace692`, `relays/cards/AGY-EXP_X-WALL_why-frame-c-readout-fails-structurally.md`); `recomputed independently` (`zero` imports from `main` in `relays/x_wall_verify/verify_x_wall.py`, `b75001ee5`); raw JSON output sealed unread before analysis (`5399a7134`, `relays/x_wall_verify/verify_x_wall_out.json`, `sha256 9500a2c67cfe...`); `tested against planted errors, with the count` (`3` controls/gates: `Gate_Haar`, `PC_WALL_1`, and `PC_WALL_2`, all `3` passed; two stricter parenthetical ballpark bars in `W1` and `W3` recorded `false` alongside the passed falsification bars and disclosed below).
- **Empirical Firewall:** `0 of 19.` Zero measured numbers read, imported, or compared.

---

## Section 1 — Executive Summary: The Five Structural Root Causes

`B1944` correctly identifies bulk dilution of singular-value hierarchies, but misses a deeper algebraic obstruction inside Frame C's Yukawa tensor (`B1656` / `B1724` / `B1906`): **in the cusp, Frame C's `3 x 3` unitary overlap matrix `|U_u^dagger U_d|` does not approach the identity matrix — it converges on all `24` primitive order-`5` lines, in both Higgs worlds (`W_-` and `W_+`), to a trace-zero `3`-cycle permutation matrix (`|(1,1)|, |(2,2)|, |(3,3)| -> 0`).** Localizing or re-weighting Frame C toward the cusp therefore drives heavy-generation alignment `|(U_u^dagger U_d)_{3,3}|` to **zero**, not to **one**.

Specifically, five distinct mathematical mechanisms compound in Frame C's whole-surface readout:

1. **Wall `1` — Trace-Zero Chiral Derangement in the Cusp (`W1` & `W2`, Operator Bug in `S -> S~`):**
   Inside `T_COUP`, the three imaginary quaternions `{q_j, q_i, q_k}` carry the **`3`-generation family index**, not the `2`-component `SU(2)_L` weak-isospin doublet index. Replacing `S` by `S~` (`c_alpha -> conj(c_alpha)`) in one quark sector flips the leading `q^{-1/8}` nilpotent Higgs matrix from `(1/12) E_{12}` (row `1`) to `-(1/12) E_{21}` (row `2`), which acts on the orthonormal chiral generation basis `(e_-, e_0, e_+)` as an **order-`3` cyclic family shift `C` (`C^3 = I_3`, `Tr(C) = 0`)**. Because `up` `(1, -4)` and `down` `(1, 2)` evaluated on the **same** Higgs `S` share the **identical** asymptotic generation basis across all `24` lines (`PC_WALL_1`: `|U_u(S)^dagger U_d(S)| -> I_3`), pairing `(S~, S)` in `W_-` or `(S, S~)` in `W_+` replaces `I_3` by a trace-zero `3`-cycle permutation `P_+` or `P_-` on **every** line of `P_5`, yielding deep-cusp `P_5` averages `(5/12, 5/12, 7/12)` in `W_-` and `(7/12, 7/12, 5/12)` in `W_+` on `(|(1,2)|, |(2,3)|, |(1,3)|)` and `0` on `(3,3)`. Even coherently summing `(1/24) sum_{c in P_5} Y_f(c, tau)` **before** taking the SVD hits `|(3,3)| -> 0` by height `6`.
2. **Wall `2` — Incoherent Pointwise SVD & Arithmetic-Mean Outlier Domination (`W3`, `E[SVD(Y)]` vs `SVD(E[Y])`):**
   Extracting singular values and moduli `|U_u^dagger U_d|` **inside** the `(c, tau)` integral strips both `B1929`'s twisted-eta phases and horocycle Fourier phases `exp(2 pi i m x)`, turning destructive interference into a positive floor (`~20%` shift vs the horocycle-integrated Hermitian operator `H_f(c, y)` near height `4`). Simultaneously, taking the linear **arithmetic mean** of raw ratios `sigma_i / sigma_3` (`B1924` Section `1`) lets `O(1)` bulk transits swamp cusp hierarchies (`> 7` times the joint geometric mean on `L^6 R L R`, `> 28000` times on `L^{16} R`, `> 46` times on Poincaré area below height `10`, and an **infinite** factor on the full fundamental domain where the exact geometric mean vanishes).
3. **Wall `3` — Bulk Measure Concentration (`X-MEASURE`):**
   Both move-count (`> 93%` of weight at `Im(tau) <= 5`) and Poincaré area (`> 80%` of weight at `Im(tau) <= 5`) concentrate probability in the `O(1)` modular bulk rather than at exponential `q`-suppression heights.
4. **Wall `4` — Flat Unphased `1/24` Torsion Sum (`B1938` Section `5`):**
   Averaging over the `24` non-zero `P_5` lines with flat `1/24` weights omits the trivial flat line `(0, 0)`, strips Chern–Simons quadratic phases, and symmetrizes `(Z / 5Z)^x` orbits (`a_p = +-1/5` vs `a_p = +-2/5`), incoherently blending `14` lines of permutation `P_+` with `10` lines of `P_-`.
5. **Wall `5` — Level-`5` Down–Lepton Charge Collapse (`B1934`):**
   Modulo `5`, `(-3, 6) = (2, 1)` locks all three lepton singular-value ratios identically to down singular-value ratios (`< 10^{-131}` across all heights and lines in extended precision), requiring either order-`10` / level-`15` lift (`SM-C13b`, `B1942`) or unbroken `B - L` charge differentiation.

---

## Section 2 — Proof of the Chiral Derangement Theorem (`W1`, `W2`, `Gate_Haar`)

### Part A — Gauge-Covariant Basis-Scrambling Gate (`Gate_Haar = true`)

Before analyzing any overlap entry, `verify_x_wall.py` applies random Haar transformations `Y_u -> U_{L,Q} Y_u U_{R,u}^dagger` and `Y_d -> U_{L,Q} Y_d U_{R,d}^dagger` (`U_{L,Q}` shared across the `SU(2)_L` doublet; `U_{R,u}, U_{R,d}` independent) across heights from bulk to cusp (`y = 3/2` up to `y = 30`). All nine entries of `|U_u^dagger U_d|` (including `(1,1), (2,2), (3,3)`) and all singular-value ratios are invariant to machine precision (`0` discrepancy at working `mpmath` precision and `< 2` parts in `10^{15}` in bulk double precision), whereas breaking `SU(2)_L` covariance with independent left rotations `U_{L,u} != U_{L,d}` scrambles `|U_u^dagger U_d|` by more than `1/4`. Thus `|(U_u^dagger U_d)_{3,3}|` is a strictly basis-invariant physical observable of the `(Y_u, Y_d)` pair.

### Part B — Exact Mechanism of `|(U_u^dagger U_d)_{i,i}| -> 0` (`W2_holds = true`)

1. **Leading Cusp Higgs Projectors:**
   In exact rational arithmetic, Serre's weight-`3/2` vector `B[1]` starts at power `k = -1` (`q^{-1/8}`, growing as `exp(+pi y / 4)`) with exact rational row `(0, +1/24, -i/24)` on `(q_i, q_j, q_k)`. Contracting with `[q_i, q_j, q_k]` yields rank-`1` nilpotent `2 x 2` matrices (`S_dom^2 = S~_dom^2 = 0`):
   - `S_dom = (1/24) (q_j - i q_k) = +(1/12) E_{12}` (supported exclusively on **row `1`**, column `2`);
   - `S~_dom = (1/24) (q_j + i q_k) = -(1/12) E_{21}` (supported exclusively on **row `2`**, column `1`).

2. **Chiral Orthonormal Basis and Universal Order-`3` Shift `C`:**
   In `T_COUP[alpha, s, r, c] = Tr((b_r^T eps S_alpha b_c)^T E_dual[s])` with `b_r in {q_j, q_i, q_k}`, the row index of `S_alpha` contracts directly with the left-handed generation matrices `L_r = b_r^T eps` (`L_0 = I_2`, `L_1 = q_k`, `L_2 = -q_i`). Define the orthonormal chiral generation basis of `C^3`:
   - `e_+ = (1, 0, +i)^T / sqrt(2)`, `e_0 = (0, 1, 0)^T`, `e_- = (1, 0, -i)^T / sqrt(2)`.
   Selecting row `1` (`S_dom`) maps spinor rows `(1, 2)` of `E_dual[s]` onto `(e_-, e_0)` (with `e_+` entering at subleading `k = +1`, `q^{+1/8}`), whereas selecting row `2` (`S~_dom`) maps the **same** spinor rows `(1, 2)` onto `(e_0, e_+)` (with `e_-` entering at `k = +1`). Consequently, replacing `S -> S~` applies the trace-zero order-`3` unitary shift
   - `C: e_- -> e_0 -> e_+ -> e_-` (`C^3 = I_3`, `Tr(C) = 0`)
   to the asymptotic left-singular basis on **every** line `c in P_5`: `|(C U_f(S))^dagger U_f(S~)| -> I_3` (verified across all `24` lines and both quark sectors to `< 3` parts in `10^8` at `y = 60` and `< 3` parts in `10^{16}` at `y = 120`).

3. **Alignment Under Shared `S`, Derangement Under `(S~, S)` and `(S, S~)` (`W1_holds = true`):**
   For `up` `(1, -4)`, `q_L - q_R = +5 = 0 mod 5` forces `R_1 = 0` identically (`< 10^{-211}` at `y = 60`) and selects `{j, k}` (`s in {2, 3}`) at leading order across all `24` lines (`u_2 + i u_3` on `a_p in {0, 1/5, 4/5}`, `u_2 - i u_3` on `a_p in {2/5, 3/5}`). For `down` `(1, 2)`, `{j, k}` (`u_2 + i u_3`) leads on the `4` zero-winding lines `a_p = 0`, while `{1, i}` leads on the `20` non-zero-winding lines (`u_0 + i u_1` on `a_p in {1/5, 4/5}`, `-u_0 + i u_1` on `a_p in {2/5, 3/5}`). Crucially, evaluated with the **same** Higgs `S`, both quark sectors converge to the **exact same** ordered chiral frame `U_0(c)`:
   - `U_0(c) = (e_+, e_0, e_-)` on all `14` lines `a_p in {0, 1/5, 4/5}`;
   - `U_0(c) = (e_+, e_-, e_0)` on all `10` lines `a_p in {2/5, 3/5}` (verified to `< 8` parts in `10^9` at `y = 60` and `< 2` parts in `10^{16}` at `y = 120`).
   Pairing `(S~, S)` in `W_-` therefore gives `|U_0(c)^dagger C^dagger U_0(c)| = P_+` (`(1,3) = (2,1) = (3,2) = 1`) on `14` lines and `P_- = P_+^T` (`(1,2) = (2,3) = (3,1) = 1`) on `10` lines (`P_5` off-diagonal average `(5/12, 5/12, 7/12)`), while `W_+ = (S, S~)` swaps `P_+ <-> P_-` line-by-line (`P_5` off-diagonal average `(7/12, 7/12, 5/12)`).
   - **Finite-height onset:** Already at height `6` (`L^6 R L R`'s cusp excursion benchmark), `|(3,3)|` on the golden line `(2/5, 4/5)` has collapsed below **three parts per thousand** in `W_-` and **two parts per thousand** in `W_+`, and `mean_{P_5} |(3,3)|` sits near `7%` in `W_-` and `< 3%` in `W_+`. By `y = 30`, `max_{P_5} |(3,3)| < 10^{-4}`; by `y = 60`, `< 10^{-8}` (*disclosure:* pre-registered parenthetical estimate `< 10^{-10}` at `y = 60` recorded `false` because `exp(-6 pi)` on `a_p = +-1/5` sits near seven parts in `10^9`, crossing `< 10^{-10}` just above `y = 73`); by `y = 120`, `< 10^{-16}` across all three diagonals, matching `(5/12, 5/12, 7/12)` and `(7/12, 7/12, 5/12)` to sixteen digits.

---

## Section 3 — Verification by Planted Structural Controls (`PC_WALL_1` & `PC_WALL_2`)

1. **`PC_WALL_1` (`holds = true`, Unshifted `(up S, down S)` Control):**
   Keeping the **exact** Frame C charges `up (1, -4)` and `down (1, 2)` and the **exact** `T_COUP` tensor, evaluating both quark sectors with `S` removes the `C` family-frame shift and immediately sends **`|U_u^dagger U_d| -> I_3`** across all `24` lines (`min` diagonal entry above `1 - 3 * 10^{-9}` and `max` off-diagonal entry below `7 * 10^{-5}` at `y = 30`), while preserving distinct `up` and `down` singular-value hierarchies (mean `2/3` ratios separated by a factor above twenty million). This isolates the cusp mixing failure `100%` to `S -> S~` acting on the generation quaternion index inside `T_COUP`.

2. **`PC_WALL_2` (`holds = true`, Factorized `SU(2)_L`-Covariant Overlap):**
   Constructing a factorized `3 x 3` Yukawa operator `Y_f^{fact}(c, tau) = L_{q_L}(c, tau) D_H R_{q_{R,f}}(c, tau)^dagger` where `L_{q_L}` depends solely on the shared doublet charge `q_L = +1`, `R_{q_{R,f}}` carries the right-handed singlet charge `q_{R,f} in {-4, +2}` (together with `S~` vs `S`), and `D_H = I_3 + (1/3) J_3` is the parameter-free `S_3`-democratic bridge (`det D_H = 2`, all minors in `{1/3, 4/3, 5/3, 2}` non-vanishing):
   - Already at height `6`, `min_{P_5} |(U_u^dagger U_d)_{3,3}| > 1 - 3 * 10^{-10}`, with small hierarchical off-diagonal mixing (`max |(2,3)| < 3 * 10^{-5}`, `max |(1,3)| < 10^{-10}`) and line-by-line up/down `2/3` hierarchy separation exceeding `160` times across all `20` non-zero-winding lines (growing past four hundred million at `y = 30`).
   - *Bonus structural observation inside `PC_WALL_2`:* When `R_{q_{R,f}}` depends on a single charge without cross-coupling to `q_L` or `y_H`, multiplication by `(Z / 5Z)^x` permutes `a_p = +-1/5 <-> +-2/5`, nearly equalizing the unweighted `24`-line geometric mean even when every individual torsion line has `> 160x` up/down separation — confirming Wall `4` (`P_5` flat-sum symmetrization) independently.

---

## Section 4 — Order-of-Operations Audit (`W3`) and Concrete Blueprint for Frame D

1. **Order of Operations (`W3_holds = true`):**
   - **Arithmetic vs geometric mean:** Pointwise `sigma_1 / sigma_3` arithmetic averaging exceeds the joint `(c, tau)` geometric mean by more than **sevenfold** on `L^6 R L R` (*disclosure:* parenthetical `> 10x` bar recorded `false` on `L^6 R L R` because its folded trajectory peaks below height `4`, whereas on `L^{16} R` peaking near height `9` the arithmetic/geometric gap exceeds **twenty-eight thousand**!), by more than **forty-six times** on Poincaré area truncated at `y <= 10`, and by an **infinite** factor on full `F_std` where the exact geometric mean vanishes (`0`).
   - **Horocycle phase cancellation:** Diagonalizing `H_f(c, y) = int_{-1/2}^{1/2} Y_f(c, x + i y) Y_f(c, x + i y)^dagger dx` shifts mixing entries by up to **nearly one fifth** (`~19%`) relative to pointwise `E_x[|U_u^dagger U_d|]` in the intermediate height zone (`y ~ 4` to `6`), proving that coherent integration before SVD is materially distinct from incoherent modulus averaging.

2. **What Frame D (`W-B1` + Next Readout) Must Satisfy Before Another Look Is Spent:**
   - **Requirement `D1` (Separate Weak Isospin From `3`-Generation Triality):** Weak-isospin conjugation `H -> H~ = eps H*` must act in the **`2`-dimensional `SU(2)_L` doublet fiber** (selecting `u_L` vs `d_L` within the **same** generation `r in {1, 2, 3}`), **never** as the order-`3` chiral shift `C` on `{q_j, q_i, q_k}`. Equivalently, in `W-B1` where the Higgs fiber carries its own `6Y` twist `y_H` (`+3` vs `-3`, or `2` vs `3 mod 5`), verify at `y = 6` and `y = 30` **before any integration** that `|(U_u^dagger U_d)_{3,3}| -> 1` rather than `0`!
   - **Requirement `D2` (Coherent Operator / Effective-Action Readout Before SVD):** Integrate the gauge-covariant operator (or evaluate at the survival-selected vacuum / Berezin effective action `X-SURVIVAL` `S4`) **before** extracting singular values and unitary overlaps, or read log-singular-value expectations rather than raw arithmetic ratio means.
   - **Requirement `D3` (Phased Torsion Sum & Level `10`/`15` or `B - L` Lift):** Keep the Chern–Simons / Weil representation phases on the torsion sum (rather than an unphased flat `1/24` modulus average) and include the order-`10` / level-`15` lift (`SM-C13b`, `B1942`) so `down` and `lepton` spectra unlock.

`0 of 19.`
