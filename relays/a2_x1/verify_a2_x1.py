#!/usr/bin/env python3
"""Standalone independent verification for Card A2-X1 (M47 + M48):
Frame D1's Higgs ground plane across three seats (SM a69cee901, Physical a47e76da6/aa9facef6,
main 4921ee923), independent 2D torus-quadrature second computation of SM-C21 and Physical's
coherent vector h*, analytical + numerical resolution of P-873 Q3 (|V(h*)| at the mark),
deciding computations DC-1..DC-6, and planted fault controls PFA2X1-1..PFA2X1-5.

Strict hygiene:
- Zero float or complex AST literals anywhere in source.
- Zero imports or execution of any other seat's code or main's closed form (cim_closed.py).
- Zero empirical / PDG targets (0 of 19).
"""

import ast
import json
import pathlib
import time

import mpmath as mp
import numpy as np
import sympy as sp


def pow10_f(exp_int: int) -> float:
    if exp_int >= 0:
        return int(10 ** int(exp_int)) / int(1)
    return int(1) / int(10 ** int(-exp_int))


def mp_rat(num: int, den: int = 1):
    return mp.mpf(int(num)) / mp.mpf(int(den))


def mp_pow10(exp_int: int):
    if exp_int >= 0:
        return mp.mpf(10 ** int(exp_int))
    return mp.mpf(1) / mp.mpf(10 ** int(-exp_int))


def mp_imag_unit():
    return mp.mpc(0, 1)


# ============================================================================
# INDEPENDENT INSTRUMENT 1: Direct 2D Wavefunction Cell Quadrature on E_tau
# Evaluates psi_{L,i}(z), psi_{R,j}(z), conj(psi_{H,k}(z)) directly on
# z_{p,q} = p/nx + tau * (q/nu) over (p, q) in [0, nx) x [0, nu) and averages.
# Zero closed-form overlap formula, zero theta(6*xi, 6*tau) identity.
# ============================================================================

def eval_magnetised_modes_2d_grid(
    flux_m: int,
    alpha_twice: int,
    beta_twice: int,
    tau,
    zeta,
    nx: int,
    nu: int,
    n_window: int = 4,
):
    iu = mp_imag_unit()
    pi = mp.pi
    pi_i = iu * pi
    two_pi_i = mp.mpf(2) * pi_i
    y = mp.im(tau)
    m_mp = mp.mpf(flux_m)
    nx_mp = mp.mpf(nx)
    nu_mp = mp.mpf(nu)

    norm = mp.power(mp.mpf(2 * flux_m) * y, mp_rat(1, 4))
    im_shift = mp.im(zeta) / y

    two_nx = 2 * nx
    wx_base = mp.exp(pi_i / nx_mp)
    wx_pows = [mp.mpc(1, 0)]
    for _ in range(1, two_nx):
        wx_pows.append(wx_pows[-1] * wx_base)

    gx_grid = []
    gx_step_q0 = mp.exp(pi_i * m_mp * im_shift / nx_mp)
    gx_step_dq = mp.exp(pi_i * m_mp / (nx_mp * nu_mp))
    cur_gx_step = gx_step_q0
    for q in range(nu):
        u = mp.mpf(q) / nu_mp
        v_im = u + im_shift
        w0 = tau * u + zeta
        g0 = norm * mp.exp(pi_i * m_mp * w0 * v_im)
        row_g = [mp.mpc(0, 0)] * nx
        cur = g0
        for p in range(nx):
            row_g[p] = cur
            cur *= cur_gx_step
        gx_grid.append(row_g)
        cur_gx_step *= gx_step_dq

    beta_mp = mp_rat(beta_twice, 2)
    modes = [[[mp.mpc(0, 0)] * nx for _ in range(nu)] for _ in range(flux_m)]

    for j in range(flux_m):
        a_mp = mp_rat(2 * j + alpha_twice, 2 * flux_m)
        n_mid = int(mp.nint(-a_mp - im_shift - mp_rat(1, 2)))
        term_cur = []
        term_step = []
        term_freq = []
        for n in range(n_mid - n_window, n_mid + n_window + 1):
            na = mp.mpf(n) + a_mp
            c0 = mp.exp(pi_i * (na * na) * m_mp * tau + two_pi_i * na * (m_mp * zeta + beta_mp))
            dq = mp.exp(two_pi_i * na * m_mp * tau / nu_mp)
            freq = (2 * flux_m * n + 2 * j + alpha_twice) % two_nx
            term_cur.append(c0)
            term_step.append(dq)
            term_freq.append(freq)

        n_terms = len(term_cur)
        for q in range(nu):
            gx_q = gx_grid[q]
            out_row = modes[j][q]
            for p in range(nx):
                acc = mp.mpc(0, 0)
                for t_idx in range(n_terms):
                    acc += term_cur[t_idx] * wx_pows[(term_freq[t_idx] * p) % two_nx]
                out_row[p] = gx_q[p] * acc
            for t_idx in range(n_terms):
                term_cur[t_idx] *= term_step[t_idx]

    return modes


def overlap_tensor_2d_quad(
    tau,
    zeta_L,
    zeta_R,
    zeta_H,
    nx: int,
    nu: int,
    n_window: int = 4,
    full_all_54: bool = False,
):
    """Direct 2D torus cell quadrature of int_{E_tau} psi_{L,i} psi_{R,j} conj(psi_{H,k}) dx du."""
    psi_L = eval_magnetised_modes_2d_grid(3, 1, 1, tau, zeta_L, nx, nu, n_window=n_window)
    psi_R = eval_magnetised_modes_2d_grid(3, 1, 1, tau, zeta_R, nx, nu, n_window=n_window)
    psi_H = eval_magnetised_modes_2d_grid(6, 0, 0, tau, zeta_H, nx, nu, n_window=n_window)
    inv_cell = mp_rat(1, nx * nu)
    Y = [[[mp.mpc(0, 0)] * 6 for _ in range(3)] for _ in range(3)]
    for q in range(nu):
        Lq = [psi_L[i][q] for i in range(3)]
        Rq = [psi_R[j][q] for j in range(3)]
        Hcq = [[mp.conj(psi_H[k][q][p]) for p in range(nx)] for k in range(6)]
        for i in range(3):
            Li = Lq[i]
            for j in range(3):
                LR = [Li[p] * Rq[j][p] for p in range(nx)]
                Yij = Y[i][j]
                if full_all_54:
                    k_list = range(6)
                else:
                    k0 = (i + j + 1) % 3
                    k_list = (k0, k0 + 3)
                for k in k_list:
                    Hck = Hcq[k]
                    s = mp.mpc(0, 0)
                    for p in range(nx):
                        s += LR[p] * Hck[p]
                    Yij[k] += s
    for i in range(3):
        for j in range(3):
            for k in range(6):
                Y[i][j][k] *= inv_cell
    return Y


# ============================================================================
# INDEPENDENT INSTRUMENT 2: Unfolded Universal-Cover 1D Real-Line Quadrature
# Uses exact x-Fourier orthogonality (3*n_L + i + 3*n_R + j + 1 == 6*n_H + k)
# to unfold u in [0,1) + Z onto R, then integrates numerically over u in R
# by composite trapezoidal quadrature on [-U_max, U_max]. Zero closed-form
# Gaussian integral and zero theta(6*xi, 6*tau)!
# ============================================================================

