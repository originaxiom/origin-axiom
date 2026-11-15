# Card `X-BRIDGE-3` — Cuspidal Petersson Normalization & Deformation Audit of $M_R(c_v, c_w, c_u)$, Fujikawa Anomaly-Invariant Strong-CP Theorem, and `agy-002` Canonical $\mathrm{SL}_2(\mathbb{Z})$ Gramian Bridge (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Third sealed stage of Campaign `X-BRIDGE` (`four stages, sixteen blind-sealed commits, 0 of 19`), addressing `physical`'s deformation and basis-invariance audits (`REVIEW.md` Sections `3` and `6`) together with `agy-002`'s Level-`25` Weil linear obstruction and zero-choice $\mathrm{SL}_2(\mathbb{Z})$-invariant left-handed Gramian (`M34` / `A2-AMP` and `M33` / `A2-SMC13`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_bridge_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; published `RGE` solver benchmark floats are strictly `AST`-isolated inside the solver-verification function.

---

## 1. The Package and the Questions

1. **Question `3A` (`Majorana Tensor Family M_R(c_v, c_w, c_u) & Cutoff-Free Cuspidal Petersson Gram Matrix`):**
   - For the `3`-parameter puncture-jet family $M_R(\tau; c_v, c_w, c_u) = c_v A_v(\tau) + c_w A_w(\tau) + c_u A_u(\tau)$, does every constant $(c_v, c_w, c_u)$ preserve exact symmetric structure and modular $T, S$ covariance to `< (1/1000)^15` while shifting bulk singular-value ratios (`e.g. (1, 2, 1) vs (1, 1, 1) by > 1/4`)?
   - Because the spin-structure characteristic satisfies $n + (j + \frac{1}{2})/3 \neq 0$ for all $n \in \mathbb{Z}$ and $j \in \{0, 1, 2\}$, do all three basis tensors $A_v, A_w, A_u$ decay exponentially as $O(y^{7/2} e^{-\pi y / 6})$ at the cusp $y = \operatorname{Im}\tau \to \infty$ (`decaying by > 100000 between y = 2 and y = 60, away from the elliptic zero E_6(i) = 0, with pointwise SL(2, Z)-invariant Frobenius norm`), so that the cutoff-free fundamental-domain Petersson Gram matrix
     $$G_{a b}^{\mathrm{Pet}} = \int_{\mathcal{F}} \operatorname{Tr}\!\big(A_a(\tau)^\dagger A_b(\tau)\big)\, \frac{dx\, dy}{y^2}, \qquad \mathcal{F} = \{\tau \in \mathbb{H} : |\operatorname{Re}\tau| \le \tfrac{1}{2},\, |\tau| \ge 1\}$$
     converges absolutely between $Y_{\mathrm{cut}} = 45$ and $Y_{\mathrm{cut}} = 60$ to `< (1/1000)^3` with strictly positive eigenvalues, fixing canonical Hilbert-space norms $\|A_a\|_{\mathrm{Pet}}$ while leaving `2` explicit `6D` puncture-coupling ratios $(\tilde{c}_v : \tilde{c}_w : \tilde{c}_u)$ on unit-normalized $\hat{A}_a = A_a / \|A_a\|_{\mathrm{Pet}}$ (with exact `UR-7` `CRT` `6w mod 1` fiber invariance and pure `3`-torsion parity collapse holding identically across all non-singular $(c_v, c_w, c_u)$)?
2. **Question `3B` (`Fujikawa Chiral Anomaly Shift & Full U(3) Basis-Invariant Strong-CP Theorem`):**
   - Under `12` completely independent random $\mathrm{U}(3)$ chiral rotations (`6` on slice $w$ and `6` independent ones on mirror slice $R w$, all with $\det U \neq 1$), when coupled to the Fujikawa chiral-anomaly gauge-angle shift $\theta_{\mathrm{YM}} \mapsto \theta_{\mathrm{YM}} - \Delta\arg\det(\mathcal{Y}_1 \mathcal{Y}_2)$, is the physical strong-CP angle $\bar{\theta}_{\mathrm{phys}} = \theta_{\mathrm{YM}} + \arg\det(\mathcal{Y}_1 \mathcal{Y}_2)$ invariant to `< (1/1000)^5` across `10` independent `24`-digit Haar trials at both UV and post-repaired-`2`-loop IR (`and identically zero whenever UV parity reflection R(a, b) = (a, -b) sets theta_YM = 0 mod pi`), while omitting the anomalous $\theta_{\mathrm{YM}}$ shift fails $\mathrm{U}(1)$ phase invariance by `> 1/2` rad?
