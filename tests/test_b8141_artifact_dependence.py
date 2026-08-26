"""Lock: the artifact-dependence scan stays honest and its finding stays recorded."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8141_artifact_dependence/results.json").read_text())

def test_the_scan_carries_a_positive_control_that_can_fail():
    src = (ROOT / "scripts/checks/artifact_dependence.py").read_text()
    assert "CONTROL FAILED" in src and "not evidence of absence" in src

def test_the_scan_still_detects_its_control_files():
    r = subprocess.run([sys.executable, "scripts/checks/artifact_dependence.py"],
                       capture_output=True, text=True, cwd=ROOT)
    assert "CONTROL PASSED" in r.stdout, r.stdout[-800:]

def test_the_class_is_distinguished_from_the_cost_class():
    d = R["distinct_from_the_cost_class"]
    assert "never REACHED" in d and "IS reached" in d

def test_the_scans_own_false_negative_is_recorded():
    m = R["my_instrument_failed_first"]
    assert "FALSE NEGATIVE" in m["what_it_reported"]
    assert "POSITIVE CONTROL" in m["hardened"]

def test_legitimate_cases_are_excluded_not_inflated():
    n = R["not_in_this_class"]
    assert "UNTRACKED on purpose" in n["why_legitimate"]

def test_no_remedy_is_claimed():
    assert any("judgements for the arcs' owner" in x for x in R["not_claimed"])


def test_the_manifest_route_is_recorded():
    e = R["extended_2026-08-26_the_manifest_route"]
    assert "STRUCTURALLY BLIND" in e["the_second_route"]
    assert "test_b646_wave2.py" in e["verified_instance"]
    assert len(e["so_the_class_has_two_routes"]) == 2

def test_the_extensions_over_reporting_is_recorded_both_times():
    o = R["extended_2026-08-26_the_manifest_route"]["my_extension_over_reported_twice"]
    assert "EIGHT are read by no test" in o["first"]
    assert "does not read it" in o["second"]

def test_the_scan_is_gated_on_actual_readers():
    src = (ROOT / "scripts/checks/artifact_dependence.py").read_text()
    assert "read by no test" in src or "readers" in src
    assert "mis-attributed" in src
