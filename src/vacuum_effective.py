"""
vacuum_effective.py

Thin "effective vacuum" wrapper.

Goal
----
Provide a small, explicit place where we turn:
  - an Act II theta_star (\u03B8\u2605) prior, and
  - a microcavity scan \u0394E(theta_star)
into a function that returns an effective cosmological constant
fraction Omega_Lambda(theta_star), suitable for FRW toy runs.

This is still a toy mapping:
  Omega_Lambda(theta_star) = k_scale * delta_E(theta_star),
clamped to [0, 0.999], with k_scale chosen so that at the
fiducial theta_star we recover a chosen Omega_Lambda,fid
(default 0.7 in this script).

Dependencies
------------
- config/theta_star_config.json      (created in Act II)
- data/processed/theta_star_microcavity_scan_full_2pi.npz
  with keys:
    "theta_grid"   : 1D array of theta_star samples
    "E0_uniform"   : vacuum energy with no cavity
    "E0_cavity"    : vacuum energy with cavity
    "delta_E"      : E0_cavity - E0_uniform  (same as before)
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

from theta_star_config import load_theta_star_config


@dataclass
class ThetaStarPrior:
    """Minimal view of the Act II theta_star (\u03B8\u2605) configuration."""
    theta_fid_rad: float
    theta_band_rad: Tuple[float, float]


@dataclass
class MicrocavityScan:
    """
    Microcavity \u0394E(theta_star) scan.

    Attributes
    ----------
    theta_grid:
        1D array of theta_star values in radians, typically covering [0, 2*pi).
    delta_E:
        1D array of E_cavity(theta_star) - E_uniform(theta_star).
    E0_uniform:
        Reference uniform-vacuum energy (usually constant across theta_star).
    E0_cavity:
        Cavity-modulated vacuum energy.
    extra:
        Any additional metadata stored in the npz file (kept for reference).
    """
    theta_grid: np.ndarray
    delta_E: np.ndarray
    E0_uniform: np.ndarray
    E0_cavity: np.ndarray
    extra: Dict[str, object]


@dataclass
class EffectiveVacuumConfig:
    """
    Configuration for the effective vacuum mapping.

    Attributes
    ----------
    theta_prior:
        Act II theta_star prior (fiducial and band).
    omega_lambda_fid:
        Target Omega_Lambda at the fiducial theta_star.
    k_scale:
        Scaling factor such that:
          Omega_Lambda(theta_fid) = k_scale * delta_E(theta_fid)
        (before clamping to [0, 0.999]).
    """
    theta_prior: ThetaStarPrior
    omega_lambda_fid: float
    k_scale: float


@dataclass
class EffectiveVacuumModel:
    """
    Effective vacuum model backed by a microcavity \u0394E(theta_star) scan.

    This is the main object that other scripts should talk to when they
    want an "Omega_Lambda(theta_star)" coming from microstructure.
    """
    cfg: EffectiveVacuumConfig
    theta_grid: np.ndarray
    delta_E: np.ndarray

    def _nearest_index(self, theta_rad: float) -> int:
        """
        Map a theta_star (radians) to the nearest grid index, with
        periodic wrapping to [0, 2*pi).
        """
        theta = float(theta_rad)
        two_pi = 2.0 * np.pi
        theta_wrapped = theta % two_pi
        idx = int(np.argmin(np.abs(self.theta_grid - theta_wrapped)))
        return idx

    def omega_lambda_of_theta(self, theta_rad: float) -> float:
        """
        Return Omega_Lambda(theta_star) for the given theta_star (radians).

        Mapping:
            raw = k_scale * delta_E(theta_star)
            Omega_Lambda = clamp(raw, 0.0, 0.999)
        """
        idx = self._nearest_index(theta_rad)
        dE = float(self.delta_E[idx])
        raw = self.cfg.k_scale * dE

        # Clamp to a reasonable flat-universe range
        if raw < 0.0:
            raw = 0.0
        if raw > 0.999:
            raw = 0.999
        return raw

    def omega_m_of_theta(self, theta_rad: float) -> float:
        """
        Flat-universe complement:
            Omega_m(theta_star) = 1 - Omega_Lambda(theta_star).
        """
        omega_lambda = self.omega_lambda_of_theta(theta_rad)
        return 1.0 - omega_lambda

    def summary(self) -> str:
        """Return a short human-readable summary."""
        tp = self.cfg.theta_prior
        lines = [
            "EffectiveVacuumModel:",
            f"  theta_fid_rad        = {tp.theta_fid_rad:.6f}",
            f"  theta_band_rad       = [{tp.theta_band_rad[0]:.6f}, {tp.theta_band_rad[1]:.6f}]",
            f"  omega_lambda_fid     = {self.cfg.omega_lambda_fid:.3f}",
            f"  k_scale              = {self.cfg.k_scale:.6e}",
            f"  n_theta_grid         = {self.theta_grid.shape[0]}",
        ]
        return "\n".join(lines)


def load_theta_star_prior_from_config() -> ThetaStarPrior:
    """
    Load the Act II theta_star (\u03B8\u2605) prior from config/theta_star_config.json.
    """
    cfg = load_theta_star_config()
    theta_fid = float(cfg.theta_star_fid_rad)
    band = cfg.theta_star_band_rad
    if not (isinstance(band, (list, tuple)) and len(band) == 2):
        raise ValueError("theta_star_band_rad in config must be a 2-element list/tuple.")
    theta_band = (float(band[0]), float(band[1]))
    return ThetaStarPrior(theta_fid_rad=theta_fid, theta_band_rad=theta_band)


def load_microcavity_scan(
    path: str | Path = "data/processed/theta_star_microcavity_scan_full_2pi.npz",
) -> MicrocavityScan:
    """
    Load the microcavity \u0394E(theta_star) scan used in Act II.

    The file is expected to contain at least:
      - "theta_grid"
      - "delta_E"
      - "E0_uniform"
      - "E0_cavity"

    Any other keys are collected into the "extra" dict.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Microcavity scan file not found at {p}. "
            "You may need to re-run src/scan_1d_theta_star_microcavity_full_band.py."
        )

    data = np.load(p, allow_pickle=True)
    keys = set(data.files)

    required = {"theta_grid", "delta_E", "E0_uniform", "E0_cavity"}
    missing = required - keys
    if missing:
        raise KeyError(
            f"Missing keys {sorted(missing)} in {p}. "
            f"Available keys: {sorted(keys)}"
        )

    theta_grid = data["theta_grid"]
    delta_E = data["delta_E"]
    E0_uniform = data["E0_uniform"]
    E0_cavity = data["E0_cavity"]

    extra_keys = keys - required
    extra: Dict[str, object] = {}
    for k in extra_keys:
        extra[k] = data[k]

    return MicrocavityScan(
        theta_grid=theta_grid,
        delta_E=delta_E,
        E0_uniform=E0_uniform,
        E0_cavity=E0_cavity,
        extra=extra,
    )


