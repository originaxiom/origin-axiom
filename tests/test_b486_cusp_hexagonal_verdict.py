"""Locks for B486 ("hexagonal cusp -> three generations": REFUTED, 11th kill).

Recomputes the decisive arithmetic exactly: the cusp modulus 2*sqrt(-3) is a rectangular
CM point (disc -48), not the hexagonal point (disc -3); the lattice Z + 2*sqrt(3)i*Z has
shortest-vector multiplicity 2 (vs the hexagonal 6) and the three claimed 'equal' curves
have norms 1, 12, 13 — all different. Also the half-truth that made the mistake seductive:
2*sqrt(-3) = 4*omega + 2 lies in Z[omega], of index 4 (Eisenstein FIELD, not hexagonal torus).
SnapPy-guarded: the live cusp modulus and orthogonal translations. Verdict lines locked
from FINDINGS.md / SIXB_VERDICT.md.
"""
import pathlib

import pytest
import sympy as sp

_DIR = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B486_cusp_hexagonal_verdict"
_FIND = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")


def test_cm_discriminants_differ():
    # tau = 2*sqrt(-3): minimal poly tau^2 + 12, disc -48; hexagonal omega: omega^2+omega+1, disc -3
    z = sp.symbols('z')
    tau = 2 * sp.sqrt(-3)
    assert sp.expand(tau**2 + 12) == 0
    assert sp.discriminant(z**2 + 12, z) == -48
    assert sp.discriminant(z**2 + z + 1, z) == -3
    assert -48 != -3                       # different CM points: not SL(2,Z)-equivalent


def test_three_claimed_curves_have_different_lengths():
    # lattice Z + 2*sqrt(3)i*Z, norm form p^2 + 12 q^2: |(1,0)|^2, |(0,1)|^2, |(1,1)|^2
    n = {v: v[0]**2 + 12 * v[1]**2 for v in [(1, 0), (0, 1), (1, 1)]}
    assert n[(1, 0)] == 1 and n[(0, 1)] == 12 and n[(1, 1)] == 13
    assert len(set(n.values())) == 3       # all different — no degeneracy
    assert abs(12**0.5 - 3.46) < 5e-3 and abs(13**0.5 - 3.61) < 5e-3   # the banked 3.46 / 3.61


def test_shortest_vector_multiplicity_2_not_hexagonal_6():
    rng = range(-3, 4)
    rect = {(p, q): p * p + 12 * q * q for p in rng for q in rng if (p, q) != (0, 0)}
    hexa = {(p, q): p * p + p * q + q * q for p in rng for q in rng if (p, q) != (0, 0)}
    m_rect = min(rect.values())
    m_hexa = min(hexa.values())
    assert m_rect == 1 and sum(1 for v in rect.values() if v == m_rect) == 2
    assert m_hexa == 1 and sum(1 for v in hexa.values() if v == m_hexa) == 6


def test_eisenstein_field_but_not_hexagonal_torus():
    # the half-truth: 2*sqrt(-3) = 4*omega + 2 IS in Z[omega], but with covolume index 4
    omega = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
    assert sp.expand(4 * omega + 2 - 2 * sp.sqrt(-3)) == 0
    covol_eisenstein = sp.im(omega)               # sqrt(3)/2
    covol_cusp = 2 * sp.sqrt(3)                   # Im(2*sqrt(-3))
    assert sp.simplify(covol_cusp / covol_eisenstein) == 4


def test_live_cusp_modulus_rectangular_snappy():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold('4_1')
    tau = complex(M.cusp_info(0).modulus)
    assert abs(tau.real) < 1e-9                       # imaginary axis, NOT Re = -1/2
    assert abs(tau.imag - 2 * 3**0.5) < 1e-9          # 2*sqrt(3)
    mer, lon = M.cusp_translations()[0]
    mer, lon = complex(mer), complex(lon)
    assert abs(abs(mer) - 1.0) < 1e-9                 # meridian length 1
    assert abs(abs(lon) - 2 * 3**0.5) < 1e-9          # longitude length 2*sqrt(3)
    # orthogonal: meridian purely imaginary, longitude real
    assert abs(mer.real) < 1e-9 and abs(lon.imag) < 1e-9


def test_verdict_lines():
    assert "REFUTED (11th kill), the cusp is rectangular" in _FIND
    assert "**Rectangular lattice.**" in _FIND
    assert "NOT SL(2,ℤ)-equivalent" in _FIND
    assert "disc −48 vs disc −3" in _FIND
    assert "**No three-fold degeneracy.**" in _FIND
    assert "11th SM kill" in _FIND
    assert "Firewall holds" in _FIND
    # 6b stayed unconfirmed after the dedicated re-run
    sixb = (_DIR / "SIXB_VERDICT.md").read_text(encoding="utf-8")
    assert "6b (power-set magnitude law) — NOT CONFIRMED" in sixb
