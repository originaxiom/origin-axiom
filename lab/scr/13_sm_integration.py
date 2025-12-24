#!/usr/bin/env python3
# 13_sm_integration.py: Phase B Step 2 – Full SM integration with gauge/fermions & EWSB test
# Version: 1.2 (fixed NameError - mu2/lambda_h scope)

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

# Higgs vev & gauge couplings (toy EW)
v_ew = 246  # GeV
g = 0.65  # SU(2) coupling
g_prime = 0.34  # U(1) coupling

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

def ew_higgs_potential(h):
    """Higgs potential with axiom floor."""
    lambda_h = 0.13
    mu2 = -(v_ew**2) * lambda_h
    V = mu2 * h**2 + lambda_h * h**4
    return V

def run_sm_simulation(theta_star, n_steps=500, dt=0.01, epsilon=1e-2):
    m_nu = toy_seesaw_mnu(theta_star)
    m_eff = m_nu[2]  # Heaviest neutrino mass

    # Toy EWSB: Higgs field h, modulated by seesaw
    h = v_ew + 0.1 * m_eff * np.sin(theta_star)  # Small perturbation

    # Axiom floor on Higgs amplitude
    A_h = abs(h)
    if A_h < epsilon:
        h += epsilon * np.sign(h)

    # Define mu2 and lambda_h in scope
    lambda_h = 0.13
    mu2 = -(v_ew**2) * lambda_h

    V_h = ew_higgs_potential(h)

    # Gauge fields (toy): g, g' modulated by θ★
    g_eff = g * (1 + 0.01 * np.sin(2*theta_star))
    g_prime_eff = g_prime * (1 + 0.01 * np.sin(theta_star))

    # Simulate EWSB stability
    h_history = [h]
    V_history = [V_h]

    for i in range(n_steps):
        # Toy evolution: relax to minimum
        dh_dt = -0.1 * (2 * mu2 * h + 4 * lambda_h * h**3)
        h += dh_dt * dt
        V = ew_higgs_potential(h)
        h_history.append(h)
        V_history.append(V)

    return {
        'final_h': h,
        'final_V': V_history[-1],
        'h_history': np.array(h_history),
        'V_history': np.array(V_history),
        'g_eff': g_eff,
        'g_prime_eff': g_prime_eff
    }

def main(args):
    config = load_theta_star_config()
    theta_star_fid = config.theta_star_fid_rad
    theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star_fid:.3f} rad, band [{theta_star_band[0]:.2f}, {theta_star_band[1]:.2f}]")

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_sm_integration_theta{theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    base_name = f"{timestamp}_sm_integration_theta{theta_star_fid:.2f}_seed{args.seed}"

    theta_stars = np.linspace(theta_star_band[0], theta_star_band[1], 10)
    results = []

    for th in theta_stars:
        sim = run_sm_simulation(th)

        results.append({
            'theta_star': th,
            'final_h': sim['final_h'],
            'final_V': sim['final_V'],
            'g_eff': sim['g_eff'],
            'g_prime_eff': sim['g_prime_eff']
        })

        print(f"θ★={th:.3f}: final_h={sim['final_h']:.2e}, final_V={sim['final_V']:.2e}")

    npz_path = raw_dir / f"{base_name}.npz"
    np.savez(npz_path, results=results)
    print(f"Raw data saved to: {npz_path}")

    df = pd.DataFrame(results)
    csv_path = processed_dir / f"{base_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Processed CSV saved to: {csv_path}")

    # Plot final_h and final_V vs θ★
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(theta_stars, [r['final_h'] for r in results], label='Final Higgs vev')
    ax1.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    ax1.set_xlabel('θ★ (rad)')
    ax1.set_ylabel('Final h (GeV)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(theta_stars, [r['final_V'] for r in results], label='Final V(h)')
    ax2.axvline(theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    ax2.set_xlabel('θ★ (rad)')
    ax2.set_ylabel('Higgs potential V(h)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.suptitle('SM Integration: EWSB with θ★ Modulation')
    plt.tight_layout()
    plt.savefig(figures_dir / f"{base_name}_ewsb.png")
    print(f"EWSB plot saved to: {figures_dir / f'{base_name}_ewsb.png'}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase B Step 2: Full SM integration with EWSB test")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()
    main(args)