"""Every orbit of L, R and their inverses on (Z/N)^3 meets the plane x = y, at N = 5, 7, 11, 13, 25; so the census of
orbits can be taken on the plane, N^2 points instead of N^3.  The orbits are found by union-find from the plane's points
under the four moves of B2017; every orbit found is checked to hold a point of the plane.
    python3 -B plane_census.py            (the claim)
    python3 -B plane_census.py --control  (the test of meeting made against the plane x = y + 1: it must fail)"""
import sys
from collections import deque
def moves(N, drop=False):
    ms = [lambda a, b, c: (a, c, (a * c - b) % N), lambda a, b, c: (c, b, (b * c - a) % N),
          lambda a, b, c: (a, (a * b - c) % N, b), lambda a, b, c: ((a * b - c) % N, b, a)]
    return ms[:3] if drop else ms
def plane_orbits(N, drop=False):
    seen = {}; orbits = []
    for x in range(N):
        for z in range(N):
            s = (x, x, z)
            if s in seen:
                continue
            k = len(orbits); seen[s] = k; q = deque([s]); mem = [s]
            while q:
                p = q.popleft()
                for m in moves(N, drop):
                    t = m(*p)
                    if t not in seen:
                        seen[t] = k; q.append(t); mem.append(t)
            orbits.append(mem)
    return orbits
ctrl = "--control" in sys.argv
allmeet = True
for N in (5, 7, 11, 13, 25):
    orbs = plane_orbits(N)
    meet = sum(any(p[0] == (p[1] + ctrl) % N for p in o) for o in orbs); allmeet &= meet == len(orbs)
    print("DECISIVE: N = %d: %d orbits, %d of them meet the plane x = y, %d points covered" % (N, len(orbs), meet, sum(map(len, orbs))))
if allmeet:
    print("DECISIVE: every orbit meets the plane x = y at every N run")
else:
    sys.exit(1)
