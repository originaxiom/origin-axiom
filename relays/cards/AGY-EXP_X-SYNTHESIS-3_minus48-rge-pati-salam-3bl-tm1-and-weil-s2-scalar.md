# Card `X-SYNTHESIS-3` — `-48` Quartic `RGE` Repair, Closed-Fibre `3(B-L)` Holonomy & `TM1` Sum Rule, Negative-Degree Holomorphic Jet Vanishing, and Weil $S^2$ Central Scalar (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-17`
- **Context:** Third sealed stage of Campaign `X-SYNTHESIS` (`four stages, sixteen blind-sealed commits, 0 of 19`), executing `physical` `PHYSICAL-C4` (`407583a8c`, Findings `1` & `6`), `agy-002/closure` (`f877e0481`, `CLOSURE-G4..G6`), and `agy` (`73eba5485`, `stage1 v16`) via a standalone zero-import verifier (`0` float literals and `0` complex literals module-wide).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_synthesis_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `3A` (`Machacek–Vaughn -48 Quartic RGE Repair, Four-Pillar Benchmark Lock, & 243-History Chiral N_g = 3 Envelopes`):**
   - Converting `2`-loop Higgs quartic running from $\frac{d}{d\ln\mu^2}$ (`where the coefficient is -24 \lambda^2 \operatorname{Tr}_Y`) to $\frac{d}{d\ln\mu} = 2\frac{d}{d\ln\mu^2}$, does repairing $-24 \lambda^2 \operatorname{Tr}_Y \to -48 \lambda^2 \operatorname{Tr}_Y$ match twice the published `2`-loop truncation identically (`while PC_SY3_WrongMinus24QuarticCoeff misses by 24 K_2 \lambda^2 \operatorname{Tr}_Y > 0`), preserve all four published `RGE` benchmark pillars (`2-loop criticality t_{\mathrm{crit}}`, `1-loop BBO`, `2-loop -11/2 mixing`, and `3-family D-parity Strong-CP`), and certify `agy-002`'s `243`-history chiral $N_g = 3$ `Pati–Salam` $\times \mathbb{Z}_2^D$ infrared corridors $\delta_{2\text{-loop}} \in [7/10000, 3/1000]$ and $\sqrt{2\lambda_{\mathrm{IR}}} \in [35/100, 78/100]$?
2. **Question `3B` (`Closed-Fibre CIM (3, 3, -6) Pati–Salam 3(B-L) Holonomy, Bergman (J_0, J_1, J_2) Basis, & Trimaximal TM1 2/3 Sum Rule`):**
   - Re-implemented independently from scratch, does closed-fibre `CIM (3, 3, -6)` stay smooth across $E[3]\setminus\{0\}$, satisfy $\{B - L, V_{\mathrm{bid}}\} = 0$, yield `288/288` Haar-invariant $|V_{tb}| = 1$ under $\mathrm{SU}(2)_R$-symmetric `3(B-L)` (`vs 4/24 on pure 6Y`) while breaking $Y_e = Y_d^T$ pointwise by `> 28` at $\operatorname{Im}\tau = 4$; do $(J_0, J_1, J_2)$ transform covariantly under $(T, S)$ with individual ranks `[1, 3, 3]` (`span rank 3 in \operatorname{Sym}^2\mathbb{C}^3`, retaining explicit $\mathbb{CP}^2$ orientation + scale); and does the `TM1` invariant $|U_{e1}|^2 = 2/3$ remain stable within `< 1/200` under downward running across $\Delta t = -30$ for $y_\tau \le 1/5$?
3. **Question `3C` (`agy 73eba5485 v16 Negative-Degree Holomorphic Jet Check & physical PHYSICAL-C4 Finding 6 Weil S^2 Central Scalar`):**
   - Does `agy` `73eba5485`'s closed-form hyperbolic cusp $L^2$ pole bound $b(a)$ combine with negative-degree holomorphic jet vanishing $h^0(E_\tau, \mathcal{O}(d\cdot p)) = 0$ ($d < 0$) and unimodular shifted-holonomy transport $u' = u\sigma$ (`mapping (9/10, 3/10) to (0, 1/10) mod 1`); and on $(N, r) \in \{(3, 2), (5, 3), (15, 1)\}$, does $(S_N^{(r)})^2 = \gamma_N(r)^{-2} P_N$ carry central parity scalar $\epsilon_N = \gamma_N(r)^{-2} = (-1, +1, -1)$ (`negative on two of the three tested factors while preserving CRT multiplicativity \epsilon_{15} = \epsilon_5 \epsilon_3 and non-projective (S_N^{(r)} T_N^{(r)})^3 = (S_N^{(r)})^2`)?

---

## 2. Pre-Registered Expectations and Mandatory Controls

1. **`E1_RepairedMinus48RGE_and_243ChiralSurface_Gate` (`Part 3A`):** Exact match `< (1/1000)^4` between $\frac{d}{d\ln\mu}$ (`with -48`) and $2\frac{d}{d\ln\mu^2}$, `4`-pillar `RGE` lock (`f64 vs mpmath45 t_{\mathrm{crit}} < (1/1000)^3 * (1/100)`, `Haar6 < (1/1000)^4`), and `243/243` chiral $N_g = 3$ histories inside $\delta_{2\text{-loop}} \in [7/10000, 3/1000]$, $\sqrt{2\lambda_{\mathrm{IR}}} \in [35/100, 78/100]$, $|\bar{\theta}_{\mathrm{QCD}}(\mathrm{IR})| < (1/1000)^4$.
2. **`E2_PatiSalam3BL_BergmanMajorana_and_TM1_Gate` (`Part 3B`):** `288/288` `3(B-L)` alignment (`1 - |V_{tb}| < (1/1000)^4`), $(Y_e, Y_d)$ $s_1/s_3$ separation factor `> 28`, `(J_0, J_1, J_2)` `(T, S)` covariance `< (1/1000)^4` with ranks `[1, 3, 3]`, `10`-trial Haar `< (1/1000)^4`, and `TM1` $|U_{e1}|^2 = 2/3$ (`IR drift < 1/200`).
3. **`E3_AgyV16Jet_and_PhysicalC4WeilCentralScalar_Gate` (`Part 3C`):** Exact negative-degree holomorphic jet vanishing $h^0(E_\tau, \mathcal{O}(d\cdot p)) = 0$ for $d \in \{-5..-1\}$, shifted-holonomy $u' \equiv (0, 1/10) \pmod 1$, and `50`-digit verification of $\epsilon_N = (-1, +1, -1)$ (`negative on 2 of 3 factors`), $\epsilon_{15} = \epsilon_5 \epsilon_3$, and $(S_N^{(r)} T_N^{(r)})^3 = (S_N^{(r)})^2$ to `< (1/1000)^14`.
4. **Mandatory Rejecting Controls:** `Gate_AST_Stage3_Synthesis_Passed` (`0` float literals, `0` complex literals module-wide), `PC_SY3_WrongMinus24QuarticCoeff`, `PC_SY3_Ng6ChiralDoublingShiftsAlpha3`, `PC_SY3_MixedHiggsPairingBreaksVtb`, `PC_SY3_FrobeniusAllOnesBasisDependence`, and `PC_SY3_TM2ColumnSwapBreaksTwoThirds`.

`0 of 19.`
