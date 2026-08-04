"""B904 stage 2: the full BS bracket on L = tri(O) + tri(C') + sum_i (O x C')_i
over Q, with free normalization scalars FIT by Jacobi, then Jacobi verified
in full (all basis triples, exact integer arithmetic).

Basis (dim 78): tri(O) 28 | tri(C') 2 | three summands 16 each.
C' = split complex (z+, z-), N(z) = z+ z-.
tri(C') = {(diag scalings)}: S = (s1, s2) acting on summand i by the
theta^{i-1}-shifted component pattern (a, b, c) with a = s1+s2? -- realized
below directly as the 2-dim abelian algebra acting diagonally with charges
fit by the triality identity for C'.
"""
import itertools, os, pickle, json
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "stage1_tri.pkl"), "rb"))
SO = [np.array([[F(x) for x in row] for row in M], dtype=object)
      for M in D["SO"]]
TRI = [tuple([F(x) for x in comp] for comp in t) for t in D["TRI"]]
nso = len(SO)

def somat(coeffs):
    M = np.zeros((8, 8), dtype=object); M[:] = F(0)
    for a, c in enumerate(coeffs):
        if c: M = M + np.array(SO[a], dtype=object)*c
    return M

# triality triples as matrix triples
TA = [tuple(somat(t[k]) for k in range(3)) for t in TRI]
# projection tri -> component-1 coefficient matrix (28x28) and its inverse:
P1 = sp.Matrix([[TRI[t][0][a] for t in range(nso)] for a in range(nso)])
P1inv = P1.inv()

def tri_from_c1(coeffs1):
    """the unique triality triple with first component = sum coeffs1*SO."""
    v = P1inv * sp.Matrix(coeffs1)
    return [sp.Rational(x) for x in v]

# octonion data
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
def oconj(x):  # xbar = 2<x,1> - x : <x,1> = (x0+x7)/2 for split basis
    tr = x[0] + x[7]
    return (tr - x[0], -x[1], -x[2], -x[3], -x[4], -x[5], -x[6], tr - x[7])
E8 = [tuple(F(1) if i == j else F(0) for j in range(8)) for i in range(8)]
# bilinear pairing <x,y> = (N(x+y)-N(x)-N(y))/2 with N = x0 x7 - x1x4-x2x5-x3x6
def opair(x, y):
    return (x[0]*y[7] + x[7]*y[0]
            - x[1]*y[4] - x[4]*y[1] - x[2]*y[5] - x[5]*y[2]
            - x[3]*y[6] - x[6]*y[3]) / 2

# t_{x,y} in tri(O): first component S_xy = 2(<x,.>y - <y,.>x) as so(N) matrix
def S_xy(x, y):
    M = np.zeros((8, 8), dtype=object); M[:] = F(0)
    for j in range(8):
        col = tuple(F(1) if i == j else F(0) for i in range(8))
        px = opair(x, col); py = opair(y, col)
        for i in range(8):
            M[i][j] = 2*(px*y[i] - py*x[i])
    return M
# coeffs of an so(N) matrix in the SO basis (solve linear system once)
SOcols = sp.Matrix([[SO[a][i][j] for a in range(nso)]
                    for i in range(8) for j in range(8)])
SOpinv = (SOcols.T*SOcols).inv()*SOcols.T
def so_coeffs(M):
    v = sp.Matrix([M[i][j] for i in range(8) for j in range(8)])
    return [sp.Rational(x) for x in SOpinv*v]

# C' data: z = (z+, z-); zbar = (z-, z+)? conjugation swaps for split C'
def cmul(z, w): return (z[0]*w[0], z[1]*w[1])
def cconj(z): return (z[1], z[0])
def cpair(z, w): return (z[0]*w[1] + z[1]*w[0]) / 2
E2 = [(F(1), F(0)), (F(0), F(1))]

# ---- basis of L ----
# indices: 0..27 tri(O) | 28,29 tri(C') | 30+16*(i)+(8*c + o) for summand i,
#   octonion unit o, C'-unit c
def sidx(i, o, c): return 30 + 16*i + 8*c + o
DIM = 78

