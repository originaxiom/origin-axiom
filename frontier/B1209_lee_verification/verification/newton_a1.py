"""R52-3, leg 1 INDEPENDENT: |a_1| = 1 at every ideal point of 4_1, from OUR OWN A-polynomial.

Lee (arXiv:2502.11950, sec 7.4) states that the admissible tangent vectors at an ideal point number
exactly |a_1|, where m ~ t^{a_1} in a uniformizer t. His Appendix A computes a_1 = +1, -1, +1, -1 at
the four ideal points of 4_1. That is not something we need to take on trust: a_1 and b_1 are the
orders of vanishing of the meridian and longitude eigenvalues, so the pair (a_1, b_1) is a primitive
EDGE VECTOR of the Newton polygon of the A-polynomial -- which main banked at B67.
"""
from itertools import combinations
from fractions import Fraction as F

# The figure-eight A-polynomial (classical; main's B67 derives it from the trace map):
#   A(M,L) = -M^4 + L(1 - M^2 - 2M^4 - M^6 + M^8) - L^2 M^4
terms = {(4, 0): -1, (0, 1): 1, (2, 1): -1, (4, 1): -2, (6, 1): -1, (8, 1): 1, (4, 2): -1}
pts = sorted(terms)
print("A-polynomial monomials (deg_M, deg_L):", pts)

def hull(points):
    pts = sorted(set(points))
    def half(pts):
        out = []
        for p in pts:
            while len(out) >= 2:
                (x1, y1), (x2, y2) = out[-2], out[-1]
                if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) <= 0: out.pop()
                else: break
            out.append(p)
        return out
    lo, up = half(pts), half(pts[::-1])
    return lo[:-1] + up[:-1]

H = hull(pts)
print("Newton polygon vertices:", H)

from math import gcd
print("\nEDGES -- each corresponds to an ideal point; (a_1, b_1) is its primitive vector:")
a1s = []
for i in range(len(H)):
    (x1, y1), (x2, y2) = H[i], H[(i + 1) % len(H)]
    dM, dL = x2 - x1, y2 - y1
    g = gcd(abs(dM), abs(dL)) or 1
    pM, pL = dM // g, dL // g
    # Lee's convention: (a_1, b_1) = (ord m, ord l) = (dL, dM) up to sign (his Case 1 is (1, -4)).
    a1, b1 = pL, pM
    a1s.append(abs(a1))
    slope = F(b1, a1) if a1 else None
    print(f"    edge {(x1,y1)}->{(x2,y2)}  primitive ({pM},{pL})  =>  (a_1, b_1) = ({a1}, {b1})"
          f"   boundary slope b_1/a_1 = {slope}")

print(f"\n|a_1| over the four ideal points: {a1s}")
assert set(a1s) == {1}, "if any |a_1| exceeded 1 the base point would NOT be unique"
print("=> |a_1| = 1 AT EVERY IDEAL POINT, derived from our own A-polynomial.")
print("   Lee's Appendix A reports a_1 = +1, -1, +1, -1: AGREES, and B1201's independent")
print("   bench computation is confirmed from the source's own structure.")

print("\nCROSS-CHECK -- the boundary slopes:")
slopes = sorted({F(b, a) for a, b in [(p, q) for p, q in
                 [( (H[(i+1)%len(H)][1]-H[i][1])//(gcd(abs(H[(i+1)%len(H)][0]-H[i][0]),
                     abs(H[(i+1)%len(H)][1]-H[i][1])) or 1),
                    (H[(i+1)%len(H)][0]-H[i][0])//(gcd(abs(H[(i+1)%len(H)][0]-H[i][0]),
                     abs(H[(i+1)%len(H)][1]-H[i][1])) or 1) ) for i in range(len(H))]] if a})
print(f"    computed: {[str(s) for s in slopes]}")
print("    the figure-eight's known boundary slopes are 0 and +-4 -- the non-zero ones MATCH,")
print("    and Lee's four (a_1,b_1) = (1,-4), (-1,-4), (1,4), (-1,4) reproduce exactly these.")

print("""
CONSEQUENCE
  The set of admissible tangential base points at an ideal point is a TORSOR under Z/|a_1|
  (rescaling the uniformizer by an |a_1|-th root of unity). For m004 that group is TRIVIAL at
  all four ideal points. It is therefore NOT Z/2 and NOT V_4: there is NO contact between Lee's
  choice-of-base-point and the programme's orientation bit (B1174/B1182/B1183).
VERIFIED""")
