#!/usr/bin/env python3
"""CLAIM CARD script for P-596 and P-568's first half: f(d), the rank of FR-FIB's ten outputs in tau, per branch.
Sealed and dependency-free: it imports only the standard library, numpy and mpmath, and reads no file. Data-free: no
measured value is used, and no inter-sector value is printed.

    python3 -I fd_rank.py

Built by build_fd_rank.py from main at 88a1e9474. It copies main's frame code verbatim (marked below):
  - qseries.py and the Higgs directions' series from the_exponents.py (B1691);
  - route A and the coupling of b1656_funcs.py (B1691's correction folder);
  - DIRS, SECTORS, direction, radii and rows_at of cm_zero_line.py (B1821), with mods() returning the embedded objects;
  - the column Re tau = 1/4 of B1667's the_canonical_cusp.json (13 points), for the radii.
The rank computation is part (1) of this seat's relations_check.py version 2 (796f02e2b).

The count. On a branch (line, direction, radius rule, reading; c by hand, H = I) the frame's only continuous input is
tau, so its outputs there form at most a two-parameter family. For each branch with the CKM defined and positive
ratios, the gradients in (Re tau, Im tau) of the ten outputs (logs of the six mass ratios and of |V_us|, |V_cb|, |V_ub|;
J itself) by central differences at step 1e-5. An output below 1e-6, or a gradient below 1e-8, is dropped from that
branch's gradients. The branch has rank 2 when two kept gradients are not parallel; printed are the largest |sin| of
the angle between two kept gradients, its distribution over the branches, and the counts below 0.1 and 1e-3.
"""
import contextlib
import io
import itertools
import math
import types
from fractions import Fraction
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

# ---- verbatim: frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py, lines 1-88 (main at 88a1e9474)
"""P-227 exploration: exact q-series in x = q^(1/8) with Gaussian-rational coefficients.
A series is a dict {power of x: complex Fraction pair (re, im)}; truncated at x^N."""
from fractions import Fraction as F

N = 240                                     # x^240 = q^30


class S:
    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != (0, 0)}

    @staticmethod
    def c(re, im=0, k=0): return S({k: (F(re), F(im))})

    def __add__(self, o):
        d = dict(self.d)
        for k, (a, b) in o.d.items():
            x, y = d.get(k, (F(0), F(0))); d[k] = (x + a, y + b)
        return S(d)

    def __neg__(self): return S({k: (-a, -b) for k, (a, b) in self.d.items()})
    def __sub__(self, o): return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, S): o = S.c(o)
        d = {}
        for k1, (a1, b1) in self.d.items():
            for k2, (a2, b2) in o.d.items():
                k = k1 + k2
                if k > N: continue
                x, y = d.get(k, (F(0), F(0))); d[k] = (x + a1 * a2 - b1 * b2, y + a1 * b2 + b1 * a2)
        return S(d)
    __rmul__ = __mul__

    def conj(self): return S({k: (a, -b) for k, (a, b) in self.d.items()})
    def ord(self): return min(self.d) if self.d else None
    def lead(self): k = self.ord(); return None if k is None else self.d[k]

    def inv(self):
        """the recursion t_m = -(1/s0) sum_{j=1..m} s_j t_{m-j}, exact"""
        k0 = self.ord(); a0, b0 = self.d[k0]; n2 = a0 * a0 + b0 * b0
        i0 = (a0 / n2, -b0 / n2)
        mul = lambda p, q: (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])
        M = N + k0                                 # 1/self = x^-k0 sum t_m x^m, keep powers <= N
        sj = [self.d.get(k0 + j, (F(0), F(0))) for j in range(M + 1)]
        t = [i0]
        for m in range(1, M + 1):
            acc = (F(0), F(0))
            for j in range(1, m + 1):
                if sj[j] != (0, 0):
                    pr = mul(sj[j], t[m - j]); acc = (acc[0] + pr[0], acc[1] + pr[1])
            v = mul(i0, acc); t.append((-v[0], -v[1]))
        return S({m - k0: t[m] for m in range(M + 1) if m - k0 <= N})

    def qdq(self):                               # q d/dq x^m = (m/8) x^m
        return S({k: (a * F(k, 8), b * F(k, 8)) for k, (a, b) in self.d.items()})


def theta2():
    d = {}; n = 0
    while (2 * n + 1) ** 2 <= N:
        d[(2 * n + 1) ** 2] = (F(2), F(0)); n += 1
    return S(d)


def theta3(sign=1):
    d = {0: (F(1), F(0))}; n = 1
    while 4 * n * n <= N:
        d[4 * n * n] = (F(2 * (sign ** n)), F(0)); n += 1
    return S(d)


