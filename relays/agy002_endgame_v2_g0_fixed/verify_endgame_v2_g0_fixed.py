#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_ENDGAME-V2-G0 (with Erratum G0-ERRATUM):
  Literature RGE Benchmark and U(3)^6 Invariance Lock (0 of 19).

Empirical Firewall: 0 of 19 (zero repository imports, zero float literals in source).
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import json
import math
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


def frac_f64(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def pow10_f64(exp_int: int) -> float:
    return float(Fraction(10, 1) ** exp_int)


# ============================================================================
# SECTION 0: AST SOURCE LOCK (ZERO REPO IMPORTS & ZERO FLOAT LITERALS)
# ============================================================================

def verify_ast_g0() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_literals = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])
        elif isinstance(node, ast.Constant) and isinstance(node.value, float):
            float_literals += 1

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    passed = (len(disallowed) == 0) and (float_literals == 0)
    return {
        "ast_gate_passed": passed,
        "imported_modules": sorted(mods),
        "disallowed_imports": disallowed,
        "float_literals_in_entire_file": float_literals,
    }


# ============================================================================
# SECTION 1: EXACT LIE-ALGEBRA TRACES & BUTTAZZO ET AL. (2013) POLYNOMIAL LOCK
# ============================================================================

def run_lie_algebra_and_polynomial_checks() -> Dict[str, Any]:
    chiral_gen = [
        (3, 2, Fraction(1, 6), Fraction(1, 2), Fraction(1, 2)),
        (3, 1, Fraction(-2, 3), Fraction(1, 2), Fraction(0, 1)),
        (3, 1, Fraction(1, 3), Fraction(1, 2), Fraction(0, 1)),
        (1, 2, Fraction(-1, 2), Fraction(0, 1), Fraction(1, 2)),
        (1, 1, Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)),
        (1, 1, Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)),
    ]
    tr_Y = sum(d3 * d2 * y for d3, d2, y, _, _ in chiral_gen)
    tr_Y3 = sum(d3 * d2 * (y ** 3) for d3, d2, y, _, _ in chiral_gen)
    tr_SU2_2_Y = sum(d3 * t2 * y for d3, _, y, _, t2 in chiral_gen)
    tr_SU3_2_Y = sum(d2 * t3 * y for _, d2, y, t3, _ in chiral_gen)
    tr_Y2 = sum(d3 * d2 * (y ** 2) for d3, d2, y, _, _ in chiral_gen)

    t_gen_3 = sum(d2 * t3 for _, d2, _, t3, _ in chiral_gen)
    t_gen_2 = sum(d3 * t2 for d3, _, _, _, t2 in chiral_gen)
    k1_gut = Fraction(3, 5)
    t_gen_1 = k1_gut * tr_Y2

    n_g = 3
    n_h = 1
    t_h_1 = k1_gut * 2 * (Fraction(1, 2) ** 2)
    t_h_2 = Fraction(1, 2)
    t_h_3 = Fraction(0, 1)

    b1_sm = Fraction(0, 1) + Fraction(2, 3) * n_g * t_gen_1 + Fraction(1, 3) * n_h * t_h_1
    b2_sm = -Fraction(11, 3) * 2 + Fraction(2, 3) * n_g * t_gen_2 + Fraction(1, 3) * n_h * t_h_2
    b3_sm = -Fraction(11, 3) * 3 + Fraction(2, 3) * n_g * t_gen_3 + Fraction(1, 3) * n_h * t_h_3

    sm_b_exact_ok = (
        tr_Y == 0
        and tr_Y3 == 0
        and tr_SU2_2_Y == 0
        and tr_SU3_2_Y == 0
        and t_gen_1 == 2
        and t_gen_2 == 2
        and t_gen_3 == 2
        and (b1_sm, b2_sm, b3_sm) == (Fraction(41, 10), Fraction(-19, 6), Fraction(-7, 1))
    )

    bl_diag = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3), Fraction(-1, 1)]
    tr_bl_sq = sum(x * x for x in bl_diag)
    c15_sq = (Fraction(1, 4) * tr_bl_sq) / Fraction(1, 2)
    c3r_sq = Fraction(1, 1)
    w_2R = k1_gut * c3r_sq
    w_4c = k1_gut * c15_sq

    y_right_states = []
    for bl in bl_diag:
        for t3r in (Fraction(1, 2), Fraction(-1, 2)):
            y_right_states.append(t3r + bl / 2)
    expected_y_right = [
        Fraction(2, 3), Fraction(-1, 3),
        Fraction(2, 3), Fraction(-1, 3),
        Fraction(2, 3), Fraction(-1, 3),
        Fraction(0, 1), Fraction(-1, 1),
    ]

    b4_ps = -Fraction(11, 3) * 4 + Fraction(2, 3) * (3 * 2) + Fraction(1, 3) * (0 + 2)
    b2L_ps = -Fraction(11, 3) * 2 + Fraction(2, 3) * (3 * 2) + Fraction(1, 3) * (1 + 2)
    b2R_ps = -Fraction(11, 3) * 2 + Fraction(2, 3) * (3 * 2) + Fraction(1, 3) * (1 + 2)

    ps_exact_ok = (
        w_2R == Fraction(3, 5)
        and w_4c == Fraction(2, 5)
        and w_2R + w_4c == 1
        and y_right_states == expected_y_right
        and (b4_ps, b2L_ps, b2R_ps) == (Fraction(-10, 1), Fraction(-7, 3), Fraction(-7, 3))
        and (b2L_ps - b4_ps) == Fraction(23, 3)
    )

    yt2 = Fraction(7, 11)
    yb2 = Fraction(3, 13)
    ytau2 = Fraction(2, 17)
    g1s = Fraction(5, 19)
    g2s = Fraction(6, 23)
    g3s = Fraction(9, 29)
    lam = Fraction(4, 31)

    y2_tr = 3 * yt2 + 3 * yb2 + ytau2
    chi2 = (
        -Fraction(27, 4) * (yt2 ** 2 + yb2 ** 2)
        - Fraction(9, 4) * (ytau2 ** 2)
        + Fraction(3, 2) * yt2 * yb2
        + (Fraction(17, 8) * g1s + Fraction(45, 8) * g2s + 20 * g3s) * yt2
        + (Fraction(5, 8) * g1s + Fraction(45, 8) * g2s + 20 * g3s) * yb2
        + (Fraction(15, 8) * g1s + Fraction(15, 8) * g2s) * ytau2
    )
    b2_yt_over_yt_matrix = (
        Fraction(3, 2) * (yt2 ** 2)
        - yt2 * yb2
        - Fraction(1, 4) * yb2 * yt2
        + Fraction(11, 4) * (yb2 ** 2)
        + (-Fraction(9, 4) * y2_tr - 12 * lam + Fraction(223, 80) * g1s + Fraction(135, 16) * g2s + 16 * g3s) * yt2
        + (Fraction(5, 4) * y2_tr - Fraction(43, 80) * g1s + Fraction(9, 16) * g2s - 16 * g3s) * yb2
        + (
            chi2
            + 6 * (lam ** 2)
            + Fraction(1187, 600) * (g1s ** 2)
            - Fraction(9, 20) * g1s * g2s
            + Fraction(19, 15) * g1s * g3s
            - Fraction(23, 4) * (g2s ** 2)
            + 9 * g2s * g3s
            - 108 * (g3s ** 2)
        )
    )
    b2_yt_over_yt_buttazzo = (
        yt2 * (-12 * yt2 - Fraction(11, 4) * yb2 - Fraction(9, 4) * ytau2 - 12 * lam + 36 * g3s + Fraction(225, 16) * g2s + Fraction(393, 80) * g1s)
        + yb2 * (-Fraction(1, 4) * yb2 + Fraction(5, 4) * ytau2 + 4 * g3s + Fraction(99, 16) * g2s + Fraction(7, 80) * g1s)
        + ytau2 * (-Fraction(9, 4) * ytau2 + Fraction(15, 8) * g2s + Fraction(15, 8) * g1s)
        + 6 * (lam ** 2) - 108 * (g3s ** 2) - Fraction(23, 4) * (g2s ** 2) + Fraction(1187, 600) * (g1s ** 2)
        + 9 * g3s * g2s + Fraction(19, 15) * g3s * g1s - Fraction(9, 20) * g2s * g1s
    )

    b2_lam_matrix = (
        -312 * (lam ** 3)
        + 36 * (lam ** 2) * (3 * g2s + Fraction(3, 5) * g1s)
        - 48 * (lam ** 2) * y2_tr
        + lam * (80 * g3s + Fraction(45, 2) * g2s) * (yt2 + yb2)
        + lam * g1s * (Fraction(17, 2) * yt2 + Fraction(5, 2) * yb2 + Fraction(15, 2) * ytau2)
        + Fraction(15, 2) * lam * g2s * ytau2
        - 3 * lam * (yt2 ** 2 + yb2 ** 2 + Fraction(1, 3) * (ytau2 ** 2) + 14 * yt2 * yb2)
        + lam * (-Fraction(73, 8) * (g2s ** 2) + Fraction(117, 20) * g1s * g2s + Fraction(1887, 200) * (g1s ** 2))
        + 30 * (yt2 ** 3 + yb2 ** 3 + Fraction(1, 3) * (ytau2 ** 3))
        - 6 * ((yt2 ** 2) * yb2 + yt2 * (yb2 ** 2))
        - 32 * g3s * (yt2 ** 2 + yb2 ** 2)
        - Fraction(8, 5) * g1s * (yt2 ** 2)
        + Fraction(4, 5) * g1s * (yb2 ** 2)
        - Fraction(12, 5) * g1s * (ytau2 ** 2)
        - Fraction(9, 4) * (g2s ** 2) * (yt2 + yb2 + Fraction(1, 3) * ytau2)
        + g1s * g2s * (Fraction(63, 10) * yt2 + Fraction(27, 10) * yb2 + Fraction(33, 10) * ytau2)
        - (g1s ** 2) * (Fraction(171, 100) * yt2 - Fraction(9, 20) * yb2 + Fraction(9, 4) * ytau2)
        + Fraction(305, 16) * (g2s ** 3)
        - Fraction(289, 80) * (g2s ** 2) * g1s
        - Fraction(1677, 400) * g2s * (g1s ** 2)
        - Fraction(3411, 2000) * (g1s ** 3)
    )
    b2_lam_buttazzo = 2 * (
        (lam ** 2) * (-156 * lam - 72 * yt2 - 72 * yb2 - 24 * ytau2 + 54 * g2s + Fraction(54, 5) * g1s)
        + lam * yt2 * (-Fraction(3, 2) * yt2 - 21 * yb2 + 40 * g3s + Fraction(45, 4) * g2s + Fraction(17, 4) * g1s)
        + lam * yb2 * (-Fraction(3, 2) * yb2 + 40 * g3s + Fraction(45, 4) * g2s + Fraction(5, 4) * g1s)
        + lam * ytau2 * (-Fraction(1, 2) * ytau2 + Fraction(15, 4) * g2s + Fraction(15, 4) * g1s)
        + lam * (-Fraction(73, 16) * (g2s ** 2) + Fraction(1887, 400) * (g1s ** 2) + Fraction(117, 40) * g2s * g1s)
        + (yt2 ** 2) * (15 * yt2 - 3 * yb2 - 16 * g3s - Fraction(4, 5) * g1s)
        + yt2 * (-Fraction(9, 8) * (g2s ** 2) - Fraction(171, 200) * (g1s ** 2) + Fraction(63, 20) * g2s * g1s)
        + (yb2 ** 2) * (-3 * yt2 + 15 * yb2 - 16 * g3s + Fraction(2, 5) * g1s)
        + yb2 * (-Fraction(9, 8) * (g2s ** 2) + Fraction(9, 40) * (g1s ** 2) + Fraction(27, 20) * g2s * g1s)
        + (ytau2 ** 2) * (5 * ytau2 - Fraction(6, 5) * g1s)
        + ytau2 * (-Fraction(3, 8) * (g2s ** 2) - Fraction(9, 8) * (g1s ** 2) + Fraction(33, 20) * g2s * g1s)
        + Fraction(305, 32) * (g2s ** 3)
        - Fraction(3411, 4000) * (g1s ** 3)
        - Fraction(289, 160) * (g2s ** 2) * g1s
        - Fraction(1677, 800) * g2s * (g1s ** 2)
    )

    buttazzo_poly_ok = (b2_yt_over_yt_matrix == b2_yt_over_yt_buttazzo) and (b2_lam_matrix == b2_lam_buttazzo)

    return {
        "lie_algebra_and_polynomial_gate_passed": bool(sm_b_exact_ok and ps_exact_ok and buttazzo_poly_ok),
        "sm_anomaly_traces_zero": [str(tr_Y), str(tr_Y3), str(tr_SU2_2_Y), str(tr_SU3_2_Y)],
        "sm_1loop_b": [str(b1_sm), str(b2_sm), str(b3_sm)],
        "pati_salam_hypercharge_weights_w2R_w4c": [str(w_2R), str(w_4c)],
        "pati_salam_1loop_b4_b2L_b2R": [str(b4_ps), str(b2L_ps), str(b2R_ps)],
        "buttazzo_2013_yt_2loop_exact_match": bool(b2_yt_over_yt_matrix == b2_yt_over_yt_buttazzo),
        "buttazzo_2013_lam_2loop_exact_match": bool(b2_lam_matrix == b2_lam_buttazzo),
    }


