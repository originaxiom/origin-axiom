"""Locks B853 -- the incoming relay verified, and the two-faces finding.

The load-bearing locks here are the PARITY ones: an order parameter must be ODD under the symmetry
it measures, and m = sqrt5/3 is FIXED under the sqrt(-3) involution that Cl(O_4)/Frob_7 acts by.
That single fact is what separates the two candidate SSBs.
"""
import importlib.util
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b853", _ROOT / "frontier" / "B853_two_faces_ssb" / "relay_verify.py")
b3 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b3)
_F = (_ROOT / "frontier" / "B853_two_faces_ssb" / "FINDINGS.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------------------------------
# The relay's facts
# ---------------------------------------------------------------------------------------
def test_fact1_both_CM_points_are_purely_imaginary_and_c_fixes_them():
    f = b3.main.__globals__  # noqa: F841  (module import side effects only)
    forms = b3.reduced_forms(-48)
    assert forms == [(1, 0, 12), (3, 0, 4)]
    assert all(b == 0 for (_a, b, _c) in forms), "b = 0 is why the CM points are imaginary"
    for (a, b, c) in forms:
        tau = b3.cm_point(a, b, -48)
        assert sp.simplify(sp.re(tau)) == 0
        assert b3.conjugation_fixes(tau)


def test_fact2_frob2_is_NOT_defined_and_frob7_is_the_generator():
    """Structural, not typographic: 2 divides the conductor 4, so (2) is outside the Artin map."""
    assert b3.conductor(-48) == 4
    from math import gcd
    assert gcd(2, 4) != 1, "2 is not coprime to the conductor"
    nontrivial = b3.primes_represented(3, 0, 4)
    principal = b3.primes_represented(1, 0, 12)
    assert nontrivial[0] == 7, f"smallest legitimate generator is Frob_7, got {nontrivial[:3]}"
    assert 2 not in nontrivial and 2 not in principal
    assert 13 in principal and 7 in nontrivial


def test_fact3_the_class_groups_differ():
    assert b3.class_number(-48) == 2      # conductor-4 order: m004's cusp
    assert b3.class_number(-3) == 1       # maximal order: m003's cusp


# ---------------------------------------------------------------------------------------
# The two faces -- the finding
# ---------------------------------------------------------------------------------------
def test_the_order_parameter_is_ODD_on_one_face_and_FIXED_on_the_other():
    """THE POINT. An order parameter must be odd under the symmetry it measures."""
    tf = b3.two_faces()
    assert tf["m_odd_under_sqrt5_galois"] is True
    assert tf["m_fixed_under_sqrt_minus3_galois"] is True
    assert tf["order_parameter_story_is_invisible_to_the_broken_symmetry"] is True


def test_B6_potential_is_a_sqrt5_face_object():
    tf = b3.two_faces()
    assert tf["critical_points_swapped_by_gal5"] is True
    assert tf["critical_values_are_galois_conjugates"] is True


def test_the_thermodynamic_ingredients_are_present_on_the_hearing_face():
    """Lower broken minimum plus a barrier -- what cc wrongly said was absent."""
    tf = b3.two_faces()
    assert tf["V_phi_below_V_zero"] is True
    assert tf["barrier_at_anti"] is True
    assert tf["barrier_height_above_minimum"] > 1.8


def test_the_arc_records_ccs_own_two_errors():
    """A B711 citation made by grep, and the microscopic/thermodynamic arrow conflation."""
    assert "cited B711 by grep" in _F
    assert "Sakharov" in _F and "microscopic time-reversibility does not block" in _F


# ---------------------------------------------------------------------------------------
# The holes I closed in my own earlier work
# ---------------------------------------------------------------------------------------
def test_the_27s_top_block_is_VERIFIED_not_assumed():
    t = b3.twenty_seven_top_block()
    assert t["principal_weight_of_omega1"] == 16 and t["top_block_of_27_is_V16"]
    assert t["control_adjoint_is_V22"], "the adjoint control must reproduce V_22"


def test_multiplicative_independence_does_NOT_rest_on_norms():
    """Both units have norm 1, so a norm argument would be vacuous here."""
    mi = b3.multiplicative_independence()
    assert mi["norm_u3"] == 1 and mi["norm_u15"] == 1
    assert mi["norms_separate_them"] is False
    assert "cap Q(sqrt15) = Q" in mi["argument"]


def test_the_arc_flags_the_B261_link_as_an_ANALOGY_not_a_result():
    assert "analogy" in _F.lower()
    assert "not an identification" in _F or "not a result" in _F.lower()


def test_the_arc_keeps_the_transcendental_question_OPEN():
    """cc closed it wrongly; it must stay open, under the relay's own DOF rule."""
    assert "OPEN, not closed" in _F
    assert "DOF-0" in _F
