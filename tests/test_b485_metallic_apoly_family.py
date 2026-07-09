"""Locks for B485 (metallic A-polynomial family, forcing edges #2/#3).

Recomputes the exact/cheap half: the Alexander family law Delta_m(a) = a^2 - (m^2+2)a + 1
as the char poly of the monodromy R^m L^m (sympy, exact), the Newton-polygon interior
lattice count (7) of the figure-eight A-polynomial (pure integer geometry), and — SnapPy
guarded — the manifold identifications (m=1,2,3 = 4_1, m136, s464) and the rectangular
(purely imaginary, decreasing) cusp moduli. The geometric genus 3 came from a sage
Curve.genus() run and is locked here as the banked FINDINGS line, not recomputed.
"""
import pathlib

import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_FIND = (_ROOT / "frontier" / "B485_metallic_apoly_family" / "FINDINGS.md").read_text(encoding="utf-8")


def _monodromy(m):
    R = sp.Matrix([[1, 1], [0, 1]])
    L = sp.Matrix([[1, 0], [1, 1]])
    return R**m * L**m


def test_alexander_family_law_is_monodromy_char_poly():
    # Delta_m(a) = det(aI - A_m) = a^2 - (m^2+2)a + 1, exactly, m = 1..5
    a = sp.symbols('a')
    for m in range(1, 6):
        A = _monodromy(m)
        assert A.det() == 1 and sp.trace(A) == m * m + 2
        cp = sp.expand((a * sp.eye(2) - A).det())
        assert cp == a**2 - (m * m + 2) * a + 1


def test_explicit_middle_coefficients_m1_to_5():
    # the banked list a^2-3a+1, a^2-6a+1, a^2-11a+1, a^2-18a+1, a^2-27a+1
    assert [sp.trace(_monodromy(m)) for m in range(1, 6)] == [3, 6, 11, 18, 27]


def _hull(points):
    pts = sorted(set(points))
    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and (
                    (out[-1][0] - out[-2][0]) * (p[1] - out[-2][1])
                    - (out[-1][1] - out[-2][1]) * (p[0] - out[-2][0])) <= 0:
                out.pop()
            out.append(p)
        return out
    lower, upper = half(pts), half(pts[::-1])
    return lower[:-1] + upper[:-1]          # counterclockwise


def test_fig8_apoly_newton_polygon_has_7_interior_points():
    # genus upper bound: interior lattice points of the Newton polygon of
    # M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4  (the geometric component)
    M, L = sp.symbols('M L')
    apoly = M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4
    support = sp.Poly(apoly, M, L).monoms()
    hull = _hull(support)
    xs = [p[0] for p in support]
    ys = [p[1] for p in support]
    interior = []
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            if all((b[0] - a[0]) * (y - a[1]) - (b[1] - a[1]) * (x - a[0]) > 0
                   for a, b in zip(hull, hull[1:] + hull[:1])):
                interior.append((x, y))
    assert len(interior) == 7


def test_findings_bank_alexander_law_and_genus3():
    # the load-bearing banked lines (genus 3 itself was a sage computation)
    assert "Δ_m(a) = a² − (m²+2)·a + 1" in _FIND
    assert "geometric genus 3" in _FIND
    assert "RECTANGULAR cusps" in _FIND
    assert "a²−3a+1, a²−6a+1, a²−11a+1, a²−18a+1, a²−27a+1" in _FIND


def test_bundle_identifications_snappy():
    snappy = pytest.importorskip("snappy")
    for m, name in [(1, '4_1'), (2, 'm136'), (3, 's464')]:
        B = snappy.Manifold('b++' + 'R' * m + 'L' * m)
        assert B.is_isometric_to(snappy.Manifold(name)), (m, name)


def test_rectangular_decreasing_cusp_moduli_snappy():
    snappy = pytest.importorskip("snappy")
    ims = []
    for m in range(1, 5):
        tau = complex(snappy.Manifold('b++' + 'R' * m + 'L' * m).cusp_info(0).modulus)
        assert abs(tau.real) < 1e-9          # purely imaginary = rectangular
        ims.append(tau.imag)
    # banked values 2*sqrt(3), 2.000, 1.6616, 1.6005 — strictly decreasing
    assert abs(ims[0] - 2 * 3**0.5) < 1e-9
    assert abs(ims[1] - 2.0) < 1e-9
    assert abs(ims[2] - 1.661575) < 1e-5
    assert abs(ims[3] - 1.600485) < 1e-5
    assert ims == sorted(ims, reverse=True)
