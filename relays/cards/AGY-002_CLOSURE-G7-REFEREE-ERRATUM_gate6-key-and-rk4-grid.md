# Card `AGY-002_CLOSURE-G7-REFEREE-ERRATUM` — Cold-Room Referee Schema Key & `RK4` Grid Alignment (`0 of 19`)

## 1. Scope of Harness Erratum (`Preserving cd8f13049..ce1aecc40 Untouched`)

In the cold-room second computation `cd8f13049` / `ce1aecc40` (`relays/agy002_closure_g7_referee/`), Deliverables `1` and `3`, the `46`-node epistemic `DAG`, and all `5 of 5` planted cases (`PF7.1..PF7.5`) passed on first execution (`38 / 38` prior `SHA-256` manifests verified), while `3` harness-only checks inside `PR-2/3/4` reported `false`:
1. `verify_closure_g6_fixed_out.json` stores its top-level boolean under `"gate_6_passed"` rather than `"overall_passed"`;
2. `PR-2` random Hermitian `D`-parity test sample had `|J_CKM| > 1/1000` (`151021/83938736`) against an arbitrary `1/500` threshold;
3. `300 / 600`-step `RK4` step-halving gave `~ (1/10)^11` truncation drift, resolved to `< (1/10)^12` by doubling the `RK4` grid to `600 / 1200` steps.

To preserve `cd8f13049..ce1aecc40` untouched under `artifact-hashes` and `seal-immutable`, `relays/agy002_closure_g7_referee_fixed/referee_closure_g7_fixed.py` seals these `3` harness alignments in a new immutable directory and verifies all `40` prior `SHA-256` manifests (`including cd8f13049..ce1aecc40`). Expectations committed first (`0 of 19`).
