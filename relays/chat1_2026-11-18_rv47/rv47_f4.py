#!/usr/bin/env python3
"""The status page's section 9: an independent check of main's refutation of step 3 of this seat's session relay of
2026-09-08 ("every sl2 of E6 conjugates into F4"). Data-free, exact. Computed once, post hoc; written without reading
main's checks/web_session_relay_f4.py.

    python3 -I -u rv47_f4.py

The 27 of E6 is minuscule: its weights are the Weyl orbit of the fundamental weight w1. An sl2 with weighted Dynkin
diagram (a_1, ..., a_6) (Bourbaki order: chain 1-3-4-5-6, node 2 on node 4) acts on a weight lam = sum q_i alpha_i
with h-eigenvalue sum q_i a_i, so the h-spectrum of the 27 gives its sl2 decomposition. F4, the fixed points of the
diagram involution, fixes a vector of the 27 (27 = 26 + 1), so an sl2 inside F4 has a trivial summand.
  P1  the regular sl2 (all a_i = 2): expect 17 + 9 + 1.
  P2  the subregular sl2 E6(a1) (a_i = 2, a_4 = 0): its decomposition, and whether it has a trivial summand.
  P3  the minimal sl2 A1 (a_2 = 1, all others 0): its decomposition (a control with a trivial part).
"""
from fractions import Fraction as Fr
from collections import Counter

# Cartan matrix of E6, Bourbaki numbering 1..6 (indices 0..5)
edges = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]
C = [[2 if i == j else 0 for j in range(6)] for i in range(6)]
for a, b in edges:
    C[a - 1][b - 1] = C[b - 1][a - 1] = -1


def inv(M):
    n = len(M); A = [[Fr(x) for x in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0); A[c], A[p] = A[p], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                A[r] = [x - A[r][c] * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


Ci = inv(C)
w1 = tuple(Ci[0])                     # w1 in simple-root coordinates (row 1 of C^-1, C symmetric)


def pair(q, i):                       # <lam, alpha_i^vee> for lam = sum q_j alpha_j
    return sum(q[j] * C[j][i] for j in range(6))


orbit = {w1}; frontier = [w1]
while frontier:
    nxt = []
    for q in frontier:
        for i in range(6):
            k = pair(q, i)
            if k != 0:
                r = tuple(q[j] - (k if j == i else 0) for j in range(6))
                if r not in orbit:
                    orbit.add(r); nxt.append(r)
    frontier = nxt
assert len(orbit) == 27, len(orbit)


def decompose(a):
    spec = Counter(sum(q[i] * a[i] for i in range(6)) for q in orbit)
    assert all(v.denominator == 1 for v in spec)
    out = []
    for m in sorted({int(v) for v in spec if v >= 0}, reverse=True):
        n = spec[Fr(m)] - spec[Fr(m + 2)]
        out += [m + 1] * n
    return out


for name, a in (("P1 regular", (2, 2, 2, 2, 2, 2)), ("P2 subregular E6(a1)", (2, 2, 2, 0, 2, 2)),
                ("P3 minimal A1", (0, 1, 0, 0, 0, 0))):
    d = decompose(a)
    print("%s: the 27 = %s (sum %d); a trivial summand: %s" % (name, " + ".join(map(str, d)), sum(d), 1 in d))
