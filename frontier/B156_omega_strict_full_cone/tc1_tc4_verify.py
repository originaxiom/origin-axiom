#!/usr/bin/env python
"""Independent re-derivation of TC-1 (Ω4 unique minimal strict-full seed) and
TC-4 (orientation no-go), surfaced by the ChatGPT/Ω history cross-check.

Fresh code; does NOT import the handoff scripts. pyenv `python`. All PASS required.

TC-1: the minimal level at which any strongly-connected positive-shear history exists
is L=4 (a strongly connected digraph on 4 nodes needs >=4 edges), and among ALL
strongly-connected L=4 histories the strict-full ones (per-matrix nondegenerate
invariant form) have characteristic polynomial EXACTLY x^4-4x^3+5x^2-4x+1 = (4,5,4)
= golden x phase, and nothing else. So the Ω4 seed is the unique minimal strict-full
seed.

TC-4: define the orientation Ω(w) = Pfaffian of the antisymmetrized dependency-count
matrix A_{ij}=C_{ij}-C_{ji} (C_{ij} = #times edge j->i used), i.e.
Pf = A01 A23 - A02 A13 + A03 A12. Under a relabeling π of the 4 nodes,
A -> Pπ A Pπ^T so Ω(πw) = sign(π) Ω(w) (Pfaffian transforms by det(Pπ)=sign(π)),
while the matrix M(πw)=Pπ M(w) Pπ^T preserves strong-connectivity and strict-fullness.
Hence any relabel-closed ensemble pairs each w (via an ODD π) with a partner of
opposite Ω, so the NET orientation residual is 0. Verified symbolically (the sign law)
and exactly (net sum = 0 over all SC histories at L4 and L5).
"""
from __future__ import annotations
import itertools
from collections import Counter
import sympy as sp

N = 4
EDGES = tuple((i, j) for i in range(N) for j in range(N) if i != j)
IDENTITY = tuple(tuple(1 if i == j else 0 for j in range(N)) for i in range(N))
_S = sp.symbols("s0:10")
_IDX = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

ok = True
def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")


def apply_shear(M, i, j):
    r = [list(x) for x in M]
    r[i] = [r[i][k] + r[j][k] for k in range(N)]
    return tuple(tuple(x) for x in r)


def mat_of(hist):
    M = IDENTITY
    for i, j in hist:
        M = apply_shear(M, i, j)
    return M


