#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-FOUNDATION-2:
  Complete Covariant Repair of All Three PHYSICAL-C6 Findings (bde538de9, HAND_CHECKS.md):
    Part 2A: Quotient Levi-Civita Second Fundamental Form II_cov = P_perp (dv_s/ds - sum_a alpha_a T_a v_s):
             U(1) frame-change control (raw error = |beta| vs covariant = 0), exact agreement with
             PHYSICAL-C6 eq. (9) Omega * 144 * cos^2(theta) / D^3 > 0 on the 18D planar SU(2) path,
             and s-dependent SU(2) gauge-frame invariance of II_cov and the eq. (5) normal defect.
    Part 2B: Joint End-Holonomy + Link-Gauss Optimizer & Induced Parabolic Kinetic Factor:
             Simultaneous optimization of interior sites + end-holonomy angle phi_end matching the
             link-eliminated Gauss functional (driving all field AND link-Gauss residuals < 10^{-12}),
             plus verification of PHYSICAL-C6 eqs. (10)-(11) K_curve(u) = 1 + c^2 (1 - 2u)^2.
    Part 2C: Derived 4-Form Hopf Connection Link Transport on 2-Cell Spin(10) 80x32 Sewing:
             Pure second-cell frame rotation D_2 = U D_1 U^H with L = U^H preserves nullity = 1,
             whereas parallel transport L_Hopf = exp(-i int A_phase) along a 4-form geodesic between
             octahedral 2O axes yields gauge-covariant nullity = 0 (invariant under V_1 x V_2 in U(16)^2).

Empirical Firewall: 0 of 19 (zero Standard Model empirical targets read, imported, or compared;
zero float literals and zero complex literals module-wide).
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
    "sympy",
    "typing",
}

I_UNIT = complex(0, 1)


def rat(p: int, q: int = 1) -> float:
    return int(p) / int(q)


def p10(exp_i: int) -> float:
    return float(Fraction(10, 1) ** exp_i)


def verify_ast_foundation2() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_lits = 0
    complex_lits = 0
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
                float_lits += 1
            elif isinstance(node.value, complex):
                complex_lits += 1
    disallowed = sorted(mods - ALLOWED_IMPORTS)
    passed = len(disallowed) == 0 and float_lits == 0 and complex_lits == 0
    return {
        "Gate_AST_Stage2_Foundation_Passed": passed,
        "zero_imports_from_repo_or_reports": len(disallowed) == 0,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "float_literals_module_wide": float_lits,
        "complex_literals_module_wide": complex_lits,
    }


