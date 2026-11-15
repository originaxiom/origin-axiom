#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-ENDGAME-3 (0 of 19).

Verifies:
  Part 3A (Weight-Zero Symmetric Puncture-Jet Seesaw Operator M_R(tau) & Exact T, S Covariance):
    - Constructs M_R(tau) = y^3 conj(E_6(tau)) v(tau) v(tau)^T + y^2 conj(E_4(tau)) w(tau) w(tau)^T
      + u(tau) u(tau)^T in 35-digit mpmath from the spin-(1/2, 3/2) puncture value, z-derivative,
      and Ramanujan-Serre covariant tau-derivative at z = 0.
    - Verifies ||M_R - M_R^T||_F / ||M_R||_F < 1e-30, full rank 3 at tau* = 2*sqrt(3)*i
      (vs planted control PC_ENDGAME3_Rank2JetSingularity dropping u(tau)), and exact T- and S-
      covariance of BOTH M_R(tau) and the ABSOLUTE singular values of W_4(tau, w) = Y_4 M_R^-1 Y_4^T
      to < 1e-24 (vs planted control PC_ENDGAME3_DiracSesquilinearMismatch breaking S-covariance > 0.5).

  Part 3B (Six-Unitary U(3)^6 Haar Scrambling Gate & Unified V_{12} vs U_{34} Mixing Contrast):
    - Evaluates Y_1, Y_2, Y_3, Y_4 (with T_{3R} cusp-collar normalization from Stage 1), M_R, and
      W_4 = Y_4 M_R^-1 Y_4^T at (tau* = 2*sqrt(3)*i, w = (4/15, 8/15)) in 35-digit precision.
    - Applies 10 independent random Haar U(3)^6 basis rotations (including symmetric Majorana
      transformation M_R -> U_{4R}^* M_R U_{4R}^dag) and verifies invariance of all singular-value
      ratios and all 18 entries of |V_{12}| and |U_{34}| to < 1e-18 (< 1e-12 guardrail).
    - Records all 9 entries of |V_{12}| and |U_{34}| verbatim, verifying max off-diagonal |V_{12}| < 0.03
      while max off-diagonal |U_{34}| lies in [0.65, 0.75] (sin^2(2 theta) > 0.99 in the parity-mixed block).

  Part 3C (Zero-Fudge Amphichiral Determinant-Phase Audit):
    - Computes arg det(Y_1 Y_2) directly from explicit 35-digit matrix determinants (zero literal flags)
      on w = (4/15, 8/15), on its amphichiral mirror R(w) = (4/15, -8/15), on the 6x6 parity-completed
      direct sum (Y_1(w) (+) Y_1(R w))(Y_2(w) (+) Y_2(R w)), and across all 4 points of O_4.
    - Verifies planted control PC_ENDGAME3_SingleSlicePhaseNonZero (|arg det| > 0.5 on single slice)
      alongside exact amphichiral parity cancellation |arg det_6x6| < 1e-30.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "fractions",
    "hashlib",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "typing",
}


def verify_ast_zero_imports() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])
    disallowed = sorted(mods - ALLOWED_IMPORTS)
    return {
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
    }


# ============================================================================
# SECTION 1: 35-DIGIT MAGNETIZED OVERLAP & SYMMETRIC PUNCTURE-JET SEESAW M_R
# ============================================================================

def erfcx_mp(x: Any) -> Any:
    with mp.extradps(60):
        return mp.exp(x * x) * mp.erfc(x)


def erfc_integral_mp(alpha: Any, beta: Any, u0: Any, thresh: float) -> Any:
    xm = alpha * u0 - beta / u0
    xp = alpha * u0 + beta / u0
    edge_exp = (alpha * u0) ** 2 + (beta / u0) ** 2
    sqrt_pi = mp.sqrt(mp.pi)
    if xm >= 0:
        if float(edge_exp) > thresh:
            return mp.mpf(0)
        return (sqrt_pi / (2 * alpha)) * mp.exp(-edge_exp) * (erfcx_mp(xm) + erfcx_mp(xp))
    if float(2 * alpha * beta) > thresh:
        return mp.mpf(0)
    part1 = 2 * mp.exp(-2 * alpha * beta)
    part2 = mp.mpf(0) if float(edge_exp) > thresh else mp.exp(-edge_exp) * (erfcx_mp(xp) - erfcx_mp(-xm))
    return (sqrt_pi / (2 * alpha)) * (part1 + part2)


