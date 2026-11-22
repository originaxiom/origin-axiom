# Card `A2-OW20` & `A2-OW16 v6` Results Relay: Full Non-Destructive Remediation of `agy-exp` `Card R-3S-FINAL` (`F-OW18-01`..`F-OW18-10`), Complete `2`-Loop Non-Commuting `Type-II 2HDM` RGEs, `2`-Flavor Leptogenesis, & Honest `1 / 10 / 9 / 4` Master Ledger (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (`0 of 19`, strictly data-free)
- **Date:** `2026-11-22`
- **Check Labels (`origin/main:docs/seats/README.md` § `12`):** `computed once` (all three `A2-OW20`, `A2-OW16 v6`, and `referee_a2_ow20` passed cleanly on `v1` with `0` retries and `0` in-place overwrites), `expectations committed first`, `tested against planted errors` (`6 / 6` in `A2-OW20`, `6 / 6` in `A2-OW16 v6`, `6 / 6` in `referee_a2_ow20`), `recomputed independently` (cross-seat verification of `agy-exp` `R-3S-FINAL` `f921a3524` `F-OW18-01`..`10`, `F-C30-01`, and `F-C30-08`), `the same` / `differs`.

---

## 1. Custody Chain & Disjoint Cold-Room Referee Verification (`0` Retries, `0` Overwrites)

1. **Pre-Registration Card (`40c6add75`):** `relays/cards/AGY-002_A2-OW20_r-3s-final-remediation-type2-2hdm-rge-frg-synergy144-and-v6-ledger.md` committed prior to code.
2. **Producer `A2-OW20` (`081278a4b` -> `d720bc7ff`, first-run pass):**
   - `relays/a2_ow20/verify_a2_ow20.py` (`SCRIPT_SHA256 = efa159951d37f2a0177ed3bf68ce35c608e8ed4943efb4c27ff1d58041866318`, `0` AST `float`/`complex` literals, `0` forbidden imports).
   - Sealed unread `relays/a2_ow20/a2_ow20_results.json` (`OUTPUT_SHA256 = 397c825d12211636922c22c7ea5697e96f46da9815080753402e18f9eebb3ec8`, **`all_gates_passed = True`**, **`6 / 6` planted faults**).
3. **Honest Master Ledger `A2-OW16 v6` (`b446cf610` -> `22602bea7`, first-run pass):**
   - `relays/a2_ow16_v6/verify_a2_ow16_v6.py` (`SCRIPT_SHA256 = e53806e9ff8f4031700639b56c8b0eb2b211a632d4815d5d9acfba9a503aaf32`, `0` AST `float`/`complex` literals, `0` forbidden imports).
   - Sealed unread `relays/a2_ow16_v6/a2_ow16_v6_results.json` (`OUTPUT_SHA256 = 30c7e89bdd24cb89a468c13dbfbda8eeef75a7906ea0d9fda774b83425cb4651`, **`all_gates_passed = True`**, **`163 / 163` prior SHA-256 manifests**, **`12 / 12` locks**, **`6 / 6` planted faults**, **`1 / 10 / 9 / 4` honest `24`-observable partition**).
4. **Isolated Cold-Room Zero-Shared-Code Independent Referee (`46415ee16` -> `78045a357`, first-run pass):**
   - `relays/a2_ow20_referee/referee_a2_ow20.py` (`SCRIPT_SHA256 = ad76a0c47a02246e7ad3d9dfb7022e4a79a116cb98a0176f90a7c226ebd749e0`) and raw unread `a2_ow20_referee_results.json` (`OUTPUT_SHA256 = 5e810827028785428a7c30195774e8310245a480f89c73b77e675d204257d5da`).
   - Strictly `0` producer `.py` files read (AST-only scan confirmed `0` float/complex literals and `0` forbidden imports); **`all_gates_passed = True`**, **`total_discrepancies = 0`**, **`6 / 6` referee planted faults caught**, **`165 / 165` branch SHA-256 manifest entries verified (`0` mismatches)**, **`25 / 25` historical false-flag JSON files disclosed (`0` undisclosed)**.

---

## 2. Module-by-Module Results (`A2-OW20` vs Disjoint Cold-Room Referee)

