#!/usr/bin/env python3
r"""
Standalone Zero-Import Verifier for Card X-SYNTHESIS-1:
  Part 1A (PHYSICAL-C5 C5-02): Spectral Newton-Fourier solution of the constant-curvature hyperbolic
           Liouville uniformization PDE Delta ln Omega_hyp = Omega_hyp^2 / ell^2 on E_{tau = i sqrt(3)} \ {0}
           across M_hyp in {16, 24, 32} with cusp-Robin matching w(0) = 0, interior curvature check,
           and Gauss-Bonnet area 2*pi*ell^2 closure via the exact analytic cusp-area tail delta_A(T).
  Part 1B (PHYSICAL-C5 C5-02 & eq. 7): Smooth radial partition-of-unity + analytic tail evaluation of
           hyperbolic (|lambda_+|/e_Q, |lambda_-|/e_Q, |lambda_+|/|lambda_-|) across n_gl in {16, 24, 32},
           plus verification of the metric-variation sensitivity identity eq. (7).
  Part 1C (PHYSICAL-C5 C5-04): Joint multi-grid refinement of physical Omega_hyp^{-3} harmonic Grams
           (n_gl in {16, 24, 32}) and Bloch-Fourier Dolbeault Green inverses (M in {16, 24, 32}) for
           colour-triplet sigma_*^hyp > 0, L^2-projection vs analytic residue agreement, symbolic
           connecting-map exactness, and enforced good-sign |dbar(K_* alpha)| gate predicate.

Empirical Firewall: 0 of 19 (0 float literals and 0 complex literals module-wide).
"""

from __future__ import annotations

import ast
import cmath
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np
import sympy as sp


# ============================================================================
# SECTION 0: AST SOURCE AUDIT (ZERO IMPORTS, ZERO FLOAT & COMPLEX LITERALS)
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
    "sympy",
    "typing",
}


def verify_ast_synthesis1() -> Dict[str, Any]:
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
        "Gate_AST_Stage1_Synthesis_Passed": passed,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "float_literals_module_wide": float_lits,
        "complex_literals_module_wide": complex_lits,
        "zero_imports_from_repo_or_reports": len(disallowed) == 0,
    }


# ============================================================================
# SECTION 1: PART 1A — HYPERBOLIC LIOUVILLE UNIFORMIZATION & GAUSS-BONNET TAIL
# ============================================================================

ELL_VAL = 3 / 2
Y_TAU = math.sqrt(3)
Q_TAU = math.exp(-math.pi * Y_TAU)
I_UNIT = complex(0, 1)


def th1_and_d1_c(z_v: complex) -> Tuple[complex, complex]:
    s0 = complex(0, 0)
    s1 = complex(0, 0)
    for n in range(10):
        sgn = -1 if (n % 2 == 1) else 1
        pw = ((2 * n + 1) ** 2) / 4
        qn = sgn * (Q_TAU ** pw)
        k = (2 * n + 1) * math.pi
        ang = k * z_v
        s0 += 2 * qn * cmath.sin(ang)
        s1 += 2 * qn * k * cmath.cos(ang)
    return s0, s1


def th3_c(z_v: complex) -> complex:
    acc = complex(1, 0)
    for n in range(1, 10):
        acc += 2 * (Q_TAU ** (n * n)) * cmath.cos(2 * n * math.pi * z_v)
    return acc


TH1_P0 = abs(th1_and_d1_c(complex(0, 0))[1])
TH3_0 = th3_c(complex(0, 0)).real


def seed_liouville_fields(x_v: float, y_v: float, bc_val: float) -> Tuple[float, float, float]:
    r"""
    Smooth real-analytic cusp seed Omega_seed(z; b_c) = ell / [R(z) * (b_c + (1/2) ln(e^2 + R(z)^{-2}))]
    with zero |ln R| branch jump anywhere on E_tau \ {0}.
    Returns (Omega_seed, Delta ln Omega_seed, F_rhs = Delta ln Omega_seed - Omega_seed^2 / ell^2).
    """
    t0_v, t1_v = th1_and_d1_c(complex(x_v, y_v))
    u = -math.pi * (y_v * y_v) / Y_TAU + math.log(abs(t0_v) / TH1_P0)
    g = t1_v / t0_v
    ux = g.real
    uy = -g.imag - 2 * math.pi * y_v / Y_TAU
    grad_u_sq = ux * ux + uy * uy
    lap_u = -2 * math.pi / Y_TAU

    if -2 * u > 24:
        s_val = bc_val - u + math.exp(2 + 2 * u) / 2
    else:
        s_val = bc_val + math.log(math.exp(2) + math.exp(-2 * u)) / 2
    p_sig = 1 / (1 + math.exp(min(60, 2 + 2 * u)))
    sp_val = -p_sig
    spp_val = 2 * p_sig * (1 - p_sig)

    om_seed = ELL_VAL * math.exp(-u) / s_val
    lap_ln = -(1 + sp_val / s_val) * lap_u - (spp_val / s_val - (sp_val * sp_val) / (s_val * s_val)) * grad_u_sq
    rhs_f = lap_ln - (om_seed * om_seed) / (ELL_VAL * ELL_VAL)
    return om_seed, lap_ln, rhs_f