def y_mag_overlap_mp(tau: Any, a_fr: Fraction, b_fr: Fraction, ql: int, qr: int) -> Any:
    qh = -(ql + qr)
    tau1, tau2 = mp.re(tau), mp.im(tau)
    a = mp.mpf(a_fr.numerator) / mp.mpf(a_fr.denominator)
    b = mp.mpf(b_fr.numerator) / mp.mpf(b_fr.denominator)
    half = mp.mpf(1) / mp.mpf(2)
    u0 = 1 / mp.sqrt(6)
    u_split = mp.sqrt(tau2)
    sqrt_tau2 = mp.sqrt(tau2)
    sqrt_pi = mp.sqrt(mp.pi)
    thresh = mp.mp.dps * 2.45 + 14.0

    t2_f = float(tau2)
    k_max = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * t2_f)) / 3.0)) + 3
    l_quad = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * t2_f)))) + 4
    l_riem = int(math.ceil(math.sqrt(thresh / math.pi))) + 3

    def f_prim(u_val: Any, b_val: Any) -> Any:
        if b_val == 0:
            return 2 * u_val
        bv_u = b_val / u_val
        if float(bv_u * bv_u) > thresh:
            return mp.mpf(0)
        return 2 * mp.exp(-(bv_u * bv_u)) * (u_val - sqrt_pi * b_val * erfcx_mp(bv_u))

    y_mat = mp.zeros(3, 3)
    for i in range(3):
        c_l = (mp.mpf(i) + half + ql * a) / 3
        zak_ang = -2 * mp.pi * (ql * b / 3) * (mp.mpf(i) + half)
        zak_ph = mp.exp(1j * zak_ang)
        for j in range(3):
            c_r = (mp.mpf(j) + half - qr * a) / 3
            acc = mp.mpc(0)
            for k in range(-k_max, k_max + 1):
                n = (j - i) - 3 * k
                na = mp.mpf(n) + qh * a
                delta_k = na / 3
                xi0 = (c_l + c_r - k) / 2
                x0 = na * tau1 + qh * b
                ang0 = mp.pi * delta_k * ((qr - ql) * b - 3)
                base_phase = mp.exp(1j * ang0)
                if abs(na) > mp.mpf("1e-28"):
                    alpha = mp.sqrt(mp.pi * tau2) * abs(na)
                    l_lin = int(math.ceil(thresh / (2.0 * math.pi * t2_f * float(abs(na))))) + 3
                    l_max_na = max(l_lin, l_quad)
                    sub = mp.mpc(0)
                    l_center = int(round(float(xi0)))
                    for dl in range(-l_max_na, l_max_na + 1):
                        l_idx = l_center + dl
                        beta = mp.sqrt(mp.pi * tau2) * abs(mp.mpf(l_idx) - xi0)
                        iv = sqrt_tau2 * erfc_integral_mp(alpha, beta, u0, thresh)
                        if iv != 0:
                            ang = 2 * mp.pi * (mp.mpf(l_idx) - xi0) * x0
                            sub += iv * mp.exp(1j * ang)
                    acc += base_phase * sub
                else:
                    sub1 = mp.mpc(0)
                    l_center = int(round(float(xi0)))
                    for dl in range(-l_riem, l_riem + 1):
                        l_idx = l_center + dl
                        beta = mp.sqrt(mp.pi * tau2) * abs(mp.mpf(l_idx) - xi0)
                        iv = sqrt_tau2 * (f_prim(u_split, beta) - f_prim(u0, beta))
                        if iv != 0:
                            ang = 2 * mp.pi * (mp.mpf(l_idx) - xi0) * x0
                            sub1 += iv * mp.exp(1j * ang)
                    sub2 = mp.mpc(0)
                    m_center = int(round(-float(x0)))
                    for dm in range(-l_riem, l_riem + 1):
                        m_idx = m_center + dm
                        mx = mp.mpf(m_idx) + x0
                        if abs(mx) > mp.mpf("1e-28") and float(mp.pi * mx * mx) <= thresh:
                            ang = 2 * mp.pi * m_idx * xi0
                            sub2 += (tau2 / (mp.pi * mx * mx)) * mp.exp(-mp.pi * mx * mx) * mp.exp(1j * ang)
                    acc += base_phase * (sub1 + sub2)
            y_mat[i, j] = zak_ph * acc
    return y_mat


