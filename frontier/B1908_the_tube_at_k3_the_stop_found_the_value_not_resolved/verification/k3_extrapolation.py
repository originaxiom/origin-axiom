#!/usr/bin/env python3
"""P-739: the tube at k = 3 on main, read by B1854's own two fits, and by the levels whose surface is good.
B1854's fits: (a) two points, Im(d) = I0 - a d^2 on d = 0.0005 and the mirror mean at 0.001; (b) three points on
0.0005, 0.001, 0.002.  ADDED HERE, and said: a parabola in d through the three levels with |det E - 1| under 1%.
The seat's sealed value at k = 3 is the comparison B1854 made at k = 2; nothing else is compared."""
import re, math, sys, os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")   # verification -> the arc -> frontier -> the root
sys.path.insert(0, os.path.join(ROOT, "frontier", "B1847_the_level_surfaces_own_modulus", "verification")); sys.path.insert(0, os.path.join(ROOT, "frontier", "B1846_the_metrics_read_out", "verification"))
from stage_b_modulus import reduce_tau
S0 = 0.755893
def parse(path):
    t = open(path).read()
    m = re.search(r"tau ([+-][0-9.]+)([+-][0-9.]+)i\s+reduced\s+([+-][0-9.]+)([+-][0-9.]+)i\s+detE-1 ([+-][0-9.e+-]+)", t)
    tau = complex(float(m.group(1)), float(m.group(2))); dE = float(m.group(5))
    return reduce_tau(complex(tau.real, tau.imag * math.sqrt(1 + dE))), dE
rows = {d: parse(os.path.join(HERE, "runs", "k3_s%.6f_N120.txt" % round(S0 + d, 6))) for d in (0.0005, 0.001, -0.001, 0.002, -0.002, 0.005)}
# ADDED 2026-11-13 (B1908): the grid-160 runs, by the same formula, so that the page's table is computed and not typed
rows160 = {d: parse(os.path.join(HERE, "runs", "k3_s%.6f_N160.txt" % round(S0 + d, 6))) for d in (-0.001, -0.0005, 0.0005, 0.001)
           if os.path.exists(os.path.join(HERE, "runs", "k3_s%.6f_N160.txt" % round(S0 + d, 6)))}
for d in sorted(rows160): print("   grid 160, d = %+.4f: covariant %+.6f%+.6fi   det E - 1 %+.2e" % (d, rows160[d][0].real, rows160[d][0].imag, rows160[d][1]))
for d in sorted(rows): print("   d = %+.4f: covariant %+.6f%+.6fi   det E - 1 %+.2e" % (d, rows[d][0].real, rows[d][0].imag, rows[d][1]))
I = lambda d: np.mean([rows[x][0].imag for x in (d, -d) if x in rows])
a2 = I(0.0005) + (I(0.0005) - I(0.001)) / 3
x = np.array([0.25, 1.0, 4.0]); y = np.array([I(0.0005), I(0.001), I(0.002)]); I0 = np.linalg.solve(np.c_[np.ones(3), -x, -x ** 2], y)[0]
good = sorted(d for d in rows if abs(rows[d][1]) < 1e-2)
g = np.array(good) * 1e3; P = np.linalg.solve(np.c_[np.ones(len(g)), g, g ** 2], np.array([rows[d][0].imag for d in good])) if len(good) == 3 else None
print("   B1854's fits: two-point %.4f, three-point %.4f" % (a2, I0))
print("   the levels with |det E - 1| under 1%%: %s; a parabola through them is %.4f at d = 0 (three points, three unknowns: no residual)" % (good, P[0] if P is not None else float("nan")))
print("   the largest |det E - 1|: k = 3 here %.1e; in B1854's runs at k = 2 it was 1.0e-02, in B1847's at k = 1 2.0e-02" % max(abs(v[1]) for v in rows.values()))
if __name__ == "__main__":                              # the write only when run, never when a lock loads it
    json.dump({"levels": {str(d): [rows[d][0].real, rows[d][0].imag, rows[d][1]] for d in rows}, "levels at grid 160": {str(d): [rows160[d][0].real, rows160[d][0].imag, rows160[d][1]] for d in rows160}, "two-point": a2, "three-point": float(I0), "good levels": good, "parabola through the good levels": float(P[0]) if P is not None else None},
              open(os.path.join(HERE, "k3_extrapolation.json"), "w"), indent=1)
