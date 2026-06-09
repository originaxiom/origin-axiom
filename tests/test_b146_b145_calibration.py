"""B146 -- B145 calibration. Part-A facts + the dichotomy bare-math unconditional; SnapPy/Sage arms gated."""
import pytest

from frontier.B146_b145_calibration.probe import arithmetic_arm, dichotomy_witness, part_a_facts


def test_part_a_facts():
    """A1: axioms permit chirality (RRL/RLL det-1 Pisot chiral). A4: symmetric-monodromy => amphichiral is sufficient,
    not necessary (RRLLRL amphichiral with non-symmetric monodromy)."""
    f = part_a_facts()
    assert f["A1_RRL_det1_pisot_chiral"] is True
    assert f["A1_RLL_chiral"] is True
    assert f["A4_RRLLRL_amphichiral"] is True
    assert f["A4_symmetric_is_sufficient_not_necessary"] is True


def test_dichotomy_witness():
    """B1: a mirror pair agrees on every orientation-independent invariant; only CS (orientation-sensitive) flips."""
    d = dichotomy_witness()
    if "skipped" in d:
        pytest.skip(d["skipped"])
    assert d["all_orientation_independent_agree_CS_flips"] is True


def test_arithmetic_arm_refuted_as_stated():
    """B2: with the INVARIANT trace field, imaginary-quadratic o-p-t bundles include CHIRAL ones (RRL = Q(sqrt-7));
    so B145's 'no quadratic chiral o-p-t bundle' is refuted as stated."""
    a = arithmetic_arm()
    if "skipped" in a:
        pytest.skip(a["skipped"])
    assert a["B145_arm_refuted_as_stated"] is True
    assert len(a["imaginary_quadratic_CHIRAL"]) > 0
