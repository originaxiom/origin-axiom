"""B8094 — L173 anchors. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8094_L173_anchors", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_scanned_knob_is_the_intercept(r):
    assert "intercept" in r["structural_fact"] and "phason" in r["structural_fact"]

def test_a_falsification_route_exists_on_standard_apparatus(r):
    assert r["falsification_route_exists"] is True
    assert r["knob_is_standard_practice"] is True

def test_anchors_are_cited(r):
    assert len(r["anchors"]) >= 5
    assert any("1403.7124" in a["cite"] for a in r["anchors"])

def test_novelty_is_explicitly_NOT_established(r):
    """The load-bearing honesty: an anchor list is not a novel prediction."""
    assert r["novelty_against_gap_labeling_established"] is False
    assert "RE-DERIVATION" in r["the_discipline"]

def test_precision_is_admitted_missing(r):
    assert r["precision_figures_extracted"] is False
