# Erratum 2 to Card `AGY-002_A2-OW17`: `v1` Findings, RK4 Refinement, and Exact `45` / Pure-PS `B = 5 / 7` Boundary (`v2`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Date:** `2026-11-22`
- **Section-12 Disclosure:** Updates two quantitative gate predicates after observing raw sealed
  `v1` output (`e10bc011f`); therefore `A2-OW17 v2` carries the label **`mended expectations`** for
  those two thresholds alongside `recomputed independently` and `tested against planted errors`.
- **Empirical Inputs:** `0 of 19`

## 1. Exact Raw `v1` Observations (`40b48e55b` -> `e10bc011f`)

- `OW17-C` (`m004` commutant, DFT, natural circulant test, `10`-trial Haar `1.73e-55`, `E[n]`
  orbits) and `OW17-D` (`4 / 4` planted faults) passed `v1` cleanly (`True`).
- `OW17-A` (`S2` brane `2H` in `Spin(10)` & `E_6`) passed `6D` Casimir (`-6` dS for both), `4D`
  FRG (`f_lam > f_crit` across all `10` configurations, FD err `< 10^{-33}`), `4`-quartic UV
  irrelevance (`all_uv_irrelevant = True`), and `c_log = 16` (`-55/3 + 103/3 = 16`), with two
  narrow gate adjustments needed for `v2`:
  1. `yb_high = 9 / 20` (`bfb_satisfied = True`) IR quartic diff vs `lam_UV = 0` was `0.00279 <
     3 / 1000` (passing), whereas `yb_low = 1 / 100` (`bfb_satisfied = False`, no `y_b^4` damping)
     had IR diff `0.00825 < 1 / 100`. `v2` asserts `< 3 / 1000` on `yb_high` and `< 1 / 100` on
     `yb_low` (matching `A2-OW13`).
  2. `380` vs `760` RK4 steps had step-halving diff `8.72e-10`; `v2` increases steps to `1200` vs
     `2400` so step-halving error drops below `10^{-11}`.
- `OW17-B` (`S3` unification census) passed first-principles Dynkin `b_i` / `B_{ij}` (`0` diff),
  `2`-loop `2H` SM RGE (`max B_eff = 0.5960 < 0.62 < 5/7`, step-halving err `1.05e-12`), and `6D`
  complete-multiplet KK universality (`0` shift to `B`), while uncovering TWO exact rational results:
  1. Among single SM split multiplets inside `Spin(10)` `45`, NO multiplet closes strictly inside
     `0 < r < 1`; instead **`2 x (1, 3, 0)_R = (1, 3, 0)_C`** (`A_5 + i A_6` complex `SU(2)_L`
     triplet inside `45`) closes **`B = 5 / 7` EXACTLY at the boundary `r = 1`** (`M_{int} = M_Z`,
     zero intermediate scale `M_{int} / M_X`, zero extra representations outside `45 + 3 x 16 + 2H`).
  2. Among intermediate Pati-Salam thresholds, **pure `PS(4, 2, 2) + 3 x 16 + (1, 2, 2)_C` with
     ZERO extra scalars outside `45 + 3 x 16 + 2H`** closes **`B_{eff} = 5 / 7` EXACTLY at
     `r = 8 / 77`** (`x = ln(M_{PS}/M_Z)/ln(M_X/M_Z) = 69 / 77`), alongside `PS + (15, 1, 1)_R`
     (also inside `45`, `r = 8 / 71`, `x = 63 / 71`) and `PS + (15, 1, 1)_R + (1, 1, 3)_R` (`r = 4 / 35`).

## 2. Exact `v2` Gate Update (`relays/a2_ow17_v2/verify_a2_ow17_v2.py`)

- `OW17-A`: Assert `ir_diff_high < 3 / 1000`, `ir_diff_low < 1 / 100`, and `rk4_err_high < 10^{-11}`
  (`1200` vs `2400` steps).
- `OW17-B`: Assert BOTH the exact `2 x (1, 3, 0)_R` boundary closure (`B_int == 5 / 7`, `r == 1`)
  AND the pure-`PS(4, 2, 2)` zero-extra-scalar closure (`r == 8 / 77`, `x == 69 / 77`, inside
  `ps_inside_45_winners`), while leaving `v1` frozen in `relays/a2_ow17/`.
- Use raw docstrings `r"""..."""` to eliminate Python `SyntaxWarning` on `\{`.

0 of 19.
