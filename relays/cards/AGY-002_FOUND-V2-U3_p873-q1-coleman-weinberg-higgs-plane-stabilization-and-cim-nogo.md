# Card `AGY-002_FOUND-V2-U3` — `P-873 Q1/Q2` `1`-Loop Radiative Quartic vs `CW`/`Berezin` Dichotomy on `2D` Higgs Plane `E`, `U_M` Ray Orbit, & Analytical `CIM` `[R_*, G] = 0` No-Go Theorem (`0 of 19`)

## 1. Package and Question

Resolving `P-873 Q1` (`sign of quartic anisotropy B on E = span(v_+, v_-)`), extending `P-873 Q2` & `Q3`, and proving why `CIM (3,3,-6)` alone cannot simultaneously stabilize `h_*` AND align `CKM` (`0 of 19`):

1. **Exact Zero-Entry Classification (`P-873 Q2`), `12`-Ray `U_M` Orbit, & Tree Quartic Anisotropy:**
   - Construct the level-`6` `Weil` operators `T_6, S_6` and commutator `U_M = T_6 S_6 T_6^dag S_6^dag` on `C^6`, extract the orthonormal basis `(v_+, v_-)` of the `2D` ground plane `E` (`phases +-pi/6`, normalized and phased so `h_* = (v_+ + v_-)/sqrt(2)` vanishes at modes `2, 3, 4`).
   - Prove symbolically (`SymPy == 0`) and numerically (`55` digits, `< (1/10)^50`) the `3` exact zero-entry directions `-v_+[k] / v_-[k]`: mode `0` (`|r| = 2 - sqrt(3), arg = pi`), modes `{1, 5}` (`|r| = 2 + sqrt(3), arg = pi`), and modes `{2, 3, 4}` (`|r| = 1, arg = 0`, i.e. `h_*`), generating `12` distinct projective rays `{U_M^k h_*}` under the `12`-fold unitary symmetry `U_M`.
   - Evaluate the standalone `2D` torus profile integral `V_4^{frozen}(h) = int_{E_tau} |Phi_h(z)|^4 d^2z` on a `24 x 24` grid at `tau in {13/100 + 17/10 i, i, 2 sqrt(3) i}`: prove `B_{frozen}^{P873} = V_4^{frozen}(v_+) - V_4^{frozen}(h_*) < -1 < 0` and `V_4^{frozen}(v_+) - <V_4^{frozen}>_{circle} < -1/5 < 0` at all `3` moduli (`tree overlap prefers eigenlines v_\pm and maximizes at h_*`), while symbolic `Cartan` relaxation gives `B_{tree, relaxed} == 0`.
2. **`1`-Loop Radiative Box vs Scale-Dependent `CW` & `Berezin` Determinant Dichotomy (`P-873 Q1`, `Guardrail 1`):**
   - Build the `24`-point order-`5` `CIM (3,3,-6)` `Yukawa` overlap tensors (`up (1,-4, -3/2*2)`, `down (1,2, 3/2*2)`, `lepton (-3,6, 3/2*2)`, `z_H = (q_L + q_R)/2 * w`) by standalone `2D` torus quadrature (`zero closed form`, avoiding any target-embedded ansatz) at bulk `tau = 13/100 + 17/10 i` and cusp `tau = 13/100 + 6 i`:
     * **Scale-free UV radiative box quartic `V_{box}(h) = -(1/24) sum_{w,f} N_c Tr[H_f(w, h)^2]` (`H_f = (Im tau) M_f M_f^dag`, coefficient of `ln Lambda_{UV}^2`):** prove `B_{box}^{P873}(v_+) = V_{box}(v_+) - V_{box}(h_*) > +15` at `y = 17/10` and `> +100` at `y = 6` (`and V_{box}(v_-) - V_{box}(h_*) > +15` at both), and attains its `216`-point `(9 theta x 24 phi)` `S^3 subset E` global minimum at `h_*` (`theta = pi/2, phi = 0`) at `y = 17/10` and its `24`-point equal-magnitude circle minimum at `h_*` (`modulo 2 pi / 12` under `U_M`) at both `y = 17/10` and `y = 6`.
     * **Scale-dependent `1`-loop `CW` `V_{CW}(h; mu) = -(1/24) sum_{w,f} N_c Tr[H_f^2 (ln(H_f / mu^2) - 3/2)]` & `B1941` functional/scale dichotomy:** prove that at `y = 6, mu = 1`, `V_{CW}(v_+; 1) - V_{CW}(h_*; 1) > +150 > 0` with `24`-point circle minimum at `h_*`; whereas at the canonical `U_M`-invariant Frobenius scale `mu_E^2 = (1/24) sum_{w,f} N_c Tr[H_f(w, v_+)]`, `ln(H_f / mu_E^2) < 0` flips the sign (`V_{CW}(v_+; mu_E) - V_{CW}(h_*; mu_E) < -40 < 0` at `y = 17/10` and `< -200 < 0` at `y = 6`), matching `Berezin` determinant `V_{det}(h) = -(1/24) sum_{w,f} N_c ln det H_f(w, h)` (`V_{det}(h_*) - min_{circle} V_{det} > +60` at `y = 17/10` and `> +250` at `y = 6`).
