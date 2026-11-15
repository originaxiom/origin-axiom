#!/usr/bin/env python3
"""W-A1, part 3, post hoc 1 (committed before its run; NOT blind: wa1_tau_i.py's output has been read).

The sealed run showed, outside its expectations, that at tau = i the readings S and St give the same sector ratios and
the four reading pairs the same |V|. This run measures that and asks whether it is special to tau = i.

  H1  at tau = i, the mark: S against St, largest relative deviation of the ratios and absolute deviation of |V| across
      the four reading pairs, below 1e-8.
  H2  (controls, a prediction) S against St deviates by more than 1e-3 at tau = 1.3i, at tau = 0.9i + 0.05 (off the axis
      of Re tau = 0) and on the act's axis at s0 +- 0.05.
  H3  reported: at tau = i, S against St at every point of order 5.
  H4  reported: the end's weight at tau = i: the mark's outputs with L_2 moved by -0.3 and +0.3 from the canonical value
      (the end is a remaining convention; how much the outputs move is the price).

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wa1_tau_i_posthoc1.py
"""
import math, os, sys
from multiprocessing import Pool
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wa1_tau_i as A  # noqa: E402
W, V = A.W, A.V


def outs(arg):
    t, pt, dL = arg
    if W.LIN is None:
        W.LIN, W.NEAR, W.YMAX = W.end_tables(W.MAIN)
    c3 = [complex(v) for v in W.NS["av"](W.mp.mpc(t.real, t.imag))]
    L2 = W.L2_of(t) + dL
    rat = W.frame_c(t, pt[0], pt[1], L2, c3)
    Y = V.couplings(t, pt[0], pt[1], L2, c3)
    mix = {}
    for ru in ("S", "St"):
        for rd in ("S", "St"):
            Uu = np.linalg.svd(Y[("up", ru)])[0][:, ::-1]
            Ud = np.linalg.svd(Y[("down", rd)])[0][:, ::-1]
            mix[(ru, rd)] = np.abs(np.conj(Uu.T) @ Ud)
    return arg, (rat, mix)


def s_vs_st(o):
    rat, mix = o
    r = max(abs(rat[k.replace("|S|", "|St|")] / rat[k] - 1) for k in rat if "|S|" in k)
    ref = mix[("S", "S")]
    v = max(float(np.max(np.abs(mix[q] - ref))) for q in mix)
    return r, v


def main():
    pts = W.POINTS
    ctrl = [1.3j, complex(0.05, 0.9), A.z(A.S0 - 0.05), A.z(A.S0 + 0.05)]
    jobs = [(1j, A.MARK, 0.0)] + [(t, A.MARK, 0.0) for t in ctrl] + [(1j, p, 0.0) for p in pts] + \
           [(1j, A.MARK, d) for d in (-0.3, 0.3)]
    with Pool(2) as P:
        res = dict(P.map(outs, jobs, chunksize=1))
    r, v = s_vs_st(res[(1j, A.MARK, 0.0)])
    A.say("H1 holds:", r < 1e-8 and v < 1e-8, "| at tau = i, the mark: S against St, ratios %.1e, |V| over the four pairs %.1e" % (r, v))
    h2 = True
    for t in ctrl:
        rr, vv = s_vs_st(res[(t, A.MARK, 0.0)])
        h2 &= max(rr, vv) > 1e-3
        A.say("   control tau = %.4f%+.4fi: ratios %.2e, |V| %.2e" % (t.real, t.imag, rr, vv))
    A.say("H2 holds:", h2)
    worst = 0.0
    for p in pts:
        rr, vv = s_vs_st(res[(1j, p, 0.0)])
        worst = max(worst, rr, vv)
        A.say("   H3 tau = i, point (%.1f, %.1f): S against St, ratios %.1e, |V| %.1e" % (p[0], p[1], rr, vv))
    A.say("H3: the largest over the 24 points: %.1e" % worst)
    base = res[(1j, A.MARK, 0.0)]
    for d in (-0.3, 0.3):
        o = res[(1j, A.MARK, d)]
        rr = max(abs(o[0][k] / base[0][k] - 1) for k in base[0])
        vv = max(float(np.max(np.abs(o[1][q] - base[1][q]))) for q in base[1])
        A.say("H4 the end moved by %+.1f at (i, mark): ratios move by up to %.2e, |V| by up to %.2e" % (d, rr, vv))


if __name__ == "__main__":
    main()
