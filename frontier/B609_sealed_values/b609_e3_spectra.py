"""B609-E3 — the spectral hearing amplitudes at kappa = 4, 7, 13
(sealed prereg 0bcc2ad4...). Gates labeled per the prereg; the NEW
values are the kappa = 7 and 13 eigenvalue multisets.
"""
import importlib.util
import math
import os

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def odd_form(level):
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    Cm = np.zeros((n, n))
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1.0
    WRL = T @ (np.linalg.inv(S) @ np.linalg.inv(T) @ S)
    assert np.allclose(Cm @ WRL, WRL @ Cm, atol=1e-9)
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    return -(U.T @ WRL @ U)


def conj_closed(vals, tol=1e-7):
    left = list(vals)
    for v in vals:
        hit = next((i for i, u in enumerate(left)
                    if abs(u - np.conj(v)) < tol), None)
        if hit is None:
            return False
        left.pop(hit)
    return True


phi = (1 + math.sqrt(5)) / 2
ok = True

# GATES (pre-determined from banked facts; labeled as gates)
B4 = odd_form(1)
g = B4.shape == (1, 1) and abs(B4[0, 0] + 1) < 1e-9 and \
    abs(B4[0, 0].imag) < 1e-12
print(f"GATE kappa=4: dim_odd = {B4.shape[0]} (expect 1); amplitude = "
      f"{B4[0,0]:+.9f} (expect -1, REAL — the unit tone is "
      f"chirality-deaf): {g}", flush=True)
ok &= g

B5 = odd_form(2)
l5 = np.linalg.eigvals(B5)
h3 = 1 / (2 * phi) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
g = conj_closed(l5) and abs(np.trace(B5) - 1 / phi) < 1e-9
print(f"GATE kappa=5: trace = {np.trace(B5).real:+.9f} (1/phi); "
      f"spectrum conj-closed: {g}", flush=True)
ok &= g

B10 = odd_form(7)
g = abs(np.trace(B10) - 1 / phi) < 1e-9 and conj_closed(np.linalg.eigvals(B10))
print(f"GATE kappa=10: trace = {np.trace(B10).real:+.9f} (1/phi); "
      f"conj-closed: {g}", flush=True)
ok &= g

# THE NEW VALUES
for kap in (7, 13):
    k = kap - 3
    B = odd_form(k)
    d = B.shape[0]
    nw = (k + 1) * (k + 2) // 2
    nsc = k // 2 + 1
    g_dim = d == (nw - nsc) // 2
    tr = np.trace(B)
    g_tr = abs(tr) < 1e-9                     # the trace law: 0 at 7, 13
    lams = sorted(np.linalg.eigvals(B), key=lambda z: (round(z.real, 9),
                                                       round(z.imag, 9)))
    g_cc = conj_closed(lams)
    print(f"\nkappa={kap}: dim_odd = {d} (formula {(nw-nsc)//2}: {g_dim}); "
          f"trace = {tr.real:+.2e}{tr.imag:+.2e}j (law 0: {g_tr}); "
          f"conj-closed: {g_cc}", flush=True)
    ok &= g_dim and g_tr and g_cc
    # char poly coefficients (real by the law) + rationalization attempt
    cp = np.poly(B)
    print("  char poly coeffs (real parts): "
          + "  ".join(f"{c.real:+.9f}" for c in cp), flush=True)
    for z in lams:
        print(f"    lambda = {z.real:+.9f}{z.imag:+.9f}j   "
              f"|lambda|^2 = {abs(z)**2:.9f}", flush=True)
    # best-effort exact identification of |lambda|^2 values
    for z in lams:
        cand = sp.nsimplify(abs(z) ** 2, [sp.sqrt(5), sp.sqrt(2), sp.sqrt(7),
                                          sp.sqrt(13)], rational=False,
                            tolerance=1e-9)
        if cand is not None and abs(float(cand) - abs(z) ** 2) < 1e-8:
            print(f"    |lambda|^2 = {abs(z)**2:.9f} ~ {cand} (best-effort)",
                  flush=True)

assert ok, "E3 gates failed"
print("\nE3 DONE", flush=True)
