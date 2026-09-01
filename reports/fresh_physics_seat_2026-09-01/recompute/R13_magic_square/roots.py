"""R13 blind — rational torus, root decomposition, Cartan matrix, E6 match.

Torus: {T in tri(O) : A diagonal in Zorn basis} (expect dim 4)  +  tri(C') (dim 2).
Split all 78 dims into joint ad-eigenspaces over Q. Expect 72 one-dim root spaces
+ 6-dim zero space (the torus itself = Cartan).
"""
from fractions import Fraction as F
import pickle, os, itertools, json
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "my_tri.pkl"), "rb"))
TRIO, TRIC = D["triO"], D["triC"]
C = np.load(os.path.join(HERE, "my_C_int.npy"))  # scaled by den=2
DEN = 2
NB = 78

# ---- torus: tri(O) elements with A diagonal ----
# coordinates: coefficient vectors c in Q^28 with sum_m c_m * A_m offdiag = 0
rows = []
for r in range(8):
    for cc in range(8):
        if r == cc:
            continue
        rows.append([TRIO[m][0][r][cc] for m in range(28)])
M = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in rows])
ns = M.nullspace()
print("diagonal-A subspace of tri(O): dim", len(ns))
assert len(ns) == 4

def tri_coef_to_L(coefs, off):
    v = [F(0)] * NB
    for m, c in enumerate(coefs):
        q = sp.Rational(c)
        if q != 0:
            v[off + m] = F(q.p, q.q)
    return v

HBAS = []  # torus basis as vectors in L
for nsv in ns:
    HBAS.append(tri_coef_to_L(list(nsv), 0))
for m in range(2):
    v = [F(0)] * NB
    v[28 + m] = F(1)
    HBAS.append(v)
print("torus dim:", len(HBAS))

# ad matrices (exact, rational): ad_h[k][q] = coeff of e_k in [h, e_q]
def admat(v):
    A = [[F(0)] * NB for _ in range(NB)]
    for p, cp in enumerate(v):
        if cp == 0:
            continue
        for q in range(NB):
            col = C[p, q]  # scaled by DEN
            for k in range(NB):
                if col[k]:
                    A[k][q] += cp * F(int(col[k]), DEN)
    return A

ADH = [admat(h) for h in HBAS]

# check torus abelian: [h_i, h_j] = 0
for i in range(6):
    for j in range(6):
        w = [sum(ADH[i][k][q] * HBAS[j][q] for q in range(NB)) for k in range(NB)]
        assert all(x == 0 for x in w), "torus not abelian!"
print("torus abelian: OK")

# ---- joint eigenspaces ----
# generic combination, float eigenvalues -> rational candidates -> exact nullspaces
coefs = [17, 291, 5043, 87381, 1514229, 26244099]  # ~17^k spread; avoids root collisions
Hgen = [[sum(coefs[t] * ADH[t][r][c] for t in range(6)) for c in range(NB)] for r in range(NB)]
Hf = np.array([[float(x) for x in row] for row in Hgen])
ev = np.linalg.eigvals(Hf)
evr = sorted(set(F(round(x.real * 4), 4) for x in ev))
print("distinct float eigenvalues (rounded to quarters):", len(evr))

Hsp = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in Hgen])
root_spaces = []
zero_space = None
tot = 0
for lam in evr:
    lam_r = sp.Rational(lam.numerator, lam.denominator)
    nsp = (Hsp - lam_r * sp.eye(NB)).nullspace()
    if not nsp:
        continue
    tot += len(nsp)
    if lam_r == 0:
        zero_space = nsp
    else:
        for v in nsp:
            root_spaces.append((lam_r, v))
print("total eigenvector count:", tot, " zero-space dim:", len(zero_space) if zero_space else 0,
      " nonzero root vectors:", len(root_spaces))
assert tot == NB, "generic combo not diagonalizable over these rationals"
assert len(zero_space) == 6 and len(root_spaces) == 72

# roots as functionals: alpha(h_t) for each torus basis element
ADHsp = [sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A]) for A in ADH]
ROOTS = []
for lam_r, v in root_spaces:
    al = []
    for t in range(6):
        w = ADHsp[t] * v
        # w = alpha_t * v
        idx = next(i for i in range(NB) if v[i] != 0)
        at = sp.Rational(w[idx] / v[idx])
        assert w == at * v, "not a joint eigenvector"
        al.append(at)
    ROOTS.append((tuple(al), v))
print("all 72 joint root vectors verified 1-dim rational")

# closed under negation?
rset = set(r for r, _ in ROOTS)
assert all(tuple(-x for x in r) in rset for r in rset)
print("root set closed under negation: OK")

# ---- Killing form on torus, inner products, Cartan matrix ----
Kt = sp.Matrix(6, 6, lambda i, j: (ADHsp[i] * ADHsp[j]).trace())
Kti = Kt.inv()
def iprod(a, b):
    va = sp.Matrix(list(a)); vb = sp.Matrix(list(b))
    return (va.T * Kti * vb)[0, 0]

# positivity by generic functional
wgt = [sp.Rational(x) for x in (101, 53, 29, 17, 7, 3)]
def height(r):
    return sum(w * x for w, x in zip(wgt, r))
POS = [r for r, _ in ROOTS if height(r) > 0]
assert len(POS) == 36
possert = set(POS)
SIMPLE = []
for r in POS:
    dec = False
    for s in POS:
        if s != r:
            t = tuple(a - b for a, b in zip(r, s))
            if t in possert:
                dec = True
                break
    if not dec:
        SIMPLE.append(r)
print("simple roots:", len(SIMPLE))
assert len(SIMPLE) == 6

CM = sp.Matrix(6, 6, lambda i, j: 2 * iprod(SIMPLE[i], SIMPLE[j]) / iprod(SIMPLE[j], SIMPLE[j]))
print("my Cartan matrix:")
sp.pprint(CM)

# match against standard E6 (Bourbaki):
E6 = sp.Matrix([[2, 0, -1, 0, 0, 0],
                [0, 2, 0, -1, 0, 0],
                [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0],
                [0, 0, 0, -1, 2, -1],
                [0, 0, 0, 0, -1, 2]])
perm_found = None
for perm in itertools.permutations(range(6)):
    if all(CM[perm[i], perm[j]] == E6[i, j] for i in range(6) for j in range(6)):
        perm_found = perm
        break
print("E6 match permutation (my simple idx for Bourbaki node i):", perm_found)
assert perm_found is not None, "NOT E6!"

out = {
    "torus_dim": 6, "n_roots": 72, "n_pos": 36, "n_simple": 6,
    "cartan": [[int(CM[i, j]) for j in range(6)] for i in range(6)],
    "e6_perm": list(perm_found),
    "simple_roots": [[str(x) for x in r] for r in SIMPLE],
}
json.dump(out, open(os.path.join(HERE, "my_roots.json"), "w"), indent=1)
pickle.dump({"HBAS": HBAS, "ROOTS": [(tuple(str(x) for x in r), [str(sp.Rational(v[i])) for i in range(NB)])
                                     for r, v in ROOTS],
             "SIMPLE": [tuple(str(x) for x in r) for r in SIMPLE],
             "perm": perm_found},
            open(os.path.join(HERE, "my_roots.pkl"), "wb"))
print("VERDICT: root system is E6 (72 roots, Cartan matrix matched). saved my_roots.*")
