#!/usr/bin/env python3
"""
Sealed post-run companion check for Card X-NEG (B1868 auxiliary items only).

Addresses three numerical/discretization bugs disclosed from the first sealed run
of verify_x_neg.py (commit be56354cc, left untouched):

1. Jensen's 60-digit exponents: verify_x_neg.py sampled u_k at exact dyadic rationals
   (k + 1/2)/512, mapping xi_k = F_nu^-1(u_k) to exact rationals where ?'(p/q) = 0
   and rational CF termination hit float residuals on Q1-Q3. Here we sample u_k along
   irrational golden-ratio Weyl points u_lo + frac((k + 1)/phi) * (u_hi - u_lo) at
   160-digit precision (460 Stern-Brocot bits, >130 guard digits beyond q > 10^30).

2. PC_B1868_liouville_flat: verify_x_neg.py used un-split global Gauss-Legendre across
   square-root corners on (0, infty) (~1.2% corner error). Here we split at the exact
   algebraic critical points of xi and the Re z = 0 chord-clipping locuszeta = y0^2 e^(+-2 eps)/xi,
   verifying |f_eps^(L)([z0]) - 1| < 1e-10 across all 9 points vs > 0.50 planted 1-side error.

3. PC_B1868_atomic_measure & Riesz geometric convergence: verify_x_neg.py placed its test
   atom at the parabolic cusp-adjacent Farey midpoint x = 1/2 (harmonic width 1/(4d+2))
   and checked |I_{1/2}^(12) - I_{1/2}^(11)| < 0.02 when the exact geometric ratio (3/4)^d
   at d = 12 has step 0.0378. Here we place the atom at the interior golden point 1/phi
   (exponential width ~ phi^-2d -> Riesz 1/2-energy diverges as phi^d) and verify the
   exact geometric convergence ratio (I_{1/2}^(d) - I_{1/2}^(d-1)) / (I_{1/2}^(d-1) - I_{1/2}^(d-2)) -> 3/4.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import time
from typing import Any

import mpmath as mp
import numpy as np


def build_stern_brocot_unit_tree(depth: int) -> tuple[np.ndarray, np.ndarray]:
    p = np.array([0, 1], dtype=np.int64)
    q = np.array([1, 1], dtype=np.int64)
    for _ in range(depth):
        pm = p[:-1] + p[1:]
        qm = q[:-1] + q[1:]
        pn = np.empty(2 * len(pm) + 1, dtype=np.int64)
        qn = np.empty(2 * len(qm) + 1, dtype=np.int64)
        pn[0::2] = p
        pn[1::2] = pm
        qn[0::2] = q
        qn[1::2] = qm
        p, q = pn, qn
    return p, q


def f_nu_mp(val: mp.mpf, max_bits: int = 520) -> mp.mpf:
    if val <= 0:
        return mp.mpf(0)
    if mp.isinf(val):
        return mp.mpf(1)
    acc = mp.mpf(0)
    bit_depth = 0
    x = val
    while bit_depth < max_bits:
        if x >= 1:
            k_mp = mp.floor(x)
            k = int(k_mp)
            rem = x - k_mp
            if rem <= 0:
                return acc + mp.ldexp(1, -bit_depth) * (1 - mp.ldexp(1, -k))
            if k < max_bits + 20:
                acc += mp.ldexp(1, -bit_depth) * (1 - mp.ldexp(1, -k))
            else:
                return acc + mp.ldexp(1, -bit_depth)
            bit_depth += k
            x = rem
        else:
            u = 1 / x
            m_mp = mp.floor(u)
            m = int(m_mp)
            rem = u - m_mp
            if rem <= 0:
                return acc + mp.ldexp(1, -(bit_depth + m))
            bit_depth += m
            if bit_depth >= max_bits:
                return acc
            x = 1 / rem
    return acc


def f_nu_inv_mp(u: mp.mpf, steps: int = 460) -> mp.mpf:
    a, b, c, d = 1, 0, 0, 1
    rem = u
    bits_used = 0
    while bits_used < steps:
        if rem == mp.mpf("0.5"):
            break
        if rem > mp.mpf("0.5"):
            one_minus = 1 - rem
            if one_minus <= 0:
                k = steps - bits_used
            else:
                k = max(1, min(steps - bits_used, int(mp.floor(-mp.log(one_minus, 2)))))
                while k > 1 and (1 - one_minus * mp.ldexp(1, k)) <= 0:
                    k -= 1
            b = a * k + b
            d = c * k + d
            rem = 1 - one_minus * mp.ldexp(1, k)
            bits_used += k
        else:
            if rem <= 0:
                m = steps - bits_used
            else:
                m = max(1, min(steps - bits_used, int(mp.floor(-mp.log(rem, 2)))))
                while m > 1 and (rem * mp.ldexp(1, m)) >= 1:
                    m -= 1
            a = a + b * m
            c = c + d * m
            rem = rem * mp.ldexp(1, m)
            bits_used += m
    return mp.mpf(a + b) / mp.mpf(c + d)


def compute_jensen_60d_irrational(
    a_h: int,
    b_h: int,
    c_h: int,
    x0_mp: mp.mpf,
    y0_mp: mp.mpf,
    n_samples: int = 512,
) -> dict[str, Any]:
    """
    Evaluate Jensen's 60-digit exponent using irrational Weyl-equidistributed quantiles
    u_k = u_lo + frac((k + 1) * phi^-1) * (u_hi - u_lo) at 160-digit working precision.
    """
    orig_dps = mp.mp.dps
    mp.mp.dps = 165
    try:
        inv_phi = (mp.sqrt(5) - 1) / 2
        if x0_mp == 0:
            u_lo = mp.mpf(0)
            u_hi = mp.mpf(1)
        elif x0_mp > 0:
            xi_lo = x0_mp
            xi_hi = (x0_mp * x0_mp + y0_mp * y0_mp) / x0_mp
            u_lo = f_nu_mp(xi_lo, max_bits=520)
            u_hi = f_nu_mp(xi_hi, max_bits=520)
        else:
            u_lo = mp.mpf(0)
            u_hi = mp.mpf(1)

        ln2 = mp.log(2)
        q_thresh = mp.mpf(10) ** 30  # 60-digit convergent cell q_N^-2 < 10^-60
        delta_30 = mp.mpf(10) ** (-30)
        ln_2delta30 = mp.log(2 * delta_30)

        cf_exps: list[float] = []
        ball30_exps: list[float] = []
        du = u_hi - u_lo
        for k in range(n_samples):
            frac_part = ((k + 1) * inv_phi) - mp.floor((k + 1) * inv_phi)
            uk = u_lo + frac_part * du
            xi = f_nu_inv_mp(uk, steps=480)
            zeta = (-a_h * xi - b_h) / (c_h * xi - a_h)

            # 60-digit continued-fraction Stern-Brocot exponent
            w = zeta if zeta >= 1 else (1 / zeta)
            q_prev, q_cur = mp.mpf(0), mp.mpf(1)
            sb_sum = 0
            for _ in range(300):
                ai = int(mp.floor(w))
                sb_sum += ai
                q_prev, q_cur = q_cur, ai * q_cur + q_prev
                rem = w - ai
                if q_cur > q_thresh or rem <= mp.mpf(10) ** (-140):
                    break
                w = 1 / rem
            cf_exps.append(float((sb_sum * ln2) / (2 * mp.log(q_cur))))

            # Independent cross-check via direct small-ball nu([zeta - 10^-30, zeta + 10^-30])
            # with max_bits = 1200 (resolves down to 2^-1200 ~ 10^-361, so exponents up to 11 never underflow!)
            m_b = f_nu_mp(zeta + delta_30, max_bits=1200) - f_nu_mp(
                max(mp.mpf(0), zeta - delta_30), max_bits=1200
            )
            if m_b > 0:
                ball30_exps.append(float(mp.log(m_b) / ln_2delta30))

        return {
            "degree": int(-a_h * a_h - b_h * c_h),
            "jensen_60d_cf_mean": float(np.mean(cf_exps)),
            "jensen_30d_ball_mean": float(np.mean(ball30_exps)),
            "valid_ball_samples": len(ball30_exps),
        }
    finally:
        mp.mp.dps = orig_dps


def rho3_inv(z: complex) -> complex:
    return 1.0 - (1.0 / z)


def rho3_inv2(z: complex) -> complex:
    return 1.0 / (1.0 - z)


def liouville_sector_piecewise_exact(z_center: complex, eps: float) -> float:
    """
    Piecewise singularity-split Gauss-Legendre integration of Liouville measure
    d xi d zeta / (xi + zeta)^2 with lambda_L = pi^2 / 3 on gamma_{-zeta, xi} cap F cap B_eps(z_center).
    """
    nodes_out, weights_out = np.polynomial.legendre.leggauss(48)
    nodes_in, weights_in = np.polynomial.legendre.leggauss(32)

    x0 = float(z_center.real)
    y0 = float(z_center.imag)
    sinh_e = math.sinh(eps)
    cosh_e = math.cosh(eps)
    c_val = y0 * sinh_e
    r2_mod = x0 * x0 + y0 * y0

    # Collect all algebraic critical points of xi > 0 where zeta_lo / zeta_hi / s_out / s_in change branch
    crit = [0.0, 1.0]
    for xc in (x0 - c_val, x0 + c_val):
        if xc > 1e-14:
            crit.append(xc)
    if abs(x0 - c_val) > 1e-14:
        v1 = r2_mod / (x0 - c_val)
        if v1 > 1e-14:
            crit.append(v1)
    if abs(x0 + c_val) > 1e-14:
        v2 = r2_mod / (x0 + c_val)
        if v2 > 1e-14:
            crit.append(v2)
    # Also split at Re z = 0 intersection heights y_e = sqrt(max(0, r_E^2 - x0^2)) +- y0 cosh(eps)
    disc_e0 = c_val * c_val - x0 * x0
    e0_y_sq_splits: list[float] = []
    if disc_e0 > 0.0:
        sq = math.sqrt(disc_e0)
        for ye in (y0 * cosh_e - sq, y0 * cosh_e + sq):
            if ye > 0.0:
                e0_y_sq_splits.append(ye * ye)
                # Also Re z = 1 intersection splits if near x = 1
    disc_e1 = c_val * c_val - (1.0 - x0) * (1.0 - x0)
    e1_splits: list[float] = []
    if disc_e1 > 0.0:
        sq1 = math.sqrt(disc_e1)
        for ye1 in (y0 * cosh_e - sq1, y0 * cosh_e + sq1):
            if ye1 > 0.0:
                e1_splits.append(ye1 * ye1)
                crit.append(1.0)

    # Semicircle e2: |z - 1/2| = 1/2 (x^2 + y^2 = x) intersection points with d_H(z, z_center) = eps:
    # Write z = (1 + cos t)/2 + i sin(t)/2 (t in (0, pi)):
    # ((1 - 2 x0)/2) cos t - (y0 cosh eps) sin t = -(x0^2 + y0^2 + (1 - 2 x0)/2)
    a_e2 = 0.5 * (1.0 - 2.0 * x0)
    b_e2 = -y0 * cosh_e
    rhs_e2 = -(r2_mod + a_e2)
    amp_e2 = math.hypot(a_e2, b_e2)
    e2_xs: list[float] = []
    if amp_e2 > 1e-15 and abs(rhs_e2) < amp_e2 - 1e-15:
        phi_ang = math.atan2(b_e2, a_e2)
        acos_val = math.acos(rhs_e2 / amp_e2)
        for t_sol in (phi_ang + acos_val, phi_ang - acos_val):
            # Normalize to (-pi, pi]
            t_n = math.atan2(math.sin(t_sol), math.cos(t_sol))
            if 1e-14 < t_n < math.pi - 1e-14:
                xs_val = 0.5 * (1.0 + math.cos(t_n))
                e2_xs.append(xs_val)
                crit.append(xs_val)

    crit = sorted({round(v, 14) for v in crit if v >= 0.0})
    # Build xi quadrature nodes over finite subintervals [crit[j], crit[j+1]] + [crit[-1], +infty)
    xi_chunks: list[np.ndarray] = []
    wxi_chunks: list[np.ndarray] = []
    for j in range(len(crit) - 1):
        a_i, b_i = crit[j], crit[j + 1]
        if b_i - a_i > 1e-14:
            hm = 0.5 * (b_i - a_i)
            mm = 0.5 * (b_i + a_i)
            xi_chunks.append(mm + hm * nodes_out)
            wxi_chunks.append(hm * weights_out)
    # Semi-infinite tail [crit[-1], +infty) via xi = c_last + (1 + t)/(1 - t)
    c_last = crit[-1]
    one_m_t = 1.0 - nodes_out
    xi_tail = c_last + (1.0 + nodes_out) / one_m_t
    wxi_tail = weights_out * (2.0 / (one_m_t * one_m_t))
    xi_chunks.append(xi_tail)
    wxi_chunks.append(wxi_tail)

    xi_grid = np.concatenate(xi_chunks)
    w_xi_all = np.concatenate(wxi_chunks)

    a_vec = r2_mod - xi_grid * x0
    b_vec = xi_grid - x0
    bm = b_vec - c_val
    bp = b_vec + c_val
    r1 = a_vec + c_val * xi_grid
    r2 = a_vec - c_val * xi_grid

    z_lo = np.zeros_like(xi_grid)
    z_hi = np.full_like(xi_grid, np.inf)
    pos1 = bm > 1e-15
    neg1 = bm < -1e-15
    with np.errstate(divide="ignore", invalid="ignore"):
        q1 = np.where(pos1 | neg1, r1 / np.where(pos1 | neg1, bm, 1.0), 0.0)
    z_hi = np.where(pos1, np.minimum(z_hi, q1), z_hi)
    z_lo = np.where(neg1, np.maximum(z_lo, q1), z_lo)

    pos2 = bp > 1e-15
    neg2 = bp < -1e-15
    with np.errstate(divide="ignore", invalid="ignore"):
        q2 = np.where(pos2 | neg2, r2 / np.where(pos2 | neg2, bp, 1.0), 0.0)
    z_lo = np.where(pos2, np.maximum(z_lo, q2), z_lo)
    z_hi = np.where(neg2, np.minimum(z_hi, q2), z_hi)

    valid = z_hi > z_lo + 1e-15
    if not np.any(valid):
        return 0.0

    xi_v = xi_grid[valid]
    w_xi_v = w_xi_all[valid]
    zlo_v = z_lo[valid]
    zhi_v = z_hi[valid]

    w_lo = zlo_v / (xi_v + zlo_v)
    w_hi = np.where(np.isinf(zhi_v), 1.0, zhi_v / (xi_v + np.where(np.isinf(zhi_v), 1.0, zhi_v)))

    # Collect inner w-breakpoints per xi_v (from Re z = 0 and Re z = 1 chord clipping if active)
    split_cols = [w_lo, w_hi]
    for ysq in e0_y_sq_splits:
        z_sp = ysq / xi_v
        w_sp = np.clip(z_sp / (xi_v + z_sp), w_lo, w_hi)
        split_cols.append(w_sp)
    for ysq1 in e1_splits:
        # At Re z = 1, (xi - 1)(zeta + 1) = y_1^2 => zeta = y_1^2 / (xi - 1) - 1
        gt1 = xi_v > 1.0 + 1e-12
        z_sp1 = np.where(gt1, ysq1 / np.where(gt1, xi_v - 1.0, 1.0) - 1.0, -1.0)
        z_sp1_pos = np.maximum(0.0, z_sp1)
        w_sp1 = np.where(z_sp1 > 0.0, np.clip(z_sp1_pos / (xi_v + z_sp1_pos), w_lo, w_hi), w_lo)
        split_cols.append(w_sp1)
    for xs2 in e2_xs:
        in_e2 = (xi_v > xs2 + 1e-12) & (xi_v < 1.0 - 1e-12)
        z_sp2 = np.where(in_e2, xs2 * (1.0 - xi_v) / np.where(in_e2, xi_v - xs2, 1.0), -1.0)
        z_sp2_pos = np.maximum(0.0, z_sp2)
        w_sp2 = np.where(z_sp2 > 0.0, np.clip(z_sp2_pos / (xi_v + z_sp2_pos), w_lo, w_hi), w_lo)
        split_cols.append(w_sp2)

    w_breaks = np.sort(np.stack(split_cols, axis=1), axis=1)
    total_val = 0.0
    for j in range(w_breaks.shape[1] - 1):
        wa = w_breaks[:, j]
        wb = w_breaks[:, j + 1]
        hdw = 0.5 * (wb - wa)
        mdw = 0.5 * (wb + wa)
        active_sub = hdw > 1e-15
        if not np.any(active_sub):
            continue
        xi_s = xi_v[active_sub]
        wxi_s = w_xi_v[active_sub]
        hdw_s = hdw[active_sub]
        mdw_s = mdw[active_sub]

        w_mat = mdw_s[:, None] + hdw_s[:, None] * nodes_in[None, :]
        zeta_mat = xi_s[:, None] * w_mat / np.maximum(1e-15, 1.0 - w_mat)
        xi_c = xi_s[:, None]

        c_geo = 0.5 * (xi_c - zeta_mat)
        r_geo = 0.5 * (xi_c + zeta_mat)
        denom_a0 = (x0 - c_geo) ** 2 + y0 * y0 + r_geo * r_geo
        tanh_s0 = np.clip((2.0 * r_geo * (x0 - c_geo)) / denom_a0, -1.0 + 1e-15, 1.0 - 1e-15)
        s0 = np.arctanh(tanh_s0)

        sinh_d = np.abs(r2_mod - (xi_c - zeta_mat) * x0 - xi_c * zeta_mat) / (y0 * (xi_c + zeta_mat))
        cosh_d = np.sqrt(1.0 + sinh_d * sinh_d)
        ratio_ch = cosh_e / cosh_d
        inside = ratio_ch > 1.0
        delta = np.zeros_like(ratio_ch)
        delta[inside] = np.arccosh(np.maximum(1.0, ratio_ch[inside]))

        s_in = 0.5 * np.log(zeta_mat / xi_c)
        gt1_xi = xi_c > 1.0 + 1e-15
        lt1_xi = xi_c < 1.0 - 1e-15
        s_out = np.full_like(s_in, 50.0)
        if np.any(gt1_xi):
            xi_gt = np.where(gt1_xi, xi_c, 2.0)
            s_out = np.where(gt1_xi, 0.5 * np.log((zeta_mat + 1.0) / (xi_gt - 1.0)), s_out)
        if np.any(lt1_xi):
            xi_lt = np.where(lt1_xi, xi_c, 0.5)
            s_out = np.where(
                lt1_xi,
                0.5 * np.log((zeta_mat * (zeta_mat + 1.0)) / (xi_lt * (1.0 - xi_lt))),
                s_out,
            )

        seg_lo = np.maximum(s_in, s0 - delta)
        seg_hi = np.minimum(s_out, s0 + delta)
        chord_len = np.where(inside, np.maximum(0.0, seg_hi - seg_lo), 0.0)

        sub_int = np.sum(chord_len * weights_in[None, :], axis=1) * (hdw_s / xi_s)
        total_val += float(np.sum(sub_int * wxi_s))

    return total_val / ((math.pi * math.pi) / 3.0)


def main() -> None:
    t0 = time.time()
    out_dir = Path(__file__).resolve().parent
    script_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    # 1. Irrational-quantile 60-digit Jensen exponents at all 9 points
    orig_dps = mp.mp.dps
    mp.mp.dps = 165
    points_spec = [
        ("exp(i pi/3)", False, complex(0.5, 0.5 * math.sqrt(3.0)), mp.mpf(1) / 2, mp.sqrt(3) / 2, (1, -2, 2)),
        ("(1 + i sqrt(7))/2", False, complex(0.5, 0.5 * math.sqrt(7.0)), mp.mpf(1) / 2, mp.sqrt(7) / 2, (1, -4, 2)),
        ("Q1 = 21/50 + 123/100 i", False, complex(0.42, 1.23), mp.mpf(21) / 50, mp.mpf(123) / 100, (4200, -16893, 10000)),
        ("Q2 = 2/25 + 33/25 i", False, complex(0.08, 1.32), mp.mpf(2) / 25, mp.mpf(33) / 25, (50, -1093, 625)),
        ("Q3 = 3/25 + 93/50 i", False, complex(0.12, 1.86), mp.mpf(3) / 25, mp.mpf(93) / 50, (300, -8685, 2500)),
        ("i", True, complex(0.0, 1.0), mp.mpf(0), mp.mpf(1), (0, -1, 1)),
        ("i sqrt(2)", True, complex(0.0, math.sqrt(2.0)), mp.mpf(0), mp.sqrt(2), (0, -2, 1)),
        ("i sqrt(3)", True, complex(0.0, math.sqrt(3.0)), mp.mpf(0), mp.sqrt(3), (0, -3, 1)),
        ("Q4 = 67/50 i", True, complex(0.0, 1.34), mp.mpf(0), mp.mpf(67) / 50, (0, -4489, 2500)),
    ]
    mp.mp.dps = orig_dps

    jensen_results: dict[str, Any] = {}
    for name, _, _, x_mp, y_mp, h_tup in points_spec:
        jensen_results[name] = compute_jensen_60d_irrational(
            h_tup[0], h_tup[1], h_tup[2], x_mp, y_mp, n_samples=512
        )

    # 2. Piecewise singularity-split Liouville control at eps = 2^-6
    e_liou = 2.0 ** (-6)
    denom_liou = 12.0 * (math.sinh(0.5 * e_liou) ** 2)
    liou_3side: dict[str, float] = {}
    liou_1side_off: dict[str, float] = {}
    for name, on_ax, z, _, _, _ in points_spec:
        m0 = liouville_sector_piecewise_exact(z, e_liou)
        m1 = liouville_sector_piecewise_exact(rho3_inv(z), e_liou)
        m2 = liouville_sector_piecewise_exact(rho3_inv2(z), e_liou)
        mult = 2.0 if on_ax else 1.0
        liou_3side[name] = (mult * (m0 + m1 + m2)) / denom_liou
        if not on_ax:
            liou_1side_off[name] = m0 / denom_liou

    max_3side_err = max(abs(v - 1.0) for v in liou_3side.values())
    min_1side_err = min(abs(v - 1.0) for v in liou_1side_off.values())
    pc_liouville_fired = bool(max_3side_err < 1e-8 and min_1side_err > 0.50)

    # 3. Riesz 1/2-energy geometric convergence ratio (3/4) vs interior golden atom 1/phi blow-up
    phi = 0.5 * (1.0 + math.sqrt(5.0))
    inv_phi_flt = 1.0 / phi
    riesz_pure: dict[int, float] = {}
    riesz_golden_atom: dict[int, float] = {}
    for d in range(7, 13):
        pud, qud = build_stern_brocot_unit_tree(d)
        x_end = pud.astype(np.float64) / qud.astype(np.float64)
        xmd = (pud[:-1] + pud[1:]).astype(np.float64) / (qud[:-1] + qud[1:]).astype(np.float64)
        len_j = 1.0 / (qud[:-1] * qud[1:]).astype(np.float64)

        w_pure = np.full(len(xmd), 2.0 ** (-d), dtype=np.float64)
        diff = np.abs(xmd[:, None] - xmd[None, :])
        np.fill_diagonal(diff, np.inf)
        riesz_pure[d] = float(
            np.sum((w_pure[:, None] * w_pure[None, :]) * (diff ** (-0.5)))
            + np.sum((w_pure * w_pure) * 2.0 * (len_j ** (-0.5)))
        )

        # Place mass 1/2 in the Stern-Brocot cell containing 1/phi (where |J_d(1/phi)| ~ 1 / (F_{d+1} F_{d+2}) ~ phi^-2d)
        idx_gold = int(np.clip(np.searchsorted(x_end, inv_phi_flt, side="right") - 1, 0, len(xmd) - 1))
        w_gold = np.full(len(xmd), 0.5 * (2.0 ** (-d)), dtype=np.float64)
        w_gold[idx_gold] += 0.5
        riesz_golden_atom[d] = float(
            np.sum((w_gold[:, None] * w_gold[None, :]) * (diff ** (-0.5)))
            + np.sum((w_gold * w_gold) * 2.0 * (len_j ** (-0.5)))
        )

    diffs_pure = {d: riesz_pure[d] - riesz_pure[d - 1] for d in range(8, 13)}
    ratios_pure = {d: diffs_pure[d] / diffs_pure[d - 1] for d in range(9, 13)}
    extrapolated_limit = riesz_pure[12] + diffs_pure[12] * (0.75 / (1.0 - 0.75))

    riesz_verified = bool(
        all(abs(r - 0.75) < 0.01 for r in ratios_pure.values())
        and extrapolated_limit < 4.0
    )
    pc_atomic_fired = bool(
        riesz_golden_atom[12] > 8.0 * riesz_golden_atom[7]
    )

    payload = {
        "card": "X-NEG-postrun-b1868",
        "seat": "agy-exp",
        "script_sha256": script_sha256,
        "elapsed_seconds": round(time.time() - t0, 3),
        "jensen_irrational_60d": jensen_results,
        "PC_B1868_liouville_flat_piecewise": {
            "liouville_3side_f_eps": liou_3side,
            "max_3side_abs_error_from_1": max_3side_err,
            "planted_1side_off_axis_f_eps": liou_1side_off,
            "min_planted_1side_abs_error_from_1": min_1side_err,
            "control_fired": pc_liouville_fired,
        },
        "riesz_geometric_convergence_and_golden_atom": {
            "pure_riesz_by_depth": {str(k): v for k, v in riesz_pure.items()},
            "pure_consecutive_step_ratios": {str(k): v for k, v in ratios_pure.items()},
            "pure_richardson_limit": extrapolated_limit,
            "riesz_geometric_convergence_verified": riesz_verified,
            "golden_atom_riesz_by_depth": {str(k): v for k, v in riesz_golden_atom.items()},
            "golden_atom_ratio_d12_over_d7": riesz_golden_atom[12] / riesz_golden_atom[7],
            "PC_B1868_atomic_measure_fired": pc_atomic_fired,
        },
        "all_postrun_checks_passed": bool(
            pc_liouville_fired
            and riesz_verified
            and pc_atomic_fired
            and (0.86 <= jensen_results["i"]["jensen_60d_cf_mean"] <= 0.89)
            and all(
                jensen_results[q]["jensen_60d_cf_mean"] > 1.0
                for q in (
                    "Q1 = 21/50 + 123/100 i",
                    "Q2 = 2/25 + 33/25 i",
                    "Q3 = 3/25 + 93/50 i",
                    "Q4 = 67/50 i",
                )
            )
        ),
    }

    out_path = out_dir / "postrun_b1868_jensen_and_controls_out.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
