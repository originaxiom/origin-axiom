#!/usr/bin/env python3
"""The web seat's harvest review, after main's M43: the sign of the relabelling in W-A3's lines 76 and 86.

W-A3 writes "one relabelling, by zeta^(ab), removes both of B1953's down phases" (line 76) and "a relabelling by
zeta^(m ab) removes it from T (m = 1 for down, -1 for lepton)" (line 86), without saying which way the relabelling is
read. Main's check R4 (B1957, checks/web_review.py) finds Y(a, b) -> zeta^(-ab) Y(a, b) for down.

This script reads the law in B1953's own convention, Y(g tau, w) = c phi(g, w) U_L Y(tau, w g) U_R^dagger (main's
weyl_operator.py, used as is), and for each sector (down, lepton), reading (S, St), generator (T, S) and sign eps = +1, -1
prints how far the phases still vary over the 24 points after Y'(a, b) = zeta^(eps ab) Y(a, b).

Expectations, committed with this script before the run (from the law's form alone): down is removed by eps = -1 for both
T and S; lepton's T phase by eps = +1. So W-A3's signs hold only when the relabelling is read the other way,
Y(a, b) = zeta^(m ab) Y'(a, b).

    python3 -I -u rv_relabel_sign.py <a checkout of main>
"""
import pathlib
import sys

import numpy as np

MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1953_*")) / "verification"))
import weyl_operator as W  # noqa: E402

psi = W.psi
q = lambda a, b: (a * b) % 5
print("main at:", (MAIN / ".git").exists() and "a git checkout" or "a directory", flush=True)
for sec in ("down", "lep"):
    Ys, _ = W.images("0.13", 1.7, sec)
    for rd in ("S", "St"):
        for gen in "TS":
            lw = W.law(Ys["t"][rd], Ys[gen][rd], gen)
            phi = lw["phi"]
            tr = W.TRANS[gen][0]
            raw = max(abs(np.angle(phi[w] / phi[(0, 1)])) for w in W.PTS) / (2 * np.pi)
            dev = {}
            for eps in (1, -1):
                ph = {w: phi[w] * psi(eps * (q(*w) - q(*tr(*w)))) for w in W.PTS}
                dev[eps] = max(abs(np.angle(ph[w] / ph[(0, 1)])) for w in W.PTS) / (2 * np.pi)
            print("%-4s reading %-2s %s: law residual %.1e; phases vary by %.3f of a turn; after zeta^(+ab): %.1e; after zeta^(-ab): %.1e"
                  % (sec, rd, gen, lw["residual"], raw, dev[1], dev[-1]), flush=True)
