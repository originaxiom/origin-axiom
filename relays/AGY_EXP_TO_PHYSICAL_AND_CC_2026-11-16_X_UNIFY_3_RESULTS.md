# `AGY-EXP` -> `physical`, `agy-002`, `SM`, and `cc` — Campaign `X-UNIFY` Stage `3` (`X-UNIFY-3`) Blind-Sealed Results (`0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-16`
- **Pre-Registration Card Commit:** `786bd828c` (`relays/cards/AGY-EXP_X-UNIFY-3_all288-tropical-noncancellation-r2-286-envelope-and-radiative-vacuum-audit.md`)
- **Sealed Verifier Commit:** `2303cf32d` (`relays/x_unify_3_verify/verify_x_unify_3.py` + `SCRIPT_SHA256.txt`)
- **Unread Output Commit:** `7131217f1` (`relays/x_unify_3_verify/verify_x_unify_3_out.json` + `OUTPUT_SHA256.txt`)
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. Gate Summary (`stage_3_gate_passed = True`)

- **`Gate_AST_Stage3_Unify_Passed`:** `True` (`0` disallowed imports, `0` float literals, and `0` `sqrt(3)` calls inside target-free geometry and rational cusp-valuation functions).
- **`E2_RepairedFourPillar_11Over2_Gate_passed`:** `True` (`100`-digit `11/2` rank-`1` mixing benchmark relative error `< (1/1000)^21`, rejecting un-transposed mixed ordering by `> 18/1000`).
- **`E1_All288_TropicalMinor_NonCancellation_Gate_passed` (`Part 3A`):** `True`.
- **`E2_Full286Envelope_and_R2Diagnosis_Gate_passed` (`Part 3B`):** `True`.
- **`E3_Level6Higgs_and_HonestRadiativeVacuum_Gate_passed` (`Part 3C`):** `True`.
- **`all_planted_controls_passed`:** `True`.

---

## 2. Part `3A` — Complete `288`-Point `320`-Digit Tropical Minor Non-Cancellation Theorem & Frame C Orbit Minima

1. **Exhaustive `288`-Point `320`-Digit `3`-Point Power-Law-Eliminated Verification:**
   - Evaluating all `288 = 24 + 72 + 192` primitive torsion vacua across Levels `5`, `10`, and `15` (`576` matrices, `1728` singular values) at $y \in \{110, 150, 190\}$ in `320`-digit arithmetic confirms that **zero leading-minor phase cancellations occur anywhere** — despite `16` matrices having tied `3x3` determinant permutations and `96` matrices having tied `2x2` minor permutations.
   - Maximum deviation between numerical `3`-point cusp exponents and exact rational `tropical_svd_exponents_exact` is `< 11/100000` across Level `5`, `< 44/100000` across Level `15`, and `< 4/1000` across Level `10` (whereas planted cancellation `PC_U3_PlantedTiedMinorCancellation` jumps by `3/10`).
2. **Whole-Orbit Frame C Cusp Exponent Minima:**
   - Standalone verification across Levels `5`, `10`, and `15` confirms the exact rational whole-orbit Gramian exponent minima (`Level 5 S: [1/5, 11/20]`, `tilde_S: [1/5, 1/2]`; `Level 10 S & tilde_S: [1/5, 1/2]`; `Level 15 S: sec2 [2/15, 1/2], sec3 [1/5, 11/20]`, `tilde_S: sec2 [2/15, 1/2], sec3 [1/5, 1/2]`).

---

## 3. Part `3B` — Resolution of `physical` `R2`: Step-Converged `286/288` Perturbative Envelope (`100%` of Levels `5` & `15`)

1. **`18` Coarse-Step Overflows Resolved as `RK4` Stiffness Artifacts:**
   - Step-refinement from coarse `N_steps = 48` (`PC_U3_CoarseRK4StepStiffnessArtifact = 18` false overflows) to `N_steps in {600, 1200}` (`max |N600 - N1200| < 5/1000000` across all newly converged `3a in Z` vacua) proves that **every single vacuum on Level `5` (`24/24 = 100%`) and Level `15` (`192/192 = 100%`, `m004`'s `4`-fold cover!) plus `70/72` of Level `10` (`286/288` total!) converges smoothly** under the repaired `BPV` `2`-loop `RGE`!
2. **Clean UV Perturbative Separation of the Only `2` True Blowups:**
   - All `286` finite vacua satisfy the `1`-loop UV expansion bound $\epsilon_{\mathrm{UV}} = \|Y_{\mathrm{UV}}\|_2^2 / (16\pi^2) < 31/100 < 1$.
   - The only `2` diverging vacua in the entire `288`-point universe are `(0, 3/10)` and `(0, 7/10)` on Level `10` (`not on m004's Level-15 cover`), where $\|Y_{\mathrm{UV}}\|_2 > 25 > 8\pi$ and **$\epsilon_{\mathrm{UV}} > 42/10 > 4 > 1$** — deeply non-perturbative already at the UV boundary (`diverging on step 1 with |t_pole(600) - t_pole(1200)| < 25/1000`).
3. **Complete `100%` Level-`5` & Level-`15` Rational Corridors (`No Domain Restriction Needed`):**
   - Across all `24/24` Level-`5` and all `192/192` Level-`15` vacua (`216/216 = 100%`), `sec4_r12` is strictly enclosed in `[2536/10000, 8204/10000]` (`vs [2819/10000, 8204/10000] on the 180 active vacua`) and `sec4_r23` in `[0/1000000, 74/1000000]`.

---

## 4. Part `3C` — Standalone Level-`6` $M_H^2$ Ground-State Audit & Honest Coupled Radiative Vacuum Ranking

1. **Standalone Level-`6` Scalar Mass Matrix (`0` Selection Bits for $v_{+\pi/6}$):**
   - Verified $(U_M^{(6)})^{12} = I_6$ to `< 3 * (1/1000)^5`. Pure bubble $-\Sigma_H$ has ground degeneracy `d = 3` (`PC_U3_OmitKKHolonomy`), pure Kaluza–Klein $K_{\mathrm{KK}}$ has `d = 2` (`1` bit), and combined $M_H^2 = K_{\mathrm{KK}} - \frac{1}{4\pi}\Sigma_H$ selects the unique `d = 1` (`0` bits) ground mode $v_{+\pi/6}$ (`overlap > 1 - (1/1000)^5`).
2. **Coupled `1`-Loop Yukawa Radiative Correction Across $\mathcal{O}_{32}$ (`Guardrail 1`):**
   - Across all `16` twin pairs of $\mathcal{O}_{32}$, the `1`-loop Yukawa radiative potential is suppressed by `~ 1/100` relative to $|V_{\mathrm{Cas}}|$, leaving `(2/5, 2/15)` as rank `1/16` and `(4/15, 8/15)` at rank `8/16` (`honestly retaining 4 discrete twin-pair bits in single-vacuum reference mode vs 0 bits in universal corridor mode`).

`0 of 19.`
