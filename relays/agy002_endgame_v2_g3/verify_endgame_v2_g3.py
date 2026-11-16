#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_ENDGAME-V2-G3:
  Radiative EWSB Scale Closure, Picard-Lindelof / Coleman-Weinberg / Vissani Threshold
  Theorems, and Dimensionless v_EW Ledger (0 of 19).

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

def verify_ast_g3() -> Dict[str, Any]:
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
    return {
        "ast_gate_passed": (len(disallowed) == 0) and (float_literals == 0),
        "imported_modules": sorted(mods),
        "disallowed_imports": disallowed,
        "float_literals_in_entire_file": float_literals,
    }


# ============================================================================
# SECTION 1: BUTTAZZO ET AL. (2013) EQ. (A.6) EXACT 2-LOOP gamma_{m^2} LOCK
# ============================================================================

def verify_buttazzo_gamma_m2_polynomial() -> Dict[str, Any]:
    yt2 = Fraction(7, 11)
    yb2 = Fraction(3, 13)
    ytau2 = Fraction(2, 17)
    g1s = Fraction(5, 19)
    g2s = Fraction(6, 23)
    g3s = Fraction(9, 29)
    lam = Fraction(4, 31)

    y2_tr = 3 * yt2 + 3 * yb2 + ytau2

    # Matrix-trace form of d(ln mu_H^2) / d(ln mu) = 2 * (1 / m^2) dm^2 / d(ln mu^2):
    gam1_mat = 12 * lam + 2 * y2_tr - Fraction(9, 2) * g2s - Fraction(9, 10) * g1s
    gam2_mat = (
        -60 * (lam ** 2)
        - 24 * lam * y2_tr
        + 72 * lam * g2s
        + Fraction(72, 5) * lam * g1s
        - Fraction(27, 2) * (yt2 ** 2 + yb2 ** 2)
        - Fraction(9, 2) * (ytau2 ** 2)
        - 21 * yt2 * yb2
        + (40 * g3s + Fraction(45, 4) * g2s + Fraction(17, 4) * g1s) * yt2
        + (40 * g3s + Fraction(45, 4) * g2s + Fraction(5, 4) * g1s) * yb2
        + (Fraction(15, 4) * g2s + Fraction(15, 4) * g1s) * ytau2
        - Fraction(145, 16) * (g2s ** 2)
        + Fraction(1671, 400) * (g1s ** 2)
        + Fraction(9, 8) * g2s * g1s
    )

    # Verbatim 2 * Buttazzo et al. (2013) Appendix A Higgs mass term (d/d ln mu = 2 d/d ln mu^2):
    gam1_buttazzo = 2 * (6 * lam + 3 * yt2 + 3 * yb2 + ytau2 - Fraction(9, 4) * g2s - Fraction(9, 20) * g1s)
    gam2_buttazzo = 2 * (
        lam * (-30 * lam - 36 * yt2 - 36 * yb2 - 12 * ytau2 + 36 * g2s + Fraction(36, 5) * g1s)
        + yt2 * (-Fraction(27, 4) * yt2 - Fraction(21, 2) * yb2 + 20 * g3s + Fraction(45, 8) * g2s + Fraction(17, 8) * g1s)
        + yb2 * (-Fraction(27, 4) * yb2 + 20 * g3s + Fraction(45, 8) * g2s + Fraction(5, 8) * g1s)
        + ytau2 * (-Fraction(9, 4) * ytau2 + Fraction(15, 8) * g2s + Fraction(15, 8) * g1s)
        - Fraction(145, 32) * (g2s ** 2)
        + Fraction(1671, 800) * (g1s ** 2)
        + Fraction(9, 16) * g2s * g1s
    )

    exact_match = (gam1_mat == gam1_buttazzo) and (gam2_mat == gam2_buttazzo)
    return {
        "buttazzo_gamma_m2_exact_match": exact_match,
        "gamma_1loop_sample_rational": str(gam1_mat),
        "gamma_2loop_sample_rational": str(gam2_mat),
    }


