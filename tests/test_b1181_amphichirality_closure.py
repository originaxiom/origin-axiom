"""B1181 lock -- the amphichirality debt closed (83/83, cc3) + the one-way family test method-law."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_arc_verdict():
    d = json.loads((ROOT / "frontier" / "B1181_amphichirality_closure" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1181" and "83 OF 83" in d["claim_one_line"]
    assert d["creates_law"] is False  # method-laws live in LAW_MAP sec-G, not the theorem registry
    assert "mirror-isometry" in d["claim_one_line"]  # not the vacuous signature route


def test_law_map_row_and_closures():
    lm = (ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "THE ONE-WAY FAMILY TEST" in lm and "a CLAIM, never a setting" in lm
    a = (ROOT / "frontier" / "B1163_w0_attempt" / "ADDENDUM_family_denominator_B8147.md").read_text(encoding="utf-8")
    assert "83 of 83" in a and "83-of-83" in a
    f = (ROOT / "frontier" / "B1180_family_retraction" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "CLOSURE" in f and "83/83" in f


def test_reproduce_uses_reliable_method():
    r = (ROOT / "frontier" / "B1181_amphichirality_closure" / "verification" / "reproduce.sh").read_text(encoding="utf-8")
    assert "is_isometric_to" in r and "isometry_signature" not in r.replace("not isometry_signature", "")
