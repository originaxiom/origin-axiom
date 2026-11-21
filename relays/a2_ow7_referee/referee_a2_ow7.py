r"""
Independent Cold-Room Zero-Trust Referee for Card AGY-002_A2-OW7 (and Erratum 1).

Resolving the Flavor Hierarchy-vs-CKM/CP Trade-Off:
  - OW7-A (Guardrail 4 Literature Benchmark Gate):
      * Exact 2-loop SM RGEs (t = ln(mu / mu_0), Machacek-Vaughn / Luo-Xiao /
        Buttazzo App. A) integrated via adaptive 8th-order Dormand-Prince
        (scipy.integrate.solve_ivp, method="DOP853") and independently
        cross-checked against 35-dps mpmath 3-stage implicit Gauss-Legendre
        RK6 (GL6) on Buttazzo et al. (1307.3536, Table 3 NNLO MS-bar inputs
        at M_t = 173.34 GeV evolved to M_Pl = 1.2209e19 GeV).
      * Exact 3x3 complex matrix SM (1H) and Type-II 2HDM (2H) RGEs (exact
        2-loop gauge + left-covariant 1-loop (Y Y^dag) Y Yukawa ordering,
        explicitly verified under random Haar Q_L -> U_L Q_L rotations) on
        Xing-Zhou (1804.01925, M_Z -> 10^14 GeV), certifying opposite SM vs
        Type-II 2HDM |V_cb| and |J_CP| running signs with frozen |V_us|.
  - OW7-B (Exact RG Rigidity Theorem on Open-Weave A2-OW6 UV Yukawas, 0 of 19):
      * Disjoint 3-stage GL6 order-20 extrapolated Fuchsian L_2(tau) solver
        plus branch-cut-free mpmath.jtheta E[5] + E[6] Regime-4b Yukawas at
        m = 8 and m = 24.
      * Downward evolution across 14 decades (dt = -14 ln(10)) for all 8
        trajectories (m in {8, 24}, SM vs 2HDM_II, y_UV in {7/10, 3/2},
        g_UV = 52/100) via 35-dps mpmath implicit GL6 (preserving m=24's
        |J_CP| ~ 10^-16 well above machine floor), cross-checked against
        adaptive DOP853 on m = 8 and step-halving on m = 24.
  - OW7-C (Exact 7D Bulk Right-Handed QR-Decoupling Across All 6/6 Permutations
           + 10-Trial 45-dps Haar Gate, 0 of 19):
      * 45-dps mpmath Householder-reflection QR (disjoint from Gram-Schmidt)
        and mp.svd_c in physical ascending (u, c, t) x (d, s, b) ordering.
      * Zero-parameter hypercharge-weighted geodesic profile
        D_{R,f} = diag(eps_f^2, eps_f, 1), eps_f = phi^(-2 |6 Y_R|) with
        |6 Y_R| = (4, 2, 6), across all 6/6 S_3 column permutations plus
        Erratum 1 universal (> 84/100) and 4/6 hierarchical (> 98/100 and
        |V_us| > |V_cb| > |V_ub| > 0) checks, finite and asymptotic (eps/1000)
        QR-limit convergence, 10-trial 45-dps Haar U(3)^5 gate, and
        asymmetric covering controls (Y_u@8, Y_d@24) & (Y_u@24, Y_d@8).
  - OW7-D (4/4 Planted Faults PF-OW7-1..4).

Hygiene:
  - 0 of 19 empirical inputs for all model predictions (published Buttazzo &
    Xing-Zhou inputs live solely inside the isolated Guardrail 4 gate OW7-A).
  - 0 float or complex AST literals.
  - 0 frontier/ or verify_a2_ow7* imports.
  - 0 hardcoded truth flags.
"""

import ast
import hashlib
import itertools
import json
import math
import os
import random
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp


# =============================================================================
# SECTION 0: CUSTODY & AST HYGIENE SELF-AUDIT
# =============================================================================

def audit_script_hygiene(script_path):
    with open(script_path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src, filename=script_path)
    bad_literals = []
    bad_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad_literals.append((getattr(node, "lineno", -1), repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if "frontier" in alias.name or "a2_ow7" in alias.name or "verify_a2" in alias.name:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "frontier" in mod or "a2_ow7" in mod or "verify_a2" in mod:
                bad_imports.append(mod)
    sha = hashlib.sha256(src.encode("utf-8")).hexdigest()
    manifest_path = os.path.join(os.path.dirname(script_path), "SCRIPT_SHA256.txt")
    manifest_match = None
    manifest_sha = None
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as mf:
            parts = mf.read().strip().split()
            if parts:
                manifest_sha = parts[0]
                manifest_match = (manifest_sha == sha)
    return {
        "script_sha256": sha,
        "manifest_sha256": manifest_sha,
        "manifest_match": manifest_match,
        "float_or_complex_ast_literals": bad_literals,
        "float_or_complex_literal_count": len(bad_literals),
        "forbidden_imports": bad_imports,
        "forbidden_import_count": len(bad_imports),
        "hygiene_pass": bool(len(bad_literals) == 0 and len(bad_imports) == 0),
    }


# =============================================================================
# SECTION 1: DISJOINT LINEAR ALGEBRA (45-DPS HOUSEHOLDER QR, SVD_C, HAAR U(3))
# =============================================================================

def mat_frob_norm_mp(A):
    acc = mp.mpf(0)
    for r in range(A.rows):
        for c in range(A.cols):
            acc += abs(A[r, c]) ** 2
    return mp.sqrt(acc)


def householder_qr_mp(A):
    """
    Complex Householder-reflection QR factorization A = Q * R in current mp.mp.dps
    (strictly disjoint from Gram-Schmidt), with column/row phase normalization so
    that diag(R) is real non-negative (Mezzadri canonical phase convention).
    """
    n = A.rows
    m = A.cols
    R = mp.matrix([[mp.mpc(A[r, c]) for c in range(m)] for r in range(n)])
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

        # Left multiply R[k:, k:] by H = I - beta * v * v^H
        for j in range(k, m):
            dot = sum(mp.conj(v[idx]) * R[k + idx, j] for idx in range(n - k))
            w = beta * dot
            for idx in range(n - k):
                R[k + idx, j] -= w * v[idx]
        # Force exact sub-diagonal zeros in column k after reflection
        for i in range(k + 1, n):
            R[i, k] = mp.mpc(0)

        # Right multiply Q[:, k:] by H = I - beta * v * v^H
        for i in range(n):
            dot = sum(Q[i, k + idx] * v[idx] for idx in range(n - k))
            w = beta * dot
            for idx in range(n - k):
                Q[i, k + idx] -= w * mp.conj(v[idx])

    # Phase-normalize diagonal of R to real positive (Mezzadri convention)
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


def svd_sector_ascending_mp(Y):
    """
    Compute exact SVD Y = U * diag(S) * Vh via mp.svd_c and reorder into
    physical ascending mass order (sigma_1 <= sigma_2 <= sigma_3):
      index 0 = 1st gen (lightest), 1 = 2nd gen, 2 = 3rd gen (heaviest).
    """
    U_raw, S_raw, Vh_raw = mp.svd_c(Y)
    s_list = [mp.re(S_raw[i]) for i in range(3)]
    idx = sorted(range(3), key=lambda i: s_list[i])
    svs_asc = [s_list[i] for i in idx]
    U_asc = mp.matrix([[U_raw[r, idx[c]] for c in range(3)] for r in range(3)])
    Vh_asc = mp.matrix([[Vh_raw[idx[r], c] for c in range(3)] for r in range(3)])
    V_asc = Vh_asc.H

    # Reconstruction and unitarity diagnostics
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
        "lams_asc": [x * x for x in svs_asc],
        "U_asc": U_asc,
        "V_asc": V_asc,
        "Vh_asc": Vh_asc,
        "H": Y * Y.H,
        "r23": r23,
        "r13": r13,
        "r12": r12,
        "recon_err": recon_err,
        "unit_err": unit_err,
    }


def extract_flavor_observables_svd_mp(Yu, Yd, Ye=None):
    """
    Extract physical ascending-order observables via mp.svd_c plus
    basis-invariant Jarlskog commutator determinant J_det_norm and identity check.
    """
    su = svd_sector_ascending_mp(Yu)
    sd = svd_sector_ascending_mp(Yd)
    se = svd_sector_ascending_mp(Ye) if Ye is not None else None

    Hu, Hd = su["H"], sd["H"]
    comm = Hu * Hd - Hd * Hu
    det_comm = mp.det(comm)
    tr_u = mp.re(Hu[0, 0] + Hu[1, 1] + Hu[2, 2])
    tr_d = mp.re(Hd[0, 0] + Hd[1, 1] + Hd[2, 2])
    J_det_raw = mp.im(det_comm)
    J_det_re_err = abs(mp.re(det_comm))
    J_det_norm = J_det_raw / ((tr_u ** 3) * (tr_d ** 3))

    V = su["U_asc"].H * sd["U_asc"]
    V_abs = [[abs(V[r, c]) for c in range(3)] for r in range(3)]
    # Standard physical Jarlskog invariant J_CP = Im(V_ud V_cs V_us^* V_cd^*)
    J_CP = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))

    lu = su["lams_asc"]
    ld = sd["lams_asc"]
    Delta_u = (lu[2] - lu[1]) * (lu[2] - lu[0]) * (lu[1] - lu[0])
    Delta_d = (ld[2] - ld[1]) * (ld[2] - ld[0]) * (ld[1] - ld[0])
    J_CP_from_det = (
        abs(J_det_raw / (2 * Delta_u * Delta_d))
        if (Delta_u != 0 and Delta_d != 0)
        else mp.mpf(0)
    )
    J_CP_id_err = abs(abs(J_CP) - J_CP_from_det)

    rel_ed_23 = None
    if se is not None and sd["r23"] > 0:
        rel_ed_23 = abs(se["r23"] - sd["r23"]) / sd["r23"]

    max_svd_err = max(
        su["recon_err"], sd["recon_err"], su["unit_err"], sd["unit_err"],
        (se["recon_err"] if se is not None else mp.mpf(0)),
        (se["unit_err"] if se is not None else mp.mpf(0)),
    )
    return {
        "u": su,
        "d": sd,
        "e": se,
        "V": V,
        "V_abs": V_abs,
        "V_us": V_abs[0][1],
        "V_cb": V_abs[1][2],
        "V_ub": V_abs[0][2],
        "V_ts": V_abs[2][1],
        "J_CP": J_CP,
        "J_det_norm": J_det_norm,
        "J_det_re_err": J_det_re_err,
        "J_CP_identity_err": J_CP_id_err,
        "rel_ed_23": rel_ed_23,
        "max_svd_err": max_svd_err,
    }


