#!/usr/bin/env python3
"""W145 (P-348): the third opinion on main's B1741, TAU FROM THE THREAD RULE, THE LINE FREE (the rule: W145_RULE.md,
committed and pushed before this script existed). It runs once, from the repository root.

  A0  the inputs: census.jsonl and comparison.json against this seat's pins; every file B1741's ARTIFACT_HASHES pins
  A1  main's compare.py re-run in a temporary tree at REV; comparison.json diffed; in that tree, B1726's lines() for A4
  A2  the chi-square calibration on own code: W142's direct sums, the seat, covariant and free menus, seeds 1741-1760,
      own draws; the minimum's row; chi2_nine under the seat's menu and the Standard Model's reading
  A3  the apex points: each of B1720's 121 stored classes (det 1, its trace against its word's own L/R product), the
      apex of its stored A against its stored tau; the distinct points against census.jsonl's
  A4  the lines: W140's 266 against B1726's lines(); census.jsonl's line indices at every apex
  B   the best six-row, the next four by chi2_six (seat's menu) and the best nine-row on this seat's own instrument
      (W138's); B0 its controls and B1724's law on own code; B2 the best row's chi2, pulls and D from own values (the
      pulls against those of main's stored row)
  C1  the line: its identity, B1735's line 149, the Smith rule for both classes at the apex, A^2 mod 10
  C2  the lepton-down relation at the best six-row; a read-out over the census of the lines where they coincide
  D1  sensitivity (labelled): allowance 0.05; the lepton factor over {1, ..., 5}; a uniform sigma of 0.10

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1741.py [--workers 4]
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
    import the_third_opinion_b1726 as T8    # noqa: E402  (W138)
    import the_third_opinion_b1734 as T41   # noqa: E402  (W141)
    import the_third_opinion_b1735 as T42   # noqa: E402  (W142)
    import the_hypercharge_line as W140     # noqa: E402  (W140)

REV = "a60430b4682fe53d77d332d7749aa976fc0bf489"   # origin/main as read for the rule
ARC = "frontier/B1741_tau_from_the_thread_rule_the_line_free"
V41 = ARC + "/verification"
V26 = "frontier/B1726_the_two_ingredients_replicated/verification"
B1720T = "frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"
DEPS = ("frontier/B1723_the_golden_valley/verification/b1656_funcs.py",
        "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py",
        "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py")
HZ, CKM, COLUMN = T8.HZ, T8.CKM, T8.COLUMN
FILES = (V41 + "/compare.py", V41 + "/census.py", V41 + "/census.jsonl", V41 + "/control.json",
         V41 + "/comparison.json", ARC + "/ARTIFACT_HASHES.txt", V26 + "/census.py", V26 + "/census.jsonl", B1720T,
         HZ, CKM, COLUMN) + DEPS
PIN = {V41 + "/census.jsonl": "8fadff8b143f775418b48b9d9e8948775b642648dc4345a6d3691d5a9217388d",
       V41 + "/comparison.json": "6217857352263b9877b25f14b24d3da16fa3eef9d1521ab45cdff9c1cc3fe248"}
OUT = HERE / "third_opinion_b1741.json"
SEEDS = tuple(range(1741, 1761))
MENUS = ("seat", "cov", "free")
SEAT, COV = T8.SEAT, T8.COV
SM = ((1, 0, 0),)
LN3 = math.log(3)
BAR6, BAR9 = 16.75, 21.67
BEST = {"line": 153, "Re_tau": 3.4, "h": "L_max"}           # FINDINGS section 1 and compare_run.txt's last line
CHI2_BEST, D_BEST = 14.932, 11.047
NINE_MAIN = {"seat": 204, "sm": 1410}
TOL = T8.TOL
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def bool_safe(m):
    return [("bool:" + x) if x in ("True", "False") else x for x in m]


# ============================================================================================ A0
def part_A0(files):
    out = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    rows = T8.census_rows(files[V41 + "/census.jsonl"])
    out["census rows"] = len(rows)
    out["census distinct (line, Re, Im)"] = len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
    pinned = {}
    for ln in files[ARC + "/ARTIFACT_HASHES.txt"].decode("utf-8").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        h, p = ln.split()[0], ln.split()[1]
        path = p if p.startswith("frontier/") else ARC + "/" + p
        pinned[path] = (T8.sha256(files[path]) == h) if path in files else "not fetched"
    out["ARTIFACT_HASHES"] = pinned
    return out


# ============================================================================================ A1: the re-run
def build_tree(tmp, files):
    (tmp / "GENESIS.md").write_text("root marker for the P-348 re-run (not main's GENESIS)\n", encoding="utf-8")
    for p, b in files.items():
        q = tmp / p
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_bytes(b)
    return tmp / V41


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
        try:                                       # B1726's lines() for A4, guarded apart from the re-run
            sys.path.insert(0, str(Path(td) / V26))
            spec = importlib.util.spec_from_file_location("b1726_census_for_lines", Path(td) / V26 / "census.py")
            K = importlib.util.module_from_spec(spec)
            with contextlib.redirect_stdout(io.StringIO()):
                spec.loader.exec_module(K)
            main_lines = [(Fr(a), Fr(b)) for a, b in K.lines()]
        except Exception:  # noqa: BLE001
            out["lines_failed"] = sanitize(traceback.format_exc()[-2000:])
        finally:
            sys.path.remove(str(Path(td) / V26))
    old = json.loads(files[V41 + "/comparison.json"].decode("utf-8"))
    if new is not None:
        dd = T8.deep_diff(old, new)
        dd["mismatches"] = [bool_safe(m) for m in dd["mismatches"][:40]]
        out["diff"] = dd
        out["cells identical"] = old["cells"] == new["cells"]
        out["per-seed fractions exact"] = (old["fraction_as_good_per_seed"] == new["fraction_as_good_per_seed"]
                                           and all(old["chi2_per_seed"][s][k][1] == new["chi2_per_seed"][s][k][1]
                                                   for s in old["chi2_per_seed"] for k in old["chi2_per_seed"][s]))
    out["main_lines"] = [[str(a), str(b)] for a, b in main_lines]
    return out


# ============================================================================================ A2: own chi-square
def arrays(files):
    rows = T8.census_rows(files[V41 + "/census.jsonl"])
    arr, lab = T8.census_arrays(rows)
    return rows, arr, lab


def nine(arr, lab, T9, s9, cfg):
    best = (math.inf, None)
    for (a, b, l) in cfg:
        for k in (0.0, LN3):
            X = np.concatenate([arr["up"][:, a], arr["dn"][:, b], (arr["lep"][:, l, 0] + k)[:, None],
                                (arr["lep"][:, l, 1] - k)[:, None], arr["K"][:, a, b]], axis=1)
            c = np.zeros(X.shape[0])
            for j in range(9):
                c += ((X[:, j] - T9[j]) / s9[j]) ** 2
            i = int(np.argmin(c))
            if c[i] < best[0]:
                best = (float(c[i]), [str(x) for x in lab[i]])
    return {"chi2_nine_min": best[0], "row": best[1]}


def calib_job(seed):
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    T = np.array(six)
    out = {}
    for menu in MENUS:
        cf = T42.configs(T42._W["arr"], menu, T42._W["sg"])
        obs = float(T42.direct_min(cf, T42._W["T6"], T42._W["sg"])[0][0])
        out[menu] = (obs, float(np.mean(T42.direct_min(cf, T, T42._W["sg"])[0] <= obs + 1e-9)))
    return seed, out


def part_A2(files, workers, tmp):
    t6, t9 = T8.targets(files)
    sg = T42.sigma(files)
    s9 = np.concatenate([sg, T42.sigma_ckm(files)])
    _rows, arr, lab = arrays(files)
    npz = str(Path(tmp) / "B1741.npz")
    np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=sg)
    T42._init("B1741", npz, 0.10)
    mins = {}
    for menu in MENUS:
        m, arg = T42.direct_min(T42.configs(arr, menu, sg), t6, sg)
        (a, b, l, k), i = arg
        mins[menu] = {"chi2_six_min": float(m[0]), "row": [str(x) for x in lab[i]],
                      "readings": [T8.RD[a], T8.RD[b], T8.RD[l]], "k": k if k == "free" else float(k)}
    with mpr.Pool(workers, initializer=T42._init, initargs=("B1741", npz, 0.10)) as P:
        per = dict(P.map(calib_job, SEEDS))
    main = json.loads(files[V41 + "/comparison.json"].decode("utf-8"))
    out = {"mins": mins, "per_seed": {str(s): {m: per[s][m][1] for m in MENUS} for s in SEEDS}}
    out["per_seed_equal_main"] = all(per[s][m][1] == main["chi2_per_seed"][str(s)]["six|" + m][1]
                                     for s in SEEDS for m in MENUS)
    out["min_rel_vs_main"] = {m: abs(mins[m]["chi2_six_min"] - main["chi2"]["six|" + m]["min"])
                              / main["chi2"]["six|" + m]["min"] for m in MENUS}
    out["mean"] = {m: float(np.mean([per[s][m][1] for s in SEEDS])) for m in MENUS}
    out["worst_seed"] = {m: float(np.max([per[s][m][1] for s in SEEDS])) for m in MENUS}
    br = mins["seat"]["row"]
    out["seat minimum at FINDINGS' row"] = (br[0] == str(BEST["line"]) and abs(float(br[1]) - BEST["Re_tau"]) < 1e-9
                                            and br[3] == BEST["h"] and mins["seat"]["readings"] == ["St", "S", "S"]
                                            and abs(mins["seat"]["k"] - LN3) < 1e-12)
    n9 = {"seat": nine(arr, lab, t9, s9, SEAT), "sm": nine(arr, lab, t9, s9, SM)}
    for m in n9:
        ref = main["chi2"]["nine|" + m]["min"]
        n9[m]["main"] = ref
        n9[m]["rel_vs_main"] = abs(n9[m]["chi2_nine_min"] - ref) / ref
    out["chi2_nine"] = n9
    # the rows ranked by chi2_six under the seat's menu, for B
    best_by_row = np.full(arr["up"].shape[0], np.inf)
    for key, X, kind in T42.configs(arr, "seat", sg):
        t = T42.tmap(t6, kind, sg)[0]
        best_by_row = np.minimum(best_by_row, ((X - t[None, :]) ** 2).sum(1))
    order = np.argsort(best_by_row)
    pts, seen = [], set()
    for i in order:
        key = lab[i][:3]
        if key not in seen:
            seen.add(key)
            pts.append({"line": int(lab[i][0]), "Re_tau": float(lab[i][1]), "Im_tau": float(lab[i][2]),
                        "chi2_six": float(best_by_row[i])})
        if len(pts) == 5:
            break
    out["top five points (seat)"] = pts
    return out


# ============================================================================================ A3, A4
def word_matrix(word):
    m = ((1, 0), (0, 1))
    for ch in word:
        x = W140.LM if ch == "L" else W140.RM
        m = ((m[0][0] * x[0][0] + m[0][1] * x[1][0], m[0][0] * x[0][1] + m[0][1] * x[1][1]),
             (m[1][0] * x[0][0] + m[1][1] * x[1][0], m[1][0] * x[0][1] + m[1][1] * x[1][1]))
    return m


def expand(word):
    """B1720's words may carry exponents (L5R2LR); expand to letters"""
    out, i = "", 0
    while i < len(word):
        ch = word[i]
        j = i + 1
        while j < len(word) and word[j].isdigit():
            j += 1
        out += ch * (int(word[i + 1:j]) if j > i + 1 else 1)
        i = j
    return out


