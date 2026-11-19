#!/usr/bin/env python3
"""W-D2: two structures that could align frame C's cusp mixing (card relays/cards/CHAT1_W-D2_two_structures_for_the_cusp_
mixing.md, committed before this script). Data-free: nothing is compared and no target is opened.

    python3 -I -u wd2_run.py <a checkout of main>

Frame C is main's B1940 frame_mp, imported and not changed: its setup, its closed-form residues with exact zeros, B1919's
norms with Theorem 90's weight, the canonical end from B1927's table, and the triplet from the record's q-series. The
script repeats frame_mp's per-sector steps for one point at a time, adds the lepton sector by the same steps, and adds
the singlet of D-2. The coupling and the CKM are frame_mp's: Y[a][b] = sum (C_a^T EPS S C_b) * M_w, |V| = |U_u^H U_d|
with the left singular vectors ordered light to heavy.

D-1: every sector reads S (the shared doublet mode). D-2: the sector's Higgs matrix is R_sec(S) + sigma_sec s 1 in the
worlds W- = (S~ up; S down, lep) and W+ = (S up; S~ down, lep), s = kappa e^(i phi) |c_max|.
"""
import json
import math
import multiprocessing as mpc
import os
import sys
import time
from fractions import Fraction as Fr
import glob

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = sys.argv[1] if len(sys.argv) > 1 else None
if MAIN:
    sys.path.insert(0, glob.glob(os.path.join(MAIN, "frontier", "B1940_*", "verification"))[0])
    _argv = sys.argv
    sys.argv = ["x"]
    import frame_mp as FM  # noqa: E402
    sys.argv = _argv
    B, te, CR = FM.B, FM.te, FM.CR
    H, f2m, UNITS = FM.H, FM.f2m, FM.UNITS

POINTS = {"mark": (Fr(2, 5), Fr(4, 5)), "twin": (Fr(1, 5), Fr(2, 5))}
SECS = ("up", "down", "lep")
D1_YS = (6, 8, 10, 14, 20, 30)
D1_XS = (Fr(0), Fr(13, 100), Fr(1, 4))
D2_YS = (10, 20, 30)
D2_X = Fr(13, 100)
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def tau_setup(tx, ty, extra=0):
    mp.mp.dps = int(30 + 2 * ty) + extra
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(f2m(tx), mp.mpf(ty))
    xr = ((float(tx) + 0.5) % 1.0) - 0.5
    L = mp.mpf(CR.canon(complex(xr, float(ty)))["L_2"])
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))
    c3 = [te.ev(cc, t) for cc in te.B[1]]
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    St = EPS * conj(S) * EPS.T
    return dict(I=I, EPS=EPS, ED=ED, BLOCKS=BLOCKS, t=t, y=mp.im(t), L=L, t1p=2 * mp.pi * eta ** 3,
                th1=lambda z: B.th_mp(1, z, t), c3=c3, S=S, St=St, ONE=mp.eye(2))


def conj(A):
    return mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])


def sector_M(T, a, b, sec):
    """frame_mp.fbar's per-sector steps, for one point and one sector"""
    I, t, y, L = T["I"], T["t"], T["y"], T["L"]
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b)
    yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0]))
    kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    u = {}
    for s in UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]):
            u[s] = 0
            continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / T["t1p"]
        al, be = cs[s][0] - H, cs[s][1] - H
        z = f2m(al) * t + f2m(be)
        a0 = 2 * I * mp.pi * f2m(al) + mp.diff(T["th1"], z) / T["th1"](z)
        c = FM.F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
        c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)
        arg = 2 * mp.pi * L + c
        u[s] = mp.sqrt(arg) * R if arg > 0 else 0
    return sum((u[s] * T["ED"][s] for s in UNITS), mp.zeros(2, 2))


