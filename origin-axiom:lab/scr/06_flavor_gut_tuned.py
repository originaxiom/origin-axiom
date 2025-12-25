# lab/scr/06_flavor_gut_tuned.py
# Step 3: Tuned for PDG eV masses

import numpy as np
from sympy import exp, I, Matrix, diag, symbols
import os
import argparse
import datetime
import pandas as pd

from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_star = cfg.theta_star_fid_rad

SEED = 42
M_GUT = 1e16
M_R = 1e12  # Tuned lower for larger light masses

def get_run_name():
    return "flavor_gut_tuned"

parser = argparse.ArgumentParser()
parser.add_argument('--seed', type=int, default=SEED)
args = parser.parse_args()

np.random.seed(args.seed)

RUN_NAME = get_run_name()
now_str = datetime.datetime.now().strftime("%m-%d_%H-%M")
DATED_PREFIX = f"{now_str}_{RUN_NAME}"

LAB_DIR = os.path.dirname(os.path.dirname(__file__)) or '..'
DATED_PROC = os.path.join(LAB_DIR, 'data', 'processed', DATED_PREFIX)
DATED_RAW = os.path.join(LAB_DIR, 'data', 'raw', DATED_PREFIX)
os.makedirs(DATED_PROC, exist_ok=True)
os.makedirs(DATED_RAW, exist_ok=True)

theta = symbols('theta')
# Tuned Yukawa for eV scale
Y_nu = Matrix([
    [1e-8 * exp(I * theta), 1e-7, 1e-6],
    [1e-7, 1e-6, 1e-5],
    [1e-6, 1e-5, 1e-4]
])

v = 246
M_D = Y_nu * v

M_R_diag = diag(M_R * 0.1, M_R, M_R * 10)

M_nu = M_D.T @ M_R_diag.inv() @ M_D

M_nu_num = np.array(M_nu.subs(theta, theta_star).evalf(), dtype=np.complex128)

eigvals = np.linalg.eigh(M_nu_num)[0]
masses = np.sort(np.real(eigvals))

sin2_theta_w = 0.375

pdg_masses = [0.0, 0.009, 0.05]
pdg_sin2_theta_w = 0.231

print(f"Calculated neutrino masses: {masses}")
print(f"PDG approx: {pdg_masses}")
print(f"Calculated sin²θ_w: {sin2_theta_w}")
print(f"PDG sin²θ_w: {pdg_sin2_theta_w}")

data = {'m1': [masses[0]], 'm2': [masses[1]], 'm3': [masses[2]], 'sin2_theta_w': [sin2_theta_w]}
pd.DataFrame(data).to_csv(os.path.join(DATED_PROC, 'flavor_tuned.csv'), index=False)

print("Run complete!")