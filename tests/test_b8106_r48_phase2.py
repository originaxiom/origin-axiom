"""B8106 — R48 phase 2. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8106_r48_phase2", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_window_is_the_frozen_one(r):
    assert r["window_head"] == "07e46c7f" and r["mode"] == "COLD"

def test_the_theorem_is_affirmed_not_attacked(r):
    """The finding is precise: the theorem is right, the consequence is stale."""
    f = r["verified_findings"][0]
    assert f["the_theorem_is_correct"] is True
    assert f["the_consequence_is_stale"] is True
    assert "NILPOTENT" in f["theorem"]

def test_the_wave_missed_this_ledger(r):
    f = r["verified_findings"][0]
    assert r["wave_touched_gut_ledger"] is False and r["wave_touched"] == 13
    assert "SM_SPECIFICATION_LEDGER.md but NOT" in f["sharpness"]

def test_the_staleness_runs_pessimistic(r):
    assert r["verified_findings"][0]["direction"].startswith("PESSIMISTIC")

def test_it_is_a_repeat_offender(r):
    assert "second occurrence" in r["verified_findings"][0]["repeat_offender"]

def test_B1102_is_excluded_as_post_boundary(r):
    assert any("B1102" in n for n in r["not_claimed"])
