# Card `AGY-002_ENDGAME-V2-G1` — `E_6 -> Pati-Salam x| Z_2^D` Universal Gauge Corridor & `3`-Family Strong-`CP` Law (`0 of 19`)

## 1. Package and Question

Replacing minimal `SU(5)` (`whose desert crossing misses at 16 sigma, B1948 Row 4`) and `6`-family mirror doubling (`where b_3^{SM} = -3`) with `3`-family `E_6 -> SU(4)_c x SU(2)_L x SU(2)_R x| Z_2^D` on the orientable twisted interval four-manifold `X_4 = m000 x~ [-1, 1]` bounded by `partial X_4 = m004`:
1. Does Left–Right `D`-parity combined with amphicheirality (`Re(tau_cusp) = 0`, `CS(m004) = 0`) enforce exact `3`-family Strong-`CP` vanishing (`bar_theta_QCD = 0`) across tree-level, `1`-loop, and `2`-loop non-commuting `SM RGE` running while preserving `N_g = 3` chiral generations and non-zero CKM `CP` violation (`J_CKM != 0`)?
2. What is the exact `0`-selection-bit `1`-loop and `2`-loop `Pati-Salam x| Z_2^D` universal gauge relation (`P-862`) across intermediate threshold ratios `Delta_PS = ln(M_U / M_PS) >= 0`, and does rigid `3D` cusp/collar geometry on `m004` fix `(alpha_U^{-1}, Delta_PS)` without `4D` bulk parameters?

## 2. Deliverables and Definition of Done

1. **Exact Cyclotomic `Z[zeta_6]` Cusp & `E_6` Weight Proof (`0 of 19`):**
   - From Riley parabolic generators `A = [[1, 1], [0, 1]]`, `B = [[1, 0], [zeta_6, 1]]` (`zeta_6^2 - zeta_6 + 1 = 0`), prove in exact `Z[zeta_6]` ring arithmetic that `[A, B^{-1}] A = B [A, B^{-1}]` holds identically, that the `0`-linking peripheral longitude word `L = B^{-1} A B A^{-2} B A B^{-1}` evaluates to `- [[1, 2 sqrt(3) i], [0, 1]]`, and therefore `Re(tau_cusp) = 0` (`tau_cusp = 2 sqrt(3) i`), isometric tangency height `t_tan = 1 / |zeta_6| = 1`, Adams maximal horotorus area `A_max(m004) = 2 sqrt(3)`, maximal cusp volume `V_cusp,max(m004) = sqrt(3)`, and `50`-digit Bloch–Wigner volume `Vol(m004) = 2 Cl_2(pi/3) = 2 Vol(m000)`.
   - Verify on the `27` weight system of `E_6 -> SU(4)_c x SU(2)_L x SU(2)_R x U(1)_psi` that `27 = (4,2,1)_{+1} + (4bar,1,2)_{+1} + (1,2,2)_{-2} + (6,1,1)_{-2} + (1,1,1)_{+4}`, so chiral APS / Dai–Freed boundary conditions on `partial X_4 = m004` yield `N_g = 3` chiral SM families (`b_SM = (41/10, -19/6, -7)`) once vector-like `(6,1,1) + (1,2,2) + (1,1,1)` decouple.
2. **Exact `3`-Family Strong-`CP` Vanishing Theorem (`Tree + 1-Loop + 2-Loop SM RGE`, `B1948` Row `19`):**
   - Construct generic complex `D`-symmetric Hermitian Yukawa matrices `Y_u(M_PS) = Y_u(M_PS)^dag`, `Y_d(M_PS) = Y_d(M_PS)^dag` (`with sgn det Y_u = sgn det Y_d` — `1` discrete sign parity, `0` continuous parameters — and non-commuting `[Y_u, Y_d] != 0` producing `|J_CKM| > 1e-5`).
   - Prove algebraically (`via trace reality Tr(H_u^a H_d^b) in R` for all `1`-loop and `2`-loop matrix beta polynomials) and verify numerically to `< 1e-13` across full `2`-loop `SM RGE` evolution and `8` random Haar `U(3)^6` basis transformations (`with Fujikawa anomaly shift`) that `|bar_theta_QCD(mu_IR)| < 1e-13` while `|J_CKM(mu_IR)| > 1e-5`.
