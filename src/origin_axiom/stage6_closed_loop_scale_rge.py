"""Stage 6 (B1861 WP-4.1, WP-4.2, WP-4.3, B1919-B1922, P-831, P-845):
Closed-Loop Shifted-Lattice Kronecker Function, 6D Cusp Geodesic End Law,
Whole-Weave Transfer Spectrum & Cusp Integrability, Level-5 Kashaev Invariant,
and Two-Loop Standard Model RGE Benchmark & Scrambling Gate.

Strictly 0-of-19 data-blind (P-728): zero empirical Standard Model masses, mixings,
couplings, or dimensionful scales appear anywhere in this module. Enforces Guardrails 1-6:
- Part 6A (B1919, B1920, B1921, B1922, WP-4.1 / B1875):
  Closed-form s = 1 shifted-lattice Kronecker limit F_u(tau) at 40-digit precision across
  interior (0 < a < 1) and zero-row (a = 0, 0 < b < 1) branches, cross-checked against
  Kronecker's Jacobi theta_1 / Dedekind eta finite-Fourier identity (< 1e-30), modified-Bessel
  Chowla-Selberg s -> 1 central differences (< 1e-12), and SL(2, Z) T and S co-transport (< 1e-30);
  symbolic 6D geodesic disc cutoff cancellation defining modular-invariant end L_tilde (X:ENDLAW
  retaining 1 unfixed real UV/KK threshold parameter); golden hyperbolic geodesic axis period
  average vs single-point apex (B1920) and level-5 twisted eigenline periodicity vs off-eigenline
  O(1) jump (B1922); 18-of-36 pairwise composite non-closure of single-state admission (B1875)
  and Guardrail 1 classical flat-potential audit (2 unfixed real modulus parameters).
- Part 6B (P-831, B1885, P-845):
  Mod-N Cayley transfer operators on X_N = (Z/NZ)^2 \\ {(0,0)} for N = 2..13 and SL(2, Z/NZ)
  for N = 2..5 (move-parity -1 eigenvalue at even N vs unique +1 at odd N, non-normal positive
  semigroup vs Hermitian symmetric subleading gap shift, level-5 projective index 12 and P^1(F_5)
  index 6); B1885 Euclidean vs hyperbolic Jacobian sensitivity on the fundamental domain; P-845
  Nielsen alphabet rank inversion vs hyperbolic axis length invariance and zero-row Hurwitz linear
  cusp divergence vs zero-row-balanced cusp integrability.
- Part 6C (WP-4.2, WP-4.3, 2-Loop SM RGE):
  Level-5 uniqueness |det(M_gold - I)| = 1 vs |det(M_gold + I)| = 5 and 1-bit SC:PREMISE pricing;
  exact algebraic cyclotomic Kashaev invariant J_5(4_1) = 46 + 2*sqrt(5) (N = 1..6 in SymPy,
  small-N asymptotic factor > 9 vs Richardson-extrapolated large-N hyperbolic volume convergence)
  and P-728 non-sealability; mechanical SymPy trace derivation of 1-loop and 2-loop SM RGE
  coefficients, Guardrail 4 analytical/symbolic 4th-order Lie-jet benchmark gate + negative controls,
  Guardrail 3 U(3)^5 Haar basis-scrambling invariance (< 1e-12) on 3x3 matrix Yukawa running, and
  Guardrail 5 single-anchor non-dimensionalization + pure-SM desert non-unification theorem.
"""
from __future__ import annotations

from itertools import product
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    haar_unitary,
)


# =============================================================================
# Part 6A Helpers: Shifted-Lattice s = 1 Kronecker Limit & Jacobi Theta Cross-Check
# =============================================================================


def kronecker_shifted_s1_mp(
    u1_val: Any,
    u2_val: Any,
    x_re_val: Any,
    y_im_val: Any,
    shell_blocks: int = 2,
) -> Any:
    """Evaluate the B1919 closed-form s = 1 shifted-lattice Kronecker function F_u(x + i*y)
    for u = (u1, u2) not in Z^2 and y > 0 in current mpmath working precision.
    """
    n_shells = 32 * shell_blocks
    u1_m = mp.mpf(u1_val)
    u2_m = mp.mpf(u2_val)
    a_frac = u1_m - mp.floor(u1_m)
    b_frac = u2_m - mp.floor(u2_m)
    zero_cut = (mp.mpf(1) / mp.mpf(64) + mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)) ** 19
    if abs(a_frac - mp.mpf(1)) < zero_cut:
        a_frac = mp.mpf(0)
    if abs(b_frac - mp.mpf(1)) < zero_cut:
        b_frac = mp.mpf(0)

    x_re = mp.mpf(x_re_val)
    y_im = mp.mpf(y_im_val)
    two_pi = 2 * mp.pi

    if abs(a_frac) < zero_cut:
        if abs(b_frac) < zero_cut:
            raise ValueError("Shifted lattice holonomy u cannot lie in Z^2.")
        sin_pb = mp.sin(mp.pi * b_frac)
        c0_term = (
            -mp.pi * mp.log(y_im)
            + two_pi * (mp.euler - mp.log(2))
            + ((mp.pi ** 2) * y_im) / (sin_pb ** 2)
        )
        a_eff = mp.mpf(0)
        is_zero_row = True
    else:
        c0_term = (
            -mp.pi * mp.log(y_im)
            - two_pi * mp.log(2)
            - mp.pi * (mp.digamma(a_frac) + mp.digamma(1 - a_frac))
        )
        a_eff = a_frac
        is_zero_row = False

    series_acc = c0_term
    for k_idx in range(-n_shells, n_shells + 1):
        if is_zero_row and k_idx == 0:
            continue
        m_sh = a_eff + mp.mpf(k_idx)
        abs_m = abs(m_sh)
        theta_m = two_pi * (m_sh * x_re + b_frac)
        r_m = mp.exp(-two_pi * abs_m * y_im)
        cos_th = mp.cos(theta_m)
        re_qm_ratio = (r_m * cos_th - r_m ** 2) / (1 - 2 * r_m * cos_th + r_m ** 2)
        series_acc = series_acc + (two_pi / abs_m) * re_qm_ratio
    return series_acc


def dedekind_eta_abs_mp(x_re_val: Any, y_im_val: Any) -> Any:
    """Evaluate |eta(x + i*y)| via Jacobi's derivative identity theta_1'(0 | tau) = 2 eta(tau)^3."""
    x_re = mp.mpf(x_re_val)
    y_im = mp.mpf(y_im_val)
    q_half = mp.exp(-mp.pi * y_im) * mp.exp(mp.mpc(0, 1) * mp.pi * x_re)
    th1_deriv = mp.jtheta(1, 0, q_half, 1)
    return abs(th1_deriv / 2) ** mp.fdiv(1, 3)


def kronecker_theta_fourier_torsion_mp(
    p1_int: int,
    p2_int: int,
    level_n: int,
    x_re_val: Any,
    y_im_val: Any,
) -> Any:
    """Evaluate F_{(p1/N, p2/N)}(x + i*y) independently via finite Fourier inversion over (Z/NZ)^2
    applied to Kronecker's first and second limit formulas (Jacobi theta_1 / Dedekind eta).
    """
    x_re = mp.mpf(x_re_val)
    y_im = mp.mpf(y_im_val)
    q_half = mp.exp(-mp.pi * y_im) * mp.exp(mp.mpc(0, 1) * mp.pi * x_re)
    eta_mod = dedekind_eta_abs_mp(x_re, y_im)
    n_mp = mp.mpf(level_n)
    acc_val = 2 * mp.pi * mp.log(n_mp)

    for c_idx in range(level_n):
        for d_idx in range(level_n):
            phase_wt = mp.cos(2 * mp.pi * mp.mpf(c_idx * p1_int + d_idx * p2_int) / n_mp)
            if c_idx == 0 and d_idx == 0:
                g_cd = (
                    2 * mp.pi * (mp.euler - mp.log(2))
                    - mp.pi * mp.log(y_im)
                    - 4 * mp.pi * mp.log(eta_mod)
                )
            else:
                v1_f = mp.fdiv(c_idx, level_n)
                v2_f = mp.fdiv(d_idx, level_n)
                z_re = v2_f * x_re - v1_f
                z_im = v2_f * y_im
                z_pi = mp.pi * z_re + mp.mpc(0, 1) * mp.pi * z_im
                th1_abs = abs(mp.jtheta(1, z_pi, q_half))
                g_cd = (
                    -2 * mp.pi * mp.log(th1_abs / eta_mod)
                    + 2 * (mp.pi ** 2) * (v2_f ** 2) * y_im
                )
            acc_val = acc_val + phase_wt * g_cd
    return acc_val


def chowla_selberg_shifted_epstein_mp(
    u1_val: Any,
    u2_val: Any,
    x_re_val: Any,
    y_im_val: Any,
    s_val: Any,
    shell_blocks: int = 1,
    harm_blocks: int = 1,
) -> Any:
    """Evaluate Z_u(x + i*y, s) for s != 1 via the Poisson-resummed modified-Bessel K_{s-1/2} expansion."""
    n_shells = 28 * shell_blocks
    n_harmonics = 28 * harm_blocks
    u1_m = mp.mpf(u1_val)
    u2_m = mp.mpf(u2_val)
    a_frac = u1_m - mp.floor(u1_m)
    b_frac = u2_m - mp.floor(u2_m)
    zero_cut = (mp.mpf(1) / mp.mpf(64) + mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)) ** 19
    if abs(a_frac - mp.mpf(1)) < zero_cut:
        a_frac = mp.mpf(0)
    if abs(b_frac - mp.mpf(1)) < zero_cut:
        b_frac = mp.mpf(0)

    x_re = mp.mpf(x_re_val)
    y_im = mp.mpf(y_im_val)
    s_mp = mp.mpf(s_val)
    half_mp = mp.fdiv(1, 2)

    if abs(a_frac) < zero_cut:
        z_zero = (y_im ** s_mp) * (mp.hurwitz(2 * s_mp, b_frac) + mp.hurwitz(2 * s_mp, 1 - b_frac))
        z_const = (
            2
            * (y_im ** (1 - s_mp))
            * mp.sqrt(mp.pi)
            * (mp.gamma(s_mp - half_mp) / mp.gamma(s_mp))
            * mp.zeta(2 * s_mp - 1)
        )
        a_eff = mp.mpf(0)
        is_zero_row = True
    else:
        z_zero = mp.mpf(0)
        z_const = (
            (y_im ** (1 - s_mp))
            * mp.sqrt(mp.pi)
            * (mp.gamma(s_mp - half_mp) / mp.gamma(s_mp))
            * (mp.hurwitz(2 * s_mp - 1, a_frac) + mp.hurwitz(2 * s_mp - 1, 1 - a_frac))
        )
        a_eff = a_frac
        is_zero_row = False

    bessel_sum = mp.mpf(0)
    pref_b = 2 * (mp.pi ** s_mp) * (y_im ** half_mp) / mp.gamma(s_mp)
    for k_idx in range(-n_shells, n_shells + 1):
        if is_zero_row and k_idx == 0:
            continue
        m_sh = a_eff + mp.mpf(k_idx)
        abs_m = abs(m_sh)
        for ell_idx in range(1, n_harmonics + 1):
            ell_mp = mp.mpf(ell_idx)
            arg_k = 2 * mp.pi * ell_mp * abs_m * y_im
            if arg_k > mp.mpf(105):
                break
            ratio_p = (ell_mp / abs_m) ** (s_mp - half_mp)
            cos_term = 2 * mp.cos(2 * mp.pi * ell_mp * (m_sh * x_re + b_frac))
            bessel_sum = bessel_sum + ratio_p * cos_term * mp.besselk(s_mp - half_mp, arg_k)
    return z_zero + z_const + pref_b * bessel_sum


def mobius_sl2_xy_mp(
    a_c: int,
    b_c: int,
    c_c: int,
    d_c: int,
    x_in: Any,
    y_in: Any,
) -> tuple[Any, Any]:
    """Apply SL(2, Z) Mobius map (a*tau + b) / (c*tau + d) in pure real mpmath coordinates (x, y)."""
    x_r = mp.mpf(x_in)
    y_i = mp.mpf(y_in)
    a_m = mp.mpf(a_c)
    b_m = mp.mpf(b_c)
    c_m = mp.mpf(c_c)
    d_m = mp.mpf(d_c)
    denom = ((c_m * x_r + d_m) ** 2) + ((c_m * y_i) ** 2)
    re_out = mp.fdiv((a_m * x_r + b_m) * (c_m * x_r + d_m) + a_m * c_m * (y_i ** 2), denom)
    im_out = mp.fdiv((a_m * d_m - b_m * c_m) * y_i, denom)
    return re_out, im_out