def sigma(k, n): return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eis(k, c):
    d = {0: (F(1), F(0))}
    for n in range(1, N // 8 + 1): d[8 * n] = (F(c * sigma(k - 1, n)), F(0))
    return S(d)


E2 = lambda: eis(2, -24)
E4 = lambda: eis(4, 240)
E6 = lambda: eis(6, -504)


def serre(f, k, e2):                             # D_k f = q df/dq - (k/12) E2 f
    return f.qdq() - e2 * f * S.c(F(k) / 12)
F = Fraction
# ---- verbatim: frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py, lines 24-29 (main at 88a1e9474)
th2, th3, th4 = theta2(), theta3(1), theta3(-1)
di = (th2 * th3 * th4).inv()
R = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * S.c(0, 1) * di]
e2, e4, e6 = E2(), E4(), E6()
B = [R, [serre(c, F(-1, 2), e2) for c in R]]
B.append([serre(c, F(3, 2), e2) for c in B[1]])
# ---- verbatim: frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py, lines 102-104 (main at 88a1e9474)
def ev(s, tau):
    x = mp.exp(2j * mp.pi * tau / 8)
    return mp.fsum(mp.mpc(mp.mpf(a.numerator) / a.denominator, mp.mpf(b.numerator) / b.denominator) * x ** kk for kk, (a, b) in s.d.items())
# ---- verbatim: frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction/b1656_funcs.py, lines 19-69 (main at 88a1e9474)
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
BLOCKS = [QJ, QI, QK]                                                        # the generations' blocks (B1644)
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
OM = complex(np.exp(2j*np.pi/3)); GEN = 0.13 + 1.07j

# ---------------------------------------------------------------- route A (numpy)
NK = 24
def thc(a, b, u, T):
    n = np.arange(-NK, NK + 1) + a; u = np.asarray(u, dtype=complex)[..., None]
    return np.sum(np.exp(1j*np.pi*T*n*n + 2j*np.pi*n*(u + b)), -1)
def th1(u, t):
    k = np.arange(-NK, NK + 1); h = k + 0.5; u = np.asarray(u, dtype=complex)[..., None]
    return -1j*np.sum((-1.0)**k*np.exp(1j*np.pi*t*h*h + 1j*np.pi*(2*k + 1)*u), -1)
def bil(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2*t; t1 = th1(u, t)
    den = 1j*np.exp(-1j*np.pi*t/2)*np.exp(-1j*np.pi*u)*t1
    X0, X1, Y0, Y1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T), thc(ay, by, u, T), thc(ay, by, u + t, T)
    return np.array([[X0*Y0/t1, np.exp(1j*np.pi*by)*X0*Y1/den], [np.exp(1j*np.pi*bx)*X1*Y0/den, np.exp(1j*np.pi*(bx + by))*X1*Y1/th1(u + t, t)]])
def pairs(x, y, u, t):
    M = bil(x, y, u, t); return {s: np.einsum('mn,mn...->...', EPS @ C, M) for s, C in UNITS.items()}
def twist_of(w, t): a = w.imag/t.imag; return (a, 2*(w.real - a*t.real))
def line_w(p1, p2, t): return p1*t - p2                                      # W59's holonomy phases (B1653)
def sector_twists(w, t, ql, qr): return twist_of(ql*w, t), twist_of(qr*w, t)
def residues(x, y, t, rad=0.01, N=256):
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t); return {s: complex(np.mean(P[s]*u)) for s in UNITS}
def rmax_np(th, t):
    d = np.exp(1j*th); y1 = d.imag/t.imag; x1 = d.real - y1*t.real; return 0.5/np.maximum(abs(x1), abs(y1))
def vangles(t):
    v = [0.5+0.5*t, -0.5+0.5*t, -0.5-0.5*t, 0.5-0.5*t]
    br = sorted(float(np.mod(np.angle(z), 2*np.pi)) for z in v); return br + [br[0] + 2*np.pi]
def a0_of(x, y, t, R, rad=0.05, N=128):
    """K_s = P_s/R_s = 1/z + a0 + a1 z + ...: a0 = the circle mean of K_s - 1/z"""
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t)
    return {s: (complex(np.mean(P[s]/R[s] - 1/u)) if abs(R[s]) > 1e-12 else None) for s in UNITS}
