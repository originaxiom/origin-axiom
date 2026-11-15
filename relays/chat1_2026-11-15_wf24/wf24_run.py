#!/usr/bin/env python3
"""W-F24: where frame C's read-out loses the hierarchy. Data-free: no data is opened and no output is compared with any
measured number (the author's ruling of 2026-11-15 allows the frame's outputs to be computed and printed).

    python3 -I -u wf24_run.py            # two worker processes

THE FRAME. This seat's transcription of B1656's frame (W-F22's wf22_outputs.py: thc, bil, pairs, twist_of, residues,
a0_of, cA, EDUAL, weighted_M, coupling) with this seat's own triplet (wf22_checks.py). Frame C's ingredients, re-typed:
  - the canonical end L_2(tau) from B1927's grid.json and B1667's the_canonical_cusp.json (mirrored in Re tau, linear
    interpolation with a nearest-point fallback, height clamped at the tables' top), as B1927 builds it;
  - Theorem 90's weight (B1932): u_s = sqrt(2 pi L_2 + c_s - pi |a0_s|^2 exp(-2 L_2)) R_s, c_s by this seat's quadrature
    (B1656's cA; main used B1924's closed form);
  - the horocycle of length 2 only; the readings S and St (S* excluded, B1922).
  Outputs per sector (up, down, lep) and reading: r2 = s2/s1 and r3 = s3/s1 of the coupling's singular values.

THE AVERAGES. F(tau, p) at the 24 points p of order 5 (B1928's POINTS). Fibre: A(tau) = mean_p F (frame C's F-bar);
G(tau) = exp mean_p log F. Surface: the path measure mu, as B1924 and B1928 define it: random words of 40 letters in
L = [[1,1],[0,1]] and R = [[1,0],[1,1]] (uniform), each word's thread the closed geodesic of W^T, sampled by arclength
over one period, every node carried into the fundamental domain; each word weighted by its length (B1928's H3). F-bar is
SL(2, Z)-invariant, so the node's reduction needs tau only. Values at the nodes: linear interpolation on this run's grid
(of A, and of log G), nearest point outside it, height clamped at the grid's top (the share clamped is printed).
  A_read = E_mu[A] (frame C's form); G_read = exp E_mu[log G] (the proposal).

EXPECTATIONS (card W-F24, committed at e7bebf402 before any frame output was computed; made exact here):
  X1  At the mark p = (2/5, 4/5), for at least one sector ratio (sector, reading, r2 or r3), the mean over the grid's
      columns of log F at height 6 minus log F at height 2 is below -1.
  X2  At more than half of the grid points with Im tau < 1.5, at least one sector ratio has max_p F / min_p F > 10.
  X3  At more than half of those points, at least one sector ratio has A / G > 3.
  X4  mu's share of time above height 2 is below 0.10.
  X5  G_read < A_read for every sector ratio.
  Plants (at every grid point, exact to 1e-9 relative):
    PL1 the value at the first point multiplied by 10 moves A by (sum + 9 r_p) / sum and G by 10^(1/24);
    PL2 the composition identity, A(r3) = A(r2) A(r3 / r2), fails (relative error above 1e-3 at some grid point), and
        G(r3) = G(r2) G(r3 / r2) holds (below 1e-9 at every grid point).
  Before the seal the pipeline was run once with the frame replaced by random numbers (a smoke test). No frame output
  was computed. That run did compute mu's height shares, which do not depend on the frame: X4 was committed with the
  card before it, but is not blind here.
  Reported, no expectation: the height law of the mark's log ratios (slope per unit of Im tau over 2 to 6), the
  fibre's spread, A_read, G_read and their ratio for every sector ratio, mu's shares above heights 1.5, 2, 3, 4.
"""
import json
import math
import os
import random
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "relays", "chat1_2026-11-14_wf22", "wf22_outputs.py")
_s = open(SRC).read()
NS = {"__file__": SRC}
exec(_s[:_s.index("def dev(x, y):")], NS)          # the transcription's functions and the triplet; computes nothing
mp = NS["mp"]


