#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), practice card P3: an own recomputation sharing nothing with the card's script.
Every positive integer solution of x^2 + y^2 + z^2 = xyz with entries <= N is found directly from the quadratic in z
(no move tree), taken without regard to order, and tested for an entry equal to 3; the card's control entry 6 likewise.
    python3 -B v_p3_own.py [N]"""
import sys
from math import isqrt

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
sols = set()
for x in range(1, N + 1):
    for y in range(x, N + 1):
        b = x * y
        disc = b * b - 4 * (x * x + y * y)
        if disc < 0:
            continue
        r = isqrt(disc)
        if r * r != disc:
            continue
        for z2 in (b + r, b - r):
            if z2 > 0 and z2 % 2 == 0 and z2 // 2 <= N:
                sols.add(tuple(sorted((x, y, z2 // 2))))
assert all(x * x + y * y + z * z == x * y * z for x, y, z in sols)
sols = sorted(sols, key=lambda s: (max(s), s))
without3 = [s for s in sols if 3 not in s]
print("positive solutions with entries <= %d, without regard to order: %d" % (N, len(sols)))
for s in sols:
    print("  %s%s" % (s, "" if 3 in s else "   <- no entry equal to 3"))
print("with an entry equal to 3: %d of %d; without: %d" % (len(sols) - len(without3), len(sols), len(without3)))
print("control, with an entry equal to 6: %d of %d" % (sum(6 in s for s in sols), len(sols)))
