# Card `X-CLOSURE-4` — $\mathrm{U}(3)$ Frame-Rotation Control on $G_{\mathrm{Pet}}^{-1/2}$, `14`-Row Four-Tier Scoped Master Closure Matrix, Non-Hermitian Schur Control, and Final Pre-Unblinding `0 of 19` Suite

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Fourth and final sealed stage of Campaign `X-CLOSURE` (`four stages, sixteen blind-sealed commits, 0 of 19`), repairing `physical` `e250dab15` Items `C` and `D` (`16-frame U(3) Petersson-orthonormal rotation control on G_Pet^{-1/2}, four-tier model-vs-parent closure matrix separating unconditional mathematics from model-conditioned theorems and parent-to-model bridges, and replacement of "iff" by "sufficient" on mirror parity decoupling via the non-Hermitian positive-real Schur control`) and sealing the final pre-unblinding `0 of 19` diagnostic suite.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_closure_4_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`all model functions strictly zero-float; published RGE solver benchmarks AST-isolated`).

---

## 1. The Package and the Questions

1. **Question `4A` (`Item C` Repair — `16`-Frame $\mathrm{U}(3)$ Rotation Control on $G_{\mathrm{Pet}}^{-1/2}$ & Unified Corridors):**
   - For `16` deterministic $\mathrm{U}(3)$ matrices $U^{(k)}$, does every rotated operator frame $E'^{(k)}_a = \sum_b (G_{\mathrm{Pet}}^{-1/2} U^{(k)})_{ba} A_b$ satisfy exact Petersson orthonormality $\langle E'^{(k)}_a, E'^{(k)}_b\rangle_{\mathrm{Pet}} = \delta_{ab}$ while its equal-coefficient source vector $c(U^{(k)}) = G_{\mathrm{Pet}}^{-1/2} U^{(k)} \mathbf{1}_3$ sweeps infrared `sec4_r23` across orders of magnitude (`> 1000x`), proving by explicit counterexample that metric isotropy alone cannot select the `2` heavy-singlet source-vector ratios?
   - Inside the unified `m004 + SU(5)/Pati–Salam + magnetized-bundle` model, do the exact `(23/134, 109/201)` + `506/(201*pi)` law, the `1320`-history `UR-1/UR-2` corridors, and the `286/288` step-converged perturbative envelope hold unchanged?
2. **Question `4B` (`Item D` Repair — `14`-Row Four-Tier Scoped Master Closure Matrix & Non-Hermitian Schur Control):**
   - Does a machine-verified `14`-row closure matrix (`6` in Tier `I-A` Unconditional Pure Math, `4` in Tier `I-B` Model-Conditioned Consequences, `2` in Tier `II` Conditional Parent-to-Model Bridges including `P-C3b`, and `2` in Tier `III` Explicit Remaining Source-Vector / State-Composition / Scale Duties) certify every row with live computed witnesses and zero literal flags?
   - On the `6x6` heavy-light block matrix $\mathcal{M}_{6\times 6} = \begin{psmallmatrix} I_3 & i b I_3 \\ i c I_3 & I_3 \end{psmallmatrix}$ ($b = 2/5, c = 3/7$), does $\mathcal{M}_{6\times 6}$ break Hermitian parity symmetry (`\|\mathcal{M} - \mathcal{M}^\dagger\|_F > 1`) with nonzero imaginary off-diagonal blocks while still giving a strictly positive-real light Schur complement $L - B H^{-1} C = (1 + bc) I_3 > 0$ (`zero determinant phase`), proving algebraically that parity-symmetric mirror decoupling is **sufficient** (`not "iff"`) for vanishing determinant phase?
3. **Question `4C` (`Final Pre-Unblinding 0-of-19 Suite & Basis-Scrambling Certificates`):**
   - Do all repaired `0 of 19` vectors agree between `float64` and `32`-digit `mpmath` to `< (1/1000)^4`, and pass `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance (`< (1/1000)^5`) and `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa strong-CP invariance (`< (1/1000)^6` rad)?

