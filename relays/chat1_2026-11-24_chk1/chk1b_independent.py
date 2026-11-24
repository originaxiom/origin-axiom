#!/usr/bin/env python3
"""CHK-1, addendum (written after CHK-1's run, committed before this script is run). CHK-1's numbers agreed with B1977's
to the last bit, which shows the same arithmetic, not an independent one. This addendum uses W-D2's referee's code
(chk1_ref_frame.py): its own theta sums, eta, coupling, and masses from the Hermitian eigenproblem of Y Y^H at
40 + 4 Im tau digits. It shares with main only F_u, the canonical end's table, the triplet's q-series and the charges.
At B1977's five slow points and seven more (every eighth of the 96), heights 20 and 30 at column 0.13, every sector
reading S: the nine rates and the least diagonal, against B1977's json.

    python3 -I -u chk1b_independent.py <a checkout of main>
"""
import json
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chk1_ref_frame as R  # noqa: E402
import chk1_run as C  # noqa: E402  (its points; it also imports W-D2's module, unused here)

mp = R.mp
KEYS = C.KEYS


def snap(a, b, y):
    P = R.point_setup(Fr(13, 100), y, int(40 + 4 * y))
    Ws = {s: R.Mw(P, a, b, s) for s in ("up", "down", "lep")}
    return R.analyse(P, Ws, {s: P["S"] for s in ("up", "down", "lep")})


def main():
    P = C.points()
    pick = sorted(set([p for p in P if (str(p[0]), str(p[1])) in C.SLOW] + P[::8]))
    M = {(r["a"], r["b"]): r for r in json.load(open(os.path.join(
        R.MAIN, "frontier", "B1977_order_30_rates_masses_and_mixing_on_one_grid", "verification", "rates30_run.json")))}
    worst, wd = 0.0, 0.0
    for a, b in pick:
        A, B = snap(a, b, 20), snap(a, b, 30)
        r = {}
        for s in ("up", "down", "lep"):
            r[s + "_m2m3"] = float(-(mp.log(B["r"][s][0]) - mp.log(A["r"][s][0])) / (mp.pi * 10))
            r[s + "_m1m3"] = float(-(mp.log(B["r"][s][1]) - mp.log(A["r"][s][1])) / (mp.pi * 10))
        for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")):
            r[n] = float(-(mp.log(B["A"][i][j]) - mp.log(A["A"][i][j])) / (mp.pi * 10))
        m = M[(str(a), str(b))]
        d = max(abs(r[k] - m[k]) for k in KEYS if m[k] is not None)
        worst = max(worst, d)
        wd = max(wd, abs(float(B["dmin"]) - m["diag"]))
        print("(%s, %s)%s largest rate difference %.2e, least diagonal %.6f (B1977 %.6f)"
              % (a, b, " *" if (str(a), str(b)) in C.SLOW else "", d, float(B["dmin"]), m["diag"]), flush=True)
    print("ADDENDUM: %d points; largest rate difference %.2e; largest diagonal difference %.2e" % (len(pick), worst, wd))


if __name__ == "__main__":
    main()