def charpoly_abc(M):
    def mm(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)) for i in range(N))
    A2 = mm(M, M); A3 = mm(A2, M)
    t1 = sum(M[i][i] for i in range(N)); t2 = sum(A2[i][i] for i in range(N)); t3 = sum(A3[i][i] for i in range(N))
    return (t1, (t1 * t1 - t2) // 2, (t1 ** 3 - 3 * t1 * t2 + 2 * t3) // 6)


def strongly_connected(hist):
    adj = [set() for _ in range(N)]; radj = [set() for _ in range(N)]
    for i, j in hist:
        adj[j].add(i); radj[i].add(j)
    def reach(g):
        seen = {0}; st = [0]
        while st:
            u = st.pop()
            for v in g[u]:
                if v not in seen:
                    seen.add(v); st.append(v)
        return len(seen) == N
    return reach(adj) and reach(radj)


def is_full_metric(M, cache):
    if M in cache:
        return cache[M]
    G = sp.zeros(N)
    for v, (i, j) in zip(_S, _IDX):
        G[i, j] = v; G[j, i] = v
    A = sp.Matrix(M)
    eqs = [(A.T * G * A - G)[i, j] for i in range(N) for j in range(i, N)]
    Aeq, _ = sp.linear_eq_to_matrix(eqs, _S)
    basis = Aeq.nullspace()
    if not basis:
        cache[M] = False; return False
    Gg = sp.zeros(N)
    for c, vec in zip(_S, basis):
        B = sp.zeros(N)
        for val, (i, j) in zip(vec, _IDX):
            B[i, j] = val; B[j, i] = val
        Gg += c * B
    res = sp.expand(Gg.det()) != 0
    cache[M] = bool(res); return bool(res)


def orientation(hist):
    C = [[0] * N for _ in range(N)]
    for i, j in hist:
        C[j][i] += 1          # dependency edge j -> i
    A = [[C[i][j] - C[j][i] for j in range(N)] for i in range(N)]
    return A[0][1] * A[2][3] - A[0][2] * A[1][3] + A[0][3] * A[1][2]


# ---------------------------------------------------------------- TC-1
print("== TC-1: Ω4 is the unique minimal strict-full seed ==")
# minimality: no strongly-connected history of length < 4
sc_below = any(strongly_connected(h) for L in (1, 2, 3) for h in itertools.product(EDGES, repeat=L))
check("no strongly-connected history at L<4 (minimal level is 4)", not sc_below)

cache = {}
full_charpolys = set()
sc_count = 0
seed_paths = 0
for h in itertools.product(EDGES, repeat=4):
    if not strongly_connected(h):
        continue
    sc_count += 1
    M = mat_of(h)
    if is_full_metric(M, cache):
        abc = charpoly_abc(M)
        full_charpolys.add(abc)
        if abc == (4, 5, 4):
            seed_paths += 1
print(f"    SC L4 histories: {sc_count}; strict-full charpolys: {sorted(full_charpolys)}; (4,5,4) paths: {seed_paths}")
check("every strict-full L4 history has charpoly (4,5,4) = golden×phase", full_charpolys == {(4, 5, 4)})
check("the Ω4 seed count is 96", seed_paths == 96)

# ---------------------------------------------------------------- TC-4
print("== TC-4: orientation no-go (zero net Pfaffian residual) ==")
# (a) sign law: Pf(Pπ A Pπ^T) = sign(π) Pf(A) for the 4x4 antisymmetric Pfaffian
a = sp.symbols("a01 a02 a03 a12 a13 a23")
A = sp.Matrix([
    [0,      a[0],  a[1],  a[2]],
    [-a[0],  0,     a[3],  a[4]],
    [-a[1], -a[3],  0,     a[5]],
    [-a[2], -a[4], -a[5],  0],
])
Pf = a[0] * a[5] - a[1] * a[4] + a[2] * a[3]   # A01 A23 - A02 A13 + A03 A12
def perm_mat(p):
    P = sp.zeros(N)
    for i in range(N):
        P[i, p[i]] = 1
    return P
def pf_of(M):
    return M[0, 1] * M[2, 3] - M[0, 2] * M[1, 3] + M[0, 3] * M[1, 2]
odd = (1, 0, 2, 3)        # transposition (0 1): odd
even = (1, 2, 0, 3)       # 3-cycle (0 1 2): even
Po, Pe = perm_mat(odd), perm_mat(even)
check("Pf(A) matches the A01A23-A02A13+A03A12 formula", sp.expand(pf_of(A) - Pf) == 0)
check("odd relabel flips Pfaffian sign: Pf(PAP^T) = -Pf(A)",
      sp.expand(pf_of(Po * A * Po.T) + Pf) == 0)
check("even relabel preserves Pfaffian: Pf(PAP^T) = +Pf(A)",
      sp.expand(pf_of(Pe * A * Pe.T) - Pf) == 0)

# (b) relabeling preserves strong-connectivity AND strict-fullness (conjugation by Pπ);
#     and maps orientation by sign(π). Check on the strict-full survivors at L4.
def relabel_hist(hist, p):
    return tuple((p[i], p[j]) for i, j in hist)
relabel_ok = True
orient_law_ok = True
for h in itertools.product(EDGES, repeat=4):
    if not strongly_connected(h):
        continue
    M = mat_of(h)
    if not is_full_metric(M, cache):
        continue
    hp = relabel_hist(h, odd)
    if not (strongly_connected(hp) and is_full_metric(mat_of(hp), cache)):
        relabel_ok = False; break
    if orientation(hp) != -orientation(h):   # odd π => sign flip
        orient_law_ok = False; break
check("odd relabel preserves SC + strict-fullness (ensemble closed)", relabel_ok)
check("odd relabel flips orientation on strict-full histories", orient_law_ok)

# (c) net orientation residual = 0 over all SC histories at L4 and L5 (exact)
for L in (4, 5):
    s = sum(orientation(h) for h in itertools.product(EDGES, repeat=L) if strongly_connected(h))
    check(f"net orientation residual = 0 over all SC histories at L{L}", s == 0)

print("\nALL PASS" if ok else "\nSOME FAILED")
import sys
sys.exit(0 if ok else 1)