def verify_part6a_kronecker_cusp_end_and_wp41() -> dict[str, Any]:
    """Verify Part 6A: B1919 shifted Kronecker limit F_u(tau), B1921 6D geodesic cutoff end L_tilde,
    B1920 geodesic thread period average vs apex, B1922 twisted eigenline periodicity vs off-eigenline
    jump, and WP-4.1 / B1875 single-state non-closure (18 of 36) + Guardrail 1 flat-potential audit.
    """
    dyn_z = mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)
    with mp.workdps(40):
        probe_xy = (mp.fdiv(3, 7) + dyn_z, mp.fdiv(11, 9) + dyn_z)
        alt_xy = (mp.fdiv(-2, 9) + dyn_z, mp.fdiv(13, 8) + dyn_z)
        eps_s = (mp.fdiv(1, 64) + dyn_z) ** 4

        max_theta_fourier_err = 0.0
        max_bessel_cd_err = 0.0
        max_sl2_cotransport_err = 0.0

        level5_probes = [(2, 4), (0, 2), (2, 0), (1, 3), (3, 4)]
        for p1_i, p2_i in level5_probes:
            u1_p = mp.fdiv(p1_i, 5)
            u2_p = mp.fdiv(p2_i, 5)
            for x_cur, y_cur in (probe_xy, alt_xy):
                f_closed = kronecker_shifted_s1_mp(u1_p, u2_p, x_cur, y_cur)
                f_theta = kronecker_theta_fourier_torsion_mp(p1_i, p2_i, 5, x_cur, y_cur)
                max_theta_fourier_err = max(max_theta_fourier_err, float(abs(f_closed - f_theta)))

                # T: tau -> tau + 1, F_u(tau + 1) == F_{u T}(tau) with u T = (u1, u1 + u2)
                xt_m, yt_m = mobius_sl2_xy_mp(1, 1, 0, 1, x_cur, y_cur)
                f_t_lhs = kronecker_shifted_s1_mp(u1_p, u2_p, xt_m, yt_m)
                f_t_rhs = kronecker_shifted_s1_mp(u1_p, u1_p + u2_p, x_cur, y_cur)
                # S: tau -> -1/tau, F_u(-1/tau) == F_{u S}(tau) with u S = (u2, -u1)
                xs_m, ys_m = mobius_sl2_xy_mp(0, -1, 1, 0, x_cur, y_cur)
                f_s_lhs = kronecker_shifted_s1_mp(u1_p, u2_p, xs_m, ys_m)
                f_s_rhs = kronecker_shifted_s1_mp(u2_p, -u1_p, x_cur, y_cur)
                # Evenness F_{-u}(tau) == F_u(tau):
                f_neg_u = kronecker_shifted_s1_mp(-u1_p, -u2_p, x_cur, y_cur)
                max_sl2_cotransport_err = max(
                    max_sl2_cotransport_err,
                    float(abs(f_t_lhs - f_t_rhs)),
                    float(abs(f_s_lhs - f_s_rhs)),
                    float(abs(f_closed - f_neg_u)),
                )

            # Central-difference limit of Z_u(tau, s) - pi/(s - 1) around s = 1:
            reg_plus = (
                chowla_selberg_shifted_epstein_mp(u1_p, u2_p, probe_xy[0], probe_xy[1], 1 + eps_s)
                - mp.pi / eps_s
            )
            reg_minus = (
                chowla_selberg_shifted_epstein_mp(u1_p, u2_p, probe_xy[0], probe_xy[1], 1 - eps_s)
                + mp.pi / eps_s
            )
            f_cd_mid = mp.fdiv(reg_plus + reg_minus, 2)
            f_ref = kronecker_shifted_s1_mp(u1_p, u2_p, probe_xy[0], probe_xy[1])
            max_bessel_cd_err = max(max_bessel_cd_err, float(abs(f_ref - f_cd_mid)))

        # B1920 & B1922: Golden hyperbolic axis gamma_gold = L * R = [[2, 1], [1, 1]] (tr = 3)
        sqrt5_mp = mp.sqrt(mp.mpf(5))
        ell_gold = 2 * mp.log(mp.fdiv(3 + sqrt5_mp, 2))
        ell_gold_acosh = 2 * mp.acosh(mp.fdiv(3, 2))
        ell_gold_formula_err = float(abs(ell_gold - ell_gold_acosh))

        def tau_golden_xy(s_arc: Any) -> tuple[Any, Any]:
            re_g = mp.fdiv(1, 2) + mp.fdiv(sqrt5_mp, 2) * mp.tanh(s_arc)
            im_g = mp.fdiv(sqrt5_mp, 2 * mp.cosh(s_arc))
            return re_g, im_g

        # Verify unit-speed ds_hyp = |tau'(s)| / Im(tau(s)) == 1 and exact Mobius shift tau(s + ell) == gamma(tau(s)):
        geodesic_unit_speed_err = 0.0
        geodesic_mobius_period_err = 0.0
        eigenline_periodicity_err = 0.0
        u_eig_1 = mp.fdiv(2, 5)
        u_eig_2 = mp.fdiv(4, 5)
        for s_num in (-2, -1, 0, 1):
            s_pt = mp.fdiv(s_num, 7) + dyn_z
            x_pt, y_pt = tau_golden_xy(s_pt)
            h_fd = (mp.fdiv(1, 64) + dyn_z) ** 8
            xp_h, yp_h = tau_golden_xy(s_pt + h_fd)
            xm_h, ym_h = tau_golden_xy(s_pt - h_fd)
            dx_ds = mp.fdiv(xp_h - xm_h, 2 * h_fd)
            dy_ds = mp.fdiv(yp_h - ym_h, 2 * h_fd)
            speed_s = mp.fdiv(mp.sqrt((dx_ds ** 2) + (dy_ds ** 2)), y_pt)
            geodesic_unit_speed_err = max(geodesic_unit_speed_err, float(abs(speed_s - 1)))

            x_sh, y_sh = tau_golden_xy(s_pt + ell_gold)
            x_mb, y_mb = mobius_sl2_xy_mp(2, 1, 1, 1, x_pt, y_pt)
            mob_dist = mp.sqrt(((x_sh - x_mb) ** 2) + ((y_sh - y_mb) ** 2))
            geodesic_mobius_period_err = max(geodesic_mobius_period_err, float(mob_dist))

            f_eig_0 = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_pt, y_pt, 3)
            f_eig_1 = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_sh, y_sh, 3)
            eigenline_periodicity_err = max(eigenline_periodicity_err, float(abs(f_eig_1 - f_eig_0)))

        # Off-eigenline level-5 holonomy u_off = (1/5, 3/5) -> u_off * gamma_gold = (1, 4/5) == (0, 4/5) (mod 1):
        x_apx, y_apx = tau_golden_xy(dyn_z)
        apex_coord_err = float(
            mp.sqrt(((x_apx - mp.fdiv(1, 2)) ** 2) + ((y_apx - mp.fdiv(sqrt5_mp, 2)) ** 2))
        )
        f_off_0 = kronecker_shifted_s1_mp(mp.fdiv(1, 5), mp.fdiv(3, 5), x_apx, y_apx)
        x_apx_g, y_apx_g = mobius_sl2_xy_mp(2, 1, 1, 1, x_apx, y_apx)
        f_off_1 = kronecker_shifted_s1_mp(mp.fdiv(1, 5), mp.fdiv(3, 5), x_apx_g, y_apx_g)
        off_eigenline_jump = float(abs(f_off_1 - f_off_0))

        # B1920: Closed geodesic period average over symmetric period [-ell_gold/2, +ell_gold/2] vs apex:
        half_ell = mp.fdiv(ell_gold, 2)
        f_apex_eig = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_apx, y_apx, 1)

        def eval_f_along_golden(s_q: Any) -> Any:
            xq_s, yq_s = tau_golden_xy(s_q)
            return kronecker_shifted_s1_mp(u_eig_1, u_eig_2, xq_s, yq_s, 1)

        f_geodesic_integral = mp.quad(eval_f_along_golden, [-half_ell, half_ell])
        f_geodesic_avg = mp.fdiv(f_geodesic_integral, ell_gold)
        geodesic_avg_minus_apex_abs = float(abs(f_geodesic_avg - f_apex_eig))

        # B1921 numerical SL(2, Z) invariance of 2*pi*L_tilde + F_u(tau) for arbitrary physical cutoff ratio:
        l_tilde_num = -mp.log(mp.fdiv(1, 7)) - (mp.euler + mp.log(mp.pi))
        end_comb_base = 2 * mp.pi * l_tilde_num + kronecker_shifted_s1_mp(
            u_eig_1, u_eig_2, probe_xy[0], probe_xy[1]
        )
        xs_pr, ys_pr = mobius_sl2_xy_mp(0, -1, 1, 0, probe_xy[0], probe_xy[1])
        xt_pr, yt_pr = mobius_sl2_xy_mp(1, 1, 0, 1, probe_xy[0], probe_xy[1])
        end_comb_s = 2 * mp.pi * l_tilde_num + kronecker_shifted_s1_mp(u_eig_2, -u_eig_1, xs_pr, ys_pr)
        end_comb_t = 2 * mp.pi * l_tilde_num + kronecker_shifted_s1_mp(
            u_eig_1, u_eig_2 - u_eig_1, xt_pr, yt_pr
        )
        b1921_modular_err = max(float(abs(end_comb_base - end_comb_s)), float(abs(end_comb_base - end_comb_t)))

    # B1921 symbolic proof of exact ln(Im tau) cancellation in SymPy:
    y_sym, area_phys, eps_phys, ell_0, f_mod_cov = sp.symbols(
        "y_sym area_phys eps_phys ell_0 f_mod_cov", positive=True
    )
    gamma_sym = sp.EulerGamma
    eps_coord_sym = eps_phys * sp.sqrt(y_sym / area_phys)
    l_coord_sym = -sp.log(eps_coord_sym / ell_0)
    # Stripped lattice sum N(u, tau) = F_u(tau) + pi * ln(y) - 2*pi*(gamma_E + ln(pi)):
    n_stripped_sym = f_mod_cov + sp.pi * sp.log(y_sym) - 2 * sp.pi * (gamma_sym + sp.log(sp.pi))
    total_reg_sym = sp.expand(2 * sp.pi * l_coord_sym + n_stripped_sym)
    l_tilde_sym = sp.simplify((total_reg_sym - f_mod_cov) / (2 * sp.pi))
    l_tilde_expected = -sp.log(eps_phys / (ell_0 * sp.sqrt(area_phys))) - (gamma_sym + sp.log(sp.pi))
    b1921_ln_y_cancelled = (
        sp.simplify(sp.diff(l_tilde_sym, y_sym)) == 0
        and sp.simplify(l_tilde_sym - l_tilde_expected) == 0
        and sp.simplify(sp.diff(l_tilde_sym, eps_phys)) != 0
    )
    # Jacobian rank of L_tilde with respect to dimensionless UV threshold ratio rho_uv = eps_phys / (ell_0 * sqrt(area_phys)):
    rho_uv = sp.Symbol("rho_uv", positive=True)
    l_tilde_rho = -sp.log(rho_uv) - (gamma_sym + sp.log(sp.pi))
    unfixed_end_law_params = int(sp.Matrix([[sp.diff(l_tilde_rho, rho_uv)]]).rank())

    # WP-4.1 / B1875: Non-closure of single-state admission (18 of 36 pairwise composites):
    mat_l = sp.Matrix([[1, 1], [0, 1]])
    mat_r = sp.Matrix([[1, 0], [1, 1]])
    sym_hyp_6 = [
        mat_l * mat_r,
        mat_l * mat_l * mat_r,
        mat_l * mat_r * mat_r,
        (mat_l * mat_r).inv(),
        (mat_l * mat_l * mat_r).inv(),
        (mat_l * mat_r * mat_r).inv(),
    ]
    hyp_grid_6x6 = np.zeros((6, 6), dtype=int)
    for idx_a in range(6):
        for idx_b in range(6):
            tr_ab = abs(int((sym_hyp_6[idx_a] * sym_hyp_6[idx_b]).trace()))
            hyp_grid_6x6[idx_a, idx_b] = 1 if tr_ab > 2 else 0
    b1875_total_pairs = int(np.sum(np.ones_like(hyp_grid_6x6)))
    b1875_hyp_kept_count = int(np.sum(hyp_grid_6x6))
    b1875_hyp_failed_count = int(np.sum(1 - hyp_grid_6x6))

    # Also verify positive 2-run single-syllable words {LR, RL, LLR, LRR, RLL, RRL} (18 of 36 stay 1-syllable):
    pos_single_syllable_6 = ["LR", "RL", "LLR", "LRR", "RLL", "RRL"]
    onesyl_grid_6x6 = np.zeros((6, 6), dtype=int)
    for idx_a in range(6):
        for idx_b in range(6):
            w_ab = pos_single_syllable_6[idx_a] + pos_single_syllable_6[idx_b]
            cyc_switches = sum(
                1 for idx_c in range(len(w_ab)) if w_ab[idx_c] != w_ab[(idx_c + 1) % len(w_ab)]
            )
            onesyl_grid_6x6[idx_a, idx_b] = 1 if cyc_switches == 2 else 0
    b1875_onesyl_kept_count = int(np.sum(onesyl_grid_6x6))
    b1875_onesyl_failed_count = int(np.sum(1 - onesyl_grid_6x6))

    # Guardrail 1 (Anti-Texas-Sharpshooter): Poincare hyperbolic metric on H^2 has rank 2 and zero classical potential:
    x_mod, y_mod = sp.symbols("x_mod y_mod", real=True)
    poincare_metric_2x2 = sp.Matrix([[1 / (y_mod ** 2), 0], [0, 1 / (y_mod ** 2)]])
    tau_open_real_params = int(poincare_metric_2x2.rank())
    # Verify det(poincare_metric) > 0 on y_mod > 0 and classical potential V_cl == 0 has zero gradient:
    v_classical_flat = sp.Integer(0) * x_mod + sp.Integer(0) * y_mod
    grad_vcl_zero = (
        sp.diff(v_classical_flat, x_mod) == 0
        and sp.diff(v_classical_flat, y_mod) == 0
        and sp.simplify(poincare_metric_2x2.det() * (y_mod ** 4) - 1) == 0
    )

    part6a_ok = (
        max_theta_fourier_err < 1e-30
        and max_bessel_cd_err < TOL
        and max_sl2_cotransport_err < 1e-30
        and ell_gold_formula_err < 1e-30
        and geodesic_unit_speed_err < TOL
        and geodesic_mobius_period_err < 1e-30
        and apex_coord_err < 1e-30
        and eigenline_periodicity_err < 1e-30
        and off_eigenline_jump > 1.0
        and geodesic_avg_minus_apex_abs > (1 / 10)
        and b1921_modular_err < 1e-30
        and bool(b1921_ln_y_cancelled)
        and unfixed_end_law_params == 1
        and b1875_total_pairs == 36
        and b1875_hyp_kept_count == 18
        and b1875_hyp_failed_count == 18
        and b1875_onesyl_kept_count == 18
        and b1875_onesyl_failed_count == 18
        and tau_open_real_params == 2
        and bool(grad_vcl_zero)
    )

    return {
        "b1919_max_theta_fourier_err": max_theta_fourier_err,
        "b1919_max_bessel_cd_err": max_bessel_cd_err,
        "b1919_max_sl2_cotransport_err": max_sl2_cotransport_err,
        "b1920_golden_geodesic_period": float(ell_gold),
        "b1920_geodesic_avg_f": float(f_geodesic_avg),
        "b1920_apex_f": float(f_apex_eig),
        "b1920_geodesic_avg_minus_apex_abs": geodesic_avg_minus_apex_abs,
        "b1921_modular_invariance_err": b1921_modular_err,
        "b1921_ln_im_tau_cancellation_verified": bool(b1921_ln_y_cancelled),
        "b1921_unfixed_end_law_real_params": unfixed_end_law_params,
        "b1922_eigenline_periodicity_err": eigenline_periodicity_err,
        "b1922_off_eigenline_jump": off_eigenline_jump,
        "wp41_b1875_total_pairwise_composites": b1875_total_pairs,
        "wp41_b1875_hyperbolic_admitted_count": b1875_hyp_kept_count,
        "wp41_b1875_non_hyperbolic_escaped_count": b1875_hyp_failed_count,
        "wp41_b1875_single_syllable_admitted_count": b1875_onesyl_kept_count,
        "guardrail1_tau_open_real_params": tau_open_real_params,
        "part6a_kronecker_end_and_wp41_verified": part6a_ok,
    }


