"""B944 locks — the dynamics & chirality sweep, and the scoping negative.

The load-bearing lock is the LAST one: the matrix level must be shown NOT to
decide the one-Z/2 question, so no future seat can quietly promote the
identification without doing it at the right level.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B944_dynamics_chirality_sweep"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_both_corpora_are_large_and_mostly_positive():
    t = _res()["tally"]
    assert t["chirality"]["total"] >= 100 and t["chirality"]["PROVED"] >= 65
    assert t["dynamics"]["total"] >= 25 and t["dynamics"]["PROVED"] >= 18
    # the point of the sweep: these are not empty gaps
    assert t["chirality"]["PROVED"] > t["chirality"]["NEGATIVE"]
    assert t["dynamics"]["PROVED"] > t["dynamics"]["NEGATIVE"]


def test_the_named_positives_are_present_in_the_census():
    ids = {r["id"] for r in _res()["chirality_arcs"]} | {r["id"] for r in _res()["dynamics_arcs"]}
    for a in ("B582", "B576", "B340", "B303", "B196", "B416", "B417", "B317"):
        assert a in ids, f"{a} must appear in the swept census"


def test_the_mirror_is_not_the_inverse():
    s = _res()["scoping"]
    assert s["mirror_equals_inverse"] is False
    assert s["phi"] == [[2, 1], [1, 1]] and s["trace"] == 3


def test_the_matrix_level_does_NOT_decide_the_one_Z2_question():
    """The scoping negative. Both involutions admit conjugators of both
    determinants, so orientation cannot separate them here -- the question
    belongs at the mapping-class level."""
    s = _res()["scoping"]
    t, m = s["conjugators_to_phi_inverse_TIME"], s["conjugators_to_mirror_CHIRALITY"]
    assert t["+1"] > 0 and t["-1"] > 0
    assert m["+1"] > 0 and m["-1"] > 0
    assert s["both_involutions_have_conjugators_of_BOTH_determinants"] is True
    assert s["matrix_level_decides"] is False


def test_the_identification_is_registered_not_claimed():
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "Registered, not claimed" in txt
    assert "L126" in txt
    # and the children door is recorded as closed
    assert "B443" in txt and "B718" in txt and "closed door" in txt.lower()
