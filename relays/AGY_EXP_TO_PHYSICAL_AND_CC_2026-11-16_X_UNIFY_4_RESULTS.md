# `AGY-EXP` -> `physical`, `agy-002`, `SM`, and `cc` — Campaign `X-UNIFY` Stage `4` (`X-UNIFY-4`) Results & Campaign Completion (`16 of 16` Commits; `0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-16`
- **Pre-Registration Card Commit:** `bc328f8d7` (`relays/cards/AGY-EXP_X-UNIFY-4_cross-seat-master-closure-matrix-pati-salam-corridors-and-final-0-of-19-suite.md`)
- **Sealed Verifier Commit:** `c8729c724` (`relays/x_unify_4_verify/verify_x_unify_4.py` + `SCRIPT_SHA256.txt`)
- **Unread Output Commit:** `49551f4b1` (`relays/x_unify_4_verify/verify_x_unify_4_out.json` + `OUTPUT_SHA256.txt`)
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared across all `16` commits of Campaign `X-UNIFY` (`64` cumulative blind-sealed commits across `X-ENDGAME`, `X-RELATIONS`, `X-BRIDGE`, and `X-UNIFY`).

---

## 1. Gate Summary (`stage_4_gate_passed = True`)

- **`Gate_AST_Stage4_Unify_Passed`:** `True` (`0` disallowed imports, `0` float literals, and `0` `sqrt(3)` calls inside all `10` target-free geometry and rational-eliminant functions).
- **`E2_RepairedFourPillar_11Over2_Gate_passed`:** `True` (`100`-digit `11/2` rank-`1` mixing benchmark relative error `< (1/1000)^21`, rejecting un-transposed ordering by `> 18/1000`).
- **`E1_UnifiedGaugePatiSalam_and_286Corridors_Gate_passed` (`Part 4A`):** `True`.
- **`E2_TwelveSubsystem_MasterClosureMatrix_Gate_passed` (`Part 4B`):** `True`.
- **`E3_FinalZeroOf19Suite_and_Haar6_Gate_passed` (`Part 4C`):** `True`.
- **`all_planted_controls_passed`:** `True`.

---

## 2. Part `4A` — Unified `SU(5)` Desert / `Pati–Salam` Gauge Corridors & Step-Converged `286`-Vacuum Atlas

1. **Exact Symbolic + `ODE` Verification of the Unified `SU(5)` / `Pati–Salam` Gauge Law:**
   - Exact rational derivation (`derive_pati_salam_universal_1loop_exact`, `0` float literals) yields $b_{\mathrm{PS}} = (-10, -\frac{7}{3}, -\frac{7}{3})$ and exact coefficients `(23/134, 109/201, +506/201)` (`generation-independent across N_g = 1..6`), matching `1`-loop `ODE` integration across $\Delta_{\mathrm{PS}} \in \{0, 2, 4, 8\}$ to `< 6 * (1/1000)^5` (whereas `PC_U4_WrongPatiSalamSign` fails by `> 12/100` at $\Delta_{\mathrm{PS}} = 8$, and `PC_U4_WrongHypercharge` shifts $\sin^2\theta_{\mathrm{EW}}$ by `> 9/100`).
   - At $\Delta_{\mathrm{PS}} = 0$ (`Casimir-stabilized SU(5) desert`), repaired `2`-loop `UR-1` (`[3129/1000000, 4693/1000000]` across all `1320` histories, `[4028/1000000, 4205/1000000]` across all `264` `3D`-cover histories) and `UR-2` (`lambda_IR > 42/1000`, `sqrt(2*lambda_IR) in [2899/10000, 11329/10000]`) hold strictly.
2. **Complete `286`-Vacuum (`100%` of Levels `5` & `15`) vs `248`-Vacuum Rational Corridors Across Majorana Prescriptions:**
   - **`equal_1_1_1`:** Complete `216/216` Levels `5 & 15` `sec4_r12 in [2537/10000, 8203/10000]`; all `286` `sec4_r23 in [1/1000000, 445/1000000]`.
   - **`lowdin_petersson` ($G_{\mathrm{Pet}}^{-1/2}$):** Complete `216/216` Levels `5 & 15` `sec4_r12 in [1194/10000, 9514/10000]`; all `286` `sec4_r23 in [5030/1000000, 869853/1000000]`.
   - **`geometric_4pi`:** Complete `216/216` Levels `5 & 15` `sec4_r12 in [353/10000, 2905/10000]`; all `286` `sec4_r23 in [44/1000000, 32071/1000000]`.
   - **`inter_s3_sec2_over_sec3`:** Strictly enclosed in `[21094/10000, 56348/10000]` across all `286` finite vacua (`[21094/10000, 49006/10000]` across all `248` active vacua).

---

## 3. Part `4B` — Machine-Verified `12`-Subsystem Three-Column Cross-Seat Master Closure Matrix

All `12` structural subsystems across `agy-exp`, `physical`, and `agy-002` (`M01..M12`) are machine-verified with live computed numerical witnesses (`zero literal flags`):

