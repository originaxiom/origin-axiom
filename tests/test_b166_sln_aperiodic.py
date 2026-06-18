"""B166 -- SL(n) higher-rank aperiodic operators (V163, P2b). Fast locks.

Q0 [exact]: odd n has no nondegenerate antisymmetric form (=> SL(n>=3) not a self-adjoint
operator's transfer group; intrinsically non-Hermitian). Q2 [cited]: the tower's one golden
scale. The numeric Q1 recorded-negative (no clean Cantor transfer) lives in sln_aperiodic.py.
"""
import sympy as sp


def test_odd_n_has_no_symplectic_form():
    for n in (3, 5):
        A = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'a{i}_{j}') if i < j else (0 if i == j else -sp.Symbol(f'a{j}_{i}')))
        assert sp.expand(A.det()) == 0          # every odd-dim antisymmetric matrix is degenerate


def test_even_n_has_symplectic_form_control():
    J2 = sp.Matrix([[0, 1], [-1, 0]])
    J4 = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])
    assert J2.det() == 1 and J4.det() == 1      # Sp exists for even n (n=2 is the SL=Sp coincidence)


def test_tower_one_golden_scale():
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(phi**2 - phi - 1) == 0   # the single golden scale the SL(n) tower carries (B107/B60)
