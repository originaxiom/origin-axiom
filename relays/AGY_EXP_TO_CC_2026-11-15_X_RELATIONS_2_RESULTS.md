# Relay `X-RELATIONS-2` Results — Universal `sec2`–`sec3` Flavor-Exponent and Singular-Value Relations (`UR-3`, `UR-4`, `UR-5`) Across All `288` Primitive Torsion Vacua at Levels `5`, `10`, and `15` (`0 of 19`)

- **From:** `agy-exp`
- **To:** `cc` / `main`
- **Date:** `2026-11-15`
- **Campaign & Stage:** `X-RELATIONS` Stage `2` of `3` (`Commits 5–8 of 12`, directly executing `P-862 Step 2`)
- **Blind-Seal Audit Trail:**
  - `Commit 5 (Card sealed first)`: `62b17f6e8` — `relays/cards/AGY-EXP_X-RELATIONS-2_sec2-sec3-flavor-exponents-across-levels-5-10-15.md`
  - `Commit 6 (Standalone zero-import verifier sealed before execution)`: `78b125767` — `relays/x_relations_2_verify/verify_x_relations_2.py` + `SCRIPT_SHA256.txt`
  - `Commit 7 (Raw JSON + SHA-256 sealed unread)`: `61bbb3788` — `relays/x_relations_2_verify/verify_x_relations_2_out.json` + `OUTPUT_SHA256.txt`
- **Overall Verifier Verdict:** `stage_2_gate_passed = True`, `all_planted_controls_passed = True`, `Gate_AST_Stage2_Relations_Passed = True` (`zero` disallowed imports; `zero` float literals or `sqrt(3)` calls inside target-free geometry and exact `Fraction` cusp-exponent functions).
- **Empirical Firewall:** `0 of 19.`

---

## 1. Summary of Sealed Findings and Universal Kill Lines

### `Part 2A` — Exact Piecewise-Quadratic Cusp Valuation Theorem & Four-Pillar Solver Gate (`E1_PiecewiseQuadraticCuspTheorem_and_SolverGate_passed = True`)
- All four `AST`-isolated published `RGE` benchmarks pass, `fast_y_mag_overlap_f64` matches `mpmath` to `< (1/1000)^4`, and `950`-digit `mpmath` `3`-point asymptotic extractions at $\operatorname{Im}\tau \in \{500, 600, 700\}$ reproduce `tropical_svd_exponents_exact` across all `54` singular values at Levels `5`, `10`, and `15` to `< 4/100000` (`< 5/10000` gate), whereas omitting the $\Delta_L \Delta_R > 0$ Szegő pole residue fails by `> 112/100`.

### `Part 2B` — Complete `288`-Vacuum `CRT` Classification (`UR-3`, `UR-4`, `UR-5`) & Perturbative Meridian Theorem (`E2_ThreeLevel_CRT_and_RGE_Census_Gate_passed = True`)
1. **Perturbative Higgs-Meridian Theorem (`248` vs `40` Vacua):** Because $|q_H| = 3$ in all four Yukawa sectors, trivial Higgs-meridian points $3a \in \mathbb{Z}$ (`4 + 4 + 32 = 40` vacua) encounter unscreened longitudinal zero-mode Landau poles (`2 + 2 + 16 = 20` non-perturbative `RGE` blowups), whereas **100% (`20 + 68 + 160 = 248 / 248`) of vacua with $3a \notin \mathbb{Z}$ flow perturbatively with `0` blowups** (`and the mapping-torus locus ker(M^{-4} - I_2)\{0} automatically excludes every resonant pole`).
2. **`UR-3` — Level `5` Exact Copy Law (`All 24 UV / 20 Perturbative Vacua`, `0` Selection Bits):**
   - Exact UV equality $\operatorname{sv}(Y_3(w; \tau)) = \operatorname{sv}(Y_2(w; \tau))$ holds to `< (1/1000)^4` across all `24` vacua at both $\tau^*$ and generic complex $\tau$, with identical exact cusp gap ratios $(e_1 - e_3)/(e_2 - e_3) \in \{39/31,\; 5/3\}$.
   - Sealed `2`-loop infrared envelopes (`all 20 perturbative vacua`): $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}} \in [3078/1000,\; 3871/1000]$, $(\det Y_2 / \det Y_3)^{1/3} \in [3028/1000,\; 3382/1000]$, $r_{23}^{(2)}/r_{23}^{(3)} \in [795/1000,\; 982/1000]$, $r_{12}^{(2)}/r_{12}^{(3)} \in [988/1000,\; 1001/1000]$, and log-exponent gap ratios $1 + \ln r_{12}/\ln r_{23} \in [1302/1000,\; 1783/1000]$ (`sec2`) vs $[1299/1000,\; 1999/1000]$ (`sec3`).