def eisenstein_2_4_6_mp(tau: Any) -> Tuple[Any, Any, Any]:
    q = mp.exp(2j * mp.pi * tau)
    n_max = int((mp.mp.dps * 2.4 + 12.0) / (2.0 * math.pi * max(float(mp.im(tau)), 0.3))) + 8
    s1 = mp.mpc(0)
    s3 = mp.mpc(0)
    s5 = mp.mpc(0)
    qn = q
    for n in range(1, n_max + 1):
        d = qn / (1 - qn)
        s1 += n * d
        s3 += (n ** 3) * d
        s5 += (n ** 5) * d
        qn *= q
    e2_holo = 1 - 24 * s1
    e4 = 1 + 240 * s3
    e6 = 1 - 504 * s5
    return e2_holo, e4, e6


def majorana_puncture_jet_mp(tau: Any, include_serre_u: bool = True) -> Any:
    """
    Constructs the weight-0, symmetric, SL(2, Z)-covariant Majorana operator M_R(tau)
    on q = 0 from the spin-(1/2, 3/2) puncture value, z-derivative, and Serre derivative.
    """
    y = mp.im(tau)
    e2_holo, e4, e6 = eisenstein_2_4_6_mp(tau)
    half = mp.mpf(1) / mp.mpf(2)
    three_halves = mp.mpf(3) / mp.mpf(2)
    n_span = int(math.sqrt((mp.mp.dps * 2.4 + 14.0) / (3.0 * math.pi * max(float(y), 0.3)))) + 6

    v_raw = [mp.mpc(0)] * 3
    w_raw = [mp.mpc(0)] * 3
    u_raw = [mp.mpc(0)] * 3

    for j in range(3):
        ac = (mp.mpf(j) + half) / 3
        sv = mp.mpc(0)
        sw = mp.mpc(0)
        dtau_sw = mp.mpc(0)
        for n in range(-n_span, n_span + 1):
            na = mp.mpf(n) + ac
            ph = mp.exp(1j * mp.pi * (na * na) * (3 * tau) + 2j * mp.pi * na * three_halves)
            sv += ph
            cz = 3j * na
            sw += cz * ph
            dtau_sw += cz * (three_halves * (na * na)) * ph
        serre_sw = dtau_sw - (three_halves / 12) * e2_holo * sw
        v_raw[j] = (y ** (mp.mpf(1) / mp.mpf(4))) * mp.conj(sv)
        w_raw[j] = (y ** (mp.mpf(3) / mp.mpf(4))) * mp.conj(sw)
        u_raw[j] = (y ** (mp.mpf(7) / mp.mpf(4))) * mp.conj(serre_sw)

    m_r = mp.zeros(3, 3)
    c_v = (y ** 3) * mp.conj(e6)
    c_w = (y ** 2) * mp.conj(e4)
    for r in range(3):
        for c in range(3):
            val = c_v * v_raw[r] * v_raw[c] + c_w * w_raw[r] * w_raw[c]
            if include_serre_u:
                val += u_raw[r] * u_raw[c]
            m_r[r, c] = val
    return m_r


