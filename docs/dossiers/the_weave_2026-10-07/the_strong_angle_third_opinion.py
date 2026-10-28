#!/usr/bin/env python3
"""W168 — the third opinion on chat1's P-323, the strong angle in the mass frame (the rule: W168_RULE.md, committed and
pushed before this script).  This seat's own instrument (W138's residues, norms and weighted M; W93's coupling) and a
measure different from chat1's: a five-point Laplacian of the phase at steps 0.04 and 0.02, flat under halving for a
non-harmonic phase and falling by four for a harmonic one.  No target is read; chat1's numbers are not read.

  P0  the closed form det Y = const (h.h)(w^2 + u.u)(u.h), for S and for S~ with conj(h); rank one at every centre
  P1  the T-step (tau + 1, b - 2/5) and the relabelling b + 1 on the ten (2/5, k/10) lines: constant shifts of theta_Y
  P2  the 800 slope-2/5 combinations (40 lines x 10 Higgs x 2 horocycles), Standard Model reading: NOT HARMONIC
  P3  the twelve lines (1/6, b), (1/3, b), b odd/12: the norms paired, the identity, theta_M HARMONIC
  P4  the horocycle enters theta_H on the ten (2/5, k/10) lines
  R   read-outs: theta_Y / pi and sign J at four rows of the record

    python3 -B docs/dossiers/the_weave_2026-10-07/the_strong_angle_third_opinion.py
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

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_two_special_higgs as W58          # noqa: E402  (W158: pins and the frame's column; T8 under it)
    import the_higgs_invariant_dichotomy as W46   # noqa: E402  (W146: thetas; W143's eps)
T8 = W58.T8
OUT = HERE / "the_strong_angle_third_opinion.json"
REV = W58.REV
UNITS = T8.UNITS                                  # ("1", "i", "j", "k")
HIGGS = ("dR",) + tuple(f"F{a}" for a in (-10, 14, 26, -6, 6, 18, -2, 10, 22))
HORS = ("L_max", "L_2")
CENTRES = [complex(x, y) for x in (0.15, 0.65) for y in (2.375, 2.875, 3.375)]
STEPS = (0.04, 0.02)
JCUT = 1e-9
_ROOT = {}
_CACHE = {}
FAILED = []


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def wrap(x):
    return (x + math.pi) % (2 * math.pi) - math.pi


# ============================================================================================ the instrument
def sector(W93, W89, sec, line, tau):
    """(R, c) for the sector at tau on the line, cached; None if the frame's norm is not finite there"""
    key = (sec, line, round(tau.real, 12), round(tau.imag, 12))
    if key not in _CACHE:
        a, b = line
        try:
            R = T8.own_residues(W93, sec, a, b, tau)
            c = T8.own_norms(W89, W93, sec, a, b, tau, R)
            _CACHE[key] = (R, c)
        except FloatingPointError as e:
            FAILED.append([sec, [str(a), str(b)], [tau.real, tau.imag], str(e)[:120]])
            _CACHE[key] = None
    return _CACHE[key]


def u_of(R, c, L):
    return {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0j)
            for s in UNITS}


def M_of(W93, u):
    return sum(u[s] * W93.EN[s] for s in UNITS)


def S_of(W93, h):
    return h[0] * W93.CN["i"] + h[1] * W93.CN["j"] + h[2] * W93.CN["k"]


def St_of(W93, S):
    return W93.EPSN @ np.conj(S) @ W93.EPSN.T


def higgs(tau, name):
    """dR, main's Higgs; F_a without its scalar eta^(3-a), whose phase cancels in theta_Y and theta_H (SM reading)"""
    if name == "dR":
        v = np.array(T8.higgs_DR(tau))
    else:
        a = int(name[1:])
        t2, t3, t4 = W46.thetas(mp.mpc(tau.real, tau.imag))[:3]
        e = W46.W143.eps_of(a)
        v = np.array([complex(e * t2 ** a), complex(e * t4 ** a), complex(1j * t3 ** a)])
    return v / np.linalg.norm(v)


