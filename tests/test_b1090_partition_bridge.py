"""B1090 lock: the omega-saddle, the saddle value, the closed form's self-consistency."""
import sympy as sp
import mpmath as mp

def test_saddle_is_omega():
    u = sp.Symbol("u")
    assert sp.expand((1 + u)**2 - u) == u**2 + u + 1
    roots = sp.solve(u**2 + u + 1, u)
    assert set(roots) == {sp.Rational(-1, 2) - sp.sqrt(3)*sp.I/2,
                          sp.Rational(-1, 2) + sp.sqrt(3)*sp.I/2}

def test_saddle_value_is_pi2_over_6_minus_i_vol():
    mp.mp.dps = 40
    z = mp.mpc(0, -2*mp.pi/3)
    v2 = -2*mp.polylog(2, -mp.e**z) - z**2/2
    vol = 2*3*(mp.clsin(2, 2*mp.pi/3)/2)
    assert abs(mp.re(v2) - mp.pi**2/6) < mp.mpf(10)**(-38)
    assert abs(mp.im(v2) + vol) < mp.mpf(10)**(-38)
    assert abs(2*mp.log(1 + mp.e**z) - z) < mp.mpf(10)**(-38)   # the saddle equation

def test_gk_closed_form_value():
    mp.mp.dps = 30
    V = 2*mp.im(mp.polylog(2, mp.e**(1j*mp.pi/3)))
    closed = mp.e**(1j*mp.pi/6)/mp.sqrt(3)*(mp.e**(V/(2*mp.pi)) - mp.e**(-V/(2*mp.pi)))
    # the value this bench reproduced numerically at 7.6e-8 from Faddeev's definition
    assert abs(closed - mp.mpc("0.328715166", "0.189783790")) < 1e-8
