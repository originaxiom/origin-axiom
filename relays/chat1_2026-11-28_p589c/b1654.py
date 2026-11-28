"""B1654 -- THE NORM OF THE BOUNDARY CLASS (sealed instrument; one run).

The parity Higgs's only massless mode is the boundary class at the puncture (the SM seat's C0, point 3). In channel r
(an even spin structure, r = 2, 3, 4) its bulk profile is the conjugate Szego kernel, S_r(z) = th_r(z) th_1'(0) /
(th_r(0) th_1(z)) ~ 1/z. Cut at a common end radius eps, its norm is ||S_r||^2 = 2 pi log(1/eps) + c_r(tau) + o(1).
Under the canonical end condition (equal canonically normalised amplitudes) the residue triplet becomes
u_r = sqrt(2 pi L + c_r) R_r, L = log(1/eps), and u.u = 2 pi L (R.R) + D = D, D(tau) = sum_r c_r R_r^2, since R.R = 0.

Route A: polar quadrature about 0 over the period parallelogram P, radial variable s = log r, cut at eps; numpy theta
series.  Route B: product Gauss-Legendre over P in (x, t), z = x + t tau, with 1/|z|^2 and 2 Re(s1 z/zbar) subtracted
and restored analytically; mpmath jtheta.  The two share no quadrature and no theta code.
Cells N0, N1, N2, N2b, N3-N6 as sealed in PREREGISTRATION.md.  Writes the_norm_of_the_boundary_class.json and _run.txt
beside this script, after every cell.
"""
import json, math, pathlib, sys, time
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

HERE = pathlib.Path(__file__).resolve().parent                            # outputs are written beside the script
OUT = {}
LOG = []
def _plain(o):
    if hasattr(o, "item") and getattr(o, "size", 1) == 1: return o.item()  # numpy scalars -> Python (np.bool_ -> bool)
    return str(o)
def dump():
    json.dump(OUT, open(HERE / "the_norm_of_the_boundary_class.json", "w"), indent=1, default=_plain)
    open(HERE / "the_norm_of_the_boundary_class_run.txt", "w").write("\n".join(LOG) + "\n")
def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)

# ---------------------------------------------------------------- route A: numpy theta series, polar quadrature
K = 24                                                                  # K = 40 overflows np.sin/np.cos above Im tau ~ 5.7
K = 40
def thetas(z, tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(0, K); m = np.arange(1, K)
    z = np.asarray(z, dtype=complex)[..., None]
    t1 = 2*np.sum((-1)**n * q**((n+.5)**2) * np.sin((2*n+1)*np.pi*z), -1)
    t2 = 2*np.sum(q**((n+.5)**2) * np.cos((2*n+1)*np.pi*z), -1)
    t3 = 1 + 2*np.sum(q**(m**2) * np.cos(2*m*np.pi*z), -1)
    t4 = 1 + 2*np.sum((-1)**m * q**(m**2) * np.cos(2*m*np.pi*z), -1)
    return t1, t2, t3, t4
def th1p(tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(0, K)
    return 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))           # = 2 pi eta^3
def S_A(r, z, tau, scale=1.0):
    t = thetas(z, tau); t0 = thetas(np.array(0.0), tau)
    return scale*t[r-1]*th1p(tau)/(t0[r-1]*t[0])
def rmax_np(th, tau):
    d = np.exp(1j*th); y1 = d.imag/tau.imag; x1 = d.real - y1*tau.real
    return 0.5/np.maximum(np.abs(x1), np.abs(y1))
def vertex_angles(tau):
    v = [0.5+0.5*tau, -0.5+0.5*tau, -0.5-0.5*tau, 0.5-0.5*tau]
    br = sorted(float(np.mod(np.angle(x), 2*np.pi)) for x in v); return br + [br[0] + 2*np.pi]
def cA(r, tau, eps, scale=1.0, nth=96, ns=64):
    """int_{P minus D_eps} |scale*S_r|^2 dA - 2 pi log(1/eps), polar about 0, s = log r, Gauss-Legendre per segment."""
    br = vertex_angles(tau); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = 0.0
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        s_hi = np.log(rmax_np(th, tau)); s_lo = math.log(eps)
        s = 0.5*(s_hi - s_lo)[:, None]*xs[None, :] + 0.5*(s_hi + s_lo)[:, None]
        wsr = 0.5*(s_hi - s_lo)[:, None]*ws[None, :]
        rr = np.exp(s); z = rr*np.exp(1j*th)[:, None]
        tot += np.sum(wt[:, None]*wsr*np.abs(S_A(r, z, tau, scale))**2*rr**2)
    return float(tot - 2*np.pi*math.log(1/eps))
def R_A(tau):
    t0 = thetas(np.array(0.0), tau); d = th1p(tau)
    return {2: -t0[1]**2/d, 4: -t0[3]**2/d, 3: 1j*t0[2]**2/d}         # R_i (th2), R_j (th4), R_k (th3): B1644
def D_of(c, R): return sum(c[r]*R[r]**2 for r in (2, 3, 4))
def nR2(R): return sum(abs(R[r])**2 for r in (2, 3, 4))

