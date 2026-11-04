#!/usr/bin/env python3
"""W184 — B1814's census rerun blind, from its sealed card (86cb26b30), on this seat's own code (the rule:
W184_RULE.md, committed and pushed before this script).  It runs once, from the repository root, on four workers.

The clocks: A0, every Lyndon word in L < R of length 2-16 (Duval); A1, every one of trace 3-400 (FKM pre-necklaces
pruned by the trace).  A draw: a class with probability l/sum(l), l = 2 arccosh(t/2); s uniform in [0, l) from the
axis's top, z = m + r tanh s + i r sech s; reduced exactly (integer gamma, 60 digits); one of the class's own lines
(vA = +-v, exact order 1-12, one per sign pair) uniformly, transported by gamma^-1.  The frame: W178's machinery with
the record's residue cut |R_s| <= 1e-12, both readings, both horocycles (B1667's L_max, L_2, Im tau clamped to [1, 4]),
the CKM per reading pair, at p = 40 + ceil(8 pi Im tau / ln 10); Im tau > 60 not computed.  The worlds: the unforced
mixture (horocycle and each sector's reading uniform per draw, c = 1) and by hand ((S~, S, S), c = 3), the horocycle
from one sequence for both arms.  Resolved: the world's six all above 1e-12.

  C1a-C1e, C2, C3  the controls (the rule)
  D1   A1, unforced, the six: p_nn > 0.05
  D1h  A1, by hand, the six: p_nn > 0.05
  D2   unforced, the six: p_F(A1) > 0.05 and p_F(A0) <= 0.05
  R    read-outs, the power beside each verdict

    python3 -B docs/dossiers/the_weave_2026-10-07/the_measured_world_rerun.py

Disclosed, after the rule's push and before this commit:
- a timing call: the clocks (0.3 s), the 8 000 draws (4.0 s; it printed the counts of draws above Im tau 12 and 60,
  312 and 44, heights the card calls foreknown), and the frame on (1/7, 4/7) at Im tau 1.5, 30 and 60 (statuses,
  digits and seconds only: 57, 368 and 695 digits; 0.24, 0.79 and 2.32 s);
- a dry run of the analysis end to end on a synthetic census (random records), with the targets and sigmas stubbed,
  so no data was read; it printed only that it ran;
- before the script, two data-free instrument checks of the covariance (the six and the CKM), printing residuals only.
"""
import bisect
import contextlib
import io
import json
import math
import multiprocessing as mpc
import platform
import random
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_six_at_the_cusp as W178          # noqa: E402  (W178: the frame's machinery and its precisions)
    import the_third_opinion_b1735 as T42      # noqa: E402  (W142: B1741's measure, B1726's census, C2)
T8, W93, W162, W177, W58 = W178.T8, W178.W93, W178.W162, W178.W177, W178.W58
mp = W177.mp
sys.setrecursionlimit(20000)

OUT = HERE / "the_measured_world_rerun.json"
SEEDS = {"A0": 18440, "A1": 18441, "config": 18442, "anarchy": 18443, "holdout": 18444, "precision": 18445}
NDRAW, NANARCHY, NHOLD, NPOWER = 4000, 1000, 500, 500
RH_SEEDS = list(range(1741, 1761))
RH_N, RH_FREE = 4000, 1000
CAP, CUT, FLOOR = 60.0, 1e-12, 1e-12
FLOORS_RO = (1e-16, 1e-8)
ALPHA = 0.05
BAR = 0.01 / 53
LN3 = math.log(3)
RD, HORO, SECS = ("S", "St"), ("L_max", "L_2"), ("up", "down", "lep")
WORKERS = 4
PREC_SHARE = 0.02
LINES_FOR_C1C = ((Fr(1, 7), Fr(2, 7)), (Fr(2, 5), Fr(3, 10)))
_G = {}


# ============================================================================================ the clocks
LM, RM = (1, 0, 1, 1), (1, 1, 0, 1)


