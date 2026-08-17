#!/usr/bin/env python3
"""B1068 CELL 3 -- does the object reach su(5)?  The computation cell 2 should have been.

Cell 2 was withdrawn after four errors, every one of which pointed the same way (toward
"no").  This cell is built so that the specific failures that produced them cannot recur
silently:

  * the CONTROL RUNS FIRST, in this same script.  27 (+) 27-bar with rank-1 weight
    vectors must reproduce  dim 45, Killing rank 24 = su(5).  If it does not, the
    instrument is wrong and nothing else is read.  Cell 2 never validated against a
    known answer.
  * every candidate idempotent is GATED ON RANK 1 (stabiliser dimension 61) before it
    is used.  That is exactly the check that exposed cell 2's fourth error, and it now
    runs before, not after.
  * the 27-bar's OWN cubic is computed.  Cell 2 reused the 27's coordinates, which is
    what produced rank-3 vectors on the bar side.
  * reductive parts come from the KILLING FORM RANK, never from a dimension alone.
    dim 44 fits both so(8)+16 and su(5)+20; dimension does not identify a type.

The question: the 27 supplies three 2T-invariant primitive idempotents (cell 1), and the
27-bar supplies its own.  Does a pair, one from each, have reductive stabiliser su(5)?
"""
import pathlib
import sys

import numpy as np
import sympy as sp
from fractions import Fraction

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import e8_build as E

P = 1093
FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {got}" + ("" if ok else f"   (want {want})"))
    if not ok:
        FAIL.append(label)


Fr = lambda q: Fraction(sp.Rational(q).p, sp.Rational(q).q)

# ---- e6 and the three graded blocks ------------------------------------------------
E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
E6_BASIS = [{i: Fraction(1)} for i in range(6)] + [E.ev(r) for r in E6_ROOTS]
BLK = {k: [r for r in E.ROOTS if r[6] % 3 == 1 and r[7] == k] for k in (-1, 0, 1)}
BAR = {k: [r for r in E.ROOTS if r[6] % 3 == 2 and r[7] == k] for k in (-1, 0, 1)}
TWENTYSEVEN, TWENTYSEVENBAR = BLK[0], BAR[0]
IDX27 = {r: i for i, r in enumerate(TWENTYSEVEN)}
IDXBAR = {r: i for i, r in enumerate(TWENTYSEVENBAR)}

print("carrier")
check("e6 dimension", len(E6_BASIS), 78)
check("the 27", len(TWENTYSEVEN), 27)
check("the 27-bar", len(TWENTYSEVENBAR), 27)


def act(vec, tgt_idx, p=P):
    cols = []
    for Xb in E6_BASIS:
        img = E.br(Xb, vec)
        col = [0] * 27
        for k, val in img.items():
            r = E.ROOTS[k - E.N]
            col[tgt_idx[r]] = (val.numerator % p) * pow(val.denominator % p, p - 2, p) % p
        cols.append(col)
    return np.array(cols, dtype=np.int64).T % p


def rank_mod_p(M, p=P):
    M = M.copy() % p
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if M[i, c]), None)
        if pr is None:
            continue
        M[[r, pr]] = M[[pr, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p - 2, p)) % p
        col = M[r + 1:, c].copy()
        nz = np.nonzero(col)[0]
        if nz.size:
            M[r + 1:][nz] = (M[r + 1:][nz] - np.outer(col[nz], M[r])) % p
        r += 1
        if r == rows:
            break
    return r


def nullspace(M, p=P):
    M = M.copy() % p
    rows, cols = M.shape
    piv, r = [], 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if M[i, c]), None)
        if pr is None:
            continue
        M[[r, pr]] = M[[pr, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p - 2, p)) % p
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] = (M[i] - M[i, c] * M[r]) % p
        piv.append(c)
        r += 1
    out = []
    for fc in [c for c in range(cols) if c not in piv]:
        v = [0] * cols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i, fc]) % p
        out.append(v)
    return out


def reductive_dim(M, p=P):
    """dim and Killing rank of the annihilator of the stacked action matrix."""
    ns = nullspace(M, p)
    elts = []
    for v in ns:
        xx = {}
        for co, Xb in zip(v, E6_BASIS):
            if co % p:
                xx = E.vadd(xx, E.vmul(Fraction(int(co) % p), Xb))
        elts.append(xx)
    K = np.zeros((len(elts), len(elts)), dtype=np.int64)
    for i, xi in enumerate(elts):
        for j, xj in enumerate(elts):
            kv = E.killing_pair(xi, xj)
            K[i, j] = (kv.numerator % p) * pow(kv.denominator % p, p - 2, p) % p
    return len(ns), rank_mod_p(K, p)


# ================= THE CONTROL, RUN FIRST =========================================
print("\n" + "=" * 74)
print("CONTROL -- validate the instrument on a KNOWN answer before reading any new one")
print("=" * 74)
m27 = {r: act(E.ev(r), IDX27) for r in TWENTYSEVEN}
mbar = {r: act(E.ev(r), IDXBAR) for r in TWENTYSEVENBAR}
check("single 27 weight vectors are rank 1 (stab 61)",
      {78 - rank_mod_p(m27[r]) for r in TWENTYSEVEN}, {61})
check("single 27-bar weight vectors are rank 1 (stab 61)",
      {78 - rank_mod_p(mbar[r]) for r in TWENTYSEVENBAR}, {61})
best = None
for r1 in TWENTYSEVEN:
    for r2 in TWENTYSEVENBAR:
        d = 78 - rank_mod_p(np.vstack([m27[r1], mbar[r2]]) % P)
        if best is None or d < best[0]:
            best = (d, r1, r2)