class HyperbolicMetricTorus:
    """Spectral periodic + cusp-Robin matched solution Omega_hyp(z) = Omega_seed(z; b_c^*) exp(w(z))."""

    def __init__(self, m_grid: int) -> None:
        self.m = m_grid
        us = -(1 / 2) + (np.arange(m_grid) + (1 / 2)) / m_grid
        self.us = us
        self.xs = us
        self.ys = us * Y_TAU
        freqs = np.fft.fftfreq(m_grid) * m_grid
        self.freqs = freqs
        idx = np.arange(m_grid)
        f_mat = np.exp(-2 * I_UNIT * math.pi * np.outer(freqs, idx) / m_grid) / math.sqrt(m_grid)
        d2x = np.real(f_mat.conj().T @ np.diag(-((2 * math.pi * freqs) ** 2)) @ f_mat)
        d2y = np.real(f_mat.conj().T @ np.diag(-((2 * math.pi * freqs / Y_TAU) ** 2)) @ f_mat)
        lap = np.kron(d2x, np.eye(m_grid)) + np.kron(np.eye(m_grid), d2y)

        # Trigonometric evaluation weights at origin (u1=0, u2=0):
        # Since us[p] = -1/2 + (p + 1/2)/M, tilde_w(0, 0) via DFT on midpoint grid:
        # w(u1, u2) = (1/M^2) sum_{kx, ky} hat_w[kx, ky] exp(2 pi i (kx u1 + ky u2)), where
        # hat_w[kx, ky] = sum_{p, q} w[p, q] exp(-2 pi i (kx us[p] + ky us[q])).
        # At (u1, u2) = (0, 0), w_trig(0, 0) = (1/M^2) sum_{p, q} w[p, q] * W0(p) * W0(q)!
        w0_1d = np.real(np.sum(np.exp(-2 * I_UNIT * math.pi * np.outer(freqs, us)), axis=0)) / m_grid
        w0_2d = np.outer(w0_1d, w0_1d).reshape(m_grid * m_grid)

        def solve_for_bc(bc_v: float) -> Tuple[float, np.ndarray, float]:
            om_s = np.zeros(m_grid * m_grid)
            rhs = np.zeros(m_grid * m_grid)
            for ix in range(m_grid):
                for iy in range(m_grid):
                    ov, _, rv = seed_liouville_fields(float(self.xs[ix]), float(self.ys[iy]), bc_v)
                    om_s[ix * m_grid + iy] = ov
                    rhs[ix * m_grid + iy] = rv
            w_vec = np.zeros(m_grid * m_grid)
            pot0 = (om_s ** 2) / (ELL_VAL * ELL_VAL)
            max_f = 1
            for _ in range(14):
                e2w = np.exp(2 * w_vec)
                f_res = -(lap @ w_vec) + pot0 * (e2w - 1) - rhs
                max_f = float(np.max(np.abs(f_res)))
                if max_f < (10 ** (-13)):
                    break
                w_vec += np.linalg.solve(-lap + np.diag(2 * pot0 * e2w), -f_res)
            return float(np.dot(w0_2d, w_vec)), w_vec.reshape(m_grid, m_grid), max_f

        b0 = 3 / 5
        b1 = 6 / 5
        f0, _, _ = solve_for_bc(b0)
        f1, w_sol, max_r = solve_for_bc(b1)
        for _ in range(10):
            if abs(f1 - f0) < (10 ** (-14)):
                break
            b2 = b1 - f1 * (b1 - b0) / (f1 - f0)
            f2, w_sol, max_r = solve_for_bc(b2)
            b0, f0 = b1, f1
            b1, f1 = b2, f2
            if abs(f1) < (10 ** (-12)):
                break

        self.bc_star = b1
        self.w_grid = w_sol
        self.pde_max_res = max_r
        self.w_origin_err = abs(f1)

        # Precompute 2D Fourier coefficients of w_grid on midpoint coordinates:
        e_m1 = np.exp(-2 * I_UNIT * math.pi * np.outer(freqs, us))
        self.w_hat = (e_m1 @ w_sol @ e_m1.T) / (m_grid * m_grid)

    def eval_w(self, x_v: float, y_v: float) -> float:
        u1 = x_v
        u2 = y_v / Y_TAU
        ex = np.exp(2 * I_UNIT * math.pi * self.freqs * u1)
        ey = np.exp(2 * I_UNIT * math.pi * self.freqs * u2)
        return float(np.real(ex @ self.w_hat @ ey))

    def omega(self, z_v: complex) -> float:
        om_s, _, _ = seed_liouville_fields(z_v.real, z_v.imag, self.bc_star)
        return om_s * math.exp(self.eval_w(z_v.real, z_v.imag))


