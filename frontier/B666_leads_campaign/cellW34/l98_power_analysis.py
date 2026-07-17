"""L98 falsifier — POWER ANALYSIS (B666 cell W3-4; post-seal, controls +
banked data + selftest only; NO target-grid point is computed).

P1  noise floor of the decision functionals g and l1 (perturbation runs).
P2  ordinal depth-stability of g at 8 control kappas (the only remaining
    noise channel = finite-size flapping).
P3  MB12 vacuity of the sealed criterion (l98_falsifier --selftest).
P4  the banked-data dry run: R3's banked coarse curves (box_dim d14 vs the
    exact g @F1597) — valley/argmax alignment + the notch regression.
"""
import json
import subprocess
import sys
import time

import numpy as np

from l98_lib import provenance_gate, metallic_word, spectrum, gap_labels

provenance_gate()
print("provenance gate PASS")

CONTROLS = (0.55, 0.60, 0.65, 0.70, 1.60, 1.65, 1.70, 1.90)
DEPTHS = (13, 14, 15)
R3_JSON = ("../../B646_wave2_integration/cc2_packets/residuals/"
           "residuals_loop/r3_peak/r3_results.json")


def g_and_label(ev):
    top, ratio = gap_labels(ev, top=5)
    P = np.c_[ev.real, ev.imag]
    dm = float(np.hypot(P[:, 0].max() - P[:, 0].min(),
                        P[:, 1].max() - P[:, 1].min()))
    return top[0][0] / dm, top[0][2], top[0][1], ratio, top


# ---------------------------------------------------------------- P1 + P2
print("\n== P1/P2: exact functionals at 8 controls x depths 13/14/15 ==")
print(f"{'kappa':>6} {'depth':>5} {'g=mst/diam':>11} {'label':>8} {'ns':>5} "
      f"{'e2/e1':>7}")
G = {}
LBL = {}
for kap in CONTROLS:
    mu = np.sqrt(2.0 - kap)
    for d in DEPTHS:
        t0 = time.time()
        ev = spectrum(metallic_word(d, 1), 1j * mu, periodic=True)
        g, lab, ns, ratio, top = g_and_label(ev)
        G[(kap, d)] = g
        LBL[(kap, d)] = lab
        print(f"{kap:6.2f} {d:5d} {g:11.6f} {lab:8.5f} {ns:5d} {ratio:7.4f}"
              f"   ({time.time()-t0:.1f}s)")

print("\nP1a  label depth-scatter per control (max pairwise |dx|):")
worst_lbl = 0.0
for kap in CONTROLS:
    xs = [LBL[(kap, d)] for d in DEPTHS]
    sc = max(xs) - min(xs)
    worst_lbl = max(worst_lbl, sc)
    print(f"  kappa={kap:.2f}: {sc:.2e}")
print(f"  WORST label depth-scatter: {worst_lbl:.2e} "
      f"(adjacent phi-hierarchy labels differ by >= 0.09)")

print("\nP1b  perturbation floor of g (1e-10 eigenvalue noise, 5 seeds, "
      "2 controls x depth 14):")
worst_dg = 0.0
for kap in (0.60, 1.90):
    mu = np.sqrt(2.0 - kap)
    ev = spectrum(metallic_word(14, 1), 1j * mu, periodic=True)
    g0, lab0, ns0, _, _ = g_and_label(ev)
    for seed in range(5):
        rng = np.random.default_rng(seed)
        pert = ev + (rng.normal(size=len(ev)) +
                     1j * rng.normal(size=len(ev))) * 1e-10
        g1, lab1, ns1, _, _ = g_and_label(pert)
        worst_dg = max(worst_dg, abs(g1 - g0))
        assert ns1 == ns0, "label flipped under 1e-10 perturbation"
    print(f"  kappa={kap:.2f}: max |dg| over 5 seeds = {worst_dg:.2e}, "
          f"label invariant")
print(f"  => measurement noise of g: {worst_dg:.2e}  "
      f"(N3's jitter floor on box_dim was 1.4e-2 — "
      f"{1.4e-2/worst_dg:.1e} times larger)")

print("\nP2  ordinal depth-stability of g at the controls "
      "(the flapping channel):")
lo = [k for k in CONTROLS if k < 1.0]
hi = [k for k in CONTROLS if k > 1.0]
consist = 0
total = 0
for side in (lo, hi):
    for a, b in zip(side, side[1:]):
        signs = [np.sign(G[(b, d)] - G[(a, d)]) for d in DEPTHS]
        ok = len(set(signs)) == 1
        consist += ok
        total += 1
        print(f"  sign(g({b:.2f})-g({a:.2f})) by depth: "
              f"{[int(s) for s in signs]}  depth-consistent: {ok}")
p_flap = 1 - consist / total
print(f"  ordinal depth-consistency: {consist}/{total} "
      f"(flapping rate {p_flap:.2f})")

print("\nP2b  magnitude: adjacent-control |dg| vs the perturbation floor:")
dgs = []
for side in (lo, hi):
    for a, b in zip(side, side[1:]):
        dgs.append(min(abs(G[(b, d)] - G[(a, d)]) for d in DEPTHS))
print(f"  min adjacent |dg| across controls/depths: {min(dgs):.2e}; "
      f"floor {worst_dg:.2e}; ratio {min(dgs)/max(worst_dg,1e-300):.1e}")

# ---------------------------------------------------------------- P3
print("\n== P3: MB12 vacuity — the sealed criterion can pass AND fail ==")
r = subprocess.run([sys.executable, "l98_falsifier.py", "--selftest"],
                   capture_output=True, text=True)
print(r.stdout.rstrip())
assert r.returncode == 0, r.stderr

# ---------------------------------------------------------------- P4
print("\n== P4: the banked-data dry run (no fresh target points) ==")
with open(R3_JSON) as fh:
    r3 = json.load(fh)
ks = r3["fine_grid_kappas"]
gscan = r3["scan_mst_gap_F1597"]["values"]
bd = {float(k): v["box_dim_depth14"] for k, v in r3["fine_rows"].items()}
bvals = [bd[k] for k in ks]
plateau = [i for i, k in enumerate(ks) if 0.8 <= k <= 1.5]
print("  banked g @F1597 :", [round(gscan[i], 5) for i in plateau])
print("  banked box_dim14:", [round(bvals[i], 5) for i in plateau])
ig = max(plateau, key=lambda i: gscan[i])
# box_dim valley strictly inside the plateau
interior = plateau[1:-1]
iv = min(interior, key=lambda i: bvals[i])
print(f"  argmax g = kappa {ks[ig]};  box_dim interior valley = kappa {ks[iv]}"
      f";  offset = {abs(ig - iv)} coarse step(s)")
# the notch regression: box_dim ~ a + b*kappa + c*g on the plateau
X = np.c_[np.ones(len(plateau)), [ks[i] for i in plateau],
          [gscan[i] for i in plateau]]
y = np.array([bvals[i] for i in plateau])
coef, res, *_ = np.linalg.lstsq(X, y, rcond=None)
fit = X @ coef
resid = y - fit
print(f"  notch regression box_dim ~ a + b*kappa + c*g: "
      f"c = {coef[2]:+.3f} (notch sign expected NEGATIVE under one-organ)")
print(f"  residual peaks (N3 rule) at plateau indices: "
      f"{[ks[plateau[i]] for i in __import__('l98_falsifier').peak_regions(list(resid))]}")
print(f"  residual range {resid.min():+.4f}..{resid.max():+.4f} vs N3 jitter "
      f"floor 0.0143")

print("\npower analysis done")
