#!/usr/bin/env python3
"""
Cold-Room Zero-Trust Disjoint Referee v3 (Remediated v6 Verification) for Card AGY-002_A2-WHOLE-INSTRUMENT (0 of 19).
Evaluates remediated Scope Card Section 4 (Pre-v6 Remediation Erratum) independently
before inspecting Authoritative Producer v6. (Supersedes failed pre-commit v2 at be9de367a
which hit dps=18 underflow at K=30 y=8.216 in W1 Part B4; zero output ever produced in v2.)

Strictly standalone: pure Python stdlib + mpmath + sympy ONLY.
Zero AST float/complex literals or casts, zero forbidden imports, zero JSON floats,
zero empirical SM/NuFIT/Planck/DESI/CODATA inputs (strictly 0 of 19).

Disjoint numerical methods (Guardrail 6):
  - Fuchsian L_2(tau): 4-stage Gauss-Legendre (GL8, order 8) symplectic ODE integrator
    with exact holomorphic variational dT/dc, Chebyshev-recurrence Jacobi theta_1
    log-derivative wp(z), Euler pentagonal eta(tau), exact Weierstrass Laurent
    recurrence, Frobenius connection, and 3-trace (Ta, Tb, Tab) Gauss-Newton.
  - Linear algebra: 6x6 Hermitian Jordan-Wielandt mp.eigh SVD (jw_svd), direct mp.eigh
    Hermitian Gramians, 6x6 real-split mp.eigsy Autonne-Takagi factorization, and
    Cayley-transform (I - iH)(I + iH)^(-1) Haar U(3)^5 sampler.
  - RGE integrator (W4): Implicit 2-stage Gauss-Legendre (GL4, order 4) fixed-point
    integrator + independent SymPy derivation of Chowdhury-Eberhardt 1503.08216
    Type-II 2HDM 1x1 coefficients (exact MV84 -29/240, -65/240; GUT g1(0)=1/2;
    1-loop quartics primary + 2-loop N_H=2 Machacek-Vaughn quartics sensitivity check).
  - Optimization (W3): 2-stage Riemannian projected Barzilai-Borwein on S^5 and
    S^5 x S^5 (8 starts at dps=22 + dps=26 polish) with exact analytic Wirtinger gradients.
  - Geodesic quadrature (W2): 16-node (+ 32-node convergence) periodic midpoint quadrature
    over all three true closed M-orbits: mark (8,1)/30 [len 12], twin_p30 (11,12)/30 [len 12],
    and off_1_5 (1,5)/30 [full len 60].
"""

import ast
import hashlib
import json
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import sympy as sp


# ============================================================================
# 0. STRICT ZERO-FLOAT / ZERO-COMPLEX HELPERS & DETERMINISTIC SHA-256 PRNG
# ============================================================================

def mp_str(x, n=28):
    if isinstance(x, bool):
        return x
    if isinstance(x, int):
        return x
    if isinstance(x, Fraction):
        return f"{x.numerator}/{x.denominator}"
    if isinstance(x, mp.mpc):
        return f"({mp.nstr(mp.re(x), n)}, {mp.nstr(mp.im(x), n)})"
    return mp.nstr(x, n)


