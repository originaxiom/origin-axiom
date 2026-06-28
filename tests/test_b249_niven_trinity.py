"""B249 locks -- Niven's theorem forces the figure-eight's clean-quadratic orbifold trace fields to exactly
{E6 (n=oo, Q(sqrt-3)), Euclidean (n=3, Q), E8 (n=2, Q(sqrt5))}; E7 (Q(sqrt2), n=4) is mixed/impossible. FIREWALLED
math (McKay/Arnold trinity, not gauge groups); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B249_niven_trinity" / "niven_trinity.py"
_spec = importlib.util.spec_from_file_location("b249", _PATH)
b249 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b249)


def test_niven_only_three_rational_orbifolds():
    rat = b249.niven_rational_orbifolds()
    assert set(r for r in rat if r != sp.oo) == {1, 2, 3}        # Niven: 2cos(pi/n) in Q only for n=1,2,3
    assert sp.oo in rat                                           # plus the complete cusp


def test_the_forced_trinity():
    assert b249.trace_field_label(sp.oo)[2] == "Q(sqrt-3)"      # E6 hyperbolic
    assert b249.trace_field_label(1)[2] == "Q(sqrt-3)"          # E6 (other parabolic)
    assert b249.trace_field_label(2)[2] == "Q(sqrt5)"          # E8 spherical
    assert b249.trace_field_label(3)[2] == "Q"                 # Euclidean (degenerate)


def test_e7_geometrically_excluded():
    # n=4 (x=sqrt2, E7's field) is NOT a clean quadratic field -> E7 impossible
    x, clean, field, mck = b249.trace_field_label(4)
    assert sp.simplify(x - sp.sqrt(2)) == 0
    assert not clean
    assert "MIXED" in field


def test_discriminant_values():
    # disc = (5-x^2)(1-x^2): -3 (E6), 0 (Euclidean), 5 (E8)
    assert sp.simplify(b249.discriminant(sp.Integer(2)) + 3) == 0
    assert sp.simplify(b249.discriminant(sp.Integer(1))) == 0
    assert sp.simplify(b249.discriminant(sp.Integer(0)) - 5) == 0
