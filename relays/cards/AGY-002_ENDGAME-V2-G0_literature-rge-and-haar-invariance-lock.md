# Card `AGY-002_ENDGAME-V2-G0` — Literature `RGE` Benchmark and `U(3)^6` Invariance Lock (`0 of 19`)

## 1. Package and Question

Before any geometric UV boundary datum from `m004` or `X_4` is evaluated, does a standalone zero-import `2`-loop matrix renormalization-group and threshold solver for `SM + Left-Right D-symmetric Pati-Salam / E_6 + Weinberg seesaw` pass exact Lie-algebra trace coefficient derivation, `4` published analytical and multi-solver `RGE` trajectory benchmarks to `>= 3` significant figures (tightened to `< 1e-7` relative tolerance), and full pre-`RGE` random Haar `U(3)^6` basis-scrambling invariance to `< 1e-12` under strict `0 of 19` isolation?

## 2. Deliverables and Definition of Done

1. **AST & Empirical Firewall Lock (`0 of 19`):** Standalone Python verifier importing only standard library, `numpy`, and `mpmath`, containing zero repository imports and zero measured Standard Model empirical constants.
2. **Exact Group-Theoretic Beta-Coefficient Derivation:** Direct computation from explicit `SU(3)_c x SU(2)_L x U(1)_Y` and `SU(4)_c x SU(2)_L x SU(2)_R` representation generators and Casimir invariants of the `1`-loop gauge slopes `b_SM = (41/10, -19/6, -7)` (`N_g = 3, N_H = 1`), the `D`-symmetric Pati-Salam slopes, and the exact hypercharge embedding identity `Y = T_{3R} + (B - L)/2` giving `alpha_1^{-1}(M_PS) = (3/5) alpha_2^{-1}(M_PS) + (2/5) alpha_3^{-1}(M_PS)` under `g_{2L}(M_PS) = g_{2R}(M_PS)` and `g_4(M_PS) = g_3(M_PS)`, verified against published rational tables (`Machacek-Vaughn 1983-85`, `Jones 1982`, `Buttazzo et al. 2013 Appendix A`) with zero discrepancy.
3. **Four Published `RGE` Solver Benchmarks (`0 of 19` Synthetic Rational States, Required `< 1e-3`, Tightened `< 1e-7`):**
   - **`B0.1` (`2`-Loop Single-Gauge Implicit Exact Integral):** Compare `50`-digit `mpmath` root solution of `int dg / (kappa_1 b g^3 + kappa_2 B g^5) = Delta t` over `Delta t = -30` against numerical `ODE` integration (`rel_err < 1e-9`).
   - **`B0.2` (`Buttazzo et al. 2013 Eq. (A.5)` `2`-Loop Scalar Quartic Zero-Crossing):** Integrate from synthetic rational boundary couplings `(g_1, g_2, g_3, y_t, lambda) = (1/2, 3/5, 1, 9/10, 1/10)` until `lambda(t_crit) = 0`, comparing `45`-digit `mpmath` adaptive step-doubling integration against `float64` `RK4` (`|Delta t_crit| / |t_crit| < 1e-7`).
   - **`B0.3` (`Machacek-Vaughn 1984` `2`-Loop Non-Commuting Complex Matrix Yukawa Flow & `Xing-Zhou 2018` Downward Determinant Identity):** Compare `float64` `2`-loop matrix `ODE` against `40`-digit `mpmath` matrix `ODE` across `Delta t = -27` on generic non-commuting complex `3 x 3` rational-seeded `(Y_u, Y_d, Y_e)` (`max rel_err < 1e-8`), and verify the exact `1`-loop `Jacobi` determinant integral `d/dt ln det(Y_f Y_f^dag) = 2 Re Tr((dY_f/dt)_{1-loop} Y_f^{-1})` (`abs_err < 1e-10`).
   - **`B0.4` (`Antusch et al. 2003` `1`-Loop Weinberg Seesaw Operator Flow):** Verify `ODE` integration of `kappa(t) = Y_nu M_R^{-1} Y_nu^T` in the left-doublet-row convention against the exact exponential/path-ordered matrix integral (`rel_err < 1e-9`).
