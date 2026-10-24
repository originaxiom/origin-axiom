#!/usr/bin/env python3
"""W157 — the third opinion on main's B1753, the six on the five-ality lines (the rule: W157_RULE.md, committed and
pushed before this script).  It runs once, from the repository root.

W156's script (the_third_opinion_b1749.py) is loaded unchanged, with W145's under it, and W145's module is re-pointed
to B1753's arc, its fresh seeds and its census, as B1753's compare.py does with B1741's: its A0, A1 and A2 parts, its
own instrument through b_job, and its sensitivity job.  W156's apex code is reused.  New here, on own code: the apexes
of length 13 and their freshness against lengths 2 to 12 (A3, A3f), the 48 lines (A4), the named rows (B), the rows
below the bar (C1), the line classes under B1724's T-law (C2), the restriction priced on B1749's census (C3) and the
sensitivity on B1753's seeds (D1).  Main's code is run only in A1, in a temporary tree.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1753.py [--workers 4]
"""
import argparse
import contextlib
import io
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
    import the_third_opinion_b1749 as W56    # noqa: E402  (W156, which loads W145's module)
W45, T8, T42, W140 = W56.W45, W56.T8, W56.T42, W56.W140

REV = "0c9d60a5fb960809bf21e7360be8102cf95df5ed"      # origin/main as read for the rule
ARC = "frontier/B1753_the_six_on_the_five_ality_lines"
V53 = ARC + "/verification"
V49, V41, V26 = W56.V49, W56.V41, W45.V26
FILES = (V53 + "/compare.py", V53 + "/census.py", V53 + "/census.jsonl", V53 + "/control.json",
         V53 + "/comparison.json", ARC + "/ARTIFACT_HASHES.txt", V41 + "/compare.py", V41 + "/census.jsonl",
         V26 + "/census.py", V26 + "/census.jsonl", W56.B1720T, W56.B1720G, W45.HZ, W45.CKM, W45.COLUMN,
         V49 + "/census.jsonl") + W45.DEPS
PIN = {V53 + "/census.jsonl": "c7f58dced34d6858bcfed9d25e01dfe27d4f212a29dd3a4d53f49010ad410c69",
       V53 + "/comparison.json": "8074b69b69002c099f124298504ae7769deaa87093f0220ae34db4f5c3275b47",
       V53 + "/control.json": "865bb71c094b9423561a84ebf5bbf4e95590cdd54ec099bdaa435e0a722e1154"}
PIN49 = {V49 + "/census.jsonl": W56.PIN[V49 + "/census.jsonl"]}
OUT = HERE / "third_opinion_b1753.json"
SEEDS = tuple(range(1789, 1809))
SEEDS49 = W56.SEEDS
NPTS = 10704
NAPEX = 223
LN3 = math.log(3)
BAR6 = 16.75
WINDOW = (2.0, 3.6)
NINE_SEAT = 183
LINE0 = (Fr(2, 5), Fr(1, 10))
FACTORS = (1.17, 0.90, 1.15, 1.06, 1.08, 0.97)            # FINDINGS section 1: the row best by the largest factor
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
DOUBLETS = ("Q", "L", "H")
TOL = W45.TOL

# re-point W145's module to this arc (its functions read these globals)
W45.V41, W45.ARC, W45.PIN, W45.SEEDS = V53, ARC, PIN, SEEDS
_ROOT = W45._ROOT


def sanitize(text):
    return W45.sanitize(text)


def odd_tenths():
    return {Fr(k, 10) for k in (1, 3, 5, 7, 9)}


# ============================================================================================ A0, A2 wrappers
def part_A0(files):
    out = W45.part_A0(files)
    out["B1749 census pin (for C3)"] = all(T8.sha256(files[p]) == h for p, h in PIN49.items())
    return out


def part_A2(files, workers, tmp):
    out = W45.part_A2(files, workers, tmp)
    out.pop("seat minimum at FINDINGS' row", None)
    counts = {s: int(round(out["per_seed"][str(s)]["seat"] * T8.NTARGET)) for s in SEEDS}
    out["seat counts"] = {"total": sum(counts.values()), "worst seed": max(counts.values()),
                          "seeds at 0": sum(1 for v in counts.values() if v == 0)}
    out["seeds 1789 and 1808, reported apart"] = {s: out["per_seed"][str(s)] for s in (1789, 1808)}
    return out


