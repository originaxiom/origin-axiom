"""B683 arithmetic-ledger locks."""
from fractions import Fraction

import mpmath as mp
import sympy as sp


def _v5(x):
    x = Fraction(x); n, d, v = x.numerator, x.denominator, 0
    while n and n % 5 == 0:
        n //= 5; v += 1
    while d and d % 5 == 0:
        d //= 5; v -= 1
    return v


def _s5(n):
    s = 0
    while n:
        s += n % 5; n //= 5
    return s


def test_L1_divided_power_binomial_valuation():
    vfac = lambda n: (n - _s5(n)) // 4
    for m in range(1, 40):
        C = sp.binomial(sp.Rational(-3, 5), m)
        assert _v5(Fraction(int(C.p), int(C.q))) == -(m + vfac(m))
    phi = [m + vfac(m) for m in range(1, 60)]
    assert all(phi[i] > phi[i-1] for i in range(1, len(phi)))


def test_L2_inert5_and_sqrt5_degenerate():
    assert sp.jacobi_symbol(-3, 5) == -1          # 5 inert
    assert (25*24*26//2) == 7800 and 7800 % 60 == 0
    assert (1 + 4) % 5 == 0                        # disc(x^2-x-1)=5≡0 mod5
    assert (9 - 3 - 1) % 5 == 0                    # phi=3 double root mod5


def test_L3_mahler_is_volume_over_pi():
    mp.mp.dps = 40
    Vol = 2*mp.im(mp.polylog(2, mp.e**(1j*mp.pi/3)))
    m = mp.mpf('0.6461318944389010281872730214476127881445')
    assert abs(Vol/mp.pi - m) < mp.mpf(10)**-30
