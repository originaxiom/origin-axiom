#!/usr/bin/env python3
"""W141 (P-339): the third opinion on main's B1734, THE THREAD RULE WITH THE TWO INGREDIENTS (the rule: W141_RULE.md,
committed and pushed before this script existed). It runs once, from the repository root.

  A0  the inputs: B1734's ARTIFACT_HASHES line by line; census.json's points, uniqueness and finiteness; its sha256
  A1  main's compare.py re-run on the committed census.json in a temporary tree; comparison.json and stdout diffed
  A2  the calibration on own code (W138's), B1734's seeds 1734-1753; the best rows; B1735's covariant-free fractions
  A3  main's post hoc all-orders check (FINDINGS section 3 B) on own code, from main's allorders.json, seeds 1734-1738
  A4  labelled: the same all-orders census over all 20 seeds and four menus
  B   28 census points on this seat's own instrument (W138's): the three named rows' points and 25 by seed 339; B0 its
      controls (residues against the re-implemented bilinear; the joint law); B2 the named rows from the own values
  C   C1 B1720's lines by brute force, the Smith rule, the order-5/10 selection; C2 the apexes from the monodromies;
      C3 the duplicated (tau, line) points among the 190
  D   D1 D_frame on every order-5 row; D2 the order-10 spread

The own instrument is W138's committed code (the_third_opinion_b1726.py), imported: its calibration (own_draws,
errors, menu_best), its own_point (W93's closed-form residues x kappa, W89's kernel norms with 12 terms, the Higgs DR
from direct theta sums), its circle residues of main's bilinear written again, and its point comparison. Nothing of
main's census.py, compare.py, posthoc.py, b1656_funcs.py, the_exponents.py or qseries.py is imported.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1734.py [--workers 4]
"""
import argparse
import contextlib
import io
import json
import math
import multiprocessing as mpr
import platform
import random
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
    import the_third_opinion_b1726 as T8  # noqa: E402  (W138)

REV = "91b76e7446f9d7475a33a44bc5b809c461e154cf"   # origin/main at S199, as read for the rule
ARC = "frontier/B1734_the_thread_rule_with_the_two_ingredients"
VER = ARC + "/verification"
B1720 = "frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"
B1735 = "frontier/B1735_the_precision_bar_on_the_two_ingredient_censuses/verification/check.json"
HZ, CKM, COLUMN = T8.HZ, T8.CKM, T8.COLUMN
FILES = (VER + "/compare.py", VER + "/census.py", VER + "/posthoc.py", VER + "/census.json", VER + "/comparison.json",
         VER + "/control.json", VER + "/posthoc.json", VER + "/allorders.json", VER + "/compare_run.txt",
         ARC + "/ARTIFACT_HASHES.txt", B1720, B1735, HZ, CKM, COLUMN)
OUT = HERE / "third_opinion_b1734.json"
SEEDS = tuple(range(1734, 1754))
SEEDS_POSTHOC = tuple(range(1734, 1739))
MAIN_MENUS = ("seat", "cov", "free")
SAMPLE_SEED, SAMPLE_N = 339, 25
COV_NINE_FINDINGS = 2.535
TOL = T8.TOL
RD, HORO, SECTS, UNITS = T8.RD, T8.HORO, T8.SECTS, T8.UNITS
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ============================================================================================ files
def fetch(root):
    return {p: T8.git_bytes(root, REV, p) for p in FILES}


def artifact_hashes(root, text):
    out = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        h, rel = line.split()
        path = rel if rel.startswith("frontier/") else f"{ARC}/{rel}"
        try:
            out.append({"path": path, "in_tree": True, "match": T8.sha256(T8.git_bytes(root, REV, path)) == h})
        except subprocess.CalledProcessError:
            out.append({"path": path, "in_tree": False, "match": None})
    return out


def part_A0(root, files, rows):
    ah = artifact_hashes(root, files[ARC + "/ARTIFACT_HASHES.txt"].decode("utf-8"))
    uniq = len({(r["cls"], r["line"]) for r in rows})
    return {"artifact_hashes": ah, "artifact_hashes_all_match": all(x["match"] for x in ah),
            "census_points": len(rows), "census_unique_points": uniq,
            "census_nonfinite_values": T8.nonfinite_count(rows),
            "census_json_sha256": T8.sha256(files[VER + "/census.json"]),
            "allorders_json_sha256": T8.sha256(files[VER + "/allorders.json"])}


