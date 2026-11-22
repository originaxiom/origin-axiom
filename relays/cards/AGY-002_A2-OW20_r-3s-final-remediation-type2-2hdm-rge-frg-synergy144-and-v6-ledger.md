# Pre-Registration Card A2-OW20 & A2-OW16 v6: Full Non-Destructive Remediation of agy-exp Card R-3S-FINAL (F-OW18-01..10), Complete 2-Loop Non-Commuting Type-II 2HDM RGEs, 2-Flavor Leptogenesis, & Honest 1/10/9/4 Master Ledger (0 of 19)

- **Seat:** `agy-002`
- **Branch:** `agy-002/verify`
- **Date:** `2026-11-22`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or lattice numbers anywhere; purely mathematical-physics and dimensionless)
- **Custody Mode:** `expectations committed first`, `tested against planted errors`, pre-hashed scripts (`SCRIPT_SHA256.txt`) committed before execution, raw unread outputs (`OUTPUT_SHA256.txt`) committed before analysis, followed by an isolated cold-room zero-shared-code referee (`relays/a2_ow20_referee/referee_a2_ow20.py`) verifying full non-commuting `3x3` IR Yukawa matrices directly via a disjoint ODE integrator. Strictly zero in-place overwrites of any sealed file.
- **Target Audit Addressed:** `agy-exp` `Card R-3S-FINAL` (`f921a3524:relays/AGY_EXP_TO_ALL_SEATS_2026-11-22_R_3S_FINAL_DELTA_AUDIT_OF_AGY_C30_AND_AGY002_OW18.md`, findings `F-OW18-01`..`F-OW18-10`, plus cross-seat harvests `F-C30-01` & `F-C30-08`).

---

## 1. Pre-Registered Modules & Acceptance Gates (`A2-OW20`)

All scripts MUST satisfy `0` Python `float` and `0` Python `complex` AST literals, `0` peer or `frontier/` imports, and all six mathematical-physics guardrails (zero hardcoded proof flags; `10`-trial Haar `U(3)^3` basis-scrambling `< 1e-25` on physical flavor observables; disjoint cold-room referee).

### Module `OW20-A` (Fixes `F-OW18-01` & Harvests `F-C30-08`): Complete `2`-Loop Non-Commuting `Type-II 2HDM` `3x3` Yukawa + Gauge + Quartic RGEs & `2`-Flavor Leptogenesis
1. **Exact `1HDM` vs `Type-II 2HDM` Machacek-Vaughn Engine (`NPB 236 (1984) 221` Eq. 3.4 & `Chowdhury-Eberhardt JHEP 11 (2015) 052`, `arXiv:1503.08216`):**
   - Explicitly verify the `1HDM` Luo-Xiao Eq. (14) non-commuting ordering `(3/2) H_u^2 - H_d H_u - (1/4) H_u H_d + (11/4) H_d^2` (and verify the `OW18-A` bug difference `(3/4)[H_d, H_u] Y_u` to `< 1e-35`, plus remove the spurious `+(5/4) tr_d` term on `H_u` so the `1x1` Arason/Buttazzo benchmark `-12 y_t^5 - (11/4) y_t^3 y_b^2 - (1/4) y_t y_b^4` holds with `0` error!).
   - Implement the complete `2`-loop non-commuting `Type-II 2HDM` `3x3` Yukawa + gauge + `1`-loop quartic coupled ODE: `b^{(1)} = (21/5, -3, -7)`, `B_{ij}(n_H=2)`, `1`-loop `+(1/2) H_d Y_u` & `+(1/2) H_u Y_d`, exact `2`-loop `Y^5` non-commuting `(3/2) H_u^2 - (1/4) H_u H_d - (1/4) H_d^2` (`Y_u`) and `(3/2) H_d^2 - (1/4) H_d H_u - (1/4) H_u^2` (`Y_d`),
   - Include exact `2`-loop quartic terms `-6 lam_2 H_u - 2 lam_3 H_d + 2 lam_4 H_d + (3/2) lam_2^2 + lam_3^2 + lam_3 lam_4 + lam_4^2` on `Y_u` (`lam_1 <-> lam_2` on `Y_d`), exact `2`-loop gauge-Yukawa `(-41/240 g_1^2 + 33/16 g_2^2 + 16/3 g_3^2) H_d` on `Y_u` and `(-53/240 g_1^2 + 33/16 g_2^2 + 16/3 g_3^2) H_u` on `Y_d`, and exact `g_1^4, g_2^4` shifts `1267/600, -113/600, 1449/200, -21/4`.
   - **Guardrail 4 Literature Benchmark Gate:** Verify exact `0` residual against all `Type-II 2HDM` `1x1` rational coefficients of `Chowdhury-Eberhardt arXiv:1503.08216` (`-12, -5/2, -5/2, -3/4, -27/4, -9/4, -3, 1267/600, -113/600, 1449/200, -21/4, 16/3, 33/16, -41/240, -53/240`).
   - **Full `3x3` Non-Commuting Integration & Guardrail 3:** Integrate a concrete non-commuting `3x3` benchmark (and `Synergy S-1` UV matrices) with `45`-dps `RK4`, seal full `3x3` `Yu_ir, Yd_ir, Ye_ir` in JSON (so the cold-room referee directly counterchecks non-commuting `3x3` matrices via `GL4`!), confirm `1`-loop CKM running sign reverses cleanly between `1HDM` (`-3/2`) and `Type-II 2HDM` (`+1/2`), and verify `10`-trial `45`-dps Haar `U(3)^3` covariance `< 1e-30`.
