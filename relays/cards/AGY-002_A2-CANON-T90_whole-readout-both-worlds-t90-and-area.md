# Card A2-CANON-T90: Critical-Path Whole-Weave Read-Out in Both Higgs Worlds (`W_-`, `W_+`), Both Channel Weights (Theorem 90 Exact `N_s` & Old `2 pi L_2 + c_s`), and Both Measures (Move-Count & Hyperbolic Area)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Mandate:** Owner critical-path dispatch (`2026-11-14`) + `M27` / `M30` (`A2-CANON`), superseding/encompassing `AGY-002_A2-CANON_canonical-end-whole-weave-readout.md` (`1dde76be0`).
- **Blind Commitment Note:** Committed and pushed **prior** to running the Theorem 90 / area-measure computation and **prior** to opening `B1927/verification/canon_readout.json`, `B1928/verification/fiber_ergodic_fine.json`, or any `agy-exp` `X-CANON` output.
- **Firewall:** Strictly one hundred percent data-free (`zero` measured numbers touched or imported); all numerical read-out seven-vectors written **exclusively to JSON**, never in `.md` prose or stdout logs; position-only output names (`up_r23`, `up_r13`, `down_r23`, `down_r13`, `abs_V12`, `abs_V23`, `abs_V13`), zero particle names.

---

## 1. Mathematical Structure & Locked Pre-Computation Expectations

1. **Exact Modular Invariance of Theorem 90's Channel Weight (`N_s^{T90} = 2 pi L_2 + c_s - pi |a_{0,s}|^2 e^{-2 L_2}`):**
   - On the lattice `Z + Z tau` (Euclidean area `Im tau`), each active normalised channel kernel `K_s(u; tau) = P_s(u; tau) / R_s(tau) = 1/u + a_{0,s}(tau) + a_{1,s}(tau) u + ...` has unitary period multipliers `(e^{2 pi i nu_s}, e^{2 pi i B_s}) != (1, 1)` and a single simple pole per cell of residue `1`. By Liouville's theorem, `K_s(u; tau)` equals the Kronecker function `theta_1'(0|tau) theta_1(u + w_s|tau) / [theta_1(u|tau) theta_1(w_s|tau)] e^{2 pi i nu_s u}` (`w_s = nu_s tau - B_s`), so its constant term has the exact closed form
     `a_{0,s}(tau) = theta_1'(w_s | tau) / theta_1(w_s | tau) + 2 pi i nu_s`,
     which transforms with strict weight `1` under `SL_2(Z)` (`|a_{0,s}(gamma c, gamma tau)|^2 = |c tau + d|^2 |a_{0,s}(c, tau)|^2`).
   - Meanwhile `B1667`'s length-two horocycle coordinate `L_2(tau)` satisfies `e^{-2 L_2(gamma tau)} = |c tau + d|^{-2} e^{-2 L_2(tau)}`, and `2 pi L_2(tau) + c_s(c, tau)` is already `SL_2(Z)`-invariant (`B1921`). Therefore the product `pi |a_{0,s}(c, tau)|^2 e^{-2 L_2(tau)}` cancels `|c tau + d|^2 |c tau + d|^{-2} = 1` identically: **`N_s^{T90}` is strictly `SL_2(Z)`-invariant and real-analytic across all of `H` (including across the boundary arc `|tau| = 1`)**.

2. **Exact Cusp Asymptotics & Strict Positivity (`0` Clamping) of Both `N_s^{T90}` and `N_s^{old}`:**
   - As `y = Im(tau_FD) -> +infty`, `lim_{y->infty} L_2(x + i y) = pi + ln(pi) - 3 ln(2) = 2.2068809978...` (`e^{-2 L_2} -> (64 / pi^2) e^{-2 pi} = 0.012119...`), while `|a_{0,s}(tau_FD)|^2` approaches `4 pi^2 (nu_s - 1/2)^2` for `nu_s in (0, 1)` and `pi^2 cot^2(pi B_s)` for `nu_s = 0, B_s in (0, 1)`.
   - Consequently, the subtracted disc term `pi |a_{0,s}|^2 e^{-2 L_2}` remains uniformly bounded (`<= ~0.3` in the cusp and `O(10^{-2}..10^{-1})` in the bulk) against `2 pi L_2 + c_s >= ~6.9`, so **both `N_s^{T90}` and `N_s^{old}` remain strictly positive (`0` clamps) everywhere on `H` and into the cusp**.
   - Relative to `N_s^{old} = 2 pi L_2 + c_s`, `N_s^{T90}` shifts the seven whole-weave outputs at the sub-percent to few-percent level (statistically resolved cleanly at `|z| > 5` in paired word-by-word and identical-grid comparisons, yet far smaller than the `~35%` Breakdown of `L_max`). Against direct 2D Gauss–Legendre integration of `int_{X_tau \ H(L_2)} |K_s(u)|^2 d^2 u` on spot points, `N_s^{T90}` matches the exact horoball integral to the `O(e^{-4 L_2}) ~ 10^{-4}` Theorem 90 remainder.

