"""B483 — the Fibonacci-anyon face: exact recompute of the anyon table + the
golden identities, and a doc-integrity lock on the B1-closed / firewall verdicts.

Recompute tier (exact, sympy/Fraction): the SU(2)_3 data (h_a = a(a+2)/20, central
charge 9/5, quantum dims 1, phi, phi, 1), theta_2 = zeta5^2 as an exact twist,
tau x tau = 1 + tau <-> the golden substitution (same characteristic polynomial
x^2 - x - 1), the FORCED arithmetic 3:8:15 = a(a+2) = (a+1)^2 - 1 (adjoint dims of
SU(2), SU(3), SU(4) — the count-matching trap, not gauge data), and the figure-eight
Jones values V(zeta5) = 1 - sqrt5 = -2/phi and V(zeta10) = 0 exactly.

Doc-integrity tier (not a recompute): the B1-closed verdict (the banked lambda_chain
1.57705744122666946 is CORRECT — seat-2's warning applied to their normalization),
the colored-Jones multiset, the torsion-wall insight, and the ninth kill label.
"""
import pathlib
from fractions import Fraction as Fr

import sympy as sp

FINDINGS = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
            / "B483_fibonacci_anyon_face" / "FINDINGS.md").read_text(encoding="utf-8")


def test_su2_level3_anyon_table_exact():
    """h_a = a(a+2)/20 = {0, 3/20, 2/5, 3/4}; c = 3k/(k+2) = 9/5; quantum dims
    sin((a+1)pi/5)/sin(pi/5) = 1, phi, phi, 1 — exactly."""
    hs = [Fr(a * (a + 2), 20) for a in range(4)]
    assert hs == [Fr(0), Fr(3, 20), Fr(2, 5), Fr(3, 4)]
    assert Fr(3 * 3, 3 + 2) == Fr(9, 5)                    # central charge
    qdims = [sp.simplify(sp.sin((a + 1) * sp.pi / 5) / sp.sin(sp.pi / 5) - w)
             for a, w in ((0, 1), (1, sp.GoldenRatio), (2, sp.GoldenRatio), (3, 1))]
    assert qdims == [0, 0, 0, 0]


def test_twist_theta2_is_zeta5_squared_exact():
    """theta_2 = e^{2 pi i h_2} with h_2 = 2/5: exactly zeta5^2 (order 5) — the
    exact golden 5-torsion living on the TQFT side of the torsion wall."""
    h2 = Fr(2, 5)
    assert 20 * h2 == 8                                    # zeta20^8 = zeta5^2
    theta2 = sp.exp(2 * sp.pi * sp.I * sp.Rational(2, 5))
    assert sp.simplify(theta2**5 - 1) == 0 and sp.simplify(theta2 - 1) != 0
    assert sp.simplify(theta2 - sp.exp(2 * sp.pi * sp.I / 5) ** 2) == 0


def test_fusion_rule_is_the_golden_substitution():
    """tau x tau = 1 + tau IS phi^2 = phi + 1: the fusion matrix [[0,1],[1,1]] and
    the substitution matrix of sigma: a -> ab, b -> a share char poly x^2 - x - 1
    with largest root phi."""
    x = sp.symbols("x")
    fusion = sp.Matrix([[0, 1], [1, 1]])
    subst = sp.Matrix([[1, 1], [1, 0]])
    assert fusion.charpoly(x).as_expr() == x**2 - x - 1
    assert subst.charpoly(x).as_expr() == x**2 - x - 1
    assert sp.simplify(sp.GoldenRatio**2 - sp.GoldenRatio - 1) == 0


def test_jones_figure_eight_golden_values_exact():
    """V(4_1; t) = t^2 - t + 1 - 1/t + 1/t^2: V(zeta5) = 1 - sqrt5 = -2/phi and
    V(zeta10) = 0, exactly (the golden-field values; banked B314, re-verified)."""
    def V(q):
        return q**2 - q + 1 - 1 / q + 1 / q**2
    z5 = sp.exp(2 * sp.pi * sp.I / 5)
    z10 = sp.exp(sp.pi * sp.I / 5)
    assert sp.simplify(sp.expand_complex(V(z5) - (1 - sp.sqrt(5)))) == 0
    assert sp.simplify(-2 / sp.GoldenRatio - (1 - sp.sqrt(5))) == 0
    assert sp.simplify(sp.expand_complex(V(z10))) == 0


def test_3_8_15_is_forced_arithmetic_not_gauge():
    """20 h_a = a(a+2) = (a+1)^2 - 1 for a = 1, 2, 3 gives 3, 8, 15 — the adjoint
    dims of SU(2), SU(3), SU(4) by an algebraic identity (NOT the SM's group list:
    SU(4) is not in the SM, U(1) is missing). The overlay is the count-matching trap."""
    nums = tuple(20 * Fr(a * (a + 2), 20) for a in (1, 2, 3))
    assert nums == (3, 8, 15)
    for a in range(1, 10):
        assert a * (a + 2) == (a + 1) ** 2 - 1             # forced identity
    assert "Ninth count-matching kill." in FINDINGS


def test_b1_closed_and_firewall_verdicts_locked():
    """Documentation-integrity lock (not a recompute): B1 CLOSED with the banked
    lambda_chain confirmed correct; the colored-Jones golden multiset; the banked
    unification statement; the torsion-wall insight (no 5-torsion on the Weil side)."""
    assert "## B1 CLOSED — the banked λ_chain is CORRECT (not a rung artifact)" in FINDINGS
    assert "1.57705744122666946" in FINDINGS
    assert "CORRECT to all 18 printed digits" in FINDINGS
    assert "{1, 1−√5, 1−√5, 1} ⊂ ℚ(√5)" in FINDINGS
    # (the phrase wraps across a line break in the file after "The")
    assert "object IS a face of the Fibonacci-anyon TQFT" in FINDINGS
    assert "No 5-torsion" in FINDINGS
