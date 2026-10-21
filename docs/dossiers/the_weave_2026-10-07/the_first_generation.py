#!/usr/bin/env python3
"""W118 -- the first generation: does the composite field, the fermions' own bilinear, lift the first generation's zero
with a forced power and a forced coefficient the data accept?  The rule is W118_RULE.md, committed and pushed before
this script.  One run; its output (the_first_generation.json, the_first_generation_run.txt) is committed before it is
read.

The order: the rule was committed (cab7adf9e) before this script was begun; its push waited on the pre-push suite and
came before this script's commit.

Pre-run disclosure: while this script was written, its parts were run in scratch only on code paths that touch no
cell: the pairing algebra (det Y(a; c) = (a.c)(a.a)(c.c), Lagrange's identity, the triple product) on random complex
vectors, and the power and double-ratio read-out on a synthetic family Y(delta) built from random vectors.  No section
of rho_R was solved or evaluated, no composite was formed, and no cell was computed.

Seen after the rule's commit and before this script's (disclosed): main's S159 (b4d0a5ed2, B1691), the commit message.
Under main's coupling to the residue triplet R (B1645) with a covariant Higgs direction, it finds the exponents near
the cusp (m2/m3 ~ |q|^(1/2), m1/m3 ~ Im tau |q|) and near omega set by the residual Z3 charge, k mod 6. W118's
composites (products of two sections, B1644's form with the coupling among the sections) are not among its sections,
and no number in it decides a W118 cell.

It reuses W65's and W68's code (the_second_unit.py, the_residual_charges_at_omega.py, imported): the 40-digit
collocation, the sections' construction loop (copied from W68's main), the eigenlines at omega, the displacements and
the power read-out.  The data are W66's (the_strong_angle.py) and W115's lepton ratios (the_shared_tau.py).

Conventions fixed here, within the rule:
- the sections are named by their weight and placement: at -1/2, E = (1, 0, 0), R = (0, 1, 0), R' = (0, 0, 1); at 3/2,
  S1 = (1, 0, 0), S2 = (0, 1, 0), S3 = (0, 0, 1); at 7/2, X = (0, 0, 0); the run checks that exactly these seven
  occur;
- the composites are P1 = S2 x S3, P2 = S3 x S1, P3 = S1 x S2, evaluated pointwise with W65's cross product;
- a pairing's double ratio is (m1/m3) / (m2/m3)^2 from the singular values, read at delta = 10^-4 and 10^-3;
- H2's away-from-omega points are W68's probes, 0.13 + 1.21i and -0.31 + 1.07i.
"""
import itertools
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_residual_charges_at_omega as RC  # noqa: E402  (W68)
import the_second_unit as SU  # noqa: E402  (W65)
import the_strong_angle as SA  # noqa: E402  (W66's quark data)
import the_shared_tau as ST  # noqa: E402  (W115's lepton data)

T0 = time.time()
OUT = HERE / "the_first_generation.json"
mp.mp.dps = 40
I = mp.mpc(0, 1)
OMEGA = RC.OMEGA
DELTAS = RC.DELTAS                          # 1e-4, 1e-3, 1e-2
ZERO = mp.mpf("1e-30")
PROBES = [mp.mpc("0.13", "1.21"), mp.mpc("-0.31", "1.07")]
NAMES = {(Fraction(-1, 2), (1, 0, 0)): "E", (Fraction(-1, 2), (0, 1, 0)): "R", (Fraction(-1, 2), (0, 0, 1)): "R'",
         (Fraction(3, 2), (1, 0, 0)): "S1", (Fraction(3, 2), (0, 1, 0)): "S2", (Fraction(3, 2), (0, 0, 1)): "S3",
         (Fraction(7, 2), (0, 0, 0)): "X"}
MADE_OF = {"P1": ("S2", "S3"), "P2": ("S3", "S1"), "P3": ("S1", "S2")}
SECTIONS7 = ["E", "R", "R'", "S1", "S2", "S3", "X"]


def log(*a):
    print(f"[{time.time() - T0:9.1f}s]", *a, flush=True)


# ------------------------------------------------------------------------------------------- the sections (W68's loop)
def build_sections():
    table = RC.dims()
    sections = []
    for k in RC.WEIGHTS:
        for u in itertools.product((0, 1), repeat=3):
            if table[(k, u)]["dimension"] != 1:
                continue
            order = [l for l, on in zip(RC.LINES, u) if on] + [l for l, on in zip(RC.LINES, u) if not on]
            best = None
            for line in order:
                terms, res = RC.solve(u, k, line)
                if best is None or res < best[1]:
                    best = (terms, res, line)
                if res < 1e-20:
                    break
            f = (lambda tm: (lambda t: SU.evaluate(tm, t)))(best[0])
            probe = [mp.mpc("0.13", "1.21"), mp.mpc("-0.31", "1.07")]
            dup = next((s for s in sections if s["k"] == k and all(RC.parallel(f(t), s["f"](t)) for t in probe)), None)
            if dup is not None:
                dup["also"].append(str(u))
                continue
            sections.append({"name": NAMES.get((k, u), f"k = {k}, u = {u}"), "k": k, "u": u, "f": f,
                             "residual": best[1], "also": []})
    return table, sections


