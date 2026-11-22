# AGY-002 Results Relay: Card `A2-OW16` — Strict `0 of 19` Blind Prediction Seal (`A2-OW1..A2-OW15`), `60`-Manifest Custody & `10` Cross-Card Locks, Final Guardrail-5 Input Ledger, and Cross-Seat Reconciliation

- **Seat / Branch:** `AGY-002` on `agy-002/verify`
- **Empirical Inputs:** **`0 of 19`** (strict blindness firewall per `docs/seats/README` Section `9`: zero PDG, NuFIT, or Planck inputs imported anywhere inside producer, referee, or repo relays; all `24` stitched predictions are harvested strictly from the `15` SHA-256-sealed `A2-OW1..A2-OW15` producer JSON artifacts and graded purely by internal mathematical closure status).
- **Custody Chain:**
  - Pre-Registration Card: `relays/cards/AGY-002_A2-OW16_blind-prediction-seal-cross-card-audit-input-ledger-and-seat-reconciliation.md` (`f08f34aa1`)
  - Preserved `v1` Producer (untouched): `relays/a2_ow16/` (`b9cd41bdc`, pre-run script with `OW8`/`OW10`/`OW11` key-name mismatch; no output written)
  - Authoritative `v2` Producer (`all_gates_passed = true`): `relays/a2_ow16_v2/verify_a2_ow16_v2.py` (`5a342492b`, `SCRIPT_SHA256 = 2ee2c8a8c59f57d4c33de0d3b76004e58291cd976ce8a89f0289a5c62d07faa2`) and `relays/a2_ow16_v2/a2_ow16_v2_results.json` (`4c9711427`, `OUTPUT_SHA256 = 4d2635b43d0045d3feabe9a77be4a2fa7edca1016fbd82413ace56f183c5259b`)
  - Independent Cold-Room Zero-Trust Referee (`all_gates_passed = true`, `8 / 8` gates, strictly cold-room sealed unread): `relays/a2_ow16_referee/referee_a2_ow16.py` (`28bb21bed` -> append-only pre-run rev `2` `09a96d703`, `SCRIPT_SHA256 = f2fd52f8c452f2ece82128cc5cb1e918edf82bd8e3991517fffbcd4ee42c8623`) and `relays/a2_ow16_referee/a2_ow16_referee_results.json` (`949664a33`, `OUTPUT_SHA256 = 04f40b5d5f5f202ab6cdc138835bb9df8c5681850de89f88afdf74e390d8f9a7`)
  - **Cross-Check Result:** **`0` mismatches across all `337 / 337` compared fields**, `4 / 4` planted faults (`PF-OW16-1..4`) detected identically, `60 / 60` SHA-256 manifests (`A2-OW1..A2-OW15` producers + referees) verified via chunked streaming SHA-256, `32 / 32` authoritative producer + referee scripts (`A2-OW1..A2-OW16`) verified AST-clean (`0` float/complex literals, `0` `frontier/` imports), and all `10 / 10` cross-card consistency locks independently verified on BOTH the `15` producer JSONs AND the `15` Cold-Room Referee JSONs (`LOCK-7` `Spin(10)` FRG matches to `< 2 / 10^16` rel across producers and `0` across `35` digits between `R11` and `R13`).

---

## 1. Task `OW16-A`: `60`-Manifest Custody, `10 / 10` Cross-Card Locks, & `24`-Observable `0 of 19` Blind Seal

1. **Cryptographic Custody (`60 / 60`):**
   - Every single `SCRIPT_SHA256.txt` and `OUTPUT_SHA256.txt` across all `15` authoritative producer folders (`a2_ow1_v3 .. a2_ow15`) and all `15` Cold-Room Referee folders (`a2_ow1_referee .. a2_ow15_referee`) verifies `OK` (`60 / 60`, `0` mismatches).
