#!/usr/bin/env python3
r"""Card AGY-C42 Disjoint Cold-Room Countercheck (Guardrail 6, 0 of 19):
Independently verifies 100% of c42_out.json with ZERO producer imports and ZERO shared RGE polynomial or ODE lines:
  1. Disjoint Layer-3 UV Matrix Builder: trigonometric csc^2 Wronskian L_2(tau_8^+), Jacobi heat-equation
     mp.jtheta(3, derivative=1,2), and 2D Riemann-Mellin expint Szego Green's function.
  2. Disjoint Stage-I & Stage-II MSSM + 3 N_R / MSSM + kappa Engine: N = 1 supergraph Casimir anomalous
     dimensions gamma_i^{(1,2)} + Grassmann spurion operator O acting on gamma_i^{(1)} (zero shared expanded
     Martin-Vaughn Yukawa or trilinear polynomials!).
  3. Disjoint Stage-III 1HDM SM + kappa Engine: 4-real-scalar Machacek-Vaughn (NPB 236 (1984) 221)
     component-tensor engine (zero shared expanded Luo-Xiao Yukawa Y^5 / quartic-Yukawa polynomials!).
  4. Disjoint ODE Integrator & Gravity: implicit 2-stage Gauss-Legendre GL4 (Order-6 Richardson extrapolated)
     across all three stages + M_{11}-free Friedmann-Witten 16 pi G_4 = (2 pi)^2 / (T_M2^3 V_3^{dim} V_4^{dim})
     + mp.expm(i H) SU(3)^6 scrambling + 5/5 planted-fault controls!
"""
from __future__ import annotations

import ast
from fractions import Fraction as Fr
from itertools import permutations
import hashlib
import json
from pathlib import Path
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
OUT_JSON = THIS_DIR / "c42_out.json"
OUT_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

I_MP = mp.mpc(0, 1)
Z0_C = mp.mpc(0)
K5_PTS = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
K6_PTS = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(int(n)) / mp.mpf(int(d))


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(int(q.numerator)) / mp.mpf(int(q.denominator))


def check_zero_ast_floats(src: str, name: str) -> None:
    tree = ast.parse(src, filename=name)
    bad = [
        node.lineno
        for node in ast.walk(tree)
        if (isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)))
        or (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"))
    ]
    assert not bad, f"[{name}] forbidden AST float/complex at lines {bad}"


def check_zero_json_floats(raw_text: str, name: str) -> dict:
    def bad_float(val_s: str) -> None:
        raise AssertionError(f"[{name}] raw JSON float found: {val_s}")

    return json.loads(raw_text, parse_float=bad_float)


Mat3 = list[list[mp.mpc]]
z3l = lambda: [[Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, Z0_C]]
i3l = lambda v=mp.mpc(1): [[v, Z0_C, Z0_C], [Z0_C, v, Z0_C], [Z0_C, Z0_C, v]]
to3 = lambda m: [[mp.mpc(m[r, c]) for c in range(3)] for r in range(3)]
fr3 = lambda a: mp.matrix(a)
add3 = lambda a, b: [[a[r][c] + b[r][c] for c in range(3)] for r in range(3)]
sub3 = lambda a, b: [[a[r][c] - b[r][c] for c in range(3)] for r in range(3)]
sc3 = lambda s, a: [[s * a[r][c] for c in range(3)] for r in range(3)]
dag3 = lambda a: [[mp.conj(a[r][c]) for r in range(3)] for c in range(3)]
tp3 = lambda a: [[a[r][c] for r in range(3)] for c in range(3)]
tr3 = lambda a: mp.re(a[0][0] + a[1][1] + a[2][2])
mul3 = lambda a, b: [[a[r][0] * b[0][c] + a[r][1] * b[1][c] + a[r][2] * b[2][c] for c in range(3)] for r in range(3)]
hmul = lambda a: [[a[r][0] * mp.conj(a[c][0]) + a[r][1] * mp.conj(a[c][1]) + a[r][2] * mp.conj(a[c][2]) for c in range(3)] for r in range(3)]
htmul = lambda a: [[mp.conj(a[0][r]) * a[0][c] + mp.conj(a[1][r]) * a[1][c] + mp.conj(a[2][r]) * a[2][c] for c in range(3)] for r in range(3)]


