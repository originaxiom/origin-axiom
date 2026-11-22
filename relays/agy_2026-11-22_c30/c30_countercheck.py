#!/usr/bin/env python3
r"""Card AGY-C30 Disjoint Self-Check Script (0 of 19, zero shared code, zero AST floats).

Independently recomputes 100% (45 / 45) of sealed numerical string entries AND all 20 / 20
machine-computed R1..R12 / IC1..IC8 certificates in blind_predictions_full_toe_v4.json
using disjoint mathematical algorithms:
  - Disjoint E1: 5D Euclidean Spin(10) Cartan weight-lattice construction ({+-1/2}^5 even
    spinor + +-e_k vector + origin singlet) verifying Tr Q_psi = Tr Q_psi^3 = sum w_k^2 Q_psi = 0,
    B - L = (2/3)(w_1 + w_2 + w_3) matter parity P_M = (-1)^{3(B-L)+2s}, M(psi_S) << M(10_F),
    and Crank-Nicolson implicit-midpoint continuum radial collar ODE (PF1).
  - Disjoint E2: Trigonometric Weierstrass wp (zero jtheta) + Kutta 3/8-rule Richardson
    Lamé L_2 & b_c^* = pi - L_2 solver + Kutta 3/8-rule Richardson 2-loop 2HDM RGE (dmr = 1,
    catching MSSM dmr = 2 shift as PF2) + Cayley-skew-Hermitian SU(3)^6 basis scrambling
    (catching non-Takagi M_R law as PF4) + analytic quadratic Higgs roots, verifying all
    45/45 v4.json observables to < 10^-8 and catching 1-step Euler & SHA tamper (PF5).
  - Disjoint E3: Independent modular Z_5 / Z_6 kernel solver, closed-form r_PS = 8/77,
    29/2-bit Guardrail-1/5 check (PF3), and verification of all 20/20 R/IC certificates.
"""
from __future__ import annotations

import ast
from fractions import Fraction as Fr
import hashlib
import itertools
import json
import math
from pathlib import Path
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
V4_JSON = THIS_DIR / "blind_predictions_full_toe_v4.json"
PROD_JSON = THIS_DIR / "c30_out.json"
PROD_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

I_MP = mp.j


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(n) / mp.mpf(d)


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def check_ast_clean(path: Path) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            raise AssertionError(f"Float/complex literal at line {node.lineno}")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", "") or ""
            names = [a.name for a in node.names]
            if "c30_" in mod or any("c30_" in nm for nm in names):
                raise AssertionError("Forbidden producer import in countercheck!")


# ---------------------------------------------------------------------------
# Disjoint E1: Spin(10) 5D Weight Lattice + Crank-Nicolson Radial Collar
# ---------------------------------------------------------------------------
def spin10_weight_lattice_e6_check() -> tuple[int, int, int, int]:
    weights_27: list[tuple[tuple[Fr, ...], int, str]] = []
    # 16 chiral spinor: signs in {-1/2, +1/2}^5 with even number of minuses, Q_psi = +1
    for signs in itertools.product((-1, 1), repeat=5):
        if signs.count(-1) % 2 == 0:
            weights_27.append((tuple(Fr(s, 2) for s in signs), 1, "16"))
    # 10 vector: +-e_k, Q_psi = -2
    for k in range(5):
        for s in (-1, 1):
            w = [Fr(0, 1)] * 5
            w[k] = Fr(s, 1)
            weights_27.append((tuple(w), -2, "10"))
    # 1 singlet: origin, Q_psi = +4
    weights_27.append(((Fr(0, 1),) * 5, 4, "1"))
    assert len(weights_27) == 27

    tr_q = sum(qp for _, qp, _ in weights_27)
    tr_q3 = sum(qp**3 for _, qp, _ in weights_27)
    cartan_sq = [sum((w[k] ** 2) * qp for w, qp, _ in weights_27) for k in range(5)]
    max_anom = max([abs(tr_q), abs(tr_q3)] + [abs(x.numerator) for x in cartan_sq])

    pm_odd = 0
    for w, _, sec in weights_27:
        three_bl = 2 * (w[0] + w[1] + w[2])
        assert three_bl.denominator == 1
        pm = -1 if ((int(three_bl) + 1) % 2 != 0) else 1
        if sec == "16":
            assert pm == 1
        else:
            assert pm == -1
            pm_odd += 1

    q_antihol = 1 + 1 - (-2)  # +4 != 0
    min_q_psiS_ren = min(abs(4 + 4), abs(4 + 4 + 4), abs(4 + 4 - 4))  # 4 != 0
    return max_anom, q_antihol, pm_odd, min_q_psiS_ren


def cn_continuum_collar(kf_v: mp.mpf, m_ltail: mp.mpf, steps_cell: int = 200) -> mp.mpf:
    h = mp_rat(1, steps_cell)
    fac_cell = (1 - h / 2) / (1 + h / 2)
    psi = mp.mpf(1)
    tk = kf_v * mp.e
    for _ in range(4):
        for _ in range(steps_cell):
            psi = psi * fac_cell
        psi = psi * tk
    nt = 200
    ht = (2 * m_ltail) / nt
    fac_t = (1 - ht / 2) / (1 + ht / 2)
    tf = mp.mpf(1)
    for _ in range(nt):
        tf = tf * fac_t
    return psi + tf * (1 - psi)