def cA(x, y, t, R, eps=1e-5, scale=1.0, nth=96, ns=64):
    """the regularised norm: int_{P minus D_eps} |scale K_s|^2 - 2 pi log(1/eps) + scale^2 pi eps^2 |a0|^2 (the disc's
    constant term; the twisted kernels are not odd, so a0 != 0; the next term is O(eps^4))"""
    A0 = a0_of(x, y, t, R)
    br = vangles(t); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = {s: 0.0 for s in UNITS}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        hi = np.log(rmax_np(th, t)); lo = math.log(eps)
        sg = 0.5*(hi-lo)[:, None]*xs[None, :] + 0.5*(hi+lo)[:, None]; w2 = 0.5*(hi-lo)[:, None]*ws[None, :]
        rr = np.exp(sg); z = rr*np.exp(1j*th)[:, None]; P = pairs(x, y, z, t)
        for s in UNITS:
            if abs(R[s]) > 1e-12: tot[s] += np.sum(wt[:, None]*w2*np.abs(scale*P[s]/R[s])**2*rr**2)
    return {s: (float(tot[s] - 2*np.pi*math.log(1/eps) + scale**2*np.pi*eps**2*abs(A0[s])**2) if abs(R[s]) > 1e-12 else None) for s in UNITS}
def nR2(R): return sum(abs(R[s])**2 for s in UNITS)
def D_of(c, R): return sum(c[s]*R[s]**2 for s in UNITS if c[s] is not None)
# ---- verbatim: frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction/b1656_funcs.py, lines 86-86 (main at 88a1e9474)
EC = {s: (EPS @ C) for s, C in UNITS.items()}
# ---- verbatim: frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction/b1656_funcs.py, lines 119-126 (main at 88a1e9474)
# ---------------------------------------------------------------- the coupling with channel weights (B1644, B1653)
def dual_basis():
    G = np.array([[np.sum(EC[t]*UNITS[s]) for s in UNITS] for t in UNITS])                 # pair(E_s := C_s, C_t)
    Gi = np.linalg.inv(G); keys = list(UNITS)
    return {keys[a]: sum(Gi[b, a]*UNITS[keys[b]] for b in range(4)) for a in range(4)}
EDUAL = dual_basis()
def weighted_M(u): return sum(u[s]*EDUAL[s] for s in UNITS)
def coupling(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])

# ---- the embedded objects that cm_zero_line's mods() loads from main's files
mp.mp.dps = 30
_te = types.SimpleNamespace(S=S, e4=e4, B=B, ev=ev)
_b = types.SimpleNamespace(QI=QI, QJ=QJ, QK=QK, EPS=EPS, UNITS=UNITS, line_w=line_w, sector_twists=sector_twists,
                           residues=residues, cA=cA, coupling=coupling, weighted_M=weighted_M)
_COL = [(1.0, 0.686656539476018, 2.7175833387330646), (1.25, 0.6744562322332821, 2.614257322096876), (1.5, 0.6663327737493074, 2.539444130577057), (1.75, 0.6606056670045855, 2.4834439488994198), (2.0, 0.6563962984619787, 2.4404154646430865), (2.25, 0.6532021695652247, 2.406639297403933), (2.5, 0.6507161435099693, 2.3796454106029277), (2.75, 0.6487406629894942, 2.3577376878276057), (3.0, 0.647143395984371, 2.3397188997332714), (3.25, 0.6458327174285687, 2.324724024445286), (3.5, 0.6447434106451755, 2.312115368570467), (3.75, 0.643827954429486, 2.3014144781630703), (4.0, 0.6430510150628824, 2.292256739933974)]
_S_ = _te.S
_Q = {"DR": _te.B[1], "a0": [_te.B[2][j] + _S_.c(F(-1, 48)) * _te.e4 * _te.B[0][j] for j in range(3)], "R": _te.B[0],
      "t=-5/288": [_te.B[2][j] + _S_.c(F(-5, 288)) * _te.e4 * _te.B[0][j] for j in range(3)]}
_M = dict(te=_te, B=_b, col=_COL, Q=_Q)


def mods():
    return _M


# ---- verbatim: frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py, lines 37-82 (main at 88a1e9474)
DIRS = ["DR", "a0", "R", "t=-5/288"] + ["F_%d" % a for a in (-10, -6, -2, 6, 10, 14, 18, 22, 26)]
SECTORS = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]


