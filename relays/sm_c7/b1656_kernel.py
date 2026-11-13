"""B1656's kernel and its regularised norm: the imports (lines 16-20) and lines 33-83 of
frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py on main at f503b1f38, copied unchanged below the
marker (only definitions: the kernel and its norm; no measured value). Used by SM-C7 steps 3 and 4, as M19 allows."""
# ---- copied from main below this line ----
import json, math, pathlib, sys, time
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
BLOCKS = [QJ, QI, QK]                                                        # the generations' blocks (B1644)
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
OM = complex(np.exp(2j*np.pi/3)); GEN = 0.13 + 1.07j

# ---------------------------------------------------------------- route A (numpy)
NK = 24
def thc(a, b, u, T):
    n = np.arange(-NK, NK + 1) + a; u = np.asarray(u, dtype=complex)[..., None]
    return np.sum(np.exp(1j*np.pi*T*n*n + 2j*np.pi*n*(u + b)), -1)
def th1(u, t):
    k = np.arange(-NK, NK + 1); h = k + 0.5; u = np.asarray(u, dtype=complex)[..., None]
    return -1j*np.sum((-1.0)**k*np.exp(1j*np.pi*t*h*h + 1j*np.pi*(2*k + 1)*u), -1)
def bil(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2*t; t1 = th1(u, t)
    den = 1j*np.exp(-1j*np.pi*t/2)*np.exp(-1j*np.pi*u)*t1
    X0, X1, Y0, Y1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T), thc(ay, by, u, T), thc(ay, by, u + t, T)
    return np.array([[X0*Y0/t1, np.exp(1j*np.pi*by)*X0*Y1/den], [np.exp(1j*np.pi*bx)*X1*Y0/den, np.exp(1j*np.pi*(bx + by))*X1*Y1/th1(u + t, t)]])
def pairs(x, y, u, t):
    M = bil(x, y, u, t); return {s: np.einsum('mn,mn...->...', EPS @ C, M) for s, C in UNITS.items()}
def twist_of(w, t): a = w.imag/t.imag; return (a, 2*(w.real - a*t.real))
def line_w(p1, p2, t): return p1*t - p2                                      # W59's holonomy phases (B1653)
def sector_twists(w, t, ql, qr): return twist_of(ql*w, t), twist_of(qr*w, t)
def residues(x, y, t, rad=0.01, N=256):
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t); return {s: complex(np.mean(P[s]*u)) for s in UNITS}
def rmax_np(th, t):
    d = np.exp(1j*th); y1 = d.imag/t.imag; x1 = d.real - y1*t.real; return 0.5/np.maximum(abs(x1), abs(y1))
def vangles(t):
    v = [0.5+0.5*t, -0.5+0.5*t, -0.5-0.5*t, 0.5-0.5*t]
    br = sorted(float(np.mod(np.angle(z), 2*np.pi)) for z in v); return br + [br[0] + 2*np.pi]
def a0_of(x, y, t, R, rad=0.05, N=128):
    """K_s = P_s/R_s = 1/z + a0 + a1 z + ...: a0 = the circle mean of K_s - 1/z"""
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t)
    return {s: (complex(np.mean(P[s]/R[s] - 1/u)) if abs(R[s]) > 1e-12 else None) for s in UNITS}
def cA(x, y, t, R, eps=1e-5, scale=1.0, nth=96, ns=64):
    """the regularised norm: int_{P minus D_eps} |scale K_s|^2 - 2 pi log(1/eps) + scale^2 pi eps^2 |a0|^2 (the disc's
    constant term; the twisted kernels are not odd, so a0 != 0; the next term is O(eps^4))"""
    A0 = a0_of(x, y, t, R)
    br = vangles(t); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = {s: 0.0 for s in UNITS}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        hi = np.log(rmax_np(th, t)); lo = math.log(eps)
        sg = 0.5*(hi-lo)[:, None]*xs[None, :] + 0.5*(hi+lo)[:, None]; w2 = 0.5*(hi-lo)[:, None]*ws[None, :]
        rr = np.exp(sg); z = rr*np.exp(1j*th)[:, None]; P = pairs(x, y, z, t)
        for s in UNITS:
            if abs(R[s]) > 1e-12: tot[s] += np.sum(wt[:, None]*w2*np.abs(scale*P[s]/R[s])**2*rr**2)
    return {s: (float(tot[s] - 2*np.pi*math.log(1/eps) + scale**2*np.pi*eps**2*abs(A0[s])**2) if abs(R[s]) > 1e-12 else None) for s in UNITS}
def nR2(R): return sum(abs(R[s])**2 for s in UNITS)
def D_of(c, R): return sum(c[s]*R[s]**2 for s in UNITS if c[s] is not None)
