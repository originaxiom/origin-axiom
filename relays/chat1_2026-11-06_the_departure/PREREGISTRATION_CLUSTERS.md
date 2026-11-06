# THE LEADING RUNG-INVISIBLE SADDLE UNDER THE PRINCIPLE'S ACTION — pre-registration (the web seat, 2026-11-06)

**For:** the owner's "lets solve it", and main's P-724 Q1: "the departures' action-weighted sum and whether its
leading term dominates, data-free".

The clock note's second referee found that at P-441's golden end, at a fixed number of moves, clusters that keep the
history golden mod 5 lose less length than the single run of 6. This check commits that finding.

**Kind:** data-free; lengths of closed threads only. It reuses `least_action_check.py`'s `space()`, `excess()` and the
post hoc's rung class (E ≡ ±I mod 5). No coupling, scale ratio or held-out quantity is computed, and nothing is
compared with data. **Written before** `cluster_check.py` is run. The smoke copy uses m ≤ 3 only, and its values are
not read.

## The two actions

- **(A) Excess length at a fixed number of runs:** excess(S) (0772952e3). Under it the run of 6 is the unique cheapest
  rung-invisible defect in the range (0772952e3's post hoc; S305v).
- **(B) Length lost at a fixed number of moves, the principle's measure at the golden end:**
  D(S) = (Σ s_i − m)·2 log φ − excess(S), for a defect S = (s₁, …, s_m). For a single run this is the leading-excitation
  check's D_n.

## Predictions

These are informed by the referee's unregistered computation, and disclosed as such.

- **P1.** Among the range's rung-invisible defects (643), under (B):
  - the run of 6 is not the cheapest;
  - the cheapest is (2, 1, 1, 3, 3, 1, 1, 2), with D ≈ 1.548;
  - the run of 6 ranks 46th;
  - (3, 1, 2, 2, 1, 3) at about 1.739, (3, 1, 1, 1, 1, 4) at about 1.828 and (2, 1, 1, 1, 1, 5) at about 2.018 are
    also lighter.
- **P2.** Under (A), the run of 6 is the cheapest, as in 0772952e3.
- **P3, per-run conservation.** Every run is invisible on its own, so runs lie in {1, 6} in this range. Then the
  cheapest defect under both (A) and (B) is the run of 6.

**What would refute:** the run of 6 cheapest under (B) without per-run conservation, or not cheapest under P3.

0 of 19.
