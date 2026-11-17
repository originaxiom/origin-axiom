# Card `AGY-002_CLOSURE-G7B-REFEREE-ERRATUM-2` — `Kahan`-Compensated `RK4` Step Accumulation (`0 of 19`)

## 1. Trigger Under `artifact-hashes` Immutability

In `relays/agy002_closure_g7b_referee_fixed/referee_closure_g7b.py` (sealed in commit `18049e565`), Deliverables `1`, `2`, `4`, and all `5` planted faults passed, while in Deliverable `3` uncompensated `600`-step `float64` addition on the `m_3 = 9` Weinberg matrix accumulated Frobenius roundoff `106 / 10^15` (`slightly above (1/10)^13 = 100 / 10^15`) between `RK4` and `expm`.

Preserving `relays/agy002_closure_g7b_referee_fixed/SCRIPT_SHA256.txt` untouched under `artifact-hashes`, `relays/agy002_closure_g7b_referee_v2/referee_closure_g7b.py` applies `Kahan` compensated summation with `n_steps = 80` in `_integrate_weinberg_rk4`, suppressing step-accumulation roundoff by over an order of magnitude below `(1/10)^13` while keeping `O(h^4)` truncation below `(1/10)^17`.
