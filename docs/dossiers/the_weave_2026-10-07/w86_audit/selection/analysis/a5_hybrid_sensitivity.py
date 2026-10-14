import json, sys
import numpy as np
S = sys.argv[1]
per = json.load(open(f"{S}/committed/chat1_2026-10-14_selection/thread_frame.json"))["readouts"]["per thread"]
banked = json.load(open(f"{S}/sm87/docs/dossiers/the_weave_2026-10-07/the_surface_yukawa.json"))
Yb = np.array([[complex(*z) for z in row] for row in banked["X4"]["Y (Y0 = 2.0)"]]).real
def r23(K, Y):
    ev, U = np.linalg.eigh(K); Kmh = U @ np.diag(ev ** -0.5) @ U.conj().T
    s = np.sort(np.linalg.svd(Kmh.T @ Y @ Kmh, compute_uv=False)); return s[1] / s[2]
rng = np.random.default_rng(7)
print("thread   own        realrandY median     W72Y entries x U[1/2,2]: median [min,max] of ratio to own")
for w in ("LR", "LLRR", "LLR", "LLLR", "LLLLR"):
    r = per[w]; K = np.array([[complex(*z) for z in row] for row in r["K"]]); own = r["m2/m3"]
    rr = []
    for _ in range(2000):
        A = rng.normal(size=(3, 3)); rr.append(r23(K, A + A.T) / own)
    pp = []
    for _ in range(2000):
        F = np.exp(rng.uniform(np.log(0.5), np.log(2), size=(3, 3))); F = np.sqrt(F * F.T)
        pp.append(r23(K, Yb * F) / own)
    pp = np.array(pp)
    print(f"{w:7s} {own:.3e}   x{np.median(rr):.3g}        x{np.median(pp):.3g} [{pp.min():.3g}, {pp.max():.3g}]")
# Which entries matter at the root? zero one entry pair at a time
K = np.array([[complex(*z) for z in row] for row in per["LR"]["K"]])
print("root: W72 Y with one symmetric entry pair set to 0 -> m2/m3")
for (a, b) in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]:
    Y2 = Yb.copy(); Y2[a, b] = Y2[b, a] = 0; print((a, b), round(r23(K, Y2), 5))
print("root with W72 Y: ", r23(K, Yb), " with K diag only:", r23(np.diag(np.diag(K)), Yb))
