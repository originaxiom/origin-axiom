# plumbing (c only, no kappa): main's route A against the closed form, by mpmath's jtheta (an independent theta route)
import sys, math, numpy as np, mpmath as mp
sys.path.insert(0, '.')
import b1654_routeA as B
mp.mp.dps = 30
def closed(tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
    return np.array([float(-4 * mp.pi * mp.log(abs(mp.jtheta(r, 0, q))) - 2 * mp.pi * mp.log(mp.pi / 2)) for r in (2, 4, 3)])
for tau in (1j, 0.13 + 1.07j, -0.49 + 0.878j, 0.4 + 4.3j):
    ca = np.array([B.cA(r, tau, 1e-5) for r in (2, 4, 3)])
    print(tau, np.max(np.abs(ca - closed(tau))))
