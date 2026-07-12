"""Locks for the B556 proof upgrade (chat-2 audit, verified)."""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

x = sp.Symbol('x')
F = sp.Matrix([[1, 1], [1, 0]])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M*M, M]]))


def test_miss_a_norm_is_minus_one():
    """N(beta) = product of quartic roots = -1 < 0 -> sqrt(beta) not in Q(tau)."""
    cp = _T(F).charpoly(x).as_expr()          # rung-1 charpoly
    assert sp.Poly(cp, x).all_coeffs()[-1] == -1      # constant term = N(beta)


def test_miss_b_det_telescope_and_negativity():
    """d_{n+1} = d_n^2 * e_n, and every e_n < 0 (rungs 0-4)."""
    M = F
    es = []
    for n in range(4):
        d = M.det()
        e = (sp.eye(M.shape[0]) - M).det()
        es.append(e)
        assert _T(M).det() == d**2 * e                # telescope
        M = _T(M)
    assert all(e < 0 for e in es)                     # doubling fires every rung


def test_miss_c_charge_tower_cyclic():
    """|e_n| = 1,11,809,18845089; coker(I-M_n) = Z/|e_n| cyclic; e_1 = -11 (B552)."""
    M = F
    mags = []
    for n in range(4):
        S = smith_normal_form(sp.eye(M.shape[0]) - M)
        diag = [abs(S[i, i]) for i in range(M.shape[0])]
        assert len([d for d in diag if d > 1]) <= 1   # cyclic
        mags.append(abs((sp.eye(M.shape[0]) - M).det()))
        M = _T(M)
    assert mags == [1, 11, 809, 18845089]
