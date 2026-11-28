"""B1656's own functions and constants (main's code), copied verbatim up to its first cell, for P-169's exploration."""
import json, math, pathlib, sys, time
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

HERE = pathlib.Path(__file__).resolve().parent
OUT = {}; LOG = []
def _plain(o):
    if hasattr(o, "item") and getattr(o, "size", 1) == 1: return o.item()
    return str(o)
def dump():
    json.dump(OUT, open(HERE / "the_electrons_zero.json", "w"), indent=1, default=_plain)
    open(HERE / "the_electrons_zero_run.txt", "w").write("\n".join(LOG) + "\n")
def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)

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

# ---------------------------------------------------------------- route B (mpmath, B1653's bilinear), strip quadrature
mp.mp.dps = 20; I = mp.mpc(0, 1)
def th_mp(n, u, t):
    q = mp.exp(I*mp.pi*t); x = mp.pi*u
    if n == 3: return mp.jtheta(3, x, q)
    if n == 4: return mp.jtheta(4, x, q)
    q4 = mp.exp(I*mp.pi*t/4); s = x + mp.pi*t/2
    if n == 2: return q4*mp.exp(I*x)*mp.jtheta(3, s, q)
    return -I*q4*mp.exp(I*x)*mp.jtheta(4, s, q)
def thc_mp(a, b, u, T): return mp.exp(I*mp.pi*a*a*T + 2*I*mp.pi*a*(u + b))*th_mp(3, u + a*T + b, T)
def bil_mp(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2*t; t1 = th_mp(1, u, t)
    den = I*mp.exp(-I*mp.pi*t/2)*mp.exp(-I*mp.pi*u)*t1
    X0, X1, Y0, Y1 = thc_mp(ax, bx, u, T), thc_mp(ax, bx, u + t, T), thc_mp(ay, by, u, T), thc_mp(ay, by, u + t, T)
    return [[X0*Y0/t1, mp.exp(I*mp.pi*by)*X0*Y1/den], [mp.exp(I*mp.pi*bx)*X1*Y0/den, mp.exp(I*mp.pi*(bx + by))*X1*Y1/th_mp(1, u + t, t)]]
EC = {s: (EPS @ C) for s, C in UNITS.items()}
def pair_mp(M, s): return sum(complex(EC[s][m, n])*M[m][n] for m in range(2) for n in range(2))
def coeffs_mp(x, y, t, s, R, rho=mp.mpf("0.02"), N=64):
    """K_s = P_s/R_s = 1/z + a0 + a1 z + ...: a0, a1 from circle averages"""
    vals = []
    for k in range(N):
        z = rho*mp.expjpi(2*mp.mpf(k)/N); vals.append((z, pair_mp(bil_mp(x, y, z, t), s)/R))
    a0 = mp.fsum(v - 1/z for z, v in vals)/N
    a1 = mp.fsum((v - 1/z - a0)/z for z, v in vals)/N
    return a0, a1
def rmax_mp(th, t):
    d = mp.expj(th); y1 = mp.im(d)/mp.im(t); x1 = mp.re(d) - y1*mp.re(t); return mp.mpf(1)/2/max(abs(x1), abs(y1))
def cB(x, y, t, s, R, n=32):
    t = mp.mpc(t); x = (mp.mpf(x[0]), mp.mpf(x[1])); y = (mp.mpf(y[0]), mp.mpf(y[1])); R = mp.mpc(R)
    a0, a1 = coeffs_mp(x, y, t, s, R)
    xg, wg = leggauss(n); xg = [mp.mpf(float(v)) for v in xg]; wg = [mp.mpf(float(v)) for v in wg]; tot = mp.mpf(0)
    for xa, xb in [(-0.5, 0.0), (0.0, 0.5)]:
        for ta, tb in [(-0.5, 0.0), (0.0, 0.5)]:
            for xi, wi in zip(xg, wg):
                xx = (xb-xa)/2*xi + (xb+xa)/2
                for tj, wj in zip(xg, wg):
                    tt = (tb-ta)/2*tj + (tb+ta)/2; z = xx + tt*t
                    K = pair_mp(bil_mp(x, y, z, t), s)/R
                    f = abs(K)**2 - 1/abs(z)**2 - 2*mp.re(a0/mp.conj(z)) - 2*mp.re(a1*z/mp.conj(z))
                    tot += wi*wj*(xb-xa)/2*(tb-ta)/2*f
    tot *= mp.im(t)
    v = [sx*mp.mpf(1)/2 + sy*t/2 for sx in (1, -1) for sy in (1, -1)]
    br = sorted(mp.arg(z) % (2*mp.pi) for z in v); br.append(br[0] + 2*mp.pi)
    I_log = mp.fsum(mp.quad(lambda th: mp.log(rmax_mp(th, t)), [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_1 = mp.fsum(mp.quad(lambda th: mp.expj(th)*rmax_mp(th, t), [a, b]) for a, b in zip(br[:-1], br[1:]))      # int 1/zbar dA
    I_2 = mp.fsum(mp.quad(lambda th: mp.expj(2*th)*rmax_mp(th, t)**2/2, [a, b]) for a, b in zip(br[:-1], br[1:]))  # int z/zbar dA
    return float(tot + 2*mp.re(a0*I_1) + 2*mp.re(a1*I_2) + I_log)

# ---------------------------------------------------------------- the coupling with channel weights (B1644, B1653)
def dual_basis():
    G = np.array([[np.sum(EC[t]*UNITS[s]) for s in UNITS] for t in UNITS])                 # pair(E_s := C_s, C_t)
    Gi = np.linalg.inv(G); keys = list(UNITS)
    return {keys[a]: sum(Gi[b, a]*UNITS[keys[b]] for b in range(4)) for a in range(4)}
EDUAL = dual_basis()
def weighted_M(u): return sum(u[s]*EDUAL[s] for s in UNITS)
def coupling(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])

T0 = time.time()
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]

