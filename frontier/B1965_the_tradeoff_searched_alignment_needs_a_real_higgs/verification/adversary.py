"""B1965 (main, 2026-11-19; data-free; the counterexample threshold fixed here before the run, no hash recorded): an adversary for the trade-off.  At fixed points of frame C,
search h in C^3 (constant Higgs triplet, normalised, global phase fixed) to make the charge-consistent mixing aligned AND
both sectors hierarchical.  Objective (minimised): log10(max(up m2/m3, down m2/m3)) + 20 * max(0, 0.9 - diag), so a
value below -2 means a counterexample (aligned to 0.9 with both heavy-pair ratios below 1e-2).
Nelder-Mead from 12 starts per point (6 random, 6 from the scan's best aligned and best hierarchical triplets' kind)."""
import sys, random, math
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import scan as SC
from fractions import Fraction as Fr
from scipy.optimize import minimize


def h_of(x):
    h = [complex(x[0], 0.0), complex(x[1], x[2]), complex(x[3], x[4])]
    n = math.sqrt(sum(abs(c) ** 2 for c in h)) or 1.0
    return [c / n for c in h]


def obj(x, y, p):
    q = SC.run(h_of(x), y, p)
    return math.log10(max(q["u21"], q["d21"], 1e-300)) + 20 * max(0.0, 0.9 - q["diag"])


if __name__ == "__main__":
    rng = random.Random(7)
    for (y, p) in ((3.0, (Fr(1, 5), Fr(2, 5))), (6.0, (Fr(1, 5), Fr(2, 5))), (3.0, (Fr(3, 7), Fr(1, 7))), (6.0, (Fr(2, 7), Fr(5, 7)))):
        best = None
        for s in range(12):
            x0 = [rng.gauss(0, 1) for _ in range(5)]
            r = minimize(obj, x0, args=(y, p), method="Nelder-Mead", options={"maxfev": 400, "xatol": 1e-4, "fatol": 1e-4})
            q = SC.run(h_of(r.x), y, p)
            cand = (r.fun, q)
            if best is None or cand[0] < best[0]: best = cand
            print("  height %.0f point %s,%s start %2d: objective %.3f; diag %.3f, up m2/m3 %.1e, down m2/m3 %.1e, r %.3f" % (y, p[0], p[1], s, r.fun, q["diag"], q["u21"], q["d21"], q["r"]), flush=True)
        f, q = best
        print("height %.0f point %s,%s: BEST objective %.3f (a counterexample needs < -2): diag %.3f, up m2/m3 %.1e, down m2/m3 %.1e, r %.3f" % (y, p[0], p[1], f, q["diag"], q["u21"], q["d21"], q["r"]), flush=True)
