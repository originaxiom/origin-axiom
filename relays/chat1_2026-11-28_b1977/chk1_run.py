#!/usr/bin/env python3
"""CHK-1: an independent recomputation of B1977's order-30 rates (card relays/cards/CHAT1_CHK1_b1977_order_30_rates.md,
committed before this script). Data-free.

    python3 -I -u chk1_run.py <a checkout of main>

The per-sector steps are W-D2's transcription of frame_mp's fbar; the coupling, SVD, ordering and CKM are W-D2's own. Every
sector reads S. Points: the 96 of order 30 whose 5-part is k(1/5, 2/5), built here by the Chinese remainder theorem.
Rates in eps = e^(-pi Im tau): -(ln|x(y2)| - ln|x(y1)|) / (pi (y2 - y1)).
"""
import json
import math
pass  # [copy: loader replaced, see MANIFEST.md]
import os
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
pass  # [copy: loader replaced, see MANIFEST.md]
W = None  # the copy does not load W-D2's module: chk1b_independent.py uses only points(), SLOW, KEYS  # [copy: loader replaced, see MANIFEST.md]

SECS = ("up", "down", "lep")
KEYS = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
SLOW = {("4/15", "1/30"), ("4/15", "11/30"), ("4/15", "7/10"), ("11/15", "3/10"), ("11/15", "19/30")}


def order(p):
    return math.lcm(p[0].denominator, p[1].denominator)


def points():
    P5 = [((k * Fr(1, 5)) % 1, (k * Fr(2, 5)) % 1) for k in range(1, 5)]
    P6 = [(Fr(i, 6), Fr(j, 6)) for i in range(6) for j in range(6) if order((Fr(i, 6), Fr(j, 6))) == 6]
    P = sorted({((a5 + a6) % 1, (b5 + b6) % 1) for a5, b5 in P5 for a6, b6 in P6})
    assert len(P) == 96 and all(order(p) == 30 for p in P) and all(((6 * a) % 1, (6 * b) % 1) in P5 for a, b in P)
    return P


def snap(a, b, x, y):
    T = W.tau_setup(x, y)
    sv, U = {}, {}
    for sec in SECS:
        s, u = W.svd_sorted(W.coupling(T, T["S"], W.sector_M(T, a, b, sec)))
        sv[sec], U[sec] = s, u
    V = W.conj(U["up"]).T * U["down"]
    return {"r": {sec: (sv[sec][1] / sv[sec][0], sv[sec][2] / sv[sec][0]) for sec in SECS},
            "V": [[abs(V[i, j]) for j in range(3)] for i in range(3)]}


def rates(A, B, dy):
    def rt(u, v):
        return float(-(mp.log(v) - mp.log(u)) / (mp.pi * dy)) if u > 0 and v > 0 else None
    out = {}
    for sec in SECS:
        out[sec + "_m2m3"] = rt(A["r"][sec][0], B["r"][sec][0])
        out[sec + "_m1m3"] = rt(A["r"][sec][1], B["r"][sec][1])
    for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")):
        out[n] = rt(A["V"][i][j], B["V"][i][j])
    return out


def task(p):
    a, b = p
    x1, x2 = Fr(13, 100), Fr(31, 100)
    s20, s30, s40 = snap(a, b, x1, 20), snap(a, b, x1, 30), snap(a, b, x1, 40)
    t20, t30 = snap(a, b, x2, 20), snap(a, b, x2, 30)
    return {"a": str(a), "b": str(b), "r2030": rates(s20, s30, 10), "r3040": rates(s30, s40, 10),
            "r2030_x31": rates(t20, t30, 10),
            "diag30": float(min(s30["V"][k][k] for k in range(3))), "diag40": float(min(s40["V"][k][k] for k in range(3)))}


