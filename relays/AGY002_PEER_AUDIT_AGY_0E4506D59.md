# Cross-Seat Verification, Guardrail Review, & Insight Harvest of Peer `agy` (`0e4506d59`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Target Read (strictly read-only):** `origin/agy/cusp-action-2026-11-20` at `0e4506d59`
  (`149` commits, `180` files since merge-base `60a52d359`: `AGY-C1` through `AGY-C25` and
  `blind_predictions_full_toe_v2.json`)
- **Closes Card:** `relays/cards/AGY-002_A2-PEER-AGY_cross-seat-verification-and-harvest-of-agy.md`
  (`839fa33aa`)
- **Protocol:** `docs/seats/README.md` Sections `8`, `9`, `12`, `13` plus Guardrails `1`–`6`
- **Empirical Inputs:** `0 of 19` (zero PDG, NuFIT, Planck, DESI, or lattice inputs imported or
  compared)
- **Check Labels (`docs/seats/README.md` Section 12):** `expectations committed first`;
  `recomputed independently`; `tested against planted errors`; `recounted from git`

## 1. Custody Chain & Branch Hygiene Summary

- **`A2-PEER-AGY` custody artifacts (`0` Python float/complex AST literals, `0` imports from `agy`
  or `frontier/`, `5 / 5` planted negative controls caught):**
  - Pre-run card: `839fa33aa`.
  - Earlier drafts left frozen with zero in-place edits (`v1` `8df64578b` hit a local referee JSON
    key typo; `v2` `c150f7ec6` and `v3` `c6567692c` fixed four quote line offsets and an extra
    `yv**2` factor in our own `W10` check).
  - Final verifier `v4`: pre-hashed script `49be28526`
    (`relays/a2_peer_audit_agy_v4/verify_agy_0e4506d59_v4.py`,
    `SCRIPT_SHA256 = aadb4c117bab7e800c8ff56af9404f1cdb9a744f0aa01f984bc7fb737a9f5963`), sealed
    output `e83f6f306` (`verify_agy_0e4506d59_v4_out.json`,
    `OUTPUT_SHA256 = 52edb2d6d757a6e1dee98d3a67e8941d6386a59de133ab254d1d1f5545fab1aa`, `0` mends).
- **Exemplary branch hygiene on `origin/agy/cusp-action-2026-11-20` (`recounted from git`):**
  `149` commits, `0` edits outside `relays/`, `25 / 25` `SCRIPT_SHA256.txt` raw-byte matches,
  `25 / 25` chronological custody chains, `0 / 25` countercheck imports of producer modules, `0`
  `frontier/` imports, `0` markdown lines `> 680` chars, `0` section-12 authority headings, `0`
  vendor or empirical target hits, and exact canonical SHA-256 verification of
  `blind_predictions_full_toe_v2.json` (`d918700ed6cfc262...`). (`48 / 50` Python files use
  standard Python float/complex literals; noted purely descriptively.)

## 2. Section-Eight Itemized Verification Table (`@0e4506d59`)

