# numpy replica of the instrument's cB (same algorithm: 4 sub-rectangles, product Gauss-Legendre in (x,t), subtraction of
# 1/|z|^2, 2Re(a0/zbar), 2Re(a1 z/zbar), analytic restoration) -- for convergence studies at larger n.
import numpy as np, math
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
def laurent(P_s, R_s, rho=0.05, N=128):
    u = rho*np.exp(2j*np.pi*np.arange(N)/N)
    return u
def cB_np(pairs, rmax_np, vangles, x, y, t, s, R, n=32, rho=0.05, N=128, subtract_a1=True, subtract_a0=True):
    u = rho*np.exp(2j*np.pi*np.arange(N)/N); K = pairs(x, y, u, t)[s]/R
    a0 = np.mean(K - 1/u) if subtract_a0 else 0.0
    a1 = np.mean((K - 1/u - (np.mean(K - 1/u)))/u) if subtract_a1 else 0.0
    xg, wg = leggauss(n); tot = 0.0
    for xa, xb in [(-0.5, 0.0), (0.0, 0.5)]:
        for ta, tb in [(-0.5, 0.0), (0.0, 0.5)]:
            xx = (xb-xa)/2*xg + (xb+xa)/2; tt = (tb-ta)/2*xg + (tb+ta)/2
            XX, TT = np.meshgrid(xx, tt, indexing="ij"); z = XX + TT*t
            Kz = pairs(x, y, z, t)[s]/R
            f = np.abs(Kz)**2 - 1/np.abs(z)**2 - 2*np.real(a0/np.conj(z)) - 2*np.real(a1*z/np.conj(z))
            W = np.outer(wg, wg)*(xb-xa)/2*(tb-ta)/2
            tot += np.sum(W*f)
    tot *= t.imag
    br = vangles(t)
    I_log = I_1 = I_2 = 0.0
    for a, b in zip(br[:-1], br[1:]):
        I_log += quad(lambda th: math.log(rmax_np(th, t)), a, b, epsabs=1e-14, epsrel=1e-14)[0]
        I_1 += quad(lambda th: math.cos(th)*rmax_np(th, t), a, b, epsabs=1e-14, epsrel=1e-14)[0] + 1j*quad(lambda th: math.sin(th)*rmax_np(th, t), a, b, epsabs=1e-14, epsrel=1e-14)[0]
        I_2 += quad(lambda th: math.cos(2*th)*rmax_np(th, t)**2/2, a, b, epsabs=1e-14, epsrel=1e-14)[0] + 1j*quad(lambda th: math.sin(2*th)*rmax_np(th, t)**2/2, a, b, epsabs=1e-14, epsrel=1e-14)[0]
    return float(tot + 2*np.real(a0*I_1) + 2*np.real(a1*I_2) + I_log), (a0, a1)
