"""B8102 — the cusped one-loop gap. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8102_cusped_gap", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_physics_literature_excludes_cusps(r):
    assert r["physics_literature_excludes_cusps"] is True
    assert "cusp-free" in r["excluding_paper"]["scope_quote"]

def test_the_cusped_mathematics_exists(r):
    assert r["cusped_math_exists"] is True
    assert any("ruelle" in p["result"].lower() for p in r["math_papers"])

def test_the_gap_is_a_bridge(r):
    assert r["the_gap_is_a_bridge_not_a_void"] is True

def test_we_hold_the_usually_hard_input(r):
    assert r["we_hold_the_hard_input"] is True
    assert "B739" in r["hard_input"]

def test_the_honest_label_is_needs_specialist(r):
    """Same discipline as L166: abstracts read, not full papers."""
    assert r["honest_label"] == "NEEDS-SPECIALIST-CONFIRMED"
    assert len(r["not_claimed"]) == 3
