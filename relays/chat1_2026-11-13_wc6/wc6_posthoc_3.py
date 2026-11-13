#!/usr/bin/env python3
"""W-C6, post hoc 3, written after post hoc 2 and committed before its own run.

Post hoc 2's C1 (the Poisson form against the direct sum at s = 3) failed at two points of c = (0.62, 0.09), where
|m + u1| is smallest (0.12): at s = 3 the Bessel series in k carries (k / Y)^(5/2) and was cut at k = 30.
EXPECTATION, written before the run: with the k series cut at 150 instead, C1 holds within 1e-9 at all twelve points.

    python3 -I -u wc6_posthoc_3.py
"""
import contextlib, io, runpy, pathlib
import numpy as np, mpmath as mp

mp.mp.dps = 30
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(str(pathlib.Path(__file__).with_name("wc6_checks.py")))
    h = runpy.run_path(str(pathlib.Path(__file__).with_name("wc6_posthoc_2.py")))


def Zp3(u1, u2, tau, K=150):
    s = mp.mpf(3); y = mp.mpf(tau.imag); X = mp.mpf(tau.real); f = mp.mpf(u1) % 1
    first = mp.sqrt(mp.pi) * mp.gamma(s - 0.5) / mp.gamma(s) * y ** (1 - 2 * s) * (mp.zeta(2 * s - 1, f) + mp.zeta(2 * s - 1, 1 - f))
    rest = mp.mpf(0)
    for m in range(-60, 61):
        p = m + mp.mpf(u1); Y = abs(p) * y; x = p * X + u2
        for k in range(1, K + 1):
            rest += 2 * (k / Y) ** (s - 0.5) * mp.besselk(s - 0.5, 2 * mp.pi * k * Y) * 2 * mp.cos(2 * mp.pi * k * x)
    return y ** s * (first + mp.pi ** s / mp.gamma(s) * rest)


ok = True
for c, tau, *_ in g["rows"]:
    u1, u2 = c[0] - 0.5, c[1] - 0.5
    d = float(Zp3(u1, u2, tau)) - h["Zdirect3"](u1, u2, tau)
    print("c", c, "tau", tau, "C1' %.1e" % d, flush=True)
    ok &= abs(d) < 1e-9
print("C1' Poisson form (k to 150) = direct sum at s = 3 at all points:", ok)
