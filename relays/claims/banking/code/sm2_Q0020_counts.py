#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): what card Q0020 states and a banking seat can recompute from it: the counting of order-30
points, their 5-parts and the act line, and the T-covariance that the card offers as the structural reason for its
factor 5. Standard library only. The Frame C numerics (covariance residuals, alignment, hierarchy, classes) rest on a
construction the card gives only by reference, and are not computed here.

    python3 relays/claims/banking/code/sm2_Q0020_counts.py            # the counts
    python3 relays/claims/banking/code/sm2_Q0020_counts.py --control  # S in place of T: the tiling must fail

v = (a, b) in ((1/30)Z / Z)^2 of exact order 30, written as integers (A, B) mod 30; pairs +-v; v has a 5-part when 5
divides the reduced denominator of a; the act line is the set with 6v mod 1 in {k (1, 2) / 5}; T = [[1,1],[0,1]] acts by
v T^-1 = (a, b - a).
"""
import sys
from fractions import Fraction
from math import gcd

CONTROL = "--control" in sys.argv
pts = [(A, B) for A in range(30) for B in range(30) if 30 // gcd(30, gcd(A, B)) == 30]
pairs = {frozenset({(A, B), ((-A) % 30, (-B) % 30)}) for A, B in pts}
five = lambda v: Fraction(v[0], 30).denominator % 5 == 0
act = lambda v: ((6 * v[0]) % 30 * 2) % 30 == (6 * v[1]) % 30 and (6 * v[0]) % 30 != 0   # 6v = k(1,2)/5, k != 0
fp = {p for p in pairs if five(next(iter(p)))}
ap = {p for p in fp if act(next(iter(p)))}
Tinv = (lambda v: ((-v[1]) % 30, v[0])) if CONTROL else (lambda v: (v[0], (v[1] - v[0]) % 30))   # v S^-1 = (-b, a)
def image(p, j):
    out = set()
    for v in p:
        for _ in range(j): v = Tinv(v)
        out.add(v)
    return frozenset(out)
tiles = [{image(p, j) for p in ap} for j in range(5)]
union = set().union(*tiles)
disjoint = sum(len(t) for t in tiles) == len(union)
# which of the five non-vertical lines of P^1(F_5) each tile lies on (the slope of 6v mod 1)
def slope(p):
    A, B = next(iter(p)); x, y = (6 * A) % 30 // 6, (6 * B) % 30 // 6
    return (y * pow(x, -1, 5)) % 5 if x else "vertical"
slopes = [sorted({slope(p) for p in t}) for t in tiles]
print("points of exact order 30: %d; pairs +-v: %d" % (len(pts), len(pairs)))
print("DECISIVE: pairs with a 5-part: %d; on the act line: %d; ratio %s" % (len(fp), len(ap), Fraction(len(fp), len(ap))))
print("DECISIVE: the act line's pairs under T^0..T^4 (v -> v T^-1): disjoint %s, their union is the 5-part pairs %s; "
      "slopes of the five tiles %s" % (disjoint, union == fp, slopes))
ok = (len(pts), len(pairs), len(fp), len(ap)) == (576, 288, 240, 48) and disjoint and union == fp
print("NOT COMPUTED: the 15 invariants and their covariance residuals, alignment, hierarchy, the 1/60-grid rates and the "
      "12 classes: Frame C's construction is given on the card by reference only")
print("RESULT: the counting %s" % ("holds" if ok else "does not hold"))
sys.exit(0 if ok else 1)
