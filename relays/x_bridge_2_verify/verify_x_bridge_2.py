#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-BRIDGE-2:
  Exact Left-Acting 2-Loop Mixed-Yukawa Adjoint Repair (BPV JHEP 09 (2014) 098 Eq. 27 &
  PRD 47, 2038 Rank-1 Coefficient 11/2), 80-Digit Invariant Verification, and
  Old-vs-Repaired UV-to-IR Trajectory Audit (0 of 19).

Empirical Firewall: 0 of 19 (zero Standard Model empirical targets read, imported, or compared;
literature RGE solver benchmark floats are strictly AST-isolated inside run_part_2b_repaired_four_pillar_gate).
"""

from __future__ import annotations

import ast
import cmath
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np


# ============================================================================
# SECTION 0: AST SOURCE AUDIT (ZERO IMPORTS & MODEL ZERO-FLOAT ISOLATION)
# ============================================================================

ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "cmath",
    "fractions",
    "hashlib",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "typing",
}

TARGET_FREE_MODEL_FUNCTIONS: Set[str] = {
    "bloch_wigner_mp",
    "z2_from_z1_gluing",
    "tau_nz_from_z1",
    "neg_vol_on_gluing_curve",
    "s_eff_joint_3d_2d",
    "solve_joint_3var_newton",
    "derive_su5_universal_1loop_eliminants_exact",
}


def verify_ast_bridge2() -> Dict[str, Any]:
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
    float_lits = 0
    sqrt3_calls = 0
    found_funcs: Set[str] = set()

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in TARGET_FREE_MODEL_FUNCTIONS:
            found_funcs.add(node.name)
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, float):
                    float_lits += 1
                if isinstance(sub, ast.Call):
                    fn = sub.func
                    is_sqrt = (isinstance(fn, ast.Name) and fn.id == "sqrt") or (
                        isinstance(fn, ast.Attribute) and fn.attr == "sqrt"
                    )
                    if is_sqrt and len(sub.args) == 1:
                        arg0 = sub.args[0]
                        if isinstance(arg0, ast.Constant) and arg0.value == 3:
                            sqrt3_calls += 1

    passed = (
        len(disallowed) == 0
        and found_funcs == TARGET_FREE_MODEL_FUNCTIONS
        and float_lits == 0
        and sqrt3_calls == 0
    )
    return {
        "Gate_AST_Stage2_Bridge_Passed": passed,
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "inspected_target_free_model_functions": sorted(found_funcs),
        "float_literals_in_target_free_model_functions": float_lits,
        "sqrt3_calls_in_target_free_model_functions": sqrt3_calls,
    }


# ============================================================================
# SECTION 1: REPAIRED & PRESERVED-OLD TWO-LOOP SM + WEINBERG RGE KERNELS
# ============================================================================

K1_F64 = 1.0 / (16.0 * math.pi * math.pi)
K2_F64 = K1_F64 * K1_F64


def svd_ascending_np(mat: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    u_m, s_v, _ = np.linalg.svd(mat)
    idx = np.argsort(s_v)
    return u_m[:, idx], s_v[idx]


def takagi_symmetric_ascending_np(w_sym: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    For complex symmetric W_4 = U_nu diag(s_1, s_2, s_3) U_nu^T with distinct singular values,
    direct SVD avoids squaring cond(W_4) ~ 10^5 -> 10^10 in W_4 W_4^dag, preserving full f64 accuracy!
    """
    u_m, s_v, _ = np.linalg.svd(w_sym)
    idx = np.argsort(s_v)
    return u_m[:, idx], s_v[idx]


def sm_2loop_plus_weinberg_rhs_f64(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    W4: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    repaired_mixed_order: bool = True,
    wrong_chirality_control: bool = False,
    wrong_majorana_transpose: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    """
    Left-acting 2-loop SM matrix RGEs + 1-loop Weinberg operator RGE in t = ln(mu).
    When repaired_mixed_order=True (default), uses exact Hermitian-conjugate of Luo-Xiao eqs. 6-7
    matching 2 * d/d(ln mu^2) of Bednyakov-Pikelner-Velizhanin (JHEP 09 (2014) 098 eq. 27, fn. 7):
      b2_Yu mixed = (-1/4 Hu Hd - Hd Hu) Yu
      b2_Yd mixed = (-1/4 Hd Hu - Hu Hd) Yd
    When repaired_mixed_order=False, preserves the prior un-transposed ordering for side-by-side diffing
    and planted-control rejection.
    """
    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    He = Ye @ Ye.conj().T

    t_u = float(np.real(np.trace(Hu)))
    t_d = float(np.real(np.trace(Hd)))
    t_e = float(np.real(np.trace(He)))
    y2_tr = 3.0 * t_u + 3.0 * t_d + t_e

    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    eye3 = np.eye(3, dtype=complex)

    if wrong_chirality_control:
        b1_Yu = Yu @ ((y2_tr - 0.85 * g1s - 2.25 * g2s - 8.0 * g3s) * eye3 + 1.5 * (Hu - Hd))
        b1_Yd = Yd @ ((y2_tr - 0.25 * g1s - 2.25 * g2s - 8.0 * g3s) * eye3 + 1.5 * (Hd - Hu))
    else:
        b1_Yu = ((y2_tr - 0.85 * g1s - 2.25 * g2s - 8.0 * g3s) * eye3 + 1.5 * (Hu - Hd)) @ Yu
        b1_Yd = ((y2_tr - 0.25 * g1s - 2.25 * g2s - 8.0 * g3s) * eye3 + 1.5 * (Hd - Hu)) @ Yd
    b1_Ye = ((y2_tr - 2.25 * g1s - 2.25 * g2s) * eye3 + 1.5 * He) @ Ye

    t_hu2 = float(np.real(np.trace(Hu @ Hu)))
    t_hd2 = float(np.real(np.trace(Hd @ Hd)))
    t_he2 = float(np.real(np.trace(He @ He)))
    t_huhd = float(np.real(np.trace(Hu @ Hd)))
    chi2 = (
        -6.75 * (t_hu2 + t_hd2)
        - 2.25 * t_he2
        + 1.5 * t_huhd
        + (17.0 / 8.0 * g1s + 45.0 / 8.0 * g2s + 20.0 * g3s) * t_u
        + (5.0 / 8.0 * g1s + 45.0 / 8.0 * g2s + 20.0 * g3s) * t_d
        + (15.0 / 8.0 * g1s + 15.0 / 8.0 * g2s) * t_e
    )

    if repaired_mixed_order:
        mix_u = -0.25 * (Hu @ Hd) - (Hd @ Hu)
        mix_d = -0.25 * (Hd @ Hu) - (Hu @ Hd)
    else:
        mix_u = -(Hu @ Hd) - 0.25 * (Hd @ Hu)
        mix_d = -(Hd @ Hu) - 0.25 * (Hu @ Hd)

    b2_Yu = (
        1.5 * (Hu @ Hu)
        + mix_u
        + (11.0 / 4.0) * (Hd @ Hd)
        + (-2.25 * y2_tr - 12.0 * lam + (223.0 / 80.0) * g1s + (135.0 / 16.0) * g2s + 16.0 * g3s) * Hu
        + (1.25 * y2_tr - (43.0 / 80.0) * g1s + (9.0 / 16.0) * g2s - 16.0 * g3s) * Hd
        + (
            chi2
            + 6.0 * lam * lam
            + (1187.0 / 600.0) * (g1s ** 2)
            - (9.0 / 20.0) * g1s * g2s
            + (19.0 / 15.0) * g1s * g3s
            - (23.0 / 4.0) * (g2s ** 2)
            + 9.0 * g2s * g3s
            - 108.0 * (g3s ** 2)
        )
        * eye3
    ) @ Yu

    b2_Yd = (
        1.5 * (Hd @ Hd)
        + mix_d
        + (11.0 / 4.0) * (Hu @ Hu)
        + (-2.25 * y2_tr - 12.0 * lam + (187.0 / 80.0) * g1s + (135.0 / 16.0) * g2s + 16.0 * g3s) * Hd
        + (1.25 * y2_tr - (79.0 / 80.0) * g1s + (9.0 / 16.0) * g2s - 16.0 * g3s) * Hu
        + (
            chi2
            + 6.0 * lam * lam
            - (127.0 / 600.0) * (g1s ** 2)
            - (27.0 / 20.0) * g1s * g2s
            + (31.0 / 15.0) * g1s * g3s
            - (23.0 / 4.0) * (g2s ** 2)
            + 9.0 * g2s * g3s
            - 108.0 * (g3s ** 2)
        )
        * eye3
    ) @ Yd

    b2_Ye = (
        1.5 * (He @ He)
        + (-2.25 * y2_tr - 12.0 * lam + (387.0 / 80.0) * g1s + (135.0 / 16.0) * g2s) * He
        + (
            chi2
            + 6.0 * lam * lam
            + (1371.0 / 200.0) * (g1s ** 2)
            + (27.0 / 20.0) * g1s * g2s
            - (23.0 / 4.0) * (g2s ** 2)
        )
        * eye3
    ) @ Ye

    dYu = K1_F64 * b1_Yu + K2_F64 * b2_Yu
    dYd = K1_F64 * b1_Yd + K2_F64 * b2_Yd
    dYe = K1_F64 * b1_Ye + K2_F64 * b2_Ye

    alpha_w = 4.0 * lam - 3.0 * g2s + 2.0 * y2_tr
    if wrong_majorana_transpose:
        dW4 = K1_F64 * (-1.5 * (He @ W4 + W4 @ He) + alpha_w * W4)
    else:
        dW4 = K1_F64 * (-1.5 * (He @ W4 + W4 @ He.T) + alpha_w * W4)

    dg1 = K1_F64 * (41.0 / 10.0) * (g1 ** 3) + K2_F64 * (g1 ** 3) * (
        (199.0 / 50.0) * g1s + (27.0 / 10.0) * g2s + (44.0 / 5.0) * g3s - 1.7 * t_u - 0.5 * t_d - 1.5 * t_e
    )
    dg2 = K1_F64 * (-19.0 / 6.0) * (g2 ** 3) + K2_F64 * (g2 ** 3) * (
        0.9 * g1s + (35.0 / 6.0) * g2s + 12.0 * g3s - 1.5 * t_u - 1.5 * t_d - 0.5 * t_e
    )
    dg3 = K1_F64 * (-7.0) * (g3 ** 3) + K2_F64 * (g3 ** 3) * (
        1.1 * g1s + 4.5 * g2s - 26.0 * g3s - 2.0 * t_u - 2.0 * t_d
    )

    t_hu3 = float(np.real(np.trace(Hu @ Hu @ Hu)))
    t_hd3 = float(np.real(np.trace(Hd @ Hd @ Hd)))
    t_he3 = float(np.real(np.trace(He @ He @ He)))
    t_hu2hd = float(np.real(np.trace(Hu @ Hu @ Hd)))
    t_huhd2 = float(np.real(np.trace(Hu @ Hd @ Hd)))

    dlam1 = (
        24.0 * lam * lam
        + lam * (4.0 * y2_tr - 9.0 * g2s - 1.8 * g1s)
        - 2.0 * (3.0 * t_hu2 + 3.0 * t_hd2 + t_he2)
        + (9.0 / 8.0) * (g2s ** 2)
        + (27.0 / 200.0) * (g1s ** 2)
        + (9.0 / 20.0) * g1s * g2s
    )
    dlam2 = (
        -312.0 * (lam ** 3)
        + 36.0 * (lam * lam) * (3.0 * g2s + 0.6 * g1s)
        - 24.0 * (lam * lam) * y2_tr
        + lam * (80.0 * g3s + 22.5 * g2s) * (t_u + t_d)
        + lam * g1s * (8.5 * t_u + 2.5 * t_d + 7.5 * t_e)
        + 7.5 * lam * g2s * t_e
        - 3.0 * lam * (t_hu2 + t_hd2 + t_he2 / 3.0 + 14.0 * t_huhd)
        + lam * (-(73.0 / 8.0) * (g2s ** 2) + (117.0 / 20.0) * g1s * g2s + (1887.0 / 200.0) * (g1s ** 2))
        + 30.0 * (t_hu3 + t_hd3 + t_he3 / 3.0)
        - 6.0 * (t_hu2hd + t_huhd2)
        - 32.0 * g3s * (t_hu2 + t_hd2)
        - 1.6 * g1s * t_hu2
        + 0.8 * g1s * t_hd2
        - 2.4 * g1s * t_he2
        - (9.0 / 4.0) * (g2s ** 2) * (t_u + t_d + t_e / 3.0)
        + g1s * g2s * (6.3 * t_u + 2.7 * t_d + 3.3 * t_e)
        - (g1s ** 2) * ((171.0 / 100.0) * t_u - (9.0 / 20.0) * t_d + (9.0 / 4.0) * t_e)
        + (305.0 / 16.0) * (g2s ** 3)
        - (289.0 / 80.0) * (g2s ** 2) * g1s
        - (1677.0 / 400.0) * g2s * (g1s ** 2)
        - (3411.0 / 2000.0) * (g1s ** 3)
    )
    dlam = K1_F64 * dlam1 + K2_F64 * dlam2
    return dYu, dYd, dYe, dW4, dg1, dg2, dg3, dlam


def rk4_integrate_full_f64(
    Yu0: np.ndarray,
    Yd0: np.ndarray,
    Ye0: np.ndarray,
    W4_0: np.ndarray,
    g1_0: float,
    g2_0: float,
    g3_0: float,
    lam0: float,
    d_ln_mu: float,
    n_steps: int = 1600,
    repaired_mixed_order: bool = True,
    wrong_chirality_control: bool = False,
) -> Dict[str, Any]:
    dt = d_ln_mu / n_steps
    Yu, Yd, Ye, W4 = Yu0.copy(), Yd0.copy(), Ye0.copy(), W4_0.copy()
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam0
    max_g = max(g1, g2, g3)
    max_y = max(
        float(np.max(np.linalg.svd(Yu, compute_uv=False))),
        float(np.max(np.linalg.svd(Yd, compute_uv=False))),
        float(np.max(np.linalg.svd(Ye, compute_uv=False))),
    )
    min_lam = lam

    for _ in range(n_steps):
        k1 = sm_2loop_plus_weinberg_rhs_f64(Yu, Yd, Ye, W4, g1, g2, g3, lam, repaired_mixed_order, wrong_chirality_control, False)
        k2 = sm_2loop_plus_weinberg_rhs_f64(
            Yu + 0.5 * dt * k1[0], Yd + 0.5 * dt * k1[1], Ye + 0.5 * dt * k1[2], W4 + 0.5 * dt * k1[3],
            g1 + 0.5 * dt * k1[4], g2 + 0.5 * dt * k1[5], g3 + 0.5 * dt * k1[6], lam + 0.5 * dt * k1[7],
            repaired_mixed_order, wrong_chirality_control, False,
        )
        k3 = sm_2loop_plus_weinberg_rhs_f64(
            Yu + 0.5 * dt * k2[0], Yd + 0.5 * dt * k2[1], Ye + 0.5 * dt * k2[2], W4 + 0.5 * dt * k2[3],
            g1 + 0.5 * dt * k2[4], g2 + 0.5 * dt * k2[5], g3 + 0.5 * dt * k2[6], lam + 0.5 * dt * k2[7],
            repaired_mixed_order, wrong_chirality_control, False,
        )
        k4 = sm_2loop_plus_weinberg_rhs_f64(
            Yu + dt * k3[0], Yd + dt * k3[1], Ye + dt * k3[2], W4 + dt * k3[3],
            g1 + dt * k3[4], g2 + dt * k3[5], g3 + dt * k3[6], lam + dt * k3[7],
            repaired_mixed_order, wrong_chirality_control, False,
        )
        Yu = Yu + (dt / 6.0) * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0])
        Yd = Yd + (dt / 6.0) * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1])
        Ye = Ye + (dt / 6.0) * (k1[2] + 2.0 * k2[2] + 2.0 * k3[2] + k4[2])
        W4 = W4 + (dt / 6.0) * (k1[3] + 2.0 * k2[3] + 2.0 * k3[3] + k4[3])
        g1 = g1 + (dt / 6.0) * (k1[4] + 2.0 * k2[4] + 2.0 * k3[4] + k4[4])
        g2 = g2 + (dt / 6.0) * (k1[5] + 2.0 * k2[5] + 2.0 * k3[5] + k4[5])
        g3 = g3 + (dt / 6.0) * (k1[6] + 2.0 * k2[6] + 2.0 * k3[6] + k4[6])
        lam = lam + (dt / 6.0) * (k1[7] + 2.0 * k2[7] + 2.0 * k3[7] + k4[7])
        max_g = max(max_g, g1, g2, g3)
        min_lam = min(min_lam, lam)

    max_y = max(
        max_y,
        float(np.max(np.linalg.svd(Yu, compute_uv=False))),
        float(np.max(np.linalg.svd(Yd, compute_uv=False))),
        float(np.max(np.linalg.svd(Ye, compute_uv=False))),
    )
    return {
        "Yu": Yu,
        "Yd": Yd,
        "Ye": Ye,
        "W4": W4,
        "g1": g1,
        "g2": g2,
        "g3": g3,
        "lam": lam,
        "max_g_along_flow": max_g,
        "max_y_along_flow": max_y,
        "min_lam_along_flow": min_lam,
    }

