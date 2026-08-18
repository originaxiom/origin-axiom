#!/usr/bin/env python3
"""B8068 CELL 2 -- what do the object's own idempotents actually stabilise?

The question this cell exists to answer, and it is NOT the one the L138 lead assumes.

The standard route is  E6 -> SU(5) via TWO Jordan-rank-1 VEVs.  But that result is for
two rank-1 elements in GENERAL POSITION.  The two the object supplies are not in general
position: they are two members of an ORTHOGONAL FRAME (cell 1 showed e1 + e2 + e3 = 1
exactly).  Whether a frame pair is a general-position pair is a question, not a given,
and the whole physics reading turns on it.

METHOD.  The joint stabiliser's Lie algebra is the annihilator

    { X in e6 : X . u = 0 }

which is a linear condition, so its dimension is a rank computation.  e6 is realised as
the c7 = c8 = 0 part of the e8 carrier (78 = 6 Cartan + 72 roots), acting on the 27-block
by the e8 bracket.  Everything is done mod a prime at which the idempotent coordinates
split, so the arithmetic is exact.

SEALED BEFORE READING, since dimension alone identifies the answer:

    dim Stab(one rank-1 element)  MUST be 61 = dim so(10) + 16.
        -> this is the GATE.  A rank-1 element has a 61-dimensional stabiliser in e6
           (the 17-dim cone, 78 - 17 = 61).  If the gate misses, the instrument is
           wrong and nothing below is read.

    then, for the PAIR:
        24 or 25  ->  su(5) (+ u(1)):  the standard route, chirality can survive
        28        ->  so(8):           right rank, but ALL so(8) reps are self-dual
                                       (-1 is in W(D4)), so the 27 goes REAL and
                                       chirality dies -- the same trade-off met by the
                                       theta-split, the tau-fold and the F4 VEV
        45 / 52   ->  so(10) / f4:     rank too high, or achiral
        anything else -> reported as found, with no story attached
"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])

import numpy as np
import sympy as sp
from fractions import Fraction

import e8_build as E

P = 1093                       # the b-coordinate cubic splits here
XX = sp.Symbol("X")
MB = 734743166976 * XX**3 - 73008 * XX + 7

FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {got}" + ("" if ok else f"  (want {want})"))
    if not ok:
        FAIL.append(label)


# ---- e6 inside e8: the c7 = c8 = 0 part -------------------------------------------
E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
BLOCK = [r for r in E.ROOTS if r[6] % 3 == 1 and r[7] == 0]
BIDX = {r: i for i, r in enumerate(BLOCK)}
print("carrier gates")
check("E6 roots inside e8", len(E6_ROOTS), 72)
check("dim e6 = 6 + 72", 6 + len(E6_ROOTS), 78)
check("the 27-block", len(BLOCK), 27)

# e6 basis: 6 Cartan directions (the E6 nodes) + the 72 root vectors
E6_BASIS = [{i: Fraction(1)} for i in range(6)] + [E.ev(r) for r in E6_ROOTS]
check("e6 basis size", len(E6_BASIS), 78)


def act_matrix_mod_p(vec_in_block, p):
    """columns: the action of each e6 basis element on the given block vector."""
    cols = []
    for Xb in E6_BASIS:
        img = E.br(Xb, vec_in_block)
        col = [0] * 27
        for k, val in img.items():
            if k < E.N:
                raise AssertionError("action left the block into the Cartan")
            r = E.ROOTS[k - E.N]
            if r not in BIDX:
                raise AssertionError("action left the 27-block")
            num, den = val.numerator, val.denominator
            col[BIDX[r]] = (num % p) * pow(den % p, p - 2, p) % p
        cols.append(col)
    return np.array(cols, dtype=np.int64).T % p          # 27 x 78


def rank_mod_p(M, p):
    M = M.copy() % p
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p - 2, p)) % p
        col = M[r + 1:, c].copy()
        nz = np.nonzero(col)[0]
        if nz.size:
            M[r + 1:][nz] = (M[r + 1:][nz] - np.outer(col[nz], M[r])) % p
        r += 1
        if r == rows:
            break
    return r


# ---- the three invariant directions, as block vectors -----------------------------
E6A = sp.Matrix(E.E6_A)
cv = E6A.T.solve(sp.Matrix([2] * 6))
Fr = lambda q: Fraction(sp.Rational(q).p, sp.Rational(q).q)
h = {j: Fr(cv[j]) for j in range(6) if cv[j] != 0}
ee = {}
for j in range(6):
    ee = E.vadd(ee, E.ev(tuple(1 if i == j else 0 for i in range(8))))
ff = {}
for j in range(6):
    pos = tuple(1 if i == j else 0 for i in range(8)); neg = tuple(-t for t in pos)
    ff = E.vadd(ff, {E.N + E.IDX[neg]: Fr(cv[j]) / E.eps(pos, neg)})


def hw_vec(n):
    cands = [r for r in BLOCK
             if int(list(E.br(h, E.ev(r)).values())[0] if E.br(h, E.ev(r)) else 0) == n]
    M = sp.zeros(E.DIM, len(cands))
    for j, r in enumerate(cands):
        for k, val in E.br(ee, E.ev(r)).items():
            M[k, j] = sp.Rational(val.numerator, val.denominator)
    ns = M.nullspace()
    v = {}
    for j, r in enumerate(cands):
        co = sp.Rational(ns[0][j])
        if co:
            v = E.vadd(v, {E.N + E.IDX[r]: Fr(co)})
    return v


x, y = sp.symbols("x y")
W = x**8 + 14 * x**4 * y**4 + y**8
FORMS = {0: sp.Integer(1), 8: W, 16: sp.expand(W**2)}


def embed(n):
    if n == 0:
        return hw_vec(0)
    Pp = sp.Poly(FORMS[n], x, y)
    out, cur = {}, hw_vec(n)
    for k in range(n + 1):
        co = Pp.coeff_monomial(x**(n - k) * y**k)
        if co:
            rat = sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n)
            out = E.vadd(out, E.vmul(Fr(rat), cur))
        cur = E.br(ff, cur)
    return out


V = {n: embed(n) for n in (0, 8, 16)}

# ---- the idempotents mod p ---------------------------------------------------------
a_, b_, c_ = sp.symbols("a b c")
DET = (a_**3 - 2515968*a_*b_**2 - sp.Rational(10300450406400, 13)*a_*c_**2
       - 1213857792*b_**3 + sp.Rational(20600900812800, 13)*b_**2*c_
       + sp.Rational(193813274846822400, 169)*b_*c_**2
       - sp.Rational(365476461139722240000, 2197)*c_**3)
S2 = sp.expand(DET.coeff(a_, 1)); S3 = sp.expand(DET.coeff(a_, 0))

def red_mod_p(expr, var, p):
    """reduce a rational-coefficient univariate polynomial mod p, exactly."""
    poly = sp.Poly(sp.expand(expr), var)
    out = 0
    for (k,), co in poly.terms():
        r = sp.Rational(co)
        cf = (r.p % p) * pow(r.q % p, p - 2, p) % p
        out += cf * var**k
    return sp.Poly(out, var, modulus=p)


bs = sorted(int(r) % P for r in sp.ground_roots(MB, modulus=P))
IDEM = []
for bv in bs:
    q2 = red_mod_p(S2.subs(b_, bv) + sp.Rational(1, 3), c_, P)
    q3 = red_mod_p(S3.subs(b_, bv) - sp.Rational(2, 27), c_, P)
    common = sp.gcd(q2, q3)
    rts = sp.ground_roots(common.as_expr(), modulus=P) if common.degree() >= 1 else {}
    for cval in rts:
        IDEM.append((bv, int(cval) % P))
print(f"\nidempotents found mod {P}: {len(IDEM)}  -> {IDEM}")


def block_vec_mod_p(a, b, c, p):
    out = {}
    for co, n in ((a, 0), (b, 8), (c, 16)):
        out = E.vadd(out, E.vmul(Fraction(int(co) % p), V[n]))
    return out


inv3 = pow(3, P - 2, P)
print("\nGATE: a single idempotent is rank 1, so its stabiliser must be 61-dimensional")
dims = []
mats = []
for (bv, cv2) in IDEM:
    u = block_vec_mod_p(inv3, bv, cv2, P)
    M = act_matrix_mod_p(u, P)
    d = 78 - rank_mod_p(M, P)
    dims.append(d); mats.append(M)
    print(f"   e(b={bv}): dim Stab = {d}")
check("every single-idempotent stabiliser is 61-dimensional", set(dims), {61})

if not FAIL:
    print("\nTHE PAIR -- the reading the whole physics question turns on")
    import itertools
    for i, j in itertools.combinations(range(len(IDEM)), 2):
        M = np.vstack([mats[i], mats[j]]) % P
        d = 78 - rank_mod_p(M, P)
        print(f"   Stab(e_{i+1}, e_{j+1}) has dimension {d}")
    M3 = np.vstack(mats) % P
    print(f"   Stab(all three)          has dimension {78 - rank_mod_p(M3, P)}")
    print("\n   reference dims:  su(5) 24 · su(5)+u(1) 25 · so(8) 28 · so(10) 45 · f4 52")
