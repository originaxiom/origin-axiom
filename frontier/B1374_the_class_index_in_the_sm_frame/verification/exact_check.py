#!/usr/bin/env python3
"""B1374: exact verification over the cyclotomic field Q(zeta_N) of the six Standard-Model sector counts at a generation-shaped pair
found over prime fields.  Own implementation: elements of K = Q(zeta_N) as coefficient vectors modulo the N-th cyclotomic polynomial,
K-ranks as Q-ranks of the regular-representation blow-up (sympy DomainMatrix over QQ) divided by [K : Q]; the same cohomology
definitions as index_lib.py (left Fox convention, H^0, H^1, the cusp torus, r_1, n = a_1 - r_1, I = n(V) - n(V*)).
Usage: python3 exact_check.py member N j psiY psiG   (j = index of the locus in the sorted intersection list; psi as exponent tuples)"""
import sys, os, math, itertools
from fractions import Fraction as Fr
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
argv = sys.argv; sys.argv = ['x', 'none']
import importlib.util
spec = importlib.util.spec_from_file_location("cis", os.path.join(os.path.dirname(os.path.abspath(__file__)), "class_index_sm_frame.py"))
cis = importlib.util.module_from_spec(spec); spec.loader.exec_module(cis)

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

name, N, j = argv[1], int(argv[2]), int(argv[3]); psiY = tuple(int(x) for x in argv[4].strip('()').split(',')); psiG = tuple(int(x) for x in argv[5].strip('()').split(','))
p = {60: 421, 48: 337, 12: 61}[N]
B = cis.Bench(name, p, N=N); gens = B.gens; rels = B.rels; mu, lam = B.mu, B.lam
common = sorted(set(tuple(chi[g] for g in gens) for (chi, h1, ct) in B.loci))     # the same ordering as the census on one prime
for q in ({60: (541, 601), 48: (433, 577), 12: (181, 241)}[N]):
    Bq = cis.Bench(name, q, N=N); common = sorted(set(common) & set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Bq.loci))
chi_exp = common[j]; chi = dict(zip(gens, chi_exp))
K = Cyc(N); print(f"K = Q(zeta_{N}), degree {K.d}; {name}: gens {gens}, rels {rels}; locus chi = {chi_exp}, psi_Y = {psiY}, psi_gamma = {psiG}")
chi2 = {g: K.zeta(2 * chi[g]) for g in gens}
# H^1(pi; chi^2) and a non-coboundary cocycle, exactly
rep1 = KRep(K, gens, {g: [[chi2[g]]] for g in gens})
d1 = K.vstack(*[K.hstack(*[rep1.fox(r)[g] for g in gens]) for r in rels]); Z = K.nullspace(d1, len(gens))
bvec = [K.sub(chi2[g], K.const(1)) for g in gens]; rb = 0 if all(K.is_zero(x) for x in bvec) else 1
h1 = len(Z) - rb; ct = None
for z in Z:
    if rb == 0 or K.rank([bvec, z]) == 2: ct = dict(zip(gens, z)); break
print(f"h^1(pi; chi^2) = {h1} exactly; non-split cocycle found: {ct is not None}")
chiv = {g: K.zeta(chi[g]) for g in gens}
rho = {g: [[chiv[g], K.mul(ct[g], K.inv(chiv[g]))], [K.const(0), K.inv(chiv[g])]] for g in gens}
R = KRep(K, gens, rho); assert all(R.word(r) == K.eye(2) for r in rels), "rho is not a representation"
print("rho_chi is a representation over K (relators to the identity, exactly)", flush=True)
def I_of(psi_exp):
    psiv = {g: K.zeta(psi_exp[g]) for g in gens}
    V = KRep(K, gens, {g: K.mscale(psiv[g], rho[g]) for g in gens}); assert all(V.word(r) == K.eye(2) for r in rels)
    a0, a1, t0, t1, r1 = data(V, rels, mu, lam); b0, b1, s0, s1, q1 = data(V.dual(), rels, mu, lam)
    assert r1 + q1 == t1 == s1, "annihilator identity"
    I = (a1 - r1) - (b1 - q1); assert I == (a0 - b0) + s0 - r1, "B1297 identity"
    return I, (a0, a1, t0, r1), (b0, b1, s0, q1)
out = []
for (lab, sy, sg) in cis.SM_SECTORS:
    psi = {g: (sy * psiY[i] + sg * psiG[i]) % N for i, g in enumerate(gens)}
    I, dV, dVd = I_of(psi); out.append(I)
    print(f"  {lab:28s} psi = {tuple(psi[g] for g in gens)}: I = {I:+d}   (a0,a1,t0,r1) V = {dV}  V* = {dVd}")
print(f"EXACT counts (Q, u^c, e^c, d^c, L, nu^c) = {tuple(out)}")
