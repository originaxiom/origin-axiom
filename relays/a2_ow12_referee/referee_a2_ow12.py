r"""
Independent Cold-Room Zero-Trust Referee for Card AGY-002_A2-OW12 (and Erratum 1).

Strong CP (bar_theta_Q & 7D CS Axion E / N = 8 / 3), Zero-Parameter eps_nu = 1
Neutrino Seesaw PMNS, Fukugita-Yanagida Leptogenesis epsilon_1, & 7D (T_{3R}, B - L)
Bulk Inter-Sector Audit (0 of 19):

  - Disjoint Operator Engine (55-dps GL6 + mpmath.jtheta):
      * 3-stage implicit Gauss-Legendre RK6 (order-20 Richardson extrapolated)
        Fuchsian L_2(tau) solver, independently verified against the SL(2, Z)
        S-transformation law and exact Z_2 mirror symmetry L_2(tau_*^+) == L_2(tau_*^-).
      * Branch-cut-free mpmath.jtheta E[5] + E[6] Regime-4b open-weave operators
        for (Y_u, Y_d, Y_e, Y_nu, M_R^{(00)}) at tau_*^+ = 8 (2 + i) / 5,
        mirror tau_*^- = 8 (-2 + i) / 5, m = 24, and CP-conserving tau_CP = 8 i / sqrt(5).
  - Disjoint Linear Algebra (45-dps mp.svd_c + Householder QR, ZERO mp.eigh):
      * Autonne-Takagi factorization U_R^T M U_R = diag(M_1, M_2, M_3 >= 0) via
        mp.svd_c and unitary-symmetric polar phase extraction (plus elementary
        real Jacobi fallback for degenerate blocks; zero mp.eigh calls).
      * Complex Ginibre + Householder-reflection QR Mezzadri Haar U(3) and SU(3)
        samplers.
  - OW12-A: bar_theta_Q = arg det(Y_u Y_d) at tau_CP, E[5] alone, E[6] alone,
            E[5] + E[6] at m_L = 8 and m = 24, exact mirror cancellation at tau_*^-,
            10-trial Haar SU(3)^3 scrambling, 6-perm positive scaling invariance,
            and exact sympy.Rational Spin(10) 7D CS axion E / N = 8 / 3.
  - OW12-B: Y_nu (w_L = -3, w_R = 0, eps_nu = 1) and complex symmetric M_R^{(00)},
            Autonne-Takagi spectrum & residual, all 6 perms PMNS + J_PMNS + dm21/dm31
            for both M_R^{(1)} = I_3 and M_R^{(00)}, exact 1-loop Fukugita-Yanagida
            epsilon_1^{norm}(tau_*^+) and mirror flip at tau_*^-, and 10-trial Haar
            U(3)_L x U(3)_e x U(3)_nu scrambling (Y_nu -> U_L Y_nu U_nu^dag,
            M_R -> U_nu^* M_R U_nu^dag).
  - OW12-C: Exact sympy.Rational 6 Y = 6 T_{3R} + 3 (B - L) across all 6 Spin(10)
            16_+ species, T_{3R} == 0 exclusively on LH doublets, exact uniform LH
            doublet scaling invariance across all 6 perms (y_tau / y_b shift phi^(-4)),
            and transparent tan(beta) = 1 inter-sector Yukawa ratios on all 6 perms.
  - OW12-D: 4 / 4 Planted-Fault Self-Checks (PF-OW12-1..4).

Hygiene:
  - 0 of 19 empirical inputs.
  - 0 float or complex AST literals.
  - 0 frontier/ or producer verify_a2_ow12* imports.
  - 0 hardcoded boolean dict-literal proof flags.
"""

import ast
import hashlib
import itertools
import json
import os
import random
import time
from fractions import Fraction

import mpmath as mp
import sympy as sp


# =============================================================================
# SECTION 0: CUSTODY & AST HYGIENE SELF-AUDIT
# =============================================================================

def audit_script_hygiene(script_path):
    with open(script_path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src, filename=script_path)
    bad_literals = []
    bad_imports = []
    dict_bool_literals = []
    eigh_calls = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad_literals.append((getattr(node, "lineno", -1), repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if (
                    "frontier" in alias.name
                    or "a2_ow12" in alias.name
                    or "verify_a2" in alias.name
                ):
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "frontier" in mod or "a2_ow12" in mod or "verify_a2" in mod:
                bad_imports.append(mod)
        elif isinstance(node, ast.Dict):
            for val in node.values:
                if isinstance(val, ast.Constant) and isinstance(val.value, bool):
                    dict_bool_literals.append((getattr(val, "lineno", -1), repr(val.value)))
        elif isinstance(node, ast.Attribute) and node.attr == "eigh":
            eigh_calls.append(getattr(node, "lineno", -1))

    sha = hashlib.sha256(src.encode("utf-8")).hexdigest()
    manifest_path = os.path.join(os.path.dirname(script_path), "SCRIPT_SHA256.txt")
    manifest_match = None
    manifest_sha = None
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as mf:
            parts = mf.read().strip().split()
            if parts:
                manifest_sha = parts[0]
                manifest_match = bool(manifest_sha == sha)

    hygiene_ok = bool(
        len(bad_literals) == 0
        and len(bad_imports) == 0
        and len(dict_bool_literals) == 0
        and len(eigh_calls) == 0
    )
    return {
        "script_sha256": sha,
        "manifest_sha256": manifest_sha,
        "manifest_match": manifest_match,
        "float_or_complex_ast_literals": bad_literals,
        "float_or_complex_literal_count": len(bad_literals),
        "forbidden_imports": bad_imports,
        "forbidden_import_count": len(bad_imports),
        "dict_literal_bools": dict_bool_literals,
        "dict_literal_bool_count": len(dict_bool_literals),
        "eigh_attribute_refs": eigh_calls,
        "eigh_ref_count": len(eigh_calls),
        "hygiene_pass": hygiene_ok,
    }


# =============================================================================
# SECTION 1: DISJOINT LINEAR ALGEBRA (45-DPS HOUSEHOLDER QR, SVD_C, TAKAGI)
# =============================================================================

def mat_copy_mp(A):
    return mp.matrix([[mp.mpc(A[r, c]) for c in range(A.cols)] for r in range(A.rows)])


def mat_conj_mp(A):
    return mp.matrix([[mp.conj(A[r, c]) for c in range(A.cols)] for r in range(A.rows)])


def mat_real_mp(A):
    return mp.matrix([[mp.mpc(mp.re(A[r, c]), 0) for c in range(A.cols)] for r in range(A.rows)])


def mat_frob_norm_mp(A):
    acc = mp.mpf(0)
    for r in range(A.rows):
        for c in range(A.cols):
            acc += abs(A[r, c]) ** 2
    return mp.sqrt(acc)


def householder_qr_mp(A):
    """
    Complex Householder-reflection QR factorization A = Q * R in current mp.mp.dps
    (disjoint from Gram-Schmidt), with Mezzadri canonical positive real diag(R).
    """
    n = A.rows
    m = A.cols
    R = mat_copy_mp(A)
    Q = mp.eye(n)
    zero = mp.mpf(0)

    for k in range(min(n, m)):
        sub = [R[i, k] for i in range(k, n)]
        norm_x = mp.sqrt(sum(abs(val) ** 2 for val in sub))
        if norm_x == zero:
            continue
        x0 = sub[0]
        abs_x0 = abs(x0)
        phase = (x0 / abs_x0) if abs_x0 > zero else mp.mpc(1)
        v = [val for val in sub]
        v[0] = v[0] + phase * norm_x
        v_norm2 = sum(abs(val) ** 2 for val in v)
        if v_norm2 == zero:
            continue
        beta = mp.mpf(2) / v_norm2

        for j in range(k, m):
            dot = sum(mp.conj(v[idx]) * R[k + idx, j] for idx in range(n - k))
            w = beta * dot
            for idx in range(n - k):
                R[k + idx, j] -= w * v[idx]
        for i in range(k + 1, n):
            R[i, k] = mp.mpc(0)

        for i in range(n):
            dot = sum(Q[i, k + idx] * v[idx] for idx in range(n - k))
            w = beta * dot
            for idx in range(n - k):
                Q[i, k + idx] -= w * mp.conj(v[idx])

    for k in range(min(n, m)):
        rkk = R[k, k]
        abs_rkk = abs(rkk)
        if abs_rkk > zero:
            d_k = rkk / abs_rkk
            d_k_conj = mp.conj(d_k)
            for i in range(n):
                Q[i, k] *= d_k
            for j in range(k, m):
                R[k, j] *= d_k_conj
            R[k, k] = mp.mpc(abs_rkk, 0)

    return Q, R


def random_haar_u3_householder_mp(rng):
    """Exact Mezzadri (2007) Haar random U(3) matrix via complex Ginibre + Householder QR."""
    two128 = 1 << 128

    def std_normal():
        u1 = mp.mpf(rng.randrange(1, two128)) / mp.mpf(two128)
        u2 = mp.mpf(rng.randrange(1, two128)) / mp.mpf(two128)
        rad = mp.sqrt(-2 * mp.log(u1))
        ang = 2 * mp.pi * u2
        return rad * mp.cos(ang), rad * mp.sin(ang)

    Z = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            x, y = std_normal()
            Z[r, c] = mp.mpc(x, y)
    Q, _ = householder_qr_mp(Z)
    return Q


def random_haar_su3_householder_mp(rng):
    """Exact Haar random SU(3) matrix (det U == 1) from Mezzadri U(3)."""
    Q = random_haar_u3_householder_mp(rng)
    det_q = mp.det(Q)
    theta = mp.arg(det_q)
    scale = mp.exp(mp.mpc(0, -1) * theta / 3)
    return scale * Q


def svd_sector_ascending_mp(Y):
    """
    Compute exact SVD Y = U * diag(S) * Vh via mp.svd_c in physical ascending
    singular-value order (sigma_1 <= sigma_2 <= sigma_3).
    """
    U_raw, S_raw, Vh_raw = mp.svd_c(Y)
    s_list = [mp.re(S_raw[i]) for i in range(3)]
    idx = sorted(range(3), key=lambda i: s_list[i])
    svs_asc = [s_list[i] for i in idx]
    U_asc = mp.matrix([[U_raw[r, idx[c]] for c in range(3)] for r in range(3)])
    Vh_asc = mp.matrix([[Vh_raw[idx[r], c] for c in range(3)] for r in range(3)])
    V_asc = Vh_asc.H

    D_asc = mp.diag(svs_asc)
    recon_err = mat_frob_norm_mp(U_asc * D_asc * Vh_asc - Y)
    unit_err = max(
        mat_frob_norm_mp(U_asc.H * U_asc - mp.eye(3)),
        mat_frob_norm_mp(V_asc.H * V_asc - mp.eye(3)),
    )

    s1, s2, s3 = svs_asc
    r23 = s2 / s3 if s3 > 0 else mp.mpf(0)
    r13 = s1 / s3 if s3 > 0 else mp.mpf(0)
    r12 = s1 / s2 if s2 > 0 else mp.mpf(0)
    return {
        "svs_asc": svs_asc,
        "U_asc": U_asc,
        "V_asc": V_asc,
        "Vh_asc": Vh_asc,
        "r23": r23,
        "r13": r13,
        "r12": r12,
        "recon_err": recon_err,
        "unit_err": unit_err,
    }


def jacobi_real_sym_mp(A_real, max_sweeps=40):
    """
    Classical real symmetric Jacobi Givens diagonalization Q^T A Q = diag
    (elementary fallback for degenerate Takagi blocks; zero mp.eigh calls).
    """
    n = A_real.rows
    A = mp.matrix([[mp.mpf(A_real[r, c]) for c in range(n)] for r in range(n)])
    Q = mp.eye(n)
    tol = mp.mpf(10) ** (-mp.mp.dps + 4)

    for _ in range(max_sweeps):
        max_off = mp.mpf(0)
        for p in range(n):
            for q in range(p + 1, n):
                apq = A[p, q]
                if abs(apq) > max_off:
                    max_off = abs(apq)
                if abs(apq) <= tol:
                    continue
                app = A[p, p]
                aqq = A[q, q]
                tau = (aqq - app) / (2 * apq)
                if tau >= 0:
                    t = 1 / (tau + mp.sqrt(1 + tau * tau))
                else:
                    t = -1 / (-tau + mp.sqrt(1 + tau * tau))
                c = 1 / mp.sqrt(1 + t * t)
                s = t * c
                for k in range(n):
                    if k != p and k != q:
                        akp = A[k, p]
                        akq = A[k, q]
                        A[k, p] = c * akp - s * akq
                        A[p, k] = A[k, p]
                        A[k, q] = s * akp + c * akq
                        A[q, k] = A[k, q]
                A[p, p] = c * c * app - 2 * s * c * apq + s * s * aqq
                A[q, q] = s * s * app + 2 * s * c * apq + c * c * aqq
                A[p, q] = mp.mpf(0)
                A[q, p] = mp.mpf(0)
                for k in range(n):
                    qkp = Q[k, p]
                    qkq = Q[k, q]
                    Q[k, p] = c * qkp - s * qkq
                    Q[k, q] = s * qkp + c * qkq
        if max_off <= tol:
            break
    return Q


def takagi_svd_mp(M):
    """
    Disjoint Autonne-Takagi factorization via mp.svd_c + unitary-symmetric
    polar phase extraction (strictly disjoint from mp.eigh!).

    For complex symmetric M = M^T, finds unitary U_R (and U_left = U_R^*) and
    non-negative ascending Takagi singular values 0 <= M_1 <= M_2 <= M_3 such that:
        U_R^T * M * U_R = diag(M_1, M_2, M_3)
        M = U_left * diag(M_1, M_2, M_3) * U_left^T.
    """
    sym_err = mat_frob_norm_mp(M - M.T)
    M_sym = (M + M.T) / 2
    svd = svd_sector_ascending_mp(M_sym)
    U_asc = svd["U_asc"]
    Vh_asc = svd["Vh_asc"]
    s_asc = svd["svs_asc"]

    # W = Vh_asc * U_asc^* satisfies U_asc^H * M_sym * U_asc^* = diag(s_asc) * W.
    # For non-degenerate singular values, W is diagonal unitary W = diag(e^{i phi_k}).
    U_conj = mat_conj_mp(U_asc)
    W = Vh_asc * U_conj
    w_offdiag = mp.sqrt(
        sum(abs(W[r, c]) ** 2 for r in range(3) for c in range(3) if r != c)
    )

    s_max = s_asc[2] if s_asc[2] > 0 else mp.mpf(1)
    deg_tol = mp.mpf(10) ** (-12) * s_max
    non_deg = bool(
        (s_asc[1] - s_asc[0]) > deg_tol
        and (s_asc[2] - s_asc[1]) > deg_tol
        and w_offdiag < mp.mpf(10) ** (-20)
    )

    if non_deg:
        Z = mp.matrix(3, 3)
        for k in range(3):
            phi_k = mp.arg(W[k, k])
            Z[k, k] = mp.exp(mp.mpc(0, -1) * phi_k / 2)
    else:
        # Degenerate-block fallback: W is block-diagonal unitary symmetric, so
        # Re(W) and Im(W) commute; diagonalize each degenerate cluster via real Jacobi.
        Z = mp.matrix(3, 3)
        clusters = []
        i = 0
        while i < 3:
            j = i + 1
            while j < 3 and abs(s_asc[j] - s_asc[i]) <= deg_tol:
                j += 1
            clusters.append(list(range(i, j)))
            i = j
        mix_c = mp.mpf(17) / 13
        for cl in clusters:
            k_sz = len(cl)
            if k_sz == 1:
                idx0 = cl[0]
                Z[idx0, idx0] = mp.exp(mp.mpc(0, -1) * mp.arg(W[idx0, idx0]) / 2)
            else:
                Wb = mp.matrix([[W[r, c] for c in cl] for r in cl])
                Wb = (Wb + Wb.T) / 2
                Rcomb = mp.matrix(
                    [[mp.re(Wb[r, c]) + mix_c * mp.im(Wb[r, c]) for c in range(k_sz)] for r in range(k_sz)]
                )
                Q_real = jacobi_real_sym_mp(Rcomb)
                D_blk = Q_real.T * Wb * Q_real
                Ph_blk = mp.matrix(k_sz, k_sz)
                for m_idx in range(k_sz):
                    Ph_blk[m_idx, m_idx] = mp.exp(mp.mpc(0, -1) * mp.arg(D_blk[m_idx, m_idx]) / 2)
                Z_blk = Q_real * Ph_blk
                for ri, r_orig in enumerate(cl):
                    for ci, c_orig in enumerate(cl):
                        Z[r_orig, c_orig] = Z_blk[ri, ci]

    U_R = U_conj * Z
    U_left = mat_conj_mp(U_R)
    D_mat = mp.diag(s_asc)

    takagi_res = mat_frob_norm_mp(U_R.T * M * U_R - D_mat)
    recon_left_res = mat_frob_norm_mp(U_left * D_mat * U_left.T - M)
    unit_err = mat_frob_norm_mp(U_R.H * U_R - mp.eye(3))

    return {
        "M_asc": s_asc,
        "U_R": U_R,
        "U_left": U_left,
        "sym_err": sym_err,
        "w_offdiag_err": w_offdiag,
        "takagi_residual": takagi_res,
        "recon_left_residual": recon_left_res,
        "unit_err": unit_err,
    }


def apply_bulk_profile_perm_mp(Y, perm, eps_f):
    """Apply right-handed 7D bulk profile Y_eff[r, c] = Y[r, perm[c]] * [eps_f^2, eps_f, 1][c]."""
    weights = [eps_f * eps_f, eps_f, mp.mpf(1)]
    out = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            out[r, c] = Y[r, perm[c]] * weights[c]
    return out


def compute_bar_theta_Q_mp(Yu, Yd):
    """Compute bar_theta_Q = arg det(Y_u Y_d) directly from explicit 3x3 complex matrices."""
    det_prod = mp.det(Yu * Yd)
    return mp.arg(det_prod)


def extract_ckm_mp(Yu, Yd):
    su = svd_sector_ascending_mp(Yu)
    sd = svd_sector_ascending_mp(Yd)
    V = su["U_asc"].H * sd["U_asc"]
    V_abs = [[abs(V[r, c]) for c in range(3)] for r in range(3)]
    J_CP = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))
    return {
        "u": su,
        "d": sd,
        "V": V,
        "V_abs": V_abs,
        "V_us": V_abs[0][1],
        "V_cb": V_abs[1][2],
        "V_ub": V_abs[0][2],
        "J_CP": J_CP,
    }