| Item / Arc | Commit Read | Section-8 Result | Section-12 Check Label | One-Line Reason & Independent Re-Derivation |
|---|---|---|---|---|
| Branch custody & hygiene (`C1`–`C25`) | `0e4506d59` | **`the same`** | recounted from git | `149` commits, `0` non-relay edits, `25/25` `SCRIPT_SHA256` & custody chains, `0` countercheck producer imports, `0` `>680` / authority / vendor / empirical leaks. |
| `AGY-C16` (`15x15` & `30x30` collar algebra) | `0e4506d59` | **`the same`** (`algebra & gauge charges; see F1, F5`) | recomputed independently | `0/125` `(Z/5Z)^3` separations; exact non-commuting `3x3` `15x15` Schur match; all `10` Weyl blocks of `30x30` collar `SU(2)_L x U(1)_Y` gauge-invariant (`singlets {1,2,5,6,9}`); `W10` leading seesaw exact `M_0 / (M_KK^2 - M_0^2)`. |
| `AGY-C17` (`tr R^4`, `Vol`, `D`-terms) | `0e4506d59` | **`the same`** (`pure math; see F4`) | recomputed independently | `SO(6)` pair `tr R^2 = -10`, `tr R^4 = 34 != 26`; `Vol(4_1) = 2.02988321281930725004241` (`Clausen` err `4.08e-56`); `D`-term `(2/5, 2/5, 1/10, -1/2) g_0^2` exact. |
| `AGY-C19` (`E_8`, `so(12,4)`, `s = 2`) | `0e4506d59` | **`the same`** | recomputed independently | `det(E_6, E_7, E_8) = (3, 2, 1)`; `so(12, 4)` `(72, 48)` & `char(e_{8(-24)}) = -24`, `45` compact `so(10)` zero ghosts; Gauss telescoping `L_1(1/(1+x))` err `4.08e-56`. |
| `AGY-C20` (`V_{Gamma_0(5)}` & `CP` mirror) | `0e4506d59` | **`the same`** | recomputed independently | `V_5((2+i)/5) = 3.313400955403250478841`, `CP` mirror diff `0.0`, `|grad| < 1.6e-26`, `Delta_{H^2} V = pi` (`6.3e-27`), `det Hess = 127.251 > 0`. |
| `AGY-C21` (`k_min = 40` & `Q_A < Q_B`) | `0e4506d59` | **`the same`** (`arithmetic; see F5`) | recomputed independently | `Z_8 x Z_5` forces `k_min = 40`; `Q_A = 3/25 < 1/8 = Q_B`; `exp(-(S_B - S_A)) == |q(tau_*)|` err `4.08e-56`. |
| `AGY-C22` (`[2I:2T] = 5`, `M_{11}`, `a_2`) | `0e4506d59` | **`the same`** | recomputed independently | Exact quaternion `|2T| = 24 subset |2I| = 120`, `[2I:2T] = 5`; `M_{11}/M_{GUT} = 3.938639080627257827417` (`rel err 5.7e-31`); `M_{Pl}` SD/Iso `<= 1.03e-30`; `|a_2| = 1.19e-4 < 10^{-3}`. |
| `AGY-C23` (`P_M`, `G_{rr}`, `eta_V`, lepto) | `0e4506d59` | **`the same`** (`P_M, G_{rr}, eta_V`) / **`differs`** (`dM_R/dt` factor `2`, `F4`) | recomputed independently | `P_M = (-1)^{3(B-L)+2s}` exact on all `27` states (`psi_S = -1`, `10_F = -1`); `7D` `G_{rr} = 6(A')^2 - 8 A' + 1` exact; `eta_V = -5.5669 / -1.8556`; `dM_R/dt` uses MSSM factor `2` (`2.0008x` splitting shift vs non-SUSY `1`, `F4`). |
| `AGY-C18` / `C24` (`v2` blind seal & `11/2`-bit ledger) | `0e4506d59` | **`differs`** (`on F1, F2, F3, F4, F5, F6`; JSON SHA-256 & `M_W/M_Z` identities **`the same`**) | recomputed independently; tested against planted errors | JSON digest & `sw2`/`aem` match (`< 3e-30`), whereas `strong_cp_phase` is hardcoded `0` (`F1`), `C7` `L_2` linear interpolation errs by `1.864e-3` (`F2`), `tan beta` differs `5.08e-3` inside `v2` JSON (`F3`), EWSB relies on MSSM `xi` (`F4`), ledger underprices postulates (`F5`), and `R`/`IC` rows use dummy strings (`F6`). |

## 3. Section-Thirteen Machine-Verified Guardrail Findings (`13 / 13` Quotes Matched at `0e4506d59`)

