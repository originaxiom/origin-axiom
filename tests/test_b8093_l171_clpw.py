"""B8093 — L171 typed MOOD not MATCH. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8093_L171_clpw", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_typing_is_mood_not_match(r):
    assert r["typing"] == "MOOD" and r["is_match"] is False

def test_criterion_a_is_a_disanalogy_about_modular_flow(r):
    """Their engine is ergodic modular flow; ours is trivial -- the opposite hypothesis."""
    a = r["criteria"]["a_crossed_product_over"]
    assert a["verdict"] == "DISANALOGY"
    assert "ERGODIC" in a["why"] and "TRIVIAL" in a["why"]

def test_criterion_b_is_unresolved_and_flagged_decisive(r):
    b = r["criteria"]["b_observer_machinery"]
    assert b["verdict"] == "UNRESOLVED" and b["is_decisive_test"] is True

def test_criterion_c_is_near_vacuous_by_uniqueness(r):
    assert r["criteria"]["c_max_entropy_tracial_state"]["verdict"] == "NEAR-VACUOUS"

def test_the_positivity_is_what_makes_it_II1(r):
    assert r["their_crossed_product_type"] == "II_infinity"
    assert r["their_final_type"] == "II_1"
    assert "Theta(q)" in r["what_converts_IIinf_to_II1"]

def test_scope_admits_what_was_not_read(r):
    assert r["successor_literature_read"] is False
    assert r["lanes_2_to_6_started"] is False