def mul(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def word_matrix(w):
    M = (1, 0, 0, 1)
    for x in w:
        M = mul(M, RM if x else LM)
    return M


def lyndon_by_length(nmax):
    w = [-1]
    while w:
        w[-1] += 1
        yield tuple(w)
        m = len(w)
        while len(w) < nmax:
            w.append(w[-m])
        while w and w[-1] == 1:
            w.pop()


def lyndon_by_trace(T):
    out = []

    def rec(w, M, p, hasR):
        n = len(w)
        if hasR and p == n:
            out.append(tuple(w))
        for x in (0, 1):
            if x < w[n - p]:
                continue
            M2 = mul(M, RM if x else LM)
            h2 = hasR or x == 1
            if (h2 and M2[0] + M2[3] > T) or (not h2 and n + 3 > T):
                continue
            w.append(x)
            rec(w, M2, p if x == w[n - p] else n + 1, h2)
            w.pop()
    rec([0], LM, 1, False)
    return out


def clocks():
    A0 = [w for w in lyndon_by_length(16) if len(w) >= 2]
    A1 = lyndon_by_trace(400)
    out = {}
    for name, ws in (("A0", A0), ("A1", A1)):
        rows = []
        for w in ws:
            M = word_matrix(w)
            t = M[0] + M[3]
            rows.append((w, M, t, 2 * math.acosh(t / 2)))
        out[name] = rows
    return out


def word_str(w):
    return "".join("R" if x else "L" for x in w)


# ============================================================================================ the thread's lines
def own_lines(M):
    """every line of exact order 1-12 the matrix fixes up to sign, one per sign pair, as (i/N, j/N)"""
    a, b, c, d = M
    out = []
    for N in range(1, 13):
        for i in range(N):
            for j in range(N):
                if math.gcd(math.gcd(i, j), N) != 1:
                    continue
                v = ((i * a + j * c) % N, (i * b + j * d) % N)
                neg = ((-i) % N, (-j) % N)
                if v != (i, j) and v != neg:
                    continue
                if (i, j) > neg:
                    continue
                out.append((Fr(i, N), Fr(j, N)))
    return out


def order(line):
    return math.lcm(line[0].denominator, line[1].denominator)


# ============================================================================================ the point
def draw_point(M, s, dps=60):
    a, b, c, d = M
    with mp.workdps(dps):
        t = a + d
        disc = mp.sqrt(mp.mpf(t * t - 4))
        m, r = mp.mpf(a - d) / (2 * c), disc / (2 * abs(c))
        s = mp.mpf(s)
        z0 = mp.mpc(m + r * mp.tanh(s), r / mp.cosh(s))
        z, g = z0, (1, 0, 0, 1)
        for _ in range(100000):
            n = int(mp.floor(mp.re(z) + mp.mpf(1) / 2))
            if n:
                z -= n
                g = mul((1, -n, 0, 1), g)
            if abs(z) < 1:
                z = -1 / z
                g = mul((0, -1, 1, 0), g)
            else:
                break
        A, B, C, D = g
        res = abs((A * z0 + B) / (C * z0 + D) - z) / abs(z)
        return z, g, float(res)


def transport(line, g):
    A, B, C, D = g
    al, be = line
    return ((al * D - be * C) % 1, (-al * B + be * A) % 1)


# ============================================================================================ the frame
def svd_sorted(Y, uv):
    if not uv:
        return None, sorted(abs(v) for v in mp.svd_c(Y, compute_uv=False))
    U, S, _V = mp.svd_c(Y, compute_uv=True)
    sv = [abs(S[i]) for i in range(3)]
    idx = sorted(range(3), key=lambda i: sv[i])
    Us = mp.matrix(3, 3)
    for col, i in enumerate(idx):
        for row in range(3):
            Us[row, col] = U[row, i]
    return Us, [sv[i] for i in idx]


def lnf(v):
    return float(mp.log(v)) if v > 0 else -math.inf


def frame_at(line, x, y, p, Ls=None):
    """per (sector, horocycle, reading) the two log-ratios [ln s_mid/s_max, ln s_min/s_max] and their log10; per
    (horocycle, up reading, down reading) ln |V_us|, |V_cb|, |V_ub|; Ls overrides the radii (C1c)"""
    a, b = line
    with mp.workdps(p):
        CM, EPSM, _B, EM = W93.units("mp")
        t = mp.mpc(mp.mpf(x), mp.mpf(y))
        dr = W178.DR_mp(t, p)
        S = dr[0] * CM["i"] + dr[1] * CM["j"] + dr[2] * CM["k"]
        reads = {"S": S, "St": EPSM * W178.mat_conj(S) * EPSM.T}
        yc = min(max(y, 1.0), 4.0)
        if Ls is None:
            Ls = {h: mp.mpf(T8.L_at(_G["col"], yc, h)) for h in HORO}
        six, six10, U = {}, {}, {}
        for sec in SECS:
            qL, qR = T8.charges(W93, sec)
            R = W93.residues((a, -b), sec, t)
            k = T8.kappa(qL, qR, a, b, t)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            terms = []
            for s in T8.UNITS:
                if W178.theta_zero(W178.W89TH[s], line, qL + qR):
                    continue
                Rs = k * R[s]
                if abs(Rs) <= CUT:
                    continue
                terms.append((s, Rs, W177.c_series(W178.W89TH[s], ub, t)))
            for h in HORO:
                M = mp.zeros(2, 2)
                for s, Rs, cs in terms:
                    w = 2 * mp.pi * Ls[h] + cs
                    if w > 0:
                        M += mp.sqrt(w) * Rs * EM[s]
                for rd in RD:
                    Y = W93.coupling_mp(reads[rd], M)
                    Us, sv = svd_sorted(Y, sec != "lep")
                    if sec != "lep":
                        U[(sec, h, rd)] = Us
                    r2 = sv[1] / sv[2] if sv[2] > 0 else mp.mpf(0)
                    r1 = sv[0] / sv[2] if sv[2] > 0 else mp.mpf(0)
                    six[f"{sec}|{h}|{rd}"] = [lnf(r2), lnf(r1)]
                    six10[f"{sec}|{h}|{rd}"] = [float(mp.log10(r2)) if r2 > 0 else -math.inf,
                                                float(mp.log10(r1)) if r1 > 0 else -math.inf]
        ckm = {}
        for h in HORO:
            for ru in RD:
                for rdn in RD:
                    V = U[("up", h, ru)].H * U[("down", h, rdn)]
                    ckm[f"{h}|{ru}|{rdn}"] = [lnf(abs(V[0, 1])), lnf(abs(V[1, 2])), lnf(abs(V[0, 2]))]
        return {"six": six, "six10": six10, "ckm": ckm}


def precision(y):
    return W178.precisions(y)[0]


# ============================================================================================ the workers
def _init(root_str):
    W178._init(root_str)
    _G["col"] = W178._G["col"]


def sanitize(text):
    return W178.sanitize(text)


def frame_task(task):
    key, line, x, y, extra = task
    t0 = time.time()
    try:
        p = precision(y) + extra
        r = frame_at(line, x, y, p)
        r.update({"key": key, "digits": p, "seconds": round(time.time() - t0, 2)})
        return r
    except Exception:  # noqa: BLE001
        return {"key": key, "failed": sanitize(traceback.format_exc()[-1500:])}


# ============================================================================================ the census
def make_draws(cl):
    draws = {}
    for arm in ("A0", "A1"):
        rows = cl[arm]
        cum, tot = [], 0.0
        for _w, _M, _t, ell in rows:
            tot += ell
            cum.append(tot)
        rng = random.Random(SEEDS[arm])
        out = []
        for i in range(NDRAW):
            ci = bisect.bisect_right(cum, rng.random() * tot)
            ci = min(ci, len(rows) - 1)
            w, M, t, ell = rows[ci]
            s = rng.random() * ell
            z, g, res = draw_point(M, s)
            lines = own_lines(M)
            v = lines[rng.randrange(len(lines))]
            v2 = transport(v, g)
            out.append({"i": i, "class": ci, "word": word_str(w), "trace": t, "length": ell, "s": s,
                        "tau": [float(mp.re(z)), float(mp.im(z))], "gamma": list(g), "reduction residual": res,
                        "thread line": [str(v[0]), str(v[1])], "line": [str(v2[0]), str(v2[1])],
                        "order": order(v2), "lines on the thread": len(lines)})
        draws[arm] = out
    rng = random.Random(SEEDS["config"])
    cfg = [{"h": rng.randrange(2), "r": [rng.randrange(2) for _ in range(3)]} for _ in range(NDRAW)]
    return draws, cfg


# ============================================================================================ the worlds
def world(rec, h, reads, c):
    """the world's six from a draw's frame record: (up, down, lep) at horocycle h with the given readings"""
    if rec is None:
        return None
    six = []
    for sec, rd in zip(SECS, reads):
        six += rec["six"][f"{sec}|{HORO[h]}|{RD[rd]}"]
    if c == 3:
        six[4] += LN3
        six[5] -= LN3
    return np.array(six)


def nine(rec, h, reads, c):
    w = world(rec, h, reads, c)
    if w is None:
        return None
    return np.concatenate([w, rec["ckm"][f"{HORO[h]}|{RD[reads[0]]}|{RD[reads[1]]}"]])


BYHAND = (1, 0, 0)
TRIPLES = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]