# ============================================================================================ A1: the re-run
def build_tree(tmp, files):
    (tmp / "GENESIS.md").write_text("root marker for the P-339 re-run (not main's GENESIS)\n", encoding="utf-8")
    for p in (VER + "/compare.py", VER + "/census.json", VER + "/control.json", HZ, CKM):
        q = tmp / p
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_bytes(files[p])
    return tmp / VER


def part_A1(files, workers):
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp>"] = td
        vdir = build_tree(Path(td), files)
        run = T8.run_compare(vdir, workers)
        new = json.loads((vdir / "comparison.json").read_text(encoding="utf-8")) if run["returncode"] == 0 else None
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    out = {"returncode": run["returncode"], "seconds": run["seconds"], "stderr_tail": sanitize(run["stderr_tail"]),
           "stdout_equals_compare_run_txt": run["stdout"].strip() == files[VER + "/compare_run.txt"].decode().strip()}
    if new is not None:
        d = T8.deep_diff(old, new)
        d["mismatches"] = [[("bool:" + x) if x in ("True", "False") else x for x in m]
                           for m in d["mismatches"][:40]]
        out.update(diff=d, fractions_exact=T8.fractions_exact(old, new), cells_equal=old["cells"] == new["cells"])
    return out


# ============================================================================================ A2: own calibration
def census_arrays(rows):
    """compare.py's order: rows by (class, line), two per point (the horocycles)"""
    rows = sorted(rows, key=lambda r: (r["cls"], r["line"]))
    up, dn, lep, K, J, lab = [], [], [], [], [], []
    for r in rows:
        for h in HORO:
            up.append([T8.floor_log(r[f"up|{h}|{a}"]) for a in RD])
            dn.append([T8.floor_log(r[f"down|{h}|{a}"]) for a in RD])
            lep.append([T8.floor_log(r[f"lep|{h}|{a}"]) for a in RD])
            K.append([[T8.floor_log(r[f"ckm|{h}|{a}|{b}"][:3]) for b in RD] for a in RD])
            J.append([[r[f"ckm|{h}|{a}|{b}"][3] for b in RD] for a in RD])
            lab.append((r["word"], r["a"] + "," + r["b"], r["order"], h))
    return {"up": np.array(up), "dn": np.array(dn), "lep": np.array(lep), "K": np.array(K), "J": np.array(J)}, lab


def describe(T, menu, lab):
    w, i, ((a, b, l), c) = T8.menu_best(T8.errors(T), menu)
    six = np.concatenate([T8._ARR["up"][i, a], T8._ARR["dn"][i, b], T8._ARR["lep"][i, l]])
    cc = math.exp(((T[4] - six[4]) - (T[5] - six[5])) / 2) if c == "free" else float(c)
    six = six + np.array([0, 0, 0, 0, math.log(cc), -math.log(cc)])
    return {"best_factor": math.exp(w), "thread": lab[i][0], "line": lab[i][1], "order": lab[i][2],
            "horocycle": lab[i][3], "readings": [RD[a], RD[b], RD[l]], "lepton_factor": cc,
            "D": math.exp(six[4] + six[3] - six[2] - six[5]), "J": float(T8._ARR["J"][i, a, b])}


def part_A2(files, rows, workers, npz_dir):
    arr, lab = census_arrays(rows)
    t6, t9 = T8.targets(files)
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    b1735 = json.loads(files[B1735].decode("utf-8"))["B1734"]["covfree_six"]
    npz = str(Path(npz_dir) / "b1734.npz")
    np.savez(npz, T6=t6, T9=t9, **arr)
    T8._init_worker(npz)
    best = {name: {m: describe(T, m, lab) for m in T8.MENUS} for name, T in (("best_six", t6), ("best_nine", t9))}
    with mpr.Pool(workers, initializer=T8._init_worker, initargs=(npz,)) as P:
        per = dict(P.map(T8.seed_job, SEEDS))
    keys = sorted(per[SEEDS[0]])
    mean = {k: float(np.mean([per[s][k] for s in SEEDS])) for k in keys}
    same = all(per[s][k] == old["fraction_as_good_per_seed"][str(s)][k]
               for s in SEEDS for k in old["fraction_as_good_per_seed"][str(s)])
    covfree_same = all(per[s]["six|cov_free"] == b1735["per_seed"][str(s)] for s in SEEDS)
    dev = {}
    for name in best:
        for m in MAIN_MENUS:
            o, n = old[name][m], best[name][m]
            dev[f"{name}|{m}"] = {
                "same_row_and_configuration": all(o[k] == n[k] for k in ("thread", "line", "order", "horocycle",
                                                                          "readings")),
                "best_factor_rel": abs(o["best_factor"] - n["best_factor"]) / o["best_factor"],
                "lepton_factor_rel": abs(o["lepton_factor"] - n["lepton_factor"]) / o["lepton_factor"],
                "D_rel": abs(o["D"] - n["D"]) / abs(o["D"])}
    return {"per_seed": {str(s): per[s] for s in SEEDS}, "mean": mean, "per_seed_equals_main": same,
            "best": best, "best_against_main": dev, "cov_free_per_seed_equals_B1735": covfree_same,
            "cov_free_mean": mean["six|cov_free"], "B1735_mean": b1735["mean"]}


