# grokscr/scr/03_scaling_tests.py
# Full main script with dated structured outputs

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import datetime

from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_star = cfg.theta_star_fid_rad

# Defaults (will override with args for naming)
DEFAULT_N = 30
DEFAULT_EPS = 1e-3
DEFAULT_LAM = 0.0
DEFAULT_DIS = True

def get_run_name(n, eps, lam, dis):
    return f"grok_3d_N{n}_eps{eps:.0e}_dis{int(dis)}_lam{lam:.2f}"

# Parse args first for naming
parser = argparse.ArgumentParser(description='Grok 3D scaling tests')
parser.add_argument('--n', type=int, default=DEFAULT_N)
parser.add_argument('--steps', type=int, default=2000)
parser.add_argument('--epsilon', type=float, default=DEFAULT_EPS)
parser.add_argument('--lambda', type=float, default=DEFAULT_LAM, dest='lam')
parser.add_argument('--disordered', type=int, default=1)
parser.add_argument('--seed', type=int, default=None)
args = parser.parse_args()

# Dynamic run name using actual args
RUN_NAME = get_run_name(args.n, args.epsilon, args.lam, bool(args.disordered))
now_str = datetime.datetime.now().strftime("%m-%d_%H-%M")
DATED_PREFIX = f"{now_str}_{RUN_NAME}"

GROK_DIR = os.path.dirname(os.path.dirname(__file__)) or '..'
DATED_FIG = os.path.join(GROK_DIR, 'data', 'figures', DATED_PREFIX)
DATED_PROC = os.path.join(GROK_DIR, 'data', 'processed', DATED_PREFIX)
DATED_RAW = os.path.join(GROK_DIR, 'data', 'raw', DATED_PREFIX)

os.makedirs(DATED_FIG, exist_ok=True)
os.makedirs(DATED_PROC, exist_ok=True)
os.makedirs(DATED_RAW, exist_ok=True)

DT = 0.05 / args.n
NOISE_AMP = 0.5

def laplacian_3d(phi):
    lap = (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
           np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) +
           np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2) - 6 * phi)
    return lap

def potential_deriv(phi, lam):
    return 2 * lam * phi * np.abs(phi)**2 if lam > 0 else 0

def initialize_field(n, theta_star, disordered=True, noise_amp=NOISE_AMP):
    volume = n**3
    if disordered:
        phases = 2 * np.pi * np.random.rand(n, n, n) + theta_star * np.random.rand()
        phi = np.exp(1j * phases)
        noise = noise_amp * (np.random.randn(n, n, n) + 1j * np.random.randn(n, n, n))
    else:
        x, y, z = np.meshgrid(np.arange(n), np.arange(n), np.arange(n), indexing='ij')
        phases = theta_star * (x + y + z) / n
        phi = np.exp(1j * phases)
        noise = 0.01 * (np.random.randn(n, n, n) + 1j * np.random.randn(n, n, n))
    
    phi = (phi + noise).astype(np.complex128) / np.sqrt(volume)
    pi = np.zeros((n, n, n), dtype=np.complex128)
    return phi, pi

def evolve(phi, pi, steps, dt, epsilon, lam, with_constraint=False):
    global_As = []
    energies = []
    volume = phi.size
    constraint_count = 0
    
    for step in range(steps):
        phi_half = phi + 0.5 * dt * pi
        force = laplacian_3d(phi_half) - potential_deriv(phi_half, lam)
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
        
        # Approx energy
        kin = 0.5 * np.mean(np.abs(pi)**2)
        grad = -0.5 * np.real(np.mean(np.conj(phi) * laplacian_3d(phi)))
        pot = lam * np.mean(np.abs(phi)**4)
        energies.append(kin + grad + pot)
        
        if (step + 1) % 400 == 0:
            print(f"  Step {step+1}/{steps} | |A| = {global_As[-1]:.6f}")
    
    if with_constraint:
        print(f"  Constraint activated {constraint_count} times")
    return np.array(global_As), np.array(energies), constraint_count

# Main run
if args.seed is not None:
    np.random.seed(args.seed)

print(f"\n=== Grok 3D Scaling Test ===")
print(f"Folder: {DATED_PREFIX}")
print(f"Params: N={args.n}, ε={args.epsilon}, λ={args.lam}, disordered={bool(args.disordered)}, θ★={theta_star:.6f}")

phi, pi = initialize_field(args.n, theta_star, bool(args.disordered))

print("Unconstrained...")
As_no, Es_no, _ = evolve(phi.copy(), pi.copy(), args.steps, DT, args.epsilon, args.lam, False)

print("Constrained...")
As_yes, Es_yes, count = evolve(phi.copy(), pi.copy(), args.steps, DT, args.epsilon, args.lam, True)

# Save raw
np.savez(os.path.join(DATED_RAW, 'data.npz'), As_no=As_no, Es_no=Es_no, As_yes=As_yes, Es_yes=Es_yes, params=vars(args))

# Plots
for name, data_no, data_yes in [('amplitude', As_no, As_yes), ('energy', Es_no, Es_yes)]:
    plt.figure(figsize=(10,6))
    plt.plot(data_no, label='No Constraint')
    plt.plot(data_yes, label='With Origin Axiom')
    plt.title(f'{name.capitalize()} – {RUN_NAME}')
    plt.xlabel('Time Step')
    plt.ylabel('|A|' if name == 'amplitude' else 'Energy Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    for ext in ['.png', '.pdf']:
        plt.savefig(os.path.join(DATED_FIG, f'{name}{ext}'), dpi=200, bbox_inches='tight')
    plt.close()

print(f"Outputs in data/figures/{DATED_PREFIX}, data/raw/{DATED_PREFIX}, etc.")
print("Update PROGRESS_LOG.md with results!")