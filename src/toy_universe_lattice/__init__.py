"""
Toy Universe lattice package.

Exports:
- CubicLattice3D
- ScalarToyUniverse
"""

from .lattice import CubicLattice3D
from .evolve_scalar import ScalarToyUniverse

__all__ = ["CubicLattice3D", "ScalarToyUniverse"]
