"""B1957: the third generation's two-loop running, transcribed by main from Buttazzo et al., arXiv:1307.3536, Appendix B,
equations (96) to (99) and (101) to (103): d/d ln(mu^2), 1/(4 pi)^2 per loop, lambda |H|^4, g1 in GUT normalisation.
Returned as d/d ln(mu) of (g1, g2, g3, yt, yb, ytau, lambda)."""
import math


def beta3(g1, g2, g3, yt, yb, yl, lam):
    a, b, c, t, B, L = g1 * g1, g2 * g2, g3 * g3, yt * yt, yb * yb, yl * yl; k = 1 / (16 * math.pi ** 2)
    da = a * a * (k * 41 / 10 + k * k * (44 * c / 5 + 27 * b / 10 + 199 * a / 50 - 17 * t / 10 - B / 2 - 3 * L / 2))
    db = b * b * (k * -19 / 6 + k * k * (12 * c + 35 * b / 6 + 9 * a / 10 - 3 * t / 2 - 3 * B / 2 - L / 2))
    dc = c * c * (k * -7 + k * k * (-26 * c + 9 * b / 2 + 11 * a / 10 - 2 * t - 2 * B))
    dl = k * (lam * (12 * lam + 6 * t + 6 * B + 2 * L - 9 * b / 2 - 9 * a / 10) - 3 * t * t - 3 * B * B - L * L + 9 * b * b / 16 + 27 * a * a / 400 + 9 * b * a / 40)
    dl += k * k * (lam * lam * (-156 * lam - 72 * t - 72 * B - 24 * L + 54 * b + 54 * a / 5)
                   + lam * t * (-3 * t / 2 - 21 * B + 40 * c + 45 * b / 4 + 17 * a / 4) + lam * B * (-3 * B / 2 + 40 * c + 45 * b / 4 + 5 * a / 4) + lam * L * (-L / 2 + 15 * b / 4 + 15 * a / 4)
                   + lam * (-73 * b * b / 16 + 1887 * a * a / 400 + 117 * b * a / 40) + t * t * (15 * t - 3 * B - 16 * c - 4 * a / 5)
                   + t * (-9 * b * b / 8 - 171 * a * a / 200 + 63 * b * a / 20) + B * B * (-3 * t + 15 * B - 16 * c + 2 * a / 5)
                   + B * (-9 * b * b / 8 + 9 * a * a / 40 + 27 * b * a / 20) + L * L * (5 * L - 6 * a / 5) + L * (-3 * b * b / 8 - 9 * a * a / 8 + 33 * b * a / 20)
                   + 305 * b ** 3 / 32 - 3411 * a ** 3 / 4000 - 289 * b * b * a / 160 - 1677 * b * a * a / 800)
    dt = t * (k * (9 * t / 2 + 3 * B / 2 + L - 8 * c - 9 * b / 4 - 17 * a / 20)
              + k * k * (t * (-12 * t - 11 * B / 4 - 9 * L / 4 - 12 * lam + 36 * c + 225 * b / 16 + 393 * a / 80) + B * (-B / 4 + 5 * L / 4 + 4 * c + 99 * b / 16 + 7 * a / 80)
                         + L * (-9 * L / 4 + 15 * b / 8 + 15 * a / 8) + 6 * lam * lam - 108 * c * c - 23 * b * b / 4 + 1187 * a * a / 600 + 9 * c * b + 19 * c * a / 15 - 9 * b * a / 20))
    dB = B * (k * (3 * t / 2 + 9 * B / 2 + L - 8 * c - 9 * b / 4 - a / 4)
              + k * k * (t * (-t / 4 - 11 * B / 4 + 5 * L / 4 + 4 * c + 99 * b / 16 + 91 * a / 80) + B * (-12 * B - 9 * L / 4 - 12 * lam + 36 * c + 225 * b / 16 + 237 * a / 80)
                         + L * (-9 * L / 4 + 15 * b / 8 + 15 * a / 8) + 6 * lam * lam - 108 * c * c - 23 * b * b / 4 - 127 * a * a / 600 + 9 * c * b + 31 * c * a / 15 - 27 * b * a / 20))
    dL = L * (k * (3 * t + 3 * B + 5 * L / 2 - 9 * b / 4 - 9 * a / 4)
              + k * k * (6 * lam * lam - 23 * b * b / 4 + 1371 * a * a / 200 + 27 * b * a / 20 + t * (-27 * t / 4 + 3 * B / 2 - 27 * L / 4 + 20 * c + 45 * b / 8 + 17 * a / 8)
                         + B * (-27 * B / 4 - 27 * L / 4 + 20 * c + 45 * b / 8 + 5 * a / 8) + L * (-3 * L - 12 * lam + 165 * b / 16 + 537 * a / 80)))
    return (da / g1, db / g2, dc / g3, dt / yt, dB / yb, dL / yl, 2 * dl)