def extract_flavor_observables_np(Yu, Yd, Ye=None):
    """Fast numpy float64 SVD extraction in physical ascending order (for DOP853)."""
    def svd_asc_np(Y):
        U, S, _ = np.linalg.svd(Y)
        idx = np.argsort(S)
        s_asc = S[idx]
        U_asc = U[:, idx]
        return {
            "svs_asc": s_asc,
            "U_asc": U_asc,
            "r23": float(s_asc[1] / s_asc[2]),
            "r13": float(s_asc[0] / s_asc[2]),
            "r12": float(s_asc[0] / s_asc[1]),
        }

    su = svd_asc_np(Yu)
    sd = svd_asc_np(Yd)
    se = svd_asc_np(Ye) if Ye is not None else None
    V = su["U_asc"].conj().T @ sd["U_asc"]
    V_abs = np.abs(V)
    J_CP = float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))
    return {
        "u": su,
        "d": sd,
        "e": se,
        "V_abs": V_abs,
        "V_us": float(V_abs[0, 1]),
        "V_cb": float(V_abs[1, 2]),
        "V_ub": float(V_abs[0, 2]),
        "J_CP": J_CP,
    }


# =============================================================================
# SECTION 2: DISJOINT GL6 ORDER-20 L_2(tau) & MP.JTHETA E[5]+E[6] YUKAWAS
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
    return [mp.mpf(M[i][K + 1].numerator) / mp.mpf(M[i][K + 1].denominator) for i in range(K + 1)]


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
            M = [[(1 if i == k else 0) + dz2 * A2[i][k] * qs[k] for k in range(3)] for i in range(3)]
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
        J = [[mp.im(dtA), mp.re(dtA)], [mp.im(dtB), mp.re(dtB)], [mp.im(dtAB), mp.re(dtAB)]]
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
        J = [[mp.im(dtA), mp.re(dtA)], [mp.im(dtB), mp.re(dtB)], [mp.im(dtAB), mp.re(dtAB)]]
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
        ck[k] = mp.mpf(3) / ((2 * k + 3) * (k - 2)) * sum(ck[j] * ck[k - 1 - j] for j in range(1, k - 1))
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
    dN_h = [-(2 * th2 * dth2) / denom_hat, -(2 * th4 * dth4) / denom_hat, (2 * im * th3 * dth3) / denom_hat]
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
            R_ch = [sum(ec_list[si][r, c] * M_m[r, c] for r in range(2) for c in range(2)) for si in range(4)]

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


def build_open_weave_yukawas(multiples=(8, 24), dps=55):
    """Build exact A2-OW6 Regime-4b E[5] + E[6] (Y_u, Y_d, Y_e) at m in multiples."""
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    ec_list, C_ten = build_fu2_coupling_tensor()
    l2_cache = {}

    # Independent S-transformation law check for our GL6 L_2 solver
    tau_s = mp.mpc(1, 0) / 5 + mp.mpc(0, 1)
    r_sa = solve_L2_F1_gl6(tau_s)
    r_sb = solve_L2_F1_gl6(-1 / tau_s)
    L2_S_law_err = abs(r_sb["L2"] - (r_sa["L2"] + mp.log(abs(tau_s))))

    lam_3 = (3 + mp.sqrt(5)) / 2
    lam_4 = (4 + mp.sqrt(12)) / 2
    w_3 = lam_3 ** (-4)
    w_4 = 4 * (lam_4 ** (-4))
    sectors = {"u": (1, -4), "d": (1, 2), "e": (-3, 6)}
    tau_base = mp.mpc(2, 1) / 5

    out = {}
    max_wchk = mp.mpf(0)
    for m in multiples:
        tau_m = m * tau_base
        L2_m, base_m = solve_L2_any_gl6(tau_m, l2_cache)
        max_wchk = max(max_wchk, base_m["w_check"])
        c3_m, den_m = compute_c3_denom_jtheta_mp(tau_m)
        fu_cache = {}
        Ym = {}
        for sec, (qL, qR) in sectors.items():
            Y5 = eval_yukawa_EN_mp(tau_m, L2_m, 5, qL, qR, ec_list, C_ten, c3_m, den_m, fu_cache)
            Y6 = eval_yukawa_EN_mp(tau_m, L2_m, 6, qL, qR, ec_list, C_ten, c3_m, den_m, fu_cache)
            Ym[sec] = w_3 * Y5 + w_4 * Y6
        out[m] = {"tau": tau_m, "L2": L2_m, "Y": Ym}

    mp.mp.dps = old_dps
    return out, L2_S_law_err, max_wchk


# =============================================================================
# SECTION 3: EXACT 2-LOOP SM & 3x3 MATRIX SM / TYPE-II 2HDM RGE INTEGRATORS
# =============================================================================

def sm_2loop_rhs_generic(state, pi_val, scale_factor):
    """
    Exact 2-loop SM beta functions (Machacek-Vaughn / Luo-Xiao / Buttazzo App. A)
    for state = [g_Y, g_2, g_3, y_t, lam] in t = ln(mu / mu_0) with V = lam |H|^4.
    Works identically in float64 (for DOP853) and high-precision mpmath (for GL6).
    """
    gY, g2, g3, yt, lam = state
    k1 = 1 / (16 * pi_val * pi_val)
    k2 = k1 * k1

    gY2 = gY * gY
    gY3 = gY2 * gY
    gY4 = gY2 * gY2
    gY6 = gY4 * gY2
    g22 = g2 * g2
    g23 = g22 * g2
    g24 = g22 * g22
    g26 = g24 * g22
    g32 = g3 * g3
    g33 = g32 * g3
    g34 = g32 * g32
    yt2 = yt * yt
    yt4 = yt2 * yt2
    yt6 = yt4 * yt2
    lam2 = lam * lam
    lam3 = lam2 * lam

    b1_gY = (41 * gY3) / 6
    b2_gY = gY3 * ((199 * gY2) / 18 + (9 * g22) / 2 + (44 * g32) / 3 - (17 * yt2) / 6)

    b1_g2 = (-19 * g23) / 6
    b2_g2 = g23 * ((3 * gY2) / 2 + (35 * g22) / 6 + 12 * g32 - (3 * yt2) / 2)

    b1_g3 = -7 * g33
    b2_g3 = g33 * ((11 * gY2) / 6 + (9 * g22) / 2 - 26 * g32 - 2 * yt2)

    b1_yt = yt * ((9 * yt2) / 2 - (17 * gY2) / 12 - (9 * g22) / 4 - 8 * g32)
    b2_yt = yt * (
        -12 * yt4
        + 6 * lam2
        - 12 * lam * yt2
        + yt2 * ((131 * gY2) / 16 + (225 * g22) / 16 + 36 * g32)
        + (1187 * gY4) / 216
        - (3 * gY2 * g22) / 4
        + (19 * gY2 * g32) / 9
        - (23 * g24) / 4
        + 9 * g22 * g32
        - 108 * g34
    )

    b1_lam = (
        24 * lam2
        - 6 * yt4
        + (3 * (2 * g24 + (g22 + gY2) * (g22 + gY2))) / 8
        + lam * (12 * yt2 - 9 * g22 - 3 * gY2)
    )
    b2_lam = (
        -312 * lam3
        + 36 * lam2 * (gY2 + 3 * g22)
        + lam * ((629 * gY4) / 24 + (39 * gY2 * g22) / 4 - (73 * g24) / 8)
        + (305 * g26) / 16
        - (289 * g24 * gY2) / 48
        - (559 * g22 * gY4) / 48
        - (379 * gY6) / 48
        - 144 * lam2 * yt2
        - 3 * lam * yt4
        + 30 * yt6
        + lam * yt2 * ((85 * gY2) / 6 + (45 * g22) / 2 + 80 * g32)
        - yt4 * ((8 * gY2) / 3 + 32 * g32)
        + yt2 * (-(9 * g24) / 4 + (21 * g22 * gY2) / 2 - (19 * gY4) / 4)
    )

    return [
        scale_factor * (k1 * b1_gY + k2 * b2_gY),
        scale_factor * (k1 * b1_g2 + k2 * b2_g2),
        scale_factor * (k1 * b1_g3 + k2 * b2_g3),
        scale_factor * (k1 * b1_yt + k2 * b2_yt),
        scale_factor * (k1 * b1_lam + k2 * b2_lam),
    ]


def integrate_sm_2loop_gl6_mp(y0_mp, t_span, n_steps, scale_factor_mp, dps=35):
    """Disjoint 35-dps mpmath 3-stage implicit Gauss-Legendre RK6 (GL6) ODE integrator."""
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    _, b_w, A, _ = gl6_tableau_mp()
    pi_val = mp.pi
    t0, t1 = t_span
    h = (t1 - t0) / n_steps
    y = [mp.mpf(val) for val in y0_mp]
    tol_fp = mp.mpf(10) ** (-dps + 4)
    max_fp_res = mp.mpf(0)
    lam_zero_t = None

    for step in range(n_steps):
        y_prev = list(y)
        f0 = sm_2loop_rhs_generic(y, pi_val, scale_factor_mp)
        K = [list(f0), list(f0), list(f0)]
        fp_res = mp.mpf(1)
        for _ in range(40):
            fp_res = mp.mpf(0)
            for i in range(3):
                yi = [
                    y[j] + h * (A[i][0] * K[0][j] + A[i][1] * K[1][j] + A[i][2] * K[2][j])
                    for j in range(5)
                ]
                ki_new = sm_2loop_rhs_generic(yi, pi_val, scale_factor_mp)
                for j in range(5):
                    d = abs(ki_new[j] - K[i][j])
                    if d > fp_res:
                        fp_res = d
                K[i] = ki_new
            if fp_res < tol_fp:
                break
        if fp_res > max_fp_res:
            max_fp_res = fp_res
        y = [
            y[j] + h * (b_w[0] * K[0][j] + b_w[1] * K[1][j] + b_w[2] * K[2][j])
            for j in range(5)
        ]
        # Detect first sign change of lambda and bisect via GL6 sub-steps to 10^-25
        if lam_zero_t is None and y_prev[4] > 0 and y[4] <= 0:
            lo_h = mp.mpf(0)
            hi_h = h
            for _ in range(70):
                mid_h = (lo_h + hi_h) / 2
                Km = [list(f0), list(f0), list(f0)]
                for _ in range(30):
                    r_m = mp.mpf(0)
                    for i in range(3):
                        yim = [
                            y_prev[j] + mid_h * (A[i][0] * Km[0][j] + A[i][1] * Km[1][j] + A[i][2] * Km[2][j])
                            for j in range(5)
                        ]
                        kn = sm_2loop_rhs_generic(yim, pi_val, scale_factor_mp)
                        for j in range(5):
                            dd = abs(kn[j] - Km[i][j])
                            if dd > r_m:
                                r_m = dd
                        Km[i] = kn
                    if r_m < tol_fp:
                        break
                lam_mid = y_prev[4] + mid_h * (b_w[0] * Km[0][4] + b_w[1] * Km[1][4] + b_w[2] * Km[2][4])
                if lam_mid > 0:
                    lo_h = mid_h
                else:
                    hi_h = mid_h
            lam_zero_t = t0 + step * h + (lo_h + hi_h) / 2

    mp.mp.dps = old_dps
    return y, lam_zero_t, max_fp_res