def arm_worlds(recs, cfg, mode, floor=FLOOR, use_nine=False):
    """the resolved worlds of one arm under one configuration: an (n, k) array and the draw indices"""
    X, idx = [], []
    lf = math.log(floor)
    for i, rec in enumerate(recs):
        if rec is None:
            continue
        h = cfg[i]["h"]
        if mode == "unforced":
            reads, c = cfg[i]["r"], 1
        elif mode == "byhand":
            reads, c = BYHAND, 3
        else:
            reads, c = mode
        x = (nine if use_nine else world)(rec, h, reads, c)
        if x is None or not np.all(np.isfinite(x)) or np.any(x[:6] <= lf):
            continue
        X.append(x)
        idx.append(i)
    return (np.array(X) if X else np.zeros((0, 9 if use_nine else 6))), idx


def unconditioned(recs, cfg, mode):
    X = []
    for i, rec in enumerate(recs):
        if rec is None:
            continue
        h = cfg[i]["h"]
        reads, c = (cfg[i]["r"], 1) if mode == "unforced" else (BYHAND, 3)
        x = world(rec, h, reads, c)
        X.append(np.maximum(np.nan_to_num(x, neginf=math.log(1e-300)), math.log(1e-300)))
    return np.array(X)


# ============================================================================================ the statistics
def nn_self(Z, chunk=400):
    n = len(Z)
    d = np.full(n, np.inf)
    for a in range(0, n, chunk):
        D = np.max(np.abs(Z[a:a + chunk, None, :] - Z[None, :, :]), axis=2)
        for k in range(D.shape[0]):
            D[k, a + k] = np.inf
        d[a:a + chunk] = D.min(axis=1)
    return d


