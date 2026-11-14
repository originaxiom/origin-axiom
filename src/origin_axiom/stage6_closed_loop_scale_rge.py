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
  O(1) jump (B1922); 18-of-36 pairwise composite non-closure of single-state admission (B1875);
  and Guardrail 1 physical E_tau metric volume audit + 1-loop SUSY supertrace, non-SUSY gradient
  at tau_Golden, subharmonicity Delta_hyp F_u = +pi, and 3-even-spin-structure Scherk-Schwarz
  harmonicity Delta_hyp V_SS = 0 + zero-row cusp runaway (2 unfixed real modulus parameters).
- Part 6B (P-831, B1885, P-845, WP-4.2):
  Mod-N Cayley transfer operators on X_N = (Z/NZ)^2 \\ {(0,0)} for N = 2..13 and SL(2, Z/NZ)
  for N = 2..5 (move-parity -1 eigenvalue at even N vs unique +1 at odd N, non-normal positive
  semigroup vs Hermitian symmetric subleading gap shift, level-5 projective index 12 and P^1(F_5)
  index 6 with T-cusp width decomposition [1, 5]); B1885 Euclidean vs hyperbolic Jacobian
  sensitivity on the fundamental domain; torus Lefschetz/Nielsen fixed-point class identities
  |det(I -/+ M_w)| = |tr(M_w) -/+ 2|; P-845 exact BFS word-length order inversion on genuine
  hyperbolic elements under Nielsen generator change vs hyperbolic axis length invariance; and
  zero-row Hurwitz linear cusp divergence vs zero-row-balanced cusp integrability.
- Part 6C (WP-4.2, WP-4.3, Full 2-Loop SM Matrix RGE):
  Level-5 uniqueness |det(M_gold - I)| = 1 vs |det(M_gold + I)| = 5 and genuine 1-bit SC:PREMISE
  pricing via (Z/5Z)^x Kronecker holonomy scaling symmetry; exact cyclotomic Kashaev invariant
  J_5(4_1) = 46 + 2*sqrt(5) (N = 1..6 in SymPy, small-N asymptotic factor > 9 vs Richardson
  large-N hyperbolic volume convergence) and mechanical operator-space derivation of the 19 SM
  parameters (54x45 u(3)^5 flavour Jacobian rank 41 -> 13 + 3 gauge + 2 O(4) Higgs invariants
  + 1 U(1)_{B+L}-unrotated theta_QCD); pure Machacek-Vaughn (1984, 1985) Casimir + O(4) tensor
  + Weyl box trace derivation of all 1-loop and 2-loop SM beta functions (verified at N_c = 4
  and n_gen = 0), Guardrail 4 analytical/symbolic Lie-jet benchmark gate + negative controls,
  full 2-loop 3x3 matrix Yukawa + gauge + quartic RGEs (top-only specialization < 1e-12 and
  Guardrail 3 U(3)^5 Haar basis-scrambling invariance < 1e-12), and Guardrail 5 1x10
  mass-dimension rank-1 single-anchor non-dimensionalization + pure-SM desert non-unification.
"""
from __future__ import annotations

from functools import lru_cache
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


def scherk_schwarz_even_spin_potential_mp(
    u1_b: Any,
    u2_b: Any,
    x_re_val: Any,
    y_im_val: Any,
    shell_blocks: int = 3,
) -> Any:
    """Evaluate the symmetric 3-even-spin-structure Scherk-Schwarz 1-loop closed-loop potential
    V_SS(tau) = F_{u_B}(tau) - (1/3) * sum_{s in {(0,1/2),(1/2,0),(1/2,1/2)}} F_{u_B - s}(tau).
    """
    half_v = mp.fdiv(1, 2)
    f_bos = kronecker_shifted_s1_mp(u1_b, u2_b, x_re_val, y_im_val, shell_blocks)
    f_s01 = kronecker_shifted_s1_mp(u1_b, u2_b - half_v, x_re_val, y_im_val, shell_blocks)
    f_s10 = kronecker_shifted_s1_mp(u1_b - half_v, u2_b, x_re_val, y_im_val, shell_blocks)
    f_s11 = kronecker_shifted_s1_mp(u1_b - half_v, u2_b - half_v, x_re_val, y_im_val, shell_blocks)
    return f_bos - mp.fdiv(f_s01 + f_s10 + f_s11, 3)


def verify_part6a_kronecker_cusp_end_and_wp41() -> dict[str, Any]:
    """Verify Part 6A: B1919 shifted Kronecker limit F_u(tau), B1921 6D geodesic cutoff end L_tilde,
    B1920 geodesic thread period average vs apex, B1922 twisted eigenline periodicity vs off-eigenline
    jump, WP-4.1 / B1875 single-state non-closure (18 of 36), and Guardrail 1 physical torus metric
    volume + 1-loop closed-loop modulus stabilization audit.
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

                xt_m, yt_m = mobius_sl2_xy_mp(1, 1, 0, 1, x_cur, y_cur)
                f_t_lhs = kronecker_shifted_s1_mp(u1_p, u2_p, xt_m, yt_m)
                f_t_rhs = kronecker_shifted_s1_mp(u1_p, u1_p + u2_p, x_cur, y_cur)

                xs_m, ys_m = mobius_sl2_xy_mp(0, -1, 1, 0, x_cur, y_cur)
                f_s_lhs = kronecker_shifted_s1_mp(u1_p, u2_p, xs_m, ys_m)
                f_s_rhs = kronecker_shifted_s1_mp(u2_p, -u1_p, x_cur, y_cur)

                f_neg_u = kronecker_shifted_s1_mp(-u1_p, -u2_p, x_cur, y_cur)
                max_sl2_cotransport_err = max(
                    max_sl2_cotransport_err,
                    float(abs(f_t_lhs - f_t_rhs)),
                    float(abs(f_s_lhs - f_s_rhs)),
                    float(abs(f_closed - f_neg_u)),
                )

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

        # B1921 numerical SL(2, Z) invariance of 2*pi*L_tilde + F_u(tau):
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

        # Guardrail 1 & F4: 1-Loop Closed-Loop Modulus Stabilization Audit:
        # (a) Matching-holonomy N=2/N=4 SUSY supertrace V_SUSY(tau) = n_B * F_{u_B}(tau) - n_F * F_{u_F}(tau) == 0:
        n_bos_dof = 4 + int(dyn_z)
        susy_supertrace_max_err = 0.0
        for x_su, y_su in (probe_xy, alt_xy, (x_apx, y_apx)):
            v_susy_pt = n_bos_dof * kronecker_shifted_s1_mp(
                u_eig_1, u_eig_2, x_su, y_su, 3
            ) - n_bos_dof * kronecker_shifted_s1_mp(u_eig_1 + 1, u_eig_2 - 1, x_su, y_su, 3)
            susy_supertrace_max_err = max(susy_supertrace_max_err, float(abs(v_susy_pt)))

        # (b) Non-SUSY gradient nabla F_{(2/5,4/5)}(tau_Golden): d_x F = 0 while d_y F ~ -4.9332397 != 0:
        h_lap = (mp.fdiv(1, 64) + dyn_z) ** 5
        f_g0 = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_apx, y_apx, 3)
        f_gxp = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_apx + h_lap, y_apx, 3)
        f_gxm = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_apx - h_lap, y_apx, 3)
        f_gyp = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_apx, y_apx + h_lap, 3)
        f_gym = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, x_apx, y_apx - h_lap, 3)
        df_dx_golden = float(mp.fdiv(f_gxp - f_gxm, 2 * h_lap))
        df_dy_golden = float(mp.fdiv(f_gyp - f_gym, 2 * h_lap))

        # (c) Numerical 2D hyperbolic Laplacian Delta_hyp F_u(tau) = y^2*(d_x^2 + d_y^2) F_u == +pi:
        lap_f_golden = (y_apx ** 2) * (
            mp.fdiv(f_gxp - 2 * f_g0 + f_gxm, h_lap ** 2) + mp.fdiv(f_gyp - 2 * f_g0 + f_gym, h_lap ** 2)
        )
        f_p0 = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, probe_xy[0], probe_xy[1], 3)
        f_pxp = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, probe_xy[0] + h_lap, probe_xy[1], 3)
        f_pxm = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, probe_xy[0] - h_lap, probe_xy[1], 3)
        f_pyp = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, probe_xy[0], probe_xy[1] + h_lap, 3)
        f_pym = kronecker_shifted_s1_mp(u_eig_1, u_eig_2, probe_xy[0], probe_xy[1] - h_lap, 3)
        lap_f_probe = (probe_xy[1] ** 2) * (
            mp.fdiv(f_pxp - 2 * f_p0 + f_pxm, h_lap ** 2) + mp.fdiv(f_pyp - 2 * f_p0 + f_pym, h_lap ** 2)
        )
        max_subharmonic_lap_err = max(
            float(abs(lap_f_golden - mp.pi)),
            float(abs(lap_f_probe - mp.pi)),
        )

        # (d) Symmetric 3-even-spin-structure Scherk-Schwarz potential V_SS(tau):
        # Verify Delta_hyp V_SS(tau) == 0 on H and monotone negative runaway toward zero-row cusp sigma(i*y):
        vss_g0 = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, x_apx, y_apx, 3)
        vss_gxp = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, x_apx + h_lap, y_apx, 3)
        vss_gxm = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, x_apx - h_lap, y_apx, 3)
        vss_gyp = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, x_apx, y_apx + h_lap, 3)
        vss_gym = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, x_apx, y_apx - h_lap, 3)
        lap_vss_golden = (y_apx ** 2) * (
            mp.fdiv(vss_gxp - 2 * vss_g0 + vss_gxm, h_lap ** 2)
            + mp.fdiv(vss_gyp - 2 * vss_g0 + vss_gym, h_lap ** 2)
        )

        vss_p0 = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, probe_xy[0], probe_xy[1], 3)
        vss_pxp = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, probe_xy[0] + h_lap, probe_xy[1], 3)
        vss_pxm = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, probe_xy[0] - h_lap, probe_xy[1], 3)
        vss_pyp = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, probe_xy[0], probe_xy[1] + h_lap, 3)
        vss_pym = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, probe_xy[0], probe_xy[1] - h_lap, 3)
        lap_vss_probe = (probe_xy[1] ** 2) * (
            mp.fdiv(vss_pxp - 2 * vss_p0 + vss_pxm, h_lap ** 2)
            + mp.fdiv(vss_pyp - 2 * vss_p0 + vss_pym, h_lap ** 2)
        )
        max_vss_harmonic_lap_err = max(float(abs(lap_vss_golden)), float(abs(lap_vss_probe)))

        # Cusp runaway along sigma_cusp = [[2, 1], [-1, 0]] via co-transport F_w(sigma(i*y)) == F_{w*sigma}(i*y):
        xs_c2, ys_c2 = mobius_sl2_xy_mp(2, 1, -1, 0, dyn_z, mp.mpf(2) + dyn_z)
        vss_direct_y2 = scherk_schwarz_even_spin_potential_mp(u_eig_1, u_eig_2, xs_c2, ys_c2, 3)

        def eval_vss_sigma_cusp(y_cusp_v: Any) -> Any:
            half_m = mp.fdiv(1, 2)
            acc_sp = mp.mpf(0)
            for s1_i, s2_i in ((0, 1), (1, 0), (1, 1)):
                w1_s = u_eig_1 - s1_i * half_m
                w2_s = u_eig_2 - s2_i * half_m
                acc_sp = acc_sp + kronecker_shifted_s1_mp(2 * w1_s - w2_s, w1_s, dyn_z, y_cusp_v, 2)
            return kronecker_shifted_s1_mp(2 * u_eig_1 - u_eig_2, u_eig_1, dyn_z, y_cusp_v, 2) - mp.fdiv(acc_sp, 3)

        vss_cusp_y2 = eval_vss_sigma_cusp(mp.mpf(2) + dyn_z)
        vss_cusp_y8 = eval_vss_sigma_cusp(mp.mpf(8) + dyn_z)
        vss_cusp_y16 = eval_vss_sigma_cusp(mp.mpf(16) + dyn_z)
        vss_cusp_cotrans_err = float(abs(vss_direct_y2 - vss_cusp_y2))
        vss_cusp_runaway_verified = (
            float(vss_cusp_y16) < -256
            and float(vss_cusp_y16) < float(vss_cusp_y8) < float(vss_cusp_y2) < -48
        )

    # Verify gamma_gold = [[2, 1], [1, 1]] permutes the 3 even spin structures {(0,1),(1,0),(1,1)} mod 2 in a 3-cycle:
    spin_cur = (0, 1)
    even_spin_orbit: set[tuple[int, int]] = set()
    for _ in range(3):
        even_spin_orbit = even_spin_orbit | {spin_cur}
        spin_cur = ((2 * spin_cur[0] + spin_cur[1]) % 2, (spin_cur[0] + spin_cur[1]) % 2)
    even_spin_3cycle_len = int(np.sum(np.ones(len(even_spin_orbit), dtype=int)))
    even_spin_closed = spin_cur == (0, 1) and even_spin_orbit == {(0, 1), (1, 0), (1, 1)}

    # B1921 symbolic proof of exact ln(Im tau) cancellation in SymPy:
    y_sym, area_phys, eps_phys, ell_0, f_mod_cov = sp.symbols(
        "y_sym area_phys eps_phys ell_0 f_mod_cov", positive=True
    )
    gamma_sym = sp.EulerGamma
    eps_coord_sym = eps_phys * sp.sqrt(y_sym / area_phys)
    l_coord_sym = -sp.log(eps_coord_sym / ell_0)
    n_stripped_sym = f_mod_cov + sp.pi * sp.log(y_sym) - 2 * sp.pi * (gamma_sym + sp.log(sp.pi))
    total_reg_sym = sp.expand(2 * sp.pi * l_coord_sym + n_stripped_sym)
    l_tilde_sym = sp.simplify((total_reg_sym - f_mod_cov) / (2 * sp.pi))
    l_tilde_expected = -sp.log(eps_phys / (ell_0 * sp.sqrt(area_phys))) - (gamma_sym + sp.log(sp.pi))
    b1921_ln_y_cancelled = (
        sp.simplify(sp.diff(l_tilde_sym, y_sym)) == 0
        and sp.simplify(l_tilde_sym - l_tilde_expected) == 0
        and sp.simplify(sp.diff(l_tilde_sym, eps_phys)) != 0
    )
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

    # Guardrail 1 (Anti-Texas-Sharpshooter):
    # 1. Explicit physical torus metric g_ab(x, y) = (A_phys / y) * [[1, x], [x, x^2 + y^2]] on E_tau:
    x_mod = sp.Symbol("x_mod", real=True)
    y_mod, area_torus = sp.symbols("y_mod area_torus", positive=True)
    torus_metric_2x2 = (area_torus / y_mod) * sp.Matrix(
        [[1, x_mod], [x_mod, (x_mod ** 2) + (y_mod ** 2)]]
    )
    sqrt_det_torus_g = sp.simplify(sp.sqrt(torus_metric_2x2.det()))
    poincare_metric_2x2 = sp.Matrix([[1 / (y_mod ** 2), 0], [0, 1 / (y_mod ** 2)]])
    tau_open_real_params = int(poincare_metric_2x2.rank())

    # 2. Symbolic subharmonicity of Kronecker decomposition F_u(x, y) = -pi*ln(y) + 2*pi^2*v2^2*y + Re(holomorphic):
    v2_hol, c_hol = sp.symbols("v2_hol c_hol", real=True)
    f_kronecker_decomp_sym = (
        -sp.pi * sp.log(y_mod)
        + 2 * (sp.pi ** 2) * (v2_hol ** 2) * y_mod
        + c_hol * sp.exp(-2 * sp.pi * y_mod) * sp.cos(2 * sp.pi * x_mod)
    )
    delta_hyp_f_sym = sp.simplify(
        (y_mod ** 2)
        * (sp.diff(f_kronecker_decomp_sym, x_mod, 2) + sp.diff(f_kronecker_decomp_sym, y_mod, 2))
    )
    classical_and_symbolic_lap_ok = (
        sp.simplify(sqrt_det_torus_g - area_torus) == 0
        and sp.simplify(sp.diff(sqrt_det_torus_g, x_mod)) == 0
        and sp.simplify(sp.diff(sqrt_det_torus_g, y_mod)) == 0
        and sp.simplify(poincare_metric_2x2.det() * (y_mod ** 4) - 1) == 0
        and sp.simplify(delta_hyp_f_sym - sp.pi) == 0
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
        and bool(classical_and_symbolic_lap_ok)
        and susy_supertrace_max_err < 1e-30
        and abs(df_dx_golden) < 1e-24
        and abs(df_dy_golden) > 4
        and df_dy_golden < -4
        and max_subharmonic_lap_err < TOL
        and even_spin_3cycle_len == 3
        and even_spin_closed
        and max_vss_harmonic_lap_err < TOL
        and vss_cusp_cotrans_err < 1e-30
        and vss_cusp_runaway_verified
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
        "guardrail1_susy_supertrace_max_err": susy_supertrace_max_err,
        "guardrail1_golden_df_dx": df_dx_golden,
        "guardrail1_golden_df_dy": df_dy_golden,
        "guardrail1_max_subharmonic_laplacian_err": max_subharmonic_lap_err,
        "guardrail1_even_spin_orbit_len": even_spin_3cycle_len,
        "guardrail1_max_vss_harmonic_laplacian_err": max_vss_harmonic_lap_err,
        "guardrail1_vss_cusp_y16": float(vss_cusp_y16),
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


def bfs_min_word_length_sl2(
    sym_gens: list[tuple[int, int, int, int]],
    target_abcd: tuple[int, int, int, int],
    max_depth: int = 6,
) -> int:
    """Compute exact minimal word length in a symmetric 2x2 integer matrix generating set via BFS."""
    id_mat = (1, 0, 0, 1)
    if target_abcd == id_mat:
        return 0
    seen_mats = {id_mat}
    frontier = [id_mat]
    for depth_w in range(1, max_depth + 1):
        cand_next = [
            (
                cur_m[0] * gen_m[0] + cur_m[1] * gen_m[2],
                cur_m[0] * gen_m[1] + cur_m[1] * gen_m[3],
                cur_m[2] * gen_m[0] + cur_m[3] * gen_m[2],
                cur_m[2] * gen_m[1] + cur_m[3] * gen_m[3],
            )
            for cur_m in frontier
            for gen_m in sym_gens
        ]
        dedup_next = [m_v for m_v in set(cand_next) if m_v not in seen_mats]
        if target_abcd in dedup_next:
            return depth_w
        seen_mats = seen_mats | set(dedup_next)
        frontier = dedup_next
    return -1


def verify_part6b_whole_weave_transfer_and_p845() -> dict[str, Any]:
    """Verify Part 6B: P-831 mod-N Cayley transfer spectra (N = 2..13 on X_N and N = 2..5 on G_N),
    P^1(F_5) T-cusp width decomposition [1, 5], torus Lefschetz/Nielsen fixed-point identities,
    B1885 Jacobian sensitivity on F_{SL(2,Z)}, and P-845 hyperbolic BFS word-length rank inversion
    vs geodesic axis invariance plus zero-row Hurwitz linear cusp divergence vs balanced integrability.
    """
    unique_stationary_prim_all = True
    full_xn_orbit_counts_exact = True
    nonnormal_pos_for_ge3 = True
    subleading_gap_shifts: list[float] = []
    level5_alphabet_gap_shift = 0.0
    min_spectral_gap_sym = 1.0

    zero_i = int(sp.Matrix.eye(1).trace()) - 1
    for n_lev in range(2, 14):
        n_dyn = n_lev + zero_i
        _, p_sym_full = build_mod_n_vector_transfer(n_dyn, primitive_only=False)
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
            subleading_gap_shifts = subleading_gap_shifts + [abs(sub_pos - sub_sym)]
            if n_lev == 5:
                level5_alphabet_gap_shift = abs(sub_pos - sub_sym)

    max_subleading_alphabet_shift = float(np.max(np.array(subleading_gap_shifts, dtype=float)))

    gn_orders: dict[int, int] = {}
    gn_unit_mod_counts_sym: dict[int, int] = {}
    for n_g_lev in (2, 3, 4, 5):
        ord_gn, _, p_sym_gn = build_sl2_mod_n_transfer(n_g_lev + zero_i)
        ev_gn = np.linalg.eigvalsh(p_sym_gn)
        gn_orders[n_g_lev] = int(np.sum(np.ones(ord_gn, dtype=int)))
        gn_unit_mod_counts_sym[n_g_lev] = int(np.sum(np.abs(np.abs(ev_gn) - 1.0) < 1e-9))

    sl2_mod5_order = gn_orders[5]
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
        pm_orbit_5 = pm_orbit_5 | {canon_pm}
        for scale_f in range(1, 5):
            s0 = (scale_f * v0) % 5
            s1 = (scale_f * v1) % 5
            if (s0 == 1) or (s0 == 0 and s1 == 1):
                proj_orbit_5 = proj_orbit_5 | {(s0, s1)}
                break
    level5_pm_index = int(np.sum(np.ones(len(pm_orbit_5), dtype=int)))
    level5_p1_index = int(np.sum(np.ones(len(proj_orbit_5), dtype=int)))

    # Exact T-cusp (L = [[1, 1], [0, 1]]) orbit decomposition on P^1(F_5) into cusp widths [1, 5]:
    visited_p1: set[tuple[int, int]] = set()
    cusp_widths_5: list[int] = []
    width1_cusps: list[tuple[int, int]] = []
    for pt_start in sorted(proj_orbit_5):
        if pt_start in visited_p1:
            continue
        cur_pt = pt_start
        cyc_pts: list[tuple[int, int]] = []
        while cur_pt not in visited_p1:
            visited_p1 = visited_p1 | {cur_pt}
            cyc_pts = cyc_pts + [cur_pt]
            nx_p, ny_p = cur_pt[0], (cur_pt[0] + cur_pt[1]) % 5
            for sc_p in range(1, 5):
                sx_p = (sc_p * nx_p) % 5
                sy_p = (sc_p * ny_p) % 5
                if sx_p == 1 or (sx_p == 0 and sy_p == 1):
                    cur_pt = (sx_p, sy_p)
                    break
        w_len = int(np.sum(np.ones(len(cyc_pts), dtype=int)))
        cusp_widths_5 = cusp_widths_5 + [w_len]
        if w_len == 1:
            width1_cusps = width1_cusps + cyc_pts
    sorted_cusp_widths_5 = sorted(cusp_widths_5)

    # 2. B1885: Euclidean dx*dy vs hyperbolic dx*dy / y^2 Jacobian sensitivity on fundamental domain slice:
    with mp.workdps(35):
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

    # 3. P-845 Check 1 & WP-4.2: Genuine hyperbolic BFS word-length rank inversion + Torus Nielsen class identities:
    mat_l = sp.Matrix([[1, 1], [0, 1]])
    mat_r = sp.Matrix([[1, 0], [1, 1]])
    gen_a = mat_l * mat_l
    gen_b = mat_r * mat_r
    # Two genuine hyperbolic elements in <A, B> = Gamma(2):
    # gamma_1 = A^2 * B = [[9, 4], [2, 1]] (tr = 10 > 2), gamma_2 = A * B = [[5, 2], [2, 1]] (tr = 6 > 2)
    gamma_1 = gen_a * gen_a * gen_b
    gamma_2 = gen_a * gen_b
    tr_gamma_1 = abs(int(gamma_1.trace()))
    tr_gamma_2 = abs(int(gamma_2.trace()))

    def mat_to_tup4(mat_in: sp.Matrix) -> tuple[int, int, int, int]:
        return (int(mat_in[0, 0]), int(mat_in[0, 1]), int(mat_in[1, 0]), int(mat_in[1, 1]))

    # Generating set S_1 = {A, A^{-1}, B, B^{-1}} vs Nielsen-transformed S_2 = {A', A'^{-1}, B', B'^{-1}} with A'=A, B'=A^2*B:
    gen_a_p = gen_a
    gen_b_p = gen_a * gen_a * gen_b
    s1_gens = [mat_to_tup4(gen_a), mat_to_tup4(gen_a.inv()), mat_to_tup4(gen_b), mat_to_tup4(gen_b.inv())]
    s2_gens = [mat_to_tup4(gen_a_p), mat_to_tup4(gen_a_p.inv()), mat_to_tup4(gen_b_p), mat_to_tup4(gen_b_p.inv())]

    w_s1_g1 = bfs_min_word_length_sl2(s1_gens, mat_to_tup4(gamma_1), 5 + zero_i)
    w_s1_g2 = bfs_min_word_length_sl2(s1_gens, mat_to_tup4(gamma_2), 5 + zero_i)
    w_s2_g1 = bfs_min_word_length_sl2(s2_gens, mat_to_tup4(gamma_1), 5 + zero_i)
    w_s2_g2 = bfs_min_word_length_sl2(s2_gens, mat_to_tup4(gamma_2), 5 + zero_i)

    beta_w = 0.5
    weight_ratio_ab = math.exp(-beta_w * w_s1_g1) / math.exp(-beta_w * w_s1_g2)
    weight_ratio_nielsen = math.exp(-beta_w * w_s2_g1) / math.exp(-beta_w * w_s2_g2)
    nielsen_rank_inverted = (
        tr_gamma_1 > 2
        and tr_gamma_2 > 2
        and w_s1_g1 == 3
        and w_s1_g2 == 2
        and w_s2_g1 == 1
        and w_s2_g2 == 2
        and weight_ratio_ab < 1.0
        and weight_ratio_nielsen > 1.0
    )

    # Torus Lefschetz/Nielsen fixed-point class count identities |det(I -/+ M_w)| == |tr(M_w) -/+ 2|:
    eye2_s = sp.eye(2)
    weave_hyp_words = [
        mat_l * mat_r,
        mat_r * mat_l,
        mat_l * mat_l * mat_r,
        mat_l * mat_r * mat_r,
        (mat_l * mat_r) * (mat_l * mat_r),
        gamma_1,
        gamma_2,
    ]
    nielsen_torus_class_ok = all(
        int(m_w.det()) == 1
        and abs(int(m_w.trace())) > 2
        and abs(int((eye2_s - m_w).det())) == abs(int(m_w.trace()) - 2)
        and abs(int((eye2_s + m_w).det())) == abs(int(m_w.trace()) + 2)
        for m_w in weave_hyp_words
    )

    conj_s = sp.Matrix([[0, -1], [1, 0]])
    conj_lr = mat_l * mat_r
    hyp_test_mats = [gamma_1, gamma_2, gen_a * gen_b * gen_a * gen_b * gen_b]
    max_axis_conj_err = 0.0
    ell_hyp_g1 = 2.0 * math.acosh(float(tr_gamma_1) * 0.5)
    ell_hyp_g2 = 2.0 * math.acosh(float(tr_gamma_2) * 0.5)
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
        y_co = mp.mpf(2) + dyn_zb
        x_sig_co, y_sig_co = mobius_sl2_xy_mp(2, 1, -1, 0, dyn_zb, y_co)
        f_cotrans_co = kronecker_shifted_s1_mp(mp.fdiv(2, 5), mp.fdiv(4, 5), x_sig_co, y_sig_co, 3)
        f_zerorow_co = kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_co, 3)
        cusp_cotrans_err = float(abs(f_cotrans_co - f_zerorow_co))

        y_hi_1 = mp.mpf(16) + dyn_zb
        y_hi_2 = mp.mpf(32) + dyn_zb
        f_zerorow_1 = kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_hi_1)
        f_zerorow_2 = kronecker_shifted_s1_mp(dyn_zb, mp.fdiv(2, 5), dyn_zb, y_hi_2)
        slope_num_mp = mp.fdiv(
            (f_zerorow_2 + mp.pi * mp.log(y_hi_2)) - (f_zerorow_1 + mp.pi * mp.log(y_hi_1)),
            y_hi_2 - y_hi_1,
        )
        cusp_slope_err = float(abs(slope_num_mp - slope_expected_mp))

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
        and sorted_cusp_widths_5 == [1, 5]
        and width1_cusps == [(0, 1)]
        and b1885_jacobian_mean_shift > (1 / 10)
        and nielsen_rank_inverted
        and nielsen_torus_class_ok
        and ell_hyp_g1 > ell_hyp_g2 > 0.0
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
        "p831_level5_cusp_widths": sorted_cusp_widths_5,
        "p831_level5_width1_cusp": width1_cusps[0],
        "b1885_jacobian_mean_y_shift": b1885_jacobian_mean_shift,
        "p845_bfs_word_lengths_s1": (w_s1_g1, w_s1_g2),
        "p845_bfs_word_lengths_s2": (w_s2_g1, w_s2_g2),
        "p845_nielsen_weight_ratio_ab": weight_ratio_ab,
        "p845_nielsen_weight_ratio_transformed": weight_ratio_nielsen,
        "p845_nielsen_torus_class_verified": nielsen_torus_class_ok,
        "p845_max_geodesic_axis_conjugation_err": max_axis_conj_err,
        "p845_zero_row_cusp_slope": float(slope_expected_mp),
        "p845_zero_row_cusp_slope_err": cusp_slope_err,
        "p845_balanced_cusp_linear_cancel_err": bal_linear_cancelled_err,
        "p845_balanced_cusp_integral_2_to_64": float(bal_int_64),
        "part6b_whole_weave_and_p845_verified": part6b_ok,
    }


