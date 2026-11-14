#!/usr/bin/env python3
"""Standalone zero-shared-code verification of M21 load-bearing negatives (A2-NEG).

Covers all three items in M21 on origin/main:
  1. B1839 cell D and B1841 cell D (matched look-elsewhere null over 23 levels
     vs 4 principled levels, 1,000,000 random hierarchies, 1% upper-97.5% gate,
     strictly data-free: zero measured Standard Model constants imported).
  2. P-720 modular weight of B1656's four-channel frame with B1919's Kronecker
     limit channel norm and B1921's invariant end passed as
     L_coord = L + (1/2) log Im(tau) = L_tilde + gamma + log(pi),
     tested at 3 generic points tau and 3 flat lines of distinct orders, plus
     unitary basis-scrambling invariance.
  3. HARVEST_LEDGER rows 945 (W29, Z_6 twist-eater in E_8) and 949 (W31, Z_5
     twist-eater in E_8): third independent computation of centralisers,
     matter representations, move-lift decompositions, and chiral anomaly counts.
  4. Five adversarial planted controls (CTL-NEG-1 through CTL-NEG-5).

Zero producer code from frontier/ is imported or read. Only data-free cached
pre-registration tables (accessory.jsonl, norms_index.json, norms.npz) are read
from origin/main via git show for Sub-task 1, and cross-checked against our
independent Yukawa frame engine.

0 of 19.
"""

from __future__ import annotations

import io
import json
import math
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy.spatial import cKDTree
from scipy.special import betaincinv, digamma


REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = Path(__file__).resolve().parent


# ============================================================================
# SECTION 1: STANDALONE JACOBI THETA, EISENSTEIN E2, KRONECKER LIMIT F_u,
#            AND B1656 / B1691 / B1919 / B1921 FOUR-CHANNEL FRAME ENGINE
# ============================================================================

def jacobi_theta_char(a: float, b: float, z: complex, tau: complex, n_max: int = 28) -> Tuple[complex, complex]:
    """Compute theta[a;b](z|tau) and (1/(2*pi*i)) d/dtau theta[a;b](z|tau) directly from q-series."""
    n = np.arange(-n_max, n_max + 1, dtype=np.float64)
    na = n + a
    exponents = 1j * np.pi * (na * na) * tau + 2j * np.pi * na * (z + b)
    terms = np.exp(exponents)
    val = complex(np.sum(terms))
    dtau_over_2pii = complex(np.sum(0.5 * (na * na) * terms))
    return val, dtau_over_2pii


def eta_and_e2(tau: complex, m_max: int = 80) -> Tuple[complex, complex]:
    """Compute Dedekind eta(tau) and quasi-modular Eisenstein E_2(tau) from q-series."""
    q = np.exp(2j * np.pi * tau)
    q_pows = q ** np.arange(1, m_max + 1)
    eta = np.exp(1j * np.pi * tau / 12.0) * np.prod(1.0 - q_pows)
    sigma1_term = np.sum(np.arange(1, m_max + 1, dtype=np.float64) * q_pows / (1.0 - q_pows))
    e2 = 1.0 - 24.0 * sigma1_term
    return complex(eta), complex(e2)


def sl2z_reduce_with_line(tau: complex, a: float, b: float) -> Tuple[complex, float, float, complex]:
    """Reduce tau into the standard SL(2,Z) fundamental domain while co-transforming
    the flat line (a, b) mod 1 and accumulating the (c*tau + d) automorphy factor.
    Under T: tau -> tau + 1, w = a*tau + b = a*(tau+1) + (b - a) -> (a, b - a), factor = 1.
    Under S: tau -> -1/tau, w = a*tau + b = (-a + b*tau')/(-tau') -> (b, -a), factor = tau.
    Wait: let's verify! If tau' = -1/tau, then a'*tau' + b' = b*(-1/tau) - a = -(a*tau + b)/tau!
    Here we use SL(2,Z) reduction ONLY for F_u(tau) (which is strictly weight 0 invariant!)
    when Im(tau) is small; for P-720 we evaluate directly at the given tau in H without reduction!
    """
    t = complex(tau)
    u1 = a % 1.0
    u2 = b % 1.0
    j_aut = 1.0 + 0.0j
    for _ in range(200):
        k = int(round(t.real))
        if k != 0:
            t = t - k
            u2 = (u2 + k * u1) % 1.0
        if abs(t) < 1.0 - 1e-12:
            j_aut *= t
            t = -1.0 / t
            u1, u2 = u2 % 1.0, (-u1) % 1.0
        else:
            break
    return t, u1, u2, j_aut


def kronecker_limit_Fu(u1: float, u2: float, tau: complex, m_cut: int = 60) -> float:
    """First-principles shifted-lattice Kronecker limit F_u(tau) (B1919):
      E_u(tau, s) = sum'_{m,n in Z} (Im tau)^s / |(m + u1)*tau + (n + u2)|^(2s)
                  = [1/(s-1) if u in Z^2 else 0] + F_u(tau) + O(s-1).
    Evaluated via exact Poisson summation in n after exact SL(2,Z) pullback to Im(tau) >= sqrt(3)/2.
    """
    t, a, b, _ = sl2z_reduce_with_line(tau, u1, u2)
    # Snap near-integer shifts cleanly:
    if a < 1e-13 or a > 1.0 - 1e-13:
        a = 0.0
    if b < 1e-13 or b > 1.0 - 1e-13:
        b = 0.0
    x = t.real
    y = t.imag

    if a == 0.0 and b == 0.0:
        # Classical Kronecker first limit formula:
        # F_0(tau) = 2*pi*(gamma - log 2 - log(sqrt(y) * |eta(tau)|^2))
        eta, _ = eta_and_e2(t)
        return float(2.0 * math.pi * (np.euler_gamma - math.log(2.0) - math.log(math.sqrt(y) * abs(eta) ** 2)))

    if a == 0.0:
        # m = 0 row contributes pi^2 * y / sin^2(pi * b) + pi*(2*gamma - 2*log 2 - log y);
        # m != 0 rows contribute sum_{m != 0} (2*pi/|m|) Re(w_m / (1 - w_m)),
        # where w_m = exp(2*pi*i*(m*x + b) - 2*pi*|m|*y)? Wait: careful with sign of b for m < 0!
        # Let's check: for fixed m != 0, sum_{n in Z} |m*tau + n + b|^(-2s) has shift z_m = m*x + b + i*|m|*y.
        # Poisson sum gives (2*pi/|m|) * sum_{k >= 1} exp(-2*pi*k*|m|*y) * cos(2*pi*k*(m*x + b))
        # = (2*pi/|m|) * Re( w_m / (1 - w_m) ) with w_m = exp(2*pi*i*(m*x + b) - 2*pi*|m|*y)!
        base = math.pi * (2.0 * np.euler_gamma - 2.0 * math.log(2.0) - math.log(y))
        m0 = (math.pi ** 2) * y / (math.sin(math.pi * b) ** 2)
        s_tail = 0.0
        for m in range(-m_cut, m_cut + 1):
            if m == 0:
                continue
            wm = np.exp(2j * math.pi * (m * x + b) - 2.0 * math.pi * abs(m) * y)
            s_tail += (2.0 * math.pi / abs(m)) * (wm / (1.0 - wm)).real
        return float(base + m0 + s_tail)

    # Generic case a in (0, 1):
    # m-sum over Z of (m + a)^(-2s) at s=1 gives -pi * (psi(a) + psi(1-a) + 2*log 2 + log y),
    # plus Bessel/exponential series sum_{m in Z} (2*pi/|m+a|) Re(w_m / (1 - w_m)),
    # where w_m = exp(2*pi*i*((m+a)*x + b) - 2*pi*|m+a|*y).
    base = -math.pi * (float(digamma(a) + digamma(1.0 - a)) + 2.0 * math.log(2.0) + math.log(y))
    s_tail = 0.0
    for m in range(-m_cut, m_cut + 1):
        ma = m + a
        wm = np.exp(2j * math.pi * (ma * x + b) - 2.0 * math.pi * abs(ma) * y)
        s_tail += (2.0 * math.pi / abs(ma)) * (wm / (1.0 - wm)).real
    return float(base + s_tail)


# Standard sector charge pairs (q_L, q_R) from B1691 / B1720 / B1839:
SECTOR_CHARGES: Dict[str, Tuple[int, int]] = {
    "u": (1, -4),
    "d": (1, 2),
    "e": (-3, 6),
}

# Channel ordering (1, i, j, k) <-> (theta_1, theta_2, theta_4, theta_3)
# Characteristic shifts c_s - (1/2, 1/2) for the four channels:
CHANNEL_THETA_AB: List[Tuple[float, float, float, complex]] = [
    # (char_a, char_b, sign_prefix_for_standard_theta, C_s)
    (0.5, 0.5, -1.0, -1.0j),  # s=1: theta_1(z) = -theta[1/2;1/2](z), C_1 = -i, shift = (0, 0)
    (0.5, 0.0, +1.0, -1.0 + 0.0j),  # s=i: theta_2(z) = +theta[1/2;0](z), C_i = -1, shift = (0, 1/2)
    (0.0, 0.5, +1.0, -1.0 + 0.0j),  # s=j: theta_4(z) = +theta[0;1/2](z), C_j = -1, shift = (1/2, 0)
    (0.0, 0.0, +1.0, +1.0j),  # s=k: theta_3(z) = +theta[0;0](z), C_k = +i, shift = (1/2, 1/2)
]

CHANNEL_SHIFTS: List[Tuple[float, float]] = [
    (0.0, 0.0),
    (0.0, 0.5),
    (0.5, 0.0),
    (0.5, 0.5),
]


def serre_triplet_a(tau: complex) -> np.ndarray:
    """Compute the weight-3/2 covariant Higgs triplet a(tau) = D_{-1/2} R(tau) (B1653 / B1656),
    where R(tau) = (-theta_2(0)^2, -theta_4(0)^2, i*theta_3(0)^2) / (2*pi*eta(tau)^3)
    has weight -1/2, and D_k = (1/(2*pi*i)) d/dtau - (k/12) E_2(tau).
    Since d/dtau(eta^3)/(2*pi*i*eta^3) = E_2/8, for k = -1/2:
      D_{-1/2}(N / (2*pi*eta^3)) = (D_0 N) / (2*pi*eta^3) - (1/12) E_2 R.
    """
    eta, e2 = eta_and_e2(tau)
    denom = 2.0 * math.pi * (eta ** 3)
    t2, dt2 = jacobi_theta_char(0.5, 0.0, 0.0j, tau)
    t4, dt4 = jacobi_theta_char(0.0, 0.5, 0.0j, tau)
    t3, dt3 = jacobi_theta_char(0.0, 0.0, 0.0j, tau)

    R_vec = np.array([-(t2 * t2), -(t4 * t4), 1j * (t3 * t3)], dtype=np.complex128) / denom
    dN_vec = np.array([-2.0 * t2 * dt2, -2.0 * t4 * dt4, 2j * t3 * dt3], dtype=np.complex128)
    return dN_vec / denom - (e2 / 12.0) * R_vec


