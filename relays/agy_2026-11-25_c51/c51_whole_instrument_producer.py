#!/usr/bin/env python3
"""Card AGY-C51 Standalone Producer (Strictly 0 of 19; python3 -I; stdlib + mpmath only).

Proves and verifies E1..E5 and Planted Controls 1..5 with zero float/complex AST literals or calls,
zero external repo/table imports, and zero empirical Standard-Model or experimental values."""
import ast
from fractions import Fraction as Fr
import hashlib
import json
import math
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "c51_out.json"
OUT_HASH = HERE / "OUTPUT_SHA256.txt"

I_MP = mp.mpc(0, 1)


def self_ast_firewall() -> dict:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    float_lits = 0
    float_calls = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            float_lits += 1
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
            float_calls += 1
    assert float_lits == 0 and float_calls == 0, (float_lits, float_calls)
    return {"ast_float_complex_literals": float_lits, "ast_float_complex_calls": float_calls}


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def thc_hol(ca: Fr, cb: Fr, tv: mp.mpc) -> mp.mpc:
    am, bm = f2m(ca), f2m(cb)
    q = mp.exp(I_MP * mp.pi * tv)
    return mp.exp(I_MP * mp.pi * am * am * tv + 2 * I_MP * mp.pi * am * bm) * mp.jtheta(3, mp.pi * (am * tv + bm), q)


def s_higgs_serre(tv: mp.mpc):
    q = mp.exp(I_MP * mp.pi * tv)
    q_mod = mp.exp(2 * I_MP * mp.pi * tv)
    t2 = 2 * mp.exp(I_MP * mp.pi * tv / 4) * (mp.qp(q_mod ** 2) ** 2) / mp.qp(q_mod)
    t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    d24 = 24 * (mp.exp(I_MP * mp.pi * tv / 12) * mp.qp(q_mod)) ** 3
    return (
        -(t2 ** 2) * ((t3 ** 4) + (t4 ** 4)) / d24,
        (t4 ** 2) * ((t2 ** 4) + (t3 ** 4)) / d24,
        I_MP * (t3 ** 2) * ((t2 ** 4) - (t4 ** 4)) / d24,
    )


def f_u_mp(u1: Fr, u2: Fr, tv: mp.mpc) -> mp.mpf:
    y = mp.im(tv)
    a_r, b_r = u1 % 1, u2 % 1
    if a_r != 0:
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(f2m(a_r)) + mp.digamma(1 - f2m(a_r)))
        zrow = mp.mpf(0)
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zrow = y * (mp.pi ** 2) / (mp.sin(mp.pi * f2m(b_r)) ** 2)
    tot = mp.mpf(0)
    k_lim = int(mp.ceil(mp.mpf(42) / y)) + 8
    for k_sum in range(-k_lim, k_lim + 1):
        m_val = f2m(a_r) + k_sum
        if m_val == 0:
            continue
        w_val = mp.exp(-2 * mp.pi * abs(m_val) * y + 2 * I_MP * mp.pi * (m_val * mp.re(tv) + f2m(u2)))
        tot += (2 * mp.pi / abs(m_val)) * mp.re(w_val / (1 - w_val))
    return first + zrow + tot


def yukawa_kahler(pa: Fr, pb: Fr, ql: int, qr: int, tv: mp.mpc, l_end: mp.mpf, with_norm: bool = True) -> mp.matrix:
    y = mp.im(tv)
    q = mp.exp(I_MP * mp.pi * tv)
    qi, qj = mp.matrix([[I_MP, 0], [0, -I_MP]]), mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    eps_q = qj
    hf = mp.mpf(1) / mp.mpf(2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    s1, s2, s3 = s_higgs_serre(tv)
    sh = s1 * qi + s2 * qj + s3 * qk
    ct = [[ca.T * eps_q * sh * cb for cb in blks] for ca in blks]
    t1p = mp.pi * mp.jtheta(2, 0, q) * mp.jtheta(3, 0, q) * mp.jtheta(4, 0, q)
    th1_fn = lambda zv: mp.jtheta(1, mp.pi * zv, q)
    hr = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hr, bp + hr), "i": (ap + hr, bp), "j": (ap, bp + hr), "k": (ap, bp)}
    ds = {"1": (am + hr, bm + hr), "i": (am + hr, bm), "j": (am, bm + hr), "k": (am, bm)}
    mw = mp.zeros(2, 2)
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hr, cs[sk][1] - hr
        dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
        if not ((al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0)):
            r_res = kap[sk] * thc_hol(cs[sk][0], cs[sk][1], tv) * thc_hol(ds[sk][0], ds[sk][1], tv) / t1p
            if with_norm:
                zv = f2m(al) * tv + f2m(be)
                a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_fn, zv) / th1_fn(zv)
                c_ch = f_u_mp(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
                mw = mw + mp.sqrt(2 * mp.pi * l_end + c_ch) * r_res * ed[sk]
            else:
                mw = mw + r_res * ed[sk]
    ym = mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])
    return mp.sqrt(y) * ym, mw


def eig_herm_asc(hm: mp.matrix):
    uu, sv, _ = mp.svd_c(hm)
    oi = sorted(range(3), key=lambda k: sv[k])
    return [sv[k] for k in oi], mp.matrix([[uu[r, oi[c]] for c in range(3)] for r in range(3)])


def herm_func(hm: mp.matrix, fn):
    ev, vv = eig_herm_asc(hm)
    return vv * mp.diag([fn(x) for x in ev]) * vv.H


# ---------------- Standalone Pure-mpmath Lame Punctured-Torus Solver (E4) ----------------
def wp_mp(z: mp.mpc, tv: mp.mpc, t30: mp.mpc, t40: mp.mpc, e1: mp.mpc, q: mp.mpc) -> mp.mpc:
    n_im = int(mp.nint(mp.im(z) / mp.im(tv)))
    zr = z - n_im * tv
    zr = zr - int(mp.nint(mp.re(zr)))
    t1 = mp.jtheta(1, mp.pi * zr, q)
    t2 = mp.jtheta(2, mp.pi * zr, q)
    return ((mp.pi * t30 * t40 * t2) / t1) ** 2 + e1


def fund_matrix_path(qf, dzf, n_steps: int) -> mp.matrix:
    s3_6 = mp.sqrt(mp.mpf(3)) / mp.mpf(6)
    q4 = mp.mpf(1) / mp.mpf(4)
    c1, c2 = mp.mpf(1) / mp.mpf(2) - s3_6, mp.mpf(1) / mp.mpf(2) + s3_6
    a11, a12, a21, a22 = q4, q4 - s3_6, q4 + s3_6, q4
    h = mp.mpf(1) / mp.mpf(n_steps)
    Y = mp.eye(2)
    for j in range(n_steps):
        t0 = j * h
        d1, Q1 = dzf(t0 + c1 * h), qf(t0 + c1 * h)
        d2, Q2 = dzf(t0 + c2 * h), qf(t0 + c2 * h)
        A1 = mp.matrix([[0, d1], [-d1 * Q1, 0]])
        A2 = mp.matrix([[0, d2], [-d2 * Q2, 0]])
        M4 = mp.eye(4)
        for r in range(2):
            for c in range(2):
                M4[r, c] -= h * a11 * A1[r, c]
                M4[r, c + 2] -= h * a12 * A1[r, c]
                M4[r + 2, c] -= h * a21 * A2[r, c]
                M4[r + 2, c + 2] -= h * a22 * A2[r, c]
        B1 = A1 * Y
        B2 = A2 * Y
        Y_next = mp.zeros(2, 2)
        for col in range(2):
            b4 = mp.matrix([B1[0, col], B1[1, col], B2[0, col], B2[1, col]])
            sol = mp.lu_solve(M4, b4)
            Y_next[0, col] = Y[0, col] + (h / mp.mpf(2)) * (sol[0] + sol[2])
            Y_next[1, col] = Y[1, col] + (h / mp.mpf(2)) * (sol[1] + sol[3])
        Y = Y_next
    return Y