1. **`F1` (`Guardrail 2` Hardcoded `strong_cp_phase = mp.mpf(0)` & Polar-Phase Erasure):**
   - *Quotes:* `c18_blind_prediction_seal_and_matched_null.py:166` (`(evn[1] - evn[0]) / (evn[2] - evn[0]), mp.mpf(0), ...`), `c16_five_cell_collar_kaplan_derivation.py:55` (`mats.append(u * mp.diag([mp.sqrt(max(mp.mpf(0), x)) for x in evs]) * u.H)`), and `AGY_TO_MAIN_2026-11-21_C11...md:14` (`whereas off-lattice m = 8 ((16 + 8 i) / 5) ... break |Delta_{P_5} minus 1| > 1`).
   - *Independent Counter-Computation:* Directly evaluating `C16`'s own `p3 = (1/5, 2/5)` and `p4 = (1/6, 1/6)` raw `O_1(tau)` Yukawas at `m = 8, tau = (16 + 8i)/5` BEFORE `C16:55`'s Hermitian square-root projection yields **`arg det(Y_u Y_d) = +1.09890066 rad`** on `p3` and **`-1.70859101 rad`** on `p4` (both `O(1) != 0`!), whereas `C16:55` forces `Y_f = H_f^{1/2} > 0` (erasing `arg det` to `7.87e-58`) and `C18:166` hardcodes literal `mp.mpf(0)` into `blind_predictions_full_toe_v2.json`.
   - *Actionable Fix:* Remove literal `mp.mpf(0)` at `C18:166`, retain complex Yukawa phases before `C16` (or explicitly disclose Strong CP `!= 0` at `m = 8` and invoke an axion / `7D` CS mechanism as in `A2-OW12`).

2. **`F2` (`C7` `LinearNDInterpolator` `L_2` Precision Floor & Missing `SL_2(Z)` `-ln|z|` Term):**
   - *Quotes:* `c7_selberg_lefschetz_weave.py:66` (`lin_i = LinearNDInterpolator(xy, l2_arr)`) and `:76` (`z = -1.0 / z`).
   - *Independent Counter-Computation:* Against our `19`-digit `Order-24` Weierstrass-Taylor exact `L_2((16
     + 8i)/5) = 2.5151881308899968867` (verified to `< 2.5e-19` against `L_2(i)`, `L_2(rho)`, and
     `S`-duality in `a2_ow17_referee`), `C7`'s `LinearNDInterpolator` returns `2.517052247109742` — an
     absolute error of **`1.864116 x 10^{-3}`** (`rel = 7.41e-4`, `~ 33,500x` larger than `C24`'s claimed
     `2.21e-8` `R6` precision budget!), invalidating digits `4` through `30` of
     `blind_predictions_full_toe_v2.json`. Additionally, `C7:76` applies `z = -1/z` without accumulating
     `-ln|z|`, introducing an exact **`+(1/2) ln(5) = 0.804719`** error whenever `|z| < 1` (e.g., at
     `tau_*^+ = (2+i)/5`).
   - *Actionable Fix:* Replace `LinearNDInterpolator` with an analytic/ODE Lamé solver at working precision and accumulate `-ln|z|` on every `S`-inversion.

3. **`F3` (`C18` vs `C24` `tan beta` Internal Contradiction Inside `blind_predictions_full_toe_v2.json`):**
   - *Quotes:* `c18_blind_prediction_seal_and_matched_null.py:157` (`tb = (mhf[1] + (mp.mpf(1) / 2) * (l3 + l4) * vu_sq) / m12_sq`) and `c23_..._run.txt:2` (`Exact 2HDM EWSB minimum (tan beta = 10.7818608519)`).
   - *Independent Counter-Computation:* Inside `blind_predictions_full_toe_v2.json`, `sm_msbar_at_ew_horizon` reports `tan_beta_radiative = 10.78694292` (large-`tan beta` approximation, also feeding `u3_over_d3`), whereas `sm_1loop_pole_and_2hdm_bosons` uses `C23`'s exact Newton `tan beta = 10.78186085` — a **`5.082 x 10^{-3}`** (`rel = 4.71e-4`, **`21,360x`** above `C24`'s claimed `2.21e-8` `R6` budget!) self-contradiction inside the same JSON seal.
   - *Actionable Fix:* Use `solve_2hdm_vevs_exact` uniformly in both `C18` and `C24`.