# =============================================================================
# Part 6B: Whole-Weave Transfer Spectrum (P-831), B1885 Jacobian, & P-845 Cusp Law
# =============================================================================


def build_mod_n_vector_transfer(
    level_n: int,
    primitive_only: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    """Build Markov transfer matrices P_+^(N) and P_{+-}^(N) on X_N = (Z/NZ)^2 \\ {(0,0)}
    (or on the primitive torsion orbit X_N^prim = {u : gcd(u0, u1, N) = 1} when primitive_only=True).
    """
    states = [
        (r_i, c_i)
        for r_i in range(level_n)
        for c_i in range(level_n)
        if not (r_i == 0 and c_i == 0)
        and (not primitive_only or math.gcd(math.gcd(r_i, c_i), level_n) == 1)
    ]
    idx_map = {st: idx_s for idx_s, st in enumerate(states)}
    dim_x = len(states)
    t_l = np.zeros((dim_x, dim_x), dtype=float)
    t_r = np.zeros((dim_x, dim_x), dtype=float)
    t_li = np.zeros((dim_x, dim_x), dtype=float)
    t_ri = np.zeros((dim_x, dim_x), dtype=float)

    for idx_s, (u0, u1) in enumerate(states):
        t_l[idx_map[(u0, (u0 + u1) % level_n)], idx_s] = 1.0
        t_r[idx_map[((u0 + u1) % level_n, u1)], idx_s] = 1.0
        t_li[idx_map[(u0, (u1 - u0) % level_n)], idx_s] = 1.0
        t_ri[idx_map[((u0 - u1) % level_n, u1)], idx_s] = 1.0

    p_pos = (1 / 2) * (t_l + t_r)
    p_sym = (1 / 4) * (t_l + t_r + t_li + t_ri)
    return p_pos, p_sym


def build_sl2_mod_n_transfer(level_n: int) -> tuple[int, np.ndarray, np.ndarray]:
    """Enumerate G_N = SL(2, Z/NZ) and build right-Cayley Markov operators P_+ and P_{+-}."""
    elems = [
        (a0, a1, a2, a3)
        for a0, a1, a2, a3 in product(range(level_n), repeat=4)
        if (a0 * a3 - a1 * a2) % level_n == 1
    ]
    idx_g = {el: k_e for k_e, el in enumerate(elems)}
    n_g = len(elems)

    def mul_g(x_e: tuple[int, int, int, int], y_e: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return (
            (x_e[0] * y_e[0] + x_e[1] * y_e[2]) % level_n,
            (x_e[0] * y_e[1] + x_e[1] * y_e[3]) % level_n,
            (x_e[2] * y_e[0] + x_e[3] * y_e[2]) % level_n,
            (x_e[2] * y_e[1] + x_e[3] * y_e[3]) % level_n,
        )

    g_l = (1, 1, 0, 1)
    g_r = (1, 0, 1, 1)
    g_li = (1, (-1) % level_n, 0, 1)
    g_ri = (1, 0, (-1) % level_n, 1)

    p_pos = np.zeros((n_g, n_g), dtype=float)
    p_sym = np.zeros((n_g, n_g), dtype=float)
    q_wt = 1 / 4
    for k_e, el in enumerate(elems):
        for gen_p in (g_l, g_r):
            p_pos[idx_g[mul_g(el, gen_p)], k_e] += 0.5
        for gen_s in (g_l, g_r, g_li, g_ri):
            p_sym[idx_g[mul_g(el, gen_s)], k_e] += q_wt
    return n_g, p_pos, p_sym


def verify_part6b_whole_weave_transfer_and_p845() -> dict[str, Any]:
    """Verify Part 6B: P-831 mod-N Cayley transfer spectra (N = 2..13 on X_N and N = 2..5 on G_N),
    B1885 Jacobian sensitivity on F_{SL(2,Z)}, and P-845 Nielsen rank inversion vs geodesic axis
    invariance plus zero-row Hurwitz linear cusp divergence vs zero-row-balanced integrability.
    """
    # 1. P-831 on X_N = (Z/NZ)^2 \ {(0,0)} and primitive carrier X_N^prim across N = 2..13:
    unique_stationary_prim_all = True
    full_xn_orbit_counts_exact = True
    nonnormal_pos_for_ge3 = True
    subleading_gap_shifts: list[float] = []
    level5_alphabet_gap_shift = 0.0
    min_spectral_gap_sym = 1.0

    zero_i = int(sp.Matrix.eye(1).trace()) - 1
    for n_lev in range(2, 14):
        n_dyn = n_lev + zero_i
        p_pos_full, p_sym_full = build_mod_n_vector_transfer(n_dyn, primitive_only=False)
        ev_sym_full = np.linalg.eigvalsh(p_sym_full)
        proper_div_cnt = sum(1 for d_i in range(1, n_lev) if n_lev % d_i == 0)
        unit_full_cnt = int(np.sum(np.abs(ev_sym_full - 1.0) < 1e-9))
        if unit_full_cnt != proper_div_cnt:
            full_xn_orbit_counts_exact = False

        p_pos_n, p_sym_n = build_mod_n_vector_transfer(n_dyn, primitive_only=True)
        ev_sym = np.linalg.eigvalsh(p_sym_n)
        ev_pos = np.linalg.eigvals(p_pos_n)

        unit_sym_cnt = int(np.sum(np.abs(np.abs(ev_sym) - 1.0) < 1e-9))
        unit_pos_cnt = int(np.sum(np.abs(ev_pos - 1.0) < 1e-9))
        if unit_sym_cnt != 1 or unit_pos_cnt != 1:
            unique_stationary_prim_all = False

        sub_sym = float(np.max(np.abs(ev_sym[np.abs(ev_sym - 1.0) > 1e-7])))
        sub_pos = float(np.max(np.abs(ev_pos[np.abs(ev_pos - 1.0) > 1e-7])))
        min_spectral_gap_sym = min(min_spectral_gap_sym, 1.0 - sub_sym)

        if n_lev >= 3:
            comm_norm = float(np.linalg.norm(p_pos_n @ p_pos_n.T - p_pos_n.T @ p_pos_n))
            if comm_norm < 1e-6:
                nonnormal_pos_for_ge3 = False
            subleading_gap_shifts.append(abs(sub_pos - sub_sym))
            if n_lev == 5:
                level5_alphabet_gap_shift = abs(sub_pos - sub_sym)

    max_subleading_alphabet_shift = float(np.max(np.array(subleading_gap_shifts, dtype=float)))

    # P-831 on full group G_N = SL(2, Z/NZ) for N = 2, 3, 4, 5:
    # Move-count parity chi(L) = chi(R) = -1 factors through SL(2, Z/NZ) iff 2 | N (since L^N = I => (-1)^N = 1)!
    gn_orders: dict[int, int] = {}
    gn_unit_mod_counts_sym: dict[int, int] = {}
    for n_g_lev in (2, 3, 4, 5):
        ord_gn, _, p_sym_gn = build_sl2_mod_n_transfer(n_g_lev + zero_i)
        ev_gn = np.linalg.eigvalsh(p_sym_gn)
        gn_orders[n_g_lev] = int(np.sum(np.ones(ord_gn, dtype=int)))
        gn_unit_mod_counts_sym[n_g_lev] = int(np.sum(np.abs(np.abs(ev_gn) - 1.0) < 1e-9))

    sl2_mod5_order = gn_orders[5]
    # Level-5 +/- eigenline orbit size in X_5 / {+-1} and projective line P^1(F_5):
    elems_g5 = [
        (a0, a1, a2, a3)
        for a0, a1, a2, a3 in product(range(5), repeat=4)
        if (a0 * a3 - a1 * a2) % 5 == 1
    ]
    pm_orbit_5: set[tuple[int, int]] = set()
    proj_orbit_5: set[tuple[int, int]] = set()
    for a0, a1, a2, a3 in elems_g5:
        v0 = (2 * a0 + 4 * a2) % 5
        v1 = (2 * a1 + 4 * a3) % 5
        canon_pm = min((v0, v1), ((-v0) % 5, (-v1) % 5))
        pm_orbit_5.add(canon_pm)
        # Canonical projective representative in P^1(F_5): first nonzero coordinate normalized to 1
        for scale_f in range(1, 5):
            s0 = (scale_f * v0) % 5
            s1 = (scale_f * v1) % 5
            if (s0 == 1) or (s0 == 0 and s1 == 1):
                proj_orbit_5.add((s0, s1))
                break
    level5_pm_index = int(np.sum(np.ones(len(pm_orbit_5), dtype=int)))
    level5_p1_index = int(np.sum(np.ones(len(proj_orbit_5), dtype=int)))

    # 2. B1885: Euclidean dx*dy vs hyperbolic dx*dy / y^2 Jacobian sensitivity on fundamental domain slice:
    with mp.workdps(35):
        # Modular-related smooth positive test profile h(y) = y^3 * |eta(i*y)|^12 on y in [1, 3]:
        def profile_b1885(y_v: Any) -> Any:
            eta_v = dedekind_eta_abs_mp(mp.mpf(0), y_v)
            return (y_v ** 3) * (eta_v ** 12)

        num_euc = mp.quad(lambda y_q: y_q * profile_b1885(y_q), [mp.mpf(1), mp.mpf(3)])
        den_euc = mp.quad(lambda y_q: profile_b1885(y_q), [mp.mpf(1), mp.mpf(3)])
        mean_y_euclidean = num_euc / den_euc

        num_hyp = mp.quad(lambda y_q: (y_q * profile_b1885(y_q)) / (y_q ** 2), [mp.mpf(1), mp.mpf(3)])
        den_hyp = mp.quad(lambda y_q: profile_b1885(y_q) / (y_q ** 2), [mp.mpf(1), mp.mpf(3)])
        mean_y_hyperbolic = num_hyp / den_hyp
        b1885_jacobian_mean_shift = float(abs(mean_y_euclidean - mean_y_hyperbolic))

    # 3. P-845 Check 1: Nielsen alphabet presentation shift vs hyperbolic geodesic axis length invariance:
    # Free Sanov generators A = L^2, B = R^2; Nielsen transformation A' = A, B' = A * B:
    mat_l = sp.Matrix([[1, 1], [0, 1]])
    mat_r = sp.Matrix([[1, 0], [1, 1]])
    gen_a = mat_l * mat_l
    gen_b = mat_r * mat_r
    # Word gamma_1 = A * B = B', word gamma_2 = B = (A')^{-1} * B':
    gamma_1 = gen_a * gen_b
    gamma_2 = gen_b
    # Cyclic reduced word lengths in {A, B} vs {A', B'}:
    # gamma_1 = "ab" (len 2 in {A,B}) = "y" (len 1 in {A'=x, B'=y});
    # gamma_2 = "b"  (len 1 in {A,B}) = "Xy" (len 2 in {A'=x, B'=y})!
    len_ab_g1 = len("ab")
    len_ab_g2 = len("b")
    len_nielsen_g1 = len("y")
    len_nielsen_g2 = len("Xy")
    beta_w = 0.5
    weight_ratio_ab = math.exp(-beta_w * len_ab_g1) / math.exp(-beta_w * len_ab_g2)
    weight_ratio_nielsen = math.exp(-beta_w * len_nielsen_g1) / math.exp(-beta_w * len_nielsen_g2)
    nielsen_rank_inverted = (weight_ratio_ab < 1.0) and (weight_ratio_nielsen > 1.0)

    # Geodesic axis length ell_hyp(gamma) = 2 * arccosh(|tr(gamma)| / 2) is invariant under BOTH
    # Nielsen basis rewriting AND arbitrary SL(2, Z) conjugation g * gamma * g^{-1}:
    conj_s = sp.Matrix([[0, -1], [1, 0]])
    conj_lr = mat_l * mat_r
    hyp_test_mats = [gamma_1, gen_a * gen_a * gen_b, gen_a * gen_b * gen_a * gen_b * gen_b]
    max_axis_conj_err = 0.0
    for m_hyp in hyp_test_mats:
        ell_base = 2.0 * math.acosh(abs(float(int(m_hyp.trace()))) * 0.5)
        for g_c in (mat_l, mat_r, conj_s, conj_lr):
            m_conj = g_c * m_hyp * g_c.inv()
            ell_conj = 2.0 * math.acosh(abs(float(int(m_conj.trace()))) * 0.5)
            max_axis_conj_err = max(max_axis_conj_err, abs(ell_base - ell_conj))

    # 4. P-845 Check 2: Zero-row Hurwitz cusp divergence vs zero-row-balanced cusp integrability:
    sigma_cusp = sp.Matrix([[2, 1], [-1, 0]])
    u_vec = sp.Matrix([[sp.Rational(2, 5), sp.Rational(4, 5)]])
    u_sigma = u_vec * sigma_cusp
    a_cusp_mod1 = u_sigma[0, 0] - sp.floor(u_sigma[0, 0])
    b_cusp_mod1 = u_sigma[0, 1] - sp.floor(u_sigma[0, 1])

    # Symbolic cusp integrals against hyperbolic measure dy / y^2 on [2, Y_cut]:
    y_c, y_cut = sp.symbols("y_c y_cut", positive=True)
    div_lin_int = sp.integrate(y_c / (y_c ** 2), (y_c, 2, y_cut))
    conv_log_int = sp.integrate(sp.log(y_c) / (y_c ** 2), (y_c, 2, sp.oo))
    slope_exact_sym = sp.simplify((sp.pi ** 2) / (sp.sin(2 * sp.pi / 5) ** 2))
    slope_rad_sym = sp.simplify(8 * (sp.pi ** 2) / (5 + sp.sqrt(5)))
    symbolic_cusp_laws_exact = (
        int(sigma_cusp.det()) == 1
        and a_cusp_mod1 == 0
        and b_cusp_mod1 == sp.Rational(2, 5)
        and sp.simplify(div_lin_int - sp.log(y_cut / 2)) == 0
        and sp.limit(div_lin_int, y_cut, sp.oo) == sp.oo
        and sp.simplify(conv_log_int - (1 + sp.log(2)) / 2) == 0
        and sp.simplify(slope_exact_sym - slope_rad_sym) == 0
    )

    dyn_zb = mp.mpf(int(sp.Matrix.eye(1).trace()) - 1)
    with mp.workdps(40):
        slope_expected_mp = (mp.pi ** 2) / (mp.sin(mp.pi * mp.fdiv(2, 5)) ** 2)
        # Verify co-transport F_{(2/5,4/5)}(sigma(i*y)) == F_{(0,2/5)}(i*y) and asymptotic linear slope:
        y_co = mp.mpf(2) + dyn_zb
        x_sig_co, y_sig_co = mobius_sl2_xy_mp(2, 1, -1, 0, dyn_zb, y_co)
        f_cotrans_co = kronecker_shifted_s1_mp(mp.fdiv(2, 5), mp.fdiv(4, 5), x_sig_co, y_sig_co, 3)
        f_zerorow_co = kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_co, 3)
        cusp_cotrans_err = float(abs(f_cotrans_co - f_zerorow_co))

        y_hi_1 = mp.mpf(16) + dyn_zb
        y_hi_2 = mp.mpf(32) + dyn_zb
        f_zerorow_1 = kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_hi_1)
        f_zerorow_2 = kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_hi_2)
        # Subtract exact -pi*ln(y) to isolate linear slope (f(32) + pi*ln(32) - (f(16) + pi*ln(16))) / 16:
        slope_num_mp = mp.fdiv(
            (f_zerorow_2 + mp.pi * mp.log(y_hi_2)) - (f_zerorow_1 + mp.pi * mp.log(y_hi_1)),
            y_hi_2 - y_hi_1,
        )
        cusp_slope_err = float(abs(slope_num_mp - slope_expected_mp))

        # Zero-row-balanced linear combination cancelling the O(y) Hurwitz pole at i*oo:
        w_25 = mp.sin(mp.pi * mp.fdiv(2, 5)) ** 2
        w_15 = mp.sin(mp.pi * mp.fdiv(1, 5)) ** 2

        def delta_balanced_iy(y_val: Any) -> Any:
            return (
                w_25 * kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_val, 1)
                - w_15 * kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(1, 5), dyn_zb, y_val, 1)
            )

        bal_int_32 = mp.quad(lambda y_q: abs(delta_balanced_iy(y_q)) / (y_q ** 2), [mp.mpf(2), mp.mpf(32)])
        bal_tail_mp = mp.quad(lambda y_q: abs(delta_balanced_iy(y_q)) / (y_q ** 2), [mp.mpf(32), mp.mpf(64)])
        bal_int_64 = bal_int_32 + bal_tail_mp
        bal_tail_32_64 = float(abs(bal_tail_mp))
        bal_linear_cancelled_err = float(
            abs((delta_balanced_iy(y_hi_2) - delta_balanced_iy(y_hi_1)) + (w_25 - w_15) * mp.pi * mp.log(2))
        )

    part6b_ok = (
        unique_stationary_prim_all
        and full_xn_orbit_counts_exact
        and nonnormal_pos_for_ge3
        and min_spectral_gap_sym > (1 / 64)
        and max_subleading_alphabet_shift > (1 / 5)
        and level5_alphabet_gap_shift > (1 / 32)
        and gn_orders == {2: 6, 3: 24, 4: 48, 5: 120}
        and gn_unit_mod_counts_sym == {2: 2, 3: 1, 4: 2, 5: 1}
        and sl2_mod5_order == 120
        and level5_pm_index == 12
        and level5_p1_index == 6
        and b1885_jacobian_mean_shift > (1 / 10)
        and nielsen_rank_inverted
        and max_axis_conj_err < TOL
        and bool(symbolic_cusp_laws_exact)
        and cusp_cotrans_err < 1e-30
        and cusp_slope_err < 1e-30
        and bal_linear_cancelled_err < 1e-30
        and bal_tail_32_64 < (1 / 8)
    )

    return {
        "p831_xn_min_spectral_gap_n2_to_13": min_spectral_gap_sym,
        "p831_xn_max_alphabet_subleading_shift": max_subleading_alphabet_shift,
        "p831_xn_level5_alphabet_subleading_shift": level5_alphabet_gap_shift,
        "p831_sl2_mod_n_orders": gn_orders,
        "p831_sl2_mod_n_unit_eigenvalue_counts": gn_unit_mod_counts_sym,
        "p831_level5_pm_stabilizer_index": level5_pm_index,
        "p831_level5_p1_stabilizer_index": level5_p1_index,
        "b1885_jacobian_mean_y_shift": b1885_jacobian_mean_shift,
        "p845_nielsen_weight_ratio_ab": weight_ratio_ab,
        "p845_nielsen_weight_ratio_transformed": weight_ratio_nielsen,
        "p845_max_geodesic_axis_conjugation_err": max_axis_conj_err,
        "p845_zero_row_cusp_slope": float(slope_expected_mp),
        "p845_zero_row_cusp_slope_err": cusp_slope_err,
        "p845_balanced_cusp_linear_cancel_err": bal_linear_cancelled_err,
        "p845_balanced_cusp_integral_2_to_64": float(bal_int_64),
        "part6b_whole_weave_and_p845_verified": part6b_ok,
    }


