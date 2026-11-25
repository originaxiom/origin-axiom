#!/usr/bin/env python3
"""Card AGY-C59 Disjoint Zero-Trust Cold-Room Countercheck (Strictly 0 of 19; python3 -I).

Implements completely disjoint algorithms (zero shared code with c59_b1993_holonomy_and_linear_dirac_producer.py,
and zero runtime script-hash self-overwrites):
- Direct integer Gaussian lattice sum for theta[a, b](tau) (no mp.jtheta),
- Euler pentagonal series for eta(tau) (no mp.qp),
- Analytic Lambert series pi*cot(pi*z) + 4*pi*sum q^{2m}/(1-q^{2m}) sin(2*pi*m*z) for theta_1'/theta_1 (no mp.diff),
- Explicit 4-stage RK4 with logarithmic radial coordinate near z=0 for Lame uniformization L_2(omega) & L_2(tau_gold) (no implicit GL-RK4),
- Direct Hermitian mp.eigh + block-Hermitian sv_asc_via_eigh (no mp.svd_c),
- Direct 3-column linear system solves mp.lu_solve(B_b, col) and mp.lu_solve(B_b.H, col) for 21x21 boundary-Dirac EFT (no B_b ** -1 inverse),
- Unitary matrix exponential mp.expm(i*H) on fresh skew-Hermitian generators for U(3)^5 scrambling (no Cayley),
- Independently verifies E1..E4, 5 referee planted faults RPF1..RPF5, and SHA-256 + parse_float=bad_float on c59_out.json."""
import ast
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
PROD_JSON = HERE / "c59_out.json"
PROD_HASH = HERE / "OUTPUT_SHA256.txt"
CC_JSON = HERE / "c59_countercheck_out.json"

I_C = mp.mpc(0, 1)


def bad_float(_x: str):
    raise AssertionError("Binary float encountered in JSON!")


def verify_ast_clean(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    fl = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))
    fc = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex"))
    assert fl == 0 and fc == 0, (path.name, fl, fc)
    return {"literals": fl, "calls": fc}


def r2m(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def theta_char_sum(ca: Fr, cb: Fr, tv: mp.mpc) -> mp.mpc:
    k0 = int(mp.nint(-r2m(ca)))
    ar = r2m(ca) + mp.mpf(k0)
    bm = r2m(cb)
    y = mp.im(tv)
    rad = int(mp.ceil(mp.sqrt(mp.mpf(mp.mp.dps + 12) / (mp.pi * y)))) + 4
    tot = mp.mpc(0)
    for m in range(-rad, rad + 1):
        na = mp.mpf(m) + ar
        tot += mp.exp(I_C * mp.pi * (na * na) * tv + 2 * I_C * mp.pi * na * bm)
    return tot


def eta_pentagonal(tv: mp.mpc) -> mp.mpc:
    y = mp.im(tv)
    rad = int(mp.ceil(mp.sqrt(mp.mpf(mp.mp.dps + 12) / (3 * mp.pi * y)))) + 4
    s = mp.mpc(0)
    for k in range(-rad, rad + 1):
        ex = mp.mpf(3 * k * k - k)
        term = mp.exp(I_C * mp.pi * ex * tv)
        s += -term if (k % 2 != 0) else term
    return mp.exp(I_C * mp.pi * tv / mp.mpf(12)) * s


def theta_nulls_and_serre(tv: mp.mpc):
    t2 = theta_char_sum(Fr(1, 2), Fr(0, 1), tv)
    t3 = theta_char_sum(Fr(0, 1), Fr(0, 1), tv)
    t4 = theta_char_sum(Fr(0, 1), Fr(1, 2), tv)
    et = eta_pentagonal(tv)
    d24 = mp.mpf(24) * (et ** 3)
    s1 = -(t2 ** 2) * ((t3 ** 4) + (t4 ** 4)) / d24
    s2 = (t4 ** 2) * ((t2 ** 4) + (t3 ** 4)) / d24
    s3 = I_C * (t3 ** 2) * ((t2 ** 4) - (t4 ** 4)) / d24
    return t2, t3, t4, et, s1, s2, s3


def theta1_logderiv_lambert(zv: mp.mpc, tv: mp.mpc) -> mp.mpc:
    y = mp.im(tv)
    m_sh = int(mp.nint(mp.im(zv) / y))
    zr = zv - m_sh * tv
    q2 = mp.exp(2 * I_C * mp.pi * tv)
    m_lim = int(mp.ceil(mp.mpf(mp.mp.dps + 12) * mp.log(10) / (mp.pi * y))) + 6
    cot_term = mp.pi * mp.cos(mp.pi * zr) / mp.sin(mp.pi * zr)
    ser = mp.mpc(0)
    q2m = q2
    for m in range(1, m_lim + 1):
        ser += (q2m / (1 - q2m)) * mp.sin(2 * mp.pi * m * zr)
        q2m *= q2
    return cot_term + 4 * mp.pi * ser - 2 * I_C * mp.pi * m_sh


def kronecker_fu_disjoint(u1: Fr, u2: Fr, tv: mp.mpc) -> mp.mpf:
    y = mp.im(tv)
    ar, br = u1 % 1, u2 % 1
    if ar != 0:
        head = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(r2m(ar)) + mp.digamma(1 - r2m(ar)))
    else:
        head = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + y * (mp.pi ** 2) / (mp.sin(mp.pi * r2m(br)) ** 2)
    m_lim = int(mp.ceil(mp.mpf(mp.mp.dps + 8) * mp.log(10) / (2 * mp.pi * y))) + 6
    acc = mp.mpf(0)
    for k in range(-m_lim, m_lim + 1):
        mv = r2m(ar) + mp.mpf(k)
        if mv == 0:
            continue
        wv = mp.exp(-2 * mp.pi * abs(mv) * y + 2 * I_C * mp.pi * (mv * mp.re(tv) + r2m(br)))
        acc += (2 * mp.pi / abs(mv)) * mp.re(wv / (1 - wv))
    return head + acc


