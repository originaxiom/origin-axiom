#!/usr/bin/env python3
"""THE RELATIVE TRIPLE PRODUCT on a once-punctured-torus bundle, at chain level.

G = <x, y, t | t x t^-1 = Phi(x), t y t^-1 = Phi(y)>,  F = <x, y> free,  Phi an automorphism of F fixing
lam = [x, y] = x y x^-1 y^-1 as a word;  P = <t, lam> = Z^2 the peripheral subgroup.

For left G-modules A, B, H, an invariant functional T: A (x) B (x) H -> k, cocycles a in Z^1(G;A), b in Z^1(G;B),
h in Z^1(G;H) and a relative lift e of a (a(p) = p e - e on P), the number

    Y = <omega, C> - <eps, z>,     omega(g1,g2,g3) = T(a(g1), g1 b(g2), g1 g2 h(g3)),
                                   eps(p, q)       = T(e, b(p), p h(q)),

is the value of the relative class (a,e) u b u h in H^3(G, P; k) = H^3(M, dM; k) on the relative fundamental class
(C, z):  z = [t|lam] - [lam|t]  the torus,  C a 3-chain of the normalised bar complex of G with  dC = z.

THE CHAIN.  sigma = [x|y] + [xy|x^-1] + [xyx^-1|y^-1] - [x|x^-1] - [y|y^-1],  d sigma = -[lam]   (the fibre rel boundary).
prism for conjugation by t:   h[g] = [t|g] - [g'|t],   h[g|k] = [t|g|k] - [g'|t|k] + [g'|k'|t],   g' = t g t^-1 = Phi(g);
                              d h + h d = id - c_t.
filling in the free group (the bar resolution against the Fox resolution, contracting homotopy s(u[..]) = [u|..]):
                              K[g|k] = sum over Fox terms (sign, u, i) of k of  sign [g|u|x_i],   dK(w) = w for a 2-cycle w of F.
C = h(sigma) + K(Phi_* sigma - sigma).   The identity dC = z is CHECKED as an identity of integer chains (check_chain).

Conventions: cocycles f(gh) = f(g) + g f(h); d[g|k] = [k] - [gk] + [g]; d[g|k|l] = [k|l] - [gk|l] + [g|kl] - [g|k].
Elements of G in normal form (f, n) = f t^n, f a reduced word in x, y (1, 2; negative = inverse), n >= 0.
"""
import sys, os, pathlib
from collections import defaultdict

X, Y = 1, 2

def reduce(w):
    out = []
    for g in w:
        if out and out[-1] == -g: out.pop()
        else: out.append(g)
    return tuple(out)
def inv(w): return tuple(-g for g in reversed(w))