def frac_str(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"


def gcd_int(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def median_mpf(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return mp.mpf(0)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


class Sha256Rng:
    """Pure integer/mpmath deterministic PRNG backed by SHA-256 (zero floats)."""

    def __init__(self, seed_str):
        self._seed = seed_str.encode("utf-8")
        self._counter = 0

    def next_uint(self, bits=128):
        chunks = (bits + 255) // 256
        val = 0
        for _ in range(chunks):
            h = hashlib.sha256(self._seed + self._counter.to_bytes(8, "big")).digest()
            self._counter += 1
            val = (val << 256) | int.from_bytes(h, "big")
        return val & ((1 << bits) - 1)

    def next_mpf_unit(self):
        bits = max(128, mp.mp.dps * 4 + 16)
        u = self.next_uint(bits)
        return (mp.mpf(2) * mp.mpf(u) / mp.mpf(1 << bits)) - mp.mpf(1)

    def next_mpf_signed_gauss_like(self):
        s = mp.mpf(0)
        for _ in range(6):
            s += self.next_mpf_unit()
        return s / mp.sqrt(mp.mpf(2))


def elapsed_sec_str(t0_ns):
    dt_ns = time.monotonic_ns() - t0_ns
    return mp.nstr(mp.mpf(dt_ns) / mp.mpf(10**9), 6)


# ============================================================================
# 1. DISJOINT LINEAR ALGEBRA (6x6 JORDAN-WIELANDT SVD, 6x6 TAKAGI, CAYLEY HAAR)
# ============================================================================

def mat_fro_norm(A):
    r, c = A.rows, A.cols
    s = mp.mpf(0)
    for i in range(r):
        for j in range(c):
            v = A[i, j]
            s += mp.re(v) * mp.re(v) + mp.im(v) * mp.im(v)
    return mp.sqrt(s)


def mat_mul_3(A, B):
    C = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            s = mp.mpc(0)
            for k in range(3):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C


def mat_dag(A):
    r, c = A.rows, A.cols
    B = mp.matrix(c, r)
    for i in range(r):
        for j in range(c):
            B[j, i] = mp.conj(A[i, j])
    return B


def mat_tr(A):
    s = mp.mpc(0)
    for i in range(A.rows):
        s += A[i, i]
    return s


def cross3(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


def vec_norm(v):
    return mp.sqrt(sum(mp.re(x) * mp.re(x) + mp.im(x) * mp.im(x) for x in v))


def vec_dot(u, v):
    return sum(mp.conj(u[i]) * v[i] for i in range(len(u)))


def jw_svd(A):
    """Non-squaring 6x6 Hermitian Jordan-Wielandt SVD via mp.eigh (disjoint from mp.svd_c)."""
    H = mp.zeros(6, 6)
    for i in range(3):
        for j in range(3):
            H[i, 3 + j] = A[i, j]
            H[3 + j, i] = mp.conj(A[i, j])
    ev, vec = mp.eigh(H)
    s3_est = max(mp.mpf(0), mp.re(ev[5]))
    zero_cut = s3_est * (mp.mpf(10) ** (-(mp.mp.dps - 6)))
    u_cols = [None, None, None]
    v_cols = [None, None, None]
    s_vals = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    done_u = []
    done_v = []
    for k in (2, 1, 0):
        lam = mp.re(ev[3 + k])
        if lam > zero_cut:
            u = [vec[i, 3 + k] for i in range(3)]
            v = [vec[3 + i, 3 + k] for i in range(3)]
            for du in done_u:
                ov = vec_dot(du, u)
                u = [u[i] - ov * du[i] for i in range(3)]
            for dv in done_v:
                ov = vec_dot(dv, v)
                v = [v[i] - ov * dv[i] for i in range(3)]
            nu = vec_norm(u)
            nv = vec_norm(v)
            if nu > zero_cut and nv > zero_cut:
                u = [x / nu for x in u]
                v = [x / nv for x in v]
                Av = [sum(A[i, j] * v[j] for j in range(3)) for i in range(3)]
                ov = vec_dot(u, Av)
                ab = abs(ov)
                if ab > mp.mpf(0):
                    ph = ov / ab
                    u = [x * ph for x in u]
                s_vals[k] = ab
                u_cols[k] = u
                v_cols[k] = v
                done_u.append(u)
                done_v.append(v)
                continue
        if len(done_u) == 2:
            u = cross3([mp.conj(x) for x in done_u[0]], [mp.conj(x) for x in done_u[1]])
            v = cross3([mp.conj(x) for x in done_v[0]], [mp.conj(x) for x in done_v[1]])
            nu = vec_norm(u)
            nv = vec_norm(v)
            u = [x / nu for x in u]
            v = [x / nv for x in v]
        else:
            best_u, best_nu = None, mp.mpf(-1)
            best_v, best_nv = None, mp.mpf(-1)
            for idx in range(3):
                eu = [mp.mpc(1 if i == idx else 0) for i in range(3)]
                for du in done_u:
                    ov = vec_dot(du, eu)
                    eu = [eu[i] - ov * du[i] for i in range(3)]
                nu = vec_norm(eu)
                if nu > best_nu:
                    best_nu = nu
                    best_u = [x / nu for x in eu]
                ev_b = [mp.mpc(1 if i == idx else 0) for i in range(3)]
                for dv in done_v:
                    ov = vec_dot(dv, ev_b)
                    ev_b = [ev_b[i] - ov * dv[i] for i in range(3)]
                nv = vec_norm(ev_b)
                if nv > best_nv:
                    best_nv = nv
                    best_v = [x / nv for x in ev_b]
            u, v = best_u, best_v
        Av = [sum(A[i, j] * v[j] for j in range(3)) for i in range(3)]
        ov = vec_dot(u, Av)
        ab = abs(ov)
        if ab > mp.mpf(0):
            u = [x * (ov / ab) for x in u]
        s_vals[k] = ab
        u_cols[k] = u
        v_cols[k] = v
        done_u.append(u)
        done_v.append(v)

    order = sorted(range(3), key=lambda k: s_vals[k])
    s_sorted = [s_vals[k] for k in order]
    U = mp.matrix(3, 3)
    V = mp.matrix(3, 3)
    for col, k in enumerate(order):
        for i in range(3):
            U[i, col] = u_cols[k][i]
            V[i, col] = v_cols[k][i]
    return s_sorted, U, V


def takagi_6x6(M):
    """
    Direct complex-symmetric Autonne-Takagi via 6x6 real-split mp.eigsy.
    Returns ascending m_sorted and unitary V_tak with V_tak^T M V_tak = diag(m_sorted).
    U_nu = conj(V_tak) satisfies U_nu^H M conj(U_nu) = diag(m_sorted) (and M = U_nu diag(m) U_nu^T).
    """
    Ms = (M + M.T) / 2
    R = mp.zeros(6, 6)
    for i in range(3):
        for j in range(3):
            re_v = mp.re(Ms[i, j])
            im_v = mp.im(Ms[i, j])
            R[i, j] = re_v
            R[i, 3 + j] = im_v
            R[3 + i, j] = im_v
            R[3 + i, 3 + j] = -re_v
    ev, vec = mp.eigsy(R)
    m_max = max(mp.mpf(0), ev[5])
    cut = m_max * (mp.mpf(10) ** (-(mp.mp.dps - 6)))
    cols = [None, None, None]
    m_vals = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    done = []
    for k in (2, 1, 0):
        if ev[3 + k] > cut:
            u = [mp.mpc(vec[i, 3 + k], -vec[3 + i, 3 + k]) for i in range(3)]
            for du in done:
                ov = vec_dot(du, u)
                u = [u[i] - ov * du[i] for i in range(3)]
            nu = vec_norm(u)
            u = [x / nu for x in u]
        else:
            if len(done) == 2:
                u = cross3([mp.conj(x) for x in done[0]], [mp.conj(x) for x in done[1]])
                u = [x / vec_norm(u) for x in u]
            else:
                best_u, best_nu = None, mp.mpf(-1)
                for idx in range(3):
                    eu = [mp.mpc(1 if i == idx else 0) for i in range(3)]
                    for du in done:
                        ov = vec_dot(du, eu)
                        eu = [eu[i] - ov * du[i] for i in range(3)]
                    nu = vec_norm(eu)
                    if nu > best_nu:
                        best_nu = nu
                        best_u = [x / nu for x in eu]
                u = best_u
        Mu = [sum(Ms[i, j] * u[j] for j in range(3)) for i in range(3)]
        quad = sum(u[i] * Mu[i] for i in range(3))
        ab = abs(quad)
        if ab > mp.mpf(0):
            ph = mp.sqrt(mp.conj(quad) / ab)
            u = [x * ph for x in u]
        m_vals[k] = ab
        cols[k] = u
        done.append(u)

    order = sorted(range(3), key=lambda k: m_vals[k])
    m_sorted = [m_vals[k] for k in order]
    V_tak = mp.matrix(3, 3)
    for col, k in enumerate(order):
        for i in range(3):
            V_tak[i, col] = cols[k][i]
    D = V_tak.T * Ms * V_tak
    for i in range(3):
        D[i, i] -= m_sorted[i]
    res = mat_fro_norm(D) / max(mp.mpf(1), mat_fro_norm(Ms))
    return m_sorted, V_tak, res


def haar_u3_cayley(rng):
    """Cayley-transform Haar U(3) sampler: diag(e^{i phi}) (I-iH1)(I+iH1)^{-1} (I-iH2)(I+iH2)^{-1}."""
    I_c = mp.mpc(0, 1)
    I3 = mp.eye(3)

    def one_cayley():
        H = mp.zeros(3, 3)
        for i in range(3):
            H[i, i] = rng.next_mpf_signed_gauss_like()
            for j in range(i + 1, 3):
                v = mp.mpc(rng.next_mpf_signed_gauss_like(), rng.next_mpf_signed_gauss_like())
                H[i, j] = v
                H[j, i] = mp.conj(v)
        return (I3 - I_c * H) * ((I3 + I_c * H) ** (-1))

    U1 = one_cayley()
    U2 = one_cayley()
    D = mp.zeros(3, 3)
    for i in range(3):
        ang = mp.pi * rng.next_mpf_unit()
        D[i, i] = mp.exp(I_c * ang)
    return mat_mul_3(D, mat_mul_3(U1, U2))


def jarlskog(V):
    return abs(mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])))


def pmns_observables_from_U(U):
    s13_sq = min(mp.mpf(1), abs(U[0, 2]) ** 2)
    c13_sq = max(mp.mpf(0), mp.mpf(1) - s13_sq)
    if c13_sq > mp.mpf(10) ** (-25):
        s12_sq = min(mp.mpf(1), (abs(U[0, 1]) ** 2) / c13_sq)
        s23_sq = min(mp.mpf(1), (abs(U[1, 2]) ** 2) / c13_sq)
    else:
        s12_sq = mp.mpf(0)
        s23_sq = mp.mpf(0)
    rad2deg = mp.mpf(180) / mp.pi
    return {
        "s12_sq": s12_sq,
        "s23_sq": s23_sq,
        "s13_sq": s13_sq,
        "theta12_deg": mp.asin(mp.sqrt(s12_sq)) * rad2deg,
        "theta23_deg": mp.asin(mp.sqrt(s23_sq)) * rad2deg,
        "theta13_deg": mp.asin(mp.sqrt(s13_sq)) * rad2deg,
        "J_PMNS": jarlskog(U),
    }


# ============================================================================
# 2. DISJOINT MODULAR FUNCTIONS & GL8 FUCHSIAN L_2(tau) SOLVER
# ============================================================================

def eta_pentagonal(tau):
    I = mp.mpc(0, 1)
    q = mp.exp(2 * mp.pi * I * tau)
    q24 = mp.exp(mp.pi * I * tau / 12)
    tol = mp.mpf(10) ** (-(mp.mp.dps + 5))
    s = mp.mpc(1)
    k = 1
    while True:
        e1 = k * (3 * k - 1) // 2
        e2 = k * (3 * k + 1) // 2
        t1 = q ** e1
        t2 = q ** e2
        if k % 2 == 1:
            s -= (t1 + t2)
        else:
            s += (t1 + t2)
        if abs(t1) < tol and abs(t2) < tol:
            break
        k += 1
    return q24 * s


def theta_nullwerte(tau):
    I = mp.mpc(0, 1)
    pi = mp.pi
    qh = mp.exp(I * pi * tau)
    tol = mp.mpf(10) ** (-(mp.mp.dps + 6))
    t2s = mp.mpc(0)
    qp = mp.mpc(1)
    n = 0
    while True:
        t2s += qp
        if abs(qp) < tol and n > 2:
            break
        n += 1
        qp *= qh ** (2 * n)
    t2 = 2 * mp.exp(I * pi * tau / 4) * t2s
    t3 = mp.mpc(1)
    t4 = mp.mpc(1)
    n = 1
    while True:
        term = qh ** (n * n)
        t3 += 2 * term
        t4 += (2 * term if n % 2 == 0 else -2 * term)
        if abs(term) < tol:
            break
        n += 1
    return t2, t3, t4


def wp_theta1_logderiv(z, tau):
    pi = mp.pi
    qh = mp.exp(mp.mpc(0, 1) * pi * tau)
    tol = mp.mpf(10) ** (-(mp.mp.dps + 6))
    u = pi * z
    s1 = mp.sin(u)
    c1 = mp.cos(u)
    s2 = 2 * s1 * c1
    c2 = 2 * c1 * c1 - 1
    sn_m = s1
    cn_m = c1
    sgn = mp.mpf(1)
    qp = mp.mpc(1)
    th = sn_m
    thp = cn_m
    thpp = -sn_m
    a1 = mp.mpc(1)
    a3 = mp.mpc(1)
    n = 1
    while True:
        qp *= qh ** (2 * n)
        sgn = -sgn
        sn_m, cn_m = sn_m * c2 + cn_m * s2, cn_m * c2 - sn_m * s2
        m = 2 * n + 1
        term = sgn * qp
        th += term * sn_m
        thp += term * m * cn_m
        thpp -= term * (m * m) * sn_m
        a1 += term * m
        a3 += term * (m * m * m)
        if abs(term) * m * m * max(mp.mpf(1), abs(sn_m) + abs(cn_m)) < tol:
            break
        n += 1
    return (pi * pi) * ((thp * thp - thpp * th) / (th * th) - a3 / (3 * a1))


def gl8_tableau():
    r30 = mp.sqrt(30)
    x1 = mp.sqrt((15 + 2 * r30) / 35)
    x2 = mp.sqrt((15 - 2 * r30) / 35)
    c = [(1 + x) / 2 for x in (-x1, -x2, x2, x1)]
    w1 = (18 - r30) / 72
    w2 = (18 + r30) / 72
    b = [w1, w2, w2, w1]
    M = mp.matrix([[c[j] ** k for j in range(4)] for k in range(4)])
    A = [[mp.mpf(0)] * 4 for _ in range(4)]
    for i in range(4):
        sol = mp.lu_solve(M, mp.matrix([c[i] ** (k + 1) / (k + 1) for k in range(4)]))
        for j in range(4):
            A[i][j] = sol[j]
    AA = [[sum(A[i][j] * A[j][k] for j in range(4)) for k in range(4)] for i in range(4)]
    return c, b, A, AA


def solve_4x4_multi(M, rhs_list):
    n = 4
    m = len(rhs_list)
    A = [row[:] for row in M]
    B = [[rhs_list[j][i] for j in range(m)] for i in range(n)]
    for i in range(n):
        piv = i
        mv = abs(A[i][i])
        for r in range(i + 1, n):
            v = abs(A[r][i])
            if v > mv:
                mv = v
                piv = r
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            B[i], B[piv] = B[piv], B[i]
        inv = 1 / A[i][i]
        Ai = A[i]
        Bi = B[i]
        for r in range(i + 1, n):
            f = A[r][i] * inv
            Ar = A[r]
            Br = B[r]
            for c in range(i + 1, n):
                Ar[c] -= f * Ai[c]
            for j in range(m):
                Br[j] -= f * Bi[j]
    X = [[mp.mpc(0)] * n for _ in range(m)]
    for i in range(n - 1, -1, -1):
        inv = 1 / A[i][i]
        Ai = A[i]
        Bi = B[i]
        for j in range(m):
            s = Bi[j]
            for c in range(i + 1, n):
                s -= Ai[c] * X[j][c]
            X[j][i] = s * inv
    return X


def gl8_propagate_with_dc(dz, n_steps, wp_nodes, c_param, tab, need_dc=True):
    cs, bs, A, AA = tab
    h = dz / n_steps
    h2 = h * h
    Y00 = mp.mpc(1)
    Y01 = mp.mpc(0)
    Y10 = mp.mpc(0)
    Y11 = mp.mpc(1)
    dY00 = mp.mpc(0)
    dY01 = mp.mpc(0)
    dY10 = mp.mpc(0)
    dY11 = mp.mpc(0)
    idx = 0
    for _ in range(n_steps):
        qs = [wp_nodes[idx + j] / 4 + c_param for j in range(4)]
        idx += 4
        M = [[(1 if i == k else 0) + h2 * AA[i][k] * qs[k] for k in range(4)] for i in range(4)]
        r0 = [Y00 + h * cs[i] * Y10 for i in range(4)]
        r1 = [Y01 + h * cs[i] * Y11 for i in range(4)]
        U0, U1 = solve_4x4_multi(M, [r0, r1])
        if need_dc:
            dr0 = [dY00 + h * cs[i] * dY10 - h2 * sum(AA[i][k] * U0[k] for k in range(4)) for i in range(4)]
            dr1 = [dY01 + h * cs[i] * dY11 - h2 * sum(AA[i][k] * U1[k] for k in range(4)) for i in range(4)]
            dU0, dU1 = solve_4x4_multi(M, [dr0, dr1])
            dL0 = [-U0[j] - qs[j] * dU0[j] for j in range(4)]
            dL1 = [-U1[j] - qs[j] * dU1[j] for j in range(4)]
            dK0 = [dY10 + h * sum(A[j][k] * dL0[k] for k in range(4)) for j in range(4)]
            dK1 = [dY11 + h * sum(A[j][k] * dL1[k] for k in range(4)) for j in range(4)]
            dY00 += h * sum(bs[j] * dK0[j] for j in range(4))
            dY01 += h * sum(bs[j] * dK1[j] for j in range(4))
            dY10 += h * sum(bs[j] * dL0[j] for j in range(4))
            dY11 += h * sum(bs[j] * dL1[j] for j in range(4))
        L0 = [-qs[j] * U0[j] for j in range(4)]
        L1 = [-qs[j] * U1[j] for j in range(4)]
        K0 = [Y10 + h * sum(A[j][k] * L0[k] for k in range(4)) for j in range(4)]
        K1 = [Y11 + h * sum(A[j][k] * L1[k] for k in range(4)) for j in range(4)]
        Y00 += h * sum(bs[j] * K0[j] for j in range(4))
        Y01 += h * sum(bs[j] * K1[j] for j in range(4))
        Y10 += h * sum(bs[j] * L0[j] for j in range(4))
        Y11 += h * sum(bs[j] * L1[j] for j in range(4))
    return mp.matrix([[Y00, Y01], [Y10, Y11]]), mp.matrix([[dY00, dY01], [dY10, dY11]])


def solve_fuchsian_gl8(tau, dps=30):
    with mp.workdps(dps):
        tau = mp.mpc(tau)
        y = mp.im(tau)
        tab = gl8_tableau()
        cs = tab[0]
        z0 = (1 + tau) / 2
        na = 16
        ha = mp.mpc(1) / na
        wp_a = [wp_theta1_logderiv(z0 + (k + ci) * ha, tau) for k in range(na) for ci in cs]
        if abs(tau) > mp.mpf(5) / 2:
            segs_b = [
                (mp.mpf(0), mp.mpf(2) / 5, 14),
                (mp.mpf(2) / 5, mp.mpf(3) / 5, 14),
                (mp.mpf(3) / 5, mp.mpf(1), 14),
            ]
        else:
            segs_b = [(mp.mpf(0), mp.mpf(1), 18)]
        wp_b_segs = []
        for s0, s1, nb in segs_b:
            hb = (s1 - s0) * tau / nb
            arr = [wp_theta1_logderiv(z0 + s0 * tau + (k + ci) * hb, tau) for k in range(nb) for ci in cs]
            wp_b_segs.append(((s1 - s0) * tau, nb, arr))

        c_p = mp.mpc(mp.pi ** 2 / 12, 0) if y >= 1 else mp.mpc(-mp.pi ** 2 / (12 * y * y), 0)
        err = mp.mpf(1)
        for _ in range(16):
            Ta, dTa = gl8_propagate_with_dc(mp.mpc(1), na, wp_a, c_p, tab, True)
            Tb = mp.eye(2)
            dTb = mp.zeros(2, 2)
            for dz_s, nb, arr in wp_b_segs:
                Ms, dMs = gl8_propagate_with_dc(dz_s, nb, arr, c_p, tab, True)
                dTb = dMs * Tb + Ms * dTb
                Tb = Ms * Tb
            Tab = Ta * Tb
            dTab = dTa * Tb + Ta * dTb
            f0 = [mp.im(Ta[0, 0] + Ta[1, 1]), mp.im(Tb[0, 0] + Tb[1, 1]), mp.im(Tab[0, 0] + Tab[1, 1])]
            err = max(abs(v) for v in f0)
            if err < mp.mpf(10) ** (-18):
                break
            J = mp.matrix(3, 2)
            for r, dM in enumerate([dTa, dTb, dTab]):
                dt = dM[0, 0] + dM[1, 1]
                J[r, 0] = mp.im(dt)
                J[r, 1] = mp.re(dt)
            step = mp.lu_solve(J.T * J, -(J.T * mp.matrix(f0)))
            c_p += mp.mpc(step[0], step[1])
            if abs(step[0]) + abs(step[1]) < mp.mpf(10) ** (-19):
                break

        r_lat = min(mp.mpf(1), abs(tau), abs(tau - 1), abs(tau + 1))
        z_m = (r_lat / 8) * z0 / abs(z0)
        M_to_m = mp.eye(2)
        n_lad = 6
        ratio = (abs(z_m) / abs(z0)) ** (mp.mpf(1) / n_lad)
        z_cur = z0
        for _ in range(n_lad):
            z_nxt = z_cur * ratio
            dz = z_nxt - z_cur
            nseg = 6
            arr = [wp_theta1_logderiv(z_cur + (k + ci) * (dz / nseg), tau) for k in range(nseg) for ci in cs]
            Ms, _ = gl8_propagate_with_dc(dz, nseg, arr, c_p, tab, False)
            M_to_m = Ms * M_to_m
            z_cur = z_nxt

        pi = mp.pi
        t2, t3, t4 = theta_nullwerte(tau)
        t2_4 = t2 ** 4
        t3_4 = t3 ** 4
        t4_4 = t4 ** 4
        g2 = (2 * pi ** 4 / 3) * (t2_4 ** 2 + t3_4 ** 2 + t4_4 ** 2)
        g3 = (4 * pi ** 6 / 27) * (t2_4 + t3_4) * (t3_4 + t4_4) * (t4_4 - t2_4)
        M_ord = 24
        alpha = [mp.mpc(0)] * (M_ord + 1)
        alpha[1] = g2 / 20
        alpha[2] = g3 / 28
        for m in range(3, M_ord + 1):
            alpha[m] = (mp.mpf(3) / ((2 * m + 3) * (m - 2))) * sum(alpha[j] * alpha[m - 1 - j] for j in range(1, m - 1))
        v = [c_p] + [alpha[m] / 4 for m in range(1, M_ord + 1)]
        a_f = [mp.mpc(0)] * (M_ord + 1)
        b_f = [mp.mpc(0)] * (M_ord + 1)
        a_f[0] = mp.mpc(1)
        for k in range(1, M_ord + 1):
            a_f[k] = -sum(v[k - 1 - j] * a_f[j] for j in range(k)) / (4 * k * k)
            b_f[k] = -(4 * k * a_f[k] + sum(v[k - 1 - j] * b_f[j] for j in range(1, k))) / (4 * k * k)

        z2 = z_m * z_m
        sqz = mp.sqrt(z_m)
        lnz = mp.log(z_m)
        S_a = mp.mpc(0)
        S_ap = mp.mpc(0)
        S_b = mp.mpc(0)
        S_bp = mp.mpc(0)
        zp = mp.mpc(1)
        for k in range(M_ord + 1):
            S_a += a_f[k] * zp
            S_b += b_f[k] * zp
            if k >= 1:
                S_ap += (2 * k) * a_f[k] * (zp / z_m)
                S_bp += (2 * k) * b_f[k] * (zp / z_m)
            zp *= z2
        u1 = sqz * S_a
        u1p = S_a / (2 * sqz) + sqz * S_ap
        u2 = u1 * lnz + sqz * S_b
        u2p = u1p * lnz + u1 / z_m + S_b / (2 * sqz) + sqz * S_bp
        F_mat = mp.matrix([[u1, u2], [u1p, u2p]])
        C_frob = M_to_m ** (-1) * F_mat
        Ta_f = C_frob ** (-1) * Ta * C_frob
        Tb_f = C_frob ** (-1) * Tb * C_frob
        rho = mp.sqrt(-Ta_f[1, 0])
        xi = -mp.mpc(0, 1) * mp.im(Ta_f[1, 1]) / rho
        Q = mp.matrix([[rho, xi], [0, 1 / rho]])
        Qinv = Q ** (-1)
        Ta_r = Q * Ta_f * Qinv
        Tb_r = Q * Tb_f * Qinv
        sl2r_err = max(
            max(abs(mp.im(Ta_r[i, j])) for i in range(2) for j in range(2)),
            max(abs(mp.im(Tb_r[i, j])) for i in range(2) for j in range(2)),
        )
        lam_s = -2 * pi * mp.im(-(rho * rho))
        sgn = mp.mpf(1) if lam_s > 0 else mp.mpf(-1)
        L2 = pi - (2 * pi / abs(lam_s)) * mp.im(sgn * rho * xi)
        return {
            "L2": L2, "c_param": c_p, "err": err, "sl2r_err": sl2r_err,
            "Qinv": Qinv, "a_f": a_f, "b_f": b_f, "r_lat": r_lat,
        }


def reduce_to_F(tau):
    a, b, c, d = 1, 0, 0, 1
    t = mp.mpc(tau)
    for _ in range(100):
        n = int(mp.nint(mp.re(t)))
        if n != 0:
            t = t - n
            a, b = a - n * c, b - n * d
        if abs(t) < mp.mpf(1) - mp.mpf(10) ** (-(mp.mp.dps - 4)):
            t = -1 / t
            a, b, c, d = -c, -d, a, b
        else:
            break
    return t, (a, b, c, d)


_L2_CACHE = {}


def get_L2(tau, solve_dps=30):
    tF, (a, b, c, d) = reduce_to_F(tau)
    xF = abs(mp.re(tF))
    yF = mp.im(tF)
    key = (mp.nstr(xF, 18), mp.nstr(yF, 18))
    if key not in _L2_CACHE:
        res = solve_fuchsian_gl8(mp.mpc(xF, yF), dps=solve_dps)
        _L2_CACHE[key] = res["L2"]
    L2_F = mp.mpf(_L2_CACHE[key])
    return L2_F - mp.log(abs(c * tau + d))


# ============================================================================
# 3. FRAME C YUKAWA ASSEMBLY WITH EXACT PER-TAU CHANNEL-WEIGHT CACHING
# ============================================================================

def build_frame_c_algebra():
    I = mp.mpc(0, 1)
    Q_I = mp.matrix([[I, 0], [0, -I]])
    Q_J = mp.matrix([[0, 1], [-1, 0]])
    Q_K = Q_I * Q_J
    eps = Q_J
    U = {"1": mp.eye(2), "i": Q_I, "j": Q_J, "k": Q_K}
    keys = ["1", "i", "j", "k"]
    B = [Q_J, Q_I, Q_K]
    G = mp.matrix(4, 4)
    for it, kt in enumerate(keys):
        A = eps * U[kt]
        for is_, ks in enumerate(keys):
            Bm = U[ks]
            G[it, is_] = sum(A[m, n] * Bm[m, n] for m in range(2) for n in range(2))
    Ginv = G ** (-1)
    EDUAL = {}
    for ia, ka in enumerate(keys):
        M = mp.zeros(2, 2)
        for ib, kb in enumerate(keys):
            M += Ginv[ib, ia] * U[kb]
        EDUAL[ka] = M
    Q_list = [Q_I, Q_J, Q_K]
    T_p = []
    for Qp in Q_list:
        Tp = [[[mp.mpc(0) for _ in range(4)] for _ in range(3)] for _ in range(3)]
        for ia in range(3):
            for ib in range(3):
                P = B[ia].T * eps * Qp * B[ib]
                for is_, ks in enumerate(keys):
                    Ed = EDUAL[ks]
                    Tp[ia][ib][is_] = sum(P[m, n] * Ed[m, n] for m in range(2) for n in range(2))
        T_p.append(Tp)
    return {
        "Q_I": Q_I, "Q_J": Q_J, "Q_K": Q_K, "eps": eps,
        "U": U, "keys": keys, "B": B, "EDUAL": EDUAL, "T_p": T_p,
    }


def make_tau_ctx(tau, L2_val=None, solve_dps=30):
    I = mp.mpc(0, 1)
    pi = mp.pi
    tau = mp.mpc(tau)
    x = mp.re(tau)
    y = mp.im(tau)
    if L2_val is None:
        L2_val = get_L2(tau, solve_dps=solve_dps)
    else:
        L2_val = mp.mpf(L2_val)
    et = eta_pentagonal(tau)
    et3 = et ** 3
    t2, t3, t4 = theta_nullwerte(tau)
    c0 = -t2 * t2 * (t3 ** 4 + t4 ** 4) / (24 * et3)
    c1 = t4 * t4 * (t2 ** 4 + t3 ** 4) / (24 * et3)
    c2 = I * t3 * t3 * (t2 ** 4 - t4 ** 4) / (24 * et3)
    c_vec = [c0, c1, c2]
    c_norm = vec_norm(c_vec)
    c_hat = [v / c_norm for v in c_vec]
    qh = mp.exp(I * pi * tau)
    return {
        "tau": tau, "x": x, "y": y, "sqy": mp.sqrt(y), "L2": L2_val,
        "dps": mp.mp.dps,
        "et3": et3, "inv_2pi_et3": 1 / (2 * pi * et3),
        "c_vec": c_vec, "c_norm": c_norm, "c_hat": c_hat,
        "qh": qh, "em2L2": mp.exp(-2 * L2_val),
        "cwt_const": pi * mp.log(y) - 2 * pi * (mp.euler + mp.log(pi)),
        "two_pi_L2": 2 * pi * L2_val,
        "Fu_kmax": max(4, int(mp.ceil((mp.mp.dps * mp.log(10) + 6) / (2 * pi * y))) + 2),
        "tol": mp.mpf(10) ** (-(mp.mp.dps + 5)),
        "cwt_cache": {},
        "th_cache": {},
    }


def theta_char(al, be, ctx):
    kdig = max(18, mp.mp.dps - 3)
    key = (mp.nstr(al, kdig), mp.nstr(be, kdig))
    cached = ctx["th_cache"].get(key)
    if cached is not None:
        return cached
    I = mp.mpc(0, 1)
    pi = mp.pi
    tau = ctx["tau"]
    tol = ctx["tol"]
    n0 = -int(mp.nint(al))
    s = mp.mpc(0)
    k = 0
    while True:
        ns = [n0] if k == 0 else [n0 - k, n0 + k]
        add = mp.mpc(0)
        for n in ns:
            m = n + al
            add += mp.exp(I * pi * tau * m * m + 2 * I * pi * m * be)
        s += add
        if abs(add) < tol and k > 2:
            break
        k += 1
    ctx["th_cache"][key] = s
    return s


def theta1_logderiv(z, ctx):
    pi = mp.pi
    qh = ctx["qh"]
    tol = ctx["tol"]
    u = pi * z
    s1 = mp.sin(u)
    c1 = mp.cos(u)
    s2 = 2 * s1 * c1
    c2 = 2 * c1 * c1 - 1
    sn = s1
    cn = c1
    sgn = mp.mpf(1)
    qp = mp.mpc(1)
    th = sn
    thp = cn
    n = 1
    while True:
        qp *= qh ** (2 * n)
        sgn = -sgn
        sn, cn = sn * c2 + cn * s2, cn * c2 - sn * s2
        m = 2 * n + 1
        term = sgn * qp
        th += term * sn
        thp += term * m * cn
        if abs(term) * m * max(mp.mpf(1), abs(sn) + abs(cn)) < tol:
            break
        n += 1
    return pi * thp / th


_DIGAMMA_SYM_CACHE = {}


def Fu_kronecker(al, be, ctx):
    y = ctx["y"]
    x = ctx["x"]
    pi = mp.pi
    I = mp.mpc(0, 1)
    if al == 0:
        tot = pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + y * pi * pi / (mp.sin(pi * be) ** 2)
    else:
        dkey = (mp.mp.dps, mp.nstr(al, max(18, mp.mp.dps - 3)))
        dg = _DIGAMMA_SYM_CACHE.get(dkey)
        if dg is None:
            dg = mp.digamma(al) + mp.digamma(1 - al)
            _DIGAMMA_SYM_CACHE[dkey] = dg
        tot = -pi * (2 * mp.log(2) + mp.log(y) + dg)
    k_max = ctx["Fu_kmax"]
    for k in range(-k_max, k_max + 1):
        m = al + k
        if m == 0:
            continue
        wm = mp.exp(-2 * pi * abs(m) * y + 2 * I * pi * (m * x + be))
        tot += (2 * pi / abs(m)) * mp.re(wm / (1 - wm))
    return tot


def eval_sqrt_arg_cached(al, be, ctx):
    """Exact per-tau cached sqrt(max(0, 2*pi*L2 + c_wt(al, be))). Only ~100 distinct keys on E[30]!"""
    kdig = max(18, mp.mp.dps - 3)
    key = (mp.nstr(al, kdig), mp.nstr(be, kdig))
    cached = ctx["cwt_cache"].get(key)
    if cached is not None:
        return cached
    I = mp.mpc(0, 1)
    pi = mp.pi
    z = al * ctx["tau"] + be
    a0 = 2 * I * pi * al + theta1_logderiv(z, ctx)
    cwt = Fu_kronecker(al, be, ctx) + ctx["cwt_const"] - pi * (abs(a0) ** 2) * ctx["em2L2"]
    arg = ctx["two_pi_L2"] + cwt
    res = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
    ctx["cwt_cache"][key] = res
    return res


def eval_u_channels(ctx, a, b, qL, qR):
    I = mp.mpc(0, 1)
    pi = mp.pi
    H = mp.mpf(1) / 2
    ap = (qL + qR) * a
    am = (qL - qR) * a
    bp = (qL + qR) * b
    bm = (qL - qR) * b
    ef = mp.exp(-2 * I * pi * qL * a)
    kaps = [-I * ef, mp.mpc(-1), -ef, I]
    shifts = [(H, H), (H, mp.mpf(0)), (mp.mpf(0), H), (mp.mpf(0), mp.mpf(0))]
    hiz_tol = mp.mpf(10) ** (-(mp.mp.dps - 6))
    us = []
    for idx in range(4):
        da, db = shifts[idx]
        ca, cb = ap + da, bp + db
        da_, db_ = am + da, bm + db
        hiz_c = (abs((ca - H) - mp.nint(ca - H)) < hiz_tol and abs((cb - H) - mp.nint(cb - H)) < hiz_tol)
        hiz_d = (abs((da_ - H) - mp.nint(da_ - H)) < hiz_tol and abs((db_ - H) - mp.nint(db_ - H)) < hiz_tol)
        if hiz_c or hiz_d:
            us.append(mp.mpc(0))
            continue
        Rs = kaps[idx] * theta_char(ca, cb, ctx) * theta_char(da_, db_, ctx) * ctx["inv_2pi_et3"]
        al = (ca - H) % 1
        be = (cb - H) % 1
        if abs(al) < hiz_tol or abs(al - 1) < hiz_tol:
            al = mp.mpf(0)
        if abs(be) < hiz_tol or abs(be - 1) < hiz_tol:
            be = mp.mpf(0)
        sq = eval_sqrt_arg_cached(al, be, ctx)
        us.append(sq * Rs if sq > 0 else mp.mpc(0))
    return us


def assemble_Y_basis(alg, ctx, a, b, qL, qR, weight_zero=True):
    us = eval_u_channels(ctx, a, b, qL, qR)
    scale = (ctx["sqy"] if weight_zero else mp.mpf(1)) * ctx["c_norm"]
    T_p = alg["T_p"]
    basis = []
    for p in range(3):
        Y = mp.matrix(3, 3)
        Tp = T_p[p]
        for ia in range(3):
            for ib in range(3):
                Tp_ab = Tp[ia][ib]
                Y[ia, ib] = scale * (Tp_ab[0] * us[0] + Tp_ab[1] * us[1] + Tp_ab[2] * us[2] + Tp_ab[3] * us[3])
        basis.append(Y)
    return basis


def eval_Y_canonical(alg, ctx, a, b, qL, qR, weight_zero=True):
    us = eval_u_channels(ctx, a, b, qL, qR)
    scale = ctx["sqy"] if weight_zero else mp.mpf(1)
    c0, c1, c2 = ctx["c_vec"]
    T_p = alg["T_p"]
    Y = mp.matrix(3, 3)
    for ia in range(3):
        for ib in range(3):
            v0 = T_p[0][ia][ib]
            v1 = T_p[1][ia][ib]
            v2 = T_p[2][ia][ib]
            s0 = v0[0] * us[0] + v0[1] * us[1] + v0[2] * us[2] + v0[3] * us[3]
            s1 = v1[0] * us[0] + v1[1] * us[1] + v1[2] * us[2] + v1[3] * us[3]
            s2 = v2[0] * us[0] + v2[1] * us[1] + v2[2] * us[2] + v2[3] * us[3]
            Y[ia, ib] = scale * (c0 * s0 + c1 * s1 + c2 * s2)
    return Y


def extract_observables(Yu, Yd, Ye):
    su, Uu, _ = jw_svd(Yu)
    sd, Ud, _ = jw_svd(Yd)
    se, Ue, _ = jw_svd(Ye)
    V = mat_mul_3(mat_dag(Uu), Ud)
    absV = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    j_cp = jarlskog(V)
    cut = mp.mpf(10) ** (-(mp.mp.dps - 4))
    ok = (
        su[2] > cut and sd[2] > cut and se[2] > cut
        and su[0] > cut and sd[0] > cut and se[0] > cut
        and absV[0][1] > cut and absV[1][2] > cut and absV[0][2] > cut
    )
    vec9 = None
    if ok:
        vec9 = [
            mp.log(su[1] / su[2]), mp.log(su[0] / su[2]),
            mp.log(sd[1] / sd[2]), mp.log(sd[0] / sd[2]),
            mp.log(se[1] / se[2]), mp.log(se[0] / se[2]),
            mp.log(absV[0][1]), mp.log(absV[1][2]), mp.log(absV[0][2]),
        ]
    return {
        "su": su, "sd": sd, "se": se,
        "V": V, "absV": absV, "J_CP": j_cp,
        "vec9": vec9,
        "min_diag": min(absV[0][0], absV[1][1], absV[2][2]),
        "u_m2m3": su[1] / su[2] if su[2] > 0 else mp.mpf(0),
        "u_m1m3": su[0] / su[2] if su[2] > 0 else mp.mpf(0),
        "d_m2m3": sd[1] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "d_m1m3": sd[0] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "e_m2m3": se[1] / se[2] if se[2] > 0 else mp.mpf(0),
        "e_m1m3": se[0] / se[2] if se[2] > 0 else mp.mpf(0),
    }


def b1980_dist(u, v):
    mx = mp.mpf(0)
    for k in range(9):
        denom = max(mp.mpf(1), abs(u[k]))
        d = abs(u[k] - v[k]) / denom
        if d > mx:
            mx = d
    return mx


# ============================================================================
# 4. EXACT SYMBOLIC TROPICAL CLASSIFIER (ALL 288 PAIRS OF E[30]_prim)
# ============================================================================

def frac_mod1(x):
    return x - (x.numerator // x.denominator)


def nearest_shift_frac(x):
    r = frac_mod1(x)
    n_floor = -(x.numerator // x.denominator)
    H = Fraction(1, 2)
    if r == H:
        return [(H, n_floor), (-H, n_floor - 1)]
    elif r < H:
        return [(r, n_floor)]
    return [(r - 1, n_floor - 1)]


def is_hiz_frac(a, b):
    H = Fraction(1, 2)
    return frac_mod1(a - H) == 0 and frac_mod1(b - H) == 0


def pair_valuations_exact(a, b, qL, qR, is_A):
    H = Fraction(1, 2)
    ap = (qL + qR) * a
    am = (qL - qR) * a
    bp = (qL + qR) * b
    bm = (qL - qR) * b
    da = H if is_A else Fraction(0)
    hiz1 = is_hiz_frac(ap + da, bp + H) or is_hiz_frac(am + da, bm + H)
    hiz2 = is_hiz_frac(ap + da, bp) or is_hiz_frac(am + da, bm)
    mc = nearest_shift_frac(ap + da)
    md = nearest_shift_frac(am + da)
    dc = abs(mc[0][0])
    dd = abs(md[0][0])
    v0 = dc * dc + dd * dd - Fraction(1, 4)
    if hiz1 and hiz2:
        return None, None, True
    if hiz1 or hiz2:
        return v0, v0, True
    if dc < H and dd < H:
        parity = (mc[0][1] + md[0][1] + int(2 * da)) % 2
        dv = min(1 - 2 * dc, 1 - 2 * dd)
        return (v0, v0 + dv, False) if parity == 0 else (v0 + dv, v0, False)
    return v0, v0, False


def tmin(vals):
    vs = [v for v in vals if v is not None]
    return min(vs) if vs else None


def tadd(x, y):
    return None if (x is None or y is None) else (x + y)


def gram_top_vec_frac(M):
    G = [[tmin([tadd(M[i][k], M[j][k]) for k in range(3)]) for j in range(3)] for i in range(3)]
    min_diag = min(G[i][i] for i in range(3))
    ps = [i for i in range(3) if G[i][i] == min_diag]
    return [tmin([G[i][p] - min_diag for p in ps]) for i in range(3)]


def sector_tropical_exact(a, b, qL, qR):
    Ap, Am, hA = pair_valuations_exact(a, b, qL, qR, True)
    Bp, Bm, hB = pair_valuations_exact(a, b, qL, qR, False)
    q1 = Fraction(1, 4)
    q2 = Fraction(1, 2)
    q3 = Fraction(3, 4)
    q5 = Fraction(5, 4)
    q7 = Fraction(7, 4)
    Ye = [
        [tmin([tadd(Bm, -q1), tadd(Ap, q1), tadd(Am, q1), tadd(Bp, q3)]),
         tmin([tadd(Bm, q1), tadd(Ap, q3)]),
         tadd(Am, -q1)],
        [tmin([tadd(Ap, -q1), tadd(Bp, q1), tadd(Am, q7)]),
         tmin([tadd(Ap, q1), tadd(Bm, q7)]),
         tadd(Bp, -q1)],
        [tmin([tadd(Am, q3), tadd(Bp, q5)]),
         tmin([tadd(Bm, q3), tadd(Ap, q5)]),
         None],
    ]
    Cof = [
        [tmin([tadd(tadd(Ap, Bp), 1), tadd(tadd(Bp, Bm), q2)]),
         tmin([tadd(tadd(Am, Bp), q2), tadd(tadd(Bp, Bp), 1)]),
         tmin([tadd(tadd(Ap, Ap), 1), tadd(tadd(Ap, Am), 1), tadd(tadd(Ap, Bm), q2), tadd(tadd(Bp, Bm), 1)])],
        [tmin([tadd(tadd(Ap, Am), 1), tadd(tadd(Ap, Bp), Fraction(3, 2)), tadd(tadd(Am, Bm), q2), tadd(tadd(Bp, Bm), 1)]),
         tmin([tadd(tadd(Am, Am), q2), tadd(tadd(Am, Bp), 2), tadd(tadd(Bp, Bp), Fraction(3, 2))]),
         tmin([tadd(tadd(Ap, Ap), Fraction(3, 2)), tadd(tadd(Ap, Am), Fraction(3, 2)), tadd(tadd(Ap, Bm), 2),
               tadd(tadd(Bp, Bm), Fraction(3, 2)), tadd(tadd(Bm, Bm), q2)])],
        [tmin([tadd(Ap, Am), tadd(tadd(Ap, Bp), q2), tadd(tadd(Am, Bm), Fraction(3, 2)), tadd(Bp, Bm)]),
         tmin([tadd(tadd(Ap, Am), -q2), tadd(tadd(Am, Am), Fraction(3, 2)), tadd(tadd(Am, Bp), 1),
               tadd(tadd(Bp, Bp), q2), tadd(tadd(Bp, Bm), -q2)]),
         tmin([tadd(tadd(Ap, Ap), q2), tadd(tadd(Ap, Am), q2), tadd(tadd(Ap, Bm), 1),
               tadd(tadd(Bp, Bm), q2), tadd(tadd(Bm, Bm), Fraction(3, 2))])],
    ]
    v_det = tadd(q2, tadd(tmin([tadd(Ap, Am), tadd(Bp, Bm)]),
                          tmin([tadd(Am, q1), tadd(Ap, q1), tadd(Bm, -q1), tadd(Bp, q3)])))
    v_s3 = tmin([v for row in Ye for v in row])
    v_s3s2 = tmin([v for row in Cof for v in row])
    v_s2 = v_s3s2 - v_s3
    v_s1 = v_det - v_s3s2
    u3 = gram_top_vec_frac(Ye)
    u1 = gram_top_vec_frac(Cof)
    u2 = [
        tmin([tadd(u3[1], u1[2]), tadd(u3[2], u1[1])]),
        tmin([tadd(u3[2], u1[0]), tadd(u3[0], u1[2])]),
        tmin([tadd(u3[0], u1[1]), tadd(u3[1], u1[0])]),
    ]
    m2 = min(u2)
    u2 = [x - m2 for x in u2]
    return {"v_s3": v_s3, "v_s2": v_s2, "v_s1": v_s1, "u1": u1, "u2": u2, "u3": u3, "has_hiz": (hA or hB)}


def classify_point_tropical(a_i, b_i, N=30):
    a = Fraction(a_i, N)
    b = Fraction(b_i, N)
    u = sector_tropical_exact(a, b, 1, -4)
    d = sector_tropical_exact(a, b, 1, 2)
    e = sector_tropical_exact(a, b, -3, 6)
    uu = [u["u1"], u["u2"], u["u3"]]
    ud = [d["u1"], d["u2"], d["u3"]]
    V = [[min(uu[i][k] + ud[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
    rates9 = (
        u["v_s2"] - u["v_s3"], u["v_s1"] - u["v_s3"],
        d["v_s2"] - d["v_s3"], d["v_s1"] - d["v_s3"],
        e["v_s2"] - e["v_s3"], e["v_s1"] - e["v_s3"],
        V[0][1], V[1][2], V[0][2],
    )
    e_D2 = (e["v_s2"] - e["v_s3"]) - (d["v_s2"] - d["v_s3"])
    e_norm = min(u["v_s3"], d["v_s3"], e["v_s3"])
    rates10 = rates9 + (e_D2,)
    aligned = (V[0][0] == 0 and V[1][1] == 0 and V[2][2] == 0
               and V[0][1] > 0 and V[1][2] > 0 and V[0][2] > 0)
    hier_ud = (rates9[0] > 0 and rates9[2] > 0 and rates9[1] > rates9[0] and rates9[3] > rates9[2])
    std_order_non_add = (V[0][1] > 0 and V[0][1] < V[1][2] < V[0][2])
    std_wolf_additive = (std_order_non_add and V[0][2] == V[0][1] + V[1][2])
    small_v23 = (Fraction(0) < V[1][2] < Fraction(1, 10))
    return {
        "rates9": rates9, "rates10": rates10, "e_D2": e_D2, "e_norm": e_norm,
        "aligned": aligned, "hier_ud": hier_ud,
        "std_order_non_add": std_order_non_add, "std_wolf_additive": std_wolf_additive,
        "small_v23": small_v23, "has_hiz": (u["has_hiz"] or d["has_hiz"] or e["has_hiz"]),
    }


# ============================================================================
# 5. LEVEL-30 SETS & MODULE W1
# ============================================================================

def generate_P30():
    K5 = [(12, 24), (18, 6), (6, 12), (24, 18)]
    E6p = [(5 * j, 5 * k) for j in range(6) for k in range(6) if gcd_int(gcd_int(j, k), 6) == 1]
    pts = sorted({((x1 + x2) % 30, (y1 + y2) % 30) for x1, y1 in K5 for x2, y2 in E6p})
    pairs = sorted({min((a, b), ((-a) % 30, (-b) % 30)) for a, b in pts})
    return pts, pairs


def generate_E30_prim():
    pts = [(a, b) for a in range(30) for b in range(30) if gcd_int(gcd_int(a, b), 30) == 1]
    pairs = sorted({min((a, b), ((-a) % 30, (-b) % 30)) for a, b in pts})
    return pts, pairs


def full_m_orbit(p):
    """Exact closed M-orbit of antipodal pair p = (a, b) in E[30]_prim / {+-1} under w -> w M^{-1}."""
    Minv = (1, 29, 29, 2)
    orb = []
    seen = set()
    c = min(p, ((-p[0]) % 30, (-p[1]) % 30))
    while c not in seen:
        seen.add(c)
        orb.append(c)
        na = (c[0] * Minv[0] + c[1] * Minv[2]) % 30
        nb = (c[0] * Minv[1] + c[1] * Minv[3]) % 30
        c = min((na, nb), ((-na) % 30, (-nb) % 30))
    return orb


def run_W1():
    t0 = time.monotonic_ns()
    out = {}

    # Part A: Exact algebra in PSL(2, Z/30)
    def mat_mod30(A, B):
        return (
            (A[0] * B[0] + A[1] * B[2]) % 30,
            (A[0] * B[1] + A[1] * B[3]) % 30,
            (A[2] * B[0] + A[3] * B[2]) % 30,
            (A[2] * B[1] + A[3] * B[3]) % 30,
        )

    def psl_canon(A):
        nA = ((-A[0]) % 30, (-A[1]) % 30, (-A[2]) % 30, (-A[3]) % 30)
        return min(A, nA)

    M_mat = (2, 1, 1, 1)
    I_psl = psl_canon((1, 0, 0, 1))
    cur = (1, 0, 0, 1)
    psl_order = 0
    traces_1_12 = []
    elliptic_count = 0
    for k in range(1, 121):
        cur = mat_mod30(cur, M_mat)
        tr = (cur[0] + cur[3]) % 30
        if k <= 12:
            traces_1_12.append(tr)
        if tr in (0, 1, 29) or ((-tr) % 30) in (0, 1, 29):
            elliptic_count += 1
        if psl_canon(cur) == I_psl:
            psl_order = k
            break

    Minv = (1, 29, 29, 2)
    Minv12 = (1, 0, 0, 1)
    for _ in range(12):
        Minv12 = mat_mod30(Minv12, Minv)

    def act_pair(p, g):
        a, b = p
        na = (a * g[0] + b * g[2]) % 30
        nb = (a * g[1] + b * g[3]) % 30
        return min((na, nb), ((-na) % 30, (-nb) % 30))

    _, prim_pairs = generate_E30_prim()
    P30_pts, P30_pairs = generate_P30()
    visited = set()
    orbit_sizes = []
    for p in prim_pairs:
        if p in visited:
            continue
        orb = full_m_orbit(p)
        for q in orb:
            visited.add(q)
        orbit_sizes.append(len(orb))
    orbit_hist = {}
    for sz in orbit_sizes:
        orbit_hist[str(sz)] = orbit_hist.get(str(sz), 0) + 1

    m12_fixed = sorted([p for p in prim_pairs if act_pair(p, Minv12) == p])
    m12_equals_P30 = (m12_fixed == P30_pairs)
    expected_traces = [3, 7, 18, 17, 3, 22, 3, 17, 18, 7, 3, 2]
    part_a_pass = (
        psl_order == 60
        and traces_1_12 == expected_traces
        and elliptic_count == 0
        and len(prim_pairs) == 288
        and orbit_hist == {"12": 4, "60": 4}
        and len(m12_fixed) == 48
        and m12_equals_P30
    )
    out["part_A"] = {
        "M_order_PSL2_Z30": psl_order,
        "trace_cycle_1_to_12": traces_1_12,
        "elliptic_elements_in_Mk_Gamma30": elliptic_count,
        "cusps_X30_count": len(prim_pairs),
        "orbit_length_histogram": orbit_hist,
        "M12_fixed_cusps_count": len(m12_fixed),
        "P30_points_count": len(P30_pts),
        "M12_fixed_equals_P30_mod_pm1": m12_equals_P30,
        "pass": part_a_pass,
    }

    # Part B1: Direct unreduced GL8 L_2(iy) vs L_2(i/y)
    axis_pairs = [
        (Fraction(5, 4), Fraction(4, 5)),
        (Fraction(3, 2), Fraction(2, 3)),
        (Fraction(5, 2), Fraction(2, 5)),
    ]
    raw_cocycle_checks = []
    L2_axis_high = {}
    max_cocycle_err = mp.mpf(0)
    with mp.workdps(30):
        for y_f, iy_f in axis_pairs:
            yv = mp.mpf(y_f.numerator) / y_f.denominator
            iyv = mp.mpf(iy_f.numerator) / iy_f.denominator
            r_hi = solve_fuchsian_gl8(mp.mpc(0, yv), dps=30)
            r_lo = solve_fuchsian_gl8(mp.mpc(0, iyv), dps=30)
            diff = abs(r_lo["L2"] - (r_hi["L2"] + mp.log(yv)))
            if diff > max_cocycle_err:
                max_cocycle_err = diff
            L2_axis_high[frac_str(y_f)] = r_hi["L2"]
            _L2_CACHE[(mp.nstr(mp.mpf(0), 18), mp.nstr(yv, 18))] = r_hi["L2"]
            raw_cocycle_checks.append({
                "pair": f"({frac_str(y_f)}, {frac_str(iy_f)})",
                "L2_iy": mp_str(r_hi["L2"], 22),
                "L2_i_over_y_raw_gl8": mp_str(r_lo["L2"], 22),
                "L2_iy_plus_ln_y": mp_str(r_hi["L2"] + mp.log(yv), 22),
                "abs_cocycle_err": mp_str(diff, 10),
            })

    # Part B2: Frame C dps=55 S-covariance on all 96/96 points of P_30
    s_cov_results = []
    max_s_cov_9log = mp.mpf(0)
    with mp.workdps(55):
        alg55 = build_frame_c_algebra()
        for y_f, iy_f in axis_pairs:
            yv = mp.mpf(y_f.numerator) / y_f.denominator
            iyv = mp.mpf(iy_f.numerator) / iy_f.denominator
            L2_y = mp.mpf(L2_axis_high[frac_str(y_f)])
            L2_iy = L2_y + mp.log(yv)
            ctx_y = make_tau_ctx(mp.mpc(0, yv), L2_val=L2_y)
            ctx_iy = make_tau_ctx(mp.mpc(0, iyv), L2_val=L2_iy)
            obs_y_map = {}
            obs_iy_map = {}
            for p in P30_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                obs_y_map[p] = extract_observables(
                    eval_Y_canonical(alg55, ctx_y, am, bm, 1, -4),
                    eval_Y_canonical(alg55, ctx_y, am, bm, 1, 2),
                    eval_Y_canonical(alg55, ctx_y, am, bm, -3, 6),
                )["vec9"]
                obs_iy_map[p] = extract_observables(
                    eval_Y_canonical(alg55, ctx_iy, am, bm, 1, -4),
                    eval_Y_canonical(alg55, ctx_iy, am, bm, 1, 2),
                    eval_Y_canonical(alg55, ctx_iy, am, bm, -3, 6),
                )["vec9"]
            pair_max = mp.mpf(0)
            count_ok = 0
            for a_i, b_i in P30_pts:
                p_orig = min((a_i, b_i), ((-a_i) % 30, (-b_i) % 30))
                wp_a, wp_b = (-b_i) % 30, a_i % 30
                p_img = min((wp_a, wp_b), ((-wp_a) % 30, (-wp_b) % 30))
                d9 = b1980_dist(obs_y_map[p_orig], obs_iy_map[p_img])
                if d9 > pair_max:
                    pair_max = d9
                if d9 < mp.mpf(10) ** (-38):
                    count_ok += 1
            if pair_max > max_s_cov_9log:
                max_s_cov_9log = pair_max
            s_cov_results.append({
                "pair": f"({frac_str(y_f)}, {frac_str(iy_f)})",
                "points_checked": len(P30_pts),
                "points_under_1e_38": count_ok,
                "max_9log_dist": mp_str(pair_max, 12),
            })

    # Part B3: Full-norm weight-0 s_k^{inv} invariance under T, S, M at tau_1 and tau_0
    gens = {"T": (1, 1, 0, 1), "S": (0, -1, 1, 0), "M": (2, 1, 1, 1)}
    test_taus = [
        ("tau1", mp.mpc(mp.mpf(13) / 100, mp.mpf(6) / 5)),
        ("tau0", mp.mpc(mp.mpf(-9) / 10, mp.mpf(6) / 5)),
    ]
    full_norm_checks = []
    max_full_norm_err = mp.mpf(0)
    with mp.workdps(55):
        alg55 = build_frame_c_algebra()
        w_a, w_b = mp.mpf(4) / 15, mp.mpf(1) / 30
        for tname, tau_v in test_taus:
            L2_0 = get_L2(tau_v, solve_dps=30)
            ctx0 = make_tau_ctx(tau_v, L2_val=L2_0)
            s_base = []
            for qL, qR in [(1, -4), (1, 2), (-3, 6)]:
                s_base.extend(jw_svd(eval_Y_canonical(alg55, ctx0, w_a, w_b, qL, qR, weight_zero=True))[0])
            for gname, (ga, gb, gc, gd) in gens.items():
                tau_g = (ga * tau_v + gb) / (gc * tau_v + gd)
                L2_g = L2_0 + mp.log(abs(gc * tau_v + gd))
                wa_g = (gd * w_a - gc * w_b) % 1
                wb_g = (-gb * w_a + ga * w_b) % 1
                ctxg = make_tau_ctx(tau_g, L2_val=L2_g)
                s_img = []
                for qL, qR in [(1, -4), (1, 2), (-3, 6)]:
                    s_img.extend(jw_svd(eval_Y_canonical(alg55, ctxg, wa_g, wb_g, qL, qR, weight_zero=True))[0])
                rel_err = max(abs(s_img[k] - s_base[k]) / s_base[k] for k in range(9))
                if rel_err > max_full_norm_err:
                    max_full_norm_err = rel_err
                full_norm_checks.append({
                    "tau": tname, "generator": gname, "max_rel_err_9_abs_sv": mp_str(rel_err, 12),
                })

    # Part B4: Corrected K != 1 duality audit (12 exact P_30 class reps & all 48 P_30 pairs vs all 451 E[30] antipodal pts)
    e30_nz_pairs = sorted({
        min((a, b), ((-a) % 30, (-b) % 30))
        for a in range(30) for b in range(30)
        if not (a == 0 and b == 0)
    })
    # Pick 12 exact class representatives of P_30 (one per distinct tropical class on P_30)
    seen_p30_cls = set()
    p30_12_reps = []
    for p in P30_pairs:
        cl = classify_point_tropical(p[0], p[1], 30)["rates9"]
        if cl not in seen_p30_cls:
            seen_p30_cls.add(cl)
            p30_12_reps.append(p)

    k_values = [2, 3, 5, 6, 10, 15, 30]
    k_duality_rows = []
    min_k_max_d = mp.mpf(10**9)
    p30_12_set = set(p30_12_reps)
    for K in k_values:
        dps_K = 28 if K <= 5 else (38 if K <= 15 else 52)
        with mp.workdps(dps_K):
            algK = build_frame_c_algebra()
            sqK = mp.sqrt(mp.mpf(K))
            y1 = mp.mpf(3) * sqK / 2
            y2 = mp.mpf(2) * sqK / 3
            ctx1 = make_tau_ctx(mp.mpc(0, y1), solve_dps=28)
            ctx2 = make_tau_ctx(mp.mpc(0, y2), solve_dps=28)
            e30_vecs = []
            for p in e30_nz_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                obs = extract_observables(
                    eval_Y_canonical(algK, ctx2, am, bm, 1, -4),
                    eval_Y_canonical(algK, ctx2, am, bm, 1, 2),
                    eval_Y_canonical(algK, ctx2, am, bm, -3, 6),
                )
                if obs["vec9"] is not None:
                    e30_vecs.append(obs["vec9"])
            best_ds_48 = []
            best_ds_12 = []
            for p in P30_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                v1 = extract_observables(
                    eval_Y_canonical(algK, ctx1, am, bm, 1, -4),
                    eval_Y_canonical(algK, ctx1, am, bm, 1, 2),
                    eval_Y_canonical(algK, ctx1, am, bm, -3, 6),
                )["vec9"]
                if v1 is None:
                    raise RuntimeError(f"W1 Part B4 underflow at K={K} p={p} dps={dps_K}")
                md = min(b1980_dist(v1, v2) for v2 in e30_vecs)
                best_ds_48.append(md)
                if p in p30_12_set:
                    best_ds_12.append(md)
            mx_48 = max(best_ds_48)
            med_48 = median_mpf(best_ds_48)
            mn_48 = min(best_ds_48)
            mx_12 = max(best_ds_12)
            med_12 = median_mpf(best_ds_12)
            mn_12 = min(best_ds_12)
            if mx_48 < min_k_max_d:
                min_k_max_d = mx_48
            k_duality_rows.append({
                "K": K,
                "dps_used": dps_K,
                "y": mp_str(y1, 12), "y_prime": mp_str(y2, 12),
                "L2_y": mp_str(ctx1["L2"], 14), "L2_y_prime": mp_str(ctx2["L2"], 14),
                "max_d_all48_P30_vs_all899": mp_str(mx_48, 10),
                "median_d_all48_P30_vs_all899": mp_str(med_48, 10),
                "min_d_all48_P30_vs_all899": mp_str(mn_48, 10),
                "max_d_12classes_vs_all899": mp_str(mx_12, 10),
                "median_d_12classes_vs_all899": mp_str(med_12, 10),
                "min_d_12classes_vs_all899": mp_str(mn_12, 10),
            })

    out["part_B"] = {
        "raw_gl8_cocycle_checks": raw_cocycle_checks,
        "max_raw_cocycle_err": mp_str(max_cocycle_err, 10),
        "s_covariance_96pts": s_cov_results,
        "max_s_cov_9log_dist": mp_str(max_s_cov_9log, 12),
        "full_norm_weight0_invariance": full_norm_checks,
        "max_full_norm_rel_err": mp_str(max_full_norm_err, 12),
        "K_neq_1_duality_audit": k_duality_rows,
        "p30_class_reps_count": len(p30_12_reps),
        "min_K_neq_1_max_d": mp_str(min_k_max_d, 10),
        "no_K_neq_1_duality": bool(min_k_max_d > mp.mpf(1) / 10),
    }
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 6. MODULE W2: WHOLE LEVEL-30 (288 PAIRS), 3 CLOSED GEODESIC ORBITS, W-LV1, B1981
# ============================================================================

def run_W2():
    t0 = time.monotonic_ns()
    out = {}
    _, prim_pairs = generate_E30_prim()
    _, P30_pairs = generate_P30()
    act_set = set(P30_pairs)

    # W2.1a: Exact symbolic tropical classification across all 288 pairs
    classes9_all, classes9_act, classes9_off = set(), set(), set()
    sym_counts = {
        "all_288": {"total": 0, "aligned": 0, "hier_ud": 0, "hier_aligned": 0, "hiz_zero": 0, "small_v23": 0, "std_non_add": 0, "std_additive": 0, "e_norm_neg": 0},
        "act_48": {"total": 0, "aligned": 0, "hier_ud": 0, "hier_aligned": 0, "hiz_zero": 0, "small_v23": 0, "std_non_add": 0, "std_additive": 0, "e_norm_neg": 0},
        "off_240": {"total": 0, "aligned": 0, "hier_ud": 0, "hier_aligned": 0, "hiz_zero": 0, "small_v23": 0, "std_non_add": 0, "std_additive": 0, "e_norm_neg": 0},
    }
    min_e_norm = None
    max_e_norm = None
    for a_i, b_i in prim_pairs:
        c = classify_point_tropical(a_i, b_i, 30)
        is_act = (a_i, b_i) in act_set
        classes9_all.add(c["rates9"])
        if is_act:
            classes9_act.add(c["rates9"])
        else:
            classes9_off.add(c["rates9"])
        en = c["e_norm"]
        if min_e_norm is None or en < min_e_norm:
            min_e_norm = en
        if max_e_norm is None or en > max_e_norm:
            max_e_norm = en
        for bucket in ("all_288", "act_48" if is_act else "off_240"):
            db = sym_counts[bucket]
            db["total"] += 1
            if c["aligned"]:
                db["aligned"] += 1
            if c["hier_ud"]:
                db["hier_ud"] += 1
            if c["aligned"] and c["hier_ud"]:
                db["hier_aligned"] += 1
            if c["has_hiz"]:
                db["hiz_zero"] += 1
            if c["small_v23"]:
                db["small_v23"] += 1
            if c["std_order_non_add"]:
                db["std_non_add"] += 1
            if c["std_wolf_additive"]:
                db["std_additive"] += 1
            if en < 0:
                db["e_norm_neg"] += 1

    out["symbolic_tropical_288"] = {
        "distinct_classes_all": len(classes9_all),
        "distinct_classes_act48": len(classes9_act),
        "distinct_classes_off240": len(classes9_off),
        "counts": sym_counts,
        "e_norm_min": frac_str(min_e_norm),
        "e_norm_max": frac_str(max_e_norm),
    }

    # W2.1b: Finite-height Frame C across all 288 pairs at y=2 and y=3 (x=13/100)
    finite_scans = {}
    with mp.workdps(32):
        alg32 = build_frame_c_algebra()
        for y_int in (2, 3):
            tau_y = mp.mpc(mp.mpf(13) / 100, mp.mpf(y_int))
            ctx_y = make_tau_ctx(tau_y, solve_dps=30)
            counts = {
                "all_288": {"total": 0, "aligned": 0, "hier_ud": 0, "e_neq_d": 0, "std_ckm": 0, "all4": 0},
                "act_48": {"total": 0, "aligned": 0, "hier_ud": 0, "e_neq_d": 0, "std_ckm": 0, "all4": 0},
                "off_240": {"total": 0, "aligned": 0, "hier_ud": 0, "e_neq_d": 0, "std_ckm": 0, "all4": 0},
            }
            for a_i, b_i in prim_pairs:
                am, bm = mp.mpf(a_i) / 30, mp.mpf(b_i) / 30
                obs = extract_observables(
                    eval_Y_canonical(alg32, ctx_y, am, bm, 1, -4),
                    eval_Y_canonical(alg32, ctx_y, am, bm, 1, 2),
                    eval_Y_canonical(alg32, ctx_y, am, bm, -3, 6),
                )
                absV = obs["absV"]
                is_aligned = obs["min_diag"] >= mp.mpf(9) / 10
                is_hier = (obs["u_m2m3"] < mp.mpf(1) / 5) and (obs["d_m2m3"] < mp.mpf(1) / 5)
                D2 = obs["e_m2m3"] / obs["d_m2m3"] if obs["d_m2m3"] > 0 else mp.mpf(1)
                is_e_neq_d = abs(mp.log(D2)) > mp.mpf(1) / 10
                is_std_ckm = (absV[0][1] > absV[1][2]) and (absV[1][2] > absV[0][2])
                is_all4 = is_aligned and is_hier and is_e_neq_d and is_std_ckm
                is_act = (a_i, b_i) in act_set
                for bucket in ("all_288", "act_48" if is_act else "off_240"):
                    db = counts[bucket]
                    db["total"] += 1
                    if is_aligned:
                        db["aligned"] += 1
                    if is_hier:
                        db["hier_ud"] += 1
                    if is_e_neq_d:
                        db["e_neq_d"] += 1
                    if is_std_ckm:
                        db["std_ckm"] += 1
                    if is_all4:
                        db["all4"] += 1
            finite_scans[f"y_{y_int}"] = {
                "tau": f"13/100 + {y_int}i", "L2": mp_str(ctx_y["L2"], 18), "counts": counts,
            }
    out["finite_height_288"] = finite_scans

    # W2.2: Closed hyperbolic geodesic gamma_M(u) over ALL THREE true closed M-orbits!
    #   1) mark = (4/15, 1/30) = (8, 1)/30 [len 12]
    #   2) twin_p30 = (11/30, 2/5) = (11, 12)/30 [len 12, genuine P_30]
    #   3) off_1_5 = (1/30, 1/6) = (1, 5)/30 [full len 60, off-line]
    with mp.workdps(55):
        s5 = mp.sqrt(5)
        ell_M_55 = 4 * mp.log((1 + s5) / 2)

        def tau_geo55(u):
            return mp.mpc(mp.mpf(1) / 2 + (s5 / 2) * mp.tanh(u), (s5 / 2) * mp.sech(u))

        max_geo_period_err = max(
            abs((2 * tau_geo55(ut) + 1) / (tau_geo55(ut) + 1) - tau_geo55(ut + ell_M_55))
            for ut in (mp.mpf(0), mp.mpf(1) / 3, mp.mpf(-7) / 10)
        )

    geo_orbits_spec = [
        ("mark_8_1", (8, 1), 12),
        ("twin_p30_11_12", (11, 12), 12),
        ("off_1_5", (1, 5), 60),
    ]
    geo_results = {}
    max_all3_trace_shift_err = mp.mpf(0)
    with mp.workdps(28):
        alg28 = build_frame_c_algebra()
        s5 = mp.sqrt(5)
        ell_M = 4 * mp.log((1 + s5) / 2)

        def make_geo_ctxs(n_nodes, shift_frac):
            du = ell_M / n_nodes
            ctxs = []
            for j in range(n_nodes):
                u = -ell_M / 2 + (mp.mpf(j) + mp.mpf(1) / 2 + shift_frac) * du
                tu = mp.mpc(mp.mpf(1) / 2 + (s5 / 2) * mp.tanh(u), (s5 / 2) * mp.sech(u))
                ctxs.append(make_tau_ctx(tu, solve_dps=28))
            return ctxs

        ctxs_16 = make_geo_ctxs(16, mp.mpf(0))
        ctxs_16_sh = make_geo_ctxs(16, mp.mpf(1) / 3)
        ctxs_32 = make_geo_ctxs(32, mp.mpf(0))

        def eval_closed_orbit_on_grid(p_rep, orb, ctxs, do_full=True):
            n_nodes = len(ctxs)
            n_orb = len(orb)
            w_norm = mp.mpf(1) / (n_orb * n_nodes)
            sectors = [(1, -4), (1, 2), (-3, 6)]
            tr2 = [mp.mpf(0)] * 3
            tr4 = [mp.mpf(0)] * 3
            avg_obs = {k: mp.mpf(0) for k in ("u_m2m3", "u_m1m3", "d_m2m3", "d_m1m3", "e_m2m3", "e_m1m3", "V12", "V23", "V13", "J_CP", "min_diag")}
            HL = [mp.zeros(3, 3) for _ in range(3)]
            Ybar = [mp.zeros(3, 3) for _ in range(3)]
            am0, bm0 = mp.mpf(p_rep[0]) / 30, mp.mpf(p_rep[1]) / 30
            for ctx in ctxs:
                if do_full:
                    for si, (qL, qR) in enumerate(sectors):
                        Ybar[si] += eval_Y_canonical(alg28, ctx, am0, bm0, qL, qR) / n_nodes
                for wp in orb:
                    wam, wbm = mp.mpf(wp[0]) / 30, mp.mpf(wp[1]) / 30
                    Ys = [eval_Y_canonical(alg28, ctx, wam, wbm, qL, qR) for qL, qR in sectors]
                    for si in range(3):
                        H = mat_mul_3(mat_dag(Ys[si]), Ys[si])
                        tr2[si] += mp.re(mat_tr(H)) * w_norm
                        tr4[si] += mp.re(mat_tr(mat_mul_3(H, H))) * w_norm
                        if do_full:
                            HL[si] += mat_mul_3(Ys[si], mat_dag(Ys[si])) * w_norm
                    if do_full:
                        obs = extract_observables(Ys[0], Ys[1], Ys[2])
                        avg_obs["u_m2m3"] += obs["u_m2m3"] * w_norm
                        avg_obs["u_m1m3"] += obs["u_m1m3"] * w_norm
                        avg_obs["d_m2m3"] += obs["d_m2m3"] * w_norm
                        avg_obs["d_m1m3"] += obs["d_m1m3"] * w_norm
                        avg_obs["e_m2m3"] += obs["e_m2m3"] * w_norm
                        avg_obs["e_m1m3"] += obs["e_m1m3"] * w_norm
                        avg_obs["V12"] += obs["absV"][0][1] * w_norm
                        avg_obs["V23"] += obs["absV"][1][2] * w_norm
                        avg_obs["V13"] += obs["absV"][0][2] * w_norm
                        avg_obs["J_CP"] += obs["J_CP"] * w_norm
                        avg_obs["min_diag"] += obs["min_diag"] * w_norm
            res = {"tr2": tr2, "tr4": tr4}
            if do_full:
                ev_u, U_u = mp.eigh(HL[0])
                ev_d, U_d = mp.eigh(HL[1])
                ev_e, _ = mp.eigh(HL[2])
                su_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_u]
                sd_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_d]
                se_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_e]
                Vg = mat_mul_3(mat_dag(U_u), U_d)
                coh = extract_observables(Ybar[0], Ybar[1], Ybar[2])
                res["avg_obs"] = avg_obs
                res["gramian_HL"] = {
                    "u_m2m3": mp_str(su_g[1] / su_g[2], 14), "u_m1m3": mp_str(su_g[0] / su_g[2], 14),
                    "d_m2m3": mp_str(sd_g[1] / sd_g[2], 14), "d_m1m3": mp_str(sd_g[0] / sd_g[2], 14),
                    "e_m2m3": mp_str(se_g[1] / se_g[2], 14), "e_m1m3": mp_str(se_g[0] / se_g[2], 14),
                    "V12": mp_str(abs(Vg[0, 1]), 14), "V23": mp_str(abs(Vg[1, 2]), 14), "V13": mp_str(abs(Vg[0, 2]), 14),
                }
                res["coherent_Ybar"] = {
                    "u_m2m3": mp_str(coh["u_m2m3"], 14), "d_m2m3": mp_str(coh["d_m2m3"], 14),
                    "e_m2m3": mp_str(coh["e_m2m3"], 14),
                    "V12": mp_str(coh["absV"][0][1], 14), "V23": mp_str(coh["absV"][1][2], 14),
                    "V13": mp_str(coh["absV"][0][2], 14), "min_diag": mp_str(coh["min_diag"], 14),
                }
            return res

        for name, p_rep, exp_len in geo_orbits_spec:
            orb = full_m_orbit(p_rep)
            r16 = eval_closed_orbit_on_grid(p_rep, orb, ctxs_16, do_full=True)
            r16_sh = eval_closed_orbit_on_grid(p_rep, orb, ctxs_16_sh, do_full=False)
            sh_err_16 = max(
                max(abs(r16["tr2"][k] - r16_sh["tr2"][k]) / max(mp.mpf(1), r16["tr2"][k]) for k in range(3)),
                max(abs(r16["tr4"][k] - r16_sh["tr4"][k]) / max(mp.mpf(1), r16["tr4"][k]) for k in range(3)),
            )
            if sh_err_16 > max_all3_trace_shift_err:
                max_all3_trace_shift_err = sh_err_16
            conv_16_32 = None
            if len(orb) == 12:
                r32 = eval_closed_orbit_on_grid(p_rep, orb, ctxs_32, do_full=False)
                conv_16_32 = max(
                    max(abs(r16["tr2"][k] - r32["tr2"][k]) / max(mp.mpf(1), r32["tr2"][k]) for k in range(3)),
                    max(abs(r16["tr4"][k] - r32["tr4"][k]) / max(mp.mpf(1), r32["tr4"][k]) for k in range(3)),
                )
            geo_results[name] = {
                "rep_pair": list(p_rep),
                "orbit_length": len(orb),
                "expected_orbit_length": exp_len,
                "smooth_tr2_16": {"u": mp_str(r16["tr2"][0], 16), "d": mp_str(r16["tr2"][1], 16), "e": mp_str(r16["tr2"][2], 16)},
                "smooth_tr4_16": {"u": mp_str(r16["tr4"][0], 16), "d": mp_str(r16["tr4"][1], 16), "e": mp_str(r16["tr4"][2], 16)},
                "basepoint_shift_rel_err_16": mp_str(sh_err_16, 10),
                "conv_16_vs_32_traces": mp_str(conv_16_32, 10) if conv_16_32 is not None else None,
                "avg_obs_16": {k: mp_str(v, 14) for k, v in r16["avg_obs"].items()},
                "gramian_HL_16": r16["gramian_HL"],
                "coherent_Ybar_16": r16["coherent_Ybar"],
            }

    out["geodesic_gamma_M"] = {
        "ell_M": mp_str(ell_M_55, 22),
        "max_periodicity_err_M_tau": mp_str(max_geo_period_err, 10),
        "max_basepoint_shift_err_all3_closed_orbits": mp_str(max_all3_trace_shift_err, 10),
        "orbits": geo_results,
    }

    # W2.3a: W-LV1 direct cross-check
    wlv1_rows = []
    max_wlv1_neg_err = mp.mpf(0)
    with mp.workdps(55):
        alg55 = build_frame_c_algebra()
        ctx2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=30)
        for label, a_f, b_f in [
            ("N10_1_10_3_10", Fraction(1, 10), Fraction(3, 10)),
            ("N30_mark_4_15_1_30", Fraction(4, 15), Fraction(1, 30)),
            ("N30_twin_p30_11_30_2_5", Fraction(11, 30), Fraction(2, 5)),
        ]:
            am = mp.mpf(a_f.numerator) / a_f.denominator
            bm = mp.mpf(b_f.numerator) / b_f.denominator
            a3, b3 = (3 * am) % 1, (3 * bm) % 1
            Ye = eval_Y_canonical(alg55, ctx2, am, bm, -3, 6)
            Yd_neg = eval_Y_canonical(alg55, ctx2, a3, b3, -1, 2)
            Yd_pos = eval_Y_canonical(alg55, ctx2, a3, b3, 1, 2)
            al_neg = sum(mp.conj(Yd_neg[i, j]) * Ye[i, j] for i in range(3) for j in range(3)) / sum(abs(Yd_neg[i, j]) ** 2 for i in range(3) for j in range(3))
            rel_neg = mat_fro_norm(Ye - al_neg * Yd_neg) / mat_fro_norm(Ye)
            se, _, _ = jw_svd(Ye)
            sd_neg, _, _ = jw_svd(Yd_neg)
            sd_pos, _, _ = jw_svd(Yd_pos)
            sv_err_neg = max(abs(se[k] / se[2] - sd_neg[k] / sd_neg[2]) / (se[k] / se[2]) for k in (0, 1))
            sv_split_pos = abs((sd_pos[1] / sd_pos[2]) - (se[1] / se[2])) / (se[1] / se[2])
            if max(rel_neg, sv_err_neg) > max_wlv1_neg_err:
                max_wlv1_neg_err = max(rel_neg, sv_err_neg)
            wlv1_rows.append({
                "point": label,
                "neg_qQ_matrix_prop_rel_err": mp_str(rel_neg, 12),
                "neg_qQ_sv_ratio_rel_err": mp_str(sv_err_neg, 12),
                "unnegated_m2m3_rel_split": mp_str(sv_split_pos, 12),
            })
    out["W_LV1"] = {"rows": wlv1_rows, "max_neg_qQ_rel_err": mp_str(max_wlv1_neg_err, 12)}

    # W2.3b: B1981 E[6]_prim shell L vs G at y=20 -> 30 (dps=110)
    E6p = [(5 * j, 5 * k) for j in range(6) for k in range(6) if gcd_int(gcd_int(j, k), 6) == 1]
    shell_24 = [((12 + dx) % 30, (24 + dy) % 30) for dx, dy in E6p]

    def eval_b1981_at(y_int, dps_use):
        with mp.workdps(dps_use):
            alg_w = build_frame_c_algebra()
            ctx_w = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(y_int)), solve_dps=30)
            L_mat = [mp.zeros(3, 3) for _ in range(3)]
            G_mat = [mp.zeros(3, 3) for _ in range(3)]
            w24 = mp.mpf(1) / 24
            for a_i, b_i in shell_24:
                am, bm = mp.mpf(a_i) / 30, mp.mpf(b_i) / 30
                for si, (qL, qR) in enumerate([(1, -4), (1, 2), (-3, 6)]):
                    Yw = eval_Y_canonical(alg_w, ctx_w, am, bm, qL, qR)
                    L_mat[si] += Yw * w24
                    G_mat[si] += mat_mul_3(Yw, mat_dag(Yw)) * w24
            obs_L = extract_observables(L_mat[0], L_mat[1], L_mat[2])
            ev_u, U_u = mp.eigh(G_mat[0])
            ev_d, U_d = mp.eigh(G_mat[1])
            ev_e, _ = mp.eigh(G_mat[2])
            su_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_u]
            sd_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_d]
            se_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_e]
            Vg = mat_mul_3(mat_dag(U_u), U_d)
            return {
                "L": {
                    "u_m2m3": obs_L["u_m2m3"], "d_m2m3": obs_L["d_m2m3"], "e_m2m3": obs_L["e_m2m3"],
                    "V23": obs_L["absV"][1][2], "min_diag": obs_L["min_diag"],
                },
                "G": {
                    "u_m2m3": su_g[1] / su_g[2], "u_m1m3": su_g[0] / su_g[2],
                    "d_m2m3": sd_g[1] / sd_g[2], "d_m1m3": sd_g[0] / sd_g[2],
                    "e_m2m3": se_g[1] / se_g[2], "e_m1m3": se_g[0] / se_g[2],
                },
            }

    b20 = eval_b1981_at(20, 110)
    b30 = eval_b1981_at(30, 110)
    with mp.workdps(110):
        rates_L = {k: mp_str(-mp.log(b30["L"][k] / b20["L"][k]) / (10 * mp.pi), 10) for k in ("u_m2m3", "d_m2m3", "e_m2m3", "V23")}
        rates_G = {k: mp_str(-mp.log(b30["G"][k] / b20["G"][k]) / (10 * mp.pi), 10) for k in b20["G"]}
    out["B1981_shell"] = {
        "rates_y20_to_y30_L": rates_L,
        "rates_y20_to_y30_G": rates_G,
        "L_y30_V23": mp_str(b30["L"]["V23"], 12),
        "L_y30_min_diag": mp_str(b30["L"]["min_diag"], 12),
    }
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 7. MODULE W3: 2-STAGE POLISHED RIEMANNIAN BB ON S^5 / S^5 x S^5 + MODULAR V(tau)
# ============================================================================

