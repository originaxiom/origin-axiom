"""Lock: the L171 verification, its extension, and the search failure that prompted it."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8145_l171_verified/results.json").read_text())

def test_all_eight_claims_were_checked_against_the_source():
    c = R["eight_claims_checked_against_source"]
    assert len(c) == 8
    assert all(v.startswith("CONFIRMED") for v in c.values())

def test_the_verbatim_matches_include_the_fine_detail():
    c = R["eight_claims_checked_against_source"]
    assert "R_+ not R" in c["observer = clock, H_obs = q >= 0, L^2(R_+)"]
    assert "VERBATIM" in c["positivity projection Pi = Theta(q), Tr 1 = 1"]

def test_the_typing_is_re_derived_not_assumed():
    t = R["typing_re_derived"]
    assert "Tomita-Takesaki" in t["a_crossed_product_over"]
    assert "trap cc pre-declared" in t["c_max_entropy_tracial_state"]
    assert "MOOD is correct" in t["verdict"]

def test_the_disclosed_gap_is_filled_and_the_reason_relocates():
    g = R["the_disclosed_gap_now_filled"]
    assert "NOT explicitly a crossed product" in g["what_the_successor_does"]
    assert "SCOPED TO CLPW" in g["consequence_for_the_typing"]
    assert g["does_MOOD_survive"].startswith("YES")
    assert "RELOCATES" in g["does_MOOD_survive"]

def test_my_search_failure_is_recorded_as_the_reason_for_this_arc():
    w = R["why_this_arc_exists"]
    assert "head -8" in w and "truncation as absence" in w

def test_nothing_overclaimed_about_the_successor():
    assert "ONE FETCH" in R["scope"]
    assert any("does not change MOOD" in x or "does not" in x for x in R["not_claimed"])
