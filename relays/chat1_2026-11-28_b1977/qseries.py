"""P-227 exploration: exact q-series in x = q^(1/8) with Gaussian-rational coefficients.
A series is a dict {power of x: complex Fraction pair (re, im)}; truncated at x^N."""
from fractions import Fraction as F

N = 240                                     # x^240 = q^30


class S:
    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != (0, 0)}

    @staticmethod
    def c(re, im=0, k=0): return S({k: (F(re), F(im))})

    def __add__(self, o):
        d = dict(self.d)
        for k, (a, b) in o.d.items():
            x, y = d.get(k, (F(0), F(0))); d[k] = (x + a, y + b)
        return S(d)

    def __neg__(self): return S({k: (-a, -b) for k, (a, b) in self.d.items()})
    def __sub__(self, o): return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, S): o = S.c(o)
        d = {}
        for k1, (a1, b1) in self.d.items():
            for k2, (a2, b2) in o.d.items():
                k = k1 + k2
                if k > N: continue
                x, y = d.get(k, (F(0), F(0))); d[k] = (x + a1 * a2 - b1 * b2, y + a1 * b2 + b1 * a2)
        return S(d)
    __rmul__ = __mul__

    def conj(self): return S({k: (a, -b) for k, (a, b) in self.d.items()})
    def ord(self): return min(self.d) if self.d else None
    def lead(self): k = self.ord(); return None if k is None else self.d[k]

    def inv(self):
        """the recursion t_m = -(1/s0) sum_{j=1..m} s_j t_{m-j}, exact"""
        k0 = self.ord(); a0, b0 = self.d[k0]; n2 = a0 * a0 + b0 * b0
        i0 = (a0 / n2, -b0 / n2)
        mul = lambda p, q: (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])
        M = N + k0                                 # 1/self = x^-k0 sum t_m x^m, keep powers <= N
        sj = [self.d.get(k0 + j, (F(0), F(0))) for j in range(M + 1)]
        t = [i0]
        for m in range(1, M + 1):
            acc = (F(0), F(0))
            for j in range(1, m + 1):
                if sj[j] != (0, 0):
                    pr = mul(sj[j], t[m - j]); acc = (acc[0] + pr[0], acc[1] + pr[1])
            v = mul(i0, acc); t.append((-v[0], -v[1]))
        return S({m - k0: t[m] for m in range(M + 1) if m - k0 <= N})

    def qdq(self):                               # q d/dq x^m = (m/8) x^m
        return S({k: (a * F(k, 8), b * F(k, 8)) for k, (a, b) in self.d.items()})


def theta2():
    d = {}; n = 0
    while (2 * n + 1) ** 2 <= N:
        d[(2 * n + 1) ** 2] = (F(2), F(0)); n += 1
    return S(d)


def theta3(sign=1):
    d = {0: (F(1), F(0))}; n = 1
    while 4 * n * n <= N:
        d[4 * n * n] = (F(2 * (sign ** n)), F(0)); n += 1
    return S(d)


def sigma(k, n): return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eis(k, c):
    d = {0: (F(1), F(0))}
    for n in range(1, N // 8 + 1): d[8 * n] = (F(c * sigma(k - 1, n)), F(0))
    return S(d)


E2 = lambda: eis(2, -24)
E4 = lambda: eis(4, 240)
E6 = lambda: eis(6, -504)


def serre(f, k, e2):                             # D_k f = q df/dq - (k/12) E2 f
    return f.qdq() - e2 * f * S.c(F(k) / 12)
