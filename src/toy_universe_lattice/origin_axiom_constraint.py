"""
Constraint implementations for the Origin Axiom.

We enforce that the global complex amplitude A(t) does not enter a small
neighborhood of a forbidden configuration A*(θ*).
"""

import numpy as np

def hard_constraint_factory(theta_star, epsilon, A_ref=0.0):
    """
    Returns a constraint(universe) function suitable for ScalarToyUniverse.step(constraint).

    Forbidden region:
        |A - A_star| < epsilon

    where:
        A_star = A_ref * exp(i θ*)

    For v0.1, we often take A_ref = 0.0 so that the forbidden configuration
    is "global cancellation" A ≈ 0 with a certain phase structure baked in θ*.
    """
    A_star = A_ref * np.exp(1j * theta_star)

    def constraint(universe):
        A = universe.global_amplitude()
        diff = A - A_star
        dist = np.abs(diff)

        if dist < epsilon:
            # Heuristic push: rescale Φ so that A is moved radially outward
            # away from the forbidden region.
            #
            # We choose a minimal factor so that |A_new - A_star| = epsilon.
            # If diff == 0 (pathological), we just apply a small random phase.
            if dist == 0.0:
                phase_kick = np.exp(1j * (epsilon))
                universe.phi *= phase_kick
            else:
                factor = (epsilon / dist)
                # Move A outward along the same complex direction:
                # A_new - A_star = factor * (A - A_star)
                # We approximate this by globally scaling Φ.
                universe.phi *= factor

    return constraint
