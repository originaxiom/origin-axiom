"""B8109 — R48 close. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8109_r48_close", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_four_findings_three_resolved(r):
    assert len(r["findings"]) == 4
    assert sum(1 for f in r["findings"] if f["status"].startswith("RESOLVED")) == 3

def test_phases_3_and_4_found_nothing_new(r):
    assert r["new_findings_phase_3_and_4"] == 0

def test_the_lag_scan_is_recorded_as_the_wrong_instrument(r):
    m = r["methodological_finding"]
    assert "WRONG INSTRUMENT" in m["lag_scan"] and "6%" in m["lag_scan"]
    assert "7 of 13" in m["banner_discriminator"]

def test_the_negative_rests_on_a_passing_positive_control(r):
    assert "PASSING positive control" in r["methodological_finding"]["what_worked"]
    assert "uncontrolled scan is worthless" in r["methodological_finding"]["principle"]

def test_the_false_zero_is_owned(r):
    assert "hard-wrap" in r["instrument_failure_self_caught"]
    assert "Second false-zero" in r["instrument_failure_self_caught"]

def test_no_document_was_edited_and_lag_is_not_deferred(r):
    assert "NO document was edited" in r["scope"]
    assert "not a deferral" in r["scope"]