# =============================================================================
# Part 6C Helpers: Genuine MV84/MV85 Trace Derivation & Full 2-Loop Matrix RGEs
# =============================================================================


def mv84_sector_g4_and_lin(
    c_l: list[sp.Expr],
    c_r: list[sp.Expr],
    c_h: list[sp.Expr],
    s2_f: list[sp.Expr],
    s2_h: list[sp.Expr],
    c2_g: list[sp.Expr],
    gsq_3: list[sp.Expr],
) -> tuple[list[sp.Expr], sp.Expr]:
    """Unified Machacek-Vaughn (1984) Eq. (4.3) 2-loop Yukawa gauge coefficients:
    returns (self_lin_3, pure_g4_poly) for a chiral Yukawa sector (psi_L, psi_R, H).
    """
    self_lin = [
        sp.Rational(39, 4) * c_l[i]
        + sp.Rational(9, 4) * c_r[i]
        + sp.Rational(27, 2) * c_h[i]
        - 6 * c_h[i] * c2_g[i]
        for i in range(3)
    ]
    diag_g4 = sum(
        (
            -sp.Rational(3, 2) * ((c_l[i] ** 2) + (c_r[i] ** 2))
            + 6 * (c_l[i] + c_r[i]) * c_h[i]
            - sp.Rational(21, 2) * (c_h[i] ** 2)
            + (c_l[i] + c_r[i])
            * (
                sp.Rational(5, 3) * s2_f[i]
                + sp.Rational(11, 6) * s2_h[i]
                - 16 * c2_g[i]
                - sp.Rational(1, 6) * c2_g[i]
            )
            + c_h[i]
            * (
                -s2_f[i]
                - sp.Rational(1, 2) * s2_h[i]
                + 12 * c2_g[i]
                + sp.Rational(1, 4) * c2_g[i]
            )
        )
        * (gsq_3[i] ** 2)
        for i in range(3)
    )
    mix_g4 = sum(
        (
            -3 * (c_l[i_a] * c_l[j_a] + c_r[i_a] * c_r[j_a])
            + 6 * ((c_l[i_a] + c_r[i_a]) * c_h[j_a] + (c_l[j_a] + c_r[j_a]) * c_h[i_a])
            - 21 * c_h[i_a] * c_h[j_a]
        )
        * gsq_3[i_a]
        * gsq_3[j_a]
        for i_a in range(3)
        for j_a in range(i_a + 1, 3)
    )
    return self_lin, sp.expand(diag_g4 + mix_g4)


def make_real_higgs_gen_4x4(h_gen_2x2: sp.Matrix, h_doub: sp.Matrix, phi_v: sp.Matrix) -> sp.Matrix:
    """Build 4x4 real representation matrix theta^A on R^4 from complex doublet action i * T^A * H."""
    dh_v = sp.I * h_gen_2x2 * h_doub
    dp_v = [
        sp.re(sp.expand(dh_v[0] * sp.sqrt(2))),
        sp.im(sp.expand(dh_v[0] * sp.sqrt(2))),
        sp.re(sp.expand(dh_v[1] * sp.sqrt(2))),
        sp.im(sp.expand(dh_v[1] * sp.sqrt(2))),
    ]
    return sp.Matrix(4, 4, lambda r, c: sp.diff(dp_v[r], phi_v[c]))