# ============================================================================================ A3, A3f: own apexes
def part_A3(files):
    out = {}
    d = json.loads(files[W56.B1720T].decode("utf-8"))
    bad, worst_h = [], 0.0
    for c in d["classes"]:
        w = W45.expand(c["word"])
        h, pts = W56.tops(w)
        worst_h = max(worst_h, abs(h - c["tau"][1]))
        if abs(h - c["tau"][1]) > 1e-9 or min(W56.circ(c["tau"][0], x) for x in pts) > 1e-9:
            bad.append(c["word"])
    out["(i) B1720 classes"] = {"classes": len(d["classes"]), "failing": bad, "worst |height - stored|": worst_h}
    words = W56.necklaces(13)
    lag, inwin = 0.0, {}
    for w in words:
        h, pts = W56.tops(w)
        lag = max(lag, abs(h - W56.lagrange(w) / 2))
        if WINDOW[0] <= h <= WINDOW[1]:
            inwin[w] = (h, pts)
    out["(ii)"] = {"necklaces of length 13": len(words), "in the window": len(inwin),
                   "worst |height - Lagrange/2|": lag}
    rows = T8.census_rows(files[V53 + "/census.jsonl"])
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
    per = sorted({len(ws) for ws in points.values()})
    out["(iii)"] = {"distinct census points": len(points), "word-point failures": fails[:20],
                    "listed words": len(listed), "listed words equal the own window words": listed == set(inwin),
                    "words per point (distinct values)": per}
    _A3["points"] = sorted(points)
    return out


_A3 = {}


def part_A3f(files):
    pts = _A3.get("points")
    if pts is None:
        rows = T8.census_rows(files[V53 + "/census.jsonl"])
        pts = sorted({(r["Re_tau"], r["Im_tau"]) for r in rows})
    older, n_words = [], 0
    for n in range(2, 13):
        for w in W56.necklaces(n):
            n_words += 1
            h, tp = W56.tops(w)
            if WINDOW[0] - 1e-6 <= h <= WINDOW[1] + 1e-6:
                older += [(x, h, w) for x in tp]
    hits, nearest = [], (math.inf, None)
    for (re_, im_) in pts:
        for (x, h, w) in older:
            dx = min(W56.circ(re_, x), W56.circ(-re_, x))
            if abs(h - im_) < 1e-6 and dx < 1e-6:
                hits.append([re_, im_, w])
            dist = math.hypot(dx, h - im_)
            if dist < nearest[0]:
                nearest = (dist, [re_, im_, w, len(w), x, h])
    mirror = sum(1 for (re_, im_) in pts
                 if any(abs(i2 - im_) < 1e-9 and W56.circ(-re_, r2) < 1e-9 and W56.circ(re_, r2) > 1e-9
                        for r2, i2 in pts))
    return {"older primitive words (lengths 2-12)": n_words, "older top points in the window": len(older),
            "overlaps": hits, "points whose mirror is another point": mirror, "mirror pairs": mirror // 2,
            "independent (pairs + singles)": len(pts) - mirror // 2,
            "read-out: the nearest older top point (distance, [Re, Im, word, length, its Re, its Im])": list(nearest)}


# ============================================================================================ A4: the lines
def part_A4(files, a1):
    rows = T8.census_rows(files[V53 + "/census.jsonl"])
    L = T8.own_lines()
    five = {k for k, ln in enumerate(L) if T8.order(ln) % 5 == 0}
    orders = {}
    for k in five:
        orders[T8.order(L[k])] = orders.get(T8.order(L[k]), 0) + 1
    per_apex = {}
    for r in rows:
        per_apex.setdefault((r["Re_tau"], r["Im_tau"]), set()).add(r["line"])
    w140 = {ln for ln in W140.lines_up_to_sign() if T8.order(ln) % 5 == 0}
    main = [(Fr(a), Fr(b)) for a, b in a1["main_lines"]] if a1 else None
    return {"five-ality indices": len(five), "by order": {str(k): v for k, v in sorted(orders.items())},
            "every apex has exactly these lines": all(v == five for v in per_apex.values()), "apexes": len(per_apex),
            "W140's lines of order 5 and 10 equal them": w140 == {L[k] for k in five},
            "main's lines() equals own_lines in order": main == L if main is not None else None}


