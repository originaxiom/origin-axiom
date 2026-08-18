#!/usr/bin/env python3
"""B1075 -- is the paper's fourteen-value rung spectrum ATTAINED?

An external referee reports that Theorem 10.23 mistakes an ambient superset for a realized
spectrum: centralizers are order-reversing, so S subset C implies z(C) subset z(S), and if
dim z(C) = 12 then EVERY dim z(S) >= 12, making the advertised values 6, 8 and 10
impossible.

This checks that in-sandbox, exactly over Q, using the paper's own charge construction
(the 2T-invariant adjoint forms W, tW, W^2, tW^2 of degrees 8, 14, 16, 22 embedded through
the principal sl2), and then computes the ACTUAL set {dim z(S)} over all subsets.
"""
import itertools
import json
import os
import sys
from fractions import Fraction as Fr

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "B1068_j2t_charge_field"))
import e8_build as E                                                   # noqa: E402

E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
DIM6 = 6 + len(E6_ROOTS)
RIDX = {r: k for k, r in enumerate(E6_ROOTS)}
OF = [i for i in range(6)] + [E.N + E.IDX[r] for r in E6_ROOTS]
INV = {g: i for i, g in enumerate(OF)}
BAS = [{i: Fr(1)} for i in range(DIM6)]

FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def brk6(u, v):
    out = {}
    for g, c in E.br({OF[i]: c for i, c in u.items()},
                     {OF[i]: c for i, c in v.items()}).items():
        if g not in INV:
            raise ValueError("bracket left e6")
        out[INV[g]] = c
    return out


def rank_rows(rows):
    rows = [list(map(Fr, r)) for r in rows]
    n = len(rows[0]) if rows else 0
    piv = 0
    for c in range(n):
        pr = next((r for r in range(piv, len(rows)) if rows[r][c] != 0), None)
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        pv = rows[piv][c]
        rows[piv] = [v / pv for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] != 0:
                fq = rows[r][c]
                rows[r] = [a - fq * b for a, b in zip(rows[r], rows[piv])]
        piv += 1
        if piv == len(rows):
            break
    return piv


def dim_z(elts):
    """dim of the common centralizer in e6 of a list of elements."""
    rows = []
    for x in elts:
        cols = [brk6(x, b) for b in BAS]
        rows += [[cols[j].get(i, Fr(0)) for j in range(DIM6)] for i in range(DIM6)]
    return DIM6 - rank_rows(rows) if rows else DIM6


# ---------------------------------------------------------------- the principal sl2
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
    ff = E.vadd(ff, {E.N + E.IDX[neg]: Fr(sp.Rational(cv[j]).p, sp.Rational(cv[j]).q)
                     / E.eps(pos, neg)})


def to6(v8):
    return {INV[g]: c for g, c in v8.items()}


def hw_e6(n):
    cands = [r for r in E6_ROOTS
             if int(list(E.br(h, E.ev(r)).values())[0] if E.br(h, E.ev(r)) else 0) == n]
    M = sp.zeros(E.DIM, len(cands))
    for j, r in enumerate(cands):
        for k, val in E.br(ee, E.ev(r)).items():
            M[k, j] = sp.Rational(val.numerator, val.denominator)
    ns = M.nullspace()
    if not ns:
        return None
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

print("=" * 78)
print("BANKED IDENTITY -- the paper's own charge construction, rebuilt exactly over Q")
print("=" * 78)
gate("e6: 72 roots, dim 78", len(E6_ROOTS) == 72 and DIM6 == 78)

C = {}
for n in (8, 14, 16, 22):
    top = hw_e6(n)
    if top is None:
        continue
    Pp = sp.Poly(ADJ[n], x_, y_)
    acc, cur = {}, top
    for k in range(n + 1):
        co = Pp.coeff_monomial(x_**(n - k) * y_**k)
        if co:
            q = sp.Rational(co) * sp.factorial(n - k) / sp.factorial(n)
            q = sp.Rational(q)
            acc = E.vadd(acc, E.vmul(Fr(q.p, q.q), cur))
        cur = E.br(ff, cur)
    C[n] = to6(acc)

gate("charge degrees 8, 14, 16, 22 all built", sorted(C) == [8, 14, 16, 22],
     f"got {sorted(C)}")