def chi_cusp_smooth(r_v: float, r_in: float, r_out: float) -> float:
    """C^infty radial partition weight: 1 for r <= r_in, 0 for r >= r_out."""
    if r_v <= r_in:
        return 1
    if r_v >= r_out:
        return 0
    t = (r_v - r_in) / (r_out - r_in)
    e1 = math.exp(-1 / t)
    e2 = math.exp(-1 / (1 - t))
    return e2 / (e1 + e2)


def integrate_smooth_partition_torus(fn: Callable[[complex], complex], n_gl: int, t_cut: float = 18) -> complex:
    """
    Integrates a periodic function fn(z) over E_{tau = i sqrt(3)} with ZERO sharp-disk discontinuity
    using a smooth C^infty radial partition of unity chi_cusp(|z|) on [r_in=1/8, r_out=1/4].
    """
    gl_x, gl_w = np.polynomial.legendre.leggauss(n_gl)
    r_in = 1 / 8
    r_out = 1 / 4
    acc = complex(0, 0)

    # 1. Cusp polar region r = r_out * exp(-t), t in [0, t_cut], theta in [0, 2*pi]:
    for it in range(n_gl):
        tv = (t_cut / 2) * (float(gl_x[it]) + 1)
        wt = (t_cut / 2) * float(gl_w[it])
        rv = r_out * math.exp(-tv)
        ch = chi_cusp_smooth(rv, r_in, r_out)
        if ch > 0:
            for ith in range(n_gl):
                thv = math.pi * (float(gl_x[ith]) + 1)
                wth = math.pi * float(gl_w[ith])
                zv = rv * cmath.exp(I_UNIT * thv)
                acc += (rv * rv) * wt * wth * ch * fn(zv)

    # 2. Smooth exterior torus [-1/2, 1/2] x [-y_tau/2, y_tau/2] weighted by (1 - chi_cusp(|z|)):
    # Use 2 * n_gl periodic midpoint / Gauss nodes across [-1/2, 1/2] x [-y_tau/2, y_tau/2]:
    m_ext = 2 * n_gl
    du = 1 / m_ext
    dy = Y_TAU / m_ext
    for ix in range(m_ext):
        xv = -(1 / 2) + (ix + (1 / 2)) * du
        for iy in range(m_ext):
            yv = -(Y_TAU / 2) + (iy + (1 / 2)) * dy
            rv = math.hypot(xv, yv)
            one_minus_ch = 1 - chi_cusp_smooth(rv, r_in, r_out)
            if one_minus_ch > 0:
                acc += (du * dy) * one_minus_ch * fn(complex(xv, yv))
    return acc