# ============================================================================================ B: own instrument
def seat_six(o, h, a, b, l, k):
    return np.log(np.array(o[f"up|{h}|{T8.RD[a]}"] + o[f"down|{h}|{T8.RD[b]}"] + o[f"lep|{h}|{T8.RD[l]}"])) + \
        np.array([0, 0, 0, 0, k, -k])


def best_configs(o, t6, sg):
    """over the seat's menu and both horocycles: the configuration with the least chi2_six and the one with the
    least largest factor"""
    best_c, best_f = None, None
    for h in T8.HORO:
        for (a, b, l) in T8.SEAT:
            for k in (0.0, LN3):
                six = seat_six(o, h, a, b, l, k)
                c = float((((six - t6) / sg) ** 2).sum())
                f = float(np.max(np.abs(six - t6)))
                cfg = [h, T8.RD[a], T8.RD[b], T8.RD[l], round(math.exp(k))]
                if best_c is None or c < best_c[0]:
                    best_c = (c, cfg, six)
                if best_f is None or f < best_f[0]:
                    best_f = (f, cfg, six)
    return best_c, best_f


def D_of(six):
    return math.exp(six[4] + six[3] - six[2] - six[5])


def part_B(root, files, a2):
    W93, W89 = T8.own_modules(root)
    W45._B.update(W93=W93, W89=W89, col=T8.L_column(files))
    rows = T8.census_rows(files[V53 + "/census.jsonl"])
    L = T8.own_lines()
    stored = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}
    k_half = L.index((Fr(2, 5), Fr(1, 2)))
    named = {"best six-row": (L.index(LINE0), 1 / 3, 3.0368), "its mirror": (k_half, 2 / 3, 3.0368),
             "best by the largest factor": (k_half, 0.6, 3.0397)}
    named_keys = {}
    for name, (k, x, y) in named.items():
        kk = None
        for (k2, x2, y2) in stored:
            if k2 == k and abs(x2 - x) < 5e-4 and abs(y2 - y) < 5e-4:
                kk = (k2, x2, y2)
        named_keys[name] = kk
    keys = [k for k in named_keys.values() if k is not None]
    for p in a2["top five points (seat)"]:
        for kk in stored:
            if kk[0] == p["line"] and abs(kk[1] - p["Re_tau"]) < 1e-6 and abs(kk[2] - p["Im_tau"]) < 1e-6 \
                    and kk not in keys:
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
    bc, _bf = best_configs(o_best, t6, sg)
    bc_main, _ = best_configs(stored[best], t6, sg)
    pulls, pulls_main = (bc[2] - t6) / sg, (bc_main[2] - t6) / sg
    row = {"chi2": bc[0], "configuration": bc[1], "chi2 from the stored row": bc_main[0], "pulls": pulls.tolist(),
           "D": D_of(bc[2]), "D stored": D_of(bc_main[2])}
    row["checks"] = {"chi2_rel": abs(row["chi2"] - bc_main[0]) / bc_main[0],
                     "pulls_abs": float(np.max(np.abs(pulls - pulls_main))),
                     "D_rel": abs(row["D"] - row["D stored"]) / row["D stored"]}
    fb = named_keys["best by the largest factor"]
    frow = None
    if fb is not None:
        _c, f = best_configs(own[fb], t6, sg)
        frow = {"configuration": f[1], "largest |log factor|": f[0],
                "model over measured (c/t, u/t, s/b, d/b, mu/tau, e/tau)": np.exp(f[2] - t6).tolist(),
                "D": D_of(f[2])}
    a, b = L[best[0]]
    tau = complex(best[1], best[2])
    rc = 0.0
    for sec in T8.SECTS:
        mine = T8.own_residues(W93, sec, a, b, tau)
        ref = T8.circle_residues(W93, sec, a, b, tau)
        rc = max(rc, max(abs(mine[s] - ref[s]) for s in T8.UNITS) / max(abs(v) for v in ref.values()))
    return {"named rows": {k: (list(v) if v else None) for k, v in named_keys.items()}, "points": per,
            "worst": worst, "joint_law_max": jl, "residue_control_rel": rc,
            "T-law image against the best row": t_law, "mirror image against the best row": mirror, "row": row,
            "factor-best row": frow}