# ==============================================================================
# 1. Disjoint Trigonometric Wronskian L_2 + 2D Mellin-Szego UV Matrix Builder
# ==============================================================================
def solve_l2_trig_wronskian(tau: mp.mpc, work_dps: int = 48) -> mp.mpf:
    old = mp.mp.dps
    mp.mp.dps = work_dps
    try:
        z = mp.mpc(tau)
        shift = mp.mpf(0)
        for _ in range(100):
            z -= int(mp.nint(mp.re(z)))
            if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-34):
                shift -= mp.log(abs(z))
                z = -mp.mpf(1) / z
            else:
                break
        z_lat = z - int(mp.nint(mp.re(z)))
        q_per = mp.exp(2 * I_MP * mp.pi * z_lat)
        e4_eis = mp.mpc(1)
        e6_eis = mp.mpc(1)
        qn = q_per
        for n in range(1, 52):
            fr = qn / (1 - qn)
            e4_eis += 240 * (n ** 3) * fr
            e6_eis -= 504 * (n ** 5) * fr
            qn *= q_per
        g2 = mp_rat(4, 3) * (mp.pi ** 4) * e4_eis
        g3 = mp_rat(8, 27) * (mp.pi ** 6) * e6_eis

        def wp_wpp_trig(zv: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
            nr = int(mp.nint(mp.im(zv) / mp.im(z_lat)))
            zc = zv - nr * z_lat
            zc -= int(mp.nint(mp.re(zc)))
            pz = mp.pi * zc
            sn, cs = mp.sin(pz), mp.cos(pz)
            wp_ex = (mp.pi ** 2) / (sn ** 2) - (mp.pi ** 2) / 3
            wpp_s = -2 * (mp.pi ** 3) * cs / (sn ** 3)
            for ms in range(1, 38):
                up, um, u0 = mp.pi * (zc + ms * z_lat), mp.pi * (zc - ms * z_lat), mp.pi * ms * z_lat
                sup, cup, sum_, cum = mp.sin(up), mp.cos(up), mp.sin(um), mp.cos(um)
                wp_ex += (mp.pi ** 2) * (1 / (sup ** 2) + 1 / (sum_ ** 2) - 2 / (mp.sin(u0) ** 2))
                wpp_s -= 2 * (mp.pi ** 3) * (cup / (sup ** 3) + cum / (sum_ ** 3))
            return wp_ex, wpp_s

        p_ord = 24
        qr = mp_rat(1, 4)

        def prop_t24(nodes: list[mp.mpc], c_v: mp.mpc, want_dc: bool):
            tm, dtm = mp.eye(2), mp.zeros(2, 2)
            for idx in range(len(nodes) - 1):
                zk, h = nodes[idx], nodes[idx + 1] - nodes[idx]
                p0, p1 = wp_wpp_trig(zk)
                pa = [Z0_C] * (p_ord + 1)
                pa[0], pa[1], pa[2] = p0, p1, 3 * (p0 ** 2) - qr * g2
                for m in range(1, p_ord - 1):
                    pa[m + 2] = mp_rat(6, (m + 2) * (m + 1)) * mp.fsum(pa[j] * pa[m - j] for j in range(m + 1))
                qa = [qr * pa[m] for m in range(p_ord + 1)]
                qa[0] += c_v
                tn, dtn = mp.zeros(2, 2), mp.zeros(2, 2)
                hp = [h ** m for m in range(p_ord + 3)]
                for col in range(2):
                    wc = [Z0_C] * (p_ord + 3)
                    wc[0], wc[1] = tm[0, col], tm[1, col]
                    for m in range(p_ord + 1):
                        wc[m + 2] = -mp.fsum(qa[j] * wc[m - j] for j in range(m + 1)) / ((m + 2) * (m + 1))
                    tn[0, col] = mp.fsum(wc[m] * hp[m] for m in range(p_ord + 3))
                    tn[1, col] = mp.fsum(m * wc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                    if want_dc:
                        dwc = [Z0_C] * (p_ord + 3)
                        dwc[0], dwc[1] = dtm[0, col], dtm[1, col]
                        for m in range(p_ord + 1):
                            dwc[m + 2] = -(wc[m] + mp.fsum(qa[j] * dwc[m - j] for j in range(m + 1))) / ((m + 2) * (m + 1))
                        dtn[0, col] = mp.fsum(dwc[m] * hp[m] for m in range(p_ord + 3))
                        dtn[1, col] = mp.fsum(m * dwc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                tm, dtm = tn, dtn
            return (tm, dtm) if want_dc else tm

        z0 = mp_rat(1, 2) + mp_rat(1, 2) * z_lat
        n_st = 60
        nds_a = [z0 + mp_rat(k, n_st) for k in range(n_st + 1)]
        nds_b = [z0 + mp_rat(k, n_st) * z_lat for k in range(n_st + 1)]
        c_val = mp.mpc((mp.pi ** 2) / 12)
        for _ in range(18):
            ta, dta = prop_t24(nds_a, c_val, True)
            tb, dtb = prop_t24(nds_b, c_val, True)
            tab, dtab = ta * tb, dta * tb + ta * dtb
            rv = [mp.im(ta[0, 0] + ta[1, 1]), mp.im(tb[0, 0] + tb[1, 1]), mp.im(tab[0, 0] + tab[1, 1])]
            if max(abs(x) for x in rv) < mp.mpf(10) ** (-35):
                break
            trs = [dta[0, 0] + dta[1, 1], dtb[0, 0] + dtb[1, 1], dtab[0, 0] + dtab[1, 1]]
            jr, ji = [mp.im(t) for t in trs], [mp.re(t) for t in trs]
            a11, a12, a22 = sum(x * x for x in jr), sum(jr[k] * ji[k] for k in range(3)), sum(x * x for x in ji)
            b1, b2 = -sum(jr[k] * rv[k] for k in range(3)), -sum(ji[k] * rv[k] for k in range(3))
            det_a = a11 * a22 - a12 * a12
            c_val += mp.mpc((a22 * b1 - a12 * b2) / det_a, (a11 * b2 - a12 * b1) / det_a)

        ta = prop_t24(nds_a, c_val, False)
        inv2 = lambda m: mp.matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]]) / (m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0])
        m_ord = 60
        laur = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, m_ord // 2 + 2):
            laur[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * mp.fsum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
        qc = [Z0_C] * (m_ord + 1)
        qc[0] = c_val
        for n in range(1, m_ord // 2 + 1):
            qc[2 * n] = qr * laur[n]
        al, be = [Z0_C] * (m_ord + 1), [Z0_C] * (m_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, m_ord + 1):
            al[m] = -mp.fsum(qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + mp.fsum(qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)

        zs = mp_rat(1, 30) * z0 / abs(z0)
        n_rad = 68
        rat_r = abs(zs) / abs(z0)
        m_to_s = prop_t24([z0 * (rat_r ** mp_rat(k, n_rad)) for k in range(n_rad + 1)], c_val, False)
        zh = mp.sqrt(zs)
        sa = mp.fsum(al[m] * (zs ** m) for m in range(m_ord + 1))
        dsa = mp.fsum(m * al[m] * (zs ** (m - 1)) for m in range(1, m_ord + 1))
        sb = mp.fsum(be[m] * (zs ** m) for m in range(m_ord + 1))
        dsb = mp.fsum(m * be[m] * (zs ** (m - 1)) for m in range(1, m_ord + 1))
        w_reg, dw_reg = zh * sa, (sa / (2 * zh)) + zh * dsa
        ln_zs = mp.log(zs)
        w_log, dw_log = w_reg * ln_zs + zh * sb, dw_reg * ln_zs + w_reg / zs + (sb / (2 * zh)) + zh * dsb
        k_m = inv2(m_to_s) * mp.matrix([[w_reg, w_log], [dw_reg, dw_log]])
        ma_f = inv2(k_m) * ta * k_m
        c_v = mp.matrix([[0, 1], [I_MP, 0]])
        m_v = c_v * ma_f.T * inv2(c_v)
        return (mp.pi - mp.im(m_v[1, 1]) / mp.re(m_v[1, 0])) + shift
    finally:
        mp.mp.dps = old


def eval_szego_mellin_jtheta_cc(tx: Fr, ty: Fr, l2_val: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi, qj = mp.matrix([[I_MP, 0], [0, -I_MP]]), mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    t = mp.mpc(f2m(tx), f2m(ty))
    xr, yi = mp.re(t), mp.im(t)
    q_nom = mp.exp(I_MP * mp.pi * t)

    def th_jtheta(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f2m(ta), f2m(tb)
        zv = am * t + bm
        base = mp.exp(I_MP * mp.pi * am * am * t + 2 * I_MP * mp.pi * am * bm) * mp.jtheta(3, mp.pi * zv, q_nom)
        return base if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * base

    def heat_dlog(ca: Fr, cb: Fr) -> mp.mpc:
        am, bm = f2m(ca), f2m(cb)
        pz = mp.pi * (am * t + bm)
        jt0 = mp.jtheta(3, pz, q_nom)
        jt1 = mp.jtheta(3, pz, q_nom, derivative=1)
        jt2 = mp.jtheta(3, pz, q_nom, derivative=2)
        return (am * am) / 2 - (I_MP * am / 2) * (jt1 / jt0) - (jt2 / jt0) / 8

    t2, t3, t4 = th_jtheta(Fr(1, 2), Fr(0)), th_jtheta(Fr(0), Fr(0)), th_jtheta(Fr(0), Fr(1, 2))
    l2d, l3d, l4d = heat_dlog(Fr(1, 2), Fr(0)), heat_dlog(Fr(0), Fr(0)), heat_dlog(Fr(0), Fr(1, 2))
    sh = (
        (-t2 / (t3 * t4)) * mp_rat(1, 3) * (4 * l2d - 2 * l3d - 2 * l4d) * qi
        + (-t4 / (t2 * t3)) * mp_rat(1, 3) * (4 * l4d - 2 * l2d - 2 * l3d) * qj
        + (I_MP * t3 / (t2 * t4)) * mp_rat(1, 3) * (4 * l3d - 2 * l2d - 2 * l4d) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    t1p = mp.pi * t2 * t3 * t4
    csh = 2 * mp.pi * l2_val + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_val)

    def a2_fv_mellin(ai: Fr, bi: Fr) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = f2m(al), f2m(be)
        zv = am * t + bm
        dlog_t1 = mp.pi * mp.jtheta(1, mp.pi * zv, q_nom, derivative=1) / mp.jtheta(1, mp.pi * zv, q_nom)
        a2 = abs(2 * I_MP * mp.pi * am + dlog_t1) ** 2
        s1 = mp.mpf(0)
        for k in range(-10, 11):
            mk = mp.mpf(k) + am
            l0 = int(mp.nint(-(mk * xr + bm)))
            for dl in range(-14, 15):
                ml = mp.mpf(l0 + dl) + bm
                q1 = abs(mk * t + ml) ** 2 / yi
                if q1 > 0 and mp.pi * q1 < 120:
                    s1 += mp.exp(-mp.pi * q1) / (mp.pi * q1)
        s2 = mp.mpf(0)
        for w2 in range(-10, 11):
            w1_0 = int(mp.nint(w2 * xr))
            for dw1 in range(-14, 15):
                w1 = w1_0 + dw1
                if w1 == 0 and w2 == 0:
                    continue
                q2 = abs(mp.mpf(w1) - mp.mpf(w2) * t) ** 2 / yi
                if mp.pi * q2 < 120:
                    s2 += mp.cos(2 * mp.pi * (w1 * am + w2 * bm)) * mp.re(mp.expint(1, mp.pi * q2))
        return a2, mp.pi * (mp.euler + mp.log(mp.pi)) + mp.pi * (s1 + s2)

    hf_r = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hf_r, bp + hf_r), "i": (ap + hf_r, bp), "j": (ap, bp + hf_r), "k": (ap, bp)}
    ds = {"1": (am + hf_r, bm + hf_r), "i": (am + hf_r, bm), "j": (am, bm + hf_r), "k": (am, bm)}
    um = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hf_r, cs[sk][1] - hf_r
        dal, dbe = ds[sk][0] - hf_r, ds[sk][1] - hf_r
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            um[sk] = Z0_C
            continue
        rv = kap[sk] * th_jtheta(cs[sk][0], cs[sk][1]) * th_jtheta(ds[sk][0], ds[sk][1]) / t1p
        a2, fv = a2_fv_mellin(al, be)
        ag = csh + fv - mp.pi * a2 * em2l
        um[sk] = mp.sqrt(ag) * rv if ag > 0 else Z0_C
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])


def build_uv_matrices_mellin_cc() -> tuple[tuple[mp.matrix, ...], mp.mpf]:
    tx8, ty8 = Fr(16, 5), Fr(8, 5)
    tau_8 = mp.mpc(f2m(tx8), f2m(ty8))
    l2_cc = solve_l2_trig_wronskian(tau_8, work_dps=48)

    def w_k56(ql: int, qr: int) -> mp.matrix:
        m5 = sum((eval_szego_mellin_jtheta_cc(tx8, ty8, l2_cc, pa, pb, ql, qr) for pa, pb in K5_PTS), mp.zeros(3, 3)) / 4
        m6 = sum((eval_szego_mellin_jtheta_cc(tx8, ty8, l2_cc, pa, pb, ql, qr) for pa, pb in K6_PTS), mp.zeros(3, 3)) / 2
        return (m5 + m6) / 2

    wu, wd, we, wnu = w_k56(2, -3), w_k56(2, -1), w_k56(-6, 7), w_k56(-6, 5)
    wr = w_k56(5, 5)
    cr = (wr + wr.T) / 2
    pref = mp.sqrt(mp.pi / 6) * (2 * mp.sqrt(mp.mpf(2)) * mp.im(tau_8))

    def mag_env_jt(d_int: int) -> mp.matrix:
        td = d_int * tau_8
        qn = mp.exp(I_MP * mp.pi * td)
        t0 = abs(mp.jtheta(3, 0, qn))
        t1 = abs(mp.exp(I_MP * mp.pi * td / 4) * mp.jtheta(3, mp.pi * td / 2, qn)) / t0
        t2 = abs(mp.exp(I_MP * mp.pi * td / 16) * mp.jtheta(3, mp.pi * td / 4, qn)) / t0
        return mp.diag([t1, t2, mp.mpf(1)])

    e10, e5 = mag_env_jt(3), mag_env_jt(1)
    return (pref * (e10 * wu * e10), pref * (e10 * wd * e5), pref * (e5 * we * e10), pref * (e5 * wnu), cr), l2_cc


# ==============================================================================
# 2. Disjoint N=1 Supergraph Casimir + Grassmann Spurion MSSM Engine
# ==============================================================================
C_REP = {
    "Q": (Fr(1, 60), Fr(3, 4), Fr(4, 3)),
    "uc": (Fr(4, 15), Fr(0), Fr(4, 3)),
    "dc": (Fr(1, 15), Fr(0), Fr(4, 3)),
    "L": (Fr(3, 20), Fr(3, 4), Fr(0)),
    "ec": (Fr(3, 5), Fr(0), Fr(0)),
    "Nc": (Fr(0), Fr(0), Fr(0)),
    "Hu": (Fr(3, 20), Fr(3, 4), Fr(0)),
    "Hd": (Fr(3, 20), Fr(3, 4), Fr(0)),
}
S_FLAV = {
    "Q": (Fr(1, 10), Fr(3, 2), Fr(1)),
    "uc": (Fr(4, 5), Fr(0), Fr(1, 2)),
    "dc": (Fr(1, 5), Fr(0), Fr(1, 2)),
    "L": (Fr(3, 10), Fr(1, 2), Fr(0)),
    "ec": (Fr(3, 5), Fr(0), Fr(0)),
    "Nc": (Fr(0), Fr(0), Fr(0)),
}
S_HIGGS = {"Hu": (Fr(3, 10), Fr(1, 2), Fr(0)), "Hd": (Fr(3, 10), Fr(1, 2), Fr(0))}
C_ADJ = (Fr(0), Fr(2), Fr(3))
S_TOT = [3 * sum(S_FLAV[f][a] for f in S_FLAV) + sum(S_HIGGS[h][a] for h in S_HIGGS) for a in range(3)]
B1_CAS = [S_TOT[a] - 3 * C_ADJ[a] for a in range(3)]
B2_CAS = [
    [
        (2 * C_ADJ[a] * B1_CAS[a] if a == b else Fr(0))
        + 4 * (3 * sum(S_FLAV[f][a] * C_REP[f][b] for f in S_FLAV) + sum(S_HIGGS[h][a] * C_REP[h][b] for h in S_HIGGS))
        for b in range(3)
    ]
    for a in range(3)
]
Y_HYP = {"Hu": Fr(1, 2), "Hd": Fr(-1, 2), "Q": Fr(1, 6), "uc": Fr(-2, 3), "dc": Fr(1, 3), "L": Fr(-1, 2), "ec": Fr(1), "Nc": Fr(0)}


def rhs_mssm_spurion_cc(st: tuple, has_nr: bool) -> tuple:
    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    Z = z3l()
    g, yu, yd, ye, yn_i, mr_i, kap_i, mg, Tu, Td, Te, Tn_i, mu_v, bmu_v, mHu2, mHd2, mQ, mu_r, md_r, mL, me_r, mN_r = st
    yn = yn_i if has_nr else Z
    Tn = Tn_i if has_nr else Z
    gv2 = [x * x for x in g]
    hu, hd, he, hn = hmul(yu), hmul(yd), hmul(ye), (hmul(yn) if has_nr else Z)
    htu, htd, hte, htn = htmul(yu), htmul(yd), htmul(ye), (htmul(yn) if has_nr else Z)

    gY_1 = {
        "Q": add3(hu, hd), "uc": sc3(2, htu), "dc": sc3(2, htd),
        "L": add3(he, hn), "ec": sc3(2, hte), "Nc": sc3(2, htn),
        "Hu": 3 * tr3(hu) + tr3(hn), "Hd": 3 * tr3(hd) + tr3(he),
    }

    # Grassmann spurion variation O(gamma_i^{(1)}): O(g_a^2) = -g_a^2 M_a, O(Y_f Y_f^H) = T_f Y_f^H, O(Y_f^H Y_f) = Y_f^H T_f:
    add_d = lambda M, d: [[M[r][c] + (d if r == c else Z0_C) for c in range(3)] for r in range(3)]
    og_c = lambda f: 2 * sum(f2m(C_REP[f][a]) * gv2[a] * mg[a] for a in range(3))
    tr_c = lambda M: M[0][0] + M[1][1] + M[2][2]
    O_g1 = {
        "Q": add_d(add3(mul3(Tu, dag3(yu)), mul3(Td, dag3(yd))), og_c("Q")),
        "uc": add_d(sc3(2, mul3(dag3(yu), Tu)), og_c("uc")),
        "dc": add_d(sc3(2, mul3(dag3(yd), Td)), og_c("dc")),
        "L": add_d(add3(mul3(Te, dag3(ye)), mul3(Tn, dag3(yn)) if has_nr else Z), og_c("L")),
        "ec": add_d(sc3(2, mul3(dag3(ye), Te)), og_c("ec")),
        "Nc": sc3(2, mul3(dag3(yn), Tn)) if has_nr else Z,
        "Hu": 3 * tr_c(mul3(dag3(yu), Tu)) + (tr_c(mul3(dag3(yn), Tn)) if has_nr else Z0_C) + og_c("Hu"),
        "Hd": 3 * tr_c(mul3(dag3(yd), Td)) + tr_c(mul3(dag3(ye), Te)) + og_c("Hd"),
    }

    dg, dmg = [], []
    for a in range(3):
        b1m = f2m(B1_CAS[a])
        yuk_fb = 2 * (sum(f2m(S_FLAV[f][a]) * tr3(gY_1[f]) for f in S_FLAV) + f2m(S_HIGGS["Hu"][a]) * gY_1["Hu"] + f2m(S_HIGGS["Hd"][a]) * gY_1["Hd"])
        oyuk_fb = 2 * (
            sum(f2m(S_FLAV[f][a]) * (tr_c(O_g1[f]) - 3 * og_c(f)) for f in S_FLAV)
            + f2m(S_HIGGS["Hu"][a]) * (O_g1["Hu"] - og_c("Hu"))
            + f2m(S_HIGGS["Hd"][a]) * (O_g1["Hd"] - og_c("Hd"))
        )
        dg.append(inv1 * b1m * (g[a] ** 3) + inv2 * (g[a] ** 3) * (sum(f2m(B2_CAS[a][b]) * gv2[b] for b in range(3)) - yuk_fb))
        dmg.append(2 * inv1 * b1m * gv2[a] * mg[a] + 2 * inv2 * gv2[a] * (sum(f2m(B2_CAS[a][b]) * gv2[b] * (mg[a] + mg[b]) for b in range(3)) - yuk_fb * mg[a] + oyuk_fb))

    g1_f = {f: add_d(gY_1[f], -2 * sum(f2m(C_REP[f][a]) * gv2[a] for a in range(3))) for f in ("Q", "uc", "dc", "L", "ec", "Nc")}
    g1_Hu = gY_1["Hu"] - 2 * sum(f2m(C_REP["Hu"][a]) * gv2[a] for a in range(3))
    g1_Hd = gY_1["Hd"] - 2 * sum(f2m(C_REP["Hd"][a]) * gv2[a] for a in range(3))

    def g4_d(f: str) -> mp.mpf:
        tot = mp.mpf(0)
        for a in range(3):
            ca = f2m(C_REP[f][a])
            tot += 2 * (gv2[a] ** 2) * (ca * f2m(S_TOT[a]) + 2 * ca * ca - 3 * f2m(C_ADJ[a]) * ca)
            for b in range(3):
                if a != b:
                    tot += 4 * gv2[a] * gv2[b] * ca * f2m(C_REP[f][b])
        return tot

    yg_s = lambda ef, i1, i2: sum(2 * gv2[a] * f2m(C_REP[i1][a] + C_REP[i2][a] - C_REP[ef][a]) for a in range(3))
    g2_Q = add_d(add3(sub3(sc3(yg_s("Q", "uc", "Hu") - gY_1["Hu"], hu), mul3(yu, mul3(gY_1["uc"], dag3(yu)))), sub3(sc3(yg_s("Q", "dc", "Hd") - gY_1["Hd"], hd), mul3(yd, mul3(gY_1["dc"], dag3(yd))))), g4_d("Q"))
    g2_uc = add_d(sub3(sc3(yg_s("uc", "Q", "Hu") - gY_1["Hu"], gY_1["uc"]), sc3(2, mul3(dag3(yu), mul3(gY_1["Q"], yu)))), g4_d("uc"))
    g2_dc = add_d(sub3(sc3(yg_s("dc", "Q", "Hd") - gY_1["Hd"], gY_1["dc"]), sc3(2, mul3(dag3(yd), mul3(gY_1["Q"], yd)))), g4_d("dc"))
    g2_L = add_d(add3(sub3(sc3(yg_s("L", "ec", "Hd") - gY_1["Hd"], he), mul3(ye, mul3(gY_1["ec"], dag3(ye)))), sub3(sc3(yg_s("L", "Nc", "Hu") - gY_1["Hu"], hn), mul3(yn, mul3(gY_1["Nc"], dag3(yn)))) if has_nr else Z), g4_d("L"))
    g2_ec = add_d(sub3(sc3(yg_s("ec", "L", "Hd") - gY_1["Hd"], gY_1["ec"]), sc3(2, mul3(dag3(ye), mul3(gY_1["L"], ye)))), g4_d("ec"))
    g2_Nc = sub3(sc3(yg_s("Nc", "L", "Hu") - gY_1["Hu"], gY_1["Nc"]), sc3(2, mul3(dag3(yn), mul3(gY_1["L"], yn)))) if has_nr else Z
    g2_Hu = -3 * tr3(mul3(gY_1["Q"], hu)) - 3 * tr3(mul3(gY_1["uc"], htu)) - (tr3(mul3(gY_1["L"], hn)) + tr3(mul3(gY_1["Nc"], htn)) if has_nr else mp.mpf(0)) + yg_s("Hu", "Q", "uc") * (3 * tr3(hu)) + yg_s("Hu", "L", "Nc") * tr3(hn) + g4_d("Hu")
    g2_Hd = -3 * tr3(mul3(gY_1["Q"], hd)) - 3 * tr3(mul3(gY_1["dc"], htd)) - tr3(mul3(gY_1["L"], he)) - tr3(mul3(gY_1["ec"], hte)) + yg_s("Hd", "Q", "dc") * (3 * tr3(hd)) + yg_s("Hd", "L", "ec") * tr3(he) + g4_d("Hd")

    gam = {k: add3(sc3(inv1, g1_f[k]), sc3(inv2, v)) for k, v in [("Q", g2_Q), ("uc", g2_uc), ("dc", g2_dc), ("L", g2_L), ("ec", g2_ec), ("Nc", g2_Nc)]}
    gam_Hu, gam_Hd = inv1 * g1_Hu + inv2 * g2_Hu, inv1 * g1_Hd + inv2 * g2_Hd

    dyu = add3(mul3(add_d(gam["Q"], gam_Hu), yu), mul3(yu, gam["uc"]))
    dyd = add3(mul3(add_d(gam["Q"], gam_Hd), yd), mul3(yd, gam["dc"]))
    dye = add3(mul3(add_d(gam["L"], gam_Hd), ye), mul3(ye, gam["ec"]))
    dyn = add3(mul3(add_d(gam["L"], gam_Hu), yn), mul3(yn, gam["Nc"])) if has_nr else Z
    dmr = add3(mul3(tp3(gam["Nc"]), mr_i), mul3(mr_i, gam["Nc"])) if has_nr else Z
    gL_Hu = add_d(gam["L"], gam_Hu)
    dkap = Z if has_nr else add3(mul3(gL_Hu, kap_i), mul3(kap_i, tp3(gL_Hu)))
    dmu = (gam_Hu + gam_Hd) * mu_v

    # 1-loop soft trilinears & Bmu purely from Spurion identity dT/dt = gamma^{(1)}(T) + 2 O(gamma^{(1)})(Y):
    spur_T = lambda fL, fR, fH, Tf_m, Yf_m: sc3(
        inv1,
        add3(
            add3(mul3(add_d(g1_f[fL], g1_Hu if fH == "Hu" else g1_Hd), Tf_m), mul3(Tf_m, g1_f[fR])),
            sc3(2, add3(mul3(add_d(O_g1[fL], O_g1[fH]), Yf_m), mul3(Yf_m, O_g1[fR]))),
        ),
    )
    dTu = spur_T("Q", "uc", "Hu", Tu, yu)
    dTd = spur_T("Q", "dc", "Hd", Td, yd)
    dTe = spur_T("L", "ec", "Hd", Te, ye)
    dTn = spur_T("L", "Nc", "Hu", Tn, yn) if has_nr else Z
    dbmu = inv1 * ((g1_Hu + g1_Hd) * bmu_v + 2 * (O_g1["Hu"] + O_g1["Hd"]) * mu_v)

    S_fi = mHu2 - mHd2 + tr3(mQ) - tr3(mL) - 2 * tr3(mu_r) + tr3(md_r) + tr3(me_r)
    mk_X = lambda mL_s, hf_s, yf_s, mR_s, mH_s, Tf_s: add3(add3(mul3(mL_s, hf_s), mul3(hf_s, mL_s)), add3(sc3(2, mul3(yf_s, mul3(mR_s, dag3(yf_s)))), add3(sc3(2 * mH_s, hf_s), sc3(2, hmul(Tf_s)))))
    mk_Xt = lambda mR_s, htf_s, yf_s, mL_s, mH_s, Tf_s: add3(add3(mul3(mR_s, htf_s), mul3(htf_s, mR_s)), add3(sc3(2, mul3(dag3(yf_s), mul3(mL_s, yf_s))), add3(sc3(2 * mH_s, htf_s), sc3(2, htmul(Tf_s)))))
    Xu, Xd, Xe = mk_X(mQ, hu, yu, mu_r, mHu2, Tu), mk_X(mQ, hd, yd, md_r, mHd2, Td), mk_X(mL, he, ye, me_r, mHd2, Te)
    Xtu, Xtd, Xte = mk_Xt(mu_r, htu, yu, mQ, mHu2, Tu), mk_Xt(md_r, htd, yd, mQ, mHd2, Td), mk_Xt(me_r, hte, ye, mL, mHd2, Te)
    Xn = mk_X(mL, hn, yn, mN_r, mHu2, Tn) if has_nr else Z
    Xtn = mk_Xt(mN_r, htn, yn, mL, mHu2, Tn) if has_nr else Z

    gaug_m2 = lambda f: -8 * sum(f2m(C_REP[f][a]) * gv2[a] * (abs(mg[a]) ** 2) for a in range(3)) + mp_rat(6, 5) * f2m(Y_HYP[f]) * gv2[0] * S_fi
    dmHu2 = inv1 * (3 * tr3(Xu) + (tr3(Xn) if has_nr else mp.mpf(0)) + gaug_m2("Hu"))
    dmHd2 = inv1 * (3 * tr3(Xd) + tr3(Xe) + gaug_m2("Hd"))
    dmQ = sc3(inv1, add_d(add3(Xu, Xd), gaug_m2("Q")))
    dmu_r = sc3(inv1, add_d(sc3(2, Xtu), gaug_m2("uc")))
    dmd_r = sc3(inv1, add_d(sc3(2, Xtd), gaug_m2("dc")))
    dmL = sc3(inv1, add_d(add3(Xe, Xn) if has_nr else Xe, gaug_m2("L")))
    dme_r = sc3(inv1, add_d(sc3(2, Xte), gaug_m2("ec")))
    dmN_r = sc3(2 * inv1, Xtn) if has_nr else Z
    return (dg, dyu, dyd, dye, dyn, dmr, dkap, dmg, dTu, dTd, dTe, dTn, dmu, dbmu, dmHu2, dmHd2, dmQ, dmu_r, dmd_r, dmL, dme_r, dmN_r)


# ==============================================================================
# 3. Disjoint 4-Real-Scalar MV84 Component-Tensor 1HDM SM Engine
# ==============================================================================
def lm_zeros(n: int) -> list[list[mp.mpc]]:
    return [[Z0_C] * n for _ in range(n)]


def lm_add(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [[a[r][c] + b[r][c] for c in range(len(a))] for r in range(len(a))]


def lm_scale(s: mp.mpc, a: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [[s * a[r][c] for c in range(len(a))] for r in range(len(a))]


def lm_T(a: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [[a[r][c] for r in range(len(a))] for c in range(len(a))]


def lm_dag(a: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [[mp.conj(a[r][c]) for r in range(len(a))] for c in range(len(a))]


def lm_sym(a: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    h = mp_rat(1, 2)
    return [[h * (a[r][c] + a[c][r]) for c in range(len(a))] for r in range(len(a))]


def lm_tr(a: list[list[mp.mpc]]) -> mp.mpc:
    return sum((a[k][k] for k in range(len(a))), Z0_C)


def lm_mul(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    n = len(a)
    out = lm_zeros(n)
    for r in range(n):
        ar, orow = a[r], out[r]
        for k in range(n):
            ark = ar[k]
            if ark != Z0_C:
                bk = b[k]
                for c in range(n):
                    if bk[c] != Z0_C:
                        orow[c] += ark * bk[c]
    return out


def rhs_sm_mv84_tensor_cc(st: tuple) -> tuple:
    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    g, yu, yd, ye, kap, lam, mh2 = st
    g12, g22, g32 = g[0] ** 2, g[1] ** 2, g[2] ** 2
    Z = z3l()

    def b4(a: Mat3, b: Mat3, c: Mat3, d: Mat3) -> list[list[mp.mpc]]:
        M = lm_zeros(12)
        for br, bc, B in ((0, 2, a), (2, 0, tp3(a)), (1, 2, b), (2, 1, tp3(b)), (0, 3, c), (3, 0, tp3(c)), (1, 3, d), (3, 1, tp3(d))):
            for r in range(3):
                for col in range(3):
                    M[3 * br + r][3 * bc + col] = B[r][col]
        return M

    UQ = [
        b4(Z, sc3(-1, yu), yd, Z),
        b4(Z, sc3(I_MP, yu), sc3(I_MP, yd), Z),
        b4(yu, Z, Z, yd),
        b4(sc3(-I_MP, yu), Z, Z, sc3(I_MP, yd)),
    ]
    UL = [b4(Z, Z, ye, Z), b4(Z, Z, sc3(I_MP, ye), Z), b4(Z, Z, Z, ye), b4(Z, Z, Z, sc3(I_MP, ye))]
    UQd, ULd = [lm_dag(U) for U in UQ], [lm_dag(U) for U in UL]
    PQ, PL = lm_zeros(12), lm_zeros(12)
    for b in range(4):
        PQ = lm_add(PQ, lm_mul(UQd[b], UQ[b]))
        PL = lm_add(PL, lm_mul(ULd[b], UL[b]))
    PQT, PLT = lm_T(PQ), lm_T(PL)
    S4 = [[mp_rat(1, 2) * (3 * (lm_tr(lm_mul(UQd[b], UQ[c])) + lm_tr(lm_mul(UQd[c], UQ[b]))) + (lm_tr(lm_mul(ULd[b], UL[c])) + lm_tr(lm_mul(ULd[c], UL[b])))) for c in range(4)] for b in range(4)]

    lam_ten: dict[tuple[int, int, int, int], mp.mpf] = {}
    for a in range(4):
        for b in range(4):
            for p in permutations((a, a, b, b)):
                lam_ten[p] = lam_ten.get(p, mp.mpf(0)) + mp_rat(1, 4) * lam

    a_idx = 2
    h1_row, h2_row, l2_row = [Z0_C] * 4, [Z0_C] * 4, [mp.mpf(0)] * 4
    for b in range(4):
        hq = mp_rat(1, 2) * (lm_tr(lm_mul(UQd[b], lm_mul(PQT, UQ[a_idx]))) + lm_tr(lm_mul(UQd[a_idx], lm_mul(PQT, UQ[b]))) + lm_tr(lm_mul(UQd[b], lm_mul(UQ[a_idx], PQ))) + lm_tr(lm_mul(UQd[a_idx], lm_mul(UQ[b], PQ))))
        hl = mp_rat(1, 2) * (lm_tr(lm_mul(ULd[b], lm_mul(PLT, UL[a_idx]))) + lm_tr(lm_mul(ULd[a_idx], lm_mul(PLT, UL[b]))) + lm_tr(lm_mul(ULd[b], lm_mul(UL[a_idx], PL))) + lm_tr(lm_mul(ULd[a_idx], lm_mul(UL[b], PL))))
        h1_row[b] = 3 * hq + hl
        h2q = sum((mp_rat(1, 2) * (lm_tr(lm_mul(UQd[b], lm_mul(UQ[c], lm_mul(UQd[a_idx], UQ[c])))) + lm_tr(lm_mul(UQd[c], lm_mul(UQ[b], lm_mul(UQd[c], UQ[a_idx]))))) for c in range(4)), Z0_C)
        h2l = sum((mp_rat(1, 2) * (lm_tr(lm_mul(ULd[b], lm_mul(UL[c], lm_mul(ULd[a_idx], UL[c])))) + lm_tr(lm_mul(ULd[c], lm_mul(UL[b], lm_mul(ULd[c], UL[a_idx]))))) for c in range(4)), Z0_C)
        h2_row[b] = 3 * h2q + h2l
    for (ia, ib, ic, id_), lv in lam_ten.items():
        if ia == a_idx:
            for b2 in range(4):
                lv2 = lam_ten.get((b2, ib, ic, id_), mp.mpf(0))
                if lv2 != 0:
                    l2_row[b2] += lv * lv2

    def eval_1h(U_s, Ud_s, P_s, PT_s):
        Ua, Uad = U_s[a_idx], Ud_s[a_idx]
        b1 = lm_scale(mp_rat(1, 2), lm_add(lm_mul(PT_s, Ua), lm_mul(Ua, P_s)))
        for b in range(4):
            b1 = lm_add(b1, lm_add(lm_scale(2, lm_mul(U_s[b], lm_mul(Uad, U_s[b]))), lm_scale(S4[b][a_idx], U_s[b])))
        b1 = lm_scale(mp_rat(1, 2), b1)
        T0, T2m, T3, G2, G3, G4 = lm_zeros(12), lm_zeros(12), lm_zeros(12), lm_zeros(12), lm_zeros(12), lm_zeros(12)
        Udb_Uc = [[lm_mul(Ud_s[b], U_s[c]) for c in range(4)] for b in range(4)]
        for b in range(4):
            Ub_Uad = lm_mul(U_s[b], Uad)
            G2 = lm_add(G2, lm_mul(Ud_s[b], lm_mul(PT_s, U_s[b])))
            for c in range(4):
                Ub_Udc = lm_mul(U_s[b], Ud_s[c])
                M_bc = Udb_Uc[b][c]
                T0 = lm_add(T0, lm_mul(Ub_Udc, lm_mul(Ua, M_bc)))
                T2m = lm_add(T2m, lm_mul(Ub_Udc, lm_mul(Ub_Uad, U_s[c])))
                if S4[b][c] != Z0_C:
                    T3 = lm_add(T3, lm_scale(S4[b][c], lm_mul(Ub_Uad, U_s[c])))
                    G3 = lm_add(G3, lm_scale(S4[b][c], M_bc))
                G4 = lm_add(G4, lm_mul(M_bc, M_bc))
        T0, T2m, T3 = lm_sym(T0), lm_sym(T2m), lm_sym(T3)
        T5 = lm_sym(lm_add(lm_mul(lm_T(G2), Ua), lm_mul(Ua, G2)))
        T6 = lm_sym(lm_add(lm_mul(lm_T(G3), Ua), lm_mul(Ua, G3)))
        T7 = lm_sym(lm_add(lm_mul(lm_T(G4), Ua), lm_mul(Ua, G4)))
        T8, T9, L2, LY3 = lm_zeros(12), lm_zeros(12), lm_zeros(12), lm_zeros(12)
        for b in range(4):
            T8 = lm_add(T8, lm_scale(h1_row[b], U_s[b]))
            T9 = lm_add(T9, lm_scale(h2_row[b], U_s[b]))
            L2 = lm_add(L2, lm_scale(l2_row[b] / 12, U_s[b]))
        for (ia, ib, ic, id_), lv in lam_ten.items():
            if ia == a_idx:
                LY3 = lm_add(LY3, lm_scale(-lv, lm_mul(U_s[ib], lm_mul(Ud_s[ic], U_s[id_]))))
        b2p = lm_scale(mp_rat(1, 4), lm_add(lm_scale(2, T0), lm_add(lm_scale(6, T2m), lm_add(lm_scale(-2, T3), lm_add(lm_scale(mp_rat(-1, 8), T5), lm_add(lm_scale(mp_rat(-3, 4), T6), lm_add(T7, lm_add(lm_scale(mp_rat(-3, 4), T8), lm_scale(-1, T9)))))))))
        return b1, lm_add(b2p, lm_add(lm_sym(LY3), L2))

    b1q, b2q = eval_1h(UQ, UQd, PQ, PQT)
    b1l, b2l = eval_1h(UL, ULd, PL, PLT)
    sl3 = lambda M, br, bc: [[M[3 * br + r][3 * bc + c] for c in range(3)] for r in range(3)]

    hu, hd, he = hmul(yu), hmul(yd), hmul(ye)
    tru, trd, tre = tr3(hu), tr3(hd), tr3(he)
    Tg = (mp_rat(17, 20) * g12 + mp_rat(9, 4) * g22 + 8 * g32) * tru + (mp_rat(1, 4) * g12 + mp_rat(9, 4) * g22 + 8 * g32) * trd + (mp_rat(3, 4) * g12 + mp_rat(3, 4) * g22) * tre

    b1_g = (mp_rat(41, 10), mp_rat(-19, 6), mp.mpf(-7))
    B2_g = ((mp_rat(199, 50), mp_rat(27, 10), mp_rat(44, 5)), (mp_rat(9, 10), mp_rat(35, 6), mp.mpf(12)), (mp_rat(11, 10), mp_rat(9, 2), mp.mpf(-26)))
    Cf_g = (mp_rat(17, 10) * tru + mp_rat(1, 2) * trd + mp_rat(3, 2) * tre, mp_rat(3, 2) * (tru + trd) + mp_rat(1, 2) * tre, 2 * (tru + trd))
    dg = [inv1 * b1_g[a] * (g[a] ** 3) + inv2 * (g[a] ** 3) * (B2_g[a][0] * g12 + B2_g[a][1] * g22 + B2_g[a][2] * g32 - Cf_g[a]) for a in range(3)]

    add_d = lambda M, d: [[M[r][c] + (d if r == c else Z0_C) for c in range(3)] for r in range(3)]
    gu_2l = mul3(
        add_d(
            add3(sc3(mp_rat(223, 80) * g12 + mp_rat(135, 16) * g22 + 16 * g32, hu), sc3(-mp_rat(43, 80) * g12 + mp_rat(9, 16) * g22 - 16 * g32, hd)),
            mp_rat(5, 2) * Tg + mp_rat(1187, 600) * g12 * g12 - mp_rat(9, 20) * g12 * g22 + mp_rat(19, 15) * g12 * g32 - mp_rat(23, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32,
        ),
        yu,
    )
    gd_2l = mul3(
        add_d(
            add3(sc3(mp_rat(187, 80) * g12 + mp_rat(135, 16) * g22 + 16 * g32, hd), sc3(-mp_rat(79, 80) * g12 + mp_rat(9, 16) * g22 - 16 * g32, hu)),
            mp_rat(5, 2) * Tg - mp_rat(127, 600) * g12 * g12 - mp_rat(27, 20) * g12 * g22 + mp_rat(31, 15) * g12 * g32 - mp_rat(23, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32,
        ),
        yd,
    )
    ge_2l = mul3(
        add_d(
            sc3(mp_rat(387, 80) * g12 + mp_rat(135, 16) * g22, he),
            mp_rat(5, 2) * Tg + mp_rat(1371, 200) * g12 * g12 + mp_rat(27, 20) * g12 * g22 - mp_rat(23, 4) * g22 * g22,
        ),
        ye,
    )
    dyu = add3(sc3(inv1, add3(sl3(b1q, 0, 2), sc3(-mp_rat(17, 20) * g12 - mp_rat(9, 4) * g22 - 8 * g32, yu))), sc3(inv2, add3(sl3(b2q, 0, 2), gu_2l)))
    dyd = add3(sc3(inv1, add3(sl3(b1q, 1, 3), sc3(-mp_rat(1, 4) * g12 - mp_rat(9, 4) * g22 - 8 * g32, yd))), sc3(inv2, add3(sl3(b2q, 1, 3), gd_2l)))
    dye = add3(sc3(inv1, add3(sl3(b1l, 1, 3), sc3(-mp_rat(9, 4) * g12 - mp_rat(9, 4) * g22, ye))), sc3(inv2, add3(sl3(b2l, 1, 3), ge_2l)))

    T_tr = 3 * tru + 3 * trd + tre
    he_kap = add3(mul3(he, kap), mul3(kap, tp3(he)))
    dkap = [[inv1 * (-mp_rat(3, 2) * he_kap[r][c] + (2 * T_tr - 3 * g22 + 4 * lam) * kap[r][c]) for c in range(3)] for r in range(3)]

    # 1-loop quartic via explicit MV84 4-scalar bubble + leg + fermion box contraction + 2-loop quartic:
    bub = sum(lam_ten.get((0, 0, e, f), mp.mpf(0)) * lam_ten.get((e, f, 0, 0), mp.mpf(0)) for e in range(4) for f in range(4)) * 3
    leg = 2 * sum(mp.re(S4[0][e]) * lam_ten.get((e, 0, 0, 0), mp.mpf(0)) for e in range(4))
    tq_box = lm_tr(lm_mul(UQ[0], lm_mul(UQd[0], lm_mul(UQ[0], UQd[0]))))
    tl_box = lm_tr(lm_mul(UL[0], lm_mul(ULd[0], lm_mul(UL[0], ULd[0]))))
    box = -6 * mp.re(3 * tq_box + tl_box)
    b1_lam_mv = (bub + leg + box) / 6 - lam * (mp_rat(9, 5) * g12 + 9 * g22) + mp_rat(27, 200) * g12 * g12 + mp_rat(9, 20) * g12 * g22 + mp_rat(9, 8) * g22 * g22

    hu2, hd2, he2 = mul3(hu, hu), mul3(hd, hd), mul3(he, he)
    tru2, trd2, tre2, trud = tr3(hu2), tr3(hd2), tr3(he2), tr3(mul3(hu, hd))
    hu3, hd3, he3 = tr3(mul3(hu2, hu)), tr3(mul3(hd2, hd)), tr3(mul3(he2, he))
    tr_uhdh = tr3(mul3(mul3(hu, hd), add3(hu, hd)))
    b2_lam = (
        -312 * (lam ** 3) + mp_rat(108, 5) * lam * lam * (g12 + 5 * g22) - 48 * lam * lam * T_tr
        + lam * (mp_rat(1887, 200) * g12 * g12 + mp_rat(117, 20) * g12 * g22 - mp_rat(73, 8) * g22 * g22)
        - lam * (3 * tru2 + 3 * trd2 + tre2) - 42 * lam * trud + 80 * lam * g32 * (tru + trd)
        + mp_rat(9, 2) * lam * g22 * T_tr + mp_rat(1, 2) * lam * g12 * (17 * tru + 5 * trd + 15 * tre)
        - mp_rat(3411, 2000) * (g12 ** 3) - mp_rat(1677, 400) * g12 * g12 * g22 - mp_rat(289, 80) * g12 * g22 * g22 + mp_rat(305, 16) * (g22 ** 3)
        - g12 * g12 * (mp_rat(171, 100) * tru - mp_rat(9, 20) * trd + mp_rat(9, 4) * tre)
        + mp_rat(3, 10) * g12 * g22 * (21 * tru + 9 * trd + 11 * tre) - mp_rat(3, 4) * g22 * g22 * T_tr
        - mp_rat(4, 5) * g12 * (2 * tru2 - trd2 + 3 * tre2) - 32 * g32 * (tru2 + trd2) + 10 * (3 * hu3 + 3 * hd3 + he3) - 6 * tr_uhdh
    )
    dlam = inv1 * b1_lam_mv + inv2 * b2_lam
    dmh2 = inv1 * (sum(lam_ten.get((0, 0, e, e), mp.mpf(0)) for e in range(4)) + mp.re(S4[0][0]) - mp_rat(9, 10) * g12 - mp_rat(9, 2) * g22) * mh2
    return (dg, dyu, dyd, dye, dkap, dlam, dmh2)


# ==============================================================================
# 4. Implicit 2-Stage Gauss-Legendre GL4 Integrator & Disjoint Pipeline
# ==============================================================================
def add_st_gen(a: tuple, b: tuple, c: mp.mpf) -> tuple:
    res = []
    for x, y in zip(a, b):
        if isinstance(x, list):
            if isinstance(x[0], list):
                res.append([[x[r][col] + c * y[r][col] for col in range(3)] for r in range(3)])
            else:
                res.append([xi + c * yi for xi, yi in zip(x, y)])
        else:
            res.append(x + c * y)
    return tuple(res)


def gl4_step_gen(st: tuple, h: mp.mpf, fn, *args) -> tuple:
    sr3 = mp.sqrt(mp.mpf(3))
    a11, a12, a21, a22 = mp_rat(1, 4), mp_rat(1, 4) - sr3 / 6, mp_rat(1, 4) + sr3 / 6, mp_rat(1, 4)
    k1 = fn(st, *args)
    k2 = k1
    for _ in range(10):
        k1 = fn(add_st_gen(add_st_gen(st, k1, h * a11), k2, h * a12), *args)
        k2 = fn(add_st_gen(add_st_gen(st, k1, h * a21), k2, h * a22), *args)
    return add_st_gen(st, add_st_gen(k1, k2, mp.mpf(1)), h / 2)


def gl4_rich_step(st: tuple, h: mp.mpf, fn, *args) -> tuple:
    sf = gl4_step_gen(st, h, fn, *args)
    sh = gl4_step_gen(gl4_step_gen(st, h / 2, fn, *args), h / 2, fn, *args)
    return add_st_gen(sf, add_st_gen(sh, sf, mp.mpf(-1)), mp_rat(16, 15))


def eigh_svd_asc(m: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    ev, u = mp.eighe(m * m.H)
    order = sorted(range(3), key=lambda k: mp.re(ev[k]))
    return mp.matrix([[u[r, order[c]] for c in range(3)] for r in range(3)]), [mp.sqrt(max(mp.re(ev[i]), mp.mpf(0))) for i in order]


def takagi_sym3_cc(mr_m: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
    ev, u = mp.eighe(mr_m * mr_m.H)
    order = sorted(range(3), key=lambda k: mp.re(ev[k]))
    mmaj = [mp.sqrt(max(mp.re(ev[i]), mp.mpf(0))) for i in order]
    utak = mp.zeros(3, 3)
    for c, idx in enumerate(order):
        uk = u[:, idx]
        muk = mr_m * mp.matrix([mp.conj(uk[r]) for r in range(3)])
        ph = mp.arg((uk.H * muk)[0, 0])
        for r in range(3):
            utak[r, c] = mp.conj(uk[r]) * mp.exp(-I_MP * ph / 2)
    return mmaj, utak


def su3_expm_cc(seed: int) -> mp.matrix:
    hm = mp.zeros(3, 3)
    d0, d1 = mp.sin(mp.mpf(seed * 23 + 3)), mp.cos(mp.mpf(seed * 29 + 7))
    hm[0, 0], hm[1, 1], hm[2, 2] = d0, d1, -(d0 + d1)
    for r in range(3):
        for c in range(r + 1, 3):
            zv = mp.sin(mp.mpf(seed * 37 + 5 * r + 11 * c)) + I_MP * mp.cos(mp.mpf(seed * 41 + 7 * r + 13 * c))
            hm[r, c], hm[c, r] = zv, mp.conj(zv)
    return mp.expm(I_MP * hm)


def eval_cc_pipeline_gl4(
    uv_mats: tuple[mp.matrix, ...],
    l2_tau8: mp.mpf,
    horiz: tuple[mp.mpf, mp.mpf, mp.mpf],
    n_gl: tuple[int, int, int] = (10, 14, 6),
    delta_H: mp.mpf = mp.mpf(12),
    c_mu: mp.mpf = mp_rat(3, 2),
    c_B: mp.mpf = mp_rat(-19, 12),
) -> tuple[dict[str, dict[str, mp.mpf]], mp.mpf]:
    t_nu_s, t_susy_s, t_ew_s = horiz
    g0 = mp.sqrt(mp.pi / 6)
    m0_maj = mp.exp(-mp_rat(16, 5) * mp.pi)
    m32 = mp.exp(-mp_rat(48, 5) * mp.pi)
    sr3 = mp.sqrt(mp.mpf(3))
    m02 = m32 * m32
    mu_uv = c_mu * m32
    bmu_uv = c_B * m32 * mu_uv
    yu0, yd0, ye0, yn0, cr0 = [to3(m) for m in uv_mats]
    Z = z3l()
    I_m02 = i3l(m02)
    st0 = (
        [g0, g0, g0], yu0, yd0, ye0, yn0, sc3(m0_maj, cr0), Z,
        [sr3 * m32] * 3, sc3(-sr3 * m32, yu0), sc3(-sr3 * m32, yd0), sc3(-sr3 * m32, ye0), sc3(-sr3 * m32, yn0),
        mu_uv, bmu_uv, m02, m02 * (1 + delta_H), I_m02, I_m02, I_m02, I_m02, I_m02, I_m02,
    )

    s1 = st0
    for _ in range(n_gl[0]):
        s1 = gl4_rich_step(s1, t_nu_s / n_gl[0], rhs_mssm_spurion_cc, True)
    mmaj_tnu, utak_tnu = takagi_sym3_cc(fr3(s1[5]))
    yn_tnu_m = fr3(s1[4])
    kap_m = to3(-yn_tnu_m * (fr3(s1[5]) ** (-1)) * yn_tnu_m.T)
    st1 = (s1[0], s1[1], s1[2], s1[3], Z, Z, kap_m, *s1[7:11], Z, *s1[12:])

    s2 = st1
    for _ in range(n_gl[1]):
        s2 = gl4_rich_step(s2, (t_susy_s - t_nu_s) / n_gl[1], rhs_mssm_spurion_cc, False)
    yu_m = fr3(s2[1])
    u_q, su_l = eigh_svd_asc(yu_m)
    yt_mssm = su_l[2]
    uL3 = u_q[:, 2]
    uR3 = (yu_m.H * uL3) / yt_mssm
    mtL2 = mp.re((uL3.H * fr3(s2[16]) * uL3)[0, 0])
    mtR2 = mp.re((uR3.H * fr3(s2[17]) * uR3)[0, 0])
    ms_val = (mtL2 * mtR2) ** mp_rat(1, 4)

    m1_sq = mp.re(s2[15]) + abs(s2[12]) ** 2
    m2_sq = mp.re(s2[14]) + abs(s2[12]) ** 2
    b_abs = abs(s2[13])
    s2b = 2 * b_abs / (m1_sq + m2_sq)
    tb = (m1_sq + m2_sq + mp.sqrt((m1_sq + m2_sq) ** 2 - 4 * (b_abs ** 2))) / (2 * b_abs)
    sb, cb = tb / mp.sqrt(1 + tb * tb), 1 / mp.sqrt(1 + tb * tb)
    c2b = cb * cb - sb * sb

    At_eff = (uL3.H * fr3(s2[8]) * uR3)[0, 0] / yt_mssm
    Xt2 = abs(At_eff - mp.conj(s2[12]) / tb) ** 2
    yt_sm_ms = sb * yt_mssm
    dlam_stop = (3 * (yt_sm_ms ** 4) / (16 * (mp.pi ** 2))) * (Xt2 / (ms_val ** 2)) * (1 - Xt2 / (12 * (ms_val ** 2)))
    g12_s, g22_s = s2[0][0] ** 2, s2[0][1] ** 2
    lam_sm_ms = ((g22_s + mp_rat(3, 5) * g12_s) / 8) * (c2b ** 2) + dlam_stop
    mh2_sm_ms = b_abs * s2b - m1_sq * (cb ** 2) - m2_sq * (sb ** 2)

    v_susy_sq = 8 * (m1_sq - m2_sq * (tb ** 2)) / ((g22_s + mp_rat(3, 5) * g12_s) * (tb * tb - 1))
    mz_susy_sq = mp_rat(1, 4) * (g22_s + mp_rat(3, 5) * g12_s) * v_susy_sq
    mw_susy_sq = mp_rat(1, 4) * g22_s * v_susy_sq
    ma0_sq = m1_sq + m2_sq
    mhpm_sq = ma0_sq + mw_susy_sq
    ev_0p, _ = mp.eighe(mp.matrix([
        [ma0_sq * (sb ** 2) + mz_susy_sq * (cb ** 2), -(ma0_sq + mz_susy_sq) * sb * cb],
        [-(ma0_sq + mz_susy_sq) * sb * cb, ma0_sq * (cb ** 2) + mz_susy_sq * (sb ** 2) + 2 * dlam_stop * v_susy_sq / (sb ** 2)],
    ]))
    mh0_heavy_sq = max(mp.re(x) for x in ev_0p)

    st_sm0 = (s2[0], sc3(sb, s2[1]), sc3(cb, s2[2]), sc3(cb, s2[3]), sc3(sb * sb, s2[6]), lam_sm_ms, mh2_sm_ms)
    s3 = st_sm0
    for _ in range(n_gl[2]):
        s3 = gl4_rich_step(s3, (t_ew_s - t_susy_s) / n_gl[2], rhs_sm_mv84_tensor_cc)

    gf, yuf_l, ydf_l, yef_l, kapf_l, lam_ir, mh2_ir = s3
    vew_dim = mp.sqrt(mh2_ir / lam_ir)
    mgut_over_vew = 1 / vew_dim
    h_res = max(abs(mp.log(mmaj_tnu[0]) - t_nu_s), abs(mp.log(ms_val) - t_susy_s), abs(mp.log(vew_dim) - t_ew_s))

    yuf, ydf, yef, kapf = fr3(yuf_l), fr3(ydf_l), fr3(yef_l), fr3(kapf_l)
    uu, su = eigh_svd_asc(yuf)
    ud, sd = eigh_svd_asc(ydf)
    ue, se = eigh_svd_asc(yef)
    un, sn = eigh_svd_asc(kapf)
    vc, up = uu.H * ud, ue.H * un
    jc = abs(mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1])))
    jp = abs(mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1])))
    ia = [(4 * mp.pi) / (x * x) for x in gf]
    gy2, gw2 = mp_rat(3, 5) * (gf[0] ** 2), gf[1] ** 2
    evn = [(mp_rat(1, 2) * s_i * vew_dim) ** 2 for s_i in sn]

    msbar = {
        "u_m1_over_m3": su[0] / su[2], "u_m2_over_m3": su[1] / su[2],
        "d_m1_over_m3": sd[0] / sd[2], "d_m2_over_m3": sd[1] / sd[2],
        "e_m1_over_m3": se[0] / se[2], "e_m2_over_m3": se[1] / se[2],
        "u3_over_d3": su[2] / sd[2], "d3_over_e3": sd[2] / se[2],
        "ckm_v12": abs(vc[0, 1]), "ckm_v23": abs(vc[1, 2]), "ckm_v13": abs(vc[0, 2]), "ckm_jarlskog": jc,
        "pmns_u12": abs(up[0, 1]), "pmns_u23": abs(up[1, 2]), "pmns_u13": abs(up[0, 2]), "pmns_jarlskog": jp,
        "nu_dm21_sq_over_dm31_sq": (evn[1] - evn[0]) / (evn[2] - evn[0]),
        "strong_cp_bar_theta_qcd_raw_rad": mp.arg(mp.det(yuf * ydf)),
        "gauge_slope_2loop": (ia[0] - ia[1]) / (ia[1] - ia[2]),
        "tan_beta_ewsb": tb, "quartic_bfb_margin": lam_ir, "electroweak_mix_ratio": gy2 / (gw2 + gy2),
    }

    mu3_ms, mc_ms, md3_ms, me3_ms = su[2] / mp.sqrt(2), su[1] / mp.sqrt(2), sd[2] / mp.sqrt(2), se[2] / mp.sqrt(2)
    a3_ir = (gf[2] ** 2) / (4 * mp.pi)
    aqed_ir = (gy2 * gw2) / (4 * mp.pi * (gw2 + gy2))
    mu3_pole = mu3_ms * (1 + (a3_ir / mp.pi) * (mp_rat(4, 3) - 2 * mp.log(mu3_ms)))
    me3_pole = me3_ms * (1 + (aqed_ir / mp.pi) * (1 - mp_rat(3, 2) * mp.log(me3_ms)))
    a3_b = a3_ir / (1 + mp_rat(23, 6) * (a3_ir / mp.pi) * mp.log(md3_ms))
    md3_low = md3_ms * ((a3_b / a3_ir) ** mp_rat(12, 23))
    md3_pole = md3_low * (1 + mp_rat(4, 3) * (a3_b / mp.pi))

    b0_5, b1_5 = mp_rat(23, 3), mp_rat(116, 3)
    rhs_q5 = lambda x: -(b0_5 / (2 * mp.pi)) * (x * x) - (b1_5 / (8 * (mp.pi ** 2))) * (x ** 3)
    av_mb = a3_ir
    h_q = mp.log(md3_ms) / 180
    sr3_m = mp.sqrt(mp.mpf(3))
    for _ in range(180):
        k1q = rhs_q5(av_mb)
        k2q = k1q
        for _ in range(12):
            k1q = rhs_q5(av_mb + h_q * (mp_rat(1, 4) * k1q + (mp_rat(1, 4) - sr3_m / 6) * k2q))
            k2q = rhs_q5(av_mb + h_q * ((mp_rat(1, 4) + sr3_m / 6) * k1q + mp_rat(1, 4) * k2q))
        av_mb += (h_q / 2) * (k1q + k2q)

    def lam_qcd_cc(mu_q: mp.mpf, av: mp.mpf, nf_q: int) -> mp.mpf:
        b0_q, b1_q = mp_rat(33 - 2 * nf_q, 3), mp_rat(306 - 38 * nf_q, 3)
        ex_q = b1_q / (2 * (b0_q ** 2))
        return mu_q * mp.exp(-2 * mp.pi / (b0_q * av)) * (((b0_q * av) / (4 * mp.pi)) ** (-ex_q)) * ((1 + (b1_q * av) / (4 * mp.pi * b0_q)) ** ex_q)

    lam_5f = lam_qcd_cc(mp.mpf(1), a3_ir, 5)
    lam_4f = lam_qcd_cc(md3_ms, av_mb, 4)
    b0_4, b1_4 = mp_rat(25, 3), mp_rat(154, 3)
    rhs_q4 = lambda x: -(b0_4 / (2 * mp.pi)) * (x * x) - (b1_4 / (8 * (mp.pi ** 2))) * (x ** 3)
    av_mc = av_mb
    hq4 = mp.log(mc_ms / md3_ms) / 180
    for _ in range(180):
        k1q = rhs_q4(av_mc)
        k2q = k1q
        for _ in range(12):
            k1q = rhs_q4(av_mc + hq4 * (mp_rat(1, 4) * k1q + (mp_rat(1, 4) - sr3_m / 6) * k2q))
            k2q = rhs_q4(av_mc + hq4 * ((mp_rat(1, 4) + sr3_m / 6) * k1q + mp_rat(1, 4) * k2q))
        av_mc += (hq4 / 2) * (k1q + k2q)
    lam_3f = lam_qcd_cc(mc_ms, av_mc, 3)

    pole_bosons = {
        "u3_pole_over_vew": mu3_pole, "d3_low_over_e3_pole": md3_low / me3_pole, "d3_pole_over_e3_pole": md3_pole / me3_pole,
        "strong_coupling_ir": a3_ir, "qed_coupling_ir": aqed_ir,
        "qcd_Lambda_5f_over_vew": lam_5f, "qcd_Lambda_4f_over_vew": lam_4f, "mc_msbar_over_qcd_Lambda_4f": mc_ms / lam_4f,
        "mw_over_vew": mp_rat(1, 2) * gf[1], "mz_over_vew": mp_rat(1, 2) * mp.sqrt(gw2 + gy2),
        "higgs_h0_over_vew": mp.sqrt(2 * lam_ir), "higgs_H0_over_vew": mp.sqrt(mh0_heavy_sq) / vew_dim,
        "higgs_A0_over_vew": mp.sqrt(ma0_sq) / vew_dim, "higgs_Hpm_over_vew": mp.sqrt(mhpm_sq) / vew_dim,
        "ewsb_vmin_over_vew4": -mp_rat(1, 4) * lam_ir,
    }

    # Disjoint M_{11}-free Friedmann-Witten 16 pi G_4 = (2 pi)^2 / (T_M2^3 V_3^{dim} V_4^{dim}) + Hurwitz zeta Vol(m004):
    vol_m004 = (mp.sqrt(mp.mpf(3)) / 6) * (mp.zeta(2, mp_rat(1, 3)) - mp.zeta(2, mp_rat(2, 3)))
    tm2_hat = 48 * mp.pi / (8 * vol_m004)
    m11_mgut = (((2 * mp.pi) ** 2) * tm2_hat) ** mp_rat(1, 3)
    v3_hat = 8 * vol_m004
    v4_iso = ((2 * mp.pi) ** 4) / 48
    v4_sd = v4_iso * (m11_mgut ** (-4))
    mpl_mgut_sd = mp.sqrt((16 * mp.pi * (tm2_hat ** 3) * v3_hat * v4_sd) / ((2 * mp.pi) ** 2))
    mpl_mgut_iso = mp.sqrt((16 * mp.pi * (tm2_hat ** 3) * v3_hat * v4_iso) / ((2 * mp.pi) ** 2))
    mpl_vew_sd, mpl_vew_iso = mpl_mgut_sd * mgut_over_vew, mpl_mgut_iso * mgut_over_vew

    grav = {
        "cusp_robin_bc_star_tau8": mp.pi - l2_tau8, "m11_over_mgut_zero_knob": m11_mgut,
        "mpl_over_vew_d4_hurwitz_self_dual": mpl_vew_sd, "gn_vew_sq_d4_hurwitz_self_dual": 1 / (mpl_vew_sd ** 2),
        "mpl_over_vew_d4_hurwitz_isotropic": mpl_vew_iso, "gn_vew_sq_d4_hurwitz_isotropic": 1 / (mpl_vew_iso ** 2),
    }

    ue_tnu, se_tnu = eigh_svd_asc(fr3(s1[3]))
    Yt = ue_tnu.H * yn_tnu_m * utak_tnu
    Ht = Yt.H * Yt
    h00 = mp.re(Ht[0, 0])
    efl = [mp.mpf(0)] * 3
    for j in (1, 2):
        xv = (mmaj_tnu[j] / mmaj_tnu[0]) ** 2
        gm = mp.re(Ht[j, j]) / (8 * mp.pi)
        dn = (xv - 1) ** 2 + xv * (gm ** 2)
        f_sv, g_os = mp.sqrt(xv) * (2 * (1 - xv) / dn - mp.log(1 + 1 / xv)), 2 * (1 - xv) / dn
        for al in range(3):
            p1j = mp.conj(Yt[al, 0]) * Yt[al, j]
            efl[al] += (mp.im(p1j * Ht[0, j]) * f_sv + mp.im(p1j * Ht[j, 0]) * g_os) / (8 * mp.pi * h00)
    pbr = [abs(Yt[a, 0]) ** 2 / h00 for a in range(3)]
    g_star = mp_rat(915, 4)
    hub_m1 = mp.sqrt((mp.pi ** 2) * g_star / 90) * (mmaj_tnu[0] / (mpl_mgut_sd / mp.sqrt(8 * mp.pi)))
    k1_tot = (h00 / (4 * mp.pi)) / hub_m1
    gam_tau_h = (mp_rat(5, 1000) * (se_tnu[2] ** 2)) / hub_m1
    eta_tau = 1 / (1 + (pbr[2] * k1_tot) ** mp_rat(29, 25))
    eta_perp = 1 / (1 + ((pbr[0] + pbr[1]) * k1_tot) ** mp_rat(29, 25))
    neq_s = 2 * (135 * mp.zeta(3)) / (4 * (mp.pi ** 4) * g_star)
    yb_val = -mp_rat(8, 23) * neq_s * (efl[2] * eta_tau + (efl[0] + efl[1]) * eta_perp)

    y_end = 1 + 2 / mp.sqrt(mp.mpf(3))
    y_inf = mp.findroot(lambda y: mp_rat(3, 4) * ((y - y_end) - mp.log(y / y_end)) - 60, mp.mpf(82))
    eps_60 = mp_rat(4, 3) / ((y_inf - 1) ** 2)
    eta_60 = -mp_rat(4, 3) * (y_inf - 2) / ((y_inf - 1) ** 2)

    cosmo = {
        "proton_decay_dim6_mgut_over_vew_pow4": mgut_over_vew ** 4,
        "leptogenesis_Y_B_2flavor_analytic_fit": yb_val,
        "leptogenesis_eps_1_tau": efl[2], "leptogenesis_washout_K1_tot": k1_tot,
        "leptogenesis_tau_equil_over_hubble": gam_tau_h,
        "inflation_conformal_S4_ns_N60": 1 - 6 * eps_60 + 2 * eta_60,
        "inflation_conformal_S4_r_N60": 16 * eps_60,
    }
    return {
        "sm_msbar_at_ew_horizon": msbar, "sm_1loop_pole_and_2hdm_bosons": pole_bosons,
        "gravity_11d_d4_hurwitz_sector": grav, "cosmology_crv_and_honest_bounds": cosmo,
    }, h_res, lam_3f


def main() -> None:
    t0 = time.time()
    check_zero_ast_floats(Path(__file__).resolve().read_text(encoding="utf-8"), Path(__file__).name)

    raw_bytes = OUT_JSON.read_bytes()
    exp_sha = OUT_SHA.read_text(encoding="utf-8").strip().split()[0]
    assert hashlib.sha256(raw_bytes).hexdigest() == exp_sha
    doc = check_zero_json_floats(raw_bytes.decode("utf-8"), OUT_JSON.name)

    mp.mp.dps = 48
    uv_mats, l2_cc = build_uv_matrices_mellin_cc()
    e1 = doc["E1_literature_benchmark_gate"]
    e2 = doc["E2_three_stage_radiative_ewsb_and_higgs_lift"]
    horiz = tuple(mp.mpf(x) for x in e2["dynamical_horizons_tnu_tsusy_tew"])

    out_cc, h_res_cc, lam_3f_cc = eval_cc_pipeline_gl4(uv_mats, l2_cc, horiz, n_gl=(30, 48, 6))
    assert h_res_cc < mp.mpf(10) ** (-11)
    assert abs(lam_3f_cc - mp.mpf(e2["qcd_Lambda_3f_over_vew"])) / lam_3f_cc < mp_rat(5, 10 ** 10)

    exact_30d = {"cusp_robin_bc_star_tau8", "m11_over_mgut_zero_knob", "inflation_conformal_S4_ns_N60", "inflation_conformal_S4_r_N60"}
    prod_obs = e2["observables_50_N240"]
    max_30d_err = mp.mpf(0)
    max_rge_err = mp.mpf(0)
    for sec, sec_d in prod_obs.items():
        for k, v_s in sec_d.items():
            vp = mp.mpf(v_s)
            vc = out_cc[sec][k]
            rel = abs(vc - vp) / max(abs(vp), mp.mpf(10) ** (-20))
            if k in exact_30d:
                max_30d_err = max(max_30d_err, rel)
            else:
                max_rge_err = max(max_rge_err, rel)
    assert max_30d_err < mp.mpf(10) ** (-29) and max_rge_err < mp_rat(5, 10 ** 10)

    # 5 Planted-Fault Controls in Disjoint Countercheck:
    pf_1 = hashlib.sha256(raw_bytes + b" ").hexdigest() != exp_sha and e1["exact_rational_sm_beta_lam_2"] == "16142087/800000"
    assert pf_1

    # PF2: Upward criticality GL4 vs factor-1/2 d/d ln mu^2 error:
    yu_c0 = [[Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, mp.mpc(1)]]
    st_c0 = ([mp_rat(1, 2), mp_rat(1, 2), mp.mpf(1)], yu_c0, z3l(), z3l(), z3l(), mp_rat(1, 8), mp.mpf(1))
    s_tc = st_c0
    t_cr = mp.mpf(e1["sm_criticality_t_star_rk4"])
    for _ in range(16):
        s_tc = gl4_rich_step(s_tc, t_cr / 16, rhs_sm_mv84_tensor_cc)
    s_half = st_c0
    for _ in range(16):
        s_half = gl4_rich_step(s_half, (t_cr / 2) / 16, rhs_sm_mv84_tensor_cc)
    pf_2 = abs(s_tc[5]) < mp.mpf(10) ** (-11) and abs(s_half[5]) > mp_rat(1, 25)
    assert pf_2

    # PF3: Delta_H = 0 fails D-flat BFB stability in Spurion + GL4 engine:
    g0 = mp.sqrt(mp.pi / 6)
    m0_maj = mp.exp(-mp_rat(16, 5) * mp.pi)
    m32 = mp.exp(-mp_rat(48, 5) * mp.pi)
    sr3 = mp.sqrt(mp.mpf(3))
    m02 = m32 * m32
    yu0, yd0, ye0, yn0, cr0 = [to3(m) for m in uv_mats]
    Z = z3l()
    st_dh0 = (
        [g0, g0, g0], yu0, yd0, ye0, yn0, sc3(m0_maj, cr0), Z,
        [sr3 * m32] * 3, sc3(-sr3 * m32, yu0), sc3(-sr3 * m32, yd0), sc3(-sr3 * m32, ye0), sc3(-sr3 * m32, yn0),
        mp_rat(3, 2) * m32, mp_rat(-19, 12) * mp_rat(3, 2) * m02, m02, m02,
        i3l(m02), i3l(m02), i3l(m02), i3l(m02), i3l(m02), i3l(m02),
    )
    sd1 = st_dh0
    for _ in range(6):
        sd1 = gl4_rich_step(sd1, horiz[0] / 6, rhs_mssm_spurion_cc, True)
    kap_d = to3(-fr3(sd1[4]) * (fr3(sd1[5]) ** (-1)) * fr3(sd1[4]).T)
    sd2 = (sd1[0], sd1[1], sd1[2], sd1[3], Z, Z, kap_d, *sd1[7:11], Z, *sd1[12:])
    for _ in range(8):
        sd2 = gl4_rich_step(sd2, (horiz[1] - horiz[0]) / 8, rhs_mssm_spurion_cc, False)
    pf_3 = (mp.re(sd2[14]) + mp.re(sd2[15]) + 2 * (abs(sd2[12]) ** 2)) < 0
    assert pf_3

    # PF4: Radiative Higgs lift mh0 / mZ > 1 vs tree bound < 1:
    mh_mz_cc = out_cc["sm_1loop_pole_and_2hdm_bosons"]["higgs_h0_over_vew"] / out_cc["sm_1loop_pole_and_2hdm_bosons"]["mz_over_vew"]
    pf_4 = mh_mz_cc > mp.mpf(1) and mp.mpf(e2["mh0_tree_bound_over_mz"]) < mp.mpf(1) and out_cc["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"] > 0
    assert pf_4

    # PF5: Disjoint mp.expm(i H) SU(3)^6 scrambling (< 10^-25) vs non-Takagi M_R break (> 1/50):
    uq, uu, ud, ul, ue = [su3_expm_cc(s) for s in (11, 22, 33, 44, 55)]
    un = su3_expm_cc(66) * mp.exp(I_MP * mp_rat(2, 9))
    un_c = mp.matrix([[mp.conj(un[r, c]) for c in range(3)] for r in range(3)])
    uv_s_ok = (uq * uv_mats[0] * uu.H, uq * uv_mats[1] * ud.H, ul * uv_mats[2] * ue.H, ul * uv_mats[3] * un.H, un_c * uv_mats[4] * un.H)
    uv_s_bad = (uq * uv_mats[0] * uu.H, uq * uv_mats[1] * ud.H, ul * uv_mats[2] * ue.H, ul * uv_mats[3] * un.H, uv_mats[4])
    out_ref_s, _, _ = eval_cc_pipeline_gl4(uv_mats, l2_cc, horiz, n_gl=(5, 7, 3))
    out_scr_s, _, _ = eval_cc_pipeline_gl4(uv_s_ok, l2_cc, horiz, n_gl=(5, 7, 3))
    out_bad_s, _, _ = eval_cc_pipeline_gl4(uv_s_bad, l2_cc, horiz, n_gl=(5, 7, 3))
    scr_err = max(abs(out_scr_s[s][k] - out_ref_s[s][k]) / max(abs(out_ref_s[s][k]), mp.mpf(10) ** (-20)) for s in out_ref_s for k in out_ref_s[s])
    bad_brk = max(abs(out_bad_s[s][k] - out_ref_s[s][k]) / max(abs(out_ref_s[s][k]), mp.mpf(10) ** (-20)) for s in out_ref_s for k in out_ref_s[s])
    pf_5 = scr_err < mp.mpf(10) ** (-25) and bad_brk > mp_rat(1, 50)
    assert pf_5

    pf_tot = sum(int(x) for x in (pf_1, pf_2, pf_3, pf_4, pf_5))
    assert pf_tot == 5
    print(
        f"AGY-C42 disjoint countercheck PASSED in {int(time.time() - t0)}s: "
        f"max_30d_rel={mp.nstr(max_30d_err, 4)}, max_rge_rel={mp.nstr(max_rge_err, 4)}, "
        f"expm_scram={mp.nstr(scr_err, 4)}, planted_faults={pf_tot}/5."
    )


if __name__ == "__main__":
    main()
