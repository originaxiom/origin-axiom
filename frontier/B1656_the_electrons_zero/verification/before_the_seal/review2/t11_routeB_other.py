# Review 2, check (E2 feasibility on OTHER cases): route B (numpy replica of cB, n=32) vs the revised route A, plus replica-vs-instrument cB at small n.
import numpy as np, math, sys, time, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, ".")
from load_inst import load
from cbfast import cB_np
ns = load()
for k in ("cA","cB","pairs","rmax_np","vangles","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","mp"): globals()[k] = ns[k]
# (1) replica fidelity: instrument cB (mpmath) at n=6 vs replica at n=6 on a case NOT among E2's three
p1, p2, t, sec = 2/9, 5/9, OM, "down"
w = line_w(p1, p2, t); fl, fr = SECTORS[sec]; x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
for s in ("i", "1"):
    vi = cB(x, y, t, s, R[s], n=6); vr, _ = cB_np(pairs, rmax_np, vangles, x, y, t, s, R[s], n=6)
    print("replica fidelity (n=6, %s, %s): instrument cB %.12f replica %.12f  diff %.2e" % (sec, s, vi, vr, abs(vi - vr)))
# (2) |A - B(n)| for n = 16, 24, 32, 48 on other cases (A = revised cA, eps=1e-5, default quadrature)
def case(p1, p2, t, sec, n_list=(16, 24, 32, 48), ql=None, qr=None):
    w = line_w(p1, p2, t); fl, fr = SECTORS[sec]
    x, y = sector_twists(w, t, SIXY[fl] if ql is None else ql, SIXY[fr] if qr is None else qr); R = residues(x, y, t)
    ca = cA(x, y, t, R)
    worst = {n: 0.0 for n in n_list}
    for s in UNITS:
        if ca[s] is None: continue
        for n in n_list:
            v, _ = cB_np(pairs, rmax_np, vangles, x, y, t, s, R[s], n=n); worst[n] = max(worst[n], abs(v - ca[s]))
    print((round(9*p1, 2), round(9*p2, 2)), np.round(t, 3), sec, " | ".join("n=%d: %.2e" % (n, worst[n]) for n in n_list), flush=True)
    return worst
T2 = -0.17 + 0.95j
t0 = time.time()
for args in [((2/9, 5/9), OM, "up"), ((2/9, 5/9), OM, "down"), ((4/9, 7/9), OM, "up"), ((7/9, 7/9), OM, "lep"), ((1/9, 2/9), OM, "up"), ((1/9, 2/9), OM, "down"), ((2/9, 0.0), OM, "lep"),
             ((2/9, 5/9), T2, "up"), ((2/9, 5/9), T2, "lep"), ((4/9, 7/9), GEN, "down"), ((0.137, 0.291), GEN, "up"), ((0.613, 0.287), T2, "down"), ((1/9, 1/9), T2, "lep")]:
    case(args[0][0], args[0][1], args[1], args[2])
print("time %.0fs" % (time.time() - t0))
