#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): independent recompute for practice card P2. Standard library only.

Every nonzero solution of x^2+y^2+z^2 = xyz with |entries| <= 300: are all three entries divisible by 9?
Enumeration: a direct triple loop over positive entries x <= y <= z <= 300 (no quadratic formula), then all orderings and
the four sign patterns (zero or two minus signs; see sm2_p1_orbits.py for the two-line proof that this is complete).
The test is on the entry itself, c % 9 == 0, and separately c % 3 and c*c % 9 to show what each instrument measures.
    python3 relays/verdicts/code/sm2_p2_divisibility.py
"""
import itertools, sys
B = 300
base = []
for x in range(1, B + 1):
    for y in range(x, B + 1):
        for z in range(y, B + 1):
            if x * x + y * y + z * z == x * y * z:
                base.append((x, y, z))
sols = set()
for t in base:
    for p in itertools.permutations(t):
        for s in [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]:
            sols.add(tuple(a * b for a, b in zip(s, p)))
assert all(x * x + y * y + z * z == x * y * z for x, y, z in sols)
bad9 = sorted((v for v in sols if any(c % 9 for c in v)), key=lambda v: (max(map(abs, v)), v))
print("unordered positive solutions:", base)
print("nonzero solutions in the box:", len(sols))
print("all entries divisible by 3:", all(c % 3 == 0 for v in sols for c in v))
print("all squares of entries divisible by 9:", all(c * c % 9 == 0 for v in sols for c in v))
print("all entries divisible by 9:", not bad9)
print("solutions with an entry not divisible by 9: %d of %d; the first: %s" % (len(bad9), len(sols), bad9[:3]))
print("solutions with all entries divisible by 9: %d" % (len(sols) - len(bad9)))
print("RESULT: the card's claim %s" % ("holds" if not bad9 else "does not hold"))
sys.exit(0 if not bad9 else 1)
