"""B1993 (main, 2026-11-25; data-free): the cusp's integer readings. M1: all integer solutions of x^2+y^2+z^2 = xyz with
|entries| <= B are = 0 mod 3; M2: the positive ones form one orbit of L, R, L^-1, R^-1 within the box; M3: the sign classes.
Exact integer arithmetic.
    python3 -B integers.py > integers_run.txt"""
import math
B = 3000
sols = set()
for x in range(-B, B + 1):
    for y in range(-B, B + 1):
        # z^2 - xy z + (x^2 + y^2) = 0
        D = (x * y) ** 2 - 4 * (x * x + y * y)
        if D < 0: continue
        r = math.isqrt(D)
        if r * r != D: continue
        for z in ((x * y + r), (x * y - r)):
            if z % 2 == 0 and abs(z // 2) <= B: sols.add((x, y, z // 2))
print("solutions with |entries| <= %d: %d (the origin included: %s)" % (B, len(sols), (0, 0, 0) in sols))
print("M1: every solution has all entries = 0 mod 3: %s" % all(v[0] % 3 == 0 and v[1] % 3 == 0 and v[2] % 3 == 0 for v in sols))
pos = {v for v in sols if v[0] > 0 and v[1] > 0 and v[2] > 0}
moves = [lambda v: (v[0], v[2], v[0] * v[2] - v[1]), lambda v: (v[2], v[1], v[1] * v[2] - v[0]),
         lambda v: (v[0], v[0] * v[1] - v[2], v[1]), lambda v: (v[0] * v[1] - v[2], v[1], v[0])]
def reach(start, inside):
    seen, st = {start}, [start]
    while st:
        u = st.pop()
        for f in moves:
            w = f(u)
            if w in inside and w not in seen: seen.add(w); st.append(w)
    return seen
r = reach((3, 3, 3), pos)
print("M2: positive solutions with max <= %d: %d; reached from (3, 3, 3) by L, R, L^-1, R^-1 within the box: %d; all: %s" % (B, len(pos), len(r), r == pos))
signs = {}
nonzero = [v for v in sols if v != (0, 0, 0)]
for v in nonzero: signs.setdefault(tuple(1 if c > 0 else -1 for c in v), 0); signs[tuple(1 if c > 0 else -1 for c in v)] += 1
print("M3: sign patterns of the nonzero solutions: %s" % sorted(signs.items()))
cls = {}
for s in signs:
    start = tuple(3 * c for c in s)
    cls[s] = len(reach(start, {v for v in nonzero if tuple(1 if c > 0 else -1 for c in v) == s}))
print("M3: within each sign pattern, reached from its (+-3, +-3, +-3): %s; L and R keep the sign pattern: %s" % (
    sorted(cls.items()), all(tuple(1 if c > 0 else -1 for c in f(v)) == tuple(1 if c > 0 else -1 for c in v) for v in list(nonzero)[:2000] for f in moves[:2] if all(abs(c) <= 10 * B for c in f(v)) and 0 not in f(v))))
print("M4 (cited): (3, 3, 3) is the one positive solution fixed by the cyclic exchange of the readings: %s" % ([v for v in pos if v[0] == v[1] == v[2]] == [(3, 3, 3)]))