def matrix_rge_coeffs_exact(model, c_cross_override=None):
    """Exact rational coefficients for 2-loop gauge + 1-loop 3x3 left-covariant Yukawa RGEs."""
    if model == "SM":
        b_g = (Fraction(41, 10), Fraction(-19, 6), Fraction(-7, 1))
        B_g = (
            (Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)),
            (Fraction(9, 10), Fraction(35, 6), Fraction(12, 1)),
            (Fraction(11, 10), Fraction(9, 2), Fraction(-26, 1)),
        )
        c_cross = Fraction(-3, 2) if c_cross_override is None else c_cross_override
    elif model == "2HDM_II":
        b_g = (Fraction(21, 5), Fraction(-3, 1), Fraction(-7, 1))
        B_g = (
            (Fraction(104, 25), Fraction(18, 5), Fraction(44, 5)),
            (Fraction(6, 5), Fraction(8, 1), Fraction(12, 1)),
            (Fraction(11, 10), Fraction(9, 2), Fraction(-26, 1)),
        )
        c_cross = Fraction(1, 2) if c_cross_override is None else c_cross_override
    else:
        raise ValueError("Unknown model: " + str(model))
    c_yuk = (
        (Fraction(17, 10), Fraction(1, 2), Fraction(3, 2)),
        (Fraction(3, 2), Fraction(3, 2), Fraction(1, 2)),
        (Fraction(2, 1), Fraction(2, 1), Fraction(0, 1)),
    )
    c_self = Fraction(3, 2)
    return b_g, B_g, c_yuk, c_self, c_cross


def pack_matrix_state_np(g1, g2, g3, Yu, Yd, Ye):
    v = np.empty(57, dtype=np.float64)
    v[0], v[1], v[2] = g1, g2, g3
    pos = 3
    for M in (Yu, Yd, Ye):
        flat = M.reshape(9)
        v[pos:pos + 9] = np.real(flat)
        v[pos + 9:pos + 18] = np.imag(flat)
        pos += 18
    return v


def unpack_matrix_state_np(v):
    g1, g2, g3 = v[0], v[1], v[2]
    mats = []
    pos = 3
    for _ in range(3):
        re_p = v[pos:pos + 9].reshape((3, 3))
        im_p = v[pos + 9:pos + 18].reshape((3, 3))
        mats.append(re_p + complex(0, 1) * im_p)
        pos += 18
    return g1, g2, g3, mats[0], mats[1], mats[2]


def matrix_rge_rhs_np(t, v, model, c_cross_override=None, two_loop_gauge=True):
    b_g, B_g, c_yuk, c_self, c_cross = matrix_rge_coeffs_exact(model, c_cross_override)
    g1, g2, g3, Yu, Yd, Ye = unpack_matrix_state_np(v)
    k1 = 1 / (16 * math.pi * math.pi)
    k2 = k1 * k1

    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    He = Ye @ Ye.conj().T
    tu = float(np.real(np.trace(Hu)))
    td = float(np.real(np.trace(Hd)))
    te = float(np.real(np.trace(He)))

    gs = (g1, g2, g3)
    g2s = (g1 * g1, g2 * g2, g3 * g3)
    dgs = []
    for i in range(3):
        b1 = (b_g[i].numerator / b_g[i].denominator) * (gs[i] ** 3)
        if two_loop_gauge:
            mix = sum((B_g[i][j].numerator / B_g[i][j].denominator) * g2s[j] for j in range(3))
            yuk = (
                (c_yuk[i][0].numerator / c_yuk[i][0].denominator) * tu
                + (c_yuk[i][1].numerator / c_yuk[i][1].denominator) * td
                + (c_yuk[i][2].numerator / c_yuk[i][2].denominator) * te
            )
            b2 = (gs[i] ** 3) * (mix - yuk)
            dgs.append(k1 * b1 + k2 * b2)
        else:
            dgs.append(k1 * b1)

    Gu = (17 * g2s[0]) / 20 + (9 * g2s[1]) / 4 + 8 * g2s[2]
    Gd = g2s[0] / 4 + (9 * g2s[1]) / 4 + 8 * g2s[2]
    Ge = (9 * g2s[0]) / 4 + (9 * g2s[1]) / 4

    if model == "SM":
        Tu = 3 * tu + 3 * td + te
        Td = Tu
        Te = Tu
    else:
        Tu = 3 * tu
        Td = 3 * td + te
        Te = Td

    cs = c_self.numerator / c_self.denominator
    cc = c_cross.numerator / c_cross.denominator
    I3 = np.eye(3, dtype=np.complex128)
    dYu = k1 * (((Tu - Gu) * I3 + cs * Hu + cc * Hd) @ Yu)
    dYd = k1 * (((Td - Gd) * I3 + cs * Hd + cc * Hu) @ Yd)
    dYe = k1 * (((Te - Ge) * I3 + cs * He) @ Ye)
    return pack_matrix_state_np(dgs[0], dgs[1], dgs[2], dYu, dYd, dYe)


def integrate_matrix_rge_dop853_np(g_init, Yu0, Yd0, Ye0, dt, model, c_cross_override=None, two_loop_gauge=True):
    v0 = pack_matrix_state_np(g_init[0], g_init[1], g_init[2], Yu0, Yd0, Ye0)
    sol = solve_ivp(
        lambda t, y: matrix_rge_rhs_np(t, y, model, c_cross_override, two_loop_gauge),
        (0, dt),
        v0,
        method="DOP853",
        rtol=1 / (10 ** 13),
        atol=1 / (10 ** 14),
    )
    if not sol.success:
        raise RuntimeError("DOP853 failed: " + str(sol.message))
    g1, g2, g3, Yu, Yd, Ye = unpack_matrix_state_np(sol.y[:, -1])
    return (g1, g2, g3), Yu, Yd, Ye, int(sol.nfev)


def matrix_rge_rhs_mp(state, model, c_cross_override=None, two_loop_gauge=True):
    """Exact high-precision mpmath 2-loop gauge + 1-loop left-covariant 3x3 matrix Yukawa RHS."""
    b_g, B_g, c_yuk, c_self, c_cross = matrix_rge_coeffs_exact(model, c_cross_override)
    g1, g2, g3, Yu, Yd, Ye = state
    k1 = mp.mpf(1) / (16 * mp.pi * mp.pi)
    k2 = k1 * k1

    Hu = Yu * Yu.H
    Hd = Yd * Yd.H
    He = Ye * Ye.H
    tu = mp.re(Hu[0, 0] + Hu[1, 1] + Hu[2, 2])
    td = mp.re(Hd[0, 0] + Hd[1, 1] + Hd[2, 2])
    te = mp.re(He[0, 0] + He[1, 1] + He[2, 2])

    def frac_mp(f):
        return mp.mpf(f.numerator) / f.denominator

    gs = (g1, g2, g3)
    g2s = (g1 * g1, g2 * g2, g3 * g3)
    dgs = []
    for i in range(3):
        b1 = frac_mp(b_g[i]) * (gs[i] ** 3)
        if two_loop_gauge:
            mix = sum(frac_mp(B_g[i][j]) * g2s[j] for j in range(3))
            yuk = frac_mp(c_yuk[i][0]) * tu + frac_mp(c_yuk[i][1]) * td + frac_mp(c_yuk[i][2]) * te
            b2 = (gs[i] ** 3) * (mix - yuk)
            dgs.append(k1 * b1 + k2 * b2)
        else:
            dgs.append(k1 * b1)

    Gu = (17 * g2s[0]) / 20 + (9 * g2s[1]) / 4 + 8 * g2s[2]
    Gd = g2s[0] / 4 + (9 * g2s[1]) / 4 + 8 * g2s[2]
    Ge = (9 * g2s[0]) / 4 + (9 * g2s[1]) / 4

    if model == "SM":
        Tu = 3 * tu + 3 * td + te
        Td = Tu
        Te = Tu
    else:
        Tu = 3 * tu
        Td = 3 * td + te
        Te = Td

    cs = frac_mp(c_self)
    cc = frac_mp(c_cross)
    I3 = mp.eye(3)
    dYu = k1 * (((Tu - Gu) * I3 + cs * Hu + cc * Hd) * Yu)
    dYd = k1 * (((Td - Gd) * I3 + cs * Hd + cc * Hu) * Yd)
    dYe = k1 * (((Te - Ge) * I3 + cs * He) * Ye)
    return (dgs[0], dgs[1], dgs[2], dYu, dYd, dYe)


def state_add_scaled_mp(base, h, coeffs, Ks):
    out_g = [
        base[idx] + h * (coeffs[0] * Ks[0][idx] + coeffs[1] * Ks[1][idx] + coeffs[2] * Ks[2][idx])
        for idx in range(3)
    ]
    out_m = []
    for idx in range(3, 6):
        M = mp.matrix(3, 3)
        B = base[idx]
        K0, K1, K2 = Ks[0][idx], Ks[1][idx], Ks[2][idx]
        c0, c1, c2 = coeffs[0], coeffs[1], coeffs[2]
        for r in range(3):
            for c in range(3):
                M[r, c] = B[r, c] + h * (c0 * K0[r, c] + c1 * K1[r, c] + c2 * K2[r, c])
        out_m.append(M)
    return (out_g[0], out_g[1], out_g[2], out_m[0], out_m[1], out_m[2])


def state_diff_inf_mp(s1, s2):
    d = max(abs(s1[i] - s2[i]) for i in range(3))
    for idx in range(3, 6):
        M1, M2 = s1[idx], s2[idx]
        for r in range(3):
            for c in range(3):
                v = abs(M1[r, c] - M2[r, c])
                if v > d:
                    d = v
    return d