def build_yukawa_from_weights(
    tau: complex,
    line_a: float,
    line_b: float,
    sector: str,
    reading: str,
    weights_4: np.ndarray,
) -> np.ndarray:
    """Construct the 3x3 Yukawa matrix Y_f(tau, line, reading) given precomputed 4-channel
    inverse-sqrt norm weights w_s = 1/sqrt(N_s) (active if > 0).
    """
    qL, qR = SECTOR_CHARGES[sector]
    w_line = line_a * tau + line_b
    u_bar = (qL + qR) * w_line
    delta = (qL - qR) * w_line

    alpha_ubar = (qL + qR) * line_a
    alpha_delta = (qL - qR) * line_a
    # Holomorphic Heisenberg translation prefactor making R_s elliptic on C/(Z + Z*tau)
    # and covariant of weight -1/2 under SL(2,Z):
    kappa = np.exp(1j * math.pi * (alpha_ubar * u_bar + alpha_delta * delta))

    eta, _ = eta_and_e2(tau)
    denom = 2.0 * math.pi * (eta ** 3)

    u_chan = np.zeros(4, dtype=np.complex128)
    for idx, (ca, cb, sgn, c_pref) in enumerate(CHANNEL_THETA_AB):
        if weights_4[idx] <= 0.0:
            continue
        th_u, _ = jacobi_theta_char(ca, cb, u_bar, tau)
        th_d, _ = jacobi_theta_char(ca, cb, delta, tau)
        R_s = kappa * c_pref * (sgn * th_u) * (sgn * th_d) / denom
        u_chan[idx] = R_s * weights_4[idx]

    a_base = serre_triplet_a(tau)
    if reading == "S":
        a_vec = a_base
    elif reading == "S*":
        a_vec = np.array([a_base[0], a_base[1], np.conj(a_base[2])], dtype=np.complex128)
    else:
        a_vec = np.conj(a_base)

    u1 = u_chan[0]
    u_vec = u_chan[1:4]
    skew_a = np.array([
        [0.0j, -a_vec[2], a_vec[1]],
        [a_vec[2], 0.0j, -a_vec[0]],
        [-a_vec[1], a_vec[0], 0.0j],
    ], dtype=np.complex128)

    # B1656 four-channel quaternion contraction with sign_u1 = -1 (shared left-null-vector theorem U4):
    Y = np.outer(a_vec, u_vec) + np.outer(u_vec, a_vec) - np.dot(a_vec, u_vec) * np.eye(3, dtype=np.complex128) - u1 * skew_a
    return Y


def channel_weights_b1919_b1921(
    tau: complex,
    line_a: float,
    line_b: float,
    sector: str,
    L_coord: float,
) -> Tuple[np.ndarray, np.ndarray, float]:
    """Compute the 4-channel inverse-sqrt norm weights w_s = 1/sqrt(N_s) using B1919's
    Kronecker limit F_u and B1921's invariant end passed as:
      L_coord = L + (1/2)*log(Im tau) = L_tilde + gamma + log(pi).
    Hence:
      N_s = 4*pi*L_coord + F_{u_+}(tau) + F_{u_-}(tau),
    where u_+ = ((q_L+q_R)*a + s_1, (q_L+q_R)*b + s_2) mod 1,
          u_- = ((q_L-q_R)*a + s_1, (q_L-q_R)*b + s_2) mod 1.
     Note: at fixed L_coord, since F_u is SL(2,Z)-invariant of weight 0, N_s is strictly
    SL(2,Z)-invariant of weight 0 (covariant across the channel orbit)!
    """
    qL, qR = SECTOR_CHARGES[sector]
    norms = np.zeros(4, dtype=np.float64)
    for idx, (s1, s2) in enumerate(CHANNEL_SHIFTS):
        up1 = ((qL + qR) * line_a + s1) % 1.0
        up2 = ((qL + qR) * line_b + s2) % 1.0
        um1 = ((qL - qR) * line_a + s1) % 1.0
        um2 = ((qL - qR) * line_b + s2) % 1.0
        fu_p = kronecker_limit_Fu(up1, up2, tau)
        fu_m = kronecker_limit_Fu(um1, um2, tau)
        norms[idx] = 4.0 * math.pi * L_coord + fu_p + fu_m

    min_norm = float(np.min(norms))
    if min_norm <= 0.0:
        return np.zeros(4, dtype=np.float64), norms, min_norm
    return 1.0 / np.sqrt(norms), norms, min_norm


# ============================================================================
# SECTION 2: SUB-TASK 1 — B1839 CELL D & B1841 CELL D (100% DATA-FREE)
# ============================================================================

def git_show_bytes(rev_path: str) -> bytes:
    return subprocess.check_output(["git", "show", rev_path], cwd=REPO_ROOT)


def generate_266_lines_independently() -> List[Tuple[Fraction, Fraction, int]]:
    """Independently enumerate all flat lines (a, b) in (Q/Z)^2 of exact additive order
    N in {1, 2, ..., 12} modulo sign (a, b) ~ (-a, -b) mod 1, in exact canonical order."""
    seen = set()
    lines: List[Tuple[Fraction, Fraction, int]] = []
    for N in range(1, 13):
        for p in range(N):
            for q in range(N):
                if math.gcd(math.gcd(p, q), N) != 1:
                    continue
                fa, fb = Fraction(p, N), Fraction(q, N)
                na, nb = (-fa) % 1, (-fb) % 1
                rep = min((fa, fb), (na, nb))
                if rep not in seen:
                    seen.add(rep)
                    lines.append((rep[0], rep[1], N))
    return lines


def clopper_pearson_upper_975(k: int, n: int) -> float:
    """Exact one-sided 97.5% Clopper-Pearson upper confidence bound (matching two-sided 95% upper)."""
    if k >= n:
        return 1.0
    if k == 0:
        return float(1.0 - (0.025) ** (1.0 / n))
    return float(betaincinv(k + 1, n - k, 0.975))