# ------------------------------------------------------------------------------------------- the pairing's read-outs
def ratios(a, c):
    S = mp.svd_c(SU.Yuk(a, c), compute_uv=False)
    return (S[2] / S[0], S[1] / S[0]) if S[0] > 0 else (mp.nan, mp.nan)


def powers(ms):
    """ms: [(m1/m3, m2/m3)] at DELTAS; W68's power read-out"""
    def power(i):
        vals = [m[i] for m in ms]
        if all(v < ZERO for v in vals):
            return "identically zero", None
        if any(v < ZERO for v in vals):
            return "zero at some delta", None
        p01 = float(mp.log(vals[1] / vals[0]) / mp.log(10))
        p12 = float(mp.log(vals[2] / vals[1]) / mp.log(10))
        return p01, p12
    return power(0), power(1)


def score(ms, p1, p2):
    """the double ratio m1 m3 / m2^2 at 1e-4 if the pairing has a stable full hierarchy and a converged limit"""
    (a1, b1), (a2, b2) = p1, p2
    if not all(isinstance(x, float) for x in (a1, b1, a2, b2)):
        return None, "no full hierarchy (a power is zero or undefined)"
    if not (abs(a1 - b1) <= 0.05 and abs(a2 - b2) <= 0.05):
        return None, "powers not stable to 0.05"
    if not (a1 > a2 > 0.05):
        return None, "not a full hierarchy (p1 > p2 > 0)"
    dr4 = ms[0][0] / ms[0][1] ** 2
    dr3 = ms[1][0] / ms[1][1] ** 2
    if abs(dr4 / dr3 - 1) >= 0.01:
        return None, f"limit not converged (1e-3: {float(dr3):.6g}; 1e-4: {float(dr4):.6g})"
    return float(dr4), "scored"


def windows():
    """the data's double ratios and windows, |ln(DR/DR_data)| <= 1.96 sigma"""
    out = {}
    for name, (i, j), logd, rel in (("up", (0, 1), SA.LOGD, SA.REL), ("down", (2, 3), SA.LOGD, SA.REL),
                                    ("leptons", (0, 1), ST.LLOG, ST.LREL)):
        dr = math.exp(logd[i] - logd[j])
        sig = math.sqrt(math.hypot(rel[i], 0.10) ** 2 + math.hypot(rel[j], 0.10) ** 2)
        out[name] = {"DR_data": dr, "sigma": sig, "window": [dr * math.exp(-1.96 * sig), dr * math.exp(1.96 * sig)]}
    return out