def integrate_matrix_rge_gl6_mp(
    g_init, Yu0, Yd0, Ye0, dt, model, n_steps=80, c_cross_override=None, two_loop_gauge=True, dps=35
):
    """
    Disjoint 35-dps mpmath 3-stage implicit Gauss-Legendre RK6 (GL6) integrator for
    3x3 complex matrix RGEs. Preserves m=24 |J_CP| ~ 10^-16 to > 15 significant digits.
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    _, b_w, A, _ = gl6_tableau_mp()
    h = mp.mpf(dt) / n_steps
    tol_fp = mp.mpf(10) ** (-dps + 4)

    st = (
        mp.mpf(g_init[0]),
        mp.mpf(g_init[1]),
        mp.mpf(g_init[2]),
        mp.matrix([[mp.mpc(Yu0[r, c]) for c in range(3)] for r in range(3)]),
        mp.matrix([[mp.mpc(Yd0[r, c]) for c in range(3)] for r in range(3)]),
        mp.matrix([[mp.mpc(Ye0[r, c]) for c in range(3)] for r in range(3)]),
    )
    max_fp_res = mp.mpf(0)

    for _ in range(n_steps):
        f0 = matrix_rge_rhs_mp(st, model, c_cross_override, two_loop_gauge)
        K = [f0, f0, f0]
        fp_res = mp.mpf(1)
        for _ in range(45):
            fp_res = mp.mpf(0)
            for i in range(3):
                yi = state_add_scaled_mp(st, h, A[i], K)
                ki_new = matrix_rge_rhs_mp(yi, model, c_cross_override, two_loop_gauge)
                diff = state_diff_inf_mp(ki_new, K[i])
                if diff > fp_res:
                    fp_res = diff
                K[i] = ki_new
            if fp_res < tol_fp:
                break
        if fp_res > max_fp_res:
            max_fp_res = fp_res
        st = state_add_scaled_mp(st, h, b_w, K)

    mp.mp.dps = old_dps
    return (st[0], st[1], st[2]), st[3], st[4], st[5], max_fp_res


def build_xing_zhou_initial_mp(model, dps=35):
    """Build standard M_Z hierarchical CKM benchmark (Xing-Zhou 1804.01925)."""
    old_dps = mp.mp.dps
    mp.mp.dps = dps

    g1 = mp.mpf(461425) / 1000000
    g2 = mp.mpf(65184) / 100000
    g3 = mp.mpf(12143) / 10000

    s12 = mp.mpf(225) / 1000
    c12 = mp.sqrt(1 - s12 * s12)
    s23 = mp.mpf(415) / 10000
    c23 = mp.sqrt(1 - s23 * s23)
    s13 = mp.mpf(36) / 10000
    c13 = mp.sqrt(1 - s13 * s13)
    delta = mp.mpf(12) / 10
    eip = mp.exp(mp.mpc(0, 1) * delta)
    eim = mp.exp(mp.mpc(0, -1) * delta)

    V0 = mp.matrix([
        [c12 * c13, s12 * c13, s13 * eim],
        [-s12 * c23 - c12 * s23 * s13 * eip, c12 * c23 - s12 * s23 * s13 * eip, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eip, -c12 * s23 - s12 * c23 * s13 * eip, c23 * c13],
    ])

    su = [mp.mpf(75) / (10 ** 7), mp.mpf(36) / 10000, mp.mpf(986) / 1000]
    sd = [mp.mpf(16) / (10 ** 6), mp.mpf(32) / (10 ** 5), mp.mpf(166) / 10000]
    se = [mp.mpf(28) / (10 ** 7), mp.mpf(60) / (10 ** 5), mp.mpf(100) / 10000]

    if model == "2HDM_II":
        # tan(beta) = 10 -> sin(beta) = 10/sqrt(101), cos(beta) = 1/sqrt(101)
        s_b = mp.mpf(10) / mp.sqrt(101)
        c_b = mp.mpf(1) / mp.sqrt(101)
        su = [x / s_b for x in su]
        sd = [x / c_b for x in sd]
        se = [x / c_b for x in se]

    Yu0 = mp.diag(su)
    Yd0 = V0 * mp.diag(sd)
    Ye0 = mp.diag(se)
    mp.mp.dps = old_dps
    return (g1, g2, g3), Yu0, Yd0, Ye0


def mp_mat_to_np(M):
    arr = np.zeros((3, 3), dtype=np.complex128)
    for r in range(3):
        for c in range(3):
            arr[r, c] = complex(float(mp.re(M[r, c])), float(mp.im(M[r, c])))
    return arr


# =============================================================================
# TASK OW7-A: GUARDRAIL 4 PUBLISHED LITERATURE BENCHMARK GATE
# =============================================================================

def run_task_ow7_a():
    # 1. Buttazzo et al. (1307.3536, Table 3 NNLO MS-bar inputs at M_t = 173.34 GeV -> M_Pl = 1.2209e19 GeV)
    M_t_f = 17334 / 100
    M_Pl_f = 12209 * (10 ** 15)
    t_Pl_f = math.log(M_Pl_f / M_t_f)

    y0_but_f = [
        35830 / 100000,   # g_Y(M_t)
        64779 / 100000,   # g_2(M_t)
        11666 / 10000,    # g_3(M_t)
        93690 / 100000,   # y_t(M_t)
        12604 / 100000,   # lam(M_t)
    ]

    def lam_zero_event(t, y):
        return y[4]
    lam_zero_event.direction = -1

    sol_but = solve_ivp(
        lambda t, y: sm_2loop_rhs_generic(y, math.pi, 1),
        (0, t_Pl_f),
        y0_but_f,
        method="DOP853",
        rtol=1 / (10 ** 13),
        atol=1 / (10 ** 14),
        events=lam_zero_event,
    )
    if not sol_but.success:
        raise RuntimeError("Buttazzo DOP853 failed")

    gY_Pl, g2_Pl, g3_Pl, yt_Pl, lam_Pl = [float(x) for x in sol_but.y[:, -1]]
    t_zero_dop = float(sol_but.t_events[0][0]) if len(sol_but.t_events[0]) > 0 else None
    log10_Lambda_lam = math.log10(M_t_f) + t_zero_dop / math.log(10) if t_zero_dop is not None else None

    # Disjoint cross-check via 35-dps mpmath implicit GL6 (N = 128 steps)
    mp.mp.dps = 35
    M_t_mp = mp.mpf(17334) / 100
    M_Pl_mp = mp.mpf(12209) * (mp.mpf(10) ** 15)
    t_Pl_mp = mp.log(M_Pl_mp / M_t_mp)
    y0_but_mp = [
        mp.mpf(35830) / 100000,
        mp.mpf(64779) / 100000,
        mp.mpf(11666) / 10000,
        mp.mpf(93690) / 100000,
        mp.mpf(12604) / 100000,
    ]
    y_gl6, t_zero_gl6, but_gl6_fp_res = integrate_sm_2loop_gl6_mp(
        y0_but_mp, (mp.mpf(0), t_Pl_mp), n_steps=128, scale_factor_mp=mp.mpf(1), dps=35
    )
    log10_lam_gl6 = (
        mp.log10(M_t_mp) + t_zero_gl6 / mp.log(10) if t_zero_gl6 is not None else None
    )
    dop_vs_gl6_but_err = max(
        abs(gY_Pl - float(y_gl6[0])),
        abs(g2_Pl - float(y_gl6[1])),
        abs(g3_Pl - float(y_gl6[2])),
        abs(yt_Pl - float(y_gl6[3])),
        abs(lam_Pl - float(y_gl6[4])),
        abs(log10_Lambda_lam - float(log10_lam_gl6)) if (log10_Lambda_lam is not None and log10_lam_gl6 is not None) else 1,
    )

    but_ok = bool(
        abs(gY_Pl - 477 / 1000) < 1 / 100
        and abs(g2_Pl - 506 / 1000) < 1 / 100
        and abs(g3_Pl - 487 / 1000) < 1 / 100
        and abs(yt_Pl - 382 / 1000) < 1 / 100
        and (-2 / 100 < lam_Pl < -1 / 100)
        and (log10_Lambda_lam is not None and 9 < log10_Lambda_lam < 105 / 10)
        and dop_vs_gl6_but_err < 1 / (10 ** 10)
    )

    # 2. Left-covariance verification of 3x3 matrix RHS under random Haar Q_L -> U_L Q_L
    mp.mp.dps = 35
    rng_cov = random.Random(2026112101)
    UL = random_haar_u3_householder_mp(rng_cov)
    URu = random_haar_u3_householder_mp(rng_cov)
    URd = random_haar_u3_householder_mp(rng_cov)
    ULe = random_haar_u3_householder_mp(rng_cov)
    URe = random_haar_u3_householder_mp(rng_cov)
    max_cov_err_mp = mp.mpf(0)
    max_cov_err_np = 0
    for mdl in ("SM", "2HDM_II"):
        g0_m, Yu0_m, Yd0_m, Ye0_m = build_xing_zhou_initial_mp(mdl, dps=35)
        st0 = (g0_m[0], g0_m[1], g0_m[2], Yu0_m, Yd0_m, Ye0_m)
        st_rot = (g0_m[0], g0_m[1], g0_m[2], UL * Yu0_m * URu.H, UL * Yd0_m * URd.H, ULe * Ye0_m * URe.H)
        rhs0 = matrix_rge_rhs_mp(st0, mdl)
        rhs_rot = matrix_rge_rhs_mp(st_rot, mdl)
        err_m = max(
            abs(rhs_rot[0] - rhs0[0]),
            abs(rhs_rot[1] - rhs0[1]),
            abs(rhs_rot[2] - rhs0[2]),
            mat_frob_norm_mp(rhs_rot[3] - UL * rhs0[3] * URu.H),
            mat_frob_norm_mp(rhs_rot[4] - UL * rhs0[4] * URd.H),
            mat_frob_norm_mp(rhs_rot[5] - ULe * rhs0[5] * URe.H),
        )
        if err_m > max_cov_err_mp:
            max_cov_err_mp = err_m

        # Same covariance check on numpy RHS
        ULn, URun, URdn, ULen, URen = [mp_mat_to_np(M) for M in (UL, URu, URd, ULe, URe)]
        Yu0n, Yd0n, Ye0n = [mp_mat_to_np(M) for M in (Yu0_m, Yd0_m, Ye0_m)]
        v0n = pack_matrix_state_np(float(g0_m[0]), float(g0_m[1]), float(g0_m[2]), Yu0n, Yd0n, Ye0n)
        vrn = pack_matrix_state_np(
            float(g0_m[0]), float(g0_m[1]), float(g0_m[2]),
            ULn @ Yu0n @ URun.conj().T, ULn @ Yd0n @ URdn.conj().T, ULen @ Ye0n @ URen.conj().T,
        )
        _, _, _, dYu0, dYd0, dYe0 = unpack_matrix_state_np(matrix_rge_rhs_np(0, v0n, mdl))
        _, _, _, dYur, dYdr, dYer = unpack_matrix_state_np(matrix_rge_rhs_np(0, vrn, mdl))
        err_n = float(max(
            np.linalg.norm(dYur - ULn @ dYu0 @ URun.conj().T),
            np.linalg.norm(dYdr - ULn @ dYd0 @ URdn.conj().T),
            np.linalg.norm(dYer - ULen @ dYe0 @ URen.conj().T),
        ))
        if err_n > max_cov_err_np:
            max_cov_err_np = err_n

    # 3. Xing-Zhou (1804.01925, M_Z -> 10^14 GeV): SM vs Type-II 2HDM opposite running direction
    M_Z_f = 911876 / 10000
    dt_xz_f = math.log((10 ** 14) / M_Z_f)
    dt_xz_mp = mp.log((mp.mpf(10) ** 14) / (mp.mpf(911876) / 10000))

    xz_results = {}
    max_xz_dop_vs_gl6 = 0
    for mdl in ("SM", "2HDM_II"):
        g0_m, Yu0_m, Yd0_m, Ye0_m = build_xing_zhou_initial_mp(mdl, dps=35)
        g0_f = tuple(float(x) for x in g0_m)
        Yu0_n, Yd0_n, Ye0_n = mp_mat_to_np(Yu0_m), mp_mat_to_np(Yd0_m), mp_mat_to_np(Ye0_m)

        obs0_np = extract_flavor_observables_np(Yu0_n, Yd0_n, Ye0_n)
        g1_f, Yu1_n, Yd1_n, Ye1_n, nfev = integrate_matrix_rge_dop853_np(
            g0_f, Yu0_n, Yd0_n, Ye0_n, dt_xz_f, mdl
        )
        obs1_np = extract_flavor_observables_np(Yu1_n, Yd1_n, Ye1_n)

        # Cross-check with 35-dps mpmath implicit GL6 (N = 128 steps)
        g1_m, Yu1_m, Yd1_m, Ye1_m, fp_res = integrate_matrix_rge_gl6_mp(
            g0_m, Yu0_m, Yd0_m, Ye0_m, dt_xz_mp, mdl, n_steps=128, dps=35
        )
        mp.mp.dps = 35
        obs0_m = extract_flavor_observables_svd_mp(Yu0_m, Yd0_m, Ye0_m)
        obs1_m = extract_flavor_observables_svd_mp(Yu1_m, Yd1_m, Ye1_m)

        vus_rat_dop = obs1_np["V_us"] / obs0_np["V_us"]
        vcb_rat_dop = obs1_np["V_cb"] / obs0_np["V_cb"]
        jcp_rat_dop = abs(obs1_np["J_CP"]) / abs(obs0_np["J_CP"])

        vus_rat_gl6 = float(obs1_m["V_us"] / obs0_m["V_us"])
        vcb_rat_gl6 = float(obs1_m["V_cb"] / obs0_m["V_cb"])
        jcp_rat_gl6 = float(abs(obs1_m["J_CP"]) / abs(obs0_m["J_CP"]))
        diff_int = max(
            abs(vus_rat_dop - vus_rat_gl6),
            abs(vcb_rat_dop - vcb_rat_gl6),
            abs(jcp_rat_dop - jcp_rat_gl6),
        )
        if diff_int > max_xz_dop_vs_gl6:
            max_xz_dop_vs_gl6 = diff_int

        xz_results[mdl] = {
            "dop853_nfev": nfev,
            "V_us_MZ": obs0_np["V_us"],
            "V_us_1e14": obs1_np["V_us"],
            "V_us_ratio": vus_rat_dop,
            "V_cb_MZ": obs0_np["V_cb"],
            "V_cb_1e14": obs1_np["V_cb"],
            "V_cb_ratio": vcb_rat_dop,
            "J_CP_MZ": obs0_np["J_CP"],
            "J_CP_1e14": obs1_np["J_CP"],
            "J_CP_ratio": jcp_rat_dop,
            "gl6_fp_max_res": mp.nstr(fp_res, 6),
            "dop853_vs_gl6_max_ratio_diff": diff_int,
        }

    sm_xz = xz_results["SM"]
    h2_xz = xz_results["2HDM_II"]
    xz_ok = bool(
        sm_xz["V_cb_ratio"] > 11 / 10
        and sm_xz["J_CP_ratio"] > 12 / 10
        and h2_xz["V_cb_ratio"] < 98 / 100
        and h2_xz["J_CP_ratio"] < 95 / 100
        and abs(sm_xz["V_us_ratio"] - 1) < 1 / 1000
        and abs(h2_xz["V_us_ratio"] - 1) < 1 / 1000
        and max_xz_dop_vs_gl6 < 1 / (10 ** 10)
    )
    cov_ok = bool(max_cov_err_mp < mp.mpf(10) ** (-30) and max_cov_err_np < 1 / (10 ** 14))
    passed = bool(but_ok and xz_ok and cov_ok)

    return {
        "integrator_primary": "scipy.integrate.solve_ivp_DOP853_adaptive_8th_order",
        "integrator_crosscheck": "mpmath_35dps_3stage_implicit_Gauss_Legendre_RK6",
        "buttazzo_1307_3536": {
            "M_t_GeV": M_t_f,
            "M_Pl_GeV": M_Pl_f,
            "dop853_nfev": int(sol_but.nfev),
            "g_Y_MPl": gY_Pl,
            "g_2_MPl": g2_Pl,
            "g_3_MPl": g3_Pl,
            "y_t_MPl": yt_Pl,
            "lam_MPl": lam_Pl,
            "log10_Lambda_lam_GeV": log10_Lambda_lam,
            "gl6_log10_Lambda_lam_GeV": mp.nstr(log10_lam_gl6, 15) if log10_lam_gl6 is not None else None,
            "gl6_fp_max_res": mp.nstr(but_gl6_fp_res, 6),
            "dop853_vs_gl6_max_err": dop_vs_gl6_but_err,
            "pass": but_ok,
        },
        "left_covariance_check": {
            "max_err_mpmath_35dps": mp.nstr(max_cov_err_mp, 6),
            "max_err_numpy_f64": max_cov_err_np,
            "pass": cov_ok,
        },
        "xing_zhou_1804_01925": {
            "M_Z_GeV": M_Z_f,
            "mu_high_GeV": 10 ** 14,
            "SM": sm_xz,
            "2HDM_II": h2_xz,
            "max_dop853_vs_gl6_ratio_diff": max_xz_dop_vs_gl6,
            "pass": xz_ok,
        },
        "pass": passed,
    }


# =============================================================================
# TASK OW7-B: RG RIGIDITY THEOREM ON OPEN-WEAVE A2-OW6 UV YUKAWAS (0 OF 19)
# =============================================================================

def run_task_ow7_b(ow_data):
    """
    Integrate all 8 trajectories (m in {8, 24}, SM vs 2HDM_II, y_UV in {7/10, 3/2},
    g_UV = 52/100, dt = -14 * ln(10)) using 35-dps mpmath implicit GL6 (N = 80),
    cross-checked against adaptive DOP853 on m = 8 and step-halving N = 160 on m = 24.
    """
    dps_ode = 35
    mp.mp.dps = dps_ode
    dt_mp = -14 * mp.log(10)
    dt_f = -14 * math.log(10)
    g_uv_mp = mp.mpf(52) / 100
    g_uv_f = 52 / 100

    trajectories = []
    max_r13_factor = mp.mpf(0)
    max_Vus_rel_shift = mp.mpf(0)
    max_Vcb_factor = mp.mpf(0)
    max_JCP_factor = mp.mpf(0)
    max_fp_res_all = mp.mpf(0)
    max_m8_dop_vs_gl6 = 0
    sm_all_suppress = True
    h2_all_enhance_lt2 = True
    step_halving_m24_err = None

    for m in (8, 24):
        Y_raw = ow_data[m]["Y"]
        # Pre-extract raw sigma_max for each sector at 35 dps
        mp.mp.dps = dps_ode
        raw_smax = {}
        for sec in ("u", "d", "e"):
            Ym_cast = mp.matrix([[mp.mpc(Y_raw[sec][r, c]) for c in range(3)] for r in range(3)])
            raw_smax[sec] = svd_sector_ascending_mp(Ym_cast)["svs_asc"][2]

        for model in ("SM", "2HDM_II"):
            for y_num, y_den in ((7, 10), (3, 2)):
                mp.mp.dps = dps_ode
                y_uv_mp = mp.mpf(y_num) / y_den
                Yu_uv = (y_uv_mp / raw_smax["u"]) * mp.matrix(
                    [[mp.mpc(Y_raw["u"][r, c]) for c in range(3)] for r in range(3)]
                )
                Yd_uv = (y_uv_mp / raw_smax["d"]) * mp.matrix(
                    [[mp.mpc(Y_raw["d"][r, c]) for c in range(3)] for r in range(3)]
                )
                Ye_uv = (y_uv_mp / raw_smax["e"]) * mp.matrix(
                    [[mp.mpc(Y_raw["e"][r, c]) for c in range(3)] for r in range(3)]
                )

                obs_uv = extract_flavor_observables_svd_mp(Yu_uv, Yd_uv, Ye_uv)
                g_ir, Yu_ir, Yd_ir, Ye_ir, fp_res = integrate_matrix_rge_gl6_mp(
                    (g_uv_mp, g_uv_mp, g_uv_mp), Yu_uv, Yd_uv, Ye_uv, dt_mp, model, n_steps=128, dps=dps_ode
                )
                if fp_res > max_fp_res_all:
                    max_fp_res_all = fp_res
                obs_ir = extract_flavor_observables_svd_mp(Yu_ir, Yd_ir, Ye_ir)

                # Ratios & symmetry factors
                r13_factors = {}
                traj_max_r13 = mp.mpf(0)
                for sec in ("u", "d", "e"):
                    rat = obs_ir[sec]["r13"] / obs_uv[sec]["r13"]
                    fac = rat if rat >= 1 else (1 / rat)
                    r13_factors[sec] = rat
                    if fac > traj_max_r13:
                        traj_max_r13 = fac

                vus_rel = abs(obs_ir["V_us"] - obs_uv["V_us"]) / obs_uv["V_us"]
                vcb_rat = obs_ir["V_cb"] / obs_uv["V_cb"]
                vcb_fac = vcb_rat if vcb_rat >= 1 else (1 / vcb_rat)
                jcp_rat = abs(obs_ir["J_CP"]) / abs(obs_uv["J_CP"])
                jcp_fac = jcp_rat if jcp_rat >= 1 else (1 / jcp_rat)

                if traj_max_r13 > max_r13_factor:
                    max_r13_factor = traj_max_r13
                if vus_rel > max_Vus_rel_shift:
                    max_Vus_rel_shift = vus_rel
                if vcb_fac > max_Vcb_factor:
                    max_Vcb_factor = vcb_fac
                if jcp_fac > max_JCP_factor:
                    max_JCP_factor = jcp_fac

                if model == "SM":
                    if not (vcb_rat < 1 and jcp_rat < 1):
                        sm_all_suppress = False
                else:
                    if not (1 < vcb_rat < 2 and 1 < jcp_rat < 2):
                        h2_all_enhance_lt2 = False

                # Cross-check m = 8 against adaptive DOP853 (float64)
                dop_diff = None
                if m == 8:
                    _, Yu_d, Yd_d, Ye_d, _ = integrate_matrix_rge_dop853_np(
                        (g_uv_f, g_uv_f, g_uv_f),
                        mp_mat_to_np(Yu_uv), mp_mat_to_np(Yd_uv), mp_mat_to_np(Ye_uv),
                        dt_f, model,
                    )
                    obs_d_uv = extract_flavor_observables_np(mp_mat_to_np(Yu_uv), mp_mat_to_np(Yd_uv), mp_mat_to_np(Ye_uv))
                    obs_d_ir = extract_flavor_observables_np(Yu_d, Yd_d, Ye_d)
                    dop_diff = max(
                        abs((obs_d_ir["V_cb"] / obs_d_uv["V_cb"]) - float(vcb_rat)),
                        abs((abs(obs_d_ir["J_CP"]) / abs(obs_d_uv["J_CP"])) - float(jcp_rat)),
                        abs((obs_d_ir["V_us"] / obs_d_uv["V_us"]) - float(obs_ir["V_us"] / obs_uv["V_us"])),
                        abs((obs_d_ir["u"]["r13"] / obs_d_uv["u"]["r13"]) - float(r13_factors["u"])),
                    )
                    if dop_diff > max_m8_dop_vs_gl6:
                        max_m8_dop_vs_gl6 = dop_diff

                # Step-halving convergence check on toughest m = 24 trajectory (y_UV = 3/2, SM)
                if m == 24 and model == "SM" and y_num == 3 and y_den == 2:
                    _, Yu_256, Yd_256, Ye_256, _ = integrate_matrix_rge_gl6_mp(
                        (g_uv_mp, g_uv_mp, g_uv_mp), Yu_uv, Yd_uv, Ye_uv, dt_mp, model, n_steps=256, dps=dps_ode
                    )
                    obs_256 = extract_flavor_observables_svd_mp(Yu_256, Yd_256, Ye_256)
                    step_halving_m24_err = max(
                        abs(obs_256["V_cb"] / obs_uv["V_cb"] - vcb_rat),
                        abs(abs(obs_256["J_CP"]) / abs(obs_uv["J_CP"]) - jcp_rat),
                        abs(obs_256["u"]["r13"] / obs_uv["u"]["r13"] - r13_factors["u"]),
                    )

                trajectories.append({
                    "m": m,
                    "model": model,
                    "y_UV": f"{y_num}/{y_den}",
                    "g_IR": [mp.nstr(x, 12) for x in g_ir],
                    "r13_u_ratio_IR_over_UV": mp.nstr(r13_factors["u"], 15),
                    "r13_d_ratio_IR_over_UV": mp.nstr(r13_factors["d"], 15),
                    "r13_e_ratio_IR_over_UV": mp.nstr(r13_factors["e"], 15),
                    "max_r13_factor": mp.nstr(traj_max_r13, 15),
                    "V_us_UV": mp.nstr(obs_uv["V_us"], 15),
                    "V_us_IR": mp.nstr(obs_ir["V_us"], 15),
                    "V_us_rel_shift": mp.nstr(vus_rel, 12),
                    "V_cb_UV": mp.nstr(obs_uv["V_cb"], 15),
                    "V_cb_IR": mp.nstr(obs_ir["V_cb"], 15),
                    "V_cb_ratio_IR_over_UV": mp.nstr(vcb_rat, 15),
                    "J_CP_UV": mp.nstr(obs_uv["J_CP"], 15),
                    "J_CP_IR": mp.nstr(obs_ir["J_CP"], 15),
                    "J_CP_ratio_IR_over_UV": mp.nstr(jcp_rat, 15),
                    "gl6_fp_max_res": mp.nstr(fp_res, 6),
                    "m8_dop853_vs_gl6_diff": dop_diff,
                })

    passed = bool(
        len(trajectories) == 8
        and max_r13_factor < 2
        and max_Vus_rel_shift < mp.mpf(4) / 100
        and max_Vcb_factor < 4
        and max_JCP_factor < 4
        and sm_all_suppress
        and h2_all_enhance_lt2
        and max_fp_res_all < mp.mpf(10) ** (-28)
        and max_m8_dop_vs_gl6 < 1 / (10 ** 10)
        and (step_halving_m24_err is not None and step_halving_m24_err < mp.mpf(10) ** (-12))
    )
    return {
        "integrator_primary": "mpmath_35dps_3stage_implicit_GL6_N128",
        "crosscheck_m8": "scipy_DOP853_adaptive_8th_order",
        "crosscheck_m24": "GL6_step_halving_N128_vs_N256",
        "n_trajectories": len(trajectories),
        "max_r13_factor": mp.nstr(max_r13_factor, 15),
        "max_Vus_rel_shift": mp.nstr(max_Vus_rel_shift, 12),
        "max_Vcb_factor": mp.nstr(max_Vcb_factor, 15),
        "max_JCP_factor": mp.nstr(max_JCP_factor, 15),
        "SM_all_suppress_downward": sm_all_suppress,
        "2HDM_II_all_enhance_lt2x_downward": h2_all_enhance_lt2,
        "max_gl6_fp_residual": mp.nstr(max_fp_res_all, 6),
        "max_m8_dop853_vs_gl6_diff": max_m8_dop_vs_gl6,
        "m24_step_halving_err_N128_vs_N256": mp.nstr(step_halving_m24_err, 6) if step_halving_m24_err is not None else None,
        "trajectories": trajectories,
        "pass": passed,
    }


# =============================================================================
# TASK OW7-C: 7D BULK RIGHT-HANDED QR-DECOUPLING ALL 6/6 PERMS + HAAR GATE
# =============================================================================

def apply_bulk_profile_perm_mp(Y, perm, eps_f):
    """Apply Y_eff[r, c] = Y[r, perm[c]] * [eps_f^2, eps_f, 1][c]."""
    weights = [eps_f * eps_f, eps_f, mp.mpf(1)]
    out = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            out[r, c] = Y[r, perm[c]] * weights[c]
    return out


def qr_limit_householder_mp(Yu, Yd, perm):
    """
    Compute exact parameter-free eps_f -> 0^+ QR-limit CKM matrix using
    Householder reflections (disjoint from Gram-Schmidt) on heaviest-first
    column order [perm[2], perm[1], perm[0]], then reverse columns to ascending
    physical order [1st, 2nd, 3rd].
    """
    def q_asc_from_householder(Y):
        B = mp.matrix(3, 3)
        order_desc = (perm[2], perm[1], perm[0])
        for r in range(3):
            for c in range(3):
                B[r, c] = Y[r, order_desc[c]]
        Q_desc, R = householder_qr_mp(B)
        recon_err = mat_frob_norm_mp(Q_desc * R - B)
        unit_err = mat_frob_norm_mp(Q_desc.H * Q_desc - mp.eye(3))
        subdiag_err = max(abs(R[1, 0]), abs(R[2, 0]), abs(R[2, 1]))
        Q_asc = mp.matrix([[Q_desc[r, 2 - c] for c in range(3)] for r in range(3)])
        return Q_asc, max(recon_err, unit_err, subdiag_err)

    Qu_asc, err_u = q_asc_from_householder(Yu)
    Qd_asc, err_d = q_asc_from_householder(Yd)
    V_qr = Qu_asc.H * Qd_asc
    V_qr_abs = [[abs(V_qr[r, c]) for c in range(3)] for r in range(3)]
    J_CP_qr = mp.im(V_qr[0, 0] * V_qr[1, 1] * mp.conj(V_qr[0, 1]) * mp.conj(V_qr[1, 0]))
    return V_qr_abs, J_CP_qr, max(err_u, err_d)


def run_haar_gate_5u3_mp(Yu, Yd, Ye, seed, n_trials=10, dps_haar=45):
    """
    Mandatory Guardrail 3: 10-trial random Haar U(3)^5 basis-scrambling gate at 45 dps
    with independent (U_L, U_{R,u}, U_{R,d}, U_{R,e}, U_{L,e}) generated via Householder QR.
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps_haar
    Yu_h = mp.matrix([[mp.mpc(Yu[r, c]) for c in range(3)] for r in range(3)])
    Yd_h = mp.matrix([[mp.mpc(Yd[r, c]) for c in range(3)] for r in range(3)])
    Ye_h = mp.matrix([[mp.mpc(Ye[r, c]) for c in range(3)] for r in range(3)])
    base = extract_flavor_observables_svd_mp(Yu_h, Yd_h, Ye_h)
    rng = random.Random(seed)

    max_unitarity_err = mp.mpf(0)
    max_ratio_drift = mp.mpf(0)
    max_V_drift = mp.mpf(0)
    max_JCP_drift = mp.mpf(0)
    max_Jdet_drift = mp.mpf(0)

    for _ in range(n_trials):
        UL = random_haar_u3_householder_mp(rng)
        URu = random_haar_u3_householder_mp(rng)
        URd = random_haar_u3_householder_mp(rng)
        URe = random_haar_u3_householder_mp(rng)
        ULe = random_haar_u3_householder_mp(rng)
        for U in (UL, URu, URd, URe, ULe):
            uerr = mat_frob_norm_mp(U.H * U - mp.eye(3))
            if uerr > max_unitarity_err:
                max_unitarity_err = uerr
        obs = extract_flavor_observables_svd_mp(
            UL * Yu_h * URu.H, UL * Yd_h * URd.H, ULe * Ye_h * URe.H
        )
        for sec in ("u", "d", "e"):
            for key in ("r23", "r13", "r12"):
                d = abs(obs[sec][key] - base[sec][key])
                if d > max_ratio_drift:
                    max_ratio_drift = d
        for r in range(3):
            for c in range(3):
                d = abs(obs["V_abs"][r][c] - base["V_abs"][r][c])
                if d > max_V_drift:
                    max_V_drift = d
        max_JCP_drift = max(max_JCP_drift, abs(obs["J_CP"] - base["J_CP"]))
        max_Jdet_drift = max(max_Jdet_drift, abs(obs["J_det_norm"] - base["J_det_norm"]))

    mp.mp.dps = old_dps
    max_all = max(max_ratio_drift, max_V_drift, max_JCP_drift, max_Jdet_drift)
    return {
        "n_trials": n_trials,
        "mpmath_dps": dps_haar,
        "haar_sampler": "complex_Ginibre_Householder_QR_Mezzadri",
        "max_haar_unitarity_err": mp.nstr(max_unitarity_err, 6),
        "max_ratio_drift": mp.nstr(max_ratio_drift, 6),
        "max_V_abs_drift": mp.nstr(max_V_drift, 6),
        "max_J_CP_drift": mp.nstr(max_JCP_drift, 6),
        "max_J_det_norm_drift": mp.nstr(max_Jdet_drift, 6),
        "max_overall_drift": mp.nstr(max_all, 6),
        "pass": bool(max_unitarity_err < mp.mpf(10) ** (-38) and max_all < mp.mpf(10) ** (-30)),
    }


