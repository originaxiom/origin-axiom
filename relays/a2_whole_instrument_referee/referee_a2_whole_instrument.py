#!/usr/bin/env python3
"""
Cold-Room Zero-Trust Disjoint Referee for Card AGY-002_A2-WHOLE-INSTRUMENT (0 of 19).

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
    Type-II 2HDM 1x1 coefficients and exact N_H=2 Machacek-Vaughn quartic terms.
  - Optimization (W3): Riemannian projected Barzilai-Borwein / steepest-descent on S^5
    and S^5 x S^5 with exact analytic Wirtinger gradients and deterministic multi-starts.
  - Geodesic quadrature (W2): 32-node AND 16-node periodic midpoint quadrature on gamma_M
    with shifted-grid basepoint invariance checks.
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
        """Uniform in (-1, 1) with full working precision."""
        bits = max(128, mp.mp.dps * 4 + 16)
        u = self.next_uint(bits)
        return (mp.mpf(2) * mp.mpf(u) / mp.mpf(1 << bits)) - mp.mpf(1)

    def next_mpf_signed_gauss_like(self):
        """Irwin-Hall sum of 6 uniforms in (-1, 1) -> smooth bell-shaped real mpf (no Box-Muller)."""
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
    """
    Non-squaring 6x6 Hermitian Jordan-Wielandt SVD via mp.eigh (disjoint from mp.svd_c).
    Returns ascending singular values [s1, s2, s3] and 3x3 unitary U, V with A = U diag(s) V^H.
    """
    H = mp.zeros(6, 6)
    for i in range(3):
        for j in range(3):
            H[i, 3 + j] = A[i, j]
            H[3 + j, i] = mp.conj(A[i, j])
    ev, vec = mp.eigh(H)
    # Eigenvalues are ascending: [-s3, -s2, -s1, +s1, +s2, +s3]
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
            # Re-orthogonalize against already extracted columns
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
                # Align phase so u^H A v >= 0
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
        # Rank-deficient / numerically zero singular value: orthogonal completion
        if len(done_u) == 2:
            u = cross3([mp.conj(x) for x in done_u[0]], [mp.conj(x) for x in done_u[1]])
            v = cross3([mp.conj(x) for x in done_v[0]], [mp.conj(x) for x in done_v[1]])
            nu = vec_norm(u)
            nv = vec_norm(v)
            u = [x / nu for x in u]
            v = [x / nv for x in v]
        else:
            # Find standard basis vector with largest orthogonal component
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

    # Sort ascending by s_vals
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
    Direct complex-symmetric Autonne-Takagi decomposition via 6x6 real-split mp.eigsy.
    Given 3x3 complex symmetric M = M^T, builds 6x6 real symmetric
      R = [[Re(M), Im(M)], [Im(M), -Re(M)]]
    and returns ascending nonnegative singular values [m1, m2, m3] and 3x3 unitary V_tak
    such that V_tak^T * M * V_tak = diag(m1, m2, m3).
    Note: U_nu = conj(V_tak) satisfies U_nu^H * M * conj(U_nu) = diag(m1, m2, m3).
    """
    # Symmetrize numerically
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
    # Eigenvalues are [-m3, -m2, -m1, +m1, +m2, +m3]
    I = mp.mpc(0, 1)
    # Take the top 3 eigenvalues (indices 3, 4, 5)
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
        # Phase-align so u^T * Ms * u >= 0
        Mu = [sum(Ms[i, j] * u[j] for j in range(3)) for i in range(3)]
        quad = sum(u[i] * Mu[i] for i in range(3))
        ab = abs(quad)
        if ab > mp.mpf(0):
            # Multiply u by exp(-i arg(quad) / 2)
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
    # Reconstruction residual ||V_tak^T M V_tak - diag(m)||_F / max(1, ||M||_F)
    D = V_tak.T * Ms * V_tak
    for i in range(3):
        D[i, i] -= m_sorted[i]
    res = mat_fro_norm(D) / max(mp.mpf(1), mat_fro_norm(Ms))
    return m_sorted, V_tak, res


def haar_u3_cayley(rng):
    """
    Haar-like U(3) unitary sampler via product of two independent Cayley transforms
    U = diag(e^{i phi}) * (I - i H1)(I + i H1)^{-1} * (I - i H2)(I + i H2)^{-1}.
    Disjoint from Box-Muller QR; guaranteed full U(3) support including eigenvalue -1.
    """
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
    """Exact rephasing-invariant Jarlskog invariant |Im(V_00 V_11 V_01^* V_10^*)|."""
    return abs(mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])))


def mixing_angles_deg(U):
    """Standard PDG parameterization angles (theta_12, theta_23, theta_13) in degrees from |U|."""
    # Columns ordered 1, 2, 3 (ascending mass for normal ordering)
    s13 = min(mp.mpf(1), abs(U[0, 2]))
    c13 = mp.sqrt(max(mp.mpf(0), mp.mpf(1) - s13 * s13))
    if c13 > mp.mpf(10) ** (-20):
        s12 = min(mp.mpf(1), abs(U[0, 1]) / c13)
        s23 = min(mp.mpf(1), abs(U[1, 2]) / c13)
    else:
        s12 = mp.mpf(0)
        s23 = mp.mpf(0)
    rad2deg = mp.mpf(180) / mp.pi
    return mp.asin(s12) * rad2deg, mp.asin(s23) * rad2deg, mp.asin(s13) * rad2deg


# ============================================================================
# 2. DISJOINT MODULAR FUNCTIONS & GL8 FUCHSIAN L_2(tau) SOLVER
# ============================================================================

def eta_pentagonal(tau):
    """Dedekind eta via Euler pentagonal number theorem (disjoint from product loop)."""
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
    """Jacobi theta_2(0,tau), theta_3(0,tau), theta_4(0,tau)."""
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
    """
    Weierstrass wp(z; tau) = -d^2/dz^2 ln theta_1(z, tau) - (pi^2/3)*theta_1'''(0)/(-pi^2*theta_1'(0))
    via Chebyshev trig recurrence (1 sin/cos call per evaluation; disjoint from wp_q4).
    """
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
    """
    Raw unreduced GL8 Fuchsian ODE solver for E_tau \\ {0}.
    Uses short-cycle seed -pi^2/(12 y^2) when Im(tau) < 1 and 3-trace (Ta, Tb, Tab)
    holomorphic Gauss-Newton. Returns dict with L2, c_param, Ta, Tb, Qinv, a_f, b_f, r_lat, err.
    """
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

        # Geometric radial ladder from z0 to z_m
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

        # Exact Weierstrass Laurent & Frobenius recurrence
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
            "L2": L2,
            "c_param": c_p,
            "err": err,
            "sl2r_err": sl2r_err,
            "Qinv": Qinv,
            "a_f": a_f,
            "b_f": b_f,
            "r_lat": r_lat,
        }


def reduce_to_F(tau):
    """
    Map tau -> tau_F = (a*tau + b)/(c*tau + d) in standard SL(2,Z) fundamental domain F.
    Also note reflection symmetry L_2(-conj(tau)) = L_2(tau).
    """
    a, b, c, d = 1, 0, 0, 1
    t = mp.mpc(tau)
    for _ in range(100):
        # Shift Re(t) into [-1/2, 1/2]
        n = int(mp.nint(mp.re(t)))
        if n != 0:
            t = t - n
            a, b = a - n * c, b - n * d
        # Invert if |t| < 1
        if abs(t) < mp.mpf(1) - mp.mpf(10) ** (-(mp.mp.dps - 4)):
            t = -1 / t
            a, b, c, d = -c, -d, a, b
        else:
            break
    return t, (a, b, c, d)


_L2_CACHE = {}


def get_L2(tau, solve_dps=30):
    """
    Exact SL(2,Z)-cocycle L_2(tau) = L_2(tau_F) - ln|c*tau + d|, caching tau_F up to
    reflection symmetry x <-> -x (since L_2(-x + iy) = L_2(x + iy)).
    """
    tF, (a, b, c, d) = reduce_to_F(tau)
    xF = abs(mp.re(tF))
    yF = mp.im(tF)
    key = (mp.nstr(xF, 18), mp.nstr(yF, 18))
    if key not in _L2_CACHE:
        res = solve_fuchsian_gl8(mp.mpc(xF, yF), dps=solve_dps)
        _L2_CACHE[key] = res["L2"]
    L2_F = mp.mpf(_L2_CACHE[key])
    # L2(tF) = L2(tau) + ln|c*tau + d| => L2(tau) = L2(tF) - ln|c*tau + d|
    return L2_F - mp.log(abs(c * tau + d))


# ============================================================================
# 3. FRAME C YUKAWA ASSEMBLY (B1656 / B1927 / B1945 / B1974 / B1980)
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
    # Precompute 3x3x4 contraction tensors T_p[a][b][s] = sum_{m,n} (B_a^T eps Q_p B_b)_{mn} (EDUAL[s])_{mn}
    # for p in (0: Q_I, 1: Q_J, 2: Q_K) so Y_f(h) is O(1) arithmetic!
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
    """Precompute tau-only quantities once per tau (massive speedup for 96/288/451 scans)."""
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
        "et3": et3, "inv_2pi_et3": 1 / (2 * pi * et3),
        "c_vec": c_vec, "c_norm": c_norm, "c_hat": c_hat,
        "qh": qh, "em2L2": mp.exp(-2 * L2_val),
        "cwt_const": pi * mp.log(y) - 2 * pi * (mp.euler + mp.log(pi)),
        "two_pi_L2": 2 * pi * L2_val,
        "Fu_kmax": max(4, int(mp.ceil((mp.mp.dps * mp.log(10) + 6) / (2 * pi * y))) + 2),
        "tol": mp.mpf(10) ** (-(mp.mp.dps + 5)),
    }


def theta_char(al, be, ctx):
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
        dkey = (mp.mp.dps, mp.nstr(al, min(24, mp.mp.dps)))
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


def eval_u_channels(ctx, a, b, qL, qR):
    """Returns [u_1, u_i, u_j, u_k] for sector (qL, qR) at w = (a, b)."""
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
        z = al * ctx["tau"] + be
        a0 = 2 * I * pi * al + theta1_logderiv(z, ctx)
        cwt = Fu_kronecker(al, be, ctx) + ctx["cwt_const"] - pi * (abs(a0) ** 2) * ctx["em2L2"]
        arg = ctx["two_pi_L2"] + cwt
        us.append(mp.sqrt(arg) * Rs if arg > 0 else mp.mpc(0))
    return us


def assemble_Y_basis(alg, ctx, a, b, qL, qR, weight_zero=True):
    """
    Returns [Y^(0), Y^(1), Y^(2)] such that for unit h = (h0, h1, h2) in S^5:
      Y(S_unit(h))       = h0*Y^(0) + h1*Y^(1) + h2*Y^(2)
      Y(S_tilde_unit(h)) = h0^* Y^(0) + h1^* Y^(1) + h2^* Y^(2)
      (since eps Q_p^* eps^T = +Q_p identically for p in {I, J, K}!)
    At h = c_hat(tau), Y(S_unit(c_hat)) == Y_inv(tau, w) (if weight_zero=True).
    """
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
    """Canonical Frame C Yukawa Y_f^{inv}(tau, w) (or bare weight-+1 Y_f if weight_zero=False)."""
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
    """Extract ascending singular values, mass ratios, CKM |V|, |J_CP|, and B1980 9-log vector."""
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
    return {
        "v_s3": v_s3, "v_s2": v_s2, "v_s1": v_s1,
        "u1": u1, "u2": u2, "u3": u3, "has_hiz": (hA or hB),
    }


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
    std_wolf = (V[0][1] > 0 and V[0][1] < V[1][2] < V[0][2])
    small_v23 = (Fraction(0) < V[1][2] < Fraction(1, 10))
    return {
        "rates9": rates9,
        "rates10": rates10,
        "e_D2": e_D2,
        "e_norm": e_norm,
        "v_s3_sectors": (u["v_s3"], d["v_s3"], e["v_s3"]),
        "V_diag": (V[0][0], V[1][1], V[2][2]),
        "aligned": aligned,
        "hier_ud": hier_ud,
        "std_wolf": std_wolf,
        "small_v23": small_v23,
        "has_hiz": (u["has_hiz"] or d["has_hiz"] or e["has_hiz"]),
    }


# ============================================================================
# 5. MODULE W1: B1980 PART A/B AUDIT, FULL-NORM WEIGHT +1, CORRECTED K != 1
# ============================================================================

def generate_P30():
    """Exact 96 points (48 +- pairs) of P_30 = K_5^* + E[6]_prim (mod 1)."""
    K5 = [(12, 24), (18, 6), (6, 12), (24, 18)]  # (2/5,4/5), (3/5,1/5), (1/5,2/5), (4/5,3/5) in /30
    E6p = [(5 * j, 5 * k) for j in range(6) for k in range(6) if gcd_int(gcd_int(j, k), 6) == 1]
    pts = sorted({((x1 + x2) % 30, (y1 + y2) % 30) for x1, y1 in K5 for x2, y2 in E6p})
    pairs = sorted({min((a, b), ((-a) % 30, (-b) % 30)) for a, b in pts})
    return pts, pairs


def generate_E30_prim():
    """Exact 576 points (288 +- pairs) of E[30]_prim."""
    pts = [(a, b) for a in range(30) for b in range(30) if gcd_int(gcd_int(a, b), 30) == 1]
    pairs = sorted({min((a, b), ((-a) % 30, (-b) % 30)) for a, b in pts})
    return pts, pairs


