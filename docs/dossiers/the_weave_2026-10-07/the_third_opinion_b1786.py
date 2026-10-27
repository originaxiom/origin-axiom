#!/usr/bin/env python3
"""W164 — the third opinion on main's B1786, the slope principle out of sample on the lines of order 25 and 30
(the rule: W164_RULE.md, committed and pushed before this script).  It runs once, from the repository root.

W163's script (the_third_opinion_b1755.py) is loaded unchanged, with W157's, W156's and W145's under it; their
helpers are reused (the census loader, the own instrument, the direct-sum chi-square, the own draws, the apex code,
the per-point minima).  New here:
  - one pass per seed gives, for each of the seed's 4 000 targets, the least chi2_six (the seat's menu, both
    horocycles) in each of the 26 slope classes at orders 25 and 30: W142's direct sums, with rows sorted by class
    and the minimum taken per class.  Main's four classes (slope 2/5, slope 1/10, the rest, all) and the class-choosing
    null are read from these minima;
  - each seed's minima are saved to a cache outside the repository as soon as the seed is done, so a restart resumes
    from the saved seeds (the minima are deterministic; the output names the seeds read from the cache);
  - the 588 lines of exact order 25 and 30 are enumerated again (A4); the offset pairs are read against the lower
    orders' censuses (C2).
Main's compare.py is not run.  Read with this script (code, not values): B1786's compare.py in full and its referee's
null.py, prep.py and analyse.py, for the class definitions and the class-choosing event (analyse.py's comment names its
validation counts on the sealed seeds, 8 and 67).

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1786.py --cache DIR [--workers 4]
"""
import argparse
import contextlib
import gc
import gzip
import io
import json
import math
import multiprocessing as mpr
import os
import platform
import sys
import time
import traceback
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_third_opinion_b1755 as W63    # noqa: E402  (W163, which loads W157's, W156's and W145's modules)
W57, W56 = W63.W57, W63.W56
W45, T8, T42 = W56.W45, W56.T8, W56.T42

REV = "8ca002cd13152f79f699799c6dac55d80d0cb74e"      # origin/main as read for the rule
ARC = "frontier/B1786_the_slope_principle_out_of_sample"
V86 = ARC + "/verification"
V55, V49 = W63.V55, W63.V49
GZ = V86 + "/census.jsonl.gz"
SHAF = V86 + "/census.jsonl.sha256"
PIN = {GZ: "5acb140b473d5f93c0442b3408d3f71c46b55ba742fe46f19b9362ccea7b3bf9",
       SHAF: "9ceece3a107685750942df846a1324a25cb4a66dd6c06c07b4e746773bbde974",
       V86 + "/comparison.json": "6da874995663337e9255eeaa3223b3b73428619cd5e6ad252da6e68a5c59a1cb",
       V86 + "/control.json": "4ad1c0a9f607e6386916840b5906c32fb90dfb5dbc97a6004f6e5a08bdddb7ac"}
PIN_LOW = {V49 + "/census.jsonl": W56.PIN[V49 + "/census.jsonl"], V55 + "/census.jsonl": W63.PIN[V55 + "/census.jsonl"]}
FILES = (GZ, SHAF, V86 + "/comparison.json", V86 + "/control.json", ARC + "/ARTIFACT_HASHES.txt",
         V49 + "/census.jsonl", V55 + "/census.jsonl", T8.HZ, T8.CKM, T8.COLUMN) + W45.DEPS
OUT = HERE / "third_opinion_b1786.json"
SEEDS = tuple(range(1829, 1869))                       # main's (B1786's compare.py)
FRESH = tuple(range(1869, 1929))                       # this seat's; 1869-1908 serve A2f
FRESH_A2F = FRESH[:40]
ORDERS = (25, 30)
COUNTS = {25: 300, 30: 288}
NROWS, NAPEX, NCLASS = 73500, 125, 26
BAR6 = 16.75
WINDOW = (2.0, 3.6)
SLOPE, TENTH = Fr(2, 5), Fr(1, 10)
OFFSETS = {25: {Fr(k, 25) for k in (3, 4, 11, 12, 17, 19, 21, 23)},
           30: {Fr(1, 6), Fr(13, 30), Fr(23, 30), Fr(5, 6)}}           # FINDINGS' twelve
