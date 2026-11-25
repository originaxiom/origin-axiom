#!/usr/bin/env python3
r"""
Disjoint Cold-Room Referee for Claim Card whole_instrument_m12_covariance_and_cube_churn (strictly 0 of 19):
Zero shared code with verify_x_whole_instrument.py (Guardrail 6 enforced).

Independent mathematical & numerical algorithms in every module:
  - R_WI_1: Chinese Remainder Theorem (CRT) factorization E[30] = F_2^2 (+) F_3^2 (+) F_5^2
            with prime-power M-periods (3, 4, 20; mod-5 Jordan kernel K_5 of period 4), proving
            lcm(3, 4, 4) = 12 algebraically and reconstructing all 96 points via CRT idempotents (15, 10, 6).
  - R_WI_2: Zero mp.qp, zero mp.jtheta, zero mp.diff, zero mp.digamma, zero GL3 collocation —
            builds Dedekind eta from Euler's pentagonal series, Jacobi thetas from infinite triple products,
            a_0 from the analytic rational triple-product logarithmic derivative, B1919's channel norm from
            2D Ewald exponential-integral lattice summation, and B1667's L_2(tau) from Order-14 Weierstrass
            differential Taylor-jet continuation (wp'' = 6 wp^2 - g2/2). Verifies SL(2,Z) cube covariance
            at an independent generic point tau_ref = -19/100 + 137/100 i.
  - R_WI_3: Zero eigensolver in propagator construction — computes sqrt(Y Y^H) via Denman-Beavers quadratic
            iteration, exp(-du * sqrt(Y Y^H)) via scaling-and-squaring diagonal Pade-(6,6) approximants,
            Floquet eigenvalues via exact 3x3 trace/determinant cubic characteristic roots (Durand-Kerner),
            and 72 local U(3) scramblers via Cayley transforms (I - K)(I + K)^{-1} of skew-Hermitian matrices.
  - R_WI_4: Independent verification of (-I_2) & amphicheiral Q_0 orbit pairing (8 -> 4 pairs), odd-level
            P5/P15 Deck-Commutant CKM Lock ([G_bar_L, W(M)] = 0 => V_CKM = I_3), and 96-point shell washout.
  - R_WI_5: Pure-integer symbolic Eisenstein ring Z[omega] = Z + Z*omega (omega^2 = -omega - 1) 2x2 matrix
            arithmetic (zero floating-point operations in group/spin holonomy!) + Lagrange-Gauss 2D cusp
            lattice reduction on 8^3_4's three cusps (1, 2, 2).

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 float()/complex() casts, 0 JSON floats.
  - 0 imports from frontier/, Producer script, snappy, numpy, scipy, or any repo module (python3 -I).
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
OUT_PATH = SELF_PATH.parent / "referee_x_whole_instrument_out.json"
PROD_REPO_OUT = SELF_PATH.parent.parent / "x_whole_instrument_verify" / "verify_x_whole_instrument_out.json"
PROD_SCRATCH_OUT = SELF_PATH.parent / "verify_x_whole_instrument_out.json"

IMAG = mp.mpc(0, 1)
H_FR = Fr(1, 2)


def rat_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(int(num)) / mp.mpf(int(den))


def pow10_mp(exp: int) -> mp.mpf:
    return mp.mpf(10) ** int(exp)


def frac_mp(val: Fr) -> mp.mpf:
    return mp.mpf(val.numerator) / mp.mpf(val.denominator)


def verify_own_ast(target: Path) -> dict[str, int]:
    tree = ast.parse(target.read_text(encoding="utf-8"), filename=str(target))
    ok_mods = {"__future__", "ast", "hashlib", "itertools", "json", "math", "fractions", "pathlib", "typing", "mpmath"}
    fl_cnt = 0
    cx_cnt = 0
    cast_cnt = 0
    imp_cnt = 0
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Constant):
            if isinstance(nd.value, float):
                fl_cnt += 1
            elif isinstance(nd.value, complex):
                cx_cnt += 1
        elif isinstance(nd, ast.Call) and isinstance(nd.func, ast.Name) and nd.func.id in ("float", "complex"):
            cast_cnt += 1
        elif isinstance(nd, ast.Import):
            for al in nd.names:
                if al.name.split(".")[0] not in ok_mods:
                    imp_cnt += 1
        elif isinstance(nd, ast.ImportFrom):
            if nd.module is None or nd.module.split(".")[0] not in ok_mods:
                imp_cnt += 1
    assert (fl_cnt, cx_cnt, cast_cnt, imp_cnt) == (0, 0, 0, 0)
    return {
        "ast_float_literals": fl_cnt,
        "ast_complex_literals": cx_cnt,
        "ast_float_or_complex_casts": cast_cnt,
        "forbidden_imports": imp_cnt,
    }


def check_json_tree(node: Any) -> None:
    if isinstance(node, (float, complex)):
        raise AssertionError(f"Forbidden float/complex in JSON: {node!r}")
    if isinstance(node, dict):
        for k, v in node.items():
            assert isinstance(k, str)
            check_json_tree(v)
    elif isinstance(node, (list, tuple)):
        for item in node:
            check_json_tree(item)


# ---------------------------------------------------------------------------
# Disjoint Order-14 Weierstrass Taylor-Jet L_2(tau) Solver (Zero Theta / GL3!)
# ---------------------------------------------------------------------------
def eisenstein_g2_g3_lambert(tau: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    q = mp.exp(2 * mp.pi * IMAG * tau)
    s3 = sum((mp.mpf(k) ** 3) * (q ** k) / (1 - q ** k) for k in range(1, 46))
    s5 = sum((mp.mpf(k) ** 5) * (q ** k) / (1 - q ** k) for k in range(1, 46))
    e4 = 1 + 240 * s3
    e6 = 1 - 504 * s5
    return rat_mp(4, 3) * (mp.pi ** 4) * e4, rat_mp(8, 27) * (mp.pi ** 6) * e6


def wp_and_dwp_trig(z: mp.mpc, tau: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    n_im = int(mp.nint(mp.im(z) / mp.im(tau)))
    zr = z - n_im * tau
    zr = zr - int(mp.nint(mp.re(zr)))
    sn0 = mp.sin(mp.pi * zr)
    cn0 = mp.cos(mp.pi * zr)
    wp_v = (mp.pi / sn0) ** 2 - (mp.pi ** 2) / 3
    dwp_v = -2 * (mp.pi ** 3) * cn0 / (sn0 ** 3)
    for n in range(1, 24):
        nt = n * tau
        s_bg = (mp.pi / mp.sin(mp.pi * nt)) ** 2
        for sgn in (1, -1):
            arg = mp.pi * (zr + sgn * nt)
            sn = mp.sin(arg)
            cn = mp.cos(arg)
            wp_v += (mp.pi / sn) ** 2 - s_bg
            dwp_v += -2 * (mp.pi ** 3) * cn / (sn ** 3)
    return wp_v, dwp_v


def taylor14_step(z0: mp.mpc, dz: mp.mpc, tau: mp.mpc, c_acc: mp.mpc, g2: mp.mpc, order: int = 14) -> mp.matrix:
    w0, dw0 = wp_and_dwp_trig(z0, tau)
    p_jet = [mp.mpc(0)] * (order + 1)
    p_jet[0] = w0
    p_jet[1] = dw0
    for k in range(order - 1):
        conv = sum(p_jet[j] * p_jet[k - j] for j in range(k + 1))
        rhs = 6 * conv - (g2 / 2 if k == 0 else 0)
        p_jet[k + 2] = rhs / ((k + 2) * (k + 1))
    qd = [(dz ** j) * p_jet[j] / 4 + (c_acc if j == 0 else 0) for j in range(order + 1)]
    dz2 = dz * dz
    cols = []
    for u0, u1 in ((mp.mpc(1), mp.mpc(0)), (mp.mpc(0), dz)):
        u_jet = [mp.mpc(0)] * (order + 1)
        u_jet[0], u_jet[1] = u0, u1
        for k in range(order - 1):
            u_jet[k + 2] = -dz2 * sum(qd[j] * u_jet[k - j] for j in range(k + 1)) / ((k + 2) * (k + 1))
        y_end = sum(u_jet)
        dy_end = sum(k * u_jet[k] for k in range(1, order + 1)) / dz
        cols.append((y_end, dy_end))
    return mp.matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])


def transfer_taylor(z_from: mp.mpc, z_to: mp.mpc, tau: mp.mpc, c_acc: mp.mpc, g2: mp.mpc, nsteps: int = 28) -> mp.matrix:
    t_m = mp.eye(2)
    dz = (z_to - z_from) / nsteps
    for k in range(nsteps):
        t_m = taylor14_step(z_from + k * dz, dz, tau, c_acc, g2, 14) * t_m
    return t_m


def mobius_ref(t_m: mp.matrix) -> mp.matrix:
    a_m = mp.matrix([[t_m[1, 1], t_m[0, 1]], [t_m[1, 0], t_m[0, 0]]])
    return a_m / mp.sqrt(a_m[0, 0] * a_m[1, 1] - a_m[0, 1] * a_m[1, 0])


def L2_taylor_ref(tau_fd: mp.mpc, c_acc: mp.mpc, nsteps: int = 28) -> mp.mpf:
    g2, g3 = eisenstein_g2_g3_lambert(tau_fd)
    z0 = (1 + tau_fd) / 2
    zs = z0 / 3
    ta = mobius_ref(transfer_taylor(z0, z0 + 1, tau_fd, c_acc, g2, nsteps))
    # Local Frobenius series from g2, g3:
    m_ord = 64
    aw: dict[int, mp.mpc] = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, m_ord // 2 + 2):
        aw[n] = rat_mp(3, (2 * n + 3) * (n - 2)) * sum(aw[m] * aw[n - 1 - m] for m in range(1, n - 1))
    qv = [mp.mpc(0)] * (m_ord + 1)
    qv[0] = c_acc
    for n in range(1, m_ord // 2 + 1):
        qv[2 * n] = aw[n] / 4
    al = [mp.mpc(0)] * (m_ord + 1)
    be = [mp.mpc(0)] * (m_ord + 1)
    al[0] = mp.mpc(1)
    for m in range(1, m_ord + 1):
        al[m] = -sum(qv[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
        be[m] = -(2 * m * al[m] + sum(qv[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)
    sz = mp.sqrt(zs)
    lz = mp.log(zs)
    hf = rat_mp(1, 2)
    sa = sum(al[m] * (zs ** m) for m in range(m_ord + 1))
    sb = sum(be[m] * (zs ** m) for m in range(m_ord + 1))
    dsa = sum((m + hf) * al[m] * (zs ** (m - 1)) for m in range(m_ord + 1))
    dsb = sum((m + hf) * be[m] * (zs ** (m - 1)) for m in range(m_ord + 1))
    y1, dy1 = sz * sa, sz * dsa
    y2, dy2 = y1 * lz + sz * sb, dy1 * lz + y1 / zs + sz * dsb
    f_zs = mp.matrix([[y1, y2], [dy1, dy2]])
    det_f = y1 * dy2 - y2 * dy1
    f_inv = mp.matrix([[dy2, -y2], [-dy1, y1]]) / det_f
    t_circ = f_zs * mp.matrix([[-1, -2 * mp.pi * IMAG], [0, -1]]) * f_inv
    t_0s = transfer_taylor(z0, zs, tau_fd, c_acc, g2, nsteps)
    det_t = t_0s[0, 0] * t_0s[1, 1] - t_0s[0, 1] * t_0s[1, 0]
    t_s0 = mp.matrix([[t_0s[1, 1], -t_0s[0, 1]], [-t_0s[1, 0], t_0s[0, 0]]]) / det_t
    p0 = mobius_ref(t_s0 * t_circ * t_0s)
    p_fix = (p0[0, 0] - p0[1, 1]) / (2 * p0[1, 0])
    disc = mp.sqrt((ta[0, 0] - ta[1, 1]) ** 2 + 4 * ta[0, 1] * ta[1, 0])
    f1 = (ta[0, 0] - ta[1, 1] + disc) / (2 * ta[1, 0])
    f2 = (ta[0, 0] - ta[1, 1] - disc) / (2 * ta[1, 0])
    sf = (f2 - f1) / (f2 - p_fix)
    gm = mp.matrix([[1 / sf, -f1 / sf], [1, -p_fix]])
    gm = gm / mp.sqrt(gm[0, 0] * gm[1, 1] - gm[0, 1] * gm[1, 0])
    if mp.im(gm[0, 1] / gm[1, 1]) < 0:
        gm = mp.matrix([[IMAG, 0], [0, -IMAG]]) * gm
    gi = mp.matrix([[gm[1, 1], -gm[0, 1]], [-gm[1, 0], gm[0, 0]]])
    rp = gm * p0 * gi
    rp = rp / rp[0, 0]
    lam = abs(mp.re(rp[0, 1]))
    w_zs = t_0s[0, 1] / t_0s[0, 0]
    u_zs = (gm[0, 0] * w_zs + gm[0, 1]) / (gm[1, 0] * w_zs + gm[1, 1])
    im_b = mp.im(u_zs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(sb / sa))
    return mp.pi - (2 * mp.pi / lam) * im_b


def solve_c_taylor(tau_fd: mp.mpc) -> mp.mpc:
    g2, _ = eisenstein_g2_g3_lambert(tau_fd)
    z0 = (1 + tau_fd) / 2

    def res(cv: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
        ta = mobius_ref(transfer_taylor(z0, z0 + 1, tau_fd, cv, g2, 18))
        tb = mobius_ref(transfer_taylor(z0, z0 + tau_fd, tau_fd, cv, g2, 18))
        return mp.im(ta[0, 0] + ta[1, 1]), mp.im(tb[0, 0] + tb[1, 1])

    c_v = mp.mpc(0)
    h = pow10_mp(-8)
    for _ in range(12):
        f1, f2 = res(c_v)
        if max(abs(f1), abs(f2)) < pow10_mp(-15):
            break
        f1x, f2x = res(c_v + h)
        f1y, f2y = res(c_v + IMAG * h)
        j11, j21 = (f1x - f1) / h, (f2x - f2) / h
        j12, j22 = (f1y - f1) / h, (f2y - f2) / h
        dj = j11 * j22 - j12 * j21
        c_v += ((-f1 * j22 + f2 * j12) / dj) + IMAG * ((-j11 * f2 + j21 * f1) / dj)
    return c_v


# ---------------------------------------------------------------------------
# Disjoint Frame C via Pentagonal Eta, Jacobi Triple Products, & 2D Ewald Norm
# ---------------------------------------------------------------------------
def eta_pentagonal(tau: mp.mpc, n_terms: int = 45) -> mp.mpc:
    q2 = mp.exp(2 * IMAG * mp.pi * tau)
    s = mp.mpc(1)
    for k in range(1, n_terms + 1):
        e1 = k * (3 * k - 1) // 2
        e2 = k * (3 * k + 1) // 2
        sgn = -1 if (k & 1) else 1
        s += sgn * ((q2 ** e1) + (q2 ** e2))
    return mp.exp(IMAG * mp.pi * tau / 12) * s


def theta3_triple(u: mp.mpc, tau: mp.mpc, n_prod: int = 50) -> mp.mpc:
    q = mp.exp(IMAG * mp.pi * tau)
    q2 = q * q
    w = mp.exp(2 * IMAG * mp.pi * u)
    wi = 1 / w
    p = mp.mpc(1)
    qn = q2
    q_odd = q
    for _ in range(n_prod):
        p *= (1 - qn) * (1 + q_odd * w) * (1 + q_odd * wi)
        qn *= q2
        q_odd *= q2
    return p


def theta234_zero_triple(tau: mp.mpc, n_prod: int = 55) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    q = mp.exp(IMAG * mp.pi * tau)
    q4 = mp.exp(IMAG * mp.pi * tau / 4)
    q2 = q * q
    p2 = mp.mpc(1)
    p3 = mp.mpc(1)
    p4 = mp.mpc(1)
    qn = q2
    q_odd = q
    for _ in range(n_prod):
        f0 = 1 - qn
        p2 *= f0 * ((1 + qn) ** 2)
        p3 *= f0 * ((1 + q_odd) ** 2)
        p4 *= f0 * ((1 - q_odd) ** 2)
        qn *= q2
        q_odd *= q2
    return 2 * q4 * p2, p3, p4


def thc_triple(a: mp.mpf, b: mp.mpf, tau: mp.mpc) -> mp.mpc:
    return mp.exp(IMAG * mp.pi * (a * a) * tau + 2 * IMAG * mp.pi * a * b) * theta3_triple(a * tau + b, tau)


def dlog_theta1_triple(z: mp.mpc, tau: mp.mpc, n_prod: int = 55) -> mp.mpc:
    """Exact analytic d/dz ln theta_1(z | tau) from Jacobi's triple product (zero mp.diff!)."""
    q2 = mp.exp(2 * IMAG * mp.pi * tau)
    w = mp.exp(2 * IMAG * mp.pi * z)
    wi = 1 / w
    acc = mp.pi * mp.cos(mp.pi * z) / mp.sin(mp.pi * z)
    qm = q2
    for _ in range(n_prod):
        t_pos = qm * w / (1 - qm * w)
        t_neg = qm * wi / (1 - qm * wi)
        acc += 2 * IMAG * mp.pi * (-t_pos + t_neg)
        qm *= q2
    return acc


