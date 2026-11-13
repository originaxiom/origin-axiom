#!/usr/bin/env python3
"""POST HOC 2 of W-C5: a diagnosis of post hoc 1's line R2 ("the rule agrees with the numerical decision at all: False").
It prints every grid point where post hoc 1's numerical decision differs from the rule n <= b(a), with the three
partial integrals it used. No expectation is changed; this file only shows where the two disagree and why.
"""
import mpmath


def b(a):
    return (a - 1) // 2 if a >= 1 else a // 2


rows = []
for a in range(-8, 10):
    for n in range(-8, 9):
        c = a - 2 * n
        f = lambda u: u ** (a - 2) * mpmath.e ** (-c * u)
        G = lambda X: mpmath.quad(f, mpmath.linspace(1, X, 40))
        g25, g100, g400 = G(25), G(100), G(400)
        d1, d2 = g100 - g25, g400 - g100
        num = bool(abs(d2) < 1e-20 or d2 <= 0.5 * d1)
        if num != (n <= b(a)):
            rows.append((a, n, c, num, n <= b(a), mpmath.nstr(d1, 5), mpmath.nstr(d2, 5)))
print("points where the numerical decision and the rule differ:", len(rows), flush=True)
for r in rows:
    print("a %d n %d a-2n %d numerical finite %s rule finite %s  G(100)-G(25) %s  G(400)-G(100) %s" % r, flush=True)
