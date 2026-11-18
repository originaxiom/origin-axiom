#!/usr/bin/env python3
"""Two small checks for the status page's section 7 (main's M45). Data-free. Post hoc: both were first run in scratch
space before this file was committed, so they are labelled computed once and not sealed.

    python3 -I -u rv45_checks.py <a checkout of main at 7022a9dae> <a directory of reruns of main's checks>

G1  W-F24's height law at the mark, from this seat's committed grid (relays/chat1_2026-11-15_wf24/wf24_grid.json): the
    drop of each of the twelve log ratios from height 2 to height 6, at Re tau = 0 alone and as the mean over the grid's
    columns (the mean is what wf24_run.py's X1 reports).
G2  Main's eight check scripts for this seat's notes, rerun on a clean checkout of main: each rerun's output against the
    run file main committed, line by line. Only whether the lines are equal, and for unequal lines whether only numbers
    below 1e-6 differ, is printed; the outputs' text is not printed.
"""
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN, RERUN = sys.argv[1], sys.argv[2]

# G1
grid = json.load(open(os.path.join(HERE, "..", "chat1_2026-11-15_wf24", "wf24_grid.json")))
POINTS = [(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
mark = POINTS.index((0.4, 0.8))
keys = list(grid[0]["F"][mark].keys())


def drops(x):
    out = {}
    for k in keys:
        col = sorted((r["tau"][1], math.log(r["F"][mark][k])) for r in grid if abs(r["tau"][0] - x) < 1e-12 and r["tau"][1] >= 2.0)
        if col and col[0][0] == 2.0 and col[-1][0] == 6.0:
            out[k] = col[0][1] - col[-1][1]
    return out


cols = sorted({r["tau"][0] for r in grid})
per = {x: drops(x) for x in cols}
per = {x: d for x, d in per.items() if len(d) == len(keys)}
at0 = per[0.0]
mean = {k: sum(per[x][k] for x in per) / len(per) for k in keys}
print("G1: the twelve log ratios at the mark fall from height 2 to height 6 by %.2f to %.2f at Re tau = 0, and by %.2f to"
      " %.2f as the mean over %d columns (Re tau %.1f to %.1f)" % (min(at0.values()), max(at0.values()), min(mean.values()),
                                                                 max(mean.values()), len(per), min(per), max(per)))

# G2
NUM = re.compile(r"[-+]?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?")
CHECKS = os.path.join(MAIN, "frontier", "B1957_the_seats_claims_register", "verification", "checks")
for s in ("web_posthoc_closure", "web_wz1_other_discriminants", "web_wf17_on_main", "web_wc4_theorem_c", "web_wb2_d1",
          "web_wf24_wf25", "web_wc2_census_and_lattices", "web_p783_spectrum"):
    A = open(os.path.join(RERUN, s + ".out")).read().splitlines()
    B = open(os.path.join(CHECKS, s + "_run.txt")).read().splitlines()
    unequal, only_small, worst = 0, True, 0.0
    for a, b in zip(A, B):
        if a == b:
            continue
        unequal += 1
        if NUM.sub("#", a) != NUM.sub("#", b):
            only_small = False
            continue
        for x, y in zip(NUM.findall(a), NUM.findall(b)):
            if x != y:
                fx, fy = float(x), float(y)
                if max(abs(fx), abs(fy)) >= 1e-6:
                    only_small = False
                worst = max(worst, max(abs(fx), abs(fy)))
    print("G2: %-28s lines %d against %d; unequal %d; %s" % (
        s, len(A), len(B), unequal,
        "identical" if unequal == 0 and len(A) == len(B) else
        ("only numbers below 1e-6 differ (largest %.1e)" % worst if only_small and len(A) == len(B) else "DIFFERS")))
