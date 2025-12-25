# grokscr/scr/04_frw_embedding.py
# FRW-embedded 3D lattice dynamics with Origin Axiom constraint
# Adds expanding scale factor a(t), coupled to field energy

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import datetime

from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_star = cfg.theta_star_fid_rad

# Defaults
EPSILON = 1e-2  # Start higher for visible effects
N = 20          # Smaller N for FRW (computational cost)
STEPS = 5000    # Longer evolution for cosmic time
DT = 0.05 / N   # Base timestep
DX = 1.0
LAMBDA = 0.0
DISORDERED = True
NOISE_AMP = 0.5
SEED = None
H0 = 1e-3       # Initial Hubble-like parameter (tuned for toy scale)
G = 1.0         # Toy gravitational constant (dimensionless units)

def get_run_name(n, eps, lam, dis):
    return f"frw_3d_N{n}_eps{eps:.0e}_dis{int(dis)}_lam{lam:.2f}"

parser = argparse.ArgumentParser(description='Grok FRW-embedded simulation')
parser.add_argument('--n', type=int, default=N)
parser.add_argument('--steps', type=int, default=STEPS)
parser.add_argument('--epsilon', type=float, default=EPSILON)
parser.add_argument('--lambda', type=float, default=LAMBDA, dest='lam')
parser.add_argument('--disordered', type=int, default=1)
parser.add_argument('--seed', type=int, default=SEED)
args = parser.parse_args()

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

DT = 0.05 / args.n  # Adjust if needed

def laplacian_3d(phi):
    lap = (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
           np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) +
           np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2) - 6 * phi) / DX**2
    return lap

def potential_deriv(phi, lam):
    return 2 * lam * phi * np.abs(phi)**2 if lam > 0 else 0

def initialize_field(n, theta_star, disordered=DISORDERED, noise_amp=NOISE_AMP):
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

def evolve_frw(phi, pi, a, steps, dt, epsilon, lam, with_constraint=False):
    global_As = []
    energies = []
    scale_factors = [a]
    Hs = []
    constraint_count = 0
    
    for step in range(steps):
        # Compute current H from Friedmann (toy: rho from field energy)
        kin = 0.5 * np.mean(np.abs(pi)**2)
        grad = -0.5 * np.real(np.mean(np.conj(phi) * laplacian_3d(phi)))
        pot = lam * np.mean(np.abs(phi)**4)
        rho = kin + grad + pot  # Energy density
        H = np.sqrt(8 * np.pi * G * rho / 3) + H0  # Minimal H0 to drive expansion
        
        # Field evolution with Hubble friction
        phi_half = phi + 0.5 * dt * pi
        force = laplacian_3d(phi_half) - potential_deriv(phi_half, lam)
        pi_new = pi + dt * force - 3 * H * dt * phi_half  # Friction term
        phi_new = phi_half + 0.5 * dt * pi_new
        
        # Volume scales with a^3
        volume = args.n**3 * a**3
        if with_constraint:
            global_A = np.sum(phi_new) * a**(3/2)  # Conformal rescaling for amplitude
            min_A = epsilon * np.sqrt(volume)
            if np.abs(global_A) < min_A:
                constraint_count += 1
                phase_dir = global_A / np.abs(global_A) if np.abs(global_A) > 1e-15 else 1.0
                target_A = min_A * phase_dir
                adjustment = (target_A - global_A) / volume
                phi_new += adjustment / a**(3/2)  # Back-rescale
        
        phi, pi = phi_new, pi_new
        
        # Update scale factor
        a_new = a + dt * H * a
        a = a_new
        
        global_As.append(np.abs(np.sum(phi)) * a**(3/2))  # Effective |A| in comoving volume
        energies.append(rho)
        scale_factors.append(a)
        Hs.append(H)
        
        if (step + 1) % 1000 == 0:
            print(f"  Step {step+1}/{steps} | |A|_eff = {global_As[-1]:.6f} | a = {a:.6f} | H = {H:.6f}")
    
    if with_constraint:
        print(f"  Constraint activated {constraint_count} times")
    return np.array(global_As), np.array(energies), np.array(scale_factors), np.array(Hs), constraint_count

if args.seed is not None:
    np.random.seed(args.seed)

print(f"\n=== Grok FRW-Embedded Test ===")
print(f"Folder: {DATED_PREFIX}")
print(f"Params: N={args.n}, ε={args.epsilon}, λ={args.lam}, disordered={bool(args.disordered)}, θ★={theta_star:.6f}")

phi, pi = initialize_field(args.n, theta_star, bool(args.disordered))
a_init = 1.0  # Initial scale factor

print("Unconstrained...")
As_no, Es_no, as_no, Hs_no, _ = evolve_frw(phi.copy(), pi.copy(), a_init, args.steps, DT, args.epsilon, args.lam, False)

print("Constrained...")
As_yes, Es_yes, as_yes, Hs_yes, count = evolve_frw(phi.copy(), pi.copy(), a_init, args.steps, DT, args.epsilon, args.lam, True)

# Save raw
np.savez(os.path.join(DATED_RAW, 'data.npz'), As_no=As_no, Es_no=Es_no, as_no=as_no, Hs_no=Hs_no, 
         As_yes=As_yes, Es_yes=Es_yes, as_yes=as_yes, Hs_yes=Hs_yes, params=vars(args))

# Plots
for name, data_no, data_yes in [('amplitude_eff', As_no, As_yes), ('energy_density', Es_no, Es_yes),
                                ('scale_factor', as_no, as_yes), ('hubble', Hs_no, Hs_yes)]:
    plt.figure(figsize=(10,6))
    plt.plot(data_no, label='No Constraint')
    plt.plot(data_yes, label='With Origin Axiom')
    plt.title(f'{name.capitalize().replace("_", " ")} – {RUN_NAME}')
    plt.xlabel('Time Step')
    plt.ylabel(name.upper().replace("_EFF", " (effective)"))
    plt.legend()
    plt.grid(True, alpha=0.3)
    for ext in ['.png', '.pdf']:
        plt.savefig(os.path.join(DATED_FIG, f'{name}{ext}'), dpi=200, bbox_inches='tight')
    plt.close()

print(f"Outputs in data/figures/{DATED_PREFIX}, etc.")
print("Update PROGRESS_LOG.md with results!")