def nn_target(T, Z, chunk=400):
    T = np.atleast_2d(T)
    d = np.empty(len(T))
    for a in range(0, len(T), chunk):
        d[a:a + chunk] = np.max(np.abs(T[a:a + chunk, None, :] - Z[None, :, :]), axis=2).min(axis=1)
    return d


class NN:
    def __init__(self, X, sig):
        self.sig = sig
        self.Z = X / sig
        self.d = nn_self(self.Z) if len(X) > 1 else np.zeros(len(X))
        self.ds = np.sort(self.d)

    def p(self, T):
        dt = nn_target(np.atleast_2d(T) / self.sig, self.Z)
        return 1.0 - np.searchsorted(self.ds, dt, side="left") / len(self.ds), dt

    def q95(self):
        return float(np.quantile(self.d, 0.95))


class Fisher:
    def __init__(self, X):
        self.S = np.sort(X, axis=0)
        n = len(X)
        self.n = n
        F = np.empty_like(X)
        for k in range(X.shape[1]):
            lo = np.searchsorted(self.S[:, k], X[:, k], side="left")
            hi = np.searchsorted(self.S[:, k], X[:, k], side="right")
            F[:, k] = (lo + 0.5 * (hi - lo - 1) + 0.5) / n
        self.Xs = np.sort(self.stat(F))

    @staticmethod
    def stat(F):
        p = np.minimum(1.0, 2 * np.minimum(F, 1 - F))
        return -2 * np.log(p).sum(axis=1)

    def marg(self, T):
        T = np.atleast_2d(T)
        F = np.empty_like(T, dtype=float)
        for k in range(T.shape[1]):
            lo = np.searchsorted(self.S[:, k], T[:, k], side="left")
            hi = np.searchsorted(self.S[:, k], T[:, k], side="right")
            F[:, k] = (lo + 0.5 * (hi - lo) + 0.5) / (self.n + 1)
        return F

    def p(self, T):
        X = self.stat(self.marg(T))
        return 1.0 - np.searchsorted(self.Xs, X, side="left") / len(self.Xs)

    def marginal_p(self, t):
        F = self.marg(t)[0]
        return [float(min(1.0, 2 * min(f, 1 - f))) for f in F]


def anarchy_six(n, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n):
        six = []
        for _sec in range(3):
            Y = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
            sv = np.sort(np.linalg.svd(Y, compute_uv=False))
            six += [math.log(sv[1] / sv[2]), math.log(sv[0] / sv[2])]
        out.append(six)
    return np.array(out)


def share_le(p, a=ALPHA):
    return float(np.mean(np.asarray(p) <= a)) if len(p) else None


def grade(holds, r):
    if not holds:
        return "FAILS"
    return "PASSED" if (r is not None and r < BAR) else "CONSISTENT, NOT SPECIFIC"


