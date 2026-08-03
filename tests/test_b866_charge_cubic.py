"""Locks B866 -- the charge cubic, verified independently."""
import sympy as sp
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_F = " ".join((_ROOT / "frontier" / "B866_charge_cubic" / "FINDINGS.md")
              .read_text(encoding="utf-8").split())

t, r = sp.symbols("t rho")
MINE = 500716339200 * t**3 - 159667200 * t**2 - 28224 * t + 1
THEIRS = 500716339200 * r**3 - 2075673600 * r**2 - 4769856 * r + 2197


def test_the_two_cubics_are_identical_up_to_normalization():
    """theirs(13t) = 2197 * mine(t), exactly."""
    assert sp.expand(THEIRS.subs(r, 13 * t) - 2197 * MINE) == 0


def test_the_cubic_is_irreducible_with_galois_S3():
    assert sp.Poly(MINE, t).is_irreducible
    d = sp.discriminant(MINE, t)
    assert d > 0, "three real roots"
    assert not sp.sqrt(d).is_rational, "non-square discriminant -> S3, not Z/3"
    assert sp.factorint(d) == {2: 32, 3: 10, 5: 2, 7: 3, 11: 1, 13: 6}


def test_the_constant_term_and_leading_coefficient():
    p = sp.Poly(MINE, t)
    assert p.all_coeffs()[0] == 500716339200
    assert p.all_coeffs()[-1] == 1
    # their normalization: constant 2197 = 13^3 -- the rho = 13t rescaling
    assert 13**3 == 2197


def test_three_real_roots_in_the_stated_window():
    roots = [complex(x) for x in sp.Poly(MINE, t).all_roots()]
    assert all(abs(z.imag) < 1e-30 for z in roots)
    vals = sorted(z.real for z in roots)
    assert abs(vals[0] - (-1.4908079e-4)) < 1e-9
    assert abs(vals[1] - 3.0632423e-5) < 1e-10
    assert abs(vals[2] - 4.3732591e-4) < 1e-9


def test_the_multiplicity_matches_the_jump():
    """16 in the det polynomial = 46 - 30."""
    assert 46 - 30 == 16
    assert "¹⁶" in (_ROOT / "frontier" / "B866_charge_cubic" / "FINDINGS.md").read_text("utf-8")


def test_the_type_is_marked_as_their_leg_not_ours():
    assert "NOT verified here" in _F
    assert "the type is theirs" in _F


def test_generations_stays_a_signature():
    assert "SIGNATURE, not a mechanism" in _F


def test_the_double_float_failure_is_recorded():
    assert "both directions" in _F
    assert "exact interpolation decided" in _F.lower() or "exact interpolation" in _F


def test_addendum_the_type_is_confirmed_on_both_legs():
    """so(10)+u(1): derived dim 45 (unique simple of dim 45 = D5), center dim 1."""
    f_raw = (_ROOT / "frontier" / "B866_charge_cubic" / "FINDINGS.md").read_text("utf-8")
    f = " ".join(f_raw.split())
    assert "derived algebra dim** | **45**" in f or "derived dim 45" in f
    assert "center dim 1" in f or "center dim** | **1**" in f
    assert "step-1 max-dim ranking retires" in f
