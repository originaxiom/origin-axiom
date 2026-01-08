"""
Phase 3 mechanism package.

At this stage we define a toy vacuum model and two related observables:
- the unconstrained global amplitude A_0(theta);
- the floor-enforced amplitude A(theta) = max(A_0(theta), epsfloor),

plus simple grid scanners and binding diagnostics. Later rungs will tie
these objects into a theta-filter artifact and the Phase 0 ledger.
"""

from .vacuum_model import (
    VacuumConfig,
    make_vacuum_config,
    amplitude_unconstrained,
    scan_amplitude_unconstrained,
    amplitude_with_floor,
    scan_amplitude_with_floor,
)

__all__ = [
    "VacuumConfig",
    "make_vacuum_config",
    "amplitude_unconstrained",
    "scan_amplitude_unconstrained",
    "amplitude_with_floor",
    "scan_amplitude_with_floor",
]
