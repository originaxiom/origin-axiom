#!/usr/bin/env python3
"""E8 Chevalley basis, sparse and on demand -- the carrier for the 27's cubic form.

e8 has a Z/3-grading by the coefficient of alpha_7 mod 3 (its mark in the highest
root is 3), with

    deg 0 : e6 (+) sl3        86 = 78 + 8
    deg 1 : (27, 3)           81
    deg 2 : (27bar, 3bar)     81

so [deg1, deg1] subset deg2 realises the quadratic adjoint of the 27 -- which is
exactly what e7 cannot do (its grading is 3-step and [27,27] = 0 there).

Everything is the SAME construction as the paper's check_charge_bracket.py, with the
E8 Cartan matrix substituted; brackets are computed on demand because the full table
would be 248^2 x 248 rationals.
"""
from fractions import Fraction

N = 8
# Bourbaki E8: chain 1-3-4-5-6-7-8, node 2 attached to node 4  (0-indexed below)
EDGES = [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1
# the first six nodes are exactly E6 (Bourbaki), matching the paper's matrix
E6_A = [[A[i][j] for j in range(6)] for i in range(6)]


def build_roots():
    simples = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
    roots = set(simples)
    frontier = list(simples)
    while frontier:
        nxt = []
        for r in frontier:
            for j in range(N):
                pair = sum(r[i] * A[i][j] for i in range(N))
                s = tuple(r[i] - pair * (1 if i == j else 0) for i in range(N))
                if any(s) and s not in roots:
                    roots.add(s)
                    nxt.append(s)
        frontier = nxt
    return sorted(roots)


ROOTS = build_roots()
IDX = {r: k for k, r in enumerate(ROOTS)}
DIM = N + len(ROOTS)

B_COCYCLE = [[0] * N for _ in range(N)]
for i in range(N):
    B_COCYCLE[i][i] = 1
    for j in range(i + 1, N):
        B_COCYCLE[i][j] = A[i][j] % 2


def eps(a, b):
    s = sum(B_COCYCLE[i][j] * a[i] * b[j] for i in range(N) for j in range(N))
    return -1 if s % 2 else 1


# ---- sparse vectors: dict index -> Fraction ----------------------------------------
def hv(i):
    return {i: Fraction(1)}


def ev(r):
    return {N + IDX[r]: Fraction(1)}


def vadd(u, v):
    out = dict(u)
    for k, c in v.items():
        out[k] = out.get(k, Fraction(0)) + c
        if out[k] == 0:
            del out[k]
    return out


def vmul(c, u):
    c = Fraction(c)
    return {} if c == 0 else {k: c * val for k, val in u.items()}


def bracket_basis(p, q):
    if p < N and q < N:
        return {}
    if p < N:
        r = ROOTS[q - N]
        c = sum(r[k] * A[k][p] for k in range(N))
        return {q: Fraction(c)} if c else {}
    if q < N:
        r = ROOTS[p - N]
        c = sum(r[k] * A[k][q] for k in range(N))
        return {p: Fraction(-c)} if c else {}
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if not any(s):
        sgn = eps(a, b)
        return {i: Fraction(sgn * a[i]) for i in range(N) if a[i]}
    if s in IDX:
        return {N + IDX[s]: Fraction(eps(a, b))}
    return {}


_CACHE = {}


def bb(p, q):
    key = (p, q)
    if key not in _CACHE:
        _CACHE[key] = bracket_basis(p, q)
    return _CACHE[key]


def br(u, v):
    out = {}
    for p, up in u.items():
        for q, vq in v.items():
            row = bb(p, q)
            if not row:
                continue
            c = up * vq
            for k, rk in row.items():
                nv = out.get(k, Fraction(0)) + c * rk
                if nv == 0:
                    out.pop(k, None)
                else:
                    out[k] = nv
    return out


def is_zero(u):
    return not u


def killing_pair(u, v):
    """Normalised invariant form: <e_a, e_-a> = eps(a,-a), <h_i, h_j> = (a_i,a_j)."""
    tot = Fraction(0)
    for p, up in u.items():
        for q, vq in v.items():
            if p < N and q < N:
                tot += up * vq * A[p][q]
            elif p >= N and q >= N:
                a, b = ROOTS[p - N], ROOTS[q - N]
                if all(a[i] + b[i] == 0 for i in range(N)):
                    tot += up * vq * eps(a, b)
    return tot
