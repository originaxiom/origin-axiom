#!/usr/bin/env python3
"""W169 — the plan's stage 4, the state at the counted line (the rule: W169_RULE.md, committed and pushed before this
script).  W167's one-loop potential of the frame's own fields (W59's kernel), on the line (2/5, 1/10) whose T-orbit
X in [0, 5) covers the class (2/5, odd/10): at each of W158's 38 rows' heights, where does it hold Re tau?

  S0  controls: the T-step V(X + 1; (2/5, 1/10)) = V(X; (2/5, 1/2)), the period V(X + 5) = V(X), the mirror
      V(X) = V(2 - X)
  S1  the height runs to the cusp at the mirror's fixed points X = 1 and 3.5
  S2  the minimum over X at each row's height lies within 0.05 of the row's X (decisive)
  S3  the curvature in X at the minimum is at least 1e-4 of the curvature in y
  R   read-outs; the bosons' weight x2 and x5

    python3 -B docs/dossiers/the_weave_2026-10-07/the_state_at_the_counted_line.py
"""
import contextlib
import io
import json
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_line_potential_at_the_strip as W67   # noqa: E402  (W167: Kernel, FIELDS, psi_of, the rows)
T8 = W67.T8
OUT = HERE / "the_state_at_the_counted_line.json"
LINE = (Fr(2, 5), Fr(1, 10))
QS = (1, 2, 3, 4, 6)
GRID = 5000
PERIOD = 5.0
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def weights(beta=1.0):
    """per |q|: the frame's own content's signed weight, bosons times beta (W167's FIELDS)"""
    w = {q: 0.0 for q in QS}
    for (_nm, q, n, s) in W67.FIELDS:
        w[abs(q)] += n * s * (beta if s > 0 else 1.0)
    return w


def kq(X, y, line=LINE):
    """the five kernels k(|q| psi) at tau = X + i y on the line"""
    K = W67.Kernel(complex(X, y))
    ps = np.array(W67.psi_of(*line))
    return np.array([K.value(q * ps) for q in QS])


def V_of(X, y, w, line=LINE):
    return float(kq(X, y, line) @ np.array([w[q] for q in QS]))


def tdist5(a, b):
    d = (a - b) % PERIOD
    return min(d, PERIOD - d)


def row_X(r):
    b = Fr(r["line"][1])
    assert Fr(r["line"][0]) == Fr(2, 5)
    for j in range(5):
        if (Fr(1, 10) + Fr(2 * j, 5)) % 1 == b % 1:
            return r["Re_tau"] + j, j
    raise ValueError("row not on the class (2/5, odd/10)")


def minimum_over_X(y, w_list):
    """grid of GRID points on [0, 5), then a bounded scalar refinement around the grid's least, per weight set"""
    Xs = np.arange(GRID) * PERIOD / GRID
    table = np.array([kq(X, y) for X in Xs])
    out = []
    for w in w_list:
        wv = np.array([w[q] for q in QS])
        vals = table @ wv
        i = int(np.argmin(vals))
        lo, hi = Xs[i] - PERIOD / GRID, Xs[i] + PERIOD / GRID
        res = minimize_scalar(lambda X: V_of(X, y, w), bounds=(lo, hi), method="bounded",
                              options={"xatol": 1e-9})
        Xs_ = float(res.x % PERIOD)
        out.append({"X*": Xs_, "V*": float(res.fun), "grid least": float(vals[i]),
                    "V range on the grid": [float(vals.min()), float(vals.max())]})
    return out


def curvatures(X, y, w, h=1e-3):
    v0 = V_of(X, y, w)
    dxx = (V_of(X + h, y, w) - 2 * v0 + V_of(X - h, y, w)) / h ** 2
    dyy = (V_of(X, y + h, w) - 2 * v0 + V_of(X, y - h, w)) / h ** 2
    return float(dxx), float(dyy)


