# Card `X-RELATIONS-2` — Universal `sec2`–`sec3` Flavor-Exponent and Singular-Value Relations Across All `288` Primitive Torsion Vacua at Levels `5`, `10`, and `15` (`Exact Piecewise-Quadratic Cusp Valuation Theorem, Complete Chinese-Remainder Classification UR-3/UR-4/UR-5, Perturbative Meridian Theorem, and Explicit Kill Lines`; `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Second sealed stage of Campaign `X-RELATIONS` (`three stages, twelve blind-sealed commits, 0 of 19`, directly executing `P-862 Step 2`). Derives data-free and seals the exact analytical cusp-exponent theorem and complete Chinese-Remainder Theorem (`CRT`) singular-value and `2`-loop infrared relations between `sec2` (`charges (1, 2, -3)`) and `sec3` (`charges (-3, 6, -3)`) across **every** primitive torsion vacuum at Level `5` (`24` vacua), Level `10` (`72` vacua), and Level `15` (`192` vacua) — `288` vacua in total, with **zero** continuous parameters and **zero** vacuum-selection bits within each level.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_relations_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; published `RGE` solver benchmark constants are strictly `AST`-isolated inside the solver-verification function.

---

## 1. The Package and the Questions

1. **Question `2A` (`Exact Piecewise-Quadratic Cusp Valuation Theorem & Four-Pillar RGE Solver Gate`):**
   - As $\operatorname{Im}\tau = y \to +\infty$, does each entry $|Y_{ij}(i y)| \sim y^p \exp(-\pi y E_{ij})$ obey the exact rational (`zero-float`) piecewise-quadratic cusp valuation law:
     $$E_{ij} = \min_{(l_1, l_2) \in \mathbb{Z}^2} \begin{cases} 3\,\big|\Delta_L^2 - \Delta_R^2\big|, & \Delta_L \Delta_R > 0 \;\text{(meromorphic Szeg\H{o} pole residue)}, \\ 3\,\big(\Delta_L^2 + \Delta_R^2\big), & \Delta_L \Delta_R \le 0 \;\text{(Gaussian boundary saddle)}, \end{cases}$$
     where $\Delta_L = \frac{2i + 1 + 2 q_L a}{6} - l_1$ and $\Delta_R = \frac{2j + 1 - 2 q_R a}{6} - l_2$, and do the resulting exact tropical singular-value exponents $(e_1 \ge e_2 \ge e_3)$ agree with `65`-digit `mpmath` `3`-point asymptotic extractions across Levels `5`, `10`, and `15` to `< 5/10000`?
2. **Question `2B` (`Complete CRT Classification UR-3 / UR-4 / UR-5 Across All 288 Vacua & Perturbative Higgs-Meridian Theorem`):**
   - **Level `5` (`all 24 primitive vacua`, `UR-3`):** Because $(q_R^{(3)}, q_L^{(3)}) = (6, -3) \equiv (1, 2) = (q_L^{(2)}, q_R^{(2)}) \pmod 5$, does $\operatorname{sv}(Y_3(w; \tau)) = \operatorname{sv}(Y_2(w; \tau))$ hold **identically** (`< (1/1000)^4`) across all `24` vacua at both $\tau^*$ and generic complex $\tau = 3/7 + i\operatorname{Im}\tau^*$, locking both sectors to the exact cusp gap ratios $(e_1 - e_3)/(e_2 - e_3) \in \{39/31,\; 5/3\}$?
   - **Level `15 = 3 × 5` (`all 192 primitive vacua`, `UR-4`):** Because `sec3` hypercharges vanish $\pmod 3$ while `sec2` carries $\mathbb{Z}_3$ triality, does the `CRT` projector $6 \equiv 0 \pmod 3,\; 6 \equiv 1 \pmod 5$ enforce the exact identity
     $$\operatorname{sv}\!\big(Y_3(w;\, \tau)\big) \equiv \operatorname{sv}\!\big(Y_2(6w \bmod 1;\, \tau)\big)$$
     across **all `192` primitive Level-`15` vacua** at both $\tau^*$ and generic complex $\tau$, locking `sec3` cusp gap ratios to `{39/31, 5/3}` while splitting `sec2` into `{15/11, 15/8, 431/190, 15}`?
   - **Level `10 = 2 × 5` (`all 72 primitive vacua`, `UR-5`):** Does $\mathbb{Z}_2$ charge-parity obstruct any integer multiplier $c \in \{0..9\}$ from equating $\operatorname{sv}(Y_3(w))$ and $\operatorname{sv}(Y_2(c w \bmod 1))$ (`error > 3/10` for every $c$), splitting `sec2` and `sec3` into paired cusp gap ratios `{10/7, 31/5}` vs `{29/26, 10/3}`?
   - **Perturbative Higgs-Meridian Theorem (`248` vs `40` Vacua):** Because $|q_H| = 3$ in every sector, do trivial-meridian points $3a \in \mathbb{Z}$ (`4 + 4 + 32 = 40` vacua) hit resonant longitudinal zero-mode Landau poles (`2 + 2 + 16 = 20` non-perturbative `RGE` blowups), whereas **all `20 + 68 + 160 = 248` Higgs-meridian-active vacua ($3a \notin \mathbb{Z}$) flow perturbatively with `0` blowups**, sealing exact infrared `sec2`/`sec3` envelopes at each level?
