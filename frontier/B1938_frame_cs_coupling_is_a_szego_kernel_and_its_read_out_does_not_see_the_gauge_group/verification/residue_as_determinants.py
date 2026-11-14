"""K4. The residue's modulus is a product of two twisted determinants:  |vt[c](0)/eta|^2 = det Box_chi (the zeta-regularised
determinant of the flat Laplacian on the line bundle with holonomy chi = c - (1/2,1/2); Ray-Singer 1973 via Kronecker's
second limit formula).  Hence |R_s| = |kappa_s| sqrt(det Box_{c_s} det Box_{d_s}) / (2 pi |eta|).
Checked here by an independent zeta computation: -zeta'(0) of sum_v |lambda_v|^-2s over the shifted lattice, from the
lattice theta series by Mellin (zeta(0) = 0, so the eigenvalue scale drops out).  Pure mathematics."""
import sys, pathlib, math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import exp1
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
_a = sys.argv; sys.argv = ["x"]; import b1656_funcs as B; sys.argv = _a
def eta(t):
    q = np.exp(2j*np.pi*t); n = np.arange(1, 400); return np.exp(1j*np.pi*t/12)*np.prod(1 - q**n)
def Theta(al, be, t, x):
    lam_max = math.sqrt(46/x); y = t.imag; M = int(lam_max/y) + 3; Nn = int(lam_max + abs(t.real)*M) + 3
    m = np.arange(-M, M + 1)[:, None] + al; n = np.arange(-Nn, Nn + 1)[None, :] - be
    return np.sum(np.exp(-x*np.abs(m*t - n)**2))
def minus_zeta_prime0(al, be, t):
    y = t.imag
    # A(0) = int_0^1 (Theta - pi/(x y)) dx/x - pi/y + int_1^inf Theta dx/x ; -zeta'(0) = -A(0)
    xg, wg = leggauss(60)
    lo = 0.0
    for a, b in ((0.02, 0.1), (0.1, 0.3), (0.3, 1.0)):
        xs = 0.5*(b - a)*xg + 0.5*(b + a); lo += 0.5*(b - a)*sum(wi*(Theta(al, be, t, xi) - math.pi/(xi*y))/xi for xi, wi in zip(xs, wg))
    small = Theta(al, be, t, 0.02) - math.pi/(0.02*y)                          # the neglected piece below x = 0.02
    # int_1^inf Theta(x) dx/x = sum_v E_1(|lambda_v|^2), term by term (exact; E_1 decays like e^-z/z)
    M = int(9/y) + 3; Nn = int(9 + abs(t.real)*M) + 3
    m = np.arange(-M, M + 1)[:, None] + al; n = np.arange(-Nn, Nn + 1)[None, :] - be
    z2 = np.abs(m*t - n)**2; hi = float(np.sum(exp1(z2))); tail = float(np.max(exp1(z2[z2 > 70]))) if np.any(z2 > 70) else 0.0
    return -(lo - math.pi/y + hi), abs(small), abs(tail)
for t in (0.13 + 1.07j, -0.31 + 1.45j, 0.5 + 0.8660254037844386j):
    for (a, b) in ((0.2 + .5, -0.4 + .5), (0.6 + .5, 0.2), (0.35, 0.15 + .5), (0.1, 0.7)):
        al, be = a - .5, b - .5
        lhs = math.log(abs(B.thc(a, b, 0.0, t)/eta(t))**2)
        rhs, small, tail = minus_zeta_prime0(al, be, t)
        print("tau %-22s c=(%.2f,%.2f)  log|vt/eta|^2 = %+.12f   -zeta'(0) = %+.12f   diff %.1e  (neglected %.0e, %.0e)"
              % (t, a, b, lhs, rhs, lhs - rhs, small, tail))
# planted fault: the characteristic not shifted by (1/2,1/2) must fail
t = 0.13 + 1.07j; a, b = 0.7, 0.1
print("PLANT (chi = c instead of c - (1/2,1/2)): diff %.2e (must be O(1))" % (math.log(abs(B.thc(a, b, 0.0, t)/eta(t))**2) - minus_zeta_prime0(a, b, t)[0]))
