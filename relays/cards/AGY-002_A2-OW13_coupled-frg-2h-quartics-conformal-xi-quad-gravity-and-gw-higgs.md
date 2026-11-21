# AGY-002 Pre-Registration Card `A2-OW13`: Coupled Gravity-Matter `2H` FRG (`lam_0` Elimination & `G_SM` Collision Wall), Conformal `xi = 1/6` & `C^2 + R^2` Quadratic Gravity, and `2H` Gildener-Weinberg Higgs Spectrum (`0 of 19`)

- **Seat:** `AGY-002`
- **Branch:** `agy-002/verify`
- **Card ID:** `A2-OW13`
- **Empirical inputs:** **`0 of 19`** (zero PDG inputs; Guardrail 4 literature benchmarks for `1`-loop SM criticality `arXiv:1307-3536` Table `3`, `Litim (2004)`, and `Avramidi-Barvinsky (1985)` / `Codello-Percacci (2006)` pure-gravity quadratic beta functions are isolated strictly inside dedicated unit gates and never enter open-weave model evaluation).
- **Guardrails:** `0` float/complex AST literals in `.py` (exact `Fraction` and integer-built `mpmath` at `>= 50` dps); `0` `frontier/` imports; zero hardcoded proof flags; `A`-only `SHA-256` manifests; Cold-Room Referee disjoint methods (`0` discrepancies, `4/4` planted faults).

---

## 1. Scientific Scope & Hypotheses

Card `A2-OW13` executes Phase 3 of Campaign 2: testing whether coupled gravity-matter FRG slashes the remaining continuous parameters (`lam_0`, `g_UV`, `tan(beta)`), auditing the radiative and gravitational stability of `A2-OW8`'s conformal coupling `xi = 1/6` together with `C^2 + R^2` higher-derivative truncation stability, and deriving the exact `1`-loop `2H` Gildener-Weinberg scalon Higgs spectrum `m_h / v_EW`.

---

## 2. Frozen Specification & Pass/Fail Acceptance Criteria

### Task `OW13-A`: Coupled Gravity-Matter `2H` FRG, `lam_0` Elimination, & `f_g > 0` Theorem

1. **Isolated Guardrail 4 Literature Benchmark Gates:**
   - **SM `1`-loop criticality benchmark (`Buttazzo et al. arXiv:1307-3536`, Table `3` inputs expressed as exact rationals):**
     At `mu_0 = 1731/10 GeV` with `(g_3, g_2, g', y_t, lam_B) = (11666/10^4, 64822/10^5, 35761/10^5, 93558/10^5, 12711/10^5)` in `V = lam_B (H^dag H)^2` (matching `2H` convention `lam_1 = 2 lam_B` via `16 pi^2 d(lam_B)/d(ln mu) = 24 lam_B^2 + 12 lam_B y_t^2 - 6 y_t^4 - 3 lam_B (3 g_2^2 + g'^2) + (3/8)(2 g_2^4 + (g_2^2 + g'^2)^2)`), integrate `t = ln(mu / mu_0)` from `0` to `40`:
     - Verify `lam_B` crosses `0` at `t_cross` with `8 < log10(mu_cross / GeV) < 9` (`13 < t_cross < 15`) and `lam_B(M_Pl) < -3/100` at `M_Pl = 122 * 10^17 GeV`.
     - Verify numerical `g_3(M_Pl)` matches the exact analytic `1`-loop closed form `(g_3(0)^(-2) + 14 t_Pl / (16 pi^2))^(-1/2)` to `< 1/10^12`.
   - **Pure-gravity Litim (`2004`) benchmark & First-Principles `f_lam(g, lam)` Derivation:**
     From the `4D` Wetterich Litim threshold integral `I_litim = (1 - eta_N / 6) / (32 pi^2)` on `lam_eff = lam + 8 pi g v`:
     - **de Donder gauge (`10` metric modes - `8` ghosts, matching `A2-OW10`):**
       `f_lam^{(dD)}(g, lam) = 5 g (1 - eta_N / 6) / (pi (1 - 2 lam)^2)`, which at `eta_N = -2` equals `20 g / (3 pi (1 - 2 lam)^2)`.
     - **Landau-DeWitt gauge (`5` TT + `1` conformal scalar - `4` gauge/ghost):**
       `f_lam^{(LDW)}(g, lam) = (g (1 - eta_N / 6) / pi) * (5 / (2 (1 - 2 lam)^2) + 1 / (3 (1 - 4 lam / 3)^2))`, which at `eta_N = -2` equals `(10 g / (3 pi (1 - 2 lam)^2)) + (4 g / (pi (3 - 4 lam)^2))`.
     - Verify `f_lam^{(dD)} > 0` and `f_lam^{(LDW)} > 0` strictly across all five gravity fixed points computed directly from `A2-OW10`/`A2-OW11` (`Pure Gravity T2`, `Spin(10) real-10 T2`, `Spin(10) real-10 T1`, `PS(4,1,2) T2`, `G_SM 2H T2`).