def part_A3(files):
    d = json.loads(files[B1720T].decode("utf-8"))
    rows = T8.census_rows(files[V41 + "/census.jsonl"])
    bad, trans, pts = [], {}, {}
    for c in d["classes"]:
        a, b, cc, dd = c["A"]
        wm = word_matrix(expand(c["word"]))
        tr_word = wm[0][0] + wm[1][1]
        t = a + dd
        re_ = (a - dd) / (2 * cc)
        im_ = math.sqrt(t * t - 4) / (2 * abs(cc))
        shift = round(c["tau"][0] - re_)
        ok = (a * dd - b * cc == 1 and abs(tr_word) == abs(t) and abs(im_ - c["tau"][1]) < 1e-9
              and abs(re_ + shift - c["tau"][0]) < 1e-9)
        if not ok:
            bad.append(c["word"])
        trans[str(shift)] = trans.get(str(shift), 0) + 1
        pts.setdefault((round(c["tau"][0], 9), round(c["tau"][1], 9)), []).append(c["word"])
    census_pts = {(round(r["Re_tau"], 9), round(r["Im_tau"], 6)) for r in rows}
    mine = {(k[0], round(k[1], 6)) for k in pts}
    return {"classes": len(d["classes"]), "classes failing": bad, "integer translates in Re tau": trans,
            "distinct apex points": len(pts), "equal census.jsonl's points": mine == census_pts,
            "census points": len(census_pts)}