BEST = ((SLOPE, Fr(23, 30)), 0.2692, 3.0375)                           # FINDINGS: the best row, L_max
FIND_MAIN = {"a2/5": (3.005, 8), "a1/10": 919.0, "rest": 103.0}
C3_BAND = (1.79e-4, 3.45e-4)                                           # 2.5 binomial sigma about the referee's 2.62e-4
TOL = T8.TOL

_ROOT = W45._ROOT


def sanitize(text):
    return W45.sanitize(text)


def own_lines86():
    """every flat line of exact order 25 or 30 up to sign, in B1726's enumeration (the key is the smaller of (a, b) and
    (-a, -b) mod 1; orders in increasing order), written again"""
    out, seen = [], set()
    for n in ORDERS:
        for j in range(n):
            for k in range(n):
                if math.gcd(math.gcd(j, k), n) != 1:
                    continue
                a, b = Fr(j, n), Fr(k, n)
                key = min((a, b), ((-a) % 1, (-b) % 1))
                if key not in seen:
                    seen.add(key)
                    out.append(key)
    return out


def mirror(line):
    """the record's mirror on a line: -b at -x, then one T-step back to 1 - x: (a, b) -> (a, -b - a)"""
    return W57.key_of(line[0], -line[1] - line[0])


# ============================================================================================ A0: the inputs
def part_A0(files, census, rows):
    out = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    out["decompressed census matches census.jsonl.sha256"] = (T8.sha256(census)
                                                              == files[SHAF].decode("utf-8").split()[0])
    out["census rows"] = len(rows)
    out["census distinct (line, Re, Im)"] = len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
    out["census distinct points"] = len({(r["Re_tau"], r["Im_tau"]) for r in rows})
    pinned = {}
    for ln in files[ARC + "/ARTIFACT_HASHES.txt"].decode("utf-8").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        h, p = ln.split()[0], ln.split()[1]
        if p == "census.jsonl":                         # the output pinned after the seal: the decompressed census
            pinned[p] = T8.sha256(census) == h
            continue
        path = p if p.startswith("frontier/") else ARC + "/" + p
        pinned[path] = (T8.sha256(files[path]) == h) if path in files else "not fetched"
    out["ARTIFACT_HASHES"] = pinned
    out["lower orders' census pins (for C2)"] = {p: T8.sha256(files[p]) == h for p, h in PIN_LOW.items()}
    return out


# ============================================================================================ A3: the points
def part_A3(files, rows):
    words12 = W56.necklaces(12)
    inwin = {}
    for w in words12:
        h, pts = W56.tops(w)
        if WINDOW[0] <= h <= WINDOW[1]:
            inwin[w] = (h, pts)
    points = {}
    for r in rows:
        points.setdefault((r["Re_tau"], r["Im_tau"]), set()).update(r["words"])
    fails, listed = [], set()
    for (re_, im_), ws in points.items():
        for w in ws:
            listed.add(w)
            h, pts = W56.tops(w)
            if abs(h - im_) > 1e-9 or min(W56.circ(re_, x) for x in pts) > 1e-9:
                fails.append([w, re_, im_])
    p49 = {(r["Re_tau"], r["Im_tau"]) for r in T8.census_rows(files[V49 + "/census.jsonl"])}
    return {"necklaces of length 12": len(words12), "in the window": len(inwin),
            "distinct census points": len(points), "word-point failures": fails[:20], "listed words": len(listed),
            "listed words equal the own window words": listed == set(inwin),
            "the points equal B1749's census points": set(points) == p49}


