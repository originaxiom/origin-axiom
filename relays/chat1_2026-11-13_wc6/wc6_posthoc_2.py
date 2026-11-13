#!/usr/bin/env python3
"""W-C6, post hoc 2, written after post hoc 1 and committed before its own run.

Post hoc 1 read A1's constant residual as a different constant in the statement. Reading main's FINDINGS of B1919
afterwards showed that main's F_u is the same sum as this seat's (u1 multiplies tau, the pole pi/(s - 1) removed) and
main's norm the same regularisation. So this seat looked again at its own F_u and found, by hand, a term left out:
in the Poisson form the first part carries sqrt(pi) Gamma(s - 1/2) / Gamma(s) = pi (1 + (s - 1) kappa + ...), with
kappa = psi(1/2) - psi(1) = -2 log 2, and it multiplies a pole, so the constant term gains pi kappa = -2 pi log 2.
That is the 4.355 of the sealed run.

EXPECTATIONS, written before the run:
  C1  The general-s Poisson form Z_u(tau, s) agrees with the direct lattice sum at s = 3 within 1e-9 at every point.
  C2  F_u from the general-s form, as [Z(1 + h) + Z(1 - h)] / 2 with h = 1e-4 (the pole cancels), agrees with the
      corrected closed form, F_corrected = F_sealed - 2 pi log 2, within 1e-6 at every point, and differs from the
      sealed F by more than 4 at every point.
  C3  With F_corrected, main's statement N = F_u + pi log y - 2 pi (gamma + log pi) holds within 1e-7 at every point of
      the sealed run, with N the sealed run's own norms.

    python3 -I -u wc6_posthoc_2.py
"""
import contextlib, io, runpy, pathlib
import numpy as np, mpmath as mp

mp.mp.dps = 30
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(str(pathlib.Path(__file__).with_name("wc6_checks.py")))
EG = float(mp.euler)


def Zp(u1, u2, tau, s):
    s = mp.mpf(s); y = mp.mpf(tau.imag); X = mp.mpf(tau.real)
    f = mp.mpf(u1) % 1
    first = mp.sqrt(mp.pi) * mp.gamma(s - 0.5) / mp.gamma(s) * y ** (1 - 2 * s) * (mp.zeta(2 * s - 1, f) + mp.zeta(2 * s - 1, 1 - f))
    rest = mp.mpf(0)
    for m in range(-60, 61):
        p = m + mp.mpf(u1); Y = abs(p) * y; x = p * X + u2
        for k in range(1, 31):
            rest += 2 * (k / Y) ** (s - 0.5) * mp.besselk(s - 0.5, 2 * mp.pi * k * Y) * 2 * mp.cos(2 * mp.pi * k * x)
    return y ** s * (first + mp.pi ** s / mp.gamma(s) * rest)


def Zdirect3(u1, u2, tau):
    m = np.arange(-400, 401)[:, None] + u1; n = np.arange(-400, 401)[None, :] + u2
    return float(np.sum(tau.imag ** 3 / np.abs(m * tau + n) ** 6))


c1 = c2 = c3 = True
for c, tau, n2, *_ in g["rows"]:
    u1, u2 = c[0] - 0.5, c[1] - 0.5
    d3 = float(Zp(u1, u2, tau, 3)) - Zdirect3(u1, u2, tau)
    h = mp.mpf("1e-4")
    Fnum = float((Zp(u1, u2, tau, 1 + h) + Zp(u1, u2, tau, 1 - h)) / 2)
    Fs = g["F"](u1, u2, tau); Fc = Fs - 2 * np.pi * np.log(2)
    res = n2 - (Fc + np.pi * np.log(tau.imag) - 2 * np.pi * (EG + np.log(np.pi)))
    print("c", c, "tau", tau, "C1 %.1e" % d3, "C2 Fnum-Fc %.1e Fnum-Fsealed %.3f" % (Fnum - Fc, Fnum - Fs), "C3 %.1e" % res, flush=True)
    c1 &= abs(d3) < 1e-9; c2 &= abs(Fnum - Fc) < 1e-6 and abs(Fnum - Fs) > 4; c3 &= abs(res) < 1e-7
print("C1 Poisson form = direct sum at s = 3:", c1)
print("C2 F from the general form = corrected closed form, and not the sealed one:", c2)
print("C3 main's statement holds with the corrected F_u:", c3)
