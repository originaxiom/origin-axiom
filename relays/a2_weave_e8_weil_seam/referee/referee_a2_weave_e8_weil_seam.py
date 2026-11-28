#!/usr/bin/env python3
"""
Disjoint Cold-Room Zero-Trust Referee (Guardrail 6) for Card A2-WEAVE-E8-WEIL-SEAM.

100% independent implementation from first principles using DIFFERENT mathematical
representations and algorithms (ZERO imports, calls, or code shared with producer):
  - S1: Completed-square 1D Jacobi theta (mp.jtheta) cross-checked against 2D box
        sums at dps=55; SVD via mp.svd_c cross-checked against 6x6 real-split
        Hermitian mp.eigsy; unitary flux via mp.expm; 10 NEW Householder-QR Haar
        and Cayley-transform U(3)_L x U(5)_Re x U(5)_Ro basis scramblings.
  - S2: F_25 constructed via DIFFERENT irreducible polynomial F_5[t]/(t^2 - 3)
        with verified ring isomorphism Phi(a + b t) = a + (2b mod 5) d to
        F_5[d]/(d^2 - 2); explicit 15,600-element SL(2, F_25) enumeration,
        commutator BFS, order-240 index-2 normal SL(2, F_5) proof, and m004
        geometric fiber point from the figure-eight knot Wirtinger presentation.
  - S3: Q_3 via 3x3 permutation x Z_3, 2T via Hurwitz unit quaternions, BD_5 via
        2x2 matrices over F_11; direct symbolic 8-conjugate product expansion for
        the B704 degree-8 polynomial (not minimal_polynomial).
  - Controls & Hygiene: 5 independent Referee Planted Fault controls (RPF1..RPF5),
        producer control execution, SHA-256 verification, 0 AST floats, 0 JSON floats.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import os
import random
import subprocess
import sys
from collections import Counter
from pathlib import Path

import mpmath as mp
import sympy as sp

# Working precision: 55 decimal digits (zero AST float literals anywhere!)
DPS = 55
mp.mp.dps = DPS

TOL_ZERO_J = mp.mpf(1) / (mp.mpf(10) ** 40)
TOL_HAAR = mp.mpf(1) / (mp.mpf(10) ** 35)
TOL_EXACT = mp.mpf(1) / (mp.mpf(10) ** 45)
TOL_THETA_1D_2D = mp.mpf(1) / (mp.mpf(10) ** 50)
TOL_PROD_J = mp.mpf(1) / (mp.mpf(10) ** 10)
TOL_PROD_V = mp.mpf(1) / (mp.mpf(10) ** 9)
TOL_PROD_SV = mp.mpf(1) / (mp.mpf(10) ** 10)


def mstr(val, n=16):
    return mp.nstr(val, n)


def mat_max_abs(A):
    m = mp.mpf(0)
    for i in range(A.rows):
        for j in range(A.cols):
            v = abs(A[i, j])
            if v > m:
                m = v
    return m


def mat_frob_norm(A):
    s = mp.mpf(0)
    for i in range(A.rows):
        for j in range(A.cols):
            s += abs(A[i, j]) ** 2
    return mp.sqrt(s)


# =============================================================================
# S1: Independent Discriminant-15 Weil Lattices (L_15, L'_15) x B2008 Flux
# =============================================================================

def jtheta_shifted(tau_eff, delta, deriv=0):
    """Evaluate sum_{k in Z} (k + delta)^deriv * exp(2*pi*i * tau_eff * (k + delta)^2)
    via 1D Jacobi theta_3 at elevated internal precision (workdps=110) to avoid any
    branch cut or cancellation loss.
    """
    with mp.workdps(110):
        d = delta - mp.nint(delta)
        q = mp.exp(2j * mp.pi * tau_eff)
        z = 2 * mp.pi * tau_eff * d
        pref = mp.exp(2j * mp.pi * tau_eff * d * d)
        th0 = mp.jtheta(3, z, q, derivative=0)
        if deriv == 0:
            res = pref * th0
        else:
            th1 = mp.jtheta(3, z, q, derivative=1)
            res = pref * (d * th0 + th1 / (2j))
    return +res


def eval_theta_L15_1d(tau):
    """L_15: Q(x, y) = x^2 + x*y + 4*y^2 = (x + y/2)^2 + (15/4)*y^2.
    Dual generator g = (-1/15, 2/15) satisfies g_x + g_y/2 = 0 identically.
    CRT cosets: gamma_{a, b} = (5*a + 3*b) * g, a in Z/3, b in Z/5.
    Odd harmonic polynomial z(x, y) = (x + y/2) + i*(sqrt(15)/2)*y.
    """
    th_r = [jtheta_shifted(tau, mp.mpf(0), 0), jtheta_shifted(tau, mp.mpf(1) / 2, 0)]
    c_odd = 1j * mp.sqrt(15) / 2
    Me = mp.matrix(3, 5)
    Mo = mp.matrix(3, 5)
    for a in range(3):
        for b in range(5):
            gy = mp.mpf(2 * (5 * a + 3 * b)) / mp.mpf(15)
            # Reduce gy ONLY by even integers so gx + gy/2 remains an integer
            gy = gy - 2 * mp.nint(gy / 2)
            se = mp.mpc(0)
            so = mp.mpc(0)
            for r in (0, 1):
                delta = (mp.mpf(r) + gy) / 2
                f0 = jtheta_shifted(15 * tau, delta, deriv=0)
                f1 = 2 * jtheta_shifted(15 * tau, delta, deriv=1)
                se += th_r[r] * f0
                so += th_r[r] * (c_odd * f1)
            Me[a, b] = se
            Mo[a, b] = so
    return Me, Mo


def eval_theta_L15p_1d(tau):
    """L'_15: Q'(x, y) = 2*x^2 + x*y + 2*y^2 = (5/4)*(x + y)^2 + (3/4)*(x - y)^2.
    Dual generator g' = (4/15, -1/15), CRT cosets gamma'_{a, b} = (5*a + 3*b) * g'.
    Odd harmonic polynomial z'(x, y) = (sqrt(5)/2)*(x + y) + i*(sqrt(3)/2)*(x - y).
    """
    s5 = mp.sqrt(5)
    is3 = 1j * mp.sqrt(3)
    Me = mp.matrix(3, 5)
    Mo = mp.matrix(3, 5)
    for a in range(3):
        for b in range(5):
            k = 5 * a + 3 * b
            gx = mp.mpf(4 * k) / mp.mpf(15)
            gy = mp.mpf(-k) / mp.mpf(15)
            u0 = int(mp.nint(gx))
            v0 = int(mp.nint(gy))
            gx -= mp.mpf(u0)
            gy -= mp.mpf(v0)
            se = mp.mpc(0)
            so = mp.mpc(0)
            for r in (0, 1):
                ds = (mp.mpf(r) + gx + gy) / 2
                dd = (mp.mpf(r) + gx - gy) / 2
                fs0 = jtheta_shifted(5 * tau, ds, deriv=0)
                fd0 = jtheta_shifted(3 * tau, dd, deriv=0)
                fs1 = jtheta_shifted(5 * tau, ds, deriv=1)
                fd1 = jtheta_shifted(3 * tau, dd, deriv=1)
                se += fs0 * fd0
                so += s5 * fs1 * fd0 + is3 * fs0 * fd1
            Me[a, b] = se
            Mo[a, b] = so
    return Me, Mo


def eval_theta_2d_box(Qfunc, zfunc, gen_col, tau, box_n=20):
    """Independent 2D lattice sum verification using mp.exp(2j*pi*tau*Q)."""
    Me = mp.matrix(3, 5)
    Mo = mp.matrix(3, 5)
    for a in range(3):
        for b in range(5):
            k = 5 * a + 3 * b
            gx = mp.mpf(k) * gen_col[0]
            gy = mp.mpf(k) * gen_col[1]
            gx -= mp.nint(gx)
            gy -= mp.nint(gy)
            se = mp.mpc(0)
            so = mp.mpc(0)
            for u in range(-box_n, box_n + 1):
                x = mp.mpf(u) + gx
                for v in range(-box_n, box_n + 1):
                    y = mp.mpf(v) + gy
                    term = mp.exp(2j * mp.pi * tau * Qfunc(x, y))
                    se += term
                    so += zfunc(x, y) * term
            Me[a, b] = se
            Mo[a, b] = so
    return Me, Mo


def svd_via_svd_c(M):
    """Left singular unitary U (3x3) and descending singular values S via mp.svd_c."""
    U, S, _ = mp.svd_c(M)
    # Guarantee descending order
    idx = sorted(range(len(S)), key=lambda i: S[i], reverse=True)
    U_ord = mp.matrix(U.rows, U.cols)
    S_ord = [S[i] for i in idx]
    for new_j, old_j in enumerate(idx):
        for i in range(U.rows):
            U_ord[i, new_j] = U[i, old_j]
    return U_ord, S_ord


def svd_via_real6_eigsy(M):
    """Second completely independent SVD via 6x6 real-split symmetric eigendecomposition
    of H = M * M^H using mp.eigsy (distinct from both mp.svd_c and 8x8 Jordan-Wielandt).
    """
    H = M * M.H
    # Real symmetric 6x6 block matrix: [[Re(H), -Im(H)], [Im(H), Re(H)]]
    R = mp.matrix(6, 6)
    for i in range(3):
        for j in range(3):
            re = mp.re(H[i, j])
            im = mp.im(H[i, j])
            R[i, j] = re
            R[i, j + 3] = -im
            R[i + 3, j] = im
            R[i + 3, j + 3] = re
    evals, evecs = mp.eigsy(R)
    # Eigenvalues come in degenerate pairs (lambda, lambda); pick descending unique 3
    order = sorted(range(6), key=lambda k: evals[k], reverse=True)
    cols = []
    sigs = []
    for k in order:
        v = mp.matrix(3, 1)
        for i in range(3):
            v[i, 0] = mp.mpc(evecs[i, k], evecs[i + 3, k])
        # Gram-Schmidt against already accepted complex eigenvectors
        for u in cols:
            proj = (u.H * v)[0, 0]
            v = v - proj * u
        nrm = mp.sqrt(sum(abs(v[i, 0]) ** 2 for i in range(3)))
        if nrm > mp.mpf(1) / mp.mpf(100):
            v = v / nrm
            cols.append(v)
            ev = evals[k]
            sigs.append(mp.sqrt(ev) if ev > 0 else mp.mpf(0))
            if len(cols) == 3:
                break
    U = mp.matrix(3, 3)
    for j in range(3):
        for i in range(3):
            U[i, j] = cols[j][i, 0]
    return U, sigs


def extract_observables(Me, Mo, svd_fn=svd_via_svd_c):
    Ue, Se = svd_fn(Me)
    Uo, So = svd_fn(Mo)
    V = Ue.H * Uo
    J = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1] * V[1, 0]))
    sv_e = [s / Se[0] for s in Se]
    sv_o = [s / So[0] for s in So]
    abs_V = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    return {
        "Ue": Ue,
        "Uo": Uo,
        "V": V,
        "J": J,
        "abs_J": abs(J),
        "sv_e": sv_e,
        "sv_o": sv_o,
        "abs_V": abs_V,
    }


def obs_to_json(obs):
    return {
        "J": mstr(obs["J"], 16),
        "abs_J": mstr(obs["abs_J"], 16),
        "J_nonzero": bool(obs["abs_J"] > TOL_ZERO_J),
        "abs_V": [[mstr(obs["abs_V"][i][j], 12) for j in range(3)] for i in range(3)],
        "sv_e_ratios": [mstr(x, 14) if x > TOL_EXACT else "0" for x in obs["sv_e"]],
        "sv_o_ratios": [mstr(x, 14) if x > TOL_EXACT else "0" for x in obs["sv_o"]],
    }


def max_abs_V_diff(obs1, obs2):
    return max(
        abs(obs1["abs_V"][i][j] - obs2["abs_V"][i][j])
        for i in range(3)
        for j in range(3)
    )


def build_sl2_f3_weil_ops(eps_q):
    """Metaplectic Weil representation operators on H_{3, eps_q} (eps_q in {1, 2}):
    q_3(a) = eps_q * a^2 / 3 mod 1, B_3(a, a') = 2 * eps_q * a * a' / 3 mod 1.
    Returns P_flip, L_3 (T-matrix), S_3 (Fourier), C_3 (= S_3 L_3), W_6, W_ch.
    """
    P_flip = mp.matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    L_3 = mp.matrix(3, 3)
    for a in range(3):
        L_3[a, a] = mp.exp(2j * mp.pi * mp.mpf(eps_q * a * a) / 3)
    # Weil phase for S_3: (1 / sqrt(3)) * sum_a exp(2*pi*i * eps_q * a^2 / 3)
    gauss = sum(mp.exp(2j * mp.pi * mp.mpf(eps_q * a * a) / 3) for a in range(3))
    sigma = mp.conj(gauss) / mp.sqrt(3)
    S_3 = mp.matrix(3, 3)
    for a in range(3):
        for ap in range(3):
            S_3[a, ap] = (sigma / mp.sqrt(3)) * mp.exp(
                -2j * mp.pi * mp.mpf(2 * eps_q * a * ap) / 3
            )
    C_3 = S_3 * L_3
    # W_6: order-6 unitary element in <S_3, L_3> (specifically C_3 or S_3^2 * C_3)
    W_6 = C_3
    W_ch = -1j * (W_6 - W_6.H)
    return {
        "P_flip": P_flip,
        "L_3": L_3,
        "S_3": S_3,
        "C_3": C_3,
        "W_6": W_6,
        "W_ch": W_ch,
    }


def rand_unit_mpf(rng):
    """Exact rational uniform in (0, 1) with zero AST floats."""
    denom = 10 ** 15
    return mp.mpf(rng.randrange(1, denom)) / mp.mpf(denom)


def rand_complex_gaussian(rng):
    u1 = rand_unit_mpf(rng)
    u2 = rand_unit_mpf(rng)
    r = mp.sqrt(-2 * mp.log(u1))
    ang = 2 * mp.pi * u2
    return mp.mpc(r * mp.cos(ang), r * mp.sin(ang))


def haar_unitary_householder(n, rng):
    """Exact Haar-random U(n) via Householder QR + Mezzadri diagonal phase fix."""
    Z = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Z[i, j] = rand_complex_gaussian(rng)
    # Householder QR factorization Z = Q * R
    R = Z.copy()
    Q = mp.eye(n)
    for k in range(n):
        x = mp.matrix(n - k, 1)
        for i in range(n - k):
            x[i, 0] = R[k + i, k]
        norm_x = mp.sqrt(sum(abs(x[i, 0]) ** 2 for i in range(n - k)))
        if norm_x == 0:
            continue
        x0 = x[0, 0]
        phase = x0 / abs(x0) if abs(x0) > 0 else mp.mpc(1)
        v = x.copy()
        v[0, 0] = v[0, 0] + phase * norm_x
        vnorm2 = sum(abs(v[i, 0]) ** 2 for i in range(n - k))
        if vnorm2 == 0:
            continue
        # H_sub = I - 2 * v v^H / vnorm2
        # Apply H_sub to R[k:, k:] on left and Q[:, k:] on right
        for j in range(k, n):
            dot = sum(mp.conj(v[i, 0]) * R[k + i, j] for i in range(n - k))
            fac = 2 * dot / vnorm2
            for i in range(n - k):
                R[k + i, j] -= fac * v[i, 0]
        for i in range(n):
            dot = sum(Q[i, k + j] * v[j, 0] for j in range(n - k))
            fac = 2 * dot / vnorm2
            for j in range(n - k):
                Q[i, k + j] -= fac * mp.conj(v[j, 0])
    # Mezzadri fix: multiply column j of Q by R[j,j]/|R[j,j]| so diag(R) > 0
    for j in range(n):
        rjj = R[j, j]
        ph = rjj / abs(rjj) if abs(rjj) > 0 else mp.mpc(1)
        for i in range(n):
            Q[i, j] *= ph
    return Q


def cayley_unitary(n, rng):
    """Independent unitary U = (I - i H)(I + i H)^{-1} from random Hermitian H."""
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = rand_complex_gaussian(rng)
    H = (A + A.H) / 2
    I_n = mp.eye(n)
    return (I_n - 1j * H) * ((I_n + 1j * H) ** -1)


def run_S1():
    tau0 = mp.mpc(mp.mpf(23) / 100, mp.mpf(137) / 100)
    tstar = mp.mpc(0, mp.mpf("2267789662") / (mp.mpf(10) ** 9))

    # 1. Compute theta matrices via 1D jtheta AND cross-check against 2D box sum
    Me_15, Mo_15 = eval_theta_L15_1d(tau0)
    Me_15p, Mo_15p = eval_theta_L15p_1d(tau0)

    Me_15_2d, Mo_15_2d = eval_theta_2d_box(
        lambda x, y: x * x + x * y + 4 * y * y,
        lambda x, y: (x + y / 2) + 1j * mp.sqrt(15) / 2 * y,
        (-mp.mpf(1) / 15, mp.mpf(2) / 15),
        tau0,
        box_n=20,
    )
    Me_15p_2d, Mo_15p_2d = eval_theta_2d_box(
        lambda x, y: 2 * x * x + x * y + 2 * y * y,
        lambda x, y: mp.sqrt(5) / 2 * (x + y) + 1j * mp.sqrt(3) / 2 * (x - y),
        (mp.mpf(4) / 15, -mp.mpf(1) / 15),
        tau0,
        box_n=20,
    )
    diff_1d_2d = {
        "L15_even": mstr(mat_max_abs(Me_15 - Me_15_2d), 8),
        "L15_odd": mstr(mat_max_abs(Mo_15 - Mo_15_2d), 8),
        "L15p_even": mstr(mat_max_abs(Me_15p - Me_15p_2d), 8),
        "L15p_odd": mstr(mat_max_abs(Mo_15p - Mo_15p_2d), 8),
    }
    max_1d_2d = max(
        mat_max_abs(Me_15 - Me_15_2d),
        mat_max_abs(Mo_15 - Mo_15_2d),
        mat_max_abs(Me_15p - Me_15p_2d),
        mat_max_abs(Mo_15p - Mo_15p_2d),
    )

    # 2. Operators on H_3
    P_flip = mp.matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    T3 = mp.matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    T3inv = mp.matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    S_heis = T3 + T3inv
    H_ch = -1j * (T3 - T3inv)
    alpha = mp.pi / 9
    # Unitary flux via mp.expm (NOT spectral formula!)
    Up = mp.expm(1j * alpha * H_ch)
    Um = mp.expm(-1j * alpha * H_ch)
    unitary_err = max(
        mat_max_abs(Up.H * Up - mp.eye(3)),
        mat_max_abs(Um.H * Um - mp.eye(3)),
    )
    H_heis = mp.exp(1j * alpha) * T3 + mp.exp(-1j * alpha) * T3inv
    A_pos = 3 * mp.eye(3) + H_heis

    # Verify commutators / anticommutators
    err_heis_sym_comm = mat_max_abs(P_flip * S_heis - S_heis * P_flip)
    err_heis_ch_anticomm = mat_max_abs(P_flip * H_ch + H_ch * P_flip)

    # Verify H_Heis(pi/9) spectrum against 2*cos(pi/9 + 2*pi*q/3)
    evals_h, _ = mp.eigh(H_heis)
    evals_h_sorted = sorted([mp.re(e) for e in evals_h])
    expected_spec = sorted(
        [2 * mp.cos(alpha + 2 * mp.pi * mp.mpf(q) / 3) for q in range(3)]
    )
    heis_spec_err = max(
        abs(evals_h_sorted[i] - expected_spec[i]) for i in range(3)
    )

    # Verify SL(2, F_3) metaplectic operators on BOTH eps_q=2 (L_15) and eps_q=1 (L'_15)
    err_pflip_sl2f3_comm = mp.mpf(0)
    sl2f3_max_J = mp.mpf(0)
    for eps_q, Me, Mo in ((2, Me_15, Mo_15), (1, Me_15p, Mo_15p)):
        ops = build_sl2_f3_weil_ops(eps_q)
        for name in ("L_3", "S_3", "C_3", "W_6", "W_ch"):
            op = ops[name]
            c_err = mat_max_abs(P_flip * op - op * P_flip)
            if c_err > err_pflip_sl2f3_comm:
                err_pflip_sl2f3_comm = c_err
            # Test parity-split or single-side action of each metaplectic operator
            o1 = extract_observables(op * Me, Mo)
            if o1["abs_J"] > sl2f3_max_J:
                sl2f3_max_J = o1["abs_J"]
        # Test unitary exp(+-i alpha W_ch) and Hermitian (3I + W_ch)
        Uw_p = mp.expm(1j * alpha * ops["W_ch"])
        Uw_m = mp.expm(-1j * alpha * ops["W_ch"])
        Aw_h = 3 * mp.eye(3) + ops["W_ch"]
        for test_Me, test_Mo in (
            (Uw_p * Me, Uw_m * Mo),
            (Aw_h * Me, Aw_h * Mo),
            ((3 * mp.eye(3) + ops["W_6"] + ops["W_6"].H) * Me, (3 * mp.eye(3) + ops["W_6"] + ops["W_6"].H) * Mo),
        ):
            o_t = extract_observables(test_Me, test_Mo)
            if o_t["abs_J"] > sl2f3_max_J:
                sl2f3_max_J = o_t["abs_J"]

    # Mirror-symmetric theta=0 check
    sym_theta0_max_J = mp.mpf(0)
    for c_shift in (0, 2, 3):
        Op_s = mp.mpf(c_shift) * mp.eye(3) + S_heis
        for Me, Mo in ((Me_15, Mo_15), (Me_15p, Mo_15p)):
            osym = extract_observables(Op_s * Me, Op_s * Mo)
            if osym["abs_J"] > sym_theta0_max_J:
                sym_theta0_max_J = osym["abs_J"]

    # 3. Core observables on L_15, L'_15, and cross-genus (plus svd_c vs real6_eigsy cross-check!)
    sectors = {
        "L_15": (Me_15, Mo_15, eval_theta_L15_1d),
        "L_15_prime": (Me_15p, Mo_15p, eval_theta_L15p_1d),
    }
    per_genus = {}
    svd_cross_check_max_err = mp.mpf(0)

    for gname, (Me, Mo, eval_fn) in sectors.items():
        o_bare = extract_observables(Me, Mo)
        o_uni = extract_observables(Up * Me, Um * Mo)
        o_herm = extract_observables(A_pos * Me, A_pos * Mo)
        o_sym = extract_observables((3 * mp.eye(3) + S_heis) * Me, (3 * mp.eye(3) + S_heis) * Mo)
        ops_g = build_sl2_f3_weil_ops(2 if gname == "L_15" else 1)
        o_sl2 = extract_observables((3 * mp.eye(3) + ops_g["W_ch"]) * Me, (3 * mp.eye(3) + ops_g["W_ch"]) * Mo)

        # Cross-check svd_c against 6x6 real-split mp.eigsy on chiral-unlocked unitary & Hermitian!
        for tMe, tMo, ref_o in ((Up * Me, Um * Mo, o_uni), (A_pos * Me, A_pos * Mo, o_herm)):
            alt_o = extract_observables(tMe, tMo, svd_fn=svd_via_real6_eigsy)
            err_j = abs(alt_o["abs_J"] - ref_o["abs_J"])
            err_v = max_abs_V_diff(alt_o, ref_o)
            svd_cross_check_max_err = max(svd_cross_check_max_err, err_j, err_v)

        # Covariance under T, T^3, S
        Me_T, Mo_T = eval_fn(tau0 + 1)
        Me_T3, Mo_T3 = eval_fn(tau0 + 3)
        Me_S, Mo_S = eval_fn(-1 / tau0)

        o_uni_T = extract_observables(Up * Me_T, Um * Mo_T)
        o_uni_T3 = extract_observables(Up * Me_T3, Um * Mo_T3)
        o_uni_S = extract_observables(Up * Me_S, Um * Mo_S)

        o_herm_T = extract_observables(A_pos * Me_T, A_pos * Mo_T)
        o_herm_T3 = extract_observables(A_pos * Me_T3, A_pos * Mo_T3)
        o_herm_S = extract_observables(A_pos * Me_S, A_pos * Mo_S)

        per_genus[gname] = {
            "bare": obs_to_json(o_bare),
            "heisenberg_parity_split_unitary_flux": obs_to_json(o_uni),
            "heisenberg_same_hermitian_flux": obs_to_json(o_herm),
            "heisenberg_theta0_symmetric": obs_to_json(o_sym),
            "metaplectic_SL2_F3_coupled": obs_to_json(o_sl2),
            "cov_parity_unitary": {
                "dJ_S": mstr(abs(o_uni_S["abs_J"] - o_uni["abs_J"]), 14),
                "dJ_T": mstr(abs(o_uni_T["abs_J"] - o_uni["abs_J"]), 14),
                "dJ_T3": mstr(abs(o_uni_T3["abs_J"] - o_uni["abs_J"]), 14),
                "dV_S": mstr(max_abs_V_diff(o_uni_S, o_uni), 14),
                "dV_T": mstr(max_abs_V_diff(o_uni_T, o_uni), 14),
                "dV_T3": mstr(max_abs_V_diff(o_uni_T3, o_uni), 14),
            },
            "cov_same_hermitian": {
                "dJ_S": mstr(abs(o_herm_S["abs_J"] - o_herm["abs_J"]), 14),
                "dJ_T": mstr(abs(o_herm_T["abs_J"] - o_herm["abs_J"]), 14),
                "dJ_T3": mstr(abs(o_herm_T3["abs_J"] - o_herm["abs_J"]), 14),
            },
        }

    # Cross-genus L_15 even x L'_15 odd
    cg_bare = extract_observables(Me_15, Mo_15p)
    cg_uni = extract_observables(Up * Me_15, Um * Mo_15p)
    cg_herm = extract_observables(A_pos * Me_15, A_pos * Mo_15p)
    cross_genus = {
        "bare": obs_to_json(cg_bare),
        "parity_split_unitary": obs_to_json(cg_uni),
        "same_hermitian": obs_to_json(cg_herm),
    }

    # Angle sweep on L_15 + oddness in alpha
    sweep = []
    for num, den in ((0, 1), (1, 18), (1, 9), (1, 6), (2, 9), (1, 3)):
        ang = mp.pi * mp.mpf(num) / mp.mpf(den)
        U1 = mp.expm(1j * ang * H_ch)
        U2 = mp.expm(-1j * ang * H_ch)
        sw = extract_observables(U1 * Me_15, U2 * Mo_15)
        sweep.append({"alpha_over_pi": f"{num}/{den}", "abs_J": mstr(sw["abs_J"], 14)})

    o_pos_a = extract_observables(Up * Me_15, Um * Mo_15)
    o_neg_a = extract_observables(Um * Me_15, Up * Mo_15)
    odd_alpha_absJ_err = abs(o_pos_a["abs_J"] - o_neg_a["abs_J"])

    # Also evaluate L_15 at tau* = 2.267789662 i (purely imaginary stationary point)
    Me_st, Mo_st = eval_theta_L15_1d(tstar)
    tstar_bare = extract_observables(Me_st, Mo_st)
    tstar_uni = extract_observables(Up * Me_st, Um * Mo_st)
    tstar_herm = extract_observables(A_pos * Me_st, A_pos * Mo_st)

    # 4. Guardrail 3: 10 NEW independent Haar (5 Householder-QR) + Cayley (5) scramblings
    rng = random.Random(2026112802)
    haar_max_err = mp.mpf(0)
    haar_unitarity_max_err = mp.mpf(0)
    targets_for_haar = [
        (Up * Me_15, Um * Mo_15, extract_observables(Up * Me_15, Um * Mo_15)),
        (A_pos * Me_15, A_pos * Mo_15, extract_observables(A_pos * Me_15, A_pos * Mo_15)),
        (Up * Me_15p, Um * Mo_15p, extract_observables(Up * Me_15p, Um * Mo_15p)),
        (Up * Me_15, Um * Mo_15p, cg_uni),
    ]
    for trial in range(10):
        gen_fn = haar_unitary_householder if trial < 5 else cayley_unitary
        UL = gen_fn(3, rng)
        URe = gen_fn(5, rng)
        URo = gen_fn(5, rng)
        haar_unitarity_max_err = max(
            haar_unitarity_max_err,
            mat_max_abs(UL.H * UL - mp.eye(3)),
            mat_max_abs(URe.H * URe - mp.eye(5)),
            mat_max_abs(URo.H * URo - mp.eye(5)),
        )
        for Me_t, Mo_t, ref_o in targets_for_haar:
            sc_o = extract_observables(UL * Me_t * URe.H, UL * Mo_t * URo.H)
            eJ = abs(sc_o["abs_J"] - ref_o["abs_J"])
            eV = max_abs_V_diff(sc_o, ref_o)
            eSe = max(abs(sc_o["sv_e"][k] - ref_o["sv_e"][k]) for k in range(3))
            eSo = max(abs(sc_o["sv_o"][k] - ref_o["sv_o"][k]) for k in range(3))
            haar_max_err = max(haar_max_err, eJ, eV, eSe, eSo)

    s1_ok = bool(
        max_1d_2d < TOL_THETA_1D_2D
        and svd_cross_check_max_err < TOL_EXACT
        and err_pflip_sl2f3_comm < TOL_EXACT
        and err_heis_sym_comm < TOL_EXACT
        and err_heis_ch_anticomm < TOL_EXACT
        and heis_spec_err < TOL_EXACT
        and unitary_err < TOL_EXACT
        and odd_alpha_absJ_err < TOL_EXACT
        and sl2f3_max_J < TOL_ZERO_J
        and sym_theta0_max_J < TOL_ZERO_J
        and haar_max_err < TOL_HAAR
        and haar_unitarity_max_err < TOL_EXACT
        and per_genus["L_15"]["heisenberg_parity_split_unitary_flux"]["J_nonzero"]
        and per_genus["L_15"]["heisenberg_same_hermitian_flux"]["J_nonzero"]
        and per_genus["L_15_prime"]["heisenberg_parity_split_unitary_flux"]["J_nonzero"]
        and per_genus["L_15_prime"]["heisenberg_same_hermitian_flux"]["J_nonzero"]
        and cross_genus["parity_split_unitary"]["J_nonzero"]
        and cross_genus["same_hermitian"]["J_nonzero"]
    )

    return {
        "ok": s1_ok,
        "theta_1d_vs_2d_max_diff": diff_1d_2d,
        "svd_c_vs_real6_eigsy_max_err": mstr(svd_cross_check_max_err, 10),
        "err_pflip_sl2f3_comm": mstr(err_pflip_sl2f3_comm, 10),
        "err_heis_sym_comm": mstr(err_heis_sym_comm, 10),
        "err_heis_ch_anticomm": mstr(err_heis_ch_anticomm, 10),
        "heis_spec_err": mstr(heis_spec_err, 10),
        "unitary_err": mstr(unitary_err, 10),
        "odd_alpha_absJ_err": mstr(odd_alpha_absJ_err, 10),
        "sl2f3_max_J": mstr(sl2f3_max_J, 10),
        "sym_theta0_max_J": mstr(sym_theta0_max_J, 10),
        "haar_10trial_max_err": mstr(haar_max_err, 10),
        "haar_unitarity_max_err": mstr(haar_unitarity_max_err, 10),
        "per_genus": per_genus,
        "cross_genus_L15even_L15podd": cross_genus,
        "L15_parity_unitary_angle_sweep": sweep,
        "L15_at_tau_star_imaginary": {
            "bare_abs_J": mstr(tstar_bare["abs_J"], 10),
            "unitary_abs_J": mstr(tstar_uni["abs_J"], 10),
            "hermitian_abs_J": mstr(tstar_herm["abs_J"], 10),
        },
        "_cache": {
            "Me_15": Me_15,
            "Mo_15": Mo_15,
            "S_heis": S_heis,
            "H_ch": H_ch,
            "Up": Up,
        },
    }


# =============================================================================
# S2: Independent F_25 = F_5[t]/(t^2 - 3), G_E8 (156,000), & 15,625 Markoff
# =============================================================================

class F25Sqrt3:
    """Explicit finite field F_25 = F_5[t]/(t^2 - 3) with precomputed tables
    and verified ring isomorphism Phi(a + b t) = a + (2b mod 5) d to F_5[d]/(d^2 - 2).
    """

    def __init__(self):
        self.elems = [(a, b) for a in range(5) for b in range(5)]
        self.to_idx = {e: i for i, e in enumerate(self.elems)}
        self.ZERO = self.to_idx[(0, 0)]
        self.ONE = self.to_idx[(1, 0)]
        self.TWO = self.to_idx[(2, 0)]
        self.NEG2 = self.to_idx[(3, 0)]
        self.NEG1 = self.to_idx[(4, 0)]

        self.add = [[0] * 25 for _ in range(25)]
        self.sub = [[0] * 25 for _ in range(25)]
        self.mul = [[0] * 25 for _ in range(25)]
        self.neg = [0] * 25
        self.inv = [None] * 25
        self.frob = [0] * 25
        self.in_F5 = [False] * 25

        for i, (a1, b1) in enumerate(self.elems):
            self.neg[i] = self.to_idx[((-a1) % 5, (-b1) % 5)]
            # (a + b t)^5 = a + b t^5 = a + b*(3^2)*t = a - b t
            self.frob[i] = self.to_idx[(a1, (-b1) % 5)]
            self.in_F5[i] = (b1 == 0)
            for j, (a2, b2) in enumerate(self.elems):
                self.add[i][j] = self.to_idx[((a1 + a2) % 5, (b1 + b2) % 5)]
                self.sub[i][j] = self.to_idx[((a1 - a2) % 5, (b1 - b2) % 5)]
                self.mul[i][j] = self.to_idx[
                    ((a1 * a2 + 3 * b1 * b2) % 5, (a1 * b2 + b1 * a2) % 5)
                ]
        for i in range(25):
            if i == self.ZERO:
                continue
            for j in range(25):
                if self.mul[i][j] == self.ONE:
                    self.inv[i] = j
                    break
            assert self.inv[i] is not None

        # Verify Phi(a + b t) = a + (2b mod 5) d is an exact ring isomorphism to F_5[d]/(d^2 - 2)
        self.iso_verified = self._verify_isomorphism_to_d2_eq_2()

    def phi_to_d(self, idx):
        a, b = self.elems[idx]
        return (a, (2 * b) % 5)

    def phi_label_d(self, idx):
        a, c = self.phi_to_d(idx)
        return f"{a}+{c}d"

    def _verify_isomorphism_to_d2_eq_2(self):
        def d_add(u, v):
            return ((u[0] + v[0]) % 5, (u[1] + v[1]) % 5)

        def d_mul(u, v):
            return ((u[0] * v[0] + 2 * u[1] * v[1]) % 5, (u[0] * v[1] + u[1] * v[0]) % 5)

        seen = set()
        for i in range(25):
            pi = self.phi_to_d(i)
            seen.add(pi)
            for j in range(25):
                pj = self.phi_to_d(j)
                if self.phi_to_d(self.add[i][j]) != d_add(pi, pj):
                    return False
                if self.phi_to_d(self.mul[i][j]) != d_mul(pi, pj):
                    return False
        return len(seen) == 25


def run_S2():
    F = F25Sqrt3()
    add, sub, mul, neg = F.add, F.sub, F.mul, F.neg
    Z, O, TWO, NEG2, NEG1 = F.ZERO, F.ONE, F.TWO, F.NEG2, F.NEG1

    def m_mul(A, B):
        return (
            add[mul[A[0]][B[0]]][mul[A[1]][B[2]]],
            add[mul[A[0]][B[1]]][mul[A[1]][B[3]]],
            add[mul[A[2]][B[0]]][mul[A[3]][B[2]]],
            add[mul[A[2]][B[1]]][mul[A[3]][B[3]]],
        )

    def m_inv(A):
        return (A[3], neg[A[1]], neg[A[2]], A[0])

    def m_tr(A):
        return add[A[0]][A[3]]

    def m_comm(A, B):
        return m_mul(m_mul(A, B), m_mul(m_inv(A), m_inv(B)))

    def gen_subgroup(gens):
        H = {I2}
        st = [I2]
        all_g = list(gens) + [m_inv(g) for g in gens]
        while st:
            cur = st.pop()
            for g in all_g:
                nx = m_mul(cur, g)
                if nx not in H:
                    H.add(nx)
                    st.append(nx)
        return H

    I2 = (O, Z, Z, O)
    NI2 = (NEG1, Z, Z, NEG1)

    # 1. Exact enumeration of SL(2, F_25) in F_5[t]/(t^2 - 3)
    sl2_all = []
    for a in range(25):
        for b in range(25):
            for c in range(25):
                bc1 = add[mul[b][c]][O]
                if a != Z:
                    d = mul[bc1][F.inv[a]]
                    sl2_all.append((a, b, c, d))
                else:
                    if bc1 == Z:
                        for d in range(25):
                            sl2_all.append((a, b, c, d))
    sl2_order = len(sl2_all)

    # Center of SL(2, F_25) by direct commutation check against generators
    t_idx = F.to_idx[(0, 1)]
    G_gens = [
        (O, O, Z, O),
        (O, t_idx, Z, O),
        (Z, NEG1, O, Z),
    ]
    center_sl2 = [
        M for M in sl2_all if all(m_mul(M, g) == m_mul(g, M) for g in G_gens)
    ]

    # Single commutator witness for -I_2 and perfectness [SL(2, F_25), SL(2, F_25)] = SL(2, F_25)
    # Build explicit commutator generators
    comm_gens = []
    minus_I_witness = None
    # Use a small deterministic pool to find a single commutator equal to -I_2
    pool = [
        (O, O, Z, O),
        (O, Z, O, O),
        (Z, NEG1, O, Z),
        (TWO, Z, Z, F.inv[TWO]),
        (t_idx, Z, Z, F.inv[t_idx]),
        (O, t_idx, Z, O),
        (O, Z, t_idx, O),
        (TWO, O, O, F.to_idx[(1, 0)]),
    ]
    # Filter to det == 1
    pool = [M for M in pool if sub[mul[M[0]][M[3]]][mul[M[1]][M[2]]] == O]
    # Also add an element of order 4: [[0, -1], [1, 0]] and [[2, 0], [0, 3]] -> check their commutator!
    # In SL(2, F_5), A=[[0,-1],[1,0]], B=[[2,1],[1,1]] -> det=1; search small pairs
    for i in range(len(pool)):
        for j in range(len(pool)):
            c = m_comm(pool[i], pool[j])
            comm_gens.append(c)
            if c == NI2 and minus_I_witness is None:
                minus_I_witness = (pool[i], pool[j])
    if minus_I_witness is None:
        # Exhaustive over small F_5 elements in SL(2, F_5)
        f5_mats = [M for M in sl2_all if all(F.in_F5[x] for x in M)]
        for A in f5_mats:
            for B in f5_mats:
                if m_comm(A, B) == NI2:
                    minus_I_witness = (A, B)
                    break
            if minus_I_witness is not None:
                break
    sl2_derived = gen_subgroup(comm_gens)
    sl2_is_perfect = len(sl2_derived) == sl2_order

    # 2. Construct BD_5 (order 20) over F_11 and compute G_E8 = SL(2, F_25) *_{Z/2} BD_5
    def m11_mul(A, B):
        return (
            (A[0] * B[0] + A[1] * B[2]) % 11,
            (A[0] * B[1] + A[1] * B[3]) % 11,
            (A[2] * B[0] + A[3] * B[2]) % 11,
            (A[2] * B[1] + A[3] * B[3]) % 11,
        )

    def m11_inv(A):
        return (A[3], (-A[1]) % 11, (-A[2]) % 11, A[0])

    I11 = (1, 0, 0, 1)
    NI11 = (10, 0, 0, 10)
    bd5_a = (2, 0, 0, 6)  # order 10, a^5 = -I
    bd5_b = (0, 10, 1, 0)  # order 4, b^2 = -I, b a b^-1 = a^-1
    bd5_set = {I11}
    st = [I11]
    while st:
        c = st.pop()
        for g in (bd5_a, bd5_b):
            nx = m11_mul(c, g)
            if nx not in bd5_set:
                bd5_set.add(nx)
                st.append(nx)
    bd5_list = list(bd5_set)
    bd5_order = len(bd5_list)
    bd5_center = [
        x for x in bd5_list if all(m11_mul(x, y) == m11_mul(y, x) for y in (bd5_a, bd5_b))
    ]
    bd5_comm_gens = [
        m11_mul(m11_mul(x, y), m11_mul(m11_inv(x), m11_inv(y)))
        for x in bd5_list
        for y in bd5_list
    ]
    bd5_derived = set(bd5_comm_gens)
    # Close under multiplication
    changed = True
    while changed:
        changed = False
        new_els = set()
        for x in bd5_derived:
            for y in bd5_derived:
                p = m11_mul(x, y)
                if p not in bd5_derived:
                    new_els.add(p)
        if new_els:
            bd5_derived |= new_els
            changed = True
    bd5_ab_order = bd5_order // len(bd5_derived)

    # Central amalgamation G_E8 = (SL(2, F_25) x BD_5) / <(-I_2, -I_11)>
    # Since -I_2 in [SL(2, F_25), SL(2, F_25)] = SL(2, F_25), the commutator subgroup
    # [G_E8, G_E8] is the image of SL(2, F_25) x <[BD_5, BD_5], -I_11> mod <(-I_2, -I_11)>.
    bd5_derived_with_neg = set(bd5_derived)
    for x in list(bd5_derived):
        bd5_derived_with_neg.add(m11_mul(x, NI11))
    assert len(center_sl2) == 2 and len(bd5_center) == 2
    ge8_order = (sl2_order * bd5_order) // 2
    ge8_center_order = (len(center_sl2) * len(bd5_center)) // 2
    ge8_comm_order = (sl2_order * len(bd5_derived_with_neg)) // 2
    ge8_ab_order = ge8_order // ge8_comm_order

    # 3. Full 15,625-point F_25 Markoff-Weave variety in F_5[t]/(t^2 - 3)
    def kappa_of(x, y, z):
        s = add[add[mul[x][x]][mul[y][y]]][mul[z][z]]
        s = sub[s][mul[mul[x][y]][z]]
        return sub[s][TWO]

    def L_move(pt):
        x, y, z = pt
        return (x, z, sub[mul[x][z]][y])

    def R_move(pt):
        x, y, z = pt
        return (z, y, sub[mul[y][z]][x])

    def P_move(pt):
        x, y, z = pt
        return (y, x, z)

    by_kappa = [[] for _ in range(25)]
    kappa_ok = True
    global_fixed = []
    for x in range(25):
        for y in range(25):
            for z in range(25):
                pt = (x, y, z)
                k = kappa_of(x, y, z)
                if (
                    kappa_of(*L_move(pt)) != k
                    or kappa_of(*R_move(pt)) != k
                    or kappa_of(*P_move(pt)) != k
                ):
                    kappa_ok = False
                if L_move(pt) == pt and R_move(pt) == pt:
                    global_fixed.append((k, pt))
                by_kappa[k].append(pt)

    leaves_summary_d = {}
    swap_any_change = False
    cusp_orbits_raw = None

    for k in range(25):
        pts = by_kappa[k]
        visited = set()
        orbits = []
        pt_to_orb = {}
        for p in pts:
            if p in visited:
                continue
            orb = []
            stack = [p]
            visited.add(p)
            while stack:
                cur = stack.pop()
                orb.append(cur)
                for nxt in (L_move(cur), R_move(cur)):
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)
            oid = len(orbits)
            orbits.append(orb)
            for q in orb:
                pt_to_orb[q] = oid

        # Check whether swap P merges any two <L, R> orbits
        swap_merges = False
        for p in pts:
            if pt_to_orb[P_move(p)] != pt_to_orb[p]:
                swap_merges = True
                swap_any_change = True

        # Also compute <L, R, P> orbits directly for independent check
        vis_p = set()
        orbs_p = []
        for p in pts:
            if p in vis_p:
                continue
            orb = []
            stack = [p]
            vis_p.add(p)
            while stack:
                cur = stack.pop()
                orb.append(cur)
                for nxt in (L_move(cur), R_move(cur), P_move(cur)):
                    if nxt not in vis_p:
                        vis_p.add(nxt)
                        stack.append(nxt)
            orbs_p.append(len(orb))

        sizes_lr = sorted([len(o) for o in orbits], reverse=True)
        sizes_lrp = sorted(orbs_p, reverse=True)
        lbl_d = F.phi_label_d(k)
        leaves_summary_d[lbl_d] = {
            "points": len(pts),
            "n_orbits_LR": len(orbits),
            "n_orbits_LRP": len(orbs_p),
            "orbit_sizes_LR": sizes_lr,
            "orbit_sizes_LRP": sizes_lrp,
            "swap_merges": swap_merges,
        }
        if k == NEG2:
            cusp_orbits_raw = sorted(orbits, key=lambda o: len(o), reverse=True)

    # 4. Cusp leaf kappa = -2 classification + m004 Wirtinger fiber + order-240 normal SL(2, F_5)
    # Derive m004 geometric fiber point from figure-eight knot Wirtinger presentation:
    # <x, y | (x Y X y) x = y (x Y X y)> with parabolic X=[[1,1],[0,1]], Y=[[1,0],[u,1]]
    m004_fiber_pts = set()
    X_w = (O, O, Z, O)
    Xi_w = m_inv(X_w)
    for u in range(25):
        if u == Z:
            continue
        Y_w = (O, Z, u, O)
        Yi_w = m_inv(Y_w)
        W_w = m_mul(m_mul(X_w, Yi_w), m_mul(Xi_w, Y_w))
        if m_mul(W_w, X_w) == m_mul(Y_w, W_w):
            b0 = m_mul(Xi_w, Y_w)
            b1 = m_mul(Y_w, Xi_w)
            c01 = m_comm(b0, b1)
            assert m_tr(c01) == NEG2
            pt_m = (m_tr(b0), m_tr(b1), m_tr(m_mul(b0, b1)))
            assert kappa_of(*pt_m) == NEG2
            m004_fiber_pts.add(pt_m)

    def find_AB_for_triple(x, y, z):
        A = (x, NEG1, O, Z)
        for a in range(25):
            d = sub[y][a]
            for b in range(25):
                c = sub[add[mul[x][a]][b]][z]
                if sub[mul[a][d]][mul[b][c]] == O:
                    B = (a, b, c, d)
                    if m_tr(m_comm(A, B)) == NEG2:
                        return A, B
        raise RuntimeError("No SL(2, F_25) lift found")

    def el_order(M):
        cur = M
        k = 1
        while cur != I2:
            cur = m_mul(cur, M)
            k += 1
        return k

    # Reference SL(2, F_5) inside SL(2, F_25)
    SL2_F5 = gen_subgroup([(O, O, Z, O), (Z, NEG1, O, Z)])
    assert len(SL2_F5) == 120
    ord_dist_SL2_F5 = Counter(el_order(M) for M in SL2_F5)

    cusp_pt_to_idx = {}
    for oid, orb in enumerate(cusp_orbits_raw):
        for p in orb:
            cusp_pt_to_idx[p] = oid

    cusp_orbit_records = []
    frob_fixed_cnt = 0
    order_240_has_normal_SL2_F5 = False

    for oid, orb in enumerate(cusp_orbits_raw):
        orb_set = set(orb)
        # Canonical minimal rep in F_5[t]
        rep = min(orb)
        A, B = find_AB_for_triple(*rep)
        H = gen_subgroup([A, B])
        h_ord = len(H)

        # Frobenius image of orbit
        frob_img = {(F.frob[p[0]], F.frob[p[1]], F.frob[p[2]]) for p in orb}
        frob_target = cusp_pt_to_idx[next(iter(frob_img))]
        frob_fixed = frob_img == orb_set
        if frob_fixed:
            frob_fixed_cnt += 1

        swap_fixed = all(P_move(p) in orb_set for p in orb)
        all_f5 = all(F.in_F5[p[0]] and F.in_F5[p[1]] and F.in_F5[p[2]] for p in orb)
        any_f5 = any(F.in_F5[p[0]] and F.in_F5[p[1]] and F.in_F5[p[2]] for p in orb)
        has_m004 = any(mp_pt in orb_set for mp_pt in m004_fiber_pts)

        # For order-240 subgroup, verify it contains an index-2 normal subgroup isomorphic to SL(2, F_5)
        if h_ord == 240:
            c_gens = [m_comm(g, h) for g in H for h in (A, B)]
            D = gen_subgroup(c_gens)
            is_normal = all(
                m_mul(m_mul(g, h), m_inv(g)) in D for g in (A, B) for h in D
            )
            ord_dist_D = Counter(el_order(M) for M in D)
            all_tr_f5 = all(F.in_F5[m_tr(M)] for M in D)
            # Also check D is perfect ([D, D] == D), uniquely identifying SL(2, F_5) of order 120!
            d_list = list(D)
            d_gens = [m_comm(d_list[0], x) for x in d_list] + [
                m_comm(d_list[1], x) for x in d_list
            ]
            D_der = gen_subgroup(d_gens)
            order_240_has_normal_SL2_F5 = bool(
                len(D) == 120
                and is_normal
                and ord_dist_D == ord_dist_SL2_F5
                and all_tr_f5
                and len(D_der) == 120
            )

        cusp_orbit_records.append(
            {
                "orbit_idx": oid,
                "size": len(orb),
                "subgroup_order": h_ord,
                "all_in_F5": all_f5,
                "any_in_F5": any_f5,
                "frob_fixed_setwise": frob_fixed,
                "frob_maps_to_orbit": frob_target,
                "swap_P_fixed_setwise": swap_fixed,
                "contains_m004_fiber": has_m004,
                "rep_in_F5t": [list(F.elems[c]) for c in rep],
                "rep_mapped_Phi_to_F5d": [list(F.phi_to_d(c)) for c in rep],
            }
        )

    global_fixed_d = sorted(
        [
            [list(F.phi_to_d(k)), [list(F.phi_to_d(c)) for c in pt]]
            for (k, pt) in global_fixed
        ]
    )

    s2_ok = bool(
        F.iso_verified
        and sl2_order == 15600
        and sl2_is_perfect
        and minus_I_witness is not None
        and ge8_order == 156000
        and ge8_center_order == 2
        and ge8_comm_order == 78000
        and ge8_ab_order == 2
        and kappa_ok
        and len(global_fixed) == 2
        and not swap_any_change
        and [r["size"] for r in cusp_orbit_records] == [600, 60, 40, 1]
        and [r["subgroup_order"] for r in cusp_orbit_records] == [15600, 240, 120, 8]
        and frob_fixed_cnt == 4
        and order_240_has_normal_SL2_F5
        and cusp_orbit_records[0]["contains_m004_fiber"]
        and all(not r["contains_m004_fiber"] for r in cusp_orbit_records[1:])
    )

    return {
        "ok": s2_ok,
        "field_model": "F_5[t]/(t^2 - 3)",
        "phi_isomorphism_to_F5d_verified": F.iso_verified,
        "G_E8_structure": {
            "SL2_F25_order": sl2_order,
            "SL2_F25_is_perfect": sl2_is_perfect,
            "minus_I_is_single_commutator": minus_I_witness is not None,
            "BD5_order": bd5_order,
            "BD5_ab_order": bd5_ab_order,
            "G_E8_order": ge8_order,
            "G_E8_center_order": ge8_center_order,
            "G_E8_comm_order": ge8_comm_order,
            "G_E8_ab_order": ge8_ab_order,
        },
        "F25_markoff_variety": {
            "total_points": sum(len(v) for v in by_kappa),
            "kappa_conserved_all_15625": kappa_ok,
            "global_fixed_points_count": len(global_fixed),
            "global_fixed_points": global_fixed_d,
            "swap_P_changes_any_orbit_across_25_leaves": swap_any_change,
            "leaves_summary": leaves_summary_d,
        },
        "cusp_leaf_kappa_minus2": {
            "total_points": sum(r["size"] for r in cusp_orbit_records),
            "n_orbits_LR": len(cusp_orbit_records),
            "frob_torsor": {
                "fixed_orbits": frob_fixed_cnt,
                "swapped_pairs": (4 - frob_fixed_cnt) // 2,
            },
            "order_240_contains_index2_normal_SL2_F5": order_240_has_normal_SL2_F5,
            "m004_wirtinger_fiber_pts_in_F5t": sorted(
                [[list(F.elems[c]) for c in pt] for pt in m004_fiber_pts]
            ),
            "orbits": cusp_orbit_records,
        },
        "_cache": {
            "F": F,
            "SL2_F5": SL2_F5,
            "m_mul": m_mul,
            "m_inv": m_inv,
            "I2": I2,
            "NI2": NI2,
            "bd5_order": bd5_order,
            "bd5_ab_order": bd5_ab_order,
            "sl2_order": sl2_order,
        },
    }


# =============================================================================
# S3: Independent Q_3, 2T, BD_5 Coupling & Direct-Expansion B704 Cube
# =============================================================================

def run_S3(s2_cache):
    # 1. Q_3 = S_3 x Z_3 (order 18) via 3x3 permutation x Z_3
    S3 = list(itertools.permutations((0, 1, 2)))
    Q3 = [(p, z) for p in S3 for z in range(3)]
    Q3_id = ((0, 1, 2), 0)

    def q3_mul(x, y):
        p1, z1 = x
        p2, z2 = y
        return (tuple(p1[p2[i]] for i in range(3)), (z1 + z2) % 3)

    # 2. 2T (order 24) via Hurwitz unit quaternions (scaled by 2 as integer 4-tuples)
    T2 = []
    for i in range(4):
        for s in (-2, 2):
            v = [0, 0, 0, 0]
            v[i] = s
            T2.append(tuple(v))
    for a in (-1, 1):
        for b in (-1, 1):
            for c in (-1, 1):
                for d in (-1, 1):
                    T2.append((a, b, c, d))
    T2_id = (2, 0, 0, 0)

    def t2_mul(q1, q2):
        a1, b1, c1, d1 = q1
        a2, b2, c2, d2 = q2
        return (
            (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2) // 2,
            (a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2) // 2,
            (a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2) // 2,
            (a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2) // 2,
        )

    # 3. BD_5 (order 20) via 2x2 matrices over F_11
    def bd5_mul(A, B):
        return (
            (A[0] * B[0] + A[1] * B[2]) % 11,
            (A[0] * B[1] + A[1] * B[3]) % 11,
            (A[2] * B[0] + A[3] * B[2]) % 11,
            (A[2] * B[1] + A[3] * B[3]) % 11,
        )

    BD5_id = (1, 0, 0, 1)
    bd5_set = {BD5_id}
    st = [BD5_id]
    while st:
        cur = st.pop()
        for g in ((2, 0, 0, 6), (0, 10, 1, 0)):
            nx = bd5_mul(cur, g)
            if nx not in bd5_set:
                bd5_set.add(nx)
                st.append(nx)
    BD5 = list(bd5_set)

    assert len(Q3) == 18 and len(T2) == 24 and len(BD5) == 20

    def g_ord(g, mul, gid):
        cur = g
        k = 1
        while cur != gid:
            cur = mul(cur, g)
            k += 1
        return k

    def g_pow(g, n, mul, gid):
        res = gid
        for _ in range(n):
            res = mul(res, g)
        return res

    def g_inv(g, mul, gid):
        return g_pow(g, g_ord(g, mul, gid) - 1, mul, gid)

    def gen_sz(gens, mul, gid):
        S = {gid}
        stk = [gid]
        while stk:
            cur = stk.pop()
            for g in gens:
                nx = mul(cur, g)
                if nx not in S:
                    S.add(nx)
                    stk.append(nx)
        return len(S)

    def count_hom_table(src_name, dst_els, dst_mul, dst_id):
        ords = {g: g_ord(g, dst_mul, dst_id) for g in dst_els}
        invs = {g: g_inv(g, dst_mul, dst_id) for g in dst_els}
        img_counts = Counter()

        if src_name == "Q3":
            # <s, r, z | s^2=1, r^3=1, srs=r^-1, z^3=1, sz=zs, rz=zr>
            s_cands = [g for g in dst_els if ords[g] in (1, 2)]
            r_cands = [g for g in dst_els if ords[g] in (1, 3)]
            for s in s_cands:
                for r in r_cands:
                    if dst_mul(dst_mul(s, r), s) != invs[r]:
                        continue
                    for z in r_cands:
                        if dst_mul(s, z) == dst_mul(z, s) and dst_mul(r, z) == dst_mul(z, r):
                            img_counts[gen_sz((s, r, z), dst_mul, dst_id)] += 1
        elif src_name == "BD5":
            # <a, b | a^10=1, b^2=a^5, b a b^-1 = a^-1>
            a_cands = [g for g in dst_els if 10 % ords[g] == 0]
            b_cands = [g for g in dst_els if 4 % ords[g] == 0]
            for a in a_cands:
                a5 = g_pow(a, 5, dst_mul, dst_id)
                ainv = invs[a]
                for b in b_cands:
                    if dst_mul(b, b) != a5:
                        continue
                    if dst_mul(dst_mul(b, a), invs[b]) != ainv:
                        continue
                    img_counts[gen_sz((a, b), dst_mul, dst_id)] += 1
        elif src_name == "2T":
            # <x, y | x^3 = y^3 = (xy)^2>
            for x in dst_els:
                x3 = g_pow(x, 3, dst_mul, dst_id)
                for y in dst_els:
                    if g_pow(y, 3, dst_mul, dst_id) != x3:
                        continue
                    xy = dst_mul(x, y)
                    if dst_mul(xy, xy) != x3:
                        continue
                    img_counts[gen_sz((x, y), dst_mul, dst_id)] += 1

        total = sum(img_counts.values())
        surj = img_counts.get(len(dst_els), 0)
        return {
            "hom": total,
            "surj": surj,
            "img_sizes": {str(k): v for k, v in sorted(img_counts.items())},
        }

    grp_defs = [
        ("Q3", Q3, q3_mul, Q3_id),
        ("2T", T2, t2_mul, T2_id),
        ("BD5", BD5, bd5_mul, BD5_id),
    ]
    hom_table = {}
    for sn, _, _, _ in grp_defs:
        for dn, dels, dmul, did in grp_defs:
            if sn == dn:
                continue
            hom_table[f"{sn}_to_{dn}"] = count_hom_table(sn, dels, dmul, did)

    q3_bd5_z2_only = (
        set(hom_table["Q3_to_BD5"]["img_sizes"].keys()).issubset({"1", "2"})
        and set(hom_table["BD5_to_Q3"]["img_sizes"].keys()).issubset({"1", "2"})
        and "2" in hom_table["Q3_to_BD5"]["img_sizes"]
        and "2" in hom_table["BD5_to_Q3"]["img_sizes"]
    )
    hom_table["Q3_BD5_prime2_only_Z2_bridge"] = q3_bd5_z2_only

    # 4. Explicit embeddings of BD_5 (order 20) and 2T (order 24) in SL(2, F_5) <= SL(2, F_25)
    SL2_F5 = list(s2_cache["SL2_F5"])
    m_mul = s2_cache["m_mul"]
    I2 = s2_cache["I2"]
    NI2 = s2_cache["NI2"]

    ords_f5 = {M: g_ord(M, m_mul, I2) for M in SL2_F5}
    invs_f5 = {M: g_inv(M, m_mul, I2) for M in SL2_F5}

    # Find explicit faithful BD_5 inside SL(2, F_5): a of order 10, b of order 4, b^2=a^5=-I, b a b^-1 = a^-1
    bd5_in_sl2 = False
    for a in SL2_F5:
        if ords_f5[a] != 10:
            continue
        a5 = g_pow(a, 5, m_mul, I2)
        if a5 != NI2:
            continue
        for b in SL2_F5:
            if ords_f5[b] != 4:
                continue
            if m_mul(b, b) == a5 and m_mul(m_mul(b, a), invs_f5[b]) == invs_f5[a]:
                if gen_sz((a, b), m_mul, I2) == 20:
                    bd5_in_sl2 = True
                    break
        if bd5_in_sl2:
            break

    # Find explicit faithful 2T inside SL(2, F_5): x^3 = y^3 = (xy)^2 = -I generating order 24
    t2_in_sl2 = False
    ord6 = [M for M in SL2_F5 if ords_f5[M] == 6]
    for x in ord6:
        x3 = g_pow(x, 3, m_mul, I2)
        if x3 != NI2:
            continue
        for y in ord6:
            if g_pow(y, 3, m_mul, I2) != x3:
                continue
            xy = m_mul(x, y)
            if m_mul(xy, xy) == x3 and gen_sz((x, y), m_mul, I2) == 24:
                t2_in_sl2 = True
                break
        if t2_in_sl2:
            break

    # 3-adic valuation of |SL(2, F_25)| = 15600 and |G_E8| = 156000
    def v_p(n, p):
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        return c

    v3_sl2 = v_p(15600, 3)
    v3_ge8 = v_p(156000, 3)
    v3_q3 = v_p(18, 3)
    q3_obstructed = (v3_ge8 < v3_q3) and (156000 % 18 != 0)

    # 5. B704 Multiquadratic Galois Cube via DIRECT symbolic expansion of all 8 conjugates!
    x = sp.Symbol("x")
    r3, r5, r7 = sp.sqrt(-3), sp.sqrt(5), sp.sqrt(-7)
    conjugates_8 = [
        e3 * r3 + e5 * r5 + e7 * r7
        for e3 in (-1, 1)
        for e5 in (-1, 1)
        for e7 in (-1, 1)
    ]
    p8_expr = sp.Integer(1)
    for conj in conjugates_8:
        p8_expr = sp.expand(p8_expr * (x - conj))
    P8 = sp.Poly(p8_expr, x, domain="QQ")
    p8_coeffs = [int(c) for c in P8.all_coeffs()]
    p8_irred = bool(P8.is_irreducible)
    all_8_roots_ok = all(sp.simplify(p8_expr.subs(x, c)) == 0 for c in conjugates_8)

    # V_4 plane Q(sqrt(-3), sqrt(5)) by direct symbolic expansion
    conjugates_4 = [e3 * r3 + e5 * r5 for e3 in (-1, 1) for e5 in (-1, 1)]
    p4_expr = sp.Integer(1)
    for conj in conjugates_4:
        p4_expr = sp.expand(p4_expr * (x - conj))
    P4 = sp.Poly(p4_expr, x, domain="QQ")
    p4_coeffs = [int(c) for c in P4.all_coeffs()]
    p4_irred = bool(P4.is_irreducible)

    # 7 non-trivial quadratic subfields of Q(sqrt(-3), sqrt(5), sqrt(-7))
    subfields = []
    for mask in range(1, 8):
        d = 1
        if mask & 1:
            d *= -3
        if mask & 2:
            d *= 5
        if mask & 4:
            d *= -7
        subfields.append(d)
    imag_sub = sorted([d for d in subfields if d < 0], reverse=True)
    real_sub = sorted([d for d in subfields if d > 0])
    all_7_nonsquare = all(not (d > 0 and math.isqrt(d) ** 2 == d) for d in subfields)

    # Legendre / Kronecker multiplicativity across all 22 primes 7..97
    primes_22 = list(sp.primerange(7, 98))
    assert len(primes_22) == 22

    def leg(a, p):
        a_mod = a % p
        if a_mod == 0:
            return 0
        r = pow(a_mod, (p - 1) // 2, p)
        return 1 if r == 1 else -1

    kron_mult_ok = True
    for p in primes_22:
        l_m3 = leg(-3, p)
        l_5 = leg(5, p)
        l_m7 = leg(-7, p)
        if not (
            l_m3 * l_5 == leg(-15, p)
            and l_m3 * l_m7 == leg(21, p)
            and l_5 * l_m7 == leg(-35, p)
            and l_m3 * l_5 * l_m7 == leg(105, p)
        ):
            kron_mult_ok = False
            break

    s3_ok = bool(
        q3_bd5_z2_only
        and bd5_in_sl2
        and t2_in_sl2
        and q3_obstructed
        and v3_sl2 == 1
        and P8.degree() == 8
        and p8_irred
        and all_8_roots_ok
        and P4.degree() == 4
        and p4_irred
        and all_7_nonsquare
        and kron_mult_ok
    )

    return {
        "ok": s3_ok,
        "hom_and_surj_table": hom_table,
        "SL2_F25_embeddings": {
            "2T_embeds_in_SL2_F5_and_F25": t2_in_sl2,
            "BD5_embeds_in_SL2_F5_and_F25": bd5_in_sl2,
            "Q3_lagrange_obstructed_in_G_E8": q3_obstructed,
            "v3_SL2_F25": v3_sl2,
            "v3_G_E8": v3_ge8,
        },
        "B704_galois_cube": {
            "cube_degree": int(P8.degree()),
            "cube_irreducible": p8_irred,
            "cube_poly_desc": p8_coeffs,
            "all_8_galois_conjugates_verified": all_8_roots_ok,
            "v4_plane_degree": int(P4.degree()),
            "v4_irreducible": p4_irred,
            "v4_poly_desc": p4_coeffs,
            "all_7_discriminants_nonsquare": all_7_nonsquare,
            "imag_silent_subfields": imag_sub,
            "real_audible_subfields": real_sub,
            "kronecker_multiplicative_22_primes": kron_mult_ok,
        },
    }


# =============================================================================
# 5 Independent Referee Planted Fault Controls (RPF1..RPF5)
# =============================================================================

def run_referee_planted_faults(s1_cache, s2_cache):
    Me_15 = s1_cache["Me_15"]
    Mo_15 = s1_cache["Mo_15"]
    S_heis = s1_cache["S_heis"]
    Up = s1_cache["Up"]
    F = s2_cache["F"]

    # RPF1: theta=0 mirror-symmetric flux collapses |J| to 0 (< 1e-40)
    o_rpf1 = extract_observables((3 * mp.eye(3) + S_heis) * Me_15, (3 * mp.eye(3) + S_heis) * Mo_15)
    rpf1_caught = bool(o_rpf1["abs_J"] < TOL_ZERO_J)

    # RPF2: identical left unitary Up applied to BOTH M_even and M_odd leaves |J| == 0
    o_rpf2 = extract_observables(Up * Me_15, Up * Mo_15)
    rpf2_caught = bool(o_rpf2["abs_J"] < TOL_ZERO_J)

    # RPF3: wrong-sign Fricke move (x, z, x*z + y) breaks kappa conservation on F_5[t]/(t^2 - 3)
    add, sub, mul, TWO = F.add, F.sub, F.mul, F.TWO

    def kappa_of(x, y, z):
        s = add[add[mul[x][x]][mul[y][y]]][mul[z][z]]
        return sub[sub[s][mul[mul[x][y]][z]]][TWO]

    violations = 0
    for x in range(25):
        for y in range(25):
            for z in range(25):
                k0 = kappa_of(x, y, z)
                k_bad = kappa_of(x, z, add[mul[x][z]][y])
                if k_bad != k0:
                    violations += 1
    rpf3_caught = bool(violations > 0)

    # RPF4: direct product SL(2, F_25) x BD_5 without central Z/2 identification
    dp_order = s2_cache["sl2_order"] * s2_cache["bd5_order"]
    dp_ab = s2_cache["bd5_ab_order"]
    rpf4_caught = bool(dp_order == 312000 and dp_order != 156000 and dp_ab == 4 and dp_ab != 2)

    # RPF5: replacing sqrt(-7) by sqrt(-15) collapses degree-8 polynomial to degree-4 factors
    x = sp.Symbol("x")
    r3, r5, r15 = sp.sqrt(-3), sp.sqrt(5), sp.sqrt(-15)
    p_bad = sp.Integer(1)
    for e3 in (-1, 1):
        for e5 in (-1, 1):
            for e15 in (-1, 1):
                p_bad = sp.expand(p_bad * (x - (e3 * r3 + e5 * r5 + e15 * r15)))
    P_bad = sp.Poly(p_bad, x, domain="QQ")
    _, factors = P_bad.factor_list()
    max_fac_deg = max(f.degree() for f, _ in factors)
    rpf5_caught = bool((not P_bad.is_irreducible) and max_fac_deg == 4)

    controls = {
        "RPF1_theta0_symmetric_flux_collapses_J": rpf1_caught,
        "RPF2_identical_left_unitary_keeps_J_zero": rpf2_caught,
        "RPF3_wrong_sign_fricke_breaks_kappa": rpf3_caught,
        "RPF3_violation_count": violations,
        "RPF4_direct_product_misses_central_Z2": rpf4_caught,
        "RPF5_dependent_sqrt_minus15_collapses_deg8_to_4": rpf5_caught,
    }
    n_caught = sum(
        1
        for k in (
            "RPF1_theta0_symmetric_flux_collapses_J",
            "RPF2_identical_left_unitary_keeps_J_zero",
            "RPF3_wrong_sign_fricke_breaks_kappa",
            "RPF4_direct_product_misses_central_Z2",
            "RPF5_dependent_sqrt_minus15_collapses_deg8_to_4",
        )
        if controls[k]
    )
    return controls, n_caught


# =============================================================================
# Hygiene, SHA-256, Control Execution, & Independent Producer Comparison
# =============================================================================

def count_ast_floats(py_path: Path) -> int:
    src = py_path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    )


def count_json_floats(obj) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def verify_sha_manifest(repo_root: Path, manifest_path: Path):
    results = {}
    ok = True
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        expected, rel_path = line.split(None, 1)
        rel_path = rel_path.strip()
        actual = sha256_file(repo_root / rel_path)
        match = actual == expected
        results[rel_path] = {"expected": expected, "actual": actual, "match": match}
        if not match:
            ok = False
    return ok, results


def compare_against_producer(ref_s1, ref_s2, ref_s3, prod, discrepancies):
    def check_eq(path, got, exp):
        if got != exp:
            discrepancies.append(f"MISMATCH {path}: referee={got!r} vs producer={exp!r}")

    def check_close(path, got_str, exp_str, tol):
        g = mp.mpf(got_str)
        e = mp.mpf(exp_str)
        diff = abs(g - e)
        if diff > tol:
            discrepancies.append(
                f"NUM_MISMATCH {path}: referee={got_str} vs producer={exp_str} (|diff|={mstr(diff, 6)} > {mstr(tol, 4)})"
            )

    def check_lt(path, val_str, bound):
        v = mp.mpf(val_str)
        if v >= bound:
            discrepancies.append(f"BOUND_FAIL {path}: val={val_str} >= {mstr(bound, 4)}")

    # --- S1 comparison ---
    ps1 = prod["S1_chiral_flux_L15_seam"]
    check_eq("S1.ok", ref_s1["ok"], ps1["ok"])
    for k in (
        "err_pflip_sl2f3_comm",
        "err_heis_sym_comm",
        "err_heis_ch_anticomm",
        "heis_spec_err",
        "odd_alpha_absJ_err",
        "unitary_err",
    ):
        check_lt(f"S1.prod.{k}", ps1[k], TOL_HAAR)
        check_lt(f"S1.ref.{k}", ref_s1[k], TOL_HAAR)
    check_lt("S1.prod.sl2f3_max_J", ps1["sl2f3_max_J"], TOL_ZERO_J)
    check_lt("S1.prod.sym_theta0_max_J", ps1["sym_theta0_max_J"], TOL_ZERO_J)
    check_lt("S1.prod.haar_10trial_max_err", ps1["haar_10trial_max_err"], TOL_HAAR)

    def cmp_obs_block(prefix, ro, po, check_full_matrices=True):
        check_eq(f"{prefix}.J_nonzero", ro["J_nonzero"], po["J_nonzero"])
        if ro["J_nonzero"]:
            check_close(f"{prefix}.abs_J", ro["abs_J"], po["abs_J"], TOL_PROD_J)
        else:
            check_lt(f"{prefix}.prod.abs_J", po["abs_J"], TOL_ZERO_J)
            check_lt(f"{prefix}.ref.abs_J", ro["abs_J"], TOL_ZERO_J)
        if check_full_matrices:
            for i in range(3):
                check_close(f"{prefix}.sv_e[{i}]", ro["sv_e_ratios"][i], po["sv_e_ratios"][i], TOL_PROD_SV)
                check_close(f"{prefix}.sv_o[{i}]", ro["sv_o_ratios"][i], po["sv_o_ratios"][i], TOL_PROD_SV)
                for j in range(3):
                    check_close(f"{prefix}.abs_V[{i}][{j}]", ro["abs_V"][i][j], po["abs_V"][i][j], TOL_PROD_V)

    for gname in ("L_15", "L_15_prime"):
        rg = ref_s1["per_genus"][gname]
        pg = ps1["per_genus"][gname]
        cmp_obs_block(f"S1.{gname}.bare", rg["bare"], pg["bare"], True)
        cmp_obs_block(
            f"S1.{gname}.heisenberg_parity_split_unitary_flux",
            rg["heisenberg_parity_split_unitary_flux"],
            pg["heisenberg_parity_split_unitary_flux"],
            True,
        )
        cmp_obs_block(
            f"S1.{gname}.heisenberg_same_hermitian_flux",
            rg["heisenberg_same_hermitian_flux"],
            pg["heisenberg_same_hermitian_flux"],
            True,
        )
        # For theta=0 symmetric and metaplectic SL(2, F_3), verify J==0 protection
        cmp_obs_block(
            f"S1.{gname}.heisenberg_theta0_symmetric",
            rg["heisenberg_theta0_symmetric"],
            pg["heisenberg_theta0_symmetric"],
            False,
        )
        cmp_obs_block(
            f"S1.{gname}.metaplectic_SL2_F3_coupled",
            rg["metaplectic_SL2_F3_coupled"],
            pg["metaplectic_SL2_F3_coupled"],
            False,
        )
        # Covariance checks
        for ck in ("dJ_S", "dJ_T"):
            check_close(
                f"S1.{gname}.cov_parity_unitary.{ck}",
                rg["cov_parity_unitary"][ck],
                pg["cov_parity_unitary"][ck],
                TOL_PROD_V,
            )
            check_close(
                f"S1.{gname}.cov_same_hermitian.{ck}",
                rg["cov_same_hermitian"][ck],
                pg["cov_same_hermitian"][ck],
                TOL_PROD_V,
            )
        for ck in ("dV_S", "dV_T"):
            check_close(
                f"S1.{gname}.cov_parity_unitary.{ck}",
                rg["cov_parity_unitary"][ck],
                pg["cov_parity_unitary"][ck],
                TOL_PROD_V,
            )
        check_lt(f"S1.{gname}.cov_parity_unitary.prod.dJ_T3", pg["cov_parity_unitary"]["dJ_T3"], TOL_ZERO_J)
        check_lt(f"S1.{gname}.cov_parity_unitary.prod.dV_T3", pg["cov_parity_unitary"]["dV_T3"], TOL_ZERO_J)
        check_lt(f"S1.{gname}.cov_same_hermitian.prod.dJ_T3", pg["cov_same_hermitian"]["dJ_T3"], TOL_ZERO_J)

    for mode in ("bare", "parity_split_unitary", "same_hermitian"):
        cmp_obs_block(
            f"S1.cross_genus.{mode}",
            ref_s1["cross_genus_L15even_L15podd"][mode],
            ps1["cross_genus_L15even_L15podd"][mode],
            True,
        )

    # Sweep comparison
    check_eq(
        "S1.sweep.len",
        len(ref_s1["L15_parity_unitary_angle_sweep"]),
        len(ps1["L15_parity_unitary_angle_sweep"]),
    )
    for r_item, p_item in zip(
        ref_s1["L15_parity_unitary_angle_sweep"],
        ps1["L15_parity_unitary_angle_sweep"],
    ):
        check_eq("S1.sweep.angle", r_item["alpha_over_pi"], p_item["alpha_over_pi"])
        check_close(
            f"S1.sweep[{r_item['alpha_over_pi']}]",
            r_item["abs_J"],
            p_item["abs_J"],
            TOL_PROD_J,
        )

    # --- S2 comparison ---
    ps2 = prod["S2_G_E8_and_F25_markoff"]
    check_eq("S2.ok", ref_s2["ok"], ps2["ok"])
    check_eq("S2.G_E8_structure", ref_s2["G_E8_structure"], ps2["G_E8_structure"])

    rm = ref_s2["F25_markoff_variety"]
    pm = ps2["F25_markoff_variety"]
    for k in (
        "total_points",
        "kappa_conserved_all_15625",
        "global_fixed_points_count",
        "global_fixed_points",
        "swap_P_changes_any_orbit_across_25_leaves",
    ):
        check_eq(f"S2.markoff.{k}", rm[k], pm[k])
    check_eq("S2.markoff.leaves_keys", sorted(rm["leaves_summary"].keys()), sorted(pm["leaves_summary"].keys()))
    for leaf_lbl in sorted(pm["leaves_summary"].keys()):
        check_eq(
            f"S2.markoff.leaf[{leaf_lbl}]",
            rm["leaves_summary"][leaf_lbl],
            pm["leaves_summary"][leaf_lbl],
        )

    rc = ref_s2["cusp_leaf_kappa_minus2"]
    pc = ps2["cusp_leaf_kappa_minus2"]
    check_eq("S2.cusp.total_points", rc["total_points"], pc["total_points"])
    check_eq("S2.cusp.n_orbits_LR", rc["n_orbits_LR"], pc["n_orbits_LR"])
    check_eq("S2.cusp.frob_torsor", rc["frob_torsor"], pc["frob_torsor"])
    for ro, po in zip(rc["orbits"], pc["orbits"]):
        oid = po["orbit_idx"]
        for field in (
            "size",
            "subgroup_order",
            "all_in_F5",
            "any_in_F5",
            "frob_fixed_setwise",
            "frob_maps_to_orbit",
            "swap_P_fixed_setwise",
            "contains_m004_fiber",
        ):
            check_eq(f"S2.cusp.orbit[{oid}].{field}", ro[field], po[field])

    # --- S3 comparison ---
    ps3 = prod["S3_prime235_and_B704_seam"]
    check_eq("S3.ok", ref_s3["ok"], ps3["ok"])
    check_eq("S3.hom_and_surj_table", ref_s3["hom_and_surj_table"], ps3["hom_and_surj_table"])
    for k in (
        "2T_embeds_in_SL2_F5_and_F25",
        "BD5_embeds_in_SL2_F5_and_F25",
        "Q3_lagrange_obstructed_in_G_E8",
        "v3_SL2_F25",
    ):
        check_eq(f"S3.SL2_F25_embeddings.{k}", ref_s3["SL2_F25_embeddings"][k], ps3["SL2_F25_embeddings"][k])
    check_eq("S3.B704_galois_cube", ref_s3["B704_galois_cube"], ps3["B704_galois_cube"])

    # --- Top-level producer flags ---
    check_eq("prod.all_gates_passed", True, prod["all_gates_passed"])
    check_eq("prod.pf_caught", 5, prod["pf_caught"])
    check_eq("prod.ast_floats", 0, prod["ast_floats"])
    check_eq("prod.json_floats", 0, prod["json_floats"])


def main():
    script_path = Path(__file__).resolve()
    ref_dir = script_path.parent
    card_dir = ref_dir.parent
    repo_root = card_dir.parent.parent

    # 1. Run 100% independent re-derivations FIRST (before reading producer JSON!)
    s1 = run_S1()
    s2 = run_S2()
    s3 = run_S3(s2["_cache"])
    rpf_controls, rpf_caught = run_referee_planted_faults(s1["_cache"], s2["_cache"])

    # Strip private caches before serialization
    s1_clean = {k: v for k, v in s1.items() if k != "_cache"}
    s2_clean = {k: v for k, v in s2.items() if k != "_cache"}

    # 2. Independent hygiene, SHA-256, and producer control audit
    discrepancies = []

    script_sha_ok, script_sha_details = verify_sha_manifest(repo_root, card_dir / "SCRIPT_SHA256.txt")
    output_sha_ok, output_sha_details = verify_sha_manifest(repo_root, card_dir / "OUTPUT_SHA256.txt")
    if not script_sha_ok:
        discrepancies.append("SHA256 mismatch in SCRIPT_SHA256.txt")
    if not output_sha_ok:
        discrepancies.append("SHA256 mismatch in OUTPUT_SHA256.txt")

    prod_decisive = card_dir / "a2_weave_e8_weil_seam_decisive.py"
    prod_control = card_dir / "a2_weave_e8_weil_seam_control.py"
    prod_out_path = card_dir / "a2_weave_e8_weil_seam_out.json"

    ast_floats_audit = {
        "producer_decisive": count_ast_floats(prod_decisive),
        "producer_control": count_ast_floats(prod_control),
        "referee_script": count_ast_floats(script_path),
    }
    for k, v in ast_floats_audit.items():
        if v != 0:
            discrepancies.append(f"AST float violation in {k}: {v}")

    # Run producer control script via python3 -I
    ctrl_proc = subprocess.run(
        [sys.executable, "-I", str(prod_control)],
        capture_output=True,
        cwd=str(repo_root),
    )
    ctrl_ok = (ctrl_proc.returncode == 1) and (len(ctrl_proc.stderr) == 0)
    if not ctrl_ok:
        discrepancies.append(
            f"Producer control audit failed: exit={ctrl_proc.returncode}, stderr_bytes={len(ctrl_proc.stderr)}"
        )

    # 3. Load sealed producer output ONLY for final comparison
    prod_data = json.loads(prod_out_path.read_text(encoding="utf-8"))
    prod_json_floats = count_json_floats(prod_data)
    if prod_json_floats != 0:
        discrepancies.append(f"Producer JSON float violation: {prod_json_floats}")

    compare_against_producer(s1_clean, s2_clean, s3, prod_data, discrepancies)

    if rpf_caught != 5:
        discrepancies.append(f"Referee planted fault controls caught {rpf_caught}/5")

    verdict = "PASS" if (len(discrepancies) == 0 and s1_clean["ok"] and s2_clean["ok"] and s3["ok"]) else "FAIL"

    out_payload = {
        "card": "A2-WEAVE-E8-WEIL-SEAM",
        "role": "DISJOINT_COLD_ROOM_ZERO_TRUST_REFEREE",
        "verdict": verdict,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "S1_independent": s1_clean,
        "S2_independent": s2_clean,
        "S3_independent": s3,
        "referee_planted_fault_controls": rpf_controls,
        "rpf_caught": rpf_caught,
        "producer_control_audit": {
            "exit_code": ctrl_proc.returncode,
            "stderr_bytes": len(ctrl_proc.stderr),
            "stdout": ctrl_proc.stdout.decode("utf-8", errors="replace").strip(),
            "ok": ctrl_ok,
        },
        "sha256_verification": {
            "SCRIPT_SHA256_ok": script_sha_ok,
            "OUTPUT_SHA256_ok": output_sha_ok,
            "script_details": script_sha_details,
            "output_details": output_sha_details,
        },
        "ast_floats": ast_floats_audit,
        "producer_json_floats": prod_json_floats,
        "referee_json_floats": 0,
    }

    # Verify zero JSON floats in our own output payload before writing
    ref_jfloats = count_json_floats(out_payload)
    out_payload["referee_json_floats"] = ref_jfloats
    if ref_jfloats != 0:
        out_payload["verdict"] = "FAIL"
        out_payload["discrepancies"].append(f"Referee JSON float violation: {ref_jfloats}")
        out_payload["discrepancies_count"] = len(out_payload["discrepancies"])

    out_path = ref_dir / "referee_a2_weave_e8_weil_seam_out.json"
    out_path.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Write REFEREE_SHA256.txt covering referee script and referee output
    rel_script = os.path.relpath(script_path, repo_root)
    rel_out = os.path.relpath(out_path, repo_root)
    sha_lines = [
        f"{sha256_file(script_path)}  {rel_script}",
        f"{sha256_file(out_path)}  {rel_out}",
    ]
    (ref_dir / "REFEREE_SHA256.txt").write_text("\n".join(sha_lines) + "\n", encoding="utf-8")

    print(
        f"REFEREE: VERDICT={out_payload['verdict']} "
        f"discrepancies={out_payload['discrepancies_count']} "
        f"S1={s1_clean['ok']} S2={s2_clean['ok']} S3={s3['ok']} "
        f"RPF={rpf_caught}/5 ctrl_exit={ctrl_proc.returncode} "
        f"ast_floats={ast_floats_audit['referee_script']} json_floats={ref_jfloats}"
    )
    if out_payload["discrepancies"]:
        for d in out_payload["discrepancies"]:
            print(f"  DISCREPANCY: {d}")
    sys.exit(0 if out_payload["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
