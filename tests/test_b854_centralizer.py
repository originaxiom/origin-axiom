"""Locks B854 -- the exact centralizer of 2T in e6 is abelian (u(1)^4).

The full E6 build takes ~100s, so the heavy facts are locked against the arc's committed
results.json and the CHEAP-but-decisive structure is recomputed here: the 2T invariant theory,
the transvectant grading, and the two-Killing-forms distinction that the competing claim conflated.
"""
import json
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B854_centralizer_exact"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = (_D / "FINDINGS.md").read_text(encoding="utf-8")

x, y = sp.symbols("x y")


# ---------------------------------------------------------------------------------------
# The E6 build's own verification, as recorded
# ---------------------------------------------------------------------------------------
def test_the_e6_build_verified_itself_before_being_used():
    assert RES["roots_positive"] == 36 and RES["roots_total"] == 72
    assert RES["dim"] == 78
    assert RES["exponents"] == [1, 4, 5, 7, 8, 11], "the E6 exponents must be RECOVERED"


def test_all_six_brackets_vanish():
    assert RES["all_brackets_vanish"] is True
    assert len(RES["brackets"]) == 6
    assert all(RES["brackets"].values())
    assert RES["brackets"]["[x14,x22]"] is True, "the decisive bracket"


def test_the_invariants_are_independent():
    assert RES["invariant_rank"] == 4


# ---------------------------------------------------------------------------------------
# THE DISTINCTION THE COMPETING CLAIM CONFLATED
# ---------------------------------------------------------------------------------------
def test_the_two_killing_forms_are_different_objects():
    """K_e6|_C is nondegenerate (rank 4) on a torus; K_C is identically zero.

    The form that separates u(1)^4 from su(2)+u(1) is K_C. A numerical rank-4 restriction with one
    small eigenvalue reads as 'rank 3 plus a zero mode' -- exactly what su(2)+u(1) needs.
    """
    assert RES["K_e6_restricted_rank"] == 4, "restriction is nondegenerate, as on a torus"
    assert RES["K_C_rank"] == 0, "the intrinsic Killing form of an abelian algebra is zero"


def test_no_four_dimensional_semisimple_lie_algebra_exists():
    """Why a 4-dim reductive algebra MUST have a centre -- so 'centre = 0' is fatal, not marginal.

    Simple Lie algebras have dimensions 3, 8, 10, 14, 15, 21, 24, 28, ... Sums of these cannot
    make 4, so a 4-dim semisimple algebra is impossible.
    """
    simple_dims = [3, 8, 10, 14, 15, 21, 24, 28, 35, 36, 45, 52, 78, 133, 248]
    reach = {0}
    for _ in range(4):
        reach |= {r + d for r in reach for d in simple_dims if r + d <= 4}
    assert 4 not in reach, "if this ever passes, the centre argument needs rewriting"


# ---------------------------------------------------------------------------------------
# The 2T invariant theory -- cheap and fully recomputed
# ---------------------------------------------------------------------------------------
def _twoT():
    I, h = sp.I, sp.Rational(1, 2)
    def q(a, b, c, d):
        return sp.Matrix([[a + b * I, c + d * I], [-c + d * I, a - b * I]])
    els = []
    for s in (1, -1):
        els += [q(s, 0, 0, 0), q(0, s, 0, 0), q(0, 0, s, 0), q(0, 0, 0, s)]
    for sa in (1, -1):
        for sb in (1, -1):
            for sc in (1, -1):
                for sd in (1, -1):
                    els.append(q(sa * h, sb * h, sc * h, sd * h))
    return els


def test_2T_has_order_24_and_lies_in_SU2():
    els = _twoT()
    assert len(els) == 24
    assert all(sp.simplify(m.det()) == 1 for m in els)


def test_the_invariant_multiplicities_are_one_in_exactly_four_blocks():
    """Rank of the averaging projector: 1 in V8,V14,V16,V22 and 0 in V2,V10. Gives dim C = 4."""
    els = _twoT()
    def symn(M, n):
        X, Y = M[0, 0] * x + M[1, 0] * y, M[0, 1] * x + M[1, 1] * y
        cols = []
        for k in range(n + 1):
            p = sp.Poly(sp.expand(X ** (n - k) * Y ** k), x, y)
            cols.append([p.coeff_monomial(x ** (n - j) * y ** j) for j in range(n + 1)])
        return sp.Matrix(cols).T
    got = {}
    for n in (2, 8, 10):                       # cheap subset; 14/16/22 are locked via results.json
        P = sp.zeros(n + 1, n + 1)
        for M in els:
            P += symn(M, n)
        got[n] = sp.simplify(P / 24).rank()
    assert got == {2: 0, 8: 1, 10: 0}, got


# ---------------------------------------------------------------------------------------
# The Z/2 grading -- exact, E6-free, and it is what reduced the problem to one bracket
# ---------------------------------------------------------------------------------------
def _transvectant(f, g, r):
    return sp.expand(sum((-1) ** k * sp.binomial(r, k)
                         * sp.diff(f, x, r - k, y, k) * sp.diff(g, x, k, y, r - k)
                         for k in range(r + 1)))


def test_odd_transvectants_vanish_and_even_ones_do_not():
    P = sp.expand((x**4 - 2*x**3*y + 2*x**2*y**2 + 2*x*y**3 + y**4)
                  * (x**4 + 2*x**3*y + 2*x**2*y**2 - 2*x*y**3 + y**4))
    t = sp.expand(x * y * (x**4 - y**4))
    INV = {8: P, 14: sp.expand(t * P), 16: sp.expand(P**2), 22: sp.expand(t * P**2)}
    for n, f in INV.items():
        assert sp.Poly(f, x, y).total_degree() == n
    checked = 0
    for (a, b) in [(8, 14), (8, 16), (8, 22), (14, 16), (14, 22), (16, 22)]:
        for c in (8, 14, 16, 22):
            if (a + b - c) % 2:
                continue
            r = (a + b - c) // 2
            if r < 0 or r > min(a, b):
                continue
            T = _transvectant(INV[a], INV[b], r)
            assert (T == 0) == (r % 2 == 1), f"({a},{b}) r={r}: parity rule broken"
            checked += 1
    assert checked >= 20, f"only {checked} transvectants exercised"


# ---------------------------------------------------------------------------------------
# Honesty locks
# ---------------------------------------------------------------------------------------
def test_the_controls_are_recorded_in_the_findings():
    """A vanishing result is worthless without a control that could have made it nonzero."""
    assert "NONZERO 5/5" in _F
    assert "random elements of the same blocks" in _F


def _norm(t):
    """Fold subscript/superscript digits and case. The prose uses E-subscript-6, not 'E6';
    matching one form but not the other is how a prose lock fails on correct text."""
    sub = {"\u2080":"0","\u2081":"1","\u2082":"2","\u2083":"3","\u2084":"4",
           "\u2085":"5","\u2086":"6","\u2087":"7","\u2088":"8","\u2089":"9",
           "\u2074":"4","\u00b2":"2","\u00b3":"3","\u2019":"'"}
    for k, v in sub.items():
        t = t.replace(k, v)
    return t.lower()


def test_the_arc_states_what_it_does_not_close():
    f = _norm(_F)
    assert _norm("Does not close the E\u2086 chain") in f
    assert "non-principal" in f, "another embedding could differ; must be said"


def test_the_verdict_is_abelian():
    assert "ABELIAN" in RES["verdict"] and "u(1)^4" in RES["verdict"]
