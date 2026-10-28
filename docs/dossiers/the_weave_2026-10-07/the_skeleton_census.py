#!/usr/bin/env python3
"""W174 — THE RIDDLE, item 4, the skeleton census (the rule: W174_RULE.md, committed and pushed before this script).
Does any forced exponent pattern on record, with one small parameter shared by the three sectors and coefficients within
a factor 3, carry the six?

  A  the cusp in B1656's frame (W162's point), every census line: the six at Im tau 3, 4, 5, 6 and Re tau 1/8, 3/8;
     the pattern is the local exponent at the top resolved heights (ratios below 1e-12 are not resolved)
  B  the cusp with a covariant Higgs (B1691): (1/2, 1) in every sector, with Im tau on m1/m3
  C  omega (B1691's table, W68's pairings): (p2, p1) in {(1,1), (2,3), (1,2), (2,4)} per sector, delta shared; 64
  S0 convergence; S1 no line passes; S2 B fails; S3 no omega assignment passes; S4 capacity (if anything passes)

    python3 -B docs/dossiers/the_weave_2026-10-07/the_skeleton_census.py
"""
import contextlib
import io
import itertools
import json
import math
import multiprocessing as mpc
import platform
import sys
import time
import traceback
import warnings
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_census_window as W162          # noqa: E402  (W162: the frame's point at any height, L held above 4)
T8, W58 = W162.T8, W162.W58
OUT = HERE / "the_skeleton_census.json"
LN3 = math.log(3)
FLOOR = math.log(1e-12)
HEIGHTS = (3.0, 4.0, 5.0, 6.0)
XS = (1 / 8, 3 / 8)
READ = (("up", 1), ("down", 0), ("lep", 0))     # the rows' readings (S~, S, S); T8.RD = ("S", "St")
OMEGA = ((1, 1), (2, 3), (1, 2), (2, 4))
NULL_N, NULL_W, SEED = 20000, 2.0, 1740174
CONV = 0.02
WORKERS = 4
SGRID = np.linspace(-80.0, 0.0, 160001)[:-1]
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def six_of(r):
    out = []
    for sec, i in READ:
        out += list(r[(sec, "L_max")][i])
    return np.array(out, dtype=float)


# ============================================================================================ the skeleton test
def interval(d, n, tol=LN3):
    """the s < 0 with |d_i - n_i s| <= tol for all i; (lo, hi) or None"""
    lo, hi = -math.inf, 0.0
    for di, ni in zip(d, n):
        if abs(ni) < 1e-12:
            if abs(di) > tol:
                return None
            continue
        a, b = (di - tol) / ni, (di + tol) / ni
        lo, hi = max(lo, min(a, b)), min(hi, max(a, b))
    return (lo, hi) if lo <= hi else None


def excess(d, model):
    """least over the s grid of the worst |d_i - model_i(s)|, minus ln 3, and its s; model(s) -> (len(s), 6)"""
    m = model(SGRID)
    w = np.abs(m - np.asarray(d)[None, :]).max(axis=1)
    j = int(np.argmin(w))
    return float(w[j] - LN3), float(SGRID[j])


def model_lin(n):
    n = np.asarray(n, dtype=float)
    return lambda s: s[:, None] * n[None, :]


def model_b(s):
    y = -s / (2 * math.pi)
    m2, m1 = s / 2, s + np.log(y)
    return np.stack([m2, m1, m2, m1, m2, m1], axis=1)


def passes_b(d, _mb=[]):
    if not _mb:
        _mb.append(model_b(SGRID))
    w = np.abs(_mb[0] - np.asarray(d)[None, :]).max(axis=1)
    return bool((w <= LN3).any())


def omega_patterns():
    pats = []
    for a in itertools.product(OMEGA, repeat=3):
        pats.append(([a[0][0], a[0][1], a[1][0], a[1][1], a[2][0], a[2][1]], [list(p) for p in a]))
    return pats


