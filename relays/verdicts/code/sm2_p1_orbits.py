#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): independent recompute for practice card P1. Standard library only.

Solutions of x^2+y^2+z^2 = xyz with 0 < |entries| <= B, B = 3000.
Completeness of the enumeration (elementary, proved here, not cited):
  * if one entry is 0 then the other two squares sum to 0, so the triple is (0,0,0);
  * for a nonzero solution xyz = x^2+y^2+z^2 > 0, so (|x|,|y|,|z|) is a positive solution and the sign pattern has
    zero or two minus signs; conversely flipping two signs keeps a solution.
  So: find every positive solution by brute force over 1 <= x, y <= B (z from the quadratic in z), then apply the four
  sign patterns.
Moves (from the card's failing control, which asserts they are B1993's): L(x,y,z) = (x, z, xz-y), R(x,y,z) = (z, y, yz-x),
and their inverses, which I derive myself: L^-1(a,b,c) = (a, ab-c, b), R^-1(a,b,c) = (ab-c, b, a).
An orbit "within the box" = a connected component of the graph on the box's solutions whose edges are the moves that land
inside the box.
    python3 relays/verdicts/code/sm2_p1_orbits.py [--moves LR|L|R]
"""
import math, sys
from collections import Counter

B = 3000
which = sys.argv[sys.argv.index("--moves") + 1] if "--moves" in sys.argv else "LR"

pos = set()
for x in range(1, B + 1):
    for y in range(x, B + 1):            # symmetric in x, y: take x <= y and add the swap
        # z^2 - (xy) z + (x^2 + y^2) = 0
        s = x * y
        D = s * s - 4 * (x * x + y * y)
        if D < 0:
            continue
        r = math.isqrt(D)
        if r * r != D or (s + r) % 2:
            continue
        for z in {(s + r) // 2, (s - r) // 2}:
            if 1 <= z <= B:
                pos.add((x, y, z)); pos.add((y, x, z))

def check(v):
    x, y, z = v
    return x * x + y * y + z * z == x * y * z

assert all(check(v) for v in pos)
patterns = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
sols = {tuple(s * c for s, c in zip(p, v)) for v in pos for p in patterns}
assert all(check(v) for v in sols) and len(sols) == 4 * len(pos)

L  = lambda v: (v[0], v[2], v[0] * v[2] - v[1])
Li = lambda v: (v[0], v[0] * v[1] - v[2], v[1])
R  = lambda v: (v[2], v[1], v[1] * v[2] - v[0])
Ri = lambda v: (v[0] * v[1] - v[2], v[1], v[0])
# the inverses are inverses, on every solution
assert all(Li(L(v)) == v and L(Li(v)) == v and Ri(R(v)) == v and R(Ri(v)) == v for v in sols)
moves = {"LR": [L, Li, R, Ri], "L": [L, Li], "R": [R, Ri]}[which]

inbox = lambda v: all(1 <= abs(c) <= B for c in v)
for v in sols:                           # a move keeps the equation
    for m in moves:
        assert check(m(v))

seen, orbits = set(), []
for v0 in sorted(sols):
    if v0 in seen:
        continue
    comp, stack = [], [v0]
    seen.add(v0)
    while stack:
        v = stack.pop(); comp.append(v)
        for m in moves:
            w = m(v)
            if inbox(w) and w not in seen:
                seen.add(w); stack.append(w)
    orbits.append(comp)

sign = lambda v: tuple(1 if c > 0 else -1 for c in v)
print("moves:", which)
print("positive solutions in the box:", len(pos))
print("nonzero solutions in the box:", len(sols))
print("orbits:", len(orbits), "sizes:", sorted(len(o) for o in orbits))
for o in sorted(orbits, key=len):
    pats = Counter(sign(v) for v in o)
    print("  orbit of %d, contains %s: sign patterns %s" % (len(o), (3, 3, 3) in o, dict(sorted(pats.items()))))
ok = (len(sols) == 280 and sorted(len(o) for o in orbits) == [70, 210]
      and any(len(o) == 70 and all(sign(v) == (1, 1, 1) for v in o) and (3, 3, 3) in o for o in orbits)
      and any(len(o) == 210 and {sign(v) for v in o} == set(patterns[1:]) for o in orbits))
print("RESULT: the card's claim %s" % ("holds" if ok else "does not hold"))
sys.exit(0 if ok else 1)
