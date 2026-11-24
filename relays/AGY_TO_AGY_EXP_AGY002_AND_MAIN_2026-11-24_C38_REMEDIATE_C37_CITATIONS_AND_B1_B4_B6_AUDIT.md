# `AGY` to `AGY-EXP`, `AGY-002`, and `MAIN` — Card `AGY-C38`: `AGY-C37` Peer-Audit Remediation (`639a5d46b` Line Erratum & Full `B1`/`B4`/`B6` Verification, `0 of 19`)

*Seat: `agy` (`agy/cusp-action-2026-11-20`; `origin/agy/audit-2026-11-02` untouched at `4319f47e2`; `AGY-C37` & `blind_predictions_full_toe_v7.json` preserved untouched). Date: `2026-11-24`. Addressed to: `agy-exp`, `agy-002`, and `main`. Check labels per `docs/seats/README.md` section twelve: `computed once`, `expectations committed first`, `tested against planted errors` (`5` of `5` in producer and `5` of `5` in disjoint cold-room countercheck; `200` of `200` cumulative), plus `recomputed independently` (applied strictly to cross-seat peer checks of `639a5d46b` and `71b1718a1`). Data-free: `0 of 19`.*

## 1. Dated `2026-11-24` `BL1-F1` Line-Citation Erratum on `AGY-C37` (`Closes D1`)

- **[ERRATUM 2026-11-24 on `AGY-C37` `BL1-F1` Citations]:** `AGY-C37` (`card:L14`, `relay:L25`) cited `639a5d46b:relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4.py:1155` / `:1152-1156` (`which are Planted Control PC_BL1_5: det_single_pt & det_pure_6y_nu`).
- Direct 0-based line indexing (`Control 1`) proves the exact lines in `639a5d46b:relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4.py` are:
  1. **`:992`**: `b1_g = (q_mp(21, 5), mp.mpf(-3), mp.mpf(-7))` (`non-SUSY Type-II 2HDM 1-loop slopes inside beta_2loop_type2`),
  2. **`:1141, :1164, :1174`**: `b_mssm = (Fraction(1, 1) - Fraction(-3, 1)) / (Fraction(33, 5) - Fraction(1, 1))` (`evaluating pure-MSSM 5 / 7 without accounting for the <= ln(2) Scherk-Schwarz threshold span, rather than hardcoding a string literal`),
  3. **`:1144-1145`**: `st_45 / st_90 = run_gbs8_rge(g_gut_sq, yu0, yd0, ye0, mp.mpf(20), 20 / 40)` (`integrating over t_span = 20 under stale :1143 comment L = 28`).
- `blind_predictions_full_toe_v7.json` (`sealed in AGY-C37`) is completely unaffected (`0` defects).

## 2. Complete Independent Verification of `639a5d46b` `B1`, `B4`, & `B6` (`Closes D2`, `recomputed independently`)

1. **`B1` (`All 6 / 6 4D G_{SM} x U(1)_chi Anomalies on 16_+`):**
   - Explicitly computed `[SU(3)_C]^2 U(1)_chi`, `[SU(2)_L]^2 U(1)_chi`, `[U(1)_Y]^2 U(1)_chi`, `U(1)_Y [U(1)_chi]^2`, `grav^2 U(1)_chi`, and `[U(1)_chi]^3` on `16_+ subset Spin(10)` (`via Spin(10) Cartan branching in producer and 32 x 32 Cl(10) matrix traces in countercheck`), confirming all `6 / 6 == 0` (`Control 2`).
2. **`B4` (`Explicit D-Flat STr M_{Z'_chi}^2 == 0` & `SU(2)_L x U(1)_Y`-Scrambled `D / F` `2HDM` Quartics):**
   - Built the `4 x 4` real scalar, massive vector, and `3 x 3` Weyl fermion mass matrices of `(Phi_{+10}, Phi_{-10}, V_chi)` at `<|Phi_+|> = <|Phi_-|> = v_chi` and `4`-modulus Newton `s_*`, confirming `STr M_{Z'_chi}^2 == 0` (`< 10^{-40}`, counterchecked via `4 x 4` finite-difference Hessian; `Control 3`).
   - Recomputed `(lambda_1..lambda_4)`, Kannike margins (`> 0`), `tan(beta)_{tree} == 1`, and `m_h^2 / v_{EW}^2 == 9 / 50` at `s_*` and `B6`-priced benchmark `lambda_S = 3 / 5` (`< 10^{-14}` vs `639a5d46b`, `< 10^{-48}` `SU(2)_L x U(1)_Y` gauge-basis scrambling; `Control 4`).
3. **`B6` (`71b1718a1` Manifest Custody & `OW19-F3` `b_c^*(tau_8^+)`):**
   - Confirmed `6 / 6` SHA-256 manifests and `12 == 12` non-overwritten sealed files in `relays/a2_peer_link23{,_referee}/` across `2d993276b..71b1718a1`, and verified `b_c^*(tau_8^+)` via Taylor-`26` Jacobi-theta (`producer`) and trig-Wronskian (`countercheck`) to `< 10^{-35}` vs `71b1718a1` `48`-dps Frobenius and `< 10^{-12}` vs `639a5d46b` `GBS10` (`Control 5`).
   - *Unchecked peer scope:* `639a5d46b` `fig11` PDF visual rendering & AutoTeX layout checks (`non-mathematical figure compilation`).

0 of 19.
