"""P8 — mapping-torus torsion |det(A^n - I)| and its log(phi^2) growth rate."""

import sympy as sp

from origin_axiom.constants import PHI_SQ
from origin_axiom.topology import torsion_growth_rate, torsion_order


def test_torsion_orders():
    # |det(A^n - I)| = L_{2n} - 2  (Lucas numbers): 1, 5, 16, 45, ...
    expected = {1: 1, 2: 5, 3: 16, 4: 45, 5: 121}
    for n, value in expected.items():
        assert torsion_order(n) == value


def test_torsion_growth_rate_converges_to_log_phi_squared():
    target = float(sp.log(PHI_SQ))
    assert abs(float(torsion_growth_rate(40)) - target) < 1e-3
    # |det(A^n - I)| = phi^{2n} * (1 - phi^{-2n})^2, so the rate rises toward
    # log(phi^2) from below as n grows.
    rate_10 = float(torsion_growth_rate(10))
    rate_60 = float(torsion_growth_rate(60))
    assert rate_10 < rate_60 <= target
