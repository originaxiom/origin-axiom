"""B1101 lock -- THE CERTIFICATION ENVELOPE (governance adoption). The R48 gate-audit
found B1101 had no dedicated lock (coverage was indirect only); this asserts its
arc_verdict and the adopted rule's FINDINGS, so the adoption record cannot silently drift."""
import json
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1101_certification_envelope"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1101"
    assert d["verdict"] == "PROVED"
    assert "CERTIFICATION ENVELOPE" in d["claim_one_line"]
    assert d["instrument"] is True
    assert d["creates_law"] is False


def test_findings_states_the_rule():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "CERTIFICATION ENVELOPE" in f
    assert "working tree is read-only" in f
    assert "fold-forward" in f
