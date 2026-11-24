#!/usr/bin/env python3
"""Cold-room zero-shared-code disjoint countercheck for Card AGY-C38 (0 of 19).

Uses strictly disjoint algorithms across all three sections:
- E1: Python `tokenize` stream inspection of 639a5d46b:verify_x_bulk_link1_v4.py
      (confirming :992, :1141, :1143-1145, :1164, :1174 vs :1152-1156 PC_BL1_5).
- E2a: Explicit 32x32 Cl(10) Clifford gamma-matrix construction + chirality projector P_+
       + 32x32 matrix traces for all 6 G_SM x U(1)_chi anomalies (no weight tuples!).
- E2b: 2D Riemann-Mellin + Euler-pentagonal contour 4-modulus solver for s_* +
       numerical finite-difference Hessian of V_D = (1/2) D_chi^2 and Wirtinger derivatives
       of D_chi for STr M_{Z'_chi}^2 == 0, scrambled via mp.expm SO(4) x U(3).
- E3a: 4x4 Vandermonde linear extraction of (lambda_1..lambda_4) from V_DF without
       analytic formulas, scrambled via mp.expm SU(2)_L x U(1)_Y.
- E3b: git cat-file / diff-tree custody check of 71b1718a1 + trigonometric csc^2 +
       Order-24 Wronskian matrix-inversion solver for Lamé b_c^*(tau_8^+).
"""
from __future__ import annotations

import ast
from fractions import Fraction as Fr
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import time
import tokenize

import mpmath as mp

THIS_FILE = Path(__file__).resolve()
THIS_DIR = THIS_FILE.parent
PROD_PY = THIS_DIR / "c38_remediate_c37_bl1_citations_and_b1_b4_b6_audit.py"
OUT_JSON = THIS_DIR / "c38_out.json"

AGY_EXP_COMMIT = "639a5d46b"
AGY_002_COMMIT = "71b1718a1"
AGY_002_BASE = "2d993276b"

I_MP = mp.mpc(0, 1)


def mp_rat(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def f2m(fr: Fr) -> mp.mpf:
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def p10(exp_i: int) -> mp.mpf:
    return mp.mpf(10) ** exp_i


def find_repo_root() -> Path:
    env_repo = os.environ.get("ORIGIN_AXIOM_REPO", "").strip()
    if env_repo:
        cand = Path(env_repo).resolve()
        if (cand / ".git").exists():
            return cand
    for anc in (THIS_DIR, *THIS_DIR.parents):
        if (anc / ".git").exists():
            return anc
    raise RuntimeError("Could not locate git repository root.")


def git_cat_blob(repo: Path, spec: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), "cat-file", "blob", spec])


def check_ast_zero_floats(py_file: Path) -> None:
    tree = ast.parse(py_file.read_text(encoding="utf-8"), filename=py_file.name)
    bad = [
        (n.lineno, n.value)
        for n in ast.walk(tree)
        if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex))
    ]
    assert not bad, f"AST float/complex found in {py_file.name}: {bad}"


def check_no_json_floats(obj: object, path_str: str = "$") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"JSON float at {path_str}: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            check_no_json_floats(v, f"{path_str}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            check_no_json_floats(v, f"{path_str}[{i}]")


# ---------------------------------------------------------------------------
# Disjoint E2a: 32x32 Cl(10) Gamma Matrices & Matrix-Trace Anomaly Check
# ---------------------------------------------------------------------------
def kron2(A: mp.matrix, B: mp.matrix) -> mp.matrix:
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    out = mp.zeros(ra * rb, ca * cb)
    for r1 in range(ra):
        for c1 in range(ca):
            v = A[r1, c1]
            if v == 0:
                continue
            for r2 in range(rb):
                for c2 in range(cb):
                    out[r1 * rb + r2, c1 * cb + c2] = v * B[r2, c2]
    return out


def kron_list(mats: list[mp.matrix]) -> mp.matrix:
    acc = mats[0]
    for m in mats[1:]:
        acc = kron2(acc, m)
    return acc


