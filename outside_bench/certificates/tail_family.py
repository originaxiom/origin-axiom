#!/usr/bin/env python3
"""THE FALSE THETA IS THE TAIL OF A FAMILY, NOT A COINCIDENCE OF TWO KNOTS.

Memo 184 found Phi_{m(5_2)} = sum_{k>=0} (-1)^k q^{k(k+1)/2}, a false theta rather
than (q;q)_inf, and observed (section 2) that the same series is Park's printed first
non-zero block for m(5_2) AND for m(7_3) -- stated there as "an observation on two
knots, not a claim".

Park's own braid presentations put those two knots in one 3-strand family:

    beta_m  =  sigma_2^{-(2m-1)} sigma_1^{-1} sigma_2 sigma_1^{-1}

    m = 2  ->  s2^-3 ...  = m(5_2)   [Park section 5.1.1]
    m = 3  ->  s2^-5 ...  = m(7_3)   [Park section 5.1.2]

so m = 1 and m = 4 are reachable with exactly the machinery memo 184 used, and cost
nothing new.  This certificate computes the bottom-end colored Jones tail for
m = 1, 2, 3, 4 from the bench's implementation of Park eq (10)+(12)+(13).

RESULT
   m = 1 is the UNKNOT (determinant 1, J_2 = 1) and its tail is the trivial series 1.
   m = 2, 3, 4 -- determinants 7, 13, 19 -- ALL have the SAME tail,
        Phi = 1 - q + q^3 - q^6 + q^10 - ...
   on eight stabilised coefficients each.

So the ceiling question memo 184 section 3 preregistered is not about one knot: under
memo 177 addendum 4's mechanism, EVERY member of this family would have
c_eff(1/Phi) = infinity.

Gate 5: exact Laurent arithmetic.  No measured input.

CONTROLS:
  C1  the family is identified, not assumed: determinants 1, 7, 13, 19 come out of the
      computed J_2, and 7 = det(5_2), 13 = det(7_3) agree with Park's own naming of the
      m = 2 and m = 3 braids.
  C2  a control the family supplies free: m = 1 closes to the UNKNOT, and the same tail
      code returns the trivial series 1 for it -- so the method does not manufacture a
      false theta out of nothing.
  C3  the tails are stable in the colour: identical at n = 7 and n = 8.
"""
import sys, io, os, contextlib
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(_HERE, 'park_rmatrix_check.py')).read()
src = src.split('print()\nprint("Park eq (10)+(12)+(13) vs the references:")')[0]
g = {'__name__': '__main__'}
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(src, g)
cj = g['cj']
print(buf.getvalue().strip())

def word(m): return [-2]*(2*m-1) + [-1, 2, -1]
def J(n, w):
    d = cj(n, w, 3)
    assert all(e % 4 == 0 for e in d), "half-integer q power"
    return {e//4: int(c) for e, c in d.items()}
PHI = [0]*24
for k in range(24):
    e = k*(k+1)//2
    if e < 24: PHI[e] = (-1)**k

print("\n" + "="*78)
print("C1  identify each member of Park's family from its own Jones polynomial")
print("="*78)
DET = {}
JONES = {}
for m in (1, 2, 3, 4):
    d = J(2, word(m)); lo = min(d)
    co = [d.get(lo+i, 0) for i in range(max(d)-lo+1)]
    DET[m] = abs(sum(c*(-1)**(lo+i) for i, c in enumerate(co)))
    JONES[m] = (lo, co)
    print("   m=%d : beta = s2^-%-2d s1^-1 s2 s1^-1   det = %-3d   J_2 = q^%d %s"
          % (m, 2*m-1, DET[m], lo, co))
c1 = (DET[1] == 1 and DET[2] == 7 and DET[3] == 13 and DET[4] == 19
      and JONES[2][1] == [1,-1,2,-1,1,-1])
print("   determinants 1, 7, 13, 19;  7 = det(5_2) and 13 = det(7_3), which is how Park")
print("   names the m = 2 and m = 3 braids ->", "PASSED" if c1 else "FAILED")

print("\n" + "="*78)
print("the stabilising BOTTOM end -- the end memo 177 addendum 7's surviving rule")
print("selects for these knots, whose blocks run down")
print("="*78)
def tail(m, NS=(6, 7, 8)):
    H = {}
    for n in NS:
        d = J(n, word(m)); lo = min(d)
        H[n] = [d.get(lo+i, 0) for i in range(24)]
    a, b = H[NS[-2]], H[NS[-1]]
    k = 0
    while k < len(a) and a[k] == b[k]: k += 1
    return b[:k], H
c2 = c3 = True
same = []
for m in (1, 2, 3, 4):
    st, H = tail(m)
    stable = len(st) >= 6
    c3 &= stable
    if m == 1:
        triv = (st[:1] == [1] and all(v == 0 for v in st[1:]) and len(st) >= 10)
        c2 = triv
        print("   m=1 (UNKNOT) : %s  -> trivial series 1 : %s"
              % (st[:10], "PASSED" if triv else "FAILED"))
    else:
        ok = (st == PHI[:len(st)])
        same.append(ok)
        print("   m=%d          : %-34s = Phi on %d coefficients : %s"
              % (m, str(st), len(st), ok))
print("   Phi = sum_{k>=0} (-1)^k q^{k(k+1)/2} =", PHI[:10])
main = all(same) and len(same) == 3
print("\n   >>> all three non-trivial members share the SAME false theta tail :",
      "YES" if main else "NO")
print("""
   CONSEQUENCE.  Memo 184 section 3 preregistered two outcomes on whether memo 177
   addendum 4's mechanism c_edge(K) = c_eff(1/Phi_K) survives a false-theta tail.
   That cell is not about one knot: 1/Phi has a pole inside the unit disc, so under the
   mechanism EVERY member of this family has no finite ceiling on c_eff.  Memo 184's
   declared prior was OUTCOME B, and an infinite family of hyperbolic knots with
   unbounded c_eff is harder to believe than one, so this pushes the same way.

   FENCES.  (i) The stabilised prefix per knot is the one printed above, and nothing
   beyond it is used; a series agreeing with 1 - q + q^3 - q^6 in that many coefficients
   and differing later is not excluded by this alone -- for m(5_2) and m(7_3) the exact coincidence with Park's printed blocks is
   what makes it more (memo 184 section 2), and for m = 4 nobody prints anything.
   (ii) Which END is the right one is memo 177 addendum 7's surviving, UNVERIFIED rule;
   this certificate uses it, as memo 184 did, and does not test it.
   (iii) Memo 184 section 2's stronger observation -- that the tail IS the first
   non-zero block -- was NOT confirmed for m = 4 here.  The large color R-matrix on a
   ten-crossing braid is not converged at the weight cutoffs this bench can reach, and
   after memo 183 addendum 1 section 5 (a block stable across eight strata and wrong)
   an unconverged block is not evidence either way.  Recorded as attempted and
   inconclusive, with the cost named, so it is not cheaply repeated.""")
print("="*78)
OK = {"C1 family identified": c1, "C2 unknot control": c2, "C3 tails stable in the colour": c3,
      "shared false theta": main}
print("CONTROLS:", {k: ("PASSED" if v else "FAILED") for k, v in OK.items()})
if not all(OK.values()): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("ALL CONTROLS PASSED.")
