"""B1013 — locks: the sort stays, the one real wall stays a wall, the burdens stay open."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_the_sort_is_in_the_framework_and_values_stay_the_real_wall():
    t = (ROOT / "docs" / "THE_FRAMEWORK.md").read_text(encoding="utf-8")
    assert "RE-SORTED 2026-08-10" in t
    assert "THE ONE REAL WALL" in t, "the value wall must keep its name"
    assert "No reframing touches a measurement" in t or "no reframing touches a measurement" in t.lower()
    flat = " ".join(t.lower().replace(">", " ").split())
    assert "relocated burden" in flat, "the burdens must stay named open accounts"


def test_the_criterion_rule_is_in_what_would_count():
    t = (ROOT / "docs" / "WHAT_WOULD_COUNT.md").read_text(encoding="utf-8")
    assert "SPECIFICATION" in t and "BOUNDARY" in t
    assert "escape hatch" in t, "the anti-relabelling clause is the rule's teeth"


def test_r4_is_discharged_and_the_level_collision_named():
    t = (ROOT / "docs" / "CROSSING_REQUIREMENTS.md").read_text(encoding="utf-8")
    assert "DISCHARGED 2026-08-10 (B1012)" in t
    term = (ROOT / "TERMINOLOGY.md").read_text(encoding="utf-8")
    assert '"level" now names TWO quantities' in term
    assert "category claim needing its own arc" in term


def test_the_unverified_branch_items_stay_owed():
    v = json.loads((ROOT / "frontier" / "B1013_wall_resort" / "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    assert "stay OWED" in c and "REFUSED stands" in c