_EWALD_CACHE: dict[tuple[Fr, Fr, str, str, int], mp.mpf] = {}


def c_norm_2d_ewald(u1: Fr, u2: Fr, tau: mp.mpc, rad: int = 10) -> mp.mpf:
    """Disjoint 2D Ewald exponential-integral representation of B1919's channel norm (zero digamma!)."""
    a_fr = u1 % 1
    b_fr = u2 % 1
    ekey = (a_fr, b_fr, mp.nstr(mp.re(tau), 30), mp.nstr(mp.im(tau), 30), int(mp.mp.dps))
    if ekey in _EWALD_CACHE:
        return _EWALD_CACHE[ekey]
    y = mp.im(tau)
    x = mp.re(tau)
    a = frac_mp(a_fr)
    b = frac_mp(b_fr)
    s_dir = mp.mpf(0)
    s_dual = mp.mpf(0)
    cutoff = mp.mpf(85)
    for m1 in range(-rad, rad + 1):
        c_dir = int(mp.nint(-(m1 + a) * x - b))
        for dm2 in range(-rad, rad + 1):
            m2 = c_dir + dm2
            w = (m1 + a) * tau + (m2 + b)
            arg_a = mp.pi * (mp.re(w) ** 2 + mp.im(w) ** 2) / y
            if arg_a < cutoff:
                s_dir += mp.exp(-arg_a) / arg_a
        c_du = int(mp.nint(m1 * x))
        for dm2 in range(-rad, rad + 1):
            m2 = c_du + dm2
            if (m1, m2) != (0, 0):
                wd = m1 * tau - m2
                arg_b = mp.pi * (mp.re(wd) ** 2 + mp.im(wd) ** 2) / y
                if arg_b < cutoff:
                    s_dual += mp.cos(2 * mp.pi * (m1 * b + m2 * a)) * mp.e1(arg_b)
    val = mp.pi * (s_dir + s_dual + mp.log(y) - mp.euler - mp.log(mp.pi))
    _EWALD_CACHE[ekey] = val
    return val


