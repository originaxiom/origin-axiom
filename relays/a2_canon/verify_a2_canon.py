#!/usr/bin/env python3
"""Standalone independent computation of the whole-weave 7-value read-out (card A2-CANON-T90,
encompassing M27/M30 A2-CANON and the critical-path dispatch for tomorrow's run):
  - Canonical end L_2(tau) (B1667 / B1927), solved 100% from scratch on our own code.
  - Both Higgs worlds:
      W_minus = (up S_tilde, down S, leptons S)
      W_plus  = (up S, down S_tilde, leptons S_tilde)
  - Both channel weights:
      exact_T90  : N_s = 2*pi*L_2 + c_s - pi * |a_{0,s}|^2 * exp(-2 * L_2)   (Theorem 90's form)
      old_weight : N_s = 2*pi*L_2 + c_s                                      (comparison / B1928 canon)
  - Both whole-weave measures:
      move_count : exhaustive exact populations n = 8..18, 600-word n = 22, 28, and 2,000-word
                   40-letter 24-point ergodic integral with jackknife standard errors.
      area       : exact hyperbolic area integral (3/pi) int_F <f>_{24} dx dy / y^2 via u = 1/y
                   compactification, high-order 2D Gauss-Legendre bulk quadrature (y <= 5), and
                   dynamic arbitrary-precision mpmath SVD cusp quadrature (y > 5) avoiding both
                   O(1/Y_cut) cusp truncation bias and IEEE-754 float64 SVD singular-vector rotation.

Strict Firewall & Independence Discipline:
  - Zero code imported from main; zero measured numbers touched or compared anywhere.
  - Committed and pushed BEFORE opening B1927/canon_readout.json, B1928/fiber_ergodic_fine.json,
    or any agy-exp X-CANON output.
  - Position-only output names; zero particle names.
  - Numerical 7-value read-outs written EXCLUSIVELY to verify_a2_canon_results.json (never stdout).

0 of 19.
"""

from __future__ import annotations

import os

for _env_var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_env_var, "1")

import json
import math
import multiprocessing as mp_proc
import random
import time
from pathlib import Path
from typing import Dict, List, Tuple

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import CubicSpline, RectBivariateSpline
from scipy.special import digamma

OUT_DIR = Path(__file__).resolve().parent
EG = 0.5772156649015328606
KRONECKER_SHIFT = EG + math.log(math.pi)
L2_CUSP_LIMIT_EXACT = math.pi + math.log(math.pi) - 3.0 * math.log(2.0)
HYP_AREA_FD = math.pi / 3.0

# Position-only 24-component internal frame names (sector, reading, index) — zero particle names:
OBS24_NAMES: List[str] = [
    "up|S|r23", "up|S|r13",
    "up|St|r23", "up|St|r13",
    "down|S|r23", "down|S|r13",
    "down|St|r23", "down|St|r13",
    "lep|S|r23", "lep|S|r13",
    "lep|St|r23", "lep|St|r13",
    "mix|S|S|12", "mix|S|S|23", "mix|S|S|13",
    "mix|S|St|12", "mix|S|St|23", "mix|S|St|13",
    "mix|St|S|12", "mix|St|S|23", "mix|St|S|13",
    "mix|St|St|12", "mix|St|St|23", "mix|St|St|13",
]

# The 7 claimed read-out positions in each Higgs world:
SEVEN_POSITION_NAMES: List[str] = [
    "up_r23",
    "up_r13",
    "down_r23",
    "down_r13",
    "abs_V12",
    "abs_V23",
    "abs_V13",
]

# W_minus = (up S_tilde, down S, leptons S) -> indices in OBS24:
W_MINUS_IDX: List[int] = [2, 3, 4, 5, 18, 19, 20]
# W_plus  = (up S, down S_tilde, leptons S_tilde) -> indices in OBS24:
W_PLUS_IDX: List[int] = [0, 1, 6, 7, 15, 16, 17]

# 12 projective representatives of the 24 non-zero points of order 5 (paired with -c):
ORDER5_12_REPS: List[Tuple[float, float]] = [
    (0.0, 0.2), (0.0, 0.4),
    (0.2, 0.0), (0.2, 0.2), (0.2, 0.4), (0.2, 0.6), (0.2, 0.8),
    (0.4, 0.0), (0.4, 0.2), (0.4, 0.4), (0.4, 0.6), (0.4, 0.8),
]


# =============================================================================
# 1. STANDALONE SPECTRAL VOLTERRA PUNCTURED-TORUS UNIFORMISATION SOLVER
# =============================================================================

_SINT_CACHE: Dict[int, Tuple[np.ndarray, np.ndarray, np.ndarray]] = {}


def get_cheb_volterra(N: int = 38) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if N not in _SINT_CACHE:
        j = np.arange(N + 1, dtype=np.float64)
        theta = math.pi * j / N
        x = -np.cos(theta)
        k = np.arange(N + 1, dtype=np.float64)
        V = np.cos(np.outer(math.pi - theta, k))
        V_inv = np.linalg.inv(V)
        T_kp1 = np.cos(np.outer(math.pi - theta, np.arange(N + 2, dtype=np.float64)))
        I_mat = np.zeros((N + 1, N + 1), dtype=np.float64)
        I_mat[:, 0] = x + 1.0
        if N >= 1:
            I_mat[:, 1] = 0.5 * (x * x - 1.0)
        for m in range(2, N + 1):
            val_x = T_kp1[:, m + 1] / (2.0 * (m + 1.0)) - T_kp1[:, m - 1] / (2.0 * (m - 1.0))
            val_m1 = ((-1.0) ** (m + 1)) * (1.0 / (2.0 * (m + 1.0)) - 1.0 / (2.0 * (m - 1.0)))
            I_mat[:, m] = val_x - val_m1
        S = I_mat @ V_inv
        _SINT_CACHE[N] = (x, S, S @ S)
    return _SINT_CACHE[N]


def wp_segment_safe(z_seg: np.ndarray, tau: complex, n_terms: int = 26) -> np.ndarray:
    """Overflow-free, branch-free Weierstrass P(z; 1, tau) along a smooth segment."""
    z_arr = np.asarray(z_seg, dtype=np.complex128)
    z_mid = 0.5 * (z_arr[0] + z_arr[-1])
    m_tau = round(z_mid.imag / tau.imag)
    n_one = round((z_mid - m_tau * tau).real)
    zr = z_arr - m_tau * tau - n_one
    ns = np.arange(1, n_terms + 1, dtype=np.float64)
    q = np.exp(2j * math.pi * tau)
    qn = q ** ns
    denom = 1.0 - qn
    e2 = 1.0 - 24.0 * np.sum(ns * qn / denom)
    term_plus = np.exp(2j * math.pi * (tau + zr)[..., None] * ns)
    term_minus = np.exp(2j * math.pi * (tau - zr)[..., None] * ns)
    u = np.where(zr.imag >= 0.0, zr, -zr)
    eu = np.exp(2j * math.pi * u)
    inv_sin2 = -4.0 * (math.pi ** 2) * eu / ((1.0 - eu) ** 2)
    series = np.sum((ns / denom) * (term_plus + term_minus), axis=-1)
    return -(math.pi ** 2 / 3.0) * e2 + inv_sin2 - 4.0 * (math.pi ** 2) * series


def g2_g3_eisenstein(tau: complex, n_terms: int = 26) -> Tuple[complex, complex]:
    q = np.exp(2j * math.pi * tau)
    ns = np.arange(1, n_terms + 1, dtype=np.float64)
    qn = q ** ns
    denom = 1.0 - qn
    e4 = 1.0 + 240.0 * np.sum((ns ** 3) * qn / denom)
    e6 = 1.0 - 504.0 * np.sum((ns ** 5) * qn / denom)
    return complex((4.0 * (math.pi ** 4) / 3.0) * e4), complex((8.0 * (math.pi ** 6) / 27.0) * e6)