def solve_accessory_mp(tv: mp.mpc, c_init: mp.mpc, n_steps: int = 24) -> mp.mpc:
    q = mp.exp(I_MP * mp.pi * tv)
    t30, t40 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    e1 = (mp.pi ** 2 / mp.mpf(3)) * (t30 ** 4 + t40 ** 4)
    z0 = (mp.mpf(1) + tv) / mp.mpf(2)

    def Q_at(z, c_acc):
        return wp_mp(z, tv, t30, t40, e1, q) / mp.mpf(4) + c_acc

    def mobius(T):
        ds = mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
        return mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]]) / ds

    def resid(c_acc):
        Ta = fund_matrix_path(lambda t: Q_at(z0 + t, c_acc), lambda t: mp.mpc(1), n_steps)
        Tb = fund_matrix_path(lambda t: Q_at(z0 + t * tv, c_acc), lambda t: tv, n_steps)
        Aa, Ab = mobius(Ta), mobius(Tb)
        return mp.im(Aa[0, 0] + Aa[1, 1]), mp.im(Ab[0, 0] + Ab[1, 1])

    c_cur = c_init
    h_fd = mp.mpf(10) ** (-9)
    tol = mp.mpf(10) ** (-22)
    for _ in range(16):
        f1, f2 = resid(c_cur)
        if max(abs(f1), abs(f2)) < tol:
            break
        f1x, f2x = resid(c_cur + h_fd)
        f1y, f2y = resid(c_cur + I_MP * h_fd)
        J = mp.matrix([[(f1x - f1) / h_fd, (f1y - f1) / h_fd], [(f2x - f2) / h_fd, (f2y - f2) / h_fd]])
        dc = mp.lu_solve(J, mp.matrix([-f1, -f2]))
        c_cur = c_cur + dc[0] + I_MP * dc[1]
    return c_cur


