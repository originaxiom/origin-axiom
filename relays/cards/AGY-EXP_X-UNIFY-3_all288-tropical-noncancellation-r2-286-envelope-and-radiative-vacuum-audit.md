# Card `X-UNIFY-3` — All-`288` Tropical Minor Non-Cancellation Theorem, `R2` Step-Converged `286`-Vacuum Full Envelope (`100%` of Levels `5` & `15`), and Coupled Radiative Vacuum-Selection Audit (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Third sealed stage of Campaign `X-UNIFY` (`four stages, sixteen blind-sealed commits, 0 of 19`), discharging `physical`'s `38b08c496` `R2` step-convergence & `288`-point tropical-minor non-cancellation duties alongside a standalone verification of `agy-002` Gate `2`'s Level-`6` scalar mass matrix $M_H^2$ and an honest Guardrail-`1` test of the coupled `1`-loop radiative vacuum potential across $\mathcal{O}_{32}$.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_unify_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; literature `RGE` benchmark floats are strictly `AST`-isolated inside the solver-verification gate.

---

## 1. The Package and the Questions

1. **Question `3A` (`Complete 288-Point 3-Point Power-Law-Eliminated Tropical Minor Non-Cancellation Verification`):**
   - Across **all `288 = 24 + 72 + 192` primitive torsion vacua** at Levels `5, 10, 15` (`576` matrices across `sec2` and `sec3`, zero sampling), do `320`-digit `mpmath` `3`-point power-law-eliminated asymptotic singular-value slopes ($y \in \{110, 150, 190\}$ at $\operatorname{Re}\tau = \operatorname{Re}\tau^*$) match the exact rational piecewise-quadratic theorem `tropical_svd_exponents_exact` to `< 5/1000` (`well below the minimal rational exponent step 1/30`) on **every single one of the `288` points** (`proving zero leading-minor phase cancellations anywhere on E*[5] U E*[10] U E*[15]`), while also confirming `Frame C` whole-orbit minima (`1 : 1` at Levels `5` and `10` vs `3/2` triality split at Level `15`)?
