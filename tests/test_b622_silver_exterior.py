"""B622 lock: the silver (m136) exterior adjoint torsion via the exact
eigenvalue identity, and the fig-8 calibration."""
import sympy as sp


def test_silver_exterior_adjoint():
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(phi ** 6 - (9 + 4 * sp.sqrt(5))) == 0
    assert sp.simplify((1 - phi ** 6) * (1 - phi ** -6) + 16) == 0


def test_fig8_calibration_face():
    # mu + 1/mu = 5 => (1-mu)(1-1/mu) = 2 - 5 = -3 (the banked tau_1)
    mu = (5 + sp.sqrt(21)) / 2
    assert sp.simplify((1 - mu) * (1 - 1 / mu) + 3) == 0
