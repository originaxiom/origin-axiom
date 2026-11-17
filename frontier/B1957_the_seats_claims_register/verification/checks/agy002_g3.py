"""B1957: agy-002's gate 3 (radiative breaking and the scale), recomputed by main.  Data-free: every input is the seat's
stated benchmark; no measured number.
G3.1  the Higgs mass term's two-loop anomalous dimension: Luo and Xiao (hep-ph/0207271), equations (11) and (12), against
      Buttazzo et al. (arXiv:1307.3536), equation (100), both read by main in the papers; and the seat's two sample values.
G3.2  the mass term keeps its sign along the Standard Model's own flow (it is multiplied by an exponential); the seat's
      benchmark minimum; the sign of the quartic's beta function at lambda = 0 with and without the top.
G3.3  the two thresholds, derived by main from the one-loop effective potential: a heavy Majorana neutrino and a heavy
      scalar coupled by lambda_HS |H|^2 |S|^2; compared with the published matching (Brivio and Trott, arXiv:1809.03450,
      equations (3.9) and (3.10), read in the paper).
G3.4  the portal's zero crossing at the seat's benchmark, and the arithmetic of the hierarchy's price."""
import sys, pathlib, math
from fractions import Fraction as F
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import sm_rge_matrix as R
K = R.K; NG = 3


def gamma_m2(v, loops=2):
    """d ln(m^2) / d ln(mu), Luo and Xiao (11), (12); their lambda (the potential (lambda/2)(phi^dagger phi)^2)"""
    g, H, FD, FL, lam = R.unpack(v); a, b, c = g * g
    U, D, E = H.conj().T @ H, FD.conj().T @ FD, FL.conj().T @ FL; tr = lambda M: np.trace(M).real
    Y2 = tr(3 * U + 3 * D + E); HS = tr(3 * U @ U + 3 * D @ D + E @ E)
    Y4 = (17 / 20 * a + 9 / 4 * b + 8 * c) * tr(U) + (1 / 4 * a + 9 / 4 * b + 8 * c) * tr(D) + 3 / 4 * (a + b) * tr(E)
    g1 = 6 * lam + 2 * Y2 - 9 / 10 * a - 9 / 2 * b
    g2 = (-15 * lam ** 2 - 12 * lam * Y2 - 9 / 2 * HS - 21 * tr(U @ D) + (36 / 5 * a + 36 * b) * lam + 5 * Y4
          + (NG + 471 / 400) * a * a + 9 / 8 * a * b + (5 * NG - 385 / 16) * b * b)
    return K * g1 + (K * K * g2 if loops >= 2 else 0.0)


def flow(v0, m0, t1, source=0.0):
    def f(t, y):
        v = y[:58]; gm = gamma_m2(v); return np.concatenate([R.rhs(t, v), [gm * y[58] + source, gm]])        # y = (couplings, m^2, integral of gamma)
    return solve_ivp(f, (0.0, t1), np.concatenate([v0, [m0, 0.0]]), method="DOP853", rtol=1e-12, atol=1e-15, dense_output=True)


