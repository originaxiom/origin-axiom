#!/usr/bin/env python3
"""Helper: extract the Levi charges y, y2 (complex 78-vectors) via the descent
pipeline, saved for B884. Same construction as B876/B881."""
import json
import os
import random

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]
mp.dps = 30
src = open(B854, encoding="utf-8").read()
g = {"__file__": B854, "__name__": "b854"}
exec(compile(src, B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
triples = {}
for p in range(DIM):
    for q in range(DIM):
        v = br(basis[p], basis[q])
        for r, c in enumerate(v):
            if c:
                triples.setdefault(p, []).append((q, r, c))


def admat_num(vec, isfrac=True):
    A = mp.zeros(DIM, DIM)
    for p in range(DIM):
        vp = vec[p]
        if isfrac:
            if not vp:
                continue
            vp = mp.mpf(vp.numerator) / mp.mpf(vp.denominator)
        else:
            if abs(vp) < mp.mpf("1e-22"):
                continue
        for q, r, c in triples.get(p, []):
            A[r, q] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
    return A


A8 = admat_num(g["INV"][8])
A16 = admat_num(g["INV"][16])
import sys
_ri = int(sys.argv[1]) if len(sys.argv) > 1 else 0
t1 = sorted(13 * mp.re(r) for r in mpmath.polyroots(
    [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))[_ri]


def kernel_basis(M):
    U, S, Vt = mpmath.svd_r(M)
    nd = sum(1 for i in range(min(M.rows, M.cols))
             if S[i] < S[0] * mp.mpf("1e-18"))
    return [[Vt[i, j] for j in range(DIM)]
            for i in range(M.cols - nd, M.cols)]


K1 = kernel_basis(A8 + t1 * A16)
adK = [admat_num(k, isfrac=False) for k in K1]
allbr = []
for i in range(len(K1)):
    for j in range(i + 1, len(K1)):
        allbr.append([x for x in (adK[i] * mp.matrix(K1[j]))])
BU, BS, BVt = mpmath.svd_r(mp.matrix(allbr))
so10 = [[BVt[i, j] for j in range(DIM)]
        for i in range(min(len(allbr), DIM))
        if BS[i] > BS[0] * mp.mpf("1e-14")]
random.seed(11)


def rand_in(B):
    co = [mp.mpf(random.uniform(-1, 1)) for _ in B]
    v = [sum(co[i] * B[i][p] for i in range(len(B))) for p in range(DIM)]
    n = mp.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


def cent_in(space, elem):
    Ae = admat_num(elem, isfrac=False)
    M = mp.matrix([[x for x in (Ae * mp.matrix(s))] for s in space])
    U2, S2, V2t = mpmath.svd_r(M)
    rank = sum(1 for i in range(min(M.rows, M.cols))
               if S2[i] > S2[0] * mp.mpf("1e-14"))
    lnull = [[U2[j, i] for j in range(M.rows)] for i in range(rank, M.rows)]
    out = []
    for c in lnull:
        v = [sum(c[i] * space[i][p] for i in range(len(space)))
             for p in range(DIM)]
        out.append(v)
    if not out:
        return []
    OU, OS, OVt = mpmath.svd_r(mp.matrix(out))
    return [[OVt[i, j] for j in range(DIM)]
            for i in range(len(out)) if OS[i] > OS[0] * mp.mpf("1e-14")]


h = so10
while len(h) > 5:
    e = rand_in(h)
    h2 = cent_in(h, e)
    if len(h2) < len(h):
        h = h2
egen = rand_in(h)
Ag = admat_num(egen, isfrac=False)
P10 = mp.matrix(so10).T
M10 = P10.T * (Ag * P10)
Mc = mp.matrix(45, 45)
for i in range(45):
    for j in range(45):
        Mc[i, j] = mp.mpc(M10[i, j])
E, ER = mpmath.eig(Mc, left=False, right=True)
Ah = [admat_num(hk, isfrac=False) for hk in h]
roots40 = []
for i in range(45):
    if abs(E[i]) > mp.mpf("1e-10"):
        vec = [sum(ER[j, i] * so10[j][p] for j in range(45)) for p in range(DIM)]
        nv = mp.sqrt(sum(abs(x) ** 2 for x in vec))
        vecn = [x / nv for x in vec]
        alpha = []
        for k in range(5):
            img = Ah[k] * mp.matrix(vecn)
            alpha.append(sum(img[p] * mp.conj(vecn[p]) for p in range(DIM)))
        roots40.append(alpha)
Gram = mp.matrix(5, 5)
for a in range(5):
    for b in range(5):
        Gram[a, b] = sum((Ah[a] * Ah[b])[i, i] for i in range(DIM))
Ginv = Gram ** -1


def ipK(a, b):
    return sum(a[i] * Ginv[i, j] * b[j] for i in range(5) for j in range(5))


scale = 2 / ipK(roots40[0], roots40[0])
IP = [[int(mp.nint(mp.re(ipK(roots40[i], roots40[j]) * scale)))
       for j in range(40)] for i in range(40)]


def find_chain(length):
    def extend(chain):
        if len(chain) == length:
            return chain
        for c in range(40):
            if c in chain:
                continue
            if IP[chain[-1]][c] != -1:
                continue
            if any(IP[x][c] != 0 for x in chain[:-1]):
                continue
            r = extend(chain + [c])
            if r:
                return r
        return None
    for s in range(40):
        r = extend([s])
        if r:
            return r
    return None


chain4 = find_chain(4)
a4 = [roots40[i] for i in chain4]


def annihilator(rootlist):
    Meq = mp.matrix(len(rootlist), 5)
    for r_ in range(len(rootlist)):
        for k in range(5):
            Meq[r_, k] = mp.mpc(rootlist[r_][k])
    Ueq, Seq, Veqt = mpmath.svd_c(Meq, full_matrices=True)
    return [mp.conj(Veqt[4, k]) for k in range(5)]


yco = annihilator(a4)
y = [sum(yco[k] * h[k][p] for k in range(5)) for p in range(DIM)]
y2co = annihilator([a4[0], a4[1], a4[3]])
y2 = [sum(y2co[k] * h[k][p] for k in range(5)) for p in range(DIM)]
json.dump(dict(root_index=_ri, s1_t=mp.nstr(t1, 35), y=[[mp.nstr(mp.re(x), 35), mp.nstr(mp.im(x), 35)] for x in y],
               y2=[[mp.nstr(mp.re(x), 35), mp.nstr(mp.im(x), 35)] for x in y2]),
          open(os.path.join(HERE, f"levi_charges_r{_ri}.json"), "w"))
print("levi charges saved")
