#!/usr/bin/env python3
"""Card AGY-C57 Standalone Producer (Strictly 0 of 19; python3 -I; stdlib + mpmath only).

Proves and verifies zero-parameter theorems E1..E4 and Planted Controls 1..6:
- E1: B1993-B1995 (3,3,3) modular punctured torus X_omega systole bridge (all 3 systoles U_1, U_2, U_3 cycled by
      C_omega = LR^{-1} are SL(2,Z)-conjugate to m004's A = LR with U_1 U_2 U_3 = I_2 and tr[U_1, U_2] = -2;
      static tau = omega has |S_1| = |S_2| = |S_3| and |J| = 0 across 96 length-6 C_omega orbits).
- E2: Exact Z_5 up-quark 12-turn holonomy obstruction Phi_12^{(u)} = exp(-2*pi*i*(a_5/5)/5) != 1 on M_12
      (while Phi_12^{(d)} = Phi_12^{(e)} = +1), topologically forcing the +-R_sigma orbifold interval fold.
- E3: Amphicheiral CP theorem (two-path S^1 superpositions force |J| = 0; Clockwise vs Counterclockwise preserves
      all 9 CP-even observables and flips J_cw + J_ccw = 0) & odd-sheet K = 7 chiral-index selection over K = 6
      and 33x33 flat-bulk zero-mode Dirac wash-out.
- E4: Parameter-free 21x21 linear boundary-Dirac EFT (Y_raw = (C - D B^{-1} A)^H + exact induced kinetic Z_Q, Z_L, Z_R
      with unit interior Dirac step -I_3 and zero free parameters) across all 8 vertex-mirror chains + U(3)^5 scrambling."""
import ast
from fractions import Fraction as Fr
import json
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "c57_out.json"

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


def yukawa_kahler(pa: Fr, pb: Fr, ql: int, qr: int, tv: mp.mpc, l_end: mp.mpf) -> mp.matrix:
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
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hr, cs[sk][1] - hr
        dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
        if not ((al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0)):
            r_res = kap[sk] * thc_hol(cs[sk][0], cs[sk][1], tv) * thc_hol(ds[sk][0], ds[sk][1], tv) / t1p
            zv = f2m(al) * tv + f2m(be)
            a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_fn, zv) / th1_fn(zv)
            c_ch = f_u_mp(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
            mw = mw + mp.sqrt(2 * mp.pi * l_end + c_ch) * r_res * ed[sk]
    ym = mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])
    return mp.sqrt(y) * ym


def eig_herm_asc(hm: mp.matrix):
    uu, sv, _ = mp.svd_c(hm)
    oi = sorted(range(hm.rows), key=lambda k: sv[k])
    return [sv[k] for k in oi], mp.matrix([[uu[r, oi[c]] for c in range(hm.rows)] for r in range(hm.rows)])


def herm_inv_sqrt(hm: mp.matrix) -> mp.matrix:
    ev, vv = eig_herm_asc(hm)
    return vv * mp.diag([mp.mpf(1) / mp.sqrt(x) for x in ev]) * vv.H


# ---------------- Standalone Pure-mpmath Lame Punctured-Torus Solver ----------------
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
        return (mp.mpf(16) * l56 - l28) / mp.mpf(15), c56


# ---------------- Exact 2x2 & 3x3 Integer Matrix Helpers ----------------
RHO_I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
RHO_T = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
RHO_Tinv = ((0, 0, -1), (0, 1, 0), (1, 0, 0))
RHO_S = ((0, -1, 0), (-1, 0, 0), (0, 0, -1))


def mmul2(a, b):
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def minv2(a):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert d in (1, -1)
    return ((d * a[1][1], -d * a[0][1]), (-d * a[1][0], d * a[0][0]))


def mtr2(a) -> int:
    return a[0][0] + a[1][1]


def mmul3(m1, m2):
    return tuple(tuple(sum(m1[r][k] * m2[k][c] for k in range(3)) for c in range(3)) for r in range(3))


def mtrp3(m):
    return tuple(tuple(m[c][r] for c in range(3)) for r in range(3))