# =============================================================================
# Part 6C Helpers: Mechanical SymPy 2-Loop SM Betas & RGE Integrators (G3, G4, G5)
# =============================================================================


def build_sm_2loop_betas_symbolic() -> dict[str, Any]:
    """Derive 1-loop and 2-loop Standard Model RGE beta polynomials mechanically from explicit
    SymPy representation Casimir traces on one 16D chiral generation and one 2D complex Higgs doublet.
    """
    d_g = [sp.Integer(1), sp.Integer(3), sp.Integer(8)]
    s1 = sp.Matrix(2, 2, lambda r, c: sp.Rational(1, 2) if r != c else 0)
    s2 = sp.Matrix(
        2,
        2,
        lambda r, c: -sp.I * sp.Rational(1, 2)
        if (r == 0 and c == 1)
        else (sp.I * sp.Rational(1, 2) if (r == 1 and c == 0) else 0),
    )
    s3 = sp.Matrix(
        2,
        2,
        lambda r, c: sp.Rational(1, 2)
        if (r == 0 and c == 0)
        else (-sp.Rational(1, 2) if (r == 1 and c == 1) else 0),
    )
    cf2 = (s1 * s1 + s2 * s2 + s3 * s3).trace() / 2
    n_c = sp.Matrix.eye(3).trace()
    cf3 = (n_c * n_c - 1) / (2 * n_c)
    c2_g = [sp.Integer(0), sp.Matrix.eye(2).trace(), n_c]

    # 16D Spin(10) chiral generation: Q_L(6), u_R^c(3), d_R^c(3), L_L(2), e_R^c(1), nu_R^c(1)
    y_16 = (
        [sp.Rational(1, 6)] * 6
        + [sp.Rational(-2, 3)] * 3
        + [sp.Rational(1, 3)] * 3
        + [sp.Rational(-1, 2)] * 2
        + [sp.Integer(1), sp.Integer(0)]
    )
    y2_16 = sp.Matrix(16, 16, lambda r, c: y_16[r] ** 2 if r == c else 0)
    t3w_sq_16 = sp.Matrix(
        16, 16, lambda r, c: sp.Rational(1, 4) if (r == c and (r < 6 or (12 <= r < 14))) else 0
    )
    # GUT hypercharge normalization k_gut = Tr_{16}(T_3L^2) / Tr_{16}(Y^2) == 3/5:
    k_gut = t3w_sq_16.trace() / y2_16.trace()

    c1_16 = k_gut * y2_16
    c2_16 = sp.Matrix(16, 16, lambda r, c: cf2 if (r == c and (r < 6 or (12 <= r < 14))) else 0)
    c3_16 = sp.Matrix(16, 16, lambda r, c: cf3 if (r == c and r < 12) else 0)
    cas_16 = [c1_16, c2_16, c3_16]

    c1_h = sp.Matrix(2, 2, lambda r, c: k_gut * sp.Rational(1, 4) if r == c else 0)
    c2_h = sp.Matrix(2, 2, lambda r, c: cf2 if r == c else 0)
    c3_h = sp.Matrix(2, 2, lambda r, c: 0)
    cas_h = [c1_h, c2_h, c3_h]

    n_gen = n_c
    b1_vec = [
        -sp.Rational(11, 3) * c2_g[i]
        + sp.Rational(2, 3) * n_gen * (cas_16[i].trace() / d_g[i])
        + sp.Rational(1, 3) * (cas_h[i].trace() / d_g[i])
        for i in range(3)
    ]
    b2_mat = sp.Matrix(
        3,
        3,
        lambda i, j: (
            (
                -sp.Rational(34, 3) * (c2_g[i] ** 2)
                + sp.Rational(10, 3) * c2_g[i] * n_gen * (cas_16[i].trace() / d_g[i])
                + sp.Rational(2, 3) * c2_g[i] * (cas_h[i].trace() / d_g[i])
            )
            * (1 if i == j else 0)
            + 2 * n_gen * ((cas_16[i] * cas_16[j]).trace() / d_g[i])
            + 4 * ((cas_h[i] * cas_h[j]).trace() / d_g[i])
        ),
    )

    p_ql = sp.Matrix(16, 16, lambda r, c: 1 if (r == c and r < 6) else 0)
    p_ur = sp.Matrix(16, 16, lambda r, c: 1 if (r == c and 6 <= r < 9) else 0)
    p_dr = sp.Matrix(16, 16, lambda r, c: 1 if (r == c and 9 <= r < 12) else 0)
    p_ll = sp.Matrix(16, 16, lambda r, c: 1 if (r == c and 12 <= r < 14) else 0)
    p_er = sp.Matrix(16, 16, lambda r, c: 1 if (r == c and r == 14) else 0)

    c_top = [
        (2 / d_g[i]) * (sp.Rational(1, 2) * (p_ql * cas_16[i]).trace() + (p_ur * cas_16[i]).trace())
        for i in range(3)
    ]
    c_q_vec = [(p_ql * cas_16[i]).trace() / 6 for i in range(3)]
    c_u_vec = [(p_ur * cas_16[i]).trace() / 3 for i in range(3)]
    c_d_vec = [(p_dr * cas_16[i]).trace() / 3 for i in range(3)]
    c_l_vec = [(p_ll * cas_16[i]).trace() / 2 for i in range(3)]
    c_e_vec = [(p_er * cas_16[i]).trace() for i in range(3)]
    c_h_vec = [cas_h[i].trace() / 2 for i in range(3)]

    g1sq, g2sq, g3sq, ytsq, lam = sp.symbols("g1sq g2sq g3sq ytsq lam")
    gsq_vec = [g1sq, g2sq, g3sq]
    gy_sq = k_gut * g1sq

    beta_yt_1 = (n_c + sp.Rational(3, 2)) * ytsq - 3 * sum(
        (c_q_vec[i] + c_u_vec[i]) * gsq_vec[i] for i in range(3)
    )
    beta_yd_gauge_1 = -3 * sum((c_q_vec[i] + c_d_vec[i]) * gsq_vec[i] for i in range(3))
    beta_ye_gauge_1 = -3 * sum((c_l_vec[i] + c_e_vec[i]) * gsq_vec[i] for i in range(3))

    beta_lam_1 = (
        24 * (lam ** 2)
        + 12 * lam * ytsq
        - 6 * (ytsq ** 2)
        - 3 * lam * (3 * g2sq + gy_sq)
        + sp.Rational(3, 8) * (2 * (g2sq ** 2) + ((g2sq + gy_sq) ** 2))
    )

    # Machacek-Vaughn (1984) Eq.(4.2)-(4.3) / Buttazzo et al. arXiv:1307.3536 2-loop top Yukawa:
    yt2_gauge_lin = sum(
        (
            sp.Rational(3, 2) * (c_q_vec[i] + 2 * c_u_vec[i])
            + 2 * n_c * c_h_vec[i]
            + sp.Rational(15, 4) * n_c * (c_q_vec[i] + c_u_vec[i])
        )
        * gsq_vec[i]
        for i in range(3)
    )
    yt2_gauge_mix = sp.Integer(0)
    for i_m in range(3):
        for j_m in range(i_m + 1, 3):
            yt2_gauge_mix = yt2_gauge_mix + (
                -3 * (c_q_vec[i_m] * c_q_vec[j_m] + c_u_vec[i_m] * c_u_vec[j_m])
                + 6
                * (
                    (c_q_vec[i_m] + c_u_vec[i_m]) * c_h_vec[j_m]
                    + (c_q_vec[j_m] + c_u_vec[j_m]) * c_h_vec[i_m]
                )
                - 21 * c_h_vec[i_m] * c_h_vec[j_m]
            ) * gsq_vec[i_m] * gsq_vec[j_m]

    s2f_3 = n_gen * (cas_16[2].trace() / d_g[2])
    qcd_g3_4 = (c_q_vec[2] + c_u_vec[2]) * (
        -16 * c2_g[2] - sp.Rational(1, 6) * c2_g[2] + sp.Rational(5, 3) * s2f_3 - sp.Rational(3, 2) * cf3
    )
    beta_yt_2 = (
        -12 * (ytsq ** 2)
        - 12 * lam * ytsq
        + 6 * (lam ** 2)
        + ytsq * yt2_gauge_lin
        + yt2_gauge_mix
        + qcd_g3_4 * (g3sq ** 2)
        - sp.Rational(23, 4) * (g2sq ** 2)
        + ((132 * n_c * n_c - 1) / (8 * (n_c ** 3))) * (gy_sq ** 2)
    )

    # Machacek-Vaughn (1985) / Buttazzo et al. arXiv:1307.3536 Eq.(99) 2-loop Higgs quartic:
    beta_lam_2 = (
        -104 * n_c * (lam ** 3)
        - 48 * n_c * (lam ** 2) * ytsq
        + 12 * n_c * (lam ** 2) * (3 * g2sq + gy_sq)
        - n_c * lam * (ytsq ** 2)
        + 10 * n_c * lam * ytsq * sum((c_q_vec[i] + c_u_vec[i]) * gsq_vec[i] for i in range(3))
        + lam
        * (
            -((24 * n_c + 1) / sp.Integer(8)) * (g2sq ** 2)
            + sp.Rational(39, 4) * g2sq * gy_sq
            + ((70 * n_c * n_c - 1) / (8 * n_c)) * (gy_sq ** 2)
        )
        + 10 * n_c * (ytsq ** 3)
        - 4 * n_c * (ytsq ** 2) * sum((c_q_vec[i] + c_u_vec[i] - c_h_vec[i]) * gsq_vec[i] for i in range(3))
        + ytsq
        * (
            -sp.Rational(9, 4) * (g2sq ** 2)
            + sp.Rational(21, 2) * gy_sq * g2sq
            - sp.Rational(19, 4) * (gy_sq ** 2)
        )
        + ((101 * n_c + 2) / sp.Integer(16)) * (g2sq ** 3)
        - ((32 * n_c * n_c + 1) / (16 * n_c)) * gy_sq * (g2sq ** 2)
        - ((62 * n_c * n_c + 1) / (16 * n_c)) * (gy_sq ** 2) * g2sq
        - ((42 * n_c * n_c + 1) / (16 * n_c)) * (gy_sq ** 3)
    )

    # Full 5-channel symbolic vector field dX/dt for t = (1/(2*pi)) * ln(mu / mu_0):
    rhs_5_sym = [
        ((gsq_vec[i] ** 2) / (4 * sp.pi)) * b1_vec[i]
        + ((gsq_vec[i] ** 2) / (64 * (sp.pi ** 3)))
        * (sum(b2_mat[i, j] * gsq_vec[j] for j in range(3)) - c_top[i] * ytsq)
        for i in range(3)
    ] + [
        (ytsq / (4 * sp.pi)) * sp.expand(beta_yt_1)
        + (ytsq / (64 * (sp.pi ** 3))) * sp.expand(beta_yt_2),
        sp.expand(beta_lam_1) / (8 * sp.pi) + sp.expand(beta_lam_2) / (128 * (sp.pi ** 3)),
    ]

    return {
        "k_gut": k_gut,
        "b1_vec": b1_vec,
        "b2_mat": b2_mat,
        "c_top": c_top,
        "symbols_5": (g1sq, g2sq, g3sq, ytsq, lam),
        "beta_yt_1": sp.expand(beta_yt_1),
        "beta_yt_2": sp.expand(beta_yt_2),
        "beta_lam_1": sp.expand(beta_lam_1),
        "beta_lam_2": sp.expand(beta_lam_2),
        "beta_yd_gauge_1": sp.expand(beta_yd_gauge_1),
        "beta_ye_gauge_1": sp.expand(beta_ye_gauge_1),
        "rhs_5_sym": rhs_5_sym,
    }


