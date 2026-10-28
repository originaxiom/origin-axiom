#!/usr/bin/env python3
"""W165 — the third opinion on main's B1792, the offset recurrence at order 60 (P-399; the rule: W165_RULE.md,
committed and pushed before this script).  It runs once, from the repository root.

W164's script (the_third_opinion_b1786.py) is loaded unchanged, with W163's, W157's, W156's and W145's under it;
their helpers are reused (the own instrument, the census arrays, the per-point minima, the direct-sum chi-square and
its per-class minima, the own draws).  New here:
  - the own census: at each of the 125 apexes, the twenty slope-2/5 lines of exact order 60 on the own instrument,
    computed before main's census is compared, each apex saved to a cache outside the repository as soon as it is done
    (a restart resumes; the output names the apexes read from the cache);
  - the own census against main's committed census at every point (K2);
  - the carrying set by two routes, from the own census and by own chi-square code from main's (K3);
  - the controls on (2/5, 1/60) at the middle apex (K4).
Main's census.py and compare.py are not run.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1792.py --cache DIR [--workers 4]
"""
import argparse
import contextlib
import gc
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
    import the_third_opinion_b1786 as W64    # noqa: E402  (W164, which loads W163's, W157's, W156's, W145's)
W63, W56 = W64.W63, W64.W56
W45, T8, T42 = W64.W45, W64.T8, W64.T42

REV = "be216a281"                                       # origin/main as read for the rule (resolved at run time)
ARC = "frontier/B1792_the_offset_recurrence_at_order_60"
V92 = ARC + "/verification"
V49 = W56.V49
PIN = {ARC + "/PREREGISTRATION.md": "0e17d2e776b3390eabaa89be591b338ed884fb6f12b52b4dcedf73b661459b38",
       V92 + "/census.py": "e696036b41eb81bc87fe0e81e73bddf7800dc97ade660d25ca240600501b3920",
       V92 + "/compare.py": "40435d82631a5e5ef0d561412ff00ea51f7d1fe9dd6fc5180ae46907d45de671",
       V92 + "/census.jsonl": "d1800553ab723ed10f181a122da1c01c36b635d2c9f171bb6e9a7a0e8dcaad8e"}
PIN49 = {V49 + "/census.jsonl": W56.PIN[V49 + "/census.jsonl"]}
FILES = tuple(PIN) + (V92 + "/control.json", V49 + "/census.jsonl", T8.HZ, T8.CKM, T8.COLUMN) + W45.DEPS
OUT = HERE / "third_opinion_b1792.json"
SLOPE = Fr(2, 5)
PRED_K = (1, 7, 29, 35, 41, 47, 49, 55)
ORDER20 = (Fr(7, 20), Fr(1, 4), Fr(9, 20), Fr(3, 20))   # B1755's order-20 carriers
SEEDS = tuple(range(4501, 4541))                          # main's specificity seeds (B1792's PREREGISTRATION)
NROWS, NAPEX, NLINES = 2500, 125, 20
BAR6 = 16.75
TOL = T8.TOL
_ROOT = W45._ROOT


def sanitize(text):
    return W45.sanitize(text)


def own_lines60():
    """the twenty slope-2/5 lines of exact order 60 up to sign, b = k/60 in increasing k (each its own key, since
    2/5 < 3/5)"""
    out = []
    for k in range(60):
        if math.gcd(k, 6) != 1:
            continue
        b = Fr(k, 60)
        key = min((SLOPE, b), ((-SLOPE) % 1, (-b) % 1))
        assert key == (SLOPE, b) and math.lcm(5, b.denominator) == 60
        out.append(key)
    return out


def mirror(line):
    return W64.mirror(line)


def predicted():
    return {(SLOPE, (b + Fr(j, 3)) % 1) for b in ORDER20 for j in (1, 2)}


# ============================================================================================ K0, K1
def main_rows(files):
    return T8.census_rows(files[V92 + "/census.jsonl"])


def points_of(rows):
    """the apex points as main's rows list them: apex index -> (Re tau, Im tau)"""
    pts = {}
    for r in rows:
        pts.setdefault(r["apex"], (r["Re_tau"], r["Im_tau"]))
    return pts


