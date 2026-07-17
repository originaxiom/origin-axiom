# C3 — BANKED (CORRECTED): THE SIGN TABLE — SCALARS, SPLITS, AND TWO PARTIAL LAWS
# (cc2 + subagent, 2026-07-17; prereg f32fbfff)
# CORRECTION NOTE (MB13, owned): the first version of this file was banked by
# the main seat from a MID-RUN log and contained errors (it read all rows as
# scalars); the agent's gated final data supersedes it. This is the corrected
# bank. Lesson: never bank from a log the run hasn't finished writing.

THE STRUCTURE (20 realized centrals, k = 2..12 both stages; A3/F2 gates
reproduced exactly):
- 9 rows are EXACT BLOCK SCALARS (+-1); 11 rows are exactly-certified +-1
  INVOLUTIONS THAT SPLIT THE BLOCK (n+/n- eigenspaces; e.g. E6 k=5: 18/16,
  k=7: 49/56, k=8: 78/92; SU3 k=12: 26/16). A3's loop-1 "block-wide scalar"
  was correct for the deep-3 pair but does NOT generalize.
- RECONCILIATION with the F2 kill theorem: KILLED centrals => +1 scalar
  (identity) exactly; SURVIVING centrals => either -1 scalar or a SPLIT — and
  the split dims (n+, n-) are the LOCAL-CONSTITUENT PARITY DATA the
  PSL-factoring theorem's priced step asked for, now measured at 11 rungs.
THE TWO PARTIAL LAWS (fit only on the 9 scalar rows — fitting splits is
meaningless): (1) p != 3 scalars: stage-flip x (p|3) — the EISENSTEIN
character — fits 4/4 applicable; (2) the best overall near-miss:
scalar = (-1)^(a-1) fits 8/9, missing exactly SU(3) k=6 — the known E/A-type
deep-3 divergence. The (i)-family (c mod 24) is ANALYTICALLY impossible
(SU3 k=3 realizes both signs at identical c).
FRONTIER FEED: the split-dimension table (n+, n-) per rung = the constituent
decomposition data — one cell away from the full local-constituent theorem
(match n+/n- against SL(2,q) irrep dimension combinatorics).
Artifacts: c3_signtable.py, c3_table.json, c3_run.log. Repo untouched.