def phases(W93, du, dd, L, h):
    """the Standard Model's reading at one point: theta_Y, theta_H, theta_M, the validity of the factors, and J"""
    uu, ud = u_of(*du, L), u_of(*dd, L)
    hb = np.conj(h)
    Yu = W93.coupling_np(St_of(W93, S_of(W93, h)), M_of(W93, uu))
    Yd = W93.coupling_np(S_of(W93, h), M_of(W93, ud))
    out = {"Y": float(np.angle(np.linalg.det(Yu)) + np.angle(np.linalg.det(Yd)))}
    fac = []
    for u, hx in ((uu, hb), (ud, h)):
        vec = np.array([u["i"], u["j"], u["k"]])
        sig = sum(u[s] ** 2 for s in UNITS)
        uh = vec @ hx
        ok = (abs(sig) > 1e-14 * sum(abs(u[s] ** 2) for s in UNITS) and abs(uh) > 1e-14 * np.sum(np.abs(vec * hx))
              and abs(hx @ hx) > 1e-14)
        fac.append((sig, uh, ok))
    out["H"] = float(np.angle(fac[0][1]) + np.angle(fac[1][1]))
    out["M"] = float(np.angle(fac[0][0]) + np.angle(fac[1][0]))
    out["ok"] = bool(fac[0][2] and fac[1][2])
    out["J"] = float(T8.ckm(Yu, Yd)[3])
    return out


# ============================================================================================ the measure
def laplacians(f, tc):
    """(Delta_h1, Delta_h2, valid) of the phase f at tc; differences wrapped about the centre"""
    c = f(tc)
    if c is None:
        return None
    out = []
    for h in STEPS:
        s = 0.0
        for d in (h, -h, 1j * h, -1j * h):
            v = f(tc + d)
            if v is None:
                return None
            dv = wrap(v - c)
            if abs(dv) >= math.pi / 2:
                return None
            s += dv
        out.append(s / h ** 2)
    return out


def classify(lap):
    if lap is None:
        return "invalid"
    d1, d2 = lap
    rho = d1 / d2 if d2 != 0 else float("inf")
    if abs(d2) > 1e-5 and 0.75 <= rho <= 1.35:
        return "N"
    if abs(d1) < 1e-7 or (3 <= rho <= 5 and abs(d1) > 1e-7):
        return "H"
    return "U"


def verdict(classes):
    if "N" in classes:
        return "NOT HARMONIC"
    valid = [c for c in classes if c in ("H", "U")]
    if len(valid) >= 3 and all(c == "H" for c in valid):
        return "HARMONIC"
    return "UNDETERMINED"


# ============================================================================================ the parts
def slope25_lines():
    L = T8.own_lines()
    base = [ln for ln in L if ln[0] == Fr(2, 5)]
    extra = [(Fr(2, 5), Fr(k, 25)) for k in range(25) if k % 5] + \
            [(Fr(2, 5), Fr(k, 30)) for k in range(30) if math.gcd(k, 6) == 1]
    return base, base + extra


def part_P0(W93, W89, lines):
    rng = np.random.default_rng(168)
    rS, rT = [], []
    for _ in range(200):
        h = rng.normal(size=3) + 1j * rng.normal(size=3)
        w = complex(rng.normal(), rng.normal())
        uv = rng.normal(size=3) + 1j * rng.normal(size=3)
        u = {"1": w, "i": uv[0], "j": uv[1], "k": uv[2]}
        M = M_of(W93, u)
        S = S_of(W93, h)
        core = w * w + uv @ uv
        rS.append(np.linalg.det(W93.coupling_np(S, M)) / ((h @ h) * core * (uv @ h)))
        hb = np.conj(h)
        rT.append(np.linalg.det(W93.coupling_np(St_of(W93, S), M)) / ((hb @ hb) * core * (uv @ hb)))
    rS, rT = np.array(rS), np.array(rT)
    rank = 0.0
    for ln in lines:
        for tc in CENTRES:
            for sec in ("up", "down"):
                d = sector(W93, W89, sec, ln, tc)
                if d is None:
                    continue
                R = d[0]
                rank = max(rank, abs(sum(R[s] ** 2 for s in UNITS)) / sum(abs(R[s]) ** 2 for s in UNITS))
    return {"S: the constant": [float(rS[0].real), float(rS[0].imag)],
            "S: spread over 200, relative": float(np.max(np.abs(rS / rS[0] - 1))),
            "S~ with conj(h): the constant": [float(rT[0].real), float(rT[0].imag)],
            "S~: spread over 200, relative": float(np.max(np.abs(rT / rT[0] - 1))),
            "rank one, worst |Sum R^2| / Sum |R|^2 over the 40 lines' centres": rank}


def theta_Y_at(W93, W89, line, tau, name, hor, col):
    du, dd = sector(W93, W89, "up", line, tau), sector(W93, W89, "down", line, tau)
    if du is None or dd is None:
        return None
    return phases(W93, du, dd, T8.L_at(col, tau.imag, hor), higgs(tau, name))


