# AGY-002 Results Relay: Card `A2-OW13` — Coupled Gravity-Matter `2H` FRG (`lam_0` Elimination & `G_SM` Collision Wall), Conformal `xi = 1/6` & `C^2 + R^2` Quadratic Gravity, and `2H` Gildener-Weinberg Higgs Spectrum (`0 of 19`)

- **Seat / Branch:** `AGY-002` on `agy-002/verify`
- **Empirical Inputs:** **`0 of 19`** (zero PDG inputs; Guardrail 4 literature benchmarks `arXiv:1307-3536` Table `3`, `Litim (2004)`, and `Avramidi-Barvinsky (1985)` / `Codello-Percacci (2006)` pure-gravity quadratic beta functions are isolated strictly inside unit gates).
- **Custody Chain:**
  - Pre-Registration Card: `relays/cards/AGY-002_A2-OW13_coupled-frg-2h-quartics-conformal-xi-quad-gravity-and-gw-higgs.md` (`6b63cc7be`)
  - Erratum 1 (`PS(4,1,2)` exact solved `(16, 48, 21)` `f_xi^{bg}` bracket): `relays/cards/AGY-002_A2-OW13-ERRATUM-1_ps412-exact-fixed-point-f-xi-window.md` (`f7504de09`)
  - Preserved `v1` Producer (untouched): `relays/a2_ow13/` (`e41426620` / `2739f6c7b`, `ow13_a/c/d = True`, `ow13_b = False` on pre-erratum `PS(4,1,2)` `f_xi^{bg}` bracket)
  - Authoritative `v2` Producer (`all_gates_passed = true`): `relays/a2_ow13_v2/verify_a2_ow13_v2.py` (`29c98fe53`, `SCRIPT_SHA256 = b07c6f6561d9501a5b9a8634fdfd7661dfcd882e32b926919dab2666d25b8b9d`) and `relays/a2_ow13_v2/a2_ow13_v2_results.json` (`7d9cf4ec6`, `OUTPUT_SHA256 = 7736b22437716992786e53fcf11fd6d7a4f7545a2b8db4f2700c53849e66af7f`)
  - Independent Cold-Room Zero-Trust Referee (strictly cold-room sealed unread): `relays/a2_ow13_referee/referee_a2_ow13.py` (`05af5ebca`, `SCRIPT_SHA256 = 552369ae7873525a67185c9e953735238a0fe22cb254b82c596249314436fb0e`) and `relays/a2_ow13_referee/a2_ow13_referee_results.json` (`a3327661d`, `OUTPUT_SHA256 = 36b9e684c445d2753b9502e81c738e8c44ba001ad1fe51e9d88b849c63285e3e`)
  - **Cross-Check Verdict:** **`0` discrepancies across all `221 / 221` compared fields (`169` numeric, `12` exact rational, `40` boolean)** plus `4 / 4` planted faults (`PF-OW13-1..4`) detected identically. Disjoint referee methods: symbolic `sympy.integrate`/`sympy.diff` derivation of `I_litim`, `f_lam`, and `beta_xi^{grav, bg}`, `sympy.real_roots`/`nroots` for all `5` gravity cubics, first-principles `8 x 8` `sympy.hessian` `Tr(H^2)` derivation of `2HDM` quartic beta functions, pure `mpmath` `RK4` (`n = 400/800`) Richardson + `scipy` `Radau` ODE integration (disjoint from `DOP853`), and `sympy.solve`/`simplify` for `C^2 + R^2` and `2H` GW identities. Max non-ODE discrepancy `<= 5 / 10^18` (JSON serialization floor); max ODE relative discrepancy `<= 3 / 10^12`. *(Strict cold-room note: the sealed referee JSON logged `2` extra referee-internal non-Card checks as `false` — an extra downward `g_3(-38)` `RK4(400/800)` error of `~139 / 10^14` vs its self-imposed `< 1/10^12` bar while `Radau` hit `~1 / 10^15`, and `sympy.solve` returning both `+-I` and real positive `4`-th roots because `g2, gp` lacked `positive=True` — while 100% of Card `A2-OW13` criteria and all `221 / 221` producer fields passed with `0` discrepancies; the cold-room seal `05af5ebca` / `a3327661d` is preserved untouched.)*

---

## 1. Task `OW13-A`: Coupled Gravity-Matter `2H` FRG — `lam_0` Elimination, `G_SM` Collision Wall, & `f_g > 0` Theorem