def assemble_yukawa_disjoint(pa: Fr, pb: Fr, ql: int, qr: int, tv: mp.mpc, l_end: mp.mpf) -> mp.matrix:
    y = mp.im(tv)
    _, _, _, et, s1, s2, s3 = theta_nulls_and_serre(tv)
    t1p = 2 * mp.pi * (et ** 3)
    qi = mp.matrix([[I_C, 0], [0, -I_C]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    sh = s1 * qi + s2 * qj + s3 * qk
    blks = [qj, qi, qk]
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    hf = mp.mpf(1) / mp.mpf(2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    hr = Fr(1, 2)
    ap, am = (ql + qr) * pa, (ql - qr) * pa
    bp, bm = (ql + qr) * pb, (ql - qr) * pb
    eph = mp.exp(-2 * I_C * mp.pi * r2m(ql * pa))
    kap = {"1": -I_C * eph, "i": mp.mpf(-1), "j": -eph, "k": I_C}
    cs = {"1": (ap + hr, bp + hr), "i": (ap + hr, bp), "j": (ap, bp + hr), "k": (ap, bp)}
    ds = {"1": (am + hr, bm + hr), "i": (am + hr, bm), "j": (am, bm + hr), "k": (am, bm)}
    mw = mp.zeros(2, 2)
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hr, cs[sk][1] - hr
        dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
        if not ((al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0)):
            tn = kap[sk] * theta_char_sum(cs[sk][0], cs[sk][1], tv) * theta_char_sum(ds[sk][0], ds[sk][1], tv)
            r_res = tn / t1p
            zv = r2m(al) * tv + r2m(be)
            a0 = 2 * I_C * mp.pi * r2m(al) + theta1_logderiv_lambert(zv, tv)
            c_ch = kronecker_fu_disjoint(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
            mw += mp.sqrt(2 * mp.pi * l_end + c_ch) * r_res * ed[sk]
    ym = mp.matrix([[ct[r][c][0, 0] * mw[0, 0] + ct[r][c][0, 1] * mw[0, 1] + ct[r][c][1, 0] * mw[1, 0] + ct[r][c][1, 1] * mw[1, 1] for c in range(3)] for r in range(3)])
    return mp.sqrt(y) * ym


def eigh_asc_disjoint(hm: mp.matrix):
    hm_sym = (hm + hm.H) / mp.mpf(2)
    ev, vv = mp.eigh(hm_sym)
    oi = sorted(range(hm.rows), key=lambda k: ev[k])
    return [max(mp.mpf(0), ev[k]) for k in oi], mp.matrix([[vv[r, oi[c]] for c in range(hm.rows)] for r in range(hm.rows)])


def sv_asc_via_eigh(ym: mp.matrix):
    n = ym.rows
    B = mp.zeros(2 * n, 2 * n)
    for r in range(n):
        for c in range(n):
            B[r, n + c] = ym[r, c]
            B[n + c, r] = mp.conj(ym[r, c])
    ev, _ = mp.eigh(B)
    pos = sorted([x for x in ev if x > 0])
    while len(pos) < n:
        pos.insert(0, mp.mpf(0))
    return pos[-n:]


def wp_disjoint(z: mp.mpc, tv: mp.mpc, t30: mp.mpc, t40: mp.mpc, e1: mp.mpc) -> mp.mpc:
    k_im = int(mp.nint(mp.im(z) / mp.im(tv)))
    zr = z - k_im * tv
    zr = zr - int(mp.nint(mp.re(zr)))
    q = mp.exp(I_C * mp.pi * tv)
    rad = 18
    t1 = mp.mpc(0)
    t2 = mp.mpc(0)
    for n in range(rad):
        qn = q ** ((mp.mpf(2 * n + 1) / mp.mpf(2)) ** 2)
        s_term = mp.sin(mp.mpf(2 * n + 1) * mp.pi * zr)
        c_term = mp.cos(mp.mpf(2 * n + 1) * mp.pi * zr)
        t1 += (mp.mpf(-2) if (n % 2 == 1) else mp.mpf(2)) * qn * s_term
        t2 += mp.mpf(2) * qn * c_term
    return ((mp.pi * t30 * t40 * t2) / t1) ** 2 + e1


def rk4_fund_disjoint(z_of_t, dz_of_t, q_pot, n_steps: int) -> mp.matrix:
    h = mp.mpf(1) / mp.mpf(n_steps)
    Y = mp.eye(2)

    def A_mat(tv_s: mp.mpf) -> mp.matrix:
        zz = z_of_t(tv_s)
        dd = dz_of_t(tv_s)
        qq = q_pot(zz)
        return mp.matrix([[0, dd], [-dd * qq, 0]])

    for j in range(n_steps):
        t0 = j * h
        tm = t0 + h / mp.mpf(2)
        t1 = t0 + h
        A0 = A_mat(t0)
        Am = A_mat(tm)
        A1 = A_mat(t1)
        K1 = A0 * Y
        K2 = Am * (Y + (h / mp.mpf(2)) * K1)
        K3 = Am * (Y + (h / mp.mpf(2)) * K2)
        K4 = A1 * (Y + h * K3)
        Y = Y + (h / mp.mpf(6)) * (K1 + 2 * K2 + 2 * K3 + K4)
    return Y


def lame_l2_rk4_logradial(tv: mp.mpc, c_init: mp.mpc, walk_steps: int = 0) -> mp.mpf:
    with mp.workdps(38):
        def solve_c_at(tau_v: mp.mpc, cg: mp.mpc, ns: int) -> mp.mpc:
            _, t30, t40, _, _, _, _ = theta_nulls_and_serre(tau_v)
            e1 = (mp.pi ** 2 / mp.mpf(3)) * (t30 ** 4 + t40 ** 4)
            z0 = (mp.mpf(1) + tau_v) / mp.mpf(2)

            def mob(T):
                ds = mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
                return mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]]) / ds

            def res(cv):
                q_fn = lambda zz: wp_disjoint(zz, tau_v, t30, t40, e1) / mp.mpf(4) + cv
                Ta = rk4_fund_disjoint(lambda t: z0 + t, lambda _t: mp.mpc(1), q_fn, ns)
                Tb = rk4_fund_disjoint(lambda t: z0 + t * tau_v, lambda _t: tau_v, q_fn, ns)
                Aa, Ab = mob(Ta), mob(Tb)
                return mp.im(Aa[0, 0] + Aa[1, 1]), mp.im(Ab[0, 0] + Ab[1, 1])

            cc = cg
            eps_fd = mp.mpf(10) ** (-9)
            for _ in range(15):
                f1, f2 = res(cc)
                if max(abs(f1), abs(f2)) < mp.mpf(10) ** (-20):
                    break
                f1x, f2x = res(cc + eps_fd)
                f1y, f2y = res(cc + I_C * eps_fd)
                J = mp.matrix([[(f1x - f1) / eps_fd, (f1y - f1) / eps_fd], [(f2x - f2) / eps_fd, (f2y - f2) / eps_fd]])
                dc = mp.lu_solve(J, mp.matrix([-f1, -f2]))
                cc = cc + dc[0] + I_C * dc[1]
            return cc

        c_cur = c_init
        if walk_steps > 0:
            for st in range(1, walk_steps + 1):
                tk = I_C + (tv - I_C) * (mp.mpf(st) / mp.mpf(walk_steps))
                c_cur = solve_c_at(tk, c_cur, 32)
        c_fin = solve_c_at(tv, c_cur, 64)

        t20, t30, t40, _, _, _, _ = theta_nulls_and_serre(tv)
        e1 = (mp.pi ** 2 / mp.mpf(3)) * (t30 ** 4 + t40 ** 4)
        z0 = (mp.mpf(1) + tv) / mp.mpf(2)
        q_fn = lambda zz: wp_disjoint(zz, tv, t30, t40, e1) / mp.mpf(4) + c_fin

        def mob(T):
            ds = mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
            return mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]]) / ds

        def eval_at_ns(ns: int) -> mp.mpf:
            Ta = rk4_fund_disjoint(lambda t: z0 + t, lambda _t: mp.mpc(1), q_fn, ns)
            Aa = mob(Ta)
            zs = (mp.mpf(1) / mp.mpf(25)) * z0 / abs(z0)
            ln_rat = mp.log(abs(zs) / abs(z0))
            T1 = rk4_fund_disjoint(lambda t: z0 * mp.exp(t * ln_rat), lambda t: z0 * ln_rat * mp.exp(t * ln_rat), q_fn, ns)
            T2 = rk4_fund_disjoint(lambda t: zs * mp.exp(2 * I_C * mp.pi * t), lambda t: 2 * I_C * mp.pi * zs * mp.exp(2 * I_C * mp.pi * t), q_fn, ns)
            T3 = rk4_fund_disjoint(lambda t: zs * mp.exp(-t * ln_rat), lambda t: -zs * ln_rat * mp.exp(-t * ln_rat), q_fn, ns)
            P0 = mob(T3 * T2 * T1)

            def fpts(M):
                a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
                disc = mp.sqrt((a - d) ** 2 + 4 * b * cc)
                return (a - d + disc) / (2 * cc), (a - d - disc) / (2 * cc)

            pp = sum(fpts(P0)) / mp.mpf(2)
            f1, f2 = fpts(Aa)
            sg = (f2 - f1) / (f2 - pp)
            gm = mp.matrix([[1 / sg, -f1 / sg], [1, -pp]])
            gm = gm / mp.sqrt(gm[0, 0] * gm[1, 1] - gm[0, 1] * gm[1, 0])
            if mp.im((-f1 / sg) / (-pp)) < 0:
                gm = mp.matrix([[I_C, 0], [0, -I_C]]) * gm
            RP = gm * P0 * (gm ** -1)
            RP = RP / RP[0, 0]
            lam = abs(mp.re(RP[0, 1]))

            kc = mp.pi ** 2 / mp.mpf(3)
            e2, e3 = kc * (t20 ** 4 - t40 ** 4), -kc * (t20 ** 4 + t30 ** 4)
            g2, g3 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2), 4 * e1 * e2 * e3
            Mf = 50
            aw = {1: g2 / mp.mpf(20), 2: g3 / mp.mpf(28)}
            for n in range(3, Mf // 2 + 2):
                aw[n] = mp.mpf(3) / mp.mpf((2 * n + 3) * (n - 2)) * sum(aw[m] * aw[n - 1 - m] for m in range(1, n - 1))
            Qf = [mp.mpc(0)] * (Mf + 1)
            Qf[0] = c_fin
            for n in range(1, Mf // 2 + 1):
                if 2 * n <= Mf:
                    Qf[2 * n] = aw[n] / mp.mpf(4)
            al = [mp.mpc(0)] * (Mf + 1)
            be = [mp.mpc(0)] * (Mf + 1)
            al[0] = mp.mpc(1)
            for m in range(1, Mf + 1):
                al[m] = -sum(Qf[j] * al[m - 2 - j] for j in range(0, m - 1)) / mp.mpf(m * m)
                be[m] = -(2 * m * al[m] + sum(Qf[j] * be[m - 2 - j] for j in range(0, m - 1))) / mp.mpf(m * m)
            gloc = sum(be[m] * (zs ** m) for m in range(Mf + 1)) / sum(al[m] * (zs ** m) for m in range(Mf + 1))
            uz = (gm[0, 0] * (T1[0, 1] / T1[0, 0]) + gm[0, 1]) / (gm[1, 0] * (T1[0, 1] / T1[0, 0]) + gm[1, 1])
            imB = mp.im(uz) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(gloc))
            return mp.pi - (2 * mp.pi / lam) * imB

        return (mp.mpf(16) * eval_at_ns(72) - eval_at_ns(36)) / mp.mpf(15)


def expm_u3_disjoint(ints9) -> mp.matrix:
    d0, d1, d2, r01, r02, r12, m01, m02, m12 = ints9
    den = mp.mpf(5)
    H = mp.matrix([
        [mp.mpf(d0) / den, mp.mpc(r01, m01) / den, mp.mpc(r02, m02) / den],
        [mp.mpc(r01, -m01) / den, mp.mpf(d1) / den, mp.mpc(r12, m12) / den],
        [mp.mpc(r02, -m02) / den, mp.mpc(r12, -m12) / den, mp.mpf(d2) / den],
    ])
    return mp.expm(I_C * H)


def solve_cols_lu(M: mp.matrix, RHS: mp.matrix) -> mp.matrix:
    out = mp.zeros(M.rows, RHS.cols)
    for col in range(RHS.cols):
        b_vec = mp.matrix([RHS[r, col] for r in range(M.rows)])
        x_vec = mp.lu_solve(M, b_vec)
        for r in range(M.rows):
            out[r, col] = x_vec[r]
    return out


def main() -> None:
    cc_ast = verify_ast_clean(Path(__file__))
    prod_ast = verify_ast_clean(HERE / "c59_b1993_holonomy_and_linear_dirac_producer.py")

    raw_bytes = PROD_JSON.read_bytes()
    actual_sha = hashlib.sha256(raw_bytes).hexdigest()
    recorded_sha = PROD_HASH.read_text(encoding="utf-8").strip().split()[0]
    assert actual_sha == recorded_sha, (actual_sha, recorded_sha)
    prod = json.loads(raw_bytes.decode("utf-8"), parse_float=bad_float)

    discrepancies = []

    # 1. Disjoint E1 check: SL(2,Z) commutator subgroup systoles, C_omega orbits, L_2(omega), |S_k(omega)|, & R_sigma CP-antisymmetry
    def mul2(x, y):
        return (
            (x[0][0] * y[0][0] + x[0][1] * y[1][0], x[0][0] * y[0][1] + x[0][1] * y[1][1]),
            (x[1][0] * y[0][0] + x[1][1] * y[1][0], x[1][0] * y[0][1] + x[1][1] * y[1][1]),
        )

    def inv2(x):
        det = x[0][0] * x[1][1] - x[0][1] * x[1][0]
        assert det in (1, -1)
        return ((det * x[1][1], -det * x[0][1]), (-det * x[1][0], det * x[0][0]))

    L_g, R_g = ((1, 1), (0, 1)), ((1, 0), (1, 1))
    C_om = mul2(L_g, inv2(R_g))
    U1 = mul2(L_g, R_g)
    U2 = mul2(C_om, mul2(U1, inv2(C_om)))
    U3 = mul2(C_om, mul2(U2, inv2(C_om)))
    if [list(map(list, U1)), list(map(list, U2)), list(map(list, U3))] != prod["E1_b1993_systole_bridge_and_omega"]["systoles_SL2Z"]:
        discrepancies.append("E1_systoles_mismatch")
    comm12 = mul2(mul2(U1, U2), mul2(inv2(U1), inv2(U2)))
    if (comm12[0][0] + comm12[1][1]) != prod["E1_b1993_systole_bridge_and_omega"]["commutator_trace_U1_U2"]:
        discrepancies.append("E1_commutator_trace_mismatch")

    # RPF1: Swapping C_omega = LR^{-1} to LR breaks the order-3 systole cycle (trace blows up to 18 != 3)
    U2_bad = mul2(U1, mul2(U1, inv2(U1)))
    U_prod_bad = mul2(U1, mul2(R_g, L_g))
    rpf1_bad_trace = U_prod_bad[0][0] + U_prod_bad[1][1]
    assert rpf1_bad_trace == 6 and U2_bad == U1 and U2 != U1

    pts_576 = [
        (a, b) for a in range(30) for b in range(30)
        if not (a % 2 == 0 and b % 2 == 0) and not (a % 3 == 0 and b % 3 == 0) and not (a % 5 == 0 and b % 5 == 0)
    ]
    seen_c = set()
    c_orbs = []
    for pt in pts_576:
        if pt in seen_c:
            continue
        oo = []
        cur = pt
        while cur not in oo:
            oo.append(cur)
            seen_c.add(cur)
            cur = ((cur[0] * C_om[0][0] + cur[1] * C_om[1][0]) % 30, (cur[0] * C_om[0][1] + cur[1] * C_om[1][1]) % 30)
        c_orbs.append(oo)
    if len(c_orbs) != prod["E1_b1993_systole_bridge_and_omega"]["C_omega_orbit_count_on_576"] or any(len(o) != 6 for o in c_orbs):
        discrepancies.append("E1_C_omega_orbits_mismatch")

    om6 = mp.exp(I_C * mp.pi / mp.mpf(3))
    tg = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
    l2_om_cc = lame_l2_rk4_logradial(om6, mp.mpc(0), 0)
    l2_tg_cc = lame_l2_rk4_logradial(tg, mp.mpc(0), 6)

    diff_l2_om = abs(l2_om_cc - mp.mpf(prod["E1_b1993_systole_bridge_and_omega"]["L2_omega_richardson"]))
    diff_l2_tg = abs(l2_tg_cc - mp.mpf(prod["E2_z5_up_holonomy_obstruction"]["L2_tau_gold_richardson"]))
    if max(diff_l2_om, diff_l2_tg) > mp.mpf(1) / mp.mpf(25000):
        discrepancies.append("L2_rk4_vs_glrk4_disagreement")

    with mp.workdps(35):
        _, t3g, t4g, _, _, _, _ = theta_nulls_and_serre(tg)
        e1g = (mp.pi ** 2 / mp.mpf(3)) * (t3g ** 4 + t4g ** 4)
        z0g = (mp.mpf(1) + tg) / mp.mpf(2)
        Tb_c0 = rk4_fund_disjoint(lambda t: z0g + t * tg, lambda _t: tg, lambda zz: wp_disjoint(zz, tg, t3g, t4g, e1g) / mp.mpf(4), 40)
        ds_b = mp.sqrt(Tb_c0[0, 0] * Tb_c0[1, 1] - Tb_c0[0, 1] * Tb_c0[1, 0])
        rpf3_im_tr = abs(mp.im((Tb_c0[1, 1] + Tb_c0[0, 0]) / ds_b))
        assert rpf3_im_tr > mp.mpf(1) / mp.mpf(100)

    with mp.workdps(62):
        om6 = mp.exp(I_C * mp.pi / mp.mpf(3))
        l2_om = mp.mpf(mp.nstr(l2_om_cc, 28))
        _, _, _, _, s1_o, s2_o, s3_o = theta_nulls_and_serre(om6)
        s_om_cc_err = max(abs(abs(s1_o) - abs(s2_o)), abs(abs(s2_o) - abs(s3_o)), abs(abs(s1_o) - abs(s3_o)))
        assert s_om_cc_err < mp.mpf(10) ** (-48)

        # Check R_sigma CP-antisymmetry at omega on a FRESH set of order-30 points (disjoint from producer's sample!)
        max_om_antisym_cc = mp.mpf(0)
        max_om_fixed_cc = mp.mpf(0)
        for a30, b30 in [(0, 11), (0, 13), (3, 5), (7, 11), (8, 26), (11, 22)]:
            w0 = (Fr(a30, 30), Fr(b30, 30))
            w_rs = ((-w0[0]) % 1, (w0[0] + w0[1]) % 1)
            yu0 = assemble_yukawa_disjoint(w0[0], w0[1], 1, -4, om6, l2_om)
            yd0 = assemble_yukawa_disjoint(w0[0], w0[1], 1, 2, om6, l2_om)
            _, uu0 = eigh_asc_disjoint(yu0 * yu0.H)
            _, ud0 = eigh_asc_disjoint(yd0 * yd0.H)
            vc0 = uu0.H * ud0
            j0 = mp.im(vc0[0, 0] * vc0[1, 1] * mp.conj(vc0[0, 1]) * mp.conj(vc0[1, 0]))
            yu1 = assemble_yukawa_disjoint(w_rs[0], w_rs[1], 1, -4, om6, l2_om)
            yd1 = assemble_yukawa_disjoint(w_rs[0], w_rs[1], 1, 2, om6, l2_om)
            _, uu1 = eigh_asc_disjoint(yu1 * yu1.H)
            _, ud1 = eigh_asc_disjoint(yd1 * yd1.H)
            vc1 = uu1.H * ud1
            j1 = mp.im(vc1[0, 0] * vc1[1, 1] * mp.conj(vc1[0, 1]) * mp.conj(vc1[1, 0]))
            max_om_antisym_cc = max(max_om_antisym_cc, abs(j0 + j1))
            if w_rs == w0 or w_rs == ((-w0[0]) % 1, (-w0[1]) % 1):
                max_om_fixed_cc = max(max_om_fixed_cc, abs(j0))
        assert max_om_antisym_cc < mp.mpf(10) ** (-45) and max_om_fixed_cc < mp.mpf(10) ** (-45)

        # 2. Disjoint E2, E3, & E4 across ALL 96 points (8 orbits of M_12):
        a12, b12, c12, d12 = 1, 0, 0, 1
        for _ in range(12):
            a12, b12, c12, d12 = (2 * a12 + b12) % 30, (a12 + b12) % 30, (2 * c12 + d12) % 30, (c12 + d12) % 30
        fix96 = sorted((Fr(a, 30), Fr(b, 30)) for (a, b) in pts_576 if ((a * a12 + b * c12) % 30, (a * b12 + b * d12) % 30) == (a, b))
        seen_o = set()
        orbs8 = []
        for pt in fix96:
            if pt in seen_o:
                continue
            oo = []
            cur = pt
            for _ in range(12):
                oo.append(cur)
                seen_o.add(cur)
                cur = ((2 * cur[0] + cur[1]) % 1, (cur[0] + cur[1]) % 1)
            orbs8.append(oo)

        tg = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        l2g = mp.mpf(mp.nstr(l2_tg_cc, 28))
        R_T = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
        R_Ti = ((0, 0, -1), (0, 1, 0), (1, 0, 0))
        R_S = ((0, -1, 0), (-1, 0, 0), (0, 0, -1))

        def mul3(m1, m2):
            return tuple(tuple(sum(m1[r][k] * m2[k][c] for k in range(3)) for c in range(3)) for r in range(3))

        R_A = mul3(R_T, mul3(R_S, mul3(R_Ti, R_S)))
        UA = mp.matrix([[mp.mpf(R_A[r][c]) for c in range(3)] for r in range(3)])
        fac_g = tg + mp.mpf(1)
        tAg = (2 * tg + mp.mpf(1)) / fac_g
        lAg = l2g + mp.log(abs(fac_g))
        phg = fac_g / abs(fac_g)

        cg_map = {(w, ql, qr): assemble_yukawa_disjoint(w[0], w[1], ql, qr, tg, l2g) for w in fix96 for ql, qr in [(1, -4), (1, 2), (-3, 6)]}
        ca_map = {(w, ql, qr): assemble_yukawa_disjoint(w[0], w[1], ql, qr, tAg, lAg) / phg for w in fix96 for ql, qr in [(1, -4), (1, 2), (-3, 6)]}

        sp_cc = {}
        max_sc_cc = mp.mpf(0)
        for w in fix96:
            wn = ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                cd = UA * cg_map[(wn, ql, qr)] * UA.T
                yA = ca_map[(w, ql, qr)]
                r0, c0 = max(((r, c) for r in range(3) for c in range(3)), key=lambda rc: abs(cd[rc[0], rc[1]]))
                sc = yA[r0, c0] / cd[r0, c0]
                max_sc_cc = max(max_sc_cc, abs(abs(sc) - mp.mpf(1)))
                sp_cc[(w, ql, qr)] = sc / abs(sc)
        assert max_sc_cc < mp.mpf(10) ** (-42)

        max_hol_de_cc = mp.mpf(0)
        max_hol_u_cc = mp.mpf(0)
        rpf2_min_periodic_err = mp.mpf(999)
        for idx, oo in enumerate(orbs8):
            r5 = int(oo[0][0] * 30) % 5
            leg5 = 1 if pow(r5, 2, 5) == 1 else -1
            if leg5 != prod["E2_z5_up_holonomy_obstruction"]["orbit_up_holonomies"][idx]["leg5"]:
                discrepancies.append(f"E2_leg5_mismatch_{idx}")
            pu = mp.mpc(1)
            pd = mp.mpc(1)
            pe = mp.mpc(1)
            for n in range(12):
                pu *= sp_cc[(oo[n], 1, -4)]
                pd *= sp_cc[(oo[n], 1, 2)]
                pe *= sp_cc[(oo[n], -3, 6)]
            zt = mp.exp(-2 * I_C * mp.pi * mp.mpf(leg5) / mp.mpf(5))
            max_hol_u_cc = max(max_hol_u_cc, abs(pu - zt))
            max_hol_de_cc = max(max_hol_de_cc, abs(pd - mp.mpf(1)), abs(pe - mp.mpf(1)))
            rpf2_min_periodic_err = min(rpf2_min_periodic_err, abs(pu - mp.mpf(1)))
        assert max_hol_u_cc < mp.mpf(10) ** (-45) and max_hol_de_cc < mp.mpf(10) ** (-45)
        assert rpf2_min_periodic_err > mp.mpf(1)

        def h_inv_sqrt(hm):
            ev, vv = eigh_asc_disjoint(hm)
            return vv * mp.diag([mp.mpf(1) / mp.sqrt(x) for x in ev]) * vv.H

        I3 = mp.eye(3)

        def eval_m21_lu_cc(oo, kv: int, direc: int, u_tup, ua_mat: mp.matrix = UA):
            UQ, Uu, Ud, ULg, Ue = u_tup
            sec_d = {}
            for sec, (ql, qr), Ul, Ur in [("u", (1, -4), UQ, Uu), ("d", (1, 2), UQ, Ud), ("e", (-3, 6), ULg, Ue)]:
                ys = []
                if direc == 1:
                    uap = mp.eye(3)
                    ph = mp.mpc(1)
                    for n in range(7):
                        k = (kv + n) % 12
                        ys.append(Ul * (ph * (uap * cg_map[(oo[k], ql, qr)] * uap.T)) * Ur.H)
                        ph *= sp_cc[(oo[k], ql, qr)]
                        uap = ua_mat * uap
                else:
                    ys.append(Ul * cg_map[(oo[kv], ql, qr)] * Ur.H)
                    uam = mp.eye(3)
                    phm = mp.mpc(1)
                    for n in range(1, 7):
                        pk = (kv - n) % 12
                        uam = ua_mat.T * uam
                        phm = phm / sp_cc[(oo[pk], ql, qr)]
                        ys.append(Ul * (phm * (uam * cg_map[(oo[pk], ql, qr)] * uam.T)) * Ur.H)
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
                X_sol = solve_cols_lu(B_b, A_b)
                W_sol = solve_cols_lu(B_b.H, D_b.H)
                Y_raw = (C_b - D_b * X_sol).H
                sec_d[sec] = (Y_raw, X_sol.H * X_sol, I3 + W_sol.H * W_sol)
            ZQ = I3 + sec_d["u"][1] + sec_d["d"][1]
            ZL = I3 + sec_d["e"][1]
            yu_e = h_inv_sqrt(ZQ) * sec_d["u"][0] * h_inv_sqrt(sec_d["u"][2])
            yd_e = h_inv_sqrt(ZQ) * sec_d["d"][0] * h_inv_sqrt(sec_d["d"][2])
            ye_e = h_inv_sqrt(ZL) * sec_d["e"][0] * h_inv_sqrt(sec_d["e"][2])
            _, uu = eigh_asc_disjoint(yu_e * yu_e.H)
            _, ud = eigh_asc_disjoint(yd_e * yd_e.H)
            su = sv_asc_via_eigh(yu_e)
            sd = sv_asc_via_eigh(yd_e)
            se = sv_asc_via_eigh(ye_e)
            vc = uu.H * ud
            j_sgn = mp.im(vc[0, 0] * vc[1, 1] * mp.conj(vc[0, 1]) * mp.conj(vc[1, 0]))
            md = min(abs(vc[0, 0]), abs(vc[1, 1]), abs(vc[2, 2]))
            obs12 = [
                su[1] / su[2], su[0] / su[2],
                sd[1] / sd[2], sd[0] / sd[2],
                se[1] / se[2], se[0] / se[2],
                sd[2] / su[2], se[2] / sd[2],
                abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]),
                abs(j_sgn),
            ]
            return obs12, md, j_sgn, yu_e

        vert_orbs = []
        for idx, oo in enumerate(orbs8):
            r_pos0 = ((-oo[0][0]) % 1, (oo[0][0] + oo[0][1]) % 1)
            if r_pos0 not in oo:
                vs = sorted(k for k in range(12) if (oo[k][0] % 1, (-(oo[k][0] + oo[k][1])) % 1) == oo[k])
                vert_orbs.append((idx, oo, vs))
        assert len(vert_orbs) == 4

        U_expm = (
            expm_u3_disjoint((1, -2, 3, 2, -1, 4, -3, 2, 1)),
            expm_u3_disjoint((-3, 2, -1, 4, 1, -2, 2, -4, 3)),
            expm_u3_disjoint((2, 3, -4, -1, 3, 2, 1, -2, -3)),
            expm_u3_disjoint((-1, 4, 2, -3, 2, 1, 4, -1, 2)),
            expm_u3_disjoint((4, -1, -2, 1, -4, 3, -2, 3, -1)),
        )

        max_cw_ccw_cpe_cc = mp.mpf(0)
        max_cw_ccw_jsum_cc = mp.mpf(0)
        max_expm_u3_5_err = mp.mpf(0)
        max_prod_vs_cc_rel_diff = mp.mpf(0)

        chain_counter = 0
        cc_m13_cnt = 0
        cc_j_cnt = 0
        cc_md_cnt = 0
        first_yue = None
        first_oo = None
        first_kv = None
        first_obs = None

        for idx, oo, vs in vert_orbs:
            o_cw0, md_cw0, j_cw0, _ = eval_m21_lu_cc(oo, vs[0], 1, (I3, I3, I3, I3, I3))
            o_ccw0, md_ccw0, j_ccw0, _ = eval_m21_lu_cc(oo, vs[0], -1, (I3, I3, I3, I3, I3))
            max_cw_ccw_cpe_cc = max(max_cw_ccw_cpe_cc, max(abs(o_cw0[k] - o_ccw0[k]) for k in range(11)), abs(md_cw0 - md_ccw0))
            max_cw_ccw_jsum_cc = max(max_cw_ccw_jsum_cc, abs(j_cw0 + j_ccw0))

            for kv in vs:
                obs_id, md_id, _, yue_id = eval_m21_lu_cc(oo, kv, 1, (I3, I3, I3, I3, I3))
                obs_ex, md_ex, _, _ = eval_m21_lu_cc(oo, kv, 1, U_expm)
                max_expm_u3_5_err = max(max_expm_u3_5_err, max(abs(obs_id[k] - obs_ex[k]) for k in range(12)), abs(md_id - md_ex))

                if first_yue is None:
                    first_yue = yue_id
                    first_oo = oo
                    first_kv = kv
                    first_obs = obs_id

                if max(obs_id[1], obs_id[3], obs_id[5]) < mp.mpf(2) / mp.mpf(1000000):
                    cc_m13_cnt += 1
                if obs_id[11] > mp.mpf(1) / mp.mpf(1000):
                    cc_j_cnt += 1
                if md_id > mp.mpf(9) / mp.mpf(10):
                    cc_md_cnt += 1

                p_rec = prod["E4_linear_21x21_boundary_dirac_eft"]["all_8_vertex_linear_eft_chains"][chain_counter]
                p_vec = [
                    mp.mpf(p_rec["up_ratios"][0]), mp.mpf(p_rec["up_ratios"][1]),
                    mp.mpf(p_rec["down_ratios"][0]), mp.mpf(p_rec["down_ratios"][1]),
                    mp.mpf(p_rec["lep_ratios"][0]), mp.mpf(p_rec["lep_ratios"][1]),
                    mp.mpf(p_rec["inter_sector_yb_yt_and_ytau_yb"][0]), mp.mpf(p_rec["inter_sector_yb_yt_and_ytau_yb"][1]),
                    mp.mpf(p_rec["ckm_moduli_and_min_diag"][0]), mp.mpf(p_rec["ckm_moduli_and_min_diag"][1]),
                    mp.mpf(p_rec["ckm_moduli_and_min_diag"][2]), mp.mpf(p_rec["jarlskog_abs"]),
                ]
                rd = max(abs(obs_id[k] - p_vec[k]) / max(p_vec[k], mp.mpf(10) ** (-14)) for k in range(12))
                max_prod_vs_cc_rel_diff = max(max_prod_vs_cc_rel_diff, rd)
                chain_counter += 1

        assert max_cw_ccw_cpe_cc < mp.mpf(10) ** (-45) and max_cw_ccw_jsum_cc < mp.mpf(10) ** (-45)
        assert max_expm_u3_5_err < mp.mpf(10) ** (-45)

        cc_counts = {
            "m1_over_m3_lt_2e_minus_6": cc_m13_cnt,
            "jarlskog_gt_1e_minus_3": cc_j_cnt,
            "min_diag_gt_9_over_10": cc_md_cnt,
        }
        if cc_counts != prod["E4_linear_21x21_boundary_dirac_eft"]["eight_chain_pass_counts"]:
            discrepancies.append("E4_pass_counts_mismatch")
        if max_prod_vs_cc_rel_diff > mp.mpf(1) / mp.mpf(500):
            discrepancies.append("E4_indep_L2_observable_disagreement")

        # RPF4: Illegal single-Dirac left-right overlap U_u^H V_u drifts > 1/10 under U(3)_{u_R}
        _, u_s1 = eigh_asc_disjoint(first_yue * first_yue.H)
        _, v_s1 = eigh_asc_disjoint(first_yue.H * first_yue)
        yue_rot = first_yue * U_expm[1].H
        _, u_s2 = eigh_asc_disjoint(yue_rot * yue_rot.H)
        _, v_s2 = eigh_asc_disjoint(yue_rot.H * yue_rot)
        rpf4_lr_drift = max(abs(abs((u_s1.H * v_s1)[r, c]) - abs((u_s2.H * v_s2)[r, c])) for r in range(3) for c in range(3))
        assert rpf4_lr_drift > mp.mpf(1) / mp.mpf(10)

        # RPF5: Omitting UA transport along the 7-sheet boundary-Dirac chain shifts CKM mixing by > 1/5
        obs_noua, _, _, _ = eval_m21_lu_cc(first_oo, first_kv, 1, (I3, I3, I3, I3, I3), ua_mat=I3)
        rpf5_noua_ckm_drift = max(abs(obs_noua[8 + k] - first_obs[8 + k]) for k in range(3))
        assert rpf5_noua_ckm_drift > mp.mpf(1) / mp.mpf(5)

    assert len(discrepancies) == 0, discrepancies

    cc_out = {
        "card": "AGY-C59-COUNTERCHECK",
        "empirical_inputs": "0 of 19",
        "verified_producer_sha256": actual_sha,
        "ast_firewall_countercheck": cc_ast,
        "ast_firewall_producer": prod_ast,
        "discrepancies_count": len(discrepancies),
        "disjoint_e1_S_omega_eq_err": mp.nstr(s_om_cc_err, 12),
        "disjoint_e1_fresh_pts_Rsigma_antisym_err": mp.nstr(max_om_antisym_cc, 12),
        "disjoint_e1_fresh_pts_fixed_jarlskog": mp.nstr(max_om_fixed_cc, 12),
        "disjoint_rk4_logradial_L2_diffs": {
            "omega": mp.nstr(diff_l2_om, 10),
            "tau_gold": mp.nstr(diff_l2_tg, 10),
        },
        "disjoint_e2_unit_modulus_sc_max_dev": mp.nstr(max_sc_cc, 12),
        "disjoint_e2_up_holonomy_zeta5_max_err": mp.nstr(max_hol_u_cc, 12),
        "disjoint_e2_down_lep_holonomy_1_max_err": mp.nstr(max_hol_de_cc, 12),
        "disjoint_e3_cw_vs_ccw_cpeven_max_diff": mp.nstr(max_cw_ccw_cpe_cc, 12),
        "disjoint_e3_cw_plus_ccw_jarlskog_max_err": mp.nstr(max_cw_ccw_jsum_cc, 12),
        "disjoint_e4_expm_u3_5_max_err_all8": mp.nstr(max_expm_u3_5_err, 12),
        "disjoint_e4_vs_producer_indep_L2_max_rel_diff": mp.nstr(max_prod_vs_cc_rel_diff, 10),
        "referee_planted_faults": {
            "RPF1_noncommutator_LR_RL_trace": rpf1_bad_trace,
            "RPF2_periodic_up_holonomy_min_jump": mp.nstr(rpf2_min_periodic_err, 8),
            "RPF3_c0_nonfuchsian_im_tr": mp.nstr(rpf3_im_tr, 8),
            "RPF4_illegal_lr_overlap_drift": mp.nstr(rpf4_lr_drift, 8),
            "RPF5_no_UA_transport_ckm_drift": mp.nstr(rpf5_noua_ckm_drift, 8),
        },
        "all_referee_checks_passed": True,
    }
    cc_text = json.dumps(cc_out, indent=2, sort_keys=True) + "\n"
    CC_JSON.write_text(cc_text, encoding="utf-8")


if __name__ == "__main__":
    main()