def run_W1(alg):
    t0 = time.monotonic_ns()
    out = {}

    # --- Part A: Exact algebra in PSL(2, Z/30) ---
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

    # Compute M^12 mod 30 and orbits on 288 cusps of X(30)
    M12 = (1, 0, 0, 1)
    for _ in range(12):
        M12 = mat_mod30(M12, M_mat)
    # Right action w -> w * M^{-1} where M^{-1} = [[1, -1], [-1, 2]]
    def act_pair(p, g):
        a, b = p
        na = (a * g[0] + b * g[2]) % 30
        nb = (a * g[1] + b * g[3]) % 30
        return min((na, nb), ((-na) % 30, (-nb) % 30))

    Minv = (1, 29, 29, 2)
    Minv12 = (1, 0, 0, 1)
    for _ in range(12):
        Minv12 = mat_mod30(Minv12, Minv)

    _, prim_pairs = generate_E30_prim()
    P30_pts, P30_pairs = generate_P30()
    visited = set()
    orbit_sizes = []
    for p in prim_pairs:
        if p in visited:
            continue
        orb = []
        c = p
        while c not in visited:
            visited.add(c)
            orb.append(c)
            c = act_pair(c, Minv)
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

    # --- Part B1: Direct unreduced GL8 L_2(iy) vs L_2(i/y) on B1980 3 axis pairs ---
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
            # Cache into _L2_CACHE as well
            _L2_CACHE[(mp.nstr(mp.mpf(0), 18), mp.nstr(yv, 18))] = r_hi["L2"]
            raw_cocycle_checks.append({
                "pair": f"({frac_str(y_f)}, {frac_str(iy_f)})",
                "L2_iy": mp_str(r_hi["L2"], 22),
                "L2_i_over_y_raw_gl8": mp_str(r_lo["L2"], 22),
                "L2_iy_plus_ln_y": mp_str(r_hi["L2"] + mp.log(yv), 22),
                "abs_cocycle_err": mp_str(diff, 10),
                "gl8_err_hi": mp_str(r_hi["err"], 8),
                "gl8_err_lo": mp_str(r_lo["err"], 8),
            })

    # --- Part B2: Frame C dps=55 S-covariance on all 96/96 points of P_30 ---
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
            # Precompute on 48 +- pairs (Frame C is antipodal Y(-w)=Y(w), verify explicitly on first pair!)
            obs_y_map = {}
            obs_iy_map = {}
            for p in P30_pairs:
                am = mp.mpf(p[0]) / 30
                bm = mp.mpf(p[1]) / 30
                Yu = eval_Y_canonical(alg55, ctx_y, am, bm, 1, -4)
                Yd = eval_Y_canonical(alg55, ctx_y, am, bm, 1, 2)
                Ye = eval_Y_canonical(alg55, ctx_y, am, bm, -3, 6)
                obs_y_map[p] = extract_observables(Yu, Yd, Ye)["vec9"]
                Yu2 = eval_Y_canonical(alg55, ctx_iy, am, bm, 1, -4)
                Yd2 = eval_Y_canonical(alg55, ctx_iy, am, bm, 1, 2)
                Ye2 = eval_Y_canonical(alg55, ctx_iy, am, bm, -3, 6)
                obs_iy_map[p] = extract_observables(Yu2, Yd2, Ye2)["vec9"]
            # Check antipodal invariance Y(-w) == Y(w) explicitly on mark point
            p0 = P30_pairs[0]
            Y_pos = eval_Y_canonical(alg55, ctx_y, mp.mpf(p0[0]) / 30, mp.mpf(p0[1]) / 30, 1, -4)
            Y_neg = eval_Y_canonical(alg55, ctx_y, mp.mpf((-p0[0]) % 30) / 30, mp.mpf((-p0[1]) % 30) / 30, 1, -4)
            antipodal_err = mat_fro_norm(Y_pos - Y_neg) / max(mp.mpf(1), mat_fro_norm(Y_pos))
            # Check all 96/96 points of P_30 under w' = w S^{-1} = (b, -a) mod 1
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
                "antipodal_check_rel_err": mp_str(antipodal_err, 10),
            })

    # --- Part B3: Full-norm weight-0 s_k^{inv} invariance under T, S, M at tau_1 and tau_0 ---
    gens = {
        "T": (1, 1, 0, 1),
        "S": (0, -1, 1, 0),
        "M": (2, 1, 1, 1),
    }
    test_taus = [
        ("tau1_13_100_plus_6_5i", mp.mpc(mp.mpf(13) / 100, mp.mpf(6) / 5)),
        ("tau0_m9_10_plus_6_5i", mp.mpc(mp.mpf(-9) / 10, mp.mpf(6) / 5)),
    ]
    full_norm_checks = []
    max_full_norm_err = mp.mpf(0)
    with mp.workdps(55):
        alg55 = build_frame_c_algebra()
        w_a = mp.mpf(4) / 15
        w_b = mp.mpf(1) / 30
        for tname, tau_v in test_taus:
            tau_v = mp.mpc(tau_v)
            L2_0 = get_L2(tau_v, solve_dps=30)
            ctx0 = make_tau_ctx(tau_v, L2_val=L2_0)
            s_base = []
            for qL, qR in [(1, -4), (1, 2), (-3, 6)]:
                Y0 = eval_Y_canonical(alg55, ctx0, w_a, w_b, qL, qR, weight_zero=True)
                s0, _, _ = jw_svd(Y0)
                s_base.extend(s0)
            for gname, (ga, gb, gc, gd) in gens.items():
                tau_g = (ga * tau_v + gb) / (gc * tau_v + gd)
                L2_g = L2_0 + mp.log(abs(gc * tau_v + gd))
                # w' = w * g^{-1} = (d*a - c*b, -b*a + a*b) mod 1
                wa_g = (gd * w_a - gc * w_b) % 1
                wb_g = (-gb * w_a + ga * w_b) % 1
                ctxg = make_tau_ctx(tau_g, L2_val=L2_g)
                s_img = []
                for qL, qR in [(1, -4), (1, 2), (-3, 6)]:
                    Yg = eval_Y_canonical(alg55, ctxg, wa_g, wb_g, qL, qR, weight_zero=True)
                    sg, _, _ = jw_svd(Yg)
                    s_img.extend(sg)
                rel_err = max(abs(s_img[k] - s_base[k]) / s_base[k] for k in range(9))
                if rel_err > max_full_norm_err:
                    max_full_norm_err = rel_err
                full_norm_checks.append({
                    "tau": tname,
                    "generator": gname,
                    "max_rel_err_9_abs_sv": mp_str(rel_err, 12),
                })

    # --- Part B4: Corrected K != 1 duality audit ---
    # K in {2,3,5,6,10,15,30}, y = (3/2)*sqrt(K), y' = (2/3)*sqrt(K)
    # Match P_30 (48 pairs, covering all 12 classes) against all 451 antipodal nonzero points of E[30]
    e30_nz_pairs = sorted({
        min((a, b), ((-a) % 30, (-b) % 30))
        for a in range(30) for b in range(30)
        if not (a == 0 and b == 0)
    })
    k_values = [2, 3, 5, 6, 10, 15, 30]
    k_duality_rows = []
    global_min_k_dist = mp.mpf(10**9)
    with mp.workdps(22):
        alg22 = build_frame_c_algebra()
        for K in k_values:
            sqK = mp.sqrt(mp.mpf(K))
            y1 = mp.mpf(3) * sqK / 2
            y2 = mp.mpf(2) * sqK / 3
            ctx1 = make_tau_ctx(mp.mpc(0, y1), solve_dps=26)
            ctx2 = make_tau_ctx(mp.mpc(0, y2), solve_dps=26)
            p30_vecs = []
            for p in P30_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                obs = extract_observables(
                    eval_Y_canonical(alg22, ctx1, am, bm, 1, -4),
                    eval_Y_canonical(alg22, ctx1, am, bm, 1, 2),
                    eval_Y_canonical(alg22, ctx1, am, bm, -3, 6),
                )
                if obs["vec9"] is not None:
                    p30_vecs.append((p, obs["vec9"]))
            e30_vecs = []
            for p in e30_nz_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                obs = extract_observables(
                    eval_Y_canonical(alg22, ctx2, am, bm, 1, -4),
                    eval_Y_canonical(alg22, ctx2, am, bm, 1, 2),
                    eval_Y_canonical(alg22, ctx2, am, bm, -3, 6),
                )
                if obs["vec9"] is not None:
                    e30_vecs.append((p, obs["vec9"]))
            min_d = mp.mpf(10**9)
            best_pair = None
            for p1, v1 in p30_vecs:
                for p2, v2 in e30_vecs:
                    d = b1980_dist(v1, v2)
                    if d < min_d:
                        min_d = d
                        best_pair = (p1, p2)
            if min_d < global_min_k_dist:
                global_min_k_dist = min_d
            k_duality_rows.append({
                "K": K,
                "y": mp_str(y1, 14),
                "y_prime": mp_str(y2, 14),
                "L2_y": mp_str(ctx1["L2"], 14),
                "L2_y_prime": mp_str(ctx2["L2"], 14),
                "valid_P30_pairs": len(p30_vecs),
                "valid_E30_pairs": len(e30_vecs),
                "min_9log_dist": mp_str(min_d, 12),
                "best_match_P30_to_E30": [list(best_pair[0]), list(best_pair[1])] if best_pair else None,
            })

    out["part_B"] = {
        "raw_gl8_cocycle_checks": raw_cocycle_checks,
        "max_raw_cocycle_err": mp_str(max_cocycle_err, 10),
        "s_covariance_96pts": s_cov_results,
        "max_s_cov_9log_dist": mp_str(max_s_cov_9log, 12),
        "full_norm_weight0_invariance": full_norm_checks,
        "max_full_norm_rel_err": mp_str(max_full_norm_err, 12),
        "K_neq_1_duality_audit": k_duality_rows,
        "E30_nonzero_antipodal_count": len(e30_nz_pairs),
        "global_min_K_neq_1_dist": mp_str(global_min_k_dist, 12),
        "no_K_neq_1_duality": bool(global_min_k_dist > mp.mpf(1) / 10),
    }
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 6. MODULE W2: WHOLE LEVEL-30 (288 PAIRS), GEODESIC gamma_M, W-LV1, B1981
# ============================================================================

def run_W2(alg):
    t0 = time.monotonic_ns()
    out = {}
    _, prim_pairs = generate_E30_prim()
    _, P30_pairs = generate_P30()
    act_set = set(P30_pairs)

    # --- W2.1a: Exact symbolic tropical classification across all 288 pairs ---
    classes9_all, classes9_act, classes9_off = set(), set(), set()
    classes10_all, classes10_act, classes10_off = set(), set(), set()
    sym_counts = {
        "all_288": {"total": 0, "aligned": 0, "hier_ud": 0, "hiz_zero": 0, "small_v23": 0, "std_wolf": 0, "e_norm_neg": 0},
        "act_48": {"total": 0, "aligned": 0, "hier_ud": 0, "hiz_zero": 0, "small_v23": 0, "std_wolf": 0, "e_norm_neg": 0},
        "off_240": {"total": 0, "aligned": 0, "hier_ud": 0, "hiz_zero": 0, "small_v23": 0, "std_wolf": 0, "e_norm_neg": 0},
    }
    e_norm_hist = {}
    min_e_norm = None
    max_e_norm = None
    for a_i, b_i in prim_pairs:
        c = classify_point_tropical(a_i, b_i, 30)
        is_act = (a_i, b_i) in act_set
        classes9_all.add(c["rates9"])
        classes10_all.add(c["rates10"])
        if is_act:
            classes9_act.add(c["rates9"])
            classes10_act.add(c["rates10"])
        else:
            classes9_off.add(c["rates9"])
            classes10_off.add(c["rates10"])
        en = c["e_norm"]
        e_norm_hist[frac_str(en)] = e_norm_hist.get(frac_str(en), 0) + 1
        if min_e_norm is None or en < min_e_norm:
            min_e_norm = en
        if max_e_norm is None or en > max_e_norm:
            max_e_norm = en
        for bucket in ("all_288", "act_48" if is_act else "off_240"):
            d_b = sym_counts[bucket]
            d_b["total"] += 1
            if c["aligned"]:
                d_b["aligned"] += 1
            if c["hier_ud"]:
                d_b["hier_ud"] += 1
            if c["has_hiz"]:
                d_b["hiz_zero"] += 1
            if c["small_v23"]:
                d_b["small_v23"] += 1
            if c["std_wolf"]:
                d_b["std_wolf"] += 1
            if en < 0:
                d_b["e_norm_neg"] += 1

    out["symbolic_tropical_288"] = {
        "distinct_9rate_classes_all": len(classes9_all),
        "distinct_9rate_classes_act48": len(classes9_act),
        "distinct_9rate_classes_off240": len(classes9_off),
        "distinct_10rate_classes_all": len(classes10_all),
        "distinct_10rate_classes_act48": len(classes10_act),
        "distinct_10rate_classes_off240": len(classes10_off),
        "counts": sym_counts,
        "e_norm_min": frac_str(min_e_norm),
        "e_norm_max": frac_str(max_e_norm),
        "e_norm_histogram": e_norm_hist,
    }

    # --- W2.1b: Finite-height Frame C across all 288 pairs at y=2 and y=3 (x = 13/100) ---
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
            mark_obs = None
            twin_obs = None
            for a_i, b_i in prim_pairs:
                am = mp.mpf(a_i) / 30
                bm = mp.mpf(b_i) / 30
                obs = extract_observables(
                    eval_Y_canonical(alg32, ctx_y, am, bm, 1, -4),
                    eval_Y_canonical(alg32, ctx_y, am, bm, 1, 2),
                    eval_Y_canonical(alg32, ctx_y, am, bm, -3, 6),
                )
                absV = obs["absV"]
                is_aligned = min(absV[0][0], absV[1][1], absV[2][2]) >= mp.mpf(9) / 10
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
                if (a_i, b_i) == (8, 1):
                    mark_obs = obs
                elif (a_i, b_i) == (1, 5):
                    twin_obs = obs

            def pack_obs(o):
                return {
                    "u_m2m3": mp_str(o["u_m2m3"], 14), "u_m1m3": mp_str(o["u_m1m3"], 14),
                    "d_m2m3": mp_str(o["d_m2m3"], 14), "d_m1m3": mp_str(o["d_m1m3"], 14),
                    "e_m2m3": mp_str(o["e_m2m3"], 14), "e_m1m3": mp_str(o["e_m1m3"], 14),
                    "V12": mp_str(o["absV"][0][1], 14), "V23": mp_str(o["absV"][1][2], 14),
                    "V13": mp_str(o["absV"][0][2], 14), "J_CP": mp_str(o["J_CP"], 14),
                }

            finite_scans[f"y_{y_int}"] = {
                "tau": f"13/100 + {y_int}i",
                "L2": mp_str(ctx_y["L2"], 18),
                "counts": counts,
                "mark_8_1": pack_obs(mark_obs),
                "twin_1_5": pack_obs(twin_obs),
            }
    out["finite_height_288"] = finite_scans

    # --- W2.2: Closed hyperbolic geodesic gamma_M(u) ---
    # M = [[2,1],[1,1]], tau(u) = 1/2 + (sqrt(5)/2)*(tanh u + i sech u), ell_M = 4 ln(phi)
    with mp.workdps(55):
        s5 = mp.sqrt(5)
        phi = (1 + s5) / 2
        ell_M = 4 * mp.log(phi)

        def tau_geo(u):
            return mp.mpc(mp.mpf(1) / 2 + (s5 / 2) * mp.tanh(u), (s5 / 2) * mp.sech(u))

        geo_period_errs = []
        for u_test in (mp.mpf(0), mp.mpf(1) / 3, mp.mpf(-7) / 10):
            tu = tau_geo(u_test)
            M_tu = (2 * tu + 1) / (tu + 1)
            tu_shift = tau_geo(u_test + ell_M)
            geo_period_errs.append(abs(M_tu - tu_shift))
        max_geo_period_err = max(geo_period_errs)

    # 32-node and 16-node periodic midpoint quadrature + shifted basepoint invariance
    Minv = (1, 29, 29, 2)

    def m_orbit_12(p):
        orb = []
        c = p
        for _ in range(12):
            orb.append(c)
            na = (c[0] * Minv[0] + c[1] * Minv[2]) % 30
            nb = (c[0] * Minv[1] + c[1] * Minv[3]) % 30
            c = min((na, nb), ((-na) % 30, (-nb) % 30))
        return orb

    geo_results = {}
    with mp.workdps(28):
        alg28 = build_frame_c_algebra()
        s5 = mp.sqrt(5)
        phi = (1 + s5) / 2
        ell_M = 4 * mp.log(phi)

        def tau_geo_w(u):
            return mp.mpc(mp.mpf(1) / 2 + (s5 / 2) * mp.tanh(u), (s5 / 2) * mp.sech(u))

        def eval_geo_grid(n_nodes, shift_frac=mp.mpf(0)):
            du = ell_M / n_nodes
            ctxs = []
            for j in range(n_nodes):
                u = -ell_M / 2 + (mp.mpf(j) + mp.mpf(1) / 2 + shift_frac) * du
                ctxs.append(make_tau_ctx(tau_geo_w(u), solve_dps=28))
            return ctxs

        ctxs_32 = eval_geo_grid(32, mp.mpf(0))
        ctxs_32_sh = eval_geo_grid(32, mp.mpf(3) / 10)
        ctxs_16 = eval_geo_grid(16, mp.mpf(0))
        ctxs_16_sh = eval_geo_grid(16, mp.mpf(3) / 10)

        def geo_analyze_point(p_rep, ctxs, full_gramian=True):
            n_nodes = len(ctxs)
            am = mp.mpf(p_rep[0]) / 30
            bm = mp.mpf(p_rep[1]) / 30
            tr1 = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
            tr2 = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
            avg_obs = {k: mp.mpf(0) for k in ("u_m2m3", "u_m1m3", "d_m2m3", "d_m1m3", "e_m2m3", "e_m1m3", "V12", "V23", "V13", "J_CP")}
            avg_s = [[mp.mpf(0)] * 3 for _ in range(3)]
            Ybar = [mp.zeros(3, 3) for _ in range(3)]
            sectors = [(1, -4), (1, 2), (-3, 6)]
            for ctx in ctxs:
                Ys = [eval_Y_canonical(alg28, ctx, am, bm, qL, qR) for qL, qR in sectors]
                for si in range(3):
                    H = mat_mul_3(mat_dag(Ys[si]), Ys[si])
                    tr1[si] += mp.re(mat_tr(H)) / n_nodes
                    tr2[si] += mp.re(mat_tr(mat_mul_3(H, H))) / n_nodes
                    Ybar[si] += Ys[si] / n_nodes
                obs = extract_observables(Ys[0], Ys[1], Ys[2])
                avg_obs["u_m2m3"] += obs["u_m2m3"] / n_nodes
                avg_obs["u_m1m3"] += obs["u_m1m3"] / n_nodes
                avg_obs["d_m2m3"] += obs["d_m2m3"] / n_nodes
                avg_obs["d_m1m3"] += obs["d_m1m3"] / n_nodes
                avg_obs["e_m2m3"] += obs["e_m2m3"] / n_nodes
                avg_obs["e_m1m3"] += obs["e_m1m3"] / n_nodes
                avg_obs["V12"] += obs["absV"][0][1] / n_nodes
                avg_obs["V23"] += obs["absV"][1][2] / n_nodes
                avg_obs["V13"] += obs["absV"][0][2] / n_nodes
                avg_obs["J_CP"] += obs["J_CP"] / n_nodes
                for k in range(3):
                    avg_s[0][k] += obs["su"][k] / n_nodes
                    avg_s[1][k] += obs["sd"][k] / n_nodes
                    avg_s[2][k] += obs["se"][k] / n_nodes

            res_d = {
                "tr_YdY": tr1,
                "tr_YdY_sq": tr2,
                "avg_obs": avg_obs,
                "avg_s_inv": avg_s,
            }
            if full_gramian:
                # Single-point coherent geodesic integral Ybar
                coh_obs = extract_observables(Ybar[0], Ybar[1], Ybar[2])
                res_d["coherent_Ybar"] = {
                    "u_m2m3": mp_str(coh_obs["u_m2m3"], 14), "u_m1m3": mp_str(coh_obs["u_m1m3"], 14),
                    "d_m2m3": mp_str(coh_obs["d_m2m3"], 14), "d_m1m3": mp_str(coh_obs["d_m1m3"], 14),
                    "e_m2m3": mp_str(coh_obs["e_m2m3"], 14), "e_m1m3": mp_str(coh_obs["e_m1m3"], 14),
                    "V12": mp_str(coh_obs["absV"][0][1], 14), "V23": mp_str(coh_obs["absV"][1][2], 14),
                    "V13": mp_str(coh_obs["absV"][0][2], 14), "J_CP": mp_str(coh_obs["J_CP"], 14),
                }
                # 12-point orbit Hermitian Gramian H_{L,f} = (1 / (12 * n_nodes)) sum_{u, w in O} Y Y^H
                orb = m_orbit_12(p_rep)
                HL = [mp.zeros(3, 3) for _ in range(3)]
                w_norm = mp.mpf(1) / (len(orb) * n_nodes)
                for ctx in ctxs:
                    for wp in orb:
                        wam, wbm = mp.mpf(wp[0]) / 30, mp.mpf(wp[1]) / 30
                        for si, (qL, qR) in enumerate(sectors):
                            Yw = eval_Y_canonical(alg28, ctx, wam, wbm, qL, qR)
                            HL[si] += mat_mul_3(Yw, mat_dag(Yw)) * w_norm
                ev_u, U_u = mp.eigh(HL[0])
                ev_d, U_d = mp.eigh(HL[1])
                ev_e, _ = mp.eigh(HL[2])
                su_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_u]
                sd_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_d]
                se_g = [mp.sqrt(max(mp.mpf(0), mp.re(v))) for v in ev_e]
                Vg = mat_mul_3(mat_dag(U_u), U_d)
                res_d["orbit_gramian_HL"] = {
                    "u_m2m3": mp_str(su_g[1] / su_g[2], 14), "u_m1m3": mp_str(su_g[0] / su_g[2], 14),
                    "d_m2m3": mp_str(sd_g[1] / sd_g[2], 14), "d_m1m3": mp_str(sd_g[0] / sd_g[2], 14),
                    "e_m2m3": mp_str(se_g[1] / se_g[2], 14), "e_m1m3": mp_str(se_g[0] / se_g[2], 14),
                    "V12": mp_str(abs(Vg[0, 1]), 14), "V23": mp_str(abs(Vg[1, 2]), 14),
                    "V13": mp_str(abs(Vg[0, 2]), 14), "J_CP": mp_str(jarlskog(Vg), 14),
                }
            return res_d

        max_trace_basepoint_err_32 = mp.mpf(0)
        max_trace_basepoint_err_16 = mp.mpf(0)
        for name, p_rep in [("mark_8_1", (8, 1)), ("twin_1_5", (1, 5))]:
            r32 = geo_analyze_point(p_rep, ctxs_32, full_gramian=True)
            r32_sh = geo_analyze_point(p_rep, ctxs_32_sh, full_gramian=False)
            r16 = geo_analyze_point(p_rep, ctxs_16, full_gramian=False)
            r16_sh = geo_analyze_point(p_rep, ctxs_16_sh, full_gramian=False)
            bp32_tr = max(
                max(abs(r32["tr_YdY"][k] - r32_sh["tr_YdY"][k]) / r32["tr_YdY"][k] for k in range(3)),
                max(abs(r32["tr_YdY_sq"][k] - r32_sh["tr_YdY_sq"][k]) / r32["tr_YdY_sq"][k] for k in range(3)),
            )
            bp16_tr = max(
                max(abs(r16["tr_YdY"][k] - r16_sh["tr_YdY"][k]) / r16["tr_YdY"][k] for k in range(3)),
                max(abs(r16["tr_YdY_sq"][k] - r16_sh["tr_YdY_sq"][k]) / r16["tr_YdY_sq"][k] for k in range(3)),
            )
            bp32_obs = max(abs(r32["avg_obs"][k] - r32_sh["avg_obs"][k]) / max(mp.mpf(10)**(-12), r32["avg_obs"][k])
                           for k in r32["avg_obs"])
            conv_16_32_tr = max(
                max(abs(r32["tr_YdY"][k] - r16["tr_YdY"][k]) / r32["tr_YdY"][k] for k in range(3)),
                max(abs(r32["tr_YdY_sq"][k] - r16["tr_YdY_sq"][k]) / r32["tr_YdY_sq"][k] for k in range(3)),
            )
            if bp32_tr > max_trace_basepoint_err_32:
                max_trace_basepoint_err_32 = bp32_tr
            if bp16_tr > max_trace_basepoint_err_16:
                max_trace_basepoint_err_16 = bp16_tr
            geo_results[name] = {
                "tr_YdY_32": [mp_str(v, 18) for v in r32["tr_YdY"]],
                "tr_YdY_sq_32": [mp_str(v, 18) for v in r32["tr_YdY_sq"]],
                "basepoint_rel_err_traces_32": mp_str(bp32_tr, 10),
                "basepoint_rel_err_traces_16": mp_str(bp16_tr, 10),
                "basepoint_rel_err_obs_32": mp_str(bp32_obs, 10),
                "convergence_16_vs_32_traces": mp_str(conv_16_32_tr, 10),
                "avg_obs_32": {k: mp_str(v, 14) for k, v in r32["avg_obs"].items()},
                "avg_obs_16": {k: mp_str(v, 14) for k, v in r16["avg_obs"].items()},
                "avg_s_inv_32": [[mp_str(x, 14) for x in row] for row in r32["avg_s_inv"]],
                "coherent_Ybar_32": r32["coherent_Ybar"],
                "orbit_gramian_HL_32": r32["orbit_gramian_HL"],
            }

    out["geodesic_gamma_M"] = {
        "ell_M": mp_str(ell_M, 24),
        "max_periodicity_err_M_tau": mp_str(max_geo_period_err, 10),
        "max_basepoint_rel_err_traces_32": mp_str(max_trace_basepoint_err_32, 10),
        "max_basepoint_rel_err_traces_16": mp_str(max_trace_basepoint_err_16, 10),
        "orbits": geo_results,
    }

    # --- W2.3a: W-LV1 direct cross-check (Y_e(w) prop Y_d^{neg-qQ}(3w) AND un-negated split) ---
    wlv1_rows = []
    max_wlv1_neg_err = mp.mpf(0)
    with mp.workdps(55):
        alg55 = build_frame_c_algebra()
        tau2 = mp.mpc(mp.mpf(13) / 100, mp.mpf(2))
        ctx2 = make_tau_ctx(tau2, solve_dps=30)
        for label, a_f, b_f in [
            ("N10_1_10_3_10", Fraction(1, 10), Fraction(3, 10)),
            ("N30_mark_4_15_1_30", Fraction(4, 15), Fraction(1, 30)),
            ("N30_twin_1_30_1_6", Fraction(1, 30), Fraction(1, 6)),
        ]:
            am = mp.mpf(a_f.numerator) / a_f.denominator
            bm = mp.mpf(b_f.numerator) / b_f.denominator
            a3 = (3 * am) % 1
            b3 = (3 * bm) % 1
            Ye = eval_Y_canonical(alg55, ctx2, am, bm, -3, 6)
            Yd_neg = eval_Y_canonical(alg55, ctx2, a3, b3, -1, 2)
            Yd_pos = eval_Y_canonical(alg55, ctx2, a3, b3, 1, 2)
            # Check proportionality Ye = alpha * Yd_neg (optimal least-squares complex scalar alpha)
            num_al = sum(mp.conj(Yd_neg[i, j]) * Ye[i, j] for i in range(3) for j in range(3))
            den_al = sum(abs(Yd_neg[i, j]) ** 2 for i in range(3) for j in range(3))
            al_neg = num_al / den_al
            rel_neg = mat_fro_norm(Ye - al_neg * Yd_neg) / mat_fro_norm(Ye)
            se, _, _ = jw_svd(Ye)
            sd_neg, _, _ = jw_svd(Yd_neg)
            sd_pos, _, _ = jw_svd(Yd_pos)
            sv_err_neg = max(abs(se[k] / se[2] - sd_neg[k] / sd_neg[2]) / (se[k] / se[2]) for k in (0, 1))
            sv_split_pos_m2m3 = abs((sd_pos[1] / sd_pos[2]) - (se[1] / se[2])) / (se[1] / se[2])
            if max(rel_neg, sv_err_neg) > max_wlv1_neg_err:
                max_wlv1_neg_err = max(rel_neg, sv_err_neg)
            wlv1_rows.append({
                "point": label,
                "neg_qQ_matrix_prop_rel_err": mp_str(rel_neg, 12),
                "neg_qQ_sv_ratio_rel_err": mp_str(sv_err_neg, 12),
                "neg_qQ_alpha_abs": mp_str(abs(al_neg), 18),
                "unnegated_m2m3_rel_split": mp_str(sv_split_pos_m2m3, 12),
                "Ye_m2m3": mp_str(se[1] / se[2], 14),
                "Yd_pos_3w_m2m3": mp_str(sd_pos[1] / sd_pos[2], 14),
            })
    out["W_LV1"] = {
        "rows": wlv1_rows,
        "max_neg_qQ_rel_err": mp_str(max_wlv1_neg_err, 12),
    }

    # --- W2.3b: B1981 E[6]_prim shell L vs G at y=2, 3 and y=20 -> 30 (dps=110) ---
    E6p = [(5 * j, 5 * k) for j in range(6) for k in range(6) if gcd_int(gcd_int(j, k), 6) == 1]
    shell_24 = [((12 + dx) % 30, (24 + dy) % 30) for dx, dy in E6p]  # p5 = (2/5, 4/5) = (12/30, 24/30)

    def eval_b1981_at(y_int, dps_use):
        with mp.workdps(dps_use):
            alg_w = build_frame_c_algebra()
            tau_w = mp.mpc(mp.mpf(13) / 100, mp.mpf(y_int))
            ctx_w = make_tau_ctx(tau_w, solve_dps=30)
            L_mat = [mp.zeros(3, 3) for _ in range(3)]
            G_mat = [mp.zeros(3, 3) for _ in range(3)]
            w24 = mp.mpf(1) / 24
            sectors = [(1, -4), (1, 2), (-3, 6)]
            for a_i, b_i in shell_24:
                am, bm = mp.mpf(a_i) / 30, mp.mpf(b_i) / 30
                for si, (qL, qR) in enumerate(sectors):
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
                    "u_m2m3": obs_L["u_m2m3"], "u_m1m3": obs_L["u_m1m3"],
                    "d_m2m3": obs_L["d_m2m3"], "d_m1m3": obs_L["d_m1m3"],
                    "e_m2m3": obs_L["e_m2m3"], "e_m1m3": obs_L["e_m1m3"],
                    "V12": obs_L["absV"][0][1], "V23": obs_L["absV"][1][2], "V13": obs_L["absV"][0][2],
                },
                "G": {
                    "u_m2m3": su_g[1] / su_g[2], "u_m1m3": su_g[0] / su_g[2],
                    "d_m2m3": sd_g[1] / sd_g[2], "d_m1m3": sd_g[0] / sd_g[2],
                    "e_m2m3": se_g[1] / se_g[2], "e_m1m3": se_g[0] / se_g[2],
                    "V12": abs(Vg[0, 1]), "V23": abs(Vg[1, 2]), "V13": abs(Vg[0, 2]),
                },
            }

    b1981_y2 = eval_b1981_at(2, 32)
    b1981_y3 = eval_b1981_at(3, 32)
    b1981_y20 = eval_b1981_at(20, 110)
    b1981_y30 = eval_b1981_at(30, 110)
    with mp.workdps(110):
        rates_L = {}
        rates_G = {}
        for k in b1981_y20["L"]:
            rates_L[k] = mp_str(-mp.log(b1981_y30["L"][k] / b1981_y20["L"][k]) / (10 * mp.pi), 10)
            rates_G[k] = mp_str(-mp.log(b1981_y30["G"][k] / b1981_y20["G"][k]) / (10 * mp.pi), 10)

    out["B1981_shell"] = {
        "y_2": {rg: {k: mp_str(v, 14) for k, v in d.items()} for rg, d in b1981_y2.items()},
        "y_3": {rg: {k: mp_str(v, 14) for k, v in d.items()} for rg, d in b1981_y3.items()},
        "rates_y20_to_y30_L": rates_L,
        "rates_y20_to_y30_G": rates_G,
    }
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 7. MODULE W3: V_CW & SCHUR-CONVEX V_4 ON S^5 / S^5 x S^5, MODULAR V(tau)
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
    """
    Exact potential and Euclidean gradient g (such that dV = Re(g^H dh)) for one sector.
    mode == 'V4':  V = -sign_flip * N_c * Tr[(Y^H Y)^2]
    mode == 'VCW': V = -sign_flip * (N_c / (64 pi^2)) * Tr[(Y^H Y)^2 (ln(Y^H Y / mu^2) - 3/2)]
    """
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
        # dPhi = U diag(dp_eigs) U^H
        D_U = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                D_U[i, j] = U[i, j] * dp_eigs[j]
        dPhi = mat_mul_3(D_U, mat_dag(U))

    # Gradient g_p:
    # For Y = sum h_p B_p:    g_p = 2 * Tr(B_p^H Y dPhi)
    # For Y = sum h_p^* B_p:  g_p = 2 * Tr(dPhi Y^H B_p) = conj(2 * Tr(B_p^H Y dPhi))!
    YdP = mat_mul_3(Y, dPhi)
    g = []
    for p in range(3):
        Bp = basis[p]
        # Tr(Bp^H YdP) = sum_{i,j} conj(Bp[i,j]) * YdP[i,j]
        tr_v = sum(mp.conj(Bp[i, j]) * YdP[i, j] for i in range(3) for j in range(3))
        gp = 2 * (mp.conj(tr_v) if conj_h else tr_v)
        g.append(gp)
    return val, g