def part_A4(files, a1):
    rows = T8.census_rows(files[V41 + "/census.jsonl"])
    mine = set(W140.lines_up_to_sign())
    main = {(Fr(a), Fr(b)) for a, b in a1["main_lines"]} if a1 else set()
    per_apex = {}
    for r in rows:
        per_apex.setdefault((r["Re_tau"], r["Im_tau"]), set()).add(r["line"])
    own_order = T8.own_lines()
    return {"W140 lines": len(mine), "main lines()": len(main), "equal as sets": mine == main,
            "W138's own_lines equal main's list in order": [(Fr(a), Fr(b)) for a, b in a1["main_lines"]] == own_order
            if a1 else None,
            "every apex has lines 0-265": all(v == set(range(266)) for v in per_apex.values()),
            "apexes": len(per_apex)}


# ============================================================================================ B
_B = {}


def b_job(task):
    line, re_t, im_t = task
    own, diag = T8.own_point(_B["W93"], _B["W89"], _B["col"], line, re_t, im_t)
    return task, own, diag


def part_B(root, files, a2):
    W93, W89 = T8.own_modules(root)
    _B.update(W93=W93, W89=W89, col=T8.L_column(files))
    rows = T8.census_rows(files[V41 + "/census.jsonl"])
    L = T8.own_lines()
    stored = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}
    pts = [(p["line"], p["Re_tau"], p["Im_tau"]) for p in a2["top five points (seat)"]]
    nr = a2["chi2_nine"]["seat"]["row"]
    pts.append((int(nr[0]), float(nr[1]), float(nr[2])))
    best = pts[0]
    im_b = best[2]
    tasks = [(L[k], re_t, im_t) for k, re_t, im_t in pts]
    tasks.append(((Fr(2, 5), Fr(1, 10)), 0.4, im_b))                     # B1724's law: the census frame
    with mpr.Pool(4) as P:
        res = P.map(b_job, tasks)
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    jl, per, own_best = 0.0, [], None
    own_frame = res[-1][1]                                               # the last task: the census frame
    for (line, re_t, im_t), own, diag in res[:-1]:
        k = L.index(line)
        dev = T8.compare_point(own, stored[(k, re_t, im_t)])
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        jl = max(jl, diag["joint_law_max"])
        per.append({"line": k, "tau": [re_t, im_t], "deviation": dev})
        if (k, re_t, im_t) == best:
            own_best = own
    tlaw = T8.compare_point(own_frame, own_best)
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)

    def six_of(r):
        s = np.log(np.array(r["up|L_max|St"] + r["down|L_max|S"] + r["lep|L_max|S"]))
        return s + np.array([0, 0, 0, 0, LN3, -LN3])
    six, six_main = six_of(own_best), six_of(stored[best])
    pulls, pulls_main = (six - t6) / sg, (six_main - t6) / sg
    row = {"chi2": float((pulls ** 2).sum()), "pulls": pulls.tolist(), "pulls_main_row": pulls_main.tolist(),
           "D": math.exp(six[4] + six[3] - six[2] - six[5]), "model_over_measured": np.exp(six - t6).tolist()}
    row["checks"] = {"chi2_rel_vs_14.932": abs(row["chi2"] - CHI2_BEST) / CHI2_BEST,
                     "pulls_abs_vs_main_row": float(np.max(np.abs(pulls - pulls_main))),
                     "D_rel_vs_11.047": abs(row["D"] - D_BEST) / D_BEST}
    a, b = L[best[0]]
    tau = complex(best[1], best[2])
    rc = 0.0
    for sec in T8.SECTS:
        mine = T8.own_residues(W93, sec, a, b, tau)
        ref = T8.circle_residues(W93, sec, a, b, tau)
        rc = max(rc, max(abs(mine[s] - ref[s]) for s in T8.UNITS) / max(abs(v) for v in ref.values()))
    return {"points": per, "worst": worst, "joint_law_max": jl, "residue_control_rel": rc,
            "B1724 law on own code (census frame against the apex)": tlaw, "row": row,
            "best point": [best[0], str(a), str(b), best[1], best[2]]}


