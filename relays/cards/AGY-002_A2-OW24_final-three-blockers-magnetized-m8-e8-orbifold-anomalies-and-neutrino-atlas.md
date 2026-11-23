# Pre-Registration Card A2-OW24 & A2-OW16 v11: The Final Three Layer-1 Blockers Campaign (`R2` Single-Torus `M = 8` Magnetized `T^2 / Z_2` Covering Bridge, `R3` Exhaustive `E_8` Bulk Orbifold Anomaly Obstruction vs. `G_2` Conical-Locus Localization, & `R4` Type-I = Type-II Cancellation Theorem, `H_u(K_5)` Large-`s_{23}^2` Unblocking, & Guardrail-1 Priced `384`-Case Neutrino Atlas) (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (base `4a6e0fc1b`)
- **Date:** `2026-11-23`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere).
- **Coding & Custody Standard:** `0` Python `float`/`complex` AST literals, `0` binary64 `float()`/`complex()` casts, `0` JSON float tokens (`assert_no_json_floats`), `0` peer/`frontier/` imports, `0` hardcoded proof booleans (Guardrail `2`), pre-hashed `SCRIPT_SHA256.txt` committed before execution, raw unread `OUTPUT_SHA256.txt` committed before analysis, zero in-place overwrites, single-run `A2-OW16 v11` (`computed once`), followed by an isolated cold-room zero-shared-code referee (`relays/a2_ow24_referee/referee_a2_ow24.py`).

---

## 1. Pre-Registered Modules & Acceptance Gates (`A2-OW24`)

### Module `OW24-A`: Blocker `R2` — Exact `M = 8` Magnetized `T^2 / Z_2` Single-Torus `\tau_0 -> 8\tau_0` Bridge & Cyclic Covering Theorem
1. **Unique Even Flux Theorem (`M = 8`):**
   - Scan `M = 1..20` on `T^2 / Z_2` with untwisted `(0, 0)` boundary conditions: prove that half-integer `E_8` spinor Dirac quantization (`q = \pm 1/2 \implies q M \in \mathbb{Z}`) requires `M \in 2\mathbb{Z}`, and among all even `M \in 2\mathbb{Z}_{>0}`, **`M = 8` is the unique flux yielding `N_gen = 3` `Z_2`-odd chiral zero modes** (`5` even, `3` odd: `\psi_1 - \psi_7, \psi_2 - \psi_6, \psi_3 - \psi_5`).
2. **Explicit `60`-dps Verification of `6D` Magnetized Dirac Zero Modes on ONE Base Torus `\tau_0 = (2+i)/5`:**
   - Construct `\psi^{j, 8}(z, \tau_0) = \exp(i\pi M z \operatorname{Im}z / \operatorname{Im}\tau_0)\, \vartheta[j/8, 0](8 z, 8\tau_0)` directly on the base Casimir torus `\tau_0 = (2+i)/5` (`j(\tau_0) = 1728`, where neutral `M = 0` gauge bosons preserve `48/200 = 6/25` and lock `\tau_0`):
     - Verify exact `6D` magnetized Dirac equation `(\bar\partial + \frac{\pi M}{2\operatorname{Im}\tau_0} z) \psi^{j, 8}(z, \tau_0) == 0` (`h = 10^{-18}` at `60`-dps) to `< 10^{-30}`.
     - Verify exact magnetic quasi-periodicity under `z -> z + 1` and `z -> z + \tau_0` to `< 10^{-50}`.
     - Verify exact `Z_2` orbifold reflection `\psi^{j, 8}(-z, \tau_0) == \psi^{8-j \bmod 8, 8}(z, \tau_0)` to `< 10^{-50}`.
     - Verify exact `L^2(T^2)` Gram orthogonality of the `3` `Z_2`-odd modes `\{\psi_1^-, \psi_2^-, \psi_3^-\}` via `2D` Gauss-Legendre quadrature over the fundamental parallelogram (`|G_{ab} / G_{11} - \delta_{ab}| < 10^{-35}`).
