#!/usr/bin/env python3
"""SM-C24, post hoc (disclosed): the sealed run's own rows split by whether the point's first coordinate a has a
5-part (5 divides its denominator).  No new frame computation.
    python3 -B posthoc_split_by_a.py"""
import json
import pathlib
from collections import Counter
from fractions import Fraction as Fr
d = json.loads((pathlib.Path(__file__).with_name("c24_results.json")).read_text())["rows"]
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
key = lambda r: tuple(None if r[k] is None else round(r[k] * 60) for k in K)
res = lambda r: max(abs(r[k] * 60 - round(r[k] * 60)) / 60 for k in K if r[k] is not None)
hier = lambda r: r["up_m2m3"] >= 0.1 and r["down_m2m3"] >= 0.1 and r["up_m1m3"] >= 0.2 and r["down_m1m3"] >= 0.2
for name, sel in (("a has a 5-part", lambda r: Fr(r["a"]).denominator % 5 == 0),
                  ("a has no 5-part", lambda r: Fr(r["a"]).denominator % 5 != 0)):
    rows = [r for r in d if sel(r)]
    print("%s: %d points; aligned and hierarchical %d; largest grid residual %.1e; class kept 30-40 to 40-50 %d; "
          "classes %d, sizes %s" % (name, len(rows), sum(r["r4050"]["diag"] >= 0.9 and hier(r["r4050"]) for r in rows),
          max(res(r["r4050"]) for r in rows), sum(key(r["r3040"]) == key(r["r4050"]) for r in rows),
          len(Counter(key(r["r4050"]) for r in rows)), sorted(Counter(key(r["r4050"]) for r in rows).values(),
                                                               reverse=True)))
line = Counter(key(r["r4050"]) for r in d if r["on_line"])
five = Counter(key(r["r4050"]) for r in d if Fr(r["a"]).denominator % 5 == 0)
print("the act's line (48 pairs): %d classes; the same classes as the 240 with a 5-part: %s; line sizes %s"
      % (len(line), set(line) == set(five), sorted(line.values(), reverse=True)))
print("ratio of each class's size, all 240 to the line's 48:", sorted({five[k] / line[k] for k in line}))
