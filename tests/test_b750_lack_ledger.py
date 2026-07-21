"""Locks for B750 -- the lack ledger (integrity of the machine-checkable ledger)."""
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEDGER = os.path.join(ROOT, "frontier", "B750_lack_ledger", "ledger.json")


def _ledger():
    with open(LEDGER, encoding="utf-8") as fh:
        return json.load(fh)


def test_verdict_unified_three_classes_x_empty():
    L = _ledger()
    assert L["verdict"] == "UNIFIED-3"
    assert L["X"] == []
    classes = {e["class"] for e in L["entries"]}
    assert classes == {"T", "R", "P"}
    counts = {c: sum(1 for e in L["entries"] if e["class"] == c) for c in classes}
    assert counts == {"T": 8, "R": 3, "P": 2}


def test_every_entry_cites_an_existing_banked_artifact():
    L = _ledger()
    for e in L["entries"]:
        path = e["citation"].split("in-repo witnesses: ")[-1]
        assert os.path.exists(os.path.join(ROOT, path)), e["id"]


def test_each_class_has_a_banked_can_fail_witness():
    L = _ledger()
    assert set(L["can_fail_witnesses"]) == {"T", "R", "P"}
    for w in L["can_fail_witnesses"].values():
        assert os.path.exists(os.path.join(ROOT, w["citation"]))


def test_admission_rule_demonstrably_excludes():
    L = _ledger()
    assert any("B733" in x["candidate"] for x in L["excluded_by_criteria"])
    ids = {e["id"] for e in L["entries"]}
    assert not any("B733" in e["refusal"] for e in L["entries"])
    assert len(ids) == len(L["entries"])                      # no duplicate ids
