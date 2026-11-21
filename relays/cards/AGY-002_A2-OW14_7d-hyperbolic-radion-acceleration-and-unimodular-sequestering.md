# AGY-002 Pre-Registration Card `A2-OW14`: Unfreezing `7D` Spacetime (`M_4 x M_3` Hyperbolic Radion & Townsend-Wohlfarth Acceleration) and Unimodular / Kaloper-Padilla Vacuum Sequestering (`0 of 19`)

- **Seat:** `AGY-002`
- **Branch:** `agy-002/verify`
- **Card ID:** `A2-OW14`
- **Empirical inputs:** **`0 of 19`** (zero PDG or cosmological-parameter inputs; pure `7D -> 4D` differential geometry, Friedmann-radion dynamics, Litim unimodular FRG, and variational sequestering algebra; Guardrail 4 literature benchmarks for `Townsend-Wohlfarth (2003)` hyperbolic `n = 3` exponent and `Kaloper-Padilla (arXiv:1309-6562)` global sequestering identity are verified directly from first principles).
- **Guardrails:** `0` float/complex AST literals in `.py` (exact `Fraction`, `sympy`, integer-built `mpmath` at `>= 55` dps); `0` `frontier/` imports; zero hardcoded proof flags; Guardrail 1 zero post-inspection pinning of `L_*`; `A`-only `SHA-256` manifests; Cold-Room Referee disjoint methods (`0` discrepancies, `4/4` planted faults).

---

## 1. Scientific Scope & Hypotheses

Card `A2-OW14` executes Phase 4 of Campaign 2: unfreezing the `7D` internal hyperbolic volume modulus `L(x)` on `M_4 x M_3` (`M_3 = H^3 / Gamma`, e.g. `m004`), quantifying both static volume stabilization and dynamical hyperbolic cosmic acceleration, and formally auditing whether **Unimodular Gravity (`det g = -1`, `lam = 0`)** and **Kaloper-Padilla global sequestering** cleanly decouple the `n_F > n_B` vacuum energy (`a_0 = -64`, `6D` bulk `-6 / -2 / -1`, and `AdS_4` radion minima) without breaking `A2-OW4` (`N = 5`), `A2-OW9` (`tau_*`), `A2-OW10` (`N_gen = 3`), `A2-OW11` (`Spin(10)` weak FRG), or `A2-OW13` (conformal `xi = 1/6` and `lam_0 -> 0`).

---

## 2. Frozen Specification & Pass/Fail Acceptance Criteria

### Task `OW14-A`: `7D -> 4D` Einstein-Frame Radion, Townsend-Wohlfarth Hyperbolic Acceleration, & Volume Stabilization

1. **First-Principles `7D` Christoffel / Ricci Dimensional Reduction (`M_4 x M_3`):**
   - Construct the explicit `7 x 7` diagonal time-dependent metric `g_{MN} = diag(-e^{2 a sig(t)}, e^{2 a sig(t)}, e^{2 a sig(t)}, e^{2 a sig(t)}, e^{2 b sig(t)}, e^{2 b sig(t)}, e^{2 b sig(t)})`, directly compute all `7^3` Christoffel symbols `Gamma^A_{BC}`, Ricci tensor `R_{BC}`, and `L_eff = (1/2) sqrt(-g_7) R_7`.
   - Enforce `4D` Einstein frame (`2 a + 3 b = 0 => a = -(3/2) b`), subtract the exact total time derivative `d/dt(c_pp * sig')`, and verify `L_kin = (15/4) b^2 (sig')^2`.
   - Solving `L_kin = (1/2) (sig')^2` yields exact canonical `b = sqrt(2/15)` and `a = -sqrt(3/10)` (`Townsend-Wohlfarth 2003` `n = 3` benchmark).
   - Compute exact `4D` Einstein-frame exponential potential slopes `gamma_i` (`V_i proportional to e^{-gamma_i phi}`), slow-roll `eps_V = gamma_i^2 / 2`, and scaling attractor `w_attr = gamma_i^2 / 3 - 1`:
     - Bulk `Lambda_7` (`L^-3`): `gamma_Lam = sqrt(6/5) < sqrt(2)`, `eps_V = 3/5`, `w_attr = -3/5 < -1/3` (accelerating).
     - Hyperbolic curvature `R(H^3) = -6 / L^2` (`L^-5`): `gamma_curv = sqrt(10/3) > sqrt(2)`, `eps_V = 5/3`, `w_attr = 1/9 > -1/3` (non-accelerating).
     - `7D` CS `3`-form flux (`L^-9`): `gamma_flux = 3 sqrt(6/5) > sqrt(2)`, `eps_V = 27/5`, `w_attr = 13/5`.
     - `1`-loop `n_F > n_B` Casimir (`L^-10`): `gamma_Cas = 2 sqrt(10/3) > sqrt(2)`, `eps_V = 20/3`, `w_attr = 31/9`.
   - Certify the **Single-Term Slow-Roll No-Go**: curvature, flux, and Casimir ALL satisfy `gamma_i > sqrt(2)` (`eps_V > 1`, `w_attr > -1/3`).

