#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): independent recompute for practice card P3. Standard library only.

Positive solutions of x^2+y^2+z^2 = xyz with entries <= 3000, unordered: does each have an entry equal to 3?
No Markov tree and no cited lemma: brute force over 1 <= x <= y <= 3000, with z the integer roots of
z^2 - xy z + (x^2 + y^2) = 0 kept when y <= z <= 3000; every solution is then checked by substitution.
    python3 relays/verdicts/code/sm2_p3_threes.py [--entry N]
"""
import math, sys
B = 3000
want = int(sys.argv[sys.argv.index("--entry") + 1]) if "--entry" in sys.argv else 3
sols = set()
for x in range(1, B + 1):
    for y in range(x, B + 1):
        s = x * y
        D = s * s - 4 * (x * x + y * y)
        if D < 0:
            continue
        r = math.isqrt(D)
        if r * r != D or (s + r) % 2:
            continue
        for z in ((s + r) // 2, (s - r) // 2):
            if y <= z <= B:
                sols.add((x, y, z))
sols = sorted(sols, key=lambda t: (t[2], t))
assert all(x * x + y * y + z * z == x * y * z for x, y, z in sols)
without = [t for t in sols if want not in t]
print("unordered positive solutions with entries <= %d: %d" % (B, len(sols)))
for t in sols:
    print("  %-18s entry %d: %s" % (t, want, want in t))
print("solutions without an entry equal to %d: %d: %s" % (want, len(without), without))
print("RESULT: the card's claim %s" % ("holds" if not without else "does not hold"))
sys.exit(0 if not without else 1)