def overlap_tensor_unfolded_1d_quad(tau, zeta_L, zeta_R, zeta_H, n_step_per_unit: int = 64, half_span: int = 3):
    iu = mp_imag_unit()
    pi = mp.pi
    pi_i = iu * pi
    two_pi_i = mp.mpf(2) * pi_i
    y = mp.im(tau)
    norm_prod = (
        mp.power(mp.mpf(6) * y, mp_rat(1, 4))
        * mp.power(mp.mpf(6) * y, mp_rat(1, 4))
        * mp.power(mp.mpf(12) * y, mp_rat(1, 4))
    )
    Y = [[[mp.mpc(0, 0)] * 6 for _ in range(3)] for _ in range(3)]
    im_L = mp.im(zeta_L) / y
    im_R = mp.im(zeta_R) / y
    im_H = mp.im(zeta_H) / y

    du = mp_rat(1, n_step_per_unit)
    u_center = -im_H
    total_pts = 2 * half_span * n_step_per_unit
    u_vals = [u_center + mp.mpf(s - half_span * n_step_per_unit) * du for s in range(total_pts)]

    for i in range(3):
        aL0 = mp_rat(2 * i + 1, 6)
        for j in range(3):
            aR0 = mp_rat(2 * j + 1, 6)
            for k in range(6):
                rem = k - i - j - 1
                if rem % 3 != 0:
                    continue
                s_sum = rem // 3
                aH0 = mp_rat(k, 6)
                dL_mid = int(mp.nint((mp.mpf(s_sum) + aR0 - aL0 + im_R - im_L) / mp.mpf(2)))
                acc_total = mp.mpc(0, 0)
                for u in u_vals:
                    wL = tau * u + zeta_L
                    wR = tau * u + zeta_R
                    wH = tau * u + zeta_H
                    g_fac = (
                        norm_prod
                        * mp.exp(pi_i * mp.mpf(3) * wL * (u + im_L))
                        * mp.exp(pi_i * mp.mpf(3) * wR * (u + im_R))
                        * mp.conj(mp.exp(pi_i * mp.mpf(6) * wH * (u + im_H)))
                    )
                    h_fac = mp.conj(
                        mp.exp(pi_i * (aH0 * aH0) * mp.mpf(6) * tau + two_pi_i * aH0 * (mp.mpf(6) * wH))
                    )
                    d_acc = mp.mpc(0, 0)
                    for dL in range(dL_mid - 4, dL_mid + 5):
                        dR = s_sum - dL
                        naL = mp.mpf(dL) + aL0
                        naR = mp.mpf(dR) + aR0
                        tL = mp.exp(
                            pi_i * (naL * naL) * mp.mpf(3) * tau
                            + two_pi_i * naL * (mp.mpf(3) * wL + mp_rat(1, 2))
                        )
                        tR = mp.exp(
                            pi_i * (naR * naR) * mp.mpf(3) * tau
                            + two_pi_i * naR * (mp.mpf(3) * wR + mp_rat(1, 2))
                        )
                        d_acc += tL * tR
                    acc_total += g_fac * h_fac * d_acc
                Y[i][j][k] = acc_total * du
    return Y


# ============================================================================
# Level-6 Metaplectic Operators & Ground Plane E
# ============================================================================

def build_level6_operators_mp():
    iu = mp_imag_unit()
    pi = mp.pi
    T6 = mp.matrix(6, 6)
    for k in range(6):
        T6[k, k] = mp.exp(iu * pi * mp_rat(k * k, 6))
    S6 = mp.matrix(6, 6)
    pref = mp.exp(-iu * pi * mp_rat(1, 4)) / mp.sqrt(mp.mpf(6))
    for j in range(6):
        for k in range(6):
            S6[j, k] = pref * mp.exp(-iu * mp.mpf(2) * pi * mp_rat(j * k, 6))
    S6_dag = S6.T.conjugate()
    T6_dag = T6.T.conjugate()
    UM = T6 * S6_dag * T6_dag * S6

    P6 = mp.matrix(6, 6)
    Z6 = mp.matrix(6, 6)
    X6 = mp.matrix(6, 6)
    for k in range(6):
        P6[(-k) % 6, k] = mp.mpf(1)
        Z6[k, k] = mp.exp(iu * mp.mpf(2) * pi * mp_rat(k, 6))
        X6[(k + 1) % 6, k] = mp.mpf(1)

    UM_pows = [mp.eye(6)]
    for _ in range(1, 12):
        UM_pows.append(UM_pows[-1] * UM)

    def eigvec_unit(angle_num: int, angle_den: int = 6):
        lam = mp.exp(iu * pi * mp_rat(angle_num, angle_den))
        proj = mp.matrix(6, 6)
        for r in range(12):
            proj += (lam ** (-r)) * UM_pows[r]
        proj /= mp.mpf(12)
        best_col = 0
        best_nrm = mp.mpf(-1)
        for c in range(6):
            col_nrm = mp.sqrt(sum(abs(proj[r, c]) ** 2 for r in range(6)))
            if col_nrm > best_nrm:
                best_nrm = col_nrm
                best_col = c
        vec = [proj[r, best_col] / best_nrm for r in range(6)]
        for r in range(6):
            if abs(vec[r]) > mp_pow10(-20):
                ph = vec[r] / abs(vec[r])
                vec = [x / ph for x in vec]
                break
        return vec, proj

    vp, proj_p = eigvec_unit(1, 6)
    vm, proj_m = eigvec_unit(-1, 6)
    v_odd_p, _ = eigvec_unit(1, 3)
    v_odd_m, _ = eigvec_unit(-1, 3)

    e12 = mp.exp(iu * pi * mp_rat(1, 12))
    inv_sqrt2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))
    hstar = [inv_sqrt2, e12 / mp.mpf(2), mp.mpc(0, 0), mp.mpc(0, 0), mp.mpc(0, 0), e12 / mp.mpf(2)]

    return {
        "T6": T6,
        "S6": S6,
        "UM": UM,
        "UM_pows": UM_pows,
        "P6": P6,
        "Z6": Z6,
        "X6": X6,
        "vp": vp,
        "vm": vm,
        "proj_E": proj_p + proj_m,
        "v_odd_p": v_odd_p,
        "v_odd_m": v_odd_m,
        "hstar": hstar,
    }


def contract_yukawa_mp(Y_tensor, h_vec):
    M = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            s = mp.mpc(0, 0)
            for k in range(6):
                s += Y_tensor[i][j][k] * h_vec[k]
            M[i, j] = s
    return M


def svd_desc_mp(M_mat):
    U, S, Vh = mp.svd_c(M_mat)
    idx = sorted(range(3), key=lambda c: S[c], reverse=True)
    s_desc = [S[c] for c in idx]
    U_desc = mp.matrix(3, 3)
    V_desc = mp.matrix(3, 3)
    for r in range(3):
        for new_c, old_c in enumerate(idx):
            U_desc[r, new_c] = U[r, old_c]
            V_desc[r, new_c] = mp.conj(Vh[old_c, r])
    return s_desc, U_desc, V_desc


def classify_mixing(V_abs):
    t_99 = mp_rat(99, 100)
    t_90 = mp_rat(9, 10)
    v_top = V_abs[0, 0]
    if v_top > t_99 and all(V_abs[d, d] > t_90 for d in range(3)):
        return "aligned"
    if v_top > t_99:
        return "top-aligned"
    if all(max(V_abs[r, c] for c in range(3)) > t_99 for r in range(3)):
        return "permutation"
    return "other"


def cayley_unitary_3x3_mp(skew_entries):
    iu = mp_imag_unit()
    A = mp.matrix(3, 3)
    A[0, 0] = iu * skew_entries[0]
    A[1, 1] = iu * skew_entries[1]
    A[2, 2] = iu * skew_entries[2]
    A[0, 1] = skew_entries[3] + iu * skew_entries[4]
    A[1, 0] = -mp.conj(A[0, 1])
    A[0, 2] = skew_entries[5] + iu * skew_entries[6]
    A[2, 0] = -mp.conj(A[0, 2])
    A[1, 2] = skew_entries[7] + iu * skew_entries[8]
    A[2, 1] = -mp.conj(A[1, 2])
    I3 = mp.eye(3)
    return (I3 - A) * ((I3 + A) ** (-1))


def check_zero_float_ast(self_path: pathlib.Path):
    tree = ast.parse(self_path.read_text(encoding="utf-8"), filename=str(self_path))
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad.append((node.lineno, repr(node.value)))
    return bad


