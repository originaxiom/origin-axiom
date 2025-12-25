#!/usr/bin/env python3
# 09_frw_seesaw_vacuum.py: Phase 2 Refined – Data-driven Λ(θ★) from Phase 1.5

import sys
import os
from datetime import datetime
import argparse
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import json
import pandas as pd
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
from src.theta_star_config import load_theta_star_config

# Load Phase 1.5 ΔE data (replace with your CSV path)
PHASE1_CSV = 'lab/data/processed/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42_M_scale_1_00e-06.csv' # Fid M_scale

def load_delta_E_interpolator(csv_path):
    df = pd.read_csv(csv_path)
    theta_stars = df['theta_star']
    delta_E = df['seesaw_delta_E']
    return interp1d(theta_stars, delta_E, kind='cubic', fill_value="extrapolate")

def frw_evolve(theta_star, n_steps=2000, dt=0.01, epsilon=1e-2, use_seesaw=False, delta_E_interp=None):
    constraint = hard_constraint_factory(theta_star=theta_star, epsilon=epsilon, A_ref=0.0)

    nx = ny = nz = 16
    c = 1.0
    m = 1e-3
    lam = 0.0

    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=c, m=m, lam=lam, dt=dt)

    rng = np.random.default_rng(42)
    shape = uni.lat.shape
    phi0 = 1e-3 * (rng.standard_normal(shape) + 1j * rng.standard_normal(shape))
    phi0 -= phi0.mean()
    uni.set_initial_conditions(phi0)

    # Initial FRW: a=1, H=1 (arbitrary units)
    a = 1.0
    H = 1.0
    rho_r = 1.0  # Initial radiation density
    rho_m = 0.3  # Initial matter density

    a_history = [a]
    H_history = [H]
    t_history = [0.0]
    rho_vac_history = [0.0]

    # Vacuum energy
    Lambda = delta_E_interp(theta_star) if use_seesaw and delta_E_interp else 0.0

    for i in range(n_steps):
        uni.step(constraint=constraint)

        # FRW densities
        rho_r_now = rho_r / a**4
        rho_m_now = rho_m / a**3
        rho_vac = Lambda  # Constant vacuum

        H2 = rho_r_now + rho_m_now + rho_vac
        H = np.sqrt(max(H2, 0))
        da_dt = H * a
        a += da_dt * dt

        a_history.append(a)
        H_history.append(H)
        t_history.append((i+1)*dt)
        rho_vac_history.append(rho_vac)

    return {
        'a_final': a_history[-1],
        'a_history': np.array(a_history),
        'H_history': np.array(H_history),
        't_history': np.array(t_history),
        'rho_vac_history': np.array(rho_vac_history),
        'constraint_hits': uni.constraint_hits if hasattr(uni, 'constraint_hits') else 0
    }

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    # Load ΔE interpolator from Phase 1.5
    delta_E_interp = load_delta_E_interpolator(PHASE1_CSV)

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_frw_seesaw_vacuum_refined_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_frw_seesaw_vacuum_refined_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 10)
    results = []

    for th in theta_stars:
        baseline = frw_evolve(th, use_seesaw=False, delta_E_interp=delta_E_interp)
        seesaw = frw_evolve(th, use_seesaw=True, delta_E_interp=delta_E_interp)

        results.append({
            'theta_star': th,
            'baseline_a_final': baseline['a_final'],
            'seesaw_a_final': seesaw['a_final'],
            'constraint_hits': seesaw['constraint_hits']
        })

        print(f"θ★={th:.3f}: baseline a_final={baseline['a_final']:.2e}, seesaw a_final={seesaw['a_final']:.2e}")

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
        'lattice_size': 16
    }
    json_path = processed_dir / f"{base_name}.json"
    with open(json_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata JSON saved to: {json_path}")

    # Plot a(t) for fiducial
    fid_baseline = frw_evolve(theta_star_fid, use_seesaw=False, delta_E_interp=delta_E_interp)
    fid_seesaw = frw_evolve(theta_star_fid, use_seesaw=True, delta_E_interp=delta_E_interp)

    fig_path = figures_dir / f"{base_name}_a_history_fiducial.png"
    plt.figure(figsize= (10, 6))
    plt.plot(fid_baseline['t_history'], fid_baseline['a_history'], label='Baseline a(t)')
    plt.plot(fid_seesaw['t_history'], fid_seesaw['a_history'], label='Seesaw a(t)')
    plt.xlabel('Time')
    plt.ylabel('Scale factor a(t)')
    plt.title(f'FRW Expansion at Fiducial θ★ = {theta_star_fid:.3f} rad')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(fig_path)
    print(f"a(t) plot saved to: {fig_path}")

    # Plot H(t) for fiducial
    fig2_path = figures_dir / f"{base_name}_H_history_fiducial.png"
    plt.figure(figsize=(10, 6))
    plt.plot(fid_baseline['t_history'], fid_baseline['H_history'], label='Baseline H(t)')
    plt.plot(fid_seesaw['t_history'], fid_seesaw['H_history'], label='Seesaw H(t)')
    plt.xlabel('Time')
    plt.ylabel('Hubble H(t)')
    plt.title(f'Hubble Parameter at Fiducial θ★ = {theta_star_fid:.3f} rad')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(fig2_path)
    print(f"H(t) plot saved to: {fig2_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    main(args)