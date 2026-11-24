#!/usr/bin/env python3
r"""Card AGY-C42 Standalone Zero-Float Producer (Layer 4 of Top-Down Synthesis, 0 of 19):
  - E1: Literature Benchmark Gate (Guardrail 4):
        (a) Verifies 50-digit agreement (< 10^-48) between expanded 2-loop Martin-Vaughn (PRD 50 (1994) 2282)
            MSSM + 3 N_R gauge/Yukawa/seesaw/Weinberg beta functions and N=1 supergraph Casimir anomalous
            dimensions gamma_i^{(1,2)} + NSVZ 2-loop gauge matrix on a non-commuting complex 3x3 rational state
            (catching transposed -2 H_d H_u Y_u > 10^-5, Control 1).
        (b) Verifies exact rational 2-loop 1HDM SM Higgs quartic beta_lambda^{(2)} == 16142087 / 800000
            (Luo-Xiao PRL 90 (2003) 011601 / Buttazzo et al. JHEP 1312 (2013) 089) and reproduces an upward
            lambda(mu) == 0 criticality horizon t_{crit}^* > 0 across Richardson-RK4 vs implicit GL4 (< 10^-11,
            catching d/d ln mu^2 vs d/d ln mu factor-of-1/2 error |Delta t_{crit}^*| > 2, Control 2).
  - E2: Self-Consistent Three-Stage Dynamical Horizon Chain (0 > t_nu^* > t_SUSY^* > t_EW^*):
        Integrates Layer-3 zero-knob UV matrices from M_GUT (alpha_GUT^-1 = |2T| = 24, M_0 / M_GUT = exp(-16 pi / 5),
        m_{3/2} / M_GUT = exp(-48 pi / 5)) under pure dilaton-dominated supergravity (M_{1/2}, m_0, A_0) =
        (sqrt(3), 1, -sqrt(3)) m_{3/2} and three rational 2 x 10_H / Giudice-Masiero boundary ratios
        (Delta_H, c_mu, c_B) = (12, 3/2, -19/12):
          * Stage I  [0, t_nu^*]:       2-loop MSSM + 3 N_R + soft RGEs -> kappa_MSSM & 2-flavor SUSY Y_B > 0;
          * Stage II [t_nu^*, t_SUSY^*]: 2-loop MSSM + kappa_MSSM + soft RGEs -> stop horizon M_S = (m_{t_L} m_{t_R})^{1/2},
            proving radiative EWSB from UV-positive m_{H_u}^2(M_GUT) = +m_0^2 > 0 & m_{H_d}^2(M_GUT) = (1 + Delta_H) m_0^2 > 0
            to m_2^2 < 0 < m_1^2 and D-flat BFB m_1^2 + m_2^2 > 2 |B mu| (vs Delta_H = 0 D-flat unbounded failure in Control 3),
            30/30 positive squark/slepton squared masses, large-tan(beta) m_t / m_b > 15, and radiative stop lift
            m_{h^0} / m_Z > 1 (vs tree-level D-term bound |cos 2 beta| < 1 in Control 4);
          * Stage III [t_SUSY^*, t_EW^*]: 2-loop 1HDM SM + kappa_SM -> v_EW(t_EW^*), MSbar + 1-loop pole masses,
            Caswell-Jones Lambda_QCD^{(5f,4f)} + dynamic charm decoupling check (n_f = 4 -> 3 when m_c > Lambda_QCD^{(4f)}),
            k = 24 Friedmann-Witten M_Pl / v_EW, and SUSY 6D B_{MN} UV QCD instanton |Delta bar_theta_UV| < 10^-30.
  - E3: Step-halving N = 120 vs N = 240 (< 10^-10), 13x single-anchor energy-unit scaling homogeneity (< 10^-30),
        and SU(3)^6 Haar basis-scrambling invariance (< 10^-25, vs non-Takagi M_R break > 1/50 in Control 5).
"""
from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction as Fr
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


def verify_ast_strict(src: str, filename: str) -> dict[str, object]:
    tree = ast.parse(src, filename=filename)
    bad_lits = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex))]
    bad_calls = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex")]
    bad_imps: list[str] = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            bad_imps.extend(a.name for a in n.names if a.name.startswith("frontier") or "grid" in a.name)
        elif isinstance(n, ast.ImportFrom) and n.module:
            if n.module.startswith("frontier") or "grid" in n.module:
                bad_imps.append(n.module)
    return {
        "float_or_complex_literals": len(bad_lits),
        "float_or_complex_calls": len(bad_calls),
        "forbidden_imports": len(bad_imps),
        "passed": not bad_lits and not bad_calls and not bad_imps,
    }


# ==============================================================================
# Fast 3x3 List-of-List Complex Matrix Primitives
# ==============================================================================
Mat3 = list[list[mp.mpc]]


def z3l() -> Mat3:
    return [[Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, Z0_C]]


def i3l(v: mp.mpc = mp.mpc(1)) -> Mat3:
    return [[v, Z0_C, Z0_C], [Z0_C, v, Z0_C], [Z0_C, Z0_C, v]]


def to3(m: mp.matrix) -> Mat3:
    return [[mp.mpc(m[r, c]) for c in range(3)] for r in range(3)]


def fr3(a: Mat3) -> mp.matrix:
    return mp.matrix(a)


def add3(a: Mat3, b: Mat3) -> Mat3:
    return [[a[r][c] + b[r][c] for c in range(3)] for r in range(3)]


def sub3(a: Mat3, b: Mat3) -> Mat3:
    return [[a[r][c] - b[r][c] for c in range(3)] for r in range(3)]


def sc3(s: mp.mpc, a: Mat3) -> Mat3:
    return [[s * a[r][c] for c in range(3)] for r in range(3)]


def dag3(a: Mat3) -> Mat3:
    return [[mp.conj(a[r][c]) for r in range(3)] for c in range(3)]


def tp3(a: Mat3) -> Mat3:
    return [[a[r][c] for r in range(3)] for c in range(3)]


def tr3(a: Mat3) -> mp.mpf:
    return mp.re(a[0][0] + a[1][1] + a[2][2])


def mul3(a: Mat3, b: Mat3) -> Mat3:
    return [
        [a[r][0] * b[0][c] + a[r][1] * b[1][c] + a[r][2] * b[2][c] for c in range(3)]
        for r in range(3)
    ]


def hmul(a: Mat3) -> Mat3:
    return [
        [a[r][0] * mp.conj(a[c][0]) + a[r][1] * mp.conj(a[c][1]) + a[r][2] * mp.conj(a[c][2]) for c in range(3)]
        for r in range(3)
    ]


def htmul(a: Mat3) -> Mat3:
    return [
        [mp.conj(a[0][r]) * a[0][c] + mp.conj(a[1][r]) * a[1][c] + mp.conj(a[2][r]) * a[2][c] for c in range(3)]
        for r in range(3)
    ]


def tr_dag_mul(a: Mat3, b: Mat3) -> mp.mpc:
    return sum((mp.conj(a[r][c]) * b[r][c] for r in range(3) for c in range(3)), Z0_C)


def max_diff3(a: Mat3, b: Mat3) -> mp.mpf:
    return max(abs(a[r][c] - b[r][c]) for r in range(3) for c in range(3))


# ==============================================================================
# Standalone Layer-3 Zero-Knob UV Yukawa & Majorana Matrix Builder
# ==============================================================================
def solve_l2_jacobi_taylor26(tau: mp.mpc, work_dps: int = 50) -> tuple[mp.mpf, mp.mpf]:
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
        q_nom = mp.exp(I_MP * mp.pi * z_lat)
        t20, t30, t40 = mp.jtheta(2, 0, q_nom), mp.jtheta(3, 0, q_nom), mp.jtheta(4, 0, q_nom)
        e1 = (mp.pi ** 2 / 3) * (t30 ** 4 + t40 ** 4)
        e2 = (mp.pi ** 2 / 3) * (t20 ** 4 - t40 ** 4)
        e3 = -(mp.pi ** 2 / 3) * (t20 ** 4 + t30 ** 4)
        g2 = 2 * (e1 ** 2 + e2 ** 2 + e3 ** 2)
        g3 = 4 * e1 * e2 * e3
        pref_wpp = -2 * (mp.pi ** 3) * ((t20 * t30 * t40) ** 2)

        def wp_wpp_jt(zv: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
            nr = int(mp.nint(mp.im(zv) / mp.im(z_lat)))
            zc = zv - nr * z_lat
            zc -= int(mp.nint(mp.re(zc)))
            pz = mp.pi * zc
            t1, t2, t3, t4 = mp.jtheta(1, pz, q_nom), mp.jtheta(2, pz, q_nom), mp.jtheta(3, pz, q_nom), mp.jtheta(4, pz, q_nom)
            return e1 + ((mp.pi * t30 * t40 * t2) / t1) ** 2, pref_wpp * (t2 * t3 * t4) / (t1 ** 3)

        p_ord = 26
        qr = mp_rat(1, 4)

        def prop_taylor(nodes: list[mp.mpc], c_v: mp.mpc, want_dc: bool):
            t_m = mp.eye(2)
            dt_m = mp.zeros(2, 2)
            for idx in range(len(nodes) - 1):
                zk = nodes[idx]
                h = nodes[idx + 1] - zk
                p0, p1 = wp_wpp_jt(zk)
                pa = [Z0_C] * (p_ord + 1)
                pa[0], pa[1], pa[2] = p0, p1, 3 * (p0 ** 2) - qr * g2
                for m in range(1, p_ord - 1):
                    pa[m + 2] = mp_rat(6, (m + 2) * (m + 1)) * mp.fsum(pa[j] * pa[m - j] for j in range(m + 1))
                qa = [qr * pa[m] for m in range(p_ord + 1)]
                qa[0] += c_v
                tn = mp.zeros(2, 2)
                dtn = mp.zeros(2, 2)
                hp = [h ** m for m in range(p_ord + 3)]
                for col in range(2):
                    wc = [Z0_C] * (p_ord + 3)
                    wc[0], wc[1] = t_m[0, col], t_m[1, col]
                    for m in range(p_ord + 1):
                        wc[m + 2] = -mp.fsum(qa[j] * wc[m - j] for j in range(m + 1)) / ((m + 2) * (m + 1))
                    tn[0, col] = mp.fsum(wc[m] * hp[m] for m in range(p_ord + 3))
                    tn[1, col] = mp.fsum(m * wc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                    if want_dc:
                        dwc = [Z0_C] * (p_ord + 3)
                        dwc[0], dwc[1] = dt_m[0, col], dt_m[1, col]
                        for m in range(p_ord + 1):
                            dwc[m + 2] = -(wc[m] + mp.fsum(qa[j] * dwc[m - j] for j in range(m + 1))) / ((m + 2) * (m + 1))
                        dtn[0, col] = mp.fsum(dwc[m] * hp[m] for m in range(p_ord + 3))
                        dtn[1, col] = mp.fsum(m * dwc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                t_m, dt_m = tn, dtn
            return (t_m, dt_m) if want_dc else t_m

        z0 = mp_rat(1, 2) + mp_rat(1, 2) * z_lat
        n_st = 64
        nds_a = [z0 + mp_rat(k, n_st) for k in range(n_st + 1)]
        nds_b = [z0 + mp_rat(k, n_st) * z_lat for k in range(n_st + 1)]
        c_val = mp.mpc((mp.pi ** 2) / 12)
        for _ in range(18):
            ta, dta = prop_taylor(nds_a, c_val, True)
            tb, dtb = prop_taylor(nds_b, c_val, True)
            tab = ta * tb
            dtab = dta * tb + ta * dtb
            rv = [mp.im(ta[0, 0] + ta[1, 1]), mp.im(tb[0, 0] + tb[1, 1]), mp.im(tab[0, 0] + tab[1, 1])]
            if max(abs(x) for x in rv) < mp.mpf(10) ** (-36):
                break
            trs = [dta[0, 0] + dta[1, 1], dtb[0, 0] + dtb[1, 1], dtab[0, 0] + dtab[1, 1]]
            jr, ji = [mp.im(t) for t in trs], [mp.re(t) for t in trs]
            a11, a12, a22 = sum(x * x for x in jr), sum(jr[k] * ji[k] for k in range(3)), sum(x * x for x in ji)
            b1, b2 = -sum(jr[k] * rv[k] for k in range(3)), -sum(ji[k] * rv[k] for k in range(3))
            det_a = a11 * a22 - a12 * a12
            c_val += mp.mpc((a22 * b1 - a12 * b2) / det_a, (a11 * b2 - a12 * b1) / det_a)

        ta = prop_taylor(nds_a, c_val, False)
        tb = prop_taylor(nds_b, c_val, False)
        inv2 = lambda m: mp.matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]]) / (m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0])
        mob = lambda m: mp.matrix([[m[1, 1], m[0, 1]], [m[1, 0], m[0, 0]]]) / mp.sqrt(m[1, 1] * m[0, 0] - m[0, 1] * m[1, 0])
        tp = tb * ta * inv2(tb) * inv2(ta)
        aa, p0 = mob(ta), mob(tp)
        pf = (p0[0, 0] - p0[1, 1]) / (2 * p0[1, 0])
        da = mp.sqrt((aa[0, 0] - aa[1, 1]) ** 2 + 4 * aa[0, 1] * aa[1, 0])
        fa1, fa2 = (aa[0, 0] - aa[1, 1] + da) / (2 * aa[1, 0]), (aa[0, 0] - aa[1, 1] - da) / (2 * aa[1, 0])
        ssc = (fa2 - fa1) / (fa2 - pf)
        g = mp.matrix([[mp.mpf(1) / ssc, -fa1 / ssc], [mp.mpf(1), -pf]])
        g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
        if mp.im(g[0, 1] / g[1, 1]) < 0:
            g = mp.matrix([[I_MP, 0], [0, -I_MP]]) * g
        rp = g * p0 * inv2(g)
        lam = abs(mp.re(rp[0, 1] / rp[0, 0]))

        m_ord = 56
        laur = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, m_ord // 2 + 2):
            laur[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * mp.fsum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
        qc = [Z0_C] * (m_ord + 1)
        qc[0] = c_val
        for n in range(1, m_ord // 2 + 1):
            qc[2 * n] = qr * laur[n]
        al = [Z0_C] * (m_ord + 1)
        be = [Z0_C] * (m_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, m_ord + 1):
            al[m] = -mp.fsum(qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + mp.fsum(qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)

        def eval_bc_at(den_r: int) -> mp.mpf:
            zs = mp_rat(1, den_r) * z0 / abs(z0)
            n_rad = 72
            rat_r = abs(zs) / abs(z0)
            nds_in = [z0 * (rat_r ** mp_rat(k, n_rad)) for k in range(n_rad + 1)]
            tin = prop_taylor(nds_in, c_val, False)
            gloc = mp.fsum(be[m] * (zs ** m) for m in range(m_ord + 1)) / mp.fsum(al[m] * (zs ** m) for m in range(m_ord + 1))
            wzs = tin[0, 1] / tin[0, 0]
            uzs = (g[0, 0] * wzs + g[0, 1]) / (g[1, 0] * wzs + g[1, 1])
            imb = mp.im(uzs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(gloc))
            return (2 * mp.pi / lam) * imb

        bc24, bc36 = eval_bc_at(24), eval_bc_at(36)
        return (mp.pi - bc24) + shift, abs(bc24 - bc36)
    finally:
        mp.mp.dps = old


def theta_triple(tau: mp.mpc, ca: Fr, cb: Fr) -> mp.mpc:
    ta, tb = ca % 1, cb % 1
    nb = int(cb - tb)
    am, bm = f2m(ta), f2m(tb)
    zv = am * tau + bm
    q = mp.exp(I_MP * mp.pi * tau)
    w = mp.exp(2 * I_MP * mp.pi * zv)
    pr = mp.mpc(1)
    for m in range(1, 95):
        q2m = q ** (2 * m)
        qm = q ** (2 * m - 1)
        if abs(qm) * max(abs(w), 1 / abs(w)) < mp.mpf(10) ** (-54):
            break
        pr *= (1 - q2m) * (1 + qm * w) * (1 + qm / w)
    base = mp.exp(I_MP * mp.pi * am * am * tau + 2 * I_MP * mp.pi * am * bm) * pr
    return base if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * base


def eval_szego_yukawa_mp(tx: Fr, ty: Fr, l2_val: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    t = mp.mpc(f2m(tx), f2m(ty))
    xr, yi = mp.re(t), mp.im(t)
    q = mp.exp(2 * I_MP * mp.pi * t)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = Z0_C
    for n in range(-28, 29):
        m2 = mp_rat((2 * n + 1) ** 2, 8)
        e2v = mp.exp(2 * I_MP * mp.pi * t * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = mp_rat(n * n, 2)
        e3v = mp.exp(2 * I_MP * mp.pi * t * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2s = mp.mpc(1)
    qn = q
    for n in range(1, 45):
        e2s -= 24 * n * (qn / (1 - qn))
        qn *= q
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / 24) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / 24) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / 24) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    pr = mp.mpc(1)
    qn = q
    for _ in range(45):
        pr *= 1 - qn
        qn *= q
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * t / 12) * pr) ** 3
    csh = 2 * mp.pi * l2_val + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_val)

    def thc(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f2m(ta), f2m(tb)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        s = mp.fsum(mp.exp(I_MP * mp.pi * t * (mp.mpf(k) ** 2) + 2 * I_MP * mp.pi * mp.mpf(k) * zv) for k in range(n0 - 26, n0 + 27))
        b = mp.exp(I_MP * mp.pi * am * am * t + 2 * I_MP * mp.pi * am * bm) * s
        return b if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * b

    def a0fu(ai: Fr, bi: Fr) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = f2m(al), f2m(be)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        vl = dr = Z0_C
        for dk in range(-26, 27):
            m = mp.mpf(n0 + dk) + hf
            trm = mp.exp(I_MP * mp.pi * t * m * m + 2 * I_MP * mp.pi * m * (zv + hf))
            vl -= trm
            dr -= (2 * I_MP * mp.pi * m) * trm
        a2 = abs(2 * I_MP * mp.pi * am + dr / vl) ** 2
        if al != 0:
            f0 = -mp.pi * (2 * mp.log(2) + mp.log(yi) + mp.digamma(am) + mp.digamma(1 - am))
        else:
            f0 = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yi)) + yi * (mp.pi ** 2) / (mp.sin(mp.pi * bm) ** 2)
        sm = mp.mpf(0)
        for k in range(-32, 33):
            m = am + k
            if m == 0:
                continue
            w = mp.exp(-2 * mp.pi * abs(m) * yi + 2 * I_MP * mp.pi * (m * xr + bm))
            sm += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
        return a2, f0 + sm

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
        rv = kap[sk] * thc(cs[sk][0], cs[sk][1]) * thc(ds[sk][0], ds[sk][1]) / t1p
        a2, fv = a0fu(al, be)
        ag = csh + fv - mp.pi * a2 * em2l
        um[sk] = mp.sqrt(ag) * rv if ag > 0 else Z0_C
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix([[ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1] for cb in range(3)] for ra in range(3)])


