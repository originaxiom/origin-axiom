#!/usr/bin/env python3
"""W142 (P-342): the third opinion on main's B1735, THE PRECISION BAR ON THE TWO-INGREDIENT CENSUSES, with an audit of
its scripts and arithmetic (the rule: W142_RULE.md, committed and pushed before this script existed). It runs once,
from the repository root.

  A0  the inputs: the two censuses against their recorded sha256 values, the data files against their pins
  A1  main's calib_chi2.py and control.py re-run in a temporary tree; calib_chi2.json and control.json diffed;
      check.json's covariant-free per-seed fractions against W138's and W141's committed ones; and, in that tree, B1735's sigma()
      and B1720's meas() executed from their own source against this seat's sigma (A3)
  A2  the chi-square calibration on own code: direct sums of squared differences (not the |X|^2 - 2X.t + |t|^2
      expansion), four menus, both censuses, each arc's 20 seeds; chi2_nine (seat)
  A3  the definitions: sigma from the pinned files; the bar against the chi-square quantiles
  A4  labelled sensitivity on B1726 (seat's menu, seeds 1726-1730): allowance 0.05 and 0.20; the lepton factor removed
  B   the chi2-best point (2/5, 1/10) at 0.35 + 3.05i and its four grid neighbours on this seat's own instrument
      (W138's); B0 its controls; B2 the row's chi2, pulls, D, CKM and J from the own values
  C1  FINDINGS' statements computed: the grid's Re steps, 79.38 / 16.75, the pulls, D, J, section 2's table

    python3 -B docs/dossiers/the_weave_2026-10-07/the_third_opinion_b1735.py [--workers 4]
"""
import argparse
import contextlib
import importlib.util
import io
import json
import math
import multiprocessing as mpr
import platform
import re
import subprocess
import sys
import tempfile
import time
import traceback
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.stats import chi2 as CHI2

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_third_opinion_b1726 as T8   # noqa: E402  (W138)
    import the_third_opinion_b1734 as T41  # noqa: E402  (W141)

REV = "bf0a9a330f811ff7f1075dd748da001df1a819e3"   # origin/main as read for the rule
V35 = "frontier/B1735_the_precision_bar_on_the_two_ingredient_censuses/verification"
V26 = "frontier/B1726_the_two_ingredients_replicated/verification"
V34 = "frontier/B1734_the_thread_rule_with_the_two_ingredients/verification"
B1720C = "frontier/B1720_the_thread_fixes_the_point/verification/compare.py"
B1720J = "frontier/B1720_the_thread_fixes_the_point/verification/comparison.json"
DEPS = ("frontier/B1723_the_golden_valley/verification/b1656_funcs.py",
        "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py",
        "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py")
HZ, CKM, COLUMN = T8.HZ, T8.CKM, T8.COLUMN
FILES = (V35 + "/check.py", V35 + "/calib_chi2.py", V35 + "/control.py", V35 + "/calib_chi2.json", V35 + "/check.json",
         V35 + "/control.json", V26 + "/compare.py", V26 + "/census.py", V26 + "/census.jsonl", V26 + "/control.json",
         V34 + "/compare.py", V34 + "/census.json", V34 + "/control.json", B1720C, B1720J, HZ, CKM, COLUMN) + DEPS
SHA = {V26 + "/census.jsonl": "d67432f0dc252e911514f211eb29844fd0bfcc5a270c00188312607435b0478d",
       V34 + "/census.json": "b29ac3e3164c1b517c36c1a65e5f6d005314967a76767c36855438f47730d5d8",
       HZ: T8.PINNED[HZ], CKM: T8.PINNED[CKM], COLUMN: T8.PINNED[COLUMN]}
