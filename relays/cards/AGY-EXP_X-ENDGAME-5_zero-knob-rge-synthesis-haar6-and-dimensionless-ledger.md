# Card `X-ENDGAME-5` — Four-Pillar Literature `RGE` Solver Gate, Zero-Knob Ultraviolet-to-Infrared Matrix Evolution Across Classical and Casimir Horotorus Areas, Six-Unitary $\mathrm{U}(3)^6$ Haar Basis Invariance, Orbit and Monotonicity Audit, and Complete Dimensionless Prediction Ledger (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Fifth and final sealed stage of Campaign `X-ENDGAME` (`five stages, twenty blind-sealed commits, 0 of 19`). Integrates the zero-knob ultraviolet boundary conditions derived across Stages `1` through `4` (`cusp modulus, hyperbolic volume, classical vs Casimir horotorus area, gauge trace unification, collar localization, magnetized overlaps, and modular-covariant puncture-jet seesaw operator`) to the infrared under `AST`-benchmarked `2`-loop matrix + `1`-loop dimension-`5` symmetric Majorana `RGE`s, verifies post-`RGE` `6`-unitary $\mathrm{U}(3)^6$ Haar basis invariance, audits order-`5` and order-`15` orbit structure and monotonicity, and seals the complete dimensionless infrared prediction vector alongside an explicit bit-counted selection ledger.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_endgame_5_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; published `RGE` solver benchmark constants are strictly `AST`-isolated inside the solver-verification function and never enter any model calculation.

---

## 1. The Package and the Questions

1. **Question `5A` (`Four-Pillar AST-Isolated Literature RGE Solver Gate, Including Noncommuting Two-Loop Matrix Check`):** Before touching any geometric ultraviolet boundary condition, does our standalone `RGE` integrator independently reproduce (i) `3`-loop high-scale gauge/quartic/fermion trajectories and scalar-quartic zero crossing, (ii) the published **noncommuting** `2`-loop $3 \times 3$ matrix mixing derivative $d\ln|V_{23}|/d\ln\mu$ (`where [H_1, H_2] != 0`, directly testing the relative ordering of $H_1 H_2 Y_1$ vs $H_2 H_1 Y_1$ that diagonal benchmarks and Haar basis checks cannot see), (iii) infrared-directed `1`-loop matrix evolution and its exact determinant invariant identity, and (iv) the exact analytical integral of the `1`-loop dimension-`5` symmetric Majorana operator evolution?
2. **Question `5B` (`Zero-Knob Ultraviolet-to-Infrared Evolution, Classical-vs-Casimir Robustness, Post-RGE U(3)^6 Haar Gate & Orbit/Monotonicity Audit`):** Starting solely from rational Newton seeds (`AST`-verified zero target literals) for `m004`'s joint `3D + 2D` stabilization, canonical `1D` collar $\times$ `2D` horotorus wavefunctions at $w = (4/15, 8/15)$, unified gauge coupling $\alpha_{\mathrm{UV}}^{-1} = \operatorname{Vol}(m004) A^*$, gauge-scalar $D$-term boundary quartic $\lambda_{\mathrm{UV}} = (1/5) g_{\mathrm{UV}}^2$, and cover-instanton log interval $\Delta\ln\mu = -(45/\pi)\operatorname{Vol}(m004)$:
   - Does the coupled `2`-loop matrix + `1`-loop symmetric Majorana flow remain smooth, perturbative, and quartic-positive (`\lambda > 0`) all the way to the infrared?
   - How much does the entire dimensionless infrared observable vector shift if the flat Epstein Casimir term is dropped completely in favor of pure classical flux + hyperbolic volume stabilization $A_{\mathrm{tree}}^* = 6\pi$?
   - Are all dimensionless infrared observables invariant to `< (1/1000)^4` under `10` independent random `6`-unitary $\mathrm{U}(3)^6$ chiral basis scramblings applied **prior** to `RGE` integration?
   - What are the exact orbit counts on $\mathcal{O}_{32}$ under $\langle M \rangle$, $\langle J \rangle$, $\langle M, -I_2 \rangle$, $\langle J, -I_2 \rangle$, and $\langle -I_2 \rangle$, and does strict diagonal monotonicity $h_1 < h_2 < h_3$ of $U_2^\dagger H_1 U_2$ hold across all `4` points of $\mathcal{O}_4$ and all `4` points of the $\tau^*$-stabilizer quartet of $(4/15, 8/15)$?