# ------------------------------------------------------------------------------------------- the run
def main():
    out = {"rule": "W118_RULE.md", "script": "the_first_generation.py", "status": "one run"}
    table, secs = build_sections()
    names = [s["name"] for s in secs]
    log("sections", names, "residuals", [f"{s['residual']:.1e}" for s in secs])
    S = {s["name"]: s for s in secs}

    # ---------------- H0, the control
    lines_ok, lines = True, {}
    for s in secs:
        v = s["f"](OMEGA)
        sines = {nm: float(SU.sine(v, ln)) for nm, ln in RC.EIG.items()}
        nearest = min(sines, key=sines.get)
        lines[s["name"]] = {"nearest": nearest, "sine": sines[nearest]}
        lines_ok &= nearest == RC.EXPECT[s["k"]] and sines[nearest] < 1e-20
    t4 = OMEGA + I * DELTAS[0]
    r_ex = ratios(S["E"]["f"](t4), S["X"]["f"](t4)) if {"E", "X"} <= set(S) else (mp.nan, mp.nan)
    r_xx = ratios(S["X"]["f"](t4), S["X"]["f"](t4)) if "X" in S else (mp.nan, mp.nan)
    dr_ex, dr_xx = r_ex[0] / r_ex[1] ** 2, r_xx[0] / r_xx[1] ** 2
    h0 = {"the sections": names, "the seven as named": sorted(names) == sorted(SECTIONS7),
          "residuals": {s["name"]: s["residual"] for s in secs}, "lines at omega": lines,
          "W68's double ratio E with X at 1e-4": float(dr_ex), "W68's double ratio X with X at 1e-4": float(dr_xx)}
    h0["holds"] = bool(h0["the seven as named"] and all(s["residual"] < 1e-20 for s in secs) and lines_ok
                       and abs(dr_ex / 15 - 1) <= 1e-6 and abs(dr_xx - 1) <= 1e-6)
    out["H0"] = h0
    log("H0", h0["holds"], float(dr_ex), float(dr_xx))
    if not h0["the seven as named"]:
        out["cells"] = {"H0": False}
        OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
        log("stopped: the sections are not the seven named in the rule")
        return

    # ---------------- the composites and H1
    def comp(l):
        m, n = MADE_OF[l]
        return lambda t, m=m, n=n: SU.cross(S[m]["f"](t), S[n]["f"](t))
    F = {nm: S[nm]["f"] for nm in SECTIONS7}
    for l in MADE_OF:
        F[l] = comp(l)
    h1 = {}
    ok1 = True
    for l in MADE_OF:
        norms = [SU.norm(F[l](OMEGA + I * d)) for d in DELTAS]
        sl = [float(mp.log(norms[1] / norms[0]) / mp.log(10)), float(mp.log(norms[2] / norms[1]) / mp.log(10))]
        v = F[l](OMEGA + I * DELTAS[0])
        sines = {nm: float(SU.sine(v, RC.EIG[nm])) for nm in ("l_w", "l_w2", "axis")}
        near = min(("l_w", "l_w2"), key=lambda nm: sines[nm])
        h1[l] = {"slopes of log|P| (1e-4 to 1e-3, 1e-3 to 1e-2)": sl, "sines at 1e-4": sines,
                 "nearest isotropic line": near, "|P| at omega": float(SU.norm(F[l](OMEGA)))}
        ok1 &= all(abs(x - 1) <= 0.02 for x in sl) and sines[near] < 1e-3
    out["H1"] = {"per composite": h1, "holds": bool(ok1)}
    log("H1", ok1, {l: (round(h1[l]["slopes of log|P| (1e-4 to 1e-3, 1e-3 to 1e-2)"][0], 4),
                        h1[l]["nearest isotropic line"]) for l in MADE_OF})

    # ---------------- the 27 pairings: H2, H3, H4
    pairs = [(l, c) for l in MADE_OF for c in SECTIONS7] + list(itertools.combinations_with_replacement(MADE_OF, 2))
    wins = windows()
    rows, ok2, scored = {}, True, []
    for a, c in pairs:
        lifts = not (c in ("R", "R'") or c in MADE_OF[a])
        ms = []
        for d in DELTAS:
            t = OMEGA + I * d
            ms.append(ratios(F[a](t), F[c](t)))
        mp_probe = [ratios(F[a](t), F[c](t)) for t in PROBES]
        if lifts:
            ok = all(r[0] > mp.mpf("1e-20") for r in mp_probe)
        else:
            ok = all(r[0] < ZERO for r in ms + mp_probe)
        ok2 &= bool(ok)
        p1, p2 = powers(ms)
        dr, why = score(ms, p1, p2)
        hits = []
        if dr is not None:
            scored.append(f"{a} | {c}")
            hits = [nm for nm, w in wins.items() if w["window"][0] <= dr <= w["window"][1]]
        rows[f"{a} | {c}"] = {
            "lifts by hand": lifts, "as derived": bool(ok),
            "m1/m3 at 1e-4, 1e-3, 1e-2": [float(r[0]) for r in ms],
            "m2/m3 at 1e-4, 1e-3, 1e-2": [float(r[1]) for r in ms],
            "m1/m3 at the probes": [float(r[0]) for r in mp_probe], "p1": list(p1), "p2": list(p2),
            "double ratio at 1e-4": None if any(float(r[1]) == 0 for r in ms[:1]) else float(ms[0][0] / ms[0][1] ** 2),
            "scored double ratio": dr, "scoring": why, "in the windows of": hits}
        log("pair", a, "|", c, "lifts", lifts, "ok", bool(ok), "p", p1[0], p2[0], why, dr, hits)
    out["H2"] = {"lifting by hand": sum(1 for r in rows.values() if r["lifts by hand"]),
                 "not lifting by hand": sum(1 for r in rows.values() if not r["lifts by hand"]), "holds": bool(ok2)}
    out["H3"] = {"every pairing": rows}
    hits = {k: r["in the windows of"] for k, r in rows.items() if r["in the windows of"]}
    out["H4"] = {"windows": wins, "scored pairings": scored, "look-elsewhere count": 3 * len(scored), "hits": hits,
                 "holds": bool(not hits)}
    out["cells"] = {c: out[c]["holds"] for c in ("H0", "H1", "H2", "H4")}
    out["seconds"] = time.time() - T0
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: float(x) if isinstance(x, (np.floating, mp.mpf))
                              else str(x)) + "\n", encoding="utf-8")
    log("cells", out["cells"])
    log("written the_first_generation.json")


if __name__ == "__main__":
    main()
