#!/usr/bin/env python3
"""Practice card P2 (main, 2026-11-26; P-885): every nonzero integer solution of x^2 + y^2 + z^2 = xyz with |entries| <= B
(B = 300) has all three entries divisible by 9. Exact integer arithmetic.
    python3 relays/claims/practice/p2_mod9.py
    python3 relays/claims/practice/p2_mod9.py --modulus 7     (the failing control's change)
Exit 0 when the claim holds on every solution found; 1 otherwise."""
import math, sys
B = 300
m = int(sys.argv[sys.argv.index("--modulus") + 1]) if "--modulus" in sys.argv else 9
sols = set()
for x in range(-B, B + 1):
    for y in range(-B, B + 1):
        D = (x * y) ** 2 - 4 * (x * x + y * y)
        if D < 0: continue
        r = math.isqrt(D)
        if r * r != D: continue
        for z in ((x * y + r), (x * y - r)):
            if z % 2 == 0 and abs(z // 2) <= B: sols.add((x, y, z // 2))
nonzero = sorted(v for v in sols if v != (0, 0, 0))
ok = all(c * c % m == 0 for v in nonzero for c in v)
print("DECISIVE: nonzero integer solutions with |entries| <= %d: %d" % (B, len(nonzero)))
print("DECISIVE: every entry of every one is divisible by %d: %s" % (m, ok))
sys.exit(0 if ok else 1)
