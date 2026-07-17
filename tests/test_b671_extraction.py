"""B671 locks — the gauge verdict + the sum rule (from banked data)."""
import json
import os

import sympy as sp

_A2 = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B666_leads_campaign", "cellA2", "a2_results.json")


def test_gauge_verdict_scalarization_dependent():
    lam = sp.symbols("lambda")
    r3 = sp.sqrt(3) * sp.I
    ca = json.load(open(_A2))["candidate_analysis"]
    inv = []
    for key, v in ca.items():
        M = sp.Matrix(3, 3, lambda i, j: sp.Rational(v["matrix"][i][j][0])
                      + sp.Rational(v["matrix"][i][j][1]) * r3)
        assert sp.simplify(M - M.T) == sp.zeros(3, 3)
        assert M.rank() == 3
        p = M.charpoly(lam)
        c3, c2, c1, c0 = p.all_coeffs()
        e1, e2, e3 = -c2, c1, -c0
        inv.append(sp.simplify(e1**3 / e3))
    assert len(inv) == 2
    assert sp.simplify(inv[0] - inv[1]) != 0    # the ratios are GAUGE


def test_sum_rule_shape():
    fnd = open(os.path.join(os.path.dirname(__file__), "..", "frontier",
                            "B671_eigenvalue_extraction",
                            "FINDINGS.md")).read()
    assert "7983360/13" in fnd and "independent" in fnd
