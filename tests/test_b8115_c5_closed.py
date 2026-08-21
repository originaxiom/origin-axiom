"""B8115 -- locks C5's closure as a negative, and locks the successor's caveat in place."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8115_c5_closed")
R = json.load(open(os.path.join(ARC, "results.json")))


def test_the_action_is_finite_group_valued():
    assert "FINITE CYCLIC GROUP" in R["the_action_target"]
    assert "(1/n)Z/Z" in R["the_action_target"]


def test_no_analytic_ingredient_is_present():
    for k in ("volume_term_present", "regulator_present", "torsion_present",
              "laplacian_determinant_present", "archimedean_height_present"):
        assert R[k] is False, k


def test_real_places_enter_algebraically_not_analytically():
    assert "COMPACT SUPPORT" in R["real_places_enter_via"]
    assert "NOT an analytic term" in R["real_places_enter_via"]


def test_c5_is_closed_as_a_negative():
    assert R["typing_after"].startswith("CLOSED")
    assert "NEGATIVE" in R["typing_after"]
    assert R["typing_before"].startswith("NEEDS-READING")


def test_the_negative_names_a_boundary():
    assert "ARCHIMEDEAN" in R["boundary_named"]
    assert "wrong side" in R["boundary_named"]


def test_the_successor_is_registered_unproved_with_the_conflation_named():
    """The lock that matters: holomorphic-vs-real torsion must stay flagged."""
    c = R["successor_caveat"]
    assert "UNPROVED" in c
    assert "HOLOMORPHIC" in c and "REAL Ray-Singer" in c
    assert "not the same object" in c
    assert "THE LEAD, not a claim" in c
