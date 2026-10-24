#!/usr/bin/env python3
"""W154 — the census over contents, Stage A (the rule: W154_RULE.md, committed and pushed before this script).

Every content that weights the three parities alike, at the forced line, has V = -(A E(tau, 3) + B E(tau, 2)) with
A = w0 - (15/16) wp - (31/1024) wrho and B = (31/1024) wrho (B1686's and B1704's units; the matter by PH2's shape).
Main's B1686 functions (E_cs, S_c, copies) are read with git show from 22b7d5739, as the B1704 mirror check did. The
domain scans use a vectorized copy of the same Chowla-Selberg formula, checked against main's E_cs (C0).

  C0  the reduction: sum of S_c over the three parities = -(15/16) E(tau, 3); contents sector by sector = A E3 + B E2;
      the cusp coefficient 2A against B1686's matter alone (5.449); the vectorized E against main's E_cs
  C1  the regimes over SL(2, Z)'s fundamental domain: A > 0 runs; A = 0; A < 0 with B <= 0 at omega; A < 0 with
      B > 0: the global minimum on the axis for t = B/|A| from 3.2 to 16, increasing, against the asymptotic t(y)
  C2  the band 2.1 <= y* <= 3.2 as a t-window, and the content condition it implies
  C3  the rows: the record's contents at the forced line and E8's 248 (two units); the extra rho_Q scalars for the band
  C4  B1704's content (a) at the line (1/2, 1/2) plus n complex scalars in rho_Q: the axis minimum at n = 89 and 95
  R   read-outs: t_c and the minimum's path below 3.2; curvatures across the axis; PH2's 1% sensitivity; SUSY pairing

    python3 -B the_content_census.py      # writes the_content_census.json beside itself
"""
import contextlib
import importlib.util
import io
import json
import math
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from mpmath import gamma as mgamma, zeta as mzeta
from scipy.optimize import minimize_scalar
from scipy.special import kv

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / "the_content_census.json"
MAIN = "22b7d5739"
FILE = "frontier/B1686_w60_w62_on_main/verification/main_w62.py"
tmp = Path(tempfile.mkdtemp())
(tmp / "main_w62.py").write_text(subprocess.run(["git", "show", f"{MAIN}:{FILE}"], cwd=ROOT, check=True,
                                                capture_output=True, text=True).stdout)
spec = importlib.util.spec_from_file_location("main_w62", tmp / "main_w62.py")
W = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(W)

K31 = 31 / 1024
PAR = [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]
OMEGA = complex(-0.5, math.sqrt(3) / 2)
Z6, Z4 = math.pi ** 6 / 945, math.pi ** 4 / 90
CC3 = float(2 * math.sqrt(math.pi) * mgamma(2.5) * mzeta(5) / mgamma(3))     # the y^(1-s) coefficients of E3, E2
CC2 = float(2 * math.sqrt(math.pi) * mgamma(1.5) * mzeta(3) / mgamma(2))


# ------------------------------------------------------------------ the basis, vectorized
def sigma(k, a):
    return sum(d ** a for d in range(1, k + 1) if k % d == 0)


def E_vec(x, y, s, K=30):
    """Chowla-Selberg, the formula of main's E_cs, on arrays"""
    x, y = np.asarray(x, float), np.asarray(y, float)
    tot = 2 * float(mzeta(2 * s)) * y ** s + 2 * math.sqrt(math.pi) * float(mgamma(s - 0.5)) * float(mzeta(2 * s - 1)) \
        * y ** (1 - s) / float(mgamma(s))
    acc = np.zeros_like(y)
    for k in range(1, K + 1):
        acc = acc + k ** (s - 0.5) * sigma(k, 1 - 2 * s) * kv(s - 0.5, 2 * math.pi * k * y) \
            * np.cos(2 * math.pi * k * x)
    return tot + 8 * math.pi ** s * np.sqrt(y) / float(mgamma(s)) * acc


def fourier(x, y, s, K=30):
    """the x-dependent part of E(tau, s) alone, so that differences in x are computed without cancellation"""
    acc = 0.0
    for k in range(1, K + 1):
        acc = acc + k ** (s - 0.5) * sigma(k, 1 - 2 * s) * kv(s - 0.5, 2 * math.pi * k * y) \
            * math.cos(2 * math.pi * k * x)
    return 8 * math.pi ** s * math.sqrt(y) / float(mgamma(s)) * acc