class Bundle:
    """the group G for a given automorphism Phi = {X: word, Y: word} of the free group"""
    def __init__(self, Phi):
        self.Phi = {X: tuple(Phi[X]), Y: tuple(Phi[Y])}
        self.lam = (X, Y, -X, -Y)
        assert self.phi(self.lam) == self.lam, "Phi must fix the commutator as a word"
    def phi(self, w, n=1):
        for _ in range(n):
            out = []
            for g in w: out += self.Phi[g] if g > 0 else inv(self.Phi[-g])
            w = reduce(out)
        return tuple(w)
    def mul(self, a, b):
        (f, n), (g, m) = a, b
        return (reduce(f + self.phi(g, n)), n + m)
    def F(self, w): return (reduce(w), 0)
    T = ((), 1)
    ID = ((), 0)

    # ---------------------------------------------------------------- chains (trivial coefficients, normalised)
    def norm(self, c):
        out = defaultdict(int)
        for cell, k in c.items():
            if k and all(g != self.ID for g in cell): out[cell] += k
        return {cell: k for cell, k in out.items() if k}
    def add(self, *chains):
        out = defaultdict(int)
        for c in chains:
            for cell, k in c.items(): out[cell] += k
        return self.norm(out)
    def scale(self, c, s): return {cell: s * k for cell, k in c.items()}
    def boundary(self, c):
        out = defaultdict(int)
        for cell, k in c.items():
            n = len(cell)
            out[cell[1:]] += k
            for i in range(n - 1):
                out[cell[:i] + (self.mul(cell[i], cell[i + 1]),) + cell[i + 2:]] += k * (-1) ** (i + 1)
            out[cell[:-1]] += k * (-1) ** n
        return self.norm(out)
    def conj_t(self, g):                                   # t g t^-1 for g in F
        f, n = g; assert n == 0
        return (self.phi(f), 0)
    def prism(self, c):                                    # h on 1- and 2-chains of F
        out = defaultdict(int); t = self.T
        for cell, k in c.items():
            if len(cell) == 1:
                g, = cell; out[(t, g)] += k; out[(self.conj_t(g), t)] -= k
            else:
                g, q = cell; g1, q1 = self.conj_t(g), self.conj_t(q)
                out[(t, g, q)] += k; out[(g1, t, q)] -= k; out[(g1, q1, t)] += k
        return self.norm(out)
    def fox_terms(self, w):                                # (sign, prefix word, generator) for each letter of w
        out = []; pre = ()
        for g in w:
            if g > 0: out.append((1, pre, g)); pre = reduce(pre + (g,))
            else: pre = reduce(pre + (g,)); out.append((-1, pre, -g))
        return out
    def fill(self, c):                                     # K on 2-chains of F
        out = defaultdict(int)
        for (g, q), k in c.items():
            assert g[1] == 0 and q[1] == 0
            for (s, u, i) in self.fox_terms(q[0]):
                out[(g, (u, 0), ((i,), 0))] += k * s
        return self.norm(out)
    def push(self, c):                                     # Phi_* on chains of F
        out = defaultdict(int)
        for cell, k in c.items(): out[tuple(self.conj_t(g) for g in cell)] += k
        return self.norm(out)
    def fundamental(self):
        Fw = self.F
        sigma = self.norm({(Fw((X,)), Fw((Y,))): 1, (Fw((X, Y)), Fw((-X,))): 1, (Fw((X, Y, -X)), Fw((-Y,))): 1,
                           (Fw((X,)), Fw((-X,))): -1, (Fw((Y,)), Fw((-Y,))): -1})
        lam = Fw(self.lam)
        assert self.boundary(sigma) == {(lam,): -1}, "d sigma = -[lam]"
        w = self.add(self.push(sigma), self.scale(sigma, -1))
        assert self.boundary(w) == {}, "Phi_* sigma - sigma is a cycle"
        E = self.fill(w)
        assert self.boundary(E) == w, "the filling: dK(w) = w"
        C = self.add(self.prism(sigma), E)
        z = self.norm({(self.T, lam): 1, (lam, self.T): -1})
        assert self.boundary(C) == z, "dC = z"
        assert self.boundary(z) == {}
        return C, z, sigma

# -------------------------------------------------------------------- modules over GF(p)
def mmul(A, B, p): return [[sum(A[i][l] * B[l][j] for l in range(len(B))) % p for j in range(len(B[0]))] for i in range(len(A))]
def mvec(A, v, p): return [sum(A[i][j] * v[j] for j in range(len(v))) % p for i in range(len(A))]
def eye(d): return [[int(i == j) for j in range(d)] for i in range(d)]
def minv(A, p):
    n = len(A); R = [list(A[i]) + [int(i == j) for j in range(n)] for i in range(n)]
    for c in range(n):
        k = next(i for i in range(c, n) if R[i][c] % p)
        R[c], R[k] = R[k], R[c]; iv = pow(R[c][c], p - 2, p); R[c] = [v * iv % p for v in R[c]]
        for i in range(n):
            if i != c and R[i][c] % p:
                f = R[i][c]; R[i] = [(v - f * u) % p for v, u in zip(R[i], R[c])]
    return [r[n:] for r in R]

class Module:
    """a representation of G: matrices for x, y, t over GF(p)"""
    def __init__(self, B, mx, my, mt, p, check=True):
        self.B, self.p, self.d = B, p, len(mx)
        self.M = {X: mx, Y: my, -X: minv(mx, p), -Y: minv(my, p)}; self.Mt = mt
        if check:
            for g in (X, Y):
                lhs = mmul(mmul(mt, self.M[g], p), minv(mt, p), p)
                assert lhs == self.rhoF(B.Phi[g]), "not a representation of G"
    def rhoF(self, w):
        R = eye(self.d)
        for g in w: R = mmul(R, self.M[g], self.p)
        return R
    def rho(self, el):
        f, n = el; R = self.rhoF(f)
        for _ in range(n): R = mmul(R, self.Mt, self.p)
        return R
    def dual(self):
        tr = lambda A: [list(r) for r in zip(*A)]
        return Module(self.B, tr(minv(self.M[X], self.p)), tr(minv(self.M[Y], self.p)), tr(minv(self.Mt, self.p)), self.p)

