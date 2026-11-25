"""B1993, POST HOC (labelled; written after integers_run.txt showed L and R move readings between sign patterns): do L, R,
L^-1, R^-1 alone join every nonzero integer reading with |entries| <= B into one orbit? Exact.
    python3 -B signs_posthoc.py > signs_posthoc_run.txt"""
import math
B = 3000
sols = set()
for x in range(-B, B + 1):
    for y in range(-B, B + 1):
        D = (x * y) ** 2 - 4 * (x * x + y * y)
        if D < 0: continue
        r = math.isqrt(D)
        if r * r != D: continue
        for z in ((x * y + r), (x * y - r)):
            if z % 2 == 0 and abs(z // 2) <= B: sols.add((x, y, z // 2))
nonzero = {v for v in sols if v != (0, 0, 0)}
moves = [lambda v: (v[0], v[2], v[0] * v[2] - v[1]), lambda v: (v[2], v[1], v[1] * v[2] - v[0]),
         lambda v: (v[0], v[0] * v[1] - v[2], v[1]), lambda v: (v[0] * v[1] - v[2], v[1], v[0])]
seen, st = {(3, 3, 3)}, [(3, 3, 3)]
while st:
    u = st.pop()
    for f in moves:
        w = f(u)
        if w in nonzero and w not in seen: seen.add(w); st.append(w)
print("nonzero integer readings with |entries| <= %d: %d; reached from (3, 3, 3) by L, R and their inverses within the box: %d; one orbit: %s" % (B, len(nonzero), len(seen), seen == nonzero))
print("examples: L(3, 3, 3) = %s; R(-3, -3, 3) = %s" % (moves[0]((3, 3, 3)), moves[1]((-3, -3, 3))))
rest = nonzero - seen; orbs = []
while rest:
    v = next(iter(rest)); o, st2 = {v}, [v]
    while st2:
        u = st2.pop()
        for f in moves:
            w = f(u)
            if w in nonzero and w not in o: o.add(w); st2.append(w)
    orbs.append(o); rest -= o
print("the other %d readings fall into %d orbit(s) of sizes %s; each mixes the three patterns with two negatives: %s" % (
    len(nonzero) - len(seen), len(orbs), sorted(len(o) for o in orbs), all(len({tuple(1 if c > 0 else -1 for c in v) for v in o}) == 3 for o in orbs)))
