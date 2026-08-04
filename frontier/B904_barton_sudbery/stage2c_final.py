"""B904 stage 2c: the BS algebra with DERIVED cross products + fitted duals.

Cross products (derived uniquely in stage2b): (1,2)->3: xy; (2,3)->1: y*conj(x);
(3,1)->2: conj(y)*x. C'-side products derived here the same way. Same-summand
duals parametrized (3 component-weights each for tri(O) and tri(C') targets)
and fitted by an iterative failure-driven Jacobi loop; then FULL Jacobi.
"""
import os, pickle, json
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "stage1_tri.pkl"), "rb"))
SO = [np.array([[F(x) for x in row] for row in M], dtype=object) for M in D["SO"]]
TRI = [tuple([F(x) for x in comp] for comp in t) for t in D["TRI"]]
nso = len(SO)
def somat(coeffs):
    M = np.zeros((8, 8), dtype=object); M[:] = F(0)
    for a, c in enumerate(coeffs):
        if c: M = M + SO[a]*c
    return M
TA = [tuple(somat(t[k]) for k in range(3)) for t in TRI]
def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
def dot(u, v): return sum(a*b for a, b in zip(u, v))
def omul(x, y):
    a1, u1, v1, b1 = x[0], x[1:4], x[4:7], x[7]
    a2, u2, v2, b2 = y[0], y[1:4], y[4:7], y[7]
    return ((a1*a2 + dot(u1, v2),)
            + tuple(a1*u2[i] + b2*u1[i] - cross(v1, v2)[i] for i in range(3))
            + tuple(a2*v1[i] + b1*v2[i] + cross(u1, u2)[i] for i in range(3))
            + (b1*b2 + dot(v1, u2),))
def oconj(x):
    tr = x[0] + x[7]
    return (tr - x[0], -x[1], -x[2], -x[3], -x[4], -x[5], -x[6], tr - x[7])
E8 = [tuple(F(1) if i == j else F(0) for j in range(8)) for i in range(8)]
def opair(x, y):
    return (x[0]*y[7] + x[7]*y[0] - x[1]*y[4] - x[4]*y[1]
            - x[2]*y[5] - x[5]*y[2] - x[3]*y[6] - x[6]*y[3]) / 2
OPROD = {0: lambda x, y: omul(x, y),            # (1,2)->3
         1: lambda x, y: omul(y, oconj(x)),     # (2,3)->1
         2: lambda x, y: omul(oconj(y), x)}     # (3,1)->2
# ---- C' ----
E2 = [(F(1), F(0)), (F(0), F(1))]
def cmul(z, w): return (z[0]*w[0], z[1]*w[1])
def cconj(z): return (z[1], z[0])
def cpair(z, w): return (z[0]*w[1] + z[1]*w[0]) / 2
TCP = [(1, 1, 0), (1, 0, 1)]          # (sA, sB, sC) basis of tri(C')
CACT = {0: 1, 1: 2, 2: 0}             # summand i acted by component ACT[i]
def cact(gen, i, z):
    s = TCP[gen][CACT[i]]
    return (s*z[0], -s*z[1])
# derive C' cross products per slot among {zw, conj(z)w, z conj(w), conj both}
CC = {"zw": lambda z, w: cmul(z, w), "czw": lambda z, w: cmul(cconj(z), w),
      "zcw": lambda z, w: cmul(z, cconj(w)),
      "czcw": lambda z, w: cmul(cconj(z), cconj(w))}
CPROD = {}
for slot, (i, j, k) in enumerate([(0, 1, 2), (1, 2, 0), (2, 0, 1)]):
    ok = []
    for name, m in CC.items():
        good = True
        for g in range(2):
            for a in range(2):
                for b in range(2):
                    lhs = tuple(TCP[g][CACT[k]]*m(E2[a], E2[b])[0]*(1 if False else 1) for _ in (0,))
                    # compute properly:
                    mv = m(E2[a], E2[b])
                    lhs = (TCP[g][CACT[k]]*mv[0], -TCP[g][CACT[k]]*mv[1])
                    r1 = m(cact(g, i, E2[a]), E2[b])
                    r2 = m(E2[a], cact(g, j, E2[b]))
                    rhs = (r1[0] + r2[0], r1[1] + r2[1])
                    if lhs != rhs: good = False; break
                if not good: break
            if not good: break
        if good: ok.append(name)
    CPROD[slot] = ok
print("C' equivariant products per slot:", CPROD, flush=True)
CPF = {s: CC[CPROD[s][0]] for s in range(3)}

def act8(M, x):
    return tuple(sum(M[i][j]*x[j] for j in range(8)) for i in range(8))
def S_xy(x, y):
    M = np.zeros((8, 8), dtype=object); M[:] = F(0)
    for j in range(8):
        col = tuple(F(1) if i == j else F(0) for i in range(8))
        px, py = opair(x, col), opair(y, col)
        for i in range(8):
            M[i][j] = 2*(px*y[i] - py*x[i])
    return M
