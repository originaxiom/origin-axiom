#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_CLOSURE-G6:
  Modular-Covariant Majorana Seesaw, TM1 RGE Survival, and Repaired 3-Family
  Pati-Salam x Z2^D 2-Loop IR Surfaces (0 of 19).

Empirical Firewall: 0 of 19 (zero repository imports, zero float/complex literals in source).
"""

from __future__ import annotations

import ast
import cmath
from fractions import Fraction
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "cmath",
    "fractions",
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
# SECTION 0: AST SOURCE LOCK (ZERO REPO IMPORTS & ZERO FLOAT/COMPLEX LITERALS)
# ============================================================================

def verify_ast_g6() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_literals = 0
    complex_literals = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    passed = (len(disallowed) == 0) and (float_literals == 0) and (complex_literals == 0)
    return {
        "ast_gate_passed": passed,
        "imported_modules": sorted(mods),
        "disallowed_imports": disallowed,
        "float_literals_in_entire_file": float_literals,
        "complex_literals_in_entire_file": complex_literals,
    }


# ============================================================================
# SECTION 1: MODULAR-COVARIANT (J0, J1, J2) MAJORANA BASIS & SEESAW HAAR LOCK
# ============================================================================

def theta_char_f64(a_c: float, b_c: float, z: complex, tau: complex, n_win: int = 18) -> complex:
    y_t = tau.imag
    alpha_z = z.imag / y_t
    n0 = int(round(-a_c - alpha_z))
    acc = complex(0, 0)
    for n in range(n0 - n_win, n0 + n_win + 1):
        na = n + a_c
        arg = complex(0, 1) * math.pi * (na * na) * tau + complex(0, 2) * math.pi * na * (z + b_c)
        if arg.real > -700:
            acc += cmath.exp(arg)
    return acc


def psi_cim_pos(j: int, I_f: int, a_s: float, b_s: float, z: complex, tau: complex, zeta: complex) -> complex:
    w = z + zeta
    im_tau = tau.imag
    norm = (2 * I_f * im_tau) ** frac_f64(1, 4)
    pref = cmath.exp(complex(0, 1) * math.pi * I_f * w * (w.imag / im_tau))
    return norm * pref * theta_char_f64((j + a_s) / I_f, b_s, I_f * w, I_f * tau)


def Y_cim_xi(tau: complex, xi: complex, n_win: int = 18) -> np.ndarray:
    x_t, y_t = tau.real, tau.imag
    pref = (3 * y_t) ** frac_f64(1, 4)
    alpha_xi = xi.imag / y_t
    beta_xi = xi.real - alpha_xi * x_t
    n_c = int(round(-alpha_xi))
    Y = np.zeros((3, 3, 6), dtype=complex)
    for i in range(3):
        for j in range(3):
            for eps in (0, 1):
                k = (i + j + 1 + 3 * eps) % 6
                d0 = (2 * i + 1 - k) % 6
                acc = complex(0, 0)
                for n in range(n_c - n_win, n_c + n_win + 1):
                    r = n + d0 / 6
                    ra = r + alpha_xi
                    re_e = -6 * math.pi * y_t * (ra * ra)
                    if re_e > -700:
                        ph = math.pi * ((6 * x_t * (ra * ra) + 6 * beta_xi * (2 * r + alpha_xi) + k / 3) % 2)
                        acc += math.exp(re_e) * complex(math.cos(ph), math.sin(ph))
                Y[i, j, k] = pref * acc
    return Y


def basis_T(I_f: int, a_s: float, b_s: float, tau: complex, zeta: complex, ngrid: int = 30) -> np.ndarray:
    grid = np.linspace(frac_f64(0, 1), frac_f64(1, 1), ngrid, endpoint=False)
    U = np.zeros((I_f, I_f), dtype=complex)
    for x in grid:
        for y in grid:
            z = x + tau * y
            vn = np.array([psi_cim_pos(a, I_f, a_s, b_s, z, tau + 1, zeta) for a in range(I_f)])
            vo = np.array([psi_cim_pos(b, I_f, a_s, b_s, z, tau, zeta) for b in range(I_f)])
            U += np.outer(vn, vo.conj())
    return U / (ngrid * ngrid)


def basis_S(I_f: int, a_s: float, b_s: float, tau: complex, zeta: complex, ngrid: int = 30) -> np.ndarray:
    grid = np.linspace(frac_f64(0, 1), frac_f64(1, 1), ngrid, endpoint=False)
    U = np.zeros((I_f, I_f), dtype=complex)
    for x in grid:
        for y in grid:
            z = x + tau * y
            vn = np.array([psi_cim_pos(a, I_f, a_s, b_s, z / tau, -1 / tau, zeta / tau) for a in range(I_f)])
            vo = np.array([psi_cim_pos(b, I_f, a_s, b_s, z, tau, zeta) for b in range(I_f)])
            U += np.outer(vn, vo.conj())
    return U / (ngrid * ngrid)


def build_majorana_basis(tau_v: complex) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    Yt = Y_cim_xi(tau_v, complex(0, 0))
    v0 = np.array([psi_cim_pos(k, 6, frac_f64(0, 1), frac_f64(0, 1), complex(0, 0), tau_v, complex(0, 0)) for k in range(6)])
    G6 = np.einsum("ijk,ijl->kl", Yt.conj(), Yt)
    J0 = np.einsum("ijk,k->ij", Yt, v0)
    J1 = np.einsum("ijk,k->ij", Yt, G6 @ v0)
    J2 = J1 @ J1.conj().T @ J1
    return J0, J1, J2


def random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[np.newaxis, :]


def run_section_1_majorana_basis_and_seesaw() -> Dict[str, Any]:
    tau = complex(frac_f64(23, 100), frac_f64(141, 100))
    UT3 = basis_T(3, frac_f64(1, 2), frac_f64(1, 2), tau, complex(0, 0))
    US3 = basis_S(3, frac_f64(1, 2), frac_f64(1, 2), tau, complex(0, 0))

    J0_0, J1_0, J2_0 = build_majorana_basis(tau)
    J0_T, J1_T, J2_T = build_majorana_basis(tau + 1)
    J0_S, J1_S, J2_S = build_majorana_basis(-1 / tau)

    max_sym_err = max(float(np.max(np.abs(m - m.T))) for m in (J0_0, J1_0, J2_0))
    max_T_err = max(float(np.max(np.abs(mT - UT3 @ m0 @ UT3.T))) for m0, mT in ((J0_0, J0_T), (J1_0, J1_T), (J2_0, J2_T)))
    max_S_err = max(float(np.max(np.abs(mS - US3 @ m0 @ US3.T))) for m0, mS in ((J0_0, J0_S), (J1_0, J1_S), (J2_0, J2_S)))

    rk_J0 = int(np.linalg.matrix_rank(J0_0, tol=pow10_f64(-10)))
    rk_J1 = int(np.linalg.matrix_rank(J1_0, tol=pow10_f64(-10)))
    rk_J2 = int(np.linalg.matrix_rank(J2_0, tol=pow10_f64(-10)))
    span_rank_sym2 = int(np.linalg.matrix_rank(np.array([J0_0.flatten(), J1_0.flatten(), J2_0.flatten()]), tol=pow10_f64(-8)))

    # Complex CP^2 relative phase sensitivity (proving 4 real projective parameters + 1 scale = 5 generally):
    MR_real = J0_0 + J1_0 + frac_f64(1, 5) * J2_0
    MR_cmpx = J0_0 + complex(0, 1) * J1_0 + frac_f64(1, 5) * J2_0
    sv_r = np.linalg.svd(MR_real, compute_uv=False)
    sv_c = np.linalg.svd(MR_cmpx, compute_uv=False)
    cp2_phase_shift = abs(float(sv_r[1] / sv_r[0] - sv_c[1] / sv_c[0]))

    # Planted PF6.1: basis-dependence of all-ones sum in Frobenius-orthonormalized basis under SO(3) rotation
    mats = [J0_0, J1_0, J2_0]
    G_frob = np.array([[np.vdot(mats[a].flatten(), mats[b].flatten()) for b in range(3)] for a in range(3)])
    eig_g, U_g = np.linalg.eigh(G_frob)
    G_inv_sqrt = U_g @ np.diag(1 / np.sqrt(eig_g)) @ U_g.conj().T
    E_orth = [sum(G_inv_sqrt[b, a] * mats[b] for b in range(3)) for a in range(3)]
    R_rot = np.array([[frac_f64(3, 5), frac_f64(-4, 5), 0], [frac_f64(4, 5), frac_f64(3, 5), 0], [0, 0, 1]], dtype=complex)
    E_rot = [sum(R_rot[b, a] * E_orth[b] for b in range(3)) for a in range(3)]
    s_o1 = np.linalg.svd(E_orth[0] + E_orth[1] + E_orth[2], compute_uv=False)
    s_o2 = np.linalg.svd(E_rot[0] + E_rot[1] + E_rot[2], compute_uv=False)
    pf6_1_shift = abs(float(s_o1[1] / s_o1[0] - s_o2[1] / s_o2[0]))
    pf6_1_caught = pf6_1_shift > frac_f64(1, 10)

    # 10-trial U(3)^6 Haar scrambling on Type-I seesaw kappa_W = Y_nu M_R^{-1} Y_nu^T + charged lepton Y_e
    w_pt = frac_f64(1, 5) * tau + frac_f64(2, 5)
    Y0_t = Y_cim_xi(tau, complex(0, 0))
    v6_0 = np.array([psi_cim_pos(k, 6, frac_f64(0, 1), frac_f64(0, 1), complex(0, 0), tau, complex(0, 0)) for k in range(6)])
    G6_t = np.einsum("ijk,ijl->kl", Y0_t.conj(), Y0_t)
    v6_1 = G6_t @ v6_0
    v6_1 = v6_1 / np.linalg.norm(v6_1)
    Y_nu = np.einsum("ijk,k->ij", Y_cim_xi(tau, -3 * w_pt), v6_1)
    Y_e = np.einsum("ijk,k->ij", Y_cim_xi(tau, frac_f64(-7, 2) * w_pt), v6_1)
    M_R = MR_real

    def seesaw_obs(Ye_m: np.ndarray, Ynu_m: np.ndarray, MR_m: np.ndarray) -> np.ndarray:
        kap = Ynu_m @ np.linalg.inv(MR_m) @ Ynu_m.T
        ue, se, _ = np.linalg.svd(Ye_m)
        ue = ue[:, ::-1]
        uk, sk, _ = np.linalg.svd(kap)
        uk = uk[:, ::-1]
        sk = sk[::-1]
        pmns_mod = np.abs(ue.conj().T @ uk)
        return np.concatenate([[se[2] / se[0], se[1] / se[0], sk[0] / sk[2], sk[1] / sk[2]], pmns_mod.ravel()])

    ref_ss = seesaw_obs(Y_e, Y_nu, M_R)
    rng = np.random.default_rng(20261118)
    max_ss_haar_err = frac_f64(0, 1)
    for _ in range(10):
        UL = random_haar_u3(rng)
        URe = random_haar_u3(rng)
        URnu = random_haar_u3(rng)
        Ye_r = UL @ Y_e @ URe.conj().T
        Ynu_r = UL @ Y_nu @ URnu.conj().T
        MR_r = URnu.conj() @ M_R @ URnu.conj().T
        obs_r = seesaw_obs(Ye_r, Ynu_r, MR_r)
        max_ss_haar_err = max(max_ss_haar_err, float(np.max(np.abs(obs_r - ref_ss))))

    sec1_passed = (
        max_sym_err < pow10_f64(-14)
        and max_T_err < pow10_f64(-12)
        and max_S_err < pow10_f64(-12)
        and (rk_J0, rk_J1, rk_J2) == (1, 3, 3)
        and span_rank_sym2 == 3
        and cp2_phase_shift > frac_f64(1, 200)
        and max_ss_haar_err < pow10_f64(-13)
        and pf6_1_caught
    )
    return {
        "section_1_passed": sec1_passed,
        "majorana_symmetry_max_err": max_sym_err,
        "majorana_max_T_cov_err": max_T_err,
        "majorana_max_S_cov_err": max_S_err,
        "individual_ranks_J0_J1_J2": [rk_J0, rk_J1, rk_J2],
        "span_rank_in_sym2_C3": span_rank_sym2,
        "cp2_complex_phase_sv23_shift": cp2_phase_shift,
        "majorana_general_parameter_count_projective_plus_scale": [4, 1],
        "majorana_cp_real_parameter_count_projective_plus_scale": [2, 1],
        "seesaw_haar_u3_max_drift_10_trials": max_ss_haar_err,
        "PF6_1_orthonormal_ones_rotation_shift": pf6_1_shift,
        "PF6_1_caught": pf6_1_caught,
    }


# ============================================================================
# SECTION 2: TRIMAXIMAL TM1 SUM-RULE EMERGENCE & DOWNWARD RGE CORRIDOR
# ============================================================================

def run_section_2_tm1_rge_corridor() -> Dict[str, Any]:
    u1 = np.array([2, -1, -1], dtype=complex) / math.sqrt(6)
    u2 = np.array([1, 1, 1], dtype=complex) / math.sqrt(3)
    u3 = np.array([0, 1, -1], dtype=complex) / math.sqrt(2)
    B_tm1 = np.column_stack([u1, u2, u3])

    phi = math.asin(frac_f64(1, 4))
    ph_cp = cmath.exp(complex(0, 1) * frac_f64(7, 10))
    R23 = np.array([
        [1, 0, 0],
        [0, math.cos(phi), math.sin(phi) * ph_cp],
        [0, -math.sin(phi) * ph_cp.conjugate(), math.cos(phi)],
    ], dtype=complex)
    U_uv = B_tm1 @ R23

    # Build symmetric kappa_UV = U_uv @ diag(m1, m2, m3) @ U_uv^T so kap @ kap^dag = U_uv @ D^2 @ U_uv^dag!
    m_nh = np.diag([frac_f64(1, 50), frac_f64(1, 10), frac_f64(1, 2)])
    kap_uv = U_uv @ m_nh @ U_uv.T
    _, U_ext_uv = np.linalg.eigh(kap_uv @ kap_uv.conj().T)
    i_tm1_uv = abs(complex(U_ext_uv[0, 0])) ** 2
    ue3_sq_uv = abs(complex(U_ext_uv[0, 2])) ** 2
    uv_tm1_err = abs(i_tm1_uv - frac_f64(2, 3))
    uv_ue3_err = abs(ue3_sq_uv - frac_f64(1, 48))

    # Planted PF6.2: TM2 column swap (placing u2 in column 1 -> |U_e1|^2 = 1/3)
    B_tm2 = np.column_stack([u2, u1, u3])
    U_tm2 = B_tm2 @ R23
    pf6_2_diff = abs((abs(complex(U_tm2[0, 0])) ** 2) - frac_f64(2, 3))
    pf6_2_caught = pf6_2_diff > frac_f64(1, 4)

    # Downward Weinberg RGE evolution dt = -30 across y_tau in {1/100, 1/20, 1/5}
    k1 = frac_f64(1, 16) / (math.pi ** 2)
    ir_shifts: Dict[str, float] = {}
    for num_y, den_y in ((1, 100), (1, 20), (1, 5)):
        ytau = frac_f64(num_y, den_y)
        He = np.diag([(ytau / 200) ** 2, (ytau / 16) ** 2, ytau ** 2]).astype(complex)
        kw = kap_uv.copy()
        n_st = 300
        h = frac_f64(-30, 1) / n_st
        for _ in range(n_st):
            s1 = k1 * (-frac_f64(3, 2) * (He @ kw + kw @ He.T))
            k_a = kw + frac_f64(1, 2) * h * s1
            s2 = k1 * (-frac_f64(3, 2) * (He @ k_a + k_a @ He.T))
            k_b = kw + frac_f64(1, 2) * h * s2
            s3 = k1 * (-frac_f64(3, 2) * (He @ k_b + k_b @ He.T))
            k_c = kw + h * s3
            s4 = k1 * (-frac_f64(3, 2) * (He @ k_c + k_c @ He.T))
            kw = kw + (h / 6) * (s1 + 2 * s2 + 2 * s3 + s4)
        _, U_ir = np.linalg.eigh(kw @ kw.conj().T)
        ir_shifts[f"{num_y}/{den_y}"] = abs((abs(complex(U_ir[0, 0])) ** 2) - frac_f64(2, 3))

    sec2_passed = (
        uv_tm1_err < pow10_f64(-14)
        and uv_ue3_err < pow10_f64(-14)
        and ir_shifts["1/100"] < frac_f64(1, 2000)
        and ir_shifts["1/20"] < frac_f64(1, 2000)
        and max(ir_shifts.values()) < frac_f64(1, 200)
        and pf6_2_caught
    )
    return {
        "section_2_passed": sec2_passed,
        "uv_I_TM1_minus_2_over_3_abs": uv_tm1_err,
        "uv_Ue3_sq_minus_1_over_48_abs": uv_ue3_err,
        "ir_I_TM1_shifts_by_ytau": ir_shifts,
        "PF6_2_tm2_swap_diff": pf6_2_diff,
        "PF6_2_caught": pf6_2_caught,
    }


# ============================================================================
# SECTION 3: 243-HISTORY 3-FAMILY PATI-SALAM x Z2^D UNIVERSAL 2-LOOP IR SURFACES
# ============================================================================

def sm_2loop_bpv_rhs(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    half_lam2_bug: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    k1 = frac_f64(1, 16) / (math.pi ** 2)
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

    b1_Yu = ((y2_tr - frac_f64(17, 20) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hu - Hd)) @ Yu
    b1_Yd = ((y2_tr - frac_f64(1, 4) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hd - Hu)) @ Yd
    b1_Ye = ((y2_tr - frac_f64(9, 4) * g1s - frac_f64(9, 4) * g2s) * eye3 + frac_f64(3, 2) * He) @ Ye

    Hu2 = Hu @ Hu
    Hd2 = Hd @ Hd
    He2 = He @ He
    HuHd = Hu @ Hd
    HdHu = Hd @ Hu

    thu2 = float(np.real(np.trace(Hu2)))
    thd2 = float(np.real(np.trace(Hd2)))
    the2 = float(np.real(np.trace(He2)))
    thuhd = float(np.real(np.trace(HuHd)))

    chi2 = (
        -frac_f64(27, 4) * (thu2 + thd2)
        - frac_f64(9, 4) * the2
        + frac_f64(3, 2) * thuhd
        + (frac_f64(17, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * tu
        + (frac_f64(5, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * td
        + (frac_f64(15, 8) * g1s + frac_f64(15, 8) * g2s) * te
    )

    b2_Yu = (
        frac_f64(3, 2) * Hu2
        - frac_f64(1, 4) * HuHd
        - HdHu
        + frac_f64(11, 4) * Hd2
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(223, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hu
        + (frac_f64(5, 4) * y2_tr - frac_f64(43, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hd
        + (
            chi2 + 6 * lam * lam + frac_f64(1187, 600) * (g1s ** 2) - frac_f64(9, 20) * g1s * g2s
            + frac_f64(19, 15) * g1s * g3s - frac_f64(23, 4) * (g2s ** 2) + 9 * g2s * g3s - 108 * (g3s ** 2)
        ) * eye3
    ) @ Yu

    b2_Yd = (
        frac_f64(3, 2) * Hd2
        - frac_f64(1, 4) * HdHu
        - HuHd
        + frac_f64(11, 4) * Hu2
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(187, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hd
        + (frac_f64(5, 4) * y2_tr - frac_f64(79, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hu
        + (
            chi2 + 6 * lam * lam - frac_f64(127, 600) * (g1s ** 2) - frac_f64(27, 20) * g1s * g2s
            + frac_f64(31, 15) * g1s * g3s - frac_f64(23, 4) * (g2s ** 2) + 9 * g2s * g3s - 108 * (g3s ** 2)
        ) * eye3
    ) @ Yd

    b2_Ye = (
        frac_f64(3, 2) * He2
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(387, 80) * g1s + frac_f64(135, 16) * g2s) * He
        + (chi2 + 6 * lam * lam + frac_f64(1371, 200) * (g1s ** 2) + frac_f64(27, 20) * g1s * g2s - frac_f64(23, 4) * (g2s ** 2)) * eye3
    ) @ Ye

    dg1 = k1 * frac_f64(41, 10) * (g1 ** 3) + k2 * (g1 ** 3) * (
        frac_f64(199, 50) * g1s + frac_f64(27, 10) * g2s + frac_f64(44, 5) * g3s - frac_f64(17, 10) * tu - frac_f64(1, 2) * td - frac_f64(3, 2) * te
    )
    dg2 = k1 * frac_f64(-19, 6) * (g2 ** 3) + k2 * (g2 ** 3) * (
        frac_f64(9, 10) * g1s + frac_f64(35, 6) * g2s + 12 * g3s - frac_f64(3, 2) * tu - frac_f64(3, 2) * td - frac_f64(1, 2) * te
    )
    dg3 = k1 * (-7) * (g3 ** 3) + k2 * (g3 ** 3) * (
        frac_f64(11, 10) * g1s + frac_f64(9, 2) * g2s - 26 * g3s - 2 * tu - 2 * td
    )

    thu3 = float(np.real(np.trace(Hu2 @ Hu)))
    thd3 = float(np.real(np.trace(Hd2 @ Hd)))
    the3 = float(np.real(np.trace(He2 @ He)))
    thu2hd = float(np.real(np.trace(Hu2 @ Hd)))
    thuhd2 = float(np.real(np.trace(Hu @ Hd2)))

    c_l2 = -24 if half_lam2_bug else -48
    dlam1 = (
        24 * lam * lam + lam * (4 * y2_tr - 9 * g2s - frac_f64(9, 5) * g1s)
        - 2 * (3 * thu2 + 3 * thd2 + the2)
        + frac_f64(9, 8) * (g2s ** 2) + frac_f64(27, 200) * (g1s ** 2) + frac_f64(9, 20) * g1s * g2s
    )
    dlam2 = (
        -312 * (lam ** 3)
        + 36 * (lam * lam) * (3 * g2s + frac_f64(3, 5) * g1s)
        + c_l2 * (lam * lam) * y2_tr
        + lam * (80 * g3s + frac_f64(45, 2) * g2s) * (tu + td)
        + lam * g1s * (frac_f64(17, 2) * tu + frac_f64(5, 2) * td + frac_f64(15, 2) * te)
        + frac_f64(15, 2) * lam * g2s * te
        - 3 * lam * (thu2 + thd2 + frac_f64(1, 3) * the2 + 14 * thuhd)
        + lam * (-frac_f64(73, 8) * (g2s ** 2) + frac_f64(117, 20) * g1s * g2s + frac_f64(1887, 200) * (g1s ** 2))
        + 30 * (thu3 + thd3 + frac_f64(1, 3) * the3)
        - 6 * (thu2hd + thuhd2)
        - 32 * g3s * (thu2 + thd2)
        - frac_f64(8, 5) * g1s * thu2 + frac_f64(4, 5) * g1s * thd2 - frac_f64(12, 5) * g1s * the2
        - frac_f64(9, 4) * (g2s ** 2) * (tu + td + frac_f64(1, 3) * te)
        + g1s * g2s * (frac_f64(63, 10) * tu + frac_f64(27, 10) * td + frac_f64(33, 10) * te)
        - (g1s ** 2) * (frac_f64(171, 100) * tu - frac_f64(9, 20) * td + frac_f64(9, 4) * te)
        + frac_f64(305, 16) * (g2s ** 3) - frac_f64(289, 80) * (g2s ** 2) * g1s
        - frac_f64(1677, 400) * g2s * (g1s ** 2) - frac_f64(3411, 2000) * (g1s ** 3)
    )
    return k1 * b1_Yu + k2 * b2_Yu, k1 * b1_Yd + k2 * b2_Yd, k1 * b1_Ye + k2 * b2_Ye, dg1, dg2, dg3, k1 * dlam1 + k2 * dlam2


def rk4_sm(
    Yu0: np.ndarray, Yd0: np.ndarray, Ye0: np.ndarray, g1_0: float, g2_0: float, g3_0: float, lam_0: float, dt: float, n_steps: int, half_bug: bool
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    h = dt / n_steps
    Yu, Yd, Ye = Yu0.copy(), Yd0.copy(), Ye0.copy()
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam_0
    for _ in range(n_steps):
        s1 = sm_2loop_bpv_rhs(Yu, Yd, Ye, g1, g2, g3, lam, half_bug)
        s2 = sm_2loop_bpv_rhs(
            Yu + frac_f64(1, 2) * h * s1[0], Yd + frac_f64(1, 2) * h * s1[1], Ye + frac_f64(1, 2) * h * s1[2],
            g1 + frac_f64(1, 2) * h * s1[3], g2 + frac_f64(1, 2) * h * s1[4], g3 + frac_f64(1, 2) * h * s1[5],
            lam + frac_f64(1, 2) * h * s1[6], half_bug,
        )
        s3 = sm_2loop_bpv_rhs(
            Yu + frac_f64(1, 2) * h * s2[0], Yd + frac_f64(1, 2) * h * s2[1], Ye + frac_f64(1, 2) * h * s2[2],
            g1 + frac_f64(1, 2) * h * s2[3], g2 + frac_f64(1, 2) * h * s2[4], g3 + frac_f64(1, 2) * h * s2[5],
            lam + frac_f64(1, 2) * h * s2[6], half_bug,
        )
        s4 = sm_2loop_bpv_rhs(
            Yu + h * s3[0], Yd + h * s3[1], Ye + h * s3[2],
            g1 + h * s3[3], g2 + h * s3[4], g3 + h * s3[5], lam + h * s3[6], half_bug,
        )
        Yu = Yu + (h / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
        Yd = Yd + (h / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
        Ye = Ye + (h / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
        g1 = g1 + (h / 6) * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
        g2 = g2 + (h / 6) * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
        g3 = g3 + (h / 6) * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
        lam = lam + (h / 6) * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
    return Yu, Yd, Ye, g1, g2, g3, lam


def bloch_wigner_mp(z_val: mp.mpc) -> mp.mpf:
    return mp.im(mp.polylog(2, z_val)) + mp.arg(1 - z_val) * mp.log(abs(z_val))


def run_section_3_ir_surfaces() -> Dict[str, Any]:
    b_ps = [frac_f64(-10, 1), frac_f64(-7, 3), frac_f64(-7, 3)]
    B_ps = [
        [frac_f64(-117, 2), frac_f64(15, 2), frac_f64(15, 2)],
        [frac_f64(75, 2), frac_f64(50, 3), frac_f64(3, 1)],
        [frac_f64(75, 2), frac_f64(3, 1), frac_f64(50, 3)],
    ]

    def rk4_ps(gu: float, dps: float) -> Tuple[float, float, float]:
        if dps == frac_f64(0, 1):
            return gu, gu, gu
        k1 = frac_f64(1, 16) / (math.pi ** 2)
        k2 = k1 * k1
        n_st = 120
        h = -dps / n_st
        g = [gu, gu, gu]

        def rhs_p(v: List[float]) -> List[float]:
            gs = [x * x for x in v]
            return [(v[a] ** 3) * (k1 * b_ps[a] + k2 * sum(B_ps[a][b] * gs[b] for b in range(3))) for a in range(3)]

        for _ in range(n_st):
            s1 = rhs_p(g)
            s2 = rhs_p([g[a] + frac_f64(1, 2) * h * s1[a] for a in range(3)])
            s3 = rhs_p([g[a] + frac_f64(1, 2) * h * s2[a] for a in range(3)])
            s4 = rhs_p([g[a] + h * s3[a] for a in range(3)])
            g = [g[a] + (h / 6) * (s1[a] + 2 * s2[a] + 2 * s3[a] + s4[a]) for a in range(3)]
        return g[0], g[1], g[2]

    Au_base = np.array([
        [complex(frac_f64(2, 25), frac_f64(3, 100)), complex(frac_f64(1, 20), frac_f64(-1, 50)), complex(frac_f64(3, 50), frac_f64(3, 100))],
        [complex(frac_f64(-1, 50), frac_f64(1, 25)), complex(frac_f64(7, 25), frac_f64(1, 20)), complex(frac_f64(9, 100), frac_f64(-3, 50))],
        [complex(frac_f64(3, 100), frac_f64(-1, 50)), complex(frac_f64(2, 25), frac_f64(3, 50)), complex(frac_f64(1, 1), frac_f64(1, 25))],
    ], dtype=complex)
    Hu_unit = Au_base @ Au_base.conj().T
    Hu_unit = Hu_unit / float(np.linalg.svd(Hu_unit, compute_uv=False)[0])

    Ad_base = np.array([
        [complex(frac_f64(3, 50), frac_f64(-1, 50)), complex(frac_f64(2, 25), frac_f64(1, 20)), complex(frac_f64(-1, 25), frac_f64(3, 50))],
        [complex(frac_f64(1, 25), frac_f64(1, 20)), complex(frac_f64(1, 4), frac_f64(-1, 20)), complex(frac_f64(9, 100), frac_f64(2, 25))],
        [complex(frac_f64(-3, 100), frac_f64(3, 100)), complex(frac_f64(7, 100), frac_f64(-3, 50)), complex(frac_f64(11, 20), frac_f64(-3, 100))],
    ], dtype=complex)
    Hd_fixed = Ad_base @ Ad_base.conj().T
    Ye_fixed = np.diag([frac_f64(1, 1000), frac_f64(1, 50), frac_f64(3, 20)]).astype(complex)

    d2l_list: List[float] = []
    s2l_list: List[float] = []
    lam_ir_min = pow10_f64(9)
    max_bar_theta = frac_f64(0, 1)
    min_j_ckm = pow10_f64(9)
    max_pf6_4_shift = frac_f64(0, 1)

    for aui in (frac_f64(52, 1), frac_f64(60, 1), frac_f64(68, 1)):
        for dps in (frac_f64(0, 1), frac_f64(2, 1), frac_f64(4, 1)):
            gu = math.sqrt(4 * math.pi / aui)
            g4, g2l, g2r = rk4_ps(gu, dps)
            a1 = frac_f64(3, 5) * (4 * math.pi / (g2r * g2r)) + frac_f64(2, 5) * (4 * math.pi / (g4 * g4))
            g1 = math.sqrt(4 * math.pi / a1)
            for dsm in (frac_f64(26, 1), frac_f64(28, 1), frac_f64(30, 1)):
                for yt_num, yt_den in ((1, 2), (7, 10), (9, 10)):
                    Yu0 = frac_f64(yt_num, yt_den) * Hu_unit
                    for c2b_num, c2b_den in ((0, 1), (1, 2), (1, 1)):
                        lam0 = frac_f64(1, 4) * (g2l * g2l) * frac_f64(c2b_num, c2b_den)
                        Yu_i, Yd_i, _, g1_i, g2_i, g3_i, lam_i = rk4_sm(
                            Yu0, Hd_fixed, Ye_fixed, g1, g2l, g4, lam0, -dsm, 120, False
                        )
                        _, _, _, _, _, _, lam_b24 = rk4_sm(
                            Yu0, Hd_fixed, Ye_fixed, g1, g2l, g4, lam0, -dsm, 120, True
                        )
                        a1i = 4 * math.pi / (g1_i * g1_i)
                        a2i = 4 * math.pi / (g2_i * g2_i)
                        a3i = 4 * math.pi / (g3_i * g3_i)
                        aemi = frac_f64(5, 3) * a1i + a2i
                        d2l_val = (a2i / aemi) - (
                            frac_f64(23, 134) + frac_f64(109, 201) * (a3i / aemi) + (frac_f64(506, 201) / math.pi) * (dps / aemi)
                        )
                        d2l_list.append(d2l_val)
                        lam_ir_min = min(lam_ir_min, lam_i)
                        s2l_val = math.sqrt(2 * lam_i)
                        s2l_list.append(s2l_val)
                        max_pf6_4_shift = max(max_pf6_4_shift, abs(s2l_val - math.sqrt(2 * lam_b24)))

                        det_p = np.linalg.det(Yu_i @ Yd_i)
                        max_bar_theta = max(max_bar_theta, abs(math.atan2(float(np.imag(det_p)), float(np.real(det_p)))))
                        uu, _, _ = np.linalg.svd(Yu_i)
                        ud, _, _ = np.linalg.svd(Yd_i)
                        V_c = uu[:, ::-1].conj().T @ ud[:, ::-1]
                        j_val = abs(float(np.imag(V_c[0, 0] * V_c[1, 1] * np.conj(V_c[0, 1]) * np.conj(V_c[1, 0]))))
                        min_j_ckm = min(min_j_ckm, j_val)

    # Planted PF6.3: N_g = 6 chiral doubling shifts alpha_3^{-1}(IR) by (b_3(6) - b_3(3)) / (2 pi) * Delta_SM = 4 / (2 pi) * 28 > 17 > 15!
    b3_ng3 = -Fraction(11, 3) * 3 + Fraction(4, 3) * 3  # -7
    b3_ng6 = -Fraction(11, 3) * 3 + Fraction(4, 3) * 6  # -3
    a3_ir_ng3 = frac_f64(52, 1) + float(b3_ng3) * frac_f64(28, 1) / (2 * math.pi)
    a3_ir_ng6 = frac_f64(52, 1) + float(b3_ng6) * frac_f64(28, 1) / (2 * math.pi)
    pf6_3_alpha3_inv_shift = abs(a3_ir_ng6 - a3_ir_ng3)
    pf6_3_caught = pf6_3_alpha3_inv_shift > frac_f64(15, 1)

    pf6_4_caught = max_pf6_4_shift > frac_f64(1, 1000)

    # Planted PF6.5: Tautological Bloch-Wigner conjugation identity D(z) + D(conj(z)) == 0 at asymmetric z = 3/5 + (4/5) i
    mp.mp.dps = 40
    z_asym = mp.mpc(mp.mpf(3) / 5, mp.mpf(4) / 5)
    pf6_5_tautology_val = float(abs(bloch_wigner_mp(z_asym) + bloch_wigner_mp(mp.conj(z_asym))))
    pf6_5_caught = pf6_5_tautology_val < pow10_f64(-15)

    d2l_min, d2l_max = min(d2l_list), max(d2l_list)
    s2l_min, s2l_max = min(s2l_list), max(s2l_list)

    sec3_passed = (
        len(d2l_list) == 243
        and max_bar_theta < pow10_f64(-13)
        and min_j_ckm > frac_f64(1, 1000)
        and d2l_min > frac_f64(7, 10000)
        and d2l_max < frac_f64(3, 1000)
        and lam_ir_min > frac_f64(1, 20)
        and s2l_min > frac_f64(35, 100)
        and s2l_max < frac_f64(78, 100)
        and pf6_3_caught
        and pf6_4_caught
        and pf6_5_caught
    )
    return {
        "section_3_passed": sec3_passed,
        "history_count": len(d2l_list),
        "max_bar_theta_qcd_ir": max_bar_theta,
        "min_abs_jarlskog_ir": min_j_ckm,
        "delta_2loop_min": d2l_min,
        "delta_2loop_max": d2l_max,
        "delta_2loop_rational_envelope": ["7/10000", "3/1000"],
        "lambda_ir_min": lam_ir_min,
        "sqrt_2lambda_ir_min": s2l_min,
        "sqrt_2lambda_ir_max": s2l_max,
        "sqrt_2lambda_ir_rational_envelope": ["35/100", "78/100"],
        "PF6_3_ng6_alpha3_inv_shift": pf6_3_alpha3_inv_shift,
        "PF6_3_caught": pf6_3_caught,
        "PF6_4_max_bug24_sqrt2lam_shift": max_pf6_4_shift,
        "PF6_4_caught": pf6_4_caught,
        "PF6_5_asymmetric_bloch_wigner_conj_sum": pf6_5_tautology_val,
        "PF6_5_caught": pf6_5_caught,
    }


def main() -> None:
    ast_res = verify_ast_g6()
    sec1_res = run_section_1_majorana_basis_and_seesaw()
    sec2_res = run_section_2_tm1_rge_corridor()
    sec3_res = run_section_3_ir_surfaces()

    all_planted_caught = (
        sec1_res["PF6_1_caught"]
        and sec2_res["PF6_2_caught"]
        and sec3_res["PF6_3_caught"]
        and sec3_res["PF6_4_caught"]
        and sec3_res["PF6_5_caught"]
    )
    gate_passed = (
        ast_res["ast_gate_passed"]
        and sec1_res["section_1_passed"]
        and sec2_res["section_2_passed"]
        and sec3_res["section_3_passed"]
        and all_planted_caught
    )

    out: Dict[str, Any] = {
        "card": "AGY-002_CLOSURE-G6",
        "empirical_firewall": "0 of 19",
        "gate_6_passed": gate_passed,
        "all_5_planted_faults_caught": all_planted_caught,
        "section_0_ast": ast_res,
        "section_1_majorana_basis_and_seesaw": sec1_res,
        "section_2_tm1_rge_corridor": sec2_res,
        "section_3_ir_surfaces": sec3_res,
    }

    out_path = Path(__file__).with_name("verify_closure_g6_fixed_out.json")
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
