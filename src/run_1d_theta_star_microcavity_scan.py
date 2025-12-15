"""
run_1d_theta_star_microcavity_scan.py

Goal
----
Minimal 1D toy showing how a *single* master phase θ★ can
modulate a piece of vacuum microstructure, using the Act II
theta★ prior as input.

We do NOT try to be fully realistic here. This is a didactic
block:

  - θ★ is taken from config/theta_star_config.json
    (wired in from origin-axiom-theta-star).
  - We build a simple 1D scalar chain with nearest-neighbour
    coupling and a "micro-cavity" region (a contiguous band of
    sites) whose mass term is modulated by cos(θ★ - θ0).
  - We compare the ground-state energy with and without that
    θ★-dependent cavity for a small set of θ★ samples inside the
    Act II prior band.

This is our first explicit toy where:

    same θ★ that flavours the PMNS sector
    ↳ directly modulates a microscopic scalar structure.

The purpose is intuition + a clean bridge, not precision physics.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import numpy as np

from theta_star_config import load_theta_star_config


@dataclass
class MicrocavityParams:
    """
    Parameters for the 1D microcavity toy.
    """
    N: int = 256           # number of lattice sites
    c: float = 1.0         # nearest-neighbour coupling
    m0: float = 0.1        # baseline mass
    cavity_frac: float = 0.2   # fraction of the chain occupied by the cavity
    alpha_mass: float = 0.5    # strength of θ★-dependent mass modulation
    theta0: float = 0.0        # reference phase for the cosine


def build_mass_profile(
    theta_star: float,
    cfg: MicrocavityParams,
) -> np.ndarray:
    """
    Build the site-dependent mass profile m(x; θ★).

    We keep it very simple:
      - Outside the cavity band: m(x) = m0.
      - Inside the cavity band:  m(x) = m0 * (1 + alpha_mass * cos(θ★ - θ0)).

    So θ★ controls how "heavy" or "light" the cavity region is,
    relative to the rest of the chain.
    """
    N = cfg.N
    m = np.full(N, cfg.m0, dtype=float)

    # define cavity region as a central block
    width = int(round(cfg.cavity_frac * N))
    width = max(1, min(N, width))
    start = (N - width) // 2
    stop = start + width

    # θ★-dependent factor inside the cavity
    scale = 1.0 + cfg.alpha_mass * np.cos(theta_star - cfg.theta0)
    m[start:stop] = cfg.m0 * scale

    return m


def build_hamiltonian(
    theta_star: float,
    cfg: MicrocavityParams,
) -> np.ndarray:
    """
    Build a very simple 1D scalar "Hamiltonian" matrix H(θ★):

      H = diag(m(x; θ★)^2 + 2c) - c * (off-diagonal nearest neighbours)

    We use *open* boundary conditions here for simplicity. The θ★
    dependence enters only through the mass profile; this is not
    the same twisted-bc model as in run_1d_twisted_vacuum_scan.py.
    """
    N = cfg.N
    c = cfg.c

    m = build_mass_profile(theta_star, cfg)
    diag = m**2 + 2.0 * c

    H = np.zeros((N, N), dtype=float)
    np.fill_diagonal(H, diag)

    # nearest-neighbour couplings
    for i in range(N - 1):
        H[i, i + 1] = -c
        H[i + 1, i] = -c

    return H


def ground_state_energy(theta_star: float, cfg: MicrocavityParams) -> float:
    """
    Compute the ground-state energy (smallest eigenvalue) of H(θ★).
    """
    H = build_hamiltonian(theta_star, cfg)
    eigvals = np.linalg.eigvalsh(H)
    return float(eigvals[0])


def ground_state_energy_uniform(cfg: MicrocavityParams) -> float:
    """
    Baseline ground-state energy with NO θ★-dependent cavity:
    just m(x) = m0 everywhere.
    """
    N = cfg.N
    c = cfg.c
    m0 = cfg.m0

    diag = m0**2 + 2.0 * c
    H = np.zeros((N, N), dtype=float)
    np.fill_diagonal(H, diag)

    for i in range(N - 1):
        H[i, i + 1] = -c
        H[i + 1, i] = -c

    eigvals = np.linalg.eigvalsh(H)
    return float(eigvals[0])


def main() -> None:
    # ------------------------------------------------------------------
    # 1) Load Act II theta★ configuration
    # ------------------------------------------------------------------
    cfg_theta = load_theta_star_config()

    theta_fid = cfg_theta.theta_star_fid_rad
    theta_lo, theta_hi = cfg_theta.theta_star_band_rad

    print("=== θ★ prior from Act II (config/theta_star_config.json) ===")
    print(f"  fiducial θ★  = {theta_fid:.6f} rad")
    print(f"  band θ★      = [{theta_lo:.6f}, {theta_hi:.6f}] rad")
    print()

    # ------------------------------------------------------------------
    # 2) Microcavity model parameters
    # ------------------------------------------------------------------
    micro_cfg = MicrocavityParams()
    print("=== 1D microcavity model parameters ===")
    print(f"  N               = {micro_cfg.N}")
    print(f"  c               = {micro_cfg.c}")
    print(f"  m0              = {micro_cfg.m0}")
    print(f"  cavity_frac     = {micro_cfg.cavity_frac}")
    print(f"  alpha_mass      = {micro_cfg.alpha_mass}")
    print(f"  theta0          = {micro_cfg.theta0}")
    print()

    # ------------------------------------------------------------------
    # 3) θ★ samples inside the Act II band
    # ------------------------------------------------------------------
    # For now, just a small fixed set spanning the band plus the fiducial.
    theta_samples = np.linspace(theta_lo, theta_hi, 5)
    # make sure θ★_fid is represented exactly once if it lies in the band
    if theta_lo <= theta_fid <= theta_hi:
        # replace the central sample by the fiducial
        mid_idx = len(theta_samples) // 2
        theta_samples[mid_idx] = theta_fid

    # Baseline (θ★-independent) uniform energy
    E0_uniform = ground_state_energy_uniform(micro_cfg)

    # ------------------------------------------------------------------
    # 4) Scan θ★ and compute cavity ground-state energies
    # ------------------------------------------------------------------
    E0_cavity = []
    dE = []

    print("=== θ★ samples and microcavity vacuum energies ===")
    print("  idx  θ★ [rad]    E0_uniform       E0_cavity        ΔE = E_cav - E_uni")
    for i, th in enumerate(theta_samples):
        E_cav = ground_state_energy(th, micro_cfg)
        delta = E_cav - E0_uniform
        E0_cavity.append(E_cav)
        dE.append(delta)
        print(f"{i:5d}  {th:8.4f}  {E0_uniform:13.6e}  {E_cav:13.6e}  {delta:13.6e}")

    E0_cavity = np.array(E0_cavity, dtype=float)
    dE = np.array(dE, dtype=float)

    # ------------------------------------------------------------------
    # 5) Save to data/processed for later plotting / analysis
    # ------------------------------------------------------------------
    out_dir = Path("data") / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "theta_star_prior_1d_microcavity_samples.npz"

    np.savez(
        out_path,
        theta_samples=np.array(theta_samples, dtype=float),
        E0_uniform=float(E0_uniform),
        E0_cavity=E0_cavity,
        dE=dE,
        micro_params=micro_cfg.__dict__,
        theta_config={
            "theta_fid_rad": theta_fid,
            "theta_band_rad": (theta_lo, theta_hi),
        },
    )

    print()
    print(f"Saved θ★-prior microcavity samples to {out_path}")
    print("You can inspect it later with, e.g.:")
    print(
        '  PYTHONPATH=src python3 -c \'import numpy as np; '
        'd = np.load("data/processed/theta_star_prior_1d_microcavity_samples.npz", '
        'allow_pickle=True); '
        'print(d.files); print(d["theta_samples"])\''
    )


if __name__ == "__main__":
    main()