def say(*a):
    print(*a, flush=True)


# ---------------- the canonical end (B1927's construction, this seat's code)
def end_tables(main_root):
    from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
    g = json.load(open(os.path.join(main_root, "frontier", next(d for d in os.listdir(os.path.join(main_root, "frontier"))
                                                                 if d.startswith("B1927_")), "verification", "grid.json")))["grid"]
    c = json.load(open(os.path.join(main_root, "frontier", "B1667_the_canonical_cusp", "verification",
                                    "the_canonical_cusp.json")))["points"]
    pts = [p for p in g if "L_2" in p] + [p for p in c if "L_2" in p]
    XY = np.array([(s * p["tau"][0], p["tau"][1]) for p in pts for s in (1, -1)])
    V = np.array([p["L_2"] for p in pts for s in (1, -1)])
    return LinearNDInterpolator(XY, V), NearestNDInterpolator(XY, V), float(XY[:, 1].max())


MAIN = os.environ.get("MAIN_CHECKOUT")
LIN = NEAR = YMAX = None


def L2_of(t):
    v = float(LIN(t.real, min(t.imag, YMAX)))
    return v if np.isfinite(v) else float(NEAR(t.real, min(t.imag, YMAX)))


# ---------------- frame C at one (tau, p)
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
POINTS = [(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
KEYS = ["%s|%s|%s" % (sec, rn, r) for sec in SECT for rn in ("S", "St") for r in ("r2", "r3")]


def frame_c(t, a, b, L2, c3):
    QI, QJ, QK, EPS, UNITS = NS["QI"], NS["QJ"], NS["QK"], NS["EPS"], NS["UNITS"]
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    reading = {"S": S, "St": EPS @ np.conj(S) @ EPS.T}
    w = a * t + b
    out = {}
    for sec, (lf, rf) in SECT.items():
        x, yy = NS["twist_of"](NS["SIXY"][lf] * w, t), NS["twist_of"](NS["SIXY"][rf] * w, t)
        R = NS["residues"](x, yy, t)
        c = NS["cA"](x, yy, t, R)
        a0 = NS["a0_of"](x, yy, t, R)
        u = {}
        for s in UNITS:
            if c[s] is None or a0[s] is None:
                u[s] = 0
                continue
            N = 2 * math.pi * L2 + c[s] - math.pi * abs(a0[s]) ** 2 * math.exp(-2 * L2)
            u[s] = math.sqrt(N) * R[s] if N > 0 else 0
        Mw = NS["weighted_M"](u)
        for rn in ("S", "St"):
            sv = np.linalg.svd(NS["coupling"](reading[rn], Mw), compute_uv=False)
            out["%s|%s|r2" % (sec, rn)] = float(sv[1] / sv[0])
            out["%s|%s|r3" % (sec, rn)] = float(sv[2] / sv[0])
    return out


def at_tau(xy):
    global LIN, NEAR, YMAX
    if LIN is None:
        LIN, NEAR, YMAX = end_tables(MAIN)
    t = complex(*xy)
    c3 = [complex(v) for v in NS["av"](mp.mpc(t.real, t.imag))]
    L2 = L2_of(t)
    return {"tau": list(xy), "L2": L2, "F": [frame_c(t, a, b, L2, c3) for a, b in POINTS]}


# ---------------- the grid
def grid():
    out = []
    for x in np.round(np.linspace(-0.5, 0.5, 11), 4):
        lo = math.sqrt(max(0.0, 1 - x * x))
        ys = [lo + 0.01, lo + 0.05, lo + 0.12] + [y for y in (1.2, 1.35, 1.5, 1.75, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0)
                                                   if y > lo + 0.17]
        out += [(float(x), round(float(y), 4)) for y in ys]
    return out


# ---------------- mu
LM = np.array([[1, 1], [0, 1]])
RM = np.array([[1, 0], [1, 1]])


def reduce_fd(z):
    for _ in range(200):
        z = complex(z.real - math.floor(z.real + 0.5), z.imag)
        if abs(z) < 1 - 1e-12:
            z = -1 / z
        else:
            return z
    return z


def thread_nodes(word):
    W = np.eye(2, dtype=np.int64)
    for ch in word:
        W = W @ (LM if ch == "L" else RM)
    g = W.T
    a, b, c, d = [int(v) for v in g.ravel()]
    tr = a + d
    ell = 2 * math.acosh(abs(tr) / 2)
    disc = math.sqrt((d - a) ** 2 + 4 * b * c)
    r1, r2 = ((a - d) + disc) / (2 * c), ((a - d) - disc) / (2 * c)
    beta, betap = max(r1, r2), min(r1, r2)
    n = max(64, int(30 * ell))
    zs = [(beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1) for s in np.linspace(0, ell, n, endpoint=False)]
    return [reduce_fd(z) for z in zs], ell


def main():
    global MAIN
    if MAIN is None:
        raise SystemExit("set MAIN_CHECKOUT to a checkout of main (the end's tables are read from it)")
    G = grid()
    say("grid points:", len(G), "| points of order 5:", len(POINTS))
    t0 = time.time()
    with Pool(2) as P:
        rows = P.map(at_tau, G, chunksize=1)
    say("frame done in %.0f s" % (time.time() - t0))
    json.dump(rows, open(os.path.join(HERE, "wf24_grid.json"), "w"))

    # fibre means
    for r in rows:
        r["A"], r["G"] = {}, {}
        for k in KEYS:
            v = np.array([f[k] for f in r["F"]])
            r["A"][k] = float(v.mean())
            r["G"][k] = float(math.exp(np.log(v).mean()))
    # plants
    pl1 = pl2a = pl2g = True
    pl2a_fail = False
    for r in rows:
        for k in KEYS:
            v = np.array([f[k] for f in r["F"]])
            v2 = v.copy(); v2[0] *= 10
            pl1 &= abs(v2.mean() / v.mean() - (v.sum() + 9 * v[0]) / v.sum()) < 1e-9
            pl1 &= abs(math.exp(np.log(v2).mean()) / math.exp(np.log(v).mean()) / 10 ** (1 / 24) - 1) < 1e-9
        for sec in SECT:
            for rn in ("S", "St"):
                v2 = np.array([f["%s|%s|r2" % (sec, rn)] for f in r["F"]])
                v3 = np.array([f["%s|%s|r3" % (sec, rn)] for f in r["F"]])
                q = v3 / v2
                ea = abs(v3.mean() / (v2.mean() * q.mean()) - 1)
                eg = abs(math.exp(np.log(v3).mean()) / (math.exp(np.log(v2).mean()) * math.exp(np.log(q).mean())) - 1)
                pl2a_fail |= ea > 1e-3
                pl2g &= eg < 1e-9
    say("PL1 holds:", pl1, "| PL2 the arithmetic composition fails somewhere:", pl2a_fail, "| the geometric one holds:", pl2g)

    # X1 and the height law, at the mark
    mark = POINTS.index((0.4, 0.8))
    cols = sorted(set(r["tau"][0] for r in rows))
    x1, slopes = False, {}
    for k in KEYS:
        d, sl = [], []
        for x in cols:
            col = sorted((r["tau"][1], math.log(r["F"][mark][k])) for r in rows if r["tau"][0] == x and r["tau"][1] >= 2.0)
            if len(col) >= 2 and col[0][0] == 2.0 and col[-1][0] == 6.0:
                d.append(col[-1][1] - col[0][1])
                ys, ls = zip(*col)
                sl.append(np.polyfit(ys, ls, 1)[0])
        slopes[k] = (float(np.mean(d)), float(np.mean(sl)))
        x1 |= np.mean(d) < -1
    say("X1 holds:", x1)
    say("  the mark's height law (mean over columns): log F(6) - log F(2), and the slope per unit of Im tau:")
    for k in KEYS:
        say("   %-14s %+8.3f  %+8.3f" % (k, slopes[k][0], slopes[k][1]))

    # X2, X3: the fibre
    bulk = [r for r in rows if r["tau"][1] < 1.5]
    s2 = sum(1 for r in bulk if any(max(f[k] for f in r["F"]) / min(f[k] for f in r["F"]) > 10 for k in KEYS))
    s3 = sum(1 for r in bulk if any(r["A"][k] / r["G"][k] > 3 for k in KEYS))
    say("X2 holds:", s2 > len(bulk) / 2, "(%d of %d bulk points)" % (s2, len(bulk)),
        "| X3 holds:", s3 > len(bulk) / 2, "(%d of %d)" % (s3, len(bulk)))
    say("  the fibre over the bulk points, per sector ratio: median of max_p/min_p, median of A/G")
    for k in KEYS:
        sp_ = [max(f[k] for f in r["F"]) / min(f[k] for f in r["F"]) for r in bulk]
        ag = [r["A"][k] / r["G"][k] for r in bulk]
        say("   %-14s %10.3g  %8.3g" % (k, float(np.median(sp_)), float(np.median(ag))))

    # mu
    from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
    XY = np.array([r["tau"] for r in rows])
    ytop = float(XY[:, 1].max())
    IA = {k: (LinearNDInterpolator(XY, [r["A"][k] for r in rows]), NearestNDInterpolator(XY, [r["A"][k] for r in rows]))
          for k in KEYS}
    IG = {k: (LinearNDInterpolator(XY, [math.log(r["G"][k]) for r in rows]),
              NearestNDInterpolator(XY, [math.log(r["G"][k]) for r in rows])) for k in KEYS}

    rng = random.Random(20261115)
    Z, Wt = [], []
    NW = 1000
    for _ in range(NW):
        word = "".join(rng.choice("LR") for _ in range(40))
        if "L" not in word or "R" not in word:
            continue
        zs, ell = thread_nodes(word)
        Z += zs
        Wt += [ell / len(zs)] * len(zs)
    Z, Wt = np.array(Z), np.array(Wt)
    X, Y = Z.real, np.minimum(Z.imag, ytop)

    def vals(I):
        v = I[0](X, Y)
        bad = ~np.isfinite(v)
        if bad.any():
            v[bad] = I[1](X[bad], Y[bad])
        return v

    wsum = Wt.sum()
    shares = {h: float(Wt[Z.imag > h].sum() / wsum) for h in (1.5, 2.0, 3.0, 4.0)}
    clamped = float(Wt[Z.imag > ytop].sum() / wsum)
    say("X4 holds:", shares[2.0] < 0.10, "| mu's shares above 1.5, 2, 3, 4:", {h: round(v, 4) for h, v in shares.items()},
        "| clamped above the grid's top: %.4f" % clamped, "| nodes:", len(Z))
    Ar = {k: float((Wt * vals(IA[k])).sum() / wsum) for k in KEYS}
    Gr = {k: float(math.exp((Wt * vals(IG[k])).sum() / wsum)) for k in KEYS}
    say("X5 holds:", all(Gr[k] < Ar[k] for k in KEYS))
    say("  the read-outs (no comparison with anything measured): A_read (frame C's form), G_read (geometric), A/G")
    for k in KEYS:
        say("   %-14s %10.4g  %10.4g  %8.3g" % (k, Ar[k], Gr[k], Ar[k] / Gr[k]))
    json.dump({"slopes": slopes, "shares": shares, "A_read": Ar, "G_read": Gr,
               "fibre": [{"tau": r["tau"], "A": r["A"], "G": r["G"]} for r in rows]},
              open(os.path.join(HERE, "wf24_summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