# ============================================================================================ the frame (menu A)
def frame_patterns(res):
    """per line and Re tau: the six per height, the pattern, its source pair, the intercepts, the convergence"""
    lines = T8.own_lines()
    per = []
    for k, (a, b) in enumerate(lines):
        entry = {"line": [str(a), str(b)], "per Re tau": []}
        for x in XS:
            fs, failed = {}, False
            for y in HEIGHTS:
                r = res[(k, x, y)]
                if "failed" in r:
                    failed = True
                    break
                fs[y] = six_of(r)
            if failed:
                entry["per Re tau"].append({"x": x, "failed": True})
                continue
            n, src, ok = [], [], True
            for i in range(6):
                pick = None
                for y1, y2 in ((5.0, 6.0), (4.0, 5.0), (3.0, 4.0)):
                    if fs[y1][i] > FLOOR and fs[y2][i] > FLOOR:
                        pick = (y1, y2)
                        break
                if pick is None:
                    ok = False
                    n.append(None)
                    src.append(None)
                    continue
                y1, y2 = pick
                n.append(float(-(fs[y2][i] - fs[y1][i]) / (2 * math.pi * (y2 - y1))))
                src.append([y1, y2])
            top_ok = all(fs[6.0][i] > FLOOR and fs[5.0][i] > FLOOR and fs[4.0][i] > FLOOR for i in range(6))
            conv = None
            if top_ok:
                e45 = -(fs[5.0] - fs[4.0]) / (2 * math.pi)
                e56 = -(fs[6.0] - fs[5.0]) / (2 * math.pi)
                conv = float(np.abs(e45 - e56).max())
            P = None
            if ok:
                P = [float(fs[s[1]][i] + 2 * math.pi * s[1] * n[i]) for i, s in enumerate(src)]
            entry["per Re tau"].append({"x": x, "six per height": {str(y): fs[y].tolist() for y in HEIGHTS},
                                        "pattern n_i": n, "from heights": src, "intercepts P_i": P,
                                        "all six resolved at 4-6": top_ok, "|e(4,5) - e(5,6)| max": conv})
        per.append(entry)
    return per


