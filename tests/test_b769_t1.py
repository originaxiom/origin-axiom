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
    # theta = contragredient (g -> g^-1). The theta-pairs are equal -- but note (C21
    # correction 2026-07-25) they are equal IDENTICALLY, not specially at omega, since
    # tr(g^-1) = tr(g) in SL(2). So this documents theta-triviality on the Sym^2 traces.
    A = _sym2(sp.Matrix([[1, 1], [0, 1]]))
    B = _sym2(sp.Matrix([[1, 0], [-omega, 1]]))
    tr = lambda M: sp.simplify(M.trace())
    assert sp.simplify(tr(A) - tr(A.inv())) == 0            # x1 = x4
    assert sp.simplify(tr(A * B) - tr(A.inv() * B.inv())) == 0     # x3 = x8
    assert sp.simplify(tr(A.inv() * B) - tr(A * B.inv())) == 0     # x6 = x7


def test_tangent_theta_odd_part_is_zero():
    # C21 correction: the geometric-point tangent d/du[tr Sym^2(AB)]|_omega = -5 + i*sqrt(3).
    # Its Re part is c-even, its Im part is c-ODD (complex conjugation) -- NOT theta-odd.
    # The theta(contragredient)-odd part is exactly 0, because tr Sym^2((AB)^-1) = tr Sym^2(AB)
    # identically. So there is no theta-frame on this module to "align" with the c-frame.
    A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-u, 1]])
    def sym2(M):
        a, b, c, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        return sp.Matrix([[a**2, a*b, b**2], [2*a*c, a*e + b*c, 2*b*e], [c**2, c*e, e**2]])
    probe = sp.simplify(sp.diff(sp.expand((A * B).trace() ** 2 - 1), u).subs(u, omega))
    probe_inv = sp.simplify(sp.diff(sp.expand(sym2((A * B).inv()).trace()), u).subs(u, omega))
    assert sp.simplify(sp.re(probe) + 5) == 0                     # Re = -5 (c-even)
    assert sp.simplify(sp.im(probe) - sp.sqrt(3)) == 0            # Im = sqrt(3) (c-ODD, not theta-odd)
    assert sp.simplify((probe - probe_inv) / 2) == 0             # theta(contragredient)-odd part = 0