def build_layer3_uv_matrices(hand_sign: int = 1) -> tuple[tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix], mp.mpf]:
    tx8, ty8 = Fr(16 * hand_sign, 5), Fr(8, 5)
    tau_8 = mp.mpc(f2m(tx8), f2m(ty8))
    l2_pos, rad_err = solve_l2_jacobi_taylor26(mp.mpc(mp_rat(16, 5), mp_rat(8, 5)), work_dps=50)
    assert rad_err < mp.mpf(10) ** (-34)

    def w_k56(ql: int, qr: int) -> mp.matrix:
        m5 = sum((eval_szego_yukawa_mp(tx8, ty8, l2_pos, pa, pb * hand_sign, ql, qr) for pa, pb in K5_PTS), mp.zeros(3, 3)) / 4
        m6 = sum((eval_szego_yukawa_mp(tx8, ty8, l2_pos, pa, pb * hand_sign, ql, qr) for pa, pb in K6_PTS), mp.zeros(3, 3)) / 2
        return (m5 + m6) / 2

    wu, wd, we, wnu = w_k56(2, -3), w_k56(2, -1), w_k56(-6, 7), w_k56(-6, 5)
    wr_raw = w_k56(5, 5)
    cr = (wr_raw + wr_raw.T) / 2

    g_gut = mp.sqrt(mp.pi / 6)
    pref = g_gut * (2 * mp.sqrt(mp.mpf(2)) * mp.im(tau_8))

    def mag_env(d_int: int) -> mp.matrix:
        td = d_int * tau_8
        t0 = abs(theta_triple(td, Fr(0), Fr(0)))
        return mp.diag([abs(theta_triple(td, Fr(1, 2), Fr(0))) / t0, abs(theta_triple(td, Fr(1, 4), Fr(0))) / t0, mp.mpf(1)])

    e10, e5 = mag_env(3), mag_env(1)
    return (pref * (e10 * wu * e10), pref * (e10 * wd * e5), pref * (e5 * we * e10), pref * (e5 * wnu), cr), l2_pos