# ============================================================================================ A4: the lines
def part_A4(rows):
    L = own_lines86()
    by = {}
    for ln in L:
        by[T8.order(ln)] = by.get(T8.order(ln), 0) + 1
    stored_ok = all((Fr(r["alpha"]), Fr(r["b"])) == L[r["line"]] and r["order"] == T8.order(L[r["line"]])
                    for r in rows)
    per_point = {}
    for r in rows:
        per_point.setdefault((r["Re_tau"], r["Im_tau"]), set()).add(r["line"])
    slope = {n: sorted(ln[1] for ln in L if ln[0] == SLOPE and T8.order(ln) == n) for n in ORDERS}
    want = {25: sorted(Fr(k, 25) for k in range(25) if k % 5 != 0),
            30: sorted(Fr(k, 30) for k in range(30) if math.gcd(k, 6) == 1)}
    tenth = {n: sum(1 for ln in L if ln[0] == TENTH and T8.order(ln) == n) for n in ORDERS}
    classes = sorted({ln[0] for ln in L})
    return {"lines": len(L), "by order": {str(k): v for k, v in sorted(by.items())},
            "slope classes": len(classes), "the classes": [str(a) for a in classes],
            "census rows carry the own lines": stored_ok,
            "every point has all lines": all(v == set(range(len(L))) for v in per_point.values()),
            "slope-2/5 offsets per order": {str(n): [str(b) for b in v] for n, v in slope.items()},
            "slope-2/5 as stated": slope == want,
            "slope-1/10 lines per order": {str(n): v for n, v in tenth.items()}}


# ============================================================================================ the per-class minima
_K = {}
_C = {}


def _kinit(npz, cache):
    d = np.load(npz)
    arr = {k: d[k] for k in ("up", "dn", "lep")}
    sg = d["sg"]
    _K.clear()
    _K.update(cf=T42.configs(arr, "seat", sg), sg=sg, starts=d["starts"], cache=cache)


def classmin(T, block=100):
    """per slope class and target: the least chi2_six over the class's rows and the seat's menu; W142's direct sums
    (T42.direct_min), with the rows sorted by class and the minimum taken per class"""
    T = np.atleast_2d(T)
    st = _K["starts"]
    out = np.full((len(st), len(T)), np.inf)
    for _key, X, kind in _K["cf"]:
        t = T42.tmap(T, kind, _K["sg"])
        for s0 in range(0, len(t), block):
            tb = t[s0:s0 + block]
            acc = np.zeros((X.shape[0], len(tb)))
            for j in range(X.shape[1]):
                acc += (X[:, j][:, None] - tb[:, j][None, :]) ** 2
            np.minimum(out[:, s0:s0 + block], np.minimum.reduceat(acc, st, axis=0), out=out[:, s0:s0 + block])
    return out


def cache_path(seed):
    return Path(_K["cache"]) / ("classmin_%d.npy" % seed)


def seed_job(seed):
    p = cache_path(seed)
    if p.exists():
        return seed, "cache"
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    m = classmin(np.array(six))
    tmp = p.parent / ("classmin_%d.part.npy" % seed)
    np.save(tmp, m)
    os.replace(tmp, p)
    return seed, "computed"


