"""B943 locks — the retroactive O3 correction to B922's priority sentence."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B943_maass_priority_correction"
B922 = ROOT / "frontier" / "B922_lambda2_receipt"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_index_relation_is_reproduced_from_humbert_not_asserted():
    r = _res()
    assert r["index_is_12"] is True
    assert abs(float(r["index_ratio"]) - 12.0) < 1e-9


def test_the_parent_ground_state_check_reproduces_B791():
    """W_parent(7.072) must land on B791's own 1.010, computed from scratch."""
    r = _res()
    assert r["reproduces_B791_W_1_010"] is True
    assert abs(float(r["W_parent_at_parent_ground_state"]) - 1.010) < 0.01


def test_lambda2_is_below_the_parent_spectrum():
    """The fact that defeats the pullback caveat."""
    r = _res()
    assert r["parent_count_below_lambda2_is_under_one"] is True
    assert float(r["W_parent_at_lambda2"]) < 1.0
    assert r["lambda2_below_parent_ground_state"] is True


def test_the_precedent_number_was_refuted():
    r = _res()
    assert r["precedent_decimal_places"] == 13
    assert r["repo_asserted_precedent_was"] == 10
    assert r["precedent_claim_refuted"] is True
    assert r["b922_decimal_places"] == 25
    assert r["improvement_decimal_places"] == 12


def test_no_priority_word_survives_in_B922_AS_A_CLAIM():
    """The gate is retroactive: the old sentence must no longer be asserted.

    It may still appear as a MENTION inside the correction banner ("this arc
    originally read ...") -- that is the record of what was claimed, which the
    house rule keeps rather than edits away. The lock therefore tests use vs
    mention, not the raw string.
    """
    txt = (B922 / "FINDINGS.md").read_text(encoding="utf-8")
    title = txt.splitlines()[0]
    assert not re.search(r"first 25-digit", title, re.I), "the title must not claim it"
    for m in re.finditer(r"first 25-digit", txt, re.I):
        window = txt[max(0, m.start() - 200):m.start()]
        assert "originally read" in window, (
            "every surviving occurrence must be a quoted mention in the correction banner")
    verdict = (B922 / "arc_verdict.json").read_text(encoding="utf-8")
    assert not re.search(r"THE FIRST 25-DIGIT", verdict)
    assert "CLAIM CORRECTED" in verdict


def test_the_two_load_bearing_qualifiers_are_present():
    txt = (B922 / "FINDINGS.md").read_text(encoding="utf-8")
    assert "cusp form" in txt
    assert "not inherited" in txt or "NOT inherited" in txt


def test_the_arc_declines_the_orbifold_escape():
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "We decline that" in txt or "decline that escape" in txt
    assert "B525" in txt


def test_the_honest_limit_on_the_screen_is_recorded():
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "screened and consistent, not proven" in txt.lower()
    assert "6.4" in txt


def test_the_gate_is_still_half_met():
    txt = (CELL / "FINDINGS.md").read_text(encoding="utf-8")
    assert "MathSciNet" in txt
    assert "half met" in txt
