"""Reviewer's independent core (NOT the instrument): period-1 thetas by direct series, characteristic thetas by direct
series centred on the dominant term, the record frame's bilinears built from B1642's definitions, pairings for the four
units with eps = QJ.  Written from the mathematics, not copied from twisted_zero_mode.py."""
import mpmath as mp

mp.mp.dps = 40
J = mp.mpc(0, 1)


def ex(x):  # e^{i pi x}
    return mp.exp(J * mp.pi * x)


def thr(r, z, t, N=45):
    """Jacobi thetas, period-1 convention: th3(z|t) = sum e^{i pi t n^2 + 2 pi i n z}"""
    h = mp.mpf(1) / 2
    if r == 3:
        return mp.fsum(ex(t * n * n + 2 * n * z) for n in range(-N, N + 1))
    if r == 4:
        return mp.fsum((-1) ** n * ex(t * n * n + 2 * n * z) for n in range(-N, N + 1))
    if r == 2:
        return mp.fsum(ex(t * (n + h) ** 2 + (2 * n + 1) * z) for n in range(-N, N + 1))
    if r == 1:
        return -J * mp.fsum((-1) ** n * ex(t * (n + h) ** 2 + (2 * n + 1) * z) for n in range(-N, N + 1))


def thab(a, b, z, T, N=45):
    """theta[a,b](z|T) = sum_n e^{i pi T (n+a)^2 + 2 pi i (n+a)(z+b)}, summed around the dominant n (centre -a - Im z/Im T)"""
    c = int(mp.nint(-a - mp.im(z) / mp.im(T)))
    return mp.fsum(ex(T * (n + a) ** 2 + 2 * (n + a) * (z + b)) for n in range(c - N, c + N + 1))


QI = mp.matrix([[J, 0], [0, -J]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; ONE = mp.eye(2)
UNIT = {"1": ONE, "i": QI, "j": QJ, "k": QK}
RTH = {"1": 1, "i": 2, "j": 4, "k": 3}
CC = {"i": -1, "j": -1, "k": J}


def bil(x, y, z, t, frame=True):
    ax, bx = x; ay, by = y
    T = 2 * t
    gx0, gx1 = thab(ax, bx, z, T), thab(ax, bx, z + t, T)
    gy0, gy1 = thab(ay, by, z, T), thab(ay, by, z + t, T)
    t1 = thr(1, z, t); t1t = thr(1, z + t, t)
    D = J * ex(-t / 2) * ex(-z) * t1           # B1642's fixed sqrt(th1(z) th1(z+t))
    px = ex(bx) if frame else 1; py = ex(by) if frame else 1
    return mp.matrix([[gx0 * gy0 / t1, py * gx0 * gy1 / D], [px * gx1 * gy0 / D, px * py * gx1 * gy1 / t1t]])


def pairings(x, y, z, t, frame=True):
    B = bil(x, y, z, t, frame)
    out = {}
    for s, C in UNIT.items():
        M = QJ * C
        out[s] = mp.fsum(M[m, n] * B[m, n] for m in range(2) for n in range(2))
    return out


def wpt(x, t):
    return x[0] * t + x[1] / 2


def th1p(t):
    """th1'(0) in the period-1 convention = 2 pi eta^3, eta by product"""
    q2 = ex(2 * t)
    eta = ex(t / 12) * mp.qp(q2)
    return 2 * mp.pi * eta ** 3


def closed_R(ub, de, t):
    """R_r up to the common kappa/th1'(0): c_r th_r(ub) th_r(de)"""
    return {s: CC[s] * thr(RTH[s], ub, t) * thr(RTH[s], de, t) for s in "ijk"}


def rel_rr(R):
    num = abs(sum(R[s] ** 2 for s in "ijk"))
    den = sum(abs(R[s]) ** 2 for s in "ijk")
    return num / den
