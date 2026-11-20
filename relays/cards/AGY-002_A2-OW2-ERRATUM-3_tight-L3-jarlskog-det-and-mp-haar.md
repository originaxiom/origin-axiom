# Erratum 3 to Card `A2-OW2` — Tight Analytic `L_3` Convexity Ball, Degenerate-Subspace Jarlskog `det[H_u, H_d]`, `m = 25` Control, and High-Precision Haar Check (`0 of 19`)

## Disclosed Technical Issues in Sealed `v3` (`84cc0d47f` / `415ec03fb`)

Sealed `v3` (`415ec03fb`, preserved untouched) passed `OW2-A`, `OW2-C`, and `OW2-E` and produced the full scientific findings (`N = 1, 2, 3` CP-conserving; `N = 4` irrational CP-breaking; `N = 5` exact CM/orbifold CP-breaking at `tau_*^{+-} = (+-2 + i)/5`; `N = 8` CP-conserving; `N = 6, 7, 9, 10, 11, 13` CP-breaking), while flagging two purely technical implementation defects:

1. **`OW2-B` coarse `L_3` ball radius (`uncert > 0`, `N = 4` `balls = False`):** Estimating the Cauchy 3rd-derivative bound `L_3` via the coarse global `lipschitz_f_bound` on `R = 1/25` overestimated `L_3` by roughly two orders of magnitude, shrinking `r_use` below the `depth = 16` box radius (and below the floor on `N = 4`'s flatter minimum) and leaving uncertified micro-boxes around the already-located minima.
2. **`OW2-D` degenerate-SVD gauge artifact (`m = 1, 5`), `Re mod 5` periodicity (`m = 15` vs `m = 25`), and `float64` conditioning at `m = 24`:**
   - At `m = 1` and `m = 5`, `Y_d` has an exact degenerate top pair (`s_1 == s_2`) and zero mode (`s_3 == 0`), where raw `Im(V_00 V_11 conj(V_01) conj(V_10))` depends on arbitrary `U(2)` SVD basis choice inside the degenerate plane whereas the physical basis-invariant Jarlskog commutator determinant `J_det = Im(det([H_u, H_d])) / (-2 i)` vanishes identically (`0` physical CP violation).
   - Because the `24`-point `E[5]` Weyl phase `zeta_5^{-a b}` is periodic modulo `5` (not `1`) under `tau -> tau + 1`, `m = 15` (`Re = 6 = 1 mod 5`) is genuinely CP-violating (`J(-conj) == -J` to `< (1/10)^65`), whereas `m = 25` (`Re = 10 = 0 mod 5`) is the true CP-conserving multiple where `J_det == 0`.
   - At `m = 24`, `s_3(Y_d) / s_1(Y_d)` is smaller than `(1/10)^11`, causing `float64` `np.linalg.svd` rounding drift near `(2/10)^11` on `|V_ij|` during the `10`-trial Haar check; executing the `10`-trial Haar check in `40`-digit `mpmath` eliminates `float64` rounding without relaxing the `< (1/10)^12` gate.

## Exact Fixes for Authoritative `v4` (`relays/a2_ow2_v4/verify_a2_ow2_v4.py`)

- Leave `relays/a2_ow2/`, `relays/a2_ow2_v2/`, and `relays/a2_ow2_v3/` completely untouched.
- In `OW2-B`, compute the analytic Cauchy `L_3` bound directly from exact `|E_2(w)|` on the `64`-point circle of radius `R_cauchy = 1/12` (bounded analytically with exact tail margin) and collect all boundary coset representatives of each global minimum so `total_uncertified_boxes == 0` and `all_convex_balls_certified == True` across all five rungs `N = 1..5`.
- In `OW2-D`, compute the exact basis-invariant Jarlskog determinant `J_raw = Im(det([H_u, H_d]))` alongside normalized `J_CP` (setting normalized `J_CP = 0` when degenerate `|s_1 - s_2| / s_1 < (1/10)^25`), test `m in {1, 5, 8, 15, 24, 25}` (verifying `J_raw == 0` at degenerate `m = 1, 5` and CP-conserving `m = 25`, and `J_raw != 0` with exact mirror antisymmetry `< (1/10)^50` at `m = 8, 15, 24`), and execute the `10`-trial Haar invariance gate in `40`-digit `mpmath` at `m = 8` and `m = 24` (`< (1/10)^12`). `0 of 19.`
