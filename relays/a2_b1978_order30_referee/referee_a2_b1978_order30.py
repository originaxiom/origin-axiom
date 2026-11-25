"""Disjoint Cold-Room Zero-Trust Referee for Card AGY-002_A2-B1978-ORDER30 (0 of 19).

Strictly data-free mathematical verification of Frame C (all-S two-doublet reading) at
order 30 on the act's line (P_30 = K_5^* + E[6]_prim), constructed independently from
the pre-committed Scope Card and standard origin/main Frame C mathematical definitions:
  - Disjoint L_2(tau) solver: 4-stage Gauss-Legendre (order 8) implicit symplectic
    Runge-Kutta + Chebyshev-recurrence Jacobi theta_1 log-derivative wp(z) + exact
    singularity-cancelling log-radial inward transform w(s) = z^{-1/2} y(z).
  - Branch-cut-free holomorphic Fourier theta series and Euler pentagonal eta(tau)
    (zero qh**frac, zero mp.jtheta(2, ...)).
  - Exact B1656 dual_basis() (EDUAL) derived from the 4x4 Gram matrix.
  - Exact B1940 digamma F_u and exact holomorphic theta_1'/theta_1 Jacobi a_0.
  - Direct Hermitian Gramian H_{L,f} = (1/K) sum Y_f Y_f^H diagonalized via mp.eigh
    at dps = 180 (y=30), 125 (y=20), 75 (y=10), 65 (y<=5).
  - Independent Cayley-transform Haar U(3)^3 scrambling U = (I - i H)(I + i H)^{-1}
    and 6/6 Referee Planted Fault controls (RPF1-RPF6).
  - Code hygiene: pure stdlib + mpmath + sympy, 0 float/complex literals or casts,
    0 numpy/scipy/frontier imports, 0 JSON float tokens, strictly 0 of 19.
"""

from collections import Counter
from fractions import Fraction as Fr
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
import random
import time

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT_PATH = HERE / "referee_a2_b1978_order30_out.json"

HALF = Fr(1, 2)
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
SECTOR_ORDER = ("up", "down", "lep")
UNIT_KEYS = ("1", "i", "j", "k")
SLOW_FIVE = (
    (Fr(4, 15), Fr(1, 30)),
    (Fr(4, 15), Fr(11, 30)),
    (Fr(4, 15), Fr(7, 10)),
    (Fr(11, 15), Fr(3, 10)),
    (Fr(11, 15), Fr(19, 30)),
)


def f2m(q):
    return mp.mpf(q.numerator) / q.denominator


def nd_fr(x):
    r = x % 1
    return r if r <= HALF else 1 - r


def fr_str(q):
    if q.denominator == 1:
        return str(q.numerator)
    return "%d/%d" % (q.numerator, q.denominator)


def m_str(x, sig=24):
    return mp.nstr(mp.mpf(x), sig)


def m_sci(x, sig=10):
    return mp.nstr(mp.mpf(x), sig)


def pt_order(p):
    return lcm(p[0].denominator, p[1].denominator)


def pt_key(p):
    return "(%s, %s)" % (fr_str(p[0]), fr_str(p[1]))


def assert_no_json_floats(obj, path="$"):
    if isinstance(obj, float):
        raise ValueError("Forbidden JSON float at %s: %r" % (path, obj))
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_json_floats(v, "%s.%s" % (path, k))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            assert_no_json_floats(v, "%s[%d]" % (path, i))


# ==============================================================================
# 1. Disjoint 4-Stage Gauss-Legendre (Order 8) Fuchsian Weierstrass L_2 Solver
# ==============================================================================

