#!/usr/bin/env python3
"""sm:B1515, one claim, with main's own code: at q = 1 (the complete hyperbolic structure) the twisted geometric four nu (x) rho_1
has interior classes on the six-fold cover at characters of order eight, and at none of the controls."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tower_own as to
jo, ix = to.jo, to.ix
from mpmath import mp, mpf, mpc, exp, pi, nstr
mp.dps = 60
def read(n, ab, lam, label):
    nu = (exp(2j * pi * mpf(ab[0][0]) / ab[0][1]), exp(2j * pi * mpf(ab[1][0]) / ab[1][1]))
    try: Phi, h, T = to.level(mpf(1), n, nu, lam)
    except AssertionError as ex: print("%-46s %s" % (label, ex)); return
    I, a, b = ix.index(Phi, h, T)
    print("%-46s index %+d  h0 %d/%d  h1 %d/%d  interior %d/%d  kept %s dropped %s" % (label, I, a["h0"], b["h0"], a["h1"], b["h1"], a["interior"], b["interior"], nstr(a["gaps"][1][0], 2), nstr(a["gaps"][1][1], 2)), flush=True)
if __name__ == "__main__":
    for ab in (((1, 8), (1, 2)), ((1, 8), (5, 8)), ((1, 8), (7, 8)), ((1, 4), (3, 8))): read(6, ab, mpc(1), "level 6, nu = (%d/%d, %d/%d), q = 1" % (ab[0] + ab[1]))
    read(6, ((1, 2), (0, 1)), mpc(1), "level 6, nu of order 2 (control)")
    read(6, ((1, 4), (1, 4)), mpc(1), "level 6, nu = (1/4, 1/4) (control)")
    read(3, ((1, 2), (0, 1)), mpc(1), "level 3, nu of order 2 (control)")
    read(1, ((0, 1), (0, 1)), mpc(1), "level 1, trivial nu (the geometric four)")