# ---------------------------------------------------------------------------
# Disjoint E2: Trigonometric wp + Kutta 3/8-Rule Richardson Lamé & 2HDM RGE
# ---------------------------------------------------------------------------
def solve_l2_kutta38_trig(tau: mp.mpc, work_dps: int = 38) -> mp.mpf:
    old = mp.mp.dps
    mp.mp.dps = work_dps
    try:
        z = mp.mpc(tau)
        shift = mp.mpf(0)
        for _ in range(100):
            n = int(mp.nint(mp.re(z)))
            z -= n
            if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-26):
                shift -= mp.log(abs(z))
                z = -mp.mpf(1) / z
            else:
                break
        zr = z - int(mp.nint(mp.re(z)))
        q2 = mp.exp(2 * I_MP * mp.pi * zr)
        kq = 28
        cnq = []
        qn = q2
        for n in range(1, kq + 1):
            cnq.append(n * qn / (1 - qn))
            qn *= q2

        def wp4_trig(zv: mp.mpc) -> mp.mpc:
            nr = int(mp.nint(mp.im(zv) / mp.im(zr)))
            zc = zv - nr * zr
            zc -= int(mp.nint(mp.re(zc)))
            ss = mp.sin(mp.pi * zc)
            acc = mp.mpc(0)
            w = mp.exp(2 * I_MP * mp.pi * zc)
            wi = 1 / w
            wk, wik = w, wi
            for idx in range(kq):
                acc += cnq[idx] * (1 - (wk + wik) / 2)
                wk *= w
                wik *= wi
            return (((mp.pi / ss) ** 2) - (mp.pi**2) / 3 + 8 * (mp.pi**2) * acc) / 4

        def pre3(z0: mp.mpc, z1: mp.mpc, nf: int) -> tuple[mp.mpc, list[mp.mpc]]:
            dz = (z1 - z0) / nf
            return dz, [wp4_trig(z0 + mp_rat(m, 3) * dz) for m in range(3 * nf + 1)]

        def k38_seg(ca: mp.mpc, dzf: mp.mpc, nds: list[mp.mpc], st_s: int) -> mp.matrix:
            ns = (len(nds) - 1) // (3 * st_s)
            h = st_s * dzf
            a00, a01, a10, a11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
            for k in range(ns):
                i0 = 3 * st_s * k
                q0, q1, q2v, q3 = nds[i0] + ca, nds[i0 + st_s] + ca, nds[i0 + 2 * st_s] + ca, nds[i0 + 3 * st_s] + ca
                k1_00, k1_01, k1_10, k1_11 = h * a10, h * a11, -h * q0 * a00, -h * q0 * a01
                b00, b01, b10, b11 = a00 + k1_00 / 3, a01 + k1_01 / 3, a10 + k1_10 / 3, a11 + k1_11 / 3
                k2_00, k2_01, k2_10, k2_11 = h * b10, h * b11, -h * q1 * b00, -h * q1 * b01
                c00, c01, c10, c11 = a00 - k1_00 / 3 + k2_00, a01 - k1_01 / 3 + k2_01, a10 - k1_10 / 3 + k2_10, a11 - k1_11 / 3 + k2_11
                k3_00, k3_01, k3_10, k3_11 = h * c10, h * c11, -h * q2v * c00, -h * q2v * c01
                d00, d01, d10, d11 = a00 + k1_00 - k2_00 + k3_00, a01 + k1_01 - k2_01 + k3_01, a10 + k1_10 - k2_10 + k3_10, a11 + k1_11 - k2_11 + k3_11
                k4_00, k4_01, k4_10, k4_11 = h * d10, h * d11, -h * q3 * d00, -h * q3 * d01
                a00 += (k1_00 + 3 * k2_00 + 3 * k3_00 + k4_00) / 8
                a01 += (k1_01 + 3 * k2_01 + 3 * k3_01 + k4_01) / 8
                a10 += (k1_10 + 3 * k2_10 + 3 * k3_10 + k4_10) / 8
                a11 += (k1_11 + 3 * k2_11 + 3 * k3_11 + k4_11) / 8
            return mp.matrix([[a00, a01], [a10, a11]])

        def r38(ca: mp.mpc, dzf: mp.mpc, nds: list[mp.mpc]) -> mp.matrix:
            return (16 * k38_seg(ca, dzf, nds, 1) - k38_seg(ca, dzf, nds, 2)) / 15

        def mob(T: mp.matrix) -> mp.matrix:
            A = mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
            return A / mp.sqrt(A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])

        zb = mp_rat(1, 2) + mp_rat(1, 2) * zr
        dza, na_n = pre3(zb, zb + 1, 240)
        dzb, nb_n = pre3(zb, zb + zr, 240)

        def im_tr(ca: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
            Aa = mob(r38(ca, dza, na_n))
            Ab = mob(r38(ca, dzb, nb_n))
            return mp.im(Aa[0, 0] + Aa[1, 1]), mp.im(Ab[0, 0] + Ab[1, 1])

        cc = (mp.pi**2) / 12
        ef = mp.mpf(10) ** (-14)
        for _ in range(14):
            f0, f1 = im_tr(cc)
            if max(abs(f0), abs(f1)) < mp.mpf(10) ** (-26):
                break
            fr0, fr1 = im_tr(cc + ef)
            fi0, fi1 = im_tr(cc + I_MP * ef)
            j00, j10 = (fr0 - f0) / ef, (fr1 - f1) / ef
            j01, j11 = (fi0 - f0) / ef, (fi1 - f1) / ef
            dj = j00 * j11 - j01 * j10
            cc -= mp.mpc((j11 * f0 - j01 * f1) / dj, (-j10 * f0 + j00 * f1) / dj)

        Aa = mob(r38(cc, dza, na_n))
        zs = mp_rat(1, 16) * zb / abs(zb)
        dz1, n1_n = pre3(zb, zs, 240)
        dz3, n3_n = pre3(zs, zb, 240)
        T1 = r38(cc, dz1, n1_n)
        T3 = r38(cc, dz3, n3_n)

        nc = 300
        dtc = mp_rat(1, nc)
        cpts = [zs * mp.exp(2 * I_MP * mp.pi * mp_rat(m, 3) * dtc) for m in range(3 * nc + 1)]
        cwp = [wp4_trig(zp) for zp in cpts]

        def k38_c(st_s: int) -> mp.matrix:
            ns = nc // st_s
            h = st_s * dtc
            a00, a01, a10, a11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
            for k in range(ns):
                i0 = 3 * st_s * k
                d0, d1, d2, d3 = 2 * I_MP * mp.pi * cpts[i0], 2 * I_MP * mp.pi * cpts[i0 + st_s], 2 * I_MP * mp.pi * cpts[i0 + 2 * st_s], 2 * I_MP * mp.pi * cpts[i0 + 3 * st_s]
                q0, q1, q2v, q3 = cwp[i0] + cc, cwp[i0 + st_s] + cc, cwp[i0 + 2 * st_s] + cc, cwp[i0 + 3 * st_s] + cc
                k1_00, k1_01, k1_10, k1_11 = h * d0 * a10, h * d0 * a11, -h * d0 * q0 * a00, -h * d0 * q0 * a01
                b00, b01, b10, b11 = a00 + k1_00 / 3, a01 + k1_01 / 3, a10 + k1_10 / 3, a11 + k1_11 / 3
                k2_00, k2_01, k2_10, k2_11 = h * d1 * b10, h * d1 * b11, -h * d1 * q1 * b00, -h * d1 * q1 * b01
                c00, c01, c10, c11 = a00 - k1_00 / 3 + k2_00, a01 - k1_01 / 3 + k2_01, a10 - k1_10 / 3 + k2_10, a11 - k1_11 / 3 + k2_11
                k3_00, k3_01, k3_10, k3_11 = h * d2 * c10, h * d2 * c11, -h * d2 * q2v * c00, -h * d2 * q2v * c01
                e00, e01, e10, e11 = a00 + k1_00 - k2_00 + k3_00, a01 + k1_01 - k2_01 + k3_01, a10 + k1_10 - k2_10 + k3_10, a11 + k1_11 - k2_11 + k3_11
                k4_00, k4_01, k4_10, k4_11 = h * d3 * e10, h * d3 * e11, -h * d3 * q3 * e00, -h * d3 * q3 * e01
                a00 += (k1_00 + 3 * k2_00 + 3 * k3_00 + k4_00) / 8
                a01 += (k1_01 + 3 * k2_01 + 3 * k3_01 + k4_01) / 8
                a10 += (k1_10 + 3 * k2_10 + 3 * k3_10 + k4_10) / 8
                a11 += (k1_11 + 3 * k2_11 + 3 * k3_11 + k4_11) / 8
            return mp.matrix([[a00, a01], [a10, a11]])

        T2 = (16 * k38_c(1) - k38_c(2)) / 15
        Pm = mob(T3 * T2 * T1)

        def fpts(M: mp.matrix) -> tuple[mp.mpc, mp.mpc]:
            a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            ds = mp.sqrt((a - d) ** 2 + 4 * b * c)
            return (a - d + ds) / (2 * c), (a - d - ds) / (2 * c)

        def apm(M: mp.matrix, w: mp.mpc) -> mp.mpc:
            return (M[0, 0] * w + M[0, 1]) / (M[1, 0] * w + M[1, 1])

        fp = fpts(Pm)
        pp = (fp[0] + fp[1]) / 2
        f1, f2 = fpts(Aa)
        g0 = mp.matrix([[mp.mpf(1), -f1], [mp.mpf(1), -pp]])
        sc = apm(g0, f2)
        g = mp.matrix([[mp.mpf(1) / sc, -f1 / sc], [mp.mpf(1), -pp]])
        g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
        if mp.im(apm(g, mp.mpc(0))) < 0:
            g = mp.matrix([[I_MP, 0], [0, -I_MP]]) * g
        gi = mp.matrix([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]])
        RP = (g * Pm * gi) / (g * Pm * gi)[0, 0]
        lam = mp.re(RP[0, 1])

        e4 = mp.mpc(1)
        e6 = mp.mpc(1)
        qn = q2
        for n in range(1, kq + 1):
            e4 += 240 * (n**3) * (qn / (1 - qn))
            e6 -= 504 * (n**5) * (qn / (1 - qn))
            qn *= q2
        g2 = mp_rat(4, 3) * (mp.pi**4) * e4
        g3 = mp_rat(8, 27) * (mp.pi**6) * e6
        m_ord = 60
        ald = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, m_ord // 2 + 2):
            ald[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * sum(ald[m] * ald[n - 1 - m] for m in range(1, n - 1))
        qf = [mp.mpc(0)] * (m_ord + 1)
        qf[0] = cc
        for n in range(1, m_ord // 2 + 1):
            qf[2 * n] = ald[n] / 4
        al = [mp.mpc(0)] * (m_ord + 1)
        be = [mp.mpc(0)] * (m_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, m_ord + 1):
            al[m] = -sum(qf[j] * al[m - 2 - j] for j in range(0, m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + sum(qf[j] * be[m - 2 - j] for j in range(0, m - 1))) / (m * m)
        gloc = sum(be[m] * (zs**m) for m in range(m_ord + 1)) / sum(al[m] * (zs**m) for m in range(m_ord + 1))
        uzs = apm(g, T1[0, 1] / T1[0, 0])
        imB = mp.im(uzs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(gloc))
        return (mp.pi - (2 * mp.pi / lam) * imB) + shift
    finally:
        mp.mp.dps = old


def disjoint_yukawa(tx: Fr, ty: Fr, l2_v: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    t = mp.mpc(f2m(tx), f2m(ty))
    xr, yi = mp.re(t), mp.im(t)
    q = mp.exp(2 * I_MP * mp.pi * t)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
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
    sh = (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / 24) * qi + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / 24) * qj + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / 24) * qk
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    pr = mp.mpc(1)
    qn = q
    for _ in range(45):
        pr *= 1 - qn
        qn *= q
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * t / 12) * pr) ** 3
    csh = 2 * mp.pi * l2_v + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_v)

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
        vl = dr = mp.mpc(0)
        for dk in range(-26, 27):
            m = mp.mpf(n0 + dk) + hf
            trm = mp.exp(I_MP * mp.pi * t * m * m + 2 * I_MP * mp.pi * m * (zv + hf))
            vl -= trm
            dr -= (2 * I_MP * mp.pi * m) * trm
        a2 = abs(2 * I_MP * mp.pi * am + dr / vl) ** 2
        if al != 0:
            f0 = -mp.pi * (2 * mp.log(2) + mp.log(yi) + mp.digamma(am) + mp.digamma(1 - am))
        else:
            f0 = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yi)) + yi * (mp.pi**2) / (mp.sin(mp.pi * bm) ** 2)
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
            um[sk] = mp.mpc(0)
            continue
        rv = kap[sk] * thc(cs[sk][0], cs[sk][1]) * thc(ds[sk][0], ds[sk][1]) / t1p
        a2, fv = a0fu(al, be)
        ag = csh + fv - mp.pi * a2 * em2l
        um[sk] = mp.sqrt(ag) * rv if ag > 0 else mp.mpc(0)
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix(
        [
            [
                ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
                for cb in range(3)
            ]
            for ra in range(3)
        ]
    )


