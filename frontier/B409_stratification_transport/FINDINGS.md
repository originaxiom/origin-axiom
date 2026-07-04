# B409 (Phase 2c) — BANKED: the transport "theorem" is KILLED — B407 folds into P67/M1

**Status: complete, the registered KILL branch. Prereg committed first. Firewalled.**

The count-conservation candidate holds on only 4 of 6 pairs (transport.json):
- MATCH: (1,3), (1,4), (2,3), (3,4) — the dark pairs and the low-multiplicity bright ones.
- DIFFER: (1,2) (table s=44 vs product s=60), (2,4) (z: 8 vs 24) — the HIGH-multiplicity
  bright pairs, where the DFT+Π_H maps products to cells NON-INJECTIVELY (merging/
  cancellation), so stratum counts are not conserved.

**Verdict (Phase-2c decision): B407 states nothing beyond P66/P67/M1 as a universal law —
it is a same-object restatement that happens to hold where multiplicity is ≤ 1.** It FOLDS
into the P67/M1 write-up; it is NOT a separate Paper-1 theorem. (This is the useful
outcome: it prevents an overclaim — the "table anatomy = product stratification" line is
scoped to low-multiplicity pairs, not asserted universally.)

**Provenance.** transport.py → transport.json; locks tests/test_b409_transport.py.