def x_rises(a, b, y):
    """V(x, y) - V(0, y) for V = -(a E3 + b E2), from the Fourier parts, at x = 0.1, 0.25, 0.4, 0.5"""
    d = [-(a * (fourier(x, y, 3) - fourier(0, y, 3)) + b * (fourier(x, y, 2) - fourier(0, y, 2)))
         for x in (0.1, 0.25, 0.4, 0.5)]
    return all(v > 0 for v in d), d


def E3(x, y):
    return E_vec(x, y, 3)


def E2(x, y):
    return E_vec(x, y, 2)


def t_formula(y):
    return (6 * Z6 * y ** 2 - 2 * CC3 / y ** 3) / (4 * Z4 * y - CC2 / y ** 2)


def y_formula(t):
    lo, hi = 1.5, 40.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_formula(mid) < t else (lo, mid)
    return (lo + hi) / 2


def AB(w0, wp, wr):
    return w0 - 15 / 16 * wp - K31 * wr, K31 * wr


# ------------------------------------------------------------------ the grid on the fundamental domain
XS = np.round(np.arange(-0.5, 0.50001, 0.01), 4)
YS = np.round(np.arange(0.86, 14.00001, 0.01), 4)
GX, GY = np.meshgrid(XS, YS, indexing="ij")
MASK = GX ** 2 + GY ** 2 >= 1 - 1e-12
G3 = np.where(MASK, E3(GX, GY), np.nan)
G2 = np.where(MASK, E2(GX, GY), np.nan)
SPECIAL = {"i": (0.0, 1.0), "omega": (OMEGA.real, OMEGA.imag)}


def grid_argmin(a, b):
    """the global minimum of V = -(a E3 + b E2) on the grid and at i and omega"""
    V = -(a * G3 + b * G2)
    k = np.nanargmin(V)
    i, j = np.unravel_index(k, V.shape)
    best = (float(V[i, j]), float(GX[i, j]), float(GY[i, j]))
    for name, (x, y) in SPECIAL.items():
        v = float(-(a * E3(x, y) + b * E2(x, y)))
        if v < best[0]:
            best = (v, x, y)
    return best


def axis_min(a, b, y0, half=0.5):
    f = lambda y: float(-(a * E3(0.0, y) + b * E2(0.0, y)))
    r = minimize_scalar(f, bounds=(max(1.0, y0 - half), y0 + half), method="bounded", options={"xatol": 1e-10})
    return float(r.x), float(r.fun)


# ------------------------------------------------------------------ C0
def C0():
    rng = np.random.default_rng(154)
    taus = [complex(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 3.0)) for _ in range(10)]
    taus = [t if abs(t) >= 1 else t + 1j for t in taus]
    rows = []
    for M in (60, 120):
        err = max(abs(sum(W.S_c(t, p, M=M) for p in PAR) + 15 / 16 * W.E_cs(t, 3)) / abs(W.E_cs(t, 3)) for t in taus)
        rows.append({"M": M, "max relative error": err})
        if err <= 1e-10:
            break
    par_ok = rows[-1]["max relative error"] <= 1e-10
    cont_err = 0.0
    for _ in range(10):
        w0, wp, wr = (int(v) for v in rng.integers(-200, 201, size=3))
        A, B = AB(w0, wp, wr)
        for t in taus[:3]:
            F_sec = w0 * W.E_cs(t, 3) + wp * sum(W.S_c(t, p, M=rows[-1]["M"]) for p in PAR) \
                + wr * (-K31) * (W.E_cs(t, 3) - W.E_cs(t, 2))
            F_red = A * W.E_cs(t, 3) + B * W.E_cs(t, 2)
            cont_err = max(cont_err, abs(F_sec - F_red) / (abs(w0) + abs(wp) + abs(wr)) / abs(W.E_cs(t, 3)))
    vec_err = max(max(abs(E3(t.real, t.imag) - W.E_cs(t, 3)) / W.E_cs(t, 3),
                      abs(E2(t.real, t.imag) - W.E_cs(t, 2)) / W.E_cs(t, 2)) for t in taus + [OMEGA, 1j])
    A_m, _ = AB(0, 0, -90)
    ch = {"the parity sum is -(15/16) E(tau, 3) to 1e-10 relative": bool(par_ok),
          "contents sector by sector equal A E3 + B E2 to 1e-10 relative": bool(cont_err <= 1e-10),
          "the cusp coefficient 2A reproduces B1686's matter alone, 5.449": abs(2 * A_m - 5.449) < 5e-4,
          "instrument: the vectorized E matches main's E_cs to 1e-12": bool(vec_err <= 1e-12)}
    return {"checks": ch, "parity sum": rows, "content error": cont_err, "vectorized E error": vec_err,
            "2A, matter alone": 2 * A_m}, all(ch.values())


