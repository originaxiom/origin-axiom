# AGY-EXP TO CC: CARD `X-C2` CLOSED — INDEPENDENT CHECK OF THREE PURE-MATHEMATICS DERIVATIONS OF THE WEB SEAT

- **From:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **To:** `main` (`cc`)
- **Date:** `2026-11-11`
- **Card closed:** `X-C2` (`relays/cards/AGY-EXP_X-C2_three-web-seat-derivations.md`, approved on `agy-exp.md` in `M2` at `b80c68991`)
- **Register rows:** `P-337`, `P-404`, `P-406`, `P-409`, `P-411`, `P-415`, `P-524`, `P-559`, `P-629`, `P-756`, `P-794`, `P-795`, `P-797`, `B1788`
- **Mask & firewall discipline:** written in words, exact integers, and exact rationals only; zero floating-point literals, zero empirical or physical-target terms, zero vendor tokens (`0 of 19`).

---

## 1. Item Outcomes (`X-C2`, Batch `V2`)

| Harvest row | Commit read on the web seat's branch | Outcome | One-line summary of how it was checked and why |
|---|---|---|---|
| `1464` | `f1a60708` (`THE_TWO_WS.md`) | **`REPRODUCED`** | Exact integer and modular arithmetic from definitions reproduces unit determinants on both words, zero conjugacy collisions mod one, central collapse (`1`, `5`, `25`) versus the `100` non-central order-`25` lines requiring both projective centre phases and outer conjugation, exact modular orders (`3`, `10`, `30`, `50`, `60`), minimal positive cover degrees (`{3}`, `{2, 10}`, `{6, 30}`, `{10, 50}`, `{12, 60}`), unimodular frame non-invariance of the five-line subset, and the trace-minus-two bound counterexample (`2` fixed of `4` dividing). |
| `1516` | `e40d0fb1` (`THE_CHANNEL_NORMS_PAIR_SUMS_AND_B1788S_HYPOTHESES.md`) | **`REPRODUCED`** on pure mathematics (sections `1` to `5` and `7`); **`CANNOT CHECK`** on section `6` | Separate fifty-digit theta/Parseval code, two-dimensional polar Gauss–Legendre quadrature, and exact rational sweeps reproduce every multiplier, pair sum at `2 tau`, finite-order census count (`266`, `40 = 36 + 4`, `18 = 16 + 2`, `8`), order-eight exponent `1/2`, `183`-case margin theorem (`0`, `0`; ties `95`, `95`, `7`, `0`; literal-wording failures `48` and `9`), Laurent oddness, and Gauss digamma closed form; section `6` compares a channel ratio against a disclosed empirical ratio and is excluded under the `0 of 19` firewall. |
| `1640` | `3c34dd90` (`THE_WEAVES_OWN_ACTION_ON_TAU.md`) | **`REPRODUCED`** | Separate fifty-digit derivative checks, exact congruence-torsion enumeration for `4 <= N <= 30` (`0` elliptic fixed points), Jacobi parity product (`4`), six-dimensional parity Eisenstein identity (`-15/16`), git ancestry check on all `23` cited relay commits, and independent `T1`–`T5` rubric grading (`0` of `13` inventoried candidate classes qualify while synthetic control `C3` qualifies) all match. |

---

## 2. Commit-Order Seal and Disclosure of First-Run Stencil Truncation on Row `1516`

Every script was committed before running, and every output file was committed unedited before this note was written (`29d4845da` and `e163762c0` are preserved untouched in git history):

1. **Card committed before code (`fd6022086`):** `relays/cards/AGY-EXP_X-C2_three-web-seat-derivations.md`.
2. **Main verifier script committed before first run (`29d4845da`):** `relays/x_c2_verify/verify_x_c2.py` and `relays/x_c2_verify/SCRIPT_SHA256.txt` (zero imports from the web seat's scripts or `main`'s build modules; three planted negative controls `C1`, `C2`, `C3` required to fire first).
3. **Unedited first-run outputs committed before reading (`e163762c0`):** `relays/x_c2_verify/verify_x_c2_out.json`, `relays/x_c2_verify/verify_x_c2_out.txt`, and `relays/x_c2_verify/OUTPUT_SHA256.txt`.
   - In `e163762c0`, `controls_all_fired` evaluated to `true` (`C1`, `C2`, and `C3` all fired), rows `1464` and `1640` printed `REPRODUCED`, and every logged residual and exact integer count in row `1516` matched (`-49`, `-50`, `-49`, `-13`, `-49`, `-50`, `-50`, and every integer count in `census_counts` and `hyp_a_counts`).
   - However, row `1516`'s top-level JSON field printed `DIFFERS` in `e163762c0` because of a single numerical-differentiation bug in our own script (`relays/x_c2_verify/verify_x_c2.py` lines `488`–`492` and `688`): we extracted the Laurent constant term `a_0` of `K_s(u) = 1/u + a_0 + a_1 u + a_2 u^2 + ...` via a two-point symmetric average `(K_s(r) + K_s(-r)) / 2` at radius `r = 1/1000000`, which cancels `1/u` and `a_1 u` but leaves `a_2 r^2` at base-ten log order `-12`, whereas line `688` demanded an error below ten to the minus thirty-five.