def lin_comb_3(basis, h, conj_h=False):
    h0, h1, h2 = (mp.conj(h[0]), mp.conj(h[1]), mp.conj(h[2])) if conj_h else (h[0], h[1], h[2])
    B0, B1, B2 = basis
    Y = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            Y[i, j] = h0 * B0[i, j] + h1 * B1[i, j] + h2 * B2[i, j]
    return Y


def sector_potential_and_grad(basis, h, N_c, mode, mu2, conj_h=False, sign_flip=1):
    Y = lin_comb_3(basis, h, conj_h=conj_h)
    H = mat_mul_3(mat_dag(Y), Y)
    if mode == "V4":
        H2 = mat_mul_3(H, H)
        val = -sign_flip * N_c * mp.re(mat_tr(H2))
        dPhi = (-2 * sign_flip * N_c) * H
    else:
        ev, U = mp.eigh(H)
        pref = -sign_flip * mp.mpf(N_c) / (64 * mp.pi * mp.pi)
        val = mp.mpf(0)
        dp_eigs = []
        tiny = mp.mpf(10) ** (-40)
        for k in range(3):
            lam = max(mp.mpf(0), mp.re(ev[k]))
            if lam > tiny:
                lnr = mp.log(lam / mu2)
                val += pref * (lam * lam) * (lnr - mp.mpf(3) / 2)
                dp_eigs.append(pref * 2 * lam * (lnr - 1))
            else:
                dp_eigs.append(mp.mpf(0))
        D_U = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                D_U[i, j] = U[i, j] * dp_eigs[j]
        dPhi = mat_mul_3(D_U, mat_dag(U))
    YdP = mat_mul_3(Y, dPhi)
    g = []
    for p in range(3):
        Bp = basis[p]
        tr_v = sum(mp.conj(Bp[i, j]) * YdP[i, j] for i in range(3) for j in range(3))
        g.append(2 * (mp.conj(tr_v) if conj_h else tr_v))
    return val, g


