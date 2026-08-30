"""B1199 lock -- the register reads + L188 closed."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1199_register_reads_and_L188"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1199" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "THE OPENNESS IS STALE" in c
    assert "FOURTH FINISHED-BUT-FORGOTTEN" in c
    assert "IS WITHDRAWN" in c                      # the failed control, not smoothed
    assert "NO NOTE IS BANKED" in c                 # R6's refutation honored
    assert "HOLDS EXACTLY" in c                     # C3's first-ever check


def test_results():
    d = json.loads((ARC / "b1199_results.json").read_text(encoding="utf-8"))
    assert d["finished_but_forgotten_count"] == 4
    assert "NOT cosmological dark matter" in d["GC-29"]["fence"]
    assert d["GC-30"]["R6"].startswith("REFUTED")
    assert "CLOSED" in d["GC-31"]["L188"]


def test_cells_archived():
    d = json.loads((ARC / "verification" / "cells.json").read_text(encoding="utf-8"))
    assert set(d) == {"GC-29", "GC-30", "GC-31"}
    assert d["GC-31"]["survives"] is True