# all six pairwise brackets vanish -- the paper's abelian claim
bad = [(a, b) for a, b in itertools.combinations(sorted(C), 2)
       if any(v != 0 for v in brk6(C[a], C[b]).values())]
gate("all six pairwise charge brackets vanish (C abelian)", not bad, f"nonzero: {bad}")

if FAILED:
    raise SystemExit("banked identity not reproduced -- stopping")

print()
print("=" * 78)
print("THE AUDIT -- dim z(S) over every subset S of the four charges")
print("=" * 78)
keys = sorted(C)
spectrum = {}
rows = []
for k in range(len(keys) + 1):
    for sub in itertools.combinations(keys, k):
        d = dim_z([C[i] for i in sub])
        rows.append((sub, d))
        spectrum.setdefault(d, []).append(sub)
        print(f"  z({', '.join('x'+str(s) for s in sub) if sub else '-- empty --':<22}) = {d}")

dim_zC = dict(rows)[tuple(keys)]

# coordinate subsets are NOT all subspaces.  Sweep general rational directions in C, and
# general 2-planes, so the reported spectrum is the real one and not a coordinate artefact.
print()
print("  general directions in C (not just coordinate subsets):")
import random                                                          # noqa: E402
rnd = random.Random(20260818)
gen = {}
COEFS = [-3, -2, -1, 0, 1, 2, 3]
seen_dirs = 0
for _ in range(220):
    co = [rnd.choice(COEFS) for _ in keys]
    if not any(co):
        continue
    v = {}
    for c, k in zip(co, keys):
        if c:
            v = {i: v.get(i, Fr(0)) + Fr(c) * val for i, val in C[k].items()} | \
                {i: v[i] for i in v if i not in C[k]}
    v = {i: c for i, c in v.items() if c != 0}
    d = dim_z([v])
    gen[d] = gen.get(d, 0) + 1
    seen_dirs += 1
for _ in range(220):
    co1 = [rnd.choice(COEFS) for _ in keys]
    co2 = [rnd.choice(COEFS) for _ in keys]
    vs = []
    for co in (co1, co2):
        if not any(co):
            continue
        v = {}
        for c, k in zip(co, keys):
            if c:
                v = {i: v.get(i, Fr(0)) + Fr(c) * val for i, val in C[k].items()} | \
                    {i: v[i] for i in v if i not in C[k]}
        vs.append({i: c for i, c in v.items() if c != 0})
    if len(vs) == 2:
        d = dim_z(vs)
        gen[d] = gen.get(d, 0) + 1
for d in sorted(gen):
    print(f"     dim z = {d:3d}   ({gen[d]} directions/planes)")

observed = sorted(set(spectrum) | set(gen))
print()
print(f"  OBSERVED SPECTRUM over all {len(rows)} subsets: {observed}")
print(f"  dim z(C) = {dim_zC}")

print()
print("=" * 78)
print("THE REFEREE'S ARGUMENT, CHECKED")
print("=" * 78)
print("  Centralizers are order-reversing: S subset C  =>  z(C) subset z(S).")
mono = all(d >= dim_zC for _, d in rows)
gate("every subset's centralizer contains z(C), so dim z(S) >= dim z(C)", mono)
PAPER = [6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]
impossible = [v for v in PAPER if v < dim_zC]
print(f"\n  paper's advertised spectrum: {PAPER}")
print(f"  values BELOW dim z(C) = {dim_zC}, hence IMPOSSIBLE for any S subset C: {impossible}")
notseen = [v for v in PAPER if v >= dim_zC and v not in observed]
print(f"  values not attained by any coordinate subset: {notseen}")
print(f"\n  REFEREE IS CORRECT: {bool(impossible)}")

RES = {
    "dim_e6": DIM6,
    "charge_degrees": keys,
    "all_pairwise_brackets_vanish": not bad,
    "dim_z_by_subset": {"+".join('x' + str(s) for s in sub) or "empty": d for sub, d in rows},
    "dim_z_C": dim_zC,
    "observed_spectrum_coordinate_subsets": observed,
    "paper_advertised_spectrum": PAPER,
    "impossible_because_below_dim_z_C": impossible,
    "advertised_but_not_attained_by_coordinate_subsets": notseen,
    "scope": ("coordinate subsets of the four charges; a full subspace sweep of C would only "
              "ADD values >= dim z(C) and cannot rescue any value below it, since z(C) is "
              "contained in z(V) for every subspace V of C"),
}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
