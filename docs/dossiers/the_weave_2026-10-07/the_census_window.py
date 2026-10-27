#!/usr/bin/env python3
"""W162 — the census window (the rule: W162_RULE.md, committed and pushed before this script).  It runs once, from the
repository root, on four worker processes.

Is the six's alpha = 2/5 a property of the lines, or of the window Im tau 2.0-3.6 every census on record scanned?  The six
with the record's Higgs DR, in B1656's frame at B1667's end on this seat's own instrument (W158's), the seat's menu and
both horocycles:
  Tier A  the 12 order-10 lines with 5w = 1/2, Re tau at 8 values, Im tau 1.2-12 at 61 heights
  Tier B  B1726's 266 lines, Re tau at 4 values, Im tau at 9 heights outside or at the edge of the old window
Above Im tau 4, where B1667's column ends, L is held at its Im tau = 4 value (the rule's stated choice).

  K0  the pins; ten of W158's strip rows against the stored census; every task computed
  K1  no line with a != 2/5 below 16.75 anywhere
  K2  each class's least up part at the exponent law's height
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_census_window.py
"""
import contextlib
import io
import json
import math
import platform
import sys
import time
import traceback
from fractions import Fraction as Fr
from multiprocessing import Pool
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_two_special_higgs as W58      # noqa: E402  (W158: rows, pins; W157, W156, W145 under it)
W57, T8, T42 = W58.W57, W58.T8, W58.T42
W56 = W57.W56

REV = W58.REV
FILES, PIN = W58.FILES, W58.PIN
V49, V53 = W58.V49, W58.V53
OUT = HERE / "the_census_window.json"
BAR6 = 16.75
RE_A = [(2 * k + 1) / 16 for k in range(8)]
IM_A = [round(1.2 + 0.1 * i, 2) for i in range(29)] + [round(4.25 + 0.25 * i, 2) for i in range(32)]
RE_B = [1 / 8, 3 / 8, 5 / 8, 7 / 8]
IM_B = [1.2, 1.4, 1.6, 1.8, 4.0, 5.0, 6.5, 8.5, 11.0]
LTOP = 4.0
WINDOW = (2.0, 3.6)
PRED = {"0": (1.4, 2.3), "1/5": (7.0, 12.0), "2/5": (2.5, 3.6)}
UNIT = ("i", "j", "k")
_ROOT = {}
_G = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def L_of(col, y, hor):
    return T8.L_at(col, min(y, LTOP), hor)


# ============================================================================================ one point, in a worker
def _init(root_str, col):
    root = Path(root_str)
    with contextlib.redirect_stdout(io.StringIO()):
        W93, W89 = T8.own_modules(root)
    _G.update(W93=W93, W89=W89, col=col, L=T8.own_lines())


def point(task):
    """(k, x, y, lscale) -> per horocycle the log-ratios per reading for up, down and leptons; dropped channels"""
    k, x, y, lscale = task
    W93, W89, col = _G["W93"], _G["W89"], _G["col"]
    a, b = _G["L"][k]
    tau = complex(x, y)
    try:
        dr = T8.higgs_DR(tau)
        S = dr[0] * W93.CN["i"] + dr[1] * W93.CN["j"] + dr[2] * W93.CN["k"]
        reads = {"S": S, "St": W93.EPSN @ np.conj(S) @ W93.EPSN.T}
        out = {"k": k, "x": x, "y": y, "dropped": 0}
        Rc = {}
        for sec in T8.SECTS:
            R = T8.own_residues(W93, sec, a, b, tau)
            c = T8.own_norms(W89, W93, sec, a, b, tau, R)
            mx = max(abs(R[s]) for s in T8.UNITS)
            out["dropped"] += sum(1 for s in T8.UNITS if 0 < abs(R[s]) <= 1e-12 and abs(R[s]) / mx > 1e-25)
            Rc[sec] = (R, c)
        for hor in T8.HORO:
            Lv = lscale * L_of(col, y, hor)
            for sec in T8.SECTS:
                R, c = Rc[sec]
                M = T8.weighted_M(W93, R, c, Lv)
                out[(sec, hor)] = [T8.floor_log(T8.ratios(W93.coupling_np(reads[rd], M))[0]).tolist() for rd in T8.RD]
        return out
    except Exception:  # noqa: BLE001  (a failed task is kept and disclosed)
        return {"k": k, "x": x, "y": y, "failed": traceback.format_exc()[-1500:]}


