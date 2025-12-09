"""
Constraint implementations for the Origin Axiom.

We enforce that the global complex amplitude A(t) does not enter a small
neighborhood of a forbidden configuration A*(θ*).

In this version we use a *gentle additive shift* of the field, which
moves the global amplitude out of the forbidden disc without violently
rescaling all modes.
"""

import numpy as np

def hard_constraint_factory(theta_star, epsilon, A_ref=0.0):
    """
    Returns a constraint(universe) function suitable for ScalarToyUniverse.step(constraint).

    Forbidden region:
        |A - A_star| < epsilon

    where:
        A_star = A_ref * exp(i θ*).

    Implementation:
        - If |A - A_star| >= epsilon: do nothing.
        - If |A - A_star| < epsilon:
            * choose a target amplitude A_target on the circle
              |A_target - A_star| = epsilon in the direction of (A - A_star)
              (or a fixed direction if A == A_star),
            * compute a uniform complex offset Δ such that
                  A_new = A + N_sites * Δ = A_target,
            * set Φ_n -> Φ_n + Δ for all lattice sites.
    """
    A_star = A_ref * np.exp(1j * theta_star)

    def constraint(universe):
        A = universe.global_amplitude()
        diff = A - A_star
        dist = np.abs(diff)

        if dist >= epsilon:
            return  # already outside forbidden disc

        # Record that the constraint fired
        if hasattr(universe, "constraint_hits"):
            universe.constraint_hits += 1

        # Number of sites
        N_sites = np.prod(universe.lat.shape)

        # Choose direction for the target amplitude on the circle
        if dist == 0.0:
            # If we are exactly at A_star, pick a fixed direction
            direction = np.exp(1j * theta_star)
        else:
            direction = diff / dist  # unit complex number

        # Target amplitude on the circle of radius epsilon around A_star
        A_target = A_star + epsilon * direction

        # Uniform offset to add to each lattice site
        delta = (A_target - A) / N_sites

        # Apply gentle additive shift
        universe.phi += delta

    return constraint
