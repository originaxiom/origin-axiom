# Pre-Registration Card: `AGY-002_A2-OW8` — Finite Conformal Induced Gravity (`xi = 1 / 6`), `2H` Type-II 2HDM Radiative EWSB Transmutation, and Guardrail 5 Scale Ledger (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW8`
- **Empirical Firewall:** Strict `0 of 19` (all scale outputs expressed as purely dimensionless ratios; zero empirical PDG inputs used as model inputs).
- **Prerequisite Custody:** Builds on `A2-OW3` (`2294c03c3` / `2fcde558a`), `A2-OW4` (`08315469d` / `1192ed854`), and `A2-OW7` (`57a8539b2` / `19d2facbe`).

## 1. Scientific Objective & Hypotheses Committed Before Run

This card attacks Hard Wall 3 (finite Newton constant when `C_grav^{quad} = 0` at conformal Higgs `xi = 1 / 6`, plus dynamical dimensional transmutation of `v_EW / M_UV` in `A2-OW3`'s forced `2H` Type-II 2HDM):

1. **Exact Subleading Logarithmic / Finite Sakharov `1 / G_N` at Conformal Higgs `xi = 1 / 6` (`OW8-A`):**
   - Derive from first principles on unit round `S^4` (`R = 12`, `Vol = 8 pi^2 / 3`, `45`-dps `mpmath` spectral summation) AND direct Schwinger proper-time quadrature `int_{1/Lambda^2}^infty t^(-2) exp(-t M^2) dt = Lambda^2 - M^2 ln(Lambda^2 / M^2) + (gamma_E - 1) M^2 + O(M^4 / Lambda^2)`:
   - **Pass bar `OW8-A`:**
     - Direct quadrature at `(M, Lambda) = (2, 1000)` matches the asymptotic formula to `< 1 / 10^4` (`O(M^4 / Lambda^2)`).
     - Exact massive Proca vector (`3` physical polarizations = `Tr(Delta_1) - Tr(Delta_0) = Tr(transverse) - 1` on `S^4`): `a_0 = 3` and `w_Proca = a1_T / R = -1 / 2` to `< (1 / 10)^9`, matching exact Goldstone eating `w_V(-2 / 3) + w_s(+1 / 6) = -1 / 2`.
     - Therefore, in `A2-OW4`'s conformal-Higgs vacuum (`xi = 1 / 6`, where the quadratic Planck divergence cancels identically via `48 * (1/6) + 12 * (-2/3) = 0`), the exact logarithmic induced gravity coefficient `c_log = -w_i` multiplying `(M_i^2 / (32 pi^2)) ln(Lambda^2 / M_i^2)` is `0` (conformal scalar), `-1 / 6` (minimal scalar or Weyl fermion, repulsive), and **`+1 / 2` (massive Proca vector, attractive)**.
     - Across `A2-OW3`'s `Spin(10) -> G_SM` threshold (`45 - 12 = 33` massive `X, Y` Proca vectors of mass `M_X` vs `3` heavy Majorana `nu^c` Weyl fermions of mass `M_R`), prove exact `c_log(M_X = M_R) = 33 * (1 / 2) + 3 * (-1 / 6) = +16 > 0` — **strictly attractive finite/logarithmic 4D gravity (`1 / G_N > 0`) for every mass ratio `M_R / M_X < sqrt(33)`** — while confirming that at a pure EW-scale threshold (`(1 / 2)(2 (M_W / m_t)^2 + (M_Z / m_t)^2) - 1 < 0` for representative ratio `(M_W/m_t, M_Z/m_t) = (804/1733, 912/1733)`), top fermions dominate negatively, proving heavy gauge vectors at the unification/KK scale are strictly required for conformal `1 / G_N > 0`.

2. **Exact `2H` vs `1H` Unification Slope Ratio & Conformal Type-II 2HDM Radiative EWSB Transmutation (`OW8-B`):**
   - Compute the exact rational `1`-loop gauge unification slope ratio `B(n_H) = (b_2 - b_3) / (b_1 - b_2)` under open-weave `Spin(10)` normalization `k_Y = 5 / 3` across `n_H in {1, 2, 3, 4, 6, 8}`.
   - Contrast exact `1`-loop conformal UV boundary (`lambda_i(M_UV) = 0`, perturbative `g_UV = 52 / 100`, running down `14` decades) in `1H` SM vs `A2-OW3`'s forced `2H` Type-II 2HDM (Branco et al. `arXiv 1106-0034` conventions):
   - **Pass bar `OW8-B`:**
     - Exact rationals `B(1) = 115 / 218`, `B(2) = 5 / 9 > B(1)` (confirming `2H` moves strictly upward toward `5 / 7` relative to `1H`, while honestly remaining below `5 / 7` without intermediate thresholds).
     - **`1H` SM conformal no-go:** Starting from `lam(M_UV) = 0` with `y_t(M_UV) in {1 / 2, 3 / 5}`, `lam(IR) > 15 / 100 > 0` (**no radiative EWSB possible in conformal `1H` SM**).
     - **`2H` Type-II 2HDM automatic radiative split:** Starting from `lam_1 = lam_2 = lam_3 = lam_4 = 0` at `M_UV` with `y_t(M_UV) in {1 / 2, 3 / 5}` and `y_b(M_UV) in {1 / 100, 1 / 10}`, running down `14` decades drives `lam_2(H_u) > 3 / 10 > 0` (stable) while driving **`lam_1(H_d) < -1 / 20 < 0` (radiative Coleman-Weinberg / Gildener-Weinberg destabilization along `H_d`)**.
     - **Exponential dimensional transmutation:** Starting from small positive UV quartics `lam_1 = lam_2 = lam_0 in {1 / 100, 1 / 50, 1 / 20}` (`lam_3 = lam_4 = 0`, `y_t = 11 / 20`, `y_b = 1 / 100`), `lam_1(mu)` crosses zero strictly monotonically at `log10(mu_GW / M_UV)` in `(-3, -25 / 10)`, `(-6, -55 / 10)`, and `(-15, -13)` respectively (generating up to `14` decades of exponential scale hierarchy cleanly before the QCD pole!).

3. **Guardrail 5 Non-Dimensionalized Scale & Continuous-Parameter Ledger (`OW8-C`):**
   - Express every scale output strictly as a dimensionless ratio (`M_Pl / M_X`, `mu_GW / M_UV`, `B(n_H)`) and explicitly price the continuous dimensionless parameters not yet dynamically fixed by the open weave (`g_UV`, `lam_0`, `tan(beta)`, `M_R / M_X`).

4. **Planted-Fault Self-Checks (`OW8-D`, `4 / 4`):**
   - `PF-OW8-1`: Flipping the mass-insertion sign (`+w_i` instead of `-w_i`) makes `33` heavy Proca vectors + `3` Weyl neutrinos yield repulsive `c_log = -16 < 0` (`caught`).
   - `PF-OW8-2`: Setting `M_R = 10 * M_X > sqrt(33) M_X` flips conformal `Spin(10)` gravity negative (`-67 / 2 < 0`, `caught`).
   - `PF-OW8-3`: Using wrong hypercharge normalization `k_Y = 1` instead of `5 / 3` shifts `B(2H)` from `5 / 9` to `2 / 5` (`caught`).
   - `PF-OW8-4`: Setting equal `y_b(UV) = y_t(UV) = 3 / 5` in `2H` Type-II 2HDM forces both `lam_1(IR) > 0` and `lam_2(IR) > 0`, eliminating `H_d` radiative destabilization (`caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; independent Cold-Room Referee built solely from this card using disjoint exact rational Bernoulli/Hurwitz-zeta `S^4` Proca heat kernel, exact `mp.e1` exponential integral evaluation, and adaptive `DOP853` ODE solver. `0 of 19.`
