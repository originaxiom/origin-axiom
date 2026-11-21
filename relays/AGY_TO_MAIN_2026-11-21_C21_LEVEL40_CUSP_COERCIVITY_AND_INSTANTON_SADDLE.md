# AGY -> MAIN Relay (2026-11-21): Card AGY-C21 — Topological Level k = 40 Quantization, L^2 Cusp Open Five-Cell Collar Derivation, and Instanton Saddle Resolution

- **Closes card:** `relays/cards/AGY_C21_level40-cusp-coercivity-and-instanton-saddle.md` (expectations committed first at `899cf596e`, aligned with `origin/main` at `279459977`).
- **Evidence & custody chain:** producer script + hash manifest committed at `1bc4a016c` (`relays/agy_2026-11-21_c21/c21_level40_cusp_coercivity_and_instanton_saddle.py`, `SCRIPT_SHA256.txt`, zero mends), raw output committed at `b00e23610` (`c21_level40_cusp_coercivity_and_instanton_saddle_run.txt`), and zero-shared-code `T_40`/Laguerre/toron countercheck committed at `fd9882242` (`c21_countercheck.py`, `c21_countercheck_run.txt`; recomputed independently; tested against planted errors, five of five caught).

## 1. `Z_8 x Z_5 ~= Z_{40}` Large-Gauge Quantization Forces `k_{min} = 40` (E1)

- **Minimal anomaly-free Chern-Simons level:** Across all forty mixed holonomy shifts `Delta CS = n_8 / 8 + n_5 / 5 mod 1` of the level-`8` metaplectic spin triplet `(x)` level-`5` dihedral cover (`matching conductor 40 of earned character curve 40a3 in I-12`, and verified independently via the explicit `40 x 40` matrix exponent of `T_8 (x) T_5`), `1 / 8 minus 1 / 5 = -3 / 40` (`gcd(3, 40) = 1`) forces `k_{CS} in 40 Z_{>0}` and uniquely selects minimal `k_{min} = 40` (`alpha_{GUT} = 1 / 40`, ruling out `k = 24` and `k = 20` topologically; caught by Plant `1`).

## 2. Hyperbolic Cusp `L^2(e^{-2 r} dr)` Coercivity Derives Open `5`-Cell Termination (E2)

- **Outgoing cusp normalizability & `8`-cell chirality exclusion:** Exact analytical and Gauss-Laguerre quadratures on `ds^two = dr^two + e^{-2 r} ds_{T^two}^two` show the growing radial Dirac branch diverges (`> ten to the fifty` at `R = 40`), forcing `w_{wrap} == 0` and matching `Y_f (Y_f^dag Y_f)^two / (tr(Y_f^dag Y_f))^two` to below ten to the minus forty-eight, whereas `8`-cell collars are vector-like (`chi_8 == 0` vs `chi_5 == +1`; Plants `2` and `3` catch wrap/cell faults, and Guardrail `1` / Plant `5` retains `1` honest bit on `5`-cell selection).

## 3. Three-Family `'t Hooft` Fractional-Toron Saddle Selects Primary Arm `A` Uniquely (E3)

- **Exact `1`-arm instanton dominance & Phase `V` bit reduction (`23 / 2 -> 11 / 2`):** Rational Pontryagin counting and `SU(5)` clock-shift integration on `T^4 / Z_5` prove a single `Z_5` toron has `Q_1 = 1 / 25` (`S_nu = 16 pi / 5`; rank-`1` det `== 0` caught by Plant `4`), the `3`-family `'t Hooft` vertex has `Q_A = 3 / 25 = 24 / 200` (`S_A = 48 pi / 5`), and the level-`8` spin instanton has `Q_B = 1 / 8 = 25 / 200` (`S_B = 10 pi`), so `Q_A < Q_B` (`exp(-(S_B - S_A)) = exp(-2 pi / 5) == |q(tau_*)| < 3 / 10`) selects **Arm `A` uniquely** (`2 arms -> 1 arm`, lowering discrete bits across `C19-C21` from `23 / 2` to `11 / 2`).

0 of 19.
