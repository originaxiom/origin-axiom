from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any

import numpy as np


@dataclass
class TwoFieldCoupledParams:
    nx: int
    ny: int
    nz: int
    c: float = 1.0
    m_phi: float = 0.1
    m_chi: float = 0.1
    lam_phi: float = 1.0
    lam_chi: float = 1.0
    g: float = 0.0               # quartic coupling g φ^2 χ^2
    dt: float = 0.005
    n_steps: int = 500
    epsilon_psi: float = 0.05    # Origin Axiom band in ψ
    A_ref_psi: complex = 0.0 + 0.0j


class TwoFieldCoupledUniverse:
    """
    Two interacting complex scalar fields φ, χ on a 3D periodic lattice.

    Dynamics:
      d^2 φ/dt^2 = c^2 ∇^2 φ - ∂V/∂φ
      d^2 χ/dt^2 = c^2 ∇^2 χ - ∂V/∂χ

    Potential:
      V = 1/2 m_φ^2 |φ|^2 + 1/4 λ_φ |φ|^4
        + 1/2 m_χ^2 |χ|^2 + 1/4 λ_χ |χ|^4
        + g |φ|^2 |χ|^2

    Origin Axiom constraint acts on ψ = φ + χ via the global amplitude
    A_ψ = <ψ>, enforcing |A_ψ - A_ref_ψ| >= ε_ψ by uniform shifts.
    """

    def __init__(self, params: TwoFieldCoupledParams, use_constraint: bool) -> None:
        self.params = params
        self.use_constraint = bool(use_constraint)

        shape = (params.nx, params.ny, params.nz)

        # Fields and conjugate momenta (complex-valued)
        self.phi = np.zeros(shape, dtype=np.complex128)
        self.chi = np.zeros(shape, dtype=np.complex128)
        self.pi_phi = np.zeros(shape, dtype=np.complex128)
        self.pi_chi = np.zeros(shape, dtype=np.complex128)

        self.t = 0.0
        self.step_index = 0
        self.constraint_hits = 0

    # --- lattice helpers -----------------------------------------------------

    def _laplacian(self, field: np.ndarray) -> np.ndarray:
        """
        3D periodic Laplacian with lattice spacing a = 1:
        ∇^2 f = Σ_dir (f_{i+1} + f_{i-1} - 2 f_i)
        """
        lap = np.zeros_like(field)
        for axis in range(3):
            lap += np.roll(field, +1, axis=axis)
            lap += np.roll(field, -1, axis=axis)
            lap -= 2.0 * field
        return lap

    # --- initialization ------------------------------------------------------

    def set_initial_conditions(
        self,
        phi0: np.ndarray,
        chi0: np.ndarray,
        mean_subtract: bool = True,
    ) -> None:
        """
        Set initial φ, χ and reset momenta + counters.
        Optionally subtract spatial means so ψ starts near A_ref_ψ = 0.
        """
        phi_init = phi0.astype(np.complex128, copy=True)
        chi_init = chi0.astype(np.complex128, copy=True)

        if mean_subtract:
            phi_init -= np.mean(phi_init)
            chi_init -= np.mean(chi_init)

        self.phi[...] = phi_init
        self.chi[...] = chi_init
        self.pi_phi[...] = 0.0 + 0.0j
        self.pi_chi[...] = 0.0 + 0.0j

        self.t = 0.0
        self.step_index = 0
        self.constraint_hits = 0

    # --- Origin Axiom constraint on ψ ---------------------------------------

    def global_amplitude_psi(self) -> complex:
        psi = self.phi + self.chi
        return complex(np.mean(psi))

    def _project_psi_if_needed(self) -> None:
        """
        Enforce |A_ψ - A_ref_ψ| >= ε_ψ by adding a uniform complex shift δ
        to ψ, split equally between φ and χ:

          ψ -> ψ + δ,   φ -> φ + δ/2,   χ -> χ + δ/2

        This is a purely k=0 modification and keeps the constraint global.
        """
        if not self.use_constraint:
            return

        A_ref = self.params.A_ref_psi
        eps = self.params.epsilon_psi

        A = self.global_amplitude_psi()
        diff = A - A_ref
        dist = abs(diff)

        if dist >= eps:
            return

        if dist == 0.0:
            direction = 1.0 + 0.0j
        else:
            direction = diff / dist

        target = A_ref + eps * direction
        delta_A = target - A

        # Split evenly between φ and χ
        shift = 0.5 * delta_A
        self.phi += shift
        self.chi += shift

        self.constraint_hits += 1

    # --- forces and energy ---------------------------------------------------

    def _dV_dphi(self) -> np.ndarray:
        p = self.params
        abs_phi2 = np.abs(self.phi) ** 2
        abs_chi2 = np.abs(self.chi) ** 2

        # ∂V/∂φ = m_φ^2 φ + λ_φ |φ|^2 φ + g |χ|^2 φ
        return (
            p.m_phi**2 * self.phi
            + p.lam_phi * abs_phi2 * self.phi
            + p.g * abs_chi2 * self.phi
        )

    def _dV_dchi(self) -> np.ndarray:
        p = self.params
        abs_phi2 = np.abs(self.phi) ** 2
        abs_chi2 = np.abs(self.chi) ** 2

        # ∂V/∂χ = m_χ^2 χ + λ_χ |χ|^2 χ + g |φ|^2 χ
        return (
            p.m_chi**2 * self.chi
            + p.lam_chi * abs_chi2 * self.chi
            + p.g * abs_phi2 * self.chi
        )

    def energy_total(self) -> float:
        """
        Total lattice energy (sum over sites) with a = 1:

          E = ∫ d^3x [
                1/2 |π_φ|^2 + 1/2 |π_χ|^2
              + 1/2 c^2 (|∇φ|^2 + |∇χ|^2)
              + V(φ, χ)
              ]
        """
        p = self.params

        # kinetic
        kinetic = 0.5 * (np.abs(self.pi_phi) ** 2 + np.abs(self.pi_chi) ** 2)

        # gradient term: sum over forward differences |φ(x+ê) - φ(x)|^2
        grad_phi = np.zeros_like(self.phi, dtype=np.float64)
        grad_chi = np.zeros_like(self.chi, dtype=np.float64)
        for axis in range(3):
            dphi = np.roll(self.phi, -1, axis=axis) - self.phi
            dchi = np.roll(self.chi, -1, axis=axis) - self.chi
            grad_phi += np.abs(dphi) ** 2
            grad_chi += np.abs(dchi) ** 2

        grad_term = 0.5 * p.c**2 * (grad_phi + grad_chi)

        # potential
        abs_phi2 = np.abs(self.phi) ** 2
        abs_chi2 = np.abs(self.chi) ** 2
        V = (
            0.5 * p.m_phi**2 * abs_phi2
            + 0.25 * p.lam_phi * abs_phi2**2
            + 0.5 * p.m_chi**2 * abs_chi2
            + 0.25 * p.lam_chi * abs_chi2**2
            + p.g * abs_phi2 * abs_chi2
        )

        rho = kinetic + grad_term + V
        return float(np.sum(rho))

    # --- time stepping -------------------------------------------------------

    def step(self) -> None:
        """
        Single leapfrog-like step:

          π_{n+1} = π_n + dt (c^2 ∇^2 φ_n - ∂V/∂φ_n)
          φ_{n+1} = φ_n + dt π_{n+1}

        and similarly for χ, with constraint applied after the field update.
        """
        p = self.params
        dt = p.dt
        c2 = p.c**2

        # forces from lattice and potential
        lap_phi = self._laplacian(self.phi)
        lap_chi = self._laplacian(self.chi)

        dV_dphi = self._dV_dphi()
        dV_dchi = self._dV_dchi()

        # update momenta
        self.pi_phi += dt * (c2 * lap_phi - dV_dphi)
        self.pi_chi += dt * (c2 * lap_chi - dV_dchi)

        # update fields
        self.phi += dt * self.pi_phi
        self.chi += dt * self.pi_chi

        # global constraint on ψ
        self._project_psi_if_needed()

        self.step_index += 1
        self.t += dt

    # --- diagnostics ---------------------------------------------------------

    def diagnostics(self) -> Dict[str, Any]:
        return {
            "t": self.t,
            "step": self.step_index,
            "A_psi": self.global_amplitude_psi(),
            "E_total": self.energy_total(),
            "constraint_hits": self.constraint_hits,
            "params": self.params.__dict__.copy(),
            "use_constraint": self.use_constraint,
        }
