# Card `X-UNIFY-2` — Löwdin–Petersson & Geometric Serre Majorana Normalization, `7D` Amphichiral $\operatorname{CS}(\mathrm{m004}) = 0$ (`0` vs $\pi$ Branch Audit), and `3`-Family $D$-Parity Strong-CP Closure Under Repaired `BPV` `2`-Loop `RGE`s (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Second sealed stage of Campaign `X-UNIFY` (`four stages, sixteen blind-sealed commits, 0 of 19`), addressing: (i) the rank-`1` jet structure and Löwdin–Petersson orthonormalization ($G_{\mathrm{Pet}}^{-1/2}$) vs parameter-free geometric Serre scaling of $M_R(\tau)$, (ii) `physical`'s `ca500dad6` Intake Point `2` (`distinguishing the parity-allowed theta_YM = pi branch from the theta_YM = 0 mod 2pi branch fixed by amphichiral 3D Chern–Simons CS(m004) = 0`), and (iii) `3`-family chiral Strong-CP vanishing without light mirror doubling (`agy-002` Gate `1` $D$-parity audited for the first time under the repaired left-acting `BPV` eq. `27` `2`-loop `RGE` + full $\mathrm{U}(3)^6$ Fujikawa anomaly shift).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_unify_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; literature `RGE` benchmark floats are strictly `AST`-isolated inside the solver-verification gate.

---

## 1. The Package and the Questions

1. **Question `2A` (`Rank-1 Jet Filtration, Löwdin–Petersson Orthonormalization G_Pet^{-1/2}, & Parameter-Free Serre Puncture Prescriptions for M_R`):**
   - Since each basis tensor $A_v = y^3 \bar{E}_6\, v \otimes v$, $A_w = y^2 \bar{E}_4\, w \otimes w$, and $A_u = u \otimes u$ individually has matrix rank `1` (`so invertible 3-generation seesaw M_R^{-1} requires all three jet channels`) while $(A_w, A_u)$ are `> 98/100` collinear in Petersson Hilbert space, how does exact **Löwdin–Petersson symmetric orthonormalization** $(\hat{E}_v, \hat{E}_w, \hat{E}_u) = G_{\mathrm{Pet}}^{-1/2} (A_v, A_w, A_u)$ (`satisfying <E_a, E_b>_Pet = delta_{a b} to < (1/1000)^4` with `0` continuous parameters once isotropic heavy-singlet kinetic normalization is specified) compare against the parameter-free geometric Serre derivative scaling $\ell_p^2 = A / (4\pi)$ and `(1, 1, 1)` across `sec4` infrared ratios?
2. **Question `2B` (`7D Amphichiral CS(m004) = 0 Selecting theta_YM = 0 mod 2pi, Exact 2-Loop Determinant-Phase Conservation, & 3-Family D-Parity Strong-CP`):**
   - From target-free `(L, R)` hyperbolic holonomy on `m004`, does orientation-reversing amphichirality $\iota: M_3 \to M_3$ force the `3D` Chern–Simons / Plebanski imaginary volume difference to vanish to `< (1/1000)^15` (`selecting the connected theta_YM = 0 mod 2pi branch, whereas the parity-allowed theta_YM = pi branch gives theta_bar_phys = pi as noted by physical ca500dad6`)?
   - Does the repaired left-acting `BPV` eq. `27` `1`-loop + `2`-loop `RGE` satisfy the **exact algebraic identity** $\operatorname{Im}\frac{d}{d\ln\mu}\ln\det(Y_1 Y_2)\big|_{1+2\text{ loop}} \equiv 0$ (`to < (1/1000)^18` at `60` digits on arbitrary noncommuting complex Yukawas, with `3`-loop CP-odd trace invariant $K_1^3 |\operatorname{Im}\operatorname{Tr}([H_1, H_2]^3)| < (1/1000)^6$)?
   - Consequently, on a **single `3`-family chiral sector** (`no light mirror doubling`) with Left–Right $\mathbb{Z}_2^D$ Hermitian UV boundary $Y_1^{\mathrm{UV}} = (Y_1^{\mathrm{UV}})^\dagger,\, Y_2^{\mathrm{UV}} = (Y_2^{\mathrm{UV}})^\dagger$ and $\operatorname{sgn}\det(Y_1^{\mathrm{UV}} Y_2^{\mathrm{UV}}) = +1$, does repaired `BPV` `2`-loop evolution preserve $|\bar{\theta}_{\mathrm{phys}}(\mathrm{IR})| < (1/1000)^8$ rad (`even as (Y_1, Y_2) depart from Hermiticity by > 1/1000`) while simultaneously maintaining `3`-family CP violation $|J_{12}| > 1/1000$ and `10`-trial `24`-digit full $\mathrm{U}(3)^6$ Fujikawa anomaly invariance `< (1/1000)^6` rad?

