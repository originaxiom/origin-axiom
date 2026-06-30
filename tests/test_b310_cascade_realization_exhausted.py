"""B310 lock -- the cascade realization question, exhausted. The E6 cascade is the standard E6 GUT chain (Slansky;
centralizers of exp(2pi i/N h), no fig-8 input); the genuinely-new "deformation realization at pi i/3 spacing on the
fig-8 character variety" is REFUTED (the cascade u-values 2pi i/N have gaps 1/3,1/6,1/10,1/15 -- not equal; the cusp
shape is 2 sqrt3 i not pi/3). The one object connection is the Eisenstein omega at trinification (B305, banked). The
physical realization (T[4_1;E6] DGG) is the CRUX -- specialist. Cascade math exhausted. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B310_cascade_realization_exhausted" / "cascade_realization_exhausted.py"
_spec = importlib.util.spec_from_file_location("b310", _PATH)
b310 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b310)


def test_cascade_is_generic_standard_chain():
    assert b310.CASCADE_IS_GENERIC_E6                     # centralizers of exp(2pi i/N h); Slansky 1981


def test_equal_pi3_spacing_refuted():
    assert b310.equal_pi3_spacing() is False
    assert b310.spacing_gaps() == [sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 10), sp.Rational(1, 15)]
    assert b310.EQUAL_PI3_SPACING_REFUTED and b310.SPACING_EQUALS_CUSP_SHAPE_REFUTED


def test_one_object_connection_is_the_banked_omega():
    assert b310.TRINIFICATION_EIGENVALUE_IS_OMEGA        # = B305 (already banked); not a new "spacing"
    assert b310.DEFORMATION_REALIZATION_VERIFIED is False


def test_realization_is_crux_math_exhausted():
    assert b310.REALIZATION_IS_THE_CRUX                  # T[4_1;E6] DGG -- specialist
    assert b310.CASCADE_MATH_EXHAUSTED                   # no new object-specific content beyond the banked omega
    assert b310.DERIVES_SM_VALUES is False
    assert b310.verdict()
