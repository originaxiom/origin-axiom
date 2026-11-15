#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-RELATIONS-1:
  Universal Selection-Free Gauge & Electroweak-Scalar Relations Across Every History,
  Measure, Collar Orientation, and Scale (Zero Parameters, Zero Discrete Selection Bits,
  Dynamic QCD-Pole Confinement Exclusion, Post-RGE U(3)^6 Haar Invariance, and Explicit Kill Lines; 0 of 19).

Empirical Firewall: 0 of 19 (zero Standard Model empirical targets read, imported, or compared;
literature RGE solver benchmark floats are strictly AST-isolated inside run_part_1a_literature_rge_solver_gate).
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


# ============================================================================
# SECTION 0: AST SOURCE AUDIT (ZERO IMPORTS & MODEL ZERO-FLOAT ISOLATION)
# ============================================================================

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

TARGET_FREE_MODEL_FUNCTIONS: Set[str] = {
    "bloch_wigner_mp",
    "z2_from_z1_gluing",
    "tau_nz_from_z1",
    "neg_vol_on_gluing_curve",
    "s_eff_joint_3d_2d",
    "solve_joint_3var_newton",
    "derive_su5_universal_1loop_eliminants_exact",
}


def verify_ast_relations1() -> Dict[str, Any]:
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
        "Gate_AST_Stage1_Relations_Passed": passed,
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "inspected_target_free_model_functions": sorted(found_funcs),
        "float_literals_in_target_free_model_functions": float_lits,
        "sqrt3_calls_in_target_free_model_functions": sqrt3_calls,
    }

# SECTION 1: TWO-LOOP SM MATRIX + ONE-LOOP WEINBERG RGE KERNELS (F64 & MPMATH)
# ============================================================================

K1_F64 = 1.0 / (16.0 * math.pi * math.pi)
K2_F64 = K1_F64 * K1_F64


