#!/usr/bin/env python3
"""POST HOC, labelled (committed before its run; reads only the committed zero-free census, ab05339eb).
Which lines give d = e exactly, and why.  Main's instrument twists each field by q*w with q = 6Y (b1656_funcs.SIXY:
Q 1, u -4, d 2, L -3, e 6, H 3) and w = alpha*tau + beta, so on a line of order N (the least N with N*alpha and N*beta
integers) a field's twist depends on 6Y mod N only.  By hand:
  6Y mod 4:  Q = L = 1, d = e = 2, u = nu = 0    (Pati-Salam's quark-lepton pairs: down and lepton sectors identical);
  6Y mod 5:  Q = u = e = 1, d = L = 2, nu = 0    (SU(5)'s 10 and 5-bar: the lepton sector is the down sector with its
                                                 left and right twists exchanged).
This script lists, for every direction and reading of the census, the lines on which |ln R2| and |ln R1| (lepton over
down, m2/m3 and m1/m3) stay below 1e-6 at every point and horocycle, and compares that list with the lines whose order
divides 4 or 5.  It also reports, on the lines of order 10 with alpha = 2/5, the largest |ln D| (D = R2*R1).
    python3 -B zero_free_de_lines.py      # writes zero_free_de_lines.json"""
import json, math, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
IDX = json.loads((HERE / "zero_free_census_index.json").read_text())
X = np.load(HERE / "zero_free_census.npz")["data"]           # point, dir, hor, field (log10 ratios first)
LINES, TASKS, DIRS = IDX["lines"], IDX["tasks"], IDX["dirs"]


def order(name):
    a, b = (Fr(s.strip()) for s in name.strip("()").split(","))
    return math.lcm(a.denominator, b.denominator)


line_of = np.array([t[0] for t in TASKS])
OUT = {"6Y mod 4": {"Q": 1 % 4, "u": -4 % 4, "d": 2 % 4, "L": -3 % 4, "e": 6 % 4, "nu": 0},
       "6Y mod 5": {"Q": 1 % 5, "u": -4 % 5, "d": 2 % 5, "L": -3 % 5, "e": 6 % 5, "nu": 0},
       "orders dividing 4 or 5": sorted(n for n in LINES if 4 % order(n) == 0 or 5 % order(n) == 0),
       "by direction and reading": {}}
for di, d in enumerate(DIRS):
    for rd, (i_dn, i_lp) in (("S", (4, 8)), ("St", (6, 10))):
        lnR2 = (X[:, di, :, i_lp] - X[:, di, :, i_dn]).astype(np.float64) * math.log(10)
        lnR1 = (X[:, di, :, i_dn + 1] - X[:, di, :, i_lp + 1]).astype(np.float64) * math.log(10)
        ok = (np.abs(lnR2) < 1e-6) & (np.abs(lnR1) < 1e-6)
        exact = sorted(LINES[k] for k in range(len(LINES)) if np.all(ok[line_of == k]))
        o10 = [k for k in range(len(LINES)) if order(LINES[k]) == 10 and LINES[k].startswith("(2/5")]
        m10 = {LINES[k]: float(np.max(np.abs((lnR2 + lnR1)[line_of == k]))) for k in o10}
        OUT["by direction and reading"][f"{d} {rd}"] = {
            "exact lines": exact, "count": len(exact),
            "equal to the order-4-or-5 list": exact == OUT["orders dividing 4 or 5"],
            "exact but order not dividing 4 or 5": [n for n in exact if n not in OUT["orders dividing 4 or 5"]],
            "order 4 or 5 but not exact": [n for n in OUT["orders dividing 4 or 5"] if n not in exact],
            "order-10 alpha = 2/5 lines: max |ln D| over points and horocycles": m10}
(HERE / "zero_free_de_lines.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
