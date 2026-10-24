#!/usr/bin/env python3
"""W156 — the third opinion on main's B1749, the six at fresh apexes (the rule: W156_RULE.md, committed and pushed
before this script).  It runs once, from the repository root.

W145's script (the_third_opinion_b1741.py) is loaded unchanged and re-pointed to B1749's arc, its fresh seeds and its
census, as B1749's compare.py does with B1741's: its A0, A1, A2 and A4 parts, its own instrument through b_job, and
its sensitivity job.  New here, on own code: the apex points and their freshness (A3, A3f), the best rows with
B1724's T-law and the mirror (B), the strip in the census (C1) and its width on own instrument (C2), and the
sensitivity with c = 1 alone added (D1).  Main's code is run only in A1, in a temporary tree.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1749.py [--workers 4]
"""
import argparse
import contextlib
import io
import itertools
import json
import math
import multiprocessing as mpr
import platform
import sys
import tempfile
import time
import traceback
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_third_opinion_b1741 as W45    # noqa: E402  (W145, re-pointed below)
T8, T41, T42, W140 = W45.T8, W45.T41, W45.T42, W45.W140

REV = "f3038f81b53e69b11d4c1f429d53b657ae837f65"      # origin/main as read for the rule
ARC = "frontier/B1749_the_six_at_fresh_apexes"
V49 = ARC + "/verification"
V41 = "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification"
V26 = W45.V26
B1720T = W45.B1720T
B1720G = "frontier/B1720_the_thread_fixes_the_point/verification/thread_geometry.py"
FILES = (V49 + "/compare.py", V49 + "/census.py", V49 + "/census.jsonl", V49 + "/control.json",
         V49 + "/comparison.json", ARC + "/ARTIFACT_HASHES.txt", V41 + "/compare.py", V41 + "/census.jsonl",
         V26 + "/census.py", V26 + "/census.jsonl", B1720T, B1720G, W45.HZ, W45.CKM, W45.COLUMN) + W45.DEPS
PIN = {V49 + "/census.jsonl": "667684c992433a0705feda7b0452d9b322a85a71c91952c3bf1275ece50281d4",
       V49 + "/comparison.json": "6d91c69dfecc90c17ee2392a62af4efa896ca52e697c24aa464343537dba005c",
       V49 + "/control.json": "bf2740c5701a8b688c992dc3892ca59cc849dd61d5de83cbbfc40b26ab5099cc"}
OUT = HERE / "third_opinion_b1749.json"
SEEDS = tuple(range(1769, 1789))
NPTS = 33250
NAPEX = 125
LN3 = math.log(3)
BAR6 = 16.75
WINDOW = (2.0, 3.6)
NINE = {"seat": 191.84, "sm": 1278.85}
MAIN_REFEREE = {"allowance 0.05": 5.09, "uniform sigma 0.10": 7.72, "c = 1 alone": 125.8}
LINE0 = (Fr(2, 5), Fr(1, 10))
TOL = W45.TOL

# re-point W145's module to this arc (its functions read these globals)
W45.V41, W45.ARC, W45.PIN, W45.SEEDS = V49, ARC, PIN, SEEDS
_ROOT = W45._ROOT


def sanitize(text):
    return W45.sanitize(text)


# ============================================================================================ A3, A3f: own apexes
def necklaces(n):
    out = set()
    for t in itertools.product("LR", repeat=n):
        w = "".join(t)
        if "L" not in w or "R" not in w:
            continue
        if any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0):
            continue
        out.add(min(w[i:] + w[:i] for i in range(n)))
    return sorted(out)


def run_lengths(w):
    n = len(w)
    i = next(j for j in range(n) if w[j] == "L" and w[j - 1] == "R")
    s = w[i:] + w[:i]
    return [len(list(g)) for _, g in itertools.groupby(s)]


def cf_periodic(seq, reps=60):
    v = float(seq[-1])
    for _ in range(reps):
        for a in reversed(seq):
            v = a + 1.0 / v
    return v


