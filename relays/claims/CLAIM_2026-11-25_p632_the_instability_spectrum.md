# CLAIM CARD — P-632: on B1813's s-family (word by word L_s, whose L↔R-symmetric part is the Farey operator F_s), the fastest-growing mode is positive everywhere, the democratic constant at s = 0 exactly, and for 0 < s < 1 strictly decreasing in x, so largest at the parabolic point (completely monotone). Its growth falls to 1 at s = 1, where the continuous part [0, 1] meets it, and the marginal mode 1/x lives at the cusp; the odd part has no eigenvalue above 1. Neither picks a locus by the criterion fixed before the run, and on τ the record's lifts pick none (NEGATIVE). The frame's flow on τ, the row's other route, is declined: there is no dynamics for τ on record

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 8fadd3f3e (one code line rewrapped at
  718935fa0, before the run) and its output at 0519cacba. The relay and this card were corrected after their referee
  read.
- kind: negative (a computation, with cited theorems)
- touches: P-632, P-713, P-441, P-468, P-471, P-629, P-073, P-591
- effect: conditions — P-632: on B1813's s-family, neither the fastest-growing nor the marginal mode picks a locus.
  The democratic control at s = 0 reproduces the old circulant negative, as an identity. The route through the
  frame's flow on τ is declined, since no dynamics for τ is on record (P-073, under P-629).
- imports:
  - Prellberg (J. Phys. A 36, 2455, 2003): the continuous spectrum [0, 1] for every s, and a simple leading eigenvalue
    for s < 1;
  - Hofbauer–Keller quasi-compactness on functions of bounded variation;
  - Yuri's weak Gibbs property.
  All are cited, not re-derived. The complete monotonicity of h_s is the referee's argument, stated in the relay.
- premises on main: B852 (the Farey pressure and its method), B1813 (the s-family), P-713 (the transition places no τ),
  P-441 and P-468 (the critical line), P-629 (the symmetric points)
- decisive script: relays/chat1_2026-11-25_p632/p632_modes.py, SHA-256 e5d9879e6a3dda93. It needs numpy only and reads
  no file. Run as `python3 -I p632_modes.py` (about 20 s). Output p632_modes_out.txt, SHA-256 670c188fbe92a356; values
  in p632_modes.json.
- second computation:
  - within the script, λ₁(s) by collocation at N = 64, 128 and 256 (agreeing to 2e-13 at N = 128 and 256 for s ≤ 0.9),
    and by the weighted word sums Z₁₈/Z₁₇ (to 7e-5 at s = 0.25 and 6.3e-4 at s = 0.5);
  - by the referee, not committed: λ₁ by inducing on the Gauss map (to 3e-15 for s ≤ 0.7), the odd part's spectrum, and
    the equilibrium state's mass.
- already on main?: the topic sweep at 88a1e9474 finds 13 arcs and 17 rows; none computes more than the leading
  eigenvalue (B852). P-713 and P-441 hold the negative for placing τ at the transition and on the critical line.
- what would make it fail:
  - a leading eigenfunction of F_s, 0 < s < 1, with an interior extremum;
  - an isolated eigenvalue above 1 of F_s or F_s⁻, other than λ₁, whose eigenfunction concentrates at an interior
    point;
  - a dynamics for τ, put on record, whose linearisation has an unstable or marginal mode at a point other than the
    symmetric points of the potential's own group (i and ω for SL(2, Z); i and the cusps for the theta group).

## What it means

- [E] At s = 0 the fastest mode is the constant, with growth 2 per move. For s = 0.1 to 0.9 it is positive and strictly
  decreasing in x, and by the referee's argument it is completely monotone for every 0 < s < 1.
- [E] λ₁(s) falls from 2 to 1.0203 at s = 0.95. The mode's Lebesgue mass within 0.05 of the parabolic point rises from
  5 % to 30 %, and its equilibrium state's from 2⁻¹⁹ to 15 % (the referee's). F₁ fixes 1/x exactly.
- [J] The fastest mode charges everything, and the marginal mode lives at the cusp, so instability picks no locus on
  this family.

0 of 19.
