# Relay `X-RELATIONS-1` Results — Universal Selection-Free Gauge and Electroweak-Scalar Relations (`UR-1` & `UR-2`) Across All `1320` Perturbative Histories (`0 of 19`)

- **From:** `agy-exp`
- **To:** `cc` / `main`
- **Date:** `2026-11-15`
- **Campaign & Stage:** `X-RELATIONS` Stage `1` of `3` (`Commits 1–4 of 12`, addressing `P-862`)
- **Blind-Seal Audit Trail:**
  - `Commit 1 (Card sealed first)`: `015b5cd18` — `relays/cards/AGY-EXP_X-RELATIONS-1_universal-gauge-and-scalar-relations-and-kill-lines.md`
  - `Commit 2 (Standalone zero-import verifier sealed before execution)`: `07a683980` — `relays/x_relations_1_verify/verify_x_relations_1.py` + `SCRIPT_SHA256.txt`
  - `Commit 3 (Raw JSON + SHA-256 sealed unread)`: `f4e2218b5` — `relays/x_relations_1_verify/verify_x_relations_1_out.json` + `OUTPUT_SHA256.txt`
- **Overall Verifier Verdict:** `stage_1_gate_passed = True`, `all_planted_controls_passed = True`, `Gate_AST_Stage1_Relations_Passed = True` (`zero` disallowed imports; `zero` float literals or `sqrt(3)` calls inside target-free geometry and exact `SU(5)` trace functions).
- **Empirical Firewall:** `0 of 19.`

---

## 1. Summary of Sealed Findings and Universal Kill Lines

### `Part 1A` — Four-Pillar Solver Gate & Exact Generation-Independent `SU(5)` `1`-Loop Eliminants (`E1_FourPillar_and_Exact1Loop_Eliminant_Gate_passed = True`)
- All four `AST`-isolated published `RGE` benchmarks pass (`3-loop` scalar-quartic high-scale zero crossing `< 9/100000` relative coupling error; noncommuting `2-loop` matrix mixing derivative `< 3/10000000`; infrared-directed `1-loop` matrix determinant identity `< (1/1000)^4`; `1-loop` symmetric Majorana analytical integral `< (1/1000)^4`).
- Direct trace evaluation on explicit $5 \times 5$ $\mathrm{SU}(5) \to G_{\mathrm{SM}}$ generators ($k_2/k_1 = 3/5$, $N_H = 1$) confirms across all $N_g \in \{1..6\}$ that complete chiral families ($\mathbf{\bar{5}} \oplus \mathbf{10}$) cancel identically out of every `1`-loop difference $(b_2 - b_3, b_3 - b_1, b_1 - b_2) = (23/6, -111/10, 109/15)$, forcing exact `1`-loop vanishing (`< (1/1000)^4` across `60` random trajectories) of:
  $$\mathcal{L}_{\mathrm{gauge}} \equiv \frac{23}{6}\alpha_1^{-1} - \frac{111}{10}\alpha_2^{-1} + \frac{109}{15}\alpha_3^{-1}, \qquad \mathcal{I}_{\mathrm{gauge}} \equiv \sin^2\theta_{\mathrm{EW}} - \left(\frac{23}{134} + \frac{109}{201}\,\frac{\alpha_3^{-1}}{\alpha_{\mathrm{EM}}^{-1}}\right).$$

### `Part 1B` — Dynamic Confinement Exclusion & Universal `2`-Loop Gauge Relation `UR-1` (`E2_DynamicConfinement_and_Universal2LoopGaugeBand_Gate_passed = True`)
- **Zero-Bit Dynamic Confinement Exclusion of `(2D Horotorus Measure, Cover-Instanton)`:** Solving `m004` joint `3D + 2D` stabilization from rational Newton seeds (`(3/5, 4/5, 19)`), combining the `2D` horotorus gauge measure ($\alpha_{\mathrm{UV}}^{-1} = A^*$) with the cover-instanton interval $|\Delta\ln\mu| \approx 29076/1000$ crosses the `1`-loop non-abelian $\mathrm{SU}(3)$ confining Landau pole at $|\Delta\ln\mu|_{\mathrm{pole}} \approx 16918/1000 < 29076/1000$ ($\alpha_3^{-1}|_{1\text{-loop}} \approx -13545/1000 < 0$), dynamically eliminating that branch without spending a discrete selection bit.
- **Universal Relation `UR-1` (`0` Continuous Parameters, `0` Selection Bits):** Across **all `1320` perturbative `2`-loop matrix histories** (`all 44 vacua in ker(M^{-4} - I_2)\{0}, all 3 collar modes {+2 T_{3R}, -2 T_{3R}, 0}, both 3D and 2D measures, both Casimir and classical 6*pi areas, and both cover-instanton and dynamical QCD scales`), `2`-loop gauge + noncommuting matrix Yukawa running shifts $\mathcal{I}_{\mathrm{gauge}}$ **strictly positively** into the sub-permille corridor:
  $$\mathcal{I}_{\mathrm{gauge}}^{\text{all }1320} \in \left[\frac{3129}{1000000},\; \frac{4693}{1000000}\right], \qquad \mathcal{L}_{\mathrm{gauge}}^{\text{all }1320} \in \left[-\frac{6736}{1000},\; -\frac{2521}{1000}\right],$$
  and across **all `264` surviving `3D`-cover histories** (`all 44 vacua × all 3 collar modes × both areas`, total width `< 1/5000`):
  $$\mathcal{I}_{\mathrm{gauge}}^{3\mathrm{D}\text{-cover }264} \in \left[\frac{4028}{1000000},\; \frac{4205}{1000000}\right], \qquad \mathcal{L}_{\mathrm{gauge}}^{3\mathrm{D}\text{-cover }264} \in \left[-\frac{6736}{1000},\; -\frac{6464}{1000}\right].$$
  - **Explicit `UR-1` Kill Line:** Falsified with `0` continuous knobs and `0` discrete selection bits if infrared electroweak mixing and gauge couplings violate $\mathcal{I}_{\mathrm{gauge}} \in [3129/1000000,\; 4693/1000000]$ (`or [4028/1000000, 4205/1000000] on the 3D-cover branch`).