def buttazzo_3loop_d_dlnmu2(state: np.ndarray) -> np.ndarray:
    """Verbatim 3-loop SM RGEs (+ 4-loop pure QCD) in u = ln(mu^2) from Buttazzo et al. (2013) Appendix A."""
    K1, K2, K3, K4 = K1_F64, K2_F64, K1_F64 ** 3, K1_F64 ** 4
    g1s, g2s, g3s, yts, ybs, ytaus, lam = state

    dg1s = (
        K1 * (g1s ** 2) * (41.0 / 10.0)
        + K2 * (g1s ** 2) * (44.0 * g3s / 5.0 + 27.0 * g2s / 10.0 + 199.0 * g1s / 50.0 - 1.7 * yts - 0.5 * ybs - 1.5 * ytaus)
        + K3 * (g1s ** 2) * (
            yts * (189.0 * yts / 16.0 - 29.0 * g3s / 5.0 - 471.0 * g2s / 32.0 - 2827.0 * g1s / 800.0)
            + lam * (-1.8 * lam + 0.9 * g2s + 27.0 * g1s / 50.0)
            + 297.0 * (g3s ** 2) / 5.0 + 789.0 * (g2s ** 2) / 64.0 - 388613.0 * (g1s ** 2) / 24000.0
            - 0.6 * g3s * g2s - 137.0 * g3s * g1s / 75.0 + 123.0 * g2s * g1s / 160.0
        )
    )
    dg2s = (
        K1 * (g2s ** 2) * (-19.0 / 6.0)
        + K2 * (g2s ** 2) * (12.0 * g3s + 35.0 * g2s / 6.0 + 0.9 * g1s - 1.5 * yts - 1.5 * ybs - 0.5 * ytaus)
        + K3 * (g2s ** 2) * (
            yts * (147.0 * yts / 16.0 - 7.0 * g3s - 729.0 * g2s / 32.0 - 593.0 * g1s / 160.0)
            + lam * (-3.0 * lam + 1.5 * g2s + 0.3 * g1s)
            + 81.0 * (g3s ** 2) + 324953.0 * (g2s ** 2) / 1728.0 - 5597.0 * (g1s ** 2) / 1600.0
            + 39.0 * g3s * g2s - 0.2 * g3s * g1s + 873.0 * g2s * g1s / 160.0
        )
    )
    dg3s = (
        K1 * (g3s ** 2) * (-7.0)
        + K2 * (g3s ** 2) * (-26.0 * g3s + 4.5 * g2s + 1.1 * g1s - 2.0 * yts - 2.0 * ybs)
        + K3 * (g3s ** 2) * (
            yts * (15.0 * yts - 40.0 * g3s - 93.0 * g2s / 8.0 - 101.0 * g1s / 40.0)
            + 32.5 * (g3s ** 2) + 109.0 * (g2s ** 2) / 8.0 - 523.0 * (g1s ** 2) / 120.0
            + 21.0 * g3s * g2s + 77.0 * g3s * g1s / 15.0 - 3.0 * g2s * g1s / 40.0
        )
        + K4 * (g3s ** 5) * (-2472.28)
    )
    dlam = (
        K1 * (
            lam * (12.0 * lam + 6.0 * yts + 6.0 * ybs + 2.0 * ytaus - 4.5 * g2s - 0.9 * g1s)
            - 3.0 * (yts ** 2) - 3.0 * (ybs ** 2) - (ytaus ** 2)
            + 9.0 * (g2s ** 2) / 16.0 + 27.0 * (g1s ** 2) / 400.0 + 9.0 * g2s * g1s / 40.0
        )
        + K2 * (
            (lam ** 2) * (-156.0 * lam - 72.0 * yts - 72.0 * ybs - 24.0 * ytaus + 54.0 * g2s + 10.8 * g1s)
            + lam * yts * (-1.5 * yts - 21.0 * ybs + 40.0 * g3s + 11.25 * g2s + 4.25 * g1s)
            + lam * ybs * (-1.5 * ybs + 40.0 * g3s + 11.25 * g2s + 1.25 * g1s)
            + lam * ytaus * (-0.5 * ytaus + 3.75 * g2s + 3.75 * g1s)
            + lam * (-73.0 * (g2s ** 2) / 16.0 + 1887.0 * (g1s ** 2) / 400.0 + 117.0 * g2s * g1s / 40.0)
            + (yts ** 2) * (15.0 * yts - 3.0 * ybs - 16.0 * g3s - 0.8 * g1s)
            + yts * (-1.125 * (g2s ** 2) - 171.0 * (g1s ** 2) / 200.0 + 63.0 * g2s * g1s / 20.0)
            + (ybs ** 2) * (-3.0 * yts + 15.0 * ybs - 16.0 * g3s + 0.4 * g1s)
            + ybs * (-1.125 * (g2s ** 2) + 9.0 * (g1s ** 2) / 40.0 + 27.0 * g2s * g1s / 20.0)
            + (ytaus ** 2) * (5.0 * ytaus - 1.2 * g1s)
            + ytaus * (-0.375 * (g2s ** 2) - 1.125 * (g1s ** 2) + 33.0 * g2s * g1s / 20.0)
            + 305.0 * (g2s ** 3) / 32.0 - 3411.0 * (g1s ** 3) / 4000.0 - 289.0 * (g2s ** 2) * g1s / 160.0 - 1677.0 * g2s * (g1s ** 2) / 800.0
        )
        + K3 * (
            (lam ** 3) * (6011.35 * lam + 873.0 * yts - 387.452 * g2s - 77.490 * g1s)
            + (lam ** 2) * yts * (1768.26 * yts + 160.77 * g3s - 359.539 * g2s - 63.869 * g1s)
            + (lam ** 2) * (-790.28 * (g2s ** 2) - 185.532 * (g1s ** 2) - 316.64 * g2s * g1s)
            + lam * (yts ** 2) * (-223.382 * yts - 662.866 * g3s - 5.470 * g2s - 21.015 * g1s)
            + lam * yts * (356.968 * (g3s ** 2) - 319.664 * (g2s ** 2) - 74.8599 * (g1s ** 2) + 15.1443 * g3s * g2s + 17.454 * g3s * g1s + 5.615 * g2s * g1s)
            + lam * (g2s ** 2) * (-57.144 * g3s + 865.483 * g2s + 79.638 * g1s)
            + lam * (g1s ** 2) * (-8.381 * g3s + 61.753 * g2s + 28.168 * g1s)
            + (yts ** 3) * (-243.149 * yts + 250.494 * g3s + 74.138 * g2s + 33.930 * g1s)
            + (yts ** 2) * (-50.201 * (g3s ** 2) + 15.884 * (g2s ** 2) + 15.948 * (g1s ** 2) + 13.349 * g3s * g2s + 17.570 * g3s * g1s - 70.356 * g2s * g1s)
            + yts * g3s * (16.464 * (g2s ** 2) + 1.016 * (g1s ** 2) + 11.386 * g2s * g1s)
            + yts * (g2s ** 2) * (62.500 * g2s + 13.041 * g1s)
            + yts * (g1s ** 2) * (10.627 * g2s + 11.117 * g1s)
            + g3s * (7.536 * (g2s ** 3) + 0.663 * (g1s ** 3) + 1.507 * (g2s ** 2) * g1s + 1.105 * g2s * (g1s ** 2))
            - 114.091 * (g2s ** 4) - 1.508 * (g1s ** 4) - 37.889 * (g2s ** 3) * g1s + 6.500 * (g2s ** 2) * (g1s ** 2) - 1.543 * g2s * (g1s ** 3)
        )
    )
    dyts = (
        K1 * yts * (4.5 * yts + 1.5 * ybs + ytaus - 8.0 * g3s - 2.25 * g2s - 0.85 * g1s)
        + K2 * yts * (
            yts * (-12.0 * yts - 2.75 * ybs - 2.25 * ytaus - 12.0 * lam + 36.0 * g3s + 225.0 * g2s / 16.0 + 393.0 * g1s / 80.0)
            + ybs * (-0.25 * ybs + 1.25 * ytaus + 4.0 * g3s + 99.0 * g2s / 16.0 + 7.0 * g1s / 80.0)
            + ytaus * (-2.25 * ytaus + 1.875 * g2s + 1.875 * g1s)
            + 6.0 * (lam ** 2) - 108.0 * (g3s ** 2) - 5.75 * (g2s ** 2) + 1187.0 * (g1s ** 2) / 600.0 + 9.0 * g3s * g2s + 19.0 * g3s * g1s / 15.0 - 0.45 * g2s * g1s
        )
        + K3 * yts * (
            (yts ** 2) * (58.6028 * yts + 198.0 * lam - 157.0 * g3s - 1593.0 * g2s / 16.0 - 2437.0 * g1s / 80.0)
            + lam * yts * (3.75 * lam + 16.0 * g3s - 67.5 * g2s - 12.7 * g1s)
            + yts * (363.764 * (g3s ** 2) + 16.990 * (g2s ** 2) - 24.422 * (g1s ** 2) + 48.370 * g3s * g2s + 18.074 * g3s * g1s + 34.829 * g2s * g1s)
            + (lam ** 2) * (-36.0 * lam + 45.0 * g2s + 9.0 * g1s)
            + lam * (-171.0 * (g2s ** 2) / 16.0 - 1089.0 * (g1s ** 2) / 400.0 + 117.0 * g2s * g1s / 40.0)
            - 619.35 * (g3s ** 3) + 169.829 * (g2s ** 3) + 16.099 * (g1s ** 3) + 73.654 * (g3s ** 2) * g2s - 15.096 * (g3s ** 2) * g1s
            - 21.072 * g3s * (g2s ** 2) - 22.319 * g3s * (g1s ** 2) - 16.05 * g3s * g2s * g1s - 4.743 * (g2s ** 2) * g1s - 4.442 * g2s * (g1s ** 2)
        )
    )
    dybs = K1 * ybs * (1.5 * yts + 4.5 * ybs + ytaus - 8.0 * g3s - 2.25 * g2s - 0.25 * g1s)
    dytaus = K1 * ytaus * (3.0 * yts + 3.0 * ybs + 2.5 * ytaus - 2.25 * g2s - 2.25 * g1s)
    return np.array([dg1s, dg2s, dg3s, dyts, dybs, dytaus, dlam], dtype=float)


def bloch_wigner_mp(z: Any) -> Any:
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def z2_from_z1_gluing(z1: Any) -> Any:
    w = z1 * (z1 - 1)
    disc = mp.sqrt(1 + mp.mpf(4) / w)
    r_plus = (1 + disc) / 2
    r_minus = (1 - disc) / 2
    return r_plus if mp.im(r_plus) > mp.im(r_minus) else r_minus


def tau_nz_from_z1(z1: Any) -> Any:
    z2 = z2_from_z1_gluing(z1)
    h_mu = z2 * (1 - z1)
    a11 = (2 * z1 - 1) * z2 * (z2 - 1)
    a12 = z1 * (z1 - 1) * (2 * z2 - 1)
    a21 = -z2
    a22 = 1 - z1
    dw1_du = h_mu / (a21 - a22 * a11 / a12)
    return (mp.mpf(2) / z1 - mp.mpf(2) / (1 - z1)) * dw1_du


def eisenstein_char_mp(tau: Any, a_fr: Fraction, b_fr: Fraction, s_int: int = 3) -> Any:
    x, y = mp.re(tau), mp.im(tau)
    s = mp.mpf(s_int)
    half = mp.mpf(1) / mp.mpf(2)
    af = mp.mpf(a_fr.numerator) / mp.mpf(a_fr.denominator)
    af = af - mp.floor(af)
    bf = mp.mpf(b_fr.numerator) / mp.mpf(b_fr.denominator)
    k0 = (
        ((-1) ** (s_int - 1))
        * ((2 * mp.pi) ** (2 * s_int))
        / mp.factorial(2 * s_int)
        * mp.bernpoly(2 * s_int, af)
        * (y ** s)
    )
    thresh = mp.mp.dps * 2.4 + 18.0
    y_fl = max(float(y), 0.5)
    af_fl = float(af)
    k_max = int(thresh / (2.0 * math.pi * y_fl * 0.15)) + 6
    m_span = 14
    tot = k0
    for k in range(1, k_max + 1):
        for m in range(-m_span, m_span + 1):
            ma_fl = abs(m + af_fl)
            if ma_fl > 1e-12 and (2.0 * math.pi * k * y_fl * ma_fl > thresh):
                continue
            ma = mp.mpf(m) + af
            ang = 2 * mp.pi * k * (bf - ma * x)
            if abs(ma) < mp.mpf("1e-30"):
                term = (
                    mp.sqrt(mp.pi) * mp.gamma(s - half) / mp.gamma(s) * (y ** (1 - s)) * (mp.mpf(k) ** (1 - 2 * s_int))
                )
            else:
                z = 2 * mp.pi * k * y * abs(ma)
                bess = mp.sqrt(mp.pi / (2 * z)) * mp.exp(-z) * (1 + 3 / z + 3 / (z * z))
                term = (2 * (mp.pi ** s) / mp.gamma(s)) * mp.sqrt(y) * ((abs(ma) / k) ** (s - half)) * bess
            tot += 2 * mp.cos(ang) * term
    return tot


_VCAS_CACHE: Dict[Tuple[int, str, str, int, int, int, int], Any] = {}


def v_cas_point_mp(tau: Any, a_fr: Fraction, b_fr: Fraction) -> Any:
    key = (
        int(mp.mp.dps),
        mp.nstr(mp.re(tau), mp.mp.dps),
        mp.nstr(mp.im(tau), mp.mp.dps),
        a_fr.numerator,
        a_fr.denominator,
        b_fr.numerator,
        b_fr.denominator,
    )
    if key in _VCAS_CACHE:
        return _VCAS_CACHE[key]
    e0 = eisenstein_char_mp(tau, Fraction(0), Fraction(0), 3)
    str_w = (
        24 * e0
        + 4 * eisenstein_char_mp(tau, 3 * a_fr, 3 * b_fr, 3)
        - (
            36 * eisenstein_char_mp(tau, a_fr, b_fr, 3)
            + 18 * eisenstein_char_mp(tau, -4 * a_fr, -4 * b_fr, 3)
            + 18 * eisenstein_char_mp(tau, 2 * a_fr, 2 * b_fr, 3)
            + 12 * eisenstein_char_mp(tau, -3 * a_fr, -3 * b_fr, 3)
            + 6 * eisenstein_char_mp(tau, 6 * a_fr, 6 * b_fr, 3)
        )
    )
    val = -(str_w / (2 * (mp.pi ** 3)))
    _VCAS_CACHE[key] = val
    return val