def part_P1(W93, W89, base, col):
    recs, worst_t, worst_b, n = [], 0.0, 0.0, 0
    tgt_t, tgt_b = 19 * math.pi / 50, -2 * math.pi / 5
    for ln in base:
        a, b = ln
        for tc in CENTRES:
            p0 = theta_Y_at(W93, W89, ln, tc, "dR", "L_max", col)
            pt = theta_Y_at(W93, W89, (a, b - a), tc + 1, "dR", "L_max", col)
            pb = theta_Y_at(W93, W89, (a, b + 1), tc, "dR", "L_max", col)
            if p0 is None or pt is None or pb is None:
                continue
            dt, db = wrap(pt["Y"] - p0["Y"]), wrap(pb["Y"] - p0["Y"])
            worst_t = max(worst_t, abs(wrap(dt - tgt_t)))
            worst_b = max(worst_b, abs(wrap(db - tgt_b)))
            n += 1
            if len(recs) < 12:
                recs.append({"line": [str(a), str(b)], "tau": [tc.real, tc.imag], "T-step shift / pi": dt / math.pi,
                             "b + 1 shift / pi": db / math.pi})
    return {"centres compared": n, "T-step: worst |shift - 19 pi/50|": worst_t,
            "b + 1: worst |shift + 2 pi/5|": worst_b, "first records": recs}


def part_P2_P4(W93, W89, lines, base, col):
    combos, rho_N, per_higgs = {}, [], {nm: {"N": 0, "H": 0, "U": 0, "invalid": 0, "J cut": 0} for nm in HIGGS}
    p4 = {}
    t0 = time.time()
    for li, ln in enumerate(lines):
        for name in HIGGS:
            for hor in HORS:
                classes = []
                for tc in CENTRES:
                    pc = theta_Y_at(W93, W89, ln, tc, name, hor, col)
                    if pc is None or not pc["ok"]:
                        classes.append("invalid")
                        per_higgs[name]["invalid"] += 1
                        continue
                    if abs(pc["J"]) <= JCUT:
                        classes.append("J cut")
                        per_higgs[name]["J cut"] += 1
                        continue

                    def f(t, ln=ln, name=name, hor=hor):
                        p = theta_Y_at(W93, W89, ln, t, name, hor, col)
                        return None if p is None or not p["ok"] else p["Y"]

                    lap = laplacians(f, tc)
                    k = classify(lap)
                    classes.append(k)
                    per_higgs[name][k] += 1
                    if k == "N":
                        rho_N.append(lap[0] / lap[1])
                combos[f"{ln[0]}|{ln[1]}|{name}|{hor}"] = verdict([c for c in classes if c not in ("J cut",)])
        print(f"P2 line {li + 1}/{len(lines)} at {time.time() - t0:.0f} s", flush=True)
    for ln in base:
        d = 0.0
        for tc in CENTRES:
            a = theta_Y_at(W93, W89, ln, tc, "dR", "L_max", col)
            b = theta_Y_at(W93, W89, ln, tc, "dR", "L_2", col)
            if a is not None and b is not None:
                d = max(d, abs(wrap(a["H"] - b["H"])))
        p4[f"{ln[0]}|{ln[1]}"] = d
    vals = list(combos.values())
    return {"combinations": len(vals), "NOT HARMONIC": vals.count("NOT HARMONIC"),
            "HARMONIC": vals.count("HARMONIC"), "UNDETERMINED": vals.count("UNDETERMINED"),
            "not NOT HARMONIC": sorted(k for k, v in combos.items() if v != "NOT HARMONIC"),
            "per Higgs, centre classes": per_higgs,
            "rho at the N centres: 10th, 50th, 90th percentiles":
            [float(np.percentile(rho_N, q)) for q in (10, 50, 90)] if rho_N else None}, \
        {"per line, max |theta_H(L_max) - theta_H(L_2)|": p4, "least over the lines": min(p4.values())}