# ==============================================================================
# Two-Loop MSSM + 3 N_R & Two-Loop 1HDM SM RGE Engines
# ==============================================================================
def rhs_mssm(st: tuple, has_nr: bool, swap_huhd_bug: bool = False) -> tuple:
    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    Z = z3l()
    g, yu, yd, ye, yn_i, mr_i, kap_i, mg, Tu, Td, Te, Tn_i, mu_v, bmu_v, mHu2, mHd2, mQ, mu_r, md_r, mL, me_r, mN_r = st
    yn = yn_i if has_nr else Z
    Tn = Tn_i if has_nr else Z
    g12, g22, g32 = g[0] ** 2, g[1] ** 2, g[2] ** 2

    hu, hd, he = hmul(yu), hmul(yd), hmul(ye)
    hn = hmul(yn) if has_nr else Z
    htu, htd, hte = htmul(yu), htmul(yd), htmul(ye)
    htn = htmul(yn) if has_nr else Z
    tru, trd, tre = tr3(hu), tr3(hd), tr3(he)
    trn = tr3(hn) if has_nr else mp.mpf(0)
    tu, td = 3 * tru + trn, 3 * trd + tre

    b1 = (mp_rat(33, 5), mp.mpf(1), mp.mpf(-3))
    B2 = (
        (mp_rat(199, 25), mp_rat(27, 5), mp_rat(88, 5)),
        (mp_rat(9, 5), mp.mpf(25), mp.mpf(24)),
        (mp_rat(11, 5), mp.mpf(9), mp.mpf(14)),
    )
    Cf = (
        mp_rat(26, 5) * tru + mp_rat(14, 5) * trd + mp_rat(18, 5) * tre + mp_rat(6, 5) * trn,
        6 * tru + 6 * trd + 2 * tre + 2 * trn,
        4 * tru + 4 * trd,
    )
    dg = [inv1 * b1[a] * (g[a] ** 3) + inv2 * (g[a] ** 3) * (B2[a][0] * g12 + B2[a][1] * g22 + B2[a][2] * g32 - Cf[a]) for a in range(3)]

    tr_yt0, tr_yt1, tr_yt2 = tr_dag_mul(yu, Tu), tr_dag_mul(yd, Td), tr_dag_mul(ye, Te)
    tr_yt3 = tr_dag_mul(yn, Tn) if has_nr else Z0_C
    Cyt = (
        mp_rat(26, 5) * tr_yt0 + mp_rat(14, 5) * tr_yt1 + mp_rat(18, 5) * tr_yt2 + mp_rat(6, 5) * tr_yt3,
        6 * tr_yt0 + 6 * tr_yt1 + 2 * tr_yt2 + 2 * tr_yt3,
        4 * tr_yt0 + 4 * tr_yt1,
    )
    dmg = [
        2 * inv1 * b1[a] * (g[a] ** 2) * mg[a]
        + 2 * inv2 * (g[a] ** 2) * (B2[a][0] * g12 * (mg[a] + mg[0]) + B2[a][1] * g22 * (mg[a] + mg[1]) + B2[a][2] * g32 * (mg[a] + mg[2]) - Cf[a] * mg[a] + Cyt[a])
        for a in range(3)
    ]

    hu2, hd2, he2 = mul3(hu, hu), mul3(hd, hd), mul3(he, he)
    hn2 = mul3(hn, hn) if has_nr else Z
    tru2, trd2, tre2 = tr3(hu2), tr3(hd2), tr3(he2)
    trn2 = tr3(hn2) if has_nr else mp.mpf(0)
    huhd, hdhu = mul3(hu, hd), mul3(hd, hu)
    trud = tr3(huhd)
    trne = tr3(mul3(hn, he)) if has_nr else mp.mpf(0)

    gHu = inv1 * (tu - mp_rat(3, 10) * g12 - mp_rat(3, 2) * g22) + inv2 * (
        -9 * tru2 - 3 * trud - 3 * trn2 - trne + (mp_rat(4, 5) * g12 + 16 * g32) * tru
        + mp_rat(207, 100) * g12 * g12 + mp_rat(9, 10) * g12 * g22 + mp_rat(15, 4) * g22 * g22
    )
    gHd = inv1 * (td - mp_rat(3, 10) * g12 - mp_rat(3, 2) * g22) + inv2 * (
        -9 * trd2 - 3 * trud - 3 * tre2 - trne + (-mp_rat(2, 5) * g12 + 16 * g32) * trd + mp_rat(6, 5) * g12 * tre
        + mp_rat(207, 100) * g12 * g12 + mp_rat(9, 10) * g12 * g22 + mp_rat(15, 4) * g22 * g22
    )

    ew_u = mp_rat(2743, 450) * g12 * g12 + g12 * g22 + mp_rat(136, 45) * g12 * g32 + mp_rat(15, 2) * g22 * g22 + 8 * g22 * g32 - mp_rat(16, 9) * g32 * g32
    ew_d = mp_rat(287, 90) * g12 * g12 + g12 * g22 + mp_rat(8, 9) * g12 * g32 + mp_rat(15, 2) * g22 * g22 + 8 * g22 * g32 - mp_rat(16, 9) * g32 * g32
    ew_e = mp_rat(27, 2) * g12 * g12 + mp_rat(9, 5) * g12 * g22 + mp_rat(15, 2) * g22 * g22
    ew_n = mp_rat(207, 50) * g12 * g12 + mp_rat(9, 5) * g12 * g22 + mp_rat(15, 2) * g22 * g22

    cross_u = hdhu if swap_huhd_bug else huhd
    du_diag = inv1 * (tu - mp_rat(13, 15) * g12 - 3 * g22 - mp_rat(16, 3) * g32) + inv2 * (-9 * tru2 - 3 * trud - 3 * trn2 - trne + (mp_rat(4, 5) * g12 + 16 * g32) * tru + ew_u)
    dd_diag = inv1 * (td - mp_rat(7, 15) * g12 - 3 * g22 - mp_rat(16, 3) * g32) + inv2 * (-9 * trd2 - 3 * trud - 3 * tre2 - trne + (-mp_rat(2, 5) * g12 + 16 * g32) * trd + mp_rat(6, 5) * g12 * tre + ew_d)
    de_diag = inv1 * (td - mp_rat(9, 5) * g12 - 3 * g22) + inv2 * (-9 * trd2 - 3 * trud - 3 * tre2 - trne + (-mp_rat(2, 5) * g12 + 16 * g32) * trd + mp_rat(6, 5) * g12 * tre + ew_e)

    au1, au2 = 3 * inv1 + inv2 * (-3 * tu + mp_rat(2, 5) * g12 + 6 * g22), inv1 + inv2 * (-td + mp_rat(2, 5) * g12)
    ad1, ad2 = 3 * inv1 + inv2 * (-3 * td + mp_rat(4, 5) * g12 + 6 * g22), inv1 + inv2 * (-tu + mp_rat(4, 5) * g12)
    ae1, ae2 = 3 * inv1 + inv2 * (-3 * td + 6 * g22), inv1 - inv2 * tu
    hehn = mul3(he, hn) if has_nr else Z

    ku = [[au1 * hu[r][c] + au2 * hd[r][c] - inv2 * (4 * hu2[r][c] + 2 * cross_u[r][c] + 2 * hd2[r][c]) + (du_diag if r == c else Z0_C) for c in range(3)] for r in range(3)]
    kd = [[ad1 * hd[r][c] + ad2 * hu[r][c] - inv2 * (4 * hd2[r][c] + 2 * hdhu[r][c] + 2 * hu2[r][c]) + (dd_diag if r == c else Z0_C) for c in range(3)] for r in range(3)]
    ke = [[ae1 * he[r][c] + ae2 * hn[r][c] - inv2 * (4 * he2[r][c] + 2 * hehn[r][c] + 2 * hn2[r][c]) + (de_diag if r == c else Z0_C) for c in range(3)] for r in range(3)]
    dyu, dyd, dye = mul3(ku, yu), mul3(kd, yd), mul3(ke, ye)

    if has_nr:
        hnhe = mul3(hn, he)
        dn_diag = inv1 * (tu - mp_rat(3, 5) * g12 - 3 * g22) + inv2 * (-9 * tru2 - 3 * trud - 3 * trn2 - trne + (mp_rat(4, 5) * g12 + 16 * g32) * tru + ew_n)
        an1, an2 = 3 * inv1 + inv2 * (-3 * tu + mp_rat(6, 5) * g12 + 6 * g22), inv1 + inv2 * (-td + mp_rat(6, 5) * g12)
        kn = [[an1 * hn[r][c] + an2 * he[r][c] - inv2 * (4 * hn2[r][c] + 2 * hnhe[r][c] + 2 * he2[r][c]) + (dn_diag if r == c else Z0_C) for c in range(3)] for r in range(3)]
        dyn = mul3(kn, yn)
        ynH_hne_yn = mul3(dag3(yn), mul3(add3(hn, he), yn))
        gn_c = 2 * inv1 + inv2 * (-2 * tu + mp_rat(6, 5) * g12 + 6 * g22)
        gN = [[gn_c * htn[r][c] - 2 * inv2 * ynH_hne_yn[r][c] for c in range(3)] for r in range(3)]
        dmr = add3(mul3(tp3(gN), mr_i), mul3(mr_i, gN))
        dkap = Z
    else:
        dyn, dmr = Z, Z
        dLHu = gHu - inv1 * (mp_rat(3, 10) * g12 + mp_rat(3, 2) * g22) + inv2 * (mp_rat(207, 100) * g12 * g12 + mp_rat(9, 10) * g12 * g22 + mp_rat(15, 4) * g22 * g22)
        cl1 = inv1 + inv2 * (-td + mp_rat(6, 5) * g12)
        gLHu = [[cl1 * he[r][c] - 2 * inv2 * he2[r][c] + (dLHu if r == c else Z0_C) for c in range(3)] for r in range(3)]
        dkap = add3(mul3(gLHu, kap_i), mul3(kap_i, tp3(gLHu)))

    dmu = (gHu + gHd) * mu_v
    su1 = tu - mp_rat(13, 15) * g12 - 3 * g22 - mp_rat(16, 3) * g32
    sd1 = td - mp_rat(7, 15) * g12 - 3 * g22 - mp_rat(16, 3) * g32
    se1 = td - mp_rat(9, 5) * g12 - 3 * g22
    cu_y = 6 * tr_yt0 + 2 * tr_yt3 + mp_rat(26, 15) * g12 * mg[0] + 6 * g22 * mg[1] + mp_rat(32, 3) * g32 * mg[2]
    cd_y = 6 * tr_yt1 + 2 * tr_yt2 + mp_rat(14, 15) * g12 * mg[0] + 6 * g22 * mg[1] + mp_rat(32, 3) * g32 * mg[2]
    ce_y = 6 * tr_yt1 + 2 * tr_yt2 + mp_rat(18, 5) * g12 * mg[0] + 6 * g22 * mg[1]

    dTu = sc3(inv1, add3(add3(mul3([[5 * hu[r][c] + hd[r][c] + (su1 if r == c else Z0_C) for c in range(3)] for r in range(3)], Tu), sc3(4, mul3(Tu, htu))), add3(sc3(2, mul3(Td, mul3(dag3(yd), yu))), sc3(cu_y, yu))))
    dTd = sc3(inv1, add3(add3(mul3([[5 * hd[r][c] + hu[r][c] + (sd1 if r == c else Z0_C) for c in range(3)] for r in range(3)], Td), sc3(4, mul3(Td, htd))), add3(sc3(2, mul3(Tu, mul3(dag3(yu), yd))), sc3(cd_y, yd))))
    t_le = sc3(2, mul3(Tn, mul3(dag3(yn), ye))) if has_nr else Z
    dTe = sc3(inv1, add3(add3(mul3([[5 * he[r][c] + hn[r][c] + (se1 if r == c else Z0_C) for c in range(3)] for r in range(3)], Te), sc3(4, mul3(Te, hte))), add3(t_le, sc3(ce_y, ye))))
    if has_nr:
        sn1 = tu - mp_rat(3, 5) * g12 - 3 * g22
        cn_y = 6 * tr_yt0 + 2 * tr_yt3 + mp_rat(6, 5) * g12 * mg[0] + 6 * g22 * mg[1]
        dTn = sc3(inv1, add3(add3(mul3([[5 * hn[r][c] + he[r][c] + (sn1 if r == c else Z0_C) for c in range(3)] for r in range(3)], Tn), sc3(4, mul3(Tn, htn))), add3(sc3(2, mul3(Te, mul3(dag3(ye), yn))), sc3(cn_y, yn))))
    else:
        dTn = Z
    dbmu = inv1 * ((tu + td - mp_rat(3, 5) * g12 - 3 * g22) * bmu_v + (6 * tr_yt0 + 6 * tr_yt1 + 2 * tr_yt2 + 2 * tr_yt3 + mp_rat(6, 5) * g12 * mg[0] + 6 * g22 * mg[1]) * mu_v)

    S_fi = mHu2 - mHd2 + tr3(mQ) - tr3(mL) - 2 * tr3(mu_r) + tr3(md_r) + tr3(me_r)
    mk_X = lambda mL_s, hf_s, yf_s, mR_s, mH_s, Tf_s: add3(add3(mul3(mL_s, hf_s), mul3(hf_s, mL_s)), add3(sc3(2, mul3(yf_s, mul3(mR_s, dag3(yf_s)))), add3(sc3(2 * mH_s, hf_s), sc3(2, hmul(Tf_s)))))
    mk_Xt = lambda mR_s, htf_s, yf_s, mL_s, mH_s, Tf_s: add3(add3(mul3(mR_s, htf_s), mul3(htf_s, mR_s)), add3(sc3(2, mul3(dag3(yf_s), mul3(mL_s, yf_s))), add3(sc3(2 * mH_s, htf_s), sc3(2, htmul(Tf_s)))))

    Xu, Xd, Xe = mk_X(mQ, hu, yu, mu_r, mHu2, Tu), mk_X(mQ, hd, yd, md_r, mHd2, Td), mk_X(mL, he, ye, me_r, mHd2, Te)
    Xtu, Xtd, Xte = mk_Xt(mu_r, htu, yu, mQ, mHu2, Tu), mk_Xt(md_r, htd, yd, mQ, mHd2, Td), mk_Xt(me_r, hte, ye, mL, mHd2, Te)
    Xn = mk_X(mL, hn, yn, mN_r, mHu2, Tn) if has_nr else Z
    Xtn = mk_Xt(mN_r, htn, yn, mL, mHu2, Tn) if has_nr else Z

    m1sq, m2sq, m3sq = abs(mg[0]) ** 2, abs(mg[1]) ** 2, abs(mg[2]) ** 2
    dmHu2 = inv1 * (3 * tr3(Xu) + (tr3(Xn) if has_nr else mp.mpf(0)) - mp_rat(6, 5) * g12 * m1sq - 6 * g22 * m2sq + mp_rat(3, 5) * g12 * S_fi)
    dmHd2 = inv1 * (3 * tr3(Xd) + tr3(Xe) - mp_rat(6, 5) * g12 * m1sq - 6 * g22 * m2sq - mp_rat(3, 5) * g12 * S_fi)
    add_d = lambda M, d: [[M[r][c] + (d if r == c else Z0_C) for c in range(3)] for r in range(3)]
    dmQ = sc3(inv1, add_d(add3(Xu, Xd), -mp_rat(2, 15) * g12 * m1sq - 6 * g22 * m2sq - mp_rat(32, 3) * g32 * m3sq + mp_rat(1, 5) * g12 * S_fi))
    dmu_r = sc3(inv1, add_d(sc3(2, Xtu), -mp_rat(32, 15) * g12 * m1sq - mp_rat(32, 3) * g32 * m3sq - mp_rat(4, 5) * g12 * S_fi))
    dmd_r = sc3(inv1, add_d(sc3(2, Xtd), -mp_rat(8, 15) * g12 * m1sq - mp_rat(32, 3) * g32 * m3sq + mp_rat(2, 5) * g12 * S_fi))
    dmL = sc3(inv1, add_d(add3(Xe, Xn) if has_nr else Xe, -mp_rat(6, 5) * g12 * m1sq - 6 * g22 * m2sq - mp_rat(3, 5) * g12 * S_fi))
    dme_r = sc3(inv1, add_d(sc3(2, Xte), -mp_rat(24, 5) * g12 * m1sq + mp_rat(6, 5) * g12 * S_fi))
    dmN_r = sc3(2 * inv1, Xtn) if has_nr else Z
    return (dg, dyu, dyd, dye, dyn, dmr, dkap, dmg, dTu, dTd, dTe, dTn, dmu, dbmu, dmHu2, dmHd2, dmQ, dmu_r, dmd_r, dmL, dme_r, dmN_r)


