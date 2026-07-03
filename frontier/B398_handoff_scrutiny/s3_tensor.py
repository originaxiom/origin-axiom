"""B398 S3 -- CRT tensor structure of the (1,2) s-matrix: fiber ranks + rectangle test."""
import json, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))
S = [[Fr(0)]*12 for _ in range(20)]
for k, v in T["1,2"].items():
    a, b = map(int, k.split(","))
    S[a][b] = Fr(v[3])

def rank_exact(M):
    M = [row[:] for row in M]; r = 0
    if not M or not M[0]: return 0
    m, n = len(M), len(M[0])
    for c in range(n):
        piv = next((i for i in range(r, m) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]; M[r] = [x/pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [x-f*y for x, y in zip(M[i], M[r])]
        r += 1
    return r

# CRT fibers: K1 = (k1%4, k1%5), K2 = (k2%4, k2%3). Fiber at (r4, s4) = the 5x3 matrix
# over (k1%5, k2%3) with k1%4 = r4, k2%4 = s4.
fibers = {}
for r4 in range(4):
    for s4 in range(4):
        M = [[Fr(0)]*3 for _ in range(5)]
        for k1 in range(20):
            if k1 % 4 != r4: continue
            for k2 in range(12):
                if k2 % 4 != s4: continue
                M[k1 % 5][k2 % 3] = S[k1][k2]
        rk = rank_exact(M)
        if rk: fibers[f"{r4},{s4}"] = rk
print("nonzero fibers and ranks:", fibers)
total_rank = sum(fibers.values())
print("sum of fiber ranks (upper bound on tensor rank):", total_rank)

# rectangle test for the naive split S = A(k1%4,k2%4) * B(k1%5,k2%3):
# for cells sharing (mod4)-pair and (mod5,mod3)-pair: S[x1]S[x4] == S[x2]S[x3]
viol = tot = 0
from itertools import product
cells = [(a, b) for a in range(20) for b in range(12) if S[a][b] != 0]
idx = {}
for (a, b) in cells:
    idx.setdefault(((a%4, b%4)), []).append((a, b))
groups5 = {}
for (a, b) in cells:
    groups5.setdefault(((a%5, b%3)), []).append((a, b))
# rectangles: (a1,b1),(a2,b2) with same mod4-pair; (a1',b1') matching crosswise:
# simpler canonical test: for cell pairs with equal mod4-class and cell pairs with equal
# mod5/3-class: S(u)S(v) == S(w)S(x) where u=(m4,m53), v=(m4',m53'), w=(m4,m53'), x=(m4',m53)
by_class = {}
for (a, b) in cells:
    by_class[((a%4, b%4), (a%5, b%3))] = S[a][b]   # CRT: unique cell per class pair
m4s = sorted({k[0] for k in by_class}); m53s = sorted({k[1] for k in by_class})
for i, m4 in enumerate(m4s):
    for m4b in m4s[i+1:]:
        for j, m5 in enumerate(m53s):
            for m5b in m53s[j+1:]:
                u = by_class.get((m4, m5)); v = by_class.get((m4b, m5b))
                w = by_class.get((m4, m5b)); x = by_class.get((m4b, m5))
                if None in (u, v, w, x): continue
                tot += 1
                if u*v != w*x: viol += 1
print(f"rectangle test: {viol}/{tot} violations")
json.dump(dict(fibers=fibers, fiber_rank_sum=total_rank, rect=[viol, tot]),
          open(os.path.join(HERE, "s3_tensor.json"), "w"), indent=1)
print("DONE")