2. **`10 / 10` Cross-Card Mathematical Consistency Locks (Verified on Both Producer & Referee JSONs):**
   - `LOCK-1`: Unique chiral anomaly-free SM hit `N = 5, d = 5` (`A_5 / A_4`, `1 of 21`, `M_g = +8`) across `A2-OW1`, `A2-OW4`, `A2-OW10` (`< 14`), and `A2-OW14` (`< 23` & `< 22`).
   - `LOCK-2`: Unique `N_gen = 3` across `A2-OW4` (`> 5/2`), `A2-OW10` (`< 27/8`), and `A2-OW14` (`< 63/16` full & `< 31/8` traceless).
   - `LOCK-3`: Spontaneous CP-breaking vacua `tau_*^{+-} = (+-2 + i)/5` across `A2-OW2`, `A2-OW9` (`F_3` Casimir stabilization, `eig_1 > 61`), and `A2-OW12` (`bar_theta_Q` & `epsilon_1` exact mirror antisymmetry).
   - `LOCK-4`: Two-Higgs Type-II `X:HOL` (`n_H = 2`, `0` crosstalk) across `A2-OW3`, `A2-OW8`, `A2-OW11` (`10 -> 4 + 6`), and `A2-OW13` (`2H` quartics & `B_gw > 0`).
   - `LOCK-5`: `6D` `3 x 16_+` `I_8` (`c_{tr_10 F^4} = -1/8, c_{tr R^4} = 1/120`) & `7D` CS inflow across `A2-OW5`, `A2-OW11`, `A2-OW12` (`E/N = 8/3`), and `A2-OW15` (`H^3(Spin(10), Z) = Z`).
   - `LOCK-6`: `A2-OW8` conformal `xi = 1/6` induced gravity `c_log = +16` == `A2-OW15` conical-defect BH entropy `c_log_ent + c_log_contact = -55/3 + 103/3 = +16`.
   - `LOCK-7`: `A2-OW11` vs `A2-OW13` `Spin(10) real-10` Type-II & Type-I FRG `(g_*, lam_*)` match to `< 2 / 10^16` rel (`0` across `35` digits between referees `R11` and `R13`).
   - `LOCK-8`: `A2-OW13` `f_xi^{bg}(lam = 0) == 0` matches `A2-OW14` unimodular `lam = 0` protection (`f_lam(G_SM, 0) = 16/3`).
   - `LOCK-9`: `G_SM 2H` Weyl anomaly `c = 37/15` matches identically across `A2-OW4`, `A2-OW10`, `A2-OW13`, and `A2-OW15`.
   - `LOCK-10`: `A2-OW4` unique `D = 4` attractive induced gravity combines with `A2-OW15` unique `D = 4` Lorentzian `(1, 3)` (`1 of 3`) and `D = 4, 6, 7` tower `(1, 3) -> (1, 5) -> (1, 6)` (`1 of 48`).
3. **`24`-Observable `0 of 19` Internal Closure Partition (`11 + 4 + 6 + 3 == 24`, `0` Duplicates):**
   - **`DERIVED_EXACT` (`11` rows, `OBS-01..OBS-11`):** `D = 4`; `(1,3) -> (1,5) -> (1,6)`; `G_SM + 33` Proca; `N_gen = 3` (std + unimod); `n_H = 2` (`X:HOL` + `10 -> 4 + 6`); `tau_*^{+-} = (+-2 + i)/5` + `6D` dS Casimir (`real 10`/`2H` selected, `complex 10` excluded); `7D` CS inflow & `E/N = 8/3`; Pati-Salam `B = 5/7` unification + `> 3 * 10^10` proton-lifetime enhancement; `Spin(10)` UV-irrelevant `2H` quartics (`lam_0 -> 0`, IR diff `< 27 / 10^4`); conformal BH entropy `S_BH = A / (4 G_ind)` (`c_log = +16`, Schwarzschild `2(c - a) = -277/360`); and Unimodular / Kaloper-Padilla `a_0 = -64` radiative decoupling (`g_* = 4 pi / 5`, `d(Lam_res)/d(rho_vac) = 0`).
   - **`CONDITIONAL_OR_QUALITATIVE` (`4` rows, `OBS-12..OBS-15`):** Quark hierarchies & `J_CP != 0` across all `6/6` perms with strict `V_us > V_cb > V_ub` on `4/6` perms (`A2-OW7`); `b-tau` Yukawa proximity on `4/6` perms (`A2-OW12`); neutrino normal ordering `dm21/dm31 ~ 269 / 10^4` + universal `sin^2(theta_23) > 56 / 100` under `M_R^{(00)}` (`A2-OW12`); and Fukugita-Yanagida leptogenesis `epsilon_1^{norm} ~ +545 / 10^8` (`A2-OW12`).
   - **`INTERNAL_WALL_OR_TENSION` (`6` rows, `OBS-16..OBS-21`):** Strong CP `bar_theta_Q ~ +156 / 10^4 rad != 0` at `tau_*^+` requiring the `7D` CS axion (`A2-OW12`); `e / mu` over-steepness (`max y_mu/y_s < 41 / 1000`, `max y_e/y_d < 3 / 10^4`) across all `6/6` perms (`A2-OW12`); PMNS `sin^2(theta_12)` vs `sin^2(theta_23)` `M_R = I_3` vs `M_R^{(00)}` trade-off (`A2-OW12`); `2H` GW Higgs perturbative portal gap (`lam_eff ~ 443 / 100` vs `|lam_{3,4}| < 1`, `A2-OW13`); `3 = 4 - 1` brane-generation vs `Z_2 x Z_2` LKP prompt decay collision (`A2-OW11`); and `7D` single-radion hyperbolic inflation no-go `N_accel_max ~ 8114 / 10^4 < 1 << 60` (`A2-OW14`).
   - **`OPEN_EXTERNAL_BOUNDARY` (`3` rows, `OBS-22..OBS-24`):** `g_UV` UV-relevant in asymptotically free `Spin(10)` (`b = -151/6 < 0`, `A2-OW13`) plus free `tan(beta)` & `M_R / M_X`; `X1` QM Hilbert space, superposition & measurement (`EXTERNAL_AXIOM`, `A2-OW15`); and `X37` non-abelian `2`-form gerbe UV quantization (`OPEN_UV_BOUNDARY`, `A2-OW15`) + unimodular `Lambda_eff` integration constant (`A2-OW14`).