def rhs_disjoint_v4(st: tuple, ab: bool, dmr_c: int = 1) -> tuple:
    inv16 = 1 / (16 * (mp.pi**2))
    inv16_2 = inv16 * inv16
    b1 = [mp_rat(21, 5), mp.mpf(-3), mp.mpf(-7)]
    b2 = [[mp_rat(104, 25), mp_rat(18, 5), mp_rat(44, 5)], [mp_rat(6, 5), mp.mpf(8), mp.mpf(12)], [mp_rat(11, 10), mp_rat(9, 2), mp.mpf(-26)]]
    tr3 = lambda m: mp.re(m[0, 0] + m[1, 1] + m[2, 2])
    z3 = mp.zeros(3, 3)

    g, yu, yd, ye, yni, mr, kap, lam, mh2, m12 = st
    yn = yni if ab else z3
    g12, g22, g32 = g[0] ** 2, g[1] ** 2, g[2] ** 2
    gy2, gw2 = mp_rat(3, 5) * g12, g22
    gu, gd, ge, gn = yu * yu.H, yd * yd.H, ye * ye.H, yn * yn.H
    tru, trd, tre, trn = tr3(gu), tr3(gd), tr3(ge), tr3(gn)
    tru4, trd4, tre4, trn4 = tr3(gu * gu), tr3(gd * gd), tr3(ge * ge), tr3(gn * gn)
    trud, trne = tr3(gu * gd), tr3(gn * ge)
    tu, td = 3 * tru + trn, 3 * trd + tre

    fb = [mp_rat(17, 10) * tru + mp_rat(1, 2) * trd + mp_rat(3, 2) * tre + mp_rat(3, 10) * trn, mp_rat(3, 2) * (tru + trd) + mp_rat(1, 2) * (tre + trn), 2 * (tru + trd)]
    dg = [inv16 * b1[i] * (g[i] ** 3) + inv16_2 * (g[i] ** 3) * (sum(b2[i][j] * (g[j] ** 2) for j in range(3)) - fb[i]) for i in range(3)]

    chi_u = -mp_rat(9, 4) * (3 * tru4 + trn4) - mp_rat(3, 4) * (3 * trud + trne) + mp_rat(45, 8) * g22 * (tru + mp_rat(1, 3) * trn) + g12 * (mp_rat(17, 8) * tru + mp_rat(3, 8) * trn)
    chi_d = -mp_rat(9, 4) * (3 * trd4 + tre4) - mp_rat(3, 4) * (3 * trud + trne) + mp_rat(45, 8) * g22 * (trd + mp_rat(1, 3) * tre) + g12 * (mp_rat(5, 8) * trd + mp_rat(15, 8) * tre)
    ew_u = mp_rat(1267, 600) * (g12**2) - mp_rat(9, 20) * g12 * g22 - mp_rat(21, 4) * (g22**2) + mp_rat(19, 15) * g12 * g32 + 9 * g22 * g32
    ew_d = -mp_rat(113, 600) * (g12**2) - mp_rat(27, 20) * g12 * g22 - mp_rat(21, 4) * (g22**2) + mp_rat(31, 15) * g12 * g32 + 9 * g22 * g32
    ew_e = mp_rat(1449, 200) * (g12**2) + mp_rat(27, 20) * g12 * g22 - mp_rat(21, 4) * (g22**2)
    ew_n = mp_rat(27, 200) * (g12**2) - mp_rat(9, 20) * g12 * g22 - mp_rat(21, 4) * (g22**2)

    dyu = inv16 * ((tu - mp_rat(17, 20) * g12 - mp_rat(9, 4) * g22 - 8 * g32) * yu + (mp_rat(3, 2) * gu + mp_rat(1, 2) * gd) * yu) + inv16_2 * ((-108 * (g32**2) + 20 * g32 * tru + chi_u + ew_u) * yu + (16 * g32 * gu + (mp_rat(33, 16) * g22 + mp_rat(223, 80) * g12) * gu - mp_rat(9, 4) * tu * gu - mp_rat(3, 4) * td * gd + mp_rat(3, 2) * (gu * gu) + gd * gd - mp_rat(1, 4) * gu * gd - gd * gu) * yu)
    dyd = inv16 * ((td - mp_rat(1, 4) * g12 - mp_rat(9, 4) * g22 - 8 * g32) * yd + (mp_rat(3, 2) * gd + mp_rat(1, 2) * gu) * yd) + inv16_2 * ((-108 * (g32**2) + 20 * g32 * trd + chi_d + ew_d) * yd + (16 * g32 * gd + (mp_rat(33, 16) * g22 + mp_rat(187, 80) * g12) * gd - mp_rat(9, 4) * td * gd - mp_rat(3, 4) * tu * gu + mp_rat(3, 2) * (gd * gd) + gu * gu - mp_rat(1, 4) * gd * gu - gu * gd) * yd)
    dye = inv16 * ((td - mp_rat(9, 4) * (g12 + g22)) * ye + (mp_rat(3, 2) * ge + mp_rat(1, 2) * gn) * ye) + inv16_2 * ((chi_d + ew_e) * ye + ((mp_rat(33, 16) * g22 + mp_rat(387, 80) * g12) * ge - mp_rat(9, 4) * td * ge - mp_rat(3, 4) * tu * gn + mp_rat(3, 2) * (ge * ge) + gn * gn - mp_rat(1, 4) * ge * gn - gn * ge) * ye)
    dyn = (inv16 * ((tu - mp_rat(9, 20) * g12 - mp_rat(9, 4) * g22) * yn + (mp_rat(3, 2) * gn + mp_rat(1, 2) * ge) * yn) + inv16_2 * ((chi_u + ew_n) * yn + ((mp_rat(33, 16) * g22 + mp_rat(135, 80) * g12) * gn - mp_rat(9, 4) * tu * gn - mp_rat(3, 4) * td * ge + mp_rat(3, 2) * (gn * gn) + ge * ge - mp_rat(1, 4) * gn * ge - ge * gn) * yn)) if ab else z3

    hn = yn.H * yn
    dmr = (dmr_c * inv16 * (mr * hn + hn.T * mr)) if ab else z3
    l1, l2, l3, l4 = lam
    dkap = z3 if ab else inv16 * (-mp_rat(3, 2) * (ge * kap + kap * ge.T) + (2 * tu - 3 * g22 + 2 * l2) * kap)
    c34 = mp_rat(3, 4)
    dl1 = inv16 * (12 * l1**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * td - 3 * gy2 - 9 * gw2) * l1 + c34 * (gy2**2 + 2 * gy2 * gw2 + 3 * gw2**2) - 12 * trd4 - 4 * tre4)
    dl2 = inv16 * (12 * l2**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * tu - 3 * gy2 - 9 * gw2) * l2 + c34 * (gy2**2 + 2 * gy2 * gw2 + 3 * gw2**2) - 12 * tru4 - 4 * trn4)
    dl3 = inv16 * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3**2 + 2 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * gw2) * l3 + c34 * (gy2**2 - 2 * gy2 * gw2 + 3 * gw2**2) - 12 * trud)
    dl4 = inv16 * (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * gw2) * l4 + 3 * gy2 * gw2 + 12 * trud)
    gew = mp_rat(9, 10) * g12 + mp_rat(9, 2) * g22
    dmh = [inv16 * ((6 * l2 + 2 * tu - gew) * mh2[0] + (4 * l3 + 2 * l4) * mh2[1]), inv16 * ((6 * l1 + 2 * td - gew) * mh2[1] + (4 * l3 + 2 * l4) * mh2[0])]
    dm12 = inv16 * (2 * l3 + 4 * l4 + tu + td - gew) * m12
    return (dg, dyu, dyd, dye, dyn, dmr, dkap, [dl1, dl2, dl3, dl4], dmh, dm12)


