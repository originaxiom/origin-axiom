#!/usr/bin/env python3
"""Standalone zero-shared-code second computation of B1924 whole-weave read-out (A2-B1924).

Implements M23 + M25 + P-845 strictly from mathematical definitions, without reading
any B1924 .py or .json file prior to committing expectations and outputs:
  - Positive move words W in {L, R}^n keeping +-(2, 4) mod 5 (equivalently +-(1, 2) mod 5).
  - Closed hyperbolic geodesic period averages via unit-speed semicircle axis ds = du
    and periodic trapezoid/midpoint rule, pulling every quadrature point back into the
    SL(2,Z) fundamental domain via exact co-transformation of (tau, a, b) so q-series
    maintain machine precision even across deep cusp excursions.
  - Evaluates BOTH mark (2/5, 4/5) and twin (1/5, 2/5) paired on the exact same words,
    weighted by geodesic length ell(gamma_W), with delete-one-word paired ratio jackknife SE.
  - Runs at word lengths n = 10 (exhaustive 2^10 = 1024), n = 16 (exhaustive stabiliser count
    + 200 sampled hyperbolic allowed words), and n = 22 (200 sampled hyperbolic allowed words),
    across ALL THREE coordinate-end constants requested in M25:
      L_coord in {0.90, 1.30, 2.20},
    where L_coord = L + (1/2)*log(Im tau) = L_tilde + gamma + log(pi).
  - Averages direct ratios (m1/m3, m2/m3) and CKM moduli |V_ij| (NOT log-ratios).
  - Runs three adversarial planted controls (CTL-B1924-1..3).

0 of 19.
"""

from __future__ import annotations

import json
import math
import time
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy.special import digamma


OUT_DIR = Path(__file__).resolve().parent

L_MAT = np.array([[1, 1], [0, 1]], dtype=np.int64)
R_MAT = np.array([[1, 0], [1, 1]], dtype=np.int64)

SECTOR_CHARGES: Dict[str, Tuple[int, int]] = {
    "u": (1, -4),
    "d": (1, 2),
    "e": (-3, 6),
}

CHANNEL_THETA_AB: List[Tuple[float, float, float, complex]] = [
    (0.5, 0.5, -1.0, -1.0j),
    (0.5, 0.0, +1.0, -1.0 + 0.0j),
    (0.0, 0.5, +1.0, -1.0 + 0.0j),
    (0.0, 0.0, +1.0, +1.0j),
]

CHANNEL_SHIFTS: List[Tuple[float, float]] = [
    (0.0, 0.0),
    (0.0, 0.5),
    (0.5, 0.0),
    (0.5, 0.5),
]


# ============================================================================
# FAST VECTORISED FRAME ENGINE ON FUNDAMENTAL-DOMAIN QUADRATURE POINTS
# ============================================================================

