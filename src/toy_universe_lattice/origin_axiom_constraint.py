"""
Constraint implementations for the Origin Axiom:

We enforce that the global complex amplitude A(t) does not enter a small
neighborhood of a forbidden configuration A*(θ*).
"""

import numpy as np

def hard_constraint_factory(theta_star, epsilon, A_ref=0.0):
    """
    Returns a constraint function suitable for ScalarToyUniverse.step(constraint).
    Forbidden region: |A - A_star| < epsilon, where A_star is derived from theta_star.

    For v0.1, we can take:
      A_star = A_ref * np.exp(1j * theta_star)
    or simply A_star = np.exp(1j * theta_star) if A_ref=1.
    """
    A_star = A_ref * np.exp(1j * theta_star)

    def constraint(universe):
        A = universe.global_amplitude()
        if np.abs(A - A_star) < epsilon:
            # Simple reflection: move A away from forbidden region
            # by rescaling the field slightly. This is heuristic and
            # will likely be refined in later versions.
            delta = epsilon - np.abs(A - A_star)
            # Apply a small global phase or amplitude tweak
            phase_kick = np.exp(1j * delta * np.angle(A - A_star))
            universe.phi *= phase_kick

    return constraint