def run_task_ow7_c(ow_data):
    dps_c = 45
    mp.mp.dps = dps_c
    phi = (1 + mp.sqrt(5)) / 2
    eps_u = phi ** (-8)    # |6 Y_R| = 4 -> phi^(-2*4)
    eps_d = phi ** (-4)    # |6 Y_R| = 2 -> phi^(-2*2)
    eps_e = phi ** (-12)   # |6 Y_R| = 6 -> phi^(-2*6)

    Yu8 = mp.matrix([[mp.mpc(ow_data[8]["Y"]["u"][r, c]) for c in range(3)] for r in range(3)])
    Yd8 = mp.matrix([[mp.mpc(ow_data[8]["Y"]["d"][r, c]) for c in range(3)] for r in range(3)])
    Ye8 = mp.matrix([[mp.mpc(ow_data[8]["Y"]["e"][r, c]) for c in range(3)] for r in range(3)])
    Yu24 = mp.matrix([[mp.mpc(ow_data[24]["Y"]["u"][r, c]) for c in range(3)] for r in range(3)])
    Yd24 = mp.matrix([[mp.mpc(ow_data[24]["Y"]["d"][r, c]) for c in range(3)] for r in range(3)])

    perm_records = {}
    all6_pass = True
    subset4_pass = True
    subset4_count = 0
    max_qr_finite_all = mp.mpf(0)
    max_qr_asymp_all = mp.mpf(0)
    max_haar_all = mp.mpf(0)
    max_hh_diag_err = mp.mpf(0)
    max_svd_diag_err = mp.mpf(0)
    max_jcp_id_err = mp.mpf(0)
    stored_Yu_eff_012 = None

    for p_idx, perm in enumerate(itertools.permutations((0, 1, 2))):
        mp.mp.dps = dps_c
        Yu_eff = apply_bulk_profile_perm_mp(Yu8, perm, eps_u)
        Yd_eff = apply_bulk_profile_perm_mp(Yd8, perm, eps_d)
        Ye_eff = apply_bulk_profile_perm_mp(Ye8, perm, eps_e)
        if perm == (0, 1, 2):
            stored_Yu_eff_012 = Yu_eff

        obs = extract_flavor_observables_svd_mp(Yu_eff, Yd_eff, Ye_eff)
        V_qr_abs, J_CP_qr, hh_err = qr_limit_householder_mp(Yu8, Yd8, perm)
        max_hh_diag_err = max(max_hh_diag_err, hh_err)
        max_svd_diag_err = max(max_svd_diag_err, obs["max_svd_err"])
        max_jcp_id_err = max(max_jcp_id_err, obs["J_CP_identity_err"])

        # Finite-eps QR deviation
        qr_diff_fin = max(
            abs(obs["V_abs"][r][c] - V_qr_abs[r][c]) for r in range(3) for c in range(3)
        )
        # Asymptotic eps_f / 1000 QR convergence
        Yu_as = apply_bulk_profile_perm_mp(Yu8, perm, eps_u / 1000)
        Yd_as = apply_bulk_profile_perm_mp(Yd8, perm, eps_d / 1000)
        obs_as = extract_flavor_observables_svd_mp(Yu_as, Yd_as, None)
        qr_diff_as = max(
            abs(obs_as["V_abs"][r][c] - V_qr_abs[r][c]) for r in range(3) for c in range(3)
        )
        jcp_diff_as = abs(abs(obs_as["J_CP"]) - abs(J_CP_qr))

        max_qr_finite_all = max(max_qr_finite_all, qr_diff_fin)
        max_qr_asymp_all = max(max_qr_asymp_all, qr_diff_as)

        # 10-trial 45-dps Haar U(3)^5 gate
        haar = run_haar_gate_5u3_mp(
            Yu_eff, Yd_eff, Ye_eff, seed=2026112150 + p_idx, n_trials=10, dps_haar=dps_c
        )
        max_haar_all = max(max_haar_all, mp.mpf(haar["max_overall_drift"]))

        u_steeper_d = obs["d"]["r13"] / obs["u"]["r13"]
        is_sub4 = (perm[2] in (0, 2))
        strict_ckm_ord = bool(obs["V_us"] > obs["V_cb"] > obs["V_ub"] > 0)

        p_ok = bool(
            obs["u"]["r13"] < mp.mpf(2) / 10000
            and obs["d"]["r13"] < mp.mpf(5) / 1000
            and obs["e"]["r13"] < mp.mpf(2) / (10 ** 6)
            and u_steeper_d > 20
            and obs["rel_ed_23"] > mp.mpf(84) / 100
            and (mp.mpf(14) / 100 < obs["V_us"] < mp.mpf(25) / 100)
            and abs(obs["J_CP"]) > mp.mpf(5) / (10 ** 5)
            and qr_diff_fin < mp.mpf(2) / 100
            and qr_diff_as < mp.mpf(1) / (10 ** 6)
            and haar["pass"]
        )
        if not p_ok:
            all6_pass = False

        sub4_ok = None
        if is_sub4:
            subset4_count += 1
            sub4_ok = bool(obs["rel_ed_23"] > mp.mpf(98) / 100 and strict_ckm_ord)
            if not sub4_ok:
                subset4_pass = False

        key = f"{perm[0]}{perm[1]}{perm[2]}"
        perm_records[key] = {
            "perm": list(perm),
            "in_4of6_hierarchical_subset": is_sub4,
            "r23_u": mp.nstr(obs["u"]["r23"], 20),
            "r13_u": mp.nstr(obs["u"]["r13"], 20),
            "r23_d": mp.nstr(obs["d"]["r23"], 20),
            "r13_d": mp.nstr(obs["d"]["r13"], 20),
            "r23_e": mp.nstr(obs["e"]["r23"], 20),
            "r13_e": mp.nstr(obs["e"]["r13"], 20),
            "u_steeper_than_d_ratio_r13d_over_r13u": mp.nstr(u_steeper_d, 15),
            "rel_ed_23": mp.nstr(obs["rel_ed_23"], 20),
            "V_us": mp.nstr(obs["V_us"], 20),
            "V_cb": mp.nstr(obs["V_cb"], 20),
            "V_ub": mp.nstr(obs["V_ub"], 20),
            "V_abs": [[mp.nstr(obs["V_abs"][r][c], 15) for c in range(3)] for r in range(3)],
            "V_QR_abs": [[mp.nstr(V_qr_abs[r][c], 15) for c in range(3)] for r in range(3)],
            "strict_hierarchical_ckm_order": strict_ckm_ord,
            "J_CP": mp.nstr(obs["J_CP"], 20),
            "J_CP_QR": mp.nstr(J_CP_qr, 20),
            "J_det_norm": mp.nstr(obs["J_det_norm"], 20),
            "qr_limit_max_abs_diff_finite": mp.nstr(qr_diff_fin, 10),
            "qr_limit_max_abs_diff_eps_div_1000": mp.nstr(qr_diff_as, 10),
            "qr_limit_JCP_diff_eps_div_1000": mp.nstr(jcp_diff_as, 10),
            "householder_qr_diag_err": mp.nstr(hh_err, 6),
            "haar_gate": haar,
            "subset4_erratum1_pass": sub4_ok,
            "pass": p_ok,
        }

    # Asymmetric covering controls: (Y_u@8, Y_d@24) and (Y_u@24, Y_d@8)
    mp.mp.dps = dps_c
    obs_u8_d24 = extract_flavor_observables_svd_mp(Yu8, Yd24, None)
    obs_u24_d8 = extract_flavor_observables_svd_mp(Yu24, Yd8, None)

    asym_u8_d24_ok = bool(
        obs_u8_d24["V_us"] > mp.mpf(5) / 100
        and abs(obs_u8_d24["J_CP"]) > mp.mpf(3) / 10000
        and obs_u8_d24["u"]["r13"] > mp.mpf(5) / 100
        and obs_u8_d24["d"]["r13"] < mp.mpf(1) / (10 ** 5)
    )
    asym_u24_d8_ok = bool(
        obs_u24_d8["V_us"] > mp.mpf(5) / 100
        and abs(obs_u24_d8["J_CP"]) > mp.mpf(3) / 10000
        and obs_u24_d8["d"]["r13"] > mp.mpf(5) / 100
        and obs_u24_d8["u"]["r13"] < mp.mpf(1) / (10 ** 5)
    )

    passed = bool(
        all6_pass
        and subset4_pass
        and subset4_count == 4
        and asym_u8_d24_ok
        and asym_u24_d8_ok
        and max_hh_diag_err < mp.mpf(10) ** (-40)
        and max_svd_diag_err < mp.mpf(10) ** (-40)
        and max_jcp_id_err < mp.mpf(10) ** (-25)
    )

    return {
        "mpmath_dps": dps_c,
        "qr_method": "Householder_reflections_Mezzadri_phase",
        "svd_method": "mp.svd_c_ascending_u_c_t_x_d_s_b",
        "geodesic_epsilons": {
            "phi": mp.nstr(phi, 30),
            "eps_u_phi_m8": mp.nstr(eps_u, 25),
            "eps_d_phi_m4": mp.nstr(eps_d, 25),
            "eps_e_phi_m12": mp.nstr(eps_e, 25),
        },
        "all_6_perms_pass": all6_pass,
        "subset_4of6_erratum1_count": subset4_count,
        "subset_4of6_erratum1_pass": subset4_pass,
        "max_qr_diff_finite_all6": mp.nstr(max_qr_finite_all, 10),
        "max_qr_diff_eps_div_1000_all6": mp.nstr(max_qr_asymp_all, 10),
        "max_haar_drift_all6": mp.nstr(max_haar_all, 6),
        "max_householder_qr_diag_err": mp.nstr(max_hh_diag_err, 6),
        "max_svd_diag_err": mp.nstr(max_svd_diag_err, 6),
        "max_J_CP_det_identity_err": mp.nstr(max_jcp_id_err, 6),
        "permutations": perm_records,
        "asymmetric_covering_controls": {
            "Yu_m8_Yd_m24": {
                "r13_u": mp.nstr(obs_u8_d24["u"]["r13"], 20),
                "r13_d": mp.nstr(obs_u8_d24["d"]["r13"], 20),
                "V_us": mp.nstr(obs_u8_d24["V_us"], 20),
                "V_cb": mp.nstr(obs_u8_d24["V_cb"], 20),
                "J_CP": mp.nstr(obs_u8_d24["J_CP"], 20),
                "pass": asym_u8_d24_ok,
            },
            "Yu_m24_Yd_m8": {
                "r13_u": mp.nstr(obs_u24_d8["u"]["r13"], 20),
                "r13_d": mp.nstr(obs_u24_d8["d"]["r13"], 20),
                "V_us": mp.nstr(obs_u24_d8["V_us"], 20),
                "V_cb": mp.nstr(obs_u24_d8["V_cb"], 20),
                "J_CP": mp.nstr(obs_u24_d8["J_CP"], 20),
                "pass": asym_u24_d8_ok,
            },
        },
        "pass": passed,
    }, stored_Yu_eff_012