3. **Question `2C` (`Post-RGE U(3)^6 Haar Basis Invariance of Flavor-Exponent Ratios`):**
   - Are the infrared flavor-exponent gap ratios $1 + \ln(r_{12})/\ln(r_{23})$ and inter-sector ratio $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}}$ invariant to `< (1/1000)^4` under `10` random `24`-digit $\mathrm{U}(3)^6$ chiral basis scramblings applied prior to `2`-loop matrix `RGE` evolution?

---

## 2. Deliverables and Definition of Done

1. **`Part 2A` (`Four-Pillar Solver Gate + Two-Route Cusp Exponent Proof`):** Pass all `4` published `RGE` checks, verify `fast_y_mag_overlap_f64` vs `mpmath` to `< (1/1000)^4`, and verify exact `Fraction` cusp exponents against `65`-digit `mpmath` `3`-point asymptotic extractions (`< 5/10000`).
2. **`Part 2B` (`Complete 288-Point CRT & 2-Loop RGE Census`):** Verify `UR-3` (`Level 5`, `24` vacua), `UR-4` (`Level 15`, `192` vacua), and `UR-5` (`Level 10`, `72` vacua) in the UV and seal exact `2`-loop infrared envelopes across all `248 = 20 + 68 + 160` perturbative $3a \notin \mathbb{Z}$ vacua.
3. **`Part 2C` (`24-Digit U(3)^6 Haar Gate`):** Verify `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance of post-`RGE` flavor-exponent ratios to `< (1/1000)^4`.

---

## 3. Pre-Registered Expectations and Falsification Criteria (Explicit Kill Lines)

1. **`E1_PiecewiseQuadraticCuspTheorem_and_SolverGate` (`Part 2A`):** All `4` published `RGE` solver checks pass, `f64` vs `mpmath` overlap error is `< (1/1000)^4`, and `65`-digit asymptotic singular-value slopes match `tropical_svd_exponents_exact` to `< 5/10000`.
2. **`E2_ThreeLevel_CRT_and_RGE_Census_Gate` (`Part 2B`, `UR-3 / UR-4 / UR-5 Kill Lines`):**
   - Exact UV `CRT` laws hold to `< (1/1000)^4` across all `24` Level-`5` vacua (`sv(Y_3(w)) = sv(Y_2(w))`) and all `192` Level-`15` vacua (`sv(Y_3(w)) = sv(Y_2(6w mod 1))`), while Level `10` (`72` vacua) violates `sv(Y_3(w)) = sv(Y_2(cw mod 1))` by `> 3/10` for every $c \in \{0..9\}$.
   - Exact coprime cusp gap-ratio sets equal `{39/31, 5/3}` (`Level 5 sec2 & sec3, and Level 15 sec3`), `{15/11, 15/8, 431/190, 15}` (`Level 15 sec2`), and `{10/7, 31/5}` vs `{29/26, 10/3}` (`Level 10 sec2 vs sec3`).
   - Across all `248 = 20 + 68 + 160` vacua with $3a \notin \mathbb{Z}$, `0` `RGE` Landau blowups occur (`whereas 2 + 2 + 16 = 20 blowups occur on trivial-meridian 3a in Z points`), sealing level-wide zero-selection-bit infrared kill-line envelopes for `sec2`/`sec3` mass and log-exponent ratios.
3. **`E3_Haar6_FlavorExponentInvariance_Gate` (`Part 2C`):** `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar basis scrambling leaves post-`RGE` infrared flavor-exponent ratios invariant to `< (1/1000)^4`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage2_Relations_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside all target-free geometry and exact `Fraction` cusp-exponent functions.
2. **`PC_REL2_OmitSzegoPoleResidue`:** Omitting the $\Delta_L \Delta_R > 0$ Szegő pole residue (`using Gaussian 3(Delta_L^2 + Delta_R^2) everywhere`) breaks `65`-digit asymptotic cusp exponents by `> 5/100`.
3. **`PC_REL2_CommutatorPerturbation`:** Injecting $\delta\beta_{Y_1} = (3/4)[H_1, H_2]Y_1$ breaks the noncommuting `2`-loop matrix mixing derivative by `> 5/1000`.
4. **`PC_REL2_WrongCRTMultiplier`:** Replacing the `CRT` projector $6w \bmod 1$ by $3w \bmod 1$ at Level `15` breaks $\operatorname{sv}(Y_3(w)) = \operatorname{sv}(Y_2(c w))$ by `> 3/10`.
5. **`PC_REL2_WrongChiralityRGE`:** Right-multiplying `1`-loop matrix Yukawa $\beta$-functions breaks right-handed $\mathrm{U}(3)_R$ Haar invariance (`error > 1/1000`).

`0 of 19.`
