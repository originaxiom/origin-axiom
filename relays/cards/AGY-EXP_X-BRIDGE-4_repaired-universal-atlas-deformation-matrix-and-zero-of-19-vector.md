# Card `X-BRIDGE-4` — Repaired `UR-1..UR-7` Universal Kill-Line Atlas, Three-Column Input & Deformation Matrix, and Repaired `0 of 19` Prediction Vector (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Fourth and final sealed stage of Campaign `X-BRIDGE` (`four stages, sixteen blind-sealed commits, 0 of 19`), consolidating Stages `1–3` into: (i) the complete `1320`-history gauge/scalar census and `288`-UV / `248`-IR flavor, amphichiral, and seesaw census re-executed under the repaired left-acting `BPV`/Luo–Xiao `2`-loop equations (`with exact side-by-side old-vs-repaired shift bounds across every history and vacuum`), (ii) a machine-verified three-column input and deformation matrix meeting `physical`'s audit standard, and (iii) the complete repaired dimensionless `0 of 19` prediction vector.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_bridge_4_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; published `RGE` solver benchmark floats are strictly `AST`-isolated inside the solver-verification function.

---

## 1. The Package and the Questions

1. **Question `4A` (`Repaired 1320-History & 248-Vacuum UR-1..UR-7 Universal Kill-Line Census`):**
   - Across all `1320` perturbative gauge/scalar histories (`UR-1`, `UR-2`) and all `288` UV / `248` meridian-active (`3a notin Z`) IR vacua across Levels `5, 10, 15` (`UR-3..UR-7`), how much do the universal infrared corridors shift when re-integrated with the repaired left-acting `BPV` `JHEP 09 (2014) 098` eq. `27` mixed-Yukawa matrix ordering (`delta beta_Y1 = +(3/4)[H_1, H_2]Y_1`, `delta beta_Y2 = -(3/4)[H_1, H_2]Y_2`) and direct-`SVD` symmetric Takagi extraction?
   - Specifically, does `max |repaired - old|` remain bounded by `< (1/1000)^4` on `I_gauge` and `< (1/1000)^2` on `sqrt(2*lambda_IR)` and all flavor/seesaw ratios across all `1320` gauge/scalar histories and all `248` perturbative flavor/seesaw vacua, preserving `0` infrared divergences on all `248` `3a notin Z` vacua, `lambda_IR > 42/1000 > 0` across all `1320` histories, exact `CRT` `6w mod 1` fiber identities (`UR-3, UR-4, UR-5, UR-7`), and amphichiral `6x6` block determinant phase `< (1/1000)^4` rad across all `288` UV and `248` IR vacua (`UR-6`)?
2. **Question `4B` (`Machine-Verified Three-Column Input & Deformation Accounting Matrix`):**
   - When every structural ingredient audited by `physical` and `agy-002` (`punctured relative carrier H^2(X, dX; Z) = Z, boundary-law stiffness c_H & cut-independence, rank-3 principal-parts unit m in {-1, +1}, Majorana Petersson norms vs 2 relative puncture ratios, Fujikawa strong-CP basis invariance vs UV parity boundary theta_YM = 0, collar & matching scales, and torsion vacuum selection vs zero-bit SL(2, Z) Gramian`) is classified into three strict disjoint columns — **(Column I) Unconditionally Derived (`0 knobs, 0 bits`)**, **(Column II) Conditional Same-Action Reduction (`stated structural premise`)**, and **(Column III) Explicit Remaining Discrete Bit / Continuous Ratio** — are all column counts and cross-references exact and internally consistent?
3. **Question `4C` (`Repaired Blind-Sealed 0-of-19 Prediction Vector & Post-RGE U(3)^6 Haar Gate`):**
   - On the Casimir-stabilized reference state (`both classical 6*pi and 1-loop Casimir A_Cas^*, and across Majorana weights (1, 1, 1) vs Petersson unit-norm`) alongside the `0`-bit universal `UR-1..UR-7` corridors and `0`-bit Frame C Gramian ratios, are all extracted dimensionless observables invariant under `10` independent `24`-digit $\mathrm{U}(3)^6$ Haar basis rotations to `< (1/1000)^5` (`and < (1/1000)^5` under `12`-factor full $\mathrm{U}(3)$ Fujikawa strong-CP rotations)?

