"""B1191 lock -- close-loop batch 3: THE GRAND COMPUTATION v0."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1191_close_loop_batch3"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1191" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "FINGERPRINT ROUTE IS DEAD" in c
    assert "SIXTH LEG" in c and "ALL-complex" in c
    assert "F2/F8 ALREADY BANKED" in c


def test_v0_document():
    t = " ".join((ROOT / "docs" / "GRAND_COMPUTATION_v0.md").read_text(encoding="utf-8").split())
    assert "HELD FOR OWNER ELECTION" in t           # I3 carried
    assert "B279" in t and "spin" in t.lower()      # F3 carried
    assert "SIXTH leg" in t or "SIXTH" in t         # the gamma5 amendment
    assert "S(member n)" in t or "V_reg" in t       # the own-unit action


def test_cells_archive():
    d = json.loads((ARC / "verification" / "batch3_cells.json").read_text(encoding="utf-8"))
    assert set(d) == {"GC-11", "GC-12", "GC-13", "GC-14", "GC-15"}
    assert sum(1 for v in d.values() if v["survives"]) == 3
