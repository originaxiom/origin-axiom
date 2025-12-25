# grokscr/run_3d_lattice_dynamics_grok.py
# Standalone 3D lattice dynamics script for Grok exploration
# Saves everything inside grokscr/ — no interference with main repo

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

# Import theta_star from your main src (requires PYTHONPATH=src)
from theta_star_config import load_theta_star_config

# Load theta_star
cfg = load_theta_star_config()
theta_star = cfg.theta_star_fid_rad

# Default parameters
EPSILON = 1e-3          # Constraint strength (relative to sqrt(volume))
N = 20                  # Grid size per dimension (N^3 sites)
STEPS = 1000            # Number of time steps
DT = 0.1 / N            # Time step for stability
DX = 1.0                # Lattice spacing

# Local output directories inside grokscr/
GROK_DIR = os.path.dirname(__file__) or '.'  # Current script directory
DATA_DIR = os.path.join(GROK_DIR, 'data')
FIG_DIR = os.path.join(GROK_DIR, 'figs')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

def laplacian_3d(phi):
    """Finite difference Laplacian in 3D with periodic boundaries."""
    lap = (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
           np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) +
           np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2) - 6 * phi) / (DX**2)
    return lap

def initialize_field(N, theta_star):
    """Initialize complex scalar field with θ★-modulated phase twist."""
    x, y, z = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    phase = theta_star * (x + y + z) / N
    phi = np.exp(1j * phase)
    # Add small random noise to break perfect coherence and encourage dynamics
    noise = 0.01 * (np.random.randn(N, N, N) + 1j * np.random.randn(N, N, N))
    phi = phi + noise
    phi = phi.astype(np.complex128)
    
    # Normalize so average |phi| per site ~ 1/sqrt(volume)
    volume = N**3
    phi /= np.sqrt(volume)
    
    pi = np.zeros((N, N, N), dtype=np.complex128)  # Initial momentum = 0
    return phi, pi

def evolve(phi, pi, steps, dt, epsilon, with_constraint=False):
    """Leapfrog time evolution with optional Origin Axiom constraint."""
    global_As = []
    volume = phi.size
    
    for step in range(steps):
        # Leapfrog steps
        phi_half = phi + 0.5 * dt * pi
        pi_new = pi + dt * laplacian_3d(phi_half)
        phi_new = phi_half + 0.5 * dt * pi_new
        
        if with_constraint:
            global_A = np.sum(phi_new)
            min_A = epsilon * np.sqrt(volume)
            if np.abs(global_A) < min_A:
                # Enforce minimum |A| while preserving approximate phase direction
                phase_dir = global_A / np.abs(global_A) if np.abs(global_A) > 1e-15 else 1.0
                target_A = min_A * phase_dir
                adjustment = (target_A - global_A) / volume
                phi_new += adjustment
        
        phi, pi = phi_new, pi_new
        global_As.append(np.abs(np.sum(phi)))
        
        # Optional progress print every 200 steps
        if (step + 1) % 200 == 0:
            print(f"  Step {step+1}/{steps} | |A| = {global_As[-1]:.6f}")
    
    return np.array(global_As)

def main(n=N, steps=STEPS, epsilon=EPSILON):
    print(f"\n=== Grok 3D Lattice Dynamics ===")
    print(f"N = {n} (volume = {n**3}), steps = {steps}, epsilon = {epsilon}")
    print(f"θ★ = {theta_star:.6f} rad")
    
    phi, pi = initialize_field(n, theta_star)
    
    print("Running unconstrained evolution...")
    global_As_no = evolve(phi.copy(), pi.copy(), steps, DT, epsilon, with_constraint=False)
    
    print("Running constrained evolution (Origin Axiom)...")
    global_As_yes = evolve(phi.copy(), pi.copy(), steps, DT, epsilon, with_constraint=True)
    
    # Save data
    output_file = os.path.join(DATA_DIR, f'3d_dynamics_N{n}_steps{steps}_eps{epsilon:.0e}.npz')
    np.savez(output_file,
             no_constraint=global_As_no,
             with_constraint=global_As_yes,
             theta_star=theta_star,
             n=n, steps=steps, epsilon=epsilon)
    print(f"Data saved: {output_file}")
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(global_As_no, label='No Constraint (free evolution)', alpha=0.8)
    plt.plot(global_As_yes, label='With Origin Axiom Constraint', alpha=0.8)
    plt.xlabel('Time Step')
    plt.ylabel('Global Amplitude |A| = |∑ φ|')
    plt.title(f'3D Lattice Dynamics\nN={n}, θ★ ≈ {theta_star:.3f}, ε={epsilon}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plot_file = os.path.join(FIG_DIR, f'3d_global_A_N{n}_steps{steps}_eps{epsilon:.0e}.png')
    plt.savefig(plot_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved: {plot_file}")
    
    print("\nRun complete! All files are in grokscr/ — safe from your main workflow.")
    print("Share the plot (figs/*.png) or describe the final |A| values, and we'll analyze the insight.\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Grok standalone 3D lattice simulation')
    parser.add_argument('--n', type=int, default=N, help='Grid size per dimension (default: 20)')
    parser.add_argument('--steps', type=int, default=STEPS, help='Number of time steps (default: 1000)')
    parser.add_argument('--epsilon', type=float, default=EPSILON, help='Constraint threshold factor (default: 1e-3)')
    args = parser.parse_args()
    
    main(n=args.n, steps=args.steps, epsilon=args.epsilon)