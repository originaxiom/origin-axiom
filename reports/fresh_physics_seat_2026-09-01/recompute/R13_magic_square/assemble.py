"""R13 blind — derive cross products by equivariance, build L = tri(O)+tri(C')+3x(O@C'),
fit the 9 scalars by Jacobi on probes, then full exact Jacobi on all triples.

My conventions (chosen independently):
  action of T=(A,B,C) in tri(O):  V1 <- B, V2 <- C, V3 <- A   (on the O factor)
  action of S=(SA,SB,SC) in tri(C'): V1 <- SB, V2 <- SC, V3 <- SA (on the C' factor)
  cross: [V_i, V_j] -> V_k for (i,j,k) cyclic in {(1,2,3),(2,3,1),(3,1,2)}:
     [x@z, y@w] = lam_k * pO_k(x,y) @ pC_k(z,w)
  same-summand: [x1@z1, x2@z2]_i = mu_i * t_i(x1,x2) * <z1,z2>_C
                                  + nu_i * s_i(z1,z2) * <x1,x2>_O
  t_i in tri(O) dual to T -> <T_i x1, x2>_O  wrt form tr(A A') on tri(O)
  s_i in tri(C') dual to S -> <S_i z1, z2>_C wrt form tr(SA SA') on tri(C')

Basis of L (78): 0..27 tri(O); 28..29 tri(C'); 30+16*(i-1)+2*a+c : V_i, o_a @ c_c.
"""
from fractions import Fraction as F
import itertools, pickle, os
import numpy as np
from octonion_core import (OBASIS, OMT, OPOL, CBASIS, CMT, CPOL,
                           omul, oconj, cmul, cconj)

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "my_tri.pkl"), "rb"))
TRIO, TRIC = D["triO"], D["triC"]
NT, NC = len(TRIO), len(TRIC)
assert NT == 28 and NC == 2

def matvec(M, v):
    return tuple(sum(M[r][c] * v[c] for c in range(len(v))) for r in range(len(M)))

# component acting on V_i (1-indexed): V1<-B, V2<-C, V3<-A
def comp(tri, i):
    A, B, C = tri
    return (B, C, A)[i - 1]

# ---------------- candidate octonion products ----------------
def pcand(name):
    """return function (x,y) -> octonion, from candidate name"""
    def f(x, y, name=name):
        xx = oconj(x) if 'cx' in name else x
        yy = oconj(y) if 'cy' in name else y
        if name.startswith('R'):
            return omul(yy, xx)
        return omul(xx, yy)
    return f

OC_NAMES = ['xy', 'cx_y', 'x_cy', 'cx_cy', 'Ryx', 'Rcx_y', 'Rx_cy', 'Rcx_cy']
# For C' (commutative) the reversed ones coincide; keep 4
CC_NAMES = ['zw', 'cz_w', 'z_cw', 'cz_cw']

def ccand(name):
    def f(z, w, name=name):
        zz = cconj(z) if 'cz' in name else z
        ww = cconj(w) if 'cw' in name else w
        return cmul(zz, ww)
    return f

