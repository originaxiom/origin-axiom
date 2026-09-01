"""R13 blind — assemble L(78) with 9 symbolic scalars, Jacobi-fit them on probes,
then FULL exact Jacobi over all ordered triples (covers all 76,076 unordered).
"""
from fractions import Fraction as F
import itertools, pickle, os, json, random
import sympy as sp
import numpy as np
from octonion_core import (OBASIS, OMT, OPOL, CBASIS, CMT, CPOL,
                           omul, oconj, cmul, cconj)

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "my_tri.pkl"), "rb"))
TRIO, TRIC = D["triO"], D["triC"]
DD = pickle.load(open(os.path.join(HERE, "my_derived.pkl"), "rb"))
TDUAL, SDUAL, TBRK, CBRK = DD["TDUAL"], DD["SDUAL"], DD["TBRK"], DD["CBRK"]
OSCAN, CSCAN = DD["OSCAN"], DD["CSCAN"]

NT, NC = 28, 2
NB = 78

def base(i):  # V_i base index, i in 1..3
    return 30 + 16 * (i - 1)

def vidx(i, a, c):
    return base(i) + 2 * a + c

def comp(tri, i):
    A, B, C = tri
    return (B, C, A)[i - 1]

def matvec(M, v):
    return tuple(sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(M)))

# derived products (unique survivors of my scan)
def pO(k, x, y):
    name = OSCAN[str((*( [(1,2,3),(2,3,1),(3,1,2)][k-1] ),))][0] if False else None
    raise RuntimeError

PO_NAME = {3: OSCAN['(1, 2, 3)'][0], 1: OSCAN['(2, 3, 1)'][0], 2: OSCAN['(3, 1, 2)'][0]}
PC_NAME = {3: CSCAN['(1, 2, 3)'][0], 1: CSCAN['(2, 3, 1)'][0], 2: CSCAN['(3, 1, 2)'][0]}

def oprod(name, x, y):
    xx = oconj(x) if 'cx' in name else x
    yy = oconj(y) if 'cy' in name else y
    return omul(yy, xx) if name.startswith('R') else omul(xx, yy)

def cprod(name, z, w):
    zz = cconj(z) if 'cz' in name else z
    ww = cconj(w) if 'cw' in name else w
    return cmul(zz, ww)

lam = sp.symbols('lam1:4')
mu = sp.symbols('mu1:4')
nu = sp.symbols('nu1:4')
SYMS = list(lam) + list(mu) + list(nu)

def frac2sp(q):
    return sp.Rational(q.numerator, q.denominator)

CYC = {(1, 2): 3, (2, 3): 1, (3, 1): 2}

def bracket_pq(p, q):
    """[b_p, b_q] as dict idx -> sympy expr, for p < q ordering handled by caller."""
    out = {}
    def add(k, val):
        if val == 0:
            return
        out[k] = out.get(k, sp.Integer(0)) + val
    if p < NT and q < NT:
        for m, c in enumerate(TBRK[(p, q)]):
            if c:
                add(m, frac2sp(c))
        return out
    if NT <= p < 30 and NT <= q < 30:
        for m, c in enumerate(CBRK[(p - NT, q - NT)]):
            if c:
                add(NT + m, frac2sp(c))
        return out
    if p < NT and NT <= q < 30:
        return out  # [tri(O), tri(C')] = 0
    if p < NT and q >= 30:  # T acting on V_i
        i = (q - 30) // 16 + 1
        r = (q - 30) % 16
        a, cc = r // 2, r % 2
        col = matvec(comp(TRIO[p], i), OBASIS[a])
        for l in range(8):
            if col[l]:
                add(vidx(i, l, cc), frac2sp(col[l]))
        return out
    if NT <= p < 30 and q >= 30:  # S acting on V_i
        i = (q - 30) // 16 + 1
        r = (q - 30) % 16
        a, cc = r // 2, r % 2
        col = matvec(comp(TRIC[p - NT], i), CBASIS[cc])
        for l in range(2):
            if col[l]:
                add(vidx(i, a, l), frac2sp(col[l]))
        return out
    if p >= 30 and q >= 30:
        i = (p - 30) // 16 + 1
        j = (q - 30) // 16 + 1
        rp, rq = (p - 30) % 16, (q - 30) % 16
        a, c1 = rp // 2, rp % 2
        b, c2 = rq // 2, rq % 2
        if i == j:
            # mu_i t_i(a,b) <z,w>_C  + nu_i s_i(c1,c2) <x,y>_O
            zp = frac2sp(CPOL[c1][c2])
            if zp:
                for m, co in enumerate(TDUAL[i][(a, b)]):
                    if co:
                        add(m, mu[i - 1] * frac2sp(co) * zp)
            xp = frac2sp(OPOL[a][b])
            if xp:
                for m, co in enumerate(SDUAL[i][(c1, c2)]):
                    if co:
                        add(NT + m, nu[i - 1] * frac2sp(co) * xp)
            return out
        if (i, j) in CYC:
            k = CYC[(i, j)]
            sgn = 1
        else:
            k = CYC[(j, i)]
            sgn = -1
            (a, c1), (b, c2) = (b, c2), (a, c1)
        xo = oprod(PO_NAME[k], OBASIS[a], OBASIS[b])
        zc = cprod(PC_NAME[k], CBASIS[c1], CBASIS[c2])
        for l in range(8):
            if xo[l]:
                for m in range(2):
                    if zc[m]:
                        add(vidx(k, l, m), sgn * lam[k - 1] * frac2sp(xo[l]) * frac2sp(zc[m]))
        return out
    raise RuntimeError((p, q))