def build_minima(files, rows, cache, workers):
    """the class-sorted arrays, the manifest, and every seed's minima (resumable)"""
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    alpha = {r["line"]: Fr(r["alpha"]) for r in rows}
    classes = sorted(set(alpha.values()))
    arr, lab = T8.census_arrays(rows)
    cid = np.array([classes.index(alpha[x[0]]) for x in lab])
    order = np.argsort(cid, kind="stable")
    cid = cid[order]
    starts = np.r_[0, np.flatnonzero(np.diff(cid)) + 1]
    assert len(starts) == len(classes) and (cid[starts] == np.arange(len(classes))).all()
    cache = Path(cache)
    cache.mkdir(parents=True, exist_ok=True)
    manifest = {"census sha256": files[SHAF].decode("utf-8").split()[0], "classes": [str(a) for a in classes],
                "array rows": int(len(cid)), "starts": [int(s) for s in starts], "targets per seed": T8.NTARGET,
                "menu": "seat", "rev": REV}
    mp_ = cache / "manifest.json"
    if mp_.exists():
        old = json.loads(mp_.read_text(encoding="utf-8"))
        if old != manifest:
            raise RuntimeError("the cache's manifest differs from this run's; not mixing")
    else:
        mp_.write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    npz = str(cache / "arrays.npz")
    np.savez(npz, up=arr["up"][order], dn=arr["dn"][order], lep=arr["lep"][order], sg=sg, starts=starts)
    _kinit(npz, str(cache))
    data = classmin(t6)[:, 0]
    del arr
    gc.collect()
    gc.freeze()                                    # the parent's objects stay out of the workers' collections
    seeds = SEEDS + FRESH
    status = {}
    with mpr.Pool(workers, initializer=_kinit, initargs=(npz, str(cache))) as P:
        for seed, how in P.imap_unordered(seed_job, seeds):
            status[seed] = how
            print("seed", seed, how, flush=True)
    gc.unfreeze()
    M = {s: np.load(cache_path(s)) for s in seeds}
    assert all(m.shape == (len(classes), T8.NTARGET) for m in M.values())
    return {"classes": classes, "data": data, "M": M, "status": status, "rows": int(len(cid))}


def part_minima(files, rows, cache, workers):
    mins = build_minima(files, rows, cache, workers)
    _C["mins"] = mins
    return {"rows": mins["rows"], "classes": [str(a) for a in mins["classes"]],
            "seeds read from the cache (a resumed run)": sorted(s for s, h in mins["status"].items() if h == "cache"),
            "seeds computed in this launch": len([s for s, h in mins["status"].items() if h == "computed"])}


# ======================================================================================= A2, A2f, C3: own chi-square
def main_class(name, classes, m):
    """main's four classes from the per-class minima (rows are the classes; columns the targets)"""
    i25, i10 = classes.index(SLOPE), classes.index(TENTH)
    if name == "a2/5":
        return m[i25]
    if name == "a1/10":
        return m[i10]
    if name == "rest":
        return np.delete(m, [i25, i10], axis=0).min(axis=0)
    return m.min(axis=0)


def calib(mins, name, seeds):
    obs = float(main_class(name, mins["classes"], mins["data"][:, None])[0])
    per = {s: float(np.mean(main_class(name, mins["classes"], mins["M"][s]) <= obs + 1e-9)) for s in seeds}
    return {"chi2_six_min": obs, "per_seed": {str(s): per[s] for s in seeds},
            "fraction_mean": float(np.mean([per[s] for s in seeds])),
            "fraction_max": float(np.max([per[s] for s in seeds])),
            "hits": int(round(sum(per[s] * T8.NTARGET for s in seeds)))}


def part_A2(files, mins):
    main = json.loads(files[V86 + "/comparison.json"].decode("utf-8"))
    out = {"classes": {}, "seeds": [SEEDS[0], SEEDS[-1]]}
    for name in ("a2/5", "a1/10", "rest", "all"):
        own = calib(mins, name, SEEDS)
        m = main["chi2"][name]["six|seat"]
        own["main"] = {k: m[k] for k in ("min", "fraction_mean", "fraction_max", "hits")}
        own["equal main (mean, worst seed, hits)"] = (own["fraction_mean"] == m["fraction_mean"]
                                                     and own["fraction_max"] == m["fraction_max"]
                                                     and own["hits"] == m["hits"])
        own["min_rel_vs_main"] = abs(own["chi2_six_min"] - m["min"]) / m["min"]
        half = lambda ss: int(round(sum(own["per_seed"][str(s)] * T8.NTARGET for s in ss)))  # noqa: E731
        own["hits, seeds 1829-1848"] = half(SEEDS[:20])
        own["hits, seeds 1849-1868"] = half(SEEDS[20:])
        out["classes"][name] = own
    out["per-class data minima (read-out)"] = {str(a): float(v) for a, v in zip(mins["classes"], mins["data"])}
    return out