def extract_pmns_from_takagi_mp(Ye, tak_nu):
    """
    Extract PMNS matrix U_PMNS = U_e^H * U_nu where M_nu = U_nu * diag(m_1, m_2, m_3) * U_nu^T
    (ascending mass order m_1 <= m_2 <= m_3 and m_e <= m_mu <= m_tau).
    """
    se = svd_sector_ascending_mp(Ye)
    U_e = se["U_asc"]
    U_nu = tak_nu["U_left"]
    U = U_e.H * U_nu
    U_abs = [[abs(U[r, c]) for c in range(3)] for r in range(3)]
    sin2_t13 = U_abs[0][2] ** 2
    denom_13 = 1 - sin2_t13
    sin2_t12 = (U_abs[0][1] ** 2) / denom_13
    sin2_t23 = (U_abs[1][2] ** 2) / denom_13
    J_PMNS = mp.im(U[0, 0] * U[1, 1] * mp.conj(U[0, 1]) * mp.conj(U[1, 0]))

    m1, m2, m3 = tak_nu["M_asc"]
    dm21 = m2 * m2 - m1 * m1
    dm31 = m3 * m3 - m1 * m1
    dm21_over_dm31 = dm21 / dm31
    return {
        "e": se,
        "U": U,
        "U_abs": U_abs,
        "sin2_theta12": sin2_t12,
        "sin2_theta23": sin2_t23,
        "sin2_theta13": sin2_t13,
        "J_PMNS": J_PMNS,
        "abs_J_PMNS": abs(J_PMNS),
        "m_nu_asc": tak_nu["M_asc"],
        "dm21_over_dm31": dm21_over_dm31,
        "takagi_residual": tak_nu["takagi_residual"],
        "e_svd_err": max(se["recon_err"], se["unit_err"]),
    }


def compute_leptogenesis_fy_mp(Y_nu, M_R):
    """
    Exact 1-loop Fukugita-Yanagida CP asymmetry epsilon_1 for lightest RH neutrino N_1:
        U_R^T M_R U_R = diag(M_1, M_2, M_3 > 0)   (ascending M_1 < M_2 < M_3)
        H_hat = U_R^H * Y_nu^H * Y_nu * U_R
        f(x) = sqrt(x) * [1 / (1 - x) + 1 - (1 + x) * ln((1 + x) / x)]
        epsilon_1 = (1 / (8 * pi)) * sum_{j=2,3} Im((H_hat)_{1j}^2) / (H_hat)_{11} * f(M_j^2 / M_1^2)
        epsilon_1^{norm} = epsilon_1 / sigma_max(Y_nu)^2.
    """
    tak_R = takagi_svd_mp(M_R)
    U_R = tak_R["U_R"]
    M1, M2, M3 = tak_R["M_asc"]
    H_hat = U_R.H * (Y_nu.H * Y_nu) * U_R
    H11 = mp.re(H_hat[0, 0])

    s_nu = svd_sector_ascending_mp(Y_nu)
    sigma_max = s_nu["svs_asc"][2]

    def fy_loop_f(x):
        return mp.sqrt(x) * (1 / (1 - x) + 1 - (1 + x) * mp.log((1 + x) / x))

    x_vals = [(M2 / M1) ** 2, (M3 / M1) ** 2]
    f_vals = [fy_loop_f(x) for x in x_vals]
    acc = mp.mpf(0)
    for idx_j, f_val in zip((1, 2), f_vals):
        h_1j_sq = H_hat[0, idx_j] ** 2
        acc += (mp.im(h_1j_sq) / H11) * f_val
    eps1_raw = acc / (8 * mp.pi)
    eps1_norm = eps1_raw / (sigma_max * sigma_max)

    return {
        "tak_R": tak_R,
        "H_hat": H_hat,
        "H_hat_11": H11,
        "sigma_max_Y_nu": sigma_max,
        "x_vals": x_vals,
        "f_vals": f_vals,
        "epsilon_1_raw": eps1_raw,
        "epsilon_1_norm": eps1_norm,
    }


# =============================================================================
# SECTION 2: DISJOINT GL6 ORDER-20 L_2(tau) & MP.JTHETA E[5]+E[6] OPERATORS
# =============================================================================

def sl2_mul(g1, g2):
    a1, b1, c1, d1 = g1
    a2, b2, c2, d2 = g2
    return (
        a1 * a2 + b1 * c2,
        a1 * b2 + b1 * d2,
        c1 * a2 + d1 * c2,
        c1 * b2 + d1 * d2,
    )


def reduce_to_F1_mp(z):
    g = (1, 0, 0, 1)
    cur = z
    half = mp.mpf(1) / 2
    tol = 1 - mp.mpf(10) ** (-mp.mp.dps + 6)
    for _ in range(250):
        k = int(mp.floor(mp.re(cur) + half))
        if k != 0:
            cur = cur - k
            g = sl2_mul((1, -k, 0, 1), g)
        n2 = mp.re(cur) ** 2 + mp.im(cur) ** 2
        if n2 < tol:
            cur = -1 / cur
            g = sl2_mul((0, -1, 1, 0), g)
        else:
            break
    k = int(mp.floor(mp.re(cur) + half))
    if k != 0:
        cur = cur - k
        g = sl2_mul((1, -k, 0, 1), g)
    return cur, g


def eta_pentagonal_mp(tau):
    im = mp.mpc(0, 1)
    q = mp.exp(2 * mp.pi * im * tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 8)
    s = mp.mpc(1)
    k = 1
    while True:
        e1 = (k * (3 * k - 1)) // 2
        e2 = (k * (3 * k + 1)) // 2
        t1 = q ** e1
        t2 = q ** e2
        term = t1 + t2
        if k % 2 == 1:
            s -= term
        else:
            s += term
        if abs(t1) < tol:
            break
        k += 1
    return mp.exp(mp.pi * im * tau / 12) * s


def eisenstein_e2_e4_e6_mp(tau):
    im = mp.mpc(0, 1)
    q = mp.exp(2 * mp.pi * im * tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 8)
    s2 = mp.mpc(0)
    s4 = mp.mpc(0)
    s6 = mp.mpc(0)
    qm = q
    m = 1
    while True:
        inv = qm / (1 - qm)
        m2 = m * m
        m3 = m2 * m
        m5 = m3 * m2
        s2 += m * inv
        s4 += m3 * inv
        s6 += m5 * inv
        if abs(qm) * m5 < tol:
            break
        qm *= q
        m += 1
    return 1 - 24 * s2, 1 + 240 * s4, 1 - 504 * s6


def exact_gl6_extrap_weights(n_seq):
    K = len(n_seq) - 1
    A = [[Fraction(1) for _ in range(K + 1)]]
    b = [Fraction(1)]
    for m in range(1, K + 1):
        p = 4 + 2 * m
        A.append([Fraction(1, nn ** p) for nn in n_seq])
        b.append(Fraction(0))
    M = [A[i] + [b[i]] for i in range(K + 1)]
    for col in range(K + 1):
        piv = next(r for r in range(col, K + 1) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        d = M[col][col]
        M[col] = [x / d for x in M[col]]
        for r in range(K + 1):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][j] - f * M[col][j] for j in range(K + 2)]
    return [
        mp.mpf(M[i][K + 1].numerator) / mp.mpf(M[i][K + 1].denominator)
        for i in range(K + 1)
    ]