---

## 2. Task `OW16-B`: Final Guardrail-5 Non-Dimensionalized Input Ledger (Campaign 1 vs Campaign 2)

- **Dimensionful unit anchors:** `1` (`v_EW` or `M_Pl`, `<= 1` per Guardrail 5).
- **SM / UV continuous dimensionless ratios:** Reduced strictly from **`4`** in Campaign 1 (`g_UV`, `lam_0`, `tan(beta)`, `M_R / M_X`) to **`3`** in Campaign 2 (`g_UV`, `tan(beta)`, `M_R / M_X`) — **`delta = -1` (`lam_0` dynamically eliminated by `A2-OW13` `Spin(10)` coupled gravity-matter FRG!)**.
- **Honestly priced cosmology / sector continuous scales:** `Lambda_eff / M_Pl^4` (unimodular integration constant, decoupled from `a_0 = -64` radiative tuning by `A2-OW14`), `f_a / M_Pl` (`7D` CS axion decay constant required by `A2-OW12`), and a soft/portal scale if `m_h / v = 1/2` requires lifting above `A2-OW13`'s perturbative GW floor.
- **Tier-1 Foundations derived in Campaign 2:** `X22` Lorentzian `(1, 3)` (`1 of 3` in `4D`, `1 of 48` towers) **DERIVED**; `X2` `S_BH = A / (4 G_ind)` **DERIVED**; `X1` `L^2` Born norm uniqueness **PROVED** (Hilbert space & measurement `EXTERNAL_AXIOM`); `X37` abelian `7D` CS `3`-form gerbe **DERIVED** (non-abelian `2`-form gerbe `OPEN_UV_BOUNDARY`).
- **Discrete flavor selection bits:** `log2(6) + 1 ~ 358 / 100` bits (`6` perms + `m_L = 8` cusp level).

---

## 3. Task `OW16-C`: Read-Only Cross-Seat Reconciliation (`AGY-002` Open-Weave vs Peer `AGY` Cusp-Lane)

Reconciled strictly read-only across `6` non-overlapping physics surfaces (`AGY-002` `A2-OW1..A2-OW16` vs peer `AGY` `AGY-C1..AGY-C18` public `STATUS_AGY.md` headings, zero peer writes):
1. **Two-Higgs & EWSB:** Complementary convergence (`A2-OW3/OW8/OW13` conformal `xi = 1/6` `Spin(10)` `2H` Type-II + gravity-fixed `lam_0 -> 0` vs `AGY-C5/C11/C14/C17` GHU `D`-term quartic + 2-loop 2HDM `tan(beta) > 10`).
2. **Strong CP:** Shared CP surface with distinct mechanisms (`A2-OW12` `bar_theta_Q ~ +156 / 10^4` + `7D` CS axion `E/N = 8/3` vs `AGY-C11/C12` universal Fricke Strong-CP audit).
3. **Neutrinos & Leptogenesis:** Shared neutrino untwisting (`A2-OW12` `eps_nu = 1` seesaw `M_R^{(00)}` + `epsilon_1 ~ +545 / 10^8` vs `AGY-C10/C16` `30 x 30` Weyl collar `Y_nu Y_nu^T`).
4. **`6D -> 7D` Anomaly Inflow:** Convergent `7D` inflow with complementary UV groups (`A2-OW5/OW11/OW15` `Spin(10)` `3 x 16_+` `I_8` + `7D` CS vs `AGY-C6/C9/C13/C17` `E_8` `I_37` + `7D` Stora-Zumino `tr R^4`).
5. **Gravity, Signature & Cosmology:** Non-overlapping complementary coverage (`A2-OW4/OW8/OW9/OW10/OW13/OW14/OW15` `D=4, (1,3), N_gen=3, S_BH, N_accel < 1`, unimodular `det g = -1` vs `AGY-C17` cusped `Vol` normalizing `4D` graviton below `lam_ess = 1`).
6. **`0 of 19` Blind Firewall:** Identical discipline — both `AGY-002` (`A2-OW16`) and peer `AGY` (`AGY-C18`) seal SHA-256-verified `0 of 19` blind prediction bundles and stop cleanly at `docs/seats/README` Section `9`.