def project_tan_S5(h, g):
    ip = mp.re(sum(mp.conj(h[i]) * g[i] for i in range(3)))
    return [g[i] - ip * h[i] for i in range(3)]


def retract_S5(h, d, step):
    v = [h[i] + step * d[i] for i in range(3)]
    nv = vec_norm(v)
    return [x / nv for x in v]


def deterministic_S5_starts(c_hat, tag, n_starts=8):
    starts = [
        c_hat[:],
        [mp.mpc(1), mp.mpc(0), mp.mpc(0)],
        [mp.mpc(0), mp.mpc(1), mp.mpc(0)],
        [mp.mpc(0), mp.mpc(0), mp.mpc(1)],
    ]
    rng = Sha256Rng(tag)
    while len(starts) < n_starts:
        v = [mp.mpc(rng.next_mpf_signed_gauss_like(), rng.next_mpf_signed_gauss_like()) for _ in range(3)]
        nv = vec_norm(v)
        starts.append([x / nv for x in v])
    return starts


def bb_run_1d(eval_fg, h0, max_iter, gtol):
    h = h0[:]
    v, g = eval_fg(h)
    step = mp.mpf(1) / max(mp.mpf(1), vec_norm(g))
    prev_h = None
    prev_g = None
    for _ in range(max_iter):
        gn = vec_norm(g)
        if gn < gtol:
            break
        if prev_h is not None:
            s_v = [h[i] - prev_h[i] for i in range(3)]
            y_v = [g[i] - prev_g[i] for i in range(3)]
            sy = mp.re(sum(mp.conj(s_v[i]) * y_v[i] for i in range(3)))
            ss = mp.re(sum(mp.conj(s_v[i]) * s_v[i] for i in range(3)))
            if sy > mp.mpf(10) ** (-32):
                step = min(mp.mpf(1000), max(mp.mpf(10) ** (-10), ss / sy))
        d = [-x for x in g]
        slope = -gn * gn
        cur_step = step
        accepted = False
        for _ls in range(28):
            h_try = retract_S5(h, d, cur_step)
            v_try, g_try = eval_fg(h_try)
            if v_try <= v + (mp.mpf(10) ** (-4)) * cur_step * slope:
                prev_h, prev_g = h, g
                h, v, g = h_try, v_try, g_try
                accepted = True
                break
            cur_step /= 2
        if not accepted:
            if prev_h is not None:
                prev_h = None
                step = mp.mpf(1) / max(mp.mpf(1), gn)
                continue
            break
    return h, v, vec_norm(g)


def bb_run_2d(eval_fg, hu0, hd0, max_iter, gtol):
    hu = hu0[:]
    hd = hd0[:]
    v, gu, gd = eval_fg(hu, hd)
    gn = mp.sqrt(vec_norm(gu) ** 2 + vec_norm(gd) ** 2)
    step = mp.mpf(1) / max(mp.mpf(1), gn)
    prev = None
    for _ in range(max_iter):
        gn = mp.sqrt(vec_norm(gu) ** 2 + vec_norm(gd) ** 2)
        if gn < gtol:
            break
        if prev is not None:
            phu, phd, pgu, pgd = prev
            su_v = [hu[i] - phu[i] for i in range(3)]
            sd_v = [hd[i] - phd[i] for i in range(3)]
            yu_v = [gu[i] - pgu[i] for i in range(3)]
            yd_v = [gd[i] - pgd[i] for i in range(3)]
            sy = mp.re(sum(mp.conj(su_v[i]) * yu_v[i] + mp.conj(sd_v[i]) * yd_v[i] for i in range(3)))
            ss = mp.re(sum(mp.conj(su_v[i]) * su_v[i] + mp.conj(sd_v[i]) * sd_v[i] for i in range(3)))
            if sy > mp.mpf(10) ** (-32):
                step = min(mp.mpf(1000), max(mp.mpf(10) ** (-10), ss / sy))
        du = [-x for x in gu]
        dd = [-x for x in gd]
        slope = -gn * gn
        cur_step = step
        accepted = False
        for _ls in range(28):
            hu_t = retract_S5(hu, du, cur_step)
            hd_t = retract_S5(hd, dd, cur_step)
            v_t, gu_t, gd_t = eval_fg(hu_t, hd_t)
            if v_t <= v + (mp.mpf(10) ** (-4)) * cur_step * slope:
                prev = (hu, hd, gu, gd)
                hu, hd, v, gu, gd = hu_t, hd_t, v_t, gu_t, gd_t
                accepted = True
                break
            cur_step /= 2
        if not accepted:
            if prev is not None:
                prev = None
                step = mp.mpf(1) / max(mp.mpf(1), gn)
                continue
            break
    return hu, hd, v, mp.sqrt(vec_norm(gu) ** 2 + vec_norm(gd) ** 2)


def minimize_1doublet_S5(bases_hi, c_hat_hi, mu2_hi, mode, tag, sign_flip=1, n_starts=8):
    """8 quick starts at dps=20 + high-precision polish at dps=28."""
    def make_fg(bases, mu2):
        bu, bd, be = bases

        def eval_fg(h):
            vu, gu = sector_potential_and_grad(bu, h, 3, mode, mu2, conj_h=False, sign_flip=sign_flip)
            vd, gd = sector_potential_and_grad(bd, h, 3, mode, mu2, conj_h=True, sign_flip=sign_flip)
            ve, ge = sector_potential_and_grad(be, h, 1, mode, mu2, conj_h=True, sign_flip=sign_flip)
            return vu + vd + ve, project_tan_S5(h, [gu[i] + gd[i] + ge[i] for i in range(3)])

        return eval_fg

    starts = deterministic_S5_starts(c_hat_hi, tag, n_starts)
    best_v = None
    best_h = None
    all_m2m3_ok = True
    with mp.workdps(20):
        fg_lo = make_fg(bases_hi, mu2_hi)
        for h0 in starts:
            h, v, _ = bb_run_1d(fg_lo, h0, 100, mp.mpf(10) ** (-10))
            r_h = abs(h[0] ** 2 + h[1] ** 2 + h[2] ** 2)
            r_cl = min(mp.mpf(1), r_h)
            t_h = r_cl / (1 + mp.sqrt(max(mp.mpf(0), 1 - r_cl * r_cl)))
            fl = (t_h * t_h) / (1 + 2 * t_h)
            om = extract_observables(lin_comb_3(bases_hi[0], h, False), lin_comb_3(bases_hi[1], h, True), lin_comb_3(bases_hi[2], h, True))
            if max(om["u_m2m3"], om["d_m2m3"]) + mp.mpf(10) ** (-10) < fl:
                all_m2m3_ok = False
            if best_v is None or v < best_v:
                best_v, best_h = v, h
    # Polish best basin at dps=28
    with mp.workdps(28):
        fg_hi = make_fg(bases_hi, mu2_hi)
        nh = vec_norm(best_h)
        best_h = [x / nh for x in best_h]
        best_h, best_v, best_gn = bb_run_1d(fg_hi, best_h, 300, mp.mpf(10) ** (-12))
        r_h = abs(best_h[0] ** 2 + best_h[1] ** 2 + best_h[2] ** 2)
        r_cl = min(mp.mpf(1), r_h)
        t_h = r_cl / (1 + mp.sqrt(max(mp.mpf(0), 1 - r_cl * r_cl)))
        m2m3_floor = (t_h * t_h) / (1 + 2 * t_h)
        obs = extract_observables(
            lin_comb_3(bases_hi[0], best_h, False),
            lin_comb_3(bases_hi[1], best_h, True),
            lin_comb_3(bases_hi[2], best_h, True),
        )
        if max(obs["u_m2m3"], obs["d_m2m3"]) + mp.mpf(10) ** (-12) < m2m3_floor:
            all_m2m3_ok = False
        return {
            "V_min": best_v, "h_star": best_h, "grad_norm": best_gn,
            "r_h": r_h, "c_hat_overlap": abs(vec_dot(c_hat_hi, best_h)),
            "m2m3_floor": m2m3_floor, "m2m3_all_starts_compliant": all_m2m3_ok, "obs": obs,
        }