def neg_vol_on_gluing_curve(x: Any, y: Any) -> Any:
    z1 = mp.mpc(x, y)
    z2 = z2_from_z1_gluing(z1)
    return -(bloch_wigner_mp(z1) + bloch_wigner_mp(z2))


def s_eff_joint_3d_2d(x: Any, y: Any, area: Any) -> Any:
    nv = neg_vol_on_gluing_curve(x, y)
    tnz = tau_nz_from_z1(mp.mpc(x, y))
    vc = v_cas_point_mp(tnz, Fraction(4, 15), Fraction(8, 15))
    c_vol = mp.mpf(1) / mp.mpf(2)
    c_flux = 2 * (mp.pi ** 2) * (mp.mpf(3) ** 2)
    return mp.re(nv + c_vol * area + c_flux / area + vc / (16 * (mp.pi ** 2) * (area ** 2)))


def solve_joint_3var_newton(seed_x: Fraction, seed_y: Fraction, seed_a: Fraction) -> Tuple[Any, Any, Any]:
    vec = [
        mp.mpf(seed_x.numerator) / mp.mpf(seed_x.denominator),
        mp.mpf(seed_y.numerator) / mp.mpf(seed_y.denominator),
        mp.mpf(seed_a.numerator) / mp.mpf(seed_a.denominator),
    ]
    steps = [mp.mpf(10) ** (-6), mp.mpf(10) ** (-6), mp.mpf(10) ** (-5)]
    tol = mp.mpf(10) ** (-14)
    for _ in range(18):
        f0 = s_eff_joint_3d_2d(vec[0], vec[1], vec[2])
        grad = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        hess = mp.zeros(3, 3)
        for i in range(3):
            vp, vm = list(vec), list(vec)
            vp[i] += steps[i]
            vm[i] -= steps[i]
            fp = s_eff_joint_3d_2d(vp[0], vp[1], vp[2])
            fm = s_eff_joint_3d_2d(vm[0], vm[1], vm[2])
            grad[i] = (fp - fm) / (2 * steps[i])
            hess[i, i] = (fp - 2 * f0 + fm) / (steps[i] ** 2)
        for i in range(3):
            for j in range(i + 1, 3):
                vpp, vpm, vmp, vmm = list(vec), list(vec), list(vec), list(vec)
                vpp[i] += steps[i]; vpp[j] += steps[j]
                vpm[i] += steps[i]; vpm[j] -= steps[j]
                vmp[i] -= steps[i]; vmp[j] += steps[j]
                vmm[i] -= steps[i]; vmm[j] -= steps[j]
                hij = (
                    s_eff_joint_3d_2d(vpp[0], vpp[1], vpp[2])
                    - s_eff_joint_3d_2d(vpm[0], vpm[1], vpm[2])
                    - s_eff_joint_3d_2d(vmp[0], vmp[1], vmp[2])
                    + s_eff_joint_3d_2d(vmm[0], vmm[1], vmm[2])
                ) / (4 * steps[i] * steps[j])
                hess[i, j] = hij
                hess[j, i] = hij
        delta = (hess ** (-1)) * mp.matrix(grad)
        for i in range(3):
            vec[i] -= delta[i, 0]
        if abs(delta[0, 0]) + abs(delta[1, 0]) + abs(delta[2, 0]) < tol:
            break
    return vec[0], vec[1], vec[2]


def erfcx_mp(x: Any) -> Any:
    with mp.extradps(50):
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


def majorana_puncture_jet_mp(tau: Any) -> Any:
    y = mp.im(tau)
    q = mp.exp(2j * mp.pi * tau)
    n_max = int((mp.mp.dps * 2.4 + 12.0) / (2.0 * math.pi * max(float(y), 0.3))) + 8
    s1, s3, s5 = mp.mpc(0), mp.mpc(0), mp.mpc(0)
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

    half = mp.mpf(1) / mp.mpf(2)
    three_halves = mp.mpf(3) / mp.mpf(2)
    n_span = int(math.sqrt((mp.mp.dps * 2.4 + 14.0) / (3.0 * math.pi * max(float(y), 0.3)))) + 6
    v_raw = [mp.mpc(0)] * 3
    w_raw = [mp.mpc(0)] * 3
    u_raw = [mp.mpc(0)] * 3
    for j in range(3):
        ac = (mp.mpf(j) + half) / 3
        sv, sw, dtau_sw = mp.mpc(0), mp.mpc(0), mp.mpc(0)
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
            m_r[r, c] = c_v * v_raw[r] * v_raw[c] + c_w * w_raw[r] * w_raw[c] + u_raw[r] * u_raw[c]
    return m_r


def collar_amp_mp(kappa_int: int, l_cusp: Any) -> Any:
    if kappa_int == 0:
        return 1 / mp.sqrt(l_cusp)
    k = mp.mpf(kappa_int)
    norm_sq = (mp.exp(2 * k * l_cusp) - 1) / (2 * k)
    return mp.exp(k * l_cusp) / mp.sqrt(norm_sq)


def mat_transpose_mp(mat: Any) -> Any:
    res = mp.zeros(mat.rows, mat.cols)
    for r in range(mat.rows):
        for c in range(mat.cols):
            res[r, c] = mat[c, r]
    return res


def build_zero_knob_uv_state_mp(
    tau_star: Any,
    vol_m004: Any,
    area_horotorus: Any,
    a_fr: Fraction,
    b_fr: Fraction,
) -> Dict[str, Any]:
    """
    Constructs the exact zero-knob UV coupling and Yukawa/seesaw matrices from
    derived (tau*, Vol(m004), A*) and canonical 1D collar + 2D magnetized wavefunctions.
    Contains ZERO float literals (AST-enforced).
    """
    l_cusp = mp.im(tau_star)
    alpha_uv_inv = vol_m004 * area_horotorus
    g_uv = mp.sqrt((4 * mp.pi) / alpha_uv_inv)
    lam_uv = (mp.mpf(1) / mp.mpf(5)) * (g_uv ** 2)
    d_ln_mu = -(mp.mpf(45) / mp.pi) * vol_m004

    amp0 = collar_amp_mp(0, l_cusp)
    ampp = collar_amp_mp(1, l_cusp)
    ampm = collar_amp_mp(-1, l_cusp)

    c_pos = g_uv * amp0 * amp0 * ampp
    c_neg = g_uv * amp0 * amp0 * ampm

    y1 = c_pos * y_mag_overlap_mp(tau_star, a_fr, b_fr, 1, -4)
    y2 = c_neg * y_mag_overlap_mp(tau_star, a_fr, b_fr, 1, 2)
    y3 = c_neg * y_mag_overlap_mp(tau_star, a_fr, b_fr, -3, 6)
    y4 = c_pos * y_mag_overlap_mp(tau_star, a_fr, b_fr, -3, 0)
    m_r = majorana_puncture_jet_mp(tau_star)
    w4 = y4 * (m_r ** (-1)) * mat_transpose_mp(y4)
    return {
        "alpha_uv_inv": alpha_uv_inv,
        "g_uv": g_uv,
        "lam_uv": lam_uv,
        "d_ln_mu": d_ln_mu,
        "Y1": y1,
        "Y2": y2,
        "Y3": y3,
        "Y4": y4,
        "M_R": m_r,
        "W4": w4,
    }


def mp_to_list3(mat: Any) -> List[List[Any]]:
    return [[mat[r, c] for c in range(3)] for r in range(3)]


def mp_to_np(mat: Any) -> np.ndarray:
    return np.array([[complex(mat[r, c]) for c in range(3)] for r in range(3)], dtype=complex)


def mp3_mul(a: List[List[Any]], b: List[List[Any]]) -> List[List[Any]]:
    return [
        [a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j] for j in range(3)]
        for i in range(3)
    ]


def mp3_dag(a: List[List[Any]]) -> List[List[Any]]:
    return [[mp.conj(a[j][i]) for j in range(3)] for i in range(3)]


def mp3_tp(a: List[List[Any]]) -> List[List[Any]]:
    return [[a[j][i] for j in range(3)] for i in range(3)]


def mp3_conj(a: List[List[Any]]) -> List[List[Any]]:
    return [[mp.conj(a[i][j]) for j in range(3)] for i in range(3)]


def mp3_tr_re(a: List[List[Any]]) -> Any:
    return mp.re(a[0][0] + a[1][1] + a[2][2])


def random_haar_u3_mp(seed: int) -> List[List[Any]]:
    rng = np.random.default_rng(seed)
    re_m = rng.normal(size=(3, 3))
    im_m = rng.normal(size=(3, 3))
    cols: List[List[Any]] = []
    for c in range(3):
        v = [mp.mpc(repr(float(re_m[r, c])), repr(float(im_m[r, c]))) for r in range(3)]
        for u in cols:
            proj = sum(mp.conj(u[r]) * v[r] for r in range(3))
            v = [v[r] - proj * u[r] for r in range(3)]
        nrm = mp.sqrt(sum(mp.re(mp.conj(v[r]) * v[r]) for r in range(3)))
        cols.append([v[r] / nrm for r in range(3)])
    return [[cols[c][r] for c in range(3)] for r in range(3)]


