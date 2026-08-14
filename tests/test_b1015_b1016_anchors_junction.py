"""B1015/B1016 — locks: the anchor set stays declared, the junction stays SEPARATE."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_the_anchor_set_is_declared_and_binding():
    d = (ROOT / "frontier" / "B1015_anchor_declaration" / "DECLARATION.md").read_text()
    flat = " ".join(d.lower().split())
    assert "a1 (dimensionful): ℓ" in flat or "a1 (dimensionful)" in flat
    assert "c — the central charge" in d or "c = 6σ" in d.replace("6 σ", "6σ") or "unquantized" in flat
    assert "re-declaration" in flat, "changing anchors must stay a new sealed act"
    assert "anchor-free" in flat, "the coupling channel's zero-anchor property must stay recorded"


def test_the_junction_verdict_is_separate_and_recomputed():
    r = json.loads((ROOT / "frontier" / "B1016_l150_junction" / "results.json").read_text())
    assert r["verdict"] == "SEPARATE"
    assert r["O1"]["O1_obstruction_holds"] == "True"
    assert r["O2"]["O2_obstruction_holds"] == "True"
    # the recomputation must keep re-deriving the banked pencil field from raw coefficients:
    assert r["O1"]["W3_disc_core"] == "3129"


def test_the_junction_recompute_runs_exact():
    sys.path.insert(0, str(ROOT / "frontier" / "B1016_l150_junction"))
    from junction import j1_pair_inventory, j2_field_obstruction, j2_module_obstruction
    inv = j1_pair_inventory()
    o1 = j2_field_obstruction(inv)
    assert o1["O1_obstruction_holds"] is True
    assert o1["all_listed_values_rational"] is True
    assert j2_module_obstruction()["O2_obstruction_holds"] is True


def test_the_channel_rule_is_in_the_requirements():
    t = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text()
    flat = " ".join(t.lower().split())
    assert "declare its channel" in flat
    assert "channel-mixing without an explicit banked bridge is forbidden" in flat
    assert "done — b1015" in flat and "done — b1016" in flat


def test_the_falsifier_scope_note_is_actioned_not_deleted():
    t = (ROOT / "docs" / "WHAT_WOULD_COUNT.md").read_text()
    flat = " ".join(t.lower().split())
    assert "actioned by b1016" in flat
    assert "not admitted as live" in flat and "not excluded" in flat, (
        "the weighing must stay two-sided — neither promotion nor burial")
