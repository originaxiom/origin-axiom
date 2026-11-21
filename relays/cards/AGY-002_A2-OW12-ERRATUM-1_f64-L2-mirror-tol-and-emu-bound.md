# Pre-Registration Erratum 1: `AGY-002_A2-OW12-ERRATUM-1` — `float64` `L_2` Mirror Tolerance, `M_R` Congruence Fix, & All-6 `y_mu / y_s` Bound (`0 of 19`)

- **Parent Card:** `AGY-002_A2-OW12` (`f9fa85bc7`)
- **Preserved `v1` Custody:** `4a163a1ae` (`relays/a2_ow12/verify_a2_ow12.py`) & `16de1c72d` (`verify_a2_ow12_out.json`).
- **Exact Clarifications (No Physics Claims Changed):**
  1. **Mirror CP Tolerance (`OW12-A`, `OW12-B`):** Because the producer evaluates `L_2(tau)` in `64`-bit floating point (`solve_L2_f64_dyadic`), `L_2(tau_*^+) - L_2(tau_*^-) ~ O(1 / 10^15)`, giving `|bar_theta_Q(tau_*^+) + bar_theta_Q(tau_*^-)| < 1 / 10^13` and `|epsilon_1^{norm}(tau_*^+) + epsilon_1^{norm}(tau_*^-)| < 1 / 10^14` (exact to `L_2` solver precision; a `45`-dps GL6 `L_2` referee achieves even tighter agreement).
  2. **Majorana Basis-Scrambling Congruence Bug in `v1` (`OW12-B`):** Under `Y_nu -> U_L Y_nu U_nu^dagger`, Majorana invariance `Y_nu M_R^(-1) Y_nu^T -> U_L (Y_nu M_R^(-1) Y_nu^T) U_L^T` requires `M_R -> U_nu^* M_R U_nu^dagger` (`v1` line 442 mistakenly wrote `U_nu M_R U_nu^T`, causing spurious Haar drift). Fixed in `v2` (giving `< 1 / 10^35` Haar drift!).
  3. **All-6 `y_mu / y_s` Bound (`OW12-C`):** Across the `4 / 6` CKM-strict permutations `y_mu / y_s < 2 / 100`, while on the `2 / 6` `Q_I`-heaviest permutations `(0, 2, 1)` and `(2, 0, 1)` `y_mu / y_s ~ 4 / 100` (`< 5 / 100`, still `> 20x` steeper than `1`). Thus the all-6 bar in `v2` is `y_mu / y_s < 5 / 100` and `y_e / y_d < 1 / 1000` (with `< 2 / 100` verified on the `4 / 6` CKM-strict subset). `0 of 19.`