def minimize_2doublet_S5xS5(bases_hi, c_hat_hi, mu2_hi, mode, lam3_val, V0, tag, n_starts=8):
    """8 quick starts at dps=20 + high-precision polish at dps=28 (up to 400 iters)."""
    lam3_V0 = lam3_val * V0

    def make_fg(bases, mu2):
        bu, bd, be = bases

        def eval_fg(hu, hd):
            vu, gu = sector_potential_and_grad(bu, hu, 3, mode, mu2, conj_h=False)
            vd, gd1 = sector_potential_and_grad(bd, hd, 3, mode, mu2, conj_h=False)
            ve, gd2 = sector_potential_and_grad(be, hd, 1, mode, mu2, conj_h=False)
            ov = vec_dot(hu, hd)
            pen = lam3_V0 * (mp.re(ov) * mp.re(ov) + mp.im(ov) * mp.im(ov))
            c_ov = mp.conj(ov)
            gu_tot = [gu[i] + 2 * lam3_V0 * c_ov * hd[i] for i in range(3)]
            gd_tot = [gd1[i] + gd2[i] + 2 * lam3_V0 * ov * hu[i] for i in range(3)]
            return vu + vd + ve + pen, project_tan_S5(hu, gu_tot), project_tan_S5(hd, gd_tot)

        return eval_fg

    s_u = deterministic_S5_starts(c_hat_hi, tag + "_u", n_starts)
    s_d = deterministic_S5_starts(c_hat_hi, tag + "_d", n_starts)
    e_orth = [mp.conj(c_hat_hi[1]), -mp.conj(c_hat_hi[0]), mp.mpc(0)]
    ne = vec_norm(e_orth)
    if ne > mp.mpf(10) ** (-10):
        s_u[1] = c_hat_hi[:]
        s_d[1] = [x / ne for x in e_orth]

    best_v = None
    best_hu = None
    best_hd = None
    with mp.workdps(20):
        fg_lo = make_fg(bases_hi, mu2_hi)
        for idx in range(n_starts):
            hu, hd, v, _ = bb_run_2d(fg_lo, s_u[idx], s_d[idx], 100, mp.mpf(10) ** (-10))
            if best_v is None or v < best_v:
                best_v, best_hu, best_hd = v, hu, hd
    with mp.workdps(28):
        fg_hi = make_fg(bases_hi, mu2_hi)
        nhu = vec_norm(best_hu)
        nhd = vec_norm(best_hd)
        best_hu = [x / nhu for x in best_hu]
        best_hd = [x / nhd for x in best_hd]
        best_hu, best_hd, best_v, best_gn = bb_run_2d(fg_hi, best_hu, best_hd, 400, mp.mpf(10) ** (-11))
        obs = extract_observables(
            lin_comb_3(bases_hi[0], best_hu, False),
            lin_comb_3(bases_hi[1], best_hd, False),
            lin_comb_3(bases_hi[2], best_hd, False),
        )
        return {
            "V_min": best_v, "hu_star": best_hu, "hd_star": best_hd, "grad_norm": best_gn,
            "hu_hd_overlap": abs(vec_dot(best_hu, best_hd)),
            "r_u": abs(best_hu[0] ** 2 + best_hu[1] ** 2 + best_hu[2] ** 2),
            "r_d": abs(best_hd[0] ** 2 + best_hd[1] ** 2 + best_hd[2] ** 2),
            "hu_chat_overlap": abs(vec_dot(c_hat_hi, best_hu)),
            "hd_chat_overlap": abs(vec_dot(c_hat_hi, best_hd)),
            "obs": obs,
        }


def eval_point_potentials(alg, ctx, a, b):
    Ys = [
        eval_Y_canonical(alg, ctx, a, b, 1, -4),
        eval_Y_canonical(alg, ctx, a, b, 1, 2),
        eval_Y_canonical(alg, ctx, a, b, -3, 6),
    ]
    Ncs = [3, 3, 1]
    Hs = [mat_mul_3(mat_dag(Y), Y) for Y in Ys]
    mu2 = (mp.re(mat_tr(Hs[0])) + mp.re(mat_tr(Hs[1])) + mp.re(mat_tr(Hs[2]))) / 3
    v4 = mp.mpf(0)
    vcw = mp.mpf(0)
    tiny = mp.mpf(10) ** (-45)
    inv64pi2 = mp.mpf(1) / (64 * mp.pi * mp.pi)
    for si in range(3):
        ev, _ = mp.eigh(Hs[si])
        nc = mp.mpf(Ncs[si])
        for k in range(3):
            lam = max(mp.mpf(0), mp.re(ev[k]))
            v4 -= nc * lam * lam
            if lam > tiny:
                vcw -= nc * inv64pi2 * lam * lam * (mp.log(lam / mu2) - mp.mpf(3) / 2)
    return v4, vcw, mu2


def run_W3():
    t0 = time.monotonic_ns()
    out = {}
    _, prim_pairs = generate_E30_prim()

    opt_results = {}
    saved_vacua = {}
    all_1d_m2m3_ok = True
    max_opt_gnorm = mp.mpf(0)
    lam3_grid = [Fraction(-1, 1), Fraction(-1, 4), Fraction(0, 1), Fraction(1, 4), Fraction(1, 1)]

    with mp.workdps(28):
        alg28 = build_frame_c_algebra()
        tau_specs = [
            ("tau_apex", mp.mpc(mp.mpf(1) / 2, mp.sqrt(5) / 2)),
            ("tau_2", mp.mpc(mp.mpf(13) / 100, mp.mpf(2))),
        ]
        pt_specs = [("mark_8_1", (8, 1)), ("twin_1_5", (1, 5))]
        for tname, tau_v in tau_specs:
            ctx = make_tau_ctx(tau_v, solve_dps=30)
            c_hat = ctx["c_hat"]
            for pname, (a_i, b_i) in pt_specs:
                am, bm = mp.mpf(a_i) / 30, mp.mpf(b_i) / 30
                bases = [
                    assemble_Y_basis(alg28, ctx, am, bm, 1, -4),
                    assemble_Y_basis(alg28, ctx, am, bm, 1, 2),
                    assemble_Y_basis(alg28, ctx, am, bm, -3, 6),
                ]
                v4_c, vcw_c, mu2 = eval_point_potentials(alg28, ctx, am, bm)
                key = f"{tname}__{pname}"
                entry = {
                    "canonical_mu2": mp_str(mu2, 16),
                    "canonical_V4": mp_str(v4_c, 16),
                    "canonical_VCW": mp_str(vcw_c, 16),
                    "one_doublet_conjugated": {},
                    "two_doublet_allS": {},
                }
                for mode, V0_val in [("VCW", abs(vcw_c)), ("V4", abs(v4_c))]:
                    r1 = minimize_1doublet_S5(bases, c_hat, mu2, mode, f"1d_{key}_{mode}", n_starts=8)
                    if not r1["m2m3_all_starts_compliant"]:
                        all_1d_m2m3_ok = False
                    if r1["grad_norm"] > max_opt_gnorm:
                        max_opt_gnorm = r1["grad_norm"]
                    entry["one_doublet_conjugated"][mode] = {
                        "V_min": mp_str(r1["V_min"], 16),
                        "grad_norm": mp_str(r1["grad_norm"], 8),
                        "r_h": mp_str(r1["r_h"], 14),
                        "c_hat_overlap": mp_str(r1["c_hat_overlap"], 14),
                        "m2m3_floor": mp_str(r1["m2m3_floor"], 14),
                        "m2m3_all_starts_compliant": r1["m2m3_all_starts_compliant"],
                        "u_m2m3": mp_str(r1["obs"]["u_m2m3"], 14),
                        "d_m2m3": mp_str(r1["obs"]["d_m2m3"], 14),
                        "e_m2m3": mp_str(r1["obs"]["e_m2m3"], 14),
                        "V12": mp_str(r1["obs"]["absV"][0][1], 14),
                        "V23": mp_str(r1["obs"]["absV"][1][2], 14),
                        "V13": mp_str(r1["obs"]["absV"][0][2], 14),
                        "J_CP": mp_str(r1["obs"]["J_CP"], 14),
                    }
                    t2_map = {}
                    for l3_f in lam3_grid:
                        l3_m = mp.mpf(l3_f.numerator) / l3_f.denominator
                        r2 = minimize_2doublet_S5xS5(
                            bases, c_hat, mu2, mode, l3_m, V0_val, f"2d_{key}_{mode}_{frac_str(l3_f)}", n_starts=8,
                        )
                        if r2["grad_norm"] > max_opt_gnorm:
                            max_opt_gnorm = r2["grad_norm"]
                        obs2 = r2["obs"]
                        std_ord = bool((obs2["absV"][0][1] > obs2["absV"][1][2]) and (obs2["absV"][1][2] > obs2["absV"][0][2]))
                        t2_map[frac_str(l3_f)] = {
                            "V_min": mp_str(r2["V_min"], 16),
                            "grad_norm": mp_str(r2["grad_norm"], 8),
                            "hu_hd_overlap": mp_str(r2["hu_hd_overlap"], 14),
                            "r_u": mp_str(r2["r_u"], 14), "r_d": mp_str(r2["r_d"], 14),
                            "hu_chat_overlap": mp_str(r2["hu_chat_overlap"], 14),
                            "hd_chat_overlap": mp_str(r2["hd_chat_overlap"], 14),
                            "u_m2m3": mp_str(obs2["u_m2m3"], 14),
                            "d_m2m3": mp_str(obs2["d_m2m3"], 14),
                            "e_m2m3": mp_str(obs2["e_m2m3"], 14),
                            "V12": mp_str(obs2["absV"][0][1], 14),
                            "V23": mp_str(obs2["absV"][1][2], 14),
                            "V13": mp_str(obs2["absV"][0][2], 14),
                            "J_CP": mp_str(obs2["J_CP"], 14),
                            "std_ckm_ordering": std_ord,
                        }
                        if tname == "tau_2" and pname == "mark_8_1" and mode == "VCW" and l3_f == Fraction(0):
                            saved_vacua["U_B"] = (r2["hu_star"], r2["hd_star"])
                        if tname == "tau_2" and pname == "mark_8_1" and mode == "V4" and l3_f == Fraction(-1, 4):
                            saved_vacua["U_D"] = (r2["hu_star"], r2["hd_star"])
                    entry["two_doublet_allS"][mode] = t2_map
                opt_results[key] = entry

    out["higgs_direction_optimization"] = {
        "results": opt_results,
        "all_1doublet_minima_M2M3_compliant": all_1d_m2m3_ok,
        "max_grad_norm": mp_str(max_opt_gnorm, 8),
    }

    # Exact symbolic cusp norm exponent theorem
    ens = [classify_point_tropical(a_i, b_i, 30)["e_norm"] for a_i, b_i in prim_pairs]
    out["cusp_norm_exponent_theorem"] = {
        "total_pairs": len(prim_pairs),
        "count_e_norm_negative": sum(1 for x in ens if x < 0),
        "min_e_norm": frac_str(min(ens)),
        "max_e_norm": frac_str(max(ens)),
        "proves_fermion_loop_cusp_runaway": bool(min(ens) < 0 and all(x < 0 for x in ens)),
    }

    # Exact SL(2, Z) invariance of V_CW^(all-288) and V_4^(all-288)
    with mp.workdps(38):
        alg38 = build_frame_c_algebra()
        tau_ref = mp.mpc(mp.mpf(1) / 4, mp.mpf(6) / 5)
        L2_ref = get_L2(tau_ref, solve_dps=32)

        def sum_all_288(tau_w, L2_w):
            ctx_w = make_tau_ctx(tau_w, L2_val=L2_w)
            sv4 = mp.mpf(0)
            svcw = mp.mpf(0)
            for a_i, b_i in prim_pairs:
                v4, vcw, _ = eval_point_potentials(alg38, ctx_w, mp.mpf(a_i) / 30, mp.mpf(b_i) / 30)
                sv4 += v4
                svcw += vcw
            return sv4, svcw

        v4_0, vcw_0 = sum_all_288(tau_ref, L2_ref)
        v4_T, vcw_T = sum_all_288(tau_ref + 1, L2_ref)
        v4_S, vcw_S = sum_all_288(-1 / tau_ref, L2_ref + mp.log(abs(tau_ref)))
        err_v4_T = abs(v4_T - v4_0) / abs(v4_0)
        err_vcw_T = abs(vcw_T - vcw_0) / abs(vcw_0)
        err_v4_S = abs(v4_S - v4_0) / abs(v4_0)
        err_vcw_S = abs(vcw_S - vcw_0) / abs(vcw_0)
        max_mod_inv_err = max(err_v4_T, err_vcw_T, err_v4_S, err_vcw_S)

    out["modular_all288_invariance"] = {
        "tau": "1/4 + 6/5 i",
        "V4_all288": mp_str(v4_0, 18), "VCW_all288": mp_str(vcw_0, 18),
        "rel_err_T_V4": mp_str(err_v4_T, 10), "rel_err_T_VCW": mp_str(err_vcw_T, 10),
        "rel_err_S_V4": mp_str(err_v4_S, 10), "rel_err_S_VCW": mp_str(err_vcw_S, 10),
        "max_rel_err": mp_str(max_mod_inv_err, 10),
    }

    # y-scan across x=0 and x=1/2 (fast with cwt_cache!)
    y_grid = [
        Fraction(1, 1), Fraction(5, 4), Fraction(3, 2), Fraction(2, 1), Fraction(5, 2),
        Fraction(3, 1), Fraction(4, 1), Fraction(5, 1), Fraction(6, 1), Fraction(8, 1),
    ]
    y_scan = {}
    with mp.workdps(24):
        alg24 = build_frame_c_algebra()
        for x_label, x_f in [("x_0", Fraction(0, 1)), ("x_half", Fraction(1, 2))]:
            rows = []
            xm = mp.mpf(x_f.numerator) / x_f.denominator
            for y_f in y_grid:
                ym = mp.mpf(y_f.numerator) / y_f.denominator
                ctx_w = make_tau_ctx(mp.mpc(xm, ym), solve_dps=26)
                sv4 = mp.mpf(0)
                svcw = mp.mpf(0)
                mv4 = tv4 = None
                for a_i, b_i in prim_pairs:
                    v4, vcw, _ = eval_point_potentials(alg24, ctx_w, mp.mpf(a_i) / 30, mp.mpf(b_i) / 30)
                    sv4 += v4
                    svcw += vcw
                    if (a_i, b_i) == (8, 1):
                        mv4 = v4
                    elif (a_i, b_i) == (1, 5):
                        tv4 = v4
                rows.append({
                    "y": frac_str(y_f), "L2": mp_str(ctx_w["L2"], 12),
                    "V4_all288": mp_str(sv4, 12), "VCW_all288": mp_str(svcw, 12),
                    "V4_mark": mp_str(mv4, 12), "V4_twin": mp_str(tv4, 12),
                })
            y_scan[x_label] = rows
    out["modular_y_scan"] = y_scan
    out["runtime_s"] = elapsed_sec_str(t0)
    return out, saved_vacua


# ============================================================================
# 8. MODULE W4: REFINED CURVED G_{s=1/2}, GL4 2-LOOP 2HDM-II RG, COVARIANT Y_nu Y_nu^T
# ============================================================================

def sympy_verify_chowdhury_eberhardt_gut():
    """
    Independent SymPy symbolic derivation & verification of 15/15 Chowdhury-Eberhardt
    (1503.08216) Type-II 2HDM 1x1 coefficients in GUT g1 normalization (g'^2 = (3/5) g1^2),
    including exact Machacek-Vaughn NPB 236 (1984) 221 Eq. (3.4) -29/240 and -65/240,
    plus exact 1HDM (-12, -11/4, -1/4) check.
    """
    yt, yb, ytau, g1, g2, g3, l1, l2, l3, l4 = sp.symbols("yt yb ytau g1 g2 g3 l1 l2 l3 l4")
    gp2 = sp.Rational(3, 5) * g1 ** 2
    Hu, Hd, He = yt ** 2, yb ** 2, ytau ** 2
    Tu, Td = 3 * Hu, 3 * Hd + He
    byu_2 = sp.expand(
        sp.Rational(3, 2) * Hu ** 2 - sp.Rational(1, 4) * Hu * Hd - sp.Rational(1, 4) * Hd ** 2
        - sp.Rational(9, 4) * Tu * Hu - sp.Rational(3, 4) * Td * Hd
        - sp.Rational(27, 4) * Hu ** 2 - sp.Rational(9, 4) * Hu * Hd
        - 6 * l2 * Hu + (-2 * l3 + 2 * l4) * Hd
        + (sp.Rational(3, 2) * l2 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2)
        + (sp.Rational(223, 48) * gp2 + sp.Rational(135, 16) * g2 ** 2 + 16 * g3 ** 2) * Hu
        + (sp.Rational(85, 24) * gp2 + sp.Rational(45, 8) * g2 ** 2 + 20 * g3 ** 2) * Hu
        + (-sp.Rational(29, 144) * gp2 + sp.Rational(33, 16) * g2 ** 2 + sp.Rational(16, 3) * g3 ** 2) * Hd
        + (sp.Rational(1267, 216) * gp2 ** 2 - sp.Rational(21, 4) * g2 ** 4 - 108 * g3 ** 4
           - sp.Rational(3, 4) * gp2 * g2 ** 2 + sp.Rational(19, 9) * gp2 * g3 ** 2 + 9 * g2 ** 2 * g3 ** 2)
    )
    byd_2 = sp.expand(
        sp.Rational(3, 2) * Hd ** 2 - sp.Rational(1, 4) * Hd * Hu - sp.Rational(1, 4) * Hu ** 2
        - sp.Rational(9, 4) * Td * Hd - sp.Rational(3, 4) * Tu * Hu
        - sp.Rational(27, 4) * Hd ** 2 - sp.Rational(9, 4) * He ** 2 - sp.Rational(9, 4) * Hu * Hd
        - 6 * l1 * Hd + (-2 * l3 + 2 * l4) * Hu
        + (sp.Rational(3, 2) * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2)
        + (sp.Rational(187, 48) * gp2 + sp.Rational(135, 16) * g2 ** 2 + 16 * g3 ** 2) * Hd
        + (sp.Rational(25, 24) * gp2 + sp.Rational(45, 8) * g2 ** 2 + 20 * g3 ** 2) * Hd
        + (sp.Rational(25, 8) * gp2 + sp.Rational(15, 8) * g2 ** 2) * He
        + (-sp.Rational(65, 144) * gp2 + sp.Rational(33, 16) * g2 ** 2 + sp.Rational(16, 3) * g3 ** 2) * Hu
        + (-sp.Rational(113, 216) * gp2 ** 2 - sp.Rational(21, 4) * g2 ** 4 - 108 * g3 ** 4
           - sp.Rational(9, 4) * gp2 * g2 ** 2 + sp.Rational(31, 9) * gp2 * g3 ** 2 + 9 * g2 ** 2 * g3 ** 2)
    )
    bye_2 = sp.expand(
        sp.Rational(3, 2) * He ** 2 - sp.Rational(9, 4) * Td * He
        - sp.Rational(27, 4) * Hd ** 2 - sp.Rational(9, 4) * He ** 2 - sp.Rational(9, 4) * Hu * Hd
        - 6 * l1 * He
        + (sp.Rational(3, 2) * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2)
        + (sp.Rational(129, 16) * gp2 + sp.Rational(135, 16) * g2 ** 2) * He
        + (sp.Rational(25, 24) * gp2 + sp.Rational(45, 8) * g2 ** 2 + 20 * g3 ** 2) * Hd
        + (sp.Rational(25, 8) * gp2 + sp.Rational(15, 8) * g2 ** 2) * He
        + (sp.Rational(161, 8) * gp2 ** 2 - sp.Rational(21, 4) * g2 ** 4 + sp.Rational(9, 4) * gp2 * g2 ** 2)
    )
    checks_15 = [
        ("yt_yt4", byu_2.coeff(yt, 4), sp.Rational(-12)),
        ("yt_yt2yb2", byu_2.coeff(yt, 2).coeff(yb, 2), sp.Rational(-5, 2)),
        ("yt_yb4", byu_2.coeff(yb, 4), sp.Rational(-5, 2)),
        ("yt_yb2ytau2", byu_2.coeff(yb, 2).coeff(ytau, 2), sp.Rational(-3, 4)),
        ("yt_g1sq_yt2", byu_2.coeff(g1, 2).coeff(yt, 2), sp.Rational(393, 80)),
        ("yt_g1sq_yb2_MV84", byu_2.coeff(g1, 2).coeff(yb, 2), sp.Rational(-29, 240)),
        ("yt_g1_4", byu_2.coeff(g1, 4), sp.Rational(1267, 600)),
        ("yb_yb4", byd_2.coeff(yb, 4), sp.Rational(-12)),
        ("yb_yt2yb2", byd_2.coeff(yt, 2).coeff(yb, 2), sp.Rational(-5, 2)),
        ("yb_yt4", byd_2.coeff(yt, 4), sp.Rational(-5, 2)),
        ("yb_yb2ytau2", byd_2.coeff(yb, 2).coeff(ytau, 2), sp.Rational(-9, 4)),
        ("yb_ytau4", byd_2.coeff(ytau, 4), sp.Rational(-9, 4)),
        ("yb_g1sq_yt2_MV84", byd_2.coeff(g1, 2).coeff(yt, 2), sp.Rational(-65, 240)),
        ("ytau_ytau4", bye_2.coeff(ytau, 4), sp.Rational(-3)),
        ("ytau_yb4", bye_2.coeff(yb, 4), sp.Rational(-27, 4)),
    ]
    byu_1h = sp.expand(
        sp.Rational(3, 2) * Hu ** 2 - sp.Rational(5, 4) * Hu * Hd + sp.Rational(11, 4) * Hd ** 2
        - sp.Rational(9, 4) * (Tu + Td) * Hu + sp.Rational(5, 4) * (Tu + Td) * Hd
        - sp.Rational(27, 4) * (Hu ** 2 + Hd ** 2) + sp.Rational(3, 2) * Hu * Hd - sp.Rational(9, 4) * He ** 2
    )
    sm_1h = (byu_1h.coeff(yt, 4), byu_1h.coeff(yt, 2).coeff(yb, 2), byu_1h.coeff(yb, 4))
    return {
        "ce15_all_exact": all(sp.simplify(g - e) == 0 for _, g, e in checks_15),
        "sm_1hdm_triple": [str(x) for x in sm_1h],
        "sm_1hdm_exact": (sm_1h == (sp.Rational(-12), sp.Rational(-11, 4), sp.Rational(-1, 4))),
    }