def direction(name, tau):
    M = mods(); te = M["te"]
    if name in M["Q"]: return [complex(te.ev(c, mp.mpc(tau.real, tau.imag))) for c in M["Q"][name]]
    a_ = int(name[2:]); q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag)); eps = 1j ** ((a_ + 2) // 2)
    th2, th3, th4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return [complex(eps * th2 ** a_), complex(eps * th4 ** a_), complex(1j * th3 ** a_)]


def radii(tau):
    col = mods()["col"]
    return float(np.interp(tau.imag, [c[0] for c in col], [c[1] for c in col])), float(np.interp(tau.imag, [c[0] for c in col], [c[2] for c in col]))


def rows_at(tau, line, Ls=None):
    B = mods()["B"]
    ch = {}
    for sn, ql, qr in SECTORS:
        w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R); ch[sn] = (R, c)
    Lmax, L2 = Ls if Ls else radii(tau)
    out = []
    for d in DIRS:
        a = direction(d, tau)
        for Ln, L in (("L_max", Lmax), ("L_2", L2)):
            for rd in itertools.product((0, 1), repeat=3):
                row = {"direction": d, "radius": Ln, "reading": "".join("S~" if r else "S" for r in rd)}
                U = {}; deg = []
                for (sn, ql, qr), r in zip(SECTORS, rd):
                    R, c = ch[sn]
                    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
                    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
                    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
                    Y = B.coupling(Sm, B.weighted_M(u))
                    u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); s = s[o]; U[sn] = u_[:, o]
                    row[sn] = [float(s[0] / s[2]), float(s[1] / s[2])]
                    if min((s[1] - s[0]) / s[2], (s[2] - s[1]) / s[2]) < 1e-8: deg.append(sn)
                Vm = U["up"].conj().T @ U["down"]
                row["V defined"] = not any(x in deg for x in ("up", "down"))
                row["V"] = [float(abs(Vm[0, 1])), float(abs(Vm[1, 2])), float(abs(Vm[0, 2]))]
                row["J"] = float(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])))
                out.append(row)
    return out


# ---- the rank, as in relations_check.py version 2, part (1)
def outs(tau, line):
    with contextlib.redirect_stdout(io.StringIO()):
        rows = rows_at(tau, line)
    res = {}
    for r in rows:
        a = [r["up"][1], r["up"][0], r["down"][1], r["down"][0], r["lepton"][1], r["lepton"][0], *r["V"]]
        if not r["V defined"] or min(a) <= 1e-300:
            continue
        res[(r["direction"], r["radius"], r["reading"])] = (np.array([math.log(v) for v in a] + [r["J"]]), np.array(a))
    return res


def main():
    print("(1) the rank of the ten in (Re tau, Im tau), per branch")
    h = 1e-5
    LINES1 = [(Fr(1, 7), Fr(2, 7)), (Fr(3, 8), Fr(3, 8)), (Fr(4, 9), Fr(1, 3)), (Fr(2, 5), Fr(1, 10)),
              (Fr(3, 11), Fr(5, 11)), (Fr(1, 12), Fr(0)), (Fr(5, 12), Fr(1, 4)), (Fr(1, 4), Fr(1, 8))]
    allmax = []
    dropped = 0
    for line in LINES1:
        for tau in (complex(0.13, 2.2), complex(0.31, 3.1)):
            o0 = outs(tau, line)
            ox = (outs(tau + h, line), outs(tau - h, line))
            oy = (outs(tau + 1j * h, line), outs(tau - 1j * h, line))
            mx = []
            for k in o0:
                if not all(k in d for d in (*ox, *oy)):
                    continue
                keep = np.array([v > 1e-6 for v in o0[k][1]] + [True])
                dropped += int(not keep.all())
                G = np.stack([(ox[0][k][0] - ox[1][k][0]) / (2 * h), (oy[0][k][0] - oy[1][k][0]) / (2 * h)], 1)[keep]
                n = np.linalg.norm(G, axis=1)
                G = G[n > 1e-8] / n[n > 1e-8][:, None]
                s = max(abs(G[i, 0] * G[j, 1] - G[i, 1] * G[j, 0]) for i in range(len(G)) for j in range(i + 1, len(G)))
                mx.append(s)
            mx = np.array(mx)
            allmax.extend(mx.tolist())
            print("    line (%s, %s), tau %.2f%+.2fi: %3d branches; max |sin| between two kept gradients: median %.3f, "
                  "minimum %.3f, below 0.1: %d" % (line[0], line[1], tau.real, tau.imag, len(mx), np.median(mx), mx.min(),
                                                   int(np.sum(mx < 0.1))))
    allmax = np.array(allmax)
    print("    all: %d branches (%d with an output below 1e-6 dropped); minimum %.3f; below 0.1: %d; below 1e-3: %d"
          % (len(allmax), dropped, allmax.min(), int(np.sum(allmax < 0.1)), int(np.sum(allmax < 1e-3))))
    print("    f(d) = 2 on every branch above:", bool(allmax.min() > 1e-3))


if __name__ == "__main__":
    main()
