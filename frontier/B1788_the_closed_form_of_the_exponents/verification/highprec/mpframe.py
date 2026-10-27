"""Referee's own high-precision re-implementation of B1656's frame as used by B1726's compute() / B1788's layers.one.
Independent code: theta series written here (no b1656_funcs import for the frame); only B1691's Higgs q-series (S) and
B1667's L column are read from the record.  Exact rational twists a = q alpha, b_char = 2 q beta.
    M(u) = [[X0 Y0/th1(u), e^{i pi by} X0 Y1/den], [e^{i pi bx} X1 Y0/den, e^{i pi(bx+by)} X1 Y1/th1(u+tau)]],
    X0 = thc(ax, bx, u, 2tau), X1 = thc(ax, bx, u+tau, 2tau), den = i e^{-i pi tau/2} e^{-i pi u} th1(u).
c_s by the instrument's own quadrature rule (polar, log-r Gauss 96 x 64 per vertex sector, eps = 1e-5, + pi eps^2 |a0|^2),
evaluated in mpmath (so the c-differences are exact to the rule, not to double precision)."""
import sys, io, json, math, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp

ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
mp.mp.dps = 40
I = mp.mpc(0, 1); PI = mp.pi
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
NT = 7

def mpm(rows): return mp.matrix([[mp.mpc(v) for v in r] for r in rows])
QI = mpm([[1j, 0], [0, -1j]]); QJ = mpm([[0, 1], [-1, 0]]); QK = QI * QJ; EPS = QJ; ONE = mpm([[1, 0], [0, 1]])
UNITS = {"1": ONE, "i": QI, "j": QJ, "k": QK}; KEYS = list(UNITS)
BLOCKS = [QJ, QI, QK]
EC = {s: EPS * C for s, C in UNITS.items()}
def ip(A, B): return sum(A[m, n] * B[m, n] for m in range(2) for n in range(2))
G = mp.matrix(4, 4)
for ti, t in enumerate(KEYS):
    for si, s in enumerate(KEYS): G[ti, si] = ip(EC[t], UNITS[s])
Gi = G ** -1
EDUAL = {}
for a_, ka in enumerate(KEYS):
    Mx = mp.matrix(2, 2)
    for b_, kb in enumerate(KEYS): Mx += Gi[b_, a_] * UNITS[kb]
    EDUAL[ka] = Mx


