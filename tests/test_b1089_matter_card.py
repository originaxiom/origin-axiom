"""B1089 lock: the matter card's numbers pin to their source arcs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _v(arc):
    return json.load(open(next((ROOT / "frontier").glob(arc + "_*")) / "arc_verdict.json"))

def test_sources_exist_and_say_what_the_card_quotes():
    law = _v("B1086")["claim_one_line"]
    assert "5 untwisted" in law and "2 for ANY theta-odd" in law
    charge = _v("B1087")["claim_one_line"]
    assert "1+8+9+8+1" in charge and "cannot be" in charge.lower() or "unmeasurable" in charge.lower()
    edge = _v("B1085")["claim_one_line"]
    assert "5-vs-6" in edge
    card = _v("B1089")["claim_one_line"]
    assert "NOT generations" in card and "vector-like" in card

def test_card_is_object_arc():
    assert _v("B1089")["instrument"] is False
