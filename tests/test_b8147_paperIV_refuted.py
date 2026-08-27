"""Lock: Paper IV's separator retraction, its witnesses, and the downstream cascade."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8147_paperIV_refuted/results.json").read_text())

def test_the_verdict_is_retracted():
    v = json.loads((ROOT / "frontier/B8147_paperIV_refuted/arc_verdict.json").read_text())
    assert v["verdict"] == "RETRACTED"

def test_both_separators_have_named_witnesses():
    r = R["refutations"]
    assert r["H1_is_Z"]["witness"] == "o10_150700"
    assert r["H1_is_Z"]["clean"].startswith("YES")
    assert len(r["cusp_shape_2sqrt3i"]["witnesses"]) == 4

def test_the_weaker_claim_is_not_silently_retreated_to():
    n = R["refutations"]["cusp_shape_2sqrt3i"]["nuance"]
    assert "DIFFERENT claim" in n and "untested" in n

def test_R014_is_credited_but_its_witness_corrected():
    v = R["R014_verdict"]
    assert "RIGHT ON THE CONCLUSION" in v and "WRONG ON THE WITNESS" in v

def test_the_family_size_is_a_lower_bound_not_a_claim():
    assert "LOWER BOUND" in R["the_root_defect"]["status_of_83"]

def test_what_survives_is_recorded_as_strengthened():
    assert any("STRENGTHENED" in x for x in R["what_survives"])

def test_the_downstream_cascade_to_cc_is_recorded():
    c = R["downstream_cascade"]
    assert "not 14" in c["my_B1163_relay"]
    assert "UNAFFECTED" in c["B1163_theorem_itself"]

def test_my_own_two_failures_are_recorded():
    f = R["my_failure"]
    assert "never tested it for completeness" in f["first"]
    assert "inbound relay queue" in f["second"]