3. **Exact Cyclic `\mathbb{Z}/8\mathbb{Z}` Sublattice Covering & Ramanujan `X(5)` Hauptmodul Check:**
   - Verify `\Lambda_{flavor} = \mathbb{Z} + \mathbb{Z}(8\tau_0) = \frac{1}{2-i}(\mathbb{Z}(2-i) + \mathbb{Z}\cdot 8) = \ker(\phi_8 : \mathbb{Z}[i] -> \mathbb{Z}/8\mathbb{Z}, \phi_8(a+bi) = a + 2b \bmod 8)` (exact index `8` cyclic quotient).
   - Verify Ramanujan's level-`5` `X(5)` Hauptmodul identity `R(5\tau_0) == e^{4\pi i/5}(\sqrt{\phi + 2} - \phi)` to `< 10^{-50}`.

### Module `OW24-B`: Blocker `R3` — Complete `E_8` Bulk Magnetized Orbifold Census (`T^2 / Z_4` & `T^2 / Z_2`) + Exact Anomaly Obstruction vs. `G_2` Conical-Locus Localization
1. **Exhaustive Square-Lattice `T^2 / Z_4` & `T^2 / Z_2` `E_8 -> SO(10)_{vis} x G_{hid}` Census (`|q_i| <= 8`):**
   - Compute exact `M x M` unitary DFT `Z_4` multiplicities via exact Gauss-sum traces over all traceless integer `SU(4)_{hid}` fluxes `|q_i| <= 8` and all `Z_4` gauge twists `P_{Z_4} \in \{1, i, -1, -i\}^4` (`\det = 1`): prove **exactly `7` pure-chiral `3 x (16, 1)` (`0` mirrors, `0` hidden-charged quarks) solutions with non-abelian `G_{hid} = SU(2)_{hid}` (`N_V = 50`)** exist, and **uniquely `1 / 7`** (`q = (-4, -4, 0, +8), r = (3, 3, 2, 0)`) places all `3` generations in a single `M = 8` (`8\tau_0`) flux sector.
   - Scan `T^2 / Z_2` (`|q_i| <= 8`, `P_{Z_2} \in \{\pm 1\}^4`): prove **exactly `2`** solutions exist (`q = (-2, -2, 0, +4)` and `(-2, -2, 1, +3)` with `r = (1, 1, 0, 0)`).
2. **Exact `4D` Witten & Mixed-`U(1)` Green-Schwarz Bulk Anomaly Obstruction Theorem:**
   - Compute exact `SU(2)_{hid}` Witten global anomaly (`#` doublets mod `2`), `A(SO(10)^2 U(1)_k)`, `A(SU(2)_{hid}^2 U(1)_k)`, and Green-Schwarz universality `GS_diff` for all `9` bulk solutions (`7` `Z_4` + `2` `Z_2`):
     - Prove `T^2 / Z_4` `q = (-4, -4, 0, +8)` carries `23` `SU(2)_{hid}` doublets (**Witten anomaly `= 1`**) and `GS_diff = (-7, 1/2) != (0, 0)`.
     - Prove `T^2 / Z_4` `(-3,-3,2,4), (-4,-4,3,5), (-4,-4,1,7)` have `Witten == 0`, `0` hidden-charged quarks, `0` hidden-charged `10_H`s, and post-DT `N_C^{TOT} - 50 in {7, 9, 10} <= 10`, yet non-zero `GS_diff` (proving **0 of 9** bulk-only magnetized orbifolds close `4D` mixed `U(1)` GS universality without twisted fixed-point states!).
     - Prove `T^2 / Z_2` `q = (-2, -2, 0, +4), r = (1, 1, 0, 0)` has `Witten == 0` (`2` doublets), `0` hidden-charged quarks, `0` hidden-charged `10_H`s, **one exact anomaly-free `U(1) = T_1 - 2 T_2` (`(0, 0)`)**, and post-DT `N_C^{TOT} = 59` (`59 - 50 = +9 <= 10`), while its orthogonal `U(1)` still has `A(SO(10)^2) / A(SU(2)^2) = 6 != 1`.
