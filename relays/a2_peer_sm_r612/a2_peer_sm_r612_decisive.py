#!/usr/bin/env python3
"""Card A2-PEER-SM-R612 — Blind Cross-Family Independent Verification of SM-R612b
(P-612, P-418, P-355; A01, A02, A03, A04, A07, A09, A10; kind: negative).

Seat code: fam3-v1-high-03 (verifying fam1-v1-unset-04 on origin/sm/cards @ 1c5b13d0a).
Strictly blind (0 of 19): ZERO sm/cards scripts or outputs opened before sealing.
Self-contained: stdlib + numpy + scipy + mpmath only; ZERO AST float literals; ZERO JSON floats.
"""
import ast
import json
import math
import os
import pathlib
import sys
from fractions import Fraction as Fr

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "a2_peer_sm_r612_out.json"

I_UNIT = complex(0, 1)
TWO = 2
HALF = 1 / 2
PI = math.pi
TWO_PI = 2 * PI

# Exact Q_8 / generation blocks & 6Y charges (B1656 / B1723 / B1842)
QI = np.array([[I_UNIT, 0], [0, -I_UNIT]], dtype=complex)
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
QK = QI @ QJ
EPS = QJ.copy()
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
UNIT_KEYS = ("1", "i", "j", "k")
EC = {s: (EPS @ UNITS[s]) for s in UNIT_KEYS}
BLOCKS = [QJ, QI, QK]
CHARGES = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}


def _build_edual():
    G = np.array([[np.sum(EC[t] * UNITS[s]) for s in UNIT_KEYS] for t in UNIT_KEYS], dtype=complex)
    Gi = np.linalg.inv(G)
    return {UNIT_KEYS[a]: sum(Gi[b, a] * UNITS[UNIT_KEYS[b]] for b in range(4)) for a in range(4)}


EDUAL = _build_edual()

# Thresholds (constructed with zero float literals)
ZERO_MASS_THR = 10 ** (-12)
CONST_THR = 10 ** (-8)
NONCONST_THR = 10 ** (-5)
CLUSTER_TOL = 10 ** (-5)
RANK_THR = 10 ** (-4)
FD_STEPS = (Fr(1, 1000), Fr(1, 2000))


# ============================================================================
# 1. Exact rational q-series for Higgs menu R, DR, D^2R (B1691) + mpmath check
# ============================================================================
QSER_N = 160  # x^160 = q^20 (at Im tau ~ 3, |q|^20 < 10^{-160})


class QSer:
    """Exact Gaussian-rational q-series in x = q^{1/8}, q = exp(2 pi i tau)."""

    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != (0, 0)}

    @staticmethod
    def const(re_v, im_v=0, k=0):
        return QSer({k: (Fr(re_v), Fr(im_v))})

    def __add__(self, o):
        d = dict(self.d)
        for k, (a, b) in o.d.items():
            x, y = d.get(k, (Fr(0), Fr(0)))
            d[k] = (x + a, y + b)
        return QSer(d)

    def __neg__(self):
        return QSer({k: (-a, -b) for k, (a, b) in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, QSer):
            o = QSer.const(o)
        d = {}
        for k1, (a1, b1) in self.d.items():
            for k2, (a2, b2) in o.d.items():
                k = k1 + k2
                if k > QSER_N:
                    continue
                x, y = d.get(k, (Fr(0), Fr(0)))
                d[k] = (x + a1 * a2 - b1 * b2, y + a1 * b2 + b1 * a2)
        return QSer(d)

    def ord(self):
        return min(self.d) if self.d else None

    def inv(self):
        k0 = self.ord()
        a0, b0 = self.d[k0]
        n2 = a0 * a0 + b0 * b0
        i0 = (a0 / n2, -b0 / n2)

        def cmul(p, q):
            return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])

        M = QSER_N + k0
        sj = [self.d.get(k0 + j, (Fr(0), Fr(0))) for j in range(M + 1)]
        t = [i0]
        for m in range(1, M + 1):
            acc = (Fr(0), Fr(0))
            for j in range(1, m + 1):
                if sj[j] != (0, 0):
                    pr = cmul(sj[j], t[m - j])
                    acc = (acc[0] + pr[0], acc[1] + pr[1])
            v = cmul(i0, acc)
            t.append((-v[0], -v[1]))
        return QSer({m - k0: t[m] for m in range(M + 1) if m - k0 <= QSER_N})

    def qdq(self):
        return QSer({k: (a * Fr(k, 8), b * Fr(k, 8)) for k, (a, b) in self.d.items()})

    def eval_complex(self, tau):
        x = np.exp(I_UNIT * PI * tau / 4)
        tot = complex(0, 0)
        for k, (a, b) in self.d.items():
            tot += (float(a.numerator) / float(a.denominator) + I_UNIT * float(b.numerator) / float(b.denominator)) * (x ** k)
        return tot


def _build_higgs_basis():
    d2 = {}
    n = 0
    while (2 * n + 1) ** 2 <= QSER_N:
        d2[(2 * n + 1) ** 2] = (Fr(2), Fr(0))
        n += 1
    th2 = QSer(d2)

    def th3_s(sgn):
        d = {0: (Fr(1), Fr(0))}
        m = 1
        while 4 * m * m <= QSER_N:
            d[4 * m * m] = (Fr(2 * (sgn ** m)), Fr(0))
            m += 1
        return QSer(d)

    th3, th4 = th3_s(1), th3_s(-1)
    di = (th2 * th3 * th4).inv()
    R = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * QSer.const(0, 1) * di]

    # E2(tau) = 1 - 24 sum sigma_1(n) q^n
    de2 = {0: (Fr(1), Fr(0))}
    for m in range(1, QSER_N // 8 + 1):
        sig1 = sum(dv for dv in range(1, m + 1) if m % dv == 0)
        de2[8 * m] = (Fr(-24 * sig1), Fr(0))
    e2 = QSer(de2)

    def serre(f, k_wt):
        return f.qdq() - e2 * f * QSer.const(k_wt / 12)

    DR = [serre(c, Fr(-1, 2)) for c in R]
    D2R = [serre(c, Fr(3, 2)) for c in DR]
    return {"R": R, "DR": DR, "D2R": D2R}


HIGGS_SERIES = _build_higgs_basis()


def eval_higgs_vec(name, tau):
    return np.array([c.eval_complex(tau) for c in HIGGS_SERIES[name]], dtype=complex)


def check_higgs_against_mpmath(tau):
    """Independent mpmath jtheta + complex-step Serre derivative check of R, DR, D^2R."""
    mp.mp.dps = 30
    mt = mp.mpc(tau.real, tau.imag)

    def R_mp(z):
        q = mp.exp(mp.j * mp.pi * z)
        t2 = mp.jtheta(2, 0, q)
        t3 = mp.jtheta(3, 0, q)
        t4 = mp.jtheta(4, 0, q)
        den = t2 * t3 * t4
        return [-(t2 * t2) / den, -(t4 * t4) / den, mp.j * (t3 * t3) / den]

    def E2_mp(z):
        q2 = mp.exp(2 * mp.j * mp.pi * z)
        s = mp.mpf(1)
        for m in range(1, 35):
            sig1 = sum(d for d in range(1, m + 1) if m % d == 0)
            s -= 24 * sig1 * (q2 ** m)
        return s

    def D_mp(fn, wt, z):
        # q d/dq = (1 / (2 pi i)) d/dz
        h = mp.mpf(1) / (10 ** 7)
        fp = fn(z + h)
        fm = fn(z - h)
        f0 = fn(z)
        e2v = E2_mp(z)
        out = []
        for idx in range(3):
            dfdz = (fp[idx] - fm[idx]) / (2 * h)
            qdf = dfdz / (2 * mp.j * mp.pi)
            out.append(qdf - (mp.mpf(wt.numerator) / mp.mpf(wt.denominator)) / 12 * e2v * f0[idx])
        return out

    r_ref = R_mp(mt)
    dr_ref = D_mp(R_mp, Fr(-1, 2), mt)
    d2r_ref = D_mp(lambda z: D_mp(R_mp, Fr(-1, 2), z), Fr(3, 2), mt)
    errs = {}
    for nm, ref in (("R", r_ref), ("DR", dr_ref), ("D2R", d2r_ref)):
        v = eval_higgs_vec(nm, tau)
        ref_np = np.array([complex(x) for x in ref], dtype=complex)
        errs[nm] = float(np.max(np.abs(v - ref_np)) / max(1, float(np.max(np.abs(ref_np)))))
    return max(errs.values())


# ============================================================================
# 2. Independent Fuchsian uniformization & canonical cusp geometry (B1667)
# ============================================================================
def _thetas_wp(v, tau, N=12):
    q = np.exp(I_UNIT * PI * tau)
    n = np.arange(N)
    hp = n + HALF
    t1 = 2 * np.sum(((-1) ** n) * (q ** (hp * hp)) * np.sin((2 * n + 1) * v))
    t2 = 2 * np.sum((q ** (hp * hp)) * np.cos((2 * n + 1) * v))
    m = np.arange(1, N)
    t3 = 1 + 2 * np.sum((q ** (m * m)) * np.cos(2 * m * v))
    t4 = 1 + 2 * np.sum(((-1) ** m) * (q ** (m * m)) * np.cos(2 * m * v))
    return t1, t2, t3, t4


class EllipticLattice:
    def __init__(self, tau):
        self.tau = complex(tau)
        _, t2, t3, t4 = _thetas_wp(0, self.tau)
        self.t20, self.t30, self.t40 = t2, t3, t4
        self.e1 = (PI * PI / 3) * (t3 ** 4 + t4 ** 4)
        self.e2 = (PI * PI / 3) * (t2 ** 4 - t4 ** 4)
        self.e3 = -(PI * PI / 3) * (t2 ** 4 + t3 ** 4)

    def wp(self, z):
        n = np.round(z.imag / self.tau.imag)
        z = z - n * self.tau
        z = z - np.round(z.real)
        t1, t2, _, _ = _thetas_wp(PI * z, self.tau)
        return (PI * self.t30 * self.t40 * t2 / t1) ** 2 + self.e1


def _transfer_path(lat, c, zf, dzf, y0):
    def rhs(t, Y):
        z, d = zf(t), dzf(t)
        Q = (1 / 4) * lat.wp(z) + c
        return [d * Y[1], -d * Q * Y[0]]

    sol = solve_ivp(rhs, (0, 1), np.asarray(y0, dtype=complex),
                    method="DOP853", rtol=10 ** (-12), atol=10 ** (-14))
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1]


