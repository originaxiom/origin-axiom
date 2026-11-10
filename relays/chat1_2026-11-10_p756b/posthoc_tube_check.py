#!/usr/bin/env python3
"""
P-756(b), the tau side: a POST HOC second code path for the exponents (the web seat, 2026-11-10).

Not part of the sealed card. Written after the card's output was read, at the owner's question whether the result is
sure. It was run once in scratch before this commit, and that output was read: tube exponents 0.8443 at i, 0.9233 at
i sqrt 2, 1.0837 at (1 + i sqrt 7)/2 and 0.9887 at Q1. This file is committed before the run made in place, whose
output is committed after it. Nothing is imported from the card's script.

What differs from the card:
 - the sampler: random letters L, R as integer matrix products (62 letters), not continued-fraction digits;
 - the quantity: the mass of geodesics passing within delta of a point (the tube), by the closed-form distance
   sinh d = | |z - c|^2 - r^2 | / (2 r Im z) for the geodesic from -zeta to xi (centre c, radius r);
 - the fit: unweighted, over delta = 2^-5 ... 2^-12.
A tube exponent a at z corresponds to the card's slope a - 1 (the density relative to area goes as eps^(a - 1)). At i
every geodesic through the point crosses the edge (0, inf), so the tube is complete there. At the other points this
chart holds only the geodesics that also cross (0, inf), so the exponent is that part's.

Data-free. 0 of 19.
"""
import math
import numpy as np


def sample(rng, n, letters=62):
    a = np.ones(n, np.int64); b = np.zeros(n, np.int64); c = np.zeros(n, np.int64); d = np.ones(n, np.int64)
    for _ in range(letters):
        R = rng.integers(0, 2, n).astype(bool)        # True: x -> x + 1 ; False: x -> x/(x + 1)
        a2 = np.where(R, a, a + b); b2 = np.where(R, a + b, b)
        c2 = np.where(R, c, c + d); d2 = np.where(R, c + d, d)
        a, b, c, d = a2, b2, c2, d2
    return (a + b) / (c + d)


pts = {'i': 1j, 'i sqrt2': 1j * math.sqrt(2), '(1+i sqrt7)/2': complex(0.5, math.sqrt(7) / 2),
       'Q1': complex(0.42, 1.23)}
deltas = [2.0 ** (-k) for k in range(2, 15)]
cnt = {k: np.zeros(len(deltas)) for k in pts}
N = 0
rng = np.random.Generator(np.random.PCG64(424242))
for chunk in range(12):
    xi = sample(rng, 2_000_000)
    ze = sample(rng, 2_000_000)
    N += xi.size
    c = (xi - ze) / 2
    r = (xi + ze) / 2
    for k, z in pts.items():
        dist = np.arcsinh(np.abs((z.real - c) ** 2 + z.imag ** 2 - r ** 2) / (2 * r * z.imag))
        for j, dl in enumerate(deltas):
            cnt[k][j] += np.count_nonzero(dist < dl)
print('samples', N)
lx = np.log(np.array(deltas))
for k in pts:
    T = cnt[k] / N
    sel = slice(3, 11)                                  # delta = 2^-5 ... 2^-12
    sl = np.polyfit(lx[sel], np.log(T[sel]), 1)[0]
    loc = np.diff(np.log(T)) / np.diff(lx)
    print(f"{k:14s} tube exponent {sl:.4f}  (the card's slope would be {sl - 1:+.4f})  count at 2^-12: {int(cnt[k][10])}")
    print('     local:', ' '.join(f'{x:.3f}' for x in loc))
