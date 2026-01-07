"""
Phase 4 package.

At this rung, Phase 4 provides:
  - a placeholder package namespace; and
  - the F1 mapping family, which maps the Phase 3 global amplitude
    into a toy vacuum-energy-like scalar.

Later rungs will:
  - add additional mapping families;
  - connect these scalars to FRW-like toy modules; and
  - construct theta-corridors or theta-filters where appropriate.
"""

from .mappings_f1 import (  # noqa: F401
    F1MappingConfig,
    build_default_f1_config,
    compute_f1_vacuum_curve,
)

__all__ = [
    "F1MappingConfig",
    "build_default_f1_config",
    "compute_f1_vacuum_curve",
]
