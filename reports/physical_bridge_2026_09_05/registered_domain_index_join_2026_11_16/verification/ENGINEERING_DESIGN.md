# Runner rejection fixtures

2026-11-16. Expectations before fixture implementation or execution.

The runner reuses the repository prospective strict gate and the frozen
P210-era custody helpers. It requires CPython 3.12.1 in isolated mode with
bytecode disabled. Its exact admitted command includes both flags.

Three infrastructure fixtures will invoke the real runner in a temporary
Git checkout containing the sealed source closure. They must stop before
scientific import when a source pin is changed, an untracked file is added,
or an ignored file is added. The two dirty-checkout cases must also be
rejected by the exact full-inventory condition used in the runner.

Each fixture copies the package and its source closure from the reviewed
checkout. A top-level sentinel replaces checks.py in the temporary copy.
For dirty-checkout fixtures its replacement hash is updated in that copy's
specification, so a source-pin mismatch cannot explain the rejection.
The sentinel would create a marker and raise if imported. The marker must
remain absent. Missing scientific admission is expected as well, but the
fixtures must identify their specific earlier rejection.

Fixtures grant no scientific admission and cannot supply a positive main
acceptance. They are source-review material until separately permitted.
Their outputs will preserve the first failure with exclusive file creation.
No fixture changes the worktree holding inherited staged material.