2. **Exact `2H` Type-II Quartic Fixed Points & `G_SM 2H` Collision Wall:**
   - Use standard `1`-loop `U(1)_PQ`-symmetric (`lam_5 = 0` from `A2-OW3`/`OW8` `X:HOL`) Type-II `2HDM` quartic beta functions `beta_{lam_i}^{(mat)}` (`i = 1, 2, 3, 4`) with GUT-normalized `g'^2 = (3/5) g_1^2`, coupled to gravity via `beta_{lam_i} = beta_{lam_i}^{(mat)} + f_lam * lam_i`.
   - Benchmark unified UV gauge coupling `g_1 = g_2 = g_3 = g_UV = 13/25`, `y_t = 11/20`, and two Yukawa regimes: low-`y_b` (`y_b = y_tau = 1/100`) vs large-`y_b` (`y_b = y_tau = 9/20`, above `y_b^{crit} = (171/600)^(1/4) g_UV`).
   - **Analytic Collision Wall:** Certify the exact `y_b = 0` `lam_1` quadratic discriminant threshold `f_crit(g_UV) = (54 + 6 sqrt(114)) g_UV^2 / (80 pi^2)` (`4/100 < f_crit < 41/1000` at `g_UV = 13/25`):
     - Verify `f_lam^{(dD)}(G_SM 2H) < 34/1000 < f_crit` and `f_lam^{(LDW)}(G_SM 2H) < 22/1000 < f_crit`, and verify directly via complex root check / discriminant `< 0` that bare `G_SM 2H` suffers a **complex fixed-point collision** for `lam_1` at `y_b = 1/100`.
     - Verify `Spin(10) real-10 T2`, `Spin(10) real-10 T1`, and `PS(4,1,2) T2` ALL lie strictly above `f_crit` in BOTH de Donder and Landau-DeWitt gauges (`f_lam^{(dD)}(Spin(10) T2) > 67/100`, `f_lam^{(LDW)}(Spin(10) T2) > 37/100`), solving the full `4`-coupling coupled nonlinear system `beta_{lam_i} = 0` to residual `< 1/10^40`.
     - Verify that at `Spin(10) T2` (both `dD` and `LDW`, both `y_b = 1/100` and `y_b = 9/20`) and `PS(4,1,2) T2`, ALL `4` critical exponents `theta_i = -Re(eig(d beta / d lam))` are **strictly negative (`theta_i < 0`, all `4` quartics UV-irrelevant)** and all `|lam_i^*| < 3/100` (eliminating `lam_0` as a free parameter!).
     - Verify that at `Spin(10) T2` with `y_b = 9/20`, ALL `4` tree-level boundedness-from-below (BFB) conditions (`lam_1 > 0`, `lam_2 > 0`, `lam_3 + sqrt(lam_1 lam_2) > 0`, `lam_3 + lam_4 + sqrt(lam_1 lam_2) > 0`) hold strictly at the UV fixed point.

3. **Downward `1`-Loop `2H` Type-II RGE (`t = 0 -> -38`, `M_Pl -> M_EW`):**
   - Integrate the full `10`-coupling `2H` Type-II system `(g_3, g_2, g', y_t, y_b, y_tau, lam_1, lam_2, lam_3, lam_4)` downward from `t = 0` to `t = -38` (`b_3 = -7, b_2 = -3, b_{g'} = +7`):
     - At `y_b = 9/20`: compare `Spin(10) T2 (dD)` gravity-fixed UV quartics against `A2-OW8`'s exact `lam_i(0) = 0` boundary; verify ALL `4` BFB conditions remain strictly positive at `t = -38` and the maximum IR quartic difference between gravity-fixed and exact-zero UV boundaries is `< 5/1000`!
     - At `y_b = 1/100`: verify `lam_1(t = -38) < -1/10` (radiative destabilization driving the `H_d` flat direction) while `lam_2(t = -38) > 7/10` remains strictly positive.

