"""POST HOC (thought of after EXPECTATIONS.md was written; recorded in NOTES.md).
The report says the mark's order-10 halves need the 6-fold cover (strict, inner) or the 3-fold (charge conjugation).
Question: the least cyclic-cover degree k for each of the four classes on the k-fold cover (monodromy M^k):
  I : M^k v = v;   O : M^k v = +-v;   Z : (M^k - I) v in (1/5 Z)^2;   ZO : (+-M^k - I) v in (1/5 Z)^2.
Also the W176 bound (row 1464's aside): gamma = L^2 R, |tr - 2| = 2, fixed points in (1/2 Z/Z)^2.
Plant: the same function on v = (1/5, 2/5) (order 5, on the mark line) must give I 2, O 1, Z 1, ZO 1, not the halves' values.
Run: OMP_NUM_THREADS=1 nice -n 10 python3 -B posthoc_cover.py
"""
from fractions import Fraction as F

MS = ((2, 1), (1, 1))


def mpow(M, k):
    R = ((1, 0), (0, 1))
    for _ in range(k):
        R = tuple(tuple(sum(R[i][t] * M[t][j] for t in range(2)) for j in range(2)) for i in range(2))
    return R


def app(A, v):
    return (A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1])


def in_lattice(x, centre):
    m = 5 if centre else 1
    return all((m * c).denominator == 1 for c in x)


def least_k(v, cls, M=MS, kmax=200):
    signs = (1, -1) if "O" in cls else (1,)
    centre = "Z" in cls
    for k in range(1, kmax + 1):
        w = app(mpow(M, k), v)
        for s in signs:
            if in_lattice((s * w[0] - v[0], s * w[1] - v[1]), centre):
                return k
    return None


if __name__ == "__main__":
    halves = [(F(7, 10), F(2, 5)), (F(1, 5), F(9, 10)), (F(7, 10), F(9, 10))]
    for h in halves:
        print("half", tuple(str(x) for x in h), {c: least_k(h, c) for c in ("I", "O", "Z", "ZO")})
    plant = (F(1, 5), F(2, 5))
    pk = {c: least_k(plant, c) for c in ("I", "O", "Z", "ZO")}
    print("plant (1/5, 2/5)", pk, "differs from halves:", pk != {c: least_k(halves[0], c) for c in ("I", "O", "Z", "ZO")})
    # all 12 order-10 halves of the mark line
    ml = [(F(k % 5, 5), F(2 * k % 5, 5)) for k in range(1, 5)]
    allh = {((m[0] / 2 + F(a, 2)) % 1, (m[1] / 2 + F(b, 2)) % 1) for m in ml for a in (0, 1) for b in (0, 1)}
    allh = {h for h in allh if max(h[0].denominator, h[1].denominator, 1) == 10 or (h[0].denominator * h[1].denominator) % 10 == 0 and 10 % h[0].denominator == 0 and 10 % h[1].denominator == 0 and 2 not in (h[0].denominator, h[1].denominator) or False}  # v2: keep order 10
    print("all 12 halves, set of (I, O, Z, ZO) least k:", {tuple(least_k(h, c) for c in ("I", "O", "Z", "ZO")) for h in allh}, len(allh))
    # every order-10 line: least k per class
    hist = {}
    for i in range(10):
        for j in range(10):
            from math import gcd
            if gcd(gcd(i, j), 10) != 1:
                continue
            v = (F(i, 10), F(j, 10))
            key = tuple(least_k(v, c) for c in ("I", "O", "Z", "ZO"))
            hist[key] = hist.get(key, 0) + 1
    print("order-10 lines, (I, O, Z, ZO) least k histogram:", hist)
    # W176 bound: gamma = L^2 R
    L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1))
    g = tuple(tuple(sum(mpow(L, 2)[i][t] * R[t][j] for t in range(2)) for j in range(2)) for i in range(2))
    fixed = [(a, b) for a in range(2) for b in range(2) if all(x % 2 == 0 for x in (app(g, (a, b))[0] - a, app(g, (a, b))[1] - b))]
    print("L^2 R =", g, "tr", g[0][0] + g[1][1], "fixed points in (1/2 Z/Z)^2:", len(fixed), "of 4")