# =========================================================================================== C1, C2: rows, classes
def below_rows(rows, t6, sg):
    arr, lab = T8.census_arrays(rows)
    best, arg = W56.seat_best_per_row(arr, t6, sg)
    return arr, lab, best, arg


def part_C1(files):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    rows = T8.census_rows(files[V53 + "/census.jsonl"])
    _arr, lab, best, arg = below_rows(rows, t6, sg)
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
    _C["53"] = (lab, best)
    return out


_C = {}


def key_of(a, b):
    return min((a % 1, b % 1), ((-a) % 1, (-b) % 1))


def t_classes(lines):
    """the orbits of B1724's T-law (alpha, b) -> (alpha, b - alpha) on lines up to sign"""
    left, out = set(lines), []
    while left:
        start = min(left)
        orb, cur = [], start
        while True:
            orb.append(cur)
            cur = key_of(cur[0], cur[1] - cur[0])
            if cur == start:
                break
        out.append(sorted(orb))
        left -= set(orb)
    return out


def twist(q, line):
    a, b = (q * line[0]) % 1, (q * line[1]) % 1
    return min(a, 1 - a), math.lcm(a.denominator, b.denominator)


def part_C2(files):
    L = T8.own_lines()
    five = [ln for ln in L if T8.order(ln) % 5 == 0]
    cl5 = t_classes([ln for ln in five if T8.order(ln) == 5])
    cl10 = t_classes([ln for ln in five if T8.order(ln) == 10])
    cl_all = t_classes(L)
    class0 = next(c for c in cl10 if key_of(*LINE0) in c)
    target = sorted(key_of(Fr(2, 5), b) for b in odd_tenths())
    out = {"(i)": {"order 5 sizes": sorted(len(c) for c in cl5), "order 10 sizes": sorted(len(c) for c in cl10),
                   "classes among the 48": len(cl5) + len(cl10), "classes among the 266": len(cl_all)},
           "the class of (2/5, 1/10)": [[str(x) for x in ln] for ln in class0],
           "it is {(2/5, b): b odd tenths}": class0 == target}
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    lab53, best53 = _C["53"] if "53" in _C else below_rows(T8.census_rows(files[V53 + "/census.jsonl"]), t6, sg)[1:3]
    rows49 = T8.census_rows(files[V49 + "/census.jsonl"])
    arr49, lab49, best49, _arg49 = below_rows(rows49, t6, sg)
    _C["49"] = (arr49, lab49)
    cls = {ln: i for i, c in enumerate(cl_all) for ln in c}
    i0 = cls[key_of(*LINE0)]
    ii = {}
    for name, lab, best in (("B1753", lab53, best53), ("B1749", lab49, best49)):
        inside = [cls[L[lab[i][0]]] == i0 for i in range(len(best)) if best[i] < BAR6]
        per = {}
        for i in range(len(best)):
            c = cls[L[lab[i][0]]]
            per[c] = min(per.get(c, math.inf), float(best[i]))
        ranked = sorted(per.items(), key=lambda kv: kv[1])[:6]
        ii[name] = {"rows below the bar": len(inside), "all in the class": bool(inside) and all(inside),
                    "read-out (post hoc): the six least class minima": [
                        {"class": [[str(x) for x in ln] for ln in cl_all[c][:2]], "size": len(cl_all[c]),
                         "order": T8.order(cl_all[c][0]), "chi2_six_min": v} for c, v in ranked]}
    out["(ii)"] = ii

    def pattern(c):
        res = {}
        for f, q in SIXY.items():
            tw = {twist(q, ln) for ln in c}
            res[f] = [[str(t[0]), t[1]] for t in sorted(tw)]
        return res
    p0 = pattern(class0)
    ok = (all(p0[f] == [["2/5", 10 if f in DOUBLETS else 5]] for f in ("Q", "u", "e"))
          and all(p0[f] == [["1/5", 10 if f in DOUBLETS else 5]] for f in ("d", "L", "H")))
    img = sorted({key_of(3 * ln[0], 3 * ln[1]) for ln in class0})
    partner = next(c for c in cl10 if img[0] in c)
    p1 = pattern(partner)
    ok3 = (img == sorted(partner) and sorted(partner) == sorted(key_of(Fr(1, 5), b) for b in odd_tenths())
           and all(p1[f] == [["1/5", 10 if f in DOUBLETS else 5]] for f in ("Q", "u", "e"))
           and all(p1[f] == [["2/5", 10 if f in DOUBLETS else 5]] for f in ("d", "L", "H")))
    out["(iii)"] = {"the class's twists": p0, "as stated": ok,
                    "its image under 3": [[str(x) for x in ln] for ln in img],
                    "the partner's twists": p1, "the image is the class (1/5, odd/10) with the twists exchanged": ok3}
    return out


