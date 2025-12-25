#!/usr/bin/env python3
# 16_predictions.py: Phase B Step 5 – Experimental predictions from θ★ modulation
# Version: 1.1 (fixed NameError - added toy_seesaw_mnu)

import sys
import os
from datetime import datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from pathlib import Path
from scipy.interpolate import interp1d

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from src.theta_star_config import load_theta_star_config

# Phase 1.5 ΔE CSV (fiducial M_scale)
PHASE1_CSV = 'lab/data/processed/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42_M_scale_1_00e-06.csv'

# Cosmological constants
H0_observed = 67.4  # km/s/Mpc (Planck)
H0_tension = 73.0  # km/s/Mpc (local)
T_CMB = 2.725  # K

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

def load_delta_E_interpolator(csv_path):
    df = pd.read_csv(csv_path)
    theta_stars = df['theta_star']
    delta_E = df['seesaw_delta_E']
    return interp1d(theta_stars, delta_E, kind='cubic', fill_value="extrapolate")

def predict_neutrino_mixing(theta_star, m_nu):
    """Toy PMNS angles modulated by θ★."""
    theta_12 = np.arcsin(np.sqrt(0.304 + 0.01 * np.sin(theta_star)))  # solar
    theta_23 = np.arcsin(np.sqrt(0.573 + 0.02 * np.sin(2*theta_star)))  # atmospheric
    theta_13 = np.arcsin(np.sqrt(0.022 + 0.005 * np.sin(theta_star)))  # reactor
    return theta_12, theta_23, theta_13

def predict_cmb_anisotropy(delta_E):
    """Toy CMB temperature anisotropy from vacuum fluctuations."""
    delta_T_over_T = delta_E / (T_CMB**4) * 1e-5  # normalized
    return delta_T_over_T

def predict_h0(delta_E):
    """Toy H0 adjustment from vacuum energy."""
    delta_H0 = H0_observed + 0.1 * (delta_E / 1e-5) * (H0_tension - H0_observed)
    return delta_H0

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    delta_E_interp = load_delta_E_interpolator(PHASE1_CSV)

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_predictions_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_predictions_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 20)
    results = []

    for th in theta_stars:
        delta_E = delta_E_interp(th)
        m_nu = toy_seesaw_mnu(th)
        theta_12, theta_23, theta_13 = predict_neutrino_mixing(th, m_nu)
        delta_T_over_T = predict_cmb_anisotropy(delta_E)
        h0 = predict_h0(delta_E)

        results.append({
            'theta_star': th,
            'delta_E': delta_E,
            'theta_12': theta_12 * 180/np.pi,  # degrees
            'theta_23': theta_23 * 180/np.pi,
            'theta_13': theta_13 * 180/np.pi,
            'delta_T_over_T': delta_T_over_T,
            'h0': h0
        })

        print(f"θ★={th:.3f}: delta_E={delta_E:.2e}, θ_13={theta_13*180/np.pi:.2f}°, H0={h0:.2f}")

    npz_path = raw_dir / f"{base_name}.npz"
    np.savez(npz_path, results=results)
    print(f"Raw data saved to: {npz_path}")

    df = pd.DataFrame(results)
    csv_path = processed_dir / f"{base_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Processed CSV saved to: {csv_path}")

    # Plot predictions vs θ★
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
    ax1.plot(theta_stars, df['theta_13'], label='θ_13 (deg)')
    ax1.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    ax1.set_ylabel('θ_13')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(theta_stars, df['delta_T_over_T'], label='ΔT/T')
    ax2.axvline(theta_star_fid, color='gray', ls=':')
    ax2.set_ylabel('ΔT/T')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    ax3.plot(theta_stars, df['h0'], label='H0 (km/s/Mpc)')
    ax3.axhline(H0_observed, color='blue', ls='--', label='Planck H0')
    ax3.axhline(H0_tension, color='red', ls='--', label='Local H0')
    ax3.axvline(theta_star_fid, color='gray', ls=':')
    ax3.set_xlabel('θ★ (rad)')
    ax3.set_ylabel('H0')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    plt.suptitle('Experimental Predictions from θ★ Modulation')
    plt.tight_layout()
    plt.savefig(figures_dir / f"{base_name}_predictions.png")
    print(f"Predictions plot saved to: {figures_dir / f'{base_name}_predictions.png'}")

    # Summary
    summary_path = processed_dir / f"{base_name}_summary.txt"
    with open(summary_path, 'w') as f:
        f.write("Phase B Step 5: Experimental Predictions\n")
        f.write(f"Date: {timestamp}\n")
        f.write(f"θ★ fiducial: {theta_star_fid:.3f} rad\n")
        f.write(f"Max ΔT/T: {max(df['delta_T_over_T']):.2e}\n")
        f.write(f"H0 range: {min(df['h0']):.2f} to {max(df['h0']):.2f} km/s/Mpc\n")
        f.write(f"Observed H0 tension: 67.4 vs 73.0\n")
    print(f"Summary saved to: {summary_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase B Step 5: Experimental predictions from θ★ modulation")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()
    main(args)