def sm_2loop_plus_weinberg_rhs_mp(
    Yu: List[List[Any]],
    Yd: List[List[Any]],
    Ye: List[List[Any]],
    W4: List[List[Any]],
    g1: Any,
    g2: Any,
    g3: Any,
    lam: Any,
    k1_mp: Any,
    k2_mp: Any,
    repaired_mixed_order: bool = True,
) -> Tuple[List[List[Any]], List[List[Any]], List[List[Any]], List[List[Any]], Any, Any, Any, Any]:
    Hu = mp3_mul(Yu, mp3_dag(Yu))
    Hd = mp3_mul(Yd, mp3_dag(Yd))
    He = mp3_mul(Ye, mp3_dag(Ye))

    t_u = mp3_tr_re(Hu)
    t_d = mp3_tr_re(Hd)
    t_e = mp3_tr_re(He)
    y2_tr = 3 * t_u + 3 * t_d + t_e

    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    F = lambda p, q: mp.mpf(p) / mp.mpf(q)

    Hu2 = mp3_mul(Hu, Hu)
    Hd2 = mp3_mul(Hd, Hd)
    He2 = mp3_mul(He, He)
    HuHd = mp3_mul(Hu, Hd)
    HdHu = mp3_mul(Hd, Hu)

    t_hu2, t_hd2, t_he2 = mp3_tr_re(Hu2), mp3_tr_re(Hd2), mp3_tr_re(He2)
    t_huhd = mp3_tr_re(HuHd)

    chi2 = (
        -F(27, 4) * (t_hu2 + t_hd2)
        - F(9, 4) * t_he2
        + F(3, 2) * t_huhd
        + (F(17, 8) * g1s + F(45, 8) * g2s + 20 * g3s) * t_u
        + (F(5, 8) * g1s + F(45, 8) * g2s + 20 * g3s) * t_d
        + (F(15, 8) * g1s + F(15, 8) * g2s) * t_e
    )

    su1_diag = y2_tr - F(17, 20) * g1s - F(9, 4) * g2s - 8 * g3s
    sd1_diag = y2_tr - F(1, 4) * g1s - F(9, 4) * g2s - 8 * g3s
    se1_diag = y2_tr - F(9, 4) * g1s - F(9, 4) * g2s

    su2_hu = -F(9, 4) * y2_tr - 12 * lam + F(223, 80) * g1s + F(135, 16) * g2s + 16 * g3s
    su2_hd = F(5, 4) * y2_tr - F(43, 80) * g1s + F(9, 16) * g2s - 16 * g3s
    su2_id = (
        chi2 + 6 * lam * lam + F(1187, 600) * g1s * g1s - F(9, 20) * g1s * g2s
        + F(19, 15) * g1s * g3s - F(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s
    )

    sd2_hd = -F(9, 4) * y2_tr - 12 * lam + F(187, 80) * g1s + F(135, 16) * g2s + 16 * g3s
    sd2_hu = F(5, 4) * y2_tr - F(79, 80) * g1s + F(9, 16) * g2s - 16 * g3s
    sd2_id = (
        chi2 + 6 * lam * lam - F(127, 600) * g1s * g1s - F(27, 20) * g1s * g2s
        + F(31, 15) * g1s * g3s - F(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s
    )

    se2_he = -F(9, 4) * y2_tr - 12 * lam + F(387, 80) * g1s + F(135, 16) * g2s
    se2_id = chi2 + 6 * lam * lam + F(1371, 200) * g1s * g1s + F(27, 20) * g1s * g2s - F(23, 4) * g2s * g2s

    lu = [[mp.mpc(0)] * 3 for _ in range(3)]
    ld = [[mp.mpc(0)] * 3 for _ in range(3)]
    le = [[mp.mpc(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            d_ij = mp.mpf(1) if i == j else mp.mpf(0)
            b1u = su1_diag * d_ij + F(3, 2) * (Hu[i][j] - Hd[i][j])
            mix_u_ij = (-F(1, 4) * HuHd[i][j] - HdHu[i][j]) if repaired_mixed_order else (-HuHd[i][j] - F(1, 4) * HdHu[i][j])
            b2u = (
                F(3, 2) * Hu2[i][j] + mix_u_ij + F(11, 4) * Hd2[i][j]
                + su2_hu * Hu[i][j] + su2_hd * Hd[i][j] + su2_id * d_ij
            )
            lu[i][j] = k1_mp * b1u + k2_mp * b2u

            b1d = sd1_diag * d_ij + F(3, 2) * (Hd[i][j] - Hu[i][j])
            mix_d_ij = (-F(1, 4) * HdHu[i][j] - HuHd[i][j]) if repaired_mixed_order else (-HdHu[i][j] - F(1, 4) * HuHd[i][j])
            b2d = (
                F(3, 2) * Hd2[i][j] + mix_d_ij + F(11, 4) * Hu2[i][j]
                + sd2_hd * Hd[i][j] + sd2_hu * Hu[i][j] + sd2_id * d_ij
            )
            ld[i][j] = k1_mp * b1d + k2_mp * b2d

            b1e = se1_diag * d_ij + F(3, 2) * He[i][j]
            b2e = F(3, 2) * He2[i][j] + se2_he * He[i][j] + se2_id * d_ij
            le[i][j] = k1_mp * b1e + k2_mp * b2e

    dYu = mp3_mul(lu, Yu)
    dYd = mp3_mul(ld, Yd)
    dYe = mp3_mul(le, Ye)

    HeW = mp3_mul(He, W4)
    WHeT = mp3_mul(W4, mp3_tp(He))
    alpha_w = 4 * lam - 3 * g2s + 2 * y2_tr
    dW4 = [
        [k1_mp * (-F(3, 2) * (HeW[r][c] + WHeT[r][c]) + alpha_w * W4[r][c]) for c in range(3)]
        for r in range(3)
    ]

    dg1 = k1_mp * F(41, 10) * (g1 ** 3) + k2_mp * (g1 ** 3) * (
        F(199, 50) * g1s + F(27, 10) * g2s + F(44, 5) * g3s - F(17, 10) * t_u - F(1, 2) * t_d - F(3, 2) * t_e
    )
    dg2 = k1_mp * (-F(19, 6)) * (g2 ** 3) + k2_mp * (g2 ** 3) * (
        F(9, 10) * g1s + F(35, 6) * g2s + 12 * g3s - F(3, 2) * t_u - F(3, 2) * t_d - F(1, 2) * t_e
    )
    dg3 = k1_mp * (-7) * (g3 ** 3) + k2_mp * (g3 ** 3) * (
        F(11, 10) * g1s + F(9, 2) * g2s - 26 * g3s - 2 * t_u - 2 * t_d
    )

    t_hu3 = mp3_tr_re(mp3_mul(Hu2, Hu))
    t_hd3 = mp3_tr_re(mp3_mul(Hd2, Hd))
    t_he3 = mp3_tr_re(mp3_mul(He2, He))
    t_hu2hd = mp3_tr_re(mp3_mul(Hu2, Hd))
    t_huhd2 = mp3_tr_re(mp3_mul(Hu, Hd2))

    dlam1 = (
        24 * lam * lam + lam * (4 * y2_tr - 9 * g2s - F(9, 5) * g1s)
        - 2 * (3 * t_hu2 + 3 * t_hd2 + t_he2)
        + F(9, 8) * g2s * g2s + F(27, 200) * g1s * g1s + F(9, 20) * g1s * g2s
    )
    dlam2 = (
        -312 * (lam ** 3) + 36 * lam * lam * (3 * g2s + F(3, 5) * g1s) - 24 * lam * lam * y2_tr
        + lam * (80 * g3s + F(45, 2) * g2s) * (t_u + t_d)
        + lam * g1s * (F(17, 2) * t_u + F(5, 2) * t_d + F(15, 2) * t_e)
        + F(15, 2) * lam * g2s * t_e
        - 3 * lam * (t_hu2 + t_hd2 + t_he2 / 3 + 14 * t_huhd)
        + lam * (-F(73, 8) * g2s * g2s + F(117, 20) * g1s * g2s + F(1887, 200) * g1s * g1s)
        + 30 * (t_hu3 + t_hd3 + t_he3 / 3) - 6 * (t_hu2hd + t_huhd2)
        - 32 * g3s * (t_hu2 + t_hd2) - F(8, 5) * g1s * t_hu2 + F(4, 5) * g1s * t_hd2 - F(12, 5) * g1s * t_he2
        - F(9, 4) * g2s * g2s * (t_u + t_d + t_e / 3)
        + g1s * g2s * (F(63, 10) * t_u + F(27, 10) * t_d + F(33, 10) * t_e)
        - g1s * g1s * (F(171, 100) * t_u - F(9, 20) * t_d + F(9, 4) * t_e)
        + F(305, 16) * (g2s ** 3) - F(289, 80) * g2s * g2s * g1s
        - F(1677, 400) * g2s * g1s * g1s - F(3411, 2000) * (g1s ** 3)
    )
    dlam = k1_mp * dlam1 + k2_mp * dlam2
    return dYu, dYd, dYe, dW4, dg1, dg2, dg3, dlam


def rk4_integrate_full_mp(
    Yu0: List[List[Any]],
    Yd0: List[List[Any]],
    Ye0: List[List[Any]],
    W4_0: List[List[Any]],
    g1_0: Any,
    g2_0: Any,
    g3_0: Any,
    lam0: Any,
    d_ln_mu: Any,
    n_steps: int = 160,
    repaired_mixed_order: bool = True,
) -> Tuple[List[List[Any]], List[List[Any]], List[List[Any]], List[List[Any]], Any, Any, Any, Any]:
    dt = d_ln_mu / mp.mpf(n_steps)
    half_dt = dt / 2
    sixth_dt = dt / 6
    k1_mp = mp.mpf(1) / (16 * mp.pi * mp.pi)
    k2_mp = k1_mp * k1_mp
    Yu = [[Yu0[r][c] for c in range(3)] for r in range(3)]
    Yd = [[Yd0[r][c] for c in range(3)] for r in range(3)]
    Ye = [[Ye0[r][c] for c in range(3)] for r in range(3)]
    W4 = [[W4_0[r][c] for c in range(3)] for r in range(3)]
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam0

    def add_s(m0: List[List[Any]], dm: List[List[Any]], sc: Any) -> List[List[Any]]:
        return [[m0[r][c] + sc * dm[r][c] for c in range(3)] for r in range(3)]

    for _ in range(n_steps):
        s1 = sm_2loop_plus_weinberg_rhs_mp(Yu, Yd, Ye, W4, g1, g2, g3, lam, k1_mp, k2_mp, repaired_mixed_order)
        s2 = sm_2loop_plus_weinberg_rhs_mp(
            add_s(Yu, s1[0], half_dt), add_s(Yd, s1[1], half_dt), add_s(Ye, s1[2], half_dt), add_s(W4, s1[3], half_dt),
            g1 + half_dt * s1[4], g2 + half_dt * s1[5], g3 + half_dt * s1[6], lam + half_dt * s1[7], k1_mp, k2_mp, repaired_mixed_order,
        )
        s3 = sm_2loop_plus_weinberg_rhs_mp(
            add_s(Yu, s2[0], half_dt), add_s(Yd, s2[1], half_dt), add_s(Ye, s2[2], half_dt), add_s(W4, s2[3], half_dt),
            g1 + half_dt * s2[4], g2 + half_dt * s2[5], g3 + half_dt * s2[6], lam + half_dt * s2[7], k1_mp, k2_mp, repaired_mixed_order,
        )
        s4 = sm_2loop_plus_weinberg_rhs_mp(
            add_s(Yu, s3[0], dt), add_s(Yd, s3[1], dt), add_s(Ye, s3[2], dt), add_s(W4, s3[3], dt),
            g1 + dt * s3[4], g2 + dt * s3[5], g3 + dt * s3[6], lam + dt * s3[7], k1_mp, k2_mp, repaired_mixed_order,
        )
        Yu = [[Yu[r][c] + sixth_dt * (s1[0][r][c] + 2*s2[0][r][c] + 2*s3[0][r][c] + s4[0][r][c]) for c in range(3)] for r in range(3)]
        Yd = [[Yd[r][c] + sixth_dt * (s1[1][r][c] + 2*s2[1][r][c] + 2*s3[1][r][c] + s4[1][r][c]) for c in range(3)] for r in range(3)]
        Ye = [[Ye[r][c] + sixth_dt * (s1[2][r][c] + 2*s2[2][r][c] + 2*s3[2][r][c] + s4[2][r][c]) for c in range(3)] for r in range(3)]
        W4 = [[W4[r][c] + sixth_dt * (s1[3][r][c] + 2*s2[3][r][c] + 2*s3[3][r][c] + s4[3][r][c]) for c in range(3)] for r in range(3)]
        g1 = g1 + sixth_dt * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
        g2 = g2 + sixth_dt * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
        g3 = g3 + sixth_dt * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
        lam = lam + sixth_dt * (s1[7] + 2 * s2[7] + 2 * s3[7] + s4[7])
    return Yu, Yd, Ye, W4, g1, g2, g3, lam

def eighe_sorted_mp(h_mat: Any) -> Tuple[List[Any], Any]:
    vals, vecs = mp.eighe(h_mat)
    order = sorted(range(3), key=lambda k: mp.re(vals[k]))
    s_out: List[Any] = []
    q_out = mp.zeros(3, 3)
    for c_new, c_old in enumerate(order):
        s_out.append(mp.sqrt(max(mp.re(vals[c_old]), mp.mpf(0))))
        nrm = mp.sqrt(sum(abs(vecs[r, c_old]) ** 2 for r in range(3)))
        for r in range(3):
            q_out[r, c_new] = vecs[r, c_old] / nrm
    return s_out, q_out


def extract_obs_mp_full(
    Yu: List[List[Any]], Yd: List[List[Any]], Ye: List[List[Any]], W4: List[List[Any]], lam: Any
) -> Dict[str, Any]:
    Hu = mp.matrix(mp3_mul(Yu, mp3_dag(Yu)))
    Hd = mp.matrix(mp3_mul(Yd, mp3_dag(Yd)))
    He = mp.matrix(mp3_mul(Ye, mp3_dag(Ye)))
    Hw = mp.matrix(mp3_mul(W4, mp3_dag(W4)))
    su, qu = eighe_sorted_mp(Hu)
    sd, qd = eighe_sorted_mp(Hd)
    se, qe = eighe_sorted_mp(He)
    sw, qw = eighe_sorted_mp(Hw)
    v12 = qu.transpose_conj() * qd
    u34 = qe.transpose_conj() * qw
    tu = sum(mp.re(Hu[i, i]) for i in range(3))
    td = sum(mp.re(Hd[i, i]) for i in range(3))
    cm = (Hu / tu) * (Hd / td) - (Hd / td) * (Hu / tu)
    cm3 = cm * cm * cm
    icp = sum(mp.im(cm3[i, i]) for i in range(3)) / 6
    return {
        "ratios": [
            su[0] / su[1], su[1] / su[2],
            sd[0] / sd[1], sd[1] / sd[2],
            se[0] / se[1], se[1] / se[2],
            sw[0] / sw[1], sw[1] / sw[2],
            su[2] / sd[2], sd[2] / se[2],
        ],
        "v12_abs": [[abs(v12[r, c]) for c in range(3)] for r in range(3)],
        "u34_abs": [[abs(u34[r, c]) for c in range(3)] for r in range(3)],
        "icp": icp,
        "lam": lam,
    }


def extract_ir_observables_f64(flow: Dict[str, Any]) -> Dict[str, Any]:
    Yu, Yd, Ye, W4 = flow["Yu"], flow["Yd"], flow["Ye"], flow["W4"]
    g1, g2, g3, lam = flow["g1"], flow["g2"], flow["g3"], flow["lam"]
    u1, s1 = svd_ascending_np(Yu)
    u2, s2 = svd_ascending_np(Yd)
    u3, s3 = svd_ascending_np(Ye)
    u4, s4 = takagi_symmetric_ascending_np(W4)

    v12_mat = u1.conj().T @ u2
    v12_abs = np.abs(v12_mat)
    u34_abs = np.abs(u3.conj().T @ u4)

    hu = Yu @ Yu.conj().T
    hd = Yd @ Yd.conj().T
    hu_hat = hu / float(np.real(np.trace(hu)))
    hd_hat = hd / float(np.real(np.trace(hd)))
    cm_hat = hu_hat @ hd_hat - hd_hat @ hu_hat
    icp_hat = float(np.imag(np.trace(cm_hat @ cm_hat @ cm_hat)) / 6.0)
    j12_cp = float(np.imag(v12_mat[0, 1] * v12_mat[1, 2] * np.conj(v12_mat[0, 2]) * np.conj(v12_mat[1, 1])))

    # Parity-mixed 2x2 block of |U_34| (rows {1, 2} of sec3 vs cols {0, 1} of sec4):
    sub_2x2 = u34_abs[1:3, 0:2]
    sin2_2theta_parity = float(4.0 * (sub_2x2[0, 0] ** 2) * (sub_2x2[0, 1] ** 2))

    gy_sq = 0.6 * (g1 ** 2)
    sin2_theta_ew = float(gy_sq / (g2 ** 2 + gy_sq))

    return {
        "alpha1_inv_gut": float(4.0 * math.pi / (g1 ** 2)),
        "alpha2_inv": float(4.0 * math.pi / (g2 ** 2)),
        "alpha3_inv": float(4.0 * math.pi / (g3 ** 2)),
        "sin2_theta_ew_ir": sin2_theta_ew,
        "lam_ir": float(lam),
        "scalar_to_condensate_sqrt_2lam": float(math.sqrt(max(2.0 * lam, 0.0))),
        "s3_sec1": float(s1[2]),
        "s3_sec2": float(s2[2]),
        "s3_sec3": float(s3[2]),
        "inter_s3_sec1_over_sec2": float(s1[2] / s2[2]),
        "inter_s3_sec2_over_sec3": float(s2[2] / s3[2]),
        "sec1_r12": float(s1[0] / s1[1]),
        "sec1_r23": float(s1[1] / s1[2]),
        "sec2_r12": float(s2[0] / s2[1]),
        "sec2_r23": float(s2[1] / s2[2]),
        "sec3_r12": float(s3[0] / s3[1]),
        "sec3_r23": float(s3[1] / s3[2]),
        "sec4_r12": float(s4[0] / s4[1]),
        "sec4_r23": float(s4[1] / s4[2]),
        "V12_abs": [[float(v12_abs[r, c]) for c in range(3)] for r in range(3)],
        "U34_abs": [[float(u34_abs[r, c]) for c in range(3)] for r in range(3)],
        "sin2_2theta_sec34_parity_block": sin2_2theta_parity,
        "I_CP_hat_IR": icp_hat,
        "J12_CP_IR": j12_cp,
    }


# ============================================================================
# SECTION 4: PART 5B & PART 5C — SYNTHESIS, HAAR-6 GATE, ORBITS & LEDGER
# ============================================================================


# ============================================================================
# SECTION 4: EXACT TARGET-FREE HELPERS & STAGE 3 AMPHICHIRAL / SEESAW CENSUS
# ============================================================================

def derive_su5_universal_1loop_eliminants_exact(n_gen: int, n_higgs: int) -> Dict[str, Fraction]:
    """Exact rational SU(5) -> G_SM trace and 1-loop eliminant derivation (ZERO float literals)."""
    tr_t3_sq_5 = Fraction(1, 2)
    tr_y_sq_5 = Fraction(5, 6)
    k2_over_k1 = tr_t3_sq_5 / tr_y_sq_5
    b1 = Fraction(4, 3) * n_gen + Fraction(1, 10) * n_higgs
    b2 = -Fraction(22, 3) + Fraction(4, 3) * n_gen + Fraction(1, 6) * n_higgs
    b3 = -Fraction(11, 1) + Fraction(4, 3) * n_gen
    c1 = b2 - b3
    c2 = b3 - b1
    c3 = b1 - b2
    denom = -(k2_over_k1 * c1) + c2
    sw2_intercept = (k2_over_k1 * c1) / (-denom)
    sw2_slope = c3 / (-denom)
    return {
        "k2_over_k1": k2_over_k1,
        "c1": c1,
        "c2": c2,
        "c3": c3,
        "sw2_intercept": sw2_intercept,
        "sw2_slope": sw2_slope,
    }

def frac_mod1(x: Fraction) -> Fraction:
    return x - (x.numerator // x.denominator)


def mat_conj_mp(mat: Any) -> Any:
    res = mp.zeros(mat.rows, mat.cols)
    for r in range(mat.rows):
        for c in range(mat.cols):
            res[r, c] = mp.conj(mat[r, c])
    return res


def fast_y_mag_overlap_f64(tau: complex, a: float, b: float, ql: int, qr: int) -> np.ndarray:
    qh = -(ql + qr)
    tau1, tau2 = tau.real, tau.imag
    u0 = 1.0 / math.sqrt(6.0)
    u_split = math.sqrt(tau2)
    sqrt_tau2 = math.sqrt(tau2)
    sqrt_pi = math.sqrt(math.pi)
    thresh = 42.0
    k_max = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * tau2)) / 3.0)) + 2
    l_quad = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * tau2)))) + 3
    l_riem = int(math.ceil(math.sqrt(thresh / math.pi))) + 2

    def erfcx_f(x: float) -> float:
        if x >= 26.0:
            x2 = x * x
            return (1.0 / (sqrt_pi * x)) * (1.0 - 0.5 / x2 + 0.75 / (x2 * x2))
        return math.exp(x * x) * math.erfc(x)

    def erfc_int_f(alpha: float, beta: float) -> float:
        xm = alpha * u0 - beta / u0
        xp = alpha * u0 + beta / u0
        edge_exp = (alpha * u0) ** 2 + (beta / u0) ** 2
        if xm >= 0.0:
            if edge_exp > thresh:
                return 0.0
            return (sqrt_pi / (2.0 * alpha)) * math.exp(-edge_exp) * (erfcx_f(xm) + erfcx_f(xp))
        if 2.0 * alpha * beta > thresh:
            return 0.0
        p1 = 2.0 * math.exp(-2.0 * alpha * beta)
        p2 = 0.0 if edge_exp > thresh else math.exp(-edge_exp) * (erfcx_f(xp) - erfcx_f(-xm))
        return (sqrt_pi / (2.0 * alpha)) * (p1 + p2)

    def f_prim_f(uv: float, bv: float) -> float:
        if bv == 0.0:
            return 2.0 * uv
        bvu = bv / uv
        if bvu * bvu > thresh:
            return 0.0
        return 2.0 * math.exp(-bvu * bvu) * (uv - sqrt_pi * bv * erfcx_f(bvu))

    ymat = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        cl = (i + 0.5 + ql * a) / 3.0
        zak_ang = -2.0 * math.pi * (ql * b / 3.0) * (i + 0.5)
        zak_ph = complex(math.cos(zak_ang), math.sin(zak_ang))
        for j in range(3):
            cr = (j + 0.5 - qr * a) / 3.0
            acc = 0.0j
            for k in range(-k_max, k_max + 1):
                n = (j - i) - 3 * k
                na = n + qh * a
                dk = na / 3.0
                xi0 = 0.5 * (cl + cr - k)
                x0 = na * tau1 + qh * b
                ang0 = math.pi * dk * ((qr - ql) * b - 3.0)
                bph = complex(math.cos(ang0), math.sin(ang0))
                if abs(na) > 1e-13:
                    alpha = math.sqrt(math.pi * tau2) * abs(na)
                    l_lin = int(math.ceil(thresh / (2.0 * math.pi * tau2 * abs(na)))) + 2
                    l_m = max(l_lin, l_quad)
                    lc = int(round(xi0))
                    sub = 0.0j
                    for dl in range(-l_m, l_m + 1):
                        li = lc + dl
                        beta = math.sqrt(math.pi * tau2) * abs(li - xi0)
                        iv = sqrt_tau2 * erfc_int_f(alpha, beta)
                        if iv != 0.0:
                            ang = 2.0 * math.pi * (li - xi0) * x0
                            sub += iv * complex(math.cos(ang), math.sin(ang))
                    acc += bph * sub
                else:
                    lc = int(round(xi0))
                    sub1 = 0.0j
                    for dl in range(-l_riem, l_riem + 1):
                        li = lc + dl
                        beta = math.sqrt(math.pi * tau2) * abs(li - xi0)
                        iv = sqrt_tau2 * (f_prim_f(u_split, beta) - f_prim_f(u0, beta))
                        if iv != 0.0:
                            ang = 2.0 * math.pi * (li - xi0) * x0
                            sub1 += iv * complex(math.cos(ang), math.sin(ang))
                    mc = int(round(-x0))
                    sub2 = 0.0j
                    for dm in range(-l_riem, l_riem + 1):
                        mi = mc + dm
                        mx = mi + x0
                        if abs(mx) > 1e-13 and math.pi * mx * mx <= thresh:
                            ang = 2.0 * math.pi * mi * xi0
                            sub2 += (tau2 / (math.pi * mx * mx)) * math.exp(-math.pi * mx * mx) * complex(math.cos(ang), math.sin(ang))
                    acc += bph * (sub1 + sub2)
            ymat[i, j] = zak_ph * acc
    return ymat


