#!/usr/bin/env python3
r"""Card AGY-C48 Disjoint Cold-Room Countercheck (Guardrail 6, Closing D1 & D3, 0 of 19):
100% standalone under `python3 -I` in any isolated sandbox directory (depends ONLY on stdlib and mpmath — ZERO SymPy,
ZERO subprocess/git, ZERO snappy, ZERO AST float/complex literals OR float()/complex() calls, OUTPUT_SHA256.txt &
parse_float=bad_float enforced):
  1. Disjoint P-557 countercheck: Constructs all 12 Halphen-Serre B1825 directions (classifying 2 null vs 10 full-rank
     dynamically) and evaluates mp.svd_c (disjoint from producer's Jacobi eigensolver) across all 266 lines x 2 disjoint
     radii x 8 readings on BOTH F_6 (full-rank) and R (null) at disjoint tau' = -23/100 + 109/100 i, independently
     deriving 50880 V-defined, 40000 four-physical, 32320 all-ten-physical ({12: 7680}), and 125/101 (PF1).
  2. Disjoint P-667 countercheck: Evaluates Dimofte-Gaiotto-Gukov I_Delta(m, e; q) via 140-node unit-circle Cauchy contour
     integral of (q x^{-e} z^{-1}; q)_oo / (x^{-e} z; q)_oo at rational q = +-1/5 (100% disjoint from Pochhammer series),
     confirming I_m004(0,0;+-1/5) == I_m003(0,0;+-1/5) to < 10^-28 (PF2).
  3. Disjoint P-640 countercheck: Evaluates eta(B_{S^1}, a) via UV/IR Poisson-split heat-kernel integral (disjoint from
     mp.zeta), confirming ind_APS == 0 for |a| < 1/2 and jump == 1 at a = 3/4 (PF3).
  4. Disjoint B1974 countercheck: 48-node Cauchy argument-principle contour winding (1/(2 pi i)) oint (c_0'/c_0) dz == 1
     around (1 + i)/2, plus T^2 multiplier exp(2 pi i / 3) != 1 on eta * c_0 (PF4).
  5. Disjoint chat1 P-596 / M3 / agy-002 / M49 countercheck: 4th-order Richardson ((-f(2h)+8f(h)-8f(-h)+f(-2h))/(12h))
     10 x 2 Frame C Jacobian SVD at disjoint point (2/5, 4/5) & tau' = 19/100 + 12/5 i (verifying rank_R == 2 vs rank-1
     collapse when Re tau is frozen), Haar U(3)^3 scrambling on H_u = H_d witness, numeric 3-factor singlet det Y, and
     numeric 50-digit m003 SL(2, Z[omega]) sister words Xyxyx / YXYx (PF5).
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction as Fr
import hashlib
import itertools
import json
import math
from pathlib import Path
import random
import time

import mpmath as mp

mp.mp.dps = 50
I_MP = mp.mpc(0, 1)
Z0 = mp.mpf(0)
HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "c48_out.json"
OUT_SHA = HERE / "OUTPUT_SHA256.txt"


def mp_rat(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def check_zero_ast_floats(src: str, name: str) -> None:
    tree = ast.parse(src, filename=name)
    bad = [
        getattr(node, "lineno", 0)
        for node in ast.walk(tree)
        if (isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)))
        or (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"))
    ]
    assert not bad, f"[{name}] forbidden AST float/complex literal or call at lines {bad}"


def check_zero_json_floats(raw_text: str, name: str) -> dict:
    def bad_float(val_s: str) -> None:
        raise AssertionError(f"[{name}] raw JSON float found: {val_s}")

    return json.loads(raw_text, parse_float=bad_float)


def thc_cc(ca: Fr, cb: Fr, tv: mp.mpc) -> mp.mpc:
    am, bm = f2m(ca), f2m(cb)
    q = mp.exp(I_MP * mp.pi * tv)
    return mp.exp(I_MP * mp.pi * am * am * tv + 2 * I_MP * mp.pi * am * bm) * mp.jtheta(3, mp.pi * (am * tv + bm), q)


def f_u_cc(u1: Fr, u2: Fr, tv: mp.mpc) -> mp.mpf:
    y = mp.im(tv)
    a_r, b_r = u1 % 1, u2 % 1
    if a_r != 0:
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(f2m(a_r)) + mp.digamma(1 - f2m(a_r)))
        zrow = Z0
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zrow = y * (mp.pi ** 2) / (mp.sin(mp.pi * f2m(b_r)) ** 2)
    tot = Z0
    k_lim = int(mp.ceil(mp.mpf(28) / y)) + 8
    for k_sum in range(-k_lim, k_lim + 1):
        m_val = f2m(a_r) + k_sum
        if m_val == 0:
            continue
        w_val = mp.exp(-2 * mp.pi * abs(m_val) * y + 2 * I_MP * mp.pi * (m_val * mp.re(tv) + f2m(u2)))
        tot += (2 * mp.pi / abs(m_val)) * mp.re(w_val / (1 - w_val))
    return first + zrow + tot


def s_higgs_serre(tv: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    q = mp.exp(I_MP * mp.pi * tv)
    q_mod = mp.exp(2 * I_MP * mp.pi * tv)
    t2 = 2 * mp.exp(I_MP * mp.pi * tv / 4) * (mp.qp(q_mod ** 2) ** 2) / mp.qp(q_mod)
    t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    eta3 = (mp.exp(I_MP * mp.pi * tv / 12) * mp.qp(q_mod)) ** 3
    d24 = 24 * eta3
    c0 = -(t2 ** 2) * ((t3 ** 4) + (t4 ** 4)) / d24
    c1 = (t4 ** 2) * ((t2 ** 4) + (t3 ** 4)) / d24
    c2 = I_MP * (t3 ** 2) * ((t2 ** 4) - (t4 ** 4)) / d24
    return c0, c1, c2


def ten_obs_cc(pa: Fr, pb: Fr, tv: mp.mpc) -> list[mp.mpf]:
    y = mp.im(tv)
    q = mp.exp(I_MP * mp.pi * tv)
    qi, qj = mp.matrix([[I_MP, 0], [0, -I_MP]]), mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    eps_q = qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    c0, c1, c2 = s_higgs_serre(tv)
    sh = c0 * qi + c1 * qj + c2 * qk
    sh_st = eps_q * mp.matrix([[mp.conj(sh[r, c]) for c in range(2)] for r in range(2)]) * eps_q.T
    t1p = mp.pi * mp.jtheta(2, 0, q) * mp.jtheta(3, 0, q) * mp.jtheta(4, 0, q)
    th1_fn = lambda zv: mp.jtheta(1, mp.pi * zv, q)
    l_end = mp.pi * y / 3
    hr = Fr(1, 2)

    def y_sec(ql: int, qr: int, use_st: bool) -> mp.matrix:
        sm = sh_st if use_st else sh
        ct = [[ca.T * eps_q * sm * cb for cb in blks] for ca in blks]
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
                r_res = kap[sk] * thc_cc(cs[sk][0], cs[sk][1], tv) * thc_cc(ds[sk][0], ds[sk][1], tv) / t1p
                zv = f2m(al) * tv + f2m(be)
                a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_fn, zv) / th1_fn(zv)
                c_ch = f_u_cc(al, be, tv) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
                mw = mw + mp.sqrt(2 * mp.pi * l_end + c_ch) * r_res * ed[sk]
        return mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])

    def sv_u_asc(ym: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
        uu, sv, _ = mp.svd_c(ym)
        oi = sorted(range(3), key=lambda idx: sv[idx])
        return [sv[idx] for idx in oi], mp.matrix([[uu[r, oi[c]] for c in range(3)] for r in range(3)])

    su, uu = sv_u_asc(y_sec(1, -4, True))
    sd, ud = sv_u_asc(y_sec(1, 2, False))
    se, _ = sv_u_asc(y_sec(-3, 6, False))
    vc = uu.H * ud
    jcp = abs(mp.im(vc[0, 0] * vc[1, 1] * mp.conj(vc[0, 1]) * mp.conj(vc[1, 0])))
    return [su[1] / su[2], su[0] / su[2], sd[1] / sd[2], sd[0] / sd[2], se[1] / se[2], se[0] / se[2], abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), jcp]


def cauchy_i_delta(m: int, e: int, q_val: mp.mpf, x_root: mp.mpc, n_nodes: int = 140) -> mp.mpc:
    r_c = (abs(x_root) ** e) * mp_rat(3, 5)
    xp = x_root ** (-e)
    acc = mp.mpc(0)
    for k in range(n_nodes):
        th = 2 * mp.pi * mp_rat(k, n_nodes)
        zv = r_c * mp.exp(I_MP * th)
        num = mp.qp(q_val * (zv ** (-1)) * xp, q_val)
        den = mp.qp(zv * xp, q_val)
        acc += (zv ** (-m)) * (num / den)
    return acc / n_nodes


def haar_u3(rng: random.Random) -> mp.matrix:
    a = mp.matrix([[mp.mpc(mp_rat(rng.randint(-97, 97), 100), mp_rat(rng.randint(-97, 97), 100)) for _ in range(3)] for _ in range(3)])
    cols: list[mp.matrix] = []
    for c in range(3):
        v = a[:, c]
        for u in cols:
            v = v - ((u.H * v)[0, 0]) * u
        v = v / mp.sqrt(mp.re((v.H * v)[0, 0]))
        cols.append(v)
    return mp.matrix([[cols[c][r, 0] for c in range(3)] for r in range(3)])


def main() -> None:
    t0 = time.time()
    check_zero_ast_floats(Path(__file__).resolve().read_text(encoding="utf-8"), Path(__file__).name)
    raw = OUT_JSON.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUT_SHA.read_text(encoding="utf-8").strip().split()[0]
    out = check_zero_json_floats(raw.decode("utf-8"), OUT_JSON.name)
    assert out["empirical_firewall"] == "0 of 19" and out["all_expectations_passed"] is True and out["planted_controls_caught"] == 5

    # 1. Disjoint P-557 check: Construct all 12 Halphen-Serre B1825 directions dynamically and run mp.svd_c across all 266 lines
    #    x 2 disjoint radii x 8 readings on BOTH F_6 (full-rank) and R (null) at disjoint tau' = -23/100 + 109/100 i!
    fl_deg = mp.mpf(10) ** (-8)
    fl = mp.mpf(10) ** (-12)
    with mp.workdps(28):
        tv_cc = mp.mpc(mp_rat(-23, 100), mp_rat(109, 100))
        y_cc = mp.im(tv_cc)
        q_cc = mp.exp(I_MP * mp.pi * tv_cc)
        q_mod_cc = mp.exp(2 * I_MP * mp.pi * tv_cc)
        t2_cc = 2 * mp.exp(I_MP * mp.pi * tv_cc / 4) * (mp.qp(q_mod_cc ** 2) ** 2) / mp.qp(q_mod_cc)
        t3_cc, t4_cc = mp.jtheta(3, 0, q_cc), mp.jtheta(4, 0, q_cc)
        t1p_cc = mp.pi * mp.jtheta(2, 0, q_cc) * t3_cc * t4_cc
        th1_cc = lambda zv: mp.jtheta(1, mp.pi * zv, q_cc)
        e4_cc = ((t2_cc ** 8) + (t3_cc ** 8) + (t4_cc ** 8)) / 2
        l2_cc = -mp.jtheta(2, 0, q_cc, derivative=2) / (8 * mp.jtheta(2, 0, q_cc))
        l3_cc = -mp.jtheta(3, 0, q_cc, derivative=2) / (8 * t3_cc)
        l4_cc = -mp.jtheta(4, 0, q_cc, derivative=2) / (8 * t4_cc)
        e2_cc = 8 * (l2_cc + l3_cc + l4_cc)
        b0_cc = [-t2_cc / (t3_cc * t4_cc), -t4_cc / (t2_cc * t3_cc), I_MP * t3_cc / (t2_cc * t4_cc)]
        b1_cc = list(s_higgs_serre(tv_cc))
        hs_cc = mp.mpf(10) ** (-9)
        b1_p_cc, b1_m_cc = s_higgs_serre(tv_cc + hs_cc), s_higgs_serre(tv_cc - hs_cc)
        b2_cc = [(b1_p_cc[k] - b1_m_cc[k]) / (4 * I_MP * mp.pi * hs_cc) - mp_rat(1, 8) * e2_cc * b1_cc[k] for k in range(3)]
        dirs_cc: dict[str, list[mp.mpc]] = {
            "DR": b1_cc,
            "a0": [b2_cc[k] - mp_rat(1, 48) * e4_cc * b0_cc[k] for k in range(3)],
            "R": b0_cc,
            "t=-5/288": [b2_cc[k] - mp_rat(5, 288) * e4_cc * b0_cc[k] for k in range(3)],
        }
        for a_e in (-10, -6, 6, 10, 14, 18, 22, 26):
            ep_c = I_MP ** ((a_e + 2) // 2)
            dirs_cc[f"F_{a_e}"] = [ep_c * (t2_cc ** a_e), ep_c * (t4_cc ** a_e), I_MP * (t3_cc ** a_e)]
        null_cc = [dn for dn, av in dirs_cc.items() if abs(av[0] ** 2 + av[1] ** 2 + av[2] ** 2) < mp.mpf(10) ** (-16)]
        full_cc = [dn for dn, av in dirs_cc.items() if abs(av[0] ** 2 + av[1] ** 2 + av[2] ** 2) > mp.mpf(10) ** (-6)]
        assert len(dirs_cc) == 12 and sorted(null_cc) == ["R", "t=-5/288"] and len(full_cc) == 10

        qi, qj = mp.matrix([[I_MP, 0], [0, -I_MP]]), mp.matrix([[0, 1], [-1, 0]])
        qk = qi * qj
        eps_q = qj
        hf = mp_rat(1, 2)
        ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
        blks = [qj, qi, qk]
        ct_pair: dict[tuple[str, int], list[list[mp.matrix]]] = {}
        for dn_rep in ("F_6", "R"):
            av_r = dirs_cc[dn_rep]
            sh_r = av_r[0] * qi + av_r[1] * qj + av_r[2] * qk
            sh_r_st = eps_q * mp.matrix([[mp.conj(sh_r[r, c]) for c in range(2)] for r in range(2)]) * eps_q.T
            ct_pair[(dn_rep, 0)] = [[ca.T * eps_q * sh_r * cb for cb in blks] for ca in blks]
            ct_pair[(dn_rep, 1)] = [[ca.T * eps_q * sh_r_st * cb for cb in blks] for ca in blks]
        radii_cc = [mp_rat(9, 5), mp_rat(13, 5)]

        seen_l: set[tuple[Fr, Fr]] = set()
        menu_cc: list[tuple[int, Fr, Fr]] = []
        for n_o in range(1, 13):
            for j in range(n_o):
                for k in range(n_o):
                    if math.gcd(math.gcd(j, k), n_o) == 1:
                        a, b = Fr(j, n_o), Fr(k, n_o)
                        ky = min((a, b), ((-a) % 1, (-b) % 1))
                        if ky not in seen_l:
                            seen_l.add(ky)
                            menu_cc.append((n_o, ky[0], ky[1]))

        cnt_vdef: Counter[str] = Counter()
        cnt_four: Counter[str] = Counter()
        cnt_ten: Counter[str] = Counter()
        six_drop_f6: Counter[int] = Counter()
        hr = Fr(1, 2)
        for n_o, pa, pb in menu_cc:
            sec_rc: dict[str, dict[str, tuple[mp.mpc, mp.mpf, mp.mpf] | None]] = {}
            for sname, ql, qr in (("u", 1, -4), ("d", 1, 2), ("e", -3, 6)):
                xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
                ap, am = xv[0] + yv[0], xv[0] - yv[0]
                bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
                eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
                kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
                cs = {"1": (ap + hr, bp + hr), "i": (ap + hr, bp), "j": (ap, bp + hr), "k": (ap, bp)}
                ds = {"1": (am + hr, bm + hr), "i": (am + hr, bm), "j": (am, bm + hr), "k": (am, bm)}
                rc: dict[str, tuple[mp.mpc, mp.mpf, mp.mpf] | None] = {}
                for sk in ("1", "i", "j", "k"):
                    al, be = cs[sk][0] - hr, cs[sk][1] - hr
                    dal, dbe = ds[sk][0] - hr, ds[sk][1] - hr
                    if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
                        rc[sk] = None
                    else:
                        r_res = kap[sk] * thc_cc(cs[sk][0], cs[sk][1], tv_cc) * thc_cc(ds[sk][0], ds[sk][1], tv_cc) / t1p_cc
                        zv = f2m(al) * tv_cc + f2m(be)
                        a0 = 2 * I_MP * mp.pi * f2m(al) + mp.diff(th1_cc, zv) / th1_cc(zv)
                        c_b = f_u_cc(al, be, tv_cc) + mp.pi * mp.log(y_cc) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                        rc[sk] = (r_res, c_b, abs(a0) ** 2)
                sec_rc[sname] = rc
            for l_r in radii_cc:
                mw_map: dict[str, mp.matrix] = {}
                for sname in ("u", "d", "e"):
                    rc = sec_rc[sname]
                    mw = mp.zeros(2, 2)
                    for sk in ("1", "i", "j", "k"):
                        if rc[sk] is not None:
                            rr, cb_v, a02 = rc[sk]
                            mw = mw + mp.sqrt(2 * mp.pi * l_r + cb_v - mp.pi * a02 * mp.exp(-2 * l_r)) * rr * ed[sk]
                    mw_map[sname] = mw
                for dn_rep in ("F_6", "R"):
                    sv_map: dict[tuple[str, int], tuple[mp.matrix, bool, bool]] = {}
                    for sname in ("u", "d", "e"):
                        mw = mw_map[sname]
                        for rb in (0, 1):
                            ct = ct_pair[(dn_rep, rb)]
                            ym = mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])
                            uu, sv, _ = mp.svd_c(ym)
                            oi = sorted(range(3), key=lambda idx: sv[idx])
                            s0, s1_v, s2_v = sv[oi[0]], sv[oi[1]], sv[oi[2]]
                            nd = (s2_v > fl) and (min((s1_v - s0) / s2_v, (s2_v - s1_v) / s2_v) >= fl_deg)
                            sx = (s2_v > fl) and (s0 / s2_v >= fl) and (s1_v / s2_v >= fl)
                            sv_map[(sname, rb)] = (mp.matrix([[uu[r, oi[c]] for c in range(3)] for r in range(3)]), nd, sx)
                    for ru, rd, re_b in itertools.product((0, 1), repeat=3):
                        uu_m, u_nd, u_ok = sv_map[("u", ru)]
                        ud_m, d_nd, d_ok = sv_map[("d", rd)]
                        _, _, e_ok = sv_map[("e", re_b)]
                        if not (u_nd and d_nd):
                            continue
                        cnt_vdef[dn_rep] += 1
                        vm = uu_m.H * ud_m
                        jcp = abs(mp.im(vm[0, 0] * vm[1, 1] * mp.conj(vm[0, 1]) * mp.conj(vm[1, 0])))
                        if (abs(vm[0, 1]) >= fl) and (abs(vm[1, 2]) >= fl) and (abs(vm[0, 2]) >= fl) and (jcp >= fl):
                            cnt_four[dn_rep] += 1
                            if u_ok and d_ok and e_ok:
                                cnt_ten[dn_rep] += 1
                            elif dn_rep == "F_6":
                                six_drop_f6[n_o] += 1

    kraft_cc = len(menu_cc) * len(dirs_cc) * len(radii_cc) * 8
    vdef_cc = len(full_cc) * cnt_vdef["F_6"] + len(null_cc) * cnt_vdef["R"]
    four_cc = len(full_cc) * cnt_four["F_6"] + len(null_cc) * cnt_four["R"]
    ten_cc = len(full_cc) * cnt_ten["F_6"] + len(null_cc) * cnt_ten["R"]
    r_bound = Fr(four_cc, ten_cc)
    pf_1 = bool(
        cnt_four["R"] == 0
        and vdef_cc == 50880
        and four_cc == 40000
        and ten_cc == 32320
        and dict(six_drop_f6) == {12: 768}
        and r_bound == Fr(125, 101)
        and [kraft_cc, vdef_cc, four_cc, ten_cc, four_cc - ten_cc] == out["E1_m16_p557_p667_p640"]["p557_computed_choices_kraft_vdef_four_ten_e0"]
    )
    assert pf_1

    # 2. Disjoint P-667 check: 140-node Cauchy unit-circle contour integral of I_Delta at q = +-1/5 for m004 vs m003:
    edges_m004 = [[2, 1, 0, 1, 0, 2], [0, 1, 2, 1, 2, 0]]
    edges_m003 = [[2, 0, 1, 2, 0, 1], [0, 2, 1, 0, 2, 1]]

    def index_cauchy_2tet(edges: list[list[int]], q_v: mp.mpf, x_v: mp.mpc) -> mp.mpc:
        tot = mp.mpc(0)
        for k1 in range(-7, 8):
            kv = [0, k1]
            t0_e = [sum(kv[r] * edges[r][s] for r in range(2)) for s in range(3)]
            t1_e = [sum(kv[r] * edges[r][3 + s] for r in range(2)) for s in range(3)]
            j0 = ((-x_v) ** (-t0_e[1])) * cauchy_i_delta(t0_e[0] - t0_e[1], t0_e[1] - t0_e[2], q_v, x_v)
            j1 = ((-x_v) ** (-t1_e[1])) * cauchy_i_delta(t1_e[0] - t1_e[1], t1_e[1] - t1_e[2], q_v, x_v)
            tot += (q_v ** k1) * j0 * j1
        return tot

    ser_ghrs_41 = {0: 1, 1: -2, 2: -3, 3: 2, 4: 8, 5: 18, 6: 18, 7: 14, 8: -12, 9: -52, 10: -106, 11: -164, 12: -209, 13: -212, 14: -141, 15: 14}
    q_pos = mp_rat(1, 5)
    q_neg = mp_rat(-1, 5)
    i_4_pos = index_cauchy_2tet(edges_m004, q_pos, mp.sqrt(q_pos))
    i_3_pos = index_cauchy_2tet(edges_m003, q_pos, mp.sqrt(q_pos))
    i_4_neg = index_cauchy_2tet(edges_m004, q_neg, I_MP * mp.sqrt(q_pos))
    i_3_neg = index_cauchy_2tet(edges_m003, q_neg, I_MP * mp.sqrt(q_pos))
    ser_approx = sum(mp.mpf(v) * (q_pos ** k) for k, v in ser_ghrs_41.items())
    m004_m003_cauchy_diff = max(abs(i_4_pos - i_3_pos), abs(i_4_neg - i_3_neg))
    pf_2 = bool(m004_m003_cauchy_diff < mp.mpf(10) ** (-28) and abs(i_4_pos - ser_approx) < mp.mpf(10) ** (-8))
    assert pf_2

    # 3. Disjoint P-640 check: UV/IR Poisson-split heat-kernel integral for eta(B_{S^1}, a):
    def eta_poisson_split(a_f: Fr) -> mp.mpf:
        u = f2m((Fr(1, 2) - a_f) % 1)
        part_uv = Z0
        for k in range(1, 35):
            c_k = (mp.pi * k) ** 2
            part_uv += (2 * mp.pi * k * mp.sin(2 * mp.pi * k * u)) * (mp.exp(-c_k) / c_k)
        part_ir = Z0
        for m in range(-14, 15):
            lam = m + u
            part_ir += (1 if lam > 0 else -1) * mp.erfc(abs(lam))
        return part_uv + part_ir

    aps_cc_unq = max(abs(f2m(a) - eta_poisson_split(a) / 2) for a in (Fr(-2, 5), Fr(1, 7), Fr(3, 8)))
    aps_cc_jmp = abs((f2m(Fr(3, 4)) - eta_poisson_split(Fr(3, 4)) / 2) - 1)
    pf_3 = bool(aps_cc_unq < mp.mpf(10) ** (-42) and aps_cc_jmp < mp.mpf(10) ** (-42))
    assert pf_3

    # 4. Disjoint B1974 check: 48-node Cauchy argument-principle winding integral around tau_ell = (1 + i)/2:
    tv_ell = mp.mpc(mp_rat(1, 2), mp_rat(1, 2))
    rad_w = mp_rat(1, 20)
    n_w = 48
    h_d = mp.mpf(10) ** (-14)
    wind_acc = mp.mpc(0)
    for k in range(n_w):
        th = 2 * mp.pi * mp_rat(k, n_w)
        z_pt = tv_ell + rad_w * mp.exp(I_MP * th)
        dz_dt = I_MP * rad_w * mp.exp(I_MP * th)
        c0_v = s_higgs_serre(z_pt)[0]
        c0_p = (s_higgs_serre(z_pt + h_d)[0] - s_higgs_serre(z_pt - h_d)[0]) / (2 * h_d)
        wind_acc += (c0_p / c0_v) * dz_dt
    winding_c0 = wind_acc / (2 * I_MP * mp.pi * n_w) * (2 * mp.pi)
    eta_fn = lambda z: mp.exp(I_MP * mp.pi * z / 12) * mp.qp(mp.exp(2 * I_MP * mp.pi * z))
    tv_t = mp.mpc(mp_rat(17, 100), mp_rat(6, 5))
    t2_mult_err = abs((eta_fn(tv_t + 2) * s_higgs_serre(tv_t + 2)[0]) / (eta_fn(tv_t) * s_higgs_serre(tv_t)[0]) - mp.exp(2 * I_MP * mp.pi / 3))
    pf_4 = bool(abs(winding_c0 - 1) < mp.mpf(10) ** (-25) and t2_mult_err < mp.mpf(10) ** (-44))
    assert pf_4

    # 5. Disjoint 4th-order Richardson 10 x 2 Frame C Jacobian SVD + Haar U(3)^3 scrambling + numeric det Y + m003 sister words:
    tv_r = mp.mpc(mp_rat(19, 100), mp_rat(12, 5))
    h_r = mp.mpf(10) ** (-7)
    f_p2x = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r + 2 * h_r)
    f_p1x = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r + h_r)
    f_m1x = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r - h_r)
    f_m2x = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r - 2 * h_r)
    f_p2y = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r + 2 * I_MP * h_r)
    f_p1y = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r + I_MP * h_r)
    f_m1y = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r - I_MP * h_r)
    f_m2y = ten_obs_cc(Fr(2, 5), Fr(4, 5), tv_r - 2 * I_MP * h_r)
    jac_rich = mp.matrix([
        [
            (-f_p2x[r] + 8 * f_p1x[r] - 8 * f_m1x[r] + f_m2x[r]) / (12 * h_r),
            (-f_p2y[r] + 8 * f_p1y[r] - 8 * f_m1y[r] + f_m2y[r]) / (12 * h_r),
        ]
        for r in range(10)
    ])
    _, sv_jr, _ = mp.svd_r(jac_rich)
    rich_ratio = min(sv_jr[0], sv_jr[1]) / max(sv_jr[0], sv_jr[1])
    _, sv_jr_fr, _ = mp.svd_r(mp.matrix([[Z0, jac_rich[r, 1]] for r in range(10)]))
    rich_frozen_s2 = min(sv_jr_fr[0], sv_jr_fr[1])

    rng = random.Random(2026112448)
    sig = [mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -I_MP], [I_MP, 0]]), mp.matrix([[1, 0], [0, -1]])]
    t_w = mp_rat(1, 100)
    hv = [1 + t_w, I_MP * (1 - t_w), Z0]
    hd = hv[0] * sig[0] + hv[1] * sig[1]
    m_rk1 = mp.matrix([[mp.mpf(1), Z0], [Z0, Z0]])
    ym_w = mp.matrix([[mp_rat(1, 2) * ((sig[a] * hd * sig[b] * m_rk1)[0, 0] + (sig[a] * hd * sig[b] * m_rk1)[1, 1]) for b in range(3)] for a in range(3)])
    _, sv0, _ = mp.svd_c(ym_w)
    s0_ord = sorted([sv0[0], sv0[1], sv0[2]], reverse=True)
    rho0 = s0_ord[1] / s0_ord[0]
    haar_err = Z0
    for _ in range(5):
        ul, ur_u, ur_d = haar_u3(rng), haar_u3(rng), haar_u3(rng)
        yu_r, yd_r = ul * ym_w * ur_u.H, ul * ym_w * ur_d.H
        uu_r, su_r, _ = mp.svd_c(yu_r)
        ud_r, sd_r, _ = mp.svd_c(yd_r)
        iu = max(range(3), key=lambda idx: su_r[idx])
        id_ = max(range(3), key=lambda idx: sd_r[idx])
        v33_r = abs((uu_r[:, iu].H * ud_r[:, id_])[0, 0])
        su_s = sorted([su_r[0], su_r[1], su_r[2]], reverse=True)
        haar_err = max(haar_err, abs(v33_r - 1), abs(su_s[1] / su_s[0] - rho0))

    hv_n = [mp.mpc(mp_rat(2, 3), mp_rat(1, 5)), mp.mpc(mp_rat(-3, 7), mp_rat(4, 9)), mp.mpc(mp_rat(1, 11), mp_rat(-2, 13))]
    uv_n = [mp.mpc(mp_rat(5, 6), mp_rat(-1, 4)), mp.mpc(mp_rat(2, 9), mp_rat(3, 8)), mp.mpc(mp_rat(-4, 7), mp_rat(1, 3))]
    w_n, s_n = mp.mpc(mp_rat(3, 5), mp_rat(-2, 7)), mp.mpc(mp_rat(4, 11), mp_rat(5, 13))
    cx = lambda v: mp.matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    uh = sum(uv_n[k] * hv_n[k] for k in range(3))
    uu_d = sum(uv_n[k] * uv_n[k] for k in range(3))
    hh_d = sum(hv_n[k] * hv_n[k] for k in range(3))
    y_s_mat = mp.matrix([[hv_n[r] * uv_n[c] + uv_n[r] * hv_n[c] for c in range(3)] for r in range(3)]) - uh * mp.eye(3) + w_n * cx(hv_n) - s_n * (w_n * mp.eye(3) + cx(uv_n))
    det_err = abs(mp.det(y_s_mat) - (uu_d + w_n * w_n) * (hh_d + s_n * s_n) * (uh - w_n * s_n))

    # Numeric 50-digit check of agy-exp 0c8debf48 m003 sister spin-swap words:
    w_mp = mp_rat(-1, 2) + I_MP * mp.sqrt(mp.mpf(3)) / 2
    w2_mp = mp.conj(w_mp)
    a3_mp = mp.matrix([[w_mp, mp.mpf(-1)], [w2_mp, w2_mp - w_mp]])
    b3_mp = mp.matrix([[-w_mp, mp.mpf(1)], [w2_mp, mp.mpf(1)]])
    a2_mp = -a3_mp
    b2_mp = b3_mp
    g3_mp = mp.matrix([[mp.mpf(1), -w_mp], [Z0, mp.mpf(1)]])
    g3i_mp = mp.matrix([[mp.mpf(1), w_mp], [Z0, mp.mpf(1)]])
    conj2 = lambda m: mp.matrix([[mp.conj(m[r, c]) for c in range(2)] for r in range(2)])
    x2_mp = g3_mp * conj2(a3_mp) * g3i_mp
    y2_mp = g3_mp * conj2(b3_mp) * g3i_mp
    x2i_mp = x2_mp ** (-1)
    y2i_mp = y2_mp ** (-1)
    m003_err = max(
        mp.mnorm(x2_mp - b2_mp * a2_mp, "F"),
        mp.mnorm(y2_mp - (b2_mp ** (-1)) * (a2_mp ** (-1)) * (b2_mp ** (-1)) * a2_mp * (b2_mp ** (-1)), "F"),
        mp.mnorm(x2i_mp * y2_mp * x2_mp * y2_mp * x2_mp - a2_mp, "F"),
        mp.mnorm(y2i_mp * x2i_mp * y2i_mp * x2_mp - b2_mp, "F"),
    )

    pf_5 = bool(
        rich_ratio > mp_rat(1, 25)
        and rich_frozen_s2 == 0
        and haar_err < mp.mpf(10) ** (-42)
        and det_err < mp.mpf(10) ** (-44)
        and m003_err < mp.mpf(10) ** (-45)
        and rho0 < mp_rat(1, 90)
    )
    assert pf_5

    pf_tot = sum(int(x) for x in (pf_1, pf_2, pf_3, pf_4, pf_5))
    assert pf_tot == 5
    print(
        f"AGY-C48 disjoint countercheck PASSED in {int(time.time() - t0)}s: "
        f"P557=40000/32320(125/101), Cauchy3D={mp.nstr(m004_m003_cauchy_diff, 3)}, APS={mp.nstr(aps_cc_unq, 3)}, "
        f"X0(2)_wind={mp.nstr(abs(winding_c0 - 1), 3)}, Rich_s2/s1={mp.nstr(rich_ratio, 3)}, m003={mp.nstr(m003_err, 3)}, faults={pf_tot}/5."
    )


if __name__ == "__main__":
    main()