---

## 2. Deliverables and Definition of Done

1. **`Part 2A`:** Proof that $\operatorname{rank}(A_a) = 1$ while $\operatorname{rank}(A_v + A_w + A_u) = 3$; computation of the symmetric Löwdin–Petersson orthonormal triad $G_{\mathrm{Pet}}^{-1/2}(A_v, A_w, A_u)$ (`<E_a, E_b>_Pet = delta_{a b}`) and parameter-free geometric Serre prescription; side-by-side `sec4` IR comparison + `UR-7` `CRT` invariance check.
2. **`Part 2B`:** `55`-digit target-free `m004` `(L, R)` complex-volume / Chern–Simons cancellation check (`0` vs `pi` parity-branch separation); `60`-digit + symbolic verification of `1+2`-loop `BPV` determinant-phase conservation; and `35`-digit repaired-`BPV` `2`-loop `3`-family $D$-parity trajectory + `10`-trial `24`-digit full $\mathrm{U}(3)^6$ Fujikawa check + parity-even vs parity-broken heavy-mirror Schur-complement decoupling audit.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_LowdinPetersson_and_JetRank_Gate` (`Part 2A`):** Individual basis tensors have rank `1` (`sv_2/sv_3 < (1/1000)^15`) and any `2`-jet sum has rank `2` (`sv_1/sv_3 < (1/1000)^15`) while `3`-jet `A_v + A_w + A_u` has full rank `3`; $(A_w, A_u)$ Petersson cosine exceeds `98/100`; Löwdin–Petersson orthonormalized operators satisfy $\|\langle \hat{E}_a, \hat{E}_b \rangle_{\mathrm{Pet}} - \delta_{a b}\|_F < (1/1000)^4$ (`Y_cut = 45 vs 60 < (1/1000)^4`, lifting `sec4_r23 > 1/10` and `sec4_r12 > 7/10` vs hierarchical `sec4_r23 < 2/1000` on `(1, 1, 1)` and geometric `4*pi` curvature scaling), with `UR-7` `CRT` `6w mod 1` invariance `< (1/1000)^3` across all `4` parameter-free prescriptions.
2. **`E2_AmphichiralCS_and_3FamilyDParity_StrongCP_Gate` (`Part 2B`):** Target-free `m004` `(L, R)` Chern–Simons / imaginary-volume asymmetry vanishes to `< (1/1000)^15`; `60`-digit `1+2`-loop `BPV` $\operatorname{Im}\operatorname{Tr}(Y_1^{-1}\beta_{Y_1} + Y_2^{-1}\beta_{Y_2})$ vanishes to `< (1/1000)^18` on generic complex noncommuting matrices; `3`-family $D$-parity Hermitian UV state evolved with repaired `BPV` `2`-loop `RGE` satisfies $|\bar{\theta}_{\mathrm{phys}}(\mathrm{IR})| < (1/1000)^8$ rad, non-Hermiticity departure `> 1/1000`, $|J_{12}(\mathrm{IR})| > 1/1000$, and `10`-trial `24`-digit full $\mathrm{U}(3)^6$ Fujikawa invariance `< (1/1000)^6` rad (`and parity-symmetric heavy mirror decoupling preserves |theta_bar| < (1/1000)^5 rad`).

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage2_Unify_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside target-free geometry functions.
2. **`PC_U2_SingleOrTwoJetSingularMajorana`:** Dropping any one of $(A_v, A_w, A_u)$ drops $\operatorname{rank}(M_R)$ to `\le 2` (`smallest singular value < (1/1000)^15`).
3. **`PC_U2_ParityPiBranchAndNegativeDetSign`:** Setting the parity-allowed branch $\theta_{\mathrm{YM}} = \pi$ or $\operatorname{sgn}\det(Y_1^{\mathrm{UV}} Y_2^{\mathrm{UV}}) = -1$ yields $|\bar{\theta}_{\mathrm{phys}}| = \pi > 3$ rad (`confirming physical ca500dad6 Intake Point 2`).
4. **`PC_U2_OmitFujikawaShiftAndAsymmetricMirrorDecoupling`:** Omitting the $\mathrm{U}(3)^6$ Fujikawa shift fails by `> 1/2` rad, and introducing parity-breaking complex mirror mass mixing shifts light `3`-family $|\bar{\theta}_{\mathrm{phys}}|$ by `> 1/10` rad.

`0 of 19.`
