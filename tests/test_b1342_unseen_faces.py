"""B1342 - three of the four strata are unseen, and kappa is why.

These recompute the load-bearing facts rather than reading them from B497's table, so the test fails
if the mathematics is ever wrong: only stratum 1 preserves kappa, every stratum divides (kappa-2),
and kappa=2 is a fixed point of the whole monoid.
"""
import pathlib
import json

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1342_the_unseen_faces"

x, y, z = sp.symbols("x y z")
KAP = lambda X, Y, Z: X ** 2 + Y ** 2 + Z ** 2 - X * Y * Z - 2

# B497's four strata as TRACE maps (each verified against its word in the arc's verification script)
TM = {"1_golden":        (z, x, x * z - y),
      "2_squaring":      (x ** 2 - 2, y ** 2 - 2, x * y * z - x ** 2 - y ** 2 + 2),
      "2p_perioddouble": (z, x ** 2 - 2, (x ** 2 - 1) * z - x * y),
      "3_thuemorse":     (z, z, x * y * z - x ** 2 - y ** 2 + 2)}


def test_arc_is_banked():
    assert (ARC / "FINDINGS.md").exists()
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1342" and v["verdict"] == "PROVED"


def test_only_stratum_1_preserves_kappa():
    """the derived reason the programme is confined: kappa is its one first integral, and kappa is
    conserved in stratum 1 alone."""
    k = KAP(x, y, z)
    assert sp.simplify(KAP(*TM["1_golden"]) - k) == 0, "stratum 1 must preserve kappa"
    for name in ("2_squaring", "2p_perioddouble", "3_thuemorse"):
        assert sp.simplify(KAP(*TM[name]) - k) != 0, f"{name} must MOVE the leaf, or nothing is at stake"


def test_u1_every_stratum_divides_kappa_minus_two():
    """B497's U1, re-derived: (kappa-2) | (kappa'-2) everywhere, so kappa=2 is absolutely invariant."""
    div = sp.Poly(KAP(x, y, z) - 2, x, y, z)
    mult = {}
    for name, tm in TM.items():
        q, r = sp.div(sp.Poly(sp.expand(KAP(*tm)) - 2, x, y, z), div)
        assert r.as_expr() == 0, f"{name}: (kappa-2) must divide (kappa'-2) exactly"
        mult[name] = sp.factor(q.as_expr())
    assert mult["1_golden"] == 1, "stratum 1's multiplier is 1 -- kappa is conserved"
    assert sp.simplify(mult["2_squaring"] - x ** 2 * y ** 2) == 0
    assert sp.simplify(mult["2p_perioddouble"] - x ** 2) == 0, (
        "the stratum-2' multiplier x^2, computed by B1342 where B497 left it open")
    assert sp.simplify(mult["3_thuemorse"] - (x ** 2 + y ** 2 - x * y * z)) == 0


def test_stratum_4_lands_on_nothing():
    """a->ab, b->ab sends both generators to the same word, so kappa' == 2 identically."""
    k4 = KAP(z, z, z ** 2 - 2)          # tr A' = tr B' = z, tr(A'B') = tr((AB)^2) = z^2 - 2
    assert sp.simplify(sp.expand(k4) - 2) == 0, "stratum 4's image must be the kappa = 2 floor"


def test_the_action_occupies_half_of_one_stratum():
    """B1341's obstruction, extended: variational needs an invariant leaf AND det +1."""
    L, P, R = (sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[1, 0], [1, 1]]))
    half, mono = L * P, (L * P) ** 2
    assert half.det() == -1 and mono.det() == 1, "the half step reverses orientation; its square does not"
    # and outside stratum 1 there is no invariant leaf at all
    assert sp.simplify(KAP(*TM["3_thuemorse"]) - KAP(x, y, z)) != 0


def test_the_confinement_is_stated_with_its_scope():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "stratum 1 of 4" in t, "B497's own sentence must be quoted"
    assert "not a hidden face of the" in t.lower(), "the scope fence must stay explicit"