# ============================================================================================ C1, C2
def part_C1(files):
    d = json.loads(files[B1720T].decode("utf-8"))
    L = T8.own_lines()
    line, frame = L[BEST["line"]], L[149]
    out = {"line 153": [str(x) for x in line], "line 149": [str(x) for x in frame],
           "b + 3 alpha = line 149's b": (line[1] + 3 * line[0]) % 1 == frame[1] and line[0] == frame[0]}
    classes = [c for c in d["classes"] if abs(c["tau"][0] - BEST["Re_tau"]) < 1e-9
               and abs(c["tau"][1] - 2.993325909) < 1e-6]
    out["classes at the apex"] = [c["word"] for c in classes]
    per = {}
    for c in classes:
        a, b, cc, dd = c["A"]
        canon_fixed, _ = T41.fixed_lines((a, b, cc, dd))
        A2 = (a * a + b * cc, a * b + b * dd, cc * a + dd * cc, cc * b + dd * dd)
        fixed2, _ = T41.fixed_lines(A2)
        by_order = {}
        for v in fixed2:
            o = T41.lorder(v)
            by_order[o] = by_order.get(o, 0) + 1
        per[c["word"]] = {"trace": a + dd, "line fixed by A up to sign": T41.canon(line) in canon_fixed,
                          "A^2 = -I mod 10": all(x % 10 == y for x, y in zip(A2, (9, 0, 0, 9))),
                          "A^2 fixes order-5 lines": by_order.get(5, 0),
                          "A^2 fixes order-10 lines": by_order.get(10, 0)}
    out["per class"] = per
    return out