SOcols = sp.Matrix([[SO[a][i][j] for a in range(nso)]
                    for i in range(8) for j in range(8)])
SOpinv = (SOcols.T*SOcols).inv()*SOcols.T
def so_coeffs(M):
    v = sp.Matrix([M[i][j] for i in range(8) for j in range(8)])
    return [sp.Rational(x) for x in SOpinv*v]
Pi = {c: sp.Matrix([[TRI[t][c][a] for t in range(nso)] for a in range(nso)])
      for c in range(3)}
Piinv = {c: Pi[c].inv() for c in range(3)}
def tri_from_c(coeffs, c):
    v = Piinv[c] * sp.Matrix(coeffs)
    return [sp.Rational(x) for x in v]

def sidx(i, o, c): return 30 + 16*i + 8*c + o
DIM = 78
mu = {i: sp.Symbol(f"mu{i}") for i in range(3)}
nu = {i: sp.Symbol(f"nu{i}") for i in range(3)}
lam = {i: sp.Symbol(f"lam{i}") for i in range(3)}
SYMS = list(mu.values()) + list(nu.values()) + list(lam.values())

# ---- Killing-dual equivariant duals (constructed, not fitted) ----
# tri Killing (trace form over the three components):
KT = sp.Matrix(nso, nso, lambda a, b: sum(
    sum(TA[a][c][i][j]*TA[b][c][j][i] for i in range(8) for j in range(8))
    for c in range(3)))
KTinv = KT.inv()
def t_dual(i, x, y):
    # functional f_b = <TA[b][OACT[i]] x, y>_opair ; dual coeffs = KTinv f
    f = sp.Matrix([opair(act8(TA[b][OACT[i]], x), y) for b in range(nso)])
    v = KTinv * f
    return [sp.Rational(t) for t in v]
# C' side: 2-dim; action of TCP[g] on summand i has scalar TCP[g][CACT[i]]
KC = sp.Matrix(2, 2, lambda a, b: sum(
    2*TCP[a][c]*TCP[b][c] for c in range(3)))
KCinv = KC.inv()
def s_dual(i, z, w):
    # functional g -> <TCP[g]-action z, w>_cpair = TCP[g][CACT[i]] * (z+w- - ... )
    f = sp.Matrix([cpair((TCP[g][CACT[i]]*z[0], -TCP[g][CACT[i]]*z[1]), w)
                   for g in range(2)])
    v = KCinv * f
    return [sp.Rational(t) for t in v]

BR = defaultdict(lambda: sp.Integer(0))
def add(a, b, k, val):
    if val == 0: return
    if a > b: a, b, val = b, a, -val
    BR[(a, b, k)] += val
# [tri(O), tri(O)]
for a in range(nso):
    for b in range(a+1, nso):
        C1 = TA[a][0] @ TA[b][0] - TA[b][0] @ TA[a][0]
        for t, c in enumerate(tri_from_c(so_coeffs(C1), 0)):
            add(a, b, t, c)
# [tri(O), summand i]: component ACT[i] = (1,2,0)[i]
OACT = {0: 1, 1: 2, 2: 0}
for a in range(nso):
    for i in range(3):
        M = TA[a][OACT[i]]
        for o in range(8):
            Ax = act8(M, E8[o])
            for c in range(2):
                for oo in range(8):
                    if Ax[oo]:
                        add(a, sidx(i, o, c), sidx(i, oo, c), sp.Rational(Ax[oo]))
# [tri(C'), summand i]
for g in range(2):
    for i in range(3):
        s = TCP[g][CACT[i]]
        for o in range(8):
            for c in range(2):
                add(28 + g, sidx(i, o, c), sidx(i, o, c),
                    sp.Integer(s if c == 0 else -s))
# cross brackets with the DERIVED products, scale 1 (absorbed into duals)
for slot, (i, j, k) in enumerate([(0, 1, 2), (1, 2, 0), (2, 0, 1)]):
    for o1 in range(8):
        for o2 in range(8):
            prod = OPROD[slot](E8[o1], E8[o2])
            for c1 in range(2):
                for c2 in range(2):
                    cz = CPF[slot](E2[c1], E2[c2])
                    for oo in range(8):
                        if not prod[oo]: continue
                        for cc in range(2):
                            v = prod[oo]*cz[cc]
                            if v:
                                add(sidx(i, o1, c1), sidx(j, o2, c2),
                                    sidx(k, oo, cc), lam[slot]*sp.Rational(v))