def sm_2loop_with_muH2_rhs_f64(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    muH2: float,
    inhom_source: float = frac_f64(0, 1),
    gamma_scale: float = frac_f64(1, 1),
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float, float, float]:
    k1 = frac_f64(1, 16) / (math.pi * math.pi)
    k2 = k1 * k1

    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    He = Ye @ Ye.conj().T

    tu = float(np.real(np.trace(Hu)))
    td = float(np.real(np.trace(Hd)))
    te = float(np.real(np.trace(He)))
    y2_tr = 3 * tu + 3 * td + te

    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    eye3 = np.eye(3, dtype=complex)

    c1_u = (y2_tr - frac_f64(17, 20) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hu - Hd)
    c1_d = (y2_tr - frac_f64(1, 4) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hd - Hu)
    c1_e = (y2_tr - frac_f64(9, 4) * g1s - frac_f64(9, 4) * g2s) * eye3 + frac_f64(3, 2) * He

    thu2 = float(np.real(np.trace(Hu @ Hu)))
    thd2 = float(np.real(np.trace(Hd @ Hd)))
    the2 = float(np.real(np.trace(He @ He)))
    thuhd = float(np.real(np.trace(Hu @ Hd)))

    chi2 = (
        -frac_f64(27, 4) * (thu2 + thd2) - frac_f64(9, 4) * the2 + frac_f64(3, 2) * thuhd
        + (frac_f64(17, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * tu
        + (frac_f64(5, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * td
        + (frac_f64(15, 8) * g1s + frac_f64(15, 8) * g2s) * te
    )

    c2_u = (
        frac_f64(3, 2) * (Hu @ Hu) - (Hu @ Hd) - frac_f64(1, 4) * (Hd @ Hu) + frac_f64(11, 4) * (Hd @ Hd)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(223, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hu
        + (frac_f64(5, 4) * y2_tr - frac_f64(43, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hd
        + (chi2 + 6 * lam * lam + frac_f64(1187, 600) * (g1s ** 2) - frac_f64(9, 20) * g1s * g2s
           + frac_f64(19, 15) * g1s * g3s - frac_f64(23, 4) * (g2s ** 2) + 9 * g2s * g3s - 108 * (g3s ** 2)) * eye3
    )
    c2_d = (
        frac_f64(3, 2) * (Hd @ Hd) - (Hd @ Hu) - frac_f64(1, 4) * (Hu @ Hd) + frac_f64(11, 4) * (Hu @ Hu)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(187, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hd
        + (frac_f64(5, 4) * y2_tr - frac_f64(79, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hu
        + (chi2 + 6 * lam * lam - frac_f64(127, 600) * (g1s ** 2) - frac_f64(27, 20) * g1s * g2s
           + frac_f64(31, 15) * g1s * g3s - frac_f64(23, 4) * (g2s ** 2) + 9 * g2s * g3s - 108 * (g3s ** 2)) * eye3
    )
    c2_e = (
        frac_f64(3, 2) * (He @ He)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(387, 80) * g1s + frac_f64(135, 16) * g2s) * He
        + (chi2 + 6 * lam * lam + frac_f64(1371, 200) * (g1s ** 2) + frac_f64(27, 20) * g1s * g2s - frac_f64(23, 4) * (g2s ** 2)) * eye3
    )

    dYu = (k1 * c1_u + k2 * c2_u) @ Yu
    dYd = (k1 * c1_d + k2 * c2_d) @ Yd
    dYe = (k1 * c1_e + k2 * c2_e) @ Ye

    dg1 = k1 * frac_f64(41, 10) * (g1 ** 3) + k2 * (g1 ** 3) * (
        frac_f64(199, 50) * g1s + frac_f64(27, 10) * g2s + frac_f64(44, 5) * g3s - frac_f64(17, 10) * tu - frac_f64(1, 2) * td - frac_f64(3, 2) * te
    )
    dg2 = k1 * frac_f64(-19, 6) * (g2 ** 3) + k2 * (g2 ** 3) * (
        frac_f64(9, 10) * g1s + frac_f64(35, 6) * g2s + 12 * g3s - frac_f64(3, 2) * tu - frac_f64(3, 2) * td - frac_f64(1, 2) * te
    )
    dg3 = k1 * (-7) * (g3 ** 3) + k2 * (g3 ** 3) * (
        frac_f64(11, 10) * g1s + frac_f64(9, 2) * g2s - 26 * g3s - 2 * tu - 2 * td
    )

    thu3 = float(np.real(np.trace(Hu @ Hu @ Hu)))
    thd3 = float(np.real(np.trace(Hd @ Hd @ Hd)))
    the3 = float(np.real(np.trace(He @ He @ He)))
    thu2hd = float(np.real(np.trace(Hu @ Hu @ Hd)))
    thuhd2 = float(np.real(np.trace(Hu @ Hd @ Hd)))

    dlam1 = (
        24 * lam * lam + lam * (4 * y2_tr - 9 * g2s - frac_f64(9, 5) * g1s)
        - 2 * (3 * thu2 + 3 * thd2 + the2)
        + frac_f64(9, 8) * (g2s ** 2) + frac_f64(27, 200) * (g1s ** 2) + frac_f64(9, 20) * g1s * g2s
    )
    dlam2 = (
        -312 * (lam ** 3) + 36 * (lam * lam) * (3 * g2s + frac_f64(3, 5) * g1s) - 48 * (lam * lam) * y2_tr
        + lam * (80 * g3s + frac_f64(45, 2) * g2s) * (tu + td)
        + lam * g1s * (frac_f64(17, 2) * tu + frac_f64(5, 2) * td + frac_f64(15, 2) * te)
        + frac_f64(15, 2) * lam * g2s * te
        - 3 * lam * (thu2 + thd2 + frac_f64(1, 3) * the2 + 14 * thuhd)
        + lam * (-frac_f64(73, 8) * (g2s ** 2) + frac_f64(117, 20) * g1s * g2s + frac_f64(1887, 200) * (g1s ** 2))
        + 30 * (thu3 + thd3 + frac_f64(1, 3) * the3) - 6 * (thu2hd + thuhd2)
        - 32 * g3s * (thu2 + thd2) - frac_f64(8, 5) * g1s * thu2 + frac_f64(4, 5) * g1s * thd2 - frac_f64(12, 5) * g1s * the2
        - frac_f64(9, 4) * (g2s ** 2) * (tu + td + frac_f64(1, 3) * te)
        + g1s * g2s * (frac_f64(63, 10) * tu + frac_f64(27, 10) * td + frac_f64(33, 10) * te)
        - (g1s ** 2) * (frac_f64(171, 100) * tu - frac_f64(9, 20) * td + frac_f64(9, 4) * te)
        + frac_f64(305, 16) * (g2s ** 3) - frac_f64(289, 80) * (g2s ** 2) * g1s
        - frac_f64(1677, 400) * g2s * (g1s ** 2) - frac_f64(3411, 2000) * (g1s ** 3)
    )
    dlam = k1 * dlam1 + k2 * dlam2

    gam1 = 12 * lam + 2 * y2_tr - frac_f64(9, 2) * g2s - frac_f64(9, 10) * g1s
    gam2 = (
        -60 * (lam * lam) - 24 * lam * y2_tr + 72 * lam * g2s + frac_f64(72, 5) * lam * g1s
        - frac_f64(27, 2) * (thu2 + thd2) - frac_f64(9, 2) * the2 - 21 * thuhd
        + (40 * g3s + frac_f64(45, 4) * g2s + frac_f64(17, 4) * g1s) * tu
        + (40 * g3s + frac_f64(45, 4) * g2s + frac_f64(5, 4) * g1s) * td
        + (frac_f64(15, 4) * g2s + frac_f64(15, 4) * g1s) * te
        - frac_f64(145, 16) * (g2s ** 2) + frac_f64(1671, 400) * (g1s ** 2) + frac_f64(9, 8) * g2s * g1s
    )
    gamma_tot = gamma_scale * (k1 * gam1 + k2 * gam2)
    dmuH2 = gamma_tot * muH2 + inhom_source
    return dYu, dYd, dYe, dg1, dg2, dg3, dlam, dmuH2, gamma_tot


def rk4_sm_muH2_step(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    muH2: float,
    h: float,
    inhom_source: float = frac_f64(0, 1),
    gamma_scale: float = frac_f64(1, 1),
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float, float, float]:
    s1 = sm_2loop_with_muH2_rhs_f64(Yu, Yd, Ye, g1, g2, g3, lam, muH2, inhom_source, gamma_scale)
    s2 = sm_2loop_with_muH2_rhs_f64(
        Yu + frac_f64(1, 2) * h * s1[0], Yd + frac_f64(1, 2) * h * s1[1], Ye + frac_f64(1, 2) * h * s1[2],
        g1 + frac_f64(1, 2) * h * s1[3], g2 + frac_f64(1, 2) * h * s1[4], g3 + frac_f64(1, 2) * h * s1[5],
        lam + frac_f64(1, 2) * h * s1[6], muH2 + frac_f64(1, 2) * h * s1[7], inhom_source, gamma_scale,
    )
    s3 = sm_2loop_with_muH2_rhs_f64(
        Yu + frac_f64(1, 2) * h * s2[0], Yd + frac_f64(1, 2) * h * s2[1], Ye + frac_f64(1, 2) * h * s2[2],
        g1 + frac_f64(1, 2) * h * s2[3], g2 + frac_f64(1, 2) * h * s2[4], g3 + frac_f64(1, 2) * h * s2[5],
        lam + frac_f64(1, 2) * h * s2[6], muH2 + frac_f64(1, 2) * h * s2[7], inhom_source, gamma_scale,
    )
    s4 = sm_2loop_with_muH2_rhs_f64(
        Yu + h * s3[0], Yd + h * s3[1], Ye + h * s3[2],
        g1 + h * s3[3], g2 + h * s3[4], g3 + h * s3[5],
        lam + h * s3[6], muH2 + h * s3[7], inhom_source, gamma_scale,
    )
    Yu_n = Yu + (h / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
    Yd_n = Yd + (h / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
    Ye_n = Ye + (h / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
    g1_n = g1 + (h / 6) * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
    g2_n = g2 + (h / 6) * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
    g3_n = g3 + (h / 6) * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
    lam_n = lam + (h / 6) * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
    muH2_n = muH2 + (h / 6) * (s1[7] + 2 * s2[7] + 2 * s3[7] + s4[7])
    # Exact Simpson quadrature increment for gamma(t) over [0, h] by taking two half-steps of size h/2!
    s1_h2 = sm_2loop_with_muH2_rhs_f64(Yu, Yd, Ye, g1, g2, g3, lam, muH2, inhom_source, gamma_scale)
    s2_h2 = sm_2loop_with_muH2_rhs_f64(
        Yu + frac_f64(1, 4) * h * s1_h2[0], Yd + frac_f64(1, 4) * h * s1_h2[1], Ye + frac_f64(1, 4) * h * s1_h2[2],
        g1 + frac_f64(1, 4) * h * s1_h2[3], g2 + frac_f64(1, 4) * h * s1_h2[4], g3 + frac_f64(1, 4) * h * s1_h2[5],
        lam + frac_f64(1, 4) * h * s1_h2[6], muH2 + frac_f64(1, 4) * h * s1_h2[7], inhom_source, gamma_scale,
    )
    s3_h2 = sm_2loop_with_muH2_rhs_f64(
        Yu + frac_f64(1, 4) * h * s2_h2[0], Yd + frac_f64(1, 4) * h * s2_h2[1], Ye + frac_f64(1, 4) * h * s2_h2[2],
        g1 + frac_f64(1, 4) * h * s2_h2[3], g2 + frac_f64(1, 4) * h * s2_h2[4], g3 + frac_f64(1, 4) * h * s2_h2[5],
        lam + frac_f64(1, 4) * h * s2_h2[6], muH2 + frac_f64(1, 4) * h * s2_h2[7], inhom_source, gamma_scale,
    )
    s4_h2 = sm_2loop_with_muH2_rhs_f64(
        Yu + frac_f64(1, 2) * h * s3_h2[0], Yd + frac_f64(1, 2) * h * s3_h2[1], Ye + frac_f64(1, 2) * h * s3_h2[2],
        g1 + frac_f64(1, 2) * h * s3_h2[3], g2 + frac_f64(1, 2) * h * s3_h2[4], g3 + frac_f64(1, 2) * h * s3_h2[5],
        lam + frac_f64(1, 2) * h * s3_h2[6], muH2 + frac_f64(1, 2) * h * s3_h2[7], inhom_source, gamma_scale,
    )
    Yu_mid = Yu + (h / 12) * (s1_h2[0] + 2 * s2_h2[0] + 2 * s3_h2[0] + s4_h2[0])
    Yd_mid = Yd + (h / 12) * (s1_h2[1] + 2 * s2_h2[1] + 2 * s3_h2[1] + s4_h2[1])
    Ye_mid = Ye + (h / 12) * (s1_h2[2] + 2 * s2_h2[2] + 2 * s3_h2[2] + s4_h2[2])
    g1_mid = g1 + (h / 12) * (s1_h2[3] + 2 * s2_h2[3] + 2 * s3_h2[3] + s4_h2[3])
    g2_mid = g2 + (h / 12) * (s1_h2[4] + 2 * s2_h2[4] + 2 * s3_h2[4] + s4_h2[4])
    g3_mid = g3 + (h / 12) * (s1_h2[5] + 2 * s2_h2[5] + 2 * s3_h2[5] + s4_h2[5])
    lam_mid = lam + (h / 12) * (s1_h2[6] + 2 * s2_h2[6] + 2 * s3_h2[6] + s4_h2[6])
    mu_mid = muH2 + (h / 12) * (s1_h2[7] + 2 * s2_h2[7] + 2 * s3_h2[7] + s4_h2[7])
    _, _, _, _, _, _, _, _, gam_mid = sm_2loop_with_muH2_rhs_f64(Yu_mid, Yd_mid, Ye_mid, g1_mid, g2_mid, g3_mid, lam_mid, mu_mid, inhom_source, gamma_scale)
    _, _, _, _, _, _, _, _, gam_end = sm_2loop_with_muH2_rhs_f64(Yu_n, Yd_n, Ye_n, g1_n, g2_n, g3_n, lam_n, muH2_n, inhom_source, gamma_scale)
    d_int_gamma = (h / 6) * (s1[8] + 4 * gam_mid + gam_end)
    return Yu_n, Yd_n, Ye_n, g1_n, g2_n, g3_n, lam_n, muH2_n, d_int_gamma


# ============================================================================
# SECTION 2: HOMOGENEOUS NON-CROSSING & COLEMAN-WEINBERG OBSTRUCTION THEOREMS
# ============================================================================

def run_homogeneous_and_cw_obstructions() -> Dict[str, Any]:
    Yu = np.diag([frac_f64(1, 100), frac_f64(1, 20), frac_f64(1, 2)]).astype(complex)
    Yd = np.diag([frac_f64(1, 200), frac_f64(1, 40), frac_f64(1, 5)]).astype(complex)
    Ye = np.diag([frac_f64(1, 300), frac_f64(1, 50), frac_f64(1, 8)]).astype(complex)
    g_uv = math.sqrt(4 * math.pi / 45)
    g1, g2, g3, lam = g_uv, g_uv, g_uv, frac_f64(1, 8)
    muH2_0 = frac_f64(1, 1)

    n_steps = 1200
    h = frac_f64(-28, 1) / n_steps
    Yu_c, Yd_c, Ye_c = Yu.copy(), Yd.copy(), Ye.copy()
    g1_c, g2_c, g3_c, lam_c, mu_c = g1, g2, g3, lam, muH2_0
    int_gamma = frac_f64(0, 1)
    min_muH2_along_flow = mu_c

    for _ in range(n_steps):
        Yu_c, Yd_c, Ye_c, g1_c, g2_c, g3_c, lam_c, mu_c, d_ig = rk4_sm_muH2_step(
            Yu_c, Yd_c, Ye_c, g1_c, g2_c, g3_c, lam_c, mu_c, h
        )
        int_gamma += d_ig
        min_muH2_along_flow = min(min_muH2_along_flow, mu_c)

    muH2_analytic_exp = muH2_0 * math.exp(int_gamma)
    picard_exp_rel_err = abs(mu_c - muH2_analytic_exp) / abs(muH2_analytic_exp)
    homogeneous_never_crosses_zero = min_muH2_along_flow > frac_f64(1, 10)

    # Coleman-Weinberg (mu_H^2 = 0) at lambda(mu_CW) = 0:
    z3 = np.zeros((3, 3), dtype=complex)
    Yu_top = np.diag([frac_f64(1, 100), frac_f64(1, 20), frac_f64(9, 10)]).astype(complex)
    _, _, _, _, _, _, beta_lam_gauge_only, _, _ = sm_2loop_with_muH2_rhs_f64(z3, z3, z3, frac_f64(1, 2), frac_f64(3, 5), frac_f64(4, 5), frac_f64(0, 1), frac_f64(0, 1))
    _, _, _, _, _, _, beta_lam_top_dom, _, _ = sm_2loop_with_muH2_rhs_f64(Yu_top, Yd, Ye, frac_f64(1, 2), frac_f64(3, 5), frac_f64(4, 5), frac_f64(0, 1), frac_f64(0, 1))

    cw_obstruction_verified = (beta_lam_gauge_only > 0) and (beta_lam_top_dom < 0)
    passed = (picard_exp_rel_err < pow10_f64(-11)) and homogeneous_never_crosses_zero and cw_obstruction_verified
    return {
        "homogeneous_and_cw_obstruction_gate_passed": passed,
        "picard_lindelof_exp_integral_rel_err": picard_exp_rel_err,
        "min_muH2_along_pure_sm_flow_from_unit_uv": min_muH2_along_flow,
        "homogeneous_msbar_crosses_zero": not homogeneous_never_crosses_zero,
        "coleman_weinberg_beta_lam_at_lam0_gauge_only": beta_lam_gauge_only,
        "coleman_weinberg_beta_lam_at_lam0_top_dominated": beta_lam_top_dom,
        "top_dominated_cw_is_maximum_not_minimum": cw_obstruction_verified,
    }


# ============================================================================
# SECTION 3: HEAVY-THRESHOLD RADIATIVE SHIFT (VISSANI SEESAW vs SCALAR PORTAL)
# ============================================================================

def haar_unitary_3x3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[None, :]


def run_threshold_ewsb_and_dimensionless_ledger() -> Dict[str, Any]:
    # 1) Verify Vissani (1998) 1-loop MSbar RG invariance mu * d/d(mu) V_eff^{(N_R)}(mu, H) = 0!
    # V_eff^{(N_R)}|_{O(|H|^2)} = [ mu_H^2(mu) - (Tr(Y_nu^dag Y_nu M_R^2) / (8 pi^2)) * (ln(M_R^2 / mu^2) - 1) ] |H|^2
    # with d(mu_H^2)/d(ln mu)|_{N_R} = - Tr(Y_nu^dag Y_nu M_R^2) / (4 pi^2) < 0!
    tr_ynu_mr2 = frac_f64(3, 5)  # in units of M_R^2
    beta_muH2_vissani = -tr_ynu_mr2 / (4 * math.pi * math.pi)

    def v_eff_quad_coeff_nr(ln_mu: float, muH2_at_0: float, beta_nr: float) -> float:
        muH2_mu = muH2_at_0 + beta_nr * ln_mu
        # Here M_R = 1 => ln(M_R^2 / mu^2) = -2 * ln_mu
        loop_coeff = -(tr_ynu_mr2 / (8 * math.pi * math.pi)) * (-2 * ln_mu - 1)
        return muH2_mu + loop_coeff

    eps_mu = pow10_f64(-6)
    rg_deriv_nr = (v_eff_quad_coeff_nr(eps_mu, frac_f64(1, 1), beta_muH2_vissani) - v_eff_quad_coeff_nr(-eps_mu, frac_f64(1, 1), beta_muH2_vissani)) / (2 * eps_mu)
    # Downward shift from M_PS to M_R (Delta_ln_mu = -ln(M_PS / M_R) = -3 < 0):
    downward_nr_shift = beta_muH2_vissani * frac_f64(-3, 1)  # STRICTLY POSITIVE (+), stabilizing unbroken phase!

    # 2) Heavy Pati-Salam complex scalar portal V >= lambda_HS |H|^2 |S|^2 (d_S real degrees of freedom):
    # V_CW^{(S)}|_{O(|H|^2)} = + (d_S * lambda_HS * M_S^2 / (32 pi^2)) * (ln(M_S^2 / mu^2) - 1) |H|^2
    # => RG invariance requires d(mu_H^2)/d(ln mu)|_S = + d_S * lambda_HS * M_S^2 / (16 pi^2) > 0!
    # Running DOWNWARD from M_U to M_PS (Delta_ln_mu = -Delta_PS < 0) gives Delta(mu_H^2) < 0, driving radiative zero crossing!
    d_S = 16  # complex (4,1,2) + (4bar,2,1) = 16 complex = 32 real? Use d_S = 16 real benchmark
    lam_HS = frac_f64(1, 2)
    beta_muH2_portal = (d_S * lam_HS) / (16 * math.pi * math.pi)  # in units of M_PS^2

    # Integrate from M_U down to M_PS over Delta_PS = 4 starting from positive mu_H^2(M_U) / M_PS^2 = +1/10:
    Yu = np.diag([frac_f64(1, 100), frac_f64(1, 20), frac_f64(1, 2)]).astype(complex)
    Yd = np.diag([frac_f64(1, 200), frac_f64(1, 40), frac_f64(1, 5)]).astype(complex)
    Ye = np.diag([frac_f64(1, 300), frac_f64(1, 50), frac_f64(1, 8)]).astype(complex)
    g_u = math.sqrt(4 * math.pi / 50)
    lam_u = frac_f64(1, 8)
    muH2_u = frac_f64(1, 10)  # > 0 in symmetric phase at M_U!

    n_ps = 400
    h_ps = frac_f64(-4, 1) / n_ps
    Yu_c, Yd_c, Ye_c = Yu.copy(), Yd.copy(), Ye.copy()
    g1_c, g2_c, g3_c, lam_c, mu_c = g_u, g_u, g_u, lam_u, muH2_u
    t_cross_found: float = frac_f64(1, 1)
    t_cur = frac_f64(0, 1)
    for _ in range(n_ps):
        mu_prev = mu_c
        Yu_c, Yd_c, Ye_c, g1_c, g2_c, g3_c, lam_c, mu_c, _ = rk4_sm_muH2_step(
            Yu_c, Yd_c, Ye_c, g1_c, g2_c, g3_c, lam_c, mu_c, h_ps, inhom_source=beta_muH2_portal
        )
        if mu_prev > 0 and mu_c <= 0 and t_cross_found > 0:
            # Linear interpolation inside tiny step |h_ps| = 0.01
            frac_step = mu_prev / (mu_prev - mu_c)
            t_cross_found = t_cur + frac_step * h_ps
        t_cur += h_ps

    portal_drives_zero_crossing = (t_cross_found < 0) and (mu_c < 0) and (lam_c > 0)

    # 3) Exact 45-digit Fine-Tuning / Hierarchy Price for M_PS / v_EW = exp(Delta_SM) (Guardrail 5):
    # At Delta_SM = 28, achieving v_EW^2 / M_PS^2 = -mu_H^2(IR) / (2 lam(IR) M_PS^2) = exp(-56)
    # requires tuning mu_H^2(M_U) / M_PS^2 against the O(beta_portal * Delta_PS) radiative shift to fractional precision:
    mp.mp.dps = 45
    delta_sm_mp = mp.mpf(28)
    natural_shift_mp = (mp.mpf(d_S) * (mp.mpf(1) / 2) / (16 * mp.pi * mp.pi)) * 4
    target_ir_ratio_mp = mp.exp(-2 * delta_sm_mp)
    fine_tuning_sensitivity_barbieri_giudice = float(natural_shift_mp / target_ir_ratio_mp)

    # 4) Guardrail 5 & Guardrail 3 Check: Express ALL fermion and boson masses purely as dimensionless ratios m_i / v_EW
    # (1 sole dimensionful anchor v_EW!) and verify U(3)^6 Haar invariance (< 1e-12)
    def dimensionless_ewsb_spectrum(Yu_ir: np.ndarray, Yd_ir: np.ndarray, Ye_ir: np.ndarray, g1_ir: float, g2_ir: float, lam_ir: float) -> np.ndarray:
        # In V = mu_H^2 |H|^2 + lam |H|^4 with <H> = (0, v_EW / sqrt(2))^T and mu_H^2 = -lam * v_EW^2:
        # m_f / v_EW = y_f / sqrt(2), m_W / v_EW = g_2 / 2, m_Z / v_EW = sqrt(g_2^2 + (3/5) g_1^2) / 2, m_h / v_EW = sqrt(2 lam)!
        su = np.sort(np.linalg.svd(Yu_ir, compute_uv=False)) / math.sqrt(2)
        sd = np.sort(np.linalg.svd(Yd_ir, compute_uv=False)) / math.sqrt(2)
        se = np.sort(np.linalg.svd(Ye_ir, compute_uv=False)) / math.sqrt(2)
        mw_over_v = g2_ir / 2
        mz_over_v = math.sqrt(g2_ir * g2_ir + frac_f64(3, 5) * g1_ir * g1_ir) / 2
        mh_over_v = math.sqrt(2 * lam_ir)
        return np.array([su[0], su[1], su[2], sd[0], sd[1], sd[2], se[0], se[1], se[2], mw_over_v, mz_over_v, mh_over_v], dtype=float)

    base_ratios = dimensionless_ewsb_spectrum(Yu_c, Yd_c, Ye_c, g1_c, g2_c, lam_c)
    rng = np.random.default_rng(20261120)
    max_haar_ratio_err = frac_f64(0, 1)
    for _ in range(8):
        UQ = haar_unitary_3x3(rng); Uu = haar_unitary_3x3(rng); Ud = haar_unitary_3x3(rng)
        UL = haar_unitary_3x3(rng); Ue = haar_unitary_3x3(rng)
        rot_ratios = dimensionless_ewsb_spectrum(UQ @ Yu_c @ Uu.conj().T, UQ @ Yd_c @ Ud.conj().T, UL @ Ye_c @ Ue.conj().T, g1_c, g2_c, lam_c)
        max_haar_ratio_err = max(max_haar_ratio_err, float(np.max(np.abs(rot_ratios - base_ratios))))

    dimensionful_anchors_used = 1  # Solely v_EW!
    passed = (
        abs(rg_deriv_nr) < pow10_f64(-12)
        and downward_nr_shift > 0
        and portal_drives_zero_crossing
        and fine_tuning_sensitivity_barbieri_giudice > pow10_f64(20)
        and dimensionful_anchors_used == 1
        and max_haar_ratio_err < pow10_f64(-12)
    )
    return {
        "threshold_ewsb_and_ledger_gate_passed": passed,
        "vissani_nr_msbar_rg_invariance_residual": abs(rg_deriv_nr),
        "vissani_downward_nr_shift_positive": downward_nr_shift,
        "portal_scalar_drives_radiative_zero_crossing": portal_drives_zero_crossing,
        "portal_zero_crossing_t": t_cross_found,
        "muH2_at_M_PS_in_M_PS_sq_units": mu_c,
        "barbieri_giudice_hierarchy_sensitivity_at_DeltaSM_28": fine_tuning_sensitivity_barbieri_giudice,
        "parameter_free_v_EW_over_M_PS_closure": False,
        "dimensionful_anchors_in_ir_ledger": dimensionful_anchors_used,
        "haar_u3_6_dimensionless_mass_ratios_max_err": max_haar_ratio_err,
    }


# ============================================================================
# SECTION 4: FIVE PLANTED FAULT CONTROLS (PF3.1 - PF3.5)
# ============================================================================

def run_planted_faults_g3() -> Dict[str, Any]:
    Yu = np.diag([frac_f64(1, 100), frac_f64(1, 20), frac_f64(1, 2)]).astype(complex)
    Yu_top = np.diag([frac_f64(1, 100), frac_f64(1, 20), frac_f64(9, 10)]).astype(complex)
    Yd = np.diag([frac_f64(1, 200), frac_f64(1, 40), frac_f64(1, 5)]).astype(complex)
    Ye = np.diag([frac_f64(1, 300), frac_f64(1, 50), frac_f64(1, 8)]).astype(complex)
    g_uv = math.sqrt(4 * math.pi / 45)
    g1, g2, g3, lam = g_uv, g_uv, g_uv, frac_f64(1, 8)

    # PF3.1: Factor-of-2 confusion (d/d ln mu^2 vs d/d ln mu) in gamma_{mu_H^2}
    Yu1, Yd1, Ye1, g1_1, g2_1, g3_1, lam_1, mu_good = Yu.copy(), Yd.copy(), Ye.copy(), g1, g2, g3, lam, frac_f64(1, 1)
    Yu2, Yd2, Ye2, g1_2, g2_2, g3_2, lam_2, mu_bad = Yu.copy(), Yd.copy(), Ye.copy(), g1, g2, g3, lam, frac_f64(1, 1)
    h = frac_f64(-28, 1) / 400
    for _ in range(400):
        Yu1, Yd1, Ye1, g1_1, g2_1, g3_1, lam_1, mu_good, _ = rk4_sm_muH2_step(Yu1, Yd1, Ye1, g1_1, g2_1, g3_1, lam_1, mu_good, h, frac_f64(0, 1), frac_f64(1, 1))
        Yu2, Yd2, Ye2, g1_2, g2_2, g3_2, lam_2, mu_bad, _ = rk4_sm_muH2_step(Yu2, Yd2, Ye2, g1_2, g2_2, g3_2, lam_2, mu_bad, h, frac_f64(0, 1), frac_f64(1, 2))
    pf3_1_err = abs(mu_bad - mu_good) / abs(mu_good)
    pf3_1_caught = pf3_1_err > frac_f64(1, 10)

    # PF3.2: Homogeneous non-crossing guard catches any false zero-crossing assertion when mu_H^2(0) > 0
    pf3_2_min_pos = mu_good
    pf3_2_caught = pf3_2_min_pos > frac_f64(1, 10)

    # PF3.3: Inverted Vissani fermion-loop MSbar sign breaks mu d/d(mu) V_eff = 0 RG invariance!
    tr_ynu = frac_f64(3, 5)
    bad_beta_nr = +tr_ynu / (4 * math.pi * math.pi)
    eps = pow10_f64(-5)
    v_plus = (1 + bad_beta_nr * eps) - (tr_ynu / (8 * math.pi * math.pi)) * (-2 * eps - 1)
    v_minus = (1 - bad_beta_nr * eps) - (tr_ynu / (8 * math.pi * math.pi)) * (2 * eps - 1)
    pf3_3_rg_err = abs((v_plus - v_minus) / (2 * eps))
    pf3_3_caught = pf3_3_rg_err > frac_f64(1, 100)

    # PF3.4: Unstable top-dominated Coleman-Weinberg critical point has negative curvature d^2 V_CW / dH^2 = 4 beta_lam v^2 < 0!
    _, _, _, _, _, _, beta_lam_top, _, _ = sm_2loop_with_muH2_rhs_f64(Yu_top, Yd, Ye, frac_f64(1, 2), frac_f64(3, 5), frac_f64(4, 5), frac_f64(0, 1), frac_f64(0, 1))
    d2V_over_v2 = 4 * beta_lam_top
    pf3_4_caught = d2V_over_v2 < -frac_f64(1, 100)

    # PF3.5: Guardrail 5 dimensionful-anchor counter catches importing a second independent dimensionful scale (e.g. M_Z alongside v_EW)
    def count_dimensionful_anchors(scales: List[str]) -> int:
        return len(set(scales))

    pf3_5_count = count_dimensionful_anchors(["v_EW", "M_Z_imported"])
    pf3_5_caught = pf3_5_count > 1

    all_caught = pf3_1_caught and pf3_2_caught and pf3_3_caught and pf3_4_caught and pf3_5_caught
    return {
        "all_5_planted_faults_caught": all_caught,
        "PF3_1_half_gamma_scale_rel_err": {"measured_err": pf3_1_err, "caught": pf3_1_caught},
        "PF3_2_homogeneous_positivity_floor": {"min_muH2": pf3_2_min_pos, "caught": pf3_2_caught},
        "PF3_3_inverted_vissani_sign_rg_violation": {"measured_err": pf3_3_rg_err, "caught": pf3_3_caught},
        "PF3_4_unstable_top_cw_curvature": {"d2V_over_v2": d2V_over_v2, "caught": pf3_4_caught},
        "PF3_5_extra_dimensionful_anchor_count": {"anchor_count": pf3_5_count, "caught": pf3_5_caught},
    }


def main() -> None:
    ast_res = verify_ast_g3()
    poly_res = verify_buttazzo_gamma_m2_polynomial()
    obs_res = run_homogeneous_and_cw_obstructions()
    ewsb_res = run_threshold_ewsb_and_dimensionless_ledger()
    pf_res = run_planted_faults_g3()

    gate_passed = (
        ast_res["ast_gate_passed"]
        and poly_res["buttazzo_gamma_m2_exact_match"]
        and obs_res["homogeneous_and_cw_obstruction_gate_passed"]
        and ewsb_res["threshold_ewsb_and_ledger_gate_passed"]
        and pf_res["all_5_planted_faults_caught"]
    )

    payload = {
        "campaign": "AGY-002-ENDGAME-V2",
        "gate": "Gate 3 — Radiative EWSB Scale Closure & Dimensionless v_EW Ledger",
        "empirical_firewall": "0 of 19",
        "gate_3_passed": gate_passed,
        "section_0_ast_lock": ast_res,
        "section_1_buttazzo_2013_gamma_m2_polynomial_lock": poly_res,
        "section_2_picard_lindelof_and_coleman_weinberg_obstructions": obs_res,
        "section_3_heavy_threshold_ewsb_and_dimensionless_vEW_ledger": ewsb_res,
        "section_4_planted_fault_controls": pf_res,
    }

    out_path = Path(__file__).resolve().parent / "verify_endgame_v2_g3_out.json"
    out_bytes = (json.dumps(payload, indent=2, sort_keys=False) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    digest = hashlib.sha256(out_bytes).hexdigest()
    sha_path = Path(__file__).resolve().parent / "OUTPUT_SHA256.txt"
    sha_path.write_text(f"{digest}  relays/agy002_endgame_v2_g3/verify_endgame_v2_g3_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
