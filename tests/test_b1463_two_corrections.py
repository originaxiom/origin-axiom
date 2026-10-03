"""B1463 -- the audit lane's AR3 and AR4 re-derived on main."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1463_the_two_early_corrections_re_derived"); V = os.path.join(A, "verification")


def test_live():
    r = subprocess.run([sys.executable, os.path.join(V, "two_corrections.py")], capture_output=True, text=True, cwd=V)
    assert r.returncode == 0 and "VERDICT two-corrections: PASS" in r.stdout, r.stdout[-500:] + r.stderr[-500:]
    d = json.load(open(os.path.join(V, "two_corrections.json")))
    assert d["AR3"]["b37_predicate_is_literal"] and d["AR3"]["predicate_false_on_every_map_in_xyz"] and d["AR3"]["predicate_fires_on_Tprime"]
    assert d["AR4"]["countermodel_k_elimination"] == [] and d["AR4"]["point_alone_k_elimination"] == ["k"]
    assert d["AR4"]["m2"]["krull_no_zero_dim_component"] and all(d["AR4"]["m%d" % m]["hilbert_dimension"] == 1 for m in (2, 3, 4))
    assert d["AR4"]["sage_components"] == {"2": {"n": 2, "dims": [1]}, "3": {"n": 2, "dims": [1]}, "4": {"n": 4, "dims": [1]}}


def test_the_record_carries_it():
    assert os.path.exists(os.path.join(ROOT, "frontier", "B37_operational_feedback_quarantine", "ADDENDUM_2026-10-03_the_detector_could_not_fire.md"))
    assert os.path.exists(os.path.join(ROOT, "frontier", "B130_no_forced_choice", "ADDENDUM_2026-10-03_the_inference_and_the_conclusion.md"))
    g = open(os.path.join(ROOT, "GENESIS.md")).read(); assert "- **v1.8 · 2026-10-03 · main B1463.**" in g
    sage = open(os.path.join(V, "b130_components_sage.out")).read(); assert sage.count("component dim 1") == 8 and "component dim 0" not in sage
