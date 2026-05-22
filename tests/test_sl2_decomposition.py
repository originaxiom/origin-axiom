"""P11 — exact sl(2,R) decomposition of log(A)."""

import sympy as sp

from origin_axiom.algebra import A, log_A_sl2


def test_log_A_exponentiates_to_A():
    logA, _a, _d = log_A_sl2()
    assert sp.simplify(logA.exp() - A) == sp.zeros(2, 2)


def test_decomposition_ratio_is_exactly_two():
    _logA, a, d = log_A_sl2()
    assert sp.simplify(d / a - 2) == 0


def test_antisymmetric_component_is_exactly_zero():
    logA, _a, _d = log_A_sl2()
    # coefficient of the antisymmetric generator E - F
    assert sp.simplify(logA[0, 1] - logA[1, 0]) == 0
