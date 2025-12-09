"""
Lattice definition for Toy Universe v0.1:
3D cubic lattice with periodic boundary conditions.
"""

import numpy as np

class CubicLattice3D:
    def __init__(self, nx, ny, nz):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.shape = (nx, ny, nz)

    def laplacian(self, field):
        """
        Discrete Laplacian with periodic boundary conditions.

        field: complex np.ndarray of shape (nx, ny, nz)
        """
        f = field
        lap = (
            np.roll(f, +1, axis=0) + np.roll(f, -1, axis=0) +
            np.roll(f, +1, axis=1) + np.roll(f, -1, axis=1) +
            np.roll(f, +1, axis=2) + np.roll(f, -1, axis=2) -
            6.0 * f
        )
        return lap
