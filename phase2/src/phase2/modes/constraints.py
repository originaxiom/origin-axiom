from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Tuple

import numpy as np

# ============================================================
# Origin Axiom — Phase 2
# Constraint / enforcement primitives
#
# Phase-2 implementation of the Origin Axiom (OA) as a GLOBAL floor:
#
#   Given a complex global amplitude A (proxy for net cancellation),
#   enforce |A| >= epsilon.
#
# This is intentionally non-local: Phase 2 does not propose a microscopic
# local enforcement mechanism, only an interface-level global constraint.
#
# Determinism contract:
#   - If A != 0 and |A| < epsilon, the correction preserves the direction of A
#     and rescales magnitude to epsilon (fully deterministic).
#   - If A == 0, the direction is chosen using the provided RNG (seed-controlled).
# ============================================================
@dataclass(frozen=True)
class ConstraintActivity:
    """
    Record of whether OA enforcement was applied.

    direction_source:
      - "disabled": constraint was disabled (no enforcement).
      - "preserve_direction": A had a defined direction (A != 0), so we rescale.
      - "random_direction": A == 0, so we choose a seeded random direction.
    """
    applied: bool
    enabled: bool
    epsilon: float
    magnitude_before: float
    magnitude_after: float
    delta_magnitude: float
    direction_source: str


def _unit_complex_from_angle(theta: float) -> complex:
    return complex(math.cos(theta), math.sin(theta))


def enforce_global_floor(
    A: complex,
    *,
    epsilon: float,
    rng: np.random.Generator,
    enabled: bool = True,
) -> Tuple[complex, ConstraintActivity]:
    """
    Enforce a strict global floor |A| >= epsilon.

    Policy:
      - If |A| >= epsilon: return A unchanged.
      - If 0 < |A| < epsilon: rescale A to have magnitude epsilon, preserving direction.
      - If A == 0: set |A| = epsilon with a seeded random direction.

    Returns:
      (A_enforced, activity)
    """
    if epsilon <= 0.0 or not np.isfinite(epsilon):
        raise ValueError(f"epsilon must be positive finite, got {epsilon}")

    if not (np.isfinite(A.real) and np.isfinite(A.imag)):
        raise ValueError(f"Amplitude A must be finite, got {A!r}")

    mag = float(abs(A))

    enabled = bool(enabled)
    if not enabled:
        return A, ConstraintActivity(
            applied=False,
            enabled=False,
            epsilon=float(epsilon),
            magnitude_before=mag,
            magnitude_after=mag,
            delta_magnitude=0.0,
            direction_source="disabled",
        )

    # Case 1: already above floor
    if mag >= epsilon:
        return A, ConstraintActivity(
            applied=False,
            enabled=True,
            epsilon=float(epsilon),
            magnitude_before=mag,
            magnitude_after=mag,
            delta_magnitude=0.0,
            direction_source="preserve_direction",
        )

    # Case 2: below floor but direction exists => rescale deterministically
    if mag > 0.0:
        scale = epsilon / mag
        A2 = complex(A.real * scale, A.imag * scale)
        mag2 = float(abs(A2))

        # Numerical sanity: should be epsilon to floating tolerance
        if not np.isfinite(mag2):
            raise ValueError("Enforced amplitude magnitude became non-finite.")

        return A2, ConstraintActivity(
            applied=True,
            enabled=True,
            epsilon=float(epsilon),
            magnitude_before=mag,
            magnitude_after=mag2,
            delta_magnitude=float(mag2 - mag),
            direction_source="preserve_direction",
        )

    # Case 3: A == 0 => choose a seeded direction
    theta = float(rng.uniform(0.0, 2.0 * math.pi))
    A2 = float(epsilon) * _unit_complex_from_angle(theta)
    mag2 = float(abs(A2))

    return A2, ConstraintActivity(
        applied=True,
        enabled=True,
        epsilon=float(epsilon),
        magnitude_before=0.0,
        magnitude_after=mag2,
        delta_magnitude=mag2,
        direction_source="random_direction",
    )