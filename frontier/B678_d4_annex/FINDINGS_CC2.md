# D4 — BANKED: THE FULL 8x12 LADDER TABLE + THE CEILING MAP (cc2 seat + subagent + main-seat surgery, 2026-07-18; prereg addendum 56e5a59c; ALL 12
# levels, ALL gates pass, tr_odd convention audited against the banked
# d4_su3 construction verbatim)

## VERDICT 1 — THE TRACK-H CONTROL (empirical, closing B669's loop):
NO GROWTH ANYWHERE: all 8 metallic words R^(n-2)L (n = 3..10), all 12
levels (kappa = 4..15), |tr_odd| bounded — growth flags False in every
cell. Chat-1's amphichiral-suppression mechanism is REFUTED empirically,
exactly as the melody/jump theorems predicted. Boundedness is universal.

## VERDICT 2 — THE CEILING MAP (the surviving Track-H content, as data):
n:      3     4     5     6     7     8      9     10
disc:   5    12    21    32    45    60     77    96
ceil: 1.0   1.0   2.0   1.0   2.0   1.732  2.0   1.785
at k:  4,8,12 (many) 12    (many) 15    9      10    8
- THE GOLDEN'S CEILING = 1 IS THE MINIMUM (tied with n = 4, 6): the
  monotone-in-conductor hypothesis is REFINED, not confirmed — the
  ceiling is resonance-structured, not disc-monotone.
- THE OWN-CHANNEL SIGNATURE: at 5-resonances the GOLDEN is QUIET
  (|Z| = 1/phi = 0.618 at kappa = 5, 10, 15) while the OTHER
  5-carrying word (n = 7, disc 45) is LOUD there (ceiling 2.0 AT
  kappa = 15). The landscape's "golden minimum at its own conductor"
  reappears at ladder level.
- CROSS-CHECK with the banked B4 landscape: the (n = 4, kappa = 12)
  cell = 0.7321 = sqrt(3) - 1 EXACTLY reproduces the banked
  trace-4-at-its-own-conductor value. Two campaigns, one number.
- The value menu is small and algebraic: {0, 1/phi, sqrt3 - 1, 1,
  sqrt2, sqrt3, 1.785..., 2} — feeds the frontier's value-catalogue
  item (1.785 at (10, kappa=8) not yet identified; flagged).

## THE ENGINEERING BANK (why this took 13 hours instead of 3 minutes):
The multi-hour per-level cost was NOT mathematics: the shared
engine_v7.gate_report() recomputes a full O(N^3) matrix product inside
every (i,j) scan — O(N^5) total. Fixed locally (fast_gate_report,
compute-once-scan-O(N^2)); engine_v7.py deliberately untouched (shared
by other banked cells) — **cc: upstream patch recommended; any cell
importing gate_report at N >= 40 pays the same tax.** Post-fix: every
level ran in < 15 s. The killed 12h monolithic run and the level-10
"cap" decision are both moot; the FULL prereg table (incl. the kappa=14,
15 resonances) is banked. Second fix: G1's original 1e-40 tolerance was
unwinnable against the banked JSON's float64 storage for irrational
values; replaced by the exact closed form ([4|k] - [5|k]/phi at dps 60)
+ 1e-10 float sanity. tr_odd = (Z_full + det(w0)*Tr(S^2 rho(w)))/2
ported verbatim from the banked Gate-3 audit.
Artifacts: d4_level.py, d4_results_k{1..12}.json, d4_results_MERGED.json,
d4_k{1..12}.log. The wrong-quantity artifacts were deleted pre-relaunch.
Repo untouched.
