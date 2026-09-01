"""R13 blind — tri(O) and tri(C') as exact nullspaces over Q.

tri(K) = {(A,B,C) skew wrt polar form : A(xy) = B(x)y + x C(y) for all x,y}.
Unknowns: entries of A,B,C. Solved by exact fraction Gaussian elimination.
"""
from fractions import Fraction as F
import itertools
from octonion_core import (OBASIS, OMT, OPOL, CBASIS, CMT, CPOL, omul, cmul)


def nullspace_frac(rows, ncols):
    """Exact nullspace of a list-of-lists rational matrix. Returns list of basis vecs."""
    import numpy as np
    M = [list(map(F, r)) for r in rows]
    m = len(M)
    piv_cols = []
    r = 0
    for c in range(ncols):
        # find pivot
        p = None
        for i in range(r, m):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for ri, pc in enumerate(piv_cols):
            v[pc] = -M[ri][fc]
        basis.append(v)
    return basis


def tri_algebra(BAS, MT, POL, n):
    """Solve for tri: unknowns A(n^2), B(n^2), C(n^2) column-major u[A_{rc}] etc."""
    NU = 3 * n * n
    def iA(r, c): return r * n + c
    def iB(r, c): return n * n + r * n + c
    def iC(r, c): return 2 * n * n + r * n + c
    rows = []
    # identity: A(e_i e_j) - B(e_i) e_j - e_i C(e_j) = 0, component k
    for i in range(n):
        for j in range(n):
            m = MT[i][j]  # e_i e_j as vector
            for k in range(n):
                row = [F(0)] * NU
                # A(m)_k = sum_l A_{k,l} m_l
                for l in range(n):
                    if m[l]:
                        row[iA(k, l)] += m[l]
                # -(B e_i) e_j: B e_i = sum_l B_{l,i} e_l ; (e_l e_j)_k = MT[l][j][k]
                for l in range(n):
                    c = MT[l][j][k]
                    if c:
                        row[iB(l, i)] -= c
                # -(e_i C e_j): C e_j = sum_l C_{l,j} e_l ; (e_i e_l)_k
                for l in range(n):
                    c = MT[i][l][k]
                    if c:
                        row[iC(l, j)] -= c
                if any(row):
                    rows.append(row)
    # skewness wrt POL for A, B, C:  POL M + M^T POL = 0
    # (POL M)_{ij} = sum_l POL_{il} M_{lj};  (M^T POL)_{ij} = sum_l M_{li} POL_{lj}
    for (base, idx) in ((0, iA), (1, iB), (2, iC)):
        for i in range(n):
            for j in range(n):
                row = [F(0)] * NU
                for l in range(n):
                    if POL[i][l]:
                        row[idx(l, j)] += POL[i][l]
                    if POL[l][j]:
                        row[idx(l, i)] += POL[l][j]
                if any(row):
                    rows.append(row)
    ns = nullspace_frac(rows, NU)
    tris = []
    for v in ns:
        A = [[v[iA(r, c)] for c in range(n)] for r in range(n)]
        B = [[v[iB(r, c)] for c in range(n)] for r in range(n)]
        Cm = [[v[iC(r, c)] for c in range(n)] for r in range(n)]
        tris.append((A, B, Cm))
    return tris


def tri_raw_dim(BAS, MT, n):
    """dim of the identity-only solution space (no skewness) — sanity report."""
    NU = 3 * n * n
    def iA(r, c): return r * n + c
    def iB(r, c): return n * n + r * n + c
    def iC(r, c): return 2 * n * n + r * n + c
    rows = []
    for i in range(n):
        for j in range(n):
            m = MT[i][j]
            for k in range(n):
                row = [F(0)] * NU
                for l in range(n):
                    if m[l]:
                        row[iA(k, l)] += m[l]
                for l in range(n):
                    c = MT[l][j][k]
                    if c:
                        row[iB(l, i)] -= c
                for l in range(n):
                    c = MT[i][l][k]
                    if c:
                        row[iC(l, j)] -= c
                if any(row):
                    rows.append(row)
    return len(nullspace_frac(rows, NU))


if __name__ == "__main__":
    import pickle, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    trO = tri_algebra(OBASIS, OMT, OPOL, 8)
    print("dim tri(O) (skew-constrained):", len(trO))
    print("dim raw identity space (O):", tri_raw_dim(OBASIS, OMT, 8))
    trC = tri_algebra(CBASIS, CMT, CPOL, 2)
    print("dim tri(C'):", len(trC))
    print("dim raw identity space (C'):", tri_raw_dim(CBASIS, CMT, 2))
    pickle.dump({"triO": trO, "triC": trC}, open(os.path.join(HERE, "my_tri.pkl"), "wb"))
    print("saved my_tri.pkl")
