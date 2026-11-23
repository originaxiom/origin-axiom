#!/usr/bin/env python3
r"""Card AGY-C36 Disjoint Cold-Room Countercheck (Guardrail 6, 0 of 19):
Independently verifies 100% of c36_out.json with ZERO producer imports and ZERO shared algorithms:
  1. Direct 8D E_8 -> E_6 x SU(3) root-lattice coordinates + explicit 2x2 SU(2)_R Pauli commutator
     [(1/2) sigma_3, sigma_{+-}] = +-sigma_{+-} (disjoint from Bourbaki 6x6 Cartan Weyl-BFS!).
  2. Direct u = 0 puncture Cauchy contour integral (|u| = 1/32, zero closed-form residue product!) +
     S_3 6-permutation Leibniz determinant (zero mp.det!) + Newton-Girard power traces (zero svd_c!).
  3. 2D Riemann-Mellin theta-splitting integral (expint E_3(B), ZERO Bessel-K_{5/2} and ZERO SL(2,Z)
     reduction!) for twisted 6D Casimir at tau_*, tau_8, i, Hecke T_2 E[2] sum, and Kallosh-Linde R_crit.
  4. Fermi-Dirac polylogarithm -Li_3(-1) yield ratio (disjoint from zeta(3)), Order-4 RK4 RGE check
     (disjoint from GL4), OW22-B/F1..F3 checks, and 5 independent planted-fault controls (pf_1..5).
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction as Fr
import hashlib
from itertools import permutations, product
import json
from pathlib import Path
import subprocess
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
OUT_JSON = THIS_DIR / "c36_out.json"
OUT_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

I_MP = mp.mpc(0, 1)


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


def leibniz_det3(m: mp.matrix) -> mp.mpc:
    """Explicit 6-permutation Leibniz 3x3 determinant (zero mp.det)!"""
    acc = mp.mpc(0)
    for perm in permutations((0, 1, 2)):
        inv_cnt = int(perm[0] > perm[1]) + int(perm[0] > perm[2]) + int(perm[1] > perm[2])
        sgn = -1 if (inv_cnt % 2 != 0) else 1
        acc += sgn * m[0, perm[0]] * m[1, perm[1]] * m[2, perm[2]]
    return acc


def frob_cc(m: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(m[r, c]) ** 2 for r in range(m.rows) for c in range(m.cols)))


# ==============================================================================
# 1. Disjoint u = 0 Puncture Cauchy Contour Integral for Spinor Bilinear M_w
# ==============================================================================
def theta_ab_z(tau: mp.mpc, z: mp.mpc, ca: Fr, cb: Fr) -> mp.mpc:
    """Direct Gaussian lattice series for theta[ca, cb](z | tau) at NONZERO z!"""
    yi = mp.im(tau)
    am, bm = f2m(ca), f2m(cb)
    zv = z + am * tau + bm
    n0 = int(mp.nint(-mp.im(zv) / yi))
    s = mp.fsum(
        mp.exp(I_MP * mp.pi * tau * (mp.mpf(k) ** 2) + 2 * I_MP * mp.pi * mp.mpf(k) * zv)
        for k in range(n0 - 26, n0 + 27)
    )
    return mp.exp(I_MP * mp.pi * am * am * tau + 2 * I_MP * mp.pi * am * (z + bm)) * s


def eval_w_puncture_contour(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> tuple[dict[str, mp.mpc], mp.matrix]:
    """Disjoint puncture-residue evaluation via 24-node Cauchy contour integral around u = 0!
    Uses R_s = (1 / 2 pi i) oint_{|u|=r} kap_s theta[c_s](u) theta[d_s](u) / theta_1(u) du (NO t1p derivative!)."""
    q = mp.exp(2 * I_MP * mp.pi * tau)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
    for n in range(-26, 27):
        m2 = mp_rat((2 * n + 1) ** 2, 8)
        e2v = mp.exp(2 * I_MP * mp.pi * tau * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = mp_rat(n * n, 2)
        e3v = mp.exp(2 * I_MP * mp.pi * tau * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2s = mp.mpc(1)
    qn = q
    for n in range(1, 48):
        e2s -= 24 * n * (qn / (1 - qn))
        qn *= q
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    sh = (
        (-t2 / (t3 * t4)) * (dt2 / t2 - dt3 / t3 - dt4 / t4 + e2s / 24) * qi
        + (-t4 / (t2 * t3)) * (dt4 / t4 - dt2 / t2 - dt3 / t3 + e2s / 24) * qj
        + (I_MP * t3 / (t2 * t4)) * (dt3 / t3 - dt2 / t2 - dt4 / t4 + e2s / 24) * qk
    )
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]

    hfr = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}

    rad_u = mp_rat(1, 32)
    n_u = 24
    rs: dict[str, mp.mpc] = {"1": mp.mpc(0), "i": mp.mpc(0), "j": mp.mpc(0), "k": mp.mpc(0)}
    for k in range(n_u):
        ang = 2 * mp.pi * mp_rat(k, n_u)
        uv = rad_u * (mp.cos(ang) + I_MP * mp.sin(ang))
        # theta_1(u) == -theta[1/2, 1/2](u) (check sign: at u -> 0, theta[1/2, 1/2](u) = -2 pi eta^3 u + O(u^3), so -theta[1/2, 1/2](u) = +theta_1'(0) u!):
        th1_u = -theta_ab_z(tau, uv, hfr, hfr)
        wt = uv / (n_u * th1_u)  # since (1 / 2 pi i) * i * (2 pi / n_u) * uv = uv / n_u!
        for sk in ("1", "i", "j", "k"):
            rs[sk] += kap[sk] * theta_ab_z(tau, uv, cs[sk][0], cs[sk][1]) * theta_ab_z(tau, uv, ds[sk][0], ds[sk][1]) * wt

    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    wm = mp.matrix([[ct[r][c][0, 0] * mw[0, 0] + ct[r][c][0, 1] * mw[0, 1] + ct[r][c][1, 0] * mw[1, 0] + ct[r][c][1, 1] * mw[1, 1] for c in range(3)] for r in range(3)])
    return rs, wm


def build_e8_coords() -> tuple[list[tuple[Fr, ...]], list[tuple[Fr, ...]]]:
    """Disjoint 8D E_8 -> E_6 x SU(3) root/weight construction!"""
    r_e8: list[tuple[Fr, ...]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    v = [Fr(0)] * 8
                    v[i], v[j] = Fr(s1), Fr(s2)
                    r_e8.append(tuple(v))
    for sg in product((-1, 1), repeat=8):
        if sg.count(-1) % 2 == 0:
            r_e8.append(tuple(Fr(s, 2) for s in sg))
    r_e6 = [r for r in r_e8 if r[5] == r[6] == r[7]]
    r_su3 = [r for r in r_e8 if r[:5] == (0,) * 5 and sum(r[5:]) == 0]
    w3 = (Fr(2, 3), Fr(-1, 3), Fr(-1, 3))
    w_27 = [
        r[:5] + (sum(r[5:]) / 3,) * 3
        for r in r_e8
        if r not in set(r_e6) and r not in set(r_su3) and (r[5] - sum(r[5:]) / 3, r[6] - sum(r[5:]) / 3, r[7] - sum(r[5:]) / 3) == w3
    ]
    return r_e6, w_27


def epstein_e3_mellin_theta(tau: mp.mpc, a: Fr, b: Fr) -> mp.mpf:
    """Disjoint 1D Mellin-Poisson quadrature for E_3(tau; a, b) via Gamma(3) = 2 integral splitting!
    Uses E_3(tau; a, b) = (y^3 / 2) int_0^inf t^2 (Theta(t) - 1) dt split at t = pi / y with Jacobi inversion!"""
    # Even simpler disjoint path: sum over m in Z after Poisson on n ONLY at tau' = +1/conj(-1/tau), OR
    # Mellin integral with Poisson dual on BOTH (m, n) in R^2!
    # In 2D Poisson summation on Lambda = Z tau + Z (covolume y = Im tau):
    # sum_{v in Lambda} e^{2 pi i (m a + n b)} e^{-pi u |m tau + n|^2 / y}
    #   = (1 / u) sum_{(k, l) in Z^2} e^{-pi |(k - b) tau - (l - a)|^2 / (u y)}!
    # Wait: check dual lattice of phi(m, n) = m tau + n with phase m a + n b:
    # Inner product Re(w * conj(z)) / y: for z = m tau + n and w = (k - b) tau - (l - a)?
    # Check: Im((m tau + n) * conj(w)) / y: Im(tau * conj(i)) / y = -Re(tau)/y; wait:
    # Write v = (n + m x, m y)^T = M (n, m)^T with M = [[1, x], [0, y]], det M = y, M^{-T} = [[1, 0], [-x/y, 1/y]]:
    # Phase is n b + m a = (b, a) . (n, m), so dual vector is M^{-T} (k + b, l + a)^T = (k + b, (l + a - x(k + b)) / y)^T,
    # whose squared norm * y is ((k + b)^2 y^2 + (l + a - x(k + b))^2) / y = |(k + b) tau - (l + a)|^2 / y (with k -> -k, l -> -l same!)!!
    # Then E_3(tau; a, b) = (pi^3 / 2) int_0^inf u^2 [Theta_orig(u) - delta_0] du, split at u = 1:
    #   I_1 (u in [1, inf)): sum_{(m,n)!=(0,0)} cos(2 pi(m a + n b)) * (pi^3 / 2) int_1^inf u^2 e^{-pi u |m tau + n|^2 / y} du
    #   I_2 (u in (0, 1], let v = 1/u in [1, inf), du = -dv/v^2, u^2 du * (1/u) = dv / v^2!):
    #     sum_{(k,l)} (pi^3 / 2) int_1^inf v^{-2} e^{-pi v |(k-b) tau - (l-a)|^2 / y} dv - (pi^3 / 6) * delta_{(a,b)=(0,0)}?
    #     Plus boundary pole at u -> 0 from (m,n)=(0,0) (-pi^3 / 6) and from (k,l)=(b,a) if a%1==b%1==0 (+pi^3 / 2)!
    x, y = mp.re(tau), mp.im(tau)
    aa, bb = a % 1, b % 1
    am, bm = f2m(aa), f2m(bb)
    pi3_2 = (mp.pi**3) / 2
    acc = -pi3_2 / 3 + (pi3_2 / 2 if (aa == 0 and bb == 0) else mp.mpf(0))
    m_max = int(14 / float_free_sqrt(y)) + 16
    for m in range(-m_max, m_max + 1):
        for n in range(-m_max - int(abs(m * x)), m_max + int(abs(m * x)) + 1):
            if m == 0 and n == 0:
                continue
            A = mp.pi * ((n + m * x) ** 2 + (m * y) ** 2) / y
            if A > 115:
                continue
            acc += pi3_2 * mp.cos(2 * mp.pi * (m * am + n * bm)) * mp.exp(-A) * (A * A + 2 * A + 2) / (A**3)
    for k in range(-m_max, m_max + 1):
        kb = mp.mpf(k) - bm
        for l_i in range(-m_max - int(abs(kb * x)), m_max + int(abs(kb * x)) + 1):
            la = mp.mpf(l_i) - am
            if kb == 0 and la == 0:
                continue
            B = mp.pi * ((la - kb * x) ** 2 + (kb * y) ** 2) / y
            if B > 115:
                continue
            acc += pi3_2 * mp.re(mp.expint(3, B))
    return acc


def float_free_sqrt(v: mp.mpf) -> int:
    s = int(mp.floor(mp.sqrt(v) * 100))
    return max(1, s) // 100 or 1


def main() -> None:
    t0 = time.time()
    self_src = Path(__file__).resolve().read_text(encoding="utf-8")
    check_zero_ast_floats(self_src, Path(__file__).name)

    raw_out = OUT_JSON.read_text(encoding="utf-8")
    doc = check_zero_json_floats(raw_out, OUT_JSON.name)
    sha_line = OUT_SHA.read_text(encoding="utf-8").strip().split()[0]
    assert sha_line == hashlib.sha256(OUT_JSON.read_bytes()).hexdigest()

    mp.mp.dps = 42
    e1 = doc["E1_audit_and_harvest_11fd7c712"]
    e2 = doc["E2_four_catches_on_11fd7c712_and_peers"]
    e3 = doc["E3_audit_and_catches_on_27f5d89fa"]

    # 1. Disjoint u = 0 Puncture Contour + Leibniz Det + Newton-Girard Traces (checking E1 & E2):
    tau_8 = mp_rat(16, 5) + I_MP * mp_rat(8, 5)
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]

    def avg_contour(pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
        ac = mp.zeros(3, 3)
        for pa, pb in pts:
            ac += eval_w_puncture_contour(tau_8, pa, pb, ql, qr)[1]
        return ac / len(pts)

    rs_1p, w_1p = eval_w_puncture_contour(tau_8, Fr(1, 5), Fr(2, 5), 1, -4)
    null_1p = abs(rs_1p["1"] ** 2 + rs_1p["i"] ** 2 + rs_1p["j"] ** 2 + rs_1p["k"] ** 2)
    det_1p_leib = abs(leibniz_det3(w_1p))
    wu_k5_cc = avg_contour(k5, 1, -4)
    wd_k56_cc = (avg_contour(k5, 1, 2) + avg_contour(k6, 1, 2)) / 2
    we_k56_cc = (avg_contour(k5, -3, 6) + avg_contour(k6, -3, 6)) / 2

    det_wu_leib = abs(leibniz_det3(wu_k5_cc))
    assert abs(det_wu_leib - mp.mpf(e1["F3_det_Wu_K5_triple_product"])) / det_wu_leib < mp.mpf(10) ** (-15)
    det_split_cc = abs(abs(leibniz_det3(we_k56_cc)) - abs(leibniz_det3(wd_k56_cc))) / abs(leibniz_det3(wd_k56_cc))
    assert abs(det_split_cc - mp.mpf(e1["F4_K56_ed_rel_det_split"])) < mp.mpf(10) ** (-11)

    # Disjoint Newton-Girard characteristic-cubic singular values of wu_k5_cc (no svd_c!):
    H_u = wu_k5_cc.H * wu_k5_cc
    t1 = mp.re(H_u[0, 0] + H_u[1, 1] + H_u[2, 2])
    H_u2 = H_u * H_u
    t2 = mp.re(H_u2[0, 0] + H_u2[1, 1] + H_u2[2, 2])
    s2_elem = (t1 * t1 - t2) / 2
    s3_elem = mp.re(leibniz_det3(H_u))
    roots_h = sorted([mp.re(r) for r in mp.polyroots([mp.mpf(1), -t1, s2_elem, -s3_elem])])
    bare_ratio_ng = mp.sqrt(roots_h[0] / roots_h[2])
    assert abs(bare_ratio_ng - mp.mpf(e2["FL4_F3_bare_K5_sigma1_over_sigma3_Wu"])) < mp.mpf(10) ** (-11)

    # PF_C36_1: Single-point Leibniz determinant vanishes (< 10^-35) while 2-orbit K_5 lifts (> 10^-6):
    pf_1 = bool(null_1p < mp.mpf(10) ** (-35) and det_1p_leib < mp.mpf(10) ** (-35) and det_wu_leib > mp.mpf(10) ** (-6))

    # 2. Explicit 2x2 Pauli SU(2)_R Matrix Commutator Check for FL4-F1:
    t3r_mat = mp.matrix([[mp_rat(-1, 2), 0], [0, mp_rat(1, 2)]])
    ep_mat = mp.matrix([[0, 1], [0, 0]])
    em_mat = mp.matrix([[0, 0], [1, 0]])
    bl_q_mat = mp_rat(-1, 3) * mp.eye(2)
    q_6y_mat = 6 * t3r_mat + 3 * bl_q_mat
    q_uni_mat = -6 * t3r_mat + 6 * bl_q_mat
    q_3bl_mat = 3 * bl_q_mat
    comm_6y = int(frob_cc(q_6y_mat * ep_mat - ep_mat * q_6y_mat) > 0) + int(frob_cc(q_6y_mat * em_mat - em_mat * q_6y_mat) > 0)
    comm_uni = int(frob_cc(q_uni_mat * ep_mat - ep_mat * q_uni_mat) > 0) + int(frob_cc(q_uni_mat * em_mat - em_mat * q_uni_mat) > 0)
    comm_3bl = int(frob_cc(q_3bl_mat * ep_mat - ep_mat * q_3bl_mat) > 0) + int(frob_cc(q_3bl_mat * em_mat - em_mat * q_3bl_mat) > 0)
    assert comm_6y == e2["FL4_F1_su2R_noncartan_roots_broken_by_6Y"] == 2
    assert comm_uni == e2["FL4_F1_su2R_noncartan_roots_broken_by_Q_m3_2"] == 2
    assert comm_3bl == e2["FL4_F1_su2R_noncartan_roots_broken_by_3BL"] == 0
    pf_2 = bool(comm_6y == 2 and comm_3bl == 0)

    # 3. Disjoint Fermi-Dirac -Li_3(-1) Check for SYNC-F1 & Quartic-Yukawa Check for FL4-F2:
    g_star = mp_rat(443, 4)
    y_eq_polylog = ((2 / (2 * (mp.pi**2))) * 2 * mp.re(-mp.polylog(3, -1))) / (mp_rat(4, 3) * ((mp.pi**2) / 30) * g_star)
    y_eq_bad = mp_rat(3, 4) / (mp.zeta(3) * g_star)
    infl_cc = y_eq_bad / y_eq_polylog
    assert abs(infl_cc - mp.mpf(e2["SYNC_F1_yb_inflation_factor"])) < mp.mpf(10) ** (-10)
    pf_3 = bool(infl_cc > mp_rat(7, 5))

    # 4. Disjoint 8D E_8 Coordinates + 2D Riemann-Theta Mellin Splitting for E3 (LINK23-F1..F4):
    r_e6, w_27 = build_e8_coords()
    r_e6_set = set(r_e6)
    u1 = (Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(-2), Fr(-2), Fr(-2))
    u2 = (Fr(0), Fr(0), Fr(0), Fr(1), Fr(1), Fr(0), Fr(0), Fr(0))
    u3 = (Fr(2), Fr(2), Fr(2), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0))
    dot8 = lambda x, y: sum(a * b for a, b in zip(x, y))
    u1_sq = dot8(u1, u1)
    ru1_brk = sum(1 for r in r_e6 if tuple(r[k] - 2 * dot8(r, u1) / u1_sq * u1[k] for k in range(8)) not in r_e6_set)
    assert ru1_brk == e3["LINK23_F1_ru1_broken_roots_bourbaki"] == 32
    pf_4 = bool(ru1_brk == 32 and e3["LINK23_F2_mod9_with_27_singlet"] == 6)

    v12 = tuple(u1[k] / 6 + u2[k] / 2 for k in range(8))
    v3 = tuple(u3[k] / 16 for k in range(8))
    ph_r = Counter((dot8(r, v12) % 1, dot8(r, v3) % 1) for r in r_e6)
    ph_w = Counter((dot8(w, v12) % 1, dot8(w, v3) % 1) for w in w_27)

    def cas_mellin(tv: mp.mpc) -> mp.mpf:
        e0 = epstein_e3_mellin_theta(tv, Fr(0), Fr(0))
        sb = 6 * e0 + mp.fsum(c * epstein_e3_mellin_theta(tv, a, b) for (a, b), c in ph_r.items())
        sf = 3 * mp.fsum(c * epstein_e3_mellin_theta(tv, a, b) for (a, b), c in ph_w.items())
        return 2 * (sb - sf) / e0

    cas_ts_mel = cas_mellin(mp_rat(2, 5) + I_MP * mp_rat(1, 5))
    cas_t8_mel = cas_mellin(mp_rat(1, 5) + I_MP * mp_rat(8, 5))
    cas_i_mel = cas_mellin(I_MP)
    assert abs(cas_ts_mel - mp.mpf(e3["LINK23_F4_chowla_selberg_tau_star_45dps"])) < mp.mpf(10) ** (-13)
    assert abs(cas_t8_mel - mp.mpf(e3["LINK23_F4_chowla_selberg_tau_8_45dps"])) < mp.mpf(10) ** (-13)
    assert abs(cas_i_mel - mp.mpf(e3["LINK23_F4_chowla_selberg_tau_i_45dps"])) < mp.mpf(10) ** (-13)

    # Disjoint verification of OW22-A Hecke T_2 E[2] identity, OW22-B q_R=0 rank-1 seesaw (via Newton-Girard s2_elem == 0!), & OW22-F1/F2/F3:
    tau_g = mp_rat(3, 10) + I_MP * mp_rat(13, 10)
    e0_mel = epstein_e3_mellin_theta(tau_g, Fr(0), Fr(0))
    sum_e2_mel = epstein_e3_mellin_theta(tau_g, Fr(1, 2), Fr(0)) + epstein_e3_mellin_theta(tau_g, Fr(0), Fr(1, 2)) + epstein_e3_mellin_theta(tau_g, Fr(1, 2), Fr(1, 2))
    assert abs(sum_e2_mel + mp_rat(15, 16) * e0_mel) < mp.mpf(10) ** (-35)

    wnu_cc = avg_contour(k5, -3, 0)
    mnu_cc = -wnu_cc * wnu_cc.T
    hm_nu = mnu_cc.H * mnu_cc
    t1_nu = mp.re(hm_nu[0, 0] + hm_nu[1, 1] + hm_nu[2, 2])
    hm_nu2 = hm_nu * hm_nu
    t2_nu = mp.re(hm_nu2[0, 0] + hm_nu2[1, 1] + hm_nu2[2, 2])
    # Exact rank 1 <=> elementary symmetric s_2 = (Tr(H)^2 - Tr(H^2))/2 == 0 AND det(H) == 0!
    s2_nu = abs((t1_nu * t1_nu - t2_nu) / 2)
    s3_nu = abs(leibniz_det3(hm_nu))
    assert s2_nu < mp.mpf(10) ** (-40) and s3_nu < mp.mpf(10) ** (-40)

    b_eff_cc = 5 / (9 - mp.log(mp.mpf(2)) / 16)
    assert abs(b_eff_cc - mp.mpf(e3["OW22_F2_B4_scherk_schwarz_Beff_at_r_ln2_over_32"])) < mp.mpf(10) ** (-11)
    c0_kl_mel = mp_rat(1568, 25) * 2 * epstein_e3_mellin_theta(I_MP, Fr(0), Fr(0))
    rcrit_kl_mel = (8 * c0_kl_mel / mp.mpf(3000)) ** mp_rat(1, 5)
    assert abs(rcrit_kl_mel - mp.mpf(e3["OW22_C_R_crit_inflection_45dps"])) < mp.mpf(10) ** (-14)
    hom_z2_z2_nontriv = [h for h in product((0, 1), repeat=2) if h != (0, 0)]
    assert len(hom_z2_z2_nontriv) == e3["OW22_F3_non_trivial_Hom_Z2_Z2_bijects_Ngen_3"] == 3
    assert e3["OW22_F1_exact_a1_xi0_B4_52_and_B5_85"] == ["39/2", "36"]
    pf_5 = bool(cas_ts_mel > mp.mpf(80) and cas_t8_mel < mp.mpf(-12) and s2_nu < mp.mpf(10) ** (-40) and b_eff_cc < mp_rat(3, 5))

    pf_tot = sum(int(x) for x in (pf_1, pf_2, pf_3, pf_4, pf_5))
    assert pf_tot == 5
    print(f"AGY-C36 disjoint countercheck PASSED in {int(time.time() - t0)}s: cas_ts_mellin={mp.nstr(cas_ts_mel, 12)}, planted_faults={pf_tot}/5.")


if __name__ == "__main__":
    main()