3. **Question `3C` (`agy-002 Level-25 Weil Obstruction, Zero-Bit Frame C SL(2, Z) Gramian, & 9-Sheet Heisenberg Cover Bridge`):**
   - On `agy-002` `M34`'s Frame C operator (`built standalone with zero imports`), does $T^5 \in \Gamma(5)$ act trivially on `sec2` ($1^2 + 2^2 = 5 \equiv 0 \pmod 5$) while multiplying `sec1` ($1^2 + (-4)^2 = 17 \equiv 2 \pmod 5$) across $|5 w_1| \in \{0, 1, 2\}$ by the three distinct fifth roots $\{1, e^{+4\pi i/5}, e^{-4\pi i/5}\}$ (`closing at T^25`), and does the zero-bit Gramian $\mathcal{H}_{L,f}^{\mathrm{FC}}(\tau) = \frac{1}{24}\sum_{w \in E^*[5]} Y_f(\tau, w) Y_f(\tau, w)^\dagger$ achieve exact $\mathrm{SL}_2(\mathbb{Z})$ invariance (`< (1/1000)^10` under $T, T^5, S$) and strict $3\times 3$ unitarity (`< (1/1000)^10`) both at UV and after repaired `2`-loop evolution (`confirming high-cusp derangement on mixed (tilde_S, S) vs alignment on (S, S)`)?
   - Simultaneously, on the magnetized `3`-bundle (`X-ENDGAME`), does parallel-transporting out the $w$-dependent Landau-gauge Zak factor $\widetilde{Y}_f(\tau, a, b) = Z_{L,f}(b)^\dagger Y_f(\tau, a, b)$ together with summing over all `9` Heisenberg cover lifts $(a + r, b + s)$ ($r, s \in \{0, 1, 2\}$) restore exact matrix $T: \tau \to \tau + 1$ invariance (`< (1/1000)^4` across Levels `5, 10, 15`, whereas omitting either the `9`-sheet cover or Zak parallel transport drifts by `> 1/1000`), while by Schur's Lemma on the irreducible `3`-dimensional Heisenberg representation collapsing $\mathcal{H}_{L,f}$ to $\frac{1}{3}\operatorname{Tr}(\mathcal{H}_{L,f})\, I_3$ (`< (1/1000)^4` — proving why non-degenerate hierarchies on a magnetized `3`-bundle require spontaneous Heisenberg symmetry breaking to individual torsion vacua, in sharp contrast to Frame C's spin-structure generations)?

---

## 2. Deliverables and Definition of Done

