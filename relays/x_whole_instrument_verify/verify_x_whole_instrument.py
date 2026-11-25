#!/usr/bin/env python3
r"""
Standalone Pre-Hashed Producer for Claim Card whole_instrument_m12_covariance_and_cube_churn (strictly 0 of 19):
Whole-Instrument 3D Mapping-Torus Cohomology, Exact Matrix SL(2,Z) Cube Covariance, and Generation-Churn Theorem:

  - WI_1 (Cohomological Origin of Order-30's P96 on m004's Cyclic Covers):
      Enumerates all 900 points of E[30] and all 576 points of exact order 30, proves ord(M mod 30) = 60
      for M = LR = [[2,1],[1,1]], and evaluates ker(M^k - I_2) across all 12 divisors k | 60.
      Proves k = 12 (the cyclic cover M_{12} -> m004) is the unique minimal cover < 60 supporting global
      exact-order-30 flat torsion bundles (all k in {1,2,3,4,5,6,10,15,20,30} give 0), and proves
      ker(M^12 - I_2) on exact-order-30 torsion equals B1976's 96-point set P96 = K_5 + E[2]* + E[3]*
      identically (96/96 exact match, decomposing into 8 closed M-orbits of length 12).

  - WI_2 (Exact Weight-0 Matrix SL(2,Z) Covariance & Cube-Group Parallel Transport — P-882 & B1982/B1984):
      Computes B1667's canonical cusp collar L_2(tau) from first principles via 3-stage order-6
      Gauss-Legendre ODE integration of y'' + (wp(z)/4 + c)y = 0 + exact analytic Frobenius monodromy
      (verified at tau = i and tau = omega = 1/2 + i*sqrt(3)/2). Proves at 32-dps that with B1921/B1982's
      covariant end law L_cov(gamma*tau) = L_cov(tau) + ln|C*tau + D|, the normalized Yukawa operator
      Y_hat_sec(tau, p) = sqrt(Im tau) * Y_sec(tau, p; L_cov(tau)) has exact modular weight 0 and obeys
        Y_hat_sec(gamma*tau, p*gamma^{-1}) = exp(i*phi) * W(gamma) * Y_hat_sec(tau, p) * W(gamma)^T
      to < 10^-25 across all generators gamma in {T, S, L, R, M=LR}, all sectors (up, down, lep), and
      torsion points. Proves <W(T), W(S)> subset O(3) has order 48 (O_h), quotient modulo +-I_3 of order
      24 (S_4 = Aut(Q_8), uniting Frame C with B1984's cube group), <W(L), W(R)> subset SO(3) has order 24,
      and W(M) = [[0,1,0],[0,0,-1],[-1,0,0]] has exact order 3 (so W(M)^12 = +I_3 closes on M_{12}).

  - WI_3 (Parameter-Free 3D Geodesic Mapping-Torus Operators, 72-Haar Gate, Deck-Commutant CKM Lock, & Churn):
      Evaluates m004's Mostow-rigid geodesic tau(u) = (phi*i*e^u - phi^{-1})/(i*e^u + 1) (zero free Im tau),
      proving algebraically that midpoint nodes u_0 = ln(phi) and u_1 = 3*ln(phi) satisfy tau(u_0) = 1 + i
      = T(i) and tau(u_1) = (3 + i)/2 = M(i) (exact accessory parameter c = 0), and checks continuum
      convergence at N_sub = 4 (48 slices around M_{12}). Constructs all three cut-free 3D operators:
      (1) Cut-Free Floquet Lyapunov Tensor G_bar_L, (2) Floquet Eigenvalue Moduli |eig(M_loop)|, and
      (3) 72x72 Kaluza-Klein Covariant Laplace-Yukawa Operator -D_{u,L}^2 + Y_hat(u) Y_hat(u)^H.
      Verifies < 10^-12 invariance under 72 independent local Haar U(3) basis rotations (Guardrail 3) and
      < 10^-12 invariance under cyclic orbit shifts p_0 -> p_0*M. Proves the Deck-Commutant CKM Lock on
      odd-order torsion P5 and P15 (|[G_bar_L, W(M)]| < 10^-22 => V_CKM = I_3 to < 10^-20, zero mixing!)
      vs E[2]* period-3 Spin-Cube Resonance on P30 (unlocking diag = 0.9834, |V_12| = 0.1085, |V_23| = 0.0864,
      and lepton-down split 0.05283 vs 0.28180 on Orbit 0, while order-3 cube-rotation churn caps symmetric
      parameter-free kappa = 1 quark ratios at up = (0.20282, 0.38793) and down = (0.28180, 0.53162)).

  - WI_4 (Whole P96 Shell Audit: Inversion & Amphicheiral Reduction 8 -> 4 Pairs & 96-Point Washout):
      Proves M^6 != -I_2 (mod 30), so elliptic inversion -I_2 pairs the 8 orbits into 4 exact isospectral
      pairs (0~2, 1~6, 3~4, 5~7; verified to < 10^-22). Proves m004's det=-1 amphicheiral involutions
      Q M Q^{-1} = M^{-1} fix orbits {0, 2, 3, 4} and swap 1<->6, 5<->7 (1 discrete bit between {0,2} and
      {3,4} prior to spectrum inspection), while choice-free 96-point shell averaging washes quark ratios
      to up = (0.51448, 0.68240), down = (0.51844, 0.76732), diag = 0.8244.

  - WI_5 (Lifting to 8^3_4's Three Cusps (1, 2, 2): Exact SL(2, Z[omega]) Spinor Decay & Order-3 Churn):
      Constructs pi_1(m004) subset SL(2, Z[omega]) and its unique |G|=10 irregular D_5 cover 8^3_4
      (cusps of degrees 1, 2, 2 with heights 2*sqrt(3), sqrt(3), sqrt(3)) directly from group matrices.
      Proves canonical longitude bABaaBAb lifts with trivial D_5 permutation and exact trace -2 on all 3
      cusps: B933's rho_1 gives (+2, -2) on all 3 cusps, twisted rho_0 splits singleton (-2, -2) from twins
      (+2, -2), both enforce exponential L^2 harmonic-spinor decay on every cusp (zero constant-mode leak),
      and interior meridian holonomies W(M), W(M)^2 both retain exact order 3.

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 float()/complex() casts, 0 JSON floats.
  - 0 imports from frontier/, peer scripts, snappy, numpy, scipy, or prior relay scripts (python3 -I).
  - 0 empirical PDG/NuFIT/Planck/DESI/CODATA constants (strictly 0 of 19).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp

SELF_PATH = Path(__file__).resolve()
OUT_PATH = SELF_PATH.parent / "verify_x_whole_instrument_out.json"

I_MP = mp.mpc(0, 1)
HALF_FR = Fr(1, 2)


def q_mp(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def p10_mp(e: int) -> mp.mpf:
    return mp.mpf(10) ** int(e)


def fr_mp(f: Fr) -> mp.mpf:
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def assert_ast_clean(path: Path) -> dict[str, int]:
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(path))
    float_lits = 0
    complex_lits = 0
    bad_casts = 0
    bad_imports = 0
    allowed = {"__future__", "ast", "hashlib", "itertools", "json", "math", "fractions", "pathlib", "typing", "mpmath"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_lits += 1
            elif isinstance(node.value, complex):
                complex_lits += 1
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("float", "complex"):
                bad_casts += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed:
                    bad_imports += 1
        elif isinstance(node, ast.ImportFrom):
            if node.module is None or node.module.split(".")[0] not in allowed:
                bad_imports += 1
    assert (float_lits, complex_lits, bad_casts, bad_imports) == (0, 0, 0, 0), (
        float_lits, complex_lits, bad_casts, bad_imports
    )
    return {
        "ast_float_literals": float_lits,
        "ast_complex_literals": complex_lits,
        "ast_float_or_complex_casts": bad_casts,
        "forbidden_imports": bad_imports,
    }


def assert_no_json_floats(obj: Any) -> None:
    if isinstance(obj, (float, complex)):
        raise AssertionError(f"Forbidden float/complex in JSON: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert isinstance(k, str)
            assert_no_json_floats(v)
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            assert_no_json_floats(item)


# ---------------------------------------------------------------------------
# Self-Contained B1667 Canonical Cusp Collar L_2(tau) via Order-6 GL3 + Frobenius
# ---------------------------------------------------------------------------
def thetas_pun(v: mp.mpc, tau: mp.mpc, n_terms: int = 16) -> tuple[mp.mpc, mp.mpc, mp.mpc, mp.mpc]:
    q = mp.exp(I_MP * mp.pi * tau)
    t1 = mp.mpc(0)
    t2 = mp.mpc(0)
    half = q_mp(1, 2)
    for n in range(n_terms):
        qn = mp.exp(I_MP * mp.pi * tau * ((mp.mpf(n) + half) ** 2))
        ang = (2 * n + 1) * v
        sgn = -1 if (n & 1) else 1
        t1 += 2 * sgn * qn * mp.sin(ang)
        t2 += 2 * qn * mp.cos(ang)
    t3 = mp.mpc(1)
    t4 = mp.mpc(1)
    for m in range(1, n_terms):
        qm = q ** (m * m)
        cm = mp.cos(2 * m * v)
        t3 += 2 * qm * cm
        t4 += 2 * (-1 if (m & 1) else 1) * qm * cm
    return t1, t2, t3, t4


def wp_pun(z: mp.mpc, tau: mp.mpc, t30: mp.mpc, t40: mp.mpc, e1: mp.mpc) -> mp.mpc:
    n_im = int(mp.nint(mp.im(z) / mp.im(tau)))
    zr = z - n_im * tau
    n_re = int(mp.nint(mp.re(zr)))
    zr = zr - n_re
    t1, t2, _, _ = thetas_pun(mp.pi * zr, tau)
    return (mp.pi * t30 * t40 * t2 / t1) ** 2 + e1


def gl3_step_2x2(z0: mp.mpc, dz: mp.mpc, tau: mp.mpc, c: mp.mpc, t30: mp.mpc, t40: mp.mpc, e1: mp.mpc) -> mp.matrix:
    s15 = mp.sqrt(15)
    nodes = [(mp.mpf(5) - s15) / 10, q_mp(1, 2), (mp.mpf(5) + s15) / 10]
    b_w = [q_mp(5, 18), q_mp(4, 9), q_mp(5, 18)]
    amat = [
        [q_mp(5, 36), q_mp(2, 9) - s15 / 15, q_mp(5, 36) - s15 / 30],
        [q_mp(5, 36) + s15 / 24, q_mp(2, 9), q_mp(5, 36) - s15 / 24],
        [q_mp(5, 36) + s15 / 30, q_mp(2, 9) + s15 / 15, q_mp(5, 36)],
    ]
    a_ops = []
    for ci in nodes:
        qi = wp_pun(z0 + ci * dz, tau, t30, t40, e1) / 4 + c
        a_ops.append(mp.matrix([[0, dz], [-dz * qi, 0]]))
    m6 = mp.zeros(6, 6)
    r6 = mp.zeros(6, 2)
    for si in range(3):
        for r in range(2):
            for col in range(2):
                r6[2 * si + r, col] = a_ops[si][r, col]
                for sj in range(3):
                    val = -amat[si][sj] * a_ops[si][r, col]
                    if si == sj and r == col:
                        val += 1
                    m6[2 * si + r, 2 * sj + col] = val
    k_sol = (m6 ** (-1)) * r6
    out = mp.eye(2)
    for si in range(3):
        out += b_w[si] * k_sol[2 * si: 2 * (si + 1), :]
    return out


def transfer_gl3(z_from: mp.mpc, z_to: mp.mpc, tau: mp.mpc, c: mp.mpc, t30: mp.mpc, t40: mp.mpc, e1: mp.mpc, nsteps: int = 36) -> mp.matrix:
    t_mat = mp.eye(2)
    dz = (z_to - z_from) / nsteps
    for k in range(nsteps):
        t_mat = gl3_step_2x2(z_from + k * dz, dz, tau, c, t30, t40, e1) * t_mat
    return t_mat


def mobius_of_2x2(t_mat: mp.matrix) -> mp.matrix:
    a_m = mp.matrix([[t_mat[1, 1], t_mat[0, 1]], [t_mat[1, 0], t_mat[0, 0]]])
    return a_m / mp.sqrt(a_m[0, 0] * a_m[1, 1] - a_m[0, 1] * a_m[1, 0])


def frobenius_puncture(z: mp.mpc, g2: mp.mpc, g3: mp.mpc, c: mp.mpc, m_ord: int = 64) -> tuple[mp.matrix, mp.mpc]:
    a_w: dict[int, mp.mpc] = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, m_ord // 2 + 2):
        a_w[n] = q_mp(3, (2 * n + 3) * (n - 2)) * sum(a_w[m] * a_w[n - 1 - m] for m in range(1, n - 1))
    q_arr = [mp.mpc(0)] * (m_ord + 1)
    q_arr[0] = c
    for n in range(1, m_ord // 2 + 1):
        q_arr[2 * n] = a_w[n] / 4
    al = [mp.mpc(0)] * (m_ord + 1)
    be = [mp.mpc(0)] * (m_ord + 1)
    al[0] = mp.mpc(1)
    for m in range(1, m_ord + 1):
        al[m] = -sum(q_arr[j] * al[m - 2 - j] for j in range(0, m - 1)) / (m * m)
        be[m] = -(2 * m * al[m] + sum(q_arr[j] * be[m - 2 - j] for j in range(0, m - 1))) / (m * m)
    sz = mp.sqrt(z)
    lz = mp.log(z)
    half = q_mp(1, 2)
    sa = sum(al[m] * (z ** m) for m in range(m_ord + 1))
    sb = sum(be[m] * (z ** m) for m in range(m_ord + 1))
    dsa = sum((m + half) * al[m] * (z ** (m - 1)) for m in range(m_ord + 1))
    dsb = sum((m + half) * be[m] * (z ** (m - 1)) for m in range(m_ord + 1))
    y1 = sz * sa
    dy1 = sz * dsa
    y2 = y1 * lz + sz * sb
    dy2 = dy1 * lz + y1 / z + sz * dsb
    return mp.matrix([[y1, y2], [dy1, dy2]]), sb / sa


def compute_L2_fd(tau_fd: mp.mpc, c_acc: mp.mpc, nsteps: int = 60) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    _, t20, t30, t40 = thetas_pun(mp.mpf(0), tau_fd)
    k_pi = (mp.pi ** 2) / 3
    e1 = k_pi * (t30 ** 4 + t40 ** 4)
    e2 = k_pi * (t20 ** 4 - t40 ** 4)
    e3 = -k_pi * (t20 ** 4 + t30 ** 4)
    g2 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2)
    g3 = 4 * e1 * e2 * e3
    z0 = (1 + tau_fd) / 2
    zs = z0 / 3
    ta = mobius_of_2x2(transfer_gl3(z0, z0 + 1, tau_fd, c_acc, t30, t40, e1, nsteps))
    f_zs, g_loc = frobenius_puncture(zs, g2, g3, c_acc, 64)
    det_f = f_zs[0, 0] * f_zs[1, 1] - f_zs[0, 1] * f_zs[1, 0]
    f_inv = mp.matrix([[f_zs[1, 1], -f_zs[0, 1]], [-f_zs[1, 0], f_zs[0, 0]]]) / det_f
    t_circ = f_zs * mp.matrix([[-1, -2 * mp.pi * I_MP], [0, -1]]) * f_inv
    t_0s = transfer_gl3(z0, zs, tau_fd, c_acc, t30, t40, e1, nsteps)
    det_t = t_0s[0, 0] * t_0s[1, 1] - t_0s[0, 1] * t_0s[1, 0]
    t_s0 = mp.matrix([[t_0s[1, 1], -t_0s[0, 1]], [-t_0s[1, 0], t_0s[0, 0]]]) / det_t
    p0 = mobius_of_2x2(t_s0 * t_circ * t_0s)
    p_fix = (p0[0, 0] - p0[1, 1]) / (2 * p0[1, 0])
    disc = mp.sqrt((ta[0, 0] - ta[1, 1]) ** 2 + 4 * ta[0, 1] * ta[1, 0])
    f1 = (ta[0, 0] - ta[1, 1] + disc) / (2 * ta[1, 0])
    f2 = (ta[0, 0] - ta[1, 1] - disc) / (2 * ta[1, 0])
    s_fac = (f2 - f1) / (f2 - p_fix)
    g_mob = mp.matrix([[1 / s_fac, -f1 / s_fac], [1, -p_fix]])
    g_mob = g_mob / mp.sqrt(g_mob[0, 0] * g_mob[1, 1] - g_mob[0, 1] * g_mob[1, 0])
    if mp.im(g_mob[0, 1] / g_mob[1, 1]) < 0:
        g_mob = mp.matrix([[I_MP, 0], [0, -I_MP]]) * g_mob
    g_inv = mp.matrix([[g_mob[1, 1], -g_mob[0, 1]], [-g_mob[1, 0], g_mob[0, 0]]])
    rp = g_mob * p0 * g_inv
    rp = rp / rp[0, 0]
    lam = abs(mp.re(rp[0, 1]))
    w_zs = t_0s[0, 1] / t_0s[0, 0]
    u_zs = (g_mob[0, 0] * w_zs + g_mob[0, 1]) / (g_mob[1, 0] * w_zs + g_mob[1, 1])
    im_b = mp.im(u_zs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(g_loc))
    l2_val = mp.pi - (2 * mp.pi / lam) * im_b
    return l2_val, lam, mp.re(p0[0, 0] + p0[1, 1])


def solve_accessory_gl3(tau_fd: mp.mpc) -> mp.mpc:
    _, _, t30, t40 = thetas_pun(mp.mpf(0), tau_fd)
    e1 = ((mp.pi ** 2) / 3) * (t30 ** 4 + t40 ** 4)
    z0 = (1 + tau_fd) / 2

    def res(cv: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
        ta = mobius_of_2x2(transfer_gl3(z0, z0 + 1, tau_fd, cv, t30, t40, e1, 24))
        tb = mobius_of_2x2(transfer_gl3(z0, z0 + tau_fd, tau_fd, cv, t30, t40, e1, 24))
        return mp.im(ta[0, 0] + ta[1, 1]), mp.im(tb[0, 0] + tb[1, 1])

    c_cur = mp.mpc(0)
    h = p10_mp(-8)
    for _ in range(12):
        f1, f2 = res(c_cur)
        if max(abs(f1), abs(f2)) < p10_mp(-15):
            break
        f1x, f2x = res(c_cur + h)
        f1y, f2y = res(c_cur + I_MP * h)
        j11, j21 = (f1x - f1) / h, (f2x - f2) / h
        j12, j22 = (f1y - f1) / h, (f2y - f2) / h
        det_j = j11 * j22 - j12 * j21
        c_cur += ((-f1 * j22 + f2 * j12) / det_j) + I_MP * ((-j11 * f2 + j21 * f1) / det_j)
    return c_cur


def reduce_to_fd_with_log(tau: mp.mpc) -> tuple[mp.mpc, mp.mpf]:
    t = tau
    log_shift = mp.mpf(0)
    for _ in range(50):
        k = int(mp.nint(mp.re(t)))
        if k != 0:
            t = t - k
        if abs(t) < mp.mpf(1) - p10_mp(-20):
            log_shift += mp.log(abs(t))
            t = -1 / t
        else:
            break
    return t, log_shift


# ---------------------------------------------------------------------------
# Self-Contained Frame C Yukawa Operator Y_sec(tau, p; L) (B1940 / B1974 / B1982)
# ---------------------------------------------------------------------------
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
UNITS_Q8 = ("1", "i", "j", "k")


def th_frame(n: int, u: mp.mpc, t: mp.mpc) -> mp.mpc:
    q = mp.exp(I_MP * mp.pi * t)
    x = mp.pi * u
    if n == 3:
        return mp.jtheta(3, x, q)
    if n == 4:
        return mp.jtheta(4, x, q)
    q4 = mp.exp(I_MP * mp.pi * t / 4)
    s = x + mp.pi * t / 2
    if n == 2:
        return q4 * mp.exp(I_MP * x) * mp.jtheta(3, s, q)
    return -I_MP * q4 * mp.exp(I_MP * x) * mp.jtheta(4, s, q)


def thc_frame(a: mp.mpf, b: mp.mpf, t: mp.mpc) -> mp.mpc:
    return mp.exp(I_MP * mp.pi * (a * a) * t + 2 * I_MP * mp.pi * a * b) * th_frame(3, a * t + b, t)


def F_u_b1919(u1: Fr, u2: Fr, t: mp.mpc, y: mp.mpf) -> mp.mpf:
    a = u1 % 1
    b = u2 % 1
    x = mp.re(t)
    if a != 0:
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(fr_mp(a)) + mp.digamma(1 - fr_mp(a)))
        zero_row = mp.mpf(0)
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zero_row = y * (mp.pi ** 2) / (mp.sin(mp.pi * fr_mp(b)) ** 2)
    k_max = int(mp.mp.dps * 5 // (int(max(1, mp.floor(2 * mp.pi * y))))) + 18
    tot = mp.mpf(0)
    for k in range(-k_max, k_max + 1):
        m = fr_mp(a) + k
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2 * I_MP * mp.pi * (m * x + fr_mp(u2)))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return first + zero_row + tot


def higgs_triplet_b1974(t: mp.mpc, eta: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    t2 = th_frame(2, mp.mpc(0), t)
    t3 = th_frame(3, mp.mpc(0), t)
    t4 = th_frame(4, mp.mpc(0), t)
    den = 24 * (eta ** 3)
    c0 = -(t2 ** 2) * (t3 ** 4 + t4 ** 4) / den
    c1 = (t4 ** 2) * (t2 ** 4 + t3 ** 4) / den
    c2 = I_MP * (t3 ** 2) * (t2 ** 4 - t4 ** 4) / den
    return c0, c1, c2


def dth1_frame(u: mp.mpc, t: mp.mpc, n_terms: int = 24) -> mp.mpc:
    """Direct Fourier q-series derivative d/du theta_1(u | tau) (period 1 in u, zero branch cuts)."""
    half = q_mp(1, 2)
    acc = mp.mpc(0)
    for n in range(n_terms):
        sgn = -1 if (n & 1) else 1
        qn = mp.exp(I_MP * mp.pi * t * ((mp.mpf(n) + half) ** 2))
        acc += sgn * (2 * n + 1) * qn * mp.cos((2 * n + 1) * mp.pi * u)
    return 2 * mp.pi * acc


_HIGGS_CACHE: dict[tuple[str, str, int], tuple[mp.mpc, mp.mpc, mp.matrix]] = {}


def frame_c_yukawa(t: mp.mpc, a: Fr, b: Fr, sec: str, l_end: mp.mpf) -> mp.matrix:
    y = mp.im(t)
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    eps = qj
    blocks = [qj, qi, qk]
    half = q_mp(1, 2)
    ed = {
        "1": half * qj,
        "i": mp.matrix([[0, half * I_MP], [half * I_MP, 0]]),
        "j": -half * mp.eye(2),
        "k": -half * qi,
    }
    ckey = (mp.nstr(mp.re(t), 30), mp.nstr(mp.im(t), 30), int(mp.mp.dps))
    if ckey in _HIGGS_CACHE:
        eta, t1p, s_mat = _HIGGS_CACHE[ckey]
    else:
        eta = mp.exp(I_MP * mp.pi * t / 12) * mp.qp(mp.exp(2 * I_MP * mp.pi * t))
        t1p = 2 * mp.pi * (eta ** 3)
        c0, c1, c2 = higgs_triplet_b1974(t, eta)
        s_mat = c0 * qi + c1 * qj + c2 * qk
        _HIGGS_CACHE[ckey] = (eta, t1p, s_mat)

    ql, qr = SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]
    x0, x1 = ql * a, 2 * ql * b
    y0, y1 = qr * a, 2 * qr * b
    ap, am = x0 + y0, x0 - y0
    bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
    e_ph = mp.exp(-2 * I_MP * mp.pi * fr_mp(x0))
    kap = {"1": -I_MP * e_ph, "i": mp.mpc(-1), "j": -e_ph, "k": I_MP}
    cs = {"1": (ap + HALF_FR, bp + HALF_FR), "i": (ap + HALF_FR, bp), "j": (ap, bp + HALF_FR), "k": (ap, bp)}
    ds = {"1": (am + HALF_FR, bm + HALF_FR), "i": (am + HALF_FR, bm), "j": (am, bm + HALF_FR), "k": (am, bm)}

    def is_zero_char(ch: tuple[Fr, Fr]) -> bool:
        return (ch[0] - HALF_FR) % 1 == 0 and (ch[1] - HALF_FR) % 1 == 0

    mw = mp.zeros(2, 2)
    for s in UNITS_Q8:
        if is_zero_char(cs[s]) or is_zero_char(ds[s]):
            continue
        r_res = kap[s] * thc_frame(fr_mp(cs[s][0]), fr_mp(cs[s][1]), t) * thc_frame(fr_mp(ds[s][0]), fr_mp(ds[s][1]), t) / t1p
        al, be = cs[s][0] - HALF_FR, cs[s][1] - HALF_FR
        al_red = al - int(mp.nint(fr_mp(al)))
        be_red = be - int(mp.nint(fr_mp(be)))
        z_pt = fr_mp(al_red) * t + fr_mp(be_red)
        a0 = 2 * I_MP * mp.pi * fr_mp(al_red) + dth1_frame(z_pt, t) / th_frame(1, z_pt, t)
        c_val = F_u_b1919(al, be, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
        c_val -= mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
        arg = 2 * mp.pi * l_end + c_val
        if arg > 0:
            mw += (mp.sqrt(arg) * r_res) * ed[s]

    y_out = mp.zeros(3, 3)
    for ia, ca in enumerate(blocks):
        for ib, cb in enumerate(blocks):
            m_prod = ca.T * eps * s_mat * cb
            acc = mp.mpc(0)
            for r_i in range(2):
                for c_i in range(2):
                    acc += m_prod[r_i, c_i] * mw[r_i, c_i]
            y_out[ia, ib] = acc
    return y_out


def yhat_norm(t: mp.mpc, a: Fr, b: Fr, sec: str, l_end: mp.mpf) -> mp.matrix:
    return mp.sqrt(mp.im(t)) * frame_c_yukawa(t, a, b, sec, l_end)


# ---------------------------------------------------------------------------
# Linear Algebra Helpers on 3x3 and (3N)x(3N) mpmath Matrices
# ---------------------------------------------------------------------------
def mat_frob(a_m: mp.matrix) -> mp.mpf:
    s = mp.mpf(0)
    for i in range(a_m.rows):
        for j in range(a_m.cols):
            s += abs(a_m[i, j]) ** 2
    return mp.sqrt(s)


def exp_neg_du_sqrt_yyh(du: mp.mpf, y_m: mp.matrix) -> mp.matrix:
    h_m = y_m * y_m.H
    h_sym = (h_m + h_m.H) / 2
    ev, u_m = mp.eighe(h_sym)
    d_m = mp.zeros(3, 3)
    for i in range(3):
        lam = ev[i] if ev[i] > 0 else mp.mpf(0)
        d_m[i, i] = mp.exp(-du * mp.sqrt(lam))
    return u_m * d_m * u_m.H


def cutfree_floquet_and_eigs(ul_links: list[mp.matrix], y_slices: list[mp.matrix], du: mp.mpf) -> tuple[mp.matrix, list[mp.mpf], mp.matrix]:
    n = len(y_slices)
    steps = [ul_links[j] * exp_neg_du_sqrt_yyh(du, y_slices[j]) for j in range(n)]
    p_trans = [mp.eye(3)]
    for j in range(n - 1):
        p_trans.append(ul_links[j] * p_trans[-1])
    p_hol = ul_links[n - 1] * p_trans[-1]
    assert mat_frob(p_hol - mp.eye(3)) < p10_mp(-20)

    g_avg = mp.zeros(3, 3)
    for j0 in range(n):
        m_j = mp.eye(3)
        for off in range(n):
            m_j = steps[(j0 + off) % n] * m_j
        g_avg += (p_trans[j0].H * (m_j * m_j.H) * p_trans[j0]) / n

    m0 = mp.eye(3)
    for j in range(n):
        m0 = steps[j] * m0
    ev_m0, _ = mp.eig(m0)
    floq_mods = sorted(abs(x) for x in ev_m0)
    return (g_avg + g_avg.H) / 2, floq_mods, m0


def kk_laplace_yukawa(ul_links: list[mp.matrix], y_slices: list[mp.matrix], du: mp.mpf) -> tuple[list[mp.mpf], mp.matrix]:
    n = len(y_slices)
    dim = 3 * n
    h_op = mp.zeros(dim, dim)
    inv_du2 = 1 / (du * du)
    for j in range(n):
        jp = (j + 1) % n
        diag_blk = 2 * inv_du2 * mp.eye(3) + (y_slices[j] * y_slices[j].H)
        hop = -inv_du2 * ul_links[j].H
        for r in range(3):
            for c in range(3):
                h_op[3 * j + r, 3 * j + c] += diag_blk[r, c]
                h_op[3 * j + r, 3 * jp + c] += hop[r, c]
                h_op[3 * jp + r, 3 * j + c] += mp.conj(hop[c, r])
    h_sym = (h_op + h_op.H) / 2
    ev, u_m = mp.eighe(h_sym)
    sv3 = [mp.sqrt(ev[i] if ev[i] > 0 else mp.mpf(0)) for i in range(3)]
    u_light = mp.zeros(dim, 3)
    for r in range(dim):
        for c in range(3):
            u_light[r, c] = u_m[r, c]
    return sv3, u_light


def deterministic_haar_u3(seed_idx: int) -> mp.matrix:
    """Deterministic full-rank complex 3x3 QR unitary (Haar-type basis scrambler, zero floats)."""
    z_m = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            k = 19 * seed_idx + 7 * r + 3 * c + 1
            re_v = mp.sin(mp.mpf(k) * mp.sqrt(2)) + mp.cos(mp.mpf(k * k + 3) * mp.sqrt(3)) / 2
            im_v = mp.cos(mp.mpf(2 * k + 1) * mp.sqrt(5)) - mp.sin(mp.mpf(k + 5) * mp.sqrt(7)) / 2
            z_m[r, c] = re_v + I_MP * im_v
    # Modified Gram-Schmidt in 32-dps:
    cols = []
    for c in range(3):
        v = mp.matrix([z_m[r, c] for r in range(3)])
        for q_prev in cols:
            proj = sum(mp.conj(q_prev[r]) * v[r] for r in range(3))
            v = v - proj * q_prev
        nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
        cols.append(v / nrm)
    u_out = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            u_out[r, c] = cols[c][r]
    return u_out


# ---------------------------------------------------------------------------
# Module WI_1: Cohomological Selection of Order-30's P96 on M_{12} -> m004
# ---------------------------------------------------------------------------
def run_wi_1() -> tuple[dict[str, Any], list[list[tuple[Fr, Fr]]]]:
    e30_exact = sorted(
        (Fr(a, 30), Fr(b, 30))
        for a in range(30)
        for b in range(30)
        if math.lcm(Fr(a, 30).denominator, Fr(b, 30).denominator) == 30
    )
    assert len(e30_exact) == 576

    def mat_mul_mod(x: list[list[int]], y: list[list[int]], mod: int = 30) -> list[list[int]]:
        return [
            [(x[0][0] * y[0][0] + x[0][1] * y[1][0]) % mod, (x[0][0] * y[0][1] + x[0][1] * y[1][1]) % mod],
            [(x[1][0] * y[0][0] + x[1][1] * y[1][0]) % mod, (x[1][0] * y[0][1] + x[1][1] * y[1][1]) % mod],
        ]

    m_act = [[2, 1], [1, 1]]
    cur_m = [[1, 0], [0, 1]]
    ord_m_mod30 = 0
    for step in range(1, 120):
        cur_m = mat_mul_mod(cur_m, m_act, 30)
        if cur_m == [[1, 0], [0, 1]]:
            ord_m_mod30 = step
            break
    assert ord_m_mod30 == 60

    divisors_60 = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
    ker_counts: dict[str, int] = {}
    ker_12_pts: list[tuple[Fr, Fr]] = []
    for k in divisors_60:
        mk = [[1, 0], [0, 1]]
        for _ in range(k):
            mk = mat_mul_mod(mk, m_act, 30)
        fixed = [
            (a, b)
            for (a, b) in e30_exact
            if ((mk[0][0] * a + mk[1][0] * b) % 1, (mk[0][1] * a + mk[1][1] * b) % 1) == (a, b)
        ]
        ker_counts[str(k)] = len(fixed)
        if k == 12:
            ker_12_pts = fixed

    # Construct B1976's P96 = K_5 + E[2]* + E[3]* directly:
    k5 = [(Fr(j, 5), Fr((2 * j) % 5, 5)) for j in range(1, 5)]
    e2_star = [(Fr(i, 2), Fr(j, 2)) for i in range(2) for j in range(2) if (i, j) != (0, 0)]
    e3_star = [(Fr(i, 3), Fr(j, 3)) for i in range(3) for j in range(3) if (i, j) != (0, 0)]
    p96_b1976 = sorted(
        ((p5[0] + p2[0] + p3[0]) % 1, (p5[1] + p2[1] + p3[1]) % 1)
        for p5 in k5
        for p2 in e2_star
        for p3 in e3_star
    )
    assert ker_12_pts == p96_b1976
    assert all(ker_counts[str(k)] == 0 for k in divisors_60 if k not in (12, 60))

    # Partition P96 into 8 closed M-orbits of length 12:
    def row_m(pt: tuple[Fr, Fr]) -> tuple[Fr, Fr]:
        return ((2 * pt[0] + pt[1]) % 1, (pt[0] + pt[1]) % 1)

    orbits: list[list[tuple[Fr, Fr]]] = []
    seen: set[tuple[Fr, Fr]] = set()
    for pt in ker_12_pts:
        if pt in seen:
            continue
        orb = []
        c = pt
        for _ in range(12):
            orb.append(c)
            seen.add(c)
            c = row_m(c)
        assert c == pt and len(set(orb)) == 12
        orbits.append(orb)
    assert len(orbits) == 8

    return {
        "exact_order_30_count": len(e30_exact),
        "ord_M_mod_30": ord_m_mod30,
        "kernel_counts_by_divisor": ker_counts,
        "minimal_nonzero_cover_degree": 12,
        "matches_b1976_p96_count": sum(1 for x, y in zip(ker_12_pts, p96_b1976) if x == y),
        "n_orbits": len(orbits),
        "orbit_lengths": [len(o) for o in orbits],
    }, orbits


# ---------------------------------------------------------------------------
# Module WI_2: Exact Matrix SL(2,Z) Covariance & Cube-Group Representation
# ---------------------------------------------------------------------------
def run_wi_2(p96_orbits: list[list[tuple[Fr, Fr]]]) -> tuple[dict[str, Any], mp.mpf]:
    mp.mp.dps = 32
    l2_i, lam_i, tr_p_i = compute_L2_fd(I_MP, mp.mpc(0), 60)
    omega6 = q_mp(1, 2) + I_MP * mp.sqrt(3) / 2
    l2_omega, lam_omega, tr_p_omega = compute_L2_fd(omega6, mp.mpc(0), 60)
    assert abs(lam_i - 2 * mp.sqrt(2)) < p10_mp(-12)
    assert abs(lam_omega - 6 / mp.sqrt(5)) < p10_mp(-12)
    assert max(abs(tr_p_i + 2), abs(tr_p_omega + 2)) < p10_mp(-25)

    # Explicit 3x3 signed permutation matrices on BLOCKS = [QJ, QI, QK]:
    w_t = mp.matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    w_s = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    # Note R = [[1,0],[1,1]] = S * T^{-1} * S? Check: S*T^{-1}*S = [[0,-1],[1,0]][[1,-1],[0,1]][[0,-1],[1,0]] = [[0,-1],[1,-1]][[0,-1],[1,0]] = [[-1,0],[-1,-1]] = -R!
    # So L = T and R = -S * T^{-1} * S; let us verify W(M) directly against Frame C!
    w_m = mp.matrix([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])
    w_r = w_t.T * w_m  # since M = L*R = T*R => W(R) = W(T)^{-1} W(M)!

    tau0 = q_mp(23, 100) + I_MP * q_mp(147, 100)
    t0_fd, l_sh0 = reduce_to_fd_with_log(tau0)
    c0_acc = solve_accessory_gl3(t0_fd)
    l0_cov = compute_L2_fd(t0_fd, c0_acc, 60)[0] + l_sh0

    gens_cov = {
        "T": ([[1, 1], [0, 1]], w_t),
        "S": ([[0, -1], [1, 0]], w_s),
        "R": ([[1, 0], [1, 1]], w_r),
        "M": ([[2, 1], [1, 1]], w_m),
    }
    max_cov_err = mp.mpf(0)
    max_mod_phase_err = mp.mpf(0)
    for g_name, (g_mat, w_mat) in gens_cov.items():
        ga, gb, gc, gd = g_mat[0][0], g_mat[0][1], g_mat[1][0], g_mat[1][1]
        tau_p = (ga * tau0 + gb) / (gc * tau0 + gd)
        l_p = l0_cov + mp.log(abs(gc * tau0 + gd))
        for orb_i in (0, 3):
            ap, bp = p96_orbits[orb_i][0]
            a_old = (ga * ap + gc * bp) % 1
            b_old = (gb * ap + gd * bp) % 1
            for sec in ("up", "down", "lep"):
                y_old = yhat_norm(tau0, a_old, b_old, sec, l0_cov)
                y_new = yhat_norm(tau_p, ap, bp, sec, l_p)
                y_rot = w_mat * y_old * w_mat.T
                # Extract scalar multiplier c_ph = <y_rot, y_new> / <y_rot, y_rot>:
                num = sum(mp.conj(y_rot[r, c]) * y_new[r, c] for r in range(3) for c in range(3))
                den = sum(abs(y_rot[r, c]) ** 2 for r in range(3) for c in range(3))
                c_ph = num / den
                rel_err = mat_frob(y_new - c_ph * y_rot) / mat_frob(y_new)
                mod_err = abs(abs(c_ph) - 1)
                if rel_err > max_cov_err:
                    max_cov_err = rel_err
                if mod_err > max_mod_phase_err:
                    max_mod_phase_err = mod_err
    assert max_cov_err < p10_mp(-25)
    assert max_mod_phase_err < p10_mp(-25)

    # Planted Control PC_WI_3: Unshifted L(-1/tau) = L(tau) (B1980's end-law error) breaks S-covariance!
    ap0, bp0 = p96_orbits[0][0]
    a_s0, b_s0 = bp0 % 1, (-ap0) % 1
    y_old_pc3 = yhat_norm(tau0, a_s0, b_s0, "up", l0_cov)
    y_bad_pc3 = yhat_norm(-1 / tau0, ap0, bp0, "up", l0_cov)  # missing +ln|tau0|!
    sv_old_pc3 = sorted(mp.sqrt(max(mp.mpf(0), x)) for x in mp.eighe((y_old_pc3 * y_old_pc3.H + (y_old_pc3 * y_old_pc3.H).H) / 2)[0])
    sv_bad_pc3 = sorted(mp.sqrt(max(mp.mpf(0), x)) for x in mp.eighe((y_bad_pc3 * y_bad_pc3.H + (y_bad_pc3 * y_bad_pc3.H).H) / 2)[0])
    unshifted_s_ratio_err = abs((sv_bad_pc3[0] / sv_bad_pc3[2]) - (sv_old_pc3[0] / sv_old_pc3[2])) / (sv_old_pc3[0] / sv_old_pc3[2])
    assert unshifted_s_ratio_err > q_mp(1, 20)

    # Generate exact integer 3x3 matrix groups <W(T), W(S)> and <W(L), W(R)>:
    def to_int_tup(m_mp: mp.matrix) -> tuple[tuple[int, ...], ...]:
        return tuple(tuple(int(mp.nint(mp.re(m_mp[r, c]))) for c in range(3)) for r in range(3))

    def mul_int3(x: tuple[tuple[int, ...], ...], y: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
        return tuple(tuple(sum(x[r][k] * y[k][c] for k in range(3)) for c in range(3)) for r in range(3))

    def gen_grp3(gens: list[tuple[tuple[int, ...], ...]]) -> set[tuple[tuple[int, ...], ...]]:
        id3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        grp = {id3}
        fr_l = [id3]
        while fr_l:
            nxt = []
            for g in fr_l:
                for h in gens:
                    gh = mul_int3(h, g)
                    if gh not in grp:
                        grp.add(gh)
                        nxt.append(gh)
            fr_l = nxt
        return grp

    wt_i, ws_i, wr_i, wm_i = to_int_tup(w_t), to_int_tup(w_s), to_int_tup(w_r), to_int_tup(w_m)
    grp_ts = gen_grp3([wt_i, ws_i])
    grp_lr = gen_grp3([wt_i, wr_i])
    proj_ts = {g if g < tuple(tuple(-x for x in row) for row in g) else tuple(tuple(-x for x in row) for row in g) for g in grp_ts}
    assert len(grp_ts) == 48 and len(proj_ts) == 24 and len(grp_lr) == 24

    wm_pow = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    ord_wm = 0
    for k in range(1, 13):
        wm_pow = mul_int3(wm_pow, wm_i)
        if wm_pow == ((1, 0, 0), (0, 1, 0), (0, 0, 1)) and ord_wm == 0:
            ord_wm = k
    assert ord_wm == 3 and wm_pow == ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    return {
        "L2_at_i": mp.nstr(l2_i, 16),
        "L2_at_omega": mp.nstr(l2_omega, 16),
        "max_matrix_sl2z_rel_err": mp.nstr(max_cov_err, 8),
        "max_weight0_phase_modulus_err": mp.nstr(max_mod_phase_err, 8),
        "order_W_SL2Z_Oh": len(grp_ts),
        "order_projective_Aut_Q8_S4": len(proj_ts),
        "order_chiral_WL_WR_cube": len(grp_lr),
        "order_W_M": ord_wm,
        "pc_wi_3_unshifted_S_ratio_rel_err": mp.nstr(unshifted_s_ratio_err, 8),
    }, l2_i


# ---------------------------------------------------------------------------
# Module WI_3 & WI_4: 3D Mapping-Torus Geodesic Operators, Haar Gate, & P96 Shell
# ---------------------------------------------------------------------------
def run_wi_3_and_4(p96_orbits: list[list[tuple[Fr, Fr]]], l2_i: mp.mpf) -> tuple[dict[str, Any], dict[str, Any], dict[str, bool]]:
    mp.mp.dps = 30
    phi = (1 + mp.sqrt(5)) / 2
    l_per = 4 * mp.log(phi)
    w_m = mp.matrix([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])

    def tau_geod(u_val: mp.mpf) -> mp.mpc:
        eu = mp.exp(u_val)
        return (phi * I_MP * eu - 1 / phi) / (I_MP * eu + 1)

    # Verify exact algebraic identities tau(ln phi) = 1 + i and tau(3 ln phi) = (3 + i)/2:
    u0_n2 = mp.log(phi)
    u1_n2 = 3 * mp.log(phi)
    t_u0 = tau_geod(u0_n2)
    t_u1 = tau_geod(u1_n2)
    geod_id_err = max(abs(t_u0 - (1 + I_MP)), abs(t_u1 - (q_mp(3, 2) + I_MP * q_mp(1, 2))))
    assert geod_id_err < p10_mp(-28)
    taus_n2 = [1 + I_MP, q_mp(3, 2) + I_MP * q_mp(1, 2)]
    ls_n2 = [l2_i, l2_i + mp.log(2) / 2]
    du_n2 = l_per / 2
    n_tot_2 = 24
    ul_base_2 = [w_m if (j % 2 == 1) else mp.eye(3) for j in range(n_tot_2)]

    def build_orbit_slices(p_start: tuple[Fr, Fr], taus_s: list[mp.mpc], ls_s: list[mp.mpf]) -> dict[str, list[mp.matrix]]:
        pts = []
        c = p_start
        for _ in range(12):
            pts.append(c)
            c = ((2 * c[0] + c[1]) % 1, (c[0] + c[1]) % 1)
        assert c == p_start
        out: dict[str, list[mp.matrix]] = {s: [] for s in ("up", "down", "lep")}
        for k in range(12):
            for m_i in range(len(taus_s)):
                for s in ("up", "down", "lep"):
                    out[s].append(yhat_norm(taus_s[m_i], pts[k][0], pts[k][1], s, ls_s[m_i]))
        return out

    # 1. Evaluate all 8 orbits of P96 on N_sub = 2:
    orbit_data: list[dict[str, Any]] = []
    g_shell = {s: mp.zeros(3, 3) for s in ("up", "down", "lep")}
    y_orb0_cache: dict[str, list[mp.matrix]] = {}

    for oi, orb in enumerate(p96_orbits):
        ys = build_orbit_slices(orb[0], taus_n2, ls_n2)
        if oi == 0:
            y_orb0_cache = ys
        sec_res: dict[str, Any] = {}
        u_cf: dict[str, mp.matrix] = {}
        for s in ("up", "down", "lep"):
            g_cf, f_mods, m0_mat = cutfree_floquet_and_eigs(ul_base_2, ys[s], du_n2)
            g_shell[s] += g_cf / 8
            ev_cf, u_mat = mp.eighe(g_cf)
            sv_cf = [mp.sqrt(ev_cf[i] if ev_cf[i] > 0 else mp.mpf(0)) for i in range(3)]
            u_cf[s] = u_mat
            sec_res[s] = {
                "g_cf": g_cf,
                "sv_cf": sv_cf,
                "ratios_cf": (sv_cf[0] / sv_cf[2], sv_cf[1] / sv_cf[2]),
                "ratios_floq_mod": (f_mods[0] / f_mods[2], f_mods[1] / f_mods[2]),
                "m0_mat": m0_mat,
            }
        v_ckm = u_cf["up"].H * u_cf["down"]
        v_abs = mp.matrix([[abs(v_ckm[r, c]) for c in range(3)] for r in range(3)])
        diag_min = min(v_abs[0, 0], v_abs[1, 1], v_abs[2, 2])
        orbit_data.append({
            "orbit_index": oi,
            "rep": [str(orb[0][0]), str(orb[0][1])],
            "sectors": sec_res,
            "ckm_abs": v_abs,
            "diag_min": diag_min,
            "v12": v_abs[0, 1],
            "v23": v_abs[1, 2],
        })

    # Also compute 72x72 KK Laplace-Yukawa on Orbit 0 + mandatory 72-matrix Haar & Orbit-Shift gates!
    sv_kk_0: dict[str, list[mp.mpf]] = {}
    u_kk_0: dict[str, mp.matrix] = {}
    for s in ("up", "down", "lep"):
        sv_kk_0[s], u_kk_0[s] = kk_laplace_yukawa(ul_base_2, y_orb0_cache[s], du_n2)
    v_kk_0 = u_kk_0["up"].H * u_kk_0["down"]
    v_kk_0_abs = mp.matrix([[abs(v_kk_0[r, c]) for c in range(3)] for r in range(3)])

    # 72 independent local U(3) basis scramblers (24 left GL + 24 GR_u + 24 GR_d):
    gl_scr = [deterministic_haar_u3(100 + j) for j in range(n_tot_2)]
    gru_scr = [deterministic_haar_u3(200 + j) for j in range(n_tot_2)]
    grd_scr = [deterministic_haar_u3(300 + j) for j in range(n_tot_2)]
    ul_scr = [gl_scr[(j + 1) % n_tot_2] * ul_base_2[j] * gl_scr[j].H for j in range(n_tot_2)]
    yu_scr = [gl_scr[j] * y_orb0_cache["up"][j] * gru_scr[j].H for j in range(n_tot_2)]
    yd_scr = [gl_scr[j] * y_orb0_cache["down"][j] * grd_scr[j].H for j in range(n_tot_2)]

    gu_s, fu_s, _ = cutfree_floquet_and_eigs(ul_scr, yu_scr, du_n2)
    gd_s, _, _ = cutfree_floquet_and_eigs(ul_scr, yd_scr, du_n2)
    eu_s, uu_s = mp.eighe(gu_s)
    ed_s, ud_s = mp.eighe(gd_s)
    v_cf_s = uu_s.H * ud_s
    sv_kk_u_s, u_kk_u_s = kk_laplace_yukawa(ul_scr, yu_scr, du_n2)
    _, u_kk_d_s = kk_laplace_yukawa(ul_scr, yd_scr, du_n2)
    v_kk_s = u_kk_u_s.H * u_kk_d_s

    eu_0 = [x ** 2 for x in orbit_data[0]["sectors"]["up"]["sv_cf"]]
    v_cf_0 = orbit_data[0]["ckm_abs"]
    haar_cf_eig_err = max(abs(eu_s[i] - eu_0[i]) for i in range(3)) / eu_0[2]
    haar_cf_ckm_err = max(abs(abs(v_cf_s[r, c]) - v_cf_0[r, c]) for r in range(3) for c in range(3))
    haar_fm_err = max(abs((fu_s[0] / fu_s[2]) - orbit_data[0]["sectors"]["up"]["ratios_floq_mod"][0]),
                      abs((fu_s[1] / fu_s[2]) - orbit_data[0]["sectors"]["up"]["ratios_floq_mod"][1]))
    haar_kk_sv_err = max(abs(sv_kk_u_s[i] - sv_kk_0["up"][i]) for i in range(3))
    haar_kk_ckm_err = max(abs(abs(v_kk_s[r, c]) - v_kk_0_abs[r, c]) for r in range(3) for c in range(3))
    max_haar_err = max(haar_cf_eig_err, haar_cf_ckm_err, haar_fm_err, haar_kk_sv_err, haar_kk_ckm_err)
    assert max_haar_err < p10_mp(-18)

    # Cyclic orbit shift p_0 -> p_0 * M (shift by 2 slices):
    ul_sh = ul_base_2[2:] + ul_base_2[:2]
    yu_sh = y_orb0_cache["up"][2:] + y_orb0_cache["up"][:2]
    yd_sh = y_orb0_cache["down"][2:] + y_orb0_cache["down"][:2]
    gu_h, fu_h, m0_sh = cutfree_floquet_and_eigs(ul_sh, yu_sh, du_n2)
    gd_h, _, _ = cutfree_floquet_and_eigs(ul_sh, yd_sh, du_n2)
    eu_h, uu_h = mp.eighe(gu_h)
    _, ud_h = mp.eighe(gd_h)
    v_cf_h = uu_h.H * ud_h
    sv_kk_u_h, u_kk_u_h = kk_laplace_yukawa(ul_sh, yu_sh, du_n2)
    _, u_kk_d_h = kk_laplace_yukawa(ul_sh, yd_sh, du_n2)
    v_kk_h = u_kk_u_h.H * u_kk_d_h

    shift_cf_err = max(
        max(abs(eu_h[i] - eu_0[i]) for i in range(3)) / eu_0[2],
        max(abs(abs(v_cf_h[r, c]) - v_cf_0[r, c]) for r in range(3) for c in range(3)),
        max(abs(sv_kk_u_h[i] - sv_kk_0["up"][i]) for i in range(3)),
        max(abs(abs(v_kk_h[r, c]) - v_kk_0_abs[r, c]) for r in range(3) for c in range(3)),
    )
    assert shift_cf_err < p10_mp(-18)

    # Planted Control PC_WI_1: Naive un-transported Floquet operator (fixing UL = I_3 without parallel-transporting links)!
    ul_id_2 = [mp.eye(3) for _ in range(n_tot_2)]
    gu_naive_b, _, _ = cutfree_floquet_and_eigs(ul_id_2, y_orb0_cache["up"], du_n2)
    gu_naive_s, _, _ = cutfree_floquet_and_eigs(ul_id_2, yu_scr, du_n2)
    ev_nb, _ = mp.eighe(gu_naive_b)
    ev_ns, _ = mp.eighe(gu_naive_s)
    r_naive_base = mp.sqrt(max(mp.mpf(0), ev_nb[0]) / ev_nb[2])
    r_naive_scr = mp.sqrt(max(mp.mpf(0), ev_ns[0]) / ev_ns[2])
    pc1_haar_violation = abs(r_naive_scr - r_naive_base) / max(r_naive_base, r_naive_scr)
    assert pc1_haar_violation > q_mp(1, 5)

    # Planted Control PC_WI_2: Single-cut svd(M_loop(j0=0)) fails cyclic orbit-shift invariance!
    m0_base = orbit_data[0]["sectors"]["up"]["m0_mat"]
    ev_m0_b, _ = mp.eighe((m0_base * m0_base.H + (m0_base * m0_base.H).H) / 2)
    ev_m0_s, _ = mp.eighe((m0_sh * m0_sh.H + (m0_sh * m0_sh.H).H) / 2)
    r_cut_b = mp.sqrt(max(mp.mpf(0), ev_m0_b[0]) / ev_m0_b[2])
    r_cut_s = mp.sqrt(max(mp.mpf(0), ev_m0_s[0]) / ev_m0_s[2])
    pc2_shift_violation = abs(r_cut_s - r_cut_b) / max(r_cut_b, r_cut_s)
    assert pc2_shift_violation > q_mp(1, 5)

    # Continuum convergence check N_sub = 4 (48 slices around M_{12}) on Orbit 0:
    taus_n4 = [tau_geod((mp.mpf(m) + q_mp(1, 2)) * mp.log(phi)) for m in range(4)]
    t4_fd0, l4_sh0 = reduce_to_fd_with_log(taus_n4[0])
    c4_acc0 = solve_accessory_gl3(t4_fd0)
    l2_t4_0 = compute_L2_fd(t4_fd0, c4_acc0, 60)[0]
    # Note taus_n4[2], taus_n4[3] reduce to -conj(t4_fd0), where L_2(-conj(tau)) == L_2(tau)! Verify directly:
    ls_n4 = []
    for m in range(4):
        tf_m, lsh_m = reduce_to_fd_with_log(taus_n4[m])
        assert min(abs(tf_m - t4_fd0), abs(tf_m - (-mp.conj(t4_fd0)))) < p10_mp(-20)
        ls_n4.append(l2_t4_0 + lsh_m)
    du_n4 = l_per / 4
    ul_base_4 = [w_m if (j % 4 == 3) else mp.eye(3) for j in range(48)]
    ys_n4_orb0 = build_orbit_slices(p96_orbits[0][0], taus_n4, ls_n4)
    gu_n4, _, _ = cutfree_floquet_and_eigs(ul_base_4, ys_n4_orb0["up"], du_n4)
    gd_n4, _, _ = cutfree_floquet_and_eigs(ul_base_4, ys_n4_orb0["down"], du_n4)
    eu_n4, uu_n4 = mp.eighe(gu_n4)
    ed_n4, ud_n4 = mp.eighe(gd_n4)
    ru_n4 = (mp.sqrt(eu_n4[0] / eu_n4[2]), mp.sqrt(eu_n4[1] / eu_n4[2]))
    rd_n4 = (mp.sqrt(ed_n4[0] / ed_n4[2]), mp.sqrt(ed_n4[1] / ed_n4[2]))
    v_n4 = uu_n4.H * ud_n4
    diag_n4 = min(abs(v_n4[0, 0]), abs(v_n4[1, 1]), abs(v_n4[2, 2]))

    # Deck-Commutant CKM Lock Theorem on Odd Levels P5 and P15 (Planted Control PC_WI_4):
    deck_lock_results: dict[str, Any] = {}
    for lvl_lbl, pt_odd in [("P5", (Fr(1, 5), Fr(2, 5))), ("P15", (Fr(8, 15), Fr(2, 5)))]:
        ys_odd = build_orbit_slices(pt_odd, taus_n2, ls_n2)
        u_odd: dict[str, mp.matrix] = {}
        max_comm = mp.mpf(0)
        sv_odd: dict[str, tuple[mp.mpf, mp.mpf]] = {}
        for s in ("up", "down", "lep"):
            g_o, _, _ = cutfree_floquet_and_eigs(ul_base_2, ys_odd[s], du_n2)
            comm_nrm = mat_frob(g_o * w_m - w_m * g_o) / mat_frob(g_o)
            if comm_nrm > max_comm:
                max_comm = comm_nrm
            ev_o, u_o = mp.eighe(g_o)
            u_odd[s] = u_o
            sv_odd[s] = (mp.sqrt(ev_o[0] / ev_o[2]), mp.sqrt(ev_o[1] / ev_o[2]))
        v_odd = u_odd["up"].H * u_odd["down"]
        # Since [G_u, W_M] = [G_d, W_M] = 0 and W_M has 3 distinct eigenvalues, V_odd is a permutation matrix (here I_3 up to sorting):
        off_diag_max = max(
            min(abs(v_odd[r, 0]), abs(v_odd[r, 1]) + abs(v_odd[r, 2]))
            for r in range(3)
        )
        # More directly: in each row of |V_odd|, the maximum entry is 1 to < 10^-20, so the sum of the OTHER two entries is < 10^-20!
        max_non_perm = max(abs(1 - max(abs(v_odd[r, c]) for c in range(3))) for r in range(3))
        assert max_comm < p10_mp(-22) and max_non_perm < p10_mp(-20)
        deck_lock_results[lvl_lbl] = {
            "max_commutator_with_WM": mp.nstr(max_comm, 8),
            "max_deviation_from_zero_mixing": mp.nstr(max_non_perm, 8),
            "up_ratios_cf": [mp.nstr(sv_odd["up"][0], 10), mp.nstr(sv_odd["up"][1], 10)],
            "down_ratios_cf": [mp.nstr(sv_odd["down"][0], 10), mp.nstr(sv_odd["down"][1], 10)],
            "lep_ratios_cf": [mp.nstr(sv_odd["lep"][0], 10), mp.nstr(sv_odd["lep"][1], 10)],
        }

    # Check kappa = 2 projector-averaging upward drift on Orbit 0:
    gu_k2, _, _ = cutfree_floquet_and_eigs(ul_base_2, y_orb0_cache["up"], 2 * du_n2)
    eu_k2, _ = mp.eighe(gu_k2)
    ru_k2_0 = mp.sqrt(eu_k2[0] / eu_k2[2])
    assert ru_k2_0 > orbit_data[0]["sectors"]["up"]["ratios_cf"][0]

    # Module WI_4: Inversion (-I_2) & Amphicheiral (Q_0 = [[-1,0],[1,1]]) Reduction of the 8 Orbits + 96-Point Shell:
    q0 = [[-1, 0], [1, 1]]
    assert q0[0][0] * q0[1][1] - q0[0][1] * q0[1][0] == -1

    def find_orb_idx(pt: tuple[Fr, Fr]) -> int:
        for idx, o in enumerate(p96_orbits):
            if pt in o:
                return idx
        raise AssertionError("Point not in P96!")

    inv_map: dict[int, int] = {}
    amph_map: dict[int, int] = {}
    max_pair_diff = mp.mpf(0)
    for oi, orb in enumerate(p96_orbits):
        p0 = orb[0]
        inv_map[oi] = find_orb_idx(((-p0[0]) % 1, (-p0[1]) % 1))
        amph_map[oi] = find_orb_idx(((q0[0][0] * p0[0] + q0[1][0] * p0[1]) % 1, (q0[0][1] * p0[0] + q0[1][1] * p0[1]) % 1))
        oj = inv_map[oi]
        assert oj != oi
        for s in ("up", "down", "lep"):
            r_i = orbit_data[oi]["sectors"][s]["ratios_cf"]
            r_j = orbit_data[oj]["sectors"][s]["ratios_cf"]
            d_ij = max(abs(r_i[0] - r_j[0]), abs(r_i[1] - r_j[1]))
            if d_ij > max_pair_diff:
                max_pair_diff = d_ij
    assert max_pair_diff < p10_mp(-22)
    amph_fixed_orbits = [oi for oi in range(8) if amph_map[oi] == oi]
    assert amph_fixed_orbits == [0, 2, 3, 4]

    # Full 96-point shell spectrum:
    u_sh: dict[str, mp.matrix] = {}
    r_sh: dict[str, list[str]] = {}
    for s in ("up", "down", "lep"):
        ev_sh, umat_sh = mp.eighe((g_shell[s] + g_shell[s].H) / 2)
        u_sh[s] = umat_sh
        r_sh[s] = [mp.nstr(mp.sqrt(ev_sh[0] / ev_sh[2]), 10), mp.nstr(mp.sqrt(ev_sh[1] / ev_sh[2]), 10)]
    v_sh = u_sh["up"].H * u_sh["down"]
    diag_sh = min(abs(v_sh[0, 0]), abs(v_sh[1, 1]), abs(v_sh[2, 2]))

    wi3_out = {
        "geodesic_midpoint_identity_err": mp.nstr(geod_id_err, 8),
        "max_72_haar_scrambling_err": mp.nstr(max_haar_err, 8),
        "max_orbit_shift_err": mp.nstr(shift_cf_err, 8),
        "orbit_0_cutfree_floquet": {
            "up_ratios": [mp.nstr(x, 12) for x in orbit_data[0]["sectors"]["up"]["ratios_cf"]],
            "down_ratios": [mp.nstr(x, 12) for x in orbit_data[0]["sectors"]["down"]["ratios_cf"]],
            "lep_ratios": [mp.nstr(x, 12) for x in orbit_data[0]["sectors"]["lep"]["ratios_cf"]],
            "ckm_diag_min": mp.nstr(orbit_data[0]["diag_min"], 12),
            "ckm_v12": mp.nstr(orbit_data[0]["v12"], 12),
            "ckm_v23": mp.nstr(orbit_data[0]["v23"], 12),
        },
        "orbit_0_floquet_moduli_up_ratios": [mp.nstr(x, 12) for x in orbit_data[0]["sectors"]["up"]["ratios_floq_mod"]],
        "orbit_0_kk_72x72": {
            "up_ratios": [mp.nstr(sv_kk_0["up"][0] / sv_kk_0["up"][2], 12), mp.nstr(sv_kk_0["up"][1] / sv_kk_0["up"][2], 12)],
            "down_ratios": [mp.nstr(sv_kk_0["down"][0] / sv_kk_0["down"][2], 12), mp.nstr(sv_kk_0["down"][1] / sv_kk_0["down"][2], 12)],
            "lep_ratios": [mp.nstr(sv_kk_0["lep"][0] / sv_kk_0["lep"][2], 12), mp.nstr(sv_kk_0["lep"][1] / sv_kk_0["lep"][2], 12)],
            "ckm_diag_min": mp.nstr(min(v_kk_0_abs[0, 0], v_kk_0_abs[1, 1], v_kk_0_abs[2, 2]), 12),
        },
        "orbit_0_continuum_nsub4_48slices": {
            "up_ratios": [mp.nstr(ru_n4[0], 12), mp.nstr(ru_n4[1], 12)],
            "down_ratios": [mp.nstr(rd_n4[0], 12), mp.nstr(rd_n4[1], 12)],
            "ckm_diag_min": mp.nstr(diag_n4, 12),
        },
        "orbit_0_kappa2_up_ratio_0": mp.nstr(ru_k2_0, 10),
        "odd_level_deck_commutant_ckm_lock": deck_lock_results,
        "pc_wi_1_naive_untransported_haar_err": mp.nstr(pc1_haar_violation, 8),
        "pc_wi_2_single_cut_orbit_shift_err": mp.nstr(pc2_shift_violation, 8),
    }

    wi4_out = {
        "inversion_orbit_pairing": {str(k): v for k, v in inv_map.items()},
        "amphicheiral_Q0_orbit_map": {str(k): v for k, v in amph_map.items()},
        "amphicheiral_fixed_orbits": amph_fixed_orbits,
        "max_inversion_pair_spectral_diff": mp.nstr(max_pair_diff, 8),
        "four_pair_summary": [
            {
                "pair": [oi, inv_map[oi]],
                "amphicheiral_self_conjugate": (amph_map[oi] == oi),
                "up_ratios": [mp.nstr(x, 10) for x in orbit_data[oi]["sectors"]["up"]["ratios_cf"]],
                "down_ratios": [mp.nstr(x, 10) for x in orbit_data[oi]["sectors"]["down"]["ratios_cf"]],
                "lep_ratios": [mp.nstr(x, 10) for x in orbit_data[oi]["sectors"]["lep"]["ratios_cf"]],
                "ckm_diag_min": mp.nstr(orbit_data[oi]["diag_min"], 10),
                "ckm_v23": mp.nstr(orbit_data[oi]["v23"], 10),
            }
            for oi in (0, 1, 3, 5)
        ],
        "full_96_point_shell": {
            "up_ratios": r_sh["up"],
            "down_ratios": r_sh["down"],
            "lep_ratios": r_sh["lep"],
            "ckm_diag_min": mp.nstr(diag_sh, 10),
        },
    }

    pc_flags = {
        "PC_WI_1_naive_product_caught_by_haar_gate": bool(pc1_haar_violation > q_mp(1, 5) and max_haar_err < p10_mp(-12)),
        "PC_WI_2_single_cut_caught_by_orbit_shift_gate": bool(pc2_shift_violation > q_mp(1, 5) and shift_cf_err < p10_mp(-12)),
        "PC_WI_4_odd_level_p5_p15_zero_ckm_caught": bool(
            mp.mpf(deck_lock_results["P5"]["max_deviation_from_zero_mixing"]) < p10_mp(-20)
            and orbit_data[0]["v12"] > q_mp(1, 20)
        ),
    }
    return wi3_out, wi4_out, pc_flags


# ---------------------------------------------------------------------------
# Module WI_5: Exact SL(2, Z[omega]) Spinor Decay & Order-3 Churn on 8^3_4
# ---------------------------------------------------------------------------
def run_wi_5() -> dict[str, Any]:
    mp.mp.dps = 32
    sq3 = mp.sqrt(3)
    om = q_mp(-1, 2) + I_MP * sq3 / 2
    a_mat = mp.matrix([[1, 1], [0, 1]])
    b_mat = mp.matrix([[1, 0], [-om, 1]])
    gens = {
        "a": a_mat,
        "A": mp.matrix([[1, -1], [0, 1]]),
        "b": b_mat,
        "B": mp.matrix([[1, 0], [om, 1]]),
    }
    rel_m004 = "aBAbaBabAB"

    def ev_word(w: str, chi_flip: bool = False) -> mp.matrix:
        cur = mp.eye(2)
        for ch in w:
            step = -gens[ch] if chi_flip else gens[ch]
            cur = cur * step
        return cur

    # Verify Riley lift rho_1 and twisted lift rho_0 both satisfy relator == +I_2 in SL(2,C):
    assert mat_frob(ev_word(rel_m004, False) - mp.eye(2)) < p10_mp(-28)
    assert mat_frob(ev_word(rel_m004, True) - mp.eye(2)) < p10_mp(-28)

    # BFS for canonical null-homologous longitude word (exp_sum == 0, M[1,0] == 0, Im M[0,1] != 0):
    inv_c = {"a": "A", "A": "a", "b": "B", "B": "b"}
    l_word = ""
    bfs = [("", mp.eye(2), 0)]
    for _ in range(10):
        nxt = []
        for w, m_c, es in bfs:
            for ch in ("a", "A", "b", "B"):
                if w and ch == inv_c[w[-1]]:
                    continue
                nw = w + ch
                nm = m_c * gens[ch]
                nes = es + (1 if ch in ("a", "b") else -1)
                if nes == 0 and abs(nm[1, 0]) < p10_mp(-26) and abs(mp.im(nm[0, 1])) > q_mp(1, 10):
                    l_word = nw
                    break
                nxt.append((nw, nm, nes))
            if l_word:
                break
        if l_word:
            break
        bfs = nxt
    assert l_word == "bABaaBAb"

    # Find the irregular D_5 degree-5 cover 8^3_4 (|G| = 10, pa = (0,4,3,2,1)):
    def p_mul(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(p[q[i]] for i in range(5))

    def p_inv(p: tuple[int, ...]) -> tuple[int, ...]:
        r = [0] * 5
        for i, x in enumerate(p):
            r[x] = i
        return tuple(r)

    def ev_perm(w: str, pa: tuple[int, ...], pb: tuple[int, ...]) -> tuple[int, ...]:
        mp_p = {"a": pa, "A": p_inv(pa), "b": pb, "B": p_inv(pb)}
        cur = (0, 1, 2, 3, 4)
        for ch in w:
            cur = p_mul(cur, mp_p[ch])
        return cur

    pa_d5 = (0, 4, 3, 2, 1)
    pb_d5: tuple[int, ...] | None = None
    for cand in itertools.permutations(range(5)):
        if ev_perm(rel_m004, pa_d5, cand) == (0, 1, 2, 3, 4):
            grp = {(0, 1, 2, 3, 4)}
            fr_q = [(0, 1, 2, 3, 4)]
            while fr_q:
                nx = []
                for g in fr_q:
                    for h in (pa_d5, cand, p_inv(pa_d5), p_inv(cand)):
                        gh = p_mul(h, g)
                        if gh not in grp:
                            grp.add(gh)
                            nx.append(gh)
                fr_q = nx
            if len(grp) == 10 and len({g[0] for g in grp}) == 5:
                pb_d5 = cand
                break
    assert pb_d5 is not None
    pl_d5 = ev_perm(l_word, pa_d5, pb_d5)
    assert pl_d5 == (0, 1, 2, 3, 4)  # canonical longitude lifts with degree 1 on all 5 sheets!

    # Compute exact spinor peripheral traces and cusp heights on all 3 cusps of 8^3_4 (sheets 0, {1,4}, {2,3}):
    cusp_reps = [(0, 1), (1, 2), (2, 2)]
    cusp_records = []
    for sh0, m_deg in cusp_reps:
        # Verify sheet orbit under <pa_d5, pl_d5>:
        assert (pa_d5[sh0] == sh0 if m_deg == 1 else pa_d5[pa_d5[sh0]] == sh0 and pa_d5[sh0] != sh0)
        mu_w = "a" * m_deg
        lam_w = l_word
        m_rho1 = ev_word(mu_w, False)
        l_rho1 = ev_word(lam_w, False)
        m_rho0 = ev_word(mu_w, True)
        l_rho0 = ev_word(lam_w, True)
        tr_rho1 = [int(mp.nint(mp.re(m_rho1[0, 0] + m_rho1[1, 1]))), int(mp.nint(mp.re(l_rho1[0, 0] + l_rho1[1, 1])))]
        tr_rho0 = [int(mp.nint(mp.re(m_rho0[0, 0] + m_rho0[1, 1]))), int(mp.nint(mp.re(l_rho0[0, 0] + l_rho0[1, 1])))]
        # Exact cusp modulus tau_F from parabolic translations (guarding sign of diagonal -1):
        t_mu = m_rho1[0, 1] * (1 if mp.re(m_rho1[0, 0]) > 0 else -1)
        t_lam = l_rho1[0, 1] * (1 if mp.re(l_rho1[0, 0]) > 0 else -1)
        if mp.im(t_lam / t_mu) < 0:
            t_lam = -t_lam
        tau_c_fd, _ = reduce_to_fd_with_log(t_lam / t_mu)
        # Non-Lie exponential L^2 spinor decay holds iff (tr_mu, tr_lam) != (+2, +2):
        l2_decay_both = (tr_rho1 != [2, 2]) and (tr_rho0 != [2, 2])
        assert l2_decay_both
        cusp_records.append({
            "sheet_rep": sh0,
            "cusp_degree": m_deg,
            "im_tau_F": mp.nstr(mp.im(tau_c_fd), 14),
            "spin_traces_rho1": tr_rho1,
            "spin_traces_rho0": tr_rho0,
            "exponential_l2_spinor_decay": l2_decay_both,
        })

    # Verify interior meridian lifts W(M)^1 and W(M)^2 both have exact order 3:
    w_m = mp.matrix([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])
    w_m2 = w_m * w_m

    def mat_ord3(x_m: mp.matrix) -> int:
        c_m = mp.eye(3)
        for k in range(1, 10):
            c_m = c_m * x_m
            if mat_frob(c_m - mp.eye(3)) < p10_mp(-28):
                return k
        raise AssertionError("Order >= 10")

    ord_wm1 = mat_ord3(w_m)
    ord_wm2 = mat_ord3(w_m2)
    assert ord_wm1 == 3 and ord_wm2 == 3

    return {
        "canonical_longitude_word": l_word,
        "longitude_perm_on_8_3_4": list(pl_d5),
        "cusps_8_3_4": cusp_records,
        "order_interior_holonomy_deg1_WM": ord_wm1,
        "order_interior_holonomy_deg2_WM2": ord_wm2,
    }


def main() -> None:
    ast_audit = assert_ast_clean(SELF_PATH)
    wi1, p96_orbits = run_wi_1()
    wi2, l2_i = run_wi_2(p96_orbits)
    wi3, wi4, pc_34 = run_wi_3_and_4(p96_orbits, l2_i)
    wi5 = run_wi_5()

    planted_controls = {
        "PC_WI_1_naive_product_caught_by_haar_gate": pc_34["PC_WI_1_naive_product_caught_by_haar_gate"],
        "PC_WI_2_single_cut_caught_by_orbit_shift_gate": pc_34["PC_WI_2_single_cut_caught_by_orbit_shift_gate"],
        "PC_WI_3_unshifted_S_end_law_caught": bool(mp.mpf(wi2["pc_wi_3_unshifted_S_ratio_rel_err"]) > q_mp(1, 20)),
        "PC_WI_4_odd_level_p5_p15_zero_ckm_caught": pc_34["PC_WI_4_odd_level_p5_p15_zero_ckm_caught"],
    }
    assert all(planted_controls.values())

    payload: dict[str, Any] = {
        "claim_id": "CLAIM_2026-11-25_whole_instrument_m12_covariance_and_cube_churn",
        "firewall": "strictly_0_of_19",
        "script_sha256": hashlib.sha256(SELF_PATH.read_bytes()).hexdigest(),
        "ast_audit": ast_audit,
        "WI_1_m12_cohomology_p96": wi1,
        "WI_2_matrix_sl2z_cube_covariance": wi2,
        "WI_3_3d_geodesic_operators_and_churn": wi3,
        "WI_4_p96_orbit_reduction_and_shell": wi4,
        "WI_5_8_3_4_three_cusp_spinor_and_churn": wi5,
        "planted_controls": planted_controls,
        "all_modules_and_controls_pass": True,
    }
    assert_no_json_floats(payload)
    OUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: verify_x_whole_instrument.py completed with 0 AST floats and 4/4 planted controls caught.")


if __name__ == "__main__":
    main()