3. **Question `5C` (`Complete Dimensionless Infrared Prediction Vector & Honest Bit-Counted Input Ledger`):** What complete vector of dimensionless infrared couplings, intra- and inter-sector singular-value ratios, $|V_{12}^{\mathrm{IR}}|$ and $|U_{34}^{\mathrm{IR}}|$ mixing moduli, $CP$-odd invariants, and single-slice vs amphichiral-doubled determinant phases emerges with **zero** continuous fitted parameters, and what is the exact discrete bit cost of every structural premise and vacuum/scheme choice?

---

## 2. Deliverables and Definition of Done

1. **`Part 5A` — Four-Pillar `AST`-Isolated Published `RGE` Solver Gate:**
   - **Pillar `1` (`3`-Loop High-Scale Benchmark):** Verify `1`-loop closed-form gauge evolution to `< (1/1000)^4` and `3`-loop extrapolation matching published high-scale couplings (`relative error < 2/1000`, quartic absolute error `< 1/2000`, scalar-quartic zero-crossing log scale within `1/20`).
   - **Pillar `2` (`Noncommuting 2-Loop Matrix Mixing Benchmark`):** Evaluate `sm_2loop_plus_majorana_rhs` on a noncommuting $[H_1, H_2] \neq 0$ state and verify that its pure `2`-loop contribution to $d\ln|V_{23}|/d\ln\mu$ matches the exact analytical `2`-loop formula (`coefficients 13/2, 7, 5/4, -16, 9/16, -79/80, -43/80`) to relative error `< 1/100000`.
   - **Pillar `3` (`Infrared-Directed 1-Loop Matrix Determinant Invariant`):** Integrate toward the infrared and verify the exact commutator-determinant scaling identity to relative error `< (1/1000)^4`.
   - **Pillar `4` (`1-Loop Dimension-5 Symmetric Majorana Analytical Integral`):** Verify numerical `RK4` integration of $\mathcal{W}_4$ against its exact analytical integral to relative error `< (1/1000)^4` while preserving $\mathcal{W}_4 = \mathcal{W}_4^T$ to `< (1/1000)^5`.
2. **`Part 5B` — Zero-Knob Ultraviolet-to-Infrared Synthesis, $\mathrm{U}(3)^6$ Haar Gate, Classical-vs-Casimir Check, and Orbit/Monotonicity Audit:**
   - Solve `m004` joint `3D + 2D` stabilization from rational seeds (`zero` target literals), build zero-knob ultraviolet matrices $(Y_1, Y_2, Y_3, Y_4, M_R, \mathcal{W}_4)$ and couplings $(g_1, g_2, g_3, \lambda)$ for both $A_{\mathrm{Cas}}^*$ and $A_{\mathrm{tree}}^* = 6\pi$, and integrate across $\Delta\ln\mu = -(45/\pi)\operatorname{Vol}(m004)$.
   - Run `10` independent `24`-digit `mpmath` random $\mathrm{U}(3)^6$ basis-scrambling trials prior to `RGE` evolution and verify post-`RGE` invariance of all singular-value ratios, $|V_{12}^{\mathrm{IR}}|$, $|U_{34}^{\mathrm{IR}}|$, $\hat{I}_{CP}^{\mathrm{IR}}$, and $\lambda_{\mathrm{IR}}$ to `< (1/1000)^4`.
   - Measure the maximum relative shift across all `15` scalar infrared observables between $A_{\mathrm{tree}}^* = 6\pi$ and $A_{\mathrm{Cas}}^*$, enumerate exact orbit decompositions of $\mathcal{O}_{32}$, and test $h_1 < h_2 < h_3$ across all `4` points of $\mathcal{O}_4$ and all `4` points of the $\tau^*$-stabilizer quartet of $(4/15, 8/15)$.
