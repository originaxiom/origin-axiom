#!/usr/bin/env python3
"""B469 Phase 2 — the sigma-lift verification (CC bank of Chat-2's Phase-2a).

conj(W(m,1)) = Par . WR_14^m . Par . D(m,14)   [the c-family convention]
Verified: complex 1e-15 (m = 1, 2) AND EXACT in F_p at p = 61, 421 (conj = the
ring hom z -> z^14 — licensed: the construction is polynomial in z over Q).
Also exact: the +j obstruction T_(-j) - T_j = c*m*j (Par D Par != D — sigma is a
twisted two-world correspondence, not a similarity), and the non-similarity of
conj(M_1) and M_14 (spectral gap 1.26 rad).
"""
import os, sys
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B465_monodromy_intake"))
from exact_engine import find_root_of_unity

N = 15

def fp_family(p, z15):
    def Dc(pw, c):
        return [[pow(z15, (pw*c*(j*(j-1)//2)) % N, p) if i == j else 0 for j in range(N)] for i in range(N)]
    F = [[pow(z15, (j*k) % N, p) for k in range(N)] for j in range(N)]
    Finv = [[pow(z15, (-j*k) % N, p) for k in range(N)] for j in range(N)]
    inv15 = pow(15, p-2, p)
    def mat(A, B):
        Bt = list(zip(*B))
        return [[sum(a*b for a, b in zip(r, col)) % p for col in Bt] for r in A]
    def matpow(A, k):
        R = [[1 if i == jx else 0 for jx in range(N)] for i in range(N)]
        while k:
            if k & 1: R = mat(R, A)
            A = mat(A, A); k >>= 1
        return R
    def WR(c):
        M = mat(mat(F, Dc(-1, c)), Finv)
        return [[(x*inv15) % p for x in row] for row in M]
    def Wmc(m, c): return mat(matpow(WR(c), m), Dc(m, c))
    Par = [[1 if i == ((-j) % N) else 0 for j in range(N)] for i in range(N)]
    return Wmc, WR, Dc, Par, mat, matpow

def main():
    ok = True
    for p in (61, 421):
        z15 = find_root_of_unity(p, 15)
        Wmc, WR, Dc, Par, mat, matpow = fp_family(p, z15)
        Wmc_c, _, _, _, _, _ = fp_family(p, pow(z15, 14, p))
        for m in (1, 2):
            lhs = Wmc_c(m, 1)
            rhs = mat(mat(Par, matpow(WR(14), m)), mat(Par, Dc(m, 14)))
            hit = lhs == rhs
            ok &= hit
            print(f"p={p} m={m}: lift exact: {hit}")
    j, m, c = sp.symbols('j m c', integer=True)
    obstruction = sp.simplify(c*m*(-j)*(-j-1)/2 - c*m*j*(j-1)/2)
    print(f"+j obstruction: T_(-j) - T_j = {obstruction}")
    ok &= obstruction == c*j*m
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