class Frame:
    def __init__(self, alpha, beta, sec, tau):
        self.tau = mp.mpc(tau); t = self.tau
        lf, rf = SECTORS[sec]; ql, qr = SIXY[lf], SIXY[rf]
        self.ax, self.bx = Fr(ql) * alpha, 2 * Fr(ql) * beta
        self.ay, self.by = Fr(qr) * alpha, 2 * Fr(qr) * beta
        T = 2 * t
        def consts(a, b):
            a = mp.mpf(a.numerator) / a.denominator; b = mp.mpf(b.numerator) / b.denominator
            C = {n: mp.exp(I * PI * T * (n + a) ** 2 + 2 * I * PI * (n + a) * b) for n in range(-NT, NT + 1)}
            D = {n: C[n] * mp.exp(2 * I * PI * (n + a) * t) for n in C}
            return a, C, D
        self.axm, self.Cx, self.Dx = consts(self.ax, self.bx)
        self.aym, self.Cy, self.Dy = consts(self.ay, self.by)
        self.Q1 = {k: (-1) ** k * mp.exp(I * PI * t * (k + mp.mpf(1) / 2) ** 2) for k in range(-NT, NT)}
        self.ph_bx = mp.exp(I * PI * (mp.mpf(self.bx.numerator) / self.bx.denominator))
        self.ph_by = mp.exp(I * PI * (mp.mpf(self.by.numerator) / self.by.denominator))
        self.emt2 = mp.exp(-I * PI * t / 2); self.emt = mp.exp(-I * PI * t)
        # residues (analytic)
        th1p0 = PI * mp.fsum((-1) ** k * (2 * k + 1) * mp.exp(I * PI * t * (k + mp.mpf(1) / 2) ** 2) for k in range(-NT, NT))
        X0, X1 = mp.fsum(self.Cx.values()), mp.fsum(self.Dx.values())
        Y0, Y1 = mp.fsum(self.Cy.values()), mp.fsum(self.Dy.values())
        self.r = [[X0 * Y0 / th1p0, self.ph_by * X0 * Y1 / (I * self.emt2 * th1p0)],
                  [self.ph_bx * X1 * Y0 / (I * self.emt2 * th1p0), self.ph_bx * self.ph_by * X1 * Y1 / (-self.emt * th1p0)]]
        r = self.r
        self.R = {"1": r[0][1] - r[1][0], "i": -I * (r[0][1] + r[1][0]), "j": -(r[0][0] + r[1][1]), "k": I * (r[0][0] - r[1][1])}

    def M(self, u):
        e = mp.exp(I * PI * u); e1 = e * e
        pw = {0: mp.mpf(1)}
        for n in range(1, NT + 1): pw[n] = pw[n - 1] * e1
        ie1 = 1 / e1
        for n in range(1, NT + 1): pw[-n] = pw[-n + 1] * ie1
        ex = mp.exp(2 * I * PI * self.axm * u); ey = mp.exp(2 * I * PI * self.aym * u)
        X0 = ex * mp.fsum(self.Cx[n] * pw[n] for n in self.Cx); X1 = ex * mp.fsum(self.Dx[n] * pw[n] for n in self.Dx)
        Y0 = ey * mp.fsum(self.Cy[n] * pw[n] for n in self.Cy); Y1 = ey * mp.fsum(self.Dy[n] * pw[n] for n in self.Dy)
        t1 = -I * e * mp.fsum(self.Q1[k] * pw[k] for k in self.Q1)
        t1t = -self.emt * t1 * ie1                              # th1(u + tau) = -e^{-i pi tau} e^{-2 pi i u} th1(u)
        den = I * self.emt2 / e * t1
        return [[X0 * Y0 / t1, self.ph_by * X0 * Y1 / den], [self.ph_bx * X1 * Y0 / den, self.ph_bx * self.ph_by * X1 * Y1 / t1t]]

    def P(self, u):
        m = self.M(u)
        return {"1": m[0][1] - m[1][0], "i": -I * (m[0][1] + m[1][0]), "j": -(m[0][0] + m[1][1]), "k": I * (m[0][0] - m[1][1])}

    def residues_contour(self, rad=mp.mpf("0.01"), N=64):
        acc = {s: 0 for s in KEYS}
        for k in range(N):
            u = rad * mp.expjpi(2 * mp.mpf(k) / N); p = self.P(u)
            for s in KEYS: acc[s] += p[s] * u
        return {s: acc[s] / N for s in KEYS}

    def cA(self, eps=1e-5, nth=96, ns=64, zero=mp.mpf(10) ** -30):
        t = self.tau; R = self.R; scale = max(abs(R[s]) for s in KEYS)
        live = [s for s in KEYS if abs(R[s]) > zero * scale]
        # a0 by the instrument's circle mean
        rad, N = mp.mpf("0.05"), 128; A0 = {s: 0 for s in live}
        for k in range(N):
            u = rad * mp.expjpi(2 * mp.mpf(k) / N); p = self.P(u)
            for s in live: A0[s] += p[s] / R[s] - 1 / u
        A0 = {s: A0[s] / N for s in live}
        v = [mp.mpf(0.5) + t / 2, -mp.mpf(0.5) + t / 2, -mp.mpf(0.5) - t / 2, mp.mpf(0.5) - t / 2]
        br = sorted(mp.arg(z) % (2 * PI) for z in v); br.append(br[0] + 2 * PI)
        xg, wg = np.polynomial.legendre.leggauss(nth); xs, ws = np.polynomial.legendre.leggauss(ns)
        xg = [mp.mpf(float(q)) for q in xg]; wg = [mp.mpf(float(q)) for q in wg]
        xs = [mp.mpf(float(q)) for q in xs]; ws = [mp.mpf(float(q)) for q in ws]
        lo = mp.log(eps); tot = {s: mp.mpf(0) for s in live}
        for a, b in zip(br[:-1], br[1:]):
            for xi, wi in zip(xg, wg):
                th = (b - a) / 2 * xi + (b + a) / 2; wt = (b - a) / 2 * wi
                d = mp.expj(th); y1 = mp.im(d) / mp.im(t); x1 = mp.re(d) - y1 * mp.re(t)
                hi = mp.log(mp.mpf(1) / 2 / max(abs(x1), abs(y1)))
                for xj, wj in zip(xs, ws):
                    sg = (hi - lo) / 2 * xj + (hi + lo) / 2; w2 = (hi - lo) / 2 * wj
                    rr = mp.exp(sg); p = self.P(rr * d)
                    for s in live: tot[s] += wt * w2 * abs(p[s] / R[s]) ** 2 * rr ** 2
        return {s: (tot[s] - 2 * PI * mp.log(1 / mp.mpf(eps)) + PI * mp.mpf(eps) ** 2 * abs(A0[s]) ** 2 if s in live else None) for s in KEYS}


_te = None
def S_of(tau):
    global _te
    if _te is None:
        P = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification"; sys.path.insert(0, str(P))
        spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
        dps = mp.mp.dps
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
        mp.mp.dps = dps; _te = te
    av = [_te.ev(cc, mp.mpc(tau)) for cc in _te.B[1]]
    return av[0] * QI + av[1] * QJ + av[2] * QK

COL = sorted((p["tau"][1], p["L_max"]) for p in json.loads(open(ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
def Lmax(y): return float(np.interp(y, [q[0] for q in COL], [q[1] for q in COL]))

def conjm(A): return mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])

def coupling(S, Mw):
    Y = mp.matrix(3, 3)
    for a, Ca in enumerate(BLOCKS):
        for b, Cb in enumerate(BLOCKS):
            Y[a, b] = ip(Ca.T * EPS * S * Cb, Mw)
    return Y

def ratios(fr, c, y, S, extra=None):
    L = Lmax(y); u = {}
    for s in KEYS:
        if c[s] is not None and 2 * PI * L + c[s] > 0: u[s] = mp.sqrt(2 * PI * L + c[s]) * fr.R[s]
        else: u[s] = 0
    Mw = mp.matrix(2, 2)
    for s in KEYS: Mw += u[s] * EDUAL[s]
    out = {}
    for rn, SS in (("S", S), ("St", EPS * conjm(S) * EPS.T)):
        sv = sorted([abs(v) for v in mp.svd_c(coupling(SS, Mw), compute_uv=False)], reverse=True)
        out[rn] = (sv[1] / sv[0], sv[2] / sv[0])
    detM = Mw[0, 0] * Mw[1, 1] - Mw[0, 1] * Mw[1, 0]
    return out, detM, Mw
