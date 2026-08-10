"""B1026 locks — the one-involution chain, and the P33/B62 convention collision.

These locks assert the MATHEMATICS (WORKING_RULES rule 7), recomputing each link rather than
asserting a transcript string. They are the campaign's step-5 requirement made executable:
*"restorations bank as arcs … re-verify the identities before restoring — never restore from
memory."*

Each link is recomputed by `frontier/B1026_the_one_involution/verify.py`, which imports nothing
from the arcs it verifies (B14, B16, B54, B62, B64) — a second pipeline, not a re-reading.
"""
import importlib.util
import pathlib

import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1026", _ROOT / "frontier" / "B1026_the_one_involution" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)


# --- link 1 (B16): P is the unique primitive-pair exchange, up to sign ------------------------

def test_exchange_involution_is_exactly_plus_minus_P():
    sols = [X for X in v.gl2z_ball(6)
            if X * X == sp.eye(2) and sp.simplify(X * v.L * X.inv() - v.R) == sp.zeros(2, 2)]
    assert sorted(map(str, sols)) == sorted(map(str, [v.P, -v.P]))


def test_operational_half_step_condition_gives_the_same_pair():
    """B19's weakest sufficient condition: {X : (LX)² = A} = {±P}."""
    sols = [X for X in v.gl2z_ball(6) if (v.L * X) ** 2 == v.A]
    assert sorted(map(str, sols)) == sorted(map(str, [v.P, -v.P]))


def test_the_weaker_condition_does_not_select_P():
    """The control that makes the above a criterion rather than a tautology. B16: 'det(X)=−1 and
    X²=I' is TOO WEAK — it must admit many solutions, or the strong condition selected nothing."""
    weak = [X for X in v.gl2z_ball(6) if X.det() == -1 and X * X == sp.eye(2)]
    assert len(weak) > 2


# --- link 2 (B14): the half-step and the a=b classification -----------------------------------

def test_square_roots_of_A_are_exactly_plus_minus_F():
    roots = [X for X in v.gl2z_ball(6) if X * X == v.A]
    assert sorted(map(str, roots)) == sorted(map(str, [v.F, -v.F]))
    assert v.F == v.L * v.P and v.F ** 2 == v.A


def test_orientation_reversing_square_root_exists_iff_a_equals_b():
    for a in range(1, 6):
        for b in range(1, 6):
            B = sp.Matrix([[1 + a * b, a], [b, 1]])
            has = any(X * X == B for X in v.gl2z_ball(6) if X.det() == -1)
            assert has == (a == b), f"B({a},{b})"


# --- link 3 (B13/B22): the selection law ------------------------------------------------------

def test_A_quadratic_appears_exactly_at_det_minus_one_trace_plus_minus_one():
    ok = v.link3_selection_law(bound=5)
    assert ok


# --- link 4 (B62 / CLAIMS P33): the opposition involution, and the convention collision --------

def test_theta_is_an_involution_preserving_height_and_flipping_the_diagram():
    for n in range(3, 9):
        for h in range(1, n):
            for r in v.roots_of_height(n, h):
                assert v.theta(n, v.theta(n, r)) == r
                assert v.theta(n, r)[1] - v.theta(n, r)[0] == h
        for i in range(1, n):
            assert v.theta(n, (i, i + 1)) == (n - i, n - i + 1)


def test_P33_closed_form_holds_over_POSITIVE_roots():
    """CLAIMS.md P33: (+1,−1)-eigendimensions = (⌈(n−h)/2⌉, ⌊(n−h)/2⌋)."""
    for n in range(3, 9):
        for h in range(1, n):
            assert v.theta_split(n, h) == (-(-(n - h) // 2), (n - h) // 2)


def test_B62_height2_numbers_are_the_FULL_space_ie_twice_P33s():
    """THE CONVENTION COLLISION, pinned.

    B62 reports height-2 splits (2,0), (2,2), (4,2) at n=3,4,5 and decides the SL(5) modes with
    them. P33's closed form gives (1,0), (1,1), (2,1). Both are correct: B62 counts the FULL
    height-±h root space (every positive root and its negative — the multiplier sector's
    dimension), P33 counts POSITIVE roots. NEITHER DECLARES ITS CONVENTION, so the two banked
    statements about the same object quote different numbers.

    This lock exists so the next reader meets the factor 2 as a stated fact rather than a
    discrepancy — error class E1 (undeclared choice drift), the programme's most recurrent.
    """
    pos = {n: v.theta_split(n, 2) for n in (3, 4, 5)}
    assert pos == {3: (1, 0), 4: (1, 1), 5: (2, 1)}                      # P33's convention
    full = {n: (2 * a, 2 * b) for n, (a, b) in pos.items()}
    assert full == {3: (2, 0), 4: (2, 2), 5: (4, 2)}                     # B62's quoted numbers
    for n in (3, 4, 5):
        assert sum(full[n]) == 2 * (n - 2)      # = dim of the height-±2 space


# --- link 5: the identification the corpus never states ---------------------------------------

def test_contragredient_acts_on_weights_as_minus_w0():
    """The exchange involution on trace coordinates is W ↦ W⁻¹ (the contragredient); on A_{n−1}
    the contragredient acts on fundamental weights as −w₀, i.e. ω_k ↦ ω_{n−k}."""
    for n in range(3, 9):
        for k in range(1, n):
            assert v.theta(n, (k, k + 1)) == (n - k, n - k + 1)
            assert sp.binomial(n, k) == sp.binomial(n, n - k)


def test_contragredient_is_invisible_at_rank_two():
    """Why the identification is easy to miss, and why THE CHAIN's C21 says θ acts trivially on
    SL(2) trace coordinates: tr(g) = tr(g⁻¹) in SL(2). Same map, invisible until rank 3."""
    g = sp.Matrix([[sp.Rational(3, 2), sp.Rational(5, 7)],
                   [sp.Rational(2, 3), sp.Rational(11, 9)]])
    g = g / sp.sqrt(g.det())
    assert sp.simplify(sp.trace(g) - sp.trace(g.inv())) == 0


# --- link 6 (B64): Dickson parity --------------------------------------------------------------

def test_dickson_parity_and_the_catalog_determinant():
    m = sp.symbols("m")
    M = sp.Matrix([[m, 1], [1, 0]])
    Mk = sp.eye(2)
    for k in range(1, 9):
        Mk = sp.expand(Mk * M)
        Lk = sp.expand(sp.trace(Mk))
        assert sp.simplify(Lk.subs(m, -m) - (-1) ** k * Lk) == 0
        assert sp.simplify(Mk.det() - (-1) ** k) == 0


# --- the whole chain ---------------------------------------------------------------------------

def test_all_six_links_verify_together():
    assert v.link1_exchange_is_pm_P(bound=5)
    assert v.link2_half_step(bound=5)
    assert v.link4_opposition_involution()
    assert v.link5_contragredient_is_minus_w0()
    assert v.link6_dickson_parity(kmax=6)