# ============================================================================================ the run
def run(out, pool):
    t00 = time.time()
    cl = clocks()
    tr = [t for _w, _M, t, _l in cl["A1"]]
    c1a = {"A0": len(cl["A0"]), "A0 length <= 14": sum(1 for w, *_ in cl["A0"] if len(w) <= 14),
           "A1": len(cl["A1"]), "A1 by trace <= 12, 18, 24, 30, 400": [sum(1 for t in tr if t <= T)
                                                                      for T in (12, 18, 24, 30, 400)]}
    c1a["holds"] = (c1a["A0"] == 8798 and c1a["A0 length <= 14"] == 2536 and c1a["A1"] == 14690
                    and c1a["A1 by trace <= 12, 18, 24, 30, 400"] == [29, 60, 96, 151, 14690])
    out["C1a"] = c1a
    draws, cfg = make_draws(cl)
    out["C1b"] = {"max reduction residual": max(d["reduction residual"] for a in draws.values() for d in a)}
    out["C1b"]["holds"] = out["C1b"]["max reduction residual"] < 1e-30
    print("draws made at", round(time.time() - t00), "s", flush=True)
    # ---- the frame tasks: the census, C3, C1e
    tasks = []
    for arm in ("A0", "A1"):
        for d in draws[arm]:
            if d["tau"][1] <= CAP:
                tasks.append(((arm, d["i"], 0), (Fr(d["line"][0]), Fr(d["line"][1])), d["tau"][0], d["tau"][1], 0))
    prng = random.Random(SEEDS["precision"])
    psample = [t for t in tasks if prng.random() < PREC_SHARE]
    tasks += [((k[0], k[1], 60), ln, x, y, 60) for k, ln, x, y, _e in psample]
    lines266 = T8.own_lines()
    tasks += [(("C1e", li, xi), ln, x, CAP, 0) for li, ln in enumerate(lines266) for xi, x in enumerate((0.05, 0.3))]
    tasks.sort(key=lambda q: -q[3])
    out["tasks"] = len(tasks)
    res, n = {}, 0
    t0 = time.time()
    for r in pool.imap_unordered(frame_task, tasks, chunksize=1):
        res[r["key"]] = r
        n += 1
        if n % 500 == 1:
            print(f"task {n}/{len(tasks)} at {round(time.time() - t0)} s", flush=True)
    out["compute seconds"] = round(time.time() - t0, 1)
    out["failed tasks"] = [[list(k), r["failed"]] for k, r in res.items() if "failed" in r]
    # ---- C3
    worst, ncmp = 0.0, 0
    for k, ln, x, y, _e in psample:
        a, b = res.get(k), res.get((k[0], k[1], 60))
        if a is None or b is None or "failed" in a or "failed" in b:
            continue
        for key in a["six"]:
            for j in range(2):
                if a["six10"][key][j] > -12 and math.isfinite(a["six"][key][j]):
                    worst = max(worst, abs(a["six"][key][j] - b["six"][key][j]))
                    ncmp += 1
    out["C3"] = {"draws": len(psample), "features compared": ncmp, "max |difference|": worst,
                 "holds": bool(ncmp > 0 and worst <= 1e-6)}
    # ---- C1e (a read-out here)
    above = []
    for li in range(len(lines266)):
        for xi in range(2):
            r = res.get(("C1e", li, xi))
            if r is None or "failed" in r:
                above.append([li, xi, "failed"])
                continue
            m = max(v for vv in r["six10"].values() for v in vv)
            if m > -12:
                above.append([li, xi, m])
    out["C1e (read-out)"] = {"points": 2 * len(lines266), "points with a ratio above 1e-12": len(above),
                             "first such": above[:20], "holds": not above}
    # ---- C1c and C1d, in the main process
    out["C1c"] = c1c()
    out["C1d"] = c1d(lines266)
    out["C2"] = c2()
    recs = {arm: [None] * NDRAW for arm in ("A0", "A1")}
    for arm in ("A0", "A1"):
        for d in draws[arm]:
            r = res.get((arm, d["i"], 0))
            if r is not None and "failed" not in r:
                recs[arm][d["i"]] = r
    out["census"] = {arm: {"draws": NDRAW, "capped (Im tau > 60)": sum(1 for d in draws[arm] if d["tau"][1] > CAP),
                           "computed": sum(1 for r in recs[arm] if r is not None),
                           "share Im tau > 3": float(np.mean([d["tau"][1] > 3 for d in draws[arm]])),
                           "share outside [1, 4]": float(np.mean([not (1 <= d["tau"][1] <= 4)
                                                                   for d in draws[arm]])),
                           "line orders": {str(o): sum(1 for d in draws[arm] if d["order"] == o)
                                           for o in range(1, 13)}} for arm in ("A0", "A1")}
    analysis(out, draws, cfg, recs)
    out["per draw"] = {arm: [dict(d, **({"frame": {k: recs[arm][d["i"]][k] for k in ("six", "ckm", "digits")}}
                                        if recs[arm][d["i"]] is not None else {})) for d in draws[arm]]
                       for arm in ("A0", "A1")}
    out["configurations"] = cfg


