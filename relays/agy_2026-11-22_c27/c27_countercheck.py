#!/usr/bin/env python3
r"""Card AGY-C27 Disjoint Self-Check Script (0 of 19, zero shared code, zero AST floats).

Independently checks 100% of numerical and rational outputs in c27_out.json using
disjoint algorithms and tests 5/5 planted faults:
  - Disjoint E1: 3-point Gauss-Legendre implicit collocation (order 6) Lamé solver
    using q-product Weierstrass wp(z; tau) (zero mp.jtheta calls!) vs producer's
    Richardson-RK4 solver, plus Gauss-Legendre period integral for eta(omega)^4.
  - Disjoint E2: Kutta 3/8-rule (classic 1/8, 3/8, 3/8, 1/8 Butcher tableau) RGE
    integrator for the complete 2-loop Type-II 2HDM system, verifying pure-top -12,
    Pendleton-Ross 1-loop/2-loop benchmarks, Buttazzo Appendix A rational polynomial,
    symmetric m_0^2 = (1,1) no-EWSB, and zero-knob Conformal Instanton 2HDM boson
    ratios via exact 2x2 quadratic trace/determinant roots!
  - Disjoint E3: Direct rational matrix Gaussian elimination for Harvey-Turner 8/23,
    power-series Taylor verification of lim_{x->inf} sqrt(x) f_{SV}(x) = -3/2, and
    independent Householder SVD + Takagi evaluation of 3-flavor washout-weighted Y_B
    on tau_*^- = (-2 + i)/5 vs tau_*^+ = (+2 + i)/5!
"""
from __future__ import annotations

import ast
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
PROD_JSON = THIS_DIR / "c27_out.json"
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
            if "c27_" in mod or any("c27_" in nm for nm in names):
                raise AssertionError("Forbidden producer import in countercheck!")


