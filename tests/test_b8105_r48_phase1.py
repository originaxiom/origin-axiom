"""B8105 — R48 phase 1. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8105_r48_phase1", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_modulus_is_declared(r):
    """cc3 is not fully cold on this window and says so."""
    assert r["mode"] == "COLD" and "NOT cold" in r["modulus"]

def test_it_runs_against_main_not_the_working_tree(r):
    assert r["run_against"] == "origin/main"
    assert any("working tree is not the corpus" in m["issue"] for m in r["method_corrections"])

def test_snapshots_are_not_counted_as_defects(r):
    assert r["dated_snapshots_not_defects"] == 21
    assert r["undated_live_surfaces"] == 36
    assert r["lagging_over_100"] == 57

def test_lag_is_flagged_as_candidates_not_verdicts(r):
    assert "CANDIDATE-GENERATOR" in r["caveat"]

def test_the_registry_violates_its_own_rule(r):
    f = r["verified_findings"][0]
    assert f["surface"] == "docs/THEOREM_REGISTRY.md"
    assert "IN THE SAME PR" in f["its_own_rule"]
    assert f["tops_out_at"] == 920 and f["corpus_tip"] == 1099
    assert "B1012" in f["verified_absent"]

def test_no_gate_reads_that_rule(r):
    assert "no gate reads that rule" in r["verified_findings"][0]["why_unenforced"]