# ============================================================================================ the controls
def c1c():
    p = 60
    out, worst, wrong_min = [], 0.0, math.inf
    with mp.workdps(p):
        t = mp.mpc("0.31", "1.47")
        L0 = mp.mpf("2.3")
        for line in LINES_FOR_C1C:
            base = frame_at(line, float(mp.re(t)), float(mp.im(t)), p, Ls={h: L0 for h in HORO})
            for name, g in (("R", (1, 1, 0, 1)), ("TS", (1, -1, 1, 0))):
                a, b, c, d = g
                t2 = (a * t + b) / (c * t + d)
                L2 = L0 + mp.log(abs(c * t + d))
                good = frame_at(transport(line, g), float(mp.re(t2)), float(mp.im(t2)), p, Ls={h: L2 for h in HORO})
                ga, gb = line
                wrong_line = ((ga * a + gb * c) % 1, (ga * b + gb * d) % 1)
                wrong = frame_at(wrong_line, float(mp.re(t2)), float(mp.im(t2)), p, Ls={h: L2 for h in HORO})
                dev = max(abs(x - y) for k in base["six"] for x, y in zip(base["six"][k], good["six"][k]))
                dev = max(dev, max(abs(x - y) for k in base["ckm"] for x, y in zip(base["ckm"][k], good["ckm"][k])))
                wd = max(abs(x - y) for k in base["six"] for x, y in zip(base["six"][k], wrong["six"][k]))
                worst, wrong_min = max(worst, dev), min(wrong_min, wd)
                out.append([[str(line[0]), str(line[1])], name, dev, wd])
    return {"cases": out, "max |log| deviation": worst, "least wrong-transport deviation": wrong_min,
            "holds": bool(worst < 1e-9 and wrong_min > 0.1)}


def c1d(lines266):
    files = {p: T8.git_bytes(ROOT, T42.REV, p) for p in T42.FILES}
    rows = T8.census_rows(files[T42.V26 + "/census.jsonl"])
    row = [r for r in rows if r["line"] == 149 and abs(r["Re_tau"] - 0.35) < 1e-12 and abs(r["Im_tau"] - 3.05) < 1e-12]
    if not row:
        return {"holds": False, "note": "no stored row at (0.35 + 3.05i, line 149)"}
    row = row[0]
    line = lines266[149]
    mine = frame_at(line, 0.35, 3.05, precision(3.05))
    worst = 0.0
    for sec in SECS:
        for h in HORO:
            for rd in RD:
                st = np.log(np.maximum(np.array(row[f"{sec}|{h}|{rd}"][:2], dtype=float), 1e-300))
                worst = max(worst, float(np.max(np.abs(st - np.array(mine["six"][f"{sec}|{h}|{rd}"])))))
    for h in HORO:
        for ru in RD:
            for rdn in RD:
                st = np.log(np.array(row[f"ckm|{h}|{ru}|{rdn}"][:3], dtype=float))
                worst = max(worst, float(np.max(np.abs(st - np.array(mine["ckm"][f"{h}|{ru}|{rdn}"])))))
    return {"line": [str(line[0]), str(line[1])], "max |log| deviation": worst, "holds": bool(worst < 1e-9)}


def c2():
    files = {p: T8.git_bytes(ROOT, T42.REV, p) for p in T42.FILES}
    t6, _t9 = T8.targets(files)
    _rows, arr, _lab = T42.load_census("B1726", files)
    sg = T42.sigma(files)
    val = float(T42.direct_min(T42.configs(arr, "seat", sg), t6, sg)[0][0])
    return {"value": val, "B1735": 3.0945633, "holds": bool(abs(val - 3.0945633) < 1e-6)}


