#!/usr/bin/env python3
"""POST HOC, second (written after p589c_posthoc_out.txt was read): the first check was undecided by its rule (the
largest order-12 lepton m1/m3 fell by a factor 3.85, from 8.8e-10 to 2.3e-10, when the quadrature was doubled in each
direction, and the largest moved to another line). This one follows each line, at three quadratures. Uses
p589c_exact_rows.py's functions; the same checkout rule. Data-free.

    python3 -B p589c_posthoc2.py <a checkout of main at 88a1e9474>      # writes p589c_posthoc2.json

At tau = 3.1i, on every order-12 line (up to sign), the leptons' m1/m3 with the exact twisted norms, the largest over
the two horocycles and the readings S and S~, at quadratures q1 = 96 x 64, q2 = 192 x 128 and q3 = 384 x 256 nodes.
Per line, f12 = value(q1)/value(q2) and f23 = value(q2)/value(q3). If the zero is exact, the value is the quadrature's
error and falls at each doubling by the quadrature's order (a factor 4 for a second-order rule); if the line is lifted,
the value levels off at the lift.

Reading rule, stated before the run, over the lines whose value at q1 exceeds 1e-12:
  - quadrature error, the zero holds at the exact norms: on every such line f23 >= 3;
  - a lift: on some such line f23 < 1.5 and value(q3) > 1e-12 (that line is named);
  - otherwise undecided.
"""
import importlib.util
import json
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rows", HERE / "p589c_exact_rows.py")
RW = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RW)

QUADS = ((96, 64), (192, 128), (384, 256))


def line_values(EE, G, rd, tau, a, b, nth, ns):
    B, K = EE.B, EE.K
    lf, rf = K.SECT["lep"]
    w = float(a) * tau + float(b)
    x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf])
    R = B.residues(x, yy, tau)
    best = 0.0
    for h in ("L_max", "L_2"):
        Nx, _ = EE.twisted_norms(tau, G["al"], G["be"], G[h], x, yy, R, nth=nth, ns=ns)
        u = {s: (math.sqrt(Nx[s]) * R[s] if Nx.get(s) is not None and Nx[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn, H in rd.items():
            sv = np.linalg.svd(B.coupling(H, Mw), compute_uv=False)
            best = max(best, float(sv[2] / sv[0]))
    return best


def main():
    EE, root = RW.load(sys.argv[1])
    tau = complex(0, 3.1)
    G, Lcol, r = RW.at_tau(EE, tau)
    rd = EE.higgs(tau)
    lines = RW.lines_of_order(12)
    vals = {}
    for nth, ns in QUADS:
        for (a, b) in lines:
            vals.setdefault("%s,%s" % (a, b), []).append(line_values(EE, G, rd, tau, a, b, nth, ns))
        print("quadrature %d x %d done" % (nth, ns), flush=True)
    rows = []
    for key, (v1, v2, v3) in vals.items():
        f12 = v1 / v2 if v2 > 0 else math.inf
        f23 = v2 / v3 if v3 > 0 else math.inf
        rows.append((key, v1, v2, v3, f12, f23))
    live = [rw for rw in rows if rw[1] > 1e-12]
    print("lines: %d; with value above 1e-12 at %d x %d: %d" % (len(rows), QUADS[0][0], QUADS[0][1], len(live)))
    for key, v1, v2, v3, f12, f23 in sorted(live, key=lambda t: -t[1]):
        print("line (%s): %.3e  %.3e  %.3e   f12 %.2f  f23 %.2f" % (key, v1, v2, v3, f12, f23))
    f23s = [rw[5] for rw in live]
    print("f23 over these lines: min %.2f, median %.2f, max %.2f; largest value at %d x %d: %.3e" % (
        min(f23s), float(np.median(f23s)), max(f23s), QUADS[2][0], QUADS[2][1], max(rw[3] for rw in rows)))
    lifted = [rw[0] for rw in live if rw[5] < 1.5 and rw[3] > 1e-12]
    if all(f >= 3 for f in f23s):
        verdict = "quadrature error: the zero holds at the exact norms"
    elif lifted:
        verdict = "a lift, on line(s) " + "; ".join(lifted)
    else:
        verdict = "undecided"
    print("reading:", verdict)
    json.dump({"tau": [0, 3.1], "quadratures": QUADS, "lines": {k: v for k, v in vals.items()}, "verdict": verdict},
              open("p589c_posthoc2.json", "w"), indent=1)


if __name__ == "__main__":
    main()