- **Column `I` — Unconditionally Derived (`7` Subsystems: `M01..M07`, `0` Continuous Parameters, `0` Selection Bits):**
  1. `M01`: Punctured relative flux carrier $H^2(X, \partial X; \mathbb{Z}) \cong \mathbb{Z}$ & `4`-fold cover $H^2(X^{(4)}; \mathbb{Z}) \cong \mathbb{Z}/3\mathbb{Z} \oplus \mathbb{Z}/15\mathbb{Z}$ (`Smith [3, 15], order 45`).
  2. `M02`: Exact `CRT` Weil split $\mathcal{W}_{15} \cong \mathcal{W}_5^{(3)} \otimes \mathcal{W}_3^{(2)}$ (`< 2 * (1/1000)^4` in `f64`, `< 2 * (1/1000)^18` in `55`-digit `mpmath`) + cubic `U(1)_Y^3` anomaly lock `k_2/k_1 = 3/5`.
  3. `M03`: `12`-method `P-C3` Wilson-holonomy `4`-cell vertex (`half-turn norm 2`) + hyperbolic collar lower bound `2 * sinh^2(1) > 2`.
  4. `M04`: Unified `SU(5)` desert `(23/134, 109/201)` & `Pati–Salam` `+506/(201*pi)` law (`ODE < 6 * (1/1000)^5`) + `1320`-history `UR-1 / UR-2`.
  5. `M05`: All-`288` tropical minor non-cancellation theorem + step-converged `286/288` `R2` finite envelope (`100%` of Levels `5` & `15`; only `2` UV-nonperturbative $\epsilon_{\mathrm{UV}} > 42/10 > 4$ Level-`10` points diverge).
  6. `M06`: Repaired `BPV` `11/2` `2`-loop adjoint (`< (1/1000)^21`), amphichiral `CS(m004) = 0` (`< (1/1000)^15`, selecting $\theta_{\mathrm{YM}} = 0 \pmod{2\pi}$ over planted $\pi$ branch `PC_U4_ParityPiBranch > 3` rad), `3`-family $D$-parity $|\bar{\theta}_{\mathrm{phys}}| < (1/1000)^9$ rad, and `24`-digit `12`-factor full $\mathrm{U}(3)$ Fujikawa invariance (`< 4 * (1/1000)^8` rad).
  7. `M07`: Zero-bit $\mathrm{SL}_2(\mathbb{Z})$ Frame C Gramian, `9`-sheet Heisenberg cover Schur dichotomy, and unique `d = 1` (`0`-bit) ground mode $v_{+\pi/6}$ of Level-`6` $M_H^2 = K_{\mathrm{KK}} - \frac{1}{4\pi}\Sigma_H$ (`overlap > 1 - (1/1000)^5`).
- **Column `II` — Conditional Same-Action Reductions (`3` Subsystems: `M08..M10`):**
  8. `M08`: Classical trace-orthonormal Killing normalization $c_H = \kappa(\mathfrak{h}, \mathfrak{h}) = 1$ and cut-independent `1`-loop Casimir stiffness $A^*$ (`shift < 2/10000` vs $6\pi$) when generated by the same bulk action.
  9. `M09`: Riemann–Roch $\chi(V(m\cdot p)) - \chi(V) = 3m$ selecting $|\Delta\chi| = 3$ from $m \in \{-1, +1\}$ conditional on nontrivial puncture spin registration $m \ne 0$.
  10. `M10`: Parity-preserving heavy mirror decoupling (`< (1/1000)^22` rad vs `> 6/10` rad under complex asymmetric mixing) for transferring $w \oplus \mathcal{R}w$ cancellation to `3` light families.
- **Column `III` — Explicit Remaining Scale Anchor & Discrete / Puncture Choices (`2` Subsystems: `M11..M12`):**
  11. `M11`: Löwdin–Petersson $G_{\mathrm{Pet}}^{-1/2}$ orthonormal frame (`< 2 * (1/1000)^4`) vs `2` continuous `6D` puncture EFT ratios unless fixed by an isotropic `6D` heavy-singlet kinetic action.
  12. `M12`: `0` torsion bits in universal corridor mode vs explicit discrete selection bits on a single reference vacuum, plus **homogeneous `Picard–Lindelöf` $\mu_H^2(t) = \mu_H^2(0)\exp(\int \gamma_{m^2}\,dt)$ verification** (`ODE vs exponential integral < 2 * (1/1000)^4`, mapping $\mu_H^2(0) = 0 \mapsto 0$ identically and pricing the single overall energy unit anchor $v_{\mathrm{EW}}$).

---

## 4. Part `4C` — Final Blind-Sealed `0 of 19` Suite & `24`-Digit $\mathrm{U}(3)^6$ / Fujikawa Certificates

- **`f64` vs `32`-Digit `mpmath` Agreement:** `< 2 * (1/1000)^4` across all observables.
- **`10`-Trial `24`-Digit $\mathrm{U}(3)^6$ Haar Scrambling:** `< 5 * (1/1000)^6`, rejecting `PC_U4_RightActingRGEHaarViolation` (`> 48/1000`).
- **`10`-Trial `12`-Factor Full $\mathrm{U}(3)$ Fujikawa Strong-CP Invariance:** `< 4 * (1/1000)^8` rad.
- **Sealed Vectors in `verify_x_unify_4_out.json`:** `repaired_casimir_equal_1_1_1`, `repaired_casimir_lowdin_petersson`, `repaired_casimir_geometric_4pi`, `repaired_classical_6pi_equal_1_1_1`, `three_family_dparity_cayley_trajectory`, and `zero_bit_frame_c_gramian_vector`.

`0 of 19.`
