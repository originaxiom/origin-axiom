# B1719 — W122 ON MAIN (P-269): THE SM SEAT'S CLOSED UNIVERSES REPRODUCED, AND THE WEEKS MANIFOLD IDENTIFIED BY ISOMETRY AS THE LEAST FILLING OF −LR ONLY, THE MEYERHOFF MANIFOLD AS THE NEXT, FROM BOTH ±LR

**Verdict: PROVED** (a verification arc). cc (main), 2026-10-22. No physical quantity. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /closed universe|Weeks|Meyerhoff|Dehn fill|least volume|filling/`. The record's fillings are:
- m004(0, 1), Sol (sm:B1380 S7);
- B1483 (m004's spin-structure end curves);
- the SM seat's W120 and W122, the gravity line.

No main arc computes the least closed filling of the threads. **Literature:** Gabai, Meyerhoff and Milley (2009), the
Weeks manifold as the least-volume closed orientable hyperbolic 3-manifold. W122 cites it, and main does not re-derive
it.

## 1. What was checked

**(a) The seat's own script, re-run on main.**
- `verification/reproduce/the_closed_universes.py` is the seat's file at bcc3686a3, byte-identical (sha256 58be11a6…).
  It was re-run under main's SnapPy 3.3.2; the log is in `reproduce/the_closed_universes_run.txt`.
- Against the seat's committed output:
  - all 3 024 fillings agree in their certification and solution type;
  - the volumes agree to 9.8 × 10⁻¹⁵;
  - R1, R2 and R3 hold as the seat's do;
  - the five least volumes and their identifications are the same.
- The one difference is the order of tied entries in a listing: R4's eleventh entry, b+-LLRR and b++LRR, both
  1.831931.

**(b) Main's own check** (`verification/main_check.py`, independent of the seat's code).
- **The method.** The least certified fillings of b+-LR (m003) and b++LR (m004) over primitive slopes ∣p∣, q ≤ 7 were
  computed, and each identified by isometry, not by volume.
- **b+-LR:** the Weeks manifold at slopes (2, 5) and (3, 5), volume 0.9427073628; next the Meyerhoff manifold at (−1, 1)
  and (2, 1), 0.9813688289.
- **b++LR:** the Meyerhoff manifold at (±1, 5); next 1.2844853005 (m004(6, 1), as in the seat's identification list).
- So among the tick's class ±LR, the Weeks manifold comes from −LR only and the Meyerhoff manifold from both. These are
  W122's R1 and R2.

## 2. What it means

- **W122's computation is verified on main.** The least closed universe filled from the record's threads (words of
  length 2–6, slopes in the seat's box) is the Weeks manifold, from the tick's sister −LR.
- **The ground-state reading stays a READING.** The volume is the energy at the 4d flow's attractor (Fischer–Moncrief,
  Andersson–Moncrief, cited by the seat). The filling slope is a choice, and nothing selects it.
- W123 and W124 (the Higgs route to the cusp's unit; the graviton spectrum on Weeks) are rules only. Main reads them when
  their runs land (P-269).

## Files

- `verification/reproduce/` holds the seat's script and main's re-run log. The 0.5 MB output is regenerable and not
  stored.
- `verification/main_check.py` → `main_check.json`.
- The lock: `tests/test_b1719_w122_on_main.py`.