3. **Analytical `CIM` `[R_*, G] = 0` No-Go Theorem on `E`:**
   - Prove symbolically (`SymPy == 0`) and numerically (`< (1/10)^40`) that `[R_*, G_u(tau, h_*)] == 0` identically at all `24` order-`5` points of shifted `Frame D1` (`maximal 1-3 CKM mixing at the mark`) AND at unshifted `CIM(0,0,0)` (`xi = 0`, where `Theta_{6-c}(tau, 0) == Theta_c(tau, 0)` forces `[R_*, G_{(0,0,0)}(h_*)] < (1/10)^40` and singular-value ratio exponents `(0, 4/3)` within `< 2/1000` across `y = 11 -> 14`).

## 2. Deliverables and Definition of Done

- Both producer (`relays/agy002_found_v2_u3/verify_found_v2_u3.py`, using `2D` torus cell quadrature) and cold-room referee (`relays/agy002_found_v2_u3_referee/referee_found_v2_u3.py`, using `1D` unfolded universal-cover quadrature / Jacobi `Theta_c(6 tau, 6 xi)` theta series) pass `AST` zero-float/zero-complex-literal checks, `0` repo imports, and matching `SCRIPT_SHA256.txt` / `OUTPUT_SHA256.txt` seals (`A`-only commits).

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PFU3-1` (`Guardrail 1` Target-Embedded Potential):** `V_{fake}(h) = 1 - |<h_* | h>|^2` breaks `12`-fold `U_M` invariance across the `12`-ray orbit `{U_M^k h_*}` by `> 1/2`.
2. **`PFU3-2` (`Frozen Tree Overlap Sign`):** Frozen tree quartic `V_4^{frozen}` gives `B_{frozen}^{P873} < -1 < 0` (`maximizes along h_*`).
3. **`PFU3-3` (`Berezin Determinant Reversal`):** Swapping `V_{box}` for `V_{det}` turns `h_*` into a steep non-minimum (`> +60` above circle minimum at `y = 17/10`).
4. **`PFU3-4` (`Un-Averaged 1-Point Quadratic Mass`):** At a single order-`5` point `(1/5, 1/5)`, un-averaged quadratic mass `sum_f N_c Tr[M_f(w_0, h)^dag M_f(w_0, h)]` breaks `(v_+, v_-)` isotropy by `> 1/5` (`relative |v_+ - v_-| / v_+`).
5. **`PFU3-5` (`Guardrail 3` `Haar` Basis Test):** `10`-trial random `Haar SU(3)` invariance of singular-value ratios `< (1/10)^30` vs raw entry ratio `|M_{00} / M_{22}|` shifting by `> 1/5`.

## 4. Firewall

Strict `0 of 19`; touches only `relays/`; `0` imports from `frontier/` or other seats; expectations committed first (`0 of 19`).