def best_six(results, t6, sg):
    """per result and horocycle the seat's best chi2_six (W156's seat_best_per_row) and the up part at the up reading"""
    up, dn, lep, lab = [], [], [], []
    for r in results:
        for hor in T8.HORO:
            up.append(r[("up", hor)])
            dn.append(r[("down", hor)])
            lep.append(r[("lep", hor)])
            lab.append((r["k"], r["x"], r["y"], hor))
    arr = {"up": np.array(up), "dn": np.array(dn), "lep": np.array(lep)}
    best, arg = W56.seat_best_per_row(arr, t6, sg)
    upart = ((arr["up"][:, 1, 0] - t6[0]) / sg[0]) ** 2 + ((arr["up"][:, 1, 1] - t6[1]) / sg[1]) ** 2
    return best, arg, upart, lab, arr


def cls(line):
    return {Fr(0): "0", Fr(1, 5): "1/5", Fr(2, 5): "2/5"}.get(line[0], str(line[0]))


# ============================================================================================ main
def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W162", "rule": "W162_RULE.md", "status": "one run", "rev": REV, "python": sys.version.split()[0],
           "numpy": np.__version__, "machine": platform.machine()}
    try:
        run(root, out, t0)
    except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
        out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


def run(root, out, t0):
    files = {p: T8.git_bytes(root, REV, p) for p in FILES}
    out["pins"] = {p: T8.sha256(files[p]) == h for p, h in PIN.items()}
    t6, _t9 = T8.targets(files)
    sg = T42.sigma(files)
    col = T8.L_column(files)
    L = T8.own_lines()
    out["L held above Im tau 4"] = {"L_max": L_of(col, LTOP, "L_max"), "L_2": L_of(col, LTOP, "L_2")}
    lines_a = [k for k, p in enumerate(L) if T8.order(p) == 10 and (5 * p[0]).denominator == 1
               and (5 * p[1] - Fr(1, 2)).denominator == 1]
    out["Tier A lines"] = [f"{L[k][0]},{L[k][1]}" for k in lines_a]
    # K0 (i): ten of W158's strip rows against the stored census
    rows_k0, stored = [], {}
    for name, path in (("B1749", V49), ("B1753", V53)):
        rows = T8.census_rows(files[path + "/census.jsonl"])
        _arr, lab, best, _arg = W57.below_rows(rows, t6, sg)
        st = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}
        for i in range(len(best)):
            if best[i] < BAR6:
                k, x, y, hor = lab[i]
                rows_k0.append((name, k, x, y))
                stored[(name, k, x, y)] = st[(k, x, y)]
    rows_k0 = rows_k0[:10]
    tasks_k0 = [(k, x, y, 1.0) for (_n, k, x, y) in rows_k0]
    tasks_a = [(k, x, y, 1.0) for k in lines_a for x in RE_A for y in IM_A]
    tasks_b = [(k, x, y, 1.0) for k in range(len(L)) for x in RE_B for y in IM_B]
    with Pool(4, initializer=_init, initargs=(str(root), col)) as pool:
        res_k0 = pool.map(point, tasks_k0, chunksize=1)
        print("K0 rows done", round(time.time() - t0, 1), flush=True)
        res_a = pool.map(point, tasks_a, chunksize=16)
        print("Tier A done", round(time.time() - t0, 1), flush=True)
        res_b = pool.map(point, tasks_b, chunksize=16)
        print("Tier B done", round(time.time() - t0, 1), flush=True)
        failed = [r for r in res_k0 + res_a + res_b if "failed" in r]
        # K0
        worst = 0.0
        for (name, k, x, y), r in zip(rows_k0, res_k0):
            if "failed" in r:
                continue
            ref = stored[(name, k, x, y)]
            for sec in T8.SECTS:
                for hor in T8.HORO:
                    for ri, rd in enumerate(T8.RD):
                        o = np.array(r[(sec, hor)][ri])
                        s = T8.floor_log(ref[f"{sec}|{hor}|{rd}"])
                        worst = max(worst, float(np.max(np.abs(o - s))))
        out["K0"] = {"pins": out["pins"], "ten strip rows, worst |log own - log stored|": worst,
                     "tasks": len(tasks_k0) + len(tasks_a) + len(tasks_b), "failed tasks": len(failed),
                     "first failure": sanitize(failed[0]["failed"]) if failed else None}
        good_a = [r for r in res_a if "failed" not in r]
        good_b = [r for r in res_b if "failed" not in r]
        # Tier A
        best, arg, upart, lab, arr = best_six(good_a, t6, sg)
        per_point = {}
        for i, (k, x, y, hor) in enumerate(lab):
            key = (k, x, y)
            if key not in per_point or best[i] < per_point[key][0]:
                per_point[key] = (float(best[i]), hor, arg[i], float(upart[i]))
        classes = {}
        for c in ("0", "1/5", "2/5"):
            idx = [i for i, l in enumerate(lab) if cls(L[l[0]]) == c]
            ib = min(idx, key=lambda i: best[i])
            iu = min(idx, key=lambda i: upart[i])
            k, x, y, hor = lab[ib]
            a_, b_, l_, kk = arg[ib]
            parts = [float(((arr[s][ib, rr, j] + (kk if (s == "lep" and j == 0) else (-kk if s == "lep" else 0))
                             - t6[2 * si + j]) / sg[2 * si + j]) ** 2)
                     for si, (s, rr) in enumerate((("up", a_), ("dn", b_), ("lep", l_))) for j in (0, 1)]
            classes[c] = {"least chi2_six": float(best[ib]), "at": [f"{L[k][0]},{L[k][1]}", x, y, hor],
                          "readings": [T8.RD[a_], T8.RD[b_], T8.RD[l_]], "c": round(math.exp(kk)),
                          "its six parts": parts,
                          "least up part": float(upart[iu]), "up part at": [f"{L[lab[iu][0]][0]},{L[lab[iu][0]][1]}",
                                                                            lab[iu][1], lab[iu][2], lab[iu][3]],
                          "least chi2_six per height": {str(h): float(min(best[i] for i in idx if lab[i][2] == h))
                                                        for h in IM_A}}
        out["Tier A"] = classes
        pass_a = sorted({(f"{L[k][0]},{L[k][1]}", x, y) for (k, x, y), v in per_point.items() if v[0] < BAR6},
                        key=lambda t: (t[0], t[2], t[1]))
        out["Tier A points below 16.75"] = [list(p) for p in pass_a]
        h25 = [p[2] for p in pass_a if p[0].startswith("2/5")]
        out["2/5 passes: heights"] = [min(h25), max(h25)] if h25 else None
        out["2/5 passes outside 2.0-3.6"] = [list(p) for p in pass_a if p[0].startswith("2/5")
                                             and not WINDOW[0] <= p[2] <= WINDOW[1]]
        # Tier B
        bestb, argb, _upb, labb, _arrb = best_six(good_b, t6, sg)
        pass_b = {}
        for i, (k, x, y, hor) in enumerate(labb):
            if bestb[i] < BAR6:
                kk = (f"{L[k][0]},{L[k][1]}", x, y)
                pass_b[kk] = min(pass_b.get(kk, np.inf), float(bestb[i]))
        out["Tier B points below 16.75"] = [[p[0], p[1], p[2], v] for p, v in sorted(pass_b.items())]
        other = [p for p in pass_a if not p[0].startswith("2/5")]
        other += [list(p) for p in pass_b if not p[0].startswith("2/5,")]
        out["lines with a != 2/5 below 16.75"] = [list(p) for p in other]
        out["dropped nonzero channels (points)"] = sum(1 for r in good_a + good_b if r["dropped"] > 0)
        # the L check above Im tau 4: each class's best point above 4 at L x (1 +- 0.02)
        lchk = {}
        for c in ("0", "1/5", "2/5"):
            idx = [i for i, l in enumerate(lab) if cls(L[l[0]]) == c and l[2] > LTOP]
            ib = min(idx, key=lambda i: best[i])
            k, x, y, _hor = lab[ib]
            rr = pool.map(point, [(k, x, y, 0.98), (k, x, y, 1.02)])
            bb = [float(best_six([r], t6, sg)[0].min()) for r in rr if "failed" not in r]
            lchk[c] = {"point": [f"{L[k][0]},{L[k][1]}", x, y], "chi2_six": float(best[ib]), "at L x 0.98, 1.02": bb}
        out["L check above Im tau 4"] = lchk
    pred = {c: PRED[c][0] <= out["Tier A"][c]["up part at"][2] <= PRED[c][1] for c in PRED}
    out["K2 by class"] = pred
    out["cells"] = {
        "K0": bool(all(out["pins"].values()) and worst < 1e-6 and not failed and len(rows_k0) == 10),
        "K1": bool(not out["lines with a != 2/5 below 16.75"]),
        "K2": bool(all(pred.values()))}


if __name__ == "__main__":
    main()