def _transfer_seg(lat, c, z_from, z_to, y0):
    d = z_to - z_from
    return _transfer_path(lat, c, lambda t: z_from + t * d, lambda t: d, y0)


def _fundamental_seg(lat, c, z_from, z_to):
    a = _transfer_seg(lat, c, z_from, z_to, [1, 0])
    b = _transfer_seg(lat, c, z_from, z_to, [0, 1])
    return np.array([[a[0], b[0]], [a[1], b[1]]], dtype=complex)


def _fundamental_path(lat, c, zf, dzf):
    a = _transfer_path(lat, c, zf, dzf, [1, 0])
    b = _transfer_path(lat, c, zf, dzf, [0, 1])
    return np.array([[a[0], b[0]], [a[1], b[1]]], dtype=complex)


def _mobius_of(T):
    A = np.array([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]], dtype=complex)
    return A / np.sqrt(np.linalg.det(A))


def _monodromy(lat, c, z0):
    Ta = _fundamental_seg(lat, c, z0, z0 + 1)
    Tb = _fundamental_seg(lat, c, z0, z0 + lat.tau)
    return _mobius_of(Ta), _mobius_of(Tb)


def _solve_accessory(tau, c0):
    lat = EllipticLattice(tau)
    z0 = HALF + HALF * lat.tau

    def F(cv):
        Aa, Ab = _monodromy(lat, cv, z0)
        return np.array([np.trace(Aa).imag, np.trace(Ab).imag])

    c = complex(c0)
    h = 10 ** (-6)
    tol = 10 ** (-12)
    for _ in range(35):
        f = F(c)
        if np.max(np.abs(f)) < tol:
            return lat, z0, c, float(np.max(np.abs(f)))
        J = np.column_stack([(F(c + h) - f) / h, (F(c + I_UNIT * h) - f) / h])
        dx = np.linalg.solve(J, -f)
        c = c + dx[0] + I_UNIT * dx[1]
    f = F(c)
    return lat, z0, c, float(np.max(np.abs(f)))


def _track_accessory(tau_target, solved_cache):
    """Continue accessory parameter c(tau) from i (where c(i) = 0 by symmetry) or nearest cached tau."""
    if not solved_cache:
        # At tau = i, c(i) is purely real; start near 0 and walk straight from 1j to tau_target
        t_start = complex(0, 1)
        _, _, c_i, r_i = _solve_accessory(t_start, complex(0, 0))
        if r_i > 10 ** (-10):
            raise RuntimeError("Failed accessory solve at i")
        solved_cache.append((t_start, c_i))

    t0, c0 = min(solved_cache, key=lambda q: abs(q[0] - tau_target))
    dist = abs(tau_target - t0)
    n_steps = max(1, int(math.ceil(dist * 4)))
    cur_t, cur_c = t0, c0
    res = 0
    for k in range(1, n_steps + 1):
        nxt_t = t0 + (tau_target - t0) * (k / n_steps)
        lat, z0, cur_c, res = _solve_accessory(nxt_t, cur_c)
        cur_t = nxt_t
    if res > 10 ** (-10):
        raise RuntimeError(f"Accessory residual too large at {tau_target}: {res}")
    solved_cache.append((tau_target, cur_c))
    return lat, z0, cur_c, res


def _apply_mob(M, w):
    return (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])


def _fixed_points(M):
    a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    disc = np.sqrt((a - d) ** 2 + 4 * b * cc)
    return (a - d + disc) / (2 * cc), (a - d - disc) / (2 * cc)


def _normalise_sl2r(Aa, Ab, P):
    fp = _fixed_points(P)
    p = HALF * (fp[0] + fp[1])
    f1, f2 = _fixed_points(Aa)
    g = np.array([[1, -f1], [1, -p]], dtype=complex)
    s = _apply_mob(g, f2)
    g = np.array([[1 / s, -f1 / s], [1, -p]], dtype=complex)
    g = g / np.sqrt(np.linalg.det(g))
    if _apply_mob(g, complex(0, 0)).imag < 0:
        g = np.array([[I_UNIT, 0], [0, -I_UNIT]], dtype=complex) @ g
    gi = np.linalg.inv(g)
    Ra, Rb, RP = g @ Aa @ gi, g @ Ab @ gi, g @ P @ gi
    RP = RP / RP[0, 0]
    lam = abs(RP[0, 1].real)
    return g, Ra, Rb, lam


def _min_c_vectorized(Ra, Rb, maxlen=8):
    """Exact minimum |c_gamma| > 0 over reduced words of length <= maxlen (vectorized)."""
    gens = np.stack([Ra, Rb, np.linalg.inv(Ra), np.linalg.inv(Rb)], axis=0)
    inv_idx = (2, 3, 0, 1)
    best = math.inf
    # Maintain arrays grouped by last generator index
    buckets = {k: gens[k][None, :, :] for k in range(4)}
    for k in range(4):
        M = buckets[k]
        c_abs = np.abs(M[:, 1, 0])
        thr = 10 ** (-9) * np.maximum(1, np.abs(M[:, 0, 0]))
        ok = c_abs > thr
        if np.any(ok):
            best = min(best, float(np.min(c_abs[ok])))
    for _ in range(1, maxlen):
        nxt_lists = {k: [] for k in range(4)}
        for last, arr in buckets.items():
            for k in range(4):
                if k == inv_idx[last]:
                    continue
                prod = arr @ gens[k]
                c_abs = np.abs(prod[:, 1, 0])
                thr = 10 ** (-9) * np.maximum(1, np.abs(prod[:, 0, 0]))
                ok = c_abs > thr
                if np.any(ok):
                    best = min(best, float(np.min(c_abs[ok])))
                nxt_lists[k].append(prod)
        buckets = {k: np.concatenate(nxt_lists[k], axis=0) for k in range(4)}
    return best