# ============================================================================================ A3, A4: all orders
def allorders_job(seed):
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    E0 = T8.errors(T8._ARR["T6"])
    obs = {m: T8.menu_best(E0, m)[0] for m in T8.MENUS}
    hits = dict.fromkeys(T8.MENUS, 0)
    for t in six:
        Et = T8.errors(t)
        for m in T8.MENUS:
            hits[m] += T8.menu_best(Et, m)[0] <= obs[m] + 1e-12
    return seed, {m: hits[m] / len(six) for m in T8.MENUS}, {m: math.exp(obs[m]) for m in T8.MENUS}


def part_A34(files, workers, npz_dir):
    d = json.loads(files[VER + "/allorders.json"].decode("utf-8"))
    ph = json.loads(files[VER + "/posthoc.json"].decode("utf-8"))["B_full_thread_rule_all_orders"]
    rows = d["rows"]
    up, dn, lep = [], [], []
    for r in rows:
        for h in HORO:
            up.append([T8.floor_log(r[f"up|{h}|{a}"]) for a in RD])
            dn.append([T8.floor_log(r[f"down|{h}|{a}"]) for a in RD])
            lep.append([T8.floor_log(r[f"lep|{h}|{a}"]) for a in RD])
    t6, _t9 = T8.targets(files)
    npz = str(Path(npz_dir) / "allorders.npz")
    np.savez(npz, T6=t6, up=np.array(up), dn=np.array(dn), lep=np.array(lep))
    with mpr.Pool(workers, initializer=T8._init_worker, initargs=(npz,)) as P:
        res = P.map(allorders_job, SEEDS)
    per = {s: f for s, f, _ in res}
    best = res[0][2]
    a3 = {}
    for m in ("seat", "cov"):
        mine = [per[s][m] for s in SEEDS_POSTHOC]
        a3[m] = {"per_seed": mine, "per_seed_main": ph[m]["per_seed"], "equal": mine == ph[m]["per_seed"],
                 "mean": float(np.mean(mine)), "best_six": best[m],
                 "best_six_rel": abs(best[m] - ph[m]["best_six"]) / ph[m]["best_six"]}
    a4 = {m: {"mean_20_seeds": float(np.mean([per[s][m] for s in SEEDS])),
              "seeds_above_1pct": sum(per[s][m] > 0.01 for s in SEEDS), "best_six": best[m]} for m in T8.MENUS}
    return {"points": d["points"], "rows": 2 * len(rows), "A3": a3, "A4_labelled": a4,
            "per_seed": {str(s): per[s] for s in SEEDS}}


# ============================================================================================ B: own rows
_B = {}


def b_job(task):
    tag, r = task
    own, diag = T8.own_point(_B["W93"], _B["W89"], _B["col"], (Fr(r["a"]), Fr(r["b"])), r["Re_tau"], r["Im_tau"])
    return tag, r["cls"], r["line"], own, diag


def sample(rows, old):
    rows = sorted(rows, key=lambda r: (r["cls"], r["line"]))
    named = {}
    for tag, b in (("best_six", old["best_six"]["seat"]), ("best_nine_seat", old["best_nine"]["seat"]),
                   ("best_nine_cov", old["best_nine"]["cov"])):
        named[tag] = next(i for i, r in enumerate(rows)
                          if r["word"] == b["thread"] and r["a"] + "," + r["b"] == b["line"])
    rest = [i for i in range(len(rows)) if i not in named.values()]
    chosen = sorted(random.Random(SAMPLE_SEED).sample(rest, SAMPLE_N))
    return rows, [(t, rows[i]) for t, i in named.items()] + [("seed339", rows[i]) for i in chosen]


