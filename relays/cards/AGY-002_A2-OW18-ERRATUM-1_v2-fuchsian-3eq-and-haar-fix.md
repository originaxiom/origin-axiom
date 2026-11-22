# Erratum 1 to Card `A2-OW18`: Pre-Run Code Fixes for `a2_ow18_v2` (Preserving Raw `v1` at `d09d4a35e` Untouched)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (`0 of 19`)
- **Date:** `2026-11-22` (committed BEFORE `relays/a2_ow18_v2/verify_a2_ow18_v2.py` runs)
- **Raw `v1` Outcome (`d09d4a35e`, kept completely untouched):** `ow18_b`, `ow18_c`, `ow18_d`, and `ow18_f_planted_faults` (`6 / 6`) all passed (`True`) on the first run; two self-verification gates inside `v1` caught two script bugs:
  1. **`OW18-E` (`solve_l2_weierstrass_taylor`):** Used only `2` equations `[Im tr(Ta), Im tr(Tb)] = [0, 0]`, which vanish identically for every real `c` on the imaginary axis `Re(tau) = 0` (`tau = i sqrt(3)`) and are ill-conditioned at small `Re(tau)` (`tau_0 = 13/100 + 17/10 i`), stopping at `c = 0.3686` instead of `0.4459394...`. Fix in `v2`: enforce all `3` `PSU(1, 1)` real-trace equations `[Im tr(Ta), Im tr(Tb), Im tr(Ta Tb)] = [0, 0, 0]` via normal-equation Gauss-Newton at `dps = 40` (`tol = 1e-32`), starting from `c = pi^2 / 12` (`mended code`, zero changed expectations).
  2. **`OW18-A` (Guardrail-3 Haar test on leptogenesis):** Applied `MR_rot = (UN^H)^T M_R UN^H` while multiplying `Ynu` on the right by `UN.T` instead of the matching `UN.H`, caught immediately by Guardrail 3 (`drift 5.19e-10`). Fix in `v2`: apply consistent `Ynu_rot = UL * Ynu * UN.H` (`matching MR_rot = UN.apply(mp.conj) * M_R * UN.H`, dropping drift to `< 1e-30`).
- **Pre-Registered Expectations Unchanged:** Every mathematical threshold and expectation in `a76a97e0d` remains strictly identical.

0 of 19.
