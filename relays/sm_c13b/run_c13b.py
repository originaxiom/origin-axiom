#!/usr/bin/env python3
"""SM-C13b: the read-out at order 10 = 5 x 2 over the mark (card relays/cards/SM_C13b_the-read-out-at-order-10.md,
pushed before this run).  Main's frame C as B1928 reads it (B1927's canon_readout: the closed-form channel norm and the
canonical end), imported unchanged from a checkout of main (first argument).
ONLY differences are written: lepton outputs minus down outputs (absolute, and relative); no output value is printed or
saved.
    python3 run_c13b.py MAIN_CHECKOUT PART [workers]      PART in {k1, k234, k5, k6}"""
import json
import math
import multiprocessing as mp
import pathlib
import random
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
PART = sys.argv[2]
WORKERS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
VER = next((MAIN / "frontier").glob("B1927_*")) / "verification"
B1928 = next((MAIN / "frontier").glob("B1928_*")) / "verification"
sys.path.insert(0, str(VER))
sys.path.insert(0, str(B1928))
import canon_readout as CR      # noqa: E402
C = CR.C
LT = {"L_max": 1.3, "L_2": 0.9}
ORDER5 = [(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
ORDER10 = [(i / 10, j / 10) for i in range(10) for j in range(10)
           if math.lcm(10 // math.gcd(i, 10), 10 // math.gcd(j, 10)) == 10]
assert len(ORDER5) == 24 and len(ORDER10) == 72
KEYS = [(h, r) for h in ("L_max", "L_2") for r in ("S", "St")]


def ends(t, mode):
    if mode == "const":
        return {h: LT[h] - 0.5 * math.log(t.imag) for h in LT}
    L = CR.canon(t)
    L.pop("_extrapolated", None)
    return L


def diff_avg(t, points, mode):
    """F-bar^lep - F-bar^down over the points, as a flat vector (KEYS x 2 ratios); and the down average's magnitude
    (used only to form relative differences in memory, never written)"""
    L = ends(t, mode)
    dl = np.zeros(8)
    dn = np.zeros(8)
    for a, b in points:
        o = C.frame(t, a, b, L)
        lep = np.concatenate([np.array(o["lep|%s|%s" % k]) for k in KEYS])
        dwn = np.concatenate([np.array(o["down|%s|%s" % k]) for k in KEYS])
        dl += lep / len(points)
        dn += dwn / len(points)
    return dl - dn, np.abs(dn)


# =========================================================================================== the explicit-charge step
def sector(t, a, b, ql, qr, L):
    """SM-C13's copy of the per-sector step (B1724's frame), on frame C's own modules: {(end, reading): [r1, r2]}"""
    M = C._modules()
    B = M["B"]
    c3 = C.components(t)
    S = c3[0] * B.QI + c3[1] * B.QJ + c3[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    w = float(a) * t + float(b)
    x, yy = B.sector_twists(w, t, ql, qr)
    R = B.residues(x, yy, t)
    c = B.cA(x, yy, t, R)
    out = {}
    for h in ("L_max", "L_2"):
        Lh = L[h]
        u = {s: (math.sqrt(2 * math.pi * Lh + c[s]) * R[s] if c[s] is not None and 2 * math.pi * Lh + c[s] > 0 else 0)
             for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn in ("S", "St"):
            sv = np.linalg.svd(B.coupling(reading[rn], Mw), compute_uv=False)
            out[(h, rn)] = np.array([sv[1] / sv[0], sv[2] / sv[0]])
    return np.concatenate([out[k] for k in KEYS])


def rel(x, y):
    return float(np.max(np.abs(x - y) / np.maximum(np.abs(y), 1e-12)))


def k234():
    out = {"P3_step_reproduces_frame": [], "K2": {}, "K3": {}, "K4": {}}
    for mode in ("const", "canon"):
        for t in C.TAUS:
            L = ends(t, mode)
            # P3: the explicit-charge step reproduces frame C's down and lepton sectors at two order-10 points
            for (a, b) in ORDER10[:2]:
                o = C.frame(t, a, b, L)
                for sec, (ql, qr) in (("down", (1, 2)), ("lep", (-3, 6))):
                    ref = np.concatenate([np.array(o["%s|%s|%s" % (sec, *k)]) for k in KEYS])
                    out["P3_step_reproduces_frame"].append(rel(sector(t, a, b, ql, qr, L), ref))
            lep = np.mean([sector(t, a, b, -3, 6, L) for a, b in ORDER10], axis=0)
            dwn = np.mean([sector(t, a, b, 1, 2, L) for a, b in ORDER10], axis=0)
            neg = np.mean([sector(t, a, b, -1, 2, L) for a, b in ORDER10], axis=0)
            pl = np.mean([sector(t, a, b, 2, 1, L) for a, b in ORDER10], axis=0)
            tag = "%s tau=(%.4f, %.4f)" % (mode, t.real, t.imag)
            out["K2"][tag] = {"%s|%s r%d" % (k[0], k[1], i + 1): rel(lep[2 * j + i], dwn[2 * j + i])
                              for j, k in enumerate(KEYS) for i in range(2)}
            out["K3"][tag] = rel(lep, neg)
            out["K4"][tag] = rel(pl, dwn)
            print(tag, "K2 min %.2e" % min(out["K2"][tag].values()), "K3 %.1e" % out["K3"][tag], "K4 %.1e" % out["K4"][tag],
                  flush=True)
    out["summary"] = {"P3 max": max(out["P3_step_reproduces_frame"]),
                      "K2 min over all": min(min(v.values()) for v in out["K2"].values()),
                      "K2 holds (all > 1e-6)": all(min(v.values()) > 1e-6 for v in out["K2"].values()),
                      "K3 max": max(out["K3"].values()), "K3 holds": max(out["K3"].values()) <= 1e-8,
                      "K4 max": max(out["K4"].values()), "K4 holds": max(out["K4"].values()) <= 1e-8}
    return out


# =========================================================================================== the grid (K1, K5)
def grid_points():
    """B1928's fine grid, as its fiber_grid.py builds it"""
    xs = np.round(np.linspace(-0.5, 0.5, 41), 4)
    ys_top = [1.0, 1.05, 1.1, 1.15, 1.2, 1.275, 1.35, 1.425, 1.5, 1.625, 1.75, 1.875, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0,
              4.5, 5.0, 6.0]
    out = []
    for x in xs:
        lo = math.sqrt(max(0.0, 1 - x * x))
        near = [0.002, 0.015, 0.03, 0.05, 0.08]
        ys = sorted(set([round(lo + d, 4) for d in near] + [y for y in ys_top if y > lo + 0.1]))
        out += [(float(x), float(y)) for y in ys]
    return out


def _grid_task(args):
    (x, y), order = args
    pts = ORDER10 if order == 10 else ORDER5
    t = complex(x, y)
    res = {}
    for mode in ("const", "canon"):
        d, mag = diff_avg(t, pts, mode)
        res[mode] = {"D": d.tolist(), "rel": float(np.max(np.abs(d) / np.maximum(mag, 1e-12)))}
    return [x, y, res]


def grid(order):
    G = grid_points()
    t0 = time.time()
    with mp.Pool(WORKERS) as pool:
        rows = pool.map(_grid_task, [(g, order) for g in G], chunksize=4)
    print("grid order %d: %d points in %.0f s" % (order, len(rows), time.time() - t0), flush=True)
    return rows


# =========================================================================================== the ergodic integral (B1928's route)
def ergodic(rows):
    from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
    import fiber_ergodic as FE        # B1928's thread() and reduce, unchanged (its module-level grid load is B1928's own)
    XY = np.array([[r[0], r[1]] for r in rows])
    out = {}
    rng = random.Random(1924)
    for _ in range(8):                # B1928's P1 draws, consumed so the word sample is the same as B1928's
        x = rng.uniform(-0.5, 0.5)
        rng.uniform(math.sqrt(1 - x * x) + 0.01, 3.0)
    words = []
    while len(words) < 3000:
        w = "".join(rng.choice("LR") for _ in range(40))
        if "L" in w and "R" in w:
            words.append(w)
    for mode in ("const", "canon"):
        V = np.array([r[2][mode]["D"] for r in rows])
        lin, near = LinearNDInterpolator(XY, V), NearestNDInterpolator(XY, V)
        A, wts = [], []
        for w in words:
            pts, ell = FE.thread(w)
            v = lin(pts)
            bad = ~np.all(np.isfinite(v), axis=1)
            if bad.any():
                v[bad] = near(pts[bad])
            A.append(v.mean(0))
            wts.append(ell)
        A, wts = np.array(A), np.array(wts)
        R = (wts[:, None] * A).sum(0) / wts.sum()
        jk = []
        for bl in np.array_split(np.arange(len(words)), 30):
            m = np.ones(len(words), bool)
            m[bl] = False
            jk.append((wts[m][:, None] * A[m]).sum(0) / wts[m].sum())
        jk = np.array(jk)
        se = np.sqrt((len(jk) - 1) * np.mean((jk - R) ** 2, 0))
        z = np.abs(R) / np.maximum(se, 1e-300)
        labels = ["%s|%s r%d" % (k[0], k[1], i + 1) for k in KEYS for i in range(2)]
        out[mode] = {"integral of D": dict(zip(labels, R.tolist())), "se": dict(zip(labels, se.tolist())),
                     "z": dict(zip(labels, z.tolist())), "share z > 3": float(np.mean(z > 3))}
        print(mode, "share of outputs with z > 3: %.2f; z range %.1f to %.1f" % (np.mean(z > 3), z.min(), z.max()), flush=True)
    return out


if __name__ == "__main__":
    t0 = time.time()
    if PART == "k234":
        res = k234()
    elif PART == "k1":
        rows = grid(5)
        res = {"rows": rows, "K1 max rel": max(max(r[2][m]["rel"] for m in r[2]) for r in rows)}
        res["K1 holds"] = res["K1 max rel"] <= 1e-8
        print("K1 max rel %.2e" % res["K1 max rel"], flush=True)
    elif PART == "k5":
        rows = grid(10)
        res = {"rows": rows, "ergodic": ergodic(rows)}
    elif PART == "k6":
        rows = json.loads((HERE / "c13b_k1.json").read_text())["rows"]
        res = {"ergodic": ergodic(rows)}
        res["K6 max |integral|"] = max(abs(v) for m in res["ergodic"].values() for v in m["integral of D"].values())
    (HERE / ("c13b_%s.json" % PART)).write_text(json.dumps(res, indent=1))
    print("done %s in %.0f s" % (PART, time.time() - t0), flush=True)
