"""EXPLORATORY: Rademacher's conjugacy invariant Psi(gamma) (via Dedekind sums) against #L - #R on positive words;
Ghys (2007): Psi(gamma) is the linking number of gamma's modular knot with the trefoil."""
from fractions import Fraction as F
from math import floor
import itertools
def saw(x):
    return F(0) if x.denominator == 1 else x - floor(x) - F(1, 2)
def ded(h, k):
    return sum(saw(F(r, k)) * saw(F(h * r, k)) for r in range(1, k))
def Phi(m):
    a, b, c, d = m
    if c == 0: return F(b, d)
    sg = 1 if c > 0 else -1
    return F(a + d, c) - 12 * sg * ded(a, abs(c))
def Psi(m):
    a, b, c, d = m
    s = (c * (a + d) > 0) - (c * (a + d) < 0)
    return Phi(m) - 3 * s
def mul(x, y):
    return (x[0]*y[0] + x[1]*y[2], x[0]*y[1] + x[1]*y[3], x[2]*y[0] + x[3]*y[2], x[2]*y[1] + x[3]*y[3])
G = {"L": (1, 1, 0, 1), "R": (1, 0, 1, 1)}
bad = 0; n = 0
for k in range(2, 11):
    for w in itertools.product("LR", repeat=k):
        if "L" not in w or "R" not in w: continue
        m = (1, 0, 0, 1)
        for ch in w: m = mul(m, G[ch])
        n += 1
        if Psi(m) != w.count("L") - w.count("R"): bad += 1
print(f"positive words with both letters, length 2..10: {n}; Psi != #L - #R on {bad}")
