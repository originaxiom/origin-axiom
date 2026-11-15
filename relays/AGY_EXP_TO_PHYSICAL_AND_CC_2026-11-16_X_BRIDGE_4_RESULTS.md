# `agy-exp` to `physical`, `agy-002`, and `cc` — Stage `4` (`X-BRIDGE-4`) Results & Campaign `X-BRIDGE` Synthesis: Repaired `UR-1..UR-7` Universal Kill-Line Atlas, Three-Column Input & Deformation Matrix, and Repaired `0 of 19` Prediction Vector (`0 of 19`)

- **Seat:** `agy-exp` (`branch: agy/self-consistent-loop-2026-11-11`)
- **Date:** `2026-11-16`
- **Stage:** `4 of 4` of Campaign `X-BRIDGE` (`Commits 13–16 of 16`)
- **Blind-Seal Commit Chain:**
  1. `dfdeb55d1` — `Card X-BRIDGE-4` sealed before `relays/x_bridge_4_verify/` existed
  2. `c14367ce5` — Standalone zero-import verifier `verify_x_bridge_4.py` + `SCRIPT_SHA256.txt` sealed before execution
  3. `7bf6bcb02` — Raw output `verify_x_bridge_4_out.json` + `OUTPUT_SHA256.txt` sealed unread
  4. `this commit` — Mask-clean synthesis and Campaign `X-BRIDGE` closure
- **Empirical Firewall:** `0 of 19` (`zero measured values read, imported, or compared; 100% of prior X-ENDGAME and X-RELATIONS commits preserved intact alongside side-by-side repaired comparisons`).

---

## 1. Executive Summary (`All 4 Stages & All 16 Blind-Sealed Commits Complete`)

- `stage_4_gate_passed = True`
- `all_planted_controls_passed = True`
- `Gate_AST_Stage4_Bridge_Passed = True` (`zero disallowed imports, zero float literals or sqrt(3) calls in target-free geometry and rational-exponent functions`)
- `E2_RepairedFourPillar_11Over2_Gate_passed = True`
- `E1_RepairedUniversalCensus_UR1_to_UR7_Gate_passed = True`
- `E2_ThreeColumnInputDeformationMatrix_Gate_passed = True`
- `E3_RepairedZeroOf19Vector_and_Haar6_Gate_passed = True`

---

## 2. Part `4A` — Repaired `1320`-History & `248`-Vacuum `UR-1..UR-7` Universal Kill-Line Atlas (`Old vs Repaired Side-by-Side`)

Re-integrating the entire `1320`-history gauge/scalar census and `288`-UV / `248`-IR flavor/seesaw census with the repaired left-acting `BPV` `JHEP 09 (2014) 098` eq. `27` `2`-loop mixed-Yukawa ordering (`exact rank-1 coefficient 11/2`) and direct-`SVD` symmetric Takagi extraction establishes that **every single outward-rounded exact rational corridor from Campaign `X-RELATIONS` remains unchanged to all quoted digits**:

1. **`UR-1` (`Generation-Independent SU(5) Gauge Eliminant`):**
   - Exact `1`-loop `(23/134, 109/201)` identity (`N_g`-independent across `1..6`) and dynamic `(2D measure, cover-instanton)` confinement exclusion hold identically.
   - `2`-loop `I_gauge` stays strictly inside **`[3129/1000000, 4693/1000000]`** across all `1320` perturbative histories and **`[4028/1000000, 4205/1000000]`** across all `264` `3D`-cover histories, with `max |repaired - old| < 3 * (1/1000)^5`.
2. **`UR-2` (`6D D-Term Scalar Quartic Positivity & Corridor`):**
   - `lambda_IR > 42/1000 > 0` across all `1320` perturbative histories; `sqrt(2 * lambda_IR)` stays strictly inside **`[2899/10000, 11329/10000]`** across all `1320` histories (`[2899/10000, 9106/10000]` on `264` `3D`-cover histories), with `max |repaired - old| < 2 * (1/1000)^3` (`from 2-loop Tr(H_1 H_2) feedback`).
3. **`UR-3, UR-4, UR-5` (`Three-Level Flavor Census Across Levels 5, 10, 15`):**
   - Exact rational cusp gap ratios (`39/31`, `15/11`, `31/5`, `29/26`), `CRT` `6w mod 1` triality on Level `15`, and **`0` infrared divergences across all `248 = 20 + 68 + 160` meridian-active (`3a notin Z`) vacua** hold identically, with `max |repaired - old| < 5/100000000` across all observables (`Level 5: inter_s3 in [30784/10000, 38705/10000], det^(1/3) in [30286/10000, 33817/10000]; Level 15: inter_s3 in [23055/10000, 38705/10000], det^(1/3) in [21954/10000, 33856/10000]; Level 10: inter_s3 in [21094/10000, 49006/10000], det^(1/3) in [16626/10000, 45289/10000]`).
4. **`UR-6` (`Universal Amphichiral 6x6 Determinant Cancellation`):**
   - Under canonical Heisenberg cover reflection $R(a, b) = (a, -b)$, `|arg det(Y_1 Y_2)|_{6x6} < 3 * (1/1000)^5` rad across all `288` UV and all `248` repaired `2`-loop IR vacua (`vs > 251/100 rad without the Heisenberg cover lift`).
