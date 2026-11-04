"""S303 check c6 (value-free; first principles, independent of every seat's code): Theorem 73 / the web seat's 'density Higgs'.
P(u) = e^{2 pi i a u} K(u; z), K = th1'(0) th1(u+z) / (th1(u) th1(z)), z = a tau - b: a meromorphic pairing with multipliers
(e^{2 pi i a}, e^{2 pi i b}) and residue 1 at u = 0.  Modes e_k(u) = exp(2 pi i (P_k xi + R_k eta)), u = xi + eta tau,
P_k = a + m, R_k = b + n, kappa_k = R_k - P_k tau.  Claim: int_cell P conj(e_k) dA = -Im tau / kappa_k (dA = dx dy).
Quadrature: polar about u = 0 over the centred cell (the r in r dr dtheta cancels the pole), Gauss-Legendre per corner
sector.  Second: the pairing's own norm int_{|u| > eps} |P|^2 dA grows like 2 pi ln(1/eps) (a normalisation needs a cut)."""
import cmath, math
import numpy as np
from numpy.polynomial.legendre import leggauss


def th1(u, tau, N=30):
    q = np.exp(1j * np.pi * tau); n = np.arange(N)
    u = np.asarray(u, dtype=complex)[..., None]
    return 2 * np.sum(((-1.0) ** n) * q ** ((n + 0.5) ** 2) * np.sin((2 * n + 1) * np.pi * u), axis=-1)


def th1p0(tau, N=30):
    q = np.exp(1j * np.pi * tau); n = np.arange(N)
    return 2 * np.pi * np.sum(((-1.0) ** n) * (2 * n + 1) * q ** ((n + 0.5) ** 2))


def Pfun(u, a, b, tau):
    z = a * tau - b
    return np.exp(2j * np.pi * a * u) * th1p0(tau) * th1(u + z, tau) / (th1(u, tau) * th1(z, tau))


def coords(u, tau):
    y = u.imag / tau.imag; x = u.real - y * tau.real; return x, y


def integrate(fun, tau, n_t=96, n_r=96, eps=0.0):
    corners = [0.5 + 0.5 * tau, -0.5 + 0.5 * tau, -0.5 - 0.5 * tau, 0.5 - 0.5 * tau]
    ang = sorted(float(np.mod(np.angle(c), 2 * np.pi)) for c in corners); ang.append(ang[0] + 2 * np.pi)
    xt, wt = leggauss(n_t); xr, wr = leggauss(n_r); acc = 0j
    for t0, t1 in zip(ang[:-1], ang[1:]):
        th = 0.5 * (t1 - t0) * xt + 0.5 * (t1 + t0); wth = 0.5 * (t1 - t0) * wt
        d = np.exp(1j * th); x, y = coords(d, tau); rmax = 0.5 / np.maximum(np.abs(x), np.abs(y))
        r = eps + 0.5 * (rmax - eps)[:, None] * (xr[None, :] + 1); wrr = 0.5 * (rmax - eps)[:, None] * wr[None, :]
        u = r * d[:, None]
        acc += np.sum(wth[:, None] * wrr * fun(u) * r)
    return acc


# quasi-periodicity and residue sanity
tau = 0.3 + 1.1j
for a, b in ((0.2, 0.35), (0.4, 0.1), (0.0, 0.25)):
    u0 = np.array([0.13 + 0.21j, -0.31 + 0.05j])
    m1 = Pfun(u0 + 1, a, b, tau) / Pfun(u0, a, b, tau); m2 = Pfun(u0 + tau, a, b, tau) / Pfun(u0, a, b, tau)
    res = 1e-6 * Pfun(np.array([1e-6]), a, b, tau)[0]
    print("(a,b)=(%.2f,%.2f): multiplier errors %.1e %.1e, residue error %.1e" % (
        a, b, np.abs(m1 - np.exp(2j * np.pi * a)).max(), np.abs(m2 - np.exp(2j * np.pi * b)).max(), abs(res - 1)))

worst = 0.0
for tau in (0.3 + 1.1j, 0.1 + 0.9j, 0.45 + 1.7j):
    for a, b in ((0.2, 0.35), (0.4, 0.1), (0.0, 0.25), (0.7, 0.6)):
        for m, n in ((0, 0), (-1, 0), (0, -1), (1, 1)):
            Pk, Rk = a + m, b + n; kap = Rk - Pk * tau
            if abs(kap) < 1e-9: continue
            def f(u):
                x, y = coords(u, tau)
                return Pfun(u, a, b, tau) * np.exp(-2j * np.pi * (Pk * x + Rk * y))
            val = integrate(f, tau)
            worst = max(worst, abs(val / (-tau.imag / kap) - 1))
print("int P conj(e_k) dA = -Im tau / kappa_k: worst relative error %.1e over 3 tau x 4 twists x 4 modes" % worst)

tau = 0.3 + 1.1j; a, b = 0.2, 0.35
vals = [integrate(lambda u: np.abs(Pfun(u, a, b, tau)) ** 2 / np.maximum(np.abs(u), 1e-300) * np.abs(u), tau, n_t=96, n_r=200, eps=e)
        for e in (1e-2, 1e-3, 1e-4)]
print("int_{|u|>eps} |P|^2 dA: increments per decade of eps %.4f, %.4f ; 2 pi ln 10 = %.4f (log divergence: the norm needs a cut)" % (
    (vals[1] - vals[0]).real, (vals[2] - vals[1]).real, 2 * np.pi * math.log(10)))
