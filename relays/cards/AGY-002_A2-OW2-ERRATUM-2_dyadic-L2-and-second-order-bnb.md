# Erratum 2 to Card `A2-OW2` — Dyadic `pts_in` Near Puncture and 2nd-Order Gradient-Monotonicity Branch-and-Bound (`0 of 19`)

## Disclosed Numerical Issues in Sealed `v2` (`377b6b59d`)

1. In `solve_L2_f64_dyadic`, the fixed `4`-segment inward path `[z0, z0/2, z0/4, z0/8, zs]` made a `6x` jump from `z0/8` to `zs` at `m = 24` (`Im(w) = 24/5`), causing `L_2` mirror discretization error above `(1/10)^10` and triggering the script's own mirror assertion before writing output.
2. In `certify_global_min_X0N`, 1st-order value-only Lipschitz pruning required quadratic box refinement near minima (long runtime).

## Exact Fixes for Authoritative `v3` (`relays/a2_ow2_v3/verify_a2_ow2_v3.py`)

- Leave `relays/a2_ow2/` and `relays/a2_ow2_v2/` completely untouched.
- Replace the fixed `4`-segment inward path in `solve_L2_f64_dyadic` with a full dyadic halving sequence down to `|cur| <= 2/25` before `zs` (restoring `L_2` mirror agreement to `< (1/10)^14`).
- Upgrade `certify_global_min_X0N` to exact 2nd-order Taylor-Hessian value pruning plus exact gradient-monotonicity pruning (`|grad g_k(z_c)| - L_2(B) * rad > 0`, using the exact `SL(2, Z)`-invariant analytic Hessian upper bound `L_2(B)`).
- All mathematical definitions, tasks (`OW2-A` through `OW2-E`), and pass bars of Card `A2-OW2` (`d19ced577`) remain completely unchanged. `0 of 19.`
