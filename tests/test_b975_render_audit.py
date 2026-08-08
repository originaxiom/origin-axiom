"""B975 locks — the render audit: B940 cleared on stated grounds, C3 verified here."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B975_cc3_render_audit"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_B940_is_cleared_with_a_reason_not_a_hope():
    c = _res()["C2_global_phase_contamination"]["B940_CHECKED_HERE"]
    assert c["verdict"] == "SAFE"
    assert "phase-INVARIANT" in c["reason"]
    assert "relative residual" in c["reason"]
    assert "prospective_warning_stands" in c


def test_the_prospective_phase_warning_is_banked():
    c = _res()["C2_global_phase_contamination"]["B940_CHECKED_HERE"]
    assert "MUST be pinned" in c["prospective_warning_stands"]
    assert "B804" in c["prospective_warning_stands"]


def test_C3_was_verified_here_not_accepted():
    r = _res()["C3_tolerance_error"]
    assert set(r["VERIFIED_HERE"]) == {"97", "91", "84"}
    assert r["the_finding_stands"] is True


def test_C1_is_bounded_by_a_control_not_by_assertion():
    r = _res()["C1_docstring_overclaim"]
    assert "BIT-IDENTICAL" in r["cc3_bounding_evidence"]
    assert r["banked_results_affected"] == []


def test_the_render_practice_is_adopted_and_its_limit_stated():
    r = _res()["THE_PROCESS_POINT"]
    assert r["cc_decision"] == "ADOPTED as a practices row"
    assert "not gateable" in r["honest_limit"].lower()
    prac = (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")
    assert "Render before banking" in prac
    assert "NOT GATED" in prac


def test_the_plate_decisions_are_recorded():
    r = _res()["C4_plate_scope"]
    assert r["cc_decision_accept_rename_to_PLATE_J_THE_NULL"] is True
    assert r["cc_decision_GO_on_PLATE_I_THE_WALL"] is True
