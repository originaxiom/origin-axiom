"""B660 — the structure campaign locks (cc2 packet, verified on receipt).

S2's cubic obstruction independently recomputed; S4's zero verdict
locked at the artifact level. See
frontier/B660_structure_campaign/FINDINGS.md.
"""
import json
import os

import sympy as sp

_PK = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B660_structure_campaign", "packet")


def test_s2_cubic_obstruction_independent():
    """Both monomial ansaetze reduce to X^3 = c with X^3 - c irreducible
    over Q(sqrt-3) — the K-rationality obstruction (verify_s2_cubic)."""
    X = sp.symbols('X')
    I3 = sp.sqrt(3) * sp.I
    c1 = (sp.Rational(46646891377, 49161262423)
          - sp.Rational(8960975540, 49161262423) * I3)
    c2 = (sp.Rational(7883324642713, 1924140653368707790695038976000)
          - sp.Rational(6883658483, 8746093878948671775886540800) * I3)
    for c in (c1, c2):
        fac = sp.factor_list(X**3 - c, extension=sp.sqrt(-3))
        assert len(fac[1]) == 1 and fac[1][0][1] == 1


def test_s2_verdict_and_flags():
    d = json.load(open(os.path.join(_PK, "s2_cp", "s2_results.json")))
    assert d["verdict"] == "DEGENERATE-INDISTINGUISHABLE"
    assert d["control_Ybar_neq_Y_nontrivial"] is True
    assert d["deck_swap_accessible"] is False        # the L103 record gap


def test_s4_zero_verdict():
    m = json.load(open(os.path.join(_PK, "s4_massshape",
                                    "s4_matrices.json")))
    assert m["verdict"] == "ZERO"
    assert m["M_antisymmetric"] is True and m["M_symmetric"] is False
    assert m["any_three_distinct"] is False
    R = m["M_5x5_readable"]
    # the solo-triple {2,3,4} block is the zero matrix; row 4 all zero
    assert all(R[i][j] == "0" for i in (2, 3, 4) for j in (2, 3, 4))
    assert all(x == "0" for x in R[4])


def test_s1_documentary_locks():
    p = os.path.join(_PK, "s1_gamma5", "FINDINGS_CC2.md")
    t = open(p).read()
    assert "CONSISTENT-NOT-SELECTIVE" in t
    assert "10-13" in t                # the pattern-space price
    assert os.path.exists(os.path.join(_PK, "s1_gamma5", "LIT_GATE_S1.md"))
