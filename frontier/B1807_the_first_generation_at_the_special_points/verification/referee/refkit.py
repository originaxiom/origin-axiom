"""Referee kit for B1807 (P-431), independent of the draft's script and of B1691's qseries.py.

Direct theta / Eisenstein sums at a point tau, carried as 2-jets (value, D value, D^2 value) with D = q d/dq =
(1/2 pi i) d/dtau, so every Serre derivative is exact termwise (no finite differences).  Normalisation of R is
B1691's q-series module's (no 1/pi): R = (-th2^2, -th4^2, i th3^2) / (th2 th3 th4); RB = R/pi is B1654's R_A /
B1691's FINDINGS normalisation.
"""
import mpmath as mp

mp.mp.dps = 40
NT = 60          # theta terms each side
NE = 80          # Eisenstein terms


class J:
    """2-jet in D: (v, d, dd)"""
    __slots__ = ("v", "d", "dd")

    def __init__(self, v, d=0, dd=0):
        self.v, self.d, self.dd = mp.mpc(v), mp.mpc(d), mp.mpc(dd)

    def __add__(s, o):
        o = o if isinstance(o, J) else J(o)
        return J(s.v + o.v, s.d + o.d, s.dd + o.dd)
    __radd__ = __add__

    def __neg__(s): return J(-s.v, -s.d, -s.dd)
    def __sub__(s, o): return s + (-(o if isinstance(o, J) else J(o)))
    def __rsub__(s, o): return (-s) + o

    def __mul__(s, o):
        if not isinstance(o, J):
            o = mp.mpc(o); return J(s.v * o, s.d * o, s.dd * o)
        return J(s.v * o.v, s.d * o.v + s.v * o.d, s.dd * o.v + 2 * s.d * o.d + s.v * o.dd)
    __rmul__ = __mul__

    def inv(s):
        g, g1, g2 = s.v, s.d, s.dd
        return J(1 / g, -g1 / g ** 2, 2 * g1 ** 2 / g ** 3 - g2 / g ** 2)

    def __truediv__(s, o): return s * (o.inv() if isinstance(o, J) else 1 / mp.mpc(o))

    def D(s):
        """D of the jet, as a 1-jet (dd unknown -> NaN marker not needed; we only use D once on order-2 jets)"""
        return J(s.d, s.dd, mp.nan)


def qpow(tau, m):
    """e^{pi i tau m} = q^{m/2}, D-factor m/2"""
    return mp.exp(mp.pi * 1j * tau * m)


def thetas(tau):
    tau = mp.mpc(tau)
    t2 = J(0); t3 = J(0); t4 = J(0)
    for n in range(-NT, NT):
        m = (n + mp.mpf(1) / 2) ** 2; e = qpow(tau, m); f = m / 2
        t2 = t2 + J(e, f * e, f * f * e)
    for n in range(-NT, NT + 1):
        m = mp.mpf(n * n); e = qpow(tau, m); f = m / 2; s = (-1) ** n
        t3 = t3 + J(e, f * e, f * f * e)
        t4 = t4 + J(s * e, s * f * e, s * f * f * e)
    return t2, t3, t4


def sigma(k, n): return sum(d ** k for d in range(1, n + 1) if n % d == 0)


SIG = {k: [0] + [sigma(k, n) for n in range(1, NE + 1)] for k in (1, 3, 5)}


def eis(tau, k, c):
    tau = mp.mpc(tau); q = mp.exp(2j * mp.pi * tau); out = J(1)
    qn = mp.mpc(1)
    for n in range(1, NE + 1):
        qn = qn * q; a = c * SIG[k - 1][n] * qn
        out = out + J(a, n * a, n * n * a)
    return out


def E2(t): return eis(t, 2, -24)
def E4(t): return eis(t, 4, 240)
def E6(t): return eis(t, 6, -504)


def eta6_product(tau):
    """independent: q^{1/4} prod (1 - q^n)^6 (value only)"""
    tau = mp.mpc(tau); q = mp.exp(2j * mp.pi * tau); p = mp.mpc(1)
    for n in range(1, 400):
        p *= (1 - q ** n)
        if abs(q ** n) < mp.mpf(10) ** (-mp.mp.dps - 5): break
    return mp.exp(2j * mp.pi * tau / 4) * p ** 6


def basis(tau):
    """R, dR (Serre, weight -1/2 -> 3/2), d2R (Serre at 3/2), as lists of mpc; plus e2,e4,e6 values, eta6"""
    t2, t3, t4 = thetas(tau)
    den = t2 * t3 * t4
    R = [(-(t2 * t2)) / den, (-(t4 * t4)) / den, (t3 * t3) * 1j / den]
    e2 = E2(tau)
    # dR = D R + (1/24) E2 R   (weight -1/2)
    dR = [J(r.d + e2.v * r.v / 24, r.dd + (e2.d * r.v + e2.v * r.d) / 24) for r in R]   # 1-jets
    # d2R = D dR - (1/8) E2 dR  (weight 3/2)
    d2R = [g.d - e2.v * g.v / 8 for g in dR]
    eta6 = (den.v / 2) ** 2
    return [r.v for r in R], [g.v for g in dR], d2R, eta6, e2, E4(tau).v, E6(tau).v


def dot(u, v): return sum(a * b for a, b in zip(u, v))
def nrm2(u): return sum(abs(a) ** 2 for a in u)