def svd_ascending_np(mat: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    u_m, s_v, _ = np.linalg.svd(mat)
    idx = np.argsort(s_v)
    return u_m[:, idx], s_v[idx]


def takagi_symmetric_ascending_np(w_sym: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Extracts left unitary U_nu and ascending singular values of a complex symmetric
    matrix W = U_nu diag(s_1, s_2, s_3) U_nu^T with distinct singular values via W W^dag.
    """
    h_w = w_sym @ w_sym.conj().T
    vals, vecs = np.linalg.eigh(h_w)
    idx = np.argsort(np.real(vals))
    s_asc = np.sqrt(np.maximum(np.real(vals[idx]), 0.0))
    u_asc = vecs[:, idx]
    return u_asc, s_asc


def sm_2loop_plus_weinberg_rhs_f64(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    W4: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    kappa_comm: float = 0.0,
    wrong_chirality_control: bool = False,
    wrong_majorana_transpose: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
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

    b2_Yu = (
        1.5 * (Hu @ Hu)
        - (Hu @ Hd)
        - 0.25 * (Hd @ Hu)
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
    if kappa_comm != 0.0:
        b2_Yu = b2_Yu + kappa_comm * ((Hu @ Hd - Hd @ Hu) @ Yu)

    b2_Yd = (
        1.5 * (Hd @ Hd)
        - (Hd @ Hu)
        - 0.25 * (Hu @ Hd)
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

    # Antusch et al. (2001) 1-loop dimension-5 Weinberg/seesaw operator RGE:
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
        k1 = sm_2loop_plus_weinberg_rhs_f64(Yu, Yd, Ye, W4, g1, g2, g3, lam, 0.0, wrong_chirality_control, False)
        k2 = sm_2loop_plus_weinberg_rhs_f64(
            Yu + 0.5 * dt * k1[0], Yd + 0.5 * dt * k1[1], Ye + 0.5 * dt * k1[2], W4 + 0.5 * dt * k1[3],
            g1 + 0.5 * dt * k1[4], g2 + 0.5 * dt * k1[5], g3 + 0.5 * dt * k1[6], lam + 0.5 * dt * k1[7],
            0.0, wrong_chirality_control, False,
        )
        k3 = sm_2loop_plus_weinberg_rhs_f64(
            Yu + 0.5 * dt * k2[0], Yd + 0.5 * dt * k2[1], Ye + 0.5 * dt * k2[2], W4 + 0.5 * dt * k2[3],
            g1 + 0.5 * dt * k2[4], g2 + 0.5 * dt * k2[5], g3 + 0.5 * dt * k2[6], lam + 0.5 * dt * k2[7],
            0.0, wrong_chirality_control, False,
        )
        k4 = sm_2loop_plus_weinberg_rhs_f64(
            Yu + dt * k3[0], Yd + dt * k3[1], Ye + dt * k3[2], W4 + dt * k3[3],
            g1 + dt * k3[4], g2 + dt * k3[5], g3 + dt * k3[6], lam + dt * k3[7],
            0.0, wrong_chirality_control, False,
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


# ============================================================================
# SECTION 2: PART 5A — FOUR-PILLAR AST-ISOLATED LITERATURE RGE GATE
# ============================================================================

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


def run_part_1a_literature_rge_solver_gate() -> Dict[str, Any]:
    """
    AST-isolated 4-pillar published RGE benchmark gate (Guardrail 4 + Codex Finding 7).
    """
    # Pillar 1: 1-loop closed-form check + Buttazzo et al. (2013) 3-loop Planck benchmark
    Yu_z = np.zeros((3, 3), dtype=complex)
    Yd_z = np.zeros((3, 3), dtype=complex)
    Ye_z = np.zeros((3, 3), dtype=complex)
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
    g_exact = g_num * 0.0
    for idx, g0 in enumerate([g1_i, g2_i, g3_i]):
        g_exact[idx] = g0 / math.sqrt(1.0 - 2.0 * K1_F64 * b_1l[idx] * (g0 ** 2) * dln_test)
    gauge_1loop_err = float(np.max(np.abs(g_num - g_exact)))

    # Planted control PC_REL1_WrongDiffFactor: omit factor of 2 between d/d ln mu and d/d ln mu^2
    g_wrong = np.array(
        [
            g0 / math.sqrt(1.0 - K1_F64 * b_1l[idx] * (g0 ** 2) * dln_test)
            for idx, g0 in enumerate([g1_i, g2_i, g3_i])
        ]
    )
    pc_wrong_diff_factor_err = float(np.max(np.abs(g_wrong - g_exact)))

    # Buttazzo 3-loop Planck extrapolation:
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

    # Pillar 2: Barger, Berger & Ohmann (PRD 47 (1993) 1093, Eq. 24) Noncommuting 2-Loop Matrix Yukawa Gate
    # + Codex's Planted Commutator Perturbation delta beta_{Y_u} = kappa [H_u, H_d] Y_u (Finding 7)!
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
    dYu_c, dYd_c, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_nc, Yd_nc, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, 0.0)
    dln_v23_num = (
        math.log(v23_mod(Yu_nc + dt_b * dYu_c, Yd_nc + dt_b * dYd_c))
        - math.log(v23_mod(Yu_nc - dt_b * dYu_c, Yd_nc - dt_b * dYd_c))
    ) / (2.0 * dt_b)

    bbo_1l = -1.5 * (yt_b ** 2 + yb_b ** 2)
    bbo_2l = (
        6.5 * (yt_b ** 4 + yb_b ** 4)
        + 7.0 * (yt_b ** 2) * (yb_b ** 2)
        + 1.25 * (ytau_b ** 2) * (yt_b ** 2 + yb_b ** 2)
        - 16.0 * (g3_b ** 2) * (yt_b ** 2 + yb_b ** 2)
        + (9.0 / 16.0) * (g2_b ** 2) * (yt_b ** 2 + yb_b ** 2)
        - (79.0 / 80.0) * (g1_b ** 2) * (yt_b ** 2)
        - (43.0 / 80.0) * (g1_b ** 2) * (yb_b ** 2)
    )
    part1_bbo = -(c_b ** 2) * K1_F64 * bbo_1l
    part2_bbo = -(c_b ** 2) * K2_F64 * bbo_2l
    part2_num = dln_v23_num - part1_bbo
    bbo_2loop_noncommuting_rel_err = abs(part2_num - part2_bbo) / abs(part2_bbo)

    # Planted control PC_REL1_CommutatorPerturbation (kappa = 0.75):
    kappa_ctrl = 0.75
    Yu_dg = np.diag([0.0, 0.0, yt_b]).astype(complex)
    Yd_dg = np.diag([0.0, 0.0, yb_b]).astype(complex)
    dYu_dg0, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_dg, Yd_dg, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, 0.0)
    dYu_dgk, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_dg, Yd_dg, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, kappa_ctrl)
    pc_comm_diag_buttazzo_diff = float(np.max(np.abs(dYu_dg0 - dYu_dgk)))

    dYu_k, dYd_k, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_nc, Yd_nc, Ye_nc, W4_z, g1_b, g2_b, g3_b, lam_b, kappa_ctrl)
    dln_v23_kappa = (
        math.log(v23_mod(Yu_nc + dt_b * dYu_k, Yd_nc + dt_b * dYd_k))
        - math.log(v23_mod(Yu_nc - dt_b * dYu_k, Yd_nc - dt_b * dYd_k))
    ) / (2.0 * dt_b)
    pc_comm_bbo_2loop_rel_err = abs((dln_v23_kappa - part1_bbo) - part2_bbo) / abs(part2_bbo)
    exact_comm_shift = kappa_ctrl * K2_F64 * (c_b ** 2) * (yt_b ** 2) * (yb_b ** 2)
    pc_comm_shift_ratio_to_exact = (dln_v23_kappa - dln_v23_num) / exact_comm_shift

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
                yu2_1
                + 2.0 * np.real(np.diag(um1 @ um1.conj().T))
                + 2.0 * np.real(np.diag(um2 @ um2.conj().T))
                + np.real(np.diag(ue @ ue.conj().T))
            )
        id_fac = math.exp(sign_dir * K1_F64 * int_ad)
        xi_fac = np.exp(-sign_dir * 1.5 * K1_F64 * int_yu2)
        return u_m, d_m, id_fac, xi_fac

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
    W_bad = w_init.copy()
    int_ak = 0.0
    int_ye2 = np.zeros(3, dtype=float)

    def ant_1loop_rhs(u_m, d_m, e_m, w_m, w_b, g1v, g2v, g3v, lamv):
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
        # Planted control on complex non-diagonal He: rotate He by a fixed complex unitary to expose W @ He vs W @ He.T!
        dw_b = K1_F64 * (-1.5 * (he @ w_b + w_b @ he) + ak * w_b)
        thu2, thd2, the2 = float(np.real(np.trace(hu @ hu))), float(np.real(np.trace(hd @ hd))), float(np.real(np.trace(he @ he)))
        dlam = K1_F64 * (
            24.0 * lamv ** 2 + lamv * (4.0 * y2 - 9.0 * g2s - 1.8 * g1s)
            - 2.0 * (3.0 * thu2 + 3.0 * thd2 + the2)
            + (9.0 / 8.0) * g2s ** 2 + (27.0 / 200.0) * g1s ** 2 + (9.0 / 20.0) * g1s * g2s
        )
        return du, dd, de, dw, dw_b, K1_F64 * 4.1 * g1v ** 3, K1_F64 * (-19.0 / 6.0) * g2v ** 3, K1_F64 * (-7.0) * g3v ** 3, dlam, ak, np.real(np.diag(he))

    for _ in range(n_ant):
        s1 = ant_1loop_rhs(Yu_a, Yd_a, Ye_a, W_a, W_bad, g1_a, g2_a, g3_a, lam_a)
        s2 = ant_1loop_rhs(Yu_a + 0.5*dt_a*s1[0], Yd_a + 0.5*dt_a*s1[1], Ye_a + 0.5*dt_a*s1[2], W_a + 0.5*dt_a*s1[3], W_bad + 0.5*dt_a*s1[4], g1_a + 0.5*dt_a*s1[5], g2_a + 0.5*dt_a*s1[6], g3_a + 0.5*dt_a*s1[7], lam_a + 0.5*dt_a*s1[8])
        s3 = ant_1loop_rhs(Yu_a + 0.5*dt_a*s2[0], Yd_a + 0.5*dt_a*s2[1], Ye_a + 0.5*dt_a*s2[2], W_a + 0.5*dt_a*s2[3], W_bad + 0.5*dt_a*s2[4], g1_a + 0.5*dt_a*s2[5], g2_a + 0.5*dt_a*s2[6], g3_a + 0.5*dt_a*s2[7], lam_a + 0.5*dt_a*s2[8])
        s4 = ant_1loop_rhs(Yu_a + dt_a*s3[0], Yd_a + dt_a*s3[1], Ye_a + dt_a*s3[2], W_a + dt_a*s3[3], W_bad + dt_a*s3[4], g1_a + dt_a*s3[5], g2_a + dt_a*s3[6], g3_a + dt_a*s3[7], lam_a + dt_a*s3[8])
        Yu_a += (dt_a / 6.0) * (s1[0] + 2.0 * s2[0] + 2.0 * s3[0] + s4[0])
        Yd_a += (dt_a / 6.0) * (s1[1] + 2.0 * s2[1] + 2.0 * s3[1] + s4[1])
        Ye_a += (dt_a / 6.0) * (s1[2] + 2.0 * s2[2] + 2.0 * s3[2] + s4[2])
        W_a += (dt_a / 6.0) * (s1[3] + 2.0 * s2[3] + 2.0 * s3[3] + s4[3])
        W_bad += (dt_a / 6.0) * (s1[4] + 2.0 * s2[4] + 2.0 * s3[4] + s4[4])
        g1_a += (dt_a / 6.0) * (s1[5] + 2.0 * s2[5] + 2.0 * s3[5] + s4[5])
        g2_a += (dt_a / 6.0) * (s1[6] + 2.0 * s2[6] + 2.0 * s3[6] + s4[6])
        g3_a += (dt_a / 6.0) * (s1[7] + 2.0 * s2[7] + 2.0 * s3[7] + s4[7])
        lam_a += (dt_a / 6.0) * (s1[8] + 2.0 * s2[8] + 2.0 * s3[8] + s4[8])
        int_ak += (dt_a / 6.0) * (s1[9] + 2.0 * s2[9] + 2.0 * s3[9] + s4[9])
        int_ye2 += (dt_a / 6.0) * (s1[10] + 2.0 * s2[10] + 2.0 * s3[10] + s4[10])

    i_kap = math.exp(K1_F64 * int_ak)
    i_lep = np.exp(-1.5 * K1_F64 * int_ye2)
    w_exact = i_kap * (np.diag(i_lep) @ w_init @ np.diag(i_lep))
    antusch_integral_rel_err = float(np.linalg.norm(W_a - w_exact) / np.linalg.norm(w_exact))
    antusch_sym_err = float(np.linalg.norm(W_a - W_a.T) / np.linalg.norm(W_a))

    # Planted control PC_REL1_WrongMajoranaTranspose on complex non-diagonal Ye:
    u_lep_c, _ = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    Ye_c = u_lep_c @ np.diag([0.05, 0.25, 0.80]).astype(complex)
    W_c = u_lep_c @ w_init @ u_lep_c.T
    _, _, _, dW_good_c, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_a0, Yd_a0, Ye_c, W_c, 0.5, 0.5, 0.5, 0.1, 0.0, False, False)
    _, _, _, dW_bad_c, *_ = sm_2loop_plus_weinberg_rhs_f64(Yu_a0, Yd_a0, Ye_c, W_c, 0.5, 0.5, 0.5, 0.1, 0.0, False, True)
    good_sym_c = float(np.linalg.norm(dW_good_c - dW_good_c.T) / np.linalg.norm(dW_good_c))
    pc_wrong_maj_transpose_sym_err = float(np.linalg.norm(dW_bad_c - dW_bad_c.T) / np.linalg.norm(dW_bad_c))

    e1_passed = bool(
        gauge_1loop_err < 1e-12
        and pc_wrong_diff_factor_err > 0.1
        and but_4coupling_rel_err < 2e-3
        and but_lam_abs_err < 5e-4
        and abs(log10_lam_zero - log10_two_lambda_v) < 0.05
        and bbo_2loop_noncommuting_rel_err < 1e-5
        and pc_comm_diag_buttazzo_diff == 0.0
        and pc_comm_bbo_2loop_rel_err > 5e-3
        and abs(pc_comm_shift_ratio_to_exact - 1.0) < 1e-4
        and xz_eq18_rel_err < 1e-12
        and pc_wrong_dir_eq18_rel_err > 0.9
        and antusch_integral_rel_err < 1e-12
        and antusch_sym_err < 1e-15
        and good_sym_c < 1e-15
        and pc_wrong_maj_transpose_sym_err > 0.1
    )

    return {
        "E1_FourPillar_Literature_RGE_Gate_passed": e1_passed,
        "pillar1_buttazzo_3loop": {
            "gauge_1loop_closed_form_err": gauge_1loop_err,
            "PC_REL1_WrongDiffFactor_err": pc_wrong_diff_factor_err,
            "four_coupling_planck_max_rel_err": float(but_4coupling_rel_err),
            "lam_planck_abs_err": float(but_lam_abs_err),
            "log10_Lambda_lam_GeV": float(log10_lam_zero),
            "log10_two_Lambda_V_GeV": float(log10_two_lambda_v),
        },
        "pillar2_bbo_noncommuting_2loop_matrix": {
            "bbo_eq24_pure_2loop_rel_err": float(bbo_2loop_noncommuting_rel_err),
            "PC_REL1_Commutator_diag_buttazzo_diff": pc_comm_diag_buttazzo_diff,
            "PC_REL1_Commutator_bbo_2loop_rel_err": float(pc_comm_bbo_2loop_rel_err),
            "PC_REL1_Commutator_shift_ratio_to_exact": float(pc_comm_shift_ratio_to_exact),
        },
        "pillar3_xing_zhou_downward_matrix": {
            "eq18_naumov_rel_err": float(xz_eq18_rel_err),
            "PC_REL1_WrongRunningDirection_eq18_rel_err": float(pc_wrong_dir_eq18_rel_err),
        },
        "pillar4_antusch_weinberg_1loop": {
            "analytical_integral_rel_err": antusch_integral_rel_err,
            "weinberg_symmetry_err": antusch_sym_err,
            "PC_REL1_WrongMajoranaTranspose_sym_err": pc_wrong_maj_transpose_sym_err,
        },
    }


# ============================================================================
# SECTION 3: TARGET-FREE GEOMETRY, OVERLAPS, SEESAW M_R & MPMATH 2-LOOP RGE
# ============================================================================

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
            b2u = (
                F(3, 2) * Hu2[i][j] - HuHd[i][j] - F(1, 4) * HdHu[i][j] + F(11, 4) * Hd2[i][j]
                + su2_hu * Hu[i][j] + su2_hd * Hd[i][j] + su2_id * d_ij
            )
            lu[i][j] = k1_mp * b1u + k2_mp * b2u

            b1d = sd1_diag * d_ij + F(3, 2) * (Hd[i][j] - Hu[i][j])
            b2d = (
                F(3, 2) * Hd2[i][j] - HdHu[i][j] - F(1, 4) * HuHd[i][j] + F(11, 4) * Hu2[i][j]
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
        s1 = sm_2loop_plus_weinberg_rhs_mp(Yu, Yd, Ye, W4, g1, g2, g3, lam, k1_mp, k2_mp)
        s2 = sm_2loop_plus_weinberg_rhs_mp(
            add_s(Yu, s1[0], half_dt), add_s(Yd, s1[1], half_dt), add_s(Ye, s1[2], half_dt), add_s(W4, s1[3], half_dt),
            g1 + half_dt * s1[4], g2 + half_dt * s1[5], g3 + half_dt * s1[6], lam + half_dt * s1[7], k1_mp, k2_mp,
        )
        s3 = sm_2loop_plus_weinberg_rhs_mp(
            add_s(Yu, s2[0], half_dt), add_s(Yd, s2[1], half_dt), add_s(Ye, s2[2], half_dt), add_s(W4, s2[3], half_dt),
            g1 + half_dt * s2[4], g2 + half_dt * s2[5], g3 + half_dt * s2[6], lam + half_dt * s2[7], k1_mp, k2_mp,
        )
        s4 = sm_2loop_plus_weinberg_rhs_mp(
            add_s(Yu, s3[0], dt), add_s(Yd, s3[1], dt), add_s(Ye, s3[2], dt), add_s(W4, s3[3], dt),
            g1 + dt * s3[4], g2 + dt * s3[5], g3 + dt * s3[6], lam + dt * s3[7], k1_mp, k2_mp,
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



# ============================================================================
# SECTION 4: EXACT SU(5) 1-LOOP ELIMINANTS, HISTORY SWEEP & UNIVERSAL KILL LINES
# ============================================================================

def derive_su5_universal_1loop_eliminants_exact(n_gen: int, n_higgs_doublets: int) -> Dict[str, Fraction]:
    """
    Computes exact rational 1-loop gauge beta-coefficients (b_1, b_2, b_3) and universal
    eliminants directly from explicit 5x5 SU(5) -> SU(3) x SU(2) x U(1)_Y representation traces.
    Contains ZERO float literals (AST-enforced).
    """
    # Explicit diagonal Cartan generators in 5x5 fundamental V_3 (+) V_2:
    # T3_8 = diag(1, 1, -2, 0, 0) / sqrt(12)  => Tr(T3_8^2) = (1 + 1 + 4)/12 = 1/2
    # T2_3 = diag(0, 0, 0, 1, -1) / 2         => Tr(T2_3^2) = (1 + 1)/4 = 1/2
    # Y_raw = diag(-1/3, -1/3, -1/3, 1/2, 1/2) => Tr(Y_raw^2) = 3*(1/9) + 2*(1/4) = 5/6
    tr_t3_sq = Fraction(1 + 1 + 4, 12)
    tr_t2_sq = Fraction(1 + 1, 4)
    tr_y_raw_sq = Fraction(3, 9) + Fraction(2, 4)
    k1_over_k2 = tr_t2_sq / tr_y_raw_sq  # Exact 3/5!

    # One chiral generation = 5_bar (+) 10 under SU(3) x SU(2) x U(1)_Y:
    # Weyl fermion Dynkin indices (2/3 * T(R)):
    #   Q_L = (3, 2, +1/6):  d_3 = 2*(1/2) = 1, d_2 = 3*(1/2) = 3/2, d_1 = (3/5)*6*(1/36) = 1/10
    #   u_R^c = (3*, 1, -2/3): d_3 = 1/2,       d_2 = 0,             d_1 = (3/5)*3*(4/9)  = 4/5
    #   d_R^c = (3*, 1, +1/3): d_3 = 1/2,       d_2 = 0,             d_1 = (3/5)*3*(1/9)  = 1/5
    #   L_L = (1, 2, -1/2):    d_3 = 0,         d_2 = 1/2,           d_1 = (3/5)*2*(1/4)  = 3/10
    #   e_R^c = (1, 1, +1):    d_3 = 0,         d_2 = 0,             d_1 = (3/5)*1*(1)    = 3/5
    fermion_1 = Fraction(2, 3) * (
        k1_over_k2 * (6 * Fraction(1, 36) + 3 * Fraction(4, 9) + 3 * Fraction(1, 9) + 2 * Fraction(1, 4) + Fraction(1, 1))
    )
    fermion_2 = Fraction(2, 3) * (3 * Fraction(1, 2) + Fraction(1, 2))
    fermion_3 = Fraction(2, 3) * (2 * Fraction(1, 2) + Fraction(1, 2) + Fraction(1, 2))

    # Complex Higgs doublet H = (1, 2, +1/2): scalar Dynkin index = (1/3) * T(R):
    higgs_1 = Fraction(1, 3) * (k1_over_k2 * 2 * Fraction(1, 4))
    higgs_2 = Fraction(1, 3) * Fraction(1, 2)
    higgs_3 = Fraction(0, 1)

    # Gauge self-coupling (-11/3 * C_2(G)):
    gauge_1 = Fraction(0, 1)
    gauge_2 = -Fraction(11, 3) * 2
    gauge_3 = -Fraction(11, 3) * 3

    b1 = gauge_1 + n_gen * fermion_1 + n_higgs_doublets * higgs_1
    b2 = gauge_2 + n_gen * fermion_2 + n_higgs_doublets * higgs_2
    b3 = gauge_3 + n_gen * fermion_3 + n_higgs_doublets * higgs_3

    c1 = b2 - b3
    c2 = b3 - b1
    c3 = b1 - b2

    # Solve (b2 - b3)*a1_inv + (b3 - b1)*a2_inv + (b1 - b2)*a3_inv = 0
    # with a1_inv = k1_over_k2 * a_em_inv * (1 - sw2) and a2_inv = a_em_inv * sw2:
    denom_sw2 = -(k1_over_k2 * c1) + c2  # negative, move to RHS
    sw2_intercept = (k1_over_k2 * c1) / (-denom_sw2)
    sw2_slope_a3_over_aem = c3 / (-denom_sw2)

    return {
        "k2_over_k1": k1_over_k2,
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "c1_b2_minus_b3": c1,
        "c2_b3_minus_b1": c2,
        "c3_b1_minus_b2": c3,
        "sw2_intercept": sw2_intercept,
        "sw2_slope": sw2_slope_a3_over_aem,
    }


def run_stage1_relations() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    rge_gate = run_part_1a_literature_rge_solver_gate()

    # Verify exact generation-number independence of (b2 - b3, b3 - b1, b1 - b2) for N_g in 1..6:
    elim_ng3 = derive_su5_universal_1loop_eliminants_exact(3, 1)
    ng_diffs_zero = all(
        derive_su5_universal_1loop_eliminants_exact(ng, 1)["c1_b2_minus_b3"] == elim_ng3["c1_b2_minus_b3"]
        and derive_su5_universal_1loop_eliminants_exact(ng, 1)["c2_b3_minus_b1"] == elim_ng3["c2_b3_minus_b1"]
        and derive_su5_universal_1loop_eliminants_exact(ng, 1)["c3_b1_minus_b2"] == elim_ng3["c3_b1_minus_b2"]
        for ng in range(1, 7)
    )
    exact_1loop_coeffs_match = (
        elim_ng3["k2_over_k1"] == Fraction(3, 5)
        and elim_ng3["c1_b2_minus_b3"] == Fraction(23, 6)
        and elim_ng3["c2_b3_minus_b1"] == Fraction(-111, 10)
        and elim_ng3["c3_b1_minus_b2"] == Fraction(109, 15)
        and elim_ng3["sw2_intercept"] == Fraction(23, 134)
        and elim_ng3["sw2_slope"] == Fraction(109, 201)
    )

    # Test 1-loop eliminants across 60 random combinations of (alpha_UV_inv, d_ln_mu, N_g):
    rng = np.random.default_rng(20261115)
    max_1loop_L_err = 0.0
    max_1loop_I_err = 0.0
    for _ in range(60):
        ng_r = int(rng.integers(1, 6))
        el_r = derive_su5_universal_1loop_eliminants_exact(ng_r, 1)
        b_vec = [float(el_r["b1"]), float(el_r["b2"]), float(el_r["b3"])]
        a_uv_inv = float(rng.uniform(22.0, 60.0))
        dln = float(rng.uniform(-34.0, -10.0))
        # Ensure perturbative:
        if min(a_uv_inv + (b_vec[k] / (2.0 * math.pi)) * abs(dln) for k in range(3)) <= 1.5:
            continue
        g0 = math.sqrt(4.0 * math.pi / a_uv_inv)
        a_ir = [1.0 / ((g0 ** 2 / (4.0 * math.pi)) / (1.0 - 2.0 * K1_F64 * b_vec[k] * (g0 ** 2) * dln)) for k in range(3)]
        l_val = (23.0 / 6.0) * a_ir[0] - (111.0 / 10.0) * a_ir[1] + (109.0 / 15.0) * a_ir[2]
        a_em = (5.0 / 3.0) * a_ir[0] + a_ir[1]
        sw2 = (0.6 * a_ir[1]) / (a_ir[0] + 0.6 * a_ir[1])
        i_val = sw2 - (23.0 / 134.0 + (109.0 / 201.0) * (a_ir[2] / a_em))
        max_1loop_L_err = max(max_1loop_L_err, abs(l_val))
        max_1loop_I_err = max(max_1loop_I_err, abs(i_val))

    # Planted controls on 1-loop universal gauge structure:
    # PC_REL1_WrongHyperchargeNorm: use k2/k1 = 1 instead of 3/5 at a_ir = [57.44, 23.90, 5.30]:
    sw2_good = (0.6 * 23.90) / (57.44 + 0.6 * 23.90)
    sw2_bad_norm = 23.90 / (57.44 + 23.90)
    pc_wrong_hypercharge_norm_shift = abs(sw2_bad_norm - sw2_good)
    # PC_REL1_ExtraHiggsDoublets: N_H = 5 instead of N_H = 1 on exact N_H=5 trajectory:
    el_nh5 = derive_su5_universal_1loop_eliminants_exact(3, 5)
    a_nh5 = [40.0 + (float(el_nh5[k]) / (2.0 * math.pi)) * 29.0 for k in ("b1", "b2", "b3")]
    pc_extra_higgs_L_violation = abs((23.0 / 6.0) * a_nh5[0] - (111.0 / 10.0) * a_nh5[1] + (109.0 / 15.0) * a_nh5[2])

    part_1a = {
        "E1_FourPillar_and_Exact1Loop_Eliminant_Gate_passed": bool(
            rge_gate["E1_FourPillar_Literature_RGE_Gate_passed"]
            and ng_diffs_zero
            and exact_1loop_coeffs_match
            and max_1loop_L_err < 1e-12
            and max_1loop_I_err < 1e-14
            and pc_wrong_hypercharge_norm_shift > 0.08
            and pc_extra_higgs_L_violation > 1.0
        ),
        "four_pillar_rge_solver_gate": rge_gate,
        "su5_universal_1loop_eliminants": {
            "generation_independence_verified_Ng_1_to_6": ng_diffs_zero,
            "exact_rational_coeffs": {k: str(v) for k, v in elim_ng3.items()},
            "random_60_trajectory_max_L_gauge_err": max_1loop_L_err,
            "random_60_trajectory_max_I_gauge_err": max_1loop_I_err,
            "PC_REL1_WrongHyperchargeNorm_shift": pc_wrong_hypercharge_norm_shift,
            "PC_REL1_ExtraHiggsDoublets_L_violation": pc_extra_higgs_L_violation,
        },
    }

    # Part 1B & 1C: Target-free m004 joint stabilization + full ensemble sweep across all 44 vacua!
    with mp.workdps(24):
        _VCAS_CACHE.clear()
        x_s, y_s, a_cas_mp = solve_joint_3var_newton(Fraction(3, 5), Fraction(4, 5), Fraction(19, 1))
        z1_s = mp.mpc(x_s, y_s)
        tau_star = tau_nz_from_z1(z1_s)
        vol_m004 = -neg_vol_on_gluing_curve(x_s, y_s)
        a_tree_mp = 6 * mp.pi

        # Enumerate all 44 non-trivial torsion points in ker(M^{-4} - I_2) \ {0}:
        m_inv = np.array([[1, -1], [-1, 2]], dtype=int)
        m_inv4 = np.linalg.matrix_power(m_inv, 4)
        ker44: List[Tuple[Fraction, Fraction]] = []
        for p in range(45):
            for q in range(45):
                if p == 0 and q == 0:
                    continue
                af, bf = Fraction(p, 45), Fraction(q, 45)
                ai = af * int(m_inv4[0, 0]) + bf * int(m_inv4[1, 0])
                bi = af * int(m_inv4[0, 1]) + bf * int(m_inv4[1, 1])
                if (ai - af).denominator == 1 and (bi - bf).denominator == 1:
                    ker44.append((af, bf))

        raw_cache = {}
        m_r_mp = majorana_puncture_jet_mp(tau_star)
        m_r_np = mp_to_np(m_r_mp)
        m_r_inv = np.linalg.inv(m_r_np)
        tau_star_c = complex(tau_star)

        def fast_y_mag_f64(tau_c: complex, a: float, b: float, ql: int, qr: int) -> np.ndarray:
            qh = -(ql + qr)
            t1, t2 = tau_c.real, tau_c.imag
            u0 = 1.0 / math.sqrt(6.0)
            us = math.sqrt(t2)
            st2 = math.sqrt(t2)
            spi = math.sqrt(math.pi)
            th = 42.0
            km = int(math.ceil(math.sqrt(th * 6.0 / (math.pi * t2)) / 3.0)) + 2
            lq = int(math.ceil(math.sqrt(th * 6.0 / (math.pi * t2)))) + 3
            lr = int(math.ceil(math.sqrt(th / math.pi))) + 2

            def erfcx_f(xv: float) -> float:
                if xv >= 26.0:
                    x2 = xv * xv
                    return (1.0 / (spi * xv)) * (1.0 - 0.5 / x2 + 0.75 / (x2 * x2))
                return math.exp(xv * xv) * math.erfc(xv)

            def erfc_i(al: float, be: float) -> float:
                xm = al * u0 - be / u0
                xp = al * u0 + be / u0
                ee = (al * u0) ** 2 + (be / u0) ** 2
                if xm >= 0.0:
                    return 0.0 if ee > th else (spi / (2.0 * al)) * math.exp(-ee) * (erfcx_f(xm) + erfcx_f(xp))
                if 2.0 * al * be > th:
                    return 0.0
                p1 = 2.0 * math.exp(-2.0 * al * be)
                p2 = 0.0 if ee > th else math.exp(-ee) * (erfcx_f(xp) - erfcx_f(-xm))
                return (spi / (2.0 * al)) * (p1 + p2)

            def fp(uv: float, bv: float) -> float:
                if bv == 0.0:
                    return 2.0 * uv
                bvu = bv / uv
                return 0.0 if bvu * bvu > th else 2.0 * math.exp(-bvu * bvu) * (uv - spi * bv * erfcx_f(bvu))

            ym = np.zeros((3, 3), dtype=complex)
            for i in range(3):
                cl = (i + 0.5 + ql * a) / 3.0
                za = -2.0 * math.pi * (ql * b / 3.0) * (i + 0.5)
                zp = complex(math.cos(za), math.sin(za))
                for j in range(3):
                    cr = (j + 0.5 - qr * a) / 3.0
                    acc = 0.0j
                    for k in range(-km, km + 1):
                        n = (j - i) - 3 * k
                        na = n + qh * a
                        dk = na / 3.0
                        xi0 = 0.5 * (cl + cr - k)
                        x0 = na * t1 + qh * b
                        a0 = math.pi * dk * ((qr - ql) * b - 3.0)
                        bp0 = complex(math.cos(a0), math.sin(a0))
                        if abs(na) > 1e-13:
                            al = math.sqrt(math.pi * t2) * abs(na)
                            lln = int(math.ceil(th / (2.0 * math.pi * t2 * abs(na)))) + 2
                            lmx = max(lln, lq)
                            lc = int(round(xi0))
                            sub = 0.0j
                            for dl in range(-lmx, lmx + 1):
                                li = lc + dl
                                be = math.sqrt(math.pi * t2) * abs(li - xi0)
                                iv = st2 * erfc_i(al, be)
                                if iv != 0.0:
                                    ag = 2.0 * math.pi * (li - xi0) * x0
                                    sub += iv * complex(math.cos(ag), math.sin(ag))
                            acc += bp0 * sub
                        else:
                            lc = int(round(xi0))
                            s1 = 0.0j
                            for dl in range(-lr, lr + 1):
                                li = lc + dl
                                be = math.sqrt(math.pi * t2) * abs(li - xi0)
                                iv = st2 * (fp(us, be) - fp(u0, be))
                                if iv != 0.0:
                                    ag = 2.0 * math.pi * (li - xi0) * x0
                                    s1 += iv * complex(math.cos(ag), math.sin(ag))
                            mc = int(round(-x0))
                            s2 = 0.0j
                            for dm in range(-lr, lr + 1):
                                mi = mc + dm
                                mx = mi + x0
                                if abs(mx) > 1e-13 and math.pi * mx * mx <= th:
                                    ag = 2.0 * math.pi * mi * xi0
                                    s2 += (t2 / (math.pi * mx * mx)) * math.exp(-math.pi * mx * mx) * complex(math.cos(ag), math.sin(ag))
                            acc += bp0 * (s1 + s2)
                    ym[i, j] = zp * acc
            return ym

        for (af, bf) in ker44:
            a_f, b_f = float(af), float(bf)
            raw_cache[(af, bf)] = (
                fast_y_mag_f64(tau_star_c, a_f, b_f, 1, -4),
                fast_y_mag_f64(tau_star_c, a_f, b_f, 1, 2),
                fast_y_mag_f64(tau_star_c, a_f, b_f, -3, 6),
                fast_y_mag_f64(tau_star_c, a_f, b_f, -3, 0),
            )

        amp0 = float(collar_amp_mp(0, mp.im(tau_star)))
        ampp = float(collar_amp_mp(1, mp.im(tau_star)))
        ampm = float(collar_amp_mp(-1, mp.im(tau_star)))
        dln_cover = -float((mp.mpf(45) / mp.pi) * vol_m004)

        # Verify dynamic QCD confining-pole exclusion of (2D horotorus measure, cover-instanton interval):
        pole_dln_2d_cas = float((2 * mp.pi / 7) * a_cas_mp)
        pole_dln_2d_tree = float((2 * mp.pi / 7) * a_tree_mp)
        a3_1l_2d_at_cover = float(a_cas_mp) - (7.0 / (2.0 * math.pi)) * abs(dln_cover)
        dynamic_2d_cover_excluded = (pole_dln_2d_cas < abs(dln_cover)) and (a3_1l_2d_at_cover < -10.0)

        # Sweep all perturbative histories across:
        #   - 3D_Cas and 3D_tree at dln_cover AND at dynamical 1-loop a3_target in {7.0, 9.0}
        #   - 2D_Cas and 2D_tree at dynamical perturbative 1-loop a3_target in {7.0, 9.0}
        #   - All 3 collar assignments kappa_mode in (+1, -1, 0)
        #   - All 44 non-trivial torsion points in ker(M^{-4} - I_2) \ {0}!
        all_I_gauge: List[float] = []
        all_L_gauge: List[float] = []
        surviving_3d_cover_I_gauge: List[float] = []
        surviving_3d_cover_L_gauge: List[float] = []
        surviving_3d_cover_sqrt2lam: List[float] = []
        collar_pos_3d_sqrt2lam: List[float] = []
        collar_both_signs_3d_sqrt2lam: List[float] = []
        unlocalized_3d_sqrt2lam: List[float] = []
        all_perturbative_sqrt2lam: List[float] = []
        all_perturbative_lam_raw: List[float] = []

        measure_defs = [
            ("3D_Cas", float(vol_m004 * a_cas_mp)),
            ("3D_tree", float(vol_m004 * a_tree_mp)),
            ("2D_Cas", float(a_cas_mp)),
            ("2D_tree", float(a_tree_mp)),
        ]

        for m_name, a_uv_inv in measure_defs:
            g_uv = math.sqrt(4.0 * math.pi / a_uv_inv)
            lam_uv = 0.2 * g_uv * g_uv
            dln_list = [("qcd_a3_7", -(a_uv_inv - 7.0) * (2.0 * math.pi / 7.0)), ("qcd_a3_9", -(a_uv_inv - 9.0) * (2.0 * math.pi / 7.0))]
            if m_name.startswith("3D"):
                dln_list.insert(0, ("cover_instanton", dln_cover))

            for d_name, d_ln_mu in dln_list:
                for k_mode in (+1, -1, 0):
                    if k_mode == +1:
                        c_14, c_23 = g_uv * amp0 * amp0 * ampp, g_uv * amp0 * amp0 * ampm
                    elif k_mode == -1:
                        c_14, c_23 = g_uv * amp0 * amp0 * ampm, g_uv * amp0 * amp0 * ampp
                    else:
                        c_14, c_23 = g_uv * amp0 * amp0 * amp0, g_uv * amp0 * amp0 * amp0

                    for (af, bf) in ker44:
                        r1, r2, r3, r4 = raw_cache[(af, bf)]
                        y1, y2, y3, y4 = c_14 * r1, c_23 * r2, c_23 * r3, c_14 * r4
                        w4 = y4 @ m_r_inv @ y4.T
                        flow = rk4_integrate_full_f64(y1, y2, y3, w4, g_uv, g_uv, g_uv, lam_uv, d_ln_mu, n_steps=40)
                        g1f, g2f, g3f, lamf = flow["g1"], flow["g2"], flow["g3"], flow["lam"]
                        a1i = 4.0 * math.pi / (g1f ** 2)
                        a2i = 4.0 * math.pi / (g2f ** 2)
                        a3i = 4.0 * math.pi / (g3f ** 2)
                        a_em = (5.0 / 3.0) * a1i + a2i
                        sw2 = (0.6 * a2i) / (a1i + 0.6 * a2i)
                        i_g = sw2 - (23.0 / 134.0 + (109.0 / 201.0) * (a3i / a_em))
                        l_g = (23.0 / 6.0) * a1i - (111.0 / 10.0) * a2i + (109.0 / 15.0) * a3i
                        s2l = math.sqrt(max(2.0 * lamf, 0.0))

                        all_I_gauge.append(i_g)
                        all_L_gauge.append(l_g)
                        all_perturbative_sqrt2lam.append(s2l)
                        all_perturbative_lam_raw.append(lamf)
                        if m_name.startswith("3D") and d_name == "cover_instanton":
                            surviving_3d_cover_I_gauge.append(i_g)
                            surviving_3d_cover_L_gauge.append(l_g)
                            surviving_3d_cover_sqrt2lam.append(s2l)
                            if k_mode == +1:
                                collar_pos_3d_sqrt2lam.append(s2l)
                            if k_mode in (+1, -1):
                                collar_both_signs_3d_sqrt2lam.append(s2l)
                            else:
                                unlocalized_3d_sqrt2lam.append(s2l)

        # 10-trial 24-digit mpmath U(3)^6 Haar basis-scrambling check on UR-1 and UR-2:
        uv_ref = build_zero_knob_uv_state_mp(tau_star, vol_m004, a_cas_mp, Fraction(4, 15), Fraction(8, 15))
        Yu0 = mp_to_list3(uv_ref["Y1"])
        Yd0 = mp_to_list3(uv_ref["Y2"])
        Ye0 = mp_to_list3(uv_ref["Y3"])
        W4_0 = mp_to_list3(uv_ref["W4"])
        _, _, _, _, g1_0m, g2_0m, g3_0m, lam_0m = rk4_integrate_full_mp(
            Yu0, Yd0, Ye0, W4_0, uv_ref["g_uv"], uv_ref["g_uv"], uv_ref["g_uv"], uv_ref["lam_uv"], uv_ref["d_ln_mu"], n_steps=32
        )

        def ur_from_mp(g1m: Any, g2m: Any, g3m: Any, lamm: Any) -> Tuple[Any, Any, Any]:
            a1m = 4 * mp.pi / (g1m ** 2)
            a2m = 4 * mp.pi / (g2m ** 2)
            a3m = 4 * mp.pi / (g3m ** 2)
            aem = (mp.mpf(5) / mp.mpf(3)) * a1m + a2m
            sw2m = (mp.mpf(3) / mp.mpf(5)) * a2m / (a1m + (mp.mpf(3) / mp.mpf(5)) * a2m)
            im = sw2m - (mp.mpf(23) / mp.mpf(134) + (mp.mpf(109) / mp.mpf(201)) * (a3m / aem))
            lm = (mp.mpf(23) / mp.mpf(6)) * a1m - (mp.mpf(111) / mp.mpf(10)) * a2m + (mp.mpf(109) / mp.mpf(15)) * a3m
            return im, lm, mp.sqrt(2 * lamm)

        ur_base = ur_from_mp(g1_0m, g2_0m, g3_0m, lam_0m)
        rng_haar = np.random.default_rng(20261116)
        haar6_max_diff = 0.0
        for trial in range(10):
            ql = random_haar_u3_mp(2000 + 6 * trial)
            u1r = random_haar_u3_mp(2001 + 6 * trial)
            u2r = random_haar_u3_mp(2002 + 6 * trial)
            ll = random_haar_u3_mp(2003 + 6 * trial)
            u3r = random_haar_u3_mp(2004 + 6 * trial)
            u4r = random_haar_u3_mp(2005 + 6 * trial)

            Yu_s = mp3_mul(mp3_mul(ql, Yu0), mp3_dag(u1r))
            Yd_s = mp3_mul(mp3_mul(ql, Yd0), mp3_dag(u2r))
            Ye_s = mp3_mul(mp3_mul(ll, Ye0), mp3_dag(u3r))
            Y4_s = mp3_mul(mp3_mul(ll, mp_to_list3(uv_ref["Y4"])), mp3_dag(u4r))
            MR_s = mp3_mul(mp3_mul(mp3_conj(u4r), mp_to_list3(uv_ref["M_R"])), mp3_dag(u4r))
            MR_s_inv = mp_to_list3(mp.matrix(MR_s) ** (-1))
            W4_s = mp3_mul(mp3_mul(Y4_s, MR_s_inv), mp3_tp(Y4_s))

            _, _, _, _, g1_s, g2_s, g3_s, lam_s = rk4_integrate_full_mp(
                Yu_s, Yd_s, Ye_s, W4_s, uv_ref["g_uv"], uv_ref["g_uv"], uv_ref["g_uv"], uv_ref["lam_uv"], uv_ref["d_ln_mu"], n_steps=32
            )
            ur_s = ur_from_mp(g1_s, g2_s, g3_s, lam_s)
            for k_idx in range(3):
                haar6_max_diff = max(haar6_max_diff, float(abs(ur_base[k_idx] - ur_s[k_idx])))

        # Planted controls for Part 1C:
        # PC_REL1_BrokenDTermQuartic: set lam_UV = 1.2 * g_UV^2 (violating 6D D-term lam_UV = (1/5) g_UV^2)
        r1_415, r2_415, r3_415, r4_415 = raw_cache[(Fraction(4, 15), Fraction(8, 15))]
        g_ref = float(uv_ref["g_uv"])
        c14_ref = g_ref * amp0 * amp0 * ampp
        c23_ref = g_ref * amp0 * amp0 * ampm
        flow_good_dterm = rk4_integrate_full_f64(
            c14_ref * r1_415, c23_ref * r2_415, c23_ref * r3_415, (c14_ref * r4_415) @ m_r_inv @ (c14_ref * r4_415).T,
            g_ref, g_ref, g_ref, 0.2 * g_ref * g_ref, dln_cover, n_steps=200,
        )
        flow_bad_dterm = rk4_integrate_full_f64(
            c14_ref * r1_415, c23_ref * r2_415, c23_ref * r3_415, (c14_ref * r4_415) @ m_r_inv @ (c14_ref * r4_415).T,
            g_ref, g_ref, g_ref, 1.2 * g_ref * g_ref, dln_cover, n_steps=200,
        )
        pc_broken_dterm_shift = abs(math.sqrt(2.0 * flow_bad_dterm["lam"]) - math.sqrt(2.0 * flow_good_dterm["lam"]))

        # PC_REL1_WrongChiralityRGE: right-multiplying 1-loop Yukawa beta breaks U(3)_R invariance:
        u1r_test, _ = np.linalg.qr(rng_haar.normal(size=(3, 3)) + 1j * rng_haar.normal(size=(3, 3)))
        flow_wc0 = rk4_integrate_full_f64(
            c14_ref * r1_415, c23_ref * r2_415, c23_ref * r3_415, (c14_ref * r4_415) @ m_r_inv @ (c14_ref * r4_415).T,
            g_ref, g_ref, g_ref, 0.2 * g_ref * g_ref, dln_cover, n_steps=200, wrong_chirality_control=True,
        )
        flow_wcr = rk4_integrate_full_f64(
            (c14_ref * r1_415) @ u1r_test.conj().T, c23_ref * r2_415, c23_ref * r3_415, (c14_ref * r4_415) @ m_r_inv @ (c14_ref * r4_415).T,
            g_ref, g_ref, g_ref, 0.2 * g_ref * g_ref, dln_cover, n_steps=200, wrong_chirality_control=True,
        )
        s1_wc0 = np.linalg.svd(flow_wc0["Yu"], compute_uv=False)
        s1_wcr = np.linalg.svd(flow_wcr["Yu"], compute_uv=False)
        pc_wrong_chirality_err = float(np.max(np.abs(np.sort(s1_wc0) - np.sort(s1_wcr))))

    i_min_all, i_max_all = float(min(all_I_gauge)), float(max(all_I_gauge))
    l_min_all, l_max_all = float(min(all_L_gauge)), float(max(all_L_gauge))
    i_min_3d, i_max_3d = float(min(surviving_3d_cover_I_gauge)), float(max(surviving_3d_cover_I_gauge))
    l_min_3d, l_max_3d = float(min(surviving_3d_cover_L_gauge)), float(max(surviving_3d_cover_L_gauge))
    s2l_min_pos, s2l_max_pos = float(min(collar_pos_3d_sqrt2lam)), float(max(collar_pos_3d_sqrt2lam))
    s2l_min_col, s2l_max_col = float(min(collar_both_signs_3d_sqrt2lam)), float(max(collar_both_signs_3d_sqrt2lam))
    s2l_min_unl, s2l_max_unl = float(min(unlocalized_3d_sqrt2lam)), float(max(unlocalized_3d_sqrt2lam))
    s2l_min_3d, s2l_max_3d = float(min(surviving_3d_cover_sqrt2lam)), float(max(surviving_3d_cover_sqrt2lam))
    s2l_min_all, s2l_max_all = float(min(all_perturbative_sqrt2lam)), float(max(all_perturbative_sqrt2lam))
    lam_min_raw = float(min(all_perturbative_lam_raw))

    part_1b = {
        "E2_DynamicConfinement_and_Universal2LoopGaugeBand_Gate_passed": bool(
            dynamic_2d_cover_excluded
            and len(all_I_gauge) == 1320
            and len(surviving_3d_cover_I_gauge) == 264
            and i_min_all > 0.002
            and i_max_all < 0.006
            and (i_max_all - i_min_all) < 0.002
        ),
        "dynamic_qcd_pole_exclusion_of_2d_cover_branch": {
            "dln_cover_abs": abs(dln_cover),
            "pole_dln_2d_Cas": pole_dln_2d_cas,
            "pole_dln_2d_tree_6pi": pole_dln_2d_tree,
            "a3_inv_1loop_at_cover_if_2d": a3_1l_2d_at_cover,
            "excluded_by_confining_landau_pole": dynamic_2d_cover_excluded,
        },
        "UR1_universal_2loop_gauge_relation": {
            "definition_I_gauge": "sin^2(theta_EW) - (23/134 + (109/201) * (alpha_3^{-1} / alpha_EM^{-1}))",
            "definition_L_gauge": "(23/6)*alpha_1^{-1} - (111/10)*alpha_2^{-1} + (109/15)*alpha_3^{-1}",
            "total_perturbative_histories_swept": len(all_I_gauge),
            "surviving_3d_cover_histories_swept": len(surviving_3d_cover_I_gauge),
            "I_gauge_envelope_all_1320_histories": [i_min_all, i_max_all],
            "I_gauge_envelope_3d_cover_264_histories": [i_min_3d, i_max_3d],
            "L_gauge_envelope_all_1320_histories": [l_min_all, l_max_all],
            "L_gauge_envelope_3d_cover_264_histories": [l_min_3d, l_max_3d],
            "strictly_positive_2loop_shift_across_every_history": i_min_all > 0.0,
            "kill_line_statement": "Falsified with 0 continuous knobs and 0 selection bits if I_gauge falls outside [i_min_all, i_max_all].",
        },
    }

    part_1c = {
        "E3_UniversalScalarQuarticAttractor_and_Haar6_Gate_passed": bool(
            haar6_max_diff < 1e-12
            and lam_min_raw > 0.04
            and s2l_min_all > 0.28
            and s2l_max_all < 1.15
            and s2l_min_3d > 0.28
            and s2l_max_3d < 0.92
            and pc_broken_dterm_shift > 0.01
            and pc_wrong_chirality_err > 1e-3
        ),
        "UR2_universal_dterm_scalar_quartic_relation": {
            "uv_boundary_law": "lambda_UV = (1/5) * g_UV^2 (6D gauge-scalar D-term)",
            "strict_vacuum_stability_all_1320_histories": lam_min_raw > 0.0,
            "min_lambda_IR_all_1320_histories": lam_min_raw,
            "sqrt_2lam_envelope_all_1320_histories": [s2l_min_all, s2l_max_all],
            "sqrt_2lam_envelope_3d_cover_all_264_histories": [s2l_min_3d, s2l_max_3d],
            "sqrt_2lam_envelope_3d_cover_pos_collar_88_histories": [s2l_min_pos, s2l_max_pos],
            "sqrt_2lam_envelope_3d_cover_both_collar_signs_176_histories": [s2l_min_col, s2l_max_col],
            "sqrt_2lam_envelope_3d_cover_unlocalized_88_histories": [s2l_min_unl, s2l_max_unl],
            "kill_line_statement": "Falsified with 0 continuous knobs and 0 selection bits if lambda_IR <= 0 or sqrt(2*lambda_IR) falls outside [s2l_min_all, s2l_max_all] (or outside [s2l_min_3d, s2l_max_3d] on surviving 3D-cover histories).",
        },
        "Gate_Haar_Stage1_Relations_U3_power_6": {
            "ten_trial_max_diff_mp24": haar6_max_diff,
            "haar_invariance_below_1e_12": haar6_max_diff < 1e-12,
            "PC_REL1_BrokenDTermQuartic_shift": pc_broken_dterm_shift,
            "PC_REL1_WrongChiralityRGE_err": pc_wrong_chirality_err,
        },
        "selection_bits_required": {
            "continuous_parameters": 0,
            "discrete_selection_bits_for_UR1_and_UR2_envelopes": 0,
        },
    }

    return part_1a, part_1b, part_1c


def main() -> None:
    ast_check = verify_ast_relations1()
    part_1a, part_1b, part_1c = run_stage1_relations()

    controls_passed = bool(
        ast_check["Gate_AST_Stage1_Relations_Passed"]
        and part_1a["su5_universal_1loop_eliminants"]["PC_REL1_WrongHyperchargeNorm_shift"] > 0.08
        and part_1a["su5_universal_1loop_eliminants"]["PC_REL1_ExtraHiggsDoublets_L_violation"] > 1.0
        and part_1a["four_pillar_rge_solver_gate"]["pillar2_bbo_noncommuting_2loop_matrix"]["PC_REL1_Commutator_bbo_2loop_rel_err"] > 5e-3
        and part_1c["Gate_Haar_Stage1_Relations_U3_power_6"]["PC_REL1_BrokenDTermQuartic_shift"] > 0.01
        and part_1c["Gate_Haar_Stage1_Relations_U3_power_6"]["PC_REL1_WrongChiralityRGE_err"] > 1e-3
    )

    stage_1_passed = bool(
        controls_passed
        and part_1a["E1_FourPillar_and_Exact1Loop_Eliminant_Gate_passed"]
        and part_1b["E2_DynamicConfinement_and_Universal2LoopGaugeBand_Gate_passed"]
        and part_1c["E3_UniversalScalarQuarticAttractor_and_Haar6_Gate_passed"]
    )

    out_payload: Dict[str, Any] = {
        "card": "X-RELATIONS-1",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_check,
        "part_1a_solver_and_exact_1loop_eliminants": part_1a,
        "part_1b_dynamic_confinement_and_UR1_gauge_band": part_1b,
        "part_1c_UR2_scalar_band_and_haar6": part_1c,
        "all_planted_controls_passed": controls_passed,
        "stage_1_gate_passed": stage_1_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_relations_1_out.json"
    out_json.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{sha}  verify_x_relations_1_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
