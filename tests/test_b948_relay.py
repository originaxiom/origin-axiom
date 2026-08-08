"""B948 locks — the retraction must have reached every surface that carried it."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B948_relay_ssb_sweep"


def _norm(p):
    return " ".join(p.read_text(encoding="utf-8").split())


def test_the_rooms_stay_clean_of_the_dead_clause():
    """The clause never leaked into the rooms; it must not start now."""
    bad = ("beta=1 SSB", "β=1 SSB", "cooling through β=1", "cooling through beta=1")
    for room in ("knowledge", "philosophy", "speculations", "story"):
        d = ROOT / room
        if not d.is_dir():
            continue
        for f in d.rglob("*.md"):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            for frag in bad:
                assert frag not in txt, f"dead clause leaked into {f.relative_to(ROOT)}"


def test_the_law_map_row_is_superseded_and_points_at_B942():
    txt = _norm(ROOT / "docs" / "LAW_MAP.md")
    assert "SUPERSEDED 2026-08-08 — READ B942 FIRST" in txt
    assert "THE OBSERVER'S MECHANISM IS THEREFORE OPEN, NOT SETTLED" in txt
    assert "UNEARNED** (L124)" in txt


def test_the_theorem_inside_the_dead_neighbourhood_is_KEPT_and_distinguished():
    """B736-P2's obstruction is a verified fact and must not be deleted with the claim."""
    txt = _norm(ROOT / "docs" / "handoffs" / "PHYSICS_PATHFINDER_PROMPT_2026-07-21.md")
    assert "NOTE ADDED 2026-08-08 (B948)" in txt
    assert "independently re-verified" in txt
    assert "The observer's mechanism is **open**" in txt
    # and the obstruction line itself is still present
    assert "pole of" in txt


def test_the_presence_side_is_recorded_as_still_owed():
    txt = _norm(CELL / "FINDINGS.md")
    assert "Not discharged by this\narc either." in (CELL / "FINDINGS.md").read_text() or \
        "Not discharged by this arc either." in txt
    assert "Still owed, both sides" in txt
