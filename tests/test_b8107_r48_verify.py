"""B8107 — R48 verification. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8107_r48_verify", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_F1_resolution_verified_not_accepted_on_label(r):
    assert r["F1"]["status"] == "VERIFIED RESOLVED"
    assert "B1100" in r["F1"]["backfill_present"]
    assert r["F1"]["over_wide_rule_killed_before_built"] is True

def test_the_gate_does_not_false_fail_legacy_verdicts(r):
    assert "do not false-fail" in r["F1"]["gate"]

def test_F2_was_scoped_not_deleted(r):
    assert r["F2"]["theorem_survives"] is True
    assert "scoping beside" in r["F2"]["fixed_by"]

def test_F4_is_F1s_pattern_one_iteration_later(r):
    assert r["F4"]["status"] == "NEW" and r["F4"]["severity"] == "LOW"
    assert "creates_law" not in r["F4"]["field_list"]
    assert "structural, not incidental" in r["F4"]["why_it_matters"]

def test_the_mathematics_is_not_claimed_audited(r):
    assert "NO re-derivation" in r["scope"] and "cited as cc's" in r["scope"]