def coupling(T, Sm, Mw):
    EPS = T["EPS"]
    return mp.matrix([[sum(((Ca.T * EPS * Sm * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0))
                       for Cb in T["BLOCKS"]] for Ca in T["BLOCKS"]])


def svd_sorted(Y):
    Uu, Sv, _ = mp.svd_c(Y)
    order = sorted(range(3), key=lambda i: -Sv[i])
    sv = [Sv[i] for i in order]
    U = mp.matrix([[Uu[r, order[2 - c]] for c in range(3)] for r in range(3)])  # columns light to heavy
    return sv, U


def cell(T, Ms, Hm):
    """Hm: the Higgs matrix per sector. Returns ratios, |V|, class, J and the lepton-down double ratios."""
    out, Us = {}, {}
    for sec in SECS:
        sv, U = svd_sorted(coupling(T, Hm[sec], Ms[sec]))
        Us[sec] = U
        out[sec] = (sv[1] / sv[0] if sv[0] != 0 else mp.mpf(0), sv[2] / sv[0] if sv[0] != 0 else mp.mpf(0))
    V = conj(Us["up"]).T * Us["down"]
    A = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    dmin, dmax = min(A[i][i] for i in range(3)), max(A[i][i] for i in range(3))
    cls = "aligned" if dmin >= 0.9 else ("deranged" if dmax <= 0.1 else "partial")
    J = mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))

    def lnD(k):
        lv, dv = out["lep"][k], out["down"][k]
        return float(abs(mp.log(lv / dv))) if lv > 0 and dv > 0 else float("inf")
    return {"r": {s: [mp.nstr(v, 12) for v in out[s]] for s in SECS}, "V": [[mp.nstr(v, 12) for v in r] for r in A],
            "cls": cls, "dmin": float(dmin), "J": mp.nstr(J, 12), "lnD2": lnD(0), "lnD1": lnD(1),
            "hp": float(max(out["up"][0], out["down"][0]))}


def d1_task(args):
    name, x, y, extra = args
    a, b = POINTS[name]
    T = tau_setup(x, y, extra)
    Ms = {sec: sector_M(T, a, b, sec) for sec in SECS}
    res = {"SSS": cell(T, Ms, {s: T["S"] for s in SECS})}
    if extra == 0:
        res["Wm"] = cell(T, Ms, {"up": T["St"], "down": T["S"], "lep": T["S"]})
        res["Wp"] = cell(T, Ms, {"up": T["S"], "down": T["St"], "lep": T["St"]})
    return (name, str(x), y, extra), res


def d2_task(args):
    name, y, extra, kmin = args
    a, b = POINTS[name]
    T = tau_setup(D2_X, y, extra)
    Ms = {sec: sector_M(T, a, b, sec) for sec in SECS}
    cmax = max(abs(c) for c in T["c3"])
    worlds = {"Wm": {"up": T["St"], "down": T["S"], "lep": T["S"]}, "Wp": {"up": T["S"], "down": T["St"], "lep": T["St"]}}
    sig = {"odd": {"up": 1, "down": -1, "lep": -1}, "even": {"up": 1, "down": 1, "lep": 1}}
    out = {"ctrl": {w: cell(T, Ms, R) for w, R in worlds.items()}, "cells": []}
    for w, R in worlds.items():
        for par, sg in sig.items():
            for k in range(kmin, 3):
                kap = mp.mpf(10) ** (mp.mpf(k) / 2)
                for j in range(8):
                    s = kap * mp.exp(mp.mpc(0, 1) * j * mp.pi / 4) * cmax
                    Hm = {sec: R[sec] + sg[sec] * s * T["ONE"] for sec in SECS}
                    c = cell(T, Ms, Hm)
                    out["cells"].append({"w": w, "par": par, "k": k, "j": j, "cls": c["cls"], "dmin": c["dmin"],
                                         "hp": c["hp"], "r_up": c["r"]["up"], "r_down": c["r"]["down"],
                                         "lnD2": c["lnD2"], "lnD1": c["lnD1"], "V": c["V"]})
    return (name, y, extra, kmin), out


