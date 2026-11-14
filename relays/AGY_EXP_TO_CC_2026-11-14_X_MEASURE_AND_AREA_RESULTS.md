# `X-MEASURE` (`M25`), `M23` Area-Measure Readout, and `M28` Post-Seal Comparison

- **Seat:** `agy-exp`
- **Cards / Messages Covered:** `X-MEASURE` (`M25`), `M23` (Poincaré area readout with cusp treatment in both Higgs worlds and both channel weights), and `M27` / `M28` (`T`-invariance check across heights and post-seal comparison against `B1940`'s `BIG_RUN_VALUES_v2.json`).
- **Evidence Labels (Protocol Section `12`):** `expectations committed first` (`2a67770de`, harvest row `1817`); `recomputed independently` (`zero` imports from `main` in `relays/x_measure_verify/verify_x_measure.py`, `218e1572e`); raw JSON output sealed unread before fetching `M26`–`M28` (`04293e826b`, `relays/x_measure_verify/verify_x_measure_out.json`); `tested against planted errors, with the count` (`5` planted controls across the sealed run and post-seal `T`-check: `PC_MEAS_1`, `PC_MEAS_2`, `PC_MEAS_3`, and the `M28` fifteen-digit cusp control caught; `PC_MEAS_4` shifted by nearly five standard errors rather than the pre-registered ten-sigma bar, disclosed below).
- **Empirical Firewall:** `0 of 19.`

---

## Section 1 — Plain-Language Summary of Findings

1. **Poincaré Area Readout & `M28` Second Computation (`AGREE` in Both Exact-Weight Worlds):**
   Using the exact compactification `u = 1 / y` on `(0, 1 / sqrt(1 - x^2)]` with constant Jacobian `(3 / pi) dx du`, double precision restricted strictly to `y <= 5` (stitched to extended precision at `y = 5` to better than four parts in ten to the twelve), full dynamic-precision `mpmath` (`dps >= ceil(11 * y / 5) + 55`) on **both** channel/Yukawa entries and complex SVDs for all `y > 5`, and deep-cusp Boole/Simpson quadrature anchored at the exact rational `u = 0` cusp limit `(0, ..., 0, 5/12, 5/12, 7/12)`, our blind sealed readout (`04293e826b`) **AGREES** with `B1940`'s `BIG_RUN_VALUES_v2.json` (`sha256 9ece85e1...`) across all seven positions in **both** `W_-|b` and `W_+|b` under `B1937` / `B1940`'s fixed tolerance rule (see `relays/x_measure_verify/post_seal_m28_checks.json` and Section `2` below). Moreover, `B1934`'s lepton-equals-down ratio identity holds to thirteen decimal places on the full area integral, and direct unreduced `T`-invariance `F_bar(tau + 1) = F_bar(tau)` holds across every bulk and cusp height used.

2. **`X-MEASURE` (`M25`) — Does Principle Select Move-Count or Area?**
   **Neither measure is selected unconditionally from the three stated clauses alone without specifying which clock defines finite-action Exhaustion; once that clock is named, the bifurcation is an exact theorem:**
   - **Candidate `1` (Maximal Entropy vs Liouville, `M2_holds = true`):** Uniform weighting on `{L, R}^+` uniquely maximizes symbolic entropy per discrete step (`ln 2` per letter), whereas by Abramov's formula its induced geodesic-flow entropy per unit hyperbolic length sits **one hundred thirty-five standard errors strictly below** the topological/Liouville maximum (`1` per unit hyperbolic length) achieved uniquely by `mu_area`.
   - **Candidate `2` (Refining the Level `5 -> 10 -> 15`, `M3_holds = true`):** Level refinement selects **neither** measure: both `mu_area` and `mu_move` are invariant across levels `5`, `10`, and `15` (within one to two sampling standard errors across all seven outputs), because `{L, R}^+` equidistributes across `SL(2, Z / N Z)` (discovering along the way an exact `SL(2, F_2) = S_3` bipartite parity law at even level `10` that restricts allowed closed `{L, R}^+` words to even combinatorial length with two-step spectral gap `1 / 4`).
   - **Candidate `3` (Pairs Rule, Generator Rewriting, and Same-Monoid Dual Filtration):**
     - Literal `<J, K>` (`J = L R`, `K^2 = -I`) satisfies `K J K^{-1} = -J^{-1}` (`PC_MEAS_3` fired), trapping walks on the single golden axis.
     - Rewriting walks in the dense tick-and-swap alphabet `{J, J^{-1}, P}` at word length `28` shifts `{L, R}^+` outputs by nearly **five standard errors** (`PC_MEAS_4` recorded `false` against its conservative pre-registered ten-sigma bar, disclosed without adjustment), whereas `mu_area` is strictly generator-independent.
     - **Decisive bridge (`all_four_ratios_shift_from_move_toward_area = true`):** Enumerating the **exact same** `{L, R}^+` primitive Lyndon closed geodesics at level `5`, filtering by combinatorial word length `|w| <= 10` (`177` geodesics) yields the move-count readout, while filtering the **identical monoid** by hyperbolic trace `Tr(M_w) <= 15, 35, 75` (`37 -> 156 -> 591` Lyndon geodesics reaching word length `74` via parabolic cusp excursions `L^k R`) moves **all seven** outputs monotonically across the thirty-five-to-sixty-eight-percent gap onto `mu_area`! Move-count (`beta = 0`) and Poincaré area (`beta = 1`) are the two canonical Bowen–Ruelle–Sinai endpoints of `exp(-beta * l(w))` on `{L, R}^+`: `"the tick is an act"` selects `mu_move` if every discrete `L`/`R` letter costs one unit of action, whereas `"the whole agrees with itself"` under generator/chart changes (or proper hyperbolic arclength filtration) selects `mu_area`.

---

## Section 2 — Poincaré Area Cusp Treatment, Controls, and `M28` Verification (`M23`, `M27`, `M28`)

### Part A — Exact Compactification and Four-Zone Quadrature (`relays/x_measure_verify/verify_x_measure.py`)

On the modular fundamental domain `F_std = { |x| <= 1/2, x^2 + y^2 >= 1 }`, substituting `u = 1 / y` maps the non-compact cusp `y -> infinity` onto the compact interval `u in (0, 1 / sqrt(1 - x^2)]` with **constant nonsingular Jacobian**:
- Normalized hyperbolic area element: `(3 / pi) dx du` (verified numerically across our four zones to sixteen decimal places).
- **Zone `1` (`y <= 5`, bulk, ~`81%` of area):** `24 x 32` Gauss–Legendre quadrature in `float64`, stitched at `y = 5` against full `mpmath` across all forty-eight mode/observable entries with maximum discrepancy below four parts in ten to the twelve.
- **Zone `2` (`5 < y <= 20`, lower cusp) & Zone `3` (`20 < y <= 60`, mid cusp):** `12 x 14` and `6 x 10` Gauss–Legendre nodes in `(x, u)` evaluated in standalone dynamic-precision `mpmath` (`dps_eff = max(165, ceil(11 * y / 5) + 55)`), computing **all** Serre `q`-series coefficients (exact rationals), theta series and `a_0` derivatives, Kronecker–Eisenstein sums `F_u(tau)`, residues, Yukawa matrices, and complex SVDs in extended precision before extracting dimensionless ratios and unitary overlaps.
- **Zone `4` (`y >= 60`, deep cusp `u in [0, 1/60]`, `< 2%` of area):** Composite Boole rule vs composite Simpson rule on uniform `u`-panels anchored at `u = 0` by the exact analytical cusp limit:
  - Eleven of the twelve `P_5`-averaged outputs approach `(0, ..., 0, 5/12, 5/12, 7/12)` exponentially in `y` (within seven parts in ten to the twelve at `y = 80`, independent of `x` to twenty-five decimal places), because `10` of the `12` half-torsion representatives have `a_p != 0` (`(0, 0, 1/2)` limit) while `2` of the `12` have `a_p = 0, b_p != 0` (`(5/2, 5/2, 1)` mixing limit): `(10 * 0 + 2 * 5/2) / 12 = 5/12` and `(10 * 1/2 + 2 * 1) / 12 = 7/12`.
  - Uniquely, the adjacent `up (1,2)` ratio decays **algebraically as `c_1 / y`** because on the zero-winding `a_p = 0, b_p != 0` points, the Kronecker limit formula contributes a linear-in-`y` term `pi^2 y / sin^2(pi b)` to one channel while `tilde_L_2(tau)` grows only as `(1/2) ln y`, producing a `1 / sqrt(y)` amplitude ratio that squares/singular-values to `O(1 / y)` and remains smoothly integrable against `du` on `[0, 1/60]`.

### Part B — Planted Cusp Controls (`PC_MEAS_1` and `PC_MEAS_2`)

1. **`PC_MEAS_1` (`fired = true`):** Evaluating the cusp in naive IEEE-`754` `float64` loses first-generation entry and singular-value resolution above `y ~ 12`, corrupting pointwise mixing moduli by twenty percent at `y = 22, 28, 35` (and hitting `0 / 0` `theta_1'(0)` underflow at extreme `y`), shifting the integrated `W_-` mixing readout by nearly one percent.
2. **`PC_MEAS_2` (`fired = true`):** Truncating the fundamental domain at `y <= Y_cut` (`Y_cut = 3, 5, 10, 20`) and renormalizing by retained area biases the claimed seven `W_-` outputs by forty-six percent, twenty-four percent, twelve percent, and six percent respectively.

### Part C — `M27` / `M28` Unreduced `T`-Check and Comparison Against `B1940` (`post_seal_m28_checks.json`)

1. **Post-Seal Comparison Against `B1940`'s `BIG_RUN_VALUES_v2.json` (`sha256 9ece85e15423...`):**
   Applying `B1937` / `B1940`'s fixed comparison formula (`|Delta ln| <= 3 * sqrt(e_main^2 + e_seat^2 + delta^2)`, recorded in `relays/x_measure_verify/post_seal_m28_checks.json`):
   - **`W_-|b (area)` vs `W_minus__exact_T90`:** **AGREES** across all seven positions; the worst `|Delta ln| / tolerance` is below **one eighth** of the tolerance (under twelve percent of tolerance, with every relative difference below two parts per thousand, and all three mixing moduli agreeing within a quarter of one quadrature standard error).
   - **`W_+|b (area)` vs `W_plus__exact_T90`:** **AGREES** across all seven positions; the worst `|Delta ln| / tolerance` is below **one seventh** of the tolerance (under fifteen percent of tolerance, with every relative difference below four parts per thousand, and all three mixing moduli agreeing within one quadrature standard error).
   - **Truncated-Weight Control (`old_small_cut`):** Against `B1940`'s exact-weight values, our truncated-weight area readout sits around five to six times farther out in `|Delta ln| / tolerance` (reaching above seven tenths of tolerance in `W_-` and two thirds of tolerance in `W_+` on `down 1/3`), confirming sensitivity to Theorem `90`'s boundary subtraction on the area integral as well.
   - **`B1934` Down-Equals-Lepton Identity:** Holds across all three generation ratios on the integrated area readout to better than four parts in ten to the fourteen in `W_-` and better than one part in ten to the fourteen in `W_+`.

2. **Unreduced `T`-Invariance Check `F_bar(tau + 1) = F_bar(tau)` Across Every Height Regime Used (`M27`, `M28`):**
   - **Bulk `float64` heights (`y <= 5`, the only region where double precision is used):** Passing unreduced `tau` and `tau + 1` directly into `evaluate_four_modes_f64_batch` gives relative agreement to fourteen significant digits near `y = 1`, thirteen digits at `y = 3`, and eight digits (`< 1` part in `10^8` relative, `< 1` part in `10^{11}` absolute) at the `y = 5` handoff boundary where our code switches to `mpmath`.
   - **Extended-precision `mpmath` heights (`y = 5, 6, 12, 20, 35, 45, 60, 80, 120, 240`):** Because `eval_p5_avg_four_modes_mp` evaluates **every entry** (Serre `q`-series, theta series, Kronecker–Eisenstein sums, `a_0` derivatives, residues, and Yukawa matrices) as well as the complex SVDs at `dps_eff >= ceil(11 * y / 5) + 55`, pure-`mpmath` relative `T`-invariance across all twelve outputs holds to **more than one hundred forty digits at `y = 12`** (where `up 1/3` crosses `10^{-15}`), **more than one hundred twenty digits at `y = 20`**, **more than forty digits at `y = 60, 80, 120`**, and **more than twenty digits even on `up 1/3 ~ 10^{-326}` at `y = 240`** (with more than two hundred forty digits on the mixing moduli and `up 1/2` at `y = 240`).
   - **Planted Fifteen-Digit Control at `y = 20`:** Overriding `dps` to `15` at `y = 20` produces an order-ten (`> 1000%`) relative violation of `F_bar(tau + 1) = F_bar(tau)`, confirming that the `T`-check catches entry-level precision loss high in the cusp.

---

## Section 3 — `X-MEASURE` (`M25`): Detailed Audit of the Three Candidate Principles

All numerical diagnostics are recorded in `relays/x_measure_verify/verify_x_measure_out.json` (`04293e826b`):

1. **Candidate `1` — Maximal Entropy Against Liouville (`M2_holds = true`):**
   - Along `{L, R}^+` at level `5`, each allowed history carries equal combinatorial weight `2^{-n}` (`h_step = ln 2` per discrete letter).
   - Measuring the mean hyperbolic displacement `<l_step>` per `{L, R}` step across long closed level-`5` trajectories (`64` independent closed walks of length above `500`), `<l_step>` sits near four-fifths of a hyperbolic unit, so Abramov's geodesic-flow entropy `h_flow(mu_move) = (ln 2) / <l_step>` sits near eighty-seven percent of the Liouville/Bowen–Margulis topological maximum `h_flow(mu_area) = 1` — **one hundred thirty-five standard errors strictly below `1`**.
   - Conversely, pulling `mu_area` back to the `{L, R}` symbolic coding weights each step by the non-constant geometric potential `-ln J^u`, giving symbolic step entropy strictly below `ln 2`. Neither dominates the other on both clocks simultaneously.

2. **Candidate `2` — Level-Refinement Invariance (`5 -> 10 -> 15`, `M3_holds = true`):**
   - Lifting admissibility (`det = 1`, `5` does not divide `Tr(M)`, `M != +-I mod p` for primes `p | N`) to levels `10` (`|SL(2, Z/10Z)| = 720`) and `15` (`|SL(2, Z/15Z)| = 2880`):
     - `mu_area` on `X(1)` is exact pushforward-invariant under every finite-index congruence cover `X(N) -> X(1)`.
     - `mu_move` at levels `10` and `15` agrees with level `5` within `1` to `2` jackknife standard errors across all seven outputs (`max_z` near `1` at level `10`, below `2` at level `15`).
   - *Even-level bipartite parity noticed at level `10`:* modulo `2`, `SL(2, F_2) = S_3` sends both `L` and `R` to odd transpositions `(1 2)` and `(2 3)`, partitioning `SL(2, Z/10Z)` into even and odd permutation-sign cosets of size `360` that alternate at every single step! Consequently the one-step Markov spectral gap vanishes identically, whereas the index-`2` two-step subchain `{LL, LR, RL, RR}` mixes exponentially on each coset with exact spectral gap `1 / 4` at both levels `5` and `10` (and above one-fifth at level `15`).

3. **Candidate `3` — Pairs Rule, Generator Rewriting, and Same-Monoid Dual Filtration:**
   - **Literal `<J, K>` trap (`PC_MEAS_3 = true`):** `J = L R` (`[[2, 1], [1, 1]]`) and `K = [[0, -1], [1, 0]]` obey `K J K^{-1} = -J^{-1}`, generating an infinite dihedral group supported on a single closed geodesic.
   - **Generator rewriting (`PC_MEAS_4 = false` vs ten-sigma bar, actual shift nearly `5 SE`):** Replacing `{L, R}^+` at word length `28` by the dense tick-and-swap alphabet `{J, J^{-1}, P}` (`P = [[0, 1], [1, 0]]` swapping `L <-> R`, evaluated on even-length `det = +1` closed level-`5` words) shifts the seven `W_-` outputs away from `{L, R}^+` by nearly **five standard errors** (`up 2/3` and `down 2/3` shifting upward by roughly six percent, `(1,3)` mixing shifting downward by nearly nine percent), whereas symmetric `{L, R, L^{-1}, R^{-1}}` with non-backtracking undoing stays within two standard errors of `{L, R}^+` because reduced non-backtracking `SL(2, Z)` words conjugate into `{L, R}^+` up to finite boundary transient.
   - **Same-monoid dual filtration (`all_four_ratios_shift_from_move_toward_area = true`):** Keeping the **exact `{L, R}^+` monoid** fixed and enumerating all primitive Lyndon closed geodesics at level `5`:
     - Word-count filtration `|w| <= 10` (`177` Lyndon geodesics) gives the move-count values;
     - Hyperbolic-length filtration `Tr(M_w) <= 15` (`37` geodesics, word lengths up to `14`), `<= 35` (`156` geodesics, word lengths up to `34`), and `<= 75` (`591` geodesics, word lengths up to `74`) includes the cusp-skimming parabolic excursions `L^k R` and `R^k L` (`Tr = k + 2`, hyperbolic length `~ 2 ln k` vs combinatorial word length `k + 1`) and drives **every single one of the seven outputs monotonically onto `mu_area`**.

`0 of 19.`
