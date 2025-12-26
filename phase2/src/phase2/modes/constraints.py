from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Tuple

import numpy as np

# ============================================================
# Origin Axiom — Phase 2
# Constraints / enforcement primitives
#
# The Origin Axiom is implemented here as a global non-cancellation floor:
# given a complex global amplitude A, enforce |A| >= epsilon.
#
# IMPORTANT:
# - This is a *global* constraint and is not a standard local QFT term.
# - Phase 2 treats epsilon as a model parameter (not derived).
# - Enforcement is designed to be deterministic given a fixed seed.
# ============================================================


@dataclass(frozen=True)
class ConstraintActivity:
    applied: bool
    epsilon: float
    magnitude_before: float
    magnitude_after: float
    delta_magnitude: float
    direction_source: str  # "preserve_direction" or "random_direction"


def _unit_complex_from_angle(theta: float) -> complex:
    return complex(math.cos(theta), math.sin(theta))


def enforce_global_floor(A: complex, *, epsilon: float, rng: np.random.Generator) -> Tuple[complex, ConstraintActivity]:
    """
    Enforce the Origin Axiom floor on a global complex amplitude.

    Input:
      A: complex amplitude (proxy for net cancellation)
      epsilon: floor magnitude (must be > 0)
      rng: numpy Generator (used only if A == 0 for direction choice)

    Output:
      (A_enforced, activity)

    Rule:
      If |A| >= epsilon: do nothing.
      If 0 < |A| < epsilon: rescale to magnitude epsilon, preserving direction.
      If A == 0: set magnitude epsilon in a random direction (seed-controlled).
    """
    if epsilon <= 0.0 or not np.isfinite(epsilon):
        raise ValueError(f"epsilon must be positive finite, got {epsilon}")

    mag = float(abs(A))

    if mag >= epsilon:
        return A, ConstraintActivity(
            applied=False,
            epsilon=float(epsilon),
            magnitude_before=mag,
            magnitude_after=mag,
            delta_magnitude=0.0,
            direction_source="preserve_direction",
        )

    if mag > 0.0:
        scale = epsilon / mag
        A2 = complex(A.real * scale, A.imag * scale)
        return A2, ConstraintActivity(
            applied=True,
            epsilon=float(epsilon),
            magnitude_before=mag,
            magnitude_after=float(abs(A2)),
            delta_magnitude=float(abs(A2) - mag),
            direction_source="preserve_direction",
        )

    # mag == 0: choose a direction deterministically from rng
    theta = float(rng.uniform(0.0, 2.0 * math.pi))
    A2 = epsilon * _unit_complex_from_angle(theta)

    return A2, ConstraintActivity(
        applied=True,
        epsilon=float(epsilon),
        magnitude_before=0.0,
        magnitude_after=float(abs(A2)),
        delta_magnitude=float(abs(A2)),
        direction_source="random_direction",
    )