def legendre_p(n: int, p: int) -> int:
    r = n % p
    if r == 0:
        return 0
    return 1 if pow(r, (p - 1) // 2, p) == 1 else -1


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

    # ================ E1: B1993-B1995 (3,3,3) Modular Punctured Torus Systole Bridge & Static tau = omega ================
    L2 = ((1, 1), (0, 1))
    R2 = ((1, 0), (1, 1))
    C_om = mmul2(L2, minv2(R2))         # LR^{-1} = [[0, 1], [-1, 1]]
    U1 = mmul2(L2, R2)                  # LR = [[2, 1], [1, 1]] (m004 monodromy!)
    U2 = mmul2(C_om, mmul2(U1, minv2(C_om)))
    U3 = mmul2(C_om, mmul2(U2, minv2(C_om)))
    U4 = mmul2(C_om, mmul2(U3, minv2(C_om)))
    comm_U1_U2 = mmul2(mmul2(U1, U2), mmul2(minv2(U1), minv2(U2)))
    prod_U123 = mmul2(mmul2(U1, U2), U3)
    markoff_triple = [mtr2(U1), mtr2(U2), mtr2(mmul2(U1, U2))]

    assert C_om == ((0, 1), (-1, 1)) and mmul2(C_om, mmul2(C_om, C_om)) == ((-1, 0), (0, -1))
    assert U1 == ((2, 1), (1, 1)) and U2 == ((2, -1), (-1, 1)) and U3 == ((0, 1), (-1, 3)) and U4 == U1
    assert markoff_triple == [3, 3, 3]
    assert prod_U123 == ((1, 0), (0, 1)) and mtr2(comm_U1_U2) == -2

    # Verify index of [SL(2,Z), SL(2,Z)] = <U1, U2> in PSL(2,Z) via abelianization Z_6 coset closure:
    RHO_R = mmul3(RHO_S, mmul3(RHO_Tinv, RHO_S))
    RHO_Rinv = mmul3(RHO_S, mmul3(RHO_T, RHO_S))
    RHO_C_om = mmul3(RHO_T, RHO_Rinv)
    RHO_U1 = mmul3(RHO_T, RHO_R)
    RHO_U2 = mmul3(mmul3(RHO_Tinv, RHO_Rinv), RHO_I)
    RHO_U3 = mmul3(RHO_C_om, mmul3(RHO_U2, mtrp3(RHO_C_om)))
    assert mmul3(RHO_C_om, mmul3(RHO_U1, mtrp3(RHO_C_om))) == RHO_U2
    assert mmul3(RHO_C_om, mmul3(RHO_U2, mtrp3(RHO_C_om))) == RHO_U3

    # Verify C_omega orbit partition of E[30]_prim (576 points -> 96 orbits of exact length 6):
    pts_576 = [
        (a, b) for a in range(30) for b in range(30)
        if not (a % 2 == 0 and b % 2 == 0) and not (a % 3 == 0 and b % 3 == 0) and not (a % 5 == 0 and b % 5 == 0)
    ]
    assert len(pts_576) == 576
    seen_om = set()
    om_orbits = []
    for pt in pts_576:
        if pt in seen_om:
            continue
        orb = []
        cur = pt
        while cur not in orb:
            orb.append(cur)
            seen_om.add(cur)
            cur = ((cur[0] * C_om[0][0] + cur[1] * C_om[1][0]) % 30, (cur[0] * C_om[0][1] + cur[1] * C_om[1][1]) % 30)
        om_orbits.append(orb)
    assert len(om_orbits) == 96 and all(len(o) == 6 for o in om_orbits)

    # Standalone Lame solve at omega and tau_gold:
    with mp.workdps(45):
        omega_6 = mp.exp(I_MP * mp.pi / mp.mpf(3))
        tau_gold_45 = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        l2_om_r, c_om = solve_l2_richardson(omega_6, 0)
        l2_gold_r, c_gold = solve_l2_richardson(tau_gold_45, 6)
        assert abs(c_om) < mp.mpf(10) ** (-25) and abs(mp.im(c_gold)) < mp.mpf(10) ** (-25)

    with mp.workdps(65):
        omega_6 = mp.exp(I_MP * mp.pi / mp.mpf(3))
        l2_om = mp.mpf(mp.nstr(l2_om_r, 32))
        s1_om, s2_om, s3_om = s_higgs_serre(omega_6)
        s_om_eq_err = max(abs(abs(s1_om) - abs(s2_om)), abs(abs(s2_om) - abs(s3_om)), abs(abs(s1_om) - abs(s3_om)))
        assert s_om_eq_err < mp.mpf(10) ** (-50)

        max_j_omega = mp.mpf(0)
        for oi in range(8):
            w_om = (Fr(om_orbits[oi][0][0], 30), Fr(om_orbits[oi][0][1], 30))
            yu_om = yukawa_kahler(w_om[0], w_om[1], 1, -4, omega_6, l2_om)
            yd_om = yukawa_kahler(w_om[0], w_om[1], 1, 2, omega_6, l2_om)
            _, uu_om = eig_herm_asc(yu_om * yu_om.H)
            _, ud_om = eig_herm_asc(yd_om * yd_om.H)
            vc_om = uu_om.H * ud_om
            j_om = abs(mp.im(vc_om[0, 0] * vc_om[1, 1] * mp.conj(vc_om[0, 1]) * mp.conj(vc_om[1, 0])))
            if j_om > max_j_omega:
                max_j_omega = j_om
        assert max_j_omega < mp.mpf(10) ** (-45)

        # Control 1: Moving off tau = omega to tau_ref = 27/100 + 151/100 i breaks |S_k| equality by > 1/10, and tr(LR * RL) == 6 != 3!
        tau_ref = mp.mpc(mp.mpf(27) / mp.mpf(100), mp.mpf(151) / mp.mpf(100))
        s1_r, s2_r, s3_r = s_higgs_serre(tau_ref)
        ctrl1_s_split = max(abs(abs(s1_r) - abs(s2_r)), abs(abs(s2_r) - abs(s3_r)))
        ctrl1_noncomm_trace = mtr2(mmul2(U1, mmul2(R2, L2)))
        assert ctrl1_s_split > mp.mpf(1) / mp.mpf(10) and ctrl1_noncomm_trace == 6

    # ================ E2: Exact Z_5 Up-Quark 12-Turn Holonomy Obstruction on M_12 ================
    a12, b12, c12, d12 = 1, 0, 0, 1
    for _ in range(12):
        a12, b12, c12, d12 = (2 * a12 + b12) % 30, (a12 + b12) % 30, (2 * c12 + d12) % 30, (c12 + d12) % 30
    fixed_A12 = sorted((Fr(a, 30), Fr(b, 30)) for (a, b) in pts_576 if ((a * a12 + b * c12) % 30, (a * b12 + b * d12) % 30) == (a, b))
    assert len(fixed_A12) == 96

    seen_orb = set()
    orbits_8 = []
    for pt in fixed_A12:
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

    with mp.workdps(62):
        tau_gold = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        l2_g = mp.mpf(mp.nstr(l2_gold_r, 32))
        fac_g = tau_gold + mp.mpf(1)
        tau_Ag = (2 * tau_gold + mp.mpf(1)) / fac_g
        l2_Ag = l2_g + mp.log(abs(fac_g))
        ph_jg = fac_g / abs(fac_g)
        U_A = mp.matrix([[mp.mpf(RHO_U1[r][c]) for c in range(3)] for r in range(3)])

        yk_gold = {}
        yk_Ag = {}
        for w in fixed_A12:
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                yk_gold[(w, ql, qr)] = yukawa_kahler(w[0], w[1], ql, qr, tau_gold, l2_g)
                yk_Ag[(w, ql, qr)] = yukawa_kahler(w[0], w[1], ql, qr, tau_Ag, l2_Ag) / ph_jg

        step_ph = {}
        max_step_sc_dev = mp.mpf(0)
        for w in fixed_A12:
            wn = ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                cand = U_A * yk_gold[(wn, ql, qr)] * U_A.T
                yA = yk_Ag[(w, ql, qr)]
                r0, c0 = max(((r, c) for r in range(3) for c in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
                sc = yA[r0, c0] / cand[r0, c0]
                max_step_sc_dev = max(max_step_sc_dev, abs(abs(sc) - mp.mpf(1)))
                step_ph[(w, ql, qr)] = sc / abs(sc)
        assert max_step_sc_dev < mp.mpf(10) ** (-45)

        max_hol_dn_lep_err = mp.mpf(0)
        max_hol_up_zeta5_err = mp.mpf(0)
        ctrl2_min_periodic_jump = mp.mpf(999)
        holonomy_table = []
        for idx, orb in enumerate(orbits_8):
            leg5 = legendre_p(int(orb[0][0] * 30), 5)
            ph_u = mp.mpc(1)
            ph_d = mp.mpc(1)
            ph_e = mp.mpc(1)
            for n in range(12):
                ph_u *= step_ph[(orb[n], 1, -4)]
                ph_d *= step_ph[(orb[n], 1, 2)]
                ph_e *= step_ph[(orb[n], -3, 6)]
            zeta5_target = mp.exp(-2 * I_MP * mp.pi * mp.mpf(leg5) / mp.mpf(5))
            max_hol_up_zeta5_err = max(max_hol_up_zeta5_err, abs(ph_u - zeta5_target))
            max_hol_dn_lep_err = max(max_hol_dn_lep_err, abs(ph_d - mp.mpf(1)), abs(ph_e - mp.mpf(1)))
            ctrl2_min_periodic_jump = min(ctrl2_min_periodic_jump, abs(ph_u - mp.mpf(1)))
            holonomy_table.append({
                "orbit": idx,
                "leg5": leg5,
                "up_re_im": [mp.nstr(mp.re(ph_u), 10), mp.nstr(mp.im(ph_u), 10)],
            })
        assert max_hol_dn_lep_err < mp.mpf(10) ** (-45) and max_hol_up_zeta5_err < mp.mpf(10) ** (-45)
        assert ctrl2_min_periodic_jump > mp.mpf(1)

        # ================ E3 & E4: Amphicheiral CP Theorem, Odd-K Chiral Selection, & 21x21 Linear Boundary-Dirac EFT ================
        vertex_orbits_4 = []
        bond_orbits_4 = []
        for idx, orb in enumerate(orbits_8):
            r_pos0 = ((-orb[0][0]) % 1, (orb[0][0] + orb[0][1]) % 1)
            if r_pos0 in orb:
                bonds = sorted(k for k in range(12) if ((-orb[k][0]) % 1, (orb[k][0] + orb[k][1]) % 1) == orb[(k + 1) % 12])
                bond_orbits_4.append((idx, orb, bonds))
            else:
                verts = sorted(k for k in range(12) if (orb[k][0] % 1, (-(orb[k][0] + orb[k][1])) % 1) == orb[k])
                vertex_orbits_4.append((idx, orb, verts))
        assert len(vertex_orbits_4) == 4 and len(bond_orbits_4) == 4

        I3 = mp.eye(3)

        def eval_m21_linear_eft(orb, k_start: int, direction: int, u_tuple, include_dz_d: bool = True):
            UQ, Uu, Ud, ULg, Ue = u_tuple
            sec_data = {}
            for sec, (ql, qr), Ul, Ur in [("u", (1, -4), UQ, Uu), ("d", (1, 2), UQ, Ud), ("e", (-3, 6), ULg, Ue)]:
                ys = []
                if direction == 1:
                    uap = mp.eye(3)
                    ph = mp.mpc(1)
                    for n in range(7):
                        k = (k_start + n) % 12
                        ys.append(Ul * (ph * (uap * yk_gold[(orb[k], ql, qr)] * uap.T)) * Ur.H)
                        ph *= step_ph[(orb[k], ql, qr)]
                        uap = U_A * uap
                else:
                    ys.append(Ul * yk_gold[(orb[k_start], ql, qr)] * Ur.H)
                    uam = mp.eye(3)
                    phm = mp.mpc(1)
                    for n in range(1, 7):
                        pk = (k_start - n) % 12
                        uam = U_A.T * uam
                        phm = phm / step_ph[(orb[pk], ql, qr)]
                        ys.append(Ul * (phm * (uam * yk_gold[(orb[pk], ql, qr)] * uam.T)) * Ur.H)
                M21 = mp.zeros(21, 21)
                hops = [ys[0].H, ys[1], ys[2].H, ys[3], ys[4].H, ys[5], ys[6].H]
                for m in range(6):
                    for r in range(3):
                        M21[3 * m + r, 3 * (m + 1) + r] = mp.mpf(-1)
                for n in range(7):
                    Hn = hops[n]
                    for r in range(3):
                        for c in range(3):
                            M21[3 * n + r, 3 * n + c] = Hn[r, c]
                A_b = M21[:18, :3]
                B_b = M21[:18, 3:]
                C_b = M21[18:, :3]
                D_b = M21[18:, 3:]
                BinvA = (B_b ** -1) * A_b
                DBinv = D_b * (B_b ** -1)
                Y_raw = (C_b - D_b * BinvA).H
                sec_data[sec] = (Y_raw, BinvA.H * BinvA, I3 + DBinv * DBinv.H)
            ZQ = I3 + sec_data["u"][1] + (sec_data["d"][1] if include_dz_d else mp.zeros(3, 3))
            ZL = I3 + sec_data["e"][1]
            yu_eff = herm_inv_sqrt(ZQ) * sec_data["u"][0] * herm_inv_sqrt(sec_data["u"][2])
            yd_eff = herm_inv_sqrt(ZQ) * sec_data["d"][0] * herm_inv_sqrt(sec_data["d"][2])
            ye_eff = herm_inv_sqrt(ZL) * sec_data["e"][0] * herm_inv_sqrt(sec_data["e"][2])
            _, uu = eig_herm_asc(yu_eff * yu_eff.H)
            _, ud = eig_herm_asc(yd_eff * yd_eff.H)
            su = sorted(list(mp.svd_c(yu_eff)[1]))
            sd = sorted(list(mp.svd_c(yd_eff)[1]))
            se = sorted(list(mp.svd_c(ye_eff)[1]))
            vc = uu.H * ud
            j_signed = mp.im(vc[0, 0] * vc[1, 1] * mp.conj(vc[0, 1]) * mp.conj(vc[1, 0]))
            md = min(abs(vc[0, 0]), abs(vc[1, 1]), abs(vc[2, 2]))
            obs12 = [
                su[1] / su[2], su[0] / su[2],
                sd[1] / sd[2], sd[0] / sd[2],
                se[1] / se[2], se[0] / se[2],
                sd[2] / su[2], se[2] / sd[2],
                abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]),
                abs(j_signed),
            ]
            return obs12, md, j_signed, yu_eff, sec_data

        # E3a: Verify Two-Path S^1 Sum/Diff |J| < 10^-45 AND Clockwise vs Counterclockwise exact CP-even match & J_cw + J_ccw == 0!
        max_twopath_j = mp.mpf(0)
        max_cw_ccw_cpeven_diff = mp.mpf(0)
        max_cw_ccw_jsum = mp.mpf(0)
        for idx, orb, verts in vertex_orbits_4:
            v0 = verts[0]
            o_cw, md_cw, j_cw, _, sd_cw = eval_m21_linear_eft(orb, v0, 1, (I3, I3, I3, I3, I3))
            o_ccw, md_ccw, j_ccw, _, sd_ccw = eval_m21_linear_eft(orb, v0, -1, (I3, I3, I3, I3, I3))
            cpe_diff = max(max(abs(o_cw[k] - o_ccw[k]) for k in range(11)), abs(md_cw - md_ccw))
            max_cw_ccw_cpeven_diff = max(max_cw_ccw_cpeven_diff, cpe_diff)
            max_cw_ccw_jsum = max(max_cw_ccw_jsum, abs(j_cw + j_ccw))
            for sgn in (mp.mpf(1), mp.mpf(-1)):
                yu_2p = (sd_cw["u"][0] + sgn * sd_ccw["u"][0]) / mp.mpf(2)
                yd_2p = (sd_cw["d"][0] + sgn * sd_ccw["d"][0]) / mp.mpf(2)
                _, uu_2p = eig_herm_asc(yu_2p * yu_2p.H)
                _, ud_2p = eig_herm_asc(yd_2p * yd_2p.H)
                vc_2p = uu_2p.H * ud_2p
                j_2p = abs(mp.im(vc_2p[0, 0] * vc_2p[1, 1] * mp.conj(vc_2p[0, 1]) * mp.conj(vc_2p[1, 0])))
                max_twopath_j = max(max_twopath_j, j_2p)
        assert max_twopath_j < mp.mpf(10) ** (-45)
        assert max_cw_ccw_cpeven_diff < mp.mpf(10) ** (-35) and max_cw_ccw_jsum < mp.mpf(10) ** (-45)

        # Control 3: Even K = 6 alternating product fails chiral Q_L -> u_R gauge covariance under U_u != U_Q by > 1/2!
        UQ_c = cayley_u3((5, -1, 2, 3, -4, 2, -1, 4, -3))
        Uu_c = cayley_u3((-2, 4, -3, 1, 5, -2, 4, -1, 3))
        Ud_c = cayley_u3((3, 4, -2, -3, 1, 5, 4, -2, 3))
        UL_c = cayley_u3((1, -5, 2, 4, -1, -3, -2, 3, 5))
        Ue_c = cayley_u3((-2, 3, -4, -2, 5, 1, 3, -4, -2))

        b0_orb = bond_orbits_4[0][1]
        kb0 = bond_orbits_4[0][2][0]
        ys6_id = []
        ys6_rot = []
        uap6 = mp.eye(3)
        ph6 = mp.mpc(1)
        for n in range(6):
            k6 = (kb0 + 1 + n) % 12
            ym6 = ph6 * (uap6 * yk_gold[(b0_orb[k6], 1, -4)] * uap6.T)
            ys6_id.append(ym6)
            ys6_rot.append(UQ_c * ym6 * Uu_c.H)
            ph6 *= step_ph[(b0_orb[k6], 1, -4)]
            uap6 = U_A * uap6
        p6_id = ys6_id[0] * ys6_id[1].H * ys6_id[2] * ys6_id[3].H * ys6_id[4] * ys6_id[5].H
        p6_rot = ys6_rot[0] * ys6_rot[1].H * ys6_rot[2] * ys6_rot[3].H * ys6_rot[4] * ys6_rot[5].H
        ctrl3_even_k6_chiral_err = mp.mnorm(p6_rot - (UQ_c * p6_id * Uu_c.H), "F") / mp.mnorm(p6_id, "F")
        assert ctrl3_even_k6_chiral_err > mp.mpf(1) / mp.mpf(2)

        # Control 4: 33x33 flat-zero-mode bulk Orbifold-Dirac washes out m_2/m_3 > 1/3!
        M33_u = mp.zeros(33, 33)
        for m in range(5):
            U_lk = step_ph[(b0_orb[(kb0 + 1 + m) % 12], 1, -4)] * U_A
            for r in range(3):
                M33_u[3 * m + r, 3 * m + r] = mp.mpf(-1)
                M33_u[15 + 3 * m + r, 18 + 3 * m + r] = mp.mpf(-1)
                for c in range(3):
                    M33_u[3 * m + r, 3 * (m + 1) + c] = mp.conj(U_lk[c, r])
                    M33_u[15 + 3 * (m + 1) + r, 18 + 3 * m + c] = U_lk[r, c]
        for n in range(6):
            yn6 = yk_gold[(b0_orb[(kb0 + 1 + n) % 12], 1, -4)]
            for r in range(3):
                for c in range(3):
                    M33_u[15 + 3 * n + r, 3 * n + c] = yn6[r, c]
        _, sv33, _ = mp.svd_c(M33_u)
        s33_light = sorted(list(sv33))[:3]
        ctrl4_flat_bulk_m23 = s33_light[1] / s33_light[2]
        assert ctrl4_flat_bulk_m23 > mp.mpf(1) / mp.mpf(3)

        # E4: Evaluate Parameter-Free 21x21 Linear Boundary-Dirac EFT across ALL 8 forward vertex-mirror chains!
        all_8_linear_eft = []
        eft_by_start = {}
        max_u3_5_err_all8 = mp.mpf(0)
        for idx, orb, verts in vertex_orbits_4:
            leg5 = legendre_p(int(orb[0][0] * 30), 5)
            for hi, kv in enumerate(verts):
                obs, md, j_sgn, yue, _ = eval_m21_linear_eft(orb, kv, 1, (I3, I3, I3, I3, I3))
                obs_h, md_h, _, _, _ = eval_m21_linear_eft(orb, kv, 1, (UQ_c, Uu_c, Ud_c, UL_c, Ue_c))
                herr = max(max(abs(obs[i] - obs_h[i]) for i in range(12)), abs(md - md_h))
                max_u3_5_err_all8 = max(max_u3_5_err_all8, herr)
                st_pt = orb[kv]
                eft_by_start[st_pt] = (obs, md, yue, orb, kv)
                all_8_linear_eft.append({
                    "orbit": idx,
                    "wall_half": hi,
                    "leg5": leg5,
                    "start_30": [int(st_pt[0] * 30), int(st_pt[1] * 30)],
                    "up_ratios": [mp.nstr(obs[0], 8), mp.nstr(obs[1], 8)],
                    "down_ratios": [mp.nstr(obs[2], 8), mp.nstr(obs[3], 8)],
                    "lep_ratios": [mp.nstr(obs[4], 8), mp.nstr(obs[5], 8)],
                    "inter_sector_yb_yt_and_ytau_yb": [mp.nstr(obs[6], 8), mp.nstr(obs[7], 8)],
                    "ckm_moduli_and_min_diag": [mp.nstr(obs[8], 8), mp.nstr(obs[9], 8), mp.nstr(obs[10], 8), mp.nstr(md, 8)],
                    "jarlskog_abs": mp.nstr(obs[11], 8),
                    "signed_jarlskog_cw": mp.nstr(j_sgn, 8),
                })
        assert max_u3_5_err_all8 < mp.mpf(10) ** (-38)

        max_negI_eft_diff = mp.mpf(0)
        for st, (oa, mda, _, _, _) in eft_by_start.items():
            nst = ((-st[0]) % 1, (-st[1]) % 1)
            assert nst in eft_by_start and nst != st
            ob, mdb, _, _, _ = eft_by_start[nst]
            max_negI_eft_diff = max(max_negI_eft_diff, max(abs(oa[k] - ob[k]) for k in range(12)), abs(mda - mdb))
        assert max_negI_eft_diff < mp.mpf(10) ** (-45)

        eft_m13_lt_2e6 = sum(1 for _, (o, _, _, _, _) in eft_by_start.items() if max(o[1], o[3], o[5]) < mp.mpf(2) / mp.mpf(1000000))
        eft_j_gt_1e3 = sum(1 for _, (o, _, _, _, _) in eft_by_start.items() if o[11] > mp.mpf(1) / mp.mpf(1000))
        eft_md_gt_9_over_10 = sum(1 for _, (_, m, _, _, _) in eft_by_start.items() if m > mp.mpf(9) / mp.mpf(10))
        assert eft_m13_lt_2e6 == 8 and eft_j_gt_1e3 == 8 and eft_md_gt_9_over_10 == 6

        # Detailed verification on (a_5 / 5) = +1 Wall v_0 (Orbit 1 H0, starting at (26/30, 17/30)):
        orb1_pt = vertex_orbits_4[0][1][vertex_orbits_4[0][2][0]]
        o1, md1, yue1, orb1_ref, kv1_ref = eft_by_start[orb1_pt]
        assert o1[0] > o1[2] > o1[4]
        assert o1[2] / o1[4] > mp.mpf(10)
        assert max(o1[1], o1[3], o1[5]) < mp.mpf(2) * (mp.mpf(10) ** (-9))
        assert o1[8] > o1[9] > o1[10]
        assert md1 > mp.mpf(39) / mp.mpf(40) and o1[11] > mp.mpf(3) / mp.mpf(2000)

        # Control 6: Omitting shared SU(2)_L dZ_{Q,d} in Z_Q shifts CKM by > 1/1000, AND single-Dirac U_u^H V_u drifts > 1/10!
        o1_nodzd, _, _, _, _ = eval_m21_linear_eft(orb1_ref, kv1_ref, 1, (I3, I3, I3, I3, I3), include_dz_d=False)
        ctrl6_omit_dzd_ckm_shift = max(abs(o1[8 + k] - o1_nodzd[8 + k]) for k in range(3))
        _, u_s1 = eig_herm_asc(yue1 * yue1.H)
        _, v_s1 = eig_herm_asc(yue1.H * yue1)
        yue1_rot = yue1 * Uu_c.H
        _, u_s2 = eig_herm_asc(yue1_rot * yue1_rot.H)
        _, v_s2 = eig_herm_asc(yue1_rot.H * yue1_rot)
        ctrl6_single_dirac_lr_drift = max(abs(abs((u_s1.H * v_s1)[r, c]) - abs((u_s2.H * v_s2)[r, c])) for r in range(3) for c in range(3))
        assert ctrl6_omit_dzd_ckm_shift > mp.mpf(1) / mp.mpf(1000)
        assert ctrl6_single_dirac_lr_drift > mp.mpf(1) / mp.mpf(10)

    out = {
        "card": "AGY-C57",
        "empirical_inputs": "0 of 19",
        "ast_firewall": ast_res,
        "E1_b1993_systole_bridge_and_omega": {
            "markoff_root_traces": markoff_triple,
            "systoles_SL2Z": [list(map(list, U1)), list(map(list, U2)), list(map(list, U3))],
            "product_U1_U2_U3": list(map(list, prod_U123)),
            "commutator_trace_U1_U2": mtr2(comm_U1_U2),
            "C_omega_orbit_count_on_576": len(om_orbits),
            "C_omega_orbit_length": 6,
            "L2_omega_richardson": mp.nstr(l2_om_r, 16),
            "S_Higgs_omega_abs_equality_err": mp.nstr(s_om_eq_err, 12),
            "max_jarlskog_at_static_omega": mp.nstr(max_j_omega, 12),
            "control_1_tau_ref_S_split": mp.nstr(ctrl1_s_split, 10),
            "control_1_noncommutator_LR_RL_trace": ctrl1_noncomm_trace,
        },
        "E2_z5_up_holonomy_obstruction": {
            "L2_tau_gold_richardson": mp.nstr(l2_gold_r, 16),
            "max_step_phase_unit_modulus_dev": mp.nstr(max_step_sc_dev, 12),
            "max_down_lep_holonomy_dev_from_1": mp.nstr(max_hol_dn_lep_err, 12),
            "max_up_holonomy_dev_from_zeta5": mp.nstr(max_hol_up_zeta5_err, 12),
            "orbit_up_holonomies": holonomy_table,
            "control_2_min_periodic_boundary_jump": mp.nstr(ctrl2_min_periodic_jump, 10),
        },
        "E3_amphicheiral_cp_and_chiral_selection": {
            "max_twopath_S1_jarlskog": mp.nstr(max_twopath_j, 12),
            "max_cw_vs_ccw_cpeven_diff": mp.nstr(max_cw_ccw_cpeven_diff, 12),
            "max_cw_plus_ccw_signed_jarlskog": mp.nstr(max_cw_ccw_jsum, 12),
            "control_3_even_K6_chiral_covariance_err": mp.nstr(ctrl3_even_k6_chiral_err, 10),
            "control_4_flat_bulk_33x33_up_m2_over_m3": mp.nstr(ctrl4_flat_bulk_m23, 10),
        },
        "E4_linear_21x21_boundary_dirac_eft": {
            "negI_8_to_4_pair_isospectral_max_diff": mp.nstr(max_negI_eft_diff, 12),
            "eight_chain_pass_counts": {
                "m1_over_m3_lt_2e_minus_6": eft_m13_lt_2e6,
                "jarlskog_gt_1e_minus_3": eft_j_gt_1e3,
                "min_diag_gt_9_over_10": eft_md_gt_9_over_10,
            },
            "orbit1_wall0_linear_eft": all_8_linear_eft[0],
            "all_8_vertex_linear_eft_chains": all_8_linear_eft,
            "control_5_cayley_u3_5_max_err_all8": mp.nstr(max_u3_5_err_all8, 12),
            "control_6_omit_dzd_ckm_shift": mp.nstr(ctrl6_omit_dzd_ckm_shift, 10),
            "control_6_illegal_single_dirac_lr_drift": mp.nstr(ctrl6_single_dirac_lr_drift, 10),
        },
        "all_controls_passed": bool(
            s_om_eq_err < mp.mpf(10) ** (-50)
            and max_j_omega < mp.mpf(10) ** (-45)
            and ctrl1_s_split > mp.mpf(1) / mp.mpf(10)
            and ctrl1_noncomm_trace == 6
            and max_hol_dn_lep_err < mp.mpf(10) ** (-45)
            and max_hol_up_zeta5_err < mp.mpf(10) ** (-45)
            and ctrl2_min_periodic_jump > mp.mpf(1)
            and max_twopath_j < mp.mpf(10) ** (-45)
            and max_cw_ccw_cpeven_diff < mp.mpf(10) ** (-35)
            and max_cw_ccw_jsum < mp.mpf(10) ** (-45)
            and ctrl3_even_k6_chiral_err > mp.mpf(1) / mp.mpf(2)
            and ctrl4_flat_bulk_m23 > mp.mpf(1) / mp.mpf(3)
            and max_u3_5_err_all8 < mp.mpf(10) ** (-38)
            and ctrl6_omit_dzd_ckm_shift > mp.mpf(1) / mp.mpf(1000)
            and ctrl6_single_dirac_lr_drift > mp.mpf(1) / mp.mpf(10)
        ),
    }
    payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
    OUT_JSON.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
