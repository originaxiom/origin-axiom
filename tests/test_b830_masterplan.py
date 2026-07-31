"""B830 — locks the fork deletion, the false-positive correction, and the revival-score fix."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_the_reviews_fork_is_gone():
    assert not (ROOT / "docs" / "REVIEWS.md").exists()
    assert (ROOT / "docs" / "progress" / "REVIEWS.md").is_file()


def test_the_two_roadmaps_are_DIFFERENT_documents_not_copies():
    """Review 35 called docs/ROADMAP.md a stale fork. It is not; they share zero headings."""
    def heads(p):
        return {l.strip() for l in (ROOT / p).read_text(encoding="utf-8").splitlines()
                if re.match(r"^#{1,3} ", l)}
    a, b = heads("ROADMAP.md"), heads("docs/ROADMAP.md")
    assert a and b
    assert not (a & b), f"the two roadmaps now share headings: {a & b}"


def test_both_roadmaps_cross_reference_each_other():
    root = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    docs = (ROOT / "docs" / "ROADMAP.md").read_text(encoding="utf-8")
    assert "tier map" in root.lower() and "docs/ROADMAP.md" in root
    assert "phase ladder" in docs.lower() and "ROADMAP.md" in docs
    assert "NOT the operative roadmap" not in docs, "the false banner must stay removed"


def test_b731_revival_score_no_longer_contradicts_its_own_note():
    d = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler"
                    / "kill_graph.json").read_text(encoding="utf-8"))
    row = next(r for r in d if r.get("id") == "B731")
    assert row["revival_score"] == 0
    assert "ALREADY RETRACTED by B734" in row["note"]


def test_no_row_tops_the_revival_ranking_while_declaring_itself_retracted():
    """The general defect: a machine-readable field contradicting the note in the same record."""
    d = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler"
                    / "kill_graph.json").read_text(encoding="utf-8"))
    scored = [r for r in d if isinstance(r.get("revival_score"), (int, float))]
    top = max(r["revival_score"] for r in scored)
    leaders = [r for r in scored if r["revival_score"] == top]
    for r in leaders:
        assert not re.search(r"ALREADY RETRACTED", r.get("note", "") or "", re.I), (
            f"{r.get('id')} tops the revival ranking while declaring itself retracted")