# ============================================================================================ the analysis
def analysis(out, draws, cfg, recs):
    files = {p: T8.git_bytes(ROOT, W58.REV, p) for p in W58.FILES}
    t6, t9 = T8.targets(files)
    s6 = T42.sigma(files)
    s9 = np.concatenate([s6, T42.sigma_ckm(files)])
    out["the data (read once)"] = {"six": t6.tolist(), "s6": s6.tolist(), "nine": t9.tolist(), "s9": s9.tolist()}
    W = {}
    for arm in ("A0", "A1"):
        for mode in ("unforced", "byhand"):
            W[(arm, mode)] = arm_worlds(recs[arm], cfg, mode)
    for (arm, mode), (X, _i) in W.items():
        out.setdefault("resolved", {})[f"{arm} {mode}"] = len(X)
    NNm = {k: NN(X, s6) for k, (X, _i) in W.items()}
    Fm = {k: Fisher(X) for k, (X, _i) in W.items()}
    res = {}
    for k in W:
        pn, dt = NNm[k].p(t6)
        res[k] = {"p_nn": float(pn[0]), "nearest distance (s6 units)": float(dt[0]), "p_F": float(Fm[k].p(t6)[0]),
                  "q95 of own nearest distances": NNm[k].q95(), "marginal p": Fm[k].marginal_p(t6)}
        Z = NNm[k].Z
        j = int(np.argmax(-np.max(np.abs(Z - t6 / s6), axis=1)))
        di = W[k][1][j]
        d = draws[k[0]][di]
        res[k]["nearest draw"] = {"draw": di, "tau": d["tau"], "word": d["word"][:60], "trace": d["trace"],
                                  "line": d["line"], "order": d["order"], "configuration": cfg[di],
                                  "|x - t|/sigma": (np.abs(W[k][0][j] - t6) / s6).tolist()}
    out["statistics"] = {f"{a} {m}": v for (a, m), v in res.items()}
    D1 = res[("A1", "unforced")]["p_nn"] > ALPHA
    D1h = res[("A1", "byhand")]["p_nn"] > ALPHA
    D2 = res[("A1", "unforced")]["p_F"] > ALPHA and res[("A0", "unforced")]["p_F"] <= ALPHA
    # ---- the random hierarchies
    rh = {"D1": [], "D2": [], "D1h fixed": [], "D1h free": []}
    W16 = {}
    for tri in TRIPLES:
        for c in (1, 3):
            W16[(tri, c)] = NN(arm_worlds(recs["A1"], cfg, (tri, c))[0], s6)
    for seed in RH_SEEDS:
        six, _nine = T8.own_draws(seed, RH_N)
        T = np.array(six)
        p1 = NNm[("A1", "unforced")].p(T)[0]
        rh["D1"].append(float(np.mean(p1 > ALPHA)))
        f1, f0 = Fm[("A1", "unforced")].p(T), Fm[("A0", "unforced")].p(T)
        rh["D2"].append(float(np.mean((f1 > ALPHA) & (f0 <= ALPHA))))
        rh["D1h fixed"].append(float(np.mean(NNm[("A1", "byhand")].p(T)[0] > ALPHA)))
        best = np.zeros(RH_FREE)
        for k16, nn in W16.items():
            best = np.maximum(best, nn.p(T[:RH_FREE])[0])
        rh["D1h free"].append(float(np.mean(best > ALPHA)))
    r = {k: float(np.mean(v)) for k, v in rh.items()}
    out["random hierarchies (mean over seeds 1741-1760)"] = {"r": r, "per seed": rh}
    # ---- the power
    anar = anarchy_six(NANARCHY, SEEDS["anarchy"])
    hr = random.Random(SEEDS["holdout"])
    power = {}

    def pick(X, n):
        idx = list(range(len(X)))
        hr.shuffle(idx)
        return X[idx[:n]]
    A0u, A1u, A0h, A1h = (W[k][0] for k in (("A0", "unforced"), ("A1", "unforced"), ("A0", "byhand"),
                                              ("A1", "byhand")))
    power["D1 (p_nn, A1 unforced)"] = {"A0 worlds": share_le(NNm[("A1", "unforced")].p(pick(A0u, NPOWER))[0]),
                                       "anarchy": share_le(NNm[("A1", "unforced")].p(anar)[0]),
                                       "random hierarchies": 1 - r["D1"]}
    power["D1h (p_nn, A1 by hand)"] = {"A0 worlds": share_le(NNm[("A1", "byhand")].p(pick(A0h, NPOWER))[0]),
                                       "anarchy": share_le(NNm[("A1", "byhand")].p(anar)[0]),
                                       "random hierarchies (fixed)": 1 - r["D1h fixed"],
                                       "random hierarchies (free)": 1 - r["D1h free"]}
    power["D2 (p_F)"] = {"A0 worlds under A1": share_le(Fm[("A1", "unforced")].p(pick(A0u, NPOWER))),
                         "A1 worlds under A0": share_le(Fm[("A0", "unforced")].p(pick(A1u, NPOWER))),
                         "anarchy under A1": share_le(Fm[("A1", "unforced")].p(anar)),
                         "anarchy under A0": share_le(Fm[("A0", "unforced")].p(anar)),
                         "random hierarchies with the D2 pattern": r["D2"]}
    cal = {}
    for arm in ("A0", "A1"):
        X = W[(arm, "unforced")][0]
        idx = list(range(len(X)))
        hr.shuffle(idx)
        half = len(idx) // 2
        model, tg = X[idx[:half]], X[idx[half:half + NHOLD]]
        cal[arm] = {"p_nn <= 0.05": share_le(NN(model, s6).p(tg)[0]), "p_F <= 0.05": share_le(Fisher(model).p(tg))}
    power["held-out calibration (unforced)"] = cal
    out["power"] = power
    # ---- read-outs
    ro = {}
    for arm in ("A0", "A1"):
        for mode in ("unforced", "byhand"):
            U = unconditioned(recs[arm], cfg, mode)
            ro[f"unconditioned {arm} {mode}"] = {"p_nn": float(NN(U, s6).p(t6)[0][0]), "p_F": float(Fisher(U).p(t6)[0])}
    ro["anarchy as the model"] = {"p_nn": float(NN(anar, s6).p(t6)[0][0]), "p_F": float(Fisher(anar).p(t6)[0])}
    floors = {}
    for fl in FLOORS_RO:
        f = {}
        for arm in ("A0", "A1"):
            for mode in ("unforced", "byhand"):
                X, _i = arm_worlds(recs[arm], cfg, mode, floor=fl)
                nn = NN(X, s6)
                pn, dt = nn.p(t6)
                f[f"{arm} {mode}"] = {"resolved": len(X), "p_nn": float(pn[0]), "nearest distance": float(dt[0]),
                                      "p_F": float(Fisher(X).p(t6)[0])}
        floors[f"{fl:g}"] = f
    ro["floors"] = floors
    nines = {}
    for arm in ("A0", "A1"):
        for mode in ("unforced", "byhand"):
            X, _i = arm_worlds(recs[arm], cfg, mode, use_nine=True)
            nn = NN(X, s9)
            pn, dt = nn.p(t9)
            nines[f"{arm} {mode}"] = {"resolved": len(X), "p_nn": float(pn[0]), "nearest distance": float(dt[0]),
                                      "p_F": float(Fisher(X).p(t9)[0]), "marginal p": Fisher(X).marginal_p(t9)}
    ro["the nine"] = nines
    ro["q95 per configuration (A1, s6 units)"] = {f"{tri}|c={c}": nn.q95() for (tri, c), nn in W16.items()}
    ro["the lepton shift log 3 / s6 (mu/tau, e/tau)"] = [LN3 / s6[4], LN3 / s6[5]]
    ro["D1h resolution condition (q95 A1 by hand finer than log 3/s6)"] = bool(
        res[("A1", "byhand")]["q95 of own nearest distances"] < min(LN3 / s6[4], LN3 / s6[5]))
    out["read-outs"] = ro
    out["D1"] = {"p_nn": res[("A1", "unforced")]["p_nn"], "holds": bool(D1), "r": r["D1"], "grade": grade(D1, r["D1"])}
    out["D1h"] = {"p_nn": res[("A1", "byhand")]["p_nn"], "holds": bool(D1h), "r (free null)": r["D1h free"],
                  "grade": grade(D1h, r["D1h free"])}
    out["D2"] = {"p_F A1": res[("A1", "unforced")]["p_F"], "p_F A0": res[("A0", "unforced")]["p_F"],
                 "holds": bool(D2), "r": r["D2"], "grade": grade(D2, r["D2"])}
    out["C"] = {"holds": bool(all(out[k]["holds"] for k in ("C1a", "C1b", "C1c", "C1d", "C2", "C3")))}
    out["cells"] = {k: out[k]["holds"] for k in ("D1", "D1h", "D2", "C")}


def clean(o):
    """non-finite floats (a zero ratio's log) are written as null"""
    if isinstance(o, float):
        return o if math.isfinite(o) else None
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating,)):
        return clean(float(o))
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def main():
    t0 = time.time()
    out = {"arc": "W184", "rule": "W184_RULE.md", "card": "B1814's PREREGISTRATION.md at 86cb26b30",
           "python": platform.python_version(), "workers": WORKERS, "seeds": SEEDS}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=_init, initargs=(str(ROOT),)) as pool:
                _init(str(ROOT))
                run(out, pool)
        except Exception:  # noqa: BLE001
            out["run_failed"] = sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(clean(out), indent=1, ensure_ascii=False, default=str, allow_nan=False) + "\n",
                   encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
