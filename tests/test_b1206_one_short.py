"""B1206 lock -- the cut ledger on the P^3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1206_one_condition_short"


def test_the_cut_ledger_arithmetic():
    d = json.loads((ARC / "b1206_results.json").read_text(encoding="utf-8"))
    L = d["cut_ledger"]
    assert L["start"] == 3
    assert L["after_linear"] == L["start"] - d["canonical_linear_functionals"] == 2
    assert L["after_cubic"] == 1 and L["needed_for_points"] == 0
    assert "ONE CONDITION SHORT" in L["verdict"]


def test_verdict_fences_the_physics():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "OPEN"
    c = d["claim_one_line"]
    assert "COUNT OF AVAILABLE STRUCTURE, not a physics claim" in c
    assert "nothing here says the lambda-term must vanish" in c
    assert "THE LEDGER CLOSES IMMEDIATELY" in c        # the cheapest route named
    assert "Nothing weakens V-3" in c