def run(root, out):
    L = T8.own_lines()
    rows = []
    for name, path in W67.ROWS_FROM.items():
        d = json.loads(T8.git_bytes(root, "HEAD", path).decode("utf-8"))
        for r in d["C1"]["rows"]:
            X, j = row_X(r)
            rows.append({"name": name, "line": r["line"], "x": r["Re_tau"], "y": r["Im_tau"], "X": X, "j": j})
    out["rows"] = len(rows)
    out["census lines (unused here)"] = len(L)
    w1, w2, w5 = weights(1), weights(2), weights(5)
    out["weights per |q| (bosons +)"] = {str(q): w1[q] for q in QS}
    # ---------------------------------------------------------------- S0
    rng = np.random.default_rng(169)
    s0 = {"T-step worst": 0.0, "period worst": 0.0, "mirror worst": 0.0}
    for r in rows[:3]:
        y = r["y"]
        for _ in range(10):
            X = float(rng.random() * PERIOD)
            v = V_of(X, y, w1)
            s0["T-step worst"] = max(s0["T-step worst"],
                                     abs(V_of(X + 1, y, w1) / V_of(X, y, w1, (Fr(2, 5), Fr(1, 2))) - 1))
            s0["period worst"] = max(s0["period worst"], abs(V_of(X + PERIOD, y, w1) / v - 1))
            s0["mirror worst"] = max(s0["mirror worst"], abs(V_of(2 - X, y, w1) / v - 1))
    out["S0"] = s0
    # ---------------------------------------------------------------- S1
    s1 = {}
    ys = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    for X in (1.0, 3.5):
        vals = [V_of(X, y, w1) for y in ys]
        s1[str(X)] = {"V at y = 2..8": vals, "decreasing": bool(all(b < a for a, b in zip(vals, vals[1:])))}
    out["S1"] = s1
    # ---------------------------------------------------------------- S2, S3, R per height
    heights = sorted({r["y"] for r in rows})
    by_y = {}
    t0 = time.time()
    for k, y in enumerate(heights):
        m1, m2, m5 = minimum_over_X(y, [w1, w2, w5])
        dxx, dyy = curvatures(m1["X*"], y, w1)
        by_y[y] = {"beta 1": m1, "beta 2": m2, "beta 5": m5, "d2V/dX2": dxx, "d2V/dy2": dyy}
        print(f"height {k + 1}/{len(heights)} at {time.time() - t0:.0f} s", flush=True)
    per_row = []
    for r in rows:
        h = by_y[r["y"]]
        Xs = h["beta 1"]["X*"]
        per_row.append({"row": [r["name"], r["line"], r["x"], r["y"]], "X_row": r["X"], "X*": Xs,
                        "|X* - X_row|": min(tdist5(Xs, r["X"]), tdist5(2 - Xs, r["X"])), "V*": h["beta 1"]["V*"],
                        "V(X_row) - V*": V_of(r["X"], r["y"], w1) - h["beta 1"]["V*"],
                        "d2V/dX2": h["d2V/dX2"], "d2V/dy2": h["d2V/dy2"],
                        "X* at bosons x2": h["beta 2"]["X*"], "X* at bosons x5": h["beta 5"]["X*"]})
    out["per row"] = per_row
    xs = [p["X*"] for p in per_row]
    out["R"] = {"X* over the heights, rounded": sorted({round(x, 4) for x in xs}),
                "X* at a fixed point of the mirror (1 or 3.5), rows": sum(1 for x in xs if min(tdist5(x, 1.0),
                                                                                              tdist5(x, 3.5)) < 1e-4),
                "least |X* - X_row|": min(p["|X* - X_row|"] for p in per_row),
                "largest |X* - X_row|": max(p["|X* - X_row|"] for p in per_row),
                "curvature ratio X over y, range": [min(abs(p["d2V/dX2"] / p["d2V/dy2"]) for p in per_row),
                                                    max(abs(p["d2V/dX2"] / p["d2V/dy2"]) for p in per_row)]}
    out["cells"] = {
        "S0": bool(max(s0.values()) < 1e-6),
        "S1": bool(all(v["decreasing"] for v in s1.values())),
        "S2": bool(all(p["|X* - X_row|"] < 0.05 for p in per_row)),
        "S3": bool(all(abs(p["d2V/dX2"]) >= 1e-4 * abs(p["d2V/dy2"]) for p in per_row))}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W169", "rule": "W169_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
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
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


if __name__ == "__main__":
    main()