def part_A2f(mins):
    out = {name: {k: v for k, v in calib(mins, name, FRESH_A2F).items()}
           for name in ("a2/5", "a1/10", "rest", "all")}
    out["seeds"] = [FRESH_A2F[0], FRESH_A2F[-1]]
    out["D's first half on the fresh seeds"] = out["a2/5"]["fraction_mean"] <= 0.001
    return out


def events(mins, seeds):
    classes = mins["classes"]
    i25 = classes.index(SLOPE)
    obs = float(mins["data"][i25])
    M = np.concatenate([mins["M"][s] for s in seeds], axis=1)
    n = M.shape[1]
    srt = np.sort(M, axis=0)
    arg = np.argmin(M, axis=0)
    any_ = srt[0] <= obs + 1e-9
    choose = any_ & (srt[1] >= BAR6)
    chosen25 = (M[i25] <= obs + 1e-9) & (np.delete(M, i25, axis=0).min(axis=0) >= BAR6)
    u, c = np.unique(arg[any_], return_counts=True)
    return {"targets": int(n), "obs (the data's slope-2/5 minimum)": obs,
            "class-choosing event (some class <= obs and every other >= 16.75)": int(choose.sum()),
            "class-choosing fraction": float(choose.sum() / n),
            "any class <= obs": int(any_.sum()), "any-class fraction": float(any_.sum() / n),
            "the slope 2/5 <= obs": int((M[i25] <= obs + 1e-9).sum()),
            "2/5 chosen (2/5 <= obs and every other >= 16.75)": int(chosen25.sum()),
            "classes carrying the any-class events": {str(classes[a]): int(b) for a, b in zip(u, c)},
            "share of the any-class events on the slope 2/5": (float(np.mean(arg[any_] == i25)) if any_.any()
                                                                 else None)}


def part_C3(mins):
    out = {"fresh seeds 1869-1928": events(mins, FRESH),
           "main's seeds 1829-1868 (diagnostic read-out)": events(mins, SEEDS)}
    f = out["fresh seeds 1869-1928"]["class-choosing fraction"]
    out["within the predicted band"] = C3_BAND[0] <= f <= C3_BAND[1]
    return out


# ============================================================================================ C1, B, C2, R


def part_C1(files, rows):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    L = own_lines86()
    pp = W63.per_point_line(rows, L, t6, sg)
    _C["86"] = pp
    below = sorted(((v[0], k, v) for k, v in pp.items() if v[0] < BAR6), key=lambda t: t[0])
    rr = [{"chi2_six": c, "line": [str(x) for x in L[k[0]]], "order": T8.order(L[k[0]]), "Re_tau": k[1],
           "Im_tau": k[2], "horocycle": v[1], "readings": v[2], "c": v[3]} for c, k, v in below]
    lines = sorted({L[k[0]] for _c, k, _v in below})
    on = all(ln[0] == SLOPE and ln[1] in OFFSETS[T8.order(ln)] for ln in lines) if lines else False
    per_line = {}
    for (k, x, y), v in pp.items():
        ln = L[k]
        if ln[0] == SLOPE:
            per_line[ln] = min(per_line.get(ln, math.inf), v[0])
    return {"points below 16.75": len(rr), "rows": rr, "lines": [[str(a), str(b)] for a, b in lines],
            "all on FINDINGS' twelve offsets": on, "horocycles": sorted({r["horocycle"] for r in rr}),
            "configurations": sorted({(tuple(r["readings"]), r["c"]) for r in rr}),
            "heights": [min(r["Im_tau"] for r in rr), max(r["Im_tau"] for r in rr)] if rr else None,
            "slope-2/5 per-line minima (read-out)": [[str(ln[1]), T8.order(ln), per_line[ln]]
                                                     for ln in sorted(per_line)]}


