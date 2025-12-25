#!/usr/bin/env python3
# 07_toy_seesaw_gut.py: Phase 1 toy seesaw with outputs matching repo style

import sys
import os
from datetime import datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from pathlib import Path

# Fix: Add repo root to sys.path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
from src.theta_star_config import load_theta_star_config

# PDG targets (NO hierarchy)
PDG_mnu_ev = np.array([0.0, 0.0088, 0.05])
PDG_sin2thw = 0.231
AXIOM_EPS = 1e-12

def toy_seesaw_mnu(theta_star, v_SM=174, M_R_base=1e14, M_scale=1.0, hierarchy='NO'):
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

def compute_sin2thw(theta_star):
    return 0.375 - 0.02 * np.sin(theta_star)

def apply_axiom_to_masses(m_nu: np.ndarray, theta_star: float, eps: float = AXIOM_EPS):
    total_mnu = np.sum(m_nu)
    if total_mnu >= eps:
        return m_nu.copy(), False
    A_star = 0.0
    A = total_mnu
    diff = A - A_star
    dist = abs(diff)
    direction = 1.0 if dist == 0 else diff / dist
    target = eps * direction
    delta = (target - A) / len(m_nu)
    m_nu_lifted = m_nu + delta
    print(f"Axiom hit: lifted from {total_mnu:.2e} to {np.sum(m_nu_lifted):.2e}")
    return m_nu_lifted, True

def main(args):
    config = load_theta_star_config()
    theta_star = config.theta_star_fid_rad
    band = config.theta_star_band_rad
    print(f"θ★ fiducial: {theta_star:.3f} rad, band [{band[0]:.2f}, {band[1]:.2f}]")

    # Timestamp in repo style: MM-DD_HH-MM
    now = datetime.now()
    timestamp = now.strftime("%m-%d_%H-%M")

    # Output subfolder name
    subfolder_name = f"{timestamp}_seesaw_scan_theta{theta_star:.2f}_seed{args.seed}"

    # Base paths inside lab/data/
    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    # Create all directories
    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # Base filename (without extension)
    base_name = f"{timestamp}_seesaw_scan_theta{theta_star:.2f}_seed{args.seed}"

    M_R_base = 10**args.M_R_log
    m_nu = toy_seesaw_mnu(theta_star, M_R_base=M_R_base, M_scale=1.0)
    m_nu_constrained, hit = apply_axiom_to_masses(m_nu, theta_star)
    if hit:
        m_nu = m_nu_constrained

    sin2thw = compute_sin2thw(theta_star)
    total_mnu = np.sum(m_nu)
    axiom_ok = total_mnu > AXIOM_EPS

    print(f"Calculated neutrino masses (eV): {m_nu}")
    print(f"PDG approx: {PDG_mnu_ev}")
    print(f"Calculated sin²θ_w: {sin2thw:.3f} (PDG: {PDG_sin2thw})")
    print(f"Total m_ν: {total_mnu:.2e} eV, Axiom floor OK: {axiom_ok}")

    if args.scan:
        M_scales = np.logspace(-10, 2, 20)
        results = {'M_scale': M_scales.tolist(), 'm1': [], 'm2': [], 'm3': [], 'delta_matm2': [], 'axiom_hits': []}
        for sc in M_scales:
            mns = toy_seesaw_mnu(theta_star, M_R_base=M_R_base, M_scale=sc)
            mns_constr, hit = apply_axiom_to_masses(mns, theta_star)
            delta_atm = mns_constr[2]**2 - mns_constr[1]**2
            results['m1'].append(mns_constr[0])
            results['m2'].append(mns_constr[1])
            results['m3'].append(mns_constr[2])
            results['delta_matm2'].append(delta_atm)
            results['axiom_hits'].append(int(hit))

            if 0.001 < abs(delta_atm) < 0.003:
                print(f"PDG match @ M_scale={sc:.2e}: m_ν={mns_constr}, Δm_atm²={delta_atm:.2e}")

        # Save raw .npz
        npz_path = raw_dir / f"{base_name}.npz"
        np.savez(npz_path, **results)
        print(f"Raw data saved to: {npz_path}")

        # Save processed CSV
        df = pd.DataFrame({
            'M_scale': results['M_scale'],
            'm1_eV': results['m1'],
            'm2_eV': results['m2'],
            'm3_eV': results['m3'],
            'Delta_m_atm2_eV2': results['delta_matm2'],
            'axiom_hit': results['axiom_hits']
        })
        csv_path = processed_dir / f"{base_name}.csv"
        df.to_csv(csv_path, index=False)
        print(f"Processed CSV saved to: {csv_path}")

        # Save metadata JSON
        metadata = {
            'timestamp': timestamp,
            'theta_star': float(theta_star),
            'M_R_base': M_R_base,
            'seed': args.seed,
            'fiducial_masses': m_nu.tolist(),
            'fiducial_total_mnu': float(total_mnu),
            'fiducial_sin2thw': float(sin2thw)
        }
        json_path = processed_dir / f"{base_name}.json"
        with open(json_path, 'w') as f:
            json.dump(metadata, f, indent=4)
        print(f"Metadata JSON saved to: {json_path}")

        # Save figure
        fig_path = figures_dir / f"{base_name}.png"
        plt.loglog(results['M_scale'], np.abs(results['delta_matm2']))
        plt.axhline(2.5e-3, ls='--', label='PDG Δm_atm²')
        plt.xlabel('M_R scale factor')
        plt.ylabel('|Δm_atm²| (eV²)')
        plt.legend()
        plt.savefig(fig_path)
        print(f"Plot saved to: {fig_path}")

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--M_R_log', type=float, default=14, help='log10(M_R / GeV)')
    parser.add_argument('--scan', action='store_true')
    args = parser.parse_args()
    main(args)