def run(root, out, pool):
    files = {p: T8.git_bytes(root, W58.REV, p) for p in W58.FILES}
    col = T8.L_column(files)
    t6, _t9 = T8.targets(files)
    d = np.array(t6, dtype=float)
    out["the six (data, read once)"] = d.tolist()
    out["R: the data's own ratios ln(m1/m3)/ln(m2/m3) (up, down, leptons)"] = [float(d[1] / d[0]), float(d[3] / d[2]),
                                                                              float(d[5] / d[4])]
    out["R: the sectors' ln(m2/m3) over the up quarks'"] = [1.0, float(d[2] / d[0]), float(d[4] / d[0])]
    # ---------------------------------------------------------------- menu A: the frame at every line
    lines = T8.own_lines()
    tasks = [(k, x, y, 1.0) for k in range(len(lines)) for x in XS for y in HEIGHTS]
    t0 = time.time()
    res = {}
    for j, r in enumerate(pool.imap(W162.point, tasks, chunksize=4)):
        res[(r["k"], r["x"], r["y"])] = r
        if j % 400 == 0:
            print(f"point {j + 1}/{len(tasks)} at {time.time() - t0:.0f} s", flush=True)
    out["menu A tasks"] = len(tasks)
    out["menu A failed tasks"] = sum(1 for r in res.values() if "failed" in r)
    out["menu A dropped channels (tasks with any)"] = sum(1 for r in res.values() if r.get("dropped", 0) > 0)
    per = frame_patterns(res)
    # S0: convergence and Re tau agreement on lines resolved at 4-6 at both Re tau
    conv_lines, conv_ok = 0, 0
    unconverged = []
    for e in per:
        pr = e["per Re tau"]
        if any(p.get("failed") or not p["all six resolved at 4-6"] for p in pr):
            continue
        conv_lines += 1
        same_x = max(abs(a - b) for a, b in zip(pr[0]["pattern n_i"], pr[1]["pattern n_i"]))
        good = max(p["|e(4,5) - e(5,6)| max"] for p in pr) <= CONV and same_x <= CONV
        conv_ok += good
        if not good:
            unconverged.append(e["line"])
    frac = conv_ok / conv_lines if conv_lines else 0.0
    out["S0"] = {"lines resolved at 4-6 at both Re tau": conv_lines, "converged and Re-tau-independent": conv_ok,
                 "fraction": frac, "unconverged lines": unconverged, "holds": bool(conv_lines > 0 and frac >= 0.9)}
    # S1: the skeleton test per line (a line passes if its pattern passes at either Re tau)
    passing, near = [], []
    for e in per:
        for p in e["per Re tau"]:
            if p.get("failed") or p["pattern n_i"] is None or any(v is None for v in p["pattern n_i"]):
                continue
            iv = interval(d, p["pattern n_i"])
            ex, s = excess(d, model_lin(p["pattern n_i"]))
            p["test interval s"] = list(iv) if iv else None
            p["least worst excess over ln 3"] = [ex, s, -s / (2 * math.pi)]
            near.append((ex, e["line"], p["x"], s))
            if iv:
                passing.append([e["line"], p["x"], list(iv), [-iv[1] / (2 * math.pi), -iv[0] / (2 * math.pi)]])
    near.sort(key=lambda v: v[0])
    out["per line"] = per
    out["S1"] = {"passing lines (line, Re tau, s interval, Im tau interval)": passing,
                 "closest ten (excess over ln 3, line, Re tau, s)": [list(v) for v in near[:10]],
                 "holds": bool(not passing)}
    # S2: B1691's covariant skeleton
    exb, sb = excess(d, model_b)
    out["S2"] = {"passes": passes_b(d), "least worst excess over ln 3": exb, "at s": sb,
                 "at Im tau": -sb / (2 * math.pi), "holds": bool(not passes_b(d))}
    # S3: omega
    om = []
    for n, a in omega_patterns():
        iv = interval(d, n)
        ex, s = excess(d, model_lin(n))
        om.append({"assignment (up, down, leptons) as (p2, p1)": a, "interval ln delta": list(iv) if iv else None,
                   "least worst excess over ln 3": ex, "at ln delta": s})
    om.sort(key=lambda v: v["least worst excess over ln 3"])
    out["S3"] = {"passing assignments": [o for o in om if o["interval ln delta"]], "closest five": om[:5],
                 "holds": bool(not any(o["interval ln delta"] for o in om))}
    # S4: the null (random sixes near the data)
    rng = np.random.default_rng(SEED)
    draws = np.empty((NULL_N, 6))
    for t in range(NULL_N):
        while True:
            z = d + rng.uniform(-NULL_W, NULL_W, 6)
            if z[1] < z[0] and z[3] < z[2] and z[5] < z[4] and (z < 0).all():
                break
        draws[t] = z
    pats_a = [p["pattern n_i"] for e in per for p in e["per Re tau"]
              if not p.get("failed") and p["pattern n_i"] is not None and all(v is not None for v in p["pattern n_i"])]
    pats_c = [n for n, _a in omega_patterns()]

    def rate(pats):
        hit = np.zeros(NULL_N, dtype=bool)
        for n in pats:
            n = np.asarray(n, dtype=float)
            lo = np.full(NULL_N, -np.inf)
            hi = np.zeros(NULL_N)
            ok = np.ones(NULL_N, dtype=bool)
            for i in range(6):
                if abs(n[i]) < 1e-12:
                    ok &= np.abs(draws[:, i]) <= LN3
                    continue
                a, b = (draws[:, i] - LN3) / n[i], (draws[:, i] + LN3) / n[i]
                lo, hi = np.maximum(lo, np.minimum(a, b)), np.minimum(hi, np.maximum(a, b))
            hit |= ok & (lo <= hi)
        return float(hit.mean())

    ra, rc = rate(pats_a), rate(pats_c)
    rb = float(np.mean([passes_b(z) for z in draws[:2000]]))
    out["R: null pass rates (A, B on the first 2000, C)"] = [ra, rb, rc]
    data_pass = {"A": bool(passing), "C": bool(out["S3"]["passing assignments"])}
    if any(data_pass.values()):
        checks = []
        if data_pass["A"]:
            checks.append(ra >= 0.05)
        if data_pass["C"]:
            checks.append(rc >= 0.05)
        out["S4"] = {"data pass": data_pass, "null rates (A, C)": [ra, rc], "holds": bool(all(checks))}
    else:
        out["S4"] = {"data pass": data_pass, "null rates (A, C)": [ra, rc], "holds": None,
                     "note": "nothing passed; read out only"}
    out["cells"] = {k: out[k]["holds"] for k in ("S0", "S1", "S2", "S3", "S4")}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W174", "rule": "W174_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
           "python": sys.version.split()[0], "numpy": np.__version__, "machine": platform.machine(),
           "workers": WORKERS}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            files = {p: T8.git_bytes(root, W58.REV, p) for p in W58.FILES}
            col = T8.L_column(files)
            with mpc.get_context("fork").Pool(WORKERS, initializer=W162._init, initargs=(str(root), col)) as pool:
                run(root, out, pool)
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("done" if "run_failed" not in out else "run failed")


if __name__ == "__main__":
    main()