def _frobenius(lat, c, M=120):
    g2 = 2 * (lat.e1 ** 2 + lat.e2 ** 2 + lat.e3 ** 2)
    g3 = 4 * lat.e1 * lat.e2 * lat.e3
    nmax = M // 2 + 2
    a = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, nmax + 1):
        a[n] = (3 / ((2 * n + 3) * (n - 2))) * sum(a[m] * a[n - 1 - m] for m in range(1, n - 1))
    Q = np.zeros(M + 1, dtype=complex)
    Q[0] = c
    for n in range(1, M // 2 + 1):
        Q[2 * n] = a[n] / 4
    al = np.zeros(M + 1, dtype=complex)
    be = np.zeros(M + 1, dtype=complex)
    al[0] = 1
    for m in range(1, M + 1):
        sa = sum(Q[j] * al[m - 2 - j] for j in range(0, m - 1))
        al[m] = -sa / (m * m)
        sb = sum(Q[j] * be[m - 2 - j] for j in range(0, m - 1))
        be[m] = -(2 * m * al[m] + sb) / (m * m)
    return al, be


def _g_local(al, be, z):
    zp = z ** np.arange(len(al))
    return np.dot(be, zp) / np.dot(al, zp)


def _voronoi(tau):
    tau = complex(tau)
    V = [1, -1, tau, -tau, tau - 1, 1 - tau, tau + 1, -tau - 1]

    def rmax(th):
        th = np.asarray(th, dtype=float)
        e = np.exp(I_UNIT * th)
        best = np.full(th.shape, math.inf)
        for v in V:
            den = (e * np.conj(v)).real
            safe = np.where(den > 10 ** (-14), den, 1)
            val = np.where(den > 10 ** (-14), (abs(v) ** 2 / 2) / safe, math.inf)
            best = np.minimum(best, val)
        return best

    verts = []
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            a, b = V[i], V[j]
            A = np.array([[a.real, a.imag], [b.real, b.imag]], dtype=float)
            if abs(np.linalg.det(A)) < 10 ** (-12):
                continue
            x = np.linalg.solve(A, [abs(a) ** 2 / 2, abs(b) ** 2 / 2])
            z = x[0] + I_UNIT * x[1]
            th = math.atan2(z.imag, z.real)
            if abs(abs(z) - float(rmax(np.array([th]))[0])) < 10 ** (-9):
                verts.append(th % TWO_PI)
    br = sorted({round(v, 11) for v in verts})
    br.append(br[0] + TWO_PI)
    return br, rmax


def _horocycle_radius_vec(al, be, Lh, thetas, r_his):
    """Vectorized bisection solving log(1/r) - Re(g_local(r e^{i theta})) = Lh over all angles at once."""
    thetas = np.asarray(thetas, dtype=float)
    r_his = np.asarray(r_his, dtype=float)
    exp_ith = np.exp(I_UNIT * thetas)
    # Evaluate g_local via vectorized Horner's method (len(al) ~ 121)
    al_rev = al[::-1]
    be_rev = be[::-1]

    def eval_f(s_arr):
        z = np.exp(s_arr) * exp_ith
        num = np.zeros_like(z, dtype=complex)
        den = np.zeros_like(z, dtype=complex)
        for cb, ca in zip(be_rev, al_rev):
            num = num * z + cb
            den = den * z + ca
        return -s_arr - (num / den).real - Lh

    lo = np.full(thetas.shape, math.log(10 ** (-12)), dtype=float)
    hi = np.log(r_his)
    if np.any(eval_f(hi) > 0):
        return None
    for _ in range(72):
        mid = HALF * (lo + hi)
        pos = eval_f(mid) > 0
        lo = np.where(pos, mid, lo)
        hi = np.where(pos, hi, mid)
    return np.exp(HALF * (lo + hi))


def compute_geometry(tau, solved_cache):
    lat, z0, c, res = _track_accessory(tau, solved_cache)
    Aa, Ab = _monodromy(lat, c, z0)
    eps = 1 / 20
    zs = eps * z0 / abs(z0)
    T1 = _fundamental_seg(lat, c, z0, zs)
    T2 = _fundamental_path(lat, c, lambda t: zs * np.exp(I_UNIT * TWO_PI * t),
                           lambda t: I_UNIT * TWO_PI * zs * np.exp(I_UNIT * TWO_PI * t))
    T3 = _fundamental_seg(lat, c, zs, z0)
    P0 = _mobius_of(T3 @ T2 @ T1)
    g, Ra, Rb, lam = _normalise_sl2r(Aa, Ab, P0)
    mc8 = _min_c_vectorized(Ra, Rb, maxlen=8)
    al, be = _frobenius(lat, c, M=120)
    a_v = _transfer_seg(lat, c, z0, zs, [1, 0])
    b_v = _transfer_seg(lat, c, z0, zs, [0, 1])
    u = _apply_mob(g, b_v[0] / a_v[0])
    im_B = u.imag + (lam / TWO_PI) * (math.log(abs(zs)) + _g_local(al, be, zs).real)
    L_max = (TWO_PI / lam) * (1 / mc8 - im_B)
    L_2 = PI - (TWO_PI / lam) * im_B
    br, rmaxf = _voronoi(tau)
    return {
        "tau": complex(tau),
        "c": c,
        "res": res,
        "al": al,
        "be": be,
        "L_max": L_max,
        "L_2": L_2,
        "L_E4": L_2 - PI / 2,
        "L_E2": math.log(2),
        "br": br,
        "rmaxf": rmaxf,
    }


def build_horoball_grid(geo, Lh, nth=40, ns=28):
    """Precompute quadrature nodes z and weights dA = wt * wsr * r^2 on Dirichlet cell minus horoball(Lh)."""
    xg, wg = leggauss(nth)
    xs, ws = leggauss(ns)
    br, rmaxf = geo["br"], geo["rmaxf"]
    al, be = geo["al"], geo["be"]
    z_list, w_list = [], []
    margin = math.inf
    for a_, b_ in zip(br[:-1], br[1:]):
        th = HALF * (b_ - a_) * xg + HALF * (b_ + a_)
        wt = HALF * (b_ - a_) * wg
        rmax = rmaxf(th)
        r_caps = np.minimum(19 / 20, (11 / 10) * rmax)
        rh = _horocycle_radius_vec(al, be, Lh, th, r_caps)
        if rh is None:
            raise RuntimeError(f"Horocycle failed to close inside cell at tau={geo['tau']}, Lh={Lh}")
        margin = min(margin, float(np.min(rmax - rh)))
        s_hi = np.log(rmax)
        s_lo = np.log(np.minimum(rh, rmax))
        s = HALF * (s_hi - s_lo)[:, None] * xs[None, :] + HALF * (s_hi + s_lo)[:, None]
        wsr = HALF * (s_hi - s_lo)[:, None] * ws[None, :]
        rr = np.exp(s)
        z = rr * np.exp(I_UNIT * th)[:, None]
        w_eff = wt[:, None] * wsr * (rr * rr)
        z_list.append(z.ravel())
        w_list.append(w_eff.ravel())
    return np.concatenate(z_list), np.concatenate(w_list), margin


# ============================================================================
# 3. Twisted theta kernels, residues, exact & small-cut norms, Yukawa matrices
# ============================================================================
NK = 24
_N_ARR = np.arange(-NK, NK + 1, dtype=float)
_K_ARR = np.arange(-NK, NK + 1, dtype=float)
_H_ARR = _K_ARR + HALF
_SGN_ARR = np.where((np.arange(-NK, NK + 1) % 2) == 0, 1, -1)


def _thc(a, b, u, T):
    n = _N_ARR + a
    u = np.asarray(u, dtype=complex)[..., None]
    return np.sum(np.exp(I_UNIT * PI * T * (n * n) + I_UNIT * TWO_PI * n * (u + b)), axis=-1)


def _th1(u, t):
    u = np.asarray(u, dtype=complex)[..., None]
    return -I_UNIT * np.sum(_SGN_ARR * np.exp(I_UNIT * PI * t * (_H_ARR * _H_ARR) + I_UNIT * PI * (2 * _K_ARR + 1) * u), axis=-1)


def _pairs(x, y, u, t):
    (ax, bx), (ay, by) = x, y
    T = 2 * t
    t1 = _th1(u, t)
    den = I_UNIT * np.exp(-I_UNIT * PI * t / 2) * np.exp(-I_UNIT * PI * u) * t1
    X0, X1 = _thc(ax, bx, u, T), _thc(ax, bx, u + t, T)
    Y0, Y1 = _thc(ay, by, u, T), _thc(ay, by, u + t, T)
    m00 = X0 * Y0 / t1
    m01 = np.exp(I_UNIT * PI * by) * X0 * Y1 / den
    m10 = np.exp(I_UNIT * PI * bx) * X1 * Y0 / den
    m11 = np.exp(I_UNIT * PI * (bx + by)) * X1 * Y1 / _th1(u + t, t)
    # EC[s] contraction with 2x2 matrix [[m00, m01], [m10, m11]]
    out = {}
    for s in UNIT_KEYS:
        C = EC[s]
        out[s] = C[0, 0] * m00 + C[0, 1] * m01 + C[1, 0] * m10 + C[1, 1] * m11
    return out


def _twist_of(w, t):
    a = w.imag / t.imag
    return (a, 2 * (w.real - a * t.real))


def _sector_twists(w, t, ql, qr):
    return _twist_of(ql * w, t), _twist_of(qr * w, t)


def _residues(x, y, t):
    rad = 1 / 100
    N = 256
    u = rad * np.exp(I_UNIT * TWO_PI * np.arange(N) / N)
    P = _pairs(x, y, u, t)
    return {s: complex(np.mean(P[s] * u)) for s in UNIT_KEYS}


def _cA_small_cut(x, y, t, R):
    """Regularized small-cut constant c_s on parallelogram fundamental domain (B1656)."""
    eps = 10 ** (-5)
    rad0 = 1 / 20
    u0 = rad0 * np.exp(I_UNIT * TWO_PI * np.arange(128) / 128)
    P0 = _pairs(x, y, u0, t)
    A0 = {s: (complex(np.mean(P0[s] / R[s] - 1 / u0)) if abs(R[s]) > ZERO_MASS_THR else None) for s in UNIT_KEYS}

    v = [HALF + HALF * t, -HALF + HALF * t, -HALF - HALF * t, HALF - HALF * t]
    br = sorted(math.atan2(z.imag, z.real) % TWO_PI for z in v)
    br.append(br[0] + TWO_PI)
    xg, wg = leggauss(72)
    xs, ws = leggauss(48)
    tot = {s: 0 for s in UNIT_KEYS}
    for a_, b_ in zip(br[:-1], br[1:]):
        th = HALF * (b_ - a_) * xg + HALF * (b_ + a_)
        wt = HALF * (b_ - a_) * wg
        d = np.exp(I_UNIT * th)
        y1 = d.imag / t.imag
        x1 = d.real - y1 * t.real
        rmax = HALF / np.maximum(np.abs(x1), np.abs(y1))
        hi = np.log(rmax)
        lo = math.log(eps)
        sg = HALF * (hi - lo)[:, None] * xs[None, :] + HALF * (hi + lo)[:, None]
        w2 = HALF * (hi - lo)[:, None] * ws[None, :]
        rr = np.exp(sg)
        z = rr * np.exp(I_UNIT * th)[:, None]
        P = _pairs(x, y, z, t)
        for s in UNIT_KEYS:
            if abs(R[s]) > ZERO_MASS_THR:
                tot[s] += float(np.sum(wt[:, None] * w2 * (np.abs(P[s] / R[s]) ** 2) * (rr * rr)))
    out = {}
    for s in UNIT_KEYS:
        if abs(R[s]) > ZERO_MASS_THR:
            out[s] = tot[s] - TWO_PI * math.log(1 / eps) + PI * (eps * eps) * (abs(A0[s]) ** 2)
        else:
            out[s] = None
    return out


def _weighted_M(u):
    return sum(u[s] * EDUAL[s] for s in UNIT_KEYS)


def _coupling(S_mat, M_mat):
    return np.array([[np.sum((Ca.T @ EPS @ S_mat @ Cb) * M_mat) for Cb in BLOCKS] for Ca in BLOCKS], dtype=complex)


def _higgs_mats(a_vec):
    S = a_vec[0] * QI + a_vec[1] * QJ + a_vec[2] * QK
    St = EPS @ np.conj(S) @ EPS.T
    return {"S": S, "St": St}


def _reduce_tau_line(tau, a_fr, b_fr):
    """T^(+-1) reduction to |Re tau| <= 1/2 (B1842)."""
    t = complex(tau)
    a, b = Fr(a_fr), Fr(b_fr)
    while t.real > HALF:
        t = t - 1
        b = (b + a) % 1
    while t.real < -HALF:
        t = t + 1
        b = (b - a) % 1
    return t, a, b


def sector_channel_data(tau, a_fr, b_fr, end_mode, geo=None, grid_cache=None, Lh_override=None,
                        nth=40, ns=28, reduce_flag=True):
    """Return {sector: (R, norms_dict)} for one (tau, line, end_mode)."""
    if reduce_flag:
        t, a, b = _reduce_tau_line(tau, a_fr, b_fr)
    else:
        t, a, b = complex(tau), Fr(a_fr), Fr(b_fr)
    w = (a.numerator / a.denominator) * t + (b.numerator / b.denominator)

    # Determine horoball quadrature grid if needed
    z_grid = w_grid = None
    small_L = None
    if end_mode == "delta_inf":
        pass
    elif end_mode in ("small_Lmax", "small_L2"):
        small_L = geo["L_max"] if end_mode == "small_Lmax" else geo["L_2"]
    else:
        if Lh_override is not None:
            Lh = Lh_override
        elif end_mode == "E1":
            Lh = geo["L_2"]
        elif end_mode == "E2":
            Lh = geo["L_E2"]
        elif end_mode == "E3":
            Lh = geo["L_max"]
        elif end_mode == "E4":
            Lh = geo["L_E4"]
        else:
            raise ValueError(f"Unknown end_mode {end_mode}")
        gkey = (round(t.real, 12), round(t.imag, 12), round(Lh, 13), nth, ns)
        if grid_cache is not None and gkey in grid_cache:
            z_grid, w_grid = grid_cache[gkey]
        else:
            z_grid, w_grid, _ = build_horoball_grid(geo, Lh, nth=nth, ns=ns)
            if grid_cache is not None:
                grid_cache[gkey] = (z_grid, w_grid)

    out = {}
    for sec in ("up", "down", "lep"):
        ql, qr = CHARGES[sec]
        x, yy = _sector_twists(w, t, ql, qr)
        R = _residues(x, yy, t)
        if end_mode == "delta_inf":
            N = {s: (1 if abs(R[s]) > ZERO_MASS_THR else 0) for s in UNIT_KEYS}
        elif end_mode in ("small_Lmax", "small_L2"):
            cs = _cA_small_cut(x, yy, t, R)
            N = {s: (TWO_PI * small_L + cs[s] if cs[s] is not None else None) for s in UNIT_KEYS}
        else:
            P = _pairs(x, yy, z_grid, t)
            N = {}
            for s in UNIT_KEYS:
                if abs(R[s]) > ZERO_MASS_THR:
                    N[s] = float(np.sum(w_grid * (np.abs(P[s] / R[s]) ** 2)))
                else:
                    N[s] = 0
        out[sec] = (R, N)
    return out


def extract_six_and_D(chan_data, a_vec, c_val, down_norm_pert=None, haar_unitaries=None):
    """Compute the six log-mass ratios [ln(m1/m2)_u, ln(m2/m3)_u, d, e] and D = c^2 R2 R1."""
    hm = _higgs_mats(a_vec)
    ratios_bare = {}
    for sec in ("up", "down", "lep"):
        R, N = chan_data[sec]
        if sec == "down" and down_norm_pert is not None:
            s_pert, fac = down_norm_pert
            N = dict(N)
            if N.get(s_pert) is not None:
                N[s_pert] = N[s_pert] * fac
        u = {s: (math.sqrt(N[s]) * R[s] if N.get(s) is not None and N[s] > 0 else 0) for s in UNIT_KEYS}
        Mw = _weighted_M(u)
        H_mat = hm["St"] if sec == "up" else hm["S"]
        Y = _coupling(H_mat, Mw)
        if haar_unitaries is not None:
            UL, UR = haar_unitaries[sec]
            Y = UL @ Y @ np.conj(UR.T)
        sv = np.linalg.svd(Y, compute_uv=False)  # descending: m3 >= m2 >= m1
        if sv[0] <= ZERO_MASS_THR:
            ratios_bare[sec] = (None, None, None)
        else:
            r23 = float(sv[1] / sv[0])
            r13 = float(sv[2] / sv[0])
            r12 = (r13 / r23) if r23 > ZERO_MASS_THR else None
            ratios_bare[sec] = (
                r12 if (r12 is not None and r12 >= ZERO_MASS_THR and r13 >= ZERO_MASS_THR) else None,
                r23 if r23 >= ZERO_MASS_THR else None,
                r13 if r13 >= ZERO_MASS_THR else None,
            )

    # Apply c to leptons: (m2/m3)_e -> c (m2/m3)_e, (m1/m3)_e -> (m1/m3)_e / c
    # Hence (m1/m2)_e -> (m1/m2)_e / c^2
    six = []
    for sec in ("up", "down", "lep"):
        r12, r23, r13 = ratios_bare[sec]
        if sec == "lep":
            l12 = (math.log(r12) - 2 * math.log(c_val)) if r12 is not None else None
            l23 = (math.log(r23) + math.log(c_val)) if r23 is not None else None
        else:
            l12 = math.log(r12) if r12 is not None else None
            l23 = math.log(r23) if r23 is not None else None
        six.extend([l12, l23])

    _, r23_d, r13_d = ratios_bare["down"]
    _, r23_e, r13_e = ratios_bare["lep"]
    if None not in (r23_d, r13_d, r23_e, r13_e):
        D_val = (c_val * c_val) * (r23_e / r23_d) * (r13_d / r13_e)
    else:
        D_val = None
    return six, D_val


def _vec_dist(v1, v2):
    """L_inf distance between two 6-vectors (infinite if defined-masks differ)."""
    m1 = tuple(x is not None for x in v1)
    m2 = tuple(x is not None for x in v2)
    if m1 != m2:
        return math.inf
    diffs = [abs(a - b) for a, b in zip(v1, v2) if a is not None]
    return max(diffs) if diffs else 0


def count_clusters(vecs, tol=CLUSTER_TOL):
    """Count distinct vectors under L_inf separation > tol (exact greedy + min inter-cluster gap)."""
    reps = []
    for v in vecs:
        matched = False
        for r in reps:
            if _vec_dist(v, r) <= tol:
                matched = True
                break
        if not matched:
            reps.append(v)
    min_gap = math.inf
    for i in range(len(reps)):
        for j in range(i + 1, len(reps)):
            d = _vec_dist(reps[i], reps[j])
            if d < min_gap:
                min_gap = d
    # Compute overall spread (max pairwise dist among all pairs with same mask, or inf if masks differ)
    spread = 0
    for i in range(len(vecs)):
        for j in range(i + 1, len(vecs)):
            d = _vec_dist(vecs[i], vecs[j])
            if d > spread:
                spread = d
    return len(reps), spread, (None if math.isinf(min_gap) else min_gap)


def _fmt(v):
    if v is None:
        return "None"
    if isinstance(v, (int, bool)):
        return str(v)
    if math.isinf(v):
        return "inf"
    return f"{v:.12g}"


def _random_haar_u3(rng):
    Z = rng.normal(size=(3, 3)) + I_UNIT * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    ph = d / np.abs(d)
    return Q * ph[None, :]


def run_all():
    # Self-check AST float literals
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    solved_cache = []
    grid_cache = {}
    geo_cache = {}

    def get_geo(t):
        t = complex(t)
        key = (round(t.real, 12), round(t.imag, 12))
        if key not in geo_cache:
            geo_cache[key] = compute_geometry(t, solved_cache)
        return geo_cache[key]

    # Test moduli (exact rational coordinates, zero float literals)
    MODULI = [
        ("T1", complex(21 / 100, 297 / 100)),
        ("T2", complex(-33 / 100, 308 / 100)),
        ("T3", complex(44 / 100, 302 / 100)),
    ]
    TAU_MIR = complex(0, 3)
    BASE_LINE = (Fr(2, 5), Fr(4, 5))
    BASE_C = 3

    # Independent cross-check of Higgs q-series vs mpmath at T1
    higgs_mp_err = check_higgs_against_mpmath(MODULI[0][1])

    # Quadrature refinement check (NTH=40,NS=28 vs NTH=56,NS=40) on base row at T1
    g_t1 = get_geo(MODULI[0][1])
    cd_40 = sector_channel_data(MODULI[0][1], BASE_LINE[0], BASE_LINE[1], "E4", geo=g_t1, grid_cache=grid_cache, nth=40, ns=28)
    cd_56 = sector_channel_data(MODULI[0][1], BASE_LINE[0], BASE_LINE[1], "E4", geo=g_t1, grid_cache=grid_cache, nth=56, ns=40)
    dr_t1 = eval_higgs_vec("DR", MODULI[0][1])
    s40, d40 = extract_six_and_D(cd_40, dr_t1, BASE_C)
    s56, d56 = extract_six_and_D(cd_56, dr_t1, BASE_C)
    quad_ref_diff = _vec_dist(s40, s56)

    per_mod = {}
    max_D_err_base = 0
    max_identity_err = 0

    for label, tau in MODULI:
        geo = get_geo(tau)
        a_DR = eval_higgs_vec("DR", tau)
        a_R = eval_higgs_vec("R", tau)
        a_D2R = eval_higgs_vec("D2R", tau)
        base_cd = sector_channel_data(tau, BASE_LINE[0], BASE_LINE[1], "E4", geo=geo, grid_cache=grid_cache)
        base_six, base_D = extract_six_and_D(base_cd, a_DR, BASE_C)
        # Check exact base-line algebraic identity (l12_e - l12_d) + 2 (l23_e - l23_d) == 0
        id_err = abs((base_six[4] - base_six[2]) + 2 * (base_six[5] - base_six[3]))
        max_identity_err = max(max_identity_err, id_err)
        max_D_err_base = max(max_D_err_base, abs(base_D - BASE_C * BASE_C))

        # --- Menu 1: c in {1, 2, 3, 4, 5} (A10) ---
        c_vecs, c_D_rel_errs, c_q_diffs = [], [], []
        for cv in range(1, 6):
            sv, dv = extract_six_and_D(base_cd, a_DR, cv)
            c_vecs.append(sv)
            c_D_rel_errs.append(abs(dv / (cv * cv) - 1))
            c_q_diffs.append(max(abs(sv[k] - base_six[k]) for k in range(4)))
        c_img, c_spread, c_gap = count_clusters(c_vecs)

        # --- Menu 2: 2/5 offsets b = k/10, k = 0..9 (A03) ---
        off_vecs = []
        off_defined = 0
        for k in range(10):
            cd_k = sector_channel_data(tau, Fr(2, 5), Fr(k, 10), "E4", geo=geo, grid_cache=grid_cache)
            sv, _ = extract_six_and_D(cd_k, a_DR, BASE_C)
            off_vecs.append(sv)
            if all(x is not None for x in sv):
                off_defined += 1
        off_img, off_spread, off_gap = count_clusters(off_vecs)

        # --- Menu 2b: All 99 nonzero lines (j/10, k/10) ---
        l99_vecs = []
        l99_unsigned_vecs = []
        seen_u = set()
        l99_def = 0
        for j in range(10):
            for k in range(10):
                if j == 0 and k == 0:
                    continue
                af, bf = Fr(j, 10), Fr(k, 10)
                cd_l = sector_channel_data(tau, af, bf, "E4", geo=geo, grid_cache=grid_cache)
                sv, _ = extract_six_and_D(cd_l, a_DR, BASE_C)
                l99_vecs.append(sv)
                if all(x is not None for x in sv):
                    l99_def += 1
                ukey = min((af, bf), ((-af) % 1, (-bf) % 1))
                if ukey not in seen_u:
                    seen_u.add(ukey)
                    l99_unsigned_vecs.append(sv)
        l99_img, l99_spread, l99_gap = count_clusters(l99_vecs)
        l51_img, _, _ = count_clusters(l99_unsigned_vecs)

        # --- Menu 3: 7 ends (A07) ---
        END_LIST = ("E1", "E2", "E3", "E4", "delta_inf", "small_Lmax", "small_L2")
        end_vecs = []
        end_D_errs = []
        for em in END_LIST:
            cd_e = sector_channel_data(tau, BASE_LINE[0], BASE_LINE[1], em, geo=geo, grid_cache=grid_cache)
            sv, dv = extract_six_and_D(cd_e, a_DR, BASE_C)
            end_vecs.append(sv)
            if dv is not None:
                end_D_errs.append(abs(dv - BASE_C * BASE_C))
                max_D_err_base = max(max_D_err_base, abs(dv - BASE_C * BASE_C))
        end_img, end_spread, end_gap = count_clusters(end_vecs)

        # --- Menu 4: Higgs menu R, DR, D^2R (A04) ---
        hm_vecs = []
        hm_D_errs = []
        hm_R_def = None
        for nm, av in (("R", a_R), ("DR", a_DR), ("D2R", a_D2R)):
            sv, dv = extract_six_and_D(base_cd, av, BASE_C)
            hm_vecs.append(sv)
            if nm == "R":
                hm_R_def = sum(1 for x in sv if x is not None)
            if dv is not None:
                hm_D_errs.append(abs(dv - BASE_C * BASE_C))
                max_D_err_base = max(max_D_err_base, abs(dv - BASE_C * BASE_C))
        hm_img, hm_spread, hm_gap = count_clusters(hm_vecs)

        # --- Continuous Jacobians at both h = 1e-3 and h = 5e-4 ---
        # 10 parameters: [Re tau, Im tau, Lh, Re a0, Im a0, Re a1, Im a1, Re a2, Im a2, ln c]
        jac_info = {}
        pl3_scale_err = 0
        pl3_phase_err = 0
        for h_fr in FD_STEPS:
            h = h_fr.numerator / h_fr.denominator
            cols = []
            D_pert_errs = []

            # 0, 1: Re tau, Im tau (evaluating DR at perturbed tau and E4(tau) at perturbed tau)
            for dt in (complex(h, 0), complex(0, h)):
                tp, tm = tau + dt, tau - dt
                gp, gm = get_geo(tp), get_geo(tm)
                cdp = sector_channel_data(tp, BASE_LINE[0], BASE_LINE[1], "E4", geo=gp, grid_cache=grid_cache)
                cdm = sector_channel_data(tm, BASE_LINE[0], BASE_LINE[1], "E4", geo=gm, grid_cache=grid_cache)
                sp, dp = extract_six_and_D(cdp, eval_higgs_vec("DR", tp), BASE_C)
                sm, dm = extract_six_and_D(cdm, eval_higgs_vec("DR", tm), BASE_C)
                cols.append([(sp[i] - sm[i]) / (2 * h) for i in range(6)])
                for dv in (dp, dm):
                    if dv is not None:
                        D_pert_errs.append(abs(dv - BASE_C * BASE_C))
                        max_D_err_base = max(max_D_err_base, abs(dv - BASE_C * BASE_C))

            # 2: Lh around E4
            cdp = sector_channel_data(tau, BASE_LINE[0], BASE_LINE[1], "E4", geo=geo, grid_cache=grid_cache,
                                      Lh_override=geo["L_E4"] + h)
            cdm = sector_channel_data(tau, BASE_LINE[0], BASE_LINE[1], "E4", geo=geo, grid_cache=grid_cache,
                                      Lh_override=geo["L_E4"] - h)
            sp, dp = extract_six_and_D(cdp, a_DR, BASE_C)
            sm, dm = extract_six_and_D(cdm, a_DR, BASE_C)
            cols.append([(sp[i] - sm[i]) / (2 * h) for i in range(6)])
            for dv in (dp, dm):
                if dv is not None:
                    D_pert_errs.append(abs(dv - BASE_C * BASE_C))
                    max_D_err_base = max(max_D_err_base, abs(dv - BASE_C * BASE_C))

            # 3..8: 6 real Higgs directions about DR (scaled by ||a_DR|| for conditioning? Use raw e_k / i e_k AND check!)
            # Note: scale of a_DR at Im tau ~ 3 is O(1); step h along Re/Im of each coordinate
            for idx in range(3):
                for d_comp in (complex(h, 0), complex(0, h)):
                    ap = a_DR.copy()
                    am = a_DR.copy()
                    ap[idx] += d_comp
                    am[idx] -= d_comp
                    sp, dp = extract_six_and_D(base_cd, ap, BASE_C)
                    sm, dm = extract_six_and_D(base_cd, am, BASE_C)
                    cols.append([(sp[i] - sm[i]) / (2 * h) for i in range(6)])
                    for dv in (dp, dm):
                        if dv is not None:
                            D_pert_errs.append(abs(dv - BASE_C * BASE_C))
                            max_D_err_base = max(max_D_err_base, abs(dv - BASE_C * BASE_C))

            # 9: ln c around ln 3
            cp = BASE_C * math.exp(h)
            cm = BASE_C * math.exp(-h)
            sp, _ = extract_six_and_D(base_cd, a_DR, cp)
            sm, _ = extract_six_and_D(base_cd, a_DR, cm)
            cols.append([(sp[i] - sm[i]) / (2 * h) for i in range(6)])

            # PL3 check: Higgs overall scale and overall phase null directions
            s_sc, _ = extract_six_and_D(base_cd, a_DR * (1 + h), BASE_C)
            s_ph, _ = extract_six_and_D(base_cd, a_DR * np.exp(I_UNIT * h), BASE_C)
            pl3_scale_err = max(pl3_scale_err, _vec_dist(s_sc, base_six))
            pl3_phase_err = max(pl3_phase_err, _vec_dist(s_ph, base_six))

            J = np.array(cols, dtype=float).T  # shape (6, 10)
            sv_all = np.linalg.svd(J, compute_uv=False)
            sv_no_c = np.linalg.svd(J[:, :9], compute_uv=False)
            sv_tau = np.linalg.svd(J[:, :2], compute_uv=False)
            sv_Lh = np.linalg.svd(J[:, 2:3], compute_uv=False)
            sv_H = np.linalg.svd(J[:, 3:9], compute_uv=False)
            sv_c = np.linalg.svd(J[:, 9:10], compute_uv=False)

            # Check algebraic constraint vector v_id = [0, 0, -1, -2, +1, +2] in left nullspace of J
            v_id = np.array([0, 0, -1, -2, 1, 2], dtype=float)
            left_null_res = float(np.max(np.abs(v_id @ J)))

            jac_info[str(h_fr)] = {
                "rank_joint_10": int(np.sum(sv_all > RANK_THR)),
                "rank_no_c_9": int(np.sum(sv_no_c > RANK_THR)),
                "rank_tau_2": int(np.sum(sv_tau > RANK_THR)),
                "rank_Lh_1": int(np.sum(sv_Lh > RANK_THR)),
                "rank_Higgs_6": int(np.sum(sv_H > RANK_THR)),
                "rank_c_1": int(np.sum(sv_c > RANK_THR)),
                "sv_joint_10": [_fmt(float(x)) for x in sv_all],
                "sv_Higgs_6": [_fmt(float(x)) for x in sv_H],
                "sv_tau_2": [_fmt(float(x)) for x in sv_tau],
                "left_null_identity_res": _fmt(left_null_res),
                "max_D_err": _fmt(max(D_pert_errs) if D_pert_errs else 0),
            }

        # PL2: Perturb one nonzero down channel weight by (1 + 1e-4)
        _, N_down = base_cd["down"]
        s_nz = next(s for s in UNIT_KEYS if N_down[s] is not None and N_down[s] > 0)
        s_pl2, _ = extract_six_and_D(base_cd, a_DR, BASE_C, down_norm_pert=(s_nz, 1 + 10 ** (-4)))
        pl2_shift = max(abs(s_pl2[2] - base_six[2]), abs(s_pl2[3] - base_six[3]))

        per_mod[label] = {
            "tau": f"{tau.real}+{tau.imag}j",
            "L_max": _fmt(geo["L_max"]),
            "L_2": _fmt(geo["L_2"]),
            "L_E4": _fmt(geo["L_E4"]),
            "accessory_res": _fmt(geo["res"]),
            "base_six": [_fmt(x) for x in base_six],
            "base_D": _fmt(base_D),
            "c_menu": {"img": c_img, "spread": _fmt(c_spread), "min_gap": _fmt(c_gap),
                       "max_D_rel_err": _fmt(max(c_D_rel_errs)), "max_quark_diff": _fmt(max(c_q_diffs))},
            "offset_2_5": {"img": off_img, "defined": off_defined, "spread": _fmt(off_spread), "min_gap": _fmt(off_gap)},
            "lines_99": {"img": l99_img, "img_unsigned_51": l51_img, "defined": l99_def, "spread": _fmt(l99_spread)},
            "ends_7": {"img": end_img, "spread": _fmt(end_spread), "min_gap": _fmt(end_gap),
                       "max_D_err": _fmt(max(end_D_errs))},
            "higgs_3": {"img": hm_img, "R_defined_entries": hm_R_def, "spread": _fmt(hm_spread),
                        "min_gap": _fmt(hm_gap), "max_D_err": _fmt(max(hm_D_errs))},
            "jacobians": jac_info,
            "PL2_down_shift": _fmt(pl2_shift),
            "PL3_scale_err": _fmt(pl3_scale_err),
            "PL3_phase_err": _fmt(pl3_phase_err),
        }

    # --- PL4: Mirror (a, b) -> (a, -b) at Re tau = 0 (tau = 3i) ---
    geo_mir = get_geo(TAU_MIR)
    a_DR_mir = eval_higgs_vec("DR", TAU_MIR)
    pl4_max_err = 0
    for af, bf in ((Fr(2, 5), Fr(1, 10)), (Fr(2, 5), Fr(3, 10)), (Fr(2, 5), Fr(4, 5)), (Fr(1, 10), Fr(3, 10))):
        cd1 = sector_channel_data(TAU_MIR, af, bf, "E4", geo=geo_mir, grid_cache=grid_cache)
        cd2 = sector_channel_data(TAU_MIR, af, (-bf) % 1, "E4", geo=geo_mir, grid_cache=grid_cache)
        s1, _ = extract_six_and_D(cd1, a_DR_mir, BASE_C)
        s2, _ = extract_six_and_D(cd2, a_DR_mir, BASE_C)
        pl4_max_err = max(pl4_max_err, _vec_dist(s1, s2))

    # --- PL5: Unreduced T-law (tau, (a, b)) -> (tau + 1, (a, b - a)) at delta = inf ---
    pl5_max_err = 0
    pl5_pairs = 0
    for _, tau in MODULI:
        for af, bf in ((Fr(2, 5), Fr(4, 5)), (Fr(2, 5), Fr(1, 10)), (Fr(1, 10), Fr(3, 10))):
            cd_src = sector_channel_data(tau, af, bf, "delta_inf", reduce_flag=False)
            cd_dst = sector_channel_data(tau + 1, af, (bf - af) % 1, "delta_inf", reduce_flag=False)
            s_src, _ = extract_six_and_D(cd_src, eval_higgs_vec("DR", tau), BASE_C)
            s_dst, _ = extract_six_and_D(cd_dst, eval_higgs_vec("DR", tau + 1), BASE_C)
            # Compare defined components (and verify identical defined-masks!)
            pl5_max_err = max(pl5_max_err, _vec_dist(s_src, s_dst))
            pl5_pairs += 1

    # --- Guardrail 3: 5-trial Haar U(3)^5 basis-scrambling invariance on T1 base row (30-digit mpmath SVD) ---
    mp.mp.dps = 30
    hm_t1 = _higgs_mats(dr_t1)
    Y_t1_mp = {}
    sv_t1_ref = {}
    for sec in ("up", "down", "lep"):
        R_s, N_s = cd_40[sec]
        u_s = {s: (math.sqrt(N_s[s]) * R_s[s] if N_s.get(s) is not None and N_s[s] > 0 else 0) for s in UNIT_KEYS}
        Y_np = _coupling(hm_t1["St"] if sec == "up" else hm_t1["S"], _weighted_M(u_s))
        Ym = mp.matrix([[mp.mpc(Y_np[i, j].real, Y_np[i, j].imag) for j in range(3)] for i in range(3)])
        Y_t1_mp[sec] = Ym
        # Non-squaring 6x6 Hermitian Jordan-Wielandt matrix for exact 30-digit singular values
        H6 = mp.zeros(6, 6)
        for i in range(3):
            for j in range(3):
                H6[i, 3 + j] = Ym[i, j]
                H6[3 + j, i] = mp.conj(Ym[i, j])
        eigs = sorted([mp.re(e) for e in mp.eighe(H6, eigvals_only=True)], reverse=True)[:3]
        sv_t1_ref[sec] = [mp.log(eigs[2] / eigs[1]), mp.log(eigs[1] / eigs[0])]

    rng = np.random.default_rng(20261127)
    haar_max_err = 0
    for _ in range(5):
        for sec in ("up", "down", "lep"):
            # Build 30-digit Gram-Schmidt Haar unitary pair (U_L, U_R)
            def _mp_haar():
                A = np.random.default_rng(int(rng.integers(1, 10 ** 9))).normal(size=(3, 3)) + I_UNIT * rng.normal(size=(3, 3))
                cols = [[mp.mpc(A[i, j].real, A[i, j].imag) for i in range(3)] for j in range(3)]
                Q = []
                for c in cols:
                    v = list(c)
                    for q in Q:
                        ip = mp.fsum(mp.conj(q[i]) * v[i] for i in range(3))
                        v = [v[i] - ip * q[i] for i in range(3)]
                    nrm = mp.sqrt(mp.fsum(abs(x) ** 2 for x in v))
                    Q.append([x / nrm for x in v])
                return mp.matrix([[Q[j][i] for j in range(3)] for i in range(3)])
            UL, UR = _mp_haar(), _mp_haar()
            Yp = UL * Y_t1_mp[sec] * UR.H
            H6 = mp.zeros(6, 6)
            for i in range(3):
                for j in range(3):
                    H6[i, 3 + j] = Yp[i, j]
                    H6[3 + j, i] = mp.conj(Yp[i, j])
            eigs = sorted([mp.re(e) for e in mp.eighe(H6, eigvals_only=True)], reverse=True)[:3]
            lr = [mp.log(eigs[2] / eigs[1]), mp.log(eigs[1] / eigs[0])]
            for a_v, b_v in zip(lr, sv_t1_ref[sec]):
                haar_max_err = max(haar_max_err, float(abs(a_v - b_v)))

    # --- Evaluate all 6 plants + summary gates ---
    pl1_max = max(float(per_mod[lb]["c_menu"]["max_D_rel_err"]) for lb, _ in MODULI)
    pl2_min = min(float(per_mod[lb]["PL2_down_shift"]) for lb, _ in MODULI)
    pl3_max = max(max(float(per_mod[lb]["PL3_scale_err"]), float(per_mod[lb]["PL3_phase_err"])) for lb, _ in MODULI)
    pl6_max = max(float(per_mod[lb]["c_menu"]["max_quark_diff"]) for lb, _ in MODULI)

    plants = {
        "PL1_D_scales_c2": pl1_max < 10 ** (-12),
        "PL2_down_weight_registers": pl2_min > 10 ** (-6),
        "PL3_higgs_scale_phase_null": pl3_max < 10 ** (-9),
        "PL4_mirror_at_3i": pl4_max_err < 10 ** (-10),
        "PL5_T_law_unreduced_delta_inf": pl5_max_err < 10 ** (-10),
        "PL6_c_leaves_quarks_unchanged": pl6_max < 10 ** (-14),
    }

    c_imgs = [per_mod[lb]["c_menu"]["img"] for lb, _ in MODULI]
    off_imgs = [per_mod[lb]["offset_2_5"]["img"] for lb, _ in MODULI]
    end_imgs = [per_mod[lb]["ends_7"]["img"] for lb, _ in MODULI]
    hm_imgs = [per_mod[lb]["higgs_3"]["img"] for lb, _ in MODULI]
    l99_imgs = [per_mod[lb]["lines_99"]["img"] for lb, _ in MODULI]
    l51_imgs = [per_mod[lb]["lines_99"]["img_unsigned_51"] for lb, _ in MODULI]
    ranks_10 = [per_mod[lb]["jacobians"][str(h_fr)]["rank_joint_10"] for lb, _ in MODULI for h_fr in FD_STEPS]
    ranks_9 = [per_mod[lb]["jacobians"][str(h_fr)]["rank_no_c_9"] for lb, _ in MODULI for h_fr in FD_STEPS]
    ranks_tau = [per_mod[lb]["jacobians"][str(h_fr)]["rank_tau_2"] for lb, _ in MODULI for h_fr in FD_STEPS]
    ranks_H = [per_mod[lb]["jacobians"][str(h_fr)]["rank_Higgs_6"] for lb, _ in MODULI for h_fr in FD_STEPS]

    all_nonconst = all(
        float(per_mod[lb][m]["spread"]) > NONCONST_THR
        for lb, _ in MODULI
        for m in ("c_menu", "offset_2_5", "lines_99", "ends_7", "higgs_3")
    ) and all(r >= 1 for r in ranks_tau + ranks_H)

    # Planted negative fault controls (confirming our checks detect real violations)
    # F1: wrong T-law (b not shifted by -a) on (1/10, 3/10) MUST break PL5 (> 1e-2)
    cd_bad_t = sector_channel_data(MODULI[0][1] + 1, Fr(1, 10), Fr(3, 10), "delta_inf", reduce_flag=False)
    cd_src_t = sector_channel_data(MODULI[0][1], Fr(1, 10), Fr(3, 10), "delta_inf", reduce_flag=False)
    s_bad_t, _ = extract_six_and_D(cd_bad_t, eval_higgs_vec("DR", MODULI[0][1] + 1), BASE_C)
    s_src_t, _ = extract_six_and_D(cd_src_t, eval_higgs_vec("DR", MODULI[0][1]), BASE_C)
    pf_bad_t = _vec_dist(s_bad_t, s_src_t) > 10 ** (-2)

    # F2: breaking mirror at Re tau != 0 (T1) MUST break (a, b) vs (a, -b) (> 1e-3)
    cd_m1 = sector_channel_data(MODULI[0][1], Fr(2, 5), Fr(1, 10), "E4", geo=g_t1, grid_cache=grid_cache)
    cd_m2 = sector_channel_data(MODULI[0][1], Fr(2, 5), Fr(9, 10), "E4", geo=g_t1, grid_cache=grid_cache)
    sm1, _ = extract_six_and_D(cd_m1, dr_t1, BASE_C)
    sm2, _ = extract_six_and_D(cd_m2, dr_t1, BASE_C)
    pf_bad_mir = _vec_dist(sm1, sm2) > 10 ** (-3)

    # F3: odd k = 1/10 breaks D = c^2 on DR (B1789 Q_I component!)
    _, d_odd = extract_six_and_D(cd_m1, dr_t1, BASE_C)
    pf_odd_D = (d_odd is not None) and (abs(d_odd - BASE_C * BASE_C) > 10 ** (-2))

    # F4: perturbing down channel weight by 1e-4 breaks D = c^2
    _, d_pert_pl2 = extract_six_and_D(cd_40, dr_t1, BASE_C, down_norm_pert=(
        next(s for s in UNIT_KEYS if cd_40["down"][1][s] > 0), 1 + 10 ** (-4)
    ))
    pf_pl2_D = abs(d_pert_pl2 - BASE_C * BASE_C) > 10 ** (-6)

    # F5: non-unitary scrambling (2*I on up) shifts ratios? Wait: scalar cancels, use diag(1, 2, 1) -> MUST shift > 0.1
    bad_u = {sec: (np.diag([1, 2, 1]).astype(complex), np.eye(3, dtype=complex)) for sec in ("up", "down", "lep")}
    s_bad_u, _ = extract_six_and_D(cd_40, dr_t1, BASE_C, haar_unitaries=bad_u)
    pf_bad_haar = _vec_dist(s_bad_u, s40) > 10 ** (-1)

    pf_controls = {
        "PF1_unshifted_T_breaks_PL5": pf_bad_t,
        "PF2_nonzero_Retau_breaks_mirror": pf_bad_mir,
        "PF3_odd_offset_breaks_D_eq_c2": pf_odd_D,
        "PF4_down_weight_pert_breaks_D": pf_pl2_D,
        "PF5_nonunitary_breaks_ratios": pf_bad_haar,
    }
    pf_caught = sum(1 for v in pf_controls.values() if v)

    all_ok = (
        ast_floats == 0
        and higgs_mp_err < 10 ** (-11)
        and quad_ref_diff < 10 ** (-6)
        and haar_max_err < 10 ** (-12)
        and all(plants.values())
        and all_nonconst
        and c_imgs == [5, 5, 5]
        and off_imgs == [10, 10, 10]
        and end_imgs == [7, 7, 7]
        and hm_imgs == [3, 3, 3]
        and all(r == 5 for r in ranks_10)
        and all(r == 4 for r in ranks_9)
        and max_D_err_base < CONST_THR
        and max_identity_err < 10 ** (-12)
        and pf_caught == 5
    )

    out = {
        "card": "A2-PEER-SM-R612",
        "seat_code": "fam3-v1-high-03",
        "verifying_seat_code": "fam1-v1-unset-04",
        "verifying_card": "SM-R612b (CLAIM_2026-11-27_count_the_image_refiled.md)",
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "higgs_mpmath_check_err": _fmt(higgs_mp_err),
        "quad_refinement_40_28_vs_56_40_diff": _fmt(quad_ref_diff),
        "haar_u3_5_max_err": _fmt(haar_max_err),
        "max_D_err_on_base_line": _fmt(max_D_err_base),
        "max_exact_identity_err": _fmt(max_identity_err),
        "summary_images": {
            "c_5": c_imgs,
            "offset_10": off_imgs,
            "ends_7": end_imgs,
            "higgs_3": hm_imgs,
            "lines_99": l99_imgs,
            "lines_unsigned_51": l51_imgs,
            "rank_joint_10": ranks_10,
            "rank_no_c_9": ranks_9,
            "rank_tau_2": ranks_tau,
            "rank_Higgs_6": ranks_H,
        },
        "plants": plants,
        "plant_metrics": {
            "PL1_max_err": _fmt(pl1_max),
            "PL2_min_shift": _fmt(pl2_min),
            "PL3_max_err": _fmt(pl3_max),
            "PL4_max_err": _fmt(pl4_max_err),
            "PL5_max_err": _fmt(pl5_max_err),
            "PL5_pairs_checked": pl5_pairs,
            "PL6_max_err": _fmt(pl6_max),
        },
        "planted_fault_controls": pf_controls,
        "pf_caught": pf_caught,
        "per_modulus": per_mod,
        "all_gates_passed": all_ok,
    }

    # Verify zero JSON floats recursively
    def count_json_floats(obj):
        if isinstance(obj, float):
            return 1
        if isinstance(obj, dict):
            return sum(count_json_floats(v) for v in obj.values())
        if isinstance(obj, list):
            return sum(count_json_floats(v) for v in obj)
        return 0

    jf = count_json_floats(out)
    out["json_floats"] = jf
    if jf != 0:
        out["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    print(f"DECISIVE: DISCRETE ok={c_imgs==[5,5,5] and off_imgs==[10,10,10] and end_imgs==[7,7,7] and hm_imgs==[3,3,3]} "
          f"c={c_imgs} off={off_imgs} ends={end_imgs} higgs={hm_imgs} l99={l99_imgs} l51={l51_imgs}")
    print(f"DECISIVE: JACOBIAN ok={all(r==5 for r in ranks_10) and all(r==4 for r in ranks_9)} "
          f"rk10={ranks_10} rk9={ranks_9} rktau={ranks_tau} rkH={ranks_H} D_eq_c2={max_D_err_base < CONST_THR} id_exact={max_identity_err < 10**(-12)}")
    print(f"DECISIVE: PLANTS ok={all(plants.values())} PL1={plants['PL1_D_scales_c2']} PL2={plants['PL2_down_weight_registers']} "
          f"PL3={plants['PL3_higgs_scale_phase_null']} PL4={plants['PL4_mirror_at_3i']} PL5={plants['PL5_T_law_unreduced_delta_inf']} "
          f"PL6={plants['PL6_c_leaves_quarks_unchanged']} haar={haar_max_err < 10**(-12)}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
