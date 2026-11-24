# Card `AGY-C38` — `AGY-C37` Peer-Audit Remediation: Exact `639a5d46b` Line Citations (`D1`) & Complete `B1`/`B4`/`B6` Verification (`D2`) (`0 of 19`)

1. **The package and the question, in a sentence:** Preserving `AGY-C37` and `blind_predictions_full_toe_v7.json` untouched (`0` defects in `v7.json`), does indexing `639a5d46b:verify_x_bulk_link1_v4.py` close `BL1-F1`'s line-citation shift (`D1`), and do independent computations confirm all `6 / 6` `G_{SM} x U(1)_chi` anomalies, `STr M_{Z'_chi}^2 == 0`, `B4` `2HDM` quartics, and `B6` (`71b1718a1` + `OW19-F3`) (`D2`, `0 of 19`)?

2. **What will be delivered, and what done means:** Pre-registered zero-float producer `relays/agy_2026-11-24_c38/c38_remediate_c37_bl1_citations_and_b1_b4_b6_audit.py`, `SCRIPT_SHA256.txt`, first-run `c38_out.json` with `OUTPUT_SHA256.txt` (`computed once`, `expectations committed first`), disjoint cold-room `c38_countercheck.py` (`tested against planted errors`), updated `relays/STATUS_AGY.md`, and relay testing:
   - **`E1` — Dated `2026-11-24` `BL1-F1` Line-Citation & Code-Characterization Erratum on `639a5d46b` (`Closes D1`):**
     - `AGY-C37` cited `verify_x_bulk_link1_v4.py:1155` / `:1152-1156` (`which are actually Planted Control PC_BL1_5: det_single_pt & det_pure_6y_nu`).
     - Exact 0-based line indexing proves `:992` sets non-SUSY `Type-II 2HDM` `b_1 = (21 / 5, -3, -7)`, `:1141, 1164, 1174` evaluate pure-MSSM `b_{mssm} == 5 / 7` (`ignoring the <= ln(2) Scherk-Schwarz threshold span, rather than hardcoding a string literal`), and `:1144-1145` integrate `run_gbs8_rge` over `Delta t = 20` (`under stale :1143 comment L = 28`).
   - **`E2` — Complete `6 / 6` `4D` `G_{SM} x U(1)_chi` Anomalies on `16_+` & Explicit `D`-Flat `STr M_{Z'_chi}^2 == 0` (`Closes D2a,b`, `recomputed independently`):**
     - Compute all `6` `4D` `G_{SM} x U(1)_chi` anomalies (`[SU(3)_C]^2 U(1)_chi`, `[SU(2)_L]^2 U(1)_chi`, `[U(1)_Y]^2 U(1)_chi`, `U(1)_Y [U(1)_chi]^2`, `grav^2 U(1)_chi`, and `[U(1)_chi]^3`) on `16_+ subset Spin(10)`, proving all `6 / 6 == 0` (`counterchecked via 32 x 32 Cl(10) matrix traces`).
     - Construct the `4 x 4` real scalar, massive vector, and `3 x 3` Weyl gaugino-chiralino mass matrices of `(Phi_{+10}, Phi_{-10}, V_chi)` at `<|Phi_+|> = <|Phi_-|> = v_chi` and `s_*`, proving `STr M_{Z'_chi}^2 = 3 M_V^2 + Tr M_{scal}^2 - 2 Tr(M_f^dagger M_f) == 0` (`< 10^{-40}`, counterchecked via `4 x 4` finite-difference Hessian).
   - **`E3` — Explicit `B4` `D / F` `2HDM` Quartics (`SU(2)_L x U(1)_Y` Scrambled) & Full `B6` Verification (`Closes D2c,d`, `recomputed independently`):**
     - Recompute `B4` quartics `(lambda_1..lambda_4)`, Kannike margins (`> 0`), and `m_h^2 / v_{EW}^2 = |lambda_S|^2 / 2` at `4`-modulus Newton `s_*` and `B6`-priced benchmark `lambda_S = 3 / 5` (`< 10^{-14}` vs `639a5d46b`, `< 10^{-48}` `SU(2)_L x U(1)_Y` gauge-basis scrambling).
     - Recompute `B6` at `71b1718a1` (`6 / 6` SHA-256 manifests, `12 == 12` non-overwritten sealed files in `relays/a2_peer_link23{,_referee}/` across `2d993276b..71b1718a1`, and Lamé `b_c^*(tau_8^+)` `< 10^{-35}` vs `71b1718a1` `48`-dps Frobenius and `< 10^{-12}` vs `639a5d46b` `GBS10`). *Unchecked peer scope: `639a5d46b` `fig11` PDF layout/rendering.*

3. **Why this card is self-contained (`blind_predictions_full_toe_v7.json` intact):** `AGY-C37` and `v7.json` (`0` mathematical or custody defects) remain untouched on disk (`WORKING_RULES.md` Rule `3`); `AGY-C38` remedies solely `AGY-C37`'s peer-citation lines and uncomputed `B1`/`B4`/`B6` sub-items.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C37`, `639a5d46b` (`agy-exp`), and `71b1718a1` (`agy-002`). Must not touch sealed past files (`AGY-C1..C37`, `v1..v7.json`), `main`, `agy/audit-2026-11-02`, peer branches, or empirical constants (`0 of 19`).

5. **Five Planted-Error Controls (`tested against planted errors`):**
   - **Control 1 (`BL1-F1` line-index shift trap):** Asserting `b_mssm` or `run_gbs8_rge` on `:1152-1156` must fail, while `:992, 1141, 1143-1145, 1164, 1174` match identically.
   - **Control 2 (`6 / 6` `G_{SM} x U(1)_chi` anomaly completeness):** Dropping `nu^c` (`Q_chi = -5` in `639a5d46b`'s `h_chi` basis) leaves all `4` `G_{SM}` mixed anomalies `0` while breaking `sum Q_chi = +5` and `sum Q_chi^3 = +125` (`proving all 6 anomalies are needed`).
   - **Control 3 (`SUSY` `D`-flat `STr M_{Z'_chi}^2 == 0` vs soft breaking):** Adding soft scalar mass `+Delta m^2` breaks `STr M^2 == 0` to `4 Delta m^2 > 0`.
   - **Control 4 (`B4` `SU(2)_L x U(1)_Y` scrambling & `lambda_S = 0` runaway):** Independent `SU(2)_L` rotations break `|H_u . H_d|^2` (`> 1 / 10`), equal `U(1)_Y` phases break `Re(H_u . H_d)` (`> 1 / 10`), and `lambda_S = 0` collapses Kannike margin `3` to `0`.
   - **Control 5 (`B6` `71b1718a1` manifest tamper & `OW19-F3` cusp bound):** Tampering any `71b1718a1` manifest digest fails `6 / 6`, while `b_c^*(tau_8^+)` matches `71b1718a1` to `< 10^{-35}` and `639a5d46b` `GBS10` to `< 10^{-12}`.

0 of 19.
