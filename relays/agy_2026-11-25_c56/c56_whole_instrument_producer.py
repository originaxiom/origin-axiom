#!/usr/bin/env python3
"""Card AGY-C56 Standalone Producer (Strictly 0 of 19; python3 -I; stdlib + mpmath only).

Forward remediation of AGY-C53 closing D1..D5: proves and verifies E1..E5 and Planted Controls 1..6
with zero float/complex AST literals or calls, zero external repo/table imports, zero runtime script-hash
overwrites, and zero empirical Standard-Model or experimental values."""
import ast
from fractions import Fraction as Fr
import json
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "c56_out.json"

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
    k_lim = int(mp.ceil(mp.mpf(mp.mp.dps + 8) * mp.log(10) / (2 * mp.pi * y))) + 6
    for k_sum in range(-k_lim, k_lim + 1):
        m_val = f2m(a_r) + k_sum
        if m_val == 0:
            continue
        w_val = mp.exp(-2 * mp.pi * abs(m_val) * y + 2 * I_MP * mp.pi * (m_val * mp.re(tv) + f2m(u2)))
        tot += (2 * mp.pi / abs(m_val)) * mp.re(w_val / (1 - w_val))
    return first + zrow + tot


def yukawa_kahler(pa: Fr, pb: Fr, ql: int, qr: int, tv: mp.mpc, l_end: mp.mpf, with_norm: bool = True, return_parts: bool = False):
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
    q_mod = mp.exp(2 * I_MP * mp.pi * tv)
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * tv / 12) * mp.qp(q_mod)) ** 3
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
    r_map = {}
    n_map = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hr, cs[sk][1] - hr
        dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
        if not ((al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0)):
            r_res = kap[sk] * thc_hol(cs[sk][0], cs[sk][1], tv) * thc_hol(ds[sk][0], ds[sk][1], tv) / t1p
            r_map[sk] = r_res
            if with_norm:
                zv = f2m(al) * tv + f2m(be)
                a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_fn, zv) / th1_fn(zv)
                c_ch = f_u_mp(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
                n_val = mp.sqrt(2 * mp.pi * l_end + c_ch)
                n_map[sk] = n_val
                mw = mw + n_val * r_res * ed[sk]
            else:
                n_map[sk] = mp.mpf(1)
                mw = mw + r_res * ed[sk]
        else:
            r_map[sk] = mp.mpc(0)
            n_map[sk] = mp.mpf(0)
    ym = mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])
    if return_parts:
        return mp.sqrt(y) * ym, mw, r_map, n_map
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

    # ================ E1: SO(3, Z) ~= S_4 Cube Homomorphism, Unitary Generator + Cusp Proof (P-882), & det = -1 Law ================
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

    with mp.workdps(70):
        tau_ref = mp.mpc(mp.mpf(27) / mp.mpf(100), mp.mpf(151) / mp.mpf(100))
        l_ref = mp.mpf(53) / mp.mpf(20)
        w_base = (Fr(0, 30), Fr(1, 30))

        # D4 Part 1: Verify generators T, S, -I_2 across all 8 orbit reps (8 x 3 x 3 = 72 sector matrices) with | |sc| - 1 | < 10^-50!
        gen_list = [
            ((1, 1, 0, 1), RHO_T),
            ((0, -1, 1, 0), RHO_S),
            ((-1, 0, 0, -1), RHO_I),
        ]
        max_gen_err = mp.mpf(0)
        max_sc_mod_dev = mp.mpf(0)
        gen_matrices_checked = 0
        for orb in orbits_8:
            wp = orb[0]
            for (ga, gb, gc, gd), Rg_tup in gen_list:
                Rm_g = mp.matrix([[mp.mpf(Rg_tup[r][col]) for col in range(3)] for r in range(3)])
                fac_g = gc * tau_ref + gd
                tau_g = (ga * tau_ref + gb) / fac_g
                l_g = l_ref + mp.log(abs(fac_g))
                ph_g = fac_g / abs(fac_g)
                # gamma^{-1} = [[gd, -gb], [-gc, ga]]; w * gamma^{-1} = (w0*gd - w1*gc, -w0*gb + w1*ga)
                w_inv = ((wp[0] * gd - wp[1] * gc) % 1, (-wp[0] * gb + wp[1] * ga) % 1)
                for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                    y0, _ = yukawa_kahler(wp[0], wp[1], ql, qr, tau_ref, l_ref)
                    y1, _ = yukawa_kahler(w_inv[0], w_inv[1], ql, qr, tau_g, l_g)
                    y1 = y1 / ph_g
                    cand = Rm_g * y0 * Rm_g.T
                    r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                    sc = y1[r0, c0] / cand[r0, c0]
                    sc_dev = abs(abs(sc) - mp.mpf(1))
                    err = mp.mnorm(y1 - sc * cand, "F") / mp.mnorm(y0, "F")
                    if sc_dev > max_sc_mod_dev:
                        max_sc_mod_dev = sc_dev
                    if err > max_gen_err:
                        max_gen_err = err
                    gen_matrices_checked += 1
        assert gen_matrices_checked == 72

        # D4 Part 2: Verify 16 multi-step BFS cusp words (8 A^12-fixed + 8 off-A^12 = 48 sector matrices) with | |sc| - 1 | < 10^-50!
        cusps_gold_sample = [k for k in fixed_A12 if abs(seen_576[k][0][2]) <= 8][:8]
        cusps_off_sample = [k for k in seen_576 if (k[1] - 2 * k[0]) % 5 != 0 and abs(seen_576[k][0][2]) <= 6][:8]
        assert len(cusps_gold_sample) == 8 and len(cusps_off_sample) == 8

        max_p882_err = mp.mpf(0)
        cusp_matrices_checked = 0
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
                y_cusp, _ = yukawa_kahler(w_base[0], w_base[1], ql, qr, tau_c, l_c)
                y_cusp = y_cusp / ph_j
                cand = Rm * y_inf * Rm.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = y_cusp[r0, c0] / cand[r0, c0]
                sc_dev = abs(abs(sc) - mp.mpf(1))
                err = mp.mnorm(y_cusp - sc * cand, "F") / mp.mnorm(y_inf, "F")
                if sc_dev > max_sc_mod_dev:
                    max_sc_mod_dev = sc_dev
                if err > max_p882_err:
                    max_p882_err = err
                cusp_matrices_checked += 1
        assert cusp_matrices_checked == 48
        assert max_gen_err < mp.mpf(10) ** (-50) and max_p882_err < mp.mpf(10) ** (-50)
        assert max_sc_mod_dev < mp.mpf(10) ** (-50)

        # Control 1: Omitting ln|c*tau + d| OR swapping gamma <-> gamma^{-1} breaks P-882 by > 1/100!
        cm_c1, dm_c1 = (1, 1)
        (a1, b1, c1, d1), R1 = seen_576[(cm_c1, dm_c1)]
        Rm1 = mp.matrix([[mp.mpf(R1[r][col]) for col in range(3)] for r in range(3)])
        fac1 = c1 * tau_ref + d1
        tau_c1 = (a1 * tau_ref + b1) / fac1
        yi_c1, _ = yukawa_kahler(Fr(cm_c1, 30), Fr(dm_c1, 30), 1, -4, tau_ref, l_ref)
        yc_noshift, _ = yukawa_kahler(w_base[0], w_base[1], 1, -4, tau_c1, l_ref)
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

        # Antiholomorphic (det = -1) laws under J_0, R_sigma, F and weave RL = R(LR)R^{-1} with | |sc| - 1 | < 10^-50!
        o3_mp = (
            [mp.matrix([[mp.mpf(g[r][col]) for col in range(3)] for r in range(3)]) for g in so3_z]
            + [mp.matrix([[mp.mpf(-g[r][col]) for col in range(3)] for r in range(3)]) for g in so3_z]
        )
        w0_a = (Fr(4, 15), Fr(1, 30))

        def check_antihol_conj(tau1, fac_bar, w1):
            nonlocal max_sc_mod_dev
            l1 = l_ref + mp.log(abs(fac_bar))
            ph = fac_bar / abs(fac_bar)
            yu0, _ = yukawa_kahler(w0_a[0], w0_a[1], 1, -4, tau_ref, l_ref)
            yu1, _ = yukawa_kahler(w1[0], w1[1], 1, -4, tau1, l1)
            yu1 = yu1 / ph
            yu0_bar = mp.matrix([[mp.conj(yu0[r, col]) for col in range(3)] for r in range(3)])
            best_e = mp.mpf(999)
            best_R = None
            best_sc_u = mp.mpc(0)
            for Rm in o3_mp:
                cand = Rm * yu0_bar * Rm.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = yu1[r0, c0] / cand[r0, c0]
                err = mp.mnorm(yu1 - sc * cand, "F") / mp.mnorm(yu0, "F")
                if err < best_e:
                    best_e = err
                    best_R = Rm
                    best_sc_u = sc
            max_sc_mod_dev = max(max_sc_mod_dev, abs(abs(best_sc_u) - mp.mpf(1)))
            for ql, qr in [(1, 2), (-3, 6)]:
                yf0, _ = yukawa_kahler(w0_a[0], w0_a[1], ql, qr, tau_ref, l_ref)
                yf1, _ = yukawa_kahler(w1[0], w1[1], ql, qr, tau1, l1)
                yf1 = yf1 / ph
                yf0_bar = mp.matrix([[mp.conj(yf0[r, col]) for col in range(3)] for r in range(3)])
                cand = best_R * yf0_bar * best_R.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = yf1[r0, c0] / cand[r0, c0]
                max_sc_mod_dev = max(max_sc_mod_dev, abs(abs(sc) - mp.mpf(1)))
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
        max_sc_mod_dev = max(max_sc_mod_dev, abs(abs(sc_RL) - mp.mpf(1)))
        err_weave_RL = mp.mnorm(yu_RL - sc_RL * cand_RL, "F") / mp.mnorm(yu_LR, "F")
        assert err_weave_RL < mp.mpf(10) ** (-50) and max_sc_mod_dev < mp.mpf(10) ** (-50)

    # ================ E2: Exact Lepton 2/5 Cusp Rate Proof + Explicit 3/5 - 1/5 Valuation Step (D5.1) ================
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
        max_quad_3_over_5_err = mp.mpf(0)
        max_sv1sq_1_over_5_err = mp.mpf(0)
        min_norm_sq_gap = mp.mpf(999)
        raw_theta_exp_pairs = []
        for a10, b10 in [(1, 0), (2, 1), (3, 0), (4, 1)]:
            _, mw_nonorm = yukawa_kahler(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 40), l_asym, with_norm=False)
            _, sv_mw0, _ = mp.svd_c(mw_nonorm)
            sv_mw0 = sorted(list(sv_mw0))
            rat0 = sv_mw0[0] / sv_mw0[1]
            if rat0 > max_b1973_rank1_ratio:
                max_b1973_rank1_ratio = rat0

            # Explicit D5.1 check on y=40 -> 50 via pure-theta numerators T_sk = t1p * r_sk: rate(|T_1^2 + T_i^2|) == 3/5, rate(|T_j^2 + T_k^2|) == 3/5, rate(|t1p|^2 sv_1^2) == 1/5!
            t40, t50 = mp.mpc(0, 40), mp.mpc(0, 50)
            t1p40 = 2 * mp.pi * (mp.exp(I_MP * mp.pi * t40 / 12) * mp.qp(mp.exp(2 * I_MP * mp.pi * t40))) ** 3
            t1p50 = 2 * mp.pi * (mp.exp(I_MP * mp.pi * t50 / 12) * mp.qp(mp.exp(2 * I_MP * mp.pi * t50))) ** 3
            _, mw40, rm40, nm40 = yukawa_kahler(Fr(a10, 30), Fr(b10, 30), -3, 6, t40, l_asym, with_norm=True, return_parts=True)
            _, mw50, rm50, _ = yukawa_kahler(Fr(a10, 30), Fr(b10, 30), -3, 6, t50, l_asym, with_norm=True, return_parts=True)
            q1i_40 = abs((t1p40 * rm40["1"]) ** 2 + (t1p40 * rm40["i"]) ** 2)
            q1i_50 = abs((t1p50 * rm50["1"]) ** 2 + (t1p50 * rm50["i"]) ** 2)
            qjk_40 = abs((t1p40 * rm40["j"]) ** 2 + (t1p40 * rm40["k"]) ** 2)
            qjk_50 = abs((t1p50 * rm50["j"]) ** 2 + (t1p50 * rm50["k"]) ** 2)
            rate_1i = -mp.log(q1i_50 / q1i_40) / (10 * mp.pi)
            rate_jk = -mp.log(qjk_50 / qjk_40) / (10 * mp.pi)
            _, svm40, _ = mp.svd_c(mw40)
            _, svm50, _ = mp.svd_c(mw50)
            sv1_40 = abs(t1p40) * sorted(list(svm40))[1]
            sv1_50 = abs(t1p50) * sorted(list(svm50))[1]
            rate_sv1sq = -mp.log((sv1_50 ** 2) / (sv1_40 ** 2)) / (10 * mp.pi)
            nsq_gap = abs((nm40["1"] ** 2) - (nm40["j"] ** 2))
            max_quad_3_over_5_err = max(max_quad_3_over_5_err, abs(rate_1i - mp.mpf(3) / mp.mpf(5)), abs(rate_jk - mp.mpf(3) / mp.mpf(5)))
            max_sv1sq_1_over_5_err = max(max_sv1sq_1_over_5_err, abs(rate_sv1sq - mp.mpf(1) / mp.mpf(5)))
            min_norm_sq_gap = min(min_norm_sq_gap, nsq_gap)

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
        assert max_quad_3_over_5_err < mp.mpf(10) ** (-20)
        assert max_sv1sq_1_over_5_err < mp.mpf(10) ** (-10)
        assert min_norm_sq_gap > mp.mpf(1)

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
        assert ctrl2_min_dev > mp.mpf(1) / mp.mpf(2)

    # ================ E3: Bijective ((q_3/3), (a_5/5)) Character Table & 16 True +-R_sigma Mirror Chains ================
    slow_counts_neg = []
    slow_counts_pos = []
    chi15_invariant_ok = True
    ctrl3_bad_q3_flips = 0
    bond_chains_8 = []    # (orb_idx, half_idx, leg3, leg5, chain_6)
    vertex_chains_8 = []  # (orb_idx, half_idx, leg3, leg5, chain_7)
    pair_char_sigs = {}

    for idx, orb in enumerate(orbits_8):
        ia0, ib0 = int(orb[0][0] * 30), int(orb[0][1] * 30)
        leg3 = legendre_p(ia0 * ia0 + 2 * ia0 * ib0 + 2 * ib0 * ib0, 3)
        leg5 = legendre_p(ia0, 5)
        c0_val = leg3 * leg5
        neg0 = ((-orb[0][0]) % 1, (-orb[0][1]) % 1)
        neg_idx = next(j for j, o in enumerate(orbits_8) if neg0 in o)
        pair_key = (min(idx, neg_idx), max(idx, neg_idx))
        pair_char_sigs[pair_key] = (leg3, leg5)

        slow_c = sum(1 for w in orb if min(w[0], 1 - w[0]) in (Fr(7, 30), Fr(8, 30)))
        if leg5 == -1:
            slow_counts_neg.append(slow_c)
        else:
            slow_counts_pos.append(slow_c)

        for w in orb:
            wa, wb = int(w[0] * 30), int(w[1] * 30)
            for ga, gb in [
                ((2 * wa + wb) % 30, (wa + wb) % 30),
                ((wa + wb) % 30, wa % 30),
                ((-wb) % 30, wa % 30),
                ((-wa) % 30, (-wb) % 30),
            ]:
                cg = legendre_p(ga * ga + 2 * ga * gb + 2 * gb * gb, 3) * legendre_p(ga, 5)
                if cg != c0_val:
                    chi15_invariant_ok = False
            q_bad0 = (wa * wa + wb * wb) % 3
            wa1, wb1 = (2 * wa + wb) % 30, (wa + wb) % 30
            q_bad1 = (wa1 * wa1 + wb1 * wb1) % 3
            if q_bad1 != q_bad0:
                ctrl3_bad_q3_flips += 1

        r_pos0 = ((-orb[0][0]) % 1, (orb[0][0] + orb[0][1]) % 1)
        r_neg0 = (orb[0][0] % 1, (-(orb[0][0] + orb[0][1])) % 1)
        if r_pos0 in orb:
            assert leg3 == 1
            bonds = sorted(k for k in range(12) if ((-orb[k][0]) % 1, (orb[k][0] + orb[k][1]) % 1) == orb[(k + 1) % 12])
            assert len(bonds) == 2 and (bonds[1] - bonds[0]) == 6
            for hi, kb in enumerate(bonds):
                bond_chains_8.append((idx, hi, leg3, leg5, [orb[(kb + 1 + n) % 12] for n in range(6)]))
        elif r_neg0 in orb:
            assert leg3 == -1
            verts = sorted(k for k in range(12) if (orb[k][0] % 1, (-(orb[k][0] + orb[k][1])) % 1) == orb[k])
            assert len(verts) == 2 and (verts[1] - verts[0]) == 6
            for hi, kv in enumerate(verts):
                vertex_chains_8.append((idx, hi, leg3, leg5, [orb[(kv + n) % 12] for n in range(7)]))
        else:
            raise AssertionError("Orbit missing +-R_sigma mirror")

    assert sorted(slow_counts_neg) == [3, 3, 6, 6] and slow_counts_pos == [0, 0, 0, 0]
    assert legendre_p(-3, 5) == -1
    assert chi15_invariant_ok and ctrl3_bad_q3_flips == 96
    assert len(bond_chains_8) == 8 and len(vertex_chains_8) == 8
    assert len(pair_char_sigs) == 4 and set(pair_char_sigs.values()) == {(1, 1), (1, -1), (-1, 1), (-1, -1)}

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

    # ================ E4: Standalone Lame Uniformization & All-96-Point Sub-Unit Contraction ================
    with mp.workdps(45):
        omega_6 = mp.exp(I_MP * mp.pi / mp.mpf(3))
        tau_gold = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        tau_part = -mp.mpf(1) / (tau_gold - mp.mpf(1))

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

    with mp.workdps(60):
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
        assert lam_inv_err < mp.mpf(10) ** (-35)
        assert mp.mpf(9) / mp.mpf(10) < lam_i < lam_gold < mp.mpf(1)

        s1a, s2a, s3a = s_higgs_serre(tau_gold)
        s1b, s2b, s3b = s_higgs_serre(tau_Ag)
        raw_s_diff = abs(mp.sqrt(abs(s1b) ** 2 + abs(s2b) ** 2 + abs(s3b) ** 2) - mp.sqrt(abs(s1a) ** 2 + abs(s2a) ** 2 + abs(s3a) ** 2))
        assert raw_s_diff > mp.mpf(1) / mp.mpf(10)

        # Control 6: mp.jtheta(2, 0, q) principal branch cut jumps by > 9 at Re(tau_Ag) = 11/7 > 1!
        q_ag = mp.exp(I_MP * mp.pi * tau_Ag)
        qm_ag = mp.exp(2 * I_MP * mp.pi * tau_Ag)
        t1p_hol_ag = 2 * mp.pi * (mp.exp(I_MP * mp.pi * tau_Ag / 12) * mp.qp(qm_ag)) ** 3
        t1p_cut_ag = mp.pi * mp.jtheta(2, 0, q_ag) * mp.jtheta(3, 0, q_ag) * mp.jtheta(4, 0, q_ag)
        ctrl6_jtheta2_cut_jump = abs(t1p_hol_ag - t1p_cut_ag)
        assert ctrl6_jtheta2_cut_jump > mp.mpf(9)

        # Cache yukawa_kahler at tau_gold and tau_Ag across ALL 96 P96 points (288 matrices) and check |sc| == 1 & sub-unit contraction!
        RHO_A = mmul3(RHO_T, mmul3(RHO_S, mmul3(RHO_Tinv, RHO_S)))
        U_A = mp.matrix([[mp.mpf(RHO_A[r][col]) for col in range(3)] for r in range(3)])
        fac_g = tau_gold + 1
        l2_Ag = l2_g + mp.log(abs(fac_g))
        ph_jg = fac_g / abs(fac_g)

        yk_gold = {}
        yk_Ag = {}
        max_raw_sigma_all96 = mp.mpf(0)
        for w in pts_96_frac:
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                ym_g, _ = yukawa_kahler(w[0], w[1], ql, qr, tau_gold, l2_g)
                ym_a, _ = yukawa_kahler(w[0], w[1], ql, qr, tau_Ag, l2_Ag)
                yk_gold[(w, ql, qr)] = ym_g
                yk_Ag[(w, ql, qr)] = ym_a / ph_jg
                s_top = mp.sqrt(max(eig_herm_asc(ym_g * ym_g.H)[0]))
                if s_top > max_raw_sigma_all96:
                    max_raw_sigma_all96 = s_top
        assert max_raw_sigma_all96 < mp.mpf(17) / mp.mpf(20)

        step_ph_map = {}
        max_step_sc_dev = mp.mpf(0)
        for w in pts_96_frac:
            w_nx = ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                yn = yk_gold[(w_nx, ql, qr)]
                yA = yk_Ag[(w, ql, qr)]
                cand = U_A * yn * U_A.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = yA[r0, c0] / cand[r0, c0]
                sc_dev = abs(abs(sc) - mp.mpf(1))
                if sc_dev > max_step_sc_dev:
                    max_step_sc_dev = sc_dev
                step_ph_map[(w, ql, qr)] = sc / abs(sc)
        assert max_step_sc_dev < mp.mpf(10) ** (-45)

        # ================ E5: Full 16-Chain Polynomial Gramian & 8-Chain Stag7 Menu + U(3)^5 Scrambling ================
        # 1. 12-turn additive Gramian average across ALL 8 orbits:
        min_add_m23_all8 = mp.mpf(999)
        max_add_jarlskog_all8 = mp.mpf(0)
        for orb in orbits_8:
            H_add_u = mp.zeros(3, 3)
            H_add_d = mp.zeros(3, 3)
            H_add_e = mp.zeros(3, 3)
            ua_n = mp.eye(3)
            for n in range(12):
                yu_n = yk_gold[(orb[n], 1, -4)]
                yd_n = yk_gold[(orb[n], 1, 2)]
                ye_n = yk_gold[(orb[n], -3, 6)]
                H_add_u += ua_n * (yu_n * yu_n.H) * ua_n.T / mp.mpf(12)
                H_add_d += ua_n * (yd_n * yd_n.H) * ua_n.T / mp.mpf(12)
                H_add_e += ua_n * (ye_n * ye_n.H) * ua_n.T / mp.mpf(12)
                ua_n = U_A * ua_n
            su_add, uu_add = eig_herm_asc(H_add_u)
            sd_add, ud_add = eig_herm_asc(H_add_d)
            se_add, _ = eig_herm_asc(H_add_e)
            vc_add = uu_add.H * ud_add
            j_add = abs(mp.im(vc_add[0, 0] * vc_add[1, 1] * mp.conj(vc_add[0, 1]) * mp.conj(vc_add[1, 0])))
            m23 = min(mp.sqrt(su_add[1] / su_add[2]), mp.sqrt(sd_add[1] / sd_add[2]), mp.sqrt(se_add[1] / se_add[2]))
            min_add_m23_all8 = min(min_add_m23_all8, m23)
            max_add_jarlskog_all8 = max(max_add_jarlskog_all8, j_add)
        assert min_add_m23_all8 > mp.mpf(9) / mp.mpf(20) and max_add_jarlskog_all8 < mp.mpf(10) ** (-40)

        # 2. Positive-barrier control exp(-kappa * H_u) at kappa = 4 * ln(phi) on Bond Orbit 0 Half 0 sheet 0:
        kap_bar = 4 * mp.log(PHI)
        yu_b0 = yk_gold[(bond_chains_8[0][4][0], 1, -4)]
        bar_op = herm_func(yu_b0 * yu_b0.H, lambda x: mp.exp(-kap_bar * x))
        sb_bar, _ = eig_herm_asc(bar_op * bar_op.H)
        bar_m23 = mp.sqrt(sb_bar[1] / sb_bar[2])
        assert bar_m23 > mp.mpf(2) / mp.mpf(3)

        # 3. Polynomial internal Gramian waveguide across ALL 16 true mirror chains (8 bond 6-sheet + 8 vertex 7-sheet):
        def run_waveguide_gramian(chain, u_tuple):
            UQ, Uu, Ud, UL_g, Ue = u_tuple
            K_sh = len(chain)
            yu_s = []
            yd_s = []
            ye_s = []
            ua_p = mp.eye(3)
            pu = mp.mpc(1)
            pd = mp.mpc(1)
            pe = mp.mpc(1)
            for n in range(K_sh):
                yu_r = yk_gold[(chain[n], 1, -4)]
                yd_r = yk_gold[(chain[n], 1, 2)]
                ye_r = yk_gold[(chain[n], -3, 6)]
                yu_s.append(UQ * (pu * (ua_p * yu_r * ua_p.T)) * Uu.H)
                yd_s.append(UQ * (pd * (ua_p * yd_r * ua_p.T)) * Ud.H)
                ye_s.append(UL_g * (pe * (ua_p * ye_r * ua_p.T)) * Ue.H)
                pu *= step_ph_map[(chain[n], 1, -4)]
                pd *= step_ph_map[(chain[n], 1, 2)]
                pe *= step_ph_map[(chain[n], -3, 6)]
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

        def run_staggered_7(chain, u_tuple):
            UQ, Uu, Ud, UL_g, Ue = u_tuple
            res_sec = []
            for (ql, qr), Ul, Ur in [((1, -4), UQ, Uu), ((1, 2), UQ, Ud), ((-3, 6), UL_g, Ue)]:
                ys = []
                ua_p = mp.eye(3)
                ph = mp.mpc(1)
                for n in range(7):
                    ym = yk_gold[(chain[n], ql, qr)]
                    ys.append(Ul * (ph * (ua_p * ym * ua_p.T)) * Ur.H)
                    ph *= step_ph_map[(chain[n], ql, qr)]
                    ua_p = U_A * ua_p
                prod7 = ys[0] * ys[1].H * ys[2] * ys[3].H * ys[4] * ys[5].H * ys[6]
                sv, uv = eig_herm_asc(prod7 * prod7.H)
                res_sec.append(([mp.sqrt(x) for x in sv], uv))
            (su7, uu7), (sd7, ud7), (se7, _) = res_sec
            vc7 = uu7.H * ud7
            j7 = abs(mp.im(vc7[0, 0] * vc7[1, 1] * mp.conj(vc7[0, 1]) * mp.conj(vc7[1, 0])))
            md7 = min(abs(vc7[0, 0]), abs(vc7[1, 1]), abs(vc7[2, 2]))
            return [su7[1] / su7[2], su7[0] / su7[2], sd7[1] / sd7[2], sd7[0] / sd7[2], se7[1] / se7[2], se7[0] / se7[2], abs(vc7[0, 1]), abs(vc7[1, 2]), abs(vc7[0, 2]), j7], md7

        I3 = mp.eye(3)
        all_16_gram = []
        gram_by_start = {}
        for kind_lbl, lst in [("bond6", bond_chains_8), ("vert7", vertex_chains_8)]:
            for idx, hi, l3, l5, ch in lst:
                obs, md, yus = run_waveguide_gramian(ch, (I3, I3, I3, I3, I3))
                gram_by_start[ch[0]] = (obs, md, yus)
                all_16_gram.append({
                    "kind": kind_lbl,
                    "orbit": idx,
                    "half": hi,
                    "leg3_leg5": [l3, l5],
                    "start_30": [int(ch[0][0] * 30), int(ch[0][1] * 30)],
                    "up_ratios": [mp.nstr(obs[0], 8), mp.nstr(obs[1], 8)],
                    "down_ratios": [mp.nstr(obs[2], 8), mp.nstr(obs[3], 8)],
                    "lep_ratios": [mp.nstr(obs[4], 8), mp.nstr(obs[5], 8)],
                    "ckm_moduli_and_min_diag": [mp.nstr(obs[8], 8), mp.nstr(obs[9], 8), mp.nstr(obs[10], 8), mp.nstr(md, 8)],
                    "jarlskog_abs": mp.nstr(obs[11], 8),
                })

        # Verify -I_2 pairs all 16 chains 2-to-1 to < 10^-45!
        max_negI_pair_diff = mp.mpf(0)
        for st, (obs_a, md_a, _) in gram_by_start.items():
            neg_st = ((-st[0]) % 1, (-st[1]) % 1)
            assert neg_st in gram_by_start and neg_st != st
            obs_b, md_b, _ = gram_by_start[neg_st]
            df_p = max(max(abs(obs_a[k] - obs_b[k]) for k in range(12)), abs(md_a - md_b))
            max_negI_pair_diff = max(max_negI_pair_diff, df_p)
        assert max_negI_pair_diff < mp.mpf(10) ** (-45)

        count_m13_lt_4e4 = sum(1 for _, (o, _, _) in gram_by_start.items() if max(o[1], o[3], o[5]) < mp.mpf(4) / mp.mpf(10000))
        count_m13_lt_1e4 = sum(1 for _, (o, _, _) in gram_by_start.items() if max(o[1], o[3], o[5]) < mp.mpf(1) / mp.mpf(10000))
        count_m23_lt_1_over_5 = sum(1 for _, (o, _, _) in gram_by_start.items() if max(o[0], o[2], o[4]) < mp.mpf(1) / mp.mpf(5))
        count_md_gt_3_over_4 = sum(1 for _, (_, m, _) in gram_by_start.items() if m > mp.mpf(3) / mp.mpf(4))
        count_md_gt_9_over_10 = sum(1 for _, (_, m, _) in gram_by_start.items() if m > mp.mpf(9) / mp.mpf(10))
        count_j_gt_1e5 = sum(1 for _, (o, _, _) in gram_by_start.items() if o[11] > mp.mpf(10) ** (-5))
        count_ckm_ordered = sum(1 for _, (o, _, _) in gram_by_start.items() if o[8] > o[9] > o[10])
        assert count_m13_lt_4e4 == 16 and count_m13_lt_1e4 == 14 and count_m23_lt_1_over_5 == 16
        assert count_md_gt_3_over_4 == 16 and count_md_gt_9_over_10 == 8 and count_j_gt_1e5 == 16 and count_ckm_ordered == 8

        # Check Bond (+1, +1) Half 0 (Orbit 0 H0, starting at (11/30, 22/30)):
        b0_ch = bond_chains_8[0][4]
        obs_b0, md_b0, yu_b0_list = gram_by_start[b0_ch[0]]
        assert max(obs_b0[1], obs_b0[3], obs_b0[5]) < mp.mpf(4) / mp.mpf(100000)
        assert max(obs_b0[0], obs_b0[2], obs_b0[4]) < mp.mpf(1) / mp.mpf(20)
        assert obs_b0[8] > obs_b0[9] > obs_b0[10]
        assert md_b0 > mp.mpf(9) / mp.mpf(10) and obs_b0[11] > mp.mpf(2) / mp.mpf(1000)

        # Evaluate Stag7 across ALL 8 true -R_sigma 7-sheet vertex-mirror chains:
        all_8_stag7 = []
        stag7_list = []
        for idx, hi, l3, l5, ch in vertex_chains_8:
            obs7, md7 = run_staggered_7(ch, (I3, I3, I3, I3, I3))
            stag7_list.append((obs7, md7, ch))
            all_8_stag7.append({
                "orbit": idx,
                "half": hi,
                "leg3_leg5": [l3, l5],
                "start_30": [int(ch[0][0] * 30), int(ch[0][1] * 30)],
                "up_ratios": [mp.nstr(obs7[0], 8), mp.nstr(obs7[1], 8)],
                "down_ratios": [mp.nstr(obs7[2], 8), mp.nstr(obs7[3], 8)],
                "lep_ratios": [mp.nstr(obs7[4], 8), mp.nstr(obs7[5], 8)],
                "ckm_moduli_and_min_diag": [mp.nstr(obs7[6], 8), mp.nstr(obs7[7], 8), mp.nstr(obs7[8], 8), mp.nstr(md7, 8)],
                "jarlskog_abs": mp.nstr(obs7[9], 8),
            })
        stag7_m13_lt_2e6 = sum(1 for o7, _, _ in stag7_list if max(o7[1], o7[3], o7[5]) < mp.mpf(2) / mp.mpf(1000000))
        stag7_j_gt_8e4 = sum(1 for o7, _, _ in stag7_list if o7[9] > mp.mpf(8) / mp.mpf(10000))
        stag7_md_gt_9_over_10 = sum(1 for _, m7, _ in stag7_list if m7 > mp.mpf(9) / mp.mpf(10))
        assert stag7_m13_lt_2e6 == 8 and stag7_j_gt_8e4 == 8 and stag7_md_gt_9_over_10 == 6

        obs_v1_h0, md_v1_h0, v1_ch = stag7_list[0]
        assert max(obs_v1_h0[1], obs_v1_h0[3], obs_v1_h0[5]) < mp.mpf(10) ** (-9)
        assert obs_v1_h0[6] > obs_v1_h0[7] > obs_v1_h0[8]
        assert md_v1_h0 > mp.mpf(98) / mp.mpf(100) and obs_v1_h0[9] > mp.mpf(8) / mp.mpf(10000)

        # Control 5 (Guardrail 3): 5 independent rational-Cayley U(3) transformations on true Bond Orbit 0 H0 & Vertex Orbit 1 H0!
        UQ_c = cayley_u3((5, -1, 2, 3, -4, 2, -1, 4, -3))
        Uu_c = cayley_u3((-2, 4, -3, 1, 5, -2, 4, -1, 3))
        Ud_c = cayley_u3((3, 4, -2, -3, 1, 5, 4, -2, 3))
        UL_c = cayley_u3((1, -5, 2, 4, -1, -3, -2, 3, 5))
        Ue_c = cayley_u3((-2, 3, -4, -2, 5, 1, 3, -4, -2))
        obs_b0_h, _, yu_b0_h = run_waveguide_gramian(b0_ch, (UQ_c, Uu_c, Ud_c, UL_c, Ue_c))
        obs_v1_h, _ = run_staggered_7(v1_ch, (UQ_c, Uu_c, Ud_c, UL_c, Ue_c))
        haar_err_b0 = max(abs(obs_b0[i] - obs_b0_h[i]) for i in range(12))
        haar_err_stag7 = max(abs(obs_v1_h0[i] - obs_v1_h[i]) for i in range(10))
        assert haar_err_b0 < mp.mpf(10) ** (-45) and haar_err_stag7 < mp.mpf(10) ** (-45)

        raw_id = yu_b0_list[5] * yu_b0_list[4] * yu_b0_list[3] * yu_b0_list[2] * yu_b0_list[1] * yu_b0_list[0]
        raw_h = yu_b0_h[5] * yu_b0_h[4] * yu_b0_h[3] * yu_b0_h[2] * yu_b0_h[1] * yu_b0_h[0]
        s_raw_id = [mp.sqrt(x) for x in eig_herm_asc(raw_id * raw_id.H)[0]]
        s_raw_h = [mp.sqrt(x) for x in eig_herm_asc(raw_h * raw_h.H)[0]]
        ctrl5_bad_prod_drift = max(abs(s_raw_id[1] / s_raw_id[2] - s_raw_h[1] / s_raw_h[2]), abs(s_raw_id[2] - s_raw_h[2]) / s_raw_id[2])
        assert ctrl5_bad_prod_drift > mp.mpf(1) / mp.mpf(100)

    out = {
        "card": "AGY-C56",
        "empirical_inputs": "0 of 19",
        "ast_firewall": ast_res,
        "E1_cube_group_and_p882": {
            "so3_z_order": len(so3_z),
            "so3_z_element_orders": order_hist,
            "primitive_order30_count": len(seen_576),
            "x30_cusp_count": len(seen_576) // 2,
            "A12_fixed_points_count": len(fixed_A12),
            "A12_fixed_cusps_count": len(fixed_A12) // 2,
            "generator_matrices_checked": gen_matrices_checked,
            "cusp_matrices_checked": cusp_matrices_checked,
            "max_generator_rel_err": mp.nstr(max_gen_err, 12),
            "max_p882_word_homomorphism_rel_err": mp.nstr(max_p882_err, 12),
            "max_unit_modulus_sc_deviation": mp.nstr(max_sc_mod_dev, 12),
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
            "max_quadratic_sum_3_over_5_rate_err": mp.nstr(max_quad_3_over_5_err, 12),
            "max_sv1_sq_1_over_5_rate_err": mp.nstr(max_sv1sq_1_over_5_err, 12),
            "min_channel_norm_sq_gap": mp.nstr(min_norm_sq_gap, 10),
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
            "negI_orbit_pair_character_bijection": {f"{k[0]}_{k[1]}": [v[0], v[1]] for k, v in sorted(pair_char_sigs.items())},
            "plus_R_sigma_bond_mirror_chains": len(bond_chains_8),
            "minus_R_sigma_vertex_mirror_chains": len(vertex_chains_8),
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
            "Lambda_geom_SL2Z_invariance_err": mp.nstr(lam_inv_err, 10),
            "max_raw_kahler_sigma_all96_p96": mp.nstr(max_raw_sigma_all96, 10),
            "max_step_phase_unit_modulus_dev_all96": mp.nstr(max_step_sc_dev, 12),
            "control_4_no_kahler_weight_drift": mp.nstr(raw_s_diff, 10),
            "control_6_jtheta2_branch_cut_jump_at_Re_11_over_7": mp.nstr(ctrl6_jtheta2_cut_jump, 10),
        },
        "E5_waveguide_full_16chain_menu_and_haar": {
            "additive_12turn_min_m2_over_m3_all8": mp.nstr(min_add_m23_all8, 10),
            "additive_12turn_max_jarlskog_abs_all8": mp.nstr(max_add_jarlskog_all8, 10),
            "barrier_sign_up_m2_over_m3": mp.nstr(bar_m23, 10),
            "negI_16_to_8_pair_isospectral_max_diff": mp.nstr(max_negI_pair_diff, 12),
            "gramian_16chain_pass_counts": {
                "m1_over_m3_lt_4e_minus_4": count_m13_lt_4e4,
                "m1_over_m3_lt_1e_minus_4": count_m13_lt_1e4,
                "m2_over_m3_lt_1_over_5": count_m23_lt_1_over_5,
                "min_diag_gt_3_over_4": count_md_gt_3_over_4,
                "min_diag_gt_9_over_10": count_md_gt_9_over_10,
                "jarlskog_gt_1e_minus_5": count_j_gt_1e5,
                "standard_ckm_ordering": count_ckm_ordered,
            },
            "stag7_8chain_pass_counts": {
                "m1_over_m3_lt_2e_minus_6": stag7_m13_lt_2e6,
                "jarlskog_gt_8e_minus_4": stag7_j_gt_8e4,
                "min_diag_gt_9_over_10": stag7_md_gt_9_over_10,
            },
            "bond6_orbit0_half0_gramian": all_16_gram[0],
            "vert7_orbit1_half0_stag7": all_8_stag7[0],
            "all_16_gramian_chains": all_16_gram,
            "all_8_stag7_vertex_chains": all_8_stag7,
            "control_5_cayley_u3_5_max_err_bond6": mp.nstr(haar_err_b0, 10),
            "control_5_cayley_u3_5_max_err_stag7": mp.nstr(haar_err_stag7, 10),
            "control_5_planted_noncovariant_product_drift": mp.nstr(ctrl5_bad_prod_drift, 10),
        },
        "all_controls_passed": bool(
            max_gen_err < mp.mpf(10) ** (-50)
            and max_p882_err < mp.mpf(10) ** (-50)
            and max_sc_mod_dev < mp.mpf(10) ** (-50)
            and ctrl1_noshift_err > mp.mpf(1) / mp.mpf(100)
            and ctrl1_inv_sv_err > mp.mpf(1) / mp.mpf(100)
            and max_quad_3_over_5_err < mp.mpf(10) ** (-20)
            and max_sv1sq_1_over_5_err < mp.mpf(10) ** (-10)
            and min_norm_sq_gap > mp.mpf(1)
            and max_25_err < mp.mpf(10) ** (-9)
            and ctrl2_min_dev > mp.mpf(1) / mp.mpf(2)
            and chi15_invariant_ok
            and ctrl3_bad_q3_flips == 96
            and lam_inv_err < mp.mpf(10) ** (-35)
            and raw_s_diff > mp.mpf(1) / mp.mpf(10)
            and bar_m23 > mp.mpf(2) / mp.mpf(3)
            and ctrl6_jtheta2_cut_jump > mp.mpf(9)
            and haar_err_b0 < mp.mpf(10) ** (-45)
            and haar_err_stag7 < mp.mpf(10) ** (-45)
            and ctrl5_bad_prod_drift > mp.mpf(1) / mp.mpf(100)
        ),
    }
    payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
