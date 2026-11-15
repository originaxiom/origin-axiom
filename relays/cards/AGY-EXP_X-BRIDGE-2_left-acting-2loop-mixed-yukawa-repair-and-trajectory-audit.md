# Card `X-BRIDGE-2` — Exact Left-Acting `2`-Loop Mixed-Yukawa Adjoint Repair (`BPV` Equation `27` & `PRD 47, 2038` Rank-`1` Coefficient `11/2`), `80`-Digit Invariant Verification, and Old-vs-Repaired Trajectory Audit (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Second sealed stage of Campaign `X-BRIDGE` (`four stages, sixteen blind-sealed commits, 0 of 19`), directly executing `physical`'s second confirmed pure-math repair (`REVIEW.md` Section `2` and `NEXT_DERIVATIONS.md` Step `1`): repairing the noncommuting `2`-loop mixed Yukawa matrix-product order in both `f64` and `mpmath` `RGE` integrators, repairing the `2`-generation rank-`1` mixing derivative reference from `7` to `11/2` (`citing PRD 47, 2038 + Luo–Xiao + Bednyakov–Pikelner–Velizhanin JHEP 09 (2014) 098 eq. 27`), and auditing the exact trajectory shift against preserved prior runs.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_bridge_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; published `RGE` solver benchmark floats are strictly `AST`-isolated inside the solver-verification function.

---

## 1. The Package and the Questions

1. **Question `2A` (`80-Digit Right-to-Left Adjoint Conversion & Noncommuting Trace Invariant`):**
   - When right-acting Yukawa matrices $Y_f^{\mathrm{R}} = Y_f^\dagger$ (`Luo–Xiao eqs. 1, 6, 7`) with mixed `2`-loop factors $Y_1^{\mathrm{R}}(-H_1 H_2 - \frac{1}{4}H_2 H_1)$ and $Y_2^{\mathrm{R}}(-H_2 H_1 - \frac{1}{4}H_1 H_2)$ are converted by Hermitian conjugation to left-acting $Y_f$, does $(A B)^\dagger = B^\dagger A^\dagger$ reverse the mixed products to:
     $$\beta_{Y_1}^{(2),\mathrm{mixed}} = \Big(-\frac{1}{4}H_1 H_2 - H_2 H_1\Big)Y_1, \qquad \beta_{Y_2}^{(2),\mathrm{mixed}} = \Big(-\frac{1}{4}H_2 H_1 - H_1 H_2\Big)Y_2,$$
     matching `2` times the $d/d\ln\mu^2$ left-acting coefficients $(-\frac{1}{8}, -\frac{1}{2})$ of Bednyakov–Pikelner–Velizhanin (`JHEP 09 (2014) 098` eq. `27` and footnote `7`) to `< (1/1000)^23` (`< (1/1000)^20` gate) on generic complex noncommuting matrices, with basis-invariant shift $\delta\frac{d}{dt}\operatorname{Tr}(H_1 H_2) = \frac{3}{2}\operatorname{Tr}([H_1, H_2]^2) < 0$ whenever $[H_1, H_2] \neq 0$?
2. **Question `2B` (`Repaired Four-Pillar Published Benchmark Gate at Coefficient 11/2`):**
   - Under `80`-digit eigenvector differentiation of the `2`-generation rank-`1` mixing problem (`PRD 47, 2038` eqs. `10, 17–26` updated with Luo–Xiao / `BPV` `2`-loop SM coefficients), does the pure `2`-loop logarithmic mixing derivative match exact coefficient **`11/2`** on $y_{3,\mathrm{sec1}}^2 y_{3,\mathrm{sec2}}^2$ (`7 - 3/4 - 3/4 = 11/2`) to `< (1/1000)^20` in `mpmath(85)` (`and < 5/10000000 in centered f64`), while rejecting the old reversed-order coefficient `7` by `> 5/1000` relative error?