OUT = HERE / "third_opinion_b1735.json"
SEEDS = {"B1726": tuple(range(1726, 1746)), "B1734": tuple(range(1734, 1754))}
SENS_SEEDS = tuple(range(1726, 1731))
MENUS = ("seat", "cov", "free", "covfree")
SEAT, COV = T8.SEAT, T8.COV
LN3 = math.log(3)
BAR6, BAR9 = 16.75, 21.67
ROW = (Fr(2, 5), Fr(1, 10), 0.35, 3.05)
NEIGH = ((0.2, 3.05), (0.55, 3.05), (0.35, 2.95), (0.35, 3.15))
CONTROL = {"chi2": 3.0945633097838114, "D": 10.76469843358276,
           "ckm": [4.411743890302265, 23.842064016485814, 10.611215922339403], "J": 0.00024679661748743805,
           "pulls": [0.6427891447757443, -1.3168672347710584, 0.6696885700921221, 0.10281417824235763,
                     0.3062746107194239, -0.628003533268474]}
# FINDINGS section 2's table as printed: (chi2 min, mean %, worst seed %) and chi2_nine
TABLE = {"B1726": {"seat": (3.09, 0.03, 0.10), "cov": (3.09, 0.10, 0.20), "free": (2.66, 0.25, 0.40),
                   "covfree": (2.66, 0.96, 1.35)},
         "B1734": {"seat": (42.3, 0.29, 0.40), "cov": (36.9, 0.64, 0.80), "free": (39.3, 1.02, 1.47),
                   "covfree": (31.3, 1.88, 2.38)}}
NINE = {"B1726": 109, "B1734": 441}
TOL = T8.TOL
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


# ============================================================================================ sigma and targets
def sigma(files, allow=0.10):
    d = json.loads(files[HZ].decode("utf-8"))["masses_GeV"]
    v, s = d["value"], d["sigma"]
    pairs = (("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau"))
    return np.array([math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + allow ** 2) for a, b in pairs])


def sigma_ckm(files, allow=0.10):
    c = json.loads(files[CKM].decode("utf-8"))["ckm_abs"]
    v, s = c["value"], c["sigma"]
    return np.array([math.sqrt((s[i][j] / v[i][j]) ** 2 + allow ** 2) for i, j in ((0, 1), (1, 2), (0, 2))])


# ============================================================================================ own chi-square
_W = {}


def configs(arr, menu, sg, ks=(0.0, LN3)):
    """per configuration the rows' coordinates in sigma units, and how a target maps to the same coordinates"""
    out = []
    cfg = SEAT if menu in ("seat", "free") else COV
    for (a, b, l) in cfg:
        base = [arr["up"][:, a, 0] / sg[0], arr["up"][:, a, 1] / sg[1], arr["dn"][:, b, 0] / sg[2],
                arr["dn"][:, b, 1] / sg[3]]
        if menu in ("seat", "cov"):
            for k in ks:
                out.append(((a, b, l, k), np.stack(base + [(arr["lep"][:, l, 0] + k) / sg[4],
                                                           (arr["lep"][:, l, 1] - k) / sg[5]], axis=1), "fixed"))
        else:
            s45 = math.hypot(sg[4], sg[5])
            out.append(((a, b, l, "free"), np.stack(base + [(arr["lep"][:, l, 0] + arr["lep"][:, l, 1]) / s45],
                                                       axis=1), "free"))
    return out


def tmap(T, kind, sg):
    T = np.atleast_2d(T)
    if kind == "fixed":
        return T / sg
    s45 = math.hypot(sg[4], sg[5])
    return np.concatenate([T[:, 0:4] / sg[0:4], ((T[:, 4] + T[:, 5]) / s45)[:, None]], axis=1)


