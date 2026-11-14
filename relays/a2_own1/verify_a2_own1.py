#!/usr/bin/env python3
"""Standalone verification of Card A2-OWN1 (M24 Open Question):
  1. Theorem 1 — Dual Twin Involutions (anti-holomorphic J vs holomorphic S) & Mark-Stabilising CP Parity:
     - Haar random unitary basis-scrambling invariance check (< 1e-13) on all observables & Jarlskog J_CP;
     - Pointwise & geodesic-period identity O(J*tau, twin) == O(tau, mark) (< 1e-12) with J_CP sign flip (< 1e-14);
     - Holomorphic modular-S identity O(-1/tau, twin) == O(tau, mark) (< 1e-12) with J_CP sign PRESERVATION (< 1e-14);
     - Composed anti-holomorphic mark-stabiliser tau -> 1 - conj(tau) fixing mark & flipping J_CP -> -J_CP;
     - Exact {L, R}^10 R-ending to L-starting bijection under J W(L,R) J^(-1) = L W(R,L) L^(-1).
  2. Theorem 2 — Four-Cusp Structure [5, 5, 1, 1], Projective Democracy, & Exact Hyperbolic-Area Read-Out (b)
     in BOTH B1656's exact 24-observable frame AND our 30-observable P-720 frame across
     L_coord in {0.90, 1.30, gamma + log(pi) [= 1.7219456, L_tilde = 0], 2.20} PLUS systole-regularised L_tilde_sys = 0.
  3. Theorem 3 — Quantitative Separation Between Bernoulli Word-Weight (a) and Hyperbolic-Area Weight (b)
     directly on B1656's exact n = 12 (345 words) & n = 16 (5,453 words) exhaustive populations and n = 28 (400-word) sample.
  4. Theorem 4 & Three Adversarial Planted Controls (CTL-OWN1-1..3):
     - Width-five cusp degeneration F_u ~ -pi ln(y) -> -infty for constant L_coord vs global positivity
       F_u^sys = F_u + pi ln(y_FD) >= +6.94 > 0 everywhere on X(Gamma_+-) with 0.0% clamping at L_tilde_sys = 0;
     - Wrong holomorphic J control, logarithmic cusp divergence of -ln(m_u/m_t), and high-cusp / sub-floor norm traps.

Strictly 100% data-free: 0 of 19.
"""

from __future__ import annotations

import json
import math
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Dict, List, Tuple

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import digamma


def flush_tiny_complex(arr: np.ndarray, thresh: float = 1e-80) -> np.ndarray:
    """Flush < 1e-80 entries to 0.0 to avoid macOS Accelerate LAPACK zlartg NaN bug on tiny entries."""
    return np.where(np.abs(arr.real) < thresh, 0.0, arr.real) + 1j * np.where(np.abs(arr.imag) < thresh, 0.0, arr.imag)


OUT_DIR = Path(__file__).resolve().parent
EG = 0.5772156649015329
KRONECKER_SHIFT = EG + math.log(math.pi)

J_MAT = np.array([[1, 1], [1, 0]], dtype=np.int64)
J_INV = np.array([[0, 1], [1, -1]], dtype=np.int64)

# ---- Frame 1 (30-obs P-720 frame) constants ----
SECTOR_CHARGES: Dict[str, Tuple[int, int]] = {"u": (1, -4), "d": (1, 2), "e": (-3, 6)}
CHANNEL_THETA_AB: List[Tuple[float, float, float]] = [
    (0.5, 0.5, -1.0),
    (0.5, 0.0, +1.0),
    (0.0, 0.5, +1.0),
    (0.0, 0.0, +1.0),
]
CHANNEL_SHIFTS: List[Tuple[float, float]] = [(0.0, 0.0), (0.0, 0.5), (0.5, 0.0), (0.5, 0.5)]
OBS30_NAMES = [
    "S_mu_mt", "S_mc_mt", "S_md_mb", "S_ms_mb", "S_me_mtau", "S_mmu_mtau",
    "St_mu_mt", "St_mc_mt", "St_md_mb", "St_ms_mb", "St_me_mtau", "St_mmu_mtau",
    "CKM_S_Vud", "CKM_S_Vus", "CKM_S_Vub", "CKM_S_Vcd", "CKM_S_Vcs", "CKM_S_Vcb", "CKM_S_Vtd", "CKM_S_Vts", "CKM_S_Vtb",
    "CKM_St_Vud", "CKM_St_Vus", "CKM_St_Vub", "CKM_St_Vcd", "CKM_St_Vcs", "CKM_St_Vcb", "CKM_St_Vtd", "CKM_St_Vts", "CKM_St_Vtb",
]

# ---- Frame 2 (Exact B1656 24-obs frame) constants ----
QI = np.array([[1j, 0], [0, -1j]], dtype=np.complex128)
QJ = np.array([[0, 1], [-1, 0]], dtype=np.complex128)
QK = QI @ QJ
EPS = QJ
UNITS_LIST = [np.eye(2, dtype=np.complex128), QI, QJ, QK]
BLOCKS = [QJ, QI, QK]
EC_LIST = [EPS @ U for U in UNITS_LIST]
G_MAT = np.array([[np.sum(EC_LIST[t] * UNITS_LIST[s]) for s in range(4)] for t in range(4)], dtype=np.complex128)
GINV = np.linalg.inv(G_MAT)
EDUAL_LIST = [sum(GINV[b, a] * UNITS_LIST[b] for b in range(4)) for a in range(4)]
Q_BASIS = [QI, QJ, QK]
Q_ST_BASIS = [EPS @ np.conj(Q) @ EPS.T for Q in Q_BASIS]
COUP_S = np.zeros((3, 4, 3, 3), dtype=np.complex128)
COUP_ST = np.zeros((3, 4, 3, 3), dtype=np.complex128)
for _qi in range(3):
    for _si in range(4):
        for _a in range(3):
            for _b in range(3):
                COUP_S[_qi, _si, _a, _b] = np.sum((BLOCKS[_a].T @ EPS @ Q_BASIS[_qi] @ BLOCKS[_b]) * EDUAL_LIST[_si])
                COUP_ST[_qi, _si, _a, _b] = np.sum((BLOCKS[_a].T @ EPS @ Q_ST_BASIS[_qi] @ BLOCKS[_b]) * EDUAL_LIST[_si])

SECT_B1656 = [("up", 1, -4), ("down", 1, 2), ("lep", -3, 6)]
CHAR_SHIFTS_B1656 = [(0.0, 0.0), (0.0, -0.5), (-0.5, 0.0), (-0.5, -0.5)]
OBS24_NAMES: List[str] = [
    "up|S|m2_m3", "up|S|m1_m3", "up|St|m2_m3", "up|St|m1_m3",
    "down|S|m2_m3", "down|S|m1_m3", "down|St|m2_m3", "down|St|m1_m3",
    "lep|S|m2_m3", "lep|S|m1_m3", "lep|St|m2_m3", "lep|St|m1_m3",
    "ckm|S|S|Vus", "ckm|S|S|Vcb", "ckm|S|S|Vub",
    "ckm|S|St|Vus", "ckm|S|St|Vcb", "ckm|S|St|Vub",
    "ckm|St|S|Vus", "ckm|St|S|Vcb", "ckm|St|S|Vub",
    "ckm|St|St|Vus", "ckm|St|St|Vcb", "ckm|St|St|Vub",
]


def random_haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = d / np.abs(d)
    return q * ph[None, :]