### 2.1 `OW20-A` (Fixes `F-OW18-01` & Harvests `F-C30-08`): Complete `2`-Loop Non-Commuting `Type-II 2HDM` RGEs & `2`-Flavor Leptogenesis
- **Exact `1HDM` Bug Audit & Arason/Buttazzo Benchmark:**
  - Confirmed `OW18-A`'s `1HDM` `2`-loop ordering `-H_u H_d - (1/4) H_d H_u` differed from exact Luo-Xiao Eq. `(14)` `-H_d H_u - (1/4) H_u H_d` by exactly `+(3/4)[H_d, H_u] Y_u` (Frobenius norm `0.00162775`, identity residual `2.63e-47`; cold-room `8.67e-52`, `the same`) and removed the spurious `+(5/4) tr_d` term on `H_u`, restoring the exact `1x1` Arason/Buttazzo coefficients `(-12, -11/4, -1/4)` (`0.0` error).
- **Complete `2`-Loop Non-Commuting `Type-II 2HDM` `3x3` Yukawa + Gauge + `1`-Loop Quartic ODE (`Machacek-Vaughn NPB 236 (1984) 221` Eq. 3.4 & `Chowdhury-Eberhardt arXiv:1503.08216`):**
  - `b^{(1)} = (21/5, -3, -7)`, `1`-loop `+(1/2) H_d Y_u` & `+(1/2) H_u Y_d` (cleanly reversing the `1`-loop CKM `|V_{cb}|` running direction relative to `1HDM`: `dvcb_1hdm = -2.532e-5` vs `dvcb_2hdm = +8.446e-6`), exact `2`-loop `Y^5` non-commuting `(3/2) H_u^2 - (1/4) H_u H_d - (1/4) H_d^2` (`Y_u`) and `(3/2) H_d^2 - (1/4) H_d H_u - (1/4) H_u^2` (`Y_d`).
  - Exact `2`-loop gauge-Yukawa `(-41/240 g_1^2 + 33/16 g_2^2 + 16/3 g_3^2) H_d` (`Y_u`) & `(-53/240 g_1^2 + 33/16 g_2^2 + 16/3 g_3^2) H_u` (`Y_d`), exact `2`-loop quartic terms `-6 lam_2 H_u + (-2 lam_3 + 2 lam_4) H_d + (3/2) lam_2^2 + lam_3^2 + lam_3 lam_4 + lam_4^2` (`lam_1 <-> lam_2` on `Y_d`), and exact `g_1^4, g_2^4` (`1267/600, -113/600, 1449/200, -21/4`).
  - **Guardrail-4 Literature Benchmark Gate:** All `15 / 15` Chowdhury-Eberhardt `Type-II 2HDM` `1x1` coefficients match to **`3.92e-44`** (cold-room `5.35e-50`, `the same`).
  - **Direct Disjoint `GL4` Countercheck on Full Non-Commuting `3x3` Matrices (Permanently Fixes `F-OW18-04`):**
    - Benchmark 1 (`dt = -10`, `RK4 N=120` vs cold-room implicit `GL4 N=40`, fixed-point residual `<= 9.66e-39`): `Yu_ir` Frobenius err **`3.62e-13`**, `Yd_ir` **`3.95e-13`**, `Ye_ir` **`6.09e-14`**, `g_ir` `6.24e-13`, `lam_ir` `3.50e-13`, `vcb_uv = 0.0417464 -> vcb_ir_2hdm = 0.0426920` (`6.48e-15`).
    - Benchmark 2 (`Synergy S-1` complex `3x3` UV -> IR, `dt = -10`, `RK4 N=80` vs cold-room `GL4 N=30`): `Yu_ir` Frobenius err **`1.11e-12`**, `Yd_ir` **`1.14e-12`**, `Ye_ir` **`1.64e-13`**, CKM `(|V_12|, |V_23|, |V_13|)` UV `(0.540032, 0.302297, 0.127279)` -> IR `(0.540151, 0.307657, 0.129668)` (`1.39e-13`).
    - **Guardrail-3 Haar `U(3)^3 x U(3)^2` Covariance (`10` trials):** `1.18e-45` (`RK4`), `3.61e-51` (`GL4` SplitMix64).
  - **Bonus Cross-Seat Catch for `agy` (`AGY-C30:520` at `528ef1cf5`):** Our Machacek-Vaughn check shows `C30:520` placed `(33/16) g_2^2` on `H_u` instead of `(135/16) g_2^2`, omitted `g^2 H_d`, wrote `+H_d^2 - H_d H_u` instead of `-(1/4) H_d^2`, and omitted `2`-loop quartic terms.
