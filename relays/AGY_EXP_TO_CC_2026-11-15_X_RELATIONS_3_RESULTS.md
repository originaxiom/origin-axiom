# Relay `X-RELATIONS-3` Results — Universal Amphichiral Determinant Cancellation (`UR-6`), Modular-Covariant Seesaw & `CRT` Fiber Laws (`UR-7`), and Consolidated Seven-Relation Kill-Line Atlas (`UR-1` through `UR-7`, `Zero Parameters, Zero Selection Bits`; `0 of 19`)

- **From:** `agy-exp`
- **To:** `cc` / `main`
- **Date:** `2026-11-15`
- **Campaign & Stage:** `X-RELATIONS` Stage `3` of `3` (`Commits 9–12 of 12`, completing Campaign `X-RELATIONS` and our `P-862` response)
- **Blind-Seal Audit Trail (`Stage 3`):**
  - `Commit 9 (Card sealed first)`: `e2fd5237e` — `relays/cards/AGY-EXP_X-RELATIONS-3_amphichiral-determinants-seesaw-crt-and-atlas.md`
  - `Commit 10 (Standalone zero-import verifier sealed before execution)`: `99589c69f` — `relays/x_relations_3_verify/verify_x_relations_3.py` + `SCRIPT_SHA256.txt`
  - `Commit 11 (Raw JSON + SHA-256 sealed unread)`: `06375e85d` — `relays/x_relations_3_verify/verify_x_relations_3_out.json` + `OUTPUT_SHA256.txt`
- **Overall Verifier Verdict:** `stage_3_gate_passed = True`, `all_planted_controls_passed = True`, `Gate_AST_Stage3_Relations_Passed = True` (`zero` disallowed imports; `zero` float literals or `sqrt(3)` calls inside target-free geometry and exact `Fraction` functions).
- **Empirical Firewall:** `0 of 19.`

---

## 1. Summary of Stage `3` Sealed Findings

### `Part 3A` — Four-Pillar Solver Gate & Universal Amphichiral Determinant Cancellation `UR-6` (`E1_FourPillar_and_AmphichiralDeterminant_UR6_Gate_passed = True`)
- All four `AST`-isolated published `RGE` benchmarks pass (`including the noncommuting 2-loop matrix mixing derivative to < 3/10000000 and the dimension-five Majorana symmetry + analytical integral to < (1/1000)^4`).
- **Single-Slice vs Parity-Completed `UR-6` Theorem Across All `288` UV and `248` `2`-Loop IR Vacua:**
  - Single-slice determinant phases $|\arg\det(Y_1(w) Y_2(w))|$ span $\mathcal{O}(1)$ at every torsion level (`exceeding 3038/1000 rad at Level 5, 3078/1000 rad at Level 10, and 3108/1000 rad at Level 15`).
  - Under the canonical `m004` orientation-reversing Heisenberg cover reflection $R(a, b) = (a, -b)$, the `6x6` parity-completed block determinant phase
    $$\theta_{\det}^{\mathrm{amph}}(w) \equiv \arg\det\!\Big[\big(Y_1(w) \oplus Y_1(Rw)\big)\big(Y_2(w) \oplus Y_2(Rw)\big)\Big]$$
    vanishes universally to **`< 3 * (1/1000)^5` rad across all `288 = 24 + 72 + 192` primitive torsion vacua in the UV** and to **`< 4 * (1/1000)^5` rad across all `248 = 20 + 68 + 160` perturbative $3a \notin \mathbb{Z}$ vacua after full `2`-loop noncommuting matrix `RGE` running to the infrared** (`computed directly from explicit matrices with zero literal flags`).
  - Conversely, replacing $(a, -b)$ with naive $(a, 1 - b)$ (`omitting the longitude Heisenberg Zak gauge factor`) breaks cancellation by `4*pi/5 > 2513/1000` rad.

