# `AGY-EXP -> PHYSICAL, AGY, AGY-002, SM, AND CC` — `X-APEX-2` Results (`Flux-Obstructed 2D Parent Domain Wall, Multi-Cell Spin(10) Octahedral Singlet Chain, & Canonical 0-Knob Schwinger–Dyson Singlet Resolvent Majorana Operator, 0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-17`
- **Sealed Trail (`Commits 5–8` of `16`):**
  1. Card first: `72154f93a` ([AGY-EXP_X-APEX-2_flux-obstructed-2d-wall-multicell-spin10-chain-and-resolvent-majorana.md](cards/AGY-EXP_X-APEX-2_flux-obstructed-2d-wall-multicell-spin10-chain-and-resolvent-majorana.md))
  2. Standalone verifier + `SHA256`: `9491eef20` ([verify_x_apex_2.py](x_apex_2_verify/verify_x_apex_2.py), [SCRIPT_SHA256.txt](x_apex_2_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `5a9157cfa` ([verify_x_apex_2_out.json](x_apex_2_verify/verify_x_apex_2_out.json), [OUTPUT_SHA256.txt](x_apex_2_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage2_Apex_Passed = True`; zero disallowed imports, zero float literals, and zero complex literals module-wide).

---

## 1. Executive Outcome

- **`stage_2_gate_passed = True`** (`all_planted_controls_passed = True`).
- Directly resolves three mathematical-physics boundaries across parent domain-wall topology (`Boundary 3b`), multi-cell $\mathrm{Spin}(10)$ state-chain singlet lifting, and `0`-knob Majorana operator selection (`Boundary 2a`):
  1. Formulates the `2D` cylinder gauge-Higgs domain wall on $[-\ell, \ell]_x \times S^1_y$ interpolating between winding-$0$ ($A_y = 0, q = v_0$) and winding-$1$ ($A_y = 1, q = v_0 e^{iy}$) vacua (`quantized flux \frac{1}{2\pi}\int F_{xy} = 1`), relaxes at parent chiral weight $\Omega = 3/2$ via guarded Levenberg–Marquardt to $\|\nabla E\| < (1/1000)^4$, and establishes a **non-unwinding positive relaxed wall tension** $E_{\mathrm{wall}} \in (1168/10000, 1169/10000) > 1/10$ (`\ell = 6 vs \ell = 8 relative diff < 7 * (1/1000)^2 * (1/100)`) and potential barrier $\in (246/1000, 247/1000) > 1/10$ (`whereas trivial zero-winding PC_AP2_ZeroWindingTrivialVacuumUnwinds collapses to < (1/1000)^9`).
  2. Extends operator-derived `16_+` $\mathrm{Spin}(10)$ Dirac/Dolbeault chains across $N_{\mathrm{cells}} \in \{2, 3, 4, 6\}$ cycling the `3` octahedral $2O$ state axes (`zero assigned eps_end`), establishing `nullity = [0, 0, 0, 0]` (`smallest singular values \in (119/1000, 180/1000) > 1/10`, `Haar < 3 * (1/1000)^5`) vs `PC_AP2_SingleAxisChainKeepsZeroMode` `nullity = [1, 1, 1, 1]`.
  3. **Eliminates the `2` continuous Majorana orientation ratios (`\mathbb{CP}^2` knobs):** proves naive $E[2]\setminus\{0\}$ half-period summation fails $T$-covariance (`> 58/10` in `PC_AP2_NaiveHalfPeriodSumBreaksModularCocycle`) via the Heisenberg magnetic Zak cocycle, whereas integrating out the `6`-plet heavy singlet with its `1`-loop fermion bubble $G_6(\tau)_{kl} = \sum_{i,j}\overline{Y_{ijk}(\tau)}Y_{ijl}(\tau)$ yields the **Schwinger–Dyson Singlet Resolvent Majorana Operator** $M_R^{\mathrm{SD}}(\tau) = Y(\tau)\cdot (I_6 + \frac{1}{4\pi} G_6(\tau))^{-1} v_0(\tau)$, which has **`0` orientation knobs, exact $\mathrm{U}(6)$ singlet-basis invariance (`< (1/1000)^5`), exact `(T, S)` modular covariance (`< 6 * (1/1000)^5`), and full rank `3` (`singular values \in (248/100, 249/100), (99/1000, 100/1000), (19/1000, 20/1000)` vs tree-level rank `1`, `10`-trial seesaw $\mathrm{U}(3)$ Haar `< (1/1000)^4`)**.

---

## 2. Gate-by-Gate Audit Summary (`Mask-Clean`)

1. **`Part 2A` — Flux-Obstructed `2D` Parent Domain Wall (`E1_FluxObstructed2DWall_NonUnwinding_Gate_passed = True`):**
   - Winding-$1$ cylinder wall carries quantized magnetic flux `= 1`, relaxes at $\Omega = 3/2$ to $\|\nabla E\| < 4 * (1/1000)^4 * (1/10)$ across both $\ell = 6$ and $\ell = 8$, and retains strictly positive $S^1_y$-averaged wall tension $E_{\mathrm{wall}} \in (1168/10000, 1169/10000)$ (`relative domain-size convergence < 7 * (1/1000)^2 * (1/100)`) and potential barrier $\in (246/1000, 247/1000)$ (`vs trivial zero-winding unwinding to < (1/1000)^9`).
2. **`Part 2B` — Multi-Cell $\mathrm{Spin}(10)$ Octahedral Singlet Chain (`E2_MultiCellSpin10_OctahedralSingletChain_Gate_passed = True`):**
   - Multi-axis chains of lengths `[2, 3, 4, 6]` lift all zero modes (`nullities = [0, 0, 0, 0]`, `smallest singular values > 119/1000`), whereas single-axis chains leave `1` exact zero mode at every length (`nullities = [1, 1, 1, 1]`).
3. **`Part 2C` — Canonical `0`-Knob Schwinger–Dyson Singlet Resolvent Majorana (`E3_SchwingerDysonResolvent_MajoranaOperator_Gate_passed = True`):**
   - Rank jumps canonically from `1` (`tree level`) to `3` (`1-loop singlet resolvent`) with zero hand-chosen weights, `10`-trial $\mathrm{U}(6)$ singlet-basis invariance `< (1/1000)^5`, `(T, S)` modular covariance `< 6 * (1/1000)^5`, and `10`-trial Type-I seesaw $\mathrm{U}(3)$ Haar invariance `< (1/1000)^4`.

`0 of 19.`
