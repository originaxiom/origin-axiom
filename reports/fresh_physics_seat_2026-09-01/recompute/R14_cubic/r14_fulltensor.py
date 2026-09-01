#!/usr/bin/env python3
"""R14 addendum: no-shape-assumption check via characters.
dim Inv(27 x 27 x 27) (FULL tensor, ordered) = multiplicity of 27bar in 27 x 27.
If this equals 1, the unique full-tensor invariant trilinear must coincide with
the symmetric cubic (survivor automatically symmetric)."""
from fractions import Fraction
import importlib.util, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("r14c", os.path.join(HERE, "r14_characters.py"))
# reuse machinery by inlining the essential pieces instead of executing the whole module:
exec(open(os.path.join(HERE, "r14_characters.py")).read().split("# ---------- the 27 ----------")[0])

w27 = weight_system((1, 0, 0, 0, 0, 0))
W = sorted(w27)
# 27 x 27 weight multiset
t2 = {}
for i in range(27):
    for j in range(27):
        s = tuple(W[i][k] + W[j][k] for k in range(6))
        t2[s] = t2.get(s, 0) + 1
assert sum(t2.values()) == 729
work = dict(t2)
dec = []
while any(v for v in work.values()):
    dom = [w for w, v in work.items() if v > 0 and all(x >= 0 for x in w)]
    lam = max(dom, key=lambda w: int(sum(root_coords(w))))
    mlam = work[lam]
    for w, mv in freudenthal(lam).items():
        work[w] = work.get(w, 0) - mlam * mv
    dec.append((lam, mlam, int(weyl_dim(lam))))
print("[27x27] decomposition:", dec)
m27bar = sum(m for l, m, d in dec if l == (0, 0, 0, 0, 0, 1))
print("[27x27x27] dim Inv(full ordered tensor cube) = mult of 27bar in 27x27 =", m27bar)
