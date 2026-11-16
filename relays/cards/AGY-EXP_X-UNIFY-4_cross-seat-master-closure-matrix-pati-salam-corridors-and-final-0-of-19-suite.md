# Card `X-UNIFY-4` — Cross-Seat Master Closure Matrix (`agy-exp` + `physical` + `agy-002`), Unified `SU(5)` / `Pati–Salam` & Seesaw Corridors, and Final Pre-Unblinding `0 of 19` Suite (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Fourth and final sealed stage of Campaign `X-UNIFY` (`four stages, sixteen blind-sealed commits, 0 of 19`), consolidating Stages `1–3` together with the verified pure-math bridges from `physical` (`9e82adbe9`) and `agy-002/endgame` (`94e511f54`) into: (i) unified `SU(5)` desert ($\Delta_{\mathrm{PS}} = 0$) vs `Pati–Salam` ($\Delta_{\mathrm{PS}} \ge 0$, slope $+506 / (201\pi)$) `P-862` gauge corridors and `286`-vacuum vs `248`-vacuum flavor/seesaw corridors, (ii) a machine-verified `12`-subsystem Three-Column Master Closure Matrix, and (iii) the complete pre-unblinding `0 of 19` prediction suite.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_unify_4_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; literature `RGE` benchmark floats are strictly `AST`-isolated inside the solver-verification gate.

---

## 1. The Package and the Questions

1. **Question `4A` (`Unified P-862 Gauge & Flavor/Seesaw Kill-Line Corridors`):**
   - When `agy-002` Gate `1`'s `1`-parameter `Pati–Salam` threshold law (`exact 1-loop slope +506 / (201*pi)` in $\Delta_{\mathrm{PS}} = \ln(M_U / M_{\mathrm{PS}}) \ge 0$) is combined with our Casimir-stabilized `m004` `SU(5)` desert corridor (`UR-1`, $\Delta_{\mathrm{PS}} = 0$) under the repaired `BPV` `2`-loop solver, does the `1`-loop closed-form slope `(23/134, 109/201, +506/(201*pi))` match numerical `ODE` integration across $\Delta_{\mathrm{PS}} \in [0, 8]$ to `< (1/1000)^4` while smoothly recovering `UR-1` at $\Delta_{\mathrm{PS}} = 0$?
   - Simultaneously, across the step-converged `286`-vacuum full finite population (`100%` of Level `5` and Level `15`, `70/72` of Level `10`) alongside the `248`-vacuum `3a notin Z` population, how do the outward-rounded rational flavor and seesaw corridors behave across `(1, 1, 1)`, Löwdin–Petersson $G_{\mathrm{Pet}}^{-1/2}$, and geometric `(4*pi)` Majorana prescriptions?
2. **Question `4B` (`Machine-Verified 12-Subsystem Cross-Seat Master Closure Matrix`):**
   - When all `12` structural subsystems across `agy-exp`, `physical`, and `agy-002` (`punctured relative carrier, CRT W_15 ~= W_5 (x) W_3 gauge-family split & anomaly k_2/k_1 = 3/5 lock, P-C3 12-method quaternion/Wilson vertex algebra, UR-1/UR-2 & Pati-Salam gauge/scalar corridors, all-288 tropical non-cancellation & 286/288 R2 step-converged flavor/CRT laws, repaired BPV 11/2 2-loop RGE & 7D amphichiral CS(m004) = 0 + 3-family D-parity strong-CP, Frame C Gramian vs Schur-Heisenberg 9-sheet dichotomy, Level-6 M_H^2 unique v_{+pi/6} ground state, classical c_H = kappa(H^2) boundary law & spin registration, Lowdin-Petersson G_Pet^{-1/2} vs 2 EFT puncture ratios, torsion vacuum orbit selection on magnetized 3-bundle, and Picard-Lindelof / Vissani electroweak scale v_EW anchor`) are classified into Columns `I, II, III`, are all `12` computed witnesses exact and internally consistent?
