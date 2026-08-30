"""B1197 lock -- the clock-coherence run (the D2 gate)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1197_clock_coherence"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1197" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "SPLIT VERDICT" in c
    assert "VACUITY TRAP" in c and "WRONG CENSUS" in c      # both catches narrated
    assert "156/156" in c                                    # the banked-positive control


def test_results_shape():
    d = json.loads((ARC / "b1197_results.json").read_text(encoding="utf-8"))
    assert d["ladder"]["vol_monotone_increasing"] is True
    assert d["ladder"]["abs_cs_monotone_decreasing"] is True
    assert d["census"]["distinct_closings"] == 78            # B289's census reproduced
    assert d["census"]["global_monotone"] is False
    assert d["controls"]["shuffle_detector_violations"] > 0  # the detector bites


def test_committed_data():
    g = json.loads((ARC / "verification" / "b4_global.json").read_text(encoding="utf-8"))
    assert g["n_closings"] == 78 and g["n_violations"] == 15
    assert g["per_family"]["1"] is True
