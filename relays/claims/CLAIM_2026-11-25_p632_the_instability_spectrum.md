# CLAIM CARD — P-632: on B1813's s-family (the Farey transfer operator F_s), the fastest-growing mode is positive everywhere, the democratic constant at s = 0 exactly and strictly decreasing toward the parabolic point for 0 < s < 1; its growth falls to 1 at s = 1, where the continuous part of the spectrum meets it and the marginal mode 1/x lives at the cusp. Neither picks a τ-locus (NEGATIVE); the frame's flow on τ, the row's other route, has no flow on record to linearise

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 8fadd3f3e (one code line rewrapped at
  718935fa0, before the run) and its output at 0519cacba.
- kind: negative (a computation, with cited theorems)
- touches: P-632, P-713, P-441, P-468, P-471, P-629
- effect: conditions — P-632: on B1813's s-family, neither the fastest-growing nor the marginal mode picks a τ-locus.
  The democratic control at s = 0 reproduces the old circulant negative. The route through the frame's flow on τ is
  declined, since no flow is on record (FL-05, P-629).
- imports: Ruelle–Perron–Frobenius and the Gibbs property (positivity and full support of the leading mode's
  equilibrium state); Prellberg's continuous spectrum for the Farey operator. All are cited, not re-derived.
- premises on main: B852 (the Farey pressure and its method), B1813 (the s-family), P-713 (the transition places no τ),
  P-441 and P-468 (the critical line), P-629 (the symmetric points)
- decisive script: relays/chat1_2026-11-25_p632/p632_modes.py, SHA-256 e5d9879e6a3dda93. It needs numpy only and reads
  no file. Run as `python3 -I p632_modes.py` (about 20 s). Output p632_modes_out.txt, SHA-256 670c188fbe92a356; values
  in p632_modes.json.
- second computation: within the script, λ₁(s) by collocation at N = 64, 128 and 256 (agreeing to 2e-13 at N = 128
  and 256 for s ≤ 0.9) and by the weighted word sums Z₁₈/Z₁₇ (to 7e-5 at s = 0.25 and 6.3e-4 at s = 0.5).
- already on main?: the topic sweep at 88a1e9474 finds 13 arcs and 17 rows; none computes the family's spectrum. P-713
  and P-441 hold the negative for placing τ at the transition and on the critical line.
- what would make it fail:
  - a leading eigenfunction of F_s, 0 < s < 1, with an interior extremum;
  - an isolated eigenvalue of F_s whose eigenfunction concentrates at an interior point and grows relative to the
    leading mode;
  - a flow on τ, put on record, whose linearisation has an unstable or marginal mode at a point other than i, ω or the
    cusp.

## What it means

- [E] At s = 0 the fastest mode is the constant, with growth 2 per move. For s = 0.1 to 0.9 it is positive and strictly
  decreasing on [0, 1].
- [E] λ₁(s) falls from 2 to 1.0203 at s = 0.95, while the mode's mass within 0.05 of the parabolic point rises from 5 %
  to 30 %. F₁ fixes 1/x exactly.
- [J] The fastest mode charges everything, and the marginal mode lives at the cusp, so no τ-locus is picked by
  instability on this family.

0 of 19.