4. **Exact `f_g > 0` Structural Theorem (`Spin(10)` vs `U(1)_Y`):**
   - Compute exact `1`-loop `Spin(10)` gauge beta coefficients from Dynkin indices (`T(adj) = 8`, `T(16_+) = 2`, `T(vec 10) = 1`): `b_{Spin(10), real 10} = -151/6 < 0` and `b_{Spin(10), complex 10} = -25 < 0`, vs `2H` `U(1)_Y` `b_1 = +21/5 > 0`.
   - Prove that for ANY `f_g > 0` in `beta_g = -f_g g + b g^3 / (16 pi^2)`:
     - `Spin(10)` (`b < 0`) admits ONLY the Gaussian fixed point `g_* = 0` with `theta_g = +f_g > 0` (**UV-relevant -> `g_UV` is NOT pinned by `f_g > 0`**).
     - `U(1)_Y` (`b_1 = +21/5 > 0`) admits a unique interactive Harst-Reuter UV fixed point `g_{1*}^2 = 16 pi^2 f_g / b_1` with `theta_g = -2 f_g < 0` (**UV-irrelevant**).

---

### Task `OW13-B`: Conformal `xi = 1/6` Stability & `C^2 + R^2` Quadratic-Gravity Truncation Audit

1. **Exact `1`-Loop `2H` Curved-Space `(beta_{xi_d}, beta_{xi_u})`:**
   - With `16 pi^2 beta_{xi_d}^{(1)} = (xi_d - 1/6)(6 lam_1 + 6 y_b^2 + 2 y_tau^2 - (9/2) g_2^2 - (3/2) g'^2) + (xi_u - 1/6)(4 lam_3 + 2 lam_4)` and `16 pi^2 beta_{xi_u}^{(1)} = (xi_u - 1/6)(6 lam_2 + 6 y_t^2 - (9/2) g_2^2 - (3/2) g'^2) + (xi_d - 1/6)(4 lam_3 + 2 lam_4)`:
     - Verify exact vanishing at `(xi_d, xi_u) = (1/6, 1/6)` (`< 1/10^45`).
     - Compute exact eigenvalues of the `2 x 2` stability matrix `M_xi`: certify saddle (`eig_1 < 0 < eig_2`) at low `y_b = 1/100` (`UV Spin(10)`), and **strictly double IR-attractive** (`0 < eig_1 < eig_2`) at BOTH `UV Spin(10)` (`y_b = 9/20`) and the IR `t = -38` endpoint (`eig_1 > 9`, `eig_2 > 13`).
2. **Exact Gravitational Background-Field `beta_xi^{grav, bg}` from `A2-OW10` `B_1, B_2`:**
   - Differentiating `k d_k Z_N(phi) = -(k^2 / (16 pi)) (B_1(lam_eff) + eta_N B_2(lam_eff))` with `Z_N(phi) = 1/(16 pi G) - (1/2) xi phi^2` and `lam_eff(phi) = lam / (1 - 8 pi g xi phi^2)` at `eta_N = -2` gives exact `beta_xi^{grav, bg} = -g lam xi (11 + 10 lam) / (pi (1 - 2 lam)^3)`.
   - Certify `f_xi^{bg} = beta_xi^{grav, bg} / xi != 0` at every `lam_* != 0` fixed point (`Spin(10) T2`: `-8/100 < f_xi^{bg} < -7/100`; `PS(4,1,2) T2`: `+4/100 < f_xi^{bg} < +5/100`; `G_SM 2H T2`: `-22/100 < f_xi^{bg} < -21/100`), honestly proving non-zero cosmological constant breaks conformal `xi = 1/6`, AND certify `f_xi^{bg}(lam = 0) = 0` identically (unimodular protection previewing `A2-OW14`).
3. **Exact `1`-Loop Quadratic Gravity (`C^2 + R^2`) + Conformal Matter (`Avramidi-Barvinsky 1985` / `Codello-Percacci 2006`):**
   - Guardrail 4 Pure Gravity (`N_S = N_W = N_V = 0`) benchmark: `16 pi^2 beta_{lam_C} = -(133/10) lam_C^2` and `16 pi^2 beta_omega = -lam_C ((10/3) omega^2 + (183/10) omega + 5/12)` with exact UV-attractive `omega_+ in (-23/1000, -22/1000)` and UV-repulsive `omega_- in (-55/10, -54/10)`.
   - With matter `(N_S, N_W, N_V)` at coupling `xi`: `c_mat = (N_S + 3 N_W + 12 N_V) / 120`, `133/10 -> 133/10 + 2 c_mat`, and constant `5/12 -> 5/12 + (3/2) N_S (xi - 1/6)^2`.
   - Certify across all `4` open-weave matter spectra (`G_SM 2H (8,48,12)`, `PS(4,1,2) (16,48,21)`, `Spin(10) real-10 (10,48,45)`, `Spin(10) complex-10 (20,48,45)`) that at conformal `xi = 1/6`: (i) `b_R^{mat}(1/6) = 0`, (ii) `C^2` asymptotic freedom strictly strengthens (`c_mat = 37/15, 103/30, 347/60, 88/15`), (iii) BOTH real `omega_+ < 0` (UV-attractive) and `omega_- < 0` (UV-repulsive) survive with strictly larger discriminant than pure gravity, AND (iv) certify the exact non-conformal collision bound `|xi - 1/6|_{crit}` (`< 22/10` for `Spin(10) real-10`, `< 19/10` for `G_SM 2H`, `< 15/10` for `PS(4,1,2)` and `Spin(10) complex-10`, excluding large-`xi` inflation).

