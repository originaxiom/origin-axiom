"""Referee's independent implementation of STEP A v2's potential (data-free; no measured number is read or compared).

Written from the construction as stated in DESIGN.md, sharing no code with model.py / search.py:
  - theta2/3/4 summed in tau; E2, E4, E6 from their divisor-sum (Lambert) series, NOT from theta identities;
  - eta from the product formula (holomorphic, q^(1/24) prod (1 - q^n));
  - DR = Serre derivative of R computed by numerical complex differentiation of R(tau) (mp.diff), not by the theta
    derivative series;
  - the heavy spectrum per copy: neutral a^2; charged = singular values^2 of [[a, b], [0, d]];
  - V = sum over the 3n heavy eigenvalues of F(u) = (u + m0^2)^2 (log((u+m0^2)/mu^2) - 3/2) - u^2 (log(u/mu^2) - 3/2);
  - the Higgs vev generalised to a 3 x 2 matrix Phi (three doublets, two SU(2) components): only K = Phi Phi^dag enters,
    beta_i = W_i^T K conj(W_i); the draft's aligned (charge-preserving) vev is K = S S^dag.
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 30
NT = 60


# ------------------------------------------------------------------------------------------------ forms
def thetas(tau):
    t2 = mp.mpc(0); t3 = mp.mpc(1); t4 = mp.mpc(1)
    for n in range(1, NT):
        e = mp.exp(1j * mp.pi * n * n * tau)
        t3 += 2 * e; t4 += 2 * (-1) ** n * e
    for m in range(0, NT):
        t2 += 2 * mp.exp(1j * mp.pi * (m + mp.mpf(1) / 2) ** 2 * tau)
    return t2, t3, t4


def eisenstein(tau, NE=120):
    q = mp.exp(2j * mp.pi * tau)
    E2 = mp.mpc(1); E4 = mp.mpc(1); E6 = mp.mpc(1)
    qn = mp.mpc(1)
    for n in range(1, NE):
        qn *= q
        if abs(qn) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
        den = 1 - qn
        E2 -= 24 * n * qn / den
        E4 += 240 * n ** 3 * qn / den
        E6 -= 504 * n ** 5 * qn / den
    return E2, E4, E6


def eta(tau, NE=400):
    q = mp.exp(2j * mp.pi * tau)
    p = mp.mpc(1); qn = mp.mpc(1)
    for n in range(1, NE):
        qn *= q
        if abs(qn) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
        p *= (1 - qn)
    return mp.exp(2j * mp.pi * tau / 24) * p


def Rvec(tau):
    t2, t3, t4 = thetas(tau)
    d = t2 * t3 * t4
    return [-t2 ** 2 / d, -t4 ** 2 / d, 1j * t3 ** 2 / d]


def DRvec(tau):
    """Serre derivative of R (weight -1/2): (1/2 pi i) dR/dtau - (-1/2)/12 E2 R"""
    E2 = eisenstein(tau)[0]
    R = Rvec(tau)
    out = []
    for k in range(3):
        dk = mp.diff(lambda t: Rvec(t)[k], tau)
        out.append(dk / (2j * mp.pi) + E2 * R[k] / 24)
    return out


def Fvec(a, tau, et=None):
    t2, t3, t4 = thetas(tau)
    et = eta(tau) if et is None else et
    eps = mp.mpc(1j) ** (((a + 2) // 2) % 4)
    return [et ** (3 - a) * eps * t2 ** a, et ** (3 - a) * eps * t4 ** a, et ** (3 - a) * 1j * t3 ** a]


def singlet(s, p, r, tau, et=None, E=None):
    et = eta(tau) if et is None else et
    E = eisenstein(tau) if E is None else E
    return et ** s * E[1] ** p * E[2] ** r


def sweight(s, p, r):
    return mp.mpf(s) / 2 + 4 * p + 6 * r


# ------------------------------------------------------------------------------------------------ menus (as declared)
SINGLETS = [(12, 1, 0), (12, 0, 1), (20, 0, 0), (24, 0, 0), (8, 0, 1), (16, 1, 0), (8, 2, 0), (20, 1, 0),
            (16, 0, 1), (12, 2, 0), (8, 1, 1), (24, 1, 0), (20, 0, 1), (16, 2, 0), (12, 1, 1), (8, 3, 0)]
MENU = {"Z": [("F", 2), ("F", 6), ("F", -2), ("F", 10), ("F", -6), ("F", 14), ("F", -10), ("F", 18)],
        "H": [("DR", None), ("F", 2), ("F", 6), ("F", -2), ("F", 10), ("F", -6), ("F", 14), ("F", -10)]}


def triplet_value(kind, a, tau, et=None):
    if kind == "DR":
        return DRvec(tau)
    return Fvec(a, tau, et)


# ------------------------------------------------------------------------------------------------ spectrum and potential
def Ffun(u, mu2, m02):
    if u <= 0:
        return m02 ** 2 * (mp.log(m02 / mu2) - mp.mpf(3) / 2)
    return (u + m02) ** 2 * (mp.log((u + m02) / mu2) - mp.mpf(3) / 2) - u ** 2 * (mp.log(u / mu2) - mp.mpf(3) / 2)


def Fprime(u, mu2, m02):
    return 2 * (u + m02) * mp.log((u + m02) / mu2) - 2 * u * mp.log(u / mu2) - 2 * m02


def charged(a2, d2, b2):
    """squared singular values of [[a, b], [0, d]] from the matrix itself (SVD), not from a closed formula"""
    a2, d2, b2 = (max(mp.re(mp.mpmathify(v)), mp.mpf(0)) for v in (a2, d2, b2))   # beta can be -1e-40 by rounding
    a = mp.sqrt(a2); d = mp.sqrt(d2); b = mp.sqrt(b2)
    MM = mp.matrix([[a * a + b * b, b * d], [b * d, d * d]])      # M M^dag with real a, b, d (phases removable)
    ev = mp.eigsy(MM)[0]
    lo, hi = sorted([ev[0], ev[1]])
    return max(hi, mp.mpf(0)), max(lo, mp.mpf(0))


def Phi(a2, d2, b2, mu2, m02):
    sp, sm = charged(a2, d2, b2)
    return Ffun(a2, mu2, m02) + Ffun(sp, mu2, m02) + Ffun(sm, mu2, m02)


def Phi_prime(a2, d2, b2, mu2, m02):
    """dPhi/d(b^2): (G(s+) - G(s-))/(s+ - s-), G(x) = x F'(x)"""
    sp, sm = charged(a2, d2, b2)
    G = lambda x: x * Fprime(x, mu2, m02) if x > 0 else mp.mpf(0)
    if abs(sp - sm) < mp.mpf(10) ** (-20) * (sp + sm):
        h = sp * mp.mpf(10) ** -8
        return (G(sp + h) - G(sp - h)) / (2 * h)
    return (G(sp) - G(sm)) / (sp - sm)


