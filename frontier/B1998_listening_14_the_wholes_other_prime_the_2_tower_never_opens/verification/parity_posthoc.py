"""B1998, POST HOC (labelled; written after two_tower_run.txt showed the 2-adic neighbourhood never opening): where the
threads' integer readings (the positive Markoff tree, B1993) sit mod 2 and mod 3. Exact.
    python3 -B parity_posthoc.py > parity_posthoc_run.txt"""
import math
B = 400; sols = set()
for x in range(1, B + 1):
    for y in range(1, B + 1):
        D = (x * y) ** 2 - 4 * (x * x + y * y)
        if D < 0: continue
        r = math.isqrt(D)
        if r * r == D:
            for z in (x * y + r, x * y - r):
                if z % 2 == 0 and 0 < z // 2 <= B: sols.add((x, y, z // 2))
print("positive integer readings with max <= %d: %d" % (B, len(sols)))
print("all over the common point mod 3 (every entry = 0 mod 3): %s" % all(c % 3 == 0 for v in sols for c in v))
print("over the common point mod 2 (every entry even): %d of %d" % (sum(all(c % 2 == 0 for c in v) for v in sols), len(sols)))
print("their residue classes mod 2: %s" % sorted({tuple(c % 2 for c in v) for v in sols}))
