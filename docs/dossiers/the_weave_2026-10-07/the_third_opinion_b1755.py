#!/usr/bin/env python3
"""W163 — the third opinion on main's B1755, the six on the lines of order 13, 14, 15 and 20 (the rule: W163_RULE.md,
committed and pushed before this script).  It runs once, from the repository root.

W157's script (the_third_opinion_b1753.py) is loaded unchanged, with W156's and W145's under it; their helpers are
reused (the census loader, the own instrument, the direct-sum chi-square, the own draws, the apex code, the T-law
classes).  New here: B1755's comparison is class by class (13, 14, 15, 20, and 15 and 20), so A1's diff and A2's
calibration are written for that layout; the 396 lines of orders 13-20 are enumerated again (A4); the per-line split is
read as one function of (Re tau mod 1, Im tau, Re w mod 1) and each order's passing lines are predicted from the other
two orders by interpolation in Re w (C2).  Main's code is run only in A1, in a temporary tree.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1755.py [--workers 4]
"""
import argparse
import contextlib
import importlib.util
import io
import json
import math
import multiprocessing as mpr
import platform
import subprocess
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
    import the_third_opinion_b1753 as W57    # noqa: E402  (W157, which loads W156's and W145's modules)
W56 = W57.W56
W45, T8, T42 = W56.W45, W56.T8, W56.T42

REV = "11ebe577b8ece7f29b3c6854c52e3a64336596b2"      # origin/main as read for the rule
ARC = "frontier/B1755_the_six_on_the_lines_of_order_13_to_20"
V55 = ARC + "/verification"
V49, V41, V26 = W56.V49, W56.V41, W45.V26
FILES = (V55 + "/compare.py", V55 + "/census.py", V55 + "/census.jsonl", V55 + "/control.json",
         V55 + "/comparison.json", ARC + "/ARTIFACT_HASHES.txt", V41 + "/compare.py", V41 + "/census.jsonl",
         V26 + "/census.py", V26 + "/census.jsonl", W56.B1720T, W56.B1720G, W45.HZ, W45.CKM, W45.COLUMN,
         V49 + "/census.py", V49 + "/census.jsonl", V49 + "/comparison.json") + W45.DEPS
PIN = {V55 + "/census.jsonl": "2589220dc7f1e94683b8c41be013c5a46a05dba6e6c5bc4041d765328351a6f8",
       V55 + "/comparison.json": "f780fd37fc21a4b2f7c7f494d2de7b0959341397b49d29adf0853a92cbebdfb9",
       V55 + "/control.json": "19700264359dee8b7ace6bf1b3f11b731adc876e70ce709c605344df99e421ee"}
PIN49 = {V49 + "/census.jsonl": W56.PIN[V49 + "/census.jsonl"]}
OUT = HERE / "third_opinion_b1755.json"
SEEDS = tuple(range(1809, 1829))
FRESH = tuple(range(1829, 1849))
ORDERS = (13, 14, 15, 20)
COUNTS = {13: 84, 14: 72, 15: 96, 20: 144}
CLASSES = {"13": (13,), "14": (14,), "15": (15,), "20": (20,), "15+20": (15, 20)}
NROWS, NAPEX = 49500, 125
LN3 = math.log(3)
BAR6 = 16.75
WINDOW = (2.0, 3.6)
SLOPE = Fr(2, 5)
PASS = {15: {Fr(2, 3), Fr(14, 15), Fr(1, 3), Fr(4, 15)}, 20: {Fr(7, 20), Fr(1, 4), Fr(9, 20), Fr(3, 20)}}
BEST = ((SLOPE, Fr(14, 15)), 0.5, 3.0619)                  # FINDINGS section 1: the best row, L_max
FIND_MAIN = {"15+20": (5.33, 78), "13": 0.0494, "14": 0.423, "15": 30, "nine": 148.9}
TOL = T8.TOL

_ROOT = W45._ROOT


def sanitize(text):
    return W45.sanitize(text)


