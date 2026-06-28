"""B251 locks -- the E6<->E8 geometric transition is golden-specific: H1(M_m)=Z(+)(Z/m)^2 so only m=1 (the
figure-eight) is a knot complement in S^3; the m=1 '5' stack (discriminant=det=2-bridge numerator=|H1(L(5,2))|=5).
FIREWALLED (topology/arithmetic); nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B251_metallic_specificity" / "metallic_specificity.py"
_spec = importlib.util.spec_from_file_location("b251", _PATH)
b251 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b251)


def test_monodromy_trace_is_metallic_discriminant_minus_two():
    for m in range(1, 8):
        assert int(b251.monodromy(m).trace()) == m * m + 2


def test_h1_torsion_is_Zm_squared():
    assert b251.h1_torsion(1) == []                       # H1(4_1) = Z
    for m in range(2, 12):
        assert b251.h1_torsion(m) == [m, m]               # H1(M_m) = Z (+) (Z/m)^2


def test_only_m1_is_a_knot_complement():
    assert b251.is_knot_complement_in_S3(1)
    assert all(not b251.is_knot_complement_in_S3(m) for m in range(2, 12))


def test_the_five_stack_all_equal_five():
    stack = b251.figure_eight_five_stack()
    assert set(stack.values()) == {5}
    assert len(stack) == 4                                # discriminant, det, 2-bridge numerator, |H1(L(5,2))|