def run_part_1a_and_1b_hyperbolic_metric_and_lambdas() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[int, HyperbolicMetricTorus]]:
    hyp_models = {m_v: HyperbolicMetricTorus(m_v) for m_v in (16, 24, 32)}
    hm32 = hyp_models[32]

    # Check interior Gaussian curvature K_Gauss(z_test) = -(Delta ln Omega_hyp) / Omega_hyp^2 vs -1 / ell^2:
    z_test = complex(19 / 100, -23 / 100)
    h_fd = 1 / 2000
    ln0 = math.log(hm32.omega(z_test))
    lap_ln_hyp = (
        math.log(hm32.omega(z_test + h_fd))
        + math.log(hm32.omega(z_test - h_fd))
        + math.log(hm32.omega(z_test + I_UNIT * h_fd))
        + math.log(hm32.omega(z_test - I_UNIT * h_fd))
        - 4 * ln0
    ) / (h_fd * h_fd)
    k_gauss_hyp = -lap_ln_hyp / (hm32.omega(z_test) ** 2)
    target_k = -1 / (ELL_VAL * ELL_VAL)
    curv_rel_err_hyp = abs(k_gauss_hyp - target_k) / abs(target_k)

    # Planted control PC_SY1_NonHyperbolicSeedCurvatureError: curvature error of uncorrected seed (w = 0, b_c = 0):
    om_s0, lap_s0, _ = seed_liouville_fields(z_test.real, z_test.imag, 0)
    k_gauss_seed = -lap_s0 / (om_s0 * om_s0)
    pc_seed_curv_rel_err = abs(k_gauss_seed - target_k) / abs(target_k)

    # Gauss-Bonnet area 2 * pi * ell^2 check WITH vs WITHOUT physical's analytic cusp-area tail delta_A(T):
    t_cut = 18
    r_out = 1 / 4
    area_gb_exact = 2 * math.pi * (ELL_VAL * ELL_VAL)
    area_num_trunc = integrate_smooth_partition_torus(lambda z: hm32.omega(z) ** 2, 32, t_cut).real
    delta_area_tail = (2 * math.pi * (ELL_VAL * ELL_VAL)) / (t_cut + math.log(1 / r_out) + hm32.bc_star)
    area_with_tail = area_num_trunc + delta_area_tail
    gb_rel_err_with_tail = abs(area_with_tail - area_gb_exact) / area_gb_exact
    pc_omitted_tail_gb_rel_err = abs(area_num_trunc - area_gb_exact) / area_gb_exact

    bc_conv_24_32 = abs(hyp_models[32].bc_star - hyp_models[24].bc_star) / abs(hyp_models[32].bc_star)

    e1_passed = bool(
        max(hyp_models[m_v].pde_max_res for m_v in (16, 24, 32)) < (10 ** (-12))
        and hm32.w_origin_err < (10 ** (-11))
        and bc_conv_24_32 < Fraction(1, 200)
        and curv_rel_err_hyp < Fraction(5, 1000)
        and pc_seed_curv_rel_err > Fraction(1, 5)
        and gb_rel_err_with_tail < Fraction(5, 1000)
        and pc_omitted_tail_gb_rel_err > Fraction(4, 100)
    )

    part_1a = {
        "E1_HyperbolicLiouville_and_GaussBonnetTail_Gate_passed": e1_passed,
        "bc_robin_star_16_24_32": [hyp_models[m_v].bc_star for m_v in (16, 24, 32)],
        "pde_max_res_16_24_32": [hyp_models[m_v].pde_max_res for m_v in (16, 24, 32)],
        "interior_curvature_rel_err_hyp": curv_rel_err_hyp,
        "PC_SY1_NonHyperbolicSeedCurvatureError_rel": pc_seed_curv_rel_err,
        "gauss_bonnet_exact_2pi_ell2": area_gb_exact,
        "area_truncated_T18_no_tail": area_num_trunc,
        "analytic_cusp_area_tail_T18": delta_area_tail,
        "area_completed_with_tail": area_with_tail,
        "gauss_bonnet_rel_err_with_tail": gb_rel_err_with_tail,
        "PC_SY1_OmittedCuspAreaTailMissesGaussBonnet_rel_err": pc_omitted_tail_gb_rel_err,
    }

    # Part 1B: Evaluate hyperbolic (|lambda_+|/e_Q, |lambda_-|/e_Q, |lambda_+|/|lambda_-|) across n_gl in {16, 24, 32}
    # WITH the exact analytic cusp-area tail delta_A(T) included in A = int Omega^2!
    def eval_lambdas_on_metric(hm: HyperbolicMetricTorus, n_gl: int, eps_def: float = 0, const_def: bool = False) -> Tuple[float, float, Dict[str, float]]:
        def om_fn(zv: complex) -> float:
            base = hm.omega(zv)
            if eps_def == 0:
                return base
            if const_def:
                return base * math.exp(eps_def)
            # Smooth periodic deformation f(z) = cos(2 pi x) cos(2 pi y / y_tau) * (1 - chi_cusp(|z|)) vanishing near cusp!
            rv = abs(zv)
            f_z = math.cos(2 * math.pi * zv.real) * math.cos(2 * math.pi * zv.imag / Y_TAU) * (1 - chi_cusp_smooth(rv, 1 / 8, 1 / 4))
            return base * math.exp(eps_def * f_z)

        a_trunc = integrate_smooth_partition_torus(lambda z: om_fn(z) ** 2, n_gl, t_cut).real
        tail_scale = math.exp(2 * eps_def) if const_def else 1
        a_tot = a_trunc + tail_scale * (2 * math.pi * (ELL_VAL * ELL_VAL)) / (t_cut + math.log(1 / r_out) + hm.bc_star)
        j_tot = integrate_smooth_partition_torus(lambda z: om_fn(z), n_gl, t_cut).real
        kp3 = integrate_smooth_partition_torus(lambda z: om_fn(z) ** (-3), n_gl, t_cut).real
        kp2 = integrate_smooth_partition_torus(lambda z: om_fn(z) ** (-2), n_gl, t_cut).real

        def nm_sq(zv: complex) -> float:
            t0_z, _ = th1_and_d1_c(zv)
            return abs(th3_c(zv) / t0_z) ** 2

        km3 = integrate_smooth_partition_torus(lambda z: nm_sq(z) * (om_fn(z) ** (-3)), n_gl, t_cut).real
        km2 = integrate_smooth_partition_torus(lambda z: nm_sq(z) * (om_fn(z) ** (-2)), n_gl, t_cut).real

        lp = math.sqrt(2 * a_tot * kp3 / (j_tot * kp2))
        lm = math.sqrt(2 * a_tot * km3 / (j_tot * km2))
        return lp, lm, {"A": a_tot, "J": j_tot, "Kp3": kp3, "Kp2": kp2, "Km3": km3, "Km2": km2}

    lp_16, lm_16, _ = eval_lambdas_on_metric(hyp_models[16], 16)
    lp_24, lm_24, _ = eval_lambdas_on_metric(hyp_models[24], 24)
    lp_32, lm_32, ints_32 = eval_lambdas_on_metric(hm32, 32)

    conv_lp_24_32 = abs(lp_32 - lp_24) / lp_32
    conv_lm_24_32 = abs(lm_32 - lm_24) / lm_32
    ratio_pm_32 = lp_32 / lm_32

    # Verify physical's eq. (7) metric-variation sensitivity identity:
    # (a) Constant rescaling f = 1: exact cancellation 2 - 1 - 3 + 2 == 0!
    lp_c_pos, _, _ = eval_lambdas_on_metric(hm32, 24, 1 / 10, True)
    const_rescale_diff = abs(lp_c_pos - lp_24)
    # Wait: compare at SAME hm32 and n_gl=24:
    lp_base24, _, ints_b24 = eval_lambdas_on_metric(hm32, 24, 0, True)
    const_rescale_exact_err = abs(lp_c_pos - lp_base24)

    # (b) Non-constant smooth deformation f(z): compare central FD d ln(lp)/d eps|_0 against eq. (7) weighted averages!
    eps_v = 1 / 10000
    lp_ep, _, _ = eval_lambdas_on_metric(hm32, 24, eps_v, False)
    lp_em, _, _ = eval_lambdas_on_metric(hm32, 24, -eps_v, False)
    dln_fd = ( math.log(lp_ep) - math.log(lp_em) ) / (2 * eps_v)

    def f_shape(zv: complex) -> float:
        rv = abs(zv)
        return math.cos(2 * math.pi * zv.real) * math.cos(2 * math.pi * zv.imag / Y_TAU) * (1 - chi_cusp_smooth(rv, 1 / 8, 1 / 4))

    avg_om2 = integrate_smooth_partition_torus(lambda z: f_shape(z) * (hm32.omega(z) ** 2), 24, t_cut).real / ints_b24["A"]
    avg_om1 = integrate_smooth_partition_torus(lambda z: f_shape(z) * hm32.omega(z), 24, t_cut).real / ints_b24["J"]
    avg_kp3 = integrate_smooth_partition_torus(lambda z: f_shape(z) * (hm32.omega(z) ** (-3)), 24, t_cut).real / ints_b24["Kp3"]
    avg_kp2 = integrate_smooth_partition_torus(lambda z: f_shape(z) * (hm32.omega(z) ** (-2)), 24, t_cut).real / ints_b24["Kp2"]
    dln_eq7 = (2 * avg_om2 - avg_om1 - 3 * avg_kp3 + 2 * avg_kp2) / 2
    eq7_err = abs(dln_fd - dln_eq7)

    e2_passed = bool(
        conv_lp_24_32 < Fraction(2, 1000)
        and conv_lm_24_32 < Fraction(2, 1000)
        and ratio_pm_32 > 1
        and const_rescale_exact_err < (10 ** (-14))
        and abs(dln_eq7) > (10 ** (-4))
        and eq7_err < (10 ** (-9))
    )

    part_1b = {
        "E2_HyperbolicLightCubic_and_MetricSensitivity_Gate_passed": e2_passed,
        "lambda_plus_over_eQ_16_24_32": [lp_16, lp_24, lp_32],
        "lambda_minus_over_eQ_16_24_32": [lm_16, lm_24, lm_32],
        "lambda_plus_over_lambda_minus_hyp_32": ratio_pm_32,
        "rel_conv_24_vs_32_plus_minus": [conv_lp_24_32, conv_lm_24_32],
        "const_rescaling_invariance_err": const_rescale_exact_err,
        "eq7_nonconst_dln_analytic_vs_fd": [dln_eq7, dln_fd],
        "eq7_sensitivity_identity_abs_err": eq7_err,
    }
    return part_1a, part_1b, hyp_models


