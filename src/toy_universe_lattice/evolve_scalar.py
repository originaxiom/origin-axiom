"""
Time evolution for the complex scalar field Φ on the cubic lattice.
Implements a simple discretized nonlinear Klein–Gordon-type equation:

  d2Φ/dt2 = c^2 ΔΦ - m^2 Φ - λ |Φ|^2 Φ

plus optional hooks for the Origin Axiom constraint, and an energy() method.
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

        # Diagnostics: how often a constraint is applied
        self.constraint_hits = 0

    def set_initial_conditions(self, phi0, phi_dot0=None):
        self.phi = np.array(phi0, dtype=np.complex128)
        if phi_dot0 is not None:
            self.phi_dot = np.array(phi_dot0, dtype=np.complex128)

    def global_amplitude(self):
        """Global complex amplitude A(t) = sum_n Φ_n."""
        return self.phi.sum()

    def energy(self):
        """
        Discrete energy functional:

        E = Σ_n [ 1/2 |dotΦ_n|^2
                 + c^2/2 Σ_neighbors |Φ_m - Φ_n|^2
                 + m^2/2 |Φ_n|^2
                 + λ/4 |Φ_n|^4 ]

        We use the identity Σ |∇Φ|^2 ~ - Φ* ΔΦ to avoid double-counting neighbor pairs.
        """
        # kinetic term
        kin = 0.5 * np.abs(self.phi_dot)**2

        # gradient term using Laplacian: Σ |∇Φ|^2 ≈ - Σ Φ* ΔΦ
        lap = self.lat.laplacian(self.phi)
        grad = -0.5 * (self.phi.conj() * lap).real * (self.c**2)

        # mass term
        mass = 0.5 * (self.m**2) * np.abs(self.phi)**2

        # self-interaction
        self_int = 0.25 * self.lam * np.abs(self.phi)**4

        E_density = kin + grad + mass + self_int
        return E_density.sum().real

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
