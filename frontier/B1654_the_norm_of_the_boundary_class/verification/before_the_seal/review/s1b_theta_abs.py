import sys; sys.path.insert(0,'.')
import numpy as np, mpmath as mp, pre
ns = pre.load(); thetas = ns['thetas']
mp.mp.dps = 40
worst = 0; where=None
for tau in (0.13+1.07j, -0.4+0.95j, 0.5+0.9j, 2.9j, 4.9j):
    q = mp.exp(1j*mp.pi*mp.mpc(tau))
    for z in (0.3+0.1j, 0.5+0.5*tau, -0.5-0.5*tau, 0.5-0.5*tau, 0.25*tau, 0.01+0.002j, 0.5*tau.imag*1j*0.99):
        z = complex(z)
        t = thetas(np.array(z), tau)
        for r in (1,2,3,4):
            ref = complex(mp.jtheta(r, mp.pi*mp.mpc(z), q))
            # scale: largest term of the series
            sc = max(1.0, abs(np.exp(np.pi*abs(z.imag)))*abs(np.exp(1j*np.pi*tau)))**0
            err = abs(ref - t[r-1])
            if err > worst: worst, where = err, (tau, z, r, ref, t[r-1])
print("worst abs err theta series vs jtheta:", worst, where)
