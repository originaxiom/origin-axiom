# `AGY-002` Card `A2-P879` Erratum `4` — Unrounded `T3` Rational Comparison & `v5` Sealed Producer (`0 of 19`)

- **Date:** `2026-11-20`
- **Cold-Room Referee Final (`9 / 9` PASS):** `relays/a2_p879_referee_v3/` (`43d61262d` / `01466ab8a`, `A`-only manifests) passed all `9 / 9` gates (`all_gates_passed = true`) and stands final with zero further modification.
- **Producer `v4` (`2a666fe82`) Finding & `v5` Fix (`relays/a2_p879_v5/`):** Producer `v4` passed `6 / 7` gates (`including T3 max_grid_vs_mobius_err < 10^{-9}` matching Referee `v3`), failing only line `655` because line `639` stored `exact_mobius = round(exact_mob, 8)` (`33333333 / 100000000`) before checking `|exact_mobius - 1/3| < 10^{-14}`. Companion `relays/a2_p879_v5/` retains unrounded `float(exact_mob)` in `run_T3_spinor_mobius`, computes singular values with `compute_uv = False` before computing left singular vectors only on `both_gap` boxes, and applies exact unit-bidisk filtering (`|z_0| <= 1, |z_1| <= 1`) on subdivided boxes while leaving `v1`–`v4` and `referee_v1`–`referee_v3` untouched.

0 of 19.