def sl2z_pullback_points(taus: np.ndarray, line_a: float, line_b: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Pull an array of M points tau in H back into the standard SL(2,Z) fundamental domain
    (|Re tau| <= 1/2, |tau| >= 1, Im tau >= sqrt(3)/2 >= 0.866), co-transforming (a, b) mod 1:
      - Under T^k (tau -> tau - k): w = a*tau + b = a*(tau - k) + (b + k*a) -> (a, (b + k*a) mod 1)
      - Under S   (tau -> -1/tau):  w = a*tau + b = (-1/tau')*a + b -> co-transformed line (b mod 1, (-a) mod 1)
    Wait: let's double-check T^(-k)!
    In P-720 we verified: for tau_new = tau + 1, line_new = (a, (b - a) mod 1) gives
      a * (tau + 1) + (b - a) = a*tau + b!
    Therefore, for tau_new = tau - k, we need a_new * (tau - k) + b_new = a*tau + b,
    so a_new = a, b_new = (b + k*a) mod 1!
    And for tau_new = -1/tau, we verified in P-720 that line_new = (b mod 1, (-a) mod 1) gives
      b * (-1/tau) - a = -(a*tau + b)/tau, which has identical weight-0 ratios and CKM moduli!
    """
    t = taus.astype(np.complex128).copy()
    u1 = np.full(len(t), line_a % 1.0, dtype=np.float64)
    u2 = np.full(len(t), line_b % 1.0, dtype=np.float64)

    for _ in range(250):
        k = np.rint(t.real)
        need_shift = k != 0.0
        if np.any(need_shift):
            t[need_shift] -= k[need_shift]
            u2[need_shift] = (u2[need_shift] + k[need_shift] * u1[need_shift]) % 1.0

        need_inv = np.abs(t) < (1.0 - 1e-12)
        if not np.any(need_inv):
            break
        t[need_inv] = -1.0 / t[need_inv]
        old_u1 = u1[need_inv].copy()
        u1[need_inv] = u2[need_inv] % 1.0
        u2[need_inv] = (-old_u1) % 1.0

    return t, u1, u2


def kronecker_Fu_vec(u1: np.ndarray, u2: np.ndarray, taus_fd: np.ndarray, m_cut: int = 32) -> np.ndarray:
    """Vectorised shifted-lattice Kronecker limit F_u(tau) on fundamental-domain points (Im tau >= 0.866).
    At Im(tau) >= 0.866, exp(-2*pi * 32 * 0.866) ~ 10^-76, well below float64 machine epsilon!"""
    M = len(taus_fd)
    a = u1 % 1.0
    b = u2 % 1.0
    a = np.where((a < 1e-12) | (a > 1.0 - 1e-12), 0.0, a)
    b = np.where((b < 1e-12) | (b > 1.0 - 1e-12), 0.0, b)

    x = taus_fd.real
    y = taus_fd.imag
    out = np.zeros(M, dtype=np.float64)

    mask_zero = (a == 0.0) & (b == 0.0)
    mask_a0 = (a == 0.0) & (~mask_zero)
    mask_gen = ~(mask_zero | mask_a0)

    if np.any(mask_zero):
        tz = taus_fd[mask_zero]
        yz = y[mask_zero]
        m_pows = np.arange(1, 45, dtype=np.float64)[None, :]
        q = np.exp(2j * math.pi * tz)[:, None]
        eta_abs2 = np.exp(-math.pi * yz / 6.0) * np.prod(np.abs(1.0 - q ** m_pows) ** 2, axis=1)
        out[mask_zero] = 2.0 * math.pi * (np.euler_gamma - math.log(2.0) - 0.5 * np.log(yz) - np.log(eta_abs2))

    if np.any(mask_a0):
        xa = x[mask_a0][:, None]
        ya = y[mask_a0][:, None]
        ba = b[mask_a0][:, None]
        base = math.pi * (2.0 * np.euler_gamma - 2.0 * math.log(2.0) - np.log(ya[:, 0]))
        m0 = (math.pi ** 2) * ya[:, 0] / (np.sin(math.pi * ba[:, 0]) ** 2)
        ms = np.concatenate([np.arange(-m_cut, 0, dtype=np.float64), np.arange(1, m_cut + 1, dtype=np.float64)])[None, :]
        wm = np.exp(2j * math.pi * (ms * xa + ba) - 2.0 * math.pi * np.abs(ms) * ya)
        tail = np.sum((2.0 * math.pi / np.abs(ms)) * (wm / (1.0 - wm)).real, axis=1)
        out[mask_a0] = base + m0 + tail

    if np.any(mask_gen):
        xg = x[mask_gen][:, None]
        yg = y[mask_gen][:, None]
        ag = a[mask_gen][:, None]
        bg = b[mask_gen][:, None]
        base = -math.pi * (digamma(ag[:, 0]) + digamma(1.0 - ag[:, 0]) + 2.0 * math.log(2.0) + np.log(yg[:, 0]))
        ms = np.arange(-m_cut, m_cut + 1, dtype=np.float64)[None, :]
        ma = ms + ag
        wm = np.exp(2j * math.pi * (ma * xg + bg) - 2.0 * math.pi * np.abs(ma) * yg)
        tail = np.sum((2.0 * math.pi / np.abs(ma)) * (wm / (1.0 - wm)).real, axis=1)
        out[mask_gen] = base + tail

    return out


def evaluate_frame_observables_on_fd_points(
    taus_fd: np.ndarray,
    la_fd: np.ndarray,
    lb_fd: np.ndarray,
    L_coord_list: List[float],
) -> Dict[float, np.ndarray]:
    """Evaluate all 30 gauge-invariant observables at M fundamental-domain points for multiple L_coord values
    in a single shared theta/Eisenstein pass!
    Observable vector (length 30) per point and per L_coord:
      [0..5]   reading S  mass ratios: (mu/mt, mc/mt, md/mb, ms/mb, me/mtau, mmu/mtau)
      [6..11]  reading S~ mass ratios: (mu/mt, mc/mt, md/mb, ms/mb, me/mtau, mmu/mtau)
      [12..20] SEAT (S~, S, S)   9 CKM moduli |V_ud, V_us, V_ub, V_cd, V_cs, V_cb, V_td, V_ts, V_tb|
      [21..29] SEAT (S~, S~, S~) 9 CKM moduli |V_ud, V_us, V_ub, V_cd, V_cs, V_cb, V_td, V_ts, V_tb|
    """
    M = len(taus_fd)
    # 1. Shared eta, E2, and Serre triplet a(tau) on taus_fd (Im >= 0.866 -> n_max=16, m_max=45 give < 1e-16!):
    m_pows = np.arange(1, 45, dtype=np.float64)[None, :]
    q = np.exp(2j * math.pi * taus_fd)[:, None]
    qp = q ** m_pows
    eta = np.exp(1j * math.pi * taus_fd / 12.0) * np.prod(1.0 - qp, axis=1)
    e2 = 1.0 - 24.0 * np.sum(m_pows * qp / (1.0 - qp), axis=1)
    denom = 2.0 * math.pi * (eta ** 3)

    n_vec = np.arange(-16, 17, dtype=np.float64)[None, :]
    t_col = taus_fd[:, None]

    def theta_0_and_dtau(ca: float, cb: float) -> Tuple[np.ndarray, np.ndarray]:
        na = n_vec + ca
        terms = np.exp(1j * math.pi * (na * na) * t_col + 2j * math.pi * na * cb)
        return np.sum(terms, axis=1), np.sum(0.5 * (na * na) * terms, axis=1)

    t2, dt2 = theta_0_and_dtau(0.5, 0.0)
    t4, dt4 = theta_0_and_dtau(0.0, 0.5)
    t3, dt3 = theta_0_and_dtau(0.0, 0.0)

    R_vec = np.column_stack([-(t2 * t2), -(t4 * t4), 1j * (t3 * t3)]) / denom[:, None]
    dN_vec = np.column_stack([-2.0 * t2 * dt2, -2.0 * t4 * dt4, 2j * t3 * dt3])
    a_S = dN_vec / denom[:, None] - (e2 / 12.0)[:, None] * R_vec
    a_St = np.conj(a_S)

    def theta_kappa_4chan(alpha_arr: np.ndarray, beta_arr: np.ndarray) -> np.ndarray:
        """Overflow-free evaluation of exp(i*pi*alpha*(alpha*tau + beta)) * theta_[ca,cb](alpha*tau + beta | tau)
        by completing the square: Re(exponent) = -pi * (n + ca + alpha)^2 * Im(tau) <= 0 everywhere!"""
        out = np.zeros((M, 4), dtype=np.complex128)
        al_c = alpha_arr[:, None]
        be_c = beta_arr[:, None]
        n_shift = np.rint(al_c)
        pref = np.exp(1j * math.pi * alpha_arr * beta_arr)
        for ch_i, (ca, cb, sgn, _) in enumerate(CHANNEL_THETA_AB):
            na = (n_vec - n_shift) + ca
            terms = np.exp(1j * math.pi * ((na + al_c) ** 2) * t_col + 2j * math.pi * na * (be_c + cb))
            out[:, ch_i] = (sgn * pref) * np.sum(terms, axis=1)
        return out

    C_PREF = np.array([-1j, -1.0 + 0j, -1.0 + 0j, +1j], dtype=np.complex128)[None, :]

    # Precompute R_s (M, 4) and F_u sum (M, 4) per sector (independent of L_coord!):
    R_sec: Dict[str, np.ndarray] = {}
    Fsum_sec: Dict[str, np.ndarray] = {}

    for sec, (qL, qR) in SECTOR_CHARGES.items():
        au = (qL + qR) * la_fd
        bu = (qL + qR) * lb_fd
        ad = (qL - qR) * la_fd
        bd = (qL - qR) * lb_fd
        R_sec[sec] = (C_PREF * theta_kappa_4chan(au, bu) * theta_kappa_4chan(ad, bd)) / denom[:, None]

        fsum = np.zeros((M, 4), dtype=np.float64)
        for ch_i, (s1, s2) in enumerate(CHANNEL_SHIFTS):
            up1 = ((qL + qR) * la_fd + s1) % 1.0
            up2 = ((qL + qR) * lb_fd + s2) % 1.0
            um1 = ((qL - qR) * la_fd + s1) % 1.0
            um2 = ((qL - qR) * lb_fd + s2) % 1.0
            fsum[:, ch_i] = kronecker_Fu_vec(up1, up2, taus_fd) + kronecker_Fu_vec(um1, um2, taus_fd)
        Fsum_sec[sec] = fsum

    def build_Y_batch(a_vecs: np.ndarray, u_chans: np.ndarray) -> np.ndarray:
        u1 = u_chans[:, 0]
        uv = u_chans[:, 1:4]
        Y = a_vecs[:, :, None] * uv[:, None, :] + uv[:, :, None] * a_vecs[:, None, :]
        dots = np.sum(a_vecs * uv, axis=1)
        Y = Y - dots[:, None, None] * np.eye(3, dtype=np.complex128)[None, :, :]
        skew = np.zeros((M, 3, 3), dtype=np.complex128)
        skew[:, 0, 1] = -a_vecs[:, 2]
        skew[:, 0, 2] = a_vecs[:, 1]
        skew[:, 1, 0] = a_vecs[:, 2]
        skew[:, 1, 2] = -a_vecs[:, 0]
        skew[:, 2, 0] = -a_vecs[:, 1]
        skew[:, 2, 1] = a_vecs[:, 0]
        return Y - u1[:, None, None] * skew

    out_by_L: Dict[float, np.ndarray] = {}
    for Lc in L_coord_list:
        obs = np.zeros((M, 30), dtype=np.float64)
        U_left: Dict[Tuple[str, str], np.ndarray] = {}

        for s_idx, sec in enumerate(["u", "d", "e"]):
            norms = 4.0 * math.pi * Lc + Fsum_sec[sec]
            if np.any(norms <= 0.0):
                raise RuntimeError(f"Non-positive channel norm at L_coord={Lc}, sector={sec}: min={np.min(norms)}")
            w_chan = 1.0 / np.sqrt(norms)
            u_vec4 = R_sec[sec] * w_chan

            for r_tag, a_arr, col_off in [("S", a_S, 0), ("S~", a_St, 6)]:
                Y_batch = build_Y_batch(a_arr, u_vec4)
                if sec in ("u", "d"):
                    U_svd, sv, _ = np.linalg.svd(Y_batch)
                    # Ascending mass order (lightest..heaviest = cols 2, 1, 0):
                    U_left[(sec, r_tag)] = U_svd[:, :, ::-1]
                else:
                    sv = np.linalg.svd(Y_batch, compute_uv=False)

                r13 = sv[:, 2] / sv[:, 0]
                r23 = sv[:, 1] / sv[:, 0]
                obs[:, col_off + 2 * s_idx] = r13
                obs[:, col_off + 2 * s_idx + 1] = r23

        # CKM moduli (M, 3, 3) -> flatten 9 entries:
        Uu_St_H = np.conj(np.transpose(U_left[("u", "S~")], (0, 2, 1)))
        V_S = np.abs(Uu_St_H @ U_left[("d", "S")]).reshape(M, 9)
        V_St = np.abs(Uu_St_H @ U_left[("d", "S~")]).reshape(M, 9)
        obs[:, 12:21] = V_S
        obs[:, 21:30] = V_St
        out_by_L[Lc] = obs

    return out_by_L


# ============================================================================
# GEODESIC AXIS & WORD ENUMERATION / SAMPLING
# ============================================================================

def word_bits_to_matrix(bits: int, length: int) -> np.ndarray:
    """Convert an integer bitmask of `length` bits (0 -> L, 1 -> R) to its SL(2,Z) matrix."""
    mat = np.eye(2, dtype=np.int64)
    for pos in range(length - 1, -1, -1):
        if (bits >> pos) & 1:
            # Multiply by R = [[1,0],[1,1]] on right: col0 += col1
            mat[:, 0] += mat[:, 1]
        else:
            # Multiply by L = [[1,1],[0,1]] on right: col1 += col0
            mat[:, 1] += mat[:, 0]
    return mat


def is_allowed_eigenline_mod5(mat: np.ndarray) -> bool:
    """Check (2, 4) @ mat == +-(2, 4) mod 5 (equivalently (1, 2) @ mat == +-(1, 2) mod 5)."""
    v0 = int((2 * mat[0, 0] + 4 * mat[1, 0]) % 5)
    v1 = int((2 * mat[0, 1] + 4 * mat[1, 1]) % 5)
    return (v0 == 2 and v1 == 4) or (v0 == 3 and v1 == 1)


def geodesic_axis_points(mat: np.ndarray, density_per_len: float = 48.0, min_nodes: int = 256) -> Tuple[float, np.ndarray]:
    """Return hyperbolic length ell(mat) and midpoint-quadrature points tau(u_k) along one closed period
    [0, ell) for a hyperbolic matrix mat = [[p, q], [r, s]] with p + s > 2."""
    p, q, r, s = float(mat[0, 0]), float(mat[0, 1]), float(mat[1, 0]), float(mat[1, 1])
    tr = p + s
    assert tr > 2.0 and r != 0.0, f"Matrix is not non-parabolic mixed word: {mat}"
    disc = math.sqrt(tr * tr - 4.0)
    ell = 2.0 * math.log(0.5 * (tr + disc))
    x_plus = ((p - s) + disc) / (2.0 * r)
    x_minus = ((p - s) - disc) / (2.0 * r)
    center = 0.5 * (x_plus + x_minus)
    half_span = 0.5 * (x_plus - x_minus)
    radius = abs(half_span)

    n_quad = max(min_nodes, int(math.ceil(density_per_len * ell)))
    # Periodic midpoint grid u_k = (k + 0.5) * ell / n_quad on [0, ell)
    # (for periodic functions on [0, ell], periodic midpoint and periodic trapezoid have identical spectral accuracy!):
    u = (np.arange(n_quad, dtype=np.float64) + 0.5) * (ell / n_quad)
    taus = (center + half_span * np.tanh(u)) + 1j * (radius / np.cosh(u))
    return ell, taus


def paired_ratio_jackknife(lengths: np.ndarray, mark_vals: np.ndarray, twin_vals: np.ndarray) -> dict:
    """Compute length-weighted means for mark, twin, and paired difference (mark - twin),
    plus exact delete-one-word ratio jackknife standard errors!
    lengths: (W,), mark_vals: (W, D), twin_vals: (W, D)."""
    W = len(lengths)
    L_sum = float(np.sum(lengths))
    w_col = lengths[:, None]

    S_mark = np.sum(w_col * mark_vals, axis=0)
    S_twin = np.sum(w_col * twin_vals, axis=0)
    mean_mark = S_mark / L_sum
    mean_twin = S_twin / L_sum
    mean_diff = mean_mark - mean_twin

    if W <= 1:
        zeros = np.zeros_like(mean_mark)
        return {
            "mark_mean": mean_mark,
            "twin_mean": mean_twin,
            "diff_mean": mean_diff,
            "mark_se": zeros,
            "twin_se": zeros,
            "paired_diff_se": zeros,
            "unpaired_diff_se": zeros,
        }

    denom_loo = (L_sum - lengths)[:, None]
    loo_mark = (S_mark[None, :] - w_col * mark_vals) / denom_loo
    loo_twin = (S_twin[None, :] - w_col * twin_vals) / denom_loo
    loo_diff = loo_mark - loo_twin

    fac = (W - 1.0) / W
    mark_se = np.sqrt(fac * np.sum((loo_mark - np.mean(loo_mark, axis=0, keepdims=True)) ** 2, axis=0))
    twin_se = np.sqrt(fac * np.sum((loo_twin - np.mean(loo_twin, axis=0, keepdims=True)) ** 2, axis=0))
    paired_se = np.sqrt(fac * np.sum((loo_diff - np.mean(loo_diff, axis=0, keepdims=True)) ** 2, axis=0))
    unpaired_se = np.sqrt(mark_se ** 2 + twin_se ** 2)

    return {
        "mark_mean": mean_mark,
        "twin_mean": mean_twin,
        "diff_mean": mean_diff,
        "mark_se": mark_se,
        "twin_se": twin_se,
        "paired_diff_se": paired_se,
        "unpaired_diff_se": unpaired_se,
    }


OBS_NAMES = [
    "S_mu_mt", "S_mc_mt", "S_md_mb", "S_ms_mb", "S_me_mtau", "S_mmu_mtau",
    "St_mu_mt", "St_mc_mt", "St_md_mb", "St_ms_mb", "St_me_mtau", "St_mmu_mtau",
    "CKM_S_Vud", "CKM_S_Vus", "CKM_S_Vub", "CKM_S_Vcd", "CKM_S_Vcs", "CKM_S_Vcb", "CKM_S_Vtd", "CKM_S_Vts", "CKM_S_Vtb",
    "CKM_St_Vud", "CKM_St_Vus", "CKM_St_Vub", "CKM_St_Vcd", "CKM_St_Vcs", "CKM_St_Vcb", "CKM_St_Vtd", "CKM_St_Vts", "CKM_St_Vtb",
]


def evaluate_word_ensemble(mats: List[np.ndarray], L_coords: List[float]) -> Dict[float, dict]:
    W = len(mats)
    lengths = np.zeros(W, dtype=np.float64)
    mark_word_avgs = {Lc: np.zeros((W, 30), dtype=np.float64) for Lc in L_coords}
    twin_word_avgs = {Lc: np.zeros((W, 30), dtype=np.float64) for Lc in L_coords}

    for wi, mat in enumerate(mats):
        ell, taus = geodesic_axis_points(mat)
        lengths[wi] = ell

        # Pullback for mark (2/5, 4/5) and twin (1/5, 2/5):
        t_m, a_m, b_m = sl2z_pullback_points(taus, 0.4, 0.8)
        t_t, a_t, b_t = sl2z_pullback_points(taus, 0.2, 0.4)

        obs_m = evaluate_frame_observables_on_fd_points(t_m, a_m, b_m, L_coords)
        obs_t = evaluate_frame_observables_on_fd_points(t_t, a_t, b_t, L_coords)

        for Lc in L_coords:
            mark_word_avgs[Lc][wi] = np.mean(obs_m[Lc], axis=0)
            twin_word_avgs[Lc][wi] = np.mean(obs_t[Lc], axis=0)

    summary_by_L: Dict[float, dict] = {}
    for Lc in L_coords:
        jk = paired_ratio_jackknife(lengths, mark_word_avgs[Lc], twin_word_avgs[Lc])
        obs_table = {}
        max_abs_diff = 0.0
        max_z_score = 0.0
        for oi, oname in enumerate(OBS_NAMES):
            dm = float(jk["diff_mean"][oi])
            pse = float(jk["paired_diff_se"][oi])
            z = abs(dm) / pse if pse > 1e-15 else 0.0
            max_abs_diff = max(max_abs_diff, abs(dm))
            max_z_score = max(max_z_score, z)
            obs_table[oname] = {
                "mark": float(jk["mark_mean"][oi]),
                "mark_se": float(jk["mark_se"][oi]),
                "twin": float(jk["twin_mean"][oi]),
                "twin_se": float(jk["twin_se"][oi]),
                "mark_minus_twin": dm,
                "paired_se": pse,
                "unpaired_se": float(jk["unpaired_diff_se"][oi]),
                "abs_z_paired": z,
            }
        summary_by_L[Lc] = {
            "n_words_evaluated": W,
            "mean_geodesic_length": float(np.mean(lengths)),
            "total_geodesic_length": float(np.sum(lengths)),
            "max_abs_mark_minus_twin": max_abs_diff,
            "max_paired_z_score": max_z_score,
            "observables": obs_table,
        }
    return summary_by_L


def run_periodicity_and_planted_controls() -> dict:
    # 1. Check periodicity and quadrature doubling on golden word LR = [[2,1],[1,1]] and asymmetric allowed word:
    # Find first asymmetric allowed hyperbolic word at n=6:
    asym_mat = None
    for bits in range(64):
        m = word_bits_to_matrix(bits, 6)
        if is_allowed_eigenline_mod5(m) and (m[0, 0] + m[1, 1] > 2) and (m[0, 1] != m[1, 0]):
            asym_mat = m
            break
    assert asym_mat is not None

    ell_a, taus_256 = geodesic_axis_points(asym_mat, density_per_len=48.0, min_nodes=256)
    _, taus_512 = geodesic_axis_points(asym_mat, density_per_len=96.0, min_nodes=512)

    # Endpoint periodicity check at u = 0 vs u = ell_a:
    p, q, r, s = float(asym_mat[0, 0]), float(asym_mat[0, 1]), float(asym_mat[1, 0]), float(asym_mat[1, 1])
    disc = math.sqrt((p + s) ** 2 - 4.0)
    xp, xm = ((p - s) + disc) / (2 * r), ((p - s) - disc) / (2 * r)
    c0, hs = 0.5 * (xp + xm), 0.5 * (xp - xm)
    u_ends = np.array([0.13, 0.13 + ell_a])
    t_ends = (c0 + hs * np.tanh(u_ends)) + 1j * (abs(hs) / np.cosh(u_ends))
    tf_ends, af_ends, bf_ends = sl2z_pullback_points(t_ends, 0.4, 0.8)
    obs_ends = evaluate_frame_observables_on_fd_points(tf_ends, af_ends, bf_ends, [1.30])[1.30]
    periodicity_err = float(np.max(np.abs(obs_ends[1] - obs_ends[0])))

    # Quadrature convergence check (256 vs 512 nodes — resolving narrow light-up avoided crossings!):
    tf256, af256, bf256 = sl2z_pullback_points(taus_256, 0.4, 0.8)
    tf512, af512, bf512 = sl2z_pullback_points(taus_512, 0.4, 0.8)
    avg256 = np.mean(evaluate_frame_observables_on_fd_points(tf256, af256, bf256, [1.30])[1.30], axis=0)
    avg512 = np.mean(evaluate_frame_observables_on_fd_points(tf512, af512, bf512, [1.30])[1.30], axis=0)
    quad_ratio_err = float(np.max(np.abs(avg512[:12] - avg256[:12])))
    quad_ckm_err = float(np.max(np.abs(avg512[12:] - avg256[12:])))

    # CTL-B1924-2: Non-stabilised word RL = [[1,1],[1,2]] maps (2,4) -> (1,0) mod 5 => FAILS periodicity on mark!
    rl_mat = R_MAT @ L_MAT
    assert not is_allowed_eigenline_mod5(rl_mat)
    ell_rl = 2.0 * math.log(0.5 * (3.0 + math.sqrt(5.0)))
    prl, qrl, rrl, srl = 1.0, 1.0, 1.0, 2.0
    disc_rl = math.sqrt(5.0)
    xp_rl, xm_rl = (-1.0 + disc_rl) / 2.0, (-1.0 - disc_rl) / 2.0
    c_rl, hs_rl = 0.5 * (xp_rl + xm_rl), 0.5 * (xp_rl - xm_rl)
    u_rl = np.array([0.2, 0.2 + ell_rl])
    t_rl = (c_rl + hs_rl * np.tanh(u_rl)) + 1j * (abs(hs_rl) / np.cosh(u_rl))
    tfrl, afrl, bfrl = sl2z_pullback_points(t_rl, 0.4, 0.8)
    obs_rl = evaluate_frame_observables_on_fd_points(tfrl, afrl, bfrl, [1.30])[1.30]
    non_allowed_period_break = float(np.max(np.abs(obs_rl[1] - obs_rl[0])))

    # CTL-B1924-3: Holding bare L constant instead of L_coord = L + 0.5*ln(Im tau) along u_ends breaks period invariance!
    L_bare = 1.10
    Lc_u0 = L_bare + 0.5 * math.log(t_ends[0].imag)
    Lc_u1 = L_bare + 0.5 * math.log(t_ends[1].imag)
    obs_bad0 = evaluate_frame_observables_on_fd_points(tf_ends[0:1], af_ends[0:1], bf_ends[0:1], [Lc_u0])[Lc_u0][0]
    obs_bad1 = evaluate_frame_observables_on_fd_points(tf_ends[1:2], af_ends[1:2], bf_ends[1:2], [Lc_u1])[Lc_u1][0]
    bare_L_period_break = float(np.max(np.abs(obs_bad1 - obs_bad0)))

    assert periodicity_err < 1e-12
    assert quad_ratio_err < 1e-7 and quad_ckm_err < 5e-4
    assert non_allowed_period_break > 1e-2
    assert bare_L_period_break > 1e-3

    return {
        "allowed_word_periodicity_max_err": periodicity_err,
        "quadrature_256_vs_512_mass_ratio_max_diff": quad_ratio_err,
        "quadrature_256_vs_512_ckm_max_diff": quad_ckm_err,
        "CTL_B1924_2_non_allowed_RL_period_break": non_allowed_period_break,
        "CTL_B1924_2_caught": bool(non_allowed_period_break > 1e-2),
        "CTL_B1924_3_bare_L_period_break": bare_L_period_break,
        "CTL_B1924_3_caught": bool(bare_L_period_break > 1e-3),
    }


def main() -> None:
    t0 = time.time()
    L_COORDS = [0.90, 1.30, 2.20]
    print("=== AGY-002 STANDALONE SECOND COMPUTATION: B1924 WHOLE-WEAVE READ-OUT (M23 + M25) ===")
    print(f"Fixed coordinate ends L_coord = L + (1/2) log Im(tau): {L_COORDS}")

    print("\n[1/4] Verifying geodesic periodicity, quadrature convergence, and planted controls...")
    ctl_res = run_periodicity_and_planted_controls()
    for k, v in ctl_res.items():
        print(f"  {k}: {v}")

    # 2. Word length n = 10 (EXACT EXHAUSTIVE CENSUS over all 2^10 = 1,024 words):
    print("\n[2/4] Running n = 10 exhaustive census (all 1,024 words in {L, R}^10)...")
    allowed_10_hyp = []
    n_parabolic_10 = 0
    for bits in range(1 << 10):
        m = word_bits_to_matrix(bits, 10)
        if is_allowed_eigenline_mod5(m):
            if m[0, 0] + m[1, 1] <= 2:
                n_parabolic_10 += 1
            else:
                allowed_10_hyp.append(m)
    tot_allowed_10 = len(allowed_10_hyp) + n_parabolic_10
    print(f"  n = 10: allowed total = {tot_allowed_10}/1024 ({tot_allowed_10/1024:.5f}), parabolic = {n_parabolic_10}, hyperbolic = {len(allowed_10_hyp)}")
    res_10 = evaluate_word_ensemble(allowed_10_hyp, L_COORDS)

    # 3. Word length n = 16 (EXHAUSTIVE stabiliser count over all 65,536 words + uniform sample of 200 allowed hyperbolic words):
    print("\n[3/4] Running n = 16 exhaustive stabiliser census (65,536 words) + 200-word paired read-out...")
    allowed_16_hyp = []
    n_parabolic_16 = 0
    for bits in range(1 << 16):
        m = word_bits_to_matrix(bits, 16)
        if is_allowed_eigenline_mod5(m):
            if m[0, 0] + m[1, 1] <= 2:
                n_parabolic_16 += 1
            else:
                allowed_16_hyp.append(m)
    tot_allowed_16 = len(allowed_16_hyp) + n_parabolic_16
    print(f"  n = 16: allowed total = {tot_allowed_16}/65536 ({tot_allowed_16/65536:.5f}, 1/12 = {1/12:.5f}), parabolic = {n_parabolic_16}, hyperbolic = {len(allowed_16_hyp)}")
    rng16 = np.random.default_rng(2026192416)
    idx16 = rng16.choice(len(allowed_16_hyp), size=200, replace=False)
    sample_16 = [allowed_16_hyp[i] for i in idx16]
    res_16 = evaluate_word_ensemble(sample_16, L_COORDS)

    # 4. Word length n = 22 (Uniform rejection sampling of 200 allowed hyperbolic words from {L, R}^22):
    print("\n[4/4] Running n = 22 uniform draw of 200 allowed hyperbolic words from {L, R}^22...")
    rng22 = np.random.default_rng(2026192422)
    sample_22 = []
    n_trials_22 = 0
    seen_bits_22 = set()
    while len(sample_22) < 200:
        b = int(rng22.integers(0, 1 << 22))
        if b in seen_bits_22:
            continue
        seen_bits_22.add(b)
        n_trials_22 += 1
        m = word_bits_to_matrix(b, 22)
        if is_allowed_eigenline_mod5(m) and (m[0, 0] + m[1, 1] > 2):
            sample_22.append(m)
    print(f"  n = 22: drew 200 unique allowed hyperbolic words in {n_trials_22} uniform trials (empirical hit rate = {200/n_trials_22:.5f})")
    res_22 = evaluate_word_ensemble(sample_22, L_COORDS)

    # Check CTL-B1924-1 (unpaired vs paired SE ratio at n=16, L_coord=1.30):
    SampleObs = res_16[1.30]["observables"]["S_ms_mb"]
    se_ratio_unpaired_vs_paired = SampleObs["unpaired_se"] / max(SampleObs["paired_se"], 1e-15)
    ctl_res["CTL_B1924_1_unpaired_over_paired_se_ratio_ms_mb"] = se_ratio_unpaired_vs_paired
    ctl_res["CTL_B1924_1_recorded"] = True

    # Print concise comparison table across n = 10, 16, 22 and L_coord = 0.90, 1.30, 2.20:
    print("\n=== SUMMARY ACROSS L_coord IN {0.90, 1.30, 2.20} AND n IN {10, 16, 22} ===")
    key_obs = ["S_mc_mt", "S_ms_mb", "S_mmu_mtau", "St_mc_mt", "St_ms_mb", "St_mmu_mtau", "CKM_S_Vus", "CKM_S_Vcb", "CKM_St_Vus", "CKM_St_Vcb"]
    for Lc in L_COORDS:
        print(f"\n--- Coordinate End L_coord = {Lc:.2f} (L_tilde = {Lc - np.euler_gamma - math.log(math.pi):+.4f}) ---")
        for n_val, rdict in [(10, res_10[Lc]), (16, res_16[Lc]), (22, res_22[Lc])]:
            print(f"  n = {n_val:2d}: max |mark - twin| = {rdict['max_abs_mark_minus_twin']:.5f} (max paired |z| = {rdict['max_paired_z_score']:.2f})")
        for oname in key_obs:
            o10 = res_10[Lc]["observables"][oname]
            o16 = res_16[Lc]["observables"][oname]
            o22 = res_22[Lc]["observables"][oname]
            print(
                f"    {oname:12s}: n=10 mark={o10['mark']:.5f} diff={o10['mark_minus_twin']:+.5f} | "
                f"n=16 mark={o16['mark']:.5f}+-{o16['mark_se']:.5f} diff={o16['mark_minus_twin']:+.5f}+-{o16['paired_se']:.5f} | "
                f"n=22 mark={o22['mark']:.5f}+-{o22['mark_se']:.5f} diff={o22['mark_minus_twin']:+.5f}+-{o22['paired_se']:.5f}"
            )

    payload = {
        "card": "AGY-002_A2-B1924_whole-weave-readout-second-computation",
        "elapsed_sec": round(time.time() - t0, 3),
        "L_coords_tested": L_COORDS,
        "L_tilde_values": [float(Lc - np.euler_gamma - math.log(math.pi)) for Lc in L_COORDS],
        "controls": ctl_res,
        "n10_exhaustive": {
            "total_words": 1024,
            "allowed_total": tot_allowed_10,
            "allowed_parabolic": n_parabolic_10,
            "allowed_hyperbolic": len(allowed_10_hyp),
            "by_L_coord": {f"{Lc:.2f}": res_10[Lc] for Lc in L_COORDS},
        },
        "n16_sample200": {
            "total_words": 65536,
            "allowed_total": tot_allowed_16,
            "allowed_parabolic": n_parabolic_16,
            "allowed_hyperbolic_total": len(allowed_16_hyp),
            "sampled_hyperbolic_words": 200,
            "by_L_coord": {f"{Lc:.2f}": res_16[Lc] for Lc in L_COORDS},
        },
        "n22_sample200": {
            "uniform_trials": n_trials_22,
            "sampled_hyperbolic_words": 200,
            "empirical_allowed_fraction": 200.0 / n_trials_22,
            "by_L_coord": {f"{Lc:.2f}": res_22[Lc] for Lc in L_COORDS},
        },
    }
    out_json = OUT_DIR / "verify_b1924_results.json"
    out_json.write_text(json.dumps(payload, indent=2, default=float), encoding="utf-8")
    print(f"\nWrote {out_json} in {payload['elapsed_sec']:.2f}s.")
    print("0 of 19.")


if __name__ == "__main__":
    main()
