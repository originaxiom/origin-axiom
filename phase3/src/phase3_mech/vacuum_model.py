"""
Phase 3 mechanism: toy vacuum model and global amplitude observable.

This module defines a simple, deterministic "vacuum" ensemble and a global
amplitude observable A(theta) that depend on a single phase parameter theta.
At this rung we implement only the *unconstrained* amplitude; later rungs
will enforce the non-cancellation floor |A| >= eps_floor and define the
associated binding certificate.

The design goal is not physical realism but a clean, reproducible testbed
for the Origin Axiom non-cancellation mechanism.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np


@dataclass(frozen=True)
class VacuumConfig:
    """
    Configuration for the toy vacuum ensemble.

    Parameters
    ----------
    n_modes : int
        Number of complex modes in the ensemble.
    seed : int
        RNG seed that fixes the base phases and signs. This ensures that
        A(theta) is deterministic given (theta, config_id).
    """
    n_modes: int = 512
    seed: int = 20260106


def make_vacuum_config(config_id: str = "baseline_v1") -> VacuumConfig:
    """
    Return a named vacuum configuration.

    This indirection allows future rungs to introduce additional configs
    (e.g. different n_modes, different seeds) while keeping the paper and
    PROGRESS_LOG anchored to stable identifiers.
    """
    if config_id == "baseline_v1":
        return VacuumConfig(n_modes=512, seed=20260106)

    raise ValueError(f"Unknown vacuum config_id: {config_id!r}")


def _mode_parameters(cfg: VacuumConfig) -> Tuple[np.ndarray, np.ndarray]:
    """
    Internal helper: construct base phases and signs for all modes.

    The phases alpha_k and signs sigma_k are drawn once per call from a
    fixed-seed RNG, so that for a given cfg the pair (alphas, sigmas) is
    deterministic and reproducible.
    """
    rng = np.random.default_rng(cfg.seed)
    alphas = rng.uniform(0.0, 2.0 * np.pi, size=cfg.n_modes)
    sigmas = rng.choice([-1.0, +1.0], size=cfg.n_modes)
    return alphas, sigmas


def amplitude_unconstrained(theta: float, cfg: VacuumConfig) -> float:
    """
    Compute the unconstrained global amplitude A_0(theta) for a given config.

    We model the toy vacuum as an ensemble of complex phasors

        z_k(theta) = exp(i * (alpha_k + sigma_k * theta)),

    where alpha_k and sigma_k are fixed by the vacuum configuration.
    The global amplitude is the modulus of the ensemble mean,

        A_0(theta) = | (1 / N) * sum_k z_k(theta) |.

    Parameters
    ----------
    theta : float
        Phase parameter in radians.
    cfg : VacuumConfig
        Vacuum configuration (number of modes, RNG seed).

    Returns
    -------
    float
        The unconstrained global amplitude A_0(theta).
    """
    alphas, sigmas = _mode_parameters(cfg)
    phases = alphas + sigmas * theta
    z = np.exp(1j * phases)
    return float(np.abs(z.mean()))


def scan_amplitude_unconstrained(
    cfg: VacuumConfig,
    n_grid: int = 1024,
    theta_min: float = 0.0,
    theta_max: float = 2.0 * np.pi,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Evaluate A_0(theta) on a regular grid in [theta_min, theta_max).

    This helper is intentionally light-weight and is meant for small,
    diagnostic scans used in the paper figures and tables.

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