def sl2z_pullback_points(taus: np.ndarray, line_a: np.ndarray, line_b: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    t = taus.astype(np.complex128).copy()
    u1 = (line_a % 1.0).astype(np.float64).copy()
    u2 = (line_b % 1.0).astype(np.float64).copy()
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


def pullback_b1724(taus: np.ndarray, a0: float, b0: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    t = taus.astype(np.complex128).copy()
    a = np.full(len(t), a0 % 1.0, dtype=np.float64)
    b = np.full(len(t), b0 % 1.0, dtype=np.float64)
    for _ in range(250):
        n = np.rint(t.real)
        ms = n != 0.0
        if np.any(ms):
            t[ms] -= n[ms]
            b[ms] = (b[ms] + n[ms] * a[ms]) % 1.0
        mi = np.abs(t) < (1.0 - 1e-12)
        if not np.any(mi):
            break
        t[mi] = -1.0 / t[mi]
        oa = a[mi].copy()
        a[mi] = (-b[mi]) % 1.0
        b[mi] = oa % 1.0
    return t, a, b


def kronecker_Fu_vec(u1: np.ndarray, u2: np.ndarray, taus_fd: np.ndarray, m_cut: int = 32, zero_to_inf: bool = False) -> np.ndarray:
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
        if zero_to_inf:
            out[mask_zero] = float("inf")
        else:
            tz = taus_fd[mask_zero]
            yz = y[mask_zero]
            m_pows = np.arange(1, 45, dtype=np.float64)[None, :]
            q = np.exp(2j * math.pi * tz)[:, None]
            # Underflow-safe exact log(|eta(tau)|^2) valid for arbitrarily large yz:
            log_eta_abs2 = -math.pi * yz / 6.0 + np.sum(2.0 * np.log(np.abs(1.0 - q ** m_pows)), axis=1)
            out[mask_zero] = 2.0 * math.pi * (EG - math.log(2.0) - 0.5 * np.log(yz) - log_eta_abs2)
    if np.any(mask_a0):
        xa = x[mask_a0][:, None]
        ya = y[mask_a0][:, None]
        ba = b[mask_a0][:, None]
        base = math.pi * (2.0 * EG - 2.0 * math.log(2.0) - np.log(ya[:, 0]))
        m0 = (math.pi ** 2) * ya[:, 0] / (np.sin(math.pi * ba[:, 0]) ** 2)
        ms = np.concatenate([np.arange(-m_cut, 0, dtype=np.float64), np.arange(1, m_cut + 1, dtype=np.float64)])[None, :]
        wm = np.exp(2j * math.pi * (ms * xa + ba) - 2.0 * math.pi * np.abs(ms) * ya)
        out[mask_a0] = base + m0 + np.sum((2.0 * math.pi / np.abs(ms)) * (wm / (1.0 - wm)).real, axis=1)
    if np.any(mask_gen):
        xg = x[mask_gen][:, None]
        yg = y[mask_gen][:, None]
        ag = a[mask_gen][:, None]
        bg = b[mask_gen][:, None]
        base = -math.pi * (digamma(ag[:, 0]) + digamma(1.0 - ag[:, 0]) + 2.0 * math.log(2.0) + np.log(yg[:, 0]))
        ms = np.arange(-m_cut, m_cut + 1, dtype=np.float64)[None, :] + ag
        wm = np.exp(2j * math.pi * (ms * xg + bg) - 2.0 * math.pi * np.abs(ms) * yg)
        out[mask_gen] = base + np.sum((2.0 * math.pi / np.abs(ms)) * (wm / (1.0 - wm)).real, axis=1)
    return out


def eval_fd_observables_and_jarlskog(
    taus_fd: np.ndarray,
    la_fd: np.ndarray,
    lb_fd: np.ndarray,
    L_coord_list: List[float],
    check_haar_scrambling: bool = False,
    systole_reg: bool = False,
    clamp_floor: bool = True,
) -> Tuple[Dict[float, np.ndarray], Dict[float, np.ndarray], Dict[float, float], float]:
    M = len(taus_fd)
    y = taus_fd.imag
    m_pows = np.arange(1, 45, dtype=np.float64)[None, :]
    q = np.exp(2j * math.pi * taus_fd)[:, None]
    qp = q ** m_pows
    eta3_scaled = np.exp(1j * math.pi * taus_fd.real / 4.0) * (np.prod(1.0 - qp, axis=1) ** 3)
    e2 = 1.0 - 24.0 * np.sum(m_pows * qp / (1.0 - qp), axis=1)
    denom = 2.0 * math.pi * eta3_scaled

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

    def theta_kappa_4chan_per_ch(alpha_arr: np.ndarray, beta_arr: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Return (scaled_4chan, d2_per_ch) where each channel ch_i has its OWN min_n (na + alpha)^2 subtracted,
        so every non-zero channel sum is O(1) before combining u and d factors."""
        out = np.zeros((M, 4), dtype=np.complex128)
        d2_ch = np.zeros((M, 4), dtype=np.float64)
        al_c = alpha_arr[:, None]
        be_c = beta_arr[:, None]
        n_shift = np.rint(al_c)
        pref = np.exp(1j * math.pi * alpha_arr * beta_arr)
        x_col = taus_fd.real[:, None]
        y_col = y[:, None]
        for ch_i, (ca, cb, sgn) in enumerate(CHANNEL_THETA_AB):
            na = (n_vec - n_shift) + ca
            c2 = (na + al_c) ** 2
            c2_min = np.min(c2, axis=1, keepdims=True)
            d2_ch[:, ch_i] = c2_min[:, 0]
            terms = np.exp(1j * math.pi * c2 * x_col - math.pi * (c2 - c2_min) * y_col + 2j * math.pi * na * (be_c + cb))
            out[:, ch_i] = (sgn * pref) * np.sum(terms, axis=1)
        return out, d2_ch

    C_PREF = np.array([-1j, -1.0 + 0j, -1.0 + 0j, +1j], dtype=np.complex128)[None, :]
    R_sec: Dict[str, np.ndarray] = {}
    Fsum_sec: Dict[str, np.ndarray] = {}
    sys_term = (2.0 * math.pi * np.log(y))[:, None] if systole_reg else 0.0

    for sec, (qL, qR) in SECTOR_CHARGES.items():
        au = (qL + qR) * la_fd
        bu = (qL + qR) * lb_fd
        ad = (qL - qR) * la_fd
        bd = (qL - qR) * lb_fd
        tu, d2_u = theta_kappa_4chan_per_ch(au, bu)
        td, d2_d = theta_kappa_4chan_per_ch(ad, bd)
        d2_sum = d2_u + d2_d
        d2_joint_min = np.min(d2_sum, axis=1, keepdims=True)
        rel_env = np.exp(-math.pi * (d2_sum - d2_joint_min) * y[:, None])
        R_sec[sec] = (C_PREF * tu * td * rel_env) / denom[:, None]
        fsum = np.zeros((M, 4), dtype=np.float64)
        for ch_i, (s1, s2) in enumerate(CHANNEL_SHIFTS):
            up1 = ((qL + qR) * la_fd + s1) % 1.0
            up2 = ((qL + qR) * lb_fd + s2) % 1.0
            um1 = ((qL - qR) * la_fd + s1) % 1.0
            um2 = ((qL - qR) * lb_fd + s2) % 1.0
            fsum[:, ch_i] = kronecker_Fu_vec(up1, up2, taus_fd) + kronecker_Fu_vec(um1, um2, taus_fd)
        Fsum_sec[sec] = fsum + sys_term

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

    obs_by_L: Dict[float, np.ndarray] = {}
    jcp_by_L: Dict[float, np.ndarray] = {}
    clamp_by_L: Dict[float, float] = {}
    max_haar_scramble_err = 0.0
    rng_h = np.random.default_rng(20261114)

    for Lc in L_coord_list:
        obs = np.zeros((M, 30), dtype=np.float64)
        jcp = np.zeros((M, 2), dtype=np.float64)
        U_left: Dict[Tuple[str, str], np.ndarray] = {}
        Y_saved: Dict[Tuple[str, str], np.ndarray] = {}
        n_clamp = 0
        n_tot = 0

        for s_idx, sec in enumerate(["u", "d", "e"]):
            raw_norms = 4.0 * math.pi * (Lc - KRONECKER_SHIFT) + Fsum_sec[sec] if systole_reg else 4.0 * math.pi * Lc + Fsum_sec[sec]
            n_tot += raw_norms.size
            n_clamp += int(np.sum(raw_norms <= 0.0))
            if (not clamp_floor) and np.any(raw_norms <= 0.0):
                raise RuntimeError(f"Non-positive norm at L_coord={Lc}: min={np.min(raw_norms)}")
            norms = np.maximum(raw_norms, 1e-12)
            u_vec4 = R_sec[sec] / np.sqrt(norms)
            u_vec4 = u_vec4 / np.maximum(np.linalg.norm(u_vec4, axis=1, keepdims=True), 1e-300)
            for r_tag, a_arr, col_off in [("S", a_S, 0), ("S~", a_St, 6)]:
                Y_batch = flush_tiny_complex(build_Y_batch(a_arr, u_vec4))
                if check_haar_scrambling:
                    Y_saved[(sec, r_tag)] = Y_batch.copy()
                if sec in ("u", "d"):
                    U_svd, sv, _ = np.linalg.svd(Y_batch)
                    U_left[(sec, r_tag)] = U_svd[:, :, ::-1]
                else:
                    sv = np.linalg.svd(Y_batch, compute_uv=False)
                denom_sv = np.maximum(sv[:, 0], 1e-300)
                obs[:, col_off + 2 * s_idx] = sv[:, 2] / denom_sv
                obs[:, col_off + 2 * s_idx + 1] = sv[:, 1] / denom_sv

        Uu_St_H = np.conj(np.transpose(U_left[("u", "S~")], (0, 2, 1)))
        V_S_mat = Uu_St_H @ U_left[("d", "S")]
        V_St_mat = Uu_St_H @ U_left[("d", "S~")]
        obs[:, 12:21] = np.abs(V_S_mat).reshape(M, 9)
        obs[:, 21:30] = np.abs(V_St_mat).reshape(M, 9)
        jcp[:, 0] = np.imag(V_S_mat[:, 0, 1] * V_S_mat[:, 1, 2] * np.conj(V_S_mat[:, 0, 2]) * np.conj(V_S_mat[:, 1, 1]))
        jcp[:, 1] = np.imag(V_St_mat[:, 0, 1] * V_St_mat[:, 1, 2] * np.conj(V_St_mat[:, 0, 2]) * np.conj(V_St_mat[:, 1, 1]))

        if check_haar_scrambling:
            UQ = random_haar_unitary(3, rng_h)
            UuR = random_haar_unitary(3, rng_h)
            UdR = random_haar_unitary(3, rng_h)
            UL = random_haar_unitary(3, rng_h)
            UeR = random_haar_unitary(3, rng_h)
            Yu_scr = UQ[None, :, :] @ Y_saved[("u", "S~")] @ UuR.conj().T[None, :, :]
            Yd_scr = UQ[None, :, :] @ Y_saved[("d", "S")] @ UdR.conj().T[None, :, :]
            Ye_scr = UL[None, :, :] @ Y_saved[("e", "S")] @ UeR.conj().T[None, :, :]
            Uu2, svu2, _ = np.linalg.svd(Yu_scr)
            Ud2, svd2, _ = np.linalg.svd(Yd_scr)
            sve2 = np.linalg.svd(Ye_scr, compute_uv=False)
            V2 = np.conj(np.transpose(Uu2[:, :, ::-1], (0, 2, 1))) @ Ud2[:, :, ::-1]
            j2 = np.imag(V2[:, 0, 1] * V2[:, 1, 2] * np.conj(V2[:, 0, 2]) * np.conj(V2[:, 1, 1]))
            err_u = float(np.max(np.abs(svu2[:, 2] / svu2[:, 0] - obs[:, 6])))
            err_e = float(np.max(np.abs(sve2[:, 2] / sve2[:, 0] - obs[:, 4])))
            err_v = float(np.max(np.abs(np.abs(V2).reshape(M, 9) - obs[:, 12:21])))
            err_j = float(np.max(np.abs(j2 - jcp[:, 0])))
            max_haar_scramble_err = max(max_haar_scramble_err, err_u, err_e, err_v, err_j)

        obs_by_L[Lc] = obs
        jcp_by_L[Lc] = jcp
        clamp_by_L[Lc] = float(n_clamp) / max(n_tot, 1)

    return obs_by_L, jcp_by_L, clamp_by_L, max_haar_scramble_err


def eval_b1656_fd(
    taus_fd: np.ndarray,
    a_fd: np.ndarray,
    b_fd: np.ndarray,
    Lc_list: List[float],
    systole_reg: bool = False,
) -> Tuple[Dict[float, np.ndarray], Dict[float, float]]:
    """Exact B1656 24-observable evaluator on F_1 points with positive-real cusp envelope scaling
    (preventing float64 underflow at arbitrary cusp height y) and exact clamp-rate diagnostic."""
    M = len(taus_fd)
    x = taus_fd.real
    y = taus_fd.imag
    t_col = taus_fd[:, None]
    m_p = np.arange(1.0, 45.0)[None, :]
    q = np.exp(2j * math.pi * taus_fd)[:, None]
    qp = q ** m_p
    eta_hat = np.exp(1j * math.pi * x / 12.0) * np.prod(1.0 - qp, axis=1)
    e2 = 1.0 - 24.0 * np.sum(m_p * qp / (1.0 - qp), axis=1)
    denom_hat = 2.0 * math.pi * (eta_hat ** 3)

    nv = np.arange(-16.0, 17.0)[None, :]

    def th0_dt(ca: float, cb: float) -> Tuple[np.ndarray, np.ndarray]:
        na = nv + ca
        terms = np.exp(1j * math.pi * (na * na) * t_col + 2j * math.pi * na * cb)
        return np.sum(terms, axis=1), np.sum(0.5 * (na * na) * terms, axis=1)

    t2, dt2 = th0_dt(0.5, 0.0)
    t4, dt4 = th0_dt(0.0, 0.5)
    t3, dt3 = th0_dt(0.0, 0.0)
    R_hat = np.column_stack([-(t2 * t2), -(t4 * t4), 1j * (t3 * t3)]) / denom_hat[:, None]
    dN_hat = np.column_stack([-2.0 * t2 * dt2, -2.0 * t4 * dt4, 2j * t3 * dt3]) / denom_hat[:, None]
    c3_S = dN_hat - (e2 / 12.0)[:, None] * R_hat
    c3_St = np.conj(c3_S)

    ks = np.arange(-20.0, 21.0)[None, :]
    x_col = x[:, None]
    y_col = y[:, None]

    def thc0_and_1_scaled(a_arr: np.ndarray, b_arr: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Multiply both X0 and X1t by the SAME positive real envelope exp(+2*pi*y*d2_min) > 0."""
        k0 = np.rint(-a_arr)[:, None]
        n0 = ks + k0 + a_arr[:, None]
        k1 = np.rint(-a_arr - 0.5)[:, None]
        n1 = ks + k1 + a_arr[:, None]
        n1_h = n1 + 0.5
        d2_min = np.minimum(np.min(n0 ** 2, axis=1), np.min(n1_h ** 2, axis=1))[:, None]
        X0 = np.sum(np.exp(2j * math.pi * x_col * (n0 ** 2) - 2.0 * math.pi * y_col * ((n0 ** 2) - d2_min) + 2j * np.pi * n0 * b_arr[:, None]), axis=1)
        X1t = np.sum(np.exp(2j * math.pi * x_col * (n1_h ** 2) - 2.0 * math.pi * y_col * ((n1_h ** 2) - d2_min) + 2j * np.pi * n1 * b_arr[:, None]), axis=1)
        return X0, X1t

    R_sec: Dict[str, np.ndarray] = {}
    Fu_sec: Dict[str, np.ndarray] = {}
    sys_term = (math.pi * np.log(y))[:, None] if systole_reg else 0.0

    for sname, ql, qr in SECT_B1656:
        ax = ql * a_fd
        bx = 2.0 * ql * b_fd
        ay = qr * a_fd
        by = 2.0 * qr * b_fd
        X0, X1t = thc0_and_1_scaled(ax, bx)
        Y0, Y1t = thc0_and_1_scaled(ay, by)
        M_mat = np.zeros((M, 2, 2), dtype=np.complex128)
        M_mat[:, 0, 0] = X0 * Y0 / denom_hat
        M_mat[:, 0, 1] = np.exp(1j * np.pi * by) * X0 * Y1t / (1j * denom_hat)
        M_mat[:, 1, 0] = np.exp(1j * np.pi * bx) * X1t * Y0 / (1j * denom_hat)
        M_mat[:, 1, 1] = -np.exp(1j * np.pi * (bx + by)) * X1t * Y1t / denom_hat
        R_arr = np.zeros((M, 4), dtype=np.complex128)
        for si in range(4):
            R_arr[:, si] = np.sum(EC_LIST[si][None, :, :] * M_mat, axis=(1, 2))
        R_sec[sname] = R_arr

        ap = ax + ay
        bp = 0.5 * (bx + by)
        fu_arr = np.zeros((M, 4), dtype=np.float64)
        for si, (ds1, ds2) in enumerate(CHAR_SHIFTS_B1656):
            fu_arr[:, si] = kronecker_Fu_vec(ap + ds1, bp + ds2, taus_fd, zero_to_inf=True)
        Fu_sec[sname] = fu_arr + sys_term

    out: Dict[float, np.ndarray] = {}
    clamp_share: Dict[float, float] = {}

    for Lc in Lc_list:
        shift_c = 2.0 * math.pi * (Lc - KRONECKER_SHIFT)
        obs = np.zeros((M, 24), dtype=np.float64)
        U_store: Dict[Tuple[str, str], np.ndarray] = {}
        col = 0
        n_clamped = 0
        n_active = 0
        for sname, _, _ in SECT_B1656:
            val = shift_c + Fu_sec[sname]
            active = np.isfinite(val)
            n_active += int(np.sum(active))
            n_clamped += int(np.sum(active & (val <= 0.0)))
            w = np.where(active, np.sqrt(np.maximum(val, 1e-12)), 0.0)
            u_ch = w * R_sec[sname]
            u_ch = u_ch / np.maximum(np.linalg.norm(u_ch, axis=1, keepdims=True), 1e-300)
            YS = flush_tiny_complex(np.einsum("mq,ms,qsab->mab", c3_S, u_ch, COUP_S))
            YSt = flush_tiny_complex(np.einsum("mq,ms,qsab->mab", c3_St, u_ch, COUP_ST))
            for rn, Ym in [("S", YS), ("St", YSt)]:
                if sname in ("up", "down"):
                    U_svd, sv, _ = np.linalg.svd(Ym)
                    U_store[(sname, rn)] = U_svd[:, :, ::-1]
                else:
                    sv = np.linalg.svd(Ym, compute_uv=False)
                denom_sv = np.maximum(sv[:, 0], 1e-300)
                obs[:, col] = sv[:, 1] / denom_sv
                obs[:, col + 1] = sv[:, 2] / denom_sv
                col += 2

        for ru in ("S", "St"):
            for rd in ("S", "St"):
                UuH = np.conj(np.transpose(U_store[("up", ru)], (0, 2, 1)))
                V = np.abs(UuH @ U_store[("down", rd)])
                obs[:, col] = V[:, 0, 1]
                obs[:, col + 1] = V[:, 1, 2]
                obs[:, col + 2] = V[:, 0, 2]
                col += 3

        out[Lc] = obs
        clamp_share[Lc] = float(n_clamped) / max(n_active, 1)

    return out, clamp_share


def word_bits_to_matrix(bits: int, length: int) -> np.ndarray:
    mat = np.eye(2, dtype=np.int64)
    for pos in range(length - 1, -1, -1):
        if (bits >> pos) & 1:
            mat[:, 0] += mat[:, 1]
        else:
            mat[:, 1] += mat[:, 0]
    return mat


def is_allowed_mod5_p720(mat: np.ndarray) -> bool:
    v0 = int((2 * mat[0, 0] + 4 * mat[1, 0]) % 5)
    v1 = int((2 * mat[0, 1] + 4 * mat[1, 1]) % 5)
    return (v0 == 2 and v1 == 4) or (v0 == 3 and v1 == 1)


def geodesic_midpoint_taus(M_word: np.ndarray, density: float = 32.0, min_nodes: int = 64) -> Tuple[float, np.ndarray]:
    gamma = M_word.T
    a, b, c, d = float(gamma[0, 0]), float(gamma[0, 1]), float(gamma[1, 0]), float(gamma[1, 1])
    tr = a + d
    disc = math.sqrt(tr * tr - 4.0)
    r1 = ((a - d) + disc) / (2.0 * c)
    r2 = ((a - d) - disc) / (2.0 * c)
    beta, betap = max(r1, r2), min(r1, r2)
    ell = 2.0 * math.log(0.5 * (abs(tr) + disc))

    def zt(s_arr: np.ndarray) -> np.ndarray:
        es = np.exp(s_arr)
        return (beta * 1j * es + betap) / (1j * es + 1.0)

    z0 = complex(zt(np.array([-0.5 * ell]))[0])
    z1 = complex(zt(np.array([+0.5 * ell]))[0])
    gz0 = (a * z0 + b) / (c * z0 + d)
    ell_signed = ell if abs(gz0 - z1) <= 1e-7 * (1.0 + abs(z0)) else -ell

    nodes = max(min_nodes, int(math.ceil(density * ell)))
    ss = -0.5 * ell_signed + ell_signed * (np.arange(nodes, dtype=np.float64) + 0.5) / nodes
    return ell, zt(ss)


def geodesic_axis_points(mat: np.ndarray, n_quad: int = 96) -> Tuple[float, np.ndarray]:
    p, q, r, s = float(mat[0, 0]), float(mat[0, 1]), float(mat[1, 0]), float(mat[1, 1])
    tr = p + s
    disc = math.sqrt(tr * tr - 4.0)
    ell = 2.0 * math.log(0.5 * (tr + disc))
    xp = ((p - s) + disc) / (2.0 * r)
    xm = ((p - s) - disc) / (2.0 * r)
    c0, hs = 0.5 * (xp + xm), 0.5 * (xp - xm)
    u = (np.arange(n_quad, dtype=np.float64) + 0.5) * (ell / n_quad)
    taus = (c0 + hs * np.tanh(u)) + 1j * (abs(hs) / np.cosh(u))
    return ell, taus


def verify_part1_dual_twin_and_cp_parity() -> dict:
    taus_test = np.array([
        -0.31 + 1.17j,
        0.19 + 0.94j,
        0.43 + 1.83j,
        -0.12 + 0.41j,
        1.73 + 0.29j,
    ], dtype=np.complex128)
    taus_J = (np.conj(taus_test) + 1.0) / np.conj(taus_test)
    taus_S = -1.0 / taus_test
    taus_MCP = 1.0 - np.conj(taus_test)

    tm, am, bm = sl2z_pullback_points(taus_test, np.full(5, 0.4), np.full(5, 0.8))
    tt_J, at_J, bt_J = sl2z_pullback_points(taus_J, np.full(5, 0.2), np.full(5, 0.4))
    tt_S, at_S, bt_S = sl2z_pullback_points(taus_S, np.full(5, 0.2), np.full(5, 0.4))
    tm_cp, am_cp, bm_cp = sl2z_pullback_points(taus_MCP, np.full(5, 0.4), np.full(5, 0.8))

    L_test = [0.90, 1.30, KRONECKER_SHIFT, 2.20]
    obs_m, jcp_m, _, haar_err = eval_fd_observables_and_jarlskog(tm, am, bm, L_test, check_haar_scrambling=True)
    obs_J, jcp_J, _, _ = eval_fd_observables_and_jarlskog(tt_J, at_J, bt_J, L_test)
    obs_S, jcp_S, _, _ = eval_fd_observables_and_jarlskog(tt_S, at_S, bt_S, L_test)
    obs_cp, jcp_cp, _, _ = eval_fd_observables_and_jarlskog(tm_cp, am_cp, bm_cp, L_test)

    # Also verify exact B1656-24 pointwise invariance under J, S, and M_CP:
    bm_t, bm_a, bm_b = pullback_b1724(taus_test, 0.4, 0.8)
    bJ_t, bJ_a, bJ_b = pullback_b1724(taus_J, 0.2, 0.4)
    bS_t, bS_a, bS_b = pullback_b1724(taus_S, 0.2, 0.4)
    bC_t, bC_a, bC_b = pullback_b1724(taus_MCP, 0.4, 0.8)
    o24_m, _ = eval_b1656_fd(bm_t, bm_a, bm_b, L_test)
    o24_J, _ = eval_b1656_fd(bJ_t, bJ_a, bJ_b, L_test)
    o24_S, _ = eval_b1656_fd(bS_t, bS_a, bS_b, L_test)
    o24_C, _ = eval_b1656_fd(bC_t, bC_a, bC_b, L_test)
    err_b1656_dual = max(
        max(float(np.max(np.abs(o24_J[Lc] - o24_m[Lc]))) for Lc in L_test),
        max(float(np.max(np.abs(o24_S[Lc] - o24_m[Lc]))) for Lc in L_test),
        max(float(np.max(np.abs(o24_C[Lc] - o24_m[Lc]))) for Lc in L_test),
    )
    assert err_b1656_dual < 1e-12, f"B1656 dual symmetry error: {err_b1656_dual}"
    assert haar_err < 1e-13, f"Haar unitary basis-scrambling failed: {haar_err}"

    err_J_obs = max(float(np.max(np.abs(obs_J[Lc] - obs_m[Lc]))) for Lc in L_test)
    err_J_jcp_flip = max(float(np.max(np.abs(jcp_J[Lc] + jcp_m[Lc]))) for Lc in L_test)
    err_S_obs = max(float(np.max(np.abs(obs_S[Lc] - obs_m[Lc]))) for Lc in L_test)
    err_S_jcp_same = max(float(np.max(np.abs(jcp_S[Lc] - jcp_m[Lc]))) for Lc in L_test)
    err_MCP_obs = max(float(np.max(np.abs(obs_cp[Lc] - obs_m[Lc]))) for Lc in L_test)
    err_MCP_jcp_flip = max(float(np.max(np.abs(jcp_cp[Lc] + jcp_m[Lc]))) for Lc in L_test)
    max_jcp_mag = max(float(np.max(np.abs(jcp_m[Lc]))) for Lc in L_test)

    assert err_J_obs < 1e-12 and err_J_jcp_flip < 1e-14 and max_jcp_mag > 1e-7
    assert err_S_obs < 1e-12 and err_S_jcp_same < 1e-14
    assert err_MCP_obs < 1e-12 and err_MCP_jcp_flip < 1e-14

    # {L, R}^10 R-ending -> L-starting bijection under J W J^-1:
    hyp10_mats = []
    hyp10_bits = []
    for b in range(1 << 10):
        m = word_bits_to_matrix(b, 10)
        if is_allowed_mod5_p720(m) and (m[0, 0] + m[1, 1] > 2):
            hyp10_mats.append(m)
            hyp10_bits.append(b)
    mat_to_idx = {(int(m[0, 0]), int(m[0, 1]), int(m[1, 0]), int(m[1, 1])): idx for idx, m in enumerate(hyp10_mats)}
    end_R_indices, start_L_partner_indices = [], []
    for idx, b in enumerate(hyp10_bits):
        if (b & 1) == 1:
            m = hyp10_mats[idx]
            mc = J_MAT @ m @ J_INV
            end_R_indices.append(idx)
            start_L_partner_indices.append(mat_to_idx[(int(mc[0, 0]), int(mc[0, 1]), int(mc[1, 0]), int(mc[1, 1]))])

    mark_R, twin_P_mapped, jcp_mR, jcp_tP_mapped = [], [], [], []
    indep_grid_obs_diffs = []
    max_axis_geom_err = 0.0
    for ir, ip in zip(end_R_indices, start_L_partner_indices):
        ell_r, tr_pts = geodesic_axis_points(hyp10_mats[ir], n_quad=128)
        ell_p, tp_indep = geodesic_axis_points(hyp10_mats[ip], n_quad=192)
        assert abs(ell_r - ell_p) < 1e-13
        # Verify J * tr_pts lies on the exact hyperbolic axis of mc = J m J^-1:
        tp_mapped = (np.conj(tr_pts) + 1.0) / np.conj(tr_pts)
        mp, mq, mr, ms = map(float, hyp10_mats[ip].ravel())
        disc_p = math.sqrt((mp + ms) ** 2 - 4.0)
        c0_p = (mp - ms) / (2.0 * mr)
        rad_p = disc_p / (2.0 * abs(mr))
        axis_err = float(np.max(np.abs(np.abs(tp_mapped - c0_p) - rad_p)) / max(1.0, rad_p))
        max_axis_geom_err = max(max_axis_geom_err, axis_err)

        tm1, am1, bm1 = sl2z_pullback_points(tr_pts, np.full(128, 0.4), np.full(128, 0.8))
        tt1, at1, bt1 = sl2z_pullback_points(tp_mapped, np.full(128, 0.2), np.full(128, 0.4))
        tti, ati, bti = sl2z_pullback_points(tp_indep, np.full(192, 0.2), np.full(192, 0.4))
        om, jm, _, _ = eval_fd_observables_and_jarlskog(tm1, am1, bm1, [1.30])
        ot, jt, _, _ = eval_fd_observables_and_jarlskog(tt1, at1, bt1, [1.30])
        oti, _, _, _ = eval_fd_observables_and_jarlskog(tti, ati, bti, [1.30])
        mark_R.append(np.mean(om[1.30], axis=0))
        twin_P_mapped.append(np.mean(ot[1.30], axis=0))
        jcp_mR.append(np.mean(jm[1.30], axis=0))
        jcp_tP_mapped.append(np.mean(jt[1.30], axis=0))
        indep_grid_obs_diffs.append(float(np.max(np.abs(np.mean(om[1.30], axis=0) - np.mean(oti[1.30], axis=0)))))

    geo_obs_err = float(np.max(np.abs(np.array(mark_R) - np.array(twin_P_mapped))))
    geo_jcp_err = float(np.max(np.abs(np.array(jcp_mR) + np.array(jcp_tP_mapped))))
    max_indep_quad_diff = float(max(indep_grid_obs_diffs))
    assert max_axis_geom_err < 1e-13 and geo_obs_err < 5e-12 and geo_jcp_err < 5e-13 and max_indep_quad_diff < 5e-3

    return {
        "haar_unitary_basis_scrambling_max_err": haar_err,
        "pointwise_J_antiholo_obs_err": err_J_obs,
        "pointwise_J_antiholo_jcp_flip_sum_err": err_J_jcp_flip,
        "pointwise_S_holo_obs_err": err_S_obs,
        "pointwise_S_holo_jcp_same_diff_err": err_S_jcp_same,
        "pointwise_MCP_mark_stabiliser_obs_err": err_MCP_obs,
        "pointwise_MCP_mark_stabiliser_jcp_flip_sum_err": err_MCP_jcp_flip,
        "pointwise_B1656_24_max_err_J_S_MCP": err_b1656_dual,
        "pointwise_max_jarlskog_magnitude": max_jcp_mag,
        "n10_hyperbolic_allowed_count": len(hyp10_mats),
        "n10_R_ending_words_count": len(end_R_indices),
        "geodesic_J_axis_geometry_max_rel_err": max_axis_geom_err,
        "geodesic_period_mark_vs_Jpartner_twin_max_obs_err": geo_obs_err,
        "geodesic_period_mark_plus_Jpartner_twin_jarlskog_err": geo_jcp_err,
        "geodesic_indep_192node_quadrature_max_diff": max_indep_quad_diff,
    }


def eval_high_cusp_point_mpmath(
    tau_c: complex,
    la: float,
    lb: float,
    L_coords: List[float],
    fsum30_pt: Dict[str, np.ndarray],
    fu24_pt: Dict[str, np.ndarray],
) -> Tuple[Dict[float, np.ndarray], Dict[float, np.ndarray], Dict[float, np.ndarray], np.ndarray, np.ndarray, np.ndarray]:
    """Arbitrary-precision mpmath evaluation at Im(tau) > 5.0, avoiding IEEE-754 float64 1e-16 SVD rank loss."""
    yv = tau_c.imag
    mp.mp.dps = max(55, int(2.2 * yv) + 35)
    t = mp.mpc(tau_c.real, yv)
    pi = mp.pi
    j = mp.j
    m_max = max(12, int(mp.mp.dps * math.log(10.0) / (2.0 * math.pi * yv)) + 5)
    q = mp.exp(2 * j * pi * t)
    eta_prod = mp.mpf(1)
    e2_sum = mp.mpf(0)
    qp = mp.mpf(1)
    for m in range(1, m_max + 1):
        qp *= q
        eta_prod *= (1 - qp)
        e2_sum += m * qp / (1 - qp)
    e2 = 1 - 24 * e2_sum
    eta_hat = mp.exp(j * pi * mp.mpf(tau_c.real) / 12) * eta_prod
    denom_hat = 2 * pi * (eta_hat ** 3)

    n_lim = max(5, int(math.sqrt(mp.mp.dps * math.log(10.0) / (math.pi * yv))) + 3)

    def th0_dt_mp(ca: float, cb: float):
        s0 = mp.mpc(0)
        sd = mp.mpc(0)
        ca_m = mp.mpf(ca)
        cb_m = mp.mpf(cb)
        for n in range(-n_lim, n_lim + 1):
            na = n + ca_m
            term = mp.exp(j * pi * (na * na) * t + 2 * j * pi * na * cb_m)
            s0 += term
            sd += mp.mpf("0.5") * (na * na) * term
        return s0, sd

    t2, dt2 = th0_dt_mp(0.5, 0.0)
    t4, dt4 = th0_dt_mp(0.0, 0.5)
    t3, dt3 = th0_dt_mp(0.0, 0.0)
    R_v = [-(t2 * t2) / denom_hat, -(t4 * t4) / denom_hat, j * (t3 * t3) / denom_hat]
    dN_v = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2 * j * t3 * dt3 / denom_hat]
    a_S = [dN_v[i] - (e2 / 12) * R_v[i] for i in range(3)]
    a_St = [mp.conj(z) for z in a_S]

    c_pref = [-j, mp.mpf(-1), mp.mpf(-1), j]

    def th_kap_mp(al_f: float, be_f: float):
        al = mp.mpf(al_f)
        be = mp.mpf(be_f)
        ns = int(round(al_f))
        pref = mp.exp(j * pi * al * be)
        res = []
        for ca, cb, sgn in CHANNEL_THETA_AB:
            s = mp.mpc(0)
            for n in range(-n_lim, n_lim + 1):
                na = (n - ns) + mp.mpf(ca)
                s += mp.exp(j * pi * ((na + al) ** 2) * t + 2 * j * pi * na * (be + mp.mpf(cb)))
            res.append(mp.mpf(sgn) * pref * s)
        return res

    R30 = {}
    for sec, (qL, qR) in SECTOR_CHARGES.items():
        tu = th_kap_mp((qL + qR) * la, (qL + qR) * lb)
        td = th_kap_mp((qL - qR) * la, (qL - qR) * lb)
        R30[sec] = [c_pref[i] * tu[i] * td[i] / denom_hat for i in range(4)]

    def thc01_mp(af: float, bf: float):
        am = mp.mpf(af)
        bm = mp.mpf(bf)
        k0 = int(round(-af))
        k1 = int(round(-af - 0.5))
        X0 = mp.mpc(0)
        X1 = mp.mpc(0)
        for k in range(-n_lim, n_lim + 1):
            n0 = k + k0 + am
            X0 += mp.exp(2 * j * pi * t * (n0 * n0) + 2 * j * pi * n0 * bm)
            n1 = k + k1 + am
            X1 += mp.exp(2 * j * pi * t * ((n1 + mp.mpf("0.5")) ** 2) + 2 * j * pi * n1 * bm)
        return X0, X1

    R24 = {}
    for sname, ql, qr in SECT_B1656:
        ax, bx = ql * la, 2.0 * ql * lb
        ay, by = qr * la, 2.0 * qr * lb
        X0, X1 = thc01_mp(ax, bx)
        Y0, Y1 = thc01_mp(ay, by)
        Mm = [
            [X0 * Y0 / denom_hat, mp.exp(j * pi * mp.mpf(by)) * X0 * Y1 / (j * denom_hat)],
            [mp.exp(j * pi * mp.mpf(bx)) * X1 * Y0 / (j * denom_hat), -mp.exp(j * pi * mp.mpf(bx + by)) * X1 * Y1 / denom_hat],
        ]
        R24[sname] = [
            sum(mp.mpc(EC_LIST[si][r, c].real, EC_LIST[si][r, c].imag) * Mm[r][c] for r in range(2) for c in range(2))
            for si in range(4)
        ]

    def eval_30_single(Lc: float, sys_reg: bool):
        row = np.zeros(30, dtype=np.float64)
        U_l = {}
        sys_add = 2.0 * math.pi * math.log(yv) if sys_reg else 0.0
        for s_i, sec in enumerate(["u", "d", "e"]):
            f_r = fsum30_pt[sec]
            rn = [
                (4.0 * math.pi * (Lc - KRONECKER_SHIFT) + float(f_r[i]) + sys_add)
                if sys_reg
                else (4.0 * math.pi * Lc + float(f_r[i]))
                for i in range(4)
            ]
            uv4 = [R30[sec][i] / mp.sqrt(mp.mpf(max(rn[i], 1e-12))) for i in range(4)]
            u1 = uv4[0]
            uv = uv4[1:4]
            for r_tag, av, off in [("S", a_S, 0), ("S~", a_St, 6)]:
                dot = av[0] * uv[0] + av[1] * uv[1] + av[2] * uv[2]
                skew = [[0, -av[2], av[1]], [av[2], 0, -av[0]], [-av[1], av[0], 0]]
                Ym = mp.matrix(3, 3)
                for a in range(3):
                    for b in range(3):
                        Ym[a, b] = av[a] * uv[b] + uv[a] * av[b] - (dot if a == b else 0) - u1 * skew[a][b]
                if sec in ("u", "d"):
                    Um, svm, _ = mp.svd_c(Ym)
                    U_l[(sec, r_tag)] = np.array([[complex(Um[r, 2 - c]) for c in range(3)] for r in range(3)], dtype=np.complex128)
                else:
                    svm = mp.svd_c(Ym, compute_uv=False)
                s0 = svm[0]
                row[off + 2 * s_i] = float(svm[2] / s0) if s0 > 0 else 0.0
                row[off + 2 * s_i + 1] = float(svm[1] / s0) if s0 > 0 else 0.0
        UuH = U_l[("u", "S~")].conj().T
        VS = UuH @ U_l[("d", "S")]
        VSt = UuH @ U_l[("d", "S~")]
        row[12:21] = np.abs(VS).ravel()
        row[21:30] = np.abs(VSt).ravel()
        jv = np.array([
            float(np.imag(VS[0, 1] * VS[1, 2] * np.conj(VS[0, 2]) * np.conj(VS[1, 1]))),
            float(np.imag(VSt[0, 1] * VSt[1, 2] * np.conj(VSt[0, 2]) * np.conj(VSt[1, 1]))),
        ], dtype=np.float64)
        return row, jv

    def eval_24_single(Lc: float, sys_reg: bool):
        row24 = np.zeros(24, dtype=np.float64)
        U_st = {}
        col = 0
        shift_c = 2.0 * math.pi * (Lc - KRONECKER_SHIFT)
        sys_add = math.pi * math.log(yv) if sys_reg else 0.0
        for sname, _, _ in SECT_B1656:
            fus = fu24_pt[sname]
            uch = [
                mp.sqrt(mp.mpf(max(shift_c + float(fus[si]) + sys_add, 1e-12))) * R24[sname][si]
                if math.isfinite(float(fus[si]))
                else mp.mpc(0)
                for si in range(4)
            ]
            for rn, c3v, coup in [("S", a_S, COUP_S), ("St", a_St, COUP_ST)]:
                Ym = mp.matrix(3, 3)
                for a in range(3):
                    for b in range(3):
                        s = mp.mpc(0)
                        for qi in range(3):
                            for si in range(4):
                                cc = coup[qi, si, a, b]
                                if cc != 0:
                                    s += c3v[qi] * uch[si] * mp.mpc(cc.real, cc.imag)
                        Ym[a, b] = s
                if sname in ("up", "down"):
                    Um, svm, _ = mp.svd_c(Ym)
                    U_st[(sname, rn)] = np.array([[complex(Um[r, 2 - c]) for c in range(3)] for r in range(3)], dtype=np.complex128)
                else:
                    svm = mp.svd_c(Ym, compute_uv=False)
                s0 = svm[0]
                row24[col] = float(svm[1] / s0) if s0 > 0 else 0.0
                row24[col + 1] = float(svm[2] / s0) if s0 > 0 else 0.0
                col += 2
        for ru in ("S", "St"):
            for rd in ("S", "St"):
                V = np.abs(U_st[("up", ru)].conj().T @ U_st[("down", rd)])
                row24[col:col + 3] = [V[0, 1], V[1, 2], V[0, 2]]
                col += 3
        return row24

    o30_pt, j30_pt, o24_pt = {}, {}, {}
    for Lc in L_coords:
        r30, jv = eval_30_single(Lc, False)
        o30_pt[Lc] = r30
        j30_pt[Lc] = jv
        o24_pt[Lc] = eval_24_single(Lc, False)
    o30_s_pt, j30_s_pt = eval_30_single(KRONECKER_SHIFT, True)
    o24_s_pt = eval_24_single(KRONECKER_SHIFT, True)
    return o30_pt, j30_pt, o24_pt, o30_s_pt, j30_s_pt, o24_s_pt


def _integrate_coset_worker(args: tuple) -> tuple:
    pa, pb, taus_f1, weights_f1, L_coords = args
    la_f = pa / 5.0
    lb_f = pb / 5.0
    la = np.full(len(taus_f1), la_f)
    lb = np.full(len(taus_f1), lb_f)
    o30, j30, cl30, _ = eval_fd_observables_and_jarlskog(taus_f1, la, lb, L_coords, systole_reg=False, clamp_floor=True)
    o24, cl24 = eval_b1656_fd(taus_f1, la, lb, L_coords, systole_reg=False)
    o30_s, j30_s, cl30_s, _ = eval_fd_observables_and_jarlskog(
        taus_f1, la, lb, [KRONECKER_SHIFT], systole_reg=True, clamp_floor=False
    )
    o24_s, cl24_s = eval_b1656_fd(taus_f1, la, lb, [KRONECKER_SHIFT], systole_reg=True)

    y_thresh = 5.5 if pa == 0 else 15.0
    high_idx = np.where(taus_f1.imag > y_thresh)[0]
    if len(high_idx) > 0:
        t_hi = taus_f1[high_idx]
        la_hi = np.full(len(t_hi), la_f)
        lb_hi = np.full(len(t_hi), lb_f)
        fsum30_hi = {
            sec: np.column_stack([
                kronecker_Fu_vec(((qL + qR) * la_hi + s1) % 1.0, ((qL + qR) * lb_hi + s2) % 1.0, t_hi)
                + kronecker_Fu_vec(((qL - qR) * la_hi + s1) % 1.0, ((qL - qR) * lb_hi + s2) % 1.0, t_hi)
                for s1, s2 in CHANNEL_SHIFTS
            ])
            for sec, (qL, qR) in SECTOR_CHARGES.items()
        }
        fu24_hi = {
            sname: np.column_stack([
                kronecker_Fu_vec((ql + qr) * la_hi + d1, (ql + qr) * lb_hi + d2, t_hi, zero_to_inf=True)
                for d1, d2 in CHAR_SHIFTS_B1656
            ])
            for sname, ql, qr in SECT_B1656
        }
        for loc_i, gi in enumerate(high_idx):
            f30_pt = {sec: fsum30_hi[sec][loc_i] for sec in fsum30_hi}
            f24_pt = {sname: fu24_hi[sname][loc_i] for sname in fu24_hi}
            r30_d, j30_d, r24_d, r30_s_pt, j30_s_pt, r24_s_pt = eval_high_cusp_point_mpmath(
                complex(taus_f1[gi]), la_f, lb_f, L_coords, f30_pt, f24_pt
            )
            for Lc in L_coords:
                o30[Lc][gi] = r30_d[Lc]
                j30[Lc][gi] = j30_d[Lc]
                o24[Lc][gi] = r24_d[Lc]
            o30_s[KRONECKER_SHIFT][gi] = r30_s_pt
            j30_s[KRONECKER_SHIFT][gi] = j30_s_pt
            o24_s[KRONECKER_SHIFT][gi] = r24_s_pt

    c_acc30 = {Lc: (weights_f1 @ o30[Lc]) / 12.0 for Lc in L_coords}
    c_jcp_sig = {Lc: (weights_f1 @ j30[Lc]) / 12.0 for Lc in L_coords}
    c_jcp_abs = {Lc: (weights_f1 @ np.abs(j30[Lc])) / 12.0 for Lc in L_coords}
    c_acc24 = {Lc: (weights_f1 @ o24[Lc]) / 12.0 for Lc in L_coords}
    c_clamp24 = {Lc: cl24[Lc] / 12.0 for Lc in L_coords}
    c_clamp30 = {Lc: cl30[Lc] / 12.0 for Lc in L_coords}
    c_acc30_s = (weights_f1 @ o30_s[KRONECKER_SHIFT]) / 12.0
    c_acc24_s = (weights_f1 @ o24_s[KRONECKER_SHIFT]) / 12.0
    c_clamp30_s = cl30_s[KRONECKER_SHIFT] / 12.0
    c_clamp24_s = cl24_s[KRONECKER_SHIFT] / 12.0
    c_jcp_s_sig = (weights_f1 @ j30_s[KRONECKER_SHIFT]) / 12.0
    c_jcp_s_abs = (weights_f1 @ np.abs(j30_s[KRONECKER_SHIFT])) / 12.0
    return (
        c_acc30, c_jcp_sig, c_jcp_abs, c_acc24, c_clamp24, c_clamp30,
        c_acc30_s, c_acc24_s, c_clamp30_s, c_clamp24_s, c_jcp_s_sig, c_jcp_s_abs,
    )


def verify_part2_cusps_and_both_hyperbolic_readouts(L_coords: List[float]) -> dict:
    proj_reps: List[Tuple[int, int]] = []
    seen = set()
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            rep = min((a, b), ((-a) % 5, (-b) % 5))
            if rep not in seen:
                seen.add(rep)
                proj_reps.append(rep)
    assert len(proj_reps) == 12
    rep_to_id = {r: i for i, r in enumerate(proj_reps)}

    visited = [False] * 12
    cusp_widths: List[int] = []
    for i in range(12):
        if visited[i]:
            continue
        cur = i
        w = 0
        while not visited[cur]:
            visited[cur] = True
            ca, cb = proj_reps[cur]
            cur = rep_to_id[min((ca % 5, (ca + cb) % 5), ((-ca) % 5, (-(ca + cb)) % 5))]
            w += 1
        cusp_widths.append(w)
    cusp_widths.sort(reverse=True)
    assert cusp_widths == [5, 5, 1, 1]

    # Verify < 1e-13 overlap agreement between numpy bulk and mpmath cusp evaluator at Im(tau) = 4.8:
    t_ov = np.array([0.17 + 4.8j])
    o30_ov_np, j30_ov_np, _, _ = eval_fd_observables_and_jarlskog(t_ov, np.array([0.4]), np.array([0.8]), [1.30])
    o24_ov_np, _ = eval_b1656_fd(t_ov, np.array([0.4]), np.array([0.8]), [1.30])
    f30_ov = {
        sec: np.array([
            float(
                kronecker_Fu_vec(np.array([((qL + qR) * 0.4 + s1) % 1.0]), np.array([((qL + qR) * 0.8 + s2) % 1.0]), t_ov)[0]
                + kronecker_Fu_vec(np.array([((qL - qR) * 0.4 + s1) % 1.0]), np.array([((qL - qR) * 0.8 + s2) % 1.0]), t_ov)[0]
            )
            for s1, s2 in CHANNEL_SHIFTS
        ])
        for sec, (qL, qR) in SECTOR_CHARGES.items()
    }
    f24_ov = {
        sname: np.array([
            float(kronecker_Fu_vec(np.array([(ql + qr) * 0.4 + d1]), np.array([(ql + qr) * 0.8 + d2]), t_ov, zero_to_inf=True)[0])
            for d1, d2 in CHAR_SHIFTS_B1656
        ])
        for sname, ql, qr in SECT_B1656
    }
    o30_ov_mp, j30_ov_mp, o24_ov_mp, _, _, _ = eval_high_cusp_point_mpmath(0.17 + 4.8j, 0.4, 0.8, [1.30], f30_ov, f24_ov)
    mp_np_overlap_err = max(
        float(np.max(np.abs(o30_ov_mp[1.30] - o30_ov_np[1.30][0]))),
        float(np.max(np.abs(j30_ov_mp[1.30] - j30_ov_np[1.30][0]))),
        float(np.max(np.abs(o24_ov_mp[1.30] - o24_ov_np[1.30][0]))),
    )
    assert mp_np_overlap_err < 1e-12

    def integrate_both_frames(nx: int, nu: int):
        gx, wx = leggauss(nx)
        gu, wu = leggauss(nu)
        X_g, U_g = np.meshgrid(0.5 * gx, 0.5 * (gu + 1.0), indexing="ij")
        WX_g, WU_g = np.meshgrid(0.5 * wx, 0.5 * wu, indexing="ij")
        y0 = np.sqrt(1.0 - X_g * X_g)
        taus_f1 = (X_g + 1j * (y0 / U_g)).ravel()
        weights_f1 = ((3.0 / math.pi) * (WX_g * WU_g) / y0).ravel()
        assert abs(float(np.sum(weights_f1)) - 1.0) < 1e-12

        acc30 = {Lc: np.zeros(30, dtype=np.float64) for Lc in L_coords}
        acc_jcp_signed = {Lc: np.zeros(2, dtype=np.float64) for Lc in L_coords}
        acc_jcp_abs = {Lc: np.zeros(2, dtype=np.float64) for Lc in L_coords}
        acc24 = {Lc: np.zeros(24, dtype=np.float64) for Lc in L_coords}
        clamp24 = {Lc: 0.0 for Lc in L_coords}
        clamp30 = {Lc: 0.0 for Lc in L_coords}

        acc30_sys0 = np.zeros(30, dtype=np.float64)
        acc24_sys0 = np.zeros(24, dtype=np.float64)
        clamp30_sys0 = 0.0
        clamp24_sys0 = 0.0
        jcp_sys0_sig = np.zeros(2, dtype=np.float64)
        jcp_sys0_abs = np.zeros(2, dtype=np.float64)

        with ProcessPoolExecutor(max_workers=12) as pool:
            coset_results = list(pool.map(_integrate_coset_worker, [(pa, pb, taus_f1, weights_f1, L_coords) for pa, pb in proj_reps]))

        for (
            c_acc30, c_jcp_sig, c_jcp_abs, c_acc24, c_clamp24, c_clamp30,
            c_acc30_s, c_acc24_s, c_clamp30_s, c_clamp24_s, c_jcp_s_sig, c_jcp_s_abs,
        ) in coset_results:
            for Lc in L_coords:
                acc30[Lc] += c_acc30[Lc]
                acc_jcp_signed[Lc] += c_jcp_sig[Lc]
                acc_jcp_abs[Lc] += c_jcp_abs[Lc]
                acc24[Lc] += c_acc24[Lc]
                clamp24[Lc] += c_clamp24[Lc]
                clamp30[Lc] += c_clamp30[Lc]
            acc30_sys0 += c_acc30_s
            acc24_sys0 += c_acc24_s
            clamp30_sys0 += c_clamp30_s
            clamp24_sys0 += c_clamp24_s
            jcp_sys0_sig += c_jcp_s_sig
            jcp_sys0_abs += c_jcp_s_abs

        return (
            acc30, acc_jcp_signed, acc_jcp_abs, acc24, clamp24, clamp30,
            acc30_sys0, acc24_sys0, clamp30_sys0, clamp24_sys0, jcp_sys0_sig, jcp_sys0_abs,
        )

    a30_24, _, _, a24_24, _, _, a30_s24, a24_s24, _, _, _, _ = integrate_both_frames(20, 24)
    (
        a30_36, jcp_sig, jcp_abs, a24_36, clamp24_36, clamp30_36,
        a30_s36, a24_s36, clamp30_s36, clamp24_s36, jcp_s_sig, jcp_s_abs,
    ) = integrate_both_frames(30, 36)

    quad_err_30 = max(float(np.max(np.abs(a30_36[Lc] - a30_24[Lc]))) for Lc in L_coords)
    quad_err_24 = max(float(np.max(np.abs(a24_36[Lc] - a24_24[Lc]))) for Lc in L_coords)
    quad_err_30_sys0 = float(np.max(np.abs(a30_s36 - a30_s24)))
    quad_err_24_sys0 = float(np.max(np.abs(a24_s36 - a24_s24)))
    assert quad_err_30 < 5e-3 and quad_err_24 < 5e-3
    assert quad_err_30_sys0 < 2e-3 and quad_err_24_sys0 < 2e-3
    assert clamp30_s36 == 0.0 and clamp24_s36 == 0.0

    max_signed_jcp_hyp = max(
        max(float(np.max(np.abs(jcp_sig[Lc]))) for Lc in L_coords),
        float(np.max(np.abs(jcp_s_sig))),
    )
    min_abs_jcp_hyp = min(
        min(float(np.min(jcp_abs[Lc])) for Lc in L_coords),
        float(np.min(jcp_s_abs)),
    )
    assert max_signed_jcp_hyp < 1e-14 and min_abs_jcp_hyp > 1e-6

    return {
        "cusp_count": 4,
        "cusp_widths": cusp_widths,
        "hyperbolic_area_4pi": 4.0 * math.pi,
        "quad_err_area_norm_frame30": quad_err_30,
        "quad_err_area_norm_b1656_24": quad_err_24,
        "quad_err_systole_L0_frame30": quad_err_30_sys0,
        "quad_err_systole_L0_b1656_24": quad_err_24_sys0,
        "whole_weave_signed_J_CP_max_abs": max_signed_jcp_hyp,
        "whole_weave_abs_J_CP_at_L_tilde_0": [float(x) for x in jcp_abs[KRONECKER_SHIFT]],
        "whole_weave_abs_J_CP_at_L_tilde_sys_0": [float(x) for x in jcp_s_abs],
        "b1656_active_channel_clamp_share_on_F1_grid": {f"{Lc:.5f}": clamp24_36[Lc] for Lc in L_coords},
        "frame30_channel_clamp_share_on_F1_grid": {f"{Lc:.5f}": clamp30_36[Lc] for Lc in L_coords},
        "systole_L0_clamp_share_b1656_and_frame30": [clamp24_s36, clamp30_s36],
        "hyperbolic_area_b_frame30": {
            **{f"{Lc:.5f}": {OBS30_NAMES[i]: float(a30_36[Lc][i]) for i in range(30)} for Lc in L_coords},
            "L_tilde_sys=0": {OBS30_NAMES[i]: float(a30_s36[i]) for i in range(30)},
        },
        "hyperbolic_area_b_b1656_24": {
            **{f"{Lc:.5f}": {OBS24_NAMES[i]: float(a24_36[Lc][i]) for i in range(24)} for Lc in L_coords},
            "L_tilde_sys=0": {OBS24_NAMES[i]: float(a24_s36[i]) for i in range(24)},
        },
        "raw30": a30_36,
        "raw24": a24_36,
        "raw30_sys0": a30_s36,
        "raw24_sys0": a24_s36,
    }


def run_planted_controls() -> dict:
    # CTL-OWN1-1: Forgetting complex conjugation in det(J) = -1:
    # (a) Raw (tau + 1)/tau has Im < 0 (leaves upper half-plane H completely);
    # (b) Even flipping sign to (-tau - 1)/tau (det = +1 on H) breaks mark-twin equality by O(1):
    tau0 = np.array([0.19 + 0.94j])
    tau_raw_holo = (tau0 + 1.0) / tau0
    leaves_upper_half_plane = bool(float(tau_raw_holo[0].imag) < 0.0)
    tau_wrong_holo_H = (-tau0 - 1.0) / tau0
    tm, am, bm = sl2z_pullback_points(tau0, np.array([0.4]), np.array([0.8]))
    tw, aw, bw = sl2z_pullback_points(tau_wrong_holo_H, np.array([0.2]), np.array([0.4]))
    om, _, _, _ = eval_fd_observables_and_jarlskog(tm, am, bm, [1.30])
    ow, _, _, _ = eval_fd_observables_and_jarlskog(tw, aw, bw, [1.30])
    holo_err = float(np.max(np.abs(ow[1.30] - om[1.30])))
    ctl1_caught = bool(leaves_upper_half_plane and holo_err > 1e-2)

    # CTL-OWN1-2: Unbounded -ln(m_u / m_t) integral diverges linearly with ln(Y_cut) in width-5 cusp
    # (integrated over fixed dyadic shells [y0(x), 4], [4, 8], [8, 16], [16, 32] in u = 1/y):
    def eval_u_mu_mt_sys0_mp(tau_c: complex, f_u_pt: np.ndarray) -> float:
        yv = tau_c.imag
        mp.mp.dps = max(55, int(2.2 * yv) + 30)
        t = mp.mpc(tau_c.real, yv)
        pi, j = mp.pi, mp.j
        q = mp.exp(2 * j * pi * t)
        eta_prod, e2_sum, qp = mp.mpf(1), mp.mpf(0), mp.mpf(1)
        for m in range(1, 14):
            qp *= q
            eta_prod *= (1 - qp)
            e2_sum += m * qp / (1 - qp)
        e2 = 1 - 24 * e2_sum
        denom_hat = 2 * pi * ((mp.exp(j * pi * mp.mpf(tau_c.real) / 12) * eta_prod) ** 3)

        def th0_dt(ca: float, cb: float):
            s0, sd = mp.mpc(0), mp.mpc(0)
            for n in range(-6, 7):
                na = n + mp.mpf(ca)
                term = mp.exp(j * pi * (na * na) * t + 2 * j * pi * na * mp.mpf(cb))
                s0 += term
                sd += mp.mpf("0.5") * (na * na) * term
            return s0, sd

        t2, dt2 = th0_dt(0.5, 0.0)
        t4, dt4 = th0_dt(0.0, 0.5)
        t3, dt3 = th0_dt(0.0, 0.0)
        R_v = [-(t2 * t2) / denom_hat, -(t4 * t4) / denom_hat, j * (t3 * t3) / denom_hat]
        dN_v = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2 * j * t3 * dt3 / denom_hat]
        av = [dN_v[i] - (e2 / 12) * R_v[i] for i in range(3)]

        def th_kap(al_f: float, be_f: float):
            al, be, ns = mp.mpf(al_f), mp.mpf(be_f), int(round(al_f))
            pref = mp.exp(j * pi * al * be)
            out = []
            for ca, cb, sgn in CHANNEL_THETA_AB:
                s = mp.mpc(0)
                for n in range(-6, 7):
                    na = (n - ns) + mp.mpf(ca)
                    s += mp.exp(j * pi * ((na + al) ** 2) * t + 2 * j * pi * na * (be + mp.mpf(cb)))
                out.append(mp.mpf(sgn) * pref * s)
            return out

        qL_u, qR_u = SECTOR_CHARGES["u"]
        tu = th_kap((qL_u + qR_u) * 0.2, 0.0)
        td = th_kap((qL_u - qR_u) * 0.2, 0.0)
        c_pref = [-j, mp.mpf(-1), mp.mpf(-1), j]
        sys_add = 2.0 * math.pi * math.log(yv)
        uv4 = [
            (c_pref[i] * tu[i] * td[i] / denom_hat) / mp.sqrt(mp.mpf(max(float(f_u_pt[i]) + sys_add, 1e-12)))
            for i in range(4)
        ]
        u1, uv = uv4[0], uv4[1:4]
        dot = av[0] * uv[0] + av[1] * uv[1] + av[2] * uv[2]
        skew = [[0, -av[2], av[1]], [av[2], 0, -av[0]], [-av[1], av[0], 0]]
        Ym = mp.matrix(3, 3)
        for a in range(3):
            for b in range(3):
                Ym[a, b] = av[a] * uv[b] + uv[a] * av[b] - (dot if a == b else 0) - u1 * skew[a][b]
        svm = mp.svd_c(Ym, compute_uv=False)
        return float(svm[2] / svm[0]) if svm[0] > 0 else 0.0

    gx, wx = leggauss(16)
    gu, wu = leggauss(16)
    X_g, S_g = np.meshgrid(0.5 * gx, 0.5 * (gu + 1.0), indexing="ij")
    WX_g, WS_g = np.meshgrid(0.5 * wx, 0.5 * wu, indexing="ij")
    Y_cuts = [4.0, 8.0, 16.0, 32.0]
    shell_bounds = [(None, 4.0), (4.0, 8.0), (8.0, 16.0), (16.0, 32.0)]
    qL_u, qR_u = SECTOR_CHARGES["u"]
    cum_ratio = 0.0
    cum_log = 0.0
    ratio_means, log_means = [], []
    for y_lo_bound, y_hi_bound in shell_bounds:
        u_lo = np.full_like(X_g, 1.0 / y_hi_bound)
        u_hi = (1.0 / np.sqrt(1.0 - X_g * X_g)) if y_lo_bound is None else np.full_like(X_g, 1.0 / y_lo_bound)
        U_g = u_lo + (u_hi - u_lo) * S_g
        W_g = (3.0 / math.pi) * WX_g * WS_g * (u_hi - u_lo)
        t_f = (X_g + 1j / U_g).ravel()
        w_f = W_g.ravel()
        if y_hi_bound <= 8.0:
            la_c = np.full(len(t_f), 0.2)
            lb_c = np.zeros(len(t_f))
            obs_c, _, _, _ = eval_fd_observables_and_jarlskog(
                t_f, la_c, lb_c, [KRONECKER_SHIFT], systole_reg=True, clamp_floor=False
            )
            r_mu_mt = obs_c[KRONECKER_SHIFT][:, 0].copy()
        else:
            la_c = np.full(len(t_f), 0.2)
            lb_c = np.zeros(len(t_f))
            f_u_shell = np.column_stack([
                kronecker_Fu_vec(((qL_u + qR_u) * la_c + s1) % 1.0, ((qL_u + qR_u) * lb_c + s2) % 1.0, t_f)
                + kronecker_Fu_vec(((qL_u - qR_u) * la_c + s1) % 1.0, ((qL_u - qR_u) * lb_c + s2) % 1.0, t_f)
                for s1, s2 in CHANNEL_SHIFTS
            ])
            r_mu_mt = np.array([eval_u_mu_mt_sys0_mp(complex(t_f[i]), f_u_shell[i]) for i in range(len(t_f))], dtype=np.float64)
        r_mu_mt = np.maximum(r_mu_mt, 1e-300)
        cum_ratio += float(w_f @ r_mu_mt)
        cum_log += float(w_f @ (-np.log(r_mu_mt)))
        ratio_means.append(cum_ratio)
        log_means.append(cum_log)

    step1 = log_means[1] - log_means[0]
    step2 = log_means[2] - log_means[1]
    step3 = log_means[3] - log_means[2]
    richardson_slope = 2.0 * step3 - step2
    exact_asymptotic_step = 3.6 * math.log(2.0)  # (3/pi) * (6*pi/5) * ln(2) = (18/5) ln(2)
    ratio_tail_drift = abs(ratio_means[3] - ratio_means[2])
    ctl2_caught = bool(
        step1 > 1.9
        and step2 > 2.2
        and step3 > 2.3
        and abs(richardson_slope - exact_asymptotic_step) < 1e-3
        and ratio_tail_drift < 1e-10
    )

    # CTL-OWN1-3: Width-5 cusp degeneration trap on constant L_coord = 2.20 vs global positivity of F_u^sys:
    high_cusp_tau = np.array([0.0 + 50.0j])
    fu_high_raw = float(kronecker_Fu_vec(np.array([0.4]), np.array([0.8]), high_cusp_tau)[0])
    val_at_2p20_y50 = 2.0 * math.pi * (2.20 - KRONECKER_SHIFT) + fu_high_raw

    xs = np.linspace(-0.5, 0.5, 41)
    us = np.linspace(1e-4, 1.0, 50)
    Xg, Ug = np.meshgrid(xs, us)
    taus_grid = (Xg + 1j * (np.sqrt(1.0 - Xg * Xg) / Ug)).ravel()
    yg = taus_grid.imag
    min_fu_sys_99 = float("inf")
    for k1 in range(10):
        for k2 in range(10):
            if k1 == 0 and k2 == 0:
                continue
            arr = kronecker_Fu_vec(np.full(len(taus_grid), k1 / 10.0), np.full(len(taus_grid), k2 / 10.0), taus_grid)
            min_fu_sys_99 = min(min_fu_sys_99, float(np.min(arr + math.pi * np.log(yg))))

    ctl3_caught = bool(val_at_2p20_y50 < 0.0 and min_fu_sys_99 > 6.9)

    assert ctl1_caught and ctl2_caught and ctl3_caught
    return {
        "CTL_OWN1_1_wrong_holomorphic_J_err": holo_err,
        "CTL_OWN1_1_caught": ctl1_caught,
        "CTL_OWN1_2_Y_cuts": Y_cuts,
        "CTL_OWN1_2_bounded_ratio_integrals": ratio_means,
        "CTL_OWN1_2_divergent_neg_log_integrals": log_means,
        "CTL_OWN1_2_doubling_steps_ln2": [step1, step2, step3],
        "CTL_OWN1_2_richardson_asymptotic_step": richardson_slope,
        "CTL_OWN1_2_exact_18_over_5_ln2": exact_asymptotic_step,
        "CTL_OWN1_2_caught": ctl2_caught,
        "CTL_OWN1_3_val_at_L2p20_y50_width5_cusp": val_at_2p20_y50,
        "CTL_OWN1_3_min_Fu_sys_across_all_99_tenth_torsion_on_F1": min_fu_sys_99,
        "CTL_OWN1_3_caught": ctl3_caught,
    }


def main() -> None:
    t0 = time.time()
    L_COORDS = [0.90, 1.30, KRONECKER_SHIFT, 2.20]
    print("=== AGY-002 OWN CARD A2-OWN1: DUAL TWIN SYMMETRIES, CP PARITY, 4-CUSP INTEGRABILITY, L_SYS=0, & (a) VS (b) ===")
    print(f"L_coord ends: {[round(x, 6) for x in L_COORDS]} (where {KRONECKER_SHIFT:.6f} is L_tilde == 0), plus systole L_tilde_sys == 0")

    print("\n[1/4] Theorem 1: Dual Twin Involutions (J vs S), Haar basis-scrambling, & Mark CP Parity M_CP...")
    part1 = verify_part1_dual_twin_and_cp_parity()
    for k, v in part1.items():
        print(f"  {k}: {v}")

    print("\n[2/4] Theorem 2: 4 cusps [5,5,1,1] & Hyperbolic-Area Read-Out (b) in BOTH B1656-24 and P720-30 frames...")
    part2 = verify_part2_cusps_and_both_hyperbolic_readouts(L_COORDS)
    raw30 = part2.pop("raw30")
    raw24 = part2.pop("raw24")
    raw30_sys0 = part2.pop("raw30_sys0")
    raw24_sys0 = part2.pop("raw24_sys0")
    print(f"  Cusps: {part2['cusp_widths']} (sum=12, Area={part2['hyperbolic_area_4pi']:.6f})")
    print(f"  Quadrature (20x24 vs 30x36) area-norm: frame30={part2['quad_err_area_norm_frame30']:.3e}, b1656_24={part2['quad_err_area_norm_b1656_24']:.3e}")
    print(f"  Quadrature (20x24 vs 30x36) systole L_tilde_sys=0: frame30={part2['quad_err_systole_L0_frame30']:.3e}, b1656_24={part2['quad_err_systole_L0_b1656_24']:.3e}")
    print(f"  Whole-weave signed <J_CP>_hyp max = {part2['whole_weave_signed_J_CP_max_abs']:.3e} (exact zero!)")
    print(f"  Whole-weave <|J_CP|>_hyp: area L_tilde=0 -> {part2['whole_weave_abs_J_CP_at_L_tilde_0']}, systole L_tilde_sys=0 -> {part2['whole_weave_abs_J_CP_at_L_tilde_sys_0']}")
    print(f"  Area-norm B1656 clamp share on F1 grid: {part2['b1656_active_channel_clamp_share_on_F1_grid']}")
    print(f"  Systole L_tilde_sys=0 clamp share [B1656-24, Frame30]: {part2['systole_L0_clamp_share_b1656_and_frame30']} (EXACT ZERO!)")

    print("\n[3/4] Theorem 3: Exact B1656 Bernoulli Word-Weight (a) vs Intrinsic Hyperbolic-Area Weight (b)...")
    # Exact B1656 word convention matching reconcile_b1924_exact_b1656.py bit-for-bit (345 hyperbolic words at n = 12):
    hyp12_mats = []
    for bits in range(1 << 12):
        W = word_bits_to_matrix(bits, 12)
        u0 = int((W[0, 0] + 2 * W[0, 1]) % 5)
        u1 = int((W[1, 0] + 2 * W[1, 1]) % 5)
        if ((u0 == 1 and u1 == 2) or (u0 == 4 and u1 == 3)) and (W[0, 0] + W[1, 1] > 2):
            hyp12_mats.append(W)
    assert len(hyp12_mats) == 345

    lens12 = np.zeros(len(hyp12_mats))
    vals12_24 = {Lc: np.zeros((len(hyp12_mats), 24)) for Lc in L_COORDS}
    vals12_24_sys0 = np.zeros((len(hyp12_mats), 24))
    for idx, W_mat in enumerate(hyp12_mats):
        ell, tpts = geodesic_midpoint_taus(W_mat, density=32.0, min_nodes=64)
        lens12[idx] = ell
        tf, af, bf = pullback_b1724(tpts, 0.4, 0.8)
        o24, _ = eval_b1656_fd(tf, af, bf, L_COORDS, systole_reg=False)
        for Lc in L_COORDS:
            vals12_24[Lc][idx] = np.mean(o24[Lc], axis=0)
        o24_s, _ = eval_b1656_fd(tf, af, bf, [KRONECKER_SHIFT], systole_reg=True)
        vals12_24_sys0[idx] = np.mean(o24_s[KRONECKER_SHIFT], axis=0)

    w12 = lens12 / np.sum(lens12)
    b1656_a_vs_b = {}
    rec_json_path = OUT_DIR.parent / "a2_b1924" / "reconcile_b1924_exact_b1656_results.json"
    rec_data = json.loads(rec_json_path.read_text(encoding="utf-8")) if rec_json_path.exists() else None

    for Lc in L_COORDS:
        mean_a12 = w12 @ vals12_24[Lc]
        mean_b24 = raw24[Lc]
        diff12 = mean_a12 - mean_b24
        entry = {
            "n12_exact_pop_345_max_abs_a_minus_b": float(np.max(np.abs(diff12))),
            "observables_n12_pop_vs_hyp_b": {
                OBS24_NAMES[i]: {
                    "bernoulli_a_n12_exact": float(mean_a12[i]),
                    "hyperbolic_area_b": float(mean_b24[i]),
                    "a_minus_b": float(diff12[i]),
                }
                for i in range(24)
            },
        }
        key_rec = str(round(Lc, 2)) if round(Lc, 2) in (0.9, 1.3, 2.2) else None
        if rec_data is not None and key_rec is not None:
            pop12_ref = np.array(rec_data["exhaustive_populations"]["12"]["R_exact_population"][key_rec])
            cross_err12 = float(np.max(np.abs(mean_a12 - pop12_ref)))
            # Small < 2e-4 difference at Lc=0.90 only if max(val, 1e-12) vs max(val, 0.0) triggers; at 1.30/2.20 < 1e-6:
            entry["n12_cross_check_vs_a2_b1924_max_diff"] = cross_err12
            pop16 = np.array(rec_data["exhaustive_populations"]["16"]["R_exact_population"][key_rec])
            s22_m = np.array(rec_data["sampled_400w_without_replacement"]["22"]["by_L_coord"][key_rec]["mark_mean"])
            s22_se = np.array(rec_data["sampled_400w_without_replacement"]["22"]["by_L_coord"][key_rec]["mark_se"])
            s28_m = np.array(rec_data["sampled_400w_without_replacement"]["28"]["by_L_coord"][key_rec]["mark_mean"])
            s28_se = np.array(rec_data["sampled_400w_without_replacement"]["28"]["by_L_coord"][key_rec]["mark_se"])
            diff16 = pop16 - mean_b24
            diff22 = s22_m - mean_b24
            z22 = np.abs(diff22) / np.maximum(s22_se, 1e-15)
            diff28 = s28_m - mean_b24
            z28 = np.abs(diff28) / np.maximum(s28_se, 1e-15)
            entry["n16_exact_pop_5453_max_abs_a_minus_b"] = float(np.max(np.abs(diff16)))
            entry["n16_exact_pop_vs_hyp_b"] = {
                OBS24_NAMES[i]: {
                    "bernoulli_a_n16_exact": float(pop16[i]),
                    "bernoulli_a_n28_sample400": float(s28_m[i]),
                    "hyperbolic_area_b": float(mean_b24[i]),
                    "a16_minus_b": float(diff16[i]),
                    "a28_minus_b": float(diff28[i]),
                    "abs_z28_vs_b": float(z28[i]),
                }
                for i in range(24)
            }
            entry["n22_sample400_max_abs_a_minus_b"] = float(np.max(np.abs(diff22)))
            entry["n22_sample400_median_z_vs_b"] = float(np.median(z22))
            entry["n28_sample400_max_abs_a_minus_b"] = float(np.max(np.abs(diff28)))
            entry["n28_sample400_median_z_vs_b"] = float(np.median(z28))
            entry["n28_sample400_max_z_vs_b"] = float(np.max(z28))
            entry["n28_sample400_share_z_gt_3"] = float(np.mean(z28 > 3.0))
            print(
                f"  B1656 L_coord={Lc:.5f}: n12_xcheck={cross_err12:.2e} | max|a16 - b|={np.max(np.abs(diff16)):.5f} | "
                f"max|a28 - b|={np.max(np.abs(diff28)):.5f} (median |z|={np.median(z28):.2f}, max |z|={np.max(z28):.2f})"
            )
        else:
            print(f"  B1656 L_coord={Lc:.5f} (area L_tilde=0): max|a12 - b|={np.max(np.abs(diff12)):.5f}")
            for show_i in [0, 1, 4, 5, 12, 13, 18, 19]:
                print(f"    {OBS24_NAMES[show_i]:16s}: (b)={mean_b24[show_i]:.6f}  vs  (a,n=12)={mean_a12[show_i]:.6f}")

        b1656_a_vs_b[f"{Lc:.5f}"] = entry

    mean_a12_sys0 = w12 @ vals12_24_sys0
    diff12_sys0 = mean_a12_sys0 - raw24_sys0
    b1656_a_vs_b["L_tilde_sys=0"] = {
        "n12_exact_pop_345_max_abs_a_minus_b": float(np.max(np.abs(diff12_sys0))),
        "observables_n12_pop_vs_hyp_b": {
            OBS24_NAMES[i]: {
                "bernoulli_a_n12_exact": float(mean_a12_sys0[i]),
                "hyperbolic_area_b": float(raw24_sys0[i]),
                "a_minus_b": float(diff12_sys0[i]),
            }
            for i in range(24)
        },
    }
    print(f"  B1656 L_tilde_sys=0 (ZERO-CLAMP SYSTOLE END): max|a12 - b|={np.max(np.abs(diff12_sys0)):.5f}")
    for show_i in [0, 1, 4, 5, 12, 13, 18, 19]:
        print(f"    {OBS24_NAMES[show_i]:16s}: (b)={raw24_sys0[show_i]:.6f}  vs  (a,n=12)={mean_a12_sys0[show_i]:.6f}")

    print("\n[4/4] Running Three Adversarial Planted Controls (CTL-OWN1-1..3)...")
    ctls = run_planted_controls()
    for k, v in ctls.items():
        print(f"  {k}: {v}")

    payload = {
        "card": "AGY-002_A2-OWN1_cusp-integrability-and-tick-involution-twin-law",
        "elapsed_sec": round(time.time() - t0, 3),
        "data_free": True,
        "L_coords_tested": L_COORDS,
        "theorem_1_dual_twin_and_cp_parity": part1,
        "theorem_2_cusps_and_hyperbolic_area_b": part2,
        "theorem_3_b1656_bernoulli_a_vs_hyperbolic_b": b1656_a_vs_b,
        "planted_controls": ctls,
    }
    out_json = OUT_DIR / "verify_a2_own1_results.json"
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"\nWrote relays/a2_own1/verify_a2_own1_results.json in {payload['elapsed_sec']:.2f}s.")
    print("0 of 19.")


if __name__ == "__main__":
    main()