def gl6_tableau_mp():
    s15 = mp.sqrt(15)
    c_nodes = [mp.mpf(1) / 2 - s15 / 10, mp.mpf(1) / 2, mp.mpf(1) / 2 + s15 / 10]
    b_w = [mp.mpf(5) / 18, mp.mpf(4) / 9, mp.mpf(5) / 18]
    A = [
        [mp.mpf(5) / 36, mp.mpf(2) / 9 - s15 / 15, mp.mpf(5) / 36 - s15 / 30],
        [mp.mpf(5) / 36 + s15 / 24, mp.mpf(2) / 9, mp.mpf(5) / 36 - s15 / 24],
        [mp.mpf(5) / 36 + s15 / 30, mp.mpf(2) / 9 + s15 / 15, mp.mpf(5) / 36],
    ]
    A2 = [[sum(A[i][m] * A[m][k] for m in range(3)) for k in range(3)] for i in range(3)]
    return c_nodes, b_w, A, A2


def make_weierstrass_wp_jtheta(tau):
    e2, _, _ = eisenstein_e2_e4_e6_mp(tau)
    pi = mp.pi
    im = mp.mpc(0, 1)
    c_e2 = (pi * pi / 3) * e2
    q_nome = mp.exp(im * pi * tau)
    im_t = mp.im(tau)

    def wp(z):
        k_shift = int(mp.nint(mp.im(z) / im_t))
        if k_shift != 0:
            z = z - k_shift * tau
        pz = pi * z
        t0 = mp.jtheta(1, pz, q_nome)
        t1 = pi * mp.jtheta(1, pz, q_nome, 1)
        t2 = (pi * pi) * mp.jtheta(1, pz, q_nome, 2)
        return -(t2 * t0 - t1 * t1) / (t0 * t0) - c_e2

    return wp


def solve3x3_two_rhs(M, r1, r2):
    A = [[M[i][j] for j in range(3)] + [r1[i], r2[i]] for i in range(3)]
    for col in range(3):
        piv = max(range(col, 3), key=lambda r: abs(A[r][col]))
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
        d = A[col][col]
        for j in range(col, 5):
            A[col][j] /= d
        for r in range(3):
            if r != col:
                f = A[r][col]
                for j in range(col, 5):
                    A[r][j] -= f * A[col][j]
    return [A[i][3] for i in range(3)], [A[i][4] for i in range(3)]


def precompute_gl6_chains(segs, wp, n_seq, glc):
    c_nodes = glc[0]
    out = []
    for nn in n_seq:
        chain = []
        for (za, zb) in segs:
            dz = (zb - za) / nn
            wps = [[wp(za + (s + c_nodes[i]) * dz) / 4 for i in range(3)] for s in range(nn)]
            chain.append((dz, wps))
        out.append(chain)
    return out


def gl6_chain_integrate(chain, c, glc, need_dc=False):
    c_nodes, b_w, A, A2 = glc
    U1, U2, V1, V2 = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
    dU1, dU2, dV1, dV2 = mp.mpc(0), mp.mpc(0), mp.mpc(0), mp.mpc(0)
    for (dz, wps) in chain:
        dz2 = dz * dz
        for w3 in wps:
            qs = [w3[i] + c for i in range(3)]
            M = [
                [(1 if i == k else 0) + dz2 * A2[i][k] * qs[k] for k in range(3)]
                for i in range(3)
            ]
            r1 = [U1 + dz * c_nodes[i] * V1 for i in range(3)]
            r2 = [U2 + dz * c_nodes[i] * V2 for i in range(3)]
            Us1, Us2 = solve3x3_two_rhs(M, r1, r2)
            Vs1 = [V1 - dz * sum(A[i][k] * qs[k] * Us1[k] for k in range(3)) for i in range(3)]
            Vs2 = [V2 - dz * sum(A[i][k] * qs[k] * Us2[k] for k in range(3)) for i in range(3)]
            if need_dc:
                dr1 = [
                    dU1 + dz * c_nodes[i] * dV1 - dz2 * sum(A2[i][k] * Us1[k] for k in range(3))
                    for i in range(3)
                ]
                dr2 = [
                    dU2 + dz * c_nodes[i] * dV2 - dz2 * sum(A2[i][k] * Us2[k] for k in range(3))
                    for i in range(3)
                ]
                dUs1, dUs2 = solve3x3_two_rhs(M, dr1, dr2)
                dVs1 = [
                    dV1 - dz * sum(A[i][k] * (qs[k] * dUs1[k] + Us1[k]) for k in range(3))
                    for i in range(3)
                ]
                dVs2 = [
                    dV2 - dz * sum(A[i][k] * (qs[k] * dUs2[k] + Us2[k]) for k in range(3))
                    for i in range(3)
                ]
                dU1 += dz * sum(b_w[i] * dVs1[i] for i in range(3))
                dU2 += dz * sum(b_w[i] * dVs2[i] for i in range(3))
                dV1 -= dz * sum(b_w[i] * (qs[i] * dUs1[i] + Us1[i]) for i in range(3))
                dV2 -= dz * sum(b_w[i] * (qs[i] * dUs2[i] + Us2[i]) for i in range(3))
            U1 += dz * sum(b_w[i] * Vs1[i] for i in range(3))
            U2 += dz * sum(b_w[i] * Vs2[i] for i in range(3))
            V1 -= dz * sum(b_w[i] * qs[i] * Us1[i] for i in range(3))
            V2 -= dz * sum(b_w[i] * qs[i] * Us2[i] for i in range(3))
    return [U1, U2, V1, V2], [dU1, dU2, dV1, dV2]


def half_to_full_monodromy(H, dH):
    a, b, cc, d = H
    da, db, dc, dd = dH
    tr = d * a + b * cc
    dtr = dd * a + d * da + db * cc + b * dc
    M = mp.matrix([[tr, 2 * b * d], [2 * a * cc, tr]])
    dM = mp.matrix([[dtr, 2 * (db * d + b * dd)], [2 * (da * cc + a * dc), dtr]])
    return M, dM


def gl6_extrap_eval(pre, weights, c, glc, need_dc=False):
    acc = [mp.mpc(0)] * 4
    dacc = [mp.mpc(0)] * 4
    for chain, w in zip(pre, weights):
        Y, dY = gl6_chain_integrate(chain, c, glc, need_dc)
        for k in range(4):
            acc[k] += w * Y[k]
            if need_dc:
                dacc[k] += w * dY[k]
    return acc, dacc


def solve_L2_F1_gl6(tau):
    wp = make_weierstrass_wp_jtheta(tau)
    glc = gl6_tableau_mp()
    if mp.re(tau) > 0:
        z0 = (-1 + tau) / 2
        midA = tau / 2
        midB = -mp.mpf(1) / 2
    else:
        z0 = (-1 - tau) / 2
        midA = -tau / 2
        midB = -mp.mpf(1) / 2

    segs_A = [(z0 + k * (midA - z0) / 2, z0 + (k + 1) * (midA - z0) / 2) for k in range(2)]
    segs_B = []
    cur = z0
    while abs(cur - midB) > mp.mpf(1) / 4:
        nxt = midB + (cur - midB) * mp.mpf(2) / 3
        segs_B.append((cur, nxt))
        cur = nxt
    segs_B.append((cur, midB))

    n_seq_m = [4, 6, 8, 12]
    n_seq_f = [4, 6, 8, 12, 16, 24, 32, 48]
    w_m = exact_gl6_extrap_weights(n_seq_m)
    w_f = exact_gl6_extrap_weights(n_seq_f)

    preA_m = precompute_gl6_chains(segs_A, wp, n_seq_m, glc)
    preB_m = precompute_gl6_chains(segs_B, wp, n_seq_m, glc)

    def gn_step(cr, ci, f, J):
        g11 = sum(J[i][0] * J[i][0] for i in range(3))
        g12 = sum(J[i][0] * J[i][1] for i in range(3))
        g22 = sum(J[i][1] * J[i][1] for i in range(3))
        b1 = sum(J[i][0] * f[i] for i in range(3))
        b2 = sum(J[i][1] * f[i] for i in range(3))
        det = g11 * g22 - g12 * g12
        return cr - (g22 * b1 - g12 * b2) / det, ci - (-g12 * b1 + g11 * b2) / det

    def get_f_J_m(c_val):
        HA, dHA = gl6_extrap_eval(preA_m, w_m, c_val, glc, True)
        HB, dHB = gl6_extrap_eval(preB_m, w_m, c_val, glc, True)
        M1, dM1 = half_to_full_monodromy(HA, dHA)
        MB, dMB = half_to_full_monodromy(HB, dHB)
        dtA = dM1[0, 0] + dM1[1, 1]
        dtB = dMB[0, 0] + dMB[1, 1]
        dAB = dM1 * MB + M1 * dMB
        dtAB = dAB[0, 0] + dAB[1, 1]
        f = [
            mp.im(M1[0, 0] + M1[1, 1]),
            mp.im(MB[0, 0] + MB[1, 1]),
            mp.im((M1 * MB)[0, 0] + (M1 * MB)[1, 1]),
        ]
        J = [
            [mp.im(dtA), mp.re(dtA)],
            [mp.im(dtB), mp.re(dtB)],
            [mp.im(dtAB), mp.re(dtAB)],
        ]
        return f, J

    cr = (mp.pi ** 2) / 12
    ci = mp.mpf(0)
    for _ in range(10):
        c_val = mp.mpc(cr, ci)
        HA, dHA = gl6_chain_integrate(preA_m[1], c_val, glc, True)
        HB, dHB = gl6_chain_integrate(preB_m[1], c_val, glc, True)
        M1, dM1 = half_to_full_monodromy(HA, dHA)
        MB, dMB = half_to_full_monodromy(HB, dHB)
        f = [
            mp.im(M1[0, 0] + M1[1, 1]),
            mp.im(MB[0, 0] + MB[1, 1]),
            mp.im((M1 * MB)[0, 0] + (M1 * MB)[1, 1]),
        ]
        if max(abs(x) for x in f) < mp.mpf(10) ** (-11):
            break
        dtA = dM1[0, 0] + dM1[1, 1]
        dtB = dMB[0, 0] + dMB[1, 1]
        dAB = dM1 * MB + M1 * dMB
        dtAB = dAB[0, 0] + dAB[1, 1]
        J = [
            [mp.im(dtA), mp.re(dtA)],
            [mp.im(dtB), mp.re(dtB)],
            [mp.im(dtAB), mp.re(dtAB)],
        ]
        cr, ci = gn_step(cr, ci, f, J)

    for _ in range(4):
        c_val = mp.mpc(cr, ci)
        f, J = get_f_J_m(c_val)
        if max(abs(x) for x in f) < mp.mpf(10) ** (-25):
            break
        cr, ci = gn_step(cr, ci, f, J)

    preA_f = precompute_gl6_chains(segs_A, wp, n_seq_f, glc)
    preB_f = precompute_gl6_chains(segs_B, wp, n_seq_f, glc)
    _, J_ref = get_f_J_m(mp.mpc(cr, ci))
    for _ in range(3):
        c_val = mp.mpc(cr, ci)
        HA, _ = gl6_extrap_eval(preA_f, w_f, c_val, glc, False)
        HB, _ = gl6_extrap_eval(preB_f, w_f, c_val, glc, False)
        M1, _ = half_to_full_monodromy(HA, [0, 0, 0, 0])
        MB, _ = half_to_full_monodromy(HB, [0, 0, 0, 0])
        f = [
            mp.im(M1[0, 0] + M1[1, 1]),
            mp.im(MB[0, 0] + MB[1, 1]),
            mp.im((M1 * MB)[0, 0] + (M1 * MB)[1, 1]),
        ]
        if max(abs(x) for x in f) < mp.mpf(10) ** (-50):
            break
        cr, ci = gn_step(cr, ci, f, J_ref)

    c_star = mp.mpc(cr, ci)
    HA, _ = gl6_extrap_eval(preA_f, w_f, c_star, glc, False)
    HB, _ = gl6_extrap_eval(preB_f, w_f, c_star, glc, False)
    M1, _ = half_to_full_monodromy(HA, [0, 0, 0, 0])
    MB, _ = half_to_full_monodromy(HB, [0, 0, 0, 0])

    m1 = M1.T
    mB = MB.T
    P = m1 * mB * (m1 ** -1) * (mB ** -1)
    PI = P + mp.eye(2)
    if abs(PI[0, 0]) + abs(PI[0, 1]) >= abs(PI[1, 0]) + abs(PI[1, 1]):
        e1 = mp.matrix([PI[0, 1], -PI[0, 0]])
    else:
        e1 = mp.matrix([PI[1, 1], -PI[1, 0]])
    e1 /= mp.norm(e1)
    e2 = mp.matrix([-mp.conj(e1[1]), mp.conj(e1[0])])
    S0 = mp.matrix([[e1[0], e2[0]], [e1[1], e2[1]]])
    S0 /= mp.sqrt(S0[0, 0] * S0[1, 1] - S0[0, 1] * S0[1, 0])
    m1t = (S0 ** -1) * m1 * S0
    r_sc = 1 / mp.sqrt(m1t[1, 0])
    s_sh = m1t[0, 0] / (r_sc * m1t[1, 0])
    C_mat = S0 * mp.matrix([[r_sc, s_sh], [0, 1 / r_sc]])
    mBh = (C_mat ** -1) * mB * C_mat
    Ph = (C_mat ** -1) * P * C_mat
    lam = abs(mp.re(Ph[0, 1]))

    segs_in = []
    cur = z0
    while abs(cur) > mp.mpf(1) / 10:
        nxt = cur * mp.mpf(2) / 3
        segs_in.append((cur, nxt))
        cur = nxt
    zs = cur
    preIn = precompute_gl6_chains(segs_in, wp, n_seq_f, glc)
    Yv, _ = gl6_extrap_eval(preIn, w_f, c_star, glc, False)
    Y = mp.matrix([[Yv[0], Yv[1]], [Yv[2], Yv[3]]])

    _, e4, e6 = eisenstein_e2_e4_e6_mp(tau)
    NT = 48
    ck = [mp.mpc(0)] * NT
    ck[1] = (mp.pi ** 4) / 15 * e4
    ck[2] = 2 * (mp.pi ** 6) / 189 * e6
    for k in range(3, NT):
        ck[k] = (
            mp.mpf(3)
            / ((2 * k + 3) * (k - 2))
            * sum(ck[j] * ck[k - 1 - j] for j in range(1, k - 1))
        )
    qk = [c_star] + [ck[m] / 4 for m in range(1, NT)]
    an = [mp.mpc(1)] + [mp.mpc(0)] * (NT - 1)
    bn = [mp.mpc(0)] * NT
    for nn in range(1, NT):
        an[nn] = -sum(qk[nn - 1 - k] * an[k] for k in range(nn)) / (4 * nn * nn)
        bn[nn] = -an[nn] / nn - sum(qk[nn - 1 - k] * bn[k] for k in range(1, nn)) / (4 * nn * nn)

    sqrt_z = mp.sqrt(zs)
    log_z = mp.log(zs)
    f1 = sqrt_z * sum(an[nn] * (zs ** (2 * nn)) for nn in range(NT))
    f1p = sum(an[nn] * (2 * nn + mp.mpf(1) / 2) * (zs ** (2 * nn - 1)) * sqrt_z for nn in range(NT))
    g2 = sqrt_z * sum(bn[nn] * (zs ** (2 * nn)) for nn in range(1, NT))
    g2p = sum(bn[nn] * (2 * nn + mp.mpf(1) / 2) * (zs ** (2 * nn - 1)) * sqrt_z for nn in range(1, NT))
    f2 = f1 * log_z + g2
    f2p = f1p * log_z + f1 / zs + g2p

    Cinv = C_mat ** -1
    phi = Cinv * mp.matrix([Y[0, 0], Y[0, 1]])
    phip = Cinv * mp.matrix([Y[1, 0], Y[1, 1]])

    def wronsk(a, ap, b, bp):
        return a * bp - ap * b

    w_chk = abs(wronsk(f1, f1p, phi[1], phip[1]))
    alpha2 = wronsk(phi[1], phip[1], f2, f2p)
    beta1 = wronsk(f1, f1p, phi[0], phip[0])
    alpha1 = wronsk(phi[0], phip[0], f2, f2p)
    slope = beta1 / alpha2
    B_const = alpha1 / alpha2
    if mp.im(-slope) < 0:
        slope = -slope
        B_const = -B_const
    L2_val = mp.pi - (2 * mp.pi / lam) * mp.im(B_const)
    im_mBh = max(abs(mp.im(mBh[i, j])) for i in range(2) for j in range(2))
    return {"L2": L2_val, "w_check": w_chk, "im_mBh_err": im_mBh}


