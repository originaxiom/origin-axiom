"""
Toy vacuum model for Phase 3 mechanism work.

At this rung we define:
- a deterministic ensemble of complex modes for a "vacuum" toy model;
- an unconstrained global amplitude observable A_0(theta);
- a floor-enforced amplitude A(theta) = max(A_0(theta), epsfloor);
- simple binding diagnostics that quantify how often the floor is active.

No attempt is made here to connect this toy model directly to observed
vacuum energy or other data; the purpose is to have a clean, reusable
mechanism on which later phases and rungs can operate.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, Dict

import numpy as np


@dataclass(frozen=True)
class VacuumConfig:
    """
    Configuration for the toy vacuum ensemble.

    Attributes
    ----------
    alphas : np.ndarray
        Phase offsets for each mode.
    sigmas : np.ndarray
        Integer "winding numbers" that control how each mode responds to theta.
    """
    alphas: np.ndarray
    sigmas: np.ndarray


def make_vacuum_config(name: str = "baseline_v1") -> VacuumConfig:
    """
    Construct a named vacuum configuration.

    The current rung defines a single baseline configuration "baseline_v1".
    It is deterministic (fixed RNG seed) so that runs are reproducible.
    """
    if name != "baseline_v1":
        raise ValueError(f"Unknown vacuum configuration name: {name!r}")

    rng = np.random.default_rng(123456)
    n_modes = 256

    # Random initial phases in [0, 2pi)
    alphas = rng.uniform(0.0, 2.0 * np.pi, size=n_modes)

    # Small positive integers that control how each mode winds with theta.
    sigmas = rng.integers(1, 5, size=n_modes)

    return VacuumConfig(alphas=alphas, sigmas=sigmas)


def _mode_parameters(cfg: VacuumConfig) -> Tuple[np.ndarray, np.ndarray]:
    """Internal helper to unpack mode parameters."""
    return cfg.alphas, cfg.sigmas


def amplitude_unconstrained(theta: float, cfg: VacuumConfig) -> float:
    """
    Compute the unconstrained global amplitude A_0(theta).

    Parameters
    ----------
    theta : float
        Phase parameter.
    cfg : VacuumConfig
        Vacuum configuration.

    Returns
    -------
    float
        |A_0(theta)|, the modulus of the ensemble average.
    """
    alphas, sigmas = _mode_parameters(cfg)
    phases = alphas + sigmas * theta
    z = np.exp(1j * phases)
    return float(np.abs(z.mean()))


def scan_amplitude_unconstrained(
    cfg: VacuumConfig,
    n_grid: int,
    theta_min: float = 0.0,
    theta_max: float = 2.0 * np.pi,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Scan A_0(theta) on a regular grid.

    Parameters
    ----------
    cfg : VacuumConfig
        Vacuum configuration.
    n_grid : int
        Number of grid points.
    theta_min : float
        Lower bound of the theta range (inclusive).
    theta_max : float
        Upper bound of the theta range (exclusive).

    Returns
    -------
    thetas : np.ndarray
        1D array of theta values.
    amps : np.ndarray
        1D array of unconstrained amplitudes A_0(theta).
    """
    thetas = np.linspace(theta_min, theta_max, num=n_grid, endpoint=False)
    alphas, sigmas = _mode_parameters(cfg)
    phases = alphas[None, :] + sigmas[None, :] * thetas[:, None]
    z = np.exp(1j * phases)
    amps = np.abs(z.mean(axis=1))
    return thetas, amps


def amplitude_with_floor(theta: float, cfg: VacuumConfig, epsfloor: float) -> float:
    """
    Floor-enforced amplitude A(theta) = max(A_0(theta), epsfloor).

    This is the analytical expression of the non-cancellation principle
    at the toy level: the global amplitude cannot cross below epsfloor.
    """
    base = amplitude_unconstrained(theta, cfg)
    return float(max(base, epsfloor))


def scan_amplitude_with_floor(
    cfg: VacuumConfig,
    epsfloor: float,
    n_grid: int,
    theta_min: float = 0.0,
    theta_max: float = 2.0 * np.pi,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, float]]:
    """
    Scan both A_0(theta) and the floor-enforced A(theta) on a grid.

    Returns arrays plus a small "binding diagnostics" dictionary that
    quantifies how often the floor is active.

    Parameters
    ----------
    cfg : VacuumConfig
        Vacuum configuration.
    epsfloor : float
        Non-cancellation floor (must be > 0).
    n_grid : int
        Number of grid points.
    theta_min : float
        Lower bound of the theta range (inclusive).
    theta_max : float
        Upper bound of the theta range (exclusive).

    Returns
    -------
    thetas : np.ndarray
        Grid of theta values.
    amps0 : np.ndarray
        Unconstrained amplitudes A_0(theta).
    amps_floor : np.ndarray
        Floor-enforced amplitudes A(theta).
    binds : np.ndarray
        Boolean mask where the floor is active (A_0 < epsfloor).
    diagnostics : dict
        Summary statistics useful for a binding certificate, including:
        - epsfloor
        - min_unconstrained
        - max_unconstrained
        - frac_bound (fraction of grid points where the floor is active)
    """
    if epsfloor <= 0.0:
        raise ValueError(f"epsfloor must be > 0, got {epsfloor}")

    thetas, amps0 = scan_amplitude_unconstrained(
        cfg, n_grid=n_grid, theta_min=theta_min, theta_max=theta_max
    )
    amps_floor = np.maximum(amps0, epsfloor)
    binds = amps0 < epsfloor

    diagnostics = {
        "epsfloor": float(epsfloor),
        "min_unconstrained": float(amps0.min()),
        "max_unconstrained": float(amps0.max()),
        "frac_bound": float(binds.mean()),
    }

    return thetas, amps0, amps_floor, binds, diagnostics