def part_B(root, files, rows):
    W93, W89 = T8.own_modules(root)
    W45._B.update(W93=W93, W89=W89, col=T8.L_column(files))
    L = own_lines86()
    idx = {ln: i for i, ln in enumerate(L)}
    pp = _C["86"]
    ranked = sorted(pp.items(), key=lambda kv: kv[1][0])
    kb = ranked[0][0]
    a, b = L[kb[0]]
    xb, yb = kb[1], kb[2]
    mline = mirror((a, b))
    mkey = next((k for k, _v in ranked if k[0] == idx.get(mline) and abs(k[1] - (1 - xb)) < 1e-9
                 and abs(k[2] - yb) < 1e-9), None)
    keys = [kb] + ([mkey] if mkey is not None else [])
    for k, _v in ranked:
        if len(keys) >= (6 if mkey is not None else 5):
            break
        if k not in keys:
            keys.append(k)
    named_ok = any(L[kb[0]] == ln and abs(kb[1] - x) < 5e-4 and abs(kb[2] - BEST[2]) < 5e-4
                   for ln, x in ((BEST[0], BEST[1]), (mirror(BEST[0]), 1 - BEST[1])))
    stored = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows if (r["line"], r["Re_tau"], r["Im_tau"]) in keys}
    controls = [((a, (b - a) % 1), xb + 1, yb),            # the T-step image
                ((a, b + 1), xb, yb),                      # b -> b + 1, the same w
                ((a, (-b - a) % 1), 1 - xb, yb)]           # the mirror image: -b at -x, then one T-step
    tasks = [(L[k[0]], k[1], k[2]) for k in keys] + controls
    with mpr.Pool(4) as P:
        res = P.map(W45.b_job, tasks)
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    per, own = [], {}
    for k, ((line, x, y), o, _diag) in zip(keys, res[:len(keys)]):
        dev = T8.compare_point(o, stored[k])
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        per.append({"line": [str(v) for v in line], "tau": [x, y], "chi2_six": pp[k][0], "deviation": dev})
        own[k] = o
    o_best = own[kb]
    return {"rows": per, "worst": worst, "the best row is FINDINGS' (or its mirror)": named_ok,
            "the mirror row is in the census": mkey is not None,
            "best row": {"line": [str(v) for v in L[kb[0]]], "tau": [xb, yb], "chi2_six": pp[kb][0]},
            "T-step image against the best row": T8.compare_point(res[-3][1], o_best),
            "b + 1 against the best row": T8.compare_point(res[-2][1], o_best),
            "mirror image against the best row": T8.compare_point(res[-1][1], o_best),
            "mirror image line": [str(v) for v in mirror((a, b))]}


