#!/usr/bin/env python3
"""W-F3, post hoc 1: written after the sealed run, committed before its own run.

The sealed run's K2 was not met: with a cone point of finite order, on the odd levels 3 and 5, two characters keep a
non-zero gap. This seat's reading before running this file: on a closed space, rational duality with the orientation
character gives h^2(V) = h^1(V* (x) w) and h^3(V) = h^0(V* (x) w), and the Euler characteristic is 0, so
    gap(V) = h^1(V) - h^1(V* (x) w) = h^0(V) - h^0(V* (x) w),
an invariant-vector term. The two characters should be the trivial one and w itself (gap +1 and -1).
EXPECTATIONS:
  Q1  For every finite k in 2..6, every level in 3..6 and every character: gap = h^0(V) - h^0(V* (x) w).
  Q2  The characters with a non-zero gap at finite k are exactly the trivial character (gap +1) and w (gap -1), on the
      odd levels only.

    python3 -I -u wf3_posthoc_1.py
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, sig_pow, abel2, LAM, conjugator = ns["red"], ns["inv"], ns["sig_pow"], ns["abel2"], ns["LAM"], ns["conjugator"]
Rep, cohomology, find_prime = ns["Rep"], ns["cohomology"], ns["find_prime"]


def prime_factors(m):
    fs, d = set(), 2
    while d * d <= m:
        while m % d == 0:
            fs.add(d)
            m //= d
        d += 1
    if m > 1:
        fs.add(m)
    return fs


p = find_prime(2 * 16 * 9 * 5 * 11 * 29 * 7, 1)
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
q1, q2 = True, True
for n in range(3, 7):
    f = sig_pow(n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    e = tor // gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    g, s = conjugator(n)
    mu = red(inv(g) + (3,))
    w = p - 1 if n % 2 else 1
    z = pow(gen, (p - 1) // (2 * e), p)
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
    chars = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)) for (a1, a2) in fib for j in range(2 * e)]
    base = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    for k in range(2, 7):
        rels = base + [red(LAM * k)]
        nonzero = []
        for ch in chars:
            V = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)
            W = Rep({1: [[pow(ch[0], p - 2, p)]], 2: [[pow(ch[1], p - 2, p)]], 3: [[pow(ch[2], p - 2, p) * w % p]]}, p)
            cV, cW = cohomology(V, rels, mu, LAM), cohomology(W, rels, mu, LAM)
            gp = cV["h1"] - cW["h1"]
            q1 &= gp == cV["h0"] - cW["h0"]
            if gp:
                kind = "trivial" if ch == (1, 1, 1) else "w" if ch == (1, 1, w) else "other"
                nonzero.append((kind, gp))
        want = [("trivial", 1), ("w", -1)] if n % 2 else []
        q2 &= sorted(nonzero) == sorted(want)
        print("level", n, "k", k, "| characters with a non-zero gap:", sorted(nonzero), flush=True)
print("Q1 gap = h0(V) - h0(V* w) for every character:", q1, "; Q2 only the trivial character and w, odd levels only:", q2)
