#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), practice card P1: an own recomputation sharing nothing with the card's script.
Every integer solution of x^2 + y^2 + z^2 = xyz with |x|, |y|, |z| <= N is found from the quadratic in z (for each x, y:
z^2 - xy z + x^2 + y^2 = 0), then the orbits of the moves L, R and their inverses are found by union-find, an edge kept
only when both ends lie in the box. Sign patterns are read off each orbit.
    python3 -B v_p1_own.py [N]"""
import sys
from math import isqrt
from collections import Counter, defaultdict

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
sols = set()
for x in range(-N, N + 1):
    for y in range(-N, N + 1):
        b = x * y
        disc = b * b - 4 * (x * x + y * y)
        if disc < 0:
            continue
        r = isqrt(disc)
        if r * r != disc:
            continue
        for z2 in (b + r, b - r):
            if z2 % 2 == 0 and abs(z2 // 2) <= N:
                sols.add((x, y, z2 // 2))
assert all(x * x + y * y + z * z == x * y * z for x, y, z in sols)
nonzero = sorted(s for s in sols if s != (0, 0, 0))
moves = (lambda v: (v[0], v[2], v[0] * v[2] - v[1]), lambda v: (v[2], v[1], v[1] * v[2] - v[0]),
         lambda v: (v[0], v[0] * v[1] - v[2], v[1]), lambda v: (v[0] * v[1] - v[2], v[1], v[0]))
S = set(nonzero)
parent = {s: s for s in S}
def find(s):
    while parent[s] != s:
        parent[s] = parent[parent[s]]; s = parent[s]
    return s
for s in S:
    for m in moves:
        t = m(s)
        assert t[0] ** 2 + t[1] ** 2 + t[2] ** 2 == t[0] * t[1] * t[2]
        if t in S:
            parent[find(s)] = find(t)
orbits = defaultdict(list)
for s in S:
    orbits[find(s)].append(s)
def pattern(s): return tuple(c < 0 for c in s)
print("box N = %d: solutions %d, nonzero %d, all-zero solution present %s" % (N, len(sols), len(nonzero),
      (0, 0, 0) in sols))
print("patterns among nonzero solutions:", dict(Counter(pattern(s) for s in nonzero)))
print("orbits within the box: %d, sizes %s" % (len(orbits), sorted(len(o) for o in orbits.values())))
for o in sorted(orbits.values(), key=len):
    print("  orbit of %d from %s: patterns %s" % (len(o), min(o, key=lambda s: (max(map(abs, s)), s)),
          dict(Counter(pattern(s) for s in o))))
# control: the moves cut to L and L^-1 (the card's control); the orbits must come apart
parent = {s: s for s in S}
for s in S:
    for m in (moves[0], moves[2]):
        t = m(s)
        if t in S:
            parent[find(s)] = find(t)
print("control, L and L^-1 alone: %d orbits" % len({find(s) for s in S}))
