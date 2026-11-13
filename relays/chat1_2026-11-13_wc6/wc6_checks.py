#!/usr/bin/env python3
"""W-C6, part 2: B1919 and B1921 computed a second time on this seat's own code.

Data-free. numpy and mpmath only; nothing of main's arcs is read by this script. The points c and tau below are this
seat's own generic choices; none is a named point of the programme.

    python3 -I -u wc6_checks.py

DEFINITIONS (this seat's reading of M17; main's own definitions are read only after this file is committed):
  theta with characteristic c = (a, b):  th_c(u) = sum_n exp(pi i (n+a)^2 tau + 2 pi i (n+a)(u+b)).
  T(u) = th_(1/2,1/2)(u), which is theta_1 up to sign.  K_c(u) = T'(0) th_c(u) / (th_c(0) T(u)), so K_c = 1/u + c0 + O(u).
  |K_c|^2 is doubly periodic on C / (Z + tau Z). P is the parallelogram {s + t tau : |s|, |t| <= 1/2}, area y = Im tau.
  The regularised flat norm: N(c, tau) = lim_{eps -> 0} [ int_{P, |u| > eps} |K_c|^2 dx dy + 2 pi log eps ].
  It is computed in polar coordinates about u = 0: N = int_P (|K_c|^2 - 1/|u|^2) dA + int_0^{2 pi} log rmax(phi) dphi,
  where rmax(phi) is the distance from 0 to the edge of P in the direction phi. Gauss-Legendre in r and in phi, with
  the phi panels split at the four corners of P.
  u = c - (1/2, 1/2) = (u1, u2), placed as the point u1 tau + u2.
  The shifted sum: Z_u(tau, s) = sum_{(m, n) in Z^2} y^s / |(m + u1) tau + n + u2|^(2s), which has a simple pole
  pi / (s - 1) at s = 1. F_u(tau) = lim_{s -> 1} [ Z_u(tau, s) - pi / (s - 1) ], its Kronecker limit.
  F_u is computed by Poisson summation over n, for u1 not an integer:
    F_u = - pi log y - pi (psi(f) + psi(1 - f)) + sum_m (pi / |m + u1|) * 2 Re[ r_m / (1 - r_m) ],
    f = u1 mod 1, r_m = exp(-2 pi |m + u1| y + 2 pi i ((m + u1) Re tau + u2)).
  (This seat's own derivation: K_c is the section with multipliers exp(2 pi i (a - 1/2)) under u -> u + 1 and
  exp(-2 pi i (b - 1/2)) under u -> u + tau, and dbar K_c = pi delta, so its Fourier coefficients are
  1 / ((m + u1) tau + (n + u2)) up to sign, and its formal norm is Z_u(tau, 1).)

EXPECTATIONS, written before the run:
  A0  N is converged: the two resolutions (120 and 200 nodes per panel and direction) agree within 1e-9 at every point.
  A1  B1919 as M17 states it: at every point below, N(c, tau) - [F_u(tau) + pi log y - 2 pi (gamma + log pi)] is
      within 1e-7 of 0.
  A2  Control: with the components of u swapped (u2 tau + u1), the same residual is above 1e-3 at some point.
  A3  Control: with the term pi log y left out, the residual is above 1e-3 at some point.
  B1  B1921 as M17 states it: with c' = (b, -a), N(c', -1/tau) - N(c, tau) + 2 pi log|tau| is within 1e-7 of 0 at every
      point below, both sides computed by the integral.
  B2  Control: with c' = c, the same quantity is above 1e-3 at some point.
  If A1 fails, the script also prints the residuals and their least-squares fit to alpha + beta log y, so that a
  difference of convention (a constant, or a multiple of log y) can be told from a failure of the statement.
"""
import numpy as np
import mpmath as mp

CS = [(0.13, 0.71), (0.30, 0.20), (0.77, 0.41), (0.62, 0.09)]
TAUS = [complex(0.21, 1.13), complex(-0.35, 0.90), complex(0.10, 1.70)]
NT = 40  # terms each side in the theta series
EG = float(mp.euler)


def th(a, b, u, tau):
    n = np.arange(-NT, NT + 1)[:, None] + a
    return np.exp(1j * np.pi * n ** 2 * tau + 2j * np.pi * n * (u[None, :] + b)).sum(axis=0)


def dth0(a, b, tau):
    n = np.arange(-NT, NT + 1) + a
    return (2j * np.pi * n * np.exp(1j * np.pi * n ** 2 * tau + 2j * np.pi * n * b)).sum()


def K2(c, tau, u):
    a, b = c
    k = dth0(0.5, 0.5, tau) * th(a, b, u, tau) / (th(a, b, np.zeros(1), tau)[0] * th(0.5, 0.5, u, tau))
    return np.abs(k) ** 2