# ===================================================================================== C3: the restriction priced
def c3_job(seed):
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    T = np.array(six)
    cf = T42.configs(T42._W["arr"], "seat", T42._W["sg"])
    obs = float(T42.direct_min(cf, T42._W["T6"], T42._W["sg"])[0][0])
    return seed, obs, float(np.mean(T42.direct_min(cf, T, T42._W["sg"])[0] <= obs + 1e-9))


def part_C3(files, workers, tmp):
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    if "49" in _C:
        arr49, lab49 = _C["49"]
    else:
        arr49, lab49 = T8.census_arrays(T8.census_rows(files[V49 + "/census.jsonl"]))
    L = T8.own_lines()
    rules = {"all 266 lines": lambda n: True, "orders 5 and 10": lambda n: n % 5 == 0,
             "order 10 alone": lambda n: n == 10, "order 5 alone": lambda n: n == 5,
             "read-out: orders divisible by 2": lambda n: n % 2 == 0}
    out = {"pin": all(T8.sha256(files[p]) == h for p, h in PIN49.items())}
    for name, rule in rules.items():
        mask = np.array([rule(T8.order(L[lab[0]])) for lab in lab49])
        npz = str(Path(tmp) / ("c3_%d.npz" % len(out)))
        np.savez(npz, up=arr49["up"][mask], dn=arr49["dn"][mask], lep=arr49["lep"][mask], T6=t6, sg=sg)
        with mpr.Pool(workers, initializer=T42._init, initargs=("C3", npz, 0.10)) as P:
            res = P.map(c3_job, SEEDS49)
        fr = [r[2] for r in res]
        out[name] = {"rows": int(mask.sum()), "chi2_six_min": res[0][1],
                     "count": int(round(sum(fr) * T8.NTARGET)), "fraction_mean": float(np.mean(fr))}
    return out