2. **Exact Closed-Form Townsend-Wohlfarth Hyperbolic Transient Acceleration (`H^3`, `gamma = sqrt(10/3)`):**
   - From the exact `1D` autonomous Friedmann-radion equation `dx/dN = (1 - x^2)(sqrt(5) - 3 x)` (`x = phidot / (sqrt(6) H)`, `w = 2 x^2 - 1`, accelerating band `|x| < 1/sqrt(3)`, attractor `x_* = sqrt(5)/3`), certify the exact closed-form supremum of transient acceleration `e`-folds:
     `N_accel_max(H^3) = (3/4) ln((sqrt(5) + sqrt(3)) / (sqrt(5) - sqrt(3))) - (sqrt(5)/4) ln((sqrt(3) + 1) / (sqrt(3) - 1))`.
   - Cross-check `N_accel_max(H^3)` THREE ways:
     (i) exact closed form (`81/100 < N_accel_max < 82/100`, strictly `< 1 << 60`, certifying the single-radion `60`-`e`-fold inflation no-go!),
     (ii) direct `55`-dps numerical quadrature of `1 / ((1 - x^2)(sqrt(5) - 3 x))` over `[-1/sqrt(3), +1/sqrt(3)]` matching to `< 1/10^45`,
     (iii) direct cosmic-time `4D` Friedmann + radion ODE (`3 H^2 = (1/2) phidot^2 + e^{-gamma phi}`, `phiddot + 3 H phidot - gamma e^{-gamma phi} = 0`) rolling up from `x_0 = -999/1000` with exact `w = -1/3` and `phidot = 0` event detection: verify de Sitter bounce `|w_min + 1| < 1/10^12`, `|N_accel_ode - N_accel_max| < 1/10^11`, and late-time approach to `w_attr = 1/9` (`|w(t = 200) - 1/9| < 2/1000`).
   - Also compute `N_accel_max(H^n)` for `n in {2, 3, 4, 6}` verifying `N_accel_max(H^2) < N_accel_max(H^3) < N_accel_max(H^4) < N_accel_max(H^6) < 2`.

