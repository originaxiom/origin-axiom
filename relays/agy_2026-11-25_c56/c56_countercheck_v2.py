#!/usr/bin/env python3
"""Card AGY-C56 Disjoint Zero-Trust Cold-Room Countercheck (Strictly 0 of 19; python3 -I).

Implements completely disjoint algorithms (zero shared code with c56_whole_instrument_producer.py,
and zero runtime script-hash overwrites):
- Direct integer lattice sum for theta[a, b](tau) (no mp.jtheta),
- Euler pentagonal series for eta(tau) (no mp.qp),
- Analytic Lambert series pi*cot(pi*z) + 4*pi*sum q^{2m}/(1-q^{2m}) sin(2*pi*m*z) for theta_1'/theta_1 (no mp.diff),
- Direct Hermitian mp.eigh (no mp.svd_c),
- Explicit 4-stage RK4 with logarithmic radial coordinate near z=0 for Lame uniformization (no implicit GL-RK4),
- Unitary matrix exponential mp.expm(i*H) on fresh skew-Hermitian generators for U(3)^5 scrambling (no Cayley),
- Unitary | |sc| - 1 | < 10^{-45} checks, pure-theta 3/5 & 1/5 valuation counterchecks, full 16-chain & 8-chain
  mirror-menu verification, and SHA-256 + parse_float=bad_float check of c56_out.json (discrepancies_count == 0)."""
import ast
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
PROD_JSON = HERE / "c56_out.json"
PROD_HASH = HERE / "OUTPUT_SHA256.txt"
CC_JSON = HERE / "c56_countercheck_v2_out.json"

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


