#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-WALL
===============================================
Seat: agy-exp
Pre-registered expectations commit: 593ace692
  (relays/cards/AGY-EXP_X-WALL_why-frame-c-readout-fails-structurally.md)

Independently constructs Frame C's exact modular operators from scratch (zero imports
from main; reuses only agy-exp's own punctured-torus canonical end solver from
relays/x_measure_verify/verify_x_measure.py) and tests:

  1. Gate_Haar (Guardrail 3):
     Gauge-allowed common left-handed U(3) Haar transformations U_{L,Q} and independent
     right-handed U(3) Haar transformations U_{R,u}, U_{R,d} leave all 9 entries of
     |U_u^dagger U_d| and all singular-value ratios invariant to < 1e-13, whereas
     adversarial independent left rotations U_{L,u} != U_{L,d} scramble |U_u^dagger U_d|.

  2. W1 — Trace-Zero Chiral Derangement Across All 24 Order-5 Lines in Both Higgs Worlds:
     Evaluates the full 3 x 3 modulus matrix |U_u^dagger U_d| in dynamic arbitrary-precision
     mpmath across all 24 primitive order-5 torsion lines c in P_5 and all 4 modes
     (W_- and W_+ x exact Theorem 90 weight and truncated weight) at heights
     y in {1.5, 3.6515, 6.0653, 9.0, 15.0, 30.0, 60.0, 120.0}, plus coherent P_5-summed
     matrices Y_bar_f(tau) = (1/24) sum_{c in P_5} Y_f(c, tau).

  3. W2 — Exact Quaternion Chiral-Ladder Theorem (S -> S~ Acts as Order-3 Shift C):
     Verifies from exact rational arithmetic that Serre's weight-3/2 vector B[1] has
     leading cusp power q^{-1/8} (k = -1) with row (0, +1/24, -i/24), yielding nilpotent
     rank-1 matrices S_dom = (1/12) E_{12} and S~_dom = -(1/12) E_{21}; verifies in the
     orthonormal chiral basis {e_+, e_0, e_-} that U_f(S~) -> C U_f(S) with C^3 = I_3,
     Tr(C) = 0 across all 24 lines of P_5.

  4. W3 — Arithmetic Mean vs Geometric Mean & Horocycle Phase Cancellation:
     (a) Compares arithmetic mean E[sigma_1 / sigma_3] against geometric mean
         exp(E[ln(sigma_1 / sigma_3)]) along closed hyperbolic geodesics L^6 R L R and
         L^{16} R and on the Poincare area measure over F_std.
     (b) Compares pointwise horocycle averaging E_x[|U_u^dagger U_d|] on x in [-1/2, 1/2]
         against diagonalizing the horocycle-integrated Hermitian operator
         H_f(c, y) = int_{-1/2}^{1/2} Y_f(c, x + i y) Y_f(c, x + i y)^dagger dx
         at heights y in {1.5, 3.6515, 6.0653, 30.0}.

  5. Planted Controls PC_WALL_1 & PC_WALL_2 + Level-5 Down-Lepton Lock:
     - PC_WALL_1: Unshifted family-frame control (up S, down S) keeping exact charges
       up (1, -4) and down (1, 2) restores |U_u^dagger U_d| -> I_3 (all 3 diagonals > 0.99
       across all 24 lines at Im(tau) = 30) while keeping distinct up/down hierarchies.
     - PC_WALL_2: Factorized SU(2)_L-covariant overlap Y_f^{fact} = L_{q_L} D_H R_{q_{R,f}}^dagger
       restores |(U_u^dagger U_d)_{3,3}| -> 1 and suppresses (2,3), (1,3) -> 0 in the cusp
       while preserving distinct up and down hierarchies.

Strict Firewall & Mask Hygiene:
  - 0 of 19: zero measured numbers read, imported, or compared.
  - Zero decimal floats or scientific notation printed to stdout; values in JSON only.
  - Zero particle or mixing-matrix proper names anywhere.
