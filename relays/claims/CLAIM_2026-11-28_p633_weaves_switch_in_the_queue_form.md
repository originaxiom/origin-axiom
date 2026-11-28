# CLAIM CARD — P-633: Mayer's transfer operator has spectral radius 1 at s = 1 (to 1e-27) with one sign change of λ₁ − 1 on the grid s = 0.80, 0.85, …, 1.20, and the Gauss–Kuzmin–Wirsing constant and the Lyapunov exponent as controls; so, read as a weight exp(−cℓ/6π) per thread under the geometric clock, the weave's critical c is 6π, as the reading and the critical exponent 1 give by construction, here confirmed numerically (the seat's card of 2026-11-25 in the queue's form)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 0a89dddd2fa84dda59eb6c77ebd3b114f78050db
- kind: computation
- touches: P-633, P-629
- effect: adds — P-633's critical c for the non-interacting weave, c* = 6π s* with s* = 1, under the stated reading of
  c and the geometric clock (under B1813's move clock it would be 6π log 2, which this script does not compute)
- scope: frame: the modular surface's closed geodesics, coded by the Gauss map's periodic orbits; object: the
  abscissa of convergence of Z(c) = Σ over closed threads of exp(−(c/6π) ℓ); reach: single; hypotheses: P-633's c read
  as a weight per unit thread length; the geometric clock (lengths ℓ); Mayer's operator discretised by collocation at
  32 Chebyshev nodes, the terms n ≤ 60 summed and the tail n > 60 taken by Hurwitz zeta values, at 60 digits
- identifications: P-633's c is the coefficient of a weight exp(−cℓ/6π) per thread of geodesic length ℓ (a new
  coupling: not P-488's c, nor P-132's coefficient)
- definitions: (L_s f)(x) = Σ_{n ≥ 1} (x + n)^(−2s) f(1/(x + n)) on [0, 1]; λ₁(s) its spectral radius. Z(c) converges
  iff λ₁(c/6π) < 1, so c* = 6π s*, with λ₁(s*) = 1. The Gauss–Kuzmin–Wirsing constant is λ₂(1) =
  −0.3036630028987326586...; the Gauss map's Lyapunov exponent is π²/(6 log 2), and d log λ₁/ds at s = 1 is its
  negative.
- imports: the standard coding of PSL(2, Z)'s closed geodesics by the Gauss map's periodic orbits (two to one on mirror
  pairs); the theorem that a lattice in PSL(2, R) has critical exponent 1; and the invariance of the Gauss measure,
  which makes λ₁(1) = 1 exactly; all standard mathematics
- premises on main: B1813 (the s-family and its two clocks), B1814 (the critical clock), B852 (the Farey map's
  transition), B1872 (the level-5 subweave)
- decisive script: relays/chat1_2026-11-25_p633/card_p633.py, SHA-256 948ac8776397f7c5, depends on the standard library
  and mpmath, run as python3 relays/chat1_2026-11-25_p633/card_p633.py, output SHA-256 65b906e7371a8bdc
- decisive lines: 6 lines marked "DECISIVE:", SHA-256 06e91718cbc0018d
- failing control: python3 relays/chat1_2026-11-25_p633/card_p633.py --control
- second computation: none that shares no code. The old card's referee reran the script identically and reproduced the
  operator's values in a second basis (a power series about x = 1, 160 digits) to 12 digits on the grid, not
  committed. The controls are independent known constants. The decisive script runs the sealed p633_switch.py
  (SHA-256 f697477746682401, at 86a46e4c4) unchanged.
- already on main?: topic_sweep.py "weave.s switch|critical c|Mayer" at 68b04c69d: 2 of 1760 arcs and 3 register rows
  match the words; the old card's sweep at 88a1e9474 found no arc that states a switch between phases in c, and B1814
  holds B1813's counting rule at s = 1
- what would make it fail: λ₁(1) away from 1, or a second sign change of λ₁ − 1 on the grid (between grid points
  the crossing rests on λ₁ decreasing in s, which is not computed here); controls away from their
  constants; a reading of c other than a weight per unit length, or another clock, which rescale c*. The control
  makes the weight (x + n)^(−3s) on purpose, computed as the true operator at 3s/2: λ₁ − 1 then stays negative on the
  grid, and the claim's check fails. It is an easy control, but it runs the sealed operator.
