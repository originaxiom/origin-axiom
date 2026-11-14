#!/usr/bin/env python3
"""W-F7, post hoc 1 (committed before its run; NOT blind: written after the sealed output was read).

Why: the sealed script, like W-F2's M3, called a matrix hyperbolic when |trace| > 2. That is right only at
determinant +1. At determinant -1 every matrix with non-zero trace is hyperbolic (the tick [[1, 1], [1, 0]] has trace 1),
and a determinant -1 matrix with |trace| = 2 (such as [[2, 1], [1, 0]]) is hyperbolic, not parabolic.

The classification used here: det +1 and |tr| > 2, or det -1 and tr != 0: hyperbolic. det +1, |tr| = 2, not +-I:
parabolic. Anything else (det +1 with |tr| < 2, +-I, det -1 with tr = 0): finite order.

    python3 -I -u wf7_posthoc_1.py

EXPECTATIONS (written before this run):
  Q1  MMM and every MMH labelling: no hyperbolic and no parabolic step (as sealed).
  Q2  Every MHH labelling: no hyperbolic step in the corrected sense; the sealed "parabolic" steps all have det +1.
  Q3  HHH: the corrected hyperbolic count is at least 380; reported, with the number of det -1 hyperbolic steps.
  Q4  Every step's matrix falls in exactly one of the three classes.
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "wf7_checks.py")).read()
ns = {"__file__": os.path.join(HERE, "wf7_checks.py")}
exec(src.split("res = {}")[0], ns)
prods, keeps_classes, keeps_rot, face, matrix, say = (ns["prods"], ns["keeps_classes"], ns["keeps_rot"], ns["face"],
                                                      ns["matrix"], ns["say"])


def kind_of(Mx):
    d = int(round(np.linalg.det(Mx)))
    tr = int(Mx[0, 0] + Mx[1, 1])
    pm_id = np.array_equal(Mx, np.eye(2, dtype=int)) or np.array_equal(Mx, -np.eye(2, dtype=int))
    if (d == 1 and abs(tr) > 2) or (d == -1 and tr != 0):
        return "hyperbolic", d
    if d == 1 and abs(tr) == 2 and not pm_id:
        return "parabolic", d
    return "finite", d


q = dict(Q1=True, Q2=True, Q3=None, Q4=True)
for kindf, labs in (("MMM", [""]), ("HHH", [""]), ("MMH", list("abc")), ("MHH", list("abc"))):
    for lab in labs:
        mirrors, rots = face(kindf, lab)
        steps = [f for _, f in prods if keeps_classes(f, mirrors) and keeps_rot(f, rots)]
        cnt = {"hyperbolic": 0, "parabolic": 0, "finite": 0, "hyp_det_minus": 0, "par_det_minus": 0}
        for f in steps:
            k, d = kind_of(matrix(f))
            cnt[k] += 1
            cnt["hyp_det_minus"] += k == "hyperbolic" and d == -1
        q["Q4"] &= cnt["hyperbolic"] + cnt["parabolic"] + cnt["finite"] == len(steps)
        say(kindf, "labelling", lab or "-", "steps", len(steps), cnt)
        if kindf in ("MMM", "MMH"):
            q["Q1"] &= cnt["hyperbolic"] == 0 and cnt["parabolic"] == 0
        if kindf == "MHH":
            q["Q2"] &= cnt["hyperbolic"] == 0
        if kindf == "HHH":
            q["Q3"] = cnt["hyperbolic"] >= 380
for key in ("Q1", "Q2", "Q3", "Q4"):
    say(key, "holds:", q[key])