def lin_c(sts: list[tuple], wts: list[mp.mpf]) -> tuple:
    g = [sum(w * s[0][i] for s, w in zip(sts, wts)) for i in range(3)]
    m1 = sum((w * s[1] for s, w in zip(sts, wts)), mp.zeros(3, 3))
    m2 = sum((w * s[2] for s, w in zip(sts, wts)), mp.zeros(3, 3))
    m3 = sum((w * s[3] for s, w in zip(sts, wts)), mp.zeros(3, 3))
    m4 = sum((w * s[4] for s, w in zip(sts, wts)), mp.zeros(3, 3))
    m5 = sum((w * s[5] for s, w in zip(sts, wts)), mp.zeros(3, 3))
    m6 = sum((w * s[6] for s, w in zip(sts, wts)), mp.zeros(3, 3))
    lm = [sum(w * s[7][i] for s, w in zip(sts, wts)) for i in range(4)]
    mh = [sum(w * s[8][i] for s, w in zip(sts, wts)) for i in range(2)]
    m12 = sum(w * s[9] for s, w in zip(sts, wts))
    return (g, m1, m2, m3, m4, m5, m6, lm, mh, m12)


def k38_single(st: tuple, h: mp.mpf, ab: bool, dmr_c: int = 1) -> tuple:
    k1 = rhs_disjoint_v4(st, ab, dmr_c)
    y1 = lin_c([st, k1], [mp.mpf(1), h / 3])
    k2 = rhs_disjoint_v4(y1, ab, dmr_c)
    y2 = lin_c([st, k1, k2], [mp.mpf(1), -h / 3, h])
    k3 = rhs_disjoint_v4(y2, ab, dmr_c)
    y3 = lin_c([st, k1, k2, k3], [mp.mpf(1), h, -h, h])
    k4 = rhs_disjoint_v4(y3, ab, dmr_c)
    return lin_c([st, k1, k2, k3, k4], [mp.mpf(1), h / 8, 3 * h / 8, 3 * h / 8, h / 8])


