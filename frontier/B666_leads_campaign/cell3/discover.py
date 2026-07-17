"""B666 cell 3 — DISCOVERY pass (floats; the exact pass follows).
E6 level-2 stage landscape: tr_odd(R^{n-2}L), n = 3..40, + general words.
"""
import importlib.util
import os
from fractions import Fraction

import numpy as np

ROOT = _REPO + ""
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(ROOT, "frontier", "B570_allowed_plays",
                       "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

# ---- build the stage (B594's fast pattern) ----
W, eps = c3.weyl_group()
assert len(W) == 51840
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (c3.C @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / c3.KH))
S /= np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S

# exact h-values (Fractions)
C6 = c3.C6
import sympy as sp
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
Cm = sp.Matrix(C6)
Cinv = Cm.inv()
KH = 14
hs_exact = []
rho_vec = Cinv * sp.Matrix([1] * 6)
for p in c3.PRIM:
    lam = Cinv * sp.Matrix(list(p))
    ip = (lam.T * Cm * (lam + 2 * rho_vec))[0, 0]
    hs_exact.append(sp.Rational(ip) / (2 * KH))
cc = sp.Rational(2 * 78, KH)
print("c =", cc, " c/24 =", sp.nsimplify(cc / 24))
for nm, h in zip(c3.NAMES, hs_exact):
    print(f"  h({nm}) = {h}")

T = np.diag([complex(sp.exp(2 * sp.pi * sp.I * (h - cc / 24)).evalf(30))
             for h in hs_exact])

# gates
uni = np.linalg.norm(S @ S.conj().T - np.eye(9))
sym = np.linalg.norm(S - S.T)
C2 = S @ S
rel = np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2)
print(f"gates: unitary {uni:.2e} sym {sym:.2e} (ST)^3-S^2 {rel:.2e}")
assert uni < 1e-9 and sym < 1e-9 and rel < 1e-8

# theta-odd 3-space, B664's convention: R = T, L = S^-1 T^-1 S
pairs = [(1, 2), (3, 4), (7, 8)]
odd = np.zeros((9, 3))
for j, (a, b) in enumerate(pairs):
    odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)

Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
X = Si @ Ti @ S

# T-phases on the odd pairs (exact): alpha_j = h_j - c/24 mod 1
print("\nodd-pair T-phases alpha_j = h_j - 13/28 (mod 1):")
alphas = []
for j, (a, b) in enumerate(pairs):
    al = sp.nsimplify(hs_exact[a] - cc / 24) % 1
    alphas.append(al)
    print(f"  pair {c3.NAMES[a]}: alpha = {al}")
print("phase differences (mod 1):")
for i in range(3):
    for j in range(i + 1, 3):
        print(f"  a{i}-a{j} = {sp.nsimplify(alphas[i]-alphas[j]) % 1}")

# X odd-block diagonal
Bx = odd.T @ X @ odd
print("\nodd block of X = S^-1 T^-1 S:")
for row in Bx:
    print("   [" + "  ".join(f"{z:+.9f}" for z in row) + "]")

# the landscape
print("\nlandscape |tr_odd(R^{n-2}L)|, n = 3..44:")
vals = []
for n in range(3, 45):
    Wm = np.linalg.matrix_power(T, n - 2) @ X
    tr = np.trace(odd.T @ Wm @ odd)
    vals.append((n, abs(tr), tr))
    print(f"  n={n:3d}  |tr_odd| = {abs(tr):.9f}   tr = {tr:+.6f}  "
          f"real: {abs(tr.imag) < 1e-9}")

# distinct values
import collections
uv = sorted({round(v, 9) for _, v, _ in vals})
print("\ndistinct |tr_odd| values:", uv)

# period scan
seq = [v for _, v, _ in vals]
for P in range(1, 30):
    if all(abs(seq[i] - seq[i + P]) < 1e-9 for i in range(len(seq) - P)):
        print(f"modulus period (observed) = {P}")
        break
else:
    print("no period <= 29 in n = 3..44")

# general words
print("\ngeneral words:")
Rm, Lm = T, X
for wname in ["RL", "RLRL", "RRLL", "RRRLLL", "RRRRRRRL", "RLL", "RRL"]:
    M = np.eye(9, dtype=complex)
    for ch in wname:
        M = M @ (Rm if ch == 'R' else Lm)
    tr = np.trace(odd.T @ M @ odd)
    print(f"  {wname:>9}: |tr_odd| = {abs(tr):.9f}  tr = {tr:+.6f}  "
          f"real: {abs(tr.imag) < 1e-9}")

# mod-7 / mod-14 class test: R^P * W vs W
print("\nshift tests |tr_odd(R^P W)| vs |tr_odd(W)|:")
for P in [5, 7, 12, 14, 21, 28, 42, 84]:
    devs = []
    RP = np.linalg.matrix_power(T, P)
    for wname in ["RL", "RLRL", "RRLL", "RRRLLL", "RLL"]:
        M = np.eye(9, dtype=complex)
        for ch in wname:
            M = M @ (Rm if ch == 'R' else Lm)
        d = abs(abs(np.trace(odd.T @ (RP @ M) @ odd))
                - abs(np.trace(odd.T @ M @ odd)))
        devs.append(d)
    print(f"  P={P:3d}: max dev = {max(devs):.3e}")
