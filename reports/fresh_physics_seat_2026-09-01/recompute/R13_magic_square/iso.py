"""R13 — MY OWN isomorphism  my-BS-algebra  ->  the build (B854 E6 Chevalley over Q).

Build side re-implemented from B854's DEFINITION (Cartan matrix + epsilon cocycle);
this is the object under test, not B904's verification code. Full Jacobi on the build
is checked here too (B854 itself only sampled 4000 triples).

Method (mine, no B904 generator map used):
  * my side: Chevalley generators from my root data (roots.py), Bourbaki-ordered
  * build side: generators from its simple roots directly
  * extend by identical bracket words (BFS to a basis), phi = W2 W1^{-1}
  * verify phi([a,b]) = [phi a, phi b] on ALL C(78,2) = 3003 unordered basis pairs
  * planted-negative control: a deliberately wrong generator scaling must FAIL
"""
from fractions import Fraction as F
import pickle, os, json, itertools, math
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
NB = 78

# ================= build side (re-implemented from B854's definition) =============
CB = [[2, 0, -1, 0, 0, 0],
      [0, 2, 0, -1, 0, 0],
      [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0],
      [0, 0, 0, -1, 2, -1],
      [0, 0, 0, 0, -1, 2]]
N6 = 6
from itertools import product

def ip(a, b):
    return sum(a[i] * b[j] * CB[i][j] for i in range(N6) for j in range(N6))

pos = [tuple(a) for a in product(range(4), repeat=N6) if any(a) and ip(a, a) == 2]
ROOTS_B = pos + [tuple(-x for x in a) for a in pos]
IDX_B = {r: k for k, r in enumerate(ROOTS_B)}
assert len(pos) == 36

E0 = [[0] * N6 for _ in range(N6)]
for i in range(N6):
    for j in range(N6):
        E0[i][j] = -1 if i == j else ((-1) ** CB[i][j] if i < j else 1)

def eps(a, b):
    s = 1
    for i in range(N6):
        if a[i] == 0:
            continue
        for j in range(N6):
            if b[j] == 0:
                continue
            if E0[i][j] == -1 and (a[i] * b[j]) % 2:
                s = -s
    return s

def build_bracket_basis(p, q):
    out = [F(0)] * NB
    if p < N6 and q < N6:
        return out
    if p < N6:
        b = ROOTS_B[q - N6]
        out[q] = F(sum(b[j] * CB[p][j] for j in range(N6)))
        return out
    if q < N6:
        a = ROOTS_B[p - N6]
        out[p] = F(-sum(a[j] * CB[q][j] for j in range(N6)))
        return out
    a, b = ROOTS_B[p - N6], ROOTS_B[q - N6]
    s = tuple(a[i] + b[i] for i in range(N6))
    if all(v == 0 for v in s):
        sg = eps(a, tuple(-v for v in a))
        for i in range(N6):
            out[i] = F(sg * a[i])
        return out
    if s in IDX_B:
        out[N6 + IDX_B[s]] = F(eps(a, b))
    return out

CBLD = np.zeros((NB, NB, NB), dtype=np.int64)
for p in range(NB):
    for q in range(NB):
        row = build_bracket_basis(p, q)
        for k, v in enumerate(row):
            if v:
                assert v.denominator == 1
                CBLD[p, q, k] = int(v)

# full Jacobi on the build
T1 = np.einsum('bdc,ace->abde', CBLD, CBLD)
J = T1 + T1.transpose(1, 2, 0, 3) + T1.transpose(2, 0, 1, 3)
nz = J.any(axis=3)
bad = sum(1 for a in range(NB) for b in range(a+1, NB) for c in range(b+1, NB) if nz[a, b, c])
print("BUILD full Jacobi over 76,076 unordered triples: failures =", bad)
assert bad == 0
assert np.array_equal(CBLD, -CBLD.transpose(1, 0, 2))
np.save(os.path.join(HERE, "build_C_int.npy"), CBLD)

# ================= my side =================
C1 = np.load(os.path.join(HERE, "my_C_int.npy"))  # scaled by 2
DEN1 = 2
R = pickle.load(open(os.path.join(HERE, "my_roots.pkl"), "rb"))
ROOTS_MY = [(tuple(sp.Rational(x) for x in r), [sp.Rational(c) for c in v]) for r, v in R["ROOTS"]]
SIMPLE = [tuple(sp.Rational(x) for x in r) for r in R["SIMPLE"]]
perm = R["perm"]  # my simple idx for Bourbaki node i
HBAS = R["HBAS"]

def br1(u, v):
    """bracket in my algebra, exact rational vectors (lists of sp.Rational)."""
    un = np.array([[x.p, x.q] for x in u], dtype=object)
    out = [sp.Integer(0)] * NB
    for p in range(NB):
        if u[p] == 0:
            continue
        for q in range(NB):
            if v[q] == 0:
                continue
            col = C1[p, q]
            cpq = u[p] * v[q]
            for k in range(NB):
                if col[k]:
                    out[k] += cpq * sp.Rational(int(col[k]), DEN1)
    return out

