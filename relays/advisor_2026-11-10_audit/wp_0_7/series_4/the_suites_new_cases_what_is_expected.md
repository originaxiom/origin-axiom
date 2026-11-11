# The suite's eight new cases: what is expected, written before any run

*cld-advisor, 2026-11-11. Card C2. Committed with the plants, before the suite is run with them on any commit.*

The suite listed six cases as manual. It now plants them itself, and two more: the case of M5 (PV31), and a further
form of PV25 that a measurement on main's `323f92327` pointed at (PV32). Each of the eight has a twin: the same plant
with the violation taken out, on which the same gates must pass.

| case | the plant | on main's `323f92327` | on the end of series 4 |
|---|---|---|---|
| PV5 | a sealed file is edited, and both of the ledger's rows are made to agree | caught: main mended it, the seal gate reads history | caught |
| PV7 | the ledger's generated rows are removed and rebuilt twice | caught: the two runs agree, and with the old fault planted again they differ | caught |
| PV23 | a new NEGATIVE worded about the object, and an old one reworded so the count stays | **not caught** | caught |
| PV25 | an arc's own lock reads a file git ignores, written `HERE / "run.log"` | caught: main mended it in this form | caught |
| PV32 | a lock in `tests/` reads an ignored file through a second name (`V = A / "verification"`, then `V / "run.log"`) | **not caught**: the gate reads 2,118 of the 5,554 paths the locks name beside themselves | caught |
| PV26 | a lock runs a script and pins a float it prints, as text | **not caught** | caught |
| PV27 | a test run rewrites a tracked file | **not caught**: the run ends with status 0 | caught |
| PV31 | a test of a lock that no hash list names is made to skip | **not caught** | caught |

Also expected:

- every twin passes, on both commits;
- the gates the cases name all pass on the clean clone, on both commits;
- the 24 older cases read on `323f92327` as they read on `f9e70c167`: 11 caught, and the three of series 4's first
  patches not caught. So on main's head 14 of 32 are expected caught, and 5 of 5 controls.

How it could come out wrong: PV5 or PV25 may pass as the suite plants them, on the real pages, though main's own tests
of them pass. A twin may fail, which would mean a gate fires on the shape of a plant and not on its violation. And
the measurement behind PV32 was made by a script that reads the locks by their syntax tree; if it reads a form
wrongly, PV32 may be caught.
