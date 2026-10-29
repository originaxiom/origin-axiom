"""The channel norms c_r(tau) of B1654 (the regularised norm of the Szego kernel S_r = th_r(z) th1'(0)/(th_r(0) th1(z))
over the period parallelogram P = {x + t tau : |x|, |t| <= 1/2}), by this referee's own route:
   c_r = int_0^{2pi} dth [ log rho(th) + int_{-inf}^{log rho(th)} (|z S_r(z)|^2 - 1) ds ],   z = e^{s + i th},
(the eps -> 0 limit taken analytically; no cutoff), own theta sums in numpy (nome q = e^{i pi tau}).
Validated against B1654's banked values: i: c2 = c4 = -1.70156, c3 = -3.87915; omega: all -2.94582;
D(i)/|R|^2 = 1.0888, D(omega) = 0.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

KT = 30


def th_all(z, tau):
    q = np.exp(1j * np.pi * tau); n = np.arange(0, KT); m = np.arange(1, KT)
    z = np.asarray(z, dtype=complex)[..., None]
    t1 = 2 * np.sum((-1.0) ** n * q ** ((n + .5) ** 2) * np.sin((2 * n + 1) * np.pi * z), -1)
    t2 = 2 * np.sum(q ** ((n + .5) ** 2) * np.cos((2 * n + 1) * np.pi * z), -1)
    t3 = 1 + 2 * np.sum(q ** (m ** 2) * np.cos(2 * m * np.pi * z), -1)
    t4 = 1 + 2 * np.sum((-1.0) ** m * q ** (m ** 2) * np.cos(2 * m * np.pi * z), -1)
    return t1, t2, t3, t4


def th1p(tau):
    q = np.exp(1j * np.pi * tau); n = np.arange(0, KT)
    return 2 * np.pi * np.sum((-1.0) ** n * (2 * n + 1) * q ** ((n + .5) ** 2))


def rho(th, tau):
    d = np.exp(1j * th); y1 = d.imag / tau.imag; x1 = d.real - y1 * tau.real
    return 0.5 / np.maximum(np.abs(x1), np.abs(y1))


def vangles(tau):
    v = [0.5 + 0.5 * tau, -0.5 + 0.5 * tau, -0.5 - 0.5 * tau, 0.5 - 0.5 * tau]
    br = sorted(float(np.mod(np.angle(x), 2 * np.pi)) for x in v); return br + [br[0] + 2 * np.pi]


def c_all(tau, nth=120, ns=120, smin=-20.0):
    """returns {2: c2, 3: c3, 4: c4}"""
    tau = complex(tau); br = vangles(tau); xg, wg = leggauss(nth); xs, ws = leggauss(ns)
    t0 = th_all(np.array(0.0), tau); tp = th1p(tau); tot = {2: 0.0, 3: 0.0, 4: 0.0}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5 * (b - a) * xg + 0.5 * (b + a); wt = 0.5 * (b - a) * wg
        hi = np.log(rho(th, tau))
        s = 0.5 * (hi - smin)[:, None] * xs[None, :] + 0.5 * (hi + smin)[:, None]; w2 = 0.5 * (hi - smin)[:, None] * ws[None, :]
        z = np.exp(s + 1j * th[:, None]); T = th_all(z, tau)
        for r in (2, 3, 4):
            S = T[r - 1] * tp / (t0[r - 1] * T[0])
            tot[r] += np.sum(wt[:, None] * w2 * (np.abs(z * S) ** 2 - 1)) + np.sum(wt * hi)
    return tot


def R_vec(tau):
    """(R2, R4, R3) in B1654/B1691's ordering (th2, th4, th3); B1654's R_A normalisation (divided by th1'(0))"""
    t0 = th_all(np.array(0.0), complex(tau)); d = th1p(complex(tau))
    return np.array([-t0[1] ** 2 / d, -t0[3] ** 2 / d, 1j * t0[2] ** 2 / d])


def c_vec(tau):
    c = c_all(tau); return np.array([c[2], c[4], c[3]])


if __name__ == "__main__":
    W = complex(np.exp(2j * np.pi / 3))
    for name, t in (("i", 1j), ("omega", W), ("t1", 0.13 + 1.07j)):
        c = c_vec(t); R = R_vec(t); D = np.sum(c * R ** 2)
        print(name, "c (2,4,3) =", np.round(c, 6), " D/|R|^2 =", np.round(D / np.sum(abs(R) ** 2), 6))
    # convergence in the quadrature
    for nn in (80, 160):
        c = c_all(1j, nth=nn, ns=nn); print("nth=ns=%d" % nn, {k: round(v, 12) for k, v in c.items()})