# ============================================================================================ D1
def part_D1(files, workers, tmp):
    t6, _t9 = T8.targets(files)
    _rows, arr, _lab = W45.arrays(files)
    npz = str(Path(tmp) / "B1753_sens.npz")
    np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=T42.sigma(files))
    variants = {"c = 1 alone": (T42.sigma(files, 0.10), (0.0,)),
                "allowance 0.05": (T42.sigma(files, 0.05), (0.0, LN3)),
                "uniform sigma 0.10": (np.full(6, 0.10), (0.0, LN3)),
                "lepton factor over {1, ..., 5}": (T42.sigma(files, 0.10), tuple(math.log(c) for c in range(1, 6)))}

    def init():
        T42._init("B1753", npz, 0.10)
        T42._W["variants"] = variants
    init()
    tasks = [(s, v) for s in SEEDS for v in variants]
    with mpr.Pool(workers, initializer=init) as P:
        res = P.map(W45.sens_job, tasks)
    out = {}
    for name in variants:
        rr = [x for x in res if x[1] == name]
        out[name] = {"chi2_six_min": rr[0][2], "fraction_mean": float(np.mean([x[3] for x in rr])),
                     "fraction_max": float(np.max([x[3] for x in rr]))}
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
                   and a.get("diff", {"max_rel": 1})["max_rel"] < 1e-10)
    if "A2" in out:
        a = out["A2"]
        n = a["seat counts"]
        c["A2"] = (a["per_seed_equal_main"] and max(a["min_rel_vs_main"].values()) < 1e-10
                   and all(a["chi2_nine"][m]["rel_vs_main"] < 1e-6 for m in ("seat", "sm"))
                   and abs(a["mins"]["seat"]["chi2_six_min"] - 2.74) < 0.01
                   and n["total"] == 7 and n["worst seed"] == 1 and n["seeds at 0"] == 13
                   and abs(a["chi2_nine"]["seat"]["chi2_nine_min"] - NINE_SEAT) < 0.5)
    if "A3" in out:
        a = out["A3"]
        c["A3"] = (a["(i) B1720 classes"]["classes"] == 121 and not a["(i) B1720 classes"]["failing"]
                   and a["(ii)"]["necklaces of length 13"] == 630 and a["(ii)"]["in the window"] == 446
                   and a["(iii)"]["distinct census points"] == NAPEX and not a["(iii)"]["word-point failures"]
                   and a["(iii)"]["listed words equal the own window words"])
    if "A3f" in out:
        c["A3f"] = not out["A3f"]["overlaps"]
    if "A4" in out:
        a = out["A4"]
        c["A4"] = (a["five-ality indices"] == 48 and a["by order"] == {"5": 12, "10": 36}
                   and a["every apex has exactly these lines"] and a["apexes"] == NAPEX
                   and a["W140's lines of order 5 and 10 equal them"] and a["main's lines() equals own_lines in order"])
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
        f = b["factor-best row"]
        c["B2"] = (v["chi2_rel"] < 1e-3 and v["pulls_abs"] < 1e-3 and v["D_rel"] < 1e-3
                   and abs(b["row"]["chi2"] - 2.74) < 0.01 and abs(b["row"]["D"] - 10.75) < 0.01
                   and f is not None
                   and all(abs(x - y) <= 0.005 for x, y in
                           zip(f["model over measured (c/t, u/t, s/b, d/b, mu/tau, e/tau)"], FACTORS))
                   and abs(f["D"] - 10.92) < 0.01)
    if "C1" in out:
        k = out["C1"]
        c["C1"] = (k["rows below 16.75"] >= 1 and set(k["lines"]) <= {("2/5", "1/10"), ("2/5", "1/2")}
                   and k["horocycles"] == ["L_max"] and k["configurations"] == [(("St", "S", "S"), 3)]
                   and 2.90 <= k["heights"][0] and k["heights"][1] <= 3.20)
    if "C2" in out:
        k = out["C2"]
        i = k["(i)"]
        c["C2"] = (i["order 5 sizes"] == [1, 1, 5, 5] and i["order 10 sizes"] == [1, 1, 2, 2, 5, 5, 10, 10]
                   and i["classes among the 48"] == 12 and i["classes among the 266"] == 64
                   and k["it is {(2/5, b): b odd tenths}"]
                   and all(k["(ii)"][n]["all in the class"] for n in ("B1753", "B1749"))
                   and k["(iii)"]["as stated"]
                   and k["(iii)"]["the image is the class (1/5, odd/10) with the twists exchanged"])
    if "C3" in out:
        k = out["C3"]
        c["C3"] = (k["pin"] and all(abs(k[n]["chi2_six_min"] - 3.57) < 0.01
                                    for n in ("all 266 lines", "orders 5 and 10", "order 10 alone"))
                   and k["all 266 lines"]["count"] == 16 and k["orders 5 and 10"]["count"] == 2
                   and k["order 10 alone"]["count"] == 1 and abs(k["order 5 alone"]["chi2_six_min"] - 20.78) < 0.01
                   and abs(k["order 5 alone"]["fraction_mean"] - 0.0019) <= 0.0002)
    if "D1" in out:
        s = out["D1"]["c = 1 alone"]
        c["D1"] = abs(s["chi2_six_min"] / 154.2 - 1) < 0.01 and abs(s["fraction_mean"] - 0.191) <= 0.015
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W157", "rule": "W157_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers}
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    guarded(out, "A0", part_A0, files)
    guarded(out, "A1", W45.part_A1, files, args.workers)
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp2>"] = td
        guarded(out, "A2", part_A2, files, args.workers, td)
        guarded(out, "D1", part_D1, files, args.workers, td)
        guarded(out, "A3", part_A3, files)
        guarded(out, "A3f", part_A3f, files)
        guarded(out, "A4", part_A4, files, out.get("A1"))
        guarded(out, "C1", part_C1, files)
        guarded(out, "C2", part_C2, files)
        guarded(out, "C3", part_C3, files, args.workers, td)
    if "A2" in out:
        guarded(out, "B", part_B, root, files, out["A2"])
    if "A1" in out:
        out["A1"].pop("main_lines", None)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    out["opinion"] = {"agrees with main's scope (the line rule a pick in effect; ungraded, a READING)":
                      bool(all(c.get(k) for k in ("A1", "A2", "B1", "C1", "C2", "C3")))}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