def lagrange(w):
    a = run_lengths(w)
    best = 0.0
    for k in range(len(a)):
        fwd = a[k:] + a[:k]
        bwd = list(reversed(a[:k])) + list(reversed(a[k:]))
        best = max(best, cf_periodic(fwd) + 1.0 / cf_periodic(bwd))
    return best


def tops(w):
    """the height (largest axis radius over the rotations and their S-conjugates) and the top points' Re tau mod 1"""
    cands = []
    for i in range(len(w)):
        (a, b), (c, d) = W45.word_matrix(w[i:] + w[:i])
        t = a + d
        for cc, num in ((c, a - d), (b, a - d)):          # A, and S A S^-1 = ((d, -c), (-b, a))
            if cc != 0:
                cands.append((math.sqrt(t * t - 4) / (2 * abs(cc)), (num / (2 * cc)) % 1.0))
    h = max(r for r, _ in cands)
    pts = sorted({round(x % 1.0, 10) % 1.0 for r, x in cands if r > h - 1e-9})
    return h, pts


def circ(a, b):
    d = abs(a - b) % 1.0
    return min(d, 1.0 - d)


def part_A3(files):
    out = {}
    d = json.loads(files[B1720T].decode("utf-8"))
    bad, worst_h = [], 0.0
    for c in d["classes"]:
        w = W45.expand(c["word"])
        h, pts = tops(w)
        worst_h = max(worst_h, abs(h - c["tau"][1]))
        if abs(h - c["tau"][1]) > 1e-9 or min(circ(c["tau"][0], x) for x in pts) > 1e-9:
            bad.append(c["word"])
    out["(i) B1720 classes"] = {"classes": len(d["classes"]), "failing": bad, "worst |height - stored|": worst_h}
    words12 = necklaces(12)
    lag, inwin = 0.0, {}
    for w in words12:
        h, pts = tops(w)
        lag = max(lag, abs(h - lagrange(w) / 2))
        if WINDOW[0] <= h <= WINDOW[1]:
            inwin[w] = (h, pts)
    out["(ii)"] = {"necklaces of length 12": len(words12), "in the window": len(inwin),
                   "worst |height - Lagrange/2|": lag}
    rows = T8.census_rows(files[V49 + "/census.jsonl"])
    points = {}
    for r in rows:
        points.setdefault((r["Re_tau"], r["Im_tau"]), set()).update(r["words"])
    fails, listed = [], set()
    for (re_, im_), ws in points.items():
        for w in ws:
            listed.add(w)
            h, pts = tops(w)
            if abs(h - im_) > 1e-9 or min(circ(re_, x) for x in pts) > 1e-9:
                fails.append([w, re_, im_])
    out["(iii)"] = {"distinct census points": len(points), "word-point failures": fails[:20],
                    "listed words": len(listed), "listed words equal the own window words": listed == set(inwin)}
    _A3["points"] = sorted(points)
    return out


_A3 = {}


