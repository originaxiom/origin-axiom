"""B1180 lock -- cc3's B8147 family retraction adopted; witnesses verified; main corrected by addenda."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_arc_verdict():
    d = json.loads((ROOT / "frontier" / "B1180_family_retraction" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1180" and "RETRACTION ADOPTED IN FULL" in d["claim_one_line"]
    assert "NO tested elementary invariant" in d["claim_one_line"]


def test_addenda_landed():
    a1 = (ROOT / "frontier" / "B1167_seat_harvest" / "ADDENDUM_family_retraction_B8147.md").read_text(encoding="utf-8")
    assert "NOT unique" in a1 and "untouched" in a1.lower()
    a2 = (ROOT / "frontier" / "B1163_w0_attempt" / "ADDENDUM_family_denominator_B8147.md").read_text(encoding="utf-8")
    assert "UNCHECKED" in a2 and "never used the family" in a2


def test_r014_adjudicated_in_results():
    d = json.loads((ROOT / "frontier" / "B1180_family_retraction" / "b1180_results.json").read_text(encoding="utf-8"))
    assert "CONFIRMED" in d["r014_adjudicated"] and "witness corrected" in d["r014_adjudicated"]
    assert "B1168" in d["unaffected"]


def test_reproduce_committed():
    r = (ROOT / "frontier" / "B1180_family_retraction" / "verification" / "reproduce.sh").read_text(encoding="utf-8")
    assert "o10_150700" in r and "REPRODUCES" in r