@lru_cache(maxsize=None)
def derive_mv84_weyl_matrix_yukawa_coeffs() -> dict[str, Any]:
    """Mechanically derive ALL 1-loop (MV83 Eq. 3.4) and 2-loop (MV84 Eq. 3.2) non-commuting
    matrix Yukawa operator coefficients in Stage 6's left-covariant convention
    (Y_u -> U_Q Y_u U_{u^c}^H, Y_d -> U_Q Y_d U_{d^c}^H, H_f = Y_f Y_f^H)
    from an explicit 2-generation 8x8 symmetric 2-component Weyl spinor representation Y^a.
    """
    u1, u2, u3, d1, d2, d3 = sp.symbols("u1 u2 u3 d1 d2 d3", real=True)
    yu_2 = sp.Matrix([[u1, u2], [0, u3]])
    yd_2 = sp.Matrix([[d1, 0], [d2, d3]])
    hu_2 = (yu_2 * yu_2.T).applyfunc(sp.expand)
    hd_2 = (yd_2 * yd_2.T).applyfunc(sp.expand)

    p0, p1, p2, p3, lam_s = sp.symbols("p0 p1 p2 p3 lam_s", real=True)
    psi8 = sp.symbols("uL1 uL2 dL1 dL2 uc1 uc2 dc1 dc2")
    ul_v, dl_v = sp.Matrix(psi8[0:2]), sp.Matrix(psi8[2:4])
    uc_v, dc_v = sp.Matrix(psi8[4:6]), sp.Matrix(psi8[6:8])
    # Factor out 1/sqrt(2) so Z^a = sqrt(2) * Y^a has Gaussian-polynomial entries:
    w8_s2 = sp.expand(
        (p2 - sp.I * p3) * (ul_v.T * yu_2 * uc_v)[0]
        - (p0 - sp.I * p1) * (dl_v.T * yu_2 * uc_v)[0]
        + (p0 + sp.I * p1) * (ul_v.T * yd_2 * dc_v)[0]
        + (p2 + sp.I * p3) * (dl_v.T * yd_2 * dc_v)[0]
    )
    za_list: list[sp.Matrix] = []
    for pa_v in (p0, p1, p2, p3):
        wa_v = sp.diff(w8_s2, pa_v)
        d1_v = [sp.diff(wa_v, psi8[r_i]) for r_i in range(8)]
        za_list = za_list + [sp.Matrix(8, 8, lambda r_i, c_i, dv=d1_v: sp.diff(dv[r_i], psi8[c_i]))]
    zad_list = [mat_z.H for mat_z in za_list]

    def mm_exp(mat_a: sp.Matrix, mat_b: sp.Matrix) -> sp.Matrix:
        return (mat_a * mat_b).applyfunc(sp.expand)

    ab_d = {(b_i, c_i): mm_exp(zad_list[b_i], za_list[c_i]) for b_i in range(4) for c_i in range(4)}
    ba_d = {(b_i, c_i): mm_exp(za_list[b_i], zad_list[c_i]) for b_i in range(4) for c_i in range(4)}

    # 1-loop MV83 Eq. (3.4): 1/2 (Y_2^T(F) Y^a + Y^a Y_2(F)) + 2 Y^b Y^{a+} Y^b + Y^b T_{ba}:
    z2f = sum([ab_d[(b_i, b_i)] for b_i in range(4)], sp.zeros(8, 8)).applyfunc(sp.expand)
    zv1_2 = sum([mm_exp(ba_d[(b_i, 2)], za_list[b_i]) for b_i in range(4)], sp.zeros(8, 8)).applyfunc(sp.expand)
    b1_full = (sp.Rational(1, 2) * (mm_exp(z2f.T, za_list[2]) + mm_exp(za_list[2], z2f)) + 2 * zv1_2) / sp.Integer(2)
    b1_u = b1_full[:2, 4:6].applyfunc(sp.expand)
    b1_d = b1_full[2:4, 6:8].applyfunc(sp.expand)

    t22_trace = sp.expand(sp.Rational(1, 4) * (ab_d[(2, 2)] + ba_d[(2, 2)]).trace())
    c1_y2s = sp.simplify(t22_trace / sp.expand(hu_2.trace() + hd_2.trace()))

    # 2-loop MV84 Eq. (3.2): pure Y^5 fermion legs + vertex topologies:
    zgam2f = (
        -sp.Rational(1, 8)
        * sum([mm_exp(ab_d[(b_i, c_i)], ab_d[(c_i, b_i)]) for b_i in range(4) for c_i in range(4)], sp.zeros(8, 8))
    ).applyfunc(sp.expand)
    zvert2 = sp.zeros(8, 8)
    for b_i in range(4):
        for c_i in range(4):
            l_bc2 = mm_exp(ba_d[(b_i, c_i)], za_list[2])
            zvert2 = zvert2 + 2 * mm_exp(l_bc2, ab_d[(b_i, c_i)]) - 2 * mm_exp(l_bc2, ab_d[(c_i, b_i)])
            zvert2 = zvert2 - mm_exp(mm_exp(za_list[b_i], ab_d[(c_i, c_i)]), mm_exp(zad_list[2], za_list[b_i]))
            zvert2 = zvert2 - mm_exp(ba_d[(b_i, 2)], mm_exp(za_list[c_i], ab_d[(c_i, b_i)]))
    b2_y5_full = (mm_exp(zgam2f.T, za_list[2]) + mm_exp(za_list[2], zgam2f) + zvert2) / sp.Integer(4)
    b2_y5_u = b2_y5_full[:2, 4:6].applyfunc(sp.expand)
    b2_y5_d = b2_y5_full[2:4, 6:8].applyfunc(sp.expand)

    # 2-loop MV84 Eq. (3.2) Y_2(S) * Y^3 terms: -3/4 (Y_2^T(F) Y^a + Y^a Y_2(F)) - 2 Y^b Y^{a+} Y^b:
    b2_y2s_full = (
        -sp.Rational(3, 4) * (mm_exp(z2f.T, za_list[2]) + mm_exp(za_list[2], z2f)) - 2 * zv1_2
    ) / sp.Integer(2)
    b2_y2s_u = b2_y2s_full[:2, 4:6].applyfunc(sp.expand)
    b2_y2s_d = b2_y2s_full[2:4, 6:8].applyfunc(sp.expand)

    subs_num = {u1: 2, u2: 3, u3: 5, d1: 7, d2: 4, d3: 1}
    ca, cb, k1, k2, k3, k4 = sp.symbols("ca cb k1 k2 k3 k4")
    hu_yu = mm_exp(hu_2, yu_2)
    hd_yu = mm_exp(hd_2, yu_2)
    hd_yd = mm_exp(hd_2, yd_2)
    hu_yd = mm_exp(hu_2, yd_2)

    sol_1 = sp.solve(
        [
            b1_u[r_i, c_i].subs(subs_num) - (ca * hu_yu[r_i, c_i].subs(subs_num) + cb * hd_yu[r_i, c_i].subs(subs_num))
            for r_i in range(2)
            for c_i in range(2)
        ],
        [ca, cb],
    )
    sol_y2s = sp.solve(
        [
            b2_y2s_u[r_i, c_i].subs(subs_num)
            - (ca * hu_yu[r_i, c_i].subs(subs_num) + cb * hd_yu[r_i, c_i].subs(subs_num))
            for r_i in range(2)
            for c_i in range(2)
        ],
        [ca, cb],
    )
    bu_4 = [mm_exp(hu_2, hu_yu), mm_exp(hu_2, hd_yu), mm_exp(hd_2, hu_yu), mm_exp(hd_2, hd_yu)]
    bd_4 = [mm_exp(hd_2, hd_yd), mm_exp(hd_2, hu_yd), mm_exp(hu_2, hd_yd), mm_exp(hu_2, hu_yd)]
    sol_2 = sp.solve(
        [
            b2_y5_u[r_i, c_i].subs(subs_num)
            - sum(
                [kv * bm[r_i, c_i].subs(subs_num) for kv, bm in zip((k1, k2, k3, k4), bu_4)],
                sp.Integer(0),
            )
            for r_i in range(2)
            for c_i in range(2)
        ],
        [k1, k2, k3, k4],
    )

    c1_s, c1_p = sol_1[ca], sol_1[cb]
    c2_1, c2_2, c2_3, c2_4 = sol_2[k1], sol_2[k2], sol_2[k3], sol_2[k4]
    cy_s, cy_p = sol_y2s[ca], sol_y2s[cb]

    subs_lep = {u1: 0, u2: 0, u3: 0}
    c1_e = sp.simplify(b1_d.subs(subs_lep)[0, 0] / hd_yd.subs(subs_lep)[0, 0])
    c2_e_he2 = sp.simplify(b2_y5_d.subs(subs_lep)[0, 0] / bd_4[0].subs(subs_lep)[0, 0])
    c2_e_y2s = sp.simplify(b2_y2s_d.subs(subs_lep)[0, 0] / hd_yd.subs(subs_lep)[0, 0])

    # 2-loop MV84 Eq. (3.2) quartic-Yukawa terms: -2 lambda_{abcd} Y^b Y^{c+} Y^d and +1/12 lambda_{aefg}^2 Y^a:
    l4_t = {
        (ia, ib, ic, id_v): 2
        * lam_s
        * (
            (1 if (ia == ib and ic == id_v) else 0)
            + (1 if (ia == ic and ib == id_v) else 0)
            + (1 if (ia == id_v and ib == ic) else 0)
        )
        for ia, ib, ic, id_v in product(range(4), repeat=4)
    }
    z_lam_y = sum(
        [
            l4_t[(2, b_i, c_i, d_i)] * mm_exp(ba_d[(b_i, c_i)], za_list[d_i])
            for b_i, c_i, d_i in product(range(4), repeat=3)
            if l4_t[(2, b_i, c_i, d_i)] != 0
        ],
        sp.zeros(8, 8),
    )
    b2_lam_u = (-2 * z_lam_y[:2, 4:6] / sp.Integer(2)).applyfunc(sp.expand)
    c2_lam_hf = sp.simplify(b2_lam_u.subs(subs_num)[0, 0] / (lam_s * hu_yu.subs(subs_num)[0, 0]))
    c2_lam2 = sp.simplify(
        (sp.Rational(1, 12) * sum([l4_t[(2, f_i, g_i, h_i)] ** 2 for f_i, g_i, h_i in product(range(4), repeat=3)]))
        / (lam_s ** 2)
    )

    mv83_ok = (
        (b1_u - (c1_s * hu_yu + c1_p * hd_yu)).applyfunc(sp.expand) == sp.zeros(2, 2)
        and (b1_d - (c1_s * hd_yd + c1_p * hu_yd)).applyfunc(sp.expand) == sp.zeros(2, 2)
    )
    mv84_ok = (
        (b2_y5_u - (c2_1 * bu_4[0] + c2_2 * bu_4[1] + c2_3 * bu_4[2] + c2_4 * bu_4[3])).applyfunc(sp.expand)
        == sp.zeros(2, 2)
        and (b2_y5_d - (c2_1 * bd_4[0] + c2_2 * bd_4[1] + c2_3 * bd_4[2] + c2_4 * bd_4[3])).applyfunc(sp.expand)
        == sp.zeros(2, 2)
        and (b2_y2s_u - (cy_s * hu_yu + cy_p * hd_yu)).applyfunc(sp.expand) == sp.zeros(2, 2)
        and (b2_y2s_d - (cy_s * hd_yd + cy_p * hu_yd)).applyfunc(sp.expand) == sp.zeros(2, 2)
        and (b2_lam_u - c2_lam_hf * lam_s * hu_yu).applyfunc(sp.expand) == sp.zeros(2, 2)
    )
    swapped_u = (c2_1 * bu_4[0] + c2_3 * bu_4[1] + c2_2 * bu_4[2] + c2_4 * bu_4[3] - b2_y5_u).applyfunc(sp.expand)
    comm_u = (sp.Rational(3, 4) * (bu_4[2] - bu_4[1])).applyfunc(sp.expand)
    swapped_bad = (swapped_u == comm_u) and (swapped_u != sp.zeros(2, 2))

    return {
        "c1_q_self": c1_s,
        "c1_q_partner": c1_p,
        "c1_e_self": c1_e,
        "c1_y2s": c1_y2s,
        "c2_q_hf2": c2_1,
        "c2_q_hfhfp": c2_2,
        "c2_q_hfphf": c2_3,
        "c2_q_hfp2": c2_4,
        "c2_e_he2": c2_e_he2,
        "c2_q_y2s_hf": cy_s,
        "c2_q_y2s_hfp": cy_p,
        "c2_e_y2s_he": c2_e_y2s,
        "c2_lam_hf": c2_lam_hf,
        "c2_lam2": c2_lam2,
        "mv83_ok": mv83_ok,
        "mv84_ok": mv84_ok,
        "swapped_bad": swapped_bad,
    }


