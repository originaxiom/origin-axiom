"""B1158 lock -- Cloud WAVE-2 harvest: the exact-law C4 closure (B1151 surmise hatch falsified, residual
quarantined), the anomaly integer identity (dark block = -(16), 'required' quarantined), the Habiro zeta_3
germ correction (mechanism solved), and two cross-seat convergences (codex R011==B1157, R012==cloud
ANOMALY_PAYMENT). Asserts on COMMITTED files only. Own reproducer for the two clean survivors. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1158_cloud_wave2_harvest"


def _d():
    return json.loads((ARC / "b1158_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1158" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_gaudin_falsifies_surmise_hatch_scoped():
    g = _d()["survivor_1_gaudin_C4"]
    assert "FALSIFIED" in g["claim"] and "B1151" in g["claim"]
    assert "law-robust" in g["claim"].lower().replace("law-robust", "LAW-ROBUST").lower() or "LAW-ROBUST" in g["claim"]
    # the residual is quarantined, not banked
    assert "Does NOT bank 'the residual is real.'" in g["scoped"]
    assert "sole live suspect" in g["scoped"].lower() or "SOLE live suspect" in g["scoped"]


def test_anomaly_integer_identity_quarantined_headline():
    a = _d()["survivor_2_anomaly_identity"]
    assert "27 = 16(+1) (+) 10(-2) (+) 1(+4)" in a["claim_INTEGER_IDENTITY"]
    assert "anomaly-free in ALL three channels" in a["claim_INTEGER_IDENTITY"]
    # the 'required' headline is quarantined as conditional
    assert "CONDITIONAL" in a["quarantined"] and "Gate 5" in a["quarantined"]
    assert "OA-C1087" in a["quarantined"]


def test_habiro_correction_mechanism_solved():
    h = _d()["survivor_3_habiro_correction"]
    assert "CORRECTS the memo" in h["reproduced"]
    assert "p^r = 1 mod 3" in h["claim"] and "BASE-EMBEDDING ARTIFACT" in h["claim"]
    assert "f=2 for p=5" in h["claim"] and "g=2 for p=7" in h["claim"]
    assert "Credit CLOUD" in h["provenance"]


def test_convergence_1_corroborates_b1157():
    c = _d()["convergence_1_R011_equals_B1157"]
    assert "CORROBORATES B1157" in c["verdict"]
    assert "k=2 fault line" in c["verdict"]
    assert "do NOT re-bank" in c["action"] or "ALREADY-COVERED" in c["action"]


def test_convergence_2_consistent():
    c = _d()["convergence_2_R012_equals_ANOMALY_PAYMENT"]
    assert "CONSISTENT" in c["verdict"]
    assert "identical" in c["detail"].lower() or "IDENTICAL" in c["detail"]


def test_codex_relayed_not_banked_r014_refuted():
    r = _d()["relayed_to_cc3_owner_gated"]
    assert "owner-gated" in r["note"] and "NOT banked" in r["note"]
    assert "BOTH literal claims REFUTED" in r["R014"] and "s955" in r["R014"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "harvest_checks.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out
    assert "grav^2-U(1)  = sum dim*q   = 0" in out
    assert "coherence r=2" in out and "coherence r=1" in out


def test_gate5_clean_no_crossing():
    d = _d()
    assert "No firewall crossing" in d["fences"] and d["gate5"].startswith("clean")