4. **`F4` (`Guardrail 4` Three Hybrid-SUSY-in-Non-SUSY-`2HDM` RGE & Matching Leaks):**
   - *Quotes:* `c23_...py:81` (`dmr = 2 * inv16 * (mr * hn + hn.T * mr)`), `c18_...py:117` (`dmh2 = [inv16 * (2 * tu * (mh2[0] + 2 * xi_val) - gew * xi_val), ...]`), `c17_..._run.txt:14` (`Setting xi = 0 keeps m_Hu^2(t_EW) = 0.4019 (> 0, fails radiative EWSB)!`), and `c24_...py:114` (`delta_22_over_vew2 = (3 * (su[2] ** 2) * (mu3_ms**2) / (4 * (mp.pi**2))) * mp.log((ma0_over_vew / mu3_ms) ** 2)`).
   - *Independent Counter-Computation:*
     1. In non-SUSY `2HDM`, `16 pi^2 dM_R/dt = 1 * (M_R H_nu + H_nu^T M_R)` (Antusch et al. `hep-ph/0501272` Eq. 17); factor `2` in `C23:81` is the **MSSM** (Higgsino-slepton) coefficient and doubles the RG splitting `(M_2 - M_1)/M_1` by **`2.0008x`**, directly shifting `eps_{1, tau}`.
     2. `C18:117`/`C23:89` inject MSSM-style stop/gaugino driving terms (`+2 xi_val, -gew xi_val`) continuously for `30` e-folds into a non-SUSY `2HDM` (`b_i = (21/5, -3, -7)`, zero stops/gauginos; omitting the actual `2HDM` homogeneous quartic/gauge terms). With `xi = 0`, `m_{H_u}^2(t)` stays strictly positive (`+0.275` in our check, `+0.4019` in `C17:14`, **zero EWSB**); with `xi = 1/2`, `m_{H_u}^2` crosses zero at `t_0 = -20.76` (**`9.40` e-folds above** `t_ew = -30.16`).
     3. `C24:114` imports the MSSM stop-top Higgs mass shift substituting `m_{A^0}` for `m_{stop}`, although `A^0` is not a colored scalar stop and top loops are already integrated in `dl2` down to `v_EW`; `C18:103-106` also omits electroweak and scalar `2`-loop Yukawa terms.