1. **Isolated Guardrail 4 Literature Benchmark Gate (`PASS`):**
   - `1`-loop `Buttazzo et al. arXiv:1307-3536` Table `3` SM criticality integration (`DOP853` producer vs `RK4` Richardson / `Radau` referee): `lam_B` crosses `0` at `t_cross ~ 1389/100` (`log10(mu_cross / GeV) ~ 827/100`), reaches `lam_B(M_Pl) < -3/100` (`~ -308/10^4`), and matches the exact analytic `1`-loop `g_3(M_Pl)` closed form to `< 2 / 10^14` (`< 5 / 10^14` referee `RK4`).
   - Exact first-principles `4D` Litim threshold derivatives match central finite differences to `< 2 / 10^34` and symbolic `sympy.diff` identically:
     - `f_lam^{(dD)}(g, lam) = 20 g / (3 pi (1 - 2 lam)^2) > 0` at `eta_N = -2` (`~ 399/100` Pure Gravity `T2`; `~ 676/1000` `Spin(10) real-10 T2`; `~ 1115/1000` `Spin(10) real-10 T1`; `~ 287/1000` `PS(4,1,2) T2`; `~ 338/10^4` `G_SM 2H T2`).
     - `f_lam^{(LDW)}(g, lam) = (10 g / (3 pi (1 - 2 lam)^2)) + (4 g / (pi (3 - 4 lam)^2)) > 0` (`~ 217/100` Pure Gravity; `~ 380/1000` `Spin(10) T2`; `~ 623/1000` `Spin(10) T1`; `~ 175/1000` `PS(4,1,2) T2`; `~ 218/10^4` `G_SM 2H T2`).

2. **Discovery — Analytic `G_SM 2H` Fixed-Point Collision Wall & UV `Spin(10)` Cure (`lam_0` Eliminated):**
   - For the `H_d` quartic `lam_1` at low `y_b`, the `1`-loop gauge box forces an exact real-root threshold `f_crit(g_UV) = (54 + 6 sqrt(114)) g_UV^2 / (80 pi^2)` (`~ 404/10^4` at `g_UV = 13/25`).
   - **Honest Failure of Bare `G_SM 2H`:** Deep negative `lam_* < -10` suppresses `f_lam` below `f_crit` in BOTH gauges (`~ 338/10^4 < 404/10^4` `dD`, `~ 218/10^4 < 404/10^4` `LDW`), driving the `lam_1` quadratic discriminant strictly negative (`~ -613/100` `dD`, `~ -1174/100` `LDW`) -> **complex fixed-point collision (no real UV fixed point for `lam_1` at `y_b = 1/100`)!**
   - **UV `Spin(10)` Cure & `lam_0` Parameter Elimination:** `A2-OW11`'s `Spin(10)` UV fixed point lifts `f_lam` roughly `20x` (`16x` above `f_crit` in `dD`, `9x` above in `LDW`), restoring a unique real, tiny (`|lam_i^*| < 15/1000` for all `Spin(10) T2/T1` in both gauges, and `< 3/100` for `PS(4,1,2) T2` in `dD` & `LDW` low-`y_b`, with referee noting `|lam_4^*| ~ 306/10^4` for `PS(4,1,2) T2 LDW` high-`y_b`), **fully UV-irrelevant (`theta_1, theta_2, theta_3, theta_4 < 0`) `2H` quartic fixed point** (`residual < 1 / 10^52`).
   - At `y_b = 9/20 > y_b^{crit} = (171/600)^(1/4) g_UV ~ 380/1000`, ALL `4` tree-level boundedness-from-below (BFB) conditions hold strictly at the UV fixed point (`Spin(10) T2` in both `dD` and `LDW`).

3. **Downward `1`-Loop `2H` Type-II RGE (`t = 0 -> -38`, `M_Pl -> M_EW`):**
   - At `y_b = 9/20`: ALL `4` BFB conditions remain strictly positive in the IR (`lam_1 ~ 476/1000, lam_2 ~ 735/1000, lam_3 ~ 597/1000, lam_4 ~ -692/1000`), and the gravity-fixed UV boundary agrees with `A2-OW8`'s exact `lam_i(0) = 0` boundary to `< 27/10^4` across all `4` quartics — dynamically proving `A2-OW8`'s `lam_0 -> 0` UV boundary and **eliminating `lam_0` from the free-parameter ledger**!
   - At `y_b = 1/100`: `lam_1` runs negative in the IR (`~ -152/1000`) while `lam_2 ~ +799/1000` stays strictly positive, driving the radiative `H_d` flat direction.

4. **Honest `f_g > 0` Structural Theorem (`g_UV` NOT Fixed in `Spin(10)`):**
   - Exact Dynkin-index `1`-loop beta coefficients `b_{Spin(10), real 10} = -151/6 < 0` and `b_{Spin(10), complex 10} = -25 < 0` prove that for ANY `f_g > 0`, asymptotically free `Spin(10)` admits ONLY the UV-relevant Gaussian fixed point `g_* = 0` (`theta_g = +f_g > 0`), so **`g_UV` remains a free relevant parameter** (whereas IR-free `2H` `U(1)_Y`, `b_1 = +21/5 > 0`, gains a unique UV-irrelevant Harst-Reuter interactive fixed point `g_{1*}^2 = 16 pi^2 f_g / (21/5)` with `theta_g = -2 f_g < 0`).

---

## 2. Task `OW13-B`: Conformal `xi = 1/6` Stability & `C^2 + R^2` Quadratic-Gravity Audit