def build_effective_vacuum_from_microcavity(
    microcavity_path: str | Path = "data/processed/theta_star_microcavity_scan_full_2pi.npz",
    omega_lambda_fid: float = 0.7,
) -> EffectiveVacuumModel:
    """
    Construct an EffectiveVacuumModel from the Act II theta_star prior
    and the microcavity \u0394E(theta_star) scan.

    Scaling rule:
      - Find the grid point closest to theta_fid_rad.
      - Read delta_E(theta_fid).
      - Set k_scale so that:
            Omega_Lambda(theta_fid) = omega_lambda_fid
        i.e. k_scale = omega_lambda_fid / delta_E(theta_fid).

    Notes
    -----
    In the current microcavity scans, delta_E(theta_fid) is negative,
    so k_scale is negative. The mapping Omega_Lambda(theta_star) =
    k_scale * delta_E(theta_star) is then clamped to [0, 0.999].
    """
    theta_prior = load_theta_star_prior_from_config()
    scan = load_microcavity_scan(microcavity_path)

    theta_fid = theta_prior.theta_fid_rad
    idx_fid = int(np.argmin(np.abs(scan.theta_grid - theta_fid)))
    delta_E_fid = float(scan.delta_E[idx_fid])

    if delta_E_fid == 0.0:
        raise ValueError(
            "delta_E at the fiducial theta_star is zero; cannot construct scaling. "
            "Check the microcavity scan or choose a different fiducial point."
        )

    k_scale = omega_lambda_fid / delta_E_fid

    cfg = EffectiveVacuumConfig(
        theta_prior=theta_prior,
        omega_lambda_fid=float(omega_lambda_fid),
        k_scale=float(k_scale),
    )

    return EffectiveVacuumModel(
        cfg=cfg,
        theta_grid=np.array(scan.theta_grid, dtype=float),
        delta_E=np.array(scan.delta_E, dtype=float),
    )


if __name__ == "__main__":
    # Small CLI preview, useful for sanity checks:
    model = build_effective_vacuum_from_microcavity()
    print(model.summary())
    tp = model.cfg.theta_prior
    for label, theta in [
        ("fiducial", tp.theta_fid_rad),
        ("band_lo", tp.theta_band_rad[0]),
        ("band_hi", tp.theta_band_rad[1]),
    ]:
        omega_L = model.omega_lambda_of_theta(theta)
        omega_m = model.omega_m_of_theta(theta)
        print(
            f"[{label}] theta_star = {theta:.6f} rad -> "
            f"Omega_Lambda = {omega_L:.3f}, Omega_m = {omega_m:.3f}"
        )