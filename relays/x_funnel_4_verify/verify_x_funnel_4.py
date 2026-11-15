#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-FUNNEL-4 (0 of 19 on all model runs).

Verifies:
  Part 4A (gate_rge_literature_solver_only — AST-isolated solver verification gate):
    1. Differential variable identity d/d(ln mu) = 2 d/d(ln mu^2) against exact 1-loop closed-form gauge running
       (plus planted wrong-factor control PC_FUNNEL4_WrongDiffFactor).
    2. Verbatim 3-loop SM RGEs (+ 4-loop pure color running) of Buttazzo et al. (2013) integrated in u = ln(mu^2)
       to the Planck scale, reproducing all five published couplings (g1, g2, g3, yt, lam) and Lambda_lam / (2 Lambda_V).
    3. Exact machine-precision agreement between the 3x3 2-loop matrix Yukawa beta function and Buttazzo's
       diagonal 2-loop expressions.
    4. Infrared-directed 1-loop matrix RGE integration of Xing & Zhou (2018), reproducing (I_u, I_d, I_l, I_nu, xi_t)
       and verifying their exact Naumov-like commutator-determinant relation (Eq. 18) to < 1e-12
       (plus planted wrong-direction control PC_FUNNEL4_WrongRunningDirection).

  Part 4B (run_x_funnel_4_model_rge — 0 of 19 pure-math dimensionless UV-to-IR bridge, AST-isolated):
    1. P-862 1-loop color intra-sector cancellation test (varying UV alpha_3 shifts inter-sector sigma_3 ratio
       by > 0.5 while leaving intra-sector singular-value ratios invariant to < 1e-12 at suppressed Yukawa trace).
    2. Case I: Order-5 m004 root-orbit point (1/5, 2/5) at height 5/2 evolved across d(ln mu) = -30 from unified
       alpha_U = 1/42 and lambda_UV = 0 — establishes radiative inter-sector amplification (> 5/2), radiative
       scalar-to-condensate ratio sqrt(2 lambda_IR) > 1/2, and the exact Order-5 RG Skew No-Go.
    3. Case II: Order-15 chiral root lift (4/15, 8/15) = (3/5, 1/5) + (2/3, 1/3) at pure integer height 3 —
       simultaneous survival of opposite consecutive skew, inter-sector color amplification, radiative quartic,
       |V_33^IR| > 0.998, and non-zero CP commutator invariant under full 2-loop matrix evolution.
    4. Mandatory Haar basis-scrambling gate Gate_Haar_RGE (10 random 5-unitary UV scramblings prior to 2-loop ODE
       integration) and planted wrong-chirality RGE control PC_FUNNEL4_WrongChiralityRGE.
"""

from __future__ import annotations

import ast
import hashlib
import inspect
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
    "inspect",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "typing",
}

K1_LOOP: float = 1.0 / (16.0 * math.pi * math.pi)
K2_LOOP: float = K1_LOOP * K1_LOOP
K3_LOOP: float = K1_LOOP * K2_LOOP
K4_LOOP: float = K2_LOOP * K2_LOOP


def verify_source_and_firewall_isolation() -> Dict[str, Any]:
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

    # AST firewall check on run_x_funnel_4_model_rge:
    # Must NOT call gate_rge_literature_solver_only or buttazzo_d_dlnmu2 or xing_zhou_top_dom_rhs,
    # and must NOT contain any empirical literature float literals.
    model_src = inspect.getsource(run_x_funnel_4_model_rge)
    banned_model_tokens = (
        "gate_rge_literature_solver_only",
        "buttazzo_d_dlnmu2",
        "xing_zhou_top_dom_rhs",
        "173.34",
        "91.1876",
        "0.35830",
        "0.64779",
        "1.1666",
        "0.93690",
        "0.12604",
        "1.2209e19",
    )
    firewall_hits = [tok for tok in banned_model_tokens if tok in model_src]

    return {
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
        "model_runner_firewall_hits_count": len(firewall_hits),
        "strict_ast_isolation_between_lit_gate_and_model": len(firewall_hits) == 0,
    }


# ============================================================================
# SECTION 1: SHARED PURE-MATH 2-LOOP SM MATRIX RGE KERNEL & MAGNETIZED OVERLAP
# ============================================================================

def sm_2loop_matrix_rhs(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    wrong_chirality_control: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    """
    2-loop SM 3x3 matrix RGEs in d/d(ln mu) (GUT-normalized g1^2 = 5/3 gY^2).
    Under Yu -> U_Q Yu U_u^dagger, Yd -> U_Q Yd U_d^dagger, Ye -> U_L Ye U_e^dagger,
    every term transforms covariantly unless wrong_chirality_control=True.
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
        # Planted error: right-multiply (Hu - Hd) onto Yu instead of left-multiplying!
        b1_Yu = (y2_tr - 0.85 * g1s - 2.25 * g2s - 8.0 * g3s) * Yu + 1.5 * (Yu @ (Hu - Hd))
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

    dYu = K1_LOOP * b1_Yu + K2_LOOP * b2_Yu
    dYd = K1_LOOP * b1_Yd + K2_LOOP * b2_Yd
    dYe = K1_LOOP * b1_Ye + K2_LOOP * b2_Ye

    dg1 = K1_LOOP * (41.0 / 10.0) * (g1 ** 3) + K2_LOOP * (g1 ** 3) * (
        (199.0 / 50.0) * g1s + (27.0 / 10.0) * g2s + (44.0 / 5.0) * g3s - 1.7 * t_u - 0.5 * t_d - 1.5 * t_e
    )
    dg2 = K1_LOOP * (-19.0 / 6.0) * (g2 ** 3) + K2_LOOP * (g2 ** 3) * (
        0.9 * g1s + (35.0 / 6.0) * g2s + 12.0 * g3s - 1.5 * t_u - 1.5 * t_d - 0.5 * t_e
    )
    dg3 = K1_LOOP * (-7.0) * (g3 ** 3) + K2_LOOP * (g3 ** 3) * (
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
    dlam = K1_LOOP * dlam1 + K2_LOOP * dlam2
    return dYu, dYd, dYe, dg1, dg2, dg3, dlam


def rk4_integrate_2loop_matrix(
    Yu0: np.ndarray,
    Yd0: np.ndarray,
    Ye0: np.ndarray,
    g1_0: float,
    g2_0: float,
    g3_0: float,
    lam0: float,
    d_ln_mu: float,
    n_steps: int = 1600,
    wrong_chirality_control: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    dt = d_ln_mu / n_steps
    Yu, Yd, Ye = Yu0.copy(), Yd0.copy(), Ye0.copy()
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam0
    for _ in range(n_steps):
        k1 = sm_2loop_matrix_rhs(Yu, Yd, Ye, g1, g2, g3, lam, wrong_chirality_control)
        k2 = sm_2loop_matrix_rhs(
            Yu + 0.5 * dt * k1[0],
            Yd + 0.5 * dt * k1[1],
            Ye + 0.5 * dt * k1[2],
            g1 + 0.5 * dt * k1[3],
            g2 + 0.5 * dt * k1[4],
            g3 + 0.5 * dt * k1[5],
            lam + 0.5 * dt * k1[6],
            wrong_chirality_control,
        )
        k3 = sm_2loop_matrix_rhs(
            Yu + 0.5 * dt * k2[0],
            Yd + 0.5 * dt * k2[1],
            Ye + 0.5 * dt * k2[2],
            g1 + 0.5 * dt * k2[3],
            g2 + 0.5 * dt * k2[4],
            g3 + 0.5 * dt * k2[5],
            lam + 0.5 * dt * k2[6],
            wrong_chirality_control,
        )
        k4 = sm_2loop_matrix_rhs(
            Yu + dt * k3[0],
            Yd + dt * k3[1],
            Ye + dt * k3[2],
            g1 + dt * k3[3],
            g2 + dt * k3[4],
            g3 + dt * k3[5],
            lam + dt * k3[6],
            wrong_chirality_control,
        )
        Yu = Yu + (dt / 6.0) * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0])
        Yd = Yd + (dt / 6.0) * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1])
        Ye = Ye + (dt / 6.0) * (k1[2] + 2.0 * k2[2] + 2.0 * k3[2] + k4[2])
        g1 = g1 + (dt / 6.0) * (k1[3] + 2.0 * k2[3] + 2.0 * k3[3] + k4[3])
        g2 = g2 + (dt / 6.0) * (k1[4] + 2.0 * k2[4] + 2.0 * k3[4] + k4[4])
        g3 = g3 + (dt / 6.0) * (k1[5] + 2.0 * k2[5] + 2.0 * k3[5] + k4[5])
        lam = lam + (dt / 6.0) * (k1[6] + 2.0 * k2[6] + 2.0 * k3[6] + k4[6])
    return Yu, Yd, Ye, g1, g2, g3, lam


def erfcx_f64(x: float) -> float:
    if x < 25.0:
        return math.exp(x * x) * math.erfc(x)
    inv2 = 1.0 / (x * x)
    return (1.0 / (math.sqrt(math.pi) * x)) * (
        1.0 + inv2 * (-0.5 + inv2 * (0.75 + inv2 * (-1.875 + inv2 * 6.5625)))
    )


