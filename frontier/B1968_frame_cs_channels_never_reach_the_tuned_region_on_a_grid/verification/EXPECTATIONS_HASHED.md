# B1968 — each script's SHA-256, recorded before its run

`reach.py` states its expectations Q1 to Q3 at its top. `reach_column.py` runs reach.py's own loop for one column, with
reach.py imported unchanged.

| script | SHA-256 before the run | UTC | note |
|---|---|---|---|
| `reach.py` | `37d5dfdc418347b0f5dd6ab017c761de26024f0e399f3d16e40e9b9d28daf758` | 2026-11-19T12:07:45Z | written before its run |
| `reach_column.py` | `6a20d40fa7d50302a5f219ec6ca6022962f286574f9bfa9567c3111b60a3faeb` | 2026-11-19T12:38:41Z | the column runner, written before its runs (reach.py unchanged) |