3. **Exact `7D` Hyperbolic Volume Stabilization Theorem (Guardrail 1 Zero-Pinning):**
   - For `V(L) = c_3 L^-3 + c_5 L^-5 + c_9 L^-9 + c_10 L^-10` with strictly positive hyperbolic curvature (`c_5 > 0`), `3`-form flux (`c_9 > 0`), and `n_F > n_B` Casimir (`c_10 > 0`):
     - **dS/zero bulk (`c_3 >= 0`):** verify `V'(L) < 0` strictly for all `L > 0` (runaway decompactification no-go, `0` positive roots).
     - **AdS bulk (`c_3 = -|c_3| < 0`):** verify via exact Descartes / Sturm root count on the benchmark `(|c_3|, c_5, c_9, c_10) = (1, 1, 1, 1)` AND symbolic elimination of `|c_3|` from `V'(L_*) = 0` that there is a **unique strictly stable volume minimum `L_* > 0`** with `V''(L_*) = 2 (5 c_5 L_*^5 + 27 c_9 L_* + 35 c_10) / L_*^12 > 0` (positive radion mass squared!) AND strictly negative `AdS_4` vacuum energy `V(L_*) = -(2 c_5 L_*^5 + 6 c_9 L_* + 7 c_10) / (3 L_*^10) < 0` (exact `7D` Maldacena-Nunez AdS stabilization theorem).
     - **Minkowski lift with negative intermediate term (`V = c_5 L^-5 - c_6 L^-6 + c_9 L^-9`):** verify exact simultaneous `V(L_*) = 0, V'(L_*) = 0` yields `c_6 = (4/3) c_5 L_*`, `c_9 = (1/3) c_5 L_*^4`, and `V''(L_*) = 4 c_5 / L_*^7 > 0`.

---

### Task `OW14-B`: Unimodular Gravity (`det g = -1`, `lam = 0`) & Kaloper-Padilla Global Sequestering

1. **Unimodular Trace-Free Einstein Decoupling & Moduli Preservation:**
   - Verify explicitly on `4 x 4` symbolic metric/stress-energy tensors that `T_{ab} -> T_{ab} - rho_vac g_{ab}` shifts the trace-free tensor `T_{ab} - (1/4) g_{ab} T` by identically `0` (decoupling `a_0 = -64`, `6D` bulk `-6/-2/-1`, and `V(L_*) < 0`), while any dynamical scalar potential `V(phi)` retains its exact Klein-Gordon equation `Box phi - V'(phi) = 0` via covariant conservation `nabla^a T_{ab} = 0` (preserving `A2-OW9` `tau_*` and `OW14-A` `L_*` stabilization untouched).
2. **Unimodular Asymptotic Safety FRG (`lam = 0` Fixed) — Double-Pincer `N_gen = 3` Survival:**
   - Evaluate `A2-OW10` Litim Type-II `B_1(0) = (M_g - 22) / (6 pi)`, `B_2(0) = 1 / (12 pi)` (`cap = 23` full `lam = 0` slice) AND traceless unimodular `B_1^{tr}(0) = (M_g - 21) / (6 pi)`, `B_2^{tr}(0) = 1 / (12 pi)` (`cap = 22`):
     - Certify exact closed forms `g_* = 12 pi / (cap - M_g)` and UV-relevant critical exponent `theta_g = 2 (cap - M_g) / (cap - 1 - M_g) > 2` for all `M_g < cap`.
     - Certify the exact **Unimodular Double Pincer `0 < M_g < cap`** for `G_SM 2H` (`M_g = 16 N_gen - 40`):
       - Full (`cap = 23`): `5/2 < N_gen < 63/16` -> **unique integer `N_gen = 3`** (`g_* = 4 pi / 5`, `theta_g = 15/7`; `N_gen = 4` has `M_g = 24 >= 23`, excluded!).
       - Traceless (`cap = 22`): `5/2 < N_gen < 31/8` -> **unique integer `N_gen = 3`** (`g_* = 6 pi / 7`, `theta_g = 14/6 = 7/3`; `N_gen = 4` excluded!).
     - Re-enumerate all `21` `Delta(2,3,N)` (`N = 2..5`) faithful coset actions directly from permutation groups and certify that **`N = 5, d = 5` (`A_5 / A_4`, `1 of 21`) remains uniquely selected** under `(chiral & anomaly_free & 0 < M_g < cap)` for BOTH `cap = 23` and `cap = 22`.
     - Certify UV `Spin(10) real-10` unimodular fixed points survive BOTH Type-II (`M_g = -122`, `g_* = 12 pi / 145` full / `12 pi / 144 = pi / 12` traceless) and Type-I (`M_g = -74`, `g_* = 12 pi / 97` full / `12 pi / 96 = pi / 8` traceless).
     - Certify `A2-OW13` bridges at `lam = 0`: (i) `f_xi^{bg}(lam = 0) = 0` identically (conformal `xi = 1/6` protected!), and (ii) for bare `G_SM 2H` (`g_* = 4 pi / 5`), `f_lam^{(dD)}(lam = 0) = 20 g_* / (3 pi) = 16/3 > 5 >> f_crit ~ 404/10^4`, curing even bare `G_SM 2H`'s `lam_1` collision wall!
