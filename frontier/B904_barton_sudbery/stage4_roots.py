"""B904 stage 4a: root decomposition of the BS algebra over its rational torus.

H = (diagonal triality triples: 4-dim) + tri(C') (2-dim). Compute the joint
ad-eigendecomposition over Q; expect 72 one-dim rational root spaces + the
6-dim Cartan; then the Cartan matrix of a simple system -- must be E6.
"""
import os, pickle, json
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = pickle.load(open(os.path.join(HERE, "stage2c_tensor.pkl"), "rb"))
DIM = 78
NBR = {}
for kstr, d in RAW.items():
    a, b = eval(kstr)[0], eval(kstr)[1]
    NBR.setdefault((a, b), {})[eval(kstr)[2] if False else None] = None
# reload properly: keys are "(a, b, k)"? check format
NBR = defaultdict(dict)
for kstr, d in RAW.items():
    key = eval(kstr)
    if len(key) == 2:
        a, b = key
        for kk, vv in d.items():
            NBR[(a, b)][int(kk)] = F(vv)
    else:
        a, b, k = key
        NBR[(a, b)][k] = F(d)
def nbr(a, b):
    if a == b: return {}
    if a < b: return NBR.get((a, b), {})
    return {k: -v for k, v in NBR.get((b, a), {}).items()}

def admat(vec):
    """ad of sum_i vec[i] basis_i as dense 78x78 Fractions."""
    M = [[F(0)]*DIM for _ in range(DIM)]
    for i, c in enumerate(vec):
        if not c: continue
        for b in range(DIM):
            for k, v in nbr(i, b).items():
                M[k][b] += c*v
    return M

# --- find the diagonal Cartan inside tri(O) ---
D1 = pickle.load(open(os.path.join(HERE, "stage1_tri.pkl"), "rb"))
SO = [np.array([[F(x) for x in row] for row in M], dtype=object)
      for M in D1["SO"]]
TRI = [tuple([F(x) for x in comp] for comp in t) for t in D1["TRI"]]
nso = len(SO)
def somat(coeffs):
    M = np.zeros((8, 8), dtype=object); M[:] = F(0)
    for a, c in enumerate(coeffs):
        if c: M = M + SO[a]*c
    return M
# solve: combos t of TRI coeffs whose FIRST component is diagonal
rows = []
for a in range(nso):
    A1 = somat(TRI[a][0])
    rows.append([A1[i][j] for i in range(8) for j in range(8) if i != j])
Mo = sp.Matrix([[sp.Rational(x) for x in r] for r in rows]).T
NSo = Mo.nullspace()
print("diagonal Cartan dim in tri(O):", len(NSo), flush=True)
Hvecs = []
for v in NSo:
    vec = [F(0)]*DIM
    for a in range(nso):
        r = sp.Rational(v[a])
        vec[a] = F(r.p, r.q)
    Hvecs.append(vec)
for g in (28, 29):
    vec = [F(0)]*DIM; vec[g] = F(1); Hvecs.append(vec)
print("torus dim:", len(Hvecs), flush=True)

ADH = [admat(h) for h in Hvecs]
# joint eigen decomposition: use sympy over Q on the commuting family
import sympy
A0 = sp.Matrix([[sp.Rational(ADH[0][i][j].numerator, ADH[0][i][j].denominator)
                 for j in range(DIM)] for i in range(DIM)])
# iterative refinement of eigenspaces
spaces = [sp.eye(DIM)]
for idx, AD in enumerate(ADH):
    A = sp.Matrix([[sp.Rational(AD[i][j].numerator, AD[i][j].denominator)
                    for j in range(DIM)] for i in range(DIM)])
    new = []
    for S in spaces:
        # restrict A to col-space of S: solve S * R = A * S
        AS = A * S
        R = (S.T*S).inv() * S.T * AS
        ev = R.eigenvals()
        if len(ev) == 1:
            new.append(S); continue
        for lam_ in ev:
            ker = (R - lam_*sp.eye(R.shape[0])).nullspace()
            if ker:
                cols = [S*k for k in ker]
                new.append(sp.Matrix.hstack(*cols))
    spaces = new
    print(f"after H{idx}: {len(spaces)} joint spaces, dims "
          f"{sorted(S.shape[1] for S in spaces)[:10]}...", flush=True)
dims = sorted(S.shape[1] for S in spaces)
print("final joint spaces:", len(spaces), "dims:", dims, flush=True)

# roots: for each 1-dim space, the 6 eigenvalues
roots = []
for S in spaces:
    if S.shape[1] != 1: continue
    v = S
    al = []
    for AD in ADH:
        A = sp.Matrix([[sp.Rational(AD[i][j].numerator, AD[i][j].denominator)
                        for j in range(DIM)] for i in range(DIM)])
        Av = A*v
        # eigenvalue = ratio at a nonzero coordinate
        nz = next(i for i in range(DIM) if v[i] != 0)
        al.append(sp.Rational(Av[nz], v[nz]))
    roots.append(tuple(al))
print("nonzero roots found:", sum(1 for r in roots if any(r)), flush=True)
json.dump({"n_spaces": len(spaces), "dims": [int(d) for d in dims],
           "n_roots": sum(1 for r in roots if any(r)),
           "roots": [[str(x) for x in r] for r in roots]},
          open(os.path.join(HERE, "stage4_roots.json"), "w"), indent=1)
print("saved", flush=True)
