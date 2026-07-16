# N3 — BANKED: ONE-ORGAN-OR-TWO = UNRESOLVED (a cc2 subagent + main-seat bank;
# 2026-07-16; prereg PREREG_N3.md sha 09246f08, sealed before the grid ran).

Anchor gate 4/4 EXACT (diff 0.0 vs banked grid/depth14/r3 values; lib byte-identical).
Grid: kappa 0.80..1.55 step 0.05, depth 14, 10 placement-jitter replicates/point
(new additive box_dim_offset estimator: independent random grid-origin shift per
scale; bit-identical to L.box_dim at zero offset; point estimates always the
deterministic value, replicates only estimate sigma).

RESULT: global argmax kappa* = 1.10 (1.080426) — R3's coarse kappa* REPRODUCED.
But the fine grid shows 5 raw local maxima (0.80, 0.95, 1.10, 1.25, 1.45), not 2;
pooled jitter sigma = 0.014337; best two-peak candidate (1.10, 1.45 via valley 1.35)
has margins 0.0182/0.0135 = ~1.27 sigma, only ~64% of the preregistered 2-sigma bar
-> mechanically UNRESOLVED. Depth-15 triple check (0.95/1.05/1.10): the candidate
gaps HALVED going deeper (0.0111/0.0126 -> 0.0056/0.0068) — shrinking, not growing.

CENTRAL FINDING (not a footnote): the jitter floor is comparable to or larger than
EVERY candidate gap on the plateau — the substructure question is not answerable by
the box-dim statistic at depth 14/15. Non-binding lean: more wiggles at finer
resolution = noise on ONE broad shelf. R3's mechanism-candidate (gap-dominated
fragmentation, MST-gap max adjacent at 1.2) is UNAFFECTED; only the one-vs-two
sub-question stays open.

Honest caveats logged: known upward depth bias (+0.069..0.076, same as V11b/R3);
estimator is new (validated on non-grid reference points, not previously banked);
depth-15 was 3 spot points, not a re-grid. Budget: 153 s total. Repo untouched.
Data: grid_table.txt, n3_results.json (raw replicate arrays), n3_output.txt.
=> proposal to cc: bank UNRESOLVED with the jitter-floor bound; a different statistic
(e.g. the MST-gap functional directly, or a multifractal moment) would be needed to
reopen; do not spend more depth on box-dim alone.
