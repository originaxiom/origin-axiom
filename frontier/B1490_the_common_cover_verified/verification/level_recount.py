#!/usr/bin/env python3
"""B1490 control C0: the figure-eight group's congruence level, recounted in SL and in PSL at levels 2, 4, 8 (Riley's
matrices a = [[1,1],[0,1]], b = [[1,0],[-w,1]]).  B731 (2026-07-20) recorded PSL-index 6 at levels 2 and 4 and 12 at level 8
("congruence at level (8)"); LP01 (2026-10-06) says level 4.  |SL(2, Z[w]/n)| is counted by closure from generators."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ONE, ZERO, W = (1, 0), (0, 0), (0, 1); I2 = ((ONE, ZERO), (ZERO, ONE))
def mul(x, y, n): p, q = x; r, s = y; return ((p*r - q*s) % n, (p*s + q*r - q*s) % n)
def add(x, y, n): return ((x[0]+y[0]) % n, (x[1]+y[1]) % n)
def neg(x, n): return ((-x[0]) % n, (-x[1]) % n)
def mmul(A, B, n): return tuple(tuple(add(mul(A[i][0], B[0][j], n), mul(A[i][1], B[1][j], n), n) for j in range(2)) for i in range(2))
def red(A, n): return tuple(tuple((e[0] % n, e[1] % n) for e in r) for r in A)
def closure(gens, n):
    seen = {red(I2, n)}; frontier = list(seen)
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                for p in (mmul(g, h, n), mmul(h, g, n)):
                    if p not in seen: seen.add(p); nxt.append(p)
        frontier = nxt
    return seen
a = ((ONE, ONE), (ZERO, ONE)); b = ((ONE, ZERO), ((0, -1), ONE)); ai = ((ONE, (-1, 0)), (ZERO, ONE)); bi = ((ONE, ZERO), (W, ONE))
SLGENS = [((ONE, ONE), (ZERO, ONE)), ((ONE, W), (ZERO, ONE)), ((ONE, ZERO), (ONE, ONE)), ((ONE, ZERO), (W, ONE))]
out = {}
for n in (2, 4, 8):
    K = closure([red(a, n), red(b, n), red(ai, n), red(bi, n)], n); G = closure([red(g, n) for g in SLGENS], n)
    mI = red(tuple(tuple(neg(e, n) for e in r) for r in I2), n); centre = 2 if (mI != red(I2, n)) else 1
    psl_K = len(K) // (2 if mI in K and centre == 2 else 1); psl_G = len(G) // centre
    out[str(n)] = dict(SL_image=len(K), SL_group=len(G), minus_I_in_image=(mI in K), PSL_image=psl_K, PSL_group=psl_G, PSL_index=psl_G // psl_K)
    print("level", n, out[str(n)], flush=True)
out["level_4_index_12"] = out["4"]["PSL_index"] == 12; out["B731_said"] = {"2": 6, "4": 6, "8": 12}
json.dump(out, open(HERE / "level_recount.json", "w"), indent=1)