def named_check(own, b, T, menu_kind):
    h, (ru, rdn, rl), c = b["horocycle"], b["readings"], b["lepton_factor"]
    six = np.log(np.array(own[f"up|{h}|{ru}"] + own[f"down|{h}|{rdn}"] + own[f"lep|{h}|{rl}"]))
    six[4] += math.log(c)
    six[5] -= math.log(c)
    err = np.abs(six - T[:6])
    if menu_kind == "nine":
        err = np.concatenate([err, np.abs(np.log(np.array(own[f"ckm|{h}|{ru}|{rdn}"][:3])) - T[6:9])])
    f = math.exp(err.max())
    return {"best_factor_own": f, "best_factor_main": b["best_factor"],
            "best_factor_rel": abs(f - b["best_factor"]) / b["best_factor"],
            "D_own": math.exp(six[4] + six[3] - six[2] - six[5]), "D_main": b["D"],
            "J_own": own[f"ckm|{h}|{ru}|{rdn}"][3], "J_main": b["J"]}


def part_B(root, files, rows, workers):
    W93, W89 = T8.own_modules(root)
    col = T8.L_column(files)
    _B.update(W93=W93, W89=W89, col=col)
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    t6, t9 = T8.targets(files)
    rows, tasks = sample(rows, old)
    t0 = time.time()
    with mpr.Pool(workers) as P:
        res = P.map(b_job, tasks, chunksize=1)
    stored = {(r["cls"], r["line"]): r for r in rows}
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    diag_all = {"joint_law_max": 0.0, "sv_gap_min": math.inf, "near_R": 0, "near_weight": 0}
    pts, own_by_tag = [], {}
    for tag, cls, line, own, diag in res:
        dev = T8.compare_point(own, stored[(cls, line)])
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        diag_all["joint_law_max"] = max(diag_all["joint_law_max"], diag["joint_law_max"])
        diag_all["sv_gap_min"] = min(diag_all["sv_gap_min"], diag["sv_gap_min"])
        diag_all["near_R"] += len(diag["near_R"])
        diag_all["near_weight"] += len(diag["near_weight"])
        r = stored[(cls, line)]
        pts.append({"tag": tag, "word": r["word"], "line": [r["a"], r["b"]], "order": r["order"],
                    "tau": [r["Re_tau"], r["Im_tau"]], "deviation": dev})
        if tag != "seed339":
            own_by_tag[tag] = own
    named = {"best_six": named_check(own_by_tag["best_six"], old["best_six"]["seat"], t6, "six"),
             "best_nine_seat": named_check(own_by_tag["best_nine_seat"], old["best_nine"]["seat"], t9, "nine"),
             "best_nine_cov": named_check(own_by_tag["best_nine_cov"], old["best_nine"]["cov"], t9, "nine")}
    named["best_nine_cov"]["against_FINDINGS_2.535_rel"] = abs(named["best_nine_cov"]["best_factor_own"]
                                                               - COV_NINE_FINDINGS) / COV_NINE_FINDINGS
    rc = 0.0
    for tag in ("best_six", "best_nine_seat", "best_nine_cov"):
        r = next(x for t, x in tasks if t == tag)
        a, b, tau = Fr(r["a"]), Fr(r["b"]), complex(r["Re_tau"], r["Im_tau"])
        for sec in SECTS:
            mine = T8.own_residues(W93, sec, a, b, tau)
            ref = T8.circle_residues(W93, sec, a, b, tau)
            scale = max(abs(v) for v in ref.values())
            rc = max(rc, max(abs(mine[s] - ref[s]) for s in UNITS) / scale)
    return {"points": pts, "worst": worst, "diagnostics": diag_all, "named": named, "residue_control_rel": rc,
            "seconds": round(time.time() - t0, 1)}