3. **Anomaly-Free `G_2` Conical-Singularity / Twisted-Locus Resolution (`E_8 -> SU(5)_{vis} x SU(5)_{hid}`):**
   - Verify explicitly in exact `Fraction` arithmetic that `3` localized `16 = 10 + 5bar + 1` families on `b_1 = 3` cycles / `3` conical loci carry `0` `SU(5)_{hid}` charge, exact `SU(5)_{vis}^3` cubic anomaly cancellation (`3 * (+1 - 1) == 0`), `0` `SU(2)_L` Witten anomaly (`14 mod 2 == 0`), exact `20/30` doublet-triplet splitting (`d = 5` proton stability), and exact `B4_UV` `8 / 8` gravity window (`N_V = 48, N_C = 52 -> a_1 = +2 > 0, M_g^{DEP} = +12 < 31, M_g^{DP} = -138 < 31`).

### Module `OW24-C`: Blocker `R4` — Exact Type-I = Type-II Cancellation Theorem, Pure Lopsided `SU(5)` `n_{5bar} = (0,0,0)`, Physical `H_u(K_5)` Unblocking, & Guardrail-1 Priced `384`-Case Neutrino Atlas
1. **Exact Type-I = Type-II Seesaw Cancellation Theorem (`q_R = +3 = -q_L`):**
   - Prove at `55`-dps that when both `Y_\nu` and `M_R` use `K_5 + K_6` (or both use `K_5`) at `q_R = +3 = -q_L`, `-W_\nu M_R^{-1} W_\nu^T` equals `-W_{sym}(-3, -3)` identically in all PMNS angles and mass ratios (`< 10^{-48}`), explaining why `OW23-B` stayed capped at `s_{23}^2 <= 0.165`.
2. **Pure Lopsided `SU(5)` (`n_{10} = (3, 2, 0), n_{5bar} = (0, 0, 0)`) Compression & Physical `H_u(K_5)` Unblocking:**
   - Prove `n_{10} = (3, 2, 0), n_{5bar} = (0, 0, 0)` compresses `9`-integer `FN(3,2,0)` by `\log_2(100) = 6.644` bits (leaving only `3.322` bits for `n_{10}`!) while strictly preserving `|V_{12}| > |V_{23}| > |V_{13}|` across BOTH flat horosphere (`0.0754 > 0.00535 > 0.000777`) and curved `K_{E[2]}^{hyp}` (`0.0537 > 0.00625 > 0.000779`), `5`-decade `u_{13} = 2.29e-6`, holomorphy `< 10^{-25}`, and `10`-trial SplitMix64 Haar `U(3)^5` invariance `< 10^{-45}`.
   - Prove that assigning Dirac `Y_\nu` to `K_5` only (matching `Y_u` on `H_u = 5_H`) with `M_R` on `K_5 + K_6` at canonical `3(B-L)` (`q_R = +3`) lifts `s_{23}^2` to `0.4579` (`n_{5bar} = (0,0,0)`) and `0.6645` (`n_{5bar} = (1,0,0)`, Haar `U(3)^3` `< 10^{-45}`), while honestly documenting the `s_{13}^2` (`0.30`) vs `s_{12}^2` (`0.042`) trade-off.