def key_of(a, b):
    return W57.key_of(Fr(a), Fr(b))


def own_lines55():
    """every flat line of exact order 13, 14, 15 or 20 up to sign, in B1726's enumeration, written again"""
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


def rows55(files):
    return T8.census_rows(files[V55 + "/census.jsonl"])


# ============================================================================================ A0
def part_A0(files):
    out = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    rows = rows55(files)
    out["census rows"] = len(rows)
    out["census distinct (line, Re, Im)"] = len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
    out["census distinct points"] = len({(r["Re_tau"], r["Im_tau"]) for r in rows})
    pinned = {}
    for ln in files[ARC + "/ARTIFACT_HASHES.txt"].decode("utf-8").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        h, p = ln.split()[0], ln.split()[1]
        path = p if p.startswith("frontier/") else ARC + "/" + p
        pinned[path] = (T8.sha256(files[path]) == h) if path in files else "not fetched"
    out["ARTIFACT_HASHES"] = pinned
    out["B1749 census pin (for C2)"] = all(T8.sha256(files[p]) == h for p, h in PIN49.items())
    return out


# ============================================================================================ A1: the re-run
def build_tree(tmp, files):
    (tmp / "GENESIS.md").write_text("root marker for the W163 re-run (not main's GENESIS)\n", encoding="utf-8")
    for p, b in files.items():
        q = tmp / p
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_bytes(b)
    return tmp / V55


def diff_at(old, new, rel_tol):
    dd = T8.deep_diff(old, new)
    real = []
    for m in dd["mismatches"]:
        if len(m) == 3 and isinstance(m[1], (int, float)) and isinstance(m[2], (int, float)) \
                and not isinstance(m[1], bool) and not isinstance(m[2], bool):
            a, b = m[1], m[2]
            if abs(a - b) / max(abs(a), abs(b), 1e-300) <= rel_tol:
                continue
        real.append(W45.bool_safe([str(x) for x in m]))
    return {"numbers": dd["numbers"], "exact": dd["exact"], "max_rel": dd["max_rel"], "mismatches": real[:40],
            "mismatch count": len(real)}


def part_A1(files, workers):
    out = {}
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp>"] = td
        vdir = build_tree(Path(td), files)
        t0 = time.time()
        p = subprocess.run([sys.executable, "-B", str(vdir / "compare.py"), "--workers", str(workers)], cwd=vdir,
                           capture_output=True, text=True)
        out["compare"] = {"returncode": p.returncode, "seconds": round(time.time() - t0, 1),
                          "stderr_tail": sanitize(p.stderr[-3000:])}
        new = json.loads((vdir / "comparison.json").read_text(encoding="utf-8")) if p.returncode == 0 else None
        main_lines = []
        try:                                       # B1755's lines(), for A4, guarded apart from the re-run
            spec = importlib.util.spec_from_file_location("b1755_census_for_lines", vdir / "census.py")
            K = importlib.util.module_from_spec(spec)
            with contextlib.redirect_stdout(io.StringIO()):
                spec.loader.exec_module(K)
            main_lines = [(Fr(a), Fr(b)) for a, b in K.lines()]
        except Exception:  # noqa: BLE001
            out["lines_failed"] = sanitize(traceback.format_exc()[-2000:])
    old = json.loads(files[V55 + "/comparison.json"].decode("utf-8"))
    if new is not None:
        out["diff"] = diff_at(old, new, 1e-10)
        out["cells identical"] = old["cells"] == new["cells"]
        out["fractions exact"] = all(old["chi2"][c][k][f] == new["chi2"][c][k][f]
                                     for c in old["chi2"] for k in old["chi2"][c]
                                     for f in ("fraction_mean", "fraction_max", "hits"))
    out["main_lines"] = [[str(a), str(b)] for a, b in main_lines]
    return out


# ======================================================================================= A2, A2f, C3: own chi-square
def class_arrays(files, orders):
    rows = [r for r in rows55(files) if r["order"] in orders]
    return T8.census_arrays(rows)


