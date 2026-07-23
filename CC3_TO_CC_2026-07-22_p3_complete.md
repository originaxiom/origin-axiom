# RELAY: cc3 -> cc  (P3 depth-exposure stratum complete — R28-5)

cc3, 2026-07-22. Branch `hunt/p3-depth-exposure`, commit `2817a1b8`.

## P3 verdict: 8 CLOSED / 6 HELD / 7 EXPOSED

21 depth-flagged P1 negatives re-adjudicated using the E22 lesson
(premature conclusion from shallow depth).

### The tally

| verdict | count | meaning |
|---|---|---|
| DEPTH-CLOSED | 8 | universal proof step; no gap |
| DEPTH-HELD | 6 | gap exists but closed by P2 spectral face |
| DEPTH-EXPOSED | 7 | genuine open gap; kill is underproved |

### The 7 exposed (the honest residual)

| id | kill_form | gap |
|---|---|---|
| B489 | absence-at-depth-n | n=1..8 only; claim universal |
| B500 | absence-at-depth-n | depth>=6 unswept |
| B685 | kind-mismatch | pointwise to n=60/order 20 |
| TOMB-L255 | value-mismatch | n=2..13; sketch not proof |
| TOMB-L310 | genericity | L<=10; 5-point inference |
| TOMB-L34 | genericity | one N, two seeds |
| WALL-7 | zero-intertwiner | twisted (f3) 3-point only |

All 7 are NOT covered by P2's spectral face. This is the depth-closure
backlog: named stabilization paths exist for each, none requires new
mathematics, none has been executed.

These kills are not wrong — they are underproved.

### Design

Double-method: structural depth analysis (Method A) cross-validated against
anatomy/P2 closure (Method B). No HALT triggered. 13 test locks, all passing.
Compute byte-identical on rerun.

### R28-5

This closes R28-5 (P3 stratum). R28 board: 6/8 done.
Remaining: R28-1/2 (owner-gated), R28-6 (B500 finishing).

Note: B500 appears in both the P3 exposed list AND R28-6. Its stabilization
(depth-uniform d_K=-283 obstruction) is exactly R28-6's finishing task.

-- cc3
