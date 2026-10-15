# c_r(tau) against -4 pi log|theta_r(0|tau)| - 2 pi ln(pi/2), main's route A (plumbing: c only, no kappa)
import sys, math, numpy as np
sys.path.insert(0, '.')
import routeA as B
W = complex(np.exp(2j*np.pi/3))
for tau in (W, 1j, 0.13+1.07j, 0.3+1.6j, 2.2j, 3.0j, 4.4j, 1.411+0.899j, -0.49+0.778j):
    th = B.thetas(np.array(0.0), tau)
    cf = np.array([-4*math.pi*math.log(abs(complex(th[r-1]))) - 2*math.pi*math.log(math.pi/2) for r in (2, 4, 3)])
    ca = np.array([B.cA(r, tau, 1e-5) for r in (2, 4, 3)])
    print(f"{tau:.3f}  route A {np.round(ca,6)}  closed form {np.round(cf,6)}  max diff {np.max(np.abs(ca-cf)):.1e}")