def rhs_sm_1hdm(st: tuple, scale_factor: mp.mpf = mp.mpf(1)) -> tuple:
    inv1 = scale_factor / (16 * (mp.pi ** 2))
    inv2 = scale_factor / ((16 * (mp.pi ** 2)) ** 2)
    g, yu, yd, ye, kap, lam, mh2 = st
    g12, g22, g32 = g[0] ** 2, g[1] ** 2, g[2] ** 2
    hu, hd, he = hmul(yu), hmul(yd), hmul(ye)
    hu2, hd2, he2 = mul3(hu, hu), mul3(hd, hd), mul3(he, he)
    huhd, hdhu = mul3(hu, hd), mul3(hd, hu)
    tru, trd, tre = tr3(hu), tr3(hd), tr3(he)
    tru2, trd2, tre2, trud = tr3(hu2), tr3(hd2), tr3(he2), tr3(huhd)
    T = 3 * tru + 3 * trd + tre
    T2 = 3 * tru2 + 3 * trd2 + tre2 - mp_rat(2, 3) * trud
    Tg = (mp_rat(17, 20) * g12 + mp_rat(9, 4) * g22 + 8 * g32) * tru + (mp_rat(1, 4) * g12 + mp_rat(9, 4) * g22 + 8 * g32) * trd + (mp_rat(3, 4) * g12 + mp_rat(3, 4) * g22) * tre

    b1 = (mp_rat(41, 10), mp_rat(-19, 6), mp.mpf(-7))
    B2 = (
        (mp_rat(199, 50), mp_rat(27, 10), mp_rat(44, 5)),
        (mp_rat(9, 10), mp_rat(35, 6), mp.mpf(12)),
        (mp_rat(11, 10), mp_rat(9, 2), mp.mpf(-26)),
    )
    Cf = (mp_rat(17, 10) * tru + mp_rat(1, 2) * trd + mp_rat(3, 2) * tre, mp_rat(3, 2) * (tru + trd) + mp_rat(1, 2) * tre, 2 * (tru + trd))
    dg = [inv1 * b1[a] * (g[a] ** 3) + inv2 * (g[a] ** 3) * (B2[a][0] * g12 + B2[a][1] * g22 + B2[a][2] * g32 - Cf[a]) for a in range(3)]

    d_u = inv1 * (T - mp_rat(17, 20) * g12 - mp_rat(9, 4) * g22 - 8 * g32) + inv2 * (
        -mp_rat(9, 4) * T2 + 6 * lam * lam + mp_rat(5, 2) * Tg + mp_rat(1187, 600) * g12 * g12 - mp_rat(9, 20) * g12 * g22 + mp_rat(19, 15) * g12 * g32 - mp_rat(23, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
    )
    d_d = inv1 * (T - mp_rat(1, 4) * g12 - mp_rat(9, 4) * g22 - 8 * g32) + inv2 * (
        -mp_rat(9, 4) * T2 + 6 * lam * lam + mp_rat(5, 2) * Tg - mp_rat(127, 600) * g12 * g12 - mp_rat(27, 20) * g12 * g22 + mp_rat(31, 15) * g12 * g32 - mp_rat(23, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
    )
    d_e = inv1 * (T - mp_rat(9, 4) * g12 - mp_rat(9, 4) * g22) + inv2 * (
        -mp_rat(9, 4) * T2 + 6 * lam * lam + mp_rat(5, 2) * Tg + mp_rat(1371, 200) * g12 * g12 + mp_rat(27, 20) * g12 * g22 - mp_rat(23, 4) * g22 * g22
    )

    au1 = mp_rat(3, 2) * inv1 + inv2 * (-mp_rat(9, 4) * T - 12 * lam + mp_rat(223, 80) * g12 + mp_rat(135, 16) * g22 + 16 * g32)
    au2 = -mp_rat(3, 2) * inv1 + inv2 * (mp_rat(5, 4) * T - mp_rat(43, 80) * g12 + mp_rat(9, 16) * g22 - 16 * g32)
    ad1 = mp_rat(3, 2) * inv1 + inv2 * (-mp_rat(9, 4) * T - 12 * lam + mp_rat(187, 80) * g12 + mp_rat(135, 16) * g22 + 16 * g32)
    ad2 = -mp_rat(3, 2) * inv1 + inv2 * (mp_rat(5, 4) * T - mp_rat(79, 80) * g12 + mp_rat(9, 16) * g22 - 16 * g32)
    ae1 = mp_rat(3, 2) * inv1 + inv2 * (-mp_rat(9, 4) * T - 12 * lam + mp_rat(387, 80) * g12 + mp_rat(135, 16) * g22)

    ku = [[au1 * hu[r][c] + au2 * hd[r][c] + inv2 * (mp_rat(3, 2) * hu2[r][c] - hdhu[r][c] - mp_rat(1, 4) * huhd[r][c] + mp_rat(11, 4) * hd2[r][c]) + (d_u if r == c else Z0_C) for c in range(3)] for r in range(3)]
    kd = [[ad1 * hd[r][c] + ad2 * hu[r][c] + inv2 * (mp_rat(3, 2) * hd2[r][c] - huhd[r][c] - mp_rat(1, 4) * hdhu[r][c] + mp_rat(11, 4) * hu2[r][c]) + (d_d if r == c else Z0_C) for c in range(3)] for r in range(3)]
    ke = [[ae1 * he[r][c] + inv2 * mp_rat(3, 2) * he2[r][c] + (d_e if r == c else Z0_C) for c in range(3)] for r in range(3)]
    dyu, dyd, dye = mul3(ku, yu), mul3(kd, yd), mul3(ke, ye)

    he_kap = add3(mul3(he, kap), mul3(kap, tp3(he)))
    dk_s = 2 * T - 3 * g22 + 4 * lam
    dkap = [[inv1 * (-mp_rat(3, 2) * he_kap[r][c] + dk_s * kap[r][c]) for c in range(3)] for r in range(3)]

    hu3, hd3, he3 = tr3(mul3(hu2, hu)), tr3(mul3(hd2, hd)), tr3(mul3(he2, he))
    tr_uhdh = tr3(mul3(huhd, add3(hu, hd)))
    b1_lam = 24 * lam * lam + 4 * lam * T - 2 * (3 * tru2 + 3 * trd2 + tre2) - lam * (mp_rat(9, 5) * g12 + 9 * g22) + mp_rat(27, 200) * g12 * g12 + mp_rat(9, 20) * g12 * g22 + mp_rat(9, 8) * g22 * g22
    b2_lam = (
        -312 * (lam ** 3) + mp_rat(108, 5) * lam * lam * (g12 + 5 * g22) - 48 * lam * lam * T
        + lam * (mp_rat(1887, 200) * g12 * g12 + mp_rat(117, 20) * g12 * g22 - mp_rat(73, 8) * g22 * g22)
        - lam * (3 * tru2 + 3 * trd2 + tre2) - 42 * lam * trud + 80 * lam * g32 * (tru + trd)
        + mp_rat(9, 2) * lam * g22 * T + mp_rat(1, 2) * lam * g12 * (17 * tru + 5 * trd + 15 * tre)
        - mp_rat(3411, 2000) * (g12 ** 3) - mp_rat(1677, 400) * g12 * g12 * g22 - mp_rat(289, 80) * g12 * g22 * g22 + mp_rat(305, 16) * (g22 ** 3)
        - g12 * g12 * (mp_rat(171, 100) * tru - mp_rat(9, 20) * trd + mp_rat(9, 4) * tre)
        + mp_rat(3, 10) * g12 * g22 * (21 * tru + 9 * trd + 11 * tre) - mp_rat(3, 4) * g22 * g22 * T
        - mp_rat(4, 5) * g12 * (2 * tru2 - trd2 + 3 * tre2) - 32 * g32 * (tru2 + trd2) + 10 * (3 * hu3 + 3 * hd3 + he3) - 6 * tr_uhdh
    )
    dlam = inv1 * b1_lam + inv2 * b2_lam
    dmh2 = inv1 * (12 * lam + 2 * T - mp_rat(9, 10) * g12 - mp_rat(9, 2) * g22) * mh2
    return (dg, dyu, dyd, dye, dkap, dlam, dmh2)


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


def rk4_gen(st: tuple, dt: mp.mpf, fn, *args) -> tuple:
    k1 = fn(st, *args)
    k2 = fn(add_st_gen(st, k1, dt / 2), *args)
    k3 = fn(add_st_gen(st, k2, dt / 2), *args)
    k4 = fn(add_st_gen(st, k3, dt), *args)
    return add_st_gen(st, add_st_gen(add_st_gen(k1, k2, mp.mpf(2)), add_st_gen(k3, k4, mp_rat(1, 2)), mp.mpf(2)), dt / 6)


def rich_gen(st: tuple, dt: mp.mpf, fn, *args) -> tuple:
    sf = rk4_gen(st, dt, fn, *args)
    sh = rk4_gen(rk4_gen(st, dt / 2, fn, *args), dt / 2, fn, *args)
    return add_st_gen(sf, add_st_gen(sh, sf, mp.mpf(-1)), mp_rat(16, 15))


# ==============================================================================
# E1: Literature Benchmark Gate (Martin-Vaughn Supergraph + Luo-Xiao Criticality)
# ==============================================================================
def verify_e1_literature_benchmarks() -> dict[str, object]:
    # 1a. N=1 Supergraph Casimir Anomalous-Dimension Engine vs Expanded Martin-Vaughn:
    # Quadratic Casimirs C_a(i) = (3/5 Y^2, C_2, C_3) and Dynkin indices S_a(i) per generation (or per doublet for H_u, H_d):
    c_rep = {
        "Q": (Fr(1, 60), Fr(3, 4), Fr(4, 3)),
        "uc": (Fr(4, 15), Fr(0), Fr(4, 3)),
        "dc": (Fr(1, 15), Fr(0), Fr(4, 3)),
        "L": (Fr(3, 20), Fr(3, 4), Fr(0)),
        "ec": (Fr(3, 5), Fr(0), Fr(0)),
        "Nc": (Fr(0), Fr(0), Fr(0)),
        "Hu": (Fr(3, 20), Fr(3, 4), Fr(0)),
        "Hd": (Fr(3, 20), Fr(3, 4), Fr(0)),
    }
    s_dyn_per_flav = {
        "Q": (Fr(1, 10), Fr(3, 2), Fr(1)),
        "uc": (Fr(4, 5), Fr(0), Fr(1, 2)),
        "dc": (Fr(1, 5), Fr(0), Fr(1, 2)),
        "L": (Fr(3, 10), Fr(1, 2), Fr(0)),
        "ec": (Fr(3, 5), Fr(0), Fr(0)),
        "Nc": (Fr(0), Fr(0), Fr(0)),
    }
    s_higgs = {
        "Hu": (Fr(3, 10), Fr(1, 2), Fr(0)),
        "Hd": (Fr(3, 10), Fr(1, 2), Fr(0)),
    }
    c_adj = (Fr(0), Fr(2), Fr(3))
    s_tot = [
        3 * sum(s_dyn_per_flav[f][a] for f in s_dyn_per_flav) + sum(s_higgs[h][a] for h in s_higgs)
        for a in range(3)
    ]
    b1_cas = [s_tot[a] - 3 * c_adj[a] for a in range(3)]
    b2_cas = [
        [
            (2 * c_adj[a] * b1_cas[a] if a == b else Fr(0))
            + 4 * (3 * sum(s_dyn_per_flav[f][a] * c_rep[f][b] for f in s_dyn_per_flav) + sum(s_higgs[h][a] * c_rep[h][b] for h in s_higgs))
            for b in range(3)
        ]
        for a in range(3)
    ]

    def g4_diag_cas(field: str, gv2: list[mp.mpf]) -> mp.mpf:
        tot = mp.mpf(0)
        for a in range(3):
            ca = f2m(c_rep[field][a])
            tot += 2 * (gv2[a] ** 2) * (ca * f2m(s_tot[a]) + 2 * ca * ca - 3 * f2m(c_adj[a]) * ca)
            for b in range(3):
                if a != b:
                    tot += 4 * gv2[a] * gv2[b] * ca * f2m(c_rep[field][b])
        return tot

    def yg_shift(ext_f: str, int_f1: str, int_f2: str, gv2: list[mp.mpf]) -> mp.mpf:
        return sum(2 * gv2[a] * f2m(c_rep[int_f1][a] + c_rep[int_f2][a] - c_rep[ext_f][a]) for a in range(3))

    g_t = [mp_rat(3, 7), mp_rat(4, 9), mp_rat(5, 6)]
    g2_t = [x * x for x in g_t]
    yu_t = [[mp_rat(1, 7), mp_rat(1, 11) + I_MP * mp_rat(1, 13), Z0_C], [mp_rat(1, 9), mp_rat(2, 7), mp_rat(1, 8)], [Z0_C, mp_rat(1, 15), mp_rat(3, 5)]]
    yd_t = [[mp_rat(1, 8), -mp_rat(1, 12), mp_rat(1, 19)], [mp_rat(1, 10), mp_rat(1, 4) - I_MP * mp_rat(1, 17), Z0_C], [mp_rat(1, 14), mp_rat(1, 16), mp_rat(2, 5)]]
    ye_t = [[mp_rat(1, 15), mp_rat(1, 23), Z0_C], [Z0_C, mp_rat(1, 9), I_MP * mp_rat(1, 21)], [mp_rat(1, 18), Z0_C, mp_rat(3, 10)]]
    yn_t = [[mp_rat(1, 11), Z0_C, mp_rat(1, 17)], [I_MP * mp_rat(1, 19), mp_rat(1, 6), Z0_C], [Z0_C, mp_rat(1, 12), mp_rat(1, 3)]]
    mr_t = [[mp_rat(2, 5), mp_rat(1, 13), Z0_C], [mp_rat(1, 13), mp_rat(3, 5), I_MP * mp_rat(1, 17)], [Z0_C, I_MP * mp_rat(1, 17), mp_rat(9, 10)]]
    kap_t = [[mp_rat(1, 5), mp_rat(1, 11) + I_MP * mp_rat(1, 19), Z0_C], [mp_rat(1, 11) + I_MP * mp_rat(1, 19), mp_rat(2, 7), mp_rat(1, 15)], [Z0_C, mp_rat(1, 15), mp_rat(1, 2)]]
    Z = z3l()
    st_nr = (g_t, yu_t, yd_t, ye_t, yn_t, mr_t, Z, [mp_rat(1, 3)] * 3, yu_t, yd_t, ye_t, yn_t, mp_rat(1, 2), mp_rat(1, 4), mp_rat(1, 5), mp_rat(1, 6), i3l(), i3l(), i3l(), i3l(), i3l(), i3l())
    st_kp = (g_t, yu_t, yd_t, ye_t, Z, Z, kap_t, [mp_rat(1, 3)] * 3, yu_t, yd_t, ye_t, Z, mp_rat(1, 2), mp_rat(1, 4), mp_rat(1, 5), mp_rat(1, 6), i3l(), i3l(), i3l(), i3l(), i3l(), i3l())

    exp_nr = rhs_mssm(st_nr, True, False)
    exp_nr_bug = rhs_mssm(st_nr, True, True)
    exp_kp = rhs_mssm(st_kp, False, False)

    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1

    def casimir_supergraph_eval(has_n: bool):
        yn_loc = yn_t if has_n else Z
        hu, hd, he, hn = hmul(yu_t), hmul(yd_t), hmul(ye_t), (hmul(yn_loc) if has_n else Z)
        htu, htd, hte, htn = htmul(yu_t), htmul(yd_t), htmul(ye_t), (htmul(yn_loc) if has_n else Z)
        gY_1 = {
            "Q": add3(hu, hd), "uc": sc3(2, htu), "dc": sc3(2, htd),
            "L": add3(he, hn), "ec": sc3(2, hte), "Nc": sc3(2, htn),
            "Hu": 3 * tr3(hu) + tr3(hn), "Hd": 3 * tr3(hd) + tr3(he),
        }
        dg_cas = []
        for a in range(3):
            yuk_fb = 2 * (
                sum(f2m(s_dyn_per_flav[f][a]) * tr3(gY_1[f]) for f in s_dyn_per_flav)
                + f2m(s_higgs["Hu"][a]) * gY_1["Hu"] + f2m(s_higgs["Hd"][a]) * gY_1["Hd"]
            )
            dg_cas.append(inv1 * f2m(b1_cas[a]) * (g_t[a] ** 3) + inv2 * (g_t[a] ** 3) * (sum(f2m(b2_cas[a][b]) * g2_t[b] for b in range(3)) - yuk_fb))

        g1_f = {}
        for f in ("Q", "uc", "dc", "L", "ec", "Nc"):
            gc = -2 * sum(f2m(c_rep[f][a]) * g2_t[a] for a in range(3))
            g1_f[f] = [[gY_1[f][r][c] + (gc if r == c else Z0_C) for c in range(3)] for r in range(3)]
        g1_Hu = gY_1["Hu"] - 2 * sum(f2m(c_rep["Hu"][a]) * g2_t[a] for a in range(3))
        g1_Hd = gY_1["Hd"] - 2 * sum(f2m(c_rep["Hd"][a]) * g2_t[a] for a in range(3))

        # 2-loop gamma_i^{(2)} directly from internal-line insertion -(gamma_m^{(Y)} + gamma_n^{(Y)}) + yg_shift + g4_diag_cas:
        add_diag = lambda M, d: [[M[r][c] + (d if r == c else Z0_C) for c in range(3)] for r in range(3)]
        g2_Q = add_diag(
            add3(
                sub3(sc3(yg_shift("Q", "uc", "Hu", g2_t) - gY_1["Hu"], hu), mul3(yu_t, mul3(gY_1["uc"], dag3(yu_t)))),
                sub3(sc3(yg_shift("Q", "dc", "Hd", g2_t) - gY_1["Hd"], hd), mul3(yd_t, mul3(gY_1["dc"], dag3(yd_t)))),
            ),
            g4_diag_cas("Q", g2_t),
        )
        g2_uc = add_diag(sub3(sc3(yg_shift("uc", "Q", "Hu", g2_t) - gY_1["Hu"], gY_1["uc"]), sc3(2, mul3(dag3(yu_t), mul3(gY_1["Q"], yu_t)))), g4_diag_cas("uc", g2_t))
        g2_dc = add_diag(sub3(sc3(yg_shift("dc", "Q", "Hd", g2_t) - gY_1["Hd"], gY_1["dc"]), sc3(2, mul3(dag3(yd_t), mul3(gY_1["Q"], yd_t)))), g4_diag_cas("dc", g2_t))
        g2_L = add_diag(
            add3(
                sub3(sc3(yg_shift("L", "ec", "Hd", g2_t) - gY_1["Hd"], he), mul3(ye_t, mul3(gY_1["ec"], dag3(ye_t)))),
                sub3(sc3(yg_shift("L", "Nc", "Hu", g2_t) - gY_1["Hu"], hn), mul3(yn_loc, mul3(gY_1["Nc"], dag3(yn_loc)))),
            ),
            g4_diag_cas("L", g2_t),
        )
        g2_ec = add_diag(sub3(sc3(yg_shift("ec", "L", "Hd", g2_t) - gY_1["Hd"], gY_1["ec"]), sc3(2, mul3(dag3(ye_t), mul3(gY_1["L"], ye_t)))), g4_diag_cas("ec", g2_t))
        g2_Nc = add_diag(sub3(sc3(yg_shift("Nc", "L", "Hu", g2_t) - gY_1["Hu"], gY_1["Nc"]), sc3(2, mul3(dag3(yn_loc), mul3(gY_1["L"], yn_loc)))), g4_diag_cas("Nc", g2_t))
        g2_Hu = (
            -3 * tr3(mul3(gY_1["Q"], hu)) - 3 * tr3(mul3(gY_1["uc"], htu))
            - tr3(mul3(gY_1["L"], hn)) - tr3(mul3(gY_1["Nc"], htn))
            + yg_shift("Hu", "Q", "uc", g2_t) * (3 * tr3(hu)) + yg_shift("Hu", "L", "Nc", g2_t) * tr3(hn)
            + g4_diag_cas("Hu", g2_t)
        )
        g2_Hd = (
            -3 * tr3(mul3(gY_1["Q"], hd)) - 3 * tr3(mul3(gY_1["dc"], htd))
            - tr3(mul3(gY_1["L"], he)) - tr3(mul3(gY_1["ec"], hte))
            + yg_shift("Hd", "Q", "dc", g2_t) * (3 * tr3(hd)) + yg_shift("Hd", "L", "ec", g2_t) * tr3(he)
            + g4_diag_cas("Hd", g2_t)
        )

        gam = {k: add3(sc3(inv1, g1_f[k]), sc3(inv2, v)) for k, v in [("Q", g2_Q), ("uc", g2_uc), ("dc", g2_dc), ("L", g2_L), ("ec", g2_ec), ("Nc", g2_Nc)]}
        gam_Hu = inv1 * g1_Hu + inv2 * g2_Hu
        gam_Hd = inv1 * g1_Hd + inv2 * g2_Hd

        dyu_c = add3(mul3(add_diag(gam["Q"], gam_Hu), yu_t), mul3(yu_t, gam["uc"]))
        dyd_c = add3(mul3(add_diag(gam["Q"], gam_Hd), yd_t), mul3(yd_t, gam["dc"]))
        dye_c = add3(mul3(add_diag(gam["L"], gam_Hd), ye_t), mul3(ye_t, gam["ec"]))
        dyn_c = add3(mul3(add_diag(gam["L"], gam_Hu), yn_loc), mul3(yn_loc, gam["Nc"])) if has_n else Z
        dmr_c = add3(mul3(tp3(gam["Nc"]), mr_t), mul3(mr_t, gam["Nc"])) if has_n else Z
        gL_Hu = add_diag(gam["L"], gam_Hu)
        dkap_c = Z if has_n else add3(mul3(gL_Hu, kap_t), mul3(kap_t, tp3(gL_Hu)))
        return dg_cas, dyu_c, dyd_c, dye_c, dyn_c, dmr_c, dkap_c

    cas_nr = casimir_supergraph_eval(True)
    cas_kp = casimir_supergraph_eval(False)
    supergraph_max_err = max(
        max(abs(exp_nr[0][i] - cas_nr[0][i]) for i in range(3)),
        max(max_diff3(exp_nr[idx], cas_nr[idx]) for idx in (1, 2, 3, 4, 5)),
        max_diff3(exp_kp[6], cas_kp[6]),
    )
    inv2_v = (1 / (16 * (mp.pi ** 2))) ** 2
    transposed_huhd_err = max_diff3(exp_nr[1], exp_nr_bug[1]) / inv2_v
    ctrl1_caught = bool(supergraph_max_err < mp.mpf(10) ** (-48) and transposed_huhd_err > mp.mpf(10) ** (-3))
    assert ctrl1_caught

    # 1b. Exact rational Luo-Xiao beta_lam^{(2)} == 16142087/800000 & upward lambda(t_crit^*) == 0 criticality:
    hu_r = [Fr(1, 100), Fr(1, 25), Fr(1, 1)]
    hd_r = [Fr(1, 400), Fr(1, 100), Fr(1, 4)]
    he_r = [Fr(1, 400), Fr(1, 100), Fr(1, 4)]
    g12_r, g22_r, g32_r, lam_r = Fr(1, 4), Fr(1, 4), Fr(1, 4), Fr(1, 10)
    tru_r, trd_r, tre_r = sum(hu_r), sum(hd_r), sum(he_r)
    tru2_r, trd2_r, tre2_r = sum(x * x for x in hu_r), sum(x * x for x in hd_r), sum(x * x for x in he_r)
    hu3_r, hd3_r, he3_r = sum(x ** 3 for x in hu_r), sum(x ** 3 for x in hd_r), sum(x ** 3 for x in he_r)
    trud_r = sum(hu_r[i] * hd_r[i] for i in range(3))
    tr_uhdh_r = sum(hu_r[i] * hd_r[i] * (hu_r[i] + hd_r[i]) for i in range(3))
    t_r = 3 * tru_r + 3 * trd_r + tre_r
    b_lam2_exact = (
        -312 * (lam_r ** 3) + Fr(108, 5) * lam_r * lam_r * (g12_r + 5 * g22_r) - 48 * lam_r * lam_r * t_r
        + lam_r * (Fr(1887, 200) * g12_r * g12_r + Fr(117, 20) * g12_r * g22_r - Fr(73, 8) * g22_r * g22_r)
        - lam_r * (3 * tru2_r + 3 * trd2_r + tre2_r) - 42 * lam_r * trud_r + 80 * lam_r * g32_r * (tru_r + trd_r)
        + Fr(9, 2) * lam_r * g22_r * t_r + Fr(1, 2) * lam_r * g12_r * (17 * tru_r + 5 * trd_r + 15 * tre_r)
        - Fr(3411, 2000) * (g12_r ** 3) - Fr(1677, 400) * g12_r * g12_r * g22_r - Fr(289, 80) * g12_r * g22_r * g22_r + Fr(305, 16) * (g22_r ** 3)
        - g12_r * g12_r * (Fr(171, 100) * tru_r - Fr(9, 20) * trd_r + Fr(9, 4) * tre_r)
        + Fr(3, 10) * g12_r * g22_r * (21 * tru_r + 9 * trd_r + 11 * tre_r) - Fr(3, 4) * g22_r * g22_r * t_r
        - Fr(4, 5) * g12_r * (2 * tru2_r - trd2_r + 3 * tre2_r) - 32 * g32_r * (tru2_r + trd2_r)
        + 10 * (3 * hu3_r + 3 * hd3_r + he3_r) - 6 * tr_uhdh_r
    )
    assert b_lam2_exact == Fr(16142087, 800000)

    # Synthetic rational upward lambda(t_crit^*) == 0 benchmark:
    yu_c0 = [[Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, Z0_C], [Z0_C, Z0_C, mp.mpc(1)]]
    st_c0 = ([mp_rat(1, 2), mp_rat(1, 2), mp.mpf(1)], yu_c0, z3l(), z3l(), z3l(), mp_rat(1, 8), mp.mpf(1))

    def lam_at_rk4(t_end: mp.mpf, n_st: int, sc_f: mp.mpf = mp.mpf(1)) -> mp.mpf:
        s = st_c0
        dt = t_end / n_st
        for _ in range(n_st):
            s = rich_gen(s, dt, rhs_sm_1hdm, sc_f)
        return s[5]

    def lam_at_gl4(t_end: mp.mpf, n_st: int) -> mp.mpf:
        s = st_c0
        h = t_end / n_st
        sr3 = mp.sqrt(mp.mpf(3))
        a11, a12, a21, a22 = mp_rat(1, 4), mp_rat(1, 4) - sr3 / 6, mp_rat(1, 4) + sr3 / 6, mp_rat(1, 4)
        for _ in range(n_st):
            k1 = rhs_sm_1hdm(s)
            k2 = k1
            for _ in range(10):
                k1 = rhs_sm_1hdm(add_st_gen(add_st_gen(s, k1, h * a11), k2, h * a12))
                k2 = rhs_sm_1hdm(add_st_gen(add_st_gen(s, k1, h * a21), k2, h * a22))
            s = add_st_gen(s, add_st_gen(k1, k2, mp.mpf(1)), h / 2)
        return s[5]

    def secant_crit(fn_lam) -> mp.mpf:
        ta, tb = mp.mpf(4), mp.mpf(5)
        fa, fb = fn_lam(ta), fn_lam(tb)
        for _ in range(10):
            if abs(fb) < mp.mpf(10) ** (-30) or abs(fb - fa) == 0:
                break
            ta, fa, tb = tb, fb, tb - fb * (tb - ta) / (fb - fa)
            fb = fn_lam(tb)
        return tb

    t_crit_rk4 = secant_crit(lambda tv: lam_at_rk4(tv, 24, mp.mpf(1)))
    t_crit_gl4 = secant_crit(lambda tv: (16 * lam_at_gl4(tv, 24) - lam_at_gl4(tv, 12)) / 15)
    t_crit_bad_dlnmu2 = secant_crit(lambda tv: lam_at_rk4(tv, 24, mp_rat(1, 2)))
    crit_rk4_vs_gl4_err = abs(t_crit_rk4 - t_crit_gl4)
    crit_dlnmu2_shift = abs(t_crit_bad_dlnmu2 - t_crit_rk4)
    ctrl2_caught = bool(b_lam2_exact == Fr(16142087, 800000) and crit_rk4_vs_gl4_err < mp.mpf(10) ** (-11) and crit_dlnmu2_shift > mp.mpf(2))
    assert ctrl2_caught

    return {
        "mssm_supergraph_vs_expanded_max_err": mp.nstr(supergraph_max_err, 8),
        "transposed_huhd_2loop_scaled_err": mp.nstr(transposed_huhd_err, 10),
        "exact_rational_sm_beta_lam_2": f"{b_lam2_exact.numerator}/{b_lam2_exact.denominator}",
        "sm_criticality_t_star_rk4": mp.nstr(t_crit_rk4, 16),
        "sm_criticality_rk4_vs_gl4_abs_err": mp.nstr(crit_rk4_vs_gl4_err, 8),
        "sm_criticality_dlnmu2_factor2_shift": mp.nstr(crit_dlnmu2_shift, 10),
        "control_1_mssm_noncomm_order_caught": ctrl1_caught,
        "control_2_sm_criticality_and_dlnmu2_caught": ctrl2_caught,
    }


# ==============================================================================
# E2 & E3: Self-Consistent Three-Stage MSSM -> SM Pipeline
# ==============================================================================
@dataclass(frozen=True)
class UVBoundary3:
    delta_H: mp.mpf
    c_mu: mp.mpf
    c_B: mp.mpf


def default_uv_boundary_3() -> UVBoundary3:
    return UVBoundary3(mp.mpf(12), mp_rat(3, 2), mp_rat(-19, 12))


def svd_asc_mp(m: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    ev, u = mp.eighe(m * m.H)
    order = sorted(range(3), key=lambda k: mp.re(ev[k]))
    s_vals = [mp.sqrt(max(mp.re(ev[i]), mp.mpf(0))) for i in order]
    u_asc = mp.matrix([[u[r, order[c]] for c in range(3)] for r in range(3)])
    return u_asc, s_vals


def takagi_sym3(mr_m: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
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


def eval_topdown_3stage_pipeline(
    uv_mats: tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    l2_tau8: mp.mpf,
    uv3: UVBoundary3,
    n_steps: int = 120,
    mu_gut_anchor: mp.mpf = mp.mpf(1),
    unscaled_bad_anchor: bool = False,
    euler_coarse: bool = False,
    fixed_horizons: tuple[mp.mpf, mp.mpf, mp.mpf] | None = None,
) -> tuple[dict[str, dict[str, mp.mpf]], dict[str, mp.mpf], tuple[mp.mpf, mp.mpf, mp.mpf], mp.mpf, mp.mpf]:
    mu0 = mp.mpf(mu_gut_anchor)
    n1 = max(2, (3 * n_steps) // 10)
    n2 = max(2, (13 * n_steps) // 20)
    n3 = max(2, n_steps - n1 - n2)

    g0 = mp.sqrt(mp.pi / 6)
    m0_maj = (mp.mpf(1) if unscaled_bad_anchor else mu0) * mp.exp(-mp_rat(16, 5) * mp.pi)
    m32 = mu0 * mp.exp(-mp_rat(48, 5) * mp.pi)
    sr3 = mp.sqrt(mp.mpf(3))
    mg0 = [sr3 * m32, sr3 * m32, sr3 * m32]
    m02 = m32 * m32
    a0 = -sr3 * m32
    mu_uv = uv3.c_mu * m32
    bmu_uv = uv3.c_B * m32 * mu_uv

    yu0, yd0, ye0, yn0, cr0 = [to3(m) for m in uv_mats]
    Z = z3l()
    I_m02 = i3l(m02)
    st0 = (
        [g0, g0, g0], yu0, yd0, ye0, yn0, sc3(m0_maj, cr0), Z,
        mg0, sc3(a0, yu0), sc3(a0, yd0), sc3(a0, ye0), sc3(a0, yn0),
        mu_uv, bmu_uv, m02, m02 * (1 + uv3.delta_H),
        I_m02, I_m02, I_m02, I_m02, I_m02, I_m02,
    )

    def int_stage(s_init: tuple, dt_tot: mp.mpf, ns: int, fn, *args) -> tuple:
        s = s_init
        dt = dt_tot / ns
        for _ in range(ns):
            s = add_st_gen(s, fn(s, *args), dt) if euler_coarse else rich_gen(rich_gen(s, dt / 2, fn, *args), dt / 2, fn, *args)
        return s

    # Stage I: [0, t_nu^*]
    def eval_stage1(tv: mp.mpf, ns: int):
        s = int_stage(st0, tv, ns, rhs_mssm, True, False)
        mmaj, utak = takagi_sym3(fr3(s[5]))
        return mp.log(mmaj[0] / mu0) - tv, s, mmaj, utak

    def solve_fp_secant(t_seed: mp.mpf, n_full: int, eval_fn):
        nc = min(n_full, 6) if not euler_coarse else n_full
        r0, *pay = eval_fn(t_seed, nc)
        t0, t1 = t_seed, t_seed + r0
        if not euler_coarse:
            for _ in range(5):
                r1, *pay = eval_fn(t1, nc)
                if abs(r1) < mp.mpf(10) ** (-30) or abs(r1 - r0) == 0:
                    break
                t0, r0, t1 = t1, r1, t1 - r1 * (t1 - t0) / (r1 - r0)
            if n_full > nc:
                t0 = t1
                r0, *pay = eval_fn(t0, n_full)
                t1 = t0 + r0
                for _ in range(3):
                    if abs(r0) < mp.mpf(10) ** (-30):
                        break
                    r1, *pay = eval_fn(t1, n_full)
                    if abs(r1) < mp.mpf(10) ** (-30) or abs(r1 - r0) == 0:
                        break
                    t0, r0, t1 = t1, r1, t1 - r1 * (t1 - t0) / (r1 - r0)
                _, *pay = eval_fn(t1, n_full)
            else:
                _, *pay = eval_fn(t1, n_full)
        else:
            _, *pay = eval_fn(t1, n_full)
        return t1, pay

    if fixed_horizons is None:
        t_nu_star, (s_tnu, mmaj_tnu, utak_tnu) = solve_fp_secant(mp.log(m0_maj / mu0), n1, eval_stage1)
    else:
        t_nu_star = fixed_horizons[0]
        _, s_tnu, mmaj_tnu, utak_tnu = eval_stage1(t_nu_star, n1)

    yn_tnu_m, mr_tnu_m = fr3(s_tnu[4]), fr3(s_tnu[5])
    kap_mssm0 = to3(-yn_tnu_m * (mr_tnu_m ** (-1)) * yn_tnu_m.T)
    st1 = (
        s_tnu[0], s_tnu[1], s_tnu[2], s_tnu[3], Z, Z, kap_mssm0,
        s_tnu[7], s_tnu[8], s_tnu[9], s_tnu[10], Z,
        s_tnu[12], s_tnu[13], s_tnu[14], s_tnu[15],
        s_tnu[16], s_tnu[17], s_tnu[18], s_tnu[19], s_tnu[20], s_tnu[21],
    )

    # Stage II: [t_nu^*, t_SUSY^*]
    def extract_stop_scale(s_loc: tuple) -> tuple[mp.mpf, mp.mpf, mp.matrix, mp.matrix]:
        yu_m = fr3(s_loc[1])
        u_q, su_l = svd_asc_mp(yu_m)
        yt_m = su_l[2]
        uL3 = u_q[:, 2]
        uR3 = (yu_m.H * uL3) / yt_m
        mtL2 = mp.re((uL3.H * fr3(s_loc[16]) * uL3)[0, 0])
        mtR2 = mp.re((uR3.H * fr3(s_loc[17]) * uR3)[0, 0])
        ms_v = (mtL2 * mtR2) ** mp_rat(1, 4)
        return ms_v, yt_m, uL3, uR3

    def eval_stage2(tv: mp.mpf, ns: int):
        s2 = int_stage(st1, tv - t_nu_star, ns, rhs_mssm, False, False)
        ms_v, yt_m, uL3, uR3 = extract_stop_scale(s2)
        return mp.log(ms_v / mu0) - tv, s2, ms_v, yt_m, uL3, uR3

    if fixed_horizons is None:
        t_susy_star, (s_susy, ms_val, yt_mssm, uL3, uR3) = solve_fp_secant(-mp_rat(48, 5) * mp.pi + mp_rat(5, 4), n2, eval_stage2)
    else:
        t_susy_star = fixed_horizons[1]
        _, s_susy, ms_val, yt_mssm, uL3, uR3 = eval_stage2(t_susy_star, n2)

    # MSSM Radiative EWSB & Threshold Matching at t_SUSY^*:
    m1_sq = mp.re(s_susy[15]) + abs(s_susy[12]) ** 2
    m2_sq = mp.re(s_susy[14]) + abs(s_susy[12]) ** 2
    b_abs = abs(s_susy[13])
    dflat_bfb = m1_sq + m2_sq - 2 * b_abs

    sf_eigs: list[mp.mpf] = []
    for idx_sf in (16, 17, 18, 19, 20):
        evs_sf, _ = mp.eighe(fr3(s_susy[idx_sf]))
        sf_eigs.extend(mp.re(x) for x in evs_sf)
    min_sf_sq = min(sf_eigs)

    s2b = 2 * b_abs / (m1_sq + m2_sq)
    tb = (m1_sq + m2_sq + mp.sqrt((m1_sq + m2_sq) ** 2 - 4 * (b_abs ** 2))) / (2 * b_abs)
    sb = tb / mp.sqrt(1 + tb * tb)
    cb = 1 / mp.sqrt(1 + tb * tb)
    c2b = cb * cb - sb * sb

    At_eff = (uL3.H * fr3(s_susy[8]) * uR3)[0, 0] / yt_mssm
    Xt2 = abs(At_eff - mp.conj(s_susy[12]) / tb) ** 2
    yt_sm_ms = sb * yt_mssm
    dlam_stop = (3 * (yt_sm_ms ** 4) / (16 * (mp.pi ** 2))) * (Xt2 / (ms_val ** 2)) * (1 - Xt2 / (12 * (ms_val ** 2)))
    g12_s, g22_s = s_susy[0][0] ** 2, s_susy[0][1] ** 2
    lam_tree_ms = ((g22_s + mp_rat(3, 5) * g12_s) / 8) * (c2b ** 2)
    lam_sm_ms = lam_tree_ms + dlam_stop
    mh2_sm_ms = b_abs * s2b - m1_sq * (cb ** 2) - m2_sq * (sb ** 2)

    # Decoupled heavy MSSM Higgses (A^0, H^0, H^+-) at M_S:
    v_susy_sq = 8 * (m1_sq - m2_sq * (tb ** 2)) / ((g22_s + mp_rat(3, 5) * g12_s) * (tb * tb - 1))
    mz_susy_sq = mp_rat(1, 4) * (g22_s + mp_rat(3, 5) * g12_s) * v_susy_sq
    mw_susy_sq = mp_rat(1, 4) * g22_s * v_susy_sq
    ma0_sq = m1_sq + m2_sq
    mhpm_sq = ma0_sq + mw_susy_sq
    m0p_mat = mp.matrix([
        [ma0_sq * (sb ** 2) + mz_susy_sq * (cb ** 2), -(ma0_sq + mz_susy_sq) * sb * cb],
        [-(ma0_sq + mz_susy_sq) * sb * cb, ma0_sq * (cb ** 2) + mz_susy_sq * (sb ** 2) + 2 * dlam_stop * v_susy_sq / (sb ** 2)],
    ])
    ev_0p, _ = mp.eighe(m0p_mat)
    mh0_heavy_sq = max(mp.re(x) for x in ev_0p)

    st_sm0 = (
        s_susy[0], sc3(sb, s_susy[1]), sc3(cb, s_susy[2]), sc3(cb, s_susy[3]),
        sc3(sb * sb, s_susy[6]), lam_sm_ms, mh2_sm_ms,
    )

    # Stage III: [t_SUSY^*, t_EW^*]
    def eval_stage3(tv: mp.mpf, ns: int):
        s3 = int_stage(st_sm0, tv - t_susy_star, ns, rhs_sm_1hdm, mp.mpf(1))
        vew_v = mp.sqrt(s3[6] / s3[5])
        return mp.log(vew_v / mu0) - tv, s3, vew_v

    if fixed_horizons is None:
        t_ew_star, (s_ir, vew_dim) = solve_fp_secant(t_susy_star - mp.mpf(1), n3, eval_stage3)
    else:
        t_ew_star = fixed_horizons[2]
        _, s_ir, vew_dim = eval_stage3(t_ew_star, n3)

    gf, yuf_l, ydf_l, yef_l, kapf_l, lam_ir, mh2_ir = s_ir
    mgut_over_vew = mu0 / vew_dim
    horizon_resid = max(
        abs(mp.log(mmaj_tnu[0] / mu0) - t_nu_star),
        abs(mp.log(ms_val / mu0) - t_susy_star),
        abs(mp.log(vew_dim / mu0) - t_ew_star),
    )

    yuf, ydf, yef, kapf = fr3(yuf_l), fr3(ydf_l), fr3(yef_l), fr3(kapf_l)
    uu, su = svd_asc_mp(yuf)
    ud, sd = svd_asc_mp(ydf)
    ue, se = svd_asc_mp(yef)
    un, sn = svd_asc_mp(kapf)
    vc = uu.H * ud
    up = ue.H * un
    jc = abs(mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1])))
    jp = abs(mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1])))
    bar_theta_raw = mp.arg(mp.det(yuf * ydf))

    ia = [(4 * mp.pi) / (x * x) for x in gf]
    gy2, gw2 = mp_rat(3, 5) * (gf[0] ** 2), gf[1] ** 2
    wmix = gy2 / (gw2 + gy2)
    mnu_vew = [mp_rat(1, 2) * s_i * vew_dim for s_i in sn]
    evn = [m_i * m_i for m_i in mnu_vew]

    msbar = {
        "u_m1_over_m3": su[0] / su[2],
        "u_m2_over_m3": su[1] / su[2],
        "d_m1_over_m3": sd[0] / sd[2],
        "d_m2_over_m3": sd[1] / sd[2],
        "e_m1_over_m3": se[0] / se[2],
        "e_m2_over_m3": se[1] / se[2],
        "u3_over_d3": su[2] / sd[2],
        "d3_over_e3": sd[2] / se[2],
        "ckm_v12": abs(vc[0, 1]),
        "ckm_v23": abs(vc[1, 2]),
        "ckm_v13": abs(vc[0, 2]),
        "ckm_jarlskog": jc,
        "pmns_u12": abs(up[0, 1]),
        "pmns_u23": abs(up[1, 2]),
        "pmns_u13": abs(up[0, 2]),
        "pmns_jarlskog": jp,
        "nu_dm21_sq_over_dm31_sq": (evn[1] - evn[0]) / (evn[2] - evn[0]),
        "strong_cp_bar_theta_qcd_raw_rad": bar_theta_raw,
        "gauge_slope_2loop": (ia[0] - ia[1]) / (ia[1] - ia[2]),
        "tan_beta_ewsb": tb,
        "quartic_bfb_margin": lam_ir,
        "electroweak_mix_ratio": wmix,
    }

    mu3_ms = su[2] / mp.sqrt(2)
    mc_ms = su[1] / mp.sqrt(2)
    md3_ms = sd[2] / mp.sqrt(2)
    me3_ms = se[2] / mp.sqrt(2)
    a3_ir = (gf[2] ** 2) / (4 * mp.pi)
    aqed_ir = (gy2 * gw2) / (4 * mp.pi * (gw2 + gy2))
    mu3_pole = mu3_ms * (1 + (a3_ir / mp.pi) * (mp_rat(4, 3) - 2 * mp.log(mu3_ms)))
    me3_pole = me3_ms * (1 + (aqed_ir / mp.pi) * (1 - mp_rat(3, 2) * mp.log(me3_ms)))
    den_5f = 1 + mp_rat(23, 6) * (a3_ir / mp.pi) * mp.log(md3_ms)
    a3_b = a3_ir / den_5f
    md3_low = md3_ms * ((a3_b / a3_ir) ** mp_rat(12, 23))
    md3_pole = md3_low * (1 + mp_rat(4, 3) * (a3_b / mp.pi))

    def run_a3_rich(a_st: mp.mpf, mu_st: mp.mpf, mu_en: mp.mpf, nf_q: int) -> mp.mpf:
        b0_q = mp_rat(33 - 2 * nf_q, 3)
        b1_q = mp_rat(306 - 38 * nf_q, 3)
        rhs_q = lambda x: -(b0_q / (2 * mp.pi)) * (x * x) - (b1_q / (8 * (mp.pi ** 2))) * (x ** 3)

        def rk4_q(n_q: int) -> mp.mpf:
            dt_q = mp.log(mu_en / mu_st) / n_q
            av = a_st
            for _ in range(n_q):
                if euler_coarse:
                    av += dt_q * rhs_q(av)
                else:
                    k1q = dt_q * rhs_q(av)
                    k2q = dt_q * rhs_q(av + k1q / 2)
                    k3q = dt_q * rhs_q(av + k2q / 2)
                    k4q = dt_q * rhs_q(av + k3q)
                    av += (k1q + 2 * k2q + 2 * k3q + k4q) / 6
            return av

        nq_b = max(4, n_steps)
        return rk4_q(nq_b) if euler_coarse else (16 * rk4_q(2 * nq_b) - rk4_q(nq_b)) / 15

    def lam_qcd_2l(mu_q: mp.mpf, av: mp.mpf, nf_q: int) -> mp.mpf:
        b0_q = mp_rat(33 - 2 * nf_q, 3)
        b1_q = mp_rat(306 - 38 * nf_q, 3)
        ex_q = b1_q / (2 * (b0_q ** 2))
        return mu_q * mp.exp(-2 * mp.pi / (b0_q * av)) * (((b0_q * av) / (4 * mp.pi)) ** (-ex_q)) * ((1 + (b1_q * av) / (4 * mp.pi * b0_q)) ** ex_q)

    lam_5f_vew = lam_qcd_2l(mp.mpf(1), a3_ir, 5)
    a3_at_mb = run_a3_rich(a3_ir, mp.mpf(1), md3_ms, 5)
    lam_4f_vew = lam_qcd_2l(md3_ms, a3_at_mb, 4)
    mc_over_lam4f = mc_ms / lam_4f_vew
    if mc_over_lam4f > mp.mpf(1):
        a3_at_mc = run_a3_rich(a3_at_mb, md3_ms, mc_ms, 4)
        lam_3f_vew = lam_qcd_2l(mc_ms, a3_at_mc, 3)
    else:
        lam_3f_vew = mp.mpf(0)

    mz_vew = mp_rat(1, 2) * mp.sqrt(gw2 + gy2)
    mh0_vew = mp.sqrt(2 * lam_ir)
    pole_bosons = {
        "u3_pole_over_vew": mu3_pole,
        "d3_low_over_e3_pole": md3_low / me3_pole,
        "d3_pole_over_e3_pole": md3_pole / me3_pole,
        "strong_coupling_ir": a3_ir,
        "qed_coupling_ir": aqed_ir,
        "qcd_Lambda_5f_over_vew": lam_5f_vew,
        "qcd_Lambda_4f_over_vew": lam_4f_vew,
        "mc_msbar_over_qcd_Lambda_4f": mc_over_lam4f,
        "mw_over_vew": mp_rat(1, 2) * gf[1],
        "mz_over_vew": mz_vew,
        "higgs_h0_over_vew": mh0_vew,
        "higgs_H0_over_vew": mp.sqrt(mh0_heavy_sq) / vew_dim,
        "higgs_A0_over_vew": mp.sqrt(ma0_sq) / vew_dim,
        "higgs_Hpm_over_vew": mp.sqrt(mhpm_sq) / vew_dim,
        "ewsb_vmin_over_vew4": -mp_rat(1, 4) * lam_ir,
    }

    # Exact k = |2T| = 24 11D M-theory reduction: 2 kappa_11^2 T_M2^3 = (2 pi)^2 & V_3 = 8 Vol(m004) M_GUT^-3:
    vol41 = 3 * mp.im(mp.polylog(2, mp.exp(2 * I_MP * mp.pi / 3)))
    m11_mgut = (24 * ((2 * mp.pi) ** 3) / (8 * vol41)) ** mp_rat(1, 3)
    vp_hat = ((2 * mp.pi) ** 4) / 48
    mpl_mgut_sd = mp.sqrt(8 * (m11_mgut ** 5) * (8 * vol41) * vp_hat / ((2 * mp.pi) ** 7))
    mpl_mgut_iso = mp.sqrt(8 * (m11_mgut ** 9) * (8 * vol41) * vp_hat / ((2 * mp.pi) ** 7))
    mbar_pl_mgut_sd = mpl_mgut_sd / mp.sqrt(8 * mp.pi)
    mpl_vew_sd = mpl_mgut_sd * mgut_over_vew
    mpl_vew_iso = mpl_mgut_iso * mgut_over_vew

    grav = {
        "cusp_robin_bc_star_tau8": mp.pi - l2_tau8,
        "m11_over_mgut_zero_knob": m11_mgut,
        "mpl_over_vew_d4_hurwitz_self_dual": mpl_vew_sd,
        "gn_vew_sq_d4_hurwitz_self_dual": 1 / (mpl_vew_sd ** 2),
        "mpl_over_vew_d4_hurwitz_isotropic": mpl_vew_iso,
        "gn_vew_sq_d4_hurwitz_isotropic": 1 / (mpl_vew_iso ** 2),
    }

    # Supersymmetric 2-flavor seesaw leptogenesis at t_nu^* (Covi-Roulet-Vissani PLB 384 (1996) 169 + Abada et al. JHEP 0604 (2006) 004):
    ue_tnu, se_tnu = svd_asc_mp(fr3(s_tnu[3]))
    Yt = ue_tnu.H * yn_tnu_m * utak_tnu
    Ht = Yt.H * Yt
    h00 = mp.re(Ht[0, 0])
    efl = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    for j in (1, 2):
        xv = (mmaj_tnu[j] / mmaj_tnu[0]) ** 2
        gm = mp.re(Ht[j, j]) / (8 * mp.pi)
        dn = (xv - 1) ** 2 + xv * (gm ** 2)
        f_sv = mp.sqrt(xv) * (2 * (1 - xv) / dn - mp.log(1 + 1 / xv))
        g_os = 2 * (1 - xv) / dn
        for al in range(3):
            p1j = mp.conj(Yt[al, 0]) * Yt[al, j]
            efl[al] += (mp.im(p1j * Ht[0, j]) * f_sv + mp.im(p1j * Ht[j, 0]) * g_os) / (8 * mp.pi * h00)
    pbr = [abs(Yt[a, 0]) ** 2 / h00 for a in range(3)]
    g_star_mssm = mp_rat(915, 4)
    m1_over_mgut = mmaj_tnu[0] / mu0
    hub_over_m1 = mp.sqrt((mp.pi ** 2) * g_star_mssm / 90) * (m1_over_mgut / mbar_pl_mgut_sd)
    k1_tot = (h00 / (4 * mp.pi)) / hub_over_m1
    gam_tau_h = (mp_rat(5, 1000) * (se_tnu[2] ** 2)) / hub_over_m1
    eta_tau = 1 / (1 + (pbr[2] * k1_tot) ** mp_rat(29, 25))
    eta_perp = 1 / (1 + ((pbr[0] + pbr[1]) * k1_tot) ** mp_rat(29, 25))
    neq_susy = 2 * (135 * mp.zeta(3)) / (4 * (mp.pi ** 4) * g_star_mssm)
    yb_val = -mp_rat(8, 23) * neq_susy * (efl[2] * eta_tau + (efl[0] + efl[1]) * eta_perp)

    y_end_inf = 1 + 2 / mp.sqrt(mp.mpf(3))
    y_inf = mp.mpf(82)
    for _ in range(20):
        y_inf -= (mp_rat(3, 4) * ((y_inf - y_end_inf) - mp.log(y_inf / y_end_inf)) - 60) / (mp_rat(3, 4) * (1 - 1 / y_inf))
    eps_60 = mp_rat(4, 3) / ((y_inf - 1) ** 2)
    eta_60 = -mp_rat(4, 3) * (y_inf - 2) / ((y_inf - 1) ** 2)

    cosmo = {
        "proton_decay_dim6_mgut_over_vew_pow4": mgut_over_vew ** 4,
        "leptogenesis_Y_B_2flavor_analytic_fit": yb_val,
        "leptogenesis_eps_1_tau": efl[2],
        "leptogenesis_washout_K1_tot": k1_tot,
        "leptogenesis_tau_equil_over_hubble": gam_tau_h,
        "inflation_conformal_S4_ns_N60": 1 - 6 * eps_60 + 2 * eta_60,
        "inflation_conformal_S4_r_N60": 16 * eps_60,
    }

    # SUSY 6D B_{MN} / Svrcek-Witten UV SU(3)_C instanton shift (with 6-gluino-zero-mode chirality factor (|M_3|/mu_0)^3):
    s_uv_qcd = 48 * mp.pi
    det_yu_yd_uv = abs(mp.det(uv_mats[0] * uv_mats[1]))
    gluino_chirality_supp = (abs(mg0[2]) / mu0) ** 3
    log10_dtheta_uv = mp.log10((s_uv_qcd ** 6) * mp.exp(-s_uv_qcd) * gluino_chirality_supp * det_yu_yd_uv * ((mgut_over_vew / lam_4f_vew) ** 4))

    diag_meta = {
        "m1_sq_over_m32_sq": m1_sq / m02,
        "m2_sq_over_m32_sq": m2_sq / m02,
        "dflat_bfb_over_m32_sq": dflat_bfb / m02,
        "min_sfermion_sq_over_m32_sq": min_sf_sq / m02,
        "ms_stop_over_m32": ms_val / m32,
        "mh0_over_mz": mh0_vew / mz_vew,
        "mh0_tree_bound_over_mz": abs(c2b),
        "qcd_Lambda_3f_over_vew": lam_3f_vew,
        "log10_susy_uv_qcd_instanton_shift": log10_dtheta_uv,
    }

    return (
        {
            "sm_msbar_at_ew_horizon": msbar,
            "sm_1loop_pole_and_2hdm_bosons": pole_bosons,
            "gravity_11d_d4_hurwitz_sector": grav,
            "cosmology_crv_and_honest_bounds": cosmo,
        },
        diag_meta,
        (t_nu_star, t_susy_star, t_ew_star),
        vew_dim,
        horizon_resid,
    )