def main():
    if W.MAIN is None:
        sys.exit("give a checkout of main")
    t0 = time.time()
    P = points()
    with mpc.get_context("fork").Pool(4) as pool:
        rows = pool.map(task, P)
    json.dump(rows, open(os.path.join(HERE, "chk1_output.json"), "w"), indent=1)
    print("computed %d points  [%.0f s]" % (len(rows), time.time() - t0))
    main_json = os.path.join(W.MAIN, "frontier", "B1977_order_30_rates_masses_and_mixing_on_one_grid", "verification",
                             "rates30_run.json")
    M = {(r["a"], r["b"]): r for r in json.load(open(main_json))}
    worst, worst_diag, missing = 0.0, 0.0, 0
    for r in rows:
        m = M.get((r["a"], r["b"]))
        if m is None:
            missing += 1
            continue
        for k in KEYS:
            if r["r2030"][k] is None or m[k] is None:
                if (r["r2030"][k] is None) != (m[k] is None):
                    worst = float("inf")
                continue
            worst = max(worst, abs(r["r2030"][k] - m[k]))
        worst_diag = max(worst_diag, abs(r["diag30"] - m["diag"]))
    r1 = missing == 0 and worst <= 1e-6 and worst_diag <= 1e-6
    print("R1 holds:", r1, "| points missing in main's json %d, worst rate difference %.2e, worst diagonal difference %.2e"
          % (missing, worst, worst_diag))
    slow = [r for r in rows if (r["a"], r["b"]) in SLOW]
    v23 = [r["r3040"]["V23"] for r in slow]
    print("R2 holds:", all(v is not None and abs(v - 1 / 30) <= 2e-3 for v in v23), "| V23 rates 30-40 at the slow points:",
          [round(v, 5) if v is not None else None for v in v23], "; 20-30:", [round(r["r2030"]["V23"], 5) for r in slow])
    dx = [abs(r["r2030_x31"][k] - r["r2030"][k]) for r in rows for k in KEYS
          if r["r2030_x31"][k] is not None and r["r2030"][k] is not None]
    print("R3 holds:", max(dx) <= 1e-3, "| largest column difference %.2e, over %d rates; above 1e-3: %d"
          % (max(dx), len(dx), sum(d > 1e-3 for d in dx)))

    def hier(q):
        return q["up_m2m3"] >= 0.1 and q["up_m1m3"] >= 0.2 and q["down_m2m3"] >= 0.1 and q["down_m1m3"] >= 0.2
    g5 = [r for r in rows if r["diag30"] >= 0.9 and hier(r["r2030"])
          and min(v for v in (r["r2030"]["V12"], r["r2030"]["V23"], r["r2030"]["V13"]) if v is not None) < 0.1]
    print("R4 holds:", all(r["diag40"] >= 0.9 for r in g5), "| G5 points %d; least diagonal at 40 among them %.4f"
          % (len(g5), min(r["diag40"] for r in g5) if g5 else float("nan")))
    r34 = [v for r in rows for v in r["r3040"].values() if v is not None]
    on = [v for v in r34 if abs(v * 60 - round(v * 60)) / 60 <= 3e-3]
    print("R5 holds:", len(on) >= 0.95 * len(r34), "| rates 30-40 on the 1/60 grid: %d of %d" % (len(on), len(r34)))
    r23 = [v for r in rows for v in r["r2030"].values() if v is not None]
    on23 = [v for v in r23 if abs(v * 60 - round(v * 60)) / 60 <= 3e-3]
    drift = [abs(r["r3040"][k] - r["r2030"][k]) for r in rows for k in KEYS
             if r["r3040"][k] is not None and r["r2030"][k] is not None]
    print("   read-outs: rates 20-30 on the grid %d of %d; drift from 20-30 to 30-40: largest %.2e, above 1e-3: %d of %d"
          % (len(on23), len(r23), max(drift), sum(d > 1e-3 for d in drift), len(drift)))
    g1 = sum(hier(r["r2030"]) for r in slow)
    g2 = sum(r["r2030"]["V23"] is not None and abs(r["r2030"]["V23"] - 1 / 30) < 2e-3 for r in slow)
    g4 = sum(abs(r["r2030"]["lep_m2m3"] - r["r2030"]["down_m2m3"]) > 1e-2 for r in slow)
    print("R6 read-out (B1977's criteria on these numbers): G1 %d of 5, G2 %d of 5, G3 %d of %d, G4 %d of 5, G5 %d points"
          % (g1, g2, len(on23), len(r23), g4, len(g5)))
    print("done  [%.0f s]" % (time.time() - t0))


if __name__ == "__main__":
    main()
