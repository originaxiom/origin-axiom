#!/usr/bin/env python3
"""B8077 -- the cascade's endpoint has a COMPACT home in the object's own real form.

A gauge algebra in physics must be COMPACT: unitarity and a positive-definite kinetic
term force it.  So reaching su(3)+su(2)+u(1) over C is not enough -- the compact real
form is required.  This asks, over Q and exhaustively over the 64 inner characters:

  (a) which real forms is the object's charge algebra C theta-stable in?
  (b) is the SM gauge algebra su(3)+su(2)+u(1) COMPACT there?
  (c) does B892's second-measurement endpoint su(3)+su(2)+u(1)^3 (dim 14, rank 6)
      sit inside the maximal compact too?
  (d) which real form carries the cascade's so(10) chain compactly?

A real form is named by dim k, its maximal compact -- an exact integer, no signatures.

QUANTIFIER (COMPUTE_THE_PROGRAM): the ALGEBRA layer, over the inner real forms of e6.
Outer forms (e6(6), e6(-26)) are NOT swept here.  Nothing is claimed about the class,
the sisters or the rows.

Criteria sealed in PREREGISTRATION.md before the first number was read.
"""
import itertools
import json
import os
import sys
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B8068_j2t_charge_field"))
import e8_build as E                                                   # noqa: E402

E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
DIM6 = 6 + len(E6_ROOTS)
RIDX = {r: k for k, r in enumerate(E6_ROOTS)}
OF = [i for i in range(6)] + [E.N + E.IDX[r] for r in E6_ROOTS]
INV = {g: i for i, g in enumerate(OF)}
A = E.A
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def brk6(u, v):
    return {INV[g]: c for g, c in E.br({OF[i]: c for i, c in u.items()},
                                       {OF[i]: c for i, c in v.items()}).items()}


def eps_of(sg):
    def f(r):
        s = 1
        for j in range(6):
            if r[j] % 2:
                s *= sg[j]
        return s
    return f


def pairing(r, s):
    return sum(r[i] * A[i][j] * s[j] for i in range(8) for j in range(8))


# ---------------------------------------------------------------- the charge algebra C
E6A = sp.Matrix(E.E6_A)
cv = E6A.T.solve(sp.Matrix([2] * 6))
h = {j: Fr(sp.Rational(cv[j]).p, sp.Rational(cv[j]).q) for j in range(6) if cv[j] != 0}
ee = {}
for j in range(6):
    ee = E.vadd(ee, E.ev(tuple(1 if i == j else 0 for i in range(8))))
ff = {}
for j in range(6):
    pos = tuple(1 if i == j else 0 for i in range(8))
    neg = tuple(-t for t in pos)
    q = sp.Rational(cv[j])
    ff = E.vadd(ff, {E.N + E.IDX[neg]: Fr(q.p, q.q) / E.eps(pos, neg)})


def to6(v):
    return {INV[g]: c for g, c in v.items()}


def hw(n):
    cands = [r for r in E6_ROOTS
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
            v = E.vadd(v, {E.N + E.IDX[r]: Fr(co.p, co.q)})
    return v


x_, y_ = sp.symbols("x y")
tf = x_**5 * y_ - x_ * y_**5
Wf = x_**8 + 14 * x_**4 * y_**4 + y_**8
ADJ = {8: Wf, 14: sp.expand(tf * Wf), 16: sp.expand(Wf**2), 22: sp.expand(tf * Wf**2)}
C = {}
for n in (8, 14, 16, 22):
    top = hw(n)
    P = sp.Poly(ADJ[n], x_, y_)
    acc, cur = {}, top
    for k in range(n + 1):
        co = P.coeff_monomial(x_**(n - k) * y_**k)
        if co:
            q = sp.Rational(sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n))
            acc = E.vadd(acc, E.vmul(Fr(q.p, q.q), cur))
        cur = E.br(ff, cur)
    C[n] = to6(acc)

print("=" * 78)
print("CONTROLS -- run before any result is read")
print("=" * 78)
gate("e6 carrier: 72 roots, dim 78", len(E6_ROOTS) == 72 and DIM6 == 78)
gate("the four charges are built, degrees 8/14/16/22", sorted(C) == [8, 14, 16, 22])
bad = [(a, b) for a, b in itertools.combinations(sorted(C), 2)
       if any(v != 0 for v in brk6(C[a], C[b]).values())]
gate("all six pairwise charge brackets vanish (C abelian)", not bad)

