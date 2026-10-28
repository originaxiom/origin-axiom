"""chat1, 2026-10-28: THE TWO W's, the exact checks behind the addendum to THE EXACT END, THE SELECTOR AND THE AUDIT.
Post hoc (written after main's B1802, 8399099f6), exact arithmetic, no data; committed before its one run.
B1802 puts W = diag(1, 1, 1, -1, -1) on the figure-eight's even fillings; the frame's counted line carries a central element
times W in its fibre b-holonomy. Do the two meet?
  1  the fibre's homology inside the mapping torus: coker(M - I) and coker(M + I) for M = LR = [[1, 1], [1, 2]] and its
     conjugate RL = [[2, 1], [1, 1]] (the order of each is |det|).
  2  conjugation in SU(5) cannot move a hypercharge holonomy: e^(2 pi i a 6Y) on the 5 has eigenvalues e^(-4 pi i a) (three
     times) and e^(6 pi i a) (twice); for a in (1/N)Z, N <= 60, distinct a mod 1 give distinct eigenvalue multisets unless
     both are central (5a an integer).
  3  covers: the least k >= 1 with M^k v = v (and with (-M)^k v = v) for the counted class (2/5, odd tenths), B1786's 12
     carriers, the order-5 and order-2 lines; and the order of M on (Z/N)^2 for N = 2, 5, 10, 25, 30.
Run:  python3 -B bridge_check.py"""
import math, cmath
from fractions import Fraction as Fr
from itertools import product
MS = {"LR": ((1, 1), (1, 2)), "RL": ((2, 1), (1, 1))}


def act(M, v, s=1):
    a, b = v
    return ((s * (M[0][0] * a + M[0][1] * b)) % 1, (s * (M[1][0] * a + M[1][1] * b)) % 1)


def period(M, v, s=1, cap=10000):
    w = act(M, v, s); k = 1
    while w != v and k < cap:
        w = act(M, w, s); k += 1
    return k


def smith_order(M, s):
    d = (s * M[0][0] - 1) * (s * M[1][1] - 1) - (s * M[0][1]) * (s * M[1][0])
    return abs(d)


print("1  the fibre's homology in the mapping torus, |coker(sM - I)| = |det(sM - I)|:")
for n, M in MS.items():
    print("   %s: s = +1 (the monodromy) %d; s = -1 (with the involution) %d" % (n, smith_order(M, 1), smith_order(M, -1)))
print("   so H1 of the mapping torus is Z (the base loop) plus a group of order %d: every flat abelian bundle is trivial on the fibre"
      % smith_order(MS["LR"], 1))

bad = 0; tested = 0
def eig(a):
    return (round(cmath.exp(-4j * math.pi * a).real, 12), round(cmath.exp(-4j * math.pi * a).imag, 12),
            round(cmath.exp(6j * math.pi * a).real, 12), round(cmath.exp(6j * math.pi * a).imag, 12))
for N in range(1, 61):
    vals = sorted({Fr(k, N) for k in range(N)})
    for a1 in vals:
        for a2 in vals:
            if a1 >= a2 or (5 * a1).denominator == 1 and (5 * a2).denominator == 1: continue
            tested += 1
            e1, e2 = eig(float(a1)), eig(float(a2))
            if sorted([e1[:2]] * 3 + [e1[2:]] * 2) == sorted([e2[:2]] * 3 + [e2[2:]] * 2): bad += 1
print("2  pairs a != a' (mod 1, denominators <= 60, not both central) with equal eigenvalue multisets on the 5: %d of %d" % (bad, tested))

counted = [(Fr(2, 5), Fr(k, 10)) for k in (1, 3, 5, 7, 9)]
b1786 = [(Fr(2, 5), Fr(k, 25)) for k in (3, 4, 11, 12, 17, 19, 21, 23)] + [(Fr(2, 5), b) for b in (Fr(1, 6), Fr(13, 30), Fr(23, 30), Fr(5, 6))]
order5 = [(Fr(2, 5), Fr(k, 5)) for k in range(5)]
order2 = [(Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))]
print("3  the least k with M^k v = v (and with (-M)^k v = v):")
for n, M in MS.items():
    for name, vs in (("the counted class (2/5, odd tenths)", counted), ("B1786's 12 carriers", b1786), ("slope 2/5, order 5", order5),
                     ("the order-2 lines", order2)):
        print("   %s, %-36s M: %s | -M: %s" % (n, name, sorted({period(M, v) for v in vs}), sorted({period(M, v, -1) for v in vs})))
    for N in (2, 5, 10, 25, 30):
        pts = [(Fr(i, N), Fr(j, N)) for i, j in product(range(N), repeat=2)]
        print("   %s, the order of M on (Z/%d)^2: %d (of -M: %d)" % (n, N, math.lcm(*[period(M, v) for v in pts]), math.lcm(*[period(M, v, -1) for v in pts])))
print("bridge_check exit 0")
