"""B1188 lock -- the grand-computation retrieval + THE DISCRETE LADDER + the ledger."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1188_grand_retrieval"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1188" and d["verdict"] == "PROVED" and d["instrument"] is True
    c = d["claim_one_line"]
    assert "THE DISCRETE LADDER" in c and "V_reg = Vol(m004)/2" in c
    assert "HELD FOR OWNER ELECTION" in c           # the last licensed row is not auto-fired
    assert "reach DEFICIT" in c                      # the L190 correction carried


def test_ladder_spectrum():
    d = json.loads((ARC / "verification" / "og3_volume_spectrum.json").read_text(encoding="utf-8"))
    assert d["non_half_integer"] == []
    assert sum(d["spectrum_half_integer"].values()) == 112
    assert d["regular_exactness"] is True


def test_ledger_surface():
    t = " ".join((ROOT / "docs" / "GRAND_COMPUTATION_LEDGER.md").read_text(encoding="utf-8").split())
    assert "IMPOSSIBLE-BY-THEOREM" in t and "THE BURIED PRIZE" in t
    assert "B766's T7=T3" in t or "T7=T3" in t        # the live contradiction is registered
    assert "HELD FOR OWNER ELECTION" in t
    assert "DEFICIT of transitive reach" in t


def test_results():
    d = json.loads((ARC / "b1188_results.json").read_text(encoding="utf-8"))
    assert d["ladder"]["exceptions"] == 0 and d["ladder"]["members"] == 112
    assert d["retrievals"]["off_surface_proved"] == 132