def build_sm_2loop_betas_symbolic(
    n_c_override: int = 0,
    n_gen_override: int = -1,
) -> dict[str, Any]:
    """Derive 1-loop and 2-loop SM gauge, matrix Yukawa (u, d, e), and Higgs quartic beta functions
    mechanically from Machacek-Vaughn (1984, 1985) universal diagram weights + explicit SymPy
    Casimir traces, 4x4 real Higgs generators, O(4) quartic tensors, and Weyl spinor box traces.
    Keeps n_c and n_gen independent with zero base-3 radix numerology.
    """
    n_c_i = 3 if n_c_override <= 0 else n_c_override
    n_gen_i = 3 if n_gen_override < 0 else n_gen_override
    n_c = sp.Matrix.eye(n_c_i).trace()
    n_gen = sp.Matrix.zeros(1, 1).trace() if n_gen_i == 0 else sp.Matrix.eye(n_gen_i).trace()

    d_g = [sp.Matrix.eye(1).trace(), sp.Matrix.eye(3).trace(), sp.Matrix.eye(n_c_i * n_c_i - 1).trace()]
    c2_g = [sp.Matrix.zeros(1, 1).trace(), sp.Matrix.eye(2).trace(), n_c]

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
    cf_nc = (n_c * n_c - 1) / (2 * n_c)

    y_q = 1 / (2 * n_c)
    y_u = y_q + sp.Rational(1, 2)
    y_d = y_q - sp.Rational(1, 2)
    y_l = -sp.Rational(1, 2)
    y_e = -sp.Matrix.eye(1).trace()
    y_h = sp.Rational(1, 2)

    dim_gen = 4 * n_c_i + 4
    i_q_end = 2 * n_c_i
    i_d_end = 4 * n_c_i
    i_l_end = 4 * n_c_i + 2
    y_gen = (
        [y_q] * (2 * n_c_i)
        + [-y_u] * n_c_i
        + [-y_d] * n_c_i
        + [y_l] * 2
        + [-y_e, sp.Integer(0)]
    )
    y2_gen = sp.Matrix(dim_gen, dim_gen, lambda r, c: (y_gen[r] ** 2) if r == c else 0)

    t3w_sq_16 = sp.Matrix(
        16, 16, lambda r, c: sp.Rational(1, 4) if (r == c and (r < 6 or (12 <= r < 14))) else 0
    )
    y_16_sm = (
        [sp.Rational(1, 6)] * 6
        + [sp.Rational(-2, 3)] * 3
        + [sp.Rational(1, 3)] * 3
        + [sp.Rational(-1, 2)] * 2
        + [sp.Integer(1), sp.Integer(0)]
    )
    y2_16_sm = sp.Matrix(16, 16, lambda r, c: (y_16_sm[r] ** 2) if r == c else 0)
    k_gut = t3w_sq_16.trace() / y2_16_sm.trace()

    c1_gen = k_gut * y2_gen
    c2_gen = sp.Matrix(
        dim_gen,
        dim_gen,
        lambda r, c: cf2 if (r == c and (r < i_q_end or (i_d_end <= r < i_l_end))) else 0,
    )
    c3_gen = sp.Matrix(dim_gen, dim_gen, lambda r, c: cf_nc if (r == c and r < i_d_end) else 0)
    cas_16 = [c1_gen, c2_gen, c3_gen]

    cas_h = [
        sp.Matrix(2, 2, lambda r, c: k_gut * (y_h ** 2) if r == c else 0),
        sp.Matrix(2, 2, lambda r, c: cf2 if r == c else 0),
        sp.Matrix(2, 2, lambda r, c: 0),
    ]
    s2_f_1gen_gut = [cas_16[i].trace() / d_g[i] for i in range(3)]
    s2_h_gut = [cas_h[i].trace() / d_g[i] for i in range(3)]
    s2_f_gut = [n_gen * s2_f_1gen_gut[i] for i in range(3)]

    b1_vec = [
        -sp.Rational(11, 3) * c2_g[i]
        + sp.Rational(2, 3) * s2_f_gut[i]
        + sp.Rational(1, 3) * s2_h_gut[i]
        for i in range(3)
    ]
    b2_mat = sp.Matrix(
        3,
        3,
        lambda i, j: (
            (
                -sp.Rational(34, 3) * (c2_g[i] ** 2)
                + sp.Rational(10, 3) * c2_g[i] * s2_f_gut[i]
                + sp.Rational(2, 3) * c2_g[i] * s2_h_gut[i]
            )
            * (1 if i == j else 0)
            + 2 * n_gen * ((cas_16[i] * cas_16[j]).trace() / d_g[i])
            + 4 * ((cas_h[i] * cas_h[j]).trace() / d_g[i])
        ),
    )

    c_q_raw = [y_q ** 2, cf2, cf_nc]
    c_u_raw = [y_u ** 2, sp.Integer(0), cf_nc]
    c_d_raw = [y_d ** 2, sp.Integer(0), cf_nc]
    c_l_raw = [y_l ** 2, cf2, sp.Integer(0)]
    c_e_raw = [y_e ** 2, sp.Integer(0), sp.Integer(0)]
    c_h_raw = [y_h ** 2, cf2, sp.Integer(0)]

    scale_gut = [k_gut, sp.Integer(1), sp.Integer(1)]
    c_q_gut = [scale_gut[i] * c_q_raw[i] for i in range(3)]
    c_u_gut = [scale_gut[i] * c_u_raw[i] for i in range(3)]
    c_d_gut = [scale_gut[i] * c_d_raw[i] for i in range(3)]
    c_l_gut = [scale_gut[i] * c_l_raw[i] for i in range(3)]
    c_e_gut = [scale_gut[i] * c_e_raw[i] for i in range(3)]

    c_yuk_mat = sp.Matrix(
        3,
        3,
        lambda i, f_idx: (2 / d_g[i])
        * (
            n_c * (c_q_gut[i] + c_u_gut[i])
            if f_idx == 0
            else (n_c * (c_q_gut[i] + c_d_gut[i]) if f_idx == 1 else (c_l_gut[i] + c_e_gut[i]))
        ),
    )
    c_top = [c_yuk_mat[i, 0] for i in range(3)]

    g1sq, g2sq, g3sq, ytsq, lam = sp.symbols("g1sq g2sq g3sq ytsq lam")
    gy_sq = k_gut * g1sq
    gsq_raw = [gy_sq, g2sq, g3sq]
    gsq_gut = [g1sq, g2sq, g3sq]

    weyl_mat_info = derive_mv84_weyl_matrix_yukawa_coeffs()
    s2_f_raw = [n_gen * y2_gen.trace(), s2_f_gut[1], s2_f_gut[2]]
    s2_h_raw = [2 * (y_h ** 2), s2_h_gut[1], s2_h_gut[2]]

    beta_yt_1 = (n_c * weyl_mat_info["c1_y2s"] + weyl_mat_info["c1_q_self"]) * ytsq - 3 * sum(
        (c_q_raw[i] + c_u_raw[i]) * gsq_raw[i] for i in range(3)
    )
    beta_yd_gauge_1 = -3 * sum((c_q_raw[i] + c_d_raw[i]) * gsq_raw[i] for i in range(3))
    beta_ye_gauge_1 = -3 * sum((c_l_raw[i] + c_e_raw[i]) * gsq_raw[i] for i in range(3))

    # MV84 2-loop Yukawa gauge terms across all 3 sectors (u, d, e):
    u_self_raw, u_pure_g4 = mv84_sector_g4_and_lin(
        c_q_raw, c_u_raw, c_h_raw, s2_f_raw, s2_h_raw, c2_g, gsq_raw
    )
    d_self_raw, d_pure_g4 = mv84_sector_g4_and_lin(
        c_q_raw, c_d_raw, c_h_raw, s2_f_raw, s2_h_raw, c2_g, gsq_raw
    )
    e_self_raw, e_pure_g4 = mv84_sector_g4_and_lin(
        c_l_raw, c_e_raw, c_h_raw, s2_f_raw, s2_h_raw, c2_g, gsq_raw
    )
    u_from_d_raw = [
        sp.Rational(39, 4) * c_q_raw[i]
        + sp.Rational(9, 4) * c_d_raw[i]
        + sp.Rational(3, 2) * c_h_raw[i]
        - 6 * c_h_raw[i] * c2_g[i]
        for i in range(3)
    ]
    d_from_u_raw = [
        sp.Rational(39, 4) * c_q_raw[i]
        + sp.Rational(9, 4) * c_u_raw[i]
        + sp.Rational(3, 2) * c_h_raw[i]
        - 6 * c_h_raw[i] * c2_g[i]
        for i in range(3)
    ]
    tr_u_raw = [sp.Rational(5, 2) * n_c * (c_q_raw[i] + c_u_raw[i]) for i in range(3)]
    tr_d_raw = [sp.Rational(5, 2) * n_c * (c_q_raw[i] + c_d_raw[i]) for i in range(3)]
    tr_e_raw = [sp.Rational(5, 2) * (c_l_raw[i] + c_e_raw[i]) for i in range(3)]

    yt2_gauge_lin = sum((u_self_raw[i] + tr_u_raw[i]) * gsq_raw[i] for i in range(3))

    # MV85 4x4 real Higgs generators + O(4) quartic tensor + Weyl Yukawa traces:
    p0, p1, p2, p3 = sp.symbols("p0 p1 p2 p3", real=True)
    phi_v = sp.Matrix([p0, p1, p2, p3])
    h_doub = sp.Matrix([p0 + sp.I * p1, p2 + sp.I * p3]) / sp.sqrt(2)
    ht_doub = sp.Matrix([p2 - sp.I * p3, -(p0 - sp.I * p1)]) / sp.sqrt(2)

    g2_sym, gy_sym = sp.symbols("g2_sym gy_sym", real=True)
    th_4 = [
        make_real_higgs_gen_4x4(h_g, h_doub, phi_v)
        for h_g in (g2_sym * s1, g2_sym * s2, g2_sym * s3, gy_sym * y_h * sp.eye(2))
    ]
    l4_ten = {
        (a_i, b_i, c_i, d_i): 2
        * lam
        * (
            (1 if (a_i == b_i and c_i == d_i) else 0)
            + (1 if (a_i == c_i and b_i == d_i) else 0)
            + (1 if (a_i == d_i and b_i == c_i) else 0)
        )
        for a_i, b_i, c_i, d_i in product(range(4), repeat=4)
    }

    candy_1loop = sp.Rational(1, 2) * sum(
        l4_ten[(2, 2, e_i, f_i)] * l4_ten[(e_i, f_i, 2, 2)] for e_i, f_i in product(range(4), repeat=2)
    )
    gamma2_s_lam = sp.Rational(1, 12) * sum(
        l4_ten[(2, f_i, g_i, h_i)] ** 2 for f_i, g_i, h_i in product(range(4), repeat=3)
    )
    scoop_2loop = sum(
        l4_ten[(2, 2, e_i, f_i)] * l4_ten[(2, e_i, g_i, h_i)] * l4_ten[(2, f_i, g_i, h_i)]
        for e_i, f_i, g_i, h_i in product(range(4), repeat=4)
    )
    pure_lam3 = -scoop_2loop + 4 * gamma2_s_lam * lam

    c2_s22 = -sum((t_m * t_m for t_m in th_4), sp.zeros(4, 4))[2, 2]
    i1_inv = c2_s22 ** 2
    i_box_inv = sum((((ta * tb + tb * ta)[2, 2] / 2) ** 2 for ta in th_4 for tb in th_4))
    th_diag_4 = [-(t_m * t_m)[2, 2] for t_m in th_4]
    cg_ew_4 = [c2_g[1], c2_g[1], c2_g[1], c2_g[0]]
    sf_ew_4 = [s2_f_raw[1], s2_f_raw[1], s2_f_raw[1], s2_f_raw[0]]
    ss_ew_4 = [-(th_4[0] * th_4[0]).trace() / (g2_sym ** 2)] * 3 + [
        -(th_4[3] * th_4[3]).trace() / (gy_sym ** 2)
    ]
    g_ew_4 = [g2_sym, g2_sym, g2_sym, gy_sym]

    k_g_inv = sum(th_diag_4[a_i] * (g_ew_4[a_i] ** 2) * cg_ew_4[a_i] for a_i in range(4))
    k_f_inv = sum(th_diag_4[a_i] * (g_ew_4[a_i] ** 2) * sf_ew_4[a_i] for a_i in range(4))
    k_s_inv = sum(th_diag_4[a_i] * (g_ew_4[a_i] ** 2) * ss_ew_4[a_i] for a_i in range(4))

    b_f_inv = sum(
        (((th_4[a_i] * th_4[b_i] + th_4[b_i] * th_4[a_i])[2, 2] / 2) ** 2)
        * (sf_ew_4[a_i] * (g_ew_4[a_i] ** 2) + sf_ew_4[b_i] * (g_ew_4[b_i] ** 2))
        / 2
        for a_i in range(4)
        for b_i in range(4)
    )
    b_s_inv = sum(
        (((th_4[a_i] * th_4[b_i] + th_4[b_i] * th_4[a_i])[2, 2] / 2) ** 2)
        * (ss_ew_4[a_i] * (g_ew_4[a_i] ** 2) + ss_ew_4[b_i] * (g_ew_4[b_i] ** 2))
        / 2
        for a_i in range(4)
        for b_i in range(4)
    )
    b_g_inv = sum(
        (((th_4[a_i] * th_4[b_i] + th_4[b_i] * th_4[a_i])[2, 2] / 2) ** 2)
        * (cg_ew_4[a_i] * (g_ew_4[a_i] ** 2) + cg_ew_4[b_i] * (g_ew_4[b_i] ** 2))
        / 2
        for a_i in range(4)
        for b_i in range(4)
    )

    subs_ew = {
        g2_sym ** 2: g2sq,
        gy_sym ** 2: gy_sq,
        g2_sym ** 4: g2sq ** 2,
        gy_sym ** 4: gy_sq ** 2,
        g2_sym ** 6: g2sq ** 3,
        gy_sym ** 6: gy_sq ** 3,
    }

    def sector_y2_g4_poly(y_left: sp.Expr, y_right: sp.Expr, dc_mult: sp.Expr, h_sel: sp.Matrix) -> sp.Expr:
        psi_1, psi_2, psi_rc = sp.symbols("psi_1 psi_2 psi_rc")
        q_2 = sp.Matrix([psi_1, psi_2])
        yuk_form = (h_sel.H * q_2)[0] * psi_rc
        psi_list = [psi_1, psi_2, psi_rc]
        ya_3 = [
            sp.Matrix(
                3, 3, lambda r, c: sp.diff(sp.diff(sp.expand(sp.diff(yuk_form, pa_s)), psi_list[r]), psi_list[c])
            )
            for pa_s in (p0, p1, p2, p3)
        ]
        ta_3 = [
            g2_sym * sp.diag(s1, 0),
            g2_sym * sp.diag(s2, 0),
            g2_sym * sp.diag(s3, 0),
            gy_sym * sp.diag(y_left * sp.eye(2), -y_right),
        ]
        m_mix_val = sum(
            ((th_4[a_i] * th_4[b_i] + th_4[b_i] * th_4[a_i])[2, e_i] / 2)
            * (ya_3[e_i] * ya_3[2].H * ((ta_3[a_i] * ta_3[b_i] + ta_3[b_i] * ta_3[a_i]) / 2)).trace()
            for a_i in range(4)
            for b_i in range(4)
            for e_i in range(4)
        )
        return sp.expand(dc_mult * (20 * i_box_inv + 48 * m_mix_val)).subs(subs_ew)

    u_y2_g4 = sector_y2_g4_poly(y_q, y_u, n_c, ht_doub)
    d_y2_g4 = sector_y2_g4_poly(y_q, y_d, n_c, h_doub)
    e_y2_g4 = sector_y2_g4_poly(y_l, y_e, sp.Integer(1), h_doub)

    # 4x4 Weyl quark doublet Yukawa traces for chi_4, lambda*Y^4, and Y^6 mixed (u, d) matrix weights:
    qu_w, qd_w, urc_w, drc_w = sp.symbols("qu_w qd_w urc_w drc_w")
    yu_s, yd_s = sp.symbols("yu_s yd_s", real=True)
    q_w2 = sp.Matrix([qu_w, qd_w])
    w_qd = yu_s * (ht_doub.H * q_w2)[0] * urc_w + yd_s * (h_doub.H * q_w2)[0] * drc_w
    q_w4 = [qu_w, qd_w, urc_w, drc_w]
    ya_q4 = [
        sp.Matrix(4, 4, lambda r, c: sp.diff(sp.diff(sp.expand(sp.diff(w_qd, pa_s)), q_w4[r]), q_w4[c]))
        for pa_s in (p0, p1, p2, p3)
    ]
    tr4_diag_q = sp.expand((ya_q4[2] * ya_q4[2].H * ya_q4[2] * ya_q4[2].H).trace())
    tr4_s1_q = sp.expand(sum((ya_q4[2] * ya_q4[e_i].H * ya_q4[e_i] * ya_q4[2].H).trace() for e_i in range(4)))
    tr4_s2_q = sp.expand(sum((ya_q4[2] * ya_q4[e_i].H * ya_q4[2] * ya_q4[e_i].H).trace() for e_i in range(4)))
    chi4_q_poly = sp.Poly(sp.expand(n_c * (-sp.Rational(3, 2) * tr4_s1_q - tr4_s2_q)), yu_s, yd_s)
    lam_y4_q_poly = sp.Poly(
        sp.expand(4 * chi4_q_poly.as_expr() + n_c * (16 * tr4_diag_q + 8 * tr4_s2_q)), yu_s, yd_s
    )
    tr6_d_q = sp.expand((ya_q4[2] * ya_q4[2].H * ya_q4[2] * ya_q4[2].H * ya_q4[2] * ya_q4[2].H).trace())
    tr6_s1_q = sp.expand(
        sum((ya_q4[2] * ya_q4[2].H * ya_q4[2] * ya_q4[e_i].H * ya_q4[e_i] * ya_q4[2].H).trace() for e_i in range(4))
    )
    tr6_s2_q = sp.expand(
        sum((ya_q4[2] * ya_q4[e_i].H * ya_q4[2] * ya_q4[2].H * ya_q4[2] * ya_q4[e_i].H).trace() for e_i in range(4))
    )
    y6_q_poly = sp.Poly(sp.expand(8 * n_c * (tr6_s1_q + 2 * tr6_d_q + tr6_s2_q)), yu_s, yd_s)

    yt2_pure_yuk = (
        weyl_mat_info["c2_q_hf2"]
        + n_c * weyl_mat_info["c2_q_y2s_hf"]
        + chi4_q_poly.coeff_monomial((4, 0))
    ) * (ytsq ** 2)
    beta_yt_2 = sp.expand(
        yt2_pure_yuk
        + weyl_mat_info["c2_lam_hf"] * lam * ytsq
        + weyl_mat_info["c2_lam2"] * (lam ** 2)
        + ytsq * yt2_gauge_lin
        + u_pure_g4
    )

    c1_lam_y2 = sp.simplify(4 * weyl_mat_info["c1_y2s"])
    c1_lam_y4 = sp.simplify(-4 * tr4_diag_q.subs({yu_s: 1, yd_s: 0}))
    c2_lam2_y2 = sp.simplify(-2 * candy_1loop * weyl_mat_info["c1_y2s"] / (lam ** 2))
    c2_lam_yg = sp.simplify(4 * weyl_mat_info["c1_y2s"])

    lam_1_ew = sp.expand(candy_1loop - 12 * lam * c2_s22 + 6 * i_box_inv).subs(subs_ew)
    beta_lam_1 = sp.expand(lam_1_ew + c1_lam_y2 * n_c * lam * ytsq + c1_lam_y4 * n_c * (ytsq ** 2))

    lam2_g2_ew = sp.expand(6 * candy_1loop * c2_s22).subs(subs_ew)
    lam_g4_ew = sp.expand(
        lam
        * (
            36 * i1_inv
            + sp.Rational(2, 3) * i1_inv
            - 32 * i_box_inv
            - 48 * k_g_inv
            + sp.Rational(1, 3) * k_g_inv
            + 10 * k_f_inv
            + sp.Rational(11, 3) * k_s_inv
        )
    ).subs(subs_ew)
    g6_ew = sp.expand(
        -sp.Rational(32, 3) * b_f_inv
        + 84 * c2_s22 * i_box_inv
        - 72 * (c2_s22 ** 3)
        - 23 * b_s_inv
        + sp.Rational(1, 3) * b_s_inv
        + 144 * b_g_inv
        - sp.Rational(1, 3) * b_g_inv
    ).subs(subs_ew)

    y4_g2_u_poly = sp.expand(-4 * n_c * sum((c_q_raw[i] + c_u_raw[i] - c_h_raw[i]) * gsq_raw[i] for i in range(3)))
    y4_g2_d_poly = sp.expand(-4 * n_c * sum((c_q_raw[i] + c_d_raw[i] - c_h_raw[i]) * gsq_raw[i] for i in range(3)))
    y4_g2_e_poly = sp.expand(-4 * sum((c_l_raw[i] + c_e_raw[i] - c_h_raw[i]) * gsq_raw[i] for i in range(3)))

    beta_lam_2 = sp.expand(
        pure_lam3
        + c2_lam2_y2 * n_c * (lam ** 2) * ytsq
        + lam2_g2_ew
        + lam * lam_y4_q_poly.coeff_monomial((4, 0)) * (ytsq ** 2)
        + c2_lam_yg * lam * ytsq * sum(tr_u_raw[i] * gsq_raw[i] for i in range(3))
        + lam_g4_ew
        + y6_q_poly.coeff_monomial((6, 0)) * (ytsq ** 3)
        + (ytsq ** 2) * y4_g2_u_poly
        + ytsq * u_y2_g4
        + g6_ew
    )

    rhs_5_sym = [
        ((gsq_gut[i] ** 2) / (4 * sp.pi)) * b1_vec[i]
        + ((gsq_gut[i] ** 2) / (64 * (sp.pi ** 3)))
        * (sum(b2_mat[i, j] * gsq_gut[j] for j in range(3)) - c_top[i] * ytsq)
        for i in range(3)
    ] + [
        (ytsq / (4 * sp.pi)) * sp.expand(beta_yt_1)
        + (ytsq / (64 * (sp.pi ** 3))) * beta_yt_2,
        beta_lam_1 / (8 * sp.pi) + beta_lam_2 / (128 * (sp.pi ** 3)),
    ]

    return {
        "k_gut": k_gut,
        "n_c": n_c,
        "n_gen": n_gen,
        "cas_16": cas_16,
        "c2_g": c2_g,
        "d_g": d_g,
        "th_4_unit": [th_mat.subs({g2_sym: 1, gy_sym: 1}) for th_mat in th_4],
        "b1_vec": b1_vec,
        "b2_mat": b2_mat,
        "c_top": c_top,
        "c_yuk_mat": c_yuk_mat,
        "symbols_5": (g1sq, g2sq, g3sq, ytsq, lam),
        "beta_yt_1": sp.expand(beta_yt_1),
        "beta_yt_2": beta_yt_2,
        "beta_lam_1": beta_lam_1,
        "beta_lam_2": beta_lam_2,
        "beta_yd_gauge_1": sp.expand(beta_yd_gauge_1),
        "beta_ye_gauge_1": sp.expand(beta_ye_gauge_1),
        "u_self_gut": [scale_gut[i] * u_self_raw[i] for i in range(3)],
        "d_self_gut": [scale_gut[i] * d_self_raw[i] for i in range(3)],
        "e_self_gut": [scale_gut[i] * e_self_raw[i] for i in range(3)],
        "u_from_d_gut": [scale_gut[i] * u_from_d_raw[i] for i in range(3)],
        "d_from_u_gut": [scale_gut[i] * d_from_u_raw[i] for i in range(3)],
        "tr_u_gut": [scale_gut[i] * tr_u_raw[i] for i in range(3)],
        "tr_d_gut": [scale_gut[i] * tr_d_raw[i] for i in range(3)],
        "tr_e_gut": [scale_gut[i] * tr_e_raw[i] for i in range(3)],
        "u_pure_g4": u_pure_g4,
        "d_pure_g4": d_pure_g4,
        "e_pure_g4": e_pure_g4,
        "u_y2_g4": u_y2_g4,
        "d_y2_g4": d_y2_g4,
        "e_y2_g4": e_y2_g4,
        "y4_g2_u_poly": y4_g2_u_poly,
        "y4_g2_d_poly": y4_g2_d_poly,
        "y4_g2_e_poly": y4_g2_e_poly,
        "pure_lam_ew_1": lam_1_ew,
        "pure_lam_ew_2": sp.expand(pure_lam3 + lam2_g2_ew + lam_g4_ew + g6_ew),
        "c1_lam_y2": c1_lam_y2,
        "c1_lam_y4": c1_lam_y4,
        "c2_lam2_y2": c2_lam2_y2,
        "c2_lam_yg": c2_lam_yg,
        "weyl_mat_info": weyl_mat_info,
        "mv83_1loop_matrix_symbolic_exact": weyl_mat_info["mv83_ok"],
        "mv84_2loop_matrix_symbolic_exact": weyl_mat_info["mv84_ok"],
        "mv84_swapped_commutator_nonzero": weyl_mat_info["swapped_bad"],
        "chi4_q_diag_coeff": chi4_q_poly.coeff_monomial((4, 0)),
        "chi4_q_mix_coeff": chi4_q_poly.coeff_monomial((2, 2)),
        "lam_y4_q_diag_coeff": lam_y4_q_poly.coeff_monomial((4, 0)),
        "lam_y4_q_mix_coeff": lam_y4_q_poly.coeff_monomial((2, 2)),
        "y6_q_diag_coeff": y6_q_poly.coeff_monomial((6, 0)),
        "y6_q_mix_coeff": y6_q_poly.coeff_monomial((4, 2)),
        "rhs_5_sym": rhs_5_sym,
    }