3. **Exact `1`-Loop & `2`-Loop `Pati-Salam x| Z_2^D` Universal Gauge Corridor (`P-862` / `B1948` Row `4`):**
   - Derive from unified `Machacek-Vaughn (1983)` Casimir/Dynkin equations both `b_PS = (-10, -7/3, -7/3)` (`delta_b_PS = b_2^{PS} - b_4^{PS} = 23/3`) and the `2`-loop matrix `B_PS = [[-117/2, 15/2, 15/2], [75/2, 50/3, 3], [75/2, 3, 50/3]]` (`verifying gauge reciprocity 15 B_{4,2L} = 3 B_{2L,4} = 225/2`).
   - Prove the exact `1`-loop closed-form `Pati-Salam` corridor identity eliminating `(alpha_U^{-1}, ln(M_PS / mu_IR))`:
     `sin^2 theta_W(mu_IR) = 23/134 + (109/201) (alpha_EM(mu_IR) / alpha_3(mu_IR)) + (22 delta_b_PS / (67 pi)) alpha_EM(mu_IR) Delta_PS`,
     with exact positive slope `22 delta_b_PS / (67 pi) = 506 / (201 pi) > 0` (`verified against 1-loop ODE integration to < 1e-14`), and compute the blind `2`-loop gauge-Yukawa corridor table across canonical `0 of 19` geometric collar invariants `Delta_PS in {0, Vol(m000), ln(2 sqrt(3)), sqrt(3), Vol(m004), 2 sqrt(3), 2 Vol(m004), 4 Vol(m004)}`.
4. **Honest `4D` Collar Scale-Fixing Obstruction Theorem (`Guardrail 1`):**
   - Prove by explicit scaling transformation `s -> lambda_4 s` of the `4D` Yang–Mills action on `X_4 = m000 x~ [-L_4, L_4]` that `3D` Mostow rigidity of `m004` fixes `tau_cusp`, `A_max`, and `Vol(m004)` uniquely, whereas `(alpha_U^{-1}, Delta_PS)` depend on the transverse `4D` interval length `L_4` and radial collar warp profile, so neither `alpha_U^{-1}` nor `Delta_PS` can be claimed `0`-parameter fixed without a `4D` bulk stabilization potential.

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Any failure of `[A, B^{-1}] A = B [A, B^{-1}]`, `Re(tau_cusp) = 0`, `A_max = 2 sqrt(3)`, or `E_6` `27` branching / reciprocity `15 B_{4,2L} = 3 B_{2L,4}`.
- Any `2`-loop `SM RGE` drift `|bar_theta_QCD(mu_IR)| >= 1e-13` or loss of CKM `CP` violation `|J_CKM(mu_IR)| <= 1e-5` on `D`-symmetric Hermitian `3`-family states, or Haar `U(3)^6` drift `>= 1e-12`.
- Any discrepancy `>= 1e-14` between the closed-form `1`-loop `Pati-Salam` corridor identity and `ODE` integration, or negative `Delta_PS` corridor slope.
- Failure to catch any of the `5` planted fault controls below.

## 4. Five Planted Fault Controls That Must Fail When Broken

1. **`PF1.1` (`D-Parity-Breaking Non-Hermitian Perturbation`):** Adding a non-Hermitian `delta Y_d != delta Y_d^dag` at `M_PS` must generate `|bar_theta_QCD(mu_IR)| > 0.05`.
2. **`PF1.2` (`Opposite Determinant Sign Parity`):** Flipping `sgn det(Y_u Y_d)` from `+1` to `-1` while keeping `Y_u, Y_d` Hermitian must shift `|bar_theta_QCD|` to `pi > 3.0`.
3. **`PF1.3` (`6-Family Mirror Doubling Regression`):** Replacing `N_g = 3` by `N_g = 6` must shift `b_3^{SM}` from `-7` to `-3` (`|Delta b_3| = 4 > 1`).
4. **`PF1.4` (`Flipped Threshold Running Sign`):** Reversing `+(b_i^{PS} / 2 pi) Delta_PS` to `-(b_i^{PS} / 2 pi) Delta_PS` must violate `ODE` matching by `> 0.01` and invert the `sin^2 theta_W` slope sign.
5. **`PF1.5` (`Over-Inflated Horoball Height t = 1/2 < t_tan = 1`):** Evaluating horoball spheres at `t = 1/2` must produce strict Euclidean overlap (`sphere diameter 2 > lattice distance 1`).

## 5. Dependencies and Firewall Boundaries

Rests on locked Gate 0 `2`-loop `RGE` solver (`AGY-002_ENDGAME-V2-G0`), `Adams (1987)`, `Machacek-Vaughn (1983-85)`, and `Ellis-Gaillard (1979)`. Strict `0 of 19` firewall; touches only files under `relays`. Expectations committed first (`0 of 19`).
