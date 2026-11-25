"""Listening card 3 (main, 2026-11-25; data-free): the moves L, R on the cusp's leaf mod p^k, restricted to the points over
the common point (all coordinates = 0 mod p), for p = 3 (k = 2..5) and p = 5, 7 (k = 2, 3): orbits, their sizes, how each
orbit at level k reduces into level k - 1, and how many pieces each lower orbit lifts into. Exact. See ../CARD.md.
    python3 -B listen3.py > listen3_run.txt"""
import json, pathlib, time
from collections import Counter
def level(p, k):
    N = p ** k
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    vals = range(0, N, p)
    pts = [(x, y, z) for x in vals for y in vals for z in vals if (x * x + y * y + z * z - x * y * z) % N == 0]
    S = set(pts)
    for f in (L, R): assert {f(v) for v in pts} == S
    seen, orbs = set(), []
    for v in pts:
        if v in seen: continue
        o, st = {v}, [v]
        while st:
            u = st.pop()
            for f in (L, R):
                w = f(u)
                if w not in o: o.add(w); st.append(w)
        seen |= o; orbs.append(frozenset(o))
    return N, orbs
res = {}; t0 = time.time()
for p, ks in ((3, (2, 3, 4, 5)), (5, (2, 3)), (7, (2, 3))):
    prev = None
    for k in ks:
        N, orbs = level(p, k)
        sizes = Counter(len(o) for o in orbs)
        line = "p = %d, k = %d (mod %d): %d points over the common point, %d orbits; sizes %s" % (p, k, N, sum(len(o) for o in orbs), len(orbs), sorted(sizes.items(), reverse=True))
        if prev is not None:
            Np, porbs = prev
            idx = {}
            for i, o in enumerate(porbs):
                for v in o: idx[v] = i
            lifts = Counter()
            for o in orbs:
                imgs = {idx[tuple(c % Np for c in v)] for v in o}
                assert len(imgs) == 1
                lifts[next(iter(imgs))] += 1
            table = sorted(Counter((len(porbs[i]), lifts[i], tuple(sorted(len(o) for o in orbs if idx[tuple(c % Np for c in next(iter(o)))] == i))) for i in range(len(porbs))).items())
            line += "\n    lifts (lower orbit size, pieces, piece sizes): count -> %s" % [(a, b, c[:6] + (("...",) if len(c) > 6 else ()), n) for (a, b, c), n in table][:14]
        print(line + "  [%.0f s]" % (time.time() - t0), flush=True)
        res["%d^%d" % (p, k)] = sorted(sizes.items(), reverse=True)
        prev = (N, orbs)
json.dump(res, open(pathlib.Path(__file__).with_name("listen3_run.json"), "w"))