# tri(C') realized as pairs (p, q): acts on (x tensor z)_i by charge
# pattern chi_i(p,q) * z-component-wise; the triality identity for C' forces
# the three patterns to be theta-shifts of ((p,q),(q,?)...): we FIT the three
# diagonal actions with unknowns and let Jacobi decide.
lam = {k: sp.Symbol(f"lam{k}") for k in range(3)}      # cross-bracket scales
mu  = {k: sp.Symbol(f"mu{k}") for k in range(3)}       # same-summand -> tri(O)
nu  = {k: sp.Symbol(f"nu{k}") for k in range(3)}       # same-summand -> tri(C')
# tri(C') action charges on summand i for basis element t1=(1,-1)-type:
# take tri(C') basis u1 acting on z=(z+,z-) in summand i as
#   (a_i z+, -a_i z-) and u2 as (b_i z+, -b_i z-) -- but two independent
# diagonal actions on three summands: 6 unknowns per generator is too free;
# BS says: tri(C') = {(A,B,C) : A(zw) = B(z)w + z C(w), each = diag(s,-s)}.
# Solve that tiny triality directly:
s1, s2, s3 = sp.symbols("s1 s2 s3")
# A = diag(sA, -sA) etc: A(zw) = B(z)w + zC(w) on units:
# (1,0)*(1,0) = (1,0): sA = sB + sC ; (0,1)*(0,1) = (0,1): -sA = -sB - sC (same)
# (1,0)*(0,1) = 0: no condition. So tri(C') = {(sB+sC, sB, sC)}: 2-dim. Good.
# Basis: T1' = (1,1,0), T2' = (1,0,1)  (values (sA,sB,sC))
TCP = [(1, 1, 0), (1, 0, 1)]
# action on summand i uses the theta^{i-1} shift of (A,B,C): summand 1 gets B
# acting... BS: [T, (x z)_i] = (theta^{i-1}T)_1-component? For the O side we
# use component i of the triple on summand i; mirror for C'.
def tri_c_charge(gen, i):
    sA, sB, sC = TCP[gen]
    comp = (sA, sB, sC)[i]     # component i acts on summand i
    return comp                # acting as diag(comp, -comp) on (z+, z-)

# bracket tensor with symbolic scalars (sparse dict)
from collections import defaultdict
BR = defaultdict(lambda: sp.Integer(0))   # (a,b,k) -> coeff, a<b antisym later

def add(a, b, k, val):
    if val == 0: return
    BR[(a, b, k)] += val

# [tri(O)_a, tri(O)_b] : componentwise commutator, expressed via component 1
for a in range(nso):
    for b in range(a+1, nso):
        C1 = TA[a][0] @ TA[b][0] - TA[b][0] @ TA[a][0]
        for t, c in enumerate(tri_from_c1(so_coeffs(C1))):
            add(a, b, t, c)
# [tri(O), tri(C')] = 0
# [tri(O)_a, (x z)_i]: component i acts on x
for a in range(nso):
    for i in range(3):
        for o in range(8):
            Ax = TA[a][i] @ np.array(E8[o], dtype=object)
            for c in range(2):
                for oo in range(8):
                    if Ax[oo]:
                        add(a, sidx(i, o, c), sidx(i, oo, c), sp.Rational(Ax[oo]))
# [tri(C')_g, (x z)_i]: charge on z
for g in range(2):
    for i in range(3):
        ch = tri_c_charge(g, i)
        for o in range(8):
            for c in range(2):
                add(28 + g, sidx(i, o, c), sidx(i, o, c),
                    sp.Integer(ch if c == 0 else -ch))
# cross: [(x z)_i, (y w)_j] -> summand k; the octonion product FORM and the
# C'-conjugation choice are discrete conventions scanned via env OPROD/CCONJ
OPROD = os.environ.get("OPROD", "cxy")   # xy | yx | cxcy | cycx | cxy(=conj(xy))
CCONJ = os.environ.get("CCONJ", "conj")  # conj | plain
def oprod(x, y):
    if OPROD == "xy":   return omul(x, y)
    if OPROD == "yx":   return omul(y, x)
    if OPROD == "cxcy": return omul(oconj(x), oconj(y))
    if OPROD == "cycx": return omul(oconj(y), oconj(x))
    if OPROD == "cxy":  return oconj(omul(x, y))
    raise ValueError(OPROD)
def cprod(z, w):
    if CCONJ == "conj": return cmul(cconj(z), cconj(w))
    return cmul(z, w)
