"""V2 (verifier). The Kronecker identification off the order-5 lines: random real lines, lines of order 7 and 12, a tau
with Re tau outside the strip, three fresh points u.  Main's bilinear (bil_mp, 20 digits) against
R_s * exp(2 pi i alpha u) theta1'(0) theta1(u+z)/(theta1(u) theta1(z)), z = (qL+qR) w - h_s, with R_s from main's numpy
contour residues (route A) -- so the closed form of R_s is NOT used here; R_s enters only as main's own contour mean.
Also: |R_s| = sqrt(det Box_chi det Box_delta)/(2 pi |eta|) on these frame lines, with the determinants computed by an
independent Mellin zeta (k4's routine copied, not imported)."""
import sys, math
import numpy as np, mpmath as mp
from numpy.polynomial.legendre import leggauss
from scipy.special import exp1
import pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
_a = sys.argv; sys.argv = ["x"]; import b1656_funcs as B; sys.argv = _a
mp.mp.dps = 20; I = mp.mpc(0, 1); H = mp.mpf(1)/2
th1 = lambda u, t: B.th_mp(1, u, t)
rng = np.random.default_rng(11)
TAUS = [mp.mpc("1.73", "1.21"), mp.mpc("0.05", "2.3")]
LINES = [(mp.mpf(1)/7, mp.mpf(3)/7), (mp.mpf(5)/12, mp.mpf(1)/12)] + [tuple(mp.mpf(float(v)) for v in rng.uniform(0, 1, 2)) for _ in range(2)]
US = [mp.mpc("0.17", "-0.23"), mp.mpc("-0.41", "0.08"), mp.mpc("0.29", "0.31")]
HS = {"1": 0, "i": H, "j": None, "k": None}
def eta_np(t):
    q = np.exp(2j*np.pi*t); n = np.arange(1, 400); return np.exp(1j*np.pi*t/12)*np.prod(1 - q**n)
def Theta(al, be, t, x):
    lam_max = math.sqrt(46/x); y = t.imag; M = int(lam_max/y) + 3; Nn = int(lam_max + abs(t.real)*M) + 3
    m = np.arange(-M, M + 1)[:, None] + al; n = np.arange(-Nn, Nn + 1)[None, :] - be
    return np.sum(np.exp(-x*np.abs(m*t - n)**2))
def logdet(al, be, t):
    al = al - math.floor(al + 0.5); be = be - math.floor(be + 0.5)      # det depends on (al, be) mod Z^2 only
    y = t.imag; xg, wg = leggauss(60); lo = 0.0
    for a, b in ((0.02, 0.1), (0.1, 0.3), (0.3, 1.0)):
        xs = 0.5*(b - a)*xg + 0.5*(b + a); lo += 0.5*(b - a)*sum(wi*(Theta(al, be, t, xi) - math.pi/(xi*y))/xi for xi, wi in zip(xs, wg))
    M = int(9/y) + 3; Nn = int(9 + abs(t.real)*M) + 3
    m = np.arange(-M, M + 1)[:, None] + al; n = np.arange(-Nn, Nn + 1)[None, :] - be
    return -(lo - math.pi/y + float(np.sum(exp1(np.abs(m*t - n)**2))))
wk = 0.0; wdet = 0.0; ncase = 0
for t in TAUS:
    T1P = mp.diff(lambda z: th1(z, t), 0); tc = complex(t)
    for p1, p2 in LINES:
        w = p1*t - p2
        for sec, (lf, rf) in B.SECTORS.items():
            qL, qR = B.SIXY[lf], B.SIXY[rf]; Q = qL + qR
            x = (qL*p1, -2*qL*p2); y = (qR*p1, -2*qR*p2)
            Rn = B.residues((float(x[0]), float(x[1])), (float(y[0]), float(y[1])), tc, rad=0.01, N=512)
            nR = math.sqrt(sum(abs(v)**2 for v in Rn.values()))
            hs = {"1": 0, "i": H, "j": t/2, "k": (1 + t)/2}
            for s in B.UNITS:
                if abs(Rn[s]) < 1e-10*nR: continue
                z = Q*w - hs[s]; k2 = mp.im(z)/mp.im(t); al = k2            # z = al tau + be
                be = mp.re(z) - al*mp.re(t)
                Kk = lambda u: mp.exp(2*I*mp.pi*al*u)*T1P*th1(u + z, t)/(th1(u, t)*th1(z, t))
                for u in US:
                    P = B.pair_mp(B.bil_mp(x, y, u, t), s)
                    wk = max(wk, abs(P/(mp.mpc(Rn[s])*Kk(u)) - 1))
                # determinants: chi = Higgs-line characteristic minus (1/2,1/2) = (al, be); delta from the relative line
                ap, am = x[0] + y[0], x[0] - y[0]; bm = (x[1] - y[1])/2
                dsh = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}[s]
                lhs = math.log(abs(Rn[s]))
                rhs = 0.5*(logdet(float(al), float(be), tc) + logdet(float(dsh[0]) - .5, float(dsh[1]) - .5, tc)) - math.log(2*math.pi*abs(eta_np(tc)))
                wdet = max(wdet, abs(lhs - rhs)); ncase += 1
print("channel cases:", ncase)
print("main's bilinear / (R_s(numpy contour) * Kronecker at z = Q w - h_s) - 1 : max %s" % mp.nstr(wk, 3))
print("log|R_s| - [1/2 log det Box_chi + 1/2 log det Box_delta - log(2 pi |eta|)] : max %.2e" % wdet)
# plant: the relative line's half-period assignment shifted (delta of channel j used for channel i) must fail
t = TAUS[0]; tc = complex(t); p1, p2 = LINES[0]; qL, qR = 1, 2; x = (qL*p1, -2*qL*p2); y = (qR*p1, -2*qR*p2)
Rn = B.residues((float(x[0]), float(x[1])), (float(y[0]), float(y[1])), tc, rad=0.01, N=512)
am, bm = x[0] - y[0], (x[1] - y[1])/2; ap, bp = x[0] + y[0], (x[1] + y[1])/2
rhs = 0.5*(logdet(float(ap) + 0.0, float(bp) - 0.5, tc) + logdet(float(am) - .5, float(bm) - .5 + 0.5, tc)) - math.log(2*math.pi*abs(eta_np(tc)))
print("PLANT (channel i with delta's half period moved): %.2e (must be O(0.1) or more)" % abs(math.log(abs(Rn["i"])) - rhs))