def build_gl4_tableau():
    """Exact 4-stage Gauss-Legendre (order 8) Butcher tableau on [0, 1]."""
    s30 = mp.sqrt(30)
    r1 = mp.sqrt((mp.mpf(15) + 2 * s30) / 35)
    r2 = mp.sqrt((mp.mpf(15) - 2 * s30) / 35)
    c = [(1 + xi) / 2 for xi in (-r1, -r2, r2, r1)]
    b = []
    A = [[mp.mpf(0)] * 4 for _ in range(4)]
    for j in range(4):
        poly = [mp.mpf(1)]
        denom = mp.mpf(1)
        for m in range(4):
            if m == j:
                continue
            denom *= c[j] - c[m]
            newp = [mp.mpf(0)] * (len(poly) + 1)
            for k, val in enumerate(poly):
                newp[k] -= val * c[m]
                newp[k + 1] += val
            poly = newp
        poly = [v / denom for v in poly]
        b.append(mp.fsum(poly[k] / (k + 1) for k in range(4)))
        for i in range(4):
            u = c[i]
            A[i][j] = mp.fsum(poly[k] * (u ** (k + 1)) / (k + 1) for k in range(4))
    A2 = [[mp.fsum(A[i][k] * A[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    BC = [b[j] * (1 - c[j]) for j in range(4)]
    return c, b, A, A2, BC


class HolomorphicWeierstrassLattice:
    """Weierstrass wp(z; tau) via direct Jacobi theta_1 logarithmic derivative:
    wp(z) = -d^2/dz^2 ln theta_1(z) + theta_1'''(0) / (3 theta_1'(0)),
    with Chebyshev angle-addition recurrence and branch-cut-free theta series."""

    def __init__(self, tau):
        I = mp.mpc(0, 1)
        self.tau = tau
        self.y = mp.im(tau)
        self.N = int(mp.ceil(mp.sqrt((mp.mp.dps + 12) * mp.ln(10) / (mp.pi * self.y)))) + 3
        self.e_n = [((-1) ** n) * mp.exp(I * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2) for n in range(self.N + 1)]
        t1p = mp.fsum((2 * n + 1) * self.e_n[n] for n in range(self.N + 1))
        t1ppp = -(mp.pi ** 2) * mp.fsum(((2 * n + 1) ** 3) * self.e_n[n] for n in range(self.N + 1))
        self.C0 = t1ppp / (3 * t1p)
        t2 = 2 * mp.fsum(mp.exp(I * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2) for n in range(self.N + 1))
        t3 = 1 + 2 * mp.fsum(mp.exp(I * mp.pi * tau * (n * n)) for n in range(1, self.N + 1))
        t4 = 1 + 2 * mp.fsum(((-1) ** n) * mp.exp(I * mp.pi * tau * (n * n)) for n in range(1, self.N + 1))
        kfac = (mp.pi ** 2) / 3
        e1 = kfac * (t3 ** 4 + t4 ** 4)
        e2 = kfac * (t2 ** 4 - t4 ** 4)
        e3 = -kfac * (t2 ** 4 + t3 ** 4)
        self.g2 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2)
        self.g3 = 4 * e1 * e2 * e3

    def wp(self, z):
        m = mp.nint(mp.im(z) / self.y)
        z = z - m * self.tau
        k = mp.nint(mp.re(z))
        z = z - k
        pz = mp.pi * z
        s_curr = mp.sin(pz)
        c_curr = mp.cos(pz)
        s2 = 2 * s_curr * c_curr
        c2 = 2 * c_curr * c_curr - 1
        en0 = self.e_n[0]
        s0 = en0 * s_curr
        s1 = en0 * c_curr
        s2sum = -en0 * s_curr
        for n in range(1, self.N + 1):
            sn_new = s_curr * c2 + c_curr * s2
            cn_new = c_curr * c2 - s_curr * s2
            s_curr, c_curr = sn_new, cn_new
            w = 2 * n + 1
            en = self.e_n[n]
            s0 += en * s_curr
            s1 += en * (w * c_curr)
            s2sum -= en * (w * w * s_curr)
        return (mp.pi ** 2) * (s1 * s1 - s0 * s2sum) / (s0 * s0) + self.C0


def _solve4x4_two_rhs(M, rhs1, rhs2):
    A = [[M[i][j] for j in range(4)] + [rhs1[i], rhs2[i]] for i in range(4)]
    for col in range(4):
        piv = max(range(col, 4), key=lambda r: abs(A[r][col]))
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        for r in range(col + 1, 4):
            fac = A[r][col] / p
            for c in range(col + 1, 6):
                A[r][c] -= fac * A[col][c]
    x1 = [mp.mpc(0)] * 4
    x2 = [mp.mpc(0)] * 4
    for r in range(3, -1, -1):
        x1[r] = (A[r][4] - mp.fsum(A[r][c] * x1[c] for c in range(r + 1, 4))) / A[r][r]
        x2[r] = (A[r][5] - mp.fsum(A[r][c] * x2[c] for c in range(r + 1, 4))) / A[r][r]
    return x1, x2


def _gl4_segment(lat, c_acc, z0, z1, grid, tab):
    GL_C, GL_B, _, GL_A2, GL_BC = tab
    d = z1 - z0
    d2 = d * d
    y1, v1, y2, v2 = mp.mpc(1), mp.mpc(0), mp.mpc(0), d
    for idx in range(len(grid) - 1):
        t0_s = grid[idx]
        h = grid[idx + 1] - t0_s
        h2 = h * h
        r = [d2 * (lat.wp(z0 + (t0_s + GL_C[j] * h) * d) / 4 + c_acc) for j in range(4)]
        M = [[(mp.mpc(1) if i == j else mp.mpc(0)) + h2 * GL_A2[i][j] * r[j] for j in range(4)] for i in range(4)]
        Y1, Y2 = _solve4x4_two_rhs(
            M,
            [y1 + h * GL_C[i] * v1 for i in range(4)],
            [y2 + h * GL_C[i] * v2 for i in range(4)],
        )
        y1 = y1 + h * v1 - h2 * mp.fsum(GL_BC[j] * r[j] * Y1[j] for j in range(4))
        v1 = v1 - h * mp.fsum(GL_B[j] * r[j] * Y1[j] for j in range(4))
        y2 = y2 + h * v2 - h2 * mp.fsum(GL_BC[j] * r[j] * Y2[j] for j in range(4))
        v2 = v2 - h * mp.fsum(GL_B[j] * r[j] * Y2[j] for j in range(4))
    return mp.matrix([[y1, y2], [v1 / d, v2 / d]])


def _gl4_log_inward(lat, c_acc, z_start, z_end, n_steps, tab):
    """Exact log-radial transform z(s) = z_start * exp(-alpha * s), w(s) = z^{-1/2} y(z),
    satisfying w''(s) + alpha^2 (z^2 Q(z) - 1/4) w(s) = 0 with exact 1/(4 z^2) pole cancellation."""
    GL_C, GL_B, _, GL_A2, GL_BC = tab
    alpha = mp.log(z_start / z_end)
    a2 = alpha * alpha
    sz0 = mp.sqrt(z_start)
    sz1 = mp.sqrt(z_end)
    w1, wp1 = 1 / sz0, alpha / (2 * sz0)
    w2, wp2 = mp.mpc(0), -alpha * sz0
    h = mp.mpf(1) / n_steps
    h2 = h * h
    for step in range(n_steps):
        s0 = mp.mpf(step) / n_steps
        r = []
        for j in range(4):
            z = z_start * mp.exp(-alpha * (s0 + GL_C[j] * h))
            r.append(a2 * (z * z * (lat.wp(z) / 4 + c_acc) - mp.mpf(1) / 4))
        M = [[(mp.mpc(1) if i == j else mp.mpc(0)) + h2 * GL_A2[i][j] * r[j] for j in range(4)] for i in range(4)]
        W1, W2 = _solve4x4_two_rhs(
            M,
            [w1 + h * GL_C[i] * wp1 for i in range(4)],
            [w2 + h * GL_C[i] * wp2 for i in range(4)],
        )
        w1 = w1 + h * wp1 - h2 * mp.fsum(GL_BC[j] * r[j] * W1[j] for j in range(4))
        wp1 = wp1 - h * mp.fsum(GL_B[j] * r[j] * W1[j] for j in range(4))
        w2 = w2 + h * wp2 - h2 * mp.fsum(GL_BC[j] * r[j] * W2[j] for j in range(4))
        wp2 = wp2 - h * mp.fsum(GL_B[j] * r[j] * W2[j] for j in range(4))
    return mp.matrix([
        [sz1 * w1, sz1 * w2],
        [(w1 / 2 - wp1 / alpha) / sz1, (w2 / 2 - wp2 / alpha) / sz1],
    ])


def _piece_grid(breaks, counts):
    g = []
    for k, n in enumerate(counts):
        a, b = breaks[k], breaks[k + 1]
        for j in range(n):
            g.append(a + (b - a) * j / n)
    g.append(breaks[-1])
    return g


def solve_L2_fuchsian(tau_in, dps_work=30, refine=False):
    """Solve exact Fuchsian Weierstrass L_2(tau) via 4-stage Gauss-Legendre (order 8)."""
    with mp.workdps(dps_work):
        I = mp.mpc(0, 1)
        tau = mp.mpc(tau_in)
        tab = build_gl4_tableau()
        lat = HolomorphicWeierstrassLattice(tau)
        z0 = (1 + tau) / 2
        sc = 2 if refine else 1
        na = max(18 * sc, int(mp.ceil(22 * sc / min(mp.mpf(1), lat.y))))
        ga = _piece_grid([mp.mpf(0), mp.mpf(1)], [na])
        if lat.y <= 3:
            nb = max(22 * sc, int(mp.ceil(26 * sc * abs(tau) / min(mp.mpf(1), lat.y))))
            gb = _piece_grid([mp.mpf(0), mp.mpf(1)], [nb])
        else:
            w1 = min(mp.mpf(1) / 4, mp.mpf(2) / lat.y)
            w2 = min(mp.mpf(1) / 2, mp.mpf(6) / lat.y)
            if w2 < mp.mpf(1) / 2 - mp.mpf(1) / 100:
                gb = _piece_grid(
                    [mp.mpf(0), mp.mpf(1) / 2 - w2, mp.mpf(1) / 2 - w1,
                     mp.mpf(1) / 2 + w1, mp.mpf(1) / 2 + w2, mp.mpf(1)],
                    [10 * sc, 14 * sc, 28 * sc, 14 * sc, 10 * sc],
                )
            else:
                gb = _piece_grid(
                    [mp.mpf(0), mp.mpf(1) / 2 - w1, mp.mpf(1) / 2 + w1, mp.mpf(1)],
                    [14 * sc, 28 * sc, 14 * sc],
                )

        c_acc = ((mp.pi ** 2) / 12 - (mp.pi / (2 * lat.y)) ** 2) if lat.y > 2 else mp.mpc(0)

        def mobius(T):
            A = mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
            return A / mp.sqrt(A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])

        def F_eval(cc):
            Ta = _gl4_segment(lat, cc, z0, z0 + 1, ga, tab)
            Tb = _gl4_segment(lat, cc, z0, z0 + tau, gb, tab)
            Aa, Ab = mobius(Ta), mobius(Tb)
            return mp.im(Aa[0, 0] + Aa[1, 1]), mp.im(Ab[0, 0] + Ab[1, 1]), Aa, Ab

        h_fd = mp.mpf(10) ** (-9)
        tol = mp.mpf(10) ** (-18)
        iters = 0
        for iters in range(1, 26):
            f1, f2, Aa, Ab = F_eval(c_acc)
            if max(abs(f1), abs(f2)) < tol:
                break
            g1, g2, _, _ = F_eval(c_acc + h_fd)
            k1, k2, _, _ = F_eval(c_acc + I * h_fd)
            J00, J01 = (g1 - f1) / h_fd, (k1 - f1) / h_fd
            J10, J11 = (g2 - f2) / h_fd, (k2 - f2) / h_fd
            det = J00 * J11 - J01 * J10
            dx = -(J11 * f1 - J01 * f2) / det
            dy = -(-J10 * f1 + J00 * f2) / det
            step = mp.hypot(dx, dy)
            if step > 1:
                dx /= step
                dy /= step
            c_acc = c_acc + dx + I * dy

        f1, f2, Aa, Ab = F_eval(c_acc)
        trace_res = max(abs(f1), abs(f2))
        inv2 = lambda M: mp.matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]]) / (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])
        # Counterclockwise puncture loop around z = 0 from z0 = (1+tau)/2
        P = inv2(Aa) * inv2(Ab) * Aa * Ab
        trP = P[0, 0] + P[1, 1]

        def fps(M):
            a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            disc = mp.sqrt((a - d) ** 2 + 4 * b * cc)
            return (a - d + disc) / (2 * cc), (a - d - disc) / (2 * cc)

        p1, p2 = fps(P)
        p_fix = (p1 + p2) / 2
        fp1, fp2 = fps(Aa)
        app = lambda M, w: (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])
        g = mp.matrix([[mp.mpc(1), -fp1], [mp.mpc(1), -p_fix]])
        s_scale = app(g, fp2)
        g = mp.matrix([[1 / s_scale, -fp1 / s_scale], [mp.mpc(1), -p_fix]])
        g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
        if mp.im(app(g, mp.mpc(0))) < 0:
            g = mp.matrix([[I, 0], [0, -I]]) * g
        RP = g * P * inv2(g)
        RP = RP / RP[0, 0]
        lam = mp.re(RP[0, 1])

        # Frobenius local expansion around z = 0
        Mdeg = 80
        a_wp = {1: lat.g2 / 20, 2: lat.g3 / 28}
        for n in range(3, Mdeg // 2 + 3):
            a_wp[n] = (mp.mpf(3) / ((2 * n + 3) * (n - 2))) * mp.fsum(a_wp[m] * a_wp[n - 1 - m] for m in range(1, n - 1))
        Q_c = [mp.mpc(0)] * (Mdeg + 1)
        Q_c[0] = c_acc
        for n in range(1, Mdeg // 2 + 1):
            if 2 * n <= Mdeg:
                Q_c[2 * n] = a_wp[n] / 4
        al = [mp.mpc(0)] * (Mdeg + 1)
        be = [mp.mpc(0)] * (Mdeg + 1)
        al[0] = mp.mpc(1)
        for m in range(1, Mdeg + 1):
            sa = mp.fsum(Q_c[j] * al[m - 2 - j] for j in range(0, m - 1))
            al[m] = -sa / (m * m)
            sb = mp.fsum(Q_c[j] * be[m - 2 - j] for j in range(0, m - 1))
            be[m] = -(2 * m * al[m] + sb) / (m * m)

        zm = mp.mpc(mp.mpf(1) / 2, mp.mpf(1) / 2) if lat.y > 2 else mp.mpc(mp.mpf(1) / 2, lat.y / 2)
        if abs(zm - z0) > mp.mpf(10) ** (-12):
            if lat.y > 12:
                zmid2 = mp.mpc(mp.mpf(1) / 2, mp.mpf(6))
                T1a = _gl4_segment(lat, c_acc, z0, zmid2, _piece_grid([mp.mpf(0), mp.mpf(1)], [16 * sc]), tab)
                T1b = _gl4_segment(lat, c_acc, zmid2, zm, _piece_grid([mp.mpf(0), mp.mpf(1)], [24 * sc]), tab)
                T1 = T1b * T1a
            else:
                nm = max(18 * sc, int(mp.ceil(22 * sc * abs(zm - z0) / min(mp.mpf(1), lat.y))))
                T1 = _gl4_segment(lat, c_acc, z0, zm, _piece_grid([mp.mpf(0), mp.mpf(1)], [nm]), tab)
        else:
            T1 = mp.eye(2)
        eps_r = mp.mpf(1) / 10
        zs = eps_r * zm / abs(zm)
        T2 = _gl4_log_inward(lat, c_acc, zm, zs, 24 * sc, tab)
        Tin = T2 * T1
        wronsk_err = abs(Tin[0, 0] * Tin[1, 1] - Tin[0, 1] * Tin[1, 0] - 1)
        u_val = app(g, Tin[0, 1] / Tin[0, 0])
        gloc = mp.fsum(be[m] * (zs ** m) for m in range(Mdeg + 1)) / mp.fsum(al[m] * (zs ** m) for m in range(Mdeg + 1))
        imB = mp.im(u_val) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(gloc))
        L2 = mp.pi - (2 * mp.pi / lam) * imB
        return {
            "L2": mp.mpf(L2),
            "c_re": mp.re(c_acc),
            "c_im": mp.im(c_acc),
            "lam": mp.mpf(lam),
            "trace_residual": mp.mpf(trace_res),
            "trP_plus_2": abs(trP + 2),
            "wronskian_err": mp.mpf(wronsk_err),
            "newton_iters": iters,
        }


# ==============================================================================
# 2. Branch-Cut-Free Holomorphic Frame C Engine (All-S Two-Doublet Reading)
# ==============================================================================

def build_frame_algebra():
    """Exact B1656 quaternion blocks and dual basis EDUAL computed directly from Gram matrix."""
    I = mp.mpc(0, 1)
    I2 = mp.eye(2)
    QI = mp.matrix([[I, 0], [0, -I]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    units = {"1": I2, "i": QI, "j": QJ, "k": QK}
    ec = {s: EPS * units[s] for s in UNIT_KEYS}
    # Gram matrix G[t, s] = sum_{m,n} (EPS * C_t)_{m,n} * (C_s)_{m,n}
    G = mp.matrix([
        [mp.fsum(ec[t][m, n] * units[s][m, n] for m in range(2) for n in range(2)) for s in UNIT_KEYS]
        for t in UNIT_KEYS
    ])
    Ginv = G ** (-1)
    edual = {}
    for a_idx, s_key in enumerate(UNIT_KEYS):
        mat = mp.zeros(2, 2)
        for b_idx, b_key in enumerate(UNIT_KEYS):
            mat += Ginv[b_idx, a_idx] * units[b_key]
        edual[s_key] = mat
    blocks = [QJ, QI, QK]
    return I, QI, QJ, QK, EPS, units, edual, blocks


def th_holo_0(k_idx, tau):
    """Branch-cut-free holomorphic theta_k(0, tau) for k in {2, 3, 4}."""
    I = mp.mpc(0, 1)
    y = mp.im(tau)
    N = int(mp.ceil(mp.sqrt((mp.mp.dps + 15) * mp.ln(10) / (mp.pi * y)))) + 3
    if k_idx == 2:
        return 2 * mp.fsum(mp.exp(I * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2) for n in range(N + 1))
    if k_idx == 3:
        return 1 + 2 * mp.fsum(mp.exp(I * mp.pi * tau * (n * n)) for n in range(1, N + 1))
    if k_idx == 4:
        return 1 + 2 * mp.fsum(((-1) ** n) * mp.exp(I * mp.pi * tau * (n * n)) for n in range(1, N + 1))
    raise ValueError("Invalid theta index")


def eta_pentagonal(tau):
    """Branch-cut-free Euler pentagonal Dedekind eta(tau)."""
    I = mp.mpc(0, 1)
    y = mp.im(tau)
    # Term exponent is -pi * y * k * (3k - 1) ~ -3 pi y k^2
    K = int(mp.ceil(mp.sqrt((mp.mp.dps + 15) * mp.ln(10) / (3 * mp.pi * y)))) + 4
    s = mp.fsum(((-1) ** k) * mp.exp(I * mp.pi * tau * (k * (3 * k - 1))) for k in range(-K, K + 1))
    return mp.exp(I * mp.pi * tau / 12) * s


def thc_holo(a_fr, b_fr, tau):
    """Branch-cut-free holomorphic characteristic theta[a; b](0, tau) for exact Fractions a, b."""
    I = mp.mpc(0, 1)
    y = mp.im(tau)
    # Center sum around integer n_c = -round(a) using exact integer arithmetic
    nc = -((2 * a_fr.numerator + a_fr.denominator) // (2 * a_fr.denominator))
    af = f2m(a_fr)
    bf = f2m(b_fr)
    N = int(mp.ceil(mp.sqrt((mp.mp.dps + 15) * mp.ln(10) / (mp.pi * y)))) + 3
    return mp.fsum(
        mp.exp(I * mp.pi * tau * ((n + af) ** 2) + 2 * I * mp.pi * (n + af) * bf)
        for n in range(nc - N, nc + N + 1)
    )


def a0_holo(al_fr, be_fr, tau):
    """Exact periodic Jacobi a_0 = 2*pi*i*al + theta_1'(z)/theta_1(z), z = al*tau + be.
    Periodic mod 1 in (al, be); reduced into (-1/2, 1/2] for uniform fast convergence."""
    I = mp.mpc(0, 1)
    # Reduce al into (-1/2, 1/2] and be into [0, 1)
    ar = al_fr % 1
    if ar > HALF:
        ar = ar - 1
    br = be_fr % 1
    af = f2m(ar)
    bf = f2m(br)
    z = af * tau + bf
    y = mp.im(tau)
    N = int(mp.ceil(mp.sqrt((mp.mp.dps + 15) * mp.ln(10) / (mp.pi * y)))) + 4
    t1 = mp.mpc(0)
    t1p = mp.mpc(0)
    for n in range(-N, N + 1):
        sgn = 1 if (n % 2 == 0) else -1
        h = n + mp.mpf(1) / 2
        term = sgn * mp.exp(I * mp.pi * tau * (h * h) + I * mp.pi * (2 * n + 1) * z)
        t1 += term
        t1p += (2 * n + 1) * term
    t1 = -I * t1
    t1p = mp.pi * t1p
    return 2 * I * mp.pi * af + t1p / t1


def F_u_exact(u1_fr, u2_fr, tau):
    """Exact B1940 digamma closed form for F_u(u1, u2, tau, Im tau)."""
    I = mp.mpc(0, 1)
    a = u1_fr % 1
    b = u2_fr % 1
    x = mp.re(tau)
    y = mp.im(tau)
    if a != 0:
        af = f2m(a)
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(af) + mp.digamma(1 - af))
        zero_row = mp.mpf(0)
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zero_row = y * (mp.pi ** 2) / (mp.sin(mp.pi * f2m(b)) ** 2) if b != 0 else mp.inf
    K = int(mp.ceil((mp.mp.dps + 12) * mp.ln(10) / (2 * mp.pi * y))) + 4
    af = f2m(a)
    u2f = f2m(u2_fr)
    tot = mp.mpf(0)
    for k in range(-K, K + 1):
        m = af + k
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2 * I * mp.pi * (m * x + u2f))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return first + zero_row + tot


def is_zero_char(c_pair):
    return (c_pair[0] - HALF) % 1 == 0 and (c_pair[1] - HALF) % 1 == 0


class FrameCTauContext:
    """Precomputed tau-level Frame C objects (S(tau), t1p, algebra) at current mp.mp.dps."""

    def __init__(self, tau, L2, flip_c0=False):
        self.tau = mp.mpc(tau)
        self.y = mp.im(self.tau)
        self.L2 = mp.mpf(L2)
        I, QI, QJ, QK, EPS, units, edual, blocks = build_frame_algebra()
        self.I = I
        self.EPS = EPS
        self.EDUAL = edual
        self.BLOCKS = blocks
        t2 = th_holo_0(2, self.tau)
        t3 = th_holo_0(3, self.tau)
        t4 = th_holo_0(4, self.tau)
        et = eta_pentagonal(self.tau)
        self.eta = et
        self.t1p = 2 * mp.pi * (et ** 3)
        e3 = 24 * (et ** 3)
        self.c0 = -t2 ** 2 * (t3 ** 4 + t4 ** 4) / e3
        self.c1 = t4 ** 2 * (t2 ** 4 + t3 ** 4) / e3
        self.c2 = I * t3 ** 2 * (t2 ** 4 - t4 ** 4) / e3
        if flip_c0:
            self.c0 = -self.c0
        self.S = self.c0 * QI + self.c1 * QJ + self.c2 * QK
        # Precompute 3x3 tensor T_{ab, mn} = (C_a^T * EPS * S * C_b)_{m, n}
        self.T = [[blocks[a].T * EPS * self.S * blocks[b] for b in range(3)] for a in range(3)]
        self.nullity_err = abs(self.c0 ** 2 + self.c1 ** 2 + self.c2 ** 2 - (et ** 6) / 4) / abs((et ** 6) / 4)
        self.jacobi_err = abs(t3 ** 4 - t2 ** 4 - t4 ** 4) / abs(t3 ** 4)
        self.eta_jacobi_err = abs(2 * (et ** 3) - t2 * t3 * t4) / abs(2 * (et ** 3))

    def yukawa(self, a_fr, b_fr, ql, qr, return_details=False):
        I = self.I
        x0, x1 = ql * a_fr, 2 * ql * b_fr
        y0, y1 = qr * a_fr, 2 * qr * b_fr
        ap, am = x0 + y0, x0 - y0
        bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
        efac = mp.exp(-2 * I * mp.pi * f2m(x0))
        kap = {"1": -I * efac, "i": mp.mpf(-1), "j": -efac, "k": I}
        cs = {"1": (ap + HALF, bp + HALF), "i": (ap + HALF, bp), "j": (ap, bp + HALF), "k": (ap, bp)}
        ds = {"1": (am + HALF, bm + HALF), "i": (am + HALF, bm), "j": (am, bm + HALF), "k": (am, bm)}
        u = {}
        zero_flags = {}
        for s in UNIT_KEYS:
            if is_zero_char(cs[s]) or is_zero_char(ds[s]):
                u[s] = mp.mpc(0)
                zero_flags[s] = True
                continue
            zero_flags[s] = False
            R = kap[s] * thc_holo(cs[s][0], cs[s][1], self.tau) * thc_holo(ds[s][0], ds[s][1], self.tau) / self.t1p
            al, be = cs[s][0] - HALF, cs[s][1] - HALF
            a0 = a0_holo(al, be, self.tau)
            c_val = F_u_exact(al, be, self.tau) + mp.pi * mp.log(self.y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
            c_val = c_val - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * self.L2)
            arg = 2 * mp.pi * self.L2 + c_val
            u[s] = mp.sqrt(arg) * R if mp.re(arg) > 0 else mp.mpc(0)
        Mw = mp.zeros(2, 2)
        for s in UNIT_KEYS:
            Mw += u[s] * self.EDUAL[s]
        Y = mp.matrix([
            [mp.fsum(self.T[a][b][m, n] * Mw[m, n] for m in range(2) for n in range(2)) for b in range(3)]
            for a in range(3)
        ])
        if return_details:
            return Y, Mw, u, zero_flags
        return Y


def svd_asc(Y):
    """Ascending singular values [m1 <= m2 <= m3] and left singular basis U = [u1, u2, u3]."""
    U, sv, Vh = mp.svd_c(Y)
    ord_i = sorted(range(3), key=lambda i: abs(sv[i]))
    U_asc = mp.matrix([[U[r, ord_i[c]] for c in range(3)] for r in range(3)])
    V_asc = mp.matrix([[mp.conj(Vh[ord_i[c], r]) for c in range(3)] for r in range(3)])
    sv_asc = [abs(sv[i]) for i in ord_i]
    return U_asc, sv_asc, V_asc


def gramian_eigh_asc(Y_list):
    """Disjoint Hermitian Left-Gramian H_L = (1/K) sum Y Y^H diagonalized via mp.eigh."""
    K = len(Y_list)
    H = mp.zeros(3, 3)
    for Y in Y_list:
        H += Y * Y.H
    H = H / K
    H = (H + H.H) / 2
    evals, Q = mp.eigh(H)
    ord_i = sorted(range(3), key=lambda i: mp.re(evals[i]))
    ev_sorted = [mp.re(evals[i]) for i in ord_i]
    sv_asc = [mp.sqrt(ev) if ev > 0 else mp.mpf(0) for ev in ev_sorted]
    U_asc = mp.matrix([[Q[r, ord_i[c]] for c in range(3)] for r in range(3)])
    return H, U_asc, sv_asc, ev_sorted


def right_gramian_eigh_asc(Y_list):
    """Hermitian Right-Gramian H_R = (1/K) sum Y^H Y diagonalized via mp.eigh."""
    K = len(Y_list)
    H = mp.zeros(3, 3)
    for Y in Y_list:
        H += Y.H * Y
    H = H / K
    H = (H + H.H) / 2
    evals, Q = mp.eigh(H)
    ord_i = sorted(range(3), key=lambda i: mp.re(evals[i]))
    ev_sorted = [mp.re(evals[i]) for i in ord_i]
    sv_asc = [mp.sqrt(ev) if ev > 0 else mp.mpf(0) for ev in ev_sorted]
    V_asc = mp.matrix([[Q[r, ord_i[c]] for c in range(3)] for r in range(3)])
    return H, V_asc, sv_asc, ev_sorted


def observables_from_U_sv(U_u, sv_u, U_d, sv_d, sv_e):
    """Compute all 10 dimensionless observables + Jarlskog + min_diag + CKM unitarity."""
    V = U_u.H * U_d
    unit_err = mp.norm(V.H * V - mp.eye(3))
    J_cp = abs(mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1])))
    min_diag = min(abs(V[k, k]) for k in range(3))
    max_off = max(abs(V[i, j]) for i in range(3) for j in range(3) if i != j)
    obs = {
        "up_m2m3": sv_u[1] / sv_u[2],
        "up_m1m3": sv_u[0] / sv_u[2],
        "down_m2m3": sv_d[1] / sv_d[2],
        "down_m1m3": sv_d[0] / sv_d[2],
        "lep_m2m3": sv_e[1] / sv_e[2],
        "lep_m1m3": sv_e[0] / sv_e[2],
        "V12": abs(V[0, 1]),
        "V23": abs(V[1, 2]),
        "V13": abs(V[0, 2]),
        "V31": abs(V[2, 0]),
        "V21": abs(V[1, 0]),
        "V32": abs(V[2, 1]),
        "J_CP": J_cp,
        "min_diag": min_diag,
        "max_off": max_off,
        "unitarity_err": unit_err,
        "V_abs": [[abs(V[i, j]) for j in range(3)] for i in range(3)],
    }
    return obs


