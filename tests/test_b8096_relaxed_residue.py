"""B8096 — the relaxed residue hunt. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8096_relaxed_residue", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_guard_was_actually_relaxed(r):
    g = r["guard_relaxed"]
    assert "frame-invariance only" in g and "nativeness" in g

def test_outcome_B_no_survivors(r):
    assert r["outcome"] == "B" and r["n_survivors"] == 0

def test_the_77_appeared(r):
    assert r["77_divides_product"] is True
    assert r["denominator_product"] == 413 * 3047 * 953

def test_and_the_77_is_vacuous_by_the_preregistered_control(r):
    """Second 77 to die to the same control: forced by per-element facts."""
    assert r["77_forced_by_per_element_facts"] is True
    assert "VACUOUS" in r["77_verdict"]

def test_scope_does_not_claim_the_guard_is_vindicated(r):
    assert "B8092 finding 1 only" in r["scope"]
    assert "owner's general claim" in r["scope"]