def seat_job(seed):
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    T = np.array(six)
    cf = T42.configs(T42._W["arr"], "seat", T42._W["sg"])
    obs = float(T42.direct_min(cf, T42._W["T6"], T42._W["sg"])[0][0])
    return seed, obs, float(np.mean(T42.direct_min(cf, T, T42._W["sg"])[0] <= obs + 1e-9))


def calibrate(files, orders, seeds, workers, tmp, name):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    arr, lab = class_arrays(files, orders)
    npz = str(Path(tmp) / ("%s.npz" % name.replace("+", "_")))
    np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=sg)
    with mpr.Pool(workers, initializer=T42._init, initargs=(name, npz, 0.10)) as P:
        res = P.map(seat_job, seeds)
    per = {s: f for s, _o, f in res}
    return {"rows": int(arr["up"].shape[0]), "chi2_six_min": res[0][1], "per_seed": {str(s): per[s] for s in seeds},
            "fraction_mean": float(np.mean([per[s] for s in seeds])),
            "fraction_max": float(np.max([per[s] for s in seeds])),
            "hits": int(round(sum(per[s] * T8.NTARGET for s in seeds)))}, arr, lab


def part_A2(files, workers, tmp):
    main = json.loads(files[V55 + "/comparison.json"].decode("utf-8"))
    t6, t9 = T8.targets(files)
    sg = T42.sigma(files)
    s9 = np.concatenate([sg, T42.sigma_ckm(files)])
    out = {"classes": {}}
    for name, orders in CLASSES.items():
        own, arr, lab = calibrate(files, orders, SEEDS, workers, tmp, name)
        m = main["chi2"][name]["six|seat"]
        own["main"] = {k: m[k] for k in ("min", "fraction_mean", "fraction_max", "hits")}
        own["equal main (mean, worst seed, hits)"] = (own["fraction_mean"] == m["fraction_mean"]
                                                     and own["fraction_max"] == m["fraction_max"]
                                                     and own["hits"] == m["hits"])
        own["min_rel_vs_main"] = abs(own["chi2_six_min"] - m["min"]) / m["min"]
        half = lambda ss: int(round(sum(own["per_seed"][str(s)] * T8.NTARGET for s in ss)))  # noqa: E731
        own["hits, seeds 1809-1818"] = half(SEEDS[:10])
        own["hits, seeds 1819-1828"] = half(SEEDS[10:])
        own["seeds 1809 and 1828, reported apart"] = {str(s): own["per_seed"][str(s)] for s in (1809, 1828)}
        if name == "15+20":
            n9 = W45.nine(arr, lab, t9, s9, T8.SEAT)
            n9["main"] = main["chi2"][name]["nine|seat"]["min"]
            n9["rel_vs_main"] = abs(n9["chi2_nine_min"] - n9["main"]) / n9["main"]
            own["chi2_nine (seat)"] = n9
        out["classes"][name] = own
    return out


def part_A2f(files, workers, tmp):
    out = {}
    for name in ("15+20", "13", "14"):
        own, _arr, _lab = calibrate(files, CLASSES[name], FRESH, workers, tmp, "fresh" + name)
        out[name] = own
    out["D on the fresh seeds"] = (out["15+20"]["fraction_mean"] <= 0.001 and out["13"]["fraction_mean"] > 0.01
                                   and out["14"]["fraction_mean"] > 0.01)
    return out


def part_C3(files, workers, tmp):
    out = {}
    for name, orders in (("13+14+15 pooled", (13, 14, 15)), ("15 alone", (15,))):
        own, _arr, _lab = calibrate(files, orders, SEEDS, workers, tmp, "c3_" + name.split()[0])
        out[name] = {k: own[k] for k in ("rows", "chi2_six_min", "fraction_mean", "fraction_max", "hits")}
    return out