def part_C2(files):
    rows = T8.census_rows(files[V41 + "/census.jsonl"])
    best = [r for r in rows if r["line"] == BEST["line"] and abs(r["Re_tau"] - BEST["Re_tau"]) < 1e-9
            and abs(r["Im_tau"] - 2.993325909) < 1e-6][0]
    lep = np.log(np.array(best["lep|L_max|S"]))
    dn = np.log(np.array(best["down|L_max|S"]))
    up = np.log(np.array(best["up|L_max|St"]))
    six = np.concatenate([up, dn, lep]) + np.array([0, 0, 0, 0, LN3, -LN3])
    D = math.exp(six[4] + six[3] - six[2] - six[5])
    out = {"best row: max |log lep - log down| (reading S, L_max)": float(np.max(np.abs(lep - dn))),
           "D": D, "D/9": D / 9}
    counts = {"same reading, every horocycle and reading": 0, "same reading, some horocycle and reading": 0,
              "swapped reading (lep S vs down St and back), every horocycle": 0}
    lines_all = {}
    for r in rows:
        dev_same = [float(np.max(np.abs(T8.floor_log(r[f"lep|{h}|{a}"]) - T8.floor_log(r[f"down|{h}|{a}"]))))
                    for h in T8.HORO for a in T8.RD]
        dev_swap = [float(np.max(np.abs(T8.floor_log(r[f"lep|{h}|{a}"]) - T8.floor_log(r[f"down|{h}|{b}"]))))
                    for h in T8.HORO for a, b in (("S", "St"), ("St", "S"))]
        if max(dev_same) < 1e-8:
            counts["same reading, every horocycle and reading"] += 1
            lines_all.setdefault(r["line"], set()).add((r["Re_tau"], r["Im_tau"]))
        if min(dev_same) < 1e-8:
            counts["same reading, some horocycle and reading"] += 1
        if max(dev_swap) < 1e-8:
            counts["swapped reading (lep S vs down St and back), every horocycle"] += 1
    L = T8.own_lines()
    out["read-out: points (of 19 950)"] = counts
    out["read-out: lines with the identity at every one of the 75 apexes"] = sorted(
        [str(L[k][0]), str(L[k][1])] for k, v in lines_all.items() if len(v) == 75)
    out["read-out: lines with the identity at some apex"] = len(lines_all)
    return out


