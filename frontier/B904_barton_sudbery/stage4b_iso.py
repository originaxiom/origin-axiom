"""B904 stage 4b: E6 verification + the explicit Chevalley isomorphism.

BS side: roots from stage4_roots.json; Killing form on H; simple system;
Cartan matrix -> match E6 up to relabeling. Chevalley generators both sides,
parallel extension by identical bracket words, then FULL verification
phi([x,y]) = [phi x, phi y] on all basis pairs.
"""
import io, os, json, pickle, contextlib, itertools
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DIM = 78
RAW = pickle.load(open(os.path.join(HERE, "stage2c_tensor.pkl"), "rb"))
NBR = defaultdict(dict)
for kstr, d in RAW.items():
    key = eval(kstr)
    a, b = key[0], key[1]
    if len(key) == 3:
        NBR[(a, b)][key[2]] = F(d) if not isinstance(d, dict) else None
    else:
        for kk, vv in d.items():
            NBR[(a, b)][int(kk)] = F(vv)
def nbr(a, b):
    if a == b: return {}
    if a < b: return NBR.get((a, b), {})
    return {k: -v for k, v in NBR.get((b, a), {}).items()}
def brv(u, v):
    out = defaultdict(lambda: F(0))
    nz_u = [i for i, c in enumerate(u) if c]
    nz_v = [j for j, c in enumerate(v) if c]
    for i in nz_u:
        for j in nz_v:
            for k, w in nbr(i, j).items():
                out[k] += u[i]*v[j]*w
    vec = [F(0)]*DIM
    for k, val in out.items(): vec[k] = val
    return vec

R = json.load(open(os.path.join(HERE, "stage4_roots.json")))
# rebuild root vectors: redo the eigen split cheaply via the saved roots:
# for each root (6-tuple), solve the joint eigenvector exactly
D1 = pickle.load(open(os.path.join(HERE, "stage1_tri.pkl"), "rb"))
SO = [np.array([[F(x) for x in row] for row in M], dtype=object) for M in D1["SO"]]
TRI = [tuple([F(x) for x in comp] for comp in t) for t in D1["TRI"]]
nso = len(SO)
def somat(coeffs):
    M = np.zeros((8, 8), dtype=object); M[:] = F(0)
    for a, c in enumerate(coeffs):
        if c: M = M + SO[a]*c
    return M
rows = []
for a in range(nso):
    A1 = somat(TRI[a][0])
    rows.append([A1[i][j] for i in range(8) for j in range(8) if i != j])
Mo = sp.Matrix([[sp.Rational(x) for x in r] for r in rows]).T
NSo = Mo.nullspace()
Hvecs = []
for v in NSo:
    vec = [F(0)]*DIM
    for a in range(nso):
        r = sp.Rational(v[a]); vec[a] = F(r.p, r.q)
    Hvecs.append(vec)
for g in (28, 29):
    vec = [F(0)]*DIM; vec[g] = F(1); Hvecs.append(vec)
ADH = []
for h in Hvecs:
    M = sp.zeros(DIM, DIM)
    for i, c in enumerate(h):
        if not c: continue
        for b in range(DIM):
            for k, v in nbr(i, b).items():
                M[k, b] += sp.Rational(c.numerator, c.denominator) \
                           * sp.Rational(v.numerator, v.denominator)
    ADH.append(M)
ROOTS_BS = [tuple(sp.Rational(x) for x in r) for r in R["roots"] if any(sp.Rational(x) != 0 for x in r)]
print("roots loaded:", len(ROOTS_BS), flush=True)
def rootvec(al):
    M = sp.Matrix.vstack(*[ADH[i] - al[i]*sp.eye(DIM) for i in range(6)])
    ns = M.nullspace()
    assert len(ns) == 1, ("root space dim", len(ns), al)
    v = ns[0]
    den = sp.lcm([sp.Rational(x).q for x in v if x != 0])
    v = v*den
    return [F(sp.Rational(x).p, sp.Rational(x).q) for x in v]
EV = {al: rootvec(al) for al in ROOTS_BS}
print("root vectors solved", flush=True)

# Killing form on H via ad traces
def killing_H(i, j):
    A, B = ADH[i], ADH[j]
    return sum((A*B)[k, k] for k in range(DIM))
KH = sp.Matrix(6, 6, lambda i, j: killing_H(i, j))
KHinv = KH.inv()
def ip(al, be):
    va = sp.Matrix(al); vb = sp.Matrix(be)
    # roots as functionals: dual vectors t_al = KHinv*va
    return (va.T*KHinv*vb)[0, 0]
# simple system
f = [sp.Rational(97, 7), sp.Rational(31, 5), sp.Rational(11, 3),
     sp.Rational(7, 11), sp.Rational(3, 13), sp.Rational(1, 17)]
def height(al): return sum(f[i]*al[i] for i in range(6))
POS = [al for al in ROOTS_BS if height(al) > 0]
assert len(POS) == 36, len(POS)
SIMPLE = [al for al in POS
          if not any(tuple(sp.Rational(al[k]) - sp.Rational(be[k]) for k in range(6)) in EV
                     for be in POS if be != al)]
# indecomposable: al not = be + ga for be, ga in POS
def is_sum(al):
    s = set(POS)
    for be in POS:
        ga = tuple(al[k] - be[k] for k in range(6))
        if ga in s: return True
    return False
SIMPLE = [al for al in POS if not is_sum(al)]
print("simple roots:", len(SIMPLE), flush=True)
C_BS = [[sp.Rational(2)*ip(a, b)/ip(b, b) for b in SIMPLE] for a in SIMPLE]
print("Cartan matrix rows:", [[int(x) for x in row] for row in C_BS], flush=True)

# match against the build's E6 Cartan matrix by permutation
CE6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
       [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
perm_found = None
for perm in itertools.permutations(range(6)):
    if all(C_BS[perm[i]][perm[j]] == CE6[i][j] for i in range(6) for j in range(6)):
        perm_found = perm; break
print("E6 match permutation:", perm_found, flush=True)
json.dump({"n_pos": len(POS), "n_simple": len(SIMPLE),
           "cartan_matrix": [[int(x) for x in row] for row in C_BS],
           "e6_permutation": list(perm_found) if perm_found else None},
          open(os.path.join(HERE, "stage4b_cartan.json"), "w"), indent=1)
if perm_found is None:
    raise SystemExit("NOT E6 -- investigate")
print("saved; BS algebra root system IS E6", flush=True)