1. **`Part 3A`:** `50`-digit modular $T, S$ covariance + deformation test of $M_R(c_v, c_w, c_u)$, cuspidal exponential decay check ($y = 2$ vs $y = 60$), `2D` Gauss–Legendre fundamental-domain Petersson Gram matrix $G_{a b}^{\mathrm{Pet}}$ ($Y_{\mathrm{cut}} = 45$ vs $60$), and `UR-7` `CRT` invariance vs `sec4` ratio comparison across `(1, 1, 1)`, `(1, 2, 1)`, and Petersson-normalized weights.
2. **`Part 3B`:** Explicit Fujikawa anomaly-paired `12`-factor full $\mathrm{U}(3)$ chiral basis-invariance verification (`10` trials in `24`-digit `mpmath`, both UV and post-repaired-`2`-loop IR) + explicit separation of basis invariance from the UV parity premise $\theta_{\mathrm{YM}} = 0 \pmod\pi$.
3. **`Part 3C`:** Standalone verification of `agy-002` `M34` Level-`25` $T^5$ Weil obstruction and Frame C zero-bit $\mathrm{SL}_2(\mathbb{Z})$ Gramian + repaired `2`-loop evolution + `9`-sheet Heisenberg-cover $T$-invariance bridge across Levels `5, 10, 15`.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_MajoranaDeformation_and_CuspidalPetersson_Gate` (`Part 3A`):** $M_R(c_v, c_w, c_u)$ satisfies $T, S$ covariance to `< (1/1000)^15` for all tested triples while `(1, 2, 1)` shifts bulk `sv2/sv3` by `> 1/4`; pointwise $\|A_a(\tau)\|_F$ is $T, S$-invariant to `< (1/1000)^15` and decays by `> 100000` between $y = 2$ and $y = 60$; $G_{a b}^{\mathrm{Pet}}$ converges between $Y_{\mathrm{cut}} = 45$ and $Y_{\mathrm{cut}} = 60$ to `< (1/1000)^3` with positive eigenvalues; and `UR-7` `CRT` `6w mod 1` invariance holds to `< (1/1000)^4` across all three weight choices.
2. **`E2_FujikawaAnomaly_FullU3_StrongCP_Gate` (`Part 3B`):** Independent `12`-factor $\mathrm{U}(3)$ (`det U != 1`) chiral rotations paired with $\theta_{\mathrm{YM}} \mapsto \theta_{\mathrm{YM}} - \Delta\arg\det(\mathcal{Y}_1 \mathcal{Y}_2)$ leave $\bar{\theta}_{\mathrm{phys}}$ invariant to `< (1/1000)^5` at both UV and repaired `2`-loop IR (`and equal to 0 to < (1/1000)^4` under amphichiral parity boundary $\theta_{\mathrm{YM}} = 0$), while planted omission of the anomaly shift fails by `> 1/2` rad.
3. **`E3_Agy002_Level25_and_SL2Z_Gramian_Gate` (`Part 3C`):** Frame C `sec1` $T^5$ Weil phases match $\{1, e^{+4\pi i/5}, e^{-4\pi i/5}\}$ to `< (1/1000)^10` (`closing at T^25`), $\mathcal{H}_{L,f}^{\mathrm{FC}}$ eigenvalues and $|V_{12}^{\mathrm{Gram}}|$ are $\mathrm{SL}_2(\mathbb{Z})$-invariant under $T, T^5, S$ to `< (1/1000)^10` with unitarity `< (1/1000)^10`, Zak-trivialized `9`-sheet Heisenberg cover averaging on the magnetized `3`-bundle restores matrix $T$-invariance to `< (1/1000)^4` and satisfies Schur scalar-identity collapse $\|\mathcal{H}_{L,f} - \frac{1}{3}\operatorname{Tr}(\mathcal{H}_{L,f}) I_3\|_F / \|\mathcal{H}_{L,f}\|_F < (1/1000)^4$ across Levels `5, 10, 15`, and `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance holds to `< (1/1000)^5`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage3_Bridge_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside target-free geometry functions.
2. **`PC_BR3_OmitFujikawaAnomalyShift`:** Applying $\mathrm{U}(3)$ rotations with $\det U \neq 1$ without updating $\theta_{\mathrm{YM}}$ shifts raw $\arg\det(\mathcal{Y}_1 \mathcal{Y}_2)$ by `> 1/2` rad.
3. **`PC_BR3_NonCuspidalZeroCharacteristicDivergence`:** Replacing spin characteristic $(j + \frac{1}{2})/3$ by integer $j/3$ creates a constant $n + a_c = 0$ mode so $y^3 |\theta|^2$ grows as $y^{7/2}$ instead of decaying exponentially (`ratio y=60 / y=2 exceeds 100000`).
4. **`PC_BR3_SingleSheetVs9SheetHeisenbergCover`:** Omitting either the `9`-sheet $(\mathbb{Z}/3\mathbb{Z})^2$ Heisenberg cover sum or the Zak parallel-transport trivialization $Z_{L,f}(b)^\dagger$ fails $T: \tau \to \tau + 1$ invariance by `> 1/1000`, and evaluating at a single torsion point fails Frame C $S$-invariance by `> 1/10`.
5. **`PC_BR3_DiracSesquilinearMismatch`:** Replacing bilinear Majorana $M_R$ by sesquilinear Dirac overlap breaks $W_4$ modular $S$-invariance by `> 1/2`.

`0 of 19.`
