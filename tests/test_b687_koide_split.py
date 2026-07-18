"""B687 — h(27)=2/3 and the Koide 45-degree constraint."""
import sympy as sp
import mpmath as mp


def test_h27_is_two_thirds():
    assert sp.Rational(1*78, 1+12) == 6            # c(E6,1)=6
    assert sp.Rational(52, 3)/(2*(1+12)) == sp.Rational(2, 3)   # h(27)=2/3


def test_koide_is_45_degrees():
    mp.mp.dps = 25
    v = [mp.sqrt(m) for m in (mp.mpf('0.51099895'),
                              mp.mpf('105.6583755'), mp.mpf('1776.86'))]
    costh = sum(v)/(mp.sqrt(sum(x*x for x in v))*mp.sqrt(3))
    assert abs(mp.acos(costh)*180/mp.pi - 45) < 1e-2   # Q=2/3 <=> 45 deg