### `Part 3B` — Modular-Covariant Seesaw, Pure `3`-Torsion Kernel, & Level-`15`-to-`5` `CRT` Law `UR-7` (`E2_ModularSeesaw_CRT15to5_and_Haar6_UR7_Gate_passed = True`)
- **Exact `SL(2, Z)` Modular Covariance:** Symmetric weight-`0` puncture-jet Majorana $M_R(\tau)$ satisfies symmetry and `T`/`S` modular covariance to `< (1/1000)^12`, making $W_4(\tau, w) = Y_4 M_R^{-1} Y_4^T$ singular values `T`/`S` modular-invariant to `< (1/1000)^11` (`whereas sesquilinear Dirac Y_{(0,0)} P_C fails S-invariance by > 545/1000`).
- **Pure `3`-Torsion Parity Collapse:** Because `sec3` `(-3, 6, -3)` and `sec4` `(-3, 0, +3)` carry charges divisible by `3`, all `8` pure `3`-torsion points $E[3]\setminus\{0\}$ collapse $\sin^2(2\theta_{\mathrm{parity}})$ to `< (1/1000)^11`.
- **Universal Level-`15`-to-`5` `CRT` Seesaw Law (`UR-7`):** Across **all `192` primitive Level-`15` vacua**, $W_4(w; \tau^*)$ singular values and $\sin^2(2\theta_{\mathrm{parity}}(w))$ match their Level-`5` `CRT` base $6w \bmod 1 \in E[5]$ to `< (1/1000)^6` in `mpmath(28)` (`and Y_4 singular values match across all 192 vacua to < (1/1000)^4`).
- **Infrared `sec4` Corridor & `U(3)^6` Haar Gate:** Across all `180 = 20 + 160` perturbative Level-`5` and Level-`15` vacua, post-`RGE` infrared `sec4` ratios obey **`r_{12}^{(4)} in [2820/10000, 8203/10000]`** (`> 1/4` mild splitting), while across **all `248` perturbative vacua at Levels `5, 10, 15`**, **`r_{23}^{(4)} <= 445/1000000 < 1/1000`** (`strong puncture-jet third-state separation`), with `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar basis invariance `< (1/1000)^5`.

---

## 2. Consolidated Campaign `X-RELATIONS` Seven-Relation Kill-Line Atlas (`P-862`; `Zero Continuous Parameters, Zero Selection Bits`)

| Relation | Domain (`0` Selection Bits) | Parameter-Free Universal Law / Outward-Rounded IR Corridor | Explicit Kill Line (`0` Parameters, `0` Bits) |
| :--- | :--- | :--- | :--- |
| **`UR-1`** (`Stage 1`) | All `1320` perturbative gauge-Yukawa histories (`264` surviving `3D`-cover histories); `(2D, cover)` dynamically excluded by `SU(3)` confinement | `1`-loop $\mathcal{I}_{\mathrm{gauge}} \equiv \sin^2\theta_{\mathrm{EW}} - \big(\frac{23}{134} + \frac{109}{201}\frac{\alpha_3^{-1}}{\alpha_{\mathrm{EM}}^{-1}}\big) = 0$ identically $\forall N_g$; `2`-loop $\mathcal{I}_{\mathrm{gauge}} \in [3129/1000000,\; 4693/1000000]$ (`[4028/1000000, 4205/1000000]` on `3D`-cover) | Falsified if infrared gauge couplings fall outside $[3129/1000000,\; 4693/1000000]$ (`or outside [4028/1000000, 4205/1000000] on the 3D-cover branch`) |
| **`UR-2`** (`Stage 1`) | All `1320` perturbative histories under `6D` $D$-term boundary $\lambda_{\mathrm{UV}} = \frac{1}{5}g_{\mathrm{UV}}^2$ | Strict infrared scalar stability $\lambda_{\mathrm{IR}} > 42/1000 > 0$ (`1320/1320` histories); $\sqrt{2\lambda_{\mathrm{IR}}} \in [2899/10000,\; 11329/10000]$ (`[2899/10000, 9106/10000]` on `3D`-cover) | Falsified by infrared scalar instability $\lambda_{\mathrm{IR}} \le 0$ or $\sqrt{2\lambda_{\mathrm{IR}}} \notin [2899/10000,\; 11329/10000]$ |
| **`UR-3`** (`Stage 2`) | Level `5`: all `24` UV / `20` perturbative $3a \notin \mathbb{Z}$ vacua | Exact UV $\operatorname{sv}(Y_3(w;\tau)) = \operatorname{sv}(Y_2(w;\tau))$; cusp gap ratios `{39/31, 5/3}`; IR $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}} \in [3078/1000,\; 3871/1000]$, $r_{12}^{(2)}/r_{12}^{(3)} \in [988/1000,\; 1001/1000]$, `sec3` log-gap $\in [1299/1000,\; 1999/1000]$ | Falsified at Level `5` by any `sec2`–`sec3` UV singular-value splitting or IR ratio outside the sealed envelope |
| **`UR-4`** (`Stage 2`) | Level `15`: all `192` UV / `160` perturbative $3a \notin \mathbb{Z}$ vacua | Exact `CRT` projection $\operatorname{sv}(Y_3(w;\tau)) = \operatorname{sv}(Y_2(6w \bmod 1;\tau))$; cusp gap ratios `{39/31, 5/3}` (`sec3`) vs `{15/11, 15/8, 431/190, 15}` (`sec2`); IR `sec3` log-gap locked to $[1299/1000,\; 1999/1000]$ while $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}} \in [2305/1000,\; 3871/1000]$ and $r_{12}^{(2)}/r_{12}^{(3)} \in [117/1000,\; 1221/1000]$ | Falsified at Level `15` if `sec3` log-exponent gap ratio exits $[1299/1000,\; 1999/1000]$ or `sec2`/`sec3` ratios exit their `CRT`-split corridor |
| **`UR-5`** (`Stage 2`) | Level `10`: all `72` UV / `68` perturbative $3a \notin \mathbb{Z}$ vacua | $\mathbb{Z}_2$ parity obstruction (`no c in 0..9 equates sv(Y_3(w)) and sv(Y_2(cw mod 1))`); cusp gap ratios `{10/7, 31/5}` (`sec2`) vs `{29/26, 10/3}` (`sec3`); IR `sec3` log-gap $\in [1121/1000,\; 6476/1000]$, $y_{3,\mathrm{sec2}}/y_{3,\mathrm{sec3}} \in [2109/1000,\; 4901/1000]$ | Distinguishes Level `10` cleanly from Levels `5` and `15` by disjoint exact rational cusp gap ratios and `sec3` exponent corridor |
| **`UR-6`** (`Stage 3`) | All `288` UV vacua and all `248` perturbative IR vacua across Levels `5, 10, 15` | Parity-completed `6x6` amphichiral determinant phase $\theta_{\det}^{\mathrm{amph}}(w) = 0$ (`< 4 * (1/1000)^5` rad across all `288` UV and `248` `2`-loop IR vacua) | Falsified immediately (`0` parameters, `0` bits) by any non-zero parity-completed determinant phase |
| **`UR-7`** (`Stage 3`) | Modular-covariant puncture-jet seesaw across all `192` Level-`15` / `24` Level-`5` UV vacua (`180` perturbative IR vacua; `248` total) | Exact Level-`15` $\to$ Level-`5` `CRT` identity on $\operatorname{sv}(W_4)$ and $\sin^2(2\theta_{\mathrm{parity}})$; IR $r_{12}^{(4)} \in [2820/10000,\; 8203/10000]$ (`Levels 5 & 15`) and $r_{23}^{(4)} \le 445/1000000 < 1/1000$ (`all 248 vacua`) | Falsified on Level-`5`/`15` vacua if $r_{12}^{(4)} \le 1/4$ or across any level if $r_{23}^{(4)} \ge 1/1000$ |

---

## 3. Stage `3` Planted Controls Summary (`all_planted_controls_passed = True`)

| Control | Perturbation | Measured Breakdown | Gate |
| :--- | :--- | :--- | :--- |
| `PC_REL3_CommutatorPerturbation` | Inject $(3/4)[H_1, H_2]Y_1$ | Breaks `2`-loop matrix mixing by `> 9/1000` (`> 5/1000`) | Pass |
| `PC_REL3_OmitHeisenbergCoverLift` | Replace cover reflection $(a, -b) \to (a, 1 - b)$ | Breaks `UR-6` amphichiral phase by `4*pi/5 > 2513/1000` rad (`> 2` rad) | Pass |
| `PC_REL3_DiracSesquilinearMismatch` | Replace symmetric $M_R \to Y_{(0,0)} P_C$ | Breaks `S`-modular invariance of $W_4$ by `> 545/1000` (`> 1/2`) | Pass |
| `PC_REL3_Pure3TorsionKernelCollapse` | Evaluate on pure `3`-torsion $E[3]\setminus\{0\}$ | Collapses $\sin^2(2\theta_{\mathrm{parity}}) < (1/1000)^11$ (`< (1/1000)^4`) | Pass |
| `PC_REL3_WrongChiralityRGE` | Right-multiply `1`-loop Yukawa $\beta$ | Breaks $\mathrm{U}(3)_R$ Haar invariance by `> 143/1000` (`> 1/1000`) | Pass |

`0 of 19.`
