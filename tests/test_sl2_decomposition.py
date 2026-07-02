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


def test_log_A_derived_independently_by_eigendecomposition():
    # Hardened 2026-07-01 (audit): log_A_sl2() hard-codes the closed-form
    # coefficients a = log(phi^2)/sqrt(5), d = 2a, so in isolation the ratio
    # test is not load-bearing. Here log(A) is *derived*: diagonalize A
    # exactly (A is symmetric positive-definite, so its principal log is
    # unique), take log on the spectrum, and match the closed form entrywise.
    from origin_axiom.constants import PHI_SQ

    P, D = A.diagonalize()
    lam = [sp.expand(D[i, i]) for i in range(2)]
    # the spectrum is {phi^2, phi^-2}: the two eigenvalues multiply to 1
    # exactly, so log(lam_small) = -log(lam_big) with no branch subtlety
    # (both are real and positive).
    assert sp.expand(lam[0] * lam[1] - 1) == 0
    signs = [1 if sp.expand(l - PHI_SQ) == 0 else -1 for l in lam]
    assert sorted(signs) == [-1, 1]
    logA_derived = sp.log(PHI_SQ) * sp.simplify(P * sp.diag(*signs) * P.inv())
    logA_closed, a, d = log_A_sl2()
    assert sp.simplify(logA_derived - logA_closed) == sp.zeros(2, 2)
    # and the coefficients really are a = log(phi^2)/sqrt(5), d/a = 2, read
    # off the derived matrix, not the constructor:
    a_derived = sp.simplify((logA_derived[0, 0] - logA_derived[1, 1]) / 2)
    d_derived = sp.simplify((logA_derived[0, 1] + logA_derived[1, 0]) / 2)
    assert sp.simplify(a_derived - a) == 0
    assert sp.simplify(d_derived / a_derived - 2) == 0