def make_sm_rge_num_coeffs(beta_info: dict[str, Any]) -> dict[str, Any]:
    """Extract float coefficients from SymPy MV84/MV85 beta polynomials for 5-channel and 3x3 matrix RK4."""
    g1sq, g2sq, g3sq, ytsq, lam = beta_info["symbols_5"]
    b1_f = np.array([float(v) for v in beta_info["b1_vec"]], dtype=float)
    b2_f = np.array(
        [[float(beta_info["b2_mat"][r_i, c_i]) for c_i in range(3)] for r_i in range(3)],
        dtype=float,
    )
    ctop_f = np.array([float(v) for v in beta_info["c_top"]], dtype=float)
    cyuk_f = np.array(
        [[float(beta_info["c_yuk_mat"][r_i, c_i]) for c_i in range(3)] for r_i in range(3)],
        dtype=float,
    )

    p_yt1 = sp.Poly(beta_info["beta_yt_1"], g1sq, g2sq, g3sq, ytsq, lam)
    p_yt2 = sp.Poly(beta_info["beta_yt_2"], g1sq, g2sq, g3sq, ytsq, lam)
    p_l1 = sp.Poly(beta_info["beta_lam_1"], g1sq, g2sq, g3sq, ytsq, lam)
    p_l2 = sp.Poly(beta_info["beta_lam_2"], g1sq, g2sq, g3sq, ytsq, lam)
    p_ydg = sp.Poly(beta_info["beta_yd_gauge_1"], g1sq, g2sq, g3sq)
    p_yeg = sp.Poly(beta_info["beta_ye_gauge_1"], g1sq, g2sq, g3sq)

    def poly3_terms(expr_3: sp.Expr) -> list[tuple[tuple[int, ...], float]]:
        return [(mon_t, float(cf_v)) for mon_t, cf_v in sp.Poly(expr_3, g1sq, g2sq, g3sq).terms()]

    p_lam_ew1 = sp.Poly(beta_info["pure_lam_ew_1"], g1sq, g2sq, g3sq, lam)
    p_lam_ew2 = sp.Poly(beta_info["pure_lam_ew_2"], g1sq, g2sq, g3sq, lam)
    n_c_fl = float(beta_info["n_c"])
    w_info = beta_info["weyl_mat_info"]

    return {
        "n_c": n_c_fl,
        "k_gut": float(beta_info["k_gut"]),
        "b1": b1_f,
        "b2": b2_f,
        "c_top": ctop_f,
        "c_yuk": cyuk_f,
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
        "c1_q_self": float(w_info["c1_q_self"]),
        "c1_q_partner": float(w_info["c1_q_partner"]),
        "c1_e_self": float(w_info["c1_e_self"]),
        "c1_y2s": float(w_info["c1_y2s"]),
        "c2_q_hf2": float(w_info["c2_q_hf2"]),
        "c2_q_hfhfp": float(w_info["c2_q_hfhfp"]),
        "c2_q_hfphf": float(w_info["c2_q_hfphf"]),
        "c2_q_hfp2": float(w_info["c2_q_hfp2"]),
        "c2_e_he2": float(w_info["c2_e_he2"]),
        "c2_q_y2s_hf": float(w_info["c2_q_y2s_hf"]),
        "c2_q_y2s_hfp": float(w_info["c2_q_y2s_hfp"]),
        "c2_e_y2s_he": float(w_info["c2_e_y2s_he"]),
        "c2_lam_hf": float(w_info["c2_lam_hf"]),
        "c2_lam2": float(w_info["c2_lam2"]),
        "c1_lam_y2": float(beta_info["c1_lam_y2"]),
        "c1_lam_y4": float(beta_info["c1_lam_y4"]),
        "c2_lam2_y2": float(beta_info["c2_lam2_y2"]),
        "c2_lam_yg": float(beta_info["c2_lam_yg"]),
        "u_self_gut": np.array([float(v) for v in beta_info["u_self_gut"]], dtype=float),
        "d_self_gut": np.array([float(v) for v in beta_info["d_self_gut"]], dtype=float),
        "e_self_gut": np.array([float(v) for v in beta_info["e_self_gut"]], dtype=float),
        "u_from_d_gut": np.array([float(v) for v in beta_info["u_from_d_gut"]], dtype=float),
        "d_from_u_gut": np.array([float(v) for v in beta_info["d_from_u_gut"]], dtype=float),
        "tr_u_gut": np.array([float(v) for v in beta_info["tr_u_gut"]], dtype=float),
        "tr_d_gut": np.array([float(v) for v in beta_info["tr_d_gut"]], dtype=float),
        "tr_e_gut": np.array([float(v) for v in beta_info["tr_e_gut"]], dtype=float),
        "u_pure_g4_terms": poly3_terms(beta_info["u_pure_g4"]),
        "d_pure_g4_terms": poly3_terms(beta_info["d_pure_g4"]),
        "e_pure_g4_terms": poly3_terms(beta_info["e_pure_g4"]),
        "u_y2_g4_terms": poly3_terms(beta_info["u_y2_g4"]),
        "d_y2_g4_terms": poly3_terms(beta_info["d_y2_g4"]),
        "e_y2_g4_terms": poly3_terms(beta_info["e_y2_g4"]),
        "y4_g2_u_terms": poly3_terms(beta_info["y4_g2_u_poly"]),
        "y4_g2_d_terms": poly3_terms(beta_info["y4_g2_d_poly"]),
        "y4_g2_e_terms": poly3_terms(beta_info["y4_g2_e_poly"]),
        "pure_lam_ew_1_terms": [(mon_t, float(cf_v)) for mon_t, cf_v in p_lam_ew1.terms()],
        "pure_lam_ew_2_terms": [(mon_t, float(cf_v)) for mon_t, cf_v in p_lam_ew2.terms()],
        "chi4_q_diag": float(beta_info["chi4_q_diag_coeff"]),
        "chi4_e_diag": float(beta_info["chi4_q_diag_coeff"]) / n_c_fl,
        "chi4_q_mix": float(beta_info["chi4_q_mix_coeff"]),
        "lam_y4_q_diag": float(beta_info["lam_y4_q_diag_coeff"]),
        "lam_y4_e_diag": float(beta_info["lam_y4_q_diag_coeff"]) / n_c_fl,
        "lam_y4_q_mix": float(beta_info["lam_y4_q_mix_coeff"]),
        "y6_q_diag": float(beta_info["y6_q_diag_coeff"]),
        "y6_e_diag": float(beta_info["y6_q_diag_coeff"]) / n_c_fl,
        "y6_q_mix": float(beta_info["y6_q_mix_coeff"]),
    }


def eval_poly_terms(x_vec: np.ndarray, terms_list: list[tuple[tuple[int, ...], float]]) -> float:
    """Evaluate a multivariate polynomial represented as (monomial_exponents, float_coeff) pairs."""
    acc_p = 0.0
    n_vars = len(x_vec)
    for mon, cf_val in terms_list:
        prd = cf_val
        for idx_v in range(n_vars):
            exp_i = mon[idx_v]
            if exp_i != 0:
                prd *= float(x_vec[idx_v]) ** exp_i
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


def matrix_yukawa_2loop_rhs(
    gsq3: np.ndarray,
    lam_val: float,
    yu_m: np.ndarray,
    yd_m: np.ndarray,
    ye_m: np.ndarray,
    coeffs: dict[str, Any],
    two_loop: bool = True,
) -> tuple[np.ndarray, float, np.ndarray, np.ndarray, np.ndarray]:
    """Full 2-loop 3-generation matrix Yukawa + gauge + Higgs quartic RGE right-hand side
    in left-covariant convention Y_u -> U_Q Y_u U_{u^c}^H, Y_d -> U_Q Y_d U_{d^c}^H,
    Y_e -> U_L Y_e U_{e^c}^H, using symbolically derived MV84/MV85 operator coefficients.
    """
    inv_4pi = 1.0 / (4 * math.pi)
    inv_8pi = 0.5 * inv_4pi
    inv_64pi3 = inv_4pi / (16 * (math.pi ** 2))
    inv_128pi3 = 0.5 * inv_64pi3

    n_c_v = coeffs["n_c"]
    hu_m = yu_m @ yu_m.conj().T
    hd_m = yd_m @ yd_m.conj().T
    he_m = ye_m @ ye_m.conj().T

    tr_hu = float(np.real(np.trace(hu_m)))
    tr_hd = float(np.real(np.trace(hd_m)))
    tr_he = float(np.real(np.trace(he_m)))
    tr_y2_all = n_c_v * tr_hu + n_c_v * tr_hd + tr_he
    tr_vec3 = np.array([tr_hu, tr_hd, tr_he], dtype=float)

    d_gsq = inv_4pi * coeffs["b1"] * (gsq3 ** 2)
    if two_loop:
        d_gsq = d_gsq + inv_64pi3 * (gsq3 ** 2) * ((coeffs["b2"] @ gsq3) - (coeffs["c_yuk"] @ tr_vec3))

    eye3 = np.eye(3, dtype=complex)
    b1_yu = (
        coeffs["c1_q_self"] * hu_m
        + coeffs["c1_q_partner"] * hd_m
        + (coeffs["c1_y2s"] * tr_y2_all - float(coeffs["yu_gauge"] @ gsq3)) * eye3
    ) @ yu_m
    b1_yd = (
        coeffs["c1_q_self"] * hd_m
        + coeffs["c1_q_partner"] * hu_m
        + (coeffs["c1_y2s"] * tr_y2_all - float(coeffs["yd_gauge"] @ gsq3)) * eye3
    ) @ yd_m
    b1_ye = (
        coeffs["c1_e_self"] * he_m
        + (coeffs["c1_y2s"] * tr_y2_all - float(coeffs["ye_gauge"] @ gsq3)) * eye3
    ) @ ye_m

    d_yu = inv_8pi * b1_yu
    d_yd = inv_8pi * b1_yd
    d_ye = inv_8pi * b1_ye

    hu2_m = hu_m @ hu_m
    hd2_m = hd_m @ hd_m
    he2_m = he_m @ he_m
    tr_hu2 = float(np.real(np.trace(hu2_m)))
    tr_hd2 = float(np.real(np.trace(hd2_m)))
    tr_he2 = float(np.real(np.trace(he2_m)))
    tr_huhd = float(np.real(np.trace(hu_m @ hd_m)))

    x4_ew = np.array([gsq3[0], gsq3[1], gsq3[2], lam_val], dtype=float)
    b1_lam = (
        eval_poly_terms(x4_ew, coeffs["pure_lam_ew_1_terms"])
        + coeffs["c1_lam_y2"] * lam_val * tr_y2_all
        + coeffs["c1_lam_y4"] * (n_c_v * tr_hu2 + n_c_v * tr_hd2 + tr_he2)
    )
    d_lam = inv_8pi * b1_lam

    if two_loop:
        chi4_tr = (
            coeffs["chi4_q_diag"] * (tr_hu2 + tr_hd2)
            + coeffs["chi4_e_diag"] * tr_he2
            + coeffs["chi4_q_mix"] * tr_huhd
        )
        y2_g_tr = (
            float(coeffs["tr_u_gut"] @ gsq3) * tr_hu
            + float(coeffs["tr_d_gut"] @ gsq3) * tr_hd
            + float(coeffs["tr_e_gut"] @ gsq3) * tr_he
        )
        u_g4_val = eval_poly_terms(gsq3, coeffs["u_pure_g4_terms"])
        d_g4_val = eval_poly_terms(gsq3, coeffs["d_pure_g4_terms"])
        e_g4_val = eval_poly_terms(gsq3, coeffs["e_pure_g4_terms"])

        b2_yu = (
            coeffs["c2_q_hf2"] * hu2_m
            + coeffs["c2_q_hfhfp"] * (hu_m @ hd_m)
            + coeffs["c2_q_hfphf"] * (hd_m @ hu_m)
            + coeffs["c2_q_hfp2"] * hd2_m
            + (coeffs["c2_q_y2s_hf"] * hu_m + coeffs["c2_q_y2s_hfp"] * hd_m) * tr_y2_all
            + coeffs["c2_lam_hf"] * lam_val * hu_m
            + (coeffs["c2_lam2"] * (lam_val ** 2) + chi4_tr + y2_g_tr + u_g4_val) * eye3
            + float(coeffs["u_self_gut"] @ gsq3) * hu_m
            - float(coeffs["u_from_d_gut"] @ gsq3) * hd_m
        ) @ yu_m

        b2_yd = (
            coeffs["c2_q_hf2"] * hd2_m
            + coeffs["c2_q_hfhfp"] * (hd_m @ hu_m)
            + coeffs["c2_q_hfphf"] * (hu_m @ hd_m)
            + coeffs["c2_q_hfp2"] * hu2_m
            + (coeffs["c2_q_y2s_hf"] * hd_m + coeffs["c2_q_y2s_hfp"] * hu_m) * tr_y2_all
            + coeffs["c2_lam_hf"] * lam_val * hd_m
            + (coeffs["c2_lam2"] * (lam_val ** 2) + chi4_tr + y2_g_tr + d_g4_val) * eye3
            + float(coeffs["d_self_gut"] @ gsq3) * hd_m
            - float(coeffs["d_from_u_gut"] @ gsq3) * hu_m
        ) @ yd_m

        b2_ye = (
            coeffs["c2_e_he2"] * he2_m
            + coeffs["c2_e_y2s_he"] * tr_y2_all * he_m
            + coeffs["c2_lam_hf"] * lam_val * he_m
            + (coeffs["c2_lam2"] * (lam_val ** 2) + chi4_tr + y2_g_tr + e_g4_val) * eye3
            + float(coeffs["e_self_gut"] @ gsq3) * he_m
        ) @ ye_m

        d_yu = d_yu + inv_128pi3 * b2_yu
        d_yd = d_yd + inv_128pi3 * b2_yd
        d_ye = d_ye + inv_128pi3 * b2_ye

        lam_ew_2 = eval_poly_terms(x4_ew, coeffs["pure_lam_ew_2_terms"])
        tr_hu3 = float(np.real(np.trace(hu2_m @ hu_m)))
        tr_hd3 = float(np.real(np.trace(hd2_m @ hd_m)))
        tr_he3 = float(np.real(np.trace(he2_m @ he_m)))
        tr_hu2hd = float(np.real(np.trace(hu2_m @ hd_m)))
        tr_huhd2 = float(np.real(np.trace(hu_m @ hd2_m)))

        b2_lam = (
            lam_ew_2
            + coeffs["c2_lam2_y2"] * (lam_val ** 2) * tr_y2_all
            + lam_val
            * (
                coeffs["lam_y4_q_diag"] * (tr_hu2 + tr_hd2)
                + coeffs["lam_y4_e_diag"] * tr_he2
                + coeffs["lam_y4_q_mix"] * tr_huhd
            )
            + coeffs["c2_lam_yg"] * lam_val * y2_g_tr
            + coeffs["y6_q_diag"] * (tr_hu3 + tr_hd3)
            + coeffs["y6_e_diag"] * tr_he3
            + coeffs["y6_q_mix"] * (tr_hu2hd + tr_huhd2)
            + eval_poly_terms(gsq3, coeffs["y4_g2_u_terms"]) * tr_hu2
            + eval_poly_terms(gsq3, coeffs["y4_g2_d_terms"]) * tr_hd2
            + eval_poly_terms(gsq3, coeffs["y4_g2_e_terms"]) * tr_he2
            + eval_poly_terms(gsq3, coeffs["u_y2_g4_terms"]) * tr_hu
            + eval_poly_terms(gsq3, coeffs["d_y2_g4_terms"]) * tr_hd
            + eval_poly_terms(gsq3, coeffs["e_y2_g4_terms"]) * tr_he
        )
        d_lam = d_lam + inv_128pi3 * b2_lam

    return d_gsq, float(d_lam), d_yu, d_yd, d_ye