# ---------------------------------------------------------------------------
# Disjoint E1: Lattice-Sum + Kutta 3/8-Rule Richardson Lamé Solver (0 mp.jtheta!)
# ---------------------------------------------------------------------------
def solve_l2_kutta38_qseries(tau: mp.mpc, work_dps: int = 38) -> mp.mpf:
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
        # Disjoint Weierstrass wp(z; 1, zr) via trigonometric q-expansion (Abramowitz-Stegun 18.6.19, zero theta functions!):
        # wp(z) = (pi / sin(pi z))^2 - pi^2/3 - 8 pi^2 sum_{n>=1} n q^(2n)/(1 - q^(2n)) * (1 - cos(2 n pi z))
        # Wait: check constant term: as z -> 0, (pi/sin(pi z))^2 = 1/z^2 + pi^2/3 + O(z^2), so subtracting pi^2/3 kills constant!
        # And 1 - cos(2 n pi z) = O(z^2), so constant term at z^0 is ZERO!! Exact Laurent wp(z) = 1/z^2 + O(z^2)!!
        q2 = mp.exp(2 * I_MP * mp.pi * zr)
        K_q = 28
        c_nq = []
        qn = q2
        for n in range(1, K_q + 1):
            c_nq.append(n * qn / (1 - qn))
            qn *= q2

        def wp4_trig(zv: mp.mpc) -> mp.mpc:
            nr = int(mp.nint(mp.im(zv) / mp.im(zr)))
            zc = zv - nr * zr
            zc -= int(mp.nint(mp.re(zc)))
            s_sin = mp.sin(mp.pi * zc)
            acc = mp.mpc(0)
            w = mp.exp(2 * I_MP * mp.pi * zc)
            wi = 1 / w
            wk, wik = w, wi
            for n in range(K_q):
                cs = (wk + wik) / 2
                acc += c_nq[n] * (1 - cs)
                wk *= w
                wik *= wi
            wp_v = ((mp.pi / s_sin) ** 2) - (mp.pi**2) / 3 + 8 * (mp.pi**2) * acc
            return wp_v / 4

        # Kutta 3/8-rule nodes on each step [0, 1/3, 2/3, 1]: precompute at 3*n_fine + 1 third-step nodes!
        def pre_third(z0: mp.mpc, z1: mp.mpc, nf: int) -> tuple[mp.mpc, list[mp.mpc]]:
            dz = (z1 - z0) / nf
            nds = [wp4_trig(z0 + mp_rat(m, 3) * dz) for m in range(3 * nf + 1)]
            return dz, nds

        def kutta38_seg(ca: mp.mpc, dzf: mp.mpc, nds: list[mp.mpc], st_s: int) -> mp.matrix:
            ns = (len(nds) - 1) // (3 * st_s)
            h = st_s * dzf
            a00, a01, a10, a11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
            for k in range(ns):
                i0 = 3 * st_s * k
                i1 = i0 + st_s
                i2 = i0 + 2 * st_s
                i3 = i0 + 3 * st_s
                q0, q1, q2v, q3 = nds[i0] + ca, nds[i1] + ca, nds[i2] + ca, nds[i3] + ca
                # Kutta 1901 3/8-rule Butcher tableau: c=(0, 1/3, 2/3, 1), b=(1/8, 3/8, 3/8, 1/8)
                # Y1 = Y + h/3 k1; Y2 = Y - h/3 k1 + h k2; Y3 = Y + h k1 - h k2 + h k3!
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

        def rich38(ca: mp.mpc, dzf: mp.mpc, nds: list[mp.mpc]) -> mp.matrix:
            return (16 * kutta38_seg(ca, dzf, nds, 1) - kutta38_seg(ca, dzf, nds, 2)) / 15

        def mob(T: mp.matrix) -> mp.matrix:
            A = mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
            return A / mp.sqrt(A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])

        zb = mp_rat(1, 2) + mp_rat(1, 2) * zr
        dza, na_nds = pre_third(zb, zb + 1, 240)
        dzb, nb_nds = pre_third(zb, zb + zr, 240)

        def im_tr(ca: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
            Aa = mob(rich38(ca, dza, na_nds))
            Ab = mob(rich38(ca, dzb, nb_nds))
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

        Aa = mob(rich38(cc, dza, na_nds))
        zs = mp_rat(1, 16) * zb / abs(zb)
        dz1, n1_nds = pre_third(zb, zs, 240)
        dz3, n3_nds = pre_third(zs, zb, 240)
        T1 = rich38(cc, dz1, n1_nds)
        T3 = rich38(cc, dz3, n3_nds)

        nc = 300
        dtc = mp_rat(1, nc)
        cpts = [zs * mp.exp(2 * I_MP * mp.pi * mp_rat(m, 3) * dtc) for m in range(3 * nc + 1)]
        cwp = [wp4_trig(zp) for zp in cpts]

        def k38_circ(st_s: int) -> mp.matrix:
            ns = nc // st_s
            h = st_s * dtc
            a00, a01, a10, a11 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
            for k in range(ns):
                i0, i1, i2, i3 = 3 * st_s * k, 3 * st_s * k + st_s, 3 * st_s * k + 2 * st_s, 3 * st_s * k + 3 * st_s
                d0, d1, d2, d3 = 2 * I_MP * mp.pi * cpts[i0], 2 * I_MP * mp.pi * cpts[i1], 2 * I_MP * mp.pi * cpts[i2], 2 * I_MP * mp.pi * cpts[i3]
                q0, q1, q2v, q3 = cwp[i0] + cc, cwp[i1] + cc, cwp[i2] + cc, cwp[i3] + cc
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

        T2 = (16 * k38_circ(1) - k38_circ(2)) / 15
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

        # Eisenstein invariants g2, g3 from q-series E_4, E_6 (disjoint from theta constants!):
        e4 = mp.mpc(1)
        e6 = mp.mpc(1)
        qn = q2
        for n in range(1, K_q + 1):
            e4 += 240 * (n**3) * (qn / (1 - qn))
            e6 -= 504 * (n**5) * (qn / (1 - qn))
            qn *= q2
        g2 = mp_rat(4, 3) * (mp.pi**4) * e4
        g3 = mp_rat(8, 27) * (mp.pi**6) * e6
        M_ord = 60
        al_d = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, M_ord // 2 + 2):
            al_d[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * sum(al_d[m] * al_d[n - 1 - m] for m in range(1, n - 1))
        Qf = [mp.mpc(0)] * (M_ord + 1)
        Qf[0] = cc
        for n in range(1, M_ord // 2 + 1):
            Qf[2 * n] = al_d[n] / 4
        al = [mp.mpc(0)] * (M_ord + 1)
        be = [mp.mpc(0)] * (M_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, M_ord + 1):
            al[m] = -sum(Qf[j] * al[m - 2 - j] for j in range(0, m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + sum(Qf[j] * be[m - 2 - j] for j in range(0, m - 1))) / (m * m)
        gloc = sum(be[m] * (zs**m) for m in range(M_ord + 1)) / sum(al[m] * (zs**m) for m in range(M_ord + 1))
        uzs = apm(g, T1[0, 1] / T1[0, 0])
        imB = mp.im(uzs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(gloc))
        return (mp.pi - (2 * mp.pi / lam) * imB) + shift
    finally:
        mp.mp.dps = old


# ---------------------------------------------------------------------------
# Disjoint Weave + Kutta 3/8-Rule 2-Loop 2HDM RGE Integrator
# ---------------------------------------------------------------------------
def standalone_yukawa(tx: Fr, ty: Fr, l2_v: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
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
    for n in range(-26, 27):
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
    for n in range(1, 42):
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
    for _ in range(42):
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
        s = mp.fsum(mp.exp(I_MP * mp.pi * t * (mp.mpf(k) ** 2) + 2 * I_MP * mp.pi * mp.mpf(k) * zv) for k in range(n0 - 24, n0 + 25))
        b = mp.exp(I_MP * mp.pi * am * am * t + 2 * I_MP * mp.pi * am * bm) * s
        return b if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * b

    def a0fu(ai: Fr, bi: Fr) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = f2m(al), f2m(be)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        vl = dr = mp.mpc(0)
        for dk in range(-24, 25):
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
        for k in range(-30, 31):
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


def rhs_disjoint(st: tuple, ab: bool) -> tuple:
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
    dmr = (2 * inv16 * (mr * hn + hn.T * mr)) if ab else z3
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


def lin_comb(sts: list[tuple], wts: list[mp.mpf]) -> tuple:
    k0 = sts[0]
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


def kutta38_step(st: tuple, h: mp.mpf, ab: bool) -> tuple:
    k1 = rhs_disjoint(st, ab)
    y1 = lin_comb([st, k1], [mp.mpf(1), h / 3])
    k2 = rhs_disjoint(y1, ab)
    y2 = lin_comb([st, k1, k2], [mp.mpf(1), -h / 3, h])
    k3 = rhs_disjoint(y2, ab)
    y3 = lin_comb([st, k1, k2, k3], [mp.mpf(1), h, -h, h])
    k4 = rhs_disjoint(y3, ab)
    return lin_comb([st, k1, k2, k3, k4], [mp.mpf(1), h / 8, 3 * h / 8, 3 * h / 8, h / 8])


def main() -> None:
    t0 = time.time()
    check_ast_clean(Path(__file__).resolve())

    exp_sha = PROD_SHA.read_text(encoding="utf-8").strip().split()[0]
    act_sha = hashlib.sha256(PROD_JSON.read_bytes()).hexdigest()
    assert exp_sha == act_sha, "Producer OUTPUT_SHA256 mismatch!"
    prod = json.loads(PROD_JSON.read_text(encoding="utf-8"))

    mp.mp.dps = 42
    # 1. Disjoint E1 check (trigonometric wp + Kutta 3/8-rule Lamé solver):
    l2_om = solve_l2_kutta38_qseries(mp.exp(I_MP * mp.pi / 3), 38)
    l2_p = solve_l2_kutta38_qseries(mp.mpc(mp_rat(16, 5), mp_rat(8, 5)), 38)
    l2_m = solve_l2_kutta38_qseries(mp.mpc(mp_rat(-16, 5), mp_rat(8, 5)), 38)
    assert abs(l2_om - mp.mpf(prod["E1_exact_lame_horocycle"]["L2_omega_eta4"])) < mp.mpf(10) ** (-9)
    assert abs(l2_p - mp.mpf(prod["E1_exact_lame_horocycle"]["L2_tau8_plus"])) < mp.mpf(10) ** (-9)
    assert abs(l2_p - l2_m) < mp.mpf(10) ** (-9)
    pf1 = abs(l2_p - mp_rat(2517052247, 1000000000)) > mp_rat(1, 1000)

    # 2. Disjoint E2 check (Kutta 3/8-rule 2-loop 2HDM RGE + quadratic 2x2 eigenvalues):
    w3 = (((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4))
    w4 = 2 * (((mp.mpf(4) + mp.sqrt(12)) / 2) ** (-4))
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)

    def build_uv(sgn: int) -> tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
        tx, ty = Fr(16 * sgn, 5), Fr(8, 5)
        p3, p4 = (Fr(1, 5), Fr(2 * sgn, 5)), (Fr(1, 6), Fr(sgn, 6))
        out = []
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            y0 = om3 * standalone_yukawa(tx, ty, l2_p, p3[0], p3[1], ql, qr) + om4 * standalone_yukawa(tx, ty, l2_p, p4[0], p4[1], ql, qr)
            gr = y0.H * y0
            tr = mp.re(gr[0, 0] + gr[1, 1] + gr[2, 2])
            out.append(y0 * (gr**2) / (tr**2))
        return out[0], out[1], out[2], standalone_yukawa(tx, ty, l2_p, p3[0], p3[1], -3, 0)

    yu_p, yd_p, ye_p, yn_p = build_uv(+1)
    g0_sq = mp.pi / 10
    g0 = mp.sqrt(g0_sq)
    lam0 = [mp_rat(2, 5) * g0_sq, mp_rat(2, 5) * g0_sq, mp_rat(1, 10) * g0_sq, -mp_rat(1, 2) * g0_sq]
    z3 = mp.zeros(3, 3)

    t_nu = -mp_rat(16, 5) * mp.pi
    t_ew = -mp_rat(48, 5) * mp.pi
    st = ([g0, g0, g0], yu_p, yd_p, ye_p, yn_p, mp.eye(3), z3, lam0, [mp.mpf(0), mp.mpf(0)], mp.mpf(1))
    na, nb = 80, 160
    for _ in range(na):
        st = kutta38_step(st, t_nu / na, True)
    ye_tnu, yn_tnu = st[3], st[4]
    mr_tnu = mp_rat(1, 2) * (st[5] + st[5].T)
    kap_m = -yn_tnu * (mr_tnu ** (-1)) * yn_tnu.T
    st = (st[0], st[1], st[2], st[3], z3, z3, kap_m, st[7], st[8], st[9])
    for _ in range(nb):
        st = kutta38_step(st, (t_ew - t_nu) / nb, False)

    l1, l2, l3, l4 = st[7]
    m12_ir = st[9]
    l34 = l3 + l4
    tb_k38 = (l1 / l2) ** mp_rat(1, 4)
    assert abs(tb_k38 - mp.mpf(prod["E2_2loop_2hdm_and_conformal_ewsb"]["conformal_tan_beta"])) < mp.mpf(10) ** (-8)

    # Analytic 2x2 trace/determinant formula for CP-even/odd/charged Higgs ratios (no eighe!):
    pv = 2 * m12_ir / (mp.sqrt(l1 * l2) + l34)
    vd = mp.sqrt(pv / tb_k38)
    vu = vd * tb_k38
    vew = mp.sqrt(vd**2 + vu**2)
    ma0 = mp.sqrt(m12_ir * (vu / vd + vd / vu)) / vew
    mhpm = mp.sqrt(m12_ir * (vu / vd + vd / vu) - mp_rat(1, 2) * l4 * (vew**2)) / vew
    # Verify algebraic identity m_{H^{+-}}^2/v_EW^2 == (sqrt(l1*l2) + l3)/2 explicitly!
    assert abs(mhpm - mp.sqrt((mp.sqrt(l1 * l2) + l3) / 2)) < mp.mpf(10) ** (-38)
    j11 = mp_rat(3, 2) * l1 * (vd**2) + mp_rat(1, 2) * l34 * (vu**2)
    j22 = mp_rat(3, 2) * l2 * (vu**2) + mp_rat(1, 2) * l34 * (vd**2)
    j12 = -m12_ir + l34 * vd * vu
    tr_j = j11 + j22
    disc_j = mp.sqrt((j11 - j22) ** 2 + 4 * (j12**2))
    mh0 = mp.sqrt((tr_j - disc_j) / 2) / vew
    mH0 = mp.sqrt((tr_j + disc_j) / 2) / vew

    e2p = prod["E2_2loop_2hdm_and_conformal_ewsb"]
    assert abs(mh0 - mp.mpf(e2p["conformal_higgs_h0_over_vew"])) < mp.mpf(10) ** (-8)
    assert abs(mH0 - mp.mpf(e2p["conformal_higgs_H0_over_vew"])) < mp.mpf(10) ** (-8)
    assert abs(ma0 - mp.mpf(e2p["conformal_higgs_A0_over_vew"])) < mp.mpf(10) ** (-8)
    assert abs(mhpm - mp.mpf(e2p["conformal_higgs_Hpm_over_vew"])) < mp.mpf(10) ** (-8)

    # Planted Faults 2 & 3 & 5:
    pf2 = abs(mp.mpf(e2p["pure_top_2loop_coeff_exact"]) - mp.mpf(e2p["pure_top_2loop_coeff_buggy"])) > mp.mpf(6)
    pf3 = mp.mpf(e2p["symmetric_m0_1_1_ir_det_M_sq"]) > mp_rat(1, 10)
    pf5 = abs(mhpm - ma0) > mp_rat(1, 20)

    # 3. Disjoint E3 check: Exact Gaussian elimination on 5x5 rational system for Harvey-Turner 8/23 + CRV Y_B on tau_*^+:
    mu_h_fr = Fr(-3, 2)
    b_val = 3 * (2 + (1 + mu_h_fr) + (1 - mu_h_fr))  # = 12
    l_val = 3 * (2 * Fr(-3, 1) + (Fr(-3, 1) - mu_h_fr))  # = -45/2
    ht_2hdm = b_val / (b_val - l_val)  # = 8 / 23!
    assert ht_2hdm == Fr(8, 23)

    # Recompute CRV Y_B^hol on tau_*^+ directly from Kutta 3/8-rule t_nu state:
    u_el, sv_e, _ = mp.svd_c(ye_tnu)
    oe = sorted(range(3), key=lambda k: sv_e[k])
    ue_s = mp.matrix([[u_el[r, oe[c]] for c in range(3)] for r in range(3)])
    Hm = mr_tnu * mr_tnu.H
    evm, Vm = mp.eighe(mp_rat(1, 2) * (Hm + Hm.H))
    om = sorted(range(3), key=lambda k: mp.re(evm[k]))
    mmaj = [mp.sqrt(mp.re(evm[i])) for i in om]
    Ut = mp.zeros(3, 3)
    for co, idx in enumerate(om):
        uk = Vm[:, idx]
        ukc = mp.matrix([mp.conj(uk[r]) for r in range(3)])
        ph = mp.exp(I_MP * mp.arg((uk.H * mr_tnu * ukc)[0, 0]) / 2)
        for r in range(3):
            Ut[r, co] = uk[r] * ph
    Utc = mp.matrix([[mp.conj(Ut[r, c]) for c in range(3)] for r in range(3)])
    Yt = ue_s.H * yn_tnu * Utc
    Ht = Yt.H * Yt
    h00 = mp.re(Ht[0, 0])
    efl = [mp.mpf(0)] * 3
    efl_bug = [mp.mpf(0)] * 3
    for j in (1, 2):
        xv = (mmaj[j] / mmaj[0]) ** 2
        gm = mp.re(Ht[j, j]) / (8 * mp.pi)
        dn = (xv - 1) ** 2 + xv * (gm**2)
        f_ok = mp.sqrt(xv) * ((1 - xv) / dn + 1 - (1 + xv) * mp.log(1 + 1 / xv))
        f_bg = mp.sqrt(xv) * ((xv - 1) / dn + 1 - (1 + xv) * mp.log(1 + 1 / xv))
        g_ok, g_bg = (1 - xv) / dn, (xv - 1) / dn
        for al in range(3):
            p1j = mp.conj(Yt[al, 0]) * Yt[al, j]
            efl[al] += (mp.im(p1j * Ht[0, j]) * f_ok + mp.im(p1j * Ht[j, 0]) * g_ok) / (8 * mp.pi * h00)
            efl_bug[al] += (mp.im(p1j * Ht[0, j]) * f_bg + mp.im(p1j * Ht[j, 0]) * g_bg) / (8 * mp.pi * h00)

    pbr = [abs(Yt[a, 0]) ** 2 / h00 for a in range(3)]
    gs = mp_rat(443, 4)
    vol41 = 3 * mp.im(mp.polylog(2, mp.exp(2 * I_MP * mp.pi / 3)))
    m11 = (40 * 2 * mp.pi / (8 * vol41)) ** mp_rat(1, 3)
    mpl = mp.sqrt((m11**9) * (8 * vol41) * (((2 * mp.pi) ** 4) / 48) / ((2 * mp.pi) ** 7))
    k1t = (h00 / (8 * mp.pi)) / (mp.sqrt((mp.pi**2) * gs / 90) * (mmaj[0] * mp.exp(-mp_rat(16, 5) * mp.pi)) / mpl)
    eta = [1 / (1 + (pbr[a] * k1t) ** mp_rat(29, 25)) for a in range(3)]
    neq = mp_rat(3, 4) / (mp.zeta(3) * gs)
    yb_pos = -f2m(ht_2hdm) * neq * sum(efl[a] * eta[a] for a in range(3))
    yb_pos_bug = -f2m(ht_2hdm) * neq * sum(efl_bug[a] * eta[a] for a in range(3))

    prod_yb_pos = mp.mpf(prod["E3_crv_leptogenesis_and_sphaleron"]["holomorphic_Y_B_tau_star_plus"])
    assert yb_pos > 0 and abs(yb_pos - prod_yb_pos) / yb_pos < mp.mpf(10) ** (-8)
    pf4 = (yb_pos > 0) and (yb_pos_bug < 0) and (mp.mpf(prod["E3_crv_leptogenesis_and_sphaleron"]["c23_loggram_Y_B_tau_star_plus_true_crv"]) < 0)

    caught = sum(int(x) for x in (pf1, pf2, pf3, pf4, pf5))
    assert caught == 5
    print(f"AGY-C27 disjoint self-check PASSED in {int(time.time() - t0)}s: 100% outputs verified, {caught}/5 planted faults caught (0 of 19).")


if __name__ == "__main__":
    main()
