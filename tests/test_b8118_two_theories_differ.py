"""B8118 -- locks the category-error result and its genericity control."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = json.load(open(os.path.join(ROOT, "frontier", "B8118_two_theories_differ", "results.json")))


def test_m004_shape_field_is_Q_sqrt_minus_3():
    assert R["m004_shape_field_disc"] == -3
    assert R["m004_shapes_regular_ideal"] is True


def test_the_b997_correction_is_rerun_not_cited():
    """SL(2,Z/3) is 2T (one involution); SL(2,Z/4) is NOT 2O (seven)."""
    assert R["sl2_z3_order"] == 24
    assert R["sl2_z3_involutions"] == 1
    assert R["sl2_z4_involutions"] == 7


def test_the_genericity_control_bites():
    """E6 cannot be m004-specific if the whole family inherits it."""
    assert R["n_sharing_shape_field"] > 1
    assert "m004" in R["sharing"] and "m003" in R["sharing"]
    assert R["n_distinct_volumes"] > 1


def test_the_triangulation_is_not_constant_on_the_family():
    """This is what makes (A) and (B) different KINDS, not rival descriptions."""
    assert len(R["tetrahedron_counts_in_family"]) > 1
    assert 2 in R["tetrahedron_counts_in_family"]


def test_the_two_attach_at_different_places():
    assert "triangulation" in R["A_attaches_at"]
    assert "shape field" in R["B_attaches_at"]
    assert R["they_differ"] is True and R["difference_is_of_kind"] is True


def test_the_verdict_names_it_a_category_error():
    assert "CATEGORY ERROR" in R["verdict"]
    assert "B990" in R["verdict"]


def test_scope_declares_the_shape_vs_trace_field_caveat():
    assert "does NOT independently verify that identification" in R["scope"]
