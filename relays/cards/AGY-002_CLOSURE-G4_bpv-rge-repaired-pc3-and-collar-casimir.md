# Card `AGY-002_CLOSURE-G4` — Canonical `BPV` `2`-Loop Matrix `RGE`, Repaired Non-Commuting `P-C3` `Schur` Package, and `4D` `m004` Collar Spectral `Casimir` Law (`0 of 19`)

## 1. Package and Question

Advancing from `ENDGAME-V2` (`Gates 0-3`) under strict `0 of 19` firewall, `Guardrails 1-6`, and mask-safe exact rational/integer bounds:
1. Does upgrading the `3`-family `SM + Pati-Salam x Z2^D + Weinberg` `2`-loop matrix `RGE` to exact Hermitian-`MSbar` `Bednyakov-Pikelner-Velizhanin` (`2014`, Eq. `27`) mixed-Yukawa ordering (`-(1/4) H_u H_d - H_d H_u`) while retaining exact `Machacek-Vaughn` (`1985`) `-48 lambda^2 Tr_Y` simultaneously reproduce `Buttazzo et al.` (`2013`) criticality, the exact `Barger-Berger-Ohmann` (`1993`) rank-`1` `2`-loop `CKM` mixing law `-11/2`, `3`-family `D`-parity `Strong-CP` vanishing, and `U(3)^6` `Haar` invariance?
2. When `physical`'s `P-C3` finite-algebra package is repaired so its `Hermitian` `Weyl` `Gram` check executes cleanly and its `1 x 1` scalar heavy block is upgraded to a genuine `3 x 3` non-commuting, non-symmetric heavy block `D(t) = D_0 + t D_1`, do all `2`nd- and `3`rd-order `Schur` complement mass identities and `Spin(10)` `2D` `U(1)_Y (+) U(1)_(B-L)` anomaly-vanishing laws hold while catching transposed-inverse and operator-order faults?
3. Does the target-free `1`-loop zeta/Bessel spectral `Casimir` potential `V_Cas(L_4)` of `3`-family `E_6 -> SU(4)_c x SU(2)_L x SU(2)_R x| Z_2^D` on `X_4 = m004 x~ [-L_4, L_4]` stabilize `Delta_PS = ln(M_U / M_PS)` without embedded scales, or obey an exact sign-dichotomy obstruction?

## 2. Deliverables and Definition of Done

1. **Canonical `BPV` + `Machacek-Vaughn` `2`-Loop Matrix `RGE` Lock (`Guardrails 3 & 4`):**
   - Verify symbolic and numerical (`DOP853` vs `45`-digit `mpmath`) production-`RHS` agreement with `Buttazzo et al.` (`2013`, Appendix A) on `t_crit` (`cross-solver diff < (1/10)^11`), catching the factor-of-`2` `-24 lambda^2 Tr_Y` error (`shift > 1/1000` on `sqrt(2 lambda_IR)`).
   - Prove symbolically and verify by direct `2`-loop matrix `ODE` integration that rank-`1` `2`-generation `CKM` mixing obeys `(16 pi^2) d ln(tan theta) / d ln(mu) = (3/2)(y_t^2 + y_b^2)` at `1`-loop and `(16 pi^2)^2 d ln(tan theta) / d ln(mu) = -(13/2)(y_t^4 + y_b^4) - (11/2) y_t^2 y_b^2` at pure-Yukawa `2`-loop for **all** `theta in (0, pi/2)` (`rel_err < (1/10)^12`, rejecting un-transposed `-7` by `> 1/10`).
   - Verify `3`-family `D`-parity `|bar_theta_QCD(IR)| < (1/10)^13` with `|J_CKM| > 1/100` and `10`-trial `U(3)^6` `Haar` basis-scrambling invariance `< (1/10)^13`.
2. **Repaired Non-Commuting `P-C3` `Schur` Vertex & Symbolic `Spin(10)` Anomaly Plane:**
   - Verify exact `SymPy` equality of holomorphic `GL_3(C)` `Weyl` `Gram` & current transport (`fixing the unexpanded conjugate-product crash`), odd Weierstrass profile + `Spin(2)` half-turn derivation of `(k_eps, j_eps) = (-1, -1)`, and `72` wrong-side `Q_8 x Q_8` deck rejections.
   - On a `6 x 6` block matrix (`3` light + `3` heavy with `||[D_0, D_1]||_F^2 > 0` and `||D_0 - D_0^T||_F^2 > 0`), verify exact `t^5` determinant factorization of `M_eff(t) = t V_1 + t^2 (V_2 - B D_0^{-1} C) + t^3 B D_0^{-1} D_1 D_0^{-1} C`, numerical `sigma_min(M_full(t)) / t^2` convergence (`rel_err < (1/10)^5` at `t = (1/10)^5`), quaternion span collapse (`9 -> 5` or `4` under `M = eps S`), `4`-slot stabilizer nullity jump (`1 -> 2` at `h_a = 0`), and symbolic `Q[a, b]` proof that `Lambda^{even}(V_5) x (det V_5)^{-1/2} ~= 16` vanishes on all `4` `4D` anomaly polynomials `[0, 0, 0, 0]` across the entire `2D` `U(1)_Y (+) U(1)_(B-L)` plane (`vs untwisted 4(3a + 2b)(9a^2 + 6ab + 5b^2)`).
