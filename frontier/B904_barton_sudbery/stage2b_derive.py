"""B904 stage 2b: DERIVE the equivariant structure instead of guessing.

Action pattern (from the triality identity A(xy) = B(x)y + xC(y)):
  T = (A,B,C) acts on V1 by B, V2 by C, V3 by A.
Cross products: for each slot ((1,2)->3, (2,3)->1, (3,1)->2), test each of
the 8 candidate octonion bilinear forms m for exact equivariance
  comp_target(m(x,y)) = m(comp_src1(x), y) + m(x, comp_src2(y))
over all 28 triality basis triples x 64 basis pairs. Multiplicity-one =>
exactly one candidate (up to scale) should survive per slot.
C'-side analogously (2-dim, cheap).
"""
import os, pickle, json
from fractions import Fraction as F
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "stage1_tri.pkl"), "rb"))
SO = [np.array([[F(x) for x in row] for row in M], dtype=object)
      for M in D["SO"]]
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
    a = a1*a2 + dot(u1, v2)
    u = tuple(a1*u2[i] + b2*u1[i] - cross(v1, v2)[i] for i in range(3))
    v = tuple(a2*v1[i] + b1*v2[i] + cross(u1, u2)[i] for i in range(3))
    b = b1*b2 + dot(v1, u2)
    return (a,) + u + v + (b,)
def oconj(x):
    tr = x[0] + x[7]
    return (tr - x[0], -x[1], -x[2], -x[3], -x[4], -x[5], -x[6], tr - x[7])
E8 = [tuple(F(1) if i == j else F(0) for j in range(8)) for i in range(8)]

CANDS = {
    "xy":    lambda x, y: omul(x, y),
    "yx":    lambda x, y: omul(y, x),
    "cx_y":  lambda x, y: omul(oconj(x), y),
    "x_cy":  lambda x, y: omul(x, oconj(y)),
    "cxcy":  lambda x, y: omul(oconj(x), oconj(y)),
    "cycx":  lambda x, y: omul(oconj(y), oconj(x)),
    "y_cx":  lambda x, y: omul(y, oconj(x)),
    "cy_x":  lambda x, y: omul(oconj(y), x),
}
# action components per summand: V1 <- B(=idx1), V2 <- C(=idx2), V3 <- A(=idx0)
ACT = {0: 1, 1: 2, 2: 0}
def act(M, x):
    return tuple(sum(M[i][j]*x[j] for j in range(8)) for i in range(8))

SLOTS = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
found = {}
for (i, j, k) in SLOTS:
    ok = []
    for name, m in CANDS.items():
        good = True
        for t in range(nso):
            Ti, Tj, Tk = TA[t][ACT[i]], TA[t][ACT[j]], TA[t][ACT[k]]
            for a in range(8):
                for b in range(8):
                    lhs = act(Tk, m(E8[a], E8[b]))
                    rhs = tuple(m(act(Ti, E8[a]), E8[b])[z]
                                + m(E8[a], act(Tj, E8[b]))[z] for z in range(8))
                    if lhs != rhs: good = False; break
                if not good: break
            if not good: break
        if good: ok.append(name)
    found[f"({i+1},{j+1})->({k+1})"] = ok
    print(f"slot ({i+1},{j+1})->{k+1}: equivariant products = {ok}", flush=True)
json.dump(found, open(os.path.join(HERE, "stage2b_products.json"), "w"),
          indent=1)
print("saved", flush=True)
