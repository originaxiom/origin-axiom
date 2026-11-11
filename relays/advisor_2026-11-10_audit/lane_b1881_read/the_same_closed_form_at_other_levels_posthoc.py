#!/usr/bin/env python3
"""POST HOC, and labelled so: where the density of the same closed form peaks at levels 13, 17 and 29.

the_same_closed_form_at_other_levels.py looked for each level's peak on that level's circle, above height 0.07, and
its test did not ask that the greatest value be inside the arc.  At levels 13 and 17 the greatest value was at the
arc's lower end: no peak was located, and that script's "HOLDS" for Z2 and Z3 is not established there.  This script
looks again, over a region and not an arc: real part 0 to 1/2, height 0.048 to 1.6 (the lowest height the tabulated
Bessel function allows).  It has no expectations sealed before it; it was written after the first output was read.

For each level it prints the greatest density found, whether that point is inside the region searched (and so a true
local maximum) or on its floor, whether it lies on the level's circle, and its height once reduced.
    python3 -B the_same_closed_form_at_other_levels_posthoc.py"""
import math
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize

FIELDS = {5: (0, 1), 13: (1, 1), 17: (3, 2), 29: (2, 1)}
NMAX, FLOOR = 320, 0.048
lines = []


def log(x):
    print(x, flush=True); lines.append(x)


t = np.linspace(0.0, 10.0, 20001); wt = np.full(len(t), t[1] - t[0]); wt[0] = wt[-1] = (t[1] - t[0]) / 2
xs = np.concatenate([np.linspace(0.3, 2.0, 1701)[:-1], np.linspace(2.0, 60.0, 5801)])


def state(D):
    """the sine series of the closed form at level D, as the_same_closed_form_at_other_levels.py builds it"""
    w = (1 + math.sqrt(D)) / 2; wc = 1 - w; q = (D - 1) // 4; u, v = FIELDS[D]
    val = lambda a, b: (a + b * w, a + b * wc)
    mul = lambda a, b, c, d: (a * c + b * d * q, a * d + b * c + b * d)
    eps = val(u, v)[0]; R = math.pi / (2 * math.log(eps)); inv = (-(u + v), v)

    def reduced(a, b):
        for _ in range(2000):
            al, co = val(a, b)
            if al < 0: a, b = -a, -b; continue
            tt = math.log(abs(al / co))
            if tt >= 2 * math.log(eps) - 1e-11: a, b = mul(a, b, *inv); continue
            if tt < -1e-11: a, b = mul(a, b, u, v); continue
            return a, b
    ideals = {}; B = int(3.0 * math.sqrt(NMAX) * eps) + 8
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            n = abs(a * a + a * b - q * b * b)
            if 1 <= n <= NMAX: ideals.setdefault(n, set()).add(reduced(a, b))
    c = np.zeros(NMAX + 1)
    for n, gens in ideals.items():
        for (a, b) in gens:
            al, co = val(a, b); c[n] += (1 if al * co > 0 else -1) * math.cos(R * math.log(abs(al / co)))
    tab = np.array([np.sum(wt * np.exp(-x * (np.cosh(t) - 1.0)) * np.cos(R * t)) for x in xs]); spl = CubicSpline(xs, tab)
    K = lambda x: np.where(np.asarray(x) < 60.0, spl(np.clip(x, 0.3, 60.0)) * np.exp(-np.clip(x, 0.3, 60.0)), 0.0)
    ns = np.arange(1, NMAX + 1)[:, None]

    def dens(X, Y):                                     # the density on arrays of points
        X, Y = np.atleast_1d(X).astype(float), np.atleast_1d(Y).astype(float)
        return (np.sqrt(Y) * np.sum(c[1:, None] * K(2 * math.pi * ns * Y[None, :]) * np.sin(2 * math.pi * ns * X[None, :]), axis=0)) ** 2
    return R, dens


def reduce_height(z):
    for _ in range(400):
        z = complex(z.real - round(z.real), z.imag)
        if abs(z) >= 1 - 1e-13: return z
        z = -1 / z
    return z


for D in FIELDS:
    R, dens = state(D)
    X = np.linspace(0.0, 0.5, 251); Y = np.concatenate([np.linspace(FLOOR, 0.3, 505), np.linspace(0.3, 1.6, 261)[1:]])
    G = np.array([dens(X, np.full(len(X), y)) for y in Y])                # rows: heights
    i, j = np.unravel_index(int(np.argmax(G)), G.shape)
    res = minimize(lambda p: -float(dens(p[0], max(p[1], FLOOR))[0]), [X[j], Y[i]], method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-18, "maxiter": 4000})
    x, y = float(res.x[0]), float(max(res.x[1], FLOOR)); top = -res.fun
    inside = (y > FLOOR + 1e-4) and (1e-4 < x < 0.5 - 1e-4)
    floor_share = float(np.max(G[0])) / top
    z = complex(x, y); red = reduce_height(z)
    log("level %2d  R = %.6f  greatest density over the region at %.6f + %.6f i  (%s);  D |z|^2 = %.5f (%s the circle);  reduced to %+.5f + %.5f i;  the greatest on the region's floor is %.3f of it" % (
        D, R, x, y, "inside the region: a true local maximum" if inside else "ON THE EDGE of the region: not located",
        D * abs(z) ** 2, "on" if abs(D * abs(z) ** 2 - 1) < 1e-4 else "off", red.real, red.imag, floor_share))
log("post hoc exit 0")
open(__file__.replace(".py", "_out.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