def eval_l2_given_c(tv: mp.mpc, c_cur: mp.mpc, n_steps: int) -> mp.mpf:
    q = mp.exp(I_MP * mp.pi * tv)
    t20, t30, t40 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    e1 = (mp.pi ** 2 / mp.mpf(3)) * (t30 ** 4 + t40 ** 4)
    z0 = (mp.mpf(1) + tv) / mp.mpf(2)

    def Q_at(z):
        return wp_mp(z, tv, t30, t40, e1, q) / mp.mpf(4) + c_cur

    def mobius(T):
        ds = mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
        return mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]]) / ds

    Ta = fund_matrix_path(lambda t: Q_at(z0 + t), lambda t: mp.mpc(1), n_steps)
    Tb = fund_matrix_path(lambda t: Q_at(z0 + t * tv), lambda t: tv, n_steps)
    Aa = mobius(Ta)
    eps_r = mp.mpf(1) / mp.mpf(20)
    zs = eps_r * z0 / abs(z0)
    T1 = fund_matrix_path(lambda t: Q_at(z0 + t * (zs - z0)), lambda t: zs - z0, n_steps)
    T2 = fund_matrix_path(
        lambda t: Q_at(zs * mp.exp(2 * I_MP * mp.pi * t)),
        lambda t: 2 * I_MP * mp.pi * zs * mp.exp(2 * I_MP * mp.pi * t),
        n_steps,
    )
    T3 = fund_matrix_path(lambda t: Q_at(zs + t * (z0 - zs)), lambda t: z0 - zs, n_steps)
    P0 = mobius(T3 * T2 * T1)

    def fix_pts(M):
        a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        disc = mp.sqrt((a - d) ** 2 + 4 * b * cc)
        return (a - d + disc) / (2 * cc), (a - d - disc) / (2 * cc)

    p_par = sum(fix_pts(P0)) / mp.mpf(2)
    fa1, fa2 = fix_pts(Aa)
    s_g = (fa2 - fa1) / (fa2 - p_par)
    g_m = mp.matrix([[1 / s_g, -fa1 / s_g], [1, -p_par]])
    g_m = g_m / mp.sqrt(g_m[0, 0] * g_m[1, 1] - g_m[0, 1] * g_m[1, 0])
    if mp.im((-fa1 / s_g) / (-p_par)) < 0:
        g_m = mp.matrix([[I_MP, 0], [0, -I_MP]]) * g_m
    RP = g_m * P0 * (g_m ** -1)
    RP = RP / RP[0, 0]
    lam = abs(mp.re(RP[0, 1]))

    k_c = mp.pi ** 2 / mp.mpf(3)
    e2, e3 = k_c * (t20 ** 4 - t40 ** 4), -k_c * (t20 ** 4 + t30 ** 4)
    g2, g3 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2), 4 * e1 * e2 * e3
    M_frob = 60
    a_wp = {1: g2 / mp.mpf(20), 2: g3 / mp.mpf(28)}
    for n in range(3, M_frob // 2 + 2):
        a_wp[n] = mp.mpf(3) / mp.mpf((2 * n + 3) * (n - 2)) * sum(a_wp[m] * a_wp[n - 1 - m] for m in range(1, n - 1))
    Qf = [mp.mpc(0)] * (M_frob + 1)
    Qf[0] = c_cur
    for n in range(1, M_frob // 2 + 1):
        if 2 * n <= M_frob:
            Qf[2 * n] = a_wp[n] / mp.mpf(4)
    al = [mp.mpc(0)] * (M_frob + 1)
    be = [mp.mpc(0)] * (M_frob + 1)
    al[0] = mp.mpc(1)
    for m in range(1, M_frob + 1):
        sa = sum(Qf[j] * al[m - 2 - j] for j in range(0, m - 1))
        al[m] = -sa / mp.mpf(m * m)
        sb = sum(Qf[j] * be[m - 2 - j] for j in range(0, m - 1))
        be[m] = -(2 * m * al[m] + sb) / mp.mpf(m * m)
    g_loc = sum(be[m] * (zs ** m) for m in range(M_frob + 1)) / sum(al[m] * (zs ** m) for m in range(M_frob + 1))
    u_zs = (g_m[0, 0] * (T1[0, 1] / T1[0, 0]) + g_m[0, 1]) / (g_m[1, 0] * (T1[0, 1] / T1[0, 0]) + g_m[1, 1])
    im_B = mp.im(u_zs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(g_loc))
    return mp.pi - (2 * mp.pi / lam) * im_B


def solve_l2_richardson(tv: mp.mpc, walk_from_i: int = 0):
    with mp.workdps(40):
        c_guess = mp.mpc(0)
        if walk_from_i > 0:
            for st in range(1, walk_from_i + 1):
                tk = I_MP + (tv - I_MP) * (mp.mpf(st) / mp.mpf(walk_from_i))
                c_guess = solve_accessory_mp(tk, c_guess, 20)
        c28 = solve_accessory_mp(tv, c_guess, 28)
        c56 = solve_accessory_mp(tv, c28, 56)
        l28 = eval_l2_given_c(tv, c28, 28)
        l56 = eval_l2_given_c(tv, c56, 56)
        l_rich = (mp.mpf(16) * l56 - l28) / mp.mpf(15)
        return l_rich, l56, c56


# ---------------- Exact Cube Group & Modular Arithmetic Helpers ----------------
RHO_I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
RHO_T = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
RHO_Tinv = ((0, 0, -1), (0, 1, 0), (1, 0, 0))
RHO_S = ((0, -1, 0), (-1, 0, 0), (0, 0, -1))


def mmul3(m1, m2):
    return tuple(tuple(sum(m1[r][k] * m2[k][c] for k in range(3)) for c in range(3)) for r in range(3))


def det3(m) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def elem_order3(m) -> int:
    cur = RHO_I
    for k in range(1, 25):
        cur = mmul3(cur, m)
        if cur == RHO_I:
            return k
    raise RuntimeError("order > 24")


def legendre_p(n: int, p: int) -> int:
    r = n % p
    if r == 0:
        return 0
    v = pow(r, (p - 1) // 2, p)
    return 1 if v == 1 else -1


def cayley_u3(seed_ints) -> mp.matrix:
    """Construct exact dense U(3) matrix U = (I + i H)(I - i H)^{-1} from rational Hermitian H (zero floats!)."""
    # seed_ints: 9 integers (3 real diag, 3 off-diag real, 3 off-diag imag)
    d0, d1, d2, r01, r02, r12, m01, m02, m12 = seed_ints
    den = mp.mpf(7)
    H = mp.matrix([
        [mp.mpf(d0) / den, mp.mpc(r01, m01) / den, mp.mpc(r02, m02) / den],
        [mp.mpc(r01, -m01) / den, mp.mpf(d1) / den, mp.mpc(r12, m12) / den],
        [mp.mpc(r02, -m02) / den, mp.mpc(r12, -m12) / den, mp.mpf(d2) / den],
    ])
    I3 = mp.eye(3)
    return (I3 + I_MP * H) * ((I3 - I_MP * H) ** -1)


def main() -> None:
    ast_res = self_ast_firewall()

    # ================ E1: SO(3, Z) ~= S_4 Cube Homomorphism, Direct P-882 Proof, & det = -1 Law ================
    so3_z = {RHO_I}
    q_grp = [RHO_I]
    while q_grp:
        cur = q_grp.pop(0)
        for g in (RHO_T, RHO_S):
            nx = mmul3(g, cur)
            if nx not in so3_z:
                so3_z.add(nx)
                q_grp.append(nx)
    assert len(so3_z) == 24 and all(det3(g) == 1 for g in so3_z)
    order_hist = {}
    for g in so3_z:
        o = elem_order3(g)
        order_hist[str(o)] = order_hist.get(str(o), 0) + 1
    assert order_hist == {"1": 1, "2": 9, "3": 8, "4": 6}

    # BFS over SL(2, Z) reaching all 576 primitive order-30 bottom rows while tracking exact word homomorphism rho_cube(gamma)!
    seen_576 = {(0, 1): ((1, 0, 0, 1), RHO_I)}
    q_bfs = [((1, 0, 0, 1), RHO_I)]
    moves = [
        ((1, 1, 0, 1), RHO_T),
        ((1, -1, 0, 1), RHO_Tinv),
        ((0, -1, 1, 0), RHO_S),
        ((-1, 0, 0, -1), RHO_I),
    ]
    while q_bfs and len(seen_576) < 576:
        (a, b, c, d), R_cur = q_bfs.pop(0)
        for (ga, gb, gc, gd), R_g in moves:
            na, nb = a * ga + b * gc, a * gb + b * gd
            nc, nd = c * ga + d * gc, c * gb + d * gd
            key = (nc % 30, nd % 30)
            if not (key[0] % 2 == 0 and key[1] % 2 == 0) and not (key[0] % 3 == 0 and key[1] % 3 == 0) and not (key[0] % 5 == 0 and key[1] % 5 == 0):
                if key not in seen_576:
                    R_nx = mmul3(R_cur, R_g)
                    seen_576[key] = ((na, nb, nc, nd), R_nx)
                    q_bfs.append(((na, nb, nc, nd), R_nx))
    assert len(seen_576) == 576

    a12, b12, c12, d12 = 1, 0, 0, 1
    for _ in range(12):
        a12, b12, c12, d12 = (2 * a12 + b12) % 30, (a12 + b12) % 30, (2 * c12 + d12) % 30, (c12 + d12) % 30
    fixed_A12 = [k for k in seen_576 if ((k[0] * a12 + k[1] * c12) % 30, (k[0] * b12 + k[1] * d12) % 30) == k]
    assert len(fixed_A12) == 96 and all((k[1] - 2 * k[0]) % 5 == 0 for k in fixed_A12)

    with mp.workdps(70):
        tau_ref = mp.mpc(mp.mpf(21) / mp.mpf(100), mp.mpf(143) / mp.mpf(100))
        l_ref = mp.mpf(53) / mp.mpf(20)
        w_base = (Fr(0, 30), Fr(1, 30))

        cusps_gold_sample = [k for k in fixed_A12 if abs(seen_576[k][0][2]) <= 8][:8]
        cusps_off_sample = [k for k in seen_576 if (k[1] - 2 * k[0]) % 5 != 0 and abs(seen_576[k][0][2]) <= 6][:8]
        assert len(cusps_gold_sample) == 8 and len(cusps_off_sample) == 8

        max_p882_err = mp.mpf(0)
        for cm, dm in cusps_gold_sample + cusps_off_sample:
            (a, b, c, d), R_tup = seen_576[(cm, dm)]
            Rm = mp.matrix([[mp.mpf(R_tup[r][col]) for col in range(3)] for r in range(3)])
            fac = c * tau_ref + d
            tau_c = (a * tau_ref + b) / fac
            l_c = l_ref + mp.log(abs(fac))
            ph_j = fac / abs(fac)
            w_pt = (Fr(cm, 30), Fr(dm, 30))
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                y_inf, _ = yukawa_kahler(w_pt[0], w_pt[1], ql, qr, tau_ref, l_ref)
                y_cusp, _ = yukawa_kahler(w_base[0], w_base[1], ql, qr, tau_cusp := tau_c, l_c)
                y_cusp = y_cusp / ph_j
                cand = Rm * y_inf * Rm.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = y_cusp[r0, c0] / cand[r0, c0]
                err = mp.mnorm(y_cusp - sc * cand, "F") / mp.mnorm(y_inf, "F")
                if err > max_p882_err:
                    max_p882_err = err
        assert max_p882_err < mp.mpf(10) ** (-50)

        # Control 1: Omitting ln|c*tau + d| OR swapping gamma <-> gamma^{-1} breaks P-882 by > 1/100!
        cm_c1, dm_c1 = (1, 1)
        (a1, b1, c1, d1), R1 = seen_576[(cm_c1, dm_c1)]
        Rm1 = mp.matrix([[mp.mpf(R1[r][col]) for col in range(3)] for r in range(3)])
        fac1 = c1 * tau_ref + d1
        tau_c1 = (a1 * tau_ref + b1) / fac1
        yi_c1, _ = yukawa_kahler(Fr(cm_c1, 30), Fr(dm_c1, 30), 1, -4, tau_ref, l_ref)
        yc_noshift, _ = yukawa_kahler(w_base[0], w_base[1], 1, -4, tau_c1, l_ref)  # OMITTED ln|fac1|!
        yc_noshift = yc_noshift / (fac1 / abs(fac1))
        cand1 = Rm1 * yi_c1 * Rm1.T
        sc1 = yc_noshift[0, 1] / cand1[0, 1]
        ctrl1_noshift_err = mp.mnorm(yc_noshift - sc1 * cand1, "F") / mp.mnorm(yi_c1, "F")
        fac_inv = -c1 * tau_ref + a1
        tau_inv1 = (d1 * tau_ref - b1) / fac_inv
        yc_wronginv, _ = yukawa_kahler(w_base[0], w_base[1], 1, -4, tau_inv1, l_ref + mp.log(abs(fac_inv)))
        sv_i1 = eig_herm_asc(yi_c1 * yi_c1.H)[0]
        sv_w1 = eig_herm_asc(yc_wronginv * yc_wronginv.H)[0]
        ctrl1_inv_sv_err = max(abs(sv_i1[k] - sv_w1[k]) for k in range(3))
        assert ctrl1_noshift_err > mp.mpf(1) / mp.mpf(100) and ctrl1_inv_sv_err > mp.mpf(1) / mp.mpf(100)

        # Antiholomorphic (det = -1) laws under J_0, R_sigma, and F = [[1, 1], [1, 0]], plus weave LR <-> RL conjugation!
        o3_mp = (
            [mp.matrix([[mp.mpf(g[r][col]) for col in range(3)] for r in range(3)]) for g in so3_z]
            + [mp.matrix([[mp.mpf(-g[r][col]) for col in range(3)] for r in range(3)]) for g in so3_z]
        )
        w0_a = (Fr(4, 15), Fr(1, 30))

        def check_antihol_conj(tau1, fac_bar, w1):
            l1 = l_ref + mp.log(abs(fac_bar))
            ph = fac_bar / abs(fac_bar)
            yu0, _ = yukawa_kahler(w0_a[0], w0_a[1], 1, -4, tau_ref, l_ref)
            yu1, _ = yukawa_kahler(w1[0], w1[1], 1, -4, tau1, l1)
            yu1 = yu1 / ph
            yu0_bar = mp.matrix([[mp.conj(yu0[r, col]) for col in range(3)] for r in range(3)])
            best_e = mp.mpf(999)
            best_R = None
            for Rm in o3_mp:
                cand = Rm * yu0_bar * Rm.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = yu1[r0, c0] / cand[r0, c0]
                err = mp.mnorm(yu1 - sc * cand, "F") / mp.mnorm(yu0, "F")
                if err < best_e:
                    best_e = err
                    best_R = Rm
            for ql, qr in [(1, 2), (-3, 6)]:
                yf0, _ = yukawa_kahler(w0_a[0], w0_a[1], ql, qr, tau_ref, l_ref)
                yf1, _ = yukawa_kahler(w1[0], w1[1], ql, qr, tau1, l1)
                yf1 = yf1 / ph
                yf0_bar = mp.matrix([[mp.conj(yf0[r, col]) for col in range(3)] for r in range(3)])
                cand = best_R * yf0_bar * best_R.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = yf1[r0, c0] / cand[r0, c0]
                ef = mp.mnorm(yf1 - sc * cand, "F") / mp.mnorm(yf0, "F")
                if ef > best_e:
                    best_e = ef
            return best_e

        err_J0 = check_antihol_conj(-mp.conj(tau_ref), mp.mpc(1), (w0_a[0], (-w0_a[1]) % 1))
        err_Rsig = check_antihol_conj(1 - mp.conj(tau_ref), mp.mpc(1), ((-w0_a[0]) % 1, (w0_a[0] + w0_a[1]) % 1))
        err_F = check_antihol_conj((mp.conj(tau_ref) + 1) / mp.conj(tau_ref), mp.conj(tau_ref), (w0_a[1], (w0_a[0] - w0_a[1]) % 1))
        assert max(err_J0, err_Rsig, err_F) < mp.mpf(10) ** (-50)

        RHO_R = mmul3(RHO_S, mmul3(RHO_Tinv, RHO_S))
        Rm_R = mp.matrix([[mp.mpf(RHO_R[r][col]) for col in range(3)] for r in range(3)])
        tau_RL = tau_ref / (tau_ref + 1)
        l_RL = l_ref + mp.log(abs(tau_ref + 1))
        ph_R = (tau_ref + 1) / abs(tau_ref + 1)
        w_RL = ((w0_a[0] - w0_a[1]) % 1, w0_a[1] % 1)
        yu_LR, _ = yukawa_kahler(w0_a[0], w0_a[1], 1, -4, tau_ref, l_ref)
        yu_RL, _ = yukawa_kahler(w_RL[0], w_RL[1], 1, -4, tau_RL, l_RL)
        yu_RL = yu_RL / ph_R
        cand_RL = Rm_R * yu_LR * Rm_R.T
        sc_RL = yu_RL[0, 1] / cand_RL[0, 1]
        err_weave_RL = mp.mnorm(yu_RL - sc_RL * cand_RL, "F") / mp.mnorm(yu_LR, "F")
        assert err_weave_RL < mp.mpf(10) ** (-50)

    # ================ E2: Exact Lepton 2/5 Cusp Rate Proof Across All 480 Order-30 Points ================
    pts_480 = [k for k in seen_576 if k[0] % 5 != 0]
    assert len(pts_480) == 480
    img_10_counts = {}
    for ia, ib in pts_480:
        k10 = (ia % 10, ib % 10)
        img_10_counts[k10] = img_10_counts.get(k10, 0) + 1
    pts_60_order10 = sorted(img_10_counts.keys())
    assert len(pts_60_order10) == 60 and all(v == 8 for v in img_10_counts.values())

    with mp.workdps(95):
        l_asym = mp.mpf(221) / mp.mpf(100)
        max_b1973_rank1_ratio = mp.mpf(0)
        raw_theta_exp_pairs = []
        for a10, b10 in [(1, 0), (2, 1), (3, 0), (4, 1)]:
            _, mw_nonorm = yukawa_kahler(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 35), l_asym, with_norm=False)
            _, sv_mw0, _ = mp.svd_c(mw_nonorm)
            sv_mw0 = sorted(list(sv_mw0))
            rat0 = sv_mw0[0] / sv_mw0[1]
            if rat0 > max_b1973_rank1_ratio:
                max_b1973_rank1_ratio = rat0
            pa, pb = Fr(a10, 30), Fr(b10, 30)
            ap, am = 3 * pa, -9 * pa
            bp, bm = 3 * pb, -9 * pb
            hr = Fr(1, 2)
            cs = {"1": (ap + hr, bp + hr), "i": (ap + hr, bp), "j": (ap, bp + hr), "k": (ap, bp)}
            ds = {"1": (am + hr, bm + hr), "i": (am + hr, bm), "j": (am, bm + hr), "k": (am, bm)}
            exps = {}
            for sk in ("1", "i", "j", "k"):
                v30 = abs(thc_hol(cs[sk][0], cs[sk][1], mp.mpc(0, 30)) * thc_hol(ds[sk][0], ds[sk][1], mp.mpc(0, 30)))
                v40 = abs(thc_hol(cs[sk][0], cs[sk][1], mp.mpc(0, 40)) * thc_hol(ds[sk][0], ds[sk][1], mp.mpc(0, 40)))
                exps[sk] = str(Fr(int(mp.nint(-100 * mp.log(v40 / v30) / (10 * mp.pi))), 100))
            assert set(exps.values()) == {"1/10", "1/5"}
            raw_theta_exp_pairs.append(exps)
        assert max_b1973_rank1_ratio < mp.mpf(10) ** (-80)

        # Evaluate ALL 60 order-10 images (by +/- symmetry 30 distinct pairs, verify all 60 explicitly!)
        max_25_err = mp.mpf(0)
        r23_set = set()
        r13_set = set()
        for a10, b10 in pts_60_order10:
            ye35, _ = yukawa_kahler(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 35), l_asym)
            ye45, _ = yukawa_kahler(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 45), l_asym)
            _, s35, _ = mp.svd_c(ye35)
            _, s45, _ = mp.svd_c(ye45)
            s35 = sorted(list(s35))
            s45 = sorted(list(s45))
            r23 = -(mp.log(s45[1] / s45[2]) - mp.log(s35[1] / s35[2])) / (10 * mp.pi)
            r13 = -(mp.log(s45[0] / s45[2]) - mp.log(s35[0] / s35[2])) / (10 * mp.pi)
            df = abs(r23 - mp.mpf(2) / mp.mpf(5))
            if df > max_25_err:
                max_25_err = df
            r23_set.add(str(Fr(int(mp.nint(60 * r23)), 60)))
            r13_set.add(str(Fr(int(mp.nint(60 * r13)), 60)))
        assert max_25_err < mp.mpf(10) ** (-9)
        assert r23_set == {"2/5"} and r13_set == {"1", "11/10", "7/5"}

        # Control 2: Points with a % 5 == 0 (excluded 96 points) fail rate(m_2/m_3) == 2/5!
        ctrl2_min_dev = mp.mpf(999)
        for ia_bad, ib_bad in [(0, 1), (5, 1), (10, 1), (15, 2)]:
            yb35, _ = yukawa_kahler(Fr(ia_bad, 30), Fr(ib_bad, 30), -3, 6, mp.mpc(0, 35), l_asym)
            yb45, _ = yukawa_kahler(Fr(ia_bad, 30), Fr(ib_bad, 30), -3, 6, mp.mpc(0, 45), l_asym)
            _, sb35, _ = mp.svd_c(yb35)
            _, sb45, _ = mp.svd_c(yb45)
            sb35 = sorted(list(sb35))
            sb45 = sorted(list(sb45))
            rb23 = -(mp.log(sb45[1] / sb45[2]) - mp.log(sb35[1] / sb35[2])) / (10 * mp.pi)
            dev = abs(rb23 - mp.mpf(2) / mp.mpf(5))
            if dev < ctrl2_min_dev:
                ctrl2_min_dev = dev
        assert ctrl2_min_dev > mp.mpf(1) / mp.mpf(10)

    # ================ E3: Legendre/Jacobi Orbit Classification & +-R_sigma Mirror Pinning ================
    pts_96_frac = sorted((Fr(ia, 30), Fr(ib, 30)) for (ia, ib) in fixed_A12)
    seen_orb = set()
    orbits_8 = []
    for pt in pts_96_frac:
        if pt in seen_orb:
            continue
        orb = []
        cur = pt
        for _ in range(12):
            orb.append(cur)
            seen_orb.add(cur)
            cur = ((2 * cur[0] + cur[1]) % 1, (cur[0] + cur[1]) % 1)
        assert cur == pt
        orbits_8.append(orb)
    assert len(orbits_8) == 8

    slow_counts_neg = []
    slow_counts_pos = []
    chi15_invariant_ok = True
    ctrl3_bad_q3_flips = 0
    bond_mirror_count = 0
    vertex_mirror_count = 0

    for idx, orb in enumerate(orbits_8):
        ia0, ib0 = int(orb[0][0] * 30), int(orb[0][1] * 30)
        leg5 = legendre_p(ia0, 5)
        # B1978 / A2-B1978 exact slow 2-3 criterion: e(V_23) = 2|nd(a) - 1/4| == 1/30 <=> nd(a) in {7/30, 8/30}!
        slow_c = sum(1 for w in orb if min(w[0], 1 - w[0]) in (Fr(7, 30), Fr(8, 30)))
        if leg5 == -1:
            slow_counts_neg.append(slow_c)
        else:
            slow_counts_pos.append(slow_c)

        # Check chi_15 invariance across A, F, S, -I on every point of the orbit:
        c0_val = legendre_p(ia0 * ia0 + 2 * ia0 * ib0 + 2 * ib0 * ib0, 3) * legendre_p(ia0, 5)
        for w in orb:
            wa, wb = int(w[0] * 30), int(w[1] * 30)
            for ga, gb in [
                ((2 * wa + wb) % 30, (wa + wb) % 30),  # A
                ((wa + wb) % 30, wa % 30),              # F
                ((-wb) % 30, wa % 30),                  # S
                ((-wa) % 30, (-wb) % 30),               # -I
            ]:
                cg = legendre_p(ga * ga + 2 * ga * gb + 2 * gb * gb, 3) * legendre_p(ga, 5)
                if cg != c0_val:
                    chi15_invariant_ok = False
            # Control 3: bad form a^2 + b^2 mod 3 flips under A!
            q_bad0 = (wa * wa + wb * wb) % 3
            wa1, wb1 = (2 * wa + wb) % 30, (wa + wb) % 30
            q_bad1 = (wa1 * wa1 + wb1 * wb1) % 3
            if q_bad1 != q_bad0:
                ctrl3_bad_q3_flips += 1

        # Check +-R_sigma stabilization:
        r_pos0 = ((-orb[0][0]) % 1, (orb[0][0] + orb[0][1]) % 1)
        r_neg0 = (orb[0][0] % 1, (-(orb[0][0] + orb[0][1])) % 1)
        if r_pos0 in orb:
            fix_v = [k for k, w in enumerate(orb) if ((-w[0]) % 1, (w[0] + w[1]) % 1) == w]
            assert len(fix_v) == 0
            bond_mirror_count += 1
        elif r_neg0 in orb:
            fix_v = [k for k, w in enumerate(orb) if (w[0] % 1, (-(w[0] + w[1])) % 1) == w]
            assert len(fix_v) == 2 and (fix_v[1] - fix_v[0]) == 6
            vertex_mirror_count += 1

    assert sorted(slow_counts_neg) == [3, 3, 6, 6] and slow_counts_pos == [0, 0, 0, 0]
    assert legendre_p(-3, 5) == -1
    assert chi15_invariant_ok and ctrl3_bad_q3_flips == 96
    assert bond_mirror_count == 4 and vertex_mirror_count == 4

    # Verify transitive <F, -I> action on the 4 orbits with chi_15 == +1 and the 4 orbits with chi_15 == -1:
    comp_sizes = []
    for sign_t in (1, -1):
        sub_idxs = [
            j for j, o in enumerate(orbits_8)
            if legendre_p(int(o[0][0] * 30) ** 2 + 2 * int(o[0][0] * 30) * int(o[0][1] * 30) + 2 * int(o[0][1] * 30) ** 2, 3)
            * legendre_p(int(o[0][0] * 30), 5) == sign_t
        ]
        vis = {sub_idxs[0]}
        qq = [sub_idxs[0]]
        while qq:
            cj = qq.pop(0)
            w_rep = orbits_8[cj][0]
            for img in [((w_rep[0] + w_rep[1]) % 1, w_rep[0] % 1), ((-w_rep[0]) % 1, (-w_rep[1]) % 1)]:
                nj = next(m for m, oo in enumerate(orbits_8) if img in oo)
                if nj not in vis:
                    vis.add(nj)
                    qq.append(nj)
        comp_sizes.append(len(vis))
    assert comp_sizes == [4, 4]

    # ================ E4: Standalone Lame Uniformization & Canonical Unit Contraction Norm ================
    with mp.workdps(45):
        omega_6 = mp.exp(I_MP * mp.pi / mp.mpf(3))
        tau_gold = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        tau_part = -mp.mpf(1) / (tau_gold - mp.mpf(1))  # 1/3 + i*sqrt(5)/3

        l2_om_r, l2_om_56, c_om = solve_l2_richardson(omega_6, 0)
        l2_i_r, _, c_i = solve_l2_richardson(I_MP, 0)
        l2_gold_r, _, c_gold = solve_l2_richardson(tau_gold, 6)
        l2_part_r, _, _ = solve_l2_richardson(tau_part, 8)

        assert abs(c_om) < mp.mpf(10) ** (-25) and abs(c_i) < mp.mpf(10) ** (-25)
        assert abs(mp.im(c_gold)) < mp.mpf(10) ** (-25)
        lame_rich_diff_om = abs(l2_om_r - l2_om_56)
        lame_mod_shift_err = abs((l2_part_r - l2_gold_r) - mp.log(abs(tau_gold - mp.mpf(1))))
        assert lame_rich_diff_om < mp.mpf(10) ** (-4)
        assert lame_mod_shift_err < mp.mpf(10) ** (-4)

    with mp.workdps(65):
        PHI = (mp.mpf(1) + mp.sqrt(mp.mpf(5))) / mp.mpf(2)
        tau_gold = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        l2_g = mp.mpf(mp.nstr(l2_gold_r, 32))
        l2_i = mp.mpf(mp.nstr(l2_i_r, 32))

        def pet_norm_S(tv: mp.mpc) -> mp.mpf:
            s1, s2, s3 = s_higgs_serre(tv)
            return mp.sqrt((mp.im(tv) ** (mp.mpf(3) / mp.mpf(2))) * (abs(s1) ** 2 + abs(s2) ** 2 + abs(s3) ** 2))

        lt_gold = l2_g + mp.log(mp.im(tau_gold)) / mp.mpf(2)
        lt_i = l2_i + mp.log(mp.im(I_MP)) / mp.mpf(2)
        lam_gold = pet_norm_S(tau_gold) * mp.sqrt(2 * mp.pi * lt_gold)
        lam_i = pet_norm_S(I_MP) * mp.sqrt(2 * mp.pi * lt_i)
        tau_Ag = (2 * tau_gold + 1) / (tau_gold + 1)
        lt_Ag = (l2_g + mp.log(abs(tau_gold + 1))) + mp.log(mp.im(tau_Ag)) / mp.mpf(2)
        lam_Ag = pet_norm_S(tau_Ag) * mp.sqrt(2 * mp.pi * lt_Ag)
        lam_inv_err = abs(lam_Ag - lam_gold)
        loop_mid_dev = abs((lam_i + lam_gold) / mp.mpf(2) - mp.mpf(1))
        assert lam_inv_err < mp.mpf(10) ** (-35)
        assert mp.mpf(9) / mp.mpf(10) < lam_i < lam_gold < mp.mpf(1)

        # Control 4: Omitting (Im tau)^{3/2} breaks SL(2, Z) invariance of ||S|| under A by > 1/10!
        s1a, s2a, s3a = s_higgs_serre(tau_gold)
        s1b, s2b, s3b = s_higgs_serre(tau_Ag)
        raw_s_diff = abs(mp.sqrt(abs(s1b) ** 2 + abs(s2b) ** 2 + abs(s3b) ** 2) - mp.sqrt(abs(s1a) ** 2 + abs(s2a) ** 2 + abs(s3a) ** 2))
        assert raw_s_diff > mp.mpf(1) / mp.mpf(10)

        # Raw sub-unit contraction check at tau_gold across all 3 sectors on Orbit 5:
        orb5 = next(o for o in orbits_8 if (Fr(1, 15), Fr(29, 30)) == o[0])
        max_raw_sigma = mp.mpf(0)
        for w in orb5:
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                ym, _ = yukawa_kahler(w[0], w[1], ql, qr, tau_gold, l2_g)
                s_top = mp.sqrt(max(eig_herm_asc(ym * ym.H)[0]))
                if s_top > max_raw_sigma:
                    max_raw_sigma = s_top
        assert max_raw_sigma < mp.mpf(4) / mp.mpf(5)

        # ================ E5: Multiplicative Waveguide Propagator vs Additive/Barrier + Haar U(3)^5 ================
        RHO_A = mmul3(RHO_T, mmul3(RHO_S, mmul3(RHO_Tinv, RHO_S)))
        U_A = mp.matrix([[mp.mpf(RHO_A[r][col]) for col in range(3)] for r in range(3)])
        fac_g = tau_gold + 1
        l2_Ag = l2_g + mp.log(abs(fac_g))
        ph_jg = fac_g / abs(fac_g)

        def step_phase(w_pt, ql, qr):
            w_nx = ((2 * w_pt[0] + w_pt[1]) % 1, (w_pt[0] + w_pt[1]) % 1)
            yn, _ = yukawa_kahler(w_nx[0], w_nx[1], ql, qr, tau_gold, l2_g)
            yA, _ = yukawa_kahler(w_pt[0], w_pt[1], ql, qr, tau_Ag, l2_Ag)
            yA = yA / ph_jg
            cand = U_A * yn * U_A.T
            r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
            sc = yA[r0, c0] / cand[r0, c0]
            return sc / abs(sc)

        # 1. 12-turn additive Gramian average on Orbit 5 (confirms B1944 / B1981 / A2-B1978 O4 wash-out & CP death):
        H_add_u = mp.zeros(3, 3)
        H_add_d = mp.zeros(3, 3)
        H_add_e = mp.zeros(3, 3)
        ua_n = mp.eye(3)
        for n in range(12):
            yu_n, _ = yukawa_kahler(orb5[n][0], orb5[n][1], 1, -4, tau_gold, l2_g)
            yd_n, _ = yukawa_kahler(orb5[n][0], orb5[n][1], 1, 2, tau_gold, l2_g)
            ye_n, _ = yukawa_kahler(orb5[n][0], orb5[n][1], -3, 6, tau_gold, l2_g)
            H_add_u += ua_n * (yu_n * yu_n.H) * ua_n.T / mp.mpf(12)
            H_add_d += ua_n * (yd_n * yd_n.H) * ua_n.T / mp.mpf(12)
            H_add_e += ua_n * (ye_n * ye_n.H) * ua_n.T / mp.mpf(12)
            ua_n = U_A * ua_n
        su_add, uu_add = eig_herm_asc(H_add_u)
        sd_add, ud_add = eig_herm_asc(H_add_d)
        se_add, _ = eig_herm_asc(H_add_e)
        vc_add = uu_add.H * ud_add
        j_add = abs(mp.im(vc_add[0, 0] * vc_add[1, 1] * mp.conj(vc_add[0, 1]) * mp.conj(vc_add[1, 0])))
        min_add_m23 = min(mp.sqrt(su_add[1] / su_add[2]), mp.sqrt(sd_add[1] / sd_add[2]), mp.sqrt(se_add[1] / se_add[2]))
        assert min_add_m23 > mp.mpf(1) / mp.mpf(2) and j_add < mp.mpf(10) ** (-40)

        # 2. Barrier-sign inversion check exp(-kappa * H_u) at kappa = 4 * ln(phi) on sheet 0:
        kap_bar = 4 * mp.log(PHI)
        yu_0, _ = yukawa_kahler(orb5[0][0], orb5[0][1], 1, -4, tau_gold, l2_g)
        bar_op = herm_func(yu_0 * yu_0.H, lambda x: mp.exp(-kap_bar * x))
        sb_bar, _ = eig_herm_asc(bar_op * bar_op.H)
        bar_m23 = mp.sqrt(sb_bar[1] / sb_bar[2])
        assert bar_m23 > mp.mpf(1) / mp.mpf(4)

        # 3. Unbroken-G_SM internal Gramian waveguide propagator on mirror-pinned Orbit 5 (K=3 & K=6, M_0=1) + Haar U(3)^5:
        def run_waveguide_gramian(orb, K_sh: int, u_tuple):
            UQ, Uu, Ud, UL_g, Ue = u_tuple
            yu_s = []
            yd_s = []
            ye_s = []
            ua_p = mp.eye(3)
            pu = mp.mpc(1)
            pd = mp.mpc(1)
            pe = mp.mpc(1)
            for n in range(K_sh):
                yu_r, _ = yukawa_kahler(orb[n][0], orb[n][1], 1, -4, tau_gold, l2_g)
                yd_r, _ = yukawa_kahler(orb[n][0], orb[n][1], 1, 2, tau_gold, l2_g)
                ye_r, _ = yukawa_kahler(orb[n][0], orb[n][1], -3, 6, tau_gold, l2_g)
                yu_s.append(UQ * (pu * (ua_p * yu_r * ua_p.T)) * Uu.H)
                yd_s.append(UQ * (pd * (ua_p * yd_r * ua_p.T)) * Ud.H)
                ye_s.append(UL_g * (pe * (ua_p * ye_r * ua_p.T)) * Ue.H)
                pu *= step_phase(orb[n], 1, -4)
                pd *= step_phase(orb[n], 1, 2)
                pe *= step_phase(orb[n], -3, 6)
                ua_p = U_A * ua_p

            chi_Q = [None] * K_sh
            chi_L = [None] * K_sh
            chi_Q[0] = mp.eye(3)
            chi_L[0] = mp.eye(3)
            for n in range(K_sh - 1):
                chi_Q[n + 1] = ((yu_s[n] * yu_s[n].H + yd_s[n] * yd_s[n].H) / mp.mpf(2)) * chi_Q[n]
                chi_L[n + 1] = (ye_s[n] * ye_s[n].H) * chi_L[n]

            chi_u = [None] * K_sh
            chi_d = [None] * K_sh
            chi_e = [None] * K_sh
            chi_u[K_sh - 1] = mp.eye(3)
            chi_d[K_sh - 1] = mp.eye(3)
            chi_e[K_sh - 1] = mp.eye(3)
            for n in range(K_sh - 2, -1, -1):
                chi_u[n] = (yu_s[n + 1].H * yu_s[n + 1]) * chi_u[n + 1]
                chi_d[n] = (yd_s[n + 1].H * yd_s[n + 1]) * chi_d[n + 1]
                chi_e[n] = (ye_s[n + 1].H * ye_s[n + 1]) * chi_e[n + 1]

            ZQ = mp.zeros(3, 3)
            ZL = mp.zeros(3, 3)
            Zu = mp.zeros(3, 3)
            Zd = mp.zeros(3, 3)
            Ze = mp.zeros(3, 3)
            Iu = mp.zeros(3, 3)
            Id = mp.zeros(3, 3)
            Ie = mp.zeros(3, 3)
            for n in range(K_sh):
                ZQ += chi_Q[n].H * chi_Q[n]
                ZL += chi_L[n].H * chi_L[n]
                Zu += chi_u[n].H * chi_u[n]
                Zd += chi_d[n].H * chi_d[n]
                Ze += chi_e[n].H * chi_e[n]
                Iu += chi_Q[n].H * yu_s[n] * chi_u[n]
                Id += chi_Q[n].H * yd_s[n] * chi_d[n]
                Ie += chi_L[n].H * ye_s[n] * chi_e[n]

            yeff_u = herm_func(ZQ, lambda x: 1 / mp.sqrt(x)) * Iu * herm_func(Zu, lambda x: 1 / mp.sqrt(x))
            yeff_d = herm_func(ZQ, lambda x: 1 / mp.sqrt(x)) * Id * herm_func(Zd, lambda x: 1 / mp.sqrt(x))
            yeff_e = herm_func(ZL, lambda x: 1 / mp.sqrt(x)) * Ie * herm_func(Ze, lambda x: 1 / mp.sqrt(x))
            su, uu = eig_herm_asc(yeff_u * yeff_u.H)
            sd, ud = eig_herm_asc(yeff_d * yeff_d.H)
            se, _ = eig_herm_asc(yeff_e * yeff_e.H)
            su = [mp.sqrt(x) for x in su]
            sd = [mp.sqrt(x) for x in sd]
            se = [mp.sqrt(x) for x in se]
            vc = uu.H * ud
            jcp = abs(mp.im(vc[0, 0] * vc[1, 1] * mp.conj(vc[0, 1]) * mp.conj(vc[1, 0])))
            md = min(abs(vc[0, 0]), abs(vc[1, 1]), abs(vc[2, 2]))
            obs12 = [
                su[1] / su[2], su[0] / su[2],
                sd[1] / sd[2], sd[0] / sd[2],
                se[1] / se[2], se[0] / se[2],
                sd[2] / su[2], se[2] / sd[2],
                abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]),
                jcp,
            ]
            return obs12, md, yu_s

        I3 = mp.eye(3)
        obs_k3, md_k3, _ = run_waveguide_gramian(orb5, 3, (I3, I3, I3, I3, I3))
        obs_k6, md_k6, yu_id = run_waveguide_gramian(orb5, 6, (I3, I3, I3, I3, I3))
        assert obs_k6[1] < mp.mpf(10) ** (-4) and obs_k6[3] < mp.mpf(10) ** (-4) and obs_k6[5] < mp.mpf(10) ** (-4)
        assert obs_k6[4] / obs_k6[2] > mp.mpf(3) / mp.mpf(2)
        assert md_k6 > mp.mpf(4) / mp.mpf(5) and obs_k6[11] > mp.mpf(10) ** (-4)

        # Companion 7-sheet staggered mirror-to-mirror chain on -R_sigma vertex-mirror Orbit 1:
        orb1 = next(o for o in orbits_8 if (Fr(1, 30), Fr(7, 30)) == o[0])
        k_fix1 = next(k for k in range(12) if (orb1[k][0] % 1, (-(orb1[k][0] + orb1[k][1])) % 1) == orb1[k])
        orb1_m7 = [orb1[(k_fix1 + n) % 12] for n in range(7)]

        def run_staggered_7(orb_m, u_tuple):
            UQ, Uu, Ud, UL_g, Ue = u_tuple
            res_sec = []
            for (ql, qr), Ul, Ur in [((1, -4), UQ, Uu), ((1, 2), UQ, Ud), ((-3, 6), UL_g, Ue)]:
                ys = []
                ua_p = mp.eye(3)
                ph = mp.mpc(1)
                for n in range(7):
                    ym, _ = yukawa_kahler(orb_m[n][0], orb_m[n][1], ql, qr, tau_gold, l2_g)
                    ys.append(Ul * (ph * (ua_p * ym * ua_p.T)) * Ur.H)
                    ph *= step_phase(orb_m[n], ql, qr)
                    ua_p = U_A * ua_p
                prod7 = ys[0] * ys[1].H * ys[2] * ys[3].H * ys[4] * ys[5].H * ys[6]
                sv, uv = eig_herm_asc(prod7 * prod7.H)
                res_sec.append(([mp.sqrt(x) for x in sv], uv))
            (su7, uu7), (sd7, ud7), (se7, _) = res_sec
            vc7 = uu7.H * ud7
            j7 = abs(mp.im(vc7[0, 0] * vc7[1, 1] * mp.conj(vc7[0, 1]) * mp.conj(vc7[1, 0])))
            md7 = min(abs(vc7[0, 0]), abs(vc7[1, 1]), abs(vc7[2, 2]))
            return [su7[1] / su7[2], su7[0] / su7[2], sd7[1] / sd7[2], sd7[0] / sd7[2], se7[1] / se7[2], se7[0] / se7[2], abs(vc7[0, 1]), abs(vc7[1, 2]), abs(vc7[0, 2]), j7], md7

        obs_stag7, md_stag7 = run_staggered_7(orb1_m7, (I3, I3, I3, I3, I3))
        assert md_stag7 > mp.mpf(95) / mp.mpf(100) and obs_stag7[9] > mp.mpf(10) ** (-4)

        # Control 5 (Guardrail 3): 5 independent rational-Cayley U(3) transformations!
        UQ_c = cayley_u3((3, -2, 4, -5, 1, 3, -4, 2, 5))
        Uu_c = cayley_u3((-3, 5, -1, 2, -4, 1, 5, -3, 2))
        Ud_c = cayley_u3((3, 4, -2, -3, 1, 5, 4, -2, 3))
        UL_c = cayley_u3((1, -5, 2, 4, -1, -3, -2, 3, 5))
        Ue_c = cayley_u3((-2, 3, -4, -2, 5, 1, 3, -4, -2))
        obs_k6_h, _, yu_h = run_waveguide_gramian(orb5, 6, (UQ_c, Uu_c, Ud_c, UL_c, Ue_c))
        obs_stag7_h, _ = run_staggered_7(orb1_m7, (UQ_c, Uu_c, Ud_c, UL_c, Ue_c))
        haar_err_k6 = max(abs(obs_k6[i] - obs_k6_h[i]) for i in range(12))
        haar_err_stag7 = max(abs(obs_stag7[i] - obs_stag7_h[i]) for i in range(10))
        assert haar_err_k6 < mp.mpf(10) ** (-45) and haar_err_stag7 < mp.mpf(10) ** (-45)

        # Planted non-gauge-covariant raw product Y_5 * Y_4 * ... * Y_0 without adjoints fails U_R invariance!
        raw_id = yu_id[5] * yu_id[4] * yu_id[3] * yu_id[2] * yu_id[1] * yu_id[0]
        raw_h = yu_h[5] * yu_h[4] * yu_h[3] * yu_h[2] * yu_h[1] * yu_h[0]
        s_raw_id = [mp.sqrt(x) for x in eig_herm_asc(raw_id * raw_id.H)[0]]
        s_raw_h = [mp.sqrt(x) for x in eig_herm_asc(raw_h * raw_h.H)[0]]
        ctrl5_bad_prod_drift = abs(s_raw_id[1] / s_raw_id[2] - s_raw_h[1] / s_raw_h[2])
        assert ctrl5_bad_prod_drift > mp.mpf(1) / mp.mpf(10)

    out = {
        "card": "AGY-C51",
        "empirical_inputs": "0 of 19",
        "ast_firewall": ast_res,
        "E1_cube_group_and_p882": {
            "so3_z_order": len(so3_z),
            "so3_z_element_orders": order_hist,
            "primitive_order30_count": len(seen_576),
            "x30_cusp_count": len(seen_576) // 2,
            "A12_fixed_points_count": len(fixed_A12),
            "A12_fixed_cusps_count": len(fixed_A12) // 2,
            "max_p882_word_homomorphism_rel_err": mp.nstr(max_p882_err, 12),
            "antiholomorphic_conj_rel_errs": {
                "J0": mp.nstr(err_J0, 12),
                "R_sigma": mp.nstr(err_Rsig, 12),
                "F_half_shift": mp.nstr(err_F, 12),
            },
            "weave_LR_RL_conjugation_rel_err": mp.nstr(err_weave_RL, 12),
            "control_1_noshift_err": mp.nstr(ctrl1_noshift_err, 10),
            "control_1_wrong_inverse_sv_err": mp.nstr(ctrl1_inv_sv_err, 10),
        },
        "E2_lepton_two_fifths_theorem": {
            "order30_nonzero_5part_points": len(pts_480),
            "order10_surjective_images": len(pts_60_order10),
            "fiber_multiplicity_3w": 8,
            "max_b1973_nonorm_sv0_over_sv1": mp.nstr(max_b1973_rank1_ratio, 12),
            "raw_theta_eps_valuations_4reps": raw_theta_exp_pairs,
            "converged_m2_over_m3_rate_set_all60": sorted(r23_set),
            "converged_m1_over_m3_rate_set_all60": sorted(r13_set),
            "max_m2_over_m3_deviation_from_2_over_5": mp.nstr(max_25_err, 12),
            "control_2_a5_zero_min_deviation": mp.nstr(ctrl2_min_dev, 10),
        },
        "E3_legendre_jacobi_and_mirrors": {
            "orbit_count": len(orbits_8),
            "orbit_length": 12,
            "slow_counts_mod5_nonresidue": sorted(slow_counts_neg),
            "slow_counts_mod5_residue": sorted(slow_counts_pos),
            "lepton_charge_legendre_mod5": legendre_p(-3, 5),
            "chi15_isom_m004_invariant": chi15_invariant_ok,
            "isom_m004_orbit_component_sizes": comp_sizes,
            "plus_R_sigma_bond_mirror_orbits": bond_mirror_count,
            "minus_R_sigma_vertex_mirror_orbits": vertex_mirror_count,
            "control_3_bad_q3_flips_of_96": ctrl3_bad_q3_flips,
        },
        "E4_standalone_lame_and_unit_contraction": {
            "L2_omega_richardson": mp.nstr(l2_om_r, 16),
            "L2_i_richardson": mp.nstr(l2_i_r, 16),
            "L2_tau_gold_richardson": mp.nstr(l2_gold_r, 16),
            "c_tau_gold_real": mp.nstr(mp.re(c_gold), 16),
            "c_tau_gold_abs_imag": mp.nstr(abs(mp.im(c_gold)), 10),
            "lame_modular_shift_err": mp.nstr(lame_mod_shift_err, 10),
            "Lambda_geom_i": mp.nstr(lam_i, 12),
            "Lambda_geom_tau_gold": mp.nstr(lam_gold, 12),
            "Lambda_geom_loop_midpoint_dev_from_1": mp.nstr(loop_mid_dev, 10),
            "Lambda_geom_SL2Z_invariance_err": mp.nstr(lam_inv_err, 10),
            "max_raw_kahler_sigma_orbit5": mp.nstr(max_raw_sigma, 10),
            "control_4_no_kahler_weight_drift": mp.nstr(raw_s_diff, 10),
        },
        "E5_waveguide_propagator_and_haar": {
            "additive_12turn_min_m2_over_m3": mp.nstr(min_add_m23, 10),
            "additive_12turn_jarlskog_abs": mp.nstr(j_add, 10),
            "barrier_sign_up_m2_over_m3": mp.nstr(bar_m23, 10),
            "waveguide_gramian_K3_orbit5": {
                "up_ratios": [mp.nstr(obs_k3[0], 8), mp.nstr(obs_k3[1], 8)],
                "down_ratios": [mp.nstr(obs_k3[2], 8), mp.nstr(obs_k3[3], 8)],
                "lep_ratios": [mp.nstr(obs_k3[4], 8), mp.nstr(obs_k3[5], 8)],
                "ckm_moduli_and_min_diag": [mp.nstr(obs_k3[8], 8), mp.nstr(obs_k3[9], 8), mp.nstr(obs_k3[10], 8), mp.nstr(md_k3, 8)],
                "jarlskog_abs": mp.nstr(obs_k3[11], 8),
            },
            "waveguide_gramian_K6_orbit5": {
                "up_ratios": [mp.nstr(obs_k6[0], 8), mp.nstr(obs_k6[1], 8)],
                "down_ratios": [mp.nstr(obs_k6[2], 8), mp.nstr(obs_k6[3], 8)],
                "lep_ratios": [mp.nstr(obs_k6[4], 8), mp.nstr(obs_k6[5], 8)],
                "inter_sector_yb_yt_and_ytau_yb": [mp.nstr(obs_k6[6], 8), mp.nstr(obs_k6[7], 8)],
                "ckm_moduli_and_min_diag": [mp.nstr(obs_k6[8], 8), mp.nstr(obs_k6[9], 8), mp.nstr(obs_k6[10], 8), mp.nstr(md_k6, 8)],
                "jarlskog_abs": mp.nstr(obs_k6[11], 8),
            },
            "staggered_7sheet_orbit1": {
                "up_ratios": [mp.nstr(obs_stag7[0], 8), mp.nstr(obs_stag7[1], 8)],
                "down_ratios": [mp.nstr(obs_stag7[2], 8), mp.nstr(obs_stag7[3], 8)],
                "lep_ratios": [mp.nstr(obs_stag7[4], 8), mp.nstr(obs_stag7[5], 8)],
                "ckm_moduli_and_min_diag": [mp.nstr(obs_stag7[6], 8), mp.nstr(obs_stag7[7], 8), mp.nstr(obs_stag7[8], 8), mp.nstr(md_stag7, 8)],
                "jarlskog_abs": mp.nstr(obs_stag7[9], 8),
            },
            "control_5_cayley_u3_5_max_err_K6": mp.nstr(haar_err_k6, 10),
            "control_5_cayley_u3_5_max_err_stag7": mp.nstr(haar_err_stag7, 10),
            "control_5_planted_noncovariant_product_drift": mp.nstr(ctrl5_bad_prod_drift, 10),
        },
        "all_controls_passed": bool(
            max_p882_err < mp.mpf(10) ** (-50)
            and ctrl1_noshift_err > mp.mpf(1) / mp.mpf(100)
            and max_25_err < mp.mpf(10) ** (-9)
            and ctrl2_min_dev > mp.mpf(1) / mp.mpf(10)
            and chi15_invariant_ok
            and ctrl3_bad_q3_flips == 96
            and lam_inv_err < mp.mpf(10) ** (-35)
            and raw_s_diff > mp.mpf(1) / mp.mpf(10)
            and haar_err_k6 < mp.mpf(10) ** (-45)
            and ctrl5_bad_prod_drift > mp.mpf(1) / mp.mpf(10)
        ),
    }
    payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    OUT_HASH.write_text(f"{digest}  c51_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
