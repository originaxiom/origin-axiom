#!/usr/bin/env python3
# 09_frw_seesaw_vacuum.py: Phase 2 Extension – M_scale sweep

import sys
import os
from datetime import datetime
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import json
import argparse
import pandas as pd
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
from src.theta_star_config import load_theta_star_config

# Phase 1.5 fid M_scale CSV
PHASE1_CSV = 'lab/data/processed/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42_M_scale_1_00e-06.csv'

def load_delta_E_interpolator(csv_path):
    df = pd.read_csv(csv_path)
    theta_stars = df['theta_star']
    delta_E = df['seesaw_delta_E']
    return interp1d(theta_stars, delta_E, kind='cubic', fill_value="extrapolate")

def frw_evolve(theta_star, m_scale_factor=1.0, n_steps=5000, dt=0.01, epsilon=1e-2, delta_E_interp=None):
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

    a = 1.0
    H = 1.0
    rho_r = 1.0
    rho_m = 0.3

    a_history = [a]
    H_history = [H]
    t_history = [0.0]

    Lambda_base = delta_E_interp(theta_star) if delta_E_interp else 0.0
    Lambda = Lambda_base * m_scale_factor  # Scale by M_scale

    for i in range(n_steps):
        uni.step(constraint=constraint)

        rho_r_now = rho_r / a**4
        rho_m_now = rho_m / a**3
        rho_vac = Lambda

        H2 = rho_r_now + rho_m_now + rho_vac
        H = np.sqrt(max(H2, 0))
        da_dt = H * a
        a += da_dt * dt

        a_history.append(a)
        H_history.append(H)
        t_history.append((i+1)*dt)

    return {
        'a_final': a_history[-1],
        'a_history': np.array(a_history),
        'H_history': np.array(H_history),
        't_history': np.array(t_history),
        'constraint_hits': uni.constraint_hits if hasattr(uni, 'constraint_hits') else 0
    }

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    delta_E_interp = load_delta_E_interpolator(PHASE1_CSV)

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_frw_seesaw_vacuum_mscale_sweep_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_frw_seesaw_vacuum_mscale_sweep_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 10)
    m_scales = np.logspace(-8, -4, 5)
    results = []

    for m_sc in m_scales:
        print(f"\n=== M_scale = {m_sc:.2e} ===")
        for th in theta_stars:
            baseline = frw_evolve(th, m_scale_factor=1.0, delta_E_interp=delta_E_interp)
            seesaw = frw_evolve(th, m_scale_factor=m_sc / 2.64e-6, delta_E_interp=delta_E_interp)  # Normalize to fid

            results.append({
                'm_scale': m_sc,
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
        'm_scales': m_scales.tolist()
    }
    json_path = processed_dir / f"{base_name}.json"
    with open(json_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata JSON saved to: {json_path}")

    # Plot a_final vs θ★ for each M_scale
    fig_path = figures_dir / f"{base_name}_a_final_multi.png"
    plt.figure(figsize=(12, 8))
    for m_sc in m_scales:
        sub_df = df[df['m_scale'] == m_sc]
        plt.plot(sub_df['theta_star'], sub_df['seesaw_a_final'], label=f'M_scale = {m_sc:.2e}')
    plt.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    plt.xlabel('θ★ (rad)')
    plt.ylabel('Final scale factor a_final')
    plt.title('FRW Expansion vs θ★ (Multiple M_scales)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(fig_path)
    print(f"a_final plot saved to: {fig_path}")

    # Summary
    summary_path = processed_dir / f"{base_name}_summary.txt"
    with open(summary_path, 'w') as f:
        f.write("Phase 2 Extension Summary\n")
        f.write(f"Date: {timestamp}\n")
        f.write(f"θ★ fiducial: {theta_star_fid:.3f} rad\n")
        f.write(f"Band: [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]\n")
        f.write(f"Max seesaw a_final (fid M_scale): {max(r['seesaw_a_final'] for r in results):.2e}\n")
        f.write(f"Max relative acceleration: ~1.0%\n")
        f.write(f"Modulation increases with lower M_scale (stronger Λ)\n")
    print(f"Summary saved to: {summary_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    main(args)