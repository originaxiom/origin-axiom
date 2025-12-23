#!/usr/bin/env python3
# 10_microstructure_multi_field.py: Phase 3 – Microstructure with seesaw-modulated multi-field
# Version: Initial Draft (Dec 23, 2025)
# Features: 3D lattice, defects as particles, seesaw mass term, axiom constraint

import sys
import os
from datetime import datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
import pandas as pd
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
from src.theta_star_config import load_theta_star_config

# Reuse seesaw mass function (tuned from Phase 1)
def toy_seesaw_mnu(theta_star, v_SM=174, M_R_base=1e14, M_scale=2.64e-6, hierarchy='NO'):
    mod_atm = np.sin(2 * theta_star)**2
    mod_sol = np.sin(theta_star)**2
    mod1 = np.cos(theta_star)**4
    if hierarchy == 'NO':
        y_nu = np.array([mod1 * 1e-6, mod_sol * 3e-4, mod_atm * 1e-3])
    else:
        y_nu = np.array([mod_atm * 1e-3, mod_sol * 3e-4, mod1 * 1e-6])
    m_nu_gev = (y_nu * v_SM)**2 / (M_R_base * M_scale)
    m_nu_ev = m_nu_gev * 1e9
    return np.abs(m_nu_ev)

def add_defect_field(uni, n_defects=5, amplitude=0.1, width=2.0):
    """Add Gaussian defects (bumps) as 'particles' to the field."""
    rng = np.random.default_rng(42)
    nx, ny, nz = uni.lat.shape
    x, y, z = np.indices((nx, ny, nz))

    for _ in range(n_defects):
        center = rng.integers(0, nx, size=3)
        dist = np.sqrt((x - center[0])**2 + (y - center[1])**2 + (z - center[2])**2)
        bump = amplitude * np.exp(-dist**2 / (2 * width**2))
        uni.phi += bump * np.exp(1j * rng.uniform(0, 2*np.pi))  # Random phase

    uni.phi -= uni.phi.mean()  # Re-center near cancellation

def run_microstructure_simulation(theta_star, n_steps=500, dt=0.01, epsilon=1e-2, n_defects=5):
    constraint = hard_constraint_factory(theta_star=theta_star, epsilon=epsilon, A_ref=0.0)

    nx = ny = nz = 32  # 3D lattice
    c = 1.0
    m = 1e-3
    lam = 0.0

    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=c, m=m, lam=lam, dt=dt)

    # Initial field + defects
    rng = np.random.default_rng(42)
    shape = uni.lat.shape
    phi0 = 1e-3 * (rng.standard_normal(shape) + 1j * rng.standard_normal(shape))
    phi0 -= phi0.mean()
    uni.set_initial_conditions(phi0)

    add_defect_field(uni, n_defects=n_defects)

    # Seesaw modulation
    m_nu = toy_seesaw_mnu(theta_star)
    m_eff = m_nu[2]
    uni.m = m_eff

    A_history = []
    energy_history = []
    hits = 0

    for i in range(n_steps):
        uni.step(constraint=constraint)
        A = uni.global_amplitude()
        E = uni.energy() if hasattr(uni, 'energy') else 0.0
        A_history.append(abs(A))
        energy_history.append(E)
        if hasattr(uni, 'constraint_hits'):
            hits += uni.constraint_hits

    delta_E = energy_history[-1] - energy_history[0] if energy_history else 0.0

    return {
        'final_A': abs(A_history[-1]),
        'delta_E': delta_E,
        'A_history': np.array(A_history),
        'energy_history': np.array(energy_history),
        'constraint_hits': hits
    }

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_microstructure_multi_field_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_microstructure_multi_field_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 10)
    results = []

    for th in theta_stars:
        sim = run_microstructure_simulation(th, n_defects=5)

        results.append({
            'theta_star': th,
            'final_A': sim['final_A'],
            'delta_E': sim['delta_E'],
            'constraint_hits': sim['constraint_hits']
        })

        print(f"θ★={th:.3f}: final_A={sim['final_A']:.2e}, ΔE={sim['delta_E']:.2e}, hits={sim['constraint_hits']}")

    npz_path = raw_dir / f"{base_name}.npz"
    np.savez(npz_path, results=results)
    print(f"Raw data saved to: {npz_path}")

    df = pd.DataFrame(results)
    csv_path = processed_dir / f"{base_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Processed CSV saved to: {csv_path}")

    metadata = {
        'timestamp': timestamp,
        'theta_star_fid': float(theta_star_fid),
        'theta_star_band': list(theta_star_band),
        'seed': args.seed,
        'lattice_size': 32,
        'n_defects': 5
    }
    json_path = processed_dir / f"{base_name}.json"
    with open(json_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata JSON saved to: {json_path}")

    # Plot final_A and ΔE vs θ★
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(theta_stars, [r['final_A'] for r in results], label='Final |A|')
    ax1.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    ax1.set_xlabel('θ★ (rad)')
    ax1.set_ylabel('Final global amplitude |A|')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(theta_stars, [r['delta_E'] for r in results], label='ΔE')
    ax2.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    ax2.set_xlabel('θ★ (rad)')
    ax2.set_ylabel('Vacuum shift ΔE')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.suptitle('Microstructure Results vs θ★')
    plt.tight_layout()
    plt.savefig(figures_dir / f"{base_name}_results.png")
    print(f"Results plot saved to: {figures_dir / f'{base_name}_results.png'}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 3: Microstructure with multi-field seesaw modulation")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()
    main(args)