2. **`2`-Flavor (`|tau>` vs `|e + mu>`) vs `3`-Flavor Leptogenesis (`F-C30-08`):**
   - Compute exact `2`-flavor (`K_{1, e+mu} = (p_e + p_mu) K_1`, `eps_{1, e+mu} = eps_{1,e} + eps_{1,mu}`) vs `3`-flavor leptogenesis on `Synergy S-1` (both flat and `2D` hyperbolic `E[2]` Kahler metrics, for both `1`-loop radiative `M_R` and tree `M_R(0, 0)`), verifying:
     - For `1`-loop radiative `M_R`: `2`-flavor preserves `Y_B(tau_*^+) > 0` while reducing `Y_B` by `~7.47x` (`ratio 2f/3f ~= 0.1339`) relative to `C30`'s unphysical `3`-flavor sum;
     - For tree `M_R(0, 0)`: `eps_{1, e+mu} = eps_{1,e} + eps_{1,mu} > 0` has the same positive sign as `eps_{1, tau} > 0`, flipping `2`-flavor `Y_B^{2f}(tau_*^+) < 0` back to **`tau_*^-`** (matching unflavored `OW12`!), with exact CP-mirror antisymmetry `< 1e-35`.

### Module `OW20-B` (Fixes `F-OW18-02`, `F-OW18-03`, `F-OW18-05`, & Verifies `F-C30-01`): Consistent Non-Chimera FRG, `E_6` `Z_4` `M_R == 0` Obstruction, & `N_W = 81` Fixed-Point Test
1. **Consistent Non-Chimera FRG Analysis (`F-OW18-02`):**
   - Formally retract `OW18-B`'s Chimera `run_2hdm_1loop` (which reused `Spin(10)` `fl_s10_dD` with retracted hybrid `f_W = +1` inside `G_SM` `2HDM`).
   - Compute `G_SM` `2HDM` (`N_S = 8, N_W = 48, N_V = 12`) under BOTH consistent `DP` Type-I (`f_W = -1/2`, `M_g = -64`) and `DEP` Type-II (`f_W = +1`, `M_g = +8`): confirm Type-I yields `f_lam = 0.1977862688 > f_crit = 0.0404323` and **positive discriminant `+789.6139146 > 0`** with two strictly negative UV fixed-point roots `r_1, r_2 < 0`, while Type-II gives `disc = -6.138578 < 0` (`0` real roots), proving no positive pure-gauge UV quartic fixed point exists in consistent `G_SM` `2HDM` under either scheme (leaving all `4` UV quartics `lambda_{1..4}(M_X)` unfixed!).