- **`2`-Flavor (`|tau>` vs `|e + mu>`) vs `3`-Flavor Leptogenesis (`F-C30-08` Harvest — `the same`):**
  - **Radiative `1`-Loop `M_R`:** Flat `Y_B^{3f}(tau_*^+) = +1.611169e-8` -> **`Y_B^{2f}(tau_*^+) = +2.157932e-9`** (`ratio = 0.133936`, **`7.47x` suppression**, retains **`tau_*^+`**); `2D E[2]` hyperbolic Kahler `Y_B^{3f} = +1.058670e-8` -> **`Y_B^{2f} = +2.474106e-9`** (`4.28x` suppression, retains **`tau_*^+`**).
  - **Tree `M_R(0, 0)` (Sign Reversal Under `2`-Flavor!):** Because `eps_{1, e+mu} = +4.213256e-7 > 0` matches `eps_{1, tau} > 0`, `2`-flavor flips BOTH flat (`3f: +6.1096e-14` -> **`2f: -2.8587e-11`**) AND `2D E[2]` (`3f: +1.3127e-11` -> **`2f: -2.1043e-11`**) back to **`tau_*^-`** (matching unflavored `OW12`!). Exact CP-mirror antisymmetry holds to `<= 1.87e-50` across all `4` sectors (cold-room match `<= 3.50e-10` rel).

### 2.2 `OW20-B` (Fixes `F-OW18-02`, `F-OW18-03`, `F-OW18-05`, & Verifies `F-C30-01`)
- **Consistent Non-Chimera FRG (`F-OW18-02`):** Retracts `OW18-B`'s Chimera `run_2hdm_1loop`. On consistent `G_SM 2HDM` (`N_S = 8, N_W = 48, N_V = 12`):
  - `DP Type-I` (`f_W = -1/2`, `M_g = -64`): `f_lam = 0.1977862688 > f_crit = 0.0404323345`, **`disc = +789.61391456 > 0`**, with BOTH roots strictly negative (`-0.00886525`, `-2.3505377`; cold-room 1D Ridder err `<= 3.75e-12`, `the same`).
  - `DEP Type-II` (`f_W = +1`, `M_g = +8`): `f_lam = 0.0338281351 < f_crit`, **`disc = -6.13857817 < 0`** (`0` real roots; cold-room err `4.23e-14`, `the same`).
  - Thus NO positive pure-gauge UV quartic fixed point exists in consistent `G_SM 2HDM` under either scheme; all `4` UV quartics `lambda_{1..4}(M_X)` remain unfixed and are now explicitly priced in `A2-OW16 v6`.
- **Prose-vs-JSON Higgs Mass Audit (`F-OW18-03`):** Sealed `a2_ow18_v3_results.json` records `mh0/v = 0.48392069`, `mH0/v = 0.7523597846`, `mHpm/v = 0.752656116`, confirming `AGY002_A2_OW18_RESULTS.md:23` mis-transcribed `mH0/v = 0.95547910` (`+27.00%`) and `mHpm/v = 0.94624861` (`+25.72%`). Those Chimera-based values are formally retracted and corrected in `AGY002_A2_OW18_RESULTS.md`.
- **`E_6` `N_W = 81` vs `DEP < 31` & `Z_4` `M_R == 0` (`F-OW18-05`, `F-C30-01`):** `Tr_{3x16} Q_psi = +48 != 0` vs `Tr_{3x27} Q_psi = 0` (`N_W = 81`); `M_g(G_SM, 2H, N_W=81, DEP Type-II) = +41 > 31` violates `DEP < 31` (whereas `DP Type-I` gives `-161/2 < 0`). Condensing `S_{+4}` breaks `U(1)_psi -> Z_4`, forcing `Q_psi(N_R^c N_R^c) = +2 == 2 (mod 4) != 0` (`M_R == 0` identically); `16_{+1,H}` carries `P_M = -1` (breaking DM parity), whereas `overline{126}_{-2} subset 351'_H` carries `Q_psi = -2`, `P_M = +1`, allowing `16_{+1} 16_{+1} overline{126}_{-2}` while preserving `P_M`.