# ============================================================================
# SECTION 2: LINEAR ALGEBRA & HAAR UNITARY HELPERS IN MPMATH
# ============================================================================

def herm_eigh_sorted_mp(h_mat: Any) -> Tuple[List[Any], Any]:
    """
    Returns ascending real eigenvalues and unitary eigenvector matrix U (columns = eigenvectors)
    of a 3x3 Hermitian matrix h_mat = Y Y^dag in high-precision mpmath.
    """
    vals, vecs = mp.eighe(h_mat)
    order = sorted(range(3), key=lambda idx: mp.re(vals[idx]))
    u_sorted = mp.zeros(3, 3)
    s_sorted: List[Any] = []
    for col_new, col_old in enumerate(order):
        s_sorted.append(mp.re(vals[col_old]))
        # Normalize column explicitly
        nrm = mp.sqrt(sum(abs(vecs[r, col_old]) ** 2 for r in range(3)))
        for r in range(3):
            u_sorted[r, col_new] = vecs[r, col_old] / nrm
    return s_sorted, u_sorted


def svd_singular_values_mp(mat: Any) -> List[Any]:
    h = mat * mat.transpose_conj()
    vals, _ = herm_eigh_sorted_mp(h)
    return [mp.sqrt(max(v, mp.mpf(0))) for v in vals]


def random_haar_u3_mp(seed: int) -> Any:
    rng = np.random.default_rng(seed)
    a_re = rng.normal(size=(3, 3))
    a_im = rng.normal(size=(3, 3))
    cols = []
    for c in range(3):
        v = [mp.mpc(mp.mpf(float(a_re[r, c])), mp.mpf(float(a_im[r, c]))) for r in range(3)]
        for prev in cols:
            proj = sum(mp.conj(prev[r]) * v[r] for r in range(3))
            v = [v[r] - proj * prev[r] for r in range(3)]
        nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
        cols.append([v[r] / nrm for r in range(3)])
    u = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            u[r, c] = cols[c][r]
    return u


def mat_transpose_mp(mat: Any) -> Any:
    res = mp.zeros(mat.rows, mat.cols)
    for r in range(mat.rows):
        for c in range(mat.cols):
            res[r, c] = mat[c, r]
    return res


def mat_conj_mp(mat: Any) -> Any:
    res = mp.zeros(mat.rows, mat.cols)
    for r in range(mat.rows):
        for c in range(mat.cols):
            res[r, c] = mp.conj(mat[r, c])
    return res


def collar_amp_mp(kappa_int: int, l_cusp: Any) -> Any:
    if kappa_int == 0:
        return 1 / mp.sqrt(l_cusp)
    k = mp.mpf(kappa_int)
    # Exact integral int_0^{L} exp(2 k t) dt = (exp(2 k L) - 1) / (2 k)
    norm_sq = (mp.exp(2 * k * l_cusp) - 1) / (2 * k)
    return mp.exp(k * l_cusp) / mp.sqrt(norm_sq)


# ============================================================================
# SECTION 3: EXECUTION OF PARTS 3A, 3B, AND 3C
# ============================================================================