3. **Target-Free `4D` `m004` Collar Spectral `Casimir` Sign-Dichotomy Theorem (`Guardrail 1`):**
   - Compute exact `UV` (`L_4 << ell_3`) and `IR` (`L_4 >> ell_3`) `Casimir` supertrace coefficients `C = 2[(-n_B^+ + (7/8) n_B^-) + (+n_F^+ - (7/8) n_F^-)]` for `3`-family `E_6 -> G_422 x| Z_2^D` (`gauge 21 (+) 57 -> +231/4`, `3 x 27_F` split `(48, 33) -> +153/4`, `27_H` split `(13, 14) -> -3/2`, total `C_UV = +189/2 > 0`).
   - Prove and verify to `45` digits in `mpmath` that: (a) when `3` chiral `Pati-Salam` `16_F` zero-mode families remain `3D`-massless alongside untwisted `G_422` + Higgs zero modes, `C_IR = +28 > 0` matches `sgn(C_UV) > 0`, so `d V_Cas / d L_4 < 0` strictly on `(0, infty)` (**exact `1`-loop runaway obstruction**, pricing `Delta_PS` as `1` continuous geometric modulus); whereas (b) a unique target-free `1`-loop minimum `d V_Cas / d L_4 = 0, d^2 V_Cas / d L_4^2 > 0` exists **if and only if** `C_UV > 0 > C_IR` (realized conditionally when hyperbolic `Weitzenbock`/cusp spinor gaps lift `3D` fermion modes above neutral bosonic `b_0(m004) = 1` zero modes).

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Any discrepancy `>= (1/10)^11` on `Buttazzo` `t_crit`, `>= (1/10)^12` on `BBO` `-11/2` `2`-loop `CKM` slope, or `>= (1/10)^13` on `Strong-CP` or `U(3)^6` `Haar` invariance.
- Any `SymPy` polynomial residual `!= 0` on `6 x 6` `Schur` `t^5` determinant factorization or `Spin(10)` `[0, 0, 0, 0]` `2D` anomaly cancellation.
- Claiming unconditional `0`-parameter `Delta_PS` stabilization despite `C_IR = +28 > 0` in the `3`-family massless-chiral branch (`Guardrail 1`).
- Any float/complex literal in source (`AST` lock) or failure to catch any of the `5` planted fault controls below.

## 4. Five Planted Fault Controls That Must Fail When Broken

1. **`PF4.1` (`Un-Transposed 2-Loop Mixed-Yukawa Ordering`):** Swapping `-(1/4) H_u H_d - H_d H_u` to `-H_u H_d - (1/4) H_d H_u` must shift the `2`-loop `y_t^2 y_b^2` `CKM` slope from `-11/2` to `-7` (`abs diff = 3/2 > 1`).
2. **`PF4.2` (`Factor-of-2 Missing Jacobian on lambda^2 Tr_Y`):** Replacing `-48 lambda^2 Tr_Y` by `-24 lambda^2 Tr_Y` in `d lambda / d ln(mu)` must break `Buttazzo` `d lambda / d ln(mu)` matching (`abs diff > 1/100`) and shift `UV-to-IR` `sqrt(2 lambda_IR)` by `> 1/1000`.
3. **`PF4.3` (`Transposed Heavy Inverse D_0^{-T} in 3 x 3 Non-Commuting Schur Complement`):** Replacing `D_0^{-1}` by `D_0^{-T}` must fail `Y_2` (`Frobenius diff^2 = 1245/1922 > 1/2`, catching what a `1 x 1` scalar heavy block misses).
4. **`PF4.4` (`Reversed Heavy Operator Order D_1 D_0^{-2} in 3rd-Order Schur Term`):** Replacing `D_0^{-1} D_1 D_0^{-1}` by `D_1 D_0^{-2}` must fail `Y_3` (`Frobenius diff^2 = 698707/1847042 > 1/4`).
5. **`PF4.5` (`Hand-Embedded Target Collar Minimum L_4^*` — `Guardrail 1`):** Injecting an artificial `(L_4 - L_target)^2` term or flipping `C_IR = +28` by literal assignment must be rejected by the derivative-monotone check on the `3`-family massless-chiral `Casimir` branch (`max d V_Cas / d L_4 < 0` violated).

## 5. Dependencies and Firewall Boundaries

Rests on `Machacek-Vaughn (1983-1985)`, `Barger-Berger-Ohmann (1993)`, `Buttazzo et al. (2013)`, `Bednyakov-Pikelner-Velizhanin (2014)`, and `Ponton-Poppitz (2001)`. Strict `0 of 19` firewall; touches only files under `relays/`. Expectations committed first (`0 of 19`).