---

## 2. Deliverables and Definition of Done

1. **`Part 4A`:** Complete `1320`-history (`UR-1, UR-2`) and `288`-UV / `248`-IR (`UR-3..UR-7`) side-by-side `old vs repaired` census with outward-rounded exact rational kill-line corridors and maximum shift ledger.
2. **`Part 4B`:** Machine-verified `3`-column input/deformation accounting matrix covering all `10` structural subsystems audited across `X-ENDGAME`, `X-RELATIONS`, `physical`, and `agy-002`.
3. **`Part 4C`:** Complete repaired blind-sealed `0 of 19` dimensionless prediction vector (`reference vacuum + 0-bit universal corridors + Petersson-normalized comparison`) and `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance verification.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_RepairedUniversalCensus_UR1_to_UR7_Gate` (`Part 4A`):** Repaired `4`-pillar `RGE` benchmark gate (`including exact 11/2 coefficient`) passes; across all `1320` perturbative gauge/scalar histories, `I_gauge` stays inside `[3129/1000000, 4693/1000000]` (`[4028/1000000, 4205/1000000]` on all `264` `3D`-cover histories) with `max |repaired - old| < (1/1000)^4`, and `lambda_IR > 42/1000 > 0` with `max |repaired - old| < (1/1000)^2` on `sqrt(2*lambda_IR)`; across all `248` meridian-active (`3a notin Z`) vacua at Levels `5, 10, 15`, `0` divergences occur, `max |repaired - old| < (1/1000)^2`, amphichiral `6x6` phase `< (1/1000)^4` rad across all `288` UV and `248` IR vacua, and `UR-7` `sec4_r12 > 1/4` on all `180` Level-`5/15` vacua with `sec4_r23 < 1/1000` on all `248` vacua.
2. **`E2_ThreeColumnInputDeformationMatrix_Gate` (`Part 4B`):** All `10` audited subsystems partition cleanly into Columns `I, II, III` with zero unpriced selections, zero literal flags, and exact match to the numerical tests in Stages `1–4`.
3. **`E3_RepairedZeroOf19Vector_and_Haar6_Gate` (`Part 4C`):** Complete repaired dimensionless `0 of 19` vector agrees between `f64` and `32`-digit `mpmath` to `< (1/1000)^4`, satisfies `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar invariance to `< (1/1000)^5`, and confirms `< 1/1000` shift between `6*pi` and `A_Cas^*`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage4_Bridge_Passed`:** `AST` check confirming zero disallowed imports and zero float literals or `sqrt(3)` calls inside target-free geometry and rational-exponent functions.
2. **`PC_BR4_ReversedMixedYukawaOrder`:** Un-transposed right-acting product order fails the `11/2` `PRD 47, 2038` + `BPV` `2`-loop mixing derivative by `> 1/100`.
3. **`PC_BR4_WrongHyperchargeAndExtraHiggs`:** Replacing `k_2/k_1 = 3/5` by `1` shifts `sin^2 theta_EW` by `> 8/100`, and `N_H = 5` violates `1`-loop `L_gauge = 0` by `> 1`.
4. **`PC_BR4_OmitHeisenbergCoverLiftAndWrongCRT`:** Naive `(a, 1 - b)` without Heisenberg cover lift breaks `UR-6` by `> 2` rad, and `3w mod 1` instead of `6w mod 1` breaks Level-`15` `CRT` triality by `> 3/10`.
5. **`PC_BR4_RightActingRGEHaarViolation`:** Placing `1`-loop Yukawa matrices on the right of `Y_f` breaks $\mathrm{U}(3)_R$ Haar singular-value invariance by `> 1/1000`.

`0 of 19.`
