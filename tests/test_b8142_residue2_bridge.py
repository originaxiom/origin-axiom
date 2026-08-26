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
