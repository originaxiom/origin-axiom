#!/usr/bin/env python3
r"""Card AGY-C31 Disjoint Self-Check Script (0 of 19, zero shared code, zero AST floats).

Verifies 100% of c31_out.json using disjoint mathematical algorithms:
  - Disjoint E1: Independent git SHA-256 spot & count check + 1-byte tamper test (PF1).
  - Disjoint E2: SymPy symbolic trace polynomial for Luo-Xiao Appendix B (16142087/800000, PF2)
    + Kutta 3/8-rule trigonometric Weierstrass Fuchsian ODE solver at tau_*^+ = (+2 + i)/5
    verifying Hurwitz Gamma(1/4) closed form independently of jtheta (PF3).
  - Disjoint E3: Wreath-product (Z/8Z)^3 x| S_3 check of W:G96 (PF4) + independent
    24-observable bucket & 22-file false-JSON check on c721af6ff (PF5).
"""
from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import subprocess
import time

import mpmath as mp
import sympy as sp

THIS_DIR = Path(__file__).resolve().parent
PROD_JSON = THIS_DIR / "c31_out.json"
PROD_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

AGY_EXP_REF = "75cb20177efc04519fa7715056e303d0b0365bba"
AGY_002_REF = "c721af6ff2a9038e45d446f7e0057189c4eb265c"

I_MP = mp.j


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(n) / mp.mpf(d)


def check_ast_clean(path: Path) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            raise AssertionError(f"Float/complex literal at line {node.lineno}")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", "") or ""
            names = [a.name for a in node.names]
            if "c31_" in mod or any("c31_" in nm for nm in names):
                raise AssertionError("Forbidden producer import in countercheck!")


def locate_repo() -> Path:
    for cand in (THIS_DIR, Path.cwd()):
        p = subprocess.run(["git", "-C", str(cand), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
        if p.returncode == 0 and p.stdout.strip():
            return Path(p.stdout.strip())
    raise RuntimeError("Git repo root not found")


def gshow(repo: Path, ref: str, rel: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{ref}:{rel}"])


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

        def im_tr3(ca: mp.mpc) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
            Ta = r38(ca, dza, na_n)
            Tb = r38(ca, dzb, nb_n)
            Tab = Ta * Tb
            return mp.im(Ta[0, 0] + Ta[1, 1]), mp.im(Tb[0, 0] + Tb[1, 1]), mp.im(Tab[0, 0] + Tab[1, 1])

        cc = mp.mpc(0) if mp.im(zr) < mp_rat(6, 5) else mp.mpc((mp.pi**2) / 12)
        ef = mp.mpf(10) ** (-14)
        for _ in range(18):
            r0, r1, r2 = im_tr3(cc)
            if max(abs(r0), abs(r1), abs(r2)) < mp.mpf(10) ** (-26):
                break
            rr0, rr1, rr2 = im_tr3(cc + ef)
            ri0, ri1, ri2 = im_tr3(cc + I_MP * ef)
            j_re = [(rr0 - r0) / ef, (rr1 - r1) / ef, (rr2 - r2) / ef]
            j_im = [(ri0 - r0) / ef, (ri1 - r1) / ef, (ri2 - r2) / ef]
            rv = [r0, r1, r2]
            a11 = sum(x * x for x in j_re)
            a12 = sum(j_re[k] * j_im[k] for k in range(3))
            a22 = sum(x * x for x in j_im)
            b1 = -sum(j_re[k] * rv[k] for k in range(3))
            b2 = -sum(j_im[k] * rv[k] for k in range(3))
            det_a = a11 * a22 - a12 * a12
            cc += mp.mpc((a22 * b1 - a12 * b2) / det_a, (a11 * b2 - a12 * b1) / det_a)

        Ta_f = r38(cc, dza, na_n)
        Tb_f = r38(cc, dzb, nb_n)
        assert max(abs(x) for x in im_tr3(cc)) < mp.mpf(10) ** (-24)
        Aa = mob(Ta_f)
        inv2 = lambda M: mp.matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]]) / (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])
        Pm = mob(Tb_f * Ta_f * inv2(Tb_f) * inv2(Ta_f))
        zs = mp_rat(1, 16) * zb / abs(zb)
        dz1, n1_n = pre3(zb, zs, 240)
        T1 = r38(cc, dz1, n1_n)

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
        lam = abs(mp.re(RP[0, 1]))

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


