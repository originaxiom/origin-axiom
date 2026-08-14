#!/usr/bin/env python3
"""B892 -- independent verification of the SECOND MEASUREMENT THEOREM by direct
wall search: scan y(theta) = cos(theta) x14 + sin(theta) x16 (the SMT's y* is
gamma*x14 - a*x16, a point on this projective line), find where
dim z(x1, y) jumps above the generic 12, and type the wall centralizer."""
import json
import os

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]
mp.dps = 30
g = {"__file__": B854, "__name__": "b854"}
exec(compile(open(B854).read(), B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
triples = {}
for p in range(DIM):
    for qq in range(DIM):
        v = br(basis[p], basis[qq])
        for r, c in enumerate(v):
            if c:
                triples.setdefault(p, []).append((qq, r, c))


def admat_num(vec, isfrac=True):
    A = mp.zeros(DIM, DIM)
    for p in range(DIM):
        vp = vec[p]
        if isfrac:
            if not vp:
                continue
            vp = mp.mpf(vp.numerator) / mp.mpf(vp.denominator)
        else:
            if abs(vp) < mp.mpf("1e-24"):
                continue
        for qq, r, c in triples.get(p, []):
            A[r, qq] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
    return A


def vnum(n):
    return [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][n]]


A8 = admat_num(g["INV"][8])
A14 = admat_num(g["INV"][14])
A16 = admat_num(g["INV"][16])
t1 = sorted(13 * mp.re(r) for r in mpmath.polyroots(
    [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))[0]
As1 = A8 + t1 * A16


def joint_nullity(th):
    Ay = A14 * mp.cos(th) + A16 * mp.sin(th)
    St = mp.matrix(2 * DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            St[i, j] = As1[i, j]
            St[DIM + i, j] = Ay[i, j]
    U, S, Vt = mpmath.svd_r(St)
    smax = S[0]
    return sum(1 for i in range(DIM) if S[i] < smax * mp.mpf("1e-18")), \
        [S[i] for i in range(DIM)]


print("[1] coarse scan for the wall (nullity > 12)...")
import math
found = []
Ngrid = 120
for k in range(Ngrid):
    th = mp.pi * k / Ngrid
    nd, sv = joint_nullity(th)
    if nd > 12:
        found.append((float(th), nd))
        print(f"    theta = {float(th):.5f}: nullity {nd}  <-- WALL")
if not found:
    # refine via the sigma-gap function: minimize the 14th-smallest sigma
    print("    no wall on coarse grid; refining via sigma minimization...")
    def s14(th):
        nd, sv = joint_nullity(th)
        return sv[DIM - 13 - 1]   # the sigma that must vanish for nullity 14
    best = None
    for k in range(Ngrid):
        th = mp.pi * k / Ngrid
        v = s14(th)
        if best is None or v < best[1]:
            best = (th, v)
    print(f"    min s14 at theta ~ {float(best[0]):.5f}, value {mp.nstr(best[1], 4)}")
    # golden-section refine
    a, b = best[0] - mp.pi / Ngrid, best[0] + mp.pi / Ngrid
    for _ in range(60):
        m1 = a + (b - a) * mp.mpf("0.381966")
        m2 = b - (b - a) * mp.mpf("0.381966")
        if s14(m1) < s14(m2):
            b = m2
        else:
            a = m1
    thw = (a + b) / 2
    ndw, svw = joint_nullity(thw)
    print(f"    refined theta = {mp.nstr(thw, 20)}: nullity {ndw}, "
          f"s14 = {mp.nstr(s14(thw), 4)}")
    found.append((float(thw), ndw))

res = dict(wall_points=found)
if found and found[-1][1] >= 14:
    th = mp.mpf(found[-1][0])
    Ay = A14 * mp.cos(th) + A16 * mp.sin(th)
    St = mp.matrix(2 * DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            St[i, j] = As1[i, j]
            St[DIM + i, j] = Ay[i, j]
    U, S, Vt = mpmath.svd_r(St)
    smax = S[0]
    nd = sum(1 for i in range(DIM) if S[i] < smax * mp.mpf("1e-15"))
    kern = [[Vt[i, j] for j in range(DIM)] for i in range(DIM - nd, DIM)]
    print(f"[2] typing the wall centralizer (dim {nd})...")
    adK = [admat_num(k2, isfrac=False) for k2 in kern]
    allbr = []
    for i in range(nd):
        for j in range(i + 1, nd):
            allbr.append([x for x in (adK[i] * mp.matrix(kern[j]))])
    BU, BS, BVt = mpmath.svd_r(mp.matrix(allbr))
    dd = sum(1 for i in range(min(len(allbr), DIM))
             if BS[i] > BS[0] * mp.mpf("1e-13"))
    print(f"    derived dim = {dd}  (SMT: dim 14, derived 11 => su(3)+su(2)+u(1)^3)")
    res["wall_dim"] = nd
    res["wall_derived"] = dd
    res["smt_verified"] = (nd == 14 and dd == 11)
json.dump(res, open(os.path.join(HERE, "wall_results.json"), "w"), indent=1)
print("done")