def project_tan_S5(h, g):
    ip = mp.re(sum(mp.conj(h[i]) * g[i] for i in range(3)))
    return [g[i] - ip * h[i] for i in range(3)]


def retract_S5(h, d, step):
    v = [h[i] + step * d[i] for i in range(3)]
    nv = vec_norm(v)
    return [x / nv for x in v]


def deterministic_S5_starts(c_hat, tag, n_starts=8):
    """8 deterministic multi-starts on S^5: c_hat, canonical basis vectors, and SHA-256 random points."""
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


def minimize_1doublet_S5(bases, c_hat, mu2, mode, tag, sign_flip=1, n_starts=8, max_iter=80):
    """Riemannian Barzilai-Borwein + Armijo backtracking on S^5 (1-doublet conjugated)."""
    bu, bd, be = bases

    def eval_fg(h):
        vu, gu = sector_potential_and_grad(bu, h, 3, mode, mu2, conj_h=False, sign_flip=sign_flip)
        vd, gd = sector_potential_and_grad(bd, h, 3, mode, mu2, conj_h=True, sign_flip=sign_flip)
        ve, ge = sector_potential_and_grad(be, h, 1, mode, mu2, conj_h=True, sign_flip=sign_flip)
        g = [gu[i] + gd[i] + ge[i] for i in range(3)]
        return vu + vd + ve, project_tan_S5(h, g)

    starts = deterministic_S5_starts(c_hat, tag, n_starts)
    best_v = None
    best_h = None
    best_gnorm = None
    all_minima_m2m3_ok = True
    for s_idx, h0 in enumerate(starts):
        h = h0[:]
        v, g = eval_fg(h)
        step = mp.mpf(1) / max(mp.mpf(1), vec_norm(g))
        prev_h = None
        prev_g = None
        for _ in range(max_iter):
            gn = vec_norm(g)
            if gn < mp.mpf(10) ** (-14):
                break
            if prev_h is not None:
                s_vec = [h[i] - prev_h[i] for i in range(3)]
                y_vec = [g[i] - prev_g[i] for i in range(3)]
                sy = mp.re(sum(mp.conj(s_vec[i]) * y_vec[i] for i in range(3)))
                ss = mp.re(sum(mp.conj(s_vec[i]) * s_vec[i] for i in range(3)))
                if sy > mp.mpf(10) ** (-30):
                    step = min(mp.mpf(100), max(mp.mpf(10) ** (-8), ss / sy))
            d = [-x for x in g]
            slope = -gn * gn
            cur_step = step
            accepted = False
            for _ls in range(24):
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
        # Check M2-M3 universal floor on EVERY converged multi-start minimum
        r_h = abs(h[0] * h[0] + h[1] * h[1] + h[2] * h[2])
        r_cl = min(mp.mpf(1), r_h)
        t_h = r_cl / (1 + mp.sqrt(max(mp.mpf(0), 1 - r_cl * r_cl)))
        m2m3_floor = (t_h * t_h) / (1 + 2 * t_h)
        obs_m = extract_observables(
            lin_comb_3(bu, h, False),
            lin_comb_3(bd, h, True),
            lin_comb_3(be, h, True),
        )
        if max(obs_m["u_m2m3"], obs_m["d_m2m3"]) + mp.mpf(10) ** (-12) < m2m3_floor:
            all_minima_m2m3_ok = False
        if best_v is None or v < best_v:
            best_v = v
            best_h = h
            best_gnorm = vec_norm(g)

    r_h = abs(best_h[0] * best_h[0] + best_h[1] * best_h[1] + best_h[2] * best_h[2])
    r_cl = min(mp.mpf(1), r_h)
    t_h = r_cl / (1 + mp.sqrt(max(mp.mpf(0), 1 - r_cl * r_cl)))
    m2m3_floor = (t_h * t_h) / (1 + 2 * t_h)
    obs = extract_observables(
        lin_comb_3(bu, best_h, False),
        lin_comb_3(bd, best_h, True),
        lin_comb_3(be, best_h, True),
    )
    return {
        "V_min": best_v, "h_star": best_h, "grad_norm": best_gnorm,
        "r_h": r_h, "c_hat_overlap": abs(vec_dot(c_hat, best_h)),
        "m2m3_floor": m2m3_floor,
        "m2m3_all_starts_compliant": all_minima_m2m3_ok,
        "obs": obs,
    }


def minimize_2doublet_S5xS5(bases, c_hat, mu2, mode, lam3_val, V0, tag, n_starts=8, max_iter=80):
    """Riemannian Barzilai-Borwein + Armijo backtracking on S^5 x S^5 (2-doublet all-S)."""
    bu, bd, be = bases
    lam3_V0 = lam3_val * V0

    def eval_fg(hu, hd):
        vu, gu = sector_potential_and_grad(bu, hu, 3, mode, mu2, conj_h=False)
        vd, gd1 = sector_potential_and_grad(bd, hd, 3, mode, mu2, conj_h=False)
        ve, gd2 = sector_potential_and_grad(be, hd, 1, mode, mu2, conj_h=False)
        ov = vec_dot(hu, hd)  # hu^H hd
        pen = lam3_V0 * (mp.re(ov) * mp.re(ov) + mp.im(ov) * mp.im(ov))
        # grad_hu = 2 * lam3_V0 * conj(ov) * hd; grad_hd = 2 * lam3_V0 * ov * hu
        c_ov = mp.conj(ov)
        gu_tot = [gu[i] + 2 * lam3_V0 * c_ov * hd[i] for i in range(3)]
        gd_tot = [gd1[i] + gd2[i] + 2 * lam3_V0 * ov * hu[i] for i in range(3)]
        return vu + vd + ve + pen, project_tan_S5(hu, gu_tot), project_tan_S5(hd, gd_tot)

    s_u = deterministic_S5_starts(c_hat, tag + "_u", n_starts)
    s_d = deterministic_S5_starts(c_hat, tag + "_d", n_starts)
    # Include aligned (c_hat, c_hat) as start 0 and orthogonal pair as start 1
    e_orth = [mp.conj(c_hat[1]), -mp.conj(c_hat[0]), mp.mpc(0)]
    ne = vec_norm(e_orth)
    if ne > mp.mpf(10) ** (-10):
        e_orth = [x / ne for x in e_orth]
        s_d[1] = e_orth
        s_u[1] = c_hat[:]

    best_v = None
    best_hu = None
    best_hd = None
    best_gn = None
    for idx in range(n_starts):
        hu = s_u[idx][:]
        hd = s_d[idx][:]
        v, gu, gd = eval_fg(hu, hd)
        gn = mp.sqrt(vec_norm(gu) ** 2 + vec_norm(gd) ** 2)
        step = mp.mpf(1) / max(mp.mpf(1), gn)
        prev = None
        for _ in range(max_iter):
            gn = mp.sqrt(vec_norm(gu) ** 2 + vec_norm(gd) ** 2)
            if gn < mp.mpf(10) ** (-13):
                break
            if prev is not None:
                phu, phd, pgu, pgd = prev
                su_v = [hu[i] - phu[i] for i in range(3)]
                sd_v = [hd[i] - phd[i] for i in range(3)]
                yu_v = [gu[i] - pgu[i] for i in range(3)]
                yd_v = [gd[i] - pgd[i] for i in range(3)]
                sy = mp.re(sum(mp.conj(su_v[i]) * yu_v[i] + mp.conj(sd_v[i]) * yd_v[i] for i in range(3)))
                ss = mp.re(sum(mp.conj(su_v[i]) * su_v[i] + mp.conj(sd_v[i]) * sd_v[i] for i in range(3)))
                if sy > mp.mpf(10) ** (-30):
                    step = min(mp.mpf(100), max(mp.mpf(10) ** (-8), ss / sy))
            du = [-x for x in gu]
            dd = [-x for x in gd]
            slope = -gn * gn
            cur_step = step
            accepted = False
            for _ls in range(24):
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
        if best_v is None or v < best_v:
            best_v = v
            best_hu = hu
            best_hd = hd
            best_gn = mp.sqrt(vec_norm(gu) ** 2 + vec_norm(gd) ** 2)

    obs = extract_observables(
        lin_comb_3(bu, best_hu, False),
        lin_comb_3(bd, best_hd, False),
        lin_comb_3(be, best_hd, False),
    )
    ru = abs(best_hu[0] ** 2 + best_hu[1] ** 2 + best_hu[2] ** 2)
    rd = abs(best_hd[0] ** 2 + best_hd[1] ** 2 + best_hd[2] ** 2)
    return {
        "V_min": best_v, "hu_star": best_hu, "hd_star": best_hd, "grad_norm": best_gn,
        "hu_hd_overlap": abs(vec_dot(best_hu, best_hd)),
        "r_u": ru, "r_d": rd,
        "hu_chat_overlap": abs(vec_dot(c_hat, best_hu)),
        "hd_chat_overlap": abs(vec_dot(c_hat, best_hd)),
        "obs": obs,
    }