def part_C2(files):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    L86, L49, L55 = own_lines86(), T8.own_lines(), W63.own_lines55()
    pp86 = _C["86"]
    rows49 = [r for r in T8.census_rows(files[V49 + "/census.jsonl"])
              if L49[r["line"]][0] == SLOPE and T8.order(L49[r["line"]]) == 10]
    pp49 = W63.per_point_line(rows49, L49, t6, sg)
    rows55 = [r for r in T8.census_rows(files[V55 + "/census.jsonl"])
              if L55[r["line"]][0] == SLOPE and T8.order(L55[r["line"]]) in (15, 20)]
    pp55 = W63.per_point_line(rows55, L55, t6, sg)
    del rows49, rows55
    # (i) the exact arithmetic
    s86 = [ln for ln in L86 if ln[0] == SLOPE]
    inv = all(mirror(mirror(ln)) == ln and mirror(ln) in s86 and T8.order(mirror(ln)) == T8.order(ln) for ln in s86)
    twelve = [(SLOPE, b) for n in ORDERS for b in OFFSETS[n]]
    pairs = sorted({tuple(sorted((ln, mirror(ln)))) for ln in twelve})
    six_pairs = (len(pairs) == 6 and all(p[0] != p[1] and p[1] in twelve for p in pairs)
                 and all(mirror(ln)[1] == (Fr(3, 5) - ln[1]) % 1 for ln in s86))
    per_line = {}
    for (k, x, y), v in pp86.items():
        if L86[k][0] == SLOPE:
            per_line[L86[k]] = min(per_line.get(L86[k], math.inf), v[0])
    pair_vals = [[[str(p[0][1]), per_line[p[0]]], [str(p[1][1]), per_line[p[1]]],
                  abs(per_line[p[0]] - per_line[p[1]]) / max(per_line[p[0]], per_line[p[1]])] for p in pairs]
    # (ii) the points
    lines_of = {"86": L86, "49": L49, "55": L55}
    below = {}
    for tag, pp in (("86", pp86), ("49", pp49), ("55", pp55)):
        for (k, x, y), v in pp.items():
            if v[0] < BAR6:
                below.setdefault(tag, set()).add((x, y))
    p86 = below.get("86", set())
    p_low = below.get("49", set()) | below.get("55", set())
    # R: the six over u at every point that carries a row below the bar at any order
    ro, passing = {}, []
    for pt in sorted(p86 | p_low):
        vals = []
        for tag, pp in (("49", pp49), ("55", pp55), ("86", pp86)):
            L = lines_of[tag]
            for (k, x, y), v in pp.items():
                if (x, y) == pt and L[k][0] == SLOPE:
                    vals.append([T8.order(L[k]), str(L[k][1]), W63.u_of(L[k], x), v[0]])
        vals.sort(key=lambda t: t[2])
        ro["%r" % (pt,)] = {"values": len(vals), "order, b, u, chi2_six (sorted by u)": vals}
    for tag, pp in (("49", pp49), ("55", pp55), ("86", pp86)):
        L = lines_of[tag]
        for (k, x, y), v in pp.items():
            if v[0] < BAR6 and L[k][0] == SLOPE:
                passing.append({"order": T8.order(L[k]), "b": str(L[k][1]), "x": x, "y": y,
                                "u": W63.u_of(L[k], x), "chi2_six": v[0]})
    return {"(i)": {"the mirror is an involution on the 30 slope-2/5 lines, order by order": inv,
                    "the twelve are six mirror pairs (b <-> 3/5 - b)": six_pairs,
                    "the pairs' line minima (read-out)": pair_vals},
            "(ii)": {"points below 16.75 at orders 25, 30": sorted(p86),
                     "points below 16.75 on slope-2/5 lines at orders 10, 15, 20": sorted(p_low),
                     "every order-25/30 point also carries a lower-order one": bool(p86) and p86 <= p_low,
                     "order-25/30 points not carried below": sorted(p86 - p_low)},
            "R: the six over u at the passing points": ro,
            "R: the passing rows": sorted(passing, key=lambda r: r["chi2_six"])}