def rge_rhs_gut(state, model="2HDM_II", quartic_2loop=False, drop_Yu=False):
    """
    Exact Scope Card Section 4 Type-II 2HDM RGEs in GUT g1 normalization (g'^2 = (3/5) g1^2):
      - 2-loop gauge (b1 = 21/5, b2 = -3, b3 = -7)
      - 2-loop non-commuting 3x3 Yukawas with exact MV84 -29/240, -65/240
      - 1-loop quartics (primary, lambda_5 = 0) OR full exact N_H=2 2-loop quartics (when quartic_2loop=True)
    """
    g1, g2, g3, l1, l2, l3, l4, Yu, Yd, Ye = state
    if drop_Yu:
        Yu = mp.zeros(3, 3)
    k1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    k2 = k1 * k1
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    gp2 = (mp.mpf(3) / 5) * g1s  # SM g'^2 = (3/5) g1_GUT^2
    gp4, g24, g34 = gp2 * gp2, g2s * g2s, g3s * g3s

    Hu = mat_mul_3(Yu, mat_dag(Yu))
    Hd = mat_mul_3(Yd, mat_dag(Yd))
    He = mat_mul_3(Ye, mat_dag(Ye))
    Hu2 = mat_mul_3(Hu, Hu)
    Hd2 = mat_mul_3(Hd, Hd)
    He2 = mat_mul_3(He, He)
    HuHd = mat_mul_3(Hu, Hd)
    HdHu = mat_mul_3(Hd, Hu)

    tr_u = mp.re(mat_tr(Hu))
    tr_d = mp.re(mat_tr(Hd))
    tr_e = mp.re(mat_tr(He))
    tr_u2 = mp.re(mat_tr(Hu2))
    tr_d2 = mp.re(mat_tr(Hd2))
    tr_e2 = mp.re(mat_tr(He2))
    tr_ud = mp.re(mat_tr(HuHd))

    Tu = 3 * tr_u
    Td = 3 * tr_d + tr_e
    I3 = mp.eye(3)

    if model == "1HDM":
        dg1 = k1 * (mp.mpf(41) / 10) * g1 ** 3 + k2 * g1 ** 3 * (
            (mp.mpf(199) / 50) * g1s + (mp.mpf(27) / 10) * g2s + (mp.mpf(44) / 5) * g3s
            - (mp.mpf(17) / 10) * tr_u - (mp.mpf(1) / 2) * tr_d - (mp.mpf(3) / 2) * tr_e
        )
        dg2 = k1 * (mp.mpf(-19) / 6) * g2 ** 3 + k2 * g2 ** 3 * (
            (mp.mpf(9) / 10) * g1s + (mp.mpf(35) / 6) * g2s + 12 * g3s
            - (mp.mpf(3) / 2) * tr_u - (mp.mpf(3) / 2) * tr_d - (mp.mpf(1) / 2) * tr_e
        )
        dg3 = k1 * (-7) * g3 ** 3 + k2 * g3 ** 3 * (
            (mp.mpf(11) / 10) * g1s + (mp.mpf(9) / 2) * g2s - 26 * g3s - 2 * tr_u - 2 * tr_d
        )
        T_all = Tu + Td
        Au1 = (mp.mpf(3) / 2) * Hu - (mp.mpf(3) / 2) * Hd + (T_all - (mp.mpf(17) / 12) * gp2 - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
        Ad1 = (mp.mpf(3) / 2) * Hd - (mp.mpf(3) / 2) * Hu + (T_all - (mp.mpf(5) / 12) * gp2 - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
        Ae1 = (mp.mpf(3) / 2) * He + (T_all - (mp.mpf(15) / 4) * gp2 - (mp.mpf(9) / 4) * g2s) * I3
        Y4_tr = (mp.mpf(27) / 4) * (tr_u2 + tr_d2) + (mp.mpf(9) / 4) * tr_e2 - (mp.mpf(3) / 2) * tr_ud
        g2_tr = ((mp.mpf(85) / 24) * gp2 + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_u \
            + ((mp.mpf(25) / 24) * gp2 + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_d \
            + ((mp.mpf(25) / 8) * gp2 + (mp.mpf(15) / 8) * g2s) * tr_e
        Au2 = (
            (mp.mpf(3) / 2) * Hu2 - (mp.mpf(1) / 4) * HuHd - HdHu + (mp.mpf(11) / 4) * Hd2
            - (mp.mpf(9) / 4) * T_all * Hu + (mp.mpf(5) / 4) * T_all * Hd - 6 * l1 * Hu
            + ((mp.mpf(223) / 48) * gp2 + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hu
            + (-(mp.mpf(43) / 48) * gp2 + (mp.mpf(9) / 16) * g2s - 16 * g3s) * Hd
            + (mp.mpf(3) / 2 * l1 * l1 - Y4_tr + g2_tr
               + (mp.mpf(1187) / 216) * gp4 - (mp.mpf(23) / 4) * g24 - 108 * g34
               - (mp.mpf(3) / 4) * gp2 * g2s + (mp.mpf(19) / 9) * gp2 * g3s + 9 * g2s * g3s) * I3
        )
        Ad2 = (
            (mp.mpf(3) / 2) * Hd2 - (mp.mpf(1) / 4) * HdHu - HuHd + (mp.mpf(11) / 4) * Hu2
            - (mp.mpf(9) / 4) * T_all * Hd + (mp.mpf(5) / 4) * T_all * Hu - 6 * l1 * Hd
            + ((mp.mpf(187) / 48) * gp2 + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hd
            + (-(mp.mpf(79) / 48) * gp2 + (mp.mpf(9) / 16) * g2s - 16 * g3s) * Hu
            + (mp.mpf(3) / 2 * l1 * l1 - Y4_tr + g2_tr
               - (mp.mpf(127) / 216) * gp4 - (mp.mpf(23) / 4) * g24 - 108 * g34
               - (mp.mpf(9) / 4) * gp2 * g2s + (mp.mpf(31) / 9) * gp2 * g3s + 9 * g2s * g3s) * I3
        )
        Ae2 = (
            (mp.mpf(3) / 2) * He2 - (mp.mpf(9) / 4) * T_all * He - 6 * l1 * He
            + ((mp.mpf(129) / 16) * gp2 + (mp.mpf(135) / 16) * g2s) * He
            + (mp.mpf(3) / 2 * l1 * l1 - Y4_tr + g2_tr
               + (mp.mpf(1371) / 72) * gp4 - (mp.mpf(23) / 4) * g24 + (mp.mpf(9) / 4) * gp2 * g2s) * I3
        )
        dl1 = k1 * (12 * l1 * l1 - (3 * gp2 + 9 * g2s) * l1 + mp.mpf(3) / 4 * (gp4 + 2 * gp2 * g2s + 3 * g24) + 4 * T_all * l1 - 12 * (tr_u2 + tr_d2) - 4 * tr_e2)
        return (dg1, dg2, dg3, dl1, mp.mpf(0), mp.mpf(0), mp.mpf(0), mat_mul_3(k1 * Au1 + k2 * Au2, Yu), mat_mul_3(k1 * Ad1 + k2 * Ad2, Yd), mat_mul_3(k1 * Ae1 + k2 * Ae2, Ye))

    # Exact 2-loop Type-II 2HDM (GUT g1)
    dg1 = k1 * (mp.mpf(21) / 5) * g1 ** 3 + k2 * g1 ** 3 * (
        (mp.mpf(104) / 25) * g1s + (mp.mpf(18) / 5) * g2s + (mp.mpf(44) / 5) * g3s
        - (mp.mpf(17) / 10) * tr_u - (mp.mpf(1) / 2) * tr_d - (mp.mpf(3) / 2) * tr_e
    )
    dg2 = k1 * (-3) * g2 ** 3 + k2 * g2 ** 3 * (
        (mp.mpf(6) / 5) * g1s + 8 * g2s + 12 * g3s
        - (mp.mpf(3) / 2) * tr_u - (mp.mpf(3) / 2) * tr_d - (mp.mpf(1) / 2) * tr_e
    )
    dg3 = k1 * (-7) * g3 ** 3 + k2 * g3 ** 3 * (
        (mp.mpf(11) / 10) * g1s + (mp.mpf(9) / 2) * g2s - 26 * g3s - 2 * tr_u - 2 * tr_d
    )

    Au1 = (mp.mpf(3) / 2) * Hu + (mp.mpf(1) / 2) * Hd + (Tu - (mp.mpf(17) / 12) * gp2 - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
    Ad1 = (mp.mpf(3) / 2) * Hd + (mp.mpf(1) / 2) * Hu + (Td - (mp.mpf(5) / 12) * gp2 - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
    Ae1 = (mp.mpf(3) / 2) * He + (Td - (mp.mpf(15) / 4) * gp2 - (mp.mpf(9) / 4) * g2s) * I3

    g2_Tu = ((mp.mpf(85) / 24) * gp2 + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_u
    g2_Td = ((mp.mpf(25) / 24) * gp2 + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_d + ((mp.mpf(25) / 8) * gp2 + (mp.mpf(15) / 8) * g2s) * tr_e
    l34_sq = l3 * l3 + l3 * l4 + l4 * l4

    Au2 = (
        (mp.mpf(3) / 2) * Hu2 - (mp.mpf(1) / 4) * HuHd - (mp.mpf(1) / 4) * Hd2
        - (mp.mpf(9) / 4) * Tu * Hu - (mp.mpf(3) / 4) * Td * Hd
        - 6 * l2 * Hu + (-2 * l3 + 2 * l4) * Hd
        + ((mp.mpf(223) / 48) * gp2 + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hu
        + (-(mp.mpf(29) / 144) * gp2 + (mp.mpf(33) / 16) * g2s + (mp.mpf(16) / 3) * g3s) * Hd
        + (-(mp.mpf(27) / 4) * tr_u2 - (mp.mpf(9) / 4) * tr_ud + (mp.mpf(3) / 2) * l2 * l2 + l34_sq + g2_Tu
           + (mp.mpf(1267) / 216) * gp4 - (mp.mpf(21) / 4) * g24 - 108 * g34
           - (mp.mpf(3) / 4) * gp2 * g2s + (mp.mpf(19) / 9) * gp2 * g3s + 9 * g2s * g3s) * I3
    )
    Ad2 = (
        (mp.mpf(3) / 2) * Hd2 - (mp.mpf(1) / 4) * HdHu - (mp.mpf(1) / 4) * Hu2
        - (mp.mpf(9) / 4) * Td * Hd - (mp.mpf(3) / 4) * Tu * Hu
        - 6 * l1 * Hd + (-2 * l3 + 2 * l4) * Hu
        + ((mp.mpf(187) / 48) * gp2 + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hd
        + (-(mp.mpf(65) / 144) * gp2 + (mp.mpf(33) / 16) * g2s + (mp.mpf(16) / 3) * g3s) * Hu
        + (-(mp.mpf(27) / 4) * tr_d2 - (mp.mpf(9) / 4) * tr_e2 - (mp.mpf(9) / 4) * tr_ud
           + (mp.mpf(3) / 2) * l1 * l1 + l34_sq + g2_Td
           - (mp.mpf(113) / 216) * gp4 - (mp.mpf(21) / 4) * g24 - 108 * g34
           - (mp.mpf(9) / 4) * gp2 * g2s + (mp.mpf(31) / 9) * gp2 * g3s + 9 * g2s * g3s) * I3
    )
    Ae2 = (
        (mp.mpf(3) / 2) * He2 - (mp.mpf(9) / 4) * Td * He - 6 * l1 * He
        + ((mp.mpf(129) / 16) * gp2 + (mp.mpf(135) / 16) * g2s) * He
        + (-(mp.mpf(27) / 4) * tr_d2 - (mp.mpf(9) / 4) * tr_e2 - (mp.mpf(9) / 4) * tr_ud
           + (mp.mpf(3) / 2) * l1 * l1 + l34_sq + g2_Td
           + (mp.mpf(161) / 8) * gp4 - (mp.mpf(21) / 4) * g24 + (mp.mpf(9) / 4) * gp2 * g2s) * I3
    )

    dYu = mat_mul_3(k1 * Au1 + k2 * Au2, Yu)
    dYd = mat_mul_3(k1 * Ad1 + k2 * Ad2, Yd)
    dYe = mat_mul_3(k1 * Ae1 + k2 * Ae2, Ye)

    b1_l1 = (12 * l1 * l1 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4 - (3 * gp2 + 9 * g2s) * l1
             + mp.mpf(3) / 4 * (gp4 + 2 * gp2 * g2s + 3 * g24) + 4 * Td * l1 - 12 * tr_d2 - 4 * tr_e2)
    b1_l2 = (12 * l2 * l2 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4 - (3 * gp2 + 9 * g2s) * l2
             + mp.mpf(3) / 4 * (gp4 + 2 * gp2 * g2s + 3 * g24) + 4 * Tu * l2 - 12 * tr_u2)
    b1_l3 = ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3 * l3 + 2 * l4 * l4 - (3 * gp2 + 9 * g2s) * l3
             + mp.mpf(3) / 4 * (gp4 - 2 * gp2 * g2s + 3 * g24) + 2 * (Tu + Td) * l3 - 12 * tr_ud)
    b1_l4 = (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4 * l4 - (3 * gp2 + 9 * g2s) * l4
             + 3 * gp2 * g2s + 2 * (Tu + Td) * l4 + 12 * tr_ud)

    if not quartic_2loop:
        return (dg1, dg2, dg3, k1 * b1_l1, k1 * b1_l2, k1 * b1_l3, k1 * b1_l4, dYu, dYd, dYe)

    tr_u3 = mp.re(mat_tr(mat_mul_3(Hu2, Hu)))
    tr_d3 = mp.re(mat_tr(mat_mul_3(Hd2, Hd)))
    tr_e3 = mp.re(mat_tr(mat_mul_3(He2, He)))
    tr_u2d = mp.re(mat_tr(mat_mul_3(Hu2, Hd)))
    tr_d2u = mp.re(mat_tr(mat_mul_3(Hd2, Hu)))
    g6_1 = -(mp.mpf(131) / 8) * gp4 * gp2 - (mp.mpf(191) / 8) * gp4 * g2s - (mp.mpf(101) / 8) * gp2 * g24 + (mp.mpf(291) / 8) * g24 * g2s
    g6_3 = -(mp.mpf(131) / 8) * gp4 * gp2 + (mp.mpf(101) / 8) * gp4 * g2s + (mp.mpf(11) / 8) * gp2 * g24 + (mp.mpf(291) / 8) * g24 * g2s
    g6_4 = -(mp.mpf(73) / 2) * gp4 * g2s - 14 * gp2 * g24
    g4Y2_u = -((mp.mpf(19) / 2) * gp4 - 21 * gp2 * g2s + (mp.mpf(9) / 2) * g24) * tr_u
    g4Y2_d = -((mp.mpf(5) / 2) * gp4 + 9 * gp2 * g2s + (mp.mpf(9) / 2) * g24) * tr_d \
        - ((mp.mpf(25) / 2) * gp4 - 11 * gp2 * g2s + (mp.mpf(3) / 2) * g24) * tr_e
    g4Y2_3 = -((mp.mpf(19) / 4) * gp4 + (mp.mpf(21) / 2) * gp2 * g2s + (mp.mpf(9) / 4) * g24) * tr_u \
        - ((mp.mpf(5) / 4) * gp4 - (mp.mpf(9) / 2) * gp2 * g2s + (mp.mpf(9) / 4) * g24) * tr_d \
        - ((mp.mpf(25) / 4) * gp4 + (mp.mpf(11) / 2) * gp2 * g2s + (mp.mpf(3) / 4) * g24) * tr_e
    g4Y2_4 = (21 * tr_u - 9 * tr_d + 11 * tr_e) * gp2 * g2s
    b2_l1 = (
        -78 * l1 ** 3 - 20 * l1 * (l3 * l3 + l3 * l4) - 12 * l1 * l4 * l4 - 16 * l3 ** 3 - 24 * l3 * l3 * l4 - 32 * l3 * l4 * l4 - 12 * l4 ** 3
        + (18 * l1 * l1 + 8 * l3 * l3 + 8 * l3 * l4 + 4 * l4 * l4) * gp2
        + (54 * l1 * l1 + 24 * l3 * l3 + 24 * l3 * l4 + 6 * l4 * l4) * g2s
        + (mp.mpf(217) / 8 * l1 + 5 * l3 + mp.mpf(5) / 2 * l4) * gp4
        + (mp.mpf(39) / 4 * l1 + 5 * l4) * gp2 * g2s
        + (-mp.mpf(51) / 8 * l1 + 15 * l3 + mp.mpf(15) / 2 * l4) * g24 + g6_1
        - 24 * Td * l1 * l1 - 4 * Tu * (2 * l3 * l3 + 2 * l3 * l4 + l4 * l4)
        + l1 * (-3 * tr_d2 - tr_e2 - 9 * tr_ud + (mp.mpf(25) / 6 * gp2 + mp.mpf(45) / 2 * g2s + 80 * g3s) * tr_d
                + (mp.mpf(25) / 2 * gp2 + mp.mpf(15) / 2 * g2s) * tr_e)
        + 60 * tr_d3 + 20 * tr_e3 + 12 * tr_d2u + (mp.mpf(8) / 3 * gp2 - 64 * g3s) * tr_d2 - 8 * gp2 * tr_e2 + g4Y2_d
    )
    b2_l2 = (
        -78 * l2 ** 3 - 20 * l2 * (l3 * l3 + l3 * l4) - 12 * l2 * l4 * l4 - 16 * l3 ** 3 - 24 * l3 * l3 * l4 - 32 * l3 * l4 * l4 - 12 * l4 ** 3
        + (18 * l2 * l2 + 8 * l3 * l3 + 8 * l3 * l4 + 4 * l4 * l4) * gp2
        + (54 * l2 * l2 + 24 * l3 * l3 + 24 * l3 * l4 + 6 * l4 * l4) * g2s
        + (mp.mpf(217) / 8 * l2 + 5 * l3 + mp.mpf(5) / 2 * l4) * gp4
        + (mp.mpf(39) / 4 * l2 + 5 * l4) * gp2 * g2s
        + (-mp.mpf(51) / 8 * l2 + 15 * l3 + mp.mpf(15) / 2 * l4) * g24 + g6_1
        - 24 * Tu * l2 * l2 - 4 * Td * (2 * l3 * l3 + 2 * l3 * l4 + l4 * l4)
        + l2 * (-3 * tr_u2 - 9 * tr_ud + (mp.mpf(85) / 6 * gp2 + mp.mpf(45) / 2 * g2s + 80 * g3s) * tr_u)
        + 60 * tr_u3 + 12 * tr_u2d + (-mp.mpf(16) / 3 * gp2 - 64 * g3s) * tr_u2 + g4Y2_u
    )
    b2_l3 = (
        -15 * (l1 * l1 + l2 * l2) * l3 - 4 * (l1 * l1 + l2 * l2) * l4 - 36 * (l1 + l2) * l3 * l3
        - 16 * (l1 + l2) * l3 * l4 - 14 * (l1 + l2) * l4 * l4 - 12 * l3 ** 3 - 4 * l3 * l3 * l4 - 16 * l3 * l4 * l4 - 12 * l4 ** 3
        + (12 * (l1 + l2) * l3 + 4 * (l1 + l2) * l4 + 2 * l3 * l3 - 2 * l4 * l4) * gp2
        + (36 * (l1 + l2) * l3 + 18 * (l1 + l2) * l4 + 6 * l3 * l3 - 12 * l3 * l4 + 6 * l4 * l4) * g2s
        + (mp.mpf(15) / 4 * (l1 + l2) + mp.mpf(197) / 8 * l3 + mp.mpf(5) / 2 * l4) * gp4
        + (-mp.mpf(5) / 2 * (l1 + l2) + mp.mpf(11) / 4 * l3 - 3 * l4) * gp2 * g2s
        + (mp.mpf(45) / 4 * (l1 + l2) - mp.mpf(111) / 8 * l3 + mp.mpf(15) / 2 * l4) * g24 + g6_3
        - (4 * Td * l1 + 4 * Tu * l2) * (3 * l3 + l4) - 4 * (Tu + Td) * (l3 * l3 + l4 * l4)
        + l3 * (-mp.mpf(27) / 2 * (tr_u2 + tr_d2) - mp.mpf(9) / 2 * tr_e2 + 3 * tr_ud
                + (mp.mpf(85) / 12 * gp2 + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_u
                + (mp.mpf(25) / 12 * gp2 + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_d
                + (mp.mpf(25) / 4 * gp2 + mp.mpf(15) / 4 * g2s) * tr_e)
        + 36 * (tr_u2d + tr_d2u) + (-mp.mpf(4) / 3 * gp2 - 64 * g3s) * tr_ud + g4Y2_3
    )
    b2_l4 = (
        -7 * (l1 * l1 + l2 * l2) * l4 - 40 * (l1 + l2) * l3 * l4 - 20 * (l1 + l2) * l4 * l4
        - 28 * l3 * l3 * l4 - 28 * l3 * l4 * l4
        + (4 * (l1 + l2) * l4 + 4 * l3 * l4 + 8 * l4 * l4) * gp2 + (36 * l3 * l4 + 18 * l4 * l4) * g2s
        + (mp.mpf(157) / 8 * l4) * gp4 + (5 * (l1 + l2) + 2 * l3 + mp.mpf(51) / 4 * l4) * gp2 * g2s
        + (-mp.mpf(231) / 8 * l4) * g24 + g6_4
        - 4 * (Td * l1 + Tu * l2) * l4 - 8 * (Tu + Td) * (2 * l3 * l4 + l4 * l4)
        + l4 * (-mp.mpf(27) / 2 * (tr_u2 + tr_d2) - mp.mpf(9) / 2 * tr_e2 - 21 * tr_ud
                + (mp.mpf(85) / 12 * gp2 + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_u
                + (mp.mpf(25) / 12 * gp2 + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_d
                + (mp.mpf(25) / 4 * gp2 + mp.mpf(15) / 4 * g2s) * tr_e)
        - 24 * (tr_u2d + tr_d2u) + (mp.mpf(4) / 3 * gp2 + 64 * g3s) * tr_ud + g4Y2_4
    )
    return (dg1, dg2, dg3, k1 * b1_l1 + k2 * b2_l1, k1 * b1_l2 + k2 * b2_l2, k1 * b1_l3 + k2 * b2_l3, k1 * b1_l4 + k2 * b2_l4, dYu, dYd, dYe)


def state_add(s1, s2, scale=mp.mpf(1)):
    return tuple(s1[i] + scale * s2[i] for i in range(10))


def state_diff_norm(s1, s2):
    mx = mp.mpf(0)
    for i in range(7):
        d = abs(s1[i] - s2[i])
        if d > mx:
            mx = d
    for i in range(7, 10):
        d = mat_fro_norm(s1[i] - s2[i])
        if d > mx:
            mx = d
    return mx


def rge_gl4_evolve(state0, t_end, n_steps, model="2HDM_II", quartic_2loop=False, drop_Yu=False):
    s3 = mp.sqrt(3)
    a11 = mp.mpf(1) / 4
    a12 = mp.mpf(1) / 4 - s3 / 6
    a21 = mp.mpf(1) / 4 + s3 / 6
    a22 = mp.mpf(1) / 4
    h = mp.mpf(t_end) / n_steps
    y = state0
    t_cur = mp.mpf(0)
    ewsb_l1 = None
    ewsb_l2 = None
    l1_s1 = None
    l2_s1 = None
    fp_tol = mp.mpf(10) ** (-(mp.mp.dps - 6))
    for step_idx in range(n_steps):
        k0 = rge_rhs_gut(y, model=model, quartic_2loop=quartic_2loop, drop_Yu=drop_Yu)
        k1 = k0
        k2 = k0
        for _fp in range(12):
            y1 = state_add(state_add(y, k1, h * a11), k2, h * a12)
            y2 = state_add(state_add(y, k1, h * a21), k2, h * a22)
            nk1 = rge_rhs_gut(y1, model=model, quartic_2loop=quartic_2loop, drop_Yu=drop_Yu)
            nk2 = rge_rhs_gut(y2, model=model, quartic_2loop=quartic_2loop, drop_Yu=drop_Yu)
            diff = max(state_diff_norm(nk1, k1), state_diff_norm(nk2, k2))
            k1, k2 = nk1, nk2
            if diff < fp_tol:
                break
        y_next = state_add(state_add(y, k1, h / 2), k2, h / 2)
        t_next = t_cur + h
        if step_idx == 0:
            l1_s1, l2_s1 = y_next[3], y_next[4]
        else:
            if ewsb_l1 is None and y[3] > 0 and y_next[3] <= 0:
                ewsb_l1 = t_cur + (y[3] / (y[3] - y_next[3])) * h
            if ewsb_l2 is None and y[4] > 0 and y_next[4] <= 0:
                ewsb_l2 = t_cur + (y[4] / (y[4] - y_next[4])) * h
        y = y_next
        t_cur = t_next
    return y, {"t_EWSB_l1": ewsb_l1, "t_EWSB_l2": ewsb_l2, "l1_step1": l1_s1, "l2_step1": l2_s1}


def polar_curved_G_s12_refined(tau, solve_dps=28):
    """Refined polar mesh (r0=r_lat/8, n_ang=18, n_w=20, n_rad=22) -> Gauss-Bonnet < 1e-4!"""
    fuch = solve_fuchsian_gl8(tau, dps=solve_dps)
    with mp.workdps(solve_dps):
        tau = mp.mpc(tau)
        x, y = mp.re(tau), mp.im(tau)
        pi = mp.pi
        c_p = fuch["c_param"]
        Qinv = fuch["Qinv"]
        a_f = fuch["a_f"]
        b_f = fuch["b_f"]
        r0 = fuch["r_lat"] / 8
        th_c1 = mp.atan2(y, 1 + x)
        th_c2 = mp.atan2(y, -1 + x)
        qh = mp.exp(mp.mpc(0, 1) * pi * tau)

        def gl_nodes_weights(n):
            J = mp.zeros(n, n)
            for k in range(1, n):
                beta = k / mp.sqrt(4 * k * k - 1)
                J[k - 1, k] = beta
                J[k, k - 1] = beta
            ev, evec = mp.eigsy(J)
            return [ev[k] for k in range(n)], [2 * (evec[0, k] ** 2) for k in range(n)]

        ang_x, ang_w = gl_nodes_weights(18)
        w_x, w_w = gl_nodes_weights(20)

        def densities(z):
            u = pi * z
            imz = mp.im(z)
            pref = mp.sqrt(2 * y) * mp.exp(-2 * pi * imz * imz / y)
            c1 = mp.cos(u)
            s1 = mp.sin(u)
            c2 = 2 * c1 * c1 - 1
            s2 = 2 * s1 * c1
            th2 = mp.mpc(0)
            cn_o, sn_o = c1, s1
            qp = mp.mpc(1)
            n = 0
            while True:
                th2 += qp * cn_o
                if abs(qp) * (abs(cn_o) + abs(sn_o) + 1) < mp.mpf(10) ** (-18) and n > 2:
                    break
                n += 1
                qp *= qh ** (2 * n)
                cn_o, sn_o = cn_o * c2 - sn_o * s2, sn_o * c2 + cn_o * s2
            th2 *= 2 * mp.exp(mp.mpc(0, 1) * pi * tau / 4)
            th3 = mp.mpc(1)
            th4 = mp.mpc(1)
            cn_e, sn_e = c2, s2
            n = 1
            while True:
                qnn = qh ** (n * n)
                t = 2 * qnn * cn_e
                th3 += t
                th4 += (t if n % 2 == 0 else -t)
                if abs(qnn) * (abs(cn_e) + abs(sn_e) + 1) < mp.mpf(10) ** (-18) and n > 2:
                    break
                n += 1
                cn_e, sn_e = cn_e * c2 - sn_e * s2, sn_e * c2 + cn_e * s2
            return [pref * abs(th4) ** 2, pref * abs(th2) ** 2, pref * abs(th3) ** 2]

        def frob_psi(z):
            z2 = z * z
            sqz = mp.sqrt(z)
            lnz = mp.log(z)
            Sa = Sap = Sb = Sbp = mp.mpc(0)
            zp = mp.mpc(1)
            for k in range(18):
                Sa += a_f[k] * zp
                Sb += b_f[k] * zp
                if k >= 1:
                    Sap += (2 * k) * a_f[k] * (zp / z)
                    Sbp += (2 * k) * b_f[k] * (zp / z)
                zp *= z2
            u1v = sqz * Sa
            u1pv = Sa / (2 * sqz) + sqz * Sap
            u2v = u1v * lnz + sqz * Sb
            u2pv = u1pv * lnz + u1v / z + Sb / (2 * sqz) + sqz * Sbp
            return (
                u1v * Qinv[0, 0] + u2v * Qinv[1, 0], u1v * Qinv[0, 1] + u2v * Qinv[1, 1],
                u1pv * Qinv[0, 0] + u2pv * Qinv[1, 0], u1pv * Qinv[0, 1] + u2pv * Qinv[1, 1],
            )

        s3 = mp.sqrt(3)
        c1_g = (mp.mpf(1) - s3 / 3) / 2
        c2_g = (mp.mpf(1) + s3 / 3) / 2
        a11 = mp.mpf(1) / 4
        a12 = mp.mpf(1) / 4 - s3 / 6
        a21 = mp.mpf(1) / 4 + s3 / 6
        a22 = mp.mpf(1) / 4
        aa11 = a11 * a11 + a12 * a21
        aa12 = a11 * a12 + a12 * a22
        aa21 = a21 * a11 + a22 * a21
        aa22 = a21 * a12 + a22 * a22

        area = mp.mpf(0)
        G_raw = [mp.mpf(0)] * 3
        with mp.workdps(18):
            for th0, th1 in [(mp.mpf(0), th_c1), (th_c1, th_c2), (th_c2, pi)]:
                th_m = (th0 + th1) / 2
                th_h = (th1 - th0) / 2
                for ai in range(len(ang_x)):
                    th = th_m + th_h * ang_x[ai]
                    w_th = 2 * th_h * ang_w[ai]
                    cth = mp.cos(th)
                    sth = mp.sin(th)
                    dir_z = mp.mpc(cth, sth)
                    denom_u = abs(cth - (x / y) * sth)
                    R_th = (y / (2 * sth)) if sth > mp.mpf(10) ** (-13) else mp.mpf(10**9)
                    if denom_u > mp.mpf(10) ** (-13):
                        R_u = mp.mpf(1) / (2 * denom_u)
                        if R_u < R_th:
                            R_th = R_u
                    for wi in range(len(w_x)):
                        wv = (1 + w_x[wi]) / 2
                        dw = w_w[wi] / 2
                        rv = r0 * mp.exp(1 - 1 / wv)
                        zv = rv * dir_z
                        p1, p2, _, _ = frob_psi(zv)
                        im12 = mp.im(p1 * mp.conj(p2))
                        jac = w_th * dw * (rv * rv) / (wv * wv)
                        area += jac / (im12 * im12)
                        eom = abs(1 / im12)
                        ds = densities(zv)
                        for j in range(3):
                            G_raw[j] += jac * eom * ds[j]
                    n_rad = 22
                    dr = (R_th - r0) / n_rad
                    dz = dr * dir_z
                    dz2 = dz * dz
                    dzh = dz / 2
                    p1, p2, p1p, p2p = frob_psi(r0 * dir_z)
                    r_cur = r0
                    for _ in range(n_rad):
                        r1 = r_cur + c1_g * dr
                        r2 = r_cur + c2_g * dr
                        z1 = r1 * dir_z
                        z2 = r2 * dir_z
                        q1 = wp_theta1_logderiv(z1, tau) / 4 + c_p
                        q2 = wp_theta1_logderiv(z2, tau) / 4 + c_p
                        m11 = 1 + dz2 * aa11 * q1
                        m12 = dz2 * aa12 * q2
                        m21 = dz2 * aa21 * q1
                        m22 = 1 + dz2 * aa22 * q2
                        idet = 1 / (m11 * m22 - m12 * m21)
                        U1_1 = (m22 * (p1 + dz * c1_g * p1p) - m12 * (p1 + dz * c2_g * p1p)) * idet
                        U1_2 = (-m21 * (p1 + dz * c1_g * p1p) + m11 * (p1 + dz * c2_g * p1p)) * idet
                        U2_1 = (m22 * (p2 + dz * c1_g * p2p) - m12 * (p2 + dz * c2_g * p2p)) * idet
                        U2_2 = (-m21 * (p2 + dz * c1_g * p2p) + m11 * (p2 + dz * c2_g * p2p)) * idet
                        for rvn, zvn, u1n, u2n in [(r1, z1, U1_1, U2_1), (r2, z2, U1_2, U2_2)]:
                            im12 = mp.im(u1n * mp.conj(u2n))
                            jac = w_th * (dr / 2) * rvn
                            area += jac / (im12 * im12)
                            eom = abs(1 / im12)
                            ds = densities(zvn)
                            for j in range(3):
                                G_raw[j] += jac * eom * ds[j]
                        L1_1, L1_2 = -q1 * U1_1, -q2 * U1_2
                        L2_1, L2_2 = -q1 * U2_1, -q2 * U2_2
                        K1_1 = p1p + dz * (a11 * L1_1 + a12 * L1_2)
                        K1_2 = p1p + dz * (a21 * L1_1 + a22 * L1_2)
                        K2_1 = p2p + dz * (a11 * L2_1 + a12 * L2_2)
                        K2_2 = p2p + dz * (a21 * L2_1 + a22 * L2_2)
                        p1 += dzh * (K1_1 + K1_2)
                        p1p += dzh * (L1_1 + L1_2)
                        p2 += dzh * (K2_1 + K2_2)
                        p2p += dzh * (L2_1 + L2_2)
                        r_cur += dr
        mean_G = sum(G_raw) / 3
        return {
            "G_norm": [g / mean_G for g in G_raw],
            "gauss_bonnet_rel_err": abs(area / (2 * pi) - 1),
            "sl2r_err": fuch["sl2r_err"],
            "L2": fuch["L2"],
        }


def apply_metric_canon(Y, G_mat_L, G_mat_R):
    def inv_sqrt_H(G):
        ev, U = mp.eigh(G)
        D = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                D[i, j] = U[i, j] / mp.sqrt(mp.re(ev[j]))
        return mat_mul_3(D, mat_dag(U))

    return mat_mul_3(inv_sqrt_H(G_mat_L), mat_mul_3(Y, inv_sqrt_H(G_mat_R)))


def run_W4(saved_vacua):
    t0 = time.monotonic_ns()
    out = {}

    # W4.1: Guardrail 4 benchmark (SymPy + numeric GUT g1 + exact MV84 -29/240, -65/240 + Xing-Zhou)
    sym_bench = sympy_verify_chowdhury_eberhardt_gut()
    with mp.workdps(50):
        g1 = mp.mpf(9) / 20
        g2 = mp.mpf(13) / 20
        g3 = mp.mpf(11) / 10
        l1 = mp.mpf(1) / 10
        l2 = mp.mpf(3) / 20
        l3 = mp.mpf(1) / 20
        l4 = mp.mpf(-3) / 100
        yt, yb, ytau = mp.mpf(9) / 10, mp.mpf(2) / 5, mp.mpf(1) / 5
        rhs = rge_rhs_gut((g1, g2, g3, l1, l2, l3, l4, mp.diag([0, 0, yt]), mp.diag([0, 0, yb]), mp.diag([0, 0, ytau])), model="2HDM_II", quartic_2loop=False)
        k1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
        k2 = k1 * k1
        b1_u = yt * (mp.mpf(9) / 2 * yt ** 2 + mp.mpf(1) / 2 * yb ** 2 - mp.mpf(17) / 20 * g1 ** 2 - mp.mpf(9) / 4 * g2 ** 2 - 8 * g3 ** 2)
        b2_u = yt * (
            -12 * yt ** 4 - mp.mpf(5) / 2 * yt ** 2 * yb ** 2 - mp.mpf(5) / 2 * yb ** 4 - mp.mpf(3) / 4 * yb ** 2 * ytau ** 2
            + (mp.mpf(393) / 80 * g1 ** 2 + mp.mpf(225) / 16 * g2 ** 2 + 36 * g3 ** 2) * yt ** 2
            + (-mp.mpf(29) / 240 * g1 ** 2 + mp.mpf(33) / 16 * g2 ** 2 + mp.mpf(16) / 3 * g3 ** 2) * yb ** 2
            + mp.mpf(1267) / 600 * g1 ** 4 - mp.mpf(9) / 20 * g1 ** 2 * g2 ** 2 + mp.mpf(19) / 15 * g1 ** 2 * g3 ** 2
            - mp.mpf(21) / 4 * g2 ** 4 + 9 * g2 ** 2 * g3 ** 2 - 108 * g3 ** 4
            - 6 * l2 * yt ** 2 + (-2 * l3 + 2 * l4) * yb ** 2 + mp.mpf(3) / 2 * l2 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2
        )
        b1_d = yb * (mp.mpf(9) / 2 * yb ** 2 + mp.mpf(1) / 2 * yt ** 2 + ytau ** 2 - mp.mpf(1) / 4 * g1 ** 2 - mp.mpf(9) / 4 * g2 ** 2 - 8 * g3 ** 2)
        b2_d = yb * (
            -12 * yb ** 4 - mp.mpf(5) / 2 * yt ** 2 * yb ** 2 - mp.mpf(5) / 2 * yt ** 4 - mp.mpf(9) / 4 * yb ** 2 * ytau ** 2 - mp.mpf(9) / 4 * ytau ** 4
            + (mp.mpf(237) / 80 * g1 ** 2 + mp.mpf(225) / 16 * g2 ** 2 + 36 * g3 ** 2) * yb ** 2
            + (-mp.mpf(65) / 240 * g1 ** 2 + mp.mpf(33) / 16 * g2 ** 2 + mp.mpf(16) / 3 * g3 ** 2) * yt ** 2
            + (mp.mpf(15) / 8 * g1 ** 2 + mp.mpf(15) / 8 * g2 ** 2) * ytau ** 2
            - mp.mpf(113) / 600 * g1 ** 4 - mp.mpf(27) / 20 * g1 ** 2 * g2 ** 2 + mp.mpf(31) / 15 * g1 ** 2 * g3 ** 2
            - mp.mpf(21) / 4 * g2 ** 4 + 9 * g2 ** 2 * g3 ** 2 - 108 * g3 ** 4
            - 6 * l1 * yb ** 2 + (-2 * l3 + 2 * l4) * yt ** 2 + mp.mpf(3) / 2 * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2
        )
        ce_num_err = max(abs(rhs[7][2, 2] - (k1 * b1_u + k2 * b2_u)), abs(rhs[8][2, 2] - (k1 * b1_d + k2 * b2_d)))

    with mp.workdps(30):
        th_cb = mp.mpf(1) / 25
        R23 = mp.matrix([[1, 0, 0], [0, mp.cos(th_cb), mp.sin(th_cb)], [0, -mp.sin(th_cb), mp.cos(th_cb)]])
        Yu_xz = mp.diag([mp.mpf(1) / 1000, mp.mpf(1) / 100, mp.mpf(1)])
        Yd_xz = mat_mul_3(R23, mp.diag([mp.mpf(1) / 500, mp.mpf(1) / 50, mp.mpf(1) / 2]))
        Ye_xz = mp.diag([mp.mpf(1) / 500, mp.mpf(1) / 50, mp.mpf(1) / 3])
        st_xz = (mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), Yu_xz, Yd_xz, Ye_xz)
        vcb0 = extract_observables(Yu_xz, Yd_xz, Ye_xz)["absV"][1][2]
        st_1h, _ = rge_gl4_evolve(st_xz, mp.mpf(-1) / 10, 8, model="1HDM")
        st_2h, _ = rge_gl4_evolve(st_xz, mp.mpf(-1) / 10, 8, model="2HDM_II")
        dvcb_1h_down = extract_observables(st_1h[7], st_1h[8], st_1h[9])["absV"][1][2] - vcb0
        dvcb_2h_down = extract_observables(st_2h[7], st_2h[8], st_2h[9])["absV"][1][2] - vcb0

    out["guardrail4_benchmark"] = {
        "sympy_ce15_all_exact": sym_bench["ce15_all_exact"],
        "sympy_sm_1hdm_triple": sym_bench["sm_1hdm_triple"],
        "sympy_sm_1hdm_exact": sym_bench["sm_1hdm_exact"],
        "numeric_ce15_max_err": mp_str(ce_num_err, 12),
        "dvcb_1hdm_down": mp_str(dvcb_1h_down, 12),
        "dvcb_2hdm_II_down": mp_str(dvcb_2h_down, 12),
        "opposite_xing_zhou_sign_ok": bool(dvcb_1h_down < 0 and dvcb_2h_down > 0),
    }

    # W4.2: Refined polar curved spin-1/2 Dirac Kahler metric G_{s=1/2}(tau) (< 1e-4 Gauss-Bonnet!)
    tau_apex = mp.mpc(mp.mpf(1) / 2, mp.sqrt(5) / 2)
    tau_2 = mp.mpc(mp.mpf(13) / 100, mp.mpf(2))
    G_apex = polar_curved_G_s12_refined(tau_apex, solve_dps=28)
    G_tau2 = polar_curved_G_s12_refined(tau_2, solve_dps=28)
    out["curved_G_s12"] = {
        "tau_apex": {
            "G_norm": [mp_str(v, 14) for v in G_apex["G_norm"]],
            "gauss_bonnet_rel_err": mp_str(G_apex["gauss_bonnet_rel_err"], 10),
            "sl2r_err": mp_str(G_apex["sl2r_err"], 10),
        },
        "tau_2": {
            "G_norm": [mp_str(v, 14) for v in G_tau2["G_norm"]],
            "gauss_bonnet_rel_err": mp_str(G_tau2["gauss_bonnet_rel_err"], 10),
            "sl2r_err": mp_str(G_tau2["sl2r_err"], 10),
        },
    }

    # W4.3: Scope Card Section 4 RG unfolding (GUT g1(0)=1/2, exact MV84 -29/240 & -65/240, 1-loop quartics)
    #       + 2-loop quartic sensitivity check on UA and UD + gauge-covariant kappa_nu = Y_nu Y_nu^T PMNS!
    rg_runs = {}
    q2_sensitivity = {}
    max_step_halving = mp.mpf(0)
    with mp.workdps(26):
        alg26 = build_frame_c_algebra()
        am_m, bm_m = mp.mpf(4) / 15, mp.mpf(1) / 30
        ctx_t2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=30)
        ctx_ap = make_tau_ctx(mp.mpc(mp.mpf(1) / 2, mp.sqrt(5) / 2), solve_dps=30)
        bases_t2 = [
            assemble_Y_basis(alg26, ctx_t2, am_m, bm_m, 1, -4),
            assemble_Y_basis(alg26, ctx_t2, am_m, bm_m, 1, 2),
            assemble_Y_basis(alg26, ctx_t2, am_m, bm_m, -3, 6),
        ]
        Ynu_t2 = eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, -3, 0)
        Ynu_ap = eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, -3, 0)

        uv_states = {
            "UA_FrameC_y2": (
                eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, 1, -4),
                eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, 1, 2),
                eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, -3, 6),
                Ynu_t2, G_tau2["G_norm"],
            ),
            "UB_W3_DynamicVCW_y2": (
                lin_comb_3(bases_t2[0], saved_vacua["U_B"][0], False),
                lin_comb_3(bases_t2[1], saved_vacua["U_B"][1], False),
                lin_comb_3(bases_t2[2], saved_vacua["U_B"][1], False),
                Ynu_t2, G_tau2["G_norm"],
            ),
            "UC_FrameC_GeodesicApex": (
                eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, 1, -4),
                eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, 1, 2),
                eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, -3, 6),
                Ynu_ap, G_apex["G_norm"],
            ),
            "UD_W3_DynamicV4_ferro_y2": (
                lin_comb_3(bases_t2[0], saved_vacua["U_D"][0], False),
                lin_comb_3(bases_t2[1], saved_vacua["U_D"][1], False),
                lin_comb_3(bases_t2[2], saved_vacua["U_D"][1], False),
                Ynu_t2, G_tau2["G_norm"],
            ),
        }

        def run_single_rg(Yu_raw, Yd_raw, Ye_raw, Ynu_raw, Gn, curved=False, quartic_2loop=False, n_steps=80):
            if curved:
                Gm = mp.diag([mp.mpf(v) for v in Gn])
                Yu0 = apply_metric_canon(Yu_raw, Gm, Gm)
                Yd0 = apply_metric_canon(Yd_raw, Gm, Gm)
                Ye0 = apply_metric_canon(Ye_raw, Gm, Gm)
                Ynu0 = apply_metric_canon(Ynu_raw, Gm, Gm)
            else:
                Yu0, Yd0, Ye0, Ynu0 = Yu_raw, Yd_raw, Ye_raw, Ynu_raw
            obs_pre = extract_observables(Yu0, Yd0, Ye0)
            s_max = max(obs_pre["su"][2], obs_pre["sd"][2], obs_pre["se"][2])
            Yu0, Yd0, Ye0 = Yu0 / s_max, Yd0 / s_max, Ye0 / s_max
            st0 = (mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), Yu0, Yd0, Ye0)
            st_ir, ewsb = rge_gl4_evolve(st0, mp.mpf(-35), n_steps, model="2HDM_II", quartic_2loop=quartic_2loop)
            obs_uv = extract_observables(Yu0, Yd0, Ye0)
            obs_ir = extract_observables(st_ir[7], st_ir[8], st_ir[9])
            # Gauge-covariant Type-I seesaw kappa_nu = Y_nu Y_nu^T (M_R = I_3) with U_e at UV and IR
            _, Ue_uv, _ = jw_svd(Ye0)
            _, Ue_ir, _ = jw_svd(st_ir[9])
            kap_cov = mat_mul_3(Ynu0, Ynu0.T)
            ms_nu, Vtak, tres = takagi_6x6(kap_cov)
            U_nu = mp.matrix([[mp.conj(Vtak[i, j]) for j in range(3)] for i in range(3)])
            pmns = pmns_observables_from_U(mat_mul_3(mat_dag(Ue_uv), U_nu))
            pmns_ir = pmns_observables_from_U(mat_mul_3(mat_dag(Ue_ir), U_nu))
            dm_r = (ms_nu[1] ** 2 - ms_nu[0] ** 2) / (ms_nu[2] ** 2 - ms_nu[0] ** 2) if ms_nu[2] > ms_nu[0] else mp.mpf(0)
            g1_ir, g2_ir, g3_ir, l1_ir, l2_ir, l3_ir, l4_ir = st_ir[:7]
            std_ir = bool((obs_ir["absV"][0][1] > obs_ir["absV"][1][2]) and (obs_ir["absV"][1][2] > obs_ir["absV"][0][2]))
            return {
                "state_ir": st_ir,
                "summary": {
                    "g1_IR": mp_str(g1_ir, 14), "g2_IR": mp_str(g2_ir, 14), "g3_IR": mp_str(g3_ir, 14),
                    "l1_IR": mp_str(l1_ir, 14), "l2_IR": mp_str(l2_ir, 14),
                    "l3_IR": mp_str(l3_ir, 14), "l4_IR": mp_str(l4_ir, 14),
                    "yt_over_g3_IR": mp_str(obs_ir["su"][2] / g3_ir, 14),
                    "mb_over_mtau_IR": mp_str(obs_ir["sd"][2] / obs_ir["se"][2], 14),
                    "ms_over_mmu_IR": mp_str(obs_ir["sd"][1] / obs_ir["se"][1], 14),
                    "u_m2m3_UV": mp_str(obs_uv["u_m2m3"], 14), "u_m2m3_IR": mp_str(obs_ir["u_m2m3"], 14),
                    "d_m2m3_UV": mp_str(obs_uv["d_m2m3"], 14), "d_m2m3_IR": mp_str(obs_ir["d_m2m3"], 14),
                    "e_m2m3_UV": mp_str(obs_uv["e_m2m3"], 14), "e_m2m3_IR": mp_str(obs_ir["e_m2m3"], 14),
                    "V12_IR": mp_str(obs_ir["absV"][0][1], 14), "V23_IR": mp_str(obs_ir["absV"][1][2], 14),
                    "V13_IR": mp_str(obs_ir["absV"][0][2], 14), "J_CP_IR": mp_str(obs_ir["J_CP"], 14),
                    "std_ckm_IR": std_ir,
                    "t_EWSB_l1": mp_str(ewsb["t_EWSB_l1"], 12) if ewsb["t_EWSB_l1"] is not None else "none",
                    "t_EWSB_l2": mp_str(ewsb["t_EWSB_l2"], 12) if ewsb["t_EWSB_l2"] is not None else "none",
                    "canonical_neutrino_PMNS_YYT": {
                        "s12_sq": mp_str(pmns["s12_sq"], 12), "s23_sq": mp_str(pmns["s23_sq"], 12),
                        "s13_sq": mp_str(pmns["s13_sq"], 12), "J_PMNS": mp_str(pmns["J_PMNS"], 12),
                        "dm21_over_dm31": mp_str(dm_r, 12),
                        "s_nu_ratios": [mp_str(ms_nu[0] / ms_nu[2], 12), mp_str(ms_nu[1] / ms_nu[2], 12)],
                        "takagi_residual": mp_str(tres, 10),
                    },
                    "canonical_neutrino_PMNS_YYT_IR": {
                        "s12_sq": mp_str(pmns_ir["s12_sq"], 12), "s23_sq": mp_str(pmns_ir["s23_sq"], 12),
                        "s13_sq": mp_str(pmns_ir["s13_sq"], 12), "J_PMNS": mp_str(pmns_ir["J_PMNS"], 12),
                    },
                },
            }

        for uname, (Yu_r, Yd_r, Ye_r, Ynu_r, Gn) in uv_states.items():
            rf = run_single_rg(Yu_r, Yd_r, Ye_r, Ynu_r, Gn, curved=False, quartic_2loop=False, n_steps=80)
            rc = run_single_rg(Yu_r, Yd_r, Ye_r, Ynu_r, Gn, curved=True, quartic_2loop=False, n_steps=80)
            rg_runs[uname] = {"FLAT": rf["summary"], "CURVED": rc["summary"]}
            if uname in ("UA_FrameC_y2", "UD_W3_DynamicV4_ferro_y2"):
                rc160 = run_single_rg(Yu_r, Yd_r, Ye_r, Ynu_r, Gn, curved=True, quartic_2loop=False, n_steps=160)
                sh = state_diff_norm(rc["state_ir"], rc160["state_ir"])
                if sh > max_step_halving:
                    max_step_halving = sh
                # 2-loop quartic sensitivity check
                rc_q2 = run_single_rg(Yu_r, Yd_r, Ye_r, Ynu_r, Gn, curved=True, quartic_2loop=True, n_steps=80)
                q_diffs = {
                    k: mp_str(abs(mp.mpf(rc_q2["summary"][k]) - mp.mpf(rc["summary"][k])) / abs(mp.mpf(rc["summary"][k])), 8)
                    for k in ("l1_IR", "l2_IR", "l3_IR", "l4_IR")
                }
                q2_sensitivity[uname] = {
                    "t_EWSB_l1_2loopQ": rc_q2["summary"]["t_EWSB_l1"],
                    "t_EWSB_l2_2loopQ": rc_q2["summary"]["t_EWSB_l2"],
                    "quartic_rel_diffs_2loop_vs_1loop": q_diffs,
                    "max_quartic_rel_diff": mp_str(max(mp.mpf(v) for v in q_diffs.values()), 8),
                }

    out["rg_unfolding_t0_to_m35"] = rg_runs
    out["quartic_2loop_sensitivity"] = q2_sensitivity
    out["gl4_step_halving_80_vs_160_err"] = mp_str(max_step_halving, 12)

    # W4.4: 10-trial Cayley-transform Haar U(3)^5 invariance (scrambling Y_nu -> W_L Y_nu directly!)
    with mp.workdps(34):
        alg34 = build_frame_c_algebra()
        am_m, bm_m = mp.mpf(4) / 15, mp.mpf(1) / 30
        ctx_h = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=30)
        Yu_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, 1, -4)
        Yd_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, 1, 2)
        Ye_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, -3, 6)
        Ynu_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, -3, 0)
        Gm_b = mp.diag([mp.mpf(v) for v in G_tau2["G_norm"]])

        def full_pipeline(Yu_in, Yd_in, Ye_in, Ynu_in, GQ, Gu, Gd, GL, Ge, Gnu):
            Yu_c = apply_metric_canon(Yu_in, GQ, Gu)
            Yd_c = apply_metric_canon(Yd_in, GQ, Gd)
            Ye_c = apply_metric_canon(Ye_in, GL, Ge)
            Ynu_c = apply_metric_canon(Ynu_in, GL, Gnu)
            s_max = max(jw_svd(Yu_c)[0][2], jw_svd(Yd_c)[0][2], jw_svd(Ye_c)[0][2])
            st0 = (mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), Yu_c / s_max, Yd_c / s_max, Ye_c / s_max)
            st_ir, _ = rge_gl4_evolve(st0, mp.mpf(-5), 16, model="2HDM_II", quartic_2loop=False)
            obs_ir = extract_observables(st_ir[7], st_ir[8], st_ir[9])
            _, Ue_ir, _ = jw_svd(st_ir[9])
            ms, Vtak, _ = takagi_6x6(mat_mul_3(Ynu_c, Ynu_c.T))
            U_nu = mp.matrix([[mp.conj(Vtak[i, j]) for j in range(3)] for i in range(3)])
            Upmns = mat_mul_3(mat_dag(Ue_ir), U_nu)
            vec = (
                obs_ir["su"] + obs_ir["sd"] + obs_ir["se"]
                + [obs_ir["absV"][i][j] for i in range(3) for j in range(3)] + [obs_ir["J_CP"]]
                + ms + [abs(Upmns[i, j]) for i in range(3) for j in range(3)] + [jarlskog(Upmns)]
            )
            return vec, Ynu_c

        base_vec, Ynu_c0 = full_pipeline(Yu_b, Yd_b, Ye_b, Ynu_b, Gm_b, Gm_b, Gm_b, Gm_b, Gm_b, Gm_b)
        ms_lit0, _, _ = takagi_6x6(mat_mul_3(Ynu_c0.T, Ynu_c0))
        rng_h = Sha256Rng("AGY002_REFEREE_V2_CAYLEY_HAAR_U3_5")
        max_haar_err = mp.mpf(0)
        max_u_err = mp.mpf(0)
        max_broken_yty_err = mp.mpf(0)
        I3 = mp.eye(3)
        for trial in range(10):
            WQ = haar_u3_cayley(rng_h)
            Wu = haar_u3_cayley(rng_h)
            Wd = haar_u3_cayley(rng_h)
            WL = haar_u3_cayley(rng_h)
            We = haar_u3_cayley(rng_h)
            for W in (WQ, Wu, Wd, WL, We):
                ue = mat_fro_norm(mat_mul_3(mat_dag(W), W) - I3)
                if ue > max_u_err:
                    max_u_err = ue
            Yu_t = mat_mul_3(WQ, mat_mul_3(Yu_b, mat_dag(Wu)))
            Yd_t = mat_mul_3(WQ, mat_mul_3(Yd_b, mat_dag(Wd)))
            Ye_t = mat_mul_3(WL, mat_mul_3(Ye_b, mat_dag(We)))
            Ynu_t = mat_mul_3(WL, Ynu_b)
            GQ_t = mat_mul_3(WQ, mat_mul_3(Gm_b, mat_dag(WQ)))
            Gu_t = mat_mul_3(Wu, mat_mul_3(Gm_b, mat_dag(Wu)))
            Gd_t = mat_mul_3(Wd, mat_mul_3(Gm_b, mat_dag(Wd)))
            GL_t = mat_mul_3(WL, mat_mul_3(Gm_b, mat_dag(WL)))
            Ge_t = mat_mul_3(We, mat_mul_3(Gm_b, mat_dag(We)))
            vec_t, Ynu_ct = full_pipeline(Yu_t, Yd_t, Ye_t, Ynu_t, GQ_t, Gu_t, Gd_t, GL_t, Ge_t, Gm_b)
            terr = max(abs(vec_t[k] - base_vec[k]) / max(mp.mpf(1), abs(base_vec[k])) for k in range(len(base_vec)))
            if terr > max_haar_err:
                max_haar_err = terr
            ms_lit_t, _, _ = takagi_6x6(mat_mul_3(Ynu_ct.T, Ynu_ct))
            berr = max(abs(ms_lit_t[k] - ms_lit0[k]) / max(mp.mpf(10) ** (-12), ms_lit0[k]) for k in range(3))
            if berr > max_broken_yty_err:
                max_broken_yty_err = berr

    out["guardrail3_cayley_haar_U3_5"] = {
        "trials": 10,
        "max_cayley_unitarity_err": mp_str(max_u_err, 10),
        "max_observable_rel_err_covariant_YYT": mp_str(max_haar_err, 12),
        "broken_literal_YTY_WL_violation_rel_err": mp_str(max_broken_yty_err, 12),
    }
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 9. MODULE W5: SIX REFEREE PLANTED CONTROLS (RPF1 - RPF6)
# ============================================================================

