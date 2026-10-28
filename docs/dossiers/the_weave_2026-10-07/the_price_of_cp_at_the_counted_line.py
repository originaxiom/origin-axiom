#!/usr/bin/env python3
"""W172 — THE RIDDLE, horn 1 at the counted line (the rule: W172_RULE.md, committed and pushed before this script).
The mirror lemma; how firmly the frame's own one-loop potential holds Re tau on the line (2/5, 1/10)'s T-orbit; whether
any stated variation of the content breaks CP there; and the price of the data's Re tau.

  P0  V(-conj tau; psi1, -psi2) = V(tau; psi1, psi2) at 24 random points, s = 3 and 4, 1e-12 (control: psi2 kept)
  P1  at the 38 rows' heights: the X-amplitude below 1e-3 of |V*|, the X-curvature below 1e-3 of the y-curvature
  P2  every variation's global X-minimum at a mirror fixed point (1 or 3.5) within 1e-4, at every height
  P3  (V(X_row) - V*) / 2 below 1e-4 of |V*| at every row
  R   the X-profile's leading Fourier coefficients; s = 3 against s = 4; any off-point minimum

    python3 -B docs/dossiers/the_weave_2026-10-07/the_price_of_cp_at_the_counted_line.py
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
    import the_state_at_the_counted_line as W69       # noqa: E402  (W169: the line, its orbit, row_X, the rows)
W67, T8 = W69.W67, W69.T8
OUT = HERE / "the_price_of_cp_at_the_counted_line.json"
LINE = W69.LINE
QS = W69.QS
NLAT = 48
GRID = 5000
PERIOD = 5.0
BETAS = (0.5, 1.0, 2.0, 5.0, 10.0, 20.0)
SS = (3, 4)
SUBSETS = {"quarks": ("Q", "u", "d"), "leptons": ("L", "e"), "Higgs pair": ("H_u", "H_d")}
PARITIES = ((0.5, 0.0), (0.0, 0.5), (0.5, 0.5))
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


class KernelS:
    """W59's joint-parity kernel at general s: k(psi) = -Sum cw cos 2 pi (m psi1 + n psi2),
    cw = c_par y^s / |m + n tau|^2s"""

    def __init__(self, t, s, N=NLAT):
        m, n = np.meshgrid(np.arange(-N, N + 1), np.arange(-N, N + 1), indexing="ij")
        m, n = m.ravel().astype(float), n.ravel().astype(float)
        keep = (m != 0) | (n != 0)
        m, n = m[keep], n[keep]
        w = t.imag ** s / np.abs(m + n * t) ** (2 * s)
        c = sum(np.cos(2 * np.pi * (m * u + n * v)) for u, v in PARITIES)
        self.m, self.n, self.cw = m, n, c * w

    def value(self, ps):
        return float(-np.sum(self.cw * np.cos(2 * np.pi * (self.m * ps[0] + self.n * ps[1]))))


def weights(beta=1.0, names=None):
    """per |q|: the content's signed weight (W67's FIELDS), bosons times beta, restricted to names if given"""
    w = {q: 0.0 for q in QS}
    for (nm, q, n, s) in W67.FIELDS:
        if names is not None and nm not in names:
            continue
        w[abs(q)] += n * s * (beta if s > 0 else 1.0)
    return np.array([w[q] for q in QS])


def kq(X, y, s, psi):
    K = KernelS(complex(X, y), s)
    return np.array([K.value(q * np.asarray(psi)) for q in QS])


def tdist5(a, b):
    d = (a - b) % PERIOD
    return min(d, PERIOD - d)


def at_fixed_point(X, tol=1e-4):
    return min(tdist5(X, 1.0), tdist5(X, 3.5)) < tol


# ----------------------------------------------------------------------------------------------- P0
def part_P0():
    rng = np.random.default_rng(172)
    worst, ctrl_fail, n_ctrl, cross = 0.0, 0, 0, 0.0
    wv = weights(1.0)
    for _ in range(24):
        t = complex(rng.uniform(-1, 1), rng.uniform(1, 4))
        ps = (float(rng.random()), float(rng.random()))
        for s in SS:
            a = kq(t.real, t.imag, s, ps) @ wv
            b = kq(-t.real, t.imag, s, (ps[0], -ps[1])) @ wv
            c = kq(-t.real, t.imag, s, ps) @ wv
            worst = max(worst, abs(a - b) / abs(a))
            n_ctrl += 1
            ctrl_fail += abs(a - c) / abs(a) > 1e-6
        K3 = W67.Kernel(t)
        mine = KernelS(t, 3)
        cross = max(cross, max(abs(K3.value(q * np.asarray(ps)) - mine.value(q * np.asarray(ps)))
                               / max(1e-300, abs(K3.value(q * np.asarray(ps)))) for q in QS))
    return {"worst relative |V(tau) - V(mirror)|": worst,
            "control (psi2 kept) fails by > 1e-6": f"{ctrl_fail} of {n_ctrl}",
            "own s = 3 kernel against W167's, worst relative": cross,
            "holds": bool(worst < 1e-12 and ctrl_fail >= n_ctrl // 2 and cross < 1e-12)}


# ----------------------------------------------------------------------------------------------- the profiles
def profiles(heights):
    """per s and height: the table k_q(X) on the grid"""
    psi = np.asarray(W67.psi_of(*LINE))
    Xs = np.arange(GRID) * PERIOD / GRID
    tables = {}
    t0 = time.time()
    for s in SS:
        for k, y in enumerate(heights):
            tables[(s, y)] = np.array([kq(X, y, s, psi) for X in Xs])
            if k % 10 == 0:
                print(f"s = {s}, height {k + 1}/{len(heights)} at {time.time() - t0:.0f} s", flush=True)
    return Xs, tables, psi


def minimum(Xs, table, wv, y, s, psi):
    vals = table @ wv
    i = int(np.argmin(vals))
    lo, hi = Xs[i] - PERIOD / GRID, Xs[i] + PERIOD / GRID
    res = minimize_scalar(lambda X: float(kq(X, y, s, psi) @ wv), bounds=(lo, hi), method="bounded",
                          options={"xatol": 1e-9})
    return float(res.x % PERIOD), float(res.fun), vals


def curvatures(X, y, s, psi, wv, h=1e-3):
    v0 = kq(X, y, s, psi) @ wv
    dxx = (kq(X + h, y, s, psi) @ wv - 2 * v0 + kq(X - h, y, s, psi) @ wv) / h ** 2
    dyy = (kq(X, y + h, s, psi) @ wv - 2 * v0 + kq(X, y - h, s, psi) @ wv) / h ** 2
    return float(dxx), float(dyy)


def run(root, out):
    out["P0"] = part_P0()
    print("P0 done", flush=True)
    rows = []
    for name, path in W67.ROWS_FROM.items():
        d = json.loads(T8.git_bytes(root, "HEAD", path).decode("utf-8"))
        for r in d["C1"]["rows"]:
            X, j = W69.row_X(r)
            rows.append({"name": name, "line": r["line"], "x": r["Re_tau"], "y": r["Im_tau"], "X": X})
    heights = sorted({r["y"] for r in rows})
    out["rows"], out["heights"] = len(rows), len(heights)
    Xs, tables, psi = profiles(heights)
    variations = {}
    for s in SS:
        for b in BETAS:
            variations[f"full content, s = {s}, bosons x{b}"] = (s, weights(b))
    for nm, names in SUBSETS.items():
        variations[f"{nm} alone, s = 3"] = (3, weights(1.0, names))
    # ---------------------------------------------------------------- P1 and R at the base content
    base = weights(1.0)
    per_h, p1_ok = {}, True
    for y in heights:
        Xm, Vm, vals = minimum(Xs, tables[(3, y)], base, y, 3, psi)
        dxx, dyy = curvatures(Xm, y, 3, psi, base)
        amp = float(vals.max() - vals.min())
        F = np.fft.rfft(vals) / GRID
        per_h[y] = {"X*": Xm, "V*": Vm, "amplitude": amp, "amplitude / |V*|": amp / abs(Vm),
                    "d2V/dX2": dxx, "d2V/dy2": dyy, "curvature ratio": abs(dxx / dyy),
                    "Fourier |c_k| / |V*|, k = 1..6 (period 5)": [float(abs(F[k]) * 2 / abs(Vm)) for k in range(1, 7)]}
        p1_ok &= amp / abs(Vm) < 1e-3 and abs(dxx / dyy) < 1e-3
    out["P1"] = {"per height": {f"{y:.6f}": v for y, v in per_h.items()},
                 "largest amplitude / |V*|": max(v["amplitude / |V*|"] for v in per_h.values()),
                 "largest curvature ratio": max(v["curvature ratio"] for v in per_h.values()),
                 "holds": bool(p1_ok)}
    # ---------------------------------------------------------------- P2
    p2, off = {}, []
    for name, (s, wv) in variations.items():
        xs = []
        for y in heights:
            Xm, Vm, _ = minimum(Xs, tables[(s, y)], wv, y, s, psi)
            xs.append(Xm)
            if not at_fixed_point(Xm):
                near = min(min(tdist5(Xm, r["X"]), tdist5(2 - Xm, r["X"])) for r in rows if r["y"] == y)
                off.append({"variation": name, "height": y, "X*": Xm,
                            "distance to the nearest row's X (mirror-aware)": near})
        p2[name] = {"X* rounded, distinct": sorted({round(x, 4) for x in xs}),
                    "at a fixed point": sum(at_fixed_point(x) for x in xs)}
    out["P2"] = {"per variation": p2, "off-point minima": off, "holds": bool(not off)}
    # ---------------------------------------------------------------- P3
    p3, worst = [], 0.0
    for r in rows:
        y = r["y"]
        Vm = per_h[y]["V*"]
        vr = float(kq(r["X"], y, 3, psi) @ base)
        price = (vr - Vm) / 2 / abs(Vm)
        worst = max(worst, price)
        p3.append({"row": [r["name"], r["line"], r["x"], y], "X_row": r["X"], "V(X_row) - V*": vr - Vm,
                   "price (lower bound) / |V*|": price})
    out["P3"] = {"per row": p3, "largest price": worst, "holds": bool(worst < 1e-4)}
    # ---------------------------------------------------------------- R: s = 3 against s = 4 at the base weights
    cmp_ = {}
    for y in heights[:: max(1, len(heights) // 6)]:
        v3 = tables[(3, y)] @ base
        v4 = tables[(4, y)] @ base
        a3, a4 = v3 - v3.mean(), v4 - v4.mean()
        cmp_[f"{y:.6f}"] = {"correlation of the X-profiles": float(a3 @ a4 / np.sqrt((a3 @ a3) * (a4 @ a4))),
                            "X* (s = 3, s = 4)": [float(Xs[np.argmin(v3)]), float(Xs[np.argmin(v4)])]}
    out["R"] = {"s = 3 against s = 4": cmp_}
    out["cells"] = {k: out[k]["holds"] for k in ("P0", "P1", "P2", "P3")}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W172", "rule": "W172_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
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