print("building symbolic bracket table ...")
BR = {}
for p in range(NB):
    for q in range(p + 1, NB):
        BR[(p, q)] = bracket_pq(p, q)

def brk(p, q):
    if p == q:
        return {}
    if p < q:
        return BR[(p, q)]
    return {k: -v for k, v in BR[(q, p)].items()}

def brk_vec(vec, q):
    """[vec, b_q] where vec is dict idx->expr"""
    out = {}
    for p, cp in vec.items():
        for k, v in brk(p, q).items():
            out[k] = out.get(k, sp.Integer(0)) + cp * v
    return out

def jacobi(pqr):
    p, q, r = pqr
    out = {}
    for (x, y, z) in ((p, q, r), (q, r, p), (r, p, q)):
        t = brk_vec(brk(y, z), x)
        for k, v in t.items():
            out[k] = out.get(k, sp.Integer(0)) + v
    return out

# probe triples: cover the scalar-coupling types
random.seed(7)
probes = []
# same-summand pure: three V_i
for i in (1, 2, 3):
    for _ in range(6):
        probes.append(tuple(random.sample(range(base(i), base(i) + 16), 3)))
# two same + one other V
for i in (1, 2, 3):
    for j in (1, 2, 3):
        if i != j:
            for _ in range(4):
                a, b = random.sample(range(base(i), base(i) + 16), 2)
                c = random.randrange(base(j), base(j) + 16)
                probes.append((a, b, c))
# fully mixed
for _ in range(10):
    probes.append((random.randrange(base(1), base(1) + 16),
                   random.randrange(base(2), base(2) + 16),
                   random.randrange(base(3), base(3) + 16)))
# with tri elements
for _ in range(8):
    probes.append((random.randrange(0, 30),
                   random.randrange(base(1), base(3) + 16),
                   random.randrange(base(1), base(3) + 16)))

print("collecting Jacobi probe equations ...")
eqs = set()
for tr in probes:
    for k, v in jacobi(tr).items():
        v = sp.expand(v)
        if v != 0:
            eqs.add(v)
eqs = list(eqs)
print("  distinct nonzero probe expressions:", len(eqs))

sol = sp.solve(eqs, SYMS, dict=True)
print("solution branches:", len(sol))
print("branches (full):", sol)
# gauge freedom: rescaling V_i rescales lam; fix lam = 1 and take the branch values
good = None
for s in sol:
    trial = dict(s)
    for L in lam:
        trial[L] = sp.Integer(1)
    trial = {k: sp.nsimplify(sp.expand(v.subs({L: 1 for L in lam}))) if not v.is_number else v
             for k, v in trial.items()}
    if all(x in trial and trial[x].is_number for x in SYMS):
        # confirm this closes the probe equations
        if all(sp.expand(e.subs(trial)) == 0 for e in eqs):
            good = trial
            break
assert good is not None, "no nondegenerate branch"
print("chosen (lam gauge-fixed to 1):", good)

# substitute and store exact Fraction tensor
SUB = {x: good.get(x, None) for x in SYMS}
for k, v in SUB.items():
    assert v is not None and v.is_number, (k, v)

TEN = {}
for (p, q), d in BR.items():
    row = {}
    for k, v in d.items():
        val = sp.nsimplify(sp.expand(v.subs(good)))
        if val != 0:
            r = sp.Rational(val)
            row[k] = F(r.p, r.q)
    if row:
        TEN[(p, q)] = row

pickle.dump({"tensor": TEN, "scalars": {str(k): str(v) for k, v in good.items()}},
            open(os.path.join(HERE, "my_bs_tensor.pkl"), "wb"))
print("saved my_bs_tensor.pkl ; scalars:", {str(k): str(v) for k, v in good.items()})
