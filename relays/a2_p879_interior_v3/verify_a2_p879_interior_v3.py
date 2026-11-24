#!/usr/bin/env python3
"""
Card A2-P879-INTERIOR (Producer v3) — Exact Universal Interior (0 <= r <= 1)
One-Doublet Trade-Off Bound for M58 / P-879 (Strictly 0 of 19).

Frozen v1 (3adf76b88) and v2 (048a143a7 -> 3eeddef8d) are preserved untouched.
v3 fixes the two bugs caught by v2's blind G4/G5 gates:
  1. Exact B1940 F_u(au, bu) digamma term -pi*(2*log(2)+log(y)+digamma(au)+digamma(1-au))
     for au != 0 and exact Jacobi theta_1'/theta_1 a_0(al, be).
  2. Cancellation-free Lagrange identity s_L = |l1_u[0]*l1_d[1] - l1_u[1]*l1_d[0]|
     in C^2 (eliminating sqrt(1 - (1 - 1e-36)) precision halving in unweighted residue check).

  - Zero empirical constants (0 of 19)
  - Zero Python float or complex AST literals
  - Zero float() / complex() casts and zero numpy/scipy/frontier imports
  - Zero JSON float tokens in output
  - Sandbox-runnable standalone
"""

import ast
from fractions import Fraction
import hashlib
import json
import math
import pathlib
import random
import time
from typing import Any, Dict, List, Tuple

import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# Exact rational / mpmath helpers (zero float or complex literals/casts)
# ---------------------------------------------------------------------------

def mp_rat(num: int, den: int = 1):
    return mp.mpf(num) / mp.mpf(den)


def mp_frac(fr: Fraction):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def mp_pow10(exp_int: int):
    return mp.power(mp.mpf(10), exp_int)


def mp_str(val, digits: int = 24) -> str:
    return mp.nstr(val, digits)


def iu():
    return mp.mpc(0, 1)


def rng_uniform_mp(rng: random.Random):
    scale = 10 ** 12
    return mp.mpf(rng.randrange(1, scale)) / mp.mpf(scale)


def rng_normal_mp(rng: random.Random):
    u1 = rng_uniform_mp(rng)
    u2 = rng_uniform_mp(rng)
    return mp.sqrt(-2 * mp.log(u1)) * mp.cos(2 * mp.pi * u2)


def rng_complex_normal_mp(rng: random.Random):
    return mp.mpc(rng_normal_mp(rng), rng_normal_mp(rng))


def svd_desc(A):
    """Exact mpmath SVD sorted in descending singular-value order.
    Returns (U, S_list, Vh) satisfying A == U * diag(S_list) * Vh."""
    U, S, Vh = mp.svd_c(A)
    n = len(S)
    order = sorted(range(n), key=lambda idx: S[idx], reverse=True)
    S_sorted = [S[i] for i in order]
    U_sorted = mp.matrix(U.rows, n)
    Vh_sorted = mp.matrix(n, Vh.cols)
    for col_new, col_old in enumerate(order):
        for r in range(U.rows):
            U_sorted[r, col_new] = U[r, col_old]
        for c in range(Vh.cols):
            Vh_sorted[col_new, c] = Vh[col_old, c]
    return U_sorted, S_sorted, Vh_sorted


def svd2_top_and_sv(M):
    """Exact cancellation-free closed-form 2x2 SVD: returns (u1, s1, s2)
    where u1 is top unit left singular vector and s2 = |det(M)| / s1."""
    a = abs(M[0, 0]) ** 2 + abs(M[0, 1]) ** 2
    d = abs(M[1, 0]) ** 2 + abs(M[1, 1]) ** 2
    b = M[0, 0] * mp.conj(M[1, 0]) + M[0, 1] * mp.conj(M[1, 1])
    tr = a + d
    diff = a - d
    disc = mp.sqrt(diff * diff + 4 * (abs(b) ** 2))
    lam1 = (tr + disc) / 2
    s1 = mp.sqrt(lam1)
    det_abs = abs(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])
    s2 = det_abs / s1 if s1 > 0 else mp.mpf(0)
    if abs(b) == 0:
        u1 = [mp.mpc(1), mp.mpc(0)] if a >= d else [mp.mpc(0), mp.mpc(1)]
    elif a >= d:
        v0 = lam1 - d
        v1 = mp.conj(b)
        nrm = mp.sqrt(abs(v0) ** 2 + abs(v1) ** 2)
        u1 = [v0 / nrm, v1 / nrm]
    else:
        v0 = b
        v1 = lam1 - a
        nrm = mp.sqrt(abs(v0) ** 2 + abs(v1) ** 2)
        u1 = [v0 / nrm, v1 / nrm]
    return u1, s1, s2


def mat_frob_norm(A):
    tot = mp.mpf(0)
    for r in range(A.rows):
        for c in range(A.cols):
            tot += abs(A[r, c]) ** 2
    return mp.sqrt(tot)


def vec_norm(v):
    return mp.sqrt(sum(abs(x) ** 2 for x in v))


def vec_inner(a, b):
    return sum(mp.conj(a[i]) * b[i] for i in range(len(a)))


def vec_bilinear(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


def spinor_pairing_sL(u, v):
    """Exact cancellation-free Lagrange identity in C^2:
    sqrt(1 - |<u|v>|^2) == |u_0 v_1 - u_1 v_0| for unit spinors u, v."""
    return abs(u[0] * v[1] - u[1] * v[0])


def gram_schmidt_haar_u(rng: random.Random, n: int):
    """Mezzadri (2007) Haar-distributed unitary in U(n) in pure mpmath."""
    Z = mp.matrix([[rng_complex_normal_mp(rng) for _ in range(n)] for _ in range(n)])
    Q = mp.matrix(n, n)
    for j in range(n):
        v = [Z[r, j] for r in range(n)]
        for k in range(j):
            qk = [Q[r, k] for r in range(n)]
            proj = vec_inner(qk, v)
            v = [v[r] - proj * qk[r] for r in range(n)]
        nrm = vec_norm(v)
        rjj = vec_inner([v[r] / nrm for r in range(n)], [Z[r, j] for r in range(n)])
        ph = rjj / abs(rjj)
        for r in range(n):
            Q[r, j] = (v[r] / nrm) * ph
    return Q


def rand_so3_mp(rng: random.Random):
    Z = mp.matrix([[rng_normal_mp(rng) for _ in range(3)] for _ in range(3)])
    Q = mp.matrix(3, 3)
    for j in range(3):
        v = [Z[r, j] for r in range(3)]
        for k in range(j):
            qk = [Q[r, k] for r in range(3)]
            proj = sum(qk[r] * v[r] for r in range(3))
            v = [v[r] - proj * qk[r] for r in range(3)]
        nrm = vec_norm(v)
        sgn = mp.mpf(1) if sum((v[r] / nrm) * Z[r, j] for r in range(3)) >= 0 else mp.mpf(-1)
        for r in range(3):
            Q[r, j] = (v[r] / nrm) * sgn
    if mp.re(mp.det(Q)) < 0:
        for r in range(3):
            Q[r, 0] = -Q[r, 0]
    return Q


# ---------------------------------------------------------------------------
# Pauli matrices, B1736 coupling Y(h; u, w), and analytic bound formulas
# ---------------------------------------------------------------------------

def paulis_mp():
    I = iu()
    sx = mp.matrix([[0, 1], [1, 0]])
    sy = mp.matrix([[0, -I], [I, 0]])
    sz = mp.matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def H_from_h_mp(h):
    sx, sy, sz = paulis_mp()
    return h[0] * sx + h[1] * sy + h[2] * sz


def M_from_uw_mp(u, w, sign_w: int = -1):
    sx, sy, sz = paulis_mp()
    return (sign_w * iu() * w) * mp.eye(2) + u[0] * sx + u[1] * sy + u[2] * sz


def Y_b1736_mp(h, u, w):
    uh = vec_bilinear(u, h)
    hx = mp.matrix([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])
    Y = mp.matrix(3, 3)
    for a in range(3):
        for b in range(3):
            Y[a, b] = u[a] * h[b] + h[a] * u[b] - (uh if a == b else 0) + w * hx[a, b]
    return Y


def Y_kron_mp(H, M):
    sigs = paulis_mp()
    Y = mp.matrix(3, 3)
    for b in range(3):
        Z = H * sigs[b] * M
        Y[0, b] = (Z[0, 1] + Z[1, 0]) / 2
        Y[1, b] = (iu() * Z[0, 1] - iu() * Z[1, 0]) / 2
        Y[2, b] = (Z[0, 0] - Z[1, 1]) / 2
    return Y


def canon_h_mp(t_val):
    denom = mp.sqrt(1 + t_val * t_val)
    cp = mp.mpf(1) / denom
    cm = t_val / denom
    s2 = mp.sqrt(2)
    ep = [mp.mpf(1) / s2, iu() / s2, mp.mpc(0)]
    em = [mp.mpf(1) / s2, -iu() / s2, mp.mpc(0)]
    return [cp * em[k] + cm * ep[k] for k in range(3)]


def t_from_r_mp(r_val):
    return r_val / (1 + mp.sqrt(max(mp.mpf(0), 1 - r_val * r_val)))


def S_unif_mp(rho):
    return mp.sqrt(2 * rho * (1 + 2 * rho)) + 2 * rho


def S_of_t_rho_mp(t_val, rho):
    m_star = mp.sqrt(rho / (2 * (1 + 2 * rho)))
    if t_val <= m_star:
        return S_unif_mp(rho)
    return rho * (1 + 2 * t_val) / t_val


def V33_ceiling_mp(sL, rho, t_val=None):
    if rho >= mp_rat(1, 6):
        return mp.mpf(1)
    arg0 = min(mp.mpf(1), max(mp.mpf(-1), (1 + sL) / (3 - sL)))
    th0 = mp.acos(arg0)
    s_val = S_unif_mp(rho) if t_val is None else S_of_t_rho_mp(t_val, rho)
    s_val = min(mp.mpf(1), max(mp.mpf(0), s_val))
    rem = th0 - 2 * mp.asin(s_val)
    if rem <= 0:
        return mp.mpf(1)
    return mp.cos(rem)


def S_req_mp(sL, align_a):
    arg0 = min(mp.mpf(1), max(mp.mpf(-1), (1 + sL) / (3 - sL)))
    arga = min(mp.mpf(1), max(mp.mpf(-1), align_a))
    gap = mp.acos(arg0) - mp.acos(arga)
    if gap <= 0:
        return mp.mpf(0)
    return mp.sin(gap / 2)


def F_three_regime_mp(t_val, sL, align_a):
    S = S_req_mp(sL, align_a)
    t1 = S / (2 * (1 + S)) if S > 0 else mp.mpf(0)
    t2 = S
    if t_val <= t1:
        return (S * S) / (2 * (1 + 2 * S))
    if t_val <= t2:
        return (S * t_val) / (1 + 2 * t_val)
    return (t_val * t_val) / (1 + 2 * t_val)


def sL_critical_mp(align_a, rho):
    th_max = mp.acos(align_a) + 2 * mp.asin(S_unif_mp(rho))
    c = mp.cos(th_max)
    return (3 * c - 1) / (1 + c)


def mw_to_uw_mp(Mw):
    I = iu()
    m0 = (Mw[0, 0] + Mw[1, 1]) / 2
    m1 = (Mw[0, 0] - Mw[1, 1]) / (2 * I)
    m2 = (Mw[0, 1] - Mw[1, 0]) / 2
    m3 = (Mw[0, 1] + Mw[1, 0]) / (2 * I)
    u = [-2 * m0, 2 * m3, -2 * m1]
    w = -2 * m2
    return u, w


# ---------------------------------------------------------------------------
# Gate G0: Self-AST, custody, and JSON-float auditor
# ---------------------------------------------------------------------------

def check_ast_and_custody(self_path: pathlib.Path) -> Dict[str, Any]:
    src = self_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(self_path))
    float_lits: List[Tuple[int, str]] = []
    bad_casts: List[Tuple[int, str]] = []
    bad_imports: List[str] = []
    forbidden = {"frontier", "numpy", "scipy"}

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            float_lits.append((node.lineno, repr(node.value)))
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
                bad_casts.append((node.lineno, node.func.id))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in forbidden:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            root = mod.split(".")[0]
            if root in forbidden:
                bad_imports.append(mod)

    digest = hashlib.sha256(src.encode("utf-8")).hexdigest()
    sha_file = self_path.parent / "SCRIPT_SHA256.txt"
    if sha_file.is_file():
        recorded = sha_file.read_text(encoding="utf-8").strip().split()[0]
        sha_status = "verified_match" if recorded == digest else "MISMATCH"
        sha_ok = recorded == digest
    else:
        sha_status = "sandbox_standalone_no_manifest"
        sha_ok = True

    passed = (len(float_lits) == 0 and len(bad_casts) == 0 and len(bad_imports) == 0 and sha_ok)
    return {
        "float_or_complex_literals": len(float_lits),
        "float_or_complex_casts": len(bad_casts),
        "bad_imports": bad_imports,
        "script_sha256": digest,
        "sha_manifest_status": sha_status,
        "passed": passed,
    }


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


