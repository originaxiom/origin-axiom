# c~ only (no forms, no kappa): Q(a') functions copied verbatim from lift_cells.py, checked against main's route A
import sys, math, time, numpy as np, mpmath as mp
sys.path.insert(0, sys.argv[1]); import b1654_routeA as BA
mp.mp.dps = 40
def ctil_direct(tau):
    return np.array([BA.cA(r, tau, 1e-5) - math.pi * math.log(tau.imag) for r in (2, 4, 3)])
def ctil_closed(tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
    return np.array([float(-4 * mp.pi * mp.log(abs(mp.jtheta(r, 0, q))) - 2 * mp.pi * mp.log(mp.pi / 2)
                           - mp.pi * mp.log(tau.imag)) for r in (2, 4, 3)])
t0 = time.time()
for tau in (1j, 0.5 + 0.8660254037844386j, -0.37 + 0.95j, 0.21 + 2.3j, -0.5 + 4.39j, 0.05 + 4.4j):
    d, c = ctil_direct(tau), ctil_closed(tau)
    print(tau, "direct", np.round(d, 6), "closed-direct", np.max(np.abs(d - c)))
# covariance of the closed form in the (2,4,3) order: T fixes idx0, swaps 1,2; S swaps 0,1, fixes 2
for tau in (0.13 + 1.07j, -0.41 + 0.93j):
    c = ctil_closed(tau); cT = ctil_closed(tau + 1); cS = ctil_closed(-1 / tau)
    print("T", np.max(np.abs(cT - c[[0, 2, 1]])), " S", np.max(np.abs(cS - c[[1, 0, 2]])))
# R_A (B1654's R) transforms by a monomial matrix with the same permutation
def Rv(t): R = BA.R_A(t); return np.array([R[2], R[4], R[3]])
for tau in (0.13 + 1.07j,):
    r, rT, rS = Rv(tau), Rv(tau + 1), Rv(-1 / tau)
    print("R(tau+1)/R(tau)[0,2,1]", rT / r[[0, 2, 1]], " R(-1/tau)/R(tau)[1,0,2]", rS / r[[1, 0, 2]])
print("s", round(time.time() - t0, 1))
