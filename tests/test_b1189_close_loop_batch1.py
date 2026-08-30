"""B1189 lock -- close-loop batch 1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1189_close_loop_batch1"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1189" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "NORM-MINUS-ONE FUNDAMENTAL UNIT" in c        # the GC-2 mechanism
    assert "DEEPER than commensurability" in c            # the GC-1 reversal
    assert "z ~ 49-59" in c                               # the GC-4 law's strength
    assert "boolean slip" in c                            # the verify-side honesty


def test_cells_archive():
    d = json.loads((ARC / "verification" / "batch1_cells.json").read_text(encoding="utf-8"))
    assert set(d) == {"GC-1", "GC-2", "GC-3", "GC-4", "GC-5"}
    assert d["GC-2"]["verdict"] == "NEGATIVE" and d["GC-1"]["verdict"] == "PARTIAL"
    assert "det(B) = -1 = N(phi)" in d["GC-2"]["evidence"]


def test_eleven_nonarithmetic():
    r = json.loads((ARC / "b1189_results.json").read_text(encoding="utf-8"))
    assert "11 non-arithmetic" in r["cells"]["GC-1"]
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for name in ("t06829", "o9_41005", "v2875"):
        assert name in t
