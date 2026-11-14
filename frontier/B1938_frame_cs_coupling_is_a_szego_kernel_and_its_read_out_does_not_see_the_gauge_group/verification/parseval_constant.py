"""K3. The channel kernel is the twisted d-bar Green's function, K_s(u) = sum_v e_v(u)/lambda_v over the shifted dual
lattice (lambda_v = (m+alpha) tau - (n-beta), e_v the flat sections' plane waves), so its regularised norm is
Im tau * sum_v |lambda_v|^-2 regularised: (pi^2/Im tau) Tr(Box_chi^-1), the twisted Laplacian's coincident Green's
function.  The heat-regularised Parseval sum, with the predicted universal conversion
    c_s - C_heat = 2 pi log y - pi gamma - 2 pi log pi + pi log 2     (y = Im tau),
is checked against main's own norm cA (B1656's definition) -- an independent route to B1919's identity that does not
use F_u.  Pure mathematics."""
import sys, pathlib, math
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
_a = sys.argv; sys.argv = ["x"]; import b1656_funcs as B; sys.argv = _a
G = 0.5772156649015329
def kernel(c, u, t):
    h = 1e-6; t1p = (B.th1(h, t) - B.th1(-h, t))/(2*h)
    return t1p*B.thc(c[0], c[1], u, t)/(B.thc(c[0], c[1], 0.0, t)*B.th1(u, t))
def lattice(al, be, t, lam_max):
    y = t.imag; M = int(lam_max/y) + 3; Nn = int(lam_max + abs(t.real)*M) + 3
    m = np.arange(-M, M + 1)[:, None] + al; n = np.arange(-Nn, Nn + 1)[None, :] - be
    return m, n, m*t - n
def fourier_K(al, be, t, u, delta):
    m, n, lam = lattice(al, be, t, math.sqrt(40/delta))
    y = t.imag; tt = u.imag/y; ss = u.real - tt*t.real
    return np.sum(np.exp(-delta*np.abs(lam)**2)*np.exp(2j*np.pi*(m*ss + n*tt))/lam)
def heat_sum(al, be, t, delta):
    m, n, lam = lattice(al, be, t, math.sqrt(40/(2*delta)))
    return t.imag*np.sum(np.exp(-2*delta*np.abs(lam)**2)/np.abs(lam)**2) - math.pi*math.log(1/delta)
cases = []
for t in (0.13 + 1.07j, -0.31 + 1.45j):
    for (p1, p2), sec in (((1/5, 2/5), "down"), ((3/5, 1/5), "up"), ((2/5, 4/5), "lep")):
        lf, rf = B.SECTORS[sec]; w = B.line_w(p1, p2, t)
        x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        ap, bp = x[0] + y[0], (x[1] + y[1])/2
        cs = {"1": (ap + .5, bp + .5), "i": (ap + .5, bp), "j": (ap, bp + .5), "k": (ap, bp)}
        for s in B.UNITS:
            if c[s] is None: continue
            al, be = cs[s][0] - .5, cs[s][1] - .5
            u = 0.31 + 0.22*t
            fk = [abs(fourier_K(al, be, t, u, d)/kernel(cs[s], u, t) - 1) for d in (1e-3, 2.5e-4)]
            h1, h2 = heat_sum(al, be, t, 1e-4), heat_sum(al, be, t, 5e-5)
            Ch = 2*h2 - h1                                               # removes the O(delta) term
            pred = 2*math.pi*math.log(t.imag) - math.pi*G - 2*math.pi*math.log(math.pi) + math.pi*math.log(2)
            cases.append((t, sec, s, fk, c[s] - Ch - pred, h1 - h2))
for t, sec, s, fk, d, hh in cases:
    print("tau %-14s %-4s ch %s  Fourier vs kernel: %.1e, %.1e   c_s - C_heat - predicted: %+.2e   (delta step %.1e)"
          % (t, sec, s, fk[0], fk[1], d, hh))
print("max |c_s - C_heat - predicted| = %.2e over %d channel cases" % (max(abs(c[4]) for c in cases), len(cases)))
# planted fault: the wrong sign of the log y term must fail
t = 0.13 + 1.07j; bad = [c[4] + 4*math.pi*math.log(t.imag) for c in cases if c[0] == t]
print("PLANT (log y with the opposite sign): min |diff| = %.2e (must be >> 1e-4)" % min(abs(b) for b in bad))