# ============================================================================================ A3: the points
def part_A3(files):
    words12 = W56.necklaces(12)
    inwin = {}
    for w in words12:
        h, pts = W56.tops(w)
        if WINDOW[0] <= h <= WINDOW[1]:
            inwin[w] = (h, pts)
    points = {}
    for r in rows55(files):
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
def part_A4(files, a1):
    L = own_lines55()
    by = {}
    for ln in L:
        by[T8.order(ln)] = by.get(T8.order(ln), 0) + 1
    rows = rows55(files)
    stored_ok = all((Fr(r["alpha"]), Fr(r["b"])) == L[r["line"]] and r["order"] == T8.order(L[r["line"]])
                    for r in rows)
    per_point = {}
    for r in rows:
        per_point.setdefault((r["Re_tau"], r["Im_tau"]), set()).add(r["line"])
    slope = {n: sorted(str(ln[1]) for ln in L if ln[0] == SLOPE and T8.order(ln) == n) for n in ORDERS}
    want15 = sorted(str(Fr(k, 15)) for k in range(15) if k % 3 != 0)
    want20 = sorted(str(Fr(k, 20)) for k in range(1, 20, 2))
    main = [(Fr(a), Fr(b)) for a, b in a1["main_lines"]] if a1 and a1.get("main_lines") else None
    return {"lines": len(L), "by order": {str(k): v for k, v in sorted(by.items())},
            "census rows carry the own lines": stored_ok,
            "every point has all lines": all(v == set(range(len(L))) for v in per_point.values()),
            "slope-2/5 offsets per order": slope,
            "slope-2/5 as stated": (not slope[13] and not slope[14] and slope[15] == want15 and slope[20] == want20),
            "main's lines() equals the own enumeration in order": (main == L) if main is not None else None}


# ============================================================================================ B: own instrument
def part_B(root, files, a2):
    W93, W89 = T8.own_modules(root)
    W45._B.update(W93=W93, W89=W89, col=T8.L_column(files))
    rows = rows55(files)
    L = own_lines55()
    stored = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    arr, lab = T8.census_arrays(rows)
    best, _arg = W56.seat_best_per_row(arr, t6, sg)
    order_ = np.argsort(best)
    keys, seen, best20 = [], set(), None
    for i in order_:
        kk = lab[i][:3]
        if kk in seen:
            continue
        seen.add(kk)
        if len(keys) < 5:
            keys.append(kk)
        if best20 is None and T8.order(L[kk[0]]) == 20:
            best20 = kk
        if len(keys) >= 5 and best20 is not None:
            break
    if best20 not in keys:
        keys.append(best20)
    kb = keys[0]
    named_ok = (L[kb[0]] in (BEST[0], (SLOPE, Fr(2, 3))) and abs(kb[1] - BEST[1]) < 5e-4
                and abs(kb[2] - BEST[2]) < 5e-4)
    xb, yb = kb[1], kb[2]
    a, b = L[kb[0]]
    controls = [((a, (b - a) % 1), xb + 1, yb),            # the T-step image
                ((a, b + 1), xb, yb),                      # b -> b + 1, the same w
                ((a, (-b) % 1), -xb, yb)]                  # the mirror image
    tasks = [(L[k], x, y) for (k, x, y) in keys] + controls
    with mpr.Pool(4) as P:
        res = P.map(W45.b_job, tasks)
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    per, own = [], {}
    for (line, x, y), o, _diag in res[:len(keys)]:
        k = L.index(line)
        dev = T8.compare_point(o, stored[(k, x, y)])
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        per.append({"line": [str(v) for v in line], "tau": [x, y], "deviation": dev})
        own[(k, x, y)] = o
    o_best = own[kb]
    return {"rows": per, "worst": worst, "the best row is FINDINGS' (or its mirror)": named_ok,
            "best row": {"line": [str(v) for v in L[kb[0]]], "tau": [xb, yb], "chi2_six": float(best[order_[0]])},
            "T-step image against the best row": T8.compare_point(res[-3][1], o_best),
            "b + 1 against the best row": T8.compare_point(res[-2][1], o_best),
            "mirror image against the best row": T8.compare_point(res[-1][1], o_best)}


