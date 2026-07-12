"""Locks for B556 — the escalator tower (verified core)."""
import numpy as np
import sympy as sp

x = sp.Symbol('x')
F = sp.Matrix([[1, 1], [1, 0]])
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
M4 = sp.Matrix([[SUB[c].count(r) for c in 'abAB'] for r in 'abAB'])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M*M, M]]))


def test_TF_equals_M4_verbatim():
    assert _T(F) == M4          # the load-bearing fact, exact (not up to perm)


def test_tower_degrees_and_irreducible():
    M = F
    degs = []
    for n in range(4):
        cp = M.charpoly(x).as_expr()
        degs.append(sp.Poly(cp, x).degree())
        fl = sp.factor_list(cp)[1]
        assert len(fl) == 1 and fl[0][1] == 1, f"rung {n} charpoly reducible"
        M = _T(M)
    assert degs == [2, 4, 8, 16]      # field doubling


def test_lambda_law():
    lam = (1 + np.sqrt(5)) / 2
    perrons = []
    for _ in range(4):
        perrons.append(lam)
        lam = lam * (1 + np.sqrt(lam))
    # match the actual matrix Perrons
    M = F
    for k in range(4):
        pf = max(abs(e) for e in np.linalg.eigvals(np.array(M.tolist(), float)))
        assert abs(pf - perrons[k]) < 1e-6
        M = _T(M)


def test_rung2_perron_is_beta_selfsimilar():
    beta = ((1 + np.sqrt(5)) / 2) * (1 + np.sqrt((1 + np.sqrt(5)) / 2))
    lam2 = beta * (1 + np.sqrt(beta))
    assert abs(lam2 - 10.724751772) < 1e-8