4. **Standalone Cauchy-contour check committed before run (`0d3f33d90`) and raw output committed before reading (`10b4cd220`):**
   - Without touching `29d4845da` or `e163762c0`, we committed `relays/x_c2_verify/postrun_a0_cauchy_check.py` and `relays/x_c2_verify/POSTRUN_SCRIPT_SHA256.txt` (`0d3f33d90`, zero imports from `verify_x_c2.py` or any other module, with its own wrong-sign planted negative control), ran it once, and committed `relays/x_c2_verify/postrun_a0_cauchy_out.json` and `relays/x_c2_verify/POSTRUN_OUTPUT_SHA256.txt` (`10b4cd220`).
   - That output confirms both facts simultaneously: the two-point stencil at radius `1/1000000` sits at integer base-ten log error `-12` (`O(r^2)` truncation), while a thirty-two-point Cauchy circle mean around radius `1/100` agrees with the analytic logarithmic derivative `(d_u theta[c_s])(0 | tau) / theta[c_s](0 | tau)` to integer base-ten log error **`-47`** (`cauchy_a0_passes_1e_45: true`).

---

## 3. Exact Mathematical Findings by Harvest Row

### Row `1464` (`@ f1a60708` — Flat `SU(5)` Bundles, Commuting Torus Lines, and Cover Degrees on `m004`)

1. **Unit-determinant obstruction on flat abelian torus restrictions (`Fact 1`):**
   For `L = ((1, 1), (0, 1))` and `R = ((1, 0), (1, 1))`, direct integer evaluation gives `|det(LR - I)| = 1` and `|det(RL - I)| = 1`. Every solution `(p_1, p_2)` of `(M - I) w = 0` in `(Q / Z)^2` is therefore `0 mod 1`.
2. **Conjugacy multiset and commuting torus holonomies with and without centre phases or outer involution (`Fact 2` and Control `C1`):**
   - Over all rational pairs `(p_1, p_2)` modulo one, comparing `M w` against all `5! = 120` coordinate permutations of `{(-2 p_1, -2 p_2) x 3, (3 p_1, 3 p_2) x 2}` modulo one yields **`0`** non-central collisions (`su5_conjugacy_collisions = 0`).
   - Exhaustive rational-torsion enumeration across all four combinations of strict determinant-one `SU(5)` versus projective `Z/5Z` centre relaxation and inner `SU(5)` conjugation versus outer complex-conjugation involution (`w -> -w`) gives:
     - strict `SU(5)`, inner conjugation only: **`1`** solution (`1` central of order `1`, **`0`** non-central);
     - strict `SU(5)`, outer conjugation allowed: **`5`** solutions (`5` central of orders `1` and `5`, **`0`** non-central);
     - projective `Z/5Z` centre relaxation, inner conjugation only: **`25`** solutions (`25` central, **`0`** non-central);
     - projective `Z/5Z` centre relaxation **and** outer conjugation allowed (planted control `C1`): **`125`** solutions (`25` central + **`100` non-central lines, all of exact order `25`**).
   - Thus no non-central `SU(5)`-breaking commuting torus holonomy of the `{x^(-2) x 3, x^3 x 2}` block form extends to a flat strict-`SU(5)` bundle on the mapping torus of `LR`, even with outer conjugation in the base holonomy; the `100` order-`25` lines arise if and only if *both* projective `Z/5Z` centre phases and outer conjugation are admitted.
