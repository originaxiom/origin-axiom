#!/usr/bin/env python3
"""COMPUTED, no data (found by chat1's referee, then checked by chat1 in scratch before this script; labelled so): in
main's B1656 coupling (B1720's instrument at 3412bf09d, unchanged), a flavour-blind Higgs S = 1 gives, in every sector,
    Y = u_1 * 1 + an antisymmetric matrix in (u_i, u_j, u_k),
whatever the line, tau and horocycle, since those enter only through the channel weights u.  The script prints the
coupling for each unit weight, and minimises m2/m3 over all complex channel weights from 300 random starts.
    python3 -B flavour_blind_bound.py      # writes flavour_blind_bound_run.txt"""
import contextlib, importlib.util, io, pathlib
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("tic", HERE.parent / "chat1_2026-10-22_selection_map" / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(tic)
B = tic.B
I2 = np.eye(2, dtype=complex)
LOG = []
for s in B.UNITS:
    u = {k: (1.0 if k == s else 0.0) for k in B.UNITS}
    Y = B.coupling(I2, B.weighted_M(u))
    LOG.append(f"unit weight on '{s}': Y = {np.round(Y.real, 12).astype(int).tolist()} (imaginary part max {np.max(np.abs(Y.imag)):.1e})")


def ratio(v):
    u = dict(zip(B.UNITS, v[:4] + 1j * v[4:]))
    sv = np.linalg.svd(B.coupling(I2, B.weighted_M(u)), compute_uv=False)
    return sv[1] / sv[0]


rng = np.random.default_rng(20261022)
vals = [minimize(ratio, rng.normal(size=8), method="Nelder-Mead",
                 options={"maxiter": 4000, "xatol": 1e-10, "fatol": 1e-12}).fun for _ in range(300)]
LOG.append(f"min over 300 starts of m2/m3 with S = 1: {min(vals):.6f} (median of the local minima {np.median(vals):.4f})")
LOG.append(f"against the data's m_c/m_t = 0.62/168.26 = {0.62 / 168.26:.5f}: at least {min(vals) / (0.62 / 168.26):.0f} times too large")
print("\n".join(LOG))
(HERE / "flavour_blind_bound_run.txt").write_text("\n".join(LOG) + "\n")
