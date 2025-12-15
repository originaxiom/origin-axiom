"""
scan_1d_theta_star_microcavity_full_band.py

Goal
----
Scan the 1D θ★-sensitive microcavity toy over a full 0..2π range and
see how the vacuum energy shift ΔE(θ★) behaves, highlighting where
the Act II θ★ band sits in that landscape.

This builds on:
  - config/theta_star_config.json (Act II prior)
  - src/run_1d_theta_star_microcavity_scan.py (MicrocavityParams + energies)

Outputs:
  - Text summary of ΔE(θ★) behaviour and where its minimum lies.
  - NPZ file with the θ★ grid and ΔE(θ★):
        data/processed/theta_star_microcavity_scan_full_2pi.npz
  - PNG figure of ΔE vs θ★ with the Act II band highlighted:
        data/processed/figures/theta_star_microcavity_deltaE_full_2pi.png
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from theta_star_config import load_theta_star_config
from run_1d_theta_star_microcavity_scan import (
    MicrocavityParams,
    ground_state_energy_uniform,
    ground_state_energy,
)

TAU = 2.0 * np.pi


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
    # 2) Microcavity model parameters (same defaults as the scan script)
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

    # Baseline θ★-independent uniform energy
    E0_uniform = ground_state_energy_uniform(micro_cfg)
    print(f"E0_uniform (no cavity modulation) = {E0_uniform:.6e}")
    print()

    # ------------------------------------------------------------------
    # 3) Build a full 0..2π grid of θ★ values
    # ------------------------------------------------------------------
    n_theta = 256  # reasonably fine scan
    theta_grid = np.linspace(0.0, TAU, n_theta, endpoint=False)

    E0_cavity = np.empty_like(theta_grid)
    delta_E = np.empty_like(theta_grid)

    print("=== Scanning ΔE(θ★) over [0, 2π) ===")
    for i, th in enumerate(theta_grid):
        E_cav = ground_state_energy(th, micro_cfg)
        dE = E_cav - E0_uniform

        E0_cavity[i] = E_cav
        delta_E[i] = dE

    idx_min = int(np.argmin(delta_E))
    theta_min = float(theta_grid[idx_min])
    dE_min = float(delta_E[idx_min])

    print(f"  Global minimum ΔE(θ★) over [0, 2π):")
    print(f"    θ★_min   = {theta_min:.6f} rad")
    print(f"    ΔE_min   = {dE_min:.6e}")
    print()

    # Check how this compares with the Act II band
    print("=== Comparison with Act II θ★ band ===")
    # fraction of points whose θ★ lies inside the band
    mask_band = (theta_grid >= theta_lo) & (theta_grid <= theta_hi)
    if mask_band.any():
        dE_band = delta_E[mask_band]
        idx_band_min = int(np.argmin(dE_band))
        theta_band_grid = theta_grid[mask_band]
        theta_band_min = float(theta_band_grid[idx_band_min])
        dE_band_min = float(dE_band[idx_band_min])
        print(f"  Inside band [{theta_lo:.6f}, {theta_hi:.6f}] rad:")
        print(f"    θ★_band_min ≈ {theta_band_min:.6f} rad")
        print(f"    ΔE_band_min ≈ {dE_band_min:.6e}")
    else:
        print("  (No grid points happened to fall inside the band.)")
    print()

    # Evaluate ΔE at the exact fiducial θ★ too
    # (interpolating by computing a fresh value)
    dE_fid = ground_state_energy(theta_fid, micro_cfg) - E0_uniform
    print(f"  At fiducial θ★ = {theta_fid:.6f} rad:")
    print(f"    ΔE_fid = {dE_fid:.6e}")
    print()

    # ------------------------------------------------------------------
    # 4) Save NPZ data
    # ------------------------------------------------------------------
    out_dir = Path("data") / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_npz = out_dir / "theta_star_microcavity_scan_full_2pi.npz"

    np.savez(
        out_npz,
        theta_grid=theta_grid,
        E0_uniform=float(E0_uniform),
        E0_cavity=E0_cavity,
        delta_E=delta_E,
        theta_star_config={
            "theta_fid_rad": theta_fid,
            "theta_band_rad": (theta_lo, theta_hi),
        },
        micro_params=micro_cfg.__dict__,
    )

    print(f"Saved full 0..2π microcavity scan to {out_npz}")
    print()

    # ------------------------------------------------------------------
    # 5) Make a simple ΔE(θ★) figure with Act II band highlighted
    # ------------------------------------------------------------------
    fig_dir = Path("data") / "processed" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    fig_path = fig_dir / "theta_star_microcavity_deltaE_full_2pi.png"

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(theta_grid, delta_E, label=r"$\Delta E(\theta_\star)$")

    # highlight Act II band
    ax.axvspan(theta_lo, theta_hi, alpha=0.15, label="Act II θ★ band")
    ax.axvline(theta_fid, linestyle="--", label="θ★ fiducial")

    ax.set_xlabel(r"$\theta_\star$ [rad]")
    ax.set_ylabel(r"$\Delta E = E_{\mathrm{cav}} - E_{\mathrm{uniform}}$")
    ax.set_title("1D microcavity vacuum energy shift vs θ★")
    ax.legend(loc="best")

    fig.tight_layout()
    fig.savefig(fig_path, dpi=150)
    plt.close(fig)

    print(f"Saved figure to {fig_path}")
    print("Done.")


if __name__ == "__main__":
    main()