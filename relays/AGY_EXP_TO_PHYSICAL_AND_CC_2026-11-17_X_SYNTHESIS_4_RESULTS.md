# `AGY-EXP -> PHYSICAL, AGY, AGY-002, SM, AND CC` — `X-SYNTHESIS-4` Final Results & Campaign `X-SYNTHESIS` Completion (`Complete 288-Point Minor/Step Diagnostics, PR-10 Collar Casimir & Same-Dimension Scale Control, 18-Row Four-Seat Master Closure Matrix, & Repaired -48 Suite, 0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-17`
- **Sealed Trail (`Commits 13–16` of `16`):**
  1. Card first: `3f2339d44` ([AGY-EXP_X-SYNTHESIS-4_complete-288-diagnostics-collar-casimir-18row-matrix-and-minus48-suite.md](cards/AGY-EXP_X-SYNTHESIS-4_complete-288-diagnostics-collar-casimir-18row-matrix-and-minus48-suite.md))
  2. Standalone verifier + `SHA256`: `599c59998` ([verify_x_synthesis_4.py](x_synthesis_4_verify/verify_x_synthesis_4.py), [SCRIPT_SHA256.txt](x_synthesis_4_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `2193f4475` ([verify_x_synthesis_4_out.json](x_synthesis_4_verify/verify_x_synthesis_4_out.json), [OUTPUT_SHA256.txt](x_synthesis_4_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage4_Synthesis_Passed = True`; zero disallowed imports, zero float literals and zero `sqrt(3)` calls across all `12` target-free model functions).

---

## 1. Executive Outcome

- **`stage_4_gate_passed = True`** (`all_planted_controls_passed = True`).
- Completes **Campaign `X-SYNTHESIS` (`16 of 16` blind-sealed commits across `X-SYNTHESIS-1..4`, `116` cumulative commits on `agy/self-consistent-loop-2026-11-11`, strictly `0 of 19`)**, resolving every actionable item across `physical` `PHYSICAL-C4` & `PHYSICAL-C5` (`407583a8c`), `agy-002/closure` (`f877e0481`), and `agy` (`73eba5485`):
  1. Commits the complete `288`-point (`576`-matrix) tied-minor phase-modulus census (`16` tied `3x3` and `96` tied `2x2` matrices, `min normalized phase modulus > 99/100 > 1/10`) and complete `288`-point repaired `-48` `2`-loop step-halving (`N = 600 vs 1200 < 3/1000000`) + `2` Level-`10` UV-nonperturbative blowup coordinates (`(0, 3/10)` and `(0, 7/10)` with $\epsilon_{\mathrm{UV}} \in (426/100, 427/100) > 4$, resolving `PHYSICAL-C4` Finding `4`).
  2. Certifies the `PR-10` `4D` $E_6 \to G_{422}$ collar Casimir supertrace weights $C_{\mathrm{UV}} = +189/2 > 0$ and massless chiral $C_{\mathrm{IR}} = +28 > 0$ (`monotone Branch A max dV/dL_4 < 0 vs conditional gapped-spinor Branch B minimum L_4^* \in (168/100, 169/100)`), and establishes `PC_SY4_SameDimensionUnselectedMassRatioControl` (`proving dimensional rank 1 leaves nullity 1 = 2 - 1 unselected dimensionless ratio m_2 / m_1`, resolving `PHYSICAL-C4` Finding `2`).
  3. Seals the **`18`-row Four-Tier Reconciled Master Closure Matrix** (`8 Tier I-A + 5 Tier I-B + 3 Tier II + 2 Tier III = 18` live-computed rows, `0` literal flags) across all four active seats (`including explicit bubble/measure scoping of Level-6 scalar mode selection per Finding 3 and parity/chiral scoping of Strong-CP per Finding 5`).
  4. Certifies the final pre-unblinding `0 of 19` vector suite with `-48 \lambda^2 \operatorname{Tr}_Y` and `-11/2` mixed-sector running active in **both** `f64` and `mpmath` (`f64 vs mpmath32 < 2 * (1/1000)^4 * (1/10)`, `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar `< 4 * (1/1000)^5 * (1/10)`, `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa `< 3 * (1/1000)^8` rad).

---

## 2. Gate-by-Gate Audit Summary (`Mask-Clean`)

1. **`Part 4A` — Complete `288`-Point Diagnostics, `PR-10` Casimir, & Same-Dimension Scale Control (`E1_Complete288Diagnostics_CollarCasimir_and_ScaleControl_Gate_passed = True`):**
   - Across all `576` `(point, sector)` matrices on Levels `5, 10, 15`, all `16` tied `3x3` determinant sums satisfy $|\det Y| / \max_\sigma \prod |Y_{i,\sigma(i)}| > 11/10 > 1/10$ and all `96` tied `2x2` minor sums satisfy $\max |\det_2 Y| / \max |Y_{ac}Y_{bd}| > 99/100 > 1/10$.
   - Under repaired `-48` `2`-loop `RGE`, `1,320/1,320` perturbative histories satisfy $\lambda_{\mathrm{IR}} > 42/1000 > 0$ (`I_gauge in (3129/1000000, 4693/1000000)`), and `286/288` vacua (`{"level_5": 24, "level_10": 70, "level_15": 192}`) converge smoothly with `N = 600 vs 1200` step-halving drift `< 3/1000000 < 5 * (1/1000)^2` (`max \epsilon_{\mathrm{UV}} < 31/100`), while only `(0, 3/10)` and `(0, 7/10)` at Level `10` diverge (`\epsilon_{\mathrm{UV}} > 42/10 > 4`).
   - Exact `PR-10` supertrace weights `(c_gauge, c_ferm, c_scal, c_UV, c_IR) = (231/4, 153/4, -3/2, 189/2, 28)` give `max dV_A / dL_4 < -1/10000 < 0` (`vs fake embedded target > 199/100` in `PC_SY4_FakeEmbeddedTargetPotential`), while `PC_SY4_SameDimensionUnselectedMassRatioControl` verifies `rank([[1, 1]]) = 1`, `nullity = 1`, and unselected ratio span `14/3 > 4`.
2. **`Part 4B` — `18`-Row Four-Seat Reconciled Master Closure Matrix (`E2_EighteenRow_FourSeat_MasterClosureMatrix_Gate_passed = True`):**
   - Machine-verifies `8` Tier `I-A` pure-math theorems (`adding T_IA_08 uniting sharp (hV)^{1,3,2} = 0 nilpotence, negative-degree holomorphic jet vanishing [0,0,0,0,0], and Weil S^2 central scalars [-1, +1, -1]`), `5` Tier `I-B` model-conditioned consequences (`adding T_IB_12 uniting closed-fibre 3(B-L) |V_{tb}| = 1 + > 28 (Y_e, Y_d) split + TM1 |U_{e1}|^2 = 2/3, and scoping Level-6 scalar ground-state selection to its stated bubble/measure operator`), `3` Tier `II` conditional parent-to-model bridges (`incorporating PR-10 Casimir dichotomy and X-SYNTHESIS-1..2 hyperbolic Liouville + cusp tail, parent eq. (5) relaxation, and 2-cell Spin(10) singlet sewing`), and `2` Tier `III` explicit remaining source-vector / vacuum-path / scale duties (`including same-dimension unselected mass-ratio nullity = 1 and Picard-Lindelof v_EW`).
3. **`Part 4C` — Final Repaired `-48` Pre-Unblinding `0 of 19` Suite (`E3_FinalRepairedMinus48_ZeroOf19Suite_Gate_passed = True`):**
   - `f64` and `32`-digit `mpmath` (`both with -48 and -11/2`) agree across all `23` scalar ratios and `18` mixing moduli to `< 2 * (1/1000)^4 * (1/10)` (`\lambda_{\mathrm{IR}} \in (329/1000, 330/1000)`, `\sqrt{2\lambda_{\mathrm{IR}}} \in (811/1000, 812/1000)` on `repaired_casimir_equal_1_1_1`), `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar holds to `< 4 * (1/1000)^5 * (1/10)` (`vs right-acting violation > 4/100`), and `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa holds to `< 3 * (1/1000)^8` rad.

`0 of 19.`
