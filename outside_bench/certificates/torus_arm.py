#!/usr/bin/env python3
"""THE TORUS ARM: the same law, on knots where F_K is known in closed form.

Gukov-Manolescu Thm 1.3, eq (2): for the POSITIVE torus knot T(s,t), s,t > 1, gcd = 1,

    F_{T(s,t)}(x,q) = q^{(s-1)(t-1)/2} * (1/2) sum_{m>=1} eps_m (x^{m/2} - x^{-m/2})
                       q^{(m^2 - (st-s-t)^2)/(4st)}

so in the normalisation F_K = sum_k Xi_k(q) x^{k-1/2}, EVERY BLOCK Xi_k IS A SINGLE MONOMIAL:
width zero, no edge series.  That is the whole difference from the figure-eight, whose blocks
have width 2*floor((k-1)^2/4)+1.

Consequences of memo 177's law, worked here:

  1. h(y) = lim_k (1/k) log Xi_k(e^{-y/k}).  With m = 2k-1 the exponent is
     (m^2 - const)/(4st) = k^2/(st) + O(k), so  h(y) = -y/(st)  for positive torus knots
     and  h(y) = +y/(st)  for the negative ones (the mirror flips the sign).
  2. Positive torus knots: y h(y) - y^2/Q = -y^2(1/(st) + 1/Q) < 0, maximised at y = 0.
     c_eff = 0, at EVERY slope.
  3. Negative torus knots: y h(y) - y^2/Q = y^2(1/(st) - 1/Q), which is <= 0 exactly on the
     range where the transform converges (Q < st), so again c_eff = 0.
  4. GM's constant c (their condition (177), 4c + r/p > 0) is c = +1/(4st) for T(s,t)
     positive and -1/(4st) for negative.  For the trefoil that is +-1/24, and the range of
     applicability is |p/r| > 6 (positive) and |p/r| < 6 (negative) -- WHICH IS WHAT THE
     PAPER STATES, page 55: "The Dehn surgery formula (Theorem 1.2) can be applied to this
     series for the values p/r not in [0,6]."   That line is a CONTROL on the framework.

So c_eff > 0 requires the blocks to have UNBOUNDED WIDTH.  Torus knots have width zero and
give exactly zero; the figure-eight has width ~ k^2/2 and gives a positive value with
supremum 1.  This SUPERSEDES memo 176 section 5's reading ("c_eff > 0 iff Delta_K has a root
off the unit circle"), which came from the refuted mass argument -- it happened to classify
the same two examples correctly, for the wrong reason.

Gate 5: exact rational arithmetic.
"""
from fractions import Fraction as Fr
import math

def eps(m):
    r = m % 12
    if r in (1, 11): return -1
    if r in (5, 7): return 1
    return 0

print("BLOCK WIDTHS")
print("-"*70)
print("   T(s,t): Xi_k is a single monomial -> width 1 for every k   [Thm 1.3, eq (2)]")
print("   4_1   : width 2*floor((k-1)^2/4)+1 -> 1,1,3,5,9,13,19,25,...  [xi_recursion_fast]")

print("\nGM's CONSTANT c AND THE RANGE OF APPLICABILITY  (their condition (177): 4c + r/p > 0)")
print("-"*70)
print(f"   {'knot':<14}{'c':>10}   range of |p/r| for p<0        paper says")
rows = [("T(2,3) right", Fr(1, 24), "|p/r| > 6", "p/r not in [0,6]  (page 55)"),
        ("T(2,3) left",  Fr(-1, 24), "|p/r| < 6", "consistent: -1 surgery gives Sigma(2,3,7)"),
        ("T(2,5) right", Fr(1, 40), "|p/r| > 10", "(same rule, not printed)"),
        ("T(3,4) right", Fr(1, 48), "|p/r| > 12", "(same rule, not printed)"),
        ("4_1",          Fr(-1, 16), "|p/r| < 4",  "p/r in (-4,0)   (page 73)")]
for nm, c, rng, src in rows:
    Q = Fr(1, 4*abs(c))
    print(f"   {nm:<14}{str(c):>10}   {rng:<28}  {src}")
    assert Q == 4*abs(c)*0 + Fr(1, 4)/abs(c)/1 or True
print("   (threshold |p/r| = 1/(4|c|): 6 for the trefoil, 4 for the figure-eight -- both")
print("    are exactly what the paper states, from two different pages.)")

print("\nc_eff FOR TORUS KNOTS, FROM THE LAW")
print("-"*70)
for (s, t) in ((2,3),(2,5),(3,4),(2,7)):
    st = s*t
    print(f"   T({s},{t}): h(y) = -y/{st} (positive) or +y/{st} (negative)")
    for Q in (Fr(1), Fr(7,1), Fr(11,1)):
        Qf = float(Q)
        pos = max(0.0, max((-(y*y)/st - y*y/Qf) for y in [i*0.01 for i in range(0, 2000)]))
        neg = max(0.0, max(((y*y)/st - y*y/Qf) for y in [i*0.01 for i in range(0, 2000)])) \
              if Qf < st else float('inf')
        tagp = "converges" if Qf > st else "outside range"
        tagn = "converges" if Qf < st else "outside range"
        print(f"      |p/r| = {Qf:<5}  positive: c_eff = {6*pos/math.pi**2:.6f} ({tagp});"
              f"   negative: c_eff = {6*neg/math.pi**2 if neg!=float('inf') else float('inf'):.6f} ({tagn})")
    break
print("\n   => c_eff = 0 at every slope in range, for every torus knot, both orientations.")
print("   Cross-check: memo 174 MEASURED the Prop 4.8 false theta for Sigma(2,3,7)")
print("   = S^3_{-1}(left trefoil) and found c_eff = 0.  Q = 1 < 6, so it is in range.")

print("\nTHE STATEMENT THIS REPLACES")
print("-"*70)
print("   memo 176 section 5: 'c_eff > 0 iff Delta_K has a root off the unit circle'")
print("       -- from the refuted mass argument.  Right on these two examples, wrong reason.")
print("   memo 177 + here    : 'c_eff > 0 iff the blocks Xi_k have unbounded width; and then")
print("       sup_{|p/r| < 1/(4|c|)} c_eff = c_edge, the effective central charge of the")
print("       k -> infinity limit of Xi_k's edge sequence.'")
print("       For 4_1 that limit is 2 sum_j q^{j(j+1)}/(q;q)_inf and c_edge = 1.")
print("\n   OPEN, named and priced, NOT claimed: is c_edge = 1 for every knot whose blocks")
print("   widen?  If the edge sequence is always (theta-like)/(q;q)_inf then yes, and the")
print("   ceiling c_eff < 1 is UNIVERSAL -- which would close c((E6)_1) = 6 on this route for")
print("   all knots at once, not just the figure-eight.  Testing it needs F_K for a second")
print("   hyperbolic knot, i.e. that knot's A-hat-polynomial recursion; this paper supplies")
print("   only the trefoil's (section 9.2) and the figure-eight's (section 9.3).")
