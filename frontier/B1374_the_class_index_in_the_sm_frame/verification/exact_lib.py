#!/usr/bin/env python3
"""B1374: exact arithmetic over the cyclotomic field Q(zeta_N) for the one-cusped index -- the field, representations, the cohomology
dimensions of the group and of the cusp torus (the same definitions as index_lib.py).  Shared by exact_check.py (the census members)
and by B1375's exact_check_cover.py (the tower's own presentations)."""
import sympy as sp
from fractions import Fraction as Fr
from sympy.polys.matrices import DomainMatrix
from sympy import QQ

class Cyc:
    """Q(zeta_N)"""
    def __init__(self, N):
        self.N = N; x = sp.symbols('x'); P = sp.Poly(sp.cyclotomic_poly(N, x), x)
        self.c = [Fr(int(a)) for a in reversed(P.all_coeffs())]; self.d = P.degree()   # low -> high, monic
    def el(self, v): v = [Fr(a) for a in v] + [Fr(0)] * self.d; return tuple(v[:self.d])
    def const(self, q): return self.el([q])
    def zeta(self, k):        # zeta^k reduced
        k %= self.N; v = [Fr(0)] * (k + 1); v[k] = Fr(1); return self.reduce(v)
    def reduce(self, p):
        p = list(p) + [Fr(0)] * max(0, self.d - len(p))
        for k in range(len(p) - 1, self.d - 1, -1):
            if p[k] != 0:
                q = p[k]; p[k] = Fr(0)
                for i in range(self.d): p[k - self.d + i] -= q * self.c[i]
        return tuple(p[:self.d])
    def add(self, a, b): return tuple(x + y for x, y in zip(a, b))
    def sub(self, a, b): return tuple(x - y for x, y in zip(a, b))
    def neg(self, a): return tuple(-x for x in a)
    def mul(self, a, b):
        p = [Fr(0)] * (2 * self.d - 1)
        for i, x in enumerate(a):
            if x == 0: continue
            for j, y in enumerate(b):
                if y != 0: p[i + j] += x * y
        return self.reduce(p)
    def is_zero(self, a): return all(x == 0 for x in a)
    def regmat(self, a):
        cols = []; x = self.const(1)
        for i in range(self.d): cols.append(self.mul(a, x)); x = self.mul(x, self.zeta(1))
        return [[cols[j][i] for j in range(self.d)] for i in range(self.d)]
    def inv(self, a):
        M = sp.Matrix(self.regmat(a)); e = sp.Matrix([1] + [0] * (self.d - 1)); b = M.LUsolve(e)
        return tuple(Fr(int(v.p), int(v.q)) for v in b)
    # matrices over K
    def eye(self, n): return [[self.const(1) if i == j else self.const(0) for j in range(n)] for i in range(n)]
    def zeros(self, n, m): return [[self.const(0)] * m for _ in range(n)]
    def mmul(self, A, B):
        n, k, m = len(A), len(B), len(B[0])
        return [[self._dot([A[i][l] for l in range(k)], [B[l][j] for l in range(k)]) for j in range(m)] for i in range(n)]
    def _dot(self, u, v):
        s = self.const(0)
        for x, y in zip(u, v): s = self.add(s, self.mul(x, y))
        return s
    def madd(self, A, B): return [[self.add(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
    def msub(self, A, B): return [[self.sub(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
    def mscale(self, c, A): return [[self.mul(c, x) for x in r] for r in A]
    def T(self, A): return [list(r) for r in zip(*A)]
    def vstack(self, *Ms): return [list(r) for M in Ms for r in M]
    def hstack(self, *Ms): return [sum((list(M[i]) for M in Ms), []) for i in range(len(Ms[0]))]
    def rank(self, A):
        if not A or not A[0]: return 0
        rows = []
        for i in range(len(A)):
            for a in range(self.d):
                row = []
                for j in range(len(A[0])):
                    R = self.regmat(A[i][j]); row += [QQ(int(R[a][b].numerator), int(R[a][b].denominator)) for b in range(self.d)]
                rows.append(row)
        r = DomainMatrix(rows, (len(rows), len(rows[0])), QQ).rank(); assert r % self.d == 0; return r // self.d
    def nullspace(self, A, ncols):
        """basis of the right kernel over K by Gauss-Jordan over K"""
        R = [list(r) for r in A]; piv = []; r = 0
        for c in range(ncols):
            if r >= len(R): break
            k = next((i for i in range(r, len(R)) if not self.is_zero(R[i][c])), None)
            if k is None: continue
            R[r], R[k] = R[k], R[r]; iv = self.inv(R[r][c]); R[r] = [self.mul(iv, x) for x in R[r]]
            for i in range(len(R)):
                if i != r and not self.is_zero(R[i][c]):
                    f = R[i][c]; R[i] = [self.sub(x, self.mul(f, y)) for x, y in zip(R[i], R[r])]
            piv.append(c); r += 1
        free = [c for c in range(ncols) if c not in piv]; out = []
        for fc in free:
            v = [self.const(0)] * ncols; v[fc] = self.const(1)
            for i, pc in enumerate(piv): v[pc] = self.neg(R[i][fc])
            out.append(v)
        return out
    def inverse2(self, A):
        if len(A) == 1: return [[self.inv(A[0][0])]]
        a, b = A[0]; c, d = A[1]; det = self.sub(self.mul(a, d), self.mul(b, c)); di = self.inv(det)
        return [[self.mul(di, d), self.neg(self.mul(di, b))], [self.neg(self.mul(di, c)), self.mul(di, a)]]

class KRep:
    def __init__(self, K, gens, mats):
        self.K = K; self.gens = gens; self.d = len(mats[gens[0]]); self.M = dict(mats)
        for g in gens: self.M[g.upper()] = K.inverse2(mats[g])
    def word(self, w):
        R = self.K.eye(self.d)
        for ch in w: R = self.K.mmul(R, self.M[ch])
        return R
    def fox(self, w):
        K = self.K; D = {g: K.zeros(self.d, self.d) for g in self.gens}; pre = K.eye(self.d)
        for ch in w:
            g = ch.lower()
            if ch.islower(): D[g] = K.madd(D[g], pre)
            else: D[g] = K.msub(D[g], K.mmul(pre, self.M[ch]))
            pre = K.mmul(pre, self.M[ch])
        return D
    def dual(self): return KRep(self.K, self.gens, {g: self.K.T(self.K.inverse2(self.M[g])) for g in self.gens})

def data(rep, rels, mu, lam):
    K = rep.K; d = rep.d; gens = rep.gens; I = K.eye(d)
    d0 = K.vstack(*[K.msub(rep.M[g], I) for g in gens]); rk0 = K.rank(d0); a0 = d - rk0
    d1 = K.vstack(*[K.hstack(*[rep.fox(r)[g] for g in gens]) for r in rels])
    Z1 = K.nullspace(d1, len(gens) * d); a1 = len(Z1) - rk0
    Wm, Wl = rep.word(mu), rep.word(lam); Am, Al = K.msub(Wm, I), K.msub(Wl, I)
    BT = K.vstack(Am, Al); rkBT = K.rank(BT); t0 = d - rkBT
    ZT = K.hstack(K.mscale(K.const(-1), Al), Am); t1 = 2 * d - K.rank(ZT) - rkBT
    Dm, Dl = rep.fox(mu), rep.fox(lam)
    Res = K.vstack(K.hstack(*[Dm[g] for g in gens]), K.hstack(*[Dl[g] for g in gens]))
    if Z1:
        cols = K.mmul(Res, K.T(Z1)); r1 = K.rank(K.hstack(cols, BT)) - rkBT
    else: r1 = 0
    return a0, a1, t0, t1, r1