def direct_min(cfgs, T, sg, block=200):
    """for each target: the minimum over rows and configurations of the sum of squared differences, summed directly;
    also the argmin (configuration, row) for the first target"""
    T = np.atleast_2d(T)
    best = np.full(len(T), np.inf)
    arg = None
    for key, X, kind in cfgs:
        t = tmap(T, kind, sg)
        for s0 in range(0, len(t), block):
            tb = t[s0:s0 + block]
            acc = np.zeros((X.shape[0], len(tb)))
            for j in range(X.shape[1]):
                acc += (X[:, j][:, None] - tb[:, j][None, :]) ** 2
            m = acc.min(axis=0)
            if s0 == 0 and m[0] < best[0]:
                arg = (key, int(acc[:, 0].argmin()))
            best[s0:s0 + block] = np.minimum(best[s0:s0 + block], m)
    return best, arg


def _init(name, npz, allow):
    d = np.load(npz)
    _W.clear()
    _W.update(name=name, arr={k: d[k] for k in ("up", "dn", "lep")}, T6=d["T6"], sg=d["sg"])


def calib_job(seed):
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    T = np.array(six)
    out = {}
    for menu in MENUS:
        cf = configs(_W["arr"], menu, _W["sg"])
        obs = float(direct_min(cf, _W["T6"], _W["sg"])[0][0])
        out[menu] = (obs, float(np.mean(direct_min(cf, T, _W["sg"])[0] <= obs + 1e-9)))
    return seed, out


def sens_job(task):
    seed, variant = task
    allow, ks = variant
    six, _nine = T8.own_draws(seed, T8.NTARGET)
    T = np.array(six)
    sg = _W["sg_by_allow"][allow]
    cf = configs(_W["arr"], "seat", sg, ks)
    obs = float(direct_min(cf, _W["T6"], sg)[0][0])
    return seed, variant, obs, float(np.mean(direct_min(cf, T, sg)[0] <= obs + 1e-9))


def load_census(name, files):
    if name == "B1726":
        rows = T8.census_rows(files[V26 + "/census.jsonl"])
        arr, lab = T8.census_arrays(rows)
    else:
        rows = json.loads(files[V34 + "/census.json"].decode("utf-8"))["rows"]
        arr, lab = T41.census_arrays(rows)
    return rows, arr, lab


def chi2_nine(arr, lab, T9, s9):
    best = (math.inf, None)
    for (a, b, l) in SEAT:
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


def part_A2(files, workers, tmp):
    t6, t9 = T8.targets(files)
    sg = sigma(files)
    s9 = np.concatenate([sg, sigma_ckm(files)])
    main_cal = json.loads(files[V35 + "/calib_chi2.json"].decode("utf-8"))
    out = {}
    for name in ("B1726", "B1734"):
        _rows, arr, lab = load_census(name, files)
        npz = str(Path(tmp) / f"{name}.npz")
        np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=sg)
        _init(name, npz, 0.10)
        mins = {}
        for menu in MENUS:
            m, arg = direct_min(configs(arr, menu, sg), t6, sg)
            (a, b, l, k), i = arg
            mins[menu] = {"chi2_six_min": float(m[0]), "row": [str(x) for x in lab[i]],
                          "readings": [T8.RD[a], T8.RD[b], T8.RD[l]], "k": k if k == "free" else float(k)}
        with mpr.Pool(workers, initializer=_init, initargs=(name, npz, 0.10)) as P:
            per = dict(P.map(calib_job, SEEDS[name]))
        mc = main_cal[name]
        r = {"mins": mins, "per_seed": {str(s): {m: per[s][m][1] for m in MENUS} for s in SEEDS[name]}}
        r["per_seed_equal_main"] = all(per[s][m][1] == mc[m]["per_seed"][str(s)] for s in SEEDS[name] for m in MENUS)
        r["min_rel_vs_main"] = {m: abs(mins[m]["chi2_six_min"] - mc[m]["chi2_six_min"]) / mc[m]["chi2_six_min"]
                                for m in MENUS}
        r["mean"] = {m: float(np.mean([per[s][m][1] for s in SEEDS[name]])) for m in MENUS}
        r["worst_seed"] = {m: float(np.max([per[s][m][1] for s in SEEDS[name]])) for m in MENUS}
        n9 = chi2_nine(arr, lab, t9, s9)
        n9["rel_vs_main"] = abs(n9["chi2_nine_min"] - mc["chi2_nine_seat"]["chi2_nine_min"]) / \
            mc["chi2_nine_seat"]["chi2_nine_min"]
        n9["row_main"] = [str(x) for x in mc["chi2_nine_seat"]["row"]]
        r["chi2_nine_seat"] = n9
        out[name] = r
    return out


