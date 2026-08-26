"""Lock: the price-ledger reconciliation stays open and stays symmetric."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8144_price_reconciliation/results.json").read_text())

def test_both_ledgers_are_recorded_in_full():
    assert len(R["banked_price_ledger"]["items"]) == 4
    assert len(R["B1164_census"]["items"]) == 3

def test_the_two_missing_items_are_named_with_their_evidence():
    m = R["reconciliation"]["missing_from_B1164"]
    assert "time's arrow" in m and "0 hits" in m["time's arrow"]
    assert "the VEV orbit-point" in m and "0 hits" in m["the VEV orbit-point"]

def test_the_bite_is_the_archimedean_thesis():
    w = R["reconciliation"]["why_it_bites"]
    assert "FINITE OVER Z" in w and "ARCHIMEDEAN" in w
    assert "over-counts" in w

def test_the_arc_decides_neither_ledger():
    nc = R["not_claimed"]
    assert any("which ledger is right" in x for x in nc)
    assert any("may already exist" in x or "does not already exist" in x for x in nc)

def test_the_verdict_is_open():
    v = json.loads((ROOT / "frontier/B8144_price_reconciliation/arc_verdict.json").read_text())
    assert v["verdict"] == "OPEN"