for i in range(3):
    j = (i + 1) % 3; k = (i + 2) % 3
    for o1 in range(8):
        for o2 in range(8):
            prod = oprod(E8[o1], E8[o2])
            for c1 in range(2):
                for c2 in range(2):
                    cz = cprod(E2[c1], E2[c2])
                    for oo in range(8):
                        for cc in range(2):
                            v = prod[oo]*cz[cc]
                            if v:
                                add(sidx(i, o1, c1), sidx(j, o2, c2),
                                    sidx(k, oo, cc), lam[i]*sp.Rational(v))
# same-summand: [(x z)_i, (y w)_i] = mu_i <z,w> t_xy^(i) + nu_i <x,y> s_zw^(i)
# t_xy^(i): the triality triple whose i-th component is S_xy;
# use theta-rotation: triple with comp i = S means first-comp = theta^{-i}...
# we have tri_from_c1; build "tri_from_ci" via permuting: the triple
# (A,B,C) with comp i prescribed = apply tri_from_c1 to the rotated algebra.
Pi = {0: P1}
for i in (1, 2):
    Pi[i] = sp.Matrix([[TRI[t][i][a] for t in range(nso)] for a in range(nso)])
Piinv = {i: Pi[i].inv() for i in range(3)}
def tri_from_ci(coeffs, i):
    v = Piinv[i] * sp.Matrix(coeffs)
    return [sp.Rational(x) for x in v]
# s_zw in tri(C'): the triple with i-th C'-component = the generator of the
# action <z,.>w - <w,.>z on C' (1-dim so): S_zw = diag(s, -s) with
# s = z+ w- - z- w+ (times pairing normalization 2*(1/2)=1)
def s_zw_val(z, w):
    return z[0]*w[1] - z[1]*w[0]
# express diag(s,-s) at component i as combo of TCP basis: need (sA,sB,sC)
# with comp i = s and the OTHER components determined by tri(C') structure:
# tri(C') is 2-dim; the triples with comp i = s form a 1-param family --
# BS fixes the choice via the dual pairing; we FIT: parametrize the choice
# as the unique triple orthogonal-complement choice: use basis solve:
kap = {k: sp.Symbol(f"kap{k}") for k in range(3)}
def tcp_from_ci(s, i):
    # affine solve of comp_i(x1,x2) = s in x-coords; the 1-dim kernel of
    # comp_i is a genuine convention freedom -- parametrized by kap_i and
    # FIT by Jacobi with the other scalars (no hand-chosen representative).
    # trip(x1,x2) = (x1+x2, x1, x2) in (sA, sB, sC) coordinates.
    if i == 0:
        part = (sp.Rational(s, 2), sp.Rational(s, 2))   # x1+x2 = s
        kern = (sp.Integer(1), sp.Integer(-1))          # comp0 = 0
    elif i == 1:
        part = (s, sp.Integer(0))                       # x1 = s
        kern = (sp.Integer(0), sp.Integer(1))           # comp1 = 0
    else:
        part = (sp.Integer(0), s)                       # x2 = s
        kern = (sp.Integer(1), sp.Integer(0))           # comp2 = 0
    return [part[0] + kap[i]*kern[0]*s, part[1] + kap[i]*kern[1]*s]
for i in range(3):
    for o1 in range(8):
        for o2 in range(8):
            Sxy = S_xy(E8[o1], E8[o2])
            tco = tri_from_ci(so_coeffs(Sxy), i)
            pxy = opair(E8[o1], E8[o2])
            for c1 in range(2):
                for c2 in range(2):
                    a_, b_ = sidx(i, o1, c1), sidx(i, o2, c2)
                    if a_ >= b_: continue
                    pzw = cpair(E2[c1], E2[c2])
                    if pzw:
                        for t, cf in enumerate(tco):
                            add(a_, b_, t, mu[i]*pzw*cf)
                    sv = s_zw_val(E2[c1], E2[c2])
                    if sv and pxy:
                        co = tcp_from_ci(sv, i)
                        add(a_, b_, 28, nu[i]*pxy*co[0])
                        add(a_, b_, 29, nu[i]*pxy*co[1])
print("symbolic tensor built:", len(BR), "entries", flush=True)
pickle.dump({str(k): sp.sstr(v) for k, v in BR.items()},
            open(os.path.join(HERE, f"stage2_tensor_{OPROD}_{CCONJ}.pkl"), "wb"))
print("saved symbolic tensor", flush=True)