3. **Both Higgs Worlds (`W_-` and `W_+`) & Exact Symmetries:**
   - `W_- = (up S~, down S, leptons S)` and `W_+ = (up S, down S~, leptons S~)` both obey exact matter-charge negation `f(tau, -c) = f(tau, +c)` (`< 10^{-13}`), exact level-five down–lepton identity (`down == leptons` to `< 10^{-14}` pointwise and in every whole-weave average), and exact finite-`n` mark–twin equality `R_n(mark) == R_n(twin)` under the reverse-swap bijection `w <-> swap_{L<->R}(reverse(w))`.
   - Across the seven claimed positions (`up_r23`, `up_r13`, `down_r23`, `down_r13`, `abs_V12`, `abs_V23`, `abs_V13`), `W_-` and `W_+` separate decisively (`|z| >> 4`) under **every** combination of `(weight in {exact_T90, old_weight}) x (measure in {move_count, area})`.

4. **Hyperbolic Area Measure (`(3 / pi) dx dy / y^2` Averaged Over All `24` Order-Five Points) & Exact Cusp Treatment:**
   - **Cusp problem diagnosis (two distinct numerical traps):**
     1. *Slow `O(1 / Y_cut)` truncation tail:* Cutting the `SL_2(Z)` fundamental domain `F` at `Im(tau) <= Y_cut` omits hyperbolic area `1 / Y_cut` out of `pi / 3`, i.e. fraction `3 / (pi Y_cut)` (`9.55%` at `Y_cut = 10`, `1.91%` at `Y_cut = 50`), biassing any bounded observable whose cusp limit `f_cusp` differs from its bulk mean by `(3 / (pi Y_cut)) (<f>_infty - f_cusp)`.
     2. *IEEE-754 `float64` SVD underflow on `|V_{ij}|` for `y >= ~8`:* As `y -> infty`, the lightest Yukawa singular value ratio `sigma_1 / sigma_3` decays exponentially below machine epsilon `2.2e-16` around `y ~ 7..9`. Naive `float64` `svd` treats `Y_f` as numerically rank-deficient and rotates the first/second left singular vectors arbitrarily into rounding noise, corrupting `|V_{12}|, |V_{23}|, |V_{13}|` on the `~10%` of hyperbolic area above `y = 10`.
   - **Our exact cusp method:** Change variables to `u = 1 / y in [0, 2 / sqrt(3)]`, transforming `dx dy / y^2` with **unit Jacobian** into `dx du` on the bounded region `|x| <= 1/2, 0 <= u <= 1 / sqrt(1 - x^2)` (cusp at `u = 0` with smooth bounded measure). Split at `y = 5` (`u = 0.20`): integrate the bulk `u in [0.20, 1 / sqrt(1 - x^2)]` (`80.90%` of area) by high-order 2D Gauss–Legendre quadrature, and integrate the cusp strip `u in (0, 0.20]` (`19.10%` of area) on multi-panel `(x, u)` Gauss–Legendre grids using **dynamic arbitrary-precision `mpmath` complex SVD** (`dps >= 3.2 y + 45`, resolving all three singular values and singular vectors cleanly past `y = 250`) plus the exact `u -> 0^+` asymptotic cusp limit on `[0, 0.002]`, alongside a full `Y_cut in {5, 10, 20, 50, 200, infty}` convergence table.
   - Expected result: `move_count` and `area` measures separate cleanly by many standard errors (`|z| >> 10`) in both `W_-` and `W_+` and under both `exact_T90` and `old_weight`.

5. **Planted Controls (`CTL-T90-1..5`):**
   - `CTL-T90-1` (*Weight-mismatch control*): Using `e^{-2(L_2 + (1/2) ln Im tau)}` instead of `e^{-2 L_2}` in `-pi |a_{0,s}|^2 e^{-2 L_2}` breaks `S`-invariance between `tau` and `-1 / tau` by a factor of `|tau|^2` (`> 10^{-2}`).
   - `CTL-T90-2` (*Wrong-sign Theorem 90 control*): Flipping `-pi |a_{0,s}|^2 e^{-2 L_2}` to `+pi |a_{0,s}|^2 e^{-2 L_2}` fails against direct 2D horoball quadrature `int_{X_tau \ H(L_2)} |K_s|^2 d^2 u` by `2 pi |a_{0,s}|^2 e^{-2 L_2}`, whereas Theorem 90's minus sign agrees to `O(e^{-4 L_2})`.
   - `CTL-T90-3` (*Cusp `float64` SVD underflow control*): Comparing `float64` SVD vs `150`-digit `mpmath` SVD at `y = 15` and `y = 30` exposes `O(10^{-1})` artificial rotation of `|V_{ij}|` in `float64`.
   - `CTL-T90-4` (*Arc smoothness control*): Symmetric second-difference ratio across `|tau| = 1` equals `4.00` for `N_s^{T90}` vs `2.00` for `L_max` and `ln y_FD`.
   - `CTL-T90-5` (*Guardrail 3 unitary basis-scrambling*): Random Haar `SU(3)_Q x SU(3)_u x SU(3)_d` rotations leave all seven outputs invariant to `< 10^{-13}` on well-conditioned bulk points.

0 of 19.