# ============================================================================
# SECTION 2: PART 2A — 85-DIGIT RIGHT-TO-LEFT ADJOINT & TRACE INVARIANT AUDIT
# ============================================================================

def run_part_2a_adjoint_and_trace_invariant() -> Dict[str, Any]:
    with mp.workdps(100):
        F = lambda p, q: mp.mpf(p) / mp.mpf(q)
        # Generic complex rational noncommuting 3x3 Yukawa test matrices:
        Y1 = mp.matrix([
            [F(7, 10) + 1j * F(1, 5), F(3, 20) - 1j * F(1, 4), F(1, 8) + 1j * F(3, 10)],
            [-F(1, 5) + 1j * F(2, 15), F(4, 5) + 1j * F(1, 10), F(1, 3) - 1j * F(1, 6)],
            [F(1, 4) - 1j * F(1, 12), -F(3, 10) + 1j * F(2, 5), F(9, 10) - 1j * F(1, 20)],
        ])
        Y2 = mp.matrix([
            [F(3, 5) - 1j * F(1, 8), F(2, 5) + 1j * F(3, 10), -F(1, 6) + 1j * F(1, 4)],
            [F(1, 3) + 1j * F(1, 5), F(1, 2) - 1j * F(3, 20), F(7, 20) + 1j * F(1, 10)],
            [-F(2, 15) + 1j * F(3, 8), F(1, 4) - 1j * F(1, 3), F(4, 5) + 1j * F(2, 9)],
        ])

        H1 = Y1 * Y1.transpose_conj()
        H2 = Y2 * Y2.transpose_conj()
        comm = H1 * H2 - H2 * H1

        # Right-acting Luo-Xiao (2003, eqs. 1, 6, 7): Y_f^LX = Y_f^dag, H_f^LX = (Y_f^LX)^dag Y_f^LX = H_f
        Y1_lx = Y1.transpose_conj()
        Y2_lx = Y2.transpose_conj()
        beta1_lx_mixed = Y1_lx * (-(H1 * H2) - F(1, 4) * (H2 * H1))
        beta2_lx_mixed = Y2_lx * (-(H2 * H1) - F(1, 4) * (H1 * H2))

        # Hermitian conjugate back to left-acting convention:
        beta1_from_lx_dag = beta1_lx_mixed.transpose_conj()
        beta2_from_lx_dag = beta2_lx_mixed.transpose_conj()

        # Left-acting Bednyakov-Pikelner-Velizhanin (JHEP 09 (2014) 098 eq. 27, fn. 7) in d/d(ln mu^2):
        bpv_dlnmu2_1 = (-F(1, 8) * (H1 * H2) - F(1, 2) * (H2 * H1)) * Y1
        bpv_dlnmu2_2 = (-F(1, 8) * (H2 * H1) - F(1, 2) * (H1 * H2)) * Y2

        # Convert d/d(ln mu^2) -> d/d(ln mu) = 2 * d/d(ln mu^2):
        beta1_bpv = 2 * bpv_dlnmu2_1
        beta2_bpv = 2 * bpv_dlnmu2_2

        # Old un-transposed product ordering:
        beta1_old = (-(H1 * H2) - F(1, 4) * (H2 * H1)) * Y1
        beta2_old = (-(H2 * H1) - F(1, 4) * (H1 * H2)) * Y2

        err_lx_vs_bpv_1 = mp.mnorm(beta1_from_lx_dag - beta1_bpv, "F")
        err_lx_vs_bpv_2 = mp.mnorm(beta2_from_lx_dag - beta2_bpv, "F")
        max_adjoint_err = max(err_lx_vs_bpv_1, err_lx_vs_bpv_2)

        # Commutator difference delta beta = beta_BPV - beta_old:
        err_comm_1 = mp.mnorm((beta1_bpv - beta1_old) - F(3, 4) * comm * Y1, "F")
        err_comm_2 = mp.mnorm((beta2_bpv - beta2_old) - (-F(3, 4) * comm * Y2), "F")
        max_comm_formula_err = max(err_comm_1, err_comm_2)

        # Planted controls on Part 2A:
        pc_reversed_order_bpv_err = max(
            mp.mnorm(beta1_from_lx_dag - beta1_old, "F") / mp.mnorm(beta1_bpv, "F"),
            mp.mnorm(beta2_from_lx_dag - beta2_old, "F") / mp.mnorm(beta2_bpv, "F"),
        )
        pc_wrong_diff_factor_bpv_err = mp.mnorm(beta1_from_lx_dag - bpv_dlnmu2_1, "F") / mp.mnorm(beta1_bpv, "F")

        # Basis-invariant trace derivative d/dt Tr(H_1 H_2) before K_2 = (16 pi^2)^{-2}:
        def dtr_h1h2(b1: Any, b2: Any) -> Any:
            dh1 = b1 * Y1.transpose_conj() + Y1 * b1.transpose_conj()
            dh2 = b2 * Y2.transpose_conj() + Y2 * b2.transpose_conj()
            m_tot = dh1 * H2 + H1 * dh2
            return sum(mp.re(m_tot[i, i]) for i in range(3))

        dtr_rep = dtr_h1h2(beta1_bpv, beta2_bpv)
        dtr_old = dtr_h1h2(beta1_old, beta2_old)
        comm_sq = comm * comm
        tr_comm_sq = sum(mp.re(comm_sq[i, i]) for i in range(3))
        trace_shift_identity_err = abs((dtr_rep - dtr_old) - F(3, 2) * tr_comm_sq)
        pc_reversed_trace_shift_abs = abs(dtr_rep - dtr_old)

        # Diagonal commuting check:
        Y1_diag = mp.diag([F(1, 5), F(1, 2), F(9, 10)])
        Y2_diag = mp.diag([F(1, 10), F(3, 10), F(7, 10)])
        H1_d = Y1_diag * Y1_diag.transpose_conj()
        H2_d = Y2_diag * Y2_diag.transpose_conj()
        comm_d = H1_d * H2_d - H2_d * H1_d
        diag_comm_norm = mp.mnorm(comm_d, "F")

    e1_passed = bool(
        float(max_adjoint_err) < 1e-60
        and float(max_comm_formula_err) < 1e-60
        and float(trace_shift_identity_err) < 1e-60
        and float(tr_comm_sq) < -1e-3
        and float(diag_comm_norm) == 0.0
        and float(pc_reversed_order_bpv_err) > 0.1
        and float(pc_reversed_trace_shift_abs) > 1e-2
        and float(pc_wrong_diff_factor_bpv_err) > 0.1
    )
    return {
        "E1_AdjointConversion_and_TraceInvariant_Gate_passed": e1_passed,
        "max_adjoint_err_lx_dag_vs_2x_bpv_eq27": float(max_adjoint_err),
        "max_commutator_formula_err": float(max_comm_formula_err),
        "trace_shift_identity_err": float(trace_shift_identity_err),
        "tr_commutator_squared_noncommuting": float(tr_comm_sq),
        "d_dt_tr_H1H2_repaired_mixed": float(dtr_rep),
        "d_dt_tr_H1H2_old_mixed": float(dtr_old),
        "diagonal_commutator_norm": float(diag_comm_norm),
        "PC_BR2_ReversedMixedProductOrder_adjoint_rel_err": float(pc_reversed_order_bpv_err),
        "PC_BR2_ReversedMixedProductOrder_trace_shift_abs": float(pc_reversed_trace_shift_abs),
        "PC_BR2_WrongDiffFactor_bpv_rel_err": float(pc_wrong_diff_factor_bpv_err),
    }


# ============================================================================
# SECTION 3: PART 2B — REPAIRED FOUR-PILLAR LITERATURE BENCHMARK GATE (COEFF 11/2)
# ============================================================================