def br2(u, v):
    out = [sp.Integer(0)] * NB
    for p in range(NB):
        if u[p] == 0:
            continue
        for q in range(NB):
            if v[q] == 0:
                continue
            col = CBLD[p, q]
            cpq = u[p] * v[q]
            for k in range(NB):
                if col[k]:
                    out[k] += cpq * sp.Integer(int(col[k]))
    return out

rdict = {r: v for r, v in ROOTS_MY}

def alpha_of(h_vec, r):
    """value of root r on torus element h (h in span of HBAS with coeffs known)."""
    raise NotImplementedError

# torus functional: my ROOTS store alpha(h_t) for the 6 HBAS elements.
rfun = {r: r for r, _ in ROOTS_MY}  # root tuple IS (alpha(h_1..h_6))

E1, F1_, H1 = [], [], []
for i in range(6):
    al = SIMPLE[perm[i]]
    neg = tuple(-x for x in al)
    ev = rdict[al]
    fv = rdict[neg]
    h = br1(ev, fv)
    # h must be in torus; alpha(h): express h in HBAS coords
    # solve h = sum_t c_t HBAS_t
    A = sp.Matrix([[sp.Rational(HBAS[t][k].numerator, HBAS[t][k].denominator)
                    for t in range(6)] for k in range(NB)])
    b = sp.Matrix([h[k] for k in range(NB)])
    sol = A.solve_least_squares(b) if False else sp.Matrix(sp.linsolve((A, b)).args[0])
    resid = A * sol - b
    assert all(x == 0 for x in resid)
    alh = sum(sol[t] * al[t] for t in range(6))  # alpha(h) = sum c_t alpha(h_t)
    assert alh != 0
    scale = sp.Rational(2) / alh
    fv = [scale * x for x in fv]
    h = [scale * x for x in h]
    E1.append(ev)
    F1_.append(fv)
    H1.append(h)
    # checks: [h,e]=2e, [h,f]=-2f
    assert br1(h, ev) == [2 * x for x in ev]
    assert br1(h, fv) == [-2 * x for x in fv]
print("my side: 6 sl2 triples normalized")
# cross-check Cartan integers: [h_i, e_j] = CB[i][j] e_j
for i in range(6):
    for j in range(6):
        assert br1(H1[i], E1[j]) == [sp.Integer(CB[i][j]) * x for x in E1[j]]
print("my side: Cartan action verified against Bourbaki E6 matrix")

E2, F2_, H2 = [], [], []
for i in range(6):
    u = [0] * N6
    u[i] = 1
    ev = [sp.Integer(0)] * NB
    ev[N6 + IDX_B[tuple(u)]] = sp.Integer(1)
    fv = [sp.Integer(0)] * NB
    fv[N6 + IDX_B[tuple(-x for x in u)]] = sp.Integer(1)
    h = br2(ev, fv)
    # alpha_i(h) with h = sum c_t h_t : alpha_i(h_t) = CB[t][i]
    alh = sum(h[t] * sp.Integer(CB[t][i]) for t in range(N6))
    scale = sp.Rational(2) / alh
    fv = [scale * x for x in fv]
    h = [scale * x for x in h]
    assert br2(h, ev) == [2 * x for x in ev]
    assert br2(h, fv) == [-2 * x for x in fv]
    E2.append(ev)
    F2_.append(fv)
    H2.append(h)
for i in range(6):
    for j in range(6):
        assert br2(H2[i], E2[j]) == [sp.Integer(CB[i][j]) * x for x in E2[j]]
print("build side: 6 sl2 triples normalized, Cartan action verified")

# ================= extend by identical bracket words =================
GEN1 = E1 + F1_
GEN2 = E2 + F2_

basis1 = []  # list of vectors (sympy rationals)
basis2 = []
Mrref = None

def rank_of(vecs):
    A = sp.Matrix([[v[k] for k in range(NB)] for v in vecs])
    return A.rank()

# seed with generators + h's
cand1 = GEN1 + H1
cand2 = GEN2 + H2
sel1, sel2 = [], []
Acur = sp.zeros(0, NB)
r = 0
def try_add(v1, v2):
    global Acur, r
    A2 = Acur.col_join(sp.Matrix([[x for x in v1]]))
    r2 = A2.rank()
    if r2 > r:
        Acur = A2
        r = r2
        sel1.append(v1)
        sel2.append(v2)
        return True
    return False

for v1, v2 in zip(cand1, cand2):
    try_add(v1, v2)
print("rank after generators+h:", r)

frontier1 = list(sel1)
frontier2 = list(sel2)
while r < NB:
    new1, new2 = [], []
    for g1, g2 in zip(GEN1, GEN2):
        for b1v, b2v in zip(frontier1, frontier2):
            w1 = br1(g1, b1v)
            if all(x == 0 for x in w1):
                continue
            w2 = br2(g2, b2v)
            if try_add(w1, w2):
                new1.append(w1)
                new2.append(w2)
                if r == NB:
                    break
        if r == NB:
            break
    assert new1, "BFS stalled before reaching full rank"
    frontier1, frontier2 = new1, new2
    print("  rank:", r)