def part_K0(files, rows):
    out = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    out["census rows"] = len(rows)
    out["census distinct (line, Re, Im)"] = len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
    out["census distinct points"] = len({(r["Re_tau"], r["Im_tau"]) for r in rows})
    out["census apex indices"] = len(points_of(rows))
    p49 = {(r["Re_tau"], r["Im_tau"]) for r in T8.census_rows(files[V49 + "/census.jsonl"])}
    out["B1749 census pin"] = all(T8.sha256(files[p]) == h for p, h in PIN49.items())
    out["the points equal B1749's census points"] = {(r["Re_tau"], r["Im_tau"]) for r in rows} == p49
    return out


def part_K1(rows):
    L = own_lines60()
    carried = all((Fr(r["alpha"]), Fr(r["b"])) == L[r["line"]] and r["order"] == 60 for r in rows)
    pred = predicted()
    per_point = {}
    for r in rows:
        per_point.setdefault((r["Re_tau"], r["Im_tau"]), set()).add(r["line"])
    return {"lines": len(L), "offsets k": [int(b * 60) for _a, b in L],
            "every k coprime to 6": all(math.gcd(int(b * 60), 6) == 1 for _a, b in L),
            "main's rows carry the own lines": carried,
            "every point has all twenty lines": all(v == set(range(len(L))) for v in per_point.values()),
            "predicted k": sorted(int(b * 60) for _a, b in pred),
            "predicted as stated": sorted(int(b * 60) for _a, b in pred) == list(PRED_K),
            "predicted lines are among the twenty": pred <= set(L),
            "predicted set closed under the mirror": all(mirror(ln) in pred for ln in pred),
            "the twenty closed under the mirror": all(mirror(ln) in set(L) for ln in L)}


# ============================================================================================ the own census
_O = {}


def apex_job(task):
    """one apex: the twenty lines on the own instrument, saved to the cache as soon as they are done"""
    pi, re_t, im_t = task
    p = Path(_O["cache"]) / ("apex_%03d.json" % pi)
    if p.exists():
        return pi, "cache"
    rows = []
    for k, line in enumerate(own_lines60()):
        o, _diag = T8.own_point(_O["W93"], _O["W89"], _O["col"], line, re_t, im_t)
        r = {key: [float(v) for v in val] for key, val in o.items()}
        r.update(line=k, Re_tau=re_t, Im_tau=im_t, apex=pi)
        rows.append(r)
    tmp = p.parent / ("apex_%03d.part.json" % pi)
    tmp.write_text(json.dumps(rows), encoding="utf-8")
    os.replace(tmp, p)
    return pi, "computed"


def part_census(root, files, rows, cache, workers):
    W93, W89 = T8.own_modules(root)
    _O.update(W93=W93, W89=W89, col=T8.L_column(files), cache=cache)
    Path(cache).mkdir(parents=True, exist_ok=True)
    pts = points_of(rows)
    tasks = [(pi, pts[pi][0], pts[pi][1]) for pi in sorted(pts)]
    status = {}
    gc.freeze()
    with mpr.Pool(workers) as P:
        for pi, how in P.imap_unordered(apex_job, tasks):
            status[pi] = how
            print("apex", pi, how, flush=True)
    gc.unfreeze()
    own = []
    for pi in sorted(pts):
        own += json.loads((Path(cache) / ("apex_%03d.json" % pi)).read_text(encoding="utf-8"))
    _O["own"] = own
    return {"rows": len(own), "apexes read from the cache (a resumed run)": sorted(p for p, h in status.items()
                                                                                  if h == "cache"),
            "apexes computed in this launch": len([p for p, h in status.items() if h == "computed"])}


# ============================================================================================ K2, K3
def part_K2(rows):
    own = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in _O["own"]}
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    over, missing = [], 0
    for r in rows:
        key = (r["line"], r["Re_tau"], r["Im_tau"])
        if key not in own:
            missing += 1
            continue
        dev = T8.compare_point(own[key], r)
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        if (max(dev[f] for f in ("up", "down", "lep", "ckm")) >= TOL["own_log"] or dev["J_rel"] >= TOL["own_J_rel"]
                or dev["zero_pattern_mismatches"]):
            over.append([r["line"], r["Re_tau"], r["Im_tau"], dev])
    return {"compared": len(rows) - missing, "missing": missing, "worst": worst, "rows over tolerance": len(over),
            "first rows over tolerance": over[:20]}