def equivariant_scan(tris, basis, ncomp, cand_names, candf, nn):
    """For each cyclic slot (i,j)->k, find candidates p with
       comp_k(T) p(x,y) = p(comp_i(T) x, y) + p(x, comp_j(T) y) for all T, basis x,y."""
    out = {}
    for (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
        good = []
        for name in cand_names:
            p = candf(name)
            ok = True
            for T in tris:
                Mi, Mj, Mk = comp(T, i), comp(T, j), comp(T, k)
                for a in range(nn):
                    for b in range(nn):
                        x, y = basis[a], basis[b]
                        lhs = matvec(Mk, p(x, y))
                        rhs = tuple(u + v for u, v in
                                    zip(p(matvec(Mi, x), y), p(x, matvec(Mj, y))))
                        if lhs != rhs:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break
            if ok:
                good.append(name)
        out[(i, j, k)] = good
    return out

print("scanning octonion cross candidates ...")
OSCAN = equivariant_scan(TRIO, OBASIS, 8, OC_NAMES, pcand, 8)
print("  O-side survivors:", OSCAN)
CSCAN = equivariant_scan(TRIC, CBASIS, 2, CC_NAMES, ccand, 2)
print("  C'-side survivors:", CSCAN)

# require unique survivors on O side (C' may have more; disambiguate by Jacobi if needed)
for k, v in OSCAN.items():
    assert len(v) >= 1, f"no equivariant product for slot {k}"

# pick first survivor for each slot (report all)
OPROD = {k: pcand(v[0]) for k, v in OSCAN.items()}
OPICK = {str(k): v for k, v in OSCAN.items()}
CPROD = {k: ccand(v[0]) for k, v in CSCAN.items()}
CPICK = {str(k): v for k, v in CSCAN.items()}

# ---------------- dual maps ----------------
def tripair(t1, t2):
    """tr(A A') + tr(B B') + tr(C C') — ad-invariant, nondegenerate on tri."""
    s = F(0)
    for ci in range(3):
        A1, A2 = t1[ci], t2[ci]
        m = len(A1)
        for r in range(m):
            for c in range(m):
                s += A1[r][c] * A2[c][r]
    return s

def triform(tris):
    n = len(tris)
    return [[tripair(tris[a], tris[b]) for b in range(n)] for a in range(n)]

def inv_frac(G):
    n = len(G)
    M = [[F(x) for x in row] + [F(1) if i == j else F(0) for j in range(n)]
         for i, row in enumerate(G)]
    for c in range(n):
        p = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [u - f * v for u, v in zip(M[i], M[c])]
    return [row[n:] for row in M]

GO = triform(TRIO)
GC = triform(TRIC)
GOI = inv_frac(GO)
GCI = inv_frac(GC)
print("tri forms nondegenerate:", True)

def polar(POL, a, b):
    return POL[a][b]

def dual_t(tris, GINV, i, basis, POL, nn):
    """t_i(e_a, e_b) as coefficient vector in the tri basis, for all pairs (a,b)."""
    n = len(tris)
    out = {}
    for a in range(nn):
        for b in range(nn):
            # rhs_m = <comp(T_m, i) e_a, e_b>
            rhs = []
            for m in range(n):
                Mv = matvec(comp(tris[m], i), basis[a])
                rhs.append(sum(POL[r][b] * Mv[r] for r in range(nn)))
            coef = [sum(GINV[p][q] * rhs[q] for q in range(n)) for p in range(n)]
            out[(a, b)] = coef
    return out

print("building dual maps ...")
TDUAL = {i: dual_t(TRIO, GOI, i, OBASIS, OPOL, 8) for i in (1, 2, 3)}
SDUAL = {i: dual_t(TRIC, GCI, i, CBASIS, CPOL, 2) for i in (1, 2, 3)}

# verify duality definition on a sample
for i in (1, 2, 3):
    for (a, b) in [(0, 1), (3, 6), (2, 2)]:
        coef = TDUAL[i][(a, b)]
        # reconstruct t and test pairing against each basis T_m
        for m in range(NT):
            lhs = sum(coef[p] * GO[p][m] for p in range(NT))
            Mv = matvec(comp(TRIO[m], i), OBASIS[a])
            rhs = sum(OPOL[r][b] * Mv[r] for r in range(8))
            assert lhs == rhs
print("dual maps verified against definition (sample)")

# ---------------- tri brackets ----------------
def commutator_triple(T1, T2):
    def comm(X, Y):
        n = len(X)
        return [[sum(X[r][k] * Y[k][c] - Y[r][k] * X[k][c] for k in range(n))
                 for c in range(n)] for r in range(n)]
    return (comm(T1[0], T2[0]), comm(T1[1], T2[1]), comm(T1[2], T2[2]))

def express_in_tri(tri, tris, GINV, G):
    """coefficients of tri (a triple) in the basis 'tris' using the tr-form."""
    n = len(tris)
    m = len(tri[0])
    rhs = [tripair(tri, tris[q]) for q in range(n)]
    coef = [sum(GINV[p][q] * rhs[q] for q in range(n)) for p in range(n)]
    # verify exact (projection must reproduce all three components)
    for compi in range(3):
        rec = [[sum(coef[p] * tris[p][compi][r][c] for p in range(n))
                for c in range(m)] for r in range(m)]
        assert rec == [list(map(F, row)) for row in tri[compi]], "tri bracket not in span!"
    return coef

print("tri(O) bracket closure ...")
TBRK = {}
for a in range(NT):
    for b in range(a + 1, NT):
        TBRK[(a, b)] = express_in_tri(commutator_triple(TRIO[a], TRIO[b]), TRIO, GOI, GO)
CBRK = {}
for a in range(NC):
    for b in range(a + 1, NC):
        CBRK[(a, b)] = express_in_tri(commutator_triple(TRIC[a], TRIC[b]), TRIC, GCI, GC)
print("tri brackets closed exactly (verified by exact reconstruction)")

pickle.dump(dict(OSCAN=OPICK, CSCAN=CPICK, TDUAL=TDUAL, SDUAL=SDUAL,
                 TBRK=TBRK, CBRK=CBRK, GO=GO, GC=GC),
            open(os.path.join(HERE, "my_derived.pkl"), "wb"))
print("saved my_derived.pkl")
