#!/usr/bin/env python3
"""B883 -- THE 27 on the B854 Chevalley frame, via the e7 3-grading.

Route (all signs inherited, none hand-fixed): build e7 by EXACTLY the B854 recipe
(same Cartan-block, same E0/eps cocycle -- so the e6 inside is B854's frame
verbatim, checked below), grade by the 7th fundamental coweight:

    e7 = 27bar (charge -1)  +  (e6 + R) (charge 0)  +  27 (charge +1),

and read the 27's matrices off e7's bracket table. Verified as a representation
on ALL 78 x 78 basis pairs exactly (integer arithmetic throughout), then
validated against the banked branching 27 = 1 + 10 + 16 at the enhancement
point (three eigenvalue clusters of rho(s1) with multiplicities {1, 10, 16}).

The instrument the queue named: unlocks the Yukawa skeleton (the cubic
invariant), the E-clause capstone, and the DVT comparison.
"""
import json
import os
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- e7 build
C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
N = 7
C = [row[:] + [0] for row in C6] + [[0, 0, 0, 0, 0, -1, 2]]
C[5][6] = -1


def ip(a, b):
    return sum(a[i] * b[j] * C[i][j] for i in range(N) for j in range(N))


print("[1] roots...")
pos = [t for t in product(range(5), repeat=N) if any(t) and ip(t, t) == 2]
assert len(pos) == 63, len(pos)
ROOTS = pos + [tuple(-x for x in t) for t in pos]
IDX = {r: k for k, r in enumerate(ROOTS)}
DIM = N + len(ROOTS)
assert DIM == 133

E0 = [[(-1 if i == j else ((-1) ** C[i][j] if i < j else 1)) for j in range(N)]
      for i in range(N)]


def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N):
            if b[j] == 0:
                continue
            if E0[i][j] == -1 and (a[i] * b[j]) % 2:
                s = -s
    return s


def bracket_basis(p, q):
    out = [0] * DIM
    if p < N and q < N:
        return out
    if p < N:
        b = ROOTS[q - N]
        out[q] = sum(b[j] * C[p][j] for j in range(N))
        return out
    if q < N:
        a = ROOTS[p - N]
        out[p] = -sum(a[j] * C[q][j] for j in range(N))
        return out
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if all(v == 0 for v in s):
        sgn = eps(a, tuple(-v for v in a))
        for i in range(N):
            out[i] = sgn * a[i]
        return out
    if s in IDX:
        out[N + IDX[s]] = eps(a, b)
    return out


print("[2] bracket table + Jacobi self-check...")
BB = [[bracket_basis(p, q) for q in range(DIM)] for p in range(DIM)]


def br(u, v):
    out = [0] * DIM
    for p, up in enumerate(u):
        if not up:
            continue
        for q, vq in enumerate(v):
            if not vq:
                continue
            row = BB[p][q]
            c = up * vq
            for k, rk in enumerate(row):
                if rk:
                    out[k] += c * rk
    return out


import random
random.seed(7)
for _ in range(1500):
    p, q, r = (random.randrange(DIM) for _ in range(3))
    ep = [0] * DIM; ep[p] = 1
    eq = [0] * DIM; eq[q] = 1
    er = [0] * DIM; er[r] = 1
    j1 = br(br(ep, eq), er)
    j2 = br(ep, br(eq, er))
    j3 = br(eq, br(ep, er))
    assert all(j1[k] == j2[k] - j3[k] for k in range(DIM)), (p, q, r)
print("    Jacobi: 1500 random basis triples exact")

# ---------------------------------------------------------------- the grading
print("[3] the 3-grading by node 6...")
charge = {}
for k, rt in enumerate(ROOTS):
    charge[N + k] = rt[6]
for i in range(N):
    charge[i] = 0
zero = [i for i in range(DIM) if charge[i] == 0]
plus = [i for i in range(DIM) if charge[i] == 1]
minus = [i for i in range(DIM) if charge[i] == -1]
assert (len(zero), len(plus), len(minus)) == (79, 27, 27)

# the e6 inside: h_0..h_5 + roots with a6 = 0 -- must be B854's frame verbatim
import importlib.util
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
src6 = open(B854, encoding="utf-8").read()
g6 = {"__file__": B854, "__name__": "b854"}
exec(compile(src6, B854, "exec"), g6)
R6, IDX6 = g6["ROOTS"], g6["IDX"]
emap = {}          # e6 basis index (B854, 0..77) -> e7 basis index
for i in range(6):
    emap[i] = i
for r6, k6 in IDX6.items():
    r7 = tuple(r6) + (0,)
    emap[6 + k6] = N + IDX[r7]