# ============================================================================================ C1, C2
_C = {}


def per_point_line(rows, lines, t6, sg):
    """the seat's chi2_six per (point, line): the least over the menu and both horocycles"""
    arr, lab = T8.census_arrays(rows)
    best, arg = W56.seat_best_per_row(arr, t6, sg)
    out = {}
    for i, (k, x, y, h) in enumerate(lab):
        key = (k, x, y)
        if key not in out or best[i] < out[key][0]:
            a, b, l, kk = arg[i]
            out[key] = (float(best[i]), h, [T8.RD[a], T8.RD[b], T8.RD[l]], round(math.exp(kk)))
    return out


def part_C1(files):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    L = own_lines55()
    pp = per_point_line(rows55(files), L, t6, sg)
    _C["55"] = pp
    below = sorted(((v[0], k, v) for k, v in pp.items() if v[0] < BAR6), key=lambda t: t[0])
    rr = [{"chi2_six": c, "line": [str(x) for x in L[k[0]]], "Re_tau": k[1], "Im_tau": k[2], "horocycle": v[1],
           "readings": v[2], "c": v[3]} for c, k, v in below]
    lines = sorted({(L[k[0]][0], L[k[0]][1]) for _c, k, _v in below})
    ok_lines = all(ln[0] == SLOPE and ln[1] in PASS[T8.order(ln)] for ln in lines) if lines else False
    return {"points below 16.75": len(rr), "rows": rr, "lines": [[str(a), str(b)] for a, b in lines],
            "all on FINDINGS' eight lines": ok_lines, "horocycles": sorted({r["horocycle"] for r in rr}),
            "configurations": sorted({(tuple(r["readings"]), r["c"]) for r in rr}),
            "heights": [min(r["Im_tau"] for r in rr), max(r["Im_tau"] for r in rr)] if rr else None}


def u_of(line, x):
    return float((float(line[0]) * x + float(line[1])) % 1.0)


def interp_periodic(us, vs, u):
    """linear interpolation in u on the circle of length 1"""
    o = np.argsort(us)
    us, vs = np.asarray(us)[o], np.asarray(vs)[o]
    ue = np.concatenate([us[-1:] - 1.0, us, us[:1] + 1.0])
    ve = np.concatenate([vs[-1:], vs, vs[:1]])
    return float(np.interp(u % 1.0, ue, ve))


def spearman(a, b):
    def ranks(v):
        v = np.asarray(v, dtype=float)
        o = np.argsort(v, kind="mergesort")
        r = np.empty(len(v))
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[o[j + 1]] == v[o[i]]:
                j += 1
            r[o[i:j + 1]] = (i + j) / 2.0
            i = j + 1
        return r
    ra, rb = ranks(a), ranks(b)
    return float(np.corrcoef(ra, rb)[0, 1])


