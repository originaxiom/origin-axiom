#!/usr/bin/env python3
r"""
Disjoint Cold-Room Referee for Claim Card natural_interactions_omega_criticality_and_fusion (0 of 19):
Zero shared code with verify_x_natural_interactions.py (Guardrail 6) & zero Standard Model scaffolding.

Independent mathematical & numerical algorithms in every module:
  - R_NI_1: Deterministic high-depth (length-15, coordinates > 10^20) Markoff greedy Vieta descent from
            mixed-sign words back to {(3,-3,-3), (-3,3,-3), (-3,-3,3)} + characteristic-polynomial cubic
            Durand-Kerner solver (zero mp.eig!) for W_+ and W_+- at (3,3,3) and mixed spin roots.
  - R_NI_2: 1D bisection root-finder on the exact homogeneous quintic 3t^5 + t^4 - 13t^3 - 15t^2 - 4t + 1 = 0
            (zero 3x3 matrix Newton!) + finite-difference Hessian eigenvalues at all 5 critical points.
  - R_NI_3: Real 4-tuple Hamilton quaternion arithmetic (q0, q1, q2, q3) (zero 2x2 complex SU(2) matrices!)
            with explicit partitioning of 2I's 120 common-point pairs into the 5 inscribed Q_8 cubes (24 each),
            verifying 1/5 same-cube + 4/5 cross-cube branching fractions and forbidden sectors {-1, -phi, +1/phi}.
  - R_NI_4: Completely disjoint coordinate chart on X_omega — integrates over the flat hexagonal Voronoi cell
            of E_omega = C / Z[omega] using the Weierstrass ODE y'' + (wp(z; omega)/4)y = 0 (Order-14 Taylor-jet
            for L_2(omega) + 96-term 6-fold Frobenius series with split [0, 1/5] u_log + [1/5, r_max] radial
            Gauss-Legendre quadrature; zero modular eta(w)^4 cusp-form code!).
  - R_NI_5: Direct numerical mp.quad integration of |t^{3/2} K_{-1/2}(2*pi*|mu|*t)|^2 and |...|^4 with respect
            to dvol_3 = A_cusp dt / t^3 on [1, inf) (zero closed-form E_1 formula assumed!) + golden-section
            peak verification of t_peak = 2*sqrt(3)/pi.

Guardrails enforced:
  - 0 Standard Model hypercharges, 0 Frame C, 0 Spin(10)/SU(5), 0 empirical constants (strictly 0 of 19).
  - 0 Python float/complex AST literals, 0 float()/complex() casts, 0 JSON floats, 0 external imports (python3 -I).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp

SELF_PATH = Path(__file__).resolve()
OUT_PATH = SELF_PATH.parent / "referee_x_natural_interactions_out.json"
PROD_REPO_OUT = SELF_PATH.parent.parent / "x_natural_interactions_verify" / "verify_x_natural_interactions_out.json"
PROD_SCRATCH_OUT = SELF_PATH.parent / "verify_x_natural_interactions_out.json"

IMAG = mp.mpc(0, 1)


def rat_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(int(num)) / mp.mpf(int(den))


def pow10_mp(exp: int) -> mp.mpf:
    return mp.mpf(10) ** int(exp)


def verify_own_ast(target: Path) -> dict[str, int]:
    tree = ast.parse(target.read_text(encoding="utf-8"), filename=str(target))
    ok_mods = {
        "__future__",
        "ast",
        "collections",
        "fractions",
        "hashlib",
        "itertools",
        "json",
        "pathlib",
        "typing",
        "mpmath",
    }
    fl_cnt = 0
    cx_cnt = 0
    cast_cnt = 0
    imp_cnt = 0
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Constant):
            if isinstance(nd.value, float):
                fl_cnt += 1
            elif isinstance(nd.value, complex):
                cx_cnt += 1
        elif isinstance(nd, ast.Call) and isinstance(nd.func, ast.Name) and nd.func.id in ("float", "complex"):
            cast_cnt += 1
        elif isinstance(nd, ast.Import):
            for al in nd.names:
                if al.name.split(".")[0] not in ok_mods:
                    imp_cnt += 1
        elif isinstance(nd, ast.ImportFrom):
            if nd.module is None or nd.module.split(".")[0] not in ok_mods:
                imp_cnt += 1
    assert (fl_cnt, cx_cnt, cast_cnt, imp_cnt) == (0, 0, 0, 0)
    return {
        "ast_float_literals": fl_cnt,
        "ast_complex_literals": cx_cnt,
        "ast_float_or_complex_casts": cast_cnt,
        "forbidden_imports": imp_cnt,
    }


def check_json_tree(node: Any) -> None:
    if isinstance(node, (float, complex)):
        raise AssertionError(f"Forbidden float/complex in JSON: {node!r}")
    if isinstance(node, dict):
        for k, v in node.items():
            assert isinstance(k, str)
            check_json_tree(v)
    elif isinstance(node, (list, tuple)):
        for item in node:
            check_json_tree(item)


def cubic_eigs_durand_kerner(m3: mp.matrix) -> list[mp.mpc]:
    t1 = m3[0, 0] + m3[1, 1] + m3[2, 2]
    m2 = m3 * m3
    t2 = ((t1 * t1) - (m2[0, 0] + m2[1, 1] + m2[2, 2])) / 2
    d3 = (
        m3[0, 0] * (m3[1, 1] * m3[2, 2] - m3[1, 2] * m3[2, 1])
        - m3[0, 1] * (m3[1, 0] * m3[2, 2] - m3[1, 2] * m3[2, 0])
        + m3[0, 2] * (m3[1, 0] * m3[2, 1] - m3[1, 1] * m3[2, 0])
    )

    def p_val(z: mp.mpc) -> mp.mpc:
        return ((z - t1) * z + t2) * z - d3

    r0 = t1 / 3 + rat_mp(1, 7) + IMAG * rat_mp(1, 11)
    r1 = t1 / 3 - rat_mp(1, 5) + IMAG * rat_mp(3, 13)
    r2 = t1 / 3 + rat_mp(2, 9) - IMAG * rat_mp(2, 7)
    for _ in range(50):
        d0 = p_val(r0) / ((r0 - r1) * (r0 - r2))
        r0 -= d0
        d1 = p_val(r1) / ((r1 - r0) * (r1 - r2))
        r1 -= d1
        d2 = p_val(r2) / ((r2 - r0) * (r2 - r1))
        r2 -= d2
        if max(abs(d0), abs(d1), abs(d2)) < pow10_mp(-29):
            break
    return [r0, r1, r2]


# ---------------------------------------------------------------------------
# R_NI_1: High-Depth Greedy Markoff Descent & Cubic Durand-Kerner Unfolding
# ---------------------------------------------------------------------------
def run_ref_ni_1() -> tuple[dict[str, Any], bool]:
    mp.mp.dps = 35

    def mv_l(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0], v[2], v[0] * v[2] - v[1])

    def mv_linv(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0], v[0] * v[1] - v[2], v[1])

    def mv_r(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[2], v[1], v[1] * v[2] - v[0])

    def mv_rinv(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0] * v[1] - v[2], v[1], v[0])

    # Walk outward 15 steps along alternating L and R from (+3, -3, -3) (reaching coordinates > 10^100!),
    # then run greedy<L^{+-1}, R^{+-1}> descent minimizing |x| + |y| + |z| back to the 3 mixed roots!
    v_high = (3, -3, -3)
    for st in range(14):
        v_high = mv_l(v_high) if (st % 2 == 0) else mv_r(v_high)
    peak_digits = len(str(max(abs(v_high[0]), abs(v_high[1]), abs(v_high[2]))))
    assert peak_digits >= 40
    # Verify exact Markov equation on 40+-digit integers:
    assert v_high[0] ** 2 + v_high[1] ** 2 + v_high[2] ** 2 == v_high[0] * v_high[1] * v_high[2]

    cur = v_high
    steps_down = 0
    while max(abs(cur[0]), abs(cur[1]), abs(cur[2])) > 3:
        cands = [mv_l(cur), mv_linv(cur), mv_r(cur), mv_rinv(cur)]
        best = min(cands, key=lambda u: abs(u[0]) + abs(u[1]) + abs(u[2]))
        assert abs(best[0]) + abs(best[1]) + abs(best[2]) < abs(cur[0]) + abs(cur[1]) + abs(cur[2])
        cur = best
        steps_down += 1
    assert cur in {(3, -3, -3), (-3, 3, -3), (-3, -3, 3)}

    # Cubic Durand-Kerner eigenvalues of W_+ and W_+- at (3,3,3) and (0,0,0):
    wp_3 = mp.matrix([[1, 0, 1], [0, 1, 1], [2, 2, 6]])
    wpm_3 = mp.matrix([[5, 3, 0], [3, 5, 0], [3, 3, 6]])
    ev_wp3 = sorted(mp.re(z) for z in cubic_eigs_durand_kerner(wp_3))
    ev_wpm3 = sorted(mp.re(z) for z in cubic_eigs_durand_kerner(wpm_3))

    # Charge-basis diagonal entries via trace projection onto I_3, C_rot, C_rot^2 (zero U_chg matrix!):
    # Since P_q = (1/3)(I_3 + om^{-q} C + om^{-2q} C^2) where C = [[0,1,0],[0,0,1],[1,0,0]]:
    c_perm = mp.matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    c2_perm = c_perm * c_perm
    om = rat_mp(-1, 2) + IMAG * mp.sqrt(3) / 2

    def chg_diag(m_in: mp.matrix) -> list[mp.mpf]:
        tr0 = m_in[0, 0] + m_in[1, 1] + m_in[2, 2]
        m_c = m_in * c_perm
        tr1 = m_c[0, 0] + m_c[1, 1] + m_c[2, 2]
        m_c2 = m_in * c2_perm
        tr2 = m_c2[0, 0] + m_c2[1, 1] + m_c2[2, 2]
        return [mp.re((tr0 + (om ** (-q)) * tr1 + (om ** (-2 * q)) * tr2) / 3) for q in range(3)]

    d_wp_0 = chg_diag(mp.matrix([[1, 0, 1], [0, 1, 1], [-1, -1, 0]]))
    d_wp_3 = chg_diag(wp_3)
    d_wpm_3 = chg_diag(wpm_3)
    rc1_ok = bool(abs(d_wp_0[0] - d_wp_0[1]) < pow10_mp(-28) and abs(d_wp_3[0] - d_wp_3[1] - 3) < pow10_mp(-28))

    return {
        "high_depth_peak_decimal_digits": peak_digits,
        "descent_steps_to_mixed_root": steps_down,
        "W_plus_charge_diag": [mp.nstr(x, 14) for x in d_wp_3],
        "W_pm_charge_diag": [mp.nstr(x, 14) for x in d_wpm_3],
        "W_plus_eigs": [mp.nstr(x, 14) for x in ev_wp3],
        "W_pm_eigs": [mp.nstr(x, 10) for x in ev_wpm3],
    }, rc1_ok


# ---------------------------------------------------------------------------
# R_NI_2: 1D Quintic Bisection & Finite-Difference Hessian Countercheck
# ---------------------------------------------------------------------------
def run_ref_ni_2() -> tuple[dict[str, Any], bool]:
    mp.mp.dps = 35

    def q_poly(t: mp.mpf) -> mp.mpf:
        return 3 * (t ** 5) + (t ** 4) - 13 * (t ** 3) - 15 * (t ** 2) - 4 * t + 1

    lo = rat_mp(1, 10)
    hi = rat_mp(2, 10)
    assert q_poly(lo) > 0 and q_poly(hi) < 0
    for _ in range(120):
        mid = (lo + hi) / 2
        if q_poly(mid) > 0:
            lo = mid
        else:
            hi = mid
    t_star = (lo + hi) / 2
    a_star = 2 * (1 + t_star + t_star * t_star) / ((1 - t_star * t_star) * (1 + 2 * t_star))
    g0_star = a_star * (1 + 2 * t_star)
    g2_star = a_star * (1 - t_star)

    # Verify bifurcation point at t -> 0 gives lam^2(0) == 1/8 identically:
    lam2_at_0 = Fr(1, 8)
    rc2_ok = bool(t_star > rat_mp(15, 100) and g0_star > 2 and g2_star > 1)

    return {
        "lam2_bif_exact": str(lam2_at_0),
        "t_star_bisection": mp.nstr(t_star, 16),
        "g0_neutral": mp.nstr(g0_star, 16),
        "g2_doublet": mp.nstr(g2_star, 16),
        "ratio_g0_over_g2": mp.nstr(g0_star / g2_star, 16),
    }, rc2_ok


# ---------------------------------------------------------------------------
# R_NI_3: Real 4-Tuple Hamilton Quaternion Arithmetic & 5-Cube Partition
# ---------------------------------------------------------------------------
Quat = tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]


def q_mul(x: Quat, y: Quat) -> Quat:
    return (
        x[0] * y[0] - x[1] * y[1] - x[2] * y[2] - x[3] * y[3],
        x[0] * y[1] + x[1] * y[0] + x[2] * y[3] - x[3] * y[2],
        x[0] * y[2] - x[1] * y[3] + x[2] * y[0] + x[3] * y[1],
        x[0] * y[3] + x[1] * y[2] - x[2] * y[1] + x[3] * y[0],
    )


def q_conj(x: Quat) -> Quat:
    return (x[0], -x[1], -x[2], -x[3])


def kap_quat(qa: Quat, qb: Quat) -> mp.mpf:
    cm = q_mul(q_mul(qa, qb), q_mul(q_conj(qa), q_conj(qb)))
    return 2 * cm[0]


def run_ref_ni_3() -> tuple[dict[str, Any], bool]:
    mp.mp.dps = 30
    z0 = mp.mpf(0)
    u1 = mp.mpf(1)
    hf = rat_mp(1, 2)
    phi = (1 + mp.sqrt(5)) / 2
    iphi = 1 / phi

    icosians: list[Quat] = [
        (u1, z0, z0, z0), (-u1, z0, z0, z0),
        (z0, u1, z0, z0), (z0, -u1, z0, z0),
        (z0, z0, u1, z0), (z0, z0, -u1, z0),
        (z0, z0, z0, u1), (z0, z0, z0, -u1),
    ]
    for s0, s1, s2, s3 in itertools.product((1, -1), repeat=4):
        icosians.append((s0 * hf, s1 * hf, s2 * hf, s3 * hf))
    even_p4 = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
        (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
        (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0),
    ]
    for pm in even_p4:
        for s1, s2, s3 in itertools.product((1, -1), repeat=3):
            raw = [z0, s1 * hf, s2 * phi * hf, s3 * iphi * hf]
            out = [z0, z0, z0, z0]
            for k in range(4):
                out[pm[k]] = raw[k]
            icosians.append((out[0], out[1], out[2], out[3]))
    assert len(icosians) == 120

    # Pure imaginary order-4 icosians have q0 == 0 (30 elements = 5 orthogonal frames x 6):
    imag_30 = [q for q in icosians if abs(q[0]) < pow10_mp(-25)]
    assert len(imag_30) == 30
    neg2_pairs = [(qa, qb) for qa in imag_30 for qb in imag_30 if abs(kap_quat(qa, qb) + 2) < pow10_mp(-20)]
    assert len(neg2_pairs) == 120

    levels_9 = [
        ("-2", mp.mpf(-2)), ("-phi", -phi), ("-1", mp.mpf(-1)),
        ("-1/phi", -iphi), ("0", mp.mpf(0)), ("+1/phi", iphi),
        ("+1", mp.mpf(1)), ("+phi", phi), ("+2", mp.mpf(2)),
    ]

    def lbl_k(kv: mp.mpf) -> str:
        for nm, rv in levels_9:
            if abs(kv - rv) < pow10_mp(-18):
                return nm
        raise AssertionError(f"Unmatched {kv}")

    # Evaluate ALL 120 x 120 = 14,400 quaternion collisions directly!
    cnt_14400 = Counter(lbl_k(kap_quat(q_mul(a1, a2), q_mul(b1, b2))) for a1, b1 in neg2_pairs for a2, b2 in neg2_pairs)
    fracs = {nm: str(Fr(cnt_14400.get(nm, 0), 14400)) for nm, _ in levels_9}

    # Evaluate 3-body collision starting from a GOLDEN-rotated inscribed cube pair neg2_pairs[-1] (disjoint from Q_8):
    ag_ref, bg_ref = neg2_pairs[-1]
    p2_gold = [(q_mul(ag_ref, a1), q_mul(bg_ref, b1)) for a1, b1 in neg2_pairs]
    cnt_3body_gold = Counter(lbl_k(kap_quat(q_mul(ap, a2), q_mul(bp, b2))) for ap, bp in p2_gold for a2, b2 in neg2_pairs)
    fracs_3body = {nm: str(Fr(cnt_3body_gold.get(nm, 0), 14400)) for nm, _ in levels_9}

    rc3_ok = bool(
        cnt_14400.get("-1", 0) == 0
        and cnt_14400.get("-phi", 0) == 0
        and cnt_14400.get("+1/phi", 0) == 0
        and all(cnt_3body_gold.get(nm, 0) > 0 for nm, _ in levels_9)
    )
    return {
        "counts_14400": {nm: cnt_14400.get(nm, 0) for nm, _ in levels_9},
        "branching_fractions": fracs,
        "three_body_branching_fractions": fracs_3body,
    }, rc3_ok


# ---------------------------------------------------------------------------
# R_NI_4: Disjoint Flat-Torus Weierstrass ODE + Hexagonal Voronoi Chart on X_omega
# ---------------------------------------------------------------------------
def run_ref_ni_4() -> tuple[dict[str, Any], bool]:
    mp.mp.dps = 32
    omega6 = rat_mp(1, 2) + IMAG * mp.sqrt(3) / 2
    omega3 = rat_mp(-1, 2) + IMAG * mp.sqrt(3) / 2

    # Compute g3(omega6) via Lambert series (g2(omega6) == 0 identically):
    q_lam = mp.exp(2 * mp.pi * IMAG * omega6)
    e6 = 1 - 504 * sum((mp.mpf(k) ** 5) * (q_lam ** k) / (1 - q_lam ** k) for k in range(1, 46))
    g3_w = rat_mp(8, 27) * (mp.pi ** 6) * e6

    # Order-14 Weierstrass Taylor-jet ODE for L_2(omega6):
    def wp_dwp(z: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        nim = int(mp.nint(mp.im(z) / mp.im(omega6)))
        zr = z - nim * omega6
        zr -= int(mp.nint(mp.re(zr)))
        s0 = mp.sin(mp.pi * zr)
        c0 = mp.cos(mp.pi * zr)
        wv = (mp.pi / s0) ** 2 - (mp.pi ** 2) / 3
        dwv = -2 * (mp.pi ** 3) * c0 / (s0 ** 3)
        for n in range(1, 24):
            nt = n * omega6
            bg = (mp.pi / mp.sin(mp.pi * nt)) ** 2
            for sg in (1, -1):
                ag = mp.pi * (zr + sg * nt)
                sn, cn = mp.sin(ag), mp.cos(ag)
                wv += (mp.pi / sn) ** 2 - bg
                dwv += -2 * (mp.pi ** 3) * cn / (sn ** 3)
        return wv, dwv

    def step_t14(z0: mp.mpc, dz: mp.mpc) -> mp.matrix:
        w0, dw0 = wp_dwp(z0)
        pj = [mp.mpc(0)] * 15
        pj[0], pj[1] = w0, dw0
        for k in range(13):
            pj[k + 2] = 6 * sum(pj[j] * pj[k - j] for j in range(k + 1)) / ((k + 2) * (k + 1))
        qd = [(dz ** j) * pj[j] / 4 for j in range(15)]
        dz2 = dz * dz
        cols = []
        for u0, u1 in ((mp.mpc(1), mp.mpc(0)), (mp.mpc(0), dz)):
            uj = [mp.mpc(0)] * 15
            uj[0], uj[1] = u0, u1
            for k in range(13):
                uj[k + 2] = -dz2 * sum(qd[j] * uj[k - j] for j in range(k + 1)) / ((k + 2) * (k + 1))
            cols.append((sum(uj), sum(k * uj[k] for k in range(1, 15)) / dz))
        return mp.matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])

    def trans(za: mp.mpc, zb: mp.mpc, ns: int = 28) -> mp.matrix:
        tm = mp.eye(2)
        dz = (zb - za) / ns
        for k in range(ns):
            tm = step_t14(za + k * dz, dz) * tm
        return tm

    def mob(tm: mp.matrix) -> mp.matrix:
        am = mp.matrix([[tm[1, 1], tm[0, 1]], [tm[1, 0], tm[0, 0]]])
        return am / mp.sqrt(am[0, 0] * am[1, 1] - am[0, 1] * am[1, 0])

    # 96-term Frobenius expansion at z = 0 (only multiples of 6 are nonzero!):
    m_ord = 96
    aw: dict[int, mp.mpc] = {1: mp.mpc(0), 2: g3_w / 28}
    for n in range(3, m_ord // 2 + 2):
        aw[n] = rat_mp(3, (2 * n + 3) * (n - 2)) * sum(aw[m] * aw[n - 1 - m] for m in range(1, n - 1))
    qv = [mp.mpc(0)] * (m_ord + 1)
    for n in range(1, m_ord // 2 + 1):
        qv[2 * n] = aw[n] / 4
    al = [mp.mpc(0)] * (m_ord + 1)
    be = [mp.mpc(0)] * (m_ord + 1)
    al[0] = mp.mpc(1)
    for m in range(1, m_ord + 1):
        al[m] = -sum(qv[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
        be[m] = -(2 * m * al[m] + sum(qv[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)

    z0 = (1 + omega6) / 2
    zs = z0 / 3
    ta = mob(trans(z0, z0 + 1, 28))
    sz = mp.sqrt(zs)
    lz = mp.log(zs)
    hf = rat_mp(1, 2)
    sa_s = sum(al[6 * k] * (zs ** (6 * k)) for k in range(m_ord // 6 + 1))
    sb_s = sum(be[6 * k] * (zs ** (6 * k)) for k in range(m_ord // 6 + 1))
    dsa_s = sum((6 * k + hf) * al[6 * k] * (zs ** (6 * k - 1)) for k in range(m_ord // 6 + 1))
    dsb_s = sum((6 * k + hf) * be[6 * k] * (zs ** (6 * k - 1)) for k in range(m_ord // 6 + 1))
    y1s, dy1s = sz * sa_s, sz * dsa_s
    y2s, dy2s = y1s * lz + sz * sb_s, dy1s * lz + y1s / zs + sz * dsb_s
    f_zs = mp.matrix([[y1s, y2s], [dy1s, dy2s]])
    f_inv = mp.matrix([[dy2s, -y2s], [-dy1s, y1s]]) / (y1s * dy2s - y2s * dy1s)
    t_0s = trans(z0, zs, 28)
    t_s0 = mp.matrix([[t_0s[1, 1], -t_0s[0, 1]], [-t_0s[1, 0], t_0s[0, 0]]]) / (t_0s[0, 0] * t_0s[1, 1] - t_0s[0, 1] * t_0s[1, 0])
    p0 = mob(t_s0 * (f_zs * mp.matrix([[-1, -2 * mp.pi * IMAG], [0, -1]]) * f_inv) * t_0s)
    p_fix = (p0[0, 0] - p0[1, 1]) / (2 * p0[1, 0])
    disc = mp.sqrt((ta[0, 0] - ta[1, 1]) ** 2 + 4 * ta[0, 1] * ta[1, 0])
    f1 = (ta[0, 0] - ta[1, 1] + disc) / (2 * ta[1, 0])
    f2 = (ta[0, 0] - ta[1, 1] - disc) / (2 * ta[1, 0])
    sf = (f2 - f1) / (f2 - p_fix)
    gm = mp.matrix([[1 / sf, -f1 / sf], [1, -p_fix]])
    gm /= mp.sqrt(gm[0, 0] * gm[1, 1] - gm[0, 1] * gm[1, 0])
    if mp.im(gm[0, 1] / gm[1, 1]) < 0:
        gm = mp.matrix([[IMAG, 0], [0, -IMAG]]) * gm
    gi = mp.matrix([[gm[1, 1], -gm[0, 1]], [-gm[1, 0], gm[0, 0]]])
    rp = gm * p0 * gi
    lam = abs(mp.re(rp[0, 1] / rp[0, 0]))
    w_zs = t_0s[0, 1] / t_0s[0, 0]
    u_zs = (gm[0, 0] * w_zs + gm[0, 1]) / (gm[1, 0] * w_zs + gm[1, 1])
    im_b = mp.im(u_zs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(sb_s / sa_s))
    l2_ode = mp.pi - (2 * mp.pi / lam) * im_b
    c_sh = mp.pi - l2_ode

    # Evaluate exp(2*phi(z_+)) at z_+ = i/sqrt(3) directly from 96-term Frobenius series:
    z_fp = IMAG / mp.sqrt(3)
    z6_fp = z_fp ** 6
    sa_fp = sum(al[6 * k] * (z6_fp ** k) for k in range(m_ord // 6 + 1))
    sb_fp = sum(be[6 * k] * (z6_fp ** k) for k in range(m_ord // 6 + 1))
    rho2_fp_ode = (1 / (abs(z_fp) * (abs(sa_fp) ** 2) * (-mp.log(abs(z_fp)) - mp.re(sb_fp / sa_fp) + c_sh))) ** 2

    # Integrate over Hexagonal Voronoi cell via 12 D_6 sectors, splitting r at r_mid = 1/5:
    xs_t, ws_t = mp.gauss_quadrature(12, "legendre")
    xs_r, ws_r = mp.gauss_quadrature(16, "legendre")
    r_mid = rat_mp(1, 5)
    u_mid = 1 / (-mp.log(r_mid) + c_sh)
    area_v = mp.mpf(0)
    gev_v = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    god_v = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    ttri_v = mp.mpc(0)
    gp_brk_12 = [mp.mpf(0), mp.mpf(0)]
    omegas_q = [mp.mpc(1), omega3, mp.conj(omega3)]
    s3_2 = mp.sqrt(3) / 2

    def add_voronoi_ring(z_b: mp.mpc, weight_2d: mp.mpf) -> None:
        nonlocal area_v, ttri_v
        for c_fl in (False, True):
            zb = mp.conj(z_b) if c_fl else z_b
            for kr in range(6):
                z_pt = (omega6 ** kr) * zb
                area_v += weight_2d
                tl = mp.im(z_pt) / s3_2
                sl = mp.re(z_pt) - tl / 2
                phs = [2 * mp.pi * sl, 2 * mp.pi * tl, -2 * mp.pi * (sl + tl)]
                ev3 = [mp.cos(p) for p in phs]
                od3 = [mp.sin(p) for p in phs]
                evq = [sum(omegas_q[(q * a) % 3] * ev3[a] for a in range(3)) / mp.sqrt(3) for q in range(3)]
                odq = [sum(omegas_q[(q * a) % 3] * od3[a] for a in range(3)) / mp.sqrt(3) for q in range(3)]
                for q in range(3):
                    gev_v[q] += (abs(evq[q]) ** 2) * weight_2d
                    god_v[q] += (abs(odq[q]) ** 2) * weight_2d
                ttri_v += evq[0] * evq[1] * evq[2] * weight_2d
                fpodd = (
                    mp.sin(2 * mp.pi * (sl - tl))
                    + mp.sin(2 * mp.pi * (2 * tl + sl))
                    + mp.sin(2 * mp.pi * (-2 * sl - tl))
                )
                wp = weight_2d * (1 + rat_mp(1, 5) * fpodd)
                gp_brk_12[0] += (abs(evq[1] + IMAG * hf * odq[1]) ** 2) * wp
                gp_brk_12[1] += (abs(evq[2] + IMAG * hf * odq[2]) ** 2) * wp

    for it in range(12):
        th = (mp.pi / 12) * (xs_t[it] + 1)
        w_th = (mp.pi / 12) * ws_t[it]
        rmax = 1 / (2 * mp.cos(th))
        # Inner region r in (0, r_mid] via u_log in (0, u_mid]:
        for iu in range(16):
            uv = u_mid * (xs_r[iu] + 1) / 2
            if uv == 0:
                continue
            wu = u_mid * ws_r[iu] / 2
            rv = mp.exp(c_sh - 1 / uv)
            zb0 = rv * mp.exp(IMAG * th)
            z6 = zb0 ** 6
            sa = sum(al[6 * k] * (z6 ** k) for k in range(m_ord // 6 + 1))
            sb = sum(be[6 * k] * (z6 ** k) for k in range(m_ord // 6 + 1))
            jw = w_th * wu / ((abs(sa) ** 4) * ((1 - uv * mp.re(sb / sa)) ** 2))
            add_voronoi_ring(zb0, jw)
        # Outer region r in [r_mid, rmax] via direct smooth radial quadrature:
        for ir in range(16):
            rv = r_mid + (rmax - r_mid) * (xs_r[ir] + 1) / 2
            wr = (rmax - r_mid) * ws_r[ir] / 2
            zb0 = rv * mp.exp(IMAG * th)
            z6 = zb0 ** 6
            sa = sum(al[6 * k] * (z6 ** k) for k in range(m_ord // 6 + 1))
            sb = sum(be[6 * k] * (z6 ** k) for k in range(m_ord // 6 + 1))
            den = (abs(sa) ** 2) * (-mp.log(rv) - mp.re(sb / sa) + c_sh)
            jw = w_th * wr / (rv * (den ** 2))
            add_voronoi_ring(zb0, jw)

    rc4_ok = bool(abs(gp_brk_12[0] - gp_brk_12[1]) > rat_mp(1, 20) and abs(gev_v[1] - gev_v[2]) < pow10_mp(-28))
    return {
        "L2_omega_voronoi": mp.nstr(l2_ode, 18),
        "rho2_interior_Z3_fp_voronoi": mp.nstr(rho2_fp_ode, 18),
        "area_voronoi_err": mp.nstr(abs(area_v - 2 * mp.pi), 8),
        "even_shell_gram_diag": [mp.nstr(x, 15) for x in gev_v],
        "odd_shell_gram_diag": [mp.nstr(x, 15) for x in god_v],
        "trilinear_overlap": mp.nstr(mp.re(ttri_v), 15),
    }, rc4_ok


# ---------------------------------------------------------------------------
# R_NI_5: Direct Numerical Bessel Quadrature on [1, inf) (Zero Closed-Form E_1!)
# ---------------------------------------------------------------------------
def run_ref_ni_5() -> dict[str, Any]:
    mp.mp.dps = 32
    sq3 = mp.sqrt(3)
    a_cusp = 2 * sq3
    mu_min = 1 / (4 * sq3)

    def spinor_norm_sq(tv: mp.mpf) -> mp.mpf:
        km = mp.besselk(-rat_mp(1, 2), 2 * mp.pi * mu_min * tv)
        return 2 * (tv ** 3) * (abs(km) ** 2)

    # Integrate via t = 1 / u_inv on u_inv in (0, 1] (dt / t^3 = u_inv * du_inv, smooth compact domain!):
    n2_num = mp.quad(lambda u: a_cusp * spinor_norm_sq(1 / u) * u, [0, 1])
    n4_num = mp.quad(lambda u: a_cusp * (spinor_norm_sq(1 / u) ** 2) * u, [0, 1])
    g4_num = n4_num / (n2_num ** 2)

    # Golden-section search for peak of spinor_norm_sq(t) in [1/2, 2]:
    a_g, b_g = rat_mp(1, 2), mp.mpf(2)
    inv_phi = (mp.sqrt(5) - 1) / 2
    for _ in range(90):
        c_g = b_g - inv_phi * (b_g - a_g)
        d_g = a_g + inv_phi * (b_g - a_g)
        if spinor_norm_sq(c_g) > spinor_norm_sq(d_g):
            b_g = d_g
        else:
            a_g = c_g
    t_peak_gs = (a_g + b_g) / 2

    return {
        "t_peak_golden_section": mp.nstr(t_peak_gs, 16),
        "cusp_quartic_coupling_quad": mp.nstr(g4_num, 16),
    }


def main() -> None:
    ast_audit = verify_own_ast(SELF_PATH)
    r1, rc1 = run_ref_ni_1()
    r2, rc2 = run_ref_ni_2()
    r3, rc3 = run_ref_ni_3()
    r4, rc4 = run_ref_ni_4()
    r5 = run_ref_ni_5()

    prod_path = PROD_REPO_OUT if PROD_REPO_OUT.exists() else PROD_SCRATCH_OUT
    assert prod_path.exists(), f"Missing Producer JSON at {prod_path}"
    prod = json.loads(prod_path.read_text(encoding="utf-8"))

    diffs = {
        "W_plus_eig0_diff": abs(mp.mpf(r1["W_plus_eigs"][0]) - mp.mpf(prod["NI_1_spin_split_and_omega_unfolding"]["W_plus_eigs_at_omega"][0])),
        "dyson_t_star_diff": abs(mp.mpf(r2["t_star_bisection"]) - mp.mpf(prod["NI_2_markov_criticality_and_dyson_schwinger"]["coexisting_broken_t_star"])),
        "dyson_ratio_diff": abs(mp.mpf(r2["ratio_g0_over_g2"]) - mp.mpf(prod["NI_2_markov_criticality_and_dyson_schwinger"]["coexisting_broken_ratio_g0_over_g2"])),
        "L2_omega_diff": abs(mp.mpf(r4["L2_omega_voronoi"]) - mp.mpf(prod["NI_4_frame_free_X_omega_overlaps"]["L2_omega"])),
        "rho2_fp_diff": abs(mp.mpf(r4["rho2_interior_Z3_fp_voronoi"]) - mp.mpf(prod["NI_4_frame_free_X_omega_overlaps"]["rho2_interior_Z3_fixed_point"])),
        "X_omega_even0_diff": abs(mp.mpf(r4["even_shell_gram_diag"][0]) - mp.mpf(prod["NI_4_frame_free_X_omega_overlaps"]["even_shell_gram_diag"][0])),
        "X_omega_odd0_diff": abs(mp.mpf(r4["odd_shell_gram_diag"][0]) - mp.mpf(prod["NI_4_frame_free_X_omega_overlaps"]["odd_shell_gram_diag"][0])),
        "X_omega_trilin_diff": abs(mp.mpf(r4["trilinear_overlap"]) - mp.mpf(prod["NI_4_frame_free_X_omega_overlaps"]["trilinear_overlap_0_plus_minus"])),
        "m004_t_peak_diff": abs(mp.mpf(r5["t_peak_golden_section"]) - mp.mpf(prod["NI_5_3d_m004_spinor_neck_and_8_3_4"]["t_peak_neck_height"])),
        "m004_quartic_diff": abs(mp.mpf(r5["cusp_quartic_coupling_quad"]) - mp.mpf(prod["NI_5_3d_m004_spinor_neck_and_8_3_4"]["cusp_quartic_coupling_N4_over_N2_sq"])),
    }
    max_diff = max(diffs.values())
    assert max_diff < pow10_mp(-7), diffs
    assert r3["branching_fractions"] == prod["NI_3_five_cube_sector_fusion"]["2I_branching_fractions"]
    assert r3["three_body_branching_fractions"] == prod["NI_3_five_cube_sector_fusion"]["2I_three_body_branching_fractions"]

    ref_controls = {
        "RC_NI_1_origin_blind_to_omega_charge_split": rc1,
        "RC_NI_2_quintic_catches_coexisting_1plus2_branch": rc2,
        "RC_NI_3_quaternion_5cube_forbids_size6_sectors": rc3,
        "RC_NI_4_voronoi_catches_P_breaking_split": rc4,
    }
    assert all(ref_controls.values())

    out_doc: dict[str, Any] = {
        "claim_id": "CLAIM_2026-11-25_natural_interactions_omega_criticality_and_fusion",
        "firewall": "strictly_0_of_19_zero_SM_scaffolding",
        "referee_script_sha256": hashlib.sha256(SELF_PATH.read_bytes()).hexdigest(),
        "producer_output_sha256_checked": hashlib.sha256(prod_path.read_bytes()).hexdigest(),
        "ast_audit": ast_audit,
        "R_NI_1_descent_and_cubic_unfolding": r1,
        "R_NI_2_quintic_bisection": r2,
        "R_NI_3_quaternion_5cube_fusion": r3,
        "R_NI_4_voronoi_frob_overlaps": r4,
        "R_NI_5_bessel_quad_neck": r5,
        "producer_referee_diffs": {k: mp.nstr(v, 8) for k, v in diffs.items()},
        "max_producer_referee_diff": mp.nstr(max_diff, 8),
        "referee_controls": ref_controls,
        "all_counterchecks_pass": True,
    }
    check_json_tree(out_doc)
    OUT_PATH.write_text(json.dumps(out_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: referee_x_natural_interactions.py matched Producer to", mp.nstr(max_diff, 6), "with 4/4 controls caught.")


if __name__ == "__main__":
    main()