def part_A4(files, workers, tmp):
    t6, _t9 = T8.targets(files)
    _rows, arr, lab = load_census("B1726", files)
    npz = str(Path(tmp) / "B1726_sens.npz")
    np.savez(npz, up=arr["up"], dn=arr["dn"], lep=arr["lep"], T6=t6, sg=sigma(files))
    variants = {"allowance 0.05": (0.05, (0.0, LN3)), "allowance 0.20": (0.20, (0.0, LN3)),
                "no lepton factor (c = 1), allowance 0.10": (0.10, (0.0,))}

    def init(npz=npz):
        _init("B1726", npz, 0.10)
        _W["sg_by_allow"] = {a: sigma(files, a) for a in (0.05, 0.10, 0.20)}
    init()
    tasks = [(s, v) for s in SENS_SEEDS for v in variants.values()]
    with mpr.Pool(workers, initializer=init) as P:
        res = P.map(sens_job, tasks)
    out = {}
    for name, v in variants.items():
        rr = [x for x in res if x[1] == v]
        out[name] = {"chi2_six_min": rr[0][2], "fraction_mean_5_seeds": float(np.mean([x[3] for x in rr])),
                     "per_seed": [x[3] for x in rr]}
    return out


# ============================================================================================ A1: the re-run
def build_tree(tmp, files):
    (tmp / "GENESIS.md").write_text("root marker for the P-342 re-run (not main's GENESIS)\n", encoding="utf-8")
    for p, b in files.items():
        q = tmp / p
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_bytes(b)
    return tmp / V35


def run(script, vdir, args=()):
    t0 = time.time()
    p = subprocess.run([sys.executable, "-B", str(vdir / script), *args], cwd=vdir, capture_output=True, text=True)
    return {"returncode": p.returncode, "seconds": round(time.time() - t0, 1), "stdout": p.stdout,
            "stderr_tail": sanitize(p.stderr[-3000:])}


def per_seed_exact(old, new):
    ok = True
    for name in ("B1726", "B1734"):
        for m in MENUS:
            ok &= old[name][m]["per_seed"] == new[name][m]["per_seed"]
    return ok