def part_A3f(files):
    pts = _A3.get("points")
    if pts is None:
        rows = T8.census_rows(files[V49 + "/census.jsonl"])
        pts = sorted({(r["Re_tau"], r["Im_tau"]) for r in rows})
    older, n_words = [], 0
    for n in range(2, 12):
        for w in necklaces(n):
            n_words += 1
            h, tp = tops(w)
            if WINDOW[0] - 1e-6 <= h <= WINDOW[1] + 1e-6:
                older += [(x, h, w) for x in tp]
    hits = []
    for (re_, im_) in pts:
        for (x, h, w) in older:
            if abs(h - im_) < 1e-6 and (circ(re_, x) < 1e-6 or circ(-re_, x) < 1e-6):
                hits.append([re_, im_, w])
    mirror = sum(1 for (re_, im_) in pts
                 if any(abs(i2 - im_) < 1e-9 and circ(-re_, r2) < 1e-9 and circ(re_, r2) > 1e-9 for r2, i2 in pts))
    return {"older primitive words (lengths 2-11)": n_words, "older top points in the window": len(older),
            "overlaps": hits, "points whose mirror is another point": mirror,
            "mirror pairs": mirror // 2, "independent (pairs + singles)": len(pts) - mirror // 2}


# ======================================================================================== C1: the strip in the census
def seat_best_per_row(arr, t6, sg):
    best = np.full(arr["up"].shape[0], np.inf)
    arg = [None] * arr["up"].shape[0]
    for key, X, kind in T42.configs(arr, "seat", sg):
        t = T42.tmap(t6, kind, sg)[0]
        c = ((X - t[None, :]) ** 2).sum(1)
        better = c < best
        for i in np.nonzero(better)[0]:
            arg[i] = key
        best = np.minimum(best, c)
    return best, arg


def part_C1(files):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    rows = T8.census_rows(files[V49 + "/census.jsonl"])
    arr, lab = T8.census_arrays(rows)
    best, arg = seat_best_per_row(arr, t6, sg)
    L = T8.own_lines()
    below = [i for i in range(len(best)) if best[i] < BAR6]
    out = {"rows below 16.75": len(below), "rows": []}
    for i in sorted(below, key=lambda j: best[j]):
        a, b, l, k = arg[i]
        out["rows"].append({"chi2_six": float(best[i]), "line": [str(x) for x in L[lab[i][0]]],
                            "Re_tau": lab[i][1], "Im_tau": lab[i][2], "horocycle": lab[i][3],
                            "readings": [T8.RD[a], T8.RD[b], T8.RD[l]], "c": round(math.exp(k))})
    rr = out["rows"]
    out["lines"] = sorted({tuple(r["line"]) for r in rr})
    out["horocycles"] = sorted({r["horocycle"] for r in rr})
    out["configurations"] = sorted({(tuple(r["readings"]), r["c"]) for r in rr})
    out["heights"] = [min(r["Im_tau"] for r in rr), max(r["Im_tau"] for r in rr)] if rr else None
    _C["best_rows"] = rr
    return out


_C = {}


# ============================================================================================ B: own instrument
def part_B(root, files, a2):
    W93, W89 = T8.own_modules(root)
    W45._B.update(W93=W93, W89=W89, col=T8.L_column(files))
    rows = T8.census_rows(files[V49 + "/census.jsonl"])
    L = T8.own_lines()
    stored = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}

    def key_near(k, re_t, im_t):
        for (kk, x, y) in stored:
            if kk == k and abs(x - re_t) < 1e-6 and abs(y - im_t) < 1e-6:
                return (kk, x, y)
        return None
    pts = [(p["line"], p["Re_tau"], p["Im_tau"]) for p in a2["top five points (seat)"]]
    k_half = L.index((Fr(2, 5), Fr(1, 2)))
    named = {"best six-row": (L.index(LINE0), 1 / 3, 3.0551), "its mirror": (k_half, 2 / 3, 3.0551),
             "best by the largest factor": (k_half, 0.6053, 3.0259)}
    named_keys = {}
    for name, (k, x, y) in named.items():
        kk = None
        for (k2, x2, y2) in stored:
            if k2 == k and abs(x2 - x) < 5e-4 and abs(y2 - y) < 5e-4:
                kk = (k2, x2, y2)
        named_keys[name] = kk
    keys = [k for k in named_keys.values() if k is not None]
    for p in pts:
        kk = key_near(*p)
        if kk is not None and kk not in keys:
            keys.append(kk)
    best = named_keys["best six-row"]
    tasks = [(L[k], x, y) for (k, x, y) in keys]
    xb, yb = best[1], best[2]
    tl = ((Fr(2, 5), (Fr(1, 10) - Fr(2, 5)) % 1), xb + 1, yb)          # B1724's T-law image of the best row
    mi = ((Fr(2, 5), (-Fr(1, 10)) % 1), -xb, yb)                       # the mirror image
    tasks += [tl, mi]
    with mpr.Pool(4) as P:
        res = P.map(W45.b_job, tasks)
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    jl, per, own = 0.0, [], {}
    for (line, x, y), o, diag in res[:-2]:
        k = L.index(line)
        dev = T8.compare_point(o, stored[(k, x, y)])
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        jl = max(jl, diag["joint_law_max"])
        per.append({"line": k, "tau": [x, y], "deviation": dev})
        own[(k, x, y)] = o
    o_best = own[best]
    t_law = T8.compare_point(res[-2][1], o_best)
    mirror = T8.compare_point(res[-1][1], o_best)
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)

    def six_of(r):
        s = np.log(np.array(r["up|L_max|St"] + r["down|L_max|S"] + r["lep|L_max|S"]))
        return s + np.array([0, 0, 0, 0, LN3, -LN3])
    six, six_main = six_of(o_best), six_of(stored[best])
    pulls, pulls_main = (six - t6) / sg, (six_main - t6) / sg
    chi_main = float((pulls_main ** 2).sum())
    row = {"chi2": float((pulls ** 2).sum()), "chi2 from the stored row": chi_main, "pulls": pulls.tolist(),
           "D": math.exp(six[4] + six[3] - six[2] - six[5]), "D stored": math.exp(six_main[4] + six_main[3]
                                                                                 - six_main[2] - six_main[5])}
    row["checks"] = {"chi2_rel": abs(row["chi2"] - chi_main) / chi_main,
                     "pulls_abs": float(np.max(np.abs(pulls - pulls_main))),
                     "D_rel": abs(row["D"] - row["D stored"]) / row["D stored"]}
    a, b = L[best[0]]
    tau = complex(best[1], best[2])
    rc = 0.0
    for sec in T8.SECTS:
        mine = T8.own_residues(W93, sec, a, b, tau)
        ref = T8.circle_residues(W93, sec, a, b, tau)
        rc = max(rc, max(abs(mine[s] - ref[s]) for s in T8.UNITS) / max(abs(v) for v in ref.values()))
    return {"named rows": {k: (list(v) if v else None) for k, v in named_keys.items()}, "points": per,
            "worst": worst, "joint_law_max": jl, "residue_control_rel": rc,
            "T-law image against the best row": t_law, "mirror image against the best row": mirror, "row": row}


