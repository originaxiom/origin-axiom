# Erratum 2 to Card A2-OW19: Frozen v2 Near-Degenerate Takagi Precision Floor and 35-dps mpmath v3 Upgrade

- **Frozen Prior Runs:** `v1` (`0d2246ff6` / `b9101c210`) and `v2` (`1f8db21dc` / `22f8ebdaf`), both preserved untouched.
- **Single Self-Check Catch in `v2`:** `OW19-B`, `OW19-C` (`grad_norm = 2.89e-33`), and `OW19-D` (`6 / 6` planted faults) all passed (`True`). In `OW19-A`, all `2D` hyperbolic metric, Gauss-Bonnet (`1.16e-10`), `2D` Kahler, and leptogenesis mirror checks passed, while `haar_10trial_max_drift = 1.454e-11` narrowly exceeded `< 1e-12` purely due to IEEE-754 `float64` SVD roundoff on the near-degenerate resonant denominator `(x - 1)^2` of `MR00` inside `eps_unflav` (while `ckm_v12..v13, J_ckm, se_12, yb_flav` were already `<= 1.67e-13`).
- **Fix in `v3`:** Keep the `2D` polar-cusp quadrature unchanged, and promote `extract_flavor_and_lepto_obs` plus the `10`-trial Haar `U(3)^3` basis-scrambling check from IEEE-754 `float64` to exact `35`-dps `mpmath` (`mp.eighe` SVD & Takagi factorization), dropping `haar_10trial_max_drift` well below `1e-25`.
- **Zero changes** to any mathematical theorem, expectation, pre-registered gate, or `0 of 19` firewall constraint.