# =============================================================================
# TASK OW7-D: FOUR PLANTED FAULTS (PF-OW7-1 THROUGH PF-OW7-4)
# =============================================================================

def run_task_ow7_d(ow_data, Yu_eff_012):
    # PF-OW7-1: Erroneous factor 1/2 in d/dt (d/d ln mu^2 mistake) pushes Buttazzo log10(Lambda_lam) > 15
    M_t_f = 17334 / 100
    t_hi_f = math.log((10 ** 25) / M_t_f)
    y0_but_f = [
        35830 / 100000,
        64779 / 100000,
        11666 / 10000,
        93690 / 100000,
        12604 / 100000,
    ]

    def lam_zero_event(t, y):
        return y[4]
    lam_zero_event.direction = -1

    sol_pf1 = solve_ivp(
        lambda t, y: sm_2loop_rhs_generic(y, math.pi, 1 / 2),
        (0, t_hi_f),
        y0_but_f,
        method="DOP853",
        rtol=1 / (10 ** 13),
        atol=1 / (10 ** 14),
        events=lam_zero_event,
    )
    t_zero_pf1 = float(sol_pf1.t_events[0][0]) if len(sol_pf1.t_events[0]) > 0 else None
    log10_lam_pf1 = math.log10(M_t_f) + t_zero_pf1 / math.log(10) if t_zero_pf1 is not None else None
    pf1_caught = bool(log10_lam_pf1 is not None and log10_lam_pf1 > 15)

    # PF-OW7-2: Flipping c_cross in SM from -3/2 to +1/2 reverses Xing-Zhou |V_cb| and |J_CP| ratios to < 1
    M_Z_f = 911876 / 10000
    dt_xz_f = math.log((10 ** 14) / M_Z_f)
    g0_m, Yu0_m, Yd0_m, Ye0_m = build_xing_zhou_initial_mp("SM", dps=35)
    g0_f = tuple(float(x) for x in g0_m)
    Yu0_n, Yd0_n, Ye0_n = mp_mat_to_np(Yu0_m), mp_mat_to_np(Yd0_m), mp_mat_to_np(Ye0_m)
    obs0_pf2 = extract_flavor_observables_np(Yu0_n, Yd0_n, Ye0_n)
    _, Yu1_pf2, Yd1_pf2, Ye1_pf2, _ = integrate_matrix_rge_dop853_np(
        g0_f, Yu0_n, Yd0_n, Ye0_n, dt_xz_f, "SM", c_cross_override=Fraction(1, 2)
    )
    obs1_pf2 = extract_flavor_observables_np(Yu1_pf2, Yd1_pf2, Ye1_pf2)
    vcb_rat_pf2 = obs1_pf2["V_cb"] / obs0_pf2["V_cb"]
    jcp_rat_pf2 = abs(obs1_pf2["J_CP"]) / abs(obs0_pf2["J_CP"])
    pf2_caught = bool(vcb_rat_pf2 < 1 and jcp_rat_pf2 < 1)

    # PF-OW7-3: Unphysical left-right overlap |V_u^T U_u| fails 10-trial 45-dps Haar gate with drift > 1/10
    mp.mp.dps = 45

    def lr_overlap_vtu_abs(Y):
        s = svd_sector_ascending_mp(Y)
        O = s["V_asc"].T * s["U_asc"]
        return [[abs(O[r, c]) for c in range(3)] for r in range(3)]

    base_O = lr_overlap_vtu_abs(Yu_eff_012)
    rng_pf3 = random.Random(2026112199)
    max_lr_drift = mp.mpf(0)
    for _ in range(10):
        UL = random_haar_u3_householder_mp(rng_pf3)
        UR = random_haar_u3_householder_mp(rng_pf3)
        Ot = lr_overlap_vtu_abs(UL * Yu_eff_012 * UR.H)
        for r in range(3):
            for c in range(3):
                d = abs(Ot[r][c] - base_O[r][c])
                if d > max_lr_drift:
                    max_lr_drift = d
    pf3_caught = bool(max_lr_drift > mp.mpf(1) / 10)

    # PF-OW7-4: Turning off bulk localization (D_{R,f} = I_3) at m = 24 regresses to collapsed CKM/CP
    mp.mp.dps = 45
    Yu24 = mp.matrix([[mp.mpc(ow_data[24]["Y"]["u"][r, c]) for c in range(3)] for r in range(3)])
    Yd24 = mp.matrix([[mp.mpc(ow_data[24]["Y"]["d"][r, c]) for c in range(3)] for r in range(3)])
    Ye24 = mp.matrix([[mp.mpc(ow_data[24]["Y"]["e"][r, c]) for c in range(3)] for r in range(3)])
    obs_pf4 = extract_flavor_observables_svd_mp(Yu24, Yd24, Ye24)
    pf4_caught = bool(
        obs_pf4["V_us"] < mp.mpf(1) / (10 ** 5)
        and abs(obs_pf4["J_CP"]) < mp.mpf(1) / (10 ** 15)
    )

    all_4 = bool(pf1_caught and pf2_caught and pf3_caught and pf4_caught)
    return {
        "PF_OW7_1_half_dt_factor_buttazzo": {
            "log10_Lambda_lam_GeV_fault": log10_lam_pf1,
            "caught": pf1_caught,
        },
        "PF_OW7_2_sm_ccross_flipped_to_plus_half": {
            "V_cb_ratio_fault": vcb_rat_pf2,
            "J_CP_ratio_fault": jcp_rat_pf2,
            "caught": pf2_caught,
        },
        "PF_OW7_3_unphysical_LR_overlap_VuT_Uu_haar": {
            "max_drift_10_trials": mp.nstr(max_lr_drift, 15),
            "caught": pf3_caught,
        },
        "PF_OW7_4_no_bulk_localization_m24_collapse": {
            "V_us_m24_bare": mp.nstr(obs_pf4["V_us"], 15),
            "J_CP_m24_bare": mp.nstr(obs_pf4["J_CP"], 15),
            "caught": pf4_caught,
        },
        "all_4_caught": all_4,
        "pass": all_4,
    }


