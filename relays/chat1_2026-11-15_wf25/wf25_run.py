#!/usr/bin/env python3
"""W-F25: frame C's cusp exponents. Data-free (the author's ruling of 2026-11-15): outputs printed, nothing compared with
any measured number.

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wf25_run.py

The frame is W-F24's (imported from wf24_run.py, this seat's code): this seat's transcription of B1656's frame, the
canonical end from B1927's and B1667's tables, Theorem 90's weight, L_2, readings S and St. The constant end is
B1924's, L_2 = 0.9 - (1/2) log Im tau.

E_k(y) = -(log r_k(y + 1) - log r_k(y)) / pi, the local slope over a unit step at heights y = 2..9. A ratio below 1e-12
is unresolved in double precision (B1940) and its steps are not used. The limit estimate is the last resolved step.

EXPECTATIONS (card W-F25, committed before any output above height 6 or at Re tau = 0.25 was computed):
  Y1  At the mark (2/5, 4/5), Re tau = 0, canonical end: for every sector ratio the last two resolved steps differ by
      less than 3 % (relative).
  Y2  The limit at Re tau = 0.25 agrees with Re tau = 0 within 2 % for every sector ratio at the mark.
  Y3  The constant end agrees with the canonical end within 2 % for every sector ratio at the mark.
  Y4  At the mark, every limit is within 2 % of a rational with denominator at most 50.
  Plant: exp(-pi (7/5) y) (1 + 0.3 e^-y) through the same estimator gives 7/5 within 1 %, identified as 7/5.
  Reported: E_k at every point of order 5 (Re tau = 0, canonical end); the fibre's mean exponent; the ratios E_k / E_l at
  the mark.
"""
import json
import math
import os
import sys
from fractions import Fraction
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "chat1_2026-11-15_wf24"))
import wf24_run as W  # noqa: E402

YS = list(range(2, 11))
FLOOR = 1e-12


def say(*a):
    print(*a, flush=True)


def job(arg):
    x, y, end = arg
    if W.LIN is None:
        W.LIN, W.NEAR, W.YMAX = W.end_tables(W.MAIN)
    t = complex(x, y)
    c3 = [complex(v) for v in W.NS["av"](W.mp.mpc(t.real, t.imag))]
    L2 = W.L2_of(t) if end == "canon" else 0.9 - 0.5 * math.log(y)
    return arg, [W.frame_c(t, a, b, L2, c3) for a, b in W.POINTS]


def limit(series):
    """series: list of (y, r). Returns (last step, previous step, number of resolved steps)."""
    s = [(-(math.log(r1) - math.log(r0)) / math.pi) for (y0, r0), (y1, r1) in zip(series, series[1:])
         if r0 > FLOOR and r1 > FLOOR]
    return (s[-1] if s else None, s[-2] if len(s) > 1 else None, len(s))


def rational(v, dmax=50):
    f = Fraction(v).limit_denominator(dmax)
    return f, abs(float(f) - v) / abs(v)


def main():
    if W.MAIN is None:
        raise SystemExit("set MAIN_CHECKOUT")
    # plant
    syn = [(y, math.exp(-math.pi * 1.4 * y) * (1 + 0.3 * math.exp(-y))) for y in YS]
    e, _, _ = limit(syn)
    f, err = rational(e)
    say("plant: estimate %.5f, rational %s (rel. %.1e), holds: %s" % (e, f, err, abs(e - 1.4) / 1.4 < 0.01 and f == Fraction(7, 5)))
    jobs = [(0.0, y, "canon") for y in YS] + [(0.25, y, "canon") for y in YS] + [(0.0, y, "const") for y in YS]
    with Pool(2) as P:
        res = dict(P.map(job, jobs, chunksize=1))
    mark = W.POINTS.index((0.4, 0.8))
    keys = W.KEYS
    out = {"mark": {}, "fibre": {}}
    y1 = y2 = y3 = y4 = True
    say("at the mark: E (Re 0, canonical) | previous step | steps | Re 0.25 | constant end | rational (rel.)")
    for k in keys:
        ser = lambda x, end, p=mark: [(y, res[(x, y, end)][p][k]) for y in YS]
        e0, ep, n = limit(ser(0.0, "canon"))
        e25, _, _ = limit(ser(0.25, "canon"))
        ec, _, _ = limit(ser(0.0, "const"))
        f, err = rational(e0)
        y1 &= ep is not None and abs(e0 - ep) / abs(e0) < 0.03
        y2 &= abs(e25 - e0) / abs(e0) < 0.02
        y3 &= abs(ec - e0) / abs(e0) < 0.02
        y4 &= err < 0.02
        out["mark"][k] = dict(E=e0, prev=ep, steps=n, E_re025=e25, E_const=ec, rational=str(f), rel=err)
        say("  %-14s %8.4f  %8.4f  %d  %8.4f  %8.4f  %s (%.1e)" % (k, e0, ep if ep is not None else float("nan"), n, e25, ec, f, err))
    say("Y1 holds:", y1, "| Y2 holds:", y2, "| Y3 holds:", y3, "| Y4 holds:", y4)
    say("every point of order 5 (Re 0, canonical end): E per sector ratio")
    say("  point      " + " ".join("%9s" % k.replace("|", "")[:9] for k in keys))
    for i, p in enumerate(W.POINTS):
        row = []
        for k in keys:
            e, _, _ = limit([(y, res[(0.0, y, "canon")][i][k]) for y in YS])
            row.append(e)
            out["fibre"].setdefault(k, []).append(e)
        say("  (%s, %s) " % (Fraction(p[0]).limit_denominator(5), Fraction(p[1]).limit_denominator(5)) +
            " ".join("%9.4f" % v if v is not None else "%9s" % "-" for v in row))
    say("the fibre's mean exponent (over the points resolved):")
    for k in keys:
        v = [e for e in out["fibre"][k] if e is not None]
        say("  %-14s %8.4f  (%d of 24 resolved)" % (k, float(np.mean(v)), len(v)))
    say("scale-free ratios at the mark, E_k / E(up|S|r3) (no comparison with anything measured):")
    ref = out["mark"]["up|S|r3"]["E"]
    for k in keys:
        say("  %-14s %8.4f" % (k, out["mark"][k]["E"] / ref))
    json.dump({"mark": out["mark"], "fibre": out["fibre"], "points": [list(p) for p in W.POINTS]},
              open(os.path.join(HERE, "wf25_summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
