"""B616 — THE HELD-OUT CONTROL RUN (one mechanical pass under the sealed
design, sha a11491e6...)."""
import hashlib
import itertools
import math
import os

import importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "HELDOUT_DESIGN.md")
h = hashlib.sha256(open(DESIGN, "rb").read()).hexdigest()
print(f"design hash: {h}")
assert h == "a11491e699333f35b9e59f01f33961f51d3184de67a528043ca65893520fc022"

# ---- HA: the m136 kappa=12 pair-basis hearing diagonals ---------------------
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

k = 12 - 3
w, S, T, cc = b238.su3_data(k)
n = len(w)
Cm = np.zeros((n, n))
for i, wt in enumerate(w):
    Cm[w.index((wt[1], wt[0])), i] = 1.0
R = T
L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
W = R @ R @ L                                   # the m136 weld R^2 L
prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
U = np.zeros((n, len(prs)))
for j, (a, b) in enumerate(prs):
    U[w.index((a, b)), j] = 1 / np.sqrt(2)
    U[w.index((b, a)), j] = -1 / np.sqrt(2)
B = -(U.T @ W @ U)
diags = np.diag(B)
print(f"\nHA: kappa=12, dim_odd = {len(diags)} pair diagonals:", flush=True)
HA = {}
for i, ((a, b), d) in enumerate(zip(prs, diags)):
    print(f"  pair {a},{b}: d = {d:+.9f}  |d|^2 = {abs(d)**2:.9f}  "
          f"Re = {d.real:+.9f}  |arg|/pi = {abs(np.angle(d))/np.pi:.9f}",
          flush=True)
    for tag, val in ((f"|d{i}|^2", abs(d) ** 2), (f"Re d{i}", d.real),
                     (f"|arg d{i}|/pi", abs(np.angle(d)) / np.pi)):
        if 0 < val <= 1:
            HA[tag] = val
print(f"HA family (filtered to (0,1]): {len(HA)} values", flush=True)

# ---- HR: the m136 bundle torsions -------------------------------------------
lam = 2 + sp.sqrt(3)
TORS = {}
for m in (1, 4, 5, 7, 8, 11):
    p = sp.Integer(1)
    for kk in range(0, 2 * m + 1):
        if kk == m:
            continue
        p *= (1 - lam ** (2 * (m - kk)))
    TORS[m] = sp.expand(sp.simplify(p))
print("\nHR: the m136 bundle torsions det'(I - Sym^{2m}(A)):", flush=True)
for m, v in TORS.items():
    print(f"  m={m:2d}: {v}   sign {'+' if v > 0 else '-'}", flush=True)
signs = [1 if TORS[m] > 0 else -1 for m in (1, 4, 5, 7, 8, 11)]
figsign = [(-1) ** m for m in (1, 4, 5, 7, 8, 11)]
print(f"  sign pattern {signs}; the fig-8 law (-1)^m gives {figsign}; "
      f"same: {signs == figsign}", flush=True)
HRvals = {f"|T{b}|/|T{a}|": float(abs(TORS[b] / TORS[a]))
          for a, b in itertools.combinations([1, 4, 5, 7, 8, 11], 2)}

# ---- the grids (identical protocol) ------------------------------------------
T_M = {"sin^2th12": 0.307, "sin^2th23": 0.546, "sin^2th13": 0.0220,
       "lambda_C": 0.22501, "|Vcb|": 0.0408, "|Vub|": 0.00382}
T_H = {"M_GUT/M_Z": 2e16 / 91.1876}
TIERS = (1e-2, 1e-3)

print("\nHG2 — every pair:", flush=True)
k_m136 = 0
npairs = 0
ps = []
for vn, v in HA.items():
    for tn, t in T_M.items():
        dev = abs(v - t) / t
        m1 = dev <= TIERS[0]
        npairs += 1
        ps.append(min(1.0, 2 * TIERS[0] * t))
        if m1:
            k_m136 += 1
            print(f"  {vn:>16s} vs {tn:<12s} v={v:.6g} t={t:.6g} "
                  f"dev={dev:.4f}  <-- MATCH@1e-2", flush=True)
print(f"  ({npairs} pairs evaluated; non-matches suppressed here, ALL "
      f"pairs in the banked raw log)", flush=True)
exp = sum(ps)
print(f"HG2: observed {k_m136} coarse-tier matches of {npairs} pairs "
      f"(expected under null {exp:.2f})", flush=True)

print("\nHG4 — the hierarchy row (data only):", flush=True)
for vn, v in HRvals.items():
    for tn, t in T_H.items():
        dev = abs(math.log10(v / t))
        flag = "  <-- within the half-decade" if dev <= 0.5 else ""
        if dev <= 1.5:
            print(f"  {vn:>14s} v={v:.4g} log10-dev={dev:.3f}{flag}",
                  flush=True)

# ---- the contrast and the verdict --------------------------------------------
nHA = len(HA)
r_fig = 3 / 25
r_m = k_m136 / nHA if nHA else 0.0
print(f"\nCONTRAST: fig-8 rate r = {r_fig:.4f} (3/25); m136 rate r = "
      f"{r_m:.4f} ({k_m136}/{nHA})", flush=True)
if r_m >= r_fig / 2:
    verdict = ("SUGGESTION-DIES: the second object matches at a comparable "
               "per-value rate — the angle windows are generic; the "
               "stopping rule closes the SM-values question at this level")
elif k_m136 == 0:
    rs = 1 / (nHA + 2)
    from math import comb
    pbin = sum(comb(25, j) * rs**j * (1 - rs)**(25 - j) for j in range(3, 26))
    verdict = (f"SPECIFICITY-EVIDENCE (binomial p = {pbin:.4f} < 0.01)"
               if pbin < 0.01 else
               f"STILL-AMBIGUOUS (k_m136 = 0 but binomial p = {pbin:.4f} "
               f">= 0.01)")
else:
    verdict = "STILL-AMBIGUOUS"
print(f"\n==== VERDICT (per the locked table): {verdict} ====", flush=True)
print("B616 DONE", flush=True)
