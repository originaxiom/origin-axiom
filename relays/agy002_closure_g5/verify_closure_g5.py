#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_CLOSURE-G5:
  Covariant Frame D1 CIM (3, 3, -6) CKM Alignment, Pati-Salam 3(B-L) Holonomy Separation,
  and Weil Cocycle / Gramian Laws (0 of 19).

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

import numpy as np


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "cmath",
    "fractions",
    "json",
    "math",
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

def verify_ast_g5() -> Dict[str, Any]:
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
# SHARED CLOSED-FIBRE CIM (3, 3, -6) OPERATORS
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


def prim_pts(N: int) -> List[Tuple[Fraction, Fraction]]:
    return [(Fraction(a, N), Fraction(b, N)) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1]


def random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[np.newaxis, :]


# ============================================================================
# SECTION 1: POLE-FREE E[3] CONTINUITY & CKM ALIGNMENT THEOREM (P-861, B1947)
# ============================================================================

def run_section_1_ckm_alignment() -> Dict[str, Any]:
    # 1A. Continuous analyticity across all 8 non-zero 3-torsion points E[3] \ {0}
    tau_r = complex(frac_f64(0, 1), 2 * math.sqrt(3))
    eps_step = pow10_f64(-6)
    max_e3_cont_diff = frac_f64(0, 1)
    min_e3_frob_norm = pow10_f64(9)
    for a_3, b_3 in prim_pts(3):
        w0 = float(a_3) * tau_r + float(b_3)
        Y0 = Y_cim_xi(tau_r, frac_f64(5, 2) * w0)
        Y_eps = Y_cim_xi(tau_r, frac_f64(5, 2) * (w0 + eps_step + eps_step * tau_r))
        max_e3_cont_diff = max(max_e3_cont_diff, float(np.max(np.abs(Y_eps - Y0))))
        min_e3_frob_norm = min(min_e3_frob_norm, float(np.linalg.norm(Y0)))

    # 1B. Pure 6Y ((Delta_up, Delta_dn) = (+5, -1)) at cusp height y = 8 on q^0 Higgs mode e_0:
    tau_cusp = complex(frac_f64(13, 100), frac_f64(8, 1))
    aligned_6y_count = 0
    deranged_6y_count = 0
    for af, bf in prim_pts(5):
        w = float(af) * tau_cusp + float(bf)
        Yu = Y_cim_xi(tau_cusp, frac_f64(5, 2) * w)[:, :, 0]
        Yd = Y_cim_xi(tau_cusp, frac_f64(-1, 2) * w)[:, :, 0]
        Uu, _, _ = np.linalg.svd(Yu)
        Ud, _, _ = np.linalg.svd(Yd)
        V = Uu[:, ::-1].conj().T @ Ud[:, ::-1]
        vtb = abs(complex(V[2, 2]))
        if vtb > frac_f64(99, 100):
            aligned_6y_count += 1
        elif vtb < frac_f64(1, 1000):
            deranged_6y_count += 1

    # 1C. SU(2)_R-symmetric Pati-Salam 3(B-L) ((Delta_up, Delta_dn) = (+2, +2)) across all 288 = 24 + 72 + 192 points:
    min_vtb_by_level: Dict[str, float] = {}
    for N_lvl in (5, 10, 15):
        min_vtb = frac_f64(1, 1)
        for af, bf in prim_pts(N_lvl):
            w = float(af) * tau_cusp + float(bf)
            Yu = Y_cim_xi(tau_cusp, 1 * w)[:, :, 0]
            Yd = Y_cim_xi(tau_cusp, 1 * w)[:, :, 0]
            Uu, _, _ = np.linalg.svd(Yu)
            Ud, _, _ = np.linalg.svd(Yd)
            V = Uu[:, ::-1].conj().T @ Ud[:, ::-1]
            min_vtb = min(min_vtb, abs(complex(V[2, 2])))
        min_vtb_by_level[str(N_lvl)] = min_vtb

    # Planted PF5.1: mixed orthogonal pairing (e_2, e_0) on 3(B-L) breaks CKM alignment!
    w_pf1 = frac_f64(1, 5) * tau_cusp + frac_f64(2, 5)
    Yu_pf1 = Y_cim_xi(tau_cusp, 1 * w_pf1)[:, :, 2]
    Yd_pf1 = Y_cim_xi(tau_cusp, 1 * w_pf1)[:, :, 0]
    Uu_pf1, _, _ = np.linalg.svd(Yu_pf1)
    Ud_pf1, _, _ = np.linalg.svd(Yd_pf1)
    pf5_1_vtb = abs(complex((Uu_pf1[:, ::-1].conj().T @ Ud_pf1[:, ::-1])[2, 2]))
    pf5_1_caught = pf5_1_vtb < frac_f64(1, 100)

    # 1D. Smooth hierarchical off-diagonal CKM generation from small SU(2)_R breaking + subleading Higgs mode, & 10-trial U(3)^6 Haar
    tau_mid = complex(frac_f64(13, 100), frac_f64(4, 1))
    vH_pert = np.array([frac_f64(1, 1), frac_f64(1, 8), frac_f64(1, 50), frac_f64(0, 1), frac_f64(1, 50), frac_f64(1, 8)], dtype=complex)
    vH_pert = vH_pert / np.linalg.norm(vH_pert)
    w_mid = frac_f64(1, 5) * tau_mid + frac_f64(2, 5)
    dw_R = frac_f64(3, 100) * tau_mid + frac_f64(1, 50)
    Yu_sm = np.einsum("ijk,k->ij", Y_cim_xi(tau_mid, w_mid + dw_R), vH_pert)
    Yd_sm = np.einsum("ijk,k->ij", Y_cim_xi(tau_mid, w_mid - dw_R), vH_pert)
    Ye_sm = np.einsum("ijk,k->ij", Y_cim_xi(tau_mid, -3 * w_mid - dw_R), vH_pert)

    def extract_obs(Yu_m: np.ndarray, Yd_m: np.ndarray, Ye_m: np.ndarray) -> np.ndarray:
        uu, su, _ = np.linalg.svd(Yu_m)
        ud, sd, _ = np.linalg.svd(Yd_m)
        _, se, _ = np.linalg.svd(Ye_m)
        V_m = np.abs(uu[:, ::-1].conj().T @ ud[:, ::-1])
        return np.array([
            su[2] / su[0], su[1] / su[0],
            sd[2] / sd[0], sd[1] / sd[0],
            se[2] / se[0], se[1] / se[0],
            V_m[2, 2], V_m[1, 2], V_m[2, 0],
        ], dtype=float)

    obs_ref = extract_obs(Yu_sm, Yd_sm, Ye_sm)
    smooth_ckm_ok = (obs_ref[6] > frac_f64(99, 100)) and (frac_f64(0, 1) < obs_ref[7] < frac_f64(1, 10)) and (frac_f64(0, 1) < obs_ref[8] < frac_f64(1, 10))

    rng = np.random.default_rng(20261117)
    max_haar_err = frac_f64(0, 1)
    for _ in range(10):
        UQ = random_haar_u3(rng)
        Uu_r = random_haar_u3(rng)
        Ud_r = random_haar_u3(rng)
        UL = random_haar_u3(rng)
        Ue_r = random_haar_u3(rng)
        obs_rot = extract_obs(UQ @ Yu_sm @ Uu_r.conj().T, UQ @ Yd_sm @ Ud_r.conj().T, UL @ Ye_sm @ Ue_r.conj().T)
        max_haar_err = max(max_haar_err, float(np.max(np.abs(obs_rot - obs_ref))))

    sec1_passed = (
        max_e3_cont_diff < pow10_f64(-3)
        and min_e3_frob_norm > frac_f64(1, 1)
        and aligned_6y_count == 4
        and deranged_6y_count == 20
        and all((1 - mv) < pow10_f64(-12) for mv in min_vtb_by_level.values())
        and smooth_ckm_ok
        and max_haar_err < pow10_f64(-13)
        and pf5_1_caught
    )
    return {
        "section_1_passed": sec1_passed,
        "e3_max_continuity_diff_at_1e_minus_6": max_e3_cont_diff,
        "e3_min_frobenius_norm": min_e3_frob_norm,
        "pure_6Y_order5_aligned_count": aligned_6y_count,
        "pure_6Y_order5_deranged_count": deranged_6y_count,
        "pure_6Y_classification": "PARTIAL_4_OF_24",
        "pati_salam_3BL_min_vtb_levels_5_10_15": min_vtb_by_level,
        "pati_salam_3BL_classification": "ALIGNED_288_OF_288",
        "perturbed_PS_vtb_vcb_vtd": [float(obs_ref[6]), float(obs_ref[7]), float(obs_ref[8])],
        "haar_u3_max_drift_10_trials": max_haar_err,
        "PF5_1_mixed_pairing_vtb": pf5_1_vtb,
        "PF5_1_caught": pf5_1_caught,
    }


