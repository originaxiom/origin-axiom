"""B1606 -- THREE ON THE WEAVE, GRADED: the puncture conditions the weave keeps, as recorded; W21's verification on
B1600's addendum, as recorded; GENESIS v1.28 carries the grade."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
HERE = ROOT / "frontier" / "B1606_three_on_the_weave_graded" / "verification"
B1600 = ROOT / "frontier" / "B1600_the_weave_verified" / "verification"


def test_the_puncture_conditions_as_recorded():
    d = json.load(open(HERE / "puncture_condition.json"))
    assert d["D1_chi_p_rho_is_u_p_rho_u_p_inverse"]
    m = d["moves"]
    assert m["order"] == 48 and m["commutant"] == 2 and m["isotypic_dimensions"] == [2, 4]
    assert m["kept_dimensions"] == [0, 2, 4, 6] and m["kept_indices"] == [-3, -1, 1, 3]
    assert m["minus_one_in_group_acts_as_minus_one"] and m["all_kept_indices_odd"]
    g = d["moves_and_grading"]
    assert g["commutant"] == 1 and g["kept_dimensions"] == [0, 6] and g["kept_indices"] == [-3, 3]


def test_w21_and_w20_as_recorded_on_b1600():
    w21 = json.load(open(B1600 / "w21_check.json"))
    assert w21["annihilates_coboundaries"] and w21["hermitian"] and w21["signature"] == [3, 3]
    assert w21["invariance"]["L"]["invariant"] and w21["invariance"]["R"]["invariant"] and w21["invariance"]["sign"]["invariant"] and w21["invariance"]["swap"]["reversed"]
    assert w21["T_positive_T_bar_negative"] and abs(w21["holomorphic_triplet_chi_L_turns"] - 0.875) < 1e-6
    w20 = json.load(open(B1600 / "w20_w22_check.json"))
    assert w20["minus_chi"]["E6 (principal)"] == 3 and w20["minus_chi"]["E6(a1)"] == 3 and w20["minus_chi"]["E6(a3)"] == 3 and w20["minus_chi"]["78 through the principal sl2"] == 16
    assert w20["fibre_terms_zero"] and w20["W22"]["irreducible_on_C2"]


def test_genesis_carries_the_grade():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 28 and "THREE ON THE WEAVE, GRADED (main, B1606" in g   # the version only moves forward; never pin the header
    assert "the flavour three is derived, the gauge three is a selection" in g
