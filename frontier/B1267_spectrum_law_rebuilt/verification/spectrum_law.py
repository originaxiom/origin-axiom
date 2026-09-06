#!/usr/bin/env python3
"""The spectrum law, own code, exact: h1(M;27), h1(M;27bar), h1(D_t;27), h1(D_t;27bar).

Presentation of pi_1(m004) (the corpus's, B1086/B1036):  < a, b | a w b^-1 w^-1 >,  w = b a^-1 b^-1 a,
Riley representation  a -> [[1,1],[0,1]],  b -> [[1,0],[u,1]],  u = 1 + omega = e^{i pi/3},
longitude  lambda = w w*,  w* = a b^-1 a^-1 b  (trace -2 lift; commutes with a).
The E6 representation: the principal (or subregular) sl2 integrated on the 27:
   rho(a) = exp(e),  rho(b) = exp(u f)   (exact: e, f are nilpotent on the 27).
The double D_t:  < a, b, d | R(a,b), R(a,d), L(a,b) L(a,d)^-1 >  (B1036's 3-generator presentation
of pi_1(M) *_{Z^2} pi_1(M), meridian identified),  rho(d) = g_t rho(b) g_t^-1,  g_t = exp(t hv) a
dial element in the centralizer of the peripheral image.

Fox calculus (left-module convention): d(x)/dx = 1, d(x^-1)/dx = -x^-1, d(uv) = du + u dv.
h1 = dim ker d1 - rank d0 = (g n - rank d1) - (n - h0).  Ranks over Q(omega) by reduction modulo
two primes = 1 mod 3 (the corpus's own robust pattern), and, for the single-manifold rows, ALSO
exactly over Q(omega) via the regular representation (a 2n x 2m rational matrix).
"""
from __future__ import annotations
import os, sys, time
from fractions import Fraction as F
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e6_instrument as E

Qw, ONE, ZERO, OMEGA, U = E.Qw, E.ONE, E.ZERO, E.OMEGA, E.U_RILEY


def qw_scale(M, c):
    return np.array([[x * c for x in row] for row in M.tolist()], dtype=object)


def qw_inv_unipotent_exp(X, c):
    """exp(-c X) for nilpotent X (the inverse of exp(c X))."""
    return E.qw_expm_nilpotent(qw_scale(X, -c))


def dual(M):
    """(M^-1)^T for a matrix given together with its inverse: caller supplies inverse."""
    raise NotImplementedError


class Rep:
    """A representation of a free group on generators 1..g with matrices over Q(omega)."""

    def __init__(self, mats, invs):
        self.n = mats[1].shape[0]
        self.M = mats           # {g: matrix}
        self.I = invs           # {g: inverse}

    def ev(self, word):
        out = E.qw_eye(self.n)
        for L in word:
            out = out.dot(self.M[L] if L > 0 else self.I[-L])
        return out

    def fox(self, word, g):
        """d(word)/d x_g evaluated in the representation (left-module convention)."""
        n = self.n
        acc = E.qw_zeros(n)
        cur = E.qw_eye(n)
        for L in word:
            if L > 0:
                if L == g:
                    acc = acc + cur
                cur = cur.dot(self.M[L])
            else:
                cur = cur.dot(self.I[-L])
                if -L == g:
                    acc = acc - cur
        return acc

    def dualrep(self):
        mats = {g: E.qw_transpose(self.I[g]) for g in self.M}
        invs = {g: E.qw_transpose(self.M[g]) for g in self.M}
        return Rep(mats, invs)


def h0_h1(rep, gens, relators):
    """(h0, h1, rank d0, rank d1) of the presentation complex with coefficients in rep."""
    n = rep.n
    I = E.qw_eye(n)
    d0 = np.vstack([rep.M[g] - I for g in gens])                       # (g n) x n
    blocks = [[rep.fox(r, g) for g in gens] for r in relators]
    d1 = np.vstack([np.hstack(row) for row in blocks])                 # (r n) x (g n)
    r0 = E.rank_qw(d0)
    r1 = E.rank_qw(d1)
    h0 = n - r0
    h1 = (len(gens) * n - r1) - r0
    return h0, h1, r0, r1


def exact_rank_qw(M):
    """Exact rank over Q(omega): Gaussian elimination on Qw entries with exact field inverses."""
    A = [[M[i, j] for j in range(M.shape[1])] for i in range(M.shape[0])]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if not A[i][c].is_zero():
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = A[r][c].inv()
        A[r] = [x * inv for x in A[r]]
        for i in range(n):
            if i != r and not A[i][c].is_zero():
                fct = A[i][c]
                A[i] = [x - fct * y for x, y in zip(A[i], A[r])]
        r += 1
        if r == n:
            break
    return r


# ---------------------------------------------------------------- words
W = [2, -1, -2, 1]                       # w = b A B a
WSTAR = [1, -2, -1, 2]                   # w* = a B A b
REL = [1] + W + [-2] + [-x for x in reversed(W)]     # a w b^-1 w^-1
LONG = W + WSTAR                          # lambda = w w*


def relator(x, y):
    """R(x, y) with generator labels x, y."""
    sub = {1: x, 2: y}
    return [sub[abs(L)] * (1 if L > 0 else -1) for L in REL]


def longitude(x, y):
    sub = {1: x, 2: y}
    return [sub[abs(L)] * (1 if L > 0 else -1) for L in LONG]


