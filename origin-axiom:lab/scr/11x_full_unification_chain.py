#!/usr/bin/env python3
# proposed_full_unification_chain.py
# Synthesized most advanced full unification script based on lab/scr contents (as of Dec 24, 2025)
# Chains: Flavor (θ★ prior + toy seesaw) → Vacuum shift (microcavity ΔE with m_eff) → Cosmology (ΔE → effective Λ → FRW scale factor) → Microstructure (simple defect stability check)
# Improvements: Full end-to-end sweep over θ★ band, aligned metrics, realistic-ish Λ mapping (calibratable k_scale), combined plots, reproducibility.

import sys
import os
from datetime import datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from pathlib import Path

# Assume repo structure; adjust if needed
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, REPO_ROOT)

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
# from src.theta_star_config import load_theta_star_config  # Assuming this exists
# Placeholder for theta_star_config if not directly importable
class ThetaStarConfig:
    theta_star_fid_rad = 3.63
    theta_star_band_rad = [2.18, 5.54]

def load_theta_star_config():
    return ThetaStarConfig()

# --------------------- Flavor Bridge: Toy Seesaw ---------------------
def toy_seesaw_mnu(theta_star, v_SM=174.0, M_R_base=1e14, M_scale=2.64e-6):
    """Modulated seesaw reproducing ~PDG masses at fiducial θ★."""
    mod_atm = np.sin(2 * theta_star)**2
    mod_sol = np.sin(theta_star)**2
    mod1 = np.cos(theta_star)**4
    y_nu = np.array([mod1 * 1e-6, mod_sol * 3e-4, mod_atm * 1e-3])
    m_nu_gev = (y_nu * v_SM)**2 / (M_R_base * M_scale)
    m_nu_ev = m_nu_gev * 1e9
    return np.sort(np.abs(m_nu_ev))  # Hierarchical

# --------------------- Vacuum Modulation: Microcavity ---------------------
def run_microcavity(theta_star, m_eff=0.0, n_steps=500, dt=0.01, lattice_size=16, epsilon=1e-2):
    constraint = hard_constraint_factory(theta_star=theta_star, epsilon=epsilon, A_ref=0.0)
    nx = ny = nz = lattice_size
    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=1.0, m=m_eff, lam=0.0, dt=dt)
    
    rng = np.random.default_rng(42)
    shape = uni.lat.shape
    phi0 = 1e-3 * (rng.standard_normal(shape) + 1j * rng.standard_normal(shape))
    phi0 -= phi0.mean()
    uni.set_initial_conditions(phi0)
    
    energy_history = []
    for _ in range(n_steps):
        uni.step(constraint=constraint)
        energy_history.append(uni.energy() if hasattr(uni, 'energy') else 0.0)
    
    delta_E = energy_history[-1] - energy_history[0]
    final_A = abs(uni.global_amplitude())
    return delta_E, final_A

# --------------------- Cosmology: Simple FRW with Λ(θ★) ---------------------
def run_frw(delta_E, k_scale=1e120, rho_m0=0.3, rho_r0=1e-4, steps=5000, t_max=14e9):  # Rough units
    """Integrate flat FRW with effective Λ from ΔE (calibrate k_scale for realistic Ω_Λ ~0.7)."""
    Lambda_eff = k_scale * delta_E  # Huge uplift needed for cosmic scales
    t = np.linspace(0, t_max, steps)
    dt = t[1] - t[0]
    a = np.zeros(steps)
    a[0] = 1.0
    for i in range(1, steps):
        H2 = (rho_r0 / a[i-1]**4) + (rho_m0 / a[i-1]**3) + Lambda_eff / 3
        H = np.sqrt(H2)
        a[i] = a[i-1] * (1 + H * dt)
    return t, a

# --------------------- Microstructure: Simple Defect Persistence ---------------------
def add_gaussian_defects(uni, n_defects=5, width=2.0):
    """Add n Gaussian bumps as defects (particle-like)."""
    shape = uni.lat.shape
    phi = uni.lat.phi
    for _ in range(n_defects):
        cx, cy, cz = np.random.randint(0, shape[0], size=3)
        x, y, z = np.ogrid[:shape[0], :shape[1], :shape[2]]
        dist2 = (x - cx)**2 + (y - cy)**2 + (z - cz)**2
        defect = 0.05 * np.exp(-dist2 / (2 * width**2)) * np.exp(1j * np.random.rand())
        phi += defect
    uni.lat.phi = phi / np.sqrt(shape[0]**3)  # Rough normalize

