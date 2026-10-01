#!/usr/bin/env python3
"""The slope as a sum over the letters of the word (numerical check of the closed form against the exact slopes).

Gauge: for a character chi = (X, Y) of F with X != 1, sigma(chi) is the cocycle with sigma(x) = 0, sigma(y) = 1/(X - 1)
(longitude value 1).  Pulling back by one twist changes the gauge by a multiple a of the coboundary of 1:
    tau_x (L: x -> x,  y -> yx):   chi' = (X, XY),   a = 0
    tau_y (R: x -> xy, y -> y ):   chi' = (XY, Y),   a = X / ((X - 1)(XY - 1))
    iota  (-I):                    chi' = (1/X, 1/Y), a = 1 / (1 - X)
and s(chi) = - (sum of a along the closed orbit of chi under the letters of Phi).
With X = exp(2 pi i a_j) before an R-step and exp(2 pi i a_j') after it:
    - X / ((X - 1)(X' - 1)) = (1 + cot(pi a_j) cot(pi a_j')) / 4 - i (cot(pi a_j) - cot(pi a_j')) / 4 .
"""
import sys, cmath, math, itertools
from slope_law import exact_slopes, ic
def numeric(el):
    N = el.F.N; z = cmath.exp(2j * math.pi / N); return sum(float(c) * z ** i for i, c in enumerate(el.c))
def letters(eps, word, k):
    """the elementary steps in the order characters are pulled back: chi -> chi o step"""
    one = (["I"] if eps < 0 else []) + list(word)
    return one * k
def orbit_sum(i, j, N, steps):
    """returns (-sum a, ok) with ok False if X = 1 is met (the gauge is not defined there)"""
    tot = 0j; a, b = i % N, j % N; cot_sum = 0.0; nR = 0
    for st in steps:
        if a % N == 0: return None
        Xc = cmath.exp(2j * math.pi * a / N)
        if st == "L": b = (a + b) % N                      # chi o tau_x = (X, XY)
        elif st == "R":
            a2 = (a + b) % N
            if a2 % N == 0: return None
            X2 = cmath.exp(2j * math.pi * a2 / N); tot += Xc / ((Xc - 1) * (X2 - 1))
            cot_sum += (1 + 1 / math.tan(math.pi * a / N) / math.tan(math.pi * a2 / N)) / 4; nR += 1
            a = a2
        else:
            tot += 1 / (1 - Xc); a, b = (-a) % N, (-b) % N
    assert (a, b) == (i % N, j % N), "the orbit closes"
    return -tot, cot_sum

def orbit_sum_general(i, j, N, steps):
    """the same sum with the gauge chosen letter by letter: gauge A (sigma(x) = 0) where X != 1, else gauge B
    (sigma(y) = 0, sigma(x) = 1/(1 - Y)).  Defined for every non-trivial character."""
    z = lambda e: cmath.exp(2j * math.pi * (e % N) / N)
    def sigma(a, b):
        Xc, Yc = z(a), z(b)
        return (0j, 1 / (Xc - 1)) if a % N else (1 / (1 - Yc), 0j)
    a, b = i % N, j % N; tot = 0j
    for st in steps:
        Xc, Yc = z(a), z(b); p, q = sigma(a, b)
        if st == "L": p2, q2 = p, q + Yc * p; a2, b2 = a, (a + b) % N            # u(yx) = u(y) + Y u(x)
        elif st == "R": p2, q2 = p + Xc * q, q; a2, b2 = (a + b) % N, b          # u(xy) = u(x) + X u(y)
        else:                                                                     # u(c g^-1 c^-1), c = yx
            uc = q + Yc * p; chic = Xc * Yc
            p2 = (1 - 1 / Xc) * uc - chic / Xc * p; q2 = (1 - 1 / Yc) * uc - chic / Yc * q; a2, b2 = (-a) % N, (-b) % N
        ps, qs = sigma(a2, b2); X2, Y2 = z(a2), z(b2)
        assert abs((1 - Y2) * p2 + (X2 - 1) * q2 - 1) < 1e-9, "the pulled-back cocycle keeps the longitude value"
        tot += (p2 - ps) / (X2 - 1) if a2 % N else (q2 - qs) / (Y2 - 1)
        a, b = a2, b2
    assert (a, b) == (i % N, j % N)
    return -tot
if __name__ == "__main__":
    worst = 0.0; n = 0; skipped = 0; nreal = 0; worst_cot = 0.0; ncot = 0; worst_gen = 0.0; ngen = 0
    for (st, k) in [("+LR", 2), ("+LR", 3), ("+LR", 4), ("+LR", 5), ("-LR", 3), ("+LLR", 3), ("-LLRLR", 1), ("-LLLRLR", 1), ("+LLLR", 3), ("-LLRR", 3), ("+LLRLR", 2)]:
        eps = 1 if st[0] == "+" else -1; N, F, S = exact_slopes(eps, st[1:], k); steps = letters(eps, st[1:], k)
        for (i, j, _), s in S.items():
            if isinstance(s, str): continue
            g = orbit_sum_general(i, j, N, steps); worst_gen = max(worst_gen, abs(g - numeric(s))); ngen += 1
            r = orbit_sum(i, j, N, steps)
            if r is None: skipped += 1; continue
            val, cs = r; ex = numeric(s); worst = max(worst, abs(val - ex)); n += 1
            nreal += abs(ex.imag) < 1e-9
            if eps > 0: worst_cot = max(worst_cot, abs(cs - ex)); ncot += 1
        print(st, k, "characters", len(S) - 1, "checked so far", n, "skipped (X = 1 on the orbit)", skipped, "max |formula - exact|", "%.2e" % worst, flush=True)
    print("general gauge, every non-trivial character: max error", "%.2e" % worst_gen, "over", ngen)
    print("slopes real:", nreal, "of", n, "; cotangent form on + states: max error", "%.2e" % worst_cot, "over", ncot)
