"""B1344 - the kappa collision, and the object's real geometric point.

These recompute rather than assert. The object's fibre point is the character fixed by the
monodromy T1^2 on the parabolic leaf; the record's OTHER kappa belongs to the knot group's meridian
pair. One symbol, two numbers (ERROR_LEDGER E72).
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1344_chat1_strata_verification"
w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
S = lambda e: sp.simplify(sp.expand(e))
kap = lambda p: S(p[0] ** 2 + p[1] ** 2 + p[2] ** 2 - p[0] * p[1] * p[2] - 2)
T1 = lambda p: (p[2], p[0], S(p[0] * p[2] - p[1]))

GEO = (S(2 + w), S(1 - w), S(1 - w))                      # the fibre geometric point
MER = (sp.Integer(2), sp.Integer(2), S(2 + w))            # the knot group's meridian point
CHAT1 = (S(w - 1), S(-2 * w), sp.Integer(-2))


def test_arc_and_error_class_are_banked():
    assert (ARC / "FINDINGS.md").exists()
    assert json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["id"] == "B1344"
    assert "E72" in (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")


def test_the_fibre_point_is_the_monodromy_fixed_point_on_kappa_minus_two():
    assert kap(GEO) == -2, "the object's fibre commutator is parabolic (B1248)"
    T2 = T1(T1(GEO))
    assert all(S(a - b) == 0 for a, b in zip(T2, GEO)), "fixed by the monodromy T1^2 (B448)"
    assert S(GEO[0] ** 2 - 3 * GEO[0] + 3) == 0, "B448 Part C's banked period-2 field Q(sqrt-3)"


def test_the_two_kappas_are_different_numbers():
    """E72: one symbol, two quantities."""
    assert kap(GEO) == -2 and S(kap(GEO) - 2) == -4
    assert S(kap(MER) - 2 - w ** 2) == 0, "the meridian kappa-2 is omega^2 (B309/B518)"
    assert S(sp.Abs(kap(MER) - 2) - 1) == 0, "and it is a UNIT, |kappa-2| = 1"
    assert S(kap(GEO) - kap(MER)) != 0, "they must not be equal, or there is no collision"


def test_chat1s_point_is_not_the_geometric_point():
    assert S(kap(CHAT1) - kap(GEO)) != 0, "wrong leaf"
    assert not all(S(a - b) == 0 for a, b in zip(T1(T1(CHAT1)), CHAT1)), "not monodromy-fixed"
    assert not all(S(a - b) == 0 for a, b in zip(T1(CHAT1), CHAT1)), "not half-step-fixed"


def test_the_z3_table_does_not_survive_at_the_object():
    """the stratum-3 multiplier equals omega at chat1's point ONLY."""
    m3 = lambda p: S(p[0] ** 2 + p[1] ** 2 - p[0] * p[1] * p[2])
    assert S(m3(CHAT1) - w) == 0, "true at chat1's point"
    assert S(m3(GEO) - w) != 0, "false at the fibre point"
    assert S(m3(MER) - w) != 0, "false at the meridian point"
    assert S(m3(GEO) - 3 * w) == 0, "at the fibre point it is 3*omega"


def test_pending_item_9_values_at_the_object():
    """the multipliers at the fibre point: 1, 9, -3w^2, 3w, 0 -- exact in Z[omega]."""
    x, y, z = GEO
    assert S(x ** 2 * y ** 2 - 9) == 0, "renormalize"
    assert S(x ** 2 + 3 * w ** 2) == 0, "period-doubling multiplier is -3*omega^2"
    assert S((x ** 2 + y ** 2 - x * y * z) - 3 * w) == 0, "decoherence multiplier is 3*omega"
