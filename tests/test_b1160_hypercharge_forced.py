"""B1160 lock -- hypercharge falls out (cloud memo 70 / L132, verified): on an SM-shaped 15-plet the four
anomaly conditions force the SM hypercharge, unique up to scale + uc<->dc, zero non-SM. Structure not value
(B950); Gate 5 clean. Pays hypercharge CONTENT, not frame existence. Asserts on COMMITTED files only."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1160_hypercharge_forced"


def _d():
    return json.loads((ARC / "b1160_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1160" and d["verdict"] == "PROVED"
    assert d["instrument"] is False and d["creates_law"] is False


def test_core_verified_unique_sm_hypercharge():
    c = _d()["verified_core_own"]
    assert "-18(t-3)(t+3)" in c and "t=+-3 ONLY" in c
    assert "(1,-4,2,-3,6) [SM]" in c and "(1,2,-4,-3,6) [SM uc<->dc]" in c
    assert "UNIQUE anomaly-consistent Y" in c


def test_scope_pays_content_not_frame():
    d = _d()
    assert "CONTENT is forced by integer arithmetic" in d["scope_pays"]
    assert "sharpen" in d["scope_pays"].lower() or "Sharpens B1159 link C" in d["scope_pays"]
    joined = " ".join(d["scope_does_not_pay"])
    assert "FRAME EXISTENCE" in joined and "observer inputs" in joined
    assert "STANDARD GUT" in joined


def test_firewall_structure_not_value():
    f = _d()["firewall_gate5"]
    assert "STRUCTURE, not value-matching" in f and "B950" in f
    assert "No measured value asserted as derived" in f and "Gate 5 clean" in f


def test_cloud_credited_provenance():
    d = _d()
    assert "cloud seat memo 70" in d["source"] and "cloud credited" in d["source"].lower()
    assert "CITED" in d["provenance"] and "own-verified" in d["provenance"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "hypercharge_check.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out
    assert "-18*(t - 3)*(t + 3)" in out
    assert "(1, -4, 2, -3, 6)   SM" in out
