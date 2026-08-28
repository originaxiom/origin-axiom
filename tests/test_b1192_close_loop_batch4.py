"""B1192 lock -- THE RELATIONAL BIT EXISTS."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1192_close_loop_batch4"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1192" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "THE RELATIONAL BIT EXISTS" in c
    assert "SINGLE-SIGNED" in c and "RESTRICTS TO c" in c
    assert "QUANTIFIER CORRECTION ADOPTED" in c        # the lens honored
    assert "FIRST REALIZED INSTANCE" in c


def test_gc16_exactness():
    d = json.loads((ARC / "verification" / "batch4_cells.json").read_text(encoding="utf-8"))
    ev = d["GC-16"]["evidence"]
    assert "X0=[[2,-3],[1,-2]]" in ev.replace(" ", "") or "[[2,-3],[1,-2]]" in ev
    assert "340" in ev                                  # trace invisibility
    assert "43/43" in ev
    assert d["GC-20"]["survives"] is True