def run_stage_3() -> Dict[str, Any]:
    with mp.workdps(35):
        # Part 3A: Exact T and S modular covariance at generic bulk point tau_test = 17/100 + 143/100 i
        tau_test = mp.mpc(mp.mpf(17) / mp.mpf(100), mp.mpf(143) / mp.mpf(100))
        a_w, b_w = Fraction(4, 15), Fraction(8, 15)

        ut_r = mp.diag([mp.exp(1j * mp.pi * ((2 * j + 1) ** 2) / 12) for j in range(3)])
        w3 = mp.exp(2j * mp.pi / 3)
        us_r = mp.matrix([[w3 ** ((j - 1) * (k - 1)) / mp.sqrt(3) for k in range(3)] for j in range(3)])

        mr_0 = majorana_puncture_jet_mp(tau_test, include_serre_u=True)
        mr_t = majorana_puncture_jet_mp(tau_test + 1, include_serre_u=True)
        mr_s = majorana_puncture_jet_mp(-1 / tau_test, include_serre_u=True)

        mr_sym_err = mp.mnorm(mr_0 - mat_transpose_mp(mr_0), "F") / mp.mnorm(mr_0, "F")
        mr_t_cov_err = mp.mnorm(
            mr_t - mat_conj_mp(ut_r) * mr_0 * ut_r.transpose_conj(), "F"
        ) / mp.mnorm(mr_0, "F")
        s_mult = -1j * ((mp.conj(tau_test) / abs(tau_test)) ** 7)
        mr_s_cov_err = mp.mnorm(
            mr_s - s_mult * (mat_conj_mp(us_r) * mr_0 * us_r.transpose_conj()), "F"
        ) / mp.mnorm(mr_0, "F")

        y4_0 = y_mag_overlap_mp(tau_test, a_w, b_w, -3, 0)
        y4_t = y_mag_overlap_mp(tau_test + 1, a_w, b_w - a_w, -3, 0)
        y4_s = y_mag_overlap_mp(-1 / tau_test, -b_w, a_w, -3, 0)

        w4_0 = y4_0 * (mr_0 ** (-1)) * mat_transpose_mp(y4_0)
        w4_t = y4_t * (mr_t ** (-1)) * mat_transpose_mp(y4_t)
        w4_s = y4_s * (mr_s ** (-1)) * mat_transpose_mp(y4_s)

        sv_w4_0 = svd_singular_values_mp(w4_0)
        sv_w4_t = svd_singular_values_mp(w4_t)
        sv_w4_s = svd_singular_values_mp(w4_s)

        w4_abs_t_err = max(abs(sv_w4_t[k] - sv_w4_0[k]) for k in range(3)) / sv_w4_0[2]
        w4_abs_s_err = max(abs(sv_w4_s[k] - sv_w4_0[k]) for k in range(3)) / sv_w4_0[2]

        # Planted control PC_ENDGAME3_DiracSesquilinearMismatch: M_bad = Y_(0,0)(tau) * P_C
        p_c = mp.matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        mbad_0 = y_mag_overlap_mp(tau_test, Fraction(0), Fraction(0), 0, 0) * p_c
        mbad_s = y_mag_overlap_mp(-1 / tau_test, Fraction(0), Fraction(0), 0, 0) * p_c
        wbad_0 = y4_0 * (mbad_0 ** (-1)) * mat_transpose_mp(y4_0)
        wbad_s = y4_s * (mbad_s ** (-1)) * mat_transpose_mp(y4_s)
        sv_bad_0 = svd_singular_values_mp(wbad_0)
        sv_bad_s = svd_singular_values_mp(wbad_s)
        pc_dirac_sesquilinear_s_ratio_err = max(
            abs(sv_bad_s[k] / sv_bad_s[2] - sv_bad_0[k] / sv_bad_0[2]) for k in range(2)
        )

        # Evaluate at Stage 1-2 geometry tau* = 2*sqrt(3)*i, w = (4/15, 8/15):
        l_cusp = 2 * mp.sqrt(3)
        tau_star = mp.mpc(0, l_cusp)
        mr_star = majorana_puncture_jet_mp(tau_star, include_serre_u=True)
        sv_mr_star = svd_singular_values_mp(mr_star)
        mr_star_s1_over_s3 = sv_mr_star[0] / sv_mr_star[2]

        # Planted control PC_ENDGAME3_Rank2JetSingularity: drop Serre derivative u(tau)
        with mp.extradps(55):
            mr_rank2 = majorana_puncture_jet_mp(tau_star, include_serre_u=False)
            sv_mr_rank2 = svd_singular_values_mp(mr_rank2)
            pc_rank2_s1_over_s3 = sv_mr_rank2[0] / sv_mr_rank2[2]

        e1_passed = bool(
            float(mr_sym_err) < 1e-30
            and float(mr_star_s1_over_s3) > 1e-9
            and float(mr_t_cov_err) < 1e-24
            and float(mr_s_cov_err) < 1e-24
            and float(w4_abs_t_err) < 1e-24
            and float(w4_abs_s_err) < 1e-24
            and float(pc_dirac_sesquilinear_s_ratio_err) > 0.5
            and float(pc_rank2_s1_over_s3) < 1e-36
        )

        # Part 3B: T_{3R}-normalized Y_1, Y_2, Y_3, Y_4 + Seesaw W_4 + 6-Unitary Haar Scrambling Gate
        amp_0 = collar_amp_mp(0, l_cusp)
        amp_p1 = collar_amp_mp(1, l_cusp)
        amp_m1 = collar_amp_mp(-1, l_cusp)

        y1 = (amp_0 * amp_p1) * y_mag_overlap_mp(tau_star, a_w, b_w, 1, -4)
        y2 = (amp_0 * amp_m1) * y_mag_overlap_mp(tau_star, a_w, b_w, 1, 2)
        y3 = (amp_0 * amp_m1) * y_mag_overlap_mp(tau_star, a_w, b_w, -3, 6)
        y4 = (amp_0 * amp_p1) * y_mag_overlap_mp(tau_star, a_w, b_w, -3, 0)
        w4 = y4 * (mr_star ** (-1)) * mat_transpose_mp(y4)

        def extract_observables(
            m_y1: Any, m_y2: Any, m_y3: Any, m_y4: Any, m_mr: Any
        ) -> Tuple[List[Any], List[List[Any]], List[List[Any]]]:
            m_w4 = m_y4 * (m_mr ** (-1)) * mat_transpose_mp(m_y4)
            e1, u1 = herm_eigh_sorted_mp(m_y1 * m_y1.transpose_conj())
            e2, u2 = herm_eigh_sorted_mp(m_y2 * m_y2.transpose_conj())
            e3, u3 = herm_eigh_sorted_mp(m_y3 * m_y3.transpose_conj())
            e4, u4 = herm_eigh_sorted_mp(m_w4 * m_w4.transpose_conj())

            s1 = [mp.sqrt(max(v, mp.mpf(0))) for v in e1]
            s2 = [mp.sqrt(max(v, mp.mpf(0))) for v in e2]
            s3 = [mp.sqrt(max(v, mp.mpf(0))) for v in e3]
            s4 = [mp.sqrt(max(v, mp.mpf(0))) for v in e4]

            ratios = [
                s1[1] / s1[2], s1[0] / s1[1],
                s2[1] / s2[2], s2[0] / s2[1],
                s3[1] / s3[2], s3[0] / s3[1],
                s4[1] / s4[2], s4[0] / s4[1],
                s1[2] / s2[2], s2[2] / s3[2],
            ]
            v12_m = u1.transpose_conj() * u2
            u34_m = u3.transpose_conj() * u4
            v12_abs = [[abs(v12_m[r, c]) for c in range(3)] for r in range(3)]
            u34_abs = [[abs(u34_m[r, c]) for c in range(3)] for r in range(3)]
            return ratios, v12_abs, u34_abs

        base_ratios, base_v12, base_u34 = extract_observables(y1, y2, y3, y4, mr_star)

        haar_max_err = mp.mpf(0)
        for trial in range(10):
            u_q = random_haar_u3_mp(7100 + 6 * trial)
            u_1r = random_haar_u3_mp(7101 + 6 * trial)
            u_2r = random_haar_u3_mp(7102 + 6 * trial)
            u_l = random_haar_u3_mp(7103 + 6 * trial)
            u_3r = random_haar_u3_mp(7104 + 6 * trial)
            u_4r = random_haar_u3_mp(7105 + 6 * trial)

            y1_s = u_q * y1 * u_1r.transpose_conj()
            y2_s = u_q * y2 * u_2r.transpose_conj()
            y3_s = u_l * y3 * u_3r.transpose_conj()
            y4_s = u_l * y4 * u_4r.transpose_conj()
            # Symmetric Majorana transformation on q = 0 right-handed singlet:
            mr_scr = mat_conj_mp(u_4r) * mr_star * u_4r.transpose_conj()

            r_h, v12_h, u34_h = extract_observables(y1_s, y2_s, y3_s, y4_s, mr_scr)
            for idx in range(len(base_ratios)):
                haar_max_err = max(haar_max_err, abs(r_h[idx] - base_ratios[idx]))
            for r in range(3):
                for c in range(3):
                    haar_max_err = max(
                        haar_max_err,
                        abs(v12_h[r][c] - base_v12[r][c]),
                        abs(u34_h[r][c] - base_u34[r][c]),
                    )

        s3_perms = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        v12_off_max = min(
            max(float(base_v12[r][perm[c]]) for r in range(3) for c in range(3) if r != c)
            for perm in s3_perms
        )
        u34_off_max = min(
            max(float(base_u34[r][perm[c]]) for r in range(3) for c in range(3) if r != c)
            for perm in s3_perms
        )
        u34_raw_ascending_offdiag_max = max(
            float(base_u34[r][c]) for r in range(3) for c in range(3) if r != c
        )
        # sin^2(2 theta_23_block) = 4 |U_{1,0}|^2 |U_{1,1}|^2
        u34_parity_block_sin2_2theta = float(4 * (base_u34[1][0] ** 2) * (base_u34[1][1] ** 2))

        e2_passed = bool(
            float(haar_max_err) < 1e-18
            and v12_off_max < 0.03
            and (0.65 <= u34_off_max <= 0.75)
            and u34_parity_block_sin2_2theta > 0.99
        )

        # Part 3C: Zero-Fudge Amphichiral Determinant-Phase Audit
        y1_mirror = (amp_0 * amp_p1) * y_mag_overlap_mp(tau_star, a_w, -b_w, 1, -4)
        y2_mirror = (amp_0 * amp_m1) * y_mag_overlap_mp(tau_star, a_w, -b_w, 1, 2)

        det_single = mp.det(y1 * y2)
        det_mirror = mp.det(y1_mirror * y2_mirror)
        arg_single = mp.arg(det_single)
        arg_mirror = mp.arg(det_mirror)

        # Explicit 6x6 parity-completed block operator (Y1(w) (+) Y1(Rw)) * (Y2(w) (+) Y2(Rw)):
        prod_6x6 = mp.zeros(6, 6)
        p_w = y1 * y2
        p_rw = y1_mirror * y2_mirror
        for r in range(3):
            for c in range(3):
                prod_6x6[r, c] = p_w[r, c]
                prod_6x6[r + 3, c + 3] = p_rw[r, c]
        det_6x6 = mp.det(prod_6x6)
        arg_6x6 = mp.arg(det_6x6)

        # Also evaluate arg det(Y1 Y2) across all 4 points of O_4:
        o4_phases: Dict[str, float] = {}
        for p5, q5 in [(1, 2), (2, 4), (3, 1), (4, 3)]:
            ya = y_mag_overlap_mp(tau_star, Fraction(p5, 5), Fraction(q5, 5), 1, -4)
            yb = y_mag_overlap_mp(tau_star, Fraction(p5, 5), Fraction(q5, 5), 1, 2)
            o4_phases[f"{p5}/5,{q5}/5"] = float(mp.arg(mp.det(ya * yb)))

        e3_passed = bool(
            (0.5 <= float(abs(arg_single)) <= 1.0)
            and float(abs(arg_single + arg_mirror)) < 1e-30
            and float(abs(arg_6x6)) < 1e-30
        )

    return {
        "part_3a_modular_covariant_seesaw": {
            "E1_Symmetric_Seesaw_Modular_Covariance_passed": e1_passed,
            "M_R_symmetry_rel_err": float(mr_sym_err),
            "M_R_T_covariance_rel_err": float(mr_t_cov_err),
            "M_R_S_covariance_rel_err": float(mr_s_cov_err),
            "W_4_absolute_sv_T_err": float(w4_abs_t_err),
            "W_4_absolute_sv_S_err": float(w4_abs_s_err),
            "M_R_tau_star_singular_values": [float(v) for v in sv_mr_star],
            "M_R_tau_star_s1_over_s3": float(mr_star_s1_over_s3),
            "PC_ENDGAME3_DiracSesquilinearMismatch_S_err": float(pc_dirac_sesquilinear_s_ratio_err),
            "PC_ENDGAME3_Rank2JetSingularity_s1_over_s3": float(pc_rank2_s1_over_s3),
        },
        "part_3b_haar_u3_6_and_mixing": {
            "E2_Haar_U3_6_and_Large_vs_Small_Mixing_passed": e2_passed,
            "Gate_Haar_Stage3_max_err_10_trials": float(haar_max_err),
            "sec4_singular_ratios_s23_s12": [float(base_ratios[6]), float(base_ratios[7])],
            "V_12_abs_matrix": [[float(x) for x in row] for row in base_v12],
            "U_34_abs_matrix": [[float(x) for x in row] for row in base_u34],
            "V_12_max_offdiag": v12_off_max,
            "U_34_max_offdiag": u34_off_max,
            "U_34_raw_ascending_offdiag_max_inverted_alignment": u34_raw_ascending_offdiag_max,
            "U_34_over_V_12_max_offdiag_ratio": u34_off_max / v12_off_max,
            "U_34_parity_block_sin2_2theta": u34_parity_block_sin2_2theta,
            "U_34_sequential_third_mode_max_angle": float(max(base_u34[0][0], base_u34[0][1])),
        },
        "part_3c_amphichiral_phase_audit": {
            "E3_Amphichiral_Determinant_Phase_Theorem_passed": e3_passed,
            "single_slice_4_15_8_15_arg_det_rad": float(arg_single),
            "mirror_slice_4_15_minus8_15_arg_det_rad": float(arg_mirror),
            "single_plus_mirror_sum_abs": float(abs(arg_single + arg_mirror)),
            "parity_completed_6x6_arg_det_abs": float(abs(arg_6x6)),
            "PC_ENDGAME3_SingleSlicePhaseNonZero_passed": bool(float(abs(arg_single)) > 0.5),
            "O_4_single_slice_phases_rad": o4_phases,
        },
    }