def rate(v1, v2, y1, y2):
    return -(math.log(v2) - math.log(v1)) / (math.pi * (y2 - y1)) if v1 > 0 and v2 > 0 else float("nan")


def main():
    if MAIN is None:
        sys.exit("give a checkout of main")
    ctx = mpc.get_context("fork")
    d1_jobs = [(n, x, y, 0) for n in POINTS for x in D1_XS for y in D1_YS] + [(n, x, 30, 20) for n in POINTS for x in D1_XS]
    d2_jobs = [(n, y, 0, -2 * y) for n in POINTS for y in D2_YS] + [(n, 30, 20, 0) for n in POINTS]
    with ctx.Pool(4) as pool:
        D1 = dict(pool.map(d1_task, d1_jobs))
        say("D-1 done  [%.0f s]" % (time.time() - T0))
        D2 = dict(pool.map(d2_task, d2_jobs))
        say("D-2 done  [%.0f s]" % (time.time() - T0))
    json.dump({"D1": {"|".join(map(str, k)): v for k, v in D1.items()},
               "D2": {"|".join(map(str, k)): v for k, v in D2.items()}},
              open(os.path.join(HERE, "wd2_output.json"), "w"), indent=0)

    # ---- D-1 tables
    for n in POINTS:
        for x in D1_XS:
            for y in D1_YS:
                c = D1[(n, str(x), y, 0)]["SSS"]
                say("D-1 %-4s x = %-6s height %2d: %-8s least diagonal %.6f  |V12| %s |V23| %s |V13| %s  J %s  "
                    "up %s  down %s  ln D2 %.1e ln D1 %.1e" % (n, x, y, c["cls"], c["dmin"], c["V"][0][1], c["V"][1][2],
                                                              c["V"][0][2], c["J"], c["r"]["up"], c["r"]["down"],
                                                              c["lnD2"], c["lnD1"]))
            for (i, j) in ((0, 1), (1, 2), (0, 2)):
                vs = [float(D1[(n, str(x), y, 0)]["SSS"]["V"][i][j]) for y in D1_YS]
                rs = [rate(vs[k], vs[k + 1], D1_YS[k], D1_YS[k + 1]) for k in range(len(D1_YS) - 1)]
                say("   rate of |V%d%d| between consecutive heights: %s" % (i + 1, j + 1, " ".join("%.4f" % r for r in rs)))
            js = [abs(float(D1[(n, str(x), y, 0)]["SSS"]["J"])) for y in D1_YS]
            say("   rate of |J|: %s" % " ".join("%.4f" % rate(js[k], js[k + 1], D1_YS[k], D1_YS[k + 1])
                                            for k in range(len(D1_YS) - 1)))

    # ---- D-2 summaries
    for n in POINTS:
        for y in D2_YS:
            r = D2[(n, y, 0, -2 * y)]
            for w in ("Wm", "Wp"):
                cc = r["ctrl"][w]
                say("D-2 %-4s height %2d %s, no singlet: %s (least diagonal %.3e), ln D2 %.1e, ln D1 %.1e"
                    % (n, y, w, cc["cls"], cc["dmin"], cc["lnD2"], cc["lnD1"]))
                for par in ("odd", "even"):
                    cells = [q for q in r["cells"] if q["w"] == w and q["par"] == par]
                    al = [q for q in cells if q["cls"] == "aligned"]
                    ks = sorted(set(q["k"] for q in al))
                    best = min(al, key=lambda q: q["hp"]) if al else None
                    big = [q for q in cells if q["k"] >= 1]
                    say("   %-4s: aligned in %3d of %3d cells (kappa exponents k/2 with k in %s); least heavy-pair ratio "
                        "when aligned %s; largest |ln D| %.3e; kappa >= 3 all aligned: %s"
                        % (par, len(al), len(cells), ks if ks else "none",
                           ("%.3e at k = %d, j = %d" % (best["hp"], best["k"], best["j"])) if best else "none",
                           max(max(q["lnD2"], q["lnD1"]) for q in cells if math.isfinite(max(q["lnD2"], q["lnD1"])))
                           if any(math.isfinite(max(q["lnD2"], q["lnD1"])) for q in cells) else float("nan"),
                           all(q["cls"] == "aligned" for q in big)))

    # ---- controls and expectations
    c1 = all(D2[(n, y, 0, -2 * y)]["ctrl"][w]["cls"] == "deranged" for n in POINTS for y in D2_YS for w in ("Wm", "Wp"))
    c2 = all(max(D1[(n, str(x), y, 0)][w]["lnD2"], D1[(n, str(x), y, 0)][w]["lnD1"]) <= 1e-20
             for n in POINTS for x in D1_XS for y in D1_YS for w in ("Wm", "Wp"))
    c3 = all(D1[(n, str(Fr(13, 100)), y, 0)]["SSS"]["cls"] == "aligned" for n in POINTS for y in (6, 30))
    worst = 0.0
    cls_same = True
    for n in POINTS:
        for x in D1_XS:
            p, q = D1[(n, str(x), 30, 0)]["SSS"], D1[(n, str(x), 30, 20)]["SSS"]
            cls_same &= p["cls"] == q["cls"]
            worst = max(worst, max(abs(float(p["V"][i][j]) - float(q["V"][i][j])) for i in range(3) for j in range(3)))
    for n in POINTS:
        lo = {(q["w"], q["par"], q["k"], q["j"]): q for q in D2[(n, 30, 0, -60)]["cells"] if q["k"] >= 0}
        for q in D2[(n, 30, 20, 0)]["cells"]:
            p = lo[(q["w"], q["par"], q["k"], q["j"])]
            cls_same &= p["cls"] == q["cls"]
            worst = max(worst, max(abs(float(p["V"][i][j]) - float(q["V"][i][j])) for i in range(3) for j in range(3)))
    c4 = cls_same and worst <= 1e-15
    x1 = all(D1[(n, str(x), y, 0)]["SSS"]["cls"] == "aligned" for n in POINTS for x in D1_XS for y in D1_YS)
    x2 = all(rate(float(D1[(n, str(x), 20, 0)]["SSS"]["V"][i][j]), float(D1[(n, str(x), 30, 0)]["SSS"]["V"][i][j]),
                  20, 30) > 0.1 for n in POINTS for x in D1_XS for (i, j) in ((0, 1), (1, 2), (0, 2)))
    x3 = all(max(D1[(n, str(x), y, 0)]["SSS"]["lnD2"], D1[(n, str(x), y, 0)]["SSS"]["lnD1"]) <= 1e-20
             for n in POINTS for x in D1_XS for y in D1_YS)
    allc = [q for n in POINTS for y in D2_YS for q in D2[(n, y, 0, -2 * y)]["cells"]]
    x4 = all(q["cls"] == "aligned" for q in allc if q["k"] >= 1)
    x5 = not any(q["cls"] == "aligned" and q["hp"] <= 1e-2 for q in allc)
    odd_split = any(max(q["lnD2"], q["lnD1"]) > 1e-6 for q in allc if q["par"] == "odd")
    even_split = any(max(q["lnD2"], q["lnD1"]) > 1e-6 for q in allc if q["par"] == "even")
    x6 = odd_split and not even_split
    say("C1 holds:", c1)
    say("C2 holds:", c2)
    say("C3 holds:", c3)
    say("C4 holds:", c4, "| worst |V| change at 20 more digits %.2e, classes unchanged %s" % (worst, cls_same))
    say("X1 holds:", x1)
    say("X2 holds:", x2)
    say("X3 holds:", x3)
    say("X4 holds:", x4)
    say("X5 holds:", x5)
    say("X6 holds:", x6, "| odd splits somewhere %s, even splits somewhere %s" % (odd_split, even_split))
    say("done  [%.0f s]" % (time.time() - T0))


if __name__ == "__main__":
    main()