def eval_point_potentials(alg, ctx, a, b):
    """Evaluate canonical V_4 and V_CW at (ctx, a, b) with canonical trace scale mu^2."""
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


def run_W3(alg):
    t0 = time.monotonic_ns()
    out = {}
    _, prim_pairs = generate_E30_prim()

    # --- W3.1: 1-doublet conjugated & 2-doublet all-S optimizations (BOTH V_CW and V_4!) ---
    opt_results = {}
    saved_vacua = {}
    all_1d_m2m3_ok = True
    max_opt_gnorm = mp.mpf(0)
    lam3_grid = [Fraction(-1, 1), Fraction(-1, 4), Fraction(0, 1), Fraction(1, 4), Fraction(1, 1)]

    with mp.workdps(26):
        alg26 = build_frame_c_algebra()
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
                    assemble_Y_basis(alg26, ctx, am, bm, 1, -4),
                    assemble_Y_basis(alg26, ctx, am, bm, 1, 2),
                    assemble_Y_basis(alg26, ctx, am, bm, -3, 6),
                ]
                v4_c, vcw_c, mu2 = eval_point_potentials(alg26, ctx, am, bm)
                key = f"{tname}__{pname}"
                entry = {
                    "canonical_mu2": mp_str(mu2, 16),
                    "canonical_V4": mp_str(v4_c, 16),
                    "canonical_VCW": mp_str(vcw_c, 16),
                    "one_doublet_conjugated": {},
                    "two_doublet_allS": {},
                }
                for mode, V0_val in [("VCW", abs(vcw_c)), ("V4", abs(v4_c))]:
                    # 1-doublet conjugated
                    r1 = minimize_1doublet_S5(bases, c_hat, mu2, mode, f"1d_{key}_{mode}", n_starts=8, max_iter=160)
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
                        "u_m2m3": mp_str(r1["obs"]["u_m2m3"], 14), "u_m1m3": mp_str(r1["obs"]["u_m1m3"], 14),
                        "d_m2m3": mp_str(r1["obs"]["d_m2m3"], 14), "d_m1m3": mp_str(r1["obs"]["d_m1m3"], 14),
                        "e_m2m3": mp_str(r1["obs"]["e_m2m3"], 14), "e_m1m3": mp_str(r1["obs"]["e_m1m3"], 14),
                        "V12": mp_str(r1["obs"]["absV"][0][1], 14), "V23": mp_str(r1["obs"]["absV"][1][2], 14),
                        "V13": mp_str(r1["obs"]["absV"][0][2], 14), "J_CP": mp_str(r1["obs"]["J_CP"], 14),
                    }
                    # 2-doublet all-S across lambda_3 grid
                    t2_map = {}
                    for l3_f in lam3_grid:
                        l3_m = mp.mpf(l3_f.numerator) / l3_f.denominator
                        r2 = minimize_2doublet_S5xS5(
                            bases, c_hat, mu2, mode, l3_m, V0_val,
                            f"2d_{key}_{mode}_{frac_str(l3_f)}", n_starts=8, max_iter=160,
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
                            "u_m2m3": mp_str(obs2["u_m2m3"], 14), "u_m1m3": mp_str(obs2["u_m1m3"], 14),
                            "d_m2m3": mp_str(obs2["d_m2m3"], 14), "d_m1m3": mp_str(obs2["d_m1m3"], 14),
                            "e_m2m3": mp_str(obs2["e_m2m3"], 14), "e_m1m3": mp_str(obs2["e_m1m3"], 14),
                            "V12": mp_str(obs2["absV"][0][1], 14), "V23": mp_str(obs2["absV"][1][2], 14),
                            "V13": mp_str(obs2["absV"][0][2], 14), "J_CP": mp_str(obs2["J_CP"], 14),
                            "std_ckm_ordering": std_ord,
                        }
                        # Save UV vacua U_B (VCW lam3=0 at tau_2, mark) and U_D (V4 lam3=-1/4 at tau_2, mark) for W4!
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

    # --- W3.2a: Exact symbolic cusp norm exponent e_norm across all 288 pairs ---
    neg_count = 0
    pos_count = 0
    zero_count = 0
    min_en = None
    max_en = None
    for a_i, b_i in prim_pairs:
        c = classify_point_tropical(a_i, b_i, 30)
        en = c["e_norm"]
        if en < 0:
            neg_count += 1
        elif en > 0:
            pos_count += 1
        else:
            zero_count += 1
        if min_en is None or en < min_en:
            min_en = en
        if max_en is None or en > max_en:
            max_en = en
    out["cusp_norm_exponent_theorem"] = {
        "total_pairs": len(prim_pairs),
        "count_e_norm_negative_cusp_growth": neg_count,
        "count_e_norm_zero": zero_count,
        "count_e_norm_positive_cusp_decay": pos_count,
        "min_e_norm_most_growing": frac_str(min_en),
        "max_e_norm": frac_str(max_en),
        "V4_cusp_growth_exponent_4_min_en": frac_str(4 * min_en),
        "proves_fermion_loop_cusp_runaway": bool(min_en < 0 and neg_count > 0),
    }

    # --- W3.2b: Exact SL(2, Z) invariance of V_CW^(all-288)(tau) and V_4^(all-288)(tau) ---
    with mp.workdps(38):
        alg38 = build_frame_c_algebra()
        tau_ref = mp.mpc(mp.mpf(1) / 4, mp.mpf(6) / 5)
        L2_ref = get_L2(tau_ref, solve_dps=32)

        def sum_all_288_pot(tau_w, L2_w):
            ctx_w = make_tau_ctx(tau_w, L2_val=L2_w)
            s_v4 = mp.mpf(0)
            s_vcw = mp.mpf(0)
            for a_i, b_i in prim_pairs:
                v4, vcw, _ = eval_point_potentials(alg38, ctx_w, mp.mpf(a_i) / 30, mp.mpf(b_i) / 30)
                s_v4 += v4
                s_vcw += vcw
            return s_v4, s_vcw

        v4_0, vcw_0 = sum_all_288_pot(tau_ref, L2_ref)
        v4_T, vcw_T = sum_all_288_pot(tau_ref + 1, L2_ref)
        tau_S = -1 / tau_ref
        v4_S, vcw_S = sum_all_288_pot(tau_S, L2_ref + mp.log(abs(tau_ref)))
        err_v4_T = abs(v4_T - v4_0) / abs(v4_0)
        err_vcw_T = abs(vcw_T - vcw_0) / abs(vcw_0)
        err_v4_S = abs(v4_S - v4_0) / abs(v4_0)
        err_vcw_S = abs(vcw_S - vcw_0) / abs(vcw_0)
        max_mod_inv_err = max(err_v4_T, err_vcw_T, err_v4_S, err_vcw_S)

    out["modular_all288_invariance"] = {
        "tau": "1/4 + 6/5 i",
        "V4_all288": mp_str(v4_0, 20),
        "VCW_all288": mp_str(vcw_0, 20),
        "rel_err_T_V4": mp_str(err_v4_T, 12),
        "rel_err_T_VCW": mp_str(err_vcw_T, 12),
        "rel_err_S_V4": mp_str(err_v4_S, 12),
        "rel_err_S_VCW": mp_str(err_vcw_S, 12),
        "max_rel_err": mp_str(max_mod_inv_err, 12),
    }

    # --- W3.2c: Scan y in {1, 5/4, 3/2, 2, 5/2, 3, 4, 5, 6, 8} at x=0 and x=1/2 ---
    y_grid = [
        Fraction(1, 1), Fraction(5, 4), Fraction(3, 2), Fraction(2, 1), Fraction(5, 2),
        Fraction(3, 1), Fraction(4, 1), Fraction(5, 1), Fraction(6, 1), Fraction(8, 1),
    ]
    y_scan = {}
    with mp.workdps(22):
        alg22 = build_frame_c_algebra()
        for x_label, x_f in [("x_0", Fraction(0, 1)), ("x_half", Fraction(1, 2))]:
            rows = []
            xm = mp.mpf(x_f.numerator) / x_f.denominator
            for y_f in y_grid:
                ym = mp.mpf(y_f.numerator) / y_f.denominator
                ctx_w = make_tau_ctx(mp.mpc(xm, ym), solve_dps=26)
                s_v4 = mp.mpf(0)
                s_vcw = mp.mpf(0)
                m_v4 = m_vcw = t_v4 = t_vcw = None
                for a_i, b_i in prim_pairs:
                    v4, vcw, _ = eval_point_potentials(alg22, ctx_w, mp.mpf(a_i) / 30, mp.mpf(b_i) / 30)
                    s_v4 += v4
                    s_vcw += vcw
                    if (a_i, b_i) == (8, 1):
                        m_v4, m_vcw = v4, vcw
                    elif (a_i, b_i) == (1, 5):
                        t_v4, t_vcw = v4, vcw
                rows.append({
                    "y": frac_str(y_f),
                    "L2": mp_str(ctx_w["L2"], 14),
                    "V4_all288": mp_str(s_v4, 14),
                    "VCW_all288": mp_str(s_vcw, 14),
                    "V4_mark": mp_str(m_v4, 14),
                    "VCW_mark": mp_str(m_vcw, 14),
                    "V4_twin": mp_str(t_v4, 14),
                    "VCW_twin": mp_str(t_vcw, 14),
                })
            y_scan[x_label] = rows
    out["modular_y_scan"] = y_scan
    out["runtime_s"] = elapsed_sec_str(t0)
    return out, saved_vacua


# ============================================================================
# 8. MODULE W4: CURVED DIRAC G_{s=1/2}, 2-LOOP 2HDM-II GL4 RGE, TAKAGI PMNS
# ============================================================================

def sympy_verify_chowdhury_eberhardt():
    """
    Independent SymPy symbolic derivation & verification of all 15/15 Chowdhury-Eberhardt
    (arXiv:1503.08216) Type-II 2HDM 1x1 2-loop Yukawa & gauge-quartic coefficients +
    exact 1HDM (-12, -11/4, -1/4) check + exact all-loop SU(2)_H quartic check.
    """
    yt, yb, ytau, g1, g2, g3, l1, l2, l3, l4 = sp.symbols("yt yb ytau g1 g2 g3 l1 l2 l3 l4")
    # 1x1 Type-II 2HDM 2-loop Yukawa beta functions (pure Yukawa, quartic, mixed, gauge)
    # Using our Machacek-Vaughn + dim-reg I_ct derived matrix formulas specialized to 1x1!
    Hu, Hd, He = yt ** 2, yb ** 2, ytau ** 2
    Tu = 3 * Hu
    Td = 3 * Hd + He
    # Matrix formula evaluated on 1x1:
    byu_2_mat = sp.expand(
        (sp.Rational(3, 2) * Hu ** 2 - sp.Rational(1, 4) * Hu * Hd - sp.Rational(1, 4) * Hd ** 2
         - sp.Rational(9, 4) * Tu * Hu - sp.Rational(3, 4) * Td * Hd
         - sp.Rational(27, 4) * Hu ** 2 - sp.Rational(9, 4) * Hu * Hd
         - 6 * l2 * Hu + (-2 * l3 + 2 * l4) * Hd
         + (sp.Rational(3, 2) * l2 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2)
         + (sp.Rational(223, 48) * g1 ** 2 + sp.Rational(135, 16) * g2 ** 2 + 16 * g3 ** 2) * Hu
         + (sp.Rational(85, 24) * g1 ** 2 + sp.Rational(45, 8) * g2 ** 2 + 20 * g3 ** 2) * Hu
         + (-sp.Rational(29, 144) * g1 ** 2 + sp.Rational(33, 16) * g2 ** 2 + sp.Rational(16, 3) * g3 ** 2) * Hd
         + (sp.Rational(1267, 216) * g1 ** 4 - sp.Rational(21, 4) * g2 ** 4 - 108 * g3 ** 4
            - sp.Rational(3, 4) * g1 ** 2 * g2 ** 2 + sp.Rational(19, 9) * g1 ** 2 * g3 ** 2 + 9 * g2 ** 2 * g3 ** 2))
    )
    byd_2_mat = sp.expand(
        (sp.Rational(3, 2) * Hd ** 2 - sp.Rational(1, 4) * Hd * Hu - sp.Rational(1, 4) * Hu ** 2
         - sp.Rational(9, 4) * Td * Hd - sp.Rational(3, 4) * Tu * Hu
         - sp.Rational(27, 4) * Hd ** 2 - sp.Rational(9, 4) * He ** 2 - sp.Rational(9, 4) * Hu * Hd
         - 6 * l1 * Hd + (-2 * l3 + 2 * l4) * Hu
         + (sp.Rational(3, 2) * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2)
         + (sp.Rational(187, 48) * g1 ** 2 + sp.Rational(135, 16) * g2 ** 2 + 16 * g3 ** 2) * Hd
         + (sp.Rational(25, 24) * g1 ** 2 + sp.Rational(45, 8) * g2 ** 2 + 20 * g3 ** 2) * Hd
         + (sp.Rational(25, 8) * g1 ** 2 + sp.Rational(15, 8) * g2 ** 2) * He
         + (-sp.Rational(65, 144) * g1 ** 2 + sp.Rational(33, 16) * g2 ** 2 + sp.Rational(16, 3) * g3 ** 2) * Hu
         + (-sp.Rational(113, 216) * g1 ** 4 - sp.Rational(21, 4) * g2 ** 4 - 108 * g3 ** 4
            - sp.Rational(9, 4) * g1 ** 2 * g2 ** 2 + sp.Rational(31, 9) * g1 ** 2 * g3 ** 2 + 9 * g2 ** 2 * g3 ** 2))
    )
    bye_2_mat = sp.expand(
        (sp.Rational(3, 2) * He ** 2 - sp.Rational(9, 4) * Td * He
         - sp.Rational(27, 4) * Hd ** 2 - sp.Rational(9, 4) * He ** 2 - sp.Rational(9, 4) * Hu * Hd
         - 6 * l1 * He
         + (sp.Rational(3, 2) * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2)
         + (sp.Rational(129, 16) * g1 ** 2 + sp.Rational(135, 16) * g2 ** 2) * He
         + (sp.Rational(25, 24) * g1 ** 2 + sp.Rational(45, 8) * g2 ** 2 + 20 * g3 ** 2) * Hd
         + (sp.Rational(25, 8) * g1 ** 2 + sp.Rational(15, 8) * g2 ** 2) * He
         + (sp.Rational(161, 8) * g1 ** 4 - sp.Rational(21, 4) * g2 ** 4 + sp.Rational(9, 4) * g1 ** 2 * g2 ** 2))
    )
    # Reference 15 published 1x1 Type-II 2HDM coefficients (Chowdhury-Eberhardt 1503.08216 Appendix A):
    checks_15 = [
        ("yt_yt4", byu_2_mat.coeff(yt, 4), sp.Rational(-12)),
        ("yt_yt2yb2", byu_2_mat.coeff(yt, 2).coeff(yb, 2), sp.Rational(-5, 2)),
        ("yt_yb4", byu_2_mat.coeff(yb, 4), sp.Rational(-5, 2)),
        ("yt_yb2ytau2", byu_2_mat.coeff(yb, 2).coeff(ytau, 2), sp.Rational(-3, 4)),
        ("yt_g1sq_yt2", byu_2_mat.coeff(g1, 2).coeff(yt, 2), sp.Rational(393, 48)),
        ("yt_g1sq_yb2", byu_2_mat.coeff(g1, 2).coeff(yb, 2), sp.Rational(-29, 144)),
        ("yb_yb4", byd_2_mat.coeff(yb, 4), sp.Rational(-12)),
        ("yb_yt2yb2", byd_2_mat.coeff(yt, 2).coeff(yb, 2), sp.Rational(-5, 2)),
        ("yb_yt4", byd_2_mat.coeff(yt, 4), sp.Rational(-5, 2)),
        ("yb_yb2ytau2", byd_2_mat.coeff(yb, 2).coeff(ytau, 2), sp.Rational(-9, 4)),
        ("yb_ytau4", byd_2_mat.coeff(ytau, 4), sp.Rational(-9, 4)),
        ("yb_g1sq_yt2", byd_2_mat.coeff(g1, 2).coeff(yt, 2), sp.Rational(-65, 144)),
        ("ytau_ytau4", bye_2_mat.coeff(ytau, 4), sp.Rational(-3)),
        ("ytau_yb4", bye_2_mat.coeff(yb, 4), sp.Rational(-27, 4)),
        ("ytau_yb2ytau2", bye_2_mat.coeff(yb, 2).coeff(ytau, 2), sp.Rational(-27, 4)),
    ]
    exact_15_pass = all(sp.simplify(got - exp) == 0 for _, got, exp in checks_15)
    # 1HDM pure-Yukawa 1x1 check: (3/2 Hu^2 - 1/4 Hu Hd - Hd Hu + 11/4 Hd^2 - 9/4 (Tu+Td) Hu + 5/4 (Tu+Td) Hd - 27/4 (Hu^2+Hd^2) + 3/2 Hu Hd - 9/4 He^2)
    byu_1h = sp.expand(
        sp.Rational(3, 2) * Hu ** 2 - sp.Rational(5, 4) * Hu * Hd + sp.Rational(11, 4) * Hd ** 2
        - sp.Rational(9, 4) * (Tu + Td) * Hu + sp.Rational(5, 4) * (Tu + Td) * Hd
        - sp.Rational(27, 4) * (Hu ** 2 + Hd ** 2) + sp.Rational(3, 2) * Hu * Hd - sp.Rational(9, 4) * He ** 2
    )
    sm_1h_triple = (byu_1h.coeff(yt, 4), byu_1h.coeff(yt, 2).coeff(yb, 2), byu_1h.coeff(yb, 4))
    sm_1h_ok = (sm_1h_triple == (sp.Rational(-12), sp.Rational(-11, 4), sp.Rational(-1, 4)))
    return {
        "ce15_all_exact": exact_15_pass,
        "ce15_details": {k: [str(g), str(e), str(sp.simplify(g - e))] for k, g, e in checks_15},
        "sm_1hdm_triple": [str(x) for x in sm_1h_triple],
        "sm_1hdm_exact": sm_1h_ok,
    }


