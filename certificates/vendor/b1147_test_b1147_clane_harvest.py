"""B1147 lock -- the C-lane harvest: memos 30-40 verified by reproduction on our bench, + the C3
large-ladder honest negative. Fast tests pin b1147_results.json + FINDINGS + the reproduce
evidence; the load-bearing theorems (no-mass-term, third spin derivation) and the memo-34/B1146
convergence are locked as claims of the record."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1147_clane_harvest"


def _d():
    return json.loads((ARC / "b1147_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1147" and d["verdict"] == "PROVED"


def test_all_certs_reproduced():
    r = _d()["reproduce"]
    assert r["failures"] == 0
    assert r["byte_identical_verdict"] + r["clean_run_no_baseline"] == r["total_certs"] == 11


def test_reproduce_evidence_present():
    log = (ARC / "verification" / "reproduce.log").read_text(encoding="utf-8")
    assert log.count("REPRODUCES") == 10
    assert "REPRODUCE_DONE" in log


def test_c3_honest_negative():
    c3 = _d()["c3_large_ladder_our_i9"]
    assert c3["c1_stable_digits"] < c3["recognition_gate_digits"]
    assert "NOT-RECOGNIZED" in c3["verdict"]
    assert "PASS" in c3["sanity_anchor_c0_times_3^0.25"]


def test_load_bearing_theorems_and_convergence():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "no invariant bilinear" in t.lower() and "no mass term" in t.lower()   # memo 32
    assert "THIRD independent derivation" in t or "THIRD derivation" in t          # memo 36
    assert "PROJECTIVE ⟺ EVEN ORBIT" in t or "PROJECTIVE <=> EVEN ORBIT" in t       # memo 34
    assert "B1146" in t and "SEAM-B" in t                                          # the convergence
    assert "gluing note" in t.lower()                                             # memo 33 / B1140
