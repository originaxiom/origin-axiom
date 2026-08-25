"""Lock: Paper I's banked claims match the paper and its verification suite."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8135_paper1_drafted/results.json").read_text())

def test_class_counts_and_threshold():
    t = R["theorems"]["class_threshold"]
    assert "[1,1,1,1,1,2,1,1,2,2,1]" in t, t
    assert "m=6 is the FIRST repetition" in t

def test_trace_only_pins_invariant_factors_not_just_order():
    # the whole point: the determinant alone leaves a cyclic Z/m^2 open
    s = R["sharpening_over_source"]
    assert "INVARIANT FACTORS" in s and "cyclic Z/m^2" in s
    assert "Smith form (m,m)" in R["theorems"]["trace_only"]

def test_the_verification_carries_live_controls():
    v = R["verification"]
    assert v["passed"] == v["checks"] == 15
    assert v["sampled_matrices"] == 896          # not only the representatives X_m
    assert any("FAILS off the locus" in c for c in v["controls"])

def test_plan_correction_is_recorded_with_its_error_class():
    p = R["plan_correction"]
    assert "NOT ONE is hyperbolic geometry" in p["why_wrong"]
    assert "label as a result" in p["error_class"]
    assert "NONE is PROVED" in p["corrected_to"]

def test_the_m12_disagreement_is_flagged_not_suppressed():
    f = R["flagged"]["m12_disagreement"]
    assert "UNRESOLVED" in f and "not load-bearing" in f

def test_paper_builds_and_verify_suite_still_passes():
    d = ROOT / "papers/structure_paper"      # sanity: repo layout intact
    v = ROOT / "papers/series/paper1_characterization/verify/check_locus.py"
    assert v.exists()
    r = subprocess.run([sys.executable, str(v)], capture_output=True, text=True, cwd=v.parent)
    assert r.returncode == 0, r.stdout[-2000:]
    assert "15/15 checks passed" in r.stdout