---

## 2. Deliverables and Definition of Done

1. **`Part 4A`:** `16`-frame $\mathrm{U}(3)$ Petersson-orthonormal basis rotation audit (`PC_CL4_MetricIsotropyCannotSelectVector`) + `Pati–Salam` `+506/(201*pi)`, `1320`-history `UR-1/UR-2`, and `286/288` step-converged `R2` verification.
2. **`Part 4B`:** Machine-verified `14`-row Four-Tier Scoped Master Closure Matrix (`6 + 4 + 2 + 2 = 14` live-witnessed rows incorporating repaired Stage `1` Weil/Zickert–Rogers theorems and Stage `2–3` `P-C3b` witnesses) + non-Hermitian positive-real Schur counterexample (`PC_CL4_NonHermitianPositiveRealSchurCounterexample`).
3. **`Part 4C`:** Final repaired `0 of 19` suite + `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar and `12`-factor full $\mathrm{U}(3)$ Fujikawa certificates.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_U3FrameRotationControl_and_Corridors_Gate` (`Part 4A`):** All `16` $\mathrm{U}(3)$-rotated frames satisfy Petersson orthonormality to `< (1/1000)^4` while `max(sec4_r23) / min(sec4_r23) > 1000` and `max(sec4_r12) - min(sec4_r12) > 1/10`; `Pati–Salam` `ODE` residual `< (1/1000)^4`; `1320`-history `min lambda_IR > 42/1000`; and finite `N = 600` counts equal `(24, 70, 192)`.
2. **`E2_FourteenRow_FourTier_MasterClosureMatrix_Gate` (`Part 4B`):** All `14` rows (`6 + 4 + 2 + 2`) pass live witness checks (`repaired Weil (ST)^3 - S^2 < (1/1000)^4, Zickert–Rogers |CS(m004) mod 1/2| < (1/1000)^15 vs |CS(m003) - 1/4| < (1/1000)^15, P-C3b kernel (1, 2, 1) & gap 3/4, non-Hermitian Schur phase = 0 rad with asymmetry > 1, and Picard–Lindelöf residual < (1/1000)^4`).
3. **`E3_FinalZeroOf19Suite_and_Haar6_Gate` (`Part 4C`):** `float64` vs `32`-digit `mpmath` max diff `< (1/1000)^4`; `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar max diff `< (1/1000)^5`; and `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa max diff `< (1/1000)^6` rad.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage4_Closure_Passed`:** `AST` check confirming zero disallowed imports and zero float literals in all `10` target-free model functions.
2. **`PC_CL4_MetricIsotropyCannotSelectVector`:** Rotating the Petersson-orthonormal basis by $U \in \mathrm{U}(3)$ preserves $\langle E'_a, E'_b\rangle_{\mathrm{Pet}} = \delta_{ab}$ identically while shifting `sec4_r23` by `> 1000x`, falsifying any claim that $G_{\mathrm{Pet}}^{-1/2}$ alone determines a unique source vector.
3. **`PC_CL4_NonHermitianPositiveRealSchurCounterexample`:** Setting $H = L = I_3, B = i(2/5)I_3, C = i(3/7)I_3$ breaks Hermitian parity symmetry (`asymmetry > 1`) while maintaining `arg det(L - B H^{-1} C) = 0`, falsifying `"iff"` necessity claims while generic asymmetric mirror mixing shifts phase `> 1/10` rad and bare $\theta_{\mathrm{bare}} = \pi$ shifts $\bar{\theta}_{\mathrm{phys}}$ to $\pi$.
4. **`PC_CL4_RightActingRGEHaarViolation`:** Corrupting chirality in `RGE` running breaks right-handed $\mathrm{U}(3)$ invariance (`> 1/1000`).

`0 of 19.`