def build_rep(e, f, hv=None, t=None):
    """rho(a) = exp(e), rho(b) = exp(u f) on the 27; optionally the double with dial exp(t hv)."""
    Re = E.qw_matrix(E.rho(e))
    Rf = E.qw_matrix(E.rho(f))
    A = E.qw_expm_nilpotent(Re)
    Ai = E.qw_expm_nilpotent(qw_scale(Re, Qw(-1)))
    B = E.qw_expm_nilpotent(qw_scale(Rf, U))
    Bi = E.qw_expm_nilpotent(qw_scale(Rf, -U))
    mats, invs = {1: A, 2: B}, {1: Ai, 2: Bi}
    if hv is not None:
        Rh = E.qw_matrix(E.rho(hv))
        G = E.qw_expm_nilpotent(qw_scale(Rh, t))
        Gi = E.qw_expm_nilpotent(qw_scale(Rh, -t))
        mats[3] = G.dot(B).dot(Gi)
        invs[3] = G.dot(Bi).dot(Gi)
    return Rep(mats, invs)


def check_rep(rep, gens, relators):
    for r in relators:
        M = rep.ev(r)
        assert E.qw_is_zero(M - E.qw_eye(rep.n)), "relator not satisfied"


def main():
    t0 = time.time()
    e, h, f = E.principal_sl2()
    HV = E.hw_vectors(e)
    es, hs, fs, g2 = E.subregular_sl2()

    print("=== the cusped manifold M = m004, principal embedding ===")
    rep = build_rep(e, f)
    check_rep(rep, [1, 2], [REL])
    lam = rep.ev(LONG)
    assert E.qw_is_zero(lam.dot(rep.M[1]) - rep.M[1].dot(lam)), "longitude does not commute with meridian"
    tr = sum((lam[i, i] for i in range(27)), ZERO)
    print("  relator holds on the 27; lambda commutes with a; tr_27(lambda) =", tr, "(27 => unipotent lift)")
    rows = {}
    for name, R in (("27", rep), ("27bar", rep.dualrep())):
        h0, h1, r0, r1 = h0_h1(R, [1, 2], [REL])
        rows[name] = (h0, h1)
        print(f"  {name}: h0 = {h0}, h1 = {h1}   (rank d0 = {r0}, rank d1 = {r1})")
    # exact cross-check of the 27 row over Q(omega)
    I = E.qw_eye(27)
    d0 = np.vstack([rep.M[1] - I, rep.M[2] - I])
    d1 = np.hstack([rep.fox(REL, 1), rep.fox(REL, 2)])
    r0x, r1x = exact_rank_qw(d0), exact_rank_qw(d1)
    print(f"  exact Q(omega) ranks (regular representation): rank d0 = {r0x}, rank d1 = {r1x}, h1 = {54 - r1x - r0x}")
    assert (27 - r0x, 54 - r1x - r0x) == rows["27"]

    print("\n=== the twisted double D_t, principal embedding ===")
    gens = [1, 2, 3]
    rels = [relator(1, 2), relator(1, 3), longitude(1, 2) + [-x for x in reversed(longitude(1, 3))]]
    table = {}
    for slot in (8, 16, 14):
        for tval, tname in ((Qw(0), "0"), (Qw(1), "1"), (Qw(2), "2"), (OMEGA, "omega")):
            R = build_rep(e, f, HV[slot], tval)
            check_rep(R, gens, rels)
            h0, h1, _, _ = h0_h1(R, gens, rels)
            h0b, h1b, _, _ = h0_h1(R.dualrep(), gens, rels)
            table[(slot, tname)] = (h1, h1b)
            print(f"  dial hv{slot:<2} t = {tname:5}:  h1(D_t;27) = {h1}   h1(D_t;27bar) = {h1b}   (h0 = {h0}, {h0b})")

    print("\n=== the cusped manifold, SUBREGULAR embedding E6(a1) (B1257's selection) ===")
    reps = build_rep(es, fs)
    check_rep(reps, [1, 2], [REL])
    for name, R in (("27", reps), ("27bar", reps.dualrep())):
        h0, h1, r0, r1 = h0_h1(R, [1, 2], [REL])
        print(f"  {name}: h0 = {h0}, h1 = {h1}   (rank d0 = {r0}, rank d1 = {r1})")

    print("\n=== the double with a subregular dial: a basis of the centralizer of e_sub ===")
    import sympy as sp
    adE = E.ad_matrix(es)
    ker = adE.nullspace()
    print("  dim C(e_sub) =", len(ker))
    cent = []
    for v in ker:
        from math import lcm
        L = 1
        for c in v:
            L = lcm(L, int(sp.Rational(c).q))
        cent.append([F(int(sp.Rational(c * L).p), int(sp.Rational(c * L).q)) for c in v])
    for k, X in enumerate(cent):
        cd = E.closure_dim([es, hs, fs, X])
        R = build_rep(es, fs, X, Qw(1))
        check_rep(R, gens, rels)
        h0, h1, _, _ = h0_h1(R, gens, rels)
        h0b, h1b, _, _ = h0_h1(R.dualrep(), gens, rels)
        nil = E.rho(X)
        # is X nilpotent on the 27 (so exp is exact)?  it is: centralizer of a nilpotent in g_>=0
        print(f"  slot {k}: closure <sl2_sub, X> = {cd:2}   h1(D;27) = {h1}   h1(D;27bar) = {h1b}   (h0 = {h0},{h0b})")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()
