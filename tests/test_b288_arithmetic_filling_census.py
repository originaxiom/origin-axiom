"""B288 lock -- THE ARITHMETIC FILLING CENSUS (the CRUX through the seam). The cusped (open) figure-eight has
invariant trace field Q(sqrt-3) (the E6 atom, B266/B282); NO closed hyperbolic filling (54 resolved over |p|,|q|<=8)
re-sees Q(sqrt-3) or is arithmetic. The E6 arithmetic is an OPEN-object property, lost on closing -- leaning
CATALOGUE for the CRUX. FIREWALLED; nothing to CLAIMS.md.
(SnapPy+Sage reproducer: sage-python frontier/B288_arithmetic_filling_census/arithmetic_census.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B288_arithmetic_filling_census" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b288", _PATH)
b288 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b288)


def test_cusped_open_object_is_Qsqrt_neg3():
    assert b288.cusped_is_Qsqrt_neg3()                       # disc(x^2-x+1) = -3  => Q(sqrt-3) (the E6 atom)
    assert b288.CUSPED_RESEES_SQRT_NEG3


def test_closed_fillings_do_not_resee_sqrt_neg3():
    # independent pyenv re-check on the sample: x^2+3 stays irreducible over each closed field
    for mp in b288.SAMPLE_CLOSED_MINPOLYS.values():
        assert not b288._field_contains_sqrt_neg3(mp)
    assert b288.N_RESEEING_SQRT_NEG3 == 0


def test_no_closed_filling_is_arithmetic():
    assert b288.N_ARITHMETIC == 0                            # none imaginary-quadratic; arithmeticity lost on closing


def test_e6_open_object_property_and_firewall():
    assert b288.E6_IS_OPEN_OBJECT_PROPERTY
    assert b288.CRUX_LEANS_CATALOGUE
    assert b288.DERIVES_SM_VALUES is False
    assert b288.verdict()
