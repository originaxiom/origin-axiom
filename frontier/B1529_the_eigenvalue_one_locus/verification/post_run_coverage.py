#!/usr/bin/env python3
"""B1529 post-run check (written after the sealed crossing run had begun; disclosed in FINDINGS): the crossings the sealed
brackets do not reach, located and read.

Why. The sealed brackets come from X1's 5-degree grid, and a bracket needs both its frames converged with |b| < 50 a.  Next to a
pole of b the frames do not converge, or (on +-LLLRLRR) the pole lies inside the bracket, so crossings near the poles go
unbracketed.  The count of crossings on a ring is fixed at first order.  On the ring l's translation is z_l = R0 e^{i alpha}, so
psi_a = a R0 cos(alpha) and psi_b = b R0 sin(alpha), and the crossings are where
    E1: b/a = -cot(alpha),   E2: b/a = 3 cot(alpha),   E3: b/a = cot(alpha) / 3,   E4: b/a = cot(alpha).
With sm:B1527's weight-3 law b/a = -tan 3(alpha - alpha_1) (alpha_1 the first of X1's type-one frames), a crossing with
b/a = c cot(alpha) is a root of
    (1 + c) cos(2 alpha - 3 alpha_1) + (c - 1) cos(4 alpha - 3 alpha_1) = 0,
which has 8, 4, 4 and 4 roots on the circle for c = -1, 3, 1/3, 1.  That gives twenty crossings on every ring; the sealed
crossings located so far lie within 0.001 degrees of these roots.

What it does.  Targets:
  missed: each first-order crossing that no pole-free sealed bracket of its kind holds (to 0.01 degrees);
  failed: each one that a pole-free sealed bracket holds but whose sealed locate did not converge (read from the sealed record,
          once that is written; a later invocation picks these up).
Route F: X1's own float64 pinned solve at alpha_c -+ w (w = 0.25, 0.5, 1 degree).  Both ends must converge with |b| < 50 a, have
no pole between them (X1's test) and show a sign change of the crossing function.  Then crossings.locate and crossings.read run
unchanged on that bracket.
Route S, where route F finds no bracket or its locate fails, is 60 digits throughout.
  - Start from the nearest converged frame of X1's grid with no first-order pole between it and alpha_c, solved at 60 digits
    (X1c's float64_then_60).
  - Continue the pinned solution toward alpha_c (X1c's solve, warm-started by X1c's rotate) in steps of at most 1 degree and at
    most a quarter of the distance to the nearest pole.  Stop at a sign change of the crossing function or within 0.5 degrees.
  - Solve the crossing system (crossings.residual_crossing, X1c's gn) from the nearer point, turned to the interpolated angle.
  - Run crossings.read unchanged at the point.
Writes post_run_coverage.jsonl (the working file: resume-safe, one line per target; git ignores *.jsonl) and
post_run_coverage.json (the record: every entry, in target order, and the summary).
Usage: python3 post_run_coverage.py [--workers N] [--states NAME ...]"""
import json
import sys
import time
import warnings
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.optimize import brentq  # noqa: E402

import crossings as C  # noqa: E402
import post_run_poles as PP  # noqa: E402

COEF = {"E1": -1.0, "E2": 3.0, "E3": 1.0 / 3.0, "E4": 1.0}   # the crossing: b/a = COEF cot(alpha)
ROOTS = {"E1": 8, "E2": 4, "E3": 4, "E4": 4}
HELD_TOL = 0.01
WIDTHS = (0.25, 0.5, 1.0)
S_STEP, S_NEAR, S_RADIUS = 1.0, 0.5, 15.0          # route S: largest step, stop distance, search radius (degrees)
_SETUP = {}


def predicted(alpha1_deg):
    """the first-order crossings: (kind, alpha in degrees, b/a), the roots of (1 + c) cos(2 al - 3 a1) + (c - 1) cos(4 al - 3 a1)"""
    a1 = np.radians(alpha1_deg)
    out = []
    for kind, c in COEF.items():
        g = lambda al: (1 + c) * np.cos(2 * al - 3 * a1) + (c - 1) * np.cos(4 * al - 3 * a1)  # noqa: E731
        xs = np.radians(np.arange(0, 360.0 + 1e-9, 0.01))
        v = g(xs)
        roots = [brentq(g, xs[i], xs[i + 1], xtol=1e-14) for i in range(len(xs) - 1) if np.sign(v[i]) != np.sign(v[i + 1])]
        roots = sorted({round(float(np.degrees(r)) % 360, 9) for r in roots})
        assert len(roots) == ROOTS[kind], (kind, alpha1_deg, roots)
        out += [(kind, r, float(-np.tan(3 * (np.radians(r) - a1)))) for r in roots]
    return out