3. **Kaloper-Padilla (`arXiv:1309-6562`) Global Vacuum Sequestering Verification:**
   - Directly vary `S = V_4 (-Lam_bare + lam_s^4 (L_0 - rho_vac)) + sigma(Lam_bare / (lam_s^4 mu^4))` with respect to global `(Lam_bare, lam_s)` (with metric scaling `g^{ab} -> lam_s^{-2} g^{ab}` producing `K_sym = g^{ab} dL_m / dg^{ab}` and `T^{phys} = lam_s^4 (4 (L_0 - rho_vac) - 2 K_sym)`).
   - Certify exact identities `Lam_bare = (1/4) <T^{phys}>`, `Lam_res = Lam_bare + lam_s^4 rho_vac = (1/4) <T^{mat}>`, and `d(Lam_res) / d(rho_vac) == 0` identically (exact sequestering of `a_0 = -64` and `V(L_*) < 0`, contingent on finite `0 < V_4 < infty`).

---

### Task `OW14-C`: `4 / 4` Planted Fault Controls (`PF-OW14-1..4`)

- `PF-OW14-1`: Corrupt `7D` Einstein-frame exponent `a = -(3/2) b` to `a = -b` -> `2 a + 3 b != 0` and canonical `b` shifts strictly away from `sqrt(2/15)`.
- `PF-OW14-2`: Flip AdS bulk sign `-|c_3| -> +|c_3|` (`c_3 = +1`) in `V(L)` -> `0` positive extrema (destroys the stable volume minimum).
- `PF-OW14-3`: Evaluate `N_gen = 4` (`M_g = 24`) in unimodular FRG (`cap = 23` and `22`) -> `g_* < 0` (no physical UV fixed point).
- `PF-OW14-4`: Omit the `lam_s^4` metric rescaling (`T^{phys} = 4 L_0 - 2 K_sym - 4 rho_vac` with unscaled `rho_vac`, varying only `Lam_bare` at fixed `lam_s = 1` without global scale constraint) -> `d(Lam_res) / d(rho_vac) = +1 != 0` (vacuum energy fails to sequester).

---

## 3. Custody & Referee Protocol

1. Commit 1: seal this Card before any producer code exists.
2. Commit 2a / 2b: seal `relays/a2_ow14/verify_a2_ow14.py` pre-run (`A`-only `SCRIPT_SHA256.txt`), run once, seal `a2_ow14_results.json` & `OUTPUT_SHA256.txt` unread.
3. Independent Cold-Room Referee (`relays/a2_ow14_referee/`): reads ONLY this Card prior to Commit 4b, implements disjoint methods (conformal-transformation curvature formula rather than explicit `7^3` Christoffel loop, disjoint `RK4` / `Radau` Friedmann ODE + direct `1D` autonomous `dx/dN` integrator, disjoint `sympy` Sturm/Descartes root audit, disjoint unimodular algebra & permutation group builder), seals Commit 4a/4b unread, and certifies `0` discrepancies + `4/4` planted faults.
4. Relay `relays/AGY002_A2_OW14_RESULTS.md` + `STATUS_AGY-002.md` item `24` + `7`-point audit + fast-forward push to `origin/agy-002/verify`.
