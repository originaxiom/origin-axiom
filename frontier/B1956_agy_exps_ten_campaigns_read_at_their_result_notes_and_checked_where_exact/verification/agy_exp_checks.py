"""B1956: main's exact checks of arithmetic that agy-exp's campaigns rest on (no data; none of its code is run).
1. The one-loop gauge eliminant with the Standard Model's coefficients: sin^2 = 23/134 + (109/201) alpha_EM/alpha_3, and the
   differences (b2 - b3, b3 - b1, b1 - b2) = (23/6, -111/10, 109/15).
2. With a Pati-Salam stage above it, coefficients (b_4, b_2L, b_2R) = (-10, -7/3, -7/3) and the matching
   alpha_1^-1 = (3/5) alpha_2R^-1 + (2/5) alpha_4^-1: the added term is (506/(201 pi)) alpha_EM Delta_PS.
   Both are relations with a free scale; neither is compared with data here.
3. The points of period dividing 4 of the act on the torus: 45, split by order as 1 + 8 + 4 + 32; the Smith form of M^4 - 1.
4. E8's roots under Q = (2/3)(e1 + e2 + e3): 46 neutral, 32 colour singlets of charge +-1, 162 coloured.
5. Three units of flux on a torus give three zero modes: the count is the flux (an index statement, printed, not computed)."""
import itertools
from fractions import Fraction as Fr


def eliminant():
    b1, b2, b3 = Fr(41, 10), Fr(-19, 6), Fr(-7)
    Dn = Fr(5, 3) * b1 + b2 - Fr(8, 3) * b3                       # alpha_EM^-1 - (8/3) alpha_3^-1 = Dn * L
    intercept = (b2 - b3) / Dn; slope = 1 - (b2 - b3) / Dn * Fr(8, 3)
    return intercept, slope, (b2 - b3, b3 - b1, b1 - b2), Dn


def pati_salam():
    b4, b2l, b2r = Fr(-10), Fr(-7, 3), Fr(-7, 3)
    d3, d2, d1 = b4, b2l, Fr(3, 5) * b2r + Fr(2, 5) * b4          # shifts of alpha_3^-1, alpha_2^-1, alpha_1^-1 per Delta_PS / (2 pi)
    _, _, (b23, _, _), Dn = eliminant()
    coeff = (d2 - d3) - (b23 / Dn) * (Fr(5, 3) * d1 + d2 - Fr(8, 3) * d3)
    return coeff / 2                                               # times Delta_PS / pi


def period_four():
    M = ((2, 1), (1, 1))
    def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    M4 = mul(mul(M, M), mul(M, M)); A = ((M4[0][0] - 1, M4[0][1]), (M4[1][0], M4[1][1] - 1))
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    pts = [(a, b) for a in range(45) for b in range(45) if (A[0][0] * a + A[0][1] * b) % 45 == 0 and (A[1][0] * a + A[1][1] * b) % 45 == 0]
    from math import gcd
    orders = {}
    for a, b in pts:
        o = 45 // gcd(45, gcd(a, b)) if (a, b) != (0, 0) else 1; orders[o] = orders.get(o, 0) + 1
    g = gcd(gcd(A[0][0], A[0][1]), gcd(A[1][0], A[1][1]))
    return abs(det), len(pts), dict(sorted(orders.items())), (g, abs(det) // g), A


def e8_partition():
    R = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj; R.add(tuple(v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0: R.add(s)
    neutral = sum(1 for r in R if r[0] + r[1] + r[2] == 0)
    singlet = sum(1 for r in R if r[0] == r[1] == r[2] and r[0] != 0)
    return len(R), neutral, singlet, len(R) - neutral - singlet


if __name__ == "__main__":
    i, s, d, Dn = eliminant()
    print("1. one loop, Standard Model coefficients: sin^2 = %s + (%s) alpha_EM/alpha_3; differences (b2 - b3, b3 - b1, b1 - b2) = (%s, %s, %s)" % (i, s, *d))
    print("2. with the Pati-Salam stage (-10, -7/3, -7/3): the added term is (%s / pi) alpha_EM Delta_PS" % pati_salam())
    det, n, orders, smith, A = period_four()
    print("3. M^4 - 1 = %s: |det| = %d, %d points of period dividing 4, by order %s; Smith form %s" % (A, det, n, orders, smith))
    print("4. E8: %d roots = %d neutral + %d colour singlets of charge +-1 + %d coloured" % e8_partition())
    print("5. (a remark, not a check) a line bundle of degree k > 0 on a torus has k sections: three families from flux three is the input k = 3")
