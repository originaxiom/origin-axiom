"""Locks for B769 -- the T1 structure (compute-grade)."""
import sympy as sp

u = sp.symbols("u")
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


def _sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, a*b, b**2], [2*a*c, a*d + b*c, 2*b*d], [c**2, c*d, d**2]])


def test_unmovedness_theorem_abelian_inner_triviality():
    els = list(range(8))
    V4 = [0, 1, 2, 3]
    assert all(((g ^ v) ^ g) == v for g in els for v in V4)


def test_geometric_point_is_theta_fixed():
    A = _sym2(sp.Matrix([[1, 1], [0, 1]]))
    B = _sym2(sp.Matrix([[1, 0], [-omega, 1]]))
    tr = lambda M: sp.simplify(M.trace())
    assert sp.simplify(tr(A) - tr(A.inv())) == 0            # x1 = x4
    assert sp.simplify(tr(A * B) - tr(A.inv() * B.inv())) == 0     # x3 = x8
    assert sp.simplify(tr(A.inv() * B) - tr(A * B.inv())) == 0     # x6 = x7


def test_tangent_alignment_probe():
    A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-u, 1]])
    d = sp.simplify(sp.diff(sp.expand((A * B).trace() ** 2 - 1), u).subs(u, omega))
    assert sp.simplify(sp.re(d) + 5) == 0                   # even along Re
    assert sp.simplify(sp.im(d) - sp.sqrt(3)) == 0          # odd along Im -- aligned frames
