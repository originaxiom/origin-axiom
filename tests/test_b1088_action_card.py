"""B1088 lock: the parameter-free action card."""
import mpmath as mp
import sympy as sp

def test_volume_from_first_principles():
    mp.mp.dps = 60
    tet = 3 * (mp.clsin(2, 2*mp.pi/3) / 2)
    vol = 2 * tet
    assert abs(vol - mp.mpf("2.02988321281930725004240510854")) < mp.mpf(10)**(-28)

def test_cs_is_exactly_one_lattice_unit():
    mp.mp.dps = 60
    z = mp.e**(mp.mpc(0, 1)*mp.pi/3)
    cv = 2 * (mp.polylog(2, z) + mp.log(z)*mp.log(1-z)/2)
    frac = mp.re(cv) / (mp.pi**2/6)
    assert abs(frac - 1) < mp.mpf(10)**(-50)          # CS part = pi^2/6 exactly -> CS = 0
    vol = 2 * 3 * (mp.clsin(2, 2*mp.pi/3) / 2)
    assert abs(mp.im(cv) - vol) < mp.mpf(10)**(-50)   # Im part = the volume

def test_brown_henneaux_closure():
    sigma = sp.Symbol("sigma", positive=True)
    c = sp.Rational(3, 2) * 1 / (1/(4*sigma))
    assert sp.simplify(c - 6*sigma) == 0