# ============================================================================================ C2: the strip's width
def part_C2(root, files, workers):
    if not W45._B:
        W93, W89 = T8.own_modules(root)
        W45._B.update(W93=W93, W89=W89, col=T8.L_column(files))
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    res_ = np.round(np.arange(0.1, 4.95, 0.2), 4)
    ims = np.round(np.arange(2.0, 3.60001, 0.02), 4)
    tasks = [(LINE0, float(x), float(y)) for x in res_ for y in ims]
    with mpr.Pool(workers) as P:
        res = P.map(W45.b_job, tasks)
    rows = []
    for (line, x, y), o, _d in res:
        r = dict(o)
        r.update(line=0, Re_tau=x, Im_tau=y)
        rows.append(r)
    arr, lab = T8.census_arrays(rows)
    best, _arg = seat_best_per_row(arr, t6, sg)
    below = {}
    for i, (_l, x, y, h) in enumerate(lab):
        if h == "L_max":
            below.setdefault(x, {})[y] = bool(best[i] < BAR6)
    per_re, single, inside, in02 = {}, True, True, True
    for x in res_:
        ys = [y for y in ims if below[float(x)][float(y)]]
        per_re[str(float(x))] = ys
        if ys:
            idx = [int(round((y - 2.0) / 0.02)) for y in ys]
            single &= idx == list(range(idx[0], idx[-1] + 1))
            inside &= 2.80 - 1e-9 <= min(ys) and max(ys) <= 3.30 + 1e-9
            in02 &= float(x) <= 2.0
    resid = {}
    for x in res_:
        rkey = round(float(x) % 1.0, 4)
        for y in ims:
            if below[float(x)][float(y)]:
                resid.setdefault(rkey, set()).add(float(y))
    covered = len(resid)
    p = float(np.mean([len(resid.get(round(r, 4), ())) / len(ims) for r in (0.1, 0.3, 0.5, 0.7, 0.9)]))
    l2 = sum(1 for i, (_l, x, y, h) in enumerate(lab) if h == "L_2" and best[i] < BAR6)
    return {"Im tau below the bar per Re tau (L_max)": per_re, "one interval at each Re tau": single,
            "inside [2.80, 3.30]": inside, "every such Re tau in [0, 2]": in02, "residues covered (of 5)": covered,
            "p": p, "1 - (1 - p)^125": 1 - (1 - p) ** 125, "read-out: L_2 points below the bar": l2,
            "points": len(tasks)}