2. **Question `3B` (`physical R2 Diagnosis — Step-Converged 286/288 Full Finite Envelope & Exact UV Loop-Threshold Separation`):**
   - When all `40` meridian-trivial (`3a in Z`) vacua (`4 + 4 + 32`) are audited with step-refinement (`N_steps = 600` vs `1200` vs coarse `N_steps = 48`):
     1. Were `18` of the `20` apparent `3a in Z` overflows in `X-RELATIONS` (`2` at Level `5` and `16` at Level `15`, where $\|Y_{\mathrm{UV}}\|_2 < 7$ and $\epsilon_{\mathrm{UV}} = \|Y_{\mathrm{UV}}\|_2^2 / (16\pi^2) < 7/20 < 1$) actually **coarse `N_steps = 48` explicit-`RK4` step-stiffness artifacts** (`exactly as physical R2 warned to diagnose!`), so that at `N_steps >= 600` (`600 vs 1200 max diff < (1/1000)^2`) **all `24/24` Level-`5` vacua, all `192/192` Level-`15` vacua (`100%` of `m004`'s cover!), and `70/72` Level-`10` vacua (`286 of 288` total!) converge smoothly**?
     2. Are the **unique `2` genuinely diverging vacua out of `288`** (`(0, 3/10)` and `(0, 7/10)` at Level `10`) cleanly separated by $\epsilon_{\mathrm{UV}} = \|Y_{\mathrm{UV}}\|_2^2 / (16\pi^2) > 4 > 1$ (`exceeding 4*pi unitarity by > 2x at the UV boundary itself, so 2-loop exceeds 1-loop at t = 0 and diverges on the initial step across N_steps = 600 and 1200` with `|t_pole(1200) - t_pole(600)| < 3/100`)?
     3. What are the complete outward-rounded rational kill-line corridors across **all `286` finite vacua** (`24 + 70 + 192`) side-by-side with the `248`-vacuum `3a notin Z` corridors?
3. **Question `3C` (`Coupled Radiative Vacuum-Selection Audit: Level-6 M_H^2 Ground State & Coupled Radiative Potential on O_32`):**
   - Built standalone without repository imports, does the `6`-dimensional Level-`6` scalar mass-squared operator $M_H^2 = K_{\mathrm{KK}} - \kappa_1 \Sigma_H$ exhibit degeneracy `d = 3` (`log_2 3` bits) on pure $\Sigma_H$, `d = 2` (`1` bit) on pure $K_{\mathrm{KK}}$, and a **unique non-degenerate `d = 1` (`0`-bit) ground state $v_{+\pi/6}$** when combined?
   - Across all `16` twin pairs of $\mathcal{O}_{32}$ at $(\tau^*, A_{\mathrm{Cas}}^*)$, does adding the `1`-loop coupled Yukawa radiative potential $V_{\mathrm{rad}}^{\mathrm{Yuk}}(w)$ to $V_{\mathrm{Cas}}(w)$ select a unique twin pair (`0` bits) or leave an explicit discrete orbit rank (`priced honestly under Guardrail 1 with zero post-inspection tuning`)?

---

## 2. Deliverables and Definition of Done

1. **`Part 3A`:** Symbolic tie-multiplicity census + complete `288`-point (`576`-matrix) `320`-digit `mpmath` `3`-point power-law-eliminated asymptotic verification of `tropical_svd_exponents_exact` + `Frame C` whole-orbit cusp minima check.
2. **`Part 3B`:** `N_steps = 48` vs `600` vs `1200` step-convergence proof across all `288` vacua, UV loop-expansion threshold theorem ($\epsilon_{\mathrm{UV}} < 7/20 < 1$ on all `286` finite vacua vs $\epsilon_{\mathrm{UV}} > 4 > 1$ on the `2` Level-`10` blowups), and complete `286`-vacuum vs `248`-vacuum rational corridors.
3. **`Part 3C`:** Standalone verification of Level-`6` $(U_M^{(6)})^{12} = I_6$ and $M_H^2 = K_{\mathrm{KK}} - \kappa_1 \Sigma_H$ (`d = 3, 2, 1` bit ledger) + honest Guardrail-`1` ranking of all `16` $\mathcal{O}_{32}$ twin pairs under $V_{\mathrm{Cas}} + V_{\mathrm{rad}}^{\mathrm{Yuk}}$.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_All288_TropicalMinor_NonCancellation_Gate` (`Part 3A`):** Maximum discrepancy between `320`-digit `mpmath` `3`-point slopes ($y \in \{110, 150, 190\}$) and exact rational `tropical_svd_exponents_exact` across **all `288` vacua** (`576` matrices) is `< 5/1000` (`zero minor cancellations anywhere`), with exact `Frame C` whole-orbit minima equality at Levels `5` and `10` and `3/2` split at Level `15`.
2. **`E2_Full286Envelope_and_R2Diagnosis_Gate` (`Part 3B`):** At `N_steps = 600` and `1200`, `24/24` Level-`5`, `192/192` Level-`15`, and `70/72` Level-`10` vacua (`286/288` total) converge smoothly (`max |obs(1200) - obs(600)| < (1/1000)^2`, all satisfying $\epsilon_{\mathrm{UV}} < 7/20 < 1$), while the `2` diverging Level-`10` vacua (`(0, 3/10), (0, 7/10)`) satisfy $\epsilon_{\mathrm{UV}} > 4 > 1$ and diverge immediately at $t = 0$ (`|t_pole(1200) - t_pole(600)| < 3/100`).
3. **`E3_Level6Higgs_and_HonestRadiativeVacuum_Gate` (`Part 3C`):** $(U_M^{(6)})^{12} = I_6$ holds to `< (1/1000)^4`; pure $\Sigma_H$ gives `d = 3`, pure $K_{\mathrm{KK}}$ gives `d = 2`, and combined $M_H^2$ gives unique `d = 1` (`0` bits) with $|v_{\min}^\dagger v_{+\pi/6}|^2 > 999/1000$; and the `16`-pair $\mathcal{O}_{32}$ `V_Cas + V_rad` ranking is computed directly from the action and priced strictly under Guardrail `1`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage3_Unify_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside target-free geometry and rational-exponent functions.
2. **`PC_U3_PlantedTiedMinorCancellation`:** Constructing a $3\times 3$ $q$-matrix whose two tied leading permutations cancel shifts the `3`-point asymptotic determinant slope away from its naive tropical sum by `> 1/10`.
3. **`PC_U3_CoarseRK4StepStiffnessArtifact`:** Running `3a in Z` vacua at coarse `N_steps = 48` causes `18` stiff-but-perturbative vacua (`\epsilon_UV < 7/20`) to overflow, whereas `N_steps = 600` and `1200` converge smoothly on all `18`.
4. **`PC_U3_OmitKKHolonomyDegeneracyBit`:** Setting $K_{\mathrm{KK}} = 0$ in Level-`6` $M_H^2$ restores `d = 3` degeneracy (`requiring log_2 3 > 1 bits`).

`0 of 19.`