class Cocycle:
    """a 1-cocycle on G with values in the module V, given by its values on x, y, t"""
    def __init__(self, V, vx, vy, vt, check=True):
        self.V, self.v, self.vt = V, {X: list(vx), Y: list(vy)}, list(vt); p = V.p
        if check:                                           # t g t^-1 = Phi(g):  f(t) + t f(g) - Phi(g) f(t) = f(Phi(g))
            for g in (X, Y):
                lhs = [(a + b - c) % p for a, b, c in zip(self.vt, mvec(V.Mt, self.v[g], p), mvec(V.rhoF(V.B.Phi[g]), self.vt, p))]
                assert lhs == self.onF(V.B.Phi[g]), "not a cocycle"
    def onF(self, w):
        p = self.V.p; d = self.V.d; out = [0] * d; pre = eye(d)
        for g in w:
            if g > 0:
                out = [(a + b) % p for a, b in zip(out, mvec(pre, self.v[g], p))]; pre = mmul(pre, self.V.M[g], p)
            else:
                pre = mmul(pre, self.V.M[g], p); out = [(a - b) % p for a, b in zip(out, mvec(pre, self.v[-g], p))]
        return out
    def __call__(self, el):
        f, n = el; p = self.V.p; out = self.onF(f); pre = self.V.rhoF(f)
        for _ in range(n):
            out = [(a + b) % p for a, b in zip(out, mvec(pre, self.vt, p))]; pre = mmul(pre, self.V.Mt, p)
        return out
    def plus_coboundary(self, v):
        p = self.V.p; d = self.V.d
        dv = lambda M: [(a - b) % p for a, b in zip(mvec(M, v, p), v)]
        return Cocycle(self.V, [(a + b) % p for a, b in zip(self.v[X], dv(self.V.M[X]))],
                       [(a + b) % p for a, b in zip(self.v[Y], dv(self.V.M[Y]))],
                       [(a + b) % p for a, b in zip(self.vt, dv(self.V.Mt))])

def solve(rows, rhs, p):
    """one solution v of rows v = rhs over GF(p), or None"""
    n = len(rows[0]); R = [list(r) + [b] for r, b in zip(rows, rhs)]; piv = []; rk = 0
    for c in range(n):
        k = next((i for i in range(rk, len(R)) if R[i][c] % p), None)
        if k is None: continue
        R[rk], R[k] = R[k], R[rk]; iv = pow(R[rk][c], p - 2, p); R[rk] = [v * iv % p for v in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][c] % p:
                f = R[i][c]; R[i] = [(v - f * u) % p for v, u in zip(R[i], R[rk])]
        piv.append(c); rk += 1
    if any(r[n] % p for r in R[rk:]): return None
    v = [0] * n
    for i, c in enumerate(piv): v[c] = R[i][n]
    return v

def relative_lift(a):
    """e with a(t) = (t - 1) e and a(lam) = (lam - 1) e, or None if a does not restrict to a coboundary on P"""
    V = a.V; p = V.p; d = V.d; I = eye(d); lam = (V.B.lam, 0)
    A1 = [[(V.Mt[i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    Rl = V.rho(lam); A2 = [[(Rl[i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    return solve(A1 + A2, a(V.B.T) + a(lam), p)

def triple(B, C, z, a, b, h, T, e):
    """Y = <T(a u b u h), C> - <T(e u b u h), z>;  T(u, v, w) a trilinear functional (python callable) to GF(p)"""
    p = a.V.p; A_, B_, H_ = a.V, b.V, h.V; tot = 0
    for (g1, g2, g3), k in C.items():
        r1B = B_.rho(g1); r12H = H_.rho(B.mul(g1, g2))
        tot += k * T(a(g1), mvec(r1B, b(g2), p), mvec(r12H, h(g3), p))
    for (g1, g2), k in z.items():
        tot -= k * T(e, b(g1), mvec(H_.rho(g1), h(g2), p))
    return tot % p
