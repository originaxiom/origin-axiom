# Card `AGY-002_CLOSURE-G6` — Modular-Covariant `Majorana` Seesaw, `TM1` `RGE` Survival, and Repaired `3`-Family `Pati-Salam x Z2^D` `2`-Loop `IR` Surfaces (`0 of 19`)

## 1. Package and Question

Completing `P-862` Step `2` under strict `0 of 19` firewall, `Guardrails 1-6`, and exact rational/integer mask-safe bounds:
1. Can `3` linearly independent, cutoff-free, weight-`0` `SL(2, Z)`-covariant symmetric `3 x 3` `Majorana` tensors `(J_0(tau), J_1(tau), J_2(tau))` be built directly from `CIM (3, 3, -6)` gauge-singlet overlaps at `z = 0`, how many irreducible continuous `Majorana` parameters survive (`Guardrails 1 & 5`), and why is an all-ones orthonormal row sum basis-dependent?
2. When a `Z_2` residual symmetry fixes the `1`st `PMNS` column to trimaximal `TM1` (`I_TM1 = |U_{e1}|^2 = cos^2 theta_12 cos^2 theta_13 = 2/3`), how tightly does `I_TM1` survive downward `Weinberg` + `SM` `RGE` evolution across normal-hierarchy histories?
3. Replacing falsified single-step `SU(5)` (`Delta_PS = 0`), the `-24 lambda^2 Tr_Y` quartic bug, and `N_g = 6` chiral doubling with `3`-family (`N_g = 3`) `E_6 -> Pati-Salam x| Z_2^D` + repaired `-48 lambda^2 Tr_Y` `BPV` `2`-loop `RGE`, what are the exact universal `2`-loop `IR` bounds on `|bar_theta_QCD(IR)|`, the `Pati-Salam` gauge residual `delta_{2-loop}`, and the `D`-term `Higgs` ratio `sqrt(2 lambda_IR) = m_H / v_EW` across all `243` perturbative grid histories?

## 2. Deliverables and Definition of Done

1. **Cutoff-Free `SL(2, Z)`-Covariant `(J_0, J_1, J_2)` `Majorana` Basis & Honest `CP^2` Parameter Count (`Guardrails 1, 3, 5`):**
   - Construct `v_0(tau)_k = psi_k^{(6)}(0; tau, 0)`, `G_6(tau) = Y_0^dag Y_0`, `J_0 = Y_0 . v_0` (`exact rank 1`), `J_1 = Y_0 . (G_6 v_0)` (`rank 3`), and `J_2 = J_1 J_1^dag J_1` (`rank 3`) from `Y_0(tau) = Y_cim(tau; 0, 0)`.
   - Verify symmetry (`||J_a - J_a^T|| < (1/10)^14`), `T` and `S` covariance `J_a(gamma tau) = U_3(gamma) J_a(tau) U_3(gamma)^T` (`< (1/10)^12`), span rank `3` in `Sym^2(C^3)`, physical sensitivity of `sv_2 / sv_3` to relative complex phases in `(c_0 : c_1 : c_2) in CP^2` (`shift > 1/200`, pricing `4` real projective ratios + `1` scale `M_0 / v_EW` generally, or `2 + 1` on `CP`-real `Re(tau) = 0`), and `10`-trial `U(3)^6` `Haar` invariance of `Type-I` seesaw `kappa_W = Y_nu M_R^{-1} Y_nu^T` (`< (1/10)^13`).
2. **Trimaximal `TM1` Sum-Rule Emergence & Downward `RGE` Corridor (`P-862` Live Relation):**
   - Verify exact `UV` `TM1` invariant `I_TM1(UV) = |U_{e1}|^2 = 2/3` (`diff < (1/10)^14`) at non-zero reactor mixing `|U_{e3}|^2 = 1/48` and non-trivial `CP` phase, and prove across normal-hierarchy downward `RGE` evolution (`dt = -30`, `y_tau in {1/100, 1/20, 1/5}`) that `|I_TM1(IR) - 2/3| < 1/200` (`and < 1/2000` for `y_tau <= 1/20`).
