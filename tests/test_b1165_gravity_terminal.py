"""B1165 lock -- the TERMINAL gravity probe (sec-E), owner-directed to a typed close. Seal
GENERIC-RHYME (NEGATIVE): the observer's archimedean closing is CO-LOCATED with the object's
gravitational sector at the infinity-place, NOT object-specifically identical -- gravity is the WHERE,
generic in dynamics, with a single static arithmetic contact (Vol=L-value). Asserts on COMMITTED files
only; the archimedean anchors via the committed reproduce runner. Gate 5 clean (no SM value)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1165_gravity_terminal"


def _d():
    return json.loads((ARC / "b1165_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_negative():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1165" and d["verdict"] == "NEGATIVE"
    assert d["instrument"] is False and d["creates_law"] is False
    # the seal is named in the one-liner
    assert "GENERIC-RHYME" in d["claim_one_line"]
    assert "REFUTED" in d["claim_one_line"]


def test_seal_generic_rhyme_co_located_not_identified():
    d = _d()
    assert d["verdict"] == "NEGATIVE" and d["seal"] == "GENERIC-RHYME"
    assert "CO-LOCATED" in d["one_line"] and "NOT object-specifically identical" in d["one_line"]
    iv = d["identification_verdict_GENERIC_RHYME"]
    # the dynamics is generic; survives the non-arithmetic-knot swap
    assert "GENERIC-RHYME" in iv["dynamics_b_to_e"]
    assert "m015=5_2" in iv["dynamics_b_to_e"]
    # the closing is supplied, not identified
    assert "SUPPLIED-not-identified" in iv["closing_is"]


def test_arithmetic_contact_is_one_static_spot_three_tier_bounded():
    iv = _d()["identification_verdict_GENERIC_RHYME"]
    assert "STATIC scalar" in iv["arithmetic_contact_one_spot"]
    # tier (i) generic-in-form (Borel), tier (ii) object-specific content (Reid), tier (iii) re-labeling
    assert "Borel regulator" in iv["tier_i_generic_in_form"]
    assert "UNIQUE arithmetic knot" in iv["tier_ii_object_specific_content"] and "Reid" in iv["tier_ii_object_specific_content"]
    assert "no dynamics" in iv["tier_iii_relabeling"]


def test_vol_three_ways_and_orientation_own_verified():
    v = _d()["own_verified_50dps"]
    assert v["Vol_2ImLi2"].startswith("2.0298832128193072500424051085490405718833786150606")
    assert "1e-45" in v["Vol_3sqrt3_over2_L"] and "1e-45" in v["Vol_9sqrt3_zetaK2_over_pi2"]
    # the orientation is a bare Z/2: -Vol via Bloch-Wigner oddness
    assert v["minus_Vol_check"].startswith("2 Im Li2(e^{-i pi/3}) = -2.0298832128193072500424051085490405718833786150606")
    assert "ODD" in v["minus_Vol_check"]
    # the ablation control is the non-arithmetic 5_2
    assert "m015=5_2" in v["ablation_control"] and "NON-arithmetic" in v["ablation_control"]


def test_scale_wall_confirmed():
    d = _d()
    assert d["scale_wall"].startswith("CONFIRMED")
    assert "dimensionless" in d["scale_wall"]
    assert "B660/B666" in d["scale_wall"]


def test_definitional_fork_is_terminal_boundary():
    fork = _d()["definitional_fork_terminal"]
    assert "Mostow" in fork
    assert "un-oriented geometry" in fork
    assert "structure/observer boundary" in fork


def test_ablation_prediction_is_the_overturn_check():
    d = _d()
    assert "5_2" in d["ablation_prediction_ME2"]
    assert "OVERTURN" in d["ablation_prediction_ME2"] and "toward MATCH" in d["ablation_prediction_ME2"]


def test_verification_note_isometry_signature_flagged_for_review():
    # verify-don't-trust catch on our own B1163 addendum, carried forward honestly
    n = _d()["verification_note_for_review"]
    assert "isometry_signature" in n and "vacuous" in n
    assert "check_family.py" in n


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
