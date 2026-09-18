"""Own exact arithmetic in Q(zeta_m) = Q[x]/Phi_m(x), coefficients Fraction. Independent of the record's code."""
from fractions import Fraction
from functools import lru_cache

def poly_divmod(a, b):
    a = list(a); out = [Fraction(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        while a and a[-1] == 0: a.pop()
        if len(a) < len(b): break
        c = a[-1] / b[-1]; d = len(a) - len(b); out[d] = c
        for i, bb in enumerate(b): a[d + i] -= c * bb
        while a and a[-1] == 0: a.pop()
    return out, a

@lru_cache(maxsize=None)
def cyclotomic(m):
    """Phi_m as a list of Fractions, low degree first. Computed by dividing x^m - 1 by Phi_d, d|m, d<m."""
    num = [Fraction(0)] * m + [Fraction(1)]; num[0] = Fraction(-1)
    for d in range(1, m):
        if m % d == 0:
            num, r = poly_divmod(num, list(cyclotomic(d)))
            assert not any(r), (m, d)
    while num and num[-1] == 0: num.pop()
    return tuple(num)

class Cyc:
    """the field Q(zeta_m); elements are tuples of Fractions of length deg = phi(m)"""
    def __init__(self, m):
        self.m = m; self.phi = list(cyclotomic(m)); self.deg = len(self.phi) - 1
        self._pw = []
        for k in range(2 * self.deg + max(2, m) + 2):
            self._pw.append(self._reduce_monomial(k))
    def _reduce_monomial(self, k):
        v = [Fraction(0)] * (k + 1); v[k] = Fraction(1)
        _, r = poly_divmod(v, self.phi)
        r = list(r) + [Fraction(0)] * (self.deg - len(r))
        return tuple(r[:self.deg])
    def zero(self): return (Fraction(0),) * self.deg
    def one(self): return self.zeta(0)
    def zeta(self, k):
        k %= self.m
        return self._pw[k]
    def add(self, a, b): return tuple(x + y for x, y in zip(a, b))
    def sub(self, a, b): return tuple(x - y for x, y in zip(a, b))
    def neg(self, a): return tuple(-x for x in a)
    def mul(self, a, b):
        d = self.deg; acc = [Fraction(0)] * d
        for i, x in enumerate(a):
            if x == 0: continue
            for j, y in enumerate(b):
                if y == 0: continue
                c = x * y; mon = self._pw[i + j]
                for t in range(d): acc[t] += c * mon[t]
        return tuple(acc)
    def is_zero(self, a): return all(x == 0 for x in a)
    def inv(self, a):
        # extended Euclid in Q[x]: find s with s*a = 1 mod Phi_m
        def trim(p):
            p = list(p)
            while p and p[-1] == 0: p.pop()
            return p
        def psub(p, q):
            n = max(len(p), len(q)); o = [Fraction(0)] * n
            for i, x in enumerate(p): o[i] += x
            for i, x in enumerate(q): o[i] -= x
            return trim(o)
        def pmul(p, q):
            if not p or not q: return []
            o = [Fraction(0)] * (len(p) + len(q) - 1)
            for i, x in enumerate(p):
                for j, y in enumerate(q): o[i + j] += x * y
            return trim(o)
        r0, r1 = trim(self.phi), trim(a)
        assert r1, "zero has no inverse"
        s0, s1 = [Fraction(1)], []          # s0*? bookkeeping: r_i = s_i * a mod Phi is not tracked; track t for a instead
        t0, t1 = [], [Fraction(1)]          # r0 = phi, r1 = a; t0 = 0, t1 = 1 so that r_i = (..)*phi + t_i*a
        while r1:
            q, r = poly_divmod(r0, r1)
            q = trim(q); r = trim(r)
            t2 = psub(t0, pmul(q, t1))
            r0, r1, t0, t1 = r1, r, t1, t2
        assert len(r0) == 1, ("gcd not constant -- Phi_m reducible or a divisible", len(r0))
        c = r0[0]
        res = [x / c for x in t0]
        _, res = poly_divmod(res + [Fraction(0)] * self.deg, self.phi)
        res = list(res) + [Fraction(0)] * self.deg
        return tuple(res[:self.deg])

def rank_cyc(F, rows, ncols):
    """rank of a matrix over F (rows = list of lists of field elements)"""
    R = [list(r) for r in rows]; rk = 0
    for c in range(ncols):
        piv = None
        for i in range(rk, len(R)):
            if not F.is_zero(R[i][c]): piv = i; break
        if piv is None: continue
        R[rk], R[piv] = R[piv], R[rk]
        iv = F.inv(R[rk][c]); R[rk] = [F.mul(iv, x) for x in R[rk]]
        for i in range(len(R)):
            if i != rk and not F.is_zero(R[i][c]):
                f = R[i][c]; R[i] = [F.sub(x, F.mul(f, y)) for x, y in zip(R[i], R[rk])]
        rk += 1
        if rk == len(R): break
    return rk
