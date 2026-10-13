# Run 13: Same-model coupled quadratic modes

Read `TECHNICAL_REPORT.md` for the assumptions, derivation, scope and source history.
No new silver spectrum, numerical particle mass, anomaly cancellation or TOE is
claimed. The result is a conditional quadratic spectral organization of one
supplied compact parent and boundary, with same-author exact controls.

## Run

Requires Python 3 and SymPy. No network access or repository clone is needed.

```sh
python verify_coupled.py
python verify_slab_reference.py
python verify_constraints.py
```

Expected final results: 59/59, 34/34 and 15/15 checks respectively. The finite
complex's control masses are arbitrary test data, not physical predictions.
The slab reference is a local/nonzero-frequency boundary control, not the silver
core's topology. Finite controls do not certify the inherited/global analytic
hypotheses. A number of tests is not a confidence percentage.

`record_replay.py` re-runs all three final scripts and records literal logs,
exit codes, durations and hashes. A final unchanged replay exited 0 for all three.

## Retained execution history

The first main run timed out before output was flushed. Exact expansion of
intermediate rational-complex matrices made it fast; a second run reached a
Python-bool/SymPy type error in a standard rest-frame control. Casting that
Kronecker delta to an integer fixed the type without changing the test.
Both old scripts and logs are retained. They are historical files, not the
recommended entry points. The reference and constraint checks passed first run.
Pre-run hashes and the later manifest are local records, not external timestamps.

## Files

- `COUPLED_RESULTS.json`, `SLAB_RESULTS.json`, `CONSTRAINT_RESULTS.json`: exact results.
- `SOURCES.json`: pinned source paths, actual read scope, inherited assumptions.
- `PLAN.md`: post-exploration, pre-formal-run scope and criteria.
- `PRE_*`, `CONSTRAINT_PRE_RUN_HASH.json`, `SEAL_CHECKS.json`: source hashes.
- `*_FIRST.log`, `*_SECOND.log`, `*_THIRD.log`, `*_REPLAY.log`: literal history.
- `FINAL_REPLAY_RECEIPT.json`: successful final replay metadata.
- `ENVIRONMENT.json`: Python and SymPy versions.

Only the local Run 13 directory is new. No original manuscript, previous report,
repository file, branch, or remote record was changed.