def solve_L2_any_gl6(tau, cache):
    tau_red, g = reduce_to_F1_mp(tau)
    _, _, c, d = g
    key = (mp.nstr(mp.re(tau_red), 50), mp.nstr(mp.im(tau_red), 50))
    if key not in cache:
        cache[key] = solve_L2_F1_gl6(tau_red)
    base = cache[key]
    return base["L2"] - mp.log(abs(c * tau + d)), base


def build_fu2_coupling_tensor():
    I2 = mp.matrix([[1, 0], [0, 1]])
    QI = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = mp.matrix([[0, mp.mpc(0, 1)], [mp.mpc(0, 1), 0]])
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]
    q_S = [QI, QJ, QK]
    ec_list = [EPS * U for U in units]

    def frob(A, B):
        return sum(A[r, c] * B[r, c] for r in range(2) for c in range(2))

    G = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            G[t, s] = frob(ec_list[t], units[s])
    Ginv = G ** -1
    edual = []
    for a in range(4):
        M = mp.matrix(2, 2)
        for b in range(4):
            M += Ginv[b, a] * units[b]
        edual.append(M)

    C = [[[[mp.mpc(0) for _ in range(3)] for _ in range(3)] for _ in range(4)] for _ in range(3)]
    for qi in range(3):
        for si in range(4):
            for a in range(3):
                for b in range(3):
                    mat = (blocks[a].T) * EPS * q_S[qi] * blocks[b]
                    C[qi][si][a][b] = frob(mat, edual[si])
    return ec_list, C


def compute_c3_denom_jtheta_mp(tau):
    im = mp.mpc(0, 1)
    et = eta_pentagonal_mp(tau)
    denom_hat = 2 * mp.pi * (et ** 3)
    e2, _, _ = eisenstein_e2_e4_e6_mp(tau)
    q = mp.exp(im * mp.pi * tau)
    ph = mp.exp(im * mp.pi * tau / 4) / (q ** (mp.mpf(1) / 4))
    th2 = ph * mp.jtheta(2, 0, q)
    dth2 = -ph * mp.jtheta(2, 0, q, 2) / 8
    th3 = mp.jtheta(3, 0, q)
    dth3 = -mp.jtheta(3, 0, q, 2) / 8
    th4 = mp.jtheta(4, 0, q)
    dth4 = -mp.jtheta(4, 0, q, 2) / 8
    R_h = [-(th2 * th2) / denom_hat, -(th4 * th4) / denom_hat, (im * th3 * th3) / denom_hat]
    dN_h = [
        -(2 * th2 * dth2) / denom_hat,
        -(2 * th4 * dth4) / denom_hat,
        (2 * im * th3 * dth3) / denom_hat,
    ]
    c_3 = [dN_h[k] - (e2 / 12) * R_h[k] for k in range(3)]
    return c_3, denom_hat


def eval_X0_X1_jtheta_mp(alpha_f, beta_f, tau):
    alpha = mp.mpf(alpha_f.numerator) / alpha_f.denominator
    beta = mp.mpf(beta_f.numerator) / beta_f.denominator
    im = mp.mpc(0, 1)
    q2 = mp.exp(2 * mp.pi * im * tau)
    z0 = mp.pi * (2 * alpha * tau + beta)
    X0 = mp.exp(2 * mp.pi * im * tau * alpha * alpha + 2 * mp.pi * im * beta * alpha) * mp.jtheta(3, z0, q2)
    a1 = alpha + mp.mpf(1) / 2
    z1 = mp.pi * (2 * a1 * tau + beta)
    X1 = mp.exp(2 * mp.pi * im * tau * a1 * a1 + 2 * mp.pi * im * beta * alpha) * mp.jtheta(3, z1, q2)
    return X0, X1


def eval_fu_a0_jtheta_mp(u_a_f, u_b_f, tau):
    pi = mp.pi
    im = mp.mpc(0, 1)
    x = mp.re(tau)
    y = mp.im(tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 6)
    u_a = mp.mpf(u_a_f.numerator) / u_a_f.denominator
    u_b = mp.mpf(u_b_f.numerator) / u_b_f.denominator

    def w_term(s_val):
        ws = mp.exp(2 * pi * im * (s_val * x + u_b) - 2 * pi * abs(s_val) * y)
        return (2 * pi / abs(s_val)) * mp.re(ws / (1 - ws))

    if u_a_f == 0:
        f_u = pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + (pi * pi * y) / (mp.sin(pi * u_b) ** 2)
        for m in range(1, 1000):
            t = w_term(mp.mpf(m)) + w_term(mp.mpf(-m))
            f_u += t
            if m > 4 and abs(t) < tol:
                break
    else:
        f_u = -pi * (mp.digamma(u_a) + mp.digamma(1 - u_a) + 2 * mp.log(2) + mp.log(y))
        f_u += w_term(u_a)
        for k in range(1, 1000):
            t = w_term(k + u_a) + w_term(-k + u_a)
            f_u += t
            if k > 4 and abs(t) < tol:
                break

    nu_f = u_a_f if u_a_f <= Fraction(1, 2) else u_a_f - 1
    nu = mp.mpf(nu_f.numerator) / nu_f.denominator
    Bm_f = (-u_b_f) % 1
    Bm = mp.mpf(Bm_f.numerator) / Bm_f.denominator
    w_z = nu * tau - Bm
    q_nome = mp.exp(im * pi * tau)
    a_0 = pi * mp.jtheta(1, pi * w_z, q_nome, 1) / mp.jtheta(1, pi * w_z, q_nome) + 2 * pi * im * nu
    return f_u, a_0


def center_mod_N(r, N):
    m = r % N
    return m if 2 * m <= N else m - N


def eval_yukawa_EN_mp(tau, L2_val, N, q_L, q_R, ec_list, C_ten, c_3, denom_hat, fu_cache):
    pi = mp.pi
    y = mp.im(tau)
    im = mp.mpc(0, 1)
    char_shifts = [
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1, 2)),
        (Fraction(-1, 2), Fraction(0)),
        (Fraction(-1, 2), Fraction(-1, 2)),
    ]
    base_const = 2 * pi * (L2_val + mp.log(y) / 2 - mp.euler - mp.log(pi))
    exp_m2L2 = mp.exp(-2 * L2_val)
    Y_sum = mp.matrix(3, 3)

    for a in range(N):
        for b in range(N):
            if a == 0 and b == 0:
                continue
            wL0 = Fraction(center_mod_N(q_L * a, N), N)
            wL1 = Fraction(center_mod_N(q_L * b, N), N)
            wR0 = Fraction(center_mod_N(q_R * a, N), N)
            wR1 = Fraction(center_mod_N(q_R * b, N), N)

            ax_f, bx_f = wL0, 2 * wL1
            ay_f, by_f = wR0, 2 * wR1
            X0x, X1x = eval_X0_X1_jtheta_mp(ax_f, bx_f, tau)
            X0y, X1y = eval_X0_X1_jtheta_mp(ay_f, by_f, tau)
            bx = mp.mpf(bx_f.numerator) / bx_f.denominator
            by = mp.mpf(by_f.numerator) / by_f.denominator
            ep_bx = mp.exp(im * pi * bx)
            ep_by = mp.exp(im * pi * by)
            M_m = mp.matrix([
                [X0x * X0y / denom_hat, -im * ep_by * X0x * X1y / denom_hat],
                [-im * ep_bx * X1x * X0y / denom_hat, -(ep_bx * ep_by) * X1x * X1y / denom_hat],
            ])
            R_ch = [
                sum(ec_list[si][r, c] * M_m[r, c] for r in range(2) for c in range(2))
                for si in range(4)
            ]

            u_ch = [mp.mpc(0)] * 4
            for si in range(4):
                ds1, ds2 = char_shifts[si]
                ua_f = (wL0 + wR0 + ds1) % 1
                ub_f = (wL1 + wR1 + ds2) % 1
                if ua_f == 0 and ub_f == 0:
                    u_ch[si] = mp.mpc(0)
                else:
                    key = (ua_f, ub_f)
                    if key not in fu_cache:
                        fu_cache[key] = eval_fu_a0_jtheta_mp(ua_f, ub_f, tau)
                    f_u, a_0 = fu_cache[key]
                    rad = base_const + f_u - pi * (abs(a_0) ** 2) * exp_m2L2
                    u_ch[si] = mp.sqrt(rad) * R_ch[si]

            phi_ab = mp.exp(2 * pi * im * ((-a * b) % N) / N)
            for ia in range(3):
                for ib in range(3):
                    entry = mp.mpc(0)
                    for qi in range(3):
                        for si in range(4):
                            cc = C_ten[qi][si][ia][ib]
                            if cc != 0:
                                entry += c_3[qi] * u_ch[si] * cc
                    Y_sum[ia, ib] += phi_ab * entry

    return Y_sum / (N * N - 1)


