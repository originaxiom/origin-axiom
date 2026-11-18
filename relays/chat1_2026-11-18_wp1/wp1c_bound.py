#!/usr/bin/env python3
"""W-P1, step 3's follow-up: the sampling's bound (W-P1c-E). Data-free; no frame is read.

    python3 -I wp1c_bound.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 3's follow-up: the diagnosis's result, and the bound"
(committed before this script). The functions and the words are wp1c_followup.py's (its text run up to its computation).

  E1  for every word, setting and height: |sampled - closed| <= 2 N / DENS, N the runs with rho > y; violations, and the
      largest ratio of the difference to the bound;
  E2  the ten words with the largest difference at each height (over all settings): the difference at DENS = 120,
      1,200 and 12,000.
"""
import pathlib

import numpy as np

src = (pathlib.Path(__file__).resolve().parent / "wp1c_followup.py").read_text()
exec(compile(src[:src.index("store = {}")], "wp1c_followup.py", "exec"))

settings = [("a", n, words_a(n, seed)) for n, seed in ((20, 1), (40, 2), (80, 3))]
settings += [("b", X, lyndon_words(X)) for X in (100, 200, 400)]
viol, worst_ratio = 0, 0.0
top = {j: [] for j in range(len(YS))}
for lab, par, words in settings:
    for w in words:
        h, wt, total, ell = thread(w)
        rs = closed(w)
        for j, Y in enumerate(YS):
            d = abs(wt[h > Y].sum() - above_closed(rs, Y))
            N = sum(1 for a, r in rs if r > Y)
            bound = 2 * N / DENS
            if d > bound + 1e-12:
                viol += 1
            if bound > 0:
                worst_ratio = max(worst_ratio, d / bound)
            top[j].append((d, w))
print("E1: words x heights checked: %d; violations of |sampled - closed| <= 2N/DENS: %d; the largest ratio to the "
      "bound: %.3f" % (sum(len(ws) for _, _, ws in settings) * len(YS), viol, worst_ratio))

for j, Y in enumerate(YS):
    ten = sorted(top[j], reverse=True)[:10]
    rows = []
    for d0, w in ten:
        rs = closed(w)
        ex = above_closed(rs, Y)
        out = []
        for dens in (120, 1200, 12000):
            DENS = dens
            h, wt, total, ell = thread(w)
            out.append(abs(wt[h > Y].sum() - ex))
        DENS = 120
        rows.append(out)
    rows = np.array(rows)
    print("E2 height %s: the ten worst words' differences at DENS 120 / 1,200 / 12,000: largest %.1e / %.1e / %.1e; "
          "median %.1e / %.1e / %.1e" % ((YN[j],) + tuple(rows.max(0)) + tuple(np.median(rows, 0))))