# ------------------------------------------------------------------ C1
def runs(a, b):
    vals = [float(-(a * E3(0.0, y) + b * E2(0.0, y))) for y in (8, 10, 12, 14)]
    return all(vals[k + 1] < vals[k] for k in range(3)), vals


def near_omega(x, y, tol=0.02):
    return abs(complex(x, y) - OMEGA) < tol or abs(complex(x, y) - (OMEGA + 1)) < tol


def C1():
    reg = {}
    reg["(i) A > 0"] = {str(r): runs(1.0, r)[0] for r in (-5.0, -1.0, 0.0, 1.0, 5.0)}
    reg["(ii) A = 0, B > 0 runs"] = runs(0.0, 1.0)[0]
    v, x, y = grid_argmin(0.0, -1.0)
    reg["(ii) A = 0, B < 0 at omega"] = bool(near_omega(x, y))
    reg["(iii) A < 0, B <= 0 at omega"] = {}
    for s in (0.0, 0.5, 1.0, 5.0, 20.0):
        v, x, y = grid_argmin(-1.0, -s)
        reg["(iii) A < 0, B <= 0 at omega"][str(s)] = bool(near_omega(x, y))
    ts = np.round(np.arange(0.05, 16.0001, 0.05), 4)
    curve, ok_axis, ok_below, ok_formula = [], True, True, True
    vi = lambda t: float(E3(0.0, 1.0) - t * E2(0.0, 1.0))
    vo = lambda t: float(E3(OMEGA.real, OMEGA.imag) - t * E2(OMEGA.real, OMEGA.imag))
    for t in ts:
        v, x, y = grid_argmin(-1.0, float(t))
        row = {"t": float(t), "grid": [x, y, v]}
        if t >= 3.2 - 1e-9:
            ya, va = axis_min(-1.0, float(t), y)
            rises, d = x_rises(-1.0, float(t), ya)
            row["axis"] = [ya, va]
            row["V(x) - V(0) at x = 0.1, 0.25, 0.4, 0.5"] = d
            ok_axis &= abs(y - ya) < 0.02 and va <= v + 1e-9 * abs(v) and rises
            ok_below &= va < vi(t) and va < vo(t)
            if ya >= 2:
                row["formula"] = y_formula(float(t))
                ok_formula &= abs(ya - row["formula"]) < 1e-3
        curve.append(row)
    band = [r["axis"][0] for r in curve if "axis" in r]
    increasing = all(band[k + 1] > band[k] for k in range(len(band) - 1))
    asym = [r["axis"][0] * math.pi ** 2 / (7 * r["t"]) for r in curve if r["t"] in (8.0, 12.0, 16.0)]
    ch = {"(i) A > 0 runs to the cusp for every B tried": all(reg["(i) A > 0"].values()),
          "(ii) A = 0: B > 0 runs, B < 0 at omega": bool(reg["(ii) A = 0, B > 0 runs"]
                                                         and reg["(ii) A = 0, B < 0 at omega"]),
          "(iii) A < 0, B <= 0: the global minimum at omega": all(reg["(iii) A < 0, B <= 0 at omega"].values()),
          "(iv) t from 3.2 to 16: the global minimum on the imaginary axis": bool(ok_axis),
          "(iv) V(y*) below V(i) and V(omega)": bool(ok_below),
          "(iv) y*(t) increasing": bool(increasing),
          "(iv) the asymptotic t(y) to 1e-3 in y for y >= 2": bool(ok_formula)}
    return {"checks": ch, "regimes": reg, "curve": curve, "y* pi^2 / 7t at t = 8, 12, 16": asym}, all(ch.values())


