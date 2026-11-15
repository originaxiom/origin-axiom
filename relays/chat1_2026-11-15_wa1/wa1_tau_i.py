#!/usr/bin/env python3
"""W-A1, part 3: frame C at tau = i on the act's axis (the author's ruling of 2026-11-15, early afternoon: outputs
printed; nothing compared with data or with any value on record).

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wa1_tau_i.py

The frame: W-F24's (this seat's transcription of B1656's frame; the canonical end from B1927's and B1667's tables;
Theorem 90's weight; L_2; readings S and St), with W-F26's couplings for the mixing |V| = |U_u^dagger U_d| (left
singular vectors ordered lightest to heaviest). The act's axis: z(s) = (phi i e^s - 1/phi) / (i e^s + 1),
phi = (1 + sqrt 5)/2; z(s0) = i at s0 = -log phi.

EXPECTATIONS (card W-A1, committed before this script):
  I1  at tau = i, the mark (2/5, 4/5) and the twin (1/5, 2/5) give the same outputs: every sector ratio in S and St, and
      |V| in the four reading pairs (largest relative deviation of the ratios, and largest absolute deviation of |V|,
      below 1e-6).
  I2  every sector ratio at (i, mark) lies strictly between 1e-8 and 1 - 1e-8 (no zero or degeneracy forced).
  I3  every s3/s1 at (i, mark) is above 1e-3 (no large hierarchy at tau = i).
  I4  reported: at s0 +- 0.05 and s0 +- 0.1 on the axis, the mark-twin deviation (expected non-zero).
  Plant: (i, mark) against (i, (0, 3/5)) differs by more than 1e-3.
  Reported: the outputs at (i, mark): the sector ratios and the four |V| matrices.
"""
import math
import os
import sys
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(R, "chat1_2026-11-15_wf24"))
sys.path.insert(0, os.path.join(R, "chat1_2026-11-15_wf26"))
import wf24_run as W  # noqa: E402
import wf26_run as V  # noqa: E402

PHI = (1 + math.sqrt(5)) / 2
S0 = -math.log(PHI)
MARK, TWIN, OTHER = (0.4, 0.8), (0.2, 0.4), (0.0, 0.6)


def z(s):
    e = math.exp(s)
    return (PHI * 1j * e - 1 / PHI) / (1j * e + 1)


def say(*a):
    print(*a, flush=True)


def outputs(arg):
    t, pt = arg
    if W.LIN is None:
        W.LIN, W.NEAR, W.YMAX = W.end_tables(W.MAIN)
    c3 = [complex(v) for v in W.NS["av"](W.mp.mpc(t.real, t.imag))]
    L2 = W.L2_of(t)
    rat = W.frame_c(t, pt[0], pt[1], L2, c3)
    Y = V.couplings(t, pt[0], pt[1], L2, c3)
    mix = {}
    for ru in ("S", "St"):
        for rd in ("S", "St"):
            Uu = np.linalg.svd(Y[("up", ru)])[0][:, ::-1]
            Ud = np.linalg.svd(Y[("down", rd)])[0][:, ::-1]
            mix[(ru, rd)] = np.abs(np.conj(Uu.T) @ Ud)
    return arg, (rat, mix)


def dev(a, b):
    r = max(abs(a[0][k] / b[0][k] - 1) for k in a[0])
    v = max(float(np.max(np.abs(a[1][q] - b[1][q]))) for q in a[1])
    return r, v


def main():
    ti = z(S0)
    say("z(s0) = %.15f%+.15fi (i expected)" % (ti.real, ti.imag))
    ti = 1j
    jobs = [(ti, MARK), (ti, TWIN), (ti, OTHER)] + [(z(S0 + d), pt) for d in (-0.1, -0.05, 0.05, 0.1) for pt in (MARK, TWIN)]
    with Pool(2) as P:
        res = dict(P.map(outputs, jobs, chunksize=1))
    m, tw, ot = res[(ti, MARK)], res[(ti, TWIN)], res[(ti, OTHER)]
    r1, v1 = dev(m, tw)
    i1 = r1 < 1e-6 and v1 < 1e-6
    vals = list(m[0].values())
    i2 = all(1e-8 < x < 1 - 1e-8 for x in vals)
    i3 = all(m[0][k] > 1e-3 for k in m[0] if k.endswith("r3"))
    rp, vp = dev(m, ot)
    plant = max(rp, vp) > 1e-3
    say("I1 holds:", i1, "| mark against twin at tau = i: ratios %.1e, |V| %.1e" % (r1, v1))
    say("I2 holds:", i2, "| I3 holds:", i3, "| plant (the mark against (0, 3/5)) fails:", plant, "(%.1e, %.1e)" % (rp, vp))
    say("I4 (the act's axis near i): mark against twin")
    for d in (-0.1, -0.05, 0.05, 0.1):
        t = z(S0 + d)
        r, v = dev(res[(t, MARK)], res[(t, TWIN)])
        say("   s0 %+.2f  tau = %.4f%+.4fi   ratios %.2e   |V| %.2e" % (d, t.real, t.imag, r, v))
    say("the outputs at (i, mark), printed and compared with nothing:")
    for k in W.KEYS:
        say("   %-14s %.6g" % (k, m[0][k]))
    for q, M in m[1].items():
        say("   |V| up %s, down %s:  %s" % (q[0], q[1], "  ".join(" ".join("%.4g" % x for x in row) for row in M)))


if __name__ == "__main__":
    main()