class RefModel:
    """norms: dict with 'singlet' -> list of 2n constants c (|Y| multiplied by c), 'triplet' -> list of n constants"""
    def __init__(self, menu, n, mu2, m02, lv, sing_c, trip_c):
        self.menu, self.n = menu, n
        self.mu2, self.m02, self.lv = mp.mpf(mu2), mp.mpf(m02), mp.mpf(lv)
        self.sing_c = [mp.mpf(c) for c in sing_c]
        self.trip_c = [mp.mpf(c) for c in trip_c]
        self._cache = {}

    def pieces(self, tau):
        key = (mp.nstr(mp.re(tau), 35), mp.nstr(mp.im(tau), 35))
        if key in self._cache:
            return self._cache[key]
        et = eta(tau); E = eisenstein(tau); y2 = 2 * mp.im(tau)
        A, D, W = [], [], []
        for i in range(self.n):
            sL, sE = SINGLETS[2 * i], SINGLETS[2 * i + 1]
            A.append(y2 ** sweight(*sL) * abs(self.sing_c[2 * i] * singlet(*sL, tau, et, E)) ** 2)
            D.append(y2 ** sweight(*sE) * abs(self.sing_c[2 * i + 1] * singlet(*sE, tau, et, E)) ** 2)
            kind, a = MENU[self.menu][i]
            v = triplet_value(kind, a, tau, et)
            g = self.lv * y2 ** (mp.mpf(3) / 4) * self.trip_c[i]
            W.append([g * c for c in v])
        self._cache[key] = (A, D, W)
        return A, D, W

    def betas_K(self, W, K):
        """beta_i = W_i^T K conj(W_i) for a 3x3 Hermitian PSD K (trace 1)"""
        out = []
        for w in W:
            s = mp.mpf(0)
            for j in range(3):
                for k in range(3):
                    s += w[j] * K[j][k] * mp.conj(w[k])
            out.append(mp.re(s))
        return out

    def V_K(self, tau, K):
        A, D, W = self.pieces(tau)
        bs = self.betas_K(W, K)
        return mp.fsum(Phi(a, d, b, self.mu2, self.m02) for a, d, b in zip(A, D, bs))

    def V(self, tau, S):
        S = unit(S)
        K = [[S[j] * mp.conj(S[k]) for k in range(3)] for j in range(3)]
        return self.V_K(tau, K)

    def Qeff(self, tau, K):
        """Q_eff = sum_i Phi_i'(beta_i) conj(W_i) W_i^T: dV = tr(dK Q_eff^T)... returned as a 3x3 Hermitian matrix H with
        dV = sum_jk dK_jk H_kj, i.e. for K -> K + eps (t t^dag - S S^dag): dV/deps = t^dag H t - S^dag H S"""
        A, D, W = self.pieces(tau)
        bs = self.betas_K(W, K)
        H = mp.matrix(3, 3)
        for a, d, b, w in zip(A, D, bs, W):
            c = Phi_prime(a, d, b, self.mu2, self.m02)
            for j in range(3):
                for k in range(3):
                    H[j, k] += c * mp.conj(w[j]) * w[k]
        return H


