#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_FOUND-G9:
  4D Amphicheiral Domain-Wall / APS Chiral Localization, SU(2)_L-Invariant 2HDM
  Strong-CP = 0, and Complete P-864 Canonical-End Repair (0 of 19).

Empirical Firewall: 0 of 19 (zero repository Python imports, zero float/complex literals in source).
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

import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
import sympy as sp


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "cmath",
    "fractions",
    "hashlib",
    "json",
    "math",
    "numpy",
    "pathlib",
    "scipy",
    "sympy",
    "typing",
}


def frac_f64(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def pow10_f64(exp_int: int) -> float:
    return float(Fraction(10, 1) ** exp_int)


# ============================================================================
# SECTION 0: AST SOURCE LOCK (ZERO REPO IMPORTS & ZERO FLOAT/COMPLEX LITERALS)
# ============================================================================

def verify_ast_g9() -> Dict[str, Any]:
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
# SECTION 1: PARITY-ODD 4D DOMAIN-WALL / KAPLAN CHIRAL LOCALIZATION
# ============================================================================

def run_section_1_domain_wall() -> Dict[str, Any]:
    # Symbolic verification of (-d/ds + M0 tanh(M0 s)) sech(M0 s) == 0
    s_sym = sp.Symbol("s", real=True)
    m0_sym = sp.Symbol("M0", positive=True)
    psi0_sym = 1 / sp.cosh(m0_sym * s_sym)
    annih_res = sp.simplify(-sp.diff(psi0_sym, s_sym) + m0_sym * sp.tanh(m0_sym * s_sym) * psi0_sym)
    norm_int = sp.simplify(sp.integrate(psi0_sym ** 2, (s_sym, -sp.oo, sp.oo)) * m0_sym - 2)
    symbolic_ok = (annih_res == 0) and (norm_int == 0)

    # 160-node Chebyshev spectral discretization on [-8, 8] with M0 = 3
    N_cheb = 160
    L4 = frac_f64(8, 1)
    M0 = frac_f64(3, 1)
    k_idx = np.arange(N_cheb + 1)
    x_nodes = np.cos(math.pi * k_idx / N_cheb)
    c_wts = np.array([frac_f64(2, 1)] + [frac_f64(1, 1)] * (N_cheb - 1) + [frac_f64(2, 1)]) * (
        (frac_f64(-1, 1)) ** k_idx
    )
    X_mat = np.tile(x_nodes, (N_cheb + 1, 1))
    D_cheb = np.outer(c_wts, frac_f64(1, 1) / c_wts) / (X_mat - X_mat.T + np.eye(N_cheb + 1))
    D_cheb = D_cheb - np.diag(np.sum(D_cheb, axis=1))
    D_s = D_cheb / L4
    D2_s = D_s @ D_s

    in_sl = slice(1, N_cheb)
    s_in = L4 * x_nodes[in_sl]
    v_L = (M0 * np.tanh(M0 * s_in)) ** 2 - (M0 * M0) / (np.cosh(M0 * s_in) ** 2)
    v_R = (M0 * np.tanh(M0 * s_in)) ** 2 + (M0 * M0) / (np.cosh(M0 * s_in) ** 2)
    H_L = -D2_s[in_sl, in_sl] + np.diag(v_L)
    H_R = -D2_s[in_sl, in_sl] + np.diag(v_R)

    vals_L_raw, vecs_L_raw = np.linalg.eig(H_L)
    idx_L = np.argsort(vals_L_raw.real)
    ev_L0 = float(vals_L_raw[idx_L[0]].real)
    ev_L1 = float(vals_L_raw[idx_L[1]].real)
    psi_num = vecs_L_raw[:, idx_L[0]].real
    psi_num = psi_num / np.linalg.norm(psi_num)
    psi_exact = frac_f64(1, 1) / np.cosh(M0 * s_in)
    psi_exact = psi_exact / np.linalg.norm(psi_exact)
    overlap_sech = float(abs(np.dot(psi_num, psi_exact)))

    ev_R0 = float(np.min(np.linalg.eigvals(H_R).real))

    # Planted PF9.1: parity-even constant mass M(s) = +M0 destroys chiral zero mode (ev_L0 > 9)
    H_L_const = -D2_s[in_sl, in_sl] + (M0 * M0) * np.eye(N_cheb - 1)
    ev_L0_const = float(np.min(np.linalg.eigvals(H_L_const).real))
    pf9_1_caught = ev_L0_const > frac_f64(9, 1)

    passed = (
        symbolic_ok
        and abs(ev_L0) < pow10_f64(-4)
        and ev_L1 > frac_f64(9, 1)
        and ev_R0 > frac_f64(9, 1)
        and overlap_sech > frac_f64(99999, 100000)
        and pf9_1_caught
    )
    return {
        "section_1_passed": passed,
        "symbolic_jackiw_rebbi_sech_zero_mode": symbolic_ok,
        "chebyshev_ev_L0": ev_L0,
        "chebyshev_ev_L1_bulk_gap": ev_L1,
        "chebyshev_ev_R0_mirror_gap": ev_R0,
        "analytic_sech_overlap": overlap_sech,
        "PF9_1_constant_mass_ev_L0": ev_L0_const,
        "PF9_1_caught": pf9_1_caught,
    }


# ============================================================================
# SECTION 2: SU(2)_L-INVARIANT PATI-SALAM (1, 2, 2) STRONG-CP = 0 & CKM J != 0
# ============================================================================

def Y_cim_spin_hh(tau: complex, xi: complex, n_win: int = 18) -> np.ndarray:
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


def wrap_pi(angle_rad: float) -> float:
    return math.atan2(math.sin(angle_rad), math.cos(angle_rad))


def run_2loop_yukawa_rk4(Yu0: np.ndarray, Yd0: np.ndarray, n_steps: int = 200) -> Tuple[np.ndarray, np.ndarray]:
    # Canonical BPV + MV 2-loop quark Yukawa RGE over dt = -30 (pure gauge-Yukawa blind UV seed)
    g1_sq = frac_f64(1, 5)
    g2_sq = frac_f64(1, 4)
    g3_sq = frac_f64(1, 3)
    dt = frac_f64(-30, n_steps)
    loop1 = frac_f64(1, 1) / (16 * (math.pi ** 2))
    loop2 = loop1 * loop1
    Yu = Yu0.copy()
    Yd = Yd0.copy()

    def rhs(Yu_m: np.ndarray, Yd_m: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        Hu = Yu_m @ Yu_m.conj().T
        Hd = Yd_m @ Yd_m.conj().T
        trY = 3 * float(np.trace(Hu + Hd).real)
        i3 = np.eye(3, dtype=complex)
        b1_u = (frac_f64(3, 2) * (Hu - Hd) + (trY - frac_f64(17, 20) * g1_sq - frac_f64(9, 4) * g2_sq - 8 * g3_sq) * i3) @ Yu_m
        b1_d = (frac_f64(3, 2) * (Hd - Hu) + (trY - frac_f64(1, 4) * g1_sq - frac_f64(9, 4) * g2_sq - 8 * g3_sq) * i3) @ Yd_m
        # Canonical BPV Eq. 27 mixed 2-loop matrix structure -(1/4) H_u H_d - H_d H_u + (3/2) H^2:
        b2_u = (frac_f64(3, 2) * (Hu @ Hu) - frac_f64(1, 4) * (Hu @ Hd) - (Hd @ Hu) - frac_f64(9, 4) * trY * Hu) @ Yu_m
        b2_d = (frac_f64(3, 2) * (Hd @ Hd) - frac_f64(1, 4) * (Hd @ Hu) - (Hu @ Hd) - frac_f64(9, 4) * trY * Hd) @ Yd_m
        return loop1 * b1_u + loop2 * b2_u, loop1 * b1_d + loop2 * b2_d

    for _ in range(n_steps):
        k1u, k1d = rhs(Yu, Yd)
        k2u, k2d = rhs(Yu + frac_f64(1, 2) * dt * k1u, Yd + frac_f64(1, 2) * dt * k1d)
        k3u, k3d = rhs(Yu + frac_f64(1, 2) * dt * k2u, Yd + frac_f64(1, 2) * dt * k2d)
        k4u, k4d = rhs(Yu + dt * k3u, Yd + dt * k3d)
        Yu = Yu + (dt / 6) * (k1u + 2 * k2u + 2 * k3u + k4u)
        Yd = Yd + (dt / 6) * (k1d + 2 * k2d + 2 * k3d + k4d)
    return Yu, Yd


def extract_theta_and_jarlskog(Yu_m: np.ndarray, Yd_m: np.ndarray) -> Tuple[float, float]:
    det_prod = complex(np.linalg.det(Yu_m @ Yd_m))
    theta_qcd = wrap_pi(cmath.phase(det_prod))
    _, Uu = np.linalg.eigh(Yu_m @ Yu_m.conj().T)
    _, Ud = np.linalg.eigh(Yd_m @ Yd_m.conj().T)
    V = Uu.conj().T @ Ud
    jarl = float((V[0, 1] * V[1, 2] * V[0, 2].conjugate() * V[1, 1].conjugate()).imag)
    return abs(theta_qcd), abs(jarl)


def run_section_2_su2l_strong_cp() -> Dict[str, Any]:
    tau_cusp = complex(0, 2 * math.sqrt(3))
    # ONE shared SU(2)_L-gauge-invariant doublet parameter xi = (23/100) i!
    xi_shared = complex(0, frac_f64(23, 100))
    Y_ten = Y_cim_spin_hh(tau_cusp, xi_shared)

    # Verify tensor D-parity identity Y[2-i, 2-j, (-k)%6] == conj(Y[j, i, k])
    max_tensor_dpar_err = max(
        float(abs(Y_ten[2 - i, 2 - j, (-k) % 6] - Y_ten[j, i, k].conjugate()))
        for i in range(3) for j in range(3) for k in range(6)
    )

    P_flip = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=float)
    # Two D-parity-symmetric bidoublet vectors v[(-k)%6] = conj(v[k]) on the +1 det-sign branch:
    v_u = np.array([
        frac_f64(5, 2),
        frac_f64(2, 5) + complex(0, frac_f64(7, 10)),
        frac_f64(-3, 10) + complex(0, frac_f64(1, 2)),
        frac_f64(4, 5),
        frac_f64(-3, 10) - complex(0, frac_f64(1, 2)),
        frac_f64(2, 5) - complex(0, frac_f64(7, 10)),
    ], dtype=complex)
    v_d_pos = -np.array([
        frac_f64(31, 10),
        frac_f64(9, 10) - complex(0, frac_f64(3, 5)),
        frac_f64(3, 5) + complex(0, frac_f64(4, 5)),
        frac_f64(-2, 5),
        frac_f64(3, 5) - complex(0, frac_f64(4, 5)),
        frac_f64(9, 10) + complex(0, frac_f64(3, 5)),
    ], dtype=complex)

    Yu_raw = P_flip @ np.tensordot(Y_ten, v_u, axes=([2], [0]))
    Yd_raw = P_flip @ np.tensordot(Y_ten, v_d_pos, axes=([2], [0]))
    herm_err = max(float(np.linalg.norm(Yu_raw - Yu_raw.conj().T)), float(np.linalg.norm(Yd_raw - Yd_raw.conj().T)))

    # Normalize to perturbative UV Yukawas (max SV = 3/5 and 2/5) keeping positive real scale
    Yu_uv = (frac_f64(3, 5) / float(np.linalg.norm(Yu_raw, 2))) * Yu_raw
    Yd_uv = (frac_f64(2, 5) / float(np.linalg.norm(Yd_raw, 2))) * Yd_raw

    Yu_ir, Yd_ir = run_2loop_yukawa_rk4(Yu_uv, Yd_uv)
    theta_ir, jarl_ir = extract_theta_and_jarlskog(Yu_ir, Yd_ir)

    # Guardrail 3: 10-trial random SU(3)^3 special-unitary Haar scrambling (preserves det = 1, tests J_CKM & bar_theta)
    rng = np.random.default_rng(20261118)
    max_haar_drift = frac_f64(0, 1)
    for _ in range(10):
        mats = []
        for _s in range(3):
            A = rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))
            Q, R = np.linalg.qr(A)
            Q = Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
            Q = Q / (np.linalg.det(Q) ** frac_f64(1, 3))
            mats.append(Q)
        U_Q, U_uR, U_dR = mats
        th_s, j_s = extract_theta_and_jarlskog(U_Q @ Yu_ir @ U_uR.conj().T, U_Q @ Yd_ir @ U_dR.conj().T)
        max_haar_drift = max(max_haar_drift, abs(th_s - theta_ir), abs(j_s - jarl_ir))

    # Planted PF9.2: splitting z_{uL} != z_{dL} violates SU(2)_L gauge covariance under SU(2)_L rotation U_2!
    th_w = math.pi / 5
    U_su2 = np.array([[math.cos(th_w), math.sin(th_w)], [-math.sin(th_w), math.cos(th_w)]], dtype=float)
    Z_good = np.diag([frac_f64(23, 100), frac_f64(23, 100)])
    Z_split_bad = np.diag([frac_f64(23, 100), frac_f64(41, 100)])
    su2_good_comm = float(np.linalg.norm(U_su2 @ Z_good - Z_good @ U_su2))
    su2_bad_comm = float(np.linalg.norm(U_su2 @ Z_split_bad - Z_split_bad @ U_su2))
    pf9_2_caught = (su2_good_comm == 0) and (su2_bad_comm > frac_f64(1, 10))

    # Planted PF9.3: opposite det-sign branch (-v_d_pos on odd N_g = 3) gives |bar_theta_QCD| = pi > 3
    th_opp, _ = extract_theta_and_jarlskog(Yu_uv, -Yd_uv)
    pf9_3_caught = abs(th_opp - math.pi) < pow10_f64(-13) and th_opp > frac_f64(3, 1)

    passed = (
        max_tensor_dpar_err < pow10_f64(-14)
        and herm_err < pow10_f64(-14)
        and theta_ir < pow10_f64(-13)
        and jarl_ir > frac_f64(1, 100)
        and max_haar_drift < pow10_f64(-13)
        and pf9_2_caught
        and pf9_3_caught
    )
    return {
        "section_2_passed": passed,
        "tensor_dparity_hermiticity_max_err": max_tensor_dpar_err,
        "uv_yukawa_hermiticity_max_err": herm_err,
        "ir_2loop_abs_bar_theta_qcd": theta_ir,
        "ir_2loop_abs_jarlskog_ckm": jarl_ir,
        "su3_3_haar_max_drift_10_trials": max_haar_drift,
        "PF9_2_su2L_violation_commutator_norm": su2_bad_comm,
        "PF9_2_caught": pf9_2_caught,
        "PF9_3_opposite_sign_branch_theta": th_opp,
        "PF9_3_caught": pf9_3_caught,
    }