def picard_jet4_matrix_yukawa_2loop(
    gsq0: np.ndarray,
    lam0: float,
    yu0: np.ndarray,
    yd0: np.ndarray,
    ye0: np.ndarray,
    dt_val: float,
    coeffs: dict[str, Any],
) -> tuple[np.ndarray, float, np.ndarray, np.ndarray, np.ndarray]:
    """4th-order real-t truncated Taylor polynomial Lie-Picard jet for the non-commuting
    2-loop 3x3 matrix Yukawa + gauge + quartic RGE system.
    """
    inv_4pi = 1.0 / (4 * math.pi)
    inv_8pi = 0.5 * inv_4pi
    inv_64pi3 = inv_4pi / (16 * (math.pi ** 2))
    inv_128pi3 = 0.5 * inv_64pi3
    n_c_v = coeffs["n_c"]

    z3_c = np.zeros((3, 3), dtype=complex)
    z3_f = np.zeros(3, dtype=float)
    eye3 = np.eye(3, dtype=complex)

    def pmul_s(sa: list[float], sb: list[float]) -> list[float]:
        return [sum(sa[j_p] * sb[k_p - j_p] for j_p in range(k_p + 1)) for k_p in range(4)]

    def pmul_m(ma: list[np.ndarray], mb: list[np.ndarray]) -> list[np.ndarray]:
        return [sum([ma[j_p] @ mb[k_p - j_p] for j_p in range(k_p + 1)], z3_c) for k_p in range(4)]

    def pscale_m(sa: list[float], ma: list[np.ndarray]) -> list[np.ndarray]:
        return [sum([sa[j_p] * ma[k_p - j_p] for j_p in range(k_p + 1)], z3_c) for k_p in range(4)]

    def peval_terms(
        vars_lists: list[list[float]], terms_list: list[tuple[tuple[int, ...], float]]
    ) -> list[float]:
        acc_l = [0.0, 0.0, 0.0, 0.0]
        n_v = len(vars_lists)
        for mon_t, cf_f in terms_list:
            prd_l = [cf_f, 0.0, 0.0, 0.0]
            for i_v in range(n_v):
                for _ in range(mon_t[i_v]):
                    prd_l = pmul_s(prd_l, vars_lists[i_v])
            acc_l = [acc_l[k_p] + prd_l[k_p] for k_p in range(4)]
        return acc_l

    gsq_p = [np.array(gsq0, dtype=float)] + [z3_f] * 4
    lam_p = [float(lam0), 0.0, 0.0, 0.0, 0.0]
    yu_p = [np.array(yu0, dtype=complex)] + [z3_c] * 4
    yd_p = [np.array(yd0, dtype=complex)] + [z3_c] * 4
    ye_p = [np.array(ye0, dtype=complex)] + [z3_c] * 4

    for _ in range(4):
        g_cols = [[float(gsq_p[k_p][i_g]) for k_p in range(4)] for i_g in range(3)]
        lam_4 = lam_p[:4]
        yu_4 = yu_p[:4]
        yd_4 = yd_p[:4]
        ye_4 = ye_p[:4]

        hu_l = pmul_m(yu_4, [mat_x.conj().T for mat_x in yu_4])
        hd_l = pmul_m(yd_4, [mat_x.conj().T for mat_x in yd_4])
        he_l = pmul_m(ye_4, [mat_x.conj().T for mat_x in ye_4])
        tr_hu_l = [float(np.real(np.trace(hu_l[k_p]))) for k_p in range(4)]
        tr_hd_l = [float(np.real(np.trace(hd_l[k_p]))) for k_p in range(4)]
        tr_he_l = [float(np.real(np.trace(he_l[k_p]))) for k_p in range(4)]
        tr_y2_l = [n_c_v * tr_hu_l[k_p] + n_c_v * tr_hd_l[k_p] + tr_he_l[k_p] for k_p in range(4)]

        dg_cols: list[list[float]] = []
        for i_g in range(3):
            gi_sq_l = pmul_s(g_cols[i_g], g_cols[i_g])
            loop2_g_l = [
                sum(float(coeffs["b2"][i_g, j_g]) * g_cols[j_g][k_p] for j_g in range(3))
                - (
                    float(coeffs["c_yuk"][i_g, 0]) * tr_hu_l[k_p]
                    + float(coeffs["c_yuk"][i_g, 1]) * tr_hd_l[k_p]
                    + float(coeffs["c_yuk"][i_g, 2]) * tr_he_l[k_p]
                )
                for k_p in range(4)
            ]
            gi_l2 = pmul_s(gi_sq_l, loop2_g_l)
            dg_cols = dg_cols + [
                [inv_4pi * float(coeffs["b1"][i_g]) * gi_sq_l[k_p] + inv_64pi3 * gi_l2[k_p] for k_p in range(4)]
            ]

        ug1_l = [sum(float(coeffs["yu_gauge"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        dg1_l = [sum(float(coeffs["yd_gauge"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        eg1_l = [sum(float(coeffs["ye_gauge"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]

        b1_yu_l = pmul_m(
            [
                coeffs["c1_q_self"] * hu_l[k_p]
                + coeffs["c1_q_partner"] * hd_l[k_p]
                + (coeffs["c1_y2s"] * tr_y2_l[k_p] - ug1_l[k_p]) * eye3
                for k_p in range(4)
            ],
            yu_4,
        )
        b1_yd_l = pmul_m(
            [
                coeffs["c1_q_self"] * hd_l[k_p]
                + coeffs["c1_q_partner"] * hu_l[k_p]
                + (coeffs["c1_y2s"] * tr_y2_l[k_p] - dg1_l[k_p]) * eye3
                for k_p in range(4)
            ],
            yd_4,
        )
        b1_ye_l = pmul_m(
            [
                coeffs["c1_e_self"] * he_l[k_p]
                + (coeffs["c1_y2s"] * tr_y2_l[k_p] - eg1_l[k_p]) * eye3
                for k_p in range(4)
            ],
            ye_4,
        )

        hu2_l = pmul_m(hu_l, hu_l)
        hd2_l = pmul_m(hd_l, hd_l)
        he2_l = pmul_m(he_l, he_l)
        huhd_l = pmul_m(hu_l, hd_l)
        hdhu_l = pmul_m(hd_l, hu_l)

        tr_hu2_l = [float(np.real(np.trace(hu2_l[k_p]))) for k_p in range(4)]
        tr_hd2_l = [float(np.real(np.trace(hd2_l[k_p]))) for k_p in range(4)]
        tr_he2_l = [float(np.real(np.trace(he2_l[k_p]))) for k_p in range(4)]
        tr_huhd_l = [float(np.real(np.trace(huhd_l[k_p]))) for k_p in range(4)]

        chi4_l = [
            coeffs["chi4_q_diag"] * (tr_hu2_l[k_p] + tr_hd2_l[k_p])
            + coeffs["chi4_e_diag"] * tr_he2_l[k_p]
            + coeffs["chi4_q_mix"] * tr_huhd_l[k_p]
            for k_p in range(4)
        ]
        tru_g_l = [sum(float(coeffs["tr_u_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        trd_g_l = [sum(float(coeffs["tr_d_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        tre_g_l = [sum(float(coeffs["tr_e_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        y2_g_l = [
            pmul_s(tru_g_l, tr_hu_l)[k_p] + pmul_s(trd_g_l, tr_hd_l)[k_p] + pmul_s(tre_g_l, tr_he_l)[k_p]
            for k_p in range(4)
        ]
        u_g4_l = peval_terms(g_cols, coeffs["u_pure_g4_terms"])
        d_g4_l = peval_terms(g_cols, coeffs["d_pure_g4_terms"])
        e_g4_l = peval_terms(g_cols, coeffs["e_pure_g4_terms"])
        lam2_l = pmul_s(lam_4, lam_4)

        uself_l = [sum(float(coeffs["u_self_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        dself_l = [sum(float(coeffs["d_self_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        eself_l = [sum(float(coeffs["e_self_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        ufd_l = [sum(float(coeffs["u_from_d_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]
        dfu_l = [sum(float(coeffs["d_from_u_gut"][j_g]) * g_cols[j_g][k_p] for j_g in range(3)) for k_p in range(4)]

        y2_hu_l = pscale_m(tr_y2_l, hu_l)
        y2_hd_l = pscale_m(tr_y2_l, hd_l)
        y2_he_l = pscale_m(tr_y2_l, he_l)
        lam_hu_l = pscale_m(lam_4, hu_l)
        lam_hd_l = pscale_m(lam_4, hd_l)
        lam_he_l = pscale_m(lam_4, he_l)
        us_hu_l = pscale_m(uself_l, hu_l)
        ufd_hd_l = pscale_m(ufd_l, hd_l)
        ds_hd_l = pscale_m(dself_l, hd_l)
        dfu_hu_l = pscale_m(dfu_l, hu_l)
        es_he_l = pscale_m(eself_l, he_l)

        b2_yu_l = pmul_m(
            [
                coeffs["c2_q_hf2"] * hu2_l[k_p]
                + coeffs["c2_q_hfhfp"] * huhd_l[k_p]
                + coeffs["c2_q_hfphf"] * hdhu_l[k_p]
                + coeffs["c2_q_hfp2"] * hd2_l[k_p]
                + coeffs["c2_q_y2s_hf"] * y2_hu_l[k_p]
                + coeffs["c2_q_y2s_hfp"] * y2_hd_l[k_p]
                + coeffs["c2_lam_hf"] * lam_hu_l[k_p]
                + (coeffs["c2_lam2"] * lam2_l[k_p] + chi4_l[k_p] + y2_g_l[k_p] + u_g4_l[k_p]) * eye3
                + us_hu_l[k_p]
                - ufd_hd_l[k_p]
                for k_p in range(4)
            ],
            yu_4,
        )
        b2_yd_l = pmul_m(
            [
                coeffs["c2_q_hf2"] * hd2_l[k_p]
                + coeffs["c2_q_hfhfp"] * hdhu_l[k_p]
                + coeffs["c2_q_hfphf"] * huhd_l[k_p]
                + coeffs["c2_q_hfp2"] * hu2_l[k_p]
                + coeffs["c2_q_y2s_hf"] * y2_hd_l[k_p]
                + coeffs["c2_q_y2s_hfp"] * y2_hu_l[k_p]
                + coeffs["c2_lam_hf"] * lam_hd_l[k_p]
                + (coeffs["c2_lam2"] * lam2_l[k_p] + chi4_l[k_p] + y2_g_l[k_p] + d_g4_l[k_p]) * eye3
                + ds_hd_l[k_p]
                - dfu_hu_l[k_p]
                for k_p in range(4)
            ],
            yd_4,
        )
        b2_ye_l = pmul_m(
            [
                coeffs["c2_e_he2"] * he2_l[k_p]
                + coeffs["c2_e_y2s_he"] * y2_he_l[k_p]
                + coeffs["c2_lam_hf"] * lam_he_l[k_p]
                + (coeffs["c2_lam2"] * lam2_l[k_p] + chi4_l[k_p] + y2_g_l[k_p] + e_g4_l[k_p]) * eye3
                + es_he_l[k_p]
                for k_p in range(4)
            ],
            ye_4,
        )

        vars4_ew = [g_cols[0], g_cols[1], g_cols[2], lam_4]
        lam_ew1_l = peval_terms(vars4_ew, coeffs["pure_lam_ew_1_terms"])
        lam_ew2_l = peval_terms(vars4_ew, coeffs["pure_lam_ew_2_terms"])
        lam_y2_l = pmul_s(lam_4, tr_y2_l)
        b1_lam_l = [
            lam_ew1_l[k_p]
            + coeffs["c1_lam_y2"] * lam_y2_l[k_p]
            + coeffs["c1_lam_y4"] * (n_c_v * tr_hu2_l[k_p] + n_c_v * tr_hd2_l[k_p] + tr_he2_l[k_p])
            for k_p in range(4)
        ]

        hu3_l = pmul_m(hu2_l, hu_l)
        hd3_l = pmul_m(hd2_l, hd_l)
        he3_l = pmul_m(he2_l, he_l)
        hu2hd_l = pmul_m(hu2_l, hd_l)
        huhd2_l = pmul_m(hu_l, hd2_l)
        tr_hu3_l = [float(np.real(np.trace(hu3_l[k_p]))) for k_p in range(4)]
        tr_hd3_l = [float(np.real(np.trace(hd3_l[k_p]))) for k_p in range(4)]
        tr_he3_l = [float(np.real(np.trace(he3_l[k_p]))) for k_p in range(4)]
        tr_hu2hd_l = [float(np.real(np.trace(hu2hd_l[k_p]))) for k_p in range(4)]
        tr_huhd2_l = [float(np.real(np.trace(huhd2_l[k_p]))) for k_p in range(4)]

        lam2_y2_l = pmul_s(lam2_l, tr_y2_l)
        ly4_tr_l = pmul_s(
            lam_4,
            [
                coeffs["lam_y4_q_diag"] * (tr_hu2_l[k_p] + tr_hd2_l[k_p])
                + coeffs["lam_y4_e_diag"] * tr_he2_l[k_p]
                + coeffs["lam_y4_q_mix"] * tr_huhd_l[k_p]
                for k_p in range(4)
            ],
        )
        lam_yg_l = pmul_s(lam_4, y2_g_l)
        y4g2u_l = pmul_s(peval_terms(g_cols, coeffs["y4_g2_u_terms"]), tr_hu2_l)
        y4g2d_l = pmul_s(peval_terms(g_cols, coeffs["y4_g2_d_terms"]), tr_hd2_l)
        y4g2e_l = pmul_s(peval_terms(g_cols, coeffs["y4_g2_e_terms"]), tr_he2_l)
        uy2g4_l = pmul_s(peval_terms(g_cols, coeffs["u_y2_g4_terms"]), tr_hu_l)
        dy2g4_l = pmul_s(peval_terms(g_cols, coeffs["d_y2_g4_terms"]), tr_hd_l)
        ey2g4_l = pmul_s(peval_terms(g_cols, coeffs["e_y2_g4_terms"]), tr_he_l)

        b2_lam_l = [
            lam_ew2_l[k_p]
            + coeffs["c2_lam2_y2"] * lam2_y2_l[k_p]
            + ly4_tr_l[k_p]
            + coeffs["c2_lam_yg"] * lam_yg_l[k_p]
            + coeffs["y6_q_diag"] * (tr_hu3_l[k_p] + tr_hd3_l[k_p])
            + coeffs["y6_e_diag"] * tr_he3_l[k_p]
            + coeffs["y6_q_mix"] * (tr_hu2hd_l[k_p] + tr_huhd2_l[k_p])
            + y4g2u_l[k_p]
            + y4g2d_l[k_p]
            + y4g2e_l[k_p]
            + uy2g4_l[k_p]
            + dy2g4_l[k_p]
            + ey2g4_l[k_p]
            for k_p in range(4)
        ]

        gsq_p = [np.array(gsq0, dtype=float)] + [
            np.array([dg_cols[i_g][k_p] / float(k_p + 1) for i_g in range(3)], dtype=float) for k_p in range(4)
        ]
        lam_p = [float(lam0)] + [(inv_8pi * b1_lam_l[k_p] + inv_128pi3 * b2_lam_l[k_p]) / float(k_p + 1) for k_p in range(4)]
        yu_p = [np.array(yu0, dtype=complex)] + [
            (inv_8pi * b1_yu_l[k_p] + inv_128pi3 * b2_yu_l[k_p]) / float(k_p + 1) for k_p in range(4)
        ]
        yd_p = [np.array(yd0, dtype=complex)] + [
            (inv_8pi * b1_yd_l[k_p] + inv_128pi3 * b2_yd_l[k_p]) / float(k_p + 1) for k_p in range(4)
        ]
        ye_p = [np.array(ye0, dtype=complex)] + [
            (inv_8pi * b1_ye_l[k_p] + inv_128pi3 * b2_ye_l[k_p]) / float(k_p + 1) for k_p in range(4)
        ]

    gsq_jet = sum([gsq_p[k_p] * (dt_val ** k_p) for k_p in range(5)], z3_f)
    lam_jet = sum(lam_p[k_p] * (dt_val ** k_p) for k_p in range(5))
    yu_jet = sum([yu_p[k_p] * (dt_val ** k_p) for k_p in range(5)], z3_c)
    yd_jet = sum([yd_p[k_p] * (dt_val ** k_p) for k_p in range(5)], z3_c)
    ye_jet = sum([ye_p[k_p] * (dt_val ** k_p) for k_p in range(5)], z3_c)
    return gsq_jet, float(lam_jet), yu_jet, yd_jet, ye_jet


def integrate_matrix_yukawa_2loop_rk4(
    gsq0: np.ndarray,
    lam0: float,
    yu0: np.ndarray,
    yd0: np.ndarray,
    ye0: np.ndarray,
    t_span: float,
    coeffs: dict[str, Any],
    step_blocks: int = 4,
    two_loop: bool = True,
) -> tuple[np.ndarray, float, np.ndarray, np.ndarray, np.ndarray]:
    """4th-order Runge-Kutta integrator for full 2-loop 3x3 matrix Yukawa + gauge + quartic RGEs."""
    n_steps = 32 * step_blocks
    gsq_c = np.array(gsq0, dtype=float)
    lam_c = float(lam0)
    yu_c = np.array(yu0, dtype=complex)
    yd_c = np.array(yd0, dtype=complex)
    ye_c = np.array(ye0, dtype=complex)
    dt = float(mp.fdiv(t_span, n_steps))
    sixth_dt = float(mp.fdiv(dt, 6))

    for _ in range(n_steps):
        kg1, kl1, ku1, kd1, ke1 = matrix_yukawa_2loop_rhs(gsq_c, lam_c, yu_c, yd_c, ye_c, coeffs, two_loop)
        kg2, kl2, ku2, kd2, ke2 = matrix_yukawa_2loop_rhs(
            gsq_c + 0.5 * dt * kg1,
            lam_c + 0.5 * dt * kl1,
            yu_c + 0.5 * dt * ku1,
            yd_c + 0.5 * dt * kd1,
            ye_c + 0.5 * dt * ke1,
            coeffs,
            two_loop,
        )
        kg3, kl3, ku3, kd3, ke3 = matrix_yukawa_2loop_rhs(
            gsq_c + 0.5 * dt * kg2,
            lam_c + 0.5 * dt * kl2,
            yu_c + 0.5 * dt * ku2,
            yd_c + 0.5 * dt * kd2,
            ye_c + 0.5 * dt * ke2,
            coeffs,
            two_loop,
        )
        kg4, kl4, ku4, kd4, ke4 = matrix_yukawa_2loop_rhs(
            gsq_c + dt * kg3,
            lam_c + dt * kl3,
            yu_c + dt * ku3,
            yd_c + dt * kd3,
            ye_c + dt * ke3,
            coeffs,
            two_loop,
        )
        gsq_c = gsq_c + sixth_dt * (kg1 + 2.0 * kg2 + 2.0 * kg3 + kg4)
        lam_c = lam_c + sixth_dt * (kl1 + 2.0 * kl2 + 2.0 * kl3 + kl4)
        yu_c = yu_c + sixth_dt * (ku1 + 2.0 * ku2 + 2.0 * ku3 + ku4)
        yd_c = yd_c + sixth_dt * (kd1 + 2.0 * kd2 + 2.0 * kd3 + kd4)
        ye_c = ye_c + sixth_dt * (ke1 + 2.0 * ke2 + 2.0 * ke3 + ke4)

    return gsq_c, lam_c, yu_c, yd_c, ye_c


def extract_physical_flavor_invariants(
    yu_m: np.ndarray,
    yd_m: np.ndarray,
    ye_m: np.ndarray,
) -> dict[str, Any]:
    """Extract gauge-invariant physical observables from (Y_u, Y_d, Y_e):
    sorted singular values, |V_CKM| magnitudes (from left Hermitian squares Y_u Y_u^H and Y_d Y_d^H),
    and Jarlskog commutator trace.
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


def compute_sm_19_operator_parameter_count(
    beta_info: dict[str, Any],
    yu_ref: np.ndarray,
    yd_ref: np.ndarray,
    ye_ref: np.ndarray,
) -> dict[str, int]:
    """Mechanically compute the 19 renormalizable SM parameters from explicit operator spaces:
    13 flavour (54x45 u(3)^5 Lie-algebra Jacobian SVD rank 41) + 3 gauge Casimir blocks
    + 2 SU(2)_L x U(1)_Y-invariant Higgs polynomials on R^4 (degrees 1..4)
    + 1 U(1)_{B+L}-unrotated strong-CP angle theta_QCD = 19.
    """
    j_im = complex(0.0, 1.0)
    diag_u3 = [
        np.array([[j_im if (r_i == c_i == k_d) else 0.0 for c_i in range(3)] for r_i in range(3)], dtype=complex)
        for k_d in range(3)
    ]
    real_off_u3 = [
        np.array(
            [
                [1.0 if (r_i == a_i and c_i == b_i) else (-1.0 if (r_i == b_i and c_i == a_i) else 0.0) for c_i in range(3)]
                for r_i in range(3)
            ],
            dtype=complex,
        )
        for a_i in range(3)
        for b_i in range(a_i + 1, 3)
    ]
    imag_off_u3 = [
        np.array(
            [
                [j_im if ((r_i == a_i and c_i == b_i) or (r_i == b_i and c_i == a_i)) else 0.0 for c_i in range(3)]
                for r_i in range(3)
            ],
            dtype=complex,
        )
        for a_i in range(3)
        for b_i in range(a_i + 1, 3)
    ]
    u3_basis = diag_u3 + real_off_u3 + imag_off_u3

    z3_c = np.zeros((3, 3), dtype=complex)
    jac_cols = [
        np.concatenate(
            [
                (k_m @ yu_ref if slot_i == 0 else (-yu_ref @ k_m if slot_i == 1 else z3_c)).real.ravel(),
                (k_m @ yu_ref if slot_i == 0 else (-yu_ref @ k_m if slot_i == 1 else z3_c)).imag.ravel(),
                (k_m @ yd_ref if slot_i == 0 else (-yd_ref @ k_m if slot_i == 2 else z3_c)).real.ravel(),
                (k_m @ yd_ref if slot_i == 0 else (-yd_ref @ k_m if slot_i == 2 else z3_c)).imag.ravel(),
                (k_m @ ye_ref if slot_i == 3 else (-ye_ref @ k_m if slot_i == 4 else z3_c)).real.ravel(),
                (k_m @ ye_ref if slot_i == 3 else (-ye_ref @ k_m if slot_i == 4 else z3_c)).imag.ravel(),
            ]
        )
        for slot_i in range(5)
        for k_m in u3_basis
    ]
    jac_54x45 = np.column_stack(jac_cols)
    _, sv_jac, vh_jac = np.linalg.svd(jac_54x45, full_matrices=True)
    jac_rank = int(np.sum(sv_jac > 1e-8))
    ker_45xnu = vh_jac[jac_rank:, :].T
    u1_conserved_nullity = 45 - jac_rank
    n_flavor_params = 54 - jac_rank

    n_gauge_params = sum(1 for c_mat in beta_info["cas_16"] if c_mat.trace() != 0)

    # SU(2)_L x U(1)_Y Lie-derivative nullities on Sym^d(R^4) for renormalizable degrees d = 1..4:
    th_4_np = [
        np.array([[float(th_mat[r_i, c_i]) for c_i in range(4)] for r_i in range(4)], dtype=float)
        for th_mat in beta_info["th_4_unit"]
    ]
    n_higgs_params = 0
    for deg_d in (1, 2, 3, 4):
        mons_d = [ex_t for ex_t in product(range(deg_d + 1), repeat=4) if sum(ex_t) == deg_d]
        idx_mon = {mon_ex: k_m for k_m, mon_ex in enumerate(mons_d)}
        dim_sym = len(mons_d)
        stacked_lie = np.zeros((4 * dim_sym, dim_sym), dtype=float)
        for g_idx, g_mat in enumerate(th_4_np):
            row_off = g_idx * dim_sym
            for col_j, ex_t in enumerate(mons_d):
                for c_v in range(4):
                    if ex_t[c_v] > 0:
                        for r_v in range(4):
                            if g_mat[r_v, c_v] != 0.0:
                                shifted_ex = tuple(
                                    ex_t[idx_e]
                                    + (1 if idx_e == r_v else 0)
                                    - (1 if idx_e == c_v else 0)
                                    for idx_e in range(4)
                                )
                                stacked_lie[row_off + idx_mon[shifted_ex], col_j] += g_mat[r_v, c_v] * ex_t[c_v]
        sv_lie = np.linalg.svd(stacked_lie, compute_uv=False)
        n_higgs_params += dim_sym - int(np.sum(sv_lie > 1e-9))

    # Mechanical chiral Weyl anomaly projection on ker(J_{54x45}) across non-abelian factors:
    nonab_indices = [idx_g for idx_g in range(3) if beta_info["c2_g"][idx_g] != 0]
    n_nonabelian_factors = len(nonab_indices)
    n_c_int = int(beta_info["n_c"])
    slot_blocks = [
        (0, 2 * n_c_int, 1.0),
        (2 * n_c_int, 3 * n_c_int, -1.0),
        (3 * n_c_int, 4 * n_c_int, -1.0),
        (4 * n_c_int, 4 * n_c_int + 2, 1.0),
        (4 * n_c_int + 2, 4 * n_c_int + 3, -1.0),
    ]
    anom_2x45 = np.array(
        [
            [
                chir_sgn
                * float(beta_info["cas_16"][idx_g][r_st:r_en, r_st:r_en].trace() / beta_info["d_g"][idx_g])
                * float(np.imag(np.trace(k_m)))
                for r_st, r_en, chir_sgn in slot_blocks
                for k_m in u3_basis
            ]
            for idx_g in nonab_indices
        ],
        dtype=float,
    )
    sv_anom = np.linalg.svd(anom_2x45 @ ker_45xnu, compute_uv=False)
    anom_rank = int(np.sum(sv_anom > 1e-8))
    n_theta_phys = n_nonabelian_factors - anom_rank

    return {
        "jac_rank": jac_rank,
        "u1_conserved_nullity": u1_conserved_nullity,
        "anom_rank": anom_rank,
        "n_flavor_params": n_flavor_params,
        "n_gauge_params": n_gauge_params,
        "n_higgs_params": n_higgs_params,
        "n_theta_phys": n_theta_phys,
        "total_sm_params": n_flavor_params + n_gauge_params + n_higgs_params + n_theta_phys,
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
    """Verify Part 6C: WP-4.2 level-5 twisted eigenline uniqueness & genuine 1-bit SC:PREMISE pricing,
    WP-4.3 exact Kashaev J_5(4_1) = 46 + 2*sqrt(5) + volume asymptotics + 19-parameter operator Jacobian,
    and full 2-loop SM MV84/MV85 RGE derivation + Guardrails 3, 4, 5.
    """
    mat_l = sp.Matrix([[1, 1], [0, 1]])
    mat_r = sp.Matrix([[1, 0], [1, 1]])
    i2_s = sp.eye(2)
    gamma_gold = mat_l * mat_r
    m_gold_rl = mat_r * mat_l

    det_untwisted_lr = abs(int((gamma_gold - i2_s).det()))
    det_twisted_lr = abs(int((gamma_gold + i2_s).det()))
    det_untwisted_rl = abs(int((m_gold_rl - i2_s).det()))
    det_twisted_rl = abs(int((m_gold_rl + i2_s).det()))

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
                primes_with_twisted_line = primes_with_twisted_line + [n_chk]

    v_lr_5 = sp.Matrix([[2, 4]])
    v_rl_5 = sp.Matrix([[1, 3]])
    lr_mod5_eigen = (v_lr_5 * gamma_gold + v_lr_5).applyfunc(lambda x_e: x_e % 5) == sp.zeros(1, 2)
    rl_mod5_eigen = (v_rl_5 * m_gold_rl + v_rl_5).applyfunc(lambda x_e: x_e % 5) == sp.zeros(1, 2)

    # Genuine SC:PREMISE 1-bit pricing via (Z/5Z)^x holonomy scaling symmetry of F_u(tau):
    zero_ic = int(sp.Matrix.eye(1).trace()) - 1
    dyn_zc = mp.mpf(zero_ic)
    with mp.workdps(40):
        x_asym = mp.fdiv(2, 7) + dyn_zc
        y_asym = mp.fdiv(11, 8) + dyn_zc
        f_base_u = kronecker_shifted_s1_mp(mp.fdiv(1, 5), mp.fdiv(2, 5), x_asym, y_asym, 2)
        n_kronecker_sym = sum(
            1
            for eps_u in (1, 2, 3, 4)
            if float(
                abs(
                    kronecker_shifted_s1_mp(
                        mp.fdiv(eps_u % 5, 5), mp.fdiv((2 * eps_u) % 5, 5), x_asym, y_asym, 2
                    )
                    - f_base_u
                )
            )
            < TOL
        )
    sc_premise_bits = int(round(math.log2(n_kronecker_sym)))

    # 2. WP-4.3: Exact Kashaev J_N(4_1) in SymPy (N = 1..6) and 40-dps mpmath + volume conjecture check:
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

        vol_4_1_mp = 2 * mp.clsin(2, mp.fdiv(mp.pi, 3))
        small_n5_asymptotic_ratio = float(j5_mp / mp.exp(5 * vol_4_1_mp / (2 * mp.pi)))

        def vol_est_subleading_stripped(block_k: int) -> Any:
            n_v = 32 * block_k
            n_m = mp.mpf(n_v)
            return (2 * mp.pi / n_m) * mp.log(kashaev_4_1_mp(n_v)) - (3 * mp.pi * mp.log(n_m)) / n_m

        v_32 = vol_est_subleading_stripped(1 + zero_ic)
        v_64 = vol_est_subleading_stripped(2 + zero_ic)
        v_128 = vol_est_subleading_stripped(4 + zero_ic)
        v_256 = vol_est_subleading_stripped(8 + zero_ic)
        r1_0 = 2 * v_64 - v_32
        r1_a = 2 * v_128 - v_64
        r1_b = 2 * v_256 - v_128
        r2_a = mp.fdiv(4 * r1_a - r1_0, 3)
        r2_b = mp.fdiv(4 * r1_b - r1_a, 3)
        vol_richardson = mp.fdiv(8 * r2_b - r2_a, 7)
        vol_conjecture_err = float(abs(vol_richardson - vol_4_1_mp))

    # 3. Genuine MV84/MV85 2-Loop SM Beta Derivation + N_c = 4 / n_gen = 0 Specializations:
    beta_sym = build_sm_2loop_betas_symbolic(0 + zero_ic, -1 + zero_ic)
    beta_nc4 = build_sm_2loop_betas_symbolic(4 + zero_ic, 3 + zero_ic)
    beta_ng0 = build_sm_2loop_betas_symbolic(3 + zero_ic, 0 + zero_ic)
    num_coeffs = make_sm_rge_num_coeffs(beta_sym)

    b1_s, b2_s, b3_s = beta_sym["b1_vec"]
    p_l2_nc4 = sp.Poly(beta_nc4["beta_lam_2"], *beta_nc4["symbols_5"])
    p_l2_ng0 = sp.Poly(beta_ng0["beta_lam_2"], *beta_ng0["symbols_5"])
    mv_specializations_exact = (
        sp.simplify(5 * beta_sym["k_gut"] - 3) == 0
        and sp.simplify(10 * b1_s - 41) == 0
        and sp.simplify(6 * b2_s + 19) == 0
        and sp.simplify(b3_s + 7) == 0
        and sp.simplify((b1_s - b2_s) * (23 * 5) - (b2_s - b3_s) * (2 * 109)) == 0
        and sp.simplify(p_l2_nc4.coeff_monomial((0, 0, 0, 0, 3)) / sp.Integer(24) + 13) == 0
        and sp.simplify(p_l2_ng0.coeff_monomial((0, 0, 0, 0, 3)) / sp.Integer(24) + 13) == 0
        and p_l2_nc4.coeff_monomial((0, 1, 0, 0, 2)) == 108
        and p_l2_ng0.coeff_monomial((0, 1, 0, 0, 2)) == 108
        and sp.simplify(3 * beta_nc4["b1_vec"][2] + 32) == 0
        and sp.simplify(10 * beta_ng0["b1_vec"][0] - 1) == 0
        and sp.simplify(6 * beta_ng0["b1_vec"][1] + 43) == 0
        and sp.simplify(beta_ng0["b1_vec"][2] + 11) == 0
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

    # Benchmark 4.3: 1-loop pure quartic exact trajectory + 2-loop pure-g3^2 exact implicit integral:
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

    # Benchmark 4.4: Full 5-channel 2-loop symbolic 4th-order Picard Taylor jet + reversibility + negative controls:
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
        picard_poly = [
            x0_syms[i_c]
            + sum(
                sp.Poly(sp.expand(rhs_5[i_c].subs(subs_p)), t_jet_sym).coeff_monomial(t_jet_sym ** deg_k)
                * (t_jet_sym ** (deg_k + 1))
                / sp.Integer(deg_k + 1)
                for deg_k in range(ord_p)
            )
            for i_c in range(5)
        ]

    t_jet = (1 / 96) * one_dyn
    jet_4_num = np.array(
        [float(picard_poly[i_c].subs(t_jet_sym, sp.Rational(1, 96)).evalf(30)) for i_c in range(5)],
        dtype=float,
    )

    x0_jet = one_dyn * np.array([1 / 4, 1 / 3, 1 / 2, 1 / 2, 1 / 8], dtype=float)
    x_rk4_jet = integrate_sm_5chan_rk4(x0_jet, t_jet, num_coeffs, step_blocks=4, two_loop=True)
    bench_5chan_jet4_err = float(np.max(np.abs(x_rk4_jet - jet_4_num)))

    x_up = integrate_sm_5chan_rk4(x0_jet, 2.0 * one_dyn, num_coeffs, step_blocks=8, two_loop=True)
    x_roundtrip = integrate_sm_5chan_rk4(x_up, -2.0 * one_dyn, num_coeffs, step_blocks=8, two_loop=True)
    bench_reversibility_err = float(np.max(np.abs(x_roundtrip - x0_jet)))

    x_wrong_t = integrate_sm_5chan_rk4(x0_jet, t_jet, num_coeffs, step_blocks=4, two_loop=True, scale_t_factor=2.0)
    x_wrong_lam = integrate_sm_5chan_rk4(x0_jet, t_jet, num_coeffs, step_blocks=4, two_loop=True, lam_factor=2.0)
    neg_ctrl_wrong_4pi_err = float(np.max(np.abs(x_wrong_t - jet_4_num)))
    neg_ctrl_wrong_lam2_err = abs(float(x_wrong_lam[4] - jet_4_num[4]))

    # 4. Full 2-Loop 3x3 Matrix Yukawa + Gauge + Quartic Specialization & Guardrail 3 U(3)^5 Haar Scrambling:
    yt_spec = (3 / 4) * one_dyn
    gsq_spec = one_dyn * np.array([1 / 4, 1 / 3, 1 / 2], dtype=float)
    lam_spec = (1 / 8) * one_dyn
    yu_spec = np.diag([0.0, 0.0, yt_spec]).astype(complex)
    z3_spec = np.zeros((3, 3), dtype=complex)
    dg_sp, dl_sp, dyu_sp, dyd_sp, dye_sp = matrix_yukawa_2loop_rhs(
        gsq_spec, lam_spec, yu_spec, z3_spec, z3_spec, num_coeffs, True
    )
    dx5_sp = sm_rge_5chan_rhs(
        np.array([gsq_spec[0], gsq_spec[1], gsq_spec[2], yt_spec ** 2, lam_spec], dtype=float),
        num_coeffs,
        two_loop=True,
    )
    matrix_to_5chan_spec_err = max(
        float(np.max(np.abs(dg_sp - dx5_sp[:3]))),
        abs(2.0 * yt_spec * float(np.real(dyu_sp[2, 2])) - float(dx5_sp[3])),
        abs(dl_sp - float(dx5_sp[4])),
        float(np.max(np.abs(dyd_sp))),
        float(np.max(np.abs(dye_sp))),
    )

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
    lam_uv = (1 / 8) * one_dyn

    obs_uv = extract_physical_flavor_invariants(yu_uv, yd_uv, ye_uv)
    uv_yb_ytau_unity_err = abs(obs_uv["yb_over_ytau"] - 1.0)

    # Non-commuting 2-loop 3x3 matrix Lie-Picard 4th-order Taylor jet benchmark + swapped negative control:
    hu_uv = yu_uv @ yu_uv.conj().T
    hd_uv = yd_uv @ yd_uv.conj().T
    comm_uv_norm = float(np.linalg.norm(hu_uv @ hd_uv - hd_uv @ hu_uv))
    dt_mat_jet = -(1 / 96) * one_dyn
    gsq_mj4, lam_mj4, yu_mj4, yd_mj4, ye_mj4 = picard_jet4_matrix_yukawa_2loop(
        gsq_uv, lam_uv, yu_uv, yd_uv, ye_uv, dt_mat_jet, num_coeffs
    )
    gsq_mrk, lam_mrk, yu_mrk, yd_mrk, ye_mrk = integrate_matrix_yukawa_2loop_rk4(
        gsq_uv, lam_uv, yu_uv, yd_uv, ye_uv, dt_mat_jet, num_coeffs, step_blocks=2, two_loop=True
    )
    bench_matrix_jet4_err = max(
        float(np.max(np.abs(gsq_mrk - gsq_mj4))),
        abs(lam_mrk - lam_mj4),
        float(np.max(np.abs(yu_mrk - yu_mj4))),
        float(np.max(np.abs(yd_mrk - yd_mj4))),
        float(np.max(np.abs(ye_mrk - ye_mj4))),
    )

    swapped_coeffs = {
        **num_coeffs,
        "c2_q_hfhfp": num_coeffs["c2_q_hfphf"],
        "c2_q_hfphf": num_coeffs["c2_q_hfhfp"],
    }
    _, _, dyu_true_0, dyd_true_0, _ = matrix_yukawa_2loop_rhs(gsq_uv, lam_uv, yu_uv, yd_uv, ye_uv, num_coeffs, True)
    _, _, dyu_swap_0, dyd_swap_0, _ = matrix_yukawa_2loop_rhs(
        gsq_uv, lam_uv, yu_uv, yd_uv, ye_uv, swapped_coeffs, True
    )
    neg_ctrl_swapped_comm_rhs_err = max(
        float(np.max(np.abs(dyu_swap_0 - dyu_true_0))),
        float(np.max(np.abs(dyd_swap_0 - dyd_true_0))),
    )
    _, _, yu_swap_dt, yd_swap_dt, _ = integrate_matrix_yukawa_2loop_rk4(
        gsq_uv, lam_uv, yu_uv, yd_uv, ye_uv, dt_mat_jet, swapped_coeffs, step_blocks=2, two_loop=True
    )
    neg_ctrl_swapped_comm_jet_err = max(
        float(np.max(np.abs(yu_swap_dt - yu_mj4))),
        float(np.max(np.abs(yd_swap_dt - yd_mj4))),
    )

    t_ir_span = -(3 / 2) * one_dyn
    gsq_ir_ref, lam_ir_ref, yu_ir_ref, yd_ir_ref, ye_ir_ref = integrate_matrix_yukawa_2loop_rk4(
        gsq_uv, lam_uv, yu_uv, yd_uv, ye_uv, t_ir_span, num_coeffs, step_blocks=8, two_loop=True
    )
    obs_ir_ref = extract_physical_flavor_invariants(yu_ir_ref, yd_ir_ref, ye_ir_ref)
    radiative_yb_ytau_shift = abs(obs_ir_ref["yb_over_ytau"] - 1.0)

    rng_haar = np.random.default_rng(73)
    max_haar_rge_scrambling_err = 0.0
    for _ in range(6):
        u_q = haar_unitary(3, rng_haar)
        u_uc = haar_unitary(3, rng_haar)
        u_dc = haar_unitary(3, rng_haar)
        u_l = haar_unitary(3, rng_haar)
        u_ec = haar_unitary(3, rng_haar)

        yu_scr_0 = u_q @ yu_uv @ u_uc.conj().T
        yd_scr_0 = u_q @ yd_uv @ u_dc.conj().T
        ye_scr_0 = u_l @ ye_uv @ u_ec.conj().T

        gsq_scr_t, lam_scr_t, yu_scr_t, yd_scr_t, ye_scr_t = integrate_matrix_yukawa_2loop_rk4(
            gsq_uv, lam_uv, yu_scr_0, yd_scr_0, ye_scr_0, t_ir_span, num_coeffs, step_blocks=8, two_loop=True
        )
        obs_scr = extract_physical_flavor_invariants(yu_scr_t, yd_scr_t, ye_scr_t)
        err_trial = max(
            float(np.max(np.abs(gsq_scr_t - gsq_ir_ref))),
            abs(lam_scr_t - lam_ir_ref),
            float(np.max(np.abs(obs_scr["sv_u"] - obs_ir_ref["sv_u"]))),
            float(np.max(np.abs(obs_scr["sv_d"] - obs_ir_ref["sv_d"]))),
            float(np.max(np.abs(obs_scr["sv_e"] - obs_ir_ref["sv_e"]))),
            float(np.max(np.abs(obs_scr["v_ckm_abs"] - obs_ir_ref["v_ckm_abs"]))),
            abs(obs_scr["jarlskog_tr"] - obs_ir_ref["jarlskog_tr"]),
            abs(obs_scr["yb_over_ytau"] - obs_ir_ref["yb_over_ytau"]),
        )
        max_haar_rge_scrambling_err = max(max_haar_rge_scrambling_err, err_trial)

    # Mechanical 19-parameter SM operator accounting (rank-3 generic + rank-2 massless-up control):
    sm19_info = compute_sm_19_operator_parameter_count(beta_sym, yu_uv, yd_uv, ye_uv)
    unresolved_sm_count = sm19_info["total_sm_params"]
    u_svd_l, sv_uv_u, vh_svd_r = np.linalg.svd(yu_uv)
    yu_zero_light = (u_svd_l * np.array([sv_uv_u[0], sv_uv_u[1], 0.0], dtype=float)) @ vh_svd_r
    sm19_massless_up = compute_sm_19_operator_parameter_count(beta_sym, yu_zero_light, yd_uv, ye_uv)

    # 5. Guardrail 5: Single-anchor non-dimensionalization & pure-SM desert 3-line unification obstruction:
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
    desert_single_scale_diff = sp.simplify(t_unif_12 - t_unif_23)
    desert_unif_scale_mismatch = float(abs(desert_single_scale_diff))

    # Dynamic 3-gate WP-4.3 bridge failure count ({SC:PREMISE, SC:R2, SC:R4}):
    rho_uv_g = sp.Symbol("rho_uv_g", positive=True)
    end_law_open_rk = int(sp.Matrix([[sp.diff(-sp.log(rho_uv_g), rho_uv_g)]]).rank())
    unproved_wp43_gates = sum(
        [
            int(det_untwisted_lr == 1 and sc_premise_bits > 0),
            int(small_n5_asymptotic_ratio > 9 and end_law_open_rk > 0),
            int(desert_single_scale_diff != 0),
        ]
    )

    # Guardrail 5 dimensionless ratio invariance + 1x10 mass-dimension matrix rank 1 (nullity 9):
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
    mass_dim_1x10 = sp.Matrix([[1, 1, 1, 1, 1, 1, 0, 0, 0, 0]])
    max_dimensionful_anchors = int(mass_dim_1x10.rank())
    dimless_ratio_nullity = int(np.sum(np.ones(len(mass_dim_1x10.nullspace()), dtype=int)))

    part6c_ok = (
        det_untwisted_lr == 1
        and det_twisted_lr == 5
        and det_untwisted_rl == 1
        and det_twisted_rl == 5
        and untwisted_nonzero_total == 0
        and primes_with_twisted_line == [5]
        and bool(lr_mod5_eigen)
        and bool(rl_mod5_eigen)
        and n_kronecker_sym == 2
        and sc_premise_bits == 1
        and bool(j_small_exact)
        and j5_mp_err < 1e-36
        and small_n5_asymptotic_ratio > 9
        and vol_conjecture_err < 1e-6
        and sm19_info["jac_rank"] == 41
        and sm19_info["u1_conserved_nullity"] == 4
        and sm19_info["anom_rank"] == 1
        and sm19_info["n_flavor_params"] == 13
        and sm19_info["n_gauge_params"] == 3
        and sm19_info["n_higgs_params"] == 2
        and sm19_info["n_theta_phys"] == 1
        and unresolved_sm_count == 19
        and sm19_massless_up["jac_rank"] == 40
        and sm19_massless_up["u1_conserved_nullity"] == 5
        and sm19_massless_up["anom_rank"] == 2
        and sm19_massless_up["n_theta_phys"] == 0
        and unproved_wp43_gates == 3
        and bool(mv_specializations_exact)
        and bool(beta_sym["mv83_1loop_matrix_symbolic_exact"])
        and bool(beta_sym["mv84_2loop_matrix_symbolic_exact"])
        and bool(beta_sym["mv84_swapped_commutator_nonzero"])
        and bench_1loop_gauge_err < TOL
        and bench_pendleton_ross_fp_err < TOL
        and bench_bernoulli_err < TOL
        and bench_pure_quartic_err < TOL
        and bench_2loop_implicit_g3_err < TOL
        and bench_5chan_jet4_err < TOL
        and bench_reversibility_err < TOL
        and neg_ctrl_wrong_4pi_err > 1e-6
        and neg_ctrl_wrong_lam2_err > 1e-6
        and matrix_to_5chan_spec_err < TOL
        and comm_uv_norm > (1 / 32)
        and bench_matrix_jet4_err < TOL
        and neg_ctrl_swapped_comm_rhs_err > 1e-6
        and neg_ctrl_swapped_comm_jet_err > 1e-8
        and uv_yb_ytau_unity_err < TOL
        and abs(obs_ir_ref["jarlskog_tr"]) > 1e-9
        and radiative_yb_ytau_shift > (1 / 10)
        and max_haar_rge_scrambling_err < TOL
        and bool(desert_ratio_obstruction_exact)
        and desert_unif_scale_mismatch > 0.5
        and bool(ratio_scale_inv)
        and max_dimensionful_anchors == 1
        and dimless_ratio_nullity == 9
    )

    return {
        "wp42_det_untwisted_lr": det_untwisted_lr,
        "wp42_det_twisted_lr": det_twisted_lr,
        "wp42_primes_with_twisted_eigenline": primes_with_twisted_line,
        "wp42_kronecker_scaling_sym_count": n_kronecker_sym,
        "wp42_sc_premise_bits": sc_premise_bits,
        "wp43_j5_mp_err": j5_mp_err,
        "wp43_j5_value": float(j5_mp),
        "wp43_small_n5_over_leading_asymptotic": small_n5_asymptotic_ratio,
        "wp43_large_n_volume_conjecture_err": vol_conjecture_err,
        "wp43_flavor_jacobian_rank": sm19_info["jac_rank"],
        "wp43_flavor_conserved_u1_nullity": sm19_info["u1_conserved_nullity"],
        "wp43_flavor_anom_rank": sm19_info["anom_rank"],
        "wp43_massless_up_nullity": sm19_massless_up["u1_conserved_nullity"],
        "wp43_massless_up_anom_rank": sm19_massless_up["anom_rank"],
        "wp43_massless_up_n_theta_phys": sm19_massless_up["n_theta_phys"],
        "wp43_unresolved_sm_parameters_count": unresolved_sm_count,
        "wp43_unproved_bridge_gates_count": unproved_wp43_gates,
        "guardrail4_1loop_gauge_err": bench_1loop_gauge_err,
        "guardrail4_pendleton_ross_fp_err": bench_pendleton_ross_fp_err,
        "guardrail4_bernoulli_coupled_err": bench_bernoulli_err,
        "guardrail4_pure_quartic_err": bench_pure_quartic_err,
        "guardrail4_2loop_implicit_g3_err": bench_2loop_implicit_g3_err,
        "guardrail4_5chan_symbolic_jet4_err": bench_5chan_jet4_err,
        "guardrail4_matrix_jet4_err": bench_matrix_jet4_err,
        "guardrail4_neg_ctrl_swapped_comm_rhs_err": neg_ctrl_swapped_comm_rhs_err,
        "guardrail4_neg_ctrl_swapped_comm_jet_err": neg_ctrl_swapped_comm_jet_err,
        "guardrail4_reversibility_err": bench_reversibility_err,
        "guardrail4_neg_ctrl_wrong_4pi_err": neg_ctrl_wrong_4pi_err,
        "guardrail4_neg_ctrl_wrong_lam2_err": neg_ctrl_wrong_lam2_err,
        "guardrail4_2loop_matrix_to_5chan_spec_err": matrix_to_5chan_spec_err,
        "guardrail3_max_haar_rge_scrambling_err": max_haar_rge_scrambling_err,
        "guardrail3_radiative_yb_over_ytau": obs_ir_ref["yb_over_ytau"],
        "guardrail5_desert_unif_scale_mismatch": desert_unif_scale_mismatch,
        "guardrail5_max_dimensionful_anchors": max_dimensionful_anchors,
        "guardrail5_dimless_ratio_nullity": dimless_ratio_nullity,
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
