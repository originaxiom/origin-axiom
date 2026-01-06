"""
Phase 3 mechanism package.

At this rung, we define a toy vacuum model and a global amplitude observable
A_0(theta) without yet enforcing the non-cancellation floor. Later rungs will
introduce the floor-enforced amplitude, binding certificates, and the
theta-filter artifact required by the Phase 0 contract.
"""

from .vacuum_model import (
    VacuumConfig,
    make_vacuum_config,
    amplitude_unconstrained,
    scan_amplitude_unconstrained,
)

__all__ = [
    "VacuumConfig",
    "make_vacuum_config",
    "amplitude_unconstrained",
    "scan_amplitude_unconstrained",
]