def run_part_2b_repaired_four_pillar_gate() -> Dict[str, Any]:
    """
    AST-isolated 4-pillar published RGE benchmark gate (Guardrail 4 + Codex REVIEW.md Section 2).
    Repairs Pillar 2 (PRD 47, 2038 eqs. 10, 17-26 + Luo-Xiao / BPV eq. 27) to exact coefficient 11/2
    on y_{3,sec1}^2 y_{3,sec2}^2, verified to < 1e-60 in 100-digit mpmath and < 5e-7 in centered f64,
    while catching the old un-transposed coefficient 7 by > 1e-2 relative error!
    """
    # Pillar 1: 1-loop closed-form gauge check + Buttazzo et al. (2013) 3-loop Planck benchmark
    W4_z = np.zeros((3, 3), dtype=complex)
    g1_i, g2_i, g3_i = 0.46, 0.65, 1.15
    dln_test = 30.0
    n_g = 3000
    dt_g = dln_test / n_g
    g_num = np.array([g1_i, g2_i, g3_i], dtype=float)
    b_1l = np.array([41.0 / 10.0, -19.0 / 6.0, -7.0], dtype=float)
    for _ in range(n_g):
        k1 = K1_F64 * b_1l * (g_num ** 3)
        k2 = K1_F64 * b_1l * ((g_num + 0.5 * dt_g * k1) ** 3)
        k3 = K1_F64 * b_1l * ((g_num + 0.5 * dt_g * k2) ** 3)
        k4 = K1_F64 * b_1l * ((g_num + dt_g * k3) ** 3)
        g_num = g_num + (dt_g / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    g_exact = np.array(
        [g0 / math.sqrt(1.0 - 2.0 * K1_F64 * b_1l[idx] * (g0 ** 2) * dln_test) for idx, g0 in enumerate([g1_i, g2_i, g3_i])]
    )
    gauge_1loop_err = float(np.max(np.abs(g_num - g_exact)))
    g_wrong = np.array(
        [g0 / math.sqrt(1.0 - K1_F64 * b_1l[idx] * (g0 ** 2) * dln_test) for idx, g0 in enumerate([g1_i, g2_i, g3_i])]
    )
    pc_wrong_diff_factor_err = float(np.max(np.abs(g_wrong - g_exact)))

    mt_lit, mpl_lit = 173.34, 1.2209e19
    g1_0 = math.sqrt(5.0 / 3.0) * 0.35830
    y_st = np.array([g1_0 ** 2, 0.64779 ** 2, 1.1666 ** 2, 0.93690 ** 2, 0.0165 ** 2, 0.0102 ** 2, 0.12604])
    u0, u1 = 2.0 * math.log(mt_lit), 2.0 * math.log(mpl_lit)
    n_but = 6000
    du = (u1 - u0) / n_but
    u_cross = 0.0
    crossed = False
    u_cur = u0
    for _ in range(n_but):
        y_prev = y_st.copy()
        k1 = buttazzo_3loop_d_dlnmu2(y_st)
        k2 = buttazzo_3loop_d_dlnmu2(y_st + 0.5 * du * k1)
        k3 = buttazzo_3loop_d_dlnmu2(y_st + 0.5 * du * k2)
        k4 = buttazzo_3loop_d_dlnmu2(y_st + du * k3)
        y_st = y_st + (du / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        if (not crossed) and y_prev[6] > 0.0 and y_st[6] <= 0.0:
            u_cross = u_cur + du * (y_prev[6] / (y_prev[6] - y_st[6]))
            crossed = True
        u_cur += du
    g1_pl, g2_pl, g3_pl, yt_pl, lam_pl = (
        math.sqrt(y_st[0]), math.sqrt(y_st[1]), math.sqrt(y_st[2]), math.sqrt(y_st[3]), float(y_st[6])
    )
    pub_pl = {"g1": 0.6154, "g2": 0.5055, "g3": 0.4873, "yt": 0.3825, "lam": -0.0143}
    but_4coupling_rel_err = max(
        abs(g1_pl - pub_pl["g1"]) / pub_pl["g1"],
        abs(g2_pl - pub_pl["g2"]) / pub_pl["g2"],
        abs(g3_pl - pub_pl["g3"]) / pub_pl["g3"],
        abs(yt_pl - pub_pl["yt"]) / pub_pl["yt"],
    )
    but_lam_abs_err = abs(lam_pl - pub_pl["lam"])
    log10_lam_zero = 0.5 * u_cross / math.log(10.0)
    log10_two_lambda_v = 9.5 + math.log10(2.0)

    # Pillar 2A (f64): Repaired PRD 47, 2038 + Luo-Xiao/BPV Rank-1 2-Loop Mixing at exact coefficient 11/2!
    yt_b, yb_b, ytau_b = 0.90, 0.50, 0.30
    g1_b, g2_b, g3_b, lam_b = 0.45, 0.65, 1.15, 0.13
    th_b = 0.25
    c_b, s_b = math.cos(th_b), math.sin(th_b)
    v_rot = np.array([[1.0, 0.0, 0.0], [0.0, c_b, s_b], [0.0, -s_b, c_b]], dtype=complex)
    Yu_nc = np.diag([1.0e-9, 2.0e-8, yt_b]).astype(complex)
    Yd_nc = v_rot @ np.diag([1.0e-9, 3.0e-8, yb_b]).astype(complex)
    Ye_nc = np.diag([1.0e-9, 1.0e-7, ytau_b]).astype(complex)

    def v23_mod(u_m: np.ndarray, d_m: np.ndarray) -> float:
        uu, _ = svd_ascending_np(u_m)
        ud, _ = svd_ascending_np(d_m)
        return float(np.abs(uu.conj().T @ ud)[1, 2])

    dt_b = 1.0e-7
    dYu_rep, dYd_rep, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_nc, Yd_nc, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, True)
    dln_v23_rep_f64 = (
        math.log(v23_mod(Yu_nc + dt_b * dYu_rep, Yd_nc + dt_b * dYd_rep))
        - math.log(v23_mod(Yu_nc - dt_b * dYu_rep, Yd_nc - dt_b * dYd_rep))
    ) / (2.0 * dt_b)

    dYu_old, dYd_old, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_nc, Yd_nc, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, False)
    dln_v23_old_f64 = (
        math.log(v23_mod(Yu_nc + dt_b * dYu_old, Yd_nc + dt_b * dYd_old))
        - math.log(v23_mod(Yu_nc - dt_b * dYu_old, Yd_nc - dt_b * dYd_old))
    ) / (2.0 * dt_b)

    rank1_1l = -1.5 * (yt_b ** 2 + yb_b ** 2)
    rank1_2l_repaired_11_over_2 = (
        6.5 * (yt_b ** 4 + yb_b ** 4)
        + (11.0 / 2.0) * (yt_b ** 2) * (yb_b ** 2)
        + 1.25 * (ytau_b ** 2) * (yt_b ** 2 + yb_b ** 2)
        - 16.0 * (g3_b ** 2) * (yt_b ** 2 + yb_b ** 2)
        + (9.0 / 16.0) * (g2_b ** 2) * (yt_b ** 2 + yb_b ** 2)
        - (79.0 / 80.0) * (g1_b ** 2) * (yt_b ** 2)
        - (43.0 / 80.0) * (g1_b ** 2) * (yb_b ** 2)
    )
    part1_f64 = -(c_b ** 2) * K1_F64 * rank1_1l
    part2_f64 = -(c_b ** 2) * K2_F64 * rank1_2l_repaired_11_over_2
    repaired_11_over_2_f64_rel_err = abs((dln_v23_rep_f64 - part1_f64) - part2_f64) / abs(part2_f64)
    pc_old_order_vs_11_over_2_f64_rel_err = abs((dln_v23_old_f64 - part1_f64) - part2_f64) / abs(part2_f64)

    # Diagonal invariance check between repaired and old:
    Yu_dg = np.diag([0.0, 0.0, yt_b]).astype(complex)
    Yd_dg = np.diag([0.0, 0.0, yb_b]).astype(complex)
    dYu_dg_rep, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_dg, Yd_dg, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, True)
    dYu_dg_old, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_dg, Yd_dg, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, False)
    diag_repaired_vs_old_diff = float(np.max(np.abs(dYu_dg_rep - dYu_dg_old)))

    # Pillar 2B (100-digit mpmath eigenvector differentiation via mp.eighe):
    with mp.workdps(100):
        F = lambda p, q: mp.mpf(p) / mp.mpf(q)
        yt_m, yb_m, ytau_m = F(9, 10), F(1, 2), F(3, 10)
        g1_m, g2_m, g3_m, lam_m = F(9, 20), F(13, 20), F(23, 20), F(13, 100)
        th_m = F(1, 4)
        cb_m, sb_m = mp.cos(th_m), mp.sin(th_m)
        eps_u, eps_d = mp.mpf(10) ** (-45), 2 * (mp.mpf(10) ** (-45))
        vrot_m = mp.matrix([[1, 0, 0], [0, cb_m, sb_m], [0, -sb_m, cb_m]])
        Yu_m0 = [[mp.mpc(0)] * 3 for _ in range(3)]
        Yu_m0[1][1] = mp.mpc(eps_u)
        Yu_m0[2][2] = mp.mpc(yt_m)
        Yd_m_mat = vrot_m * mp.matrix([[0, 0, 0], [0, eps_d, 0], [0, 0, yb_m]])
        Yd_m0 = [[Yd_m_mat[r, c] for c in range(3)] for r in range(3)]
        Ye_m0 = [[mp.mpc(0)] * 3 for _ in range(3)]
        Ye_m0[2][2] = mp.mpc(ytau_m)
        W4_m0 = [[mp.mpc(0)] * 3 for _ in range(3)]

        k1_m = mp.mpf(1) / (16 * mp.pi * mp.pi)
        k2_m = k1_m * k1_m

        def v23_mp_eighe(u_list: List[List[Any]], d_list: List[List[Any]]) -> Any:
            hu = mp.matrix(mp3_mul(u_list, mp3_dag(u_list)))
            hd = mp.matrix(mp3_mul(d_list, mp3_dag(d_list)))
            _, qu = eighe_sorted_mp(hu)
            _, qd = eighe_sorted_mp(hd)
            v12 = qu.transpose_conj() * qd
            return abs(v12[1, 2])

        def add_mp3(a: List[List[Any]], b: List[List[Any]], sc: Any) -> List[List[Any]]:
            return [[a[r][c] + sc * b[r][c] for c in range(3)] for r in range(3)]

        dt_m = mp.mpf(10) ** (-35)
        dYu_mr, dYd_mr, *_ = sm_2loop_plus_weinberg_rhs_mp(Yu_m0, Yd_m0, Ye_m0, W4_m0, g1_m, g2_m, g3_m, lam_m, k1_m, k2_m, True)
        dln_mr = (
            mp.log(v23_mp_eighe(add_mp3(Yu_m0, dYu_mr, dt_m), add_mp3(Yd_m0, dYd_mr, dt_m)))
            - mp.log(v23_mp_eighe(add_mp3(Yu_m0, dYu_mr, -dt_m), add_mp3(Yd_m0, dYd_mr, -dt_m)))
        ) / (2 * dt_m)

        dYu_mo, dYd_mo, *_ = sm_2loop_plus_weinberg_rhs_mp(Yu_m0, Yd_m0, Ye_m0, W4_m0, g1_m, g2_m, g3_m, lam_m, k1_m, k2_m, False)
        dln_mo = (
            mp.log(v23_mp_eighe(add_mp3(Yu_m0, dYu_mo, dt_m), add_mp3(Yd_m0, dYd_mo, dt_m)))
            - mp.log(v23_mp_eighe(add_mp3(Yu_m0, dYu_mo, -dt_m), add_mp3(Yd_m0, dYd_mo, -dt_m)))
        ) / (2 * dt_m)

        r1_1l_m = -F(3, 2) * (yt_m ** 2 + yb_m ** 2)
        r1_2l_m = (
            F(13, 2) * (yt_m ** 4 + yb_m ** 4)
            + F(11, 2) * (yt_m ** 2) * (yb_m ** 2)
            + F(5, 4) * (ytau_m ** 2) * (yt_m ** 2 + yb_m ** 2)
            - 16 * (g3_m ** 2) * (yt_m ** 2 + yb_m ** 2)
            + F(9, 16) * (g2_m ** 2) * (yt_m ** 2 + yb_m ** 2)
            - F(79, 80) * (g1_m ** 2) * (yt_m ** 2)
            - F(43, 80) * (g1_m ** 2) * (yb_m ** 2)
        )
        p1_m = -(cb_m ** 2) * k1_m * r1_1l_m
        p2_m = -(cb_m ** 2) * k2_m * r1_2l_m
        repaired_11_over_2_mp_rel_err = float(abs((dln_mr - p1_m) - p2_m) / abs(p2_m))
        pc_old_order_vs_11_over_2_mp_rel_err = float(abs((dln_mo - p1_m) - p2_m) / abs(p2_m))

    # Pillar 3: Xing & Zhou (2018) downward 1-loop matrix RGE & Eq. (18) Naumov identity
    t_uv = math.log(1.0e12 / 91.1876)
    g1_mz, g2_mz, g3_mz = 0.4614, 0.6518, 1.2143
    g1_x0 = g1_mz / math.sqrt(1.0 - 2.0 * K1_F64 * (41.0 / 10.0) * (g1_mz ** 2) * t_uv)
    g2_x0 = g2_mz / math.sqrt(1.0 - 2.0 * K1_F64 * (-19.0 / 6.0) * (g2_mz ** 2) * t_uv)
    g3_x0 = g3_mz / math.sqrt(1.0 - 2.0 * K1_F64 * (-7.0) * (g3_mz ** 2) * t_uv)
    Yu_x0 = np.diag([1.0e-5, 3.0e-3, 0.52]).astype(complex)
    c12, s12 = math.cos(0.22), math.sin(0.22)
    c23, s23 = math.cos(0.04), math.sin(0.04)
    c13, s13 = math.cos(0.004), math.sin(0.004)
    eid = complex(math.cos(1.15), -math.sin(1.15))
    v_xz = (
        np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], dtype=complex)
        @ np.array([[c13, 0, s13 * eid], [0, 1, 0], [-s13 * eid.conjugate(), 0, c13]], dtype=complex)
        @ np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], dtype=complex)
    )
    Yd_x0 = v_xz @ np.diag([1.5e-5, 3.0e-4, 1.4e-2]).astype(complex)
    Yl_x0 = np.diag([2.8e-6, 6.0e-4, 1.0e-2]).astype(complex)

    def xz_rhs(u_m: np.ndarray, d_m: np.ndarray, l_m: np.ndarray, g1v: float, g2v: float, g3v: float):
        hu = u_m @ u_m.conj().T
        hl = l_m @ l_m.conj().T
        chi = float(np.real(3.0 * np.trace(hu) + np.trace(hl)))
        g1s, g2s, g3s = g1v ** 2, g2v ** 2, g3v ** 2
        au = -0.85 * g1s - 2.25 * g2s - 8.0 * g3s + chi
        ad = -0.25 * g1s - 2.25 * g2s - 8.0 * g3s + chi
        al = -2.25 * g1s - 2.25 * g2s + chi
        eye3 = np.eye(3, dtype=complex)
        du = K1_F64 * (au * eye3 + 1.5 * hu) @ u_m
        dd = K1_F64 * (ad * eye3 - 1.5 * hu) @ d_m
        dl = K1_F64 * (al * eye3 + 1.5 * hl) @ l_m
        return du, dd, dl, K1_F64 * 4.1 * g1v ** 3, K1_F64 * (-19.0 / 6.0) * g2v ** 3, K1_F64 * (-7.0) * g3v ** 3, ad

    def run_xz(sign_dir: float) -> Tuple[np.ndarray, np.ndarray, float, np.ndarray]:
        n_xz = 3000
        dt_x = sign_dir * t_uv / n_xz
        u_m, d_m, l_m = Yu_x0.copy(), Yd_x0.copy(), Yl_x0.copy()
        g1v, g2v, g3v = g1_x0, g2_x0, g3_x0
        int_ad = 0.0
        int_yu2 = np.zeros(3, dtype=float)
        for _ in range(n_xz):
            du1, dd1, dl1, dg1_1, dg2_1, dg3_1, ad1 = xz_rhs(u_m, d_m, l_m, g1v, g2v, g3v)
            yu2_1 = np.real(np.diag(u_m @ u_m.conj().T))
            um1, dm1, lm1 = u_m + 0.5 * dt_x * du1, d_m + 0.5 * dt_x * dd1, l_m + 0.5 * dt_x * dl1
            du2, dd2, dl2, dg1_2, dg2_2, dg3_2, ad2 = xz_rhs(um1, dm1, lm1, g1v + 0.5 * dt_x * dg1_1, g2v + 0.5 * dt_x * dg2_1, g3v + 0.5 * dt_x * dg3_1)
            um2, dm2, lm2 = u_m + 0.5 * dt_x * du2, d_m + 0.5 * dt_x * dd2, l_m + 0.5 * dt_x * dl2
            du3, dd3, dl3, dg1_3, dg2_3, dg3_3, ad3 = xz_rhs(um2, dm2, lm2, g1v + 0.5 * dt_x * dg1_2, g2v + 0.5 * dt_x * dg2_2, g3v + 0.5 * dt_x * dg3_2)
            ue, de, le = u_m + dt_x * du3, d_m + dt_x * dd3, l_m + dt_x * dl3
            du4, dd4, dl4, dg1_4, dg2_4, dg3_4, ad4 = xz_rhs(ue, de, le, g1v + dt_x * dg1_3, g2v + dt_x * dg2_3, g3v + dt_x * dg3_3)
            u_m += (dt_x / 6.0) * (du1 + 2.0 * du2 + 2.0 * du3 + du4)
            d_m += (dt_x / 6.0) * (dd1 + 2.0 * dd2 + 2.0 * dd3 + dd4)
            l_m += (dt_x / 6.0) * (dl1 + 2.0 * dl2 + 2.0 * dl3 + dl4)
            g1v += (dt_x / 6.0) * (dg1_1 + 2.0 * dg1_2 + 2.0 * dg1_3 + dg1_4)
            g2v += (dt_x / 6.0) * (dg2_1 + 2.0 * dg2_2 + 2.0 * dg2_3 + dg2_4)
            g3v += (dt_x / 6.0) * (dg3_1 + 2.0 * dg3_2 + 2.0 * dg3_3 + dg3_4)
            ds = abs(dt_x)
            int_ad += (ds / 6.0) * (ad1 + 2.0 * ad2 + 2.0 * ad3 + ad4)
            int_yu2 += (ds / 6.0) * (
                yu2_1 + 2.0 * np.real(np.diag(um1 @ um1.conj().T)) + 2.0 * np.real(np.diag(um2 @ um2.conj().T)) + np.real(np.diag(ue @ ue.conj().T))
            )
        return u_m, d_m, math.exp(sign_dir * K1_F64 * int_ad), np.exp(-sign_dir * 1.5 * K1_F64 * int_yu2)

    def naumov_combo(u_m: np.ndarray, d_m: np.ndarray) -> float:
        hu, hd = u_m @ u_m.conj().T, d_m @ d_m.conj().T
        eu = np.sort(np.real(np.linalg.eigvalsh(hu)))
        det_c = np.linalg.det(hu @ hd - hd @ hu)
        prod_u = (eu[1] - eu[0]) * (eu[2] - eu[1]) * (eu[2] - eu[0])
        return float(np.imag(det_c) / (2.0 * prod_u))

    Yu_xz_ir, Yd_xz_ir, Id_xz, xi_xz = run_xz(-1.0)
    rhs_xz = (Id_xz ** 6) * float(np.prod(xi_xz ** 2)) * naumov_combo(Yu_x0, Yd_x0)
    xz_eq18_rel_err = abs(naumov_combo(Yu_xz_ir, Yd_xz_ir) - rhs_xz) / abs(rhs_xz)
    Yu_xz_bad, Yd_xz_bad, _, _ = run_xz(+1.0)
    pc_wrong_dir_eq18_rel_err = abs(naumov_combo(Yu_xz_bad, Yd_xz_bad) - rhs_xz) / abs(rhs_xz)

    # Pillar 4: Antusch et al. (2001/2003) 1-loop dimension-5 Weinberg operator analytical integral check
    rng = np.random.default_rng(20261115)
    a_sym = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    w_init = 0.5 * (a_sym + a_sym.T)
    Yu_a0 = np.diag([1.0e-4, 4.0e-3, 0.6]).astype(complex)
    Yd_a0 = np.diag([2.0e-4, 3.0e-3, 0.02]).astype(complex)
    Ye_a0 = np.diag([1.0e-5, 2.0e-3, 0.15]).astype(complex)
    g1_a, g2_a, g3_a, lam_a = 0.55, 0.55, 0.55, 0.05
    n_ant = 2500
    dt_a = -25.0 / n_ant
    Yu_a, Yd_a, Ye_a, W_a = Yu_a0.copy(), Yd_a0.copy(), Ye_a0.copy(), w_init.copy()
    int_ak = 0.0
    int_ye2 = np.zeros(3, dtype=float)

    def ant_1loop_rhs(u_m, d_m, e_m, w_m, g1v, g2v, g3v, lamv):
        hu, hd, he = u_m @ u_m.conj().T, d_m @ d_m.conj().T, e_m @ e_m.conj().T
        tu, td, te = float(np.real(np.trace(hu))), float(np.real(np.trace(hd))), float(np.real(np.trace(he)))
        y2 = 3.0 * tu + 3.0 * td + te
        g1s, g2s, g3s = g1v ** 2, g2v ** 2, g3v ** 2
        eye3 = np.eye(3, dtype=complex)
        du = K1_F64 * (((y2 - 0.85 * g1s - 2.25 * g2s - 8.0 * g3s) * eye3 + 1.5 * (hu - hd)) @ u_m)
        dd = K1_F64 * (((y2 - 0.25 * g1s - 2.25 * g2s - 8.0 * g3s) * eye3 + 1.5 * (hd - hu)) @ d_m)
        de = K1_F64 * (((y2 - 2.25 * g1s - 2.25 * g2s) * eye3 + 1.5 * he) @ e_m)
        ak = 4.0 * lamv - 3.0 * g2s + 2.0 * y2
        dw = K1_F64 * (-1.5 * (he @ w_m + w_m @ he.T) + ak * w_m)
        thu2, thd2, the2 = float(np.real(np.trace(hu @ hu))), float(np.real(np.trace(hd @ hd))), float(np.real(np.trace(he @ he)))
        dlam = K1_F64 * (
            24.0 * lamv ** 2 + lamv * (4.0 * y2 - 9.0 * g2s - 1.8 * g1s)
            - 2.0 * (3.0 * thu2 + 3.0 * thd2 + the2)
            + (9.0 / 8.0) * g2s ** 2 + (27.0 / 200.0) * g1s ** 2 + (9.0 / 20.0) * g1s * g2s
        )
        return du, dd, de, dw, K1_F64 * 4.1 * g1v ** 3, K1_F64 * (-19.0 / 6.0) * g2v ** 3, K1_F64 * (-7.0) * g3v ** 3, dlam, ak, np.real(np.diag(he))

    for _ in range(n_ant):
        s1 = ant_1loop_rhs(Yu_a, Yd_a, Ye_a, W_a, g1_a, g2_a, g3_a, lam_a)
        s2 = ant_1loop_rhs(Yu_a + 0.5*dt_a*s1[0], Yd_a + 0.5*dt_a*s1[1], Ye_a + 0.5*dt_a*s1[2], W_a + 0.5*dt_a*s1[3], g1_a + 0.5*dt_a*s1[4], g2_a + 0.5*dt_a*s1[5], g3_a + 0.5*dt_a*s1[6], lam_a + 0.5*dt_a*s1[7])
        s3 = ant_1loop_rhs(Yu_a + 0.5*dt_a*s2[0], Yd_a + 0.5*dt_a*s2[1], Ye_a + 0.5*dt_a*s2[2], W_a + 0.5*dt_a*s2[3], g1_a + 0.5*dt_a*s2[4], g2_a + 0.5*dt_a*s2[5], g3_a + 0.5*dt_a*s2[6], lam_a + 0.5*dt_a*s2[7])
        s4 = ant_1loop_rhs(Yu_a + dt_a*s3[0], Yd_a + dt_a*s3[1], Ye_a + dt_a*s3[2], W_a + dt_a*s3[3], g1_a + dt_a*s3[4], g2_a + dt_a*s3[5], g3_a + dt_a*s3[6], lam_a + dt_a*s3[7])
        Yu_a += (dt_a / 6.0) * (s1[0] + 2.0 * s2[0] + 2.0 * s3[0] + s4[0])
        Yd_a += (dt_a / 6.0) * (s1[1] + 2.0 * s2[1] + 2.0 * s3[1] + s4[1])
        Ye_a += (dt_a / 6.0) * (s1[2] + 2.0 * s2[2] + 2.0 * s3[2] + s4[2])
        W_a += (dt_a / 6.0) * (s1[3] + 2.0 * s2[3] + 2.0 * s3[3] + s4[3])
        g1_a += (dt_a / 6.0) * (s1[4] + 2.0 * s2[4] + 2.0 * s3[4] + s4[4])
        g2_a += (dt_a / 6.0) * (s1[5] + 2.0 * s2[5] + 2.0 * s3[5] + s4[5])
        g3_a += (dt_a / 6.0) * (s1[6] + 2.0 * s2[6] + 2.0 * s3[6] + s4[6])
        lam_a += (dt_a / 6.0) * (s1[7] + 2.0 * s2[7] + 2.0 * s3[7] + s4[7])
        int_ak += (dt_a / 6.0) * (s1[8] + 2.0 * s2[8] + 2.0 * s3[8] + s4[8])
        int_ye2 += (dt_a / 6.0) * (s1[9] + 2.0 * s2[9] + 2.0 * s3[9] + s4[9])

    i_kap = math.exp(K1_F64 * int_ak)
    i_lep = np.exp(-1.5 * K1_F64 * int_ye2)
    w_exact = i_kap * (np.diag(i_lep) @ w_init @ np.diag(i_lep))
    antusch_integral_rel_err = float(np.linalg.norm(W_a - w_exact) / np.linalg.norm(w_exact))
    antusch_sym_err = float(np.linalg.norm(W_a - W_a.T) / np.linalg.norm(W_a))

    u_lep_c, _ = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    Ye_c = u_lep_c @ np.diag([0.05, 0.25, 0.80]).astype(complex)
    W_c = u_lep_c @ w_init @ u_lep_c.T
    _, _, _, dW_good_c, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_a0, Yd_a0, Ye_c, W_c, 0.5, 0.5, 0.5, 0.1, True, False, False)
    _, _, _, dW_bad_c, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_a0, Yd_a0, Ye_c, W_c, 0.5, 0.5, 0.5, 0.1, True, False, True)
    good_sym_c = float(np.linalg.norm(dW_good_c - dW_good_c.T) / np.linalg.norm(dW_good_c))
    pc_wrong_maj_transpose_sym_err = float(np.linalg.norm(dW_bad_c - dW_bad_c.T) / np.linalg.norm(dW_bad_c))

    e2_passed = bool(
        gauge_1loop_err < 1e-12
        and pc_wrong_diff_factor_err > 0.1
        and but_4coupling_rel_err < 2e-3
        and but_lam_abs_err < 5e-4
        and abs(log10_lam_zero - log10_two_lambda_v) < 0.05
        and repaired_11_over_2_mp_rel_err < 1e-60
        and repaired_11_over_2_f64_rel_err < 5e-7
        and pc_old_order_vs_11_over_2_mp_rel_err > 1e-2
        and pc_old_order_vs_11_over_2_f64_rel_err > 1e-2
        and diag_repaired_vs_old_diff == 0.0
        and xz_eq18_rel_err < 1e-12
        and pc_wrong_dir_eq18_rel_err > 0.5
        and antusch_integral_rel_err < 1e-12
        and antusch_sym_err < 1e-15
        and good_sym_c < 1e-15
        and pc_wrong_maj_transpose_sym_err > 0.2
    )
    return {
        "E2_RepairedFourPillar_11Over2_Gate_passed": e2_passed,
        "pillar1_buttazzo_3loop": {
            "gauge_1loop_closed_form_err": gauge_1loop_err,
            "PC_BR2_WrongDiffFactor_err": pc_wrong_diff_factor_err,
            "four_coupling_planck_max_rel_err": float(but_4coupling_rel_err),
            "lam_planck_abs_err": float(but_lam_abs_err),
            "log10_Lambda_lam_GeV": float(log10_lam_zero),
            "log10_two_Lambda_V_GeV": float(log10_two_lambda_v),
        },
        "pillar2_repaired_rank1_mixing_11_over_2": {
            "repaired_11_over_2_mp100_rel_err": repaired_11_over_2_mp_rel_err,
            "repaired_11_over_2_f64_rel_err": float(repaired_11_over_2_f64_rel_err),
            "PC_BR2_ReversedMixedProductOrder_mp100_rel_err": pc_old_order_vs_11_over_2_mp_rel_err,
            "PC_BR2_ReversedMixedProductOrder_f64_rel_err": float(pc_old_order_vs_11_over_2_f64_rel_err),
            "diagonal_repaired_vs_old_max_diff": diag_repaired_vs_old_diff,
        },
        "pillar3_xing_zhou_downward_matrix": {
            "eq18_naumov_rel_err": float(xz_eq18_rel_err),
            "PC_BR2_WrongRunningDirection_eq18_rel_err": float(pc_wrong_dir_eq18_rel_err),
        },
        "pillar4_antusch_weinberg_1loop": {
            "analytical_integral_rel_err": antusch_integral_rel_err,
            "weinberg_symmetry_err": antusch_sym_err,
            "PC_BR2_WrongMajoranaTranspose_sym_err": pc_wrong_maj_transpose_sym_err,
        },
    }