# same-summand with CONSTRUCTED equivariant duals, scalars mu_i / nu_i only
for i in range(3):
    for o1 in range(8):
        for o2 in range(8):
            td = t_dual(i, E8[o1], E8[o2])
            pxy = opair(E8[o1], E8[o2])
            for c1 in range(2):
                for c2 in range(2):
                    a_, b_ = sidx(i, o1, c1), sidx(i, o2, c2)
                    if a_ >= b_: continue
                    pzw = cpair(E2[c1], E2[c2])
                    if pzw:
                        for t, cf in enumerate(td):
                            add(a_, b_, t, mu[i]*pzw*cf)
                    if pxy:
                        sd = s_dual(i, E2[c1], E2[c2])
                        for g in range(2):
                            add(a_, b_, 28 + g, nu[i]*pxy*sd[g])
print("tensor entries:", len(BR), flush=True)

BRIDX = defaultdict(dict)
for (a, b, k), v in BR.items():
    if v != 0: BRIDX[(a, b)][k] = v
def br(a, b):
    if a == b: return {}
    if a < b: return BRIDX.get((a, b), {})
    return {k: -v for k, v in BRIDX.get((b, a), {}).items()}
def jac(a, b, c):
    tot = defaultdict(lambda: sp.Integer(0))
    for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
        for k, v in br(y, z).items():
            for kk, vv in br(x, k).items():
                tot[kk] += v*vv
    return {k: sp.expand(v) for k, v in tot.items() if sp.expand(v) != 0}

import random
random.seed(3)
probes = [(0, 30, 46), (28, 30, 62), (30, 46, 62), (30, 31, 46),
          (5, 33, 50), (36, 52, 68), (30, 47, 65), (32, 49, 64),
          (30, 31, 42), (30, 32, 43), (46, 47, 58), (46, 48, 59),
          (62, 63, 74), (62, 64, 75), (30, 31, 45), (30, 33, 44)]
probes += [tuple(sorted(random.sample(range(30, 78), 3))) for _ in range(30)]
SUB = {}
for round_ in range(5):
    eqs = set()
    for t in probes:
        for k, v in jac(*t).items():
            eqs.add(sp.expand(v.subs(SUB)) if SUB else v)
    eqs = [e for e in eqs if e != 0]
    if not eqs:
        print("round", round_, ": no residual equations", flush=True)
        break
    sols = sp.solve(eqs, [s for s in SYMS if s not in SUB], dict=True)
    good = [s for s in sols if not any(v == 0 for v in s.values())]
    if sols and not good:
        print("  family detail:", [{str(k): v for k, v in s.items()} for s in sols[:2]], flush=True)
    print("round", round_, ":", len(eqs), "eqs,", len(sols), "families,",
          len(good), "nondegenerate", flush=True)
    if not good:
        json.dump({"fit": "FAILED_ROUND_%d" % round_},
                  open(os.path.join(HERE, "stage2c_results.json"), "w"))
        raise SystemExit(0)
    s0 = good[0]
    SUB.update(s0)
    # fix any remaining free symbols appearing in values
    for k in list(SUB):
        v = sp.sympify(SUB[k])
        for fs in v.free_symbols:
            if fs not in SUB: SUB[fs] = 1
        SUB[k] = v.subs(SUB)
    undet = [s for s in SYMS if s not in SUB]
    if not undet:
        break
print("fitted:", {str(k): sp.sstr(sp.nsimplify(v)) for k, v in SUB.items()},
      flush=True)
for s in SYMS:
    if s not in SUB: SUB[s] = 1
NBR = defaultdict(dict)
for (a, b, k), v in BR.items():
    val = sp.Rational(sp.expand(sp.sympify(v).subs(SUB)))
    if val != 0: NBR[(a, b)][k] = F(val.p, val.q)
def nbr(a, b):
    if a == b: return {}
    if a < b: return NBR.get((a, b), {})
    return {k: -v for k, v in NBR.get((b, a), {}).items()}
bad = 0; checked = 0; first = []
for a in range(DIM):
    for b in range(a+1, DIM):
        for c in range(b+1, DIM):
            tot = defaultdict(lambda: F(0))
            for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
                for k, v in nbr(y, z).items():
                    for kk, vv in nbr(x, k).items():
                        tot[kk] += v*vv
            checked += 1
            if any(v != 0 for v in tot.values()):
                bad += 1
                if len(first) < 5: first.append((a, b, c))
print(f"FULL JACOBI: {checked} triples, {bad} failures", first, flush=True)
if bad == 0:
    pickle.dump({str(k): {kk: str(vv) for kk, vv in d.items()}
                 for k, d in NBR.items()},
                open(os.path.join(HERE, "stage2c_tensor.pkl"), "wb"))
json.dump({"fit": "OK" if bad == 0 else "JACOBI_FAIL",
           "scalars": {str(k): str(v) for k, v in SUB.items()},
           "jacobi_failures": bad, "cprod": {str(k): v for k, v in CPROD.items()}},
          open(os.path.join(HERE, "stage2c_results.json"), "w"), indent=1)
print("saved", flush=True)