# ============================================================================================ cells and main
def guarded(out, name, fn, *args):
    t0 = time.time()
    try:
        out[name] = fn(*args)
    except Exception:  # noqa: BLE001  (a failed part is a failed launch of that part, disclosed as such)
        out[name + "_failed"] = sanitize(traceback.format_exc()[-4000:])
    out.setdefault("part_seconds", {})[name] = round(time.time() - t0, 1)
    print("part", name, "done" if name in out else "FAILED", flush=True)


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
        c["A0"] = (all(a[p] for p in PIN) and a["decompressed census matches census.jsonl.sha256"]
                   and a["census rows"] == NROWS and a["census distinct (line, Re, Im)"] == NROWS
                   and a["census distinct points"] == NAPEX and all(v is True for v in a["ARTIFACT_HASHES"].values())
                   and all(a["lower orders' census pins (for C2)"].values()))
    if "A2" in out:
        k = out["A2"]["classes"]
        c["A2"] = (all(v["equal main (mean, worst seed, hits)"] and v["min_rel_vs_main"] < 1e-10 for v in k.values())
                   and abs(k["a2/5"]["chi2_six_min"] - FIND_MAIN["a2/5"][0]) <= 0.001
                   and k["a2/5"]["hits"] == FIND_MAIN["a2/5"][1]
                   and abs(k["a1/10"]["chi2_six_min"] - FIND_MAIN["a1/10"]) <= 1
                   and abs(k["rest"]["chi2_six_min"] - FIND_MAIN["rest"]) <= 1)
    if "A2f" in out:
        c["A2f"] = out["A2f"]["D's first half on the fresh seeds"]
    if "C3" in out:
        c["C3"] = out["C3"]["within the predicted band"]
    if "A3" in out:
        a = out["A3"]
        c["A3"] = (a["distinct census points"] == NAPEX and not a["word-point failures"]
                   and a["listed words equal the own window words"] and a["the points equal B1749's census points"])
    if "A4" in out:
        a = out["A4"]
        c["A4"] = (a["lines"] == 588 and a["by order"] == {str(k): v for k, v in COUNTS.items()}
                   and a["slope classes"] == NCLASS and a["census rows carry the own lines"]
                   and a["every point has all lines"] and a["slope-2/5 as stated"]
                   and a["slope-1/10 lines per order"] == {"25": 0, "30": 20})
    if "B" in out:
        b = out["B"]
        ts, b1, mi = b["T-step image against the best row"], b["b + 1 against the best row"], \
            b["mirror image against the best row"]
        fam = ("up", "down", "lep", "ckm")
        c["B0"] = (max(ts[f] for f in fam) < 1e-8 and ts["J_rel"] < 1e-8
                   and max(b1[f] for f in fam) < 1e-8 and b1["J_rel"] < 1e-8
                   and max(mi[f] for f in fam) < 1e-8 and abs(mi["J_rel"] - 2) < 1e-8
                   and b["the best row is FINDINGS' (or its mirror)"])
        w = b["worst"]
        c["B1"] = (b["the best row is FINDINGS' (or its mirror)"] and b["the mirror row is in the census"]
                   and max(w[f] for f in fam) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                   and w["zero_pattern_mismatches"] == 0)
    if "C1" in out:
        k = out["C1"]
        c["C1"] = (k["points below 16.75"] >= 1 and k["all on FINDINGS' twelve offsets"]
                   and 2.90 <= k["heights"][0] and k["heights"][1] <= 3.20)
    if "C2" in out:
        k = out["C2"]
        c["C2 (i)"] = (k["(i)"]["the mirror is an involution on the 30 slope-2/5 lines, order by order"]
                       and k["(i)"]["the twelve are six mirror pairs (b <-> 3/5 - b)"] and c.get("B0", False))
        c["C2 (ii)"] = k["(ii)"]["every order-25/30 point also carries a lower-order one"]
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--cache", required=True, help="a directory outside the repository for each seed's minima")
    args = ap.parse_args()
    root = T8.repo_root()
    cache = str(Path(args.cache).resolve())
    if Path(cache).is_relative_to(root):
        raise SystemExit("the cache must lie outside the repository")
    _ROOT["<cache>"] = cache
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W164", "rule": "W164_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers,
           "cache": "outside the repository (its path is not recorded)"}
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    for ln in files[ARC + "/ARTIFACT_HASHES.txt"].decode("utf-8").splitlines():
        if ln.strip() and not ln.startswith("#"):
            p = ln.split()[1]
            path = p if p.startswith("frontier/") else ARC + "/" + p
            if p != "census.jsonl" and path not in files:
                files[path] = T8.git_bytes(root, REV, path)
    census = gzip.decompress(files[GZ])
    rows = T8.census_rows(census)
    guarded(out, "A0", part_A0, files, census, rows)
    del census
    guarded(out, "A3", part_A3, files, rows)
    guarded(out, "A4", part_A4, rows)
    guarded(out, "C1", part_C1, files, rows)
    guarded(out, "minima", part_minima, files, rows, cache, args.workers)
    mins = _C.get("mins")
    if mins:
        guarded(out, "A2", part_A2, files, mins)
        guarded(out, "A2f", part_A2f, mins)
        guarded(out, "C3", part_C3, mins)
    guarded(out, "B", part_B, root, files, rows)
    del rows
    gc.collect()
    guarded(out, "C2", part_C2, files)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    out["opinion"] = {"agrees with main's scope (a selection by the data, not a derivation; ungraded, a READING)":
                      bool(all(c.get(k) for k in ("A2", "B1", "C1", "C3")))}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("cells written:", len(out["cells"]))
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
