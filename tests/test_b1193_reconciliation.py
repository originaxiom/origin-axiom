"""B1193 lock -- the two campaigns reconciled."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_arc():
    d = json.loads((ROOT / "frontier" / "B1193_two_campaigns_reconciled" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED"
    assert "THE FLOOR IS AMENDED" in d["claim_one_line"]
    assert "FOUNDING-BIT IDENTITY" in d["claim_one_line"]


def test_v0_amended():
    t = " ".join((ROOT / "docs" / "GRAND_COMPUTATION_v0.md").read_text(encoding="utf-8").split())
    assert "THE FLOOR AMENDMENT" in t and "PARTIAL-CONTESTED" in t
    assert "the ℙ³ adjudication" in t or "P^3" in t or "ℙ³" in t


def test_ledger_merged_core():
    t = (ROOT / "docs" / "GRAND_COMPUTATION_LEDGER.md").read_text(encoding="utf-8")
    assert "THE MERGED OPEN CORE" in t and "branch↦r" in t
