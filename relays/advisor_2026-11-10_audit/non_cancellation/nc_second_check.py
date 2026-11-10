#!/usr/bin/env python3
"""A second, independent check of the enumeration's headline cases: sympy integer matrices, no modular arithmetic
until the end, a different code path from nc_enumerate.py. Also brute-forces golden level 5 to 12 letters afresh."""
import itertools, sympy as sp
L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]]); I = sp.eye(2)
def D(runs):
    M = sp.eye(2)
    for i, r in enumerate(runs): M = M * (L if i % 2 == 0 else R) ** r
    return M
def E(S, b=1): return D(S) * D([b] * len(S)).inv()
def cls(S, N, b=1):
    e = E(S, b).applyfunc(lambda x: x % N); A = (L**b * R**b)
    plus = e == I.applyfunc(lambda x: x % N); minus = e == (-I).applyfunc(lambda x: x % N)
    com = (E(S, b) * A - A * E(S, b)).applyfunc(lambda x: x % N) == sp.zeros(2)
    return "charge+" if plus else "charge-" if minus else "line only" if com else "visible"
cases = [((6,), 5, 1), ((2, 2, 2), 5, 1), ((2, 1, 1, 1, 2), 5, 1), ((2, 2, 1, 5), 5, 1), ((2, 1, 1, 1, 1, 5), 5, 1),
         ((8,), 7, 1), ((12,), 11, 1), ((2, 1, 3, 1, 1, 1, 1, 3, 1, 2), 60, 1), ((2, 2, 2, 2, 1, 1, 4, 4), 60, 1),
         ((2, 1, 2, 4, 4), 20, 1), ((10,), 8, 2), ((1, 2, 1, 2, 1, 2, 1), 8, 2), ((2, 1, 1, 3, 6), 13, 3),
         ((1, 5, 1, 1, 1, 1, 1, 2), 13, 3), ((16,), 13, 3)]
for S, N, b in cases: print("b=%d N=%-3d %-34s letters %-3d %s" % (b, N, S, sum(S), cls(S, N, b)))
# fresh brute force, golden, level 5, all defects to 12 letters
def comps(n):
    if n == 0: yield (); return
    for r in range(1, n + 1):
        for rest in comps(n - r): yield (r,) + rest
found = {"charge+": [], "charge-": [], "line only": []}
for n in range(2, 13):
    for S in comps(n):
        if S[0] < 2 or S[-1] < 2: continue
        c = cls(S, 5)
        if c in found: found[c].append(S)
for k, v in found.items(): print(k, "to 12 letters:", len(v), "| shortest:", sorted(v, key=lambda s: (sum(s), s))[:4])
