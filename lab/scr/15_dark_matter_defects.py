#!/usr/bin/env python3
# 15_dark_matter_defects.py: Phase B Step 4 – Dark matter model from defects
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

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from src.theta_star_config import load_theta_star_config

# Cosmological constants (Planck 2018)
h = 0.674
rho_crit = 1.878e-26  # kg/m³
T0 = 2.725  # CMB temperature (K)
g_star = 3.91  # effective degrees of freedom at freeze-out

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

def toy_defect_mass(theta_star):
    """Defect mass from seesaw m_eff."""
    m_nu = toy_seesaw_mnu(theta_star)
    return m_nu[2] * 1e-6  # GeV scale (toy)

def relic_density(theta_star, n_defects=5, sigma_v=1e-9):
    """Toy relic density calculation (freeze-out approximation)."""
    m_DM = toy_defect_mass(theta_star)
    # Freeze-out temperature T_f ~ m_DM / 20
    T_f = m_DM / 20
    # Equilibrium number density
    n_eq = (g_star * T_f**3) / (2 * np.pi**2) * np.exp(-m_DM / T_f)
    # Relic density
    Omega_h2 = (m_DM * n_eq * sigma_v) / rho_crit * h**2
    return Omega_h2

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_dark_matter_defects_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_dark_matter_defects_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 20)
    n_defects_list = [1, 5, 10]
    results = []

    for n_def in n_defects_list:
        omega_list = []
        for th in theta_stars:
            omega = relic_density(th, n_defects=n_def)
            omega_list.append(omega)
            print(f"θ★={th:.3f}, n_def={n_def}: Ω_DM h²={omega:.2e}")

        results.append({
            'n_defects': n_def,
            'theta_stars': theta_stars.tolist(),
            'omega_h2': omega_list
        })

    npz_path = raw_dir / f"{base_name}.npz"
    np.savez(npz_path, results=results)
    print(f"Raw data saved to: {npz_path}")

    df = pd.DataFrame({
        'theta_star': theta_stars,
        'omega_h2_n1': results[0]['omega_h2'],
        'omega_h2_n5': results[1]['omega_h2'],
        'omega_h2_n10': results[2]['omega_h2']
    })
    csv_path = processed_dir / f"{base_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Processed CSV saved to: {csv_path}")

    # Plot Ω_DM h² vs θ★ for each n_defects
    fig_path = figures_dir / f"{base_name}_omega_vs_theta.png"
    plt.figure(figsize=(10, 6))
    for res in results:
        plt.plot(res['theta_stars'], res['omega_h2'], label=f'n_defects = {res["n_defects"]}')
    plt.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    plt.axhline(0.12, color='red', ls='--', label='Observed Ω_DM h²')
    plt.xlabel('θ★ (rad)')
    plt.ylabel('Relic density Ω_DM h²')
    plt.title('Dark Matter Relic Density from Defects')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(fig_path)
    print(f"Ω_DM plot saved to: {fig_path}")

    # Summary
    summary_path = processed_dir / f"{base_name}_summary.txt"
    with open(summary_path, 'w') as f:
        f.write("Phase B Step 4: Dark Matter Model\n")
        f.write(f"Date: {timestamp}\n")
        f.write(f"θ★ fiducial: {theta_star_fid:.3f} rad\n")
        f.write(f"Max Ω_DM h²: {max(max(r['omega_h2']) for r in results):.2e}\n")
        f.write(f"Observed Ω_DM h²: 0.12\n")
        f.write(f"Modulation from θ★: ~sin(2θ★) dependence\n")
    print(f"Summary saved to: {summary_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase B Step 4: Dark matter model from defects")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()
    main(args)