2. **Exact Prose Transcription Correction (`F-OW18-03`):**
   - Read sealed `relays/a2_ow18_v3/a2_ow18_v3_results.json` directly to verify exact recorded values `mh0/v = 0.48392069`, `mH0/v = 0.7523597846`, `mHpm/v = 0.752656116`, documenting the `+27.00%` / `+25.72%` prose transcription error in `AGY002_A2_OW18_RESULTS.md:23` (and marking those Chimera-based values retracted).
3. **`E_6` `N_W = 81` vs `DEP` Type-II `< 31` & `Z_4` `M_R == 0` Selection Rule (`F-OW18-05`, `F-C30-01`):**
   - Verify `Tr_{3 x 16} Q_psi = +48 != 0` vs `Tr_{3 x 27} Q_psi = 0` (`N_W = 81`); prove `M_g(G_SM, 2H, N_W = 81, DEP Type-II) = +41 > 31` (violating `DEP` `< 31` bound) vs `M_g(DP Type-I) = -161/2 < 0`.
   - Prove `Z_4` `M_R == 0` theorem: condensing `S_{+4} in (1_{+4})_H` breaks `U(1)_psi -> Z_4`, under which `Q_psi(N_R^c N_R^c) = +2 == 2 (mod 4) != 0` for all powers `4n + 2`, forcing `M_R == 0` identically; `16_{+1,H}` carries `P_M = (-1)^{3(1)+0} = -1` (breaking DM parity), whereas `overline{126}_{-2} subset 351'_H` carries `Q_psi = -2`, `B - L = +-2`, `P_M = (-1)^{+-6} = +1` (allowing `16_{+1} 16_{+1} overline{126}_{-2}` while preserving `P_M`).

