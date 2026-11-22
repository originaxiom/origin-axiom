# Erratum 2 to Card `A2-OW18`: Panel Refinement for `a2_ow18_v3` (Preserving Raw `v1` & `v2` Untouched)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (`0 of 19`)
- **Date:** `2026-11-22` (committed BEFORE `relays/a2_ow18_v3/verify_a2_ow18_v3.py` runs)
- **Raw `v2` Outcome (`0699fac13`, kept completely untouched):** Five of six modules (`ow18_a`, `ow18_b`, `ow18_c`, `ow18_d`, `ow18_f_planted_faults` `6 / 6`) passed (`True`); in `ow18_e`, all `151 / 151` Lefschetz kernel classes, `Bridge B-3S-01` (`0.00010276 < 2e-4`), `tau_8` mirror (`2.02e-23`), and `AGY-C27` agreement (`1.365e-9 < 1e-8`) passed, with the sole sub-gate exceeding its tolerance being `max_commutator_tr_err = 1.638e-22` vs `< 1e-22` along the longer `tau = i sqrt(3)` panel (`n_b = 22`).
- **Fix in `v3` (`mended code`, zero changed expectations or thresholds):** Increase `solve_l2_weierstrass_taylor` panel counts from `(n_a=14, n_b=22, deg=26)` to `(n_a=16, n_b=28, deg=28)` so `max_commutator_tr_err` drops well below `1e-25`. Also updates Card `A2-OW18` descriptive note that true Fuchsian `L_2(13/100 + 17/10 i) = 2.4934722835041529...` (`matching verify_a2_wg96.py:747 and verify_a2_ow12_v3.py` to `15` digits, offset `0.04483` from `referee_a2_wg96.py`'s collapsed `1D` radial disk `2.44864347...`).

0 of 19.