if __name__ == "__main__":
    # G3.1
    yt2, yb2, yl2, g1s, g2s, g3s, lam = F(7, 11), F(3, 13), F(2, 17), F(5, 19), F(6, 23), F(9, 29), F(4, 31)       # the seat's sample; lam is Buttazzo's
    lx = 2 * lam; Y2 = 3 * yt2 + 3 * yb2 + yl2; HS = 3 * yt2 ** 2 + 3 * yb2 ** 2 + yl2 ** 2
    Y4 = (F(17, 20) * g1s + F(9, 4) * g2s + 8 * g3s) * yt2 + (F(1, 4) * g1s + F(9, 4) * g2s + 8 * g3s) * yb2 + F(3, 4) * (g1s + g2s) * yl2
    LX1 = 6 * lx + 2 * Y2 - F(9, 10) * g1s - F(9, 2) * g2s
    LX2 = (-15 * lx ** 2 - 12 * lx * Y2 - F(9, 2) * HS - 21 * yt2 * yb2 + (F(36, 5) * g1s + 36 * g2s) * lx + 5 * Y4
           + (3 + F(471, 400)) * g1s ** 2 + F(9, 8) * g1s * g2s + (15 - F(385, 16)) * g2s ** 2)
    B1 = 2 * (6 * lam + 3 * yt2 + 3 * yb2 + yl2 - F(9, 4) * g2s - F(9, 20) * g1s)
    B2 = 2 * (lam * (-30 * lam - 36 * yt2 - 36 * yb2 - 12 * yl2 + 36 * g2s + F(36, 5) * g1s)
              + yt2 * (-F(27, 4) * yt2 - F(21, 2) * yb2 + 20 * g3s + F(45, 8) * g2s + F(17, 8) * g1s) + yb2 * (-F(27, 4) * yb2 + 20 * g3s + F(45, 8) * g2s + F(5, 8) * g1s)
              + yl2 * (-F(9, 4) * yl2 + F(15, 8) * g2s + F(15, 8) * g1s) - F(145, 32) * g2s ** 2 + F(1671, 800) * g1s ** 2 + F(9, 16) * g2s * g1s)
    print("G3.1: Luo and Xiao (11), (12) against Buttazzo et al. (100), exact rationals: one loop %s, two loops %s" % (LX1 == B1, LX2 == B2))
    print("      values %s and %s; the seat's: 367247879/65865514 and -886154046205665125/503238848400166736: %s, %s" % (B1, B2, B1 == F(367247879, 65865514), B2 == F(-886154046205665125, 503238848400166736)))
    # G3.2
    gu = math.sqrt(4 * math.pi / 45); Yu, Yd, Ye = np.diag([1 / 100, 1 / 20, 1 / 2]), np.diag([1 / 200, 1 / 40, 1 / 5]), np.diag([1 / 300, 1 / 50, 1 / 8])
    s = flow(R.pack([gu, gu, gu], Yu, Yd, Ye, 2 / 8), 1.0, -28.0); ts = np.linspace(0, -28, 2801); m = s.sol(ts)[-2]; ig = s.sol(ts)[-1]
    print("G3.2: the seat's benchmark, 28 e-folds down from m^2 = 1: m^2 against exp(integral of gamma): %.1e; least m^2 along the flow %.4f (the seat: +0.6102); it never changes sign" % (np.abs(m / np.exp(ig) - 1).max(), m.min()))
    z = np.zeros((3, 3)); bl = lambda Y: R.unpack(R.rhs(0, R.pack([1 / 2, 3 / 5, 4 / 5], Y, z if Y is z else Yd, z if Y is z else Ye, 0.0)))[4] / 2
    print("      the quartic's beta function at lambda = 0, at (g1, g2, g3) = (1/2, 3/5, 4/5): gauge only %+.3e (the seat: +1.26e-3); with a top of 9/10 %+.3e (the seat: -2.36e-2)" % (bl(z), bl(np.diag([1 / 100, 1 / 20, 9 / 10]))))
    # G3.3
    y, h, M, mu, lhs, MS, dS = sp.symbols("y h M mu lambda_HS M_S d_S", positive=True); x = sp.symbols("x", positive=True)
    mD2 = y ** 2 * h ** 2 / 2                                                 # (y h / sqrt 2)^2, with |H|^2 = h^2 / 2
    disc = sp.sqrt((M ** 2 + 2 * x) ** 2 - 4 * x ** 2); mp_, mm_ = (M ** 2 + 2 * x + disc) / 2, (M ** 2 + 2 * x - disc) / 2   # eigenvalues of the squared seesaw matrix, x = m_D^2
    assert sp.simplify(mp_ + mm_ - (M ** 2 + 2 * x)) == 0 and sp.simplify(mp_ * mm_ - x ** 2) == 0
    V1 = -sp.Rational(2, 64) / sp.pi ** 2 * (mp_ ** 2 * (sp.log(mp_ / mu ** 2) - sp.Rational(3, 2)))                         # the heavy state; the light one starts at x^4
    ser = sp.series(V1, x, 0, 3).removeO(); c1 = sp.simplify(ser.coeff(x, 1)); c2 = sp.simplify(ser.coeff(x, 2))
    want1 = M ** 2 / (8 * sp.pi ** 2) * (1 + sp.log(mu ** 2 / M ** 2)); want2 = -1 / (16 * sp.pi ** 2) * (1 - sp.log(mu ** 2 / M ** 2))
    print("G3.3: heavy Majorana neutrino, one-loop effective potential: coefficient of y^2 |H|^2 is (M^2 / 8 pi^2)(1 + ln(mu^2 / M^2)): %s; of y^4 |H|^4 is -(1 / 16 pi^2)(1 - ln(mu^2 / M^2)): %s" % (sp.simplify(sp.expand_log(c1 - want1, force=True)) == 0, sp.simplify(sp.expand_log(c2 - want2, force=True)) == 0))
    print("      so d(m_H^2)/d ln(mu) = -y^2 M^2 / (4 pi^2): %s; the same as Brivio and Trott's corrected matching, equations (3.9), (3.10), whose m^2 enters as -(m^2 / 2) H^dagger H" % (sp.simplify(sp.expand_log(-sp.diff(c1, mu) * mu + M ** 2 / (4 * sp.pi ** 2), force=True)) == 0))
    print("      the finite part's sign: 1 + ln(mu^2 / M^2) is +1 at mu = M and -1/2 at mu = M e^(-3/4) (Brivio and Trott's choice): the neutrino's threshold raises m_H^2 in the first and lowers it in the second")
    H2 = sp.symbols("H2", positive=True); VS = dS / (64 * sp.pi ** 2) * (MS ** 2 + lhs * H2) ** 2 * (sp.log((MS ** 2 + lhs * H2) / mu ** 2) - sp.Rational(3, 2))
    cS = sp.simplify(sp.series(VS, H2, 0, 2).removeO().coeff(H2, 1)); wantS = dS * lhs * MS ** 2 / (32 * sp.pi ** 2) * (sp.log(MS ** 2 / mu ** 2) - 1)
    print("      heavy scalars, d_S real components of mass M_S: coefficient of |H|^2 is (d_S lambda_HS M_S^2 / 32 pi^2)(ln(M_S^2 / mu^2) - 1): %s; so d(m_H^2)/d ln(mu) = +d_S lambda_HS M_S^2 / (16 pi^2): %s" % (sp.simplify(sp.expand_log(cS - wantS, force=True)) == 0, sp.simplify(sp.expand_log(-sp.diff(cS, mu) * mu - dS * lhs * MS ** 2 / (16 * sp.pi ** 2), force=True)) == 0))
    # G3.4
    gu = math.sqrt(4 * math.pi / 50); src = 16 * 0.5 / (16 * math.pi ** 2)
    s = flow(R.pack([gu, gu, gu], Yu, Yd, Ye, 2 / 8), 0.1, -4.0, source=src); tc = brentq(lambda t: s.sol(t)[-2], -4.0, 0.0, xtol=1e-13)
    print("G3.4: the portal at the seat's benchmark (16 components, lambda_HS = 1/2, m^2 = 1/10 at the top): m^2 crosses zero at t = %.8f (the seat: -1.95017760; its referee: -1.95017764); the quartic there %.4f > 0" % (tc, s.sol(tc)[57] / 2))
    print("      the hierarchy's price as the seat defines it, (source x 4 e-folds) / exp(-56) = %.3e (the seat: 4.24e23): arithmetic, no dynamics" % (src * 4 * math.exp(56)))
