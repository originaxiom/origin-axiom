#!/usr/bin/env python3
# 12_extension_qg_hints.py: Phase B Step 1 – Derive ε from QG first principles
# Version: Initial (Dec 24, 2025)

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

from src.theta_star_config import load_theta_star_config

# Planck scale constants (SI units, converted)
PLANCK_LENGTH = 1.616e-35  # m
PLANCK_MASS = 2.176e-8  # kg
PLANCK_ENERGY = PLANCK_MASS * 3e8**2  # J
HBAR = 1.0545718e-34  # J s
C = 3e8  # m/s

def derive_epsilon(theta_star, n_defects=5):
    """
    Derive ε from QG hints:
    - Planck energy scale as cutoff
    - Holographic bound: ε ~ (Planck area) / (volume) * θ★ modulation
    - Toy: ε = (Planck energy / hbar c) * sin(θ★) * (1/n_defects)
    """
    # Holographic volume factor (toy)
    volume = n_defects  # effective defect volume
    holographic_factor = (PLANCK_LENGTH**2) / volume

    # Modulation from θ★ (sin for simplicity)
    modulation = np.abs(np.sin(theta_star))

    # Planck-scale cutoff
    planck_cutoff = PLANCK_ENERGY / (HBAR * C)  # 1/length scale

    epsilon = planck_cutoff * holographic_factor * modulation
    return epsilon

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_qg_hints_epsilon_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_qg_hints_epsilon_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 20)
    n_defects_list = [1, 5, 10]
    results = []

    for n_def in n_defects_list:
        epsilons = []
        for th in theta_stars:
            eps = derive_epsilon(th, n_defects=n_def)
            epsilons.append(eps)
            print(f"θ★={th:.3f}, n_def={n_def}: ε={eps:.2e}")

        results.append({
            'n_defects': n_def,
            'theta_stars': theta_stars.tolist(),
            'epsilons': epsilons
        })

    npz_path = raw_dir / f"{base_name}.npz"
    np.savez(npz_path, results=results)
    print(f"Raw data saved to: {npz_path}")

    df = pd.DataFrame({
        'theta_star': theta_stars,
        'epsilon_n1': results[0]['epsilons'],
        'epsilon_n5': results[1]['epsilons'],
        'epsilon_n10': results[2]['epsilons']
    })
    csv_path = processed_dir / f"{base_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Processed CSV saved to: {csv_path}")

    # Plot ε vs θ★ for each n_defects
    fig_path = figures_dir / f"{base_name}_epsilon_vs_theta.png"
    plt.figure(figsize=(10, 6))
    for res in results:
        plt.plot(res['theta_stars'], res['epsilons'], label=f'n_defects = {res["n_defects"]}')
    plt.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    plt.xlabel('θ★ (rad)')
    plt.ylabel('Derived ε (Planck units)')
    plt.title('Axiom Floor ε(θ★) from QG Hints')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(fig_path)
    print(f"ε plot saved to: {fig_path}")

    # Summary
    summary_path = processed_dir / f"{base_name}_summary.txt"
    with open(summary_path, 'w') as f:
        f.write("Phase B Step 1: QG Hints for ε\n")
        f.write(f"Date: {timestamp}\n")
        f.write(f"θ★ fiducial: {theta_star_fid:.3f} rad\n")
        f.write(f"Derived ε range: {min(min(r['epsilons']) for r in results):.2e} to {max(max(r['epsilons']) for r in results):.2e}\n")
        f.write(f"Modulation from θ★: ~sin(θ★) dependence\n")
    print(f"Summary saved to: {summary_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase B Step 1: Derive ε from QG hints")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()
    main(args)