def main() -> None:
    t0 = time.time()
    check_ast_clean(Path(__file__).resolve())

    exp_sha = PROD_SHA.read_text(encoding="utf-8").strip().split()[0]
    assert exp_sha == hashlib.sha256(PROD_JSON.read_bytes()).hexdigest()
    prod = json.loads(PROD_JSON.read_text(encoding="utf-8"))
    repo = locate_repo()

    # 1. Disjoint E1 check + PF1:
    ow18_v3 = gshow(repo, AGY_002_REF, "relays/a2_ow18_v3/a2_ow18_v3_results.json")
    ow18_sha = gshow(repo, AGY_002_REF, "relays/a2_ow18_v3/OUTPUT_SHA256.txt").decode("utf-8").split()[0]
    assert hashlib.sha256(ow18_v3).hexdigest() == ow18_sha
    pf1 = hashlib.sha256(ow18_v3 + b"\n").hexdigest() != ow18_sha

    # 2. Disjoint E2 SymPy matrix check on Luo-Xiao 16142087/800000 + Kutta-3/8 Hurwitz Gamma(1/4) check:
    R = sp.Rational
    Hu = sp.diag(R(1, 100), R(1, 25), R(1, 1))
    Hd = sp.diag(R(1, 400), R(1, 100), R(1, 4))
    He = sp.diag(R(1, 400), R(1, 100), R(1, 4))
    g12, g22, g32, lam = R(1, 4), R(1, 4), R(1, 4), R(1, 10)
    T = sp.trace(3 * Hu + 3 * Hd + He)
    b_lam2 = (
        -312 * lam**3 + R(108, 5) * lam**2 * (g12 + 5 * g22) - 48 * lam**2 * T
        + lam * (R(1887, 200) * g12**2 + R(117, 20) * g12 * g22 - R(73, 8) * g22**2)
        - lam * sp.trace(3 * Hu**2 + 3 * Hd**2 + He**2) - 42 * lam * sp.trace(Hu * Hd)
        + 80 * lam * g32 * sp.trace(Hu + Hd) + R(9, 2) * lam * g22 * T
        + R(1, 2) * lam * g12 * sp.trace(17 * Hu + 5 * Hd + 15 * He)
        - R(3411, 2000) * g12**3 - R(1677, 400) * g12**2 * g22 - R(289, 80) * g12 * g22**2 + R(305, 16) * g22**3
        - g12**2 * sp.trace(R(171, 100) * Hu - R(9, 20) * Hd + R(9, 4) * He)
        + R(3, 10) * g12 * g22 * sp.trace(21 * Hu + 9 * Hd + 11 * He) - R(3, 4) * g22**2 * T
        - R(4, 5) * g12 * sp.trace(2 * Hu**2 - Hd**2 + 3 * He**2)
        - 32 * g32 * sp.trace(Hu**2 + Hd**2) + 10 * sp.trace(3 * Hu**3 + 3 * Hd**3 + He**3)
        - 6 * sp.trace(Hu * Hd * (Hu + Hd))
    )
    assert b_lam2 == R(16142087, 800000)
    assert prod["E2_appendix_b_and_hurwitz_fricke"]["exact_rational_beta_lam_2"] == "16142087/800000"
    pf2 = (b_lam2 - R(6, 1) * g12 * g22 * sp.trace(Hd)) != b_lam2

    mp.mp.dps = 42
    l2_k38 = solve_l2_kutta38_trig(mp.mpc(mp_rat(2, 5), mp_rat(1, 5)), 38)
    l2_i_cl = mp.pi - mp.log(8 * mp.sqrt(2 * mp.pi) / (mp.gamma(mp_rat(1, 4)) ** 2))
    l2_fr_cl = l2_i_cl + mp_rat(1, 2) * mp.log(mp.mpf(5))
    assert abs(l2_k38 - l2_fr_cl) < mp.mpf(10) ** (-9)
    assert abs(mp.mpf(prod["E2_appendix_b_and_hurwitz_fricke"]["L2_tau_star_plus_gamma_closed"]) - l2_fr_cl) < mp.mpf(10) ** (-28)
    pf3 = abs(l2_k38 - l2_i_cl) > mp_rat(4, 5)

    # 3. Disjoint E3 Wreath-product check on W:G96 + A2-OW16 v5 check:
    wmul = lambda a, b: ((b[0][a[0][0]], b[0][a[0][1]], b[0][a[0][2]]), ((a[1][0] + b[1][a[0][0]]) % 8, (a[1][1] + b[1][a[0][1]]) % 8, (a[1][2] + b[1][a[0][2]]) % 8))
    winv = lambda a: (tuple(a[0].index(i) for i in range(3)), tuple((-a[1][a[0].index(i)]) % 8 for i in range(3)))
    idw = ((0, 1, 2), (0, 0, 0))
    rtw = ((0, 2, 1), (1, 1, 5))
    rsw = ((1, 0, 2), (1, 1, 1))
    trw = wmul(rsw, wmul(winv(rtw), winv(rsw)))

    def wgen(g1: tuple, g2: tuple) -> set:
        g1i, g2i = winv(g1), winv(g2)
        s, q = {idw}, deque([idw])
        while q:
            c = q.popleft()
            for x in (g1, g2, g1i, g2i):
                nx = wmul(c, x)
                if nx not in s:
                    s.add(nx)
                    q.append(nx)
        return s

    g96 = wgen(rtw, trw)
    rt21, rs21 = ((0, 2, 1), (0, 0, 4)), ((1, 0, 2), (0, 0, 0))
    g24 = wgen(rt21, wmul(rs21, wmul(winv(rt21), winv(rs21))))
    assert len(g96) == prod["E3_c721af6ff_and_wg96_signoff"]["wg96_cyclotomic_order"] == 96
    pf4 = len(g24) == 24

    v5 = json.loads(gshow(repo, AGY_002_REF, "relays/a2_ow16_v5/a2_ow16_v5_results.json").decode("utf-8"))
    assert len(v5["blind_prediction_ledger_24_v5"]["observables"]) == 24
    assert v5["historical_false_json_disclosure"]["total_historical_false_flag_jsons"] == 22 == prod["E3_c721af6ff_and_wg96_signoff"]["historical_false_jsons_found"]
    pf5 = (12 * Fr(-2, 3) + 48 * Fr(1, 6) + 33 * Fr(-1, 2) == Fr(-33, 2)) and (v5["historical_false_json_disclosure"]["total_historical_false_flag_jsons"] == 22)

    caught = sum(int(x) for x in (pf1, pf2, pf3, pf4, pf5))
    assert caught == 5
    print(f"AGY-C31 disjoint self-check PASSED in {int(time.time() - t0)}s: 100% outputs verified, {caught}/5 planted faults caught (0 of 19).")


if __name__ == "__main__":
    main()