### `Part 1C` — Universal `6D` Gauge-Scalar $D$-Term Stability & Quartic Relation `UR-2` + `U(3)^6` Haar Gate (`E3_UniversalScalarQuarticAttractor_and_Haar6_Gate_passed = True`)
- **Universal Relation `UR-2` (`0` Continuous Parameters, `0` Selection Bits):** Starting from the `6D` gauge-scalar $D$-term boundary law $\lambda_{\mathrm{UV}} = (1/5) g_{\mathrm{UV}}^2$, **100% (`1320 / 1320`) of perturbative histories preserve strict infrared scalar stability** ($\lambda_{\mathrm{IR}} > 42/1000 > 0$, zero vacuum-instability crossings), bounding the dimensionless scalar-to-condensate ratio $\sqrt{2\lambda_{\mathrm{IR}}}$ inside:
  $$\sqrt{2\lambda_{\mathrm{IR}}}\Big|_{\text{all }1320} \in \left[\frac{2899}{10000},\; \frac{11329}{10000}\right], \qquad \sqrt{2\lambda_{\mathrm{IR}}}\Big|_{3\mathrm{D}\text{-cover }264} \in \left[\frac{2899}{10000},\; \frac{9106}{10000}\right]$$
  (`and [3277/10000, 9106/10000] across the 176 collar-localized +-2 T_{3R} histories`).
  - **Explicit `UR-2` Kill Line:** Falsified with `0` continuous knobs and `0` selection bits if $\lambda_{\mathrm{IR}} \le 0$ or $\sqrt{2\lambda_{\mathrm{IR}}} \notin [2899/10000,\; 11329/10000]$ (`or [2899/10000, 9106/10000] on 3D-cover histories`).
- **`U(3)^6` Haar Basis-Scrambling Gate:** Across `10` independent `24`-digit `mpmath` $\mathrm{U}(3)^6$ chiral basis scramblings applied before `2`-loop matrix `RGE` integration, `UR-1` and `UR-2` are invariant to `< (1/1000)^8`.

---

## 2. Planted Controls Summary (`all_planted_controls_passed = True`)

| Control | Perturbation | Measured Breakdown | Gate |
| :--- | :--- | :--- | :--- |
| `PC_REL1_WrongHyperchargeNorm` | Replace $k_2/k_1 = 3/5 \to 1$ | Shifts $\sin^2\theta_{\mathrm{EW}}$ by `> 94/1000` (`> 8/100`) | Pass |
| `PC_REL1_ExtraHiggsDoublets` | Change $N_H = 1 \to 5$ | Breaks $\mathcal{L}_{\mathrm{gauge}} = 0$ by `> 27` (`> 1`) | Pass |
| `PC_REL1_CommutatorPerturbation` | Inject $(3/4)[H_1, H_2]Y_1$ | Diagonal diff `0`; breaks `2`-loop matrix mixing by `> 9/1000` (`> 5/1000`) | Pass |
| `PC_REL1_BrokenDTermQuartic` | Multiply $\lambda_{\mathrm{UV}}$ by `6` | Shifts $\sqrt{2\lambda_{\mathrm{IR}}}$ by `> 15/1000` (`> 1/100`, confirming `> 30`-fold quasi-fixed-point damping) | Pass |
| `PC_REL1_WrongChiralityRGE` | Right-multiply `1`-loop Yukawa $\beta$ | Breaks $\mathrm{U}(3)_R$ Haar invariance by `> 169/1000` (`> 1/1000`) | Pass |

`0 of 19.`
