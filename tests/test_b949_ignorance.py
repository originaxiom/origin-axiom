"""B949 locks — the ignorance map.

The load-bearing lock is the LAST one: source_free must stay recorded as a DEAD
direction rather than a gap, so no future sweep re-reports a closed door as an
opportunity.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B949_ignorance_map"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_obstacle_table_covers_every_type():
    r = _res()
    assert r["corpus_size"] >= 860
    assert len(r["obstacle_table"]) == 11, "all eleven obstacle types, not the built-in six"
    for ob, row in r["obstacle_table"].items():
        assert row["total"] == row["banked"] + row["dead"] + row["open"] + row["dormant"]


def test_bridge_construction_is_the_objective_frontier():
    """Most-attempted-least-resolved among types with a real sample."""
    r = _res()
    t = r["obstacle_table"]["bridge_construction"]
    assert t["banked"] == 5 and t["dead"] == 8 and t["total"] == 14
    assert r["objective_frontier"] == "bridge_construction"
    # every other multi-probe type resolves better
    for ob, row in r["obstacle_table"].items():
        if ob in ("bridge_construction", "source_free"):
            continue
        assert row["resolved_pct"] > t["resolved_pct"]


def test_no_structural_motif_gap():
    r = _res()
    assert r["no_structural_motif_gap"] is True
    assert r["strongest_motif_avoidance"]["ratio"] > 0.7


def test_source_free_is_a_DEAD_DIRECTION_not_a_gap():
    """The correction this arc makes to its own first reading. If a later sweep
    re-reports source_free as an opportunity, it is double-counting a closed door."""
    r = _res()
    assert r["source_free_is_a_recorded_dead_direction"] is True
    assert r["source_free_probe"]["status"] == "dead"
    assert r["source_free_probe"]["is_keyword_match_not_a_real_attack"] is True
    # hard-wrapped markdown: normalise whitespace before matching prose
    u = " ".join((ROOT / "docs" / "UNIQUENESS_THEOREM.md").read_text(encoding="utf-8").split())
    assert "**not** a derivation of the substrate from nothing" in u
    assert "that direction is mapped dead" in u


def test_the_real_ignorance_is_the_axioms_and_A7_is_only_registered():
    txt = " ".join((CELL / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "WHY *these* axioms" in txt or "Why *these* axioms" in txt
    assert "Registered as L131, NOT claimed" in txt
    assert "The discriminating computation has not been run" in txt
