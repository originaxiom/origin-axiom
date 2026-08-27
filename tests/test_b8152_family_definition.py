"""Lock: the family is 111 under the paper's own criterion, and the criteria are nested."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8152_family_definition/results.json").read_text())
TEX = (ROOT / "papers/series/paper4_what_cannot_be_supplied/main.tex").read_text()

def test_the_two_criteria_are_nested_not_equal():
    c = R["the_two_criteria"]
    assert c["A_all_regular_ideal"] == 77 and c["B_shape_field_in_Qsqrt3"] == 111
    assert c["A_strictly_inside_B"] is True
    assert c["in_A_not_B"] == 0 and c["in_B_not_A"] == 34

def test_the_paper_uses_criterion_B_and_states_111():
    assert "111" in TEX and "shape field contained in" in TEX

def test_separators_still_fail_and_the_cusp_count_grew():
    s = R["consequences"]["separators_still_fail"]
    assert "o10_150700" in s and "SIX members" in s

def test_amphichirality_strengthened_to_111():
    assert "111 of 111" in R["consequences"]["amphichirality_strengthens_again"]

def test_the_one_way_test_is_recorded_as_confirmed_twice():
    assert "both enlargements" in R["consequences"]["the_one_way_test_confirmed_twice"]

def test_the_census_bound_is_stated():
    assert "NOT a claim about all hyperbolic 3-manifolds" in R["scope"]["census_bounded"]