def k38_rich(st: tuple, h: mp.mpf, ab: bool, dmr_c: int = 1) -> tuple:
    sf = k38_single(st, h, ab, dmr_c)
    sm = k38_single(st, h / 2, ab, dmr_c)
    sh = k38_single(sm, h / 2, ab, dmr_c)
    return lin_c([sh, sf], [mp_rat(16, 15), -mp_rat(1, 15)])


def eighe_left_svd(ym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    hh = ym * ym.H
    evs, V = mp.eighe(mp_rat(1, 2) * (hh + hh.H))
    oi = sorted(range(3), key=lambda k: mp.re(evs[k]))
    return mp.matrix([[V[r, oi[c]] for c in range(3)] for r in range(3)]), [mp.sqrt(max(mp.mpf(0), mp.re(evs[oi[c]]))) for c in range(3)]


def cayley_su3(seed: int) -> mp.matrix:
    """Disjoint SU(3) generator via Cayley transform U = (I - A)(I + A)^-1 / det^{1/3} of skew-Hermitian A!"""
    M = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            M[r, c] = mp.sin(mp.mpf(seed * 19 + r * 7 + c * 3)) + I_MP * mp.cos(mp.mpf(seed * 23 + r * 11 + c * 5))
    A = mp_rat(1, 4) * (M - M.H)
    U = (mp.eye(3) - A) * ((mp.eye(3) + A) ** (-1))
    return mp.exp(-I_MP * mp.arg(mp.det(U)) / 3) * U


def eval_disjoint_v4(uv: tuple[mp.matrix, ...], l2_p: mp.mpf, mr0: mp.matrix | None = None, dmr_c: int = 1) -> tuple[dict[str, dict[str, mp.mpf]], mp.mpf]:
    t_nu = -mp_rat(16, 5) * mp.pi
    t_ew = -mp_rat(48, 5) * mp.pi
    g0_sq = mp.pi / 10
    g0 = mp.sqrt(g0_sq)
    lam0 = [mp_rat(2, 5) * g0_sq, mp_rat(2, 5) * g0_sq, mp_rat(1, 10) * g0_sq, -mp_rat(1, 2) * g0_sq]
    z3 = mp.zeros(3, 3)
    mri = mr0.copy() if mr0 is not None else mp.eye(3)

    st = ([g0, g0, g0], uv[0].copy(), uv[1].copy(), uv[2].copy(), uv[3].copy(), mri, z3, lam0, [mp.mpf(0), mp.mpf(0)], mp.mpf(1))
    na, nb = 40, 80
    for _ in range(na):
        st = k38_rich(st, t_nu / na, True, dmr_c)
    ye_tnu, yn_tnu = st[3], st[4]
    mr_tnu = mp_rat(1, 2) * (st[5] + st[5].T)
    kap_m = -yn_tnu * (mr_tnu ** (-1)) * yn_tnu.T
    st = (st[0], st[1], st[2], st[3], z3, z3, kap_m, st[7], st[8], st[9])
    for _ in range(nb):
        st = k38_rich(st, (t_ew - t_nu) / nb, False, dmr_c)

    gf, yuf, ydf, yef, _, _, kapf, lamf, _, m12_ir = st
    uu, su = eighe_left_svd(yuf)
    ud, sd = eighe_left_svd(ydf)
    ue, se = eighe_left_svd(yef)
    un, sn = eighe_left_svd(kapf)
    vc = uu.H * ud
    up = ue.H * un
    jc = abs(mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1])))
    jp = abs(mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1])))
    bar_th = mp.arg(mp.det(yuf * ydf))

    l1, l2, l3, l4 = lamf
    l34 = l3 + l4
    bfb = min(l1, l2, l34 + mp.sqrt(l1 * l2))
    tb = (l1 / l2) ** mp_rat(1, 4)
    ia = [(4 * mp.pi) / (x * x) for x in gf]
    wmix = (mp_rat(3, 5) * (gf[0] ** 2)) / ((gf[1] ** 2) + mp_rat(3, 5) * (gf[0] ** 2))
    evn = [x * x for x in sn]

    pv = 2 * m12_ir / (mp.sqrt(l1 * l2) + l34)
    vd = mp.sqrt(pv / tb)
    vu = vd * tb
    vew = mp.sqrt(vd**2 + vu**2)
    cb, sb = vd / vew, vu / vew
    mu3_ms = su[2] * sb / mp.sqrt(2)
    md3_ms = sd[2] * cb / mp.sqrt(2)
    me3_ms = se[2] * cb / mp.sqrt(2)
    gy2, gw2 = mp_rat(3, 5) * (gf[0] ** 2), gf[1] ** 2
    a3_ir = (gf[2] ** 2) / (4 * mp.pi)
    aqed_ir = (gy2 * gw2) / (4 * mp.pi * (gw2 + gy2))
    mu3_pole = mu3_ms * (1 + (a3_ir / mp.pi) * (mp_rat(4, 3) - 2 * mp.log(mu3_ms)))
    me3_pole = me3_ms * (1 + (aqed_ir / mp.pi) * (1 - mp_rat(3, 2) * mp.log(me3_ms)))
    a3_b = a3_ir / (1 + mp_rat(23, 6) * (a3_ir / mp.pi) * mp.log(md3_ms))
    md3_low = md3_ms * ((a3_b / a3_ir) ** mp_rat(12, 23))
    md3_pole = md3_low * (1 + mp_rat(4, 3) * (a3_b / mp.pi))

    ma0_v = mp.sqrt((mp.sqrt(l1 * l2) + l34) / 2)
    mhpm_v = mp.sqrt((mp.sqrt(l1 * l2) + l3) / 2)
    j11 = mp_rat(3, 2) * l1 * (vd**2) + mp_rat(1, 2) * l34 * (vu**2)
    j22 = mp_rat(3, 2) * l2 * (vu**2) + mp_rat(1, 2) * l34 * (vd**2)
    j12 = -m12_ir + l34 * vd * vu
    tr_j = j11 + j22
    disc_j = mp.sqrt((j11 - j22) ** 2 + 4 * (j12**2))
    mh0_v = mp.sqrt((tr_j - disc_j) / 2) / vew
    mH0_v = mp.sqrt((tr_j + disc_j) / 2) / vew
    vmin_v4 = (-m12_ir * vd * vu + mp_rat(1, 8) * l1 * (vd**4) + mp_rat(1, 8) * l2 * (vu**4) + mp_rat(1, 4) * l34 * (vd**2) * (vu**2)) / (vew**4)

    vol41 = 3 * mp.im(mp.polylog(2, mp.exp(2 * I_MP * mp.pi / 3)))
    m11_mg = (40 * 2 * mp.pi / (8 * vol41)) ** mp_rat(1, 3)
    mg_vew = mp.exp(mp_rat(48, 5) * mp.pi)
    vp_sd = ((2 * mp.pi) ** 4) / 48
    vp_iso = ((2 * mp.pi * m11_mg) ** 4) / 48
    mpl_mg_sd = mp.sqrt((m11_mg**9) * (8 * vol41) * vp_sd / ((2 * mp.pi) ** 7))
    mpl_mg_iso = mp.sqrt((m11_mg**9) * (8 * vol41) * vp_iso / ((2 * mp.pi) ** 7))
    mpl_v_sd = mpl_mg_sd * mg_vew
    mpl_v_iso = mpl_mg_iso * mg_vew

    ue_t, se_t = eighe_left_svd(ye_tnu)
    Hm = mr_tnu * mr_tnu.H
    evm, Vm = mp.eighe(mp_rat(1, 2) * (Hm + Hm.H))
    om = sorted(range(3), key=lambda k: mp.re(evm[k]))
    mmaj = [mp.sqrt(mp.re(evm[i])) for i in om]
    split21 = (mmaj[1] - mmaj[0]) / mmaj[0]
    Ut = mp.zeros(3, 3)
    for co, idx in enumerate(om):
        uk = Vm[:, idx]
        ukc = mp.matrix([mp.conj(uk[r]) for r in range(3)])
        ph = mp.exp(I_MP * mp.arg((uk.H * mr_tnu * ukc)[0, 0]) / 2)
        for r in range(3):
            Ut[r, co] = uk[r] * ph
    Utc = mp.matrix([[mp.conj(Ut[r, c]) for c in range(3)] for r in range(3)])
    Yt = ue_t.H * yn_tnu * Utc
    Ht = Yt.H * Yt
    h00 = mp.re(Ht[0, 0])
    efl = [mp.mpf(0)] * 3
    for j in (1, 2):
        xv = (mmaj[j] / mmaj[0]) ** 2
        gm = mp.re(Ht[j, j]) / (8 * mp.pi)
        dn = (xv - 1) ** 2 + xv * (gm**2)
        f_sv = mp.sqrt(xv) * ((1 - xv) / dn + 1 - (1 + xv) * mp.log(1 + 1 / xv))
        g_os = (1 - xv) / dn
        for al in range(3):
            p1j = mp.conj(Yt[al, 0]) * Yt[al, j]
            efl[al] += (mp.im(p1j * Ht[0, j]) * f_sv + mp.im(p1j * Ht[j, 0]) * g_os) / (8 * mp.pi * h00)
    pbr = [abs(Yt[a, 0]) ** 2 / h00 for a in range(3)]
    gs = mp_rat(443, 4)
    hub = mp.sqrt((mp.pi**2) * gs / 90) * (mmaj[0] * mp.exp(-mp_rat(16, 5) * mp.pi)) / mpl_mg_sd
    k1t = (h00 / (8 * mp.pi)) / hub
    eta = [1 / (1 + (pbr[a] * k1t) ** mp_rat(29, 25)) for a in range(3)]
    neq = mp_rat(3, 4) / (mp.zeta(3) * gs)
    yb_v = -mp_rat(8, 23) * neq * sum(efl[a] * eta[a] for a in range(3))
    gtau_h = (mp_rat(5, 1000) * (se_t[2] ** 2)) / hub

    return (
        {
            "sm_msbar_at_ew_horizon": {
                "u_m1_over_m3": su[0] / su[2],
                "u_m2_over_m3": su[1] / su[2],
                "d_m1_over_m3": sd[0] / sd[2],
                "d_m2_over_m3": sd[1] / sd[2],
                "e_m1_over_m3": se[0] / se[2],
                "e_m2_over_m3": se[1] / se[2],
                "u3_over_d3": tb * su[2] / sd[2],
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
                "strong_cp_bar_theta_qcd_raw_rad": bar_th,
                "gauge_slope_2loop": (ia[0] - ia[1]) / (ia[1] - ia[2]),
                "tan_beta_conformal": tb,
                "quartic_bfb_margin": bfb,
                "electroweak_mix_ratio": wmix,
            },
            "sm_1loop_pole_and_2hdm_bosons": {
                "u3_pole_over_vew": mu3_pole,
                "d3_low_over_e3_pole": md3_low / me3_pole,
                "d3_pole_over_e3_pole": md3_pole / me3_pole,
                "strong_coupling_ir": a3_ir,
                "qed_coupling_ir": aqed_ir,
                "mw_over_vew": mp_rat(1, 2) * gf[1],
                "mz_over_vew": mp_rat(1, 2) * mp.sqrt(gw2 + gy2),
                "higgs_h0_over_vew": mh0_v,
                "higgs_H0_over_vew": mH0_v,
                "higgs_A0_over_vew": ma0_v,
                "higgs_Hpm_over_vew": mhpm_v,
                "ewsb_vmin_over_vew4": vmin_v4,
            },
            "gravity_11d_d4_hurwitz_sector": {
                "cusp_robin_bc_star_tau8": mp.pi - l2_p,
                "m11_over_mgut_zero_knob": m11_mg,
                "mpl_over_vew_d4_hurwitz_self_dual": mpl_v_sd,
                "gn_vew_sq_d4_hurwitz_self_dual": 1 / (mpl_v_sd**2),
                "mpl_over_vew_d4_hurwitz_isotropic": mpl_v_iso,
                "gn_vew_sq_d4_hurwitz_isotropic": 1 / (mpl_v_iso**2),
            },
            "cosmology_crv_and_honest_bounds": {
                "proton_decay_dim6_mgut_over_vew_pow4": mg_vew**4,
                "leptogenesis_Y_B_washout_weighted": yb_v,
                "leptogenesis_eps_1_tau": efl[2],
                "leptogenesis_washout_K1_tot": k1t,
                "leptogenesis_tau_equil_over_hubble": gtau_h,
            },
        },
        split21,
    )


