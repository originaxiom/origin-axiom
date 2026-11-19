"""B1968's column runner (main, 2026-11-19): reach.py's own loop for one column x (argv[1]), with reach.py imported
unchanged; the random starts are seeded per column (1968 + column index) instead of one stream, the only difference.
    python3 -B reach_column.py <x> > reach_run_<x>.txt"""
import sys, pathlib, json
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reach as R
X = sys.argv[1]
rng = np.random.default_rng(1968 + ("0", "0.13", "0.25", "0.5").index(X))
from fractions import Fraction as Fr
pts = [(Fr(i, n), Fr(j, n)) for n in (5, 7) for i in range(n) for j in range(n) if (i, j) != (0, 0)]
found = []
for y in (1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 10.0):
    least = []
    for (a, b) in pts:
        ch = (R.channels(X, y, a, b, "up"), R.channels(X, y, a, b, "down"))
        best = None
        for s in range(8):
            res = minimize(lambda p: R.score(p, ch)[0], rng.normal(size=5), method="Nelder-Mead", options={"maxfev": 2000, "xatol": 1e-7, "fatol": 1e-9})
            sc = R.score(res.x, ch)
            if best is None or sc[0] < best[0]: best = sc + (list(res.x),)
        f, diag, r2, r1, rr, px = best
        ce = diag >= 0.9 and all(1e-6 <= v <= 1e-2 for v in r2) and r1 <= 0.5
        if ce: found.append((X, y, str(a), str(b), diag, r2, r1, rr, px))
        if diag >= 0.9: least.append(max(r2))
    print("x %4s height %4.1f: %d points; alignment 0.9 reached at %d; least max m2/m3 there %s; counterexamples so far %d" % (
        X, y, len(pts), len(least), ("%.2e" % min(least)) if least else "none", len(found)), flush=True)
print("COUNTEREXAMPLES (x = %s): %d" % (X, len(found)))
for c in found[:20]: print("  ", c[:8])
json.dump([[str(v) for v in c] for c in found], open(pathlib.Path(__file__).with_name("reach_found_%s.json" % X), "w"), indent=1)
