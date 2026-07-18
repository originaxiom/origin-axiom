"""B697 — phi is a Gaussian period of the 5th roots of unity."""
import sympy as sp


def test_phi_is_zeta5_gaussian_period():
    z = sp.exp(2*sp.I*sp.pi/5)
    assert sp.simplify(sp.re(z + z**4 + 1) - (1 + sp.sqrt(5))/2) == 0