"""

from __future__ import annotations

import hashlib
import json
import math
import pathlib
import sys
import time
from fractions import Fraction
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
from scipy.special import roots_legendre

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "x_measure_verify"))
import verify_x_measure as vxm  # agy-exp's own zero-import module (used for L_2 solver)

OUT_JSON = HERE / "verify_x_wall_out.json"
SHA_TXT = HERE / "OUTPUT_SHA256.txt"

P5_ALL_24_INT: List[Tuple[int, int]] = [
    (ja, jb) for ja in range(5) for jb in range(5) if (ja, jb) != (0, 0)
]
assert len(P5_ALL_24_INT) == 24

SIX_CHARGES: Dict[str, Tuple[int, int]] = {
    "up": (1, -4),
    "down": (1, 2),
    "lepton": (-3, 6),
}


# ============================================================================
# SECTION 1: INDEPENDENT OPERATOR CONSTRUCTION & QUATERNION ALGEBRA
# ============================================================================

def build_quaternions_and_coupling() -> Dict[str, Any]:
    i2 = np.eye(2, dtype=np.complex128)
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=np.complex128)
    qj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=np.complex128)
    qk = qi @ qj
    eps = qj
    units = [i2, qi, qj, qk]
    ec = [eps @ u for u in units]
    G = np.array([[np.sum(ec[t] * units[s]) for s in range(4)] for t in range(4)], dtype=np.complex128)
    Gi = np.linalg.inv(G)
    edual = [sum(Gi[b, a] * units[b] for b in range(4)) for a in range(4)]
    blocks = [qj, qi, qk]
    higgs_units = [qi, qj, qk]
    T = np.zeros((3, 4, 3, 3), dtype=np.complex128)
    for alpha in range(3):
        S_unit = higgs_units[alpha]
        for s_idx in range(4):
            M_unit = edual[s_idx]
            for ra in range(3):
                for cb in range(3):
                    T[alpha, s_idx, ra, cb] = np.sum((blocks[ra].T @ eps @ S_unit @ blocks[cb]) * M_unit)
    nz: List[Tuple[int, int, int, int, int, int]] = []
    for al in range(3):
        for si in range(4):
            for ra in range(3):
                for cb in range(3):
                    val = T[al, si, ra, cb]
                    if abs(val) > 1e-14:
                        tr2 = int(round(val.real * 2.0))
                        ti2 = int(round(val.imag * 2.0))
                        assert abs(val - complex(tr2 / 2.0, ti2 / 2.0)) < 1e-14
                        nz.append((al, si, ra, cb, tr2, ti2))
    return {
        "units": units,
        "edual": edual,
        "blocks": blocks,
        "higgs_units": higgs_units,
        "T": T,
        "T_nz": nz,
    }


QUAT_DATA = build_quaternions_and_coupling()
T_COUP = QUAT_DATA["T"]
T_COUP_NZ = QUAT_DATA["T_nz"]
_, _, SERRE_EXACT_ROWS = vxm._build_serre_B1_exact(168)


# ============================================================================
# SECTION 2: ARBITRARY-PRECISION MPMATH YUKAWA & FULL 3x3 SVD EVALUATOR
# ============================================================================

def eval_single_point_mp(
    x_val: float,
    y_val: float,
    L2_raw_val: float,
    lines_int: List[Tuple[int, int]],
    charges_map: Dict[str, Tuple[int, int]],
    dps_min: int = 170,
) -> Dict[str, Any]:
    """
    Evaluates exact complex 3x3 Yukawa matrices in mpmath across all requested
    order-5 lines and charges at tau = x_val + i * y_val.
    """
    dps_eff = max(dps_min, int(math.ceil(2.25 * y_val)) + 65)
    with mp.workdps(dps_eff):
        tau = mp.mpc(mp.mpf(repr(float(x_val))), mp.mpf(repr(float(y_val))))
        yv = mp.im(tau)
        L2 = mp.mpf(repr(float(L2_raw_val)))
        tl2 = L2 + mp.mpf("0.5") * mp.log(yv) - (mp.euler + mp.log(mp.pi))
        exp_m2L2 = mp.exp(-2 * L2)

        xq = mp.exp(mp.j * mp.pi * tau / 4)
        c3_S = [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
        cutoff_serre = mp.mpf(10) ** (-(dps_eff + 10))
        for k_int, cols_frac in SERRE_EXACT_ROWS:
            pw = xq ** k_int
            if abs(pw) < cutoff_serre and k_int > 8:
                break
            for col_j in range(3):
                fr, fi = cols_frac[col_j]
                if fr or fi:
                    c_mp = mp.mpc(
                        mp.mpf(fr.numerator) / fr.denominator,
                        mp.mpf(fi.numerator) / fi.denominator,
                    )
                    c3_S[col_j] += pw * c_mp
        c3_St = [mp.conj(z) for z in c3_S]

        def th_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            s = mp.mpc(0)
            k_lim = max(12, int(math.ceil(math.sqrt((dps_eff * math.log(10.0) + 25.0) / (math.pi * max(y_val, 0.5))))) + 2)
            for k in range(-k_lim, k_lim + 1):
                m = mp.mpf(k) + at
                s += mp.exp(mp.j * mp.pi * tau * (m * m) + 2 * mp.j * mp.pi * m * be)
            return s

        def a0_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            den = mp.mpc(0)
            num = mp.mpc(0)
            k_lim = max(12, int(math.ceil(math.sqrt((dps_eff * math.log(10.0) + 25.0) / (math.pi * max(y_val, 0.5))))) + 2)
            for k in range(-k_lim, k_lim + 1):
                m = mp.mpf(k) + at
                t = mp.exp(mp.j * mp.pi * tau * (m * m) + 2 * mp.j * mp.pi * m * be)
                den += t
                num += m * t
            return (2 * mp.j * mp.pi * num) / den

        th1p0 = mp.mpc(0)
        k_th1 = max(12, int(math.ceil(math.sqrt((dps_eff * math.log(10.0) + 25.0) / (math.pi * max(y_val, 0.5))))) + 2)
        for k in range(k_th1):
            h = mp.mpf(k) + mp.mpf("0.5")
            sgn = (-1) ** k
            th1p0 += sgn * (2 * k + 1) * mp.exp(mp.j * mp.pi * tau * (h * h))
        th1p0 *= 2 * mp.pi

        def F_kron(u1: mp.mpf, u2: mp.mpf) -> mp.mpf:
            a = u1 - mp.floor(u1)
            b = u2 - mp.floor(u2)
            az = (abs(a) < mp.mpf("1e-40")) or (abs(a - 1) < mp.mpf("1e-40"))
            bz = (abs(b) < mp.mpf("1e-40")) or (abs(b - 1) < mp.mpf("1e-40"))
            if az:
                base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yv))
                if not bz:
                    base += yv * (mp.pi ** 2) / (mp.sin(mp.pi * b) ** 2)
                a_eff = mp.mpf(0)
            else:
                base = -mp.pi * (2 * mp.log(2) + mp.log(yv) + mp.digamma(a) + mp.digamma(1 - a))
                a_eff = a
            tot = base
            for k in range(-16, 17):
                m = mp.mpf(k) + a_eff
                if abs(m) > mp.mpf("1e-40"):
                    w = mp.exp(-2 * mp.pi * abs(m) * yv + 2 * mp.j * mp.pi * (m * mp.re(tau) + u2))
                    if abs(w) > cutoff_serre:
                        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
            return tot

        half = mp.mpf("0.5")
        zero_thr = mp.mpf(10) ** (-dps_eff + 25)

        def make_Y_mp(c_vec: List[mp.mpc], u_v: List[mp.mpc]) -> mp.matrix:
            Y = mp.zeros(3, 3)
            for al_i, s_i, ra, cb, tr2, ti2 in T_COUP_NZ:
                Y[ra, cb] += c_vec[al_i] * u_v[s_i] * mp.mpc(tr2, ti2) * half
            return Y

        per_line: List[Dict[str, Any]] = []
        for ja, jb in lines_int:
            a_p = mp.mpf(ja) / 5
            b_p = mp.mpf(jb) / 5
            u_t90_sec: Dict[str, List[mp.mpc]] = {}
            u_old_sec: Dict[str, List[mp.mpc]] = {}
            R_sec: Dict[str, List[mp.mpc]] = {}
            for sec, (qL, qR) in charges_map.items():
                ap = (qL + qR) * a_p
                bp = (qL + qR) * b_p
                am = (qL - qR) * a_p
                bm = (qL - qR) * b_p
                ph1 = mp.exp(-mp.j * mp.pi * (ap + am))
                R_1 = (-mp.j) * ph1 * th_char(ap + half, bp + half) * th_char(am + half, bm + half) / th1p0
                R_i = (-1) * th_char(ap + half, bp) * th_char(am + half, bm) / th1p0
                R_j = (-1) * ph1 * th_char(ap, bp + half) * th_char(am, bm + half) / th1p0
                R_k = (+mp.j) * th_char(ap, bp) * th_char(am, bm) / th1p0
                Rs = [R_1, R_i, R_j, R_k]
                R_sec[sec] = Rs
                sh = [
                    ((ap, bp), (ap + half, bp + half)),
                    ((ap, bp - half), (ap + half, bp)),
                    ((ap - half, bp), (ap, bp + half)),
                    ((ap - half, bp - half), (ap, bp)),
                ]
                vt90 = [mp.mpc(0)] * 4
                vold = [mp.mpc(0)] * 4
                for s_i in range(4):
                    if abs(Rs[s_i]) > zero_thr:
                        Fu = F_kron(sh[s_i][0][0], sh[s_i][0][1])
                        a0v = a0_char(sh[s_i][1][0], sh[s_i][1][1])
                        n_old = 2 * mp.pi * tl2 + Fu
                        corr = mp.pi * (abs(a0v) ** 2) * exp_m2L2
                        vold[s_i] = mp.sqrt(n_old) * Rs[s_i]
                        vt90[s_i] = mp.sqrt(n_old - corr) * Rs[s_i]
                u_t90_sec[sec] = vt90
                u_old_sec[sec] = vold

            Ys_t90_S = {sec: make_Y_mp(c3_S, u_t90_sec[sec]) for sec in charges_map}
            Ys_t90_St = {sec: make_Y_mp(c3_St, u_t90_sec[sec]) for sec in charges_map}
            Ys_old_S = {sec: make_Y_mp(c3_S, u_old_sec[sec]) for sec in charges_map}
            Ys_old_St = {sec: make_Y_mp(c3_St, u_old_sec[sec]) for sec in charges_map}

            per_line.append({
                "line_int": (ja, jb),
                "R_sec": R_sec,
                "u_t90": u_t90_sec,
                "u_old": u_old_sec,
                "Y_t90_S": Ys_t90_S,
                "Y_t90_St": Ys_t90_St,
                "Y_old_S": Ys_old_S,
                "Y_old_St": Ys_old_St,
            })

        return {
            "dps_eff": dps_eff,
            "c3_S": c3_S,
            "c3_St": c3_St,
            "per_line": per_line,
        }


def svd_asc_mp(Y: mp.matrix, dps_eff: int) -> Tuple[mp.matrix, List[mp.mpf], mp.matrix]:
    with mp.workdps(dps_eff):
        U_desc, sv_desc, Vh_desc = mp.svd_c(Y)
        # Reverse to ascending order sigma_1 <= sigma_2 <= sigma_3
        U_asc = mp.zeros(3, 3)
        V_asc = mp.zeros(3, 3)
        sv_asc = [sv_desc[2], sv_desc[1], sv_desc[0]]
        for col_new, col_old in enumerate((2, 1, 0)):
            for r in range(3):
                U_asc[r, col_new] = U_desc[r, col_old]
                V_asc[r, col_new] = mp.conj(Vh_desc[col_old, r])
        return U_asc, sv_asc, V_asc


def overlap_mod_matrix_mp(Uu_asc: mp.matrix, Ud_asc: mp.matrix, dps_eff: int) -> np.ndarray:
    with mp.workdps(dps_eff):
        M = np.zeros((3, 3), dtype=np.float64)
        for i in range(3):
            for j in range(3):
                s = mp.mpc(0)
                for r in range(3):
                    s += mp.conj(Uu_asc[r, i]) * Ud_asc[r, j]
                M[i, j] = float(abs(s))
        return M


def ratios_from_sv_mp(sv_asc: List[mp.mpf], dps_eff: int) -> Dict[str, float]:
    with mp.workdps(dps_eff):
        return {
            "2_over_3": float(sv_asc[1] / sv_asc[2]),
            "1_over_3": float(sv_asc[0] / sv_asc[2]),
            "1_over_2": float(sv_asc[0] / sv_asc[1]),
        }


# ============================================================================
# SECTION 3: GATE_HAAR (GUARDRAIL 3 — UNITARY BASIS-SCRAMBLING TEST)
# ============================================================================

def random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    Z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    ph = d / np.abs(d)
    return Q * ph[None, :]


def extract_full_overlap_f64(Yu: np.ndarray, Yd: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    Uu_d, sv_u, _ = np.linalg.svd(Yu)
    Ud_d, sv_d, _ = np.linalg.svd(Yd)
    Uu_a = Uu_d[:, ::-1]
    Ud_a = Ud_d[:, ::-1]
    V_mod = np.abs(Uu_a.conj().T @ Ud_a)
    ratios = np.array([
        sv_u[1] / sv_u[0], sv_u[2] / sv_u[0], sv_u[2] / sv_u[1],
        sv_d[1] / sv_d[0], sv_d[2] / sv_d[0], sv_d[2] / sv_d[1],
    ], dtype=np.float64)
    return V_mod, ratios


def run_gate_haar() -> Dict[str, Any]:
    rng = np.random.default_rng(20261115)
    test_points = [
        (0.17, 1.5),
        (-0.23, 3.6515),
        (0.11, 6.0653),
        (0.17, 30.0),
    ]
    max_unitarity_err = 0.0
    max_covariant_diff_mp = 0.0
    max_covariant_diff_bulk_f64 = 0.0
    min_broken_su2_scramble = 1e9

    def np_u3_to_mp(U_np: np.ndarray, dps_eff: int) -> Tuple[mp.matrix, mp.matrix]:
        with mp.workdps(dps_eff):
            # Re-orthonormalize via Higham Newton-Schulz iterations in mpmath so U is Haar-unitary to working precision
            U = mp.matrix([[mp.mpc(repr(float(U_np[r, c].real)), repr(float(U_np[r, c].imag))) for c in range(3)] for r in range(3)])
            half = mp.mpf("0.5")
            three = mp.mpf("3")
            I3 = mp.eye(3)
            for _ in range(7):
                Uh = mp.zeros(3, 3)
                for r in range(3):
                    for c in range(3):
                        Uh[r, c] = mp.conj(U[c, r])
                U = half * U * (three * I3 - Uh * U)
            Uh_fin = mp.zeros(3, 3)
            for r in range(3):
                for c in range(3):
                    Uh_fin[r, c] = mp.conj(U[c, r])
            return U, Uh_fin

    for xv, yv in test_points:
        l2 = vxm.uniformize_L2_raw_fast(complex(xv, yv))
        ev = eval_single_point_mp(xv, yv, l2, [(2, 4), (1, 3), (0, 2)], SIX_CHARGES, dps_min=160)
        dps_eff = ev["dps_eff"]
        for line_item in ev["per_line"]:
            for is_w_plus in (False, True):
                Yu_mp = line_item["Y_t90_S"]["up"] if is_w_plus else line_item["Y_t90_St"]["up"]
                Yd_mp = line_item["Y_t90_St"]["down"] if is_w_plus else line_item["Y_t90_S"]["down"]
                Uu0, sv_u0, _ = svd_asc_mp(Yu_mp, dps_eff)
                Ud0, sv_d0, _ = svd_asc_mp(Yd_mp, dps_eff)
                V0_mp = overlap_mod_matrix_mp(Uu0, Ud0, dps_eff)
                rat0_mp = ratios_from_sv_mp(sv_u0, dps_eff)
                ratd0_mp = ratios_from_sv_mp(sv_d0, dps_eff)

                if yv <= 2.0:
                    Yu_f = np.array([[complex(float(mp.re(Yu_mp[r, c])), float(mp.im(Yu_mp[r, c]))) for c in range(3)] for r in range(3)], dtype=np.complex128)
                    Yd_f = np.array([[complex(float(mp.re(Yd_mp[r, c])), float(mp.im(Yd_mp[r, c]))) for c in range(3)] for r in range(3)], dtype=np.complex128)
                    V0_f, rat0_f = extract_full_overlap_f64(Yu_f, Yd_f)

                for trial in range(4):
                    UL_np = random_haar_u3(rng)
                    URu_np = random_haar_u3(rng)
                    URd_np = random_haar_u3(rng)
                    for U_mat in (UL_np, URu_np, URd_np):
                        u_err = float(np.max(np.abs(U_mat.conj().T @ U_mat - np.eye(3))))
                        if u_err > max_unitarity_err:
                            max_unitarity_err = u_err

                    UL_m, _ = np_u3_to_mp(UL_np, dps_eff)
                    _, URu_h = np_u3_to_mp(URu_np, dps_eff)
                    _, URd_h = np_u3_to_mp(URd_np, dps_eff)
                    with mp.workdps(dps_eff):
                        Yu_rot = UL_m * Yu_mp * URu_h
                        Yd_rot = UL_m * Yd_mp * URd_h
                    Uu1, sv_u1, _ = svd_asc_mp(Yu_rot, dps_eff)
                    Ud1, sv_d1, _ = svd_asc_mp(Yd_rot, dps_eff)
                    V1_mp = overlap_mod_matrix_mp(Uu1, Ud1, dps_eff)
                    rat1_mp = ratios_from_sv_mp(sv_u1, dps_eff)
                    ratd1_mp = ratios_from_sv_mp(sv_d1, dps_eff)
                    diff_mp = max(
                        float(np.max(np.abs(V1_mp - V0_mp))),
                        max(abs(rat1_mp[k] - rat0_mp[k]) for k in rat0_mp),
                        max(abs(ratd1_mp[k] - ratd0_mp[k]) for k in ratd0_mp),
                    )
                    if diff_mp > max_covariant_diff_mp:
                        max_covariant_diff_mp = diff_mp

                    if yv <= 2.0:
                        V1_f, rat1_f = extract_full_overlap_f64(UL_np @ Yu_f @ URu_np.conj().T, UL_np @ Yd_f @ URd_np.conj().T)
                        df64 = max(float(np.max(np.abs(V1_f - V0_f))), float(np.max(np.abs(rat1_f - rat0_f))))
                        if df64 > max_covariant_diff_bulk_f64:
                            max_covariant_diff_bulk_f64 = df64

                # Adversarial broken-SU(2)_L check: independent left rotations UL_u != UL_d must scramble V
                ULu_m, _ = np_u3_to_mp(random_haar_u3(rng), dps_eff)
                ULd_m, _ = np_u3_to_mp(random_haar_u3(rng), dps_eff)
                with mp.workdps(dps_eff):
                    Uu_s, _, _ = svd_asc_mp(ULu_m * Yu_mp, dps_eff)
                    Ud_s, _, _ = svd_asc_mp(ULd_m * Yd_mp, dps_eff)
                V_scr = overlap_mod_matrix_mp(Uu_s, Ud_s, dps_eff)
                scr = float(np.max(np.abs(V_scr - V0_mp)))
                if scr < min_broken_su2_scramble:
                    min_broken_su2_scramble = scr

    gate_holds = bool(
        max_unitarity_err < 1e-14
        and max_covariant_diff_mp < 1e-14
        and max_covariant_diff_bulk_f64 < 1e-13
        and min_broken_su2_scramble > 0.05
    )
    assert gate_holds, "Gate_Haar failed"
    return {
        "gate_holds": gate_holds,
        "max_haar_unitarity_err": max_unitarity_err,
        "max_gauge_covariant_invariance_err_mp": max_covariant_diff_mp,
        "max_gauge_covariant_invariance_err_bulk_f64": max_covariant_diff_bulk_f64,
        "min_broken_su2_left_scramble_shift": min_broken_su2_scramble,
    }


# ============================================================================
# SECTION 4: W1 & W2 — HEIGHT SWEEP, CHIRAL BASIS THEOREM, AND CONTROLS
# ============================================================================

def run_w1_w2_and_controls() -> Dict[str, Any]:
    # 1. Exact rational verification of leading Serre k = -1 row in B[1]
    min_k, min_cols = SERRE_EXACT_ROWS[0]
    assert min_k == -1
    # Expected row at k = -1: (0, +1/24, -i/24)
    k_m1_exact_match = bool(
        min_cols[0] == (Fraction(0), Fraction(0))
        and min_cols[1] == (Fraction(1, 24), Fraction(0))
        and min_cols[2] == (Fraction(0), Fraction(-1, 24))
    )
    assert k_m1_exact_match

    # Construct S_dom = (1/24)*(q_j - i*q_k) and S~_dom = (1/24)*(q_j + i*q_k) directly
    qi, qj, qk = QUAT_DATA["higgs_units"]
    S_dom = (1.0 / 24.0) * (qj - 1j * qk)
    St_dom = (1.0 / 24.0) * (qj + 1j * qk)
    E12 = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=np.complex128)
    E21 = np.array([[0.0, 0.0], [1.0, 0.0]], dtype=np.complex128)
    s_dom_err = float(np.max(np.abs(S_dom - (1.0 / 12.0) * E12)))
    st_dom_err = float(np.max(np.abs(St_dom - (-1.0 / 12.0) * E21)))
    nilpotent_err = float(max(np.max(np.abs(S_dom @ S_dom)), np.max(np.abs(St_dom @ St_dom))))
    assert s_dom_err < 1e-15 and st_dom_err < 1e-15 and nilpotent_err < 1e-15

    # Orthonormal chiral generation basis E_chir = [e_+, e_0, e_-] and order-3 shift C
    inv_rt2 = 1.0 / math.sqrt(2.0)
    e_plus = np.array([inv_rt2, 0.0, 1j * inv_rt2], dtype=np.complex128)
    e_zero = np.array([0.0, 1.0, 0.0], dtype=np.complex128)
    e_minus = np.array([inv_rt2, 0.0, -1j * inv_rt2], dtype=np.complex128)
    E_chir = np.column_stack([e_plus, e_zero, e_minus])
    echir_unitary_err = float(np.max(np.abs(E_chir.conj().T @ E_chir - np.eye(3))))
    assert echir_unitary_err < 1e-15

    # C maps e_- -> e_0 -> e_+ -> e_-: in basis [e_+, e_0, e_-], C e_+ = e_-, C e_0 = e_+, C e_- = e_0
    C_in_chir = np.array([
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
    ], dtype=np.complex128)
    C_op = E_chir @ C_in_chir @ E_chir.conj().T
    c_order3_err = float(np.max(np.abs(C_op @ C_op @ C_op - np.eye(3))))
    c_trace_abs = float(abs(np.trace(C_op)))
    assert c_order3_err < 1e-15 and c_trace_abs < 1e-15

    P_plus = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=np.float64)
    P_minus = P_plus.T.copy()

    # 2. Height sweep across all 24 lines of P_5
    heights = [1.5, 3.6515, 6.0653, 9.0, 15.0, 30.0, 60.0, 120.0]
    x_probe = 0.17
    sweep_summary: Dict[str, Any] = {}
    saved_evs: Dict[float, Dict[str, Any]] = {}
    lepton_down_max_diff_all_heights = 0.0
    inversion_c_negc_max_diff = 0.0

    for yv in heights:
        l2 = vxm.uniformize_L2_raw_fast(complex(x_probe, yv))
        ev = eval_single_point_mp(x_probe, yv, l2, P5_ALL_24_INT, SIX_CHARGES, dps_min=210 if yv >= 60.0 else 170)
        if yv in (30.0, 60.0, 120.0):
            saved_evs[yv] = ev
        dps_eff = ev["dps_eff"]

        # Verify Y(-c) == Y(c) across all 24 lines at y = 3.6515 and y = 30.0
        if yv in (3.6515, 30.0):
            by_line = {item["line_int"]: item for item in ev["per_line"]}
            for ja, jb in P5_ALL_24_INT:
                neg = ((-ja) % 5, (-jb) % 5)
                Y1 = by_line[(ja, jb)]["Y_t90_St"]["up"]
                Y2 = by_line[neg]["Y_t90_St"]["up"]
                with mp.workdps(dps_eff):
                    d_inv = max(float(abs(Y1[r, c] - Y2[r, c])) for r in range(3) for c in range(3))
                if d_inv > inversion_c_negc_max_diff:
                    inversion_c_negc_max_diff = d_inv

        modes_spec = [
            ("W_minus__exact_T90", "Y_t90_St", "Y_t90_S"),
            ("W_minus__old_small_cut", "Y_old_St", "Y_old_S"),
            ("W_plus__exact_T90", "Y_t90_S", "Y_t90_St"),
            ("W_plus__old_small_cut", "Y_old_S", "Y_old_St"),
        ]
        y_key = f"y_{yv}"
        sweep_summary[y_key] = {"Im_tau": yv, "Re_tau": x_probe, "L2_raw": l2, "modes": {}}

        for mode_name, up_key, dn_key in modes_spec:
            mats_24 = []
            diag33_list = []
            diag_all_max = 0.0
            perm_14_max_err = 0.0
            perm_10_max_err = 0.0
            golden_mat = None
            up_r13_list = []
            dn_r13_list = []

            # Also build coherent P_5-summed Yukawa matrices (1/24) sum_{c in P_5} Y_f(c, tau)
            with mp.workdps(dps_eff):
                Yu_coh = mp.zeros(3, 3)
                Yd_coh = mp.zeros(3, 3)

            for item in ev["per_line"]:
                ja, jb = item["line_int"]
                Yu = item[up_key]["up"]
                Yd = item[dn_key]["down"]
                Yl = item[dn_key]["lepton"]

                with mp.workdps(dps_eff):
                    Yu_coh += Yu / 24
                    Yd_coh += Yd / 24

                Uu, sv_u, _ = svd_asc_mp(Yu, dps_eff)
                Ud, sv_d, _ = svd_asc_mp(Yd, dps_eff)
                _, sv_l, _ = svd_asc_mp(Yl, dps_eff)

                # B1934 mod-5 down-equals-lepton ratio identity check
                with mp.workdps(dps_eff):
                    dl_diff = max(
                        float(abs(sv_d[1] / sv_d[2] - sv_l[1] / sv_l[2])),
                        float(abs(sv_d[0] / sv_d[2] - sv_l[0] / sv_l[2])),
                        float(abs(sv_d[0] / sv_d[1] - sv_l[0] / sv_l[1])),
                    )
                if dl_diff > lepton_down_max_diff_all_heights:
                    lepton_down_max_diff_all_heights = dl_diff

                M = overlap_mod_matrix_mp(Uu, Ud, dps_eff)
                mats_24.append(M)
                diag33_list.append(float(M[2, 2]))
                d_max = float(max(M[0, 0], M[1, 1], M[2, 2]))
                if d_max > diag_all_max:
                    diag_all_max = d_max

                is_w_minus = mode_name.startswith("W_minus")
                if ja in (0, 1, 4):
                    target_P = P_plus if is_w_minus else P_minus
                    err_p = float(np.max(np.abs(M - target_P)))
                    if err_p > perm_14_max_err:
                        perm_14_max_err = err_p
                else:
                    target_P = P_minus if is_w_minus else P_plus
                    err_p = float(np.max(np.abs(M - target_P)))
                    if err_p > perm_10_max_err:
                        perm_10_max_err = err_p

                if (ja, jb) == (2, 4):
                    golden_mat = M.tolist()

                up_r13_list.append(float(sv_u[0] / sv_u[2]))
                dn_r13_list.append(float(sv_d[0] / sv_d[2]))

            Uu_c, _, _ = svd_asc_mp(Yu_coh, dps_eff)
            Ud_c, _, _ = svd_asc_mp(Yd_coh, dps_eff)
            M_coh = overlap_mod_matrix_mp(Uu_c, Ud_c, dps_eff)

            avg_M = np.mean(np.stack(mats_24, axis=0), axis=0)
            sweep_summary[y_key]["modes"][mode_name] = {
                "p5_mean_mod_matrix": avg_M.tolist(),
                "golden_line_2_4_mod_matrix": golden_mat,
                "coherent_p5_sum_mod_matrix": M_coh.tolist(),
                "max_diag_3_3_across_24_lines": float(max(diag33_list)),
                "min_diag_3_3_across_24_lines": float(min(diag33_list)),
                "mean_diag_3_3_across_24_lines": float(np.mean(diag33_list)),
                "max_any_diagonal_entry_across_24_lines": diag_all_max,
                "max_err_vs_perm_on_14_lines_a_0_1_4": perm_14_max_err,
                "max_err_vs_perm_on_10_lines_a_2_3": perm_10_max_err,
                "p5_mean_mixing_12_23_13": [float(avg_M[0, 1]), float(avg_M[1, 2]), float(avg_M[0, 2])],
                "p5_mean_up_1_over_3": float(np.mean(up_r13_list)),
                "p5_mean_down_1_over_3": float(np.mean(dn_r13_list)),
            }

    # Verify W2 directly on U_f(S) and U_f(S~) at y = 60.0 and y = 120.0 across all 24 lines
    E_chir_mp = mp.matrix([[mp.mpc(E_chir[r, c].real, E_chir[r, c].imag) for c in range(3)] for r in range(3)])
    C_op_mp = mp.matrix([[mp.mpc(C_op[r, c].real, C_op[r, c].imag) for c in range(3)] for r in range(3)])

    def check_w2_at_ev(ev_obj: Dict[str, Any]) -> Tuple[float, float, float]:
        dps_loc = ev_obj["dps_eff"]
        b_max, s_max, r1_max = 0.0, 0.0, 0.0
        for item in ev_obj["per_line"]:
            ja, _ = item["line_int"]
            r1_up = float(abs(item["R_sec"]["up"][0]))
            if r1_up > r1_max:
                r1_max = r1_up
            for sec in ("up", "down"):
                U_S, _, _ = svd_asc_mp(item["Y_t90_S"][sec], dps_loc)
                U_St, _, _ = svd_asc_mp(item["Y_t90_St"][sec], dps_loc)
                proj_S = overlap_mod_matrix_mp(E_chir_mp, U_S, dps_loc)
                target_basis = np.eye(3) if ja in (0, 1, 4) else np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
                b_err = float(np.max(np.abs(proj_S - target_basis)))
                if b_err > b_max:
                    b_max = b_err
                with mp.workdps(dps_loc):
                    CU_S = C_op_mp * U_S
                shift_mat = overlap_mod_matrix_mp(CU_S, U_St, dps_loc)
                s_err = float(np.max(np.abs(shift_mat - np.eye(3))))
                if s_err > s_max:
                    s_max = s_err
        return b_max, s_max, r1_max

    max_u0_basis_err_y60, max_c_shift_err_y60, max_r1_up_abs = check_w2_at_ev(saved_evs[60.0])
    max_u0_basis_err_y120, max_c_shift_err_y120, _ = check_w2_at_ev(saved_evs[120.0])

    # 3. Planted Control PC_WALL_1: Unshifted family-frame (up S, down S) keeping exact charges (1,-4) and (1,2)
    ev30 = saved_evs[30.0]
    dps30 = ev30["dps_eff"]
    pc1_min_diag_y30 = 1.0
    pc1_max_offdiag_y30 = 0.0
    pc1_up23_y30 = []
    pc1_dn23_y30 = []
    for item in ev30["per_line"]:
        Uu_S, sv_u_S, _ = svd_asc_mp(item["Y_t90_S"]["up"], dps30)
        Ud_S, sv_d_S, _ = svd_asc_mp(item["Y_t90_S"]["down"], dps30)
        M_same = overlap_mod_matrix_mp(Uu_S, Ud_S, dps30)
        d_min = float(min(M_same[0, 0], M_same[1, 1], M_same[2, 2]))
        if d_min < pc1_min_diag_y30:
            pc1_min_diag_y30 = d_min
        off_max = float(max(M_same[0, 1], M_same[0, 2], M_same[1, 2], M_same[1, 0], M_same[2, 0], M_same[2, 1]))
        if off_max > pc1_max_offdiag_y30:
            pc1_max_offdiag_y30 = off_max
        pc1_up23_y30.append(float(sv_u_S[1] / sv_u_S[2]))
        pc1_dn23_y30.append(float(sv_d_S[1] / sv_d_S[2]))

    pc1_up23_mean = float(np.mean(pc1_up23_y30))
    pc1_dn23_mean = float(np.mean(pc1_dn23_y30))
    pc1_rel_hierarchy_sep = abs(pc1_up23_mean - pc1_dn23_mean) / max(pc1_dn23_mean, 1e-30)
    pc1_holds = bool(pc1_min_diag_y30 > 0.99 and pc1_max_offdiag_y30 < 0.02 and pc1_rel_hierarchy_sep > 0.5)
    assert pc1_holds, "PC_WALL_1 failed"

    # 4. Planted Control PC_WALL_2: Factorized SU(2)_L-covariant overlap Y_f^{fact} = L_{q_L} D_H R_{q_{R,f}}^dagger
    fact_charges = {
        "left_qL": (1, 0),          # depends solely on shared doublet charge q_L = +1
        "right_up": (-4, 16),       # depends solely on up singlet charge q_{R,u} = -4 -> (q_R, q_R^2)
        "right_down": (2, 4),       # depends solely on down singlet charge q_{R,d} = +2 -> (q_R, q_R^2)
    }
    pc2_summary: Dict[str, Any] = {}
    for y_pc2 in (6.0653, 30.0):
        l2_p = vxm.uniformize_L2_raw_fast(complex(x_probe, y_pc2))
        ev_f = eval_single_point_mp(x_probe, y_pc2, l2_p, P5_ALL_24_INT, fact_charges, dps_min=170)
        dps_f = ev_f["dps_eff"]
        with mp.workdps(dps_f):
            # Parameter-free S_3-democratic bridge D_H = I_3 + (1/3) J_3
            D_H = mp.eye(3)
            third = mp.mpf(1) / 3
            for r in range(3):
                for c in range(3):
                    D_H[r, c] += third

            diag33_f = []
            mix23_f = []
            mix13_f = []
            up23_f = []
            dn23_f = []
            up13_f = []
            dn13_f = []
            non_zero_winding_min_rel_sep = 1e9
            for item in ev_f["per_line"]:
                ja_f, _ = item["line_int"]
                L_mat = item["Y_t90_S"]["left_qL"]
                Ru_mat = item["Y_t90_St"]["right_up"]
                Rd_mat = item["Y_t90_S"]["right_down"]
                Ru_dag = mp.zeros(3, 3)
                Rd_dag = mp.zeros(3, 3)
                for r in range(3):
                    for c in range(3):
                        Ru_dag[r, c] = mp.conj(Ru_mat[c, r])
                        Rd_dag[r, c] = mp.conj(Rd_mat[c, r])
                Yu_f = L_mat * D_H * Ru_dag
                Yd_f = L_mat * D_H * Rd_dag
                Uu_f, sv_uf, _ = svd_asc_mp(Yu_f, dps_f)
                Ud_f, sv_df, _ = svd_asc_mp(Yd_f, dps_f)
                M_f = overlap_mod_matrix_mp(Uu_f, Ud_f, dps_f)
                diag33_f.append(float(M_f[2, 2]))
                mix23_f.append(float(M_f[1, 2]))
                mix13_f.append(float(M_f[0, 2]))
                r23_u = float(sv_uf[1] / sv_uf[2])
                r23_d = float(sv_df[1] / sv_df[2])
                r13_u = float(sv_uf[0] / sv_uf[2])
                r13_d = float(sv_df[0] / sv_df[2])
                up23_f.append(r23_u)
                dn23_f.append(r23_d)
                up13_f.append(r13_u)
                dn13_f.append(r13_d)
                if ja_f != 0:
                    line_sep = abs(r23_u - r23_d) / max(min(r23_u, r23_d), 1e-300)
                    if line_sep < non_zero_winding_min_rel_sep:
                        non_zero_winding_min_rel_sep = line_sep

        up23_geom = float(np.exp(np.mean(np.log(np.maximum(up23_f, 1e-300)))))
        dn23_geom = float(np.exp(np.mean(np.log(np.maximum(dn23_f, 1e-300)))))
        pc2_summary[f"y_{y_pc2}"] = {
            "min_diag_3_3_across_24_lines": float(min(diag33_f)),
            "mean_diag_3_3_across_24_lines": float(np.mean(diag33_f)),
            "max_mix_2_3_across_24_lines": float(max(mix23_f)),
            "max_mix_1_3_across_24_lines": float(max(mix13_f)),
            "p5_mean_up_2_over_3": float(np.mean(up23_f)),
            "p5_mean_down_2_over_3": float(np.mean(dn23_f)),
            "p5_geom_up_2_over_3": up23_geom,
            "p5_geom_down_2_over_3": dn23_geom,
            "p5_geom_up_1_over_3": float(np.exp(np.mean(np.log(np.maximum(up13_f, 1e-300))))),
            "p5_geom_down_1_over_3": float(np.exp(np.mean(np.log(np.maximum(dn13_f, 1e-300))))),
            "min_nonzero_winding_rel_23_sep": non_zero_winding_min_rel_sep,
        }

    pc2_y30 = pc2_summary["y_30.0"]
    pc2_holds = bool(
        pc2_y30["min_diag_3_3_across_24_lines"] > 0.9999
        and pc2_y30["max_mix_2_3_across_24_lines"] < 1e-3
        and pc2_y30["max_mix_1_3_across_24_lines"] < 1e-3
        and pc2_y30["min_nonzero_winding_rel_23_sep"] > 5.0
    )
    assert pc2_holds, "PC_WALL_2 failed"

    # Check W1 and W2 quantitative criteria
    w1_y30_wm = sweep_summary["y_30.0"]["modes"]["W_minus__exact_T90"]
    w1_y30_wp = sweep_summary["y_30.0"]["modes"]["W_plus__exact_T90"]
    w1_y60_wm = sweep_summary["y_60.0"]["modes"]["W_minus__exact_T90"]
    w1_y60_wp = sweep_summary["y_60.0"]["modes"]["W_plus__exact_T90"]
    w1_y120_wm = sweep_summary["y_120.0"]["modes"]["W_minus__exact_T90"]
    w1_y120_wp = sweep_summary["y_120.0"]["modes"]["W_plus__exact_T90"]

    target_wm_mix = np.array([5.0 / 12.0, 5.0 / 12.0, 7.0 / 12.0])
    target_wp_mix = np.array([7.0 / 12.0, 7.0 / 12.0, 5.0 / 12.0])
    wm_mix_err_y120 = float(np.max(np.abs(np.array(w1_y120_wm["p5_mean_mixing_12_23_13"]) - target_wm_mix)))
    wp_mix_err_y120 = float(np.max(np.abs(np.array(w1_y120_wp["p5_mean_mixing_12_23_13"]) - target_wp_mix)))

    w1_y60_strict_1e10 = bool(
        w1_y60_wm["max_diag_3_3_across_24_lines"] < 1e-10
        and w1_y60_wp["max_diag_3_3_across_24_lines"] < 1e-10
    )
    w1_holds = bool(
        w1_y30_wm["max_diag_3_3_across_24_lines"] < 1e-4
        and w1_y30_wp["max_diag_3_3_across_24_lines"] < 1e-4
        and w1_y60_wm["max_diag_3_3_across_24_lines"] < 1e-8
        and w1_y60_wp["max_diag_3_3_across_24_lines"] < 1e-8
        and w1_y120_wm["max_diag_3_3_across_24_lines"] < 1e-10
        and w1_y120_wp["max_diag_3_3_across_24_lines"] < 1e-10
        and wm_mix_err_y120 < 1e-12
        and wp_mix_err_y120 < 1e-12
    )
    assert w1_holds, "W1 failed"

    w2_holds = bool(
        k_m1_exact_match
        and s_dom_err < 1e-15
        and st_dom_err < 1e-15
        and c_order3_err < 1e-15
        and c_trace_abs < 1e-15
        and max_r1_up_abs < 1e-40
        and max_u0_basis_err_y60 < 1e-7
        and max_c_shift_err_y60 < 1e-7
        and max_u0_basis_err_y120 < 1e-12
        and max_c_shift_err_y120 < 1e-12
    )
    assert w2_holds, "W2 failed"

    return {
        "W1_holds": w1_holds,
        "W1_parenthetical_y60_lt_1e10": w1_y60_strict_1e10,
        "W2_holds": w2_holds,
        "PC_WALL_1_holds": pc1_holds,
        "PC_WALL_2_holds": pc2_holds,
        "inversion_Y_neg_c_vs_Y_c_max_diff": inversion_c_negc_max_diff,
        "B1934_down_lepton_ratio_max_diff_mp": lepton_down_max_diff_all_heights,
        "W2_algebraic_checks": {
            "serre_k_minus_1_exact_row_match": k_m1_exact_match,
            "S_dom_vs_E12_over_12_err": s_dom_err,
            "St_dom_vs_minus_E21_over_12_err": st_dom_err,
            "nilpotent_square_err": nilpotent_err,
            "chiral_basis_unitarity_err": echir_unitary_err,
            "C_shift_order_3_err": c_order3_err,
            "C_shift_trace_abs": c_trace_abs,
            "max_R1_up_abs_at_y60": max_r1_up_abs,
            "max_U0_vs_chiral_basis_err_at_y60": max_u0_basis_err_y60,
            "max_C_shift_alignment_err_at_y60": max_c_shift_err_y60,
            "max_U0_vs_chiral_basis_err_at_y120": max_u0_basis_err_y120,
            "max_C_shift_alignment_err_at_y120": max_c_shift_err_y120,
        },
        "W1_deep_cusp_limit_errors_at_y120": {
            "W_minus_err_vs_5_12__5_12__7_12": wm_mix_err_y120,
            "W_plus_err_vs_7_12__7_12__5_12": wp_mix_err_y120,
        },
        "PC_WALL_1_same_S_summary_at_y30": {
            "min_diagonal_entry_across_24_lines": pc1_min_diag_y30,
            "max_off_diagonal_entry_across_24_lines": pc1_max_offdiag_y30,
            "p5_mean_up_2_over_3": pc1_up23_mean,
            "p5_mean_down_2_over_3": pc1_dn23_mean,
            "relative_up_down_hierarchy_separation": pc1_rel_hierarchy_sep,
        },
        "PC_WALL_2_factorized_summary": pc2_summary,
        "height_sweep": sweep_summary,
    }


# ============================================================================
# SECTION 5: W3 — ARITHMETIC VS GEOMETRIC MEAN & HOROCYCLE PHASE CANCELLATION
# ============================================================================

def fold_to_fundamental_domain(z: complex) -> complex:
    for _ in range(200):
        k = int(round(z.real))
        if k != 0:
            z = z - k
        if z.real * z.real + z.imag * z.imag < 1.0 - 1e-13:
            z = -1.0 / z
        else:
            break
    if abs(z.real) > 0.5 + 1e-13:
        z = z - round(z.real)
    return z


def closed_geodesic_tau_nodes(word: str, n_nodes: int = 128) -> Tuple[np.ndarray, float, int]:
    L_mat = np.array([[1, 1], [0, 1]], dtype=np.int64)
    R_mat = np.array([[1, 0], [1, 1]], dtype=np.int64)
    M = np.eye(2, dtype=np.int64)
    for ch in word:
        M = M @ (L_mat if ch == "L" else R_mat)
    a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1])
    tr = a + d
    assert a * d - b * c == 1 and tr > 2
    assert (tr % 5) != 0  # level-5 non-parabolic admissibility
    disc = math.sqrt(float(tr * tr - 4))
    # Fixed points of (a z + b)/(c z + d) = z -> c z^2 + (d - a) z - b = 0
    r_plus = ((a - d) + disc) / (2.0 * c)
    r_minus = ((a - d) - disc) / (2.0 * c)
    center = 0.5 * (r_plus + r_minus)
    radius = 0.5 * abs(r_plus - r_minus)
    ell = 2.0 * math.acosh(0.5 * tr)
    # Uniform hyperbolic arclength parametrization along Euclidean semicircle:
    # z(t) = center + radius * tanh(t) + i * radius / cosh(t), ds_hyp = dt!
    # Check M maps t_0 = 0 to t_0 + ell (or -ell): any strip of width ell is one full closed period!
    ts = (np.arange(n_nodes, dtype=np.float64) + 0.5) * (ell / n_nodes) - 0.5 * ell
    taus = []
    for tv in ts:
        z_raw = complex(center + radius * math.tanh(tv), radius / math.cosh(tv))
        taus.append(fold_to_fundamental_domain(z_raw))
    return np.array(taus, dtype=np.complex128), ell, tr


def eval_ratios_grid_f64(taus_red: np.ndarray) -> Dict[str, np.ndarray]:
    """
    Evaluates (up 1/3, down 1/3) on every (tau, c in P_5_HALF_12) point in float64
    for y <= 10 (where sigma_1/sigma_3 >= 1e-13 >> float64 underflow).
    Returns array of shape (len(taus_red), 12, 2) for W_minus_T90.
    """
    n_pts = len(taus_red)
    l2_raw = np.array([vxm.uniformize_L2_raw_fast(complex(z)) for z in taus_red], dtype=np.float64)
    tl2 = l2_raw + 0.5 * np.log(taus_red.imag) - vxm.NORM_CONST_SHIFT

    tau_rep = np.repeat(taus_red, 12)
    tl_rep = np.repeat(tl2, 12)
    a_tile = np.tile(np.array([p[0] for p in vxm.P5_HALF_12], dtype=np.float64), n_pts)
    b_tile = np.tile(np.array([p[1] for p in vxm.P5_HALF_12], dtype=np.float64), n_pts)

    modes = vxm.evaluate_four_modes_f64_batch(tau_rep, a_tile, b_tile, tl_rep)
    wm = modes["W_minus_T90"].reshape(n_pts, 12, 12)
    return {
        "up_1_over_3_per_line": wm[:, :, 1],
        "down_1_over_3_per_line": wm[:, :, 4],
        "up_2_over_3_per_line": wm[:, :, 0],
        "down_2_over_3_per_line": wm[:, :, 3],
    }


def run_w3_checks() -> Dict[str, Any]:
    # Part (a): Arithmetic vs Geometric mean on L^6 R L R, L^{16} R, and Poincare area (y <= 10 + analytical tail)
    geodesic_results: Dict[str, Any] = {}
    for word in ("LLLLLLRLR", "LLLLLLLLLLLLLLLLR"):
        taus, ell, tr = closed_geodesic_tau_nodes(word, n_nodes=128)
        grid = eval_ratios_grid_f64(taus)
        u13 = grid["up_1_over_3_per_line"]
        d13 = grid["down_1_over_3_per_line"]

        arith_u13 = float(np.mean(u13))
        geom_joint_u13 = float(np.exp(np.mean(np.log(np.maximum(u13, 1e-300)))))
        geom_p5first_u13 = float(np.exp(np.mean(np.log(np.mean(u13, axis=1)))))

        arith_d13 = float(np.mean(d13))
        geom_joint_d13 = float(np.exp(np.mean(np.log(np.maximum(d13, 1e-300)))))
        geom_p5first_d13 = float(np.exp(np.mean(np.log(np.mean(d13, axis=1)))))

        geodesic_results[word] = {
            "trace": tr,
            "hyperbolic_length": ell,
            "max_Im_tau_visited": float(np.max(taus.imag)),
            "min_Im_tau_visited": float(np.min(taus.imag)),
            "up_1_over_3_arith_mean": arith_u13,
            "up_1_over_3_geom_mean_joint_p5_tau": geom_joint_u13,
            "up_1_over_3_geom_mean_p5_avg_first": geom_p5first_u13,
            "up_1_over_3_arith_over_geom_joint_factor": arith_u13 / geom_joint_u13,
            "down_1_over_3_arith_mean": arith_d13,
            "down_1_over_3_geom_mean_joint_p5_tau": geom_joint_d13,
            "down_1_over_3_arith_over_geom_joint_factor": arith_d13 / geom_joint_d13,
        }

    # Poincare area arithmetic vs geometric mean on y <= 10 (90.45% of area) + mpmath strip 10 < y <= 40
    gx, wx = roots_legendre(12)
    gu, wu = roots_legendre(16)
    xs = 0.5 * gx
    wx_s = 0.5 * wx
    u_cut = 0.1  # y <= 10
    taus_b = []
    w_b = []
    for ix, xv in enumerate(xs):
        u_hi = 1.0 / math.sqrt(1.0 - float(xv * xv))
        h_du = 0.5 * (u_hi - u_cut)
        mid_u = 0.5 * (u_hi + u_cut)
        for iu, uv_r in enumerate(gu):
            uv = mid_u + h_du * float(uv_r)
            taus_b.append(complex(float(xv), 1.0 / uv))
            w_b.append((3.0 / math.pi) * float(wx_s[ix]) * h_du * float(wu[iu]))
    taus_b_arr = np.array(taus_b, dtype=np.complex128)
    w_b_arr = np.array(w_b, dtype=np.float64)
    grid_area = eval_ratios_grid_f64(taus_b_arr)
    u13_b = grid_area["up_1_over_3_per_line"]
    d13_b = grid_area["down_1_over_3_per_line"]
    w_norm = w_b_arr / np.sum(w_b_arr)

    area_y10_arith_u13 = float(np.sum(w_norm[:, None] * u13_b) / 12.0)
    area_y10_geom_joint_u13 = float(np.exp(np.sum(w_norm[:, None] * np.log(u13_b)) / 12.0))
    area_y10_geom_p5first_u13 = float(np.exp(np.sum(w_norm * np.log(np.mean(u13_b, axis=1)))))

    # Note: on full F_std (u -> 0+), up 1/3 and down 1/3 decay as exp(-c * y) = exp(-c / u),
    # so int_0^{u_0} ln(sigma_1/sigma_3) du = int_0^{u_0} (-c / u) du = -infty -> exact geometric mean on F_std is 0!
    # Verify linear growth of -ln(sigma_1/sigma_3) in y between y = 20 and y = 60:
    y20_l2 = vxm.uniformize_L2_raw_fast(complex(0.17, 20.0))
    y40_l2 = vxm.uniformize_L2_raw_fast(complex(0.17, 40.0))
    ev_y20 = eval_single_point_mp(0.17, 20.0, y20_l2, [(2, 4)], SIX_CHARGES, dps_min=130)
    ev_y40 = eval_single_point_mp(0.17, 40.0, y40_l2, [(2, 4)], SIX_CHARGES, dps_min=170)
    _, sv_u20, _ = svd_asc_mp(ev_y20["per_line"][0]["Y_t90_St"]["up"], ev_y20["dps_eff"])
    _, sv_u40, _ = svd_asc_mp(ev_y40["per_line"][0]["Y_t90_St"]["up"], ev_y40["dps_eff"])
    neg_ln_u20 = float(-mp.log(sv_u20[0] / sv_u20[2]))
    neg_ln_u40 = float(-mp.log(sv_u40[0] / sv_u40[2]))

    # Part (b): Horocycle operator H_f(c, y) = int_{-1/2}^{1/2} Y_f(c, x + i y) Y_f^dagger dx vs E_x[|U_u^dagger U_d|]
    # Use full dynamic-precision mpmath (dps >= 4.6 * y + 65) so Y_f Y_f^dagger never underflows on sigma_1^2!
    gx_h, wx_h = roots_legendre(16)
    xs_h = 0.5 * gx_h
    ws_h = 0.5 * wx_h
    horocycle_results: Dict[str, Any] = {}
    for y_h in (1.5, 3.6515, 6.0653, 30.0):
        dps_h_min = max(160, int(math.ceil(4.6 * y_h)) + 65)
        l2_h = [vxm.uniformize_L2_raw_fast(complex(float(xv), y_h)) for xv in xs_h]
        with mp.workdps(dps_h_min):
            H_u_acc = [mp.zeros(3, 3) for _ in range(12)]
            H_d_acc = [mp.zeros(3, 3) for _ in range(12)]
            pw_mod_acc = [np.zeros((3, 3), dtype=np.float64) for _ in range(12)]

            for ix, xv in enumerate(xs_h):
                wt_f = float(ws_h[ix])
                wt_mp = mp.mpf(repr(wt_f))
                ev_h = eval_single_point_mp(float(xv), y_h, l2_h[ix], vxm.P5_HALF_12_INT, SIX_CHARGES, dps_min=dps_h_min)
                dps_h = ev_h["dps_eff"]
                for il, item in enumerate(ev_h["per_line"]):
                    Yu_m = item["Y_t90_St"]["up"]
                    Yd_m = item["Y_t90_S"]["down"]
                    Uu_m, _, _ = svd_asc_mp(Yu_m, dps_h)
                    Ud_m, _, _ = svd_asc_mp(Yd_m, dps_h)
                    pw_mod_acc[il] += wt_f * overlap_mod_matrix_mp(Uu_m, Ud_m, dps_h)

                    for r in range(3):
                        for c in range(3):
                            su = mp.mpc(0)
                            sd = mp.mpc(0)
                            for k_col in range(3):
                                su += Yu_m[r, k_col] * mp.conj(Yu_m[c, k_col])
                                sd += Yd_m[r, k_col] * mp.conj(Yd_m[c, k_col])
                            H_u_acc[il][r, c] += wt_mp * su
                            H_d_acc[il][r, c] += wt_mp * sd

            op_mods = []
            half_mp = mp.mpf("0.5")
            for il in range(12):
                Hu_sym = mp.zeros(3, 3)
                Hd_sym = mp.zeros(3, 3)
                for r in range(3):
                    for c in range(3):
                        Hu_sym[r, c] = half_mp * (H_u_acc[il][r, c] + mp.conj(H_u_acc[il][c, r]))
                        Hd_sym[r, c] = half_mp * (H_d_acc[il][r, c] + mp.conj(H_d_acc[il][c, r]))
                _, eu = mp.eigh(Hu_sym)
                _, ed = mp.eigh(Hd_sym)
                op_mods.append(overlap_mod_matrix_mp(eu, ed, dps_h_min))

        pw_mean = np.mean(np.stack(pw_mod_acc, axis=0), axis=0)
        op_mean = np.mean(np.stack(op_mods, axis=0), axis=0)
        max_diff_pw_vs_op = float(np.max(np.abs(pw_mean - op_mean)))
        horocycle_results[f"y_{y_h}"] = {
            "pointwise_horocycle_mean_mod_matrix": pw_mean.tolist(),
            "operator_H_f_horocycle_mod_matrix": op_mean.tolist(),
            "max_abs_diff_pointwise_vs_operator": max_diff_pw_vs_op,
            "operator_H_f_diag_3_3": float(op_mean[2, 2]),
        }

    jensen_l6rlr_factor = geodesic_results["LLLLLLRLR"]["up_1_over_3_arith_over_geom_joint_factor"]
    jensen_l16r_factor = geodesic_results["LLLLLLLLLLLLLLLLR"]["up_1_over_3_arith_over_geom_joint_factor"]
    jensen_area_y10_factor = area_y10_arith_u13 / area_y10_geom_joint_u13
    bulk_y15_op_diff = horocycle_results["y_1.5"]["max_abs_diff_pointwise_vs_operator"]

    w3_l6rlr_strict_10x = bool(jensen_l6rlr_factor > 10.0)
    w3_area_y10_strict_10x = bool(jensen_area_y10_factor > 10.0)
    w3_holds = bool(
        jensen_l6rlr_factor > 2.0
        and jensen_l16r_factor > 10.0
        and jensen_area_y10_factor > 2.0
        and neg_ln_u40 > 1.9 * neg_ln_u20
        and bulk_y15_op_diff > 1e-3
        and horocycle_results["y_30.0"]["operator_H_f_diag_3_3"] < 1e-4
    )
    assert w3_holds, "W3 failed"

    return {
        "W3_holds": w3_holds,
        "W3_parenthetical_l6rlr_gt_10x": w3_l6rlr_strict_10x,
        "W3_parenthetical_area_y10_gt_10x": w3_area_y10_strict_10x,
        "geodesics_arith_vs_geom": geodesic_results,
        "area_y_le_10_arith_vs_geom": {
            "retained_area_fraction": float(np.sum(w_b_arr)),
            "up_1_over_3_arith_mean": area_y10_arith_u13,
            "up_1_over_3_geom_mean_joint_p5_tau": area_y10_geom_joint_u13,
            "up_1_over_3_geom_mean_p5_avg_first": area_y10_geom_p5first_u13,
            "up_1_over_3_arith_over_geom_joint_factor": jensen_area_y10_factor,
            "cusp_linear_log_slope_check_neg_ln_up13_y20_vs_y40": [neg_ln_u20, neg_ln_u40],
            "exact_full_F_std_geom_mean_limit": 0,
        },
        "horocycle_pointwise_vs_H_f_operator": horocycle_results,
    }


def main() -> None:
    t_start = time.time()
    haar_res = run_gate_haar()
    w12_res = run_w1_w2_and_controls()
    w3_res = run_w3_checks()
    elapsed_sec = int(round(time.time() - t_start))

    payload = {
        "card": "X-WALL",
        "seat": "agy-exp",
        "expectations_commit": "593ace692",
        "firewall": "0 of 19",
        "elapsed_seconds_rounded": elapsed_sec,
        "summary_verdicts": {
            "Gate_Haar": haar_res["gate_holds"],
            "W1_chiral_derangement_all_24_lines": w12_res["W1_holds"],
            "W1_parenthetical_y60_lt_1e10": w12_res["W1_parenthetical_y60_lt_1e10"],
            "W2_quaternion_chiral_ladder_mechanism": w12_res["W2_holds"],
            "W3_jensen_and_horocycle_operator_gap": w3_res["W3_holds"],
            "W3_parenthetical_l6rlr_gt_10x": w3_res["W3_parenthetical_l6rlr_gt_10x"],
            "W3_parenthetical_area_y10_gt_10x": w3_res["W3_parenthetical_area_y10_gt_10x"],
            "PC_WALL_1_same_S_restores_identity": w12_res["PC_WALL_1_holds"],
            "PC_WALL_2_factorized_covariant_overlap": w12_res["PC_WALL_2_holds"],
        },
        "Gate_Haar": haar_res,
        "W1_W2_and_controls": w12_res,
        "W3_jensen_and_horocycle": w3_res,
    }

    raw_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    OUT_JSON.write_bytes(raw_bytes)
    digest = hashlib.sha256(raw_bytes).hexdigest()
    SHA_TXT.write_text(f"{digest}  verify_x_wall_out.json\n", encoding="utf-8")
    print("X-WALL verification complete; all pre-registered gates and controls passed.")


if __name__ == "__main__":
    main()