def build_cl10_and_verify_anomalies() -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    i2 = mp.eye(2)
    s1 = mp.matrix([[0, 1], [1, 0]])
    s2 = mp.matrix([[0, -I_MP], [I_MP, 0]])
    s3 = mp.matrix([[1, 0], [0, -1]])

    gammas: list[mp.matrix] = []
    for k in range(5):
        prefix = [s3] * k
        suffix = [i2] * (4 - k)
        gammas.append(kron_list(prefix + [s1] + suffix))
        gammas.append(kron_list(prefix + [s2] + suffix))

    # Chirality operator Gamma_11 = (-i)^5 Gamma_1 ... Gamma_10 = s3^(x5):
    g11 = (-I_MP) ** 5 * kron_list([i2] * 5)
    for gm in gammas:
        g11 = g11 * gm
    # Note: In our convention each (Gamma_{2a-1}, Gamma_{2a}) pair has (-i) s1 s2 = +s3,
    # so prod_{a=1}^5 (-i Gamma_{2a-1} Gamma_{2a}) = s3^(x5), and even-# of (-1) eigenvalues
    # corresponds to Gamma_11 = +1 => P_+ = (I_32 + g11)/2!
    i32 = mp.eye(32)
    p_plus = (i32 + g11) / 2
    tr_p_plus = mp.re(sum(p_plus[d, d] for d in range(32)))
    assert abs(tr_p_plus - 16) < p10(-45)

    # Spin(10) generators Sigma_{a,b} = -(i/4)[Gamma_a, Gamma_b] (0-indexed a,b in 0..9):
    def sig_ab(a: int, b: int) -> mp.matrix:
        return (-I_MP / 4) * (gammas[a] * gammas[b] - gammas[b] * gammas[a])

    # Cartan generators H_k = Sigma_{2k, 2k+1} = +(1/2) s3 on factor k (eigenvalues +/- 1/2):
    H = [sig_ab(2 * k, 2 * k + 1) for k in range(5)]

    # Complexified creation/annihilation combinations for SU(3)_C (k=0,1,2) and SU(2)_L (k=3,4):
    # Raising/lowering between slot a and slot b preserving H_a + H_b:
    # T^{(sym)}_{ab} = (1/2)(Sigma_{2a, 2b} + Sigma_{2a+1, 2b+1}), T^{(skew)}_{ab} = (1/2)(Sigma_{2a, 2b+1} - Sigma_{2a+1, 2b})
    def su_pair(a: int, b: int) -> tuple[mp.matrix, mp.matrix]:
        t_re = mp_rat(1, 2) * (sig_ab(2 * a, 2 * b) + sig_ab(2 * a + 1, 2 * b + 1))
        t_im = mp_rat(1, 2) * (sig_ab(2 * a, 2 * b + 1) - sig_ab(2 * a + 1, 2 * b))
        return t_re, t_im

    su3_gens: list[mp.matrix] = []
    for a, b in ((0, 1), (0, 2), (1, 2)):
        tr_m, ti_m = su_pair(a, b)
        su3_gens.extend([tr_m, ti_m])
    su3_gens.append(mp_rat(1, 2) * (H[0] - H[1]))
    su3_gens.append((mp.mpf(1) / (2 * mp.sqrt(3))) * (H[0] + H[1] - 2 * H[2]))

    su2_re, su2_im = su_pair(3, 4)
    su2_gens = [su2_re, su2_im, mp_rat(1, 2) * (H[3] - H[4])]

    # Verify Tr(P_+ [G, Q_chi]) == 0 and [G, 6Y] == 0 on all 8 SU(3)_C and 3 SU(2)_L generators!
    mat_6y = 2 * (H[0] + H[1] + H[2]) - 3 * (H[3] + H[4])
    mat_qchi = -2 * (H[0] + H[1] + H[2] + H[3] + H[4])
    comm_err = mp.mpf(0)
    for g_m in su3_gens + su2_gens:
        c1 = g_m * mat_6y - mat_6y * g_m
        c2 = g_m * mat_qchi - mat_qchi * g_m
        comm_err = max(
            comm_err,
            max(abs(c1[r, c]) for r in range(32) for c in range(32)),
            max(abs(c2[r, c]) for r in range(32) for c in range(32)),
        )
    assert comm_err < p10(-45)

    def tr32(M: mp.matrix) -> mp.mpc:
        return sum((M[d, d] for d in range(32)), mp.mpc(0))

    # Compute all 6 anomalies directly via 32x32 matrix traces on P_+:
    anom_su3 = max(abs(mp_rat(1, 2) * tr32(p_plus * (ga * gb + gb * ga) * mat_qchi)) for ga in su3_gens for gb in su3_gens)
    anom_su2 = max(abs(mp_rat(1, 2) * tr32(p_plus * (ga * gb + gb * ga) * mat_qchi)) for ga in su2_gens for gb in su2_gens)
    anom_y2_chi = abs(tr32(p_plus * mat_6y * mat_6y * mat_qchi))
    anom_y_chi2 = abs(tr32(p_plus * mat_6y * mat_qchi * mat_qchi))
    anom_grav_chi = abs(tr32(p_plus * mat_qchi))
    anom_chi3 = abs(tr32(p_plus * mat_qchi * mat_qchi * mat_qchi))
    max_anom_err = max(anom_su3, anom_su2, anom_y2_chi, anom_y_chi2, anom_grav_chi, anom_chi3)
    assert max_anom_err < p10(-45)

    # Disjoint Control 2: Project out the unique SU(5)-singlet nu^c state (where all H_k = +1/2):
    p_nuc = i32
    for hk in H:
        p_nuc = p_nuc * (mp_rat(1, 2) * i32 + hk)
    p_15 = p_plus - p_nuc
    assert abs(tr32(p_15) - 15) < p10(-45)
    su3_15 = max(abs(mp_rat(1, 2) * tr32(p_15 * (ga * gb + gb * ga) * mat_qchi)) for ga in su3_gens for gb in su3_gens)
    su2_15 = max(abs(mp_rat(1, 2) * tr32(p_15 * (ga * gb + gb * ga) * mat_qchi)) for ga in su2_gens for gb in su2_gens)
    y2_15 = abs(tr32(p_15 * mat_6y * mat_6y * mat_qchi))
    yc2_15 = abs(tr32(p_15 * mat_6y * mat_qchi * mat_qchi))
    grav_15 = mp.re(tr32(p_15 * mat_qchi))
    chi3_15 = mp.re(tr32(p_15 * mat_qchi * mat_qchi * mat_qchi))
    assert max(su3_15, su2_15, y2_15, yc2_15) < p10(-45)
    return max_anom_err, grav_15, chi3_15


# ---------------------------------------------------------------------------
# Disjoint E2b: 2D Riemann-Mellin + Euler-Pentagonal 4-Modulus Solver & FD STr
# ---------------------------------------------------------------------------
def epstein_e3_mellin_theta(tau: mp.mpc, a: Fr, b: Fr) -> mp.mpf:
    aa, bb = a % 1, b % 1
    x, y = mp.re(tau), mp.im(tau)
    am, bm = f2m(aa), f2m(bb)
    acc = (mp_rat(1, 2) if (aa == 0 and bb == 0) else mp.mpf(0)) - mp_rat(1, 3)
    m_lim = int(mp.ceil(mp.sqrt(116 / y))) + 2
    n_hw = int(mp.ceil(mp.sqrt(116 * y))) + 2
    for m in range(-m_lim, m_lim + 1):
        n0 = int(mp.floor(-m * x))
        for dn in range(-n_hw, n_hw + 1):
            n = n0 + dn
            if m != 0 or n != 0:
                u = mp.pi * (abs(m * tau + n) ** 2) / y
                if u < 135:
                    acc += mp.cos(2 * mp.pi * (m * am + n * bm)) * ((2 + 2 * u + u * u) / (u ** 3)) * mp.exp(-u)
    for k2 in range(-m_lim, m_lim + 1):
        w2 = mp.mpf(k2) + bm
        k1_0 = int(mp.floor(w2 * x - am))
        for dk1 in range(-n_hw, n_hw + 1):
            w1 = mp.mpf(k1_0 + dk1) + am
            if w1 != 0 or w2 != 0:
                u_d = mp.pi * (abs(w1 - w2 * tau) ** 2) / y
                if u_d < 135:
                    acc += mp.re(mp.expint(3, u_d))
    return (mp.pi ** 3 / 2) * acc


