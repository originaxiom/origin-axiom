"""Lock: the charge-tower period characterization (partial, verified)."""
import sympy as sp

x = sp.Symbol('x')
F = sp.Matrix([[1, 1], [1, 0]])


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M*M, M]]))


def test_g_root_structure_mod_p():
    """g = x^3-x^2+2x-1 has a linear root mod {5,7,11,...}, inert mod {3,13,29}."""
    g = x**3 - x**2 + 2*x - 1
    def has_linear_root(p):
        return any(f.degree() == 1 for f, _ in sp.factor_list(sp.Poly(g, x, modulus=p))[1])
    assert all(has_linear_root(p) for p in [5, 7, 11, 17, 19, 23])
    assert not any(has_linear_root(p) for p in [3, 13, 29])


def test_11_period_3_is_orbit_return():
    """p | e_n <=> 1 in spec(M_n) mod p; for 11 this is n = 1,4 (period 3)."""
    M = F
    zeros = []
    for n in range(5):
        if (sp.eye(M.shape[0]) - M).det() % 11 == 0:
            zeros.append(n)
        M = _T(M)
    assert zeros == [1, 4]           # period-3 returns within range
