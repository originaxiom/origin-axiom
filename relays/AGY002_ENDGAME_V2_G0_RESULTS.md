# `AGY-002_ENDGAME-V2-G0` — Gate 0 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `b59b2458b`: `relays/cards/AGY-002_ENDGAME-V2-G0_literature-rge-and-haar-invariance-lock.md`
  - Erratum card commit `46f43c26f` (prior to any output file): `relays/cards/AGY-002_ENDGAME-V2-G0-ERRATUM_mp-log-sign-bisection.md`
  - First script seal `76a59ae79`: `relays/agy002_endgame_v2_g0_fixed/verify_endgame_v2_g0_fixed.py`, `relays/agy002_endgame_v2_g0_fixed/SCRIPT_SHA256.txt` (unmodified prior script at `faead675a`: `relays/agy002_endgame_v2_g0/verify_endgame_v2_g0.py`, `relays/agy002_endgame_v2_g0/SCRIPT_SHA256.txt`)
  - First output seal `b35660cc7` (committed unread): `relays/agy002_endgame_v2_g0_fixed/verify_endgame_v2_g0_fixed_out.json`, `relays/agy002_endgame_v2_g0_fixed/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Second script seal `71d4fbef4` (built from the card and published literature alone without reading or importing the first script): `relays/agy002_endgame_v2_g0_referee/referee_endgame_v2_g0.py`, `relays/agy002_endgame_v2_g0_referee/SCRIPT_SHA256.txt`
  - Second output seal `841f3031d` (committed unread): `relays/agy002_endgame_v2_g0_referee/referee_endgame_v2_g0_out.json`, `relays/agy002_endgame_v2_g0_referee/OUTPUT_SHA256.txt`
- **tested against planted errors:**
  - `4 of 5` planted cases exceeded `0.25` in `relays/agy002_endgame_v2_g0_fixed/verify_endgame_v2_g0_fixed_out.json` (`PF0.1` evaluated there only on pure-gauge `B0.1` at shallow step `-15`, giving `0.17532544356533436`, which is `1.75e6` times the `1e-7` solver lock but below `0.25`);
  - `5 of 5` planted cases caught in `relays/agy002_endgame_v2_g0_referee/referee_endgame_v2_g0_out.json` when evaluated on the card's full `PF0.1` specification (`B0.2` relative shift `1.0000000000005378 > 0.25`, `B0.1` at `-30` relative shift `0.880941503251885 > 0.25`, `B0.1` at `-25` relative shift `0.43832101783208366 > 0.25`, while reproducing the `-15` shift `0.17532544356533597` to `1.61e-15`).

## 2. Numerical Summary (`0 of 19`)

| Check | First Computation (`verify_endgame_v2_g0_fixed_out.json`) | Second Computation (`referee_endgame_v2_g0_out.json`) | Bound |
|---|---|---|---|
| AST zero float literals & allowed imports | `0` floats, `True` | `0` floats, `True` | `0` floats |
| Exact `SU(4)_c x SU(2)_L x SU(2)_R` & `SM` 1-loop slopes & `Buttazzo et al. (2013)` 2-loop polynomials | `b_SM = (41/10, -19/6, -7)`, `b_PS = (-10, -7/3, -7/3)`, `(3/5, 2/5)`, `True` | `C_2(adj) = (2,3,4)`, `b_SM = (41/10, -19/6, -7)`, `b_PS = (-10, -7/3, -7/3)`, `(3/5, 2/5)`, `True` | Exact |
| `B0.1` `2`-loop single-gauge exact antiderivative vs ODE | `3.322e-15` (`RK4` at `-15`) | `7.840e-14` (`-15`), `3.985e-13` (`-25`), `8.296e-15` (`+30`, `DOP853`) | `< 1e-7` |
| `B0.2` `Buttazzo et al. (2013)` `2`-loop quartic zero-crossing `t_crit` | `7.578626559317348` (`rel_err = 1.860e-13`) | `7.578626559316068` (`rel_err = 2.567e-13`; cross-script diff `1.689e-13`) | `< 1e-7` |
| `B0.3` `2`-loop non-commuting complex `3 x 3` Yukawa flow & `1`-loop `Xing-Zhou` Jacobi identity | `1.616e-11` / Jacobi `9.415e-14` | `1.650e-13` (`DOP853` vs `mpmath`) / Jacobi `5.773e-15` | `< 1e-7` / `< 1e-10` |
| `B0.4` `1`-loop `Antusch et al. (2003)` Weinberg operator matrix flow | `7.153e-14` | `5.014e-15` | `< 1e-9` |
| Pre-`RGE` random Haar `U(3)^6` basis-scrambling (`21` observables, Fujikawa `bar_theta`) | `1.033e-14` (`8` trials); `RGE` `theta` shift `1.288e-14` | `1.033e-14` (`DOP853`, `12` trials), `3.197e-14` (`RK4`); `RGE` `theta` shift `1.377e-14` | `< 1e-12` |

## 3. Result for Gate 0

Both independent `2`-loop matrix `RGE` and `Pati-Salam -> seesaw -> SM` threshold implementations satisfy the `0 of 19` AST lock, exact Lie-algebraic and `Buttazzo et al. (2013)` rational polynomial identities, all `4` published benchmark classes to `10`–`14` significant figures (exceeding the `3`-significant-figure requirement and `< 1e-7` tightened lock), pre-`RGE` random Haar `U(3)^6` invariance to `< 3.2e-14`, and all `5` planted fault controls on the card's specification. Gate 0 is locked. `0 of 19.`