def carriers(rows, files):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    L = own_lines60()
    pp = W63.per_point_line(rows, L, t6, sg)
    per_line = {}
    for (k, x, y), v in pp.items():
        per_line[k] = min(per_line.get(k, math.inf), v[0])
    carry = {L[k] for k, v in per_line.items() if v < BAR6}
    return pp, per_line, carry


def part_K3(files, rows):
    L = own_lines60()
    pred = predicted()
    pp_o, pl_o, c_o = carriers(_O["own"], files)
    pp_m, pl_m, c_m = carriers(rows, files)
    _O["pp"] = pp_o
    _O["per_line"] = pl_o
    others = [ln for ln in L if ln not in pred]
    out = {"carrying set, own census": sorted(int(b * 60) for _a, b in c_o),
           "carrying set, main's census by own code": sorted(int(b * 60) for _a, b in c_m),
           "the two routes agree": c_o == c_m,
           "largest per-line difference between the routes (relative)":
               max(abs(pl_o[k] - pl_m[k]) / max(pl_o[k], pl_m[k]) for k in pl_o)}
    for tag, c in (("own", c_o), ("main's census", c_m)):
        out["R_a (every predicted line carries), " + tag] = pred <= c
        out["R_b (none of the other twelve carries), " + tag] = not (c & set(others))
        out["R exact, " + tag] = c == pred
    return out


