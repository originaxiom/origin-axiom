"""R63 -- adjoint (78) and 27 decompositions of e6 under the principal and subregular sl2, from the root system. Exact."""
import numpy as np
from collections import Counter
from fractions import Fraction as Fr
C = [[ 2, 0,-1, 0, 0, 0],[ 0, 2, 0,-1, 0, 0],[-1, 0, 2,-1, 0, 0],[ 0,-1,-1, 2,-1, 0],[ 0, 0, 0,-1, 2,-1],[ 0, 0, 0, 0,-1, 2]]
simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]
pos, fr = set(simple), list(simple)
def pairing(beta, i): return sum(beta[j]*C[j][i] for j in range(6))
while fr:
    beta = fr.pop()
    for i in range(6):
        p, b = 0, list(beta); b[i] -= 1
        while tuple(b) in pos: p += 1; b[i] -= 1
        if p - pairing(beta, i) > 0:
            nb = list(beta); nb[i] += 1; nb = tuple(nb)
            if nb not in pos: pos.add(nb); fr.append(nb)
roots = list(pos) + [tuple(-c for c in r) for r in pos]; assert len(roots) == 72
# 27 weights in fundamental coords -> simple-root coords via C^-1 (fractions)
Cinv = np.linalg.inv(np.array(C, dtype=float))
def reflect(wt, i): return tuple(wt[j] - wt[i]*C[i][j] for j in range(6))
w0 = tuple(int(j == 0) for j in range(6)); W27, fr = {w0}, [w0]
while fr:
    v = fr.pop()
    for i in range(6):
        u = reflect(v, i)
        if u not in W27: W27.add(u); fr.append(u)
assert len(W27) == 27
def decompose(weights):     # multiset of integer h-weights -> list of sl2 irrep dims
    cnt = Counter(weights); dims = []
    for m in sorted(cnt, reverse=True):
        while cnt[m] > 0:
            n = m + 1; dims.append(n)
            for k in range(-m, m+1, 2): cnt[k] -= 1
    assert all(v == 0 for v in cnt.values()), cnt
    return sorted(dims, reverse=True)
def index_from(dims, ref):   # Dynkin index relative to the rep's own index
    return Fr(sum(n*(n*n-1) for n in dims), 6) / ref
for name, c in (("principal (2,2,2,2,2,2)", (2,2,2,2,2,2)), ("subregular (2,2,2,0,2,2)", (2,2,2,0,2,2))):
    adj_w = [sum(c[i]*r[i] for i in range(6)) for r in roots] + [0]*6
    adj = decompose(adj_w)
    w27 = [round(float(np.array(v) @ Cinv @ np.array(c))) for v in W27]   # <h, weight> with h = sum c_i alpha_i^vee: weight in fundamental coords . C^-1 . c
    d27 = decompose(w27)
    print(f"{name}\n   78 = {' + '.join(map(str, adj))}   [V2 (spin-2) count = {adj.count(3)}, trivial summands = {adj.count(1)}]"
          f"\n   27 = {' + '.join(map(str, d27))}\n   Dynkin index via adjoint (index(78)=24): {index_from(adj, 24)};  via the 27 (index(27)=6): {index_from(d27, 6)}")
