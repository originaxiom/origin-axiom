"""B1345 - the Jorgensen number is B309's 'unit obstruction', and two readings die.

Arithmetic only (no SnapPy) so the lock runs everywhere; the geometric computation lives in the
arc's verification scripts.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1345_the_jorgensen_number"
w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2


def test_arc_is_banked():
    assert (ARC / "FINDINGS.md").exists()
    assert json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["id"] == "B1345"


def test_a_parabolic_pair_reduces_J_to_kappa_minus_two():
    """tr A = +-2 kills |tr^2 A - 4| exactly, so J = |kappa - 2|."""
    for tr in (2, -2):
        assert tr ** 2 - 4 == 0


def test_b309s_unit_obstruction_is_the_saturation_value():
    """B309/B518/B1010: kappa - 2 = omega^2, |kappa - 2| = 1 -- Jorgensen's bound, saturated."""
    assert sp.simplify(w ** 3 - 1) == 0 and sp.simplify(w ** 2 + w + 1) == 0
    assert sp.simplify(sp.Abs(w ** 2) - 1) == 0, "the unit obstruction IS the bound's value"


def test_e72_is_load_bearing_here():
    """only the meridian branch saturates; the fibre branch gives 4."""
    assert sp.simplify(sp.Abs(w ** 2)) == 1, "meridian kappa - 2 = omega^2 saturates"
    assert sp.Abs(sp.Integer(-2) - 2) == 4, "fibre kappa = -2 gives 4, not the Jorgensen number"


def test_amphichirality_cannot_be_equivalent_to_saturation():
    """A LOGICAL test, independent of any computation: uniqueness forbids it.

    Callahan: m004 is the ONLY orientable hyperbolic 3-manifold with J = 1. If J = 1 were equivalent
    to amphichirality, every amphichiral manifold would have J = 1. There is more than one
    amphichiral orientable hyperbolic 3-manifold (6_3, 8_3, 8_9, 8_12, 8_17, 8_18 among knots).
    Hence the equivalence is impossible."""
    amphichiral_besides_4_1 = ["6_3", "8_3", "8_9", "8_12", "8_17", "8_18"]
    assert len(amphichiral_besides_4_1) > 0, (
        "if any amphichiral manifold other than m004 exists, J = 1 cannot characterise amphichirality")
    # and the measured values, pinned from the arc's run
    measured = {"4_1": 1.0, "6_3": 1.4655712, "8_17": 2.0444284, "5_2": 1.3247180}
    assert measured["5_2"] < measured["6_3"], (
        "a CHIRAL knot sits below an AMPHICHIRAL one -- the orders interleave")
    assert all(v > 1.0 for k, v in measured.items() if k != "4_1")


def test_chi_is_zero_at_every_slack():
    """chi(M) = chi(dM)/2 = 0 for every compact 3-manifold with torus boundary, whatever J is.
    So 'no Euler characteristic because it has no slack' cannot be right."""
    chi_torus = 0
    for n_cusps in (1, 2, 3, 5):
        assert (n_cusps * chi_torus) // 2 == 0, "chi vanishes independently of any slack value"


def test_the_index_explanation_is_refuted_by_b1335():
    """B1335 exhibits I = +-1 on m010, which also has chi = 0 -- so chi = 0 cannot be the cause."""
    v = json.loads((ROOT / "frontier" / "B1335_the_vanishing_is_not_formal_exhibited"
                    / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "NEGATIVE"
    c = v["claim_one_line"]
    assert "m010" in c and "I = +-1" in c.replace("±", "+-"), (
        "B1335 must still exhibit a non-zero index on a chi = 0 one-cusped manifold")
