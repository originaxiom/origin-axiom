"""B1957, check 5: agy-002's gate 2, the part main can recompute on its own tools (data-free).
Row 3: the cusp exponents of frame C by level, from B1788's tropical rule as B1945 and B1949 use it: the least exponent of
m2/m3 and of m1/m3 over all points of exact order N, for the down pair (1, 2) and the lepton pair (-3, 6), readings S, S~.
Row 1: the Wang sequence: det(M - 1) and the Smith form."""
import pathlib, sys
from fractions import Fraction as Fr
from math import gcd
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification")); import tropical as T
P = {rd: T.polys(rd) for rd in ("S", "St")}
ex = lambda ql, qr, a, rd: T.predict(P[rd], T.E(ql * a, qr * a))


def minima(ql, qr, N, rd):
    pts = sorted({Fr(i, N) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N})
    es = [ex(ql, qr, a, rd) for a in pts]
    return min(e[0] for e in es), min(e[1] for e in es)


if __name__ == "__main__":
    for N in (5, 10, 15):
        for rd in ("S", "St"):
            d = minima(1, 2, N, rd); l = minima(-3, 6, N, rd)
            print("N = %2d, %-2s: least exponents (m2/m3, m1/m3): down %s, lepton %s; ratios lepton/down: %s, %s" % (N, rd, tuple(str(x) for x in d), tuple(str(x) for x in l), l[0] / d[0], l[1] / d[1]))
    for N in (10,):
        for rd in ("S",):
            sw = [(str(a), tuple(str(x) for x in ex(1, 2, a, rd)), tuple(str(x) for x in ex(-3, 6, a, rd))) for a in (Fr(1, 10), Fr(3, 10))]
            print("N = 10, S, pointwise at a = 1/10 and 3/10 (down, lepton):", sw)
    M = [[2, 1], [1, 1]]; A = [[M[0][0] - 1, M[0][1]], [M[1][0], M[1][1] - 1]]
    print("Wang: M - 1 = %s, det %d: the fibre's H_1 contributes nothing, H_1(m004) = Z, H_2 = 0, H^2 = 0" % (A, A[0][0] * A[1][1] - A[0][1] * A[1][0]))
