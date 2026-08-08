"""B956 locks — L133 reframed as an intermediate-closure problem."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B956_l133_analysis"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def _n(p):
    """Normalise markdown prose for substring matching.

    Third time this bit: markdown is hard-wrapped AND carries inline markers
    (blockquote '>' and emphasis '*') that land mid-sentence once whitespace is
    collapsed. Strip the markers, then collapse.
    """
    import re
    txt = p.read_text(encoding="utf-8")
    txt = re.sub(r"(?m)^\s*>\s?", "", txt)   # blockquote markers
    txt = txt.replace("*", "")                 # emphasis markers
    return " ".join(txt.split())


def test_the_target_is_strictly_between_two_computed_regimes():
    r = _res()
    assert r["regimes_the_object_has"]["abelian_torus_data"]["rank"] == 6
    assert r["regimes_the_object_has"]["zariski_dense"]["rank"] == 0
    assert r["target"]["rank"] == 4
    assert r["target_is_strictly_between"] is True


def test_the_chirality_construction_provably_overshoots():
    r = _res()
    assert "contains BOTH glued SL(2) images" in r["why_B582_overshoots"]
    b582 = _n(ROOT / "frontier" / "B582_chiral_play" / "FINDINGS.md")
    assert "Zariski closure equal to FULL E₆(ℂ)" in b582


def test_the_recurrence_is_flagged_as_possibly_a_theorem():
    t = _n(CELL / "FINDINGS.md")
    assert "is this a coincidence of two constructions, or is there a theorem behind it?" in t.lower()
    assert "l133 is a no-go rather than a lead" in t.lower()


def test_the_candidate_mechanism_carries_its_risk_on_the_record():
    """The Wilson-line proposal may inherit the very obstruction it was to solve."""
    r = _res()
    assert "rank-PRESERVING" in r["wilson_line_caution"]
    assert "PENDING the panel" in r["wilson_line_caution"]
    t = _n(CELL / "FINDINGS.md")
    assert "is NOT settled here" in t


def test_the_lead_is_recorded_as_virgin_ground():
    r = _res()
    assert r["repo_status"]["wilson_line_hosotani_worked_before_today"] is False
    assert r["repo_status"]["arcs_mentioning_VEV"] == 11