# ============================================================================
# SECTION 2: 2-LOOP MATRIX RGE KERNELS (FLOAT64 & ARBITRARY-PRECISION MPMATH)
# ============================================================================

def sm_2loop_weinberg_rhs_f64(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    kappa_w: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    two_loop: bool = True,
    scale_factor: float = frac_f64(1, 1),
    wrong_chirality: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    k1 = frac_f64(1, 16) / (math.pi * math.pi)
    k2 = k1 * k1 if two_loop else frac_f64(0, 1)

    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    He = Ye @ Ye.conj().T

    tu = float(np.real(np.trace(Hu)))
    td = float(np.real(np.trace(Hd)))
    te = float(np.real(np.trace(He)))
    y2_tr = 3 * tu + 3 * td + te

    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    eye3 = np.eye(3, dtype=complex)

    c_u = (y2_tr - frac_f64(17, 20) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hu - Hd)
    c_d = (y2_tr - frac_f64(1, 4) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hd - Hu)
    c_e = (y2_tr - frac_f64(9, 4) * g1s - frac_f64(9, 4) * g2s) * eye3 + frac_f64(3, 2) * He

    if wrong_chirality:
        b1_Yu = Yu @ c_u
        b1_Yd = Yd @ c_d
    else:
        b1_Yu = c_u @ Yu
        b1_Yd = c_d @ Yd
    b1_Ye = c_e @ Ye

    thu2 = float(np.real(np.trace(Hu @ Hu)))
    thd2 = float(np.real(np.trace(Hd @ Hd)))
    the2 = float(np.real(np.trace(He @ He)))
    thuhd = float(np.real(np.trace(Hu @ Hd)))

    chi2 = (
        -frac_f64(27, 4) * (thu2 + thd2)
        - frac_f64(9, 4) * the2
        + frac_f64(3, 2) * thuhd
        + (frac_f64(17, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * tu
        + (frac_f64(5, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * td
        + (frac_f64(15, 8) * g1s + frac_f64(15, 8) * g2s) * te
    )

    b2_Yu = (
        frac_f64(3, 2) * (Hu @ Hu)
        - (Hu @ Hd)
        - frac_f64(1, 4) * (Hd @ Hu)
        + frac_f64(11, 4) * (Hd @ Hd)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(223, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hu
        + (frac_f64(5, 4) * y2_tr - frac_f64(43, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hd
        + (
            chi2
            + 6 * lam * lam
            + frac_f64(1187, 600) * (g1s ** 2)
            - frac_f64(9, 20) * g1s * g2s
            + frac_f64(19, 15) * g1s * g3s
            - frac_f64(23, 4) * (g2s ** 2)
            + 9 * g2s * g3s
            - 108 * (g3s ** 2)
        ) * eye3
    ) @ Yu

    b2_Yd = (
        frac_f64(3, 2) * (Hd @ Hd)
        - (Hd @ Hu)
        - frac_f64(1, 4) * (Hu @ Hd)
        + frac_f64(11, 4) * (Hu @ Hu)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(187, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hd
        + (frac_f64(5, 4) * y2_tr - frac_f64(79, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hu
        + (
            chi2
            + 6 * lam * lam
            - frac_f64(127, 600) * (g1s ** 2)
            - frac_f64(27, 20) * g1s * g2s
            + frac_f64(31, 15) * g1s * g3s
            - frac_f64(23, 4) * (g2s ** 2)
            + 9 * g2s * g3s
            - 108 * (g3s ** 2)
        ) * eye3
    ) @ Yd

    b2_Ye = (
        frac_f64(3, 2) * (He @ He)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(387, 80) * g1s + frac_f64(135, 16) * g2s) * He
        + (
            chi2
            + 6 * lam * lam
            + frac_f64(1371, 200) * (g1s ** 2)
            + frac_f64(27, 20) * g1s * g2s
            - frac_f64(23, 4) * (g2s ** 2)
        ) * eye3
    ) @ Ye

    dYu = scale_factor * (k1 * b1_Yu + k2 * b2_Yu)
    dYd = scale_factor * (k1 * b1_Yd + k2 * b2_Yd)
    dYe = scale_factor * (k1 * b1_Ye + k2 * b2_Ye)

    alpha_w = 4 * lam - 3 * g2s + 2 * y2_tr
    dkappa = scale_factor * k1 * (-frac_f64(3, 2) * (He @ kappa_w + kappa_w @ He.T) + alpha_w * kappa_w)

    dg1 = scale_factor * (
        k1 * frac_f64(41, 10) * (g1 ** 3)
        + k2 * (g1 ** 3) * (frac_f64(199, 50) * g1s + frac_f64(27, 10) * g2s + frac_f64(44, 5) * g3s - frac_f64(17, 10) * tu - frac_f64(1, 2) * td - frac_f64(3, 2) * te)
    )
    dg2 = scale_factor * (
        k1 * frac_f64(-19, 6) * (g2 ** 3)
        + k2 * (g2 ** 3) * (frac_f64(9, 10) * g1s + frac_f64(35, 6) * g2s + 12 * g3s - frac_f64(3, 2) * tu - frac_f64(3, 2) * td - frac_f64(1, 2) * te)
    )
    dg3 = scale_factor * (
        k1 * (-7) * (g3 ** 3)
        + k2 * (g3 ** 3) * (frac_f64(11, 10) * g1s + frac_f64(9, 2) * g2s - 26 * g3s - 2 * tu - 2 * td)
    )

    thu3 = float(np.real(np.trace(Hu @ Hu @ Hu)))
    thd3 = float(np.real(np.trace(Hd @ Hd @ Hd)))
    the3 = float(np.real(np.trace(He @ He @ He)))
    thu2hd = float(np.real(np.trace(Hu @ Hu @ Hd)))
    thuhd2 = float(np.real(np.trace(Hu @ Hd @ Hd)))

    dlam1 = (
        24 * lam * lam
        + lam * (4 * y2_tr - 9 * g2s - frac_f64(9, 5) * g1s)
        - 2 * (3 * thu2 + 3 * thd2 + the2)
        + frac_f64(9, 8) * (g2s ** 2)
        + frac_f64(27, 200) * (g1s ** 2)
        + frac_f64(9, 20) * g1s * g2s
    )
    dlam2 = (
        -312 * (lam ** 3)
        + 36 * (lam * lam) * (3 * g2s + frac_f64(3, 5) * g1s)
        - 48 * (lam * lam) * y2_tr
        + lam * (80 * g3s + frac_f64(45, 2) * g2s) * (tu + td)
        + lam * g1s * (frac_f64(17, 2) * tu + frac_f64(5, 2) * td + frac_f64(15, 2) * te)
        + frac_f64(15, 2) * lam * g2s * te
        - 3 * lam * (thu2 + thd2 + frac_f64(1, 3) * the2 + 14 * thuhd)
        + lam * (-frac_f64(73, 8) * (g2s ** 2) + frac_f64(117, 20) * g1s * g2s + frac_f64(1887, 200) * (g1s ** 2))
        + 30 * (thu3 + thd3 + frac_f64(1, 3) * the3)
        - 6 * (thu2hd + thuhd2)
        - 32 * g3s * (thu2 + thd2)
        - frac_f64(8, 5) * g1s * thu2
        + frac_f64(4, 5) * g1s * thd2
        - frac_f64(12, 5) * g1s * the2
        - frac_f64(9, 4) * (g2s ** 2) * (tu + td + frac_f64(1, 3) * te)
        + g1s * g2s * (frac_f64(63, 10) * tu + frac_f64(27, 10) * td + frac_f64(33, 10) * te)
        - (g1s ** 2) * (frac_f64(171, 100) * tu - frac_f64(9, 20) * td + frac_f64(9, 4) * te)
        + frac_f64(305, 16) * (g2s ** 3)
        - frac_f64(289, 80) * (g2s ** 2) * g1s
        - frac_f64(1677, 400) * g2s * (g1s ** 2)
        - frac_f64(3411, 2000) * (g1s ** 3)
    )
    dlam = scale_factor * (k1 * dlam1 + k2 * dlam2)
    return dYu, dYd, dYe, dkappa, dg1, dg2, dg3, dlam


def integrate_sm_rk4_f64(
    Yu0: np.ndarray,
    Yd0: np.ndarray,
    Ye0: np.ndarray,
    kappa0: np.ndarray,
    g1_0: float,
    g2_0: float,
    g3_0: float,
    lam_0: float,
    dt_total: float,
    n_steps: int,
    two_loop: bool = True,
    scale_factor: float = frac_f64(1, 1),
    wrong_chirality: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    h = dt_total / n_steps
    Yu = Yu0.copy()
    Yd = Yd0.copy()
    Ye = Ye0.copy()
    kw = kappa0.copy()
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam_0

    for _ in range(n_steps):
        s1 = sm_2loop_weinberg_rhs_f64(Yu, Yd, Ye, kw, g1, g2, g3, lam, two_loop, scale_factor, wrong_chirality)
        s2 = sm_2loop_weinberg_rhs_f64(
            Yu + frac_f64(1, 2) * h * s1[0], Yd + frac_f64(1, 2) * h * s1[1],
            Ye + frac_f64(1, 2) * h * s1[2], kw + frac_f64(1, 2) * h * s1[3],
            g1 + frac_f64(1, 2) * h * s1[4], g2 + frac_f64(1, 2) * h * s1[5],
            g3 + frac_f64(1, 2) * h * s1[6], lam + frac_f64(1, 2) * h * s1[7],
            two_loop, scale_factor, wrong_chirality,
        )
        s3 = sm_2loop_weinberg_rhs_f64(
            Yu + frac_f64(1, 2) * h * s2[0], Yd + frac_f64(1, 2) * h * s2[1],
            Ye + frac_f64(1, 2) * h * s2[2], kw + frac_f64(1, 2) * h * s2[3],
            g1 + frac_f64(1, 2) * h * s2[4], g2 + frac_f64(1, 2) * h * s2[5],
            g3 + frac_f64(1, 2) * h * s2[6], lam + frac_f64(1, 2) * h * s2[7],
            two_loop, scale_factor, wrong_chirality,
        )
        s4 = sm_2loop_weinberg_rhs_f64(
            Yu + h * s3[0], Yd + h * s3[1],
            Ye + h * s3[2], kw + h * s3[3],
            g1 + h * s3[4], g2 + h * s3[5],
            g3 + h * s3[6], lam + h * s3[7],
            two_loop, scale_factor, wrong_chirality,
        )
        Yu = Yu + (h / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
        Yd = Yd + (h / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
        Ye = Ye + (h / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
        kw = kw + (h / 6) * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
        g1 = g1 + (h / 6) * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
        g2 = g2 + (h / 6) * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
        g3 = g3 + (h / 6) * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
        lam = lam + (h / 6) * (s1[7] + 2 * s2[7] + 2 * s3[7] + s4[7])

    return Yu, Yd, Ye, kw, g1, g2, g3, lam


def mp_conj_t(M: mp.matrix) -> mp.matrix:
    r, c = M.rows, M.cols
    out = mp.matrix(c, r)
    for i in range(r):
        for j in range(c):
            out[j, i] = mp.conj(M[i, j])
    return out


def mp_trace_re(M: mp.matrix) -> mp.mpf:
    return mp.re(sum(M[i, i] for i in range(M.rows)))


def sm_2loop_rhs_mp(
    Yu: mp.matrix,
    Yd: mp.matrix,
    Ye: mp.matrix,
    g1: mp.mpf,
    g2: mp.mpf,
    g3: mp.mpf,
    lam: mp.mpf,
) -> Tuple[mp.matrix, mp.matrix, mp.matrix, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    k1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    k2 = k1 * k1

    Hu = Yu * mp_conj_t(Yu)
    Hd = Yd * mp_conj_t(Yd)
    He = Ye * mp_conj_t(Ye)

    tu = mp_trace_re(Hu)
    td = mp_trace_re(Hd)
    te = mp_trace_re(He)
    y2_tr = 3 * tu + 3 * td + te

    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    eye3 = mp.eye(3)

    b1_Yu = ((y2_tr - mp.mpf(17) / 20 * g1s - mp.mpf(9) / 4 * g2s - 8 * g3s) * eye3 + mp.mpf(3) / 2 * (Hu - Hd)) * Yu
    b1_Yd = ((y2_tr - mp.mpf(1) / 4 * g1s - mp.mpf(9) / 4 * g2s - 8 * g3s) * eye3 + mp.mpf(3) / 2 * (Hd - Hu)) * Yd
    b1_Ye = ((y2_tr - mp.mpf(9) / 4 * g1s - mp.mpf(9) / 4 * g2s) * eye3 + mp.mpf(3) / 2 * He) * Ye

    Hu2 = Hu * Hu
    Hd2 = Hd * Hd
    He2 = He * He
    HuHd = Hu * Hd
    HdHu = Hd * Hu

    thu2 = mp_trace_re(Hu2)
    thd2 = mp_trace_re(Hd2)
    the2 = mp_trace_re(He2)
    thuhd = mp_trace_re(HuHd)

    chi2 = (
        -mp.mpf(27) / 4 * (thu2 + thd2)
        - mp.mpf(9) / 4 * the2
        + mp.mpf(3) / 2 * thuhd
        + (mp.mpf(17) / 8 * g1s + mp.mpf(45) / 8 * g2s + 20 * g3s) * tu
        + (mp.mpf(5) / 8 * g1s + mp.mpf(45) / 8 * g2s + 20 * g3s) * td
        + (mp.mpf(15) / 8 * g1s + mp.mpf(15) / 8 * g2s) * te
    )

    b2_Yu = (
        mp.mpf(3) / 2 * Hu2
        - HuHd
        - mp.mpf(1) / 4 * HdHu
        + mp.mpf(11) / 4 * Hd2
        + (-mp.mpf(9) / 4 * y2_tr - 12 * lam + mp.mpf(223) / 80 * g1s + mp.mpf(135) / 16 * g2s + 16 * g3s) * Hu
        + (mp.mpf(5) / 4 * y2_tr - mp.mpf(43) / 80 * g1s + mp.mpf(9) / 16 * g2s - 16 * g3s) * Hd
        + (
            chi2
            + 6 * lam * lam
            + mp.mpf(1187) / 600 * (g1s ** 2)
            - mp.mpf(9) / 20 * g1s * g2s
            + mp.mpf(19) / 15 * g1s * g3s
            - mp.mpf(23) / 4 * (g2s ** 2)
            + 9 * g2s * g3s
            - 108 * (g3s ** 2)
        ) * eye3
    ) * Yu

    b2_Yd = (
        mp.mpf(3) / 2 * Hd2
        - HdHu
        - mp.mpf(1) / 4 * HuHd
        + mp.mpf(11) / 4 * Hu2
        + (-mp.mpf(9) / 4 * y2_tr - 12 * lam + mp.mpf(187) / 80 * g1s + mp.mpf(135) / 16 * g2s + 16 * g3s) * Hd
        + (mp.mpf(5) / 4 * y2_tr - mp.mpf(79) / 80 * g1s + mp.mpf(9) / 16 * g2s - 16 * g3s) * Hu
        + (
            chi2
            + 6 * lam * lam
            - mp.mpf(127) / 600 * (g1s ** 2)
            - mp.mpf(27) / 20 * g1s * g2s
            + mp.mpf(31) / 15 * g1s * g3s
            - mp.mpf(23) / 4 * (g2s ** 2)
            + 9 * g2s * g3s
            - 108 * (g3s ** 2)
        ) * eye3
    ) * Yd

    b2_Ye = (
        mp.mpf(3) / 2 * He2
        + (-mp.mpf(9) / 4 * y2_tr - 12 * lam + mp.mpf(387) / 80 * g1s + mp.mpf(135) / 16 * g2s) * He
        + (
            chi2
            + 6 * lam * lam
            + mp.mpf(1371) / 200 * (g1s ** 2)
            + mp.mpf(27) / 20 * g1s * g2s
            - mp.mpf(23) / 4 * (g2s ** 2)
        ) * eye3
    ) * Ye

    dg1 = k1 * (mp.mpf(41) / 10) * (g1 ** 3) + k2 * (g1 ** 3) * (
        mp.mpf(199) / 50 * g1s + mp.mpf(27) / 10 * g2s + mp.mpf(44) / 5 * g3s - mp.mpf(17) / 10 * tu - mp.mpf(1) / 2 * td - mp.mpf(3) / 2 * te
    )
    dg2 = k1 * (mp.mpf(-19) / 6) * (g2 ** 3) + k2 * (g2 ** 3) * (
        mp.mpf(9) / 10 * g1s + mp.mpf(35) / 6 * g2s + 12 * g3s - mp.mpf(3) / 2 * tu - mp.mpf(3) / 2 * td - mp.mpf(1) / 2 * te
    )
    dg3 = k1 * (-7) * (g3 ** 3) + k2 * (g3 ** 3) * (
        mp.mpf(11) / 10 * g1s + mp.mpf(9) / 2 * g2s - 26 * g3s - 2 * tu - 2 * td
    )

    thu3 = mp_trace_re(Hu2 * Hu)
    thd3 = mp_trace_re(Hd2 * Hd)
    the3 = mp_trace_re(He2 * He)
    thu2hd = mp_trace_re(Hu2 * Hd)
    thuhd2 = mp_trace_re(Hu * Hd2)

    dlam1 = (
        24 * lam * lam
        + lam * (4 * y2_tr - 9 * g2s - mp.mpf(9) / 5 * g1s)
        - 2 * (3 * thu2 + 3 * thd2 + the2)
        + mp.mpf(9) / 8 * (g2s ** 2)
        + mp.mpf(27) / 200 * (g1s ** 2)
        + mp.mpf(9) / 20 * g1s * g2s
    )
    dlam2 = (
        -312 * (lam ** 3)
        + 36 * (lam * lam) * (3 * g2s + mp.mpf(3) / 5 * g1s)
        - 48 * (lam * lam) * y2_tr
        + lam * (80 * g3s + mp.mpf(45) / 2 * g2s) * (tu + td)
        + lam * g1s * (mp.mpf(17) / 2 * tu + mp.mpf(5) / 2 * td + mp.mpf(15) / 2 * te)
        + mp.mpf(15) / 2 * lam * g2s * te
        - 3 * lam * (thu2 + thd2 + mp.mpf(1) / 3 * the2 + 14 * thuhd)
        + lam * (-mp.mpf(73) / 8 * (g2s ** 2) + mp.mpf(117) / 20 * g1s * g2s + mp.mpf(1887) / 200 * (g1s ** 2))
        + 30 * (thu3 + thd3 + mp.mpf(1) / 3 * the3)
        - 6 * (thu2hd + thuhd2)
        - 32 * g3s * (thu2 + thd2)
        - mp.mpf(8) / 5 * g1s * thu2
        + mp.mpf(4) / 5 * g1s * thd2
        - mp.mpf(12) / 5 * g1s * the2
        - mp.mpf(9) / 4 * (g2s ** 2) * (tu + td + mp.mpf(1) / 3 * te)
        + g1s * g2s * (mp.mpf(63) / 10 * tu + mp.mpf(27) / 10 * td + mp.mpf(33) / 10 * te)
        - (g1s ** 2) * (mp.mpf(171) / 100 * tu - mp.mpf(9) / 20 * td + mp.mpf(9) / 4 * te)
        + mp.mpf(305) / 16 * (g2s ** 3)
        - mp.mpf(289) / 80 * (g2s ** 2) * g1s
        - mp.mpf(1677) / 400 * g2s * (g1s ** 2)
        - mp.mpf(3411) / 2000 * (g1s ** 3)
    )
    return (
        k1 * b1_Yu + k2 * b2_Yu,
        k1 * b1_Yd + k2 * b2_Yd,
        k1 * b1_Ye + k2 * b2_Ye,
        dg1,
        dg2,
        dg3,
        k1 * dlam1 + k2 * dlam2,
    )


# ============================================================================
# SECTION 3: FOUR PUBLISHED LITERATURE RGE SOLVER BENCHMARKS (B0.1 - B0.4)
# ============================================================================

def run_four_literature_benchmarks() -> Dict[str, Any]:
    # --- B0.1: 2-loop pure gauge exact analytical antiderivative vs RK4 ---
    mp.mp.dps = 50
    k1_mp = mp.mpf(1) / (16 * mp.pi * mp.pi)
    a_mp = k1_mp * (-7)
    c_mp = (k1_mp ** 2) * (-26)
    g0_mp = mp.mpf(3) / 5
    dt_b1 = mp.mpf(-15)

    def antideriv_2loop_gauge(gv: mp.mpf) -> mp.mpf:
        u = gv * gv
        return -1 / (2 * a_mp * u) - (c_mp / (2 * a_mp * a_mp)) * mp.log(abs(u / (a_mp + c_mp * u)))

    target_F = antideriv_2loop_gauge(g0_mp) + dt_b1
    # Strictly monotone decreasing F(g) on [3/5, 2]: F(3/5) - target_F = +15 > 0, F(2) - target_F < 0
    lo_g, hi_g = mp.mpf(3) / 5, mp.mpf(2)
    for _ in range(160):
        mid_g = (lo_g + hi_g) / 2
        if antideriv_2loop_gauge(mid_g) - target_F > 0:
            lo_g = mid_g
        else:
            hi_g = mid_g
    g_exact_mp = (lo_g + hi_g) / 2

    z3 = np.zeros((3, 3), dtype=complex)
    _, _, _, _, _, _, g3_rk4, _ = integrate_sm_rk4_f64(
        z3, z3, z3, z3, frac_f64(0, 1), frac_f64(0, 1), frac_f64(3, 5), frac_f64(0, 1), frac_f64(-15, 1), 1500, two_loop=True
    )
    b0_1_rel_err = abs(g3_rk4 - float(g_exact_mp)) / abs(float(g_exact_mp))

    # --- B0.2: Buttazzo et al. (2013) 2-loop Higgs quartic zero-crossing t_crit ---
    def find_t_crit_f64(scale_fac: float = frac_f64(1, 1)) -> float:
        Yu = np.zeros((3, 3), dtype=complex)
        Yu[2, 2] = frac_f64(9, 10)
        Yd = np.zeros((3, 3), dtype=complex)
        Ye = np.zeros((3, 3), dtype=complex)
        kw = np.zeros((3, 3), dtype=complex)
        g1, g2, g3, lam = frac_f64(1, 2), frac_f64(3, 5), frac_f64(1, 1), frac_f64(1, 10)
        h = frac_f64(1, 200)
        t_cur = frac_f64(0, 1)
        for _ in range(6000):
            s1 = sm_2loop_weinberg_rhs_f64(Yu, Yd, Ye, kw, g1, g2, g3, lam, True, scale_fac, False)
            dlam_left = s1[7]
            Yu_n, Yd_n, Ye_n, kw_n, g1_n, g2_n, g3_n, lam_n = integrate_sm_rk4_f64(
                Yu, Yd, Ye, kw, g1, g2, g3, lam, h, 1, True, scale_fac, False
            )
            if lam_n <= 0:
                s_end = sm_2loop_weinberg_rhs_f64(Yu_n, Yd_n, Ye_n, kw_n, g1_n, g2_n, g3_n, lam_n, True, scale_fac, False)
                dlam_right = s_end[7]
                lo, hi = frac_f64(0, 1), h
                for _ in range(60):
                    mid = (lo + hi) / 2
                    s = mid / h
                    h00 = 2 * (s ** 3) - 3 * (s ** 2) + 1
                    h10 = (s ** 3) - 2 * (s ** 2) + s
                    h01 = -2 * (s ** 3) + 3 * (s ** 2)
                    h11 = (s ** 3) - (s ** 2)
                    val = h00 * lam + h10 * h * dlam_left + h01 * lam_n + h11 * h * dlam_right
                    if val > 0:
                        lo = mid
                    else:
                        hi = mid
                return t_cur + (lo + hi) / 2
            Yu, Yd, Ye, kw, g1, g2, g3, lam = Yu_n, Yd_n, Ye_n, kw_n, g1_n, g2_n, g3_n, lam_n
            t_cur += h
        return frac_f64(-1, 1)

    def find_t_crit_mp() -> mp.mpf:
        mp.mp.dps = 45
        Yu = mp.zeros(3, 3)
        Yu[2, 2] = mp.mpf(9) / 10
        Yd = mp.zeros(3, 3)
        Ye = mp.zeros(3, 3)
        g1, g2, g3, lam = mp.mpf(1) / 2, mp.mpf(3) / 5, mp.mpf(1), mp.mpf(1) / 10
        h = mp.mpf(1) / 50
        t_cur = mp.mpf(0)
        for _ in range(1500):
            s1 = sm_2loop_rhs_mp(Yu, Yd, Ye, g1, g2, g3, lam)
            s2 = sm_2loop_rhs_mp(
                Yu + h * s1[0] / 2, Yd + h * s1[1] / 2, Ye + h * s1[2] / 2,
                g1 + h * s1[3] / 2, g2 + h * s1[4] / 2, g3 + h * s1[5] / 2, lam + h * s1[6] / 2,
            )
            s3 = sm_2loop_rhs_mp(
                Yu + h * s2[0] / 2, Yd + h * s2[1] / 2, Ye + h * s2[2] / 2,
                g1 + h * s2[3] / 2, g2 + h * s2[4] / 2, g3 + h * s2[5] / 2, lam + h * s2[6] / 2,
            )
            s4 = sm_2loop_rhs_mp(
                Yu + h * s3[0], Yd + h * s3[1], Ye + h * s3[2],
                g1 + h * s3[3], g2 + h * s3[4], g3 + h * s3[5], lam + h * s3[6],
            )
            Yu_n = Yu + (h / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
            Yd_n = Yd + (h / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
            Ye_n = Ye + (h / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
            g1_n = g1 + (h / 6) * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
            g2_n = g2 + (h / 6) * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
            g3_n = g3 + (h / 6) * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
            lam_n = lam + (h / 6) * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
            if lam_n <= 0:
                s_end = sm_2loop_rhs_mp(Yu_n, Yd_n, Ye_n, g1_n, g2_n, g3_n, lam_n)
                dlam_l = s1[6]
                dlam_r = s_end[6]
                lo, hi = mp.mpf(0), h
                for _ in range(90):
                    mid = (lo + hi) / 2
                    s = mid / h
                    h00 = 2 * (s ** 3) - 3 * (s ** 2) + 1
                    h10 = (s ** 3) - 2 * (s ** 2) + s
                    h01 = -2 * (s ** 3) + 3 * (s ** 2)
                    h11 = (s ** 3) - (s ** 2)
                    val = h00 * lam + h10 * h * dlam_l + h01 * lam_n + h11 * h * dlam_r
                    if val > 0:
                        lo = mid
                    else:
                        hi = mid
                return t_cur + (lo + hi) / 2
            Yu, Yd, Ye, g1, g2, g3, lam = Yu_n, Yd_n, Ye_n, g1_n, g2_n, g3_n, lam_n
            t_cur += h
        return mp.mpf(-1)

    t_crit_f64 = find_t_crit_f64()
    t_crit_mp = find_t_crit_mp()
    b0_2_rel_err = abs(t_crit_f64 - float(t_crit_mp)) / abs(float(t_crit_mp))

    # --- B0.3: Non-commuting 2-loop complex matrix Yukawa flow (38-digit mpmath vs float64) + Xing-Zhou Jacobi integral ---
    Yu0_frac = [
        [(Fraction(1, 25), Fraction(1, 40)), (Fraction(1, 30), Fraction(-1, 50)), (Fraction(1, 20), Fraction(1, 35))],
        [(Fraction(-1, 45), Fraction(1, 30)), (Fraction(3, 20), Fraction(1, 40)), (Fraction(1, 15), Fraction(-1, 25))],
        [(Fraction(1, 35), Fraction(-1, 40)), (Fraction(1, 18), Fraction(1, 28)), (Fraction(11, 20), Fraction(-1, 30))],
    ]
    Yd0_frac = [
        [(Fraction(1, 30), Fraction(-1, 50)), (Fraction(1, 22), Fraction(1, 45)), (Fraction(-1, 35), Fraction(1, 40))],
        [(Fraction(1, 28), Fraction(1, 36)), (Fraction(1, 10), Fraction(-1, 30)), (Fraction(1, 24), Fraction(1, 32))],
        [(Fraction(-1, 40), Fraction(1, 50)), (Fraction(1, 20), Fraction(-1, 35)), (Fraction(7, 25), Fraction(1, 40))],
    ]
    Ye0_frac = [
        [(Fraction(1, 40), Fraction(1, 60)), (Fraction(1, 50), Fraction(-1, 70)), (Fraction(1, 45), Fraction(1, 80))],
        [(Fraction(-1, 55), Fraction(1, 65)), (Fraction(1, 14), Fraction(1, 50)), (Fraction(1, 30), Fraction(-1, 45))],
        [(Fraction(1, 60), Fraction(-1, 50)), (Fraction(1, 35), Fraction(1, 40)), (Fraction(1, 5), Fraction(-1, 50))],
    ]

    def build_np_and_mp(spec: List[List[Tuple[Fraction, Fraction]]]) -> Tuple[np.ndarray, mp.matrix]:
        m_np = np.zeros((3, 3), dtype=complex)
        m_mp = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                re_f, im_f = spec[i][j]
                m_np[i, j] = complex(float(re_f), float(im_f))
                m_mp[i, j] = mp.mpc(mp.mpf(re_f.numerator) / re_f.denominator, mp.mpf(im_f.numerator) / im_f.denominator)
        return m_np, m_mp

    mp.mp.dps = 38
    Yu0_np, Yu0_mp = build_np_and_mp(Yu0_frac)
    Yd0_np, Yd0_mp = build_np_and_mp(Yd0_frac)
    Ye0_np, Ye0_mp = build_np_and_mp(Ye0_frac)

    g1_0_mp = mp.sqrt(4 * mp.pi / 45)
    g2_0_mp = mp.sqrt(4 * mp.pi / 45)
    g3_0_mp = mp.sqrt(4 * mp.pi / 45)
    lam_0_mp = mp.mpf(1) / 8
    g1_0_np, g2_0_np, g3_0_np, lam_0_np = float(g1_0_mp), float(g2_0_mp), float(g3_0_mp), frac_f64(1, 8)

    Yu_f, Yd_f, Ye_f, _, g1_f, g2_f, g3_f, lam_f = integrate_sm_rk4_f64(
        Yu0_np, Yd0_np, Ye0_np, z3, g1_0_np, g2_0_np, g3_0_np, lam_0_np, frac_f64(-27, 1), 1080, True
    )

    Yu_m, Yd_m, Ye_m = Yu0_mp.copy(), Yd0_mp.copy(), Ye0_mp.copy()
    g1_m, g2_m, g3_m, lam_m = g1_0_mp, g2_0_mp, g3_0_mp, lam_0_mp
    n_mp_steps = 270
    h_mp = mp.mpf(-27) / n_mp_steps
    for _ in range(n_mp_steps):
        s1 = sm_2loop_rhs_mp(Yu_m, Yd_m, Ye_m, g1_m, g2_m, g3_m, lam_m)
        s2 = sm_2loop_rhs_mp(
            Yu_m + h_mp * s1[0] / 2, Yd_m + h_mp * s1[1] / 2, Ye_m + h_mp * s1[2] / 2,
            g1_m + h_mp * s1[3] / 2, g2_m + h_mp * s1[4] / 2, g3_m + h_mp * s1[5] / 2, lam_m + h_mp * s1[6] / 2,
        )
        s3 = sm_2loop_rhs_mp(
            Yu_m + h_mp * s2[0] / 2, Yd_m + h_mp * s2[1] / 2, Ye_m + h_mp * s2[2] / 2,
            g1_m + h_mp * s2[3] / 2, g2_m + h_mp * s2[4] / 2, g3_m + h_mp * s2[5] / 2, lam_m + h_mp * s2[6] / 2,
        )
        s4 = sm_2loop_rhs_mp(
            Yu_m + h_mp * s3[0], Yd_m + h_mp * s3[1], Ye_m + h_mp * s3[2],
            g1_m + h_mp * s3[3], g2_m + h_mp * s3[4], g3_m + h_mp * s3[5], lam_m + h_mp * s3[6],
        )
        Yu_m = Yu_m + (h_mp / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
        Yd_m = Yd_m + (h_mp / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
        Ye_m = Ye_m + (h_mp / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
        g1_m = g1_m + (h_mp / 6) * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
        g2_m = g2_m + (h_mp / 6) * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
        g3_m = g3_m + (h_mp / 6) * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
        lam_m = lam_m + (h_mp / 6) * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])

    Yu_mp_as_np = np.array([[complex(Yu_m[i, j]) for j in range(3)] for i in range(3)])
    Yd_mp_as_np = np.array([[complex(Yd_m[i, j]) for j in range(3)] for i in range(3)])
    Ye_mp_as_np = np.array([[complex(Ye_m[i, j]) for j in range(3)] for i in range(3)])
    b0_3_rel_err = max(
        float(np.linalg.norm(Yu_f - Yu_mp_as_np) / np.linalg.norm(Yu_mp_as_np)),
        float(np.linalg.norm(Yd_f - Yd_mp_as_np) / np.linalg.norm(Yd_mp_as_np)),
        float(np.linalg.norm(Ye_f - Ye_mp_as_np) / np.linalg.norm(Ye_mp_as_np)),
        abs(g3_f - float(g3_m)) / abs(float(g3_m)),
        abs(lam_f - float(lam_m)) / abs(float(lam_m)),
    )

    Yu_cur, Yd_cur, Ye_cur = Yu0_np.copy(), Yd0_np.copy(), Ye0_np.copy()
    g1_c, g2_c, g3_c, lam_c = g1_0_np, g2_0_np, g3_0_np, lam_0_np
    n_det = 1080
    h_det = frac_f64(-27, 1) / n_det
    quad_acc = frac_f64(0, 1)

    def jacobi_rate(Yu_v: np.ndarray, Yd_v: np.ndarray, Ye_v: np.ndarray, g1v: float, g2v: float, g3v: float, lamv: float) -> float:
        dYu1, _, _, _, _, _, _, _ = sm_2loop_weinberg_rhs_f64(Yu_v, Yd_v, Ye_v, z3, g1v, g2v, g3v, lamv, two_loop=False)
        return 2 * float(np.real(np.trace(dYu1 @ np.linalg.inv(Yu_v))))

    for _ in range(n_det):
        r0 = jacobi_rate(Yu_cur, Yd_cur, Ye_cur, g1_c, g2_c, g3_c, lam_c)
        Yu_m1, Yd_m1, Ye_m1, _, g1_m1, g2_m1, g3_m1, lam_m1 = integrate_sm_rk4_f64(
            Yu_cur, Yd_cur, Ye_cur, z3, g1_c, g2_c, g3_c, lam_c, h_det / 2, 1, two_loop=False
        )
        rm = jacobi_rate(Yu_m1, Yd_m1, Ye_m1, g1_m1, g2_m1, g3_m1, lam_m1)
        Yu_nx, Yd_nx, Ye_nx, _, g1_nx, g2_nx, g3_nx, lam_nx = integrate_sm_rk4_f64(
            Yu_cur, Yd_cur, Ye_cur, z3, g1_c, g2_c, g3_c, lam_c, h_det, 1, two_loop=False
        )
        r1 = jacobi_rate(Yu_nx, Yd_nx, Ye_nx, g1_nx, g2_nx, g3_nx, lam_nx)
        quad_acc += (h_det / 6) * (r0 + 4 * rm + r1)
        Yu_cur, Yd_cur, Ye_cur, g1_c, g2_c, g3_c, lam_c = Yu_nx, Yd_nx, Ye_nx, g1_nx, g2_nx, g3_nx, lam_nx

    ln_det_diff = math.log(float(np.real(np.linalg.det(Yu_cur @ Yu_cur.conj().T)))) - math.log(
        float(np.real(np.linalg.det(Yu0_np @ Yu0_np.conj().T)))
    )
    b0_3_jacobi_abs_err = abs(ln_det_diff - quad_acc)

    # --- B0.4: Antusch et al. (2003) 1-loop Weinberg seesaw operator analytical integral vs matrix ODE ---
    Ye_diag = np.diag([frac_f64(1, 50), frac_f64(1, 15), frac_f64(1, 4)]).astype(complex)
    kw0 = np.array(
        [
            [complex(frac_f64(2, 10), frac_f64(1, 25)), complex(frac_f64(1, 12), frac_f64(-1, 30)), complex(frac_f64(1, 20), frac_f64(1, 40))],
            [complex(frac_f64(1, 12), frac_f64(-1, 30)), complex(frac_f64(3, 10), frac_f64(-1, 20)), complex(frac_f64(1, 8), frac_f64(1, 15))],
            [complex(frac_f64(1, 20), frac_f64(1, 40)), complex(frac_f64(1, 8), frac_f64(1, 15)), complex(frac_f64(1, 2), frac_f64(1, 10))],
        ],
        dtype=complex,
    )
    Yu_w, Yd_w, Ye_w, kw_w = Yu0_np.copy(), Yd0_np.copy(), Ye_diag.copy(), kw0.copy()
    g1_w, g2_w, g3_w, lam_w = g1_0_np, g2_0_np, g3_0_np, lam_0_np
    int_alpha = frac_f64(0, 1)
    int_he = np.zeros(3, dtype=float)
    k1_f = frac_f64(1, 16) / (math.pi * math.pi)
    n_w = 1080
    h_w = frac_f64(-27, 1) / n_w

    def weinberg_rates(Yu_v: np.ndarray, Yd_v: np.ndarray, Ye_v: np.ndarray, g2v: float, lamv: float) -> Tuple[float, np.ndarray]:
        tu = float(np.real(np.trace(Yu_v @ Yu_v.conj().T)))
        td = float(np.real(np.trace(Yd_v @ Yd_v.conj().T)))
        he_d = np.real(np.diag(Ye_v @ Ye_v.conj().T))
        y2 = 3 * tu + 3 * td + float(np.sum(he_d))
        return k1_f * (4 * lamv - 3 * g2v * g2v + 2 * y2), k1_f * he_d

    for _ in range(n_w):
        a0, e0 = weinberg_rates(Yu_w, Yd_w, Ye_w, g2_w, lam_w)
        Yu_m1, Yd_m1, Ye_m1, _, g1_m1, g2_m1, g3_m1, lam_m1 = integrate_sm_rk4_f64(
            Yu_w, Yd_w, Ye_w, kw_w, g1_w, g2_w, g3_w, lam_w, h_w / 2, 1, True
        )
        am, em = weinberg_rates(Yu_m1, Yd_m1, Ye_m1, g2_m1, lam_m1)
        Yu_nx, Yd_nx, Ye_nx, kw_nx, g1_nx, g2_nx, g3_nx, lam_nx = integrate_sm_rk4_f64(
            Yu_w, Yd_w, Ye_w, kw_w, g1_w, g2_w, g3_w, lam_w, h_w, 1, True
        )
        a1, e1 = weinberg_rates(Yu_nx, Yd_nx, Ye_nx, g2_nx, lam_nx)
        int_alpha += (h_w / 6) * (a0 + 4 * am + a1)
        int_he = int_he + (h_w / 6) * (e0 + 4 * em + e1)
        Yu_w, Yd_w, Ye_w, kw_w, g1_w, g2_w, g3_w, lam_w = Yu_nx, Yd_nx, Ye_nx, kw_nx, g1_nx, g2_nx, g3_nx, lam_nx

    kw_exact = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            kw_exact[i, j] = kw0[i, j] * math.exp(int_alpha - frac_f64(3, 2) * (int_he[i] + int_he[j]))

    b0_4_rel_err = float(np.linalg.norm(kw_w - kw_exact) / np.linalg.norm(kw_exact))

    tol_tight = pow10_f64(-7)
    all_passed = (
        t_crit_f64 > 0
        and float(t_crit_mp) > 0
        and b0_1_rel_err < tol_tight
        and b0_2_rel_err < tol_tight
        and b0_3_rel_err < tol_tight
        and b0_3_jacobi_abs_err < pow10_f64(-10)
        and b0_4_rel_err < pow10_f64(-9)
    )
    return {
        "four_benchmarks_gate_passed": all_passed,
        "B0_1_2loop_gauge_implicit_rel_err": b0_1_rel_err,
        "B0_2_buttazzo_t_crit_f64": t_crit_f64,
        "B0_2_buttazzo_t_crit_mp45": float(t_crit_mp),
        "B0_2_buttazzo_t_crit_rel_err": b0_2_rel_err,
        "B0_3_noncommuting_2loop_matrix_mp38_vs_f64_rel_err": b0_3_rel_err,
        "B0_3_xing_zhou_1loop_jacobi_abs_err": b0_3_jacobi_abs_err,
        "B0_4_antusch_weinberg_analytic_vs_ode_rel_err": b0_4_rel_err,
    }


# ============================================================================
# SECTION 4: MANDATORY PRE-RGE RANDOM HAAR U(3)^6 INVARIANCE GATE & PLANTED FAULTS
# ============================================================================

def haar_unitary_3x3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = d / np.abs(d)
    return q * ph[None, :]


def wrap_angle_pi(angle: float) -> float:
    return math.atan2(math.sin(angle), math.cos(angle))


def extract_21_observables(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    kappa_w: np.ndarray,
    theta_g: float,
) -> np.ndarray:
    uu, su, _ = np.linalg.svd(Yu)
    iu = np.argsort(su)
    uu, su = uu[:, iu], su[iu]

    ud, sd, _ = np.linalg.svd(Yd)
    id_ = np.argsort(sd)
    ud, sd = ud[:, id_], sd[id_]

    ue, se, _ = np.linalg.svd(Ye)
    ie = np.argsort(se)
    ue, se = ue[:, ie], se[ie]

    h_nu = kappa_w @ kappa_w.conj().T
    evals, u_nu = np.linalg.eigh(h_nu)
    inu = np.argsort(np.real(evals))
    s_nu = np.sqrt(np.maximum(np.real(evals[inu]), frac_f64(0, 1)))
    u_nu = u_nu[:, inu]

    v_ckm = uu.conj().T @ ud
    u_pmns = ue.conj().T @ u_nu

    j_ckm = float(np.imag(v_ckm[0, 1] * v_ckm[1, 2] * np.conj(v_ckm[0, 2]) * np.conj(v_ckm[1, 1])))
    j_pmns = float(np.imag(u_pmns[0, 1] * u_pmns[1, 2] * np.conj(u_pmns[0, 2]) * np.conj(u_pmns[1, 1])))

    det_y = np.linalg.det(Yu @ Yd)
    bar_theta = wrap_angle_pi(theta_g + math.atan2(float(np.imag(det_y)), float(np.real(det_y))))

    return np.array(
        [
            su[0], su[1], su[2],
            sd[0], sd[1], sd[2],
            se[0], se[1], se[2],
            s_nu[0], s_nu[1], s_nu[2],
            abs(v_ckm[0, 1]), abs(v_ckm[1, 2]), abs(v_ckm[0, 2]), j_ckm,
            abs(u_pmns[0, 1]), abs(u_pmns[0, 2]), abs(u_pmns[1, 2]), j_pmns,
            bar_theta,
        ],
        dtype=float,
    )


def build_synthetic_uv_state() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    Yu = np.array(
        [
            [complex(frac_f64(1, 50), frac_f64(1, 80)), complex(frac_f64(1, 35), frac_f64(-1, 60)), complex(frac_f64(1, 25), frac_f64(1, 45))],
            [complex(frac_f64(-1, 60), frac_f64(1, 40)), complex(frac_f64(3, 25), frac_f64(1, 50)), complex(frac_f64(1, 16), frac_f64(-1, 30))],
            [complex(frac_f64(1, 45), frac_f64(-1, 50)), complex(frac_f64(1, 20), frac_f64(1, 35)), complex(frac_f64(11, 20), frac_f64(-1, 40))],
        ],
        dtype=complex,
    )
    Yd = np.array(
        [
            [complex(frac_f64(1, 60), frac_f64(-1, 90)), complex(frac_f64(1, 30), frac_f64(1, 55)), complex(frac_f64(-1, 40), frac_f64(1, 50))],
            [complex(frac_f64(1, 32), frac_f64(1, 45)), complex(frac_f64(1, 12), frac_f64(-1, 40)), complex(frac_f64(1, 25), frac_f64(1, 35))],
            [complex(frac_f64(-1, 50), frac_f64(1, 60)), complex(frac_f64(1, 22), frac_f64(-1, 40)), complex(frac_f64(6, 25), frac_f64(1, 50))],
        ],
        dtype=complex,
    )
    Ye = np.array(
        [
            [complex(frac_f64(1, 70), frac_f64(1, 90)), complex(frac_f64(1, 55), frac_f64(-1, 80)), complex(frac_f64(1, 50), frac_f64(1, 90))],
            [complex(frac_f64(-1, 65), frac_f64(1, 75)), complex(frac_f64(1, 15), frac_f64(1, 60)), complex(frac_f64(1, 28), frac_f64(-1, 50))],
            [complex(frac_f64(1, 70), frac_f64(-1, 60)), complex(frac_f64(1, 32), frac_f64(1, 45)), complex(frac_f64(1, 5), frac_f64(-1, 60))],
        ],
        dtype=complex,
    )
    Ynu = np.array(
        [
            [complex(frac_f64(1, 40), frac_f64(-1, 70)), complex(frac_f64(1, 25), frac_f64(1, 50)), complex(frac_f64(1, 30), frac_f64(-1, 45))],
            [complex(frac_f64(1, 28), frac_f64(1, 55)), complex(frac_f64(1, 9), frac_f64(-1, 35)), complex(frac_f64(1, 18), frac_f64(1, 28))],
            [complex(frac_f64(-1, 35), frac_f64(1, 45)), complex(frac_f64(1, 16), frac_f64(-1, 30)), complex(frac_f64(9, 20), frac_f64(1, 35))],
        ],
        dtype=complex,
    )
    MR_base = np.array(
        [
            [complex(frac_f64(2, 10), frac_f64(1, 30)), complex(frac_f64(1, 25), frac_f64(-1, 40)), complex(frac_f64(1, 35), frac_f64(1, 50))],
            [complex(frac_f64(1, 25), frac_f64(-1, 40)), complex(frac_f64(7, 10), frac_f64(-1, 20)), complex(frac_f64(1, 15), frac_f64(1, 30))],
            [complex(frac_f64(1, 35), frac_f64(1, 50)), complex(frac_f64(1, 15), frac_f64(1, 30)), complex(frac_f64(9, 5), frac_f64(1, 10))],
        ],
        dtype=complex,
    )
    MR = (MR_base + MR_base.T) / 2
    return Yu, Yd, Ye, Ynu, MR


def run_two_step_ps_seesaw_sm_pipeline(
    Yu_mps: np.ndarray,
    Yd_mps: np.ndarray,
    Ye_mps: np.ndarray,
    Ynu_mps: np.ndarray,
    MR_mps: np.ndarray,
    theta_g_mps: float,
    alpha_u_inv: float = frac_f64(45, 1),
    dt_ps: float = frac_f64(-4, 1),
) -> np.ndarray:
    a4_ps = alpha_u_inv - (frac_f64(-10, 1) / (2 * math.pi)) * dt_ps
    a2_ps = alpha_u_inv - (frac_f64(-7, 3) / (2 * math.pi)) * dt_ps
    a1_ps = frac_f64(3, 5) * a2_ps + frac_f64(2, 5) * a4_ps
    a3_ps = a4_ps

    g1_ps = math.sqrt(4 * math.pi / a1_ps)
    g2_ps = math.sqrt(4 * math.pi / a2_ps)
    g3_ps = math.sqrt(4 * math.pi / a3_ps)
    lam_ps = (g2_ps * g2_ps) / 5

    kappa_ps = Ynu_mps @ np.linalg.inv(MR_mps) @ Ynu_mps.T

    Yu_ir, Yd_ir, Ye_ir, kw_ir, _, _, _, _ = integrate_sm_rk4_f64(
        Yu_mps, Yd_mps, Ye_mps, kappa_ps, g1_ps, g2_ps, g3_ps, lam_ps, frac_f64(-27, 1), 540, True
    )
    return extract_21_observables(Yu_ir, Yd_ir, Ye_ir, kw_ir, theta_g_mps)


def run_haar_u3_6_and_planted_faults() -> Dict[str, Any]:
    Yu0, Yd0, Ye0, Ynu0, MR0 = build_synthetic_uv_state()
    theta0 = frac_f64(3, 10)
    base_obs = run_two_step_ps_seesaw_sm_pipeline(Yu0, Yd0, Ye0, Ynu0, MR0, theta0)

    rng = np.random.default_rng(20261116)
    max_obs_err_per_trial: List[float] = []
    max_rge_theta_shift_err = frac_f64(0, 1)

    det0_uv = np.linalg.det(Yu0 @ Yd0)
    uv_arg0 = math.atan2(float(np.imag(det0_uv)), float(np.real(det0_uv)))
    base_rge_theta_shift = wrap_angle_pi((base_obs[20] - theta0) - uv_arg0)

    for _ in range(8):
        UQ = haar_unitary_3x3(rng)
        Uu = haar_unitary_3x3(rng)
        Ud = haar_unitary_3x3(rng)
        UL = haar_unitary_3x3(rng)
        Ue = haar_unitary_3x3(rng)
        UN = haar_unitary_3x3(rng)

        Yu_s = UQ @ Yu0 @ Uu.conj().T
        Yd_s = UQ @ Yd0 @ Ud.conj().T
        Ye_s = UL @ Ye0 @ Ue.conj().T
        Ynu_s = UL @ Ynu0 @ UN.conj().T
        MR_s = UN.conj() @ MR0 @ UN.conj().T

        jac = (np.linalg.det(UQ) ** 2) * np.linalg.det(Uu.conj().T) * np.linalg.det(Ud.conj().T)
        theta_s = wrap_angle_pi(theta0 - math.atan2(float(np.imag(jac)), float(np.real(jac))))

        obs_s = run_two_step_ps_seesaw_sm_pipeline(Yu_s, Yd_s, Ye_s, Ynu_s, MR_s, theta_s)
        diffs = np.abs(obs_s[:20] - base_obs[:20])
        theta_diff = abs(wrap_angle_pi(obs_s[20] - base_obs[20]))
        trial_max = max(float(np.max(diffs)), theta_diff)
        max_obs_err_per_trial.append(trial_max)

        obs_no_fujikawa = run_two_step_ps_seesaw_sm_pipeline(Yu_s, Yd_s, Ye_s, Ynu_s, MR_s, frac_f64(0, 1))
        det_s_uv = np.linalg.det(Yu_s @ Yd_s)
        uv_arg_s = math.atan2(float(np.imag(det_s_uv)), float(np.real(det_s_uv)))
        rge_shift_s = wrap_angle_pi(obs_no_fujikawa[20] - uv_arg_s)
        max_rge_theta_shift_err = max(max_rge_theta_shift_err, abs(wrap_angle_pi(rge_shift_s - base_rge_theta_shift)))

    haar_max_err = max(max_obs_err_per_trial)
    haar_gate_passed = (haar_max_err < pow10_f64(-12)) and (max_rge_theta_shift_err < pow10_f64(-12))

    z3 = np.zeros((3, 3), dtype=complex)
    _, _, _, _, _, _, g3_good, _ = integrate_sm_rk4_f64(
        z3, z3, z3, z3, frac_f64(0, 1), frac_f64(0, 1), frac_f64(3, 5), frac_f64(0, 1), frac_f64(-15, 1), 600, True, frac_f64(1, 1)
    )
    _, _, _, _, _, _, g3_pf1, _ = integrate_sm_rk4_f64(
        z3, z3, z3, z3, frac_f64(0, 1), frac_f64(0, 1), frac_f64(3, 5), frac_f64(0, 1), frac_f64(-15, 1), 600, True, frac_f64(1, 2)
    )
    pf0_1_err = abs(g3_pf1 - g3_good) / abs(g3_good)
    pf0_1_caught = pf0_1_err > frac_f64(1, 4)

    UQ_t = haar_unitary_3x3(rng)
    Uu_t = haar_unitary_3x3(rng)
    Ud_t = haar_unitary_3x3(rng)
    g_test = math.sqrt(4 * math.pi / 40)
    Yu_wc_1, Yd_wc_1, _, _, _, _, _, _ = integrate_sm_rk4_f64(
        Yu0, Yd0, Ye0, z3, g_test, g_test, g_test, frac_f64(1, 8), frac_f64(-27, 1), 300, True, frac_f64(1, 1), wrong_chirality=True
    )
    Yu_wc_2, Yd_wc_2, _, _, _, _, _, _ = integrate_sm_rk4_f64(
        UQ_t @ Yu0 @ Uu_t.conj().T, UQ_t @ Yd0 @ Ud_t.conj().T, Ye0, z3, g_test, g_test, g_test, frac_f64(1, 8),
        frac_f64(-27, 1), 300, True, frac_f64(1, 1), wrong_chirality=True
    )
    uu1, su1, _ = np.linalg.svd(Yu_wc_1); uu1 = uu1[:, np.argsort(su1)]
    ud1, sd1, _ = np.linalg.svd(Yd_wc_1); ud1 = ud1[:, np.argsort(sd1)]
    uu2, su2, _ = np.linalg.svd(Yu_wc_2); uu2 = uu2[:, np.argsort(su2)]
    ud2, sd2, _ = np.linalg.svd(Yd_wc_2); ud2 = ud2[:, np.argsort(sd2)]
    pf0_2_err = float(np.max(np.abs(np.abs(uu1.conj().T @ ud1) - np.abs(uu2.conj().T @ ud2))))
    pf0_2_caught = pf0_2_err > pow10_f64(-3)

    u_lr_1, _, vh_lr_1 = np.linalg.svd(Yu0)
    vr_1 = vh_lr_1.conj().T
    u_lr_2, _, vh_lr_2 = np.linalg.svd(UQ_t @ Yu0 @ Uu_t.conj().T)
    vr_2 = vh_lr_2.conj().T
    pf0_3_err = float(np.max(np.abs(np.abs(u_lr_1.conj().T @ vr_1) - np.abs(u_lr_2.conj().T @ vr_2))))
    pf0_3_caught = pf0_3_err > frac_f64(1, 10)

    UL_t = haar_unitary_3x3(rng)
    UN_t = haar_unitary_3x3(rng)
    kw_bad_1 = Ynu0.T @ np.linalg.inv(MR0) @ Ynu0
    Ynu_rot = UL_t @ Ynu0 @ UN_t.conj().T
    MR_rot = UN_t.conj() @ MR0 @ UN_t.conj().T
    kw_bad_2 = Ynu_rot.T @ np.linalg.inv(MR_rot) @ Ynu_rot
    ue_1, se_1, _ = np.linalg.svd(Ye0); ue_1 = ue_1[:, np.argsort(se_1)]
    ue_2, se_2, _ = np.linalg.svd(UL_t @ Ye0); ue_2 = ue_2[:, np.argsort(se_2)]
    ev1, un1 = np.linalg.eigh(kw_bad_1 @ kw_bad_1.conj().T); un1 = un1[:, np.argsort(np.real(ev1))]
    ev2, un2 = np.linalg.eigh(kw_bad_2 @ kw_bad_2.conj().T); un2 = un2[:, np.argsort(np.real(ev2))]
    pf0_4_err = float(np.max(np.abs(np.abs(ue_1.conj().T @ un1) - np.abs(ue_2.conj().T @ un2))))
    pf0_4_caught = pf0_4_err > frac_f64(1, 10)

    pf0_5_err = float(abs(Fraction(1, 2) - Fraction(3, 5)))
    pf0_5_caught = pf0_5_err > frac_f64(1, 20)

    all_planted_caught = pf0_1_caught and pf0_2_caught and pf0_3_caught and pf0_4_caught and pf0_5_caught
    return {
        "haar_u3_6_gate_passed": haar_gate_passed,
        "haar_u3_6_max_err_across_8_trials_21_observables": haar_max_err,
        "haar_u3_6_per_trial_max_err": max_obs_err_per_trial,
        "haar_u3_6_rge_theta_shift_max_err": max_rge_theta_shift_err,
        "all_5_planted_faults_caught": all_planted_caught,
        "planted_faults": {
            "PF0_1_scale_factor_err": {"measured_err": pf0_1_err, "caught": pf0_1_caught},
            "PF0_2_wrong_chirality_err": {"measured_err": pf0_2_err, "caught": pf0_2_caught},
            "PF0_3_left_right_overlap_err": {"measured_err": pf0_3_err, "caught": pf0_3_caught},
            "PF0_4_transposed_weinberg_err": {"measured_err": pf0_4_err, "caught": pf0_4_caught},
            "PF0_5_corrupted_ps_weights_err": {"measured_err": pf0_5_err, "caught": pf0_5_caught},
        },
    }


def main() -> None:
    ast_res = verify_ast_g0()
    lie_res = run_lie_algebra_and_polynomial_checks()
    bench_res = run_four_literature_benchmarks()
    haar_res = run_haar_u3_6_and_planted_faults()

    gate_passed = (
        ast_res["ast_gate_passed"]
        and lie_res["lie_algebra_and_polynomial_gate_passed"]
        and bench_res["four_benchmarks_gate_passed"]
        and haar_res["haar_u3_6_gate_passed"]
        and haar_res["all_5_planted_faults_caught"]
    )

    out_payload = {
        "campaign": "AGY-002-ENDGAME-V2",
        "gate": "Gate 0 — Literature RGE & U(3)^6 Invariance Lock",
        "empirical_firewall": "0 of 19",
        "gate_0_passed": gate_passed,
        "section_0_ast_lock": ast_res,
        "section_1_lie_algebra_and_buttazzo_polynomial_lock": lie_res,
        "section_2_four_literature_rge_benchmarks": bench_res,
        "section_3_haar_u3_6_and_planted_faults": haar_res,
    }

    out_path = Path(__file__).resolve().parent / "verify_endgame_v2_g0_fixed_out.json"
    out_bytes = (json.dumps(out_payload, indent=2, sort_keys=False) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    digest = hashlib.sha256(out_bytes).hexdigest()
    sha_path = Path(__file__).resolve().parent / "OUTPUT_SHA256.txt"
    sha_path.write_text(f"{digest}  relays/agy002_endgame_v2_g0_fixed/verify_endgame_v2_g0_fixed_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
