"""B1991 (main, 2026-11-25; data-free): the moves L, R on every reading = (0,0,0) mod 2, mod 2^k, k = 2..6: orbits, sizes,
leaves, nesting; where the lifts of the common point and of 'nothing' sit; the linear group of dL, dR over F_2. Exact.
    python3 -B listen8.py > listen8_run.txt"""
from collections import Counter
from itertools import product
def kap(v, N): return (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2] - 2) % N
dL = ((1, 0, 0), (0, 0, 1), (0, -1, 0)); dR = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
def mm(A, B, p): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) % p for j in range(3)) for i in range(3))
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1)); G = {E}; fr = [E]
while fr:
    A = fr.pop()
    for B in (dL, dR):
        C = mm(tuple(tuple(x % 2 for x in r) for r in B), A, 2)
        if C not in G: G.add(C); fr.append(C)
perms = all(sorted(sum(r) for r in g) == [1, 1, 1] and all(sum(g[i][j] for i in range(3)) == 1 for j in range(3)) for g in G)
print("Q1: the linear group of dL, dR over F_2 has order %d; every element a permutation matrix of the three coordinates: %s" % (len(G), perms))
prev = None
for k in range(2, 7):
    N = 2 ** k
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    pts = list(product(range(0, N, 2), repeat=3))
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
    where = {v: i for i, o in enumerate(orbs) for v in o}
    c0, c2 = where[(0, 0, 0)], where[(2 % N, 2 % N, 2 % N)]
    sizes = Counter(len(o) for o in orbs)
    leaves = Counter(kap(next(iter(o)), N) for o in orbs)
    line = "mod %d: %d readings over the meeting point, %d orbits; sizes %s; the common point's orbit size %d, 'nothing''s %d, the same orbit: %s; orbits per leaf (kappa mod %d): %s" % (
        N, len(pts), len(orbs), sorted(sizes.items(), reverse=True)[:10], len(orbs[c0]), len(orbs[c2]), c0 == c2, N, sorted(leaves.items())[:16])
    if prev is not None:
        Np, pw = prev
        pieces = Counter()
        for o in orbs:
            imgs = {pw[tuple(c % Np for c in v)] for v in o}; assert len(imgs) == 1; pieces[next(iter(imgs))] += 1
        line += "\n    each lower orbit lifts into (pieces: count): %s" % sorted(Counter(pieces.values()).items())
    print(line, flush=True)
    prev = (N, where)
