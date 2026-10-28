#!/usr/bin/env python3
"""W175 — THE RIDDLE's horn 1 off the mirror (the rule: W175_RULE.md, committed and pushed before this script). The
web seat's question 1: the frame's own one-loop potential (W172's kernel and content) on the slope-2/5 line classes
that have no mirror-fixed point above Im tau = 1 (orders 15-30), with the order-10 and order-5 classes as controls.

  C0  the criterion: a mirror-fixed point on the T-orbit above Im tau = 1 iff the order divides 10 (exact, order <= 60)
  C1  each mirror pair's X-profiles agree reflected, 1e-6 relative, at every height
  C2  |J| at the X-minimum > 1e-8 on every mirror-free class and height; < 1e-12 on the controls (decisive)
  C3  the X-amplitude below 1e-3 of |V*| everywhere
  C4  dV/dy > 0 at the X-minimum everywhere
  R   X*, |J| and signs, the consistency check, the two-dimensional least, |J| against the measured J (one look)

    python3 -B docs/dossiers/the_weave_2026-10-07/the_potential_off_the_mirror.py
"""
import contextlib
import io
import json
import math
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.optimize import minimize, minimize_scalar

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_price_of_cp_at_the_counted_line as W72   # noqa: E402  (W172: the kernel at general s, the content)
    import the_higgs_from_the_action as W66             # noqa: E402  (W166: the frame for own_point)
W67, T8 = W72.W67, W72.T8
OUT = HERE / "the_potential_off_the_mirror.json"
A = Fr(2, 5)
FREE = {15: (Fr(1, 15), Fr(2, 15)), 20: (Fr(1, 20), Fr(3, 20)), 25: (Fr(1, 25), Fr(2, 25), Fr(3, 25), Fr(4, 25)),
        30: (Fr(1, 30), Fr(1, 6))}
PAIRS = ((Fr(1, 15), Fr(2, 15)), (Fr(1, 20), Fr(3, 20)), (Fr(1, 25), Fr(4, 25)), (Fr(2, 25), Fr(3, 25)),
         (Fr(1, 30), Fr(1, 6)))
CONTROLS = (Fr(1, 10), Fr(0))
HEIGHTS = (1.5, 2.0, 2.5, 3.0, 3.5)
NX = 1000
PERIOD = 5.0
S = 3
KEY = "ckm|L_max|St|S"
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def order(a, b):
    return math.lcm(a.denominator, b.denominator)


# ============================================================================================ C0
def fixed_point_direct(b):
    """does some X in (1/2)Z, 0 <= X < 5, have (-X, -b) ~ (X, b) under (tau + k, b) ~ (tau, b + k a)?"""
    for twoX in range(10):
        X = Fr(twoX, 2)
        k = -2 * X                      # -X = X + k
        if (-b + k * A - b) % 1 == 0:
            return True
    return False


def part_C0():
    rows, bad = 0, []
    for d in range(1, 61):
        for j in range(d):
            b = Fr(j, d)
            if b.denominator != d:
                continue
            n = order(A, b)
            if n > 60:
                continue
            rows += 1
            if fixed_point_direct(b) != (10 % n == 0):
                bad.append([str(b), n])
    return {"lines checked": rows, "disagreements": bad, "holds": not bad}


# ============================================================================================ the potential
def profile(b, y, wv):
    psi = np.asarray(W67.psi_of(A, b))
    Xs = np.arange(NX) * PERIOD / NX
    vals = np.array([W72.kq(X, y, S, psi) @ wv for X in Xs])
    return Xs, vals, psi


def x_minimum(b, y, wv):
    Xs, vals, psi = profile(b, y, wv)
    i = int(np.argmin(vals))
    res = minimize_scalar(lambda X: float(W72.kq(X, y, S, psi) @ wv),
                          bounds=(Xs[i] - PERIOD / NX, Xs[i] + PERIOD / NX), method="bounded", options={"xatol": 1e-9})
    Xm, Vm = float(res.x % PERIOD), float(res.fun)
    dxx, dyy = W72.curvatures(Xm, y, S, psi, wv)
    h = 1e-3
    dy = float((W72.kq(Xm, y + h, S, psi) @ wv - W72.kq(Xm, y - h, S, psi) @ wv) / (2 * h))
    return {"X*": Xm, "V*": Vm, "amplitude / |V*|": float((vals.max() - vals.min()) / abs(Vm)),
            "X-curvature / y-curvature": float(dxx / dyy) if dyy else None, "dV/dy": dy}, vals