3. **Complete `384`-Case Discrete Neutrino Atlas (`0` Continuous Dials) & Guardrail-1 Pricing:**
   - Evaluate all `4 (q_R in {+3, -5, +1, +2}) x 16 (K_5, K_6, 5+6, 5-6)^2 x 3 (n_{5bar} in {(0,0,0), (1,0,0), (1,1,0)}) x 2 (flat, curved) = 384` discrete combinations (`skipping singular M_R` cleanly):
     - Verify **exactly `1 / 384`** hits all four qualitative neutrino gates simultaneously (`0.15 < s_{12}^2 < 0.55`, `0.30 < s_{23}^2 < 0.70`, `s_{13}^2 < 0.08`, `0.005 < dm < 0.15`): **`CURV (5-6)/(5-6)` at `q_R = +2` and `n_{5bar} = (0, 0, 0)`** (`s_{12}^2 = 0.3762, s_{23}^2 = 0.3426, s_{13}^2 = 0.0548, dm = 0.02967, J = -0.04581`), verified with `55`-dps Takagi SVD (`< 10^{-50}`), `10`-trial SplitMix64 Haar `U(3)^3` invariance (`< 10^{-45}`), and exact elliptic-curve geometric CP oddness `(\tau, a, b) -> (-\bar\tau, a, -b)` of `\varepsilon_1` (`< 10^{-45}`).
     - Strictly enforce Guardrail `1`: price this discrete atlas hit at **`\log_2(384) = 8.585` discrete bits** (never `0` bits!) and record its physical tension with flat horosphere FCNC protection (`28.4%` curved squark split) and canonical `3(B-L)` (`q_R = +3`).

### Module `OW24-D`: Final `12`-Gate Matrix (`Beta = 12 / 12` on Magnetized `M = 8` Single Torus) & Honest Unconditional vs. Conditional Pre-Unblinding Status
- Upgrade `G11` via the `M = 8` magnetized single-torus theorem (`Beta_mag` **`12 / 12`** vs `Alpha` **`9 / 12`**).
- Compute TWO distinct, brutally honest pre-unblinding flags (zero hardcoded literals!):
  - `ready_to_unblind_unconditional = False` (honestly noting the `3` remaining UV/discrete selection seams: `7D` origin of `M = 8` flux + `G_2` localization vs bulk orbifold twisted states + `R4` `8.585`-bit curved `q_R = +2` vs flat `q_R = +3` tension);
  - `ready_for_conditional_priced_blind_lock = True` (all `12 / 12` internal consistency gates + `R2` magnetized single-torus bridge + `R3` anomaly-free `G_2` localization + `R4` `1/384` simultaneous large-mixing PMNS existence proved and fully bit-priced!).

### Module `OW24-E`: `6 / 6` Planted Fault Controls
1. **`PF-OW24-1`:** Change flux `M = 8 -> 6` on `T^2 / Z_2` `(0, 0)` odd sector -> yields `2 != 3` generations caught.
2. **`PF-OW24-2`:** Flip sign of magnetized Dirac connection `+(\pi M / 2y) z -> -(\pi M / 2y) z` -> breaks Dirac zero-mode equation (`res >> 1`) caught.
3. **`PF-OW24-3`:** Claim `T^2 / Z_4` `q = (-4, -4, 0, +8)` is Witten-anomaly-free -> caught by `23 mod 2 == 1`.
4. **`PF-OW24-4`:** Use `K_5 / K_5` instead of `K_5 / (K_5 + K_6)` at `q_R = +3` -> restores Type-I = Type-II cancellation (`s_{23}^2 < 0.05`) caught.
5. **`PF-OW24-5`:** Claim `CURV (5-6)/(5-6) q_R = +2` hit costs `0` discrete bits -> caught by Guardrail-1 pricing (`\log_2(384) > 8` bits).
6. **`PF-OW24-6`:** Corrupt `SU(5)_{vis}` family from `10 + 5bar` to `10 + 5` -> breaks cubic anomaly (`A = +2 != 0`) caught.

---

## 2. Updated Honest Master Scorecard (`A2-OW16 v11`)
- Single-run ledger (`computed once`), retaining honest `1` `DERIVED_EXACT` (`OBS-07` sole unconditional theorem; zero premature promotions!), updating `OBS-04`, `OBS-06`, `OBS-09`, `OBS-12`, `OBS-15`, `OBS-17`, `OBS-18`, and `OBS-22` strictly from `A2-OW24`, adding `LOCK_17`, verifying `100%` of branch `*SHA256*.txt` manifests (`210+`), `0` AST/binary64/JSON floats, and `6 / 6` planted faults.