### Module `OW20-C` (Fixes `F-OW18-06`, `F-OW18-08`): Exact `Synergy S-1` `144 -> 2` (`6.17` Bits), `SL(2, Z)` Conjugacy Covariance, Broken `w ~ -w`, & Explicit `SO(2d)` `SU(d)^3` Cubic Anomaly Computation
1. **`Synergy S-1` Exact Cardinality, Conjugacy Covariance, & Broken `w ~ -w` (`F-OW18-06`, `F-C30-03`):**
   - Compute primitive torsion orders by inclusion-exclusion: `|E[5]_prim| = 24 -> |P_5| = 12`, `|E[6]_prim| = 6^2 - 2^2 - 3^2 + 1 = 24 -> |P_6| = 12`, `|P_5 x P_6| = 144`, reduction `144 -> 2` is `log_2(72) = 6.16992500144` bits (retracting `OW18-D`'s double-divided `5.17` bits and `72`).
   - Verify explicit `SL(2, Z)` basis covariance `ker(g M g^{-1} + I_2) = g ker(M + I_2)` comparing `LR` vs `T^3 S` (`t = 3`) and `L^2 R`, `LR^2` vs `T^4 S` (`t = 4`).
   - Compute `Y_0 = om_3 Y(p_3) + om_4 Y(p_4)` at `p_3 = (1/5, 2/5)` vs `-p_3 = (4/5, 3/5)` (fixed `p_4 = (1/6, 1/6)`), independently confirming `Delta|V_cb| = 0.124213 > 0.1` and raw `bar_theta_QCD` sign flip (`-1.105` -> `+0.953` rad), proving `w ~ -w` fails on the coherent weave (`4` distinct relative-sign worlds).
2. **Explicit `SO(2d)` `SU(d)^3` Cubic Anomaly Computation (Fixes `F-OW18-08` Literal `anom_free = True`):**
   - Replace `verify_a2_ow18_v3.py:1587`'s hardcoded literal `anom_free = True` with exact computed `SU(d)^3` cubic anomaly sums `A(S_+) = sum_{k even} (d - 2k) (d - 3)! / ((k - 1)!(d - k - 1)!)` across `d = 3..15`, proving `A(SO(6)) = -1 != 0` and `A(SO(2d)) == 0` for all `d = 4..15` (no literal boolean!).
   - Verify pure-fermion `Spin(10)` brane-`2H` `1`-loop gauge beta `b_0 = -(11/3)*8 + (2/3)*3*2 = -76/3` vs bulk `10_R` `-151/6` (`F-OW18-07`).

### Module `OW20-D`: `6 / 6` Planted Fault Controls (`tested against planted errors`)
1. **`PF-OW20-1`:** Reverting `1HDM` `-3/2 H_d Y_u` or `OW18-A`'s wrong `-H_u H_d - (1/4) H_d H_u` order produces non-zero commutator error `(3/4)[H_d, H_u] Y_u != 0` and reverses CKM running.
2. **`PF-OW20-2`:** Restoring retracted hybrid `f_W = +1` on `G_SM` `2HDM` flips consistent Type-I discriminant `+789.61 > 0` back to `-6.14 < 0`.
3. **`PF-OW20-3`:** Trying `16_{+1,H}` (`B - L = 1, s = 0`) to generate `M_R` violates `P_M = +1` (`P_M = -1`).
4. **`PF-OW20-4`:** Using `|P_6| = 6` (`72` pairs) or double-dividing `72 / 2` (`5.17` bits) fails exact `|P_5 x P_6| = 144` (`6.17` bits).
5. **`PF-OW20-5`:** Claiming `SO(6)` (`d = 3`) half-spinor is anomaly-free fails explicit `A(S_+) = -1 != 0`.
6. **`PF-OW20-6`:** Using `b_{Spin(10)} = -151/6` for pure-fermion brane `2H` fails exact `-76/3` check (off by `+1/6` from phantom bulk `10_R`).

---

## 2. Pre-Registered Honest Master Ledger Rebuild (`A2-OW16 v6`, Fixes `F-OW18-07` & `F-OW18-08`)

`relays/a2_ow16_v6/verify_a2_ow16_v6.py` rebuilds the `24`-observable partition with zero overclaimed `DERIVED_EXACT` rows:
- **`1` `DERIVED_EXACT`:** `OBS-07` (`6D I_8(16_+)` rank-`4` GS obstruction `det Q = 1/1679616` & `7D` CS axion `E/N = 8/3`).
- **`10` `CONDITIONAL_OR_QUALITATIVE`:** `OBS-02` (Lorentzian class `{(1,3)~(3,1)}` conditional on `D = 4`), `OBS-03`, `OBS-04` (`N_W = 81` `E_6` vs `DEP < 31` conflict disclosed), `OBS-05` (`E_6` `Z_4` `M_R == 0` + `\overline{126}_{-2}` + `1`-loop `Z'_psi` hierarchy wall), `OBS-08`, `OBS-11`, `OBS-12` (`2D` hyperbolic Kahler + `144 -> 2` `6.17` bits + broken `w ~ -w`), `OBS-13`, `OBS-14`, `OBS-15` (`2`-flavor radiative `tau_*^+` vs `2`-flavor tree `tau_*^-`).
- **`9` `INTERNAL_WALL_OR_TENSION`:** `OBS-06` (exhaustive `3905`-tuple `E_8` `6D` `s = 3` Casimir), `OBS-09` (non-SUSY `2HDM` quartics unfixed; Type-I `disc = +789.61` negative roots & Type-II `disc = -6.14`), `OBS-10`, `OBS-16`, `OBS-17`, `OBS-18`, `OBS-19`, `OBS-20` (Majorana `psi_S` Planck-suppressed `M_{11}^{-2}` `p`-wave), `OBS-21`.
- **`4` `OPEN_EXTERNAL_BOUNDARY`:** `OBS-01` (`D = 4`, demoted for zero branch computation), `OBS-22` (corrected `b_{Spin(10)} = -76/3`, explicitly pricing all newly unfixed continuous/discrete parameters: `4` `2HDM` UV quartics `lambda_{1..4}`, `m_{12}^2/M_X^2`, `(Re tau, Im tau)`, and `1` CP-branch bit), `OBS-23`, `OBS-24`.
- Includes `6 / 6` planted fault controls, full live SHA-256 verification of all prior branch manifests, and computed `guardrail5_anchor_limit_ok` (`0` AST float/complex literals).
