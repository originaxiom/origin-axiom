"""C2 exploration (main, unsealed, labelled): the twisted channels per sector. With a flat hypercharge line each sector's
four unit pairings P_s (s = 1, i, j, k) are twisted Szego-type kernels with a simple pole at 0 and residues R_s forming a
null quaternion (B1653). Under the canonical end condition the defect is D_sector = sum_s c_s R_s^2, c_s the regularised
norm of K_s = P_s/R_s. Is D_sector != 0 at tau = omega on the record's lines?"""
import numpy as np, math
from numpy.polynomial.legendre import leggauss
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
NK = 30
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
    M = bil(x, y, u, t)                                               # shape (2, 2, ...)
    return {s: np.einsum('mn,mn...->...', EPS @ C, M) for s, C in UNITS.items()}
def twist_of(w, t): a = w.imag/t.imag; return (a, 2*(w.real - a*t.real))
def line_w(p1, p2, t): return p1*t - p2
def residues(x, y, t, rad=0.01, N=256):
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t)
    return {s: np.mean(P[s]*u) for s in UNITS}
def rmax(th, t):
    d = np.exp(1j*th); y1 = d.imag/t.imag; x1 = d.real - y1*t.real; return 0.5/np.maximum(abs(x1), abs(y1))
def cnorms(x, y, t, R, eps=1e-5, nth=64, ns=48):
    v = [0.5+0.5*t, -0.5+0.5*t, -0.5-0.5*t, 0.5-0.5*t]
    br = sorted(float(np.mod(np.angle(z), 2*np.pi)) for z in v); br += [br[0] + 2*np.pi]
    xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = {s: 0.0 for s in UNITS}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        hi = np.log(rmax(th, t)); lo = math.log(eps)
        s_ = 0.5*(hi-lo)[:, None]*xs[None, :] + 0.5*(hi+lo)[:, None]; w2 = 0.5*(hi-lo)[:, None]*ws[None, :]
        rr = np.exp(s_); z = rr*np.exp(1j*th)[:, None]
        P = pairs(x, y, z, t)
        for s in UNITS:
            if abs(R[s]) > 1e-12: tot[s] += np.sum(wt[:, None]*w2*np.abs(P[s]/R[s])**2*rr**2)
    return {s: (tot[s] - 2*np.pi*math.log(1/eps)) if abs(R[s]) > 1e-12 else None for s in UNITS}
OM = complex(np.exp(2j*np.pi/3))
lines = {"half(1/2,0)": line_w(0.5, 0, OM), "half(0,1/2)": line_w(0, 0.5, OM), "tors(1/3,1/3)": line_w(1/3, 1/3, OM),
         "higgs(1/9,1/9)": line_w(1/9, 1/9, OM), "higgs(1/9,4/9)": line_w(1/9, 4/9, OM), "higgs(2/9,5/9)": line_w(2/9, 5/9, OM),
         "untwisted": 0j}
for lname, w in lines.items():
    row = []
    for sec, (fl, fr) in SECTORS.items():
        x = twist_of(SIXY[fl]*w, OM); y = twist_of(SIXY[fr]*w, OM)
        R = residues(x, y, OM); n2 = sum(abs(R[s])**2 for s in R); null = abs(sum(R[s]**2 for s in R))/n2
        c = cnorms(x, y, OM, R)
        D = sum(c[s]*R[s]**2 for s in UNITS if c[s] is not None)
        row.append(f"{sec}: null {null:.1e} |D|/|R|^2 {abs(D)/n2:.4f}")
    print(f"{lname:16s}", " | ".join(row))
