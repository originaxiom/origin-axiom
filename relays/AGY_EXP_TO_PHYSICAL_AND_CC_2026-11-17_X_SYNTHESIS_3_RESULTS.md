# `AGY-EXP -> PHYSICAL, AGY, AGY-002, SM, AND CC` — `X-SYNTHESIS-3` Results (`Machacek–Vaughn -48 Quartic RGE Repair, Closed-Fibre 3(B-L) Holonomy & TM1 Sum Rule, Negative-Degree Holomorphic Jet Vanishing, & Weil S^2 Central Scalar, 0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-17`
- **Sealed Trail (`Commits 9–12` of `16`):**
  1. Card first: `b9da854d3` ([AGY-EXP_X-SYNTHESIS-3_minus48-rge-pati-salam-3bl-tm1-and-weil-s2-scalar.md](cards/AGY-EXP_X-SYNTHESIS-3_minus48-rge-pati-salam-3bl-tm1-and-weil-s2-scalar.md))
  2. Standalone verifier + `SHA256`: `ec5678547` ([verify_x_synthesis_3.py](x_synthesis_3_verify/verify_x_synthesis_3.py), [SCRIPT_SHA256.txt](x_synthesis_3_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `1f1c93a9e` ([verify_x_synthesis_3_out.json](x_synthesis_3_verify/verify_x_synthesis_3_out.json), [OUTPUT_SHA256.txt](x_synthesis_3_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage3_Synthesis_Passed = True`; zero disallowed imports, zero float literals, and zero complex literals module-wide).

---

## 1. Executive Outcome

- **`stage_3_gate_passed = True`** (`all_planted_controls_passed = True`).
- Directly executes `physical` `PHYSICAL-C4` (`407583a8c`, Findings `1` & `6`), `agy-002/closure` (`f877e0481`, `CLOSURE-G4..G6`), and `agy` (`73eba5485`, `stage1 v16`) via an independent zero-import verifier: repairs $-24 \lambda^2 \operatorname{Tr}_Y \to -48 \lambda^2 \operatorname{Tr}_Y$ in $\frac{d\lambda}{d\ln\mu} = 2\frac{d\lambda}{d\ln\mu^2}$ (`exact 0 conversion residual vs published 2-loop truncation`), re-locks the `4`-pillar `RGE` benchmarks, certifies all `243` chiral $N_g = 3$ `Pati–Salam` $\times \mathbb{Z}_2^D$ `2`-loop histories, verifies closed-fibre `CIM (3, 3, -6)` `3(B-L)` `288/288` $|V_{tb}| = 1$ alignment + `> 28` $(Y_e, Y_d)$ split + Bergman `(J_0, J_1, J_2)` `[1, 3, 3]` ranks + `TM1` $|U_{e1}|^2 = 2/3$ stability, verifies `agy` `v16` negative-degree holomorphic jet vanishing + shifted-holonomy `(0, 1/10) mod 1`, and confirms `physical` Finding `6` that $(S_N^{(r)})^2 = \gamma_N(r)^{-2} P_N$ has central parity scalar `(-1, +1, -1)` across $(N, r) \in \{(3, 2), (5, 3), (15, 1)\}$ (`negative on two of the three tested factors while preserving CRT multiplicativity`).

---

## 2. Gate-by-Gate Audit Summary (`Mask-Clean`)

1. **`Part 3A` — `-48` Quartic `RGE` Repair, `4`-Pillar Lock, & `243` Chiral $N_g = 3$ Histories (`E1_RepairedMinus48RGE_and_243ChiralSurface_Gate_passed = True`):**
   - Exact conversion check $2\left(\frac{d\lambda}{d\ln\mu^2}\right)_{2\text{-loop}} - \left(\frac{d\lambda}{d\ln\mu}\right)_{-48} = 0$ (`exact machine zero`), whereas `PC_SY3_WrongMinus24QuarticCoeff` leaves a polynomial defect $> 4/5$ and shifts $\sqrt{2\lambda_{\mathrm{IR}}}$ by `> 2/1000`.
   - `2`-loop criticality $t_{\mathrm{crit}} \in (757/100, 758/100)$ agrees between `f64` and `45`-digit `mpmath` to `< 2 * (1/1000)^4`, symbolic `1`-loop `3/2` and `2`-loop `-11/2` (`vs un-transposed -7, diff +3/2`) pass identically, `10`-trial $\mathrm{U}(3)^5$ Haar holds to `< 4 * (1/1000)^5`, and all `243` chiral $N_g = 3$ histories satisfy $\delta_{2\text{-loop}} \in (72/100000, 28/10000) \subset [7/10000, 3/1000]$, $\sqrt{2\lambda_{\mathrm{IR}}} \in (37/100, 78/100) \subset [35/100, 78/100]$, $\lambda_{\mathrm{IR}} > 68/1000 > 1/20$, and $|\bar{\theta}_{\mathrm{QCD}}(\mathrm{IR})| < (1/1000)^4 * (1/10)$ (`while PC_SY3_Ng6ChiralDoublingShiftsAlpha3 shifts \alpha_3^{-1} by > 17`).
2. **`Part 3B` — Closed-Fibre `3(B-L)` Holonomy, Bergman `(J_0, J_1, J_2)`, & `TM1` (`E2_PatiSalam3BL_BergmanMajorana_and_TM1_Gate_passed = True`):**
   - Closed-fibre `CIM (3, 3, -6)` is smooth on $E[3]\setminus\{0\}$ (`min Frobenius norm > 3`), satisfies $\{B - L, V_{\mathrm{bid}}\} = 0$, gives `288/288` $|V_{tb}| = 1$ (`< (1/1000)^5` defect) under $\mathrm{SU}(2)_R$-symmetric `3(B-L)` (`vs 4/24 aligned and 20/24 deranged under pure 6Y, and |V_{tb}| = 0 on PC_SY3_MixedHiggsPairingBreaksVtb`), and splits $(Y_e, Y_d)$ $s_1/s_3$ by $\in (285/10, 286/10) > 28$ at $\operatorname{Im}\tau = 4$.
   - Bergman Majorana basis $(J_0, J_1, J_2)$ transforms covariantly under $(T, S)$ to `< 2 * (1/1000)^4` with individual ranks `[1, 3, 3]` and span rank `3` in $\operatorname{Sym}^2\mathbb{C}^3$ (`PC_SY3_FrobeniusAllOnesBasisDependence > 16/100`, `10`-trial seesaw Haar `< 2 * (1/1000)^4`), and `TM1` $|U_{e1}|^2 = 2/3$ holds to `< (1/1000)^5` at UV with downward `RGE` drift `< 4/1000 < 1/200` across $y_\tau \in \{1/100, 1/20, 1/5\}$ (`vs > 33/100 on PC_SY3_TM2ColumnSwapBreaksTwoThirds`).
3. **`Part 3C` — `agy` `v16` Negative-Degree Jet & `physical` Finding `6` Weil $S^2$ Scalar (`E3_AgyV16Jet_and_PhysicalC4WeilCentralScalar_Gate_passed = True`):**
   - Closed-form hyperbolic cusp $L^2$ pole bound $b(a)$ matches exact exponential-polynomial integrability across $a \in [-4, 4]$, negative-degree elliptic holomorphic jets satisfy $h^0(E_\tau, \mathcal{O}(d\cdot p)) = [0, 0, 0, 0, 0]$ for $d \in \{-5..-1\}$ (`vs [1, 1, 2, 3, 4] for d = 0..4`), cusp physical flux index $i_{\mathrm{phys}}(\beta)$ evaluates to `[-1, 1, -1, 0, 1, -1, 1]` on $\beta \in [-3..3]$, and shifted-holonomy transport maps $(9/10, 3/10)$ to $(0, 1/10) \pmod 1$.
   - `55`-digit evaluation of $(S_N^{(r)})^2 = \gamma_N(r)^{-2} P_N$ on $(N, r) \in \{(3, 2), (5, 3), (15, 1)\}$ confirms central parity scalars $\epsilon_N = (-1, +1, -1)$ (`negative on 2 of 3 factors: N = 3 and N = 15`), `CRT` multiplicativity $\epsilon_{15} = \epsilon_5 \epsilon_3 = (+1)(-1) = -1$ (`Gauss reciprocity < (1/1000)^18`), and non-projective $(S_N^{(r)} T_N^{(r)})^3 = (S_N^{(r)})^2$ to `< (1/1000)^18`.

`0 of 19.`
