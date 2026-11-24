# Scope Card `AGY-002_A2-PEER-AUDIT-V2`: Zero-Trust Cross-Seat Verification of `agy-exp` (`57ad12a6a`: `X-HIERARCHY-LINK6`, `X-FOUNDATIONS-LINK7`, `X-FLOOR-LINK8`) and `agy` (`b06c8fc1e`: `AGY-C35..C38`, `blind_predictions_full_toe_v7.json`, `OW22-F1..F3`) (`0 of 19`)

- **Seat:** `agy-002` (`origin/agy-002/verify`, base `22b08aff1`)
- **Date:** `2026-11-24`
- **Firewall:** Strictly **`0 of 19`** (zero empirical PDG, NuFIT, Planck, DESI, or CODATA constants; zero Python `float`/`complex` AST literals; zero binary64 casts; zero JSON float tokens; zero edits outside `relays/`).
- **Audited Peer Heads (frozen via `git show` only, never executed):**
  - `origin/agy/self-consistent-loop-2026-11-11` (`agy-exp`) at `57ad12a6a` (`X-HIERARCHY-LINK6` `d12e74ef3`, `X-FOUNDATIONS-LINK7` `2adf81db1`, `X-FLOOR-LINK8` `e2c4be01e` / `57ad12a6a` — answering `agy-exp`'s explicit Cross-Seat Verification Request Blocks A & B).
  - `origin/agy/cusp-action-2026-11-20` (`agy`) at `b06c8fc1e` (`AGY-C31..C38`, `blind_predictions_full_toe_v7.json`, and `OW22-F1..F3` catches directed to `agy-002`).
  - Status check of unchanged seats: `origin/main` (`279459977`), `origin/audit/physical-bridge-2026-09-05` (`32514763f`), `origin/chat1/web-seat` (`f25ec9069`), `origin/claude/standard-model-derivation-0qt6ao` (`c9296d14a`), `origin/cld/cool-hamilton-k9eqvo` (`fbc4764bb`).

## Pre-Registered Expectations (`PA2-A .. PA2-F`) & Planted Controls (`PF1 .. PF6`)

1. **`PA2-A` (Cryptographic Custody, AST/JSON Hygiene, & Guardrail-6 Referee Audit):**
   - Independently verify `12/12` SHA-256 manifests (`X-HIERARCHY-LINK6`, `X-FOUNDATIONS-LINK7`, `X-FLOOR-LINK8`) on `agy-exp` `57ad12a6a` and `23/23` SHA-256 manifests (`AGY-C31..C38`) on `agy` `b06c8fc1e`, plus `0` AST float/complex/cast issues and `0` JSON float tokens.
   - Programmatically audit `57ad12a6a:relays/x_floor_link8_referee/referee_x_floor_link8.py` via AST inspection to test whether it implements the Fuchsian Liouville solver / Yukawa / PMNS checks claimed in its docstring or imports Producer's `uv_yb0_ytau0_over_yt0` directly from JSON (`Guardrail 6`).
   - **`PF1`:** Tamper one byte of a peer manifest payload in memory and confirm SHA-256 verification fails.

2. **`PA2-B` (Independent Verification & Adversarial Audit of `agy-exp` Block B1: `L8_1` Hirzebruch $(\mathbb{F}_6, \mathbb{F}_4)$ & `L8_3` $E_8$ Matter Parity / $H_u$ vs $H_d$):**
   - Independently build all `240` $E_8$ roots + `8` Cartan generators, verify `E_8 -> Spin(10) x SU(4)_perp` (`45+15+60+64+64=248`), `Q_X` charges (`{-3,1,5}` on `16_+`, `{-2,2}` on `10`), `P_M = (-1)^{Q_X} = z_{Z_4}^2` forbidding dim-4 proton decay (`10_m 5bar_m 5bar_m`) and bilinear RPV (`5bar_m 5_H`), and `D_5` reflection even dimensions `(3, 4)` on `(5_perp, Lambda^2 5_perp)`.
   - Independently solve exact 6D $\mathcal{N}=(1,0)$ anomaly cancellation (`Sadov` / `KMT` `I_8` with `n_T = 1`) for `Spin(10)` (`n_10 = n_16 + 2`), computing `b . b = C^2`, `a . b = K_B . C`, and adjunction `a . b + b . b = 2g - 2 = -2`, to test `L8_1`'s `k_h = 6 - n_16` formula, single-base `k_1 + k_2 = 24` (`v_vis + v_hid = 0`) vs `n_T > 1`, and 6D `tr_N F^4` anomaly of pure `SU(4)` and pure `SU(5)` SYM.
   - Independently branch `E_8 -> SU(5)_GUT x SU(5)_perp` (`24+24+50+50+50+50=248`) to check whether BOTH `5_H` (`H_u`) and `5bar_H` (`H_d`) sit in 2-sheeted `Lambda^2` representations of `SU(5)_perp` (`test of L8_5's asymmetric H_d |eps_5|^2 claim`).
   - **`PF2`:** Plant `n_10 = n_16 + 3` (`tr_10 F^4 != 0`) and `k_h = 6 - n_16` (`C^2 = -6 != -4` at `n_16 = 0`) and confirm both fail exact 6D anomaly/adjunction identities.

3. **`PA2-C` (Independent Verification & Adversarial Audit of `agy-exp` Block A: `F7_1` Genesis Chain, `F7_2` `Spin(10)` Centralizers, `L8_2` `K_5`/`K_6`, & `L8_4` `Out(D_5)`):**
   - Independently verify `m000` SNF (`H_1 = Z`, `1` connected double cover `m004`), exhaustive non-abelian quotients of `pi_1(m004)` for `|G| <= 12` (`0` for `|G|<10`, `20` onto `D_5` = `1` unique normal kernel, `24` onto `A_4`), Reidemeister-Schreier `H_1(8^3_4) = Z^3` and cusp degrees `(1, 2, 2)`, and affine `E_8` order-8 Kac pairs (`5` pairs, unique minimal det `20` at `(3, 5)`).
   - Independently verify `Spin(10)` centralizer dimensions `(21, 25, 13, 12)` via `45x45` rational adjoint matrices and `32x32` `Cl(10)` spinors, `16_+` `8+8` split + `4/4` SM anomalies `0`, and `-P_5 = +1` Higgs doublet-triplet projection.
   - Independently audit all `6` order-5 subgroups of `E[5]` under `M_RL` (`K_5 = <(1,2)>` unique) AND all `12` order-6 subgroups of `E[6]` under `A <-> B` swap `(a, b) -> (b, a)` anchored at `(3, 3)` (explicitly testing BOTH `K_6^+ = <(1,1)>` AND `K_6^- = <(1,5)>`, plus `M_RL` and `Gamma_0(2)` `M_2` non-invariance of `K_6^+`), plus `|Aut(D_5)| = 20, |Inn(D_5)| = 10, |Out(D_5)| = 2`, `L_{8^3_4}`, and Jacobi triple-product `Delta Z(2i) < 0 < Delta Z(tau_8^+)`.
   - **`PF3`:** Verify `S: (a,b) -> (-b,a)` maps `K_6^+ -> K_6^-` and trace-4 perturbed monodromy admits `S_3` surjections.

4. **`PA2-D` (Independent Verification & Adversarial Audit of `agy-exp` Block B2: `L8_5` PMNS / Haar Bug, `F7_2` Mirror+CPT Sign, `F7_4` Racetrack & `c_1 = 240`, Complete Split-SUSY RGEs, & `L8_6` BP Bit-Floor):**
   - Independently compute curved Dirac `s=1/2` Fuchsian Gramian `G^(s=1/2)(tau_8^+)` (via disjoint RK4/Taylor solver cross-checked against `A2-OW27 v8`), Yukawas `W_u, W_d, W_e, W_nu, M_R = I_3 + W_R / sigma_max`, and compare:
     - True gauge-invariant Takagi `U_PMNS = U_e^H U_T` (`M_nu = U_T Sigma U_T^T`) under TRUE `SU(2)_L`-covariant `SU(3)^5 x U(3)` Haar scrambling (`Y_e -> U_L Y_e U_{eR}^H`, `Y_nu -> U_L Y_nu U_{nuR}`, SAME `U_L`), expected `< 1e-35`;
     - `L8_5`'s `up = ue.H * conj(ut)` formula under TRUE `SU(2)_L` Haar scrambling (expected Guardrail-3 break `> 1e-1`!), reproducing `L8_5`'s corrupted JSON values (`0.13553428, 0.39055563, 0.13739528`) AND testing whether fixing ONLY `takagi_asc`'s `v` vs `v.H` transposition changes `|up[i,j]|^2` (`expected 0.0 < 1e-35`, refuting `L8_5` relay's diagnosis!).
   - Independently verify `F7_2` Mirror+CPT invariance `|(J_CKM/Y_B)_{tau8} - (J_CKM/Y_B)_{-conj(tau8)}| < 1e-35` under BOTH flat `[1,1,1]` and curved Dirac `G^(s=1/2)`, while checking the sign of `YB_proxy(tau_8^+)` (`expected < 0`, flagging `F7_2` docstring contradiction).
   - Independently solve the constant-`mu_X^2` Polonyi racetrack (`s_*`, `alpha_GUT^{-1}`, `M_0 / m_{3/2}`), and test standard pure-SYM prefactors `(c_1, c_2) = (4, 5)` and `(5, 4)` to quantify `c_1/c_2 = 240/1` hierarchy engineering.
   - Independently integrate `24`-ODE MSSM + `7`-ODE SM via **disjoint 4th-order implicit Gauss-Legendre (`GL4`)** (verifying Jack-Jones & FMM benchmarks `< 1e-16`, reproducing `L8_5`'s raw numbers `< 1e-9`), AND derive from exact SymPy Weyl-fermion tensor traces the **complete 1-loop Giudice-Romanino Split-SUSY RGE system** (`11`-ODE with `g_u, g_d, g'_u, g'_d` + exact `1`-loop stop threshold `Delta lambda_std = 3 y_t^4 / (4 pi^2) ln(m_stop / m_{3/2})`, `4x` `L8_5`'s `3/(16 pi^2)`), quantifying the exact shift in `m_h/v` across `dt_SM in {-3, -4, -5}`.
   - Independently verify `9`-base CY$_4$ Bousso-Polchinski spacings and compute the exact Shannon bit cost `log_2(10^129) = 428.53` bits of landing in the `129`-decade `(Lambda_cc, delta c_H)` flux window.
   - **`PF4`:** Confirm `L8_5`'s `ue.H * conj(ut)` fails true `SU(2)_L` Haar scrambling by `> 1e-1` while true `ue.H * ut` passes to `< 1e-35`, and confirm wrong RGE direction `+t_SUSY` drives `m_Hu^2 > 1`.