# ============================================================================================ D1
def sens_job(task):
    seed, name = task
    sg, ks = T42._W["variants"][name]
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    T = np.array(six)
    cf = T42.configs(T42._W["arr"], "seat", sg, ks)
    obs = float(T42.direct_min(cf, T42._W["T6"], sg)[0][0])
    return seed, name, obs, float(np.mean(T42.direct_min(cf, T, sg)[0] <= obs + 1e-9))


def part_D1(files, workers, tmp):
    t6, _t9 = T8.targets(files)
    _rows, arr, _lab = arrays(files)
    npz = str(Path(tmp) / "B1741_sens.npz")
    np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=T42.sigma(files))
    variants = {"allowance 0.05": (T42.sigma(files, 0.05), (0.0, LN3)),
                "lepton factor over {1, ..., 5}": (T42.sigma(files, 0.10), tuple(math.log(c) for c in range(1, 6))),
                "uniform sigma 0.10": (np.full(6, 0.10), (0.0, LN3))}

    def init():
        T42._init("B1741", npz, 0.10)
        T42._W["variants"] = variants
    init()
    tasks = [(s, v) for s in SEEDS for v in variants]
    with mpr.Pool(workers, initializer=init) as P:
        res = P.map(sens_job, tasks)
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
    except Exception:  # noqa: BLE001  (a missing part leaves its cells False, with the trace kept)
        out["cells_failed"] = sanitize(traceback.format_exc()[-2000:])
        return {key: bool(val) for key, val in c.items()}