def assemble_yukawa_disjoint(pa: Fr, pb: Fr, ql: int, qr: int, tv: mp.mpc, l_end: mp.mpf, with_norm: bool = True, return_pure_theta: bool = False):
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
    t_num = {}
    n_ch = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hr, cs[sk][1] - hr
        dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
        if not ((al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0)):
            tn = kap[sk] * theta_char_sum(cs[sk][0], cs[sk][1], tv) * theta_char_sum(ds[sk][0], ds[sk][1], tv)
            t_num[sk] = tn
            r_res = tn / t1p
            if with_norm:
                zv = r2m(al) * tv + r2m(be)
                a0 = 2 * I_C * mp.pi * r2m(al) + theta1_logderiv_lambert(zv, tv)
                c_ch = kronecker_fu_disjoint(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
                nv = mp.sqrt(2 * mp.pi * l_end + c_ch)
                n_ch[sk] = nv
                mw += nv * r_res * ed[sk]
            else:
                n_ch[sk] = mp.mpf(1)
                mw += r_res * ed[sk]
        else:
            t_num[sk] = mp.mpc(0)
            n_ch[sk] = mp.mpf(0)
    ym = mp.matrix([[ct[r][c][0, 0] * mw[0, 0] + ct[r][c][0, 1] * mw[0, 1] + ct[r][c][1, 0] * mw[1, 0] + ct[r][c][1, 1] * mw[1, 1] for c in range(3)] for r in range(3)])
    if return_pure_theta:
        return mp.sqrt(y) * ym, mw, t_num, n_ch, t1p
    return mp.sqrt(y) * ym, mw


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


def main() -> None:
    cc_ast = verify_ast_clean(Path(__file__))
    prod_ast = verify_ast_clean(HERE / "c56_whole_instrument_producer.py")

    raw_bytes = PROD_JSON.read_bytes()
    actual_sha = hashlib.sha256(raw_bytes).hexdigest()
    recorded_sha = PROD_HASH.read_text(encoding="utf-8").strip().split()[0]
    assert actual_sha == recorded_sha, (actual_sha, recorded_sha)
    prod = json.loads(raw_bytes.decode("utf-8"), parse_float=bad_float)

    discrepancies = []

    R_I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    R_T = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
    R_Ti = ((0, 0, -1), (0, 1, 0), (1, 0, 0))
    R_S = ((0, -1, 0), (-1, 0, 0), (0, 0, -1))

    def mul3(a, b):
        return tuple(tuple(sum(a[r][k] * b[k][c] for k in range(3)) for c in range(3)) for r in range(3))

    bfs = {(0, 1): ((1, 0, 0, 1), R_I)}
    qb = [((1, 0, 0, 1), R_I)]
    for_moves = [((1, 1, 0, 1), R_T), ((1, -1, 0, 1), R_Ti), ((0, -1, 1, 0), R_S), ((-1, 0, 0, -1), R_I)]
    while qb and len(bfs) < 576:
        (a, b, c, d), rc = qb.pop(0)
        for (ga, gb, gc, gd), rg in for_moves:
            na, nb, nc, nd = a * ga + b * gc, a * gb + b * gd, c * ga + d * gc, c * gb + d * gd
            k = (nc % 30, nd % 30)
            if not (k[0] % 2 == 0 and k[1] % 2 == 0) and not (k[0] % 3 == 0 and k[1] % 3 == 0) and not (k[0] % 5 == 0 and k[1] % 5 == 0):
                if k not in bfs:
                    bfs[k] = ((na, nb, nc, nd), mul3(rc, rg))
                    qb.append(bfs[k])
    if len(bfs) != prod["E1_cube_group_and_p882"]["primitive_order30_count"]:
        discrepancies.append("E1_576_count")

    # 1. Countercheck E1 on DIFFERENT modulus tau_alt = -29/100 + 153/100 i, checking | |sc| - 1 | < 10^-45 on T, S, -I and 12 cusps:
    with mp.workdps(60):
        tau_alt = mp.mpc(mp.mpf(-29) / mp.mpf(100), mp.mpf(153) / mp.mpf(100))
        l_alt = mp.mpf(29) / mp.mpf(10)
        w_b = (Fr(0, 30), Fr(1, 30))
        sample_alt = [k for k in bfs if (k[1] - 2 * k[0]) % 5 == 0 and abs(bfs[k][0][2]) <= 7][:6] + [
            k for k in bfs if (k[1] - 2 * k[0]) % 5 != 0 and abs(bfs[k][0][2]) <= 5
        ][:6]
        max_e1_cc = mp.mpf(0)
        max_sc_cc = mp.mpf(0)
        for (ga, gb, gc, gd), rt in [((1, 1, 0, 1), R_T), ((0, -1, 1, 0), R_S), ((-1, 0, 0, -1), R_I)]:
            Rm = mp.matrix([[mp.mpf(rt[r][col]) for col in range(3)] for r in range(3)])
            fac = gc * tau_alt + gd
            tc = (ga * tau_alt + gb) / fac
            lc = l_alt + mp.log(abs(fac))
            ph = fac / abs(fac)
            wp0 = (Fr(2, 30), Fr(29, 30))
            winv = ((wp0[0] * gd - wp0[1] * gc) % 1, (-wp0[0] * gb + wp0[1] * ga) % 1)
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                y0, _ = assemble_yukawa_disjoint(wp0[0], wp0[1], ql, qr, tau_alt, l_alt)
                y1, _ = assemble_yukawa_disjoint(winv[0], winv[1], ql, qr, tc, lc)
                y1 = y1 / ph
                cd = Rm * y0 * Rm.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cd[rc[0], rc[1]]))
                sc = y1[r0, c0] / cd[r0, c0]
                max_sc_cc = max(max_sc_cc, abs(abs(sc) - mp.mpf(1)))
                max_e1_cc = max(max_e1_cc, mp.mnorm(y1 - sc * cd, "F") / mp.mnorm(y0, "F"))
        for cm, dm in sample_alt:
            (a, b, c, d), rt = bfs[(cm, dm)]
            Rm = mp.matrix([[mp.mpf(rt[r][col]) for col in range(3)] for r in range(3)])
            fac = c * tau_alt + d
            tc = (a * tau_alt + b) / fac
            lc = l_alt + mp.log(abs(fac))
            ph = fac / abs(fac)
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                yi, _ = assemble_yukawa_disjoint(Fr(cm, 30), Fr(dm, 30), ql, qr, tau_alt, l_alt)
                yc, _ = assemble_yukawa_disjoint(w_b[0], w_b[1], ql, qr, tc, lc)
                yc = yc / ph
                cd = Rm * yi * Rm.T
                r0, c0 = max(((r, col) for r in range(3) for col in range(3)), key=lambda rc: abs(cd[rc[0], rc[1]]))
                sc = yc[r0, c0] / cd[r0, c0]
                max_sc_cc = max(max_sc_cc, abs(abs(sc) - mp.mpf(1)))
                er = mp.mnorm(yc - sc * cd, "F") / mp.mnorm(yi, "F")
                if er > max_e1_cc:
                    max_e1_cc = er
        assert max_e1_cc < mp.mpf(10) ** (-45) and max_sc_cc < mp.mpf(10) ** (-45)

        Rm_bad = mp.matrix([[0, 0, -1], [0, 1, 0], [-1, 0, 0]])
        yi_p1, _ = assemble_yukawa_disjoint(Fr(0, 30), Fr(1, 30), 1, -4, tau_alt + 1, l_alt)
        yi_0, _ = assemble_yukawa_disjoint(Fr(0, 30), Fr(1, 30), 1, -4, tau_alt, l_alt)
        cd_bad = Rm_bad * yi_0 * Rm_bad.T
        sc_b = yi_p1[0, 2] / cd_bad[0, 2]
        rpf1_err = mp.mnorm(yi_p1 - sc_b * cd_bad, "F") / mp.mnorm(yi_0, "F")
        assert rpf1_err > mp.mpf(1) / mp.mpf(10)

    # 2. Countercheck E2 pure-theta 3/5 & 1/5 valuation step on y = 38 -> 48 + all 30 reps on y = 32 -> 42 via sv_asc_via_eigh:
    with mp.workdps(90):
        l_cc = mp.mpf(23) / mp.mpf(10)
        max_35_cc = mp.mpf(0)
        max_15_cc = mp.mpf(0)
        for a10, b10 in [(1, 0), (2, 1), (3, 0), (4, 1)]:
            _, mw38, tn38, nc38, tp38 = assemble_yukawa_disjoint(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 38), l_cc, with_norm=True, return_pure_theta=True)
            _, mw48, tn48, _, tp48 = assemble_yukawa_disjoint(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 48), l_cc, with_norm=True, return_pure_theta=True)
            q38 = abs(tn38["1"] ** 2 + tn38["i"] ** 2)
            q48 = abs(tn48["1"] ** 2 + tn48["i"] ** 2)
            r35 = -mp.log(q48 / q38) / (10 * mp.pi)
            s38 = abs(tp38) * sv_asc_via_eigh(mw38)[1]
            s48 = abs(tp48) * sv_asc_via_eigh(mw48)[1]
            r15 = -mp.log((s48 ** 2) / (s38 ** 2)) / (10 * mp.pi)
            assert abs((nc38["1"] ** 2) - (nc38["j"] ** 2)) > mp.mpf(1)
            max_35_cc = max(max_35_cc, abs(r35 - mp.mpf(3) / mp.mpf(5)))
            max_15_cc = max(max_15_cc, abs(r15 - mp.mpf(1) / mp.mpf(5)))
        assert max_35_cc < mp.mpf(10) ** (-20) and max_15_cc < mp.mpf(10) ** (-10)

        pts_30_rep = sorted({(min(ia % 10, (-ia) % 10), ib % 10 if ia % 10 <= (-ia) % 10 else (-ib) % 10) for (ia, ib) in bfs if ia % 5 != 0})
        r23_cc = set()
        r13_cc = set()
        max_25_cc = mp.mpf(0)
        for a10, b10 in pts_30_rep:
            y32, _ = assemble_yukawa_disjoint(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 32), l_cc)
            y42, _ = assemble_yukawa_disjoint(Fr(a10, 30), Fr(b10, 30), -3, 6, mp.mpc(0, 42), l_cc)
            s32 = sv_asc_via_eigh(y32)
            s42 = sv_asc_via_eigh(y42)
            rt23 = -(mp.log(s42[1] / s42[2]) - mp.log(s32[1] / s32[2])) / (10 * mp.pi)
            rt13 = -(mp.log(s42[0] / s42[2]) - mp.log(s32[0] / s32[2])) / (10 * mp.pi)
            dv = abs(rt23 - mp.mpf(2) / mp.mpf(5))
            if dv > max_25_cc:
                max_25_cc = dv
            r23_cc.add(str(Fr(int(mp.nint(60 * rt23)), 60)))
            r13_cc.add(str(Fr(int(mp.nint(60 * rt13)), 60)))
        if sorted(r23_cc) != prod["E2_lepton_two_fifths_theorem"]["converged_m2_over_m3_rate_set_all60"]:
            discrepancies.append("E2_r23_set")
        if sorted(r13_cc) != prod["E2_lepton_two_fifths_theorem"]["converged_m1_over_m3_rate_set_all60"]:
            discrepancies.append("E2_r13_set")

        _, mw0_ok = assemble_yukawa_disjoint(Fr(1, 30), Fr(7, 30), -3, 6, mp.mpc(mp.mpf(1) / mp.mpf(5), mp.mpf(2)), l_cc, with_norm=False)
        sv_ok = sv_asc_via_eigh(mw0_ok)
        assert sv_ok[0] / sv_ok[1] < mp.mpf(10) ** (-70)
        mw0_bad = mp.matrix([[mw0_ok[0, 0], -mw0_ok[0, 1]], [mw0_ok[1, 0], mw0_ok[1, 1]]])
        sv_bad = sv_asc_via_eigh(mw0_bad)
        rpf2_ratio = sv_bad[0] / sv_bad[1]
        assert rpf2_ratio > mp.mpf(1) / mp.mpf(100)

    # 3. Countercheck E4 via Disjoint Explicit-RK4 + Log-Radial Lame Solver:
    om6 = mp.exp(I_C * mp.pi / mp.mpf(3))
    tg = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
    l2_om_cc = lame_l2_rk4_logradial(om6, mp.mpc(0), 0)
    l2_i_cc = lame_l2_rk4_logradial(I_C, mp.mpc(0), 0)
    l2_tg_cc = lame_l2_rk4_logradial(tg, mp.mpc(0), 6)

    diff_l2_om = abs(l2_om_cc - mp.mpf(prod["E4_standalone_lame_and_unit_contraction"]["L2_omega_richardson"]))
    diff_l2_i = abs(l2_i_cc - mp.mpf(prod["E4_standalone_lame_and_unit_contraction"]["L2_i_richardson"]))
    diff_l2_tg = abs(l2_tg_cc - mp.mpf(prod["E4_standalone_lame_and_unit_contraction"]["L2_tau_gold_richardson"]))
    if max(diff_l2_om, diff_l2_i, diff_l2_tg) > mp.mpf(1) / mp.mpf(25000):
        discrepancies.append("E4_L2_disagreement")

    with mp.workdps(35):
        _, t3g, t4g, _, _, _, _ = theta_nulls_and_serre(tg)
        e1g = (mp.pi ** 2 / mp.mpf(3)) * (t3g ** 4 + t4g ** 4)
        z0g = (mp.mpf(1) + tg) / mp.mpf(2)
        Tb_c0 = rk4_fund_disjoint(lambda t: z0g + t * tg, lambda _t: tg, lambda zz: wp_disjoint(zz, tg, t3g, t4g, e1g) / mp.mpf(4), 40)
        ds_b = mp.sqrt(Tb_c0[0, 0] * Tb_c0[1, 1] - Tb_c0[0, 1] * Tb_c0[1, 0])
        rpf3_im_tr = abs(mp.im((Tb_c0[1, 1] + Tb_c0[0, 0]) / ds_b))
        assert rpf3_im_tr > mp.mpf(1) / mp.mpf(100)

    # 4. Countercheck E3 & E5 Full 16-Chain & 8-Chain Mirror Menu + Expm U(3)^5 Scrambling against c56_out.json:
    a12, b12, c12, d12 = 1, 0, 0, 1
    for _ in range(12):
        a12, b12, c12, d12 = (2 * a12 + b12) % 30, (a12 + b12) % 30, (2 * c12 + d12) % 30, (c12 + d12) % 30
    fix96 = sorted((Fr(k[0], 30), Fr(k[1], 30)) for k in bfs if ((k[0] * a12 + k[1] * c12) % 30, (k[0] * b12 + k[1] * d12) % 30) == k)
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

    # Build the 4 unique -I_2 orbit representatives {0, 1, 3, 5} (8 representative chains; each has exact -I_2 twin):
    rep_bond4 = []
    rep_vert4 = []
    for idx in [0, 3]:
        oo = orbs8[idx]
        bs = sorted(k for k in range(12) if ((-oo[k][0]) % 1, (oo[k][0] + oo[k][1]) % 1) == oo[(k + 1) % 12])
        for kb in bs:
            rep_bond4.append([oo[(kb + 1 + n) % 12] for n in range(6)])
    for idx in [1, 5]:
        oo = orbs8[idx]
        vs = sorted(k for k in range(12) if (oo[k][0] % 1, (-(oo[k][0] + oo[k][1])) % 1) == oo[k])
        for kv in vs:
            rep_vert4.append([oo[(kv + n) % 12] for n in range(7)])

    with mp.workdps(62):
        tg = mp.mpc(mp.mpf(1) / mp.mpf(2), mp.sqrt(mp.mpf(5)) / mp.mpf(2))
        l2g = mp.mpf(mp.nstr(l2_tg_cc, 28))
        R_A = mul3(R_T, mul3(R_S, mul3(R_Ti, R_S)))
        UA = mp.matrix([[mp.mpf(R_A[r][c]) for c in range(3)] for r in range(3)])
        fac_g = tg + 1
        tAg = (2 * tg + 1) / fac_g
        lAg = l2g + mp.log(abs(fac_g))
        phg = fac_g / abs(fac_g)

        # Cache on the 48 points of representative orbits {0, 1, 3, 5}:
        pts48 = [w for idx in [0, 1, 3, 5] for w in orbs8[idx]]
        cg_map = {(w, ql, qr): assemble_yukawa_disjoint(w[0], w[1], ql, qr, tg, l2g)[0] for w in pts48 for ql, qr in [(1, -4), (1, 2), (-3, 6)]}
        ca_map = {(w, ql, qr): assemble_yukawa_disjoint(w[0], w[1], ql, qr, tAg, lAg)[0] / phg for w in pts48 for ql, qr in [(1, -4), (1, 2), (-3, 6)]}
        sp_cc = {}
        max_step_sc_cc = mp.mpf(0)
        for w in pts48:
            wn = ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
            for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
                cd = UA * cg_map[(wn, ql, qr)] * UA.T
                yA = ca_map[(w, ql, qr)]
                r0, c0 = max(((r, c) for r in range(3) for c in range(3)), key=lambda rc: abs(cd[rc[0], rc[1]]))
                sc = yA[r0, c0] / cd[r0, c0]
                max_step_sc_cc = max(max_step_sc_cc, abs(abs(sc) - mp.mpf(1)))
                sp_cc[(w, ql, qr)] = sc / abs(sc)
        assert max_step_sc_cc < mp.mpf(10) ** (-42)

        def h_inv_sqrt(hm):
            ev, vv = eigh_asc_disjoint(hm)
            return vv * mp.diag([1 / mp.sqrt(x) for x in ev]) * vv.H

        def eval_gram_cc(ch, u_tup):
            UQ, Uu, Ud, ULg, Ue = u_tup
            K = len(ch)
            yus, yds, yes = [], [], []
            uap = mp.eye(3)
            pu, pd, pe = mp.mpc(1), mp.mpc(1), mp.mpc(1)
            for n in range(K):
                yus.append(UQ * (pu * (uap * cg_map[(ch[n], 1, -4)] * uap.T)) * Uu.H)
                yds.append(UQ * (pd * (uap * cg_map[(ch[n], 1, 2)] * uap.T)) * Ud.H)
                yes.append(ULg * (pe * (uap * cg_map[(ch[n], -3, 6)] * uap.T)) * Ue.H)
                pu *= sp_cc[(ch[n], 1, -4)]
                pd *= sp_cc[(ch[n], 1, 2)]
                pe *= sp_cc[(ch[n], -3, 6)]
                uap = UA * uap
            cQ = [mp.eye(3)]
            cL = [mp.eye(3)]
            for n in range(K - 1):
                cQ.append(((yus[n] * yus[n].H + yds[n] * yds[n].H) / mp.mpf(2)) * cQ[-1])
                cL.append((yes[n] * yes[n].H) * cL[-1])
            cu = [None] * K
            cd = [None] * K
            ce = [None] * K
            cu[-1] = cd[-1] = ce[-1] = mp.eye(3)
            for n in range(K - 2, -1, -1):
                cu[n] = (yus[n + 1].H * yus[n + 1]) * cu[n + 1]
                cd[n] = (yds[n + 1].H * yds[n + 1]) * cd[n + 1]
                ce[n] = (yes[n + 1].H * yes[n + 1]) * ce[n + 1]
            ZQ = sum((cQ[n].H * cQ[n] for n in range(K)), mp.zeros(3, 3))
            ZL = sum((cL[n].H * cL[n] for n in range(K)), mp.zeros(3, 3))
            Zu = sum((cu[n].H * cu[n] for n in range(K)), mp.zeros(3, 3))
            Zd = sum((cd[n].H * cd[n] for n in range(K)), mp.zeros(3, 3))
            Ze = sum((ce[n].H * ce[n] for n in range(K)), mp.zeros(3, 3))
            Iu = sum((cQ[n].H * yus[n] * cu[n] for n in range(K)), mp.zeros(3, 3))
            Id = sum((cQ[n].H * yds[n] * cd[n] for n in range(K)), mp.zeros(3, 3))
            Ie = sum((cL[n].H * yes[n] * ce[n] for n in range(K)), mp.zeros(3, 3))
            yu_e = h_inv_sqrt(ZQ) * Iu * h_inv_sqrt(Zu)
            yd_e = h_inv_sqrt(ZQ) * Id * h_inv_sqrt(Zd)
            ye_e = h_inv_sqrt(ZL) * Ie * h_inv_sqrt(Ze)
            eu, uu = eigh_asc_disjoint(yu_e * yu_e.H)
            ed_v, ud = eigh_asc_disjoint(yd_e * yd_e.H)
            ee, _ = eigh_asc_disjoint(ye_e * ye_e.H)
            su = [mp.sqrt(x) for x in eu]
            sd = [mp.sqrt(x) for x in ed_v]
            se = [mp.sqrt(x) for x in ee]
            vc = uu.H * ud
            jcp = abs(mp.im(vc[0, 0] * vc[1, 1] * mp.conj(vc[0, 1]) * mp.conj(vc[1, 0])))
            md = min(abs(vc[0, 0]), abs(vc[1, 1]), abs(vc[2, 2]))
            return [su[1] / su[2], su[0] / su[2], sd[1] / sd[2], sd[0] / sd[2], se[1] / se[2], se[0] / se[2], abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), jcp], md, yu_e

        def eval_stag7_cc(ch, u_tup):
            UQ, Uu, Ud, ULg, Ue = u_tup
            res = []
            for (ql, qr), Ul, Ur in [((1, -4), UQ, Uu), ((1, 2), UQ, Ud), ((-3, 6), ULg, Ue)]:
                ys = []
                uap = mp.eye(3)
                ph = mp.mpc(1)
                for n in range(7):
                    ys.append(Ul * (ph * (uap * cg_map[(ch[n], ql, qr)] * uap.T)) * Ur.H)
                    ph *= sp_cc[(ch[n], ql, qr)]
                    uap = UA * uap
                p7 = ys[0] * ys[1].H * ys[2] * ys[3].H * ys[4] * ys[5].H * ys[6]
                _, uv = eigh_asc_disjoint(p7 * p7.H)
                res.append((sv_asc_via_eigh(p7), uv))
            (su, uu), (sd, ud), (se, _) = res
            vc = uu.H * ud
            jcp = abs(mp.im(vc[0, 0] * vc[1, 1] * mp.conj(vc[0, 1]) * mp.conj(vc[1, 0])))
            md = min(abs(vc[0, 0]), abs(vc[1, 1]), abs(vc[2, 2]))
            return [su[1] / su[2], su[0] / su[2], sd[1] / sd[2], sd[0] / sd[2], se[1] / se[2], se[0] / se[2], abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), jcp], md

        I3 = mp.eye(3)
        rep8_gram = [eval_gram_cc(ch, (I3, I3, I3, I3, I3)) for ch in rep_bond4 + rep_vert4]
        rep4_stag = [eval_stag7_cc(ch, (I3, I3, I3, I3, I3)) for ch in rep_vert4]

        pc_16 = {
            "m1_over_m3_lt_4e_minus_4": 2 * sum(1 for o, _, _ in rep8_gram if max(o[1], o[3], o[5]) < mp.mpf(4) / mp.mpf(10000)),
            "m1_over_m3_lt_1e_minus_4": 2 * sum(1 for o, _, _ in rep8_gram if max(o[1], o[3], o[5]) < mp.mpf(1) / mp.mpf(10000)),
            "m2_over_m3_lt_1_over_5": 2 * sum(1 for o, _, _ in rep8_gram if max(o[0], o[2], o[4]) < mp.mpf(1) / mp.mpf(5)),
            "min_diag_gt_3_over_4": 2 * sum(1 for _, m, _ in rep8_gram if m > mp.mpf(3) / mp.mpf(4)),
            "min_diag_gt_9_over_10": 2 * sum(1 for _, m, _ in rep8_gram if m > mp.mpf(9) / mp.mpf(10)),
            "jarlskog_gt_1e_minus_5": 2 * sum(1 for o, _, _ in rep8_gram if o[9] > mp.mpf(10) ** (-5)),
            "standard_ckm_ordering": 2 * sum(1 for o, _, _ in rep8_gram if o[6] > o[7] > o[8]),
        }
        pc_stag = {
            "m1_over_m3_lt_2e_minus_6": 2 * sum(1 for o, _ in rep4_stag if max(o[1], o[3], o[5]) < mp.mpf(2) / mp.mpf(1000000)),
            "jarlskog_gt_8e_minus_4": 2 * sum(1 for o, _ in rep4_stag if o[9] > mp.mpf(8) / mp.mpf(10000)),
            "min_diag_gt_9_over_10": 2 * sum(1 for _, m in rep4_stag if m > mp.mpf(9) / mp.mpf(10)),
        }
        if pc_16 != prod["E5_waveguide_full_16chain_menu_and_haar"]["gramian_16chain_pass_counts"]:
            discrepancies.append("E5_16chain_counts_mismatch")
        if pc_stag != prod["E5_waveguide_full_16chain_menu_and_haar"]["stag7_8chain_pass_counts"]:
            discrepancies.append("E5_stag7_counts_mismatch")

        obs_b0_id, md_b0_id, yue_id = rep8_gram[0]
        U_expm = (
            expm_u3_disjoint((1, -2, 3, 2, -1, 4, -3, 2, 1)),
            expm_u3_disjoint((-3, 2, -1, 4, 1, -2, 2, -4, 3)),
            expm_u3_disjoint((2, 3, -4, -1, 3, 2, 1, -2, -3)),
            expm_u3_disjoint((-1, 4, 2, -3, 2, 1, 4, -1, 2)),
            expm_u3_disjoint((4, -1, -2, 1, -4, 3, -2, 3, -1)),
        )
        obs_b0_ex, _, _ = eval_gram_cc(rep_bond4[0], U_expm)
        obs_v1_id, _ = rep4_stag[0]
        obs_v1_ex, _ = eval_stag7_cc(rep_vert4[0], U_expm)
        expm_haar_err = max(max(abs(obs_b0_id[k] - obs_b0_ex[k]) for k in range(10)), max(abs(obs_v1_id[k] - obs_v1_ex[k]) for k in range(10)))
        assert expm_haar_err < mp.mpf(10) ** (-45)

        _, u_single = eigh_asc_disjoint(yue_id * yue_id.H)
        _, v_single = eigh_asc_disjoint(yue_id.H * yue_id)
        yue_rot = yue_id * U_expm[1].H
        _, u_s2 = eigh_asc_disjoint(yue_rot * yue_rot.H)
        _, v_s2 = eigh_asc_disjoint(yue_rot.H * yue_rot)
        rpf4_lr_drift = max(abs(abs((u_single.H * v_single)[r, c]) - abs((u_s2.H * v_s2)[r, c])) for r in range(3) for c in range(3))
        assert rpf4_lr_drift > mp.mpf(1) / mp.mpf(100)

        pb0 = prod["E5_waveguide_full_16chain_menu_and_haar"]["bond6_orbit0_half0_gramian"]
        prod_vec = [
            mp.mpf(pb0["up_ratios"][0]), mp.mpf(pb0["up_ratios"][1]),
            mp.mpf(pb0["down_ratios"][0]), mp.mpf(pb0["down_ratios"][1]),
            mp.mpf(pb0["lep_ratios"][0]), mp.mpf(pb0["lep_ratios"][1]),
            mp.mpf(pb0["ckm_moduli_and_min_diag"][0]), mp.mpf(pb0["ckm_moduli_and_min_diag"][1]),
            mp.mpf(pb0["ckm_moduli_and_min_diag"][2]), mp.mpf(pb0["jarlskog_abs"]),
        ]
        max_b0_rel_diff = max(abs(obs_b0_id[k] - prod_vec[k]) / max(prod_vec[k], mp.mpf(10) ** (-12)) for k in range(10))
        if max_b0_rel_diff > mp.mpf(1) / mp.mpf(500):
            discrepancies.append("E5_bond6_orbit0_disagreement")

        UA_save = UA
        UA = mp.eye(3)
        obs_noua, _, _ = eval_gram_cc(rep_bond4[0], (I3, I3, I3, I3, I3))
        UA = UA_save
        rpf5_noua_drift = abs(obs_noua[6] - obs_b0_id[6])
        assert rpf5_noua_drift > mp.mpf(1) / mp.mpf(100)

    assert len(discrepancies) == 0, discrepancies

    cc_out = {
        "card": "AGY-C56-COUNTERCHECK",
        "empirical_inputs": "0 of 19",
        "verified_producer_sha256": actual_sha,
        "ast_firewall_countercheck": cc_ast,
        "ast_firewall_producer": prod_ast,
        "discrepancies_count": len(discrepancies),
        "disjoint_e1_alt_modulus_max_err": mp.nstr(max_e1_cc, 12),
        "disjoint_e1_unit_modulus_sc_max_dev": mp.nstr(max_sc_cc, 12),
        "disjoint_e2_pure_theta_3_over_5_err": mp.nstr(max_35_cc, 12),
        "disjoint_e2_sv1sq_1_over_5_err": mp.nstr(max_15_cc, 12),
        "disjoint_e2_y32_42_max_2_over_5_err": mp.nstr(max_25_cc, 12),
        "disjoint_e4_rk4_logradial_L2_diffs": {
            "omega": mp.nstr(diff_l2_om, 10),
            "i": mp.nstr(diff_l2_i, 10),
            "tau_gold": mp.nstr(diff_l2_tg, 10),
        },
        "disjoint_e5_expm_u3_5_max_err": mp.nstr(expm_haar_err, 12),
        "disjoint_e5_vs_producer_indep_L2_max_rel_diff": mp.nstr(max_b0_rel_diff, 10),
        "referee_planted_faults": {
            "RPF1_bad_rhoT_err": mp.nstr(rpf1_err, 8),
            "RPF2_bad_kap_rank1_ratio": mp.nstr(rpf2_ratio, 8),
            "RPF3_c0_nonfuchsian_im_tr": mp.nstr(rpf3_im_tr, 8),
            "RPF4_illegal_lr_overlap_drift": mp.nstr(rpf4_lr_drift, 8),
            "RPF5_no_UA_transport_ckm_drift": mp.nstr(rpf5_noua_drift, 8),
        },
        "all_referee_checks_passed": True,
    }
    cc_text = json.dumps(cc_out, indent=2, sort_keys=True) + "\n"
    CC_JSON.write_text(cc_text, encoding="utf-8")


if __name__ == "__main__":
    main()
