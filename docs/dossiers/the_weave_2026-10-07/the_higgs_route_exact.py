#!/usr/bin/env python3
"""W123, a second and exact route (post hoc, labelled so; after the one run's read-out and the threshold check).

Every weakly holomorphic form of weight 3/2 for rho_R is c0 R + c1 DR + c2 D2R with c_j in Delta^-N C[E4, E6]
(R, DR, D2R are a basis at every tau: their Wronskian is a constant times eta^9, B1691). So d(m), the dimension with
order >= lambda - m on each eigenline, is the kernel of an exact rational matrix: no collocation and no threshold.
Computed at N = 3 and N = 4 (they must agree), compared with the run and with the threshold check, and the (0, 0, 1)
section compared with DR exactly.

    python3 -B the_higgs_route_exact.py      # writes the_higgs_route_exact.json beside itself
"""
import ast
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
import sympy as sp

D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
import the_higgs_route as HR

HR.NT = 160
L = HR.L
NT = HR.NT


def sigma(n, k):
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eis(k, c):
    co = [Fr(0)] * NT
    co[0] = Fr(1)
    for n in range(1, NT // 8 + 1):
        if 8 * n < NT:
            co[8 * n] = Fr(c * sigma(n, k - 1))
    return L(0, co)


E4, E6 = eis(4, 240), eis(6, -504)
DELTA = (E4 * E4 * E4 + (E6 * E6).neg()).scale(Fr(1, 1728))
assert DELTA.v == 8 and DELTA.c[0] == 1                      # q = x^8


def one():
    c = [Fr(0)] * NT
    c[0] = Fr(1)
    return L(0, c)


def powr(s, n):
    r = one()
    for _ in range(n):
        r = r * s
    return r


def Mbasis(w):
    return [(a, b) for a in range(w // 4 + 1) for b in range(w // 6 + 1) if 4 * a + 6 * b == w]


_, lines, _, dlines = HR.the_R_series()
e2 = HR.E2()
serre32 = lambda s: s.qdq() + (e2 * s).scale(Fr(-1, 8))       # D at weight 3/2: q d/dq - (3/2)/12 E2
d2lines = {e: serre32(s) for e, s in dlines.items()}
B = [lines, dlines, d2lines]                                   # weights -1/2, 3/2, 7/2
EXPS = [Fr(1, 8), Fr(3, 8), Fr(7, 8)]


def columns(N):
    Dinv = powr(DELTA, N).inv()
    cols = []
    for j, w in enumerate((2, 0, -2)):
        for (a, b) in Mbasis(w + 12 * N):
            c = powr(E4, a) * powr(E6, b) * Dinv
            cols.append({e: c * B[j][e] for e in EXPS})
    return cols


def dim(m, cols):
    rows = []
    for e, me in zip(EXPS, m):
        bound = 8 * (e - me)                                   # x-exponent bound: keep x^k with k >= bound
        ks = sorted({col[e].v + i for col in cols for i, a in enumerate(col[e].c) if a and col[e].v + i < bound})
        for k in ks:
            rows.append([col[e].c[k - col[e].v] if 0 <= k - col[e].v < NT else Fr(0) for col in cols])
    if not rows:
        return len(cols), None
    M = sp.Matrix(rows)
    r = M.rank()
    return len(cols) - r, M


res = {}
for N in (3, 4):
    cols = columns(N)
    tab = {}
    for m in itertools.product((-1, 0, 1, 2), repeat=3):
        tab[str(m)] = dim(m, cols)[0]
    res[N] = tab
    print("N", N, "columns", len(cols), flush=True)
same = res[3] == res[4]
print("N = 3 and N = 4 agree:", same)
ph = json.loads((D / "the_higgs_route_posthoc.json").read_text())["rho"]["table"]
run = json.loads((D / "the_higgs_route.json").read_text())["census rho"]
dis = {m: (res[4][m], ph[m][0]) for m in res[4] if res[4][m] != ph[m][0]}
print("exact d vs collocation (post hoc 1e-12) disagreements:", dis)
print("exact d vs the run's d disagreements:",
      {m: (res[4][m], run[m]["d"]) for m in res[4] if res[4][m] != run[m]["d"]})
print("exact d: m<=0 all zero:", all(res[4][m] == 0 for m in res[4] if max(ast.literal_eval(m)) <= 0))
for m in ("(1, 0, 0)", "(0, 1, 0)", "(0, 0, 1)", "(1, 1, 1)", "(2, 2, 2)"):
    print("  d", m, "=", res[4][m])
# the (0,0,1) space: is it C . DR exactly?
cols = columns(4)
_, M = dim((0, 0, 1), cols)
ker = M.nullspace()
print("kernel dim (0,0,1):", len(ker))
v = ker[0]
f = {e: None for e in EXPS}
for e in EXPS:
    acc = None
    for c, col in zip(v, cols):
        if c != 0:
            t = col[e].scale(Fr(int(sp.Rational(c).p), int(sp.Rational(c).q)))
            acc = t if acc is None else acc + t
    f[e] = acc
# compare with DR line series up to x^60
ratio = None; ok = True
for e in EXPS:
    a, b = f[e], dlines[e]
    for k in range(min(a.v, b.v), 60):
        ca = a.c[k - a.v] if 0 <= k - a.v < NT else 0
        cb = b.c[k - b.v] if 0 <= k - b.v < NT else 0
        if cb != 0 and ratio is None:
            ratio = Fr(ca) / Fr(cb)
        if ratio is not None and Fr(ca) != ratio * Fr(cb):
            ok = False
print("the (0,0,1) section equals DR up to scale (exact, to x^60):", ok, "ratio", ratio)
dis_run = {m: [res[4][m], run[m]["d"]] for m in res[4] if res[4][m] != run[m]["d"]}
out = {"arc": "W123", "status": "post hoc, labelled; an exact second route", "d at N = 3": res[3], "d at N = 4": res[4],
       "N = 3 and N = 4 agree": same, "disagreements with the threshold check (1e-12)": dis,
       "disagreements with the run (exact, run)": dis_run, "d = 0 for every m <= 0": all(
           res[4][m] == 0 for m in res[4] if max(ast.literal_eval(m)) <= 0),
       "the (0, 0, 1) section equals DR (exact, to x^60)": ok, "ratio": str(ratio)}
(D / "the_higgs_route_exact.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
