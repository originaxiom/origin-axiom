# CLAIM CARD — P-631: on the fibre the two-loop sunset repeats the one-loop shape (C₁,₁,₁ = E₃ + ζ(3)) and only the figure-eight's E₂² is new; with the principle for Im τ sealed (a two-loop term selects Im τ only where it is at most a third of the one-loop term), two loops select no Im τ: near the cusp every balance sits at |V₂/V₁| = 3/4, and none of 12 stationary points on Im τ ∈ [1.2, 20] meets the bound

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 852afb281 and its output at 719443701.
- kind: negative
- touches: P-631, P-373, P-629, P-380
- effect: conditions — P-373's principle for Im τ: at two loops, with untwisted six-dimensional fields, no stationary
  point of V₁ + V₂ off the symmetric points meets the sealed bound. Adds to P-631 the inventory: the sunset's shape is
  the one-loop E₃ plus a constant, and the figure-eight's E₂² is new τ-dependence. The couplings that weight both are
  at least three free numbers (FL-05).
- imports: the six-dimensional star relation and Zagier's identity C₁,₁,₁ = E₃ + ζ(3), both standard mathematics,
  the second reproduced numerically here.
- premises on main: B1686 and B1704 (the one-loop term and its run to the cusp), P-380 (the SM seat's census), P-629
  (stationarity at i and ω)
- decisive script: relays/chat1_2026-11-25_p631/p631_two_loop.py, SHA-256 aa5c850a33237e43; depends on only the
  standard library, numpy and mpmath, and reads no file. Run as `python3 -I p631_two_loop.py` (90 s). Output
  p631_two_loop_out.txt, SHA-256 0c9f970bcab17a05.
- second computation: within the script, E₂ and E₃ are computed two ways (Fourier expansion and direct lattice sum,
  agreeing to 2.9e-10), and C₁,₁,₁ by a lattice sum against Zagier's closed form (to 6e-5). No independent second
  computation yet.
- already on main?: `scripts/checks/topic_sweep.py "two-loop|two loop|2-loop|modular graph|Zagier"` at 88a1e9474
  finds 11 arcs and 3 rows; none computes a two-loop vacuum term on the fibre. The nearest are P-631 itself and the
  one-loop arcs B1686 and B1704.
- what would make it fail:
  - a stationary point of V₁ + V₂ with Im τ > 1.2, off the symmetric points, where |V₂| ≤ |V₁|/3;
  - a lattice C₁,₁,₁ that differs from E₃ + ζ(3) beyond its extrapolation error;
  - a combination of Eisenstein series that reproduces E₂² to its evaluation precision.

## What it means

- [E] The sunset with three distinct images is π³ C₁,₁,₁(τ)/A³ times the couplings, and C₁,₁,₁ = E₃ + ζ(3). Its
  stationary points are the one-loop term's.
- [E] The figure-eight is ∝ E₂², outside the span of the Eisenstein series (its cusp term in y¹ has no match).
- [E] Near the cusp, V = −αE₃ + βE₂² is stationary at y* = 3αc₃/(4βc₂²), where |V₂/V₁| = 3/4 for every β/α.
- [J] Two loops do not supply P-373's principle: a holder of Im τ needs a non-perturbative term, or the couplings
  derived, and a check beyond the leading orders. Twisted fields, the divergent coincident-image terms and the
  numerators of fermion and gauge loops are not covered.

0 of 19.
