#!/usr/bin/env python3
"""SM-C24: the whole instrument at order 30.  By SM-C23 a point's rates at the cusp g(inf) are the rates at inf of the
point carried by g, and SL(2, Z) carries any point of exact order 30 to every other; so each point's table over all
cusps is the rates at inf of all 576 points of exact order 30.  This computes that table with main's frame unchanged
(B1945's parts and U_of), read as B1977 reads it (column 0.13, rates between heights), at heights 30, 40 and 50.
Card relays/cards/SM_C24_the-whole-instrument-at-order-30.md, pushed with this script before it is run.  Data-free.
    python3 -B run_c24.py MAIN_CHECKOUT > c24_run.txt"""
import json
import pathlib
import sys
from collections import Counter
from fractions import Fraction as Fr
from math import gcd, lcm

HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL      # noqa: E402
import cusp_mixing as CM          # noqa: E402
mp = DL.mp
CR = DL.FM.CR
TABLE_CANON = CR.canon
SECS = ("up", "down", "lep")
X = "0.13"
HEIGHTS = (30.0, 40.0, 50.0)

def order(p): return lcm(p[0].denominator, p[1].denominator)
ALL30 = sorted({(Fr(i, 30), Fr(j, 30)) for i in range(30) for j in range(30)
                if gcd(gcd(i, j), 30) == 1})
assert len(ALL30) == 576 and all(order(p) == 30 for p in ALL30)
P6 = sorted({(Fr(i, 6), Fr(j, 6)) for i in range(6) for j in range(6) if order((Fr(i, 6), Fr(j, 6))) == 6})
P5 = [((k * Fr(1, 5)) % 1, (k * Fr(2, 5)) % 1) for k in range(1, 5)]
LINE96 = {((a5 + a6) % 1, (b5 + b6) % 1) for (a5, b5) in P5 for (a6, b6) in P6}
assert len(LINE96) == 96 and LINE96 <= set(ALL30)
REPS = sorted({min(p, ((-p[0]) % 1, (-p[1]) % 1)) for p in ALL30})
assert len(REPS) == 288

def snap(a, b, y, L=None):
    if L is not None:
        CR.canon = lambda z: {"L_2": L, "L_max": L, "_extrapolated": False}
    try:
        Y = {s: DL.parts(X, y, a, b, s)[2]["S"] for s in SECS}
    finally:
        CR.canon = TABLE_CANON
    sv = {s: sorted(abs(x) for x in mp.svd_c(Y[s], compute_uv=False)) for s in SECS}
    V = CM.U_of(Y["up"]).H * CM.U_of(Y["down"])
    return sv, V

def rate(x1, x2, dy): return float(-(mp.log(abs(x2)) - mp.log(abs(x1))) / (mp.pi * dy))
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")

def rates(a, b, y1, y2, L=None):
    A, B = snap(a, b, y1, L), snap(a, b, y2, L)
    r = {}
    for s in SECS:
        r[s + "_m2m3"] = rate(A[0][s][1] / A[0][s][2], B[0][s][1] / B[0][s][2], y2 - y1)
        r[s + "_m1m3"] = rate(A[0][s][0] / A[0][s][2], B[0][s][0] / B[0][s][2], y2 - y1)
    for (i, j, n) in ((0, 1, "V12"), (1, 2, "V23"), (0, 2, "V13")):
        ok = abs(A[1][i, j]) > 0 and abs(B[1][i, j]) > 0
        r[n] = rate(A[1][i, j], B[1][i, j], y2 - y1) if ok else None
    r["diag"] = float(min(abs(B[1][k, k]) for k in range(3)))
    return r

def key(r): return tuple(None if r[k] is None else round(r[k] * 60) for k in K)
def hier(r): return r["up_m2m3"] >= 0.1 and r["down_m2m3"] >= 0.1 and r["up_m1m3"] >= 0.2 and r["down_m1m3"] >= 0.2

def main():
    rows = []
    for n, (a, b) in enumerate(REPS):
        r1 = rates(a, b, HEIGHTS[0], HEIGHTS[1]); r2 = rates(a, b, HEIGHTS[1], HEIGHTS[2])
        rows.append(dict(a=str(a), b=str(b), on_line=(a, b) in LINE96 or (((-a) % 1, (-b) % 1) in LINE96),
                         r3040=r1, r4050=r2))
        if n % 48 == 0:
            print("point", n, flush=True)
    resid = max(abs(row["r4050"][k] * 60 - round(row["r4050"][k] * 60)) / 60 for row in rows for k in K
                if row["r4050"][k] is not None)
    stable = sum(key(row["r3040"]) == key(row["r4050"]) for row in rows)
    cls = Counter(key(row["r4050"]) for row in rows)
    cls_line = Counter(key(row["r4050"]) for row in rows if row["on_line"])
    out = {
        "E1 aligned (least |V_kk| >= 0.9 at height 50), all 288": sum(row["r4050"]["diag"] >= 0.9 for row in rows),
        "E1 aligned, on the act's line (48)": sum(row["r4050"]["diag"] >= 0.9 for row in rows if row["on_line"]),
        "E1 hierarchical in both quark sectors, all 288": sum(hier(row["r4050"]) for row in rows),
        "E1 aligned and hierarchical, all 288": sum(hier(row["r4050"]) and row["r4050"]["diag"] >= 0.9 for row in rows),
        "E2 largest distance of a 40-50 rate from the grid of 1/60": resid,
        "E2 points whose class is the same on 30-40 and 40-50": stable,
        "E3 classes (40-50, on the grid of 1/60), all 288": len(cls),
        "E3 classes on the act's line": len(cls_line),
        "E3 class sizes": sorted(cls.values(), reverse=True),
    }
    # E4: the sign of the point, on 12 pairs
    e4 = 0.0
    for (a, b) in REPS[::24]:
        r, s = rates(a, b, 40.0, 50.0), rates((-a) % 1, (-b) % 1, 40.0, 50.0)
        e4 = max(e4, *(abs(r[k] - s[k]) for k in K if r[k] is not None and s[k] is not None))
    out["E4 largest rate difference between v and -v (12 pairs)"] = e4
    # K0: the frozen end; rates with L moved by +-0.05 from the table's value, 12 points
    L0 = TABLE_CANON(complex(0.13, 6.0))["L_2"]
    k0 = 0.0
    for (a, b) in REPS[::24]:
        base = rates(a, b, 40.0, 50.0)
        for dL in (-0.05, 0.05):
            r = rates(a, b, 40.0, 50.0, L=L0 + dL)
            k0 = max(k0, *(abs(r[k] - base[k]) for k in K if r[k] is not None and base[k] is not None))
    out["K0 largest rate change with the end moved by 0.05 (12 points)"] = k0
    (HERE / "c24_results.json").write_text(json.dumps(dict(summary=out, rows=rows), indent=1))
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