# ============================================================================================ D1
def part_D1(files, workers, tmp):
    t6, _t9 = T8.targets(files)
    _rows, arr, _lab = W45.arrays(files)
    npz = str(Path(tmp) / "B1749_sens.npz")
    np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=T42.sigma(files))
    variants = {"allowance 0.05": (T42.sigma(files, 0.05), (0.0, LN3)),
                "lepton factor over {1, ..., 5}": (T42.sigma(files, 0.10), tuple(math.log(c) for c in range(1, 6))),
                "uniform sigma 0.10": (np.full(6, 0.10), (0.0, LN3)),
                "c = 1 alone": (T42.sigma(files, 0.10), (0.0,))}

    def init():
        T42._init("B1749", npz, 0.10)
        T42._W["variants"] = variants
    init()
    tasks = [(s, v) for s in SEEDS for v in variants]
    with mpr.Pool(workers, initializer=init) as P:
        res = P.map(W45.sens_job, tasks)
    out = {}
    for name in variants:
        rr = [x for x in res if x[1] == name]
        out[name] = {"chi2_six_min": rr[0][2], "fraction_mean": float(np.mean([x[3] for x in rr])),
                     "fraction_max": float(np.max([x[3] for x in rr])), "per_seed": [x[3] for x in rr]}
    return out


# ============================================================================================ cells and main
def guarded(out, name, fn, *args):
    t0 = time.time()
    try:
        out[name] = fn(*args)
    except Exception:  # noqa: BLE001  (a failed part is a failed launch of that part, disclosed as such)
        out[name + "_failed"] = sanitize(traceback.format_exc()[-4000:])
    out.setdefault("part_seconds", {})[name] = round(time.time() - t0, 1)


def cells(out):
    c = {}
    try:
        return _cells(out, c)
    except Exception:  # noqa: BLE001
        out["cells_failed"] = sanitize(traceback.format_exc()[-2000:])
        return {key: bool(val) for key, val in c.items()}