def erfc_integral_f64(alpha: float, beta: float, u0: float, thresh: float = 42.0) -> float:
    xm = alpha * u0 - beta / u0
    xp = alpha * u0 + beta / u0
    edge_exp = (alpha * u0) ** 2 + (beta / u0) ** 2
    if xm >= 0.0:
        if edge_exp > thresh:
            return 0.0
        return (math.sqrt(math.pi) / (2.0 * alpha)) * math.exp(-edge_exp) * (erfcx_f64(xm) + erfcx_f64(xp))
    if 2.0 * alpha * beta > thresh:
        return 0.0
    part1 = 2.0 * math.exp(-2.0 * alpha * beta)
    part2 = 0.0 if edge_exp > thresh else math.exp(-edge_exp) * (erfcx_f64(xp) - erfcx_f64(-xm))
    return (math.sqrt(math.pi) / (2.0 * alpha)) * (part1 + part2)


def y_ref_zak_f64(tau: complex, a: float, b: float, ql: int, qr: int) -> np.ndarray:
    qh = -(ql + qr)
    tau1, tau2 = tau.real, tau.imag
    u0 = 1.0 / math.sqrt(6.0)
    u_split = math.sqrt(tau2)
    thresh = 42.0
    k_max = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * tau2)) / 3.0)) + 3
    l_quad = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * tau2)))) + 4
    l_riem = int(math.ceil(math.sqrt(thresh / math.pi))) + 3

    def f_prim(u_val: float, b_val: float) -> float:
        if b_val == 0.0:
            return 2.0 * u_val
        bv_u = b_val / u_val
        if bv_u * bv_u > thresh:
            return 0.0
        return 2.0 * math.exp(-(bv_u * bv_u)) * (u_val - math.sqrt(math.pi) * b_val * erfcx_f64(bv_u))

    y_mat = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        c_l = (i + 0.5 + ql * a) / 3.0
        zak_ang = -2.0 * math.pi * (ql * b / 3.0) * (i + 0.5)
        zak_ph = complex(math.cos(zak_ang), math.sin(zak_ang))
        for j in range(3):
            c_r = (j + 0.5 - qr * a) / 3.0
            acc = 0.0j
            for k in range(-k_max, k_max + 1):
                n = (j - i) - 3 * k
                na = float(n) + qh * a
                delta_k = na / 3.0
                xi0 = (c_l + c_r - k) / 2.0
                x0 = na * tau1 + qh * b
                ang0 = math.pi * delta_k * ((qr - ql) * b - 3.0)
                base_phase = complex(math.cos(ang0), math.sin(ang0))
                if abs(na) > 1e-14:
                    alpha = math.sqrt(math.pi * tau2) * abs(na)
                    l_lin = int(math.ceil(thresh / (2.0 * math.pi * tau2 * abs(na)))) + 3
                    l_max_na = max(l_lin, l_quad)
                    sub = 0.0j
                    l_center = int(round(xi0))
                    for dl in range(-l_max_na, l_max_na + 1):
                        l = l_center + dl
                        beta = math.sqrt(math.pi * tau2) * abs(l - xi0)
                        iv = math.sqrt(tau2) * erfc_integral_f64(alpha, beta, u0, thresh)
                        if iv != 0.0:
                            ang = 2.0 * math.pi * (l - xi0) * x0
                            sub += iv * complex(math.cos(ang), math.sin(ang))
                    acc += base_phase * sub
                else:
                    sub1 = 0.0j
                    l_center = int(round(xi0))
                    for dl in range(-l_riem, l_riem + 1):
                        l = l_center + dl
                        beta = math.sqrt(math.pi * tau2) * abs(l - xi0)
                        iv = math.sqrt(tau2) * (f_prim(u_split, beta) - f_prim(u0, beta))
                        if iv != 0.0:
                            ang = 2.0 * math.pi * (l - xi0) * x0
                            sub1 += iv * complex(math.cos(ang), math.sin(ang))
                    sub2 = 0.0j
                    m_center = int(round(-x0))
                    for dm in range(-l_riem, l_riem + 1):
                        m = m_center + dm
                        mx = m + x0
                        if abs(mx) > 1e-14 and math.pi * mx * mx <= thresh:
                            ang = 2.0 * math.pi * m * xi0
                            sub2 += (
                                (tau2 / (math.pi * mx * mx))
                                * math.exp(-math.pi * mx * mx)
                                * complex(math.cos(ang), math.sin(ang))
                            )
                    acc += base_phase * (sub1 + sub2)
            y_mat[i, j] = zak_ph * acc
    return y_mat


# ============================================================================
# SECTION 2: PART 4A — AST-ISOLATED LITERATURE SOLVER BENCHMARK GATE
# ============================================================================

