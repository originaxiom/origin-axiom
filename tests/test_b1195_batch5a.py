"""B1195 lock -- batch 5A."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_arc():
    d = json.loads((ROOT / "frontier" / "B1195_close_loop_batch5a" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "FOUNDING QUADRATIC" in c and "LAMBDA PLACED" in c
    assert "ONE INVARIANT" in c and "PERMANENT-AT-CURRENT-KNOWLEDGE" in c

def test_cells():
    d = json.loads((ROOT / "frontier" / "B1195_close_loop_batch5a" / "verification" / "batch5a_cells.json").read_text(encoding="utf-8"))
    assert len(d) == 5
