"""B904 stage 1: construct L(O_split, C_split) explicitly over Q.

Split octonions via Zorn vector matrices: x = [[a, u], [v, b]], a,b in Q,
u,v in Q^3; product (a1,u1,v1,b1)*(a2,u2,v2,b2) =
  (a1a2 + u1.v2, a1u2 + b2u1 - v1 x v2, a2v1 + b1v2 + u1 x u2, b1b2 + v1.u2)
Norm N(x) = ab - u.v (split). Basis: 8 units.
Triality Lie algebra: tri = {(A,B,C) in gl(8)^3 : A(xy) = B(x)y + x C(y)},
with each component constrained to so(N) (the norm's orthogonal algebra).
Expect dim 28. BS bracket on L = tri + (O x C')_1,2,3 with C' = R+R giving
each summand O x 2. Free scalars in [x_i, y_j] -> z_k and [x_i, y_i] -> tri
are FIT by imposing Jacobi on a probe set, then Jacobi verified on a large
random exact sample.
"""
import itertools, json, os
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

def omul(x, y):
    a1, u1, v1, b1 = x[0], x[1:4], x[4:7], x[7]
    a2, u2, v2, b2 = y[0], y[1:4], y[4:7], y[7]
    a = a1*a2 + dot(u1, v2)
    u = tuple(a1*u2[i] + b2*u1[i] - cross(v1, v2)[i] for i in range(3))
    v = tuple(a2*v1[i] + b1*v2[i] + cross(u1, u2)[i] for i in range(3))
    b = b1*b2 + dot(v1, u2)
    return (a,) + u + v + (b,)

E = [tuple(F(1) if i == j else F(0) for j in range(8)) for i in range(8)]
MT = [[omul(E[i], E[j]) for j in range(8)] for i in range(8)]
# norm bilinear form: N(x) = x0*x7 - x1x4 - x2x5 - x3x6 ; polarize
G = sp.zeros(8, 8)
G[0, 7] = G[7, 0] = sp.Rational(1, 2)
for i in (1, 2, 3):
    G[i, i+3] = G[i+3, i] = sp.Rational(-1, 2)

# so(N) = {A : A^T G + G A = 0}, dim 28
Asym = sp.symbols(f"a0:64")
Amat = sp.Matrix(8, 8, Asym)
cond = Amat.T*G + G*Amat
sols = sp.solve([c for c in cond], Asym, dict=True)[0]
free = sorted({s for s in Asym} - set(sols), key=lambda s: int(str(s)[1:]))
SO = []
for f_ in free:
    M = Amat.subs(sols).subs([(g, 0) for g in free if g != f_]).subs(f_, 1)
    SO.append(np.array([[F(int(M[i, j])) if M[i, j].is_Integer else F(str(M[i, j]))
                         for j in range(8)] for i in range(8)], dtype=object))
print("dim so(N):", len(SO), flush=True)

# triality: A(xy) = B(x)y + x C(y) with A,B,C in so(N)
# unknowns: coefficients of B and C in the SO basis given A in SO basis:
# solve the big linear system for (a, b, c) coefficient triples
nso = len(SO)
def act(M, x):
    return tuple(sum(M[i][j]*x[j] for j in range(8)) for i in range(8))
rows = []
# equation per (basis x, basis y, component k): sum_a alpha_a A_a(x*y)_k
#  - sum_b beta_b (B_b(x)*y)_k - sum_c gamma_c (x*C_c(y))_k = 0
cols = 3*nso
eqrows = []
for xi in range(8):
    for yi in range(8):
        xy = MT[xi][yi]
        for k in range(8):
            row = [F(0)]*cols
            for a in range(nso):
                row[a] = act(SO[a], xy)[k]
            for b_ in range(nso):
                row[nso + b_] = -omul(act(SO[b_], E[xi]), E[yi])[k]
            for c in range(nso):
                row[2*nso + c] = -omul(E[xi], act(SO[c], E[yi]))[k]
            eqrows.append(row)
Msys = sp.Matrix([[sp.Rational(x) for x in r] for r in eqrows])
NS = Msys.nullspace()
print("dim tri(O):", len(NS), flush=True)
json.dump({"dim_soN": nso, "dim_tri": len(NS)},
          open(os.path.join(HERE, "stage1_dims.json"), "w"), indent=1)
# persist the triality triples
TRI = []
for v in NS:
    al = [sp.Rational(v[a]) for a in range(nso)]
    be = [sp.Rational(v[nso + a]) for a in range(nso)]
    ga = [sp.Rational(v[2*nso + a]) for a in range(nso)]
    TRI.append((al, be, ga))
import pickle
pickle.dump({"SO": [[[str(SO[a][i][j]) for j in range(8)] for i in range(8)]
                    for a in range(nso)],
             "TRI": [[[str(x) for x in comp] for comp in t] for t in TRI]},
            open(os.path.join(HERE, "stage1_tri.pkl"), "wb"))
print("saved", flush=True)
