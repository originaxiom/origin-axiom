#!/usr/bin/env python3
"""B1600, addendum: main's check of the SM seat's W20 (the weave's count in E6) and W22 (the puncture condition).
W20: chi(Aut+(F2); 27) with the 27 restricted to the moves' SL(2, Z) through E6's principal sl2 (27 = Sym16 + Sym8 + Sym0)
equals chi(SL(2, Z); 27) because the fibre's terms Sym^k (x) H are odd under -I; and chi(SL(2, Z); V) for the amalgam
Z/4 *_{Z/2} Z/6 is dim V^{Z/4} + dim V^{Z/6} - dim V^{Z/2} over Q.  Also E6(a1) (12 + 8 + 4), E6(a3) (8 + 6 + 4 + 4 + 0)
and the 78's control (the adjoint through the principal sl2: 2, 8, 10, 14, 16, 22).  W22: the lifts of L and R in 2O act
irreducibly on C^2, and so do the lifts of the moves fixing one parity (<g_L, g_R^2>, order 16).  Writes w20_w22_check.json."""
import json, pathlib
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
x, y = sp.symbols("x y")


def sym_matrix(M, k):
    a, b, c, d = [sp.Integer(int(v)) for v in np.array(M).flatten()]
    basis = [x ** (k - j) * y ** j for j in range(k + 1)]; cols = []
    for p in basis:
        q = sp.expand(p.subs({x: a * x + c * y, y: b * x + d * y}, simultaneous=True)); poly = sp.Poly(q, x, y)
        cols.append([poly.coeff_monomial(x ** (k - j) * y ** j) for j in range(k + 1)])
    return np.array(cols, dtype=float).T


S = np.array([[0, -1], [1, 0]]); U = np.array([[0, -1], [1, 1]]); MI = -np.eye(2, dtype=int)


def fixed_dim(A):
    n = A.shape[0]; order = 1; P = A.copy()
    while not np.allclose(P, np.eye(n)):
        P = P @ A; order += 1
    return int(round(np.trace(sum(np.linalg.matrix_power(A, i) for i in range(order)) / order)))


def chi_sl2z(k, tensor_H=False):
    tot = 0
    for M, w in ((S, 1), (U, 1), (MI, -1)):
        A = sym_matrix(M, k)
        if tensor_H:
            A = np.kron(A, sym_matrix(M, 1))
        tot += w * fixed_dim(A)
    return tot


out = {"chi_SL2Z_Sym_k": {k: chi_sl2z(k) for k in (0, 2, 4, 6, 8, 10, 12, 14, 16, 22)},
       "fibre_terms_zero": all(chi_sl2z(k, True) == 0 for k in (16, 8, 0))}
dec = {"E6 (principal)": [16, 8, 0], "E6(a1)": [12, 8, 4], "E6(a3)": [8, 6, 4, 4, 0], "78 through the principal sl2": [22, 16, 14, 10, 8, 2]}
out["minus_chi"] = {name: -sum(out["chi_SL2Z_Sym_k"][k] for k in ks) for name, ks in dec.items()}
out["dims"] = {name: sum(k + 1 for k in ks) for name, ks in dec.items()}
# W22
I2 = np.eye(2); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]]); s = 1 / np.sqrt(2)
gL = (I2 + qi) * s; gR = (I2 - qj) * s


def group(gens):
    """closure with a tolerance membership test (rounding keys can split one element into two at a rounding edge)"""
    G = [np.eye(2, dtype=complex)]; fr = [np.eye(2, dtype=complex)]
    while fr:
        M = fr.pop()
        for g in gens:
            N = M @ g
            if not any(np.allclose(N, E, atol=1e-7) for E in G):
                G.append(N); fr.append(N)
    return G


def irr(G):
    return round(float(sum(abs(np.trace(g)) ** 2 for g in G).real / len(G)), 6)


G2O = group([gL, gR]); H = group([gL, gR @ gR])
out["W22"] = {"<g_L,g_R> order": len(G2O), "sum|chi|^2/|G|": irr(G2O), "<g_L,g_R^2> order": len(H), "sum|chi|^2/|H|": irr(H),
              "irreducible_on_C2": irr(G2O) == 1.0 and irr(H) == 1.0}
json.dump(out, open(HERE / "w20_w22_check.json", "w"), indent=1); print(json.dumps(out, indent=1))
