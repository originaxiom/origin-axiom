#!/usr/bin/env python3
"""W173 — THE RIDDLE, horn 3 at the record's best rows (the rule: W173_RULE.md, committed and pushed before this
script). At W158's 38 strip rows, on B1726's own instrument as this seat rebuilt it (own_point): the six decomposed as
f_i = -2 pi y e_i + P_i (local exponents from a central difference in Im tau, h = 0.01), the six swept over Re tau on
the line's T-orbit (60 points over a period of 5), and at four rows every census line at the row's tau.

  Q0  the own frame's chi2_six reproduces each stored row's to 1e-6 relative
  Q1  at every row some feature sweeps more than 10 sigma over Re tau
  Q2  at every row some |P_i| > ln 3 (decisive: the forced exponents with one height do not carry the six)
  R   e_i, P_i, the data's own exponents, the height's sensitivity, the CKM's sweep, the line sweep

    python3 -B docs/dossiers/the_weave_2026-10-07/the_fit_at_the_rows.py
"""
import contextlib
import io
import json
import math
import multiprocessing as mpc
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_from_the_action as W66      # noqa: E402  (W166: the frame, the rows' lists, the targets' modules)
T8, W58, T42 = W66.T8, W66.W58, W66.T42
OUT = HERE / "the_fit_at_the_rows.json"
H = 0.01
NX = 60
PERIOD = 5.0
LN3 = math.log(3)
WORKERS = 4
_ROOT = {}
_F = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def _init(root_str):
    with contextlib.redirect_stdout(io.StringIO()):
        col, _sha, W93, W89, L = W66.frame(Path(root_str))
    _F.update(col=col, W93=W93, W89=W89)


def _point(task):
    line, x, y = task
    o, _d = T8.own_point(_F["W93"], _F["W89"], _F["col"], (Fr(line[0]), Fr(line[1])), x, y)
    return o


def six_of(o, rd=("St", "S", "S"), c=3):
    v = np.log(np.array(o[f"up|L_max|{rd[0]}"] + o[f"down|L_max|{rd[1]}"] + o[f"lep|L_max|{rd[2]}"]))
    return v + np.array([0, 0, 0, 0, math.log(c), -math.log(c)])