# ------------------------------------------------------------------ C2
def t_for_y(target, lo=2.5, hi=6.0):
    for _ in range(60):
        mid = (lo + hi) / 2
        y, _ = axis_min(-1.0, mid, y_formula(mid), half=1.0)
        lo, hi = (mid, hi) if y < target else (lo, mid)
    return (lo + hi) / 2


def C2():
    t1, t2 = t_for_y(2.1), t_for_y(3.2)
    r1, r2 = 1 - 1 / t1, 1 - 1 / t2
    dom = (1 / (K31 * r2), 1 / (K31 * r1))
    width = (r2 - r1) / ((r1 + r2) / 2)
    w0, wp, wr = 22, 0, 1000
    A, B = AB(w0, wp, wr)
    v, x, y = grid_argmin(A, B)
    yr, vr = axis_min(A, B, y)
    rises, _ = x_rises(A, B, yr)
    ch = {"t1 = 3.205 and t2 = 4.624 to 0.01": abs(t1 - 3.205) < 0.01 and abs(t2 - 4.624) < 0.01,
          "the ratio window is [0.688, 0.784] to 0.003": abs(r1 - 0.688) < 0.003 and abs(r2 - 0.784) < 0.003,
          "rho_Q bosons outweigh the rest 42 to 48 times": round(dom[0]) == 42 and round(dom[1]) == 48,
          "the window's relative width is about 13%": 0.12 <= width <= 0.14,
          "an integer content in the window (22, 0, 1000) holds tau in the band": bool(2.1 <= yr <= 3.2 and rises
                                                                                        and abs(y - yr) < 0.02)}
    return {"checks": ch, "t1": t1, "t2": t2, "ratio window": [r1, r2], "dominance": list(dom), "width": width,
            "example (22, 0, 1000)": {"A": A, "B": B, "t": B / abs(A), "y*": yr}}, all(ch.values())


# ------------------------------------------------------------------ C3
ROWS = {"the matter (45 Weyl in rho_Q)": (0, 0, -90), "+ the Higgs's three copies": (0, 2, -90),
        "+ the 12 gauge fields": (48, 2, -90), "+ the graviton": (57, 2, -90),
        "E8's 248 as 6d vectors": (220, 108, 224), "E8's 248, the alternative rho_Q unit": (220, 108, 448)}
PRED_A = {"the matter (45 Weyl in rho_Q)": 2.72, "+ the Higgs's three copies": 0.85, "+ the 12 gauge fields": 48.85,
          "+ the graviton": 57.85, "E8's 248 as 6d vectors": 111.97, "E8's 248, the alternative rho_Q unit": 105.19}


def C3(c2):
    r1, r2 = c2["ratio window"]
    out, ok = {}, True
    for name, (w0, wp, wr) in ROWS.items():
        A, B = AB(w0, wp, wr)
        run_ok, vals = runs(A, B)
        rest = w0 - 15 / 16 * wp
        if rest <= 0:
            n_band = "none"
        else:
            lo = math.ceil((rest / (K31 * r2) - wr) / 2)
            hi = math.floor((rest / (K31 * r1) - wr) / 2)
            n_band = [lo, hi] if lo <= hi else "none"
        out[name] = {"weights": [w0, wp, wr], "A": A, "B": B, "runs to the cusp": run_ok,
                     "extra complex scalars in rho_Q for the band": n_band}
        ok &= A > 0 and run_ok and abs(A - PRED_A[name]) < 0.006
    ok &= out["+ the Higgs's three copies"]["extra complex scalars in rho_Q for the band"] == "none"
    ch = {"every row has A > 0 and runs to the cusp, with A as predicted": bool(ok)}
    return {"checks": ch, "rows": out}, all(ch.values())