4. **Mandatory Pre-`RGE` Random Haar `U(3)^6` Scrambling Gate (`Guardrail 3`):** Apply `8` independent Haar-random unitary tuples `(U_Q, U_u, U_d, U_L, U_e, U_N) in U(3)^6` (`with M_R -> U_N^* M_R U_N^dag`) to the UV state prior to full two-step `Pati-Salam -> seesaw -> 2-loop SM` integration, and verify invariance to `< 1e-12` of all `21` physical dimensionless observables (`9` Dirac singular values, `3` Weinberg neutrino singular values, `4` CKM invariants `|V_{us}|, |V_{cb}|, |V_{ub}|, J_CKM`, `4` PMNS invariants `|U_{e2}|, |U_{e3}|, |U_{mu3}|, J_PMNS`, and `bar_theta_QCD = arg det(Y_u Y_d)`).

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Any non-zero discrepancy in Lie-algebra trace derivations of `b_SM`, `b_PS`, or the `(3/5, 2/5)` Pati-Salam hypercharge matching weights.
- Any solver discrepancy `>= 1e-3` (literature `3`-significant-figure threshold) or `>= 1e-7` (tightened numerical lock) on `B0.1`–`B0.4`.
- Any post-`RGE` observable drift `>= 1e-12` across the `8` random Haar `U(3)^6` basis transformations.
- Failure to catch any of the `5` planted fault controls below.

## 4. Foundations and Firewall Boundaries

- **Rests on:** Published `2`-loop `MSbar` `RGE` polynomials (`Machacek-Vaughn, Nucl. Phys. B222 (1983) 83; B236 (1984) 221; B249 (1985) 70`; `Antusch et al., Nucl. Phys. B674 (2003) 401`; `Buttazzo et al., JHEP 12 (2013) 089`; `Xing-Zhou, JHEP 05 (2018) 005`).
- **Must not touch:** Any of the `19` measured Standard Model parameters (`0 of 19`), any governing file outside the `relays` folder, or any producer import during independent recomputation.

## 5. Five Planted Fault Controls That Must Fail When Broken

1. **`PF0.1` (`d/d ln mu^2` vs `d/d ln mu` Scale Factor Error):** Dividing `beta` by `2` (`or 4*pi`) must break `B0.1` and `B0.2` by `> 0.25`.
2. **`PF0.2` (`Right-Multiplied Yukawa Beta`):** Replacing left-acting `H_u Y_u` with `Y_u H_u` in `beta_{Y_u}` must break `U(3)^6` Haar invariance of post-`RGE` `|V_CKM|` by `> 1e-3`.
3. **`PF0.3` (`Single-Matrix Left-Right Overlap`):** Extracting mixing from `|U_{L,u}^dag V_{R,u}|` must fail `U(3)_Q x U(3)_u` Haar scrambling by `> 0.1`.
4. **`PF0.4` (`Transposed Weinberg Contraction Mismatch`):** Using `Y_nu^T M_R^{-1} Y_nu` instead of `Y_nu M_R^{-1} Y_nu^T` under left-row doublet transformation `Y_nu -> U_L Y_nu U_N^dag` must break `U(3)_L x U(3)_N` Haar invariance of `|U_PMNS|` by `> 0.1`.
5. **`PF0.5` (`Corrupted Pati-Salam Hypercharge Weights`):** Replacing `(3/5, 2/5)` by `(1/2, 1/2)` in `alpha_1^{-1}(M_PS)` must violate `SU(4)_c x SU(2)_R` generator normalization `Tr(Y^2)` by `> 0.05`.

## 6. Dependencies

None from `main` or other seats. Expectations committed first (`0 of 19`).
