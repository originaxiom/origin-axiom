# Card `X-APEX-2` — Topological Flux-Obstructed `2D` Parent Domain Wall, Multi-Cell $\mathrm{Spin}(10)$ Octahedral Singlet Chain, and `0`-Knob Schwinger–Dyson Singlet Resolvent Majorana Operator (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-17`
- **Context:** Second sealed stage of Campaign `X-APEX` (`four stages, sixteen blind-sealed commits, 0 of 19`), resolving Boundary `3b` (`preventing 0D domain-wall unwinding via quantized 2D topological magnetic flux`) and Boundary `2a` (`eliminating hand-chosen (1, 1, 1) Majorana orientation ratios via the U(6)-invariant Schwinger-Dyson 1-loop singlet resolvent M_R^{\mathrm{SD}}(\tau)`), plus extending multi-state singlet sewing across $N_{\mathrm{cells}} \in \{2, 3, 4, 6\}$ octahedral chains (`0` float literals and `0` complex literals module-wide).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_apex_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `2A` (`Topological Flux-Obstructed 2D Parent Domain Wall — Non-Unwinding Positive Tension`):**
   - Placing the `4`-slot gauge-Higgs parent action on the cylinder $[-\ell, \ell]_x \times S^1_y$ (`retaining winding-0 mode f_0(x), winding-1 mode f_1(x) e^{iy}, and connection A_y(x) = a(x)`) between the winding-$0$ vacuum $(0, v_0, 0)$ at $x = -\ell$ and winding-$1$ vacuum $(1, 0, v_0)$ at $x = +\ell$, does quantized topological flux $\frac{1}{2\pi}\int F_{xy}\,dx\,dy = 1$ prevent unwinding to zero energy (`converging under Levenberg-Marquardt relaxation to ||\nabla E|| < (1/1000)^3 with strictly positive, \ell-independent wall tension E_{\mathrm{wall}} > 0 and interior potential barrier E_{\mathrm{pot}} > 1/10` at parent weight $\Omega = 3/2$)?
2. **Question `2B` (`Multi-Cell Spin(10) Octahedral State-Chain Singlet Spectrum`):**
   - Across coupled `16_+` Dirac/Dolbeault chains of lengths $N_{\mathrm{cells}} \in \{2, 3, 4, 6\}$ (`with zero hand-assigned eps_end`), does every multi-axis chain cycling through distinct octahedral $\mathrm{Spin}(10)$ axes lift **all** singlet zero modes (`nullity = 0`, smallest singular value `> 1/20`), whereas every single-axis chain of length $N_{\mathrm{cells}} \in \{2, 3, 4, 6\}$ retains exact `nullity = 1`?
3. **Question `2C` (`0-Knob Schwinger–Dyson 1-Loop Singlet Resolvent Majorana Operator M_R^{\mathrm{SD}}(\tau)`):**
   - Integrating out the `6`-component heavy singlet $\Phi$ with its `1`-loop Yukawa bubble self-energy $G_6(\tau)_{kl} = \sum_{i,j}\overline{Y_{ijk}(\tau)}Y_{ijl}(\tau)$ via the exact Schwinger–Dyson resolvent $M_R^{\mathrm{SD}}(\tau) = Y(\tau)\cdot (I_6 + \frac{1}{4\pi} G_6(\tau))^{-1} v_0(\tau)$, is $M_R^{\mathrm{SD}}(\tau)$ **identically invariant under arbitrary $\mathrm{U}(6)$ basis rotations** of the singlet bundle (`immune to U(3)/SO(3) Gram-frame ambiguity!`), covariant under `(T, S)` modular transformations (`< (1/1000)^4`), and full rank `3` (`lifting tree-level J_0 of rank 1 to hierarchical rank 3 without any hand-chosen CP^2 ratios, while naive E[2]\setminus\{0\} half-period summation fails via the Heisenberg cocycle`)?

---

## 2. Pre-Registered Expectations and Mandatory Controls

1. **`E1_FluxObstructed2DWall_NonUnwinding_Gate` (`Part 2A`):** Exact topological flux $\Phi_{\mathrm{mag}} = 1$ (`< (1/1000)^4`), relaxed gradient norm `< (1/1000)^3` at $\ell \in \{6, 8\}$ (`\ell = 6 vs \ell = 8 wall-tension shift < 1/1000, proving finite localized soliton!`), and strictly positive relaxed potential energy $E_{\mathrm{pot}} > 1/10$.
2. **`E2_MultiCellSpin10_OctahedralSingletChain_Gate` (`Part 2B`):** Multi-axis nullities `[0, 0, 0, 0]` across $N_{\mathrm{cells}} \in \{2, 3, 4, 6\}$ (`all min singular values > 1/20`) vs single-axis control nullities `[1, 1, 1, 1]`, and unitary basis-scrambling invariance `< (1/1000)^4`.
3. **`E3_SchwingerDysonResolvent_MajoranaOperator_Gate` (`Part 2C`):** Exact `10`-trial $\mathrm{U}(6)$ singlet-basis rotation invariance `< (1/1000)^4`, `(T, S)` modular covariance `< (1/1000)^4`, full rank `3` (`vs tree-level \kappa = 0 rank 1`), and `10`-trial Type-I seesaw $\mathrm{U}(3)^3$ Haar invariance `< (1/1000)^4`.
4. **Mandatory Rejecting Controls:** `Gate_AST_Stage2_Apex_Passed` (`0` float literals, `0` complex literals module-wide), `PC_AP2_ZeroWindingTrivialVacuumUnwinds` (`winding 0 -> 0 relaxes to E < (1/1000)^8`), `PC_AP2_SingleAxisChainKeepsZeroMode` (`nullity == 1` across all $N$), and `PC_AP2_NaiveHalfPeriodSumBreaksModularCocycle` (`naive E[2]\setminus\{0\} sum breaks T/S covariance by > 1`).

`0 of 19.`