def obs_rate(v1, v2, y1, y2):
    a1, a2 = abs(v1), abs(v2)
    if a1 == 0 or a2 == 0:
        return None
    return -(mp.log(a2) - mp.log(a1)) / (mp.pi * (y2 - y1))


def elapsed_sec_str(t0_ns):
    return m_str(mp.mpf((time.monotonic_ns() - t0_ns) // 1000000) / 1000, 8)


def ckm_mag_order_label(obs):
    pairs = sorted([("V12", obs["V12"]), ("V23", obs["V23"]), ("V13", obs["V13"])], key=lambda kv: -kv[1])
    return ">".join(k for k, _ in pairs)


def ed_split_metrics(obs):
    r2 = abs(mp.log(obs["lep_m2m3"] / obs["down_m2m3"])) if (obs["lep_m2m3"] > 0 and obs["down_m2m3"] > 0) else mp.mpf(0)
    r1 = abs(mp.log(obs["lep_m1m3"] / obs["down_m1m3"])) if (obs["lep_m1m3"] > 0 and obs["down_m1m3"] > 0) else mp.mpf(0)
    return r2, max(r2, r1)


# ==============================================================================
# 3. Torsion Point Sets & Exact O1 Tropical Theorem (SymPy + Fraction)
# ==============================================================================

def build_torsion_sets():
    K5 = [((k * Fr(1, 5)) % 1, (k * Fr(2, 5)) % 1) for k in range(1, 5)]
    E6 = sorted({(Fr(i, 6), Fr(j, 6)) for i in range(6) for j in range(6) if pt_order((Fr(i, 6), Fr(j, 6))) == 6})
    P30 = sorted({((a5 + a6) % 1, (b5 + b6) % 1) for (a5, b5) in K5 for (a6, b6) in E6})
    assert len(K5) == 4 and len(E6) == 24 and len(P30) == 96
    assert all(pt_order(p) == 30 for p in P30)
    return K5, E6, P30


def build_level_N_sets(N):
    """Build both unconstrained E[N]_prim and act-line-lifted P_N (for 5 | N)."""
    E_N = sorted({(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if pt_order((Fr(i, N), Fr(j, N))) == N})
    K5 = [((k * Fr(1, 5)) % 1, (k * Fr(2, 5)) % 1) for k in range(1, 5)]
    K5_set = set(K5)
    if N % 5 != 0:
        return E_N, E_N
    k = N // 5
    if k % 5 != 0:
        Ek = [(Fr(i, k), Fr(j, k)) for i in range(k) for j in range(k) if pt_order((Fr(i, k), Fr(j, k))) == k]
        P_N = sorted({((a5 + ak) % 1, (b5 + bk) % 1) for (a5, b5) in K5 for (ak, bk) in Ek})
    else:
        # 25 | N: lift K_5^* via exact order-25 points w with 5*w in K_5^*, then add E[N/25]_prim
        m = N // 25
        P25 = [
            (Fr(i, 25), Fr(j, 25))
            for i in range(25)
            for j in range(25)
            if ((5 * Fr(i, 25)) % 1, (5 * Fr(j, 25)) % 1) in K5_set
        ]
        if m == 1:
            P_N = sorted(P25)
        else:
            Em = [(Fr(i, m), Fr(j, m)) for i in range(m) for j in range(m) if pt_order((Fr(i, m), Fr(j, m))) == m]
            P_N = sorted({((a25 + am) % 1, (b25 + bm) % 1) for (a25, b25) in P25 for (am, bm) in Em})
    assert all(pt_order(p) == N for p in P_N)
    return E_N, P_N


def build_symbolic_tropical_engine():
    """Exact SymPy min-plus engine for M(s=0) = Higgs-SVD shared-Higgs-cancelled Yukawa."""
    up, um, ap, am, t = sp.symbols("up um ap am t")
    upc, umc, apc, amc, tc = sp.symbols("upc umc apc amc tc")
    M = sp.Matrix([
        [2 * up, ap, 0],
        [am, -um - t * up, t * ap],
        [0, t * am, 2 * t * um],
    ])
    Mc = sp.Matrix([
        [2 * upc, apc, 0],
        [amc, -umc - tc * upc, tc * apc],
        [0, tc * amc, 2 * tc * umc],
    ])
    H = sp.expand(M * Mc.T)
    D01 = sp.expand(H[0, 0] * H[1, 1] - H[0, 1] * H[1, 0])
    # Exact numerators of Schur complement couplings:
    # S_21_num = H[2,1]*H[0,0] - H[2,0]*H[0,1]; S_20_num = H[2,0]*H[1,1] - H[2,1]*H[1,0]
    S21_num = sp.expand(H[2, 1] * H[0, 0] - H[2, 0] * H[0, 1])
    S20_num = sp.expand(H[2, 0] * H[1, 1] - H[2, 1] * H[1, 0])

    def compile_poly(expr):
        monoms = []
        for term in sp.expand(expr).as_ordered_terms():
            coeff, factors = term.as_coeff_mul()
            if coeff == 0:
                continue
            pw_map = []
            for f in factors:
                if isinstance(f, sp.Pow):
                    pw_map.append((f.args[0], int(f.args[1])))
                else:
                    pw_map.append((f, 1))
            monoms.append(pw_map)
        return monoms

    polys = {
        "H00": compile_poly(H[0, 0]),
        "H11": compile_poly(H[1, 1]),
        "H01": compile_poly(H[0, 1]),
        "H02": compile_poly(H[0, 2]),
        "H12": compile_poly(H[1, 2]),
        "D01": compile_poly(D01),
        "S21": compile_poly(S21_num),
        "S20": compile_poly(S20_num),
    }

    def eval_poly_trop(name, exps):
        best = None
        for pw_map in polys[name]:
            e = Fr(0)
            for sym, pw in pw_map:
                e += exps[sym] * pw
            if best is None or e < best:
                best = e
        return best

    def floor_half_int(x):
        y = x + HALF
        return y.numerator // y.denominator

    def channel_exps(a_fr, ql, qr):
        apv = (ql + qr) * a_fr
        amv = (ql - qr) * a_fr
        e_dom_jk = nd_fr(apv) ** 2 + nd_fr(amv) ** 2 - Fr(1, 4)
        gap_jk = min(1 - 2 * nd_fr(apv), 1 - 2 * nd_fr(amv))
        if gap_jk == 0:
            e_up = e_um = e_dom_jk
        else:
            if (floor_half_int(apv) + floor_half_int(amv)) % 2 == 0:
                e_up, e_um = e_dom_jk, e_dom_jk + gap_jk
            else:
                e_up, e_um = e_dom_jk + gap_jk, e_dom_jk
        ap2, am2 = apv + HALF, amv + HALF
        e_dom_1i = nd_fr(ap2) ** 2 + nd_fr(am2) ** 2 - Fr(1, 4)
        gap_1i = min(2 * nd_fr(apv), 2 * nd_fr(amv))
        if gap_1i == 0:
            e_ap = e_am = e_dom_1i
        else:
            if (floor_half_int(ap2) + floor_half_int(am2)) % 2 == 0:
                e_am, e_ap = e_dom_1i, e_dom_1i + gap_1i
            else:
                e_ap, e_am = e_dom_1i, e_dom_1i + gap_1i
        return {
            up: e_up, upc: e_up,
            um: e_um, umc: e_um,
            ap: e_ap, apc: e_ap,
            am: e_am, amc: e_am,
            t: Fr(1), tc: Fr(1),
        }

    def sector_tropical(a_fr, ql, qr):
        ex = channel_exps(a_fr, ql, qr)
        e_up, e_um, e_ap, e_am = ex[up], ex[um], ex[ap], ex[am]
        INF = Fr(999)
        M_exp = [
            [e_up, e_ap, INF],
            [e_am, min(e_um, 1 + e_up), 1 + e_ap],
            [INF, 1 + e_am, 1 + e_um],
        ]
        e3 = min(M_exp[i][j] for i in range(3) for j in range(3))
        minors = []
        for r1 in range(3):
            for r2 in range(r1 + 1, 3):
                for c1 in range(3):
                    for c2 in range(c1 + 1, 3):
                        minors.append(min(M_exp[r1][c1] + M_exp[r2][c2], M_exp[r1][c2] + M_exp[r2][c1]))
        e32 = min(minors)
        e2 = e32 - e3
        # Exact B1659 / B1969 determinant exponent: det M = (s^2+2t)(2 up um + ap am)(um + s ui + t up)
        e_det_channel = min(e_up + e_um, e_ap + e_am)
        e_uh = min(e_um, HALF + min(e_ap, e_am), 1 + e_up)
        e321 = 1 + e_det_channel + e_uh
        e1 = e321 - e32

        h00 = eval_poly_trop("H00", ex)
        h11 = eval_poly_trop("H11", ex)
        h01 = eval_poly_trop("H01", ex)
        h02 = eval_poly_trop("H02", ex)
        h12 = eval_poly_trop("H12", ex)
        d01 = eval_poly_trop("D01", ex)
        if h00 < h11:
            heavy = "e_+"
            lam3 = h00
            lam2 = d01 - h00
            u3M = h01 - lam3
            u3L = min(h02 - lam3, h12 + h01 - 2 * lam3)
            u2L = eval_poly_trop("S21", ex) - d01
            u1H = eval_poly_trop("S20", ex) - d01
        elif h11 < h00:
            heavy = "e_1"
            lam3 = h11
            lam2 = d01 - h11
            u3M = h01 - lam3
            u3L = min(h12 - lam3, h02 + h01 - 2 * lam3)
            u2L = eval_poly_trop("S20", ex) - d01
            u1H = eval_poly_trop("S21", ex) - d01
        else:
            heavy = "tie"
            u3M = Fr(0)
            u3L = Fr(0)
            u2L = Fr(0)
            u1H = Fr(0)
        return {
            "m2m3": e2 - e3,
            "m1m3": e1 - e3,
            "heavy": heavy,
            "u3M": u3M,
            "u3L": u3L,
            "u2L": u2L,
            "u1H": u1H,
            "h00": h00,
            "h11": h11,
        }

    def full_tropical_rates(a_fr, qu_r=-4):
        su = sector_tropical(a_fr, 1, qu_r)
        sd = sector_tropical(a_fr, 1, 2)
        se = sector_tropical(a_fr, -3, 6)
        if su["heavy"] != sd["heavy"] or su["heavy"] == "tie":
            aligned = False
            e23 = Fr(0)
            e12 = Fr(0)
            e13 = Fr(0)
            e31 = Fr(0)
        else:
            aligned = True
            e23 = min(su["u3M"], sd["u3M"])
            e12 = min(su["u2L"], sd["u2L"])
            e13 = min(su["u1H"], su["u2L"] + sd["u3M"], sd["u3L"])
            e31 = min(sd["u1H"], sd["u2L"] + su["u3M"], su["u3L"])
        return {
            "up_m2m3": su["m2m3"],
            "up_m1m3": su["m1m3"],
            "down_m2m3": sd["m2m3"],
            "down_m1m3": sd["m1m3"],
            "lep_m2m3": se["m2m3"],
            "lep_m1m3": se["m1m3"],
            "V12": e12,
            "V23": e23,
            "V13": e13,
            "V31": e31,
            "aligned": aligned,
            "heavy_up": su["heavy"],
            "heavy_down": sd["heavy"],
        }

    return full_tropical_rates


# ==============================================================================
# 4. Main Cold-Room Referee Execution
# ==============================================================================

def main():
    t_start = time.monotonic_ns()
    K5, E6, P30 = build_torsion_sets()
    trop_fn = build_symbolic_tropical_engine()

    report = {
        "meta": {
            "card": "AGY-002_A2-B1978-ORDER30",
            "role": "Disjoint Cold-Room Zero-Trust Referee",
            "firewall": "0 of 19 (strictly data-free)",
            "L2_algorithm": "4-stage Gauss-Legendre (order 8) symplectic IRK + Chebyshev theta1 log-deriv wp + log-radial inward transform",
            "gramian_algorithm": "Direct Hermitian H_L = (1/K) sum Y Y^H diagonalized via mp.eigh (dps=180 at y=30, 125 at y=20, 75 at y=10, 65 at y<=5)",
            "haar_algorithm": "Independent Cayley transform U = (I - i H)(I + i H)^{-1} from integer PRNG Hermitian H",
        }
    }

    # --------------------------------------------------------------------------
    # STEP 1: Disjoint Fuchsian Weierstrass L_2(tau) Verification & Table
    # --------------------------------------------------------------------------
    print("[Referee] Step 1: Solving L_2(tau) via 4-stage Gauss-Legendre (order 8)...", flush=True)
    t_l2 = time.monotonic_ns()

    # Benchmark gate at tau = i
    res_i = solve_L2_fuchsian(mp.mpc(0, 1), dps_work=30)

    # Covariance check at tau0 = -9/10 + 6/5 i for T, S, M
    tau0_fr = (Fr(-9, 10), Fr(6, 5))
    tau0_mp = mp.mpc(f2m(tau0_fr[0]), f2m(tau0_fr[1]))
    res_tau0 = solve_L2_fuchsian(tau0_mp, dps_work=30)
    gammas = {
        "T": (1, 1, 0, 1),
        "S": (0, -1, 1, 0),
        "M": (2, 1, 1, 1),
    }
    l2_cov_tau0 = {}
    max_l2_cov_err = mp.mpf(0)
    max_l2_trace_res = max(res_i["trace_residual"], res_tau0["trace_residual"])
    for gname, (ga, gb, gc, gd) in gammas.items():
        gt = (ga * tau0_mp + gb) / (gc * tau0_mp + gd)
        rg = solve_L2_fuchsian(gt, dps_work=30)
        expected = res_tau0["L2"] + mp.log(abs(gc * tau0_mp + gd))
        err = abs(rg["L2"] - expected)
        max_l2_cov_err = max(max_l2_cov_err, err)
        max_l2_trace_res = max(max_l2_trace_res, rg["trace_residual"])
        l2_cov_tau0[gname] = {
            "gamma_tau_re": m_str(mp.re(gt), 18),
            "gamma_tau_im": m_str(mp.im(gt), 18),
            "L2_ode": m_str(rg["L2"], 20),
            "L2_expected": m_str(expected, 20),
            "abs_err": m_sci(err, 8),
            "trace_residual": m_sci(rg["trace_residual"], 8),
            "wronskian_err": m_sci(rg["wronskian_err"], 8),
        }

    # 14 heights at x = 13/100
    heights_14 = [
        Fr(1, 1), Fr(3, 2), Fr(2, 1), Fr(5, 2), Fr(3, 1), Fr(4, 1), Fr(5, 1),
        Fr(6, 1), Fr(8, 1), Fr(10, 1), Fr(15, 1), Fr(20, 1), Fr(30, 1), Fr(40, 1),
    ]
    x_main = Fr(13, 100)
    L2_table = {}
    L2_profile_x13 = {}
    for y_fr in heights_14:
        tau_val = mp.mpc(f2m(x_main), f2m(y_fr))
        r = solve_L2_fuchsian(tau_val, dps_work=30)
        L2_table[(x_main, y_fr)] = r["L2"]
        max_l2_trace_res = max(max_l2_trace_res, r["trace_residual"])
        L2_profile_x13[fr_str(y_fr)] = {
            "L2": m_str(r["L2"], 20),
            "c_re": m_str(r["c_re"], 16),
            "c_im": m_str(r["c_im"], 16),
            "lam": m_str(r["lam"], 16),
            "trace_residual": m_sci(r["trace_residual"], 8),
            "wronskian_err": m_sci(r["wronskian_err"], 8),
        }

    # Check L_2(tau + 1) = L_2(tau) at (13/100, 2) and (13/100, 6)
    l2_shift_checks = {}
    max_l2_shift_err = mp.mpf(0)
    for y_fr in (Fr(2, 1), Fr(6, 1)):
        tau_sh = mp.mpc(f2m(x_main + 1), f2m(y_fr))
        r_sh = solve_L2_fuchsian(tau_sh, dps_work=30)
        err = abs(r_sh["L2"] - L2_table[(x_main, y_fr)])
        max_l2_shift_err = max(max_l2_shift_err, err)
        max_l2_trace_res = max(max_l2_trace_res, r_sh["trace_residual"])
        l2_shift_checks[fr_str(y_fr)] = {
            "L2_tau": m_str(L2_table[(x_main, y_fr)], 20),
            "L2_tau_plus_1": m_str(r_sh["L2"], 20),
            "abs_err": m_sci(err, 8),
            "trace_residual": m_sci(r_sh["trace_residual"], 8),
        }

    # Extra columns x in {0, 31/100, 1/2} at y in {2, 4, 10, 20}
    extra_cols = [Fr(0, 1), Fr(31, 100), Fr(1, 2)]
    col_heights = [Fr(2, 1), Fr(4, 1), Fr(10, 1), Fr(20, 1)]
    L2_extra_cols = {}
    for x_fr in extra_cols:
        L2_extra_cols[fr_str(x_fr)] = {}
        for y_fr in col_heights:
            tau_val = mp.mpc(f2m(x_fr), f2m(y_fr))
            r = solve_L2_fuchsian(tau_val, dps_work=30)
            L2_table[(x_fr, y_fr)] = r["L2"]
            max_l2_trace_res = max(max_l2_trace_res, r["trace_residual"])
            L2_extra_cols[fr_str(x_fr)][fr_str(y_fr)] = {
                "L2": m_str(r["L2"], 20),
                "trace_residual": m_sci(r["trace_residual"], 8),
            }

    L2_y6 = L2_table[(x_main, Fr(6, 1))]
    L2_minus_L2_6 = {
        fr_str(y_fr): m_str(L2_table[(x_main, y_fr)] - L2_y6, 16)
        for y_fr in (Fr(10, 1), Fr(20, 1), Fr(30, 1), Fr(40, 1))
    }

    report["L2_fuchsian"] = {
        "benchmark_tau_i": {
            "L2": m_str(res_i["L2"], 20),
            "lam": m_str(res_i["lam"], 16),
            "trace_residual": m_sci(res_i["trace_residual"], 8),
            "wronskian_err": m_sci(res_i["wronskian_err"], 8),
        },
        "tau0_base": {
            "tau_re": fr_str(tau0_fr[0]),
            "tau_im": fr_str(tau0_fr[1]),
            "L2": m_str(res_tau0["L2"], 20),
            "trace_residual": m_sci(res_tau0["trace_residual"], 8),
        },
        "tau0_covariance": l2_cov_tau0,
        "max_covariance_err": m_sci(max_l2_cov_err, 8),
        "T_shift_checks": l2_shift_checks,
        "max_T_shift_err": m_sci(max_l2_shift_err, 8),
        "max_trace_residual": m_sci(max_l2_trace_res, 8),
        "profile_x_13_100": L2_profile_x13,
        "L2_y_minus_L2_6": L2_minus_L2_6,
        "extra_columns": L2_extra_cols,
        "elapsed_sec": elapsed_sec_str(t_l2),
    }
    print("[Referee] Step 1 done in %ss | max_cov_err=%s | max_trace_res=%s" % (
        report["L2_fuchsian"]["elapsed_sec"], m_sci(max_l2_cov_err, 4), m_sci(max_l2_trace_res, 4)), flush=True)

    # --------------------------------------------------------------------------
    # STEP 2: Cache High-Precision Frame C Snapshots for P30 at y in {2,3,5,10,20,30,40}
    # --------------------------------------------------------------------------
    print("[Referee] Step 2: Computing P30 Frame C snapshots (y=2,3,5,10,20,30,40)...", flush=True)
    t_snap = time.monotonic_ns()

    # Exact dps schedule ensuring >25 spare digits even for squared Gramian eigenvalues (mp.eigh)
    dps_for_y = {
        Fr(2, 1): 65,
        Fr(3, 1): 65,
        Fr(5, 1): 65,
        Fr(10, 1): 75,
        Fr(20, 1): 125,
        Fr(30, 1): 180,
        Fr(40, 1): 135,  # SVD only at y=40 (not squared Gramian)
    }

    P30_Y = {}      # (y_fr) -> {pt: {sec: Y}}
    P30_obs = {}    # (y_fr) -> {pt: obs}
    P30_u_one_y30 = {}
    is_zero_total_count = 0
    internal_invariants = {}

    for y_fr in (Fr(2, 1), Fr(3, 1), Fr(5, 1), Fr(10, 1), Fr(20, 1), Fr(30, 1), Fr(40, 1)):
        dps_y = dps_for_y[y_fr]
        with mp.workdps(dps_y):
            tau_val = mp.mpc(f2m(x_main), f2m(y_fr))
            ctx = FrameCTauContext(tau_val, L2_table[(x_main, y_fr)])
            if y_fr == Fr(10, 1):
                # Also cross-check B1659 determinant law and a0 vs mp.diff once
                Y_chk, Mw_chk, _, _ = ctx.yukawa(Fr(4, 15), Fr(1, 30), 1, 2, return_details=True)
                det_lhs = mp.det(Y_chk)
                pair_tr = mp.fsum((ctx.EPS * ctx.S * Mw_chk.T)[i, i] for i in range(2))
                det_rhs = 4 * mp.det(ctx.S) * mp.det(Mw_chk) * pair_tr
                det_law_err = abs(det_lhs - det_rhs) / abs(det_lhs)
                # Cross-check a0_holo vs mp.diff on holomorphic th1
                al_t, be_t = Fr(3, 10), Fr(7, 30)
                z_t = f2m(al_t) * tau_val + f2m(be_t)
                def _th1_scalar(zz):
                    N_l = 12
                    return -ctx.I * mp.fsum(
                        ((-1) ** n) * mp.exp(ctx.I * mp.pi * tau_val * (n + mp.mpf(1) / 2) ** 2 + ctx.I * mp.pi * (2 * n + 1) * zz)
                        for n in range(-N_l, N_l + 1)
                    )
                a0_diff = 2 * ctx.I * mp.pi * f2m(al_t) + mp.diff(_th1_scalar, z_t) / _th1_scalar(z_t)
                a0_err = abs(a0_holo(al_t, be_t, tau_val) - a0_diff) / abs(a0_diff)
                internal_invariants = {
                    "higgs_nullity_rel_err": m_sci(ctx.nullity_err, 8),
                    "jacobi_quartic_rel_err": m_sci(ctx.jacobi_err, 8),
                    "eta_triple_rel_err": m_sci(ctx.eta_jacobi_err, 8),
                    "B1659_det_law_rel_err": m_sci(det_law_err, 8),
                    "a0_vs_mp_diff_rel_err": m_sci(a0_err, 8),
                }

            y_mats = {}
            y_obs = {}
            for pt in P30:
                a_fr, b_fr = pt
                sec_Y = {}
                sec_U = {}
                sec_sv = {}
                for sec in SECTOR_ORDER:
                    ql, qr = SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]
                    if y_fr == Fr(30, 1):
                        Ym, _, u_d, zf = ctx.yukawa(a_fr, b_fr, ql, qr, return_details=True)
                        is_zero_total_count += sum(1 for v in zf.values() if v)
                        if sec == "up":
                            mx = max(abs(v) for v in u_d.values())
                            P30_u_one_y30[pt] = abs(u_d["1"]) / mx
                    else:
                        Ym = ctx.yukawa(a_fr, b_fr, ql, qr)
                    sec_Y[sec] = Ym
                    U_s, sv_s, _ = svd_asc(Ym)
                    sec_U[sec] = U_s
                    sec_sv[sec] = sv_s
                y_mats[pt] = sec_Y
                y_obs[pt] = observables_from_U_sv(sec_U["up"], sec_sv["up"], sec_U["down"], sec_sv["down"], sec_sv["lep"])
            # Keep raw Y matrices only at y in {3, 5, 10, 20, 30} needed for O4 & O5
            if y_fr in (Fr(3, 1), Fr(5, 1), Fr(10, 1), Fr(20, 1), Fr(30, 1)):
                P30_Y[y_fr] = y_mats
            P30_obs[y_fr] = y_obs

    report["internal_invariants"] = internal_invariants
    print("[Referee] Step 2 done in %ss | det_law_err=%s | nullity_err=%s" % (
        elapsed_sec_str(t_snap),
        internal_invariants["B1659_det_law_rel_err"],
        internal_invariants["higgs_nullity_rel_err"],
    ), flush=True)

    # --------------------------------------------------------------------------
    # MODULE O1 (G1): Exact Tropical Law, 12 Classes, Counterfactual, E3/E4, Level Scan
    # --------------------------------------------------------------------------
    print("[Referee] Module O1: Tropical law, 960 rates, counterfactual, general-N scan...", flush=True)
    t_o1 = time.monotonic_ns()

    RATE_KEYS_10 = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13", "V31")
    RATE_KEYS_9 = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")

    nd_groups = {}
    for pt in P30:
        nda = nd_fr(pt[0])
        nd_groups.setdefault(nda, []).append(pt)
    nd_sorted = sorted(nd_groups.keys())

    exact_12_classes = {}
    all_mult_1_60 = True
    all_v23_law = True
    max_diff_960_y30_40 = mp.mpf(0)
    max_diff_864_y30_40 = mp.mpf(0)
    worst_entry_960 = None

    w_std_pts = 0
    w_inv_pts = 0
    w_nonadd_pts = 0
    w_nonadd_v12_lt_v23_lt_v13_pts = 0

    with mp.workdps(120):
        for nda in nd_sorted:
            pts_c = nd_groups[nda]
            tr = trop_fn(nda)
            v23_law = 2 * abs(nda - Fr(1, 4))
            if tr["V23"] != v23_law:
                all_v23_law = False
            for rk in RATE_KEYS_10:
                if (tr[rk] * 60).denominator != 1:
                    all_mult_1_60 = False
            e12, e23, e13, e31 = tr["V12"], tr["V23"], tr["V13"], tr["V31"]
            if e13 == e12 + e23 and e12 < e23:
                ord_cls = "W_STD_additive"
                w_std_pts += len(pts_c)
            elif e13 == e12 + e23 and e23 < e12:
                ord_cls = "W_INV_additive"
                w_inv_pts += len(pts_c)
            else:
                ord_cls = "W_NONADD"
                w_nonadd_pts += len(pts_c)
                if e12 < e23 < e13:
                    w_nonadd_v12_lt_v23_lt_v13_pts += len(pts_c)

            cls_max_err = mp.mpf(0)
            rep_pt = pts_c[0]
            rep_num_rates = {}
            for pt in pts_c:
                o30 = P30_obs[Fr(30, 1)][pt]
                o40 = P30_obs[Fr(40, 1)][pt]
                for rk in RATE_KEYS_10:
                    nr = obs_rate(o30[rk], o40[rk], mp.mpf(30), mp.mpf(40))
                    err = abs(nr - f2m(tr[rk]))
                    if err > cls_max_err:
                        cls_max_err = err
                    if err > max_diff_960_y30_40:
                        max_diff_960_y30_40 = err
                        worst_entry_960 = {"pt": pt_key(pt), "obs": rk, "exact": fr_str(tr[rk]), "num": m_str(nr, 12), "err": m_sci(err, 6)}
                    if rk in RATE_KEYS_9 and err > max_diff_864_y30_40:
                        max_diff_864_y30_40 = err
                    if pt == rep_pt:
                        rep_num_rates[rk] = m_str(nr, 12)

            exact_12_classes[fr_str(nda)] = {
                "count": len(pts_c),
                "rep_pt": pt_key(rep_pt),
                "heavy_axis": tr["heavy_up"],
                "exact_rates": {rk: fr_str(tr[rk]) for rk in RATE_KEYS_10},
                "V23_law_2_abs_nd_minus_quarter": fr_str(v23_law),
                "ckm_ordering_class": ord_cls,
                "rep_y30_40_num_rates": rep_num_rates,
                "class_max_abs_err_y30_40": m_sci(cls_max_err, 6),
            }

        # B1977 finite-y (y=20->30) benchmark check & 17 rounded classes
        b1977_g1 = 0
        b1977_g2 = 0
        b1977_g3 = 0
        b1977_g4 = 0
        b1977_g5 = 0
        rounded_classes_20_30 = Counter()
        for pt in P30:
            o20 = P30_obs[Fr(20, 1)][pt]
            o30 = P30_obs[Fr(30, 1)][pt]
            r20_30 = {rk: obs_rate(o20[rk], o30[rk], mp.mpf(20), mp.mpf(30)) for rk in RATE_KEYS_9}
            for rk in RATE_KEYS_9:
                if abs(r20_30[rk] * 60 - mp.nint(r20_30[rk] * 60)) / 60 <= mp.mpf(3) / 1000:
                    b1977_g3 += 1
            hier = (
                r20_30["up_m2m3"] >= mp.mpf(1) / 10
                and r20_30["up_m1m3"] >= mp.mpf(2) / 10
                and r20_30["down_m2m3"] >= mp.mpf(1) / 10
                and r20_30["down_m1m3"] >= mp.mpf(2) / 10
            )
            if o30["min_diag"] >= mp.mpf(9) / 10 and hier and min(r20_30["V12"], r20_30["V23"], r20_30["V13"]) < mp.mpf(1) / 10:
                b1977_g5 += 1
            if pt in SLOW_FIVE:
                if hier:
                    b1977_g1 += 1
                if abs(r20_30["V23"] - mp.mpf(1) / 30) < mp.mpf(2) / 1000:
                    b1977_g2 += 1
                if abs(r20_30["lep_m2m3"] - r20_30["down_m2m3"]) > mp.mpf(1) / 100:
                    b1977_g4 += 1
            # 2-decimal rounded signature (pure integer nint(100*r), zero floats!)
            sig = tuple(int(mp.nint(r20_30[rk] * 100)) for rk in RATE_KEYS_9)
            rounded_classes_20_30[sig] += 1

        # E3 and E4 exact sub-lattices at y = 30
        e3_tied_pts = []
        e4_suppressed_pts = []
        for pt in P30:
            _, d_max = ed_split_metrics(P30_obs[Fr(30, 1)][pt])
            if d_max <= mp.mpf(1) / 10:
                e3_tied_pts.append(pt)
            if P30_u_one_y30[pt] <= mp.mpf(10) ** (-10):
                e4_suppressed_pts.append(pt)

    # B1971 Review 86 counterfactual (R86-1): flip s -> -s (c0 -> -c0) in Y_u alone
    cf_pts = [(Fr(7, 30), Fr(19, 30)), (Fr(4, 15), Fr(1, 30))]
    counterfactual_r86 = {}
    with mp.workdps(135):
        cf_snaps = {}
        for y_fr in (Fr(30, 1), Fr(40, 1)):
            tau_v = mp.mpc(f2m(x_main), f2m(y_fr))
            ctx_plus = FrameCTauContext(tau_v, L2_table[(x_main, y_fr)], flip_c0=False)
            ctx_minus = FrameCTauContext(tau_v, L2_table[(x_main, y_fr)], flip_c0=True)
            for pt in cf_pts:
                Uu_flip, svu_flip, _ = svd_asc(ctx_minus.yukawa(pt[0], pt[1], 1, -4))
                Ud_norm, svd_norm, _ = svd_asc(ctx_plus.yukawa(pt[0], pt[1], 1, 2))
                _, sve_norm, _ = svd_asc(ctx_plus.yukawa(pt[0], pt[1], -3, 6))
                cf_snaps[(pt, y_fr)] = observables_from_U_sv(Uu_flip, svu_flip, Ud_norm, svd_norm, sve_norm)
        for pt in cf_pts:
            o30_n, o40_n = P30_obs[Fr(30, 1)][pt], P30_obs[Fr(40, 1)][pt]
            o30_f, o40_f = cf_snaps[(pt, Fr(30, 1))], cf_snaps[(pt, Fr(40, 1))]
            counterfactual_r86[pt_key(pt)] = {
                "shared_Higgs_rates_y30_40": {
                    k: m_str(obs_rate(o30_n[k], o40_n[k], mp.mpf(30), mp.mpf(40)), 10)
                    for k in ("V12", "V23", "V13", "V31")
                },
                "flipped_c0_in_Yu_rates_y30_40": {
                    k: m_str(obs_rate(o30_f[k], o40_f[k], mp.mpf(30), mp.mpf(40)), 10)
                    for k in ("V12", "V23", "V13", "V31")
                },
            }

    # Exact L_2(y) vs clamped L_2(6) comparison on the 5 slow points at y in {20, 30, 40}
    clamped_vs_exact_slow = {}
    with mp.workdps(135):
        clamped_obs = {}
        for y_fr in (Fr(20, 1), Fr(30, 1), Fr(40, 1)):
            tau_v = mp.mpc(f2m(x_main), f2m(y_fr))
            ctx_cl = FrameCTauContext(tau_v, L2_y6)
            for pt in SLOW_FIVE:
                Uu, svu, _ = svd_asc(ctx_cl.yukawa(pt[0], pt[1], 1, -4))
                Ud, svd, _ = svd_asc(ctx_cl.yukawa(pt[0], pt[1], 1, 2))
                _, sve, _ = svd_asc(ctx_cl.yukawa(pt[0], pt[1], -3, 6))
                clamped_obs[(pt, y_fr)] = observables_from_U_sv(Uu, svu, Ud, svd, sve)
        max_rate_shift_20_30 = mp.mpf(0)
        max_rate_shift_30_40 = mp.mpf(0)
        max_rel_prefactor_shift_y30 = mp.mpf(0)
        per_slow = {}
        for pt in SLOW_FIVE:
            shifts_20_30 = {}
            shifts_30_40 = {}
            pref_shift_30 = {}
            for rk in RATE_KEYS_10:
                re_20_30 = obs_rate(P30_obs[Fr(20, 1)][pt][rk], P30_obs[Fr(30, 1)][pt][rk], mp.mpf(20), mp.mpf(30))
                rc_20_30 = obs_rate(clamped_obs[(pt, Fr(20, 1))][rk], clamped_obs[(pt, Fr(30, 1))][rk], mp.mpf(20), mp.mpf(30))
                d23 = abs(re_20_30 - rc_20_30)
                max_rate_shift_20_30 = max(max_rate_shift_20_30, d23)
                shifts_20_30[rk] = m_sci(d23, 6)

                re_30_40 = obs_rate(P30_obs[Fr(30, 1)][pt][rk], P30_obs[Fr(40, 1)][pt][rk], mp.mpf(30), mp.mpf(40))
                rc_30_40 = obs_rate(clamped_obs[(pt, Fr(30, 1))][rk], clamped_obs[(pt, Fr(40, 1))][rk], mp.mpf(30), mp.mpf(40))
                d34 = abs(re_30_40 - rc_30_40)
                max_rate_shift_30_40 = max(max_rate_shift_30_40, d34)
                shifts_30_40[rk] = m_sci(d34, 6)

                rel_p = abs(P30_obs[Fr(30, 1)][pt][rk] - clamped_obs[(pt, Fr(30, 1))][rk]) / abs(P30_obs[Fr(30, 1)][pt][rk])
                max_rel_prefactor_shift_y30 = max(max_rel_prefactor_shift_y30, rel_p)
                pref_shift_30[rk] = m_sci(rel_p, 6)
            per_slow[pt_key(pt)] = {
                "rate_shift_y20_30": shifts_20_30,
                "rate_shift_y30_40": shifts_30_40,
                "rel_observable_shift_y30": pref_shift_30,
            }
        clamped_vs_exact_slow = {
            "max_rate_shift_y20_30": m_sci(max_rate_shift_20_30, 8),
            "max_rate_shift_y30_40": m_sci(max_rate_shift_30_40, 8),
            "max_rel_observable_shift_y30": m_sci(max_rel_prefactor_shift_y30, 8),
            "per_slow_point": per_slow,
        }

    # General-level N anti-sharpshooting scan (14 levels)
    scan_levels = (5, 6, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)
    level_scan = {}
    formula_all_match_unconstrained = True
    for N_lv in scan_levels:
        E_N, P_N = build_level_N_sets(N_lv)
        if N_lv % 4 == 0:
            law_uncon = Fr(0, 1)
        elif N_lv % 4 == 2:
            law_uncon = Fr(1, N_lv)
        else:
            law_uncon = Fr(1, 2 * N_lv)
        min_2abs_uncon = min(2 * abs(nd_fr(p[0]) - Fr(1, 4)) for p in E_N)
        if min_2abs_uncon != law_uncon:
            formula_all_match_unconstrained = False

        # Evaluate exact tropical rates across P_N (act-line lift if 5 | N else E_N)
        # Note: at N=6, u = -4 == 2 = d (mod 6), so Y_u and Y_d share left basis identically -> V = I (mixing = 0)
        e23_vals = []
        aligned_cnt = 0
        hier_cnt = 0
        ed2_split_cnt = 0
        slow_lt_1_10_cnt = 0
        viable_all4_cnt = 0
        min_v23_viable = None
        for p in P_N:
            nda = nd_fr(p[0])
            tr = trop_fn(nda)
            # Check exact mod-N lens tie for up == down (e.g. N=6)
            up_eq_dn = ((-4) % N_lv == 2 % N_lv)
            is_aligned = True if up_eq_dn else (tr["aligned"] and nda != Fr(1, 4) and nda != Fr(1, 2) and nda != Fr(0, 1))
            # Careful: a = 0 or a = 1/2 or a = 1/4 can be unaligned / degenerate
            if is_aligned:
                aligned_cnt += 1
            is_hier = (tr["up_m2m3"] > 0 and tr["up_m1m3"] > tr["up_m2m3"] and tr["down_m2m3"] > 0 and tr["down_m1m3"] > tr["down_m2m3"])
            if is_hier:
                hier_cnt += 1
            is_ed2 = (tr["lep_m2m3"] != tr["down_m2m3"])
            if is_ed2:
                ed2_split_cnt += 1
            v23_r = None if up_eq_dn else (2 * abs(nda - Fr(1, 4)))
            if v23_r is not None:
                e23_vals.append(v23_r)
            is_slow = (v23_r is not None and Fr(0, 1) < v23_r < Fr(1, 10))
            if is_slow:
                slow_lt_1_10_cnt += 1
            if is_aligned and is_hier and is_ed2 and is_slow:
                viable_all4_cnt += 1
                if min_v23_viable is None or v23_r < min_v23_viable:
                    min_v23_viable = v23_r

        min_2abs_PN = min(2 * abs(nd_fr(p[0]) - Fr(1, 4)) for p in P_N)
        level_scan[str(N_lv)] = {
            "N": N_lv,
            "E_N_size": len(E_N),
            "P_N_size": len(P_N),
            "P_N_kind": "K5_lift" if N_lv % 5 == 0 else "E_N_prim",
            "law_e_min_unconstrained": fr_str(law_uncon),
            "actual_min_2abs_E_N": fr_str(min_2abs_uncon),
            "actual_min_2abs_P_N": fr_str(min_2abs_PN),
            "aligned_count": aligned_cnt,
            "both_quark_hier_count": hier_cnt,
            "ed_2nd_gen_split_count": ed2_split_cnt,
            "slow_v23_lt_1_10_count": slow_lt_1_10_cnt,
            "viable_all4_count": viable_all4_cnt,
            "min_v23_among_viable": fr_str(min_v23_viable) if min_v23_viable is not None else None,
        }

    report["O1_tropical"] = {
        "n_points_P30": len(P30),
        "n_nd_classes": len(nd_sorted),
        "nd_values": [fr_str(v) for v in nd_sorted],
        "is_zero_channel_cancellations_total": is_zero_total_count,
        "all_960_exact_multiples_of_1_60": all_mult_1_60,
        "all_96_V23_equals_2_abs_nd_minus_quarter": all_v23_law,
        "max_abs_err_960_rates_y30_40": m_sci(max_diff_960_y30_40, 8),
        "max_abs_err_864_rates_y30_40": m_sci(max_diff_864_y30_40, 8),
        "worst_entry_960_y30_40": worst_entry_960,
        "exact_12_classes": exact_12_classes,
        "ckm_ordering_census": {
            "W_STD_additive_pts": w_std_pts,
            "W_INV_additive_pts": w_inv_pts,
            "W_NONADD_pts": w_nonadd_pts,
            "W_NONADD_with_V12_lt_V23_lt_V13_pts": w_nonadd_v12_lt_v23_lt_v13_pts,
        },
        "B1976_E3_E4_sublattices": {
            "E3_tied_count": len(e3_tied_pts),
            "E3_split_count": len(P30) - len(e3_tied_pts),
            "E3_tied_points": [pt_key(p) for p in e3_tied_pts],
            "E4_suppressed_count": len(e4_suppressed_pts),
            "E4_nonzero_gt_1e_10_count": len(P30) - len(e4_suppressed_pts),
            "E4_suppressed_points": [pt_key(p) for p in e4_suppressed_pts],
        },
        "B1977_y20_30_reproduction": {
            "G1_slow_hier_of_5": b1977_g1,
            "G2_slow_V23_near_1_30_of_5": b1977_g2,
            "G3_rates_within_3e_3_of_1_60_of_864": b1977_g3,
            "G4_slow_lep_neq_down_m2m3_of_5": b1977_g4,
            "G5_aligned_hier_slow_lt_1_10_of_96": b1977_g5,
            "rounded_2dp_class_count_y20_30": len(rounded_classes_20_30),
        },
        "B1971_R86_counterfactual_flip_c0_Yu": counterfactual_r86,
        "exact_L2_vs_clamped_L2_6_slow5": clamped_vs_exact_slow,
        "general_level_N_scan": {
            "unconstrained_law_matches_all_14": formula_all_match_unconstrained,
            "levels": level_scan,
        },
        "elapsed_sec": elapsed_sec_str(t_o1),
    }
    print("[Referee] Module O1 done in %ss | max_960_err=%s | E3_tied=%d | E4_supp=%d" % (
        report["O1_tropical"]["elapsed_sec"], m_sci(max_diff_960_y30_40, 4), len(e3_tied_pts), len(e4_suppressed_pts)), flush=True)

    # --------------------------------------------------------------------------
    # MODULE O2 (G2): Moderate-Height Survival, 14-Height Trajectories, Column Spread
    # --------------------------------------------------------------------------
    print("[Referee] Module O2: 96-pt survival, 14-height trajectories, column spread...", flush=True)
    t_o2 = time.monotonic_ns()

    survival_96 = {}
    for y_fr in (Fr(2, 1), Fr(3, 1), Fr(5, 1), Fr(10, 1), Fr(20, 1), Fr(30, 1), Fr(40, 1)):
        c_align = 0
        c_hier = 0
        c_ed2 = 0
        c_ed_any = 0
        c_all3 = 0
        ord_cnt = Counter()
        for pt in P30:
            ob = P30_obs[y_fr][pt]
            al_ok = ob["min_diag"] >= mp.mpf(9) / 10
            hi_ok = (
                ob["up_m2m3"] < mp.mpf(1) / 2
                and ob["up_m1m3"] < mp.mpf(1) / 10
                and ob["down_m2m3"] < mp.mpf(1) / 2
                and ob["down_m1m3"] < mp.mpf(1) / 10
            )
            r2, rmax = ed_split_metrics(ob)
            ed2_ok = r2 > mp.mpf(1) / 10
            ed_any_ok = rmax > mp.mpf(1) / 10
            if al_ok:
                c_align += 1
            if hi_ok:
                c_hier += 1
            if ed2_ok:
                c_ed2 += 1
            if ed_any_ok:
                c_ed_any += 1
            if al_ok and hi_ok and ed2_ok:
                c_all3 += 1
            ord_cnt[ckm_mag_order_label(ob)] += 1
        survival_96[fr_str(y_fr)] = {
            "aligned_ge_0p9": c_align,
            "both_quark_hier": c_hier,
            "ed_2nd_gen_split_gt_0p1": c_ed2,
            "ed_any_split_gt_0p1": c_ed_any,
            "all_three": c_all3,
            "ckm_magnitude_ordering": dict(sorted(ord_cnt.items())),
        }

    # 14-height trajectories for (4/15, 1/30), (7/15, 1/10), plus all 12 nd representatives + slow 5
    rep_pts_12 = [nd_groups[nda][0] for nda in nd_sorted]
    traj_pts = sorted(set([(Fr(4, 15), Fr(1, 30)), (Fr(7, 15), Fr(1, 10))] + rep_pts_12 + list(SLOW_FIVE)))
    traj_obs = {pt: {} for pt in traj_pts}
    for y_fr in heights_14:
        if y_fr in P30_obs:
            for pt in traj_pts:
                traj_obs[pt][y_fr] = P30_obs[y_fr][pt]
        else:
            dps_t = 65 if y_fr <= Fr(10, 1) else 95
            with mp.workdps(dps_t):
                tau_v = mp.mpc(f2m(x_main), f2m(y_fr))
                ctx = FrameCTauContext(tau_v, L2_table[(x_main, y_fr)])
                for pt in traj_pts:
                    Uu, svu, _ = svd_asc(ctx.yukawa(pt[0], pt[1], 1, -4))
                    Ud, svd, _ = svd_asc(ctx.yukawa(pt[0], pt[1], 1, 2))
                    _, sve, _ = svd_asc(ctx.yukawa(pt[0], pt[1], -3, 6))
                    traj_obs[pt][y_fr] = observables_from_U_sv(Uu, svu, Ud, svd, sve)

    # Format detailed 14-height trajectories + O(1) prefactors + local rates for the 2 featured points
    featured_trajectories = {}
    rate_windows = [(Fr(2, 1), Fr(3, 1)), (Fr(3, 1), Fr(5, 1)), (Fr(5, 1), Fr(8, 1)),
                    (Fr(8, 1), Fr(10, 1)), (Fr(20, 1), Fr(30, 1)), (Fr(30, 1), Fr(40, 1))]
    with mp.workdps(120):
        for pt in ((Fr(4, 15), Fr(1, 30)), (Fr(7, 15), Fr(1, 10))):
            tr_ex = trop_fn(nd_fr(pt[0]))
            by_y = {}
            for y_fr in heights_14:
                ob = traj_obs[pt][y_fr]
                eps_y = mp.exp(-mp.pi * f2m(y_fr))
                r2, rmax = ed_split_metrics(ob)
                by_y[fr_str(y_fr)] = {
                    "obs": {k: m_str(ob[k], 14) for k in RATE_KEYS_10 + ("J_CP", "min_diag")},
                    "O1_prefactors": {k: m_str(ob[k] * (eps_y ** (-f2m(tr_ex[k]))), 12) for k in RATE_KEYS_10},
                    "ed_2nd_gen_ln": m_str(r2, 10),
                    "ckm_order": ckm_mag_order_label(ob),
                }
            loc_rates = {}
            for y1, y2 in rate_windows:
                loc_rates["%s->%s" % (fr_str(y1), fr_str(y2))] = {
                    k: m_str(obs_rate(traj_obs[pt][y1][k], traj_obs[pt][y2][k], f2m(y1), f2m(y2)), 10)
                    for k in RATE_KEYS_10
                }
            featured_trajectories[pt_key(pt)] = {
                "nd_a": fr_str(nd_fr(pt[0])),
                "exact_rates": {k: fr_str(tr_ex[k]) for k in RATE_KEYS_10},
                "by_height": by_y,
                "local_rates": loc_rates,
            }

    # Column spreads across x in {0, 13/100, 31/100, 1/2} at y in {2, 4, 10, 20} for (4/15, 1/30) and (7/15, 1/10)
    all_cols = [Fr(0, 1), Fr(13, 100), Fr(31, 100), Fr(1, 2)]
    col_pts = [(Fr(4, 15), Fr(1, 30)), (Fr(7, 15), Fr(1, 10))]
    col_data = {pt: {y_fr: {} for y_fr in col_heights} for pt in col_pts}
    for x_fr in all_cols:
        for y_fr in col_heights:
            if x_fr == x_main:
                for pt in col_pts:
                    col_data[pt][y_fr][x_fr] = traj_obs[pt][y_fr]
            else:
                dps_c = 65 if y_fr <= Fr(10, 1) else 105
                with mp.workdps(dps_c):
                    tau_v = mp.mpc(f2m(x_fr), f2m(y_fr))
                    ctx = FrameCTauContext(tau_v, L2_table[(x_fr, y_fr)])
                    for pt in col_pts:
                        Uu, svu, _ = svd_asc(ctx.yukawa(pt[0], pt[1], 1, -4))
                        Ud, svd, _ = svd_asc(ctx.yukawa(pt[0], pt[1], 1, 2))
                        _, sve, _ = svd_asc(ctx.yukawa(pt[0], pt[1], -3, 6))
                        col_data[pt][y_fr][x_fr] = observables_from_U_sv(Uu, svu, Ud, svd, sve)

    column_spreads = {}
    with mp.workdps(80):
        for pt in col_pts:
            by_y = {}
            for y_fr in col_heights:
                spread_map = {}
                for k in RATE_KEYS_10:
                    vals = [col_data[pt][y_fr][xf][k] for xf in all_cols]
                    vmin, vmax = min(vals), max(vals)
                    spread_map[k] = {
                        "min": m_str(vmin, 12),
                        "max": m_str(vmax, 12),
                        "rel_spread": m_sci((vmax - vmin) / vmin if vmin > 0 else mp.mpf(0), 6),
                        "by_x": {fr_str(xf): m_str(col_data[pt][y_fr][xf][k], 12) for xf in all_cols},
                    }
                by_y[fr_str(y_fr)] = spread_map
            column_spreads[pt_key(pt)] = by_y

    report["O2_moderate_height"] = {
        "survival_96_points": survival_96,
        "featured_14height_trajectories": featured_trajectories,
        "column_spreads": column_spreads,
        "elapsed_sec": elapsed_sec_str(t_o2),
    }
    print("[Referee] Module O2 done in %ss | y=2 all3=%d | y=3 all3=%d | y=10 all3=%d" % (
        report["O2_moderate_height"]["elapsed_sec"],
        survival_96["2"]["all_three"], survival_96["3"]["all_three"], survival_96["10"]["all_three"]), flush=True)

    # --------------------------------------------------------------------------
    # MODULE O3 (G3): Exact Joint SL(2, Z) & M = [[2,1],[1,1]] Covariance
    # --------------------------------------------------------------------------
    print("[Referee] Module O3: Pointwise joint covariance under T, S, M + controls...", flush=True)
    t_o3 = time.monotonic_ns()

    o3_test_pts = [
        (Fr(4, 15), Fr(1, 30)),
        (Fr(7, 30), Fr(19, 30)),
        (Fr(7, 15), Fr(1, 10)),
        (Fr(1, 5), Fr(7, 30)),
    ]

    def act_w_right_inv(pt, g):
        a, b = pt
        ga, gb, gc, gd = g
        # (a, b) * [[gd, -gb], [-gc, ga]]
        return ((gd * a - gc * b) % 1, (-gb * a + ga * b) % 1)

    def act_w_right_wrong(pt, g):
        a, b = pt
        ga, gb, gc, gd = g
        # Wrong action: (a, b) * [[ga, gb], [gc, gd]]
        return ((ga * a + gc * b) % 1, (gb * a + gd * b) % 1)

    O3_OBS_KEYS = RATE_KEYS_10 + ("J_CP",)

    def max_rel_obs_diff(ob1, ob2):
        worst = mp.mpf(0)
        for k in O3_OBS_KEYS:
            v1, v2 = ob1[k], ob2[k]
            denom = max(abs(v1), abs(v2), mp.mpf(10) ** (-40))
            d = abs(v1 - v2) / denom
            if d > worst:
                worst = d
        return worst

    o3_results = {}
    max_joint_cov_err = mp.mpf(0)
    max_fixed_L2_drift = mp.mpf(0)
    min_fixed_L2_S_M_drift = None
    max_wrong_w_drift = mp.mpf(0)
    min_wrong_w_T_M_drift = None
    min_fixed_tau_M_drift = None

    with mp.workdps(75):
        tau_cases = {
            "tau0_-9_10+6_5i": (mp.mpc(f2m(Fr(-9, 10)), f2m(Fr(6, 5))), res_tau0["L2"]),
            "tau1_13_100+2i": (mp.mpc(f2m(Fr(13, 100)), f2m(Fr(2, 1))), L2_table[(Fr(13, 100), Fr(2, 1))]),
        }
        for tname, (tau_b, L2_b) in tau_cases.items():
            ctx_b = FrameCTauContext(tau_b, L2_b)
            base_obs = {}
            for pt in o3_test_pts:
                Uu, svu, _ = svd_asc(ctx_b.yukawa(pt[0], pt[1], 1, -4))
                Ud, svd, _ = svd_asc(ctx_b.yukawa(pt[0], pt[1], 1, 2))
                _, sve, _ = svd_asc(ctx_b.yukawa(pt[0], pt[1], -3, 6))
                base_obs[pt] = observables_from_U_sv(Uu, svu, Ud, svd, sve)

            t_res = {}
            for gname, gmat in gammas.items():
                ga, gb, gc, gd = gmat
                gtau = (ga * tau_b + gb) / (gc * tau_b + gd)
                L2_exact = L2_b + mp.log(abs(gc * tau_b + gd))
                ctx_exact = FrameCTauContext(gtau, L2_exact)
                ctx_fixed_L2 = FrameCTauContext(gtau, L2_b)

                worst_exact = mp.mpf(0)
                worst_fixed_L2 = mp.mpf(0)
                worst_wrong_w = mp.mpf(0)
                worst_fixed_tau = mp.mpf(0)
                for pt in o3_test_pts:
                    pt_cov = act_w_right_inv(pt, gmat)
                    pt_bad = act_w_right_wrong(pt, gmat)

                    # Joint exact covariance
                    Uu, svu, _ = svd_asc(ctx_exact.yukawa(pt_cov[0], pt_cov[1], 1, -4))
                    Ud, svd, _ = svd_asc(ctx_exact.yukawa(pt_cov[0], pt_cov[1], 1, 2))
                    _, sve, _ = svd_asc(ctx_exact.yukawa(pt_cov[0], pt_cov[1], -3, 6))
                    d_ex = max_rel_obs_diff(base_obs[pt], observables_from_U_sv(Uu, svu, Ud, svd, sve))
                    worst_exact = max(worst_exact, d_ex)

                    # Control 1 (PF3): Fixed L2
                    Uu, svu, _ = svd_asc(ctx_fixed_L2.yukawa(pt_cov[0], pt_cov[1], 1, -4))
                    Ud, svd, _ = svd_asc(ctx_fixed_L2.yukawa(pt_cov[0], pt_cov[1], 1, 2))
                    _, sve, _ = svd_asc(ctx_fixed_L2.yukawa(pt_cov[0], pt_cov[1], -3, 6))
                    d_fl = max_rel_obs_diff(base_obs[pt], observables_from_U_sv(Uu, svu, Ud, svd, sve))
                    worst_fixed_L2 = max(worst_fixed_L2, d_fl)

                    # Control 2 (PF4): Wrong point action w * gamma
                    Uu, svu, _ = svd_asc(ctx_exact.yukawa(pt_bad[0], pt_bad[1], 1, -4))
                    Ud, svd, _ = svd_asc(ctx_exact.yukawa(pt_bad[0], pt_bad[1], 1, 2))
                    _, sve, _ = svd_asc(ctx_exact.yukawa(pt_bad[0], pt_bad[1], -3, 6))
                    d_ww = max_rel_obs_diff(base_obs[pt], observables_from_U_sv(Uu, svu, Ud, svd, sve))
                    worst_wrong_w = max(worst_wrong_w, d_ww)

                    # Control 3 (B1978 caveat): Fixed tau, move w -> w * gamma^{-1}
                    Uu, svu, _ = svd_asc(ctx_b.yukawa(pt_cov[0], pt_cov[1], 1, -4))
                    Ud, svd, _ = svd_asc(ctx_b.yukawa(pt_cov[0], pt_cov[1], 1, 2))
                    _, sve, _ = svd_asc(ctx_b.yukawa(pt_cov[0], pt_cov[1], -3, 6))
                    d_ft = max_rel_obs_diff(base_obs[pt], observables_from_U_sv(Uu, svu, Ud, svd, sve))
                    worst_fixed_tau = max(worst_fixed_tau, d_ft)

                max_joint_cov_err = max(max_joint_cov_err, worst_exact)
                if gname in ("S", "M"):
                    max_fixed_L2_drift = max(max_fixed_L2_drift, worst_fixed_L2)
                    min_fixed_L2_S_M_drift = worst_fixed_L2 if min_fixed_L2_S_M_drift is None else min(min_fixed_L2_S_M_drift, worst_fixed_L2)
                if gname in ("T", "M"):
                    max_wrong_w_drift = max(max_wrong_w_drift, worst_wrong_w)
                    min_wrong_w_T_M_drift = worst_wrong_w if min_wrong_w_T_M_drift is None else min(min_wrong_w_T_M_drift, worst_wrong_w)
                if gname == "M":
                    min_fixed_tau_M_drift = worst_fixed_tau if min_fixed_tau_M_drift is None else min(min_fixed_tau_M_drift, worst_fixed_tau)

                t_res[gname] = {
                    "exact_joint_max_rel_err": m_sci(worst_exact, 8),
                    "fixed_L2_control_max_rel_drift": m_sci(worst_fixed_L2, 8),
                    "wrong_w_gamma_control_max_rel_drift": m_sci(worst_wrong_w, 8),
                    "fixed_tau_B1978_control_max_rel_drift": m_sci(worst_fixed_tau, 8),
                }
            o3_results[tname] = t_res

    report["O3_joint_covariance"] = {
        "test_points": [pt_key(p) for p in o3_test_pts],
        "max_exact_joint_cov_rel_err": m_sci(max_joint_cov_err, 8),
        "by_tau": o3_results,
        "elapsed_sec": elapsed_sec_str(t_o3),
    }
    print("[Referee] Module O3 done in %ss | max_joint_cov_err=%s" % (
        report["O3_joint_covariance"]["elapsed_sec"], m_sci(max_joint_cov_err, 4)), flush=True)

    # --------------------------------------------------------------------------
    # MODULE O4 (G4): Exact 8-Orbit Algebraic Classification & 12-Point Orbit Gramians (mp.eigh)
    # --------------------------------------------------------------------------
    print("[Referee] Module O4: 8 M-orbits, Gramians (mp.eigh), coherent sums...", flush=True)
    t_o4 = time.monotonic_ns()

    def act_M_fwd(p):
        return ((2 * p[0] + p[1]) % 1, (p[0] + p[1]) % 1)

    seen_orb = set()
    orbits = []
    for p in P30:
        if p in seen_orb:
            continue
        orb = [p]
        cur = act_M_fwd(p)
        while cur != p:
            orb.append(cur)
            cur = act_M_fwd(cur)
        seen_orb.update(orb)
        orbits.append(orb)
    assert len(orbits) == 8 and all(len(o) == 12 for o in orbits)

    # Exact CRT classification: P_30 = K_5^* x E[2]_prim x E[3]_prim
    # For w in P_30, w_5 = 6*w (Wait: 6 == 1 mod 5, 0 mod 6, so 6*w mod 1 = w_5!)
    # w_2 = 15*w (15 == 1 mod 2, 0 mod 3, 0 mod 5 -> 15*w mod 1 = w_2!)
    # w_3 = 10*w (10 == 1 mod 3, 0 mod 2, 0 mod 5 -> 10*w mod 1 = w_3!)
    MARK_5 = {(Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))}
    orbit_algebra = []
    slow_mults = []
    for idx, orb in enumerate(orbits):
        w5_set = sorted({((6 * p[0]) % 1, (6 * p[1]) % 1) for p in orb})
        w2_set = sorted({((15 * p[0]) % 1, (15 * p[1]) % 1) for p in orb})
        w3_set = sorted({((10 * p[0]) % 1, (10 * p[1]) % 1) for p in orb})
        is_mark = set(w5_set) == MARK_5
        a3_zero_cnt = sum(1 for (a3, _) in w3_set if a3 == 0)
        e3_orb_type = "Orbit_A_a3_nonzero_4of4" if a3_zero_cnt == 0 else "Orbit_B_a3_zero_2of4"
        slow_cnt = sum(1 for p in orb if 2 * abs(nd_fr(p[0]) - Fr(1, 4)) == Fr(1, 30))
        lt_q_cnt = sum(1 for p in orb if nd_fr(p[0]) < Fr(1, 4))
        gt_q_cnt = sum(1 for p in orb if nd_fr(p[0]) > Fr(1, 4))
        slow_mults.append(slow_cnt)
        orbit_algebra.append({
            "orbit_id": "O%d" % (idx + 1),
            "rep_pt": pt_key(orb[0]),
            "size": len(orb),
            "family": "MARK" if is_mark else "TWIN",
            "w5_orbit": [pt_key(q) for q in w5_set],
            "w2_orbit_size": len(w2_set),
            "w3_orbit_size": len(w3_set),
            "e3_orbit_type": e3_orb_type,
            "slow_V23_1_30_count": slow_cnt,
            "nd_lt_quarter_count": lt_q_cnt,
            "nd_gt_quarter_count": gt_q_cnt,
            "crosses_quarter": (lt_q_cnt > 0 and gt_q_cnt > 0),
        })

    # Evaluate Hermitian Gramian H_{L,f}^{(O)} (via mp.eigh) and coherent sum Y_bar^{(O)} at y in {3, 5, 10, 20, 30}
    orb_heights = (Fr(3, 1), Fr(5, 1), Fr(10, 1), Fr(20, 1), Fr(30, 1))
    orbit_gramian_data = {}
    orbit_coherent_data = {}
    max_orb_unitarity_err = mp.mpf(0)
    max_orb_M_invariance_err = mp.mpf(0)

    for idx, orb in enumerate(orbits):
        oid = "O%d" % (idx + 1)
        orb_shifted = [act_M_fwd(p) for p in orb]
        g_by_y = {}
        c_by_y = {}
        g_raw = {}
        c_raw = {}
        for y_fr in orb_heights:
            with mp.workdps(dps_for_y[y_fr]):
                ym = P30_Y[y_fr]
                U_g = {}
                sv_g = {}
                U_c = {}
                sv_c = {}
                for sec in SECTOR_ORDER:
                    Y_list = [ym[p][sec] for p in orb]
                    H_g, U_s, sv_s, _ = gramian_eigh_asc(Y_list)
                    U_g[sec] = U_s
                    sv_g[sec] = sv_s
                    # M-invariance check on w -> M w (reordered sum)
                    H_sh, _, _, _ = gramian_eigh_asc([ym[p][sec] for p in orb_shifted])
                    m_err = mp.norm(H_g - H_sh) / mp.norm(H_g)
                    max_orb_M_invariance_err = max(max_orb_M_invariance_err, m_err)
                    # Coherent sum
                    Y_bar = mp.zeros(3, 3)
                    for Yk in Y_list:
                        Y_bar += Yk
                    Y_bar = Y_bar / len(Y_list)
                    _, U_cs, sv_cs, _ = gramian_eigh_asc([Y_bar])
                    U_c[sec] = U_cs
                    sv_c[sec] = sv_cs

                ob_g = observables_from_U_sv(U_g["up"], sv_g["up"], U_g["down"], sv_g["down"], sv_g["lep"])
                ob_c = observables_from_U_sv(U_c["up"], sv_c["up"], U_c["down"], sv_c["down"], sv_c["lep"])
                max_orb_unitarity_err = max(max_orb_unitarity_err, ob_g["unitarity_err"], ob_c["unitarity_err"])
                g_raw[y_fr] = ob_g
                c_raw[y_fr] = ob_c
                g_by_y[fr_str(y_fr)] = {k: m_str(ob_g[k], 14) for k in RATE_KEYS_10 + ("J_CP", "min_diag")}
                c_by_y[fr_str(y_fr)] = {k: m_str(ob_c[k], 14) for k in RATE_KEYS_10 + ("J_CP", "min_diag")}

        with mp.workdps(120):
            def fmt_rate(v1, v2):
                rv = obs_rate(v1, v2, mp.mpf(20), mp.mpf(30))
                return None if rv is None else m_str(rv, 10)
            g_rates_20_30 = {k: fmt_rate(g_raw[Fr(20, 1)][k], g_raw[Fr(30, 1)][k]) for k in RATE_KEYS_10}
            c_rates_20_30 = {k: fmt_rate(c_raw[Fr(20, 1)][k], c_raw[Fr(30, 1)][k]) for k in RATE_KEYS_10}
        orbit_gramian_data[oid] = {"by_height": g_by_y, "rates_y20_30": g_rates_20_30}
        orbit_coherent_data[oid] = {"by_height": c_by_y, "rates_y20_30": c_rates_20_30}

    report["O4_orbits_and_gramians"] = {
        "n_orbits": len(orbits),
        "orbit_sizes": [len(o) for o in orbits],
        "slow_multiplicities_sorted_desc": sorted(slow_mults, reverse=True),
        "all_8_orbits_cross_quarter": all(x["crosses_quarter"] for x in orbit_algebra),
        "algebraic_classification": orbit_algebra,
        "max_ckm_unitarity_err": m_sci(max_orb_unitarity_err, 8),
        "max_M_action_invariance_err": m_sci(max_orb_M_invariance_err, 8),
        "orbit_gramians_eigh": orbit_gramian_data,
        "orbit_coherent_sums": orbit_coherent_data,
        "elapsed_sec": elapsed_sec_str(t_o4),
    }
    print("[Referee] Module O4 done in %ss | slow_mults=%s | max_unit_err=%s | max_M_err=%s" % (
        report["O4_orbits_and_gramians"]["elapsed_sec"],
        sorted(slow_mults, reverse=True),
        m_sci(max_orb_unitarity_err, 4),
        m_sci(max_orb_M_invariance_err, 4),
    ), flush=True)

    # --------------------------------------------------------------------------
    # MODULE O5 (G5): P-845 Group-Theoretic Lens Census (N=1..60) & Shell Gramians
    # --------------------------------------------------------------------------
    print("[Referee] Module O5: N=1..60 lens census & E6/P30/K5 shell Gramians...", flush=True)
    t_o5 = time.monotonic_ns()

    SEC_PAIRS = {s: (SIXY[SECTORS[s][0]], SIXY[SECTORS[s][1]]) for s in SECTOR_ORDER}

    def unit_tie_mod_N(N_val, p, q):
        units_N = [k for k in range(1, N_val) if gcd(k, N_val) == 1]
        for k in units_N:
            a = ((k * p[0]) % N_val, (k * p[1]) % N_val)
            if a == (q[0] % N_val, q[1] % N_val):
                return "k=%d" % k
            if a == (q[1] % N_val, q[0] % N_val):
                return "k=%d_swapped" % k
        return None

    census_1_60 = {}
    zero_tie_levels = []
    zero_tie_div_by_5 = []
    zero_tie_div_by_5_and_3 = []
    for N_val in range(1, 61):
        ties = {}
        for i_s, s1 in enumerate(SECTOR_ORDER):
            for s2 in SECTOR_ORDER[i_s + 1:]:
                t_rel = unit_tie_mod_N(N_val, SEC_PAIRS[s1], SEC_PAIRS[s2])
                if t_rel is not None:
                    ties["%s~%s" % (s1, s2)] = t_rel
        # Order collapses via gcd(6Y, N)
        lep_order_collapse = gcd(3, N_val)  # 3 divides both L=-3 and e=6 -> collapses order-3m leptons by factor 3!
        down_R_collapse = gcd(2, N_val)
        up_R_collapse = gcd(4, N_val)
        if not ties:
            zero_tie_levels.append(N_val)
            if N_val % 5 == 0:
                zero_tie_div_by_5.append(N_val)
                if N_val % 3 == 0:
                    zero_tie_div_by_5_and_3.append(N_val)
        census_1_60[str(N_val)] = {
            "unit_ties": ties,
            "n_unit_ties": len(ties),
            "lep_gcd_collapse_factor": lep_order_collapse,
            "down_R_gcd_factor": down_R_collapse,
            "up_R_gcd_factor": up_R_collapse,
            "carries_K5": (N_val % 5 == 0),
        }

    # Head-to-head Shell Gramians at y in {3, 10, 20, 30} for E6 (24), P30 (96), K5 (4)
    shell_heights = (Fr(3, 1), Fr(10, 1), Fr(20, 1), Fr(30, 1))
    shells_data = {"E6_prim_24": {}, "P30_96": {}, "K5_star_4": {}}
    shells_raw = {"E6_prim_24": {}, "P30_96": {}, "K5_star_4": {}}
    k5_pointwise_max_ed_tie = mp.mpf(0)
    k5_left_gram_vs_right_gram_ed_err = mp.mpf(0)
    k5_left_gram_ed_split = {}

    for y_fr in shell_heights:
        with mp.workdps(dps_for_y[y_fr]):
            tau_v = mp.mpc(f2m(x_main), f2m(y_fr))
            ctx = FrameCTauContext(tau_v, L2_table[(x_main, y_fr)])

            # P30 (reuse cached matrices!)
            U_p, sv_p = {}, {}
            for sec in SECTOR_ORDER:
                _, U_p[sec], sv_p[sec], _ = gramian_eigh_asc([P30_Y[y_fr][p][sec] for p in P30])
            ob_p = observables_from_U_sv(U_p["up"], sv_p["up"], U_p["down"], sv_p["down"], sv_p["lep"])
            shells_raw["P30_96"][y_fr] = ob_p
            shells_data["P30_96"][fr_str(y_fr)] = {k: m_str(ob_p[k], 14) for k in RATE_KEYS_10 + ("J_CP", "min_diag")}

            # E6 (24 pts)
            E6_Y = {sec: [ctx.yukawa(p[0], p[1], SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]) for p in E6] for sec in SECTOR_ORDER}
            U_e6, sv_e6 = {}, {}
            for sec in SECTOR_ORDER:
                _, U_e6[sec], sv_e6[sec], _ = gramian_eigh_asc(E6_Y[sec])
            ob_e6 = observables_from_U_sv(U_e6["up"], sv_e6["up"], U_e6["down"], sv_e6["down"], sv_e6["lep"])
            shells_raw["E6_prim_24"][y_fr] = ob_e6
            shells_data["E6_prim_24"][fr_str(y_fr)] = {k: m_str(ob_e6[k], 14) for k in RATE_KEYS_10 + ("J_CP", "min_diag")}

            # K5* (4 pts): check pointwise e=d tie AND Left-Gramian splitting vs Right-Gramian tie
            K5_Y = {sec: [ctx.yukawa(p[0], p[1], SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]) for p in K5] for sec in SECTOR_ORDER}
            for k_idx in range(len(K5)):
                _, svd_k, _ = svd_asc(K5_Y["down"][k_idx])
                _, sve_k, _ = svd_asc(K5_Y["lep"][k_idx])
                d_tie = max(
                    abs(mp.log((sve_k[1] / sve_k[2]) / (svd_k[1] / svd_k[2]))),
                    abs(mp.log((sve_k[0] / sve_k[2]) / (svd_k[0] / svd_k[2]))),
                )
                k5_pointwise_max_ed_tie = max(k5_pointwise_max_ed_tie, d_tie)

            U_k5, sv_k5 = {}, {}
            for sec in SECTOR_ORDER:
                _, U_k5[sec], sv_k5[sec], _ = gramian_eigh_asc(K5_Y[sec])
            # Also check Right-Gramian of down vs Left-Gramian of lep!
            _, _, sv_k5_down_R, _ = right_gramian_eigh_asc(K5_Y["down"])
            rg_diff = max(
                abs((sv_k5["lep"][1] / sv_k5["lep"][2]) - (sv_k5_down_R[1] / sv_k5_down_R[2])) / (sv_k5["lep"][1] / sv_k5["lep"][2]),
                abs((sv_k5["lep"][0] / sv_k5["lep"][2]) - (sv_k5_down_R[0] / sv_k5_down_R[2])) / (sv_k5["lep"][0] / sv_k5["lep"][2]),
            )
            k5_left_gram_vs_right_gram_ed_err = max(k5_left_gram_vs_right_gram_ed_err, rg_diff)

            ob_k5 = observables_from_U_sv(U_k5["up"], sv_k5["up"], U_k5["down"], sv_k5["down"], sv_k5["lep"])
            r2_k5, rmax_k5 = ed_split_metrics(ob_k5)
            k5_left_gram_ed_split[fr_str(y_fr)] = {"ln_2nd_gen": m_str(r2_k5, 12), "ln_max": m_str(rmax_k5, 12)}
            shells_raw["K5_star_4"][y_fr] = ob_k5
            shells_data["K5_star_4"][fr_str(y_fr)] = {k: m_str(ob_k5[k], 14) for k in RATE_KEYS_10 + ("J_CP", "min_diag")}

    # Shell y=20->30 Gramian rates
    shell_rates_20_30 = {}
    with mp.workdps(120):
        for sname in ("E6_prim_24", "P30_96", "K5_star_4"):
            sr_map = {}
            for k in RATE_KEYS_10:
                rv = obs_rate(shells_raw[sname][Fr(20, 1)][k], shells_raw[sname][Fr(30, 1)][k], mp.mpf(20), mp.mpf(30))
                sr_map[k] = None if rv is None else m_str(rv, 10)
            shell_rates_20_30[sname] = sr_map

    # Exact T, S, M modular invariance of E6_prim (24-pt) and P30 (96-pt) shells at tau0 = -9/10 + 6/5 i
    shell_mod_inv = {"E6_prim_24": {}, "P30_96_fixed_set": {}, "P30_96_transported": {}}
    max_e6_tsm_err = mp.mpf(0)
    p30_M_fixed_err = mp.mpf(0)
    with mp.workdps(75):
        def eval_shell_gramian_at(pts_list, tau_v, L2_v):
            ctx = FrameCTauContext(tau_v, L2_v)
            Us, svs = {}, {}
            for sec in SECTOR_ORDER:
                ql, qr = SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]
                Ys = [ctx.yukawa(p[0], p[1], ql, qr) for p in pts_list]
                _, Us[sec], svs[sec], _ = gramian_eigh_asc(Ys)
            return observables_from_U_sv(Us["up"], svs["up"], Us["down"], svs["down"], svs["lep"])

        tau_b = mp.mpc(f2m(Fr(-9, 10)), f2m(Fr(6, 5)))
        L2_b = res_tau0["L2"]
        ob_e6_b = eval_shell_gramian_at(E6, tau_b, L2_b)
        ob_p30_b = eval_shell_gramian_at(P30, tau_b, L2_b)
        for gname, gmat in gammas.items():
            ga, gb, gc, gd = gmat
            gt = (ga * tau_b + gb) / (gc * tau_b + gd)
            L2_g = L2_b + mp.log(abs(gc * tau_b + gd))
            # E6_prim is mapped onto itself by ALL of SL(2, Z)
            ob_e6_g = eval_shell_gramian_at(E6, gt, L2_g)
            de6 = max_rel_obs_diff(ob_e6_b, ob_e6_g)
            max_e6_tsm_err = max(max_e6_tsm_err, de6)
            shell_mod_inv["E6_prim_24"][gname] = m_sci(de6, 8)

            # P30 fixed set (preserved by M, moved off act line by T and S)
            ob_p30_g = eval_shell_gramian_at(P30, gt, L2_g)
            dp30 = max_rel_obs_diff(ob_p30_b, ob_p30_g)
            shell_mod_inv["P30_96_fixed_set"][gname] = m_sci(dp30, 8)
            if gname == "M":
                p30_M_fixed_err = dp30

            # P30 transported by w -> w gamma^{-1} (exact covariance for all T, S, M)
            P30_tr = [act_w_right_inv(p, gmat) for p in P30]
            ob_p30_tr = eval_shell_gramian_at(P30_tr, gt, L2_g)
            shell_mod_inv["P30_96_transported"][gname] = m_sci(max_rel_obs_diff(ob_p30_b, ob_p30_tr), 8)

    report["O5_p845_and_shells"] = {
        "N1_to_60_lens_census": {
            "E0_control_N5": census_1_60["5"]["unit_ties"],
            "E0_control_N6": census_1_60["6"]["unit_ties"],
            "E0_control_N30": census_1_60["30"]["unit_ties"],
            "zero_tie_levels_1_to_60": zero_tie_levels,
            "zero_tie_levels_carrying_K5": zero_tie_div_by_5,
            "zero_tie_levels_carrying_K5_and_3divN": zero_tie_div_by_5_and_3,
            "minimal_N_zero_ties_with_K5": min(zero_tie_div_by_5),
            "minimal_N_zero_ties_with_K5_and_3divN": min(zero_tie_div_by_5_and_3),
            "head_to_head_10_15_20_30": {str(n): census_1_60[str(n)] for n in (10, 15, 20, 30)},
            "all_60": census_1_60,
        },
        "shell_gramians_by_height": shells_data,
        "shell_gramians_rates_y20_30": shell_rates_20_30,
        "K5_star_ed_analysis": {
            "pointwise_max_ln_ed_tie_all_heights": m_sci(k5_pointwise_max_ed_tie, 8),
            "left_gramian_ed_splitting_by_height": k5_left_gram_ed_split,
            "left_gramian_lep_vs_right_gramian_down_max_rel_err": m_sci(k5_left_gram_vs_right_gram_ed_err, 8),
        },
        "modular_invariance_at_tau0": shell_mod_inv,
        "E6_prim_max_TSM_err": m_sci(max_e6_tsm_err, 8),
        "P30_fixed_M_err": m_sci(p30_M_fixed_err, 8),
        "elapsed_sec": elapsed_sec_str(t_o5),
    }
    print("[Referee] Module O5 done in %ss | E6_TSM_err=%s | P30_M_err=%s | K5_pw_tie=%s | K5_LG_vs_RG=%s" % (
        report["O5_p845_and_shells"]["elapsed_sec"],
        m_sci(max_e6_tsm_err, 4),
        m_sci(p30_M_fixed_err, 4),
        m_sci(k5_pointwise_max_ed_tie, 4),
        m_sci(k5_left_gram_vs_right_gram_ed_err, 4),
    ), flush=True)

    # --------------------------------------------------------------------------
    # MODULE G6: Independent Cayley-Transform Haar U(3)^3 Scrambling + RPF1..RPF6
    # --------------------------------------------------------------------------
    print("[Referee] Module G6: 10-trial Cayley Haar U(3)^3 scrambling + RPF1..RPF6...", flush=True)
    t_g6 = time.monotonic_ns()

    def cayley_haar_u3(rng):
        """Construct random U in U(3) via Cayley transform U = (I - i H)(I + i H)^{-1}
        from integer-PRNG Hermitian H (zero floats!)."""
        I = mp.mpc(0, 1)
        SCALE = 10 ** 18
        H = mp.zeros(3, 3)
        for i in range(3):
            H[i, i] = mp.mpf(rng.randint(-SCALE, SCALE)) / SCALE
            for j in range(i + 1, 3):
                re_v = mp.mpf(rng.randint(-SCALE, SCALE)) / SCALE
                im_v = mp.mpf(rng.randint(-SCALE, SCALE)) / SCALE
                H[i, j] = mp.mpc(re_v, im_v)
                H[j, i] = mp.mpc(re_v, -im_v)
        I3 = mp.eye(3)
        # Solve (I + i H) U = (I - i H)
        U = mp.lu_solve(I3 + I * H, I3 - I * H)
        return U

    rng = random.Random(20261125)
    max_cayley_unit_err = mp.mpf(0)
    max_haar_pw_drift = mp.mpf(0)
    max_haar_orb_drift = mp.mpf(0)
    max_rpf5_lr_overlap_drift = mp.mpf(0)

    with mp.workdps(75):
        pt_h = (Fr(4, 15), Fr(1, 30))
        Yu0 = P30_Y[Fr(10, 1)][pt_h]["up"]
        Yd0 = P30_Y[Fr(10, 1)][pt_h]["down"]
        Ye0 = P30_Y[Fr(10, 1)][pt_h]["lep"]
        Uu0, svu0, Vu0 = svd_asc(Yu0)
        Ud0, svd0, _ = svd_asc(Yd0)
        _, sve0, _ = svd_asc(Ye0)
        ob_pw0 = observables_from_U_sv(Uu0, svu0, Ud0, svd0, sve0)
        lr0 = [[abs((Uu0.H * Vu0)[i, j]) for j in range(3)] for i in range(3)]

        # Orbit O1 at y = 10
        orb1 = orbits[0]
        O1_u0 = [P30_Y[Fr(10, 1)][p]["up"] for p in orb1]
        O1_d0 = [P30_Y[Fr(10, 1)][p]["down"] for p in orb1]
        O1_e0 = [P30_Y[Fr(10, 1)][p]["lep"] for p in orb1]
        _, Uo_u0, svo_u0, _ = gramian_eigh_asc(O1_u0)
        _, Uo_d0, svo_d0, _ = gramian_eigh_asc(O1_d0)
        _, _, svo_e0, _ = gramian_eigh_asc(O1_e0)
        ob_orb0 = observables_from_U_sv(Uo_u0, svo_u0, Uo_d0, svo_d0, svo_e0)

        for _ in range(10):
            UL = cayley_haar_u3(rng)
            URu = cayley_haar_u3(rng)
            URd = cayley_haar_u3(rng)
            URe = cayley_haar_u3(rng)
            for Umat in (UL, URu, URd, URe):
                max_cayley_unit_err = max(max_cayley_unit_err, mp.norm(Umat.H * Umat - mp.eye(3)))

            # Pointwise scramble: Y_f -> UL * Y_f * UR_f^H
            Uu1, svu1, Vu1 = svd_asc(UL * Yu0 * URu.H)
            Ud1, svd1, _ = svd_asc(UL * Yd0 * URd.H)
            _, sve1, _ = svd_asc(UL * Ye0 * URe.H)
            ob_pw1 = observables_from_U_sv(Uu1, svu1, Ud1, svd1, sve1)
            max_haar_pw_drift = max(max_haar_pw_drift, max_rel_obs_diff(ob_pw0, ob_pw1))

            # RPF5: non-physical left-right overlap |U_u^H V_u|
            lr1 = [[abs((Uu1.H * Vu1)[i, j]) for j in range(3)] for i in range(3)]
            lr_d = max(abs(lr1[i][j] - lr0[i][j]) for i in range(3) for j in range(3))
            max_rpf5_lr_overlap_drift = max(max_rpf5_lr_overlap_drift, lr_d)

            # Orbit-Gramian scramble
            _, Uo_u1, svo_u1, _ = gramian_eigh_asc([UL * Y * URu.H for Y in O1_u0])
            _, Uo_d1, svo_d1, _ = gramian_eigh_asc([UL * Y * URd.H for Y in O1_d0])
            _, _, svo_e1, _ = gramian_eigh_asc([UL * Y * URe.H for Y in O1_e0])
            ob_orb1 = observables_from_U_sv(Uo_u1, svo_u1, Uo_d1, svo_d1, svo_e1)
            max_haar_orb_drift = max(max_haar_orb_drift, max_rel_obs_diff(ob_orb0, ob_orb1))

    # RPF1: 6Y(u) = -4 -> -3 breaks >90% of 96 up-sector tropical rates in O1
    rpf1_broken = 0
    for pt in P30:
        nda = nd_fr(pt[0])
        tr_ok = trop_fn(nda, qu_r=-4)
        tr_bad = trop_fn(nda, qu_r=-3)
        if tr_ok["up_m2m3"] != tr_bad["up_m2m3"] or tr_ok["up_m1m3"] != tr_bad["up_m1m3"]:
            rpf1_broken += 1

    # RPF2: Replacing 1/4 by 1/3 in 2|nd(a) - 1/4| breaks 100% (96/96) of V23 rates
    rpf2_broken = sum(
        1 for pt in P30 if 2 * abs(nd_fr(pt[0]) - Fr(1, 3)) != trop_fn(nd_fr(pt[0]))["V23"]
    )

    rpf_verdicts = {
        "RPF1_qu_minus4_to_minus3": {
            "broken_of_96": rpf1_broken,
            "threshold": "> 86 of 96 (>90%)",
            "caught": rpf1_broken > 86,
        },
        "RPF2_quarter_to_third_in_V23_law": {
            "broken_of_96": rpf2_broken,
            "threshold": "96 of 96 (100%)",
            "caught": rpf2_broken == 96,
        },
        "RPF3_fixed_L2_under_S_M": {
            "min_drift_S_M": m_sci(min_fixed_L2_S_M_drift, 8),
            "max_drift_S_M": m_sci(max_fixed_L2_drift, 8),
            "threshold": "> 1e-3",
            "caught": max_fixed_L2_drift > mp.mpf(10) ** (-3),
        },
        "RPF4_wrong_w_gamma_under_T_M": {
            "min_drift_T_M": m_sci(min_wrong_w_T_M_drift, 8),
            "max_drift_T_M": m_sci(max_wrong_w_drift, 8),
            "threshold": "> 1e-1",
            "caught": max_wrong_w_drift > mp.mpf(10) ** (-1),
        },
        "RPF5_nonphysical_LR_overlap": {
            "max_drift_10_trials": m_sci(max_rpf5_lr_overlap_drift, 8),
            "threshold": "> 1e-1",
            "caught": max_rpf5_lr_overlap_drift > mp.mpf(10) ** (-1),
        },
        "RPF6_drop_E6_K5_pointwise_collapse": {
            "max_ln_ed_split_K5": m_sci(k5_pointwise_max_ed_tie, 8),
            "threshold": "< 1e-35",
            "caught": k5_pointwise_max_ed_tie < mp.mpf(10) ** (-35),
        },
    }

    report["G6_haar_and_planted"] = {
        "n_cayley_trials": 10,
        "max_cayley_unitarity_err": m_sci(max_cayley_unit_err, 8),
        "max_pointwise_haar_drift": m_sci(max_haar_pw_drift, 8),
        "max_orbit_gramian_haar_drift": m_sci(max_haar_orb_drift, 8),
        "planted_faults": rpf_verdicts,
        "planted_caught_count": sum(1 for v in rpf_verdicts.values() if v["caught"]),
        "elapsed_sec": elapsed_sec_str(t_g6),
    }

    # --------------------------------------------------------------------------
    # Final RG1..RG6 Gate Verdicts (Computed Directly from Measured Quantities)
    # --------------------------------------------------------------------------
    cf_v12_7_30 = mp.mpf(counterfactual_r86["(7/30, 19/30)"]["flipped_c0_in_Yu_rates_y30_40"]["V12"])
    cf_v13_4_15 = mp.mpf(counterfactual_r86["(4/15, 1/30)"]["flipped_c0_in_Yu_rates_y30_40"]["V13"])

    rg_gates = {
        "RG1_O1_tropical_law": (
            len(nd_sorted) == 12
            and is_zero_total_count == 0
            and all_mult_1_60
            and all_v23_law
            and max_diff_960_y30_40 < mp.mpf(10) ** (-3)
            and len(e3_tied_pts) == 8
            and len(e4_suppressed_pts) == 4
            and abs(cf_v12_7_30 - mp.mpf(1) / 2) < mp.mpf(2) / 1000
            and abs(cf_v13_4_15 - mp.mpf(1) / 2) < mp.mpf(2) / 1000
            and formula_all_match_unconstrained
        ),
        "RG2_O2_moderate_height_L2": (
            max_l2_trace_res < mp.mpf(10) ** (-11)
            and max_l2_shift_err < mp.mpf(10) ** (-10)
            and b1977_g1 == 5
            and b1977_g2 == 5
            and b1977_g4 == 5
            and b1977_g5 == 30
        ),
        "RG3_O3_joint_covariance": (
            max_l2_cov_err < mp.mpf(10) ** (-10)
            and max_joint_cov_err < mp.mpf(10) ** (-35)
        ),
        "RG4_O4_orbits_and_gramians": (
            len(orbits) == 8
            and sorted(slow_mults, reverse=True) == [6, 6, 3, 3, 0, 0, 0, 0]
            and max_orb_unitarity_err < mp.mpf(10) ** (-35)
            and max_orb_M_invariance_err < mp.mpf(10) ** (-35)
        ),
        "RG5_O5_p845_and_shells": (
            bool(census_1_60["5"]["unit_ties"])
            and bool(census_1_60["6"]["unit_ties"])
            and not bool(census_1_60["30"]["unit_ties"])
            and k5_pointwise_max_ed_tie < mp.mpf(10) ** (-35)
            and k5_left_gram_vs_right_gram_ed_err < mp.mpf(10) ** (-35)
            and max_e6_tsm_err < mp.mpf(10) ** (-35)
            and p30_M_fixed_err < mp.mpf(10) ** (-35)
        ),
        "RG6_haar_and_planted": (
            max_haar_pw_drift < mp.mpf(10) ** (-30)
            and max_haar_orb_drift < mp.mpf(10) ** (-30)
            and report["G6_haar_and_planted"]["planted_caught_count"] == 6
        ),
    }

    report["summary_verdicts"] = {
        "RG_gates": rg_gates,
        "RG_passed_count": sum(1 for v in rg_gates.values() if v),
        "RPF_caught_count": report["G6_haar_and_planted"]["planted_caught_count"],
        "total_elapsed_sec": elapsed_sec_str(t_start),
    }

    assert_no_json_floats(report)
    out_bytes = (json.dumps(report, indent=2, sort_keys=False) + "\n").encode("utf-8")
    OUT_PATH.write_bytes(out_bytes)
    out_sha = hashlib.sha256(out_bytes).hexdigest()
    print("[Referee] COMPLETE in %ss | RG=%d/6 | RPF=%d/6 | OUT_SHA256=%s" % (
        report["summary_verdicts"]["total_elapsed_sec"],
        report["summary_verdicts"]["RG_passed_count"],
        report["summary_verdicts"]["RPF_caught_count"],
        out_sha,
    ), flush=True)


if __name__ == "__main__":
    main()
