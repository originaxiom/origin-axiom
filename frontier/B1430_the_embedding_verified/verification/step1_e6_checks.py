"""Step 1: build E6 from scratch and check it."""
from fractions import Fraction as F
from rootsys import *
import json, sys

simple = E6_simple()
roots = generate_roots(simple)

print("=== E6 ROOT SYSTEM CHECKS ===")
print("ambient dimension of the coordinates:", len(simple[0]))
print("number of roots produced by reflection-closure:", len(roots))

# lengths
lens = sorted({ip(r, r) for r in roots})
print("distinct squared lengths among the roots:", [str(x) for x in lens])

# rank
print("rank (exact Q-rank of the span of all roots):", rank_of(roots))
print("rank of the simple system:", rank_of(simple))

# reducedness: only +-r proportional
idx = {r: i for i, r in enumerate(roots)}
red = True
for r in roots:
    for k in (F(2), F(3), F(1, 2), F(-2), F(3, 2)):
        if tuple(k * x for x in r) in idx:
            red = False
print("reduced (no root is a non-trivial multiple of another):", red)

# closure under ALL reflections (not just simple)
allclosed = True
S = set(roots)
for r in roots:
    for a in roots:
        if refl(r, a) not in S:
            allclosed = False
print("closed under every root reflection:", allclosed)

# Cartan matrix
A = cartan_matrix(simple)
print("Cartan matrix (rows i, cols j, A_ij = 2(ai,aj)/(aj,aj)):")
for row in A:
    print("   ", [int(x) for x in row])

# intrinsic Dynkin-shape check (no table lookup)
edges = dynkin_edges(simple)
print("Dynkin edges (i,j, A_ij*A_ji):", edges)
n = len(simple)
deg = [0] * n
for (i, j, p) in edges:
    deg[i] += 1
    deg[j] += 1
print("degree sequence:", sorted(deg))
print("all bonds single (simply laced):", all(p == 1 for (_, _, p) in edges))
print("is a tree (n-1 edges, connected):", len(edges) == n - 1)
# branch lengths from the trivalent node
tri = [i for i in range(n) if deg[i] == 3]
print("trivalent nodes:", tri)
adj = {i: [] for i in range(n)}
for (i, j, _) in edges:
    adj[i].append(j)
    adj[j].append(i)


def branch_len(start, prev):
    L = 1
    cur, pr = start, prev
    while True:
        nxt = [x for x in adj[cur] if x != pr]
        if not nxt:
            return L
        pr, cur = cur, nxt[0]
        L += 1


if tri:
    c = tri[0]
    bl = sorted(branch_len(x, c) for x in adj[c])
    print("branch lengths from the trivalent node:", bl,
          "-> D/E shape (1,2,2) is E6" if bl == [1, 2, 2] else "")

# Weyl group order by explicit permutation-group closure
order, group = weyl_group_order(roots, simple)
print("|W| by BFS closure of the permutation group on the 72 roots:", order)
print("|W| == 51840:", order == 51840)

# sanity: W is transitive on roots
orb = {0}
gens = simple_reflection_perms(roots, simple)
frontier = [0]
while frontier:
    nf = []
    for x in frontier:
        for g in gens:
            y = g[x]
            if y not in orb:
                orb.add(y)
                nf.append(y)
    frontier = nf
print("W-orbit of one root has size:", len(orb), "(transitive on roots:",
      len(orb) == len(roots), ")")

# number of roots at each inner product with a fixed root
a = roots[0]
from collections import Counter
print("multiset of (a,b) for fixed root a:",
      dict(Counter(str(ip(a, b)) for b in roots)))

with open("e6_roots.json", "w") as f:
    json.dump([[str(x) for x in r] for r in roots], f)
print("wrote e6_roots.json")