3. **Question `4C` (`Final Blind-Sealed 0-of-19 Prediction Suite & 24-Digit U(3)^6 / Fujikawa Certificate`):**
   - Across the complete `0 of 19` observable suite (`repaired Casimir (1, 1, 1)`, `Lowdin-Petersson G_Pet^{-1/2}`, `geometric 4*pi`, `3-family D-parity trajectory`, and `0-bit Frame C Gramian`), do `f64` and `32`-digit `mpmath` agree to `< (1/1000)^4`, `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar scrambling hold to `< (1/1000)^5`, and `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa strong-CP invariance hold to `< (1/1000)^6` rad?

---

## 2. Deliverables and Definition of Done

1. **`Part 4A`:** Exact symbolic + numerical verification of the unified `SU(5)` / `Pati–Salam` `+506 / (201*pi)` corridor (`\Delta_PS >= 0`) + complete `286`-vacuum vs `248`-vacuum rational corridors across Majorana prescriptions.
2. **`Part 4B`:** Machine-verified `12`-subsystem Three-Column Cross-Seat Master Closure Matrix (`with direct computed numerical witnesses on every row and zero literal flags`) + standalone verification of the `Picard–Lindelöf` homogeneous `mu_H^2` non-crossing identity (`pricing v_EW`).
3. **`Part 4C`:** Final blind-sealed `0 of 19` dimensionless vector suite + `24`-digit $\mathrm{U}(3)^6$ Haar & full $\mathrm{U}(3)$ Fujikawa certificates.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_UnifiedGaugePatiSalam_and_286Corridors_Gate` (`Part 4A`):** Exact symbolic derivation yields `(23/134, 109/201, 506/201)` matching `1`-loop `ODE` integration to `< (1/1000)^4` across $\Delta_{\mathrm{PS}} \in \{0, 2, 4, 8\}$; repaired `2`-loop `SU(5)` `UR-1` (`[3129/1000000, 4693/1000000]`) and `UR-2` (`lambda_IR > 42/1000`) hold across all `1320` histories; and all `286` finite vacua (`including 100% of Levels 5 & 15`) are strictly enclosed by outward-rounded rational corridors.
2. **`E2_TwelveSubsystem_MasterClosureMatrix_Gate` (`Part 4B`):** All `12` subsystems partition cleanly into Columns `I, II, III` (`7` Unconditionally Derived, `3` Conditional Same-Action Reductions, `2` Explicit Remaining Scale/Discrete Items) with verified computed witnesses (`including homogeneous Picard–Lindelöf mu_H^2(t) = mu_H^2(0) exp(...) != 0`).
3. **`E3_FinalZeroOf19Suite_and_Haar6_Gate` (`Part 4C`):** `f64` vs `32`-digit `mpmath` agrees to `< (1/1000)^4`, `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar holds to `< (1/1000)^5`, and `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa holds to `< (1/1000)^6` rad.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage4_Unify_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside target-free geometry and rational-eliminant functions.
2. **`PC_U4_WrongPatiSalamSignOrHypercharge`:** Flipping the sign of `+506 / (201*pi)` fails the `Pati–Salam` `ODE` trajectory by `> 1/100`, and setting `k_2/k_1 = 1` shifts $\sin^2\theta_{\mathrm{EW}}$ by `> 8/100`.
3. **`PC_U4_ParityPiBranchAndReversedMixedOrder`:** Setting $\theta_{\mathrm{YM}} = \pi$ gives $|\bar{\theta}_{\mathrm{phys}}| = \pi > 3$ rad, and un-transposed `2`-loop mixed ordering fails the `11/2` benchmark by `> 1/100`.
4. **`PC_U4_RightActingRGEHaarViolation`:** Placing `1`-loop Yukawa matrices on the right of $Y_f$ breaks $\mathrm{U}(3)_R$ Haar singular-value invariance by `> 1/1000`.

`0 of 19.`