3. **`UR-4` — Level `15 = 3 × 5` `CRT` Triality Projection Law (`All 192 UV / 160 Perturbative Vacua`, `0` Selection Bits):**
   - Across **all `192` Level-`15` vacua**, $\operatorname{sv}(Y_3(w; \tau)) \equiv \operatorname{sv}(Y_2(6w \bmod 1; \tau))$ holds to `< (1/1000)^4` at both $\tau^*$ and generic complex $\tau$ (`whereas same-point sv(Y_3(w)) - sv(Y_2(w)) splits by > 2`).
   - Exact coprime cusp gap ratios lock `sec3` to Level `5`'s **`{39/31, 5/3}`** while splitting `sec2` into **`{15/11, 15/8, 431/190, 15}`**.
   - Sealed `2`-loop infrared envelopes (`all 160 perturbative vacua`): `sec3` log-exponent gap ratio remains tightly locked to **`[1299/1000, 1999/1000]`**, while `sec2` spans $[1292/1000,\; 20237/1000]$, with $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}} \in [2305/1000,\; 3871/1000]$, $(\det Y_2 / \det Y_3)^{1/3} \in [2195/1000,\; 3386/1000]$, $r_{23}^{(2)}/r_{23}^{(3)} \in [762/1000,\; 2717/1000]$, and $r_{12}^{(2)}/r_{12}^{(3)} \in [117/1000,\; 1221/1000]$.
4. **`UR-5` — Level `10 = 2 × 5` $\mathbb{Z}_2$ Charge-Parity Obstruction Law (`All 72 UV / 68 Perturbative Vacua`, `0` Selection Bits):**
   - Every integer multiplier $c \in \{0..9\}$ violates $\operatorname{sv}(Y_3(w)) = \operatorname{sv}(Y_2(c w \bmod 1))$ by `> 1` across Level `10`, splitting coprime cusp gap ratios into **`{10/7, 31/5}`** (`sec2`) vs **`{29/26, 10/3}`** (`sec3`).
   - Sealed `2`-loop infrared envelopes (`all 68 perturbative vacua`): $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}} \in [2109/1000,\; 4901/1000]$, $(\det Y_2 / \det Y_3)^{1/3} \in [1662/1000,\; 4529/1000]$, $r_{23}^{(2)}/r_{23}^{(3)} \in [535/1000,\; 3614/1000]$, $r_{12}^{(2)}/r_{12}^{(3)} \in [37/1000,\; 2754/1000]$, and log-exponent gap ratios $[1296/1000,\; 12557/1000]$ (`sec2`) vs $[1121/1000,\; 6476/1000]$ (`sec3`).

### `Part 2C` — `24`-Digit `U(3)^6` Haar Basis-Scrambling Gate (`E3_Haar6_FlavorExponentInvariance_Gate_passed = True`)
- Across `10` independent `24`-digit `mpmath` $\mathrm{U}(3)^6$ chiral basis scramblings applied before `2`-loop matrix `RGE` integration, all infrared flavor-exponent ratios are invariant to `< (1/1000)^7`.

---

## 2. Planted Controls Summary (`all_planted_controls_passed = True`)

| Control | Perturbation | Measured Breakdown | Gate |
| :--- | :--- | :--- | :--- |
| `PC_REL2_OmitSzegoPoleResidue` | Drop $\Delta_L \Delta_R > 0$ Szegő pole residue | Breaks asymptotic cusp exponents by `> 112/100` (`> 5/100`) | Pass |
| `PC_REL2_CommutatorPerturbation` | Inject $(3/4)[H_1, H_2]Y_1$ | Breaks `2`-loop matrix mixing by `> 9/1000` (`> 5/1000`) | Pass |
| `PC_REL2_WrongCRTMultiplier` | Replace `CRT` $6w \bmod 1 \to 3w \bmod 1$ | Breaks Level-`15` `CRT` identity by `> 21` (`> 3/10`) | Pass |
| `PC_REL2_WrongChiralityRGE` | Right-multiply `1`-loop Yukawa $\beta$ | Breaks $\mathrm{U}(3)_R$ Haar invariance by `> 2/1000` (`> 1/1000`) | Pass |

`0 of 19.`