def part_C2(files):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    L55, L49 = own_lines55(), T8.own_lines()
    pp55 = _C["55"] if "55" in _C else per_point_line(rows55(files), L55, t6, sg)
    rows49 = [r for r in T8.census_rows(files[V49 + "/census.jsonl"])
              if L49[r["line"]][0] == SLOPE and T8.order(L49[r["line"]]) == 10]
    pp49 = per_point_line(rows49, L49, t6, sg)
    # (i) the exact arithmetic
    cls = {}
    for n in (15, 20):
        lines = [ln for ln in L55 if ln[0] == SLOPE and T8.order(ln) == n]
        tc = W57.t_classes(lines)
        idx = {ln: i for i, c in enumerate(tc) for ln in c}
        passing = [(SLOPE, b) for b in PASS[n]]
        mirror_cls = {i: idx[key_of(SLOPE, -tc[i][0][1])] for i in range(len(tc))}
        cls[str(n)] = {"class sizes": sorted(len(c) for c in tc),
                       "passing per class": sorted(sum(1 for p in passing if idx[p] == i) for i in range(len(tc))),
                       "the mirror exchanges the classes": all(mirror_cls[i] != i for i in mirror_cls)}
    exact = all(v["class sizes"] == [5, 5] and v["passing per class"] == [2, 2]
                and v["the mirror exchanges the classes"] for v in cls.values())
    # (ii) the samples per point: (u, log chi2) for each slope-2/5 line of orders 10, 15 and 20
    samples = {}                                   # point -> order -> list of (line, u, chi2)
    for (k, x, y), v in pp49.items():
        samples.setdefault((x, y), {}).setdefault(10, []).append((L49[k], u_of(L49[k], x), v[0]))
    for (k, x, y), v in pp55.items():
        ln = L55[k]
        if ln[0] == SLOPE:
            samples.setdefault((x, y), {}).setdefault(T8.order(ln), []).append((ln, u_of(ln, x), v[0]))
    pred = {}
    for target, others in ((20, (10, 15)), (15, (10, 20))):
        actual, predicted = {}, {}
        for pt, by in samples.items():
            known = [s for o in others for s in by.get(o, [])]
            us, vs = [s[1] for s in known], [math.log(s[2]) for s in known]
            for ln, u, c in by.get(target, []):
                actual[ln] = min(actual.get(ln, math.inf), c)
                predicted[ln] = min(predicted.get(ln, math.inf), math.exp(interp_periodic(us, vs, u)))
        lines = sorted(actual)
        pset = {ln[1] for ln in lines if predicted[ln] < BAR6}
        aset = {ln[1] for ln in lines if actual[ln] < BAR6}
        pred[str(target)] = {
            "per line (b, actual, predicted)": [[str(ln[1]), actual[ln], predicted[ln]] for ln in lines],
            "predicted below 16.75": sorted(str(b) for b in pset), "actual below 16.75": sorted(str(b) for b in aset),
            "predicted set equals FINDINGS' four": pset == PASS[target],
            "actual set equals FINDINGS' four": aset == PASS[target],
            "spearman": spearman([actual[ln] for ln in lines], [predicted[ln] for ln in lines])}
    # read-out: the passing points' (x, y, u) and 5u + 3x mod 1
    ro = []
    for (k, x, y), v in pp55.items():
        if v[0] < BAR6:
            ln = L55[k]
            u = u_of(ln, x)
            ro.append({"line": [str(ln[0]), str(ln[1])], "x": x, "y": y, "u": u, "5u + 3x mod 1": (5 * u + 3 * x) % 1.0,
                       "chi2_six": v[0]})
    for (k, x, y), v in pp49.items():
        if v[0] < BAR6:
            ln = L49[k]
            u = u_of(ln, x)
            ro.append({"line": [str(ln[0]), str(ln[1])], "x": x, "y": y, "u": u, "5u + 3x mod 1": (5 * u + 3 * x) % 1.0,
                       "chi2_six": v[0], "census": "B1749"})
    return {"(i)": {"classes": cls, "as stated": exact}, "(ii)": pred,
            "read-out: the passing points": sorted(ro, key=lambda r: r["chi2_six"])}


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
        c["A0"] = (all(a[p] for p in PIN) and a["census rows"] == NROWS and a["census distinct (line, Re, Im)"] == NROWS
                   and a["census distinct points"] == NAPEX and all(v is True for v in a["ARTIFACT_HASHES"].values()))
    if "A1" in out:
        a = out["A1"]
        c["A1"] = (a["compare"]["returncode"] == 0 and a.get("cells identical") and a.get("fractions exact")
                   and a.get("diff", {"mismatch count": 1})["mismatch count"] == 0)
    if "A2" in out:
        k = out["A2"]["classes"]
        c["A2"] = (all(v["equal main (mean, worst seed, hits)"] and v["min_rel_vs_main"] < 1e-10 for v in k.values())
                   and abs(k["15+20"]["chi2_six_min"] - FIND_MAIN["15+20"][0]) < 0.01
                   and k["15+20"]["hits"] == FIND_MAIN["15+20"][1]
                   and abs(k["13"]["fraction_mean"] - FIND_MAIN["13"]) <= 0.0001
                   and abs(k["14"]["fraction_mean"] - FIND_MAIN["14"]) <= 0.0005       # FINDINGS' 42.3%
                   and k["15"]["hits"] == FIND_MAIN["15"]
                   and abs(k["15+20"]["chi2_nine (seat)"]["chi2_nine_min"] - FIND_MAIN["nine"]) < 0.5)
    if "A2f" in out:
        c["A2f"] = out["A2f"]["D on the fresh seeds"]
    if "A3" in out:
        a = out["A3"]
        c["A3"] = (a["distinct census points"] == NAPEX and not a["word-point failures"]
                   and a["listed words equal the own window words"] and a["the points equal B1749's census points"])
    if "A4" in out:
        a = out["A4"]
        c["A4"] = (a["lines"] == 396 and a["by order"] == {str(k): v for k, v in COUNTS.items()}
                   and a["census rows carry the own lines"] and a["every point has all lines"]
                   and a["slope-2/5 as stated"] and a["main's lines() equals the own enumeration in order"])
    if "B" in out:
        b = out["B"]
        ts, b1, mi = b["T-step image against the best row"], b["b + 1 against the best row"], \
            b["mirror image against the best row"]
        fam = ("up", "down", "lep", "ckm")
        c["B0"] = (max(ts[f] for f in fam) < 1e-8 and ts["J_rel"] < 1e-8
                   and max(b1[f] for f in fam) < 1e-8 and b1["J_rel"] < 1e-8
                   and max(mi[f] for f in fam) < 1e-8 and abs(mi["J_rel"] - 2) < 1e-8)
        w = b["worst"]
        c["B1"] = (b["the best row is FINDINGS' (or its mirror)"]
                   and max(w[f] for f in fam) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                   and w["zero_pattern_mismatches"] == 0)
    if "C1" in out:
        k = out["C1"]
        c["C1"] = (k["points below 16.75"] >= 1 and k["all on FINDINGS' eight lines"] and k["horocycles"] == ["L_max"]
                   and 2.90 <= k["heights"][0] and k["heights"][1] <= 3.20)
    if "C2" in out:
        k = out["C2"]
        c["C2 (i)"] = k["(i)"]["as stated"] and c.get("B0", False)
        c["C2 (ii) order 20"] = k["(ii)"]["20"]["predicted set equals FINDINGS' four"]
        c["C2 (ii) order 15"] = k["(ii)"]["15"]["predicted set equals FINDINGS' four"]
        c["C2r"] = k["(ii)"]["20"]["spearman"] >= 0.6 and k["(ii)"]["15"]["spearman"] >= 0.6
    if "C3" in out:
        k = out["C3"]
        c["C3"] = abs(k["13+14+15 pooled"]["fraction_mean"] - 0.00096) <= 0.0001 and k["15 alone"]["hits"] == 30
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W163", "rule": "W163_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers}
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    guarded(out, "A0", part_A0, files)
    guarded(out, "A1", part_A1, files, args.workers)
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp2>"] = td
        guarded(out, "A2", part_A2, files, args.workers, td)
        guarded(out, "A2f", part_A2f, files, args.workers, td)
        guarded(out, "C3", part_C3, files, args.workers, td)
    guarded(out, "A3", part_A3, files)
    guarded(out, "A4", part_A4, files, out.get("A1"))
    guarded(out, "C1", part_C1, files)
    guarded(out, "C2", part_C2, files)
    guarded(out, "B", part_B, root, files, out.get("A2"))
    if "A1" in out:
        out["A1"].pop("main_lines", None)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    out["opinion"] = {"agrees with main's scope (through the slope; ungraded, a READING)":
                      bool(all(c.get(k) for k in ("A1", "A2", "B1", "C1", "C3")))}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("cells written:", len(out["cells"]))
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
