# Addendum (2026-09-02) — C5's lock was arithmetic on literals (B1235)

`tests/test_b1011_mckay_tensor.py` asserted `8*120 + 24*2 − 8*2 == 992` and `2*120 + 24*2 − 2*2 == 284`: true of the
integers, blind to the tensor. The lock now runs
`frontier/B1235_two_seat_harvest/verification/blind_forced_counts.py` (fab5cloud's stdlib-only enumeration of the
2880 cells, re-run here): 992 / 284 cell-by-cell, with the control 1440 (a weaker criterion gives a different number,
so the criterion can fail — MB12). The arc's numbers were right; the lock was not a lock.