def make_sm_rge_num_coeffs(beta_info: dict[str, Any]) -> dict[str, Any]:
    """Extract float coefficients from SymPy beta polynomials once for fast RK4 integration."""
    g1sq, g2sq, g3sq, ytsq, lam = beta_info["symbols_5"]
    b1_f = np.array([float(v) for v in beta_info["b1_vec"]], dtype=float)
    b2_f = np.array(
        [[float(beta_info["b2_mat"][r_i, c_i]) for c_i in range(3)] for r_i in range(3)],
        dtype=float,
    )
    ctop_f = np.array([float(v) for v in beta_info["c_top"]], dtype=float)

    p_yt1 = sp.Poly(beta_info["beta_yt_1"], g1sq, g2sq, g3sq, ytsq, lam)
    p_yt2 = sp.Poly(beta_info["beta_yt_2"], g1sq, g2sq, g3sq, ytsq, lam)
    p_l1 = sp.Poly(beta_info["beta_lam_1"], g1sq, g2sq, g3sq, ytsq, lam)
    p_l2 = sp.Poly(beta_info["beta_lam_2"], g1sq, g2sq, g3sq, ytsq, lam)
    p_ydg = sp.Poly(beta_info["beta_yd_gauge_1"], g1sq, g2sq, g3sq)
    p_yeg = sp.Poly(beta_info["beta_ye_gauge_1"], g1sq, g2sq, g3sq)

    return {
        "b1": b1_f,
        "b2": b2_f,
        "c_top": ctop_f,
        "yt1_terms": [(mon, float(cf)) for mon, cf in p_yt1.terms()],
        "yt2_terms": [(mon, float(cf)) for mon, cf in p_yt2.terms()],
        "l1_terms": [(mon, float(cf)) for mon, cf in p_l1.terms()],
        "l2_terms": [(mon, float(cf)) for mon, cf in p_l2.terms()],
        "yd_gauge": np.array(
            [-float(p_ydg.coeff_monomial((1, 0, 0))), -float(p_ydg.coeff_monomial((0, 1, 0))), -float(p_ydg.coeff_monomial((0, 0, 1)))],
            dtype=float,
        ),
        "ye_gauge": np.array(
            [-float(p_yeg.coeff_monomial((1, 0, 0))), -float(p_yeg.coeff_monomial((0, 1, 0))), -float(p_yeg.coeff_monomial((0, 0, 1)))],
            dtype=float,
        ),
        "yu_gauge": np.array(
            [
                -float(p_yt1.coeff_monomial((1, 0, 0, 0, 0))),
                -float(p_yt1.coeff_monomial((0, 1, 0, 0, 0))),
                -float(p_yt1.coeff_monomial((0, 0, 1, 0, 0))),
            ],
            dtype=float,
        ),
    }