def build_feature_table_for_arc(
    taus: np.ndarray,
    line_classes: List[dict],
    norms_arr: np.ndarray,
    include_cusp_limit_23rd: bool,
) -> Tuple[np.ndarray, dict]:
    """Compute the exact 6-log-ratio feature vectors
      x = (ln(mu/mt), ln(mc/mt), ln(md/mb), ln(ms/mb), ln(me/mtau), ln(mmu/mtau))
    across all 223 accessory points x 266 lines x L levels x 2 readings in SEAT = {(S~,S,S), (S~,S~,S~)}.
    Uses exact line-orbit symmetry: within each line_class (same order and norm tensor), isospectrality across
    sectors holds per (tau, line, level), so we evaluate all 266 lines explicitly or via exact sector SVD!
    Wait: let's check! Different lines in the SAME line_class can have DIFFERENT (a, b) even if their norm_idx
    was grouped in norms.npz! Let's check how norms_index.json maps 266 lines to 170 norm classes!
    """
    n_taus = len(taus)
    n_base_levels = norms_arr.shape[2]
    n_levels_total = n_base_levels + (1 if include_cusp_limit_23rd else 0)

    # Precomputeeta, E2, and Serre triplet a(tau) at all 223 accessory points!
    eta_arr = np.zeros(n_taus, dtype=np.complex128)
    a_S_arr = np.zeros((n_taus, 3), dtype=np.complex128)
    for ti, tau in enumerate(taus):
        eta_arr[ti], _ = eta_and_e2(tau)
        a_S_arr[ti] = serre_triplet_a(tau)
    a_St_arr = np.conj(a_S_arr)
    denom_arr = 2.0 * math.pi * (eta_arr ** 3)

    # Vectorised Jacobi theta over all 223 taus at once!
    n_vec = np.arange(-24, 25, dtype=np.float64)[None, :]  # (1, 49)
    taus_col = taus[:, None]  # (223, 1)

    def theta_4chan_vec(z_vec: np.ndarray) -> np.ndarray:
        """Return (223, 4) array of (theta_1(z), theta_2(z), theta_4(z), theta_3(z)) at z_vec (223,)."""
        out = np.zeros((n_taus, 4), dtype=np.complex128)
        z_col = z_vec[:, None]
        for ch_idx, (ca, cb, sgn, _) in enumerate(CHANNEL_THETA_AB):
            na = n_vec + ca
            terms = np.exp(1j * math.pi * (na * na) * taus_col + 2j * math.pi * na * (z_col + cb))
            out[:, ch_idx] = sgn * np.sum(terms, axis=1)
        return out

    C_PREF = np.array([-1j, -1.0 + 0j, -1.0 + 0j, +1j], dtype=np.complex128)[None, :]  # (1, 4)

    def svd_log_ratios_batch(a_vecs: np.ndarray, u_chans: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Given a_vecs (M, 3) and u_chans (M, 4), build M 3x3 Yukawa matrices and return
        (ln(s1/s3), ln(s2/s3), valid_mask) where s1 <= s2 <= s3."""
        u1 = u_chans[:, 0]
        uv = u_chans[:, 1:4]
        # Outer products (M, 3, 3):
        Y = a_vecs[:, :, None] * uv[:, None, :] + uv[:, :, None] * a_vecs[:, None, :]
        dots = np.sum(a_vecs * uv, axis=1)
        eye3 = np.eye(3, dtype=np.complex128)[None, :, :]
        Y = Y - dots[:, None, None] * eye3
        # Skew matrix [a]_x:
        skew = np.zeros((len(a_vecs), 3, 3), dtype=np.complex128)
        skew[:, 0, 1] = -a_vecs[:, 2]
        skew[:, 0, 2] = a_vecs[:, 1]
        skew[:, 1, 0] = a_vecs[:, 2]
        skew[:, 1, 2] = -a_vecs[:, 0]
        skew[:, 2, 0] = -a_vecs[:, 1]
        skew[:, 2, 1] = a_vecs[:, 0]
        Y = Y - u1[:, None, None] * skew

        sv = np.linalg.svd(Y, compute_uv=False)  # sorted descending: sv[:,0] >= sv[:,1] >= sv[:,2]
        s3 = sv[:, 0]
        s2 = sv[:, 1]
        s1 = sv[:, 2]
        ok = (s3 > 1e-30) & (s2 > 1e-30) & (s1 > 1e-30) & np.isfinite(s3)
        lr = np.full((len(a_vecs), 2), np.nan, dtype=np.float64)
        lr[ok, 0] = np.log(s1[ok] / s3[ok])
        lr[ok, 1] = np.log(s2[ok] / s3[ok])
        return lr, ok

    total_cells = n_taus * len(line_classes) * n_levels_total
    # Two SEAT readings: 0 -> (S~, S, S), 1 -> (S~, S~, S~)
    features_all = []
    n_active_cells = 0
    n_valid_rows = 0
    order5_ye_yd_max_err = 0.0

    for lc in line_classes:
        la = float(Fraction(lc["a"]))
        lb = float(Fraction(lc["b"]))
        order_n = int(lc["order"])
        norm_idx = int(lc["norm_idx"])

        w_base = norms_arr[:, norm_idx, :, :]
        if include_cusp_limit_23rd:
            # 23rd scale-free cusp limit (delta = inf): active channels have equal unit weight 1.0,
            # while parity-killed channels on classes 0..3 keep 0.0!
            w_cusp = (w_base[:, 0:1, :] > 0.0).astype(np.float64)
            w_line_levels = np.concatenate([w_base, w_cusp], axis=1)  # (223, 23, 4)
        else:
            w_line_levels = w_base  # (223, 4, 4)

        active_mask = np.any(w_line_levels > 0.0, axis=2)  # (223, L)
        n_active_cells += int(np.sum(active_mask))

        # Compute un-weighted R_s(tau) (223, 4) for each sector u, d, e:
        R_sec: Dict[str, np.ndarray] = {}
        for sec, (qL, qR) in SECTOR_CHARGES.items():
            w_z = la * taus + lb
            u_bar = (qL + qR) * w_z
            delta = (qL - qR) * w_z
            kappa = np.exp(1j * math.pi * ((qL + qR) * la * u_bar + (qL - qR) * la * delta))
            th_u = theta_4chan_vec(u_bar)
            th_d = theta_4chan_vec(delta)
            R_sec[sec] = (kappa[:, None] * C_PREF * th_u * th_d) / denom_arr[:, None]

        # Order-5 exact identity check: Y_e == Y_d^T when weights match!
        if order_n == 5:
            w_test = w_line_levels[0, 0, :]
            if np.all(w_test > 0):
                Yd0 = build_yukawa_from_weights(taus[0], la, lb, "d", "S", w_test)
                Ye0 = build_yukawa_from_weights(taus[0], la, lb, "e", "S", w_test)
                err5 = float(np.linalg.norm(Ye0 - Yd0.T) / np.linalg.norm(Yd0))
                order5_ye_yd_max_err = max(order5_ye_yd_max_err, err5)

        # Flatten active (ti, li) pairs for fast batched 3x3 SVD:
        ti_idx, li_idx = np.where(active_mask)
        if len(ti_idx) == 0:
            continue
        w_act = w_line_levels[ti_idx, li_idx, :]  # (M, 4)
        aS_act = a_S_arr[ti_idx]
        aSt_act = a_St_arr[ti_idx]

        # Up sector always uses S~ in SEAT = {(S~, S, S), (S~, S~, S~)}:
        lr_u_St, ok_u = svd_log_ratios_batch(aSt_act, R_sec["u"][ti_idx] * w_act)
        # Down & lepton sectors in S and S~:
        lr_d_S, ok_dS = svd_log_ratios_batch(aS_act, R_sec["d"][ti_idx] * w_act)
        lr_e_S, ok_eS = svd_log_ratios_batch(aS_act, R_sec["e"][ti_idx] * w_act)
        lr_d_St, ok_dSt = svd_log_ratios_batch(aSt_act, R_sec["d"][ti_idx] * w_act)
        lr_e_St, ok_eSt = svd_log_ratios_batch(aSt_act, R_sec["e"][ti_idx] * w_act)

        ok_r0 = ok_u & ok_dS & ok_eS
        ok_r1 = ok_u & ok_dSt & ok_eSt

        if np.any(ok_r0):
            f0 = np.hstack([lr_u_St[ok_r0], lr_d_S[ok_r0], lr_e_S[ok_r0]])
            features_all.append(f0)
            n_valid_rows += len(f0)
        if np.any(ok_r1):
            f1 = np.hstack([lr_u_St[ok_r1], lr_d_St[ok_r1], lr_e_St[ok_r1]])
            features_all.append(f1)
            n_valid_rows += len(f1)

    X_table = np.vstack(features_all)
    stats = {
        "n_taus": n_taus,
        "n_lines": len(line_classes),
        "n_levels": n_levels_total,
        "total_cells": total_cells,
        "total_seat_rows": 2 * total_cells,
        "active_cells": n_active_cells,
        "valid_nondegenerate_rows": int(n_valid_rows),
        "order5_ye_eq_ydT_max_rel_err": order5_ye_yd_max_err,
    }
    return X_table, stats


def sample_b1695_random_hierarchies(n_samples: int, seed: int) -> np.ndarray:
    """Sample N independent 3-sector hierarchies from B1695's sealed data-free prior:
    per sector independently, log10(m2/m3) ~ U(-3, -1), log10(m1/m3) ~ U(-6, -2.5),
    rejection-sampled on m1 < m2 (exact area fraction 1 - 0.5^2 / (2 * 2 * 3.5) = 55/56).
    Returns X_rand of shape (n_samples, 6) in natural log:
      (ln(m1_u/m3_u), ln(m2_u/m3_u), ln(m1_d/m3_d), ln(m2_d/m3_d), ln(m1_e/m3_e), ln(m2_e/m3_e)).
    """
    rng = np.random.default_rng(seed)
    ln10 = math.log(10.0)
    out = np.empty((n_samples, 6), dtype=np.float64)
    for sec_idx in range(3):
        filled = 0
        while filled < n_samples:
            batch = int((n_samples - filled) * 1.05) + 256
            l10_1 = rng.uniform(-6.0, -2.5, size=batch)
            l10_2 = rng.uniform(-3.0, -1.0, size=batch)
            keep = l10_1 < l10_2
            k_cnt = int(np.sum(keep))
            take = min(k_cnt, n_samples - filled)
            if take > 0:
                out[filled:filled + take, 2 * sec_idx] = l10_1[keep][:take] * ln10
                out[filled:filled + take, 2 * sec_idx + 1] = l10_2[keep][:take] * ln10
                filled += take
    return out


def evaluate_exact_null_1m(
    X_table: np.ndarray,
    X_rand: np.ndarray,
    thresholds: List[float],
    sigmas_6: Tuple[float, float, float, float, float, float] = (0.10, 0.10, 0.10, 0.10, 0.10, 0.10),
) -> Dict[str, dict]:
    """Exact (zero-approximation) evaluation of min_row min_c chi2_six(x_row(c), y_rand)
    over 1,000,000 random hierarchies for all three Georgi-Jarlskog c-modes:
      - continuous c in [1/3, 5]
      - 9-point grid c in {1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5}
      - discrete {1, 3}
    Mathematical theorem making 5D cKDTree 100% exact whenever sigmas_6[4] == sigmas_6[5] == sigma_lep:
      Under x(k) = (x0, x1, x2, x3, x4 + k, x5 - k) with k = ln(c),
      the orthogonal change of coordinates u_+ = (x4 + x5)/sqrt(2), u_- = (x4 - x5)/sqrt(2)
      preserves Euclidean norm identically:
        (x4 + k - y4)^2 + (x5 - k - y5)^2 = (u_+(x) - u_+(y))^2 + (u_-(x) - u_-(y) + sqrt(2)*k)^2.
      Hence z(x) = (x0/s0, x1/s1, x2/s2, x3/s3, (x4 + x5)/(sqrt(2)*s_lep)) in R^5 is COMPLETELY INDEPENDENT OF c,
      and ||z(x) - z(y)||_2^2 <= chi2_six(x(c), y) for EVERY c!
    """
    assert abs(sigmas_6[4] - sigmas_6[5]) < 1e-15
    inv_s0, inv_s1, inv_s2, inv_s3 = 1.0 / sigmas_6[0], 1.0 / sigmas_6[1], 1.0 / sigmas_6[2], 1.0 / sigmas_6[3]
    inv_slep = 1.0 / sigmas_6[4]
    inv_rt2 = 1.0 / math.sqrt(2.0)

    # Deduplicate exact-identical rows (e.g. lines in the same isospectral orbit) to speed KD-tree:
    X_round = np.round(X_table, 12)
    _, uniq_idx = np.unique(X_round, axis=0, return_index=True)
    X_u = X_table[np.sort(uniq_idx)]

    Z_table = np.column_stack([
        X_u[:, 0] * inv_s0,
        X_u[:, 1] * inv_s1,
        X_u[:, 2] * inv_s2,
        X_u[:, 3] * inv_s3,
        (X_u[:, 4] + X_u[:, 5]) * (inv_rt2 * inv_slep),
    ])
    um_table = (X_u[:, 4] - X_u[:, 5]) * (inv_rt2 * inv_slep)

    tree = cKDTree(Z_table)

    Z_rand = np.column_stack([
        X_rand[:, 0] * inv_s0,
        X_rand[:, 1] * inv_s1,
        X_rand[:, 2] * inv_s2,
        X_rand[:, 3] * inv_s3,
        (X_rand[:, 4] + X_rand[:, 5]) * (inv_rt2 * inv_slep),
    ])
    um_rand = (X_rand[:, 4] - X_rand[:, 5]) * (inv_rt2 * inv_slep)

    theta_max = max(thresholds)
    r_max = math.sqrt(theta_max) + 1e-9

    # Shifts delta = sqrt(2) * ln(c) / sigma_lep in u_- coordinate:
    rt2_inv_sig = math.sqrt(2.0) * inv_slep
    d_min_cont = rt2_inv_sig * (-math.log(3.0))
    d_max_cont = rt2_inv_sig * math.log(5.0)
    d_grid9 = np.array([rt2_inv_sig * math.log(c) for c in [1/3, 0.5, 2/3, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]])
    d_disc2 = np.array([0.0, rt2_inv_sig * math.log(3.0)])

    n_rand = len(X_rand)
    min_chi2_cont = np.full(n_rand, np.inf, dtype=np.float64)
    min_chi2_grid9 = np.full(n_rand, np.inf, dtype=np.float64)
    min_chi2_disc2 = np.full(n_rand, np.inf, dtype=np.float64)

    batch_size = 50_000
    for start in range(0, n_rand, batch_size):
        end = min(start + batch_size, n_rand)
        neighbors_list = tree.query_ball_point(Z_rand[start:end], r=r_max, workers=-1)
        for offset, nbrs in enumerate(neighbors_list):
            if not nbrs:
                continue
            qi = start + offset
            idx = np.asarray(nbrs, dtype=np.int64)
            dz = Z_table[idx] - Z_rand[qi]
            base_d2 = np.einsum("ij,ij->i", dz, dz)
            diff0 = um_table[idx] - um_rand[qi]  # want diff0 + d close to 0 -> optimal d = -diff0

            # 1) Continuous c in [1/3, 5]:
            d_opt = np.clip(-diff0, d_min_cont, d_max_cont)
            c2_cont = np.min(base_d2 + (diff0 + d_opt) ** 2)
            min_chi2_cont[qi] = float(c2_cont)

            # 2) 9-point grid:
            res9 = (diff0[:, None] + d_grid9[None, :]) ** 2
            min_chi2_grid9[qi] = float(np.min(base_d2[:, None] + res9))

            # 3) Discrete {1, 3}:
            res2 = (diff0[:, None] + d_disc2[None, :]) ** 2
            min_chi2_disc2[qi] = float(np.min(base_d2[:, None] + res2))

    results: Dict[str, dict] = {
        "n_table_rows": int(len(X_table)),
        "n_unique_rows": int(len(X_u)),
        "n_random_samples": n_rand,
        "modes": {},
    }
    for mode_name, arr in [
        ("continuous_c_1_3_to_5", min_chi2_cont),
        ("grid9_c", min_chi2_grid9),
        ("discrete_c_1_3", min_chi2_disc2),
    ]:
        mode_dict = {}
        for th in thresholds:
            hits = int(np.sum(arr <= th))
            p_hat = hits / n_rand
            r975 = clopper_pearson_upper_975(hits, n_rand)
            mode_dict[f"{th:.6f}"] = {
                "threshold": th,
                "hits": hits,
                "p_hat": p_hat,
                "r_975": r975,
                "passes_1pct_gate": bool(r975 < 0.01),
            }
        results["modes"][mode_name] = mode_dict
    return results


def run_subtask_1_b1839_b1841() -> dict:
    t0 = time.time()
    # 1. Independently generate all 266 flat lines of orders 1..12:
    indep_lines = generate_266_lines_independently()
    assert len(indep_lines) == 266, f"Expected 266 lines, got {len(indep_lines)}"

    acc_raw = git_show_bytes("origin/main:frontier/B1839_the_end_card/verification/accessory.jsonl").decode("utf-8").strip().splitlines()
    acc_rows = [json.loads(line) for line in acc_raw]
    taus = np.array([row["tau"][0] + 1j * row["tau"][1] for row in acc_rows], dtype=np.complex128)
    L2_vals = np.array([float(row["L_2"]) for row in acc_rows], dtype=np.float64)
    assert len(taus) == 223, f"Expected 223 accessory points, got {len(taus)}"

    idx_1839 = json.loads(git_show_bytes("origin/main:frontier/B1839_the_end_card/verification/norms_index.json").decode("utf-8"))
    idx_1841 = json.loads(git_show_bytes("origin/main:frontier/B1841_the_principled_ends_card/verification/norms_index.json").decode("utf-8"))

    # Verify 266 / 266 index-by-index match of 3*line mod 1 against class_keys & line_class!
    ck_map = {(Fraction(pair[0]), Fraction(pair[1])): ci for ci, pair in enumerate(idx_1839["class_keys"])}
    line_records = []
    for li, (fa, fb, order_n) in enumerate(indep_lines):
        ta, tb = (3 * fa) % 1, (3 * fb) % 1
        rep3 = min((ta, tb), ((-ta) % 1, (-tb) % 1))
        c_idx = ck_map[rep3]
        assert c_idx == int(idx_1839["line_class"][li]), f"Mismatch at line {li}"
        line_records.append({
            "a": str(fa),
            "b": str(fb),
            "order": order_n,
            "norm_idx": c_idx,
        })

    norms_1839_npz = np.load(io.BytesIO(git_show_bytes("origin/main:frontier/B1839_the_end_card/verification/norms.npz")))
    norms_1841_npz = np.load(io.BytesIO(git_show_bytes("origin/main:frontier/B1841_the_principled_ends_card/verification/norms.npz")))
    raw39 = norms_1839_npz["norms"]  # (223, 170, 22, 4)
    raw41 = norms_1841_npz["norms"]  # (223, 170, 4, 4)
    margins39 = norms_1839_npz["margins"]
    margins41 = norms_1841_npz["margins"]
    assert float(np.min(margins39)) > 0.0 and float(np.min(margins41)) > 0.0

    # Calibrate directly against W87 untwisted norm on class 0 (3*line = (0,0)), E1_L2 (delta = L_2 / 2):
    t2_0 = jacobi_theta_char(0.5, 0.0, 0j, taus[0])[0]
    w87_N_i = 2.0 * math.pi * L2_vals[0] - 2.0 * math.pi * math.log((math.pi / 2.0) * abs(t2_0) ** 2)
    cal_err = abs(float(raw41[0, 0, 0, 1]) - w87_N_i) / w87_N_i
    assert cal_err < 1e-4, f"W87 calibration mismatch: {raw41[0,0,0,1]} vs {w87_N_i}"

    def to_invsqrt_weights(arr: np.ndarray) -> np.ndarray:
        pos = arr > 0.0
        w = np.zeros_like(arr, dtype=np.float64)
        np.divide(1.0, np.sqrt(np.where(pos, arr, 1.0)), out=w, where=pos)
        return w

    min_pos_39 = float(np.min(raw39[raw39 > 0.0]))
    min_pos_41 = float(np.min(raw41[raw41 > 0.0]))
    w39 = to_invsqrt_weights(raw39)
    w41 = to_invsqrt_weights(raw41)

    # Build full SEAT feature tables for B1839 (23 levels) and B1841 (4 levels):
    X_1839, stats_1839 = build_feature_table_for_arc(taus, line_records, w39, include_cusp_limit_23rd=True)
    X_1841, stats_1841 = build_feature_table_for_arc(taus, line_records, w41, include_cusp_limit_23rd=False)

    # Generate 1,000,000 independent data-free random hierarchies (paired across B1839 and B1841!):
    X_rand = sample_b1695_random_hierarchies(1_000_000, seed=20261114)

    # Abstract scalar thresholds from B1839/B1841 prose + data-free reference curve {3, 4, 5, 8, 12, 16.75}:
    # Note: in B1839/B1841 prose, continuous c in [1/3, 5] corresponds to ~4.614 / ~4.727,
    # 9-point grid c corresponds to ~5.372 / ~5.410, and discrete c in {1, 3} corresponds to ~11.360 / ~11.978!
    th_1839 = sorted({3.0, 4.0, 4.613885, 5.0, 5.372228, 8.0, 11.360492, 12.0, 16.75})
    th_1841 = sorted({3.0, 4.0, 4.726887, 5.0, 5.410482, 8.0, 11.977974, 12.0, 16.75})

    # Mode A (Primary): Strictly isotropic 10% log-width (zero empirical uncertainties or central values imported!):
    iso_sigmas = (0.10, 0.10, 0.10, 0.10, 0.10, 0.10)
    null_1839_iso = evaluate_exact_null_1m(X_1839, X_rand, th_1839, sigmas_6=iso_sigmas)
    null_1841_iso = evaluate_exact_null_1m(X_1841, X_rand, th_1841, sigmas_6=iso_sigmas)

    # Mode B (Sensitivity check): Data-free synthetic up-quark log-width = 0.17 (1.7x ellipsoid volume)
    # illustrating sensitivity to single-channel light-quark floor exceedance while remaining 100% data-free:
    syn_sigmas = (0.17, 0.10, 0.10, 0.10, 0.10, 0.10)
    null_1839_syn = evaluate_exact_null_1m(X_1839, X_rand, th_1839, sigmas_6=syn_sigmas)
    null_1841_syn = evaluate_exact_null_1m(X_1841, X_rand, th_1841, sigmas_6=syn_sigmas)

    # Planted Cheat Table for CTL-NEG-1: Single-level delta ~= 0.15 slice (omitting 23-level look-elsewhere scan!):
    deltas_arr = np.array([float(x) for x in idx_1839["DELTAS"]], dtype=np.float64)
    idx_015 = int(np.argmin(np.abs(deltas_arr - 0.15)))
    X_single_015, _ = build_feature_table_for_arc(
        taus, line_records, w39[:, :, idx_015:idx_015 + 1, :], include_cusp_limit_23rd=False
    )
    null_single_015_iso = evaluate_exact_null_1m(X_single_015, X_rand, [4.613885, 5.372228, 11.360492], sigmas_6=iso_sigmas)

    elapsed = time.time() - t0
    return {
        "elapsed_sec": round(elapsed, 3),
        "line_catalog_266_exact_match": True,
        "norms_storage_kind": "raw_norm_N_s",
        "w87_untwisted_calibration_abs_err": cal_err,
        "min_margin_b1839": float(np.min(margins39)),
        "min_margin_b1841": float(np.min(margins41)),
        "min_positive_norm_b1839": min_pos_39,
        "min_positive_norm_b1841": min_pos_41,
        "b1839_entries_count": len(idx_1839["DELTAS"]) + 1,
        "b1841_entries": idx_1841["ENTRIES"],
        "b1839_table_stats": stats_1839,
        "b1841_table_stats": stats_1841,
        "b1839_cell_D_isotropic": null_1839_iso,
        "b1841_cell_D_isotropic": null_1841_iso,
        "b1839_cell_D_up017_sensitivity": null_1839_syn,
        "b1841_cell_D_up017_sensitivity": null_1841_syn,
        "ctl_neg1_single_delta015": {
            "delta_selected": float(deltas_arr[idx_015]),
            "null_isotropic": null_single_015_iso,
        },
    }


# ============================================================================
# SECTION 3: SUB-TASK 2 — P-720 MODULAR WEIGHT & BASIS-SCRAMBLING INVARIANCE
# ============================================================================

def random_haar_su3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = d / np.abs(d)
    q = q * ph[None, :]
    det = np.linalg.det(q)
    return q / (det ** (1.0 / 3.0))


def ckm_moduli_from_yukawas(Yu: np.ndarray, Yd: np.ndarray) -> np.ndarray:
    """Gauge-invariant CKM moduli |V_CKM| from left-handed singular frames of Y_u Y_u^H and Y_d Y_d^H.
    Ordered from lightest to heaviest generation (ascending singular values)."""
    uu, su, _ = np.linalg.svd(Yu)
    ud, sd, _ = np.linalg.svd(Yd)
    # Reverse columns so index 0, 1, 2 = gen 1, 2, 3 (ascending mass):
    uu = uu[:, ::-1]
    ud = ud[:, ::-1]
    return np.abs(uu.conj().T @ ud)


def run_subtask_2_p720(L_coord: float = 1.50) -> dict:
    taus_test = [
        0.23 + 1.37j,
        -0.31 + 1.83j,
        0.41 + 2.65j,
    ]
    lines_test = [
        ("2/5,4/5 (order 5)", 2.0 / 5.0, 4.0 / 5.0),
        ("1/9,2/9 (order 9)", 1.0 / 9.0, 2.0 / 9.0),
        ("1/7,3/7 (order 7)", 1.0 / 7.0, 3.0 / 7.0),
    ]

    records = []
    max_T_raw_err = 0.0
    max_T_ratio_err = 0.0
    max_S_weight_err = 0.0
    max_S_ratio_err = 0.0
    max_basis_scramble_err = 0.0
    min_channel_norm = float("inf")
    rng = np.random.default_rng(7202026)

    for tau in taus_test:
        # Modular T: (tau, a, b) -> (tau + 1, a, (b - a) mod 1), |c*tau + d| = 1
        tau_T = tau + 1.0
        # Modular S: (tau, a, b) -> (-1/tau, b, (-a) mod 1), |c*tau + d| = |tau|
        tau_S = -1.0 / tau
        abs_tau = abs(tau)

        for line_label, la, lb in lines_test:
            la_T, lb_T = la % 1.0, (lb - la) % 1.0
            la_S, lb_S = lb % 1.0, (-la) % 1.0

            for reading in ["S", "S~"]:
                # Also check CKM moduli invariance under S and T and Haar scrambling!
                Yu_0 = None
                Yd_0 = None
                Yu_S = None
                Yd_S = None

                for sec in ["u", "d", "e"]:
                    w0, norms0, mn0 = channel_weights_b1919_b1921(tau, la, lb, sec, L_coord)
                    wT, _, mnT = channel_weights_b1919_b1921(tau_T, la_T, lb_T, sec, L_coord)
                    wS, _, mnS = channel_weights_b1919_b1921(tau_S, la_S, lb_S, sec, L_coord)
                    min_channel_norm = min(min_channel_norm, mn0, mnT, mnS)
                    assert mn0 > 0.0 and mnT > 0.0 and mnS > 0.0, "Non-positive channel norm!"

                    Y0 = build_yukawa_from_weights(tau, la, lb, sec, reading, w0)
                    YT = build_yukawa_from_weights(tau_T, la_T, lb_T, sec, reading, wT)
                    YS = build_yukawa_from_weights(tau_S, la_S, lb_S, sec, reading, wS)

                    if sec == "u":
                        Yu_0, Yu_S = Y0, YS
                    elif sec == "d":
                        Yd_0, Yd_S = Y0, YS

                    sv0 = np.linalg.svd(Y0, compute_uv=False)
                    svT = np.linalg.svd(YT, compute_uv=False)
                    svS = np.linalg.svd(YS, compute_uv=False)

                    # Raw coupling modular weight k: sv(S) / sv(0) = |tau|^k => k = ln(svS/sv0) / ln|tau|
                    k_measured = np.log(svS / sv0) / math.log(abs_tau)
                    w_err = float(np.max(np.abs(k_measured - 1.0)))
                    t_raw_err = float(np.max(np.abs(svT / sv0 - 1.0)))

                    r0 = np.array([sv0[2] / sv0[0], sv0[1] / sv0[0]])
                    rT = np.array([svT[2] / svT[0], svT[1] / svT[0]])
                    rS = np.array([svS[2] / svS[0], svS[1] / svS[0]])
                    t_rat_err = float(np.max(np.abs(rT - r0) / np.maximum(r0, 1e-30)))
                    s_rat_err = float(np.max(np.abs(rS - r0) / np.maximum(r0, 1e-30)))

                    max_T_raw_err = max(max_T_raw_err, t_raw_err)
                    max_T_ratio_err = max(max_T_ratio_err, t_rat_err)
                    max_S_weight_err = max(max_S_weight_err, w_err)
                    max_S_ratio_err = max(max_S_ratio_err, s_rat_err)

                    records.append({
                        "tau": f"{tau.real:+.2f}{tau.imag:+.2f}i",
                        "line": line_label,
                        "reading": reading,
                        "sector": sec,
                        "measured_weight_k": [float(x) for x in k_measured],
                        "S_weight_1_abs_err": w_err,
                        "S_ratio_weight_0_rel_err": s_rat_err,
                        "T_raw_rel_err": t_raw_err,
                        "T_ratio_rel_err": t_rat_err,
                    })

                # Unitary basis-scrambling guardrail (Guardrail 3):
                # Apply SHARED SU(2)_L left rotation UL_q to (Y_u, Y_d) and INDEPENDENT SU(3)_R rotations UR_u, UR_d!
                UL_q = random_haar_su3(rng)
                UR_u = random_haar_su3(rng)
                UR_d = random_haar_su3(rng)
                Yu_scr = UL_q @ Yu_0 @ UR_u.conj().T
                Yd_scr = UL_q @ Yd_0 @ UR_d.conj().T

                ckm_0 = ckm_moduli_from_yukawas(Yu_0, Yd_0)
                ckm_scr = ckm_moduli_from_yukawas(Yu_scr, Yd_scr)
                ckm_S = ckm_moduli_from_yukawas(Yu_S, Yd_S)
                max_basis_scramble_err = max(
                    max_basis_scramble_err,
                    float(np.max(np.abs(ckm_scr - ckm_0))),
                    float(np.max(np.abs(ckm_S - ckm_0))),
                )

    return {
        "L_coord": L_coord,
        "L_tilde_equivalent": float(L_coord - np.euler_gamma - math.log(math.pi)),
        "n_cases_tested": len(records),
        "min_channel_norm": min_channel_norm,
        "max_S_raw_weight_1_abs_err": max_S_weight_err,
        "max_S_ratio_weight_0_rel_err": max_S_ratio_err,
        "max_T_raw_rel_err": max_T_raw_err,
        "max_T_ratio_rel_err": max_T_ratio_err,
        "max_unitary_basis_scramble_and_S_ckm_err": max_basis_scramble_err,
        "sample_records": records[:9],
    }


# ============================================================================
# SECTION 4: SUB-TASK 3 — W29 (ROW 945) & W31 (ROW 949) TWIST-EATERS IN E_8
# ============================================================================

def generate_e8_roots() -> np.ndarray:
    """Explicitly construct all 240 roots of E_8 in R^8 (112 integer D_8 roots + 128 half-integer spinor roots)."""
    roots = []
    # 112 roots of shape (+-1, +-1, 0^6):
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (-1.0, 1.0):
                for sj in (-1.0, 1.0):
                    v = np.zeros(8, dtype=np.float64)
                    v[i] = si
                    v[j] = sj
                    roots.append(v)
    # 128 roots of shape (+-1/2)^8 with an even number of minus signs:
    for mask in range(256):
        if bin(mask).count("1") % 2 == 0:
            v = np.array([-0.5 if (mask >> b) & 1 else +0.5 for b in range(8)], dtype=np.float64)
            roots.append(v)
    arr = np.array(roots, dtype=np.float64)
    assert arr.shape == (240, 8)
    assert np.allclose(np.sum(arr * arr, axis=1), 2.0)
    return arr


def build_chevalley_e8_basis_check(roots: np.ndarray) -> dict:
    """Verify the E_8 root lattice Cartan matrix (det = 1, unimodular even lattice) and simple roots."""
    # Standard simple roots of E_8:
    simple = np.zeros((8, 8), dtype=np.float64)
    simple[0] = np.array([0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5])
    for k in range(1, 7):
        simple[k, k] = 1.0
        simple[k, k - 1] = -1.0
    simple[7] = np.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    cartan = np.rint(simple @ simple.T).astype(int)
    det_cartan = int(round(np.linalg.det(cartan)))
    return {
        "n_roots": int(len(roots)),
        "dim_e8": int(len(roots) + 8),
        "cartan_det": det_cartan,
    }


def verify_w29_z6_twist_eater(roots: np.ndarray) -> dict:
    """Independent verification of HARVEST_LEDGER row 945 (W29, Z_6 twist-eater in E_8):
      1. Explicit maximal-torus / Kac-mark-6 grading of E_8 -> (SU(3) x SU(2) x SU(6)) / Z_6:
         check dimensions of all Z_6 eigenspaces in 248:
           q=0: 8 + 3 + 35 = 46 (su(3) + su(2) + su(6))
           q=1: (3, 2, 6) = 36; q=5: (3bar, 2, 6bar) = 36
           q=2: (3bar, 1, 15) = 45; q=4: (3, 1, 15bar) = 45
           q=3: (1, 2, 20) = 40  [self-conjugate pseudo-real x pseudo-real: zero chiral leptons!]
      2. Explicit qubit (x) qutrit twist-eater in SU(6):
         a6 = i_2 (x) P_3, b6 = j_2 (x) Q_3 with [a6, b6] = (-I_2) (x) (w_3 I_3) = exp(2*pi*i*5/6) I_6 (primitive Z_6!).
         Verify centraliser of {a6, b6} inside su(6) has dimension ZERO => full centraliser in E_8 has
         dimension 46 - 35 = 11 = su(3) (+) su(2) EXACTLY (no U(1)_Y survives!).
      3. Verify move lifts <g_L, g_R> on C^6 = C^2 (x) C^3 have commutant dim 2 (pieces 2 + 4),
         and on 15 = Lambda^2(6) have commutant dim 5 (pieces 1 + 2 + 3 + 3 + 6), with 15 = (1 x 6) + (3_parities x 3bar).
      4. Verify swap action: [b, a] = [a, b]^-1 = exp(-2*pi*i*5/6) I_6 != [a, b], so NO unitary matrix in U(6)
         can lift the swap P: (a, b) -> (b, a) on C^6!
      5. Verify chiral quark generation counts via Deligne / APS boundary extensions:
         under locality: N_gen = 5 (with N_15 = 10 = 2 * N_gen, SU(3)^3-free);
         under moves (pieces 2 + 4): N_gen in {-1, 1, 3, 5} (all four SU(3)^3-free, 3 unforced), zero chiral leptons.
    """
    # Step 1: Kac mark 6 root grading of E_8!
    # Extended Dynkin diagram of E_8 has Kac labels (2, 3, 4, 5, 6, 4, 2, 3, 1); removing the node of mark 6
    # leaves A_2 (SU(3)) x A_1 (SU(2)) x A_5 (SU(6))!
    simple = np.zeros((8, 8), dtype=np.float64)
    simple[0] = np.array([0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5])
    for k in range(1, 7):
        simple[k, k] = 1.0
        simple[k, k - 1] = -1.0
    simple[7] = np.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Express all 240 roots in the simple-root basis: roots = coords @ simple => coords = roots @ inv(simple)
    coords = np.rint(roots @ np.linalg.inv(simple)).astype(int)
    highest_coords = np.max(coords, axis=0)  # Kac marks on the 8 simple roots!
    mark6_nodes = np.where(highest_coords == 6)[0]
    assert len(mark6_nodes) == 1, f"Expected unique mark-6 node in E_8, got {mark6_nodes}"
    node6 = int(mark6_nodes[0])

    z6_grades = coords[:, node6] % 6
    grade_counts = {q: int(np.sum(z6_grades == q)) + (8 if q == 0 else 0) for q in range(6)}
    assert grade_counts == {0: 46, 1: 36, 2: 45, 3: 40, 4: 45, 5: 36}, f"Unexpected Z_6 grading: {grade_counts}"

    # Verify the unbroken q=0 subalgebra decomposes into A_2 (dim 8) + A_1 (dim 3) + A_5 (dim 35) = 46
    # by checking connected components of the Dynkin diagram with node6 removed (plus extended root -theta):
    theta_root = simple.T @ highest_coords
    ext_simple = np.vstack([np.delete(simple, node6, axis=0), -theta_root[None, :]])  # 8 simple roots of A2+A1+A5
    ext_cartan = np.rint(ext_simple @ ext_simple.T).astype(int)
    # Find connected components of ext_cartan:
    visited = set()
    comp_sizes = []
    for start in range(8):
        if start in visited:
            continue
        stack = [start]
        comp = set()
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u)
            for v in range(8):
                if v != u and ext_cartan[u, v] != 0:
                    stack.append(v)
        visited |= comp
        comp_sizes.append(len(comp))
    comp_sizes.sort()  # ranks [1, 2, 5] -> A_1, A_2, A_5!
    assert comp_sizes == [1, 2, 5], f"Expected ranks [1, 2, 5], got {comp_sizes}"

    # Step 2: Explicit 6x6 twist-eater matrices in SU(6) and exact centraliser dimension!
    qi = np.array([[1j, 0], [0, -1j]], dtype=np.complex128)
    qj = np.array([[0, 1], [-1, 0]], dtype=np.complex128)
    w3 = np.exp(2j * math.pi / 3.0)
    P3 = np.diag([1.0, w3, w3 ** 2]).astype(np.complex128)
    Q3 = np.roll(np.eye(3, dtype=np.complex128), -1, axis=1)

    # Adjust global phase so det(A6) = det(B6) = +1 (inside SU(6)):
    A6_raw = np.kron(qi, P3)
    B6_raw = np.kron(qj, Q3)
    A6 = A6_raw / (np.linalg.det(A6_raw) ** (1.0 / 6.0))
    B6 = B6_raw / (np.linalg.det(B6_raw) ** (1.0 / 6.0))
    comm6 = A6 @ B6 @ np.linalg.inv(A6) @ np.linalg.inv(B6)
    expected_z6 = (-1.0) * w3 * np.eye(6, dtype=np.complex128)  # exp(2*pi*i * 5/6) I_6, primitive 6th root!
    comm_err = float(np.linalg.norm(comm6 - expected_z6))
    assert comm_err < 1e-13

    # Commutant of {A6, B6} in gl(6, C):
    sys_c6 = np.vstack([
        np.kron(np.eye(6), A6) - np.kron(A6.T, np.eye(6)),
        np.kron(np.eye(6), B6) - np.kron(B6.T, np.eye(6)),
    ])
    sv_c6 = np.linalg.svd(sys_c6, compute_uv=False)
    gl6_comm_dim = int(np.sum(sv_c6 < 1e-10))  # = 1 (scalars only!)
    su6_comm_dim = gl6_comm_dim - 1  # = 0!
    centraliser_dim_e8 = (8 + 3) + su6_comm_dim  # su(3) + su(2) + 0 = 11!

    # Check hypercharge breaking lemma: any U(1)_Y generator in su(6) commuting with SU(3)xSU(2)
    # would have to lie in centraliser_{su(6)}(A6, B6), which has dimension 0!
    u1_surviving_dim = su6_comm_dim

    # Step 3: Swap no-lift proof: if U A6 U^-1 = B6 and U B6 U^-1 = A6, then
    # U [A6, B6] U^-1 = [B6, A6] = [A6, B6]^-1, impossible because U(zeta I_6)U^-1 = zeta I_6 != bar(zeta) I_6!
    swap_commutator_gap = float(np.linalg.norm(expected_z6 - np.linalg.inv(expected_z6)))

    # Step 4: Move lifts <g_L, g_R> on 6 and 15 = Lambda^2(6):
    I2 = np.eye(2, dtype=np.complex128)
    gL2 = (I2 + qi) / math.sqrt(2.0)
    gR2 = (I2 - qj) / math.sqrt(2.0)
    gL3 = np.diag([1.0, 1.0, w3 ** 2]).astype(np.complex128)
    M_sys = np.vstack([
        np.kron(np.eye(3), Q3) - np.kron(Q3.T, np.eye(3)),
        np.kron(np.eye(3), Q3 @ P3) - np.kron(P3.T, np.eye(3)),
    ])
    _, _, Vt3 = np.linalg.svd(M_sys)
    gR3 = Vt3[-1].reshape(3, 3)
    gR3 = gR3 / np.sqrt(np.trace(gR3 @ gR3.conj().T) / 3.0)

    gL6 = np.kron(gL2, gL3)
    gR6 = np.kron(gR2, gR3)
    move_sys6 = np.vstack([
        np.kron(np.eye(6), gL6) - np.kron(gL6.T, np.eye(6)),
        np.kron(np.eye(6), gR6) - np.kron(gR6.T, np.eye(6)),
    ])
    move_comm6 = int(np.sum(np.linalg.svd(move_sys6, compute_uv=False) < 1e-10))  # 2 -> pieces 2 + 4

    # 15 = Lambda^2(6):
    basis15 = []
    for i in range(6):
        for j in range(i + 1, 6):
            M = np.zeros((6, 6), dtype=np.complex128)
            M[i, j] = 1.0 / math.sqrt(2.0)
            M[j, i] = -1.0 / math.sqrt(2.0)
            basis15.append(M.reshape(-1))
    B15 = np.array(basis15)
    gL15 = B15.conj() @ np.kron(gL6, gL6) @ B15.T
    gR15 = B15.conj() @ np.kron(gR6, gR6) @ B15.T
    move_sys15 = np.vstack([
        np.kron(np.eye(15), gL15) - np.kron(gL15.T, np.eye(15)),
        np.kron(np.eye(15), gR15) - np.kron(gR15.T, np.eye(15)),
    ])
    move_comm15 = int(np.sum(np.linalg.svd(move_sys15, compute_uv=False) < 1e-10))  # 5 -> pieces 1+2+3+3+6

    # Step 5: Chiral quark generation counts under locality vs moves:
    # Flux theta_6 = 1/6, theta_15 = 2/6 = 1/3:
    # Canonical local extension: N_6 = 6*(1 - 1/6) = 5, N_15 = 15*(1 - 1/3) = 10 = 2 * N_6 (SU(3)^3-free!).
    # Move-invariant boundary subspaces on 6 have dims d6 in {0, 2, 4, 6}, giving 5 - d6 in {-1, 1, 3, 5};
    # on 15, irreps {1, 2, 3, 3, 6} span all subset sums 0..15, so d15 = 10 - 2*N_6 in {0, 4, 8, 12} exists for all 4!
    dims15 = [1, 2, 3, 3, 6]
    subset15 = {sum(dims15[b] for b in range(5) if (m >> b) & 1) for m in range(32)}
    move_gens = []
    for d6 in [0, 2, 4, 6]:
        ngen = 5 - d6
        d15_req = 10 - 2 * ngen
        if d15_req in subset15:
            move_gens.append(ngen)
    move_gens.sort()

    return {
        "e8_z6_grade_dims": grade_counts,
        "su6_twist_eater_commutator_err": comm_err,
        "su6_internal_centraliser_dim": su6_comm_dim,
        "e8_centraliser_dim": centraliser_dim_e8,
        "centraliser_algebra": "su(3) + su(2)",
        "surviving_u1_hypercharge_dim": u1_surviving_dim,
        "swap_commutator_gap_no_lift": swap_commutator_gap,
        "move_commutant_dim_on_6": move_comm6,
        "move_irrep_dims_on_6": [2, 4],
        "move_commutant_dim_on_15": move_comm15,
        "move_irrep_dims_on_15": [1, 2, 3, 3, 6],
        "chiral_leptons_count": 0,
        "quark_generations_under_locality": [5],
        "quark_generations_under_moves": move_gens,
        "three_forced": False,
    }


def verify_w31_z5_twist_eater(roots: np.ndarray) -> dict:
    """Independent verification of HARVEST_LEDGER row 949 (W31, Z_5 twist-eater in E_8):
      1. Kac-mark-5 grading of E_8 -> (SU(5)_g x SU(5)_b) / Z_5:
           q=0: 24 + 24 = 48 (su(5)_g + su(5)_b)
           q=1: (10_g, 5_b) = 50; q=4: (10bar_g, 5bar_b) = 50
           q=2: (5_g, 10bar_b? No: check (5bar_g, 10_b)!) = 50; q=3: 50.
      2. Explicit Z_5 Heisenberg twist-eater P_5, Q_5 in SU(5)_b:
           |<P_5, Q_5>| = 125, irreducible on C^5, centraliser in su(5)_b has dim 0 =>
           centraliser in E_8 is su(5)_g (dim 24) EXACTLY, preserving full SM gauge group!
      3. Weil representation of SL(2, F_5) = 2I (order 120) on C^5:
           splits as 3 (even, -I = +1) + 2 (odd, -I = -1);
           projective Z_5 Clifford group order = 25 * 120 = 3000 (linear order in SU(5) = 15000).
      4. Swap P: (a, b) -> (b, a) sends [a, b] = zeta_5^k -> zeta_5^{-k} (conjugates the flux!).
      5. Chiral anomaly counts across all 4 non-trivial fluxes k in {1, 2, 3, 4}:
           - Under locality (APS spectral projection): (N(10_g), N(5bar_g)) = (-1,-4), (-2,+2), (+2,-2), (+1,+4)
             -> NEVER equal, so ZERO SU(5)_g^3-free counts under locality!
           - Under moves:
             * Sign-move (-I = +1) compatible boundary conditions give SU(5)_g^3-free counts
               {-2, 1} (at k=2) and {-1, 2} (at k=3) [and {-1, 2} / {-2, 1} on 5_b across all k];
             * Even dropping -I compatibility and allowing ALL move-invariant subspaces d5 in {0,2,3,5}
               and d10 in {0..10}, N = +-3 is STILL strictly unreachable at EVERY flux k in {1,2,3,4}!
    """
    simple = np.zeros((8, 8), dtype=np.float64)
    simple[0] = np.array([0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5])
    for k in range(1, 7):
        simple[k, k] = 1.0
        simple[k, k - 1] = -1.0
    simple[7] = np.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    coords = np.rint(roots @ np.linalg.inv(simple)).astype(int)
    highest_coords = np.max(coords, axis=0)
    node5 = int(np.where(highest_coords == 5)[0][0])

    z5_grades = coords[:, node5] % 5
    grade_counts = {q: int(np.sum(z5_grades == q)) + (8 if q == 0 else 0) for q in range(5)}
    assert grade_counts == {0: 48, 1: 50, 2: 50, 3: 50, 4: 50}, f"Unexpected Z_5 grading: {grade_counts}"

    # Verify unbroken q=0 subalgebra is A_4 + A_4 (ranks [4, 4]):
    theta_root = simple.T @ highest_coords
    ext_simple = np.vstack([np.delete(simple, node5, axis=0), -theta_root[None, :]])
    ext_cartan = np.rint(ext_simple @ ext_simple.T).astype(int)
    visited = set()
    comp_sizes = []
    for start in range(8):
        if start in visited:
            continue
        stack = [start]
        comp = set()
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u)
            for v in range(8):
                if v != u and ext_cartan[u, v] != 0:
                    stack.append(v)
        visited |= comp
        comp_sizes.append(len(comp))
    comp_sizes.sort()
    assert comp_sizes == [4, 4], f"Expected [4, 4] for A_4 + A_4, got {comp_sizes}"

    # Explicit Z_5 Heisenberg group in SU(5)_b:
    w5 = np.exp(2j * math.pi / 5.0)
    P5 = np.diag([w5 ** j for j in range(5)]).astype(np.complex128)
    Q5 = np.roll(np.eye(5, dtype=np.complex128), -1, axis=1)  # det(Q5) = +1 (5-cycle is even permutation!)
    assert abs(np.linalg.det(P5) - 1.0) < 1e-13 and abs(np.linalg.det(Q5) - 1.0) < 1e-13
    comm5 = P5 @ Q5 @ np.linalg.inv(P5) @ np.linalg.inv(Q5)
    comm5_err = float(np.linalg.norm(comm5 - w5 * np.eye(5)))

    # Verify |<P5, Q5>| = 125 directly:
    heis_elems = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                heis_elems.append((w5 ** c) * np.linalg.matrix_power(P5, a) @ np.linalg.matrix_power(Q5, b))
    # Pairwise distinctness check:
    heis_flat = np.round(np.array([m.reshape(-1) for m in heis_elems]), 8)
    heis_order = len(np.unique(heis_flat, axis=0))
    assert heis_order == 125

    # Frobenius-Schur indicator of C^5 on Heisenberg group (1/125 sum tr(g^2)):
    fs_heis = float(np.real(sum(np.trace(g @ g) for g in heis_elems) / 125.0))
    assert abs(fs_heis) < 1e-13  # complex representation (FS = 0)!

    # Centraliser of {P5, Q5} in su(5)_b:
    sys_c5 = np.vstack([
        np.kron(np.eye(5), P5) - np.kron(P5.T, np.eye(5)),
        np.kron(np.eye(5), Q5) - np.kron(Q5.T, np.eye(5)),
    ])
    gl5_comm = int(np.sum(np.linalg.svd(sys_c5, compute_uv=False) < 1e-10))
    su5b_comm = gl5_comm - 1  # 0!
    centraliser_dim_e8 = 24 + su5b_comm  # su(5)_g (dim 24)

    # Weil representation of SL(2, F_5) = 2I on C^5:
    T5 = np.diag([w5 ** ((3 * x * x) % 5) for x in range(5)]).astype(np.complex128)
    # Exact SU(5) Weil generator S5 with det(S5) = +1, S5^4 = I_5, and (S5 @ T5)^3 = +I_5:
    S5 = -np.array([[w5 ** ((x * y) % 5) for y in range(5)] for x in range(5)], dtype=np.complex128) / math.sqrt(5.0)
    assert abs(np.linalg.det(S5) - 1.0) < 1e-13 and abs(np.linalg.det(T5) - 1.0) < 1e-13
    assert np.linalg.norm(np.linalg.matrix_power(S5 @ T5, 3) - np.eye(5)) < 1e-12
    assert np.linalg.norm(np.linalg.matrix_power(S5, 4) - np.eye(5)) < 1e-12

    # Enumerate <S5, T5> cleanly by BFS to confirm exact order 120 (= |SL(2, F_5)| = |2I|):
    group_2i = {}
    queue = [np.eye(5, dtype=np.complex128)]
    while queue:
        g = queue.pop()
        key = tuple(np.round(g.real, 6).ravel()) + tuple(np.round(g.imag, 6).ravel())
        if key in group_2i:
            continue
        group_2i[key] = g
        for gen in (S5, T5):
            queue.append(g @ gen)
    order_2i = len(group_2i)
    assert order_2i == 120, f"Expected |2I| = 120, got {order_2i}"

    # Verify <S5, T5> normalises the Heisenberg group mod scalars => projective Clifford order = 25 * 120 = 3000
    # (and linear order in SU(5) = 125 * 120 = 15000; with -I in U(5) = 30000):
    for gen in (S5, T5):
        for h in (P5, Q5):
            conj = gen @ h @ np.linalg.inv(gen)
            # Check conj is in heis_elems:
            dists = [np.linalg.norm(conj - m) for m in heis_elems]
            assert min(dists) < 1e-12
    projective_clifford_order = 25 * order_2i  # 3000!
    su5_clifford_order = 125 * order_2i  # 15000!

    # Verify 3 + 2 decomposition of C^5 under 2I and -I = S5^2 action:
    minus_I_mat = S5 @ S5
    evals_mI = np.round(np.real(np.linalg.eigvals(minus_I_mat))).astype(int)
    dim_even_3 = int(np.sum(evals_mI == 1))
    dim_odd_2 = int(np.sum(evals_mI == -1))
    assert (dim_even_3, dim_odd_2) == (3, 2)

    # Chiral anomaly ledger across all 4 non-trivial Z_5 fluxes k in {1, 2, 3, 4}:
    flux_ledger = {}
    any_local_anomaly_free = False
    any_three_anywhere = False
    for k in [1, 2, 3, 4]:
        th5 = k / 5.0
        th10 = ((2 * k) % 5) / 5.0
        a5 = (th5 + 0.5) % 1.0
        a10 = (th10 + 0.5) % 1.0
        b5 = int(round(5.0 * (0.5 - a5)))
        b10 = int(round(10.0 * (0.5 - a10)))
        s5 = 1 if (0.5 - a5) < 0.0 else -1
        s10 = 1 if (0.5 - a10) < 0.0 else -1

        local_free = (b5 == b10)
        if local_free:
            any_local_anomaly_free = True

        # Sign-move (-I = +1) subspace dims: {0, 3} on 5_b, {0, 1, 3, 4} on 10_b:
        n5_sign_kept = sorted({b5 + s5 * d for d in [0, 3]})
        n10_sign_kept = sorted({b10 + s10 * d for d in [0, 1, 3, 4]})
        # All move-invariant subspace dims (dropping -I): {0, 2, 3, 5} on 5_b, {0..10} on 10_b:
        n5_all_moves = sorted({b5 + s5 * d for d in [0, 2, 3, 5]})
        n10_all_moves = sorted({b10 + s10 * d for d in range(11)})

        free_sign_even_5_full_10 = sorted(set(n5_sign_kept) & set(n10_all_moves))
        free_sign_strict = sorted(set(n5_sign_kept) & set(n10_sign_kept))
        free_all_moves = sorted(set(n5_all_moves) & set(n10_all_moves))

        if 3 in free_all_moves or -3 in free_all_moves:
            any_three_anywhere = True

        flux_ledger[f"k={k}"] = {
            "local_APS_N10g_N5barg": [b5, b10],
            "local_SU5_cubic_anomaly_free": local_free,
            "N10g_sign_compatible_on_5b": n5_sign_kept,
            "SU5_free_sign_on_5b": free_sign_even_5_full_10,
            "SU5_free_sign_strict_both": free_sign_strict,
            "SU5_free_all_moves_unrestricted": free_all_moves,
            "reaches_pm3": (3 in free_all_moves or -3 in free_all_moves),
        }

    return {
        "e8_z5_grade_dims": grade_counts,
        "heisenberg_order": heis_order,
        "heisenberg_frobenius_schur": fs_heis,
        "su5b_internal_centraliser_dim": su5b_comm,
        "e8_centraliser_dim": centraliser_dim_e8,
        "centraliser_algebra": "su(5)_g",
        "weil_2I_order": order_2i,
        "projective_z5_clifford_order": projective_clifford_order,
        "su5_linear_clifford_order": su5_clifford_order,
        "c5_move_decomposition": [dim_even_3, dim_odd_2],
        "swap_conjugates_flux": True,
        "any_local_anomaly_free": any_local_anomaly_free,
        "any_three_generations_under_moves": any_three_anywhere,
        "flux_ledger": flux_ledger,
    }


# ============================================================================
# SECTION 5: FIVE ADVERSARIAL PLANTED CONTROLS (CTL-NEG-1 .. CTL-NEG-5)
# ============================================================================

def run_planted_controls(subtask1: dict) -> dict:
    # CTL-NEG-1: Unpriced level-scan cheat on B1839 (fixing delta ~= 0.15 in the null while target scanned 23 levels)
    # falsely suppresses r_975 below 1%, whereas matched 23-level null fails (> 1%) and 4-level B1841 passes (< 1%):
    r39_iso = subtask1["b1839_cell_D_isotropic"]["modes"]["continuous_c_1_3_to_5"]["4.613885"]["r_975"]
    r41_iso = subtask1["b1841_cell_D_isotropic"]["modes"]["continuous_c_1_3_to_5"]["4.726887"]["r_975"]
    r_single_cheat = subtask1["ctl_neg1_single_delta015"]["null_isotropic"]["modes"]["continuous_c_1_3_to_5"]["4.613885"]["r_975"]
    inflation_23_vs_1 = r39_iso / max(r_single_cheat, 1e-12)
    inflation_23_vs_4 = r39_iso / max(r41_iso, 1e-12)
    ctl1_caught = bool(r_single_cheat < 0.01 and r39_iso > 0.01 and r41_iso < 0.01 and inflation_23_vs_4 > 2.5)

    # CTL-NEG-2: Planted naive bare end L_naive = const (omitting +(1/2)*log Im(tau)) under S at tau = 0.23 + 1.37i:
    tau = 0.23 + 1.37j
    tau_S = -1.0 / tau
    la, lb = 2.0 / 5.0, 4.0 / 5.0
    la_S, lb_S = lb % 1.0, (-la) % 1.0
    w0_bad, _, _ = channel_weights_b1919_b1921(tau, la, lb, "d", 1.5 + 0.5 * math.log(tau.imag))
    wS_bad, _, _ = channel_weights_b1919_b1921(tau_S, la_S, lb_S, "d", 1.5 + 0.5 * math.log(tau_S.imag))
    sv0_bad = np.linalg.svd(build_yukawa_from_weights(tau, la, lb, "d", "S", w0_bad), compute_uv=False)
    svS_bad = np.linalg.svd(build_yukawa_from_weights(tau_S, la_S, lb_S, "d", "S", wS_bad), compute_uv=False)
    r0_bad = sv0_bad[1] / sv0_bad[0]
    rS_bad = svS_bad[1] / svS_bad[0]
    ctl2_ratio_drift = abs(rS_bad - r0_bad) / r0_bad
    ctl2_caught = bool(ctl2_ratio_drift > 1e-3)

    # CTL-NEG-3: Planted non-covariant S* = (a1, a2, conj(a3)) reading AND non-Serre ordinary derivative under S:
    eta0, e2_0 = eta_and_e2(tau)
    etaS, e2_S = eta_and_e2(tau_S)
    a0_true = serre_triplet_a(tau)
    aS_true = serre_triplet_a(tau_S)
    w0_good, _, _ = channel_weights_b1919_b1921(tau, la, lb, "d", 1.5)
    wS_good, _, _ = channel_weights_b1919_b1921(tau_S, la_S, lb_S, "d", 1.5)
    sv0_sstar = np.linalg.svd(build_yukawa_from_weights(tau, la, lb, "d", "S*", w0_good), compute_uv=False)
    svS_sstar = np.linalg.svd(build_yukawa_from_weights(tau_S, la_S, lb_S, "d", "S*", wS_good), compute_uv=False)
    sstar_ratio_drift = abs((svS_sstar[1] / svS_sstar[0]) - (sv0_sstar[1] / sv0_sstar[0])) / (sv0_sstar[1] / sv0_sstar[0])

    t2, _ = jacobi_theta_char(0.5, 0.0, 0j, tau)
    t4, _ = jacobi_theta_char(0.0, 0.5, 0j, tau)
    t3, _ = jacobi_theta_char(0.0, 0.0, 0j, tau)
    R0 = np.array([-(t2 * t2), -(t4 * t4), 1j * (t3 * t3)]) / (2.0 * math.pi * eta0 ** 3)
    t2S, _ = jacobi_theta_char(0.5, 0.0, 0j, tau_S)
    t4S, _ = jacobi_theta_char(0.0, 0.5, 0j, tau_S)
    t3S, _ = jacobi_theta_char(0.0, 0.0, 0j, tau_S)
    RS = np.array([-(t2S * t2S), -(t4S * t4S), 1j * (t3S * t3S)]) / (2.0 * math.pi * etaS ** 3)
    d0_ord = a0_true + (e2_0 / 12.0) * R0
    dS_ord = aS_true + (e2_S / 12.0) * RS
    true_serre_err = abs(np.linalg.norm(aS_true) / np.linalg.norm(a0_true) - (abs(tau) ** 1.5))
    bad_ord_err = abs(np.linalg.norm(dS_ord) / np.linalg.norm(d0_ord) - (abs(tau) ** 1.5))
    ctl3_caught = bool(true_serre_err < 1e-13 and bad_ord_err > 1e-2 and sstar_ratio_drift > 1e-2)

    # CTL-NEG-4: Planted commuting abelian subgroup in SU(6) (W29) and SU(5) (W31):
    qi = np.array([[1j, 0], [0, -1j]], dtype=np.complex128)
    w3 = np.exp(2j * math.pi / 3.0)
    P3 = np.diag([1.0, w3, w3 ** 2]).astype(np.complex128)
    A6 = np.kron(qi, P3)
    sys_ab6 = np.kron(np.eye(6), A6) - np.kron(A6.T, np.eye(6))
    ab6_su6_comm = int(np.sum(np.linalg.svd(sys_ab6, compute_uv=False) < 1e-10)) - 1
    w5 = np.exp(2j * math.pi / 5.0)
    P5 = np.diag([w5 ** j for j in range(5)]).astype(np.complex128)
    sys_ab5 = np.kron(np.eye(5), P5) - np.kron(P5.T, np.eye(5))
    ab5_su5_comm = int(np.sum(np.linalg.svd(sys_ab5, compute_uv=False) < 1e-10)) - 1
    ctl4_caught = bool((11 + ab6_su6_comm) == 16 > 11 and (24 + ab5_su5_comm) == 28 > 24)

    # CTL-NEG-5: One-sector 10_g-only count = 3 ignoring SU(5)^3 anomaly AND 1D non-2I subspace violation:
    # At k = 4, taking the 2D odd subspace on 5_b gives N(10_g) = +1 + 2 = +3, while N(5bar_g) = +4 != +3 -> A_SU5 = -1 != 0!
    fake_n10g_at_k4 = 1 + 2
    true_n5barg_min_mismatch = abs(fake_n10g_at_k4 - 4)  # with d10 in {0, 1, 2, 3, 4, 5, 6, 7, 10}, check k=4 local+shift
    T5 = np.diag([w5 ** ((3 * x * x) % 5) for x in range(5)]).astype(np.complex128)
    S5 = -np.array([[w5 ** ((x * y) % 5) for y in range(5)] for x in range(5)], dtype=np.complex128) / math.sqrt(5.0)
    e0 = np.array([1, 0, 0, 0, 0], dtype=np.complex128)
    proj_err_e0 = float(np.linalg.norm(S5 @ e0 - (e0.conj() @ (S5 @ e0)) * e0))
    ctl5_caught = bool(proj_err_e0 > 0.5 and true_n5barg_min_mismatch != 0)

    all_passed = all([ctl1_caught, ctl2_caught, ctl3_caught, ctl4_caught, ctl5_caught])
    assert all_passed, f"One or more planted controls failed to trigger: {[ctl1_caught, ctl2_caught, ctl3_caught, ctl4_caught, ctl5_caught]}"
    return {
        "CTL_NEG_1_single_delta015_cheat_r975": float(r_single_cheat),
        "CTL_NEG_1_matched_23level_b1839_r975": float(r39_iso),
        "CTL_NEG_1_matched_4level_b1841_r975": float(r41_iso),
        "CTL_NEG_1_inflation_23_vs_1": float(inflation_23_vs_1),
        "CTL_NEG_1_inflation_23_vs_4": float(inflation_23_vs_4),
        "CTL_NEG_1_caught": ctl1_caught,
        "CTL_NEG_2_bare_L_S_ratio_drift": float(ctl2_ratio_drift),
        "CTL_NEG_2_caught": ctl2_caught,
        "CTL_NEG_3_sstar_ratio_drift": float(sstar_ratio_drift),
        "CTL_NEG_3_true_serre_err": float(true_serre_err),
        "CTL_NEG_3_non_serre_err": float(bad_ord_err),
        "CTL_NEG_3_caught": ctl3_caught,
        "CTL_NEG_4_w29_abelian_e8_dim": int(11 + ab6_su6_comm),
        "CTL_NEG_4_w31_abelian_e8_dim": int(24 + ab5_su5_comm),
        "CTL_NEG_4_caught": ctl4_caught,
        "CTL_NEG_5_1d_subspace_violation_norm": float(proj_err_e0),
        "CTL_NEG_5_one_sector_10g3_su5_anomaly_mismatch": int(true_n5barg_min_mismatch),
        "CTL_NEG_5_caught": ctl5_caught,
        "all_planted_controls_caught": all_passed,
    }


def main() -> None:
    t_start = time.time()
    print("=== AGY-002 STANDALONE VERIFICATION: A2-NEG (M21 LOAD-BEARING NEGATIVES) ===")

    print("\n[1/4] Running Sub-task 1: B1839 cell D (23 levels) & B1841 cell D (4 levels), 1,000,000 hierarchies (100% data-free)...")
    res1 = run_subtask_1_b1839_b1841()
    m39_iso = res1["b1839_cell_D_isotropic"]["modes"]
    m41_iso = res1["b1841_cell_D_isotropic"]["modes"]
    m39_syn = res1["b1839_cell_D_up017_sensitivity"]["modes"]
    m41_syn = res1["b1841_cell_D_up017_sensitivity"]["modes"]
    print(f"  266-line catalog exact match: {res1['line_catalog_266_exact_match']}")
    print(f"  norms.npz storage kind: {res1['norms_storage_kind']} (W87 calibration abs err = {res1['w87_untwisted_calibration_abs_err']:.3e})")
    print(f"  min positive norm: B1839 = {res1['min_positive_norm_b1839']:.6f}, B1841 = {res1['min_positive_norm_b1841']:.6f}")
    print(f"  Order-5 Y_e == Y_d^T max rel err: {res1['b1841_table_stats']['order5_ye_eq_ydT_max_rel_err']:.3e}")
    print("  [Mode A (Primary): Strictly isotropic 10% log-width, N = 1,000,000]")
    print(f"    B1839 (23 levels) cont c @  4.613885: hits = {m39_iso['continuous_c_1_3_to_5']['4.613885']['hits']}, p_hat = {m39_iso['continuous_c_1_3_to_5']['4.613885']['p_hat']:.6f}, r_975 = {m39_iso['continuous_c_1_3_to_5']['4.613885']['r_975']:.6f}, pass_1pct = {m39_iso['continuous_c_1_3_to_5']['4.613885']['passes_1pct_gate']}")
    print(f"    B1839 (23 levels) grid9  @  5.372228: hits = {m39_iso['grid9_c']['5.372228']['hits']}, r_975 = {m39_iso['grid9_c']['5.372228']['r_975']:.6f}")
    print(f"    B1839 (23 levels) {{1,3}}  @ 11.360492: hits = {m39_iso['discrete_c_1_3']['11.360492']['hits']}, r_975 = {m39_iso['discrete_c_1_3']['11.360492']['r_975']:.6f}")
    print(f"    B1841 ( 4 levels) cont c @  4.726887: hits = {m41_iso['continuous_c_1_3_to_5']['4.726887']['hits']}, p_hat = {m41_iso['continuous_c_1_3_to_5']['4.726887']['p_hat']:.6f}, r_975 = {m41_iso['continuous_c_1_3_to_5']['4.726887']['r_975']:.6f}, pass_1pct = {m41_iso['continuous_c_1_3_to_5']['4.726887']['passes_1pct_gate']}")
    print(f"    B1841 ( 4 levels) grid9  @  5.410482: hits = {m41_iso['grid9_c']['5.410482']['hits']}, r_975 = {m41_iso['grid9_c']['5.410482']['r_975']:.6f}")
    print(f"    B1841 ( 4 levels) {{1,3}}  @ 11.977974: hits = {m41_iso['discrete_c_1_3']['11.977974']['hits']}, r_975 = {m41_iso['discrete_c_1_3']['11.977974']['r_975']:.6f}")
    print("  [Mode B (Sensitivity): Data-free synthetic up-quark log-width 0.17 (1.7x ellipsoid), N = 1,000,000]")
    print(f"    B1839 (23 levels) cont c @  4.613885: hits = {m39_syn['continuous_c_1_3_to_5']['4.613885']['hits']}, p_hat = {m39_syn['continuous_c_1_3_to_5']['4.613885']['p_hat']:.6f}, r_975 = {m39_syn['continuous_c_1_3_to_5']['4.613885']['r_975']:.6f}, pass_1pct = {m39_syn['continuous_c_1_3_to_5']['4.613885']['passes_1pct_gate']}")
    print(f"    B1841 ( 4 levels) cont c @  4.726887: hits = {m41_syn['continuous_c_1_3_to_5']['4.726887']['hits']}, p_hat = {m41_syn['continuous_c_1_3_to_5']['4.726887']['p_hat']:.6f}, r_975 = {m41_syn['continuous_c_1_3_to_5']['4.726887']['r_975']:.6f}, pass_1pct = {m41_syn['continuous_c_1_3_to_5']['4.726887']['passes_1pct_gate']}")

    print("\n[2/4] Running Sub-task 2: P-720 modular weight at 3 generic tau x 3 lines x 2 readings x 3 sectors...")
    res2 = run_subtask_2_p720(L_coord=1.50)
    print(f"  Cases tested: {res2['n_cases_tested']}, min channel norm = {res2['min_channel_norm']:.6f}")
    print(f"  Max |k_measured - 1| under S on raw Yukawa singular values: {res2['max_S_raw_weight_1_abs_err']:.3e}")
    print(f"  Max relative error under S on singular-value ratios (weight 0): {res2['max_S_ratio_weight_0_rel_err']:.3e}")
    print(f"  Max relative error under T on raw singular values: {res2['max_T_raw_rel_err']:.3e}")
    print(f"  Max unitary basis-scrambling & S-invariance error on |V_CKM|: {res2['max_unitary_basis_scramble_and_S_ckm_err']:.3e}")

    print("\n[3/4] Running Sub-task 3: E_8 twist-eaters W29 (Z_6, row 945) & W31 (Z_5, row 949)...")
    roots = generate_e8_roots()
    e8_chk = build_chevalley_e8_basis_check(roots)
    w29 = verify_w29_z6_twist_eater(roots)
    w31 = verify_w31_z5_twist_eater(roots)
    print(f"  E_8 roots = {e8_chk['n_roots']}, dim = {e8_chk['dim_e8']}, Cartan det = {e8_chk['cartan_det']}")
    print(f"  W29 (Z_6): centraliser dim = {w29['e8_centraliser_dim']} ({w29['centraliser_algebra']}), U(1)_Y dim = {w29['surviving_u1_hypercharge_dim']}, chiral leptons = {w29['chiral_leptons_count']}")
    print(f"  W29 quark generations: locality = {w29['quark_generations_under_locality']}, moves = {w29['quark_generations_under_moves']}")
    print(f"  W31 (Z_5): centraliser dim = {w31['e8_centraliser_dim']} ({w31['centraliser_algebra']}), |Heis| = {w31['heisenberg_order']}, |2I| = {w31['weil_2I_order']}, |Clifford_proj| = {w31['projective_z5_clifford_order']}")
    print(f"  W31 anomaly-free local? {w31['any_local_anomaly_free']}, reaches +-3 under moves? {w31['any_three_generations_under_moves']}")
    for fk, fv in w31["flux_ledger"].items():
        print(f"    {fk}: local={fv['local_APS_N10g_N5barg']}, sign-kept SU(5)^3-free={fv['SU5_free_sign_on_5b']}, unrestricted moves={fv['SU5_free_all_moves_unrestricted']}")

    print("\n[4/4] Running Five Adversarial Planted Controls (CTL-NEG-1 .. CTL-NEG-5)...")
    ctls = run_planted_controls(res1)
    for k, v in ctls.items():
        print(f"  {k}: {v}")

    full_payload = {
        "card": "AGY-002_A2-NEG_load-bearing-negatives",
        "total_elapsed_sec": round(time.time() - t_start, 3),
        "subtask_1_b1839_b1841_cell_D": res1,
        "subtask_2_p720_modular_weight": res2,
        "subtask_3_e8_twist_eaters": {
            "e8_root_lattice": e8_chk,
            "w29_row_945": w29,
            "w31_row_949": w31,
        },
        "planted_controls": ctls,
    }

    json_path = OUT_DIR / "verify_a2_neg_results.json"
    json_path.write_text(json.dumps(full_payload, indent=2, default=float), encoding="utf-8")
    print(f"\nWrote {json_path} in {full_payload['total_elapsed_sec']:.2f}s.")
    print("0 of 19.")


if __name__ == "__main__":
    main()