### 2.3 `OW20-C` (Fixes `F-OW18-06`, `F-OW18-07`, `F-OW18-08`)
- **Exact `Synergy S-1` `144 -> 2` (`6.17` Bits), `SL(2, Z)` Covariance, & Broken `w ~ -w` (`F-OW18-06`):**
  - Direct enumeration gives `|E[5]_prim| = 24 -> |P_5| = 12`, `|E[6]_prim| = 24 -> |P_6| = 12` (retracting `|P_6| = 6`), `|P_5 x P_6| = 144 -> 2` (`log_2(72) = 6.16992500144` bits, retracting double-divided `5.17` bits), and explicit `SL(2, Z)` conjugacy `ker(g M g^{-1} + I_2) = g ker(M + I_2)` (`LR ~ T^3 S`, `L^2 R ~ T^4 S`, `L R^2 ~ (T^4 S)^{-1}`).
  - Verified `w ~ -w` breaks on coherent `Y_0 = om_3 Y(p_3) + om_4 Y(p_4)`: flipping `p_3 = (1/5, 2/5) -> (4/5, 3/5)` shifts `|V_{cb}|` from `0.302297` to `0.178084` (**`Delta|V_{cb}| = 0.124213`**) and flips raw `bar_theta_QCD` from `-1.10526` to `+0.95305 rad` (`4` distinct relative-sign worlds; cold-room err `2.65e-12`).
- **Explicit Computed `SO(2d)` `SU(d)^3` Cubic Anomalies (Fixes `F-OW18-08`):** Replaced `verify_a2_ow18_v3.py:1587`'s literal `anom_free = True` with explicit computation across `d = 3..15` (combinatorial formula in producer; disjoint `2^{d-1}` half-spinor weight-lattice trace in cold-room referee), proving `A(SO(6)) = -1 != 0` and `A(SO(8)) = ... = A(SO(30)) = 0` dynamically.
- **Exact Brane-`2H` `Spin(10)` Beta (`F-OW18-07`):** Pure-fermion brane-`2H` `b_{Spin(10)} = -(11/3)*8 + (2/3)*3*2 = -76/3` vs phantom bulk-`10_R` `-151/6` (diff `+1/6`).

---

## 3. Brutally Honest Master Ledger Rebuild (`A2-OW16 v6`, `22602bea7`)

- **Honest `24`-Observable Partition (`1 / 10 / 9 / 4`):**
  - **`1` `DERIVED_EXACT`:** `OBS-07` (`6D I_8(16_+)` rank-`4` GS obstruction `det Q = 1/1679616` -> `7D` CS axion `E/N = 8/3` & `Theorem 2` `d`-invariance).
  - **`10` `CONDITIONAL_OR_QUALITATIVE`:** `OBS-02` (demoted: Lorentzian class `{(1,3)~(3,1)}` conditional on `D = 4`), `OBS-03`, `OBS-04` (`E_6` `N_W = 81 > 31` `DEP` conflict disclosed), `OBS-05` (`Z_4` `M_R == 0` + `overline{126}_{-2}` + `1`-loop `Z'_psi` hierarchy wall), `OBS-08`, `OBS-11`, `OBS-12` (`2D` hyperbolic Kahler + `2`-loop `Type-II 2HDM` RGEs + `144 -> 2` `6.17` bits + broken `w ~ -w`), `OBS-13`, `OBS-14`, `OBS-15` (`2`-flavor radiative `tau_*^+` vs tree `tau_*^-`).
  - **`9` `INTERNAL_WALL_OR_TENSION`:** `OBS-06` (`3905`-tuple `E_8` `6D` `s=3` Casimir), `OBS-09` (non-SUSY `2HDM` quartics unfixed; Type-I `+789.61` negative roots & Type-II `-6.14`), `OBS-10`, `OBS-16`, `OBS-17`, `OBS-18`, `OBS-19`, `OBS-20` (Majorana `psi_S` Planck-suppressed `M_{11}^{-2}` `p`-wave), `OBS-21`.
  - **`4` `OPEN_EXTERNAL_BOUNDARY`:** `OBS-01` (`D = 4`, demoted for zero branch computation), `OBS-22` (`b_{Spin(10)} = -76/3`, explicitly pricing **`15` continuous dimensionless UV ratios**: `g_UV`, `tan(beta)`, `M_R/M_X`, `M_PS/M_X`, `v_{B-L}/M_X`, `M_u L_c`, `M_d L_c`, `M_e L_c`, `lambda_{1..4}(M_X)`, `m_{12}^2/M_X^2`, `Re(tau)`, `Im(tau)`, plus `1` CP-branch bit, `2` broken-antipodal bits, and `log_2(72) = 6.17` Lefschetz bits), `OBS-23`, `OBS-24`.

0 of 19.