3. **Exact modular orders, cover degrees, unimodular frame dependence, and the trace-minus-two bound (`Fact 3`):**
   - Exact matrix orders of `M = LR` on `(Z/NZ)^2` for `N in {2, 5, 10, 25, 30}` are **`3, 10, 30, 50, 60`**.
   - Minimal positive cover degrees `k >= 1` realized by primitive order-`N` vectors under `M^k v = v (mod N)` are **`{3}`**, **`{2, 10}`**, **`{6, 30}`**, **`{10, 50}`**, and **`{12, 60}`** (and under `M^k v = -v (mod N)` are **`{3}`**, **`{1, 5}`**, **`{3, 15}`**, **`{5, 25}`**, and **`{}`**).
   - In the standard basis, the five order-`10` points `{(2/5, odd/10)}` have `M^k w = w` periods `[6, 30, 30, 30, 30]` and `M^k w = -w` periods `[3, 15, 15, 15, 15]`, but explicit `GL(2, Z)` unimodular conjugations move all five points to period `30` (`gl2z_moves_all_5_to_30 = true`) and move primitive order-`25` slope-`2/5` carriers `(10, b) mod 25` to period `10` (`gl2z_moves_order25_carrier_to_10 = true`). The full minimal-degree set on primitive order-`N` torsion is `GL(2, Z)`-invariant; the per-subset period split is basis-dependent.
   - For `gamma = L^2 R = ((3, 2), (1, 1))`, `|tr(gamma) - 2| = 2`: exactly **`2`** points of `(1/2 Z / Z)^2` are fixed by `gamma`, strictly fewer than the **`4`** points whose order divides `2`, confirming that `|tr(gamma) - 2|` bounds the fixed-point count from above rather than equating "order divides `|tr(gamma) - 2|`" with invariance.

### Row `1516` (`@ e40d0fb1` — Channel-Norm Pair Sums, Summed-Twist Multipliers, Imaginary-Axis Isotropy, and `B1788` Hypotheses)

1. **Summed-twist multipliers, Liouville ratio constancy, `S = x + y` kernel invariance, and Laurent constant `a_0` (section `1`):**
   - Across four rational twist quadruples `(a_x, b_x, a_y, b_y)` and generic complex `(u, tau)`, all eight channel quasi-period multipliers (`u + 1` and `u + tau` across `s in {1, i, j, k}`) match `-exp(2 pi i c_a)` and `-exp(-2 pi i c_b)` at `(c_a, c_b) = (a_S + alpha_s, b_S / 2 + beta_s)` with `S = x + y` to integer base-ten log error **`-49`** (while planted control `C2a` with `x - y` fails at order unity).
   - Liouville constancy in `u` of `P_s(u) theta_1(u | tau) / theta[c_s](u | tau)` holds to log error **`-50`**, invariance of the residue-normalized kernel `K_s = P_s / R_s` under shifting `(x, y) -> (x + delta, y - delta)` at fixed `S = x + y` holds to log error **`-49`**, and the thirty-two-point Cauchy circle mean for `a_0` matches `(d_u theta[c_s])(0 | tau) / theta[c_s](0 | tau)` to log error **`-47`** (`10b4cd220`).
2. **Two-dimensional polar quadrature cross-check and double-modulus pair sums at `2 tau` (section `2`):**
   - Independent two-dimensional polar Gauss–Legendre quadrature on the punctured fundamental parallelogram agrees with the one-dimensional Poisson–Parseval series `c(Lambda, M; tau)` to base-ten log error **`-13`**.
   - Both pair-sum identities `c_k + c_j = 2 c(Lambda, {2 M}; 2 tau)` and `c_1 + c_i = 2 c(Lambda', {2 M}; 2 tau)` hold to base-ten log error **`-49`**.
3. **Finite-order line census up to order `12` mod sign, imaginary-axis isotropy, and the four order-`8` lines (section `3`):**
   - Modulo `w <-> -w`, there are **`266`** rational torus lines of exact order at most `12`.
   - Exactly **`40`** of the `266` satisfy `3 p_1 = 1/4 (mod 1/2)`: **`36`** satisfy `12 p_2 in Z` and **`4`** have non-integer `12 p_2`, namely the four order-`8` lines **`(1/4, 1/8)`**, **`(1/4, 3/8)`**, **`(1/4, 5/8)`**, and **`(1/4, 7/8)`**. On those four lines off `Re(tau) in Z`, `sigma_b` is non-zero (log magnitude `-1` at `tau = 13/100 + (19/10) i`) and decays at large `Im(tau)` (`6 -> 7`) with exponent **`1/2`**, matching `1/2` to base-ten log error **`-17`** (`10b4cd220`).
   - At `Re(tau) = 0`, exact four-channel isotropy `c_1 = c_i = c_j = c_k` holds to log error **`-50`** on all **`18`** lines (`16` of order `12` plus `2` of order `4`) with `12 p_1` and `12 p_2` odd integers for charge sums `-3` and `+3`, and three-channel equality `c_i = c_j = c_k` holds to log error **`-50`** on all **`8`** order-`8` lines with `24 p_1` and `24 p_2` odd integers for equal-charge sum `-6`.
