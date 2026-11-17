# Card `AGY-002_CLOSURE-G7B-REFEREE-ERRATUM` — Unsquared `SVD` Projector Extraction and Native `JSON` Boolean Serialization (`0 of 19`)

## 1. Trigger Under `artifact-hashes` Immutability

During first cold-room execution of `relays/agy002_closure_g7b_referee/referee_closure_g7b.py` (sealed pre-execution in commit `997f7482e`), `json.dumps` raised `TypeError: Object of type bool is not JSON serializable` on a `numpy` boolean scalar returned by short-circuit evaluation in Deliverable `3` when squaring `H_e = Y_e Y_e^dagger` at `y_e / y_tau = 1/2000` amplified `float64` eigenvector roundoff by `(20)^2 = 400` near the `(1/10)^13` `Haar` threshold.

Per `artifact-hashes` immutability (`*SHA256.txt` files may only be added `A`, never modified `M`), `relays/agy002_closure_g7b_referee/` is preserved untouched and the corrected cold-room referee is placed in `relays/agy002_closure_g7b_referee_fixed/` prior to reading any producer script or output.

## 2. Two Technical Fixes (`0 of 19`, Zero `float`/`complex` AST Literals)

1. **Unsquared `SVD` Left-Singular Projector Extraction (`Guardrail 3`):** Extract `P_e` and `P_{nu_1}` directly from left singular vectors of `Y_e` (`hierarchical rational ratios 1/100 : 1/10 : 1`) and `kappa` via `np.linalg.svd`, avoiding condition-number squaring in `Y_e Y_e^dagger` and keeping `10`-trial `U(3)_L x U(3)_{eR}` `Haar` basis-scrambling invariance well below `(1/10)^13`.
2. **Native `JSON` Scalar Sanitization & Custody Accounting:** Convert all `numpy` scalar returns to native `Python` `bool`/`int` before `json.dumps`, and verify byte-for-byte `SHA-256` custody across all `44` campaign manifests (`Gates 0-7B` producer) plus `relays/agy002_closure_g7b_referee/SCRIPT_SHA256.txt` (`45` prior manifests total) and runtime self-verification of `relays/agy002_closure_g7b_referee_fixed/SCRIPT_SHA256.txt`.
