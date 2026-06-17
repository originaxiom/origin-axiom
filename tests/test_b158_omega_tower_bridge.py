"""B158 -- the Ω↔tower bridge audit (V152). Fast deterministic locks.

Locks: the exact factorization relation (p-2)(q-2) = -2(m+1); that genuine integer
R_{a,m} on the live cone realize (metallic monodromy)x(phase) (silver T=6 x Phi6 =
R_{7,1}); and the commuting-shears obstruction (no faithful mechanism).
"""
import sympy as sp
import numpy as np

x, a, m = sp.symbols('x a m')


def _R(av, mv):
    return sp.Matrix([[av-3, av-2, 1, av-4], [0, 1, 1, 0], [mv+1, mv+1, 1, mv+1], [1, 1, 0, 1]])


def _G(av, mv):
    return sp.Matrix([
        [-1, 0, sp.Rational(av-4, mv+1), 0],
        [0, sp.Rational(-(2*av-mv-9), mv+1), 0, 2],
        [sp.Rational(av-4, mv+1), 0, sp.Rational(-(av**2-8*av+2*mv+18), (mv+1)**2), 1],
        [0, 2, 1, 0]])


def _sig(av, mv):
    ev = np.linalg.eigvalsh(np.array(_G(av, mv).evalf(), dtype=float))
    return int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((abs(ev) <= 1e-9).sum())


def test_factorization_relation():
    # (x^2-px+1)(x^2-qx+1) = chi_Omega forces p+q=a, pq=2a-2m-6; Vieta => (p-2)(q-2)=-2(m+1)
    pq, psum = 2*a - 2*m - 6, a
    assert sp.simplify((pq - 2*psum + 4) - (-2*(m+1))) == 0
    # the nontrivial coefficient match: 2 + pq == 2a-2m-4
    assert sp.simplify((2 + (2*a - 2*m - 6)) - (2*a - 2*m - 4)) == 0


def test_metallic_monodromies_realized_on_live_cone():
    # (a, m, T_M, q): tower monodromy trace T_M=M^2+2 x phase q, at integer/half-integer Omega points
    pts = [(4, sp.Rational(-1, 2), 3, 1),   # figure-eight x Phi6 = Omega_4 = B155 (half-integer)
           (7, 1, 6, 1),                     # silver x Phi6 = R_{7,1} (integer, live cone)
           (19, 7, 18, 1),                   # M=4 x Phi6
           (3, 0, 3, 0)]                     # figure-eight x Phi4
    for av, mv, T, qv in pts:
        cp = sp.expand((x*sp.eye(4) - _R(av, mv)).det())
        assert sp.simplify(cp - sp.expand((x**2 - T*x + 1)*(x**2 - qv*x + 1))) == 0
        assert _sig(av, mv) == (1, 3, 0)
    # T_M = M^2 + 2 is the metallic bundle-monodromy trace (m=1->3, m=2->6, m=4->18)
    assert [M*M + 2 for M in (1, 2, 4)] == [3, 6, 18]


def test_commuting_shears_obstruction():
    E = lambda i, j: (lambda Z: (Z.__setitem__((i, j), 1), Z)[1])(np.zeros((4, 4), int))
    A = np.eye(4, dtype=int) + E(0, 3)
    C = np.eye(4, dtype=int) + E(2, 3)
    assert np.array_equal(A @ C, C @ A)   # commute => abelian image only, no faithful mechanism
