# grokscr/scr/05_gut_adjoint_toy.py
# Step 1: Multi-field SU(5)-like adjoint scalar Φ (24-dim toy)
# Potential V = λ Tr(Φ^4), axiom on Tr(Φ) ≠ 0, θ★ phase modulation

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import datetime

from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_star = cfg.theta_star_fid_rad

# Defaults
EPSILON = 1e-2
N = 10                  # Small lattice for 24x24 matrices (memory intensive)
STEPS = 2000
DT = 0.05 / N
DX = 1.0                # Lattice spacing (fixed the missing definition)
LAMBDA = 0.1            # Nonlinear coupling
DISORDERED = True
SEED = 42
DIM = 24                # SU(5) adjoint dimension

def get_run_name(n, eps, lam):
    return f"gut_toy_N{n}_eps{eps:.0e}_lam{lam:.2f}"

parser = argparse.ArgumentParser(description='GUT Adjoint Toy Model')
parser.add_argument('--n', type=int, default=N)
parser.add_argument('--steps', type=int, default=STEPS)
parser.add_argument('--epsilon', type=float, default=EPSILON)
parser.add_argument('--lambda', type=float, default=LAMBDA, dest='lam')
parser.add_argument('--disordered', type=int, default=1)
parser.add_argument('--seed', type=int, default=SEED)
args = parser.parse_args()

np.random.seed(args.seed)

RUN_NAME = get_run_name(args.n, args.epsilon, args.lam)
now_str = datetime.datetime.now().strftime("%m-%d_%H-%M")
DATED_PREFIX = f"{now_str}_{RUN_NAME}"

GROK_DIR = os.path.dirname(os.path.dirname(__file__)) or '..'
DATED_FIG = os.path.join(GROK_DIR, 'data', 'figures', DATED_PREFIX)
DATED_RAW = os.path.join(GROK_DIR, 'data', 'raw', DATED_PREFIX)
os.makedirs(DATED_FIG, exist_ok=True)
os.makedirs(DATED_RAW, exist_ok=True)

# Initialize adjoint scalar Φ (complex Hermitian 24x24 matrices on lattice)
volume = args.n**3
phi = np.zeros((args.n, args.n, args.n, DIM, DIM), dtype=np.complex128)
pi = np.zeros_like(phi)

# Disordered init with θ★ phase modulation
if args.disordered:
    for i in range(DIM):
        for j in range(DIM):
            phase = theta_star * np.random.rand(args.n, args.n, args.n)
            magnitude = np.random.rand(args.n, args.n, args.n)
            phi[..., i, j] = magnitude * np.exp(1j * phase)
            if i != j:
                phi[..., j, i] = np.conj(phi[..., i, j])  # Hermitian
else:
    x, y, z = np.meshgrid(np.arange(args.n), np.arange(args.n), np.arange(args.n), indexing='ij')
    phase = theta_star * (x + y + z) / args.n
    phi = np.exp(1j * phase)[..., np.newaxis, np.newaxis] * np.eye(DIM)

phi /= np.sqrt(volume * DIM**2)  # Normalize

def laplacian_adj(phi):
    lap = np.zeros_like(phi)
    for ax in range(3):
        lap += np.roll(phi, 1, axis=ax) + np.roll(phi, -1, axis=ax)
    lap -= 6 * phi
    return lap / (DX**2)

def potential_deriv_adj(phi, lam):
    # V = λ Tr(Φ^4) derivative
    phi_mat = phi.reshape(-1, DIM, DIM)  # Flatten lattice
    phi2 = phi_mat @ phi_mat
    phi3 = phi2 @ phi_mat
    dV_dPhi = 4 * lam * (phi3 @ phi_mat)
    return dV_dPhi.reshape(phi.shape)

def evolve_gut(phi, pi, steps, dt, epsilon, lam, with_constraint=False):
    traces = []
    energies = []
    constraint_count = 0

    for step in range(steps):
        phi_half = phi + 0.5 * dt * pi
        force = laplacian_adj(phi_half) - potential_deriv_adj(phi_half, lam)
        pi_new = pi + dt * force
        phi_new = phi_half + 0.5 * dt * pi_new

        if with_constraint:
            tr_phi = np.trace(phi_new, axis1=-2, axis2=-1)
            global_tr = np.sum(tr_phi)
            min_tr = epsilon * np.sqrt(volume)
            if np.abs(global_tr) < min_tr:
                constraint_count += 1
                phase_dir = global_tr / np.abs(global_tr) if np.abs(global_tr) > 1e-15 else 1.0
                target_tr = min_tr * phase_dir
                adjustment = (target_tr - global_tr) / (volume * DIM)
                phi_new += adjustment * np.eye(DIM)

        phi, pi = phi_new, pi_new

        current_tr = np.abs(np.sum(np.trace(phi, axis1=-2, axis2=-1)))
        traces.append(current_tr)

        kin = 0.5 * np.mean(np.abs(pi)**2)
        grad = -0.5 * np.real(np.mean(np.conj(phi) * laplacian_adj(phi)))
        pot = lam * np.mean(np.real(np.trace(phi @ phi @ phi @ phi, axis1=-2, axis2=-1)))
        energies.append(kin + grad + pot)

        if (step + 1) % 500 == 0:
            print(f"  Step {step+1}/{steps} | |Tr(Φ)| = {current_tr:.6f}")

    if with_constraint:
        print(f"  Constraint activated {constraint_count} times")
    return np.array(traces), np.array(energies), constraint_count

print(f"\n=== GUT Adjoint Toy Model ===")
print(f"Folder: {DATED_PREFIX}")
print(f"N={args.n}, ε={args.epsilon}, λ={args.lam}, θ★={theta_star:.6f}")

print("Unconstrained...")
tr_no, e_no, _ = evolve_gut(phi.copy(), pi.copy(), args.steps, DT, args.epsilon, args.lam, False)

print("Constrained...")
tr_yes, e_yes, count = evolve_gut(phi.copy(), pi.copy(), args.steps, DT, args.epsilon, args.lam, True)

# Save & Plot
np.savez(os.path.join(DATED_RAW, 'data.npz'), tr_no=tr_no, e_no=e_no, tr_yes=tr_yes, e_yes=e_yes)

plt.figure(figsize=(10,6))
plt.plot(tr_no, label='No Constraint |Tr(Φ)|')
plt.plot(tr_yes, label='With Origin Axiom |Tr(Φ)|')
plt.title(f'GUT Adjoint Trace – {RUN_NAME}')
plt.xlabel('Time Step')
plt.ylabel('|Tr(Φ)|')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(DATED_FIG, 'trace.png'), dpi=200)
plt.savefig(os.path.join(DATED_FIG, 'trace.pdf'))
plt.close()

plt.figure(figsize=(10,6))
plt.plot(e_no, label='No Constraint Energy')
plt.plot(e_yes, label='With Axiom Energy')
plt.title(f'Energy – {RUN_NAME}')
plt.xlabel('Time Step')
plt.ylabel('Energy Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(DATED_FIG, 'energy.png'), dpi=200)
plt.savefig(os.path.join(DATED_FIG, 'energy.pdf'))
plt.close()

print("Run complete! Check dated folders.")