def dkl_pentagonal_contour(tau: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
    def log_eta_pent(tv: mp.mpc) -> mp.mpc:
        q = mp.exp(2 * I_MP * mp.pi * tv)
        s = mp.mpc(1)
        for k in range(1, 90):
            e1 = k * (3 * k - 1) // 2
            e2 = k * (3 * k + 1) // 2
            t1, t2 = q ** e1, q ** e2
            if abs(t1) < p10(-56):
                break
            sg = -1 if (k % 2 == 1) else 1
            s += sg * (t1 + t2)
        return I_MP * mp.pi * tv / 12 + mp.log(s)

    y = mp.im(tau)
    le0 = log_eta_pent(tau)
    eta4 = abs(mp.exp(le0)) ** 4
    rad = mp_rat(1, 32)
    dle = mp.mpc(0)
    for k in range(32):
        ang = 2 * mp.pi * mp_rat(k, 32)
        u = rad * (mp.cos(ang) + I_MP * mp.sin(ang))
        dle += log_eta_pent(tau + u) / (32 * u)
    e2 = dle * (12 / (I_MP * mp.pi))
    hat_e2 = e2 - 3 / (mp.pi * y)
    inv_e = 1 / (2 * y * eta4)
    return inv_e, 2 * inv_e * (y ** 2) * (abs(hat_e2) ** 2)


def c_cas_mellin(tau: mp.mpc) -> mp.mpf:
    a1, a2 = Fr(1, 2), Fr(1, 2)
    tot = mp.mpf(1024) * (epstein_e3_mellin_theta(tau, Fr(0), Fr(0)) - epstein_e3_mellin_theta(tau, a1, a2))
    for mult, g1, g2 in [(8, Fr(0), Fr(1, 2)), (12, Fr(1, 2), Fr(0)), (12, Fr(1, 2), Fr(1, 2))]:
        tot -= mp.mpf(4 * mult) * (epstein_e3_mellin_theta(tau, g1, g2) - epstein_e3_mellin_theta(tau, g1 + a1, g2 + a2))
    for mult_h, g1, g2 in [(12, Fr(1, 2), Fr(1, 4)), (4, Fr(0), Fr(1, 2))]:
        tot += mp.mpf(4 * mult_h) * (epstein_e3_mellin_theta(tau, g1, g2) - epstein_e3_mellin_theta(tau, g1 + a1, g2 + a2))
    return tot / (2 * (mp.pi ** 7))


def solve_s_star_mellin_coord_secant() -> mp.mpf:
    """Independent 4x4 damped Newton minimization using 2D Riemann-Mellin + Euler pentagonal DKL!"""
    old = mp.mp.dps
    mp.mp.dps = 54
    try:
        gr2 = mp_rat(1, 600)
        x = [mp.mpf(303), mp.mpf(32), mp_rat(17, 20), mp_rat(2, 5)]

        def eval_vm_direct(tv: mp.mpf, sv: mp.mpf, rx: mp.mpf, ry: mp.mpf) -> mp.mpf:
            ie, ft = dkl_pentagonal_contour(rx + I_MP * ry)
            cc = c_cas_mellin(rx + I_MP * ry)
            p1, p2 = 2 * mp.pi / 36, 2 * mp.pi / 48
            ws = 3 * mp.exp(-p1 * sv) - mp.exp(-p2 * sv)
            dws = -3 * p1 * mp.exp(-p1 * sv) + p2 * mp.exp(-p2 * sv)
            dsw = dws - ws / (2 * sv)
            v_ss = ((2 * gr2 * tv - 1) ** 2) / (2 * gr2 * sv * (tv ** 3))
            v_f = (1 / (4 * sv * tv)) * (ie * (4 * (sv ** 2) * (dsw ** 2) - 2 * (ws ** 2)) + (mp.pi ** 2 / 18) * ft * (ws ** 2))
            return v_ss + v_f + cc / ((sv ** 2) * (tv ** 2))

        for hs, n_it in [
            ([p10(-10), p10(-11), p10(-12), p10(-12)], 8),
            ([p10(-14), p10(-15), p10(-16), p10(-16)], 3),
        ]:
            for _ in range(n_it):
                tau_c: dict[tuple[int, int], tuple[mp.mpf, mp.mpf, mp.mpf]] = {}
                for ix in (-1, 0, 1):
                    for iy in (-1, 0, 1):
                        tp = (x[2] + ix * hs[2]) + I_MP * (x[3] + iy * hs[3])
                        ie_m, ft_m = dkl_pentagonal_contour(tp)
                        tau_c[(ix, iy)] = (ie_m, ft_m, c_cas_mellin(tp))

                def vm(ta: mp.mpf, sa: mp.mpf, ix: int, iy: int) -> mp.mpf:
                    ie, ft, cc = tau_c[(ix, iy)]
                    p1, p2 = 2 * mp.pi / 36, 2 * mp.pi / 48
                    ws = 3 * mp.exp(-p1 * sa) - mp.exp(-p2 * sa)
                    dws = -3 * p1 * mp.exp(-p1 * sa) + p2 * mp.exp(-p2 * sa)
                    dsw = dws - ws / (2 * sa)
                    v_ss = ((2 * gr2 * ta - 1) ** 2) / (2 * gr2 * sa * (ta ** 3))
                    v_f = (1 / (4 * sa * ta)) * (ie * (4 * (sa ** 2) * (dsw ** 2) - 2 * (ws ** 2)) + (mp.pi ** 2 / 18) * ft * (ws ** 2))
                    return v_ss + v_f + cc / ((sa ** 2) * (ta ** 2))

                v0 = vm(x[0], x[1], 0, 0)
                gr = mp.zeros(4, 1)
                hm = mp.zeros(4, 4)
                gr[0, 0] = (vm(x[0] + hs[0], x[1], 0, 0) - vm(x[0] - hs[0], x[1], 0, 0)) / (2 * hs[0])
                gr[1, 0] = (vm(x[0], x[1] + hs[1], 0, 0) - vm(x[0], x[1] - hs[1], 0, 0)) / (2 * hs[1])
                gr[2, 0] = (vm(x[0], x[1], 1, 0) - vm(x[0], x[1], -1, 0)) / (2 * hs[2])
                gr[3, 0] = (vm(x[0], x[1], 0, 1) - vm(x[0], x[1], 0, -1)) / (2 * hs[3])
                gn = mp.sqrt(mp.fsum(gr[i, 0] ** 2 for i in range(4)))
                if gn < p10(-40):
                    break
                hm[0, 0] = (vm(x[0] + hs[0], x[1], 0, 0) - 2 * v0 + vm(x[0] - hs[0], x[1], 0, 0)) / (hs[0] ** 2)
                hm[1, 1] = (vm(x[0], x[1] + hs[1], 0, 0) - 2 * v0 + vm(x[0], x[1] - hs[1], 0, 0)) / (hs[1] ** 2)
                hm[2, 2] = (vm(x[0], x[1], 1, 0) - 2 * v0 + vm(x[0], x[1], -1, 0)) / (hs[2] ** 2)
                hm[3, 3] = (vm(x[0], x[1], 0, 1) - 2 * v0 + vm(x[0], x[1], 0, -1)) / (hs[3] ** 2)
                hm[0, 1] = hm[1, 0] = (vm(x[0] + hs[0], x[1] + hs[1], 0, 0) - vm(x[0] + hs[0], x[1] - hs[1], 0, 0) - vm(x[0] - hs[0], x[1] + hs[1], 0, 0) + vm(x[0] - hs[0], x[1] - hs[1], 0, 0)) / (4 * hs[0] * hs[1])
                for ci, (px, py) in [(2, (1, 0)), (3, (0, 1))]:
                    hm[0, ci] = hm[ci, 0] = (vm(x[0] + hs[0], x[1], px, py) - vm(x[0] + hs[0], x[1], -px, -py) - vm(x[0] - hs[0], x[1], px, py) + vm(x[0] - hs[0], x[1], -px, -py)) / (4 * hs[0] * hs[ci])
                    hm[1, ci] = hm[ci, 1] = (vm(x[0], x[1] + hs[1], px, py) - vm(x[0], x[1] + hs[1], -px, -py) - vm(x[0], x[1] - hs[1], px, py) + vm(x[0], x[1] - hs[1], -px, -py)) / (4 * hs[1] * hs[ci])
                hm[2, 3] = hm[3, 2] = (vm(x[0], x[1], 1, 1) - vm(x[0], x[1], 1, -1) - vm(x[0], x[1], -1, 1) + vm(x[0], x[1], -1, -1)) / (4 * hs[2] * hs[3])
                hs_reg = (hm + hm.T) / 2
                evs, _ = mp.eighe(hs_reg)
                min_ev = min(mp.re(e) for e in evs)
                max_ev = max(abs(mp.re(e)) for e in evs)
                if min_ev <= 0:
                    hs_reg += (abs(min_ev) + max_ev * mp_rat(1, 1000)) * mp.eye(4)
                step = mp.lu_solve(hs_reg, -gr)
                al = mp.mpf(1)
                for _ in range(20):
                    nx = [x[i] + al * step[i, 0] for i in range(4)]
                    if nx[0] > 10 and nx[1] > 5 and nx[3] > mp_rat(1, 20):
                        vn = eval_vm_direct(nx[0], nx[1], nx[2], nx[3])
                        if vn < v0 or gn < p10(-15):
                            x = nx
                            break
                    al /= 2
        return x[1]
    finally:
        mp.mp.dps = old


# ---------------------------------------------------------------------------
# Disjoint E3b: Trigonometric csc^2 + Order-24 Wronskian Lamé L_2(tau_8^+)
# ---------------------------------------------------------------------------
def solve_l2_trig_wronskian(tau: mp.mpc, work_dps: int = 50) -> mp.mpf:
    old = mp.mp.dps
    mp.mp.dps = work_dps
    try:
        z = mp.mpc(tau)
        shift = mp.mpf(0)
        for _ in range(100):
            z -= int(mp.nint(mp.re(z)))
            if abs(z) < mp.mpf(1) - p10(-34):
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
            wp_exact = (mp.pi ** 2) / (sn ** 2) - (mp.pi ** 2) / 3
            wpp_s = -2 * (mp.pi ** 3) * cs / (sn ** 3)
            for m_strip in range(1, 38):
                up = mp.pi * (zc + m_strip * z_lat)
                um = mp.pi * (zc - m_strip * z_lat)
                u0 = mp.pi * m_strip * z_lat
                sup, cup = mp.sin(up), mp.cos(up)
                sum_, cum = mp.sin(um), mp.cos(um)
                wp_exact += (mp.pi ** 2) * (1 / (sup ** 2) + 1 / (sum_ ** 2) - 2 / (mp.sin(u0) ** 2))
                wpp_s -= 2 * (mp.pi ** 3) * (cup / (sup ** 3) + cum / (sum_ ** 3))
            return wp_exact, wpp_s

        p_ord = 24
        qr = mp_rat(1, 4)

        def prop_t24(nodes: list[mp.mpc], c_v: mp.mpc, want_dc: bool):
            T = mp.eye(2)
            dT = mp.zeros(2, 2)
            for idx in range(len(nodes) - 1):
                zk = nodes[idx]
                h = nodes[idx + 1] - zk
                p0, p1 = wp_wpp_trig(zk)
                pa = [mp.mpc(0)] * (p_ord + 1)
                pa[0], pa[1] = p0, p1
                pa[2] = 3 * (p0 ** 2) - qr * g2
                for m in range(1, p_ord - 1):
                    pa[m + 2] = mp_rat(6, (m + 2) * (m + 1)) * mp.fsum(pa[j] * pa[m - j] for j in range(m + 1))
                qa = [qr * pa[m] for m in range(p_ord + 1)]
                qa[0] += c_v
                Tn = mp.zeros(2, 2)
                dTn = mp.zeros(2, 2)
                hp = [h ** m for m in range(p_ord + 3)]
                for col in range(2):
                    wc = [mp.mpc(0)] * (p_ord + 3)
                    wc[0], wc[1] = T[0, col], T[1, col]
                    for m in range(p_ord + 1):
                        wc[m + 2] = -mp.fsum(qa[j] * wc[m - j] for j in range(m + 1)) / ((m + 2) * (m + 1))
                    Tn[0, col] = mp.fsum(wc[m] * hp[m] for m in range(p_ord + 3))
                    Tn[1, col] = mp.fsum(m * wc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                    if want_dc:
                        dwc = [mp.mpc(0)] * (p_ord + 3)
                        dwc[0], dwc[1] = dT[0, col], dT[1, col]
                        for m in range(p_ord + 1):
                            dwc[m + 2] = -(wc[m] + mp.fsum(qa[j] * dwc[m - j] for j in range(m + 1))) / ((m + 2) * (m + 1))
                        dTn[0, col] = mp.fsum(dwc[m] * hp[m] for m in range(p_ord + 3))
                        dTn[1, col] = mp.fsum(m * dwc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                T, dT = Tn, dTn
            return (T, dT) if want_dc else T

        z0 = mp_rat(1, 2) + mp_rat(1, 2) * z_lat
        n_st = 60
        nds_a = [z0 + mp_rat(k, n_st) for k in range(n_st + 1)]
        nds_b = [z0 + mp_rat(k, n_st) * z_lat for k in range(n_st + 1)]
        c_val = mp.mpc((mp.pi ** 2) / 12)
        for _ in range(18):
            Ta, dTa = prop_t24(nds_a, c_val, True)
            Tb, dTb = prop_t24(nds_b, c_val, True)
            Tab = Ta * Tb
            dTab = dTa * Tb + Ta * dTb
            rv = [mp.im(Ta[0, 0] + Ta[1, 1]), mp.im(Tb[0, 0] + Tb[1, 1]), mp.im(Tab[0, 0] + Tab[1, 1])]
            if max(abs(x) for x in rv) < p10(-36):
                break
            trs = [dTa[0, 0] + dTa[1, 1], dTb[0, 0] + dTb[1, 1], dTab[0, 0] + dTab[1, 1]]
            jr = [mp.im(t) for t in trs]
            ji = [mp.re(t) for t in trs]
            a11 = sum(x * x for x in jr)
            a12 = sum(jr[k] * ji[k] for k in range(3))
            a22 = sum(x * x for x in ji)
            b1 = -sum(jr[k] * rv[k] for k in range(3))
            b2 = -sum(ji[k] * rv[k] for k in range(3))
            det_a = a11 * a22 - a12 * a12
            c_val += mp.mpc((a22 * b1 - a12 * b2) / det_a, (a11 * b2 - a12 * b1) / det_a)

        Ta = prop_t24(nds_a, c_val, False)
        Tb = prop_t24(nds_b, c_val, False)
        inv2 = lambda M: mp.matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]]) / (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])

        m_ord = 60
        laur = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, m_ord // 2 + 2):
            laur[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * mp.fsum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
        qc = [mp.mpc(0)] * (m_ord + 1)
        qc[0] = c_val
        for n in range(1, m_ord // 2 + 1):
            qc[2 * n] = qr * laur[n]
        al = [mp.mpc(0)] * (m_ord + 1)
        be = [mp.mpc(0)] * (m_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, m_ord + 1):
            al[m] = -mp.fsum(qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + mp.fsum(qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)

        zs = mp_rat(1, 30) * z0 / abs(z0)
        n_rad = 68
        rat_r = abs(zs) / abs(z0)
        M_to_s = prop_t24([z0 * (rat_r ** mp_rat(k, n_rad)) for k in range(n_rad + 1)], c_val, False)
        zh = mp.sqrt(zs)
        sa = mp.fsum(al[m] * (zs ** m) for m in range(m_ord + 1))
        dsa = mp.fsum(m * al[m] * (zs ** (m - 1)) for m in range(1, m_ord + 1))
        sb = mp.fsum(be[m] * (zs ** m) for m in range(m_ord + 1))
        dsb = mp.fsum(m * be[m] * (zs ** (m - 1)) for m in range(1, m_ord + 1))
        w_reg = zh * sa
        dw_reg = (sa / (2 * zh)) + zh * dsa
        ln_zs = mp.log(zs)
        w_log = w_reg * ln_zs + zh * sb
        dw_log = dw_reg * ln_zs + w_reg / zs + (sb / (2 * zh)) + zh * dsb
        F_s = mp.matrix([[w_reg, w_log], [dw_reg, dw_log]])
        K = inv2(M_to_s) * F_s
        MA_F = inv2(K) * Ta * K
        Mb_F = inv2(K) * Tb * K
        C_v = mp.matrix([[0, 1], [I_MP, 0]])
        M_v = C_v * MA_F.T * inv2(C_v)
        Mb_v = C_v * Mb_F.T * inv2(C_v)
        h_hor = -mp.im(M_v[1, 1]) / mp.re(M_v[1, 0])
        h_hor_b = -mp.im(Mb_v[1, 1]) / mp.re(Mb_v[1, 0])
        assert abs(h_hor - h_hor_b) < p10(-32)
        return (mp.pi + h_hor) + shift
    finally:
        mp.mp.dps = old


def expm_so4(seed: int) -> mp.matrix:
    a = mp.zeros(4, 4)
    for r in range(4):
        for c in range(r + 1, 4):
            v = mp_rat(((7 * seed + 3 * r + 5 * c + 2) % 11) - 5, 13)
            a[r, c] = v
            a[c, r] = -v
    return mp.expm(a)


def expm_u3(seed: int) -> mp.matrix:
    hm = mp.zeros(3, 3)
    for r in range(3):
        hm[r, r] = mp_rat(((3 * seed + 2 * r + 1) % 9) - 4, 8)
        for c in range(r + 1, 3):
            zv = mp_rat(((5 * seed + r + 2 * c + 1) % 7) - 3, 9) + I_MP * mp_rat(((7 * seed + 3 * r + c + 2) % 9) - 4, 11)
            hm[r, c] = zv
            hm[c, r] = mp.conj(zv)
    return mp.expm(I_MP * hm)


def expm_su2(seed: int) -> mp.matrix:
    hm = mp.zeros(2, 2)
    d = mp_rat(((5 * seed + 3) % 7) - 3, 8)
    z = mp_rat(((3 * seed + 1) % 9) - 4, 9) + I_MP * mp_rat(((7 * seed + 2) % 11) - 5, 10)
    hm[0, 0] = d
    hm[1, 1] = -d
    hm[0, 1] = z
    hm[1, 0] = mp.conj(z)
    return mp.expm(I_MP * hm)


def main() -> None:
    t0 = time.time()
    mp.mp.dps = 52
    repo = find_repo_root()

    check_ast_zero_floats(THIS_FILE)
    check_ast_zero_floats(PROD_PY)

    out_doc = json.loads(OUT_JSON.read_text(encoding="utf-8"))
    check_no_json_floats(out_doc)
    out_sha_file = THIS_DIR / "OUTPUT_SHA256.txt"
    if out_sha_file.exists():
        exp_h, fn = out_sha_file.read_text(encoding="utf-8").strip().split()
        assert hashlib.sha256((THIS_DIR / fn).read_bytes()).hexdigest() == exp_h

    # ==========================================================================
    # PF_CC_1: Token-stream verification of 639a5d46b:verify_x_bulk_link1_v4.py
    # ==========================================================================
    peer_py = git_cat_blob(repo, f"{AGY_EXP_COMMIT}:relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4.py").decode("utf-8")
    name_lines: dict[str, list[int]] = {}
    for tok in tokenize.generate_tokens(io.StringIO(peer_py).readline):
        if tok.type == tokenize.NAME and tok.string in ("b1_g", "b_mssm", "run_gbs8_rge", "det_single_pt", "det_pure_6y_nu"):
            name_lines.setdefault(tok.string, []).append(tok.start[0])

    pf_1 = (
        992 in name_lines["b1_g"]
        and name_lines["b_mssm"] == [1141, 1164, 1174]
        and 1144 in name_lines["run_gbs8_rge"]
        and 1145 in name_lines["run_gbs8_rge"]
        and 1155 in name_lines["det_single_pt"]
        and 1156 in name_lines["det_pure_6y_nu"]
        and all(ln not in range(1152, 1157) for ln in name_lines["b_mssm"] + name_lines["run_gbs8_rge"])
    )
    assert pf_1, f"PF_CC_1 failed: {name_lines}"

    # ==========================================================================
    # PF_CC_2: 32x32 Cl(10) matrix-trace verification of all 6 anomalies
    # ==========================================================================
    max_anom_err, grav_15, chi3_15 = build_cl10_and_verify_anomalies()
    pf_2 = (max_anom_err < p10(-45)) and (abs(grav_15 - 5) < p10(-44)) and (abs(chi3_15 - 125) < p10(-42))
    assert pf_2

    # ==========================================================================
    # PF_CC_3: Disjoint Mellin s_* + Finite-Difference Hessian STr M_{Z'_chi}^2 == 0
    # ==========================================================================
    s_star_cc = solve_s_star_mellin_coord_secant()
    s_star_prod = mp.mpf(out_doc["E2_all_6_anomalies_and_explicit_dflat_str_zchi"]["four_modulus_newton_t_s_re_im_45d"][1])
    assert abs(s_star_cc - s_star_prod) < p10(-30), f"s_* mismatch: {abs(s_star_cc - s_star_prod)}"

    g_chi = mp.sqrt(4 * mp.pi / s_star_cc)
    v_chi = mp.exp(mp.mpf(24))
    rt2 = mp.sqrt(2)

    def d_chi_fn(rp: mp.mpf, rm: mp.mpf, sp: mp.mpf, sm: mp.mpf) -> mp.mpf:
        phi_p_sq = (v_chi + rp / rt2) ** 2 + (sp / rt2) ** 2
        phi_m_sq = (v_chi + rm / rt2) ** 2 + (sm / rt2) ** 2
        return g_chi * (10 * phi_p_sq - 10 * phi_m_sq)

    def vd_fn(vec4: list[mp.mpf]) -> mp.mpf:
        dv = d_chi_fn(vec4[0], vec4[1], vec4[2], vec4[3])
        return mp_rat(1, 2) * (dv ** 2)

    # Central finite-difference 4x4 scalar Hessian of V_D & gradient of D_chi (for M_V^2 and M_f):
    h_fd = p10(-14) * v_chi
    z4 = [mp.mpf(0)] * 4
    v0_d = vd_fn(z4)
    hess_sc = mp.zeros(4, 4)
    for a in range(4):
        for b in range(a, 4):
            if a == b:
                 pa = list(z4); pa[a] = h_fd
                 ma = list(z4); ma[a] = -h_fd
                 hess_sc[a, a] = (vd_fn(pa) - 2 * v0_d + vd_fn(ma)) / (h_fd ** 2)
            else:
                pp = list(z4); pp[a] = h_fd; pp[b] = h_fd
                pm = list(z4); pp_m = list(z4); pm[a] = h_fd; pm[b] = -h_fd
                mp_v = list(z4); mp_v[a] = -h_fd; mp_v[b] = h_fd
                mm = list(z4); mm[a] = -h_fd; mm[b] = -h_fd
                hess_sc[a, b] = hess_sc[b, a] = (vd_fn(pp) - vd_fn(pm) - vd_fn(mp_v) + vd_fn(mm)) / (4 * (h_fd ** 2))

    # In N=1 SUSY, dD/drho_i at sigma=0 gives the gaugino-chiralino Dirac coupling and sum (dD/drho_i)^2 = M_V^2!
    dd_drp = (d_chi_fn(h_fd, mp.mpf(0), mp.mpf(0), mp.mpf(0)) - d_chi_fn(-h_fd, mp.mpf(0), mp.mpf(0), mp.mpf(0))) / (2 * h_fd)
    dd_drm = (d_chi_fn(mp.mpf(0), h_fd, mp.mpf(0), mp.mpf(0)) - d_chi_fn(mp.mpf(0), -h_fd, mp.mpf(0), mp.mpf(0))) / (2 * h_fd)
    mv_sq_fd = dd_drp ** 2 + dd_drm ** 2
    mf_fd = mp.matrix([
        [mp.mpc(0), mp.mpc(0), dd_drp],
        [mp.mpc(0), mp.mpc(0), dd_drm],
        [dd_drp, dd_drm, mp.mpc(0)],
    ])
    r4_e = expm_so4(17)
    u3_e = expm_u3(29)
    u3_ec = mp.matrix([[mp.conj(u3_e[r, c]) for c in range(3)] for r in range(3)])
    ev_sc_fd, _ = mp.eigh(r4_e * hess_sc * r4_e.T)
    mf_s = u3_ec * mf_fd * u3_e.H
    ev_fm_fd, _ = mp.eigh(mf_s.H * mf_s)
    str_fd = 3 * mv_sq_fd + sum(mp.re(e) for e in ev_sc_fd) - 2 * sum(mp.re(e) for e in ev_fm_fd)
    assert abs(str_fd) / mv_sq_fd < p10(-22)

    dm_s = mp_rat(7, 3)
    ev_sc_soft, _ = mp.eigh(hess_sc + dm_s * mp.eye(4))
    str_soft_fd = 3 * mv_sq_fd + sum(mp.re(e) for e in ev_sc_soft) - 2 * sum(mp.re(e) for e in ev_fm_fd)
    pf_3 = (abs(str_fd) / mv_sq_fd < p10(-22)) and (abs(str_soft_fd - 4 * dm_s) < p10(-18) * mv_sq_fd)
    assert pf_3

    # ==========================================================================
    # PF_CC_4: Vandermonde 4x4 Extraction of (lambda_1..lambda_4) & mp.expm Scrambling
    # ==========================================================================
    g2_sq = 4 * mp.pi / s_star_cc
    gy_sq = mp_rat(3, 5) * g2_sq
    lam_s = mp_rat(3, 5)
    sig1 = mp.matrix([[0, 1], [1, 0]])
    sig2 = mp.matrix([[0, -I_MP], [I_MP, 0]])
    sig3 = mp.matrix([[1, 0], [0, -1]])

    def eval_vdf(hu_m: mp.matrix, hd_m: mp.matrix, ls_v: mp.mpf = lam_s) -> mp.mpf:
        da2 = sum(((mp.re((hu_m.H * sm * hu_m)[0, 0] + (hd_m.H * sm * hd_m)[0, 0]) / 2) ** 2 for sm in (sig1, sig2, sig3)), mp.mpf(0))
        dy = mp.re((hu_m.H * hu_m)[0, 0] - (hd_m.H * hd_m)[0, 0]) / 2
        hud = hu_m[0, 0] * hd_m[1, 0] - hu_m[1, 0] * hd_m[0, 0]
        return mp_rat(1, 2) * g2_sq * da2 + mp_rat(1, 2) * gy_sq * (dy ** 2) + (ls_v ** 2) * (abs(hud) ** 2)

    configs = [
        (mp.matrix([[mp.mpf(1)], [mp.mpf(0)]]), mp.matrix([[mp.mpf(0)], [mp.mpf(0)]])),
        (mp.matrix([[mp.mpf(0)], [mp.mpf(0)]]), mp.matrix([[mp.mpf(1)], [mp.mpf(0)]])),
        (mp.matrix([[mp.mpf(1)], [mp.mpf(0)]]), mp.matrix([[mp.mpf(1)], [mp.mpf(0)]])),
        (mp.matrix([[mp.mpf(1)], [mp.mpf(0)]]), mp.matrix([[mp.mpf(0)], [mp.mpf(1)]])),
    ]
    A_v = mp.zeros(4, 4)
    b_v = mp.zeros(4, 1)
    for row_i, (hu_c, hd_c) in enumerate(configs):
        phi1 = [mp.conj(hd_c[1, 0]), -mp.conj(hd_c[0, 0])]
        phi2 = [hu_c[0, 0], hu_c[1, 0]]
        n1 = abs(phi1[0]) ** 2 + abs(phi1[1]) ** 2
        n2 = abs(phi2[0]) ** 2 + abs(phi2[1]) ** 2
        p12 = mp.conj(phi1[0]) * phi2[0] + mp.conj(phi1[1]) * phi2[1]
        A_v[row_i, 0] = mp_rat(1, 2) * (n1 ** 2)
        A_v[row_i, 1] = mp_rat(1, 2) * (n2 ** 2)
        A_v[row_i, 2] = n1 * n2
        A_v[row_i, 3] = abs(p12) ** 2
        b_v[row_i, 0] = eval_vdf(hu_c, hd_c)

    lam_sol = mp.lu_solve(A_v, b_v)
    prod_lams = [mp.mpf(s) for s in out_doc["E3_b4_2hdm_quartics_and_b6_verification"]["B4_2hdm_quartics_recomputed"]["derived_2hdm_quartics_at_s_star_35d"]]
    lam_cc_err = max(abs(lam_sol[i, 0] - prod_lams[i]) for i in range(4))
    assert lam_cc_err < p10(-30)

    u2_e = expm_su2(13)
    u2_bad = expm_su2(41)
    th_e = mp_rat(5, 9)
    hu_t = 2 * mp.matrix([[mp_rat(4, 9) + I_MP * mp_rat(3, 11)], [mp_rat(7, 13) - I_MP * mp_rat(2, 7)]])
    hd_t = 2 * mp.matrix([[mp_rat(5, 11) - I_MP * mp_rat(1, 6)], [-mp_rat(3, 8) + I_MP * mp_rat(4, 15)]])
    v_ref = eval_vdf(hu_t, hd_t)
    v_ok = eval_vdf(mp.exp(I_MP * th_e / 2) * (u2_e * hu_t), mp.exp(-I_MP * th_e / 2) * (u2_e * hd_t))
    v_bad = eval_vdf(u2_e * hu_t, u2_bad * hd_t)
    pf_4 = (abs(v_ok - v_ref) < p10(-46)) and (abs(v_bad - v_ref) > mp_rat(1, 20))
    assert pf_4

    # ==========================================================================
    # PF_CC_5: git cat-file / diff-tree B6 check & trig-Wronskian b_c^*(tau_8^+)
    # ==========================================================================
    manifests = [
        "relays/a2_peer_link23/SCRIPT_SHA256.txt",
        "relays/a2_peer_link23/OUTPUT_SHA256.txt",
        "relays/a2_peer_link23_referee/SCRIPT_SHA256.txt",
        "relays/a2_peer_link23_referee/OUTPUT_SHA256.txt",
        "relays/a2_peer_link23_referee/SCRIPT_SHA256_v2.txt",
        "relays/a2_peer_link23_referee/OUTPUT_SHA256_v2.txt",
    ]
    for mf in manifests:
        exp_h, rel_t = git_cat_blob(repo, f"{AGY_002_COMMIT}:{mf}").decode("utf-8").strip().split()
        full_t = rel_t if "/" in rel_t else f"{Path(mf).parent.as_posix()}/{rel_t}"
        assert hashlib.sha256(git_cat_blob(repo, f"{AGY_002_COMMIT}:{full_t}")).hexdigest() == exp_h

    revs = subprocess.check_output(
        ["git", "-C", str(repo), "rev-list", f"{AGY_002_BASE}..{AGY_002_COMMIT}"],
        text=True,
    ).splitlines()
    status_pairs: list[tuple[str, str]] = []
    for rv in revs:
        dt = subprocess.check_output(
            ["git", "-C", str(repo), "diff-tree", "--no-commit-id", "--name-status", "-r", rv],
            text=True,
        ).splitlines()
        for ln in dt:
            st, fp = ln.strip().split("\t", 1)
            if fp.startswith(("relays/a2_peer_link23/", "relays/a2_peer_link23_referee/")):
                status_pairs.append((st, fp))
    assert len(status_pairs) == 12 and all(st == "A" for st, _ in status_pairs)

    l2_wronsk = solve_l2_trig_wronskian((mp.mpf(1) + I_MP * mp.mpf(8)) / 5, work_dps=50)
    bc_wronsk = mp.pi - l2_wronsk
    bc_prod = mp.mpf(out_doc["E3_b4_2hdm_quartics_and_b6_verification"]["B6_peer_link23_and_ow19_f3_recomputed"]["ow19_f3_bc_star_taylor26_42d"])
    a2_doc = json.loads(git_cat_blob(repo, f"{AGY_002_COMMIT}:relays/a2_peer_link23/a2_peer_link23_results.json").decode("utf-8"))
    bc_71b = mp.mpf(a2_doc["L23_C_ow19_f1_f3_remediation"]["OW19_F3_exact_48dps_frobenius_bc_star"]["bc_star_exact_48dps"])
    b6_639 = json.loads(git_cat_blob(repo, f"{AGY_EXP_COMMIT}:relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4_out.json").decode("utf-8"))["B6_peer_link23_audit_and_parameter_ledger"]
    bc_639 = mp.mpf(b6_639["ow19_f3_bc_star_gbs10"])

    pf_5 = (
        abs(bc_wronsk - bc_prod) < p10(-31)
        and abs(bc_wronsk - bc_71b) < p10(-31)
        and abs(bc_wronsk - bc_639) < p10(-12)
    )
    assert pf_5

    pf_total = sum(int(x) for x in (pf_1, pf_2, pf_3, pf_4, pf_5))
    assert pf_total == 5
    elapsed = int(time.time() - t0)
    print(
        f"AGY-C38 disjoint countercheck PASSED in {elapsed}s: "
        f"Cl(10)_anom={mp.nstr(max_anom_err, 8)}, |s*_mel-s*_newt|={mp.nstr(abs(s_star_cc - s_star_prod), 8)}, "
        f"|bc_wronsk-bc_taylor|={mp.nstr(abs(bc_wronsk - bc_prod), 8)}, planted_faults={pf_total}/5."
    )


if __name__ == "__main__":
    main()
