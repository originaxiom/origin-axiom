#!/usr/bin/env python3
"""B1222 test 3: does MORE symmetry go with LESS carried content? Thesis says yes; data says no."""
import math
from collections import defaultdict
import snappy

rows = []
for M in snappy.OrientableCuspedCensus(cusps=1)[:400]:
    try:
        o = M.symmetry_group().order()
        tor = [c for c in M.homology().elementary_divisors() if c != 0]
        rows.append((o, 1 if tor else 0))
    except Exception:
        continue

by = defaultdict(list)
for o, h in rows:
    by[o].append(h)
print(f"n = {len(rows)}")
for o in sorted(by):
    v = by[o]
    if len(v) >= 5:
        print(f"  |Sym|={o:2d}  n={len(v):4d}  frac with H1 torsion = {sum(v)/len(v):.3f}")

xs = [r[0] for r in rows]; ys = [r[1] for r in rows]
n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
den = math.sqrt(sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys))
r = num/den
print(f"\nPearson r(|Sym|, has-torsion) = {r:+.4f}")
print("thesis predicted NEGATIVE ->", "REFUTED" if r > 0 else "supported")
assert r > 0, "the banked refutation expects a positive correlation"
