#!/usr/bin/env python3
"""W-D2, post hoc (labelled; written after the run's printed output was read, committed before this script is run).
It reads wd2_output.json only and computes nothing new about the frame.

  P1  the control C1 failed as worded: the |V| of the one partial cell (the twin, height 10, W+, no singlet).
  P2  D-2: per point, height and world, the best least-diagonal any singlet reaches, with its kappa and phase.
  P3  D-2: the split between leptons and down quarks against the hierarchy. Per kappa: the largest |ln D| over the
      cells whose heavy-pair ratios are both at most 1e-2, and the least heavy-pair ratio over the cells with
      |ln D| >= 0.5.
  P4  D-2: odd and even give the same lepton-down ratios with the phase shifted by pi (j -> j + 4), since the down
      quarks and the leptons carry the same sign in both.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
O = json.load(open(os.path.join(HERE, "wd2_output.json")))
D2 = O["D2"]


def lnd(q):
    return max(q["lnD2"], q["lnD1"])


key = [k for k in D2 if k.startswith("twin|10|0|")][0]
print("P1: the twin, height 10, W+, no singlet: |V| =", D2[key]["ctrl"]["Wp"]["V"], "class", D2[key]["ctrl"]["Wp"]["cls"])

for k, r in sorted(D2.items()):
    name, y, extra, kmin = k.split("|")
    if extra != "0":
        continue
    for w in ("Wm", "Wp"):
        cells = [q for q in r["cells"] if q["w"] == w]
        best = max(cells, key=lambda q: q["dmin"])
        print("P2: %s height %s %s: best least diagonal %.4f at k = %d (kappa 10^(k/2)), j = %d, %s; heavy-pair %.3e"
              % (name, y, w, best["dmin"], best["k"], best["j"], best["par"], best["hp"]))
        ks = sorted(set(q["k"] for q in cells))
        row = []
        for kk in ks:
            sub = [q for q in cells if q["k"] == kk]
            hier = [q for q in sub if q["hp"] <= 1e-2 and math.isfinite(lnd(q))]
            split = [q for q in sub if math.isfinite(lnd(q)) and lnd(q) >= 0.5]
            row.append("%d:%s/%s" % (kk, ("%.2g" % max(lnd(q) for q in hier)) if hier else "-",
                                     ("%.2g" % min(q["hp"] for q in split)) if split else "-"))
        print("P3: %s height %s %s, per k: (largest |ln D| with hierarchy kept / least heavy-pair with |ln D| >= 0.5)"
              % (name, y, w))
        print("    " + "  ".join(row))
    odd = {(q["w"], q["k"], q["j"]): q for q in r["cells"] if q["par"] == "odd"}
    worst = 0.0
    for q in r["cells"]:
        if q["par"] != "even":
            continue
        p = odd[(q["w"], q["k"], (q["j"] + 4) % 8)]
        for f in ("lnD2", "lnD1"):
            if math.isfinite(p[f]) and math.isfinite(q[f]):
                worst = max(worst, abs(p[f] - q[f]))
    print("P4: %s height %s: largest difference of |ln D| between even at phase j and odd at j + 4: %.2e" % (name, y, worst))