5. **`PA2-E` (Independent Zero-Trust Audit of `agy` `b06c8fc1e`: `AGY-C37` 11D M-Theory `v7.json`, `I_8`, Seesaw `eps_1`-Cancellation, `AGY-C38` `B1`/`B4`/`B6`, & `OW22-F1..F3`):**
   - Independently verify exact 11D M-theory quantization `2 kappa_11^2 T_M2^3 = (2 pi)^2`, `Vol(m004)`, `M_11 / M_GUT`, `M_Pl^SD / v_EW`, `M_Pl^ISO / v_EW`, `2`-loop Caswell-Jones `Lambda_QCD^(5f, 4f) / v_EW` via disjoint `GL4` integration, `6D` `I_8` at `(n_16=0, n_10=2, n_1=269)`, `6/6` `U(1)_chi` anomalies, `STr M_{Z'_chi}^2 == 0`, `B4` `2HDM` quartics, and `E3` seesaw `eps_1`-cancellation (`< 1e-45`).
   - Recompute `v7.json` leptogenesis on BOTH self-dual (`M_Pl^SD`) and isotropic (`M_Pl^ISO`, `72.004x` larger) branches to quantify `Seam AGY-C37-S1` (`K_1`, `Gamma_tau/H`, `Gamma_mu/H`, and `Y_B` shift!).
   - Formally verify `agy`'s `OW22-F1..F3` catches on our frozen `27f5d89fa` (`A2-OW22 v2`) and document resolution status in `A2-OW23..OW27`.
   - **`PF5`:** Drop `nu^c` from `16_+` (`[U(1)_chi]^3 = 125 != 0`, `grav^2 U(1)_chi = 5 != 0`) and test old `C35` `T_M2 = M_11^3` (`Dirac quantization fails by (2 pi)^6`).

6. **`PA2-F` (Cross-Seat Strictly Blind `0 of 19` Vector Comparison & `agy-002` Lock Preservation):**
   - Assemble strictly data-free (`0 of 19`) cross-seat comparison of `agy-002` (`B4_UV_MZ_BLIND_LOCK_V3`), `agy` (`blind_predictions_full_toe_v7.json`), and `agy-exp` (`X-FLOOR-LINK8` raw vs corrected Split-SUSY/PMNS).
   - Confirm `A2-OW27 v8` `LOCK_V3` digest (`ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a`) intact.
   - **`PF6`:** Tamper one digit of `LOCK_V3` copy in memory and assert digest mismatch caught.
