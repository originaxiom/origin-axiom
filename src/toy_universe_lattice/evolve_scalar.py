"""
Time evolution for the complex scalar field Φ on the cubic lattice.
Implements a simple discretized nonlinear Klein–Gordon-type equation:

  d2Φ/dt2 = c^2 ΔΦ - m^2 Φ - λ |Φ|^2 Φ

plus optional hooks for the Origin Axiom constraint.
"""

import numpy as np
from .lattice import CubicLattice3D

class ScalarToyUniverse:
    def __init__(self, nx, ny, nz, c=1.0, m=0.0, lam=0.0, dt=0.01):
        self.lat = CubicLattice3D(nx, ny, nz)
        self.c = c
        self.m = m
        self.lam = lam
        self.dt = dt

        # Fields
        self.phi = np.zeros(self.lat.shape, dtype=np.complex128)
        self.phi_dot = np.zeros_like(self.phi)

    def set_initial_conditions(self, phi0, phi_dot0=None):
        self.phi = np.array(phi0, dtype=np.complex128)
        if phi_dot0 is not None:
            self.phi_dot = np.array(phi_dot0, dtype=np.complex128)

    def global_amplitude(self):
        return self.phi.sum()

    def step(self, constraint=None):
        """
        Advance the field by one time step using a simple leapfrog scheme.

        constraint: optional callable constraint(self) -> None
          Can modify self.phi / self.phi_dot after free update
          to enforce the Origin Axiom constraint.
        """
        dt = self.dt
        lap = self.lat.laplacian(self.phi)
        accel = (
            self.c**2 * lap
            - self.m**2 * self.phi
            - self.lam * np.abs(self.phi)**2 * self.phi
        )

        # Leapfrog update
        self.phi_dot = self.phi_dot + accel * dt
        self.phi = self.phi + self.phi_dot * dt

        if constraint is not None:
            constraint(self)