def _cells(out, c):
    if "A0" in out:
        a = out["A0"]
        c["A0"] = (all(a[p] for p in PIN) and a["census rows"] == NPTS and a["census distinct (line, Re, Im)"] == NPTS
                   and all(v is True for v in a["ARTIFACT_HASHES"].values()))
    if "A1" in out:
        a = out["A1"]
        c["A1"] = (a["compare"]["returncode"] == 0 and a.get("cells identical") and a.get("per-seed fractions exact")
                   and not a.get("diff", {"mismatches": [1]})["mismatches"]
                   and a.get("diff", {"max_rel": 1})["max_rel"] < 1e-12)
    if "A2" in out:
        a = out["A2"]
        c["A2"] = (a["per_seed_equal_main"] and max(a["min_rel_vs_main"].values()) < 1e-10
                   and all(a["chi2_nine"][m]["rel_vs_main"] < 1e-6 for m in ("seat", "sm"))
                   and all(abs(a["chi2_nine"][m]["chi2_nine_min"] - NINE[m]) < 0.01 for m in ("seat", "sm")))
    if "A3" in out:
        a = out["A3"]
        c["A3"] = (a["(i) B1720 classes"]["classes"] == 121 and not a["(i) B1720 classes"]["failing"]
                   and a["(ii)"]["necklaces of length 12"] == 335 and a["(ii)"]["in the window"] == 238
                   and a["(iii)"]["distinct census points"] == NAPEX and not a["(iii)"]["word-point failures"]
                   and a["(iii)"]["listed words equal the own window words"])
    if "A3f" in out:
        c["A3f"] = not out["A3f"]["overlaps"]
    if "A4" in out:
        a = out["A4"]
        c["A4"] = (a["W140 lines"] == 266 and a["equal as sets"] and a["every apex has lines 0-265"]
                   and a["apexes"] == NAPEX)
    if "B" in out:
        b = out["B"]
        w, tl, mi, v = b["worst"], b["T-law image against the best row"], b["mirror image against the best row"], \
            b["row"]["checks"]
        c["B0"] = (b["residue_control_rel"] < TOL["residue_rel"] and b["joint_law_max"] < TOL["joint_law"]
                   and max(tl["up"], tl["down"], tl["lep"], tl["ckm"]) < 1e-8 and tl["J_rel"] < 1e-8
                   and max(mi["up"], mi["down"], mi["lep"], mi["ckm"]) < 1e-8 and abs(mi["J_rel"] - 2) < 1e-8)
        c["B1"] = (all(v2 is not None for v2 in b["named rows"].values())
                   and max(w["up"], w["down"], w["lep"], w["ckm"]) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                   and w["zero_pattern_mismatches"] == 0)
        c["B2"] = (v["chi2_rel"] < 1e-3 and v["pulls_abs"] < 1e-3 and v["D_rel"] < 1e-3
                   and abs(b["row"]["chi2"] - 3.57) < 0.01 and abs(b["row"]["D"] - 10.94) < 0.01)
    if "C1" in out:
        k = out["C1"]
        c["C1"] = (k["rows below 16.75"] == 12 and k["lines"] == [("2/5", "1/10"), ("2/5", "1/2")]
                   and k["horocycles"] == ["L_max"] and k["configurations"] == [(("St", "S", "S"), 3)]
                   and abs(k["heights"][0] - 2.961) < 5e-4 and abs(k["heights"][1] - 3.119) < 5e-4)
    if "C2" in out:
        k = out["C2"]
        c["C2"] = (k["one interval at each Re tau"] and k["inside [2.80, 3.30]"] and k["every such Re tau in [0, 2]"]
                   and k["residues covered (of 5)"] >= 4 and k["1 - (1 - p)^125"] >= 0.99)
    if "D1" in out:
        s = out["D1"]
        c["D1"] = (abs(s["allowance 0.05"]["chi2_six_min"] / MAIN_REFEREE["allowance 0.05"] - 1) < 0.01
                   and abs(s["uniform sigma 0.10"]["chi2_six_min"] / MAIN_REFEREE["uniform sigma 0.10"] - 1) < 0.01
                   and s["uniform sigma 0.10"]["fraction_mean"] <= 0.001
                   and s["lepton factor over {1, ..., 5}"]["fraction_mean"] <= 0.001
                   and abs(s["c = 1 alone"]["chi2_six_min"] / MAIN_REFEREE["c = 1 alone"] - 1) < 0.01)
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W156", "rule": "W156_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers}
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    guarded(out, "A0", W45.part_A0, files)
    guarded(out, "A1", W45.part_A1, files, args.workers)
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp2>"] = td
        guarded(out, "A2", W45.part_A2, files, args.workers, td)
        guarded(out, "D1", part_D1, files, args.workers, td)
    guarded(out, "A3", part_A3, files)
    guarded(out, "A3f", part_A3f, files)
    guarded(out, "A4", W45.part_A4, files, out.get("A1"))
    guarded(out, "C1", part_C1, files)
    if "A2" in out:
        guarded(out, "B", part_B, root, files, out["A2"])
    guarded(out, "C2", part_C2, root, files, args.workers)
    if "A1" in out:
        out["A1"].pop("main_lines", None)
    if "A2" in out:
        a2 = out["A2"]
        out["A2"]["seeds 1769 and 1788 (main's referee recomputed these)"] = {
            s: a2["per_seed"].get(str(s)) for s in (1769, 1788)}
        out["A2"].pop("seat minimum at FINDINGS' row", None)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    out["opinion"] = {"agrees with main's scope (a property of the frame's strip, not a selection of tau)":
                      bool(all(c.get(k) for k in ("A1", "A2", "B1", "C1", "C2")))}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