def poles(alpha1_deg):
    return [(alpha1_deg + 30 + 60 * k) % 360 for k in range(6)]


def circ(x, y):
    """y - x on the circle, in (-180, 180]"""
    d = (y - x) % 360
    return d - 360 if d > 180 else d


def pole_between(x, y, a1):
    d = circ(x, y)
    return any(0 < circ(x, p) * np.sign(d) < abs(d) for p in poles(a1))


def pole_distance(x, a1):
    return min(abs(circ(x, p)) for p in poles(a1))


def held(tagged, kind, ac):
    for b in tagged:
        if b["kind"] != kind or b["pole"]:
            continue
        lo, hi = b["between"]
        for x in (ac, ac + 360):
            if lo - HELD_TOL <= x <= hi + HELD_TOL:
                return b
    return None


def sealed_record(name):
    """the sealed record's entries by bracket, or None while the state is still running"""
    f = HERE / ("crossings_" + name + ".json")
    if not f.exists():
        return None
    d = json.loads(f.read_text())
    return {(e["kind"], round(e["bracket (deg)"][0], 6)): e for e in d["crossings"]}


def targets(states):
    out = []
    for sign, word in states:
        name = C.R.name_of(sign, word)
        x1 = json.loads((C.B1527 / ("x1_" + name + ".json")).read_text())
        a1 = x1["type-one frames"][0]
        tagged = PP.brackets_with_poles(name)
        rec = sealed_record(name)
        for kind, ac, ba in predicted(a1):
            b = held(tagged, kind, ac)
            key = f"{name} {kind} {ac:.4f}"
            if b is None:
                out.append({"key": key, "sign": sign, "word": word, "kind": kind, "alpha predicted": ac,
                            "b/a predicted": ba, "target": "missed"})
            elif rec is not None and "read" not in rec[(kind, round(b["between"][0], 6))]:
                out.append({"key": key, "sign": sign, "word": word, "kind": kind, "alpha predicted": ac,
                            "b/a predicted": ba, "target": "failed", "sealed bracket": b["between"]})
    return out


def setup(sign, word):
    if (sign, word) not in _SETUP:
        G, img = C.FL.word_group(sign, word)
        chars, D = C.FL.torsion_characters(img)
        P64 = C.X1.Pinned(sign, word)
        P60 = C.XC.Problem(sign, word)
        x1 = json.loads((C.B1527 / ("x1_" + C.R.name_of(sign, word) + ".json")).read_text())
        _SETUP[(sign, word)] = (G, img, chars, D, P64, P60, x1)
    return _SETUP[(sign, word)]


def route_f(P64, P60, G, img, kind, ac, a):
    f = C.FUNCS[kind]
    tried = []
    for w in WIDTHS:
        lo, hi = ac - w, ac + w
        rlo, rhi = P64.solve(np.radians(lo)), P64.solve(np.radians(hi))
        ok = rlo["converged"] and rhi["converged"]
        why = None
        if not ok:
            why = "an end did not converge"
        elif abs(rlo["b"]) > C.GRID_B_MAX * a or abs(rhi["b"]) > C.GRID_B_MAX * a:
            why = "|b| > 50 a at an end"
        elif np.sign(rlo["b"]) != np.sign(rhi["b"]) and not (abs(rlo["b"]) < PP.POLE_B * a and abs(rhi["b"]) < PP.POLE_B * a):
            why = "a pole between"
        elif np.sign(f(rlo["psi_a(l)"], rlo["psi_b(l)"])) == np.sign(f(rhi["psi_a(l)"], rhi["psi_b(l)"])):
            why = "no sign change"
        tried.append({"width": w, "outcome": why or "bracket"})
        if why is None:
            br = {"kind": kind, "between": [lo, hi]}
            loc, V = C.locate(P64, P60, br, G, img)
            return {"tried": tried, "bracket": [lo, hi], "locate": loc}, V
    return {"tried": tried}, None


