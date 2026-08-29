"""B1217 — the seat integration. Locks what was verified, and what was only cited."""
import json
from itertools import combinations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1217_seat_integration"


def _res():
    return json.loads((ARC / "b1217_results.json").read_text(encoding="utf-8"))


def test_the_determinant_characters_cancel():
    """R026's equivariance, re-derived: codex reports B:6 W:11 G:7 without flagging that they must
    sum to zero mod 12. They do, and nearby ledgers do not."""
    W = (0, 2, 6, 8, 9, 10)
    assert sum(W) % 12 == 11
    assert (6 + 11 + 7) % 12 == 0
    for bad in ((6, 11, 8), (5, 11, 7), (6, 10, 7)):
        assert sum(bad) % 12 != 0, "the check must be able to fail"


def test_the_wedge_sign_and_the_384_count():
    lhs, tgt = ["sb", "sc", "k1", "sd", "k2", "sa"], ["sa", "sb", "sc", "sd", "k1", "k2"]
    perm = [tgt.index(x) for x in lhs]
    inv = sum(1 for i, j in combinations(range(6), 2) if perm[i] > perm[j])
    assert (-1) ** inv == 1, "R026's connecting-product sign"
    assert 8 * 8 * comb(4, 2) == 384, "R027's Eilenberg-Zilber bound; the 6 is the (2,2)-shuffles"


def test_clouds_gating_control_matches_our_banked_B1137():
    """The half of V-NEG this bench can actually check, and it checks out exactly."""
    d = json.loads((ROOT / "frontier" / "B1137_regulator_probe" / "results" /
                    "final_report.json").read_text(encoding="utf-8"))
    rows = d["per_target"]
    assert sum(r["raw_found"] for r in rows) == 117
    assert sum(r["involves_V"] for r in rows) == 117
    assert sum(r["involves_regulator"] for r in rows) == 0, "the decisive column"
    vub = [r for r in rows if "ub" in r["target"].lower()][0]
    assert vub["raw_found"] == 9 and vub["involves_regulator"] == 0, (
        "their 117->108 explanation stands or falls on this row")


def test_the_extended_run_is_typed_as_cited_not_reproduced():
    """The honesty that matters in a harvest: a headline whose certificate is absent must be
    labelled CITED, however well-supported its checkable parts are."""
    g = _res()["evidence_contract_gap"]
    assert "not reproducible as committed" in g["what"]
    assert g["typed"].startswith("CITED")
    assert "artifact, not the argument" in g["what_this_does_not_undermine"]
    tbl = _res()["verified_here"]["cloud_VNEG"]["their_reported_table"]
    assert tbl["control_25_entries"]["involves_regulator"] == 0
    assert tbl["extended_28_entries"]["involves_regulator"] == 0


def test_delta_G_is_one_of_three_and_the_fork_is_still_open():
    """The single most over-readable thing in this harvest."""
    r = _res()["verified_here"]["codex_R026"]
    assert "component 1 of 3" in r["status"]
    assert "OPEN" in r["fork_status"]
    assert "LEAD" in _res()["verified_here"]["codex_R027_lead"]["status"]