def rmax(phi, tau):
    y = tau.imag
    beta = np.sin(phi) / y
    alpha = np.cos(phi) - beta * tau.real
    return 0.5 / np.maximum(np.abs(alpha), np.abs(beta))


def corners(tau):
    out = []
    for s, t in ((0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)):
        w = s + t * tau
        out.append(np.angle(w) % (2 * np.pi))
    return sorted(out)


def norm(c, tau, nodes):
    x, wx = np.polynomial.legendre.leggauss(nodes)
    cs = corners(tau)
    edges = cs + [cs[0] + 2 * np.pi]
    total, logpart = 0.0, 0.0
    for p0, p1 in zip(edges[:-1], edges[1:]):
        phi = 0.5 * (p1 - p0) * x + 0.5 * (p1 + p0)
        wphi = 0.5 * (p1 - p0) * wx
        R = rmax(phi, tau)
        logpart += np.sum(wphi * np.log(R))
        for ph, wp, Rm in zip(phi, wphi, R):
            r = 0.5 * Rm * (x + 1)
            wr = 0.5 * Rm * wx
            u = r * np.exp(1j * ph)
            f = (K2(c, tau, u) * r ** 2 - 1.0) / r  # (|K|^2 - 1/r^2) * r
            total += wp * np.sum(wr * f)
    return total + logpart


def F(u1, u2, tau):
    y = tau.real * 0 + tau.imag
    f = u1 % 1.0
    val = -mp.pi * mp.log(y) - mp.pi * (mp.digamma(f) + mp.digamma(1 - f))
    s = 0.0
    for m in range(-200, 201):
        p = m + u1
        r = np.exp(-2 * np.pi * abs(p) * y + 2j * np.pi * (p * tau.real + u2))
        s += (np.pi / abs(p)) * 2 * (r / (1 - r)).real
    return float(val) + s


def say(*a):
    print(*a, flush=True)


rows = []
for c in CS:
    for tau in TAUS:
        n1, n2 = norm(c, tau, 120), norm(c, tau, 200)
        u1, u2 = c[0] - 0.5, c[1] - 0.5
        y = tau.imag
        claim = F(u1, u2, tau) + np.pi * np.log(y) - 2 * np.pi * (EG + np.log(np.pi))
        swapped = F(u2, u1, tau) + np.pi * np.log(y) - 2 * np.pi * (EG + np.log(np.pi))
        nolog = F(u1, u2, tau) - 2 * np.pi * (EG + np.log(np.pi))
        rows.append((c, tau, n2, n2 - n1, n2 - claim, n2 - swapped, n2 - nolog))
        say("A  c", c, "tau", tau, "N %.12f" % n2, "resolution diff %.1e" % (n2 - n1),
            "residual %.2e" % (n2 - claim), "swapped %.2e" % (n2 - swapped), "no log %.2e" % (n2 - nolog))
say("A0 converged within 1e-9 at all points:", all(abs(r[3]) < 1e-9 for r in rows))
a1 = all(abs(r[4]) < 1e-7 for r in rows)
say("A1 B1919 holds within 1e-7 at all points:", a1, "; largest residual %.2e" % max(abs(r[4]) for r in rows))
say("A2 control, u swapped, above 1e-3 at some point:", any(abs(r[5]) > 1e-3 for r in rows))
say("A3 control, no pi log y, above 1e-3 at some point:", any(abs(r[6]) > 1e-3 for r in rows))
if not a1:
    ly = np.array([np.log(r[1].imag) for r in rows])
    res = np.array([r[4] for r in rows])
    coef, *_ = np.linalg.lstsq(np.vstack([np.ones_like(ly), ly]).T, res, rcond=None)
    say("A1 fit of the residuals to alpha + beta log y: alpha %.6f beta %.6f ; largest misfit %.2e"
        % (coef[0], coef[1], np.max(np.abs(res - coef[0] - coef[1] * ly))))

brows = []
for c in CS:
    for tau in TAUS:
        a, b = c
        cp = (b % 1.0, (-a) % 1.0)
        tp = -1 / tau
        lhs = norm(cp, tp, 200)
        base = [r[2] for r in rows if r[0] == c and r[1] == tau][0]
        q = lhs - base + 2 * np.pi * np.log(abs(tau))
        ctrl = norm(c, tp, 200) - base + 2 * np.pi * np.log(abs(tau))
        brows.append((q, ctrl))
        say("B  c", c, "tau", tau, "quantity %.2e" % q, "control c'=c %.2e" % ctrl)
say("B1 B1921 holds within 1e-7 at all points:", all(abs(q) < 1e-7 for q, _ in brows),
    "; largest %.2e" % max(abs(q) for q, _ in brows))
say("B2 control, c' = c, above 1e-3 at some point:", any(abs(cq) > 1e-3 for _, cq in brows))
