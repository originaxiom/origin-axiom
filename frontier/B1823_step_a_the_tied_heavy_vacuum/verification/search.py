"""STEP A v2 -- menus, normalisations and the vacuum search (numpy/scipy, double precision; data-free)."""
import numpy as np
from scipy.optimize import minimize
from model import (Singlet, Triplet, Copy, form_values, eigs_from, Ffun, unit, reduce_to_F, LINV, LMAT, PMAT)

# ------------------------------------------------------------------------------------------- the declared menus (PLAN.md)
SINGLET_LIST = [  # (s, p, r): eta^s E4^p E6^r, cusp forms with s >= 8, weights 10-16; copy i takes entries 2i, 2i+1
    (12, 1, 0), (12, 0, 1),     # copy 1: W150's eta^12 E4 (weight 10) and the 1' family's weight-12 member
    (20, 0, 0), (24, 0, 0),     # copy 2
    (8, 0, 1), (16, 1, 0),      # copy 3
    (8, 2, 0), (20, 1, 0),      # copy 4
    (16, 0, 1), (12, 2, 0),     # copy 5
    (8, 1, 1), (24, 1, 0),      # copy 6
    (20, 0, 1), (16, 2, 0),     # copy 7
    (12, 1, 1), (8, 3, 0),      # copy 8
]
MENU_Z = [("F", 2), ("F", 6), ("F", -2), ("F", 10), ("F", -6), ("F", 14), ("F", -10), ("F", 18)]   # B1730's one-unit lines
MENU_H = [("DR", None), ("F", 2), ("F", 6), ("F", -2), ("F", 10), ("F", -6), ("F", 14), ("F", -10)]  # with H-cov's DR first

_SUP = {}


def sup_norm(s, p, r):
    """sup over the upper half plane of (2 Im tau)^w |eta^s E4^p E6^r|^2 (a cusp form: bounded); grid over F + Nelder-Mead"""
    key = (s, p, r)
    if key in _SUP:
        return _SUP[key]
    S = Singlet(s, p, r)
    def cm(x, y):
        x = min(max(x, 0.0), 0.5); y = max(y, np.sqrt(1 - x * x))
        th, dth, ddth, E4, E6, ae = form_values(x + 1j * y)
        return (2 * y) ** S.w * S.absval(th, E4, E6, ae) ** 2
    best = (-1.0, None)
    for x in np.linspace(0, 0.5, 11):
        for y in np.linspace(np.sqrt(1 - x * x) + 1e-12, 8, 160):
            v = cm(x, y)
            if v > best[0]:
                best = (v, (x, y))
    r = minimize(lambda q: -cm(q[0], q[1]), best[1], method="Nelder-Mead",
                 options=dict(xatol=1e-11, fatol=1e-15, maxiter=6000))
    _SUP[key] = max(-r.fun, best[0])
    return _SUP[key]


class NSinglet(Singlet):
    """a singlet divided by a constant: norm 'sup' (its canonical mass has maximum 1) or 'cusp' (leading coefficient 1)"""
    def __init__(self, s, p, r, norm="sup"):
        super().__init__(s, p, r)
        self.norm = norm
        self.c = 1.0 / np.sqrt(sup_norm(s, p, r)) if norm == "sup" else 1.0
        self.name = self.name + ("" if norm == "cusp" else " /sup")

    def absval(self, th, E4, E6, ae):
        return self.c * super().absval(th, E4, E6, ae)


class NTriplet(Triplet):
    """triplets with a declared normalisation: F_a 'N' (N(F_a) = i eta^9) or 'cusp' (B1730's, leading |coef| 1);
    DR 'cusp' (24 DR: leading |coef| 1; DR's is 1/24)"""
    def __init__(self, kind, a=None, norm="N"):
        super().__init__(kind, a, norm if kind == "F" else "cusp")
        if kind == "DR":
            self.scale = 24.0

    def vec_noeta(self, th, dth, ddth, E4):
        v, f = super().vec_noeta(th, dth, ddth, E4)
        return v, (f * self.scale if self.kind == "DR" else f)


def make_copies(n, menu="Z", tnorm="N", snorm="sup"):
    trip = MENU_Z if menu == "Z" else MENU_H
    out = []
    for i in range(n):
        YL = NSinglet(*SINGLET_LIST[2 * i], norm=snorm); YE = NSinglet(*SINGLET_LIST[2 * i + 1], norm=snorm)
        kind, a = trip[i]
        out.append(Copy(YL, YE, NTriplet(kind, a, tnorm)))
    return out