# ============================================================================================ C: lines and points
def fixed_lines(A):
    """the nontrivial lines v in (Q/Z)^2 with v A = +-v (row vectors), up to sign, by brute force"""
    a, b, c, d = A
    pts = set()
    for s in (1, -1):
        m = ((a - s, b), (c, d - s))
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        adj = ((m[1][1], -m[0][1]), (-m[1][0], m[0][0]))
        n = abs(det)
        for w0 in range(n):
            for w1 in range(n):
                v = (Fr(w0 * adj[0][0] + w1 * adj[1][0], det) % 1, Fr(w0 * adj[0][1] + w1 * adj[1][1], det) % 1)
                assert (v[0] * (a - s) + v[1] * c) % 1 == 0 and (v[0] * b + v[1] * (d - s)) % 1 == 0
                pts.add(v)
    pts.discard((Fr(0), Fr(0)))
    return {canon(v) for v in pts}, pts


def canon(v):
    return min(v, ((-v[0]) % 1, (-v[1]) % 1))


def lorder(v):
    return math.lcm(v[0].denominator, v[1].denominator)


def smith_d2(A, s):
    a, b, c, d = A
    m = (a - s, b, c, d - s)
    det = abs(m[0] * m[3] - m[1] * m[2])
    d1 = math.gcd(math.gcd(m[0], m[1]), math.gcd(m[2], m[3]))
    return det // d1


def part_C(files, rows):
    d = json.loads(files[B1720].decode("utf-8"))
    cls = d["classes"]
    mism_lines, smith_mism, apex_worst, col_match = [], 0, 0.0, 0
    sel = set()
    for ci, c in enumerate(cls):
        A = tuple(c["A"])
        mine, allpts = fixed_lines(A)
        stored = {canon((Fr(x) % 1, Fr(y) % 1)) for x, y in c["lines"]}
        if mine != stored:
            mism_lines.append([ci, c["word"], len(mine), len(stored)])
        col_match += fixed_lines((A[0], A[2], A[1], A[3]))[0] == stored  # read-out: the column convention
        orders_fixed = {lorder(v) for v in allpts} | {1}
        dp, dm = smith_d2(A, 1), smith_d2(A, -1)
        for N in range(1, 31):
            # a line of exact order N is fixed iff N divides the exponent of coker(A - I) or of coker(A + I)
            brute = N in orders_fixed
            smith = dp % N == 0 or dm % N == 0
            smith_mism += brute != smith
        a, b, cc, dd = A
        t = a + dd
        if cc != 0:
            ctr, rad = (a - dd) / (2 * cc), math.sqrt(t * t - 4) / (2 * abs(cc))
            apex_worst = max(apex_worst, abs(ctr - c["tau"][0]), abs(rad - c["tau"][1]))
        else:
            apex_worst = math.inf
        for v in stored:
            if lorder(v) in (5, 10):
                sel.add((ci, v))
    sel_classes = {ci for ci, _ in sel}
    pairs_ok = all(canon(((2 * v[0]) % 1, (2 * v[1]) % 1)) in {w for cj, w in sel if cj == ci}
                   for ci, v in sel if lorder(v) == 5)
    census = {(r["cls"], canon((Fr(r["a"]), Fr(r["b"])))) for r in rows}
    groups = {}
    for r in rows:
        groups.setdefault((r["Re_tau"], r["Im_tau"], r["a"], r["b"]), set()).add(r["word"])
    shared = sorted([sorted(ws) for ws in groups.values() if len(ws) > 1])
    return {"classes": len(cls), "line_set_mismatches": mism_lines, "smith_mismatches_N_le_30": smith_mism,
            "read-out: classes whose stored lines equal the column convention's": col_match,
            "apex_worst_abs": apex_worst, "selected_classes": len(sel_classes), "selected_points": len(sel),
            "selected_order5": sum(1 for _, v in sel if lorder(v) == 5),
            "selected_order10": sum(1 for _, v in sel if lorder(v) == 10),
            "order5_pairs_complete": bool(pairs_ok), "selection_equals_census": sel == census,
            "C3_distinct_points": len(groups), "C3_shared_point_groups": len(shared), "C3_shared": shared}