print("basis built by identical words: rank", r)

W1 = sp.Matrix([[v[k] for k in range(NB)] for v in sel1]).T  # columns = basis1
W2 = sp.Matrix([[v[k] for k in range(NB)] for v in sel2]).T
PHI = W2 * W1.inv()
print("phi computed; det =", sp.det(PHI))

# ================= verify homomorphism on all 3003 pairs =================
PHIc = [[PHI[i, j] for j in range(NB)] for i in range(NB)]

def phi_vec(v):
    return [sum(PHIc[i][j] * v[j] for j in range(NB) if v[j] != 0) for i in range(NB)]

std = [[sp.Integer(1) if k == i else sp.Integer(0) for k in range(NB)] for i in range(NB)]
PHI_cols = [[PHI[i, j] for i in range(NB)] for j in range(NB)]

mism = 0
checked = 0
for a in range(NB):
    for b in range(a + 1, NB):
        lhs_raw = [sp.Rational(int(C1[a, b, k]), DEN1) for k in range(NB)]
        lhs = phi_vec(lhs_raw)
        rhs = br2(PHI_cols[a], PHI_cols[b])
        checked += 1
        if lhs != rhs:
            mism += 1
print(f"homomorphism check: {checked} pairs, {mism} mismatches")
detphi = sp.det(PHI)

# ================= planted-negative control =================
# corrupt one generator scaling (e_3 -> 2 e_3 on build side) and redo a quick check:
E2b = [list(v) for v in E2]
E2b[2] = [2 * x for x in E2b[2]]
# quick: the extension map with mismatched normalization cannot be a homomorphism;
# test just h_3' = [2e_3, f_3] = 2 h_3 breaks [h,e]=2e scaling chain -> check a few pairs
selb2 = []
Acur2 = sp.zeros(0, NB)
r2v = 0
GEN2b = E2b + F2_
pairs = []
sel1b = []
def try_add2(v1, v2):
    global Acur2, r2v
    A2 = Acur2.col_join(sp.Matrix([[x for x in v1]]))
    rr = A2.rank()
    if rr > r2v:
        Acur2 = A2
        r2v = rr
        sel1b.append(v1)
        selb2.append(v2)
        return True
    return False
cand1b = GEN1 + H1
cand2b = GEN2b + H2
for v1, v2 in zip(cand1b, cand2b):
    try_add2(v1, v2)
f1 = list(sel1b); f2 = list(selb2)
while r2v < NB:
    n1, n2 = [], []
    for g1, g2 in zip(GEN1, GEN2b):
        for b1v, b2v in zip(f1, f2):
            w1 = br1(g1, b1v)
            if all(x == 0 for x in w1):
                continue
            w2 = br2(g2, b2v)
            if try_add2(w1, w2):
                n1.append(w1); n2.append(w2)
                if r2v == NB:
                    break
        if r2v == NB:
            break
    if not n1:
        break
    f1, f2 = n1, n2
ctrl_mism = 0
if r2v == NB:
    W1b = sp.Matrix([[v[k] for k in range(NB)] for v in sel1b]).T
    W2b = sp.Matrix([[v[k] for k in range(NB)] for v in selb2]).T
    PHIb = W2b * W1b.inv()
    PHIb_cols = [[PHIb[i, j] for i in range(NB)] for j in range(NB)]
    PHIbc = [[PHIb[i, j] for j in range(NB)] for i in range(NB)]
    import random
    random.seed(3)
    for _ in range(60):
        a = random.randrange(NB); b = random.randrange(NB)
        if a == b:
            continue
        lhs_raw = [sp.Rational(int(C1[a, b, k]), DEN1) for k in range(NB)]
        lhs = [sum(PHIbc[i][j] * lhs_raw[j] for j in range(NB) if lhs_raw[j] != 0) for i in range(NB)]
        rhs = br2(PHIb_cols[a], PHIb_cols[b])
        if lhs != rhs:
            ctrl_mism += 1
print("planted-negative control (corrupted generator): mismatches on 60 random pairs =", ctrl_mism, "(must be > 0)")

res = dict(build_jacobi_failures=int(bad), pairs_checked=checked, mismatches=mism,
           det_phi=str(detphi), control_mismatches=ctrl_mism)
json.dump(res, open(os.path.join(HERE, "my_iso_result.json"), "w"), indent=1)
pickle.dump({"PHI": [[str(PHI[i, j]) for j in range(NB)] for i in range(NB)]},
            open(os.path.join(HERE, "my_phi.pkl"), "wb"))
print("RESULT:", res)
assert mism == 0 and ctrl_mism > 0
print("VERDICT: my BS algebra IS isomorphic to the build, by my own explicit phi.")
