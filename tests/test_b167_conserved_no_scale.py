"""B167 -- the conserved => no-internal-scale lemma (V158). Fast symbolic locks.

Backbone [exact]: kappa is a conserved, dimensionless first integral of the trace map;
'conserved' is falsifiable (a coordinate is not conserved); a scale enters only externally
(door-4 non-vacuity witness). FIREWALL-SIDE: sharpens the wall; nothing to CLAIMS.md.
"""
import sympy as sp

x, y, z, lam, u = sp.symbols('x y z Lambda u')
kappa = x**2 + y**2 + z**2 - x*y*z - 2


def _Ta(p): X, Y, Z = p; return (X, Z, X*Z - Y)
def _Tb(p): X, Y, Z = p; return (Z, Y, Y*Z - X)
def _kap(p): X, Y, Z = p; return X**2 + Y**2 + Z**2 - X*Y*Z - 2
def _phi(p, m):
    for _ in range(m): p = _Tb(p)
    for _ in range(m): p = _Ta(p)
    return p


def test_kappa_is_conserved_first_integral():
    assert sp.expand(_kap(_Ta((x, y, z))) - kappa) == 0
    assert sp.expand(_kap(_Tb((x, y, z))) - kappa) == 0
    for m in (1, 2, 3):
        assert sp.expand(_kap(_phi((x, y, z), m)) - kappa) == 0


def test_conserved_is_falsifiable_control():
    # MB6/MB12: a coordinate is NOT conserved (Tb: x->z), and phi_1 does not fix the triple
    assert sp.expand(_Tb((x, y, z))[0] - x) != 0
    assert _phi((x, y, z), 1) != (x, y, z)


def test_kappa_dimensionless_not_unit_homogeneous():
    ku = (u*x)**2 + (u*y)**2 + (u*z)**2 - (u*x)*(u*y)*(u*z) - 2
    degs = {sp.Poly(t, u).degree() for t in sp.expand(ku).as_ordered_terms()}
    assert len(degs) > 1          # mixes u^0,u^2,u^3 => traces must be dimensionless


def test_door4_nonvacuity_witness():
    # a scale CAN enter, but only externally: units of kappa*Lambda^4 come from Lambda, not kappa
    assert sp.diff(kappa * lam**4, lam) != 0
    assert lam not in kappa.free_symbols