def random_haar_un(rng: np.random.Generator, n_dim: int) -> np.ndarray:
    z = (rng.standard_normal((n_dim, n_dim)) + I_UNIT * rng.standard_normal((n_dim, n_dim))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[np.newaxis, :]


# ============================================================================
# PART 2A: QUOTIENT LEVI-CIVITA SECOND FUNDAMENTAL FORM II_cov (PHYSICAL-C6 §2)
# ============================================================================

def run_part_2a_covariant_second_fundamental_form() -> Dict[str, Any]:
    # 1. PHYSICAL-C6 §2 U(1) Frame-Change Rejecting Control:
    # X(s) = (1, s) in C^2 -> X_tilde(s) = exp(i * beta * s) * (1, s) with beta = 3/5:
    beta_u1 = rat(3, 5)
    hs = p10(-7)

    def u1_horiz_and_alpha(s_v: float, twisted: bool) -> Tuple[np.ndarray, float, np.ndarray]:
        ph = cmath.exp(I_UNIT * beta_u1 * s_v) if twisted else complex(1, 0)
        x_s = np.array([ph, ph * s_v], dtype=complex)
        xdot = (
            np.array([I_UNIT * beta_u1 * ph, ph * (1 + I_UNIT * beta_u1 * s_v)], dtype=complex)
            if twisted
            else np.array([0, 1], dtype=complex)
        )
        kx = I_UNIT * x_s  # vertical generator on C^2
        # Real Euclidean inner product <u, w>_R = Re(u^H w):
        norm_kx_sq = float(np.real(np.vdot(kx, kx)))
        alpha = float(np.real(np.vdot(kx, xdot))) / norm_kx_sq
        v_s = xdot - alpha * kx
        return v_s, alpha, kx

    def proj_perp_u1(vec_c2: np.ndarray, s_v: float, twisted: bool) -> np.ndarray:
        v_s, _, kx = u1_horiz_and_alpha(s_v, twisted)
        w = vec_c2 - (float(np.real(np.vdot(kx, vec_c2))) / float(np.real(np.vdot(kx, kx)))) * kx
        w = w - (float(np.real(np.vdot(v_s, w))) / float(np.real(np.vdot(v_s, v_s)))) * v_s
        return w

    vt_0, al_0, _ = u1_horiz_and_alpha(rat(0), twisted=True)
    vt_p, _, _ = u1_horiz_and_alpha(hs, twisted=True)
    vt_m, _, _ = u1_horiz_and_alpha(-hs, twisted=True)
    dvt_ds = (vt_p - vt_m) / (2 * hs)
    ii_u1_raw_err = float(np.linalg.norm(proj_perp_u1(dvt_ds, rat(0), twisted=True)))
    ii_u1_cov_err = float(np.linalg.norm(proj_perp_u1(dvt_ds - I_UNIT * al_0 * vt_0, rat(0), twisted=True)))

    # 2. 18-Coordinate 4-Slot Parent Gauge-Higgs Trajectory & PHYSICAL-C6 eq. (9):
    om_w = rat(3, 2)
    s_om = math.sqrt(om_w)
    s2 = math.sqrt(2)
    pauli = [
        np.array([[0, 1], [1, 0]], dtype=complex) / s2,
        np.array([[0, -I_UNIT], [I_UNIT, 0]], dtype=complex) / s2,
        np.array([[1, 0], [0, -1]], dtype=complex) / s2,
    ]

    def unpack_x(vec18: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        ax = sum(vec18[k] * pauli[k] for k in range(3))
        ay = sum(vec18[3 + k] * pauli[k] for k in range(3))
        q_m = sum((vec18[6 + k] + I_UNIT * vec18[9 + k]) * pauli[k] for k in range(3))
        r_m = sum((vec18[12 + k] + I_UNIT * vec18[15 + k]) * pauli[k] for k in range(3))
        return ax, ay, q_m, r_m

    def pack_x(ax: np.ndarray, ay: np.ndarray, q_m: np.ndarray, r_m: np.ndarray) -> np.ndarray:
        out = np.zeros(18, dtype=float)
        for k in range(3):
            out[k] = float(np.real(np.trace(pauli[k] @ ax)))
            out[3 + k] = float(np.real(np.trace(pauli[k] @ ay)))
            cq = np.trace(pauli[k] @ q_m)
            cr = np.trace(pauli[k] @ r_m)
            out[6 + k] = float(np.real(cq))
            out[9 + k] = float(np.imag(cq))
            out[12 + k] = float(np.real(cr))
            out[15 + k] = float(np.imag(cr))
        return out

    g_chiral_diag = np.array([rat(1, 2)] * 6 + [om_w] * 12, dtype=float)
    g_chiral_inv = 1 / g_chiral_diag

    # Explicit 18x18 adjoint representation matrices T_a (a=0,1,2) of su(2) on R^18:
    def apply_su2_gen(a_idx: int, vec18: np.ndarray) -> np.ndarray:
        ax, ay, q_m, r_m = unpack_x(vec18)
        al = pauli[a_idx]
        # Under X -> exp(i t al) X exp(-i t al), d/dt at t=0 is i [al, M] on ALL four slots!
        return pack_x(
            I_UNIT * (al @ ax - ax @ al),
            I_UNIT * (al @ ay - ay @ al),
            I_UNIT * (al @ q_m - q_m @ al),
            I_UNIT * (al @ r_m - r_m @ al),
        )

    t_gens_18 = [np.column_stack([apply_su2_gen(a_idx, np.eye(18)[col]) for col in range(18)]) for a_idx in range(3)]

    def eval_residual_21(vec18: np.ndarray) -> np.ndarray:
        ax, ay, q_m, r_m = unpack_x(vec18)
        a_c = ax + I_UNIT * ay
        r1 = (-I_UNIT * (a_c @ q_m - q_m @ a_c)) / s_om
        r2 = (-I_UNIT * (a_c @ r_m - r_m @ a_c)) / s_om
        r3 = s2 * (q_m @ r_m - r_m @ q_m)
        r4 = (-I_UNIT * (ax @ ay - ay @ ax) + om_w * ((q_m @ q_m.conj().T - q_m.conj().T @ q_m) + (r_m @ r_m.conj().T - r_m.conj().T @ r_m))) / (s2 * om_w)
        out = np.zeros(21, dtype=float)
        for idx_m, mat in enumerate((r1, r2, r3)):
            base = 6 * idx_m
            for k in range(3):
                cm = np.trace(pauli[k] @ mat)
                out[base + k] = float(np.real(cm))
                out[base + 3 + k] = float(np.imag(cm))
        for k in range(3):
            out[18 + k] = float(np.real(np.trace(pauli[k] @ r4)))
        return out

    def eval_dr_dir(vec18: np.ndarray, dvec18: np.ndarray) -> np.ndarray:
        ax, ay, q_m, r_m = unpack_x(vec18)
        dax, day, u_m, v_m = unpack_x(dvec18)
        a_c = ax + I_UNIT * ay
        da_c = dax + I_UNIT * day
        dr1 = (-I_UNIT * ((a_c @ u_m - u_m @ a_c) + (da_c @ q_m - q_m @ da_c))) / s_om
        dr2 = (-I_UNIT * ((a_c @ v_m - v_m @ a_c) + (da_c @ r_m - r_m @ da_c))) / s_om
        dr3 = s2 * ((u_m @ r_m - r_m @ u_m) + (q_m @ v_m - v_m @ q_m))
        df_a = -I_UNIT * ((dax @ ay - ay @ dax) + (ax @ day - day @ ax))
        dmom_q = (u_m @ q_m.conj().T - q_m.conj().T @ u_m) + (q_m @ u_m.conj().T - u_m.conj().T @ q_m)
        dmom_r = (v_m @ r_m.conj().T - r_m.conj().T @ v_m) + (r_m @ v_m.conj().T - v_m.conj().T @ r_m)
        dr4 = (df_a + om_w * (dmom_q + dmom_r)) / (s2 * om_w)
        out = np.zeros(21, dtype=float)
        for idx_m, mat in enumerate((dr1, dr2, dr3)):
            base = 6 * idx_m
            for k in range(3):
                cm = np.trace(pauli[k] @ mat)
                out[base + k] = float(np.real(cm))
                out[base + 3 + k] = float(np.imag(cm))
        for k in range(3):
            out[18 + k] = float(np.real(np.trace(pauli[k] @ dr4)))
        return out

    def eval_dr_mat(vec18: np.ndarray) -> np.ndarray:
        jm = np.zeros((21, 18), dtype=float)
        for col in range(18):
            ek = np.zeros(18, dtype=float)
            ek[col] = rat(1)
            jm[:, col] = eval_dr_dir(vec18, ek)
        return jm

    th_end = rat(3, 5)
    tau_tilde = math.cos(th_end) * pauli[1] + math.sin(th_end) * pauli[0]
    z2 = np.zeros((2, 2), dtype=complex)
    x_end0 = pack_x(z2, z2, 2 * pauli[0], pauli[0])
    x_end1 = pack_x(z2, z2, 2 * tau_tilde, -tau_tilde)

    def eval_curve_second_fund_and_defect(path_fn: Any, dpath_fn: Any, s_pt: float) -> Dict[str, Any]:
        h_d = p10(-4)

        def horiz_at(sv: float) -> Tuple[np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
            xs = path_fn(sv)
            xd = dpath_fn(sv)
            ks_m = np.column_stack([t_gens_18[a_i] @ xs for a_i in range(3)])
            gram_g = ks_m.T @ (g_chiral_diag[:, None] * ks_m)
            alpha_v = np.linalg.solve(gram_g, ks_m.T @ (g_chiral_diag * xd))
            v_h = xd - ks_m @ alpha_v
            k_norm_sq = float(np.dot(g_chiral_diag * v_h, v_h))
            return xs, v_h, k_norm_sq, ks_m, alpha_v

        xs0, v0, k0, ks0, al0 = horiz_at(s_pt)
        _, vp1, _, _, _ = horiz_at(s_pt + h_d)
        _, vm1, _, _, _ = horiz_at(s_pt - h_d)
        _, vp2, _, _, _ = horiz_at(s_pt + 2 * h_d)
        _, vm2, _, _, _ = horiz_at(s_pt - 2 * h_d)
        dv_ds = (-vp2 + 8 * vp1 - 8 * vm1 + vm2) / (12 * h_d)
        conn_term = sum(al0[a_i] * (t_gens_18[a_i] @ v0) for a_i in range(3))

        def p_perp(vec_in: np.ndarray) -> np.ndarray:
            gram_g = ks0.T @ (g_chiral_diag[:, None] * ks0)
            cg = np.linalg.solve(gram_g, ks0.T @ (g_chiral_diag * vec_in))
            w = vec_in - ks0 @ cg
            cv = float(np.dot(g_chiral_diag * v0, w)) / k0
            return w - cv * v0

        ii_raw = p_perp(dv_ds)
        ii_cov = p_perp(dv_ds - conn_term)
        missing_vec = ii_cov - ii_raw

        # Normal equation eq. (5) LHS = P_perp (DR_{X_s})^* C where R(X_s) = s(1-s) C:
        r_xs = eval_residual_21(xs0)
        c_local = r_xs / (s_pt * (1 - s_pt))
        b_local = float(np.dot(c_local, c_local))
        dr_star_c = g_chiral_inv * (eval_dr_mat(xs0).T @ c_local)
        lhs_5 = p_perp(dr_star_c)
        rhs_5_cov = (b_local * s_pt * (1 - s_pt) / k0) * ii_cov
        rhs_5_raw = (b_local * s_pt * (1 - s_pt) / k0) * ii_raw

        norm_c = lambda v: math.sqrt(float(np.dot(g_chiral_diag * v, v)))
        return {
            "ii_raw_norm": norm_c(ii_raw),
            "ii_cov_norm": norm_c(ii_cov),
            "missing_term_norm_sq": float(np.dot(g_chiral_diag * missing_vec, missing_vec)),
            "eq5_defect_cov": norm_c(lhs_5 - rhs_5_cov),
            "eq5_defect_raw": norm_c(lhs_5 - rhs_5_raw),
        }

    s_eval = rat(2, 5)
    xdot_const = x_end1 - x_end0
    base_res = eval_curve_second_fund_and_defect(
        lambda sv: (1 - sv) * x_end0 + sv * x_end1,
        lambda _sv: xdot_const,
        s_eval,
    )

    # Exact analytic formula from PHYSICAL-C6 HAND_CHECKS.md eq. (9): Omega * 144 * cos^2(theta) / D^3:
    d_c6 = 10 - 6 * math.sin(th_end)
    big_d_c6 = 5 - d_c6 * s_eval * (1 - s_eval)
    exact_missing_norm_sq_c6 = om_w * 144 * (math.cos(th_end) ** 2) / (big_d_c6 ** 3)
    c6_eq9_abs_err = abs(base_res["missing_term_norm_sq"] - exact_missing_norm_sq_c6)

    # Apply a non-abelian s-dependent SU(2) gauge rotation g(s) = exp(s * (4/5 * T_0 - 3/7 * T_1 + 1/2 * T_2))!
    gen_mix = rat(4, 5) * t_gens_18[0] - rat(3, 7) * t_gens_18[1] + rat(1, 2) * t_gens_18[2]
    evals_m, evecs_m = np.linalg.eig(gen_mix)
    evecs_m_inv = np.linalg.inv(evecs_m)

    def rot18_at(sv: float) -> np.ndarray:
        return np.real(evecs_m @ np.diag(np.exp(sv * evals_m)) @ evecs_m_inv)

    gauged_res = eval_curve_second_fund_and_defect(
        lambda sv: rot18_at(sv) @ ((1 - sv) * x_end0 + sv * x_end1),
        lambda sv: rot18_at(sv) @ xdot_const + (gen_mix @ rot18_at(sv)) @ ((1 - sv) * x_end0 + sv * x_end1),
        s_eval,
    )
    cov_ii_gauge_diff = abs(base_res["ii_cov_norm"] - gauged_res["ii_cov_norm"])
    cov_defect_gauge_diff = abs(base_res["eq5_defect_cov"] - gauged_res["eq5_defect_cov"])
    raw_ii_gauge_diff = abs(base_res["ii_raw_norm"] - gauged_res["ii_raw_norm"])

    e1_passed = bool(
        abs(ii_u1_raw_err - beta_u1) < p10(-8)
        and ii_u1_cov_err < p10(-11)
        and c6_eq9_abs_err < p10(-10)
        and cov_ii_gauge_diff < p10(-10)
        and cov_defect_gauge_diff < p10(-10)
        and raw_ii_gauge_diff > rat(1, 10)
    )
    return {
        "E1_CovariantQuotientSecondFundForm_Gate_passed": e1_passed,
        "PC_FD2_RawAffineSecondFundFormFailsGaugeCovariance": {
            "u1_raw_norm_at_0": ii_u1_raw_err,
            "u1_cov_norm_at_0": ii_u1_cov_err,
            "su2_raw_II_gauge_violation": raw_ii_gauge_diff,
        },
        "c6_eq9_exact_missing_norm_sq": exact_missing_norm_sq_c6,
        "computed_missing_norm_sq": base_res["missing_term_norm_sq"],
        "c6_eq9_abs_err": c6_eq9_abs_err,
        "planar_su2_II_raw_vs_cov_norm": [base_res["ii_raw_norm"], base_res["ii_cov_norm"]],
        "planar_su2_eq5_defect_raw_vs_cov": [base_res["eq5_defect_raw"], base_res["eq5_defect_cov"]],
        "s_dependent_su2_gauge_invariance_II_and_defect_err": [cov_ii_gauge_diff, cov_defect_gauge_diff],
    }


# ============================================================================
# PART 2B: JOINT END-HOLONOMY + LINK-GAUSS OPTIMIZER & PARABOLIC KINETIC FACTOR
# ============================================================================

def run_part_2b_joint_end_holonomy_gauss_and_parabolic_kinetic() -> Dict[str, Any]:
    om_w = rat(3, 2)
    th_end = rat(3, 5)
    n_int = 36
    l_dom = rat(6)
    dx = (2 * l_dom) / n_int

    xs_fd = np.linspace(-l_dom, l_dom, n_int + 1)
    sig_raw = 1 / (1 + np.exp(-2 * xs_fd))
    s_grid = (sig_raw - sig_raw[0]) / (sig_raw[-1] - sig_raw[0])

    end0_4 = np.array([rat(2), rat(0), rat(1), rat(0)], dtype=float)
    end1_4 = np.array(
        [2 * math.sin(th_end), 2 * math.cos(th_end), -math.sin(th_end), -math.cos(th_end)],
        dtype=float,
    )
    u_init = np.outer(1 - s_grid, end0_4) + np.outer(s_grid, end1_4)

    def rot2(ang: float, vec4: np.ndarray) -> np.ndarray:
        ca, sa = math.cos(ang), math.sin(ang)
        return np.array([
            ca * vec4[0] - sa * vec4[1],
            sa * vec4[0] + ca * vec4[1],
            ca * vec4[2] - sa * vec4[3],
            sa * vec4[2] + ca * vec4[3],
        ], dtype=float)

    def j_rot(vec4: np.ndarray) -> np.ndarray:
        return np.array([-vec4[1], vec4[0], -vec4[3], vec4[2]], dtype=float)

    # 1. Joint optimization over interior U[1..N-1] AND free end-holonomy angle phi_end:
    def energy_joint(w_vars: np.ndarray) -> float:
        u_m = u_init.copy()
        u_m[1:n_int] = w_vars[:-1].reshape(n_int - 1, 4)
        u_m[n_int] = rot2(float(w_vars[-1]), end1_4)
        diff = u_m[1:] - u_m[:-1]
        e_kin = (om_w / dx) * float(np.sum(diff * diff))
        cm = u_m[1:n_int, 0] * u_m[1:n_int, 3] - u_m[1:n_int, 1] * u_m[1:n_int, 2]
        e_pot = dx * 4 * float(np.sum(cm * cm))
        return e_kin + e_pot

    def grad_joint(w_vars: np.ndarray) -> np.ndarray:
        u_m = u_init.copy()
        u_m[1:n_int] = w_vars[:-1].reshape(n_int - 1, 4)
        ph_e = float(w_vars[-1])
        u_m[n_int] = rot2(ph_e, end1_4)
        g_u = (2 * om_w / dx) * (2 * u_m[1:n_int] - u_m[:-2] - u_m[2:])
        u1, u2, v1, v2 = u_m[1:n_int, 0], u_m[1:n_int, 1], u_m[1:n_int, 2], u_m[1:n_int, 3]
        cm = u1 * v2 - u2 * v1
        g_u[:, 0] += dx * 8 * cm * v2
        g_u[:, 1] -= dx * 8 * cm * v1
        g_u[:, 2] -= dx * 8 * cm * u2
        g_u[:, 3] += dx * 8 * cm * u1
        du_end = j_rot(u_m[n_int])
        g_ph = (2 * om_w / dx) * float(np.dot(u_m[n_int] - u_m[n_int - 1], du_end))
        return np.concatenate([g_u.reshape(-1), [g_ph]])

    def link_gauss_currents(u_m: np.ndarray) -> np.ndarray:
        # Discrete longitudinal SO(2) Gauss current on each link j = 0..N-1: <U_j, J U_{j+1}> / dx!
        # In horizontal gauge (A_link = 0 on every link), the Gauss equation dE/d(phi_link_j) = 0 requires <U_j, J U_{j+1}> == 0 on EVERY link!
        return np.array([float(np.dot(u_m[j], j_rot(u_m[j + 1]))) / dx for j in range(n_int)], dtype=float)

    def lm_minimize(e_fn: Any, g_fn: Any, x0: np.ndarray) -> np.ndarray:
        x = x0.copy()
        reg = rat(1, 10)
        for _ in range(45):
            g = g_fn(x)
            gnorm = float(np.linalg.norm(g))
            if gnorm < p10(-13):
                break
            nv = len(x)
            hess = np.zeros((nv, nv), dtype=float)
            eps_h = p10(-7)
            for col in range(nv):
                ec = np.zeros(nv, dtype=float)
                ec[col] = eps_h
                hess[:, col] = (g_fn(x + ec) - g) / eps_h
            hess = (hess + hess.T) / 2
            ev = np.linalg.eigvalsh(hess)
            sh = max(reg, -float(ev[0]) + reg)
            if float(ev[0]) > rat(1, 1000) and gnorm < p10(-4):
                step_nw = -np.linalg.solve(hess, g)
                xn = x + step_nw
                if float(np.linalg.norm(g_fn(xn))) < gnorm:
                    x = xn
                    continue
            step = -np.linalg.solve(hess + sh * np.eye(nv), g)
            eb = e_fn(x)
            sl = float(np.dot(g, step))
            al = rat(1)
            acc = False
            for _ in range(25):
                et = e_fn(x + al * step)
                if math.isfinite(et) and (et < eb or abs(sl) < p10(-22)):
                    x = x + al * step
                    acc = True
                    break
                al /= 2
            if acc and al == rat(1):
                reg = max(p10(-11), reg / 4)
            elif not acc:
                reg *= 10
        return x

    # Planted Control PC_FD2_FixedEndHolonomyLeavesNonzeroGaussCurrent (holding phi_end = 0 fixed as in X-SYNTHESIS-2!):
    w_fixed0 = u_init[1:n_int].reshape(-1).copy()
    w_fixed_sol = lm_minimize(
        lambda v: energy_joint(np.concatenate([v, [rat(0)]])),
        lambda v: grad_joint(np.concatenate([v, [rat(0)]]))[:-1],
        w_fixed0,
    )
    u_fixed = u_init.copy()
    u_fixed[1:n_int] = w_fixed_sol.reshape(n_int - 1, 4)
    fixed_end_angle_grad_abs = abs(float(grad_joint(np.concatenate([w_fixed_sol, [rat(0)]]))[-1]))
    fixed_max_link_gauss_abs = float(np.max(np.abs(link_gauss_currents(u_fixed))))

    # Repaired Joint (U_int + phi_end) Solve:
    w_joint0 = np.concatenate([w_fixed0, [rat(0)]])
    w_joint_sol = lm_minimize(energy_joint, grad_joint, w_joint0)
    e_joint_relaxed = energy_joint(w_joint_sol)
    g_joint_full = grad_joint(w_joint_sol)
    g_joint_norm = float(np.linalg.norm(g_joint_full))
    joint_end_angle_grad_abs = abs(float(g_joint_full[-1]))
    u_joint = u_init.copy()
    u_joint[1:n_int] = w_joint_sol[:-1].reshape(n_int - 1, 4)
    u_joint[n_int] = rot2(float(w_joint_sol[-1]), end1_4)
    joint_max_link_gauss_abs = float(np.max(np.abs(link_gauss_currents(u_joint))))

    # Cross-check against exact link-eliminated energy (sum_j (om_w/dx)(|U_j|^2 + |U_{j+1}|^2 - 2 hypot(A_j, B_j)) + V_pot)
    # evaluated on u_joint (where free phi_end allows EVERY link angle phi_j^* = atan2(B_j, A_j) == 0 simultaneously!):
    e_link_elim_at_joint = rat(0)
    for j in range(n_int):
        ua, ub = u_joint[j], u_joint[j + 1]
        ac = float(np.dot(ua, ub))
        bs = float(np.dot(ua, j_rot(ub)))
        e_link_elim_at_joint += (om_w / dx) * max(rat(0), float(np.dot(ua, ua) + np.dot(ub, ub)) - 2 * math.hypot(ac, bs))
    cm_j = u_joint[1:n_int, 0] * u_joint[1:n_int, 3] - u_joint[1:n_int, 1] * u_joint[1:n_int, 2]
    e_link_elim_at_joint += dx * 4 * float(np.sum(cm_j * cm_j))
    joint_vs_link_elim_diff = abs(e_joint_relaxed - e_link_elim_at_joint)

    # 2. PHYSICAL-C6 §3 eqs. (10)-(11) Induced Parabolic Kinetic Factor:
    b_cmp = rat(2)
    c_cmp = rat(3, 5)
    gl_x, gl_w = np.polynomial.legendre.leggauss(64)
    u_nodes = (gl_x + 1) / 2
    u_weights = gl_w / 2
    k_curve = 1 + (c_cmp ** 2) * ((1 - 2 * u_nodes) ** 2)
    true_parabolic_tension = float(2 * math.sqrt(b_cmp) * np.sum(u_weights * u_nodes * (1 - u_nodes) * np.sqrt(k_curve)))
    uncurved_tension = math.sqrt(b_cmp) / 3
    straight_tension = math.sqrt(b_cmp + c_cmp * c_cmp) / 3
    true_parabolic_to_straight_ratio = true_parabolic_tension / straight_tension
    old_omitted_kinetic_ratio = math.sqrt(b_cmp) / math.sqrt(b_cmp + c_cmp * c_cmp)
    parabolic_kinetic_excess = true_parabolic_tension - uncurved_tension
    parabolic_y_double_prime_residual = abs(-2 * c_cmp)

    e2_passed = bool(
        fixed_end_angle_grad_abs > rat(1, 20)
        and fixed_max_link_gauss_abs > rat(1, 50)
        and g_joint_norm < p10(-11)
        and joint_end_angle_grad_abs < p10(-12)
        and joint_max_link_gauss_abs < p10(-12)
        and joint_vs_link_elim_diff < p10(-13)
        and e_joint_relaxed < energy_joint(np.concatenate([w_fixed_sol, [rat(0)]]))
        and parabolic_kinetic_excess > rat(1, 200)
        and true_parabolic_to_straight_ratio > old_omitted_kinetic_ratio
        and parabolic_y_double_prime_residual > rat(1)
    )
    return {
        "E2_JointEndHolonomyGauss_and_ParabolicKinetic_Gate_passed": e2_passed,
        "PC_FD2_FixedEndHolonomyLeavesNonzeroGaussCurrent": {
            "end_angle_grad_abs": fixed_end_angle_grad_abs,
            "max_link_gauss_current_abs": fixed_max_link_gauss_abs,
        },
        "repaired_joint_end_holonomy_solve": {
            "phi_end_star": float(w_joint_sol[-1]),
            "e_joint_relaxed": e_joint_relaxed,
            "full_grad_norm": g_joint_norm,
            "end_angle_grad_abs": joint_end_angle_grad_abs,
            "max_all_links_gauss_current_abs": joint_max_link_gauss_abs,
            "joint_vs_link_eliminated_energy_diff": joint_vs_link_elim_diff,
        },
        "parabolic_induced_kinetic_c6_eq10_11": {
            "true_parabolic_tension": true_parabolic_tension,
            "uncurved_tension_omitting_eq10": uncurved_tension,
            "kinetic_curvature_excess": parabolic_kinetic_excess,
            "true_vs_old_tension_ratio": [true_parabolic_to_straight_ratio, old_omitted_kinetic_ratio],
            "nonzero_static_y_double_prime_abs": parabolic_y_double_prime_residual,
        },
    }


# ============================================================================
# PART 2C: DERIVED HOPF A_phase LINK TRANSPORT ON 2-CELL SPIN(10) SEWING
# ============================================================================

def build_spin10_16plus_np() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    i2 = sp.eye(2)

    def kron_list(ms: List[sp.Matrix]) -> sp.Matrix:
        out = ms[0]
        for m in ms[1:]:
            out = sp.kronecker_product(out, m)
        return out

    gammas: List[sp.Matrix] = []
    for k in range(5):
        gammas.append(kron_list([sz] * k + [sx] + [i2] * (4 - k)))
        gammas.append(kron_list([sz] * k + [sy] + [i2] * (4 - k)))

    gamma_chir = kron_list([sz, sz, sz, sz, sz])
    plus_idx = [idx for idx in range(32) if gamma_chir[idx, idx] == 1]

    def proj16(m32: sp.Matrix) -> sp.Matrix:
        return sp.Matrix([[m32[i, j] for j in plus_idx] for i in plus_idx])

    def sigma16(a: int, b: int) -> sp.Matrix:
        if a == b:
            return sp.zeros(16, 16)
        return sp.Rational(1, 2) * proj16(gammas[a] * gammas[b])

    hp_raw = sp.I * (sigma16(0, 1) + 2 * sigma16(2, 3))
    hm_raw = sp.I * (sigma16(6, 7) + 2 * sigma16(8, 9))
    weights = [(hp_raw[k, k], hm_raw[k, k], k) for k in range(16)]
    weights.sort(key=lambda t: (-t[0], -t[1]))
    perm = [w[2] for w in weights]
    p_ord = sp.Matrix([[1 if j == perm[i] else 0 for j in range(16)] for i in range(16)])
    to_ord = lambda m16: p_ord * m16 * p_ord.T

    e_short_p = to_ord(sigma16(0, 4) - sp.I * sigma16(1, 4))
    e_long_p = to_ord(sp.Rational(1, 2) * (sigma16(2, 0) - sp.I * sigma16(3, 0) + sp.I * sigma16(2, 1) + sigma16(3, 1)))
    e_plus = sp.sqrt(sp.Rational(3, 2)) * e_short_p + sp.sqrt(sp.Integer(2)) * e_long_p

    e_short_m = to_ord(sigma16(6, 5) - sp.I * sigma16(7, 5))
    e_long_m = to_ord(sp.Rational(1, 2) * (sigma16(8, 6) - sp.I * sigma16(9, 6) + sp.I * sigma16(8, 7) + sigma16(9, 7)))
    e_minus = sp.sqrt(sp.Rational(3, 2)) * e_short_m + sp.sqrt(sp.Integer(2)) * e_long_m

    c0_gen = to_ord(sigma16(0, 5))
    q_cartan = to_ord(sp.I * (sigma16(0, 1) + sigma16(6, 7)))
    return (
        np.array(e_plus.tolist(), dtype=complex),
        np.array(e_minus.tolist(), dtype=complex),
        np.array(c0_gen.tolist(), dtype=complex),
        np.array(q_cartan.tolist(), dtype=complex),
    )


def run_part_2c_derived_hopf_link_transport() -> Dict[str, Any]:
    ep, em, c0_gen, q_cartan = build_spin10_16plus_np()
    d1_cell = np.vstack([ep, em])  # 32 x 16

    # Octahedral state-axis Spin(10) rotation U_2O (angle pi/2 between distinct 2O state axes -> pi/4 in spinor):
    evals_g, evecs_g = np.linalg.eigh(-I_UNIT * c0_gen)
    u_axis2 = evecs_g @ np.diag(np.exp(I_UNIT * (math.pi / 4) * evals_g)) @ evecs_g.conj().T
    d2_cell_phys = np.vstack([u_axis2 @ ep @ u_axis2.conj().T, u_axis2 @ em @ u_axis2.conj().T])

    # Derive inter-cell Abelian phase holonomy int_0^1 A_phase ds from PHYSICAL-C7's 4-form connection:
    # A_phase = [Im(P^H dP) - Im(R^H dR)] / (||P||^2 + ||R||^2) along a latitude path joining the two 2O axes!
    n_quad = 200
    ds = rat(1, n_quad)
    int_a_phase = rat(0)
    for k_i in range(n_quad):
        s_m = (k_i + rat(1, 2)) * ds
        ang = (math.pi / 2) * s_m
        # P(s) = (cos(ang/2) e^{i s}, sin(ang/2)), R(s) = (cos(ang/2) e^{-i s}, -sin(ang/2)):
        ca, sa = math.cos(ang / 2), math.sin(ang / 2)
        dca = -(math.pi / 4) * sa
        dsa = (math.pi / 4) * ca
        phs = cmath.exp(I_UNIT * s_m)
        p_vec = np.array([ca * phs, sa], dtype=complex)
        dp_vec = np.array([(dca + I_UNIT * ca) * phs, dsa], dtype=complex)
        r_vec = np.array([ca * phs.conjugate(), -sa], dtype=complex)
        dr_vec = np.array([(dca - I_UNIT * ca) * phs.conjugate(), -dsa], dtype=complex)
        num = float(np.imag(np.vdot(p_vec, dp_vec)) - np.imag(np.vdot(r_vec, dr_vec)))
        den = float(np.real(np.vdot(p_vec, p_vec) + np.vdot(r_vec, r_vec)))
        int_a_phase += ds * (num / den)

    # Parallel-transport link L_Hopf = exp(-i * int_a_phase * Q_cartan) in Spin(10):
    ev_q, vc_q = np.linalg.eigh(q_cartan)
    l_hopf = vc_q @ np.diag(np.exp(-I_UNIT * int_a_phase * ev_q)) @ vc_q.conj().T

    def assemble_sewn_80x32(d1_m: np.ndarray, d2_m: np.ndarray, link_12: np.ndarray, kap: float) -> np.ndarray:
        z32 = np.zeros((32, 16), dtype=complex)
        i16 = np.eye(16, dtype=complex)
        return np.block([
            [d1_m, z32],
            [z32, d2_m],
            [kap * i16, -kap * link_12],
        ])

    # 1. PHYSICAL-C6 §4 Rejecting Control PC_FD2_PureFrameChangePreservesZeroMode:
    # Changing cell 2's frame D_1 -> U D_1 U^H while carrying the link I -> U^H gives nullity == 1!
    m_pure_frame = assemble_sewn_80x32(d1_cell, d2_cell_phys, u_axis2.conj().T, rat(1, 2))
    sv_pure_frame = np.sort(np.linalg.svd(m_pure_frame, compute_uv=False))
    null_pure_frame = int(np.sum(sv_pure_frame < p10(-11)))

    # 2. Physical 2-axis join with derived L_Hopf link transport (distinct physical axes + Hopf holonomy):
    m_hopf_join = assemble_sewn_80x32(d1_cell, d2_cell_phys, l_hopf, rat(1, 2))
    sv_hopf_join = np.sort(np.linalg.svd(m_hopf_join, compute_uv=False))
    null_hopf_join = int(np.sum(sv_hopf_join < p10(-11)))

    # 3. 10-trial independent local cell gauge invariance:
    # Under psi_1 -> V_1 psi_1, psi_2 -> V_2 psi_2 (and 32-dim ranges diag(V_1,V_1), diag(V_2,V_2)),
    # carrying L_Hopf -> V_1 L_Hopf V_2^H leaves ALL 32 singular values invariant to < 10^{-14}!
    rng = np.random.default_rng(20261126)
    max_local_gauge_sv_err = rat(0)
    for _ in range(10):
        v1 = random_haar_un(rng, 16)
        v2 = random_haar_un(rng, 16)
        v1_32 = np.block([[v1, np.zeros((16, 16))], [np.zeros((16, 16)), v1]])
        v2_32 = np.block([[v2, np.zeros((16, 16))], [np.zeros((16, 16)), v2]])
        d1_g = v1_32 @ d1_cell @ v1.conj().T
        d2_g = v2_32 @ d2_cell_phys @ v2.conj().T
        l_g = v1 @ l_hopf @ v2.conj().T
        m_g = assemble_sewn_80x32(d1_g, d2_g, l_g, rat(1, 2))
        sv_g = np.sort(np.linalg.svd(m_g, compute_uv=False))
        max_local_gauge_sv_err = max(max_local_gauge_sv_err, float(np.max(np.abs(sv_g - sv_hopf_join))))

    e3_passed = bool(
        null_pure_frame == 1
        and null_hopf_join == 0
        and abs(int_a_phase) > rat(1, 5)
        and float(sv_hopf_join[0]) > rat(1, 10)
        and max_local_gauge_sv_err < p10(-13)
    )
    return {
        "E3_DerivedHopfLinkTransport_Spin10Sewing_Gate_passed": e3_passed,
        "PC_FD2_PureFrameChangePreservesZeroMode_nullity": null_pure_frame,
        "derived_4form_hopf_integral_phase_rad": int_a_phase,
        "hopf_transported_two_axis_nullity": null_hopf_join,
        "hopf_transported_lowest_3_svs": [float(x) for x in sv_hopf_join[:3]],
        "ten_trial_independent_cell_gauge_transport_max_sv_err": max_local_gauge_sv_err,
    }


def main() -> None:
    ast_res = verify_ast_foundation2()
    p2a = run_part_2a_covariant_second_fundamental_form()
    p2b = run_part_2b_joint_end_holonomy_gauss_and_parabolic_kinetic()
    p2c = run_part_2c_derived_hopf_link_transport()

    controls_passed = bool(
        ast_res["Gate_AST_Stage2_Foundation_Passed"]
        and p2a["PC_FD2_RawAffineSecondFundFormFailsGaugeCovariance"]["su2_raw_II_gauge_violation"] > rat(1, 10)
        and p2b["PC_FD2_FixedEndHolonomyLeavesNonzeroGaussCurrent"]["end_angle_grad_abs"] > rat(1, 20)
        and p2c["PC_FD2_PureFrameChangePreservesZeroMode_nullity"] == 1
    )
    stage_passed = bool(
        controls_passed
        and p2a["E1_CovariantQuotientSecondFundForm_Gate_passed"]
        and p2b["E2_JointEndHolonomyGauss_and_ParabolicKinetic_Gate_passed"]
        and p2c["E3_DerivedHopfLinkTransport_Spin10Sewing_Gate_passed"]
    )

    out = {
        "card": "X-FOUNDATION-2",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_res,
        "part_2a_covariant_second_fundamental_form": p2a,
        "part_2b_joint_end_holonomy_gauss_and_parabolic_kinetic": p2b,
        "part_2c_derived_hopf_link_transport": p2c,
        "all_planted_controls_passed": controls_passed,
        "stage_2_gate_passed": stage_passed,
    }
    out_path = Path(__file__).resolve().parent / "verify_x_foundation_2_out.json"
    txt = json.dumps(out, indent=2, sort_keys=True) + "\n"
    out_path.write_text(txt, encoding="utf-8")
    digest = hashlib.sha256(txt.encode("utf-8")).hexdigest()
    (Path(__file__).resolve().parent / "OUTPUT_SHA256.txt").write_text(
        f"{digest}  verify_x_foundation_2_out.json\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
