"""B1190 lock -- close-loop batch 2 (the refutation-heavy batch)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1190_close_loop_batch2"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1190" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "KIND ERROR" in c                      # the GC-6 kill named
    assert "zero orphans" in c                    # the GC-7 positive
    assert "rank-4 EXHIBITS STAND" in c or "rank-4 EXISTS" in c
    assert "1/5" in c                             # the honest survival rate


def test_cells_archive():
    d = json.loads((ARC / "verification" / "batch2_cells.json").read_text(encoding="utf-8"))
    assert set(d) == {"GC-6", "GC-7", "GC-8", "GC-9", "GC-10"}
    assert d["GC-7"]["survives"] is True
    assert sum(1 for v in d.values() if v["survives"]) == 1
    assert all(v["refutations"] for k, v in d.items() if not v["survives"])  # every kill has reasons