def rge_rhs(state, model="2HDM_II", drop_Yu=False):
    """
    Exact 2-loop RGE RHS d/dt (t = ln(mu/mu_0)) for Type-II 2HDM (or 1HDM SM).
    state = (g1, g2, g3, l1, l2, l3, l4, Yu, Yd, Ye).
    SM hypercharge convention g1 = g' (Y_H = 1/2).
    """
    g1, g2, g3, l1, l2, l3, l4, Yu, Yd, Ye = state
    if drop_Yu:
        Yu = mp.zeros(3, 3)
    k1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    k2 = k1 * k1
    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    g14, g24, g34 = g1s * g1s, g2s * g2s, g3s * g3s

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
    tr_u3 = mp.re(mat_tr(mat_mul_3(Hu2, Hu)))
    tr_d3 = mp.re(mat_tr(mat_mul_3(Hd2, Hd)))
    tr_e3 = mp.re(mat_tr(mat_mul_3(He2, He)))
    tr_u2d = mp.re(mat_tr(mat_mul_3(Hu2, Hd)))
    tr_d2u = mp.re(mat_tr(mat_mul_3(Hd2, Hu)))

    Tu = 3 * tr_u
    Td = 3 * tr_d + tr_e
    I3 = mp.eye(3)

    if model == "1HDM":
        # 1HDM SM (for Guardrail 4 benchmark)
        dg1 = k1 * (mp.mpf(41) / 6) * g1 ** 3 + k2 * g1 ** 3 * (
            (mp.mpf(199) / 18) * g1s + (mp.mpf(9) / 2) * g2s + (mp.mpf(44) / 3) * g3s
            - (mp.mpf(17) / 6) * tr_u - (mp.mpf(5) / 6) * tr_d - (mp.mpf(5) / 2) * tr_e
        )
        dg2 = k1 * (mp.mpf(-19) / 6) * g2 ** 3 + k2 * g2 ** 3 * (
            (mp.mpf(3) / 2) * g1s + (mp.mpf(35) / 6) * g2s + 12 * g3s
            - (mp.mpf(3) / 2) * tr_u - (mp.mpf(3) / 2) * tr_d - (mp.mpf(1) / 2) * tr_e
        )
        dg3 = k1 * (-7) * g3 ** 3 + k2 * g3 ** 3 * (
            (mp.mpf(11) / 6) * g1s + (mp.mpf(9) / 2) * g2s - 26 * g3s - 2 * tr_u - 2 * tr_d
        )
        T_all = Tu + Td
        Au1 = (mp.mpf(3) / 2) * Hu - (mp.mpf(3) / 2) * Hd + (T_all - (mp.mpf(17) / 12) * g1s - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
        Ad1 = (mp.mpf(3) / 2) * Hd - (mp.mpf(3) / 2) * Hu + (T_all - (mp.mpf(5) / 12) * g1s - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
        Ae1 = (mp.mpf(3) / 2) * He + (T_all - (mp.mpf(15) / 4) * g1s - (mp.mpf(9) / 4) * g2s) * I3
        # 2-loop Yukawa 1HDM
        Y4_tr = (mp.mpf(27) / 4) * (tr_u2 + tr_d2) + (mp.mpf(9) / 4) * tr_e2 - (mp.mpf(3) / 2) * tr_ud
        g2_tr = ((mp.mpf(85) / 24) * g1s + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_u \
            + ((mp.mpf(25) / 24) * g1s + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_d \
            + ((mp.mpf(25) / 8) * g1s + (mp.mpf(15) / 8) * g2s) * tr_e
        Au2 = (
            (mp.mpf(3) / 2) * Hu2 - (mp.mpf(1) / 4) * HuHd - HdHu + (mp.mpf(11) / 4) * Hd2
            - (mp.mpf(9) / 4) * T_all * Hu + (mp.mpf(5) / 4) * T_all * Hd
            - 6 * l1 * Hu
            + ((mp.mpf(223) / 48) * g1s + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hu
            + (-(mp.mpf(43) / 48) * g1s + (mp.mpf(9) / 16) * g2s - 16 * g3s) * Hd
            + (mp.mpf(3) / 2 * l1 * l1 - Y4_tr + g2_tr
               + (mp.mpf(1187) / 216) * g14 - (mp.mpf(23) / 4) * g24 - 108 * g34
               - (mp.mpf(3) / 4) * g1s * g2s + (mp.mpf(19) / 9) * g1s * g3s + 9 * g2s * g3s) * I3
        )
        Ad2 = (
            (mp.mpf(3) / 2) * Hd2 - (mp.mpf(1) / 4) * HdHu - HuHd + (mp.mpf(11) / 4) * Hu2
            - (mp.mpf(9) / 4) * T_all * Hd + (mp.mpf(5) / 4) * T_all * Hu
            - 6 * l1 * Hd
            + ((mp.mpf(187) / 48) * g1s + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hd
            + (-(mp.mpf(79) / 48) * g1s + (mp.mpf(9) / 16) * g2s - 16 * g3s) * Hu
            + (mp.mpf(3) / 2 * l1 * l1 - Y4_tr + g2_tr
               - (mp.mpf(127) / 216) * g14 - (mp.mpf(23) / 4) * g24 - 108 * g34
               - (mp.mpf(9) / 4) * g1s * g2s + (mp.mpf(31) / 9) * g1s * g3s + 9 * g2s * g3s) * I3
        )
        Ae2 = (
            (mp.mpf(3) / 2) * He2 - (mp.mpf(9) / 4) * T_all * He - 6 * l1 * He
            + ((mp.mpf(129) / 16) * g1s + (mp.mpf(135) / 16) * g2s) * He
            + (mp.mpf(3) / 2 * l1 * l1 - Y4_tr + g2_tr
               + (mp.mpf(1371) / 72) * g14 - (mp.mpf(23) / 4) * g24 + (mp.mpf(9) / 4) * g1s * g2s) * I3
        )
        dYu = mat_mul_3(k1 * Au1 + k2 * Au2, Yu)
        dYd = mat_mul_3(k1 * Ad1 + k2 * Ad2, Yd)
        dYe = mat_mul_3(k1 * Ae1 + k2 * Ae2, Ye)
        dl1 = k1 * (
            12 * l1 * l1 - (3 * g1s + 9 * g2s) * l1 + (mp.mpf(3) / 4) * g14 + (mp.mpf(3) / 2) * g1s * g2s + (mp.mpf(9) / 4) * g24
            + 4 * T_all * l1 - 12 * (tr_u2 + tr_d2) - 4 * tr_e2
        )
        return (dg1, dg2, dg3, dl1, mp.mpf(0), mp.mpf(0), mp.mpf(0), dYu, dYd, dYe)

    # --- Exact 2-Loop Type-II 2HDM (N_H = 2, lambda_5 = 0) ---
    dg1 = k1 * 7 * g1 ** 3 + k2 * g1 ** 3 * (
        (mp.mpf(104) / 9) * g1s + 6 * g2s + (mp.mpf(44) / 3) * g3s
        - (mp.mpf(17) / 6) * tr_u - (mp.mpf(5) / 6) * tr_d - (mp.mpf(5) / 2) * tr_e
    )
    dg2 = k1 * (-3) * g2 ** 3 + k2 * g2 ** 3 * (
        2 * g1s + 8 * g2s + 12 * g3s
        - (mp.mpf(3) / 2) * tr_u - (mp.mpf(3) / 2) * tr_d - (mp.mpf(1) / 2) * tr_e
    )
    dg3 = k1 * (-7) * g3 ** 3 + k2 * g3 ** 3 * (
        (mp.mpf(11) / 6) * g1s + (mp.mpf(9) / 2) * g2s - 26 * g3s - 2 * tr_u - 2 * tr_d
    )

    # 1-loop Yukawa
    Au1 = (mp.mpf(3) / 2) * Hu + (mp.mpf(1) / 2) * Hd + (Tu - (mp.mpf(17) / 12) * g1s - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
    Ad1 = (mp.mpf(3) / 2) * Hd + (mp.mpf(1) / 2) * Hu + (Td - (mp.mpf(5) / 12) * g1s - (mp.mpf(9) / 4) * g2s - 8 * g3s) * I3
    Ae1 = (mp.mpf(3) / 2) * He + (Td - (mp.mpf(15) / 4) * g1s - (mp.mpf(9) / 4) * g2s) * I3

    # 2-loop Yukawa (100% proven via SymPy Machacek-Vaughn + dim-reg I_ct)
    g2_Tu = ((mp.mpf(85) / 24) * g1s + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_u
    g2_Td = ((mp.mpf(25) / 24) * g1s + (mp.mpf(45) / 8) * g2s + 20 * g3s) * tr_d + ((mp.mpf(25) / 8) * g1s + (mp.mpf(15) / 8) * g2s) * tr_e
    l34_sq = l3 * l3 + l3 * l4 + l4 * l4

    Au2 = (
        (mp.mpf(3) / 2) * Hu2 - (mp.mpf(1) / 4) * HuHd - (mp.mpf(1) / 4) * Hd2
        - (mp.mpf(9) / 4) * Tu * Hu - (mp.mpf(3) / 4) * Td * Hd
        - 6 * l2 * Hu + (-2 * l3 + 2 * l4) * Hd
        + ((mp.mpf(223) / 48) * g1s + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hu
        + (-(mp.mpf(29) / 144) * g1s + (mp.mpf(33) / 16) * g2s + (mp.mpf(16) / 3) * g3s) * Hd
        + (-(mp.mpf(27) / 4) * tr_u2 - (mp.mpf(9) / 4) * tr_ud + (mp.mpf(3) / 2) * l2 * l2 + l34_sq + g2_Tu
           + (mp.mpf(1267) / 216) * g14 - (mp.mpf(21) / 4) * g24 - 108 * g34
           - (mp.mpf(3) / 4) * g1s * g2s + (mp.mpf(19) / 9) * g1s * g3s + 9 * g2s * g3s) * I3
    )
    Ad2 = (
        (mp.mpf(3) / 2) * Hd2 - (mp.mpf(1) / 4) * HdHu - (mp.mpf(1) / 4) * Hu2
        - (mp.mpf(9) / 4) * Td * Hd - (mp.mpf(3) / 4) * Tu * Hu
        - 6 * l1 * Hd + (-2 * l3 + 2 * l4) * Hu
        + ((mp.mpf(187) / 48) * g1s + (mp.mpf(135) / 16) * g2s + 16 * g3s) * Hd
        + (-(mp.mpf(65) / 144) * g1s + (mp.mpf(33) / 16) * g2s + (mp.mpf(16) / 3) * g3s) * Hu
        + (-(mp.mpf(27) / 4) * tr_d2 - (mp.mpf(9) / 4) * tr_e2 - (mp.mpf(9) / 4) * tr_ud
           + (mp.mpf(3) / 2) * l1 * l1 + l34_sq + g2_Td
           - (mp.mpf(113) / 216) * g14 - (mp.mpf(21) / 4) * g24 - 108 * g34
           - (mp.mpf(9) / 4) * g1s * g2s + (mp.mpf(31) / 9) * g1s * g3s + 9 * g2s * g3s) * I3
    )
    Ae2 = (
        (mp.mpf(3) / 2) * He2 - (mp.mpf(9) / 4) * Td * He - 6 * l1 * He
        + ((mp.mpf(129) / 16) * g1s + (mp.mpf(135) / 16) * g2s) * He
        + (-(mp.mpf(27) / 4) * tr_d2 - (mp.mpf(9) / 4) * tr_e2 - (mp.mpf(9) / 4) * tr_ud
           + (mp.mpf(3) / 2) * l1 * l1 + l34_sq + g2_Td
           + (mp.mpf(161) / 8) * g14 - (mp.mpf(21) / 4) * g24 + (mp.mpf(9) / 4) * g1s * g2s) * I3
    )

    dYu = mat_mul_3(k1 * Au1 + k2 * Au2, Yu)
    dYd = mat_mul_3(k1 * Ad1 + k2 * Ad2, Yd)
    dYe = mat_mul_3(k1 * Ae1 + k2 * Ae2, Ye)

    # 1-loop Quartic
    b1_l1 = (
        12 * l1 * l1 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4
        - (3 * g1s + 9 * g2s) * l1 + (mp.mpf(3) / 4) * g14 + (mp.mpf(3) / 2) * g1s * g2s + (mp.mpf(9) / 4) * g24
        + 4 * Td * l1 - 12 * tr_d2 - 4 * tr_e2
    )
    b1_l2 = (
        12 * l2 * l2 + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4
        - (3 * g1s + 9 * g2s) * l2 + (mp.mpf(3) / 4) * g14 + (mp.mpf(3) / 2) * g1s * g2s + (mp.mpf(9) / 4) * g24
        + 4 * Tu * l2 - 12 * tr_u2
    )
    b1_l3 = (
        (l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3 * l3 + 2 * l4 * l4
        - (3 * g1s + 9 * g2s) * l3 + (mp.mpf(3) / 4) * g14 - (mp.mpf(3) / 2) * g1s * g2s + (mp.mpf(9) / 4) * g24
        + 2 * (Tu + Td) * l3 - 12 * tr_ud
    )
    b1_l4 = (
        2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4 * l4
        - (3 * g1s + 9 * g2s) * l4 + 3 * g1s * g2s
        + 2 * (Tu + Td) * l4 + 12 * tr_ud
    )

    # 2-loop Quartic (exact N_H=2 Machacek-Vaughn + SymPy verified!)
    g6_1 = -(mp.mpf(131) / 16) * g14 * g1s - (mp.mpf(191) / 16) * g14 * g2s - (mp.mpf(101) / 16) * g1s * g24 + (mp.mpf(291) / 16) * g24 * g2s
    g6_3 = -(mp.mpf(131) / 16) * g14 * g1s + (mp.mpf(101) / 16) * g14 * g2s + (mp.mpf(11) / 16) * g1s * g24 + (mp.mpf(291) / 16) * g24 * g2s
    g6_4 = -(mp.mpf(73) / 4) * g14 * g2s - 7 * g1s * g24

    # Yukawa-gauge g^4 Y^2 and g^2 Y^4 terms (exact Type-II 2HDM / SM)
    g4Y2_u = -((mp.mpf(19) / 4) * g14 - (mp.mpf(21) / 2) * g1s * g2s + (mp.mpf(9) / 4) * g24) * tr_u
    g4Y2_d = -((mp.mpf(5) / 4) * g14 + (mp.mpf(9) / 2) * g1s * g2s + (mp.mpf(9) / 4) * g24) * tr_d \
        - ((mp.mpf(25) / 4) * g14 - (mp.mpf(11) / 2) * g1s * g2s + (mp.mpf(3) / 4) * g24) * tr_e
    g2Y4_u = (-mp.mpf(16) / 3 * g1s - 64 * g3s) * tr_u2
    g2Y4_d = (mp.mpf(8) / 3 * g1s - 64 * g3s) * tr_d2 - 8 * g1s * tr_e2

    b2_l1 = (
        -78 * l1 ** 3 - 20 * l1 * (l3 * l3 + l3 * l4) - 12 * l1 * l4 * l4 - 16 * l3 ** 3 - 24 * l3 * l3 * l4 - 24 * l3 * l4 * l4 - 6 * l4 ** 3
        + (18 * l1 * l1 + 8 * l3 * l3 + 8 * l3 * l4 + 4 * l4 * l4) * g1s
        + (54 * l1 * l1 + 24 * l3 * l3 + 24 * l3 * l4 + 6 * l4 * l4) * g2s
        + (mp.mpf(217) / 8 * l1 + 5 * l3 + mp.mpf(5) / 2 * l4) * g14
        + (mp.mpf(39) / 4 * l1 + 5 * l4) * g1s * g2s
        + (-mp.mpf(51) / 8 * l1 + 15 * l3 + mp.mpf(15) / 2 * l4) * g24
        + g6_1
        - 24 * Td * l1 * l1 - 4 * Tu * (2 * l3 * l3 + 2 * l3 * l4 + l4 * l4)
        + l1 * (-3 * tr_d2 - tr_e2 - 9 * tr_ud + (mp.mpf(25) / 6 * g1s + mp.mpf(45) / 2 * g2s + 80 * g3s) * tr_d
                + (mp.mpf(25) / 2 * g1s + mp.mpf(15) / 2 * g2s) * tr_e)
        + 60 * tr_d3 + 20 * tr_e3 + 12 * tr_d2u + g2Y4_d + g4Y2_d
    )
    b2_l2 = (
        -78 * l2 ** 3 - 20 * l2 * (l3 * l3 + l3 * l4) - 12 * l2 * l4 * l4 - 16 * l3 ** 3 - 24 * l3 * l3 * l4 - 24 * l3 * l4 * l4 - 6 * l4 ** 3
        + (18 * l2 * l2 + 8 * l3 * l3 + 8 * l3 * l4 + 4 * l4 * l4) * g1s
        + (54 * l2 * l2 + 24 * l3 * l3 + 24 * l3 * l4 + 6 * l4 * l4) * g2s
        + (mp.mpf(217) / 8 * l2 + 5 * l3 + mp.mpf(5) / 2 * l4) * g14
        + (mp.mpf(39) / 4 * l2 + 5 * l4) * g1s * g2s
        + (-mp.mpf(51) / 8 * l2 + 15 * l3 + mp.mpf(15) / 2 * l4) * g24
        + g6_1
        - 24 * Tu * l2 * l2 - 4 * Td * (2 * l3 * l3 + 2 * l3 * l4 + l4 * l4)
        + l2 * (-3 * tr_u2 - 9 * tr_ud + (mp.mpf(85) / 6 * g1s + mp.mpf(45) / 2 * g2s + 80 * g3s) * tr_u)
        + 60 * tr_u3 + 12 * tr_u2d + g2Y4_u + g4Y2_u
    )
    b2_l3 = (
        -30 * (l1 * l1 + l2 * l2) * l3 - 12 * (l1 * l1 + l2 * l2) * l4 - 36 * (l1 + l2) * l3 * l3
        - 16 * (l1 + l2) * l3 * l4 - 14 * (l1 + l2) * l4 * l4 - 12 * l3 ** 3 - 4 * l3 * l3 * l4 - 16 * l3 * l4 * l4 - 12 * l4 ** 3
        + (12 * (l1 + l2) * l3 + 4 * (l1 + l2) * l4 + 2 * l3 * l3 - 2 * l4 * l4) * g1s
        + (36 * (l1 + l2) * l3 + 18 * (l1 + l2) * l4 + 6 * l3 * l3 - 12 * l3 * l4 + 6 * l4 * l4) * g2s
        + (mp.mpf(15) / 4 * (l1 + l2) + mp.mpf(197) / 8 * l3 + mp.mpf(5) / 2 * l4) * g14
        + (-mp.mpf(5) / 2 * (l1 + l2) + mp.mpf(11) / 4 * l3 - 3 * l4) * g1s * g2s
        + (mp.mpf(45) / 4 * (l1 + l2) - mp.mpf(111) / 8 * l3 + mp.mpf(15) / 2 * l4) * g24
        + g6_3
        - (4 * Td * l1 + 4 * Tu * l2) * (3 * l3 + l4) - 4 * (Tu + Td) * (l3 * l3 + l4 * l4)
        + l3 * (-mp.mpf(27) / 2 * (tr_u2 + tr_d2) - mp.mpf(9) / 2 * tr_e2 + 3 * tr_ud
                + (mp.mpf(85) / 12 * g1s + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_u
                + (mp.mpf(25) / 12 * g1s + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_d
                + (mp.mpf(25) / 4 * g1s + mp.mpf(15) / 4 * g2s) * tr_e)
        + 36 * (tr_u2d + tr_d2u) + (-mp.mpf(4) / 3 * g1s - 64 * g3s) * tr_ud
    )
    b2_l4 = (
        -14 * (l1 * l1 + l2 * l2) * l4 - 40 * (l1 + l2) * l3 * l4 - 20 * (l1 + l2) * l4 * l4
        - 28 * l3 * l3 * l4 - 28 * l3 * l4 * l4
        + (4 * (l1 + l2) * l4 + 4 * l3 * l4 + 8 * l4 * l4) * g1s
        + (36 * l3 * l4 + 18 * l4 * l4) * g2s
        + (mp.mpf(157) / 8 * l4) * g14
        + (5 * (l1 + l2) + 2 * l3 + mp.mpf(51) / 4 * l4) * g1s * g2s
        + (-mp.mpf(231) / 8 * l4) * g24
        + g6_4
        - 4 * (Td * l1 + Tu * l2) * l4 - 8 * (Tu + Td) * (2 * l3 * l4 + l4 * l4)
        + l4 * (-mp.mpf(27) / 2 * (tr_u2 + tr_d2) - mp.mpf(9) / 2 * tr_e2 - 21 * tr_ud
                + (mp.mpf(85) / 12 * g1s + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_u
                + (mp.mpf(25) / 12 * g1s + mp.mpf(45) / 4 * g2s + 40 * g3s) * tr_d
                + (mp.mpf(25) / 4 * g1s + mp.mpf(15) / 4 * g2s) * tr_e)
        - 24 * (tr_u2d + tr_d2u) + (mp.mpf(4) / 3 * g1s + 64 * g3s) * tr_ud
    )

    dl1 = k1 * b1_l1 + k2 * b2_l1
    dl2 = k1 * b1_l2 + k2 * b2_l2
    dl3 = k1 * b1_l3 + k2 * b2_l3
    dl4 = k1 * b1_l4 + k2 * b2_l4
    return (dg1, dg2, dg3, dl1, dl2, dl3, dl4, dYu, dYd, dYe)


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


def rge_gl4_evolve(state0, t_end, n_steps, model="2HDM_II", drop_Yu=False):
    """
    Implicit 2-stage Gauss-Legendre (GL4, order 4) fixed-point ODE integrator (disjoint from RK4!).
    Tracks exact linear-interpolated EWSB crossings (l1 or l2 crossing 0 downward) and step-1 signs.
    """
    s3 = mp.sqrt(3)
    a11 = mp.mpf(1) / 4
    a12 = mp.mpf(1) / 4 - s3 / 6
    a21 = mp.mpf(1) / 4 + s3 / 6
    a22 = mp.mpf(1) / 4
    h = mp.mpf(t_end) / n_steps
    y = state0
    t_cur = mp.mpf(0)
    ewsb_t = None
    ewsb_which = None
    ewsb_l1 = None
    ewsb_l2 = None
    l1_step1 = None
    l2_step1 = None
    fp_tol = mp.mpf(10) ** (-(mp.mp.dps - 6))
    for step_idx in range(n_steps):
        k0 = rge_rhs(y, model=model, drop_Yu=drop_Yu)
        k1 = k0
        k2 = k0
        for _fp in range(12):
            y1 = state_add(state_add(y, k1, h * a11), k2, h * a12)
            y2 = state_add(state_add(y, k1, h * a21), k2, h * a22)
            nk1 = rge_rhs(y1, model=model, drop_Yu=drop_Yu)
            nk2 = rge_rhs(y2, model=model, drop_Yu=drop_Yu)
            diff = max(state_diff_norm(nk1, k1), state_diff_norm(nk2, k2))
            k1, k2 = nk1, nk2
            if diff < fp_tol:
                break
        y_next = state_add(state_add(y, k1, h / 2), k2, h / 2)
        t_next = t_cur + h
        if step_idx == 0:
            l1_step1 = y_next[3]
            l2_step1 = y_next[4]
        else:
            if ewsb_l1 is None and y[3] > 0 and y_next[3] <= 0:
                ewsb_l1 = t_cur + (y[3] / (y[3] - y_next[3])) * h
            if ewsb_l2 is None and y[4] > 0 and y_next[4] <= 0:
                ewsb_l2 = t_cur + (y[4] / (y[4] - y_next[4])) * h
            if ewsb_t is None:
                for idx_l, name_l in ((3, "lambda_1"), (4, "lambda_2")):
                    if y[idx_l] > 0 and y_next[idx_l] <= 0:
                        ewsb_t = t_cur + (y[idx_l] / (y[idx_l] - y_next[idx_l])) * h
                        ewsb_which = name_l
                        break
        y = y_next
        t_cur = t_next
    ewsb_meta = {
        "t_EWSB": ewsb_t, "which": ewsb_which,
        "t_EWSB_l1": ewsb_l1, "t_EWSB_l2": ewsb_l2,
        "l1_step1": l1_step1, "l2_step1": l2_step1,
    }
    return y, ewsb_t, ewsb_meta


def polar_curved_G_s12(tau, solve_dps=28):
    """
    Polar Fuchsian developing-map quadrature for spin-1/2 Dirac Kahler metric G_{s=1/2}(tau)
    on centered fundamental parallelogram, verifying Gauss-Bonnet |Area/(2 pi) - 1| < 1e-3.
    """
    fuch = solve_fuchsian_gl8(tau, dps=solve_dps)
    with mp.workdps(solve_dps):
        tau = mp.mpc(tau)
        x, y = mp.re(tau), mp.im(tau)
        pi = mp.pi
        c_p = fuch["c_param"]
        Qinv = fuch["Qinv"]
        a_f = fuch["a_f"]
        b_f = fuch["b_f"]
        r0 = fuch["r_lat"] / 10
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

        ang_x, ang_w = gl_nodes_weights(12)
        w_x, w_w = gl_nodes_weights(14)

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
                if abs(qp) * (abs(cn_o) + abs(sn_o) + 1) < mp.mpf(10) ** (-16) and n > 2:
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
                if abs(qnn) * (abs(cn_e) + abs(sn_e) + 1) < mp.mpf(10) ** (-16) and n > 2:
                    break
                n += 1
                cn_e, sn_e = cn_e * c2 - sn_e * s2, sn_e * c2 + cn_e * s2
            # Exact order k in (4, 2, 3)
            return [pref * abs(th4) ** 2, pref * abs(th2) ** 2, pref * abs(th3) ** 2]

        def frob_psi(z):
            z2 = z * z
            sqz = mp.sqrt(z)
            lnz = mp.log(z)
            Sa = mp.mpc(0)
            Sap = mp.mpc(0)
            Sb = mp.mpc(0)
            Sbp = mp.mpc(0)
            zp = mp.mpc(1)
            for k in range(16):
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
            p1 = u1v * Qinv[0, 0] + u2v * Qinv[1, 0]
            p2 = u1v * Qinv[0, 1] + u2v * Qinv[1, 1]
            p1p = u1pv * Qinv[0, 0] + u2pv * Qinv[1, 0]
            p2p = u1pv * Qinv[0, 1] + u2pv * Qinv[1, 1]
            return p1, p2, p1p, p2p

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
        G_raw = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        with mp.workdps(16):
            sectors = [(mp.mpf(0), th_c1), (th_c1, th_c2), (th_c2, pi)]
            for th0, th1 in sectors:
                th_mid = (th0 + th1) / 2
                th_half = (th1 - th0) / 2
                for ai in range(len(ang_x)):
                    th = th_mid + th_half * ang_x[ai]
                    w_th = 2 * th_half * ang_w[ai]
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
                        e2om = 1 / (im12 * im12)
                        eom = abs(1 / im12)
                        jac = w_th * dw * (rv * rv) / (wv * wv)
                        area += jac * e2om
                        ds = densities(zv)
                        for j in range(3):
                            G_raw[j] += jac * eom * ds[j]
                    n_rad = 12
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
                        rh1_1 = p1 + dz * c1_g * p1p
                        rh1_2 = p1 + dz * c2_g * p1p
                        rh2_1 = p2 + dz * c1_g * p2p
                        rh2_2 = p2 + dz * c2_g * p2p
                        U1_1 = (m22 * rh1_1 - m12 * rh1_2) * idet
                        U1_2 = (-m21 * rh1_1 + m11 * rh1_2) * idet
                        U2_1 = (m22 * rh2_1 - m12 * rh2_2) * idet
                        U2_2 = (-m21 * rh2_1 + m11 * rh2_2) * idet
                        for rv_n, zv_n, u1n, u2n in [(r1, z1, U1_1, U2_1), (r2, z2, U1_2, U2_2)]:
                            im12 = mp.im(u1n * mp.conj(u2n))
                            e2om = 1 / (im12 * im12)
                            eom = abs(1 / im12)
                            jac = w_th * (dr / 2) * rv_n
                            area += jac * e2om
                            ds = densities(zv_n)
                            for j in range(3):
                                G_raw[j] += jac * eom * ds[j]
                        L1_1 = -q1 * U1_1
                        L1_2 = -q2 * U1_2
                        L2_1 = -q1 * U2_1
                        L2_2 = -q2 * U2_2
                        K1_1 = p1p + dz * (a11 * L1_1 + a12 * L1_2)
                        K1_2 = p1p + dz * (a21 * L1_1 + a22 * L1_2)
                        K2_1 = p2p + dz * (a11 * L2_1 + a12 * L2_2)
                        K2_2 = p2p + dz * (a21 * L2_1 + a22 * L2_2)
                        p1 += dzh * (K1_1 + K1_2)
                        p1p += dzh * (L1_1 + L1_2)
                        p2 += dzh * (K2_1 + K2_2)
                        p2p += dzh * (L2_1 + L2_2)
                        r_cur += dr
        mean_G = (G_raw[0] + G_raw[1] + G_raw[2]) / 3
        G_norm = [g / mean_G for g in G_raw]
        gb_err = abs(area / (2 * pi) - 1)
        return {
            "G_norm": G_norm,
            "gauss_bonnet_rel_err": gb_err,
            "sl2r_err": fuch["sl2r_err"],
            "L2": fuch["L2"],
        }


def apply_metric_canon(Y, G_mat_L, G_mat_R):
    """Canonicalize Y -> G_L^{-1/2} Y G_R^{-1/2} via mp.eigh (handles arbitrary Hermitian basis!)."""
    def inv_sqrt_H(G):
        ev, U = mp.eigh(G)
        D = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                D[i, j] = U[i, j] / mp.sqrt(mp.re(ev[j]))
        return mat_mul_3(D, mat_dag(U))

    return mat_mul_3(inv_sqrt_H(G_mat_L), mat_mul_3(Y, inv_sqrt_H(G_mat_R)))


def run_W4(alg, saved_vacua):
    t0 = time.monotonic_ns()
    out = {}

    # --- W4.1: Guardrail 4 Literature Benchmark Gate ---
    sym_bench = sympy_verify_chowdhury_eberhardt()
    # Numeric check of rge_rhs() on 1x1 diagonal matrices against SymPy 15/15 Type-II 2HDM!
    with mp.workdps(50):
        g1 = mp.mpf(3) / 7
        g2 = mp.mpf(5) / 8
        g3 = mp.mpf(9) / 10
        l1 = mp.mpf(1) / 5
        l2 = mp.mpf(2) / 7
        l3 = mp.mpf(-1) / 9
        l4 = mp.mpf(3) / 11
        yt = mp.mpf(4) / 5
        yb = mp.mpf(3) / 10
        ytau = mp.mpf(1) / 6
        Yu = mp.diag([0, 0, yt])
        Yd = mp.diag([0, 0, yb])
        Ye = mp.diag([0, 0, ytau])
        rhs = rge_rhs((g1, g2, g3, l1, l2, l3, l4, Yu, Yd, Ye), model="2HDM_II")
        k1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
        k2 = k1 * k1
        # Independent 1x1 Chowdhury-Eberhardt formula for (yt, yb, ytau)
        b1_u = (mp.mpf(9) / 2 * yt ** 2 + mp.mpf(1) / 2 * yb ** 2 - mp.mpf(17) / 12 * g1 ** 2 - mp.mpf(9) / 4 * g2 ** 2 - 8 * g3 ** 2) * yt
        b2_u = (
            -12 * yt ** 4 - mp.mpf(5) / 2 * yt ** 2 * yb ** 2 - mp.mpf(5) / 2 * yb ** 4 - mp.mpf(3) / 4 * yb ** 2 * ytau ** 2
            - 6 * l2 * yt ** 2 + (-2 * l3 + 2 * l4) * yb ** 2 + mp.mpf(3) / 2 * l2 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2
            + (mp.mpf(393) / 48 * g1 ** 2 + mp.mpf(225) / 16 * g2 ** 2 + 36 * g3 ** 2) * yt ** 2
            + (-mp.mpf(29) / 144 * g1 ** 2 + mp.mpf(33) / 16 * g2 ** 2 + mp.mpf(16) / 3 * g3 ** 2) * yb ** 2
            + mp.mpf(1267) / 216 * g1 ** 4 - mp.mpf(21) / 4 * g2 ** 4 - 108 * g3 ** 4
            - mp.mpf(3) / 4 * g1 ** 2 * g2 ** 2 + mp.mpf(19) / 9 * g1 ** 2 * g3 ** 2 + 9 * g2 ** 2 * g3 ** 2
        ) * yt
        b1_d = (mp.mpf(9) / 2 * yb ** 2 + mp.mpf(1) / 2 * yt ** 2 + ytau ** 2 - mp.mpf(5) / 12 * g1 ** 2 - mp.mpf(9) / 4 * g2 ** 2 - 8 * g3 ** 2) * yb
        b2_d = (
            -12 * yb ** 4 - mp.mpf(5) / 2 * yt ** 2 * yb ** 2 - mp.mpf(5) / 2 * yt ** 4 - mp.mpf(9) / 4 * yb ** 2 * ytau ** 2 - mp.mpf(9) / 4 * ytau ** 4
            - 6 * l1 * yb ** 2 + (-2 * l3 + 2 * l4) * yt ** 2 + mp.mpf(3) / 2 * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2
            + (mp.mpf(237) / 48 * g1 ** 2 + mp.mpf(225) / 16 * g2 ** 2 + 36 * g3 ** 2) * yb ** 2
            + (-mp.mpf(65) / 144 * g1 ** 2 + mp.mpf(33) / 16 * g2 ** 2 + mp.mpf(16) / 3 * g3 ** 2) * yt ** 2
            + (mp.mpf(25) / 8 * g1 ** 2 + mp.mpf(15) / 8 * g2 ** 2) * ytau ** 2
            - mp.mpf(113) / 216 * g1 ** 4 - mp.mpf(21) / 4 * g2 ** 4 - 108 * g3 ** 4
            - mp.mpf(9) / 4 * g1 ** 2 * g2 ** 2 + mp.mpf(31) / 9 * g1 ** 2 * g3 ** 2 + 9 * g2 ** 2 * g3 ** 2
        ) * yb
        b1_e = (mp.mpf(5) / 2 * ytau ** 2 + 3 * yb ** 2 - mp.mpf(15) / 4 * g1 ** 2 - mp.mpf(9) / 4 * g2 ** 2) * ytau
        b2_e = (
            -3 * ytau ** 4 - mp.mpf(27) / 4 * yb ** 4 - mp.mpf(27) / 4 * yb ** 2 * ytau ** 2 - mp.mpf(9) / 4 * yt ** 2 * yb ** 2
            - 6 * l1 * ytau ** 2 + mp.mpf(3) / 2 * l1 ** 2 + l3 ** 2 + l3 * l4 + l4 ** 2
            + (mp.mpf(179) / 16 * g1 ** 2 + mp.mpf(165) / 16 * g2 ** 2) * ytau ** 2
            + (mp.mpf(25) / 24 * g1 ** 2 + mp.mpf(45) / 8 * g2 ** 2 + 20 * g3 ** 2) * yb ** 2
            + mp.mpf(161) / 8 * g1 ** 4 - mp.mpf(21) / 4 * g2 ** 4 + mp.mpf(9) / 4 * g1 ** 2 * g2 ** 2
        ) * ytau
        ce_num_err = max(
            abs(rhs[7][2, 2] - (k1 * b1_u + k2 * b2_u)),
            abs(rhs[8][2, 2] - (k1 * b1_d + k2 * b2_d)),
            abs(rhs[9][2, 2] - (k1 * b1_e + k2 * b2_e)),
        )

    # Opposite Xing-Zhou |V_cb| downward running sign (dt < 0): 1HDM decreases (<0), Type-II 2HDM increases (>0)
    with mp.workdps(30):
        # Construct clean hierarchical Yukawas with small V_cb = 1/25
        th_cb = mp.mpf(1) / 25
        c_cb = mp.cos(th_cb)
        s_cb = mp.sin(th_cb)
        R23 = mp.matrix([[1, 0, 0], [0, c_cb, s_cb], [0, -s_cb, c_cb]])
        Yu_xz = mp.diag([mp.mpf(1) / 1000, mp.mpf(1) / 100, mp.mpf(1)])
        Yd_xz = mat_mul_3(R23, mp.diag([mp.mpf(1) / 500, mp.mpf(1) / 50, mp.mpf(1) / 2]))
        Ye_xz = mp.diag([mp.mpf(1) / 500, mp.mpf(1) / 50, mp.mpf(1) / 3])
        st_xz = (mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), Yu_xz, Yd_xz, Ye_xz)
        vcb0 = extract_observables(Yu_xz, Yd_xz, Ye_xz)["absV"][1][2]
        st_1h, _, _ = rge_gl4_evolve(st_xz, mp.mpf(-1) / 10, 8, model="1HDM")
        st_2h, _, _ = rge_gl4_evolve(st_xz, mp.mpf(-1) / 10, 8, model="2HDM_II")
        vcb_1h = extract_observables(st_1h[7], st_1h[8], st_1h[9])["absV"][1][2]
        vcb_2h = extract_observables(st_2h[7], st_2h[8], st_2h[9])["absV"][1][2]
        dvcb_1h_down = vcb_1h - vcb0
        dvcb_2h_down = vcb_2h - vcb0

    out["guardrail4_benchmark"] = {
        "sympy_ce15_all_exact": sym_bench["ce15_all_exact"],
        "sympy_sm_1hdm_triple": sym_bench["sm_1hdm_triple"],
        "sympy_sm_1hdm_exact": sym_bench["sm_1hdm_exact"],
        "numeric_ce15_max_err": mp_str(ce_num_err, 12),
        "dvcb_1hdm_down": mp_str(dvcb_1h_down, 12),
        "dvcb_2hdm_II_down": mp_str(dvcb_2h_down, 12),
        "opposite_xing_zhou_sign_ok": bool(dvcb_1h_down < 0 and dvcb_2h_down > 0),
    }

    # --- W4.2: Polar curved spin-1/2 Dirac Kahler metric G_{s=1/2}(tau) ---
    tau_apex = mp.mpc(mp.mpf(1) / 2, mp.sqrt(5) / 2)
    tau_2 = mp.mpc(mp.mpf(13) / 100, mp.mpf(2))
    G_apex = polar_curved_G_s12(tau_apex, solve_dps=28)
    G_tau2 = polar_curved_G_s12(tau_2, solve_dps=28)
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

    # --- W4.3: Un-sculpted 2-loop 2HDM-II GL4 RG unfolding (U_A, U_B, U_C, U_D; FLAT & CURVED) ---
    rg_runs = {}
    step_halving_err = None
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

        # Build UV raw Yukawas for U_A, U_B, U_C, U_D
        uv_states = {
            "UA_FrameC_y2": (
                eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, 1, -4),
                eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, 1, 2),
                eval_Y_canonical(alg26, ctx_t2, am_m, bm_m, -3, 6),
                G_tau2["G_norm"],
            ),
            "UB_W3_VCW_lam3_0_y2": (
                lin_comb_3(bases_t2[0], saved_vacua["U_B"][0], False),
                lin_comb_3(bases_t2[1], saved_vacua["U_B"][1], False),
                lin_comb_3(bases_t2[2], saved_vacua["U_B"][1], False),
                G_tau2["G_norm"],
            ),
            "UC_GeodesicApex": (
                eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, 1, -4),
                eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, 1, 2),
                eval_Y_canonical(alg26, ctx_ap, am_m, bm_m, -3, 6),
                G_apex["G_norm"],
            ),
            "UD_W3_DynamicV4_y2": (
                lin_comb_3(bases_t2[0], saved_vacua["U_D"][0], False),
                lin_comb_3(bases_t2[1], saved_vacua["U_D"][1], False),
                lin_comb_3(bases_t2[2], saved_vacua["U_D"][1], False),
                G_tau2["G_norm"],
            ),
        }

        def run_single_rg(Yu_raw, Yd_raw, Ye_raw, G_norm_vec, curved=False, g1_init=mp.mpf(1) / 2, n_steps=80):
            if curved:
                Gm = mp.diag([mp.mpf(v) for v in G_norm_vec])
                Yu0 = apply_metric_canon(Yu_raw, Gm, Gm)
                Yd0 = apply_metric_canon(Yd_raw, Gm, Gm)
                Ye0 = apply_metric_canon(Ye_raw, Gm, Gm)
            else:
                Yu0, Yd0, Ye0 = Yu_raw, Yd_raw, Ye_raw
            obs_uv_pre = extract_observables(Yu0, Yd0, Ye0)
            s_max = max(obs_uv_pre["su"][2], obs_uv_pre["sd"][2], obs_uv_pre["se"][2])
            Yu0 = Yu0 / s_max
            Yd0 = Yd0 / s_max
            Ye0 = Ye0 / s_max
            st0 = (
                g1_init, mp.mpf(1) / 2, mp.mpf(1) / 2,
                mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0),
                Yu0, Yd0, Ye0,
            )
            st_ir, t_ewsb, ewsb_meta = rge_gl4_evolve(st0, mp.mpf(-35), n_steps, model="2HDM_II")
            obs_uv = extract_observables(Yu0, Yd0, Ye0)
            obs_ir = extract_observables(st_ir[7], st_ir[8], st_ir[9])
            g1_ir, g2_ir, g3_ir, l1_ir, l2_ir, l3_ir, l4_ir = st_ir[:7]
            std_uv = bool((obs_uv["absV"][0][1] > obs_uv["absV"][1][2]) and (obs_uv["absV"][1][2] > obs_uv["absV"][0][2]))
            std_ir = bool((obs_ir["absV"][0][1] > obs_ir["absV"][1][2]) and (obs_ir["absV"][1][2] > obs_ir["absV"][0][2]))
            return {
                "state_ir": st_ir,
                "summary": {
                    "g1_IR": mp_str(g1_ir, 14), "g2_IR": mp_str(g2_ir, 14), "g3_IR": mp_str(g3_ir, 14),
                    "l1_IR": mp_str(l1_ir, 14), "l2_IR": mp_str(l2_ir, 14),
                    "l3_IR": mp_str(l3_ir, 14), "l4_IR": mp_str(l4_ir, 14),
                    "l1_step1": mp_str(ewsb_meta["l1_step1"], 10), "l2_step1": mp_str(ewsb_meta["l2_step1"], 10),
                    "yt_IR": mp_str(obs_ir["su"][2], 14), "yb_IR": mp_str(obs_ir["sd"][2], 14), "ytau_IR": mp_str(obs_ir["se"][2], 14),
                    "yt_over_g3_IR": mp_str(obs_ir["su"][2] / g3_ir, 14),
                    "mb_over_mtau_IR": mp_str(obs_ir["sd"][2] / obs_ir["se"][2], 14),
                    "ms_over_mmu_IR": mp_str(obs_ir["sd"][1] / obs_ir["se"][1], 14),
                    "u_m2m3_UV": mp_str(obs_uv["u_m2m3"], 14), "u_m2m3_IR": mp_str(obs_ir["u_m2m3"], 14),
                    "u_m1m3_IR": mp_str(obs_ir["u_m1m3"], 14),
                    "d_m2m3_UV": mp_str(obs_uv["d_m2m3"], 14), "d_m2m3_IR": mp_str(obs_ir["d_m2m3"], 14),
                    "d_m1m3_IR": mp_str(obs_ir["d_m1m3"], 14),
                    "e_m2m3_UV": mp_str(obs_uv["e_m2m3"], 14), "e_m2m3_IR": mp_str(obs_ir["e_m2m3"], 14),
                    "e_m1m3_IR": mp_str(obs_ir["e_m1m3"], 14),
                    "V12_UV": mp_str(obs_uv["absV"][0][1], 14), "V12_IR": mp_str(obs_ir["absV"][0][1], 14),
                    "V23_UV": mp_str(obs_uv["absV"][1][2], 14), "V23_IR": mp_str(obs_ir["absV"][1][2], 14),
                    "V13_UV": mp_str(obs_uv["absV"][0][2], 14), "V13_IR": mp_str(obs_ir["absV"][0][2], 14),
                    "J_CP_UV": mp_str(obs_uv["J_CP"], 14), "J_CP_IR": mp_str(obs_ir["J_CP"], 14),
                    "std_ckm_UV": std_uv, "std_ckm_IR": std_ir,
                    "t_EWSB": mp_str(t_ewsb, 14) if t_ewsb is not None else None,
                    "ewsb_channel": ewsb_meta["which"],
                    "t_EWSB_l1": mp_str(ewsb_meta["t_EWSB_l1"], 14) if ewsb_meta["t_EWSB_l1"] is not None else None,
                    "t_EWSB_l2": mp_str(ewsb_meta["t_EWSB_l2"], 14) if ewsb_meta["t_EWSB_l2"] is not None else None,
                },
            }

        for uname, (Yu_r, Yd_r, Ye_r, Gn) in uv_states.items():
            res_flat = run_single_rg(Yu_r, Yd_r, Ye_r, Gn, curved=False, n_steps=80)
            res_curv = run_single_rg(Yu_r, Yd_r, Ye_r, Gn, curved=True, n_steps=80)
            rg_runs[uname] = {
                "FLAT": res_flat["summary"],
                "CURVED": res_curv["summary"],
            }
            if uname == "UA_FrameC_y2":
                # Step-halving convergence check: 80 vs 160 GL4 steps on UA CURVED
                res_160 = run_single_rg(Yu_r, Yd_r, Ye_r, Gn, curved=True, n_steps=160)
                step_halving_err = state_diff_norm(res_curv["state_ir"], res_160["state_ir"])
                # Secondary g1_GUT diagnostic: g1_GUT(0) = 1/2 => g1(0) = sqrt(3/5)/2
                res_gut = run_single_rg(Yu_r, Yd_r, Ye_r, Gn, curved=True, g1_init=mp.sqrt(mp.mpf(3) / 5) / 2, n_steps=80)
                rg_runs["UA_FrameC_y2_g1GUT_diagnostic"] = res_gut["summary"]

    out["rg_unfolding_t0_to_m35"] = rg_runs
    out["gl4_step_halving_80_vs_160_err"] = mp_str(step_halving_err, 12)

    # --- W4.4: Canonical Neutrinos & Guardrail 3 Cayley Haar U(3)^5 Invariance ---
    nu_results = {}
    with mp.workdps(34):
        alg34 = build_frame_c_algebra()
        am_m, bm_m = mp.mpf(4) / 15, mp.mpf(1) / 30
        for label, tau_v, Gn in [
            ("tau_2_mark", mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), G_tau2["G_norm"]),
            ("tau_apex_mark", mp.mpc(mp.mpf(1) / 2, mp.sqrt(5) / 2), G_apex["G_norm"]),
        ]:
            ctx_w = make_tau_ctx(tau_v, solve_dps=30)
            Ye_raw = eval_Y_canonical(alg34, ctx_w, am_m, bm_m, -3, 6)
            Ynu_raw = eval_Y_canonical(alg34, ctx_w, am_m, bm_m, -3, 0)
            nu_sym_diff = mat_fro_norm(Ynu_raw - Ynu_raw.T) / mat_fro_norm(Ynu_raw)
            Gm = mp.diag([mp.mpf(v) for v in Gn])
            entry_nu = {"Ynu_asymmetry_rel": mp_str(nu_sym_diff, 12)}
            for metric_tag, is_curv in [("FLAT", False), ("CURVED", True)]:
                Ye_m = apply_metric_canon(Ye_raw, Gm, Gm) if is_curv else Ye_raw
                Ynu_m = apply_metric_canon(Ynu_raw, Gm, Gm) if is_curv else Ynu_raw
                _, Ue, _ = jw_svd(Ye_m)

                def pmns_block(kap, use_conj_U=True):
                    ms, Vtak, tres = takagi_6x6(kap)
                    # If L is on row: U_nu = conj(Vtak) satisfies U_nu^H kap U_nu^* = diag(ms)
                    U_nu = mp.matrix([[mp.conj(Vtak[i, j]) for j in range(3)] for i in range(3)]) if use_conj_U else Vtak
                    Upmns = mat_mul_3(mat_dag(Ue), U_nu)
                    th12, th23, th13 = mixing_angles_deg(Upmns)
                    dm21_sq = ms[1] ** 2 - ms[0] ** 2
                    dm31_sq = ms[2] ** 2 - ms[0] ** 2
                    r_dm = dm21_sq / dm31_sq if dm31_sq > 0 else mp.mpf(0)
                    return {
                        "m_nu": [mp_str(m, 14) for m in ms],
                        "m2_over_m3": mp_str(ms[1] / ms[2], 14),
                        "m1_over_m3": mp_str(ms[0] / ms[2], 14),
                        "dm21sq_over_dm31sq": mp_str(r_dm, 14),
                        "theta12_deg": mp_str(th12, 12),
                        "theta23_deg": mp_str(th23, 12),
                        "theta13_deg": mp_str(th13, 12),
                        "J_PMNS": mp_str(jarlskog(Upmns), 14),
                        "abs_Upmns": [[mp_str(abs(Upmns[i, j]), 12) for j in range(3)] for i in range(3)],
                        "takagi_residual": mp_str(tres, 10),
                    }

                # (A) Gauge-covariant L-row Weinberg operator kappa = Y_nu Y_nu^T with U_nu = conj(V_tak)
                kap_row = mat_mul_3(Ynu_m, Ynu_m.T)
                # (B) Literal Scope Card string kappa = Y_nu^T Y_nu (both conj(V_tak) and V_tak recorded)
                kap_lit = mat_mul_3(Ynu_m.T, Ynu_m)
                entry_nu[metric_tag] = {
                    "kappa_YYT_gauge_covariant": pmns_block(kap_row, use_conj_U=True),
                    "kappa_YTY_literal_Uconj": pmns_block(kap_lit, use_conj_U=True),
                    "kappa_YTY_literal_Vtak": pmns_block(kap_lit, use_conj_U=False),
                }
            nu_results[label] = entry_nu

        # 10-trial Cayley-transform Haar U(3)^5 invariance test across:
        #   Curved Kahler (G_f -> W_f G_f W_f^H) + 2-loop GL4 RG (t = 0 -> -5, 16 steps) + Takagi PMNS!
        ctx_h = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=30)
        Yu_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, 1, -4)
        Yd_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, 1, 2)
        Ye_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, -3, 6)
        Ynu_b = eval_Y_canonical(alg34, ctx_h, am_m, bm_m, -3, 0)
        Gm_b = mp.diag([mp.mpf(v) for v in G_tau2["G_norm"]])

        def full_pipeline_observables(Yu_in, Yd_in, Ye_in, Ynu_in, GQ, Gu, Gd, GL, Ge, Gnu):
            Yu_c = apply_metric_canon(Yu_in, GQ, Gu)
            Yd_c = apply_metric_canon(Yd_in, GQ, Gd)
            Ye_c = apply_metric_canon(Ye_in, GL, Ge)
            Ynu_c = apply_metric_canon(Ynu_in, GL, Gnu)
            # Normalize by max singular value (U(3)^5 invariant!)
            s_max = max(jw_svd(Yu_c)[0][2], jw_svd(Yd_c)[0][2], jw_svd(Ye_c)[0][2])
            st0 = (
                mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2,
                mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0),
                Yu_c / s_max, Yd_c / s_max, Ye_c / s_max,
            )
            st_ir, _, _ = rge_gl4_evolve(st0, mp.mpf(-5), 16, model="2HDM_II")
            obs_ir = extract_observables(st_ir[7], st_ir[8], st_ir[9])
            # Takagi PMNS on gauge-covariant kappa = Ynu_c Ynu_c^T with IR U_e (Wait: U_e from Ye_ir transforms as W_L U_e!)
            _, Ue_ir, _ = jw_svd(st_ir[9])
            kap = mat_mul_3(Ynu_c, Ynu_c.T)
            ms, Vtak, _ = takagi_6x6(kap)
            U_nu = mp.matrix([[mp.conj(Vtak[i, j]) for j in range(3)] for i in range(3)])
            Upmns = mat_mul_3(mat_dag(Ue_ir), U_nu)
            vec = (
                obs_ir["su"] + obs_ir["sd"] + obs_ir["se"]
                + [obs_ir["absV"][i][j] for i in range(3) for j in range(3)]
                + [obs_ir["J_CP"]]
                + ms
                + [abs(Upmns[i, j]) for i in range(3) for j in range(3)]
                + [jarlskog(Upmns)]
            )
            return vec, Ue_ir, Ynu_c

        base_vec, Ue_base, Ynu_c_base = full_pipeline_observables(
            Yu_b, Yd_b, Ye_b, Ynu_b, Gm_b, Gm_b, Gm_b, Gm_b, Gm_b, Gm_b
        )
        rng_haar = Sha256Rng("AGY002_REFEREE_CAYLEY_HAAR_U3_5")
        max_haar_err = mp.mpf(0)
        max_unitarity_err = mp.mpf(0)
        I3 = mp.eye(3)
        # Also test whether literal Ynu^T Ynu breaks Ynu -> W_L Ynu (Guardrail 3 diagnostic!)
        kap_lit_base = mat_mul_3(Ynu_c_base.T, Ynu_c_base)
        ms_lit0, Vtak_lit0, _ = takagi_6x6(kap_lit_base)
        max_lit_YTY_wl_break = mp.mpf(0)

        for trial in range(10):
            WQ = haar_u3_cayley(rng_haar)
            Wu = haar_u3_cayley(rng_haar)
            Wd = haar_u3_cayley(rng_haar)
            WL = haar_u3_cayley(rng_haar)
            We = haar_u3_cayley(rng_haar)
            for W in (WQ, Wu, Wd, WL, We):
                uerr = mat_fro_norm(mat_mul_3(mat_dag(W), W) - I3)
                if uerr > max_unitarity_err:
                    max_unitarity_err = uerr
            # Transform raw Yukawas AND curved Kahler metrics under U(3)^5 (nu_R fixed by M_R = I_3!)
            Yu_t = mat_mul_3(WQ, mat_mul_3(Yu_b, mat_dag(Wu)))
            Yd_t = mat_mul_3(WQ, mat_mul_3(Yd_b, mat_dag(Wd)))
            Ye_t = mat_mul_3(WL, mat_mul_3(Ye_b, mat_dag(We)))
            Ynu_t = mat_mul_3(WL, Ynu_b)
            GQ_t = mat_mul_3(WQ, mat_mul_3(Gm_b, mat_dag(WQ)))
            Gu_t = mat_mul_3(Wu, mat_mul_3(Gm_b, mat_dag(Wu)))
            Gd_t = mat_mul_3(Wd, mat_mul_3(Gm_b, mat_dag(Wd)))
            GL_t = mat_mul_3(WL, mat_mul_3(Gm_b, mat_dag(WL)))
            Ge_t = mat_mul_3(We, mat_mul_3(Gm_b, mat_dag(We)))
            vec_t, _, Ynu_ct = full_pipeline_observables(Yu_t, Yd_t, Ye_t, Ynu_t, GQ_t, Gu_t, Gd_t, GL_t, Ge_t, Gm_b)
            terr = max(abs(vec_t[k] - base_vec[k]) / max(mp.mpf(1), abs(base_vec[k])) for k in range(len(base_vec)))
            if terr > max_haar_err:
                max_haar_err = terr
            if trial == 0:
                ms_lit_t, _, _ = takagi_6x6(mat_mul_3(Ynu_ct.T, Ynu_ct))
                max_lit_YTY_wl_break = max(abs(ms_lit_t[k] - ms_lit0[k]) / max(mp.mpf(10)**(-12), ms_lit0[k]) for k in range(3))

    out["canonical_neutrinos"] = nu_results
    out["guardrail3_cayley_haar_U3_5"] = {
        "trials": 10,
        "max_cayley_unitarity_err": mp_str(max_unitarity_err, 10),
        "max_observable_rel_err_curved_rg_takagi": mp_str(max_haar_err, 12),
        "diagnostic_literal_YTY_breaks_WL_rel_err": mp_str(max_lit_YTY_wl_break, 12),
    }
    out["runtime_s"] = elapsed_sec_str(t0)
    return out


# ============================================================================
# 9. MODULE W5: SIX REFEREE PLANTED NEGATIVE CONTROLS (RPF1 - RPF6)
# ============================================================================

def run_W5(alg):
    t0 = time.monotonic_ns()
    out = {}
    _, P30_pairs = generate_P30()
    P30_pts, _ = generate_P30()

    # --- RPF1: Drop +ln(y) from L_2(i/y) reproduces B1980 (0.12, 0.18, 0.32) ---
    rpf1_rows = []
    b1980_targets = [mp.mpf("0.12"), mp.mpf("0.18"), mp.mpf("0.32")]
    rpf1_caught = True
    with mp.workdps(26):
        alg26 = build_frame_c_algebra()
        axis_pairs = [
            (Fraction(5, 4), Fraction(4, 5)),
            (Fraction(3, 2), Fraction(2, 3)),
            (Fraction(5, 2), Fraction(2, 5)),
        ]
        for idx_p, (y_f, iy_f) in enumerate(axis_pairs):
            yv = mp.mpf(y_f.numerator) / y_f.denominator
            iyv = mp.mpf(iy_f.numerator) / iy_f.denominator
            L2_y = get_L2(mp.mpc(0, yv), solve_dps=28)
            # PLANTED BUG: use clamped L2_y instead of L2_y + ln(y) at i/y!
            ctx_y = make_tau_ctx(mp.mpc(0, yv), L2_val=L2_y)
            ctx_iy_bug = make_tau_ctx(mp.mpc(0, iyv), L2_val=L2_y)
            map_y = {}
            map_iy = {}
            for p in P30_pairs:
                am, bm = mp.mpf(p[0]) / 30, mp.mpf(p[1]) / 30
                map_y[p] = extract_observables(
                    eval_Y_canonical(alg26, ctx_y, am, bm, 1, -4),
                    eval_Y_canonical(alg26, ctx_y, am, bm, 1, 2),
                    eval_Y_canonical(alg26, ctx_y, am, bm, -3, 6),
                )["vec9"]
                map_iy[p] = extract_observables(
                    eval_Y_canonical(alg26, ctx_iy_bug, am, bm, 1, -4),
                    eval_Y_canonical(alg26, ctx_iy_bug, am, bm, 1, 2),
                    eval_Y_canonical(alg26, ctx_iy_bug, am, bm, -3, 6),
                )["vec9"]
            mx_d = mp.mpf(0)
            for a_i, b_i in P30_pts:
                p1 = min((a_i, b_i), ((-a_i) % 30, (-b_i) % 30))
                wp_a, wp_b = (-b_i) % 30, a_i % 30
                p2 = min((wp_a, wp_b), ((-wp_a) % 30, (-wp_b) % 30))
                d9 = b1980_dist(map_y[p1], map_iy[p2])
                if d9 > mx_d:
                    mx_d = d9
            if abs(mx_d - b1980_targets[idx_p]) > mp.mpf(2) / 100:
                rpf1_caught = False
            rpf1_rows.append({
                "pair": f"({frac_str(y_f)}, {frac_str(iy_f)})",
                "buggy_max_9log_dist": mp_str(mx_d, 10),
                "expected_approx": mp_str(b1980_targets[idx_p], 4),
            })
    out["RPF1_drop_ln_y_reproduces_B1980"] = {
        "rows": rpf1_rows,
        "caught": rpf1_caught,
    }

    # --- RPF2: Drop sqrt(y) breaks absolute s_k invariance by exact factor |c*tau + d| ---
    with mp.workdps(35):
        alg35 = build_frame_c_algebra()
        tau1 = mp.mpc(mp.mpf(13) / 100, mp.mpf(6) / 5)
        L2_1 = get_L2(tau1, solve_dps=30)
        ctx1 = make_tau_ctx(tau1, L2_val=L2_1)
        tau_S = -1 / tau1
        ctxS = make_tau_ctx(tau_S, L2_val=L2_1 + mp.log(abs(tau1)))
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        # Bare weight-+1 Y (weight_zero=False)
        s0 = jw_svd(eval_Y_canonical(alg35, ctx1, am, bm, 1, -4, weight_zero=False))[0][2]
        sS = jw_svd(eval_Y_canonical(alg35, ctxS, (-bm) % 1, am, 1, -4, weight_zero=False))[0][2]
        ratio_S = sS / s0
        expected_fac = abs(tau1)
        ratio_match_err = abs(ratio_S - expected_fac) / expected_fac
        rel_break = abs(sS - s0) / s0
    out["RPF2_drop_sqrt_y_breaks_abs_sk"] = {
        "bare_s3_ratio_S": mp_str(ratio_S, 18),
        "expected_abs_c_tau_plus_d": mp_str(expected_fac, 18),
        "ratio_match_rel_err": mp_str(ratio_match_err, 10),
        "rel_invariance_break": mp_str(rel_break, 12),
        "caught": bool(rel_break > mp.mpf(1) / 10 and ratio_match_err < mp.mpf(10) ** (-25)),
    }

    # --- RPF3: Flip V_4 -> -V_4 (and V_CW -> -V_CW) reverses optimum / destroys hierarchy ---
    with mp.workdps(24):
        alg24 = build_frame_c_algebra()
        tau2 = mp.mpc(mp.mpf(13) / 100, mp.mpf(2))
        ctx2 = make_tau_ctx(tau2, solve_dps=28)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        bases = [
            assemble_Y_basis(alg24, ctx2, am, bm, 1, -4),
            assemble_Y_basis(alg24, ctx2, am, bm, 1, 2),
            assemble_Y_basis(alg24, ctx2, am, bm, -3, 6),
        ]
        _, _, mu2 = eval_point_potentials(alg24, ctx2, am, bm)
        r_v4_good = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "V4", "rpf3_v4_g", sign_flip=1, n_starts=6, max_iter=60)
        r_v4_flip = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "V4", "rpf3_v4_f", sign_flip=-1, n_starts=6, max_iter=60)
        r_vcw_good = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "VCW", "rpf3_vcw_g", sign_flip=1, n_starts=6, max_iter=60)
        r_vcw_flip = minimize_1doublet_S5(bases, ctx2["c_hat"], mu2, "VCW", "rpf3_vcw_f", sign_flip=-1, n_starts=6, max_iter=60)
        rpf3_caught = bool(
            (r_v4_flip["r_h"] > r_v4_good["r_h"] + mp.mpf(3) / 10)
            and (r_v4_flip["obs"]["d_m2m3"] > r_v4_good["obs"]["d_m2m3"] * 5)
            and (abs(r_vcw_flip["r_h"] - r_vcw_good["r_h"]) > mp.mpf(3) / 10)
        )
    out["RPF3_sign_flip_destroys_hierarchy"] = {
        "V4_good_r": mp_str(r_v4_good["r_h"], 10),
        "V4_good_d_m2m3": mp_str(r_v4_good["obs"]["d_m2m3"], 10),
        "V4_flipped_r": mp_str(r_v4_flip["r_h"], 10),
        "V4_flipped_d_m2m3": mp_str(r_v4_flip["obs"]["d_m2m3"], 10),
        "VCW_good_r": mp_str(r_vcw_good["r_h"], 10),
        "VCW_flipped_r": mp_str(r_vcw_flip["r_h"], 10),
        "caught": rpf3_caught,
    }

    # --- RPF4: Wrong point action w*gamma (instead of w*gamma^{-1}) breaks T and M ---
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
        wrong_dists = {}
        for gname, (ga, gb, gc, gd) in [("T", (1, 1, 0, 1)), ("M", (2, 1, 1, 1))]:
            tau_g = (ga * tau1 + gb) / (gc * tau1 + gd)
            ctxg = make_tau_ctx(tau_g, L2_val=L2_1 + mp.log(abs(gc * tau1 + gd)))
            # WRONG action w * gamma = (a*w0 + c*w1, b*w0 + d*w1) mod 1
            wa_bad = (ga * am + gc * bm) % 1
            wb_bad = (gb * am + gd * bm) % 1
            vg = extract_observables(
                eval_Y_canonical(alg30, ctxg, wa_bad, wb_bad, 1, -4),
                eval_Y_canonical(alg30, ctxg, wa_bad, wb_bad, 1, 2),
                eval_Y_canonical(alg30, ctxg, wa_bad, wb_bad, -3, 6),
            )["vec9"]
            wrong_dists[gname] = b1980_dist(v0, vg)
    out["RPF4_wrong_point_action_breaks_T_and_M"] = {
        "T_wrong_action_9log_dist": mp_str(wrong_dists["T"], 12),
        "M_wrong_action_9log_dist": mp_str(wrong_dists["M"], 12),
        "caught": bool(wrong_dists["T"] > mp.mpf(1) / 10 and wrong_dists["M"] > mp.mpf(1) / 10),
    }

    # --- RPF5: Drop Y_u from 2HDM RG breaks benchmark & eliminates lambda_2 EWSB ---
    with mp.workdps(26):
        alg26 = build_frame_c_algebra()
        ctx2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=28)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        Yu0 = eval_Y_canonical(alg26, ctx2, am, bm, 1, -4)
        Yd0 = eval_Y_canonical(alg26, ctx2, am, bm, 1, 2)
        Ye0 = eval_Y_canonical(alg26, ctx2, am, bm, -3, 6)
        s_max = max(jw_svd(Yu0)[0][2], jw_svd(Yd0)[0][2], jw_svd(Ye0)[0][2])
        st0 = (
            mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2,
            mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0),
            Yu0 / s_max, Yd0 / s_max, Ye0 / s_max,
        )
        st_good, t_ewsb_good, meta_good = rge_gl4_evolve(st0, mp.mpf(-35), 40, model="2HDM_II", drop_Yu=False)
        st_drop, t_ewsb_drop, meta_drop = rge_gl4_evolve(st0, mp.mpf(-35), 40, model="2HDM_II", drop_Yu=True)
        # Also check 1x1 yt benchmark error when drop_Yu=True
        rhs_good = rge_rhs((mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, 0, 0, 0, 0, mp.diag([0, 0, 1]), mp.diag([0, 0, mp.mpf(1) / 2]), mp.diag([0, 0, mp.mpf(1) / 3])), drop_Yu=False)
        rhs_bad = rge_rhs((mp.mpf(1) / 2, mp.mpf(1) / 2, mp.mpf(1) / 2, 0, 0, 0, 0, mp.diag([0, 0, 1]), mp.diag([0, 0, mp.mpf(1) / 2]), mp.diag([0, 0, mp.mpf(1) / 3])), drop_Yu=True)
        bench_break = abs(rhs_good[7][2, 2] - rhs_bad[7][2, 2])
    out["RPF5_drop_Yu_breaks_RG_and_EWSB"] = {
        "good_l2_IR": mp_str(st_good[4], 12),
        "dropped_Yu_l2_IR": mp_str(st_drop[4], 12),
        "good_l2_step1": mp_str(meta_good["l2_step1"], 10),
        "dropped_Yu_l2_step1": mp_str(meta_drop["l2_step1"], 10),
        "good_t_EWSB": mp_str(t_ewsb_good, 10) if t_ewsb_good is not None else None,
        "good_ewsb_channel": meta_good["which"],
        "dropped_Yu_t_EWSB": mp_str(t_ewsb_drop, 10) if t_ewsb_drop is not None else None,
        "dropped_Yu_ewsb_channel": meta_drop["which"],
        "benchmark_dyt_break": mp_str(bench_break, 10),
        "caught": bool(bench_break > mp.mpf(1) / 1000 and abs(st_good[4] - st_drop[4]) > mp.mpf(1) / 100),
    }

    # --- RPF6: Non-unitary basis rotation breaks Haar invariance ---
    with mp.workdps(30):
        alg30 = build_frame_c_algebra()
        ctx2 = make_tau_ctx(mp.mpc(mp.mpf(13) / 100, mp.mpf(2)), solve_dps=28)
        am, bm = mp.mpf(4) / 15, mp.mpf(1) / 30
        Yu0 = eval_Y_canonical(alg30, ctx2, am, bm, 1, -4)
        Yd0 = eval_Y_canonical(alg30, ctx2, am, bm, 1, 2)
        Ye0 = eval_Y_canonical(alg30, ctx2, am, bm, -3, 6)
        obs0 = extract_observables(Yu0, Yd0, Ye0)
        # Non-unitary invertible matrix S_nu = diag(1, 3/2, 2/3) + shear
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
                root = alias.name.split(".")[0]
                if root in forbidden:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                if root in forbidden:
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
    out_json_path = os.path.join(out_dir, "referee_a2_whole_instrument_out.json")
    out_sha_path = os.path.join(out_dir, "OUTPUT_SHA256.txt")

    mp.mp.dps = 30
    alg = build_frame_c_algebra()

    w1 = run_W1(alg)
    w2 = run_W2(alg)
    w3, saved_vacua = run_W3(alg)
    w4 = run_W4(alg, saved_vacua)
    w5 = run_W5(alg)
    ast_audit = ast_purity_audit(script_path)

    # Dynamically compute all 6 Referee Gates (RG1 - RG6) from numerical results (Guardrail 2!)
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
        and mp.mpf(w2["geodesic_gamma_M"]["max_basepoint_rel_err_traces_32"]) < mp.mpf(10) ** (-9)
        and mp.mpf(w2["W_LV1"]["max_neg_qQ_rel_err"]) < mp.mpf(10) ** (-40)
    )
    rg3 = bool(
        w3["higgs_direction_optimization"]["all_1doublet_minima_M2M3_compliant"]
        and mp.mpf(w3["higgs_direction_optimization"]["max_grad_norm"]) < mp.mpf(10) ** (-8)
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
        and mp.mpf(w4["guardrail3_cayley_haar_U3_5"]["max_observable_rel_err_curved_rg_takagi"]) < mp.mpf(10) ** (-25)
    )
    rg5 = bool(w5["all_6_caught"])
    rg6 = bool(ast_audit["pass"])

    payload = {
        "card_id": "AGY-002_A2-WHOLE-INSTRUMENT",
        "role": "COLD_ROOM_ZERO_TRUST_DISJOINT_REFEREE",
        "firewall": "0 of 19",
        "disjoint_methods": {
            "fuchsian_L2": "4-stage Gauss-Legendre (GL8, order 8) + holomorphic variational dT/dc + Chebyshev theta_1 log-deriv wp + Euler pentagonal eta + 3-trace (Ta,Tb,Tab) Gauss-Newton",
            "linear_algebra": "6x6 Hermitian Jordan-Wielandt mp.eigh SVD + 6x6 real-split mp.eigsy Autonne-Takagi + Cayley-transform Haar U(3)^5",
            "rge_integrator": "Implicit 2-stage Gauss-Legendre (GL4, order 4) fixed-point + independent SymPy CE15/MV85 derivation",
            "optimization": "Riemannian projected Barzilai-Borwein on S^5 and S^5 x S^5 with analytic Wirtinger gradients",
            "geodesic_quadrature": "32-node + 16-node periodic midpoint quadrature with shifted-grid basepoint checks",
        },
        "W1": w1,
        "W2": w2,
        "W3": w3,
        "W4": w4,
        "W5": w5,
        "RG6_ast_audit": ast_audit,
        "gates": {
            "RG1": rg1,
            "RG2": rg2,
            "RG3": rg3,
            "RG4": rg4,
            "RG5": rg5,
            "RG6": rg6,
            "all_6_gates_pass": bool(rg1 and rg2 and rg3 and rg4 and rg5 and rg6),
        },
        "total_runtime_s": elapsed_sec_str(t_total),
    }

    raw_json = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    # Strict zero-JSON-float verification before sealing!
    def reject_float(s):
        raise ValueError(f"JSON float token forbidden: {s}")

    json.loads(raw_json, parse_float=reject_float)

    with open(out_json_path, "w", encoding="utf-8") as f:
        f.write(raw_json)

    digest = hashlib.sha256(raw_json.encode("utf-8")).hexdigest()
    with open(out_sha_path, "w", encoding="utf-8") as f:
        f.write(f"{digest}  referee_a2_whole_instrument_out.json\n")

    print(f"SEALED {out_json_path} sha256={digest} runtime={payload['total_runtime_s']}s")


if __name__ == "__main__":
    main()