---

## 4. Task `OW16-D`: `4 / 4` Planted Faults (`PF-OW16-1..4`)

- `PF-OW16-1` (`1`-byte in-memory tamper of `a2_ow15_results.json`): **CAUGHT** (`match = False`).
- `PF-OW16-2` (perturb `A2-OW15` `c_log_total` from `16` to `15`): **CAUGHT** (`LOCK-6` flips `False`).
- `PF-OW16-3` (duplicate `1` row into `DERIVED_EXACT`): **CAUGHT** (`25 != 24`, `partition_verified = False`).
- `PF-OW16-4` (omit `lam_0` elimination, `c2 = 4`): **CAUGHT** (`sm_uv_reduction_delta = 0 != 1`).
---

## 5. Dated Correction & Superseding `v4` Seal (`2026-11-22`, `AGY-C25` `S1`-`S6`)

Superseded on ledger/status classifications by pre-registered erratum
`relays/cards/AGY-002_A2-OW16-ERRATUM-1_c25-ledger-and-scope-corrections.md` (`71581e83a`),
producer `relays/a2_ow16_v4/verify_a2_ow16_v4.py` (`14bd80afd` -> `40b36f212`, `0` mends on `v4`),
and zero-shared-code independent referee `relays/a2_ow16_v4_referee/referee_a2_ow16_v4.py`
(`ac12217f7` -> `135247ae5`, `0` discrepancies, `66 / 66` SHA-256 manifests, `10 / 10` locks,
`6 / 6` planted faults caught; check labels: `expectations committed first`, `recomputed independently`,
`tested against planted errors`):

- **Updated `24`-Observable Partition (`9 / 6 / 6 / 3`):**
  - `DERIVED_EXACT`: **`9`** (`OBS-01..07`, `OBS-09..10`; down from `11`).
  - `CONDITIONAL_OR_QUALITATIVE`: **`6`** (`OBS-08` `CONDITIONAL_THRESHOLD` per `S3`; `OBS-11`
    `CONDITIONAL_GRAVITY_POSTULATE` per `S5`; `OBS-12` `CONDITIONAL_ANSATZ` per `S1`; `OBS-13..15`).
  - `INTERNAL_WALL_OR_TENSION`: **`6`** (`OBS-16..21`, noting `S2` `10_R = 1H` vs `2H = 10_C` seam
    and `S1` `m004` `3`-cycle collision).
  - `OPEN_EXTERNAL_BOUNDARY`: **`3`** (`OBS-22..24`).
- **Updated Guardrail-5 Continuous SM/UV Ledger (`S3`):**
  - Without PS threshold (`B(2) = 5 / 9`, non-unified IR `1/alpha ~ (72, 28, 4)`): **`3`** ratios
    (`g_UV`, `tan(beta)`, `M_R / M_X`; `delta = -1` vs Campaign 1 via `OW13` `lam_0 -> 0`).
  - With Pati-Salam `B_{eff} = 5 / 7` closure: **`4`** continuous ratios (`g_UV`, `tan(beta)`,
    `M_R / M_X`, **`M_{PS} / M_X`**; net `delta = 0` vs Campaign 1) plus extra PS scalars outside
    `16 + 10 + 45` (`(4,1,2)_C`, `(15,1,1)_R`, or `(10,1,3)_C`).
- **Updated Discrete Flavor Selection Bits (`S1`):** `log_2(6) + log_2(3) = log_2(18) ~ 417 / 100`
  bits (`6` perms x `3` cusp levels `m_L in {8, 24, 40}`) BEFORE pricing the un-derived `D_{R,f}`
  ansatz.
- **Clarified `OBS-02` (`S4`) & `S6`:** `(1, 3)` selection requires `t = 1` hyperbolicity or
  Euclidean fiber addition (`Cl^0(1,3) ~= Cl^0(3,1)`), `1 of 5` ordered fibered towers (`1 of 48`
  Cartesian triples); `6` post-`v1` errata cards (`A2-P879`, `A2-OW6`, `A2-OW7`, `A2-OW11`,
  `A2-OW12`, `A2-OW13`) explicitly logged as `mended expectations` under section 12.
