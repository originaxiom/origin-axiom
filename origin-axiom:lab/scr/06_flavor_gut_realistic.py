# lab/scr/06_flavor_gut_realistic.py
# Step 3: Realistic SO(10)-like Yukawa with θ★, tuned seesaw for eV masses

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
M_GUT = 1e16
M_R = 1e14  # Tuned right-handed scale for eV masses

def get_run_name():
    return "flavor_gut_realistic"

parser = argparse.ArgumentParser(description='Realistic Flavor GUT')
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

# Realistic SO(10)-like Yukawa (toy hierarchical with θ★ phases)
theta = symbols('theta')
Y_u = Matrix([
    [1e-5, 0, 0],
    [0, 1e-3, 0],
    [0, 0, 1]
]) * exp(I * theta / 3)  # Up-type toy

Y_d = Y_u * 0.1  # Down-type smaller

Y_nu = Matrix([
    [1e-6 * exp(I * theta), 1e-5, 1e-4],
    [1e-5, 1e-4, 1e-3],
    [1e-4, 1e-3, 0.01]
])  # Neutrino Dirac

v = 246  # Higgs VEV
M_D = Y_nu * v

M_R_diag = diag(M_R * 1e-2, M_R, M_R * 10)  # Hierarchical right-handed

M_nu = M_D.T @ M_R_diag.inv() @ M_D

M_nu_num = np.array(M_nu.subs(theta, theta_star).evalf(), dtype=np.complex128)

eigvals = np.linalg.eigh(M_nu_num)[0]
masses = np.sort(np.real(eigvals))

sin2_theta_w = 0.375  # GUT value (toy)

pdg_masses = [0.0, 0.009, 0.05]
pdg_sin2_theta_w = 0.231

print(f"Calculated neutrino masses: {masses}")
print(f"PDG approx: {pdg_masses}")
print(f"Calculated sin²θ_w: {sin2_theta_w}")
print(f"PDG sin²θ_w: {pdg_sin2_theta_w}")

data = {'m1': [masses[0]], 'm2': [masses[1]], 'm3': [masses[2]], 'sin2_theta_w': [sin2_theta_w]}
pd.DataFrame(data).to_csv(os.path.join(DATED_PROC, 'flavor_realistic.csv'), index=False)

print("Run complete!")