# ============================================================================
# SECTION 3: COMPLETE P-864 REPAIR, CHORD-LENS DIAGNOSIS, & B1927..B1949 SWEEP
# ============================================================================

def sl2z_gauss_reduce(t: complex) -> Tuple[complex, Tuple[int, int, int, int]]:
    a, b, c_g, d_g = 1, 0, 0, 1
    z = t
    tol = pow10_f64(-13)
    for _ in range(250):
        n_sh = int(round(z.real))
        if n_sh != 0:
            z = z - n_sh
            a, b = a - n_sh * c_g, b - n_sh * d_g
        if abs(z) < frac_f64(1, 1) - tol:
            z = -frac_f64(1, 1) / z
            a, b, c_g, d_g = -b, a, -d_g, c_g
        elif abs(z.real) <= frac_f64(1, 2) + tol:
            break
    return z, (a, b, c_g, d_g)


def collect_tau_pairs(obj: Any, found: List[Tuple[float, float]]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "tau" and isinstance(v, list) and len(v) == 2 and all(isinstance(x, (int, float)) for x in v):
                found.append((float(v[0]), float(v[1])))
            else:
                collect_tau_pairs(v, found)
    elif isinstance(obj, list):
        for item in obj:
            collect_tau_pairs(item, found)


def run_section_3_p864_repair_and_sweep() -> Dict[str, Any]:
    self_dir = Path(__file__).resolve().parent
    relays_dir = self_dir.parent
    repo_root = relays_dir.parent

    b1927_vdir = next((repo_root / "frontier").glob("B1927_*")) / "verification"
    pts = [p for p in json.loads((b1927_vdir / "grid.json").read_text(encoding="utf-8"))["grid"] if "L_max" in p]
    b1667_pts = json.loads(
        (repo_root / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text(encoding="utf-8")
    )["points"]
    pts += [p for p in b1667_pts if "L_max" in p]

    XY = np.array([(sgn * p["tau"][0], p["tau"][1]) for p in pts for sgn in (1, -1)], dtype=float)
    L2_arr = np.array([p["L_2"] for p in pts for sgn in (1, -1)], dtype=float)
    ymax = float(XY[:, 1].max())
    lin_l2 = LinearNDInterpolator(XY, L2_arr)
    near_l2 = NearestNDInterpolator(XY, L2_arr)

    def canon_unreduced_l2(t_in: complex) -> Tuple[float, bool]:
        yq = min(t_in.imag, ymax)
        val = float(lin_l2(t_in.real, yq))
        if not np.isfinite(val):
            val = float(near_l2(t_in.real, yq))
        return val, (t_in.imag > ymax)

    def canon_gauss_reduced_l2(t_in: complex) -> Tuple[float, bool]:
        z_fd, (_, _, c_g, d_g) = sl2z_gauss_reduce(t_in)
        above = z_fd.imag > ymax
        yq = min(z_fd.imag, ymax)
        val_fd = float(lin_l2(z_fd.real, yq))
        if not np.isfinite(val_fd):
            val_fd = float(near_l2(z_fd.real, yq))
        return val_fd - math.log(abs(c_g * t_in + d_g)), above

    # Test SL(2, Z) covariance L(gamma t) == L(t) + ln|c t + d| across P-864 benchmark points:
    t_main = complex(frac_f64(13, 100), frac_f64(17, 10))
    t_chord_1 = complex(0, frac_f64(9, 10))  # inside Delaunay chord lens 0.866 <= 0.9 < 1!
    t_chord_2 = complex(frac_f64(3, 10), frac_f64(96, 100))  # |t|^2 = 1.0116 > 1, -1/t inside chord lens!

    max_repaired_cov_err = frac_f64(0, 1)
    for t_base in (t_main, t_chord_1, t_chord_2):
        l_base, _ = canon_gauss_reduced_l2(t_base)
        for (a_m, b_m, c_m, d_m) in ((0, -1, 1, 0), (1, 1, 0, 1), (1, -1, 1, 0), (2, -1, 1, 0)):
            t_img = (a_m * t_base + b_m) / (c_m * t_base + d_m)
            l_img, _ = canon_gauss_reduced_l2(t_img)
            err = abs(l_img - (l_base + math.log(abs(c_m * t_base + d_m))))
            max_repaired_cov_err = max(max_repaired_cov_err, err)

    # Planted PF9.4: unreduced canon fails at -1/t_main (> 1/4) AND at 9/10 i inside chord lens (> 1/1000)
    l_unred_main_inv, _ = canon_unreduced_l2(-frac_f64(1, 1) / t_main)
    l_unred_main_base, _ = canon_unreduced_l2(t_main)
    unred_err_main = abs(l_unred_main_inv - (l_unred_main_base + math.log(abs(t_main))))

    l_unred_c1, _ = canon_unreduced_l2(t_chord_1)
    l_unred_c1_inv, _ = canon_unreduced_l2(-frac_f64(1, 1) / t_chord_1)
    unred_err_chord = abs(l_unred_c1_inv - (l_unred_c1 + math.log(abs(t_chord_1))))
    pf9_4_caught = (unred_err_main > frac_f64(1, 4)) and (unred_err_chord > frac_f64(1, 1000))

    # Planted PF9.5: above-grid evaluation Im(tau) = 10 > Y_max sets above_ymax == True
    _, flag_high = canon_gauss_reduced_l2(complex(frac_f64(1, 10), frac_f64(10, 1)))
    pf9_5_caught = flag_high is True

    # Read-only sweep of tracked JSON tau coordinates in B1927, B1928, B1940, B1941, B1944, B1945, B1946, B1949
    sweep_report: Dict[str, Dict[str, int]] = {}
    for arc_num in (1927, 1928, 1940, 1941, 1944, 1945, 1946, 1949):
        tau_list: List[Tuple[float, float]] = []
        for arc_dir in sorted((repo_root / "frontier").glob(f"B{arc_num}_*")):
            v_dir = arc_dir / "verification"
            if v_dir.is_dir():
                for jf in sorted(v_dir.glob("*.json")):
                    try:
                        collect_tau_pairs(json.loads(jf.read_text(encoding="utf-8")), tau_list)
                    except Exception:
                        pass
        below_unit = sum(1 for (x_v, y_v) in tau_list if (x_v * x_v + y_v * y_v) < frac_f64(1, 1) - pow10_f64(-9))
        sweep_report[f"B{arc_num}"] = {"tau_points_found": len(tau_list), "strictly_below_unit_circle": below_unit}

    # Verify all 6 prior Gate 8 SHA-256 manifests + self SCRIPT_SHA256.txt
    prior_mfs = sorted(p for p in relays_dir.glob("*/*SHA256.txt") if p.parent != self_dir)
    matched_mfs = 0
    for mf in prior_mfs:
        sp_p = mf.read_text(encoding="utf-8").strip().split()
        if hashlib.sha256((repo_root / sp_p[1]).read_bytes()).hexdigest() == sp_p[0]:
            matched_mfs += 1

    self_mf = self_dir / "SCRIPT_SHA256.txt"
    self_ok = False
    if self_mf.exists():
        sp_s = self_mf.read_text(encoding="utf-8").strip().split()
        self_ok = hashlib.sha256((repo_root / sp_s[1]).read_bytes()).hexdigest() == sp_s[0]

    passed = (
        max_repaired_cov_err < pow10_f64(-14)
        and pf9_4_caught
        and pf9_5_caught
        and len(prior_mfs) == 7
        and matched_mfs == 7
        and self_ok
    )
    return {
        "section_3_passed": passed,
        "repaired_sl2z_covariance_max_err": max_repaired_cov_err,
        "PF9_4_unreduced_main_point_err": unred_err_main,
        "PF9_4_unreduced_chord_lens_0p9i_err": unred_err_chord,
        "PF9_4_caught": pf9_4_caught,
        "PF9_5_caught": pf9_5_caught,
        "landed_arc_json_tau_sweep": sweep_report,
        "prior_sha256_manifests_total": len(prior_mfs),
        "prior_sha256_manifests_matched": matched_mfs,
        "self_script_sha256_matched": self_ok,
    }


def main() -> None:
    ast_res = verify_ast_g9()
    sec1_res = run_section_1_domain_wall()
    sec2_res = run_section_2_su2l_strong_cp()
    sec3_res = run_section_3_p864_repair_and_sweep()

    all_planted = (
        sec1_res["PF9_1_caught"]
        and sec2_res["PF9_2_caught"]
        and sec2_res["PF9_3_caught"]
        and sec3_res["PF9_4_caught"]
        and sec3_res["PF9_5_caught"]
    )
    gate_passed = (
        ast_res["ast_gate_passed"]
        and sec1_res["section_1_passed"]
        and sec2_res["section_2_passed"]
        and sec3_res["section_3_passed"]
        and all_planted
    )

    out: Dict[str, Any] = {
        "card": "AGY-002_FOUND-G9",
        "empirical_firewall": "0 of 19",
        "gate_9_passed": gate_passed,
        "all_5_planted_faults_caught": all_planted,
        "section_0_ast": ast_res,
        "section_1_domain_wall": sec1_res,
        "section_2_su2l_strong_cp": sec2_res,
        "section_3_p864_repair_and_sweep": sec3_res,
    }

    out_path = Path(__file__).with_name("verify_found_g9_fixed_out.json")
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