def part_A1(files, workers, own_sigma):
    out = {}
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp>"] = td
        vdir = build_tree(Path(td), files)
        rc = run("calib_chi2.py", vdir, ("--workers", str(workers)))
        new = json.loads((vdir / "calib_chi2.json").read_text(encoding="utf-8")) if rc["returncode"] == 0 else None
        rk = run("control.py", vdir)
        newc = json.loads((vdir / "control.json").read_text(encoding="utf-8")) if rk["returncode"] == 0 else None
        # A3's executions in the same tree: B1735's sigma() and B1720's meas() from their own source
        spec = importlib.util.spec_from_file_location("b1735_check", vdir / "check.py")
        chk = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(chk)
        sg_main = np.array(chk.sigma())
        src = (Path(td) / B1720C).read_text(encoding="utf-8")
        lines = [ln for ln in src.splitlines() if ln.startswith("ALLOW =") or ln.startswith("def meas(")]
        d = json.loads((Path(td) / HZ).read_text(encoding="utf-8"))["masses_GeV"]
        ns = {"math": math, "v": d["value"], "s": d["sigma"]}
        exec("\n".join(lines), ns)  # noqa: S102  (two lines of B1720's committed compare.py, read for the audit)
        sg_1720 = np.array([ns["meas"](a, b)[1] for a, b in (("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"),
                                                             ("mu", "tau"), ("e", "tau"))])
    old = json.loads(files[V35 + "/calib_chi2.json"].decode("utf-8"))
    oldc = json.loads(files[V35 + "/control.json"].decode("utf-8"))
    out["calib"] = {k: v for k, v in rc.items() if k != "stdout"}
    out["control"] = {k: v for k, v in rk.items() if k != "stdout"}
    if new is not None:
        dd = T8.deep_diff(old, new)
        dd["mismatches"] = [[("bool:" + x) if x in ("True", "False") else x for x in m] for m in dd["mismatches"][:40]]
        out["calib_diff"] = dd
        out["calib_per_seed_exact"] = per_seed_exact(old, new)
    if newc is not None:
        dc = T8.deep_diff(oldc, newc)
        dc["mismatches"] = [[("bool:" + x) if x in ("True", "False") else x for x in m] for m in dc["mismatches"][:40]]
        out["control_diff"] = dc
    chk_json = json.loads(files[V35 + "/check.json"].decode("utf-8"))
    w138 = json.loads((HERE / "third_opinion_b1726.json").read_text(encoding="utf-8"))["A2"]["per_seed"]
    w141 = json.loads((HERE / "third_opinion_b1734.json").read_text(encoding="utf-8"))["A2"]["per_seed"]
    out["check_covfree_equals_W138"] = all(chk_json["B1726"]["covfree_six"]["per_seed"][s] == w138[s]["six|cov_free"]
                                           for s in chk_json["B1726"]["covfree_six"]["per_seed"])
    out["check_covfree_equals_W141"] = all(chk_json["B1734"]["covfree_six"]["per_seed"][s] == w141[s]["six|cov_free"]
                                           for s in chk_json["B1734"]["covfree_six"]["per_seed"])
    out["A3_sigma_main_vs_own_max"] = float(np.max(np.abs(sg_main - own_sigma)))
    out["A3_sigma_B1720_vs_own_max"] = float(np.max(np.abs(sg_1720 - own_sigma)))
    return out


def part_A0(files):
    return {p: T8.sha256(files[p]) == h for p, h in SHA.items()}


def part_A3(files):
    sg = sigma(files)
    q6, q9 = float(CHI2.ppf(0.99, 6)), float(CHI2.ppf(0.99, 9))
    return {"sigma": sg.tolist(), "sigma_ckm": sigma_ckm(files).tolist(), "chi2_6_99": q6, "chi2_9_99": q9,
            "bar6_below_q6": BAR6 < q6, "bar9_equals_q9_to_1e-2": abs(BAR9 - q9) < 1e-2}


# ============================================================================================ B: the row on own code
_B = {}


def b_job(pt):
    re_t, im_t = pt
    own, diag = T8.own_point(_B["W93"], _B["W89"], _B["col"], (ROW[0], ROW[1]), re_t, im_t)
    return pt, own, diag


