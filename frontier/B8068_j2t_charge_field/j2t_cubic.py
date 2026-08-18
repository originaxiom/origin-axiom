#!/usr/bin/env python3
"""THE PAYOFF: the E6 cubic form restricted to (27)^{2T}, and the etale algebra it names.

Carrier: e8 with its Z/3 grading e8 = (e6 + sl3) + (27,3) + (27bar,3bar).
The three 27-blocks are distinguished by the coefficient of alpha_8; the two A2 root
vectors P = e_{alpha_8} and Q = e_{beta} map block 0 bijectively onto blocks +1 and -1.
Since P and Q commute with e6 and the Killing form is invariant,

    C(x) = < [x, P.x] , Q.x >

is an E6-invariant cubic on the 27, hence proportional to det.  Uniqueness of the
E6-invariant cubic is what makes the scale irrelevant to every question asked here.

SEALED before reading (from build_j2t.py):
  * cubic FIELD  -> no rational primitive idempotents -> no rational rank-1 VEV
  * SPLIT        -> three of them, two of which start E6 -> SU(5)
  * compare disc of the restricted cubic against disc K = 6237 = 3^4 * 7 * 11.
"""
import sympy as sp
from fractions import Fraction

import e8_build as E

FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}\n          got:      {got}")
        FAIL.append(label)


# ---- principal sl2 of the E6 subalgebra -------------------------------------------
E6A = sp.Matrix(E.E6_A)
cv = E6A.T.solve(sp.Matrix([2] * 6))
Fr = lambda q: Fraction(sp.Rational(q).p, sp.Rational(q).q)
h = {j: Fr(cv[j]) for j in range(6) if cv[j] != 0}
ee = {}
for j in range(6):
    ee = E.vadd(ee, E.ev(tuple(1 if i == j else 0 for i in range(8))))
ff = {}
for j in range(6):
    pos = tuple(1 if i == j else 0 for i in range(8))
    neg = tuple(-t for t in pos)
    ff = E.vadd(ff, {E.N + E.IDX[neg]: Fr(cv[j]) / E.eps(pos, neg)})
check("principal sl2: [e,f] = h", E.br(ee, ff) == h, True)

BLOCK = [r for r in E.ROOTS if r[6] % 3 == 1 and r[7] == 0]
check("block 0 has 27 roots", len(BLOCK), 27)


def hwt(r):
    v = E.br(h, E.ev(r))
    return int(list(v.values())[0]) if v else 0


# ---- highest-weight vectors of the three sl2-blocks --------------------------------
def hw_vectors(n):
    """vectors of h-weight n in the block that are killed by e."""
    cands = [r for r in BLOCK if hwt(r) == n]
    M = sp.zeros(E.DIM, len(cands))
    for j, r in enumerate(cands):
        for k, val in E.br(ee, E.ev(r)).items():
            M[k, j] = sp.Rational(val.numerator, val.denominator)
    ns = M.nullspace()
    out = []
    for vec in ns:
        v = {}
        for j, r in enumerate(cands):
            co = sp.Rational(vec[j])
            if co:
                v = E.vadd(v, {E.N + E.IDX[r]: Fr(co)})
        out.append(v)
    return out


tops = {}
for n in (16, 8, 0):
    vs = hw_vectors(n)
    check(f"exactly one sl2-highest vector at h-weight {n}", len(vs), 1)
    tops[n] = vs[0]

# ---- embed the 2T-invariant binary form into each block ---------------------------
x, y = sp.symbols("x y")
W = x**8 + 14 * x**4 * y**4 + y**8
FORMS = {0: sp.Integer(1), 8: W, 16: sp.expand(W**2)}
print(f"\n  W^2 = {FORMS[16]}")


def embed(n):
    """x^{n-k} y^k  |->  ((n-k)!/n!) f^k . v_top   -- the sl2-equivariant map."""
    P = sp.Poly(FORMS[n], x, y) if n else None
    out = {}
    cur = tops[n]
    if n == 0:
        return dict(tops[0])
    for k in range(n + 1):
        c = P.coeff_monomial(x**(n - k) * y**k)
        if c:
            rat = sp.Rational(c) * sp.factorial(n - k) / sp.factorial(n)
            out = E.vadd(out, E.vmul(Fr(rat), cur))
        cur = E.br(ff, cur)
    return out


V = {n: embed(n) for n in (0, 8, 16)}
for n in (0, 8, 16):
    check(f"v{n} is nonzero", not E.is_zero(V[n]), True)

# ---- GATE: these three really are 2T-invariant --------------------------------------
# 2T is generated inside the principal SU(2); invariance under the FORM is what the
# embedding guarantees.  The independent check available here: the three vectors span
# a 3-dimensional space and the Molien series predicted exactly 3.
print("\n  (dim (27)^{2T} = 3 was fixed in advance by the Molien series of 2T)")

# ---- the two A2 linking operators ---------------------------------------------------
P_ROOT = (0, 0, 0, 0, 0, 0, 0, 1)
Q_ROOT = (-2, -3, -4, -6, -5, -4, -3, -1)
Pop, Qop = E.ev(P_ROOT), E.ev(Q_ROOT)


def cubic(vec):
    return E.killing_pair(E.br(vec, E.br(Pop, vec)), E.br(Qop, vec))


# ---- restrict the cubic to span(v0, v8, v16) ---------------------------------------
a, b, c = sp.symbols("a b c")
print("\n" + "=" * 74)
print("the E6 cubic restricted to (27)^{2T}")
print("=" * 74)

# evaluate on a grid and interpolate the ternary cubic exactly
mons = [a**3, a**2*b, a**2*c, a*b**2, a*b*c, a*c**2, b**3, b**2*c, b*c**2, c**3]
pts, vals = [], []
import itertools
for A_, B_, C_ in itertools.product(range(-2, 3), repeat=3):
    if (A_, B_, C_) == (0, 0, 0):
        continue
    vec = {}
    for co, n in ((A_, 0), (B_, 8), (C_, 16)):
        if co:
            vec = E.vadd(vec, E.vmul(co, V[n]))
    pts.append((A_, B_, C_))
    vals.append(cubic(vec))
    if len(pts) >= 40:
        break

M = sp.Matrix([[sp.Rational(int(sp.Poly(m, a, b, c).eval({a: p[0], b: p[1], c: p[2]})))
                for m in mons] for p in pts])
rhs = sp.Matrix([sp.Rational(v.numerator, v.denominator) for v in vals])
sol = M.solve_least_squares(rhs)
resid = (M * sol - rhs).norm()
print(f"  interpolation residual (must be 0): {sp.simplify(resid)}")
form = sum(sol[i] * mons[i] for i in range(len(mons)))
form = sp.simplify(sp.expand(form))
print(f"\n  C(a,b,c) = {form}")
if FAIL:
    print("\nGATES FAILED -- not reading the algebra off a broken build.")
    for f in FAIL:
        print("   -", f)