# ============================================================================
# SECTION 2: PART 1C — MULTI-GRID GRAM + FOURIER SIGMA_*^HYP & DBAR PREDICATE
# ============================================================================

def run_part_1c_refined_sigma_star_and_dbar_gate(hyp_models: Dict[int, HyperbolicMetricTorus]) -> Dict[str, Any]:
    # 1. Symbolic verification of exactness of 0 -> Abar(p) --(g0, g1)--> Bbar + Cbar --(-g1, g0)--> Dbar(-p) -> 0
    #    at every point (where g0, g1 have NO common zero, i.e., |g0|^2 + |g1|^2 > 0):
    g0_s, g1_s = sp.symbols("g0_s g1_s")
    m_in = sp.Matrix([[g0_s], [g1_s]])
    m_out = sp.Matrix([[-g1_s, g0_s]])
    seq_comp_zero = (m_out * m_in) == sp.zeros(1, 1)
    # Exactness when (g0_s, g1_s) != (0, 0): homotopy (g0_bar / N, g1_bar / N) shows ker(m_out) == im(m_in) of dim 1!
    g0b, g1b = sp.symbols("g0b g1b")
    norm2 = g0_s * g0b + g1_s * g1b
    proj_im = (m_in * sp.Matrix([[g0b, g1b]])) / norm2
    proj_ker = sp.eye(2) - (sp.Matrix([[-g1b], [g0b]]) * m_out) / norm2
    exact_id = sp.simplify(proj_im - proj_ker) == sp.zeros(2, 2)

    # 2. Joint refinement across (n_gl, M_fourier) in {(16, 16), (24, 24), (32, 32)} on the hyperbolic metric!
    tau_c = I_UNIT * Y_TAU
    bA = (-1 / 3, 0)
    bD = (5 / 6, 1 / 2)
    th1_wA, _ = th1_and_d1_c(bA[0] * tau_c - bA[1])
    th1_wD, _ = th1_and_d1_c(bD[0] * tau_c - bD[1])

    def ks_pair_c(zv: complex, b1: float, b2: float, th1_w: complex) -> Tuple[complex, complex]:
        wv = b1 * tau_c - b2
        t1z, dt1z = th1_and_d1_c(zv)
        t1zw, dt1zw = th1_and_d1_c(zv + wv)
        kv = (TH1_P0 / th1_w) * cmath.exp(2 * I_UNIT * math.pi * b1 * zv) * (t1zw / t1z)
        dkv = kv * (2 * I_UNIT * math.pi * b1 + (dt1zw / t1zw) - (dt1z / t1z))
        return kv, dkv

    def gs_upper_2x2_np(gram: np.ndarray) -> np.ndarray:
        g00 = float(np.real(gram[0, 0]))
        g01 = complex(gram[0, 1])
        g11 = float(np.real(gram[1, 1]))
        n0 = math.sqrt(g00)
        c = -g01 / g00
        n1 = math.sqrt(g11 - (abs(g01) ** 2) / g00)
        return np.array([[1 / n0, c / n1], [0, 1 / n1]], dtype=complex)

    sig = 3 / 16
    sig2 = sig * sig
    sig4 = sig2 * sig2

    def alpha_gauss_c(zv: complex, c0: complex, c1: complex) -> complex:
        u2 = zv.imag / Y_TAU
        n0 = math.floor(u2 + (1 / 2))
        u2_r = u2 - n0
        u1 = zv.real
        m0 = math.floor(u1 + (1 / 2))
        u1_r = u1 - m0
        z0 = complex(u1_r, u2_r * Y_TAU)
        base_bloch = cmath.exp(2 * I_UNIT * math.pi * (1 / 3) * m0)
        acc = complex(0, 0)
        for dm in range(-3, 4):
            ph = cmath.exp(2 * I_UNIT * math.pi * (1 / 3) * dm)
            for dn in range(-3, 4):
                w = z0 - dm - dn * tau_c
                r2 = w.real * w.real + w.imag * w.imag
                if r2 < 6:
                    acc += ph * (-(c0 + c1 * w) * w * r2 / sig4) * math.exp(-r2 / sig2)
        return base_bloch * acc

    def eval_joint_level(lvl: int) -> Dict[str, Any]:
        hm = hyp_models[lvl]
        nf0_sq = integrate_smooth_partition_torus(lambda z: hm.omega(z) ** (-2), lvl).real
        nf1_sq = integrate_smooth_partition_torus(
            lambda z: (abs(th3_c(z) / th1_and_d1_c(z)[0]) ** 2) * (hm.omega(z) ** (-2)), lvl
        ).real
        kap0 = 1 / math.sqrt(nf0_sq)
        kap1 = 1 / math.sqrt(nf1_sq)

        ga = np.zeros((2, 2), dtype=complex)
        gd = np.zeros((2, 2), dtype=complex)
        for j in range(2):
            for k in range(2):
                ga[j, k] = integrate_smooth_partition_torus(
                    lambda z, jj=j, kk=k: ks_pair_c(z, bA[0], bA[1], th1_wA)[jj].conjugate()
                    * ks_pair_c(z, bA[0], bA[1], th1_wA)[kk]
                    * (hm.omega(z) ** (-3)),
                    lvl,
                )
                gd[j, k] = integrate_smooth_partition_torus(
                    lambda z, jj=j, kk=k: ks_pair_c(z, bD[0], bD[1], th1_wD)[jj].conjugate()
                    * ks_pair_c(z, bD[0], bD[1], th1_wD)[kk]
                    * (hm.omega(z) ** (-3)),
                    lvl,
                )

        ta = gs_upper_2x2_np(ga)
        td = gs_upper_2x2_np(gd)
        p_serre = np.array([[-math.pi, 0], [0, math.pi]], dtype=complex)
        c_mat = np.linalg.inv(ta.T @ p_serre)

        # Bloch-Fourier Green solve on M = lvl:
        us = -(1 / 2) + (np.arange(lvl) + (1 / 2)) / lvl
        freqs = np.array(list(range(-(lvl // 2), lvl - (lvl // 2))), dtype=float)
        exp_u1 = np.exp(-2 * I_UNIT * math.pi * np.outer(freqs, us))
        exp_u2 = np.exp(-2 * I_UNIT * math.pi * np.outer(freqs, us))

        def solve_dbar(rhs_g: np.ndarray, b1: float, b2: float) -> np.ndarray:
            ph_grid = np.exp(-2 * I_UNIT * math.pi * (b1 * us[:, None] + b2 * us[None, :]))
            tilde = rhs_g * ph_grid
            hat = (exp_u1 @ tilde @ exp_u2.T) / (lvl * lvl)
            lam = (math.pi / Y_TAU) * ((freqs[:, None] + b1) * tau_c - (freqs[None, :] + b2))
            return hat / lam

        def eval_series(sol_h: np.ndarray, b1: float, b2: float, zv: complex) -> complex:
            u1 = zv.real
            u2 = zv.imag / Y_TAU
            e1 = np.exp(2 * I_UNIT * math.pi * (freqs + b1) * u1)
            e2 = np.exp(2 * I_UNIT * math.pi * (freqs + b2) * u2)
            return complex(e1 @ sol_h @ e2)

        def f1_c(zv: complex) -> complex:
            return kap1 * (th3_c(zv) / th1_and_d1_c(zv)[0])

        k_l2 = np.zeros((2, 2), dtype=complex)
        dbar_good_err = 0
        dbar_bad_err = 0
        z_ann = complex(1 / 5, 1 / 7)
        eps_d = 1 / (10 ** 6)

        for j in range(2):
            c0, c1 = complex(c_mat[0, j]), complex(c_mat[1, j])
            rhs_b = np.zeros((lvl, lvl), dtype=complex)
            rhs_c = np.zeros((lvl, lvl), dtype=complex)
            for p in range(lvl):
                for q in range(lvl):
                    zp = complex(float(us[p]), float(us[q]) * Y_TAU)
                    av = alpha_gauss_c(zp, c0, c1)
                    rhs_b[p, q] = kap0 * av
                    rhs_c[p, q] = f1_c(zp) * av
            sol_b = solve_dbar(rhs_b, 1 / 3, 0)
            sol_c = solve_dbar(rhs_c, 5 / 6, 1 / 2)

            def k_good(zv: complex) -> complex:
                return kap0 * eval_series(sol_c, 5 / 6, 1 / 2, zv) - f1_c(zv) * eval_series(sol_b, 1 / 3, 0, zv)

            def k_bad(zv: complex) -> complex:
                return kap0 * eval_series(sol_c, 5 / 6, 1 / 2, zv) + f1_c(zv) * eval_series(sol_b, 1 / 3, 0, zv)

            dg = ((k_good(z_ann + eps_d) - k_good(z_ann - eps_d)) / (2 * eps_d) + I_UNIT * (k_good(z_ann + I_UNIT * eps_d) - k_good(z_ann - I_UNIT * eps_d)) / (2 * eps_d)) / 2
            db = ((k_bad(z_ann + eps_d) - k_bad(z_ann - eps_d)) / (2 * eps_d) + I_UNIT * (k_bad(z_ann + I_UNIT * eps_d) - k_bad(z_ann - I_UNIT * eps_d)) / (2 * eps_d)) / 2
            dbar_good_err = max(dbar_good_err, abs(dg))
            dbar_bad_err = max(dbar_bad_err, abs(db))

            # Full L^2(Omega_hyp^{-3}) inner-product projection onto orthonormal basis eD_orth (fixing C5-04's 2-point remark!):
            for k_row in range(2):
                def ed_orth_k(zv: complex, kr: int = k_row) -> complex:
                    ed0, ed1 = ks_pair_c(zv, bD[0], bD[1], th1_wD)
                    return complex(td[0, kr]) * ed0 + complex(td[1, kr]) * ed1

                k_l2[k_row, j] = integrate_smooth_partition_torus(
                    lambda z, kr=k_row: ed_orth_k(z, kr).conjugate() * k_good(z) * (hm.omega(z) ** (-3)),
                    lvl,
                )

        svs = np.linalg.svd(k_l2, compute_uv=False)
        res_f1 = kap1 * (TH3_0 / TH1_P0)
        sigma_res = abs(kap0 * res_f1 / complex(td[0, 0])) * math.hypot(abs(complex(c_mat[0, 0])), abs(complex(c_mat[0, 1])))
        return {
            "sigma_1_l2": float(svs[0]),
            "sigma_2_l2": float(svs[1]),
            "sigma_2_over_sigma_1": float(svs[1] / svs[0]),
            "sigma_analytic_residue": float(sigma_res),
            "l2_vs_residue_rel_err": float(abs(svs[0] - sigma_res) / sigma_res),
            "dbar_good_err": float(dbar_good_err),
            "dbar_bad_err": float(dbar_bad_err),
        }

    r16 = eval_joint_level(16)
    r24 = eval_joint_level(24)
    r32 = eval_joint_level(32)

    joint_conv_24_32 = abs(r32["sigma_1_l2"] - r24["sigma_1_l2"]) / r32["sigma_1_l2"]

    e3_passed = bool(
        seq_comp_zero
        and exact_id
        and joint_conv_24_32 < Fraction(2, 1000)
        and r32["l2_vs_residue_rel_err"] < Fraction(1, 10 ** 6)
        and r32["sigma_2_over_sigma_1"] < Fraction(1, 10 ** 8)
        and r32["dbar_good_err"] < (10 ** (-8))  # ENFORCED IN GATE PREDICATE PER C5-04!
        and r32["dbar_bad_err"] > Fraction(1, 10)
    )

    return {
        "E3_RefinedTripletSigmaStar_and_DbarPredicate_Gate_passed": e3_passed,
        "symbolic_connecting_sequence_exactness": bool(seq_comp_zero and exact_id),
        "sigma_star_hyp_l2_16_24_32": [r16["sigma_1_l2"], r24["sigma_1_l2"], r32["sigma_1_l2"]],
        "sigma_star_hyp_residue_16_24_32": [r16["sigma_analytic_residue"], r24["sigma_analytic_residue"], r32["sigma_analytic_residue"]],
        "sqrt2_sigma_star_hyp_32": math.sqrt(2) * r32["sigma_1_l2"],
        "joint_gram_and_fourier_24_vs_32_rel_diff": joint_conv_24_32,
        "l2_projection_vs_analytic_residue_rel_err_32": r32["l2_vs_residue_rel_err"],
        "sigma_2_over_sigma_1_l2_32": r32["sigma_2_over_sigma_1"],
        "enforced_dbar_good_residual_32": r32["dbar_good_err"],
        "PC_SY1_SwappedKoszulSignBreaksHolomorphicity_dbar_err": r32["dbar_bad_err"],
    }


def main() -> None:
    ast_res = verify_ast_synthesis1()
    part_1a, part_1b, hyp_models = run_part_1a_and_1b_hyperbolic_metric_and_lambdas()
    part_1c = run_part_1c_refined_sigma_star_and_dbar_gate(hyp_models)

    controls_passed = bool(
        ast_res["Gate_AST_Stage1_Synthesis_Passed"]
        and part_1a["PC_SY1_NonHyperbolicSeedCurvatureError_rel"] > Fraction(1, 5)
        and part_1a["PC_SY1_OmittedCuspAreaTailMissesGaussBonnet_rel_err"] > Fraction(4, 100)
        and part_1c["PC_SY1_SwappedKoszulSignBreaksHolomorphicity_dbar_err"] > Fraction(1, 10)
    )

    stage_1_passed = bool(
        controls_passed
        and part_1a["E1_HyperbolicLiouville_and_GaussBonnetTail_Gate_passed"]
        and part_1b["E2_HyperbolicLightCubic_and_MetricSensitivity_Gate_passed"]
        and part_1c["E3_RefinedTripletSigmaStar_and_DbarPredicate_Gate_passed"]
    )

    out_payload: Dict[str, Any] = {
        "card": "X-SYNTHESIS-1",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_res,
        "part_1a_hyperbolic_liouville_and_gauss_bonnet": part_1a,
        "part_1b_hyperbolic_light_cubic_and_sensitivity": part_1b,
        "part_1c_refined_triplet_sigma_star_and_dbar_gate": part_1c,
        "all_planted_controls_passed": controls_passed,
        "stage_1_gate_passed": stage_1_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_synthesis_1_out.json"
    out_json.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{sha}  verify_x_synthesis_1_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