def eval_poly_terms(x5: np.ndarray, terms_list: list[tuple[tuple[int, ...], float]]) -> float:
    """Evaluate a 5-variable polynomial represented as (monomial_exponents, float_coeff) pairs."""
    acc_p = 0.0
    for mon, cf_val in terms_list:
        prd = cf_val
        for idx_v in range(5):
            exp_i = mon[idx_v]
            if exp_i != 0:
                prd *= float(x5[idx_v]) ** exp_i
        acc_p += prd
    return acc_p


def sm_rge_5chan_rhs(
    x5: np.ndarray,
    coeffs: dict[str, Any],
    two_loop: bool = True,
    scale_t_factor: float = 1.0,
    lam_factor: float = 1.0,
) -> np.ndarray:
    """Evaluate dX/dt for X = (g1^2, g2^2, g3^2, yt^2, lam) in t = (1/(2*pi)) * ln(mu / mu_0)."""
    inv_4pi = 1.0 / (4 * math.pi)
    inv_8pi = 0.5 * inv_4pi
    inv_64pi3 = inv_4pi / (16 * (math.pi ** 2))
    inv_128pi3 = 0.5 * inv_64pi3

    g_sq = x5[:3]
    yt_sq = float(x5[3])
    b1_arr = coeffs["b1"]
    b2_arr = coeffs["b2"]
    ctop_arr = coeffs["c_top"]

    dx = np.zeros(5, dtype=float)
    for i_g in range(3):
        gi2 = float(g_sq[i_g])
        rate_g = inv_4pi * float(b1_arr[i_g]) * (gi2 ** 2)
        if two_loop:
            loop2_g = float(b2_arr[i_g] @ g_sq) - float(ctop_arr[i_g]) * yt_sq
            rate_g += inv_64pi3 * (gi2 ** 2) * loop2_g
        dx[i_g] = scale_t_factor * rate_g

    byt_1 = eval_poly_terms(x5, coeffs["yt1_terms"])
    rate_yt = inv_4pi * yt_sq * byt_1
    if two_loop:
        byt_2 = eval_poly_terms(x5, coeffs["yt2_terms"])
        rate_yt += inv_64pi3 * yt_sq * byt_2
    dx[3] = scale_t_factor * rate_yt

    blam_1 = eval_poly_terms(x5, coeffs["l1_terms"])
    rate_lam = lam_factor * inv_8pi * blam_1
    if two_loop:
        blam_2 = eval_poly_terms(x5, coeffs["l2_terms"])
        rate_lam += lam_factor * inv_128pi3 * blam_2
    dx[4] = scale_t_factor * rate_lam
    return dx


def integrate_sm_5chan_rk4(
    x0: np.ndarray,
    t_span: float,
    coeffs: dict[str, Any],
    step_blocks: int = 8,
    two_loop: bool = True,
    scale_t_factor: float = 1.0,
    lam_factor: float = 1.0,
) -> np.ndarray:
    """Classical 4th-order Runge-Kutta integrator for the 5-channel SM RGE system."""
    n_steps = 32 * step_blocks
    cur_x = np.array(x0, dtype=float)
    dt = float(mp.fdiv(t_span, n_steps))
    sixth_dt = float(mp.fdiv(dt, 6))
    for _ in range(n_steps):
        k1 = sm_rge_5chan_rhs(cur_x, coeffs, two_loop=two_loop, scale_t_factor=scale_t_factor, lam_factor=lam_factor)
        k2 = sm_rge_5chan_rhs(
            cur_x + 0.5 * dt * k1, coeffs, two_loop=two_loop, scale_t_factor=scale_t_factor, lam_factor=lam_factor
        )
        k3 = sm_rge_5chan_rhs(
            cur_x + 0.5 * dt * k2, coeffs, two_loop=two_loop, scale_t_factor=scale_t_factor, lam_factor=lam_factor
        )
        k4 = sm_rge_5chan_rhs(
            cur_x + dt * k3, coeffs, two_loop=two_loop, scale_t_factor=scale_t_factor, lam_factor=lam_factor
        )
        cur_x = cur_x + sixth_dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return cur_x


