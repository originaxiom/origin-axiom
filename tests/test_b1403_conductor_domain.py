"""B1403 — the cusp field is quadratic only at m = 1, 2, so B1002's gcd has a two-point domain."""
import math
from fractions import Fraction

import pytest

mp = pytest.importorskip("mpmath")
snappy = pytest.importorskip("snappy")


DPS = 60


def _is_rat(x):
    """PSLQ at FULL precision -- Fraction(float(x)) truncates at 1e-16 and can never match a
    non-dyadic rational like 13/12, which is exactly the m=1 answer.

    The precision is set EXPLICITLY here rather than relying on the ambient mp.mp.dps: pslq
    does tol = to_fixed(tol, prec) and then asserts it is non-zero, so a low ambient precision
    turns a 1e-40 tolerance into 0 and the call dies. Global numeric state is not a contract.
    """
    with mp.workdps(DPS):
        tol = mp.mpf(10) ** -30
        if abs(x) < tol:
            return True, Fraction(0)
        rel = mp.pslq([x, mp.mpf(1)], tol=mp.mpf(10) ** -40, maxcoeff=10 ** 8, maxsteps=10000)
        if not rel or rel[0] == 0:
            return False, None
        f = Fraction(-int(rel[1]), int(rel[0]))
        return (abs(mp.mpf(f.numerator) / f.denominator - x) < tol), f


def _quad(tau):
    with mp.workdps(DPS):
        b = -mp.im(tau * tau) / mp.im(tau)
        c = -mp.re(tau * tau) - b * mp.re(tau)
    okb, fb = _is_rat(b)
    okc, fc = _is_rat(c)
    return (okb and okc), fb, fc


def _tau(m):
    """HIGH precision -- going through complex() truncates and the exact test then always fails."""
    M = snappy.Manifold("b++" + "R" * m + "L" * m).high_precision()
    sh = M.cusp_info('shape')[0]
    with mp.workdps(DPS):
        return mp.mpc(mp.mpf(str(sh.real()).replace(' ', '')),
                      mp.mpf(str(sh.imag()).replace(' ', '')))


def test_the_rationality_test_is_not_fooled_by_non_dyadic_denominators():
    """THE CONTROL THAT CAUGHT THE BUG. A first version used only 0, 1, 4, -1 -- all exactly
    representable -- and so never exercised the float truncation."""
    # the VALUES must be built at full precision too -- a first version constructed them at
    # the ambient precision and the control failed for the very reason it exists to catch.
    with mp.workdps(DPS):
        thirteen_twelfths = mp.mpf(13) / 12
        pi = +mp.pi
        m1_tau = 1 + mp.sqrt(-3) / 6
    ok, f = _is_rat(thirteen_twelfths)
    assert ok and f == Fraction(13, 12), (ok, f)
    ok2, _ = _is_rat(pi)
    assert not ok2, "must reject a transcendental"
    # and the quadratic test on the value whose c is non-dyadic
    q, b, c = _quad(m1_tau)
    assert q and b == Fraction(-2) and c == Fraction(13, 12), (q, b, c)


def test_golden_and_silver_are_quadratic_and_reproduce_B675s_fields():
    q1, b1, c1 = _quad(_tau(1))
    assert q1 and b1 == Fraction(-2) and c1 == Fraction(13, 12), (q1, b1, c1)
    d1 = b1 * b1 - 4 * c1
    assert d1 == Fraction(-1, 3), d1
    assert d1 * 9 == -3, "disc -1/3 and -3 differ by a square, so the field is Q(sqrt-3)"
    q2, b2, c2 = _quad(_tau(2))
    assert q2 and b2 == 0 and c2 == Fraction(1, 4), (q2, b2, c2)
    assert b2 * b2 - 4 * c2 == -1, "field Q(i)"


def test_the_family_leaves_the_quadratic_world_at_bronze():
    for m in range(3, 7):
        q, _, _ = _quad(_tau(m))
        assert not q, f"m={m} must NOT be quadratic"


def test_the_two_domains_are_disjoint():
    """B1002's gcd exists at m = 1, 2 -- both UNITS of Z/15, both branch B. gcd(m,15)'s content
    is on branch A. No m is informative for both."""
    conductor_domain = [1, 2]
    for m in conductor_domain:
        assert math.gcd(m, 15) == 1, f"m={m} must be a unit -> branch B"
    branch_A = [m for m in range(1, 16) if math.gcd(m, 15) > 1]
    assert branch_A == [3, 5, 6, 9, 10, 12, 15]
    assert not (set(conductor_domain) & set(branch_A)), "the domains must not overlap"
    assert min(branch_A) == 3, "and the conductor fails at the very first branch-A member"