def part_B(root, files):
    W93, W89 = T8.own_modules(root)
    _B.update(W93=W93, W89=W89, col=T8.L_column(files))
    rows = T8.census_rows(files[V26 + "/census.jsonl"])
    k = T8.own_lines().index((ROW[0], ROW[1]))
    stored = {(r["Re_tau"], r["Im_tau"]): r for r in rows if r["line"] == k}
    pts = [(ROW[2], ROW[3])] + list(NEIGH)
    with mpr.Pool(len(pts)) as P:
        res = P.map(b_job, pts)
    worst = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    jl, per = 0.0, []
    own_row = None
    for pt, own, diag in res:
        dev = T8.compare_point(own, stored[pt])
        for f in worst:
            worst[f] = worst[f] + dev[f] if f == "zero_pattern_mismatches" else max(worst[f], dev[f])
        jl = max(jl, diag["joint_law_max"])
        per.append({"tau": list(pt), "deviation": dev})
        if pt == (ROW[2], ROW[3]):
            own_row = own
    t6, _t9 = T8.targets(files)
    sg = sigma(files)
    six = np.log(np.array(own_row["up|L_max|St"] + own_row["down|L_max|S"] + own_row["lep|L_max|S"]))
    six += np.array([0, 0, 0, 0, LN3, -LN3])
    pulls = (six - t6) / sg
    C = json.loads(files[CKM].decode("utf-8"))["ckm_abs"]["value"]
    ck = own_row["ckm|L_max|St|S"]
    row = {"chi2": float((pulls ** 2).sum()), "pulls": pulls.tolist(),
           "D": math.exp(six[4] + six[3] - six[2] - six[5]),
           "ckm_over_data": [ck[0] / C[0][1], ck[1] / C[1][2], ck[2] / C[0][2]], "J": ck[3]}
    row["vs_control"] = {"chi2_rel": abs(row["chi2"] - CONTROL["chi2"]) / CONTROL["chi2"],
                         "pulls_abs": float(np.max(np.abs(pulls - np.array(CONTROL["pulls"])))),
                         "D_rel": abs(row["D"] - CONTROL["D"]) / CONTROL["D"],
                         "ckm_rel": max(abs(a - b) / b for a, b in zip(row["ckm_over_data"], CONTROL["ckm"])),
                         "J_rel": abs(row["J"] - CONTROL["J"]) / abs(CONTROL["J"])}
    a, b, tau = ROW[0], ROW[1], complex(ROW[2], ROW[3])
    rc = 0.0
    for sec in T8.SECTS:
        mine = T8.own_residues(W93, sec, a, b, tau)
        ref = T8.circle_residues(W93, sec, a, b, tau)
        rc = max(rc, max(abs(mine[s] - ref[s]) for s in T8.UNITS) / max(abs(v) for v in ref.values()))
    return {"points": per, "worst": worst, "joint_law_max": jl, "residue_control_rel": rc, "row": row}