def part_P3(W93, W89, col):
    lines = [(Fr(1, 6), Fr(k, 12)) for k in (1, 3, 5, 7, 9, 11)] + [(Fr(1, 3), Fr(k, 12)) for k in (1, 3, 5, 7, 9, 11)]
    pair_worst, ident_worst, clamps = 0.0, 0.0, 0
    verdicts, centre_classes = {}, {}
    for ln in lines:
        classes = []
        for tc in CENTRES:
            for sec in ("up", "down"):
                d = sector(W93, W89, sec, ln, tc)
                if d is None:
                    continue
                R, c = d
                if any(c[s] is None for s in UNITS):
                    clamps += 1
                    continue
                pair_worst = max(pair_worst, abs(c["1"] - c["i"]) / abs(c["1"]), abs(c["j"] - c["k"]) / abs(c["j"]))
                L0 = T8.L_at(col, tc.imag, "L_max")
                u = u_of(R, c, L0)
                sig = sum(u[s] ** 2 for s in UNITS)
                rhs = (c["1"] - c["j"]) * (R["1"] ** 2 + R["i"] ** 2)
                ident_worst = max(ident_worst, abs(sig - rhs) / sum(abs(u[s] ** 2) for s in UNITS))

            def fM(t, ln=ln):
                du, dd = sector(W93, W89, "up", ln, t), sector(W93, W89, "down", ln, t)
                if du is None or dd is None:
                    return None
                p = phases(W93, du, dd, T8.L_at(col, t.imag, "L_max"), np.array([1.0, 0.0, 0.0], dtype=complex))
                return p["M"]

            k = classify(laplacians(fM, tc))
            classes.append(k)
        verdicts[f"{ln[0]}|{ln[1]}"] = verdict(classes)
        centre_classes[f"{ln[0]}|{ln[1]}"] = classes
    return {"lines": len(lines), "pairing worst relative": pair_worst, "identity worst relative": ident_worst,
            "sector-centres with a clamp (skipped)": clamps, "theta_M verdicts": verdicts,
            "theta_M centre classes": centre_classes}


def part_R(W93, W89, col):
    L = T8.own_lines()
    rows = [("B1726's best six-row (W138)", L[151], complex(0.55, 3.05)),
            ("B1749's best row (W156)", (Fr(2, 5), Fr(1, 2)), complex(0.666666667, 3.055050463303893)),
            ("B1786's best row (W164)", (Fr(2, 5), Fr(5, 6)), complex(0.730769231, 3.037487672558812)),
            ("its mirror", (Fr(2, 5), (Fr(3, 5) - Fr(5, 6)) % 1), complex(1 - 0.730769231, 3.037487672558812))]
    out = []
    for name, ln, tau in rows:
        p = theta_Y_at(W93, W89, ln, tau, "dR", "L_max", col)
        out.append({"row": name, "line": [str(ln[0]), str(ln[1])], "tau": [tau.real, tau.imag],
                    "theta_Y / pi (mod 2)": (p["Y"] / math.pi) % 2 if p else None,
                    "J": p["J"] if p else None})
    return out


def run(root, out):
    col_bytes = T8.git_bytes(root, REV, T8.COLUMN)
    col = T8.L_column({T8.COLUMN: col_bytes})
    out["column sha256"] = T8.sha256(col_bytes)
    W93, W89 = T8.own_modules(root)
    base, lines = slope25_lines()
    out["slope-2/5 lines"] = {"of order up to 12": len(base), "in scope": len(lines)}
    out["P0"] = part_P0(W93, W89, lines)
    out["P1"] = part_P1(W93, W89, base, col)
    out["P3"] = part_P3(W93, W89, col)
    out["R"] = part_R(W93, W89, col)
    out["P2"], out["P4"] = part_P2_P4(W93, W89, lines, base, col)
    out["frame norms not finite (points skipped)"] = FAILED
    p0, p1, p2, p3, p4 = out["P0"], out["P1"], out["P2"], out["P3"], out["P4"]
    out["cells"] = {
        "P0": bool(p0["S: spread over 200, relative"] < 1e-12 and p0["S~: spread over 200, relative"] < 1e-12
                   and p0["rank one, worst |Sum R^2| / Sum |R|^2 over the 40 lines' centres"] < 1e-12),
        "P1": bool(p1["centres compared"] == 60 and p1["T-step: worst |shift - 19 pi/50|"] < 1e-9
                   and p1["b + 1: worst |shift + 2 pi/5|"] < 1e-9),
        "P2": bool(p2["combinations"] == 800 and p2["NOT HARMONIC"] == 800),
        "P3": bool(p3["pairing worst relative"] < 1e-10 and p3["identity worst relative"] < 1e-10
                   and all(v == "HARMONIC" for v in p3["theta_M verdicts"].values())),
        "P4": bool(len(p4["per line, max |theta_H(L_max) - theta_H(L_2)|"]) == 10 and p4["least over the lines"] > 1e-6)}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W168", "rule": "W168_RULE.md", "status": "one run", "rev": REV, "head": T8.resolve(root, "HEAD"),
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