3. **Question `2C` (`Preserved Old-vs-Repaired UV-to-IR Trajectory Shift & 24-Digit U(3)^6 Haar Gate`):**
   - Across both the Casimir-stabilized `X-ENDGAME` reference vacuum `(4/15, 8/15)` and representative vacua across Levels `5`, `10`, and `15`, how much does the $+\frac{3}{4}[H_1, H_2]Y_1$, $-\frac{3}{4}[H_1, H_2]Y_2$ repair shift all infrared dimensionless gauge, scalar, mass-ratio, mixing, seesaw, and amphichiral observables (`recorded side-by-side with the preserved old ordering`), and does the repaired `mpmath` `2`-loop integrator preserve `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar basis invariance to `< (1/1000)^5`?

---

## 2. Deliverables and Definition of Done

1. **`Part 2A`:** `80`-digit `mpmath` right-acting Luo–Xiao vs left-acting `BPV` adjoint equivalence check and $\delta\frac{d}{dt}\operatorname{Tr}(H_1 H_2) = \frac{3}{2}\operatorname{Tr}([H_1, H_2]^2)$ basis-invariant identity check on generic complex rational Yukawa matrices.
2. **`Part 2B`:** `80`-digit and `f64` repaired `4`-pillar `RGE` benchmark gate (`with PRD 47, 2038 + BPV rank-1 mixing coefficient 11/2`, catching the old reversed product order as a mandatory planted failure control).
3. **`Part 2C`:** Side-by-side `old vs repaired` UV-to-IR `2`-loop matrix `RGE` trajectory comparison (`in both f64 and 32-digit mpmath`) + `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance check.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_AdjointConversion_and_TraceInvariant_Gate` (`Part 2A`):** `(beta_LX(Y^dagger))^dagger == beta_BPV(Y)` holds to `< (1/1000)^20`, $\delta\frac{d}{dt}\operatorname{Tr}(H_1 H_2) - \frac{3}{2}\operatorname{Tr}([H_1, H_2]^2) = 0$ to `< (1/1000)^20`, and $\operatorname{Tr}([H_1, H_2]^2) < -1/1000$ on the noncommuting test state (`while vanishing identically on diagonal matrices`).
2. **`E2_RepairedFourPillar_11Over2_Gate` (`Part 2B`):** Repaired rank-`1` `2`-loop mixing derivative matches analytical coefficient `11/2` to `< (1/1000)^20` in `80`-digit `mpmath` (`and < 5/10000000 in f64`), alongside all other three published pillars.
3. **`E3_OldVsRepairedTrajectory_and_Haar6_Gate` (`Part 2C`):** Repaired `f64` and `32`-digit `mpmath` trajectories agree to `< (1/1000)^4`, side-by-side `old vs repaired` shifts are non-zero on noncommuting mixing observables while leaving `1`-loop gauge eliminants and amphichiral determinant cancellation `< (1/1000)^4` intact, and `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance holds to `< (1/1000)^5`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage2_Bridge_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside target-free geometry functions.
2. **`PC_BR2_ReversedMixedProductOrder`:** Reverting to the old un-transposed `(-H_1 H_2 - 1/4 H_2 H_1) Y_1` and `(-H_2 H_1 - 1/4 H_1 H_2) Y_2` ordering fails the `BPV` adjoint identity, shifts $\frac{d}{dt}\operatorname{Tr}(H_1 H_2)$ by `> 1/100`, and fails the `11/2` rank-`1` mixing derivative by `> 1/100` relative error.
3. **`PC_BR2_WrongDiffFactor`:** Omitting the factor of `2` between $d/d\ln\mu$ and $d/d\ln\mu^2$ fails `BPV` eq. `27` and `1`-loop gauge integration by `> 1/10`.
4. **`PC_BR2_WrongRunningDirection`:** Flipping `RGE` sign fails downward Naumov running by `> 1/2`.
5. **`PC_BR2_WrongMajoranaTranspose`:** Replacing $W_4 H_3^T \to W_4 H_3$ breaks Majorana symmetry by `> 1/5`.
6. **`PC_BR2_WrongChiralityRGE`:** Right-multiplying `1`-loop Yukawa $\beta$-functions breaks $\mathrm{U}(3)_R$ Haar invariance by `> 1/1000`.

`0 of 19.`
