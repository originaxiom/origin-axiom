"""The average over the modular surface of f = |D|/||rho||^2 = pi |theta_3|^4 |h(lambda)| / (|theta_2|^4+|theta_3|^4+|theta_4|^4),
lambda = theta_2^4/theta_3^4, h(l) = l log|l| + (1-l) log|1-l|: the integral over the standard fundamental domain against
dx dy / y^2, divided by its area pi/3. Gauss-Legendre in x and in t = 1/y on the strip above the arc (|x| <= 1/2,
sqrt(1-x^2) <= y), at three resolutions."""
import numpy as np
from numpy.polynomial.legendre import leggauss


def thetas(tau, N=12):
    q = np.exp(1j * np.pi * tau); n = np.arange(N)[:, None]; m = np.arange(1, N)[:, None]
    t2 = 2 * np.sum(q ** ((n + 0.5) ** 2), axis=0)
    t3 = 1 + 2 * np.sum(q ** (m ** 2), axis=0)
    t4 = 1 + 2 * np.sum((-1) ** m * q ** (m ** 2), axis=0)
    return t2, t3, t4


def f(tau):
    t2, t3, t4 = thetas(tau)
    lam = t2 ** 4 / t3 ** 4
    with np.errstate(divide="ignore", invalid="ignore"):
        a = np.where(np.abs(lam) > 0, lam * np.log(np.abs(lam)), 0.0)   # l log|l| -> 0 at the cusp
        b = np.where(np.abs(1 - lam) > 0, (1 - lam) * np.log(np.abs(1 - lam)), 0.0)
    h = a + b
    return np.pi * np.abs(t3 ** 4 * h) / (np.abs(t2) ** 4 + np.abs(t3) ** 4 + np.abs(t4) ** 4)


def average(nx, nt):
    xg, wx = leggauss(nx); tg, wt = leggauss(nt)
    tot = 0.0
    for xi, wxi in zip(xg, wx):
        x = 0.5 * xi; w1 = 0.5 * wxi                       # x in [-1/2, 1/2]
        tmax = 1 / np.sqrt(1 - x * x)                       # t = 1/y in (0, 1/sqrt(1-x^2)]
        t = 0.5 * tmax * (tg + 1); w2 = 0.5 * tmax * wt     # dx dy / y^2 = dx dt
        tot += w1 * np.sum(w2 * f(x + 1j / t))
    return tot / (np.pi / 3)


for nx, nt in ((64, 96), (96, 144), (128, 192)):
    print(f"nodes {nx} x {nt}: average of f = {average(nx, nt):.10f}")
