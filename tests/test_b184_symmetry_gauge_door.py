"""B184 -- the symmetry/gauge door (V178). Fast locks (algebra + PSLQ).

A gauge group is NOT forced by the collective. Each unit has a forced INFLATION symmetry (x lam_m =
the companion [[m,1],[1,0]] in GL(2,Z)); the interaction of DISTINCT-field units BREAKS it (the
cross-product alpha_1*alpha_2 escapes the module) and only MULTIPLIES the per-unit dualities
(proliferation, not selection). Same-field units keep a shared inflation (field-not-count, cf. B182).
Full version in symmetry_gauge.py.
"""
import numpy as np
import pytest
from mpmath import mp, mpf, sqrt, pslq, log


@pytest.fixture(autouse=True)
def _mp_dps():
    """set precision per-test (not at module level) so collection order can't leak a lower global dps."""
    mp.dps = 50


def _lam(m):   return (m + sqrt(m * m + 4)) / 2
def _alpha(m): return (sqrt(m * m + 4) - m) / 2


def test_each_unit_has_forced_inflation_symmetry():
    # x lam_m is a module automorphism of Z + Z*alpha_m: lam*1 = m+alpha, lam*alpha = 1, companion det -1
    for m in (1, 2, 3):
        L, a = _lam(m), _alpha(m)
        assert abs(L * 1 - (m + a)) < mpf("1e-30")
        assert abs(L * a - 1) < mpf("1e-30")
        assert int(round(np.linalg.det(np.array([[m, 1], [1, 0]])))) == -1


def test_distinct_field_interaction_breaks_inflation():
    # cross-product escapes span{1,a1,a2} (rank 4) -> no common inflation
    a1, a2 = _alpha(1), _alpha(2)
    assert pslq([mpf(1), a1, a2, a1 * a2], maxcoeff=10**8, maxsteps=10**5) is None


def test_same_field_keeps_shared_inflation():
    # control (field-not-count): same-field product stays in span{1,a1} -> a shared inflation survives
    b1, b4 = _alpha(1), _alpha(4)
    assert pslq([mpf(1), b1, b1 * b4], maxcoeff=10**8, maxsteps=10**5) is not None
    assert abs(2 - 3 * b1 - b1 * b4) < mpf("1e-30")          # a1*a4 = 2 - 3 a1


def test_inflations_proliferate_with_distinct_fields():
    # distinct lam multiplicatively independent -> independent inflation directions grow with N
    assert pslq([log(_lam(1)), log(_lam(2))], maxcoeff=10**9, maxsteps=10**5) is None
