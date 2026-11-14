"""Planted control for gauge_class_readout.py: the same comparison machinery must detect the truncated weight's ~1 %
shift. U(1) words read on the exact-weight grid against Pin(2) words read on the truncated grid (B1928's fiber_grid_fine):
expected max |z| well above 3."""
import sys, math, random, pathlib
import numpy as np
sys.argv = ["x"]
exec(open(pathlib.Path(__file__).resolve().parent / "gauge_class_readout.py").read().split("rng = random.Random")[0])
I0 = E.build(E.V / "fiber_grid_fine.json")
rng = random.Random(1937); bins = {"U1": [], "Pin": []}
while min(len(b) for b in bins.values()) < 3000:
    w = "".join(rng.choice("LR") for _ in range(40))
    if "L" not in w or "R" not in w: continue
    c = cls(w)
    if c in bins and len(bins[c]) < 3000: bins[c].append(w)
def readout(ws, I):
    A, wt = [], []
    for w in ws:
        pts, ell = E.thread(w); A.append(E.interp(I, pts).mean(0)); wt.append(ell)
    A, wt = np.array(A), np.array(wt); R = (wt[:, None] * A).sum(0) / wt.sum(); jk = []
    for bl in np.array_split(np.arange(len(ws)), 30):
        m = np.ones(len(ws), bool); m[bl] = False; jk.append((wt[m][:, None] * A[m]).sum(0) / wt[m].sum())
    return R, np.sqrt(29 * np.mean((np.array(jk) - R) ** 2, 0)) / R
a = readout(bins["U1"], I1); b = readout(bins["Pin"], I0)
d = np.log(a[0] / b[0]); z = d / np.sqrt(a[1] ** 2 + b[1] ** 2)
print("CONTROL U1(exact) vs Pin(truncated): max |d ln| %.4f, max |z| %.1f -> %s" % (np.max(np.abs(d)), np.max(np.abs(z)), "CAUGHT" if np.max(np.abs(z)) > 3 else "MISSED"))
