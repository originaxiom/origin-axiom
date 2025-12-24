#!/usr/bin/env python3
# 14_baryogenesis.py: Phase B Step 3 – Baryogenesis via θ★-driven CP asymmetry in defect decay
# Version: Initial (Dec 24, 2025)

import sys
import os
from datetime import datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from src.theta_star_config import load_theta_star_config

# Baryon asymmetry parameters
eta_B_observed = 6.1e-10  # PDG value

def toy_defect_decay_rate(theta_star, n_defects=5):
    """Toy decay rate with θ★-dependent CP asymmetry."""
    # Base rate
    rate = 1e-3  # arbitrary units
    # CP asymmetry from θ★ (e.g., sin(2θ★))
    cp_asym = np.sin(2 * theta_star) * 0.1  # ~10% max
    return rate * (1 + cp_asym)

def compute_baryon_asymmetry(theta_star, n_defects=5, t_decay=1e-3):
    """Compute η_B from defect decay."""
    decay_rate = toy_defect_decay_rate(theta_star, n_defects)
    # Toy baryon production
    n_b = decay_rate * t_decay * n_defects
    n_gamma = 1.0  # normalized photon density
    eta_B = n_b / n_gamma
    return eta_B

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_baryogenesis_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_baryogenesis_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 20)
    n_defects_list = [1, 5, 10]
    results = []

    for n_def in n_defects_list:
        eta_B_list = []
        for th in theta_stars:
            eta_B = compute_baryon_asymmetry(th, n_defects=n_def)
            eta_B_list.append(eta_B)
            print(f"θ★={th:.3f}, n_def={n_def}: η_B={eta_B:.2e}")

        results.append({
            'n_defects': n_def,
            'theta_stars': theta_stars.tolist(),
            'eta_B': eta_B_list
        })

    npz_path = raw_dir / f"{base_name}.npz"
    np.savez(npz_path, results=results)
    print(f"Raw data saved to: {npz_path}")

    df = pd.DataFrame({
        'theta_star': theta_stars,
        'eta_B_n1': results[0]['eta_B'],
        'eta_B_n5': results[1]['eta_B'],
        'eta_B_n10': results[2]['eta_B']
    })
    csv_path = processed_dir / f"{base_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Processed CSV saved to: {csv_path}")

    # Plot η_B vs θ★ for each n_defects
    fig_path = figures_dir / f"{base_name}_etaB_vs_theta.png"
    plt.figure(figsize=(10, 6))
    for res in results:
        plt.plot(res['theta_stars'], res['eta_B'], label=f'n_defects = {res["n_defects"]}')
    plt.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    plt.axhline(eta_B_observed, color='red', ls='--', label='Observed η_B')
    plt.xlabel('θ★ (rad)')
    plt.ylabel('Baryon asymmetry η_B')
    plt.title('Baryogenesis: η_B(θ★) from Defect Decay')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(fig_path)
    print(f"η_B plot saved to: {fig_path}")

    # Summary
    summary_path = processed_dir / f"{base_name}_summary.txt"
    with open(summary_path, 'w') as f:
        f.write("Phase B Step 3: Baryogenesis Calculation\n")
        f.write(f"Date: {timestamp}\n")
        f.write(f"θ★ fiducial: {theta_star_fid:.3f} rad\n")
        f.write(f"Max η_B: {max(max(r['eta_B']) for r in results):.2e}\n")
        f.write(f"Observed η_B: {eta_B_observed:.2e}\n")
        f.write(f"Modulation from θ★: ~sin(2θ★) dependence\n")
    print(f"Summary saved to: {summary_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase B Step 3: Baryogenesis via θ★-driven CP asymmetry")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()
    main(args)