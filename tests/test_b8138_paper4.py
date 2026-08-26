"""Lock: Paper IV's banked claims match the paper and its verification."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8138_paper4_drafted/results.json").read_text())

def test_every_no_go_carries_an_escape():
    for k, v in R["three_theorems"].items():
        assert "escape" in v and v["escape"], k

def test_the_scale_theorem_is_not_overstated():
    e = R["three_theorems"]["scale"]["escape"]
    assert "DIMENSIONLESS" in e and "FALSE" in e

def test_the_orbit_escapes_are_exactly_two_and_exhaustive():
    o = R["three_theorems"]["orbit"]
    assert "exactly TWO" in o["escape"] and "Exhaustive because" in o["escape"]
    assert "WRONG TYPE" in o["why_a_theorem_not_a_gap"]

def test_the_volume_identity_is_recorded_as_family_level():
    f = R["three_theorems"]["family"]
    assert f["shared"]["volume"] == ["m003"]
    assert "FAMILY property" in f["corollary_volume"]
    assert "FAMILY-LEVEL input" in f["corollary_input"]

def test_both_errors_are_reported_with_why_they_were_invisible():
    e = R["two_errors_reported_in_the_paper"]
    assert "FLATTERED" in e["float_equality_on_CS"]
    assert "answers a different question" in e["neighbouring_property"]

def test_the_family_table_was_regenerated_not_quoted():
    v = R["verification"]
    assert v["passed"] == v["checks"] == 7
    assert "regenerated from the census" in v["independent_reproduction"]
    assert any("amphichirality claim" in c and "tested, not asserted" in c for c in v["controls"])
