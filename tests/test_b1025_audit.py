"""B1025 — locks: the verified joins and the revised floor."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1025_input_derivability"))


def test_the_joins_verify():
    from audit_checks import i5_singlet_multiplicities, i3_unit_untouched_by_sigma, \
        i1_arrow_is_downstream_of_closing
    i5 = i5_singlet_multiplicities()
    assert i5["both_unique_lines"], "the VEV directions must stay multiplicity-one lines"
    assert i3_unit_untouched_by_sigma()["l_still_free"], (
        "even sigma = 1 must leave the unit free -- I3's strengthening")
    assert i1_arrow_is_downstream_of_closing()["arrow_needs_closing"]


def test_the_verdicts_and_the_floor():
    v = json.loads((ROOT / "frontier" / "B1025_input_derivability" /
                    "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    for phrase in ("I1 THE ARROW BIT SURVIVES", "I2 THE CHIRALITY BIT SURVIVES",
                   "I3 THE UNIT l SURVIVES", "I4 THE 6D TYPE J NARROWS",
                   "I5 THE RANK-CLOSING VEV NARROWS"):
        assert phrase in c
    assert "ONE UNIT, TWO BITS, AND TWO ACCEPTANCES" in c, "the revised floor must stay stated"
    assert "RESCOPED not contradicted" in c, "B990's scope discipline must survive"
    assert "S1" in c, "the J-closer must stay named"
