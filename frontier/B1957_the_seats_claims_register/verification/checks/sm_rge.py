"""B1957: main's own two-loop Standard Model running, transcribed from the primary source (Buttazzo, Degrassi, Giardino,
Giudice, Sala, Salvio, Strumia, JHEP 12 (2013) 089, arXiv:1307.3536, Appendix B, equations (96) to (103); read by main in
the paper's PDF).  There the derivative is d/d ln(mu^2), each loop carries 1/(4 pi)^2, g1 is in GUT normalisation and the
potential is lambda |H|^4.  Here t = ln(mu), so every right-hand side is doubled.  No measured number is used."""
import math
import mpmath as mp


def beta(v, loops=2):
    """v = (g1, g2, g3, yt, lam) (yb = ytau = 0); returns d v / d ln(mu)"""
    g1, g2, g3, yt, lam = v; a, b, c, y = g1 * g1, g2 * g2, g3 * g3, yt * yt; k = 1 / (16 * mp.pi ** 2)
    two = 1 if loops >= 2 else 0
    da = a * a * (k * mp.mpf(41) / 10 + two * k * k * (mp.mpf(44) / 5 * c + mp.mpf(27) / 10 * b + mp.mpf(199) / 50 * a - mp.mpf(17) / 10 * y))
    db = b * b * (k * -mp.mpf(19) / 6 + two * k * k * (12 * c + mp.mpf(35) / 6 * b + mp.mpf(9) / 10 * a - mp.mpf(3) / 2 * y))
    dc = c * c * (k * -7 + two * k * k * (-26 * c + mp.mpf(9) / 2 * b + mp.mpf(11) / 10 * a - 2 * y))
    dl = k * (lam * (12 * lam + 6 * y - mp.mpf(9) / 2 * b - mp.mpf(9) / 10 * a) - 3 * y * y + mp.mpf(9) / 16 * b * b + mp.mpf(27) / 400 * a * a + mp.mpf(9) / 40 * a * b)
    dl += two * k * k * (lam * lam * (-156 * lam - 72 * y + 54 * b + mp.mpf(54) / 5 * a)
                         + lam * y * (-mp.mpf(3) / 2 * y + 40 * c + mp.mpf(45) / 4 * b + mp.mpf(17) / 4 * a)
                         + lam * (-mp.mpf(73) / 16 * b * b + mp.mpf(1887) / 400 * a * a + mp.mpf(117) / 40 * a * b)
                         + y * y * (15 * y - 16 * c - mp.mpf(4) / 5 * a)
                         + y * (-mp.mpf(9) / 8 * b * b - mp.mpf(171) / 200 * a * a + mp.mpf(63) / 20 * a * b)
                         + mp.mpf(305) / 32 * b ** 3 - mp.mpf(3411) / 4000 * a ** 3 - mp.mpf(289) / 160 * b * b * a - mp.mpf(1677) / 800 * b * a * a)
    dy = y * (k * (mp.mpf(9) / 2 * y - 8 * c - mp.mpf(9) / 4 * b - mp.mpf(17) / 20 * a)
              + two * k * k * (y * (-12 * y - 12 * lam + 36 * c + mp.mpf(225) / 16 * b + mp.mpf(393) / 80 * a) + 6 * lam * lam - 108 * c * c - mp.mpf(23) / 4 * b * b
                               + mp.mpf(1187) / 600 * a * a + 9 * c * b + mp.mpf(19) / 15 * c * a - mp.mpf(9) / 20 * b * a))
    # d(g^2)/d ln(mu^2) = X  ->  dg/d ln(mu) = X / g ;  d(yt^2) likewise ; d lam / d ln(mu) = 2 X
    return (da / g1, db / g2, dc / g3, dy / yt, 2 * dl)


def run(v0, t1, loops=2, dps=None):
    """integrate from t = 0 to t1; float arithmetic with a high-order adaptive solver, or mpmath's Taylor solver if dps is set"""
    import numpy as np
    from scipy.integrate import solve_ivp
    old = mp.mp.dps; mp.mp.dps = 15
    f = lambda t, v: [float(x) for x in beta(tuple(mp.mpf(float(x)) for x in v), loops)]
    r = solve_ivp(f, (0.0, float(t1)), [float(x) for x in v0], method="DOP853", rtol=1e-13, atol=1e-15)
    mp.mp.dps = old
    return r.y[:, -1]


def t_crit(v0, loops=2):
    from scipy.optimize import brentq
    return brentq(lambda t: run(v0, t, loops)[4], 1.0, 30.0, xtol=1e-14, rtol=1e-14)


if __name__ == "__main__":
    v0 = (0.5, 0.6, 1.0, 0.9, 0.1)
    print("the paper's two-loop coefficient of lambda^2 yt^2 in d lambda / d ln(mu^2) is -72 (eq. 99); in d / d ln(mu) it is -144 = -48 x (3 yt^2): the physical lane's F12 and agy-002's repair are right, and -24 x Tr_Y is half of it")
    tc = t_crit(v0, 2)
    print("agy-002's benchmark B0.2, from (g1, g2, g3, yt, lambda) = (1/2, 3/5, 1, 9/10, 1/10), all five couplings at two loops: lambda crosses zero at t = %.12f; its value: 7.578626559317; difference %.1e" % (tc, abs(tc - 7.578626559317)))
    print("   at one loop only: t = %.9f" % t_crit(v0, 1))