3. **Exact `243`-History `3`-Family `Pati-Salam x Z2^D` Universal `2`-Loop `IR` Envelopes:**
   - Across `alpha_U^{-1} in {52, 60, 68} x Delta_PS in {0, 2, 4} x Delta_SM in {26, 28, 30} x y_t(M_PS) in {1/2, 7/10, 9/10} x cos^2(2 beta) in {0, 1/2, 1}` (`243` histories) with tree-level bidoublet `D`-term `lambda(M_PS) = (1/4) g_2^2(M_PS) cos^2(2 beta)` and `D`-symmetric `3`-family complex Yukawas:
     1. `max |bar_theta_QCD(IR)| < (1/10)^13` (`with |J_CKM| > 1/1000`);
     2. `2`-loop `Pati-Salam` gauge residual `delta_{2-loop} = sin^2 theta_W(IR) - [23/134 + (109/201)(alpha_EM / alpha_3) + (506 / (201 pi)) alpha_EM Delta_PS]` bounded strictly inside **`[7/10000, 3/1000]`** across all `243` histories;
     3. `2`-loop `Higgs`-to-`VEV` ratio `sqrt(2 lambda_IR) = m_H / v_EW` (`with exact -48 lambda^2 Tr_Y`) bounded strictly inside **`[35/100, 78/100]`** (`min lambda_IR > 1/20 > 0` vacuum stability across `243 / 243` histories).

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Any `T/S` covariance error `>= (1/10)^12` on `(J_0, J_1, J_2)`, span rank `!= 3`, `Seesaw` `Haar` drift `>= (1/10)^13`, or `TM1` `RGE` excursion `>= 1/200`.
- Any breach of `[7/10000, 3/1000]` on `delta_{2-loop}`, `[35/100, 78/100]` on `sqrt(2 lambda_IR)`, or `(1/10)^13` on `|bar_theta_QCD(IR)|` across the `243` histories.
- Any float/complex literal in source or failure to catch any of `PF6.1..PF6.5`.

## 4. Five Planted Fault Controls That Must Fail When Broken

1. **`PF6.1` (`Basis-Dependent Orthonormal All-Ones Row Sum`):** Applying an `SO(3)` rotation to the `Frobenius`-orthonormalized `(E_0, E_1, E_2)` basis must shift `sv_2 / sv_3` of `E_0 + E_1 + E_2` by `> 1/10` (`refuting 0-parameter isotropy claims`).
2. **`PF6.2` (`TM2 Column Swap Falsifier`):** Placing `u_2 = (1, 1, 1)^T / sqrt(3)` (`|U_{e2}|^2 = 1/3`) in column `1` instead of `u_TM1` must violate `|I_TM1 - 2/3| > 1/4`.
3. **`PF6.3` (`N_g = 6 Chiral Family Doubling Gauge Ruin`):** Replacing `N_g = 3` (`b_3 = -7`) by `N_g = 6` (`b_3 = -3`) over `Delta_SM = 28` must shift `alpha_3^{-1}(IR)` by `> 15`.
4. **`PF6.4` (`-24 vs -48 lambda^2 Tr_Y Factor-of-2 Bug Across 243-History Grid`):** Switching `-48` to `-24` must shift `max |Delta sqrt(2 lambda_IR)| > 1/1000`.
5. **`PF6.5` (`Tautological Bloch-Wigner Conjugation Identity D(conj(z)) + D(z) == 0`):** Evaluating `|D(z) + D(conj(z))|` at an asymmetric complex shape `z = 3/5 + (4/5) i` (`not m004!`) must still return `< (1/10)^15`, proving `D(z) + D(conj(z)) = 0` cannot discriminate amphichirality or select `theta_YM = 0` over `pi`.

## 5. Dependencies and Firewall Boundaries

Rests on `Weinberg` (`1979`), `Machacek-Vaughn` (`1983-1985`), `Bednyakov-Pikelner-Velizhanin` (`2014`), and `Gates 1-5`. Strict `0 of 19` firewall; touches only files under `relays/`. Expectations committed first (`0 of 19`).
