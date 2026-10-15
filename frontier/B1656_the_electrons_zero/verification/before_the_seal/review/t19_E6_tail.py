# E6's quark criteria over MANY random S (seed 20261015, line (5/9,8/9)) -- NOT the sealed draws -- to estimate the chance that one of 30 sealed draws trips a threshold
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","SECTORS","SIXY","UNITS","coupling","weighted_M","cA","np"): globals()[k] = ns[k]
rng = np.random.default_rng(20261015)
w = line_w(5/9, 8/9, OM)
errs = {"up": [], "down": []}; q40 = {"up": [], "down": []}
for sec in ("up", "down"):
    fl, fr = SECTORS[sec]; x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
    us = {L: weighted_M({s: math.sqrt(2*np.pi*L + c[s])*R[s] for s in UNITS}) for L in (40.0, 640.0, 2560.0)}
    for _ in range(4000):
        S = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
        v = {L: (lambda sv: sv[2]/sv[0])(np.linalg.svd(coupling(S, us[L]), compute_uv=False)) for L in us}
        errs[sec].append(abs(2560*v[2560]/(640*v[640]) - 1)); q40[sec].append(v[40.0])
for sec in errs:
    e = np.array(errs[sec]); q = np.array(q40[sec])
    print(sec, "L-ratio rel err: median %.2e, 99th pct %.2e, max %.2e; frac > 0.02: %.4f ; sigma3/sigma1(L=40): min %.2e, frac < 1e-6: %.5f" % (np.median(e), np.percentile(e, 99), e.max(), np.mean(e > 0.02), q.min(), np.mean(q < 1e-6)))
    print("   probability that at least one of 15 draws (5 S x 3 lines, per sector) exceeds 2%%: %.3f" % (1 - (1 - np.mean(e > 0.02))**15))
