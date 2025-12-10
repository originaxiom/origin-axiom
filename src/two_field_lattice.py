from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Any

import numpy as np


@dataclass
class TwoFieldParams:
    # Lattice sizes
    nx: int = 16
    ny: int = 16
    nz: int = 16

    # Wave speed
    c: float = 1.0

    # Masses
    m_phi: float = 0.1
    m_chi: float = 0.1

    # Self-couplings
    lam_phi: float = 0.0
    lam_chi: float = 0.0

    # Cross-coupling between |phi|^2 and |chi|^2
    g: float = 0.0

    # Time step and number of steps
    dt: float = 0.01
    n_steps: int = 500

    # Origin Axiom parameters for the combined field psi = phi + chi
    epsilon: float = 0.05  # minimum allowed global amplitude radius
    A_ref: float = 0.0     # not used here, but kept for continuity

    # RNG and initial state options
    seed: int = 42
    mean_subtracted: bool = True


class TwoFieldToyUniverse:
    """
    Self-contained 3D lattice evolution for two complex scalar fields phi, chi
    with optional Origin-Axiom-style constraint on the combined field
        psi = phi + chi
    via the global amplitude A_psi = <psi> (spatial average).
    """

    def __init__(self, params: TwoFieldParams, use_constraint: bool = False) -> None:
        self.params = params
        self.use_constraint = use_constraint

        nx, ny, nz = params.nx, params.ny, params.nz
        shape = (nx, ny, nz)

        # Complex fields
        self.phi = np.zeros(shape, dtype=np.complex128)
        self.chi = np.zeros(shape, dtype=np.complex128)

        # Canonical momenta pi_phi, pi_chi
        self.pi_phi = np.zeros_like(self.phi)
        self.pi_chi = np.zeros_like(self.chi)

        # Time and constraint bookkeeping
        self.t: float = 0.0
        self.constraint_hits_psi: int = 0

    # ------------------------------------------------------------------
    # Initial conditions and helpers
    # ------------------------------------------------------------------

    def set_initial_conditions(self, phi0: np.ndarray, chi0: np.ndarray) -> None:
        """
        Set initial complex fields and reset momenta / time.
        """
        if phi0.shape != self.phi.shape or chi0.shape != self.chi.shape:
            raise ValueError(
                f"Initial condition shapes {phi0.shape}, {chi0.shape} "
                f"do not match lattice shape {self.phi.shape}"
            )

        self.phi[...] = phi0
        self.chi[...] = chi0

        if self.params.mean_subtracted:
            self.phi -= self.phi.mean()
            self.chi -= self.chi.mean()

        self.pi_phi[...] = 0.0
        self.pi_chi[...] = 0.0

        self.t = 0.0
        self.constraint_hits_psi = 0

    @staticmethod
    def _laplacian(f: np.ndarray) -> np.ndarray:
        """
        3D periodic Laplacian: sum of nearest neighbours minus 6*f.
        """
        return (
            np.roll(f, 1, axis=0)
            + np.roll(f, -1, axis=0)
            + np.roll(f, 1, axis=1)
            + np.roll(f, -1, axis=1)
            + np.roll(f, 1, axis=2)
            + np.roll(f, -1, axis=2)
            - 6.0 * f
        )

    # ------------------------------------------------------------------
    # Time evolution
    # ------------------------------------------------------------------

    def step(self) -> None:
        """
        One explicit Euler step for the coupled complex Klein-Gordon system:

            ∂_t^2 φ - c^2 ∇^2 φ + m_φ^2 φ + λ_φ |φ|^2 φ + g |χ|^2 φ = 0
            ∂_t^2 χ - c^2 ∇^2 χ + m_χ^2 χ + λ_χ |χ|^2 χ + g |φ|^2 χ = 0

        with π_φ = ∂_t φ, π_χ = ∂_t χ.
        """
        p = self.params
        dt = p.dt
        c2 = p.c ** 2

        # Spatial laplacians
        lap_phi = self._laplacian(self.phi)
        lap_chi = self._laplacian(self.chi)

        # Nonlinear forces
        abs_phi2 = np.abs(self.phi) ** 2
        abs_chi2 = np.abs(self.chi) ** 2

        force_phi = (
            c2 * lap_phi
            - (p.m_phi ** 2) * self.phi
            - p.lam_phi * abs_phi2 * self.phi
            - p.g * abs_chi2 * self.phi
        )

        force_chi = (
            c2 * lap_chi
            - (p.m_chi ** 2) * self.chi
            - p.lam_chi * abs_chi2 * self.chi
            - p.g * abs_phi2 * self.chi
        )

        # Update momenta
        self.pi_phi += dt * force_phi
        self.pi_chi += dt * force_chi

        # Update fields
        self.phi += dt * self.pi_phi
        self.chi += dt * self.pi_chi

        # Apply Origin Axiom constraint on psi = phi + chi, if requested
        if self.use_constraint:
            self._apply_psi_constraint()

        self.t += dt

    def _apply_psi_constraint(self) -> None:
        """
        Global constraint on the combined field psi = phi + chi:

        Let A_psi = <psi> (spatial average). If |A_psi| < epsilon, we shift psi
        uniformly so that |A_psi'| = epsilon, keeping the same phase when possible.

        We implement this shift by adding half of the uniform correction to phi
        and half to chi, so that psi = phi + chi gets shifted correctly.
        """
        p = self.params
        psi = self.phi + self.chi
        A_psi = psi.mean()

        r = np.abs(A_psi)
        if r >= p.epsilon:
            return  # constraint inactive

        if r == 0.0:
            # If phase is undefined, just pick phase 0
            phase = 0.0
        else:
            phase = np.angle(A_psi)

        A_target = p.epsilon * np.exp(1j * phase)
        delta = A_target - A_psi

        shift = 0.5 * delta
        self.phi += shift
        self.chi += shift

        self.constraint_hits_psi += 1

    # ------------------------------------------------------------------
    # Diagnostics
    # ------------------------------------------------------------------

    def global_amplitude_phi(self) -> complex:
        return self.phi.mean()

    def global_amplitude_chi(self) -> complex:
        return self.chi.mean()

    def global_amplitude_psi(self) -> complex:
        return (self.phi + self.chi).mean()

    def energy_density(self) -> np.ndarray:
        """
        Energy density for both fields (up to discretization conventions):

            e = 1/2 (|π_φ|^2 + |π_χ|^2)
                + 1/2 c^2 (|∇φ|^2 + |∇χ|^2)
                + 1/2 (m_φ^2 |φ|^2 + m_χ^2 |χ|^2)
                + 1/4 (λ_φ |φ|^4 + λ_χ |χ|^4)
                + 1/2 g |φ|^2 |χ|^2

        For |∇φ|^2 we use the identity (on a periodic lattice)
            |∇φ|^2 ≈ - Re( φ* ∇^2 φ )
        """
        p = self.params
        c2 = p.c ** 2

        lap_phi = self._laplacian(self.phi)
        lap_chi = self._laplacian(self.chi)

        grad_phi_sq = -np.real(np.conjugate(self.phi) * lap_phi)
        grad_chi_sq = -np.real(np.conjugate(self.chi) * lap_chi)

        abs_phi2 = np.abs(self.phi) ** 2
        abs_chi2 = np.abs(self.chi) ** 2

        e_kin = 0.5 * (np.abs(self.pi_phi) ** 2 + np.abs(self.pi_chi) ** 2)
        e_grad = 0.5 * c2 * (grad_phi_sq + grad_chi_sq)
        e_mass = 0.5 * ((p.m_phi ** 2) * abs_phi2 + (p.m_chi ** 2) * abs_chi2)
        e_self = 0.25 * (p.lam_phi * abs_phi2 ** 2 + p.lam_chi * abs_chi2 ** 2)
        e_cross = 0.5 * p.g * abs_phi2 * abs_chi2

        return e_kin + e_grad + e_mass + e_self + e_cross

    def total_energy(self) -> float:
        return float(self.energy_density().sum())

    def diagnostics(self) -> Dict[str, Any]:
        """
        One-shot diagnostics snapshot, convenient if you want it.
        """
        return {
            "t": self.t,
            "A_phi": self.global_amplitude_phi(),
            "A_chi": self.global_amplitude_chi(),
            "A_psi": self.global_amplitude_psi(),
            "E": self.total_energy(),
            "constraint_hits_psi": self.constraint_hits_psi,
            "params": asdict(self.params),
            "use_constraint": self.use_constraint,
        }