# frame check: structure constants agree on 3000 random pairs
from fractions import Fraction as Fr
br6 = g6["br"]
ok = True
for _ in range(3000):
    p6, q6 = random.randrange(78), random.randrange(78)
    v6 = br6([Fr(1) if i == p6 else Fr(0) for i in range(78)],
             [Fr(1) if i == q6 else Fr(0) for i in range(78)])
    v7 = BB[emap[p6]][emap[q6]]
    for k6 in range(78):
        if Fr(v7[emap[k6]]) != v6[k6]:
            ok = False
assert ok
print("    e6-inside-e7 frame == B854 frame: 3000 random pairs exact")

# ---------------------------------------------------------------- the 27
print("[4] the 27 matrices...")
pidx = {b: a for a, b in enumerate(plus)}
REP = {}
for p6 in range(78):
    p7 = emap[p6]
    M = [[0] * 27 for _ in range(27)]
    for j, bidx in enumerate(plus):
        row = BB[p7][bidx]
        for k, coef in enumerate(row):
            if coef:
                assert charge[k] == 1, "grading violated"
                M[pidx[k]][j] = coef
    REP[p6] = M


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(27) if A[i][k])
             for j in range(27)] for i in range(27)]


print("[5] full homomorphism check (78 x 78 pairs, exact integers)...")
bad = 0
for p6 in range(78):
    for q6 in range(78):
        v6 = br6([Fr(1) if i == p6 else Fr(0) for i in range(78)],
                 [Fr(1) if i == q6 else Fr(0) for i in range(78)])
        L = matmul(REP[p6], REP[q6])
        Rm = matmul(REP[q6], REP[p6])
        for i in range(27):
            for j in range(27):
                lhs = L[i][j] - Rm[i][j]
                rhs = sum(int(v6[k6]) * REP[k6][i][j] for k6 in range(78)
                          if v6[k6])
                if lhs != rhs:
                    bad += 1
assert bad == 0
print("    rho([x,y]) = [rho x, rho y] on ALL 6084 basis pairs: exact")

# weights: minuscule, multiplicity 1, highest weight a fundamental one
wts = []
for bidx in plus:
    rt = ROOTS[bidx - N]
    wts.append(tuple(sum(rt[j] * C[i][j] for j in range(N)) for i in range(6)))
assert len(set(wts)) == 27
hw = [w for w in wts if all(x >= 0 for x in w)]
print(f"    27 distinct weights; dominant: {hw}")

json.dump(dict(rep={str(p): REP[p] for p in REP},
               weights=[list(w) for w in wts],
               plus_roots=[list(ROOTS[b - N]) for b in plus],
               convention="B854 e6 basis order (0..5 Cartan, 6.. root vectors); "
                          "27 basis = charge-+1 roots of e7 in listed order"),
          open(os.path.join(HERE, "rep27.json"), "w"))
print("    rep27.json written")

# ---------------------------------------------------------------- validation
print("[6] validation: 27 = 1 + 10 + 16 at the enhancement point...")
import mpmath
from mpmath import mp
mp.dps = 30
CUBIC = [500716339200, -159667200, -28224, 1]
t1 = sorted(13 * mp.re(r) for r in mpmath.polyroots(
    [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))[0]
inv8 = g6["INV"][8]
inv16 = g6["INV"][16]
S27 = mp.zeros(27, 27)
for p6 in range(78):
    c8 = mp.mpf(inv8[p6].numerator) / mp.mpf(inv8[p6].denominator)
    c16 = mp.mpf(inv16[p6].numerator) / mp.mpf(inv16[p6].denominator)
    coef = c8 + t1 * c16
    if abs(coef) < mp.mpf("1e-25"):
        continue
    for i in range(27):
        for j in range(27):
            if REP[p6][i][j]:
                S27[i, j] += coef * REP[p6][i][j]
Mc = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        Mc[i, j] = mp.mpc(S27[i, j])
E2, ER2 = mpmath.eig(Mc, left=False, right=True)
vals = [E2[i] for i in range(27)]
groups = []
for v in vals:
    for grp in groups:
        if abs(v - grp[0]) < mp.mpf("1e-9"):
            grp.append(v)
            break
    else:
        groups.append([v])
mults = sorted(len(gp) for gp in groups)
print(f"    rho(s1) eigenvalue multiplicities: {mults}  (banked branching needs [1, 10, 16])")
res = dict(jacobi_triples=1500, frame_pairs=3000, hom_pairs=6084,
           weights_distinct=27, dominant_weights=[list(w) for w in hw],
           s1_multiplicities=mults,
           validated=(mults == [1, 10, 16]))
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True, default=str)
print(f"  VALIDATED: {res['validated']}")