def run(root, out, pool):
    rows = []
    for name, path in W66.ROWS_FROM.items():
        d = json.loads(T8.git_bytes(root, "HEAD", path).decode("utf-8"))
        for r in d["C1"]["rows"]:
            rows.append({"name": name, "line": r["line"], "x": r["Re_tau"], "y": r["Im_tau"], "hor": r["horocycle"],
                         "rd": r["readings"], "c": r["c"], "stored chi2_six": r["chi2_six"]})
    out["rows"] = len(rows)
    out["row settings"] = sorted({(r["hor"], tuple(r["rd"]), r["c"]) for r in rows})
    files = {p: T8.git_bytes(root, W58.REV, p) for p in W58.FILES}
    t6, _t9 = T8.targets(files)
    sg = np.array(T42.sigma(files))
    t6 = np.array(t6)
    # ---------------------------------------------------------------- the tasks
    tasks = []
    for r in rows:
        tasks += [(tuple(r["line"]), r["x"], r["y"]), (tuple(r["line"]), r["x"], r["y"] - H),
                  (tuple(r["line"]), r["x"], r["y"] + H)]
        tasks += [(tuple(r["line"]), r["x"] + PERIOD * k / NX, r["y"]) for k in range(NX)]
    best4 = sorted(range(len(rows)), key=lambda i: rows[i]["stored chi2_six"])
    pick = [i for i in best4 if rows[i]["name"] == "B1749"][:2] + [i for i in best4 if rows[i]["name"] == "B1753"][:2]
    lines = T8.own_lines()
    for i in pick:
        tasks += [((str(a), str(b)), rows[i]["x"], rows[i]["y"]) for (a, b) in lines]
    t0 = time.time()
    res = {}
    for k, o in enumerate(pool.imap(_point, tasks, chunksize=4)):
        res[tasks[k]] = o
        if k % 400 == 0:
            print(f"point {k + 1}/{len(tasks)} at {time.time() - t0:.0f} s", flush=True)
    # ---------------------------------------------------------------- per row
    per, q0, q1, q2 = [], True, True, True
    for r in rows:
        ln = tuple(r["line"])
        rd, c = tuple(r["rd"]), r["c"]
        f0 = six_of(res[(ln, r["x"], r["y"])], rd, c)
        fm = six_of(res[(ln, r["x"], r["y"] - H)], rd, c)
        fp = six_of(res[(ln, r["x"], r["y"] + H)], rd, c)
        d1 = (fp - fm) / (2 * H)
        e = -d1 / (2 * math.pi)
        P = f0 - r["y"] * d1
        chi = float((((f0 - t6) / sg) ** 2).sum())
        dchi = float(((((fp - t6) / sg) ** 2).sum() - (((fm - t6) / sg) ** 2).sum()) / (2 * H))
        sweep = np.array([six_of(res[(ln, r["x"] + PERIOD * k / NX, r["y"])], rd, c) for k in range(NX)])
        chis = (((sweep - t6) / sg) ** 2).sum(axis=1)
        span_sigma = (sweep.max(axis=0) - sweep.min(axis=0)) / sg
        ck = np.array([res[(ln, r["x"] + PERIOD * k / NX, r["y"])][f"ckm|L_max|{rd[0]}|{rd[1]}"][:3]
                       for k in range(NX)])
        rel = abs(chi - r["stored chi2_six"]) / r["stored chi2_six"]
        q0 &= rel < 1e-6
        q1 &= bool(span_sigma.max() > 10)
        q2 &= bool(np.abs(P).max() > LN3)
        per.append({"row": [r["name"], r["line"], r["x"], r["y"]],
                    "chi2_six (own, stored)": [chi, r["stored chi2_six"]],
                    "six": f0.tolist(), "targets": t6.tolist(), "local exponents e_i": e.tolist(),
                    "intercepts P_i": P.tolist(), "exponent parts -2 pi y e_i": (-2 * math.pi * r["y"] * e).tolist(),
                    "the data's own exponents -d_i/(2 pi y)": (-t6 / (2 * math.pi * r["y"])).tolist(),
                    "largest |P_i|": float(np.abs(P).max()),
                    "Re tau sweep: each feature's span in sigma": span_sigma.tolist(),
                    "Re tau sweep: chi2_six range": [float(chis.min()), float(chis.max())],
                    "Re tau sweep: least chi2_six at Re tau": float(r["x"] + PERIOD * int(np.argmin(chis)) / NX),
                    "d chi2_six / d Im tau": dchi,
                    "Im tau step for a change of 10 (linear)": 10 / max(abs(dchi), 1e-300),
                    "CKM moduli over Re tau: min, max": [ck.min(axis=0).tolist(), ck.max(axis=0).tolist()]})
    out["per row"] = per
    out["Q0"] = {"worst relative": max(abs(p["chi2_six (own, stored)"][0] - p["chi2_six (own, stored)"][1])
                                       / p["chi2_six (own, stored)"][1] for p in per), "holds": bool(q0)}
    out["Q1"] = {"least of the rows' largest span (sigma)": min(max(p["Re tau sweep: each feature's span in sigma"])
                                                                for p in per), "holds": bool(q1)}
    out["Q2"] = {"least of the rows' largest |P_i|": min(p["largest |P_i|"] for p in per),
                 "rows with every |P_i| <= ln 3": [p["row"] for p in per if p["largest |P_i|"] <= LN3],
                 "holds": bool(q2)}
    # ---------------------------------------------------------------- the line sweep (read-out)
    lsw = []
    for i in pick:
        r = rows[i]
        rd, c = tuple(r["rd"]), r["c"]
        vals = []
        for (a, b) in lines:
            f = six_of(res[((str(a), str(b)), r["x"], r["y"])], rd, c)
            vals.append((float((((f - t6) / sg) ** 2).sum()), [str(a), str(b)], f))
        arr = np.array([v[2] for v in vals])
        order = sorted(vals, key=lambda v: v[0])
        lsw.append({"row": [r["name"], r["line"], r["x"], r["y"]],
                    "least chi2_six over lines and its line": [order[0][0], order[0][1]],
                    "lines with chi2_six < 16.75": [[v[1], v[0]] for v in order if v[0] < 16.75],
                    "each feature's spread over lines (sigma)": ((arr.max(axis=0) - arr.min(axis=0)) / sg).tolist()})
    out["R"] = {"line sweep at four rows": lsw}
    out["cells"] = {k: out[k]["holds"] for k in ("Q0", "Q1", "Q2")}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W173", "rule": "W173_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
           "python": sys.version.split()[0], "numpy": np.__version__, "machine": platform.machine(),
           "workers": WORKERS}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=_init, initargs=(str(root),)) as pool:
                run(root, out, pool)
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


if __name__ == "__main__":
    main()