d, r1, r2 = best
dim, kr = reductive_dim(np.vstack([m27[r1], mbar[r2]]) % P)
check("generic 27 x 27-bar stabiliser dimension", dim, 45)
check("its Killing rank identifies su(5)", kr, 24)
if FAIL:
    print("\nCONTROL FAILED -- instrument not trusted, nothing further is read.")
    sys.exit(1)
print("  CONTROL PASSED: the instrument reproduces su(5) where su(5) is known to be.")

# ================= the 27-bar's OWN cubic =========================================
print("\n" + "=" * 74)
print("the 27-bar's OWN invariants and OWN cubic (cell 2 reused the 27's -- the bug)")
print("=" * 74)
E6A = sp.Matrix(E.E6_A)
cv = E6A.T.solve(sp.Matrix([2] * 6))
h = {j: Fr(cv[j]) for j in range(6) if cv[j] != 0}
ee = {}
for j in range(6):
    ee = E.vadd(ee, E.ev(tuple(1 if i == j else 0 for i in range(8))))
ff = {}
for j in range(6):
    pos = tuple(1 if i == j else 0 for i in range(8)); neg = tuple(-t for t in pos)
    ff = E.vadd(ff, {E.N + E.IDX[neg]: Fr(cv[j]) / E.eps(pos, neg)})
x, y = sp.symbols("x y")
W = x**8 + 14 * x**4 * y**4 + y**8
FORMS = {0: sp.Integer(1), 8: W, 16: sp.expand(W**2)}


def invariants(block):
    def hw(n):
        cands = [r for r in block
                 if int(list(E.br(h, E.ev(r)).values())[0] if E.br(h, E.ev(r)) else 0) == n]
        M = sp.zeros(E.DIM, len(cands))
        for j, r in enumerate(cands):
            for k, val in E.br(ee, E.ev(r)).items():
                M[k, j] = sp.Rational(val.numerator, val.denominator)
        ns = M.nullspace(); v = {}
        for j, r in enumerate(cands):
            co = sp.Rational(ns[0][j])
            if co:
                v = E.vadd(v, {E.N + E.IDX[r]: Fr(co)})
        return v
    out = {}
    for n in (0, 8, 16):
        if n == 0:
            out[0] = hw(0); continue
        Pp = sp.Poly(FORMS[n], x, y); acc, cur = {}, hw(n)
        for k in range(n + 1):
            co = Pp.coeff_monomial(x**(n - k) * y**k)
            if co:
                acc = E.vadd(acc, E.vmul(
                    Fr(sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n)), cur))
            cur = E.br(ff, cur)
        out[n] = acc
    return out


V27, VBAR = invariants(TWENTYSEVEN), invariants(TWENTYSEVENBAR)
check("27-bar invariants all nonzero", all(VBAR[n] for n in VBAR), True)

# the bar cubic, via the A2 operators that link the BAR blocks
Pop = E.ev((0, 0, 0, 0, 0, 0, 0, 1))
Qop = E.ev((-2, -3, -4, -6, -5, -4, -3, -1))


def cubic_of(vec):
    return E.killing_pair(E.br(vec, E.br(Pop, vec)), E.br(Qop, vec))


import itertools
a, b, c = sp.symbols("a b c")
mons = [a**3, a**2*b, a**2*c, a*b**2, a*b*c, a*c**2, b**3, b**2*c, b*c**2, c**3]


def restricted_cubic(Vd):
    pts, vals = [], []
    for A_, B_, C_ in itertools.product(range(-2, 3), repeat=3):
        if (A_, B_, C_) == (0, 0, 0):
            continue
        vec = {}
        for co, n in ((A_, 0), (B_, 8), (C_, 16)):
            if co:
                vec = E.vadd(vec, E.vmul(co, Vd[n]))
        pts.append((A_, B_, C_)); vals.append(cubic_of(vec))
        if len(pts) >= 40:
            break
    M = sp.Matrix([[sp.Rational(int(sp.Poly(m, a, b, c).eval({a: p[0], b: p[1], c: p[2]})))
                    for m in mons] for p in pts])
    rhs = sp.Matrix([sp.Rational(v.numerator, v.denominator) for v in vals])
    sol = M.solve_least_squares(rhs)
    resid = sp.simplify((M * sol - rhs).norm())
    return sp.expand(sum(sol[i] * mons[i] for i in range(len(mons)))), resid


CBAR, res = restricted_cubic(VBAR)
check("bar cubic interpolation residual is 0", res, 0)
pb = sp.Poly(CBAR, a, b, c)
check("bar cubic has no a^2b / a^2c / abc terms (the shape prediction)",
      (pb.coeff_monomial(a**2*b), pb.coeff_monomial(a**2*c), pb.coeff_monomial(a*b*c)),
      (0, 0, 0))
lead = pb.coeff_monomial(a**3)
DBAR = sp.expand(CBAR / lead)
print(f"\n  det_bar(a,b,c) = {DBAR}")
s2b, s3b = sp.expand(DBAR.coeff(a, 1)), sp.expand(DBAR.coeff(a, 0))
fbar = sp.Symbol('L')**3 + s2b.subs({b: 1, c: 0}) * sp.Symbol('L') - s3b.subs({b: 1, c: 0})
dfb = sp.discriminant(sp.Poly(fbar, sp.Symbol('L')))
sf = 1
for pr, e in sp.factorint(sp.Rational(dfb).p * sp.Rational(dfb).q).items():
    if e % 2:
        sf *= pr
print(f"  the bar side's cubic field: square-free disc part = {sf}   (the 27's is 77)")