3. **`Part 5C` — Complete Dimensionless Infrared Vector & Honest Bit-Counted Ledger:**
   - Emit all dimensionless infrared observables (`gauge couplings, electroweak mixing ratio, scalar-to-condensate ratio, all intra- and inter-sector singular-value ratios across sec1..sec4, all 9 moduli of |V_{12}| and |U_{34}|, parity-block mixing, CP invariants, and UV/IR single-slice vs parity-doubled determinant phases`) alongside an explicit `0`-continuous-parameter, `8`-discrete-bit selection ledger.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_FourPillar_Literature_RGE_Gate` (`Part 5A`):** All four published `RGE` solver benchmarks pass simultaneously within their pre-registered tolerances (`including < 1/100000 relative error on the pure 2-loop noncommuting matrix mixing derivative`).
2. **`E2_ZeroKnob_UV_to_IR_and_Haar6_Gate` (`Part 5B`):** Perturbative smoothness holds throughout (`\max g_i < 2`, `\max \sigma_3(Y_f) < 2`, `\min \lambda > 0`), `10`-trial `24`-digit $\mathrm{U}(3)^6$ post-`RGE` Haar invariance holds to `< (1/1000)^4`, replacing $A_{\mathrm{Cas}}^*$ by classical $A_{\mathrm{tree}}^* = 6\pi$ shifts all `15` scalar infrared observables by `< 1/1000`, $\mathcal{O}_{32}$ decomposes into `(8, 4, 4, 2, 16)` orbits under $(\langle M\rangle, \langle J\rangle, \langle M,-I_2\rangle, \langle J,-I_2\rangle, \langle -I_2\rangle)$, and $h_1 < h_2 < h_3$ holds on all `4` points of $\mathcal{O}_4$ and all `4` points of $(4/15, 8/15)$'s $\tau^*$-stabilizer quartet.
3. **`E3_Complete_Dimensionless_IR_Ledger_Gate` (`Part 5C`):** In the infrared, $|V_{12}^{\mathrm{IR}}|$ remains diagonally aligned (`max off-diagonal < 3/100`), $|U_{34}^{\mathrm{IR}}|$ retains near-maximal parity-block mixing ($\sin^2(2\theta) > 99/100$), single-slice $\arg\det(Y_1^{\mathrm{IR}} Y_2^{\mathrm{IR}})$ is `O(1)` non-zero while its amphichiral-doubled partner vanishes to `< (1/1000)^4`, continuous fitted parameters equal `0`, and total explicitly priced discrete selection/scheme bits equal `8`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage5_Passed`:** `AST` audit confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside any target-free geometry or model-UV builder function.
2. **`PC_ENDGAME5_WrongDiffFactor`:** Omitting the factor of `2` between $d/d\ln\mu$ and $d/d\ln\mu^2$ breaks the `1`-loop closed-form gauge check by `> 1/10`.
3. **`PC_ENDGAME5_CommutatorPerturbation`:** Injecting $\delta\beta_{Y_1} = (3/4)[H_1, H_2]Y_1$ leaves the diagonal `2`-loop scalar check identically `0`, yet shifts the noncommuting `2`-loop mixing derivative by exact $(3/4) K_2 \cos^2\theta\, y_1^2 y_2^2$ (`breaking the noncommuting 2-loop benchmark by > 5/1000`).
4. **`PC_ENDGAME5_WrongRunningDirection`:** Reversing integration sign (`+1` instead of `-1`) breaks the `1`-loop commutator-determinant scaling identity by `> 9/10`.
5. **`PC_ENDGAME5_WrongMajoranaTranspose`:** Replacing $H_3 \mathcal{W}_4 + \mathcal{W}_4 H_3^T$ by $H_3 \mathcal{W}_4 + \mathcal{W}_4 H_3$ on complex $Y_3$ breaks symmetric $\mathcal{W}_4 = \mathcal{W}_4^T$ invariance (`relative asymmetry > 1/10`).
6. **`PC_ENDGAME5_WrongChiralityRGE`:** Right-multiplying `1`-loop matrix Yukawa $\beta$-functions breaks right-handed $\mathrm{U}(3)_R$ Haar basis invariance (`error > 1/1000`).

`0 of 19.`