def unit(S):
    S = [mp.mpc(c) for c in S]
    nrm = mp.sqrt(mp.fsum(abs(c) ** 2 for c in S))
    return [c / nrm for c in S]


# ------------------------------------------------------------------------------------------------ normalisations
def sup_norm_singlet(s, p, r):
    """sup over the fundamental domain of (2y)^w |eta^s E4^p E6^r|^2, by a grid and a local refinement (mpmath)"""
    w = sweight(s, p, r)
    def f(x, y):
        tau = mp.mpc(x, y)
        return (2 * y) ** w * abs(singlet(s, p, r, tau)) ** 2
    best = (mp.mpf(-1), None)
    mp.mp.dps = 20
    for xi in range(0, 11):
        x = mp.mpf(xi) / 20
        y0 = mp.sqrt(1 - x * x)
        for yi in range(0, 60):
            y = y0 + mp.mpf(yi) * (5 - y0) / 59
            v = f(x, y)
            if v > best[0]:
                best = (v, (x, y))
    mp.mp.dps = 30
    x0, y0 = best[1]
    # refine: maximise over (x in [0, 1/2], y >= sqrt(1-x^2)) by coordinate Newton on a fine local grid
    x, y = mp.mpf(x0), mp.mpf(y0)
    h = mp.mpf("0.02")
    for _ in range(60):
        improved = False
        for dx, dy in ((h, 0), (-h, 0), (0, h), (0, -h), (h, h), (-h, -h), (h, -h), (-h, h)):
            xn = min(max(x + dx, mp.mpf(0)), mp.mpf(1) / 2); yn = max(y + dy, mp.sqrt(1 - xn * xn))
            v = f(xn, yn)
            if v > best[0]:
                best = (v, (xn, yn)); x, y = xn, yn; improved = True
        if not improved:
            h /= 2
            if h < mp.mpf("1e-10"):
                break
    return best[0], (float(x), float(y))
