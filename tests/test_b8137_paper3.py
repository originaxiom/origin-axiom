"""Lock: Paper III's banked claims match the paper and its verification."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8137_paper3_drafted/results.json").read_text())

def test_the_identity_and_its_negative_answer():
    i = R["identity"]
    assert "GMY nome, EXACTLY" in i["statement"]
    assert "INFINITE PRODUCT" in i["consequence"]
    assert "NONE OF THEM" in i["answers"]
    assert "k>=3 tail" in i["pfaff_reaches"] and "abscissa" in i["pfaff_reaches"]

def test_n2_reports_no_breakdown_but_does_not_claim_convergence():
    n = R["n2_at_the_abscissa"]
    assert "21.8x" in n["bite_control"] and "ABORTS" in n["bite_control"]
    assert "CONVERGENCE IS NOT PROVED" in n["NOT_established"]

def test_three_residues_each_carry_a_closer():
    r = R["three_residues"]
    assert len(r) == 3
    assert all("CLOSED BY:" in v for v in r.values())
    assert "EXISTENCE gap as an EVALUATION gap" in r["2_evaluation_point"]

def test_the_L_chi_result_is_stated_negatively_and_scoped():
    s = R["L_chi_negative"]["statement"]
    assert "PURELY GEODESIC" in s and "does NOT factor through" in s
    assert "DOES enter the functional equation" in s

def test_corroboration_is_recorded_because_absence_is_weak():
    c = R["independent_corroboration"]
    assert c["OA-C1062"].startswith("EXTERNAL_BLOCKER")
    assert "ASSERTION OF ABSENCE" in c["why_recorded"]

def test_the_missing_reproducer_is_recorded_not_silently_supplied():
    g = R["gap_found_and_filled"]
    assert "NO reproducer in the tree" in g["what"]
    assert "~3%" in g["residual"]