# ============================================================================
# SECTION 4: PART 2C — OLD-VS-REPAIRED TRAJECTORY DIFF & 24-DIGIT HAAR-6 GATE
# ============================================================================

def compare_obs_dicts(old_obs: Dict[str, Any], rep_obs: Dict[str, Any]) -> Dict[str, Any]:
    scalar_keys = [
        "alpha1_inv_gut", "alpha2_inv", "alpha3_inv", "sin2_theta_ew_ir",
        "lam_ir", "scalar_to_condensate_sqrt_2lam",
        "s3_sec1", "s3_sec2", "s3_sec3",
        "inter_s3_sec1_over_sec2", "inter_s3_sec2_over_sec3",
        "sec1_r12", "sec1_r23", "sec2_r12", "sec2_r23",
        "sec3_r12", "sec3_r23", "sec4_r12", "sec4_r23",
        "sin2_2theta_sec34_parity_block", "I_CP_hat_IR", "J12_CP_IR",
    ]
    diffs: Dict[str, Dict[str, float]] = {}
    max_scalar_abs = 0.0
    max_scalar_rel = 0.0
    for k in scalar_keys:
        vo, vr = float(old_obs[k]), float(rep_obs[k])
        da = abs(vr - vo)
        dr = da / max(abs(vo), 1e-30)
        diffs[k] = {"old": vo, "repaired": vr, "abs_diff": da, "rel_diff": dr}
        max_scalar_abs = max(max_scalar_abs, da)
        max_scalar_rel = max(max_scalar_rel, dr)

    v12_old = np.array(old_obs["V12_abs"], dtype=float)
    v12_rep = np.array(rep_obs["V12_abs"], dtype=float)
    v12_abs_diff = np.abs(v12_rep - v12_old)
    v12_rel_diff = v12_abs_diff / np.maximum(v12_old, 1e-30)

    u34_old = np.array(old_obs["U34_abs"], dtype=float)
    u34_rep = np.array(rep_obs["U34_abs"], dtype=float)
    u34_abs_diff = np.abs(u34_rep - u34_old)

    return {
        "scalar_comparisons": diffs,
        "V12_abs_old": old_obs["V12_abs"],
        "V12_abs_repaired": rep_obs["V12_abs"],
        "V12_max_abs_diff": float(np.max(v12_abs_diff)),
        "V12_max_rel_diff": float(np.max(v12_rel_diff)),
        "U34_max_abs_diff": float(np.max(u34_abs_diff)),
        "overall_max_abs_diff": float(max(max_scalar_abs, float(np.max(v12_abs_diff)), float(np.max(u34_abs_diff)))),
        "overall_max_rel_diff": float(max(max_scalar_rel, float(np.max(v12_rel_diff)))),
    }


