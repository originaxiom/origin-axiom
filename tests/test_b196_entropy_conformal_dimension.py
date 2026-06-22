"""B196 -- the entropy<->conformal-dimension bridge (V186). Fast locks.

Under Painleve-VI <-> c=1 (GIL), the metallic monodromy's bundle/time-monodromy (hyperbolic, tr=m^2+2) has c=1
conformal dimension Delta = -(ln lam_m/pi)^2 = -(topological entropy/2pi)^2. Exact identities + the cosh bridge.
Full version in entropy_dimension.py.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 40


def test_bridge_identities_exact():
    m = sp.symbols('m', positive=True, integer=True)
    lam = (m + sp.sqrt(m**2 + 4))/2
    assert sp.simplify(lam + 1/lam - sp.sqrt(m**2 + 4)) == 0
    assert sp.simplify(lam**2 + 1/lam**2 - (m**2 + 2)) == 0     # bundle monodromy trace on H1


def test_entropy_dimension_bridge():
    for mm in (1, 2, 3, 4):
        L = (mm + mp.sqrt(mm**2 + 4))/2
        P = mp.log(L)/mp.pi                       # Liouville momentum
        h = mp.log(L**2)                          # topological entropy
        Delta = -(P**2)
        assert abs(2*mp.cosh(2*mp.pi*P) - (mm**2 + 2)) < mp.mpf(10)**(-30)   # defines P
        assert abs(Delta - (-(h/(2*mp.pi))**2)) < mp.mpf(10)**(-30)          # Delta = -(h/2pi)^2
        assert Delta < 0                                                      # non-unitary (hyperbolic)


def test_twist_field_dimension():
    theta = sp.Rational(1, 4)
    assert theta**2 == sp.Rational(1, 16)         # four order-2 twist fields, Delta=1/16 (OPT->(0,4) cover)