# ------------------------------------------------------------------------------------------- fast evaluation
class Model:
    def __init__(self, copies, mu2, m02, lv, M=1.0):
        self.copies, self.mu2, self.m02, self.lv, self.M = copies, mu2, m02, lv, M

    def pieces(self, tau):
        """per copy: a^2, d^2 and the triplet vector scaled so that b^2 = |S . vec|^2 (unit S)"""
        fv = form_values(tau); th, dth, ddth, E4, E6, ae = fv
        y2 = 2 * tau.imag; A = []; D = []; W = []
        for c in self.copies:
            A.append(self.M ** 2 * y2 ** c.YL.w * c.YL.absval(th, E4, E6, ae) ** 2)
            D.append(self.M ** 2 * y2 ** c.YE.w * c.YE.absval(th, E4, E6, ae) ** 2)
            vec, fac = c.Y3.vec_noeta(th, dth, ddth, E4)
            W.append(self.lv * y2 ** (c.Y3.w / 2) * fac * vec)
        return np.array(A), np.array(D), np.array(W)

    def V_pieces(self, A, D, W, S):
        b2 = np.abs(W @ S) ** 2
        mus = getattr(self, "mu2s", None)
        v = 0.0
        for i, (a2, d2, bb) in enumerate(zip(A, D, b2)):
            mu2, m02 = (self.mu2, self.m02) if mus is None else (mus[i], self.m0_ratio * mus[i])
            for u in eigs_from(a2, d2, bb):
                v += Ffun(u, mu2, m02)
        return v

    YMAX = 40.0          # a soft wall deep in the cusp (after reduction): the searches see a runaway, not an overflow

    def V(self, tau, S, reduce=True):
        if tau.imag <= 0:
            return np.inf
        S = unit(S)
        if reduce:
            tau, S = reduce_to_F(tau, S)
        if tau.imag > self.YMAX:
            return 1e30
        try:
            with np.errstate(over="raise", invalid="raise", divide="raise"):
                return self.V_pieces(*self.pieces(tau), S)
        except (FloatingPointError, OverflowError, ZeroDivisionError):
            return 1e30

    def V0(self, tau):
        """the potential at zero mixing (all b = 0): singlets only"""
        A, D, W = self.pieces(tau)
        return sum(Ffun(a, self.mu2, self.m02) * 2 + Ffun(d, self.mu2, self.m02) for a, d in zip(A, D))

    def Q(self, tau):
        """the leading-order Hermitian form: V = V0 + S^dag Q S + O(lv^4), Q = sum_i c_i conj(W_i) W_i^T"""
        A, D, W = self.pieces(tau)
        Qm = np.zeros((3, 3), dtype=complex)
        for a2, d2, w in zip(A, D, W):
            Qm += self.c_coef(a2, d2) * np.outer(w.conj(), w)
        return Qm

    def Fp(self, u):
        m, mu2 = self.m02, self.mu2
        return 2 * (u + m) * np.log((u + m) / mu2) - 2 * u * np.log(u / mu2) - 2 * m

    def c_coef(self, a2, d2):
        """dV/d(b^2) at b = 0 for one copy: (G(a^2) - G(d^2))/(a^2 - d^2), G(x) = x F'(x)"""
        G = lambda x: x * self.Fp(x)
        if abs(a2 - d2) < 1e-9 * max(a2, d2):
            h = 1e-6 * a2; return (G(a2 + h) - G(a2 - h)) / (2 * h)
        return (G(a2) - G(d2)) / (a2 - d2)


def u_star(mu2, m02):
    """the exact minimiser of F (F'(u*) = 0); u* = mu^2 only at leading order in m0^2/mu^2"""
    from scipy.optimize import brentq
    Fp = lambda u: 2 * (u + m02) * np.log((u + m02) / mu2) - 2 * u * np.log(u / mu2) - 2 * m02
    return brentq(Fp, 1e-6 * mu2, 10 * mu2, xtol=1e-15, rtol=1e-15)


def x_to(x):
    return x[0] + 1j * x[1], np.array([x[2] + 1j * x[3], x[4] + 1j * x[5], x[6] + 1j * x[7]])


def local_min(model, tau0, S0, gtol=1e-10):
    S0 = unit(S0)
    x0 = np.array([tau0.real, tau0.imag, S0[0].real, S0[0].imag, S0[1].real, S0[1].imag, S0[2].real, S0[2].imag])
    def f(x):
        tau, S = x_to(x)
        nS = np.linalg.norm(S)
        if tau.imag <= 0.05 or nS < 1e-8:
            return 1e30
        return model.V(tau, S) + (nS ** 2 - 1) ** 2
    r = minimize(f, x0, method="BFGS", options=dict(gtol=gtol, maxiter=4000))
    tau, S = x_to(r.x)
    tau, S = reduce_to_F(tau, unit(S))
    return tau, unit(S), model.V(tau, S), r


def fs_dist(S0, S1):
    ov = abs(np.vdot(unit(S0), unit(S1)))
    return float(np.arccos(min(1.0, ov)))