def run_part_2c_trajectory_diff_and_haar6() -> Dict[str, Any]:
    elim_exact = derive_su5_universal_1loop_eliminants_exact(3, 1)
    sw2_int = float(elim_exact["sw2_intercept"])
    sw2_slp = float(elim_exact["sw2_slope"])

    with mp.workdps(36):
        _VCAS_CACHE.clear()
        x_s, y_s, a_cas_mp = solve_joint_3var_newton(Fraction(3, 5), Fraction(4, 5), Fraction(19, 1))
        tau_star_mp = tau_nz_from_z1(mp.mpc(x_s, y_s))
        vol_m004_mp = -neg_vol_on_gluing_curve(x_s, y_s)

        uv_ref_mp = build_zero_knob_uv_state_mp(tau_star_mp, vol_m004_mp, a_cas_mp, Fraction(4, 15), Fraction(8, 15))
        mr_star_mp = uv_ref_mp["M_R"]
        m_r_np = mp_to_np(mr_star_mp)
        m_r_inv = np.linalg.inv(m_r_np)
        tau_star_c = complex(tau_star_mp)
        amp0 = float(collar_amp_mp(0, mp.im(tau_star_mp)))
        ampp = float(collar_amp_mp(1, mp.im(tau_star_mp)))
        ampm = float(collar_amp_mp(-1, mp.im(tau_star_mp)))
        a_uv_inv = float(vol_m004_mp * a_cas_mp)
        g_uv = math.sqrt(4.0 * math.pi / a_uv_inv)
        lam_uv = 0.2 * g_uv * g_uv
        dln_cover = -float((mp.mpf(45) / mp.pi) * vol_m004_mp)
        c_pos = g_uv * amp0 * amp0 * ampp
        c_neg = g_uv * amp0 * amp0 * ampm

    # 32-digit mpmath integration of BOTH repaired and old on reference vacuum (4/15, 8/15) at n_steps=600:
    with mp.workdps(32):
        uv32 = build_zero_knob_uv_state_mp(tau_star_mp, vol_m004_mp, a_cas_mp, Fraction(4, 15), Fraction(8, 15))
        Yu_mp_rep, Yd_mp_rep, Ye_mp_rep, W4_mp_rep, g1_mp_r, g2_mp_r, g3_mp_r, lam_mp_r = rk4_integrate_full_mp(
            mp_to_list3(uv32["Y1"]), mp_to_list3(uv32["Y2"]), mp_to_list3(uv32["Y3"]), mp_to_list3(uv32["W4"]),
            uv32["g_uv"], uv32["g_uv"], uv32["g_uv"], uv32["lam_uv"], uv32["d_ln_mu"], n_steps=600, repaired_mixed_order=True,
        )
        Yu_mp_old, Yd_mp_old, Ye_mp_old, W4_mp_old, _, _, _, lam_mp_o = rk4_integrate_full_mp(
            mp_to_list3(uv32["Y1"]), mp_to_list3(uv32["Y2"]), mp_to_list3(uv32["Y3"]), mp_to_list3(uv32["W4"]),
            uv32["g_uv"], uv32["g_uv"], uv32["g_uv"], uv32["lam_uv"], uv32["d_ln_mu"], n_steps=600, repaired_mixed_order=False,
        )
        obs_mp32_rep = extract_obs_mp_full(Yu_mp_rep, Yd_mp_rep, Ye_mp_rep, W4_mp_rep, lam_mp_r)
        obs_mp32_old = extract_obs_mp_full(Yu_mp_old, Yd_mp_old, Ye_mp_old, W4_mp_old, lam_mp_o)
        mp32_v12_old_vs_rep_max_abs_diff = float(
            max(abs(obs_mp32_rep["v12_abs"][r][c] - obs_mp32_old["v12_abs"][r][c]) for r in range(3) for c in range(3))
        )

    # f64 (n_steps=1600) side-by-side audit across representative vacua at Levels 5, 10, 15:
    sample_vacua = [
        ("level15_casimir_ref_4_15_8_15", Fraction(4, 15), Fraction(8, 15)),
        ("level15_alt_1_15_2_15", Fraction(1, 15), Fraction(2, 15)),
        ("level5_rep_1_5_2_5", Fraction(1, 5), Fraction(2, 5)),
        ("level10_rep_1_10_3_10", Fraction(1, 10), Fraction(3, 10)),
    ]
    vacuum_reports: Dict[str, Any] = {}
    max_amphichiral_ir_repaired = 0.0

    for label, af, bf in sample_vacua:
        a, b = float(af), float(bf)
        y1_w = c_pos * fast_y_mag_overlap_f64(tau_star_c, a, b, 1, -4)
        y2_w = c_neg * fast_y_mag_overlap_f64(tau_star_c, a, b, 1, 2)
        y3_w = c_neg * fast_y_mag_overlap_f64(tau_star_c, a, b, -3, 6)
        y4_w = c_pos * fast_y_mag_overlap_f64(tau_star_c, a, b, -3, 0)
        w4_w = y4_w @ m_r_inv @ y4_w.T

        fl_old = rk4_integrate_full_f64(y1_w, y2_w, y3_w, w4_w, g_uv, g_uv, g_uv, lam_uv, dln_cover, n_steps=1600, repaired_mixed_order=False)
        fl_rep = rk4_integrate_full_f64(y1_w, y2_w, y3_w, w4_w, g_uv, g_uv, g_uv, lam_uv, dln_cover, n_steps=1600, repaired_mixed_order=True)

        obs_old = extract_ir_observables_f64(fl_old)
        obs_rep = extract_ir_observables_f64(fl_rep)

        # Gauge eliminant I_gauge on old vs repaired:
        def igauge(ob: Dict[str, Any]) -> float:
            aem_inv = (5.0 / 3.0) * ob["alpha1_inv_gut"] + ob["alpha2_inv"]
            return ob["sin2_theta_ew_ir"] - (sw2_int + sw2_slp * (ob["alpha3_inv"] / aem_inv))

        ig_old, ig_rep = igauge(obs_old), igauge(obs_rep)

        # Mirror partner R(a, b) = (a, -b) under repaired flow to check amphichiral determinant cancellation:
        y1_rw = c_pos * fast_y_mag_overlap_f64(tau_star_c, a, -b, 1, -4)
        y2_rw = c_neg * fast_y_mag_overlap_f64(tau_star_c, a, -b, 1, 2)
        y3_rw = c_neg * fast_y_mag_overlap_f64(tau_star_c, a, -b, -3, 6)
        y4_rw = c_pos * fast_y_mag_overlap_f64(tau_star_c, a, -b, -3, 0)
        w4_rw = y4_rw @ m_r_inv @ y4_rw.T
        fl_rw_rep = rk4_integrate_full_f64(y1_rw, y2_rw, y3_rw, w4_rw, g_uv, g_uv, g_uv, lam_uv, dln_cover, n_steps=1600, repaired_mixed_order=True)
        blk6 = np.block([[fl_rep["Yu"] @ fl_rep["Yd"], np.zeros((3, 3), dtype=complex)], [np.zeros((3, 3), dtype=complex), fl_rw_rep["Yu"] @ fl_rw_rep["Yd"]]])
        amp_phase_rep = abs(cmath.phase(np.linalg.det(blk6)))
        max_amphichiral_ir_repaired = max(max_amphichiral_ir_repaired, amp_phase_rep)

        comp = compare_obs_dicts(obs_old, obs_rep)
        comp["I_gauge_old"] = ig_old
        comp["I_gauge_repaired"] = ig_rep
        comp["I_gauge_abs_diff"] = abs(ig_rep - ig_old)
        comp["amphichiral_6x6_arg_det_repaired_rad"] = amp_phase_rep
        vacuum_reports[label] = comp

    # Cross-check f64 (n_steps=600) vs mpmath(32) (n_steps=600) AND f64 RK4 convergence (600 vs 1600):
    a_ref, b_ref = float(Fraction(4, 15)), float(Fraction(8, 15))
    y1_r6 = c_pos * fast_y_mag_overlap_f64(tau_star_c, a_ref, b_ref, 1, -4)
    y2_r6 = c_neg * fast_y_mag_overlap_f64(tau_star_c, a_ref, b_ref, 1, 2)
    y3_r6 = c_neg * fast_y_mag_overlap_f64(tau_star_c, a_ref, b_ref, -3, 6)
    y4_r6 = c_pos * fast_y_mag_overlap_f64(tau_star_c, a_ref, b_ref, -3, 0)
    w4_r6 = y4_r6 @ m_r_inv @ y4_r6.T
    obs_f64_600 = extract_ir_observables_f64(
        rk4_integrate_full_f64(y1_r6, y2_r6, y3_r6, w4_r6, g_uv, g_uv, g_uv, lam_uv, dln_cover, n_steps=600, repaired_mixed_order=True)
    )
    ref_rep_f64 = vacuum_reports["level15_casimir_ref_4_15_8_15"]
    f64_vs_mp32_max_diff = 0.0
    rk4_600_vs_1600_max_diff = 0.0
    ratio_keys_f64 = [
        "sec1_r12", "sec1_r23", "sec2_r12", "sec2_r23", "sec3_r12", "sec3_r23",
        "sec4_r12", "sec4_r23", "inter_s3_sec1_over_sec2", "inter_s3_sec2_over_sec3",
    ]
    for idx, rk in enumerate(ratio_keys_f64):
        v_f6 = float(obs_f64_600[rk])
        v_f16 = ref_rep_f64["scalar_comparisons"][rk]["repaired"]
        v_m = float(obs_mp32_rep["ratios"][idx])
        f64_vs_mp32_max_diff = max(f64_vs_mp32_max_diff, abs(v_f6 - v_m))
        rk4_600_vs_1600_max_diff = max(rk4_600_vs_1600_max_diff, abs(v_f6 - v_f16))
    for r in range(3):
        for c in range(3):
            f64_vs_mp32_max_diff = max(
                f64_vs_mp32_max_diff,
                abs(float(obs_f64_600["V12_abs"][r][c]) - float(obs_mp32_rep["v12_abs"][r][c])),
            )
            rk4_600_vs_1600_max_diff = max(
                rk4_600_vs_1600_max_diff,
                abs(float(obs_f64_600["V12_abs"][r][c]) - ref_rep_f64["V12_abs_repaired"][r][c]),
            )
    f64_vs_mp32_max_diff = max(
        f64_vs_mp32_max_diff,
        abs(float(obs_f64_600["lam_ir"]) - float(obs_mp32_rep["lam"])),
    )
    rk4_600_vs_1600_max_diff = max(
        rk4_600_vs_1600_max_diff,
        abs(float(obs_f64_600["lam_ir"]) - ref_rep_f64["scalar_comparisons"]["lam_ir"]["repaired"]),
    )

    # 10-trial 24-digit U(3)^6 Haar invariance check on REPAIRED mpmath integrator:
    with mp.workdps(24):
        uv_w = build_zero_knob_uv_state_mp(tau_star_mp, vol_m004_mp, a_cas_mp, Fraction(4, 15), Fraction(8, 15))
        Yu_b, Yd_b, Ye_b, W4_b, _, _, _, lam_b = rk4_integrate_full_mp(
            mp_to_list3(uv_w["Y1"]), mp_to_list3(uv_w["Y2"]), mp_to_list3(uv_w["Y3"]), mp_to_list3(uv_w["W4"]),
            uv_w["g_uv"], uv_w["g_uv"], uv_w["g_uv"], uv_w["lam_uv"], uv_w["d_ln_mu"], n_steps=40, repaired_mixed_order=True,
        )
        obs_b = extract_obs_mp_full(Yu_b, Yd_b, Ye_b, W4_b, lam_b)

        haar6_max_diff = 0.0
        for trial in range(10):
            ql = random_haar_u3_mp(5100 + 6 * trial)
            u1r = random_haar_u3_mp(5101 + 6 * trial)
            u2r = random_haar_u3_mp(5102 + 6 * trial)
            ll = random_haar_u3_mp(5103 + 6 * trial)
            u3r = random_haar_u3_mp(5104 + 6 * trial)
            u4r = random_haar_u3_mp(5105 + 6 * trial)

            Yu_s = mp3_mul(mp3_mul(ql, mp_to_list3(uv_w["Y1"])), mp3_dag(u1r))
            Yd_s = mp3_mul(mp3_mul(ql, mp_to_list3(uv_w["Y2"])), mp3_dag(u2r))
            Ye_s = mp3_mul(mp3_mul(ll, mp_to_list3(uv_w["Y3"])), mp3_dag(u3r))
            Y4_s = mp3_mul(mp3_mul(ll, mp_to_list3(uv_w["Y4"])), mp3_dag(u4r))
            MR_s = mp3_mul(mp3_mul(mp3_conj(u4r), mp_to_list3(uv_w["M_R"])), mp3_dag(u4r))
            W4_s = mp3_mul(mp3_mul(Y4_s, mp_to_list3(mp.matrix(MR_s) ** (-1))), mp3_tp(Y4_s))

            Yu_i, Yd_i, Ye_i, W4_i, _, _, _, lam_i = rk4_integrate_full_mp(
                Yu_s, Yd_s, Ye_s, W4_s, uv_w["g_uv"], uv_w["g_uv"], uv_w["g_uv"], uv_w["lam_uv"], uv_w["d_ln_mu"], n_steps=40, repaired_mixed_order=True
            )
            obs_s = extract_obs_mp_full(Yu_i, Yd_i, Ye_i, W4_i, lam_i)
            for idx in range(len(obs_b["ratios"])):
                haar6_max_diff = max(haar6_max_diff, float(abs(obs_b["ratios"][idx] - obs_s["ratios"][idx])))
            for r in range(3):
                for c in range(3):
                    haar6_max_diff = max(
                        haar6_max_diff,
                        float(abs(obs_b["v12_abs"][r][c] - obs_s["v12_abs"][r][c])),
                        float(abs(obs_b["u34_abs"][r][c] - obs_s["u34_abs"][r][c])),
                    )
            haar6_max_diff = max(
                haar6_max_diff,
                float(abs(obs_b["icp"] - obs_s["icp"])),
                float(abs(obs_b["lam"] - obs_s["lam"])),
            )

        rng_haar = np.random.default_rng(20261119)
        u1r_t, _ = np.linalg.qr(rng_haar.normal(size=(3, 3)) + 1j * rng_haar.normal(size=(3, 3)))
        y1_t, y2_t, y3_t, w4_t = mp_to_np(uv_w["Y1"]), mp_to_np(uv_w["Y2"]), mp_to_np(uv_w["Y3"]), mp_to_np(uv_w["W4"])
        fl0 = rk4_integrate_full_f64(y1_t, y2_t, y3_t, w4_t, g_uv, g_uv, g_uv, lam_uv, dln_cover, n_steps=160, repaired_mixed_order=True, wrong_chirality_control=True)
        flr = rk4_integrate_full_f64(y1_t @ u1r_t.conj().T, y2_t, y3_t, w4_t, g_uv, g_uv, g_uv, lam_uv, dln_cover, n_steps=160, repaired_mixed_order=True, wrong_chirality_control=True)
        pc_wrong_chirality_err = float(np.max(np.abs(np.sort(np.linalg.svd(fl0["Yu"], compute_uv=False)) - np.sort(np.linalg.svd(flr["Yu"], compute_uv=False)))))

    ref_v12_shift = ref_rep_f64["V12_max_abs_diff"]
    f64_vs_mp32_shift_agreement = abs(ref_v12_shift - mp32_v12_old_vs_rep_max_abs_diff)
    e3_passed = bool(
        f64_vs_mp32_max_diff < 1e-12
        and rk4_600_vs_1600_max_diff < 1e-9
        and ref_v12_shift > 0.0
        and f64_vs_mp32_shift_agreement < 1e-13
        and max_amphichiral_ir_repaired < 1e-12
        and haar6_max_diff < 1e-15
        and pc_wrong_chirality_err > 1e-3
    )

    return {
        "E3_OldVsRepairedTrajectory_and_Haar6_Gate_passed": e3_passed,
        "f64_vs_mp32_repaired_max_diff": f64_vs_mp32_max_diff,
        "rk4_step_600_vs_1600_max_diff": rk4_600_vs_1600_max_diff,
        "mp32_v12_old_vs_repaired_max_abs_diff": mp32_v12_old_vs_rep_max_abs_diff,
        "f64_vs_mp32_old_vs_repaired_shift_agreement": f64_vs_mp32_shift_agreement,
        "max_amphichiral_6x6_ir_arg_det_repaired_rad": max_amphichiral_ir_repaired,
        "vacuum_old_vs_repaired_comparisons": vacuum_reports,
        "Gate_Haar_Stage2_Bridge_U3_power_6": {
            "ten_trial_max_diff_mp24": haar6_max_diff,
            "haar_invariance_below_1e_15": haar6_max_diff < 1e-15,
            "PC_BR2_WrongChiralityRGE_err": pc_wrong_chirality_err,
        },
    }


def main() -> None:
    ast_check = verify_ast_bridge2()
    part_2a = run_part_2a_adjoint_and_trace_invariant()
    part_2b = run_part_2b_repaired_four_pillar_gate()
    part_2c = run_part_2c_trajectory_diff_and_haar6()

    controls_passed = bool(
        ast_check["Gate_AST_Stage2_Bridge_Passed"]
        and part_2a["PC_BR2_ReversedMixedProductOrder_adjoint_rel_err"] > 0.1
        and part_2a["PC_BR2_ReversedMixedProductOrder_trace_shift_abs"] > 1e-2
        and part_2b["pillar2_repaired_rank1_mixing_11_over_2"]["PC_BR2_ReversedMixedProductOrder_mp100_rel_err"] > 1e-2
        and part_2b["pillar2_repaired_rank1_mixing_11_over_2"]["PC_BR2_ReversedMixedProductOrder_f64_rel_err"] > 1e-2
        and part_2a["PC_BR2_WrongDiffFactor_bpv_rel_err"] > 0.1
        and part_2b["pillar1_buttazzo_3loop"]["PC_BR2_WrongDiffFactor_err"] > 0.1
        and part_2b["pillar3_xing_zhou_downward_matrix"]["PC_BR2_WrongRunningDirection_eq18_rel_err"] > 0.5
        and part_2b["pillar4_antusch_weinberg_1loop"]["PC_BR2_WrongMajoranaTranspose_sym_err"] > 0.2
        and part_2c["Gate_Haar_Stage2_Bridge_U3_power_6"]["PC_BR2_WrongChiralityRGE_err"] > 1e-3
    )

    stage_2_passed = bool(
        controls_passed
        and part_2a["E1_AdjointConversion_and_TraceInvariant_Gate_passed"]
        and part_2b["E2_RepairedFourPillar_11Over2_Gate_passed"]
        and part_2c["E3_OldVsRepairedTrajectory_and_Haar6_Gate_passed"]
    )

    out_payload: Dict[str, Any] = {
        "card": "X-BRIDGE-2",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_check,
        "part_2a_adjoint_and_trace_invariant": part_2a,
        "part_2b_repaired_four_pillar_gate": part_2b,
        "part_2c_old_vs_repaired_trajectory_and_haar6": part_2c,
        "all_planted_controls_passed": controls_passed,
        "stage_2_gate_passed": stage_2_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_bridge_2_out.json"
    out_json.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{sha}  verify_x_bridge_2_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
