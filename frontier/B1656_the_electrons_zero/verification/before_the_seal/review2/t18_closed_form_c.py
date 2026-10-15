# Review 2: an INDEPENDENT evaluation of the regularised norms c_s from the closed-form twisted Szego kernel
#   K_s(z) = exp(2 pi i A z) th_s(z + ubar) th1'(0) / ( th_s(ubar) th1(z) ),  A = Im(ubar)/Im(tau),   (th1<->1, th2<->i, th4<->j, th3<->k)
# using a Cartesian product Gauss rule on the 4 sub-rectangles with the same kind of singular subtraction, but with closed-form thetas (no 'pairs'/'bil').
# It is NOT one of the sealed cells (a different line sector is used for the comparison: ubar = 3 w for w=(2/9,5/9) at omega).
import numpy as np, math, sys
from numpy.polynomial.legendre import leggauss
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","rmax_np","vangles","np"): globals()[k] = ns[k]
NK = 30
m = np.arange(-NK, NK + 1)
def th(n, z, t):
    z = np.asarray(z, dtype=complex)[..., None]
    if n == 1: return -1j*np.sum((-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z), -1)
    if n == 2: return np.sum(np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z), -1)
    if n == 3: return np.sum(np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z), -1)
    return np.sum((-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z), -1)
def dth1_0(t): return complex(np.sum(-1j*(-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2)*1j*np.pi*(2*m+1)))
THOF = {"1": 1, "i": 2, "j": 4, "k": 3}
def K(s, z, ub, t):
    A = ub.imag/t.imag
    return np.exp(2j*np.pi*A*z)*th(THOF[s], z + ub, t)*dth1_0(t)/(th(THOF[s], ub, t)*th(1, z, t))
def c_closed(s, ub, t, n=48):
    # laurent a0, a1 by circle means of the closed form
    u = 0.05*np.exp(2j*np.pi*np.arange(128)/128); Ku = K(s, u, ub, t)
    a0 = np.mean(Ku - 1/u); a1 = np.mean((Ku - 1/u - a0)/u)
    xg, wg = leggauss(n); tot = 0.0
    for xa, xb in [(-0.5, 0.0), (0.0, 0.5)]:
        for ta, tb in [(-0.5, 0.0), (0.0, 0.5)]:
            xx = (xb-xa)/2*xg + (xb+xa)/2; tt = (tb-ta)/2*xg + (tb+ta)/2
            XX, TT = np.meshgrid(xx, tt, indexing="ij"); z = XX + TT*t
            f = np.abs(K(s, z, ub, t))**2 - 1/np.abs(z)**2 - 2*np.real(a0/np.conj(z)) - 2*np.real(a1*z/np.conj(z))
            tot += np.sum(np.outer(wg, wg)*(xb-xa)/2*(tb-ta)/2*f)
    tot *= t.imag
    from scipy.integrate import quad
    br = vangles(t); I_log = I_1 = I_2 = 0.0
    for a, b in zip(br[:-1], br[1:]):
        I_log += quad(lambda th_: math.log(rmax_np(th_, t)), a, b, epsabs=1e-14, epsrel=1e-14)[0]
        I_1 += quad(lambda th_: math.cos(th_)*rmax_np(th_, t), a, b, epsabs=1e-14, epsrel=1e-14)[0] + 1j*quad(lambda th_: math.sin(th_)*rmax_np(th_, t), a, b, epsabs=1e-14, epsrel=1e-14)[0]
        I_2 += quad(lambda th_: math.cos(2*th_)*rmax_np(th_, t)**2/2, a, b, epsabs=1e-14, epsrel=1e-14)[0] + 1j*quad(lambda th_: math.sin(2*th_)*rmax_np(th_, t)**2/2, a, b, epsabs=1e-14, epsrel=1e-14)[0]
    return float(tot + 2*np.real(a0*I_1) + 2*np.real(a1*I_2) + I_log)
for (p1, p2), t, tn, sec in [((2/9, 5/9), OM, "omega", "down"), ((2/9, 5/9), OM, "omega", "up"), ((0.137, 0.291), GEN, "generic", "down"), ((0.613, 0.287), -0.17+0.95j, "T2", "up")]:
    w = line_w(p1, p2, t); fl, fr = SECTORS[sec]; ub = (SIXY[fl] + SIXY[fr])*w
    x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t); cA_ = cA(x, y, t, R)
    out = []
    for s in UNITS:
        cc = c_closed(s, ub, t); out.append("%s: closed %.9f  routeA %.9f  diff %.1e" % (s, cc, cA_[s], abs(cc - cA_[s])))
    print((round(9*p1, 2), round(9*p2, 2)), tn, sec, " | ".join(out))
