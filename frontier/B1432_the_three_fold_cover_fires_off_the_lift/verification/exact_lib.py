#!/usr/bin/env python3
"""EXACT (characteristic zero) index of a doublet module on M_n, over Q(zeta_N) with N = $OA_CYC (default 4), using
main's own cyclotomic arithmetic (B1427 cyclo.py). No prime field anywhere. Same definitions as myindex.py:
I = (a1 - r1)(V) - (a1 - r1)(V*), cocycle convention f(gh) = f(g) + rho(g) f(h)."""
import sys, json, pathlib
from collections import Counter
REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'frontier/B1427_the_towers_generation_count_verified/verification'))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cyclo import Cyc
import cover_census as cc

import os
F = Cyc(int(os.environ.get('OA_CYC','4'))); Z, O = F.zero(), F.one()

def rref(rows, ncols, want_null=False):
    R = [list(r) for r in rows]; piv = []; rk = 0
    for c in range(ncols):
        k = next((i for i in range(rk, len(R)) if not F.is_zero(R[i][c])), None)
        if k is None: continue
        R[rk], R[k] = R[k], R[rk]
        iv = F.inv(R[rk][c]); R[rk] = [F.mul(iv, x) for x in R[rk]]
        for i in range(len(R)):
            if i != rk and not F.is_zero(R[i][c]):
                f = R[i][c]; R[i] = [F.sub(x, F.mul(f, y)) for x, y in zip(R[i], R[rk])]
        piv.append(c); rk += 1
    if not want_null: return rk, None
    NS = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [Z] * ncols; v[fc] = O
        for i, pc in enumerate(piv): v[pc] = F.neg(R[i][fc])
        NS.append(v)
    return rk, NS

def mmul(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            acc = Z
            for l in range(len(B)): acc = F.add(acc, F.mul(A[i][l], B[l][j]))
            row.append(acc)
        out.append(row)
    return out
def msub(A, B): return [[F.sub(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
def madd(A, B): return [[F.add(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
def eye(d): return [[O if i == j else Z for j in range(d)] for i in range(d)]
def inv2(M):      # upper or lower triangular 2x2 with unit-modulus diagonal: generic 2x2 inverse
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = F.sub(F.mul(a, d), F.mul(b, c)); iv = F.inv(det)
    return [[F.mul(iv, d), F.neg(F.mul(iv, b))], [F.neg(F.mul(iv, c)), F.mul(iv, a)]]
def T(M): return [list(r) for r in zip(*M)]

class Rep:
    def __init__(s, mats): s.m = mats; s.i = [inv2(M) for M in mats]; s.ng = len(mats)
    def ev(s, w):
        R = eye(2)
        for L in w: R = mmul(R, s.m[L - 1] if L > 0 else s.i[-L - 1])
        return R
    def fox(s, w):
        D = [[[Z, Z], [Z, Z]] for _ in range(s.ng)]; pre = eye(2)
        for L in w:
            g = abs(L) - 1
            if L > 0: D[g] = madd(D[g], pre); pre = mmul(pre, s.m[g])
            else: pre = mmul(pre, s.i[g]); D[g] = msub(D[g], pre)
        return D
    def dual(s): return Rep([T(M) for M in s.i])

def cohom(V, rels, mu, lam):
    d = 2; ng = V.ng; I2 = eye(2)
    D0 = [row for M in V.m for row in msub(M, I2)]
    rk0, _ = rref(D0, d); a0 = d - rk0
    J = []
    for r in rels:
        Fx = V.fox(r)
        for i in range(d): J.append([Fx[g][i][j] for g in range(ng) for j in range(d)])
    rkJ, Z1 = rref(J, ng * d, want_null=True); a1 = (ng * d - rkJ) - rk0
    Am = msub(V.ev(mu), I2); Al = msub(V.ev(lam), I2)
    BT = [list(r) for r in Am] + [list(r) for r in Al]
    rkBT, _ = rref(BT, d); t0 = d - rkBT
    ZT = [[F.neg(Al[i][j]) for j in range(d)] + [Am[i][j] for j in range(d)] for i in range(d)]
    rkZT, _ = rref(ZT, 2 * d); t1 = (2 * d - rkZT) - rkBT
    Dm = V.fox(mu); Dl = V.fox(lam)
    Res = [[Dm[g][i][j] for g in range(ng) for j in range(d)] for i in range(d)] + \
          [[Dl[g][i][j] for g in range(ng) for j in range(d)] for i in range(d)]
    cols = []
    for z in Z1:
        col = []
        for i in range(2 * d):
            acc = Z
            for k in range(len(z)): acc = F.add(acc, F.mul(Res[i][k], z[k]))
            col.append(acc)
        cols.append(col)
    BTc = [[BT[i][j] for i in range(2 * d)] for j in range(d)]
    rk_all, _ = rref(cols + BTc, 2 * d); rkB, _ = rref(BTc, 2 * d)
    return a0, a1, t0, t1, rk_all - rkB

def index(V, rels, mu, lam):
    a0, a1, t0, t1, r1 = cohom(V, rels, mu, lam); b0, b1, s0, s1, q1 = cohom(V.dual(), rels, mu, lam)
    I = (a1 - r1) - (b1 - q1)
    assert r1 + q1 == t1 == s1 and I == (a0 - b0) + s0 - r1
    return I

def fox1(word, val, ng):
    D = [Z] * ng; pre = O
    for L in word:
        g = abs(L) - 1
        if L > 0: D[g] = F.add(D[g], pre); pre = F.mul(pre, val[g])
        else: pre = F.mul(pre, F.inv(val[g])); D[g] = F.sub(D[g], pre)
    return D


def exact_index(n, N, lc, al):
    ng, rels, mu, lam, tau = cc.cover(n)
    assert F.m == N
    val = [F.zeta(e) for e in lc]
    rows = [fox1(r, val, ng) for r in rels]
    rk, NS = rref(rows, ng, want_null=True)
    b = [F.sub(v, O) for v in val]; rb = 0 if all(F.is_zero(x) for x in b) else 1
    assert len(NS) - rb == 1
    ct = next(z for z in NS if rb == 0 or rref([b, z], ng)[0] == 2)
    mats = []
    for g in range(ng):
        a = F.zeta(al[g]); bb = F.zeta(al[g] - lc[g])
        mats.append([[a, F.mul(ct[g], bb)], [Z, bb]])
    V = Rep(mats)
    assert all(V.ev(r) == eye(2) for r in rels)
    return index(V, rels, mu, lam)