def route_s(P60, G, img, x1, kind, ac):
    f = C.FUNCS[kind]
    a1, a = x1["type-one frames"][0], x1["a"]
    A = P60.a
    log = {"starts": []}
    cands = [g for g in x1["grid"] if g["converged"] and abs(g["b"]) < C.GRID_B_MAX * a
             and abs(circ(g["alpha0"], ac)) <= S_RADIUS and not pole_between(g["alpha0"], ac, a1)]
    cands.sort(key=lambda g: abs(circ(g["alpha0"], ac)))
    fun = lambda v: C.residual_crossing(v, P60.a, G, img, P60.R0, kind)  # noqa: E731
    for g in cands[:3]:
        mp.mp.dps = C.XC.DPS
        rec, V = P60.float64_then_60(g["alpha0"])
        st = {"frame": g["alpha0"], "float64_then_60": rec, "steps": 0}
        log["starts"].append(st)
        if V is None:
            continue
        x = g["alpha0"]
        goal = x + circ(x, ac)                       # alpha_c on the same unwrapped branch as x
        direction = 1.0 if goal >= x else -1.0
        fx = f(A * V[48], V[52] * V[49])
        crossed = None
        while abs(goal - x) > S_NEAR:
            step = min(S_STEP, 0.25 * pole_distance(x % 360, a1), abs(goal - x))
            xn = x + direction * step
            Vn, fn_, it, ok = P60.solve(xn, C.XC.rotate(V, xn - x))
            st["steps"] += 1
            if not ok:
                st["failed at"] = xn
                break
            fn = f(A * Vn[48], Vn[52] * Vn[49])
            if mp.sign(fn) != mp.sign(fx):
                crossed = (x, V, fx, xn, Vn, fn)
                break
            x, V, fx = xn, Vn, fn
        if "failed at" in st:
            continue
        if crossed is not None:
            x0, V0, f0, xn, Vn, fn = crossed
            xi = x0 + (xn - x0) * float(f0 / (f0 - fn))
            base, bx = (V0, x0) if abs(xi - x0) <= abs(xn - xi) else (Vn, xn)
        else:
            xi, base, bx = goal, V, x
        st["start of the crossing system (deg)"] = float(xi)
        Vc, fc, itc, okc = C.XC.gn(fun, C.XC.rotate(base, xi - bx))
        st.update({"crossing system |F|": mp.nstr(fc, 3), "iterations": itc, "converged": bool(okc)})
        if okc:
            return log, Vc
    return log, None


def one(t):
    sign, word, kind, ac = t["sign"], t["word"], t["kind"], t["alpha predicted"]
    G, img, chars, D, P64, P60, x1 = setup(sign, word)
    t1 = time.time()
    entry = dict(t)
    rf, V = route_f(P64, P60, G, img, kind, ac, x1["a"])
    entry["route F"] = rf
    entry["route"] = "F" if V is not None else None
    if V is None:
        rs, V = route_s(P60, G, img, x1, kind, ac)
        entry["route S"] = rs
        entry["route"] = "S" if V is not None else None
    if V is not None:
        Xl, Yl = V[48], V[49]
        entry["alpha (deg)"] = float(mp.degrees(mp.atan2(Yl, Xl)) % 360)
        entry["alpha - predicted (deg)"] = circ(ac, entry["alpha (deg)"])
        entry["b/a"] = mp.nstr(V[52] / C.A, 12)
        entry["crossing function / a"] = mp.nstr(C.FUNCS[kind](C.A * Xl, V[52] * Yl) / C.A, 3)
        entry["read"] = C.read(sign, word, G, img, V, kind, chars, D)
    entry["seconds"] = round(time.time() - t1)
    return entry


def main():
    args = sys.argv[1:]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 4
    states = C.R.MANIFOLDS if "--states" not in args else [
        (n[0], n[1:]) for n in args[args.index("--states") + 1:] if not n.startswith("--")]
    t0 = time.time()
    f = HERE / "post_run_coverage.jsonl"
    done = {}
    if f.exists():
        for line in f.read_text().splitlines():
            r = json.loads(line)
            done[r["key"]] = r
    todo = [t for t in targets(states) if t["key"] not in done]
    print(f"coverage: {len(todo)} targets to do, {len(done)} done", flush=True)
    with Pool(workers) as pool:
        for e in pool.imap_unordered(one, todo, chunksize=1):
            done[e["key"]] = e
            with open(f, "a") as fh:
                fh.write(json.dumps(e, default=str) + "\n")
            print(f"{e['key']} ({e['target']}): route {e['route']}, alpha {e.get('alpha (deg)')}, "
                  f"off by {e.get('alpha - predicted (deg)')}, {e['seconds']} s", flush=True)
    summary = {"targets": len(done), "located": sum(1 for e in done.values() if "read" in e),
               "by route": {r: sum(1 for e in done.values() if e["route"] == r) for r in ("F", "S", None)},
               "by state": {}}
    for e in done.values():
        s = summary["by state"].setdefault(e["sign"] + e["word"], {"targets": 0, "located": 0})
        s["targets"] += 1
        s["located"] += "read" in e
    summary["seconds this invocation"] = round(time.time() - t0)
    order = {t["key"]: i for i, t in enumerate(targets(states))}
    entries = sorted(done.values(), key=lambda e: order.get(e["key"], len(order)))
    (HERE / "post_run_coverage.json").write_text(json.dumps({"summary": summary, "entries": entries}, indent=1,
                                                            default=str))
    print(json.dumps(summary, indent=1), flush=True)


if __name__ == "__main__":
    main()
