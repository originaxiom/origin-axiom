"""B1148 lock -- the carrier harvest: cloud memos 41-48 reproduce-verified. The batch's load-bearing
cells (the only-spinor no-go, the carrier Psi=C^2 (x) 27 lock, the Yukawa shape theorem, the coupling
uniqueness) and the freedom ledger are locked as claims of the record, with the honest fence that the
internal->spacetime bridge is NOT closed."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1148_carrier_harvest"


def _d():
    return json.loads((ARC / "b1148_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1148" and d["verdict"] == "PROVED"


def test_all_eight_reproduced():
    r = _d()["reproduce"]
    assert r["failures"] == 0 and r["byte_identical_verdict"] == r["total_certs"] == 8


def test_reproduce_evidence_present():
    log = (ARC / "verification" / "reproduce.log").read_text(encoding="utf-8")
    assert log.count("REPRODUCES") == 8 and "DONE" in log


def test_carrier_and_yukawa_and_ledger():
    d = _d()["memos"]
    assert "C^2 (x) 27" in d["46"] and "matter sector" in d["46"]        # the carrier lock
    assert "SHAPE is a theorem" in d["47"] and "Gate 5" in d["47"]       # the Yukawa shape/value split
    assert "ONLY spin-1/2" in d["45"] and "no-go half" in d["45"]        # the only-spinor no-go
    assert "NO shape assumption" in d["48"] and "6615" in d["48"]        # the coupling uniqueness
    assert "4 audited columns" in d["42"] and "the beat" in d["42"]      # the freedom ledger


def test_bridge_not_closed_and_convergences():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "bridge is NOT closed" in t or "bridge is **NOT closed**" in t
    assert "B1146" in t and "SEAM-B" in t                                # the convergence
    assert "codex" in t.lower() and "memo-30" in t.lower()               # codex R003 cross-verification
    fences = _d()["fences"]
    assert "no field" in fences and "no value" in fences                 # Gate 5 fence