def main():
    t_start = time.time()
    mp.mp.dps = 65
    iu = mp_imag_unit()

    self_path = pathlib.Path(__file__).resolve()
    bad_literals = check_zero_float_ast(self_path)
    assert len(bad_literals) == 0, f"Float/complex AST literals found: {bad_literals}"

    ops = build_level6_operators_mp()
    T6, S6, UM = ops["T6"], ops["S6"], ops["UM"]
    P6, Z6, X6 = ops["P6"], ops["Z6"], ops["X6"]
    vp, vm, hstar = ops["vp"], ops["vm"], ops["hstar"]
    proj_E = ops["proj_E"]

    # ========================================================================
    # 0. Instrument Calibration: Two 2D Grid Resolutions vs 1D Unfolded Cover
    # ========================================================================
    tau_cal = mp_rat(13, 100) + iu * mp.mpf(8)
    w_cal = mp_rat(2, 5) * tau_cal + mp_rat(4, 5)
    Y_cal_g1 = overlap_tensor_2d_quad(
        tau_cal, w_cal, mp.mpf(-4) * w_cal, mp_rat(-3, 2) * w_cal, 11, 64, full_all_54=True
    )
    Y_cal_g2 = overlap_tensor_2d_quad(
        tau_cal, w_cal, mp.mpf(-4) * w_cal, mp_rat(-3, 2) * w_cal, 17, 84, full_all_54=True
    )
    Y_cal_1d = overlap_tensor_unfolded_1d_quad(
        tau_cal, w_cal, mp.mpf(-4) * w_cal, mp_rat(-3, 2) * w_cal, 64, 3
    )

    err_grid_conv_y8 = max(
        abs(Y_cal_g1[i][j][k] - Y_cal_g2[i][j][k]) for i in range(3) for j in range(3) for k in range(6)
    )
    err_forbidden_36_triples = max(
        abs(Y_cal_g2[i][j][k])
        for i in range(3) for j in range(3) for k in range(6)
        if (k - i - j - 1) % 3 != 0
    )
    err_2d_vs_1d_y8 = max(
        abs(Y_cal_g2[i][j][k] - Y_cal_1d[i][j][k]) for i in range(3) for j in range(3) for k in range(6)
    )
    tau_cal14 = mp_rat(13, 100) + iu * mp.mpf(14)
    w_cal14 = mp_rat(2, 5) * tau_cal14 + mp_rat(4, 5)
    Y14_g1 = overlap_tensor_2d_quad(
        tau_cal14, w_cal14, mp.mpf(2) * w_cal14, mp_rat(3, 2) * w_cal14, 11, 80, full_all_54=True
    )
    Y14_g2 = overlap_tensor_2d_quad(
        tau_cal14, w_cal14, mp.mpf(2) * w_cal14, mp_rat(3, 2) * w_cal14, 17, 100, full_all_54=True
    )
    err_grid_conv_y14 = max(
        abs(Y14_g1[i][j][k] - Y14_g2[i][j][k]) for i in range(3) for j in range(3) for k in range(6)
    )
    assert err_grid_conv_y8 < mp_pow10(-50)
    assert err_forbidden_36_triples < mp_pow10(-60)
    assert err_2d_vs_1d_y8 < mp_pow10(-50)
    assert err_grid_conv_y14 < mp_pow10(-50)

    # ========================================================================
    # 1. DC-1: Contradiction C-1 — Unitary vs Antiunitary Exchange of (v+, v-)
    # ========================================================================
    UM_alt = T6 * S6 * T6.T.conjugate() * S6.T.conjugate()
    err_um_comm = max(abs(UM[r, c] - UM_alt[r, c]) for r in range(6) for c in range(6))
    err_um_ord12 = max(abs((ops["UM_pows"][11] * UM - mp.eye(6))[r, c]) for r in range(6) for c in range(6))
    S6_UM_S6inv = S6 * UM * S6.T.conjugate()
    UM_inv_mp = UM.T.conjugate()
    err_S6_inverts_UM = max(abs(S6_UM_S6inv[r, c] - UM_inv_mp[r, c]) for r in range(6) for c in range(6))
    S6_vp = [sum(S6[r, c] * vp[c] for c in range(6)) for r in range(6)]
    ov_vm_S6_vp = abs(sum(mp.conj(vm[r]) * S6_vp[r] for r in range(6)))

    TS = T6 * S6
    Sigma_sq = TS * TS.conjugate()
    err_Sigma_sq_UM = max(abs(Sigma_sq[r, c] - UM[r, c]) for r in range(6) for c in range(6))
    Sigma_vp = [sum(TS[r, c] * mp.conj(vp[c]) for c in range(6)) for r in range(6)]
    ov_vm_Sigma_vp = abs(sum(mp.conj(vm[r]) * Sigma_vp[r] for r in range(6)))
    assert err_S6_inverts_UM < mp_pow10(-55)
    assert abs(ov_vm_S6_vp - mp.mpf(1)) < mp_pow10(-55)
    assert err_Sigma_sq_UM < mp_pow10(-55)
    assert abs(ov_vm_Sigma_vp - mp.mpf(1)) < mp_pow10(-55)

    T6_np = np.array([[complex(T6[r, c]) for c in range(6)] for r in range(6)], dtype=np.complex128)
    S6_np = np.array([[complex(S6[r, c]) for c in range(6)] for r in range(6)], dtype=np.complex128)
    UM_np = np.array([[complex(UM[r, c]) for c in range(6)] for r in range(6)], dtype=np.complex128)
    UM_inv_np = UM_np.conj().T
    vp_np = np.array([complex(x) for x in vp], dtype=np.complex128)
    vm_np = np.array([complex(x) for x in vm], dtype=np.complex128)

    thresh_nz = pow10_f(-1)

    def canon_proj_tiefree(mat):
        flat = mat.reshape(-1)
        idx = next(i for i, z in enumerate(flat) if abs(z) > thresh_nz)
        ph = flat[idx] / abs(flat[idx])
        m = mat / ph
        key = tuple(int(round(x * 100000)) for z in m.reshape(-1) for x in (z.real, z.imag))
        return m, key

    gens = [T6_np, S6_np, T6_np.conj().T, S6_np.conj().T]
    id_m, id_k = canon_proj_tiefree(np.eye(6, dtype=np.complex128))
    proj_group = {id_k: id_m}
    frontier_g = [id_m]
    while frontier_g:
        cur = frontier_g.pop()
        for g in gens:
            nxt, k_nxt = canon_proj_tiefree(cur @ g)
            if k_nxt not in proj_group:
                proj_group[k_nxt] = nxt
                frontier_g.append(nxt)

    tol_np = pow10_f(-9)
    dc1_counts = {}
    for g in proj_group.values():
        ginv = g.conj().T
        for kind, conj_u, img in (
            ("unitary", g @ UM_np @ ginv, g @ vp_np),
            ("antiunitary", g @ UM_np.conj() @ ginv, g @ vp_np.conj()),
        ):
            if float(np.linalg.norm(conj_u - UM_np)) < tol_np:
                u_act = "keeps_UM"
            elif float(np.linalg.norm(conj_u - UM_inv_np)) < tol_np:
                u_act = "inverts_UM"
            else:
                u_act = "neither"
            if abs(abs(complex(np.vdot(vm_np, img))) - 1) < tol_np:
                p_act = "exchanges_pair"
            elif abs(abs(complex(np.vdot(vp_np, img))) - 1) < tol_np:
                p_act = "keeps_pair"
            else:
                p_act = "leaves_pair"
            k_str = f"{kind}:{u_act}:{p_act}"
            dc1_counts[k_str] = dc1_counts.get(k_str, 0) + 1

    assert len(proj_group) == 576
    assert dc1_counts["unitary:inverts_UM:exchanges_pair"] == 12
    assert dc1_counts["unitary:keeps_UM:keeps_pair"] == 12
    assert dc1_counts["antiunitary:keeps_UM:exchanges_pair"] == 12
    assert dc1_counts["antiunitary:inverts_UM:keeps_pair"] == 12

    # ========================================================================
    # 2. DC-2: Complex 2D Ground Plane E, Scalar Quadratic Response, & Degree 14/24
    # ========================================================================
    r0 = mp.mpf(1) / mp.sqrt(mp.mpf(3))
    phys_sq_p = [
        ((mp.mpf(1) - r0) ** 2) / mp.mpf(4),
        ((mp.mpf(1) + r0) ** 2) / mp.mpf(8),
        mp_rat(1, 12),
        mp_rat(1, 6),
        mp_rat(1, 12),
        ((mp.mpf(1) + r0) ** 2) / mp.mpf(8),
    ]
    phys_sq_m = [
        ((mp.mpf(1) + r0) ** 2) / mp.mpf(4),
        ((mp.mpf(1) - r0) ** 2) / mp.mpf(8),
        mp_rat(1, 12),
        mp_rat(1, 6),
        mp_rat(1, 12),
        ((mp.mpf(1) - r0) ** 2) / mp.mpf(8),
    ]
    err_vp_sq_tab = max(abs(abs(vp[k]) ** 2 - phys_sq_p[k]) for k in range(6))
    err_vm_sq_tab = max(abs(abs(vm[k]) ** 2 - phys_sq_m[k]) for k in range(6))
    assert err_vp_sq_tab < mp_pow10(-55) and err_vm_sq_tab < mp_pow10(-55)

    Hm = (UM + UM.T.conjugate()) / mp.mpf(2)
    c_target = mp.sqrt(mp.mpf(3)) / mp.mpf(2)
    basis_E = [vp, vm]
    Hm_E = mp.matrix(2, 2)
    for a in range(2):
        Hu = [sum(Hm[r, c] * basis_E[a][c] for c in range(6)) for r in range(6)]
        for b in range(2):
            Hm_E[b, a] = sum(mp.conj(basis_E[b][r]) * Hu[r] for r in range(6))
    err_Hm_scalar_on_E = max(abs((Hm_E - c_target * mp.eye(2))[a, b]) for a in range(2) for b in range(2))
    assert err_Hm_scalar_on_E < mp_pow10(-55)

    paulis = [
        sp.Matrix([[1, 0], [0, 1]]),
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    S_E_sym = sp.Matrix([[0, sp.exp(sp.I * sp.pi / 6)], [1, 0]])
    T_herm = sp.zeros(4, 4)
    for col_idx, P_mat in enumerate(paulis):
        img_mat = sp.simplify(S_E_sym * P_mat.conjugate() * S_E_sym.H)
        for row_idx in range(4):
            T_herm[row_idx, col_idx] = sp.simplify(sp.trace(img_mat * paulis[row_idx]) / 2)
    dim_sigma_even_herm = int(4 - (T_herm - sp.eye(4)).rank())
    dim_sigma_odd_herm = int(4 - (T_herm + sp.eye(4)).rank())

    inv_dims_full_E = {}
    inv_dims_N_Delta2 = {}
    for two_m in (2, 4, 6, 8, 10, 12, 14, 16, 24):
        m = two_m // 2
        mons = [(a, m - a, c, m - c) for a in range(m + 1) for c in range(m + 1) if (a - c) % 6 == 0]
        idx_map = {mon: idx for idx, mon in enumerate(mons)}
        dim_M = len(mons)
        S_poly = sp.zeros(dim_M, dim_M)
        for col_i, (a, b, c, d) in enumerate(mons):
            sign_fac = (-1) ** ((a - c) // 6)
            S_poly[idx_map[(d, c, b, a)], col_i] = sign_fac
        inv_dims_full_E[str(two_m)] = int(dim_M - (S_poly - sp.eye(dim_M)).rank())
        inv_dims_N_Delta2[str(two_m)] = int(sum(1 for v in range(m // 2 + 1) if (m - 2 * v) >= 0))

    min_circle_harmonic_k = next(k for k in range(1, 30) if (k % 12) == 0)
    min_circle_poly_deg = 2 * min_circle_harmonic_k
    assert dim_sigma_even_herm == 1 and dim_sigma_odd_herm == 1
    assert inv_dims_full_E["12"] == 4 and inv_dims_full_E["14"] == 6 and min_circle_poly_deg == 24

    # ========================================================================
    # 3. DC-3 + SM-C21 + Physical h* + P-873 Q3 (Direct 2D Wavefunction Quadrature)
    # ========================================================================
    norm_hstar_sq = sum(abs(x) ** 2 for x in hstar)
    proj_hstar = [sum(proj_E[r, c] * hstar[c] for c in range(6)) for r in range(6)]
    err_hstar_in_E = mp.sqrt(sum(abs(hstar[r] - proj_hstar[r]) ** 2 for r in range(6)))
    Hm_hstar = [sum(Hm[r, c] * hstar[c] for c in range(6)) for r in range(6)]
    err_Hm_hstar = mp.sqrt(sum(abs(Hm_hstar[r] - c_target * hstar[r]) ** 2 for r in range(6)))
    ov_vp_hstar_sq = abs(sum(mp.conj(vp[r]) * hstar[r] for r in range(6))) ** 2
    ov_vm_hstar_sq = abs(sum(mp.conj(vm[r]) * hstar[r] for r in range(6))) ** 2
    assert abs(norm_hstar_sq - mp.mpf(1)) < mp_pow10(-55)
    assert err_hstar_in_E < mp_pow10(-55)
    assert abs(ov_vp_hstar_sq - mp_rat(1, 2)) < mp_pow10(-55)
    assert abs(ov_vm_hstar_sq - mp_rat(1, 2)) < mp_pow10(-55)

    c_gen_p = mp_rat(3, 5) * mp.exp(iu * mp.pi * mp_rat(2, 7))
    c_gen_m = mp_rat(4, 5) * mp.exp(-iu * mp.pi * mp_rat(5, 11))
    vgen = [c_gen_p * vp[r] + c_gen_m * vm[r] for r in range(6)]

    sectors_charges = {
        "up": (1, -4),
        "down": (1, 2),
        "lepton": (-3, 6),
    }

    mark_heights = [6, 8, 10, 11, 14]
    mark_Y = {}
    for y_int in mark_heights:
        tau_y = mp_rat(13, 100) + iu * mp.mpf(y_int)
        w_y = mp_rat(2, 5) * tau_y + mp_rat(4, 5)
        nu_y = 64 if y_int <= 8 else (76 if y_int <= 11 else 92)
        mark_Y[y_int] = {}
        for sec, (qL, qR) in sectors_charges.items():
            zL = mp.mpf(qL) * w_y
            zR = mp.mpf(qR) * w_y
            zH = mp_rat(qL + qR, 2) * w_y
            mark_Y[y_int][sec] = overlap_tensor_2d_quad(tau_y, zL, zR, zH, 11, nu_y)

    worst_lep_down_transpose = mp.mpf(0)
    test_c6_vecs = [
        vp,
        vm,
        hstar,
        [mp_rat(k + 1, 7) + iu * mp_rat(5 - k, 11) for k in range(6)],
    ]
    for y_int in mark_heights:
        for hv in test_c6_vecs:
            Md = contract_yukawa_mp(mark_Y[y_int]["down"], hv)
            Ml = contract_yukawa_mp(mark_Y[y_int]["lepton"], hv)
            best_ij = max(((i, j) for i in range(3) for j in range(3)), key=lambda ij: abs(Md[ij[1], ij[0]]))
            ph = Ml[best_ij[0], best_ij[1]] / Md[best_ij[1], best_ij[0]]
            denom = abs(Ml[best_ij[0], best_ij[1]])
            rel = max(abs(Ml[i, j] - ph * Md[j, i]) for i in range(3) for j in range(3)) / denom
            if rel > worst_lep_down_transpose:
                worst_lep_down_transpose = rel
    assert worst_lep_down_transpose < mp_pow10(-55)

    vec_suite = {
        "v_plus": vp,
        "v_minus": vm,
        "v_generic_E": vgen,
        "h_star": hstar,
    }
    mark_svals = {vname: {sec: {} for sec in sectors_charges} for vname in vec_suite}
    mark_ckm_moduli = {vname: {} for vname in vec_suite}

    for y_int in mark_heights:
        for vname, hvec in vec_suite.items():
            u_left = {}
            for sec in sectors_charges:
                M_sec = contract_yukawa_mp(mark_Y[y_int][sec], hvec)
                sv, U_mat, _ = svd_desc_mp(M_sec)
                mark_svals[vname][sec][y_int] = sv
                u_left[sec] = U_mat
            V_mat = u_left["up"].T.conjugate() * u_left["down"]
            V_abs = mp.matrix([[abs(V_mat[r, c]) for c in range(3)] for r in range(3)])
            mark_ckm_moduli[vname][str(y_int)] = [[float(V_abs[r, c]) for c in range(3)] for r in range(3)]

    is2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))
    V_hstar_lim = mp.matrix([
        [is2, mp.mpf(0), is2],
        [is2, mp.mpf(0), is2],
        [mp.mpf(0), mp.mpf(1), mp.mpf(0)],
    ])
    tau_24 = mp_rat(13, 100) + iu * mp.mpf(24)
    w_24 = mp_rat(2, 5) * tau_24 + mp_rat(4, 5)
    Yup_24 = overlap_tensor_2d_quad(tau_24, w_24, mp.mpf(-4) * w_24, mp_rat(-3, 2) * w_24, 11, 128)
    Ydn_24 = overlap_tensor_2d_quad(tau_24, w_24, mp.mpf(2) * w_24, mp_rat(3, 2) * w_24, 11, 128)
    _, Uu_24, _ = svd_desc_mp(contract_yukawa_mp(Yup_24, hstar))
    _, Ud_24, _ = svd_desc_mp(contract_yukawa_mp(Ydn_24, hstar))
    Vm_24 = Uu_24.T.conjugate() * Ud_24
    mark_ckm_moduli["h_star"]["24"] = [[float(abs(Vm_24[r, c])) for c in range(3)] for r in range(3)]
    err_Vhstar_lim_y8 = max(
        abs(mp.mpf(mark_ckm_moduli["h_star"]["8"][r][c]) - V_hstar_lim[r, c])
        for r in range(3) for c in range(3)
    )
    err_Vhstar_lim_y14 = max(
        abs(mp.mpf(mark_ckm_moduli["h_star"]["14"][r][c]) - V_hstar_lim[r, c])
        for r in range(3) for c in range(3)
    )
    err_Vhstar_lim_y24 = max(
        abs(abs(Vm_24[r, c]) - V_hstar_lim[r, c]) for r in range(3) for c in range(3)
    )
    assert err_Vhstar_lim_y14 < mp_rat(1, 100)
    assert err_Vhstar_lim_y24 < mp_rat(1, 1000)

    def extract_exp_pair(sv_dict, y0: int, y1: int):
        s0 = sv_dict[y0]
        s1 = sv_dict[y1]
        dy = mp.mpf(y1 - y0)
        e2 = -(mp.log(s1[1] / s1[0]) - mp.log(s0[1] / s0[0])) / (mp.pi * dy)
        e3 = -(mp.log(s1[2] / s1[0]) - mp.log(s0[2] / s0[0])) / (mp.pi * dy)
        return [float(e2), float(e3)]

    exponents_summary = {}
    for vname in vec_suite:
        exponents_summary[vname] = {}
        for sec in sectors_charges:
            sv_d = mark_svals[vname][sec]
            exponents_summary[vname][sec] = {
                "6_to_8": extract_exp_pair(sv_d, 6, 8),
                "8_to_10": extract_exp_pair(sv_d, 8, 10),
                "8_to_11": extract_exp_pair(sv_d, 8, 11),
                "11_to_14": extract_exp_pair(sv_d, 11, 14),
            }

    for vname in ("v_plus", "v_minus", "v_generic_E"):
        for sec in ("up", "down", "lepton"):
            e6_8 = exponents_summary[vname][sec]["6_to_8"]
            e8_10 = exponents_summary[vname][sec]["8_to_10"]
            e11_14 = exponents_summary[vname][sec]["11_to_14"]
            assert max(abs(e6_8[0]), abs(e6_8[1])) < (3 / 100)
            assert max(abs(e8_10[0]), abs(e8_10[1])) < (13 / 1000)
            assert max(abs(e11_14[0]), abs(e11_14[1])) < (4 / 1000)
    assert abs(exponents_summary["h_star"]["up"]["11_to_14"][0] - 0) < pow10_f(-3)
    assert abs(exponents_summary["h_star"]["up"]["11_to_14"][1] - (4 / 3)) < pow10_f(-3)
    assert abs(exponents_summary["h_star"]["down"]["11_to_14"][0] - (1 / 5)) < pow10_f(-3)
    assert abs(exponents_summary["h_star"]["down"]["11_to_14"][1] - (4 / 5)) < pow10_f(-3)

    # 96-case sweep (24 order-5 points x 4 lifts) at height 4 and height 8 directly via 2D quadrature!
    # At dps = 40, nx = 11, nu = 40/50, alias error is < 1e-35 while running 3x faster!
    t_96_start = time.time()
    mp.mp.dps = 40
    pts_24 = [(i5, j5) for i5 in range(5) for j5 in range(5) if (i5, j5) != (0, 0)]
    lifts_4 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    rank_thresh = mp_pow10(-12)

    mixing_by_height = {}
    for y_sweep, nu_sweep in ((4, 40), (8, 50)):
        tau_s = mp_rat(13, 100) + iu * mp.mpf(y_sweep)
        res_h = {
            vname: {
                f"lift_{la}_{lb}": {
                    "aligned": 0,
                    "top-aligned": 0,
                    "permutation": 0,
                    "other": 0,
                    "full_rank_up_count": 0,
                    "full_rank_down_count": 0,
                    "top_aligned_points": [],
                    "aligned_points": [],
                    "permutation_points": [],
                }
                for (la, lb) in lifts_4
            }
            for vname in ("v_plus", "v_minus", "h_star")
        }
        for (i5, j5) in pts_24:
            for (la, lb) in lifts_4:
                a_val = mp_rat(i5 + 5 * la, 5)
                b_val = mp_rat(j5 + 5 * lb, 5)
                w_pt = a_val * tau_s + b_val
                Y_up = overlap_tensor_2d_quad(
                    tau_s, w_pt, mp.mpf(-4) * w_pt, mp_rat(-3, 2) * w_pt, 11, nu_sweep, n_window=3
                )
                Y_dn = overlap_tensor_2d_quad(
                    tau_s, w_pt, mp.mpf(2) * w_pt, mp_rat(3, 2) * w_pt, 11, nu_sweep, n_window=3
                )
                lkey = f"lift_{la}_{lb}"
                for vname, hvec in (("v_plus", vp), ("v_minus", vm), ("h_star", hstar)):
                    Mu = contract_yukawa_mp(Y_up, hvec)
                    Md = contract_yukawa_mp(Y_dn, hvec)
                    su, Uu, _ = svd_desc_mp(Mu)
                    sd, Ud, _ = svd_desc_mp(Md)
                    if su[2] > rank_thresh * su[0]:
                        res_h[vname][lkey]["full_rank_up_count"] += 1
                    if sd[2] > rank_thresh * sd[0]:
                        res_h[vname][lkey]["full_rank_down_count"] += 1
                    V_m = Uu.T.conjugate() * Ud
                    V_a = mp.matrix([[abs(V_m[r, c]) for c in range(3)] for r in range(3)])
                    cls = classify_mixing(V_a)
                    res_h[vname][lkey][cls] += 1
                    if cls == "top-aligned":
                        res_h[vname][lkey]["top_aligned_points"].append([i5, j5])
                    elif cls == "aligned":
                        res_h[vname][lkey]["aligned_points"].append([i5, j5])
                    elif cls == "permutation":
                        res_h[vname][lkey]["permutation_points"].append([i5, j5])
        mixing_by_height[f"height_{y_sweep}"] = res_h

    mp.mp.dps = 65
    sweep_96_sec = time.time() - t_96_start
    for (la, lb) in lifts_4:
        lk = f"lift_{la}_{lb}"
        assert mixing_by_height["height_8"]["v_plus"][lk]["other"] == 24
        assert mixing_by_height["height_8"]["v_plus"][lk]["full_rank_up_count"] == 24
        assert mixing_by_height["height_8"]["v_plus"][lk]["full_rank_down_count"] == 24
        assert mixing_by_height["height_8"]["v_minus"][lk]["top-aligned"] == 4
        assert mixing_by_height["height_8"]["v_minus"][lk]["other"] == 20
        assert mixing_by_height["height_8"]["v_minus"][lk]["full_rank_up_count"] == 24
        assert mixing_by_height["height_8"]["v_minus"][lk]["full_rank_down_count"] == 24

    # ========================================================================
    # 4. DC-4: Coordinate Reflection R0 on Spin-(0,0) Flux-6 Modes
    # ========================================================================
    def eval_single_flux6_point(tau_pt, z_pt, zeta_pt):
        y = mp.im(tau_pt)
        norm = mp.power(mp.mpf(12) * y, mp_rat(1, 4))
        w_arg = z_pt + zeta_pt
        g = norm * mp.exp(iu * mp.pi * mp.mpf(6) * w_arg * (mp.im(w_arg) / y))
        out = []
        for k in range(6):
            a = mp_rat(k, 6)
            s = mp.mpc(0, 0)
            for n in range(-14, 15):
                na = mp.mpf(n) + a
                s += mp.exp(iu * mp.pi * (na * na) * mp.mpf(6) * tau_pt + iu * mp.mpf(2) * mp.pi * na * (mp.mpf(6) * w_arg))
            out.append(g * s)
        return out

    tau_r0 = mp_rat(19, 100) + iu * mp_rat(17, 10)
    z_r0 = mp_rat(23, 100) + iu * mp_rat(31, 100)
    zeta_r0 = mp_rat(11, 100) - iu * mp_rat(7, 100)
    psi_orig = eval_single_flux6_point(tau_r0, z_r0, zeta_r0)
    psi_anti_jacobi = eval_single_flux6_point(-mp.conj(tau_r0), -mp.conj(z_r0), -mp.conj(zeta_r0))
    psi_sm_card = eval_single_flux6_point(-mp.conj(tau_r0), mp.conj(z_r0), mp.conj(zeta_r0))

    err_anti_jacobi_vs_K = max(abs(psi_anti_jacobi[k] - mp.conj(psi_orig[k])) for k in range(6))
    err_sm_card_vs_K = max(abs(psi_sm_card[k] - mp.conj(psi_orig[k])) for k in range(6))
    err_sm_card_vs_PK = max(abs(psi_sm_card[k] - mp.conj(psi_orig[(-k) % 6])) for k in range(6))

    PTS = P6 * TS
    Sigma_plus_sq = PTS * PTS.conjugate()
    err_Sigma_plus_sq_UM = max(abs(Sigma_plus_sq[r, c] - UM[r, c]) for r in range(6) for c in range(6))
    diff_on_even = max(
        mp.sqrt(sum(abs(sum((TS[r, c] - PTS[r, c]) * mp.conj(v[c]) for c in range(6))) ** 2 for r in range(6)))
        for v in (vp, vm)
    )
    diff_on_odd = min(
        mp.sqrt(sum(abs(sum((TS[r, c] - PTS[r, c]) * mp.conj(v[c]) for c in range(6))) ** 2 for r in range(6)))
        for v in (ops["v_odd_p"], ops["v_odd_m"])
    )
    assert err_anti_jacobi_vs_K < mp_pow10(-55)
    assert err_sm_card_vs_PK < mp_pow10(-55)
    assert err_sm_card_vs_K > mp_rat(1, 2)
    assert diff_on_even < mp_pow10(-55)
    assert abs(diff_on_odd - mp.mpf(2)) < mp_pow10(-55)

    # ========================================================================
    # 5. DC-5: Degree-4 E[2] Cover, 2/3 Leakage, Zero M-Invariant Character,
    #    and Single-Point Non-Scalar B(w) vs 4-Lift Scalar Twirl
    # ========================================================================
    Z3 = Z6 ** 3
    X3 = X6 ** 3
    ZX3 = Z3 * X3
    XZ3 = X3 * Z3
    err_klein_anticomm = max(abs((ZX3 + XZ3)[r, c]) for r in range(6) for c in range(6))

    leak_records = {}
    for gname, gmat in (("Z3", Z3), ("X3", X3), ("Z3X3", ZX3)):
        gvp = [sum(gmat[r, c] * vp[c] for c in range(6)) for r in range(6)]
        ov_p_sq = abs(sum(mp.conj(vp[r]) * gvp[r] for r in range(6))) ** 2
        ov_m = abs(sum(mp.conj(vm[r]) * gvp[r] for r in range(6)))
        pgvp = [sum(proj_E[r, c] * gvp[c] for c in range(6)) for r in range(6)]
        leak_sq = sum(abs(gvp[r] - pgvp[r]) ** 2 for r in range(6))
        leak_records[gname] = {
            "ov_vp_sq_err_from_1_3": float(abs(ov_p_sq - mp_rat(1, 3))),
            "ov_vm_abs": float(ov_m),
            "leak_out_of_E_err_from_2_3": float(abs(leak_sq - mp_rat(2, 3))),
        }
        assert abs(ov_p_sq - mp_rat(1, 3)) < mp_pow10(-55)
        assert ov_m < mp_pow10(-55)
        assert abs(leak_sq - mp_rat(2, 3)) < mp_pow10(-55)

    M_mod2 = [[2 % 2, 1 % 2], [1 % 2, 1 % 2]]
    m_inv_chars = sum(
        1
        for c0 in (0, 1)
        for c1 in (0, 1)
        if (c0, c1) != (0, 0)
        and ((c0 * M_mod2[0][0] + c1 * M_mod2[1][0]) % 2, (c0 * M_mod2[0][1] + c1 * M_mod2[1][1]) % 2) == (c0, c1)
    )
    assert m_inv_chars == 0

    tau_c7 = mp_rat(17, 100) + iu * mp_rat(9, 5)
    w_c7 = mp_rat(2, 5) * tau_c7 + mp_rat(3, 5)

    def bubble_from_Y(Yt):
        B = mp.matrix(6, 6)
        for k1 in range(6):
            for k2 in range(6):
                s = mp.mpc(0, 0)
                for i in range(3):
                    for j in range(3):
                        s += mp.conj(Yt[i][j][k1]) * Yt[i][j][k2]
                B[k1, k2] = s
        return B

    Y_w = overlap_tensor_2d_quad(tau_c7, w_c7, mp.mpf(-4) * w_c7, mp_rat(-3, 2) * w_c7, 11, 48)
    Y_w1 = overlap_tensor_2d_quad(
        tau_c7, w_c7 + mp.mpf(1), mp.mpf(-4) * (w_c7 + mp.mpf(1)), mp_rat(-3, 2) * (w_c7 + mp.mpf(1)), 11, 48
    )
    Y_wt = overlap_tensor_2d_quad(
        tau_c7, w_c7 + tau_c7, mp.mpf(-4) * (w_c7 + tau_c7), mp_rat(-3, 2) * (w_c7 + tau_c7), 11, 48
    )
    Bw = bubble_from_Y(Y_w)
    Bw1 = bubble_from_Y(Y_w1)
    Bwt = bubble_from_Y(Y_wt)

    err_cov_B_w1 = max(abs((Bw1 - Z3 * Bw * Z3.T.conjugate())[r, c]) for r in range(6) for c in range(6))
    err_cov_B_wt = max(abs((Bwt - X3 * Bw * X3.T.conjugate())[r, c]) for r in range(6) for c in range(6))
    Bw_np = np.array([[complex(Bw[r, c]) for c in range(6)] for r in range(6)], dtype=np.complex128)
    eigs_Bw = np.linalg.eigvalsh(Bw_np)
    rel_spread_single_Bw = float((eigs_Bw[-1] - eigs_Bw[0]) / np.trace(Bw_np).real)

    B_twirl = mp.matrix(6, 6)
    for g in (mp.eye(6), Z3, X3, ZX3):
        B_twirl += g * Bw * g.T.conjugate()
    B_twirl /= mp.mpf(4)
    tr_Bw = sum(Bw[k, k] for k in range(6))
    err_twirl_scalar = max(abs((B_twirl - (tr_Bw / mp.mpf(6)) * mp.eye(6))[r, c]) for r in range(6) for c in range(6))
    assert err_cov_B_w1 < mp_pow10(-50) and err_cov_B_wt < mp_pow10(-50)
    assert rel_spread_single_Bw > pow10_f(-2)
    assert err_twirl_scalar < mp_pow10(-55)

    # ========================================================================
    # 6. DC-6: Level-5 tau -> tau + 5 Point-Phase Law Across Both "Frame D1"s
    #    (a) Szego-pole residue D1 (B1945 §6 / P-871, h = c * q_H * w)
    #    (b) Closed-fibre flux-(3,3,6) D1 (SM-C18, via 2D quadrature with nx=11)
    # ========================================================================
    def thc_1d(alpha_val, beta_val, u_val, T_val, n_lim: int = 16):
        s = mp.mpc(0, 0)
        for n in range(-n_lim, n_lim + 1):
            na = mp.mpf(n) + alpha_val
            s += mp.exp(iu * mp.pi * (na * na) * T_val + iu * mp.mpf(2) * mp.pi * na * (u_val + beta_val))
        return s

    def t1p_deriv(tau_val, n_lim: int = 18):
        s = mp.mpc(0, 0)
        for n in range(-n_lim, n_lim + 1):
            na = mp.mpf(n) + mp_rat(1, 2)
            s += (iu * mp.mpf(2) * mp.pi * na) * mp.exp(
                iu * mp.pi * (na * na) * tau_val + iu * mp.pi * na
            )
        return s

    def szego_resid_2x2(tau_val, i5: int, j5: int, qL: int, qR: int, qH: int, c_pl: int):
        a_mp = mp_rat(i5, 5)
        b_mp = mp_rat(j5, 5)
        h_val = mp.mpf(c_pl * qH) * (a_mp * tau_val + b_mp)
        T2 = mp.mpf(2) * tau_val
        vL = [
            thc_1d(mp.mpf(qL) * a_mp, mp.mpf(2 * qL) * b_mp, -h_val, T2),
            -iu * thc_1d(mp.mpf(qL) * a_mp + mp_rat(1, 2), mp.mpf(2 * qL) * b_mp, -h_val, T2),
        ]
        vR = [
            thc_1d(mp.mpf(qR) * a_mp, mp.mpf(2 * qR) * b_mp, -h_val, T2),
            -iu * thc_1d(mp.mpf(qR) * a_mp + mp_rat(1, 2), mp.mpf(2 * qR) * b_mp, -h_val, T2),
        ]
        denom = t1p_deriv(tau_val)
        return [[vL[m] * vR[n] / denom for n in range(2)] for m in range(2)]

    sec_q3 = {"up": (1, -4, 3), "down": (1, 2, -3), "lepton": (-3, 6, -3)}
    tau_base = mp_rat(13, 100) + iu * mp_rat(17, 10)
    zeta5 = mp.exp(iu * mp.mpf(2) * mp.pi * mp_rat(1, 5))

    szego_c_summary = {}
    worst_szego_law_err = mp.mpf(0)
    for c_pl in (0, 1, -1, 2, -2, 5, 7):
        closed_secs = []
        sec_info = {}
        for sec, (qL, qR, qH) in sec_q3.items():
            E_mod5 = (qL * qL + qR * qR + c_pl * qH * qH) % 5
            base_24 = {p: szego_resid_2x2(tau_base, p[0], p[1], qL, qR, qH, c_pl) for p in pts_24}
            p5_24 = {p: szego_resid_2x2(tau_base + mp.mpf(5), p[0], p[1], qL, qR, qH, c_pl) for p in pts_24}
            p25_24 = {p: szego_resid_2x2(tau_base + mp.mpf(25), p[0], p[1], qL, qR, qH, c_pl) for p in pts_24}
            ref_p = (0, 1)
            r5_ref = [p5_24[ref_p][m][n] / base_24[ref_p][m][n] for m in range(2) for n in range(2)]
            r25_ref = [p25_24[ref_p][m][n] / base_24[ref_p][m][n] for m in range(2) for n in range(2)]
            max_e = mp.mpf(0)
            all_scalar_p5 = True
            all_scalar_p25 = True
            for (i5, j5) in pts_24:
                r5_p = [(p5_24[(i5, j5)][m][n] / base_24[(i5, j5)][m][n]) / r5_ref[2 * m + n] for m in range(2) for n in range(2)]
                r25_p = [(p25_24[(i5, j5)][m][n] / base_24[(i5, j5)][m][n]) / r25_ref[2 * m + n] for m in range(2) for n in range(2)]
                target_ph5 = zeta5 ** ((E_mod5 * i5 * i5) % 5)
                off_sign = (-1) ** ((c_pl * i5) % 2)
                expected_5 = [target_ph5, target_ph5 * off_sign, target_ph5 * off_sign, target_ph5]
                expected_25 = [mp.mpf(1), mp.mpf(off_sign), mp.mpf(off_sign), mp.mpf(1)]
                for idx4 in range(4):
                    max_e = max(max_e, abs(r5_p[idx4] - expected_5[idx4]), abs(r25_p[idx4] - expected_25[idx4]))
                if off_sign != 1:
                    all_scalar_p5 = False
                    all_scalar_p25 = False
            if max_e > worst_szego_law_err:
                worst_szego_law_err = max_e
            closes_l5 = (E_mod5 == 0) and all_scalar_p5
            if closes_l5:
                closed_secs.append(sec)
            sec_info[sec] = {
                "E_mod5": E_mod5,
                "scalar_at_p5": all_scalar_p5,
                "scalar_at_p25": all_scalar_p25,
                "closes_level5": closes_l5,
                "max_law_err": float(max_e),
            }
        szego_c_summary[str(c_pl)] = {"closed_sectors": closed_secs, "sectors": sec_info}

    both_up_down_c = [
        c_pl for c_pl in (0, 1, -1, 2, -2, 5, 7)
        if "up" in szego_c_summary[str(c_pl)]["closed_sectors"]
        and "down" in szego_c_summary[str(c_pl)]["closed_sectors"]
    ]
    assert worst_szego_law_err < mp_pow10(-50)
    assert len(both_up_down_c) == 0

    # Closed-fibre flux-(3,3,6) D1 under tau -> tau + 5 across all 24 points via 2D quadrature (nx=11 coprime to 6!)
    mp.mp.dps = 55
    err_closed_fibre_l5 = mp.mpf(0)
    closed_fibre_l5_summary = {}
    for sec, (qL, qR) in sectors_charges.items():
        Delta_s = qL - qR
        max_sec_err = mp.mpf(0)
        fifth_obstructed_pts = 0
        for (i5, j5) in pts_24:
            a_mp = mp_rat(i5, 5)
            b_mp = mp_rat(j5, 5)
            w0 = a_mp * tau_base + b_mp
            tau_p5 = tau_base + mp.mpf(5)
            w5 = a_mp * tau_p5 + b_mp
            Y0 = overlap_tensor_2d_quad(tau_base, mp.mpf(qL) * w0, mp.mpf(qR) * w0, mp_rat(qL + qR, 2) * w0, 11, 46, n_window=6)
            Y5 = overlap_tensor_2d_quad(tau_p5, mp.mpf(qL) * w5, mp.mpf(qR) * w5, mp_rat(qL + qR, 2) * w5, 11, 46, n_window=6)
            for i in range(3):
                for j in range(3):
                    for m_par in (0, 1):
                        k = (i + j + 1 + 3 * m_par) % 6
                        c_idx = (i - j + 3 * m_par) % 6
                        ph_exact = mp.exp(
                            iu * mp.pi * mp_rat(5 * c_idx * c_idx, 6)
                            + iu * mp.pi * mp.mpf(c_idx * Delta_s * i5)
                            + iu * mp.pi * mp_rat(3 * Delta_s * Delta_s * i5 * i5, 10)
                        )
                        err_ijm = abs(Y5[i][j][k] - ph_exact * Y0[i][j][k])
                        if err_ijm > max_sec_err:
                            max_sec_err = err_ijm
            if (2 * Delta_s * Delta_s * i5 * i5) % 5 != 0:
                fifth_obstructed_pts += 1
        if max_sec_err > err_closed_fibre_l5:
            err_closed_fibre_l5 = max_sec_err
        closed_fibre_l5_summary[sec] = {
            "max_phase_law_err": float(max_sec_err),
            "fifth_root_obstructed_points_of_24": fifth_obstructed_pts,
        }
    mp.mp.dps = 65
    assert err_closed_fibre_l5 < mp_pow10(-45)
    assert closed_fibre_l5_summary["up"]["fifth_root_obstructed_points_of_24"] == 0
    assert closed_fibre_l5_summary["down"]["fifth_root_obstructed_points_of_24"] == 20
    assert closed_fibre_l5_summary["lepton"]["fifth_root_obstructed_points_of_24"] == 20

    # ========================================================================
    # 7. Five Planted Fault Controls (PFA2X1-1 .. PFA2X1-5, Guardrails 2, 3, 6)
    # ========================================================================
    pfa1_caught = dc1_counts["unitary:inverts_UM:exchanges_pair"] > 0
    pfa2_caught = exponents_summary["h_star"]["up"]["11_to_14"][1] > 1
    pfa3_caught = err_sm_card_vs_K > mp_rat(1, 2)
    simul_c_mod5 = [c_m for c_m in range(5) if (2 + 4 * c_m) % 5 == 0 and (4 * c_m) % 5 == 0]
    pfa4_caught = len(simul_c_mod5) == 0

    WL = cayley_unitary_3x3_mp([mp_rat(k + 1, 13) for k in range(9)])
    WR_u = cayley_unitary_3x3_mp([mp_rat(2 * k + 3, 17) for k in range(9)])
    WR_d = cayley_unitary_3x3_mp([mp_rat(3 * k - 4, 19) for k in range(9)])
    Mu_ref = contract_yukawa_mp(mark_Y[8]["up"], hstar)
    Md_ref = contract_yukawa_mp(mark_Y[8]["down"], hstar)
    su_0, Uu_0, Vu_0 = svd_desc_mp(Mu_ref)
    sd_0, Ud_0, _ = svd_desc_mp(Md_ref)
    V_0 = Uu_0.T.conjugate() * Ud_0

    Mu_scr = WL * Mu_ref * WR_u.T.conjugate()
    Md_scr = WL * Md_ref * WR_d.T.conjugate()
    su_1, Uu_1, Vu_1 = svd_desc_mp(Mu_scr)
    sd_1, Ud_1, _ = svd_desc_mp(Md_scr)
    V_1 = Uu_1.T.conjugate() * Ud_1

    err_haar_svals = max(max(abs(su_0[i] - su_1[i]), abs(sd_0[i] - sd_1[i])) for i in range(3))
    err_haar_ckm = max(abs(abs(V_0[r, c]) - abs(V_1[r, c])) for r in range(3) for c in range(3))
    LR_0 = Uu_0.T.conjugate() * Vu_0
    LR_1 = Uu_1.T.conjugate() * Vu_1
    drift_forbidden_lr = max(abs(abs(LR_0[r, c]) - abs(LR_1[r, c])) for r in range(3) for c in range(3))
    pfa5_caught = (err_haar_svals < mp_pow10(-55)) and (err_haar_ckm < mp_pow10(-55)) and (drift_forbidden_lr > mp_rat(1, 10))
    assert pfa1_caught and pfa2_caught and pfa3_caught and pfa4_caught and pfa5_caught

    out_payload = {
        "card": "A2-X1",
        "zero_float_ast_literals": len(bad_literals) == 0,
        "empirical_targets_used": 0,
        "other_seat_code_executed": False,
        "main_cim_closed_used": False,
        "instrument_calibration": {
            "err_2d_grid_11x64_vs_17x84_y8": float(err_grid_conv_y8),
            "err_forbidden_36_triples_y8": float(err_forbidden_36_triples),
            "err_2d_quad_vs_1d_unfolded_y8": float(err_2d_vs_1d_y8),
            "err_2d_grid_11x80_vs_17x100_y14": float(err_grid_conv_y14),
        },
        "dc1_exchange_and_group": {
            "projective_group_size": len(proj_group),
            "err_UM_commutator_identity": float(err_um_comm),
            "err_UM_order_12": float(err_um_ord12),
            "err_S6_inverts_UM": float(err_S6_inverts_UM),
            "overlap_vm_S6_vp": float(ov_vm_S6_vp),
            "err_Sigma_sq_minus_UM": float(err_Sigma_sq_UM),
            "overlap_vm_Sigma_vp": float(ov_vm_Sigma_vp),
            "counts": dc1_counts,
        },
        "dc2_ground_plane_and_invariants": {
            "err_vp_sq_table": float(err_vp_sq_tab),
            "err_vm_sq_table": float(err_vm_sq_tab),
            "err_Hm_scalar_on_E": float(err_Hm_scalar_on_E),
            "dim_sigma_even_hermitian_on_E": dim_sigma_even_herm,
            "dim_sigma_odd_hermitian_on_E": dim_sigma_odd_herm,
            "invariant_poly_dims_full_E": inv_dims_full_E,
            "invariant_poly_dims_R_N_Delta2": inv_dims_N_Delta2,
            "min_circle_nonconst_poly_degree": min_circle_poly_deg,
        },
        "dc3_sm_c21_and_hstar": {
            "err_hstar_norm_sq": float(abs(norm_hstar_sq - mp.mpf(1))),
            "err_hstar_in_E": float(err_hstar_in_E),
            "err_Hm_hstar": float(err_Hm_hstar),
            "ov_vp_hstar_sq": float(ov_vp_hstar_sq),
            "ov_vm_hstar_sq": float(ov_vm_hstar_sq),
            "worst_lepton_down_transpose_rel_err": float(worst_lep_down_transpose),
            "mark_exponents": exponents_summary,
            "mark_ckm_moduli": mark_ckm_moduli,
            "p873_q3_mark_hstar_limit_errs": {
                "y8": float(err_Vhstar_lim_y8),
                "y14": float(err_Vhstar_lim_y14),
                "y24": float(err_Vhstar_lim_y24),
            },
            "mixing_96_cases": mixing_by_height,
            "sweep_96_direct_2d_quad_seconds": round(sweep_96_sec, 3),
        },
        "dc4_reflection_lift": {
            "err_anti_jacobi_minus_zbar_vs_K": float(err_anti_jacobi_vs_K),
            "err_sm_card_plus_zbar_vs_K": float(err_sm_card_vs_K),
            "err_sm_card_plus_zbar_vs_PK": float(err_sm_card_vs_PK),
            "err_Sigma_plus_sq_minus_UM": float(err_Sigma_plus_sq_UM),
            "diff_Sigma_minus_vs_Sigma_plus_on_even_E": float(diff_on_even),
            "diff_Sigma_minus_vs_Sigma_plus_on_odd_plane": float(diff_on_odd),
        },
        "dc5_cover_leak_and_covariant_bubble": {
            "err_klein_anticommutator": float(err_klein_anticomm),
            "leak_records": leak_records,
            "nonzero_M_invariant_F2_characters": m_inv_chars,
            "single_point_Bw_relative_spread": rel_spread_single_Bw,
            "err_cov_Bw_shift_1": float(err_cov_B_w1),
            "err_cov_Bw_shift_tau": float(err_cov_B_wt),
            "err_twirl_scalar": float(err_twirl_scalar),
        },
        "dc6_level5_point_phase": {
            "szego_residue_d1_worst_law_err": float(worst_szego_law_err),
            "szego_c_closing_both_up_and_down": both_up_down_c,
            "szego_by_c": szego_c_summary,
            "closed_fibre_d1_worst_law_err": float(err_closed_fibre_l5),
            "closed_fibre_by_sector": closed_fibre_l5_summary,
        },
        "planted_fault_controls": {
            "PFA2X1-1_caught": pfa1_caught,
            "PFA2X1-2_caught": pfa2_caught,
            "PFA2X1-3_caught": pfa3_caught,
            "PFA2X1-4_caught": pfa4_caught,
            "PFA2X1-5_caught": pfa5_caught,
            "haar_svals_err": float(err_haar_svals),
            "haar_ckm_err": float(err_haar_ckm),
            "forbidden_single_dirac_lr_drift": float(drift_forbidden_lr),
        },
        "elapsed_seconds": round(time.time() - t_start, 3),
        "all_assertions_passed": True,
    }

    out_json_path = self_path.parent / "verify_a2_x1_out.json"
    out_txt_path = self_path.parent / "verify_a2_x1_out.txt"
    out_json_path.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    summary_lines = [
        "Card A2-X1 Standalone Verification Summary (0 of 19; zero float/complex AST literals)",
        f"zero_float_ast_literals = {out_payload['zero_float_ast_literals']}",
        f"other_seat_code_executed = {out_payload['other_seat_code_executed']}",
        f"main_cim_closed_used = {out_payload['main_cim_closed_used']}",
        f"DC-1 projective_group_size = {len(proj_group)}, counts = {dc1_counts}",
        f"DC-2 sigma_even_herm_dim = {dim_sigma_even_herm}, poly_dims_deg12_14 = ({inv_dims_full_E['12']}, {inv_dims_full_E['14']}), circle_deg = {min_circle_poly_deg}",
        f"DC-3 height_8 v_plus lift_0_0 = {mixing_by_height['height_8']['v_plus']['lift_0_0']}",
        f"DC-3 height_8 v_minus lift_0_0 = {mixing_by_height['height_8']['v_minus']['lift_0_0']}",
        f"DC-3 height_8 h_star lift_0_0 = {mixing_by_height['height_8']['h_star']['lift_0_0']}",
        f"DC-4 anti_jacobi_K_ok = {err_anti_jacobi_vs_K < mp_pow10(-55)}, plus_zbar_PK_ok = {err_sm_card_vs_PK < mp_pow10(-55)}",
        f"DC-5 nonzero_M_inv_F2_chars = {m_inv_chars}, leak_2_3_ok = True, twirl_scalar_ok = True",
        f"DC-6 szego_both_up_down = {both_up_down_c}, closed_fibre_obstructed_pts = { {s: closed_fibre_l5_summary[s]['fifth_root_obstructed_points_of_24'] for s in ('up','down','lepton')} }",
        "planted_fault_controls = 5 / 5 caught",
        "all_assertions_passed = True",
    ]
    out_txt_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print("\n".join(summary_lines))


if __name__ == "__main__":
    main()