def run_W5():
    t0 = time.monotonic_ns()
    out = {}
    P30_pts, P30_pairs = generate_P30()
    e30_nz_pairs = sorted({
        min((a, b), ((-a) % 30, (-b) % 30))
        for a in range(30) for b in range(30)
        if not (a == 0 and b == 0)
    })

    # RPF1: Drop +ln(y) from L_2(i/y) reproduces BOTH fixed S-partner (0.134, 0.178, 2.13)
    #       AND all-899 E[30]\{0} bijection match (0.123, 0.178, 0.323) & median (0.0372, 0.0789, 0.178)!
    rpf1_rows = []
    targets_max = [mp.mpf(123) / 1000, mp.mpf(178) / 1000, mp.mpf(323) / 1000]
    rpf1_caught = True
    with mp.workdps(24):
        alg24 = build_frame_c_algebra()
        axis_pairs = [
            (Fraction(5, 4), Fraction(4, 5)),
            (Fraction(3, 2), Fraction(2, 3)),
            (Fraction(5, 2), Fraction(2, 5)),
        ]
        for idx_p, (y_f, iy_f) in enumerate(axis_pairs):
            yv = mp.mpf(y_f.numerator) / y_f.denominator
            iyv = mp.mpf(iy_f.numerator) / iy_f.denominator
            L2_y = get_L2(mp.mpc(0, yv), solve_dps=28)
            ctx_y = make_tau_ctx(mp.mpc(0, yv), L2_val=L2_y)
            ctx_iy_bug = make_tau_ctx(mp.mpc(0, iyv), L2_val=L2_y)
            map_y = {}
            for p in P30_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                map_y[p] = extract_observables(
                    eval_Y_canonical(alg24, ctx_y, am, bm, 1, -4),
                    eval_Y_canonical(alg24, ctx_y, am, bm, 1, 2),
                    eval_Y_canonical(alg24, ctx_y, am, bm, -3, 6),
                )["vec9"]
            map_iy_all = {}
            e30_iy_vecs = []
            for p in e30_nz_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                v = extract_observables(
                    eval_Y_canonical(alg24, ctx_iy_bug, am, bm, 1, -4),
                    eval_Y_canonical(alg24, ctx_iy_bug, am, bm, 1, 2),
                    eval_Y_canonical(alg24, ctx_iy_bug, am, bm, -3, 6),
                )["vec9"]
                if v is not None:
                    map_iy_all[p] = v
                    e30_iy_vecs.append(v)
            # Fixed S-partner max distance
            mx_partner = mp.mpf(0)
            for a_i, b_i in P30_pts:
                p1 = min((a_i, b_i), ((-a_i) % 30, (-b_i) % 30))
                wp_a, wp_b = (-b_i) % 30, a_i % 30
                p2 = min((wp_a, wp_b), ((-wp_a) % 30, (-wp_b) % 30))
                d9 = b1980_dist(map_y[p1], map_iy_all[p2])
                if d9 > mx_partner:
                    mx_partner = d9
            # All-899 best-match distances over P_30
            best_all899 = [min(b1980_dist(map_y[p], v2) for v2 in e30_iy_vecs) for p in P30_pairs]
            mx_899 = max(best_all899)
            med_899 = median_mpf(best_all899)
            if abs(mx_899 - targets_max[idx_p]) > mp.mpf(1) / 100:
                rpf1_caught = False
            rpf1_rows.append({
                "pair": f"({frac_str(y_f)}, {frac_str(iy_f)})",
                "buggy_S_partner_max_d": mp_str(mx_partner, 10),
                "b1980_all899_max_d": mp_str(mx_899, 10),
                "b1980_all899_median_d": mp_str(med_899, 10),
            })
    out["RPF1_drop_ln_y_reproduces_B1980"] = {"rows": rpf1_rows, "caught": rpf1_caught}

    # RPF2: Drop sqrt(y) breaks absolute s_k invariance by exact factor |c*tau + d|
    with mp.workdps(35):
        alg35 = build_frame_c_algebra()
        tau1 = mp.mpc(mp.mpf(13) / 100, mp.mpf(6) / 5)
        L2_1 = get_L2(tau1, solve_dps=30)
        ctx1 = make_tau_ctx(tau1, L2_val=L2_1)
        ctxS = make_tau_ctx(-1 / tau1, L2_val=L2_1 + mp.log(abs(tau1)))
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        s0 = jw_svd(eval_Y_canonical(alg35, ctx1, am, bm, 1, -4, weight_zero=False))[0][2]
        sS = jw_svd(eval_Y_canonical(alg35, ctxS, (-bm) % 1, am, 1, -4, weight_zero=False))[0][2]
        ratio_S = sS / s0
        exp_fac = abs(tau1)
        ratio_err = abs(ratio_S - exp_fac) / exp_fac
        rel_break = abs(sS - s0) / s0
    out["RPF2_drop_sqrt_y_breaks_abs_sk"] = {
        "bare_s3_ratio_S": mp_str(ratio_S, 16),
        "expected_abs_c_tau_plus_d": mp_str(exp_fac, 16),
        "ratio_match_rel_err": mp_str(ratio_err, 10),
        "rel_invariance_break": mp_str(rel_break, 12),
        "caught": bool(rel_break > mp.mpf(1) / 10 and ratio_err < mp.mpf(10) ** (-25)),
    }

    # RPF3: Flip V_4 -> -V_4 and V_CW -> -V_CW destroys hierarchy / reverses optimum
    with mp.workdps(26):
        alg26 = build_frame_c_algebra()
        ctx2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=28)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        bases = [assemble_Y_basis(alg26, ctx2, am, bm, qL, qR) for qL, qR in [(1, -4), (1, 2), (-3, 6)]]
        _, _, mu2 = eval_point_potentials(alg26, ctx2, am, bm)
        rv4g = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "V4", "rpf3_v4_g", sign_flip=1, n_starts=6)
        rv4f = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "V4", "rpf3_v4_f", sign_flip=-1, n_starts=6)
        rcwg = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "VCW", "rpf3_cw_g", sign_flip=1, n_starts=6)
        rcwf = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "VCW", "rpf3_cw_f", sign_flip=-1, n_starts=6)
        rpf3_ok = bool(
            rv4f["r_h"] > rv4g["r_h"] + mp.mpf(3) / 10
            and rv4f["obs"]["d_m2m3"] > rv4g["obs"]["d_m2m3"] * 5
            and abs(rcwf["r_h"] - rcwg["r_h"]) > mp.mpf(3) / 10
        )
    out["RPF3_sign_flip_destroys_hierarchy"] = {
        "V4_good_r": mp_str(rv4g["r_h"], 10), "V4_good_d_m2m3": mp_str(rv4g["obs"]["d_m2m3"], 10),
        "V4_flipped_r": mp_str(rv4f["r_h"], 10), "V4_flipped_d_m2m3": mp_str(rv4f["obs"]["d_m2m3"], 10),
        "VCW_good_r": mp_str(rcwg["r_h"], 10), "VCW_flipped_r": mp_str(rcwf["r_h"], 10),
        "caught": rpf3_ok,
    }

    # RPF4: Wrong point action w*gamma breaks T and M
    with mp.workdps(30):
        alg30 = build_frame_c_algebra()
        tau1 = mp.mpc(mp.mpf(13) / 100, mp.mpf(6) / 5)
        L2_1 = get_L2(tau1, solve_dps=28)
        ctx1 = make_tau_ctx(tau1, L2_val=L2_1)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        v0 = extract_observables(
            eval_Y_canonical(alg30, ctx1, am, bm, 1, -4),
            eval_Y_canonical(alg30, ctx1, am, bm, 1, 2),
            eval_Y_canonical(alg30, ctx1, am, bm, -3, 6),
        )["vec9"]
        wd = {}
        for gname, (ga, gb, gc, gd) in [("T", (1, 1, 0, 1)), ("M", (2, 1, 1, 1))]:
            ctxg = make_tau_ctx((ga * tau1 + gb) / (gc * tau1 + gd), L2_val=L2_1 + mp.log(abs(gc * tau1 + gd)))
            vg = extract_observables(
                eval_Y_canonical(alg30, ctxg, (ga * am + gc * bm) % 1, (gb * am + gd * bm) % 1, 1, -4),
                eval_Y_canonical(alg30, ctxg, (ga * am + gc * bm) % 1, (gb * am + gd * bm) % 1, 1, 2),
                eval_Y_canonical(alg30, ctxg, (ga * am + gc * bm) % 1, (gb * am + gd * bm) % 1, -3, 6),
            )["vec9"]
            wd[gname] = b1980_dist(v0, vg)
    out["RPF4_wrong_point_action_breaks_T_and_M"] = {
        "T_wrong_action_9log_dist": mp_str(wd["T"], 12),
        "M_wrong_action_9log_dist": mp_str(wd["M"], 12),
        "caught": bool(wd["T"] > mp.mpf(1) / 10 and wd["M"] > mp.mpf(1) / 10),
    }

    # RPF5: Drop Y_u from 2HDM RG breaks benchmark & flips lambda_2(IR) sign!
    with mp.workdps(26):
        alg26 = build_frame_c_algebra()
        ctx2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=28)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        Yu0 = eval_Y_canonical(alg26, ctx2, am, bm, 1, -4)
        Yd0 = eval_Y_canonical(alg26, ctx2, am, bm, 1, 2)
        Ye0 = eval_Y_canonical(alg26, ctx2, am, bm, -3, 6)
        s_max = max(jw_svd(Yu0)[0][2], jw_svd(Yd0)[0][2], jw_svd(Ye0)[0][2])
        st0 = (mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), Yu0 / s_max, Yd0 / s_max, Ye0 / s_max)
        st_g, _ = rge_gl4_evolve(st0, mp.mpf(-35), 40, model="2HDM_II", quartic_2loop=False, drop_Yu=False)
        st_b, _ = rge_gl4_evolve(st0, mp.mpf(-35), 40, model="2HDM_II", quartic_2loop=False, drop_Yu=True)
        rg_g = rge_rhs_gut((mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, 0, 0, 0, 0, mp.diag([0, 0, 1]), mp.diag([0, 0, mp.mpf(1) / 2]), mp.diag([0, 0, mp.mpf(1) / 3])), drop_Yu=False)
        rg_b = rge_rhs_gut((mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, 0, 0, 0, 0, mp.diag([0, 0, 1]), mp.diag([0, 0, mp.mpf(1) / 2]), mp.diag([0, 0, mp.mpf(1) / 3])), drop_Yu=True)
        b_brk = abs(rg_g[7][2, 2] - rg_b[7][2, 2])
    out["RPF5_drop_Yu_breaks_RG_and_EWSB"] = {
        "good_l2_IR": mp_str(st_g[4], 12), "dropped_Yu_l2_IR": mp_str(st_b[4], 12),
        "benchmark_dyt_break": mp_str(b_brk, 10),
        "caught": bool(b_brk > mp.mpf(1) / 1000 and st_g[4] > 0 and st_b[4] < 0),
    }

    # RPF6: Non-unitary basis rotation breaks Haar invariance
    with mp.workdps(30):
        alg30 = build_frame_c_algebra()
        ctx2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=28)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        Yu0 = eval_Y_canonical(alg30, ctx2, am, bm, 1, -4)
        Yd0 = eval_Y_canonical(alg30, ctx2, am, bm, 1, 2)
        Ye0 = eval_Y_canonical(alg30, ctx2, am, bm, -3, 6)
        obs0 = extract_observables(Yu0, Yd0, Ye0)
        S_nu = mp.matrix([[mp.mpf(1), mp.mpf(3) / 10, 0], [0, mp.mpf(3) / 2, mp.mpf(1) / 5], [0, 0, mp.mpf(2) / 3]])
        obs_bad = extract_observables(mat_mul_3(S_nu, Yu0), mat_mul_3(S_nu, Yd0), mat_mul_3(S_nu, Ye0))
        nu_break = max(
            abs(obs_bad["u_m2m3"] - obs0["u_m2m3"]) / obs0["u_m2m3"],
            abs(obs_bad["absV"][0][1] - obs0["absV"][0][1]) / obs0["absV"][0][1],
        )
    out["RPF6_non_unitary_breaks_invariance"] = {
        "rel_observable_break": mp_str(nu_break, 12),
        "caught": bool(nu_break > mp.mpf(1) / 10),
    }

    out["all_6_caught"] = all(
        out[k]["caught"]
        for k in (
            "RPF1_drop_ln_y_reproduces_B1980",
            "RPF2_drop_sqrt_y_breaks_abs_sk",
            "RPF3_sign_flip_destroys_hierarchy",
            "RPF4_wrong_point_action_breaks_T_and_M",
            "RPF5_drop_Yu_breaks_RG_and_EWSB",
            "RPF6_non_unitary_breaks_invariance",
        )
    )
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 10. SELF-AST PURITY AUDIT (RG6) & MAIN ORCHESTRATOR
# ============================================================================

