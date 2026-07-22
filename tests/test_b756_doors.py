"""Locks for B756 -- cc2's remaining-doors package, cc-verified."""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2


def _a(chi2):
    return (phi + phi**-2 * chi2) / 2


def test_door3_iff_law_and_exact_defect():
    for cm in (1, -1):
        for cn in (1, -1):
            defect = sp.simplify(_a(cm) * _a(cn) - _a(cm * cn))
            if cm == cn == -1:
                assert sp.simplify(defect - (1 - sp.sqrt(5)) / 2) == 0
            else:
                assert defect == 0


def test_door2_counterexample_monodromy_discs_not_golden():
    # Alexander charpolys recomputed in-arc (cc_verify_door2.py): traces -5, 4, 6
    t = sp.symbols("t")
    for tr, disc_expected in ((5, 21), (4, 12), (6, 32)):
        assert sp.discriminant(t**2 - tr * t + 1, t) == disc_expected != 5
    # golden needs trace 3
    assert sp.discriminant(t**2 - 3 * t + 1, t) == 5


def test_door2_five_inert_in_the_recomputed_fields():
    x = sp.symbols("x")
    for poly, deg in ((x**4 + 3 * x**2 - x + 1, 4),    # m022, disc 697
                      (x**2 - x + 2, 2),               # m009, Q(sqrt-7)
                      (x**3 - x**2 - x - 1, 3)):       # m039, disc -44
        fac = sp.factor_list(poly, modulus=5)
        degs = sorted(sp.Poly(f, x).degree() for f, m in fac[1] for _ in range(m))
        assert degs == [deg]                            # totally inert at 5