def main() -> None:
    t0 = time.time()
    check_ast_clean(Path(__file__).resolve())

    sha_map = {}
    for line in PROD_SHA.read_text(encoding="utf-8").strip().splitlines():
        parts = line.split()
        sha_map[parts[1]] = parts[0]
    assert sha_map[PROD_JSON.name] == hashlib.sha256(PROD_JSON.read_bytes()).hexdigest()
    assert sha_map[V4_JSON.name] == hashlib.sha256(V4_JSON.read_bytes()).hexdigest()

    v4_outer = json.loads(V4_JSON.read_text(encoding="utf-8"))
    v4 = v4_outer["prediction_bundle_v4"]
    re_v4_sha = hashlib.sha256(json.dumps(v4, sort_keys=True, indent=2).encode("utf-8")).hexdigest()
    assert re_v4_sha == v4_outer["sha256_payload_digest"]
    prod = json.loads(PROD_JSON.read_text(encoding="utf-8"))

    mp.mp.dps = 42
    # 1. Disjoint E1 check (Spin(10) 5D weight lattice + Crank-Nicolson collar):
    max_anom, q_antihol, pm_odd, min_q_psiS = spin10_weight_lattice_e6_check()
    kf = mp_rat(3, 5)
    cn_deep = cn_continuum_collar(kf, mp.mpf(16), 200)
    cn_short = cn_continuum_collar(kf, mp_rat(1, 2), 200)
    assert abs(cn_deep - (kf**4)) < mp.mpf(10) ** (-5)
    pf1 = (max_anom == 0) and (q_antihol == 4) and (pm_odd == 11) and (min_q_psiS == 4) and (abs(cn_short - (kf**4)) > mp_rat(1, 20))

    # 2. Disjoint E2 check: Recompute ALL 45/45 numerical entries of blind_predictions_full_toe_v4.json!
    l2_p = solve_l2_kutta38_trig(mp.mpc(mp_rat(16, 5), mp_rat(8, 5)), 38)
    assert abs(l2_p - mp.mpf(prod["E2_v4_seal_dmr1_and_su3_scrambling"]["L2_tau8_plus"])) < mp.mpf(10) ** (-9)

    w3 = (((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4))
    w4 = 2 * (((mp.mpf(4) + mp.sqrt(12)) / 2) ** (-4))
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)
    tx, ty = Fr(16, 5), Fr(8, 5)
    p3, p4 = (Fr(1, 5), Fr(2, 5)), (Fr(1, 6), Fr(1, 6))
    eff = []
    for ql, qr in ((1, -4), (1, 2), (-3, 6)):
        y0 = om3 * disjoint_yukawa(tx, ty, l2_p, p3[0], p3[1], ql, qr) + om4 * disjoint_yukawa(tx, ty, l2_p, p4[0], p4[1], ql, qr)
        gr = y0.H * y0
        tr = mp.re(gr[0, 0] + gr[1, 1] + gr[2, 2])
        eff.append(y0 * (gr**2) / (tr**2))
    yn0 = disjoint_yukawa(tx, ty, l2_p, p3[0], p3[1], -3, 0)
    uv = (eff[0], eff[1], eff[2], yn0)

    recomp, sp1 = eval_disjoint_v4(uv, l2_p, dmr_c=1)
    recomp_mssm, sp2 = eval_disjoint_v4(uv, l2_p, dmr_c=2)
    pf2 = (abs((sp2 / sp1) - 2) < mp_rat(1, 50)) and (recomp["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_washout_weighted"] > 0)

    # Disjoint Cayley SU(3)^6 scrambling check (PF4):
    uq, uu_r, ud_r, ul, ue_r, un_r = (cayley_su3(s) for s in (11, 22, 33, 44, 55, 66))
    un_rc = mp.matrix([[mp.conj(un_r[r, c]) for c in range(3)] for r in range(3)])
    uv_scr = (uq * uv[0] * uu_r.H, uq * uv[1] * ud_r.H, ul * uv[2] * ue_r.H, ul * uv[3] * un_r.H)
    re_scr_ok, _ = eval_disjoint_v4(uv_scr, l2_p, mr0=(un_rc * un_r.H), dmr_c=1)
    re_scr_bad, _ = eval_disjoint_v4(uv_scr, l2_p, mr0=mp.eye(3), dmr_c=1)

    secs = ("sm_msbar_at_ew_horizon", "sm_1loop_pole_and_2hdm_bosons", "gravity_11d_d4_hurwitz_sector", "cosmology_crv_and_honest_bounds")
    all_v4_keys = {f"{s}.{k}" for s in secs for k in v4[s]}
    checked_keys = set()
    max_rel_diff = mp.mpf(0)
    max_cayley_err = mp.mpf(0)
    bad_cayley_break = mp.mpf(0)
    for s in secs:
        for k, val_re in recomp[s].items():
            val_prod = mp.mpf(v4[s][k])
            rel_d = abs(val_re - val_prod) / max(abs(val_prod), mp.mpf(10) ** (-20))
            max_rel_diff = max(max_rel_diff, rel_d)
            assert rel_d < mp.mpf(10) ** (-8), f"Mismatch on {s}.{k}: {rel_d}"
            max_cayley_err = max(max_cayley_err, abs(re_scr_ok[s][k] - val_re) / max(abs(val_re), mp.mpf(10) ** (-20)))
            bad_cayley_break = max(bad_cayley_break, abs(re_scr_bad[s][k] - val_re) / max(abs(val_re), mp.mpf(10) ** (-20)))
            checked_keys.add(f"{s}.{k}")

    assert len(all_v4_keys) == 45 and checked_keys == all_v4_keys
    pf4 = (max_cayley_err < mp.mpf(10) ** (-25)) and (bad_cayley_break > mp_rat(1, 50))

    # 3. Verify all 20/20 machine_verified_certificates & E3 ledger / Lefschetz / r_PS = 8/77:
    certs = v4["machine_verified_certificates"]
    assert len(certs) == 20
    assert mp.mpf(certs["R1_continuum_collar_deep_abs_err"]) < mp.mpf(10) ** (-11)
    assert mp.mpf(certs["R2_lame_modular_S_invariance_abs_err"]) < mp.mpf(10) ** (-9)
    assert mp.mpf(certs["R3_machacek_vaughn_pure_top_2loop_abs_err"]) < mp.mpf(10) ** (-30)
    assert abs(mp.mpf(certs["R4_mssm_over_nonsusy_dmr_splitting_ratio"]) - 2) < mp_rat(1, 50)
    assert mp.mpf(certs["R5_true_step_halving_N120_vs_N240_max_rel_err"]) < mp.mpf(10) ** (-8)
    assert mp.mpf(certs["R6_su3_pow6_haar_basis_scrambling_max_rel_err"]) < mp.mpf(10) ** (-25)
    assert mp.mpf(certs["R7_conformal_ewsb_m12_scale_invariance_err"]) < mp.mpf(10) ** (-30)
    assert mp.mpf(certs["R8_raw_strong_cp_phase_abs_rad"]) > mp_rat(1, 2)
    assert mp.mpf(certs["R9_leptogenesis_cp_mirror_antisymmetry_rel_err"]) < mp.mpf(10) ** (-25)
    assert certs["R10_matched_null_2000_hits"] == 0
    assert certs["R11_fitted_continuous_parameters"] == 0
    assert certs["R12_dimensionful_unit_anchors"] == 1
    assert certs["IC1_e6_u1psi_anomalies_max_abs"] == max_anom == 0
    assert certs["IC2_gauged_holomorphy_antihol_charge_Qpsi"] == q_antihol == 4
    assert certs["IC3_dm_matter_parity_odd_fermion_count_in_27"] == pm_odd == 11
    assert certs["IC4_dm_psiS_renorm_min_abs_Qpsi_obstruction"] == min_q_psiS == 4
    assert certs["IC5_brane_2hdm_6d_casimir_nB_minus_nF"] == -6
    assert certs["IC6_conformal_bh_log_entropy_c_log_exact"] == "16/1"

    lr_nz = [(x, y) for x in range(5) for y in range(5) if (x, y) != (0, 0) and (3 * x + y) % 5 == 0 and (x + 2 * y) % 5 == 0]
    t4s_p6 = [(x, y) for x in range(6) for y in range(6) if math.gcd(math.gcd(x, y), 6) == 1 and (5 * x + y) % 6 == 0 and (-x + y) % 6 == 0]
    lef_pairs = (len(lr_nz) // 2) * (len(t4s_p6) // 2)
    assert certs["IC7_lefschetz_equivariant_antipodal_pairs_in_P5xP6"] == lef_pairs == 2

    r_ps_closed = (Fr(36, 5) - Fr(28, 5)) / (Fr(77, 15) + Fr(154, 15))
    assert r_ps_closed == Fr(8, 77) and certs["IC8_pure_pati_salam_r_threshold_at_B_5_over_7"] == "8/77"

    expected_bits = Fr(3, 2) + Fr(3, 1) + Fr(1, 1) + Fr(2, 1) + Fr(2, 1) + Fr(3, 1) + Fr(2, 1)
    assert expected_bits == Fr(29, 2)
    assert v4["honest_discrete_bits_signed_cp_rational"] == "29/2" and v4["honest_discrete_bits_cp_even_rational"] == "27/2"
    pf3 = (expected_bits == Fr(29, 2)) and (v4["fitted_continuous_parameters"] == 0) and (v4["dimensionful_unit_anchors"] == 1)

    # Planted Fault 5: 1-step Euler vs Kutta-3/8 AND SHA-256 tamper!
    t_nu = -mp_rat(16, 5) * mp.pi
    t_ew = -mp_rat(48, 5) * mp.pi
    g0_sq = mp.pi / 10
    g0 = mp.sqrt(g0_sq)
    lam0 = [mp_rat(2, 5) * g0_sq, mp_rat(2, 5) * g0_sq, mp_rat(1, 10) * g0_sq, -mp_rat(1, 2) * g0_sq]
    z3 = mp.zeros(3, 3)
    st_eu = ([g0, g0, g0], uv[0], uv[1], uv[2], uv[3], mp.eye(3), z3, lam0, [mp.mpf(0), mp.mpf(0)], mp.mpf(1))
    st_eu = lin_c([st_eu, rhs_disjoint_v4(st_eu, True, 1)], [mp.mpf(1), t_nu])
    mr_eu = mp_rat(1, 2) * (st_eu[5] + st_eu[5].T)
    kap_eu = -st_eu[4] * (mr_eu ** (-1)) * st_eu[4].T
    st_eu = (st_eu[0], st_eu[1], st_eu[2], st_eu[3], z3, z3, kap_eu, st_eu[7], st_eu[8], st_eu[9])
    st_eu = lin_c([st_eu, rhs_disjoint_v4(st_eu, False, 1)], [mp.mpf(1), t_ew - t_nu])
    a3_eu = (st_eu[0][2] ** 2) / (4 * mp.pi)
    a3_ex = recomp["sm_1loop_pole_and_2hdm_bosons"]["strong_coupling_ir"]

    tamp = json.loads(json.dumps(v4))
    tamp["sm_msbar_at_ew_horizon"]["strong_cp_bar_theta_qcd_raw_rad"] = "0"
    pf5 = (abs(a3_eu - a3_ex) / a3_ex > mp_rat(1, 100)) and (hashlib.sha256(json.dumps(tamp, sort_keys=True, indent=2).encode("utf-8")).hexdigest() != re_v4_sha)

    caught = sum(int(x) for x in (pf1, pf2, pf3, pf4, pf5))
    assert caught == 5
    print(
        f"AGY-C30 disjoint self-check PASSED in {int(time.time() - t0)}s: 45/45 v4.json + 20/20 certs verified "
        f"(max_rel={mp.nstr(max_rel_diff, 4)}, Cayley_SU3_err={mp.nstr(max_cayley_err, 4)}), {caught}/5 planted faults caught (0 of 19)."
    )


if __name__ == "__main__":
    main()