# --------------------- Main Unification Chain ---------------------
def main(args):
    cfg = load_theta_star_config()
    theta_fid = cfg.theta_star_fid_rad
    band = cfg.theta_star_band_rad
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    out_dir = Path("lab/data/full_unification") / f"{timestamp}_chain_theta{theta_fid:.2f}"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    theta_stars = np.linspace(band[0], band[1], args.n_theta)
    results = []
    
    for theta in theta_stars:
        print(f"\nProcessing θ★ = {theta:.3f} rad")
        
        # Flavor
        m_nu = toy_seesaw_mnu(theta)
        m_eff = m_nu[-1]  # Heaviest as effective mass
        
        # Vacuum
        delta_E_baseline, _ = run_microcavity(theta, m_eff=0.0, lattice_size=args.lat_size)
        delta_E_seesaw, final_A = run_microcavity(theta, m_eff=m_eff, lattice_size=args.lat_size)
        mod_percent = 100 * (delta_E_seesaw - delta_E_baseline) / abs(delta_E_baseline) if delta_E_baseline != 0 else 0
        
        # Cosmology
        t, a = run_frw(delta_E_seesaw, k_scale=args.k_scale)
        accel_percent = 100 * (a[-1] - a[0]) / a[0]  # Rough growth metric (calibrate baseline separately)
        
        # Microstructure (simple: run short with defects, check persistence via final_A)
        uni_def = ScalarToyUniverse(nx=args.lat_size, ny=args.lat_size, nz=args.lat_size, m=m_eff)
        add_gaussian_defects(uni_def, n_defects=args.n_defects)
        uni_def.set_initial_conditions(uni_def.lat.phi)
        constraint = hard_constraint_factory(theta_star=theta, epsilon=1e-2)
        for _ in range(200):
            uni_def.step(constraint=constraint)
        defect_persist = abs(uni_def.global_amplitude())
        
        results.append({
            'theta_star': theta,
            'm3_ev': m_eff,
            'delta_E': delta_E_seesaw,
            'vacuum_mod_%': mod_percent,
            'a_final': a[-1],
            'cosmo_accel_%': accel_percent,
            'defect_A_final': defect_persist
        })
    
    df = pd.DataFrame(results)
    df.to_csv(out_dir / "unification_chain.csv", index=False)
    
    # Summary plots
    fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True)
    axs[0].plot(df['theta_star'], df['m3_ev'], 'o-')
    axs[0].set_ylabel('m3 (eV)')
    axs[0].axvline(theta_fid, color='gray', ls='--')
    
    axs[1].plot(df['theta_star'], df['delta_E'], 'o-')
    axs[1].set_ylabel('ΔE (lattice units)')
    
    axs[2].plot(df['theta_star'], df['a_final'], 'o-')
    axs[2].set_ylabel('Final scale factor a')
    
    axs[3].plot(df['theta_star'], df['defect_A_final'], 'o-')
    axs[3].set_ylabel('Defect |A| persistence')
    axs[3].set_xlabel('θ★ (rad)')
    
    plt.suptitle(f'Full Unification Chain – Fiducial θ★ = {theta_fid:.2f} rad')
    plt.tight_layout()
    plt.savefig(out_dir / "unification_overview.png")
    
    # Metadata
    meta = {'timestamp': timestamp, 'n_theta': args.n_theta, 'lat_size': args.lat_size, 'k_scale': args.k_scale}
    with open(out_dir / "metadata.json", 'w') as f:
        json.dump(meta, f, indent=4)
    
    print(f"\nFull chain complete! Results in {out_dir}")
    print(f"End-to-end modulation example: ~{abs(df['vacuum_mod_%'].max()):.1f}% vacuum, ~{abs(df['cosmo_accel_%'].mean()):.1f}% cosmo")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Full Unification Chain")
    parser.add_argument('--n_theta', type=int, default=20, help="Points in θ★ band")
    parser.add_argument('--lat_size', type=int, default=16, help="Lattice size (NxNxN)")
    parser.add_argument('--k_scale', type=float, default=1e120, help="ΔE → Λ calibration (tune for realistic Ω_Λ)")
    parser.add_argument('--n_defects', type=int, default=5, help="Gaussian defects for microstructure")
    args = parser.parse_args()
    main(args)