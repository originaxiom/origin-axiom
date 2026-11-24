#!/usr/bin/env python3
"""
Disjoint Cold-Room Zero-Trust Referee (Guardrail 6) for Card A2-P879-INTERIOR.

Strictly 0 of 19 (zero empirical PDG/NuFIT/Planck/DESI/CODATA constants).
Zero Python float or complex AST literals, zero float()/complex() casts,
zero frontier/ imports, zero JSON float tokens.

Disjoint methods:
- Symbolic algebra: independent SymPy proofs of M1, M2, M3 (including exact
  Kronecker unitary similarity, Bell-state constant projection, canonical
  witness attainment, crossing M_*(rho), and 3-regime floor continuity/monotonicity).
- M2 Bell-split subspace verification: explicitly constructs orthonormal 2D
  subspaces W = span{w_1, z_2} and W' = span{u_1', z_2'} in sl_2(C) and verifies
  every intermediate proof inequality on 2,200 single-sector trials (2,000 random
  + 200 adversarial boundary/corner trials) plus exact 50-digit check of the
  canonical witness across 11 rational reality values.
- M3 two-sector adversarial test: 2,200 trials across r in [0, 1) (both hierarchical
  rho < 1/6 and generic channels) plus positive controls C1-A (r = 1/2000, s_L = 1),
  B1967 (16-rational witness at r = 3/1000), and r = 1.
- M4 Frame C certification: genuinely disjoint Chebyshev-Lobatto spectral collocation
  Fuchsian ODE solver with exact Cauchy-Riemann holomorphic Jacobian and Frobenius
  puncture connection for L_2(tau) (NO RK4, NO Gauss-Legendre), mp.jtheta(3, ...)
  for theta_c, mp.qp for eta, mp.jtheta(1, ..., 1) for a_0, and transposed k-outer
  Fourier summation for F_u cross-checked against m-outer summation.
  Evaluates both M4-A (B1973 30 pts x 2 heights = 60 pairs, dps=35/45) and
  M4-B (B1968 full 72 pts x 28 tau = 2,016 points, dps=30/38).
- Guardrail 3: 10 deterministic Haar U(3)_Q x U(3)_u x U(3)_d basis scramblings
  via SHA-256 PRNG + Mezzadri QR phase normalization (< 10^{-30}).
- Six independent Referee Planted Faults (RPF1-RPF6).
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


# ============================================================================
# Exact Arithmetic Helpers (Zero float/complex literals or casts)
# ============================================================================

def mp_pow10(exp_int: int) -> mp.mpf:
    if exp_int >= 0:
        return mp.mpf(10) ** exp_int
    return mp.mpf(1) / (mp.mpf(10) ** (-exp_int))


def mp_rat(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def mp_frac(f: Fraction) -> mp.mpf:
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def mp_str(x: mp.mpf, digits: int = 30) -> str:
    return mp.nstr(x, digits)


def mp_sci(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def frac_str(f: Fraction) -> str:
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"


def clamp_unit_real(x: mp.mpf) -> mp.mpf:
    one = mp.mpf(1)
    if x > one:
        return one
    if x < -one:
        return -one
    return x


def clamp_nonneg_unit(x: mp.mpf) -> mp.mpf:
    zero = mp.mpf(0)
    one = mp.mpf(1)
    if x < zero:
        return zero
    if x > one:
        return one
    return x


# ============================================================================
# Deterministic Zero-Float SHA-256 PRNG & Exact Haar U(n) Generator
# ============================================================================

class Sha256Prng:
    """Pure-integer deterministic PRNG backed by SHA-256 counter mode."""

    def __init__(self, seed_tag: str) -> None:
        self.seed = seed_tag.encode("utf-8")
        self.counter = 0

    def next_uint128(self) -> int:
        h = hashlib.sha256(self.seed + self.counter.to_bytes(8, "big")).digest()
        self.counter += 1
        return int.from_bytes(h[:16], "big")

    def uniform_open01(self) -> mp.mpf:
        # Strictly inside (0, 1): (u + 1) / (2^128 + 1)
        u = self.next_uint128()
        return mp.mpf(u + 1) / mp.mpf((1 << 128) + 1)

    def uniform_range(self, lo: mp.mpf, hi: mp.mpf) -> mp.mpf:
        return lo + (hi - lo) * self.uniform_open01()

    def standard_normal(self) -> mp.mpf:
        u1 = self.uniform_open01()
        u2 = self.uniform_open01()
        return mp.sqrt(-2 * mp.log(u1)) * mp.cos(2 * mp.pi * u2)

    def complex_normal(self) -> mp.mpc:
        u1 = self.uniform_open01()
        u2 = self.uniform_open01()
        rad = mp.sqrt(-mp.log(u1))
        ang = 2 * mp.pi * u2
        return mp.mpc(rad * mp.cos(ang), rad * mp.sin(ang))

    def haar_unitary(self, n: int) -> mp.matrix:
        # Ginibre matrix + modified Gram-Schmidt QR with Mezzadri diagonal phase fix
        G = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                G[i, j] = self.complex_normal()
        Q = mp.matrix(n, n)
        for j in range(n):
            v = [G[i, j] for i in range(n)]
            # Two passes of modified Gram-Schmidt for full working-precision orthogonality
            for _ in range(2):
                for k in range(j):
                    ip = sum(mp.conj(Q[i, k]) * v[i] for i in range(n))
                    for i in range(n):
                        v[i] -= ip * Q[i, k]
            nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
            # Mezzadri phase: diagonal of R is positive real (align phase of R[j,j] = <q_j, G[:,j]>)
            # Equivalently compute R_jj from original column:
            q_tmp = [x / nrm for x in v]
            r_jj = sum(mp.conj(q_tmp[i]) * G[i, j] for i in range(n))
            ph = r_jj / abs(r_jj) if abs(r_jj) > mp.mpf(0) else mp.mpf(1)
            for i in range(n):
                Q[i, j] = q_tmp[i] * ph
        return Q


# ============================================================================
# Gate RG0: AST / Custody / Firewall Self-Check & JSON Float Audit
# ============================================================================

def audit_script_ast(script_path: Path) -> dict:
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_literals = []
    complex_literals = []
    banned_calls = []
    banned_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals.append((getattr(node, "lineno", 0), repr(node.value)))
            elif isinstance(node.value, complex):
                complex_literals.append((getattr(node, "lineno", 0), repr(node.value)))
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
                banned_calls.append((getattr(node, "lineno", 0), node.func.id))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if "frontier" in alias.name or alias.name in ("numpy", "scipy", "random"):
                    banned_imports.append((getattr(node, "lineno", 0), alias.name))
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "frontier" in mod or mod.split(".")[0] in ("numpy", "scipy", "random"):
                banned_imports.append((getattr(node, "lineno", 0), mod))
    passed = (
        len(float_literals) == 0
        and len(complex_literals) == 0
        and len(banned_calls) == 0
        and len(banned_imports) == 0
    )
    return {
        "script_path": str(script_path),
        "float_literal_count": len(float_literals),
        "complex_literal_count": len(complex_literals),
        "banned_call_count": len(banned_calls),
        "banned_import_count": len(banned_imports),
        "passed": passed,
    }


def count_json_floats(obj) -> int:
    if isinstance(obj, bool) or isinstance(obj, int) or obj is None or isinstance(obj, str):
        return 0
    if isinstance(obj, float):
        return 1
    if isinstance(obj, list):
        return sum(count_json_floats(x) for x in obj)
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    return 1


# ============================================================================
# Core Linear Algebra & Pure-Triplet Yukawa Primitives (Pure mpmath)
# ============================================================================

def pauli_matrices() -> tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    I2 = mp.matrix([[1, 0], [0, 1]])
    s1 = mp.matrix([[0, 1], [1, 0]])
    s2 = mp.matrix([[0, -mp.j], [mp.j, 0]])
    s3 = mp.matrix([[1, 0], [0, -1]])
    return I2, s1, s2, s3


def build_H(h_vec: list) -> mp.matrix:
    _, s1, s2, s3 = pauli_matrices()
    return h_vec[0] * s1 + h_vec[1] * s2 + h_vec[2] * s3


def build_M(u_vec: list, w_val, sign_w: int = -1) -> mp.matrix:
    I2, s1, s2, s3 = pauli_matrices()
    return (sign_w * mp.j * w_val) * I2 + u_vec[0] * s1 + u_vec[1] * s2 + u_vec[2] * s3


def build_Y(h_vec: list, u_vec: list, w_val) -> mp.matrix:
    dot_uh = u_vec[0] * h_vec[0] + u_vec[1] * h_vec[1] + u_vec[2] * h_vec[2]
    hx = mp.matrix([
        [0, -h_vec[2], h_vec[1]],
        [h_vec[2], 0, -h_vec[0]],
        [-h_vec[1], h_vec[0], 0],
    ])
    Y = mp.matrix(3, 3)
    for a in range(3):
        for b in range(3):
            Y[a, b] = u_vec[a] * h_vec[b] + h_vec[a] * u_vec[b] - (dot_uh if a == b else mp.mpf(0)) + w_val * hx[a, b]
    return Y


def extract_uw_from_Mw(Mw: mp.matrix) -> tuple[list, mp.mpc]:
    m0 = (Mw[0, 0] + Mw[1, 1]) / 2
    m1 = (Mw[0, 0] - Mw[1, 1]) / (2 * mp.j)
    m2 = (Mw[0, 1] - Mw[1, 0]) / 2
    m3 = (Mw[0, 1] + Mw[1, 0]) / (2 * mp.j)
    u = [-2 * m0, 2 * m3, -2 * m1]
    w = -2 * m2
    return u, w


def build_Lu_Ru() -> tuple[mp.matrix, mp.matrix]:
    inv_sq2 = mp.mpf(1) / mp.sqrt(2)
    H2 = mp.matrix([[1, 1], [1, -1]]) * inv_sq2
    Lu = mp.matrix([[1, 0], [0, mp.j]]) * H2
    Ru = H2 * mp.matrix([[0, -1], [mp.j, 0]])
    return Lu, Ru


def reality_to_t(r: mp.mpf) -> mp.mpf:
    return r / (1 + mp.sqrt(max(mp.mpf(0), 1 - r * r)))


def t_to_reality(t: mp.mpf) -> mp.mpf:
    return (2 * t) / (1 + t * t)


def spinor_sL_from_cols(l_u: list, l_d: list) -> mp.mpf:
    """Exact cancellation-free s_L = |det[l_u, l_d]| = |l_u0 l_d1 - l_u1 l_d0|."""
    return abs(l_u[0] * l_d[1] - l_u[1] * l_d[0])


def vec_norm(v: list) -> mp.mpf:
    return mp.sqrt(sum(abs(x) ** 2 for x in v))


def vec_ip(a: list, b: list) -> mp.mpc:
    return sum(mp.conj(a[i]) * b[i] for i in range(len(a)))


def sin_angle_unit(u: list, v: list) -> mp.mpf:
    """Cancellation-free sin(theta(u, v)) = ||u - <v|u> v||_2 for unit vectors."""
    ip = vec_ip(v, u)
    perp = [u[i] - ip * v[i] for i in range(len(u))]
    return vec_norm(perp)


def kron2(A: mp.matrix, B: mp.matrix) -> mp.matrix:
    K = mp.matrix(4, 4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    K[2 * i + k, 2 * j + l] = A[i, j] * B[k, l]
    return K


def vec_kron2(a: list, b: list) -> list:
    return [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]


def mat_mul_vec(M: mp.matrix, v: list) -> list:
    rows, cols = M.rows, M.cols
    return [sum(M[i, j] * v[j] for j in range(cols)) for i in range(rows)]


def frob_norm(M: mp.matrix) -> mp.mpf:
    return mp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))


def svd2_exact(M: mp.matrix) -> tuple[mp.matrix, list, mp.matrix]:
    """Wrapper around mp.svd_c guaranteeing descending order S[0] >= S[1]."""
    U, S, Vh = mp.svd_c(M)
    return U, [S[0], S[1]], Vh


def S_t_bound(t: mp.mpf, rho: mp.mpf) -> mp.mpf:
    m_star = mp.sqrt(rho / (2 * (1 + 2 * rho)))
    if t <= m_star:
        return mp.sqrt(2 * rho * (1 + 2 * rho)) + 2 * rho
    return rho * (1 + 2 * t) / t


def S_req_val(sL: mp.mpf, a: mp.mpf) -> mp.mpf:
    mob = clamp_unit_real((1 + sL) / (3 - sL))
    diff = mp.acos(mob) - mp.acos(clamp_unit_real(a))
    if diff <= 0:
        return mp.mpf(0)
    return mp.sin(diff / 2)


def F_three_regime(t: mp.mpf, sL: mp.mpf, a: mp.mpf) -> mp.mpf:
    sreq = S_req_val(sL, a)
    if sreq == 0:
        return (t * t) / (1 + 2 * t)
    t1 = sreq / (2 * (1 + sreq))
    if t <= t1:
        return (sreq * sreq) / (2 * (1 + 2 * sreq))
    if t <= sreq:
        return (sreq * t) / (1 + 2 * t)
    return (t * t) / (1 + 2 * t)


def V33_ceiling(t: mp.mpf, sL: mp.mpf, rho: mp.mpf) -> mp.mpf:
    mob = clamp_unit_real((1 + sL) / (3 - sL))
    st = clamp_nonneg_unit(S_t_bound(t, rho))
    ang = mp.acos(mob) - 2 * mp.asin(st)
    if ang <= 0:
        return mp.mpf(1)
    return mp.cos(ang)


def build_h_with_t(prng: Sha256Prng, t: mp.mpf) -> list:
    """Build unit h in C^3 with exact singular ratio sigma_2(H)/sigma_1(H) = t via random SU(2) spinors."""
    # Canonical h_0 = (e_- + t e_+) / sqrt(1 + t^2) has H(h_0) = sqrt(2)/(sqrt(1+t^2)) * [[0, t], [1, 0]]
    # Rotate H by random U in SU(2): H' = U H_0 U^T ? Wait: H must stay traceless!
    # For any U in U(2), U H_0 U^dagger is traceless with IDENTICAL singular values!
    inv_sq2 = mp.mpf(1) / mp.sqrt(2)
    den = mp.sqrt(1 + t * t)
    h0 = [(1 + t) * inv_sq2 / den, mp.j * (t - 1) * inv_sq2 / den, mp.mpf(0)]
    H0 = build_H(h0)
    U = prng.haar_unitary(2)
    Hp = U * H0 * U.transpose_conj()
    # Add global random phase e^{i phi}
    phi = prng.uniform_range(mp.mpf(0), 2 * mp.pi)
    ph = mp.exp(mp.j * phi)
    Hp = ph * Hp
    _, s1, s2, s3 = pauli_matrices()
    h = [
        (Hp * s1)[0, 0] / 2 + (Hp * s1)[1, 1] / 2,
        (Hp * s2)[0, 0] / 2 + (Hp * s2)[1, 1] / 2,
        (Hp * s3)[0, 0] / 2 + (Hp * s3)[1, 1] / 2,
    ]
    nrm = vec_norm(h)
    return [x / nrm for x in h]


def build_M_with_kappa(prng: Sha256Prng, kappa: mp.mpf) -> tuple[mp.matrix, list, mp.mpc]:
    """Build 2x2 M with exact singular values (1, kappa) and random Haar U, V."""
    U = prng.haar_unitary(2)
    V = prng.haar_unitary(2)
    D = mp.matrix([[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), kappa]])
    M = U * D * V.transpose_conj()
    I2, s1, s2, s3 = pauli_matrices()
    w_val = mp.j * ((M[0, 0] + M[1, 1]) / 2)
    u_vec = [
        ((M * s1)[0, 0] + (M * s1)[1, 1]) / 2,
        ((M * s2)[0, 0] + (M * s2)[1, 1]) / 2,
        ((M * s3)[0, 0] + (M * s3)[1, 1]) / 2,
    ]
    return M, u_vec, w_val


def build_M_with_rho1_kappa(prng: Sha256Prng, rho1: list, kappa: mp.mpf) -> tuple[mp.matrix, list, mp.mpc]:
    """Build 2x2 M with prescribed dominant right singular vector rho1 and singular values (1, kappa)."""
    U = prng.haar_unitary(2)
    rho2 = [-mp.conj(rho1[1]), mp.conj(rho1[0])]
    # M = u1 rho1^dagger + kappa u2 rho2^dagger
    M = mp.matrix(2, 2)
    for i in range(2):
        for j in range(2):
            M[i, j] = U[i, 0] * mp.conj(rho1[j]) + kappa * U[i, 1] * mp.conj(rho2[j])
    _, s1, s2, s3 = pauli_matrices()
    w_val = mp.j * ((M[0, 0] + M[1, 1]) / 2)
    u_vec = [
        ((M * s1)[0, 0] + (M * s1)[1, 1]) / 2,
        ((M * s2)[0, 0] + (M * s2)[1, 1]) / 2,
        ((M * s3)[0, 0] + (M * s3)[1, 1]) / 2,
    ]
    return M, u_vec, w_val


# ============================================================================
# Gate RG1: M1 — Kronecker Compression, Unitary Frame Equivalence, Bell Lemma
# ============================================================================

def run_M1() -> dict:
    # --- Symbolic Proofs in SymPy ---
    h1, h2, h3, u1, u2, u3, w = sp.symbols("h1 h2 h3 u1 u2 u3 w")
    I = sp.I
    s0 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -I], [I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    basis = [s0, s1, s2, s3]

    H = h1 * s1 + h2 * s2 + h3 * s3
    M = -I * w * s0 + u1 * s1 + u2 * s2 + u3 * s3
    hvec = sp.Matrix([h1, h2, h3])
    uvec = sp.Matrix([u1, u2, u3])
    hx = sp.Matrix([[0, -h3, h2], [h3, 0, -h1], [-h2, h1, 0]])
    Y_direct = uvec * hvec.T + hvec * uvec.T - uvec.dot(hvec) * sp.eye(3) + w * hx
    Y_trace = sp.Matrix(3, 3, lambda a, b: sp.Rational(1, 2) * (basis[a + 1] * H * basis[b + 1] * M).trace())
    sym_m1_1_trace_zero = sp.simplify(Y_direct - Y_trace) == sp.zeros(3, 3)

    # Full 4x4 operator T_Pauli(a, b) = (1/2) Tr(e_a H e_b M) vs U_P^H (H kron M^T) U_P
    T_pauli = sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2) * (basis[a] * H * basis[b] * M).trace())
    # vec(X) = [X00, X01, X10, X11]^T / sqrt(2) -> columns of U_P are vec(e_a)
    U_P = sp.Matrix([
        [1, 0, 0, 1],
        [0, 1, -I, 0],
        [0, 1, I, 0],
        [1, 0, 0, -1],
    ]) / sp.sqrt(2)
    sym_UP_unitary = sp.simplify(U_P.H * U_P - sp.eye(4)) == sp.zeros(4, 4)
    # Kronecker product H kron M^T
    HKM = sp.kronecker_product(H, M.T)
    sym_kron_equiv = sp.simplify(U_P.H * HKM * U_P - T_pauli) == sp.zeros(4, 4)
    sym_block_Y = sp.simplify(T_pauli[1:, 1:] - Y_direct) == sp.zeros(3, 3)

    # H(h) singular-value identity: Tr(H^H H) = 2 ||h||^2, det(H) = -h.h
    hr1, hr2, hr3, hi1, hi2, hi3 = sp.symbols("hr1 hr2 hr3 hi1 hi2 hi3", real=True)
    hc = [hr1 + I * hi1, hr2 + I * hi2, hr3 + I * hi3]
    Hc = hc[0] * s1 + hc[1] * s2 + hc[2] * s3
    h_norm2 = hr1**2 + hi1**2 + hr2**2 + hi2**2 + hr3**2 + hi3**2
    h_dot_h = hc[0]**2 + hc[1]**2 + hc[2]**2
    sym_H_tr = sp.simplify((Hc.H * Hc).trace() - 2 * h_norm2) == 0
    sym_H_det = sp.simplify(Hc.det() + h_dot_h) == 0
    r_sym = sp.Symbol("r_sym", positive=True)
    t_expr = r_sym / (1 + sp.sqrt(1 - r_sym**2))
    sym_r_mobius = sp.simplify(2 * t_expr / (1 + t_expr**2) - r_sym) == 0
    s1_sq = 1 + sp.sqrt(1 - r_sym**2)
    s2_sq = 1 - sp.sqrt(1 - r_sym**2)
    sym_sv_ratio = sp.simplify(s2_sq / s1_sq - t_expr**2) == 0

    # M1.2: M(u, w) = 2 L_u M_w^T R_u
    a00, a01, a10, a11 = sp.symbols("a00 a01 a10 a11")
    Mw_s = sp.Matrix([[a00, a01], [a10, a11]])
    m0 = (a00 + a11) / 2
    m1 = (a00 - a11) / (2 * I)
    m2 = (a01 - a10) / 2
    m3 = (a01 + a10) / (2 * I)
    M_uw_s = -I * (-2 * m2) * s0 + (-2 * m0) * s1 + (2 * m3) * s2 + (-2 * m1) * s3
    H2 = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    Lu_s = sp.Matrix([[1, 0], [0, I]]) * H2
    Ru_s = H2 * sp.Matrix([[0, -1], [I, 0]])
    sym_Lu_u = sp.simplify(Lu_s.H * Lu_s - sp.eye(2)) == sp.zeros(2, 2)
    sym_Ru_u = sp.simplify(Ru_s.H * Ru_s - sp.eye(2)) == sp.zeros(2, 2)
    sym_m1_2 = sp.simplify(M_uw_s - 2 * Lu_s * Mw_s.T * Ru_s) == sp.zeros(2, 2)

    # M1.3: Bell-state constant projection lemma symbolically using arbitrary SU(2) x SU(2)
    th1, ph1, ps1, th2, ph2, ps2 = sp.symbols("th1 ph1 ps1 th2 ph2 ps2", real=True)
    # General orthonormal basis {al1, al2} of C^2 and unit vector be1 of C^2
    al1 = sp.Matrix([sp.cos(th1) * sp.exp(I * ph1), sp.sin(th1) * sp.exp(I * ps1)])
    al2 = sp.Matrix([-sp.sin(th1) * sp.exp(-I * ps1), sp.cos(th1) * sp.exp(-I * ph1)])
    be1 = sp.Matrix([sp.cos(th2) * sp.exp(I * ph2), sp.sin(th2) * sp.exp(I * ps2)])
    be2 = sp.Matrix([-sp.sin(th2) * sp.exp(-I * ps2), sp.cos(th2) * sp.exp(-I * ph2)])
    e0_s = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    u1_s = sp.kronecker_product(al1, be1)
    u2_a = sp.kronecker_product(al2, be1)
    u2_b = sp.kronecker_product(al1, be2)
    ip1 = (e0_s.H * u1_s)[0]
    ip2a = (e0_s.H * u2_a)[0]
    ip2b = (e0_s.H * u2_b)[0]
    proj_a = sp.simplify(ip1 * sp.conjugate(ip1) + ip2a * sp.conjugate(ip2a))
    proj_b = sp.simplify(ip1 * sp.conjugate(ip1) + ip2b * sp.conjugate(ip2b))
    sym_bell_a = sp.simplify(proj_a - sp.Rational(1, 2)) == 0
    sym_bell_b = sp.simplify(proj_b - sp.Rational(1, 2)) == 0
    sym_bell_single = sp.simplify(ip1 * sp.conjugate(ip1) - sp.Rational(1, 2) * ((al1.T * be1)[0] * sp.conjugate((al1.T * be1)[0]))) == 0

    # --- High-Precision Numerical Checks (dps = 50, 50 trials each) ---
    mp.mp.dps = 50
    prng = Sha256Prng("referee-M1-v1")
    Lu, Ru = build_Lu_Ru()
    e0_vec = [mp.mpf(1) / mp.sqrt(2), mp.mpf(0), mp.mpf(0), mp.mpf(1) / mp.sqrt(2)]
    QJ = mp.matrix([[0, 1], [-1, 0]])

    max_kron_sv_err = mp.mpf(0)
    max_trace_Y_err = mp.mpf(0)
    max_kappa_eq_err = mp.mpf(0)
    max_rho1_spinor_err = mp.mpf(0)
    max_sL_equiv_err = mp.mpf(0)
    max_QJ_gauge_err = mp.mpf(0)
    max_bell_proj_err = mp.mpf(0)
    max_bell_single_excess = mp.mpf(0)

    I2, ms1, ms2, ms3 = pauli_matrices()
    mbasis = [I2, ms1, ms2, ms3]

    for _ in range(50):
        # M1.1 numeric check
        h = [prng.complex_normal() for _ in range(3)]
        u = [prng.complex_normal() for _ in range(3)]
        wv = prng.complex_normal()
        Hm = build_H(h)
        Mm = build_M(u, wv)
        Ym = build_Y(h, u, wv)
        Tm = mp.matrix(4, 4)
        for a in range(4):
            for b in range(4):
                P = mbasis[a] * Hm * mbasis[b] * Mm
                Tm[a, b] = (P[0, 0] + P[1, 1]) / 2
        for a in range(3):
            for b in range(3):
                max_trace_Y_err = max(max_trace_Y_err, abs(Tm[a + 1, b + 1] - Ym[a, b]))
        _, sH, _ = svd2_exact(Hm)
        _, sM, _ = svd2_exact(Mm)
        _, sT, _ = mp.svd_c(Tm)
        exp_sv = sorted([sH[0] * sM[0], sH[0] * sM[1], sH[1] * sM[0], sH[1] * sM[1]], reverse=True)
        for k in range(4):
            max_kron_sv_err = max(max_kron_sv_err, abs(sT[k] - exp_sv[k]))

        # M1.2 numeric check (two sectors)
        Mwu = mp.matrix([[prng.complex_normal(), prng.complex_normal()], [prng.complex_normal(), prng.complex_normal()]])
        Mwd = mp.matrix([[prng.complex_normal(), prng.complex_normal()], [prng.complex_normal(), prng.complex_normal()]])
        uu, wu = extract_uw_from_Mw(Mwu)
        ud, wd = extract_uw_from_Mw(Mwd)
        Mu = build_M(uu, wu)
        Md = build_M(ud, wd)
        Uu_w, Su_w, _ = svd2_exact(Mwu)
        Ud_w, Sd_w, _ = svd2_exact(Mwd)
        _, Su_m, Vhu_m = svd2_exact(Mu)
        _, Sd_m, Vhd_m = svd2_exact(Md)
        max_kappa_eq_err = max(max_kappa_eq_err, abs(Su_m[1] / Su_m[0] - Su_w[1] / Su_w[0]), abs(Sd_m[1] / Sd_m[0] - Sd_w[1] / Sd_w[0]))

        lu_w = [Uu_w[0, 0], Uu_w[1, 0]]
        ld_w = [Ud_w[0, 0], Ud_w[1, 0]]
        ru_m = [mp.conj(Vhu_m[0, 0]), mp.conj(Vhu_m[0, 1])]
        rd_m = [mp.conj(Vhd_m[0, 0]), mp.conj(Vhd_m[0, 1])]
        # Check rho1(M) == R_u^dagger conj(l1(Mw)) up to phase
        lu_mapped = mat_mul_vec(Ru.transpose_conj(), [mp.conj(lu_w[0]), mp.conj(lu_w[1])])
        max_rho1_spinor_err = max(max_rho1_spinor_err, sin_angle_unit(ru_m, lu_mapped))
        sL_w = spinor_sL_from_cols(lu_w, ld_w)
        sL_m = spinor_sL_from_cols(ru_m, rd_m)
        max_sL_equiv_err = max(max_sL_equiv_err, abs(sL_w - sL_m))

        # Check Q_J left-gauge invariance between E_s^dual and Q_J E_s^dual
        Uuq, Suq, _ = svd2_exact(QJ * Mwu)
        Udq, Sdq, _ = svd2_exact(QJ * Mwd)
        sL_q = spinor_sL_from_cols([Uuq[0, 0], Uuq[1, 0]], [Udq[0, 0], Udq[1, 0]])
        max_QJ_gauge_err = max(
            max_QJ_gauge_err,
            abs(sL_q - sL_w),
            abs(Suq[1] / Suq[0] - Su_w[1] / Su_w[0]),
            abs(Sdq[1] / Sdq[0] - Sd_w[1] / Sd_w[0]),
        )

        # M1.3 numeric Bell check
        UA = prng.haar_unitary(2)
        UB = prng.haar_unitary(2)
        a1 = [UA[0, 0], UA[1, 0]]
        a2 = [UA[0, 1], UA[1, 1]]
        b1 = [UB[0, 0], UB[1, 0]]
        b2 = [UB[0, 1], UB[1, 1]]
        p11 = abs(vec_ip(e0_vec, vec_kron2(a1, b1))) ** 2
        p21 = abs(vec_ip(e0_vec, vec_kron2(a2, b1))) ** 2
        p12 = abs(vec_ip(e0_vec, vec_kron2(a1, b2))) ** 2
        p22 = abs(vec_ip(e0_vec, vec_kron2(a2, b2))) ** 2
        half = mp_rat(1, 2)
        for pv in (p11, p21, p12, p22):
            if pv > half:
                max_bell_single_excess = max(max_bell_single_excess, pv - half)
        max_bell_proj_err = max(
            max_bell_proj_err,
            abs(p11 + p21 - half),
            abs(p11 + p12 - half),
            abs(p22 + p12 - half),
            abs(p22 + p21 - half),
        )

    tol30 = mp_pow10(-30)
    all_sym = all([
        sym_m1_1_trace_zero,
        sym_UP_unitary,
        sym_kron_equiv,
        sym_block_Y,
        sym_H_tr,
        sym_H_det,
        sym_r_mobius,
        sym_sv_ratio,
        sym_Lu_u,
        sym_Ru_u,
        sym_m1_2,
        sym_bell_a,
        sym_bell_b,
        sym_bell_single,
    ])
    all_num = all([
        max_kron_sv_err < tol30,
        max_trace_Y_err < tol30,
        max_kappa_eq_err < tol30,
        max_rho1_spinor_err < tol30,
        max_sL_equiv_err < tol30,
        max_QJ_gauge_err < tol30,
        max_bell_proj_err < tol30,
        max_bell_single_excess < tol30,
    ])
    return {
        "symbolic_checks": {
            "m1_1_trace_identity": sym_m1_1_trace_zero,
            "m1_1_U_pauli_unitary": sym_UP_unitary,
            "m1_1_kronecker_similarity": sym_kron_equiv,
            "m1_1_sl2_block_equals_Y": sym_block_Y,
            "m1_1_H_trace_norm": sym_H_tr,
            "m1_1_H_det_bilinear": sym_H_det,
            "m1_1_r_mobius": sym_r_mobius,
            "m1_1_sv_ratio_t": sym_sv_ratio,
            "m1_2_Lu_unitary": sym_Lu_u,
            "m1_2_Ru_unitary": sym_Ru_u,
            "m1_2_M_equals_2_Lu_MwT_Ru": sym_m1_2,
            "m1_3_bell_subspace_a_half": sym_bell_a,
            "m1_3_bell_subspace_b_half": sym_bell_b,
            "m1_3_bell_product_formula": sym_bell_single,
        },
        "numeric_dps": 50,
        "numeric_trials": 50,
        "max_kron_sv_err": mp_sci(max_kron_sv_err),
        "max_trace_Y_err": mp_sci(max_trace_Y_err),
        "max_kappa_eq_err": mp_sci(max_kappa_eq_err),
        "max_rho1_spinor_err": mp_sci(max_rho1_spinor_err),
        "max_sL_equiv_err": mp_sci(max_sL_equiv_err),
        "max_QJ_gauge_err": mp_sci(max_QJ_gauge_err),
        "max_bell_proj_err": mp_sci(max_bell_proj_err),
        "max_bell_single_excess": mp_sci(max_bell_single_excess),
        "passed": all_sym and all_num,
    }


# ============================================================================
# Gate RG2: M2 — Explicit Bell-Split Subspace Audit, Witness & 2,200 Trials
# ============================================================================

def run_M2() -> dict:
    # --- Symbolic Proofs in SymPy ---
    t_s, k_s, cp_s, rho_s = sp.symbols("t_s k_s cp_s rho_s", positive=True)
    I = sp.I
    k_star = t_s / (1 + 2 * t_s)
    sym_cross_eq = sp.simplify(t_s * k_star - (t_s - k_star) / 2) == 0
    sym_floor_val = sp.simplify(t_s * k_star - t_s**2 / (1 + 2 * t_s)) == 0
    sym_r1_third = sp.simplify((t_s**2 / (1 + 2 * t_s)).subs(t_s, 1) - sp.Rational(1, 3)) == 0
    # Canonical witness B^H Y B / cp
    ep = sp.Matrix([1, I, 0]) / sp.sqrt(2)
    em = sp.Matrix([1, -I, 0]) / sp.sqrt(2)
    e3 = sp.Matrix([0, 0, 1])
    B = sp.Matrix.hstack(ep, em, e3)
    h_w = cp_s * em + cp_s * t_s * ep
    u_w = em - k_s * ep
    Y_w = u_w * h_w.T + h_w * u_w.T - u_w.dot(h_w) * sp.eye(3)
    BYB = sp.simplify(B.H * Y_w * B / cp_s)
    expected_BYB = sp.Matrix([[0, -2 * t_s * k_s, 0], [2, 0, 0], [0, 0, -(t_s - k_s)]])
    sym_witness_mat = sp.simplify(BYB - expected_BYB) == sp.zeros(3, 3)
    # Bottleneck quadratic M^2 - 2*rho*M - rho = 0 -> M = rho + sqrt(rho^2 + rho)
    M_root = rho_s + sp.sqrt(rho_s**2 + rho_s)
    sym_bottleneck = sp.simplify(M_root**2 / (1 + 2 * M_root) - rho_s) == 0

    # --- 2,200 Trials with EXPLICIT Bell-Split Subspace Construction (dps = 30) ---
    mp.mp.dps = 30
    prng = Sha256Prng("referee-M2-bell-v1")
    inv_sq2 = mp.mpf(1) / mp.sqrt(2)
    e0_vec = [inv_sq2, mp.mpf(0), mp.mpf(0), inv_sq2]
    U_P = mp.matrix([
        [1, 0, 0, 1],
        [0, 1, -mp.j, 0],
        [0, 1, mp.j, 0],
        [1, 0, 0, -1],
    ]) * inv_sq2
    # Projector onto sl_2 in C^4: P_sl2 = I_4 - e0 e0^dagger
    P_sl2 = mp.eye(4)
    for i in range(4):
        for j in range(4):
            P_sl2[i, j] -= e0_vec[i] * mp.conj(e0_vec[j])

    # Build 2,000 random + 200 adversarial boundary/corner (t, kap) pairs
    tk_pairs = []
    for idx in range(2000):
        mode = idx % 5
        if mode == 0:
            # Uniform r in [0, 1], uniform kap in [0, 1]
            r_v = prng.uniform_open01()
            t_v = reality_to_t(r_v)
            k_v = prng.uniform_open01()
        elif mode == 1:
            # Near crossing kap = t/(1 + 2t)
            t_v = prng.uniform_open01()
            k_opt = t_v / (1 + 2 * t_v)
            delta = prng.uniform_range(mp_rat(-1, 50), mp_rat(1, 50))
            k_v = clamp_nonneg_unit(k_opt + delta)
        elif mode == 2:
            # Small t, small kap (log-uniform down to 10^-6)
            t_v = mp.exp(prng.uniform_range(-14 * mp.mpf(1), mp.mpf(0)))
            k_v = mp.exp(prng.uniform_range(-14 * mp.mpf(1), mp.mpf(0)))
        elif mode == 3:
            # t ~ kap diagonal
            t_v = prng.uniform_open01()
            k_v = clamp_nonneg_unit(t_v + prng.uniform_range(mp_rat(-1, 100), mp_rat(1, 100)))
        else:
            # Large t near 1 or large kap near 1
            t_v = mp.mpf(1) - mp.exp(prng.uniform_range(-12 * mp.mpf(1), -mp.mpf(1)))
            k_v = prng.uniform_open01()
        tk_pairs.append((t_v, k_v))

    # 200 targeted boundary/corner trials
    corner_grid = [mp.mpf(0), mp_pow10(-6), mp_rat(1, 100), mp_rat(1, 10), mp_rat(1, 3), mp_rat(1, 2), mp_rat(9, 10), mp.mpf(1) - mp_pow10(-6), mp.mpf(1)]
    for tv in corner_grid:
        for kv in corner_grid:
            tk_pairs.append((tv, kv))  # 81 pairs
    for k_idx in range(119):
        tv = mp_rat(k_idx, 118)
        kv = tv / (1 + 2 * tv) if tv > 0 else mp.mpf(0)
        tk_pairs.append((tv, kv))  # exact optimal floor curve

    max_bell_V12_err = mp.mpf(0)
    max_bell_U12_err = mp.mpf(0)
    max_subspace_orth_e0_err = mp.mpf(0)
    max_B_decomp_err = mp.mpf(0)
    max_viol_sigma2_B12 = mp.mpf(0)
    max_viol_norm_B34 = mp.mpf(0)
    max_viol_sigma2_B = mp.mpf(0)
    max_viol_m2_ge_sigma2_B = mp.mpf(0)
    max_viol_m2_ge_tk = mp.mpf(0)
    max_viol_m3_le_1 = mp.mpf(0)
    max_viol_two_var_floor = mp.mpf(0)
    max_viol_univ_floor = mp.mpf(0)
    min_slack_two_var = mp.mpf(10)
    min_slack_univ = mp.mpf(10)

    for tv, kv in tk_pairs:
        h = build_h_with_t(prng, tv)
        Mm, u_vec, w_val = build_M_with_kappa(prng, kv)
        Hm = build_H(h)
        Ym = build_Y(h, u_vec, w_val)

        Uh, Sh, Vhh = svd2_exact(Hm)
        Um, Sm, Vhm = svd2_exact(Mm)
        # Normalize H_hat = Hm / Sh[0], M_hat = Mm / Sm[0]
        H_hat = Hm / Sh[0]
        M_hat = Mm / Sm[0]
        Y_hat = Ym / (Sh[0] * Sm[0])
        t_meas = Sh[1] / Sh[0]
        k_meas = Sm[1] / Sm[0]

        # SVD of H_hat and M_hat^T for Kronecker operator T_hat = H_hat kron M_hat^T
        U_h, S_h, Vh_h = svd2_exact(H_hat)
        U_mt, S_mt, Vh_mt = svd2_exact(M_hat.T)
        al1 = [U_h[0, 0], U_h[1, 0]]
        al2 = [U_h[0, 1], U_h[1, 1]]
        be1 = [mp.conj(Vh_h[0, 0]), mp.conj(Vh_h[0, 1])]
        be2 = [mp.conj(Vh_h[1, 0]), mp.conj(Vh_h[1, 1])]
        ga1 = [U_mt[0, 0], U_mt[1, 0]]
        ga2 = [U_mt[0, 1], U_mt[1, 1]]
        de1 = [mp.conj(Vh_mt[0, 0]), mp.conj(Vh_mt[0, 1])]
        de2 = [mp.conj(Vh_mt[1, 0]), mp.conj(Vh_mt[1, 1])]

        if t_meas >= k_meas:
            s_hi, s_lo = t_meas, k_meas
            u1, v1 = vec_kron2(al1, ga1), vec_kron2(be1, de1)
            u2, v2 = vec_kron2(al2, ga1), vec_kron2(be2, de1)
            u3, v3 = vec_kron2(al1, ga2), vec_kron2(be1, de2)
            u4, v4 = vec_kron2(al2, ga2), vec_kron2(be2, de2)
        else:
            s_hi, s_lo = k_meas, t_meas
            u1, v1 = vec_kron2(al1, ga1), vec_kron2(be1, de1)
            u2, v2 = vec_kron2(al1, ga2), vec_kron2(be1, de2)
            u3, v3 = vec_kron2(al2, ga1), vec_kron2(be2, de1)
            u4, v4 = vec_kron2(al2, ga2), vec_kron2(be2, de2)

        # Build T_12 and T_34 explicitly in C^4
        T12 = mp.matrix(4, 4)
        T34 = mp.matrix(4, 4)
        for i in range(4):
            for j in range(4):
                T12[i, j] = u1[i] * mp.conj(v1[j]) + s_hi * u2[i] * mp.conj(v2[j])
                T34[i, j] = s_lo * u3[i] * mp.conj(v3[j]) + (t_meas * k_meas) * u4[i] * mp.conj(v4[j])

        # Explicit Bell-split construction for W = span{w1, z2} in sl_2
        cv1 = vec_ip(v1, e0_vec)
        cv2 = vec_ip(v2, e0_vec)
        norm2_V12 = abs(cv1) ** 2 + abs(cv2) ** 2
        max_bell_V12_err = max(max_bell_V12_err, abs(norm2_V12 - mp_rat(1, 2)))
        w2_raw = [cv1 * v1[i] + cv2 * v2[i] for i in range(4)]
        w2p_raw = [e0_vec[i] - w2_raw[i] for i in range(4)]
        n_w2 = vec_norm(w2_raw)
        n_w2p = vec_norm(w2p_raw)
        w2 = [x / n_w2 for x in w2_raw]
        w2p = [x / n_w2p for x in w2p_raw]
        # Unit coefficients (c1, c2) of w2 in {v1, v2}
        c1, c2 = cv1 / n_w2, cv2 / n_w2
        w1 = [-mp.conj(c2) * v1[i] + mp.conj(c1) * v2[i] for i in range(4)]
        z2 = [(w2[i] - w2p[i]) * inv_sq2 for i in range(4)]

        # Explicit Bell-split construction for W' = span{u1', z2'} in sl_2
        du1 = vec_ip(u1, e0_vec)
        du2 = vec_ip(u2, e0_vec)
        norm2_U12 = abs(du1) ** 2 + abs(du2) ** 2
        max_bell_U12_err = max(max_bell_U12_err, abs(norm2_U12 - mp_rat(1, 2)))
        u2p_raw = [du1 * u1[i] + du2 * u2[i] for i in range(4)]
        u2pp_raw = [e0_vec[i] - u2p_raw[i] for i in range(4)]
        n_u2p = vec_norm(u2p_raw)
        n_u2pp = vec_norm(u2pp_raw)
        u2p = [x / n_u2p for x in u2p_raw]
        u2pp = [x / n_u2pp for x in u2pp_raw]
        d1, d2 = du1 / n_u2p, du2 / n_u2p
        u1p = [-mp.conj(d2) * u1[i] + mp.conj(d1) * u2[i] for i in range(4)]
        z2p = [(u2p[i] - u2pp[i]) * inv_sq2 for i in range(4)]

        max_subspace_orth_e0_err = max(
            max_subspace_orth_e0_err,
            abs(vec_ip(e0_vec, w1)),
            abs(vec_ip(e0_vec, z2)),
            abs(vec_ip(e0_vec, u1p)),
            abs(vec_ip(e0_vec, z2p)),
        )

        # Build 4x2 basis matrices W and Wp
        W_mat = mp.matrix([[w1[i], z2[i]] for i in range(4)])
        Wp_mat = mp.matrix([[u1p[i], z2p[i]] for i in range(4)])
        B12 = Wp_mat.transpose_conj() * T12 * W_mat
        B34 = Wp_mat.transpose_conj() * T34 * W_mat
        B_sum = B12 + B34

        # Verify B_sum == Wp^H (P_sl2 T_hat P_sl2) W
        T_hat_4 = kron2(H_hat, M_hat.T)
        B_direct = Wp_mat.transpose_conj() * (P_sl2 * T_hat_4 * P_sl2) * W_mat
        max_B_decomp_err = max(max_B_decomp_err, frob_norm(B_sum - B_direct))

        # Verify ALL intermediate proof steps!
        _, sB12, _ = svd2_exact(B12)
        _, sB34, _ = svd2_exact(B34)
        _, sB, _ = svd2_exact(B_sum)
        _, sY, _ = mp.svd_c(Y_hat)
        m3_hat, m2_hat = sY[0], sY[1]
        rho_val = m2_hat / m3_hat

        v1_err = (s_hi / 2) - sB12[1]
        v2_err = sB34[0] - (s_lo / 2)
        v3_err = (abs(t_meas - k_meas) / 2) - sB[1]
        v4_err = sB[1] - m2_hat
        v5_err = (t_meas * k_meas) - m2_hat
        v6_err = m3_hat - mp.mpf(1)

        two_var_floor = max(t_meas * k_meas, abs(t_meas - k_meas) / 2)
        univ_floor = (t_meas * t_meas) / (1 + 2 * t_meas)
        v7_err = two_var_floor - rho_val
        v8_err = univ_floor - rho_val

        max_viol_sigma2_B12 = max(max_viol_sigma2_B12, v1_err)
        max_viol_norm_B34 = max(max_viol_norm_B34, v2_err)
        max_viol_sigma2_B = max(max_viol_sigma2_B, v3_err)
        max_viol_m2_ge_sigma2_B = max(max_viol_m2_ge_sigma2_B, v4_err)
        max_viol_m2_ge_tk = max(max_viol_m2_ge_tk, v5_err)
        max_viol_m3_le_1 = max(max_viol_m3_le_1, v6_err)
        max_viol_two_var_floor = max(max_viol_two_var_floor, v7_err)
        max_viol_univ_floor = max(max_viol_univ_floor, v8_err)
        min_slack_two_var = min(min_slack_two_var, rho_val - two_var_floor)
        min_slack_univ = min(min_slack_univ, rho_val - univ_floor)

    # --- Exact 50-Digit Check of Canonical Witness Across 11 Rational Reality Values ---
    mp.mp.dps = 50
    inv_sq2_50 = mp.mpf(1) / mp.sqrt(2)
    ep_50 = [inv_sq2_50, mp.j * inv_sq2_50, mp.mpf(0)]
    em_50 = [inv_sq2_50, -mp.j * inv_sq2_50, mp.mpf(0)]
    r_grid_11 = [
        Fraction(0, 1),
        Fraction(1, 1000),
        Fraction(1, 100),
        Fraction(1, 20),
        Fraction(1, 10),
        Fraction(1, 5),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(9, 10),
        Fraction(1, 1),
    ]
    witness_rows = []
    max_witness_err = mp.mpf(0)
    for rf in r_grid_11:
        rm = mp_frac(rf)
        tm = reality_to_t(rm)
        k_opt = tm / (1 + 2 * tm) if tm > 0 else mp.mpf(0)
        # h = e_- + t e_+ (with c_+ = 1), u = e_- - k_opt e_+, w = 0
        hw = [em_50[i] + tm * ep_50[i] for i in range(3)]
        uw = [em_50[i] - k_opt * ep_50[i] for i in range(3)]
        Yw = build_Y(hw, uw, mp.mpf(0))
        Hm = build_H(hw)
        Mm = build_M(uw, mp.mpf(0))
        _, sH, _ = svd2_exact(Hm)
        _, sM, _ = svd2_exact(Mm)
        _, sY, _ = mp.svd_c(Yw)
        m3_hat = sY[0] / (sH[0] * sM[0])
        m2_hat = sY[1] / (sH[0] * sM[0])
        rho_w = sY[1] / sY[0]
        exact_floor = (tm * tm) / (1 + 2 * tm)
        err = max(abs(rho_w - exact_floor), abs(m2_hat - exact_floor), abs(m3_hat - mp.mpf(1)))
        max_witness_err = max(max_witness_err, err)
        witness_rows.append({
            "r": frac_str(rf),
            "t": mp_str(tm, 25),
            "kappa_star": mp_str(k_opt, 25),
            "m2_over_m3": mp_str(rho_w, 25),
            "exact_floor": mp_str(exact_floor, 25),
            "abs_err": mp_sci(err),
        })

    tol25 = mp_pow10(-25)
    tol45 = mp_pow10(-45)
    all_sym = all([sym_cross_eq, sym_floor_val, sym_r1_third, sym_witness_mat, sym_bottleneck])
    all_num = all([
        max_bell_V12_err < tol25,
        max_bell_U12_err < tol25,
        max_subspace_orth_e0_err < tol25,
        max_B_decomp_err < tol25,
        max_viol_sigma2_B12 < tol25,
        max_viol_norm_B34 < tol25,
        max_viol_sigma2_B < tol25,
        max_viol_m2_ge_sigma2_B < tol25,
        max_viol_m2_ge_tk < tol25,
        max_viol_m3_le_1 < tol25,
        max_viol_two_var_floor < tol25,
        max_viol_univ_floor < tol25,
        max_witness_err < tol45,
    ])
    return {
        "symbolic_checks": {
            "crossing_kappa_star": sym_cross_eq,
            "universal_floor_formula": sym_floor_val,
            "r1_recovers_one_third": sym_r1_third,
            "canonical_witness_matrix": sym_witness_mat,
            "bottleneck_inverse": sym_bottleneck,
        },
        "n_trials_total": len(tk_pairs),
        "n_trials_random": 2000,
        "n_trials_corner": len(tk_pairs) - 2000,
        "bell_split_intermediate_checks": {
            "max_bell_V12_err": mp_sci(max_bell_V12_err),
            "max_bell_U12_err": mp_sci(max_bell_U12_err),
            "max_subspace_orth_e0_err": mp_sci(max_subspace_orth_e0_err),
            "max_B_decomp_err": mp_sci(max_B_decomp_err),
            "max_viol_sigma2_B12_ge_max_half": mp_sci(max_viol_sigma2_B12),
            "max_viol_norm_B34_le_min_half": mp_sci(max_viol_norm_B34),
            "max_viol_sigma2_B_ge_diff_half": mp_sci(max_viol_sigma2_B),
            "max_viol_m2_hat_ge_sigma2_B": mp_sci(max_viol_m2_ge_sigma2_B),
            "max_viol_m2_hat_ge_t_kappa": mp_sci(max_viol_m2_ge_tk),
            "max_viol_m3_hat_le_1": mp_sci(max_viol_m3_le_1),
            "max_viol_two_var_floor": mp_sci(max_viol_two_var_floor),
            "max_viol_univ_floor": mp_sci(max_viol_univ_floor),
            "min_slack_two_var": mp_sci(min_slack_two_var),
            "min_slack_univ": mp_sci(min_slack_univ),
        },
        "canonical_witness_11_pts_dps50": witness_rows,
        "max_witness_err_dps50": mp_sci(max_witness_err),
        "passed": all_sym and all_num,
    }


# ============================================================================
# Gate RG3: M3 — Single-Sector Perturbation, Two-Sector Trade-Off & Controls
# ============================================================================

def compute_vhat(H_mat: mp.matrix, M_mat: mp.matrix) -> tuple[list, list, list]:
    """Return (v_hat in C^3, alpha_1 of H, rho_1 of M)."""
    Uh, _, _ = svd2_exact(H_mat)
    _, _, Vhm = svd2_exact(M_mat)
    al1 = [Uh[0, 0], Uh[1, 0]]
    rho1 = [mp.conj(Vhm[0, 0]), mp.conj(Vhm[0, 1])]
    _, s1, s2, s3 = pauli_matrices()
    # (u1)_a = (1/sqrt(2)) rho1^dagger sigma_a alpha_1
    v_raw = []
    for sig in (s1, s2, s3):
        sa = mat_mul_vec(sig, al1)
        v_raw.append(vec_ip(rho1, sa))
    nrm = vec_norm(v_raw)
    v_hat = [x / nrm for x in v_raw]
    return v_hat, al1, rho1


def run_M3() -> dict:
    # --- Symbolic Proofs in SymPy ---
    rho_s, S_s, t_s, sL_s = sp.symbols("rho_s S_s t_s sL_s", positive=True)
    # 1. Non-degeneracy bound at rho = 1/6
    m_bound_sixth = sp.simplify((rho_s + sp.sqrt(rho_s**2 + rho_s)).subs(rho_s, sp.Rational(1, 6)))
    sym_nondeg_lt_1 = bool(m_bound_sixth < 1)
    # 2. Crossing M_*(rho) = sqrt(rho / (2*(1 + 2*rho)))
    M_star = sp.sqrt(rho_s / (2 * (1 + 2 * rho_s)))
    g1 = 2 * M_star / (1 - 2 * M_star)
    g2 = rho_s * (1 + 2 * M_star) / M_star
    S_val = sp.sqrt(2 * rho_s * (1 + 2 * rho_s)) + 2 * rho_s
    sym_cross_g1_g2 = sp.simplify(g1 - g2) == 0
    sym_cross_S = sp.simplify(g2 - S_val) == 0
    # 3. Exact inverse rho(S) = S^2 / (2*(1 + 2*S)) (factor perfect-square radicand before sqrt)
    rho_of_S = S_s**2 / (2 * (1 + 2 * S_s))
    sym_inverse_S = sp.simplify(sp.sqrt(sp.factor(2 * rho_of_S * (1 + 2 * rho_of_S))) + 2 * rho_of_S - S_s) == 0
    # 4. M_*(rho(S)) == S / (2*(1 + S))
    t1_expr = S_s / (2 * (1 + S_s))
    sym_t1_match = sp.simplify(sp.sqrt(sp.factor(rho_of_S / (2 * (1 + 2 * rho_of_S)))) - t1_expr) == 0
    # 5. Three-regime F continuity at t1 and t2 = S_s
    F1 = S_s**2 / (2 * (1 + 2 * S_s))
    F2 = S_s * t_s / (1 + 2 * t_s)
    F3 = t_s**2 / (1 + 2 * t_s)
    sym_F_cont1 = sp.simplify(F2.subs(t_s, t1_expr) - F1) == 0
    sym_F_cont2 = sp.simplify(F2.subs(t_s, S_s) - F3.subs(t_s, S_s)) == 0
    # 6. Max F2 over all possible S_req <= 1/sqrt(3) is strictly < 1/6
    F2_max_at_inv_sq3 = sp.simplify(F3.subs(t_s, 1 / sp.sqrt(3)))
    sym_F2_lt_sixth = bool(F2_max_at_inv_sq3 < sp.Rational(1, 6))
    # 7. Conjugate Higgs identity H(hbar) = -eps conj(H(h)) eps^H
    I = sp.I
    hr1, hr2, hr3, hi1, hi2, hi3 = sp.symbols("hr1 hr2 hr3 hi1 hi2 hi3", real=True)
    sp1 = sp.Matrix([[0, 1], [1, 0]])
    sp2 = sp.Matrix([[0, -I], [I, 0]])
    sp3 = sp.Matrix([[1, 0], [0, -1]])
    eps_s = sp.Matrix([[0, 1], [-1, 0]])
    H_s = (hr1 + I * hi1) * sp1 + (hr2 + I * hi2) * sp2 + (hr3 + I * hi3) * sp3
    Hbar_s = (hr1 - I * hi1) * sp1 + (hr2 - I * hi2) * sp2 + (hr3 - I * hi3) * sp3
    sym_conj_H = sp.simplify(Hbar_s + eps_s * sp.conjugate(H_s) * eps_s.H) == sp.zeros(2, 2)
    # 8. Symbolic Möbius ceiling (1 + s_L)/(3 - s_L) attained at xi = (cos t_*, -sin t_*)
    # In canonical gauge rho_d = e_1, rho_u = (cos alpha, sin alpha) with sin alpha = s_L, alpha in [0, pi/2]
    al_sym, th_sym = sp.symbols("al_sym th_sym", real=True)
    rd_g = sp.Matrix([1, 0])
    ru_g = sp.Matrix([sp.cos(al_sym), sp.sin(al_sym)])
    xi_g = sp.Matrix([sp.cos(th_sym), -sp.sin(th_sym)])
    xi_u_g = eps_s * xi_g  # real xi -> bar(xi) = xi
    vd_g = sp.Matrix([(rd_g.H * sig * xi_g)[0] for sig in (sp1, sp2, sp3)])
    vu_g = sp.Matrix([(ru_g.H * sig * xi_u_g)[0] for sig in (sp1, sp2, sp3)])
    num_sq = sp.simplify(sp.trigsimp((vu_g.H * vd_g)[0] * sp.conjugate((vu_g.H * vd_g)[0])))
    den_sq = sp.simplify(sp.trigsimp((vu_g.H * vu_g)[0] * (vd_g.H * vd_g)[0]))
    t_opt_s = sp.pi / 4 - al_sym / 2
    val_at_opt = sp.simplify(sp.trigsimp((num_sq / den_sq).subs(th_sym, t_opt_s)))
    mob_sq = ((1 + sp.sin(al_sym)) / (3 - sp.sin(al_sym))) ** 2
    sym_mobius_attain = sp.simplify(sp.trigsimp(val_at_opt - mob_sq)) == 0

    # --- Exact 50-digit s_L^crit(9/10, 1/100) ---
    mp.mp.dps = 50
    rho_ref = mp_rat(1, 100)
    a_ref = mp_rat(9, 10)
    S_ref = S_t_bound(mp.mpf(0), rho_ref)
    c_crit = mp.cos(mp.acos(a_ref) + 2 * mp.asin(S_ref))
    sL_crit_exact = (3 * c_crit - 1) / (1 + c_crit)

    # --- 2,200 Two-Sector Adversarial Trials across r in [0, 1) (dps = 30) ---
    mp.mp.dps = 30
    prng = Sha256Prng("referee-M3-twosector-v1")
    eps_m = mp.matrix([[0, 1], [-1, 0]])
    sixth = mp_rat(1, 6)

    n_trials_total = 2200
    n_rho_lt_sixth = 0
    max_conj_spinor_err = mp.mpf(0)
    max_viol_sin_theta_u = mp.mpf(0)
    max_viol_sin_theta_d = mp.mpf(0)
    max_viol_vhat_mobius = mp.mpf(0)
    max_viol_V33_ceiling = mp.mpf(0)
    max_viol_F_floor = mp.mpf(0)
    min_slack_V33 = mp.mpf(10)
    min_slack_F = mp.mpf(10)

    for idx in range(n_trials_total):
        if idx < 2000:
            mode = idx % 5
            if mode == 0:
                # Hierarchical small (t, kappa_u, kappa_d) -> mostly rho < 1/6
                t_v = mp.exp(prng.uniform_range(-12 * mp.mpf(1), -2 * mp.mpf(1)))
                ku = mp.exp(prng.uniform_range(-12 * mp.mpf(1), -2 * mp.mpf(1)))
                kd = mp.exp(prng.uniform_range(-12 * mp.mpf(1), -2 * mp.mpf(1)))
            elif mode == 1:
                # Moderate interior t in [0.01, 0.45], small kappa -> stress-tests Regime 2!
                t_v = prng.uniform_range(mp_rat(1, 100), mp_rat(45, 100))
                ku = prng.uniform_range(mp.mpf(0), mp_rat(1, 5))
                kd = prng.uniform_range(mp.mpf(0), mp_rat(1, 5))
            elif mode == 2:
                # Near-aligned spinors (small s_L) with small t, kappa
                t_v = mp.exp(prng.uniform_range(-10 * mp.mpf(1), -mp.mpf(1)))
                ku = mp.exp(prng.uniform_range(-10 * mp.mpf(1), -mp.mpf(1)))
                kd = mp.exp(prng.uniform_range(-10 * mp.mpf(1), -mp.mpf(1)))
            elif mode == 3:
                # Generic full interior r in (0, 1), generic kappa in [0, 1]
                r_v = prng.uniform_open01()
                t_v = reality_to_t(r_v)
                ku = prng.uniform_open01()
                kd = prng.uniform_open01()
            else:
                # High reality r near 1 (Regime 3)
                t_v = prng.uniform_range(mp_rat(1, 2), mp.mpf(1) - mp_pow10(-6))
                ku = prng.uniform_open01()
                kd = prng.uniform_open01()
            h = build_h_with_t(prng, t_v)
            Mu, uu, wu = build_M_with_kappa(prng, ku)
            Md, ud, wd = build_M_with_kappa(prng, kd)
        else:
            # 200 targeted adversarial trials: Möbius-optimal xi with controlled s_L in [0, 1]
            sub = idx - 2000
            sL_target = mp_rat(sub % 20, 19)
            al_t = mp.asin(clamp_nonneg_unit(sL_target))
            t_star = mp.pi / 4 - al_t / 2
            # Set t_v spanning [0, 0.5]
            t_v = mp_rat((sub // 20), 20)
            ku = prng.uniform_range(mp.mpf(0), mp_rat(1, 10))
            kd = prng.uniform_range(mp.mpf(0), mp_rat(1, 10))
            # Build H(h) whose top left singular vector is xi = (cos t_*, -sin t_*)
            # Note H = sigma_1 xi eta^dagger + sigma_2 xi_perp eta_perp^dagger must be traceless!
            # Traceless condition for H = a1 b1^dagger + t a2 b2^dagger:
            # Tr(H) = b1^dagger a1 + t b2^dagger a2 = 0.
            # Pick b1 = eps conj(a1) (= (-conj(a1_1), conj(a1_0))^T -> b1^dagger a1 = 0!),
            # and b2 = eps conj(a2) (= -a1_perp -> b2^dagger a2 = 0!).
            # Check: for real xi = (c, -s), b1 = (s, c), xi_perp = (s, c), b2 = (-c, s):
            # H = xi b1^T + t xi_perp b2^T -> Tr = 0 + 0 = 0!
            xi_v = [mp.cos(t_star), -mp.sin(t_star)]
            xi_p = [mp.sin(t_star), mp.cos(t_star)]
            b1_v = [mp.sin(t_star), mp.cos(t_star)]
            b2_v = [-mp.cos(t_star), mp.sin(t_star)]
            Hm_adv = mp.matrix(2, 2)
            for i in range(2):
                for j in range(2):
                    Hm_adv[i, j] = xi_v[i] * mp.conj(b1_v[j]) + t_v * xi_p[i] * mp.conj(b2_v[j])
            _, s1, s2, s3 = pauli_matrices()
            h = [
                ((Hm_adv * s1)[0, 0] + (Hm_adv * s1)[1, 1]) / 2,
                ((Hm_adv * s2)[0, 0] + (Hm_adv * s2)[1, 1]) / 2,
                ((Hm_adv * s3)[0, 0] + (Hm_adv * s3)[1, 1]) / 2,
            ]
            hn = vec_norm(h)
            h = [x / hn for x in h]
            rd_target = [mp.mpf(1), mp.mpf(0)]
            ru_target = [mp.cos(al_t), mp.sin(al_t)]
            Mu, uu, wu = build_M_with_rho1_kappa(prng, ru_target, ku)
            Md, ud, wd = build_M_with_rho1_kappa(prng, rd_target, kd)

        hbar = [mp.conj(x) for x in h]
        Hd = build_H(h)
        Hu = build_H(hbar)
        _, Shd, _ = svd2_exact(Hd)
        t_meas = Shd[1] / Shd[0]

        Yd = build_Y(h, ud, wd)
        Yu = build_Y(hbar, uu, wu)
        Ud, Sd, _ = mp.svd_c(Yd)
        Uu, Su, _ = mp.svd_c(Yu)
        rho_d = Sd[1] / Sd[0]
        rho_u = Su[1] / Su[0]
        rho_max = max(rho_u, rho_d)

        u3_d = [Ud[i, 0] for i in range(3)]
        u3_u = [Uu[i, 0] for i in range(3)]
        V33 = abs(vec_ip(u3_u, u3_d))

        vh_d, al_d, rho1_d = compute_vhat(Hd, Md)
        vh_u, al_u, rho1_u = compute_vhat(Hu, Mu)
        sL_val = spinor_sL_from_cols(rho1_u, rho1_d)

        # Check F(t; sL, |V33|) <= rho_max unconditionally on ALL 2,200 trials!
        F_val = F_three_regime(t_meas, sL_val, V33)
        max_viol_F_floor = max(max_viol_F_floor, F_val - rho_max)
        min_slack_F = min(min_slack_F, rho_max - F_val)

        if rho_max < sixth:
            n_rho_lt_sixth += 1
            # Check conjugate spinor identity al_u == eps conj(al_d) up to phase
            al_u_exp = mat_mul_vec(eps_m, [mp.conj(al_d[0]), mp.conj(al_d[1])])
            max_conj_spinor_err = max(max_conj_spinor_err, sin_angle_unit(al_u, al_u_exp))

            st_u = sin_angle_unit(u3_u, vh_u)
            st_d = sin_angle_unit(u3_d, vh_d)
            max_viol_sin_theta_u = max(max_viol_sin_theta_u, st_u - S_t_bound(t_meas, rho_u))
            max_viol_sin_theta_d = max(max_viol_sin_theta_d, st_d - S_t_bound(t_meas, rho_d))

            vh_ip = abs(vec_ip(vh_u, vh_d))
            mob_lim = (1 + sL_val) / (3 - sL_val)
            max_viol_vhat_mobius = max(max_viol_vhat_mobius, vh_ip - mob_lim)

            ceil_V33 = V33_ceiling(t_meas, sL_val, rho_max)
            max_viol_V33_ceiling = max(max_viol_V33_ceiling, V33 - ceil_V33)
            min_slack_V33 = min(min_slack_V33, ceil_V33 - V33)

    # --- Positive Controls at dps = 50 ---
    mp.mp.dps = 50
    # Control 1: C1-A at r = 1/2000, s_L = 1 (orthogonal rank-1 spinors, Möbius-optimal xi)
    r_c1a = mp_rat(1, 2000)
    t_c1a = reality_to_t(r_c1a)
    # s_L = 1 -> alpha = pi/2 -> t_* = 0 -> xi = (1, 0), b1 = (0, 1), xi_p = (0, 1), b2 = (-1, 0)
    # H = [[0, 1], [-t, 0]] -> h_1 = (1-t)/2, h_2 = i(1+t)/2, h_3 = 0!
    # Check: h.h = (1-t)^2/4 - (1+t)^2/4 = -t, ||h||^2 = (1+t^2)/2 -> |h.h|/||h||^2 = 2t/(1+t^2) = r!
    den_c1a = mp.sqrt((1 + t_c1a * t_c1a) / 2)
    h_c1a = [(1 - t_c1a) / (2 * den_c1a), mp.j * (1 + t_c1a) / (2 * den_c1a), mp.mpf(0)]
    hbar_c1a = [mp.conj(x) for x in h_c1a]
    # Rank-1 M_d with rho1_d = e_1 = (1, 0), lambda_d = (1, 0) -> M_d = [[1, 0], [0, 0]]
    # Rank-1 M_u with rho1_u = e_2 = (0, 1), lambda_u = (0, 1) -> M_u = [[0, 0], [0, 1]]
    Md_c1a = mp.matrix([[1, 0], [0, 0]])
    Mu_c1a = mp.matrix([[0, 0], [0, 1]])
    _, s1_50, s2_50, s3_50 = pauli_matrices()
    ud_c1a = [mp.mpf(0), mp.mpf(0), mp_rat(1, 2)]
    wd_c1a = mp.j * mp_rat(1, 2)
    uu_c1a = [mp.mpf(0), mp.mpf(0), mp_rat(-1, 2)]
    wu_c1a = mp.j * mp_rat(1, 2)
    Yd_c1a = build_Y(h_c1a, ud_c1a, wd_c1a)
    Yu_c1a = build_Y(hbar_c1a, uu_c1a, wu_c1a)
    Ud_c1a, Sd_c1a, _ = mp.svd_c(Yd_c1a)
    Uu_c1a, Su_c1a, _ = mp.svd_c(Yu_c1a)
    rho_u_c1a = Su_c1a[1] / Su_c1a[0]
    rho_d_c1a = Sd_c1a[1] / Sd_c1a[0]
    rho_c1a = max(rho_u_c1a, rho_d_c1a)
    V33_c1a = abs(vec_ip([Uu_c1a[i, 0] for i in range(3)], [Ud_c1a[i, 0] for i in range(3)]))
    vh_u_c1a, _, r1u_c1a = compute_vhat(build_H(hbar_c1a), Mu_c1a)
    vh_d_c1a, _, r1d_c1a = compute_vhat(build_H(h_c1a), Md_c1a)
    sL_c1a = spinor_sL_from_cols(r1u_c1a, r1d_c1a)
    F_c1a = F_three_regime(t_c1a, sL_c1a, V33_c1a)
    ceil_c1a = V33_ceiling(t_c1a, sL_c1a, rho_c1a)
    c1a_ok = (
        abs(sL_c1a - 1) < mp_pow10(-45)
        and rho_c1a <= mp_rat(1, 100)
        and V33_c1a >= mp_rat(9, 10)
        and rho_c1a >= F_c1a - mp_pow10(-45)
        and V33_c1a <= ceil_c1a + mp_pow10(-45)
    )

    # Control 2: B1967 exact 16-rational counterexample at r = 3/1000
    uu_b = [
        mp.mpc(mp_rat(8112623, 23657898), mp_rat(29517392, 42170071)),
        mp.mpc(mp_rat(-32191861, 58976063), mp_rat(10109002, 39589433)),
        mp.mpc(mp_rat(8361869, 35299624), mp_rat(201121, 6549724)),
    ]
    wu_b = mp.mpc(mp_rat(32621059, 80596130), mp_rat(-2122066, 7900781))
    ud_b = [
        mp.mpc(mp_rat(8253345, 14846974), mp_rat(32273371, 84797632)),
        mp.mpc(mp_rat(13917810, 48354631), mp_rat(-69799368, 69016585)),
        mp.mpc(mp_rat(29492199, 87199192), mp_rat(-23893336, 16802917)),
    ]
    wd_b = mp.mpc(mp_rat(126906246, 75918835), mp_rat(16923861, 50797165))
    r_b = mp_rat(3, 1000)
    t_b = reality_to_t(r_b)
    h_b = [mp.sqrt((1 + r_b) / 2), mp.j * mp.sqrt((1 - r_b) / 2), mp.mpf(0)]
    hbar_b = [mp.conj(x) for x in h_b]
    Yd_b = build_Y(h_b, ud_b, wd_b)
    Yu_b = build_Y(hbar_b, uu_b, wu_b)
    Ud_b, Sd_b, _ = mp.svd_c(Yd_b)
    Uu_b, Su_b, _ = mp.svd_c(Yu_b)
    V_b = Uu_b.transpose_conj() * Ud_b
    min_Vdiag_b = min(abs(V_b[k, k]) for k in range(3))
    V33_b = abs(V_b[0, 0])
    rho_u_b = Su_b[1] / Su_b[0]
    rho_d_b = Sd_b[1] / Sd_b[0]
    rho_b = max(rho_u_b, rho_d_b)
    m1m2_u_b = Su_b[2] / Su_b[1]
    m1m2_d_b = Sd_b[2] / Sd_b[1]
    Mu_b = build_M(uu_b, wu_b)
    Md_b = build_M(ud_b, wd_b)
    _, Smu_b, _ = svd2_exact(Mu_b)
    _, Smd_b, _ = svd2_exact(Md_b)
    ku_b = Smu_b[1] / Smu_b[0]
    kd_b = Smd_b[1] / Smd_b[0]
    vh_u_b, _, r1u_b = compute_vhat(build_H(hbar_b), Mu_b)
    vh_d_b, _, r1d_b = compute_vhat(build_H(h_b), Md_b)
    sL_b = spinor_sL_from_cols(r1u_b, r1d_b)
    F_b = F_three_regime(t_b, sL_b, V33_b)
    ceil_b = V33_ceiling(t_b, sL_b, rho_b)
    b1967_ok = (
        sL_b > mp_rat(9, 10)
        and min_Vdiag_b >= mp_rat(9, 10)
        and rho_u_b <= mp_rat(1, 100)
        and rho_d_b <= mp_rat(1, 100)
        and m1m2_u_b <= mp_rat(1, 2)
        and m1m2_d_b <= mp_rat(1, 2)
        and rho_b >= F_b - mp_pow10(-45)
        and V33_b <= ceil_b + mp_pow10(-45)
        and rho_u_b >= max(t_b * ku_b, abs(t_b - ku_b) / 2) - mp_pow10(-45)
        and rho_d_b >= max(t_b * kd_b, abs(t_b - kd_b) / 2) - mp_pow10(-45)
    )

    # Control 3: r = 1 (t = 1, real Higgs)
    h_r1 = [mp.mpf(1), mp.mpf(0), mp.mpf(0)]
    # Witness at r=1: h = (1, 0, 0) = (e_+ + e_-)/sqrt(2), kappa = 1/3 -> u = (e_- - (1/3) e_+)
    inv_sq2_50 = mp.mpf(1) / mp.sqrt(2)
    ep_50 = [inv_sq2_50, mp.j * inv_sq2_50, mp.mpf(0)]
    em_50 = [inv_sq2_50, -mp.j * inv_sq2_50, mp.mpf(0)]
    u_r1 = [em_50[i] - mp_rat(1, 3) * ep_50[i] for i in range(3)]
    Y_r1 = build_Y(h_r1, u_r1, mp.mpf(0))
    _, S_r1, _ = mp.svd_c(Y_r1)
    rho_r1 = S_r1[1] / S_r1[0]
    F_r1 = F_three_regime(mp.mpf(1), mp.mpf(0), mp_rat(9, 10))
    r1_ok = abs(rho_r1 - mp_rat(1, 3)) < mp_pow10(-45) and abs(F_r1 - mp_rat(1, 3)) < mp_pow10(-45)

    tol25 = mp_pow10(-25)
    all_sym = all([
        sym_nondeg_lt_1,
        sym_cross_g1_g2,
        sym_cross_S,
        sym_inverse_S,
        sym_t1_match,
        sym_F_cont1,
        sym_F_cont2,
        sym_F2_lt_sixth,
        sym_conj_H,
        sym_mobius_attain,
    ])
    all_num = all([
        n_rho_lt_sixth >= 500,
        max_conj_spinor_err < tol25,
        max_viol_sin_theta_u < tol25,
        max_viol_sin_theta_d < tol25,
        max_viol_vhat_mobius < tol25,
        max_viol_V33_ceiling < tol25,
        max_viol_F_floor < tol25,
        c1a_ok,
        b1967_ok,
        r1_ok,
    ])
    return {
        "symbolic_checks": {
            "nondeg_M_max_at_sixth_lt_1": sym_nondeg_lt_1,
            "crossing_g1_eq_g2": sym_cross_g1_g2,
            "crossing_value_S": sym_cross_S,
            "exact_inverse_rho_of_S": sym_inverse_S,
            "t1_equals_M_star_of_rho_S": sym_t1_match,
            "F_continuous_at_t1": sym_F_cont1,
            "F_continuous_at_t2": sym_F_cont2,
            "F_regime2_always_lt_sixth": sym_F2_lt_sixth,
            "conjugate_H_pauli_identity": sym_conj_H,
            "mobius_ceiling_attainment": sym_mobius_attain,
        },
        "sL_crit_9_10_1_100_exact": mp_str(sL_crit_exact, 25),
        "n_trials_total": n_trials_total,
        "n_trials_rho_lt_sixth": n_rho_lt_sixth,
        "max_conj_spinor_err": mp_sci(max_conj_spinor_err),
        "max_viol_sin_theta_u": mp_sci(max_viol_sin_theta_u),
        "max_viol_sin_theta_d": mp_sci(max_viol_sin_theta_d),
        "max_viol_vhat_mobius": mp_sci(max_viol_vhat_mobius),
        "max_viol_V33_ceiling": mp_sci(max_viol_V33_ceiling),
        "max_viol_F_floor": mp_sci(max_viol_F_floor),
        "min_slack_V33": mp_sci(min_slack_V33),
        "min_slack_F": mp_sci(min_slack_F),
        "controls": {
            "C1_A_r_1_2000": {
                "r": "1/2000",
                "s_L": mp_str(sL_c1a, 25),
                "rho_u": mp_str(rho_u_c1a, 20),
                "rho_d": mp_str(rho_d_c1a, 20),
                "V33": mp_str(V33_c1a, 20),
                "F_floor": mp_str(F_c1a, 20),
                "V33_ceiling": mp_str(ceil_c1a, 20),
                "passed": c1a_ok,
            },
            "B1967_16_rational_r_3_1000": {
                "r": "3/1000",
                "s_L": mp_str(sL_b, 25),
                "kappa_u": mp_str(ku_b, 20),
                "kappa_d": mp_str(kd_b, 20),
                "rho_u": mp_str(rho_u_b, 20),
                "rho_d": mp_str(rho_d_b, 20),
                "m1_over_m2_u": mp_str(m1m2_u_b, 20),
                "m1_over_m2_d": mp_str(m1m2_d_b, 20),
                "V33": mp_str(V33_b, 20),
                "min_diag_V": mp_str(min_Vdiag_b, 20),
                "F_floor": mp_str(F_b, 20),
                "V33_ceiling": mp_str(ceil_b, 20),
                "passed": b1967_ok,
            },
            "r_eq_1_real_higgs": {
                "r": "1",
                "rho_witness": mp_str(rho_r1, 25),
                "F_floor": mp_str(F_r1, 25),
                "passed": r1_ok,
            },
        },
        "passed": all_sym and all_num,
    }


# ============================================================================
# Disjoint Chebyshev-Lobatto Spectral Collocation Solver for Fuchsian L_2(tau)
# ============================================================================

def cheb_lobatto_matrices(N: int) -> tuple[list, mp.matrix, mp.matrix]:
    s = [-mp.cos(mp.pi * j / N) for j in range(N + 1)]
    c = [mp.mpf(2) if (j == 0 or j == N) else mp.mpf(1) for j in range(N + 1)]
    D = mp.matrix(N + 1, N + 1)
    for i in range(N + 1):
        rs = mp.mpf(0)
        for j in range(N + 1):
            if i != j:
                v = (c[i] / c[j]) * ((-1) ** (i + j)) / (s[i] - s[j])
                D[i, j] = v
                rs += v
        D[i, i] = -rs
    return s, D, D * D


def reduce_to_fundamental_domain(tau: mp.mpc) -> tuple[mp.mpc, mp.mpf]:
    """Gauss SL_2(Z) reduction: returns (tau_fd, log|c*tau + d|) so L2(tau) = L2(tau_fd) - log|c*tau + d|."""
    # Track cumulative log|c*tau + d|:
    # T^k: tau -> tau + k (c=0, d=1 -> log|1| = 0)
    # S: tau -> -1/tau (c=1, d=0 -> adds log|tau|)
    cur = tau
    log_jac = mp.mpf(0)
    half = mp_rat(1, 2)
    for _ in range(100):
        # Shift real part into [-1/2, 1/2]
        k = int(mp.floor(mp.re(cur) + half))
        if k != 0:
            cur = cur - k
        if abs(cur) >= mp.mpf(1) - mp_pow10(-30):
            break
        log_jac += mp.log(abs(cur))
        cur = -mp.mpf(1) / cur
    return cur, log_jac


def frobenius_eval_puncture(z: mp.mpc, a_coeffs: dict, c_val: mp.mpc, nmax: int) -> tuple[mp.mpc, mp.mpc, mp.mpc, mp.mpc]:
    """Exact Frobenius basis (u_log, u_log', u_0, u_0') at z near puncture 0."""
    q = {0: -c_val / 4}
    for k in range(1, nmax + 1):
        q[k] = a_coeffs[k + 1] / 4
    p = [mp.mpf(0)] * (nmax + 1)
    r = [mp.mpf(0)] * (nmax + 1)
    p[0] = mp.mpf(1)
    for m in range(1, nmax + 1):
        sp_v = sum(q[k] * p[m - 1 - k] for k in range(m))
        sr_v = sum(q[k] * r[m - 1 - k] for k in range(m))
        p[m] = -sp_v / (4 * m * m)
        r[m] = -(4 * m * p[m] + sr_v) / (4 * m * m)
    sq = mp.sqrt(z)
    lz = mp.log(z)
    z2 = z * z
    u0_s = mp.mpf(0)
    du0_s = mp.mpf(0)
    r_s = mp.mpf(0)
    dr_s = mp.mpf(0)
    zp = mp.mpf(1)
    half = mp_rat(1, 2)
    for m in range(nmax + 1):
        u0_s += p[m] * zp
        du0_s += (2 * m + half) * p[m] * zp
        r_s += r[m] * zp
        dr_s += (2 * m + half) * r[m] * zp
        zp *= z2
    u0 = sq * u0_s
    du0 = (sq / z) * du0_s
    ulog = u0 * lz + sq * r_s
    dulog = du0 * lz + u0 / z + (sq / z) * dr_s
    return ulog, dulog, u0, du0


class ChebyshevFuchsianL2Solver:
    """Genuiely disjoint Chebyshev-Lobatto spectral collocation Fuchsian L_2(tau) solver."""

    def __init__(self, N_cheb: int, n_pa: int = 4, frob_terms: int = 34) -> None:
        self.N_cheb = N_cheb
        self.n_pa = n_pa
        self.frob_terms = frob_terms
        self.s_nodes, self.D, self.D2 = cheb_lobatto_matrices(N_cheb)
        self.J = mp.matrix([[1, 0], [0, -1]])

    def _inv2(self, X: mp.matrix) -> mp.matrix:
        return mp.matrix([[X[1, 1], -X[0, 1]], [-X[1, 0], X[0, 0]]])

    def _prop(self, pre_segs: list, c_val: mp.mpc, need_deriv: bool) -> tuple[mp.matrix, mp.matrix]:
        N = self.N_cheb
        D = self.D
        D2 = self.D2
        M = mp.eye(2)
        dM = mp.zeros(2, 2)
        for dz, row in pre_segs:
            sc = (dz / 2) ** 2
            A = D2.copy()
            for j in range(N + 1):
                A[0, j] = mp.mpf(1) if j == 0 else mp.mpf(0)
                A[N, j] = D[0, j]
            for i in range(1, N):
                A[i, i] += sc * ((row[i - 1] - c_val) / 4)
            A_lu, p = mp.mp.LU_decomp(A)
            b0 = mp.matrix(N + 1, 1)
            b0[0] = mp.mpf(1)
            u0 = mp.mp.U_solve(A_lu, mp.mp.L_solve(A_lu, b0, p))
            b1 = mp.matrix(N + 1, 1)
            b1[N] = dz / 2
            u1 = mp.mp.U_solve(A_lu, mp.mp.L_solve(A_lu, b1, p))
            du0 = sum(D[N, j] * u0[j] for j in range(N + 1))
            du1 = sum(D[N, j] * u1[j] for j in range(N + 1))
            Mk = mp.matrix([[u0[N], u1[N]], [(2 / dz) * du0, (2 / dz) * du1]])
            if need_deriv:
                r0 = mp.matrix(N + 1, 1)
                r1 = mp.matrix(N + 1, 1)
                cs = sc / 4
                for i in range(1, N):
                    r0[i] = cs * u0[i]
                    r1[i] = cs * u1[i]
                v0 = mp.mp.U_solve(A_lu, mp.mp.L_solve(A_lu, r0, p))
                v1 = mp.mp.U_solve(A_lu, mp.mp.L_solve(A_lu, r1, p))
                dv0 = sum(D[N, j] * v0[j] for j in range(N + 1))
                dv1 = sum(D[N, j] * v1[j] for j in range(N + 1))
                dMk = mp.matrix([[v0[N], v1[N]], [(2 / dz) * dv0, (2 / dz) * dv1]])
                dM = dMk * M + Mk * dM
            M = Mk * M
        return M, dM

    def solve_fd(self, tau_fd: mp.mpc, c_init: mp.mpc | None = None) -> dict:
        q = mp.exp(mp.j * mp.pi * tau_fd)
        t20 = mp.jtheta(2, 0, q)
        t30 = mp.jtheta(3, 0, q)
        t40 = mp.jtheta(4, 0, q)
        e1 = (mp.pi ** 2 / 3) * (t30 ** 4 + t40 ** 4)
        e2 = (mp.pi ** 2 / 3) * (t20 ** 4 - t40 ** 4)
        e3 = -(mp.pi ** 2 / 3) * (t20 ** 4 + t30 ** 4)
        g2 = -4 * (e1 * e2 + e2 * e3 + e3 * e1)
        g3 = 4 * e1 * e2 * e3
        nmax = self.frob_terms
        a = {2: g2 / 20, 3: g3 / 28}
        for n in range(4, nmax + 2):
            a[n] = (3 * sum(a[k] * a[n - k] for k in range(2, n - 1))) / ((2 * n + 1) * (n - 3))

        z3 = (1 + tau_fd) / 2
        s_nodes = self.s_nodes
        N = self.N_cheb

        def wp(z: mp.mpc) -> mp.mpc:
            u = mp.pi * z
            return e1 + (mp.pi * t30 * t40 * mp.jtheta(2, u, q) / mp.jtheta(1, u, q)) ** 2

        def precomp(segs: list) -> list:
            return [(zb - za, [wp(za + (s_nodes[i] + 1) * (zb - za) / 2) for i in range(1, N)]) for za, zb in segs]

        # a-path: [z3, z3 + 1/2]
        dza = mp_rat(1, 2 * self.n_pa)
        segs_a = [(z3 + k * dza, z3 + (k + 1) * dza) for k in range(self.n_pa)]

        # Graded b-path: [z3, z3 + tau/2] (finer near z3 + tau/2 where dist to poles is 1/2)
        L_b = abs(tau_fd / 2)
        pts_b = [z3 + tau_fd / 2]
        cur = z3 + tau_fd / 2
        u_dir = (-tau_fd / 2) / L_b
        rem = L_b
        min_step_b = mp_rat(1, 6)
        ratio_b = mp_rat(7, 20)
        rem_cut_b = mp_rat(1, 8)
        while rem > 0:
            dist = abs(cur - (z3 + tau_fd / 2))
            step = min(rem, max(min_step_b, ratio_b * mp.sqrt(mp_rat(1, 4) + dist * dist)))
            if rem - step < rem_cut_b:
                step = rem
            cur = cur + u_dir * step
            pts_b.append(cur)
            rem -= step
        pts_b.reverse()
        segs_b = [(pts_b[k], pts_b[k + 1]) for k in range(len(pts_b) - 1)]

        pa = precomp(segs_a)
        pb = precomp(segs_b)
        J = self.J

        if c_init is None:
            y = mp.im(tau_fd)
            c = mp.mpc(-(mp.pi ** 2 / 3) * (1 - mp.exp(-mp.pi * max(mp.mpf(0), y - 1))), 0)
        else:
            c = c_init

        step_tol = mp_pow10(-(mp.mp.dps - 8))
        Ta = Tb = mp.eye(2)
        res_norm = mp.mpf(1)
        iters = 0
        for it in range(14):
            iters = it + 1
            Ap, dAp = self._prop(pa, c, True)
            Bp, dBp = self._prop(pb, c, True)
            Api = self._inv2(Ap)
            Bpi = self._inv2(Bp)
            Ta = J * Api * J * Ap
            dTa = -J * Api * dAp * Api * J * Ap + J * Api * J * dAp
            Tb = J * Bpi * J * Bp
            dTb = -J * Bpi * dBp * Bpi * J * Bp + J * Bpi * J * dBp
            Tab = Ta * Tb
            dTab = dTa * Tb + Ta * dTb
            tr_a = Ta[0, 0] + Ta[1, 1]
            tr_b = Tb[0, 0] + Tb[1, 1]
            tr_ab = Tab[0, 0] + Tab[1, 1]
            dtr_a = dTa[0, 0] + dTa[1, 1]
            dtr_b = dTb[0, 0] + dTb[1, 1]
            dtr_ab = dTab[0, 0] + dTab[1, 1]
            res = mp.matrix([mp.im(tr_a), mp.im(tr_b), mp.im(tr_ab)])
            res_norm = mp.norm(res)
            Jac = mp.matrix([
                [mp.im(dtr_a), mp.re(dtr_a)],
                [mp.im(dtr_b), mp.re(dtr_b)],
                [mp.im(dtr_ab), mp.re(dtr_ab)],
            ])
            step = mp.lu_solve(Jac.T * Jac, Jac.T * res)
            c -= mp.mpc(step[0], step[1])
            if mp.norm(step) < step_tol:
                break

        # Re-evaluate final Ta, Tb at converged c
        Ap, _ = self._prop(pa, c, False)
        Bp, _ = self._prop(pb, c, False)
        Ta = J * self._inv2(Ap) * J * Ap
        Tb = J * self._inv2(Bp) * J * Bp
        comm = Ta * Tb * self._inv2(Ta) * self._inv2(Tb)
        comm_err = abs(comm[0, 0] + comm[1, 1] + 2)

        # Graded connection path from zm (|zm| = 1/5) to z3
        zm = (1 + tau_fd) / (5 * abs(1 + tau_fd))
        pts_m = [zm]
        cur = zm
        rem = abs(z3 - zm)
        u_dir = (z3 - zm) / rem
        min_step_m = mp_rat(2, 25)
        ratio_m = mp_rat(3, 10)
        rem_cut_m = mp_rat(1, 20)
        while rem > 0:
            step = min(rem, max(min_step_m, ratio_m * abs(cur)))
            if rem - step < rem_cut_m:
                step = rem
            cur = cur + u_dir * step
            pts_m.append(cur)
            rem -= step
        segs_m = [(pts_m[k], pts_m[k + 1]) for k in range(len(pts_m) - 1)]
        pm = precomp(segs_m)
        P_m, _ = self._prop(pm, c, False)
        ulog, dulog, u0, du0 = frobenius_eval_puncture(zm, a, c, nmax=nmax)
        wron_err = abs(dulog * u0 - ulog * du0 - 1)
        C = P_m * mp.matrix([[ulog, u0], [dulog, du0]])
        Ci = C ** (-1)
        Ma = (Ci * Ta * C).T
        Mb = (Ci * Tb * C).T
        bc_a = mp.re((Ma[0, 0] - Ma[1, 1]) / (2 * Ma[1, 0]))
        bc_b = mp.re((Mb[0, 0] - Mb[1, 1]) / (2 * Mb[1, 0]))
        L2_fd = mp.pi - bc_a
        return {
            "L2": L2_fd,
            "c_star": c,
            "tr_a": Ta[0, 0] + Ta[1, 1],
            "tr_b": Tb[0, 0] + Tb[1, 1],
            "diff_ab": abs(bc_a - bc_b),
            "comm_err": comm_err,
            "wron_err": wron_err,
            "res_norm": res_norm,
            "iters": iters,
        }

    def solve(self, tau: mp.mpc, c_init: mp.mpc | None = None) -> dict:
        tau_fd, log_jac = reduce_to_fundamental_domain(tau)
        out = self.solve_fd(tau_fd, c_init=c_init)
        # L2(tau) = L2(tau_fd) - log|c*tau + d|
        out["L2"] = out["L2"] - log_jac
        return out


# ============================================================================
# Independent Frame C Channel Construction (jtheta + qp + Transposed k-Sum F_u)
# ============================================================================

def theta_c_jtheta(al: mp.mpf, be: mp.mpf, tau: mp.mpc) -> mp.mpc:
    q = mp.exp(mp.j * mp.pi * tau)
    return mp.exp(mp.j * mp.pi * al * al * tau + 2 * mp.j * mp.pi * al * be) * mp.jtheta(3, mp.pi * (al * tau + be), q)


def theta_c_lattice_sum(al: mp.mpf, be: mp.mpf, tau: mp.mpc, nlim: int = 24) -> mp.mpc:
    s = mp.mpc(0)
    for n in range(-nlim, nlim + 1):
        na = n + al
        s += mp.exp(mp.j * mp.pi * na * na * tau + 2 * mp.j * mp.pi * na * be)
    return s


def dedekind_eta_qp(tau: mp.mpc) -> mp.mpc:
    q = mp.exp(mp.j * mp.pi * tau)
    return mp.exp(mp.j * mp.pi * tau / 12) * mp.qp(q * q)


def a0_jtheta(al_r: mp.mpf, be_r: mp.mpf, tau: mp.mpc) -> mp.mpc:
    q = mp.exp(mp.j * mp.pi * tau)
    z = mp.pi * (al_r * tau + be_r)
    return 2 * mp.j * mp.pi * al_r + mp.pi * mp.jtheta(1, z, q, 1) / mp.jtheta(1, z, q)


def Fu_ksum_transposed(al_r: mp.mpf, be_r: mp.mpf, tau: mp.mpc, tol_exp: int) -> mp.mpf:
    """Transposed k-outer Fourier summation for regularized Green sum F_u (disjoint from m-outer sum)."""
    x = mp.re(tau)
    y = mp.im(tau)
    if al_r == 0:
        base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + (mp.pi ** 2 * y) / (mp.sin(mp.pi * be_r) ** 2)
        s = mp.mpf(0)
        kmax = int(mp.ceil(mp.mpf(tol_exp) / (2 * mp.pi * y))) + 2
        for k in range(1, kmax + 1):
            qp = mp.exp(2 * mp.j * mp.pi * k * tau)
            qm = mp.exp(-2 * mp.pi * k * y - 2 * mp.j * mp.pi * k * x)
            phase = mp.exp(2 * mp.j * mp.pi * k * be_r)
            s += 2 * mp.pi * mp.re(-phase * (mp.log(1 - qp) + mp.log(1 - qm)))
        return base + s
    base = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.psi(0, al_r) + mp.psi(0, 1 - al_r))
    s = mp.mpf(0)
    for a_sh, sgn_x in ((al_r, 1), (1 - al_r, -1)):
        kmax = int(mp.ceil(mp.mpf(tol_exp) / (2 * mp.pi * a_sh * y))) + 2
        for k in range(1, kmax + 1):
            z_step = mp.exp(-2 * mp.pi * k * y + 2 * mp.j * mp.pi * k * sgn_x * x)
            z_cur = mp.exp(-2 * mp.pi * k * a_sh * y + 2 * mp.j * mp.pi * k * (sgn_x * a_sh * x + be_r))
            rem_exp = mp.mpf(tol_exp) - 2 * mp.pi * k * a_sh * y
            nmax = int(mp.ceil(rem_exp / (2 * mp.pi * k * y))) + 1 if rem_exp > 0 else 0
            sub = mp.mpc(0)
            for n in range(nmax + 1):
                sub += z_cur / (n + a_sh)
                z_cur *= z_step
            s += 2 * mp.pi * mp.re(sub)
    return base + s


def Fu_msum_direct(al_r: mp.mpf, be_r: mp.mpf, tau: mp.mpc, tol_exp: int) -> mp.mpf:
    """Direct m-outer sum used solely to cross-check Fu_ksum_transposed on test points."""
    x = mp.re(tau)
    y = mp.im(tau)
    mmax = int(mp.ceil(mp.mpf(tol_exp) / (2 * mp.pi * y))) + 2
    if al_r == 0:
        base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + (mp.pi ** 2 * y) / (mp.sin(mp.pi * be_r) ** 2)
        s = mp.mpf(0)
        for m in range(1, mmax + 1):
            for sgn in (1, -1):
                wm = mp.exp(-2 * mp.pi * m * y + 2 * mp.j * mp.pi * (sgn * m * x + be_r))
                s += (2 * mp.pi / m) * mp.re(wm / (1 - wm))
        return base + s
    base = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.psi(0, al_r) + mp.psi(0, 1 - al_r))
    s = mp.mpf(0)
    for m in range(-mmax, mmax + 1):
        ma = m + al_r
        ama = abs(ma)
        wm = mp.exp(-2 * mp.pi * ama * y + 2 * mp.j * mp.pi * (ma * x + be_r))
        s += (2 * mp.pi / ama) * mp.re(wm / (1 - wm))
    return base + s


def build_E_dual_interior() -> dict:
    return {
        "1": mp.matrix([[1, 0], [0, 1]]) / 2,
        "i": mp.matrix([[-mp.j, 0], [0, mp.j]]) / 2,
        "j": mp.matrix([[0, 1], [-1, 0]]) / 2,
        "k": mp.matrix([[0, -mp.j], [-mp.j, 0]]) / 2,
    }


def eval_frame_c_sector(
    af: Fraction,
    bf: Fraction,
    tau: mp.mpc,
    L2: mp.mpf,
    eta3: mp.mpc,
    qL: int,
    qR: int,
    weighted: bool,
    tol_exp: int,
    fu_cache: dict,
    a0_cache: dict,
    E_dual: dict,
) -> tuple[mp.matrix, mp.mpf | None]:
    x0 = qL * af
    x1 = 2 * qL * bf
    y0 = qR * af
    y1 = 2 * qR * bf
    ap = x0 + y0
    am = x0 - y0
    bp = (x1 + y1) / 2
    bm = (x1 - y1) / 2
    H = Fraction(1, 2)
    e_ph = mp.exp(-2 * mp.j * mp.pi * mp_frac(x0))
    kap = {"1": -mp.j * e_ph, "i": mp.mpf(-1), "j": -e_ph, "k": mp.j}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    y_im = mp.im(tau)
    Mw = mp.zeros(2, 2)
    min_Ns = None
    for s in ("1", "i", "j", "k"):
        c0, c1 = cs[s]
        d0, d1 = ds[s]
        al_c, be_c = c0 - H, c1 - H
        al_d, be_d = d0 - H, d1 - H
        if (al_c.denominator == 1 and be_c.denominator == 1) or (al_d.denominator == 1 and be_d.denominator == 1):
            us = mp.mpf(0)
        else:
            Rs = (
                kap[s]
                * theta_c_jtheta(mp_frac(c0), mp_frac(c1), tau)
                * theta_c_jtheta(mp_frac(d0), mp_frac(d1), tau)
                / (2 * mp.pi * eta3)
            )
            if not weighted:
                us = Rs
            else:
                key = (al_c % 1, be_c % 1)
                if key not in fu_cache:
                    al_m = mp_frac(key[0])
                    be_m = mp_frac(key[1])
                    fu_cache[key] = Fu_ksum_transposed(al_m, be_m, tau, tol_exp=tol_exp)
                    a0_cache[key] = a0_jtheta(al_m, be_m, tau)
                fu = fu_cache[key]
                a0 = a0_cache[key]
                Ns = (
                    2 * mp.pi * L2
                    + fu
                    + mp.pi * mp.log(y_im)
                    - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                    - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L2)
                )
                if min_Ns is None or Ns < min_Ns:
                    min_Ns = Ns
                us = mp.sqrt(max(mp.mpf(0), Ns)) * Rs
        Mw += us * E_dual[s]
    return Mw, min_Ns


# ============================================================================
# Gates RG4 & RG5: M4-A (60 Pairs) & M4-B (2,016-Point Full Grid)
# ============================================================================

def run_M4() -> tuple[dict, dict, dict]:
    # --- Step 1: Independent L_2 & Frame C Primitive Cross-Checks (dps = 45) ---
    mp.mp.dps = 45
    solver_hi = ChebyshevFuchsianL2Solver(N_cheb=30, n_pa=5, frob_terms=38)

    # Exact benchmark 1: tau = i vs Gamma(1/4) exact formula
    L2_i_exact = mp.pi - mp.log(8 * mp.sqrt(2 * mp.pi) / (mp.gamma(mp_rat(1, 4)) ** 2))
    out_i = solver_hi.solve(mp.mpc(0, 1), c_init=mp.mpc(0, 0))
    err_L2_i = abs(out_i["L2"] - L2_i_exact)

    # Exact benchmark 2: tau = (2 + i)/5 via Gauss SL_2(Z) reduction -> L2(i) + (1/2) ln 5
    L2_2i5_exact = L2_i_exact + mp.log(5) / 2
    out_2i5 = solver_hi.solve(mp.mpc(mp_rat(2, 5), mp_rat(1, 5)), c_init=mp.mpc(0, 0))
    err_L2_2i5 = abs(out_2i5["L2"] - L2_2i5_exact)

    # Exact benchmark 3: hexagonal tau = 1/2 + i*sqrt(3)/2 -> c* = 0, tr(Ta) = tr(Tb) = 3
    out_hex = solver_hi.solve(mp.mpc(mp_rat(1, 2), mp.sqrt(3) / 2), c_init=mp.mpc(0, 0))
    err_hex_c = abs(out_hex["c_star"])
    err_hex_tr = max(abs(out_hex["tr_a"] - 3), abs(out_hex["tr_b"] - 3))

    # Cross-check Fu_ksum_transposed vs Fu_msum_direct AND theta_c_jtheta vs lattice sum
    mp.mp.dps = 40
    tau_chk = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    max_Fu_cross_err = mp.mpf(0)
    max_theta_cross_err = mp.mpf(0)
    for al_f, be_f in [
        (Fraction(0, 1), Fraction(1, 5)),
        (Fraction(2, 5), Fraction(3, 5)),
        (Fraction(1, 7), Fraction(4, 7)),
        (Fraction(3, 8), Fraction(1, 8)),
    ]:
        al_m, be_m = mp_frac(al_f), mp_frac(be_f)
        max_Fu_cross_err = max(
            max_Fu_cross_err,
            abs(Fu_ksum_transposed(al_m, be_m, tau_chk, 105) - Fu_msum_direct(al_m, be_m, tau_chk, 105)),
        )
        max_theta_cross_err = max(
            max_theta_cross_err,
            abs(theta_c_jtheta(al_m, be_m, tau_chk) - theta_c_lattice_sum(al_m, be_m, tau_chk, 22)),
        )

    # --- Step 2: Solve L_2(tau) across all 28 (x, y) grid points ---
    x_cols = [Fraction(0, 1), Fraction(13, 100), Fraction(1, 4), Fraction(1, 2)]
    y_heights = [
        Fraction(1, 1),
        Fraction(3, 2),
        Fraction(2, 1),
        Fraction(3, 1),
        Fraction(4, 1),
        Fraction(6, 1),
        Fraction(10, 1),
    ]

    # Solve high-precision L_2 for M4-A points (x=13/100, y in {2, 6}) at dps = 45, N_cheb = 30
    mp.mp.dps = 45
    L2_table_hi = {}
    L2_diagnostics = {}
    for yf in (Fraction(2, 1), Fraction(6, 1)):
        xf = Fraction(13, 100)
        tau = mp.mpc(mp_frac(xf), mp_frac(yf))
        out = solver_hi.solve(tau)
        L2_table_hi[(xf, yf)] = out["L2"]
        L2_diagnostics[f"hi_{frac_str(xf)}_{frac_str(yf)}"] = {
            "L2": mp_str(out["L2"], 35),
            "diff_ab": mp_sci(out["diff_ab"]),
            "comm_err": mp_sci(out["comm_err"]),
            "wron_err": mp_sci(out["wron_err"]),
            "iters": out["iters"],
        }

    # Solve all 28 grid tau values at dps = 38, N_cheb = 26 with smooth y-continuation per column
    mp.mp.dps = 38
    solver_grid = ChebyshevFuchsianL2Solver(N_cheb=26, n_pa=4, frob_terms=34)
    L2_table_28 = {}
    max_L2_dab = mp.mpf(0)
    max_L2_comm = mp.mpf(0)
    max_L2_wron = mp.mpf(0)
    max_L2_hi_vs_grid = mp.mpf(0)

    for xf in x_cols:
        c_prev = mp.mpc(0, 0)
        for yf in y_heights:
            tau = mp.mpc(mp_frac(xf), mp_frac(yf))
            out = solver_grid.solve(tau, c_init=c_prev)
            c_prev = out["c_star"]
            L2_table_28[(xf, yf)] = out["L2"]
            max_L2_dab = max(max_L2_dab, out["diff_ab"])
            max_L2_comm = max(max_L2_comm, out["comm_err"])
            max_L2_wron = max(max_L2_wron, out["wron_err"])
            if (xf, yf) in L2_table_hi:
                max_L2_hi_vs_grid = max(max_L2_hi_vs_grid, abs(out["L2"] - L2_table_hi[(xf, yf)]))
            L2_diagnostics[f"{frac_str(xf)}_{frac_str(yf)}"] = {
                "L2": mp_str(out["L2"], 28),
                "diff_ab": mp_sci(out["diff_ab"]),
                "comm_err": mp_sci(out["comm_err"]),
                "iters": out["iters"],
            }

    # --- Step 3: M4-A (B1973 30 points x 2 heights = 60 pairs at dps = 38) ---
    mp.mp.dps = 38
    E_dual = build_E_dual_interior()
    pts_ord5 = [(Fraction(i, 5), Fraction(j, 5)) for i in range(5) for j in range(5) if not (i == 0 and j == 0)]
    pts_mixed6 = [
        (Fraction(1, 7), Fraction(3, 7)),
        (Fraction(2, 7), Fraction(1, 7)),
        (Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 4), Fraction(3, 4)),
        (Fraction(1, 6), Fraction(1, 6)),
        (Fraction(3, 8), Fraction(1, 8)),
    ]
    pts_30 = pts_ord5 + pts_mixed6

    rho_bar = mp_rat(1, 100)
    a_bar = mp_rat(9, 10)
    sL_bar = mp_rat(39, 100)
    V33_bar = mp_rat(78, 100)
    rho_floor_bar = mp_rat(24, 1000)

    m4a_pairs = []
    m4a_max_sL_res = mp.mpf(0)
    m4a_max_sv2_res = mp.mpf(0)
    m4a_max_sL = mp.mpf(0)
    m4a_max_V33_ceil = mp.mpf(0)
    m4a_min_rho_floor = mp.mpf(1)
    m4a_min_Ns = mp.mpf(1000)
    m4a_max_ku = mp.mpf(0)
    m4a_max_kd = mp.mpf(0)
    m4a_failed = 0

    for yf in (Fraction(2, 1), Fraction(6, 1)):
        xf = Fraction(13, 100)
        tau = mp.mpc(mp_frac(xf), mp_frac(yf))
        L2 = L2_table_hi[(xf, yf)]
        eta3 = dedekind_eta_qp(tau) ** 3
        fu_cache: dict = {}
        a0_cache: dict = {}
        for af, bf in pts_30:
            Mur, _ = eval_frame_c_sector(af, bf, tau, L2, eta3, 1, -4, False, 100, fu_cache, a0_cache, E_dual)
            Mdr, _ = eval_frame_c_sector(af, bf, tau, L2, eta3, 1, 2, False, 100, fu_cache, a0_cache, E_dual)
            Uur, Sur, _ = svd2_exact(Mur)
            Udr, Sdr, _ = svd2_exact(Mdr)
            sL_r = spinor_sL_from_cols([Uur[0, 0], Uur[1, 0]], [Udr[0, 0], Udr[1, 0]])
            sv2_u_r = Sur[1] / Sur[0]
            sv2_d_r = Sdr[1] / Sdr[0]

            Mu, min_Ns_u = eval_frame_c_sector(af, bf, tau, L2, eta3, 1, -4, True, 100, fu_cache, a0_cache, E_dual)
            Md, min_Ns_d = eval_frame_c_sector(af, bf, tau, L2, eta3, 1, 2, True, 100, fu_cache, a0_cache, E_dual)
            Uu, Su, _ = svd2_exact(Mu)
            Ud, Sd, _ = svd2_exact(Md)
            sL_w = spinor_sL_from_cols([Uu[0, 0], Uu[1, 0]], [Ud[0, 0], Ud[1, 0]])
            ku = Su[1] / Su[0]
            kd = Sd[1] / Sd[0]
            v33_c = V33_ceiling(mp.mpf(0), sL_w, rho_bar)
            rho_f = F_three_regime(mp.mpf(0), sL_w, a_bar)

            m4a_max_sL_res = max(m4a_max_sL_res, sL_r)
            m4a_max_sv2_res = max(m4a_max_sv2_res, sv2_u_r, sv2_d_r)
            m4a_max_sL = max(m4a_max_sL, sL_w)
            m4a_max_V33_ceil = max(m4a_max_V33_ceil, v33_c)
            m4a_min_rho_floor = min(m4a_min_rho_floor, rho_f)
            m4a_max_ku = max(m4a_max_ku, ku)
            m4a_max_kd = max(m4a_max_kd, kd)
            if min_Ns_u is not None:
                m4a_min_Ns = min(m4a_min_Ns, min_Ns_u)
            if min_Ns_d is not None:
                m4a_min_Ns = min(m4a_min_Ns, min_Ns_d)

            pt_ok = (
                sL_r < mp_pow10(-25)
                and sv2_u_r < mp_pow10(-25)
                and sv2_d_r < mp_pow10(-25)
                and sL_w < sL_bar
                and v33_c < V33_bar
                and rho_f > rho_floor_bar
            )
            if not pt_ok:
                m4a_failed += 1
            m4a_pairs.append({
                "y": frac_str(yf),
                "a": frac_str(af),
                "b": frac_str(bf),
                "sL_res": mp_sci(sL_r, 8),
                "sv2_u_res": mp_sci(sv2_u_r, 8),
                "sv2_d_res": mp_sci(sv2_d_r, 8),
                "sL": mp_str(sL_w, 22),
                "kappa_u": mp_str(ku, 20),
                "kappa_d": mp_str(kd, 20),
                "V33_ceiling_rho_1e2": mp_str(v33_c, 20),
                "rho_floor_a_9e1": mp_str(rho_f, 20),
            })

    m4a_passed = (
        len(m4a_pairs) == 60
        and m4a_failed == 0
        and m4a_max_sL_res < mp_pow10(-25)
        and m4a_max_sv2_res < mp_pow10(-25)
        and m4a_max_sL < sL_bar
        and m4a_max_V33_ceil < V33_bar
        and m4a_min_rho_floor > rho_floor_bar
        and m4a_min_Ns > 0
    )

    m4a_res = {
        "dps": 38,
        "n_pairs": len(m4a_pairs),
        "n_failed": m4a_failed,
        "max_sL_res": mp_sci(m4a_max_sL_res),
        "max_sv2_over_sv1_res": mp_sci(m4a_max_sv2_res),
        "max_sL_weighted": mp_str(m4a_max_sL, 25),
        "max_kappa_u": mp_str(m4a_max_ku, 22),
        "max_kappa_d": mp_str(m4a_max_kd, 22),
        "max_V33_ceiling_at_rho_1e2": mp_str(m4a_max_V33_ceil, 25),
        "min_rho_floor_at_a_9e1": mp_str(m4a_min_rho_floor, 25),
        "min_Ns_active": mp_str(m4a_min_Ns, 20),
        "pairs": m4a_pairs,
        "passed": m4a_passed,
    }

    # --- Step 4: M4-B (B1968 Full 2,016-Point Grid at dps = 30) ---
    mp.mp.dps = 30
    E_dual_30 = build_E_dual_interior()
    pts_ord7 = [(Fraction(i, 7), Fraction(j, 7)) for i in range(7) for j in range(7) if not (i == 0 and j == 0)]
    pts_72 = pts_ord5 + pts_ord7

    total_pts = 0
    failed_pts = 0
    global_max_sL = mp.mpf(0)
    global_argmax = {}
    global_max_V33_ceil = mp.mpf(0)
    global_min_rho_floor = mp.mpf(1)
    global_max_ku = mp.mpf(0)
    global_max_kd = mp.mpf(0)
    global_min_Ns = mp.mpf(1000)

    per_height: dict = {}
    per_column: dict = {}
    for yf in y_heights:
        per_height[frac_str(yf)] = {
            "n_points": 0,
            "n_failed": 0,
            "max_sL": mp.mpf(0),
            "max_V33_ceiling": mp.mpf(0),
            "min_rho_floor": mp.mpf(1),
            "argmax": {},
        }
    for xf in x_cols:
        per_column[frac_str(xf)] = {
            "n_points": 0,
            "n_failed": 0,
            "max_sL": mp.mpf(0),
            "max_V33_ceiling": mp.mpf(0),
            "min_rho_floor": mp.mpf(1),
        }

    for xf in x_cols:
        xk = frac_str(xf)
        for yf in y_heights:
            yk = frac_str(yf)
            tau = mp.mpc(mp_frac(xf), mp_frac(yf))
            L2 = L2_table_28[(xf, yf)]
            eta3 = dedekind_eta_qp(tau) ** 3
            fu_cache_g: dict = {}
            a0_cache_g: dict = {}
            for af, bf in pts_72:
                Mu, min_Ns_u = eval_frame_c_sector(af, bf, tau, L2, eta3, 1, -4, True, 80, fu_cache_g, a0_cache_g, E_dual_30)
                Md, min_Ns_d = eval_frame_c_sector(af, bf, tau, L2, eta3, 1, 2, True, 80, fu_cache_g, a0_cache_g, E_dual_30)
                Uu, Su, _ = svd2_exact(Mu)
                Ud, Sd, _ = svd2_exact(Md)
                sL_w = spinor_sL_from_cols([Uu[0, 0], Uu[1, 0]], [Ud[0, 0], Ud[1, 0]])
                ku = Su[1] / Su[0]
                kd = Sd[1] / Sd[0]
                v33_c = V33_ceiling(mp.mpf(0), sL_w, rho_bar)
                rho_f = F_three_regime(mp.mpf(0), sL_w, a_bar)

                total_pts += 1
                global_max_ku = max(global_max_ku, ku)
                global_max_kd = max(global_max_kd, kd)
                if min_Ns_u is not None:
                    global_min_Ns = min(global_min_Ns, min_Ns_u)
                if min_Ns_d is not None:
                    global_min_Ns = min(global_min_Ns, min_Ns_d)

                pt_ok = (sL_w < sL_bar) and (v33_c < V33_bar) and (rho_f > rho_floor_bar)
                if not pt_ok:
                    failed_pts += 1

                if sL_w > global_max_sL:
                    global_max_sL = sL_w
                    global_argmax = {"x": xk, "y": yk, "a": frac_str(af), "b": frac_str(bf)}
                global_max_V33_ceil = max(global_max_V33_ceil, v33_c)
                global_min_rho_floor = min(global_min_rho_floor, rho_f)

                ph = per_height[yk]
                ph["n_points"] += 1
                if not pt_ok:
                    ph["n_failed"] += 1
                if sL_w > ph["max_sL"]:
                    ph["max_sL"] = sL_w
                    ph["argmax"] = {"x": xk, "a": frac_str(af), "b": frac_str(bf)}
                ph["max_V33_ceiling"] = max(ph["max_V33_ceiling"], v33_c)
                ph["min_rho_floor"] = min(ph["min_rho_floor"], rho_f)

                pc = per_column[xk]
                pc["n_points"] += 1
                if not pt_ok:
                    pc["n_failed"] += 1
                pc["max_sL"] = max(pc["max_sL"], sL_w)
                pc["max_V33_ceiling"] = max(pc["max_V33_ceiling"], v33_c)
                pc["min_rho_floor"] = min(pc["min_rho_floor"], rho_f)

    # Format per_height_summary and per_column_summary with string decimals
    per_height_out = {}
    for yf in y_heights:
        yk = frac_str(yf)
        ph = per_height[yk]
        per_height_out[yk] = {
            "n_points": ph["n_points"],
            "n_failed": ph["n_failed"],
            "max_sL": mp_str(ph["max_sL"], 22),
            "max_V33_ceiling_at_rho_1e2": mp_str(ph["max_V33_ceiling"], 22),
            "min_rho_floor_at_a_9e1": mp_str(ph["min_rho_floor"], 22),
            "argmax": ph["argmax"],
        }
    per_column_out = {}
    for xf in x_cols:
        xk = frac_str(xf)
        pc = per_column[xk]
        per_column_out[xk] = {
            "n_points": pc["n_points"],
            "n_failed": pc["n_failed"],
            "max_sL": mp_str(pc["max_sL"], 22),
            "max_V33_ceiling_at_rho_1e2": mp_str(pc["max_V33_ceiling"], 22),
            "min_rho_floor_at_a_9e1": mp_str(pc["min_rho_floor"], 22),
        }

    # Compute global_r_curve across r in [0, 1] at global_max_sL
    r_curve_pts = [
        Fraction(0, 1),
        Fraction(1, 10000),
        Fraction(1, 2000),
        Fraction(1, 1000),
        Fraction(3, 1000),
        Fraction(1, 100),
        Fraction(1, 50),
        Fraction(1, 20),
        Fraction(1, 10),
        Fraction(1, 5),
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(9, 10),
        Fraction(99, 100),
        Fraction(1, 1),
    ]
    global_r_curve = []
    for rf in r_curve_pts:
        rm = mp_frac(rf)
        tm = reality_to_t(rm)
        f_val = F_three_regime(tm, global_max_sL, a_bar)
        v_ceil = V33_ceiling(tm, global_max_sL, rho_bar)
        univ_f = (tm * tm) / (1 + 2 * tm)
        global_r_curve.append({
            "r": frac_str(rf),
            "t": mp_str(tm, 22),
            "rho_floor_a_9e1": mp_str(f_val, 22),
            "V33_ceiling_rho_1e2": mp_str(v_ceil, 22),
            "universal_reality_floor": mp_str(univ_f, 22),
        })

    l2_bench_passed = (
        err_L2_i < mp_pow10(-25)
        and err_L2_2i5 < mp_pow10(-25)
        and err_hex_c < mp_pow10(-20)
        and err_hex_tr < mp_pow10(-20)
        and max_Fu_cross_err < mp_pow10(-30)
        and max_theta_cross_err < mp_pow10(-30)
        and max_L2_dab < mp_pow10(-18)
        and max_L2_comm < mp_pow10(-18)
        and max_L2_wron < mp_pow10(-30)
        and max_L2_hi_vs_grid < mp_pow10(-22)
    )

    m4b_passed = (
        total_pts == 2016
        and failed_pts == 0
        and global_max_sL < sL_bar
        and global_max_V33_ceil < V33_bar
        and global_min_rho_floor > rho_floor_bar
        and global_min_Ns > 0
        and l2_bench_passed
    )

    m4b_res = {
        "dps": 30,
        "n_points": total_pts,
        "n_failed": failed_pts,
        "global_max_sL": mp_str(global_max_sL, 25),
        "global_argmax": global_argmax,
        "global_max_kappa_u": mp_str(global_max_ku, 22),
        "global_max_kappa_d": mp_str(global_max_kd, 22),
        "global_max_V33_ceiling_at_rho_1e2": mp_str(global_max_V33_ceil, 25),
        "global_min_rho_floor_at_a_9e1": mp_str(global_min_rho_floor, 25),
        "global_min_Ns_active": mp_str(global_min_Ns, 20),
        "per_height_summary": per_height_out,
        "per_column_summary": per_column_out,
        "global_r_curve": global_r_curve,
        "l2_and_primitive_checks": {
            "err_L2_i_vs_gamma14": mp_sci(err_L2_i),
            "err_L2_2i5_sl2z": mp_sci(err_L2_2i5),
            "err_hex_c_star": mp_sci(err_hex_c),
            "err_hex_traces_3": mp_sci(err_hex_tr),
            "max_Fu_ksum_vs_msum": mp_sci(max_Fu_cross_err),
            "max_theta_jtheta_vs_sum": mp_sci(max_theta_cross_err),
            "max_L2_diff_ab_28pts": mp_sci(max_L2_dab),
            "max_L2_comm_err_28pts": mp_sci(max_L2_comm),
            "max_L2_wron_err_28pts": mp_sci(max_L2_wron),
            "max_L2_hi_vs_grid": mp_sci(max_L2_hi_vs_grid),
            "passed": l2_bench_passed,
        },
        "L2_table_28": L2_diagnostics,
        "passed": m4b_passed,
    }

    # Return L2_table_hi for Guardrail 3 and RPF3 reuse
    return m4a_res, m4b_res, {"L2_13_100_2": L2_table_hi[(Fraction(13, 100), Fraction(2, 1))]}


# ============================================================================
# Gate RG6: Guardrail 3 — 10 Random Haar U(3)_Q x U(3)_u x U(3)_d Scramblings
# ============================================================================

def run_G6_haar_scrambling(L2_ref: mp.mpf) -> dict:
    mp.mp.dps = 38
    prng = Sha256Prng("referee-G6-haar-v1")
    E_dual = build_E_dual_interior()

    # Case 1: Frame C at tau = 13/100 + 2i, (a, b) = (1/5, 2/5), interior h with r = 1/10
    tau = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    eta3 = dedekind_eta_qp(tau) ** 3
    fc: dict = {}
    ac: dict = {}
    Mwu, _ = eval_frame_c_sector(Fraction(1, 5), Fraction(2, 5), tau, L2_ref, eta3, 1, -4, True, 100, fc, ac, E_dual)
    Mwd, _ = eval_frame_c_sector(Fraction(1, 5), Fraction(2, 5), tau, L2_ref, eta3, 1, 2, True, 100, fc, ac, E_dual)
    uu_fc, wu_fc = extract_uw_from_Mw(Mwu)
    ud_fc, wd_fc = extract_uw_from_Mw(Mwd)
    h_fc = build_h_with_t(prng, reality_to_t(mp_rat(1, 10)))
    Yu_fc = build_Y([mp.conj(x) for x in h_fc], uu_fc, wu_fc)
    Yd_fc = build_Y(h_fc, ud_fc, wd_fc)

    # Case 2: B1967 16-rational control at r = 3/1000
    uu_b = [
        mp.mpc(mp_rat(8112623, 23657898), mp_rat(29517392, 42170071)),
        mp.mpc(mp_rat(-32191861, 58976063), mp_rat(10109002, 39589433)),
        mp.mpc(mp_rat(8361869, 35299624), mp_rat(201121, 6549724)),
    ]
    wu_b = mp.mpc(mp_rat(32621059, 80596130), mp_rat(-2122066, 7900781))
    ud_b = [
        mp.mpc(mp_rat(8253345, 14846974), mp_rat(32273371, 84797632)),
        mp.mpc(mp_rat(13917810, 48354631), mp_rat(-69799368, 69016585)),
        mp.mpc(mp_rat(29492199, 87199192), mp_rat(-23893336, 16802917)),
    ]
    wd_b = mp.mpc(mp_rat(126906246, 75918835), mp_rat(16923861, 50797165))
    r_b = mp_rat(3, 1000)
    h_b = [mp.sqrt((1 + r_b) / 2), mp.j * mp.sqrt((1 - r_b) / 2), mp.mpf(0)]
    Yu_b = build_Y([mp.conj(x) for x in h_b], uu_b, wu_b)
    Yd_b = build_Y(h_b, ud_b, wd_b)

    max_sv_drift = mp.mpf(0)
    max_rho_drift = mp.mpf(0)
    max_V_drift = mp.mpf(0)
    max_unitarity_err = mp.mpf(0)

    for Yu, Yd in ((Yu_fc, Yd_fc), (Yu_b, Yd_b)):
        Uu0, Su0, _ = mp.svd_c(Yu)
        Ud0, Sd0, _ = mp.svd_c(Yd)
        V0 = Uu0.transpose_conj() * Ud0
        rho_u0 = Su0[1] / Su0[0]
        rho_d0 = Sd0[1] / Sd0[0]
        for _ in range(10):
            UQ = prng.haar_unitary(3)
            UuR = prng.haar_unitary(3)
            UdR = prng.haar_unitary(3)
            for Umat in (UQ, UuR, UdR):
                max_unitarity_err = max(max_unitarity_err, frob_norm(Umat.transpose_conj() * Umat - mp.eye(3)))
            Yup = UQ * Yu * UuR.transpose_conj()
            Ydp = UQ * Yd * UdR.transpose_conj()
            Uup, Sup, _ = mp.svd_c(Yup)
            Udp, Sdp, _ = mp.svd_c(Ydp)
            Vp = Uup.transpose_conj() * Udp
            for k in range(3):
                max_sv_drift = max(max_sv_drift, abs(Sup[k] - Su0[k]), abs(Sdp[k] - Sd0[k]))
            max_rho_drift = max(max_rho_drift, abs(Sup[1] / Sup[0] - rho_u0), abs(Sdp[1] / Sdp[0] - rho_d0))
            for i in range(3):
                for j in range(3):
                    max_V_drift = max(max_V_drift, abs(abs(Vp[i, j]) - abs(V0[i, j])))

    tol30 = mp_pow10(-30)
    passed = (
        max_unitarity_err < tol30
        and max_sv_drift < tol30
        and max_rho_drift < tol30
        and max_V_drift < tol30
    )
    return {
        "dps": 38,
        "n_cases": 2,
        "n_haar_trials_per_case": 10,
        "max_unitarity_err": mp_sci(max_unitarity_err),
        "max_sv_drift": mp_sci(max_sv_drift),
        "max_rho_drift": mp_sci(max_rho_drift),
        "max_V_ckm_drift": mp_sci(max_V_drift),
        "passed": passed,
    }


# ============================================================================
# Gate RG7: Six Independent Referee Planted Faults (RPF1-RPF6)
# ============================================================================

def run_G7_planted_faults(L2_ref: mp.mpf) -> dict:
    mp.mp.dps = 35
    prng = Sha256Prng("referee-G7-rpf-v1")
    _, s1, s2, s3 = pauli_matrices()
    sigs = [s1, s2, s3]

    # RPF1: Corrupt M sign (-iw -> +iw) breaks M1.1 Kronecker trace identity
    h = [prng.complex_normal() for _ in range(3)]
    u = [prng.complex_normal() for _ in range(3)]
    wv = mp.mpc(1, mp_rat(1, 2))
    Hm = build_H(h)
    M_bad = build_M(u, wv, sign_w=+1)
    Y_true = build_Y(h, u, wv)
    Y_bad_tr = mp.matrix(3, 3)
    for a in range(3):
        for b in range(3):
            P = sigs[a] * Hm * sigs[b] * M_bad
            Y_bad_tr[a, b] = (P[0, 0] + P[1, 1]) / 2
    rpf1_err = frob_norm(Y_true - Y_bad_tr)
    rpf1_caught = rpf1_err > mp_rat(1, 10)

    # RPF2: Wrong floor t/2 at canonical witness kappa = t/(1 + 2t) for r = 1/2
    t_r2 = reality_to_t(mp_rat(1, 2))
    k_opt_r2 = t_r2 / (1 + 2 * t_r2)
    inv_sq2 = mp.mpf(1) / mp.sqrt(2)
    ep = [inv_sq2, mp.j * inv_sq2, mp.mpf(0)]
    em = [inv_sq2, -mp.j * inv_sq2, mp.mpf(0)]
    hw = [em[i] + t_r2 * ep[i] for i in range(3)]
    uw = [em[i] - k_opt_r2 * ep[i] for i in range(3)]
    _, Sw, _ = mp.svd_c(build_Y(hw, uw, mp.mpf(0)))
    rho_wit = Sw[1] / Sw[0]
    false_floor = t_r2 / 2
    rpf2_violation = false_floor - rho_wit
    rpf2_caught = rpf2_violation > mp_rat(1, 50)

    # RPF3: Break shared q_L between up and down (q_L_up = 2 vs q_L_down = 1) -> breaks s_L^res = 0
    tau = mp.mpc(mp_rat(13, 100), mp.mpf(2))
    eta3 = dedekind_eta_qp(tau) ** 3
    E_dual = build_E_dual_interior()
    Mu_bad_r, _ = eval_frame_c_sector(Fraction(1, 5), Fraction(2, 5), tau, L2_ref, eta3, 2, -4, False, 90, {}, {}, E_dual)
    Md_ok_r, _ = eval_frame_c_sector(Fraction(1, 5), Fraction(2, 5), tau, L2_ref, eta3, 1, 2, False, 90, {}, {}, E_dual)
    Uu_br, _, _ = svd2_exact(Mu_bad_r)
    Ud_or, _, _ = svd2_exact(Md_ok_r)
    rpf3_sL_res = spinor_sL_from_cols([Uu_br[0, 0], Uu_br[1, 0]], [Ud_or[0, 0], Ud_or[1, 0]])
    rpf3_caught = rpf3_sL_res > mp_rat(1, 100)

    # RPF4: Dropping factor 2 in 2*arcsin(S_t) fails exact two-sector CP^2 geodesic witness
    # Take s_L = 0 -> arccos((1+s_L)/(3-s_L)) = arccos(1/3). Let rho = 1/100 -> delta = arcsin(S_0(1/100)).
    # Place v_hat_u = (1, 0, 0), v_hat_d = (1/3, sqrt(8)/3, 0) (exact angle alpha = arccos(1/3)).
    # Tilt u_{3,u} toward v_hat_d by delta and u_{3,d} toward v_hat_u by delta:
    # Both obey sin theta(u_{3,f}, v_hat_f) = S_0(rho) EXACTLY, and angle(u_{3,u}, u_{3,d}) = alpha - 2*delta!
    al_0 = mp.acos(mp_rat(1, 3))
    S_0 = S_t_bound(mp.mpf(0), mp_rat(1, 100))
    delta = mp.asin(S_0)
    u3u_w = [mp.cos(delta), mp.sin(delta), mp.mpf(0)]
    u3d_w = [mp.cos(al_0 - delta), mp.sin(al_0 - delta), mp.mpf(0)]
    v33_wit = abs(vec_ip(u3u_w, u3d_w))
    false_ceil_no2 = mp.cos(al_0 - delta)
    true_ceil_with2 = mp.cos(al_0 - 2 * delta)
    rpf4_excess = v33_wit - false_ceil_no2
    rpf4_caught = (rpf4_excess > mp_rat(1, 10)) and (abs(v33_wit - true_ceil_with2) < mp_pow10(-30))

    # RPF5: Break shared U_Q in Haar scrambling (U_{Q,u} != U_{Q,d}) -> |V_CKM| drifts > 1/10
    h_5 = build_h_with_t(prng, mp_rat(1, 10))
    _, uu_5, wu_5 = build_M_with_kappa(prng, mp_rat(1, 5))
    _, ud_5, wd_5 = build_M_with_kappa(prng, mp_rat(1, 4))
    Yu_5 = build_Y([mp.conj(x) for x in h_5], uu_5, wu_5)
    Yd_5 = build_Y(h_5, ud_5, wd_5)
    Uu0, _, _ = mp.svd_c(Yu_5)
    Ud0, _, _ = mp.svd_c(Yd_5)
    V0 = Uu0.transpose_conj() * Ud0
    UQu = prng.haar_unitary(3)
    UQd = prng.haar_unitary(3)
    Uup, _, _ = mp.svd_c(UQu * Yu_5)
    Udp, _, _ = mp.svd_c(UQd * Yd_5)
    Vp = Uup.transpose_conj() * Udp
    rpf5_drift = max(abs(abs(Vp[i, j]) - abs(V0[i, j])) for i in range(3) for j in range(3))
    rpf5_caught = rpf5_drift > mp_rat(1, 10)

    # RPF6: Drop conjugate hbar -> h in Y_u with collinear rank-1 s_L = 0 channels at r = 0
    # Both sectors read h -> Y_u = Y_d -> |V33| = 1 with rho = 0, violating M3's 1/3 ceiling!
    h_null = [mp.mpf(1) / mp.sqrt(2), mp.j / mp.sqrt(2), mp.mpf(0)]
    # Rank-1 channel M = [[1, 0], [0, 0]] -> u = (0, 0, 1/2), w = i/2
    u_rk1 = [mp.mpf(0), mp.mpf(0), mp_rat(1, 2)]
    w_rk1 = mp.j * mp_rat(1, 2)
    Yd_6 = build_Y(h_null, u_rk1, w_rk1)
    Yu_6_noconj = build_Y(h_null, u_rk1, w_rk1)
    Ud_6, Sd_6, _ = mp.svd_c(Yd_6)
    Uu_6, Su_6, _ = mp.svd_c(Yu_6_noconj)
    V33_noconj = abs(vec_ip([Uu_6[i, 0] for i in range(3)], [Ud_6[i, 0] for i in range(3)]))
    rho_noconj = max(Su_6[1] / Su_6[0], Sd_6[1] / Sd_6[0])
    rpf6_excess = V33_noconj - mp_rat(1, 3)
    rpf6_caught = (rpf6_excess > mp_rat(1, 2)) and (rho_noconj < mp_pow10(-30))

    all_caught = all([rpf1_caught, rpf2_caught, rpf3_caught, rpf4_caught, rpf5_caught, rpf6_caught])
    return {
        "RPF1_M_sign_flip": {"residual_norm": mp_sci(rpf1_err), "caught": rpf1_caught},
        "RPF2_naive_t_half_floor": {"violation": mp_sci(rpf2_violation), "caught": rpf2_caught},
        "RPF3_broken_shared_qL": {"sL_res": mp_sci(rpf3_sL_res), "caught": rpf3_caught},
        "RPF4_dropped_factor2_in_2arcsin": {"V33_excess_over_false_ceil": mp_sci(rpf4_excess), "caught": rpf4_caught},
        "RPF5_unequal_UQ_scrambling": {"max_V_ckm_drift": mp_sci(rpf5_drift), "caught": rpf5_caught},
        "RPF6_dropped_h_conjugate": {"V33_noconj": mp_str(V33_noconj, 15), "rho_noconj": mp_sci(rho_noconj), "excess_over_third": mp_sci(rpf6_excess), "caught": rpf6_caught},
        "all_caught": all_caught,
        "passed": all_caught,
    }


# ============================================================================
# Main Driver
# ============================================================================

def main() -> int:
    t_start = time.perf_counter_ns()
    script_path = Path(__file__).resolve()
    out_path = script_path.parent / "referee_a2_p879_interior_run2_results.json"

    g0 = audit_script_ast(script_path)
    g1 = run_M1()
    g2 = run_M2()
    g3 = run_M3()
    g4, g5, ctx_m4 = run_M4()
    g6 = run_G6_haar_scrambling(ctx_m4["L2_13_100_2"])
    g7 = run_G7_planted_faults(ctx_m4["L2_13_100_2"])

    t_end = time.perf_counter_ns()
    elapsed_ms = int((t_end - t_start) // 1000000)

    gates = {
        "RG0_ast_firewall": g0["passed"],
        "RG1_M1_kronecker_unitary_bell": g1["passed"],
        "RG2_M2_bell_split_and_witness": g2["passed"],
        "RG3_M3_twosector_and_controls": g3["passed"],
        "RG4_M4A_b1973_60pairs": g4["passed"],
        "RG5_M4B_b1968_2016grid": g5["passed"],
        "RG6_guardrail3_haar_scrambling": g6["passed"],
        "RG7_planted_faults_RPF1_RPF6": g7["passed"],
    }

    result = {
        "card": "A2-P879-INTERIOR",
        "role": "disjoint-cold-room-zero-trust-referee",
        "script": "relays/a2_p879_interior_referee/referee_a2_p879_interior_run2.py",
        "empirical_inputs": "0 of 19",
        "elapsed_ms": elapsed_ms,
        "gate_summary": gates,
        "all_referee_gates_passed": all(gates.values()),
        "RG0": g0,
        "RG1_M1": g1,
        "RG2_M2": g2,
        "RG3_M3": g3,
        "RG4_M4A": g4,
        "RG5_M4B": g5,
        "RG6_Guardrail3": g6,
        "RG7_PlantedFaults": g7,
    }

    # Verify zero JSON float tokens before writing
    json_text = json.dumps(result, indent=2, sort_keys=False)
    parsed = json.loads(json_text)
    json_float_count = count_json_floats(parsed)
    result["json_float_token_count"] = json_float_count
    if json_float_count != 0:
        result["gate_summary"]["RG0_ast_firewall"] = False
        result["all_referee_gates_passed"] = False

    out_path.write_text(json.dumps(result, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    # Print ONLY a compact sealed-custody summary (do NOT dump JSON contents to stdout!)
    print(f"SEALED_WRITE_OK path={out_path.name} bytes={out_path.stat().st_size} elapsed_ms={elapsed_ms} json_floats={json_float_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