def two_d(b, wv):
    psi = np.asarray(W67.psi_of(A, b))
    Xs = np.arange(200) * PERIOD / 200
    Ys = np.round(np.arange(1.2, 4.0001, 0.05), 4)
    grid = np.array([[W72.kq(X, y, S, psi) @ wv for X in Xs] for y in Ys])
    i, j = np.unravel_index(int(np.argmin(grid)), grid.shape)
    res = minimize(lambda v: float(W72.kq(v[0], v[1], S, psi) @ wv), x0=[Xs[j], Ys[i]], method="L-BFGS-B",
                   bounds=[(Xs[j] - 0.05, Xs[j] + 0.05), (1.2, 4.0)])
    X, yv = float(res.x[0] % PERIOD), float(res.x[1])
    return {"least at (X, Im tau)": [X, yv], "V": float(res.fun), "on the lower edge": bool(yv < 1.2 + 1e-6),
            "grid least at": [float(Xs[j]), float(Ys[i])]}


def run(root, out):
    out["C0"] = part_C0()
    with contextlib.redirect_stdout(io.StringIO()):
        col, _sha, W93, W89, _L = W66.frame(root)
    wv = W72.weights(1.0)
    classes = [b for n in FREE for b in FREE[n]] + list(CONTROLS)
    per, prof = {}, {}
    t0 = time.time()
    for b in classes:
        rec = {"order": order(A, b), "mirror-free": b not in CONTROLS, "per height": {}}
        for y in HEIGHTS:
            m, vals = x_minimum(b, y, wv)
            prof[(b, y)] = vals
            Xm = m["X*"]
            o, _d = T8.own_point(W93, W89, col, (A, b), Xm, y)
            m["J"] = float(o[KEY][3])
            j = int(math.floor(Xm))
            o2, _d2 = T8.own_point(W93, W89, col, (A, (b + j * A) % 1), Xm - j, y)
            m["J by the shifted line"] = float(o2[KEY][3])
            rec["per height"][str(y)] = m
        rec["two-dimensional"] = two_d(b, wv)
        per[str(b)] = rec
        print(f"class {b} done at {time.time() - t0:.0f} s", flush=True)
    out["per class"] = per
    # C1: the mirror pairs, reflected
    c1 = []
    for b1, b2 in PAIRS:
        for y in HEIGHTS:
            v1, v2 = prof[(b1, y)], prof[(b2, y)]
            best = min(((float(np.max(np.abs(v1 - np.roll(v2[::-1], c)))) / float(np.max(np.abs(v1))), c)
                        for c in range(NX)))
            j1 = per[str(b1)]["per height"][str(y)]["J"]
            j2 = per[str(b2)]["per height"][str(y)]["J"]
            c1.append({"pair": [str(b1), str(b2)], "height": y, "relative misfit": best[0],
                       "shift (grid steps after reversal)": best[1], "J signs": [math.copysign(1, j1),
                                                                                  math.copysign(1, j2)]})
    out["C1"] = {"per pair and height": c1, "worst": max(r["relative misfit"] for r in c1),
                 "holds": bool(max(r["relative misfit"] for r in c1) < 1e-6)}
    # C2
    jf = [abs(per[str(b)]["per height"][str(y)]["J"]) for b in classes if b not in CONTROLS for y in HEIGHTS]
    jc = [abs(per[str(b)]["per height"][str(y)]["J"]) for b in CONTROLS for y in HEIGHTS]
    out["C2"] = {"least |J| on the mirror-free classes": min(jf), "largest |J| on the controls": max(jc),
                 "holds": bool(min(jf) > 1e-8 and max(jc) < 1e-12)}
    amp = [per[str(b)]["per height"][str(y)]["amplitude / |V*|"] for b in classes for y in HEIGHTS]
    out["C3"] = {"largest amplitude / |V*|": max(amp), "holds": bool(max(amp) < 1e-3)}
    dys = [per[str(b)]["per height"][str(y)]["dV/dy"] for b in classes for y in HEIGHTS]
    out["C4"] = {"least dV/dy": min(dys), "holds": bool(min(dys) > 0)}
    cons = [abs(per[str(b)]["per height"][str(y)]["J"] - per[str(b)]["per height"][str(y)]["J by the shifted line"])
            for b in classes for y in HEIGHTS]
    jp = W66.W61.J_PDG
    out["R"] = {"consistency: largest |J - J(shifted line)|": max(cons),
                "|J| at the minima over the measured J (one look)": {
                    str(b): [abs(per[str(b)]["per height"][str(y)]["J"]) / jp for y in HEIGHTS]
                    for b in classes if b not in CONTROLS},
                "measured J used": jp}
    out["cells"] = {k: out[k]["holds"] for k in ("C0", "C1", "C2", "C3", "C4")}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W175", "rule": "W175_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
           "python": sys.version.split()[0], "numpy": np.__version__, "machine": platform.machine()}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            run(root, out)
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("done" if "run_failed" not in out else "run failed")


if __name__ == "__main__":
    main()