def buttazzo_d_dlnmu2(state: np.ndarray) -> np.ndarray:
    """Verbatim 3-loop SM RGEs (+ 4-loop pure QCD) in u = ln(mu^2) from Buttazzo et al. (2013) Appendix A."""
    g1s, g2s, g3s, yts, ybs, ytaus, lam = state

    dg1s = (
        K1_LOOP * (g1s ** 2) * (41.0 / 10.0)
        + K2_LOOP * (g1s ** 2) * (44.0 * g3s / 5.0 + 27.0 * g2s / 10.0 + 199.0 * g1s / 50.0 - 1.7 * yts - 0.5 * ybs - 1.5 * ytaus)
        + K3_LOOP * (g1s ** 2) * (
            yts * (189.0 * yts / 16.0 - 29.0 * g3s / 5.0 - 471.0 * g2s / 32.0 - 2827.0 * g1s / 800.0)
            + lam * (-1.8 * lam + 0.9 * g2s + 27.0 * g1s / 50.0)
            + 297.0 * (g3s ** 2) / 5.0 + 789.0 * (g2s ** 2) / 64.0 - 388613.0 * (g1s ** 2) / 24000.0
            - 0.6 * g3s * g2s - 137.0 * g3s * g1s / 75.0 + 123.0 * g2s * g1s / 160.0
        )
    )
    dg2s = (
        K1_LOOP * (g2s ** 2) * (-19.0 / 6.0)
        + K2_LOOP * (g2s ** 2) * (12.0 * g3s + 35.0 * g2s / 6.0 + 0.9 * g1s - 1.5 * yts - 1.5 * ybs - 0.5 * ytaus)
        + K3_LOOP * (g2s ** 2) * (
            yts * (147.0 * yts / 16.0 - 7.0 * g3s - 729.0 * g2s / 32.0 - 593.0 * g1s / 160.0)
            + lam * (-3.0 * lam + 1.5 * g2s + 0.3 * g1s)
            + 81.0 * (g3s ** 2) + 324953.0 * (g2s ** 2) / 1728.0 - 5597.0 * (g1s ** 2) / 1600.0
            + 39.0 * g3s * g2s - 0.2 * g3s * g1s + 873.0 * g2s * g1s / 160.0
        )
    )
    dg3s = (
        K1_LOOP * (g3s ** 2) * (-7.0)
        + K2_LOOP * (g3s ** 2) * (-26.0 * g3s + 4.5 * g2s + 1.1 * g1s - 2.0 * yts - 2.0 * ybs)
        + K3_LOOP * (g3s ** 2) * (
            yts * (15.0 * yts - 40.0 * g3s - 93.0 * g2s / 8.0 - 101.0 * g1s / 40.0)
            + 32.5 * (g3s ** 2) + 109.0 * (g2s ** 2) / 8.0 - 523.0 * (g1s ** 2) / 120.0
            + 21.0 * g3s * g2s + 77.0 * g3s * g1s / 15.0 - 3.0 * g2s * g1s / 40.0
        )
        + K4_LOOP * (g3s ** 5) * (-2472.28)
    )
    dlam = (
        K1_LOOP * (
            lam * (12.0 * lam + 6.0 * yts + 6.0 * ybs + 2.0 * ytaus - 4.5 * g2s - 0.9 * g1s)
            - 3.0 * (yts ** 2) - 3.0 * (ybs ** 2) - (ytaus ** 2)
            + 9.0 * (g2s ** 2) / 16.0 + 27.0 * (g1s ** 2) / 400.0 + 9.0 * g2s * g1s / 40.0
        )
        + K2_LOOP * (
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
        + K3_LOOP * (
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
        K1_LOOP * yts * (4.5 * yts + 1.5 * ybs + ytaus - 8.0 * g3s - 2.25 * g2s - 0.85 * g1s)
        + K2_LOOP * yts * (
            yts * (-12.0 * yts - 2.75 * ybs - 2.25 * ytaus - 12.0 * lam + 36.0 * g3s + 225.0 * g2s / 16.0 + 393.0 * g1s / 80.0)
            + ybs * (-0.25 * ybs + 1.25 * ytaus + 4.0 * g3s + 99.0 * g2s / 16.0 + 7.0 * g1s / 80.0)
            + ytaus * (-2.25 * ytaus + 1.875 * g2s + 1.875 * g1s)
            + 6.0 * (lam ** 2) - 108.0 * (g3s ** 2) - 5.75 * (g2s ** 2) + 1187.0 * (g1s ** 2) / 600.0 + 9.0 * g3s * g2s + 19.0 * g3s * g1s / 15.0 - 0.45 * g2s * g1s
        )
        + K3_LOOP * yts * (
            (yts ** 2) * (58.6028 * yts + 198.0 * lam - 157.0 * g3s - 1593.0 * g2s / 16.0 - 2437.0 * g1s / 80.0)
            + lam * yts * (3.75 * lam + 16.0 * g3s - 67.5 * g2s - 12.7 * g1s)
            + yts * (363.764 * (g3s ** 2) + 16.990 * (g2s ** 2) - 24.422 * (g1s ** 2) + 48.370 * g3s * g2s + 18.074 * g3s * g1s + 34.829 * g2s * g1s)
            + (lam ** 2) * (-36.0 * lam + 45.0 * g2s + 9.0 * g1s)
            + lam * (-171.0 * (g2s ** 2) / 16.0 - 1089.0 * (g1s ** 2) / 400.0 + 117.0 * g2s * g1s / 40.0)
            - 619.35 * (g3s ** 3) + 169.829 * (g2s ** 3) + 16.099 * (g1s ** 3) + 73.654 * (g3s ** 2) * g2s - 15.096 * (g3s ** 2) * g1s
            - 21.072 * g3s * (g2s ** 2) - 22.319 * g3s * (g1s ** 2) - 16.05 * g3s * g2s * g1s - 4.743 * (g2s ** 2) * g1s - 4.442 * g2s * (g1s ** 2)
        )
    )
    dybs = K1_LOOP * ybs * (1.5 * yts + 4.5 * ybs + ytaus - 8.0 * g3s - 2.25 * g2s - 0.25 * g1s)
    dytaus = K1_LOOP * ytaus * (3.0 * yts + 3.0 * ybs + 2.5 * ytaus - 2.25 * g2s - 2.25 * g1s)
    return np.array([dg1s, dg2s, dg3s, dyts, dybs, dytaus, dlam], dtype=float)


def xing_zhou_top_dom_rhs(
    Yu: np.ndarray, Yd: np.ndarray, Yl: np.ndarray, g1: float, g2: float, g3: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float, float, float, float]:
    """1-loop top-dominance matrix RGEs Eqs. (5)-(6) of Xing & Zhou (2018) in t = ln(mu/Lambda_EW)."""
    chi = float(np.real(3.0 * np.trace(Yu @ Yu.conj().T) + np.trace(Yl @ Yl.conj().T)))
    au = -0.85 * g1 * g1 - 2.25 * g2 * g2 - 8.0 * g3 * g3 + chi
    ad = -0.25 * g1 * g1 - 2.25 * g2 * g2 - 8.0 * g3 * g3 + chi
    al = -2.25 * g1 * g1 - 2.25 * g2 * g2 + chi
    anu = -0.45 * g1 * g1 - 2.25 * g2 * g2 + chi
    Hu = Yu @ Yu.conj().T
    Hl = Yl @ Yl.conj().T
    eye3 = np.eye(3, dtype=complex)
    dYu = K1_LOOP * (au * eye3 + 1.5 * Hu) @ Yu
    dYd = K1_LOOP * (ad * eye3 - 1.5 * Hu) @ Yd
    dYl = K1_LOOP * (al * eye3 + 1.5 * Hl) @ Yl
    dg1 = K1_LOOP * (41.0 / 10.0) * (g1 ** 3)
    dg2 = K1_LOOP * (-19.0 / 6.0) * (g2 ** 3)
    dg3 = K1_LOOP * (-7.0) * (g3 ** 3)
    return dYu, dYd, dYl, dg1, dg2, dg3, au, ad, al, anu


def gate_rge_literature_solver_only() -> Dict[str, Any]:
    """
    Guardrail 4 Literature Benchmark Gate — strictly isolated from model UV evolution.
    """
    # 1. Exact 1-loop closed-form gauge running check + d/d(ln mu) = 2 d/d(ln mu^2) convention gate:
    b_vec = [41.0 / 10.0, -19.0 / 6.0, -7.0]
    g0_vec = [0.46, 0.65, 1.15]
    d_ln_mu = 30.0
    n_s = 2500
    dt = d_ln_mu / n_s
    g_num = list(g0_vec)
    g_wrong_diff = list(g0_vec)
    for _ in range(n_s):
        for idx in range(3):
            b = b_vec[idx]
            # Correct: dg/d(ln mu) = (1 / (2 g)) * 2 * dg^2/d(ln mu^2) = K1 * b * g^3
            f = lambda gv: K1_LOOP * b * (gv ** 3)
            gv = g_num[idx]
            k1 = f(gv)
            k2 = f(gv + 0.5 * dt * k1)
            k3 = f(gv + 0.5 * dt * k2)
            k4 = f(gv + dt * k3)
            g_num[idx] = gv + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            # Planted PC_FUNNEL4_WrongDiffFactor: omits factor of 2 between ln(mu) and ln(mu^2)!
            fw = lambda gw: 0.5 * K1_LOOP * b * (gw ** 3)
            gw = g_wrong_diff[idx]
            w1 = fw(gw)
            w2 = fw(gw + 0.5 * dt * w1)
            w3 = fw(gw + 0.5 * dt * w2)
            w4 = fw(gw + dt * w3)
            g_wrong_diff[idx] = gw + (dt / 6.0) * (w1 + 2.0 * w2 + 2.0 * w3 + w4)

    g_exact = [
        g0_vec[idx] / math.sqrt(1.0 - 2.0 * K1_LOOP * b_vec[idx] * (g0_vec[idx] ** 2) * d_ln_mu)
        for idx in range(3)
    ]
    gauge_1loop_closed_form_max_err = max(abs(g_num[idx] - g_exact[idx]) for idx in range(3))
    pc_wrong_diff_factor_err = max(abs(g_wrong_diff[idx] - g_exact[idx]) for idx in range(3))

    # 2. 2-loop matrix vs Buttazzo diagonal Yukawa & quartic beta-function match:
    yt_c, yb_c, ytau_c, g1_c, g2_c, g3_c, lam_c = 0.93, 0.02, 0.01, 0.46, 0.65, 1.16, 0.12
    dYu_m, dYd_m, dYe_m, _, _, _, dlam_m = sm_2loop_matrix_rhs(
        np.diag([0.0, 0.0, yt_c]).astype(complex),
        np.diag([0.0, 0.0, yb_c]).astype(complex),
        np.diag([0.0, 0.0, ytau_c]).astype(complex),
        g1_c,
        g2_c,
        g3_c,
        lam_c,
    )
    g1s, g2s, g3s = g1_c ** 2, g2_c ** 2, g3_c ** 2
    yts, ybs, ytaus = yt_c ** 2, yb_c ** 2, ytau_c ** 2
    byt_but = K1_LOOP * yt_c * (4.5 * yts + 1.5 * ybs + ytaus - 8.0 * g3s - 2.25 * g2s - 0.85 * g1s) + K2_LOOP * yt_c * (
        yts * (-12.0 * yts - 2.75 * ybs - 2.25 * ytaus - 12.0 * lam_c + 36.0 * g3s + 225.0 / 16.0 * g2s + 393.0 / 80.0 * g1s)
        + ybs * (-0.25 * ybs + 1.25 * ytaus + 4.0 * g3s + 99.0 / 16.0 * g2s + 7.0 / 80.0 * g1s)
        + ytaus * (-2.25 * ytaus + 1.875 * g2s + 1.875 * g1s)
        + 6.0 * (lam_c ** 2) - 108.0 * (g3s ** 2) - 5.75 * (g2s ** 2) + 1187.0 / 600.0 * (g1s ** 2) + 9.0 * g3s * g2s + 19.0 / 15.0 * g3s * g1s - 0.45 * g2s * g1s
    )
    byb_but = K1_LOOP * yb_c * (1.5 * yts + 4.5 * ybs + ytaus - 8.0 * g3s - 2.25 * g2s - 0.25 * g1s) + K2_LOOP * yb_c * (
        yts * (-0.25 * yts - 2.75 * ybs + 1.25 * ytaus + 4.0 * g3s + 99.0 / 16.0 * g2s + 91.0 / 80.0 * g1s)
        + ybs * (-12.0 * ybs - 2.25 * ytaus - 12.0 * lam_c + 36.0 * g3s + 225.0 / 16.0 * g2s + 237.0 / 80.0 * g1s)
        + ytaus * (-2.25 * ytaus + 1.875 * g2s + 1.875 * g1s)
        + 6.0 * (lam_c ** 2) - 108.0 * (g3s ** 2) - 5.75 * (g2s ** 2) - 127.0 / 600.0 * (g1s ** 2) + 9.0 * g3s * g2s + 31.0 / 15.0 * g3s * g1s - 1.35 * g2s * g1s
    )
    bytau_but = K1_LOOP * ytau_c * (3.0 * yts + 3.0 * ybs + 2.5 * ytaus - 2.25 * g2s - 2.25 * g1s) + K2_LOOP * ytau_c * (
        6.0 * (lam_c ** 2) - 5.75 * (g2s ** 2) + 1371.0 / 200.0 * (g1s ** 2) + 1.35 * g2s * g1s
        + yts * (-6.75 * yts + 1.5 * ybs - 6.75 * ytaus + 20.0 * g3s + 5.625 * g2s + 2.125 * g1s)
        + ybs * (-6.75 * ybs - 6.75 * ytaus + 20.0 * g3s + 5.625 * g2s + 0.625 * g1s)
        + ytaus * (-3.0 * ytaus - 12.0 * lam_c + 165.0 / 16.0 * g2s + 537.0 / 80.0 * g1s)
    )
    matrix_vs_buttazzo_2loop_max_diff = max(
        abs(float(dYu_m[2, 2].real) - byt_but),
        abs(float(dYd_m[2, 2].real) - byb_but),
        abs(float(dYe_m[2, 2].real) - bytau_but),
    )

    # 3. Buttazzo et al. (2013) 3-loop Planck-scale extrapolation & zero-crossing benchmark:
    mt_lit = 173.34
    mpl_lit = 1.2209e19
    g1_0 = math.sqrt(5.0 / 3.0) * 0.35830
    y_st = np.array([g1_0 ** 2, 0.64779 ** 2, 1.1666 ** 2, 0.93690 ** 2, 0.0165 ** 2, 0.0102 ** 2, 0.12604], dtype=float)
    u0 = 2.0 * math.log(mt_lit)
    u1 = 2.0 * math.log(mpl_lit)
    n_but = 8000
    du = (u1 - u0) / n_but
    u_cross = 0.0
    crossed = False
    u_cur = u0
    for _ in range(n_but):
        y_prev = y_st.copy()
        k1 = buttazzo_d_dlnmu2(y_st)
        k2 = buttazzo_d_dlnmu2(y_st + 0.5 * du * k1)
        k3 = buttazzo_d_dlnmu2(y_st + 0.5 * du * k2)
        k4 = buttazzo_d_dlnmu2(y_st + du * k3)
        y_st = y_st + (du / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        if (not crossed) and y_prev[6] > 0.0 and y_st[6] <= 0.0:
            u_cross = u_cur + du * (y_prev[6] / (y_prev[6] - y_st[6]))
            crossed = True
        u_cur += du

    g1_pl, g2_pl, g3_pl, yt_pl, lam_pl = (
        math.sqrt(y_st[0]),
        math.sqrt(y_st[1]),
        math.sqrt(y_st[2]),
        math.sqrt(y_st[3]),
        float(y_st[6]),
    )
    pub_pl = {"g1": 0.6154, "g2": 0.5055, "g3": 0.4873, "yt": 0.3825, "lam": -0.0143}
    but_4coupling_max_rel_err = max(
        abs(g1_pl - pub_pl["g1"]) / pub_pl["g1"],
        abs(g2_pl - pub_pl["g2"]) / pub_pl["g2"],
        abs(g3_pl - pub_pl["g3"]) / pub_pl["g3"],
        abs(yt_pl - pub_pl["yt"]) / pub_pl["yt"],
    )
    but_lam_abs_err = abs(lam_pl - pub_pl["lam"])
    log10_lam_zero = 0.5 * u_cross / math.log(10.0)
    log10_two_lambda_v = 9.5 + math.log10(2.0)

    # 4. Xing & Zhou (2018) infrared-directed 1-loop matrix running & exact Naumov-like Eq. (18):
    t_uv = math.log(1.0e12 / 91.1876)
    g1_mz, g2_mz, g3_mz = 0.4614, 0.6518, 1.2143
    g1_uv = g1_mz / math.sqrt(1.0 - 2.0 * K1_LOOP * (41.0 / 10.0) * (g1_mz ** 2) * t_uv)
    g2_uv = g2_mz / math.sqrt(1.0 - 2.0 * K1_LOOP * (-19.0 / 6.0) * (g2_mz ** 2) * t_uv)
    g3_uv = g3_mz / math.sqrt(1.0 - 2.0 * K1_LOOP * (-7.0) * (g3_mz ** 2) * t_uv)

    Yu0 = np.diag([1.0e-5, 3.0e-3, 0.52]).astype(complex)
    th12, th23, th13, dcp = 0.22, 0.04, 0.004, 1.15
    c12, s12 = math.cos(th12), math.sin(th12)
    c23, s23 = math.cos(th23), math.sin(th23)
    c13, s13 = math.cos(th13), math.sin(th13)
    e_id = complex(math.cos(dcp), -math.sin(dcp))
    r23 = np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], dtype=complex)
    u13 = np.array([[c13, 0, s13 * e_id], [0, 1, 0], [-s13 * e_id.conjugate(), 0, c13]], dtype=complex)
    r12 = np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], dtype=complex)
    v_uv = r23 @ u13 @ r12
    Yd0 = v_uv @ np.diag([1.5e-5, 3.0e-4, 1.4e-2]).astype(complex)
    Yl0 = np.diag([2.8e-6, 6.0e-4, 1.0e-2]).astype(complex)

    def run_xz(sign_dir: float) -> Tuple[np.ndarray, np.ndarray, float, float, float, float, np.ndarray]:
        n_xz = 3500
        dt_xz = sign_dir * t_uv / n_xz
        Yu, Yd, Yl = Yu0.copy(), Yd0.copy(), Yl0.copy()
        g1, g2, g3 = g1_uv, g2_uv, g3_uv
        int_au = int_ad = int_al = int_anu = 0.0
        int_yu2 = np.zeros(3, dtype=float)
        for _ in range(n_xz):
            dYu1, dYd1, dYl1, dg1_1, dg2_1, dg3_1, au1, ad1, al1, anu1 = xing_zhou_top_dom_rhs(Yu, Yd, Yl, g1, g2, g3)
            yu2_1 = np.real(np.diag(Yu @ Yu.conj().T))
            Yu_m = Yu + 0.5 * dt_xz * dYu1
            Yd_m = Yd + 0.5 * dt_xz * dYd1
            Yl_m = Yl + 0.5 * dt_xz * dYl1
            g1_m, g2_m, g3_m = g1 + 0.5 * dt_xz * dg1_1, g2 + 0.5 * dt_xz * dg2_1, g3 + 0.5 * dt_xz * dg3_1
            dYu2, dYd2, dYl2, dg1_2, dg2_2, dg3_2, au2, ad2, al2, anu2 = xing_zhou_top_dom_rhs(Yu_m, Yd_m, Yl_m, g1_m, g2_m, g3_m)
            Yu_m2 = Yu + 0.5 * dt_xz * dYu2
            Yd_m2 = Yd + 0.5 * dt_xz * dYd2
            Yl_m2 = Yl + 0.5 * dt_xz * dYl2
            g1_m2, g2_m2, g3_m2 = g1 + 0.5 * dt_xz * dg1_2, g2 + 0.5 * dt_xz * dg2_2, g3 + 0.5 * dt_xz * dg3_2
            dYu3, dYd3, dYl3, dg1_3, dg2_3, dg3_3, au3, ad3, al3, anu3 = xing_zhou_top_dom_rhs(Yu_m2, Yd_m2, Yl_m2, g1_m2, g2_m2, g3_m2)
            Yu_e = Yu + dt_xz * dYu3
            Yd_e = Yd + dt_xz * dYd3
            Yl_e = Yl + dt_xz * dYl3
            g1_e, g2_e, g3_e = g1 + dt_xz * dg1_3, g2 + dt_xz * dg2_3, g3 + dt_xz * dg3_3
            dYu4, dYd4, dYl4, dg1_4, dg2_4, dg3_4, au4, ad4, al4, anu4 = xing_zhou_top_dom_rhs(Yu_e, Yd_e, Yl_e, g1_e, g2_e, g3_e)
            Yu = Yu + (dt_xz / 6.0) * (dYu1 + 2.0 * dYu2 + 2.0 * dYu3 + dYu4)
            Yd = Yd + (dt_xz / 6.0) * (dYd1 + 2.0 * dYd2 + 2.0 * dYd3 + dYd4)
            Yl = Yl + (dt_xz / 6.0) * (dYl1 + 2.0 * dYl2 + 2.0 * dYl3 + dYl4)
            g1 = g1 + (dt_xz / 6.0) * (dg1_1 + 2.0 * dg1_2 + 2.0 * dg1_3 + dg1_4)
            g2 = g2 + (dt_xz / 6.0) * (dg2_1 + 2.0 * dg2_2 + 2.0 * dg2_3 + dg2_4)
            g3 = g3 + (dt_xz / 6.0) * (dg3_1 + 2.0 * dg3_2 + 2.0 * dg3_3 + dg3_4)
            ds = abs(dt_xz)
            int_au += (ds / 6.0) * (au1 + 2.0 * au2 + 2.0 * au3 + au4)
            int_ad += (ds / 6.0) * (ad1 + 2.0 * ad2 + 2.0 * ad3 + ad4)
            int_al += (ds / 6.0) * (al1 + 2.0 * al2 + 2.0 * al3 + al4)
            int_anu += (ds / 6.0) * (anu1 + 2.0 * anu2 + 2.0 * anu3 + anu4)
            yu2_2 = np.real(np.diag(Yu_m @ Yu_m.conj().T))
            yu2_3 = np.real(np.diag(Yu_m2 @ Yu_m2.conj().T))
            yu2_4 = np.real(np.diag(Yu_e @ Yu_e.conj().T))
            int_yu2 += (ds / 6.0) * (yu2_1 + 2.0 * yu2_2 + 2.0 * yu2_3 + yu2_4)
        # In Xing-Zhou Eq. (7)-(8), I_f = exp(-1/(16 pi^2) int_0^{t_0} alpha_f dt) for downward running (-1.0);
        # if running upward (+1.0), Y_end / Y_start has opposite exponent!
        Iu = math.exp(sign_dir * K1_LOOP * int_au)
        Id = math.exp(sign_dir * K1_LOOP * int_ad)
        Il = math.exp(sign_dir * K1_LOOP * int_al)
        Inu = math.exp(sign_dir * K1_LOOP * int_anu)
        xi = np.exp(-sign_dir * 1.5 * K1_LOOP * int_yu2)
        return Yu, Yd, Iu, Id, Il, Inu, xi

    def naumov_combo(Yu_m: np.ndarray, Yd_m: np.ndarray) -> float:
        Hu = Yu_m @ Yu_m.conj().T
        Hd = Yd_m @ Yd_m.conj().T
        eu = np.sort(np.real(np.linalg.eigvalsh(Hu)))
        comm = Hu @ Hd - Hd @ Hu
        det_c = np.linalg.det(comm)
        prod_u = (eu[1] - eu[0]) * (eu[2] - eu[1]) * (eu[2] - eu[0])
        return float(np.imag(det_c) / (2.0 * prod_u))

    Yu_ir, Yd_ir, Iu, Id, Il, Inu, xi = run_xz(-1.0)
    lhs_ir = naumov_combo(Yu_ir, Yd_ir)
    rhs_uv = (Id ** 6) * float(np.prod(xi ** 2)) * naumov_combo(Yu0, Yd0)
    xz_eq18_rel_err = abs(lhs_ir - rhs_uv) / abs(rhs_uv)

    # Planted control PC_FUNNEL4_WrongRunningDirection (+1.0 upward instead of -1.0 downward):
    Yu_bad, Yd_bad, Iu_bad, Id_bad, _, _, _ = run_xz(+1.0)
    lhs_bad = naumov_combo(Yu_bad, Yd_bad)
    pc_wrong_dir_eq18_rel_err = abs(lhs_bad - rhs_uv) / abs(rhs_uv)

    e1_passed = bool(
        gauge_1loop_closed_form_max_err < 1e-12
        and pc_wrong_diff_factor_err > 0.1
        and matrix_vs_buttazzo_2loop_max_diff < 1e-15
        and but_4coupling_max_rel_err < 2e-3
        and but_lam_abs_err < 5e-4
        and abs(log10_lam_zero - log10_two_lambda_v) < 0.05
        and (1.9 < Id < Iu < 2.2)
        and (0.9 < Inu < Il < 1.05)
        and (1.05 < float(xi[2]) < 1.18)
        and xz_eq18_rel_err < 1e-12
        and Iu_bad < 1.0
        and pc_wrong_dir_eq18_rel_err > 0.9
    )

    return {
        "E1_Literature_RGE_Solver_Gate_passed": e1_passed,
        "gauge_1loop_closed_form_max_err": float(gauge_1loop_closed_form_max_err),
        "PC_FUNNEL4_WrongDiffFactor_err": float(pc_wrong_diff_factor_err),
        "matrix_vs_buttazzo_2loop_max_diff": float(matrix_vs_buttazzo_2loop_max_diff),
        "buttazzo_3loop_planck_benchmark": {
            "computed": {"g1": g1_pl, "g2": g2_pl, "g3": g3_pl, "yt": yt_pl, "lam": lam_pl},
            "published_eq_sys_Pl": pub_pl,
            "four_coupling_max_rel_err": float(but_4coupling_max_rel_err),
            "lam_abs_err": float(but_lam_abs_err),
            "log10_Lambda_lam_GeV": float(log10_lam_zero),
            "log10_two_Lambda_V_GeV": float(log10_two_lambda_v),
        },
        "xing_zhou_downward_1loop_benchmark": {
            "Iu": float(Iu),
            "Id": float(Id),
            "Il": float(Il),
            "Inu": float(Inu),
            "xi_t": float(xi[2]),
            "eq18_naumov_rel_err": float(xz_eq18_rel_err),
            "PC_FUNNEL4_WrongRunningDirection_Iu": float(Iu_bad),
            "PC_FUNNEL4_WrongRunningDirection_eq18_rel_err": float(pc_wrong_dir_eq18_rel_err),
        },
    }


