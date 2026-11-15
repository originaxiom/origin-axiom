#!/usr/bin/env python3
"""W-F26: frame C's mixing high in the cusp, in every option. Data-free (the author's ruling of 2026-11-15).

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wf26_run.py

W-F24's frame (this seat's transcription; canonical end; Theorem 90's weight; L_2). For each sector the coupling Y is
built in both readings; V = U_u^dagger U_d with each left-singular basis ordered lightest to heaviest (B1724's
svd(Y)[0][:, ::-1]). Options: point in {mark (2/5, 4/5), twin (1/5, 2/5)} x up reading {S, St} x down reading {S, St}.
Heights 3, 4, 6, 8 at Re tau = 0 and 1/4.

EXPECTATIONS (card W-F26, committed with this script before any of its output):
  Z1  In all eight options |V| is within 0.05 of a permutation (max entrywise |V| - P) at heights 6 and 8, both Re tau.
  Z2  In at least one option that permutation is not the identity.
  Reported: the permutation per option, whether it is the identity, and for options near the identity the off-diagonal
  moduli's local exponents -(1/pi) d log|V_ij| / d Im tau between heights 6 and 8.
"""
import itertools, math, os, sys
from multiprocessing import Pool
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "chat1_2026-11-15_wf24"))
import wf24_run as W  # noqa: E402
NS = W.NS
PTS = {"mark": (0.4, 0.8), "twin": (0.2, 0.4)}
HS = (3.0, 4.0, 6.0, 8.0)
XS = (0.0, 0.25)
PERMS = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]


def say(*a):
    print(*a, flush=True)


def couplings(t, a, b, L2, c3):
    S = c3[0] * NS["QI"] + c3[1] * NS["QJ"] + c3[2] * NS["QK"]
    reading = {"S": S, "St": NS["EPS"] @ np.conj(S) @ NS["EPS"].T}
    w = a * t + b
    Y = {}
    for sec in ("up", "down"):
        lf, rf = W.SECT[sec]
        x, yy = NS["twist_of"](NS["SIXY"][lf] * w, t), NS["twist_of"](NS["SIXY"][rf] * w, t)
        R = NS["residues"](x, yy, t); c = NS["cA"](x, yy, t, R); a0 = NS["a0_of"](x, yy, t, R)
        u = {}
        for s in NS["UNITS"]:
            if c[s] is None or a0[s] is None:
                u[s] = 0; continue
            N = 2 * math.pi * L2 + c[s] - math.pi * abs(a0[s]) ** 2 * math.exp(-2 * L2)
            u[s] = math.sqrt(N) * R[s] if N > 0 else 0
        Mw = NS["weighted_M"](u)
        for rn in ("S", "St"):
            Y[(sec, rn)] = NS["coupling"](reading[rn], Mw)
    return Y


def job(arg):
    name, x, y = arg
    if W.LIN is None:
        W.LIN, W.NEAR, W.YMAX = W.end_tables(W.MAIN)
    t = complex(x, y)
    c3 = [complex(v) for v in NS["av"](W.mp.mpc(t.real, t.imag))]
    Y = couplings(t, *PTS[name], W.L2_of(t), c3)
    out = {}
    for ru in ("S", "St"):
        for rd in ("S", "St"):
            Uu = np.linalg.svd(Y[("up", ru)])[0][:, ::-1]
            Ud = np.linalg.svd(Y[("down", rd)])[0][:, ::-1]
            out[(ru, rd)] = np.abs(np.conj(Uu.T) @ Ud)
    return arg, out


def main():
    jobs = [(n, x, y) for n in PTS for x in XS for y in HS]
    with Pool(2) as P:
        res = dict(P.map(job, jobs, chunksize=1))
    z1, nonid = True, 0
    for n in PTS:
        for ru in ("S", "St"):
            for rd in ("S", "St"):
                say("option: %s, up %s, down %s" % (n, ru, rd))
                perm_hi = None
                for x in XS:
                    for y in HS:
                        V = res[(n, x, y)][(ru, rd)]
                        devs = [float(np.max(np.abs(V - P))) for P in PERMS]
                        k = int(np.argmin(devs))
                        lab = "".join(str(int(np.argmax(PERMS[k][i]))) for i in range(3))
                        say("   Re %.2f  Im %.0f  nearest permutation %s (identity 012)  max dev %.3g   |V| rows %s" % (
                            x, y, lab, devs[k], "  ".join(" ".join("%.3g" % v for v in row) for row in V)))
                        if y >= 6:
                            z1 &= devs[k] < 0.05
                            perm_hi = lab if perm_hi in (None, lab) else "mixed"
                nonid += perm_hi != "012"
                if perm_hi == "012":
                    for x in XS:
                        V6, V8 = res[(n, x, 6.0)][(ru, rd)], res[(n, x, 8.0)][(ru, rd)]
                        ex = [[-(math.log(V8[i, j]) - math.log(V6[i, j])) / (2 * math.pi) if V6[i, j] > 1e-12 and V8[i, j] > 1e-12 else float("nan")
                               for j in range(3)] for i in range(3)]
                        say("   near the identity; off-diagonal exponents (Re %.2f): %s" % (x, ex))
                say("   permutation at heights 6 and 8: %s" % perm_hi)
    say("Z1 holds:", z1, "| Z2 holds:", nonid >= 1, "| options whose high permutation is not the identity: %d of 8" % nonid)


if __name__ == "__main__":
    main()
