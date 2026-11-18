#!/usr/bin/env python3
"""W-P1, step 3's follow-up: the diagnosis of F0's per-word failure (W-P1c-D). Data-free; no frame is read.

    python3 -I wp1c_diag.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 3's follow-up: F0's per-word bound failed" (committed
before this script). The functions and the words are wp1c_followup.py's (its text run up to its computation).

  D1  per setting and height (1.118, 2, 3, 4, 6): the worst per-word difference, sampling against the closed form;
  D2  the worst word overall: its height, its runs with rho - y in (0, 1e-3) (number, closed-form time), and the
      difference again at ten times the sampling density.
"""
import math
import pathlib

import numpy as np

src = (pathlib.Path(__file__).resolve().parent / "wp1c_followup.py").read_text()
exec(compile(src[:src.index("store = {}")], "wp1c_followup.py", "exec"))

settings = [("a", n, words_a(n, seed)) for n, seed in ((20, 1), (40, 2), (80, 3))]
settings += [("b", X, lyndon_words(X)) for X in (100, 200, 400)]
worst = (0.0, None, None)
for lab, par, words in settings:
    wd = np.zeros(len(YS)); arg = [None] * len(YS)
    for w in words:
        h, wt, total, ell = thread(w)
        rs = closed(w)
        for j, Y in enumerate(YS):
            d = abs(wt[h > Y].sum() - above_closed(rs, Y))
            if d > wd[j]:
                wd[j], arg[j] = d, w
            if d > worst[0]:
                worst = (d, w, j)
    print("D1 %s %d: worst per-word difference at heights %s: %s" % (lab, par, "/".join(YN), ["%.1e" % v for v in wd]))

d, w, j = worst
Y = YS[j]
rs = closed(w)
graze = [(a, r) for a, r in rs if 0 < r - Y < 1e-3]
h, wt, total, ell = thread(w)
print("D2: the worst word (%d letters, longest run %d) at height %s: difference %.2e; runs with rho - y in (0, 1e-3): %d, "
      "their closed-form time %.4f" % (len(w), longest_run(w), YN[j], d, len(graze),
                                      sum(2 * math.acosh(r / Y) for a, r in graze)))
DENS = 1200
h2, wt2, total2, ell2 = thread(w)
print("D2: at ten times the density: difference %.2e (before %.2e)" % (abs(wt2[h2 > Y].sum() - above_closed(rs, Y)), d))
