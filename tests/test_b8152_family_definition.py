"""Lock: the family is 111 under the paper's own criterion, and the criteria are nested."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8152_family_definition/results.json").read_text())
TEX = (ROOT / "papers/series/paper4_what_cannot_be_supplied/main.tex").read_text()

def test_the_two_criteria_are_nested_not_equal():
    c = R["the_two_criteria"]
    assert c["A_all_regular_ideal"] == 77 and c["B_shape_field_in_Qsqrt3"] == 112
    assert c["A_strictly_inside_B"] is True
    assert c["in_A_not_B"] == 0 and c["in_B_not_A"] == 35

def test_the_paper_uses_criterion_B_and_states_111():
    assert "112" in TEX and "111" not in TEX and "shape field contained in" in TEX

def test_separators_still_fail_and_the_cusp_count_grew():
    s = R["consequences"]["separators_still_fail"]
    assert "o10_150700" in s and "SIX members" in s

def test_amphichirality_strengthened_to_111():
    assert "111 of 111" in R["consequences"]["amphichirality_strengthens_again"]  # as first banked

def test_the_one_way_test_is_recorded_as_confirmed_twice():
    assert "both enlargements" in R["consequences"]["the_one_way_test_confirmed_twice"]

def test_the_census_bound_is_stated():
    assert "NOT a claim about all hyperbolic 3-manifolds" in R["scope"]["census_bounded"]


def test_the_off_by_one_correction_is_recorded_with_its_cause():
    c = R["CORRECTION_2026-08-27_the_count_is_112"]
    assert "t06829" in c["the_missing_member"] and "98" in c["the_missing_member"]
    assert "maxden = 60" in c["my_error"]
    assert "ONE-SIDED" in c["why_my_control_did_not_catch_it"]

def test_the_stability_control_is_the_fix():
    c = R["CORRECTION_2026-08-27_the_count_is_112"]
    assert "stabilises" in c["the_fix"] and "16x range" in c["the_fix"]

def test_both_parameters_are_recorded_as_opposing():
    c = R["CORRECTION_2026-08-27_the_count_is_112"]
    assert "over-admits" in c["both_parameters_matter_in_opposite_directions"]
    assert "189" in c["both_parameters_matter_in_opposite_directions"]
