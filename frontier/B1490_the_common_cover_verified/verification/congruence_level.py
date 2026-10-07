#!/usr/bin/env python3
"""R60-3, first half (run once 2026-10-07, unsealed): LP01's sentence "the figure-eight group is a congruence subgroup of level 4
in PSL(2, Z[w])".  K = <a, b>, Riley's a = [[1,1],[0,1]], b = [[1,0],[-w,1]] (w^2 + w + 1 = 0), of index 12 (Riley).  K contains
Gamma(N) iff its image in PSL(2, Z[w]/N) has index 12 there.  |PSL(2, Z[w]/4)| = 3840/2 = 1920 (2 is inert; the local ring of
order 16 over F_4), so level 4 iff the image has order 160; |PSL(2, F_4)| = 60, so level 2 iff order 5."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def run(N):
    def mul(x, y): p, q = x; r, s = y; return ((p*r - q*s) % N, (p*s + q*r - q*s) % N)
    def add(x, y): return ((x[0]+y[0]) % N, (x[1]+y[1]) % N)
    def neg(x): return ((-x[0]) % N, (-x[1]) % N)
    def mmul(A, B): return tuple(tuple(add(mul(A[i][0], B[0][j]), mul(A[i][1], B[1][j])) for j in range(2)) for i in range(2))
    def canon(A): B = tuple(tuple(neg(x) for x in r) for r in A); return min(A, B)
    one, zero, w = (1, 0), (0, 0), (0, 1)
    a = ((one, one), (zero, one)); b = ((one, zero), (neg(w), one))
    seen = {canon(((one, zero), (zero, one)))}; frontier = list(seen)
    while frontier:
        nxt = []
        for g in frontier:
            for h in (a, b):
                for prod in (mmul(g, h), mmul(h, g)):
                    c = canon(prod)
                    if c not in seen: seen.add(c); nxt.append(c)
        frontier = nxt
    return len(seen)
out = {"image_order_mod_4": run(4), "PSL_order_mod_4": 1920, "image_order_mod_2": run(2), "PSL_order_mod_2": 60}
out["level_4_given_index_12"] = out["image_order_mod_4"] * 12 == 1920
out["level_2"] = out["image_order_mod_2"] * 12 == 60
json.dump(out, open(HERE / "congruence_level.json", "w"), indent=1); print(out)
