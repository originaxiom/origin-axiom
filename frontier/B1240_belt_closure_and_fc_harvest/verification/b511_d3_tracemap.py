#!/usr/bin/env python3
"""B1240 — B511/D3.3 re-done on trace coordinates at high precision (independent re-implementation; fc R48 is the
finding under verification).  The banked model (d3_wild_access.py, read): Haar pairs (A,B) in SU(2); per step with
prob mix[0] apply M: (A,B)->(AB,BA); with prob mix[1] apply D: (A,B)->(A^2,B^2); else F: (A,B)->(AB,A); 3000 steps;
kappa = x^2+y^2+z^2-xyz-2 on (x,y,z) = (tr A, tr B, tr AB); classical = |kappa-2|<0.05; wild = |kappa-2|>0.5 & -2<=kappa<=2.
Trace-coordinate maps (derived here from the SL2 trace identities tr(XY)=tr X tr Y - tr(X^-1 Y)):
  F: (x,y,z) -> (z, x, xz-y)          [tr(ABA) = tr(A^2 B) = x z - y]
  M: (x,y,z) -> (z, z, w)             [tr(AB BA) = tr(A^2 B^2) = w]
  D: (x,y,z) -> (x^2-2, y^2-2, w)     with w = tr(A^2B^2) = (xz-y) y - (x^2-2) = xyz - x^2 - y^2 + 2
Each map is first VERIFIED against explicit 2x2 matrices (random SU(2), 200 trials, tolerance 1e-12) before use.
Precision: gmpy2 mpfr at PREC bits.  Two seeds per mix (E52 rule) and a double-precision (53-bit) run of the same
code, to see the collapse fc reports.  F-only control: kappa must be conserved exactly."""
import sys, json, random, math
import numpy as np
import gmpy2
from gmpy2 import mpfr

# ---- 1. verify the trace maps against matrices --------------------------------------------------
def haar_su2(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q); a, b, c, d = q
    return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])
rng = np.random.default_rng(1)
worst = 0.0
for _ in range(200):
    A, B = haar_su2(rng), haar_su2(rng)
    x, y, z = np.trace(A).real, np.trace(B).real, np.trace(A @ B).real
    w = x*y*z - x*x - y*y + 2
    F = (np.trace(A@B).real, np.trace(A).real, np.trace(A@B@A).real)
    M = (np.trace(A@B).real, np.trace(B@A).real, np.trace(A@B@B@A).real)
    D = (np.trace(A@A).real, np.trace(B@B).real, np.trace(A@A@B@B).real)
    worst = max(worst, abs(F[0]-z), abs(F[1]-x), abs(F[2]-(x*z-y)),
                abs(M[0]-z), abs(M[1]-z), abs(M[2]-w),
                abs(D[0]-(x*x-2)), abs(D[1]-(y*y-2)), abs(D[2]-w))
print(f"trace maps vs matrices, 200 Haar pairs: max discrepancy {worst:.2e}")
assert worst < 1e-12

# ---- 2. the dynamics at precision PREC --------------------------------------------------------
def run(seed, n, steps, mix, prec):
    gmpy2.get_context().precision = prec
    rs = random.Random(seed); rng = np.random.default_rng(seed)
    hist = []
    for _ in range(n):
        A, B = haar_su2(rng), haar_su2(rng)      # Haar initial pair (double is exact enough for an initial condition)
        hist.append([mpfr(np.trace(A).real), mpfr(np.trace(B).real), mpfr(np.trace(A@B).real)])
    two = mpfr(2)
    for t in range(steps):
        for h in hist:
            r = rs.random(); x, y, z = h
            if r < mix[0]:                                   # M
                w = x*y*z - x*x - y*y + two; h[0], h[1], h[2] = z, z, w
            elif r < mix[0] + mix[1]:                        # D
                w = x*y*z - x*x - y*y + two; h[0], h[1], h[2] = x*x - two, y*y - two, w
            else:                                            # F
                h[0], h[1], h[2] = z, x, x*z - y
    ks = []; esc = 0
    for x, y, z in hist:
        k = x*x + y*y + z*z - x*y*z - two
        if not (abs(x) <= 2.0000001 and abs(y) <= 2.0000001 and abs(z) <= 2.0000001) or not gmpy2.is_finite(k):
            esc += 1
        ks.append(k)
    return ks, esc

def summarize(ks, esc):
    n = len(ks)
    fin = [k for k in ks if gmpy2.is_finite(k)]
    classical = sum(1 for k in fin if abs(k - 2) < 0.05) / n
    wild = sum(1 for k in fin if abs(k - 2) > 0.5 and -2 <= k <= 2) / n
    return {"classical": round(classical, 3), "wild": round(wild, 3), "escaped": esc,
            "median_kappa": float(sorted(fin)[len(fin)//2]) if fin else None}

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
STEPS = 3000
out = {"N_per_seed": N, "steps": STEPS, "runs": {}}
mixes = [((0.10, 0.10), "M10/D10/F80"), ((0.20, 0.0), "M20/F80"), ((0.0, 0.20), "D20/F80"), ((0.0, 0.0), "F100 control")]
for prec, label in [(200, "prec200 (~60 digits)"), (53, "double (53 bits)")]:
    for mix, name in mixes:
        for seed in (11, 23):
            ks, esc = run(seed, N, STEPS, mix, prec)
            s = summarize(ks, esc)
            if name.startswith("F100"):
                # kappa must be conserved: recompute the initial kappa for the same seed and compare
                gmpy2.get_context().precision = prec
                rng0 = np.random.default_rng(seed); k0 = []
                for _ in range(N):
                    A, B = haar_su2(rng0), haar_su2(rng0)
                    x, y, z = mpfr(np.trace(A).real), mpfr(np.trace(B).real), mpfr(np.trace(A@B).real)
                    k0.append(x*x + y*y + z*z - x*y*z - 2)
                s["max_kappa_drift"] = float(max(abs(a - b) for a, b in zip(ks, k0)))
            out["runs"][f"{label} | {name} | seed {seed}"] = s
            print(f"{label:22s} {name:13s} seed {seed}: {s}", flush=True)
json.dump(out, open(__file__.replace(".py", ".json"), "w"), indent=1, default=str)

# ---- verdict (two-sided): 200-bit runs never escape and the three mixes are classical-dominated;
# the F-only control is wild-dominated (the detector bites); the 53-bit copy of the SAME code escapes
# by the hundreds -- the collapse behind the banked "2.0,2.0,2.0" percentiles.
runs = out["runs"]; ok = True
for k, s in runs.items():
    if k.startswith("prec200"):
        ok &= s["escaped"] == 0
        ok &= (s["classical"] < 0.05 and s["wild"] > 0.7) if "control" in k else (s["classical"] >= 0.85 and s["wild"] < 0.1)
    elif "control" not in k:
        ok &= s["escaped"] >= 100 and s["classical"] < 0.7
print("REPRODUCES" if ok else "DIFF")