def su3_cayley(seed: int) -> mp.matrix:
    hm = mp.zeros(3, 3)
    for r in range(3):
        hm[r, r] = mp_rat((seed + 2 * r + 1) % 7 - 3, 5)
        for c in range(r + 1, 3):
            zv = mp_rat((3 * seed + r + 2 * c + 1) % 9 - 4, 7) + I_MP * mp_rat((5 * seed + 2 * r + c + 2) % 11 - 5, 9)
            hm[r, c], hm[c, r] = zv, mp.conj(zv)
    i3 = mp.eye(3)
    u0 = (i3 - I_MP * hm) * ((i3 + I_MP * hm) ** (-1))
    return u0 * mp.exp(-I_MP * mp.arg(mp.det(u0)) / 3)


def main() -> None:
    t0 = time.time()
    self_src = Path(__file__).resolve().read_text(encoding="utf-8")
    ast_res = verify_ast_strict(self_src, Path(__file__).name)
    assert ast_res["passed"], f"Self AST check failed: {ast_res}"

    mp.mp.dps = 54
    e1_res = verify_e1_literature_benchmarks()

    mp.mp.dps = 48
    uv_mats, l2_pos = build_layer3_uv_matrices(1)
    uv3 = default_uv_boundary_3()

    out_120, meta_120, horiz_120, vew_1, h_res_120 = eval_topdown_3stage_pipeline(uv_mats, l2_pos, uv3, n_steps=120)
    out_240, meta_240, horiz_240, _, h_res_240 = eval_topdown_3stage_pipeline(uv_mats, l2_pos, uv3, n_steps=240)
    t_nu_s, t_susy_s, t_ew_s = horiz_240
    assert mp.mpf(0) > t_nu_s > t_susy_s > t_ew_s and max(h_res_120, h_res_240) < mp.mpf(10) ** (-24)

    # Planted Control 3: Delta_H = 0 fails D-flat BFB stability (y_b^UV > y_t^UV drives m_1^2 + m_2^2 < 0 at t_SUSY^*)!
    Z = z3l()
    g0 = mp.sqrt(mp.pi / 6)
    m0_maj = mp.exp(-mp_rat(16, 5) * mp.pi)
    m32 = mp.exp(-mp_rat(48, 5) * mp.pi)
    sr3 = mp.sqrt(mp.mpf(3))
    m02 = m32 * m32
    yu_l, yd_l, ye_l, yn_l, cr_l = [to3(m) for m in uv_mats]
    st_dh0 = (
        [g0, g0, g0], yu_l, yd_l, ye_l, yn_l, sc3(m0_maj, cr_l), Z,
        [sr3 * m32] * 3, sc3(-sr3 * m32, yu_l), sc3(-sr3 * m32, yd_l), sc3(-sr3 * m32, ye_l), sc3(-sr3 * m32, yn_l),
        uv3.c_mu * m32, uv3.c_B * (uv3.c_mu * m02), m02, m02,
        i3l(m02), i3l(m02), i3l(m02), i3l(m02), i3l(m02), i3l(m02),
    )
    s_dh0_1 = st_dh0
    for _ in range(16):
        s_dh0_1 = rich_gen(s_dh0_1, t_nu_s / 16, rhs_mssm, True, False)
    kap_dh0 = to3(-fr3(s_dh0_1[4]) * (fr3(s_dh0_1[5]) ** (-1)) * fr3(s_dh0_1[4]).T)
    s_dh0_2 = (s_dh0_1[0], s_dh0_1[1], s_dh0_1[2], s_dh0_1[3], Z, Z, kap_dh0, *s_dh0_1[7:11], Z, *s_dh0_1[12:])
    for _ in range(24):
        s_dh0_2 = rich_gen(s_dh0_2, (t_susy_s - t_nu_s) / 24, rhs_mssm, False, False)
    m1_plus_m2_dh0_over_m32_sq = (mp.re(s_dh0_2[14]) + mp.re(s_dh0_2[15]) + 2 * (abs(s_dh0_2[12]) ** 2)) / m02

    ctrl3_caught = bool(
        meta_240["m2_sq_over_m32_sq"] < 0 < meta_240["m1_sq_over_m32_sq"]
        and meta_240["dflat_bfb_over_m32_sq"] > 0
        and meta_240["min_sfermion_sq_over_m32_sq"] > 0
        and m1_plus_m2_dh0_over_m32_sq < 0
    )
    assert ctrl3_caught

    ctrl4_caught = bool(
        meta_240["mh0_over_mz"] > mp.mpf(1)
        and meta_240["mh0_tree_bound_over_mz"] < mp.mpf(1)
        and out_240["sm_msbar_at_ew_horizon"]["u3_over_d3"] > mp.mpf(15)
        and out_240["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"] > 0
        and out_240["cosmology_crv_and_honest_bounds"]["leptogenesis_tau_equil_over_hubble"] > mp.mpf(1)
        and meta_240["log10_susy_uv_qcd_instanton_shift"] < -mp.mpf(30)
    )
    assert ctrl4_caught

    # E3: Step-halving N=120 vs N=240, 13x scaling homogeneity, & SU(3)^6 scrambling:
    out_13x, _, _, vew_13, _ = eval_topdown_3stage_pipeline(uv_mats, l2_pos, uv3, n_steps=120, mu_gut_anchor=mp.mpf(13))
    vew_homog_exp = mp.log(vew_13 / vew_1) / mp.log(mp.mpf(13))
    homog_13x_err = max(abs(out_13x[s][k] - out_120[s][k]) / max(abs(out_120[s][k]), mp.mpf(10) ** (-20)) for s in out_120 for k in out_120[s])
    assert abs(vew_homog_exp - 1) < mp.mpf(10) ** (-30) and homog_13x_err < mp.mpf(10) ** (-30)

    uq, uu, ud, ul, ue = su3_cayley(13), su3_cayley(29), su3_cayley(47), su3_cayley(71), su3_cayley(89)
    un = su3_cayley(107) * mp.exp(I_MP * mp_rat(4, 13))
    un_c = mp.matrix([[mp.conj(un[r, c]) for c in range(3)] for r in range(3)])
    uv_scram_ok = (uq * uv_mats[0] * uu.H, uq * uv_mats[1] * ud.H, ul * uv_mats[2] * ue.H, ul * uv_mats[3] * un.H, un_c * uv_mats[4] * un.H)
    uv_scram_bad = (uq * uv_mats[0] * uu.H, uq * uv_mats[1] * ud.H, ul * uv_mats[2] * ue.H, ul * uv_mats[3] * un.H, uv_mats[4])

    out_scr_ok, _, _, _, _ = eval_topdown_3stage_pipeline(uv_scram_ok, l2_pos, uv3, n_steps=120)
    out_scr_bad, _, _, _, _ = eval_topdown_3stage_pipeline(uv_scram_bad, l2_pos, uv3, n_steps=120)

    max_rel_120_240 = mp.mpf(0)
    max_scram_rel_err = mp.mpf(0)
    bad_takagi_break = mp.mpf(0)
    n_obs = 0
    for sec in out_240:
        for k, v240 in out_240[sec].items():
            n_obs += 1
            v120 = out_120[sec][k]
            vscr = out_scr_ok[sec][k]
            vbad = out_scr_bad[sec][k]
            d240 = max(abs(v240), mp.mpf(10) ** (-20))
            d120 = max(abs(v120), mp.mpf(10) ** (-20))
            max_rel_120_240 = max(max_rel_120_240, abs(v240 - v120) / d240)
            max_scram_rel_err = max(max_scram_rel_err, abs(vscr - v120) / d120)
            bad_takagi_break = max(bad_takagi_break, abs(vbad - v120) / d120)

    assert n_obs == 50
    ctrl5_caught = bool(
        max_rel_120_240 < mp.mpf(10) ** (-10)
        and homog_13x_err < mp.mpf(10) ** (-30)
        and max_scram_rel_err < mp.mpf(10) ** (-25)
        and bad_takagi_break > mp_rat(1, 50)
    )
    assert ctrl5_caught

    controls_caught = sum(int(x) for x in (
        e1_res["control_1_mssm_noncomm_order_caught"],
        e1_res["control_2_sm_criticality_and_dlnmu2_caught"],
        ctrl3_caught,
        ctrl4_caught,
        ctrl5_caught,
    ))
    assert controls_caught == 5

    exact_30d = {"cusp_robin_bc_star_tau8", "m11_over_mgut_zero_knob", "inflation_conformal_S4_ns_N60", "inflation_conformal_S4_r_N60"}
    fmt_obs = {
        sec: {k: mp.nstr(v, 30 if k in exact_30d else 12) for k, v in sorted(out_240[sec].items())}
        for sec in sorted(out_240.keys())
    }

    payload = {
        "card": "AGY-C42",
        "layer": "Layer 4 (Two-Loop MSSM + 3 N_R to 1HDM SM RGE, Radiative EWSB, & Higgs Lift)",
        "empirical_firewall": "0 of 19",
        "check_labels_section_12": [
            "computed once",
            "expectations committed first",
            "tested against planted errors",
        ],
        "ast_zero_float_check": ast_res,
        "assumed_continuous_uv_parameters_layer4": ["Delta_H = 12 (on 10_{H,2}, with m_{H_u}^2(M_GUT) = +m_0^2 > 0)", "c_mu = 3/2", "c_B = -19/12"],
        "E1_literature_benchmark_gate": e1_res,
        "E2_three_stage_radiative_ewsb_and_higgs_lift": {
            "dynamical_horizons_tnu_tsusy_tew": [mp.nstr(t_nu_s, 15), mp.nstr(t_susy_s, 15), mp.nstr(t_ew_s, 15)],
            "horizon_fixed_point_max_residual": mp.nstr(h_res_240, 8),
            "m1_sq_over_m32_sq": mp.nstr(meta_240["m1_sq_over_m32_sq"], 12),
            "m2_sq_over_m32_sq": mp.nstr(meta_240["m2_sq_over_m32_sq"], 12),
            "m1_plus_m2_sq_at_DeltaH_0_over_m32_sq": mp.nstr(m1_plus_m2_dh0_over_m32_sq, 12),
            "dflat_bfb_margin_over_m32_sq": mp.nstr(meta_240["dflat_bfb_over_m32_sq"], 12),
            "min_sfermion_sq_over_m32_sq": mp.nstr(meta_240["min_sfermion_sq_over_m32_sq"], 12),
            "ms_stop_over_m32": mp.nstr(meta_240["ms_stop_over_m32"], 12),
            "mh0_over_mz_radiative": mp.nstr(meta_240["mh0_over_mz"], 12),
            "mh0_tree_bound_over_mz": mp.nstr(meta_240["mh0_tree_bound_over_mz"], 12),
            "charm_perturbatively_decouples_to_3f": bool(out_240["sm_1loop_pole_and_2hdm_bosons"]["mc_msbar_over_qcd_Lambda_4f"] > mp.mpf(1)),
            "qcd_Lambda_3f_over_vew": mp.nstr(meta_240["qcd_Lambda_3f_over_vew"], 12),
            "log10_susy_uv_qcd_instanton_shift": mp.nstr(meta_240["log10_susy_uv_qcd_instanton_shift"], 12),
            "observables_50_N240": fmt_obs,
            "control_3_deltaH0_no_ewsb_caught": ctrl3_caught,
            "control_4_radiative_higgs_lift_caught": ctrl4_caught,
        },
        "E3_convergence_homogeneity_and_scrambling": {
            "true_step_halving_N120_vs_N240_max_rel_err": mp.nstr(max_rel_120_240, 10),
            "vew_13x_scaling_exponent": mp.nstr(vew_homog_exp, 16),
            "homogeneity_13x_max_rel_err": mp.nstr(homog_13x_err, 8),
            "su3_pow6_scrambling_max_rel_err": mp.nstr(max_scram_rel_err, 8),
            "non_takagi_mR_negative_ctrl_rel_break": mp.nstr(bad_takagi_break, 10),
            "control_5_convergence_and_scrambling_caught": ctrl5_caught,
        },
        "planted_controls_caught": controls_caught,
        "planted_controls_total": 5,
        "all_expectations_passed": True,
    }

    raw_b = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    OUT_JSON.write_bytes(raw_b)
    OUT_SHA.write_text(f"{hashlib.sha256(raw_b).hexdigest()}  {OUT_JSON.name}\n", encoding="utf-8")
    print(
        f"AGY-C42 producer complete in {int(time.time() - t0)}s: "
        f"horizons=({mp.nstr(t_nu_s, 5)},{mp.nstr(t_susy_s, 5)},{mp.nstr(t_ew_s, 5)}), "
        f"mh/mZ={mp.nstr(meta_240['mh0_over_mz'], 5)}, mt/mb={fmt_obs['sm_msbar_at_ew_horizon']['u3_over_d3'][:6]}, "
        f"N120v240={mp.nstr(max_rel_120_240, 3)}, controls={controls_caught}/5."
    )


if __name__ == "__main__":
    main()