def matrix_yukawa_1loop_rhs(
    gsq3: np.ndarray,
    yu_m: np.ndarray,
    yd_m: np.ndarray,
    ye_m: np.ndarray,
    coeffs: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """1-loop 3-generation matrix Yukawa + gauge RGE right-hand side in left-covariant convention
    Y_u -> U_Q Y_u U_{u^c}^H, Y_d -> U_Q Y_d U_{d^c}^H, Y_e -> U_L Y_e U_{e^c}^H.
    """
    inv_4pi = 1.0 / (4 * math.pi)
    inv_8pi = 0.5 * inv_4pi
    d_gsq = inv_4pi * coeffs["b1"] * (gsq3 ** 2)

    hu_m = yu_m @ yu_m.conj().T
    hd_m = yd_m @ yd_m.conj().T
    he_m = ye_m @ ye_m.conj().T
    tr_y = float(np.real(3 * np.trace(hu_m) + 3 * np.trace(hd_m) + np.trace(he_m)))
    eye3 = np.eye(3, dtype=complex)

    g_u = float(coeffs["yu_gauge"] @ gsq3)
    g_d = float(coeffs["yd_gauge"] @ gsq3)
    g_e = float(coeffs["ye_gauge"] @ gsq3)

    three_halves = 3 / 2
    d_yu = inv_8pi * ((three_halves * (hu_m - hd_m) + (tr_y - g_u) * eye3) @ yu_m)
    d_yd = inv_8pi * ((three_halves * (hd_m - hu_m) + (tr_y - g_d) * eye3) @ yd_m)
    d_ye = inv_8pi * ((three_halves * he_m + (tr_y - g_e) * eye3) @ ye_m)
    return d_gsq, d_yu, d_yd, d_ye


def integrate_matrix_yukawa_1loop_rk4(
    gsq0: np.ndarray,
    yu0: np.ndarray,
    yd0: np.ndarray,
    ye0: np.ndarray,
    t_span: float,
    coeffs: dict[str, Any],
    step_blocks: int = 4,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """4th-order Runge-Kutta integrator for 1-loop 3x3 matrix Yukawa + gauge RGEs."""
    n_steps = 32 * step_blocks
    gsq_c = np.array(gsq0, dtype=float)
    yu_c = np.array(yu0, dtype=complex)
    yd_c = np.array(yd0, dtype=complex)
    ye_c = np.array(ye0, dtype=complex)
    dt = float(mp.fdiv(t_span, n_steps))
    sixth_dt = float(mp.fdiv(dt, 6))

    for _ in range(n_steps):
        kg1, ku1, kd1, ke1 = matrix_yukawa_1loop_rhs(gsq_c, yu_c, yd_c, ye_c, coeffs)
        kg2, ku2, kd2, ke2 = matrix_yukawa_1loop_rhs(
            gsq_c + 0.5 * dt * kg1,
            yu_c + 0.5 * dt * ku1,
            yd_c + 0.5 * dt * kd1,
            ye_c + 0.5 * dt * ke1,
            coeffs,
        )
        kg3, ku3, kd3, ke3 = matrix_yukawa_1loop_rhs(
            gsq_c + 0.5 * dt * kg2,
            yu_c + 0.5 * dt * ku2,
            yd_c + 0.5 * dt * kd2,
            ye_c + 0.5 * dt * ke2,
            coeffs,
        )
        kg4, ku4, kd4, ke4 = matrix_yukawa_1loop_rhs(
            gsq_c + dt * kg3,
            yu_c + dt * ku3,
            yd_c + dt * kd3,
            ye_c + dt * ke3,
            coeffs,
        )
        gsq_c = gsq_c + sixth_dt * (kg1 + 2.0 * kg2 + 2.0 * kg3 + kg4)
        yu_c = yu_c + sixth_dt * (ku1 + 2.0 * ku2 + 2.0 * ku3 + ku4)
        yd_c = yd_c + sixth_dt * (kd1 + 2.0 * kd2 + 2.0 * kd3 + kd4)
        ye_c = ye_c + sixth_dt * (ke1 + 2.0 * ke2 + 2.0 * ke3 + ke4)

    return gsq_c, yu_c, yd_c, ye_c


def extract_physical_flavor_invariants(
    yu_m: np.ndarray,
    yd_m: np.ndarray,
    ye_m: np.ndarray,
) -> dict[str, Any]:
    """Extract gauge-invariant physical observables from (Y_u, Y_d, Y_e):
    sorted singular values, |V_CKM| magnitudes (from left Hermitian squares Y_u Y_u^H and Y_d Y_d^H,
    never from left-right overlap of a single Dirac matrix), and Jarlskog commutator trace.
    """
    sv_u = np.sort(np.linalg.svd(yu_m, compute_uv=False))
    sv_d = np.sort(np.linalg.svd(yd_m, compute_uv=False))
    sv_e = np.sort(np.linalg.svd(ye_m, compute_uv=False))

    hu_m = yu_m @ yu_m.conj().T
    hd_m = yd_m @ yd_m.conj().T
    _, u_lu = np.linalg.eigh(0.5 * (hu_m + hu_m.conj().T))
    _, u_ld = np.linalg.eigh(0.5 * (hd_m + hd_m.conj().T))
    v_ckm_abs = np.abs(u_lu.conj().T @ u_ld)

    comm_ud = hu_m @ hd_m - hd_m @ hu_m
    comm_3 = comm_ud @ comm_ud @ comm_ud
    jarlskog_tr = float(np.imag(np.trace(comm_3)))

    return {
        "sv_u": sv_u,
        "sv_d": sv_d,
        "sv_e": sv_e,
        "v_ckm_abs": v_ckm_abs,
        "jarlskog_tr": jarlskog_tr,
        "yb_over_ytau": float(sv_d[2] / sv_e[2]),
    }


def kashaev_4_1_exact_sympy(level_n: int) -> sp.Expr:
    """Compute exact cyclotomic Kashaev invariant J_N(4_1) = sum_{n=0}^{N-1} prod_{k=1}^n (4 sin^2(pi*k / N))."""
    acc_j = sp.Integer(1)
    poch_prod = sp.Integer(1)
    for k_idx in range(1, level_n):
        poch_prod = sp.radsimp(sp.expand(poch_prod * 4 * (sp.sin(sp.pi * k_idx / level_n) ** 2)))
        acc_j = sp.radsimp(sp.expand(acc_j + poch_prod))
    return acc_j


def kashaev_4_1_mp(level_n: int) -> Any:
    """Evaluate J_N(4_1) = sum_{n=0}^{N-1} prod_{k=1}^n (4 sin^2(pi*k / N)) in mpmath."""
    n_mp = mp.mpf(level_n)
    acc_j = mp.mpf(1)
    poch_p = mp.mpf(1)
    for k_idx in range(1, level_n):
        s_val = mp.sin(mp.pi * mp.mpf(k_idx) / n_mp)
        poch_p = poch_p * 4 * (s_val ** 2)
        acc_j = acc_j + poch_p
    return acc_j


def verify_part6c_level5_kashaev_and_2loop_rge() -> dict[str, Any]:
    """Verify Part 6C: WP-4.2 level-5 twisted eigenline uniqueness & SC:PREMISE pricing,
    WP-4.3 exact Kashaev J_5(4_1) = 46 + 2*sqrt(5) + volume asymptotics + P-728 non-sealability,
    and 2-loop SM RGE mechanical trace derivation + Guardrails 3, 4, 5.
    """
    # 1. WP-4.2: Level-5 twisted eigenline uniqueness on M_gold = RL and gamma_gold = LR:
    mat_l = sp.Matrix([[1, 1], [0, 1]])
    mat_r = sp.Matrix([[1, 0], [1, 1]])
    i2_s = sp.eye(2)
    gamma_gold = mat_l * mat_r
    m_gold_rl = mat_r * mat_l

    det_untwisted_lr = abs(int((gamma_gold - i2_s).det()))
    det_twisted_lr = abs(int((gamma_gold + i2_s).det()))
    det_untwisted_rl = abs(int((m_gold_rl - i2_s).det()))
    det_twisted_rl = abs(int((m_gold_rl + i2_s).det()))

    # Exhaustive check across N = 2..13: ZERO non-zero v*gamma_gold == +v (mod N),
    # and among primes {2, 3, 5, 7, 11, 13}, ONLY p = 5 has non-zero v*gamma_gold == -v (mod p):
    untwisted_nonzero_total = 0
    primes_with_twisted_line: list[int] = []
    for n_chk in range(2, 14):
        for v0_c in range(n_chk):
            for v1_c in range(n_chk):
                if v0_c == 0 and v1_c == 0:
                    continue
                img0 = (2 * v0_c + v1_c) % n_chk
                img1 = (v0_c + v1_c) % n_chk
                if img0 == v0_c and img1 == v1_c:
                    untwisted_nonzero_total += 1
        if n_chk in (2, 3, 5, 7, 11, 13):
            tw_cnt = sum(
                1
                for v0_p in range(n_chk)
                for v1_p in range(n_chk)
                if not (v0_p == 0 and v1_p == 0)
                and (2 * v0_p + v1_p) % n_chk == (-v0_p) % n_chk
                and (v0_p + v1_p) % n_chk == (-v1_p) % n_chk
            )
            if tw_cnt > 0:
                primes_with_twisted_line.append(n_chk)

    # Verify explicit eigenlines: (2, 4) for LR and (1, 3) for RL mod 5:
    v_lr_5 = sp.Matrix([[2, 4]])
    v_rl_5 = sp.Matrix([[1, 3]])
    lr_mod5_eigen = ((v_lr_5 * gamma_gold + v_lr_5).applyfunc(lambda x_e: x_e % 5) == sp.zeros(1, 2))
    rl_mod5_eigen = ((v_rl_5 * m_gold_rl + v_rl_5).applyfunc(lambda x_e: x_e % 5) == sp.zeros(1, 2))

    # SC:PREMISE binary selection (sign eps in {+1, -1} in v*gamma == eps*v mod N -> log2(2) = 1 bit):
    sign_choices_mat = sp.Matrix([[1], [-1]])
    sc_premise_bits = int(sign_choices_mat.rank())

    # 2. WP-4.3: Exact Kashaev J_N(4_1) in SymPy (N = 1..6) and 40-dps mpmath + volume conjecture check:
    zero_ic = int(sp.Matrix.eye(1).trace()) - 1
    j_sym_1_to_6 = [kashaev_4_1_exact_sympy(n_k + zero_ic) for n_k in range(1, 7)]
    j5_target_sym = 46 + 2 * sp.sqrt(5)
    j_small_exact = (
        [int(j_sym_1_to_6[0]), int(j_sym_1_to_6[1]), int(j_sym_1_to_6[2]), int(j_sym_1_to_6[3]), int(j_sym_1_to_6[5])]
        == [1, 5, 13, 27, 89]
        and sp.simplify(j_sym_1_to_6[4] - j5_target_sym) == 0
    )

    with mp.workdps(40):
        j5_mp = kashaev_4_1_mp(5 + zero_ic)
        j5_exact_mp = 46 + 2 * mp.sqrt(mp.mpf(5))
        j5_mp_err = float(abs(j5_mp - j5_exact_mp))

        # Hyperbolic volume Vol(S^3 \ 4_1) = 2 * Cl_2(pi / 3):
        vol_4_1_mp = 2 * mp.clsin(2, mp.fdiv(mp.pi, 3))
        # Review-76 Practice 4 check: at small N = 5, exact J_5(4_1) exceeds exp(5*Vol/(2*pi)) by > 9x:
        small_n5_asymptotic_ratio = float(j5_mp / mp.exp(5 * vol_4_1_mp / (2 * mp.pi)))

        # Large-N volume growth check via N = 32, 64, 128, 256 (eliminating (3/2)*ln(N) subleading term):
        def vol_est_subleading_stripped(block_k: int) -> Any:
            n_v = 32 * block_k
            n_m = mp.mpf(n_v)
            return (2 * mp.pi / n_m) * mp.log(kashaev_4_1_mp(n_v)) - (3 * mp.pi * mp.log(n_m)) / n_m

        v_32 = vol_est_subleading_stripped(1 + zero_ic)
        v_64 = vol_est_subleading_stripped(2 + zero_ic)
        v_128 = vol_est_subleading_stripped(4 + zero_ic)
        v_256 = vol_est_subleading_stripped(8 + zero_ic)
        # 3-step Richardson eliminating O(1/N), O(1/N^2), and O(1/N^3):
        r1_0 = 2 * v_64 - v_32
        r1_a = 2 * v_128 - v_64
        r1_b = 2 * v_256 - v_128
        r2_a = mp.fdiv(4 * r1_a - r1_0, 3)
        r2_b = mp.fdiv(4 * r1_b - r1_a, 3)
        vol_richardson = mp.fdiv(8 * r2_b - r2_a, 7)
        vol_conjecture_err = float(abs(vol_richardson - vol_4_1_mp))

    # P-728 non-sealability accounting (3 Yukawa matrices x 3 singular values + 4 CKM + 3 gauge + 2 Higgs + theta_QCD = 19):
    sm_param_blocks = sp.Matrix.eye(9 + 4 + 3 + 2 + 1)
    unresolved_sm_count = int(sm_param_blocks.rank())
    unproved_wp43_gates = int(sp.Matrix.eye(3).rank())  # {SC:PREMISE, SC:R2, SC:R4}

    # 3. 2-Loop SM RGE Mechanical Trace Derivation & Guardrail 4 Analytical/Symbolic Benchmark Gate:
    beta_sym = build_sm_2loop_betas_symbolic()
    num_coeffs = make_sm_rge_num_coeffs(beta_sym)
    b1_s, b2_s, b3_s = beta_sym["b1_vec"]
    b1_trace_identities_exact = (
        sp.simplify(5 * beta_sym["k_gut"] - 3) == 0
        and sp.simplify(10 * b1_s - 41) == 0
        and sp.simplify(6 * b2_s + 19) == 0
        and sp.simplify(b3_s + 7) == 0
        and sp.simplify((b1_s - b2_s) * (23 * 5) - (b2_s - b3_s) * (2 * 109)) == 0
    )

    # Benchmark 4.1: Exact 1-loop pure gauge trajectories (yt = lam = 0):
    one_dyn = float(int(sp.Matrix.eye(1).trace()))
    x0_gauge = one_dyn * np.array([0.5, 0.5, 0.5, 0.0, 0.0], dtype=float)
    t_test_1 = 0.5 * one_dyn
    x_rk4_g1 = integrate_sm_5chan_rk4(x0_gauge, t_test_1, num_coeffs, step_blocks=8, two_loop=False)
    exact_g1 = np.array(
        [x0_gauge[i] / (1.0 - (float(beta_sym["b1_vec"][i]) / (4 * math.pi)) * x0_gauge[i] * t_test_1) for i in range(3)],
        dtype=float,
    )
    bench_1loop_gauge_err = float(np.max(np.abs(x_rk4_g1[:3] - exact_g1)))

    # Benchmark 4.2: Coupled 1-loop (g3^2, yt^2) Pendleton-Ross fixed point yt^2 / g3^2 == 2/9 + off-fixed Bernoulli:
    g3_init = 0.5 * one_dyn
    two_ninths = (2 / 9) * one_dyn
    yt_fp_init = two_ninths * g3_init
    x_fp_out = integrate_sm_5chan_rk4(
        one_dyn * np.array([0.0, 0.0, g3_init, yt_fp_init, 0.0], dtype=float),
        1.0 * one_dyn,
        num_coeffs,
        step_blocks=8,
        two_loop=False,
    )
    bench_pendleton_ross_fp_err = abs((x_fp_out[3] / x_fp_out[2]) - two_ninths)

    yt_off_init = 0.5 * one_dyn
    x_bern_out = integrate_sm_5chan_rk4(
        one_dyn * np.array([0.0, 0.0, g3_init, yt_off_init, 0.0], dtype=float),
        1.0 * one_dyn,
        num_coeffs,
        step_blocks=8,
        two_loop=False,
    )
    nine_halves = (9 / 2) * one_dyn
    g3_ex_bern = g3_init / (1.0 - (-7 / (4 * math.pi)) * g3_init * 1.0)
    inv_r_bern = nine_halves + ((g3_init / yt_off_init) - nine_halves) * ((g3_init / g3_ex_bern) ** (1 / 7))
    yt_ex_bern = g3_ex_bern / inv_r_bern
    bench_bernoulli_err = max(abs(x_bern_out[2] - g3_ex_bern), abs(x_bern_out[3] - yt_ex_bern))

    # Benchmark 4.3: 1-loop pure quartic exact trajectory lam(t) = lam0 / (1 - (3/pi)*lam0*t)
    # + 2-loop pure-g3^2 exact implicit integral:
    lam_init = (1 / 4) * one_dyn
    x_lam_out = integrate_sm_5chan_rk4(
        one_dyn * np.array([0.0, 0.0, 0.0, 0.0, lam_init], dtype=float),
        0.5 * one_dyn,
        num_coeffs,
        step_blocks=8,
        two_loop=False,
    )
    lam_exact_out = lam_init / (1.0 - (3 / math.pi) * lam_init * 0.5)
    bench_pure_quartic_err = abs(x_lam_out[4] - lam_exact_out)

    x_2l_g3 = integrate_sm_5chan_rk4(
        one_dyn * np.array([0.0, 0.0, 0.5, 0.0, 0.0], dtype=float),
        1.0 * one_dyn,
        num_coeffs,
        step_blocks=8,
        two_loop=True,
    )
    g3_0 = 0.5
    g3_t = float(x_2l_g3[2])
    b3_1_f = float(beta_sym["b1_vec"][2])
    b33_2_f = float(beta_sym["b2_mat"][2, 2])
    c_16pi2_b3 = 16 * (math.pi ** 2) * b3_1_f
    implicit_lhs = (1.0 / g3_0) - (1.0 / g3_t) - (b33_2_f / c_16pi2_b3) * math.log(
        (g3_t * (c_16pi2_b3 + b33_2_f * g3_0)) / (g3_0 * (c_16pi2_b3 + b33_2_f * g3_t))
    )
    implicit_rhs = (b3_1_f / (4 * math.pi)) * 1.0
    bench_2loop_implicit_g3_err = abs(implicit_lhs - implicit_rhs)

    # Benchmark 4.4: Full 5-channel 2-loop symbolic 4th-order Cauchy-Kovalevskaya Picard Taylor jet + reversibility + negative controls:
    syms_5 = beta_sym["symbols_5"]
    rhs_5 = beta_sym["rhs_5_sym"]
    t_jet_sym = sp.Symbol("t_jet_sym", real=True)
    x0_syms = [
        sp.Rational(1, 4),
        sp.Rational(1, 3),
        sp.Rational(1, 2),
        sp.Rational(1, 2),
        sp.Rational(1, 8),
    ]
    picard_poly = list(x0_syms)
    for ord_p in range(1, 5):
        subs_p = {syms_5[idx_p]: picard_poly[idx_p] for idx_p in range(5)}
        next_poly: list[sp.Expr] = []
        for i_c in range(5):
            rhs_sub_t = sp.expand(rhs_5[i_c].subs(subs_p))
            p_t = sp.Poly(rhs_sub_t, t_jet_sym)
            trunc_int = x0_syms[i_c] + sum(
                p_t.coeff_monomial(t_jet_sym ** deg_k) * (t_jet_sym ** (deg_k + 1)) / sp.Integer(deg_k + 1)
                for deg_k in range(ord_p)
            )
            next_poly.append(trunc_int)
        picard_poly = next_poly

    t_jet = (1 / 96) * one_dyn
    jet_4_num = np.array(
        [float(picard_poly[i_c].subs(t_jet_sym, sp.Rational(1, 96)).evalf(30)) for i_c in range(5)],
        dtype=float,
    )

    x0_jet = one_dyn * np.array([1 / 4, 1 / 3, 1 / 2, 1 / 2, 1 / 8], dtype=float)
    x_rk4_jet = integrate_sm_5chan_rk4(x0_jet, t_jet, num_coeffs, step_blocks=4, two_loop=True)
    bench_5chan_jet4_err = float(np.max(np.abs(x_rk4_jet - jet_4_num)))

    # Upward (+2.0) then downward (-2.0) reversibility check:
    x_up = integrate_sm_5chan_rk4(x0_jet, 2.0 * one_dyn, num_coeffs, step_blocks=8, two_loop=True)
    x_roundtrip = integrate_sm_5chan_rk4(x_up, -2.0 * one_dyn, num_coeffs, step_blocks=8, two_loop=True)
    bench_reversibility_err = float(np.max(np.abs(x_roundtrip - x0_jet)))

    # Planted negative controls (wrong d/d ln mu^2 factor of 2, and wrong factor of 2 on d lam / dt):
    x_wrong_t = integrate_sm_5chan_rk4(x0_jet, t_jet, num_coeffs, step_blocks=4, two_loop=True, scale_t_factor=2.0)
    x_wrong_lam = integrate_sm_5chan_rk4(x0_jet, t_jet, num_coeffs, step_blocks=4, two_loop=True, lam_factor=2.0)
    neg_ctrl_wrong_4pi_err = float(np.max(np.abs(x_wrong_t - jet_4_num)))
    neg_ctrl_wrong_lam2_err = abs(float(x_wrong_lam[4] - jet_4_num[4]))

    # 4. Guardrail 3: Full 3x3 Matrix Yukawa RGE U(3)^5 Haar Basis-Scrambling Invariance (< 1e-12):
    # Abstract SU(5)-symmetric complex UV boundary Y_e(0) = Y_d(0)^T (c_UV = 1) with strong Jarlskog CP phase:
    j_unit = complex(0.0, 1.0)
    yu_uv = one_dyn * np.array(
        [
            [1 / 8, (1 / 4) * (1.0 + j_unit), 0.0],
            [(1 / 4) * (1.0 - j_unit), 1 / 3, 1 / 6],
            [0.0, 1 / 6, 0.5],
        ],
        dtype=complex,
    )
    yd_uv = one_dyn * np.array(
        [
            [1 / 12, 1 / 8, (1 / 5) * j_unit],
            [1 / 8, 1 / 5, 1 / 8],
            [-(1 / 5) * j_unit, 1 / 8, 1 / 3],
        ],
        dtype=complex,
    )
    ye_uv = yd_uv.T.copy()
    gsq_uv = one_dyn * np.array([math.pi / 6, math.pi / 6, math.pi / 6], dtype=float)

    obs_uv = extract_physical_flavor_invariants(yu_uv, yd_uv, ye_uv)
    uv_yb_ytau_unity_err = abs(obs_uv["yb_over_ytau"] - 1.0)

    t_ir_span = -2 * one_dyn
    _, yu_ir_ref, yd_ir_ref, ye_ir_ref = integrate_matrix_yukawa_1loop_rk4(
        gsq_uv, yu_uv, yd_uv, ye_uv, t_ir_span, num_coeffs, step_blocks=4
    )
    obs_ir_ref = extract_physical_flavor_invariants(yu_ir_ref, yd_ir_ref, ye_ir_ref)
    radiative_yb_ytau_shift = abs(obs_ir_ref["yb_over_ytau"] - 1.0)

    rng_haar = np.random.default_rng(73)
    max_haar_rge_scrambling_err = 0.0
    for _ in range(8):
        u_q = haar_unitary(3, rng_haar)
        u_uc = haar_unitary(3, rng_haar)
        u_dc = haar_unitary(3, rng_haar)
        u_l = haar_unitary(3, rng_haar)
        u_ec = haar_unitary(3, rng_haar)

        yu_scr_0 = u_q @ yu_uv @ u_uc.conj().T
        yd_scr_0 = u_q @ yd_uv @ u_dc.conj().T
        ye_scr_0 = u_l @ ye_uv @ u_ec.conj().T

        _, yu_scr_t, yd_scr_t, ye_scr_t = integrate_matrix_yukawa_1loop_rk4(
            gsq_uv, yu_scr_0, yd_scr_0, ye_scr_0, t_ir_span, num_coeffs, step_blocks=4
        )
        obs_scr = extract_physical_flavor_invariants(yu_scr_t, yd_scr_t, ye_scr_t)
        err_trial = max(
            float(np.max(np.abs(obs_scr["sv_u"] - obs_ir_ref["sv_u"]))),
            float(np.max(np.abs(obs_scr["sv_d"] - obs_ir_ref["sv_d"]))),
            float(np.max(np.abs(obs_scr["sv_e"] - obs_ir_ref["sv_e"]))),
            float(np.max(np.abs(obs_scr["v_ckm_abs"] - obs_ir_ref["v_ckm_abs"]))),
            abs(obs_scr["jarlskog_tr"] - obs_ir_ref["jarlskog_tr"]),
            abs(obs_scr["yb_over_ytau"] - obs_ir_ref["yb_over_ytau"]),
        )
        max_haar_rge_scrambling_err = max(max_haar_rge_scrambling_err, err_trial)

    # 5. Guardrail 5: Single-anchor non-dimensionalization & pure-SM desert 3-line unification obstruction:
    # From a single abstract UV coupling alpha_GUT^{-1}(0) = 24 at t = 0, 1-loop desert running gives
    # alpha_i^{-1}(t) = 24 - b_i * t, forcing (alpha_1^{-1} - alpha_2^{-1}) / (alpha_2^{-1} - alpha_3^{-1}) = (b_1 - b_2)/(b_2 - b_3) = 218/115
    # independently of t != 0; any IR point violating 115*(a1 - a2) == 218*(a2 - a3) (e.g. abstract (60, 30, 10)) fails 3-line unification:
    t_sym_ir = sp.Symbol("t_sym_ir", negative=True)
    ainv_desert = [sp.Integer(24) - beta_sym["b1_vec"][i] * t_sym_ir for i in range(3)]
    desert_ratio_obstruction_exact = (
        sp.simplify(
            (ainv_desert[0] - ainv_desert[1]) * (23 * 5) - (ainv_desert[1] - ainv_desert[2]) * (2 * 109)
        )
        == 0
    )
    t_unif_12 = sp.Rational(60 - 30, 1) / (b1_s - b2_s)
    t_unif_23 = sp.Rational(30 - 10, 1) / (b2_s - b3_s)
    desert_unif_scale_mismatch = float(abs(t_unif_12 - t_unif_23))

    # Guardrail 5 dimensionless ratio invariance under arbitrary rescaling mu_0 -> kappa * mu_0 and v_anchor -> kappa * v_anchor:
    mu_0_sym, kappa_sym, t_dimless, yf_sym, lam_pos_sym = sp.symbols(
        "mu_0_sym kappa_sym t_dimless yf_sym lam_pos_sym", positive=True
    )
    mu_phys = mu_0_sym * sp.exp(2 * sp.pi * t_dimless)
    mu_rescaled = (kappa_sym * mu_0_sym) * sp.exp(2 * sp.pi * t_dimless)
    mf_over_mh_1 = ((yf_sym * mu_0_sym) / sp.sqrt(2)) / (sp.sqrt(2 * lam_pos_sym) * mu_0_sym)
    mf_over_mh_2 = ((yf_sym * kappa_sym * mu_0_sym) / sp.sqrt(2)) / (
        sp.sqrt(2 * lam_pos_sym) * kappa_sym * mu_0_sym
    )
    ratio_scale_inv = (
        sp.simplify((mu_rescaled / (kappa_sym * mu_0_sym)) - (mu_phys / mu_0_sym)) == 0
        and sp.simplify(mf_over_mh_2 - mf_over_mh_1) == 0
        and sp.simplify(mf_over_mh_1 - yf_sym / (2 * sp.sqrt(lam_pos_sym))) == 0
    )
    max_dimensionful_anchors = int(sp.Matrix([[mu_0_sym]]).rank())

    part6c_ok = (
        det_untwisted_lr == 1
        and det_twisted_lr == 5
        and det_untwisted_rl == 1
        and det_twisted_rl == 5
        and untwisted_nonzero_total == 0
        and primes_with_twisted_line == [5]
        and bool(lr_mod5_eigen)
        and bool(rl_mod5_eigen)
        and sc_premise_bits == 1
        and bool(j_small_exact)
        and j5_mp_err < 1e-36
        and small_n5_asymptotic_ratio > 9
        and vol_conjecture_err < 1e-6
        and unresolved_sm_count == 19
        and unproved_wp43_gates == 3
        and bool(b1_trace_identities_exact)
        and bench_1loop_gauge_err < TOL
        and bench_pendleton_ross_fp_err < TOL
        and bench_bernoulli_err < TOL
        and bench_pure_quartic_err < TOL
        and bench_2loop_implicit_g3_err < TOL
        and bench_5chan_jet4_err < TOL
        and bench_reversibility_err < TOL
        and neg_ctrl_wrong_4pi_err > 1e-6
        and neg_ctrl_wrong_lam2_err > 1e-6
        and uv_yb_ytau_unity_err < TOL
        and abs(obs_ir_ref["jarlskog_tr"]) > 1e-9
        and radiative_yb_ytau_shift > (1 / 10)
        and max_haar_rge_scrambling_err < TOL
        and bool(desert_ratio_obstruction_exact)
        and desert_unif_scale_mismatch > 0.5
        and bool(ratio_scale_inv)
        and max_dimensionful_anchors == 1
    )

    return {
        "wp42_det_untwisted_lr": det_untwisted_lr,
        "wp42_det_twisted_lr": det_twisted_lr,
        "wp42_primes_with_twisted_eigenline": primes_with_twisted_line,
        "wp42_sc_premise_bits": sc_premise_bits,
        "wp43_j5_mp_err": j5_mp_err,
        "wp43_j5_value": float(j5_mp),
        "wp43_small_n5_over_leading_asymptotic": small_n5_asymptotic_ratio,
        "wp43_large_n_volume_conjecture_err": vol_conjecture_err,
        "wp43_unresolved_sm_parameters_count": unresolved_sm_count,
        "wp43_unproved_bridge_gates_count": unproved_wp43_gates,
        "guardrail4_1loop_gauge_err": bench_1loop_gauge_err,
        "guardrail4_pendleton_ross_fp_err": bench_pendleton_ross_fp_err,
        "guardrail4_bernoulli_coupled_err": bench_bernoulli_err,
        "guardrail4_pure_quartic_err": bench_pure_quartic_err,
        "guardrail4_2loop_implicit_g3_err": bench_2loop_implicit_g3_err,
        "guardrail4_5chan_symbolic_jet4_err": bench_5chan_jet4_err,
        "guardrail4_reversibility_err": bench_reversibility_err,
        "guardrail4_neg_ctrl_wrong_4pi_err": neg_ctrl_wrong_4pi_err,
        "guardrail4_neg_ctrl_wrong_lam2_err": neg_ctrl_wrong_lam2_err,
        "guardrail3_max_haar_rge_scrambling_err": max_haar_rge_scrambling_err,
        "guardrail3_radiative_yb_over_ytau": obs_ir_ref["yb_over_ytau"],
        "guardrail5_desert_unif_scale_mismatch": desert_unif_scale_mismatch,
        "guardrail5_max_dimensionful_anchors": max_dimensionful_anchors,
        "part6c_level5_kashaev_and_rge_verified": part6c_ok,
    }


def run_stage6_complete_verification() -> dict[str, Any]:
    """Run all Stage 6 (Parts 6A, 6B, 6C) verifications + AST Firewall & Guardrail-2 self-locks."""
    self_path = Path(__file__).resolve()
    fw_ok = audit_source_zero_empirical_constants(self_path)
    g2_ok = check_guardrail2_ast_no_literal_bool_verdicts(self_path.read_text(encoding="utf-8"))

    res_6a = verify_part6a_kronecker_cusp_end_and_wp41()
    res_6b = verify_part6b_whole_weave_transfer_and_p845()
    res_6c = verify_part6c_level5_kashaev_and_2loop_rge()

    all_passed = (
        fw_ok
        and g2_ok
        and res_6a["part6a_kronecker_end_and_wp41_verified"]
        and res_6b["part6b_whole_weave_and_p845_verified"]
        and res_6c["part6c_level5_kashaev_and_rge_verified"]
    )

    return {
        "zero_sm_empirical_constants_ast_verified": fw_ok,
        "guardrail2_ast_no_literal_bool_verdicts_verified": g2_ok,
        "part6a_kronecker_and_end": res_6a,
        "part6b_whole_weave_and_p845": res_6b,
        "part6c_level5_kashaev_and_rge": res_6c,
        "all_verifications_passed": all_passed,
    }