def _cells(out, c):
    if "A0" in out:
        a = out["A0"]
        c["A0"] = (all(a[p] for p in PIN) and a["census rows"] == 19950 and a["census distinct (line, Re, Im)"] == 19950
                   and all(v is True for v in a["ARTIFACT_HASHES"].values()))
    if "A1" in out:
        a = out["A1"]
        c["A1"] = (a["compare"]["returncode"] == 0 and a.get("cells identical") and a.get("per-seed fractions exact")
                   and not a.get("diff", {"mismatches": [1]})["mismatches"]
                   and a.get("diff", {"max_rel": 1})["max_rel"] < 1e-12)
    if "A2" in out:
        a = out["A2"]
        c["A2"] = (a["per_seed_equal_main"] and max(a["min_rel_vs_main"].values()) < 1e-10
                   and a["seat minimum at FINDINGS' row"]
                   and all(a["chi2_nine"][m]["rel_vs_main"] < 1e-6 for m in ("seat", "sm"))
                   and all(round(a["chi2_nine"][m]["chi2_nine_min"]) == NINE_MAIN[m] for m in ("seat", "sm")))
    if "A3" in out:
        a = out["A3"]
        c["A3"] = (a["classes"] == 121 and not a["classes failing"] and a["distinct apex points"] == 75
                   and a["equal census.jsonl's points"] and a["census points"] == 75)
    if "A4" in out:
        a = out["A4"]
        c["A4"] = (a["W140 lines"] == 266 and a["equal as sets"] and a["every apex has lines 0-265"]
                   and a["apexes"] == 75)
    if "B" in out:
        b = out["B"]
        w, t, v = b["worst"], b["B1724 law on own code (census frame against the apex)"], b["row"]["checks"]
        c["B0"] = (b["residue_control_rel"] < TOL["residue_rel"] and b["joint_law_max"] < TOL["joint_law"]
                   and max(t["up"], t["down"], t["lep"], t["ckm"]) < 1e-8)
        c["B1"] = (max(w["up"], w["down"], w["lep"], w["ckm"]) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                   and w["zero_pattern_mismatches"] == 0)
        c["B2"] = v["chi2_rel_vs_14.932"] < 1e-4 and v["pulls_abs_vs_main_row"] < 1e-3 and v["D_rel_vs_11.047"] < 1e-4
    if "C1" in out:
        k = out["C1"]
        pc = k["per class"].values()
        c["C1"] = (k["line 153"] == ["2/5", "9/10"] and k["line 149"] == ["2/5", "1/10"]
                   and k["b + 3 alpha = line 149's b"]
                   and len(k["per class"]) == 2 and all(not p["line fixed by A up to sign"] and p["trace"] == 30
                                                        and p["A^2 = -I mod 10"] and p["A^2 fixes order-5 lines"] == 12
                                                        and p["A^2 fixes order-10 lines"] == 36 for p in pc))
    if "C2" in out:
        k = out["C2"]
        c["C2"] = k["best row: max |log lep - log down| (reading S, L_max)"] > 1e-3 and abs(k["D/9"] - 1.227) < 1e-3
    if "D1" in out:
        s = out["D1"]
        c["D1"] = (s["allowance 0.05"]["chi2_six_min"] > BAR6
                   and s["lepton factor over {1, ..., 5}"]["fraction_mean"] > 0.01
                   and abs(s["uniform sigma 0.10"]["chi2_six_min"] - 19.61) < 0.01
                   and s["uniform sigma 0.10"]["chi2_six_min"] > BAR6
                   and s["uniform sigma 0.10"]["fraction_mean"] <= 0.01)
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W145", "rule": "W145_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers}
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    guarded(out, "A0", part_A0, files)
    guarded(out, "A1", part_A1, files, args.workers)
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp2>"] = td
        guarded(out, "A2", part_A2, files, args.workers, td)
        guarded(out, "D1", part_D1, files, args.workers, td)
    guarded(out, "A3", part_A3, files)
    guarded(out, "A4", part_A4, files, out.get("A1"))
    guarded(out, "C1", part_C1, files)
    guarded(out, "C2", part_C2, files)
    if "A2" in out:
        guarded(out, "B", part_B, root, files, out["A2"])
    if "A1" in out:
        out["A1"].pop("main_lines", None)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    out["opinion"] = {"replicated value-level READING, bankable as that and no more":
                      bool(all(c.get(k) for k in ("A1", "A2", "B1")))}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