# ============================================================================================ C1: FINDINGS' statements
def part_C1(files, a2):
    rows = T8.census_rows(files[V26 + "/census.jsonl"])
    res = sorted({r["Re_tau"] for r in rows})
    steps = sorted({round(b - a, 10) for a, b in zip(res[:-1], res[1:])})
    b1720 = json.loads(files[B1720J].decode("utf-8"))["best_chi2"]["chi2"]
    cal = json.loads(files[V35 + "/calib_chi2.json"].decode("utf-8"))
    ctl = json.loads(files[V35 + "/control.json"].decode("utf-8"))
    table = {}
    ok_table = True
    for name, menus in TABLE.items():
        half = 0.05 if name == "B1734" else 0.005          # half a unit of the printed precision
        for m, (mn, mean, worst) in menus.items():
            c = cal[name][m]
            got = (c["chi2_six_min"], 100 * c["fraction_mean"], 100 * c["fraction_max"])
            table[f"{name}|{m}"] = {"printed": [mn, mean, worst], "computed": list(got)}
            ok_table &= (abs(got[0] - mn) <= half + 1e-9 and abs(got[1] - mean) <= 0.005 + 1e-9
                         and abs(got[2] - worst) <= 0.005 + 1e-9)
    nine = {n: round(cal[n]["chi2_nine_seat"]["chi2_nine_min"]) for n in NINE}
    ok_nine = nine == NINE
    pull_max = max(abs(p) for p in ctl["pulls"])
    dsig = (ctl["D"] - 10.58) / 0.11
    jx = ctl["J"] / 3.08e-5
    return {"re_tau_values": res, "re_steps": steps, "slip_1_grid_step_not_all_0.15": steps != [0.15],
            "B1720_best_chi2": b1720, "ratio_to_bar": b1720 / BAR6, "slip_2_factor_below_5": b1720 / BAR6 < 5,
            "max_pull": pull_max, "pulls_within_1.32": pull_max <= 1.32, "D_sigma": dsig, "D_within_1.7": dsig < 1.7,
            "J_over_PDG": jx, "J_eight_times": round(jx) == 8, "table": table, "table_as_printed": ok_table,
            "chi2_nine_rounded": nine, "chi2_nine_as_printed": ok_nine}


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
        c["A0"] = all(out["A0"].values())
    if "A1" in out:
        a = out["A1"]
        c["A1"] = (a["calib"]["returncode"] == 0 and a["control"]["returncode"] == 0 and a.get("calib_per_seed_exact")
                   and not a.get("calib_diff", {"mismatches": [1]})["mismatches"]
                   and not a.get("control_diff", {"mismatches": [1]})["mismatches"]
                   and a["check_covfree_equals_W138"] and a["check_covfree_equals_W141"])
    if "A2" in out:
        a = out["A2"]
        c["A2"] = all(a[n]["per_seed_equal_main"] and max(a[n]["min_rel_vs_main"].values()) < 1e-10
                      and a[n]["chi2_nine_seat"]["rel_vs_main"] < 1e-10
                      and a[n]["chi2_nine_seat"]["row"] == a[n]["chi2_nine_seat"]["row_main"] for n in a)
    if "A3" in out and "A1" in out:
        c["A3"] = (out["A1"]["A3_sigma_main_vs_own_max"] < 1e-15 and out["A1"]["A3_sigma_B1720_vs_own_max"] < 1e-15
                   and out["A3"]["bar6_below_q6"] and out["A3"]["bar9_equals_q9_to_1e-2"])
    if "A4" in out:
        s = out["A4"]
        c["A4"] = (s["allowance 0.05"]["chi2_six_min"] < BAR6
                   and s["no lepton factor (c = 1), allowance 0.10"]["chi2_six_min"] > BAR6)
    if "B" in out:
        b = out["B"]
        w, v = b["worst"], b["row"]["vs_control"]
        c["B0"] = b["residue_control_rel"] < TOL["residue_rel"] and b["joint_law_max"] < TOL["joint_law"]
        c["B1"] = (max(w["up"], w["down"], w["lep"], w["ckm"]) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                   and w["zero_pattern_mismatches"] == 0)
        c["B2"] = (v["chi2_rel"] < 1e-6 and v["pulls_abs"] < 1e-5 and v["D_rel"] < 1e-6 and v["ckm_rel"] < 1e-6
                   and v["J_rel"] < 1e-5)
    if "C1" in out:
        k = out["C1"]
        c["C1"] = (k["slip_1_grid_step_not_all_0.15"] and k["slip_2_factor_below_5"] and k["pulls_within_1.32"]
                   and k["D_within_1.7"] and k["J_eight_times"] and k["table_as_printed"] and k["chi2_nine_as_printed"])
    return {key: bool(val) for key, val in c.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W142", "rule": "W142_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "mpmath": mp.__version__, "machine": platform.machine(), "workers": args.workers}
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    guarded(out, "A0", part_A0, files)
    guarded(out, "A3", part_A3, files)
    guarded(out, "A1", part_A1, files, args.workers, sigma(files))
    with tempfile.TemporaryDirectory() as td:
        _ROOT["<tmp2>"] = td
        guarded(out, "A2", part_A2, files, args.workers, td)
        guarded(out, "A4", part_A4, files, args.workers, td)
    guarded(out, "C1", part_C1, files, out.get("A2"))
    guarded(out, "B", part_B, root, files)
    out["cells"] = cells(out)
    out["every predicted cell holds"] = bool(out["cells"]) and all(out["cells"].values())
    c = out["cells"]
    out["opinion"] = {
        "replicated value-level READING, bankable as that and no more": all(c.get(k) for k in ("A1", "A2", "B1")),
        "no error in main's code or arithmetic (A1, A2, A3, B1, C1)": all(c.get(k) for k in ("A1", "A2", "A3", "B1",
                                                                                            "C1"))}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", ", ".join(failed), file=sys.stderr)


if __name__ == "__main__":
    main()
