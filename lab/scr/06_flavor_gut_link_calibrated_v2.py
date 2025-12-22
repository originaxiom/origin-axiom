# grokscr/scr/06_flavor_gut_link_calibrated_v2.py
# Step 3: Calibrated Flavor - Add seesaw for eV masses

import numpy as np
from sympy import sin, cos, exp, I, Matrix, diag, symbols
import os
import argparse
import datetime
import pandas as pd

from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_star = cfg.theta_star_fid_rad

# Defaults
SEED = 42
DIM_Y = 3
M_GUT = 1e16
M_R = M_GUT  # Right-handed neutrino scale for seesaw

def get_run_name():
    return "flavor_gut_link_calibrated_v2"

parser = argparse.ArgumentParser(description='Calibrated Flavor GUT Link v2')
parser.add_argument('--seed', type=int, default=SEED)
args = parser.parse_args()

np.random.seed(args.seed)

RUN_NAME = get_run_name()
now_str = datetime.datetime.now().strftime("%m-%d_%H-%M")
DATED_PREFIX = f"{now_str}_{RUN_NAME}"

GROK_DIR = os.path.dirname(os.path.dirname(__file__)) or '..'
DATED_PROC = os.path.join(GROK_DIR, 'data', 'processed', DATED_PREFIX)
DATED_RAW = os.path.join(GROK_DIR, 'data', 'raw', DATED_PREFIX)
os.makedirs(DATED_PROC, exist_ok=True)
os.makedirs(DATED_RAW, exist_ok=True)

# Toy Yukawa matrix Y modulated by θ★ phases
theta = symbols('theta')
Y = Matrix([
    [1, 0.1 * exp(I * theta), 0.01 * exp(2*I * theta)],
    [0.1 * exp(I * theta), 0.5, 0.05 * exp(I * theta)],
    [0.01 * exp(2*I * theta), 0.05 * exp(I * theta), 0.2]
])

# Dirac mass matrix M_D = Y v (v ~246 GeV Higgs VEV, scaled)
v = 246
M_D = Y * v

# Seesaw: M_ν = M_D^T M_R^{-1} M_D (M_R right-handed matrix)
M_R_toy = diag(M_R, M_R, M_R)  # Toy diagonal

M_nu = M_D.T @ M_R_toy.inv() @ M_D

# Numerical eval
M_nu_num = np.array(M_nu.subs(theta, theta_star).evalf(), dtype=np.complex128)

# Diagonalize
eigvals, eigvecs = np.linalg.eigh(M_nu_num)
masses = np.sort(np.real(eigvals))  # eV scale

# sin²θ_w toy from GUT
sin2_theta_w = 3/8 * (1 - (masses[2]**2 / M_GUT**2))

# PDG
pdg_masses = [0.0, 0.009, 0.05]
pdg_sin2_theta_w = 0.231

print(f"Calculated neutrino masses: {masses}")
print(f"PDG approx: {pdg_masses}")
print(f"Calculated sin²θ_w: {sin2_theta_w}")
print(f"PDG sin²θ_w: {pdg_sin2_theta_w}")

# Save CSV
data = {'m1': [masses[0]], 'm2': [masses[1]], 'm3': [masses[2]], 'sin2_theta_w': [sin2_theta_w]}
df = pd.DataFrame(data)
df.to_csv(os.path.join(DATED_PROC, 'flavor_results_calibrated.csv'), index=False)

print("Run complete! Check dated folders.")