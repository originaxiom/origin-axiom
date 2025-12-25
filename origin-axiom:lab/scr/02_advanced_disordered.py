# grokscr/run_3d_lattice_dynamics_adv.py
# Advanced 3D lattice dynamics for Grok exploration: adds disordered init and nonlinearity
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
N = 30                  # Grid size per dimension (larger for more realism)
STEPS = 2000            # More time steps for evolution
DT = 0.05 / N           # Adjusted for stability with larger N
DX = 1.0                # Lattice spacing
LAMBDA = 0.0            # Nonlinear coupling (0=free; >0 for |phi|^4 interactions)
DISORDERED = False      # Flag for random phase init (True to force dephasing/cancellation)
NOISE_AMP = 0.5         # Noise amplitude for disordered mode (higher=more random)

# Local outputs inside grokscr/
GROK_DIR = os.path.dirname(__file__) or '.'
DATA_DIR = os.path.join(GROK_DIR, 'data')
FIG_DIR = os.path.join(GROK_DIR, 'figs')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

def laplacian_3d(phi):
    lap = (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
           np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) +
           np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2) - 6 * phi) / (DX**2)
    return lap

def potential_deriv(phi, lambda_):
    return 2 * lambda_ * phi * np.abs(phi)**2 if lambda_ > 0 else 0

def initialize_field(N, theta_star, disordered=False, noise_amp=NOISE_AMP):
    volume = N**3
    if disordered:
        # Random phases per site, modulated by theta_star for consistency
        phases = 2 * np.pi * np.random.rand(N, N, N) + theta_star * np.random.rand()  # Base randomness + theta offset
        phi = np.exp(1j * phases)
        noise = noise_amp * (np.random.randn(N, N, N) + 1j * np.random.randn(N, N, N))
    else:
        # Original smooth twist
        x, y, z = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
        phases = theta_star * (x + y + z) / N
        phi = np.exp(1j * phases)
        noise = 0.01 * (np.random.randn(N, N, N) + 1j * np.random.randn(N, N, N))
    
    phi = (phi + noise).astype(np.complex128)
    phi /= np.sqrt(volume)  # Normalize avg |phi|^2 ~1/volume
    pi = np.zeros((N, N, N), dtype=np.complex128)
    return phi, pi

def evolve(phi, pi, steps, dt, epsilon, lambda_, with_constraint=False):
    global_As = []
    energies = []
    volume = phi.size
    constraint_count = 0
    
    for step in range(steps):
        phi_half = phi + 0.5 * dt * pi
        force = laplacian_3d(phi_half) - potential_deriv(phi_half, lambda_)
        pi_new = pi + dt * force
        phi_new = phi_half + 0.5 * dt * pi_new
        
        if with_constraint:
            global_A = np.sum(phi_new)
            min_A = epsilon * np.sqrt(volume)
            if np.abs(global_A) < min_A:
                constraint_count += 1
                phase_dir = global_A / np.abs(global_A) if np.abs(global_A) > 1e-15 else 1.0
                target_A = min_A * phase_dir
                adjustment = (target_A - global_A) / volume
                phi_new += adjustment
        
        phi, pi = phi_new, pi_new
        global_As.append(np.abs(np.sum(phi)))
        
        # Energy: kinetic + gradient + potential
        kin = np.mean(np.abs(pi)**2) / 2
        grad = -np.mean(phi.conj() * laplacian_3d(phi)) / 2  # Approx
        pot = lambda_ * np.mean(np.abs(phi)**4)
        energies.append(kin + grad + pot)
        
        if (step + 1) % 400 == 0:
            print(f"  Step {step+1}/{steps} | |A| = {global_As[-1]:.6f} | Energy density = {energies[-1]:.6f}")
    
    print(f"  Constraint activated {constraint_count} times" if with_constraint else "")
    return np.array(global_As), np.array(energies)

def main(n=N, steps=STEPS, epsilon=EPSILON, lambda_=LAMBDA, disordered=DISORDERED):
    print(f"\n=== Advanced Grok 3D Lattice Dynamics ===")
    print(f"N = {n} (volume = {n**3}), steps = {steps}, epsilon = {epsilon}, lambda = {lambda_}")
    print(f"Disordered init: {disordered}, θ★ = {theta_star:.6f} rad")
    
    phi, pi = initialize_field(n, theta_star, disordered=disordered)
    
    print("Running unconstrained evolution...")
    global_As_no, energies_no = evolve(phi.copy(), pi.copy(), steps, DT, epsilon, lambda_, with_constraint=False)
    
    print("Running constrained evolution (Origin Axiom)...")
    global_As_yes, energies_yes = evolve(phi.copy(), pi.copy(), steps, DT, epsilon, lambda_, with_constraint=True)
    
    # Save data
    dis_str = '_disordered' if disordered else ''
    output_file = os.path.join(DATA_DIR, f'3d_adv_N{n}_steps{steps}_eps{epsilon:.0e}_lam{lambda_:.2f}{dis_str}.npz')
    np.savez(output_file,
             no_constraint_A=global_As_no, no_constraint_E=energies_no,
             with_constraint_A=global_As_yes, with_constraint_E=energies_yes,
             theta_star=theta_star, n=n, steps=steps, epsilon=epsilon, lambda_=lambda_, disordered=disordered)
    print(f"Data saved: {output_file}")
    
    # Plot amplitudes
    plt.figure(figsize=(10, 6))
    plt.plot(global_As_no, label='No Constraint', alpha=0.8)
    plt.plot(global_As_yes, label='With Origin Axiom', alpha=0.8)
    plt.xlabel('Time Step')
    plt.ylabel('Global |A|')
    plt.title(f'3D Advanced Dynamics\nN={n}, θ★≈{theta_star:.3f}, ε={epsilon}, λ={lambda_}, Disordered={disordered}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plot_file_A = os.path.join(FIG_DIR, f'3d_adv_A_N{n}_steps{steps}_eps{epsilon:.0e}{dis_str}.png')
    plt.savefig(plot_file_A, dpi=150)
    plt.close()
    print(f"Amplitude plot: {plot_file_A}")
    
    # Plot energies
    plt.figure(figsize=(10, 6))
    plt.plot(energies_no, label='No Constraint Energy Density', alpha=0.8)
    plt.plot(energies_yes, label='With Origin Axiom Energy Density', alpha=0.8)
    plt.xlabel('Time Step')
    plt.ylabel('Avg Energy Density')
    plt.title(f'Energy Evolution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plot_file_E = os.path.join(FIG_DIR, f'3d_adv_E_N{n}_steps{steps}_eps{epsilon:.0e}{dis_str}.png')
    plt.savefig(plot_file_E, dpi=150)
    plt.close()
    print(f"Energy plot: {plot_file_E}")
    
    print("\nRun complete! Check plots/data in grokscr/.")
    print("For insight: If disordered, expect unconstrained |A| to drop; constrained to hold floor.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advanced Grok 3D lattice simulation')
    parser.add_argument('--n', type=int, default=N, help='Grid size (default: 30)')
    parser.add_argument('--steps', type=int, default=STEPS, help='Time steps (default: 2000)')
    parser.add_argument('--epsilon', type=float, default=EPSILON, help='Constraint factor (default: 1e-3)')
    parser.add_argument('--lambda', type=float, default=LAMBDA, dest='lambda_', help='Nonlinear lambda (default: 0.0)')
    parser.add_argument('--disordered', type=int, default=0, help='1 for disordered init (default: 0)')
    args = parser.parse_args()
    
    main(n=args.n, steps=args.steps, epsilon=args.epsilon, lambda_=args.lambda_,
         disordered=bool(args.disordered))