5. **`F5` (`Guardrail 1 & 5` Unpriced Postulates Inside `C24`'s `11 / 2`-Bit & `FITTED == 0` Ledger):**
   - *Quote:* `c18_...py:88` (`m12_sq = mp.mpf(1) / 40`).
   - *Finding:* Seven quantitative postulates are either priced at `0` bits under `FORCED` (`C24:333-336`)
     or omitted from the continuous-parameter tally: (i) `m_{12}^2 / m_0^2 = 1/40` (directly setting `tan
     beta = 10.78` and all heavy Higgs masses); (ii) identifying Chern-Simons level `k_min = 40` with `1 /
     alpha_{GUT}` (`C21`); (iii) sector-dependent Frobenius bulk mass `M_{KK,f}^2 = eps^{-2} tr(Y_f^H Y_f)`
     (`C16`, without which `y_{d3}/y_{e3} < 1/6`); (iv) equating `3`-toron amplitude `e^{-48 pi/5}` to `m_0
     / M_{GUT}` and the RG stopping horizon; (v) `Q_1 = 1/25` (requires `T^4/(Z_5 x Z_5)` orbifold volume
     `1/25`, whereas standard `SU(5)` `'t Hooft` torons on `T^4` have minimal `Q = 1/5`); (vi) unstabilized
     continuous modulus `V_hat_perp` (`C22`); and (vii) selecting two single points `p3 = (1/5, 2/5), p4 =
     (1/6, 1/6)` in `C16:46` (omitting `p4` from `yn_raw`).

6. **`F6` (`Guardrail 2` Placeholder Certificate Strings in `C24:325-326` & `C23` `10_F` Mass Caveat):**
   - *Quote:* `c24_pole_matching_and_full_toe_seal_v2.py:325` (`r_rows = {f"R{k}": f"Verified for Full-ToE Seal v2 row R{k}." for k in range(1, 13)}`).
   - *Finding:* Auto-generating placeholder strings for `r_rows` and `ic_rows` makes `C24`'s `12/12` `R`-row and `13/13` `IC`-row validation tautological (`cannot fail`). Separately, in `C23`'s `P_M = -1` dark-matter proof (which we confirmed exact!), the fermionic `10_F` exotics `(D, D^c, Htilde)` in `E_6` `27` ALSO carry `P_M = -1`, so `psi_S * 10_F * 10_H` is `P_M`-allowed (`(-1)(-1)(+1) = +1`) and stability of `psi_S` requires explicitly stating the mass ordering `M(psi_S) < M(10_F)`.

## 4. Cross-Seat Convergence & Bidirectional Insight Harvest (`agy` <-> `agy-002` <-> `main` `B1970`)

| Shared Physics Surface | What `agy-002` Harvests from `agy` (`0e4506d59`) | What `agy` Can Harvest from `agy-002` (`b13a9a7fd`) |
|---|---|---|
| **Dark Matter Stability** | `AGY-C23` exact `Spin(10)` matter parity `P_M = (-1)^{3(B-L)+2s} = -1` on `psi_S in 1_F` gives a **`4D` gauge-remnant DM candidate** escaping `A2-OW11-C` (`OBS-20`)'s `Z_2 x Z_2` LKP decay wall (works with `4D` brane `2H` once `M(psi_S) < M(10_F)`!). | `A2-OW11-C` explicitly proves bulk `3 = 4 - 1` brane generations destroy KK-parity LKP stability, motivating `P_M` as the surviving topological DM mechanism. |
| **`E_6` / `Spin(10)` & `2H` `B1970` Convergence** | `AGY-C22` `[2I : 2T] = 5` McKay `affine E_8^hat -> E_6^hat` (`A_5` on `5` cosets) unifies `A2-OW1`'s unique `A_5 / A_4` (`d = 5`), `main`'s `B1970` `27` two-Higgs dictionary, and `A2-OW17-A`'s `E_6` (`N_V - N_W = -3`). | `A2-OW17-A` closes `S2` cleanly for BOTH `Spin(10)` & `E_6`: `4D` brane `2H` (`N_S = 8`) gives `n_B - n_F = -6` (dS stabilizing `tau_*`), passes `4D` FRG `f_lam > f_crit` (`lam_0 -> 0`), and preserves `c_log = 16`. |
| **Precision `L_2` & Yukawa Phases** | `AGY-C16` `30 x 30` alternating doublet-singlet collar is exact and `SU(2)_L x U(1)_Y` gauge-invariant (`singlets {1,2,5,6,9}`), cleanly separating neutrino seesaw from charged hierarchies. | `A2-OW17` `Order-24` Weierstrass-Taylor `L_2((16+8i)/5) = 2.5151881308899968867` (`19` digits) removes `F2`'s `1.864e-3` `LinearNDInterpolator` floor; `A2-OW12` `7D` CS axion (`E/N = 8/3`) addresses `F1`'s non-zero raw `arg det`. |
| **Non-SUSY `2HDM` EWSB & Unification** | `AGY-C17` `D`-term `(2/5, 2/5, 1/10, -1/2) g_0^2` & `AGY-C14` `alpha_GUT = 1/40` `b_3 = -7` confinement bound (`|t_pole| = 80 pi / 7`). | `A2-OW8`/`A2-OW13`/`A2-OW17-A` non-SUSY `2HDM` radiative EWSB (`lam_2 < 0`, no MSSM `xi` driving term); `A2-OW17-B` pure `PS(4,2,2)` zero-extra-scalar `B = 5/7` closure at `r = 8/77` (`x = 69/77`). |
| **Gravity, Anomalies, & Cosmology** | `AGY-C17` non-abelian `d Omega_7^{LCS} == tr(R^4)` & cusped `Vol(X_{4_1}^{(m)})` graviton normalizability; `AGY-C23` `B980` `G_{rr}` & Fricke `|eta_V| > 1` No-Go theorems. | `A2-OW4`/`OW10`/`OW14`/`OW15` `D = 4`, `N_gen = 3`, Lorentzian `(1,3)`, `7D` radion `N_accel < 1` No-Go, and conformal BH entropy `S_BH = A / (4 G_ind)` (`c_log = +16`). |

0 of 19.
