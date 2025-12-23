#!/usr/bin/env python3
# 09_frw_seesaw_vacuum.py: Phase 2 Final – Consolidated, data-driven FRW with seesaw vacuum modulation
# Version: Final (Dec 23, 2025)
# Modes: --mode simple (default), --mode sweep, --mode fiducial-only
# Reproduces all prior results; authoritative for Phase 2

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

# Fix sys.path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, REPO_ROOT)

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
from src.theta_star_config import load_theta_star_config

# Phase 1.5 fid M_scale CSV (update if needed)
PHASE1_CSV = 'lab/data/processed/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42/12-22_21-49_microcavity_seesaw_polished_v5_theta3.63_seed42_M_scale_1_00e-06.csv'

def load_delta_E_interpolator(csv_path):
    """Load ΔE(θ★) from Phase 1.5 CSV for vacuum energy."""
    df = pd.read_csv(csv_path)
    theta_stars = df['theta_star']
    delta_E = df['seesaw_delta_E']
    return interp1d(theta_stars, delta_E, kind='cubic', fill_value="extrapolate")

def frw_evolve(theta_star, m_scale_factor=1.0, n_steps=5000, dt=0.01, epsilon=1e-2, delta_E_interp=None):
    """Core FRW evolution with seesaw-modulated vacuum energy."""
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
    rho_r = 1.0  # Initial radiation
    rho_m = 0.3  # Initial matter

    a_history = [a]
    H_history = [H]
    t_history = [0.0]

    Lambda_base = delta_E_interp(theta_star) if delta_E_interp else 0.0
    Lambda = Lambda_base * m_scale_factor  # Scale by M_scale factor

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

def run_mode_simple(args, delta_E_interp):
    """Simple run: baseline vs seesaw at fiducial θ★."""
    fid_baseline = frw_evolve(args.theta_star_fid, m_scale_factor=1.0, delta_E_interp=delta_E_interp)
    fid_seesaw = frw_evolve(args.theta_star_fid, m_scale_factor=1.0, delta_E_interp=delta_E_interp)

    print(f"Fiducial θ★={args.theta_star_fid:.3f}: baseline a_final={fid_baseline['a_final']:.2e}, seesaw a_final={fid_seesaw['a_final']:.2e}")

    # Plot a(t) and H(t)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    ax1.plot(fid_baseline['t_history'], fid_baseline['a_history'], label='Baseline')
    ax1.plot(fid_seesaw['t_history'], fid_seesaw['a_history'], label='Seesaw')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Scale factor a(t)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(fid_baseline['t_history'], fid_baseline['H_history'], label='Baseline')
    ax2.plot(fid_seesaw['t_history'], fid_seesaw['H_history'], label='Seesaw')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Hubble H(t)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.suptitle(f'FRW at Fiducial θ★ = {args.theta_star_fid:.3f} rad')
    plt.tight_layout()
    plt.savefig(args.output_dir / 'a_H_fiducial.png')
    print(f"Plots saved to: {args.output_dir / 'a_H_fiducial.png'}")

def run_mode_sweep(args, delta_E_interp):
    """Full sweep: baseline vs seesaw over θ★ band, with M_scale variation."""
    m_scales = np.logspace(-8, -4, 5)
    results = []

    for m_sc in m_scales:
        print(f"\n=== M_scale = {m_sc:.2e} ===")
        for th in args.theta_stars:
            baseline = frw_evolve(th, m_scale_factor=1.0, delta_E_interp=delta_E_interp)
            seesaw = frw_evolve(th, m_scale_factor=m_sc / 2.64e-6, delta_E_interp=delta_E_interp)

            results.append({
                'm_scale': m_sc,
                'theta_star': th,
                'baseline_a_final': baseline['a_final'],
                'seesaw_a_final': seesaw['a_final'],
                'constraint_hits': seesaw['constraint_hits']
            })

            print(f"θ★={th:.3f}: baseline a_final={baseline['a_final']:.2e}, seesaw a_final={seesaw['a_final']:.2e}")

    df = pd.DataFrame(results)
    df.to_csv(args.output_dir / 'sweep_results.csv', index=False)
    print(f"Sweep results saved to: {args.output_dir / 'sweep_results.csv'}")

    # Plot a_final vs θ★ for each M_scale
    fig, ax = plt.subplots(figsize=(12, 8))
    for m_sc in m_scales:
        sub_df = df[df['m_scale'] == m_sc]
        ax.plot(sub_df['theta_star'], sub_df['seesaw_a_final'], label=f'M_scale = {m_sc:.2e}')
    ax.axvline(args.theta_star_fid, color='gray', ls=':', label='Fiducial θ★')
    ax.set_xlabel('θ★ (rad)')
    ax.set_ylabel('Final scale factor a_final')
    ax.set_title('FRW Expansion vs θ★ (Multiple M_scales)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.savefig(args.output_dir / 'a_final_multi.png')
    print(f"a_final plot saved to: {args.output_dir / 'a_final_multi.png'}")

def main(args):
    config = load_theta_star_config()
    args.theta_star_fid = config.theta_star_fid_rad
    args.theta_star_band = config.theta_star_band_rad
    print(f"θ★ fiducial: {args.theta_star_fid:.3f} rad, band [{args.theta_star_band[0]:.2f}, {args.theta_star_band[1]:.2f}]")

    delta_E_interp = load_delta_E_interpolator(PHASE1_CSV)

    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    subfolder_name = f"{timestamp}_frw_seesaw_vacuum_final_theta{args.theta_star_fid:.2f}_seed{args.seed}"

    base_dir = Path("lab/data")
    figures_dir = base_dir / "figures" / subfolder_name
    processed_dir = base_dir / "processed" / subfolder_name
    raw_dir = base_dir / "raw" / subfolder_name

    for d in [figures_dir, processed_dir, raw_dir]:
        d.mkdir(parents=True, exist_ok=True)

    args.output_dir = figures_dir  # For convenience

    if args.mode == 'simple':
        run_mode_simple(args, delta_E_interp)
    elif args.mode == 'sweep':
        run_mode_sweep(args, delta_E_interp)
    elif args.mode == 'fiducial-only':
        run_mode_simple(args, delta_E_interp)  # Same as simple but focused
    else:
        print("Invalid mode. Use --mode simple|sweep|fiducial-only")
        sys.exit(1)

    print("Run complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Final Phase 2 FRW script - consolidated version")
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    parser.add_argument('--mode', type=str, default='simple', choices=['simple', 'sweep', 'fiducial-only'],
                        help='Run mode: simple (fiducial only), sweep (full M_scale), fiducial-only')
    args = parser.parse_args()
    main(args)