def build_all_ow12_operators(dps=55):
    """
    Build all open-weave A2-OW12 Yukawa and Majorana operators at 55 dps using
    disjoint GL6 order-20 L_2(tau) + mpmath.jtheta.
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    ec_list, C_ten = build_fu2_coupling_tensor()
    l2_cache = {}

    # Independent SL(2, Z) S-transformation law check without cache reuse
    tau_s = mp.mpc(1, 0) / 5 + mp.mpc(0, 1)
    r_sa = solve_L2_F1_gl6(tau_s)
    r_sb = solve_L2_F1_gl6(-1 / tau_s)
    L2_S_law_err = abs(r_sb["L2"] - (r_sa["L2"] + mp.log(abs(tau_s))))

    lam_3 = (3 + mp.sqrt(5)) / 2
    lam_4 = (4 + mp.sqrt(12)) / 2
    w_3 = lam_3 ** (-4)
    w_4 = 4 * (lam_4 ** (-4))

    points = {
        "m8_plus": (
            8 * mp.mpc(2, 1) / 5,
            {
                "u": (1, -4),
                "d": (1, 2),
                "e": (-3, 6),
                "nu": (-3, 0),
                "MR00": (0, 0),
                "q10": (1, 0),
            },
        ),
        "m8_minus": (
            8 * mp.mpc(-2, 1) / 5,
            {
                "u": (1, -4),
                "d": (1, 2),
                "nu": (-3, 0),
                "MR00": (0, 0),
            },
        ),
        "m24_plus": (
            24 * mp.mpc(2, 1) / 5,
            {
                "u": (1, -4),
                "d": (1, 2),
            },
        ),
        "tau_CP": (
            8 * mp.mpc(0, 1) / mp.sqrt(5),
            {
                "u": (1, -4),
                "d": (1, 2),
            },
        ),
    }

    out = {}
    max_wchk = max(r_sa["w_check"], r_sb["w_check"])
    max_im_mBh = max(r_sa["im_mBh_err"], r_sb["im_mBh_err"])

    for label, (tau_val, sec_map) in points.items():
        L2_val, base_info = solve_L2_any_gl6(tau_val, l2_cache)
        max_wchk = max(max_wchk, base_info["w_check"])
        max_im_mBh = max(max_im_mBh, base_info["im_mBh_err"])
        c3_val, den_val = compute_c3_denom_jtheta_mp(tau_val)
        fu_cache = {}
        Y_tot = {}
        Y_5_map = {}
        Y_6_map = {}
        for sec, (qL, qR) in sec_map.items():
            Y5 = eval_yukawa_EN_mp(tau_val, L2_val, 5, qL, qR, ec_list, C_ten, c3_val, den_val, fu_cache)
            Y6 = eval_yukawa_EN_mp(tau_val, L2_val, 6, qL, qR, ec_list, C_ten, c3_val, den_val, fu_cache)
            Y_5_map[sec] = Y5
            Y_6_map[sec] = Y6
            Y_tot[sec] = w_3 * Y5 + w_4 * Y6
        out[label] = {
            "tau": tau_val,
            "L2": L2_val,
            "w_check": base_info["w_check"],
            "im_mBh_err": base_info["im_mBh_err"],
            "Y": Y_tot,
            "Y5": Y_5_map,
            "Y6": Y_6_map,
        }

    L2_mirror_diff = abs(out["m8_plus"]["L2"] - out["m8_minus"]["L2"])
    diag = {
        "dps_engine": dps,
        "L2_m8_plus": mp.nstr(out["m8_plus"]["L2"], 35),
        "L2_m8_minus": mp.nstr(out["m8_minus"]["L2"], 35),
        "L2_m8_mirror_diff": mp.nstr(L2_mirror_diff, 10),
        "L2_m24_plus": mp.nstr(out["m24_plus"]["L2"], 35),
        "L2_tau_CP": mp.nstr(out["tau_CP"]["L2"], 35),
        "L2_S_law_err": mp.nstr(L2_S_law_err, 10),
        "max_w_check": mp.nstr(max_wchk, 10),
        "max_im_mBh_err": mp.nstr(max_im_mBh, 10),
        "engine_pass": bool(
            L2_S_law_err < mp.mpf(10) ** (-28)
            and max_wchk < mp.mpf(10) ** (-28)
            and max_im_mBh < mp.mpf(10) ** (-28)
            and L2_mirror_diff < mp.mpf(10) ** (-35)
        ),
    }

    mp.mp.dps = old_dps
    return out, diag


# =============================================================================
# SECTION 3: EXACT SYMPY.RATIONAL SPIN(10) 16_+ QUANTUM NUMBERS & ANOMALIES
# =============================================================================

def spin10_16plus_species_table():
    """
    Exact Spin(10) 16_+ single-generation LH Weyl fermion multiplet in sympy.Rational.
    Fundamental quantum numbers: (d_3, T(R_3), d_2, T_{3L} components, T_{3R}, B - L, card 6Y).
    """
    R = sp.Rational
    return [
        {
            "name": "Q_L",
            "chirality_rep": "LH_doublet",
            "d3": R(3),
            "T3_dynkin": R(1, 2),
            "d2": R(2),
            "T3L_list": [R(1, 2), R(-1, 2)],
            "T3R": R(0),
            "B_minus_L": R(1, 3),
            "six_Y_expected": R(1),
        },
        {
            "name": "u^c",
            "chirality_rep": "RH_singlet",
            "d3": R(3),
            "T3_dynkin": R(1, 2),
            "d2": R(1),
            "T3L_list": [R(0)],
            "T3R": R(-1, 2),
            "B_minus_L": R(-1, 3),
            "six_Y_expected": R(-4),
        },
        {
            "name": "d^c",
            "chirality_rep": "RH_singlet",
            "d3": R(3),
            "T3_dynkin": R(1, 2),
            "d2": R(1),
            "T3L_list": [R(0)],
            "T3R": R(1, 2),
            "B_minus_L": R(-1, 3),
            "six_Y_expected": R(2),
        },
        {
            "name": "L_L",
            "chirality_rep": "LH_doublet",
            "d3": R(1),
            "T3_dynkin": R(0),
            "d2": R(2),
            "T3L_list": [R(1, 2), R(-1, 2)],
            "T3R": R(0),
            "B_minus_L": R(-1),
            "six_Y_expected": R(-3),
        },
        {
            "name": "e^c",
            "chirality_rep": "RH_singlet",
            "d3": R(1),
            "T3_dynkin": R(0),
            "d2": R(1),
            "T3L_list": [R(0)],
            "T3R": R(1, 2),
            "B_minus_L": R(1),
            "six_Y_expected": R(6),
        },
        {
            "name": "nu^c",
            "chirality_rep": "RH_singlet",
            "d3": R(1),
            "T3_dynkin": R(0),
            "d2": R(1),
            "T3L_list": [R(0)],
            "T3R": R(-1, 2),
            "B_minus_L": R(1),
            "six_Y_expected": R(0),
        },
    ]


def compute_cs_axion_anomaly_sympy(species_list, q_pq=sp.Rational(1)):
    """
    Compute exact electromagnetic and color PQ anomaly coefficients (E_gen, N_gen, E/N)
    directly from (T_{3L}, T_{3R}, B - L, d_3, d_2, T(R_3)) over Q (sympy.Rational).
    """
    R = sp.Rational
    E_gen = R(0)
    N_gen = R(0)
    weyl_dim = R(0)
    breakdown = {}

    for sp_rec in species_list:
        Y_val = sp_rec["T3R"] + sp_rec["B_minus_L"] / 2
        Q_list = [t3l + Y_val for t3l in sp_rec["T3L_list"]]
        E_contrib = q_pq * sp_rec["d3"] * sum(q * q for q in Q_list)
        N_contrib = q_pq * sp_rec["d2"] * sp_rec["T3_dynkin"]
        E_gen += E_contrib
        N_gen += N_contrib
        weyl_dim += sp_rec["d3"] * sp_rec["d2"]
        breakdown[sp_rec["name"]] = {
            "Y": str(Y_val),
            "Q_em": [str(q) for q in Q_list],
            "E_contrib": str(E_contrib),
            "N_contrib": str(N_contrib),
        }

    E_over_N = E_gen / N_gen
    E_3gen = 3 * E_gen
    N_3gen = 3 * N_gen
    return {
        "E_gen": E_gen,
        "N_gen": N_gen,
        "E_over_N": E_over_N,
        "E_3gen": E_3gen,
        "N_3gen": N_3gen,
        "weyl_dim": int(weyl_dim),
        "breakdown": breakdown,
    }


# =============================================================================
# SECTION 4: TASK OW12-A (STRONG CP bar_theta_Q & 7D CS AXION E / N = 8 / 3)
# =============================================================================

def run_task_ow12_a(ops, dps=45):
    old_dps = mp.mp.dps
    mp.mp.dps = dps

    Yu_cp = mat_copy_mp(ops["tau_CP"]["Y"]["u"])
    Yd_cp = mat_copy_mp(ops["tau_CP"]["Y"]["d"])
    theta_cp = compute_bar_theta_Q_mp(Yu_cp, Yd_cp)

    Yu5_p = mat_copy_mp(ops["m8_plus"]["Y5"]["u"])
    Yd5_p = mat_copy_mp(ops["m8_plus"]["Y5"]["d"])
    theta_e5 = compute_bar_theta_Q_mp(Yu5_p, Yd5_p)

    Yu6_p = mat_copy_mp(ops["m8_plus"]["Y6"]["u"])
    Yd6_p = mat_copy_mp(ops["m8_plus"]["Y6"]["d"])
    theta_e6 = compute_bar_theta_Q_mp(Yu6_p, Yd6_p)

    Yu_p = mat_copy_mp(ops["m8_plus"]["Y"]["u"])
    Yd_p = mat_copy_mp(ops["m8_plus"]["Y"]["d"])
    theta_m8_p = compute_bar_theta_Q_mp(Yu_p, Yd_p)

    Yu_m = mat_copy_mp(ops["m8_minus"]["Y"]["u"])
    Yd_m = mat_copy_mp(ops["m8_minus"]["Y"]["d"])
    theta_m8_m = compute_bar_theta_Q_mp(Yu_m, Yd_m)
    mirror_sum_abs = abs(theta_m8_p + theta_m8_m)

    Yu_24 = mat_copy_mp(ops["m24_plus"]["Y"]["u"])
    Yd_24 = mat_copy_mp(ops["m24_plus"]["Y"]["d"])
    theta_m24_p = compute_bar_theta_Q_mp(Yu_24, Yd_24)

    # 10-trial random Haar SU(3)_Q x SU(3)_u x SU(3)_d scrambling gate
    rng = random.Random(2026112101)
    n_trials = 10
    max_su3_unit_err = mp.mpf(0)
    max_su3_det_err = mp.mpf(0)
    max_su3_theta_drift = mp.mpf(0)

    for _ in range(n_trials):
        UQ = random_haar_su3_householder_mp(rng)
        Uu = random_haar_su3_householder_mp(rng)
        Ud = random_haar_su3_householder_mp(rng)
        for U in (UQ, Uu, Ud):
            max_su3_unit_err = max(max_su3_unit_err, mat_frob_norm_mp(U.H * U - mp.eye(3)))
            max_su3_det_err = max(max_su3_det_err, abs(mp.det(U) - 1))
        th_scr = compute_bar_theta_Q_mp(UQ * Yu_p * Uu.H, UQ * Yd_p * Ud.H)
        max_su3_theta_drift = max(max_su3_theta_drift, abs(th_scr - theta_m8_p))

    su3_haar_ok = bool(
        max_su3_unit_err < mp.mpf(10) ** (-38)
        and max_su3_det_err < mp.mpf(10) ** (-38)
        and max_su3_theta_drift < mp.mpf(10) ** (-30)
    )

    # 6-perm positive diagonal right-handed eps_f scaling invariance
    phi = (1 + mp.sqrt(5)) / 2
    eps_u = phi ** (-8)
    eps_d = phi ** (-4)
    perm_thetas = {}
    max_perm_drift = mp.mpf(0)
    for perm in itertools.permutations((0, 1, 2)):
        Yu_eff = apply_bulk_profile_perm_mp(Yu_p, perm, eps_u)
        Yd_eff = apply_bulk_profile_perm_mp(Yd_p, perm, eps_d)
        th_p = compute_bar_theta_Q_mp(Yu_eff, Yd_eff)
        drift = abs(th_p - theta_m8_p)
        max_perm_drift = max(max_perm_drift, drift)
        perm_thetas[f"{perm[0]}{perm[1]}{perm[2]}"] = {
            "bar_theta_Q": mp.nstr(th_p, 25),
            "abs_drift": mp.nstr(drift, 8),
        }
    perm_scaling_ok = bool(max_perm_drift < mp.mpf(10) ** (-30))

    # Exact sympy.Rational Spin(10) 7D CS axion anomaly ratio E / N = 8 / 3
    species = spin10_16plus_species_table()
    ax = compute_cs_axion_anomaly_sympy(species)
    axion_ok = bool(
        ax["weyl_dim"] == 16
        and ax["E_gen"] == sp.Rational(16, 3)
        and ax["N_gen"] == sp.Rational(2)
        and ax["E_over_N"] == sp.Rational(8, 3)
        and ax["E_3gen"] / ax["N_3gen"] == sp.Rational(8, 3)
    )

    passed = bool(
        abs(theta_cp) < mp.mpf(10) ** (-30)
        and theta_e5 > mp.mpf(9) / 10
        and theta_e6 < -mp.mpf(6) / 10
        and (mp.mpf(15) / 1000 < theta_m8_p < mp.mpf(16) / 1000)
        and abs(theta_m24_p) > mp.mpf(9) / 10
        and mirror_sum_abs < mp.mpf(10) ** (-30)
        and su3_haar_ok
        and perm_scaling_ok
        and axion_ok
    )

    mp.mp.dps = old_dps
    return {
        "bar_theta_Q_tau_CP": mp.nstr(theta_cp, 12),
        "bar_theta_Q_m8_E5_only": mp.nstr(theta_e5, 25),
        "bar_theta_Q_m8_E6_only": mp.nstr(theta_e6, 25),
        "bar_theta_Q_m8_plus": mp.nstr(theta_m8_p, 25),
        "bar_theta_Q_m8_minus": mp.nstr(theta_m8_m, 25),
        "mirror_sum_abs_m8": mp.nstr(mirror_sum_abs, 10),
        "bar_theta_Q_m24_plus": mp.nstr(theta_m24_p, 25),
        "haar_su3_cube_10trials": {
            "n_trials": n_trials,
            "mpmath_dps": dps,
            "max_su3_unitarity_err": mp.nstr(max_su3_unit_err, 8),
            "max_su3_det_err": mp.nstr(max_su3_det_err, 8),
            "max_bar_theta_drift": mp.nstr(max_su3_theta_drift, 8),
            "pass": su3_haar_ok,
        },
        "perm6_positive_scaling_invariance": {
            "per_perm": perm_thetas,
            "max_abs_drift": mp.nstr(max_perm_drift, 8),
            "pass": perm_scaling_ok,
        },
        "cs_axion_spin10_16plus": {
            "weyl_dim": ax["weyl_dim"],
            "E_gen": str(ax["E_gen"]),
            "N_gen": str(ax["N_gen"]),
            "E_over_N": str(ax["E_over_N"]),
            "E_3gen": str(ax["E_3gen"]),
            "N_3gen": str(ax["N_3gen"]),
            "breakdown": ax["breakdown"],
            "pass": axion_ok,
        },
        "pass": passed,
    }


# =============================================================================
# SECTION 5: TASK OW12-B (SEESAW PMNS & FUKUGITA-YANAGIDA LEPTOGENESIS)
# =============================================================================

def run_task_ow12_b(ops, dps=45):
    old_dps = mp.mp.dps
    mp.mp.dps = dps

    phi = (1 + mp.sqrt(5)) / 2
    eps_e = phi ** (-12)

    Ye_p = mat_copy_mp(ops["m8_plus"]["Y"]["e"])
    Ynu_p = mat_copy_mp(ops["m8_plus"]["Y"]["nu"])
    MR00_p = mat_copy_mp(ops["m8_plus"]["Y"]["MR00"])

    Ynu_m = mat_copy_mp(ops["m8_minus"]["Y"]["nu"])
    MR00_m = mat_copy_mp(ops["m8_minus"]["Y"]["MR00"])

    # 1. Exact symmetry & disjoint Autonne-Takagi factorization of M_R^{(00)}
    mr00_sym_err = mat_frob_norm_mp(MR00_p - MR00_p.T)
    mr00_m_sym_err = mat_frob_norm_mp(MR00_m - MR00_m.T)
    tak_MR00_p = takagi_svd_mp(MR00_p)
    M1, M2, M3 = tak_MR00_p["M_asc"]
    mr00_hier_ok = bool(0 < M1 < M2 < M3)
    mr00_tak_ok = bool(
        mr00_sym_err < mp.mpf(10) ** (-35)
        and mr00_m_sym_err < mp.mpf(10) ** (-35)
        and tak_MR00_p["takagi_residual"] < mp.mpf(10) ** (-30)
        and tak_MR00_p["unit_err"] < mp.mpf(10) ** (-35)
        and mr00_hier_ok
    )

    # 2. Type-I Seesaw M_nu for both M_R^{(1)} = I_3 and M_R^{(00)}
    Mnu_I3 = Ynu_p * Ynu_p.T
    Mnu_00 = Ynu_p * (MR00_p ** -1) * Ynu_p.T
    tak_Mnu_I3 = takagi_svd_mp(Mnu_I3)
    tak_Mnu_00 = takagi_svd_mp(Mnu_00)

    dm_I3 = (tak_Mnu_I3["M_asc"][1] ** 2 - tak_Mnu_I3["M_asc"][0] ** 2) / (
        tak_Mnu_I3["M_asc"][2] ** 2 - tak_Mnu_I3["M_asc"][0] ** 2
    )
    dm_00 = (tak_Mnu_00["M_asc"][1] ** 2 - tak_Mnu_00["M_asc"][0] ** 2) / (
        tak_Mnu_00["M_asc"][2] ** 2 - tak_Mnu_00["M_asc"][0] ** 2
    )

    perms = list(itertools.permutations((0, 1, 2)))
    per_perm_I3 = {}
    per_perm_00 = {}
    qi_I3_checks = []
    ckm4_I3_t23_vals = []
    all6_00_checks = []
    all6_00_t23_vals = []
    all6_00_t12_vals = []
    all6_00_t13_vals = []

    for perm in perms:
        key = f"{perm[0]}{perm[1]}{perm[2]}"
        is_qi_heavy = bool(perm[2] == 1)
        is_ckm_strict = bool(perm[2] in (0, 2))
        Ye_eff = apply_bulk_profile_perm_mp(Ye_p, perm, eps_e)

        p_I3 = extract_pmns_from_takagi_mp(Ye_eff, tak_Mnu_I3)
        p_00 = extract_pmns_from_takagi_mp(Ye_eff, tak_Mnu_00)

        per_perm_I3[key] = {
            "perm": list(perm),
            "is_QI_heaviest": is_qi_heavy,
            "is_CKM_strict_4of6": is_ckm_strict,
            "sin2_theta12": mp.nstr(p_I3["sin2_theta12"], 25),
            "sin2_theta23": mp.nstr(p_I3["sin2_theta23"], 25),
            "sin2_theta13": mp.nstr(p_I3["sin2_theta13"], 25),
            "J_PMNS": mp.nstr(p_I3["J_PMNS"], 25),
            "abs_J_PMNS": mp.nstr(p_I3["abs_J_PMNS"], 25),
            "U_PMNS_abs": [[mp.nstr(p_I3["U_abs"][r][c], 18) for c in range(3)] for r in range(3)],
        }
        if is_qi_heavy:
            qi_I3_checks.append(bool(
                (mp.mpf(28) / 100 < p_I3["sin2_theta12"] < mp.mpf(33) / 100)
                and (mp.mpf(51) / 100 < p_I3["sin2_theta23"] < mp.mpf(53) / 100)
                and (mp.mpf(5) / 100 < p_I3["sin2_theta13"] < mp.mpf(7) / 100)
                and p_I3["abs_J_PMNS"] > mp.mpf(4) / 100
            ))
        if is_ckm_strict:
            ckm4_I3_t23_vals.append(p_I3["sin2_theta23"])

        per_perm_00[key] = {
            "perm": list(perm),
            "is_QI_heaviest": is_qi_heavy,
            "is_CKM_strict_4of6": is_ckm_strict,
            "sin2_theta12": mp.nstr(p_00["sin2_theta12"], 25),
            "sin2_theta23": mp.nstr(p_00["sin2_theta23"], 25),
            "sin2_theta13": mp.nstr(p_00["sin2_theta13"], 25),
            "J_PMNS": mp.nstr(p_00["J_PMNS"], 25),
            "abs_J_PMNS": mp.nstr(p_00["abs_J_PMNS"], 25),
            "U_PMNS_abs": [[mp.nstr(p_00["U_abs"][r][c], 18) for c in range(3)] for r in range(3)],
        }
        all6_00_t23_vals.append(p_00["sin2_theta23"])
        all6_00_t12_vals.append(p_00["sin2_theta12"])
        all6_00_t13_vals.append(p_00["sin2_theta13"])
        all6_00_checks.append(bool(
            p_00["sin2_theta23"] > mp.mpf(55) / 100
            and (mp.mpf(1) / 100 < p_00["sin2_theta12"] < mp.mpf(12) / 100)
            and (mp.mpf(5) / 100 < p_00["sin2_theta13"] < mp.mpf(11) / 100)
        ))

    mr_I3_ok = bool(
        (mp.mpf(5) / 1000 < dm_I3 < mp.mpf(7) / 1000)
        and len(qi_I3_checks) == 2
        and all(qi_I3_checks)
        and len(ckm4_I3_t23_vals) == 4
        and max(ckm4_I3_t23_vals) < mp.mpf(2) / 10
        and tak_Mnu_I3["takagi_residual"] < mp.mpf(10) ** (-30)
    )
    mr_00_ok = bool(
        (mp.mpf(26) / 1000 < dm_00 < mp.mpf(28) / 1000)
        and len(all6_00_checks) == 6
        and all(all6_00_checks)
        and tak_Mnu_00["takagi_residual"] < mp.mpf(10) ** (-30)
    )

    # 3. Exact 1-loop Fukugita-Yanagida leptogenesis at tau_*^+ and mirror tau_*^-
    fy_p = compute_leptogenesis_fy_mp(Ynu_p, MR00_p)
    fy_m = compute_leptogenesis_fy_mp(Ynu_m, MR00_m)
    eps1_mirror_sum = abs(fy_p["epsilon_1_norm"] + fy_m["epsilon_1_norm"])
    fy_ok = bool(
        (mp.mpf(5) / (10 ** 6) < fy_p["epsilon_1_norm"] < mp.mpf(6) / (10 ** 6))
        and eps1_mirror_sum < mp.mpf(10) ** (-25)
        and fy_m["tak_R"]["takagi_residual"] < mp.mpf(10) ** (-30)
    )

    # 4. Guardrail 3: 10-trial Haar U(3)_L x U(3)_e x U(3)_nu scrambling across ALL 6 perms
    rng = random.Random(2026112102)
    n_trials = 10
    max_haar_unit_err = mp.mpf(0)
    max_I3_dm_drift = mp.mpf(0)
    max_I3_U_drift = mp.mpf(0)
    max_I3_ang_drift = mp.mpf(0)
    max_I3_J_drift = mp.mpf(0)
    max_00_M_drift = mp.mpf(0)
    max_00_dm_drift = mp.mpf(0)
    max_00_U_drift = mp.mpf(0)
    max_00_ang_drift = mp.mpf(0)
    max_00_J_drift = mp.mpf(0)
    max_00_eps1_drift = mp.mpf(0)

    # Precompute reference baseline across all 6 perms
    Ye_eff_map = {perm: apply_bulk_profile_perm_mp(Ye_p, perm, eps_e) for perm in perms}
    base_I3_map = {perm: extract_pmns_from_takagi_mp(Ye_eff_map[perm], tak_Mnu_I3) for perm in perms}
    base_00_map = {perm: extract_pmns_from_takagi_mp(Ye_eff_map[perm], tak_Mnu_00) for perm in perms}
    I3_mat = mp.eye(3)

    for _ in range(n_trials):
        UL = random_haar_u3_householder_mp(rng)
        Ue = random_haar_u3_householder_mp(rng)
        Unu = random_haar_u3_householder_mp(rng)
        for U in (UL, Ue, Unu):
            max_haar_unit_err = max(max_haar_unit_err, mat_frob_norm_mp(U.H * U - I3_mat))

        Unu_conj = mat_conj_mp(Unu)
        Ynu_s = UL * Ynu_p * Unu.H
        MR_I3_s = Unu_conj * I3_mat * Unu.H
        MR_00_s = Unu_conj * MR00_p * Unu.H

        Mnu_I3_s = Ynu_s * (MR_I3_s ** -1) * Ynu_s.T
        Mnu_00_s = Ynu_s * (MR_00_s ** -1) * Ynu_s.T
        tak_I3_s = takagi_svd_mp(Mnu_I3_s)
        tak_00_s = takagi_svd_mp(Mnu_00_s)

        fy_s = compute_leptogenesis_fy_mp(Ynu_s, MR_00_s)
        max_00_eps1_drift = max(max_00_eps1_drift, abs(fy_s["epsilon_1_norm"] - fy_p["epsilon_1_norm"]))
        for k in range(3):
            max_00_M_drift = max(max_00_M_drift, abs(fy_s["tak_R"]["M_asc"][k] - tak_MR00_p["M_asc"][k]))

        for perm in perms:
            Ye_s = UL * Ye_eff_map[perm] * Ue.H
            o_I3 = extract_pmns_from_takagi_mp(Ye_s, tak_I3_s)
            b_I3 = base_I3_map[perm]
            max_I3_dm_drift = max(max_I3_dm_drift, abs(o_I3["dm21_over_dm31"] - b_I3["dm21_over_dm31"]))
            max_I3_J_drift = max(max_I3_J_drift, abs(o_I3["J_PMNS"] - b_I3["J_PMNS"]))
            for ang_k in ("sin2_theta12", "sin2_theta23", "sin2_theta13"):
                max_I3_ang_drift = max(max_I3_ang_drift, abs(o_I3[ang_k] - b_I3[ang_k]))
            for r in range(3):
                for c in range(3):
                    max_I3_U_drift = max(max_I3_U_drift, abs(o_I3["U_abs"][r][c] - b_I3["U_abs"][r][c]))

            o_00 = extract_pmns_from_takagi_mp(Ye_s, tak_00_s)
            b_00 = base_00_map[perm]
            max_00_dm_drift = max(max_00_dm_drift, abs(o_00["dm21_over_dm31"] - b_00["dm21_over_dm31"]))
            max_00_J_drift = max(max_00_J_drift, abs(o_00["J_PMNS"] - b_00["J_PMNS"]))
            for ang_k in ("sin2_theta12", "sin2_theta23", "sin2_theta13"):
                max_00_ang_drift = max(max_00_ang_drift, abs(o_00[ang_k] - b_00[ang_k]))
            for r in range(3):
                for c in range(3):
                    max_00_U_drift = max(max_00_U_drift, abs(o_00["U_abs"][r][c] - b_00["U_abs"][r][c]))

    max_haar_all = max(
        max_I3_dm_drift,
        max_I3_U_drift,
        max_I3_ang_drift,
        max_I3_J_drift,
        max_00_M_drift,
        max_00_dm_drift,
        max_00_U_drift,
        max_00_ang_drift,
        max_00_J_drift,
        max_00_eps1_drift,
    )
    haar_ok = bool(
        max_haar_unit_err < mp.mpf(10) ** (-38)
        and max_haar_all < mp.mpf(10) ** (-25)
    )

    passed = bool(mr00_tak_ok and mr_I3_ok and mr_00_ok and fy_ok and haar_ok)

    mp.mp.dps = old_dps
    return {
        "takagi_solver": "mp.svd_c_Autonne_Takagi_polar_phase_extraction_zero_eigh",
        "M_R_00_diagnostics": {
            "sym_err_plus": mp.nstr(mr00_sym_err, 8),
            "sym_err_minus": mp.nstr(mr00_m_sym_err, 8),
            "takagi_masses_asc": [mp.nstr(x, 25) for x in tak_MR00_p["M_asc"]],
            "M2_over_M1": mp.nstr(M2 / M1, 25),
            "M3_over_M1": mp.nstr(M3 / M1, 25),
            "takagi_residual": mp.nstr(tak_MR00_p["takagi_residual"], 8),
            "takagi_unitarity_err": mp.nstr(tak_MR00_p["unit_err"], 8),
            "w_offdiag_err": mp.nstr(tak_MR00_p["w_offdiag_err"], 8),
            "strict_hierarchy": mr00_hier_ok,
            "pass": mr00_tak_ok,
        },
        "seesaw_MR_I3": {
            "m_nu_asc": [mp.nstr(x, 25) for x in tak_Mnu_I3["M_asc"]],
            "dm21_over_dm31": mp.nstr(dm_I3, 25),
            "takagi_residual": mp.nstr(tak_Mnu_I3["takagi_residual"], 8),
            "per_perm": per_perm_I3,
            "QI_heaviest_2of6_pass": bool(len(qi_I3_checks) == 2 and all(qi_I3_checks)),
            "CKM_strict_4of6_max_sin2_theta23": mp.nstr(max(ckm4_I3_t23_vals), 20),
            "CKM_strict_4of6_sin2_theta23_lt_0p2": bool(max(ckm4_I3_t23_vals) < mp.mpf(2) / 10),
            "pass": mr_I3_ok,
        },
        "seesaw_MR_00": {
            "m_nu_asc": [mp.nstr(x, 25) for x in tak_Mnu_00["M_asc"]],
            "dm21_over_dm31": mp.nstr(dm_00, 25),
            "takagi_residual": mp.nstr(tak_Mnu_00["takagi_residual"], 8),
            "per_perm": per_perm_00,
            "all6_min_sin2_theta23": mp.nstr(min(all6_00_t23_vals), 20),
            "all6_sin2_theta12_range": [mp.nstr(min(all6_00_t12_vals), 20), mp.nstr(max(all6_00_t12_vals), 20)],
            "all6_sin2_theta13_range": [mp.nstr(min(all6_00_t13_vals), 20), mp.nstr(max(all6_00_t13_vals), 20)],
            "pass": mr_00_ok,
        },
        "leptogenesis_fukugita_yanagida": {
            "sigma_max_Y_nu_plus": mp.nstr(fy_p["sigma_max_Y_nu"], 25),
            "H_hat_11_plus": mp.nstr(fy_p["H_hat_11"], 25),
            "x_vals_Mj_over_M1_sq_plus": [mp.nstr(x, 25) for x in fy_p["x_vals"]],
            "f_x_vals_plus": [mp.nstr(x, 25) for x in fy_p["f_vals"]],
            "epsilon_1_raw_plus": mp.nstr(fy_p["epsilon_1_raw"], 25),
            "epsilon_1_norm_plus": mp.nstr(fy_p["epsilon_1_norm"], 25),
            "sigma_max_Y_nu_minus": mp.nstr(fy_m["sigma_max_Y_nu"], 25),
            "epsilon_1_raw_minus": mp.nstr(fy_m["epsilon_1_raw"], 25),
            "epsilon_1_norm_minus": mp.nstr(fy_m["epsilon_1_norm"], 25),
            "mirror_sum_abs_eps1_norm": mp.nstr(eps1_mirror_sum, 10),
            "pass": fy_ok,
        },
        "haar_u3_cube_10trials_all6perms": {
            "n_trials": n_trials,
            "mpmath_dps": dps,
            "max_haar_unitarity_err": mp.nstr(max_haar_unit_err, 8),
            "MR_I3_max_dm_ratio_drift": mp.nstr(max_I3_dm_drift, 8),
            "MR_I3_max_U_abs_drift": mp.nstr(max_I3_U_drift, 8),
            "MR_I3_max_angles_drift": mp.nstr(max_I3_ang_drift, 8),
            "MR_I3_max_J_PMNS_drift": mp.nstr(max_I3_J_drift, 8),
            "MR_00_max_takagi_mass_drift": mp.nstr(max_00_M_drift, 8),
            "MR_00_max_dm_ratio_drift": mp.nstr(max_00_dm_drift, 8),
            "MR_00_max_U_abs_drift": mp.nstr(max_00_U_drift, 8),
            "MR_00_max_angles_drift": mp.nstr(max_00_ang_drift, 8),
            "MR_00_max_J_PMNS_drift": mp.nstr(max_00_J_drift, 8),
            "MR_00_max_eps1_norm_drift": mp.nstr(max_00_eps1_drift, 8),
            "max_overall_drift": mp.nstr(max_haar_all, 8),
            "pass": haar_ok,
        },
        "pass": passed,
    }


# =============================================================================
# SECTION 6: TASK OW12-C (7D (T_{3R}, B - L) DECOMPOSITION & INTER-SECTOR RATIOS)
# =============================================================================

def run_task_ow12_c(ops, dps=45):
    old_dps = mp.mp.dps
    mp.mp.dps = dps

    # 1. Exact sympy.Rational Spin(10) identity 6 Y == 6 T_{3R} + 3 (B - L)
    species = spin10_16plus_species_table()
    decomp_records = {}
    decomp_checks = []
    for sp_rec in species:
        six_Y_calc = 6 * sp_rec["T3R"] + 3 * sp_rec["B_minus_L"]
        is_lh = bool(sp_rec["d2"] == 2)
        id_ok = bool(six_Y_calc == sp_rec["six_Y_expected"])
        t3r_ok = bool(sp_rec["T3R"] == 0) if is_lh else bool(abs(sp_rec["T3R"]) == sp.Rational(1, 2))
        decomp_checks.append(bool(id_ok and t3r_ok))
        decomp_records[sp_rec["name"]] = {
            "chirality_rep": sp_rec["chirality_rep"],
            "T3R": str(sp_rec["T3R"]),
            "B_minus_L": str(sp_rec["B_minus_L"]),
            "six_T3R_plus_three_BmL": str(six_Y_calc),
            "six_Y_expected": str(sp_rec["six_Y_expected"]),
            "identity_exact": id_ok,
            "T3R_vanishes_iff_LH_doublet": t3r_ok,
        }
    decomp_ok = bool(len(decomp_checks) == 6 and all(decomp_checks))

    # 2. Exact uniform LH doublet scaling invariance & tan(beta) = 1 inter-sector ratios
    phi = (1 + mp.sqrt(5)) / 2
    eps_u = phi ** (-8)
    eps_d = phi ** (-4)
    eps_e = phi ** (-12)
    c_QL = phi ** (-2)
    c_LL = phi ** (-6)
    expected_ytau_yb_factor = phi ** (-4)

    Yu_p = mat_copy_mp(ops["m8_plus"]["Y"]["u"])
    Yd_p = mat_copy_mp(ops["m8_plus"]["Y"]["d"])
    Ye_p = mat_copy_mp(ops["m8_plus"]["Y"]["e"])
    Ynu_p = mat_copy_mp(ops["m8_plus"]["Y"]["nu"])
    MR00_p = mat_copy_mp(ops["m8_plus"]["Y"]["MR00"])

    Mnu_I3 = Ynu_p * Ynu_p.T
    Mnu_00 = Ynu_p * (MR00_p ** -1) * Ynu_p.T
    tak_I3 = takagi_svd_mp(Mnu_I3)
    tak_00 = takagi_svd_mp(Mnu_00)
    fy_base = compute_leptogenesis_fy_mp(Ynu_p, MR00_p)

    Ynu_lh = c_LL * Ynu_p
    Mnu_I3_lh = Ynu_lh * Ynu_lh.T
    Mnu_00_lh = Ynu_lh * (MR00_p ** -1) * Ynu_lh.T
    tak_I3_lh = takagi_svd_mp(Mnu_I3_lh)
    tak_00_lh = takagi_svd_mp(Mnu_00_lh)
    fy_lh = compute_leptogenesis_fy_mp(Ynu_lh, MR00_p)

    max_intra_drift = mp.mpf(0)
    max_ckm_drift = mp.mpf(0)
    max_jcp_drift = mp.mpf(0)
    max_pmns_I3_drift = mp.mpf(0)
    max_pmns_00_drift = mp.mpf(0)
    max_jpmns_drift = mp.mpf(0)
    max_theta_drift = mp.mpf(0)
    max_eps1_drift = abs(fy_lh["epsilon_1_norm"] - fy_base["epsilon_1_norm"])
    max_ytau_yb_fac_err = mp.mpf(0)

    inter_records = {}
    b_tau_count = 0
    all6_mu_s = []
    ckm4_mu_s = []
    all6_e_d = []

    for perm in itertools.permutations((0, 1, 2)):
        key = f"{perm[0]}{perm[1]}{perm[2]}"
        is_ckm_strict = bool(perm[2] in (0, 2))

        Yu_eff = apply_bulk_profile_perm_mp(Yu_p, perm, eps_u)
        Yd_eff = apply_bulk_profile_perm_mp(Yd_p, perm, eps_d)
        Ye_eff = apply_bulk_profile_perm_mp(Ye_p, perm, eps_e)

        Yu_lh = c_QL * Yu_eff
        Yd_lh = c_QL * Yd_eff
        Ye_lh = c_LL * Ye_eff

        ckm_0 = extract_ckm_mp(Yu_eff, Yd_eff)
        ckm_1 = extract_ckm_mp(Yu_lh, Yd_lh)
        se_0 = svd_sector_ascending_mp(Ye_eff)
        se_1 = svd_sector_ascending_mp(Ye_lh)

        pmns_I3_0 = extract_pmns_from_takagi_mp(Ye_eff, tak_I3)
        pmns_I3_1 = extract_pmns_from_takagi_mp(Ye_lh, tak_I3_lh)
        pmns_00_0 = extract_pmns_from_takagi_mp(Ye_eff, tak_00)
        pmns_00_1 = extract_pmns_from_takagi_mp(Ye_lh, tak_00_lh)

        th_0 = compute_bar_theta_Q_mp(Yu_eff, Yd_eff)
        th_1 = compute_bar_theta_Q_mp(Yu_lh, Yd_lh)
        max_theta_drift = max(max_theta_drift, abs(th_1 - th_0))

        for s0, s1 in ((ckm_0["u"], ckm_1["u"]), (ckm_0["d"], ckm_1["d"]), (se_0, se_1)):
            for rk in ("r23", "r13", "r12"):
                max_intra_drift = max(max_intra_drift, abs(s1[rk] - s0[rk]))
        max_intra_drift = max(
            max_intra_drift,
            abs(pmns_I3_1["dm21_over_dm31"] - pmns_I3_0["dm21_over_dm31"]),
            abs(pmns_00_1["dm21_over_dm31"] - pmns_00_0["dm21_over_dm31"]),
        )
        for r in range(3):
            for c in range(3):
                max_ckm_drift = max(max_ckm_drift, abs(ckm_1["V_abs"][r][c] - ckm_0["V_abs"][r][c]))
                max_pmns_I3_drift = max(max_pmns_I3_drift, abs(pmns_I3_1["U_abs"][r][c] - pmns_I3_0["U_abs"][r][c]))
                max_pmns_00_drift = max(max_pmns_00_drift, abs(pmns_00_1["U_abs"][r][c] - pmns_00_0["U_abs"][r][c]))
        for ang_k in ("sin2_theta12", "sin2_theta23", "sin2_theta13"):
            max_pmns_I3_drift = max(max_pmns_I3_drift, abs(pmns_I3_1[ang_k] - pmns_I3_0[ang_k]))
            max_pmns_00_drift = max(max_pmns_00_drift, abs(pmns_00_1[ang_k] - pmns_00_0[ang_k]))
        max_jcp_drift = max(max_jcp_drift, abs(ckm_1["J_CP"] - ckm_0["J_CP"]))
        max_jpmns_drift = max(
            max_jpmns_drift,
            abs(pmns_I3_1["J_PMNS"] - pmns_I3_0["J_PMNS"]),
            abs(pmns_00_1["J_PMNS"] - pmns_00_0["J_PMNS"]),
        )

        # Inter-sector ratios at tan(beta) = 1
        su = ckm_0["u"]["svs_asc"]
        sd = ckm_0["d"]["svs_asc"]
        se = se_0["svs_asc"]
        yt_yb = su[2] / sd[2]
        ytau_yb = se[2] / sd[2]
        ymu_ys = se[1] / sd[1]
        ye_yd = se[0] / sd[0]

        ytau_yb_lh = se_1["svs_asc"][2] / ckm_1["d"]["svs_asc"][2]
        fac_ratio = ytau_yb_lh / ytau_yb
        max_ytau_yb_fac_err = max(max_ytau_yb_fac_err, abs(fac_ratio - expected_ytau_yb_factor))

        b_tau_ok = bool(mp.mpf(9) / 10 < ytau_yb < mp.mpf(14) / 10)
        if b_tau_ok:
            b_tau_count += 1
        all6_mu_s.append(ymu_ys)
        if is_ckm_strict:
            ckm4_mu_s.append(ymu_ys)
        all6_e_d.append(ye_yd)

        inter_records[key] = {
            "perm": list(perm),
            "is_CKM_strict_4of6": is_ckm_strict,
            "y_t_over_y_b": mp.nstr(yt_yb, 25),
            "y_tau_over_y_b": mp.nstr(ytau_yb, 25),
            "y_mu_over_y_s": mp.nstr(ymu_ys, 25),
            "y_e_over_y_d": mp.nstr(ye_yd, 25),
            "b_tau_in_0p9_to_1p4": b_tau_ok,
            "y_mu_over_y_s_lt_0p05": bool(ymu_ys < mp.mpf(5) / 100),
            "y_mu_over_y_s_lt_0p02": bool(ymu_ys < mp.mpf(2) / 100),
            "y_e_over_y_d_lt_0p001": bool(ye_yd < mp.mpf(1) / 1000),
        }

    max_lh_inv_drift = max(
        max_intra_drift,
        max_ckm_drift,
        max_jcp_drift,
        max_pmns_I3_drift,
        max_pmns_00_drift,
        max_jpmns_drift,
        max_theta_drift,
        max_eps1_drift,
    )
    lh_scaling_ok = bool(
        max_lh_inv_drift < mp.mpf(10) ** (-30)
        and max_ytau_yb_fac_err < mp.mpf(10) ** (-30)
    )
    inter_ok = bool(
        b_tau_count >= 4
        and max(all6_mu_s) < mp.mpf(5) / 100
        and max(ckm4_mu_s) < mp.mpf(2) / 100
        and max(all6_e_d) < mp.mpf(1) / 1000
    )
    passed = bool(decomp_ok and lh_scaling_ok and inter_ok)

    mp.mp.dps = old_dps
    return {
        "spin10_T3R_BmL_decomposition": {
            "species": decomp_records,
            "pass": decomp_ok,
        },
        "lh_uniform_scaling_invariance": {
            "c_QL": mp.nstr(c_QL, 25),
            "c_LL": mp.nstr(c_LL, 25),
            "expected_y_tau_over_y_b_factor_phi_m4": mp.nstr(expected_ytau_yb_factor, 25),
            "max_intra_ratio_drift": mp.nstr(max_intra_drift, 8),
            "max_ckm_drift": mp.nstr(max_ckm_drift, 8),
            "max_jcp_drift": mp.nstr(max_jcp_drift, 8),
            "max_pmns_I3_drift": mp.nstr(max_pmns_I3_drift, 8),
            "max_pmns_00_drift": mp.nstr(max_pmns_00_drift, 8),
            "max_jpmns_drift": mp.nstr(max_jpmns_drift, 8),
            "max_bar_theta_drift": mp.nstr(max_theta_drift, 8),
            "max_eps1_norm_drift": mp.nstr(max_eps1_drift, 8),
            "max_overall_invariance_drift": mp.nstr(max_lh_inv_drift, 8),
            "max_ytau_over_yb_factor_err": mp.nstr(max_ytau_yb_fac_err, 8),
            "pass": lh_scaling_ok,
        },
        "inter_sector_ratios_tan_beta_1": {
            "per_perm": inter_records,
            "b_tau_proximity_count": b_tau_count,
            "all6_max_y_mu_over_y_s": mp.nstr(max(all6_mu_s), 20),
            "ckm_strict_4of6_max_y_mu_over_y_s": mp.nstr(max(ckm4_mu_s), 20),
            "all6_max_y_e_over_y_d": mp.nstr(max(all6_e_d), 20),
            "pass": inter_ok,
        },
        "pass": passed,
    }


# =============================================================================
# SECTION 7: TASK OW12-D (4 / 4 PLANTED-FAULT SELF-CHECKS PF-OW12-1..4)
# =============================================================================

def run_task_ow12_d(ops, dps=45):
    old_dps = mp.mp.dps
    mp.mp.dps = dps

    Yu_p = mat_copy_mp(ops["m8_plus"]["Y"]["u"])
    Yd_p = mat_copy_mp(ops["m8_plus"]["Y"]["d"])
    Ynu_p = mat_copy_mp(ops["m8_plus"]["Y"]["nu"])
    MR00_p = mat_copy_mp(ops["m8_plus"]["Y"]["MR00"])
    Yq10_p = mat_copy_mp(ops["m8_plus"]["Y"]["q10"])

    # PF-OW12-1: Anomalous U(1)_A chiral phase exp(i / 2) I_3 on Y_u shifts arg det by +3 / 2
    theta_base = compute_bar_theta_Q_mp(Yu_p, Yd_p)
    phase_u1a = mp.exp(mp.mpc(0, 1) / 2)
    theta_fault = compute_bar_theta_Q_mp(phase_u1a * Yu_p, Yd_p)
    delta_theta = theta_fault - theta_base
    err_3_2 = abs(delta_theta - mp.mpf(3) / 2)
    pf1_caught = bool(err_3_2 < mp.mpf(10) ** (-30) and abs(delta_theta) > 1)

    # PF-OW12-2: Purely real symmetric Re(M_R^{(00)}) + purely real Re(Y_nu) drives eps_1 == 0
    MR_real = mat_real_mp(MR00_p)
    Ynu_real = mat_real_mp(Ynu_p)
    fy_real = compute_leptogenesis_fy_mp(Ynu_real, MR_real)
    pf2_caught = bool(
        abs(fy_real["epsilon_1_norm"]) < mp.mpf(10) ** (-30)
        and fy_real["tak_R"]["takagi_residual"] < mp.mpf(10) ** (-30)
    )

    # PF-OW12-3: Wrong quark twist w_L = +1 (Y_u) instead of lepton twist w_L = -3 (Y_nu) under M_R = I_3
    tak_nu_I3 = takagi_svd_mp(Ynu_p * Ynu_p.T)
    dm_nu_I3 = (tak_nu_I3["M_asc"][1] ** 2 - tak_nu_I3["M_asc"][0] ** 2) / (
        tak_nu_I3["M_asc"][2] ** 2 - tak_nu_I3["M_asc"][0] ** 2
    )
    tak_u_I3 = takagi_svd_mp(Yu_p * Yu_p.T)
    dm_u_I3 = (tak_u_I3["M_asc"][1] ** 2 - tak_u_I3["M_asc"][0] ** 2) / (
        tak_u_I3["M_asc"][2] ** 2 - tak_u_I3["M_asc"][0] ** 2
    )
    tak_q10_I3 = takagi_svd_mp(Yq10_p * Yq10_p.T)
    dm_q10_I3 = (tak_q10_I3["M_asc"][1] ** 2 - tak_q10_I3["M_asc"][0] ** 2) / (
        tak_q10_I3["M_asc"][2] ** 2 - tak_q10_I3["M_asc"][0] ** 2
    )
    pf3_caught = bool(
        (mp.mpf(5) / 1000 < dm_nu_I3 < mp.mpf(7) / 1000)
        and dm_u_I3 > mp.mpf(3) / 10
    )

    # PF-OW12-4: Omitting e^c from 16_+ shifts E / N from 8 / 3 to 13 / 6
    species_no_ec = [s for s in spin10_16plus_species_table() if s["name"] != "e^c"]
    ax_fault = compute_cs_axion_anomaly_sympy(species_no_ec)
    pf4_caught = bool(
        ax_fault["E_gen"] == sp.Rational(13, 3)
        and ax_fault["N_gen"] == sp.Rational(2)
        and ax_fault["E_over_N"] == sp.Rational(13, 6)
        and ax_fault["E_over_N"] != sp.Rational(8, 3)
    )

    caught_list = [pf1_caught, pf2_caught, pf3_caught, pf4_caught]
    caught_count = sum(1 for x in caught_list if x)
    passed = bool(caught_count == 4)

    mp.mp.dps = old_dps
    return {
        "PF_OW12_1_anomalous_U1A_phase": {
            "bar_theta_Q_base": mp.nstr(theta_base, 25),
            "bar_theta_Q_fault": mp.nstr(theta_fault, 25),
            "shift": mp.nstr(delta_theta, 25),
            "abs_err_from_3_over_2": mp.nstr(err_3_2, 8),
            "caught": pf1_caught,
        },
        "PF_OW12_2_real_MR_and_real_Ynu": {
            "takagi_residual": mp.nstr(fy_real["tak_R"]["takagi_residual"], 8),
            "epsilon_1_norm_real": mp.nstr(fy_real["epsilon_1_norm"], 12),
            "caught": pf2_caught,
        },
        "PF_OW12_3_wrong_quark_twist_Yu": {
            "dm21_over_dm31_Y_nu": mp.nstr(dm_nu_I3, 25),
            "dm21_over_dm31_Y_u": mp.nstr(dm_u_I3, 25),
            "dm21_over_dm31_qL1_qR0_diag": mp.nstr(dm_q10_I3, 25),
            "caught": pf3_caught,
        },
        "PF_OW12_4_omit_ec_from_16plus": {
            "weyl_dim_fault": ax_fault["weyl_dim"],
            "E_gen_fault": str(ax_fault["E_gen"]),
            "N_gen_fault": str(ax_fault["N_gen"]),
            "E_over_N_fault": str(ax_fault["E_over_N"]),
            "caught": pf4_caught,
        },
        "caught_count": caught_count,
        "total_faults": 4,
        "pass": passed,
    }


# =============================================================================
# MAIN ENTRYPOINT
# =============================================================================

def main():
    t0 = time.time()
    script_path = os.path.abspath(__file__)
    hygiene = audit_script_hygiene(script_path)

    ops, engine_diag = build_all_ow12_operators(dps=55)
    ow12_a = run_task_ow12_a(ops, dps=45)
    ow12_b = run_task_ow12_b(ops, dps=45)
    ow12_c = run_task_ow12_c(ops, dps=45)
    ow12_d = run_task_ow12_d(ops, dps=45)

    elapsed_int_ms = int(round((time.time() - t0) * 1000))
    overall_pass = bool(
        hygiene["hygiene_pass"]
        and engine_diag["engine_pass"]
        and ow12_a["pass"]
        and ow12_b["pass"]
        and ow12_c["pass"]
        and ow12_d["pass"]
    )

    report = {
        "card_id": "AGY-002_A2-OW12",
        "erratum_id": "AGY-002_A2-OW12-ERRATUM-1",
        "role": "Independent_Cold_Room_Zero_Trust_Referee",
        "empirical_firewall": "0_of_19",
        "elapsed_ms": elapsed_int_ms,
        "hygiene": hygiene,
        "engine_L2_gl6_jtheta": engine_diag,
        "OW12_A": ow12_a,
        "OW12_B": ow12_b,
        "OW12_C": ow12_c,
        "OW12_D": ow12_d,
        "overall_pass": overall_pass,
    }

    out_path = os.path.join(os.path.dirname(script_path), "referee_a2_ow12_out.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
        fh.write("\n")

    print(
        f"A2-OW12 Cold-Room Referee complete in {elapsed_int_ms} ms | "
        f"overall_pass={overall_pass} | "
        f"hygiene={hygiene['hygiene_pass']} engine={engine_diag['engine_pass']} "
        f"A={ow12_a['pass']} B={ow12_b['pass']} C={ow12_c['pass']} D={ow12_d['pass']}"
    )


if __name__ == "__main__":
    main()