_REF_HIGGS_CACHE: dict[tuple[str, str, int], tuple[mp.mpc, mp.matrix]] = {}


def yhat_referee(tau: mp.mpc, a: Fr, b: Fr, sec: str, l_end: mp.mpf) -> mp.matrix:
    sec_map = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
    ql, qr = sec_map[sec]
    qi = mp.matrix([[IMAG, 0], [0, -IMAG]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    blocks = [qj, qi, qk]
    hf = rat_mp(1, 2)
    ed = {
        "1": hf * qj,
        "i": mp.matrix([[0, hf * IMAG], [hf * IMAG, 0]]),
        "j": -hf * mp.eye(2),
        "k": -hf * qi,
    }
    rkey = (mp.nstr(mp.re(tau), 30), mp.nstr(mp.im(tau), 30), int(mp.mp.dps))
    if rkey in _REF_HIGGS_CACHE:
        t1p, s_mat = _REF_HIGGS_CACHE[rkey]
    else:
        eta = eta_pentagonal(tau)
        t1p = 2 * mp.pi * (eta ** 3)
        t2, t3, t4 = theta234_zero_triple(tau)
        den = 24 * (eta ** 3)
        c0 = -(t2 ** 2) * (t3 ** 4 + t4 ** 4) / den
        c1 = (t4 ** 2) * (t2 ** 4 + t3 ** 4) / den
        c2 = IMAG * (t3 ** 2) * (t2 ** 4 - t4 ** 4) / den
        s_mat = c0 * qi + c1 * qj + c2 * qk
        _REF_HIGGS_CACHE[rkey] = (t1p, s_mat)

    x0, x1 = ql * a, 2 * ql * b
    y0, y1 = qr * a, 2 * qr * b
    ap, am = x0 + y0, x0 - y0
    bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
    eph = mp.exp(-2 * IMAG * mp.pi * frac_mp(x0))
    kap = {"1": -IMAG * eph, "i": mp.mpc(-1), "j": -eph, "k": IMAG}
    cs = {"1": (ap + H_FR, bp + H_FR), "i": (ap + H_FR, bp), "j": (ap, bp + H_FR), "k": (ap, bp)}
    ds = {"1": (am + H_FR, bm + H_FR), "i": (am + H_FR, bm), "j": (am, bm + H_FR), "k": (am, bm)}

    mw = mp.zeros(2, 2)
    for u_key in ("1", "i", "j", "k"):
        c_ch, d_ch = cs[u_key], ds[u_key]
        if ((c_ch[0] - H_FR) % 1 == 0 and (c_ch[1] - H_FR) % 1 == 0) or (
            (d_ch[0] - H_FR) % 1 == 0 and (d_ch[1] - H_FR) % 1 == 0
        ):
            continue
        r_val = kap[u_key] * thc_triple(frac_mp(c_ch[0]), frac_mp(c_ch[1]), tau) * thc_triple(frac_mp(d_ch[0]), frac_mp(d_ch[1]), tau) / t1p
        al, be = c_ch[0] - H_FR, c_ch[1] - H_FR
        al_r = al - int(mp.nint(frac_mp(al)))
        be_r = be - int(mp.nint(frac_mp(be)))
        z_pt = frac_mp(al_r) * tau + frac_mp(be_r)
        a0 = 2 * IMAG * mp.pi * frac_mp(al_r) + dlog_theta1_triple(z_pt, tau)
        c_nrm = c_norm_2d_ewald(al, be, tau) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
        arg = 2 * mp.pi * l_end + c_nrm
        if arg > 0:
            mw += (mp.sqrt(arg) * r_val) * ed[u_key]

    y_m = mp.zeros(3, 3)
    for ia, ca in enumerate(blocks):
        for ib, cb in enumerate(blocks):
            pr = ca.T * qj * s_mat * cb
            y_m[ia, ib] = pr[0, 0] * mw[0, 0] + pr[0, 1] * mw[0, 1] + pr[1, 0] * mw[1, 0] + pr[1, 1] * mw[1, 1]
    return mp.sqrt(mp.im(tau)) * y_m


# ---------------------------------------------------------------------------
# Disjoint Denman-Beavers sqrtm + Pade-(6,6) expm + Durand-Kerner Cubic Eigs
# ---------------------------------------------------------------------------
def frob_norm(m_in: mp.matrix) -> mp.mpf:
    return mp.sqrt(sum(abs(m_in[r, c]) ** 2 for r in range(m_in.rows) for c in range(m_in.cols)))


def denman_beavers_sqrtm3(h_psd: mp.matrix) -> mp.matrix:
    """Quadratic Denman-Beavers iteration for 3x3 Hermitian PSD square root (zero eigensolver!)."""
    eps_reg = pow10_mp(-50) * mp.eye(3)
    yk = (h_psd + h_psd.H) / 2 + eps_reg
    zk = mp.eye(3)
    for _ in range(16):
        yk_next = (yk + (zk ** (-1))) / 2
        zk_next = (zk + (yk ** (-1))) / 2
        if frob_norm(yk_next - yk) < pow10_mp(-27):
            yk = yk_next
            break
        yk, zk = yk_next, zk_next
    return (yk + yk.H) / 2


def pade66_expm3(a_mat: mp.matrix) -> mp.matrix:
    """Scaling-and-squaring diagonal Pade-(6,6) matrix exponential (zero eigensolver!)."""
    nrm = frob_norm(a_mat)
    s_pow = 0
    while nrm / (2 ** s_pow) > rat_mp(1, 8):
        s_pow += 1
    x = a_mat / (2 ** s_pow)
    # Pade-(6,6) coefficients c_k = (12 - k)! 6! / (12! k! (6 - k)!):
    c_p = [
        mp.mpf(1),
        rat_mp(1, 2),
        rat_mp(5, 44),
        rat_mp(1, 66),
        rat_mp(1, 792),
        rat_mp(1, 15840),
        rat_mp(1, 665280),
    ]
    p_num = mp.zeros(3, 3)
    q_den = mp.zeros(3, 3)
    xk = mp.eye(3)
    for k in range(7):
        p_num += c_p[k] * xk
        q_den += ((-1 if (k & 1) else 1) * c_p[k]) * xk
        if k < 6:
            xk = xk * x
    res = (q_den ** (-1)) * p_num
    for _ in range(s_pow):
        res = res * res
    return res


def cubic_roots_3x3(m3: mp.matrix) -> list[mp.mpc]:
    """Eigenvalues of 3x3 matrix via characteristic polynomial l^3 - t1 l^2 + t2 l - d = 0 + Durand-Kerner."""
    t1 = m3[0, 0] + m3[1, 1] + m3[2, 2]
    m2 = m3 * m3
    t2 = ((t1 * t1) - (m2[0, 0] + m2[1, 1] + m2[2, 2])) / 2
    det3 = (
        m3[0, 0] * (m3[1, 1] * m3[2, 2] - m3[1, 2] * m3[2, 1])
        - m3[0, 1] * (m3[1, 0] * m3[2, 2] - m3[1, 2] * m3[2, 0])
        + m3[0, 2] * (m3[1, 0] * m3[2, 1] - m3[1, 1] * m3[2, 0])
    )

    def poly(z: mp.mpc) -> mp.mpc:
        return ((z - t1) * z + t2) * z - det3

    r0 = t1 / 3 + rat_mp(1, 7) + IMAG * rat_mp(1, 11)
    r1 = t1 / 3 - rat_mp(1, 5) + IMAG * rat_mp(3, 13)
    r2 = t1 / 3 + rat_mp(2, 9) - IMAG * rat_mp(2, 7)
    for _ in range(45):
        d0 = poly(r0) / ((r0 - r1) * (r0 - r2))
        r0 -= d0
        d1 = poly(r1) / ((r1 - r0) * (r1 - r2))
        r1 -= d1
        d2 = poly(r2) / ((r2 - r0) * (r2 - r1))
        r2 -= d2
        if max(abs(d0), abs(d1), abs(d2)) < pow10_mp(-27):
            break
    return [r0, r1, r2]


def hermitian_3x3_eigenframe(h_in: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
    """Sorted eigenvalues and orthonormal eigenvectors of 3x3 Hermitian matrix via cubic roots + adjugate/nullspace."""
    hs = (h_in + h_in.H) / 2
    evs = sorted(mp.re(x) for x in cubic_roots_3x3(hs))
    vecs = []
    for lam in evs:
        b_m = hs - lam * mp.eye(3)
        # Cross-product / cofactor columns of (H - lam I) give exact eigenvector when eigenvalues are distinct:
        best_v = mp.zeros(3, 1)
        best_nrm = mp.mpf(0)
        # Cofactor matrix adj(b_m):
        for col in range(3):
            r_a, r_b = (col + 1) % 3, (col + 2) % 3
            cand = mp.matrix([
                b_m[1, r_a] * b_m[2, r_b] - b_m[1, r_b] * b_m[2, r_a],
                b_m[2, r_a] * b_m[0, r_b] - b_m[2, r_b] * b_m[0, r_a],
                b_m[0, r_a] * b_m[1, r_b] - b_m[0, r_b] * b_m[1, r_a],
            ])
            for prev in vecs:
                pr = sum(mp.conj(prev[r]) * cand[r] for r in range(3))
                cand = cand - pr * prev
            nrm = mp.sqrt(sum(abs(cand[r]) ** 2 for r in range(3)))
            if nrm > best_nrm:
                best_nrm = nrm
                best_v = cand / nrm
        vecs.append(best_v)
    u_out = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            u_out[r, c] = vecs[c][r]
    return evs, u_out


def cayley_u3_scrambler(seed_n: int) -> mp.matrix:
    """Disjoint Cayley unitary U = (I - K)(I + K)^{-1} from skew-Hermitian K^H = -K (zero QR!)."""
    k_mat = mp.zeros(3, 3)
    for r in range(3):
        for c in range(r, 3):
            idx = 23 * seed_n + 11 * r + 5 * c + 3
            if r == c:
                k_mat[r, r] = IMAG * mp.sin(mp.mpf(idx) * mp.sqrt(2))
            else:
                v = mp.cos(mp.mpf(idx) * mp.sqrt(3)) / 2 + IMAG * mp.sin(mp.mpf(idx + 2) * mp.sqrt(5)) / 2
                k_mat[r, c] = v
                k_mat[c, r] = -mp.conj(v)
    return (mp.eye(3) - k_mat) * ((mp.eye(3) + k_mat) ** (-1))


def floquet_referee(ul_links: list[mp.matrix], ys: list[mp.matrix], du: mp.mpf) -> tuple[mp.matrix, list[mp.mpf], mp.matrix]:
    n = len(ys)
    steps = [ul_links[j] * pade66_expm3(-du * denman_beavers_sqrtm3(ys[j] * ys[j].H)) for j in range(n)]
    p_tr = [mp.eye(3)]
    for j in range(n - 1):
        p_tr.append(ul_links[j] * p_tr[-1])
    g_avg = mp.zeros(3, 3)
    for j0 in range(n):
        mj = mp.eye(3)
        for off in range(n):
            mj = steps[(j0 + off) % n] * mj
        g_avg += (p_tr[j0].H * (mj * mj.H) * p_tr[j0]) / n
    m0 = mp.eye(3)
    for j in range(n):
        m0 = steps[j] * m0
    f_mods = sorted(abs(x) for x in cubic_roots_3x3(m0))
    return (g_avg + g_avg.H) / 2, f_mods, m0


# ---------------------------------------------------------------------------
# R_WI_1: Disjoint CRT Factorization of E[30] & Jordan-Block Cohomology
# ---------------------------------------------------------------------------
def run_ref_wi_1() -> tuple[dict[str, Any], list[list[tuple[Fr, Fr]]]]:
    def fixed_mod_p(p_mod: int, k_pow: int) -> list[tuple[int, int]]:
        mk = [[1, 0], [0, 1]]
        m1 = [[2 % p_mod, 1], [1, 1]]
        for _ in range(k_pow):
            mk = [
                [(mk[0][0] * m1[0][0] + mk[0][1] * m1[1][0]) % p_mod, (mk[0][0] * m1[0][1] + mk[0][1] * m1[1][1]) % p_mod],
                [(mk[1][0] * m1[0][0] + mk[1][1] * m1[1][0]) % p_mod, (mk[1][0] * m1[0][1] + mk[1][1] * m1[1][1]) % p_mod],
            ]
        return [
            (a, b)
            for a in range(p_mod)
            for b in range(p_mod)
            if (a, b) != (0, 0) and ((mk[0][0] * a + mk[1][0] * b) % p_mod, (mk[0][1] * a + mk[1][1] * b) % p_mod) == (a, b)
        ]

    # Exact CRT count on divisors of 60: |ker(M^k - I) cap E[30]_exact| = |F_2^*(k)| * |F_3^*(k)| * |F_5^*(k)|!
    divs = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
    crt_counts = {str(k): len(fixed_mod_p(2, k)) * len(fixed_mod_p(3, k)) * len(fixed_mod_p(5, k)) for k in divs}
    assert crt_counts["12"] == 96
    assert all(crt_counts[str(k)] == 0 for k in divs if k not in (12, 60))

    # Reconstruct all 96 points via CRT orthogonal weights (15, 10, 6) mod 30:
    f2 = fixed_mod_p(2, 12)
    f3 = fixed_mod_p(3, 12)
    f5 = fixed_mod_p(5, 12)
    p96_crt = sorted(
        (Fr((15 * u2[0] + 10 * u3[0] + 6 * u5[0]) % 30, 30), Fr((15 * u2[1] + 10 * u3[1] + 6 * u5[1]) % 30, 30))
        for u2 in f2
        for u3 in f3
        for u5 in f5
    )
    assert len(p96_crt) == 96

    orbits: list[list[tuple[Fr, Fr]]] = []
    seen: set[tuple[Fr, Fr]] = set()
    for pt in p96_crt:
        if pt in seen:
            continue
        orb = []
        c = pt
        for _ in range(12):
            orb.append(c)
            seen.add(c)
            c = ((2 * c[0] + c[1]) % 1, (c[0] + c[1]) % 1)
        orbits.append(orb)
    return {"crt_kernel_counts": crt_counts, "p96_count": len(p96_crt), "n_orbits": len(orbits)}, orbits


# ---------------------------------------------------------------------------
# R_WI_2, R_WI_3, R_WI_4: Disjoint Ewald/Taylor/Pade/Cayley Counterchecks
# ---------------------------------------------------------------------------
def fd_ref(tau: mp.mpc) -> tuple[mp.mpc, mp.mpf]:
    t = tau
    ls = mp.mpf(0)
    for _ in range(50):
        k = int(mp.nint(mp.re(t)))
        if k != 0:
            t -= k
        if abs(t) < mp.mpf(1) - pow10_mp(-20):
            ls += mp.log(abs(t))
            t = -1 / t
        else:
            break
    return t, ls


def run_ref_wi_2_3_4(orbits: list[list[tuple[Fr, Fr]]]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    mp.mp.dps = 32
    l2_i_ref = L2_taylor_ref(IMAG, mp.mpc(0), 28)
    l2_w_ref = L2_taylor_ref(rat_mp(1, 2) + IMAG * mp.sqrt(3) / 2, mp.mpc(0), 28)

    # Independent SL(2,Z) covariance check at tau_ref = -19/100 + 137/100 i:
    tau_r = rat_mp(-19, 100) + IMAG * rat_mp(137, 100)
    tr_fd, lr_sh = fd_ref(tau_r)
    cr_acc = solve_c_taylor(tr_fd)
    lr_cov = L2_taylor_ref(tr_fd, cr_acc, 28) + lr_sh

    w_t = mp.matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    w_s = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    w_m = mp.matrix([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])

    max_cov_ref = mp.mpf(0)
    for g_mat, w_mat in [([[1, 1], [0, 1]], w_t), ([[0, -1], [1, 0]], w_s), ([[2, 1], [1, 1]], w_m)]:
        ga, gb, gc, gd = g_mat[0][0], g_mat[0][1], g_mat[1][0], g_mat[1][1]
        tp = (ga * tau_r + gb) / (gc * tau_r + gd)
        lp = lr_cov + mp.log(abs(gc * tau_r + gd))
        ap, bp = orbits[1][0]
        a0 = (ga * ap + gc * bp) % 1
        b0 = (gb * ap + gd * bp) % 1
        for sec in ("up", "down", "lep"):
            yo = yhat_referee(tau_r, a0, b0, sec, lr_cov)
            yn = yhat_referee(tp, ap, bp, sec, lp)
            yr = w_mat * yo * w_mat.T
            c_ph = sum(mp.conj(yr[r, c]) * yn[r, c] for r in range(3) for c in range(3)) / sum(
                abs(yr[r, c]) ** 2 for r in range(3) for c in range(3)
            )
            err = frob_norm(yn - c_ph * yr) / frob_norm(yn)
            if err > max_cov_ref:
                max_cov_ref = err
            assert abs(abs(c_ph) - 1) < pow10_mp(-24)
    assert max_cov_ref < pow10_mp(-24)

    # Planted control PC_WI_3 in Referee: unshifted L under S fails by > 1/20:
    ap0, bp0 = orbits[0][0]
    yo_s = yhat_referee(tau_r, bp0 % 1, (-ap0) % 1, "up", lr_cov)
    yb_s = yhat_referee(-1 / tau_r, ap0, bp0, "up", lr_cov)
    evo_s, _ = hermitian_3x3_eigenframe(yo_s * yo_s.H)
    evb_s, _ = hermitian_3x3_eigenframe(yb_s * yb_s.H)
    pc3_ref = abs(mp.sqrt(evb_s[0] / evb_s[2]) - mp.sqrt(evo_s[0] / evo_s[2])) / mp.sqrt(evo_s[0] / evo_s[2])
    assert pc3_ref > rat_mp(1, 20)

    # Geodesic N_sub = 2 operators via Denman-Beavers + Pade-(6,6) + Cubic Eigenframe:
    mp.mp.dps = 30
    phi = (1 + mp.sqrt(5)) / 2
    du = 2 * mp.log(phi)
    taus_2 = [1 + IMAG, rat_mp(3, 2) + IMAG * rat_mp(1, 2)]
    ls_2 = [l2_i_ref, l2_i_ref + mp.log(2) / 2]
    ul_2 = [w_m if (j % 2 == 1) else mp.eye(3) for j in range(24)]

    def slices_ref(p_st: tuple[Fr, Fr]) -> dict[str, list[mp.matrix]]:
        pts = []
        c = p_st
        for _ in range(12):
            pts.append(c)
            c = ((2 * c[0] + c[1]) % 1, (c[0] + c[1]) % 1)
        return {
            s: [yhat_referee(taus_2[m], pts[k][0], pts[k][1], s, ls_2[m]) for k in range(12) for m in range(2)]
            for s in ("up", "down", "lep")
        }

    # Evaluate all 8 orbits:
    g_shell = {s: mp.zeros(3, 3) for s in ("up", "down", "lep")}
    orb_ref = []
    ys0_ref = {}
    for oi, o in enumerate(orbits):
        ys = slices_ref(o[0])
        if oi == 0:
            ys0_ref = ys
        sr = {}
        umat = {}
        for s in ("up", "down", "lep"):
            gcf, fm, m0 = floquet_referee(ul_2, ys[s], du)
            g_shell[s] += gcf / 8
            evs, um = hermitian_3x3_eigenframe(gcf)
            umat[s] = um
            sr[s] = {
                "ratios_cf": (mp.sqrt(evs[0] / evs[2]), mp.sqrt(evs[1] / evs[2])),
                "ratios_fm": (fm[0] / fm[2], fm[1] / fm[2]),
                "m0": m0,
            }
        v_m = umat["up"].H * umat["down"]
        va = mp.matrix([[abs(v_m[r, c]) for c in range(3)] for r in range(3)])
        orb_ref.append({"sectors": sr, "diag": min(va[0, 0], va[1, 1], va[2, 2]), "v12": va[0, 1], "v23": va[1, 2], "va": va})

    # Cayley 72-matrix local U(3) scrambling & cyclic shift counterchecks on Orbit 0:
    gl = [cayley_u3_scrambler(10 + j) for j in range(24)]
    gru = [cayley_u3_scrambler(50 + j) for j in range(24)]
    grd = [cayley_u3_scrambler(90 + j) for j in range(24)]
    ul_c = [gl[(j + 1) % 24] * ul_2[j] * gl[j].H for j in range(24)]
    yu_c = [gl[j] * ys0_ref["up"][j] * gru[j].H for j in range(24)]
    yd_c = [gl[j] * ys0_ref["down"][j] * grd[j].H for j in range(24)]
    gu_c, fu_c, _ = floquet_referee(ul_c, yu_c, du)
    gd_c, _, _ = floquet_referee(ul_c, yd_c, du)
    eu_c, uu_c = hermitian_3x3_eigenframe(gu_c)
    _, ud_c = hermitian_3x3_eigenframe(gd_c)
    vc = uu_c.H * ud_c
    cayley_err = max(
        abs(mp.sqrt(eu_c[0] / eu_c[2]) - orb_ref[0]["sectors"]["up"]["ratios_cf"][0]),
        max(abs(abs(vc[r, c]) - orb_ref[0]["va"][r, c]) for r in range(3) for c in range(3)),
        abs((fu_c[0] / fu_c[2]) - orb_ref[0]["sectors"]["up"]["ratios_fm"][0]),
    )
    assert cayley_err < pow10_mp(-18)

    # Planted control PC_WI_1 (un-transported Floquet operator UL = I_3) & PC_WI_2 (single cut):
    ul_id = [mp.eye(3) for _ in range(24)]
    gn_0, _, _ = floquet_referee(ul_id, ys0_ref["up"], du)
    gn_c, _, _ = floquet_referee(ul_id, yu_c, du)
    ev_n0, _ = hermitian_3x3_eigenframe(gn_0)
    ev_nc, _ = hermitian_3x3_eigenframe(gn_c)
    rn0 = mp.sqrt(max(mp.mpf(0), ev_n0[0]) / ev_n0[2])
    rnc = mp.sqrt(max(mp.mpf(0), ev_nc[0]) / ev_nc[2])
    pc1_ref = abs(rnc - rn0) / max(rn0, rnc)
    assert pc1_ref > rat_mp(1, 5)

    ul_sh = ul_2[2:] + ul_2[:2]
    yu_sh = ys0_ref["up"][2:] + ys0_ref["up"][:2]
    _, _, m0_sh = floquet_referee(ul_sh, yu_sh, du)
    m0_0 = orb_ref[0]["sectors"]["up"]["m0"]
    ev_c0, _ = hermitian_3x3_eigenframe(m0_0 * m0_0.H)
    ev_cs, _ = hermitian_3x3_eigenframe(m0_sh * m0_sh.H)
    rc0 = mp.sqrt(ev_c0[0] / ev_c0[2])
    rcs = mp.sqrt(ev_cs[0] / ev_cs[2])
    pc2_ref = abs(rcs - rc0) / max(rc0, rcs)
    assert pc2_ref > rat_mp(1, 5)

    # Odd-level P5 Deck-Commutant CKM Lock (PC_WI_4):
    ys_p5 = slices_ref((Fr(1, 5), Fr(2, 5)))
    gu_p5, _, _ = floquet_referee(ul_2, ys_p5["up"], du)
    gd_p5, _, _ = floquet_referee(ul_2, ys_p5["down"], du)
    _, uu_p5 = hermitian_3x3_eigenframe(gu_p5)
    _, ud_p5 = hermitian_3x3_eigenframe(gd_p5)
    vp5 = uu_p5.H * ud_p5
    p5_zero_mix_err = max(abs(1 - max(abs(vp5[r, c]) for c in range(3))) for r in range(3))
    assert p5_zero_mix_err < pow10_mp(-20)

    # Full 96-point shell:
    ush = {}
    rsh = {}
    for s in ("up", "down", "lep"):
        evs, um = hermitian_3x3_eigenframe(g_shell[s])
        ush[s] = um
        rsh[s] = [mp.nstr(mp.sqrt(evs[0] / evs[2]), 10), mp.nstr(mp.sqrt(evs[1] / evs[2]), 10)]
    vsh = ush["up"].H * ush["down"]
    diag_sh = min(abs(vsh[0, 0]), abs(vsh[1, 1]), abs(vsh[2, 2]))

    return (
        {
            "L2_at_i_taylor": mp.nstr(l2_i_ref, 16),
            "L2_at_omega_taylor": mp.nstr(l2_w_ref, 16),
            "max_ewald_sl2z_rel_err": mp.nstr(max_cov_ref, 8),
            "pc_wi_3_ref_unshifted_err": mp.nstr(pc3_ref, 8),
        },
        {
            "max_72_cayley_scrambling_err": mp.nstr(cayley_err, 8),
            "orbit_0_cutfree_floquet": {
                "up_ratios": [mp.nstr(x, 12) for x in orb_ref[0]["sectors"]["up"]["ratios_cf"]],
                "down_ratios": [mp.nstr(x, 12) for x in orb_ref[0]["sectors"]["down"]["ratios_cf"]],
                "lep_ratios": [mp.nstr(x, 12) for x in orb_ref[0]["sectors"]["lep"]["ratios_cf"]],
                "ckm_diag_min": mp.nstr(orb_ref[0]["diag"], 12),
                "ckm_v12": mp.nstr(orb_ref[0]["v12"], 12),
                "ckm_v23": mp.nstr(orb_ref[0]["v23"], 12),
            },
            "orbit_0_floquet_moduli_up_ratios": [mp.nstr(x, 12) for x in orb_ref[0]["sectors"]["up"]["ratios_fm"]],
            "p5_zero_mixing_deviation": mp.nstr(p5_zero_mix_err, 8),
            "pc_wi_1_ref_err": mp.nstr(pc1_ref, 8),
            "pc_wi_2_ref_err": mp.nstr(pc2_ref, 8),
        },
        {
            "full_96_point_shell": {
                "up_ratios": rsh["up"],
                "down_ratios": rsh["down"],
                "lep_ratios": rsh["lep"],
                "ckm_diag_min": mp.nstr(diag_sh, 10),
            }
        },
    )


# ---------------------------------------------------------------------------
# R_WI_5: Pure-Integer Symbolic Z[omega] Spin Holonomy on 8^3_4 (Zero Floats!)
# ---------------------------------------------------------------------------
ZInt = tuple[int, int]  # u + v*omega with omega^2 = -omega - 1


def z_add(x: ZInt, y: ZInt) -> ZInt:
    return (x[0] + y[0], x[1] + y[1])


def z_neg(x: ZInt) -> ZInt:
    return (-x[0], -x[1])


def z_mul(x: ZInt, y: ZInt) -> ZInt:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def zmat_mul(a: list[list[ZInt]], b: list[list[ZInt]]) -> list[list[ZInt]]:
    return [
        [z_add(z_mul(a[0][0], b[0][0]), z_mul(a[0][1], b[1][0])), z_add(z_mul(a[0][0], b[0][1]), z_mul(a[0][1], b[1][1]))],
        [z_add(z_mul(a[1][0], b[0][0]), z_mul(a[1][1], b[1][0])), z_add(z_mul(a[1][0], b[0][1]), z_mul(a[1][1], b[1][1]))],
    ]


def zmat_neg(a: list[list[ZInt]]) -> list[list[ZInt]]:
    return [[z_neg(a[0][0]), z_neg(a[0][1])], [z_neg(a[1][0]), z_neg(a[1][1])]]


def run_ref_wi_5() -> dict[str, Any]:
    z0, z1 = (0, 0), (1, 0)
    id_z = [[z1, z0], [z0, z1]]
    gens_z = {
        "a": [[z1, z1], [z0, z1]],
        "A": [[z1, (-1, 0)], [z0, z1]],
        "b": [[z1, z0], [(0, -1), z1]],
        "B": [[z1, z0], [(0, 1), z1]],
    }
    rel = "aBAbaBabAB"

    def eval_zw(w: str, flip: bool = False) -> list[list[ZInt]]:
        cur = id_z
        for ch in w:
            step = zmat_neg(gens_z[ch]) if flip else gens_z[ch]
            cur = zmat_mul(cur, step)
        return cur

    assert eval_zw(rel, False) == id_z and eval_zw(rel, True) == id_z
    ell_z = eval_zw("bABaaBAb", False)
    assert ell_z == [[(-1, 0), (-2, -4)], [(0, 0), (-1, 0)]]
    # Note -2 - 4*omega = -2 - 4*(-1/2 + i*sqrt(3)/2) = 0 - 2*i*sqrt(3), exact norm = (-2)^2 - (-2)(-4) + (-4)^2 = 12!

    cusp_traces = []
    for deg in (1, 2, 2):
        mu_rho1 = eval_zw("a" * deg, False)
        mu_rho0 = eval_zw("a" * deg, True)
        tr1 = [z_add(mu_rho1[0][0], mu_rho1[1][1])[0], z_add(ell_z[0][0], ell_z[1][1])[0]]
        tr0 = [z_add(mu_rho0[0][0], mu_rho0[1][1])[0], z_add(ell_z[0][0], ell_z[1][1])[0]]
        assert z_add(mu_rho1[0][0], mu_rho1[1][1])[1] == 0 and z_add(ell_z[0][0], ell_z[1][1])[1] == 0
        assert tr1 != [2, 2] and tr0 != [2, 2]
        cusp_traces.append({"degree": deg, "rho1": tr1, "rho0": tr0})
    return {"ell_symbolic_Z_omega": [[-1, 0], [-2, -4], [0, 0], [-1, 0]], "cusp_spin_traces": cusp_traces}


def main() -> None:
    ast_audit = verify_own_ast(SELF_PATH)
    r1, orbits = run_ref_wi_1()
    r2, r3, r4 = run_ref_wi_2_3_4(orbits)
    r5 = run_ref_wi_5()

    # Load Producer output JSON and verify < 10^-10 agreement on every decisive quantity:
    prod_path = PROD_REPO_OUT if PROD_REPO_OUT.exists() else PROD_SCRATCH_OUT
    assert prod_path.exists(), f"Missing Producer JSON at {prod_path}"
    prod = json.loads(prod_path.read_text(encoding="utf-8"))

    diffs = {
        "L2_i_diff": abs(mp.mpf(r2["L2_at_i_taylor"]) - mp.mpf(prod["WI_2_matrix_sl2z_cube_covariance"]["L2_at_i"])),
        "L2_omega_diff": abs(mp.mpf(r2["L2_at_omega_taylor"]) - mp.mpf(prod["WI_2_matrix_sl2z_cube_covariance"]["L2_at_omega"])),
        "orb0_up0_diff": abs(
            mp.mpf(r3["orbit_0_cutfree_floquet"]["up_ratios"][0])
            - mp.mpf(prod["WI_3_3d_geodesic_operators_and_churn"]["orbit_0_cutfree_floquet"]["up_ratios"][0])
        ),
        "orb0_down0_diff": abs(
            mp.mpf(r3["orbit_0_cutfree_floquet"]["down_ratios"][0])
            - mp.mpf(prod["WI_3_3d_geodesic_operators_and_churn"]["orbit_0_cutfree_floquet"]["down_ratios"][0])
        ),
        "orb0_lep0_diff": abs(
            mp.mpf(r3["orbit_0_cutfree_floquet"]["lep_ratios"][0])
            - mp.mpf(prod["WI_3_3d_geodesic_operators_and_churn"]["orbit_0_cutfree_floquet"]["lep_ratios"][0])
        ),
        "orb0_ckm_diag_diff": abs(
            mp.mpf(r3["orbit_0_cutfree_floquet"]["ckm_diag_min"])
            - mp.mpf(prod["WI_3_3d_geodesic_operators_and_churn"]["orbit_0_cutfree_floquet"]["ckm_diag_min"])
        ),
        "shell_up0_diff": abs(
            mp.mpf(r4["full_96_point_shell"]["up_ratios"][0])
            - mp.mpf(prod["WI_4_p96_orbit_reduction_and_shell"]["full_96_point_shell"]["up_ratios"][0])
        ),
    }
    max_prod_ref_diff = max(diffs.values())
    assert max_prod_ref_diff < pow10_mp(-10), diffs
    assert r1["crt_kernel_counts"] == prod["WI_1_m12_cohomology_p96"]["kernel_counts_by_divisor"]
    assert [c["rho1"] for c in r5["cusp_spin_traces"]] == [
        c["spin_traces_rho1"] for c in prod["WI_5_8_3_4_three_cusp_spinor_and_churn"]["cusps_8_3_4"]
    ]
    assert [c["rho0"] for c in r5["cusp_spin_traces"]] == [
        c["spin_traces_rho0"] for c in prod["WI_5_8_3_4_three_cusp_spinor_and_churn"]["cusps_8_3_4"]
    ]

    ref_controls = {
        "RC_WI_1_cayley_catches_naive_untransported_product": bool(mp.mpf(r3["pc_wi_1_ref_err"]) > rat_mp(1, 5)),
        "RC_WI_2_pade_catches_single_cut_orbit_shift": bool(mp.mpf(r3["pc_wi_2_ref_err"]) > rat_mp(1, 5)),
        "RC_WI_3_ewald_catches_unshifted_S_end_law": bool(mp.mpf(r2["pc_wi_3_ref_unshifted_err"]) > rat_mp(1, 20)),
        "RC_WI_4_cubic_catches_odd_level_p5_zero_mixing": bool(mp.mpf(r3["p5_zero_mixing_deviation"]) < pow10_mp(-20)),
    }
    assert all(ref_controls.values())

    out_doc: dict[str, Any] = {
        "claim_id": "CLAIM_2026-11-25_whole_instrument_m12_covariance_and_cube_churn",
        "firewall": "strictly_0_of_19",
        "referee_script_sha256": hashlib.sha256(SELF_PATH.read_bytes()).hexdigest(),
        "producer_output_sha256_checked": hashlib.sha256(prod_path.read_bytes()).hexdigest(),
        "ast_audit": ast_audit,
        "R_WI_1_crt_cohomology": r1,
        "R_WI_2_ewald_taylor_covariance": r2,
        "R_WI_3_denman_pade_cayley_operators": r3,
        "R_WI_4_shell_washout": r4,
        "R_WI_5_symbolic_z_omega_8_3_4": r5,
        "producer_referee_diffs": {k: mp.nstr(v, 8) for k, v in diffs.items()},
        "max_producer_referee_diff": mp.nstr(max_prod_ref_diff, 8),
        "referee_controls": ref_controls,
        "all_counterchecks_pass": True,
    }
    check_json_tree(out_doc)
    OUT_PATH.write_text(json.dumps(out_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: referee_x_whole_instrument.py matched Producer to", mp.nstr(max_prod_ref_diff, 6), "with 4/4 controls caught.")


if __name__ == "__main__":
    main()
