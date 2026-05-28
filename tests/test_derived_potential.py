"""P16 — the derived potential.

The gradient flow ``v = -dV/dtau`` integrates to the cubic potential
``V(tau) = KAPPA*(tau^3/3 - tau^2/2 - tau)``, with ``V'(tau) = KAPPA*(tau^2 - tau - 1)``.
The minimum is at ``phi`` (V'' = +KAPPA*sqrt(5)), the maximum at ``-1/phi``
(V'' = -KAPPA*sqrt(5)), and ``tau = 0`` is NOT a critical point (V'(0) = -KAPPA).

Pure algebra — antiderivative of P15's vector field. No physical interpretation.
"""

import sympy as sp

from origin_axiom.constants import PHI
from origin_axiom.mobius import (
    KAPPA,
    mass_squared,
    potential,
    potential_derivative,
    potential_second_derivative,
    tau,
    vector_field,
)


def test_potential_derivative_is_the_golden_polynomial():
    """``V'(tau) = KAPPA*(tau^2 - tau - 1)`` exactly (differentiate V)."""
    Vp = sp.diff(potential(), tau)
    assert sp.simplify(Vp - potential_derivative()) == 0
    assert sp.simplify(Vp - KAPPA * (tau**2 - tau - 1)) == 0


def test_gradient_flow_relation():
    """``v(tau) = -V'(tau)`` exactly: the vector field is minus the potential gradient."""
    assert sp.simplify(vector_field() + potential_derivative()) == 0


def test_phi_is_a_critical_point():
    """``V'(phi) = 0`` since ``phi^2 - phi - 1 = 0``."""
    assert sp.simplify(potential_derivative(PHI)) == 0


def test_minus_one_over_phi_is_a_critical_point():
    """``V'(-1/phi) = 0``."""
    assert sp.simplify(potential_derivative(-1 / PHI)) == 0


def test_phi_is_a_minimum():
    """``V''(phi) = KAPPA*sqrt(5) > 0``. The golden vacuum is stable."""
    Vpp = potential_second_derivative(PHI)
    assert sp.simplify(Vpp - KAPPA * sp.sqrt(5)) == 0
    assert float(Vpp) > 0


def test_minus_one_over_phi_is_a_maximum():
    """``V''(-1/phi) = -KAPPA*sqrt(5) < 0``. The other extremum is unstable."""
    Vpp = potential_second_derivative(-1 / PHI)
    assert sp.simplify(Vpp + KAPPA * sp.sqrt(5)) == 0
    assert float(Vpp) < 0


def test_zero_is_not_a_critical_point():
    """``V'(0) = -KAPPA != 0``. 'Nothing' (tau = 0) is not an equilibrium of the flow."""
    assert sp.simplify(potential_derivative(0) + KAPPA) == 0
    assert float(potential_derivative(0)) != 0


def test_mass_squared_is_kappa_root5():
    """``mass^2 = V''(phi) = KAPPA*sqrt(5)``; numerical anchor ~1.924847."""
    assert sp.simplify(mass_squared() - KAPPA * sp.sqrt(5)) == 0
    assert abs(float(mass_squared()) - 1.924847) < 1e-6


def test_potential_values_at_extrema():
    """Numerical anchors for V at the two critical points (with KAPPA included)."""
    # V(phi) with the KAPPA prefactor = -1.304163 (NOT -1.515028, which omits KAPPA).
    assert abs(float(potential(PHI)) - (-1.304163)) < 1e-6
    assert abs(float(potential(-1 / PHI)) - 0.299876) < 1e-6
