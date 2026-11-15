#!/usr/bin/env python3
"""W-F25, post hoc 1 (committed before its run; NOT blind: wf25_run's output has been read).

The sealed run's Y3 failed: B1924's constant end, L_2 = 0.9 - (1/2) log Im tau, falls without bound, and at the cusp
2 pi L_2 + c_s turns negative, so channels drop out (the run's warnings: all singular values zero at some heights). The
canonical end settles near 2.25 at the tables' top (Im tau = 6) and is held there. This run asks whether the cusp
exponents depend on the end's value when the end stays bounded.

  H1  With L_2 held at 1.5, 2.25 and 3.0 at every height, the S reading's four exponents at the mark (up and down, r2
      and r3) agree with the canonical end's (wf25_run) within 1 %.
  Reported: the same for St; and the four non-zero points of the act's line (B1943), k (2/5, 4/5), k = 1..4.

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wf25_posthoc1.py
"""
import json, math, os, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wf25_run as R  # noqa: E402
W = R.W
LS = (1.5, 2.25, 3.0)
LINE = [(0.4, 0.8), (0.8, 0.6), (0.2, 0.4), (0.6, 0.2)]


def job(arg):
    y, L = arg
    t = complex(0.0, y)
    c3 = [complex(v) for v in W.NS["av"](W.mp.mpc(t.real, t.imag))]
    return arg, [W.frame_c(t, a, b, L, c3) for a, b in LINE]


def main():
    base = json.load(open(os.path.join(HERE, "wf25_summary.json")))["mark"]
    with Pool(2) as P:
        res = dict(P.map(job, [(y, L) for y in R.YS for L in LS], chunksize=1))
    h1 = True
    for k in W.KEYS:
        row = []
        for L in LS:
            e, _, _ = R.limit([(y, res[(y, L)][0][k]) for y in R.YS])
            row.append(e)
            if "|S|" in k:
                h1 &= e is not None and abs(e - base[k]["E"]) / abs(base[k]["E"]) < 0.01
        R.say("  %-14s canonical %8.4f | L = 1.5, 2.25, 3.0: %s" % (k, base[k]["E"], "  ".join("%8.4f" % v if v is not None else "-" for v in row)))
    R.say("H1 holds:", h1)
    R.say("the act's line, L = 2.25: exponents at k (2/5, 4/5), k = 1..4")
    for k in W.KEYS:
        R.say("  %-14s %s" % (k, "  ".join("%8.4f" % (R.limit([(y, res[(y, 2.25)][i][k]) for y in R.YS])[0] or float("nan")) for i in range(4))))


if __name__ == "__main__":
    main()