---

### Task `OW13-C`: Exact `2H` Gildener-Weinberg Scalon Spectrum `m_h / v_EW` & Collider Sum Rule

1. Verify the exact `1`-loop identity `m_h^2 / v^2 = 8 B_GW = (1/2) beta_{lam_1}(lam_1 = 0)` along the `H_d` flat direction (`H_u = 0`, `m_{H+-}^2 = (1/2) lam_3 v^2`, `m_H^2 = m_A^2 = (1/2)(lam_3 + lam_4) v^2`) to `< 1/10^45`.
2. Certify the `1H` SM top-tachyon no-go threshold `y_t^{crit} = ((3 g_2^4 + 2 g_2^2 g'^2 + g'^4) / 16)^(1/4)`: `45/100 < y_t^{crit} < 46/100` at EW-like benchmark `(g_2 = 13/20, g' = 9/25)` and `37/100 < y_t^{crit} < 38/100` at GUT benchmark `(g_2 = 13/25, g' = sqrt(3/5) * 13/25)` (proving `B_{1H} < 0` tachyonic for any `O(1)` top Yukawa).
3. Certify strict `B_{2H} > 0` along `H_d` (top quark decoupled):
   - Pure-gauge Weinberg-Linde GW floor: `39/1000 < m_h / v < 40/1000` (EW benchmark) and `28/1000 < m_h / v < 29/1000` (GUT benchmark).
   - Collider sum rule for `m_h / v = 1/2`: degenerate heavy `H_u` mass `148/100 < M_heavy / v < 150/100` and sum-rule invariant `(m_H^4 + m_A^4 + 2 m_{H+-}^4)^(1/4) / v in (210/100, 211/100)`, requiring tree-level portal `lam_eff = 2 (M_heavy / v)^2 > 44/10` (honestly exposing the perturbative gap vs the `|lam_{3,4}| < 1` downward RGE output of `OW13-A`).

---

### Task `OW13-D`: `4 / 4` Planted Fault Controls (`PF-OW13-1..4`)

- `PF-OW13-1`: Flip gravitational quartic anomalous dimension `f_lam -> -f_lam` at `Spin(10) T2 (dD)` -> all `4` critical exponents flip to `theta_i > 0` (UV-relevant, destroying `lam_0` predictivity).
- `PF-OW13-2`: Flip sign of the `1`-loop gauge box `(3/4)(3 g_2^4 + 2 g_2^2 g'^2 + g'^4)` in `beta_{lam_1}` -> `G_SM 2H` at `y_b = 1/100` falsely gains a real `lam_1` root (destroying the collision wall).
- `PF-OW13-3`: Set non-conformal `xi = 5` (`|xi - 1/6| > |xi - 1/6|_{crit}`) in `C^2 + R^2` quadratic gravity for `Spin(10) real-10` -> `omega` discriminant flips strictly negative (`< 0`, destroying both real UV fixed points).
- `PF-OW13-4`: Couple the top quark `y_t = 94/100` to the `H_d` GW flat direction at EW benchmark -> `B_GW` flips strictly negative (`m_h^2 / v^2 < 0`, tachyonic instability).

---

## 3. Custody & Referee Protocol

1. Commit 1: seal this Card before any producer code exists.
2. Commit 2a / 2b: seal `relays/a2_ow13/verify_a2_ow13.py` pre-run (`A`-only `SCRIPT_SHA256.txt`), run once, seal `a2_ow13_results.json` & `OUTPUT_SHA256.txt` unread.
3. Independent Cold-Room Referee (`relays/a2_ow13_referee/`): reads ONLY this Card prior to Commit 4b, implements disjoint methods (`sympy` symbolic differentiation of the `4D` Litim potential & exact `A2-OW10` `B_1, B_2`, independent `RK4` / `scipy` ODE integrator, independent `sympy` quadratic-gravity & `2HDM` algebra), seals Commit 4a/4b unread, and certifies `0` discrepancies + `4/4` planted faults.
4. Relay `relays/AGY002_A2_OW13_RESULTS.md` + `STATUS_AGY-002.md` item `23` + `7`-point audit + fast-forward push to `origin/agy-002/verify`.
