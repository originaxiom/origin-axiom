#!/usr/bin/env python3
"""W-F17, post hoc 1 (committed before its run; NOT blind: the sealed run's output for m = 1-4 and 6 has been read).

The sealed run stopped m = 5 at its 1,800-second budget. This run repeats item 3 at m = 5 with the sealed script's own
functions (imported, unchanged) and a budget of 6,900 seconds. It also checks two things read off the sealed output:

  H1  m = 5, the sealed expectations as written: T5 (purely one-dimensional, covered, the origin on a curve), T6
      (m^2 + 2 = 27 points on kappa = 2), T7 (kappa not constant on any curve), the predicted lines inside (four over C,
      in two Q-components: x = y and x + y = -1 with x^2 + x - 1 = 0).
  H2  For m = 4 and 8 the coordinate lines {y = z = 0} and {x = z = 0} lie in the fixed locus; for m = 2 and 6 they do
      not (by hand: Ta fixes (x, 0, 0) and Tb has order 4 on it; Tb fixes (0, y, 0) and Ta has order 4 on it; so both
      lines are fixed exactly when 4 divides m).
  H3  The m = 3 curve of the sealed run, projected to (x, y) (z eliminated), is
      x^2 y^2 - x^2 y - x^2 - x y^2 + x y + x - y^2 + y = 0, the polynomial agy-exp's note gives for m = 3 (its
      exponents read through the mask as 2; this run checks that reading).

    python3 -I -u wf17_posthoc1.py
"""
import importlib.util
import os
import random

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("wf17", os.path.join(HERE, "wf17_checks.py"))
W = importlib.util.module_from_spec(spec)
spec.loader.exec_module(W)
x, y, z = W.x, W.y, W.z


def say(*a):
    print(*a, flush=True)


# H2
h2 = True
for m in (2, 4, 6, 8):
    I = W.fixed_ideal(m, m)
    on = [all(W.contains(W.GB(L), g) for g in I) for L in ([y, z], [x, z])]
    say("H2 m", m, "lines {y = z = 0}, {x = z = 0} inside:", on)
    h2 &= all(on) == (m % 4 == 0) and (any(on) == (m % 4 == 0))
say("H2 holds:", h2)

# H3
I3 = W.fixed_ideal(3, 3)
comps = W.minimal(W.split(I3))
curve = [P for P in comps if W.dimension(P) == 1 and not all(W.contains(P, g) for g in (x + 1, y + 1))]
want = sp.expand(x**2 * y**2 - x**2 * y - x**2 - x * y**2 + x * y + x - y**2 + y)
H = sp.groebner(list(curve[0].exprs), z, x, y, order="lex", domain=sp.QQ)
proj = [g for g in H.exprs if not g.has(z)]
h3 = len(proj) == 1 and sp.simplify(proj[0] / want).is_number
say("H3: the m = 3 curve's (x, y) eliminant:", proj, "| equals agy-exp's polynomial up to a constant:", h3)

# H1
r = W.analyse(5, random.Random(130), budget=6900)
if r.get("timeout"):
    say("H1: m = 5 not finished within", r["seconds"], "s")
else:
    say("m 5 | components:", len(r["comps"]), "| degree of I", r["degI"], "= sum over curves", r["sum_deg"],
        "| covered (two draws)", r["covered"], "| points on kappa = 2:", r["reducible_points"], "| predicted lines inside",
        r["lines_in"], "| lines over C (formula)", r["nlines_C"], "|", r["seconds"], "s")
    for row in r["comps"]:
        say("   ", row)
    say("   plants: P3", r["P3"], "| P4", r["P4"])
    h1 = (all(row["dim"] == 1 for row in r["comps"]) and all(r["covered"])
          and any(row["origin"] for row in r["comps"] if row["dim"] == 1) and r["reducible_points"] == 27
          and all(not row.get("kappa_constant", False) for row in r["comps"] if row["dim"] == 1)
          and r["lines_in"] and r["nlines_C"] == 4)
    say("H1 holds:", h1)