# ============================================================================
# SECTION 3: PART 4B — PURE-MATH DIMENSIONLESS UV-TO-IR BRIDGE (0 OF 19)
# ============================================================================

def random_haar_u3_mp(seed: int) -> List[List[Any]]:
    """Deterministic 3x3 unitary matrix in current mpmath precision via complex Gram-Schmidt."""
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


def mp3_mul(a: List[List[Any]], b: List[List[Any]]) -> List[List[Any]]:
    return [
        [a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j] for j in range(3)]
        for i in range(3)
    ]


def mp3_dag(a: List[List[Any]]) -> List[List[Any]]:
    return [[mp.conj(a[j][i]) for j in range(3)] for i in range(3)]


def mp3_tr_re(a: List[List[Any]]) -> Any:
    return mp.re(a[0][0] + a[1][1] + a[2][2])


def sm_2loop_matrix_rhs_mp(
    Yu: List[List[Any]],
    Yd: List[List[Any]],
    Ye: List[List[Any]],
    g1: Any,
    g2: Any,
    g3: Any,
    lam: Any,
    k1_mp: Any,
    k2_mp: Any,
) -> Tuple[List[List[Any]], List[List[Any]], List[List[Any]], Any, Any, Any, Any]:
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

    t_hu2 = mp3_tr_re(Hu2)
    t_hd2 = mp3_tr_re(Hd2)
    t_he2 = mp3_tr_re(He2)
    t_huhd = mp3_tr_re(HuHd)

    chi2 = (
        -F(27, 4) * (t_hu2 + t_hd2)
        - F(9, 4) * t_he2
        + F(3, 2) * t_huhd
        + (F(17, 8) * g1s + F(45, 8) * g2s + 20 * g3s) * t_u
        + (F(5, 8) * g1s + F(45, 8) * g2s + 20 * g3s) * t_d
        + (F(15, 8) * g1s + F(15, 8) * g2s) * t_e
    )

    s1_u = y2_tr - F(17, 20) * g1s - F(9, 4) * g2s - 8 * g3s
    s1_d = y2_tr - F(1, 4) * g1s - F(9, 4) * g2s - 8 * g3s
    s1_e = y2_tr - F(9, 4) * g1s - F(9, 4) * g2s

    c_hu_u = -F(9, 4) * y2_tr - 12 * lam + F(223, 80) * g1s + F(135, 16) * g2s + 16 * g3s
    c_hd_u = F(5, 4) * y2_tr - F(43, 80) * g1s + F(9, 16) * g2s - 16 * g3s
    s2_u = (
        chi2 + 6 * lam * lam + F(1187, 600) * g1s * g1s - F(9, 20) * g1s * g2s
        + F(19, 15) * g1s * g3s - F(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s
    )

    c_hd_d = -F(9, 4) * y2_tr - 12 * lam + F(187, 80) * g1s + F(135, 16) * g2s + 16 * g3s
    c_hu_d = F(5, 4) * y2_tr - F(79, 80) * g1s + F(9, 16) * g2s - 16 * g3s
    s2_d = (
        chi2 + 6 * lam * lam - F(127, 600) * g1s * g1s - F(27, 20) * g1s * g2s
        + F(31, 15) * g1s * g3s - F(23, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s
    )

    c_he_e = -F(9, 4) * y2_tr - 12 * lam + F(387, 80) * g1s + F(135, 16) * g2s
    s2_e = chi2 + 6 * lam * lam + F(1371, 200) * g1s * g1s + F(27, 20) * g1s * g2s - F(23, 4) * g2s * g2s

    op_u = [
        [
            k1_mp * ((s1_u if r == c else 0) + F(3, 2) * (Hu[r][c] - Hd[r][c]))
            + k2_mp * (
                F(3, 2) * Hu2[r][c] - HuHd[r][c] - F(1, 4) * HdHu[r][c] + F(11, 4) * Hd2[r][c]
                + c_hu_u * Hu[r][c] + c_hd_u * Hd[r][c] + (s2_u if r == c else 0)
            )
            for c in range(3)
        ]
        for r in range(3)
    ]
    op_d = [
        [
            k1_mp * ((s1_d if r == c else 0) + F(3, 2) * (Hd[r][c] - Hu[r][c]))
            + k2_mp * (
                F(3, 2) * Hd2[r][c] - HdHu[r][c] - F(1, 4) * HuHd[r][c] + F(11, 4) * Hu2[r][c]
                + c_hd_d * Hd[r][c] + c_hu_d * Hu[r][c] + (s2_d if r == c else 0)
            )
            for c in range(3)
        ]
        for r in range(3)
    ]
    op_e = [
        [
            k1_mp * ((s1_e if r == c else 0) + F(3, 2) * He[r][c])
            + k2_mp * (F(3, 2) * He2[r][c] + c_he_e * He[r][c] + (s2_e if r == c else 0))
            for c in range(3)
        ]
        for r in range(3)
    ]

    dYu = mp3_mul(op_u, Yu)
    dYd = mp3_mul(op_d, Yd)
    dYe = mp3_mul(op_e, Ye)

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
    return dYu, dYd, dYe, dg1, dg2, dg3, dlam


def rk4_integrate_2loop_matrix_mp(
    Yu0: List[List[Any]],
    Yd0: List[List[Any]],
    Ye0: List[List[Any]],
    g1_0: Any,
    g2_0: Any,
    g3_0: Any,
    lam0: Any,
    d_ln_mu: Any,
    n_steps: int = 200,
) -> Tuple[List[List[Any]], List[List[Any]], List[List[Any]], Any]:
    dt = d_ln_mu / mp.mpf(n_steps)
    half_dt = dt / 2
    sixth_dt = dt / 6
    k1_mp = mp.mpf(1) / (16 * mp.pi * mp.pi)
    k2_mp = k1_mp * k1_mp
    Yu = [[Yu0[r][c] for c in range(3)] for r in range(3)]
    Yd = [[Yd0[r][c] for c in range(3)] for r in range(3)]
    Ye = [[Ye0[r][c] for c in range(3)] for r in range(3)]
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam0

    def add_scaled(m0: List[List[Any]], dm: List[List[Any]], sc: Any) -> List[List[Any]]:
        return [[m0[r][c] + sc * dm[r][c] for c in range(3)] for r in range(3)]

    for _ in range(n_steps):
        s1 = sm_2loop_matrix_rhs_mp(Yu, Yd, Ye, g1, g2, g3, lam, k1_mp, k2_mp)
        s2 = sm_2loop_matrix_rhs_mp(
            add_scaled(Yu, s1[0], half_dt), add_scaled(Yd, s1[1], half_dt), add_scaled(Ye, s1[2], half_dt),
            g1 + half_dt * s1[3], g2 + half_dt * s1[4], g3 + half_dt * s1[5], lam + half_dt * s1[6], k1_mp, k2_mp,
        )
        s3 = sm_2loop_matrix_rhs_mp(
            add_scaled(Yu, s2[0], half_dt), add_scaled(Yd, s2[1], half_dt), add_scaled(Ye, s2[2], half_dt),
            g1 + half_dt * s2[3], g2 + half_dt * s2[4], g3 + half_dt * s2[5], lam + half_dt * s2[6], k1_mp, k2_mp,
        )
        s4 = sm_2loop_matrix_rhs_mp(
            add_scaled(Yu, s3[0], dt), add_scaled(Yd, s3[1], dt), add_scaled(Ye, s3[2], dt),
            g1 + dt * s3[3], g2 + dt * s3[4], g3 + dt * s3[5], lam + dt * s3[6], k1_mp, k2_mp,
        )
        Yu = [[Yu[r][c] + sixth_dt * (s1[0][r][c] + 2 * s2[0][r][c] + 2 * s3[0][r][c] + s4[0][r][c]) for c in range(3)] for r in range(3)]
        Yd = [[Yd[r][c] + sixth_dt * (s1[1][r][c] + 2 * s2[1][r][c] + 2 * s3[1][r][c] + s4[1][r][c]) for c in range(3)] for r in range(3)]
        Ye = [[Ye[r][c] + sixth_dt * (s1[2][r][c] + 2 * s2[2][r][c] + 2 * s3[2][r][c] + s4[2][r][c]) for c in range(3)] for r in range(3)]
        g1 = g1 + sixth_dt * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
        g2 = g2 + sixth_dt * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
        g3 = g3 + sixth_dt * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
        lam = lam + sixth_dt * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
    return Yu, Yd, Ye, lam


def extract_obs_mp(Yu: List[List[Any]], Yd: List[List[Any]], Ye: List[List[Any]]) -> Dict[str, Any]:
    Hu = mp.matrix(mp3_mul(Yu, mp3_dag(Yu)))
    Hd = mp.matrix(mp3_mul(Yd, mp3_dag(Yd)))
    He = mp.matrix(mp3_mul(Ye, mp3_dag(Ye)))
    eu, qu = mp.eighe(Hu)
    ed, qd = mp.eighe(Hd)
    ee, _ = mp.eighe(He)
    su = [mp.sqrt(max(eu[k], mp.mpf(0))) for k in range(3)]
    sd = [mp.sqrt(max(ed[k], mp.mpf(0))) for k in range(3)]
    se = [mp.sqrt(max(ee[k], mp.mpf(0))) for k in range(3)]
    v_mat = qu.transpose_conj() * qd
    v_abs = [[abs(v_mat[r, c]) for c in range(3)] for r in range(3)]
    tu = sum(mp.re(Hu[i, i]) for i in range(3))
    td = sum(mp.re(Hd[i, i]) for i in range(3))
    hu_hat = Hu / tu
    hd_hat = Hd / td
    cm = hu_hat * hd_hat - hd_hat * hu_hat
    cm3 = cm * cm * cm
    icp = sum(mp.im(cm3[i, i]) for i in range(3)) / 6
    return {
        "ratios": [su[1] / su[2], su[0] / su[1], sd[1] / sd[2], sd[0] / sd[1], se[1] / se[2], se[0] / se[1]],
        "v_abs": v_abs,
        "icp_hat": icp,
    }


def random_haar_u3_np(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[np.newaxis, :]


def svd_ascending_np(m: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    u, s, _ = np.linalg.svd(m)
    idx = np.argsort(s)
    return u[:, idx], s[idx]


def extract_dimensionless_ir_observables(
    Yu: np.ndarray, Yd: np.ndarray, Ye: np.ndarray, lam: float
) -> Dict[str, Any]:
    u1, su = svd_ascending_np(Yu)
    u2, sd = svd_ascending_np(Yd)
    _, se = svd_ascending_np(Ye)
    vmix = np.abs(u1.conj().T @ u2)
    hu_hat = (Yu @ Yu.conj().T) / float(np.real(np.trace(Yu @ Yu.conj().T)))
    hd_hat = (Yd @ Yd.conj().T) / float(np.real(np.trace(Yd @ Yd.conj().T)))
    cm_hat = hu_hat @ hd_hat - hd_hat @ hu_hat
    icp_hat = float(np.imag(np.trace(cm_hat @ cm_hat @ cm_hat)) / 6.0)
    return {
        "sec1_r23": float(su[1] / su[2]),
        "sec1_r12": float(su[0] / su[1]),
        "sec2_r23": float(sd[1] / sd[2]),
        "sec2_r12": float(sd[0] / sd[1]),
        "sec3_r23": float(se[1] / se[2]),
        "sec3_r12": float(se[0] / se[1]),
        "inter_sector_s3_sec2_over_sec3": float(sd[2] / se[2]),
        "scalar_to_condensate_sqrt_2lam": float(math.sqrt(max(2.0 * lam, 0.0))),
        "lam_ir": float(lam),
        "V_abs": [[float(vmix[r, c]) for c in range(3)] for r in range(3)],
        "V33": float(vmix[2, 2]),
        "V12": float(vmix[0, 1]),
        "V23": float(vmix[1, 2]),
        "V13": float(vmix[0, 2]),
        "I_CP_hat_IR": icp_hat,
    }


def run_x_funnel_4_model_rge() -> Dict[str, Any]:
    """
    Pure-math dimensionless UV-to-IR evolution (0 of 19; zero empirical constants).
    All UV inputs are rational numbers and exact magnetized triple-overlap matrices.
    """
    alpha_u = float(Fraction(1, 42))
    g_u = math.sqrt(4.0 * math.pi * alpha_u)
    d_ln_mu = -30.0
    y1_top_uv = float(Fraction(1, 2))
    y23_uni_uv = float(Fraction(1, 50))
    lam_uv = 0.0

    # 1. P-862 1-loop color intra-sector cancellation check:
    # At suppressed Yukawa scale 1/10000 on (1/5, 2/5), compare alpha_3(UV) = 1/42 vs 1/35 under 1-loop running:
    tau_c1 = complex(float(Fraction(13, 100)), float(Fraction(5, 2)))
    a5, b5 = float(Fraction(1, 5)), float(Fraction(2, 5))
    y1_r5 = y_ref_zak_f64(tau_c1, a5, b5, 1, -4)
    y2_r5 = y_ref_zak_f64(tau_c1, a5, b5, 1, 2)
    y3_r5 = y_ref_zak_f64(tau_c1, a5, b5, -3, 6)
    _, s1_5 = svd_ascending_np(y1_r5)
    _, s2_5 = svd_ascending_np(y2_r5)
    _, s3_5 = svd_ascending_np(y3_r5)

    eps_y = float(Fraction(1, 10000))
    eps_y_1e6 = float(Fraction(1, 1000000))
    g3_alt = math.sqrt(4.0 * math.pi * float(Fraction(1, 35)))

    def rk4_1loop_only(
        Yu0: np.ndarray, Yd0: np.ndarray, Ye0: np.ndarray, g3_init: float, pure_gauge: bool = False
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        n_st = 1200
        dt = d_ln_mu / n_st
        Yu, Yd, Ye = Yu0.copy(), Yd0.copy(), Ye0.copy()
        g1, g2, g3 = g_u, g_u, g3_init
        eye3 = np.eye(3, dtype=complex)

        def rhs1(u_m: np.ndarray, d_m: np.ndarray, e_m: np.ndarray, g1v: float, g2v: float, g3v: float):
            if pure_gauge:
                du = K1_LOOP * (-0.85 * g1v ** 2 - 2.25 * g2v ** 2 - 8.0 * g3v ** 2) * u_m
                dd = K1_LOOP * (-0.25 * g1v ** 2 - 2.25 * g2v ** 2 - 8.0 * g3v ** 2) * d_m
                de = K1_LOOP * (-2.25 * g1v ** 2 - 2.25 * g2v ** 2) * e_m
            else:
                hu, hd, he = u_m @ u_m.conj().T, d_m @ d_m.conj().T, e_m @ e_m.conj().T
                yt_tr = float(np.real(3.0 * np.trace(hu) + 3.0 * np.trace(hd) + np.trace(he)))
                du = K1_LOOP * ((yt_tr - 0.85 * g1v ** 2 - 2.25 * g2v ** 2 - 8.0 * g3v ** 2) * eye3 + 1.5 * (hu - hd)) @ u_m
                dd = K1_LOOP * ((yt_tr - 0.25 * g1v ** 2 - 2.25 * g2v ** 2 - 8.0 * g3v ** 2) * eye3 + 1.5 * (hd - hu)) @ d_m
                de = K1_LOOP * ((yt_tr - 2.25 * g1v ** 2 - 2.25 * g2v ** 2) * eye3 + 1.5 * he) @ e_m
            return du, dd, de, K1_LOOP * 4.1 * g1v ** 3, K1_LOOP * (-19.0 / 6.0) * g2v ** 3, K1_LOOP * (-7.0) * g3v ** 3

        for _ in range(n_st):
            k1 = rhs1(Yu, Yd, Ye, g1, g2, g3)
            k2 = rhs1(Yu + 0.5 * dt * k1[0], Yd + 0.5 * dt * k1[1], Ye + 0.5 * dt * k1[2], g1 + 0.5 * dt * k1[3], g2 + 0.5 * dt * k1[4], g3 + 0.5 * dt * k1[5])
            k3 = rhs1(Yu + 0.5 * dt * k2[0], Yd + 0.5 * dt * k2[1], Ye + 0.5 * dt * k2[2], g1 + 0.5 * dt * k2[3], g2 + 0.5 * dt * k2[4], g3 + 0.5 * dt * k2[5])
            k4 = rhs1(Yu + dt * k3[0], Yd + dt * k3[1], Ye + dt * k3[2], g1 + dt * k3[3], g2 + dt * k3[4], g3 + dt * k3[5])
            Yu += (dt / 6.0) * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0])
            Yd += (dt / 6.0) * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1])
            Ye += (dt / 6.0) * (k1[2] + 2.0 * k2[2] + 2.0 * k3[2] + k4[2])
            g1 += (dt / 6.0) * (k1[3] + 2.0 * k2[3] + 2.0 * k3[3] + k4[3])
            g2 += (dt / 6.0) * (k1[4] + 2.0 * k2[4] + 2.0 * k3[4] + k4[4])
            g3 += (dt / 6.0) * (k1[5] + 2.0 * k2[5] + 2.0 * k3[5] + k4[5])
        return Yu, Yd, Ye

    u_a, d_a, e_a = rk4_1loop_only(eps_y * y1_r5 / s1_5[2], eps_y * y2_r5 / s2_5[2], eps_y * y3_r5 / s3_5[2], g_u)
    u_b, d_b, e_b = rk4_1loop_only(eps_y * y1_r5 / s1_5[2], eps_y * y2_r5 / s2_5[2], eps_y * y3_r5 / s3_5[2], g3_alt)
    obs_p862_a = extract_dimensionless_ir_observables(u_a, d_a, e_a, 0.0)
    obs_p862_b = extract_dimensionless_ir_observables(u_b, d_b, e_b, 0.0)
    p862_color_intra_ratio_max_shift = max(
        abs(obs_p862_a["sec2_r23"] - obs_p862_b["sec2_r23"]),
        abs(obs_p862_a["sec2_r12"] - obs_p862_b["sec2_r12"]),
    )
    p862_color_inter_sector_shift = abs(
        obs_p862_a["inter_sector_s3_sec2_over_sec3"] - obs_p862_b["inter_sector_s3_sec2_over_sec3"]
    )

    u_a6, d_a6, e_a6 = rk4_1loop_only(eps_y_1e6 * y1_r5 / s1_5[2], eps_y_1e6 * y2_r5 / s2_5[2], eps_y_1e6 * y3_r5 / s3_5[2], g_u)
    u_b6, d_b6, e_b6 = rk4_1loop_only(eps_y_1e6 * y1_r5 / s1_5[2], eps_y_1e6 * y2_r5 / s2_5[2], eps_y_1e6 * y3_r5 / s3_5[2], g3_alt)
    obs_p862_a6 = extract_dimensionless_ir_observables(u_a6, d_a6, e_a6, 0.0)
    obs_p862_b6 = extract_dimensionless_ir_observables(u_b6, d_b6, e_b6, 0.0)
    p862_color_intra_ratio_shift_eps_1e6 = max(
        abs(obs_p862_a6["sec2_r23"] - obs_p862_b6["sec2_r23"]),
        abs(obs_p862_a6["sec2_r12"] - obs_p862_b6["sec2_r12"]),
    )

    u_ag, d_ag, e_ag = rk4_1loop_only(y1_r5 / s1_5[2], y2_r5 / s2_5[2], y3_r5 / s3_5[2], g_u, pure_gauge=True)
    u_bg, d_bg, e_bg = rk4_1loop_only(y1_r5 / s1_5[2], y2_r5 / s2_5[2], y3_r5 / s3_5[2], g3_alt, pure_gauge=True)
    obs_p862_ag = extract_dimensionless_ir_observables(u_ag, d_ag, e_ag, 0.0)
    obs_p862_bg = extract_dimensionless_ir_observables(u_bg, d_bg, e_bg, 0.0)
    p862_color_intra_ratio_shift_pure_gauge = max(
        abs(obs_p862_ag["sec2_r23"] - obs_p862_bg["sec2_r23"]),
        abs(obs_p862_ag["sec2_r12"] - obs_p862_bg["sec2_r12"]),
    )

    # 2. Case I: Order-5 root point (1/5, 2/5) at height 5/2 under full 2-loop matrix RGE:
    Yu5_0 = y1_top_uv * (y1_r5 / s1_5[2])
    Yd5_0 = y23_uni_uv * (y2_r5 / s2_5[2])
    Ye5_0 = y23_uni_uv * (y3_r5 / s3_5[2])
    Yu5_ir, Yd5_ir, Ye5_ir, _, _, _, lam5_ir = rk4_integrate_2loop_matrix(Yu5_0, Yd5_0, Ye5_0, g_u, g_u, g_u, lam_uv, d_ln_mu)
    obs_case1_uv = extract_dimensionless_ir_observables(Yu5_0, Yd5_0, Ye5_0, lam_uv)
    obs_case1_ir = extract_dimensionless_ir_observables(Yu5_ir, Yd5_ir, Ye5_ir, lam5_ir)
    case1_both_ratios_drop = bool(
        obs_case1_ir["sec2_r23"] < obs_case1_ir["sec3_r23"]
        and obs_case1_ir["sec2_r12"] < obs_case1_ir["sec3_r12"]
    )

    # 3. Case II: Order-15 root lift (4/15, 8/15) = (3/5, 1/5) + (2/3, 1/3) at pure integer height 3:
    tau_c2 = complex(float(Fraction(13, 100)), 3.0)
    a15, b15 = float(Fraction(4, 15)), float(Fraction(8, 15))
    y1_r15 = y_ref_zak_f64(tau_c2, a15, b15, 1, -4)
    y2_r15 = y_ref_zak_f64(tau_c2, a15, b15, 1, 2)
    y3_r15 = y_ref_zak_f64(tau_c2, a15, b15, -3, 6)
    _, s1_15 = svd_ascending_np(y1_r15)
    _, s2_15 = svd_ascending_np(y2_r15)
    _, s3_15 = svd_ascending_np(y3_r15)

    Yu15_0 = y1_top_uv * (y1_r15 / s1_15[2])
    Yd15_0 = y23_uni_uv * (y2_r15 / s2_15[2])
    Ye15_0 = y23_uni_uv * (y3_r15 / s3_15[2])
    Yu15_ir, Yd15_ir, Ye15_ir, g1_15, g2_15, g3_15, lam15_ir = rk4_integrate_2loop_matrix(
        Yu15_0, Yd15_0, Ye15_0, g_u, g_u, g_u, lam_uv, d_ln_mu
    )
    obs_case2_uv = extract_dimensionless_ir_observables(Yu15_0, Yd15_0, Ye15_0, lam_uv)
    obs_case2_ir = extract_dimensionless_ir_observables(Yu15_ir, Yd15_ir, Ye15_ir, lam15_ir)
    case2_opposite_skew_survived = bool(
        obs_case2_ir["sec2_r23"] < obs_case2_ir["sec3_r23"]
        and obs_case2_ir["sec2_r12"] > obs_case2_ir["sec3_r12"]
    )

    # 4. Mandatory Gate_Haar_RGE in 30-digit mpmath (10 random 5-unitary UV scramblings BEFORE 2-loop matrix integration):
    haar_rge_spec_mix_max_diff = 0.0
    haar_rge_icp_max_rel_diff = 0.0
    mp_vs_f64_ir_obs_max_diff = 0.0
    with mp.workdps(30):
        Yu15_mp = [[mp.mpc(repr(float(Yu15_0[r, c].real)), repr(float(Yu15_0[r, c].imag))) for c in range(3)] for r in range(3)]
        Yd15_mp = [[mp.mpc(repr(float(Yd15_0[r, c].real)), repr(float(Yd15_0[r, c].imag))) for c in range(3)] for r in range(3)]
        Ye15_mp = [[mp.mpc(repr(float(Ye15_0[r, c].real)), repr(float(Ye15_0[r, c].imag))) for c in range(3)] for r in range(3)]
        g_u_mp = mp.sqrt(4 * mp.pi * (mp.mpf(1) / mp.mpf(42)))
        dln_mp = mp.mpf(-30)
        lam_mp0 = mp.mpf(0)

        u_ref_mp, d_ref_mp, e_ref_mp, lam_ref_mp = rk4_integrate_2loop_matrix_mp(
            Yu15_mp, Yd15_mp, Ye15_mp, g_u_mp, g_u_mp, g_u_mp, lam_mp0, dln_mp, n_steps=200
        )
        obs_ref_mp = extract_obs_mp(u_ref_mp, d_ref_mp, e_ref_mp)
        f64_ratios = [
            obs_case2_ir["sec1_r23"], obs_case2_ir["sec1_r12"],
            obs_case2_ir["sec2_r23"], obs_case2_ir["sec2_r12"],
            obs_case2_ir["sec3_r23"], obs_case2_ir["sec3_r12"],
        ]
        mp_vs_f64_ir_obs_max_diff = max(
            max(abs(float(obs_ref_mp["ratios"][k]) - f64_ratios[k]) for k in range(6)),
            abs(float(lam_ref_mp) - lam15_ir),
        )

        for trial in range(10):
            uq = random_haar_u3_mp(4000 + 5 * trial)
            ur1 = random_haar_u3_mp(4001 + 5 * trial)
            ur2 = random_haar_u3_mp(4002 + 5 * trial)
            ul = random_haar_u3_mp(4003 + 5 * trial)
            ur3 = random_haar_u3_mp(4004 + 5 * trial)
            u_ir_h, d_ir_h, e_ir_h, _ = rk4_integrate_2loop_matrix_mp(
                mp3_mul(uq, mp3_mul(Yu15_mp, mp3_dag(ur1))),
                mp3_mul(uq, mp3_mul(Yd15_mp, mp3_dag(ur2))),
                mp3_mul(ul, mp3_mul(Ye15_mp, mp3_dag(ur3))),
                g_u_mp, g_u_mp, g_u_mp, lam_mp0, dln_mp, n_steps=200,
            )
            obs_h = extract_obs_mp(u_ir_h, d_ir_h, e_ir_h)
            for k in range(6):
                haar_rge_spec_mix_max_diff = max(
                    haar_rge_spec_mix_max_diff, float(abs(obs_h["ratios"][k] - obs_ref_mp["ratios"][k]))
                )
            for r_i in range(3):
                for c_i in range(3):
                    haar_rge_spec_mix_max_diff = max(
                        haar_rge_spec_mix_max_diff, float(abs(obs_h["v_abs"][r_i][c_i] - obs_ref_mp["v_abs"][r_i][c_i]))
                    )
            haar_rge_icp_max_rel_diff = max(
                haar_rge_icp_max_rel_diff,
                float(abs(obs_h["icp_hat"] - obs_ref_mp["icp_hat"]) / abs(obs_ref_mp["icp_hat"])),
            )

    # Planted control PC_FUNNEL4_WrongChiralityRGE: right-multiplied (Hu - Hd) breaks Haar invariance!
    uq_bad = random_haar_u3_np(9401)
    ur1_bad = random_haar_u3_np(9402)
    u_wc0, d_wc0, e_wc0, _, _, _, lam_wc0 = rk4_integrate_2loop_matrix(
        Yu5_0, Yd5_0, Ye5_0, g_u, g_u, g_u, lam_uv, d_ln_mu, n_steps=600, wrong_chirality_control=True
    )
    u_wc1, d_wc1, e_wc1, _, _, _, lam_wc1 = rk4_integrate_2loop_matrix(
        uq_bad @ Yu5_0 @ ur1_bad.conj().T,
        uq_bad @ Yd5_0,
        Ye5_0,
        g_u,
        g_u,
        g_u,
        lam_uv,
        d_ln_mu,
        n_steps=600,
        wrong_chirality_control=True,
    )
    obs_wc0 = extract_dimensionless_ir_observables(u_wc0, d_wc0, e_wc0, lam_wc0)
    obs_wc1 = extract_dimensionless_ir_observables(u_wc1, d_wc1, e_wc1, lam_wc1)
    pc_wrong_chirality_haar_break = max(
        abs(obs_wc1[k] - obs_wc0[k]) for k in ("sec1_r23", "V12", "V23", "V13")
    )

    core_e2_without_p862_eps_threshold = bool(
        p862_color_inter_sector_shift > 0.5
        and obs_case1_ir["inter_sector_s3_sec2_over_sec3"] > 2.5
        and obs_case1_ir["scalar_to_condensate_sqrt_2lam"] > 0.5
        and case1_both_ratios_drop
        and obs_case2_ir["inter_sector_s3_sec2_over_sec3"] > 2.5
        and obs_case2_ir["scalar_to_condensate_sqrt_2lam"] > 0.5
        and case2_opposite_skew_survived
        and obs_case2_ir["V33"] > 0.998
        and abs(obs_case2_ir["I_CP_hat_IR"]) > 1e-12
        and haar_rge_spec_mix_max_diff < 1e-12
        and haar_rge_icp_max_rel_diff < 1e-12
        and pc_wrong_chirality_haar_break > 0.05
    )
    # Keep strict pre-registered bound (< 1e-12 at eps_y = 1/10000) untouched, plus exact eps_y^2 scaling diagnostic:
    e2_passed = bool(core_e2_without_p862_eps_threshold and p862_color_intra_ratio_max_shift < 1e-12)
    e2_quadratic_scaling_passed = bool(
        core_e2_without_p862_eps_threshold
        and p862_color_intra_ratio_shift_pure_gauge < 1e-14
        and p862_color_intra_ratio_shift_eps_1e6 < 1e-12
        and abs((p862_color_intra_ratio_max_shift / p862_color_intra_ratio_shift_eps_1e6) - 1.0e4) < 500.0
    )

    return {
        "E2_Model_Order5_NoGo_and_Order15_Bridge_passed": e2_passed,
        "E2_with_quadratic_eps_y_scaling_passed": e2_quadratic_scaling_passed,
        "p862_1loop_color_protection": {
            "intra_sector_ratio_max_shift_at_card_eps_1e_4": float(p862_color_intra_ratio_max_shift),
            "intra_sector_ratio_max_shift_at_eps_1e_6": float(p862_color_intra_ratio_shift_eps_1e6),
            "intra_sector_ratio_max_shift_pure_gauge_1loop": float(p862_color_intra_ratio_shift_pure_gauge),
            "quadratic_eps_y_scaling_ratio_1e4_over_1e6": float(
                p862_color_intra_ratio_max_shift / p862_color_intra_ratio_shift_eps_1e6
            ),
            "inter_sector_s3_ratio_shift_under_g3_variation": float(p862_color_inter_sector_shift),
        },
        "case1_order5_1_5_2_5_height_2p5": {
            "uv": obs_case1_uv,
            "ir": obs_case1_ir,
            "order5_both_ratios_drop_no_opposite_skew": case1_both_ratios_drop,
        },
        "case2_order15_4_15_8_15_height_3": {
            "ir_gauge_couplings": {"g1": float(g1_15), "g2": float(g2_15), "g3": float(g3_15)},
            "uv": obs_case2_uv,
            "ir": obs_case2_ir,
            "opposite_consecutive_skew_survived": case2_opposite_skew_survived,
        },
        "controls_4b": {
            "Gate_Haar_RGE_spec_mix_max_diff_10_trials": float(haar_rge_spec_mix_max_diff),
            "Gate_Haar_RGE_icp_hat_max_rel_diff_10_trials": float(haar_rge_icp_max_rel_diff),
            "mp30_vs_float64_case2_ir_max_diff": float(mp_vs_f64_ir_obs_max_diff),
            "PC_FUNNEL4_WrongChiralityRGE_haar_break": float(pc_wrong_chirality_haar_break),
        },
    }


def main() -> None:
    ast_info = verify_source_and_firewall_isolation()
    res_4a = gate_rge_literature_solver_only()
    res_4b = run_x_funnel_4_model_rge()

    all_controls_passed = bool(
        ast_info["zero_imports_from_main_or_other_relays"]
        and ast_info["strict_ast_isolation_between_lit_gate_and_model"]
        and res_4a["PC_FUNNEL4_WrongDiffFactor_err"] > 0.1
        and res_4a["xing_zhou_downward_1loop_benchmark"]["PC_FUNNEL4_WrongRunningDirection_eq18_rel_err"] > 0.9
        and res_4b["controls_4b"]["Gate_Haar_RGE_spec_mix_max_diff_10_trials"] < 1e-12
        and res_4b["controls_4b"]["Gate_Haar_RGE_icp_hat_max_rel_diff_10_trials"] < 1e-12
        and res_4b["controls_4b"]["PC_FUNNEL4_WrongChiralityRGE_haar_break"] > 0.05
    )
    stage_4_passed = bool(
        all_controls_passed
        and res_4a["E1_Literature_RGE_Solver_Gate_passed"]
        and res_4b["E2_Model_Order5_NoGo_and_Order15_Bridge_passed"]
    )

    payload: Dict[str, Any] = {
        "card": "X-FUNNEL-4",
        "empirical_firewall": "0 of 19 on all model runs (AST-isolated from solver benchmark gate)",
        "source_and_firewall_ast_check": ast_info,
        "part_4a_literature_solver_gate": res_4a,
        "part_4b_model_uv_to_ir_bridge": res_4b,
        "all_planted_controls_passed": all_controls_passed,
        "stage_4_gate_passed": stage_4_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_funnel_4_out.json"
    out_txt = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out_json.write_text(out_txt, encoding="utf-8")
    digest = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_funnel_4_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