def frobenius_series(tau: complex, c: complex, M_frob: int = 56) -> Tuple[np.ndarray, np.ndarray]:
    g2, g3 = g2_g3_eisenstein(tau)
    laur = {1: g2 / 20.0, 2: g3 / 28.0}
    for n in range(3, M_frob // 2 + 2):
        laur[n] = (3.0 / ((2 * n + 3) * (n - 2))) * sum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
    Qc = np.zeros(M_frob + 1, dtype=np.complex128)
    Qc[0] = c
    for n in range(1, M_frob // 2 + 1):
        Qc[2 * n] = 0.25 * laur[n]
    al = np.zeros(M_frob + 1, dtype=np.complex128)
    be = np.zeros(M_frob + 1, dtype=np.complex128)
    al[0] = 1.0
    for m in range(1, M_frob + 1):
        al[m] = -sum(Qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
        be[m] = -(2.0 * m * al[m] + sum(Qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)
    return al, be


def ivp_volterra(q0_vals: np.ndarray, c: complex, dz: complex, N: int = 36, want_dc: bool = False):
    x, S, S2 = get_cheb_volterra(N)
    h = 0.5 * dz
    q_tot = q0_vals + c
    Id = np.eye(N + 1, dtype=np.complex128)
    A = Id + (h * h) * (S2 * q_tot[None, :])
    rhs = np.column_stack([np.ones(N + 1, dtype=np.complex128), (x + 1.0) * h])
    Y = np.linalg.solve(A, rhs)
    yp0 = -h * np.dot(S[N, :], q_tot * Y[:, 0])
    yp1 = 1.0 - h * np.dot(S[N, :], q_tot * Y[:, 1])
    T = np.array([[Y[N, 0], Y[N, 1]], [yp0, yp1]], dtype=np.complex128)
    if not want_dc:
        return T
    Y_dc = np.linalg.solve(A, -(h * h) * (S2 @ Y))
    dyp0 = -h * np.dot(S[N, :], Y[:, 0] + q_tot * Y_dc[:, 0])
    dyp1 = -h * np.dot(S[N, :], Y[:, 1] + q_tot * Y_dc[:, 1])
    dT = np.array([[Y_dc[N, 0], Y_dc[N, 1]], [dyp0, dyp1]], dtype=np.complex128)
    return T, dT


def const_prop(dz: complex, Q_const: complex, want_dc: bool = False):
    w = np.sqrt(Q_const + 0j)
    wz = w * dz
    if abs(wz) < 1e-6:
        wz2 = wz * wz
        c_val = 1.0 - wz2 / 2.0 + (wz2 * wz2) / 24.0
        s_over_w = dz * (1.0 - wz2 / 6.0 + (wz2 * wz2) / 120.0)
    else:
        c_val = np.cos(wz)
        s_over_w = np.sin(wz) / w
    T = np.array([[c_val, s_over_w], [-Q_const * s_over_w, c_val]], dtype=np.complex128)
    if not want_dc:
        return T
    dc_val = -0.5 * dz * s_over_w
    if abs(wz) < 1e-4:
        wz2 = wz * wz
        ds_over_w = (dz ** 3) * (-1.0 / 6.0 + wz2 / 60.0 - (wz2 * wz2) / 2520.0)
    else:
        ds_over_w = (dz * c_val - s_over_w) / (2.0 * Q_const)
    dT = np.array([[dc_val, ds_over_w], [-s_over_w - Q_const * ds_over_w, dc_val]], dtype=np.complex128)
    return T, dT


def prop_path(za: complex, zb: complex, tau: complex, c: complex, N: int = 36, want_dc: bool = False):
    y = tau.imag
    x_nodes, _, _ = get_cheb_volterra(N)
    s = 0.5 * (x_nodes + 1.0)
    q = np.exp(2j * math.pi * tau)
    ns = np.arange(1, 27, dtype=np.float64)
    qn = q ** ns
    e2 = 1.0 - 24.0 * np.sum(ns * qn / (1.0 - qn))
    Q_flat = c - ((math.pi ** 2) / 12.0) * e2
    im0, im1 = za.imag, zb.imag
    if abs(im1 - im0) < 1e-12 or y <= 12.0:
        n_sub = max(2, int(math.ceil(abs(zb - za) / 1.15)))
        ts = np.linspace(0.0, 1.0, n_sub + 1)
        segs = [(ts[k], ts[k + 1], False) for k in range(n_sub)]
    else:
        lo, hi = min(im0, im1), max(im0, im1)
        m_min = int(math.floor((lo - 5.5) / y))
        m_max = int(math.ceil((hi + 5.5) / y))
        cuts = {0.0, 1.0}
        for m in range(m_min, m_max + 1):
            for edge in (m * y - 5.5, m * y + 5.5):
                t_edge = (edge - im0) / (im1 - im0)
                if 0.0 < t_edge < 1.0:
                    cuts.add(t_edge)
        t_sorted = sorted(cuts)
        segs = []
        for t_a, t_b in zip(t_sorted[:-1], t_sorted[1:]):
            im_mid = im0 + 0.5 * (t_a + t_b) * (im1 - im0)
            if abs(im_mid - round(im_mid / y) * y) >= 5.499:
                segs.append((t_a, t_b, True))
            else:
                dz_seg = (t_b - t_a) * (zb - za)
                nsub = max(1, int(math.ceil(abs(dz_seg) / 1.15)))
                sub_ts = np.linspace(t_a, t_b, nsub + 1)
                for j in range(nsub):
                    segs.append((sub_ts[j], sub_ts[j + 1], False))
    T = np.eye(2, dtype=np.complex128)
    dT = np.zeros((2, 2), dtype=np.complex128)
    for t_a, t_b, is_flat in segs:
        z_s = za + t_a * (zb - za)
        dz_s = (t_b - t_a) * (zb - za)
        if is_flat:
            if want_dc:
                Tk, dTk = const_prop(dz_s, Q_flat, want_dc=True)
            else:
                Tk = const_prop(dz_s, Q_flat, want_dc=False)
        else:
            q0 = 0.25 * wp_segment_safe(z_s + s * dz_s, tau)
            if want_dc:
                Tk, dTk = ivp_volterra(q0, c, dz_s, N=N, want_dc=True)
            else:
                Tk = ivp_volterra(q0, c, dz_s, N=N, want_dc=False)
        if want_dc:
            dT = dTk @ T + Tk @ dT
        T = Tk @ T
    return (T, dT) if want_dc else T


def to_mobius(T: np.ndarray) -> np.ndarray:
    M = np.array([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]], dtype=np.complex128)
    return M / np.sqrt(np.linalg.det(M))


def solve_uniformisation_exact(
    tau: complex, c_init: complex = 0.0j, N: int = 36, want_lmax: bool = False
) -> Tuple[complex, float, float, float]:
    c = complex(c_init)
    z0 = 0.5 + 0.5 * tau
    for _ in range(28):
        Ta, dTa = prop_path(z0, z0 + 1.0, tau, c, N=N, want_dc=True)
        Tb, dTb = prop_path(z0, z0 + tau, tau, c, N=N, want_dc=True)
        Tab, dTab = Ta @ Tb, dTa @ Tb + Ta @ dTb
        res = np.array([np.trace(Ta).imag, np.trace(Tb).imag, np.trace(Tab).imag], dtype=np.float64)
        if np.max(np.abs(res)) < 1e-13:
            break
        df = np.array([np.trace(dTa), np.trace(dTb), np.trace(dTab)])
        step, _, _, _ = np.linalg.lstsq(np.column_stack([df.imag, df.real]), -res, rcond=None)
        c += complex(step[0], step[1])

    T_punct = Tb @ Ta @ np.linalg.inv(Tb) @ np.linalg.inv(Ta)
    Aa, Ab, P0 = to_mobius(Ta), to_mobius(Tb), to_mobius(T_punct)
    p_fix = (P0[0, 0] - P0[1, 1]) / (2.0 * P0[1, 0])
    disc_a = np.sqrt((Aa[0, 0] - Aa[1, 1]) ** 2 + 4.0 * Aa[0, 1] * Aa[1, 0])
    fa1 = (Aa[0, 0] - Aa[1, 1] + disc_a) / (2.0 * Aa[1, 0])
    fa2 = (Aa[0, 0] - Aa[1, 1] - disc_a) / (2.0 * Aa[1, 0])
    g0 = np.array([[1.0, -fa1], [1.0, -p_fix]], dtype=np.complex128)
    s_sc = (g0[0, 0] * fa2 + g0[0, 1]) / (g0[1, 0] * fa2 + g0[1, 1])
    g = np.array([[1.0 / s_sc, -fa1 / s_sc], [1.0, -p_fix]], dtype=np.complex128)
    g /= np.sqrt(np.linalg.det(g))
    if (g[0, 1] / g[1, 1]).imag < 0:
        g = np.array([[1j, 0.0], [0.0, -1j]], dtype=np.complex128) @ g
    g_inv = np.linalg.inv(g)
    Ra, Rb, RP = g @ Aa @ g_inv, g @ Ab @ g_inv, g @ P0 @ g_inv
    RP /= RP[0, 0]
    lam = abs(float(RP[0, 1].real))
    real_err = float(max(np.max(np.abs(Ra.imag)), np.max(np.abs(Rb.imag))))

    al, be = frobenius_series(tau, c, M_frob=56)
    zs = 0.05 * z0 / abs(z0)
    T_in = prop_path(z0, zs, tau, c, N=N, want_dc=False)
    zp = zs ** np.arange(len(al))
    g_loc = np.dot(be, zp) / np.dot(al, zp)
    w_zs = T_in[0, 1] / T_in[0, 0]
    u_zs = (g[0, 0] * w_zs + g[0, 1]) / (g[1, 0] * w_zs + g[1, 1])
    imB = float(u_zs.imag + (lam / (2.0 * math.pi)) * (math.log(abs(zs)) + float(g_loc.real)))
    L_2 = math.pi - (2.0 * math.pi / lam) * imB

    L_max = float("nan")
    if want_lmax:
        gens = [Ra, Rb, np.linalg.inv(Ra), np.linalg.inv(Rb)]
        inv_idx = (2, 3, 0, 1)
        mc8 = float("inf")
        front = [(np.eye(2, dtype=np.complex128), -1)]
        for _ in range(8):
            nxt = []
            for Mat, prev in front:
                for k in range(4):
                    if prev >= 0 and inv_idx[k] == prev:
                        continue
                    Nmat = Mat @ gens[k]
                    if abs(Nmat[1, 0]) > 1e-9 * max(1.0, abs(Nmat[0, 0])):
                        mc8 = min(mc8, float(abs(Nmat[1, 0])))
                    nxt.append((Nmat, k))
            front = nxt
        L_max = (2.0 * math.pi / lam) * (1.0 / mc8 - imB)

    return c, L_2, L_max, real_err


def track_exact(tau_target: complex, N_final: int = 44, want_lmax: bool = False) -> Tuple[complex, float, float, float]:
    t_cur = 1j
    c_cur = 0.0j
    y_mid = max(1.05, tau_target.imag) if tau_target.imag < 1.05 else 1.05
    for wp in (complex(tau_target.real, y_mid), complex(tau_target)):
        hyp_d = abs(wp.real - t_cur.real) / min(wp.imag, t_cur.imag)
        logy_d = abs(math.log(wp.imag / t_cur.imag))
        n_st = max(1, int(math.ceil(max(hyp_d, logy_d) / 0.16)))
        for k in range(1, n_st + 1):
            frac = k / n_st
            xk = t_cur.real + (wp.real - t_cur.real) * frac
            yk = t_cur.imag * ((wp.imag / t_cur.imag) ** frac)
            c_cur, _, _, _ = solve_uniformisation_exact(complex(xk, yk), c_cur, N=34, want_lmax=False)
        t_cur = wp
    return solve_uniformisation_exact(tau_target, c_cur, N=N_final, want_lmax=want_lmax)


class CanonicalL2Interpolant:
    """High-order 2D quintic + 1D cusp-clamped spline for L_2(tau_FD) across the entire SL(2,Z)
    fundamental domain (y in [sqrt(3)/2, +inf)), achieving ~5e-11 median / <1e-8 max error."""

    def __init__(self) -> None:
        xs_core = np.linspace(0.0, 0.5, 21)
        us_2d = np.linspace(0.18, 1.20, 39)
        L2_core = np.zeros((len(xs_core), len(us_2d)), dtype=np.float64)
        idx_u1 = int(np.argmin(np.abs(us_2d - 1.0)))
        c_row = np.zeros(len(xs_core), dtype=np.complex128)
        c_cur = 0.0j
        for ix, xv in enumerate(xs_core):
            c_cur, L2_core[ix, idx_u1], _, _ = solve_uniformisation_exact(
                complex(xv, 1.0 / us_2d[idx_u1]), c_cur, N=36
            )
            c_row[ix] = c_cur
        for ix, xv in enumerate(xs_core):
            c_cur = c_row[ix]
            for iu in range(idx_u1 + 1, len(us_2d)):
                c_cur, L2_core[ix, iu], _, _ = solve_uniformisation_exact(
                    complex(xv, 1.0 / us_2d[iu]), c_cur, N=36
                )
            c_cur = c_row[ix]
            for iu in range(idx_u1 - 1, -1, -1):
                c_cur, L2_core[ix, iu], _, _ = solve_uniformisation_exact(
                    complex(xv, 1.0 / us_2d[iu]), c_cur, N=36
                )
        pad = 3
        xs_ext = np.concatenate([-xs_core[pad:0:-1], xs_core, 1.0 - xs_core[-2:-2 - pad:-1]])
        L2_ext = np.vstack([L2_core[pad:0:-1, :], L2_core, L2_core[-2:-2 - pad:-1, :]])
        self.sp2d = RectBivariateSpline(xs_ext, us_2d, L2_ext, kx=5, ky=5)

        us_1d = np.linspace(0.0, 0.22, 23)
        L2_1d = np.zeros(len(us_1d), dtype=np.float64)
        L2_1d[0] = L2_CUSP_LIMIT_EXACT
        c_cur = c_row[0]
        for uk in np.linspace(float(us_2d[idx_u1]), 0.22, 14)[1:]:
            c_cur, _, _, _ = solve_uniformisation_exact(complex(0.0, 1.0 / uk), c_cur, N=34)
        for iu in range(len(us_1d) - 1, 0, -1):
            c_cur, L2_1d[iu], _, _ = solve_uniformisation_exact(complex(0.0, 1.0 / us_1d[iu]), c_cur, N=38)
        self.sp1d = CubicSpline(us_1d, L2_1d, bc_type=((1, 0.0), "not-a-knot"))

    def eval_fd(self, taus_fd: np.ndarray) -> np.ndarray:
        xa = np.abs(taus_fd.real)
        u = 1.0 / taus_fd.imag
        out = np.empty(len(taus_fd), dtype=np.float64)
        m2 = u >= 0.20
        if np.any(m2):
            out[m2] = self.sp2d.ev(xa[m2], u[m2])
        if np.any(~m2):
            out[~m2] = self.sp1d(u[~m2])
        return out


# =============================================================================
# 2. STANDALONE CHANNEL WEIGHTS (THEOREM 90 EXACT & OLD SMALL-CUT) & FRAME
# =============================================================================

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

COUP_S_FLAT = COUP_S.reshape(12, 9)
COUP_ST_FLAT = COUP_ST.reshape(12, 9)
SECT = [("up", 1, -4), ("down", 1, 2), ("lep", -3, 6)]
CHAR_SHIFTS = [(0.0, 0.0), (0.0, -0.5), (-0.5, 0.0), (-0.5, -0.5)]


def pullback_b1724(taus: np.ndarray, a0: float, b0: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    t = taus.astype(np.complex128).copy()
    a = np.full(len(t), a0 % 1.0, dtype=np.float64)
    b = np.full(len(t), b0 % 1.0, dtype=np.float64)
    for _ in range(250):
        n = np.rint(t.real)
        m_sh = n != 0.0
        if np.any(m_sh):
            t[m_sh] -= n[m_sh]
            b[m_sh] = (b[m_sh] + n[m_sh] * a[m_sh]) % 1.0
        m_inv = np.abs(t) < (1.0 - 1e-12)
        if not np.any(m_inv):
            break
        t[m_inv] = -1.0 / t[m_inv]
        oa = a[m_inv].copy()
        a[m_inv] = (-b[m_inv]) % 1.0
        b[m_inv] = oa % 1.0
    return t, a, b


def F_u_vec(u1: np.ndarray, u2: np.ndarray, taus_fd: np.ndarray, m_cut: int = 10) -> np.ndarray:
    M = len(taus_fd)
    a = u1 % 1.0
    b = u2 % 1.0
    a = np.where((a < 1e-12) | (a > 1.0 - 1e-12), 0.0, a)
    b = np.where((b < 1e-12) | (b > 1.0 - 1e-12), 0.0, b)
    x = taus_fd.real
    y = taus_fd.imag
    out = np.zeros(M, dtype=np.float64)
    m_z = (a == 0.0) & (b == 0.0)
    m_a0 = (a == 0.0) & (~m_z)
    m_g = ~(m_z | m_a0)
    if np.any(m_z):
        out[m_z] = float("inf")
    if np.any(m_a0):
        xa = x[m_a0][:, None]
        ya = y[m_a0][:, None]
        ba = b[m_a0][:, None]
        base = math.pi * (2.0 * EG - 2.0 * math.log(2.0) - np.log(ya[:, 0]))
        m0 = (math.pi ** 2) * ya[:, 0] / (np.sin(math.pi * ba[:, 0]) ** 2)
        ms = np.concatenate([np.arange(-m_cut, 0.0), np.arange(1.0, m_cut + 1.0)])[None, :]
        wm = np.exp(2j * math.pi * (ms * xa + ba) - 2.0 * math.pi * np.abs(ms) * ya)
        out[m_a0] = base + m0 + np.sum((2.0 * math.pi / np.abs(ms)) * (wm / (1.0 - wm)).real, axis=1)
    if np.any(m_g):
        xg = x[m_g][:, None]
        yg = y[m_g][:, None]
        ag = a[m_g][:, None]
        bg = b[m_g][:, None]
        base = -math.pi * (digamma(ag[:, 0]) + digamma(1.0 - ag[:, 0]) + 2.0 * math.log(2.0) + np.log(yg[:, 0]))
        ms = np.arange(-m_cut, m_cut + 1.0)[None, :] + ag
        wm = np.exp(2j * math.pi * (ms * xg + bg) - 2.0 * math.pi * np.abs(ms) * yg)
        out[m_g] = base + np.sum((2.0 * math.pi / np.abs(ms)) * (wm / (1.0 - wm)).real, axis=1)
    return out


def a0_kronecker_vec(u1: np.ndarray, u2: np.ndarray, taus_fd: np.ndarray, m_cut: int = 15) -> np.ndarray:
    """Exact Kronecker-Eisenstein constant term a_{0,s}(tau_FD) of the normalised channel kernel
    K_s(u) = 1/u + a_{0,s} + a_{1,s} u + ... via symmetric-strip Lambert series (|Im w| <= 0.5 Im tau)."""
    nu = ((u1 + 0.5) % 1.0) - 0.5
    nu = np.where(np.abs(nu + 0.5) < 1e-12, 0.5, nu)
    nu = np.where(np.abs(nu) < 1e-12, 0.0, nu)
    Bm = (-u2) % 1.0
    Bm = np.where((Bm < 1e-12) | (Bm > 1.0 - 1e-12), 0.0, Bm)
    deg = (nu == 0.0) & (Bm == 0.0)
    w = nu * taus_fd - Bm
    pos = w.imag >= 0.0
    z_pos = np.where(pos, w, -w)
    ez = np.exp(2j * math.pi * z_pos)
    with np.errstate(divide="ignore", invalid="ignore"):
        cot_abs = 1j * (ez + 1.0) / (ez - 1.0)
    cot_pi_w = np.where(pos, cot_abs, -cot_abs)
    ns = np.arange(1.0, m_cut + 1.0)[None, :]
    q = np.exp(2j * math.pi * taus_fd)[:, None]
    qn = q ** ns
    ep = np.exp(2j * math.pi * (taus_fd + w)[:, None] * ns)
    em = np.exp(2j * math.pi * (taus_fd - w)[:, None] * ns)
    series = np.sum((ep - em) / (2j * (1.0 - qn)), axis=1)
    out = math.pi * cot_pi_w + 4.0 * math.pi * series + 2j * math.pi * nu
    return np.where(deg, 0.0j, out)


def _eval_base_c3(taus_fd: np.ndarray, wide_cut: bool = False) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    t_col = taus_fd[:, None]
    m_p = np.arange(1.0, 44.0 if wide_cut else 15.0)[None, :]
    q = np.exp(2j * math.pi * taus_fd)[:, None]
    qp = q ** m_p
    eta_hat = np.exp(1j * math.pi * taus_fd.real / 12.0) * np.prod(1.0 - qp, axis=1)
    e2 = 1.0 - 24.0 * np.sum(m_p * qp / (1.0 - qp), axis=1)
    denom_hat = 2.0 * math.pi * (eta_hat ** 3)

    nv = np.arange(-15.0, 16.0)[None, :] if wide_cut else np.arange(-6.0, 7.0)[None, :]

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
    return denom_hat, c3_S, np.conj(c3_S)


def eval_frame_modes(
    taus_fd: np.ndarray,
    a_fd: np.ndarray,
    b_fd: np.ndarray,
    l2_fd: np.ndarray,
    mode_list: Tuple[str, ...] = ("exact_T90", "old_weight"),
    return_matrices: bool = False,
    wide_cut: bool = False,
) -> Tuple[Dict[str, np.ndarray], Dict[str, int], Dict[str, Dict[Tuple[str, str], np.ndarray]]]:
    """Evaluate all 24 internal frame outputs simultaneously for requested channel-weight modes:
      - 'exact_T90'          : N_s = 2*pi*L_2 + c_s - pi * |a_{0,s}|^2 * exp(-2 * L_2)
      - 'old_weight'         : N_s = 2*pi*L_2 + c_s
      - 'ctl_wrong_sign_T90' : N_s = 2*pi*L_2 + c_s + pi * |a_{0,s}|^2 * exp(-2 * L_2)
      - 'ctl_bad_lcoord_exp' : N_s = 2*pi*L_2 + c_s - pi * |a_{0,s}|^2 * exp(-2 * (L_2 + 0.5*ln Im tau))
      - 'const_1p30'         : constant L_coord = 1.30
      - 'const_2p85'         : constant L_coord = 2.85
    """
    M = len(taus_fd)
    y = taus_fd.imag
    t_col = taus_fd[:, None]
    denom_hat, c3_S, c3_St = _eval_base_c3(taus_fd, wide_cut=wide_cut)
    ks = np.arange(-18.0, 19.0)[None, :] if wide_cut else np.arange(-5.0, 6.0)[None, :]
    m_fu = 30 if wide_cut else 10
    m_a0 = 24 if wide_cut else 15

    def thc0_and_1(a_arr: np.ndarray, b_arr: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        k0 = np.rint(-a_arr)[:, None]
        n0 = ks + k0 + a_arr[:, None]
        X0 = np.sum(np.exp(2j * math.pi * t_col * (n0 ** 2) + 2j * np.pi * n0 * b_arr[:, None]), axis=1)
        k1 = np.rint(-a_arr - 0.5)[:, None]
        n1 = ks + k1 + a_arr[:, None]
        X1t = np.sum(np.exp(2j * math.pi * t_col * ((n1 + 0.5) ** 2) + 2j * np.pi * n1 * b_arr[:, None]), axis=1)
        return X0, X1t

    need_a0 = any(m in ("exact_T90", "ctl_wrong_sign_T90", "ctl_bad_lcoord_exp") for m in mode_list)
    R_sec: Dict[str, np.ndarray] = {}
    Fu_sec: Dict[str, np.ndarray] = {}
    A0sq_sec: Dict[str, np.ndarray] = {}

    for sname, ql, qr in SECT:
        ax = ql * a_fd
        bx = 2.0 * ql * b_fd
        ay = qr * a_fd
        by = 2.0 * qr * b_fd
        X0, X1t = thc0_and_1(ax, bx)
        Y0, Y1t = thc0_and_1(ay, by)
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
        a0sq_arr = np.zeros((M, 4), dtype=np.float64)
        for si, (ds1, ds2) in enumerate(CHAR_SHIFTS):
            u1 = ap + ds1
            u2 = bp + ds2
            fu_arr[:, si] = F_u_vec(u1, u2, taus_fd, m_cut=m_fu)
            if need_a0:
                a0_v = a0_kronecker_vec(u1, u2, taus_fd, m_cut=m_a0)
                a0sq_arr[:, si] = (a0_v.real ** 2) + (a0_v.imag ** 2)
        Fu_sec[sname] = fu_arr
        A0sq_sec[sname] = a0sq_arr

    lcoord_canon = l2_fd + 0.5 * np.log(y)
    shift_canon = (2.0 * math.pi * (lcoord_canon - KRONECKER_SHIFT))[:, None]
    em2l2 = np.exp(-2.0 * l2_fd)[:, None]
    em2lc = np.exp(-2.0 * lcoord_canon)[:, None]
    log_thresh = math.log(1e-12)

    out: Dict[str, np.ndarray] = {}
    clamps: Dict[str, int] = {}
    mats_out: Dict[str, Dict[Tuple[str, str], np.ndarray]] = {}

    for mname in mode_list:
        obs = np.zeros((M, 24), dtype=np.float64)
        U_store: Dict[Tuple[str, str], np.ndarray] = {}
        Y_store: Dict[Tuple[str, str], np.ndarray] = {}
        clamp_cnt = 0
        col = 0
        for sname, _, _ in SECT:
            if mname in ("const_1p30", "const_2p85"):
                with np.errstate(divide="ignore"):
                    log_R_abs = np.log(np.maximum(np.abs(R_sec[sname]), 1e-300)) - (0.25 * math.pi * y)[:, None]
                active = (log_R_abs > log_thresh) & np.isfinite(Fu_sec[sname])
            else:
                active = np.isfinite(Fu_sec[sname])
            if mname == "exact_T90":
                val = shift_canon + Fu_sec[sname] - math.pi * A0sq_sec[sname] * em2l2
            elif mname == "old_weight":
                val = shift_canon + Fu_sec[sname]
            elif mname == "ctl_wrong_sign_T90":
                val = shift_canon + Fu_sec[sname] + math.pi * A0sq_sec[sname] * em2l2
            elif mname == "ctl_bad_lcoord_exp":
                val = shift_canon + Fu_sec[sname] - math.pi * A0sq_sec[sname] * em2lc
            elif mname == "const_1p30":
                val = 2.0 * math.pi * (1.30 - KRONECKER_SHIFT) + Fu_sec[sname]
            elif mname == "const_2p85":
                val = 2.0 * math.pi * (2.85 - KRONECKER_SHIFT) + Fu_sec[sname]
            else:
                raise ValueError(f"Unknown mode {mname}")
            clamp_cnt += int(np.sum(active & (val <= 0.0)))
            w = np.where(active & (val > 0.0), np.sqrt(np.maximum(val, 0.0)), 0.0)
            u_ch = w * R_sec[sname]
            YS = ((c3_S[:, :, None] * u_ch[:, None, :]).reshape(M, 12) @ COUP_S_FLAT).reshape(M, 3, 3)
            YSt = ((c3_St[:, :, None] * u_ch[:, None, :]).reshape(M, 12) @ COUP_ST_FLAT).reshape(M, 3, 3)
            for rn, Ym in [("S", YS), ("St", YSt)]:
                if return_matrices:
                    Y_store[(sname, rn)] = Ym
                if sname in ("up", "down"):
                    U_svd, sv, _ = np.linalg.svd(Ym)
                    U_store[(sname, rn)] = U_svd[:, :, ::-1]
                else:
                    sv = np.linalg.svd(Ym, compute_uv=False)
                s0_pos = sv[:, 0] > 0.0
                s0_safe = np.where(s0_pos, sv[:, 0], 1.0)
                obs[:, col] = np.where(s0_pos, sv[:, 1] / s0_safe, 0.0)
                obs[:, col + 1] = np.where(s0_pos, sv[:, 2] / s0_safe, 0.0)
                col += 2
        for ru in ("S", "St"):
            for rd in ("S", "St"):
                UuH = np.conj(np.transpose(U_store[("up", ru)], (0, 2, 1)))
                V = np.abs(UuH @ U_store[("down", rd)])
                obs[:, col] = V[:, 0, 1]
                obs[:, col + 1] = V[:, 1, 2]
                obs[:, col + 2] = V[:, 0, 2]
                col += 3
        out[mname] = obs
        clamps[mname] = clamp_cnt
        if return_matrices:
            mats_out[mname] = Y_store

    return out, clamps, mats_out


def eval_frame_12pt_avg_fd(
    taus_fd: np.ndarray,
    l2_fd: np.ndarray,
    mode_list: Tuple[str, ...] = ("exact_T90", "old_weight"),
) -> Tuple[Dict[str, np.ndarray], Dict[str, int]]:
    """Fast shared-base evaluation of the 12-pair (24-point) order-5 average directly on taus_fd.
    Shares c3_S across all 12 sheets and deduplicates theta-(ax,bx) and Kronecker-(u1,u2) evaluations
    across the finite 1/10-lattice, matching 12-sheet pullback evaluation to < 1e-12 (verified in Step 0)."""
    M = len(taus_fd)
    y = taus_fd.imag
    t_col = taus_fd[:, None]
    denom_hat, c3_S, c3_St = _eval_base_c3(taus_fd, wide_cut=False)
    ks = np.arange(-5.0, 6.0)[None, :]
    need_a0 = any(m in ("exact_T90", "ctl_wrong_sign_T90", "ctl_bad_lcoord_exp") for m in mode_list)

    th_cache: Dict[Tuple[int, int], Tuple[np.ndarray, np.ndarray]] = {}
    fa_cache: Dict[Tuple[int, int], Tuple[np.ndarray, np.ndarray]] = {}

    def get_thc(a_sc: float, b_sc: float) -> Tuple[np.ndarray, np.ndarray]:
        ak = round(a_sc * 5) % 5
        bk = round(b_sc * 5) % 50
        key = (ak, bk)
        if key not in th_cache:
            af = ak / 5.0
            bf = bk / 5.0
            k0 = round(-af)
            n0 = ks + (k0 + af)
            X0 = np.sum(np.exp(2j * math.pi * t_col * (n0 ** 2) + 2j * math.pi * n0 * bf), axis=1)
            k1 = round(-af - 0.5)
            n1 = ks + (k1 + af)
            X1t = np.sum(np.exp(2j * math.pi * t_col * ((n1 + 0.5) ** 2) + 2j * math.pi * n1 * bf), axis=1)
            th_cache[key] = (X0, X1t)
        return th_cache[key]

    def get_fa(u1_sc: float, u2_sc: float) -> Tuple[np.ndarray, np.ndarray]:
        u1k = round(u1_sc * 10) % 10
        u2k = round(u2_sc * 10) % 10
        key = (u1k, u2k)
        if key not in fa_cache:
            u1_arr = np.full(M, u1k / 10.0, dtype=np.float64)
            u2_arr = np.full(M, u2k / 10.0, dtype=np.float64)
            fu = F_u_vec(u1_arr, u2_arr, taus_fd, m_cut=10)
            if need_a0:
                a0_v = a0_kronecker_vec(u1_arr, u2_arr, taus_fd, m_cut=15)
                a0sq = (a0_v.real ** 2) + (a0_v.imag ** 2)
            else:
                a0sq = np.zeros(M, dtype=np.float64)
            fa_cache[key] = (fu, a0sq)
        return fa_cache[key]

    lcoord_canon = l2_fd + 0.5 * np.log(y)
    shift_canon = (2.0 * math.pi * (lcoord_canon - KRONECKER_SHIFT))[:, None]
    em2l2 = np.exp(-2.0 * l2_fd)[:, None]
    em2lc = np.exp(-2.0 * lcoord_canon)[:, None]
    log_thresh = math.log(1e-12)

    acc_out = {m: np.zeros((M, 24), dtype=np.float64) for m in mode_list}
    clamps = {m: 0 for m in mode_list}

    for la, lb in ORDER5_12_REPS:
        R_sec: Dict[str, np.ndarray] = {}
        Fu_sec: Dict[str, np.ndarray] = {}
        A0sq_sec: Dict[str, np.ndarray] = {}
        for sname, ql, qr in SECT:
            ax, bx = ql * la, 2.0 * ql * lb
            ay, by = qr * la, 2.0 * qr * lb
            X0, X1t = get_thc(ax, bx)
            Y0, Y1t = get_thc(ay, by)
            eb_x = cmath_exp_pi(bx)
            eb_y = cmath_exp_pi(by)
            M_mat = np.zeros((M, 2, 2), dtype=np.complex128)
            M_mat[:, 0, 0] = X0 * Y0 / denom_hat
            M_mat[:, 0, 1] = eb_y * X0 * Y1t / (1j * denom_hat)
            M_mat[:, 1, 0] = eb_x * X1t * Y0 / (1j * denom_hat)
            M_mat[:, 1, 1] = -(eb_x * eb_y) * X1t * Y1t / denom_hat
            R_arr = np.zeros((M, 4), dtype=np.complex128)
            for si in range(4):
                R_arr[:, si] = np.sum(EC_LIST[si][None, :, :] * M_mat, axis=(1, 2))
            R_sec[sname] = R_arr
            ap = ax + ay
            bp = 0.5 * (bx + by)
            fu_arr = np.zeros((M, 4), dtype=np.float64)
            a0sq_arr = np.zeros((M, 4), dtype=np.float64)
            for si, (ds1, ds2) in enumerate(CHAR_SHIFTS):
                fu_v, a0sq_v = get_fa(ap + ds1, bp + ds2)
                fu_arr[:, si] = fu_v
                a0sq_arr[:, si] = a0sq_v
            Fu_sec[sname] = fu_arr
            A0sq_sec[sname] = a0sq_arr

        for mname in mode_list:
            obs = np.zeros((M, 24), dtype=np.float64)
            U_store: Dict[Tuple[str, str], np.ndarray] = {}
            col = 0
            for sname, _, _ in SECT:
                if mname in ("const_1p30", "const_2p85"):
                    with np.errstate(divide="ignore"):
                        log_R_abs = np.log(np.maximum(np.abs(R_sec[sname]), 1e-300)) - (0.25 * math.pi * y)[:, None]
                    active = (log_R_abs > log_thresh) & np.isfinite(Fu_sec[sname])
                else:
                    active = np.isfinite(Fu_sec[sname])
                if mname == "exact_T90":
                    val = shift_canon + Fu_sec[sname] - math.pi * A0sq_sec[sname] * em2l2
                elif mname == "old_weight":
                    val = shift_canon + Fu_sec[sname]
                elif mname == "ctl_wrong_sign_T90":
                    val = shift_canon + Fu_sec[sname] + math.pi * A0sq_sec[sname] * em2l2
                elif mname == "ctl_bad_lcoord_exp":
                    val = shift_canon + Fu_sec[sname] - math.pi * A0sq_sec[sname] * em2lc
                elif mname == "const_1p30":
                    val = 2.0 * math.pi * (1.30 - KRONECKER_SHIFT) + Fu_sec[sname]
                elif mname == "const_2p85":
                    val = 2.0 * math.pi * (2.85 - KRONECKER_SHIFT) + Fu_sec[sname]
                else:
                    raise ValueError(f"Unknown mode {mname}")
                clamps[mname] += int(np.sum(active & (val <= 0.0)))
                w = np.where(active & (val > 0.0), np.sqrt(np.maximum(val, 0.0)), 0.0)
                u_ch = w * R_sec[sname]
                YS = ((c3_S[:, :, None] * u_ch[:, None, :]).reshape(M, 12) @ COUP_S_FLAT).reshape(M, 3, 3)
                YSt = ((c3_St[:, :, None] * u_ch[:, None, :]).reshape(M, 12) @ COUP_ST_FLAT).reshape(M, 3, 3)
                for rn, Ym in [("S", YS), ("St", YSt)]:
                    if sname in ("up", "down"):
                        U_svd, sv, _ = np.linalg.svd(Ym)
                        U_store[(sname, rn)] = U_svd[:, :, ::-1]
                    else:
                        sv = np.linalg.svd(Ym, compute_uv=False)
                    s0_pos = sv[:, 0] > 0.0
                    s0_safe = np.where(s0_pos, sv[:, 0], 1.0)
                    obs[:, col] = np.where(s0_pos, sv[:, 1] / s0_safe, 0.0)
                    obs[:, col + 1] = np.where(s0_pos, sv[:, 2] / s0_safe, 0.0)
                    col += 2
            for ru in ("S", "St"):
                for rd in ("S", "St"):
                    UuH = np.conj(np.transpose(U_store[("up", ru)], (0, 2, 1)))
                    V = np.abs(UuH @ U_store[("down", rd)])
                    obs[:, col] = V[:, 0, 1]
                    obs[:, col + 1] = V[:, 1, 2]
                    obs[:, col + 2] = V[:, 0, 2]
                    col += 3
            acc_out[mname] += obs / 12.0

    return acc_out, clamps


def cmath_exp_pi(val: float) -> complex:
    bf = (round(val * 5) % 50) / 5.0
    return complex(math.cos(math.pi * bf), math.sin(math.pi * bf))


# =============================================================================
# 3. ARBITRARY-PRECISION MPMATH CUSP EVALUATOR & HYPERBOLIC AREA INTEGRATOR
# =============================================================================


def eval_mp_12pt_avg(tau_fd: complex, l2_val: float) -> Dict[str, np.ndarray]:
    """Dynamic arbitrary-precision mpmath evaluation of the 12-pair (24-point) order-5 average
    of all 24 internal frame outputs at any cusp point tau_fd (Im tau_fd >= 2.0), eliminating
    IEEE-754 float64 SVD singular-vector rotation when sigma_min / sigma_max < 2.2e-16."""
    y_f = tau_fd.imag
    dps = max(55, int(3.2 * y_f) + 45)
    with mp.workdps(dps):
        t = mp.mpc(mp.mpf(repr(tau_fd.real)), mp.mpf(repr(tau_fd.imag)))
        x_r, y_r = mp.re(t), mp.im(t)
        l2 = mp.mpf(repr(l2_val))
        pi = mp.pi
        eg = mp.euler
        q = mp.exp(2j * pi * t)
        m_max = max(6, int(math.ceil(dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 3)))
        eta_prod = mp.mpf(1)
        e2 = mp.mpf(1)
        qp = mp.mpc(1)
        for m in range(1, m_max + 3):
            qp *= q
            eta_prod *= 1 - qp
            e2 -= 24 * m * qp / (1 - qp)
        denom_hat = 2 * pi * ((mp.exp(1j * pi * x_r / 12) * eta_prod) ** 3)
        n_th = max(6, int(math.ceil(math.sqrt(dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 3)))

        def th0_dt_mp(ca: float, cb: float):
            s0 = mp.mpc(0)
            s1 = mp.mpc(0)
            for k in range(-n_th, n_th + 1):
                na = mp.mpf(k) + mp.mpf(ca)
                tm = mp.exp(1j * pi * na * na * t + 2j * pi * na * mp.mpf(cb))
                s0 += tm
                s1 += mp.mpf("0.5") * na * na * tm
            return s0, s1

        t2, dt2 = th0_dt_mp(0.5, 0.0)
        t4, dt4 = th0_dt_mp(0.0, 0.5)
        t3, dt3 = th0_dt_mp(0.0, 0.0)
        R_h = [-(t2 * t2) / denom_hat, -(t4 * t4) / denom_hat, 1j * (t3 * t3) / denom_hat]
        dN_h = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2j * t3 * dt3 / denom_hat]
        c3_S = [dN_h[q_i] - (e2 / 12) * R_h[q_i] for q_i in range(3)]
        c3_St = [mp.conj(v) for v in c3_S]

        def thc01_mp(aa, bb):
            k0 = round(-float(aa))
            k1 = round(-float(aa) - 0.5)
            X0 = mp.mpc(0)
            X1 = mp.mpc(0)
            for k in range(-n_th, n_th + 1):
                n0 = mp.mpf(k + k0) + aa
                X0 += mp.exp(2j * pi * t * n0 * n0 + 2j * pi * n0 * bb)
                n1 = mp.mpf(k + k1) + aa
                X1 += mp.exp(2j * pi * t * ((n1 + mp.mpf("0.5")) ** 2) + 2j * pi * n1 * bb)
            return X0, X1

        fa_cache = {}

        def Fu_a0sq(u1_f: float, u2_f: float):
            ai = round(u1_f * 10) % 10
            bi = round(u2_f * 10) % 10
            if (ai, bi) in fa_cache:
                return fa_cache[(ai, bi)]
            if ai == 0 and bi == 0:
                fa_cache[(ai, bi)] = (None, mp.mpf(0))
                return fa_cache[(ai, bi)]
            a_m = mp.mpf(ai) / 10
            b_m = mp.mpf(bi) / 10
            if ai == 0:
                fu = pi * (2 * eg - 2 * mp.log(2) - mp.log(y_r)) + (pi ** 2) * y_r / (mp.sin(pi * b_m) ** 2)
                for m in range(1, m_max + 2):
                    for ms in (mp.mpf(m), mp.mpf(-m)):
                        wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                        fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
            else:
                fu = -pi * (mp.digamma(a_m) + mp.digamma(1 - a_m) + 2 * mp.log(2) + mp.log(y_r))
                for k in range(-m_max - 1, m_max + 2):
                    ms = mp.mpf(k) + a_m
                    wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                    fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
            nu_i = ((ai + 5) % 10) - 5
            if nu_i == -5:
                nu_i = 5
            nu = mp.mpf(nu_i) / 10
            Bm = mp.mpf((-bi) % 10) / 10
            w_z = nu * t - Bm
            ser = mp.mpc(0)
            for m in range(1, m_max + 2):
                qm = q ** m
                ser += (mp.exp(2j * pi * m * (t + w_z)) - mp.exp(2j * pi * m * (t - w_z))) / (2j * (1 - qm))
            a0 = pi * mp.cot(pi * w_z) + 4 * pi * ser + 2j * pi * nu
            fa_cache[(ai, bi)] = (fu, abs(a0) ** 2)
            return fa_cache[(ai, bi)]

        shift_old = 2 * pi * (l2 + mp.mpf("0.5") * mp.log(y_r) - eg - mp.log(pi))
        em2l2 = mp.exp(-2 * l2)
        acc = {"exact_T90": np.zeros(24, dtype=np.float64), "old_weight": np.zeros(24, dtype=np.float64)}

        for a_fd, b_fd in ORDER5_12_REPS:
            afd_mp = mp.mpf(round(a_fd * 5)) / 5
            bfd_mp = mp.mpf(round(b_fd * 5)) / 5
            sec_R = {}
            for sname, ql, qr in SECT:
                ax, bx = ql * afd_mp, 2 * ql * bfd_mp
                ay, by = qr * afd_mp, 2 * qr * bfd_mp
                X0, X1 = thc01_mp(ax, bx)
                Y0, Y1 = thc01_mp(ay, by)
                Mm = [
                    [X0 * Y0 / denom_hat, mp.exp(1j * pi * by) * X0 * Y1 / (1j * denom_hat)],
                    [mp.exp(1j * pi * bx) * X1 * Y0 / (1j * denom_hat), -mp.exp(1j * pi * (bx + by)) * X1 * Y1 / denom_hat],
                ]
                sec_R[sname] = [sum(EC_LIST[si][r, c] * Mm[r][c] for r in range(2) for c in range(2)) for si in range(4)]

            for mode in ("exact_T90", "old_weight"):
                vec24 = np.zeros(24, dtype=np.float64)
                U_st = {}
                col = 0
                for sname, ql, qr in SECT:
                    ap_f, bp_f = float(ql + qr) * a_fd, float(ql + qr) * b_fd
                    u_ch = []
                    for si, (ds1, ds2) in enumerate(CHAR_SHIFTS):
                        fu, a0sq = Fu_a0sq(ap_f + ds1, bp_f + ds2)
                        if fu is None:
                            u_ch.append(mp.mpc(0))
                            continue
                        val = shift_old + fu - (pi * a0sq * em2l2 if mode == "exact_T90" else 0)
                        assert val > 0, f"Unexpected non-positive cusp weight in {mode}"
                        u_ch.append(mp.sqrt(val) * sec_R[sname][si])
                    for rn, c3v, Cmat in (("S", c3_S, COUP_S), ("St", c3_St, COUP_ST)):
                        Ym = mp.matrix(3, 3)
                        for a_i in range(3):
                            for b_i in range(3):
                                s_val = mp.mpc(0)
                                for qi in range(3):
                                    for si in range(4):
                                        cc = Cmat[qi, si, a_i, b_i]
                                        if cc != 0:
                                            s_val += c3v[qi] * u_ch[si] * mp.mpc(cc.real, cc.imag)
                                Ym[a_i, b_i] = s_val
                        U_m, S_v, _ = mp.svd_c(Ym)
                        vec24[col] = float(S_v[1] / S_v[0])
                        vec24[col + 1] = float(S_v[2] / S_v[0])
                        col += 2
                        if sname in ("up", "down"):
                            U_rev = mp.matrix(3, 3)
                            for r_i in range(3):
                                for c_i in range(3):
                                    U_rev[r_i, c_i] = U_m[r_i, 2 - c_i]
                            U_st[(sname, rn)] = U_rev
                for ru in ("S", "St"):
                    for rd in ("S", "St"):
                        V = U_st[("up", ru)].H * U_st[("down", rd)]
                        vec24[col] = float(abs(V[0, 1]))
                        vec24[col + 1] = float(abs(V[1, 2]))
                        vec24[col + 2] = float(abs(V[0, 2]))
                        col += 3
                acc[mode] += vec24 / 12.0
        return acc


def _cusp_mp_worker(args: Tuple[complex, float]) -> Dict[str, np.ndarray]:
    t_pt, l2_pt = args
    return eval_mp_12pt_avg(t_pt, l2_pt)


def compute_hyperbolic_area_measure(l2_interp: CanonicalL2Interpolant) -> dict:
    """Compute the exact hyperbolic area average (3/pi) int_F <f>_{24}(tau) dx dy / y^2
    via u = 1/y compactification (dx dy / y^2 = dx du), splitting at y = 5 (u = 0.20):
      - Bulk (y <= 5, u in [0.20, 1/sqrt(1 - x^2)]): evaluated at BOTH coarse (24x32) and fine (36x48)
        2D Gauss-Legendre grids in float64 (also cross-checked against mpmath at y = 4.9).
      - Cusp (y > 5, u in (0, 0.20]): multi-panel Gauss-Legendre in u = 1/y ([0.10, 0.20], [0.05, 0.10],
        [0.02, 0.05], [0.01, 0.02], [0.005, 0.01]) + exact u -> 0^+ plateau on [0, 0.005], using dynamic
        arbitrary-precision mpmath SVD so every Y_cut in {5, 10, 20, 50, 100, 200, infty} is exact.
      - Also runs a naive float64 cusp control (CTL-T90-3) on y in [5, 100] to measure the exact
        IEEE-754 SVD singular-vector rotation error if arbitrary-precision cusp handling is omitted."""
    modes = ("exact_T90", "old_weight")

    def bulk_integral(nx_half: int, nu: int) -> Tuple[Dict[str, np.ndarray], float, int]:
        # Integrate x on [-0.5, 0] and [0, 0.5] separately so the minor Re(tau)=0 symmetry line is respected cleanly:
        xg, wg = leggauss(nx_half)
        ug, wug = leggauss(nu)
        xs_all = np.concatenate([-0.25 + 0.25 * xg, 0.25 + 0.25 * xg])
        wx_all = np.concatenate([0.25 * wg, 0.25 * wg])
        u_lo = 0.20
        u_hi = 1.0 / np.sqrt(1.0 - xs_all * xs_all)
        span_u = (u_hi - u_lo)[:, None]
        u_grid = u_lo + 0.5 * span_u * (ug[None, :] + 1.0)
        w_grid = wx_all[:, None] * (0.5 * span_u * wug[None, :])
        taus_fd = (xs_all[:, None] + 1j / u_grid).ravel()
        weights = w_grid.ravel()
        area_bulk = float(np.sum(weights))
        l2_vals = l2_interp.eval_fd(taus_fd)
        acc12, cl_d = eval_frame_12pt_avg_fd(taus_fd, l2_vals, mode_list=modes)
        clamps_tot = sum(cl_d.values())
        integ = {m: np.sum(weights[:, None] * acc12[m], axis=0) for m in modes}
        return integ, area_bulk, clamps_tot

    bulk_coarse, area_b_coarse, _ = bulk_integral(12, 24)
    bulk_fine, area_b_fine, bulk_clamps = bulk_integral(18, 36)
    assert bulk_clamps == 0
    assert abs(area_b_fine - (HYP_AREA_FD - 0.20)) < 1e-13
    bulk_quad_err = max(float(np.max(np.abs(bulk_fine[m] - bulk_coarse[m]))) / HYP_AREA_FD for m in modes)

    # Spot-check float64 vs mpmath right at the y = 4.95 seam:
    t_seam = 0.17 + 4.95j
    l2_seam = float(l2_interp.eval_fd(np.array([t_seam]))[0])
    mp_seam = eval_mp_12pt_avg(t_seam, l2_seam)
    f64_seam = {m: np.zeros(24, dtype=np.float64) for m in modes}
    for la, lb in ORDER5_12_REPS:
        ob_s, _, _ = eval_frame_modes(np.array([t_seam]), np.array([la]), np.array([lb]), np.array([l2_seam]), mode_list=modes)
        for m in modes:
            f64_seam[m] += ob_s[m][0] / 12.0
    seam_f64_vs_mp_err = max(float(np.max(np.abs(f64_seam[m] - mp_seam[m]))) for m in modes)
    assert seam_f64_vs_mp_err < 1e-10, f"Seam float64 vs mpmath mismatch: {seam_f64_vs_mp_err}"

    # Cusp panels aligned with Y_cut in {5, 10, 20, 50, 100, 200}:
    # u_panels from high u (y=5) down to 0 (y=infty):
    #   P1: [0.10, 0.20] (y in [5, 10]),  P2: [0.05, 0.10] (y in [10, 20]),
    #   P3: [0.02, 0.05] (y in [20, 50]), P4: [0.01, 0.02] (y in [50, 100]),
    #   P5: [0.005, 0.01] (y in [100, 200]), P6: [0.0, 0.005] (y in [200, infty), plateau).
    panel_specs = [
        ("y_5_to_10", 0.10, 0.20, 6, 4),
        ("y_10_to_20", 0.05, 0.10, 5, 3),
        ("y_20_to_50", 0.02, 0.05, 5, 2),
        ("y_50_to_100", 0.01, 0.02, 3, 1),
        ("y_100_to_200", 0.005, 0.01, 2, 1),
    ]
    panel_integrals = {pname: {m: np.zeros(24, dtype=np.float64) for m in modes} for pname, *_ in panel_specs}
    panel_f64_naive = {pname: {m: np.zeros(24, dtype=np.float64) for m in modes} for pname, *_ in panel_specs}

    cusp_jobs = []
    for pname, u_a, u_b, n_u, n_x in panel_specs:
        ug, wug = leggauss(n_u)
        us = 0.5 * (u_b - u_a) * ug + 0.5 * (u_b + u_a)
        wus = 0.5 * (u_b - u_a) * wug
        xs = -0.5 + (np.arange(n_x, dtype=np.float64) + 0.5) / n_x
        wx = 1.0 / n_x
        for u_val, wu_val in zip(us, wus):
            y_val = 1.0 / float(u_val)
            for x_val in xs:
                t_pt = complex(float(x_val), y_val)
                l2_pt = float(l2_interp.eval_fd(np.array([t_pt]))[0])
                cusp_jobs.append((pname, float(wu_val * wx), t_pt, l2_pt))

    pool = get_spawn_pool(l2_interp)
    mp_vals = pool.map(_cusp_mp_worker, [(t_pt, l2_pt) for _, _, t_pt, l2_pt in cusp_jobs])

    for (pname, w_tot, t_pt, l2_pt), mp_v in zip(cusp_jobs, mp_vals):
        for m in modes:
            panel_integrals[pname][m] += w_tot * mp_v[m]
        for la, lb in ORDER5_12_REPS:
            ob_f, _, _ = eval_frame_modes(
                np.array([t_pt]), np.array([la]), np.array([lb]), np.array([l2_pt]), mode_list=modes
            )
            for m in modes:
                panel_f64_naive[pname][m] += w_tot * (ob_f[m][0] / 12.0)

    # Asymptotic cusp limit at y = 200 vs y = 300 (verifying plateau to < 1e-13):
    cusp_200 = eval_mp_12pt_avg(0.11 + 200.0j, float(l2_interp.eval_fd(np.array([0.11 + 200.0j]))[0]))
    cusp_300 = eval_mp_12pt_avg(0.11 + 300.0j, L2_CUSP_LIMIT_EXACT)
    cusp_plateau_diff = max(float(np.max(np.abs(cusp_300[m] - cusp_200[m]))) for m in modes)
    assert cusp_plateau_diff < 1e-11
    panel_p6 = {m: 0.005 * cusp_300[m] for m in modes}

    # Assemble cumulative renormalized truncated integrals at Y_cut = 5, 10, 20, 50, 100, 200, and exact infty:
    ycut_chain = [
        ("Y_5", 5.0, []),
        ("Y_10", 10.0, ["y_5_to_10"]),
        ("Y_20", 20.0, ["y_5_to_10", "y_10_to_20"]),
        ("Y_50", 50.0, ["y_5_to_10", "y_10_to_20", "y_20_to_50"]),
        ("Y_100", 100.0, ["y_5_to_10", "y_10_to_20", "y_20_to_50", "y_50_to_100"]),
        ("Y_200", 200.0, ["y_5_to_10", "y_10_to_20", "y_20_to_50", "y_50_to_100", "y_100_to_200"]),
    ]
    ycut_table = {}
    for label, ycut, p_list in ycut_chain:
        area_sub = HYP_AREA_FD - (1.0 / ycut)
        entry = {"Y_cut": ycut, "captured_area_fraction": area_sub / HYP_AREA_FD}
        for m in modes:
            tot_m = bulk_fine[m].copy()
            for pn in p_list:
                tot_m += panel_integrals[pn][m]
            avg24 = tot_m / area_sub
            entry[m] = {
                "W_minus_7": avg24[W_MINUS_IDX].tolist(),
                "W_plus_7": avg24[W_PLUS_IDX].tolist(),
                "all_24": avg24.tolist(),
            }
        ycut_table[label] = entry

    # Full untruncated exact hyperbolic area average over all of F:
    exact_area_res = {}
    naive_f64_area_res = {}
    for m in modes:
        tot_inf = bulk_fine[m].copy()
        tot_f64 = bulk_fine[m].copy()
        for pn, *_ in panel_specs:
            tot_inf += panel_integrals[pn][m]
            tot_f64 += panel_f64_naive[pn][m]
        tot_inf += panel_p6[m]
        # In naive float64 on [0, 0.005], float64 gives its y=200 underflowed value:
        f64_200 = np.zeros(24, dtype=np.float64)
        for la, lb in ORDER5_12_REPS:
            ob200, _, _ = eval_frame_modes(
                np.array([0.11 + 200.0j]), np.array([la]), np.array([lb]), np.array([L2_CUSP_LIMIT_EXACT]), mode_list=(m,)
            )
            f64_200 += ob200[m][0] / 12.0
        tot_f64 += 0.005 * f64_200
        avg_inf = tot_inf / HYP_AREA_FD
        avg_f64 = tot_f64 / HYP_AREA_FD
        lep_down_diff = float(np.max(np.abs(avg_inf[4:8] - avg_inf[8:12])))
        assert lep_down_diff < 1e-12
        exact_area_res[m] = {
            "W_minus_7": avg_inf[W_MINUS_IDX].tolist(),
            "W_plus_7": avg_inf[W_PLUS_IDX].tolist(),
            "all_24": avg_inf.tolist(),
            "lep_minus_down_max_abs_diff": lep_down_diff,
        }
        naive_f64_area_res[m] = {
            "W_minus_7": avg_f64[W_MINUS_IDX].tolist(),
            "W_plus_7": avg_f64[W_PLUS_IDX].tolist(),
            "max_abs_corruption_on_W_minus_7": float(np.max(np.abs(avg_f64[W_MINUS_IDX] - avg_inf[W_MINUS_IDX]))),
            "max_abs_corruption_on_W_plus_7": float(np.max(np.abs(avg_f64[W_PLUS_IDX] - avg_inf[W_PLUS_IDX]))),
        }

    # Pointwise CTL-T90-3 check at y = 15 and y = 30:
    ctl3_pt_errs = {}
    for y_test in (15.0, 30.0):
        t_t = complex(0.23, y_test)
        l2_t = float(l2_interp.eval_fd(np.array([t_t]))[0])
        mp_t = eval_mp_12pt_avg(t_t, l2_t)["exact_T90"]
        f64_t = np.zeros(24, dtype=np.float64)
        for la, lb in ORDER5_12_REPS:
            obt, _, _ = eval_frame_modes(np.array([t_t]), np.array([la]), np.array([lb]), np.array([l2_t]), mode_list=("exact_T90",))
            f64_t += obt["exact_T90"][0] / 12.0
        ctl3_pt_errs[f"y_{int(y_test)}"] = float(np.max(np.abs(f64_t[W_MINUS_IDX] - mp_t[W_MINUS_IDX])))
        assert ctl3_pt_errs[f"y_{int(y_test)}"] > 1e-2, "Expected O(10^-1) float64 SVD underflow corruption in cusp"

    return {
        "method": (
            "Compactified u = 1/y integration (dx dy / y^2 = dx du on u in [0, 2/sqrt(3)]); "
            "2D Gauss-Legendre bulk quadrature on y <= 5 (80.90% of area) + 5-panel Gauss-Legendre "
            "dynamic arbitrary-precision mpmath SVD quadrature on y in [5, 200] + exact cusp limit on y >= 200."
        ),
        "bulk_coarse_vs_fine_max_err": bulk_quad_err,
        "seam_y4p95_f64_vs_mpmath_max_err": seam_f64_vs_mp_err,
        "cusp_y200_vs_y300_plateau_max_diff": cusp_plateau_diff,
        "cusp_limit_y_infty_24pt_avg": {
            m: {
                "W_minus_7": cusp_300[m][W_MINUS_IDX].tolist(),
                "W_plus_7": cusp_300[m][W_PLUS_IDX].tolist(),
            }
            for m in modes
        },
        "exact_untruncated": exact_area_res,
        "Y_cut_convergence_table": ycut_table,
        "CTL_T90_3_naive_float64_cusp_svd_corruption": {
            "pointwise_12avg_W_minus_max_err": ctl3_pt_errs,
            "integrated_area_corruption": naive_f64_area_res,
        },
    }


# =============================================================================
# 4. MOVE-COUNT WORD ENUMERATION, GEODESIC QUADRATURE, AND JACKKNIFE
# =============================================================================


def word_bits_to_mat(bits: int, length: int) -> np.ndarray:
    M = np.eye(2, dtype=np.int64)
    for pos in range(length - 1, -1, -1):
        if (bits >> pos) & 1:
            M[:, 0] += M[:, 1]
        else:
            M[:, 1] += M[:, 0]
    return M


def reverse_swap_bits(bits: int, length: int) -> int:
    rev = 0
    for k in range(length):
        rev = (rev << 1) | (1 - ((bits >> k) & 1))
    return rev


def keeps_mark_mat(M: np.ndarray) -> bool:
    u0 = int((M[0, 0] + 2 * M[0, 1]) % 5)
    u1 = int((M[1, 0] + 2 * M[1, 1]) % 5)
    return (u0 == 1 and u1 == 2) or (u0 == 4 and u1 == 3)


def enumerate_allowed_words(n: int) -> Tuple[List[int], List[np.ndarray]]:
    if n <= 16:
        bits_list: List[int] = []
        mats_list: List[np.ndarray] = []
        all_ones = (1 << n) - 1
        for b in range(1, all_ones):
            M = word_bits_to_mat(b, n)
            if keeps_mark_mat(M):
                bits_list.append(b)
                mats_list.append(M)
        return bits_list, mats_list
    total = 1 << n
    M = np.zeros((total, 2, 2), dtype=np.int64)
    M[:, 0, 0] = 1
    M[:, 1, 1] = 1
    idx_all = np.arange(total, dtype=np.int64)
    for pos in range(n - 1, -1, -1):
        is_R = ((idx_all >> pos) & 1) == 1
        M[is_R, :, 0] += M[is_R, :, 1]
        M[~is_R, :, 1] += M[~is_R, :, 0]
    u0 = (M[:, 0, 0] + 2 * M[:, 0, 1]) % 5
    u1 = (M[:, 1, 0] + 2 * M[:, 1, 1]) % 5
    keep = ((u0 == 1) & (u1 == 2)) | ((u0 == 4) & (u1 == 3))
    keep[0] = False
    keep[-1] = False
    kept_idx = np.nonzero(keep)[0]
    return kept_idx.tolist(), [M[i] for i in kept_idx]


def geodesic_midpoint_taus(M_word: np.ndarray, density: float = 34.0, min_nodes: int = 120) -> Tuple[float, np.ndarray]:
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


_SHARED_L2_INTERP: CanonicalL2Interpolant | None = None
_SPAWN_POOL = None
N_WORKERS = min(12, max(1, (os.cpu_count() or 4) - 2))


def _init_spawn_worker(l2_interp: CanonicalL2Interpolant) -> None:
    global _SHARED_L2_INTERP
    _SHARED_L2_INTERP = l2_interp


def get_spawn_pool(l2_interp: CanonicalL2Interpolant):
    global _SPAWN_POOL
    if _SPAWN_POOL is None:
        ctx = mp_proc.get_context("spawn")
        _SPAWN_POOL = ctx.Pool(processes=N_WORKERS, initializer=_init_spawn_worker, initargs=(l2_interp,))
    return _SPAWN_POOL


def close_spawn_pool() -> None:
    global _SPAWN_POOL
    if _SPAWN_POOL is not None:
        _SPAWN_POOL.close()
        _SPAWN_POOL.join()
        _SPAWN_POOL = None


def _allowed_worker(args):
    mats_sub, eval_twin, mode_list, density, min_nodes, batch_pts = args
    return _evaluate_allowed_serial(mats_sub, _SHARED_L2_INTERP, eval_twin, mode_list, density, min_nodes, batch_pts)


def _evaluate_allowed_serial(
    mats: List[np.ndarray],
    l2_interp: CanonicalL2Interpolant,
    eval_twin: bool = True,
    mode_list: Tuple[str, ...] = ("exact_T90", "old_weight"),
    density: float = 34.0,
    min_nodes: int = 120,
    batch_pts: int = 32000,
) -> Tuple[np.ndarray, Dict[str, np.ndarray], Dict[str, np.ndarray], Dict[str, int]]:
    W = len(mats)
    lengths = np.zeros(W, dtype=np.float64)
    mark_means = {m: np.zeros((W, 24), dtype=np.float64) for m in mode_list}
    twin_means = {m: np.zeros((W, 24), dtype=np.float64) for m in mode_list} if eval_twin else {}
    total_clamps = {m: 0 for m in mode_list}

    idx = 0
    while idx < W:
        chunk_taus = []
        chunk_slices = []
        tot_pts = 0
        while idx < W and (tot_pts == 0 or tot_pts < batch_pts):
            ell, taus = geodesic_midpoint_taus(mats[idx], density=density, min_nodes=min_nodes)
            lengths[idx] = ell
            n_pts = len(taus)
            chunk_taus.append(taus)
            chunk_slices.append((idx, tot_pts, tot_pts + n_pts))
            tot_pts += n_pts
            idx += 1

        big_taus = np.concatenate(chunk_taus)
        t_fd, a_m, b_m = pullback_b1724(big_taus, 0.4, 0.8)
        l2_fd = l2_interp.eval_fd(t_fd)
        obs_m, cl_m, _ = eval_frame_modes(t_fd, a_m, b_m, l2_fd, mode_list=mode_list)
        for m in mode_list:
            total_clamps[m] += cl_m[m]
            arr = obs_m[m]
            for w_i, s_lo, s_hi in chunk_slices:
                mark_means[m][w_i] = np.mean(arr[s_lo:s_hi], axis=0)

        if eval_twin:
            _, a_t, b_t = pullback_b1724(big_taus, 0.2, 0.4)
            obs_t, _, _ = eval_frame_modes(t_fd, a_t, b_t, l2_fd, mode_list=mode_list)
            for m in mode_list:
                arr = obs_t[m]
                for w_i, s_lo, s_hi in chunk_slices:
                    twin_means[m][w_i] = np.mean(arr[s_lo:s_hi], axis=0)

    return lengths, mark_means, twin_means, total_clamps


def evaluate_allowed_word_set(
    mats: List[np.ndarray],
    l2_interp: CanonicalL2Interpolant,
    eval_twin: bool = True,
    mode_list: Tuple[str, ...] = ("exact_T90", "old_weight"),
    density: float = 34.0,
    min_nodes: int = 120,
    batch_pts: int = 32000,
) -> Tuple[np.ndarray, Dict[str, np.ndarray], Dict[str, np.ndarray], Dict[str, int]]:
    if len(mats) < 240 or N_WORKERS <= 1:
        return _evaluate_allowed_serial(mats, l2_interp, eval_twin, mode_list, density, min_nodes, batch_pts)
    n_w = N_WORKERS
    splits = [mats[i::n_w] for i in range(n_w)]
    tasks = [(s, eval_twin, mode_list, density, min_nodes, batch_pts) for s in splits]
    pool = get_spawn_pool(l2_interp)
    parts = pool.map(_allowed_worker, tasks)
    W = len(mats)
    lengths = np.zeros(W, dtype=np.float64)
    mark_means = {m: np.zeros((W, 24), dtype=np.float64) for m in mode_list}
    twin_means = {m: np.zeros((W, 24), dtype=np.float64) for m in mode_list} if eval_twin else {}
    total_clamps = {m: 0 for m in mode_list}
    for i, (l_p, mm_p, tm_p, cl_p) in enumerate(parts):
        lengths[i::n_w] = l_p
        for m in mode_list:
            mark_means[m][i::n_w] = mm_p[m]
            total_clamps[m] += cl_p[m]
            if eval_twin:
                twin_means[m][i::n_w] = tm_p[m]
    return lengths, mark_means, twin_means, total_clamps


def _ergodic_worker(args):
    mats_sub, mode_list, density, min_nodes, batch_pts = args
    return _evaluate_ergodic_serial(mats_sub, _SHARED_L2_INTERP, mode_list, density, min_nodes, batch_pts)


def _evaluate_ergodic_serial(
    mats: List[np.ndarray],
    l2_interp: CanonicalL2Interpolant,
    mode_list: Tuple[str, ...] = ("exact_T90", "old_weight"),
    density: float = 24.0,
    min_nodes: int = 96,
    batch_pts: int = 32000,
) -> Tuple[np.ndarray, Dict[str, np.ndarray], Dict[str, int], float]:
    W = len(mats)
    lengths = np.zeros(W, dtype=np.float64)
    avg24_means = {m: np.zeros((W, 24), dtype=np.float64) for m in mode_list}
    total_clamps = {m: 0 for m in mode_list}
    max_y_visited = 0.0

    idx = 0
    while idx < W:
        chunk_taus = []
        chunk_slices = []
        tot_pts = 0
        while idx < W and (tot_pts == 0 or tot_pts < batch_pts):
            ell, taus = geodesic_midpoint_taus(mats[idx], density=density, min_nodes=min_nodes)
            lengths[idx] = ell
            n_pts = len(taus)
            chunk_taus.append(taus)
            chunk_slices.append((idx, tot_pts, tot_pts + n_pts))
            tot_pts += n_pts
            idx += 1

        big_taus = np.concatenate(chunk_taus)
        t_fd, _, _ = pullback_b1724(big_taus, 0.0, 0.2)
        max_y_visited = max(max_y_visited, float(np.max(t_fd.imag)))
        l2_fd = l2_interp.eval_fd(t_fd)
        acc_pt, cl_r = eval_frame_12pt_avg_fd(t_fd, l2_fd, mode_list=mode_list)
        for m in mode_list:
            total_clamps[m] += cl_r[m]
        hi_idx = np.nonzero(t_fd.imag > 8.0)[0]
        for hi_i in hi_idx:
            mp_hi = eval_mp_12pt_avg(complex(t_fd[hi_i]), float(l2_fd[hi_i]))
            for m in ("exact_T90", "old_weight"):
                if m in acc_pt:
                    acc_pt[m][hi_i] = mp_hi[m]
        for m in mode_list:
            arr = acc_pt[m]
            for w_i, s_lo, s_hi in chunk_slices:
                avg24_means[m][w_i] = np.mean(arr[s_lo:s_hi], axis=0)

    return lengths, avg24_means, total_clamps, max_y_visited


def evaluate_ergodic_24pt_words(
    mats: List[np.ndarray],
    l2_interp: CanonicalL2Interpolant,
    mode_list: Tuple[str, ...] = ("exact_T90", "old_weight"),
    density: float = 24.0,
    min_nodes: int = 96,
    batch_pts: int = 32000,
) -> Tuple[np.ndarray, Dict[str, np.ndarray], Dict[str, int], float]:
    """Evaluate unconstrained 40-letter words averaged over all 24 order-5 points (12 projective pairs),
    tracking max Im(tau_FD) visited along all closed geodesics."""
    if len(mats) < 120 or N_WORKERS <= 1:
        return _evaluate_ergodic_serial(mats, l2_interp, mode_list, density, min_nodes, batch_pts)
    n_w = N_WORKERS
    splits = [mats[i::n_w] for i in range(n_w)]
    tasks = [(s, mode_list, density, min_nodes, batch_pts) for s in splits]
    pool = get_spawn_pool(l2_interp)
    parts = pool.map(_ergodic_worker, tasks)
    W = len(mats)
    lengths = np.zeros(W, dtype=np.float64)
    avg24_means = {m: np.zeros((W, 24), dtype=np.float64) for m in mode_list}
    total_clamps = {m: 0 for m in mode_list}
    max_y_visited = 0.0
    for i, (l_p, am_p, cl_p, my_p) in enumerate(parts):
        lengths[i::n_w] = l_p
        max_y_visited = max(max_y_visited, my_p)
        for m in mode_list:
            avg24_means[m][i::n_w] = am_p[m]
            total_clamps[m] += cl_p[m]
    return lengths, avg24_means, total_clamps, max_y_visited


def weighted_mean(lengths: np.ndarray, vals: np.ndarray) -> np.ndarray:
    return np.sum(lengths[:, None] * vals, axis=0) / float(np.sum(lengths))


def jackknife_mean_se(lengths: np.ndarray, vals: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    W = len(lengths)
    L_sum = float(np.sum(lengths))
    w_c = lengths[:, None]
    S = np.sum(w_c * vals, axis=0)
    R = S / L_sum
    loo = (S[None, :] - w_c * vals) / (L_sum - lengths)[:, None]
    se = np.sqrt(((W - 1.0) / W) * np.sum((loo - np.mean(loo, axis=0, keepdims=True)) ** 2, axis=0))
    return R, se


def paired_jackknife(lengths: np.ndarray, m_vals: np.ndarray, t_vals: np.ndarray) -> dict:
    Rm, se_m = jackknife_mean_se(lengths, m_vals)
    Rt, se_t = jackknife_mean_se(lengths, t_vals)
    W = len(lengths)
    L_sum = float(np.sum(lengths))
    w_c = lengths[:, None]
    Sm = np.sum(w_c * m_vals, axis=0)
    St = np.sum(w_c * t_vals, axis=0)
    loo_d = ((Sm - St)[None, :] - w_c * (m_vals - t_vals)) / (L_sum - lengths)[:, None]
    se_d = np.sqrt(((W - 1.0) / W) * np.sum((loo_d - np.mean(loo_d, axis=0, keepdims=True)) ** 2, axis=0))
    Rd = Rm - Rt
    z_p = np.abs(Rd) / np.maximum(se_d, 1e-30)
    return {"Rm": Rm, "Rt": Rt, "Rd": Rd, "se_m": se_m, "se_t": se_t, "se_paired": se_d, "z_paired": z_p}


# =============================================================================
# 5. BENCHMARKS, PLANTED CONTROLS, AND MAIN VERIFICATION SUITE
# =============================================================================


def random_su3(rng: np.random.Generator) -> np.ndarray:
    Z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    Q = Q * (d / np.abs(d))[None, :]
    return Q / (np.linalg.det(Q) ** (1.0 / 3.0))


def check_direct_2d_horoball_t90(tau: complex) -> dict:
    """Standalone 2D Gauss-Legendre integration of int_{X_tau \\ H(L_2)} |K_s(u)|^2 dx dy on mark (2/5, 4/5)
    verifying Theorem 90's -pi |a_{0,s}|^2 e^{-2 L_2} term and catching CTL-T90-2 (+pi wrong sign)."""
    c_acc, l2_val, _, _ = track_exact(tau, N_final=44)
    al, be = frobenius_series(tau, c_acc, M_frob=50)
    pows = np.arange(len(al))[None, :]

    def horo_r(th_arr: np.ndarray) -> np.ndarray:
        r = np.full_like(th_arr, math.exp(-l2_val), dtype=np.float64)
        for _ in range(8):
            z = (r * np.exp(1j * th_arr))[:, None] ** pows
            g_re = ((z @ be) / (z @ al)).real
            r = np.exp(-l2_val - g_re)
        return r

    NK = 22

    def thc(a, b, u, T):
        n = np.arange(-NK, NK + 1) + a
        u = np.asarray(u, dtype=np.complex128)[..., None]
        return np.sum(np.exp(1j * math.pi * T * n * n + 2j * math.pi * n * (u + b)), axis=-1)

    def th1(u, t):
        k = np.arange(-NK, NK + 1)
        h = k + 0.5
        u = np.asarray(u, dtype=np.complex128)[..., None]
        return -1j * np.sum(((-1.0) ** k) * np.exp(1j * math.pi * t * h * h + 1j * math.pi * (2 * k + 1) * u), axis=-1)

    def bil(ax, bx, ay, by, u, t):
        T = 2 * t
        t1 = th1(u, t)
        den = 1j * np.exp(-1j * math.pi * t / 2) * np.exp(-1j * math.pi * u) * t1
        X0, X1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T)
        Y0, Y1 = thc(ay, by, u, T), thc(ay, by, u + t, T)
        return np.array(
            [
                [X0 * Y0 / t1, np.exp(1j * math.pi * by) * X0 * Y1 / den],
                [np.exp(1j * math.pi * bx) * X1 * Y0 / den, np.exp(1j * math.pi * (bx + by)) * X1 * Y1 / th1(u + t, t)],
            ]
        )

    a_fd, b_fd = 0.4, 0.8
    ax, bx = 1.0 * a_fd, 2.0 * b_fd
    ay, by = 2.0 * a_fd, 4.0 * b_fd
    uc = 0.01 * np.exp(2j * math.pi * np.arange(64) / 64)
    Mc = bil(ax, bx, ay, by, uc, tau)
    R_s = [np.mean(np.einsum("mn,mnk->k", EC_LIST[si], Mc) * uc) for si in range(4)]
    a0_cauchy = [np.mean(np.einsum("mn,mnk->k", EC_LIST[si], Mc) / R_s[si] - 1.0 / uc) for si in range(4)]
    a1_cauchy = [np.mean((np.einsum("mn,mnk->k", EC_LIST[si], Mc) / R_s[si] - 1.0 / uc - a0_cauchy[si]) / uc) for si in range(4)]

    verts = [0.5 + 0.5 * tau, -0.5 + 0.5 * tau, -0.5 - 0.5 * tau, 0.5 - 0.5 * tau]
    br = sorted(float(np.angle(z) % (2 * math.pi)) for z in verts)
    br.append(br[0] + 2 * math.pi)
    xg, wg = leggauss(72)
    xs, ws = leggauss(56)
    tot = np.zeros(4, dtype=np.float64)
    for a_ang, b_ang in zip(br[:-1], br[1:]):
        th = 0.5 * (b_ang - a_ang) * xg + 0.5 * (b_ang + a_ang)
        wt = 0.5 * (b_ang - a_ang) * wg
        d = np.exp(1j * th)
        y1 = d.imag / tau.imag
        x1 = d.real - y1 * tau.real
        rmax = 0.5 / np.maximum(np.abs(x1), np.abs(y1))
        rh = horo_r(th)
        shi, slo = np.log(rmax), np.log(rh)
        sg = 0.5 * (shi - slo)[:, None] * xs[None, :] + 0.5 * (shi + slo)[:, None]
        wsr = 0.5 * (shi - slo)[:, None] * ws[None, :]
        rr = np.exp(sg)
        z = rr * np.exp(1j * th)[:, None]
        Mz = bil(ax, bx, ay, by, z, tau)
        for si in range(4):
            Kz = np.einsum("mn,mnij->ij", EC_LIST[si], Mz) / R_s[si]
            tot[si] += np.sum(wt[:, None] * wsr * (np.abs(Kz) ** 2) * (rr ** 2))

    ap, bp = ax + ay, 0.5 * (bx + by)
    err_old, err_t90, err_t90_e4, err_wrong, err_a0_formula = [], [], [], [], []
    for si, (ds1, ds2) in enumerate(CHAR_SHIFTS):
        fu = F_u_vec(np.array([ap + ds1]), np.array([bp + ds2]), np.array([tau]))[0]
        a0_cl = a0_kronecker_vec(np.array([ap + ds1]), np.array([bp + ds2]), np.array([tau]))[0]
        err_a0_formula.append(float(abs(a0_cl - a0_cauchy[si])))
        n_old = 2 * math.pi * (l2_val + 0.5 * math.log(tau.imag) - KRONECKER_SHIFT) + fu
        n_t90 = n_old - math.pi * (abs(a0_cl) ** 2) * math.exp(-2 * l2_val)
        n_wrong = n_old + math.pi * (abs(a0_cl) ** 2) * math.exp(-2 * l2_val)
        n_e4 = n_t90 - 0.5 * math.pi * (abs(a1_cauchy[si] - 0.5 * c_acc) ** 2) * math.exp(-4 * l2_val)
        err_old.append(float(abs(tot[si] - n_old)))
        err_t90.append(float(abs(tot[si] - n_t90)))
        err_t90_e4.append(float(abs(tot[si] - n_e4)))
        err_wrong.append(float(abs(tot[si] - n_wrong)))

    assert max(err_a0_formula) < 1e-12
    assert max(err_t90) < 5e-4 and max(err_t90_e4) < 5e-6 and max(err_wrong) > 0.1
    return {
        "max_a0_kronecker_vs_cauchy_err": max(err_a0_formula),
        "max_2D_horoball_minus_old_weight": max(err_old),
        "max_2D_horoball_minus_exact_T90": max(err_t90),
        "max_2D_horoball_minus_T90_plus_e4L": max(err_t90_e4),
        "CTL_T90_2_max_2D_horoball_minus_wrong_sign": max(err_wrong),
    }


def main() -> None:
    t0 = time.time()
    lines_out: List[str] = []

    def log(msg: str) -> None:
        print(msg, flush=True)
        lines_out.append(msg)

    log("=== A2-CANON-T90: Standalone Whole-Weave 7-Value Read-Out (W_- & W_+, T90 & Old, Move-Count & Area) ===")

    # -------------------------------------------------------------------------
    # STEP 0: Uniformisation benchmarks, Theorem 90 2D horoball check, & controls
    # -------------------------------------------------------------------------
    log("\n[0/5] Uniformisation benchmarks, Theorem 90 2D horoball quadrature, planted controls, and symmetries...")
    omega6 = np.exp(1j * math.pi / 3.0)
    _, l2_om, lm_om, rerr_om = solve_uniformisation_exact(omega6, 0.0j, N=46, want_lmax=True)
    _, l2_y500, _, rerr_y500 = track_exact(500.0j, N_final=44, want_lmax=False)
    cusp_y500_diff = abs(l2_y500 - L2_CUSP_LIMIT_EXACT)
    assert rerr_om < 1e-13 and cusp_y500_diff < 2e-5

    t90_2d_check = check_direct_2d_horoball_t90(0.23 + 1.37j)

    # Exact S-covariance of BOTH exact_T90 and old_weight vs CTL-T90-1 (bad L_coord in exp(-2 L)):
    s_cov_t90_errs, s_cov_old_errs, ctl1_breaks = [], [], []
    for t_pt in [0.23 + 1.41j, -0.37 + 1.18j, 0.44 + 2.35j]:
        _, l2_a, _, _ = track_exact(t_pt, N_final=44)
        _, l2_b, _, _ = track_exact(-1.0 / t_pt, N_final=44)
        # Compare un-pulled-back frame evaluations directly at (t_pt, (0.4, 0.8)) vs (-1/t_pt, (-0.8%1, 0.4)):
        ob_a, _, _ = eval_frame_modes(
            np.array([t_pt]), np.array([0.4]), np.array([0.8]), np.array([l2_a]),
            mode_list=("exact_T90", "old_weight", "ctl_bad_lcoord_exp"),
        )
        ob_b, _, _ = eval_frame_modes(
            np.array([-1.0 / t_pt]), np.array([(-0.8) % 1.0]), np.array([0.4]), np.array([l2_b]),
            mode_list=("exact_T90", "old_weight", "ctl_bad_lcoord_exp"),
        )
        s_cov_t90_errs.append(float(np.max(np.abs(ob_a["exact_T90"] - ob_b["exact_T90"]))))
        s_cov_old_errs.append(float(np.max(np.abs(ob_a["old_weight"] - ob_b["old_weight"]))))
        ctl1_breaks.append(float(np.max(np.abs(ob_a["ctl_bad_lcoord_exp"] - ob_b["ctl_bad_lcoord_exp"]))))
    max_s_cov_t90 = max(s_cov_t90_errs)
    max_s_cov_old = max(s_cov_old_errs)
    max_ctl1_break = max(ctl1_breaks)
    assert max_s_cov_t90 < 1e-11 and max_s_cov_old < 1e-11 and max_ctl1_break > 1e-2

    # CTL-T90-4: Smoothness across |tau| = 1 at 80 deg and 70 deg (h = 0.01):
    corner_check = {}
    h_step = 0.01
    for deg in (80, 70):
        th = math.radians(deg)
        u_dir = complex(math.cos(th), math.sin(th))
        pts_l2, pts_t90, pts_lm, pts_sy = {}, {}, {}, {}
        for mult in (-2.0, -1.0, 0.0, 1.0, 2.0):
            t_raw = (1.0 + mult * h_step) * u_dir
            if abs(t_raw) < 1.0 - 1e-15:
                t_red = -1.0 / t_raw
                a_r, b_r = (-0.8) % 1.0, 0.4
            else:
                t_red = t_raw
                a_r, b_r = 0.4, 0.8
            _, v2, vm, _ = track_exact(t_red, N_final=44, want_lmax=True)
            # Test both L_2 + 0.5 ln Im(tau) and the S-invariant down identity channel s=0 (ds1=0, ds2=0) across |tau| = 1:
            fu_r = F_u_vec(np.array([3 * a_r]), np.array([3 * b_r]), np.array([t_red]))[0]
            a0_r = a0_kronecker_vec(np.array([3 * a_r]), np.array([3 * b_r]), np.array([t_red]))[0]
            pts_l2[mult] = v2 + 0.5 * math.log(t_red.imag)
            pts_t90[mult] = 2 * math.pi * (pts_l2[mult] - KRONECKER_SHIFT) + fu_r - math.pi * (abs(a0_r) ** 2) * math.exp(-2 * v2)
            pts_lm[mult] = vm + 0.5 * math.log(t_red.imag)
            pts_sy[mult] = 0.5 * math.log(t_red.imag)
        d2_l2_1 = pts_l2[1.0] + pts_l2[-1.0] - 2.0 * pts_l2[0.0]
        d2_l2_2 = pts_l2[2.0] + pts_l2[-2.0] - 2.0 * pts_l2[0.0]
        d2_t90_1 = pts_t90[1.0] + pts_t90[-1.0] - 2.0 * pts_t90[0.0]
        d2_t90_2 = pts_t90[2.0] + pts_t90[-2.0] - 2.0 * pts_t90[0.0]
        d2_lm_1 = pts_lm[1.0] + pts_lm[-1.0] - 2.0 * pts_lm[0.0]
        d2_lm_2 = pts_lm[2.0] + pts_lm[-2.0] - 2.0 * pts_lm[0.0]
        d2_sy_1 = pts_sy[1.0] + pts_sy[-1.0] - 2.0 * pts_sy[0.0]
        d2_sy_2 = pts_sy[2.0] + pts_sy[-2.0] - 2.0 * pts_sy[0.0]
        corner_check[f"deg_{deg}"] = {
            "L2_sym_ratio": d2_l2_2 / d2_l2_1,
            "N_T90_sym_ratio": d2_t90_2 / d2_t90_1,
            "Lmax_sym_ratio": d2_lm_2 / d2_lm_1,
            "systole_sym_ratio": d2_sy_2 / d2_sy_1,
        }
        assert abs(corner_check[f"deg_{deg}"]["L2_sym_ratio"] - 4.0) < 0.05
        assert abs(corner_check[f"deg_{deg}"]["N_T90_sym_ratio"] - 4.0) < 0.05
        assert abs(corner_check[f"deg_{deg}"]["Lmax_sym_ratio"] - 2.0) < 0.05
        assert abs(corner_check[f"deg_{deg}"]["systole_sym_ratio"] - 2.0) < 0.05

    # Build fast 2D+1D interpolant and validate on 16 random off-grid FD points:
    t_grid0 = time.time()
    l2_interp = CanonicalL2Interpolant()
    grid_sec = time.time() - t_grid0
    rng_py = random.Random(20261114)
    interp_errs = []
    for _ in range(16):
        xv = rng_py.uniform(-0.5, 0.5)
        yv = math.exp(rng_py.uniform(math.log(math.sqrt(1.0 - xv * xv) + 1e-4), math.log(80.0)))
        tv = complex(xv, yv)
        _, l2_ex, _, _ = track_exact(tv, N_final=44)
        l2_sp = float(l2_interp.eval_fd(np.array([tv]))[0])
        interp_errs.append(abs(l2_ex - l2_sp))
    max_interp_err = max(interp_errs)
    med_interp_err = float(np.median(interp_errs))
    assert max_interp_err < 1e-7

    # CTL-T90-5 (Guardrail 3 unitary basis-scrambling on bulk points) + c -> -c + lep == down pointwise:
    rng_np = np.random.default_rng(2026111499)
    bulk_taus = np.array([0.13 + 1.24j, -0.31 + 1.77j, 0.42 + 0.98j, -0.19 + 2.35j, 0.07 + 2.90j])
    t_fd_u, a_u, b_u = pullback_b1724(bulk_taus, 0.4, 0.8)
    l2_u = l2_interp.eval_fd(t_fd_u)
    obs_u, _, mats_u = eval_frame_modes(t_fd_u, a_u, b_u, l2_u, mode_list=("exact_T90", "old_weight"), return_matrices=True)
    max_unitary_scramble_err = 0.0
    for m_i in range(len(bulk_taus)):
        for w_idx, (ru, rd) in [(W_MINUS_IDX, ("St", "S")), (W_PLUS_IDX, ("S", "St"))]:
            UL_q = random_su3(rng_np)
            UR_u = random_su3(rng_np)
            UR_d = random_su3(rng_np)
            Yu_rot = UL_q @ mats_u["exact_T90"][("up", ru)][m_i] @ UR_u.conj().T
            Yd_rot = UL_q @ mats_u["exact_T90"][("down", rd)][m_i] @ UR_d.conj().T
            Uu_r, sv_u, _ = np.linalg.svd(Yu_rot)
            Ud_r, sv_d, _ = np.linalg.svd(Yd_rot)
            Uu_r = Uu_r[:, ::-1]
            Ud_r = Ud_r[:, ::-1]
            V_r = np.abs(Uu_r.conj().T @ Ud_r)
            rot_7 = np.array([sv_u[1] / sv_u[0], sv_u[2] / sv_u[0], sv_d[1] / sv_d[0], sv_d[2] / sv_d[0], V_r[0, 1], V_r[1, 2], V_r[0, 2]])
            ref_7 = obs_u["exact_T90"][m_i, w_idx]
            max_unitary_scramble_err = max(max_unitary_scramble_err, float(np.max(np.abs(rot_7 - ref_7))))
    assert max_unitary_scramble_err < 1e-12

    # Verify wide vs machine-epsilon series cutoffs AND 12-sheet pullback bijection identity on non-FD points:
    obs_u_wide, _, _ = eval_frame_modes(t_fd_u, a_u, b_u, l2_u, mode_list=("exact_T90", "old_weight"), wide_cut=True)
    max_series_trunc_err = max(float(np.max(np.abs(obs_u[m] - obs_u_wide[m]))) for m in ("exact_T90", "old_weight"))
    assert max_series_trunc_err < 1e-13

    non_fd_taus = -1.0 / (bulk_taus - 2.0)
    t_fd_nf, _, _ = pullback_b1724(non_fd_taus, 0.0, 0.2)
    l2_nf = l2_interp.eval_fd(t_fd_nf)
    pb_avg = {m: np.zeros((len(non_fd_taus), 24), dtype=np.float64) for m in ("exact_T90", "old_weight")}
    max_c_flip_err = 0.0
    max_lep_down_pt_err = 0.0
    for la, lb in ORDER5_12_REPS:
        _, a_p, b_p = pullback_b1724(non_fd_taus, la, lb)
        _, a_n, b_n = pullback_b1724(non_fd_taus, (-la) % 1.0, (-lb) % 1.0)
        op, _, _ = eval_frame_modes(t_fd_nf, a_p, b_p, l2_nf, mode_list=("exact_T90", "old_weight"))
        on, _, _ = eval_frame_modes(t_fd_nf, a_n, b_n, l2_nf, mode_list=("exact_T90", "old_weight"))
        for m in ("exact_T90", "old_weight"):
            pb_avg[m] += op[m] / 12.0
            max_c_flip_err = max(max_c_flip_err, float(np.max(np.abs(op[m] - on[m]))))
            max_lep_down_pt_err = max(max_lep_down_pt_err, float(np.max(np.abs(op[m][:, 4:8] - op[m][:, 8:12]))))
    fd_avg_direct, _ = eval_frame_12pt_avg_fd(t_fd_nf, l2_nf, mode_list=("exact_T90", "old_weight"))
    max_bijection_12avg_err = max(float(np.max(np.abs(pb_avg[m] - fd_avg_direct[m]))) for m in ("exact_T90", "old_weight"))
    assert max_c_flip_err < 1e-12 and max_lep_down_pt_err < 1e-12 and max_bijection_12avg_err < 1e-12

    log(
        f"  Grid built in {grid_sec:.2f}s | off-grid interp median={med_interp_err:.2e}, max={max_interp_err:.2e}\n"
        f"  T90 vs 2D horoball quadrature: old={t90_2d_check['max_2D_horoball_minus_old_weight']:.2e}, "
        f"T90={t90_2d_check['max_2D_horoball_minus_exact_T90']:.2e}, T90+e4L={t90_2d_check['max_2D_horoball_minus_T90_plus_e4L']:.2e}, "
        f"CTL-2 wrong-sign={t90_2d_check['CTL_T90_2_max_2D_horoball_minus_wrong_sign']:.2e}\n"
        f"  S-invariance err: T90={max_s_cov_t90:.2e}, old={max_s_cov_old:.2e} | CTL-1 bad-exp break={max_ctl1_break:.2e}\n"
        f"  CTL-4 arc ratios (80deg): N_T90={corner_check['deg_80']['N_T90_sym_ratio']:.4f}, "
        f"Lmax={corner_check['deg_80']['Lmax_sym_ratio']:.4f}, sys={corner_check['deg_80']['systole_sym_ratio']:.4f}\n"
        f"  CTL-5 Haar unitary={max_unitary_scramble_err:.2e} | c->-c={max_c_flip_err:.2e} | lep==down={max_lep_down_pt_err:.2e} | "
        f"12-bijection={max_bijection_12avg_err:.2e} | trunc={max_series_trunc_err:.2e}"
    )

    # -------------------------------------------------------------------------
    # STEP 1: Move-Count Route 1 — Exhaustive Populations n = 8..18 & n = 22, 28
    # -------------------------------------------------------------------------
    log("\n[1/5] Move-Count Route 1: Exhaustive zero-noise populations n = 8..18 + 600-word n = 22, 28...")
    exhaustive_res = {}
    pop16_old = None
    for n in [8, 10, 12, 14, 16, 18]:
        tn = time.time()
        bits_list, mats_list = enumerate_allowed_words(n)
        do_full_twin = n <= 16
        dens = 26.0 if n <= 16 else 22.0
        min_nd = 96 if n <= 16 else 80
        lengths, m_means, t_means, clamps = evaluate_allowed_word_set(
            mats_list, l2_interp, eval_twin=do_full_twin, mode_list=("exact_T90", "old_weight"), density=dens, min_nodes=min_nd
        )
        assert clamps["exact_T90"] == 0 and clamps["old_weight"] == 0

        if do_full_twin:
            bit_to_idx = {b: i for i, b in enumerate(bits_list)}
            dual_idx = np.array([bit_to_idx[reverse_swap_bits(b, n)] for b in bits_list], dtype=np.int64)
            max_dual_err = float(np.max(np.abs(m_means["exact_T90"] - t_means["exact_T90"][dual_idx])))
            max_pop_twin = float(
                np.max(np.abs(weighted_mean(lengths, m_means["exact_T90"]) - weighted_mean(lengths, t_means["exact_T90"])))
            )
            assert max_pop_twin < 5e-4
        else:
            bit_to_idx = {b: i for i, b in enumerate(bits_list)}
            sub_idx = list(range(0, min(200, len(bits_list))))
            sub_dual_mats = [mats_list[bit_to_idx[reverse_swap_bits(bits_list[i], n)]] for i in sub_idx]
            _, _, sub_t, _ = evaluate_allowed_word_set(
                sub_dual_mats, l2_interp, eval_twin=True, mode_list=("exact_T90", "old_weight"), density=dens, min_nodes=min_nd
            )
            max_dual_err = float(np.max(np.abs(m_means["exact_T90"][sub_idx] - sub_t["exact_T90"])))
            max_pop_twin = 0.0

        by_wmode = {}
        for m in ("exact_T90", "old_weight"):
            r24 = weighted_mean(lengths, m_means[m])
            by_wmode[m] = {
                "W_minus_7": r24[W_MINUS_IDX].tolist(),
                "W_plus_7": r24[W_PLUS_IDX].tolist(),
                "all_24": r24.tolist(),
            }
        exhaustive_res[str(n)] = {
            "n": n,
            "hyperbolic_allowed_count": len(mats_list),
            "clamps_exact_T90": clamps["exact_T90"],
            "clamps_old_weight": clamps["old_weight"],
            "max_word_reverse_swap_duality_err": max_dual_err,
            "max_population_mark_minus_twin_abs_diff": max_pop_twin,
            "by_weight": by_wmode,
        }
        if n == 16:
            pop16_old = (lengths, m_means["old_weight"])
        log(
            f"  n = {n:2d}: {len(mats_list):5d} words ({time.time() - tn:5.2f}s) | clamps=(0,0) | "
            f"max |A(w,mark)-A(w*,twin)|={max_dual_err:.2e}"
        )

    det_steps = {}
    for a_n, b_n in zip([8, 10, 12, 14, 16], [10, 12, 14, 16, 18]):
        ra = np.array(exhaustive_res[str(a_n)]["by_weight"]["exact_T90"]["W_minus_7"])
        rb = np.array(exhaustive_res[str(b_n)]["by_weight"]["exact_T90"]["W_minus_7"])
        det_steps[f"{a_n}_to_{b_n}"] = float(np.max(np.abs(rb - ra)))
        log(f"    Deterministic step n={a_n}->{b_n} (exact_T90, W_minus 7): max |Delta R| = {det_steps[f'{a_n}_to_{b_n}']:.6f}")

    rng_s = np.random.default_rng(2026111405)
    sampled_res = {}
    for n in [22, 28]:
        tn = time.time()
        seen = set()
        mats_n: List[np.ndarray] = []
        all_ones = (1 << n) - 1
        while len(mats_n) < 600:
            b = int(rng_s.integers(1, all_ones))
            if b in seen:
                continue
            M = word_bits_to_mat(b, n)
            if keeps_mark_mat(M):
                seen.add(b)
                mats_n.append(M)
        lengths, m_means, t_means, clamps = evaluate_allowed_word_set(
            mats_n, l2_interp, eval_twin=True, mode_list=("exact_T90", "old_weight"), density=26.0, min_nodes=96
        )
        assert clamps["exact_T90"] == 0 and clamps["old_weight"] == 0
        by_m = {}
        for m in ("exact_T90", "old_weight"):
            st = paired_jackknife(lengths, m_means[m], t_means[m])
            by_m[m] = {
                "W_minus_7_mean": st["Rm"][W_MINUS_IDX].tolist(),
                "W_minus_7_se": st["se_m"][W_MINUS_IDX].tolist(),
                "W_plus_7_mean": st["Rm"][W_PLUS_IDX].tolist(),
                "W_plus_7_se": st["se_m"][W_PLUS_IDX].tolist(),
                "all_24_mean": st["Rm"].tolist(),
                "all_24_se": st["se_m"].tolist(),
                "paired_mark_twin_z_median_24": float(np.median(st["z_paired"])),
                "paired_mark_twin_z_share_gt2_24": float(np.mean(st["z_paired"] > 2.0)),
            }
        sampled_res[str(n)] = {"n": n, "n_words": 600, "by_weight": by_m}
        log(
            f"  n = {n:2d} (600w, {time.time() - tn:5.2f}s): clamps=(0,0) | "
            f"paired mark-twin |z| median={by_m['exact_T90']['paired_mark_twin_z_median_24']:.2f}"
        )

    # 60-word draw calibration on exact n=16 old_weight population:
    len16, m16_o = pop16_old
    r16_o = weighted_mean(len16, m16_o)
    r18_o = np.array(exhaustive_res["18"]["by_weight"]["old_weight"]["all_24"])
    share_gt2_60w = np.zeros(2000, dtype=np.float64)
    for t_i in range(2000):
        ia = rng_s.choice(len(len16), size=60, replace=False)
        ib = rng_s.choice(len(len16), size=60, replace=False)
        ra, sa = jackknife_mean_se(len16[ia], m16_o[ia])
        rb, sb = jackknife_mean_se(len16[ib], m16_o[ib])
        zab = np.abs((rb + (r18_o - r16_o)) - ra) / np.sqrt(sa ** 2 + sb ** 2)
        share_gt2_60w[t_i] = float(np.mean(zab > 2.0))
    prob_gt_20pct = float(np.mean(share_gt2_60w >= (5.0 / 24.0 - 1e-9)))

    # -------------------------------------------------------------------------
    # STEP 2: Move-Count Route 2 — Primary 24-Point Ergodic Integral (2,000 x 40-letter words)
    # -------------------------------------------------------------------------
    log("\n[2/5] Move-Count Route 2 (Primary): Evaluating 2,000 unconstrained 40-letter words over all 24 order-5 points...")
    t_erg0 = time.time()
    erg_mats: List[np.ndarray] = []
    seen40 = set()
    all40 = (1 << 40) - 1
    while len(erg_mats) < 2000:
        b40 = int(rng_s.integers(1, all40))
        if b40 in seen40:
            continue
        seen40.add(b40)
        erg_mats.append(word_bits_to_mat(b40, 40))

    erg_len, erg_means, erg_clamps, erg_max_y = evaluate_ergodic_24pt_words(
        erg_mats, l2_interp, mode_list=("exact_T90", "old_weight"), density=24.0, min_nodes=96
    )
    assert erg_clamps["exact_T90"] == 0 and erg_clamps["old_weight"] == 0

    erg_len_c, erg_means_c, erg_clamps_c, _ = evaluate_ergodic_24pt_words(
        erg_mats[:400], l2_interp, mode_list=("const_1p30", "const_2p85"), density=24.0, min_nodes=96
    )

    ergodic_move_res = {}
    for m in ("exact_T90", "old_weight"):
        rm, sem = jackknife_mean_se(erg_len, erg_means[m])
        r_h1, s_h1 = jackknife_mean_se(erg_len[:1000], erg_means[m][:1000])
        r_h2, s_h2 = jackknife_mean_se(erg_len[1000:], erg_means[m][1000:])
        z_split = np.abs(r_h1 - r_h2) / np.sqrt(s_h1 ** 2 + s_h2 ** 2)
        lep_down_err = float(np.max(np.abs(rm[4:8] - rm[8:12])))
        assert lep_down_err < 1e-12
        ergodic_move_res[m] = {
            "n_words": 2000,
            "W_minus_7_mean": rm[W_MINUS_IDX].tolist(),
            "W_minus_7_se": sem[W_MINUS_IDX].tolist(),
            "W_plus_7_mean": rm[W_PLUS_IDX].tolist(),
            "W_plus_7_se": sem[W_PLUS_IDX].tolist(),
            "all_24_mean": rm.tolist(),
            "all_24_se": sem.tolist(),
            "split_half_1000v1000_median_z_24": float(np.median(z_split)),
            "split_half_1000v1000_max_z_7_W_minus": float(np.max(z_split[W_MINUS_IDX])),
            "lep_minus_down_max_abs_diff": lep_down_err,
        }
    for m in ("const_1p30", "const_2p85"):
        rm, sem = jackknife_mean_se(erg_len_c, erg_means_c[m])
        ergodic_move_res[m] = {
            "n_words": 400,
            "clamps": erg_clamps_c[m],
            "W_minus_7_mean": rm[W_MINUS_IDX].tolist(),
            "W_minus_7_se": sem[W_MINUS_IDX].tolist(),
            "W_plus_7_mean": rm[W_PLUS_IDX].tolist(),
            "W_plus_7_se": sem[W_PLUS_IDX].tolist(),
        }

    # Check if any word in erg_mats visited y > 7.0; if so, verify float64 vs mpmath on the highest-y word!
    # Find word with largest trace / cusp excursion:
    traces40 = [int(M[0, 0] + M[1, 1]) for M in erg_mats]
    log(
        f"  Move-count 24-pt ergodic (2,000w x 40L, {time.time() - t_erg0:5.2f}s): clamps=(0,0) | max Im(tau_FD)={erg_max_y:.2f}\n"
        f"    exact_T90 W_minus median rel SE = {100*np.median(np.array(ergodic_move_res['exact_T90']['W_minus_7_se'])/np.array(ergodic_move_res['exact_T90']['W_minus_7_mean'])):.3f}% | "
        f"split-half median |z| = {ergodic_move_res['exact_T90']['split_half_1000v1000_median_z_24']:.2f}"
    )

    # -------------------------------------------------------------------------
    # STEP 3: Hyperbolic Area Measure (Exact u = 1/y + Dynamic mpmath Cusp SVD)
    # -------------------------------------------------------------------------
    log("\n[3/5] Hyperbolic Area Measure: Bulk 2D Gauss-Legendre + multi-panel dynamic mpmath cusp SVD...")
    t_area0 = time.time()
    area_res = compute_hyperbolic_area_measure(l2_interp)
    log(
        f"  Area measure completed in {time.time() - t_area0:5.2f}s | bulk coarse-vs-fine err={area_res['bulk_coarse_vs_fine_max_err']:.2e} | "
        f"seam y=4.95 f64-vs-mpmath={area_res['seam_y4p95_f64_vs_mpmath_max_err']:.2e} | "
        f"cusp y=200..300 plateau diff={area_res['cusp_y200_vs_y300_plateau_max_diff']:.2e}\n"
        f"  CTL-3 naive float64 cusp SVD corruption: pointwise y=15 max err={area_res['CTL_T90_3_naive_float64_cusp_svd_corruption']['pointwise_12avg_W_minus_max_err']['y_15']:.3e}, "
        f"integrated area W_minus max corruption={area_res['CTL_T90_3_naive_float64_cusp_svd_corruption']['integrated_area_corruption']['exact_T90']['max_abs_corruption_on_W_minus_7']:.3e}"
    )

    # -------------------------------------------------------------------------
    # STEP 4: Cross-Comparisons (Relative Shifts & z-Scores ONLY on Stdout!)
    # -------------------------------------------------------------------------
    log("\n[4/5] Paired shifts & z-separations across weights, worlds, and measures (7-values in JSON only):")

    # 1. Exact T90 vs Old Weight (paired word-by-word on move-count, and exact on area):
    t90_minus_old_w = erg_means["exact_T90"] - erg_means["old_weight"]
    d_t90_m, d_t90_se = jackknife_mean_se(erg_len, t90_minus_old_w)
    z_t90_vs_old_Wm = np.abs(d_t90_m[W_MINUS_IDX]) / d_t90_se[W_MINUS_IDX]
    z_t90_vs_old_Wp = np.abs(d_t90_m[W_PLUS_IDX]) / d_t90_se[W_PLUS_IDX]
    rel_shift_t90_move_Wm = d_t90_m[W_MINUS_IDX] / np.array(ergodic_move_res["old_weight"]["W_minus_7_mean"])
    rel_shift_t90_move_Wp = d_t90_m[W_PLUS_IDX] / np.array(ergodic_move_res["old_weight"]["W_plus_7_mean"])

    area_t90_Wm = np.array(area_res["exact_untruncated"]["exact_T90"]["W_minus_7"])
    area_old_Wm = np.array(area_res["exact_untruncated"]["old_weight"]["W_minus_7"])
    area_t90_Wp = np.array(area_res["exact_untruncated"]["exact_T90"]["W_plus_7"])
    area_old_Wp = np.array(area_res["exact_untruncated"]["old_weight"]["W_plus_7"])
    rel_shift_t90_area_Wm = (area_t90_Wm - area_old_Wm) / area_old_Wm
    rel_shift_t90_area_Wp = (area_t90_Wp - area_old_Wp) / area_old_Wp

    # 2. W_minus vs W_plus separation under both weights and both measures:
    wm_move_t90 = np.array(ergodic_move_res["exact_T90"]["W_minus_7_mean"])
    wp_move_t90 = np.array(ergodic_move_res["exact_T90"]["W_plus_7_mean"])
    sm_move_t90 = np.array(ergodic_move_res["exact_T90"]["W_minus_7_se"])
    sp_move_t90 = np.array(ergodic_move_res["exact_T90"]["W_plus_7_se"])
    z_worlds_move_unpaired_t90 = np.abs(wm_move_t90 - wp_move_t90) / np.sqrt(sm_move_t90 ** 2 + sp_move_t90 ** 2)
    dw_m, dw_se = jackknife_mean_se(erg_len, erg_means["exact_T90"][:, W_MINUS_IDX] - erg_means["exact_T90"][:, W_PLUS_IDX])
    z_worlds_move_paired_t90 = np.abs(dw_m) / dw_se

    # 3. Move-count vs Hyperbolic Area separation (measured in move-count SEs):
    z_move_vs_area_t90_Wm = np.abs(wm_move_t90 - area_t90_Wm) / sm_move_t90
    z_move_vs_area_t90_Wp = np.abs(wp_move_t90 - area_t90_Wp) / sp_move_t90

    # 4. Route 1 (n=28, 600w) vs Route 2 (2,000w ergodic) agreement:
    r28_t90 = np.array(sampled_res["28"]["by_weight"]["exact_T90"]["all_24_mean"])
    s28_t90 = np.array(sampled_res["28"]["by_weight"]["exact_T90"]["all_24_se"])
    rerg_t90 = np.array(ergodic_move_res["exact_T90"]["all_24_mean"])
    serg_t90 = np.array(ergodic_move_res["exact_T90"]["all_24_se"])
    z_r1_vs_r2_24 = np.abs(r28_t90 - rerg_t90) / np.sqrt(s28_t90 ** 2 + serg_t90 ** 2)

    # 5. Cusp Y_cut truncation convergence relative to exact untruncated area:
    ycut_rel_errs = {}
    for ylbl, yentry in area_res["Y_cut_convergence_table"].items():
        v_cut = np.array(yentry["exact_T90"]["W_minus_7"])
        ycut_rel_errs[ylbl] = float(np.max(np.abs(v_cut - area_t90_Wm) / area_t90_Wm))

    log(
        f"  Exact T90 vs Old Weight relative shift (7 values):\n"
        f"    Move-count W_- : min={100*np.min(rel_shift_t90_move_Wm):+.3f}%, max={100*np.max(rel_shift_t90_move_Wm):+.3f}% "
        f"(paired |z| range {np.min(z_t90_vs_old_Wm):.1f}..{np.max(z_t90_vs_old_Wm):.1f})\n"
        f"    Move-count W_+ : min={100*np.min(rel_shift_t90_move_Wp):+.3f}%, max={100*np.max(rel_shift_t90_move_Wp):+.3f}% "
        f"(paired |z| range {np.min(z_t90_vs_old_Wp):.1f}..{np.max(z_t90_vs_old_Wp):.1f})\n"
        f"    Area       W_- : min={100*np.min(rel_shift_t90_area_Wm):+.3f}%, max={100*np.max(rel_shift_t90_area_Wm):+.3f}%\n"
        f"    Area       W_+ : min={100*np.min(rel_shift_t90_area_Wp):+.3f}%, max={100*np.max(rel_shift_t90_area_Wp):+.3f}%\n"
        f"  W_- vs W_+ separation (Move-count, exact_T90): unpaired |z|={np.min(z_worlds_move_unpaired_t90):.1f}..{np.max(z_worlds_move_unpaired_t90):.1f}, "
        f"paired |z|={np.min(z_worlds_move_paired_t90):.1f}..{np.max(z_worlds_move_paired_t90):.1f}\n"
        f"  Move-count vs Hyperbolic Area separation (exact_T90, in move SEs):\n"
        f"    W_- |z| range: {np.min(z_move_vs_area_t90_Wm):.1f}..{np.max(z_move_vs_area_t90_Wm):.1f} (median {np.median(z_move_vs_area_t90_Wm):.1f})\n"
        f"    W_+ |z| range: {np.min(z_move_vs_area_t90_Wp):.1f}..{np.max(z_move_vs_area_t90_Wp):.1f} (median {np.median(z_move_vs_area_t90_Wp):.1f})\n"
        f"  Route 1 (n=28, 600w) vs Route 2 (2000w ergodic) median |z|={np.median(z_r1_vs_r2_24):.2f} (share>2={100*np.mean(z_r1_vs_r2_24>2):.1f}%)\n"
        f"  Area Y_cut max rel bias vs untruncated: Y=5 -> {100*ycut_rel_errs['Y_5']:.2f}%, Y=10 -> {100*ycut_rel_errs['Y_10']:.2f}%, "
        f"Y=50 -> {100*ycut_rel_errs['Y_50']:.2f}%, Y=200 -> {100*ycut_rel_errs['Y_200']:.3f}%"
    )

    # Top-level crisp summary table of the 8 requested 7-vectors (2 measures x 2 weights x 2 worlds):
    headline_seven_values = {
        "position_names": SEVEN_POSITION_NAMES,
        "position_definitions": {
            "up_r23": "up middle-to-heaviest singular-value ratio (sigma_2 / sigma_3)",
            "up_r13": "up lightest-to-heaviest singular-value ratio (sigma_1 / sigma_3)",
            "down_r23": "down middle-to-heaviest singular-value ratio (sigma_2 / sigma_3; equals lepton S/S_tilde at level 5)",
            "down_r13": "down lightest-to-heaviest singular-value ratio (sigma_1 / sigma_3; equals lepton S/S_tilde at level 5)",
            "abs_V12": "|(U_up^H U_down)_{1,2}| with columns ordered ascending (1=lightest, 2=middle, 3=heaviest)",
            "abs_V23": "|(U_up^H U_down)_{2,3}|",
            "abs_V13": "|(U_up^H U_down)_{1,3}|",
        },
        "higgs_worlds": {
            "W_minus": "(up S_tilde, down S, leptons S)",
            "W_plus": "(up S, down S_tilde, leptons S_tilde)",
        },
        "channel_weights": {
            "exact_T90": "2*pi*L_2 + c_s - pi * |a_{0,s}|^2 * exp(-2 * L_2)",
            "old_weight": "2*pi*L_2 + c_s",
        },
        "move_count_measure": {
            "exact_T90": {
                "W_minus": {
                    "mean_7": ergodic_move_res["exact_T90"]["W_minus_7_mean"],
                    "se_7": ergodic_move_res["exact_T90"]["W_minus_7_se"],
                },
                "W_plus": {
                    "mean_7": ergodic_move_res["exact_T90"]["W_plus_7_mean"],
                    "se_7": ergodic_move_res["exact_T90"]["W_plus_7_se"],
                },
            },
            "old_weight": {
                "W_minus": {
                    "mean_7": ergodic_move_res["old_weight"]["W_minus_7_mean"],
                    "se_7": ergodic_move_res["old_weight"]["W_minus_7_se"],
                },
                "W_plus": {
                    "mean_7": ergodic_move_res["old_weight"]["W_plus_7_mean"],
                    "se_7": ergodic_move_res["old_weight"]["W_plus_7_se"],
                },
            },
        },
        "area_measure_exact_untruncated": {
            "exact_T90": {
                "W_minus": {"value_7": area_res["exact_untruncated"]["exact_T90"]["W_minus_7"]},
                "W_plus": {"value_7": area_res["exact_untruncated"]["exact_T90"]["W_plus_7"]},
            },
            "old_weight": {
                "W_minus": {"value_7": area_res["exact_untruncated"]["old_weight"]["W_minus_7"]},
                "W_plus": {"value_7": area_res["exact_untruncated"]["old_weight"]["W_plus_7"]},
            },
        },
    }

    results = {
        "card": "A2-CANON-T90",
        "seat": "agy-002",
        "date": "2026-11-14",
        "data_free": True,
        "zero_shared_code": True,
        "blind_before_reading_b1928_or_xcanon": True,
        "seven_values_summary": headline_seven_values,
        "benchmarks_and_controls": {
            "omega6_SL2R_reality_err": rerr_om,
            "L2_omega6": l2_om,
            "Lmax_omega6": lm_om,
            "L2_cusp_limit_exact_formula": "pi + ln(pi) - 3*ln(2)",
            "L2_cusp_limit_exact_value": L2_CUSP_LIMIT_EXACT,
            "L2_at_y500": l2_y500,
            "L2_y500_minus_exact_limit": cusp_y500_diff,
            "theorem90_vs_2D_horoball_quadrature": t90_2d_check,
            "S_invariance_exact_T90_max_err": max_s_cov_t90,
            "S_invariance_old_weight_max_err": max_s_cov_old,
            "CTL_T90_1_bad_lcoord_exp_S_break": max_ctl1_break,
            "CTL_T90_4_arc_smoothness_ratios": corner_check,
            "CTL_T90_5_haar_unitary_scramble_max_err": max_unitary_scramble_err,
            "interpolant_off_grid_16pt_median_err": med_interp_err,
            "interpolant_off_grid_16pt_max_err": max_interp_err,
            "matter_charge_flip_c_to_minus_c_max_err": max_c_flip_err,
            "lepton_equals_down_pointwise_max_err": max_lep_down_pt_err,
            "sl2z_12sheet_bijection_max_err": max_bijection_12avg_err,
            "series_truncation_vs_wide_max_err": max_series_trunc_err,
        },
        "move_count_route1_exhaustive_populations": exhaustive_res,
        "move_count_route1_deterministic_steps_W_minus_7": det_steps,
        "move_count_route1_sampled_600w_no_replacement": sampled_res,
        "move_count_route1_60w_calibration": {
            "n_mc_pairs": 2000,
            "prob_share_gt2_at_least_5_of_24": prob_gt_20pct,
        },
        "move_count_route2_ergodic_24pt_2000w_40let": ergodic_move_res,
        "area_measure_detail": area_res,
        "comparisons_and_separations": {
            "exact_T90_minus_old_rel_shift_move_W_minus_7": rel_shift_t90_move_Wm.tolist(),
            "exact_T90_minus_old_rel_shift_move_W_plus_7": rel_shift_t90_move_Wp.tolist(),
            "exact_T90_minus_old_paired_z_move_W_minus_7": z_t90_vs_old_Wm.tolist(),
            "exact_T90_minus_old_paired_z_move_W_plus_7": z_t90_vs_old_Wp.tolist(),
            "exact_T90_minus_old_rel_shift_area_W_minus_7": rel_shift_t90_area_Wm.tolist(),
            "exact_T90_minus_old_rel_shift_area_W_plus_7": rel_shift_t90_area_Wp.tolist(),
            "W_minus_vs_W_plus_unpaired_z_move_exact_T90_7": z_worlds_move_unpaired_t90.tolist(),
            "W_minus_vs_W_plus_paired_z_move_exact_T90_7": z_worlds_move_paired_t90.tolist(),
            "move_vs_area_z_in_move_se_exact_T90_W_minus_7": z_move_vs_area_t90_Wm.tolist(),
            "move_vs_area_z_in_move_se_exact_T90_W_plus_7": z_move_vs_area_t90_Wp.tolist(),
            "route1_n28_vs_route2_2000w_median_z_24": float(np.median(z_r1_vs_r2_24)),
            "route1_n28_vs_route2_2000w_share_gt2_24": float(np.mean(z_r1_vs_r2_24 > 2.0)),
            "area_Y_cut_max_rel_bias_W_minus_exact_T90": ycut_rel_errs,
        },
        "obs24_position_names": OBS24_NAMES,
        "elapsed_seconds": round(time.time() - t0, 2),
    }

    close_spawn_pool()
    json_path = OUT_DIR / "verify_a2_canon_results.json"
    out_path = OUT_DIR / "verify_a2_canon_out.txt"
    log(f"\n[5/5] Completed in {time.time() - t0:.2f}s. Writing 7-value read-out vectors strictly to {json_path.name}.")
    log("0 of 19.")
    json_path.write_text(json.dumps(results, indent=2, default=float) + "\n", encoding="utf-8")
    out_path.write_text("\n".join(lines_out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

# 0 of 19.
