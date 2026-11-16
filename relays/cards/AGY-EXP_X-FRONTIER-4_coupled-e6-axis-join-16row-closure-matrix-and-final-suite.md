# Card `X-FRONTIER-4` — Coupled `1D` $E_6$ State-Axis Joining Boundary-Value Problem, Updated `16`-Row Four-Tier Scoped Master Closure Matrix, and Final Pre-Unblinding `0 of 19` Suite

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Fourth and final sealed stage of Campaign `X-FRONTIER` (`four stages, sixteen blind-sealed commits, 0 of 19`), formulating and solving the reduced `1D` coupled $E_6$ Wilson + charged-form state-axis joining boundary-value problem (`neutral-only non-localization vs Higgsed exponential screening`), upgrading `X-CLOSURE-4`'s `14`-row closure ledger to a **`16`-row Four-Tier Scoped Master Closure Matrix** (`integrating P-C3c..P-C3f, (\lambda_+, \lambda_-), \sigma_* > 0, and the D_5 cross-form nilpotent-centralizer theorem`), and sealing the final `24`-digit $\mathrm{U}(3)^6$ Haar and `12`-factor full $\mathrm{U}(3)$ Fujikawa certificates.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_frontier_4_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`literature RGE solver benchmark constants strictly AST-isolated`).

---

## 1. The Package and the Questions

1. **Question `4A` (`1D` Coupled $E_6$ Wilson + Charged-Form State-Axis Joining `BVP`):**
   - Because distinct state axes `(k, j, i)` carry distinct discrete characters `(-1, -1)`, `(-1, +1)`, `(+1, -1)` on $H = (\mathrm{Spin}(10)\cdot \mathrm{U}(1)_Q) / \mathbb{Z}_4$, any smooth configuration interpolating on $x \in [-L, +L]$ (`L \in \{6, 12, 24\}`) between `(-1, -1)` (`c(-L) = 0`) and `(-1, +1)` (`c(+L) = \pi`) inside the neutral sector (`t = 0`, $m_Q = 0$) satisfies $c''(x) = 0$: does its transition derivative $|c'(L)| / |c'(0)| = 1$ fail exponential localization (`gradient energy scaling as \pi^2 / (2 L)`), whereas turning on the charged $E_6$ Higgsed branch (`m_Q = 2 e_Q t > 0` screening the transition around the localized wall `-c''(x) + (1/2) m_Q^2 \sin(2 c(x)) = 0`) localizes the join exponentially (`|c'(L)| / |c'(0)| < (1/1000)^2` at $L = 12$ and `< (1/1000)^3` at $L = 24$, with $L$-convergent finite wall action $4 m_Q$ to `< (1/1000)^8`)?
2. **Question `4B` (`16`-Row Four-Tier Scoped Master Closure Matrix):**
   - Can all pure-math theorems, model-conditioned consequences, conditional `P-C3a..f` parent-to-model bridges (`keeping infinite-dimensional Banach-IFT, L^2 Dolbeault graph-closure, and transverse 3D PDE stationarity visibly scoped`), and explicit remaining duties (`2` heavy-singlet source-vector ratios under $\mathrm{U}(3)$ Petersson isotropy, multi-state composition / endpoint lifting, and Picard–Lindelöf $v_{\mathrm{EW}}$) be assembled into a `16`-row machine-verified **Four-Tier Scoped Master Closure Matrix** (`7` Tier `I-A` + `4` Tier `I-B` + `3` Tier `II` + `2` Tier `III` = `16`, zero literal flags)?
3. **Question `4C` (Final Repaired `0 of 19` Suite & `24`-Digit $\mathrm{U}(3)^6$ / `12`-Factor Fujikawa Certificates):**
   - Does the full `0 of 19` trajectory suite hold with `f64 vs mpmath32 < 2 * (1/1000)^4`, `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance `< (1/1000)^5`, and `10`-trial `12`-factor full $\mathrm{U}(3)$ Fujikawa anomaly-paired Strong-CP invariance `< (1/1000)^6` rad?

---

## 2. Deliverables and Definition of Done

1. **`Part 4A`:** Exact + `60`-digit `BVP` verification comparing neutral-only `t = 0` linear-ramp non-localization against charged $E_6$ Higgsed ($m_Q = 2 e_Q t > 0$) exponential domain-wall localization across $L \in \{6, 12, 24\}$, plus `16`-frame $\mathrm{U}(3)$ Petersson isotropy and `286`-vacuum / `Pati–Salam` corridors.
2. **`Part 4B`:** Machine-verified `16`-row **Four-Tier Scoped Master Closure Matrix** (`7 + 4 + 3 + 2 = 16` live-computed witnesses, including `T_IA_07` for `78`-dim $E_6$ centralizer + `248`-dim $E_8$ eighth-power trace law and `T_II_14` for `P-C3c..f` spin quartic, order-`2`/order-`6` $J$, $(\lambda_+, \lambda_-)$, $\sigma_* > 0$, $D_5$ cross-form nilpotent-centralizer selection rule, and screened $E_6$ axis join).
3. **`Part 4C`:** Final `0 of 19` vector suite + `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar and `12`-factor full $\mathrm{U}(3)$ Fujikawa certificates.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_CoupledE6StateAxisJoin_and_Corridors_Gate` (`Part 4A`):** Neutral-only boundary-to-midpoint slope ratio equals `1` (`non-localized`), whereas Higgsed $E_6$ (`m_Q = 2 e_Q t = 2` at `(e_Q, t) = (1, 1)`) achieves $|c'(12)| / |c'(0)| < (1/1000)^2$, $|c'(24)| / |c'(0)| < (1/1000)^3$, and wall-action convergence $|S_{\mathrm{wall}}(24) - 4 m_Q| / (4 m_Q) < (1/1000)^8$; `16`-frame $\mathrm{U}(3)$ sweep `> 1000x`; `286` of `288` vacua finite (`100%` of Levels `5` & `15`).
2. **`E2_SixteenRow_FourTier_MasterClosureMatrix_Gate` (`Part 4B`):** All `16` rows carry live numerical/symbolic witnesses (`0` hard-coded boolean/zero claim flags) with exact tier counts `(7, 4, 3, 2)`.
3. **`E3_FinalZeroOf19Suite_and_Haar6_Gate` (`Part 4C`):** `f64 vs mpmath32 < (1/1000)^4`, `Haar6 < (1/1000)^5`, and `12`-factor Fujikawa `< (1/1000)^6` rad.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage4_Frontier_Passed`:** `AST` check confirming zero disallowed imports and strict isolation of `0` float literals inside target-free model functions.
2. **`PC_FR4_NeutralOnlyUnscreenedRampNonLocalization`:** Setting $t = 0 \implies m_Q = 0$ leaves $|c'(L)| / |c'(0)| = 1$ for all $L \in \{6, 12, 24\}$, proving neutral-only configurations cannot exponentially localize a state-axis holonomy jump.
3. **`PC_CL4_MetricIsotropyCannotSelectVector` & `PC_CL4_NonHermitianPositiveRealSchurCounterexample`:** `U(3)` Petersson rotation sweeps `sec4_r23` by `> 1000x`, and non-Hermitian $H = L = I_3, B = i(2/5)I_3, C = i(3/7)I_3$ gives real positive Schur complement $(41/35)I_3$.
4. **`PC_CL4_RightActingRGEHaarViolation`:** Un-transposed `2`-loop mixed Yukawa violates $\mathrm{U}(3)^6$ Haar invariance (`> 1/1000`).

`0 of 19.`