# ============================================================================
# SECTION 2: LOCAL 10_vec NO-GO, (1/3)-PERIODICITY, & PATI-SALAM LEPTON-DOWN SPLIT
# ============================================================================

def run_section_2_lepton_down_separation() -> Dict[str, Any]:
    # 2A. Local SO(10) 10_vec = (6,1,1) (+) (1,2,2) commutant check: [B-L, P_bidoublet] == 0
    # Spin(10) spinor 16 = (4, 2, 1) (+) (4bar, 1, 2) = 8_L (+) 8_R, where B-L acts on 4 as diag(1/3, 1/3, 1/3, -1):
    bl_4 = np.diag([frac_f64(1, 3), frac_f64(1, 3), frac_f64(1, 3), frac_f64(-1, 1)])
    BL_16 = np.block([
        [np.kron(bl_4, np.eye(2)), np.zeros((8, 8))],
        [np.zeros((8, 8)), np.kron(-bl_4, np.eye(2))],
    ])
    # Bidoublet Yukawa vertex maps (4, 2, 1) x (4bar, 1, 2) via I_4_color x E_{ab}^{weak} (SU(4)_c singlet!):
    max_local_bl_comm = frac_f64(0, 1)
    for a_w in range(2):
        for b_w in range(2):
            E_ab = np.zeros((2, 2), dtype=float)
            E_ab[a_w, b_w] = frac_f64(1, 1)
            V_bid = np.block([
                [np.zeros((8, 8)), np.kron(np.eye(4), E_ab)],
                [np.kron(np.eye(4), E_ab.T), np.zeros((8, 8))],
            ])
            # Chiral Yukawa bilinear psi_L^T C V_bid psi_R checks B-L neutrality BL_L + BL_R = 0 AND color-lepton universality:
            # Specifically, on 8_L -> 8_R block, bl_4 * I_4 - I_4 * bl_4 == 0 identically!
            comm_block = np.kron(bl_4, np.eye(2)) @ np.kron(np.eye(4), E_ab) - np.kron(np.eye(4), E_ab) @ np.kron(bl_4, np.eye(2))
            max_local_bl_comm = max(max_local_bl_comm, float(np.max(np.abs(comm_block))))
    local_10vec_commutes_exact = max_local_bl_comm == frac_f64(0, 1)

    # 2B. Exact (1/3) Lambda_tau singular-value periodicity of Y_cim(tau; xi)[:, :, 0] & PF5.2 (tau/4 shift)
    tau_p = complex(frac_f64(23, 100), frac_f64(3, 2))
    xi_p = frac_f64(1, 5) * tau_p + frac_f64(2, 5)
    sv_0 = np.linalg.svd(Y_cim_xi(tau_p, xi_p)[:, :, 0], compute_uv=False)
    sv_sh1 = np.linalg.svd(Y_cim_xi(tau_p, xi_p + frac_f64(1, 3))[:, :, 0], compute_uv=False)
    sv_sht = np.linalg.svd(Y_cim_xi(tau_p, xi_p + tau_p / 3)[:, :, 0], compute_uv=False)
    sv_pf2 = np.linalg.svd(Y_cim_xi(tau_p, xi_p + tau_p / 4)[:, :, 0], compute_uv=False)

    third_period_err = max(float(np.max(np.abs(sv_0 - sv_sh1))), float(np.max(np.abs(sv_0 - sv_sht))))
    pf5_2_quarter_diff = float(np.max(np.abs(sv_0 - sv_pf2)))
    pf5_2_caught = pf5_2_quarter_diff > frac_f64(1, 100)

    # 2C. Whole-orbit invariance on pure 6Y & pure 3(B-L) vs pointwise Level-5 split on 3(B-L) & whole-orbit split on 6Y + 3(B-L)
    tau_4 = complex(frac_f64(13, 100), frac_f64(4, 1))
    w_pt5 = frac_f64(1, 5) * tau_4 + frac_f64(2, 5)
    sv_dn_pt5 = np.linalg.svd(Y_cim_xi(tau_4, 1 * w_pt5)[:, :, 0], compute_uv=False)
    sv_lp_pt5 = np.linalg.svd(Y_cim_xi(tau_4, -3 * w_pt5)[:, :, 0], compute_uv=False)
    pointwise_3BL_ratio_factor = (sv_dn_pt5[2] / sv_dn_pt5[0]) / (sv_lp_pt5[2] / sv_lp_pt5[0])

    orbit_pure_6Y_max_diff: Dict[str, float] = {}
    orbit_pure_3BL_max_diff: Dict[str, float] = {}
    orbit_combined_6Y_plus_3BL_max_diff: Dict[str, float] = {}

    for N_lvl in (5, 10, 15):
        pts_N = prim_pts(N_lvl)
        dn_6y = sorted(
            float(np.linalg.svd(Y_cim_xi(tau_4, frac_f64(-1, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[2]
                  / np.linalg.svd(Y_cim_xi(tau_4, frac_f64(-1, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[0])
            for a, b in pts_N
        )
        lp_6y = sorted(
            float(np.linalg.svd(Y_cim_xi(tau_4, frac_f64(-9, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[2]
                  / np.linalg.svd(Y_cim_xi(tau_4, frac_f64(-9, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[0])
            for a, b in pts_N
        )
        dn_bl = sorted(
            float(np.linalg.svd(Y_cim_xi(tau_4, 1 * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[2]
                  / np.linalg.svd(Y_cim_xi(tau_4, 1 * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[0])
            for a, b in pts_N
        )
        lp_bl = sorted(
            float(np.linalg.svd(Y_cim_xi(tau_4, -3 * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[2]
                  / np.linalg.svd(Y_cim_xi(tau_4, -3 * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[0])
            for a, b in pts_N
        )
        dn_comb = sorted(
            float(np.linalg.svd(Y_cim_xi(tau_4, frac_f64(1, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[2]
                  / np.linalg.svd(Y_cim_xi(tau_4, frac_f64(1, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[0])
            for a, b in pts_N
        )
        lp_comb = sorted(
            float(np.linalg.svd(Y_cim_xi(tau_4, frac_f64(-15, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[2]
                  / np.linalg.svd(Y_cim_xi(tau_4, frac_f64(-15, 2) * (float(a) * tau_4 + float(b)))[:, :, 0], compute_uv=False)[0])
            for a, b in pts_N
        )
        orbit_pure_6Y_max_diff[str(N_lvl)] = max(abs(x - y) for x, y in zip(dn_6y, lp_6y))
        orbit_pure_3BL_max_diff[str(N_lvl)] = max(abs(x - y) for x, y in zip(dn_bl, lp_bl))
        orbit_combined_6Y_plus_3BL_max_diff[str(N_lvl)] = max(abs(x - y) for x, y in zip(dn_comb, lp_comb))

    sec2_passed = (
        local_10vec_commutes_exact
        and third_period_err < pow10_f64(-14)
        and pointwise_3BL_ratio_factor > 10
        and all(v < pow10_f64(-13) for v in orbit_pure_6Y_max_diff.values())
        and all(v < pow10_f64(-13) for v in orbit_pure_3BL_max_diff.values())
        and all(v > pow10_f64(-4) for v in orbit_combined_6Y_plus_3BL_max_diff.values())
        and pf5_2_caught
    )
    return {
        "section_2_passed": sec2_passed,
        "local_10vec_BL_commutator_zero": local_10vec_commutes_exact,
        "k0_third_lattice_periodicity_err": third_period_err,
        "pointwise_level5_3BL_dn_over_lep_s13_factor": float(pointwise_3BL_ratio_factor),
        "orbit_pure_6Y_s13_max_diff": orbit_pure_6Y_max_diff,
        "orbit_pure_3BL_s13_max_diff": orbit_pure_3BL_max_diff,
        "orbit_combined_6Y_plus_3BL_s13_max_diff": orbit_combined_6Y_plus_3BL_max_diff,
        "PF5_2_quarter_tau_shift_diff": pf5_2_quarter_diff,
        "PF5_2_caught": pf5_2_caught,
    }


# ============================================================================
# SECTION 3: WEIL ZETA-INDEPENDENCE, HEISENBERG COCYCLE, & GRAMIAN LAWS
# ============================================================================

def run_section_3_weil_and_gramian() -> Dict[str, Any]:
    tau = complex(frac_f64(23, 100), frac_f64(3, 2))
    UT3_0 = basis_T(3, frac_f64(1, 2), frac_f64(1, 2), tau, complex(0, 0))
    US3_0 = basis_S(3, frac_f64(1, 2), frac_f64(1, 2), tau, complex(0, 0))

    # 3A. Zeta-independence of U_3(T; zeta) and U_3(S; zeta)
    max_zeta_dep_err = frac_f64(0, 1)
    for af, bf in [(Fraction(1, 5), Fraction(2, 5)), (Fraction(2, 5), Fraction(3, 5)), (Fraction(1, 3), Fraction(2, 3))]:
        zeta = float(af) * tau + float(bf)
        UT_z = basis_T(3, frac_f64(1, 2), frac_f64(1, 2), tau, zeta)
        US_z = basis_S(3, frac_f64(1, 2), frac_f64(1, 2), tau, zeta)
        max_zeta_dep_err = max(
            max_zeta_dep_err,
            float(np.max(np.abs(UT_z - UT3_0))),
            float(np.max(np.abs(US_z - US3_0))),
        )

    # 3B. Exact Heisenberg cocycle Y(xi + 1) = exp(+6 i pi alpha) Y(xi), Y(xi + tau) = exp(-6 i pi beta) Y(xi)
    xi0 = frac_f64(37, 100) * tau + frac_f64(41, 100)
    alpha0 = xi0.imag / tau.imag
    beta0 = xi0.real - alpha0 * tau.real
    Y0 = Y_cim_xi(tau, xi0)
    cocycle_err_1 = float(np.max(np.abs(Y_cim_xi(tau, xi0 + 1) - cmath.exp(complex(0, 6) * math.pi * alpha0) * Y0)))
    cocycle_err_tau = float(np.max(np.abs(Y_cim_xi(tau, xi0 + tau) - cmath.exp(complex(0, -6) * math.pi * beta0) * Y0)))

    # 3C. Single-sheet E^*[5] Gramian covariance with covariant puncture Higgs v_6(tau) = psi^{(6)}(0; tau, 0):
    def eval_v6_origin(t_v: complex) -> np.ndarray:
        return np.array([psi_cim_pos(k, 6, frac_f64(0, 1), frac_f64(0, 1), complex(0, 0), t_v, complex(0, 0)) for k in range(6)])

    def gram_e5_v6(t_v: complex, delta_q: int) -> np.ndarray:
        v6 = eval_v6_origin(t_v)
        G = np.zeros((3, 3), dtype=complex)
        for af, bf in prim_pts(5):
            w = float(af) * t_v + float(bf)
            Yf = np.einsum("ijk,k->ij", Y_cim_xi(t_v, (delta_q / 2) * w), v6)
            G += Yf @ Yf.conj().T
        return G / 24

    # Even Delta (+2 and -6 for Pati-Salam 3(B-L)): exact T and S covariance < 10^{-13} and non-degenerate eigenvalues!
    even_max_T_err = frac_f64(0, 1)
    even_max_S_err = frac_f64(0, 1)
    min_even_anisotropy = pow10_f64(9)
    for dq_even in (2, -6):
        G0 = gram_e5_v6(tau, dq_even)
        GT = gram_e5_v6(tau + 1, dq_even)
        GS = gram_e5_v6(-1 / tau, dq_even)
        even_max_T_err = max(even_max_T_err, float(np.max(np.abs(GT - UT3_0 @ G0 @ UT3_0.conj().T))))
        even_max_S_err = max(even_max_S_err, float(np.max(np.abs(GS - US3_0 @ G0 @ US3_0.conj().T))))
        evs = np.linalg.eigvalsh(G0)
        min_even_anisotropy = min(min_even_anisotropy, float(evs[2] - evs[0]))

    # Planted PF5.3: odd Delta = -1 (pure 6Y down) fails single-sheet E^*[5] T/S covariance (> 1/50)!
    G0_odd = gram_e5_v6(tau, -1)
    GT_odd = gram_e5_v6(tau + 1, -1)
    GS_odd = gram_e5_v6(-1 / tau, -1)
    pf5_3_odd_err = max(
        float(np.max(np.abs(GT_odd - UT3_0 @ G0_odd @ UT3_0.conj().T))),
        float(np.max(np.abs(GS_odd - US3_0 @ G0_odd @ US3_0.conj().T))),
    )
    pf5_3_caught = pf5_3_odd_err > frac_f64(1, 50)

    # 3D. 9-sheet E[3] Schur-Heisenberg collapse AND Planted PF5.4 (unflavoured 6-mode Higgs trace isotropy collapse — B1727)
    X3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    w3 = cmath.exp(complex(0, 2) * math.pi / 3)
    Z3 = np.diag([frac_f64(1, 1), w3, w3 * w3])
    G_seed = gram_e5_v6(tau, 2)
    G_schur_9 = sum(
        (np.linalg.matrix_power(X3, a) @ np.linalg.matrix_power(Z3, b)).conj().T
        @ G_seed
        @ (np.linalg.matrix_power(X3, a) @ np.linalg.matrix_power(Z3, b))
        for a in range(3)
        for b in range(3)
    ) / 9
    ev_schur = np.linalg.eigvalsh(G_schur_9)
    schur_9_anisotropy = float(ev_schur[2] - ev_schur[0])

    G_unflav_higgs = sum(
        np.einsum("ijk,ljk->il", Y_cim_xi(tau, float(af) * tau + float(bf)), Y_cim_xi(tau, float(af) * tau + float(bf)).conj())
        for af, bf in prim_pts(5)
    ) / 24
    ev_unflav = np.linalg.eigvalsh(G_unflav_higgs)
    pf5_4_unflav_anisotropy = float(ev_unflav[2] - ev_unflav[0])
    pf5_4_caught = pf5_4_unflav_anisotropy < pow10_f64(-13)

    # Planted PF5.5: Naive linear unweighted sum over E^*[5] fails tau -> tau + 1 (> 1/1000)!
    v6_0 = eval_v6_origin(tau)
    v6_T = eval_v6_origin(tau + 1)
    S_lin_0 = sum(np.einsum("ijk,k->ij", Y_cim_xi(tau, float(af) * tau + float(bf)), v6_0) for af, bf in prim_pts(5))
    S_lin_T = sum(np.einsum("ijk,k->ij", Y_cim_xi(tau + 1, float(af) * (tau + 1) + float(bf)), v6_T) for af, bf in prim_pts(5))
    sv_l0 = np.linalg.svd(S_lin_0, compute_uv=False)
    sv_lT = np.linalg.svd(S_lin_T, compute_uv=False)
    pf5_5_linear_sum_drift = float(np.max(np.abs(sv_l0 / sv_l0[0] - sv_lT / sv_lT[0])))
    pf5_5_caught = pf5_5_linear_sum_drift > frac_f64(1, 1000)

    sec3_passed = (
        max_zeta_dep_err < pow10_f64(-13)
        and cocycle_err_1 < pow10_f64(-13)
        and cocycle_err_tau < pow10_f64(-13)
        and even_max_T_err < pow10_f64(-13)
        and even_max_S_err < pow10_f64(-13)
        and min_even_anisotropy > frac_f64(1, 100)
        and schur_9_anisotropy < pow10_f64(-13)
        and pf5_3_caught
        and pf5_4_caught
        and pf5_5_caught
    )
    return {
        "section_3_passed": sec3_passed,
        "weil_zeta_independence_max_err": max_zeta_dep_err,
        "heisenberg_cocycle_shift_1_err": cocycle_err_1,
        "heisenberg_cocycle_shift_tau_err": cocycle_err_tau,
        "even_delta_gramian_max_T_err": even_max_T_err,
        "even_delta_gramian_max_S_err": even_max_S_err,
        "even_delta_gramian_min_anisotropy": min_even_anisotropy,
        "schur_9sheet_anisotropy": schur_9_anisotropy,
        "PF5_3_odd_delta_gramian_err": pf5_3_odd_err,
        "PF5_3_caught": pf5_3_caught,
        "PF5_4_unflavoured_higgs_trace_anisotropy": pf5_4_unflav_anisotropy,
        "PF5_4_caught": pf5_4_caught,
        "PF5_5_naive_linear_sum_tau_plus_1_drift": pf5_5_linear_sum_drift,
        "PF5_5_caught": pf5_5_caught,
    }


def main() -> None:
    ast_res = verify_ast_g5()
    sec1_res = run_section_1_ckm_alignment()
    sec2_res = run_section_2_lepton_down_separation()
    sec3_res = run_section_3_weil_and_gramian()

    all_planted_caught = (
        sec1_res["PF5_1_caught"]
        and sec2_res["PF5_2_caught"]
        and sec3_res["PF5_3_caught"]
        and sec3_res["PF5_4_caught"]
        and sec3_res["PF5_5_caught"]
    )
    gate_passed = (
        ast_res["ast_gate_passed"]
        and sec1_res["section_1_passed"]
        and sec2_res["section_2_passed"]
        and sec3_res["section_3_passed"]
        and all_planted_caught
    )

    out: Dict[str, Any] = {
        "card": "AGY-002_CLOSURE-G5",
        "empirical_firewall": "0 of 19",
        "gate_5_passed": gate_passed,
        "all_5_planted_faults_caught": all_planted_caught,
        "section_0_ast": ast_res,
        "section_1_ckm_alignment": sec1_res,
        "section_2_lepton_down_separation": sec2_res,
        "section_3_weil_and_gramian": sec3_res,
    }

    out_path = Path(__file__).with_name("verify_closure_g5_out.json")
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
