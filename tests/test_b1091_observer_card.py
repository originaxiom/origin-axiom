"""B1091 lock: the observer card's rows pin to their sources."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _v(arc):
    return json.load(open(next((ROOT / "frontier").glob(arc + "_*")) / "arc_verdict.json"))

def test_negative_half_sources():
    assert "cannot be" in _v("B1087")["claim_one_line"].lower() or "unmeasurable" in _v("B1087")["claim_one_line"].lower()
    assert "IDS" in _v("B1085")["claim_one_line"] or "blind" in _v("B1085")["claim_one_line"]

def test_card_synthesis_and_campaign_state():
    c = _v("B1091")["claim_one_line"]
    assert "observer IS the cut" in c
    assert "C1-C4" in c and "C5 fenced" in c
    assert _v("B1091")["instrument"] is False and _v("B1090")["instrument"] is False