# =============================================================================
# MAIN DRIVER
# =============================================================================

def main():
    t_start = time.time()
    script_path = os.path.abspath(__file__)
    out_path = os.path.join(os.path.dirname(script_path), "referee_a2_ow7_out.json")

    sec0 = audit_script_hygiene(script_path)
    t0 = time.time()
    secA = run_task_ow7_a()
    tA = time.time()
    ow_data, l2_s_err, l2_wchk = build_open_weave_yukawas(multiples=(8, 24), dps=55)
    tY = time.time()
    secB = run_task_ow7_b(ow_data)
    tB = time.time()
    secC, Yu_eff_012 = run_task_ow7_c(ow_data)
    tC = time.time()
    secD = run_task_ow7_d(ow_data, Yu_eff_012)
    tD = time.time()

    l2_ok = bool(l2_s_err < mp.mpf(10) ** (-25) and l2_wchk < mp.mpf(10) ** (-25))
    all_pass = bool(
        sec0["hygiene_pass"]
        and l2_ok
        and secA["pass"]
        and secB["pass"]
        and secC["pass"]
        and secD["pass"]
    )
    payload = {
        "card": "AGY-002_A2-OW7_plus_ERRATUM-1",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_firewall": "0 of 19 for all model predictions (published Buttazzo/Xing-Zhou isolated in OW7-A)",
        "section_0_custody_and_hygiene": sec0,
        "open_weave_yukawa_builder": {
            "L2_solver": "disjoint_3stage_GL6_order20_extrapolation_jtheta_wp_plus_Frobenius",
            "L2_S_transformation_law_err": mp.nstr(l2_s_err, 6),
            "max_L2_ode_wronskian_err": mp.nstr(l2_wchk, 6),
            "pass": l2_ok,
        },
        "task_OW7_A": secA,
        "task_OW7_B": secB,
        "task_OW7_C": secC,
        "task_OW7_D": secD,
        "timings_seconds": {
            "OW7_A": round(tA - t0, 3),
            "yukawa_build_m8_m24": round(tY - tA, 3),
            "OW7_B": round(tB - tY, 3),
            "OW7_C": round(tC - tB, 3),
            "OW7_D": round(tD - tC, 3),
            "total": round(tD - t_start, 3),
        },
        "overall_pass": all_pass,
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
    print("WROTE:", out_path)
    print("TIMINGS:", payload["timings_seconds"])


if __name__ == "__main__":
    main()