# ============================================================================================ K4, read-outs
def part_K4(root, files, rows):
    W93, W89 = T8.own_modules(root)
    W45._B.update(W93=W93, W89=W89, col=T8.L_column(files))
    pts = points_of(rows)
    x, y = pts[NAPEX // 2]
    a, b = SLOPE, Fr(1, 60)
    tasks = [((a, b), x, y), ((a, (b - a) % 1), x + 1, y), ((a, b + 1), x, y), ((a, (-b - a) % 1), 1 - x, y)]
    with mpr.Pool(4) as P:
        res = P.map(W45.b_job, tasks)
    base = res[0][1]
    return {"apex": NAPEX // 2, "tau": [x, y], "mirror image line": [str(v) for v in tasks[3][0]],
            "T-step image": T8.compare_point(res[1][1], base), "b + 1": T8.compare_point(res[2][1], base),
            "mirror image": T8.compare_point(res[3][1], base)}


def part_R(files):
    L = own_lines60()
    pred = predicted()
    pl, pp = _O["per_line"], _O["pp"]
    pairs = sorted({tuple(sorted((ln, mirror(ln)))) for ln in pred})
    rows_below = sorted(([v[0], int(L[k][1] * 60), x, y, W63.u_of(L[k], x), v[1], v[2], v[3]]
                         for (k, x, y), v in pp.items() if v[0] < BAR6), key=lambda t: t[0])
    others = [k for k, ln in enumerate(L) if ln not in pred]
    # the predicted class's specificity on own code with main's seeds (W142's direct sums, W164's per-class minima)
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    arr, lab = T8.census_arrays(_O["own"])
    cid = np.array([0 if L[x[0]] in pred else 1 for x in lab])
    order = np.argsort(cid, kind="stable")
    starts = np.r_[0, np.flatnonzero(np.diff(cid[order])) + 1]
    tmpd = Path(_O["cache"])
    npz = str(tmpd / "spec_arrays.npz")
    np.savez(npz, up=arr["up"][order], dn=arr["dn"][order], lep=arr["lep"][order], sg=sg, starts=starts)
    W64._kinit(npz, str(tmpd))
    data = W64.classmin(t6)[:, 0]
    obs = float(data[0])
    per = {}
    for s in SEEDS:
        six, _nine = T8.own_draws(s, T8.NTARGET)
        m = W64.classmin(np.array(six))
        per[s] = float(np.mean(m[0] <= obs + 1e-9))
    return {"per-line minima (k, chi2_six)": [[int(L[k][1] * 60), pl[k]] for k in sorted(pl)],
            "predicted mirror pairs (k, k', minima, relative difference)":
                [[int(p[0][1] * 60), int(p[1][1] * 60), pl[L.index(p[0])], pl[L.index(p[1])],
                  abs(pl[L.index(p[0])] - pl[L.index(p[1])]) / max(pl[L.index(p[0])], pl[L.index(p[1])])]
                 for p in pairs],
            "the twelve others, nearest approach": sorted([int(L[k][1] * 60), pl[k]] for k in others),
            "least of the twelve others": min(pl[k] for k in others),
            "rows below 16.75 (chi2, k, x, y, u, horocycle, readings, c)": rows_below,
            "specificity, the predicted class (main's seeds 4501-4540)": {
                "chi2_six_min": obs, "fraction_mean": float(np.mean(list(per.values()))),
                "fraction_max": float(np.max(list(per.values()))),
                "hits": int(round(sum(v * T8.NTARGET for v in per.values()))),
                "per_seed": {str(s): per[s] for s in SEEDS}}}


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
        if "K0" in out:
            a = out["K0"]
            c["K0"] = (all(a[p] for p in PIN) and a["census rows"] == NROWS
                       and a["census distinct (line, Re, Im)"] == NROWS and a["census distinct points"] == NAPEX
                       and a["census apex indices"] == NAPEX and a["B1749 census pin"]
                       and a["the points equal B1749's census points"])
        if "K1" in out:
            a = out["K1"]
            c["K1"] = (a["lines"] == NLINES and a["every k coprime to 6"] and a["main's rows carry the own lines"]
                       and a["every point has all twenty lines"] and a["predicted as stated"]
                       and a["predicted lines are among the twenty"] and a["predicted set closed under the mirror"])
        if "K2" in out:
            k, w = out["K2"], out["K2"]["worst"]
            c["K2"] = (k["compared"] == NROWS and k["missing"] == 0
                       and max(w[f] for f in ("up", "down", "lep", "ckm")) < TOL["own_log"]
                       and w["J_rel"] < TOL["own_J_rel"] and w["zero_pattern_mismatches"] == 0)
        if "K3" in out:
            c["K3"] = out["K3"]["the two routes agree"]
        if "K4" in out:
            k = out["K4"]
            fam = ("up", "down", "lep", "ckm")
            c["K4"] = (max(k["T-step image"][f] for f in fam) < 1e-8 and k["T-step image"]["J_rel"] < 1e-8
                       and max(k["b + 1"][f] for f in fam) < 1e-8 and k["b + 1"]["J_rel"] < 1e-8
                       and max(k["mirror image"][f] for f in fam) < 1e-8
                       and abs(k["mirror image"]["J_rel"] - 2) < 1e-8)
    except Exception:  # noqa: BLE001
        out["cells_failed"] = sanitize(traceback.format_exc()[-2000:])
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--cache", required=True, help="a directory outside the repository for each apex's rows")
    args = ap.parse_args()
    root = T8.repo_root()
    cache = str(Path(args.cache).resolve())
    if Path(cache).is_relative_to(root):
        raise SystemExit("the cache must lie outside the repository")
    _ROOT["<cache>"] = cache
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    rev = T8.resolve(root, REV)
    out = {"arc": "W165", "rule": "W165_RULE.md", "status": "one run", "rev": rev, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers,
           "cache": "outside the repository (its path is not recorded)"}
    files = {p: T8.git_bytes(root, rev, p) for p in FILES}
    rows = main_rows(files)
    guarded(out, "K0", part_K0, files, rows)
    guarded(out, "K1", part_K1, rows)
    guarded(out, "census", part_census, root, files, rows, cache, args.workers)
    if "own" in _O:
        guarded(out, "K2", part_K2, rows)
        guarded(out, "K3", part_K3, files, rows)
    guarded(out, "K4", part_K4, root, files, rows)
    if "pp" in _O:
        guarded(out, "R", part_R, files)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("cells written:", len(out["cells"]))
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