def ast_purity_audit(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    float_lits = 0
    complex_lits = 0
    bad_casts = 0
    bad_imports = []
    forbidden = {"numpy", "scipy", "math", "cmath", "random", "statistics", "frontier"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_lits += 1
            elif isinstance(node.value, complex):
                complex_lits += 1
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
                bad_casts += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in forbidden:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in forbidden:
                bad_imports.append(node.module)
    return {
        "ast_float_literals": float_lits,
        "ast_complex_literals": complex_lits,
        "ast_float_complex_casts": bad_casts,
        "forbidden_imports": bad_imports,
        "script_sha256": hashlib.sha256(src.encode("utf-8")).hexdigest(),
        "pass": (float_lits == 0 and complex_lits == 0 and bad_casts == 0 and len(bad_imports) == 0),
    }


def main():
    t_total = time.monotonic_ns()
    script_path = os.path.abspath(__file__)
    out_dir = os.path.dirname(script_path)
    out_json_path = os.path.join(out_dir, "referee_a2_whole_instrument_v3_out.json")
    out_sha_path = os.path.join(out_dir, "OUTPUT_SHA256.txt")

    mp.mp.dps = 30
    w1 = run_W1()
    w2 = run_W2()
    w3, saved_vacua = run_W3()
    w4 = run_W4(saved_vacua)
    w5 = run_W5()
    ast_audit = ast_purity_audit(script_path)

    # All 6 Referee Gates computed strictly from numerical results (Guardrail 2!)
    rg1 = bool(
        w1["part_A"]["pass"]
        and mp.mpf(w1["part_B"]["max_raw_cocycle_err"]) < mp.mpf(10) ** (-8)
        and mp.mpf(w1["part_B"]["max_s_cov_9log_dist"]) < mp.mpf(10) ** (-38)
        and mp.mpf(w1["part_B"]["max_full_norm_rel_err"]) < mp.mpf(10) ** (-38)
        and len(w1["part_B"]["K_neq_1_duality_audit"]) == 7
    )
    rg2 = bool(
        w2["symbolic_tropical_288"]["counts"]["all_288"]["total"] == 288
        and w2["finite_height_288"]["y_2"]["counts"]["all_288"]["total"] == 288
        and w2["finite_height_288"]["y_3"]["counts"]["all_288"]["total"] == 288
        and mp.mpf(w2["geodesic_gamma_M"]["max_periodicity_err_M_tau"]) < mp.mpf(10) ** (-40)
        and mp.mpf(w2["geodesic_gamma_M"]["max_basepoint_shift_err_all3_closed_orbits"]) < mp.mpf(10) ** (-8)
        and mp.mpf(w2["W_LV1"]["max_neg_qQ_rel_err"]) < mp.mpf(10) ** (-40)
    )
    rg3 = bool(
        w3["higgs_direction_optimization"]["all_1doublet_minima_M2M3_compliant"]
        and mp.mpf(w3["higgs_direction_optimization"]["max_grad_norm"]) < mp.mpf(10) ** (-6)
        and mp.mpf(w3["modular_all288_invariance"]["max_rel_err"]) < mp.mpf(10) ** (-30)
        and w3["cusp_norm_exponent_theorem"]["total_pairs"] == 288
    )
    rg4 = bool(
        w4["guardrail4_benchmark"]["sympy_ce15_all_exact"]
        and w4["guardrail4_benchmark"]["sympy_sm_1hdm_exact"]
        and mp.mpf(w4["guardrail4_benchmark"]["numeric_ce15_max_err"]) < mp.mpf(10) ** (-40)
        and w4["guardrail4_benchmark"]["opposite_xing_zhou_sign_ok"]
        and mp.mpf(w4["curved_G_s12"]["tau_apex"]["gauss_bonnet_rel_err"]) < mp.mpf(10) ** (-3)
        and mp.mpf(w4["curved_G_s12"]["tau_2"]["gauss_bonnet_rel_err"]) < mp.mpf(10) ** (-3)
        and mp.mpf(w4["gl4_step_halving_80_vs_160_err"]) < mp.mpf(10) ** (-6)
        and all(
            v["t_EWSB_l1_2loopQ"] == "none"
            and v["t_EWSB_l2_2loopQ"] == "none"
            and mp.mpf(v["max_quartic_rel_diff"]) < mp.mpf(1) / 50
            for v in w4["quartic_2loop_sensitivity"].values()
        )
        and mp.mpf(w4["guardrail3_cayley_haar_U3_5"]["max_observable_rel_err_covariant_YYT"]) < mp.mpf(10) ** (-25)
        and mp.mpf(w4["guardrail3_cayley_haar_U3_5"]["broken_literal_YTY_WL_violation_rel_err"]) > mp.mpf(1)
    )
    rg5 = bool(w5["all_6_caught"])
    rg6 = bool(ast_audit["pass"])

    payload = {
        "card_id": "AGY-002_A2-WHOLE-INSTRUMENT",
        "role": "COLD_ROOM_ZERO_TRUST_DISJOINT_REFEREE_V3",
        "firewall": "0 of 19",
        "W1": w1, "W2": w2, "W3": w3, "W4": w4, "W5": w5,
        "RG6_ast_audit": ast_audit,
        "gates": {
            "RG1": rg1, "RG2": rg2, "RG3": rg3, "RG4": rg4, "RG5": rg5, "RG6": rg6,
            "all_6_gates_pass": bool(rg1 and rg2 and rg3 and rg4 and rg5 and rg6),
        },
        "total_runtime_s": elapsed_sec_str(t_total),
    }

    raw_json = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    def reject_float(s):
        raise ValueError(f"JSON float token forbidden: {s}")

    json.loads(raw_json, parse_float=reject_float)

    with open(out_json_path, "w", encoding="utf-8") as f:
        f.write(raw_json)
    digest = hashlib.sha256(raw_json.encode("utf-8")).hexdigest()
    with open(out_sha_path, "w", encoding="utf-8") as f:
        f.write(f"{digest}  referee_a2_whole_instrument_v3_out.json\n")

    print(f"SEALED {out_json_path} sha256={digest} runtime={payload['total_runtime_s']}s")


if __name__ == "__main__":
    main()
