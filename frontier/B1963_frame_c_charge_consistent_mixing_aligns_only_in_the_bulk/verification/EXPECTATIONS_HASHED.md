# B1963 — each script's SHA-256, recorded before its run

Each script states its expectations at its top. Its hash was taken before it ran, with the UTC time. The lock
(`test_b1963_window.py`) checks that each script now has the last hash recorded for it.

| script | SHA-256 before the run | UTC | note |
|---|---|---|---|
| `conjugation_cycle.py` | `d35aac73da361b3202dbfdcef9a10457cff7624291b5a4474755fe04f76b78d4` | 2026-11-19T08:29:09Z | the first run; void (its degeneracy screen, 1e-30, set every point aside); kept as conjugation_cycle_run_VOID_threshold_bug.txt |
| `conjugation_cycle.py` | `433d2b88c117e07c5272b10c41eaa20e3b6348d07bec8977852d01b145ae61d3` | 2026-11-19T08:31:04Z | the second run, after the screen was amended to the working precision; expectations unchanged; this is the file as it stands |
| `height_window.py` | `a9240978cc422ee987faef00e4cb3b19f378833a29b09484d30ce06f1ced9d17` | 2026-11-19T08:35:45Z | the height window, written after part 1's result |
| `columns.py` | `abec0672585b43355b7cf31d8b26d1524c374e8b9beaf0c46c14f71c62fb87a8` | 2026-11-19T08:38:17Z | the columns, written after part 2's result |
