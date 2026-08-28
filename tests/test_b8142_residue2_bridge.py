"""Lock: the Sym-power factorisation, its scope, and the vacuous control that was caught."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8142_residue2_bridge/results.json").read_text())

def test_the_identity_is_stated_and_verified_with_live_controls():
    i = R["identity"]
    assert i["statement"] == "R_{rho(m)}(s) = prod_{j=-m}^{m} R(s-j, sigma_j)"
    assert "5e-18" in i["verified"] and "m=0,1,2,3,4" in i["verified"]

def test_no_novelty_is_claimed_for_the_identity():
    assert "NONE CLAIMED" in R["identity"]["novelty"]
    assert "novelty for the identity" in R["not_claimed"]

def test_the_graviton_factors_are_located_inside_frieds_point():
    w = R["what_it_does_at_frieds_point"]
    assert "EXACTLY the graviton's own factors" in w["the_graviton_is_inside"]
    assert "NOT CHECKED HERE" in w["conditional"]

def test_residue2_is_reduced_not_closed():
    s = R["residue2_status"]
    assert "NEGATIVE integers" in s["after_first_reduction"]
    assert "FUNCTIONAL EQUATION" in s["after_second_reduction"]
    assert "remains open" in s["NOT_CLOSED"]

def test_the_vacuous_control_is_recorded_and_kept_visible():
    v = R["my_own_vacuous_control"]
    assert "could NEVER fail" in v["why"]
    assert "SYMMETRY rather than a control" in v["kept_as_a_record"]
    assert len(v["replaced_by"]) == 3


def test_the_forced_reflection_formula_is_recorded_as_conditional():
    f = R["forced_reflection_formula"]
    assert f["statement"].startswith("|R(-m, sigma_m)|")
    assert "CONDITIONAL" in f["status"] and "NOT verified here" in f["status"]
    assert "falsifiable" in f

def test_the_reflection_values_decay_by_the_damping():
    v = R["forced_reflection_formula"]["computed_for_m004"]
    assert v["5"] < v["4"] < v["3"]
    assert all(x < 1e-3 for x in v.values())

def test_the_tuned_threshold_slip_is_recorded():
    t = R["my_own_tuned_threshold"]
    assert "TUNED TO THE TWO DATA POINTS" in t["why_wrong"]
    assert "c(2)/c(2) = 1" in t["also_fixed"]


def test_the_antecedent_refutation_is_recorded_and_reproduced():
    c = R["CORRECTION_2026-08-26_antecedent_refuted"]
    assert "REPRODUCED HERE FROM SCRATCH" in c["what_happened"]
    assert "(0,1,1)" in c["the_computation"]
    assert "INVALID" in c["what_this_kills"] and "WITHDRAWN" in c["what_this_kills"]

def test_the_identity_survives_the_refutation():
    c = R["CORRECTION_2026-08-26_antecedent_refuted"]
    assert "unconditional eigenvalue algebra" in c["what_survives_untouched"]

def test_the_open_route_is_named_and_not_claimed_done():
    c = R["CORRECTION_2026-08-26_antecedent_refuted"]
    assert "Park/Pfaff" in c["what_remains_open"]
    assert "has NOT been performed" in c["what_remains_open"]


def test_the_alexander_control_exists_in_code_not_only_in_prose():
    src = (ROOT / "frontier/B8142_residue2_bridge/acyclicity.py").read_text()
    assert "Alexander polynomial is x^2 - 3x + 1" in src
    assert src.count("check(") >= 9

def test_the_check_counter_cannot_go_stale():
    src = (ROOT / "frontier/B8142_residue2_bridge/acyclicity.py").read_text()
    assert "_TOTAL ==" in src and "check-count drifted" in src

def test_the_claimed_but_unrun_control_is_recorded():
    c = R["CORRECTION_2026-08-28_a_control_claimed_but_not_run"]
    assert "NO SUCH CHECK EXISTED" in c["what"]
    assert c["the_result"].startswith("THE CONTROL PASSES")


def test_the_failed_detector_is_recorded_and_its_output_withheld():
    f = R["CORRECTION_2026-08-28_a_control_claimed_but_not_run"]["attempted_generalisation_FAILED"]
    assert f["verdict"].startswith("UNRELIABLE")
    assert "NOT published as findings" in f["verdict"]
    assert "B8111" in f["why_it_missed"]

def test_the_class_is_recorded_as_having_no_detector():
    f = R["CORRECTION_2026-08-28_a_control_claimed_but_not_run"]["attempted_generalisation_FAILED"]
    assert "no detector" in f["what_this_means"] and "caught by accident" in f["what_this_means"]