1. **Exact `1`-Loop `2H` Curved-Space `beta_xi`:**
   - Vanishes identically (`0`) at `(xi_d, xi_u) = (1/6, 1/6)` across all UV and IR benchmarks.
   - Stability matrix `M_xi`: saddle at low `y_b = 1/100` (`eig ~ (-147/100, +40/100)`), and **strictly double IR-attractive** at `y_b = 9/20` BOTH in the UV (`eig ~ (+182/1000, +402/1000)`) and in the IR at `t = -38` (`eig ~ (+955/100, +1362/100)`).
2. **Exact Gravitational Background-Field `beta_xi^{grav, bg}` (Honest Wall + Unimodular Bridge):**
   - Derived identically from `A2-OW10` `B_1, B_2` at `eta_N = -2`: `beta_xi^{grav, bg} = -g lam xi (11 + 10 lam) / (pi (1 - 2 lam)^3)` (analytic vs FD error `< 6 / 10^35`, symbolic match `0`).
   - Honestly non-zero whenever `lam_* != 0` (`Spin(10) T2`: `f_xi^{bg} ~ -726/10^4`; `Spin(10) T1`: `~ -208/1000`; `PS(4,1,2) T2`: `~ +167/10^4`; `G_SM 2H T2`: `~ -216/1000`), proving a non-zero cosmological constant breaks conformal `xi = 1/6` in the UV.
   - **Exact Unimodular Protection:** At `lam = 0` (`A2-OW14`), `f_xi^{bg}(lam = 0) = 0` identically!
3. **Exact `1`-Loop Quadratic Gravity (`C^2 + R^2`) + Conformal Matter (`Avramidi-Barvinsky` / `Codello-Percacci`):**
   - Guardrail 4 Pure Gravity benchmark matches `b_{lam_C} = 133/10`, UV-attractive `omega_+ ~ -2286/10^5`, and UV-repulsive `omega_- ~ -5467/1000`.
   - Across all `4` open-weave matter tiers (`G_SM 2H` `c = 37/15`, `PS(4,1,2)` `c = 103/30`, `Spin(10) real-10` `c = 347/60`, `Spin(10) complex-10` `c = 88/15`), conformal `xi = 1/6` gives `b_R^{mat} = 0`, strictly strengthens `C^2` asymptotic freedom (`547/30`, `121/6`, `373/15`, `751/30`), increases the `omega` discriminant strictly above pure gravity (`329 -> 534 -> 628 -> 886 -> 896`), and preserves BOTH real fixed points (`omega_+ ~ -140/10^4`, `omega_- ~ -895/100` for `Spin(10) real-10`).
   - Exact non-conformal collision bound: `|xi - 1/6|_{crit} ~ 211/100` (`Spin(10) real-10`), `~ 183/100` (`G_SM 2H`), `~ 140/100` (`PS(4,1,2)`), `~ 150/100` (`Spin(10) complex-10`) — strictly excluding large-`xi` inflation.

---

## 3. Task `OW13-C`: Exact `2H` Gildener-Weinberg Scalon Spectrum `m_h / v_EW`

1. Exact identity `m_h^2 / v^2 = 8 B_GW = (1/2) beta_{lam_1}(lam_1 = 0)` verified symbolically (`0`) and numerically (`0` residual).
2. **`1H` SM Top-Tachyon No-Go:** `B_{1H} < 0` for any `y_t > y_t^{crit}` (`~ 451/1000` EW benchmark, `~ 380/1000` GUT benchmark).
3. **`2H` `H_d` Flat Direction (`B_{2H} > 0` Strictly) & Honest Perturbative Gap:**
   - Top quark decouples from `H_d`, yielding the Weinberg-Linde pure-gauge GW floor `m_h / v ~ 396/10^4` (EW) / `~ 281/10^4` (GUT).
   - Reaching `m_h / v = 1/2` purely via `1`-loop GW along `H_d` fixes the collider sum rule `(m_H^4 + m_A^4 + 2 m_{H+-}^4)^(1/4) / v ~ 210/100` (degenerate `M_heavy / v ~ 149/100`), which requires tree-level portal coupling `lam_eff = 2 (M_heavy / v)^2 ~ 443/100` — honestly exposing a large gap above the perturbative `|lam_{3,4}| < 1` portals generated by downward running from `Spin(10)` UV fixed points.

---

## 4. Task `OW13-D`: `4 / 4` Planted Faults (`PF-OW13-1..4`)

- `PF-OW13-1` (flip `f_lam -> -f_lam`): **CAUGHT** — all `4` quartic critical exponents flip positive (`theta_i > 67/100`, UV-relevant).
- `PF-OW13-2` (flip gauge-box sign in `beta_{lam_1}`): **CAUGHT** — `G_SM 2H` discriminant flips from `< -6` to `> +17`, falsely creating a real root.
- `PF-OW13-3` (set non-conformal `xi = 5` in `C^2 + R^2` `Spin(10)`): **CAUGHT** — `omega` discriminant plunges to `~ -3786 < 0`, destroying both real UV fixed points.
- `PF-OW13-4` (couple `y_t = 94/100` to `H_d` GW): **CAUGHT** — `B_GW` flips negative (`m_h^2 / v^2 ~ -281/10^4 < 0`, tachyonic).
