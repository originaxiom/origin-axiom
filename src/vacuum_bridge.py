"""
vacuum_bridge.py

Utilities to translate dimensionless lattice vacuum energy shifts ΔE(θ★)
into a physical vacuum energy density ρ_Λ and an effective Ω_Λ,
given explicit choices of length and energy scales.

This is intentionally simple and explicit:
  - We assume one "cell" of volume V0 = L0^3.
  - ΔE_dimless is interpreted as a total energy shift per cell in code units.
  - energy_unit_eV sets the physical energy per code unit.
  - We work in SI and compare to the critical density ρ_c from H0.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

# Physical constants (CODATA-ish, enough for order-of-magnitude work)
C_LIGHT = 2.99792458e8            # m/s
ELECTRON_VOLT_J = 1.602176634e-19 # J
G_NEWTON = 6.67430e-11            # m^3 / (kg s^2)
KM = 1.0e3                        # m
MPC = 3.0856775814913673e22       # m


@dataclass
class VacuumScaling:
    """
    Choice of microphysical scales for a single effective "cell".

    length_unit_m:
        L0 = physical linear size of one cell (meters).
        We take the cell volume as V0 = L0^3.

    energy_unit_eV:
        E0 = physical energy per code energy unit (in eV).
        If the lattice ΔE is dimensionless, the physical energy shift is
        |ΔE| * E0 (converted to Joules).
    """
    length_unit_m: float
    energy_unit_eV: float

    def cell_volume_m3(self) -> float:
        return self.length_unit_m ** 3

    def energy_unit_J(self) -> float:
        return self.energy_unit_eV * ELECTRON_VOLT_J


def lattice_deltaE_to_rho_lambda(deltaE_dimless: float,
                                 scaling: VacuumScaling) -> Tuple[float, float]:
    """
    Map a dimensionless ΔE from the microcavity model to:

      - rho_E: vacuum energy density ρ_Λ in J/m^3
      - rho_m: effective mass density ρ_Λ, mass in kg/m^3

    Given a choice of L0 and E0 in `scaling`.

    We interpret ΔE_dimless as the *total* energy shift per cell in code units.
    The sign of ΔE is kept, but for energy density magnitude we usually care
    about |ΔE|.
    """
    # Total physical energy shift per cell
    E_phys_J = deltaE_dimless * scaling.energy_unit_J()

    # Cell volume
    V0 = scaling.cell_volume_m3()
    if V0 <= 0.0:
        raise ValueError("Cell volume must be positive.")

    # Energy density (can be negative if ΔE_dimless < 0)
    rho_E = E_phys_J / V0  # J/m^3

    # Convert to mass density via E = rho_m * c^2 * V
    rho_m = rho_E / (C_LIGHT ** 2)  # kg/m^3

    return rho_E, rho_m


def critical_density_kg_m3(H0_km_s_Mpc: float) -> float:
    """
    Critical density ρ_c = 3 H0^2 / (8π G) in kg/m^3,
    for a given H0 in km/s/Mpc.
    """
    import math

    # Convert H0 to s^-1
    H0_SI = (H0_km_s_Mpc * KM) / MPC  # (km/s)/Mpc -> s^-1

    rho_c = 3.0 * H0_SI ** 2 / (8.0 * math.pi * G_NEWTON)
    return rho_c


def rho_to_omega_lambda(rho_lambda_mass_kg_m3: float,
                        H0_km_s_Mpc: float = 70.0) -> float:
    """
    Convert a vacuum mass density ρ_Λ (kg/m^3) to Ω_Λ
    using ρ_c computed from H0.
    """
    rho_c = critical_density_kg_m3(H0_km_s_Mpc)
    if rho_c <= 0.0:
        raise ValueError("Critical density must be positive.")
    return rho_lambda_mass_kg_m3 / rho_c


def describe_scaling(scaling: VacuumScaling) -> str:
    """
    Convenience helper: short text description of a scaling choice.
    """
    return (f"L0 = {scaling.length_unit_m:.3e} m, "
            f"E0 = {scaling.energy_unit_eV:.3e} eV, "
            f"V0 = {scaling.cell_volume_m3():.3e} m^3")