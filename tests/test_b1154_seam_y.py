"""B1154 lock -- SEAM-Y resolved MISMATCH: codex's up-Yukawa=0 (cohomological emptiness) and our
period-value disjointness (arithmetic non-overlap) are two INDEPENDENT walls, both confirming the one
thesis (structure, not values). Asserts on COMMITTED files only (no gitignored artifacts -- cc3 B8141
the artifact class). Gate 5 untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1154_seam_y"


def _d():
    return json.loads((ARC / "b1154_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1154" and d["verdict"] == "PROVED"


def test_seam_y_is_mismatch_two_walls_one_thesis():
    d = _d()
    assert "MISMATCH" in d["verdict_outcome"] and "TWO-ROUTES-ONE-VERDICT" in d["verdict_outcome"]
    assert "structure" in d["verdict_outcome"].lower() and "values" in d["verdict_outcome"].lower()


def test_the_two_walls_are_different_kinds():
    d = _d()
    assert "EMPTINESS" in d["codex_wall"]["type"] and "COHOMOLOGICAL" in d["codex_wall"]["mechanism"]
    assert "NON-OVERLAP" in d["our_wall"]["type"] and "ARITHMETIC" in d["our_wall"]["mechanism"]
    assert "Emptiness != non-overlap" in d["discriminating_fact"]
    assert "NO SM number" in d["codex_wall"]["type"] and "REQUIRES the SM target list" in d["our_wall"]["type"]


def test_provenance_debt_flagged_not_leaned_on():
    d = _d()
    assert "OFF-BRANCH" in d["provenance_debt"] and "unversioned" in d["provenance_debt"].lower()
    assert "does NOT lean" in d["provenance_debt"]
    # the discriminating-fact evidence is a COMMITTED .txt (not the gitignored reproduce.log pattern)
    ev = (ARC / "verification" / "discriminating_fact.txt").read_text(encoding="utf-8")
    assert "MISMATCH" in ev and "Emptiness != non-overlap" in ev


def test_gate5_untouched_and_no_match_third_opinion_needed():
    d = _d()
    assert "Gate 5 untouched" in d["fences"] and "MISMATCH" in d["fences"]