# ------------------------------------------------------------------ C4
def C4():
    cps = [((p[0] + 1.5) % 1.0, (p[1] + 1.5) % 1.0) for p in PAR]
    ys = np.round(np.arange(0.9, 8.0001, 0.005), 4)
    S = {c: np.array([W.S_c(complex(0, y), c) for y in ys]) for c in set(cps)}
    e3 = np.array([W.E_cs(complex(0, y), 3) for y in ys])
    e2 = np.array([W.E_cs(complex(0, y), 2) for y in ys])
    res = {}
    for n in (89, 95):
        wr = -90 + 2 * n
        F = sum(2 * (e3 if c == (0.0, 0.0) else S[c]) for c in cps) + wr * (-K31) * (e3 - e2)
        V = -F
        d = np.diff(V)
        mins = [float(ys[i + 1]) for i in range(len(d) - 1) if d[i] < 0 <= d[i + 1]]
        res[str(n)] = mins
    ch = {"n = 89: an axis minimum at y = 3.08 +- 0.03": any(abs(y - 3.08) <= 0.03 for y in res["89"]),
          "n = 95: an axis minimum at y = 2.13 +- 0.03": any(abs(y - 2.13) <= 0.03 for y in res["95"])}
    return {"checks": ch, "copies": cps, "axis minima": res}, all(ch.values())


# ------------------------------------------------------------------ R
def R(c1, c2):
    h = 1e-4
    x0, y0 = OMEGA.real, OMEGA.imag

    def hess(f):
        fxx = (f(x0 + h, y0) + f(x0 - h, y0) - 2 * f(x0, y0)) / h ** 2
        fyy = (f(x0, y0 + h) + f(x0, y0 - h) - 2 * f(x0, y0)) / h ** 2
        return float(fxx), float(fyy)

    h3, h2 = hess(E3), hess(E2)
    t_c = h3[1] / h2[1]
    path = [{"t": r["t"], "tau": r["grid"][1:3]} for r in c1["curve"]
            if r["t"] < 3.2 and abs(r["t"] * 4 - round(r["t"] * 4)) < 1e-9]
    curv = {}
    for name, t in (("t1", c2["t1"]), ("t2", c2["t2"])):
        y, _ = axis_min(-1.0, t, y_formula(t), half=1.0)
        f = lambda x, yy: float(E3(x, yy) - t * E2(x, yy))
        curv[name] = {"y": y, "d2V/dx2": (f(1e-3, y) + f(-1e-3, y) - 2 * f(0, y)) / 1e-6,
                      "d2V/dy2": (f(0, y + 1e-3) + f(0, y - 1e-3) - 2 * f(0, y)) / 1e-6}
    sens = {}
    for scale in (0.99, 1.01):
        t = 3.7
        y_lo, _ = axis_min(-1.0, t * scale, y_formula(t * scale), half=1.0)
        sens[str(scale)] = y_lo
    y_mid, _ = axis_min(-1.0, 3.7, y_formula(3.7), half=1.0)
    return {"omega's Hessians (E3, E2) as (xx, yy)": [h3, h2], "t_c": t_c,
            "the global minimum's path below t = 3.2 (grid)": path, "curvatures at the band's ends": curv,
            "PH2's 1%: y* at t = 3.7 and at 0.99, 1.01 times": [y_mid, sens["0.99"], sens["1.01"]],
            "SUSY pairing": "every boson with a fermion partner in its sector: A = B = 0, V identically 0"}


def main():
    out, ok = {}, {}
    for name, f in (("C0", C0), ("C1", C1)):
        out[name], ok[name] = f()
    out["C2"], ok["C2"] = C2()
    out["C3"], ok["C3"] = C3(out["C2"])
    out["C4"], ok["C4"] = C4()
    out["R"] = R(out["C1"], out["C2"])
    for name in ("C0", "C1", "C2", "C3", "C4"):
        print(name, "holds" if ok[name] else "FAILS")
        for k, v in out[name]["checks"].items():
            print("   ", "ok  " if v else "FAIL", k)
    out["cells holding"] = ok
    out["verdict"] = ("every cell as predicted" if all(ok.values())
                      else "cells failed: " + ", ".join(k for k, v in ok.items() if not v))
    print("C2:", {k: out["C2"][k] for k in ("t1", "t2", "ratio window", "dominance", "width")})
    print("C3:", {k: (v["A"], v["extra complex scalars in rho_Q for the band"]) for k, v in out["C3"]["rows"].items()})
    print("R: t_c", out["R"]["t_c"], "; PH2 1%:", out["R"]["PH2's 1%: y* at t = 3.7 and at 0.99, 1.01 times"])
    print("verdict:", out["verdict"])
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
