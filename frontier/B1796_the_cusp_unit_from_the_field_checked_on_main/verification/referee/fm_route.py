"""Referee B1796 -- W123 re-derived with the referee's own series code (no B1691 code), in the eigenline basis over Q.
Series in x = q^(1/8): (val, [c_val, c_val+1, ...]) truncated at x^PREC.  Lines (B1700's): P = R0, M = R1 + i R2,
N = R1 - i R2 for R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4); in this basis every series is rational.
d(m) = dim of weight-3/2 weakly holomorphic forms with line orders >= (1,7,3) - 8m, computed as
{f0 R + f1 DR + f2 D2R : f_j in M_*} at weight 3/2 + 12N, N = max(0, max m), with orders >= (1,7,3) + 8(N - m).
    python3 -B fm_route.py [mmin mmax]"""
import sys, itertools
from fractions import Fraction as F

PREC = 420


class Ser:
    def __init__(self, val, c):
        self.val, self.c = val, list(c)[: max(0, PREC - val + 1)]

    def coef(self, k):
        i = k - self.val
        return self.c[i] if 0 <= i < len(self.c) else F(0)

    def __add__(self, o):
        v = min(self.val, o.val); top = PREC
        return Ser(v, [self.coef(k) + o.coef(k) for k in range(v, top + 1)])

    def __neg__(self): return Ser(self.val, [-a for a in self.c])
    def __sub__(self, o): return self + (-o)

    def scale(self, s): return Ser(self.val, [s * a for a in self.c])

    def __mul__(self, o):
        v = self.val + o.val; n = PREC - v + 1
        out = [F(0)] * max(0, n)
        for i, a in enumerate(self.c):
            if a == 0: continue
            for j, b in enumerate(o.c):
                if i + j >= n: break
                if b: out[i + j] += a * b
        return Ser(v, out)

    def order(self):
        for i, a in enumerate(self.c):
            if a != 0: return self.val + i
        return None

    def inv(self):
        k0 = self.order(); s = [self.coef(k0 + j) for j in range(PREC + 2 * abs(k0) + 2)]
        t = [F(1) / s[0]]
        n = PREC + k0 + 1 + abs(k0)
        for m in range(1, n):
            acc = sum((s[j] * t[m - j] for j in range(1, m + 1) if j < len(s) and s[j]), F(0))
            t.append(-acc / s[0])
        return Ser(-k0, t)

    def qdq(self): return Ser(self.val, [a * F(self.val + i, 8) for i, a in enumerate(self.c)])


def mono(d):  # dict exponent -> coefficient, val 0
    top = max(0, max(d)); c = [F(0)] * (PREC + 1)
    for k, a in d.items():
        if 0 <= k <= PREC: c[k] += a
    return Ser(0, c)


th2 = mono({(2 * n + 1) ** 2: 2 for n in range(0, 40) if (2 * n + 1) ** 2 <= PREC})
th3 = mono({0: 1, **{4 * n * n: 2 for n in range(1, 40) if 4 * n * n <= PREC}})
th4 = mono({0: 1, **{4 * n * n: 2 * (-1) ** n for n in range(1, 40) if 4 * n * n <= PREC}})


def sigma(k, n): return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eis(k, c): return mono({0: 1, **{8 * n: c * sigma(k - 1, n) for n in range(1, PREC // 8 + 1)}})


E2, E4, E6 = eis(2, -24), eis(4, 240), eis(6, -504)
# sanity: E4^3 - E6^2 = 1728 Delta, Delta = q prod (1-q^n)^24 has order x^8 with leading 1
D = (E4 * E4 * E4 - E6 * E6).scale(F(1, 1728))
assert D.order() == 8 and D.coef(8) == 1 and D.coef(16) == -24
di = (th2 * th3 * th4).inv()
P = -(th2 * th2 * di); M = -((th4 * th4 + th3 * th3) * di); N = (th3 * th3 - th4 * th4) * di
R = [P, M, N]


def serre(f, k): return f.qdq() - (E2 * f).scale(F(k) / 12)


DR = [serre(f, F(-1, 2)) for f in R]
D2R = [serre(f, F(3, 2)) for f in DR]
print("line orders R, DR, D2R:", [[f.order() for f in v] for v in (R, DR, D2R)])
print("residues mod 8 per line (R, DR, D2R):",
      [[sorted({(f.val + i) % 8 for i, a in enumerate(f.c) if a != 0}) for f in v] for v in (R, DR, D2R)])

_mb = {}


def Mbasis(w):
    if w < 0: return []
    if w in _mb: return _mb[w]
    res = []
    for a in range(w // 4 + 1):
        for b in range(w // 6 + 1):
            if 4 * a + 6 * b == w:
                f = mono({0: 1})
                for _ in range(a): f = f * E4
                for _ in range(b): f = f * E6
                res.append(f)
    _mb[w] = res
    return res


def rank(rows):
    rows = [list(r) for r in rows if any(r)]
    rk, col = 0, 0
    ncol = len(rows[0]) if rows else 0
    while rk < len(rows) and col < ncol:
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None: col += 1; continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        p = rows[rk][col]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                f = rows[i][col] / p
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[rk])]
        rk += 1; col += 1
    return rk


_cand = {}


def cands(Nn):
    if Nn in _cand: return _cand[Nn]
    c = [[f * g for g in R] for f in Mbasis(2 + 12 * Nn)] + [[f * g for g in DR] for f in Mbasis(12 * Nn)] + \
        [[f * g for g in D2R] for f in Mbasis(12 * Nn - 2)]
    _cand[Nn] = c
    return c


def d_of(m, Nn=None):
    if Nn is None: Nn = max(0, max(m))
    cand = cands(Nn)
    bounds = [b + 8 * (Nn - mi) for b, mi in zip((1, 7, 3), m)]
    assert max(bounds) < PREC - 20
    conds = []
    for li in range(3):
        lo = min(c[li].order() for c in cand if c[li].order() is not None)
        for k in range(lo, bounds[li]):
            row = [c[li].coef(k) for c in cand]
            if any(row): conds.append(row)
    return len(cand) - (rank(conds) if conds else 0), len(cand), len(conds)


if __name__ == "__main__":
    for n in range(0, 7):
        print("uniform n=%d: d=%d (cands %d, nonzero cond rows %d)" % ((n,) + d_of((n, n, n))))
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (-1, 2)
    bad = []; tot = 0
    for m in itertools.product(range(lo, hi + 1), repeat=3):
        d, nc, ncond = d_of(m); tot += 1
        if d != max(0, sum(m)): bad.append((m, d))
    print("range %d..%d: %d vectors; d(m) != max(0, sum m) at %d:" % (lo, hi, tot, len(bad)), bad[:40])
    # N-independence: recompute a few at a larger N
    for m in [(1, 1, 1), (2, -1, -1), (-1, 2, -1), (0, 1, 0), (2, 2, -1)]:
        print("N-check", m, d_of(m)[0], d_of(m, Nn=max(0, max(m)) + 2)[0])