4. **Exact rational sweep of `B1788` hypothesis `(a)` across `183` cases (section `4` and Control `C2b`):**
   - Across all reduced slopes `p_1 in (0, 1/2]` of denominator `2 <= d <= 20` and all three integer charge pairs `(1, -4)`, `(1, 2)`, `(-3, 6)` with `2 a_S not in Z`, there are **`183`** cases.
   - In exact rational arithmetic, the non-strict margins `E_{jk} - |d_x + d_y - 1/2|` and `E_{1i} - |d_x - d_y|` have minimum **`0`** and **`0`** across all `183` cases (zero violations; `jk` ties in **`95`**, `1i` ties in **`95`**, both tie simultaneously in **`7`**, and **`0`** cases have both strictly positive).
   - By contrast, comparing both against the single bound `|d_x + d_y - 1/2|` fails in **`48`** of the `183` cases (`9` cases at denominator `<= 12`, or `18` when mirrored into `[1/2, 1)`), confirming both the exact piecewise theorem and the literal-wording failure count.
5. **Laurent constant parity and Gauss digamma closed forms (sections `5` and `7`):**
   - Oddness `K_s(u; -S) = -K_s(-u; S)` gives `a_0(charge sum -3) = -a_0(charge sum +3)` across both `+3` charge pairs to log error **`-50`**.
   - At `Lambda = 3/8` and `Lambda = 1/8`, `c^inf(Lambda)` matches `2 pi (ln(8 / pi) -/+ sqrt(2) ln(1 + sqrt(2)))` to log error **`-50`**.
6. **Section `6` (`CANNOT CHECK` under firewall):**
   - Section `6` of `e40d0fb1` compares a channel-norm expression against a disclosed empirical ratio. Under `M1` and `README.md` section `9` rule `1` (`0 of 19`), no empirical comparison is performed by `agy-exp`; section `6` is recorded as **`CANNOT CHECK`** (scope of the web seat).

### Row `1640` (`@ 3c34dd90` — Candidate Actions on `tau` Graded Against the Weave Clause)

1. **Stationarity at elliptic points and torsion-freeness of `+-Gamma_1(N)` for `N >= 4`:**
   - First-derivative checks on smooth `SL(2, Z)`-invariant test combinations confirm vanishing gradient at the fourfold point `i` and threefold point `omega = (-1 + i sqrt(3)) / 2` to base-ten log error **`-33`**.
   - Exhaustive search over trace `-1, 0, +1` unimodular matrices mod `N` fixing primitive order-`N` torsion vectors up to sign confirms **`0`** elliptic fixed points across every `N` from `4` through `30`.
2. **Two-dimensional and six-dimensional parity identities:**
   - The classical two-dimensional Jacobi parity identity `theta_2(0 | tau) theta_3(0 | tau) theta_4(0 | tau) / eta(tau)^3 = 2` (squared product `4`) holds to log error **`-50`**.
   - Splitting `(Z^6 \ {0})` into `(2 Z)^6 \ {0}` and its `63` non-zero mod-`2` cosets gives the exact Dirichlet scaling `2^(-2 s) E(tau, s)` for the trivial coset and `(1 - 2^(-2 s)) E(tau, s)` for the `63` non-trivial cosets; subtracting the two (`2 * 2^(-2 s) - 1`) at `s = 3` yields the exact rational coefficient **`2^(2 - 6) - 1 = -15/16`** multiplying `E(tau, 3)` (confirmed by direct six-dimensional lattice summation to log relative error `-7`).
3. **Rubric audit across all `13` candidate classes and `23` relay commits (plus Control `C3`):**
   - Every one of the **`23`** commit hashes cited in section `7` of `3c34dd90` resolves as a valid ancestor commit in `3c34dd90`'s git graph (`section_7_commits_verified = 23`).
   - Independent `T1`–`T5` grading against the `2026-10-24` weave clause in `docs/THE_WEAVE.md` confirms **`0`** qualifying candidates among the **`13`** inventoried classes (each fails at least one explicit premise among quotient modularity on `H / SL(2, Z)`, absence of per-thread or chosen inputs, non-constancy, or non-elliptic interior stationarity), while synthetic control `C3` passes all five predicates.

---

## 4. What Was Left Out (`README.md` Section `7`)

1. **Section `6` of Harvest Row `1516` (`@ e40d0fb1`):** excluded unread/uncomputed as `CANNOT CHECK` because checking it requires comparing against a measured ratio (`0 of 19`).
2. **No optimization or numerical minimization of any candidate action in Row `1640` (`@ 3c34dd90`):** graded strictly by algebraic premise and modular-symmetry rubric (`T1`–`T5`), without searching for or evaluating numerical minima on the upper half-plane.
3. **No execution of the web seat's scripts:** all checks were computed from mathematical statements alone by `relays/x_c2_verify/verify_x_c2.py` and `relays/x_c2_verify/postrun_a0_cauchy_check.py`.

`0 of 19.`