# ---------------------------------------------------------------------------
# Gate G1 (M1): Exact 4x4 Kronecker, M = 2 L_u Mw^T R_u, Bell Projection
# ---------------------------------------------------------------------------

def run_G1_M1() -> Dict[str, Any]:
    h1, h2, h3, u1, u2, u3, w = sp.symbols("h1 h2 h3 u1 u2 u3 w")
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)
    sigs = [sx, sy, sz]
    H_sym = h1 * sx + h2 * sy + h3 * sz
    M_sym = -sp.I * w * I2 + u1 * sx + u2 * sy + u3 * sz
    Y_k = sp.Matrix(3, 3, lambda a, b: sp.expand(sp.Rational(1, 2) * (sigs[a] * H_sym * sigs[b] * M_sym).trace()))
    hv = sp.Matrix([h1, h2, h3])
    uv = sp.Matrix([u1, u2, u3])
    hx = sp.Matrix([[0, -h3, h2], [h3, 0, -h1], [-h2, h1, 0]])
    Y_b = uv * hv.T + hv * uv.T - (uv.dot(hv)) * sp.eye(3) + w * hx
    kron_diff_zero = (sp.simplify(Y_k - Y_b) == sp.zeros(3, 3))

    m00, m01, m10, m11 = sp.symbols("m00 m01 m10 m11")
    Mw_s = sp.Matrix([[m00, m01], [m10, m11]])
    m0 = (m00 + m11) / 2
    m1 = (m00 - m11) / (2 * sp.I)
    m2 = (m01 - m10) / 2
    m3 = (m01 + m10) / (2 * sp.I)
    us = sp.Matrix([-2 * m0, 2 * m3, -2 * m1])
    ws = -2 * m2
    M_from_mw = -sp.I * ws * I2 + us[0] * sx + us[1] * sy + us[2] * sz
    H2 = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    L_u = sp.Matrix([[1, 0], [0, sp.I]]) * H2
    R_u = H2 * sp.Matrix([[0, -1], [sp.I, 0]])
    mw_map_zero = (sp.simplify(M_from_mw - 2 * L_u * Mw_s.T * R_u) == sp.zeros(2, 2))
    Lu_unitary = (sp.simplify(L_u.H * L_u - I2) == sp.zeros(2, 2))
    Ru_unitary = (sp.simplify(R_u.H * R_u - I2) == sp.zeros(2, 2))

    mp.mp.dps = 40
    rng = random.Random(20261124)
    max_kron_err = mp.mpf(0)
    max_svd_rec_err = mp.mpf(0)
    max_svd2_err = mp.mpf(0)
    max_kap_err = mp.mpf(0)
    max_sL_err = mp.mpf(0)
    max_bell_err = mp.mpf(0)
    e0_vec = [mp.mpf(1) / mp.sqrt(2), mp.mpc(0), mp.mpc(0), mp.mpf(1) / mp.sqrt(2)]

    for _ in range(20):
        h = [rng_complex_normal_mp(rng) for _ in range(3)]
        Mwu = mp.matrix([[rng_complex_normal_mp(rng) for _ in range(2)] for _ in range(2)])
        Mwd = mp.matrix([[rng_complex_normal_mp(rng) for _ in range(2)] for _ in range(2)])
        uu, wu = mw_to_uw_mp(Mwu)
        ud, wd = mw_to_uw_mp(Mwd)
        H = H_from_h_mp(h)
        Mu = M_from_uw_mp(uu, wu)
        Md = M_from_uw_mp(ud, wd)

        Yb = Y_b1736_mp(h, ud, wd)
        Yk = Y_kron_mp(H, Md)
        max_kron_err = max(max_kron_err, mat_frob_norm(Yb - Yk))

        Uy, Sy, Vhy = svd_desc(Yb)
        max_svd_rec_err = max(max_svd_rec_err, mat_frob_norm(Uy * mp.diag(Sy) * Vhy - Yb))

        _, Smu, Vhmu = svd_desc(Mu)
        Umd, Smd, Vhmd = svd_desc(Md)
        Umwu, Smwu, _ = svd_desc(Mwu)
        Umwd, Smwd, _ = svd_desc(Mwd)

        u1c, s1c, s2c = svd2_top_and_sv(Mwu)
        max_svd2_err = max(
            max_svd2_err,
            abs(s1c - Smwu[0]),
            abs(s2c - Smwu[1]),
            spinor_pairing_sL(u1c, [Umwu[0, 0], Umwu[1, 0]]),
        )

        max_kap_err = max(max_kap_err, abs(Smu[1] / Smu[0] - Smwu[1] / Smwu[0]))
        max_kap_err = max(max_kap_err, abs(Smd[1] / Smd[0] - Smwd[1] / Smwd[0]))

        r1u = [mp.conj(Vhmu[0, c]) for c in range(2)]
        r1d = [mp.conj(Vhmd[0, c]) for c in range(2)]
        l1u_mw = [Umwu[r, 0] for r in range(2)]
        l1d_mw = [Umwd[r, 0] for r in range(2)]
        sL_M = spinor_pairing_sL(r1u, r1d)
        sL_Mw = spinor_pairing_sL(l1u_mw, l1d_mw)
        max_sL_err = max(max_sL_err, abs(sL_M - sL_Mw))

        UH, SH, VhH = svd_desc(H)
        a1 = [UH[r, 0] for r in range(2)]
        a2 = [UH[r, 1] for r in range(2)]
        b1 = [Vhmd[0, c] for c in range(2)]
        b2 = [Vhmd[1, c] for c in range(2)]
        t_val = SH[1] / SH[0]
        kap_val = Smd[1] / Smd[0]
        u1 = [a1[i] * b1[j] for i in range(2) for j in range(2)]
        u2 = [a2[i] * b1[j] for i in range(2) for j in range(2)] if t_val >= kap_val else [a1[i] * b2[j] for i in range(2) for j in range(2)]
        proj_U12 = abs(vec_inner(u1, e0_vec)) ** 2 + abs(vec_inner(u2, e0_vec)) ** 2
        max_bell_err = max(max_bell_err, abs(proj_U12 - mp_rat(1, 2)))

        g1 = [mp.conj(VhH[0, c]) for c in range(2)]
        g2 = [mp.conj(VhH[1, c]) for c in range(2)]
        d1 = [mp.conj(Umd[r, 0]) for r in range(2)]
        d2 = [mp.conj(Umd[r, 1]) for r in range(2)]
        v1 = [g1[i] * d1[j] for i in range(2) for j in range(2)]
        v2 = [g2[i] * d1[j] for i in range(2) for j in range(2)] if t_val >= kap_val else [g1[i] * d2[j] for i in range(2) for j in range(2)]
        proj_V12 = abs(vec_inner(v1, e0_vec)) ** 2 + abs(vec_inner(v2, e0_vec)) ** 2
        max_bell_err = max(max_bell_err, abs(proj_V12 - mp_rat(1, 2)))

    tol = mp_pow10(-30)
    passed = (
        kron_diff_zero and mw_map_zero and Lu_unitary and Ru_unitary
        and max_kron_err < tol and max_svd_rec_err < tol and max_svd2_err < tol
        and max_kap_err < tol and max_sL_err < tol and max_bell_err < tol
    )
    return {
        "sympy_kron_zero": kron_diff_zero,
        "sympy_mw_unitary_map_zero": mw_map_zero,
        "sympy_Lu_unitary": Lu_unitary,
        "sympy_Ru_unitary": Ru_unitary,
        "max_kron_err": mp_str(max_kron_err, 8),
        "max_svd_rec_err": mp_str(max_svd_rec_err, 8),
        "max_svd2_closed_form_err": mp_str(max_svd2_err, 8),
        "max_kap_err": mp_str(max_kap_err, 8),
        "max_sL_err": mp_str(max_sL_err, 8),
        "max_bell_proj_err": mp_str(max_bell_err, 8),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G2 (M2): Exact Sharp Two-Variable Floor & Universal Reality Floor
# ---------------------------------------------------------------------------

def run_G2_M2() -> Dict[str, Any]:
    t_s, k_s, r_s, S_s = sp.symbols("t k rho S", positive=True)
    k_star = t_s / (1 + 2 * t_s)
    sym_min_eq = (sp.simplify(t_s * k_star - (t_s - k_star) / 2) == 0)
    sym_min_val = (sp.simplify(t_s * k_star - t_s ** 2 / (1 + 2 * t_s)) == 0)

    M_star = sp.sqrt(r_s / (2 * (1 + 2 * r_s)))
    S_closed = sp.sqrt(2 * r_s * (1 + 2 * r_s)) + 2 * r_s
    sym_cross_eq = (sp.simplify(M_star / (sp.Rational(1, 2) - M_star) - r_s * (1 + 2 * M_star) / M_star) == 0)
    sym_S_closed = (sp.simplify(M_star / (sp.Rational(1, 2) - M_star) - S_closed) == 0)

    rho_inv = S_s ** 2 / (2 * (1 + 2 * S_s))
    rad = sp.factor(2 * rho_inv * (1 + 2 * rho_inv))
    sym_rad_sq = (sp.simplify(rad - (S_s * (S_s + 1) / (2 * S_s + 1)) ** 2) == 0)
    sym_S_inv = (sp.simplify(S_s * (S_s + 1) / (2 * S_s + 1) + 2 * rho_inv - S_s) == 0)

    t1_s = S_s / (2 * (1 + S_s))
    t2_s = S_s
    sym_junc1 = (sp.simplify(S_s * t1_s / (1 + 2 * t1_s) - rho_inv) == 0)
    sym_junc2 = (sp.simplify(S_s * t2_s / (1 + 2 * t2_s) - t2_s ** 2 / (1 + 2 * t2_s)) == 0)

    A_w = sp.Matrix([[0, -2 * t_s * k_s, 0], [2, 0, 0], [0, 0, -(t_s - k_s)]])
    evs = {sp.expand(sp.simplify(e)) for e in (A_w.H * A_w).eigenvals().keys()}
    expected_evs = {sp.Integer(4), 4 * t_s ** 2 * k_s ** 2, sp.expand((t_s - k_s) ** 2)}
    sym_witness_evs = (evs == expected_evs)

    mp.mp.dps = 50
    r_grid = [
        Fraction(0, 1), Fraction(1, 100), Fraction(1, 20), Fraction(1, 10),
        Fraction(1, 5), Fraction(3, 10), Fraction(1, 2), Fraction(7, 10),
        Fraction(17, 20), Fraction(19, 20), Fraction(1, 1),
    ]
    s2 = mp.sqrt(2)
    ep = [mp.mpf(1) / s2, iu() / s2, mp.mpc(0)]
    em = [mp.mpf(1) / s2, -iu() / s2, mp.mpc(0)]
    max_witness_err = mp.mpf(0)
    witness_table: List[Dict[str, str]] = []
    for rf in r_grid:
        rv = mp_frac(rf)
        tv = t_from_r_mp(rv)
        kv = tv / (1 + 2 * tv)
        hv = canon_h_mp(tv)
        uv = [em[j] - kv * ep[j] for j in range(3)]
        Y = Y_b1736_mp(hv, uv, mp.mpc(0))
        _, sv, _ = svd_desc(Y)
        rho_w = sv[1] / sv[0]
        floor_w = (tv * tv) / (1 + 2 * tv)
        err_w = abs(rho_w - floor_w)
        max_witness_err = max(max_witness_err, err_w)
        witness_table.append({
            "r": str(rf),
            "t": mp_str(tv, 16),
            "rho_witness": mp_str(rho_w, 16),
            "floor_t2_over_1p2t": mp_str(floor_w, 16),
            "err": mp_str(err_w, 6),
        })

    mp.mp.dps = 28
    rng = random.Random(202601)
    n_trials = 2000
    v_m2 = 0
    v_rho_tk = 0
    v_rho_t = 0
    min_gap_m2 = mp.mpf(10)
    min_gap_rho_t = mp.mpf(10)
    tol_viol = mp_pow10(-25)

    for idx in range(n_trials):
        if idx % 5 < 2:
            tv = rng_uniform_mp(rng) * mp_rat(1, 5)
            kv = rng_uniform_mp(rng) * mp_rat(1, 5)
        else:
            tv = rng_uniform_mp(rng)
            kv = rng_uniform_mp(rng)
        O = rand_so3_mp(rng)
        hc = canon_h_mp(tv)
        h = [sum(O[r, c] * hc[c] for c in range(3)) for r in range(3)]
        H = H_from_h_mp(h)
        sH1 = mp.sqrt(mp.mpf(2) / (1 + tv * tv))
        UM = gram_schmidt_haar_u(rng, 2)
        VM = gram_schmidt_haar_u(rng, 2)
        M = UM * mp.diag([mp.mpf(1), kv]) * VM.H
        Y_hat = Y_kron_mp(H, M) / sH1
        _, sv, _ = svd_desc(Y_hat)
        m3, m2 = sv[0], sv[1]
        rho = m2 / m3
        fl_tk = max(tv * kv, abs(tv - kv) / 2)
        fl_t = (tv * tv) / (1 + 2 * tv)
        if m2 < fl_tk - tol_viol:
            v_m2 += 1
        if rho < fl_tk - tol_viol:
            v_rho_tk += 1
        if rho < fl_t - tol_viol:
            v_rho_t += 1
        min_gap_m2 = min(min_gap_m2, m2 - fl_tk)
        min_gap_rho_t = min(min_gap_rho_t, rho - fl_t)

    passed = (
        sym_min_eq and sym_min_val and sym_cross_eq and sym_S_closed
        and sym_rad_sq and sym_S_inv and sym_junc1 and sym_junc2 and sym_witness_evs
        and max_witness_err < mp_pow10(-45)
        and v_m2 == 0 and v_rho_tk == 0 and v_rho_t == 0
    )
    return {
        "sympy_all_9_identities_zero": (
            sym_min_eq and sym_min_val and sym_cross_eq and sym_S_closed
            and sym_rad_sq and sym_S_inv and sym_junc1 and sym_junc2 and sym_witness_evs
        ),
        "witness_11_max_err": mp_str(max_witness_err, 8),
        "witness_r1_floor": witness_table[-1]["rho_witness"],
        "witness_table": witness_table,
        "random_trials": n_trials,
        "violations_m2_ge_fl_tk": v_m2,
        "violations_rho_ge_fl_tk": v_rho_tk,
        "violations_rho_ge_fl_t": v_rho_t,
        "min_gap_m2_minus_fl_tk": mp_str(min_gap_m2, 8),
        "min_gap_rho_minus_fl_t": mp_str(min_gap_rho_t, 8),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G3 (M3): Single-Sector Perturbation, Two-Sector Bound, & Controls
# ---------------------------------------------------------------------------

def run_G3_M3() -> Dict[str, Any]:
    mp.mp.dps = 28
    rng = random.Random(202602)
    sigs = paulis_mp()
    n_trials = 2000
    tol_viol = mp_pow10(-25)

    v_sin_M = 0
    v_sin_St = 0
    v_V33 = 0
    v_F = 0
    max_sin_over_M = mp.mpf(0)
    max_sin_over_St = mp.mpf(0)
    max_V33_minus_bnd = mp.mpf(-10)
    min_rho_minus_F = mp.mpf(10)
    n_rho_lt_1_6 = 0

    for idx in range(n_trials):
        if idx % 10 < 7:
            tv = rng_uniform_mp(rng) * mp_rat(7, 20)
            ku = rng_uniform_mp(rng) * mp_rat(7, 20)
            kd = rng_uniform_mp(rng) * mp_rat(7, 20)
        else:
            tv = rng_uniform_mp(rng) * mp_rat(999, 1000)
            ku = rng_uniform_mp(rng) * mp_rat(999, 1000)
            kd = rng_uniform_mp(rng) * mp_rat(999, 1000)
        O = rand_so3_mp(rng)
        hc = canon_h_mp(tv)
        h = [sum(O[r, c] * hc[c] for c in range(3)) for r in range(3)]
        hb = [mp.conj(z) for z in h]
        Hd = H_from_h_mp(h)
        Hu = H_from_h_mp(hb)
        a1d, sHd1, _ = svd2_top_and_sv(Hd)
        a1u, sHu1, _ = svd2_top_and_sv(Hu)

        UMu = gram_schmidt_haar_u(rng, 2)
        VMu = gram_schmidt_haar_u(rng, 2)
        UMd = gram_schmidt_haar_u(rng, 2)
        VMd = gram_schmidt_haar_u(rng, 2)
        Mu = UMu * mp.diag([mp.mpf(1), ku]) * VMu.H
        Md = UMd * mp.diag([mp.mpf(1), kd]) * VMd.H
        r1u = [VMu[r, 0] for r in range(2)]
        r1d = [VMd[r, 0] for r in range(2)]
        sL = spinor_pairing_sL(r1u, r1d)

        Yu_h = Y_kron_mp(Hu, Mu) / sHu1
        Yd_h = Y_kron_mp(Hd, Md) / sHd1
        Uu, Su, _ = svd_desc(Yu_h)
        Ud, Sd, _ = svd_desc(Yd_h)
        rho_u = Su[1] / Su[0]
        rho_d = Sd[1] / Sd[0]
        rho = max(rho_u, rho_d)

        for (a1, r1f, Uf, Sf, kf, rhof) in (
            (a1u, r1u, Uu, Su, ku, rho_u),
            (a1d, r1d, Ud, Sd, kd, rho_d),
        ):
            X1 = mp.matrix([[a1[r] * mp.conj(r1f[c]) for c in range(2)] for r in range(2)])
            vh = [((sigs[k] * X1)[0, 0] + (sigs[k] * X1)[1, 1]) / 2 for k in range(3)]
            vn = vec_norm(vh)
            vh = [z / vn for z in vh]
            u3 = [Uf[r, 0] for r in range(3)]
            sin_th = mp.sqrt(max(mp.mpf(0), 1 - abs(vec_inner(u3, vh)) ** 2))
            M_f = max(tv, kf)
            if sin_th > M_f / Sf[0] + tol_viol:
                v_sin_M += 1
            if M_f > 0:
                max_sin_over_M = max(max_sin_over_M, sin_th / (M_f / Sf[0]))
            if rhof < mp_rat(1, 6):
                St = S_of_t_rho_mp(tv, rhof)
                if sin_th > St + tol_viol:
                    v_sin_St += 1
                if St > 0:
                    max_sin_over_St = max(max_sin_over_St, sin_th / St)

        u3u = [Uu[r, 0] for r in range(3)]
        u3d = [Ud[r, 0] for r in range(3)]
        v33 = abs(vec_inner(u3u, u3d))

        if rho < mp_rat(1, 6):
            n_rho_lt_1_6 += 1
            vbnd = V33_ceiling_mp(sL, rho, tv)
            if v33 > vbnd + tol_viol:
                v_V33 += 1
            max_V33_minus_bnd = max(max_V33_minus_bnd, v33 - vbnd)

        F_val = F_three_regime_mp(tv, sL, v33)
        if rho < F_val - tol_viol:
            v_F += 1
        min_rho_minus_F = min(min_rho_minus_F, rho - F_val)

    mp.mp.dps = 50
    s2 = mp.sqrt(2)
    ep = [mp.mpf(1) / s2, iu() / s2, mp.mpc(0)]
    em = [mp.mpf(1) / s2, -iu() / s2, mp.mpc(0)]

    r_c1 = mp_rat(1, 2000)
    t_c1 = t_from_r_mp(r_c1)
    h_c1 = canon_h_mp(t_c1)
    hb_c1 = [mp.conj(z) for z in h_c1]
    ud_c1 = [ep[k] + mp_rat(4, 1000) * em[k] for k in range(3)]
    uu_c1 = [mp_rat(1, 80000) * ep[k] + em[k] for k in range(3)]
    Mu_c1 = M_from_uw_mp(uu_c1, mp.mpc(0))
    Md_c1 = M_from_uw_mp(ud_c1, mp.mpc(0))
    _, _, VhMu_c1 = svd_desc(Mu_c1)
    _, _, VhMd_c1 = svd_desc(Md_c1)
    sL_c1 = spinor_pairing_sL([mp.conj(VhMu_c1[0, c]) for c in range(2)], [mp.conj(VhMd_c1[0, c]) for c in range(2)])
    Uu_c1, Su_c1, _ = svd_desc(Y_b1736_mp(hb_c1, uu_c1, mp.mpc(0)))
    Ud_c1, Sd_c1, _ = svd_desc(Y_b1736_mp(h_c1, ud_c1, mp.mpc(0)))
    v33_c1 = abs(vec_inner([Uu_c1[r, 0] for r in range(3)], [Ud_c1[r, 0] for r in range(3)]))
    rho_c1 = max(Su_c1[1] / Su_c1[0], Sd_c1[1] / Sd_c1[0])
    F_c1 = F_three_regime_mp(t_c1, sL_c1, v33_c1)
    c1_ok = (abs(sL_c1 - 1) < mp_pow10(-45) and abs(v33_c1 - 1) < mp_pow10(-45) and rho_c1 >= F_c1)

    raw_pairs = [
        (8112623, 23657898), (-32191861, 58976063), (8361869, 35299624),
        (29517392, 42170071), (10109002, 39589433), (201121, 6549724),
        (32621059, 80596130), (-2122066, 7900781),
        (8253345, 14846974), (13917810, 48354631), (29492199, 87199192),
        (32273371, 84797632), (-69799368, 69016585), (-23893336, 16802917),
        (126906246, 75918835), (16923861, 50797165),
    ]
    vals = [mp_rat(n, d) for n, d in raw_pairs]
    I = iu()
    uu_b = [vals[0] + I * vals[3], vals[1] + I * vals[4], vals[2] + I * vals[5]]
    wu_b = vals[6] + I * vals[7]
    ud_b = [vals[8] + I * vals[11], vals[9] + I * vals[12], vals[10] + I * vals[13]]
    wd_b = vals[14] + I * vals[15]
    r_b = mp_rat(3, 1000)
    t_b = t_from_r_mp(r_b)
    th_b = mp.acos(r_b) / 2
    h_b = [mp.cos(th_b), I * mp.sin(th_b), mp.mpc(0)]
    hb_b = [mp.conj(z) for z in h_b]
    Mu_b = M_from_uw_mp(uu_b, wu_b)
    Md_b = M_from_uw_mp(ud_b, wd_b)
    _, _, VhMu_b = svd_desc(Mu_b)
    _, _, VhMd_b = svd_desc(Md_b)
    sL_b = spinor_pairing_sL([mp.conj(VhMu_b[0, c]) for c in range(2)], [mp.conj(VhMd_b[0, c]) for c in range(2)])
    Uu_b, Su_b, _ = svd_desc(Y_b1736_mp(hb_b, uu_b, wu_b))
    Ud_b, Sd_b, _ = svd_desc(Y_b1736_mp(h_b, ud_b, wd_b))
    v33_b = abs(vec_inner([Uu_b[r, 0] for r in range(3)], [Ud_b[r, 0] for r in range(3)]))
    rho_b = max(Su_b[1] / Su_b[0], Sd_b[1] / Sd_b[0])
    F_b = F_three_regime_mp(t_b, sL_b, v33_b)
    sL_crit_90_01 = sL_critical_mp(mp_rat(9, 10), mp_rat(1, 100))
    b1967_ok = (sL_b > sL_crit_90_01 and v33_b >= mp_rat(9, 10) and rho_b < mp_rat(1, 100) and rho_b >= F_b)

    F_r1_zero = F_three_regime_mp(mp.mpf(1), mp.mpf(0), mp_rat(9, 10))
    F_r1_one = F_three_regime_mp(mp.mpf(1), mp.mpf(1), mp.mpf(1))
    r1_ok = (abs(F_r1_zero - mp_rat(1, 3)) < mp_pow10(-45) and abs(F_r1_one - mp_rat(1, 3)) < mp_pow10(-45))

    passed = (
        v_sin_M == 0 and v_sin_St == 0 and v_V33 == 0 and v_F == 0
        and c1_ok and b1967_ok and r1_ok
    )
    return {
        "random_two_sector_trials": n_trials,
        "trials_with_rho_lt_1_6": n_rho_lt_1_6,
        "violations_sin_le_M_over_m3": v_sin_M,
        "violations_sin_le_St": v_sin_St,
        "violations_V33_le_ceiling": v_V33,
        "violations_rho_ge_F": v_F,
        "max_sin_over_M_m3": mp_str(max_sin_over_M, 8),
        "max_sin_over_St": mp_str(max_sin_over_St, 8),
        "max_V33_minus_ceiling": mp_str(max_V33_minus_bnd, 8),
        "min_rho_minus_F": mp_str(min_rho_minus_F, 8),
        "sL_critical_at_a9_10_rho1_100": mp_str(sL_crit_90_01, 12),
        "control_C1A": {
            "sL": mp_str(sL_c1, 12), "V33": mp_str(v33_c1, 12),
            "rho": mp_str(rho_c1, 12), "F_bound": mp_str(F_c1, 12), "ok": c1_ok,
        },
        "control_B1967": {
            "sL": mp_str(sL_b, 12), "V33": mp_str(v33_b, 12),
            "rho": mp_str(rho_b, 12), "F_bound": mp_str(F_b, 12), "ok": b1967_ok,
        },
        "control_r1_B1727_exact": r1_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Fast Pure-mpmath Frame C Engine (Coarse-to-Fine RK4 L_2 + Exact B1940 F_u/a0)
# ---------------------------------------------------------------------------

def solve_L2_fast_mp(tau, dps: int = 25):
    """Coarse-to-fine pure-mpmath Richardson-RK4 Weierstrass L_2(tau) solver."""
    mp.mp.dps = dps
    I = iu()
    pi = mp.pi
    ty = mp.im(tau)
    q = mp.exp(2 * I * pi * tau)
    y_int = max(1, int(mp.floor(ty)))
    K = max(4, (dps * 231) // (628 * y_int) + 3)
    e2 = mp.mpf(1)
    e4 = mp.mpf(1)
    e6 = mp.mpf(1)
    dn = []
    qn = mp.mpc(1)
    for n in range(1, K + 1):
        qn = qn * q
        d = 1 - qn
        dn.append(d)
        e2 -= 24 * n * qn / d
        e4 += 240 * (n ** 3) * qn / d
        e6 -= 504 * (n ** 5) * qn / d
    g2 = mp_rat(4, 3) * (pi ** 4) * e4
    g3 = mp_rat(8, 27) * (pi ** 6) * e6

    def wp(z):
        mt = int(mp.nint(mp.im(z) / ty))
        n1 = int(mp.nint(mp.re(z - mt * tau)))
        zr = z - mt * tau - n1
        u = zr if mp.im(zr) >= 0 else -zr
        eu = mp.exp(2 * I * pi * u)
        sm = mp.mpc(0)
        ep_base = mp.exp(2 * I * pi * (tau + zr))
        em_base = mp.exp(2 * I * pi * (tau - zr))
        ep_p = mp.mpc(1)
        em_p = mp.mpc(1)
        for idx, d in enumerate(dn):
            n = idx + 1
            ep_p = ep_p * ep_base
            em_p = em_p * em_base
            sm += (n / d) * (ep_p + em_p)
        return -pi * pi * e2 / 3 - 4 * pi * pi * eu / ((1 - eu) ** 2) - 4 * pi * pi * sm

    def build_seg(pts, spu: int, min_n: int):
        segs = []
        for za, zb in zip(pts[:-1], pts[1:]):
            dz = zb - za
            nsteps = max(min_n, int(mp.ceil(abs(dz) * spu)))
            h = dz / nsteps
            w0 = [wp(za + k * h) / 4 for k in range(nsteps + 1)]
            wm = [wp(za + (k + mp_rat(1, 2)) * h) / 4 for k in range(nsteps)]
            segs.append((h, nsteps, w0, wm))
        return segs

    def prop(segs, c_val, want_dc: bool = False):
        t00 = mp.mpc(1)
        t01 = mp.mpc(0)
        t10 = mp.mpc(0)
        t11 = mp.mpc(1)
        d00 = mp.mpc(0)
        d01 = mp.mpc(0)
        d10 = mp.mpc(0)
        d11 = mp.mpc(0)
        for h, nsteps, w0, wm in segs:
            h2 = h / 2
            h6 = h / 6
            for k in range(nsteps):
                qa = w0[k] + c_val
                qm = wm[k] + c_val
                qb = w0[k + 1] + c_val
                k1_00, k1_01 = t10, t11
                k1_10, k1_11 = -qa * t00, -qa * t01
                m00, m01, m10, m11 = t00 + h2 * k1_00, t01 + h2 * k1_01, t10 + h2 * k1_10, t11 + h2 * k1_11
                k2_00, k2_01 = m10, m11
                k2_10, k2_11 = -qm * m00, -qm * m01
                n00, n01, n10, n11 = t00 + h2 * k2_00, t01 + h2 * k2_01, t10 + h2 * k2_10, t11 + h2 * k2_11
                k3_00, k3_01 = n10, n11
                k3_10, k3_11 = -qm * n00, -qm * n01
                p00, p01, p10, p11 = t00 + h * k3_00, t01 + h * k3_01, t10 + h * k3_10, t11 + h * k3_11
                k4_00, k4_01 = p10, p11
                k4_10, k4_11 = -qb * p00, -qb * p01
                if want_dc:
                    l1_00, l1_01 = d10, d11
                    l1_10, l1_11 = -qa * d00 - t00, -qa * d01 - t01
                    dm00, dm01, dm10, dm11 = d00 + h2 * l1_00, d01 + h2 * l1_01, d10 + h2 * l1_10, d11 + h2 * l1_11
                    l2_00, l2_01 = dm10, dm11
                    l2_10, l2_11 = -qm * dm00 - m00, -qm * dm01 - m01
                    dn00, dn01, dn10, dn11 = d00 + h2 * l2_00, d01 + h2 * l2_01, d10 + h2 * l2_10, d11 + h2 * l2_11
                    l3_00, l3_01 = dn10, dn11
                    l3_10, l3_11 = -qm * dn00 - n00, -qm * dn01 - n01
                    dp00, dp01, dp10, dp11 = d00 + h * l3_00, d01 + h * l3_01, d10 + h * l3_10, d11 + h * l3_11
                    l4_00, l4_01 = dp10, dp11
                    l4_10, l4_11 = -qb * dp00 - p00, -qb * dp01 - p01
                    d00 += h6 * (l1_00 + 2 * l2_00 + 2 * l3_00 + l4_00)
                    d01 += h6 * (l1_01 + 2 * l2_01 + 2 * l3_01 + l4_01)
                    d10 += h6 * (l1_10 + 2 * l2_10 + 2 * l3_10 + l4_10)
                    d11 += h6 * (l1_11 + 2 * l2_11 + 2 * l3_11 + l4_11)
                t00 += h6 * (k1_00 + 2 * k2_00 + 2 * k3_00 + k4_00)
                t01 += h6 * (k1_01 + 2 * k2_01 + 2 * k3_01 + k4_01)
                t10 += h6 * (k1_10 + 2 * k2_10 + 2 * k3_10 + k4_10)
                t11 += h6 * (k1_11 + 2 * k2_11 + 2 * k3_11 + k4_11)
        T = mp.matrix([[t00, t01], [t10, t11]])
        return (T, mp.matrix([[d00, d01], [d10, d11]])) if want_dc else T

    z0 = (1 + tau) / 2
    spu_b = 10 if ty >= 6 else 14
    ga1 = build_seg([z0, z0 + 1], 14, 14)
    gb1 = build_seg([z0, z0 + tau], spu_b, 14)
    c_val = mp.mpc(pi * pi / 12, 0)

    tol_c = mp_pow10(-11)
    for _ in range(18):
        Ta, dTa = prop(ga1, c_val, True)
        Tb, dTb = prop(gb1, c_val, True)
        Tab = Ta * Tb
        dTab = dTa * Tb + Ta * dTb
        res = [mp.im(Ta[0, 0] + Ta[1, 1]), mp.im(Tb[0, 0] + Tb[1, 1]), mp.im(Tab[0, 0] + Tab[1, 1])]
        if max(abs(v) for v in res) < tol_c:
            break
        df = [dTa[0, 0] + dTa[1, 1], dTb[0, 0] + dTb[1, 1], dTab[0, 0] + dTab[1, 1]]
        J = mp.matrix([[mp.im(d), mp.re(d)] for d in df])
        rv = mp.matrix([-v for v in res])
        step = mp.lu_solve(J.T * J, J.T * rv)
        c_val += mp.mpc(step[0], step[1])

    ga2 = build_seg([z0, z0 + 1], 28, 28)
    gb2 = build_seg([z0, z0 + tau], 2 * spu_b, 28)
    tol_f = mp_pow10(-16)
    for _ in range(4):
        Ta1, dTa1 = prop(ga1, c_val, True)
        Ta2, dTa2 = prop(ga2, c_val, True)
        Ta = (16 * Ta2 - Ta1) / 15
        dTa = (16 * dTa2 - dTa1) / 15
        Tb1, dTb1 = prop(gb1, c_val, True)
        Tb2, dTb2 = prop(gb2, c_val, True)
        Tb = (16 * Tb2 - Tb1) / 15
        dTb = (16 * dTb2 - dTb1) / 15
        Tab = Ta * Tb
        dTab = dTa * Tb + Ta * dTb
        res = [mp.im(Ta[0, 0] + Ta[1, 1]), mp.im(Tb[0, 0] + Tb[1, 1]), mp.im(Tab[0, 0] + Tab[1, 1])]
        if max(abs(v) for v in res) < tol_f:
            break
        df = [dTa[0, 0] + dTa[1, 1], dTb[0, 0] + dTb[1, 1], dTab[0, 0] + dTab[1, 1]]
        J = mp.matrix([[mp.im(d), mp.re(d)] for d in df])
        rv = mp.matrix([-v for v in res])
        step = mp.lu_solve(J.T * J, J.T * rv)
        c_val += mp.mpc(step[0], step[1])

    Ta = (16 * prop(ga2, c_val) - prop(ga1, c_val)) / 15
    Tb = (16 * prop(gb2, c_val) - prop(gb1, c_val)) / 15

    def to_mob(T):
        M = mp.matrix([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]])
        return M / mp.sqrt(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])

    Tp = Tb * Ta * (Tb ** -1) * (Ta ** -1)
    Aa, P0 = to_mob(Ta), to_mob(Tp)
    pf = (P0[0, 0] - P0[1, 1]) / (2 * P0[1, 0])
    da = mp.sqrt((Aa[0, 0] - Aa[1, 1]) ** 2 + 4 * Aa[0, 1] * Aa[1, 0])
    fa1 = (Aa[0, 0] - Aa[1, 1] + da) / (2 * Aa[1, 0])
    fa2 = (Aa[0, 0] - Aa[1, 1] - da) / (2 * Aa[1, 0])
    g0 = mp.matrix([[1, -fa1], [1, -pf]])
    ssc = (g0[0, 0] * fa2 + g0[0, 1]) / (g0[1, 0] * fa2 + g0[1, 1])
    g = mp.matrix([[1 / ssc, -fa1 / ssc], [1, -pf]])
    g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
    if mp.im(g[0, 1] / g[1, 1]) < 0:
        g = mp.matrix([[I, 0], [0, -I]]) * g
    RP = g * P0 * (g ** -1)
    RP = RP / RP[0, 0]
    lam = abs(mp.re(RP[0, 1]))

    zs = (z0 / abs(z0)) / 20
    in_pts = [z0, z0 / 2, z0 / 4, z0 / 8, zs]
    gin1 = build_seg(in_pts, 14, 18)
    gin2 = build_seg(in_pts, 28, 36)
    Tin = (16 * prop(gin2, c_val) - prop(gin1, c_val)) / 15

    Mf = 56
    laur = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, Mf // 2 + 2):
        laur[n] = (mp.mpf(3) / ((2 * n + 3) * (n - 2))) * sum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
    Qc = [mp.mpc(0)] * (Mf + 1)
    Qc[0] = c_val
    for n in range(1, Mf // 2 + 1):
        Qc[2 * n] = laur[n] / 4
    al = [mp.mpc(0)] * (Mf + 1)
    be = [mp.mpc(0)] * (Mf + 1)
    al[0] = mp.mpc(1)
    for m in range(1, Mf + 1):
        al[m] = -sum(Qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
        be[m] = -(2 * m * al[m] + sum(Qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)
    zp = [zs ** k for k in range(Mf + 1)]
    gloc = sum(be[k] * zp[k] for k in range(Mf + 1)) / sum(al[k] * zp[k] for k in range(Mf + 1))
    wzs = Tin[0, 1] / Tin[0, 0]
    uzs = (g[0, 0] * wzs + g[0, 1]) / (g[1, 0] * wzs + g[1, 1])
    imB = mp.im(uzs) + (lam / (2 * pi)) * (mp.log(abs(zs)) + mp.re(gloc))
    return pi - (2 * pi / lam) * imB


class FrameCTauContext:
    """Per-(x, y) cached pure-mpmath Frame C evaluator (exact B1940 F_u/a0)."""

    def __init__(self, tx_f: Fraction, ty_f: Fraction, dps: int = 25):
        self.tx_f = tx_f
        self.ty_f = ty_f
        self.dps = dps
        mp.mp.dps = dps
        I = iu()
        pi = mp.pi
        self.tx_m = mp_frac(tx_f)
        self.ty_m = mp_frac(ty_f)
        self.tau = mp.mpc(self.tx_m, self.ty_m)
        self.L = solve_L2_fast_mp(self.tau, dps=dps)

        q = mp.exp(2 * I * pi * self.tau)
        self.K_q = (dps * 231 * ty_f.denominator) // (628 * ty_f.numerator) + 12
        eta_p = mp.mpc(1)
        qp = mp.mpc(1)
        for _ in range(1, self.K_q + 2):
            qp = qp * q
            eta_p = eta_p * (1 - qp)
        self.t1p = 2 * pi * ((mp.exp(I * pi * self.tau / 12) * eta_p) ** 3)
        self.qh = mp.exp(I * pi * self.tau)
        rad_int = (dps * 231 * ty_f.denominator) // (314 * ty_f.numerator) + 4
        self.nmax_th = math.isqrt(rad_int) + 10

        self.edual = {
            "1": mp.matrix([[mp_rat(1, 2), 0], [0, mp_rat(1, 2)]]),
            "i": mp.matrix([[-I / 2, 0], [0, I / 2]]),
            "j": mp.matrix([[0, mp_rat(1, 2)], [mp_rat(-1, 2), 0]]),
            "k": mp.matrix([[0, -I / 2], [-I / 2, 0]]),
        }
        self._thc_base_cache: Dict[Tuple[Fraction, Fraction], Any] = {}
        self._weight_cache: Dict[Tuple[Fraction, Fraction], Any] = {}

    def thc_direct(self, ca: Fraction, cb: Fraction):
        mp.mp.dps = self.dps
        I = iu()
        pi = mp.pi
        ca_m = mp_frac(ca)
        cb_m = mp_frac(cb)
        k0 = -int(round(ca))
        s = mp.mpc(0)
        for dk in range(-self.nmax_th, self.nmax_th + 1):
            n = k0 + dk
            na = n + ca_m
            s += (self.qh ** (na * na)) * mp.exp(2 * I * pi * na * cb_m)
        return s

    def thc(self, ca: Fraction, cb: Fraction):
        a_r = ca - math.floor(ca)
        n_b = math.floor(cb)
        b_r = cb - n_b
        key = (a_r, b_r)
        if key not in self._thc_base_cache:
            self._thc_base_cache[key] = self.thc_direct(a_r, b_r)
        base = self._thc_base_cache[key]
        if n_b == 0:
            return base
        mp.mp.dps = self.dps
        return mp.exp(2 * iu() * mp.pi * mp_frac(a_r) * n_b) * base

    def _weight_sqrt(self, al: Fraction, be: Fraction):
        al_r = al - math.floor(al)
        be_r = be - math.floor(be)
        key = (al_r, be_r)
        if key not in self._weight_cache:
            mp.mp.dps = self.dps
            I = iu()
            pi = mp.pi
            al_m = mp_frac(al_r)
            be_m = mp_frac(be_r)
            # Exact B1940 a_0(al, be) = 2*pi*i*al_r + theta_1'(z)/theta_1(z)
            z_r = al_m * self.tau + be_m
            th1_v = mp.mpc(0)
            th1_d = mp.mpc(0)
            for n in range(0, self.nmax_th + 2):
                sgn = 1 if n % 2 == 0 else -1
                w = sgn * (self.qh ** (n * (n + 1)))
                ang = (2 * n + 1) * pi * z_r
                th1_v += w * mp.sin(ang)
                th1_d += w * (2 * n + 1) * pi * mp.cos(ang)
            a0 = 2 * I * pi * al_m + th1_d / th1_v

            # Exact B1940 F_u(al, be)
            if al_r != 0:
                first = -pi * (2 * mp.log(2) + mp.log(self.ty_m) + mp.digamma(al_m) + mp.digamma(1 - al_m))
                zrow = mp.mpf(0)
            else:
                first = pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(self.ty_m))
                zrow = self.ty_m * (pi ** 2) / (mp.sin(pi * be_m) ** 2)
            tot = mp.mpf(0)
            for k in range(-self.K_q, self.K_q + 1):
                m = al_m + k
                if m == 0:
                    continue
                w = mp.exp(-2 * pi * abs(m) * self.ty_m + 2 * I * pi * (m * self.tx_m + be_m))
                tot += (2 * pi / abs(m)) * mp.re(w / (1 - w))
            Fu = first + zrow + tot

            c = Fu + pi * mp.log(self.ty_m) - 2 * pi * (mp.euler + mp.log(pi)) - pi * (abs(a0) ** 2) * mp.exp(-2 * self.L)
            arg = 2 * pi * self.L + c
            self._weight_cache[key] = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
        return self._weight_cache[key]

    def channels(self, a_f: Fraction, b_f: Fraction, qL: int, qR: int):
        mp.mp.dps = self.dps
        I = iu()
        pi = mp.pi
        H = Fraction(1, 2)
        xf = (qL * a_f, 2 * qL * b_f)
        yf = (qR * a_f, 2 * qR * b_f)
        ap, am = xf[0] + yf[0], xf[0] - yf[0]
        bp, bm = (xf[1] + yf[1]) / 2, (xf[1] - yf[1]) / 2
        e = mp.exp(-2 * I * pi * mp_frac(xf[0]))
        kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
        cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
        ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}

        Mw_full = mp.zeros(2, 2)
        Mw_res = mp.zeros(2, 2)
        for s in ("1", "i", "j", "k"):
            zc = (cs[s][0] - H).denominator == 1 and (cs[s][1] - H).denominator == 1
            zd = (ds[s][0] - H).denominator == 1 and (ds[s][1] - H).denominator == 1
            if zc or zd:
                continue
            R = kap[s] * self.thc(cs[s][0], cs[s][1]) * self.thc(ds[s][0], ds[s][1]) / self.t1p
            w_s = self._weight_sqrt(cs[s][0] - H, cs[s][1] - H)
            Mw_res += R * self.edual[s]
            Mw_full += (w_s * R) * self.edual[s]
        return Mw_full, Mw_res


def pairing_and_kappas(Mwu, Mwd):
    l1u, s1u, s2u = svd2_top_and_sv(Mwu)
    l1d, s1d, s2d = svd2_top_and_sv(Mwd)
    sL = spinor_pairing_sL(l1u, l1d)
    ku = s2u / s1u
    kd = s2d / s1d
    return sL, ku, kd


# ---------------------------------------------------------------------------
# Gate G4 (M4-A): B1973 30-point x 2-height benchmark (60 pairs, dps=35)
# ---------------------------------------------------------------------------

def run_G4_M4A() -> Tuple[Dict[str, Any], FrameCTauContext]:
    pts30 = (
        [(Fraction(i, 5), Fraction(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
        + [
            (Fraction(1, 7), Fraction(3, 7)), (Fraction(2, 7), Fraction(1, 7)),
            (Fraction(1, 3), Fraction(1, 3)), (Fraction(1, 4), Fraction(3, 4)),
            (Fraction(1, 6), Fraction(1, 6)), (Fraction(3, 8), Fraction(1, 8)),
        ]
    )
    max_sL_res = mp.mpf(0)
    max_rk_res = mp.mpf(0)
    max_sL_w = mp.mpf(0)
    max_ku = mp.mpf(0)
    max_kd = mp.mpf(0)
    max_th_shift_err = mp.mpf(0)
    worst_pt = ""
    ctx_y2 = None

    for y_int in (2, 6):
        ctx = FrameCTauContext(Fraction(13, 100), Fraction(y_int, 1), dps=35)
        if y_int == 2:
            ctx_y2 = ctx
            for ca, cb in ((Fraction(7, 5), Fraction(9, 5)), (Fraction(-11, 5), Fraction(13, 10)), (Fraction(3, 7), Fraction(-8, 7))):
                max_th_shift_err = max(max_th_shift_err, abs(ctx.thc_direct(ca, cb) - ctx.thc(ca, cb)))
        for a_f, b_f in pts30:
            Mwu, Mru = ctx.channels(a_f, b_f, 1, -4)
            Mwd, Mrd = ctx.channels(a_f, b_f, 1, 2)
            sL_r, ku_r, kd_r = pairing_and_kappas(Mru, Mrd)
            sL_w, ku_w, kd_w = pairing_and_kappas(Mwu, Mwd)
            max_sL_res = max(max_sL_res, sL_r)
            max_rk_res = max(max_rk_res, ku_r, kd_r)
            max_ku = max(max_ku, ku_w)
            max_kd = max(max_kd, kd_w)
            if sL_w > max_sL_w:
                max_sL_w = sL_w
                worst_pt = f"x=13/100,y={y_int},a={a_f},b={b_f}"

    mp.mp.dps = 35
    v33_ceil = V33_ceiling_mp(max_sL_w, mp_rat(1, 100))
    rho_floor = F_three_regime_mp(mp.mpf(0), max_sL_w, mp_rat(9, 10))
    passed = (
        max_th_shift_err < mp_pow10(-32)
        and max_sL_res < mp_pow10(-25)
        and max_rk_res < mp_pow10(-25)
        and max_sL_w < mp_rat(39, 100)
        and v33_ceil < mp_rat(78, 100)
        and rho_floor > mp_rat(24, 1000)
    )
    return {
        "pairs_checked": len(pts30) * 2,
        "theta_mod1_shift_max_err": mp_str(max_th_shift_err, 8),
        "unweighted_max_sL_res": mp_str(max_sL_res, 8),
        "unweighted_max_sv2_over_sv1": mp_str(max_rk_res, 8),
        "weighted_max_sL": mp_str(max_sL_w, 12),
        "weighted_max_kappa_u": mp_str(max_ku, 10),
        "weighted_max_kappa_d": mp_str(max_kd, 10),
        "worst_point": worst_pt,
        "analytic_V33_ceiling_at_rho_1_100": mp_str(v33_ceil, 12),
        "analytic_rho_floor_at_V33_9_10_all_r": mp_str(rho_floor, 12),
        "passed": passed,
    }, ctx_y2


# ---------------------------------------------------------------------------
# Gate G5 (M4-B): B1968 Full 2,016-Point Grid (dps = 25)
# ---------------------------------------------------------------------------

def run_G5_M4B() -> Dict[str, Any]:
    pts5 = [(Fraction(i, 5), Fraction(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
    pts7 = [(Fraction(i, 7), Fraction(j, 7)) for i in range(7) for j in range(7) if (i, j) != (0, 0)]
    all72 = pts5 + pts7
    cols = [Fraction(0, 1), Fraction(13, 100), Fraction(1, 4), Fraction(1, 2)]
    heights = [
        Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(3, 1),
        Fraction(4, 1), Fraction(6, 1), Fraction(10, 1),
    ]
    global_max_sL = mp.mpf(0)
    global_worst = ""
    per_height: List[Dict[str, str]] = []
    total_pts = 0
    failed_pts = 0

    for yf in heights:
        y_max_sL = mp.mpf(0)
        y_max_ku = mp.mpf(0)
        y_max_kd = mp.mpf(0)
        for xf in cols:
            ctx = FrameCTauContext(xf, yf, dps=25)
            for a_f, b_f in all72:
                total_pts += 1
                Mwu, _ = ctx.channels(a_f, b_f, 1, -4)
                Mwd, _ = ctx.channels(a_f, b_f, 1, 2)
                sL, ku, kd = pairing_and_kappas(Mwu, Mwd)
                y_max_sL = max(y_max_sL, sL)
                y_max_ku = max(y_max_ku, ku)
                y_max_kd = max(y_max_kd, kd)
                if sL >= mp_rat(39, 100):
                    failed_pts += 1
                if sL > global_max_sL:
                    global_max_sL = sL
                    global_worst = f"x={xf},y={yf},a={a_f},b={b_f}"
        mp.mp.dps = 25
        per_height.append({
            "y": str(yf),
            "points": str(len(cols) * len(all72)),
            "max_sL": mp_str(y_max_sL, 10),
            "max_kappa_u": mp_str(y_max_ku, 8),
            "max_kappa_d": mp_str(y_max_kd, 8),
            "V33_ceiling_at_rho_1_100": mp_str(V33_ceiling_mp(y_max_sL, mp_rat(1, 100)), 10),
            "rho_floor_at_V33_9_10_all_r": mp_str(F_three_regime_mp(mp.mpf(0), y_max_sL, mp_rat(9, 10)), 10),
        })

    mp.mp.dps = 35
    v33_ceil = V33_ceiling_mp(global_max_sL, mp_rat(1, 100))
    rho_floor = F_three_regime_mp(mp.mpf(0), global_max_sL, mp_rat(9, 10))
    r_curve: List[Dict[str, str]] = []
    for rf in (Fraction(0, 1), Fraction(1, 10), Fraction(1, 5), Fraction(3, 10), Fraction(1, 2), Fraction(7, 10), Fraction(4, 5), Fraction(1, 1)):
        tv = t_from_r_mp(mp_frac(rf))
        r_curve.append({
            "r": str(rf),
            "t": mp_str(tv, 10),
            "F_floor_at_V33_9_10": mp_str(F_three_regime_mp(tv, global_max_sL, mp_rat(9, 10)), 10),
            "universal_reality_floor": mp_str((tv * tv) / (1 + 2 * tv), 10),
        })

    passed = (
        total_pts == 2016
        and failed_pts == 0
        and global_max_sL < mp_rat(39, 100)
        and v33_ceil < mp_rat(78, 100)
        and rho_floor > mp_rat(24, 1000)
    )
    return {
        "total_points_certified_all_r": total_pts,
        "failed_points": failed_pts,
        "global_max_sL": mp_str(global_max_sL, 12),
        "global_worst_point": global_worst,
        "analytic_V33_ceiling_at_rho_1_100": mp_str(v33_ceil, 12),
        "analytic_rho_floor_at_V33_9_10_all_r": mp_str(rho_floor, 12),
        "per_height_summary": per_height,
        "global_r_curve": r_curve,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Gate G6 (Guardrail 3) & Gate G7 (PF1-PF6 Planted Faults)
# ---------------------------------------------------------------------------

def run_G6_and_G7(ctx_y2: FrameCTauContext) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    mp.mp.dps = 35
    Mwu, _ = ctx_y2.channels(Fraction(1, 5), Fraction(2, 5), 1, -4)
    Mwd, _ = ctx_y2.channels(Fraction(1, 5), Fraction(2, 5), 1, 2)
    uu, wu = mw_to_uw_mp(Mwu)
    ud, wd = mw_to_uw_mp(Mwd)

    tv = t_from_r_mp(mp_rat(1, 5))
    h = canon_h_mp(tv)
    hb = [mp.conj(z) for z in h]
    Yu = Y_b1736_mp(hb, uu, wu)
    Yd = Y_b1736_mp(h, ud, wd)
    Uu0, Su0, _ = svd_desc(Yu)
    Ud0, Sd0, _ = svd_desc(Yd)
    V0 = Uu0.H * Ud0
    absV0 = [[abs(V0[r, c]) for c in range(3)] for r in range(3)]

    rng = random.Random(202603)
    max_sv_drift = mp.mpf(0)
    max_V_drift = mp.mpf(0)
    for _ in range(10):
        UQ = gram_schmidt_haar_u(rng, 3)
        Uu_r = gram_schmidt_haar_u(rng, 3)
        Ud_r = gram_schmidt_haar_u(rng, 3)
        Yu_s = UQ * Yu * Uu_r.H
        Yd_s = UQ * Yd * Ud_r.H
        Uus, Sus, _ = svd_desc(Yu_s)
        Uds, Sds, _ = svd_desc(Yd_s)
        Vs = Uus.H * Uds
        for k in range(3):
            max_sv_drift = max(max_sv_drift, abs(Sus[k] - Su0[k]), abs(Sds[k] - Sd0[k]))
        for r in range(3):
            for c in range(3):
                max_V_drift = max(max_V_drift, abs(abs(Vs[r, c]) - absV0[r][c]))

    g6 = {
        "haar_trials": 10,
        "max_sv_drift": mp_str(max_sv_drift, 8),
        "max_V_abs_drift": mp_str(max_V_drift, 8),
        "passed": (max_sv_drift < mp_pow10(-30) and max_V_drift < mp_pow10(-30)),
    }

    M_bad = M_from_uw_mp(ud, wd, sign_w=+1)
    pf1_err = mat_frob_norm(Y_b1736_mp(h, ud, wd) - Y_kron_mp(H_from_h_mp(h), M_bad))
    pf1_caught = (pf1_err > mp_rat(1, 10))

    t_pf2 = mp_rat(1, 5)
    k_pf2 = t_pf2 / (1 + 2 * t_pf2)
    s2 = mp.sqrt(2)
    ep = [mp.mpf(1) / s2, iu() / s2, mp.mpc(0)]
    em = [mp.mpf(1) / s2, -iu() / s2, mp.mpc(0)]
    Yw_pf2 = Y_b1736_mp(canon_h_mp(t_pf2), [em[j] - k_pf2 * ep[j] for j in range(3)], mp.mpc(0))
    _, sv_pf2, _ = svd_desc(Yw_pf2)
    rho_pf2 = sv_pf2[1] / sv_pf2[0]
    pf2_caught = (rho_pf2 < t_pf2 / 2 - mp_rat(1, 20))

    _, Mru_bad = ctx_y2.channels(Fraction(1, 5), Fraction(2, 5), 2, -4)
    _, Mrd_ok = ctx_y2.channels(Fraction(1, 5), Fraction(2, 5), 1, 2)
    sL_pf3, _, _ = pairing_and_kappas(Mru_bad, Mrd_ok)
    pf3_caught = (sL_pf3 > mp_rat(1, 10))

    h_r1 = canon_h_mp(mp.mpf(1))
    M_rk1 = mp.matrix([[mp.mpc(0), mp.sqrt(2)], [mp.mpc(0), mp.mpc(0)]])
    Uu_pf4, _, _ = svd_desc(Y_kron_mp(H_from_h_mp([mp.conj(z) for z in h_r1]), M_rk1))
    Ud_pf4, _, _ = svd_desc(Y_kron_mp(H_from_h_mp(h_r1), M_rk1))
    v33_pf4 = abs(vec_inner([Uu_pf4[r, 0] for r in range(3)], [Ud_pf4[r, 0] for r in range(3)]))
    pf4_caught = (v33_pf4 > mp_rat(1, 3) + mp_rat(1, 2))

    UQu = gram_schmidt_haar_u(rng, 3)
    UQd = gram_schmidt_haar_u(rng, 3)
    Uu5, _, _ = svd_desc(UQu * Yu)
    Ud5, _, _ = svd_desc(UQd * Yd)
    V5 = Uu5.H * Ud5
    pf5_drift = max(abs(abs(V5[r, c]) - absV0[r][c]) for r in range(3) for c in range(3))
    pf5_caught = (pf5_drift > mp_rat(1, 10))

    h_r0 = canon_h_mp(mp.mpf(0))
    Uu6, _, _ = svd_desc(Y_kron_mp(H_from_h_mp(h_r0), M_rk1))
    Ud6, _, _ = svd_desc(Y_kron_mp(H_from_h_mp(h_r0), M_rk1))
    v33_pf6 = abs(vec_inner([Uu6[r, 0] for r in range(3)], [Ud6[r, 0] for r in range(3)]))
    pf6_caught = (v33_pf6 > mp_rat(1, 3) + mp_rat(1, 2))

    g7 = {
        "PF1_M_sign_flip_err": mp_str(pf1_err, 8),
        "PF1_caught": pf1_caught,
        "PF2_wrong_rank1_floor_rho": mp_str(rho_pf2, 8),
        "PF2_caught": pf2_caught,
        "PF3_broken_qL_residue_sL": mp_str(sL_pf3, 8),
        "PF3_caught": pf3_caught,
        "PF4_r0_ceiling_at_r1_V33": mp_str(v33_pf4, 8),
        "PF4_caught": pf4_caught,
        "PF5_unshared_UQ_drift": mp_str(pf5_drift, 8),
        "PF5_caught": pf5_caught,
        "PF6_no_conjugate_r0_V33": mp_str(v33_pf6, 8),
        "PF6_caught": pf6_caught,
        "caught_count": sum(int(x) for x in (pf1_caught, pf2_caught, pf3_caught, pf4_caught, pf5_caught, pf6_caught)),
        "total_faults": 6,
        "passed": all((pf1_caught, pf2_caught, pf3_caught, pf4_caught, pf5_caught, pf6_caught)),
    }
    return g6, g7


def main() -> None:
    t0 = time.monotonic()
    self_path = pathlib.Path(__file__).resolve()
    g0 = check_ast_and_custody(self_path)
    g1 = run_G1_M1()
    g2 = run_G2_M2()
    g3 = run_G3_M3()
    g4, ctx_y2 = run_G4_M4A()
    g5 = run_G5_M4B()
    g6, g7 = run_G6_and_G7(ctx_y2)

    elapsed_int = int(time.monotonic() - t0)
    all_ok = all(g["passed"] for g in (g0, g1, g2, g3, g4, g5, g6, g7))

    out: Dict[str, Any] = {
        "card": "A2-P879-INTERIOR",
        "producer_version": "v3",
        "empirical_firewall": "0 of 19",
        "runtime_seconds_int": elapsed_int,
        "G0_ast_and_custody": g0,
        "G1_M1_kronecker_unitary_bell": g1,
        "G2_M2_sharp_two_variable_and_reality_floor": g2,
        "G3_M3_perturbation_interior_tradeoff_and_controls": g3,
        "G4_M4A_frame_c_b1973_30pt_benchmark": g4,
        "G5_M4B_frame_c_b1968_2016pt_all_r_certification": g5,
        "G6_guardrail3_haar_u3_scrambling": g6,
        "G7_planted_faults_PF1_to_PF6": g7,
        "json_float_tokens": 0,
        "all_gates_passed": all_ok,
    }
    jf = count_json_floats(out)
    out["json_float_tokens"] = jf
    if jf != 0:
        out["all_gates_passed"] = False

    out_path = self_path.parent / "a2_p879_interior_v3_results.json"
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"A2-P879-INTERIOR Producer v3 finished in {elapsed_int}s | all_gates_passed={out['all_gates_passed']} | json_floats={jf}")
    if not out["all_gates_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