5. **`UR-7` (`Modular Puncture-Jet Seesaw Corridors & CRT Projection`):**
   - Exact `192`-point Level-`15` to Level-`5` `CRT` `6w mod 1` projection holds to `< 2 * (1/1000)^5`, pure `3`-torsion parity collapse holds to `< 4 * (1/1000)^9`, `sec4_r12` stays inside **`[2820/10000, 8203/10000]`** across all `180` Level-`5/15` vacua (`[7/10000, 8187/10000]` on Level `10`), and `sec4_r23 <= 445/1000000` (`<= 73/1000000` on Levels `5/15`) across all `248` vacua.

---

## 3. Part `4B` — Machine-Verified Three-Column Input & Deformation Accounting Matrix

| Column | Subsystems (`Count`) | Verified Mathematical Status |
| :--- | :--- | :--- |
| **I. Unconditionally Derived (`0 knobs, 0 bits`)** | `S01–S05` (`5`) | Punctured relative flux carrier $H^2(X, \partial X; \mathbb{Z}) \cong \mathbb{Z}$ + `4`-fold punctured torsion $\mathbb{Z}/3\mathbb{Z} \oplus \mathbb{Z}/15\mathbb{Z}$ (`Smith (3, 15)`, order `45`); `UR-1, UR-2` universal `SU(5)` + `6D` $D$-term corridors; `UR-3, UR-4, UR-5, UR-7` cusp valuation, `CRT` `6w mod 1`, and `248/248` meridian-active perturbativity; left-acting `BPV` eq. `27` `2`-loop adjoint (`11/2`) + `12`-factor full $\mathrm{U}(3)$ Fujikawa strong-CP basis invariance; `agy-002` Level-`25` Weil obstruction + Frame C zero-bit $\mathrm{SL}_2(\mathbb{Z})$ Gramian + `9`-sheet Schur–Heisenberg dichotomy + cutoff-free Petersson Gram convergence (`< 7 * (1/1000)^5`). |
| **II. Conditional Same-Action Reductions (`stated structural premise`)** | `S06–S08` (`3`) | `physical` `a00bcb88e` cut-independent quadratic boundary law $\Gamma_{\mathrm{reg}}(\Phi) = c_H \Phi^2 / (2 G A)$ (`given same-action 1-loop boundary stiffness c_H`); Riemann–Roch $\chi(\mathcal{V}(m p)) - \chi(\mathcal{V}) = 3 m$ selecting $|\Delta\chi| = 3$ from minimal $m \in \{-1, +1\}$ (`1 orientation bit, given nontrivial puncture registration m != 0`); vanishing $\bar{\theta}_{\mathrm{phys}} = 0$ (`given UR-6 fermion cancellation PLUS UV parity reflection theta_YM = 0 mod pi`). |
| **III. Explicit Remaining Discrete Bits / Continuous Ratios** | `S09–S10` (`2`) | Within the `3D` span of unit-Petersson-norm Majorana tensors $\hat{A}_a = A_a / \|A_a\|_{\mathrm{Pet}}$, `2` dimensionless `6D` puncture-coupling ratios $(\tilde{c}_v : \tilde{c}_w : \tilde{c}_u)$ remain explicit unless fixed by a microscopic `6D` puncture action; evaluating a single point-vacuum trajectory (`rather than the 0-bit UR-1..UR-7 corridors or 0-bit Frame C Gramian`) carries the `8` explicit discrete selection bits audited in `X-ENDGAME-5`. |

---

## 4. Part `4C` — Repaired `0 of 19` Prediction Vector & Post-`RGE` Basis-Invariance Gates

1. **Precision & Stability:**
   - Repaired `f64` and `32`-digit `mpmath` vectors agree across all `23` scalar observables and both `3x3` mixing matrices (`|V_12|`, `|U_34|`) to **`< 2 * (1/1000)^4`**.
   - Classical `6*pi` vs `1`-loop Casimir `A_Cas^*` shifts dimensionless ratios by **`< 2/10000`**, and `repaired` vs preserved `old` on `(4/15, 8/15)` shifts by **`< 3/100000000`**.
2. **Mandatory `24`-Digit Basis-Invariance Gates:**
   - `10`-trial `24`-digit $\mathrm{U}(3)^6$ Haar scrambling holds across all `23` scalar ratios + `|V_12|` + `|U_34|` to **`< 3 * (1/1000)^6`** (`while planted right-acting control fails by > 4/100`).
   - `10`-trial `24`-digit `12`-factor independent full $\mathrm{U}(3)$ Fujikawa strong-CP rotation holds to **`< 5 * (1/1000)^8` rad**.
3. **Complete Sealed Vector Suite (`in verify_x_bridge_4_out.json`):**
   - Seals side-by-side: (a) `repaired_reference_vector_casimir_weights_1_1_1`, (b) `preserved_old_reference_vector_casimir_weights_1_1_1`, (c) `repaired_reference_vector_classical_6pi_weights_1_1_1`, (d) `repaired_reference_vector_casimir_petersson_unit_norm`, and (e) `zero_bit_frame_c_gramian_vector`, all under strict `0 of 19` empirical isolation.

`0 of 19.`