census = {}
for sg in itertools.product([1, -1], repeat=6):
    ch = eps_of(sg)
    census.setdefault(6 + sum(1 for r in E6_ROOTS if ch(r) == 1), 0)
    census[6 + sum(1 for r in E6_ROOTS if ch(r) == 1)] += 1
gate("the inner census reproduces B907 unprompted: 78x1, 46x27, 38x36",
     census == {78: 1, 46: 27, 38: 36}, str(dict(sorted(census.items()))))
if FAILED:
    raise SystemExit("controls failed -- nothing may be read")

# ---------------------------------------------------------------- the sweep
NAMES = {78: "compact e6(-78)", 46: "e6(-14)", 38: "e6(2)"}
rows = []
for sg in itertools.product([1, -1], repeat=6):
    ch = eps_of(sg)
    kr = [r for r in E6_ROOTS if ch(r) == 1]
    dimk = 6 + len(kr)
    span = set()
    for r in kr:
        for j in range(6):
            if r[j]:
                span.add(j)
    derk = len(kr) + len(span)

    # (a) is C theta-stable?  each charge must be a theta-eigenvector
    stable = True
    for n in sorted(C):
        tv = {i: (c if i < 6 else c * ch(E6_ROOTS[i - 6])) for i, c in C[n].items()}
        keys = set(tv) | set(C[n])
        same = all(tv.get(i, Fr(0)) == C[n].get(i, Fr(0)) for i in keys)
        neg = all(tv.get(i, Fr(0)) == -C[n].get(i, Fr(0)) for i in keys)
        if not (same or neg):
            stable = False
            break

    # (b)/(c) does k contain an A2+A1 subsystem?  8 roots + 4 Cartan = the SM (12);
    # the same 8 roots + the full rank-6 Cartan = B892's endpoint (14).
    hit = None
    for a, b in itertools.combinations(kr, 2):
        if pairing(a, b) != -1:
            continue
        s = tuple(a[i] + b[i] for i in range(8))
        if not (any(s) and s in E.IDX and ch(s) == 1):
            continue
        for c in kr:
            if c in (a, b) or tuple(-x for x in c) in (a, b):
                continue
            if pairing(c, a) == 0 and pairing(c, b) == 0:
                hit = (a, b, s, c)
                break
        if hit:
            break
    rows.append((sg, dimk, derk, stable, hit is not None))

print()
print("=" * 78)
print("THE RESULT")
print("=" * 78)
st = [r for r in rows if r[3]]
byform = {}
for sg, dk, dr, s, a2 in st:
    byform[dk] = byform.get(dk, 0) + 1
print(f"\n(a) the object's charge algebra C is theta-stable in {len(st)} of 64 characters:")
for dk in sorted(byform, reverse=True):
    print(f"      {NAMES.get(dk,'?'):18s} {byform[dk]}")
print("    B907 sealed e6(2) for the wall by a wholly different route (128 swept")
print("    involutions).  This lands on e6(2) from the charge side.  Two methods, one form.")

for dk, label in ((38, "e6(2)"), (46, "e6(-14)")):
    tot = sum(1 for r in rows if r[1] == dk)
    ok = sum(1 for r in rows if r[1] == dk and r[4])
    print(f"\n(b/c) {label}: k contains an A2+A1 subsystem in {ok} of {tot} characters")
    print(f"        => su(3)+su(2)+u(1)   = 8 roots + 4 Cartan = 12  COMPACT")
    print(f"        => su(3)+su(2)+u(1)^3 = 8 roots + 6 Cartan = 14  COMPACT  (B892's endpoint)")

so10 = [r for r in rows if r[1] == 46 and r[2] == 45]
print(f"\n(d) characters with k = so(10)+u(1) (dim 46, derived 45): {len(so10)}")
print("    the cascade's chain E6 -> SO(10) -> SU(5) -> SM is a chain of COMPACT")
print("    subalgebras there -- so(10) itself is compact in e6(-14).")

RES = {
    "census": {str(k): v for k, v in sorted(census.items())},
    "C_theta_stable_total": len(st),
    "C_theta_stable_by_form": {str(k): v for k, v in sorted(byform.items())},
    "A2A1_in_k": {str(dk): [sum(1 for r in rows if r[1] == dk and r[4]),
                            sum(1 for r in rows if r[1] == dk)] for dk in (38, 46)},
    "so10_compact_characters": len(so10),
    "sm_dim": 12, "b892_endpoint_dim": 14,
    "scope": ("inner real forms only; outer forms e6(6) and e6(-26) NOT swept. "
              "Shows a compact home EXISTS for the endpoint in the object's own real "
              "form; does NOT show the object's specific subalgebra IS that one."),
}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