# ============================================================================================ D: D_frame
def part_D(rows, old):
    out = {}
    for r_name in RD:
        st = {"values": 0, "masked": 0, "max_abs_log_D": 0.0}
        ten = []
        for r in rows:
            for h in HORO:
                lep, dn = r[f"lep|{h}|{r_name}"], r[f"down|{h}|{r_name}"]
                if min(lep + dn) <= TOL["zero"]:
                    if r["order"] == 5:
                        st["masked"] += 1
                    continue
                D = lep[0] * dn[1] / (dn[0] * lep[1])
                if r["order"] == 5:
                    st["values"] += 1
                    st["max_abs_log_D"] = max(st["max_abs_log_D"], abs(math.log(D)))
                else:
                    ten.append(D)
        out[r_name] = {"order5": st, "order10_spread": {"n": len(ten), "min": min(ten), "median": float(np.median(ten)),
                                                         "max": max(ten)}}
    b = old["best_six"]["seat"]
    out["best_six_row"] = {"D": b["D"], "c": b["lepton_factor"], "D_frame": b["D"] / b["lepton_factor"] ** 2,
                           "order": b["order"]}
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
    if "A0" in out:
        a = out["A0"]
        c["A0"] = (a["artifact_hashes_all_match"] and a["census_points"] == 190 and a["census_unique_points"] == 190
                   and a["census_nonfinite_values"] == 0)
    if "A1" in out and "diff" in out["A1"]:
        a = out["A1"]
        c["A1"] = (a["returncode"] == 0 and a["fractions_exact"] and a["cells_equal"] and not a["diff"]["mismatches"]
                   and a["stdout_equals_compare_run_txt"])
    if "A2" in out:
        a = out["A2"]
        c["A2"] = (a["per_seed_equals_main"] and a["cov_free_per_seed_equals_B1735"]
                   and all(v["same_row_and_configuration"] and v["best_factor_rel"] < 1e-12
                           for v in a["best_against_main"].values()))
    if "A34" in out:
        a = out["A34"]
        c["A3"] = all(v["equal"] and v["best_six_rel"] < 1e-12 for v in a["A3"].values())
        c["A4"] = a["A4_labelled"]["seat"]["mean_20_seeds"] > 0.01
    if "B" in out:
        b = out["B"]
        w, n = b["worst"], b["named"]
        c["B0"] = b["residue_control_rel"] < TOL["residue_rel"] and b["diagnostics"]["joint_law_max"] < TOL["joint_law"]
        c["B1"] = (max(w["up"], w["down"], w["lep"], w["ckm"]) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                   and w["zero_pattern_mismatches"] == 0)
        c["B2"] = (n["best_six"]["best_factor_rel"] < 1e-6 and abs(n["best_six"]["D_own"] - 9) / 9 < 1e-6
                   and n["best_nine_seat"]["best_factor_rel"] < 1e-6 and abs(n["best_nine_seat"]["J_own"]) < 1e-10
                   and abs(n["best_nine_seat"]["J_main"]) < 1e-10
                   and n["best_nine_cov"]["against_FINDINGS_2.535_rel"] < 1e-3)
    if "C" in out:
        k = out["C"]
        c["C1"] = (k["classes"] == 121 and not k["line_set_mismatches"] and k["smith_mismatches_N_le_30"] == 0
                   and k["selected_classes"] == 49 and k["selected_points"] == 190 and k["selected_order5"] == 98
                   and k["selected_order10"] == 92 and k["order5_pairs_complete"] and k["selection_equals_census"])
        c["C2"] = k["apex_worst_abs"] < 1e-12
    if "D" in out:
        c["D1"] = all(out["D"][r]["order5"]["max_abs_log_D"] <= 1e-8 and out["D"][r]["order5"]["values"] > 0
                      and out["D"][r]["order5"]["values"] + out["D"][r]["order5"]["masked"] == 196 for r in RD)
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W141", "rule": "W141_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers,
           "tolerances": TOL}
    files = fetch(root)
    rows = json.loads(files[VER + "/census.json"].decode("utf-8"))["rows"]
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    guarded(out, "A0", part_A0, root, files, rows)
    guarded(out, "A1", part_A1, files, args.workers)
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp2>"] = td
        guarded(out, "A2", part_A2, files, rows, args.workers, td)
        guarded(out, "A34", part_A34, files, args.workers, td)
    guarded(out, "C", part_C, files, rows)
    guarded(out, "D", part_D, rows, old)
    guarded(out, "B", part_B, root, files, rows, args.workers)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    need = ("A1", "A2", "B1", "C1")
    out["opinion"] = {"inputs_for_banking (A1, A2, B1, C1)": [c.get(k) for k in need],
                      "replicated READING, bankable as that and no more": all(c.get(k) for k in need)}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", ", ".join(failed), file=sys.stderr)


if __name__ == "__main__":
    main()