def main() -> None:
    ast_info = verify_ast_zero_imports()
    res = run_stage_3()

    p3a = res["part_3a_modular_covariant_seesaw"]
    p3b = res["part_3b_haar_u3_6_and_mixing"]
    p3c = res["part_3c_amphichiral_phase_audit"]

    all_controls_passed = bool(
        ast_info["zero_imports_from_main_or_other_relays"]
        and p3b["Gate_Haar_Stage3_max_err_10_trials"] < 1e-12
        and p3a["PC_ENDGAME3_DiracSesquilinearMismatch_S_err"] > 0.5
        and p3a["PC_ENDGAME3_Rank2JetSingularity_s1_over_s3"] < 1e-36
        and p3c["PC_ENDGAME3_SingleSlicePhaseNonZero_passed"]
    )
    stage_3_passed = bool(
        all_controls_passed
        and p3a["E1_Symmetric_Seesaw_Modular_Covariance_passed"]
        and p3b["E2_Haar_U3_6_and_Large_vs_Small_Mixing_passed"]
        and p3c["E3_Amphichiral_Determinant_Phase_Theorem_passed"]
    )

    payload: Dict[str, Any] = {
        "card": "X-ENDGAME-3",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_info,
        "part_3a_modular_covariant_seesaw": p3a,
        "part_3b_haar_u3_6_and_mixing": p3b,
        "part_3c_amphichiral_phase_audit": p3c,
        "all_planted_controls_passed": all_controls_passed,
        "stage_3_gate_passed": stage_3_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_endgame_3_out.json"
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_endgame_3_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
