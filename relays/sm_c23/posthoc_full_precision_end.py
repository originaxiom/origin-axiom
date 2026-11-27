#!/usr/bin/env python3
"""SM-C23, post hoc (after the sealed run, disclosed): the sealed script passes the shifted end L to the frame as a
double, which bounds S's and the act's residuals near 1e-17.  This re-runs action C1 for S and the act at tau0 =
0.13 + 1.2i on the twelve orbit points with L kept in mpmath.
    python3 -B posthoc_full_precision_end.py MAIN_CHECKOUT"""
import sys
import run_c23 as R
mp = R.mp
def frame_mp(t, v, L):
    R.CR.canon = lambda z: {"L_2": L, "L_max": L, "_extrapolated": False}
    try:
        Ys = {s: R.DL.parts(mp.re(t), mp.im(t), v[0], v[1], s)[2]["S"] for s in R.SECS}
    finally:
        R.CR.canon = R.TABLE_CANON
    out = {}
    for s in R.SECS:
        sv = sorted(abs(x) for x in mp.svd_c(Ys[s], compute_uv=False)); out[s] = [sv[0] / sv[2], sv[1] / sv[2]]
    V = R.CM.U_of(Ys["up"]).H * R.CM.U_of(Ys["down"])
    out["V"] = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    return out
mp.mp.dps = 50
t0 = mp.mpc("0.13", "1.2"); L0 = mp.mpf(R.TABLE_CANON(complex(0.13, 1.2))["L_2"])
for gname, g in (("S", R.S), ("ACT", R.ACT)):
    wm = wv = 0.0
    for v in R.orb:
        mp.mp.dps = 50; t1, j = R.mob(g, t0); L1 = L0 + mp.log(abs(j))
        A = frame_mp(t0, v, L0); mp.mp.dps = 50; B = frame_mp(t1, R.CANDIDATES["C1 (a,b) g^-1"](v, g), L1)
        dm, dv = R.dist(A, B); wm, wv = max(wm, dm), max(wv, dv)
    print("post hoc, L in mpmath: %-3s C1 worst |ln ratio| %.2e  worst |dV| %.2e" % (gname, wm, wv))
