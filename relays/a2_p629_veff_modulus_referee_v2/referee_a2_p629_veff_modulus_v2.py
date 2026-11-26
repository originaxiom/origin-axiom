#!/usr/bin/env python3
"""
100% Blind Disjoint Cold-Room Zero-Trust Referee v2
Card: AGY-002_A2-P629-VEFF-MODULUS (Strictly 0 of 19, zero empirical numbers)

Disjoint Algorithms Implemented (Guardrails 1-6):
  - RP1: Dedekind eta via Euler's pentagonal number theorem; E2 via exact
    logarithmic derivative 1 + 24 q P'(q)/P(q); E(tau, s) via Chowla-Selberg
    cross-checked against direct N=45 square-box lattice sum; exact Fraction
    proof + lattice check of -15/16; Kronecker first limit; FILQ (1990) n=1..3.
  - RP2: wp(z)/4 via exact Jacobi theta_1 logarithmic derivative; Fuchsian
    L2(tau) via explicit 6th-order Yoshida-Suzuki (15-stage) symplectic
    splitting + exact variational Newton + Frobenius matching + Vandermonde
    extrapolation + FD cocycle; real-split 6x6 symmetric mp.eigsy for all
    eigenvalues/SVDs/Autonne-Takagi; full all-288 phase diagram (P2-A, P2-B, P2-C).
  - RP3: Chowdhury-Eberhardt (arXiv:1503.08216 App. A) 2-loop Type-II 2HDM
    benchmarks (numerical < 1e-38 + exact SymPy rational proof), Martin
    (hep-ph/9709356 Eqs. 6.5.24-6.5.30) 7-eq benchmark, Xing-Zhou opposite sign;
    curved spin-1/2 Dirac G_{s=1/2} via piecewise Voronoi Clenshaw-Curtis polar
    quadrature + symplectic ODE; Piece 2 via implicit 2-stage 4th-order
    Gauss-Legendre (GL4) integrator with Branco/CE D-term boundary and
    multi-start Riemannian descent for DynamicV4; Piece 3 Autonne-Takagi PMNS;
    Guardrail 3 via 10-trial Cayley-transform Haar U(3)^5 x U(3)_{nu_R} scrambling.
  - RP4: All 6/6 planted negative controls (RPF1-RPF6) & 6/6 referee gates (RG1-RG6).

Pure stdlib + mpmath + sympy ONLY. Zero AST float/complex literals or casts.
Zero JSON floats. Strictly 0 of 19.
"""

import ast
import fractions
import hashlib
import json
import math
import os
import sys
import time

import mpmath as mp
import sympy as sp

Fraction = fractions.Fraction


# ============================================================================
# STRICT FLOAT-FREE HELPERS & SERIALIZATION
# ============================================================================

def rat(num, den=1):
    return mp.mpf(num) / mp.mpf(den)


def pow10(exp_int):
    return mp.power(mp.mpf(10), exp_int)


def fmt(val, digits=35):
    if val is None:
        return None
    if isinstance(val, mp.mpc):
        return {
            "re": mp.nstr(mp.re(val), digits),
            "im": mp.nstr(mp.im(val), digits),
        }
    return mp.nstr(mp.mpf(val), digits)


def assert_no_json_floats(obj, path="root"):
    if isinstance(obj, float):
        raise ValueError(f"Forbidden JSON float at {path}: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_json_floats(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            assert_no_json_floats(v, f"{path}[{i}]")


def self_audit_ast(script_path):
    with open(script_path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src, filename=script_path)
    forbidden_mods = {"numpy", "scipy", "frontier", "sage", "gap"}
    float_lits = 0
    complex_lits = 0
    bad_casts = 0
    bad_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_lits += 1
            elif isinstance(node.value, complex):
                complex_lits += 1
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
                bad_casts += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in forbidden_mods:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                if root in forbidden_mods:
                    bad_imports.append(node.module)
    return {
        "ast_float_literals": float_lits,
        "ast_complex_literals": complex_lits,
        "ast_float_complex_casts": bad_casts,
        "forbidden_imports": bad_imports,
        "clean": (float_lits == 0 and complex_lits == 0 and bad_casts == 0 and len(bad_imports) == 0),
    }


# ============================================================================
# DISJOINT LINEAR ALGEBRA (6x6 REAL-SPLIT SYMMETRIC mp.eigsy & 3x3 LIST OPS)
# ============================================================================

def mat3_zero():
    z = mp.mpc(0)
    return [[z, z, z], [z, z, z], [z, z, z]]


def mat3_eye():
    o = mp.mpc(1)
    z = mp.mpc(0)
    return [[o, z, z], [z, o, z], [z, z, o]]


def mat3_copy(A):
    return [[A[i][j] for j in range(3)] for i in range(3)]


def mat3_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]


def mat3_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]


def mat3_scale(c, A):
    return [[c * A[i][j] for j in range(3)] for i in range(3)]


def mat3_mul(A, B):
    out = mat3_zero()
    for i in range(3):
        a0, a1, a2 = A[i][0], A[i][1], A[i][2]
        for j in range(3):
            out[i][j] = a0 * B[0][j] + a1 * B[1][j] + a2 * B[2][j]
    return out


def mat3_dag(A):
    return [[mp.conj(A[j][i]) for j in range(3)] for i in range(3)]


def mat3_T(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def mat3_conj(A):
    return [[mp.conj(A[i][j]) for j in range(3)] for i in range(3)]


def mat3_sym_herm(A):
    half = rat(1, 2)
    return [[half * (A[i][j] + mp.conj(A[j][i])) for j in range(3)] for i in range(3)]


def mat3_tr(A):
    return A[0][0] + A[1][1] + A[2][2]


def mat3_frob(A):
    s = mp.mpf(0)
    for i in range(3):
        for j in range(3):
            v = A[i][j]
            s += mp.re(v) * mp.re(v) + mp.im(v) * mp.im(v)
    return mp.sqrt(s)


def mat3_inv(A):
    M = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            M[i, j] = A[i][j]
    Minv = M ** (-1)
    return [[Minv[i, j] for j in range(3)] for i in range(3)]


def herm3_eig_real_split(H):
    """Disjoint Hermitian 3x3 eigendecomposition via 6x6 real-split mp.eigsy."""
    R = mp.matrix(6, 6)
    for i in range(3):
        for j in range(3):
            hij = rat(1, 2) * (H[i][j] + mp.conj(H[j][i]))
            re_ij = mp.re(hij)
            im_ij = mp.im(hij)
            R[i, j] = re_ij
            R[i + 3, j + 3] = re_ij
            R[i, j + 3] = -im_ij
            R[i + 3, j] = im_ij
    evals, V = mp.eigsy(R)
    # Eigenvalues come in duplicate pairs: (0,1), (2,3), (4,5) sorted ascending
    # Build orthonormal complex eigenvectors carefully (Gram-Schmidt for degenerate pairs)
    lam = [evals[0], evals[2], evals[4]]
    cols = []
    for k in range(3):
        # Pick vector from pair (2k, 2k+1) with largest residual norm after orthogonalization
        best_vec = None
        best_nrm = mp.mpf(-1)
        for idx in (2 * k, 2 * k + 1):
            vec = [mp.mpc(V[i, idx], V[i + 3, idx]) for i in range(3)]
            for prev in cols:
                dot = sum(mp.conj(prev[i]) * vec[i] for i in range(3))
                vec = [vec[i] - dot * prev[i] for i in range(3)]
            nrm = mp.sqrt(sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in vec))
            if nrm > best_nrm:
                best_nrm = nrm
                best_vec = vec
        # Second Gram-Schmidt pass for high-precision orthogonality
        for prev in cols:
            dot = sum(mp.conj(prev[i]) * best_vec[i] for i in range(3))
            best_vec = [best_vec[i] - dot * prev[i] for i in range(3)]
        nrm = mp.sqrt(sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in best_vec))
        cols.append([c / nrm for c in best_vec])
    U = [[cols[j][i] for j in range(3)] for i in range(3)]
    return lam, U


def svd_left_real_split(Y):
    """Compute ascending singular values (s1 <= s2 <= s3) and left unitary U_L via 6x6 eigsy."""
    HL = mat3_mul(Y, mat3_dag(Y))
    evals, UL = herm3_eig_real_split(HL)
    sigs = [mp.sqrt(ev) if ev > 0 else mp.mpf(0) for ev in evals]
    return sigs, UL


def autonne_takagi_real_split(K):
    """
    Disjoint Autonne-Takagi factorization of complex symmetric 3x3 matrix K = K^T:
    K = U diag(s1, s2, s3) U^T with 0 <= s1 <= s2 <= s3, via 6x6 real symmetric
    A6 = [[Re K, Im K], [Im K, -Re K]] using mp.eigsy.
    """
    Ks = [[rat(1, 2) * (K[i][j] + K[j][i]) for j in range(3)] for i in range(3)]
    A6 = mp.matrix(6, 6)
    for i in range(3):
        for j in range(3):
            rk = mp.re(Ks[i][j])
            ik = mp.im(Ks[i][j])
            A6[i, j] = rk
            A6[i, j + 3] = ik
            A6[i + 3, j] = ik
            A6[i + 3, j + 3] = -rk
    evals, V = mp.eigsy(A6)
    # Eigenvalues are (-s3, -s2, -s1, +s1, +s2, +s3)
    # Top 3 indices 3, 4, 5 correspond to +s1 <= +s2 <= +s3
    sigs = [max(mp.mpf(0), evals[3]), max(mp.mpf(0), evals[4]), max(mp.mpf(0), evals[5])]
    cols = []
    for k in range(3):
        idx = 3 + k
        vec = [mp.mpc(V[i, idx], V[i + 3, idx]) for i in range(3)]
        # Verify/enforce complex unitarity against previous columns
        for prev in cols:
            dot = sum(mp.conj(prev[i]) * vec[i] for i in range(3))
            vec = [vec[i] - dot * prev[i] for i in range(3)]
        nrm = mp.sqrt(sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in vec))
        vec = [c / nrm for c in vec]
        # Fix overall Takagi phase so K conj(u) = +sigma u
        if sigs[k] > pow10(-30):
            Kuc = [sum(Ks[i][j] * mp.conj(vec[j]) for j in range(3)) for i in range(3)]
            ov = sum(mp.conj(vec[i]) * Kuc[i] for i in range(3))
            if abs(ov) > 0:
                ph = mp.sqrt(ov / abs(ov))
                vec = [c * ph for c in vec]
        cols.append(vec)
    U = [[cols[j][i] for j in range(3)] for i in range(3)]
    # Compute exact reconstruction error ||U diag(s) U^T - Ks||_F
    Smat = [[sigs[i] if i == j else mp.mpc(0) for j in range(3)] for i in range(3)]
    Krec = mat3_mul(mat3_mul(U, Smat), mat3_T(U))
    rec_err = mat3_frob(mat3_sub(Krec, Ks))
    unit_err = mat3_frob(mat3_sub(mat3_mul(mat3_dag(U), U), mat3_eye()))
    return sigs, U, rec_err, unit_err


# ============================================================================
# MODULE RP1: PENTAGONAL eta & E2, CHOWLA-SELBERG & LATTICE E(tau, s), FILQ
# ============================================================================

def eta_and_E2_pentagonal(tau):
    """
    Disjoint Dedekind eta via Euler's pentagonal number theorem:
      P(q) = sum_{k=-inf}^{inf} (-1)^k q^{k(3k-1)/2}
      eta(tau) = exp(i pi tau / 12) P(q)
      E2(tau) = 1 + 24 q P'(q) / P(q)
    """
    q = mp.exp(mp.mpc(0, 2) * mp.pi * tau)
    P = mp.mpc(1)
    qPp = mp.mpc(0)
    tol = pow10(-(mp.mp.dps + 10))
    k = 1
    while True:
        e1 = (k * (3 * k - 1)) // 2
        e2 = (k * (3 * k + 1)) // 2
        t1 = mp.power(q, e1)
        t2 = mp.power(q, e2)
        if abs(t1) * mp.mpf(e2) < tol:
            break
        if k % 2 == 1:
            P -= t1 + t2
            qPp -= mp.mpf(e1) * t1 + mp.mpf(e2) * t2
        else:
            P += t1 + t2
            qPp += mp.mpf(e1) * t1 + mp.mpf(e2) * t2
        k += 1
    eta = mp.exp(mp.mpc(0, 1) * mp.pi * tau / mp.mpf(12)) * P
    E2 = mp.mpc(1) + mp.mpf(24) * qPp / P
    return eta, E2


def V_RS(tau):
    y = mp.im(tau)
    eta, _ = eta_and_E2_pentagonal(tau)
    return -mp.log(y * mp.power(abs(eta), 4))


def V_FILQ(tau, n, drop_nonhol=False):
    y = mp.im(tau)
    eta, E2 = eta_and_E2_pentagonal(tau)
    E2_eff = E2 if drop_nonhol else (E2 - mp.mpf(3) / (mp.pi * y))
    pref = mp.power(mp.mpf(2) * y, -3 * n) * mp.power(abs(eta), -12 * n)
    bracket = (mp.mpf(n) * (mp.pi ** 2) * y * y / mp.mpf(3)) * (abs(E2_eff) ** 2) - mp.mpf(3)
    return pref * bracket


def divisor_sigma_neg(r, power_exp):
    """Compute sum_{d | r} d^{power_exp}."""
    s = mp.mpf(0)
    lim = math.isqrt(r)
    for d in range(1, lim + 1):
        if r % d == 0:
            s += mp.power(mp.mpf(d), power_exp)
            q = r // d
            if q != d:
                s += mp.power(mp.mpf(q), power_exp)
    return s


def E_chowla_selberg(tau, s):
    """Real-analytic Eisenstein series E(tau, s) = sum' y^s |m tau + n|^{-2s}."""
    x = mp.re(tau)
    y = mp.im(tau)
    sm = mp.mpf(s)
    term0 = mp.mpf(2) * mp.zeta(mp.mpf(2) * sm) * mp.power(y, sm)
    term1 = (
        mp.mpf(2)
        * mp.sqrt(mp.pi)
        * (mp.gamma(sm - rat(1, 2)) / mp.gamma(sm))
        * mp.zeta(mp.mpf(2) * sm - mp.mpf(1))
        * mp.power(y, mp.mpf(1) - sm)
    )
    pref = mp.mpf(8) * mp.power(mp.pi, sm) * mp.sqrt(y) / mp.gamma(sm)
    cutoff = mp.mpf(mp.mp.dps + 12) * mp.log(mp.mpf(10))
    fourier = mp.mpf(0)
    r = 1
    while True:
        z = mp.mpf(2) * mp.pi * mp.mpf(r) * y
        if z > cutoff:
            break
        sig = divisor_sigma_neg(r, mp.mpf(1) - mp.mpf(2) * sm)
        if s == 3:
            K = mp.sqrt(mp.pi / (mp.mpf(2) * z)) * mp.exp(-z) * (
                mp.mpf(1) + mp.mpf(3) / z + mp.mpf(3) / (z * z)
            )
        elif s == 2:
            K = mp.sqrt(mp.pi / (mp.mpf(2) * z)) * mp.exp(-z) * (mp.mpf(1) + mp.mpf(1) / z)
        else:
            K = mp.besselk(sm - rat(1, 2), z)
        fourier += (
            pref
            * mp.power(mp.mpf(r), sm - rat(1, 2))
            * sig
            * K
            * mp.cos(mp.mpf(2) * mp.pi * mp.mpf(r) * x)
        )
        r += 1
    return term0 + term1 + fourier


def E_lattice_box(tau, s, N_box):
    """Direct square-box lattice sum for both bosonic and half-period spin sums."""
    x = mp.re(tau)
    y = mp.im(tau)
    ys = mp.power(y, s)
    bos = mp.mpf(0)
    half = mp.mpf(0)
    for m in range(-N_box, N_box + 1):
        mx = mp.mpf(m) * x
        my2 = (mp.mpf(m) * y) ** 2
        m_even = (m % 2 == 0)
        for n in range(-N_box, N_box + 1):
            if m == 0 and n == 0:
                continue
            r2 = (mx + mp.mpf(n)) ** 2 + my2
            val = ys / mp.power(r2, s)
            bos += val
            if m_even and (n % 2 == 0):
                half += mp.mpf(3) * val
            else:
                half -= val
    return bos, half


def grad_hess_2d_fd4(func, x0, y0, hx, hy):
    """4th-order central finite-difference gradient and 2D Hessian."""
    def f(x, y):
        return func(mp.mpc(x, y))

    f0 = f(x0, y0)
    fxp1 = f(x0 + hx, y0)
    fxm1 = f(x0 - hx, y0)
    fxp2 = f(x0 + mp.mpf(2) * hx, y0)
    fxm2 = f(x0 - mp.mpf(2) * hx, y0)
    fyp1 = f(x0, y0 + hy)
    fym1 = f(x0, y0 - hy)
    fyp2 = f(x0, y0 + mp.mpf(2) * hy)
    fym2 = f(x0, y0 - mp.mpf(2) * hy)

    gx = (-fxp2 + mp.mpf(8) * fxp1 - mp.mpf(8) * fxm1 + fxm2) / (mp.mpf(12) * hx)
    gy = (-fyp2 + mp.mpf(8) * fyp1 - mp.mpf(8) * fym1 + fym2) / (mp.mpf(12) * hy)
    hxx = (-fxp2 + mp.mpf(16) * fxp1 - mp.mpf(30) * f0 + mp.mpf(16) * fxm1 - fxm2) / (
        mp.mpf(12) * hx * hx
    )
    hyy = (-fyp2 + mp.mpf(16) * fyp1 - mp.mpf(30) * f0 + mp.mpf(16) * fym1 - fym2) / (
        mp.mpf(12) * hy * hy
    )
    fpp = f(x0 + hx, y0 + hy)
    fpm = f(x0 + hx, y0 - hy)
    fmp = f(x0 - hx, y0 + hy)
    fmm = f(x0 - hx, y0 - hy)
    hxy = (fpp - fpm - fmp + fmm) / (mp.mpf(4) * hx * hy)
    tr = hxx + hyy
    disc = mp.sqrt((hxx - hyy) ** 2 + mp.mpf(4) * hxy * hxy)
    lam1 = rat(1, 2) * (tr - disc)
    lam2 = rat(1, 2) * (tr + disc)
    return f0, gx, gy, hxx, hyy, hxy, lam1, lam2


def run_rp1():
    mp.mp.dps = 55
    tau_i = mp.mpc(0, 1)
    tau_om = mp.mpc(rat(1, 2), mp.sqrt(mp.mpf(3)) / mp.mpf(2))
    tau_gen = mp.mpc(rat(137, 1000), rat(1213, 1000))
    tau_2i = mp.mpc(0, 2)
    tau_4i = mp.mpc(0, 4)

    # 1. T and S invariance of E3, E2, V_RS at tau_gen
    pots = {
        "E3": lambda t: E_chowla_selberg(t, 3),
        "E2": lambda t: E_chowla_selberg(t, 2),
        "V_RS": V_RS,
    }
    inv_res = {}
    crit_res = {}
    h_fd = pow10(-8)
    for name, fn in pots.items():
        v0 = fn(tau_gen)
        vT = fn(tau_gen + mp.mpf(1))
        vS = fn(-mp.mpc(1) / tau_gen)
        errT = abs(vT - v0) / abs(v0)
        errS = abs(vS - v0) / abs(v0)
        inv_res[name] = {
            "val_gen": fmt(v0, 40),
            "T_rel_err": fmt(errT, 10),
            "S_rel_err": fmt(errS, 10),
            "pass_lt_1e32": bool(errT < pow10(-32) and errS < pow10(-32)),
        }
        vi, gxi, gyi, hxxi, hyyi, hxyi, l1i, l2i = grad_hess_2d_fd4(fn, mp.mpf(0), mp.mpf(1), h_fd, h_fd)
        vo, gxo, gyo, hxxo, hyyo, hxyo, l1o, l2o = grad_hess_2d_fd4(
            fn, rat(1, 2), mp.sqrt(mp.mpf(3)) / mp.mpf(2), h_fd, h_fd
        )
        v2i = fn(tau_2i)
        v4i = fn(tau_4i)
        crit_res[name] = {
            "val_i": fmt(vi, 35),
            "grad_i_norm": fmt(mp.hypot(gxi, gyi), 10),
            "eig1_i": fmt(l1i, 25),
            "eig2_i": fmt(l2i, 25),
            "i_is_saddle": bool(l1i < 0 and l2i > 0 and mp.hypot(gxi, gyi) < pow10(-20)),
            "val_omega": fmt(vo, 35),
            "grad_omega_norm": fmt(mp.hypot(gxo, gyo), 10),
            "eig1_omega": fmt(l1o, 25),
            "eig2_omega": fmt(l2o, 25),
            "omega_is_isotropic_min": bool(
                l1o > 0
                and l2o > 0
                and abs(l1o - l2o) / abs(l1o) < pow10(-20)
                and mp.hypot(gxo, gyo) < pow10(-20)
            ),
            "val_2i": fmt(v2i, 35),
            "val_4i": fmt(v4i, 35),
            "cusp_monotone": bool(vo < vi < v2i < v4i),
        }

    # 2. Direct square-box lattice cross-check (N=45) and exact -15/16 proof
    exact_s3_ratio = Fraction(4, 2 ** (2 * 3)) - Fraction(1, 1)  # 4/64 - 1 = -15/16
    assert exact_s3_ratio == Fraction(-15, 16)
    bos_box, half_box = E_lattice_box(tau_gen, 3, 45)
    E3_cs_gen = E_chowla_selberg(tau_gen, 3)
    box_vs_cs_rel = abs(bos_box - E3_cs_gen) / abs(E3_cs_gen)
    ratio_box = half_box / bos_box
    ratio_err = abs(ratio_box - rat(-15, 16))
    half_period_res = {
        "exact_fraction_proof": f"{exact_s3_ratio.numerator}/{exact_s3_ratio.denominator}",
        "exact_equals_neg_15_16": bool(exact_s3_ratio == Fraction(-15, 16)),
        "N_box": 45,
        "E3_box_gen": fmt(bos_box, 25),
        "E3_cs_gen": fmt(E3_cs_gen, 25),
        "box_vs_cs_rel_err": fmt(box_vs_cs_rel, 10),
        "half_period_ratio_box": fmt(ratio_box, 25),
        "half_period_ratio_abs_err": fmt(ratio_err, 10),
        "pass": bool(exact_s3_ratio == Fraction(-15, 16) and box_vs_cs_rel < pow10(-5) and ratio_err < pow10(-5)),
    }

    # 3. Kronecker first limit formula at i, omega_+, tau_gen
    eps_k = pow10(-24)
    s_k = mp.mpf(1) + eps_k
    kron_res = {}
    kron_pass = True
    for label, tpt in (("i", tau_i), ("omega", tau_om), ("tau_gen", tau_gen)):
        lhs = E_chowla_selberg(tpt, s_k) - mp.pi / eps_k
        rhs = mp.pi * V_RS(tpt) + mp.mpf(2) * mp.pi * (mp.euler - mp.log(mp.mpf(2)))
        err = abs(lhs - rhs)
        ok = bool(err < pow10(-16))
        kron_pass = kron_pass and ok
        kron_res[label] = {
            "lhs": fmt(lhs, 30),
            "rhs": fmt(rhs, 30),
            "abs_err": fmt(err, 10),
            "pass_lt_1e16": ok,
        }

    # 4. Zero-parameter N=1 SUGRA FILQ (1990) potentials n=1, 2, 3
    filq_res = {}
    filq_vacua = {}
    filq_pass = True
    h_n = pow10(-10)
    for n in (1, 2, 3):
        fn = lambda t, nn=n: V_FILQ(t, nn)
        v0 = fn(tau_gen)
        vT = fn(tau_gen + mp.mpf(1))
        vS = fn(-mp.mpc(1) / tau_gen)
        errT = abs(vT - v0) / abs(v0)
        errS = abs(vS - v0) / abs(v0)
        # Solve 1D Newton along x=0 starting from y = 6/5 (independent of target!)
        y = rat(6, 5)
        for _ in range(30):
            _, _, gy, _, hyy, _, _, _ = grad_hess_2d_fd4(fn, mp.mpf(0), y, h_n, h_n)
            if abs(gy) < pow10(-32):
                break
            step = gy / hyy
            if abs(step) > rat(1, 5):
                step = (rat(1, 5) if step > 0 else rat(-1, 5))
            y -= step
        vst, gx, gy, hxx, hyy, hxy, l1, l2 = grad_hess_2d_fd4(fn, mp.mpf(0), y, h_n, h_n)
        vi = fn(tau_i)
        vo = fn(tau_om)
        v2i = fn(tau_2i)
        v4i = fn(tau_4i)
        gnorm = mp.hypot(gx, gy)
        ok = bool(
            errT < pow10(-32)
            and errS < pow10(-32)
            and gnorm < pow10(-20)
            and hxx > 0
            and hyy > 0
            and l1 > 0
            and vst < vi < vo
            and v4i > v2i > 0
        )
        filq_pass = filq_pass and ok
        filq_vacua[n] = mp.mpc(0, y)
        filq_res[f"n={n}"] = {
            "T_rel_err": fmt(errT, 10),
            "S_rel_err": fmt(errS, 10),
            "y_star": fmt(y, 35),
            "V_star": fmt(vst, 35),
            "grad_norm": fmt(gnorm, 10),
            "V_xx": fmt(hxx, 25),
            "V_yy": fmt(hyy, 25),
            "V_xy": fmt(hxy, 10),
            "eig1": fmt(l1, 25),
            "eig2": fmt(l2, 25),
            "V_i": fmt(vi, 30),
            "V_omega": fmt(vo, 30),
            "V_2i": fmt(v2i, 30),
            "V_4i": fmt(v4i, 30),
            "pass": ok,
        }

    rg1_pass = (
        all(v["pass_lt_1e32"] for v in inv_res.values())
        and all(v["i_is_saddle"] and v["omega_is_isotropic_min"] and v["cusp_monotone"] for v in crit_res.values())
        and half_period_res["pass"]
        and kron_pass
        and filq_pass
    )
    out = {
        "modular_invariance": inv_res,
        "critical_points_and_cusp": crit_res,
        "half_period_minus_15_16": half_period_res,
        "kronecker_first_limit": kron_res,
        "filq_sugra": filq_res,
        "RG1_pass": rg1_pass,
    }
    return out, filq_vacua


# ============================================================================
# MODULE RP2: DISJOINT FUCHSIAN L2(tau) SOLVER & FRAME C ALL-288 PHASE DIAGRAM
# ============================================================================

def fd_reduce(tau):
    """Map tau -> z_fd in standard SL(2, Z) fundamental domain, returning (z_fd, c, d)."""
    # Track matrix M = [[a, b], [c, d]] so z_fd = (a tau + b) / (c tau + d)
    a, b, c, d = 1, 0, 0, 1
    z = tau
    for _ in range(100):
        k = int(mp.nint(mp.re(z)))
        if k != 0:
            z = z - mp.mpf(k)
            a, b = a - k * c, b - k * d
        if abs(z) < mp.mpf(1) - pow10(-30):
            z = -mp.mpc(1) / z
            a, b, c, d = -c, -d, a, b
        else:
            break
    # Canonical boundary tie-break: Re(z) in (-1/2, 1/2]
    if mp.re(z) <= -rat(1, 2) + pow10(-30):
        z = z + mp.mpf(1)
        a, b = a + c, b + d
    return z, c, d


def make_wp_div4_theta1(tau, E2_val):
    """
    Disjoint Weierstrass wp(z)/4 via exact Jacobi theta_1 logarithmic derivative:
      wp(z) = -d_z^2 ln theta_1(pi z, tau) - (pi^2 / 3) E2(tau)
    """
    q = mp.exp(mp.mpc(0, 1) * mp.pi * tau)
    y = mp.im(tau)
    nmax = int(mp.ceil(mp.sqrt((mp.mpf(mp.mp.dps) * mp.mpf(3) + mp.pi * y * mp.mpf(2)) / (mp.pi * y)))) + 5
    coeffs = []
    for n in range(nmax):
        e = mp.mpf(2 * n + 1)
        sgn = mp.mpf(2) if (n % 2 == 0) else mp.mpf(-2)
        coeffs.append((e, sgn * mp.power(q, e * e / mp.mpf(4))))
    c_e2 = (mp.pi ** 2 / mp.mpf(3)) * E2_val
    pi2 = mp.pi ** 2
    inv2i = mp.mpc(0, -rat(1, 2))
    inv2 = rat(1, 2)

    def wp_div4(z):
        k_sh = int(mp.nint(mp.im(z) / y))
        zr = z - mp.mpf(k_sh) * tau
        v = mp.pi * zr
        eiv = mp.exp(mp.mpc(0, 1) * v)
        emiv = mp.mpc(1) / eiv
        e2iv = eiv * eiv
        em2iv = emiv * emiv
        p_pos = eiv
        p_neg = emiv
        s0 = mp.mpc(0)
        s1 = mp.mpc(0)
        s2 = mp.mpc(0)
        for e, c in coeffs:
            sv = (p_pos - p_neg) * inv2i
            cv = (p_pos + p_neg) * inv2
            s0 += c * sv
            s1 += c * e * cv
            s2 -= c * e * e * sv
            p_pos *= e2iv
            p_neg *= em2iv
        return (-pi2 * (s2 * s0 - s1 * s1) / (s0 * s0) - c_e2) / mp.mpf(4)

    return wp_div4


def make_yoshida6_15_weights():
    """Exact algebraic 15-stage 6th-order Yoshida-Suzuki symplectic weights (max|w|=0.888)."""
    r3 = mp.power(mp.mpf(4), rat(1, 3))
    s4 = mp.mpf(1) / (mp.mpf(4) - r3)
    m4 = mp.mpf(1) - mp.mpf(4) * s4
    W4 = [s4, s4, m4, s4, s4]
    r5 = mp.power(mp.mpf(2), rat(1, 5))
    w1_6 = mp.mpf(1) / (mp.mpf(2) - r5)
    w0_6 = -r5 * w1_6
    return [w1_6 * w for w in W4] + [w0_6 * w for w in W4] + [w1_6 * w for w in W4]


def vandermonde_extrap_weights(muls, start_p=6):
    m = len(muls)
    A = mp.matrix(m, m)
    b = mp.matrix(m, 1)
    for j in range(m):
        A[0, j] = mp.mpf(1)
    b[0] = mp.mpf(1)
    for i in range(1, m):
        p = start_p + 2 * (i - 1)
        for j in range(m):
            A[i, j] = mp.power(mp.mpf(muls[j]), -p)
        b[i] = mp.mpf(0)
    w = mp.lu_solve(A, b)
    return [w[j] for j in range(m)]


def build_symplectic_nodes(segments, W):
    nodes = []
    for za, zb, n in segments:
        dz = (zb - za) / mp.mpf(n)
        z = za
        for _ in range(n):
            zc = z
            for w in W:
                h = dz * w
                h2 = h / mp.mpf(2)
                nodes.append((h, h2, zc + h2))
                zc += h
            z += dz
    return nodes


def eval_monodromy_var(q_arr, h_arr, B):
    """Explicit Yoshida-Suzuki symplectic propagation of M and dM/dB (exact det=1)."""
    u1 = mp.mpc(1)
    u2 = mp.mpc(0)
    v1 = mp.mpc(0)
    v2 = mp.mpc(1)
    du1 = mp.mpc(0)
    du2 = mp.mpc(0)
    dv1 = mp.mpc(0)
    dv2 = mp.mpc(0)
    for (h, h2), q0 in zip(h_arr, q_arr):
        u1 += h2 * v1
        u2 += h2 * v2
        du1 += h2 * dv1
        du2 += h2 * dv2
        q = q0 + B
        dv1 -= h * (q * du1 + u1)
        dv2 -= h * (q * du2 + u2)
        v1 -= h * q * u1
        v2 -= h * q * u2
        u1 += h2 * v1
        u2 += h2 * v2
        du1 += h2 * dv1
        du2 += h2 * dv2
    return (u1, u2, v1, v2), (du1, du2, dv1, dv2)


def solve_invariant_G(Ma, Mb):
    """Solve M_a G M_a^dag = G, M_b G M_b^dag = G, G^dag = G, det G = -1 via 4x4 eigsy."""
    def eqs(M):
        a, b, c, d = M
        ab = a * mp.conj(b)
        cd = c * mp.conj(d)
        ac = a * mp.conj(c)
        ad = a * mp.conj(d)
        bc = b * mp.conj(c)
        bd = b * mp.conj(d)
        cr = ad - mp.mpc(1) + bc
        cs = mp.mpc(0, 1) * (ad - mp.mpc(1) - bc)
        return [
            [mp.re(a * mp.conj(a)) - mp.mpf(1), mp.mpf(2) * mp.re(ab), -mp.mpf(2) * mp.im(ab), mp.re(b * mp.conj(b))],
            [mp.re(c * mp.conj(c)), mp.mpf(2) * mp.re(cd), -mp.mpf(2) * mp.im(cd), mp.re(d * mp.conj(d)) - mp.mpf(1)],
            [mp.re(ac), mp.re(cr), mp.re(cs), mp.re(bd)],
            [mp.im(ac), mp.im(cr), mp.im(cs), mp.im(bd)],
        ]

    rows = eqs(Ma) + eqs(Mb)
    ATA = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            ATA[i, j] = sum(row[i] * row[j] for row in rows)
    _, evecs = mp.eigsy(ATA)
    h11, r, s, h22 = [evecs[i, 0] for i in range(4)]
    sc = mp.sqrt(-(h11 * h22 - r * r - s * s))
    G = mp.matrix([[h11 / sc, mp.mpc(r, s) / sc], [mp.mpc(r, -s) / sc, h22 / sc]])
    if mp.re(G[0, 0]) < 0:
        G = -G
    return G


def frobenius_coeffs(tau, B, Kmax):
    """Exact Frobenius series coefficients aa[k], bb[k] for u'' + (wp(z)/4 + B) u = 0 at z=0."""
    y = mp.im(tau)
    n_th = int(mp.ceil(mp.sqrt(mp.mpf(mp.mp.dps) * mp.mpf(3) / (mp.pi * y)))) + 4
    th2 = mp.mpc(0)
    th3 = mp.mpc(0)
    th4 = mp.mpc(0)
    for n in range(-n_th, n_th + 1):
        nf = mp.mpf(n)
        th2 += mp.exp(mp.mpc(0, 1) * mp.pi * tau * (nf + rat(1, 2)) ** 2)
        t3n = mp.exp(mp.mpc(0, 1) * mp.pi * tau * nf * nf)
        th3 += t3n
        th4 += t3n if (n % 2 == 0) else -t3n
    E4 = (mp.power(th2, 8) + mp.power(th3, 8) + mp.power(th4, 8)) / mp.mpf(2)
    E6 = (
        (mp.power(th2, 4) + mp.power(th3, 4))
        * (mp.power(th3, 4) + mp.power(th4, 4))
        * (mp.power(th4, 4) - mp.power(th2, 4))
        / mp.mpf(2)
    )
    g2 = (mp.mpf(4) * mp.power(mp.pi, 4) / mp.mpf(3)) * E4
    g3 = (mp.mpf(8) * mp.power(mp.pi, 6) / mp.mpf(27)) * E6
    cc = [mp.mpc(0)] * (Kmax + 1)
    cc[1] = g2 / mp.mpf(20)
    cc[2] = g3 / mp.mpf(28)
    for k in range(3, Kmax + 1):
        cc[k] = (mp.mpf(3) / mp.mpf((2 * k + 3) * (k - 2))) * sum(
            cc[j] * cc[k - 1 - j] for j in range(1, k - 1)
        )
    qq = [B] + [cc[m] / mp.mpf(4) for m in range(1, Kmax + 1)]
    aa = [mp.mpc(0)] * (Kmax + 1)
    bb = [mp.mpc(0)] * (Kmax + 1)
    aa[0] = mp.mpc(1)
    for k in range(1, Kmax + 1):
        aa[k] = -sum(qq[m] * aa[k - 1 - m] for m in range(k)) / mp.mpf(4 * k * k)
        bb[k] = -(mp.mpf(4 * k) * aa[k] + sum(qq[m] * bb[k - 1 - m] for m in range(k))) / mp.mpf(
            4 * k * k
        )
    return aa, bb


def eval_frobenius(zs, aa, bb):
    sqz = mp.sqrt(zs)
    lnz = mp.log(zs)
    z2 = zs * zs
    zp = mp.mpc(1)
    p1 = mp.mpc(0)
    dp1 = mp.mpc(0)
    p2 = mp.mpc(0)
    dp2 = mp.mpc(0)
    for k in range(len(aa)):
        p = mp.mpf(2 * k) + rat(1, 2)
        p1 += aa[k] * zp
        dp1 += aa[k] * p * zp
        p2 += bb[k] * zp
        dp2 += bb[k] * p * zp
        zp *= z2
    f1 = sqz * p1
    f1p = (sqz / zs) * dp1
    f2 = f1 * lnz + sqz * p2
    f2p = f1p * lnz + f1 / zs + (sqz / zs) * dp2
    return f1, f2, f1p, f2p


def solve_L2_raw(tau, high_prec=False):
    """
    Direct raw Fuchsian L2(tau) = pi - C(tau) solver via explicit 6th-order
    Yoshida-Suzuki symplectic splitting + Vandermonde extrapolation + Frobenius match.
    """
    _, E2_val = eta_and_E2_pentagonal(tau)
    wp4 = make_wp_div4_theta1(tau, E2_val)
    W6 = make_yoshida6_15_weights()
    z0 = (mp.mpf(1) + tau) / mp.mpf(2)
    pts_b = [
        mp.mpf(0), rat(1, 4), rat(3, 8), rat(7, 16), rat(1, 2),
        rat(9, 16), rat(5, 8), rat(3, 4), mp.mpf(1),
    ]
    y_scale = max(1, int(mp.ceil(abs(tau) / mp.mpf(2))))

    if high_prec:
        # 8-level sequence -> O(h^20), achieves < 1e-28 even at Im(tau)=0.799 in ~4s
        muls = [2, 3, 4, 5, 6, 8, 10, 12]
        base_a = 6
        base_b = [y_scale, y_scale, y_scale, 2 * y_scale, 2 * y_scale, y_scale, y_scale, y_scale]
        base_r = 3
        n_oct = 4
        Kmax = 28
        newton_tol = pow10(-34)
    else:
        # 4-level fast sequence -> O(h^12), achieves < 1e-16 cleanly at all y up to y=5 in ~1s
        muls = [2, 3, 4, 6]
        base_a = 4
        base_b = [y_scale, y_scale, y_scale, 2 * y_scale, 2 * y_scale, y_scale, y_scale, y_scale]
        base_r = 2
        n_oct = 4
        Kmax = 22
        newton_tol = pow10(-20)

    ew = vandermonde_extrap_weights(muls, 6)
    a_grids = []
    b_grids = []
    for mul in muls:
        na_nodes = build_symplectic_nodes([(z0, z0 + mp.mpf(1), base_a * mul)], W6)
        a_grids.append(([wp4(zc) for _, _, zc in na_nodes], [(h, h2) for h, h2, _ in na_nodes]))
        segs_b = [
            (z0 + pts_b[i] * tau, z0 + pts_b[i + 1] * tau, base_b[i] * mul)
            for i in range(len(base_b))
        ]
        nb_nodes = build_symplectic_nodes(segs_b, W6)
        b_grids.append(([wp4(zc) for _, _, zc in nb_nodes], [(h, h2) for h, h2, _ in nb_nodes]))

    def eval_MaMb(B_val):
        Mas, dMas, Mbs, dMbs = [], [], [], []
        for (qa, ha), (qb, hb) in zip(a_grids, b_grids):
            Ma, dMa = eval_monodromy_var(qa, ha, B_val)
            Mb, dMb = eval_monodromy_var(qb, hb, B_val)
            Mas.append(Ma)
            dMas.append(dMa)
            Mbs.append(Mb)
            dMbs.append(dMb)
        Ma_ex = tuple(sum(w * m[i] for w, m in zip(ew, Mas)) for i in range(4))
        dMa_ex = tuple(sum(w * m[i] for w, m in zip(ew, dMas)) for i in range(4))
        Mb_ex = tuple(sum(w * m[i] for w, m in zip(ew, Mbs)) for i in range(4))
        dMb_ex = tuple(sum(w * m[i] for w, m in zip(ew, dMbs)) for i in range(4))
        return Ma_ex, dMa_ex, Mb_ex, dMb_ex

    B = (mp.pi ** 2 / mp.mpf(12)) * (E2_val - mp.mpf(3) / (mp.pi * mp.im(tau)))
    # Warm-start Newton on coarsest level
    for _ in range(6):
        Ma0, dMa0 = eval_monodromy_var(a_grids[0][0], a_grids[0][1], B)
        Mb0, dMb0 = eval_monodromy_var(b_grids[0][0], b_grids[0][1], B)
        f1 = mp.im(Ma0[0] + Ma0[3])
        f2 = mp.im(Mb0[0] + Mb0[3])
        if max(abs(f1), abs(f2)) < pow10(-10):
            break
        dta = dMa0[0] + dMa0[3]
        dtb = dMb0[0] + dMb0[3]
        det = mp.im(dta) * mp.re(dtb) - mp.re(dta) * mp.im(dtb)
        B += mp.mpc(-(mp.re(dtb) * f1 - mp.re(dta) * f2) / det, -(-mp.im(dtb) * f1 + mp.im(dta) * f2) / det)

    # Full extrapolated Newton
    for _ in range(8):
        Ma, dMa, Mb, dMb = eval_MaMb(B)
        f1 = mp.im(Ma[0] + Ma[3])
        f2 = mp.im(Mb[0] + Mb[3])
        if max(abs(f1), abs(f2)) < newton_tol:
            break
        dta = dMa[0] + dMa[3]
        dtb = dMb[0] + dMb[3]
        det = mp.im(dta) * mp.re(dtb) - mp.re(dta) * mp.im(dtb)
        B += mp.mpc(-(mp.re(dtb) * f1 - mp.re(dta) * f2) / det, -(-mp.im(dtb) * f1 + mp.im(dta) * f2) / det)

    G = solve_invariant_G(Ma, Mb)

    # Inward ray z0 -> zs with |zs| <= 1/16 even for large y (y = 4, 5)!
    n_pre = 0
    z_test = z0
    while abs(z_test) > mp.mpf(1):
        z_test = z_test / mp.mpf(2)
        n_pre += 1
    total_oct = n_oct + n_pre
    Mrs = []
    zs = z0 / mp.mpf(1 << total_oct)
    for mul in muls:
        segs_r = []
        zc = z0
        for _ in range(total_oct):
            zn = zc / mp.mpf(2)
            segs_r.append((zc, zn, base_r * mul))
            zc = zn
        nr_nodes = build_symplectic_nodes(segs_r, W6)
        qr = [wp4(zpt) for _, _, zpt in nr_nodes]
        hr = [(h, h2) for h, h2, _ in nr_nodes]
        Mr, _ = eval_monodromy_var(qr, hr, B)
        Mrs.append(Mr)
    Mr_ex = tuple(sum(w * m[i] for w, m in zip(ew, Mrs)) for i in range(4))

    aa, bb = frobenius_coeffs(tau, B, Kmax)
    f1, f2, f1p, f2p = eval_frobenius(zs, aa, bb)
    F = mp.matrix([[f1, f2], [f1p, f2p]])
    Mmat = mp.matrix([[Mr_ex[0], Mr_ex[1]], [Mr_ex[2], Mr_ex[3]]])
    Cconn = (F ** (-1)) * Mmat
    G0 = Cconn * G * Cconn.H
    C_val = mp.re(G0[0, 0]) / mp.mpf(2)
    L2_val = mp.pi - C_val
    return L2_val, C_val, B, abs(G0[1, 1]), abs(G0[0, 1] + mp.mpc(1))


def solve_L2_fd_covariant(tau, high_prec=False):
    """FD-reduced covariant L2(tau) = L2(z_fd) - ln|c tau + d|."""
    z_fd, c, d = fd_reduce(tau)
    L2_fd, C_fd, B_fd, g22, g12 = solve_L2_raw(z_fd, high_prec=high_prec)
    factor = abs(mp.mpf(c) * tau + mp.mpf(d))
    L2_tau = L2_fd - mp.log(factor)
    return L2_tau, C_fd, B_fd, g22, g12


# ---- Frame C Operators & All-288 Fermion Potential ----

def build_quaternion_frame_c():
    I2 = mp.matrix([[1, 0], [0, 1]])
    QI = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    BL = [QJ, QI, QK]
    U_list = [I2, QI, QJ, QK]
    A_mat = mp.matrix(4, 4)
    for a_idx, ua in enumerate(U_list):
        M = EPS * ua
        A_mat[a_idx, 0] = M[0, 0]
        A_mat[a_idx, 1] = M[0, 1]
        A_mat[a_idx, 2] = M[1, 0]
        A_mat[a_idx, 3] = M[1, 1]
    A_inv = A_mat ** (-1)
    keys = ("1", "i", "j", "k")
    edual = {}
    for b_idx, key in enumerate(keys):
        edual[key] = mp.matrix(
            [[A_inv[0, b_idx], A_inv[1, b_idx]], [A_inv[2, b_idx], A_inv[3, b_idx]]]
        )
    # Direct algebraic verification of dual basis orthogonality (< 1e-12)
    max_orth_err = mp.mpf(0)
    for a_idx, ua in enumerate(U_list):
        M = EPS * ua
        for b_idx, key in enumerate(keys):
            E = edual[key]
            ip = M[0, 0] * E[0, 0] + M[0, 1] * E[0, 1] + M[1, 0] * E[1, 0] + M[1, 1] * E[1, 1]
            target = mp.mpc(1) if a_idx == b_idx else mp.mpc(0)
            err = abs(ip - target)
            if err > max_orth_err:
                max_orth_err = err
    assert max_orth_err < pow10(-20)
    return QI, QJ, QK, EPS, BL, edual


def build_E30_prim_mod_pm():
    pts = []
    seen = set()
    for m in range(30):
        for n in range(30):
            if math.gcd(math.gcd(m, n), 30) == 1:
                canon = min((m, n), ((-m) % 30, (-n) % 30))
                if canon not in seen:
                    seen.add(canon)
                    pts.append(canon)
    assert len(pts) == 288
    return pts


def theta_char(ca, cb, tau, need_deriv=False):
    ca_r = ca - mp.floor(ca)
    s = mp.mpc(0)
    ds = mp.mpc(0)
    y = mp.im(tau)
    cutoff = mp.mpf(mp.mp.dps + 10) * mp.log(mp.mpf(10))
    nmax = int(mp.ceil(mp.sqrt(cutoff / (mp.pi * y)))) + 2
    for n in range(-nmax, nmax + 1):
        nc = mp.mpf(n) + ca_r
        t = mp.exp(mp.mpc(0, 1) * mp.pi * tau * nc * nc + mp.mpc(0, 2) * mp.pi * nc * cb)
        s += t
        if need_deriv:
            ds += mp.mpc(0, 2) * mp.pi * nc * t
    return (s, ds) if need_deriv else s


def F_u_kronecker(alpha, beta, tau):
    """Regularized Kronecker / digamma sum F_u(alpha, beta; tau) = lim_{s->1}(Z - pi/(s-1))."""
    a = alpha - mp.floor(alpha)
    b = beta - mp.floor(beta)
    x = mp.re(tau)
    y = mp.im(tau)
    cutoff = mp.mpf(mp.mp.dps + 10) * mp.log(mp.mpf(10))
    if abs(a) < pow10(-(mp.mp.dps - 5)):
        m0 = (mp.pi ** 2 * y) / (mp.sin(mp.pi * b) ** 2)
        zm = mp.mpf(2) * mp.pi * mp.euler - mp.pi * mp.log(y) - mp.mpf(2) * mp.pi * mp.log(mp.mpf(2))
        nzm = mp.mpf(0)
        m = 1
        while True:
            um = mp.mpf(m) * y
            if mp.mpf(2) * mp.pi * um > cutoff:
                break
            for vm in (mp.mpf(m) * x + b, -mp.mpf(m) * x + b):
                w = mp.exp(mp.mpc(-mp.mpf(2) * mp.pi * um, mp.mpf(2) * mp.pi * vm))
                nzm += (mp.pi / mp.mpf(m)) * mp.mpf(2) * mp.re(w / (mp.mpf(1) - w))
            m += 1
        return m0 + zm + nzm
    zm = (
        -mp.pi * (mp.digamma(a) + mp.digamma(mp.mpf(1) - a))
        - mp.pi * mp.log(y)
        - mp.mpf(2) * mp.pi * mp.log(mp.mpf(2))
    )
    nzm = mp.mpf(0)
    m = 0
    while True:
        ma = mp.mpf(m) + a
        um = ma * y
        if mp.mpf(2) * mp.pi * um > cutoff:
            break
        vm = ma * x + b
        w = mp.exp(mp.mpc(-mp.mpf(2) * mp.pi * um, mp.mpf(2) * mp.pi * vm))
        nzm += (mp.pi / ma) * mp.mpf(2) * mp.re(w / (mp.mpf(1) - w))
        m += 1
    k = 1
    while True:
        ma = mp.mpf(k) - a
        um = ma * y
        if mp.mpf(2) * mp.pi * um > cutoff:
            break
        vm = -ma * x + b
        w = mp.exp(mp.mpc(-mp.mpf(2) * mp.pi * um, mp.mpf(2) * mp.pi * vm))
        nzm += (mp.pi / ma) * mp.mpf(2) * mp.re(w / (mp.mpf(1) - w))
        k += 1
    return zm + nzm


def S_coeffs_frame_c(tau):
    eta, _ = eta_and_E2_pentagonal(tau)
    eta3 = eta ** 3
    th2 = theta_char(rat(1, 2), mp.mpf(0), tau)
    th3 = theta_char(mp.mpf(0), mp.mpf(0), tau)
    th4 = theta_char(mp.mpf(0), rat(1, 2), tau)
    c0 = -(th2 ** 2) * (th3 ** 4 + th4 ** 4) / (mp.mpf(24) * eta3)
    c1 = (th4 ** 2) * (th2 ** 4 + th3 ** 4) / (mp.mpf(24) * eta3)
    c2 = mp.mpc(0, 1) * (th3 ** 2) * (th2 ** 4 - th4 ** 4) / (mp.mpf(24) * eta3)
    return c0, c1, c2, eta3


def eval_all288_potentials(tau, L2_val, pts_288, frame_c):
    """Evaluate all-288 Tr2, V4, V_CW(1), V_CW^(tr) using disjoint 6x6 real-split eigsy."""
    QI, QJ, QK, EPS, BL, EDUAL = frame_c
    c0, c1, c2, eta3 = S_coeffs_frame_c(tau)
    Smat = c0 * QI + c1 * QJ + c2 * QK
    Pmat = [[BL[a].T * EPS * Smat * BL[b] for b in range(3)] for a in range(3)]
    y = mp.im(tau)
    sqy = mp.sqrt(y)
    twopi_eta3 = mp.mpf(2) * mp.pi * eta3
    const_c = mp.pi * mp.log(y) - mp.mpf(2) * mp.pi * (mp.euler + mp.log(mp.pi))
    exp_m2L = mp.exp(-mp.mpf(2) * L2_val)
    twopi_L2 = mp.mpf(2) * mp.pi * L2_val

    th_cache = {}
    wt_cache = {}

    def get_th(ca60, cb60):
        cm = ca60 % 60
        dm = cb60 % 60
        key = (cm, dm)
        if key not in th_cache:
            th_cache[key] = theta_char(rat(cm, 60), rat(dm, 60), tau)
        sh = (cb60 - dm) // 60
        if sh != 0:
            return th_cache[key] * mp.exp(mp.mpc(0, 2) * mp.pi * rat(cm, 60) * mp.mpf(sh))
        return th_cache[key]

    def get_wt(ca60, cb60):
        al60 = (ca60 - 30) % 60
        be60 = (cb60 - 30) % 60
        key = (al60, be60)
        if key not in wt_cache:
            al = rat(al60, 60)
            be = rat(be60, 60)
            fu = F_u_kronecker(al, be, tau)
            th0, dth0 = theta_char(al + rat(1, 2), be + rat(1, 2), tau, True)
            a0 = dth0 / th0
            cval = fu + const_c - mp.pi * (abs(a0) ** 2) * exp_m2L
            arg = twopi_L2 + cval
            wt_cache[key] = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
        return wt_cache[key]

    sectors = ((1, -4, 3), (1, 2, 3), (-3, 6, 1))
    shifts = {"1": (30, 30), "i": (30, 0), "j": (0, 30), "k": (0, 0)}
    tr2 = mp.mpf(0)
    v4 = mp.mpf(0)
    vcw1 = mp.mpf(0)
    all_lams = []
    denom_cw = mp.mpf(64) * (mp.pi ** 2)
    three_halves = rat(3, 2)

    for m, n in pts_288:
        for qL, qR, Nc in sectors:
            ap = (qL + qR) * 2 * m
            bp = (qL + qR) * 2 * n
            am = (qL - qR) * 2 * m
            bm = (qL - qR) * 2 * n
            ef = mp.exp(mp.mpc(0, -2) * mp.pi * rat(qL * m, 30))
            kappas = {"1": mp.mpc(0, -1) * ef, "i": mp.mpc(-1), "j": -ef, "k": mp.mpc(0, 1)}
            m00 = mp.mpc(0)
            m01 = mp.mpc(0)
            m10 = mp.mpc(0)
            m11 = mp.mpc(0)
            for s in ("1", "i", "j", "k"):
                sa, sb = shifts[s]
                csa, csb = ap + sa, bp + sb
                dsa, dsb = am + sa, bm + sb
                if (csa % 60 == 30 and csb % 60 == 30) or (dsa % 60 == 30 and dsb % 60 == 30):
                    continue
                Rs = kappas[s] * get_th(csa, csb) * get_th(dsa, dsb) / twopi_eta3
                wR = get_wt(csa, csb) * Rs
                E = EDUAL[s]
                m00 += wR * E[0, 0]
                m01 += wR * E[0, 1]
                m10 += wR * E[1, 0]
                m11 += wR * E[1, 1]
            Y = mat3_zero()
            for ai in range(3):
                for bi in range(3):
                    P = Pmat[ai][bi]
                    Y[ai][bi] = sqy * (P[0, 0] * m00 + P[0, 1] * m01 + P[1, 0] * m10 + P[1, 1] * m11)
            H = mat3_mul(mat3_dag(Y), Y)
            evals, _ = herm3_eig_real_split(H)
            nc_f = mp.mpf(Nc)
            for ev in evals:
                lam = ev if ev > 0 else mp.mpf(0)
                tr2 += nc_f * lam
                v4 -= nc_f * lam * lam
                if lam > 0:
                    vcw1 -= nc_f * lam * lam * (mp.log(lam) - three_halves) / denom_cw
                    all_lams.append((nc_f, lam))

    # Trace-renormalized V_CW^(tr): mu^2 = Tr2
    # Note: sum Nc lam^2 (ln(lam/Tr2) - 3/2) = sum Nc lam^2 (ln lam - 3/2) - ln(Tr2) sum Nc lam^2
    # Compute directly for independent numerical check!
    vcw_tr = mp.mpf(0)
    for nc_f, lam in all_lams:
        vcw_tr -= nc_f * lam * lam * (mp.log(lam / tr2) - three_halves) / denom_cw

    return {"Tr2": tr2, "V4": v4, "V_CW_1": vcw1, "V_CW_tr": vcw_tr}


def run_rp2(filq_vacua):
    pts_288 = build_E30_prim_mod_pm()
    frame_c = build_quaternion_frame_c()

    # 1. High-precision L2 verification at i, omega_+, tau_mod, and RAW -1/tau_mod (dps = 48)
    mp.mp.dps = 48
    tau_i = mp.mpc(0, 1)
    tau_om = mp.mpc(rat(1, 2), mp.sqrt(mp.mpf(3)) / mp.mpf(2))
    tau_mod = mp.mpc(rat(1, 4), rat(6, 5))
    tau_arc = mp.exp(mp.mpc(0, 5) * mp.pi / mp.mpf(12))

    L2_i, Ci, Bi, g22_i, g12_i = solve_L2_raw(tau_i, high_prec=True)
    L2_om, Com, Bom, g22_om, g12_om = solve_L2_raw(tau_om, high_prec=True)
    Ci_exact = mp.log(mp.mpf(8) * mp.sqrt(mp.mpf(2) * mp.pi) / (mp.gamma(rat(1, 4)) ** 2))
    Com_exact = mp.log(
        mp.power(mp.mpf(2), rat(7, 3)) * mp.sqrt(mp.mpf(3)) * mp.pi / (mp.gamma(rat(1, 3)) ** 3)
    )
    L2_i_err = abs(L2_i - (mp.pi - Ci_exact))
    L2_om_err = abs(L2_om - (mp.pi - Com_exact))

    L2_mod, C_mod, B_mod, g22_mod, g12_mod = solve_L2_raw(tau_mod, high_prec=True)
    L2_S_raw, _, _, g22_S_raw, g12_S_raw = solve_L2_raw(-mp.mpc(1) / tau_mod, high_prec=True)
    L2_S_fd, _, _, _, _ = solve_L2_fd_covariant(-mp.mpc(1) / tau_mod, high_prec=True)
    L2_T_fd, _, _, _, _ = solve_L2_fd_covariant(tau_mod + mp.mpf(1), high_prec=True)
    raw_S_cocycle_err = abs(L2_S_raw - (L2_mod + mp.log(abs(tau_mod))))
    fd_S_cocycle_err = abs(L2_S_fd - (L2_mod + mp.log(abs(tau_mod))))

    # T and S invariance of ALL-288 fermion potentials at tau_mod (BOTH raw L2 AND FD-covariant L2!)
    r_mod = eval_all288_potentials(tau_mod, L2_mod, pts_288, frame_c)
    r_mod_T = eval_all288_potentials(tau_mod + mp.mpf(1), L2_T_fd, pts_288, frame_c)
    r_mod_S_fd = eval_all288_potentials(-mp.mpc(1) / tau_mod, L2_S_fd, pts_288, frame_c)
    r_mod_S_raw = eval_all288_potentials(-mp.mpc(1) / tau_mod, L2_S_raw, pts_288, frame_c)

    mod_inv = {}
    mod_inv_ok = True
    for k in ("Tr2", "V4", "V_CW_1", "V_CW_tr"):
        eT = abs(r_mod_T[k] - r_mod[k]) / abs(r_mod[k])
        eS_fd = abs(r_mod_S_fd[k] - r_mod[k]) / abs(r_mod[k])
        eS_raw = abs(r_mod_S_raw[k] - r_mod[k]) / abs(r_mod[k])
        ok = bool(eT < pow10(-25) and eS_fd < pow10(-25) and eS_raw < pow10(-25))
        mod_inv_ok = mod_inv_ok and ok
        mod_inv[k] = {
            "val_tau_mod": fmt(r_mod[k], 35),
            "T_rel_err": fmt(eT, 10),
            "S_fd_rel_err": fmt(eS_fd, 10),
            "S_raw_rel_err": fmt(eS_raw, 10),
            "pass_lt_1e25": ok,
        }

    # 2. Switch to dps = 30 for fast accurate phase-diagram scan & optimization
    mp.mp.dps = 30
    tau_i = mp.mpc(0, 1)
    tau_om = mp.mpc(rat(1, 2), mp.sqrt(mp.mpf(3)) / mp.mpf(2))
    tau_arc = mp.exp(mp.mpc(0, 5) * mp.pi / mp.mpf(12))

    # Cache L2 and all288 evaluations
    eval_cache = {}

    def get_all288(tau_pt, hp=False):
        key = (mp.nstr(mp.re(tau_pt), 20), mp.nstr(mp.im(tau_pt), 20), hp)
        if key not in eval_cache:
            L2v, Cv, Bv, _, _ = solve_L2_fd_covariant(tau_pt, high_prec=hp)
            res = eval_all288_potentials(tau_pt, L2v, pts_288, frame_c)
            res["L2"] = L2v
            res["C"] = Cv
            res["B"] = Bv
            eval_cache[key] = res
        return eval_cache[key]

    # Key points: omega_+, arc, i, 2i, 4i
    p_om = get_all288(tau_om)
    p_arc = get_all288(tau_arc)
    p_i = get_all288(tau_i)
    p_2i = get_all288(mp.mpc(0, 2))
    p_4i = get_all288(mp.mpc(0, 4))

    # Theorem P2-A: Dynamical trace-scale global stabilization
    p2a_pass = bool(
        p_i["V_CW_tr"] > 0
        and p_om["V_CW_tr"] > 0
        and p_arc["V_CW_tr"] > 0
        and p_i["V_CW_tr"] < p_om["V_CW_tr"] < p_arc["V_CW_tr"]
        and p_i["V_CW_tr"] < p_2i["V_CW_tr"] < p_4i["V_CW_tr"]
        and p_arc["V4"] < p_i["V4"]
        and p_arc["V4"] < p_om["V4"]
    )

    # Theorem P2-B: Polynomial Casimir no-go & orbifold transition
    Ei3 = E_chowla_selberg(tau_i, 3)
    Eom3 = E_chowla_selberg(tau_om, 3)
    E4i3 = E_chowla_selberg(mp.mpc(0, 4), 3)
    cB_crit = (p_om["V_CW_1"] - p_i["V_CW_1"]) / (Ei3 - Eom3)
    casimir_4i = p_4i["V_CW_1"] + mp.mpf(100) * E4i3
    p2b_pass = bool(cB_crit > 0 and casimir_4i < -pow10(8))

    # Theorem P2-C: Globally stable coupled vacuum V_tot(tau; cF) = V_FILQ,3(tau) + cF V_CW(1; tau)
    def V_tot(tau_pt, cF, hp=False):
        return V_FILQ(tau_pt, 3) + mp.mpf(cF) * get_all288(tau_pt, hp=hp)["V_CW_1"]

    tau_f3 = filq_vacua[3]
    v_tot_f3_70 = V_tot(tau_f3, 70)
    p_h4i = get_all288(mp.mpc(rat(1, 2), mp.mpf(4)))
    p_h5i = get_all288(mp.mpc(rat(1, 2), mp.mpf(5)))
    v_tot_h4i_70 = V_FILQ(mp.mpc(rat(1, 2), mp.mpf(4)), 3) + mp.mpf(70) * p_h4i["V_CW_1"]
    v_tot_h4i_100 = V_FILQ(mp.mpc(rat(1, 2), mp.mpf(4)), 3) + mp.mpf(100) * p_h4i["V_CW_1"]
    v_tot_h5i_100 = V_FILQ(mp.mpc(rat(1, 2), mp.mpf(5)), 3) + mp.mpf(100) * p_h5i["V_CW_1"]

    # Locate exact 1D minimum on x=1/2 for cF=70 via golden-section bracket + parabolic/secant refinement
    # Bracket on [29/10, 39/10] (independent of target y*)
    a_y = rat(29, 10)
    b_y = rat(39, 10)
    phi_g = (mp.sqrt(mp.mpf(5)) - mp.mpf(1)) / mp.mpf(2)
    c_y = b_y - phi_g * (b_y - a_y)
    d_y = a_y + phi_g * (b_y - a_y)
    fc = V_tot(mp.mpc(rat(1, 2), c_y), 70)
    fd = V_tot(mp.mpc(rat(1, 2), d_y), 70)
    for _ in range(18):
        if fc < fd:
            b_y = d_y
            d_y = c_y
            fd = fc
            c_y = b_y - phi_g * (b_y - a_y)
            fc = V_tot(mp.mpc(rat(1, 2), c_y), 70)
        else:
            a_y = c_y
            c_y = d_y
            fc = fd
            d_y = a_y + phi_g * (b_y - a_y)
            fd = V_tot(mp.mpc(rat(1, 2), d_y), 70)
    y_star = rat(1, 2) * (a_y + b_y)

    # Polish y_star with 4th-order central-difference Newton steps to |g_y| < 1e-4
    hy_n = pow10(-5)
    for _ in range(6):
        v0 = V_tot(mp.mpc(rat(1, 2), y_star), 70)
        vp1 = V_tot(mp.mpc(rat(1, 2), y_star + hy_n), 70)
        vm1 = V_tot(mp.mpc(rat(1, 2), y_star - hy_n), 70)
        vp2 = V_tot(mp.mpc(rat(1, 2), y_star + mp.mpf(2) * hy_n), 70)
        vm2 = V_tot(mp.mpc(rat(1, 2), y_star - mp.mpf(2) * hy_n), 70)
        gy = (-vp2 + mp.mpf(8) * vp1 - mp.mpf(8) * vm1 + vm2) / (mp.mpf(12) * hy_n)
        hyy = (-vp2 + mp.mpf(16) * vp1 - mp.mpf(30) * v0 + mp.mpf(16) * vm1 - vm2) / (
            mp.mpf(12) * hy_n * hy_n
        )
        step = gy / hyy
        y_star -= step
        if abs(step) < pow10(-12):
            break

    tau_tot_70 = mp.mpc(rat(1, 2), y_star)
    # 2D gradient & Hessian at tau_tot_70 using hx = 1/50 and 4th-order hy = 1e-5
    hx_p2c = rat(1, 50)
    hy_p2c = pow10(-5)
    v_st = V_tot(tau_tot_70, 70)
    v_xp = V_tot(mp.mpc(rat(1, 2) + hx_p2c, y_star), 70)
    v_xm = V_tot(mp.mpc(rat(1, 2) - hx_p2c, y_star), 70)
    v_yp1 = V_tot(mp.mpc(rat(1, 2), y_star + hy_p2c), 70)
    v_ym1 = V_tot(mp.mpc(rat(1, 2), y_star - hy_p2c), 70)
    v_yp2 = V_tot(mp.mpc(rat(1, 2), y_star + mp.mpf(2) * hy_p2c), 70)
    v_ym2 = V_tot(mp.mpc(rat(1, 2), y_star - mp.mpf(2) * hy_p2c), 70)
    gx_st = (v_xp - v_xm) / (mp.mpf(2) * hx_p2c)
    gy_st = (-v_yp2 + mp.mpf(8) * v_yp1 - mp.mpf(8) * v_ym1 + v_ym2) / (mp.mpf(12) * hy_p2c)
    vxx_st = (v_xp - mp.mpf(2) * v_st + v_xm) / (hx_p2c * hx_p2c)
    vyy_st = (-v_yp2 + mp.mpf(16) * v_yp1 - mp.mpf(30) * v_st + mp.mpf(16) * v_ym1 - v_ym2) / (
        mp.mpf(12) * hy_p2c * hy_p2c
    )

    # Compare against (0, y_star) saddle!
    v_0y = V_tot(mp.mpc(mp.mpf(0), y_star), 70)
    v_0y_xp = V_tot(mp.mpc(hx_p2c, y_star), 70)
    v_0y_xm = V_tot(mp.mpc(-hx_p2c, y_star), 70)
    vxx_0y = (v_0y_xp - mp.mpf(2) * v_0y + v_0y_xm) / (hx_p2c * hx_p2c)

    # Also compute exact c_F^crit (first-order transition threshold on x=1/2 vs tau_FILQ3^*)
    # At y on x=1/2, V_tot(1/2+iy; cF) == V_tot(tau_FILQ3^*; cF) => cF(y) = (Vf3(y) - Vf3(f3)) / (Vcw(f3) - Vcw(y))
    vf3_at_f3 = V_FILQ(tau_f3, 3)
    vcw_at_f3 = get_all288(tau_f3)["V_CW_1"]

    def cF_eq(y_val):
        t = mp.mpc(rat(1, 2), y_val)
        return (V_FILQ(t, 3) - vf3_at_f3) / (vcw_at_f3 - get_all288(t)["V_CW_1"])

    ca, cb = rat(27, 10), rat(34, 10)
    cc = cb - phi_g * (cb - ca)
    cd = ca + phi_g * (cb - ca)
    fcc, fcd = cF_eq(cc), cF_eq(cd)
    for _ in range(14):
        if fcc < fcd:
            cb, cd, fcd = cd, cc, fcc
            cc = cb - phi_g * (cb - ca)
            fcc = cF_eq(cc)
        else:
            ca, cc, fcc = cc, cd, fcd
            cd = ca + phi_g * (cb - ca)
            fcd = cF_eq(cd)
    y_crit = rat(1, 2) * (ca + cb)
    cF_crit = cF_eq(y_crit)

    p2c_pass = bool(
        v_st < -mp.mpf(6) * pow10(6)
        and abs(gx_st) < pow10(-8)
        and abs(gy_st) < pow10(-1)
        and vxx_st > 0
        and vyy_st > 0
        and vxx_0y < 0
        and v_st < v_0y
        and v_tot_f3_70 > 0
        and v_tot_h4i_70 > mp.mpf(4) * pow10(9)
        and v_tot_h4i_100 < 0
        and v_tot_h5i_100 > pow10(12)
    )

    rg2_pass = bool(
        L2_i_err < pow10(-25)
        and L2_om_err < pow10(-25)
        and raw_S_cocycle_err < pow10(-25)
        and fd_S_cocycle_err < pow10(-30)
        and mod_inv_ok
        and p2a_pass
        and p2b_pass
        and p2c_pass
    )

    # Also store exact L2, C, B at tau_tot_70 and tau_FILQ1^* for RP3
    tau_f1 = filq_vacua[1]
    L2_f1, C_f1, B_f1, _, _ = solve_L2_fd_covariant(tau_f1, high_prec=False)
    p_tot_70 = get_all288(tau_tot_70)

    rp2_out = {
        "L2_solver_checks": {
            "L2_i": fmt(L2_i, 35),
            "L2_i_err_vs_exact": fmt(L2_i_err, 10),
            "L2_omega": fmt(L2_om, 35),
            "L2_omega_err_vs_exact": fmt(L2_om_err, 10),
            "L2_tau_mod": fmt(L2_mod, 35),
            "L2_S_tau_mod_raw": fmt(L2_S_raw, 35),
            "raw_S_cocycle_err": fmt(raw_S_cocycle_err, 10),
            "fd_S_cocycle_err": fmt(fd_S_cocycle_err, 10),
            "g22_i": fmt(g22_i, 8),
            "g22_omega": fmt(g22_om, 8),
            "g22_S_raw": fmt(g22_S_raw, 8),
        },
        "all288_modular_invariance": mod_inv,
        "orbifold_scan": {
            "omega": {k: fmt(p_om[k], 25) for k in ("L2", "Tr2", "V4", "V_CW_1", "V_CW_tr")},
            "arc": {k: fmt(p_arc[k], 25) for k in ("L2", "Tr2", "V4", "V_CW_1", "V_CW_tr")},
            "i": {k: fmt(p_i[k], 25) for k in ("L2", "Tr2", "V4", "V_CW_1", "V_CW_tr")},
            "2i": {k: fmt(p_2i[k], 25) for k in ("L2", "Tr2", "V4", "V_CW_1", "V_CW_tr")},
            "4i": {k: fmt(p_4i[k], 25) for k in ("L2", "Tr2", "V4", "V_CW_1", "V_CW_tr")},
        },
        "P2_A_trace_stabilization": {"pass": p2a_pass},
        "P2_B_casimir_nogo": {
            "cB_crit": fmt(cB_crit, 25),
            "V_CW1_plus_100E3_at_4i": fmt(casimir_4i, 25),
            "pass": p2b_pass,
        },
        "P2_C_coupled_vacuum": {
            "cF_crit": fmt(cF_crit, 20),
            "y_crit": fmt(y_crit, 20),
            "y_star_cF70": fmt(y_star, 25),
            "L2_star_cF70": fmt(p_tot_70["L2"], 25),
            "V_star_cF70": fmt(v_st, 25),
            "g_x": fmt(gx_st, 10),
            "g_y": fmt(gy_st, 10),
            "V_xx_half": fmt(vxx_st, 20),
            "V_yy_half": fmt(vyy_st, 20),
            "V_at_0_ystar": fmt(v_0y, 25),
            "V_xx_at_0_ystar": fmt(vxx_0y, 20),
            "V_tot_at_tau_FILQ3_cF70": fmt(v_tot_f3_70, 25),
            "V_tot_at_half_4i_cF70": fmt(v_tot_h4i_70, 25),
            "V_tot_at_half_4i_cF100": fmt(v_tot_h4i_100, 25),
            "V_tot_at_half_5i_cF100": fmt(v_tot_h5i_100, 25),
            "pass": p2c_pass,
        },
        "RG2_pass": rg2_pass,
    }
    vacua_data = {
        "omega": {"tau": tau_om, "L2": L2_om, "C": Com, "B": Bom},
        "tau_FILQ1": {"tau": tau_f1, "L2": L2_f1, "C": C_f1, "B": B_f1},
        "tau_tot_70": {
            "tau": tau_tot_70,
            "L2": p_tot_70["L2"],
            "C": p_tot_70["C"],
            "B": p_tot_70["B"],
        },
    }
    return rp2_out, vacua_data, frame_c, pts_288


# ============================================================================
# MODULE RP3: GUARDRAIL 4 BENCHMARKS, CURVED DIRAC G_{s=1/2}, GL4 RGE, PMNS, HAAR
# ============================================================================

def rge_rhs_2hdm_type2_soft(state, include_2loop=True, mode="2hdm2"):
    """
    Full 3x3 matrix 2-loop Type-II 2HDM (arXiv:1503.08216 App. A, GUT g_Y^2 = 3/5 g1^2)
    + Branco/CE quartics (l1, l2, l3, l4, l5=0)
    + Martin (hep-ph/9709356 Eqs. 6.5.24-6.5.30) 3x3 Hermitian soft-mass RGEs (Ma=0, A0=0).
    Convention: Y_f has rows = LH doublet (Q_L, L_L), cols = RH singlet (u_R, d_R, e_R).
    """
    g1, g2, g3, l1, l2, l3, l4, Yu, Yd, Ye, mHu2, mHd2, MQ2, Mu2, Md2, ML2, Me2 = state
    g1_2 = g1 * g1
    g2_2 = g2 * g2
    g3_2 = g3 * g3
    gY_2 = rat(3, 5) * g1_2
    g1_4 = g1_2 * g1_2
    g2_4 = g2_2 * g2_2
    g3_4 = g3_2 * g3_2
    gY_4 = gY_2 * gY_2

    Yu_dag = mat3_dag(Yu)
    Yd_dag = mat3_dag(Yd)
    Ye_dag = mat3_dag(Ye)
    Su = mat3_mul(Yu, Yu_dag)
    Sd = mat3_mul(Yd, Yd_dag)
    Se = mat3_mul(Ye, Ye_dag)
    Su2 = mat3_mul(Su, Su)
    Sd2 = mat3_mul(Sd, Sd)
    Se2 = mat3_mul(Se, Se)
    SuSd = mat3_mul(Su, Sd)
    SdSu = mat3_mul(Sd, Su)

    Tu = mp.re(mat3_tr(Su))
    Td = mp.re(mat3_tr(Sd))
    Te = mp.re(mat3_tr(Se))
    TrSu2 = mp.re(mat3_tr(Su2))
    TrSd2 = mp.re(mat3_tr(Sd2))
    TrSe2 = mp.re(mat3_tr(Se2))
    TrSuSd = mp.re(mat3_tr(SuSd))
    TrSu3 = mp.re(mat3_tr(mat3_mul(Su2, Su)))
    TrSd3 = mp.re(mat3_tr(mat3_mul(Sd2, Sd)))
    TrSe3 = mp.re(mat3_tr(mat3_mul(Se2, Se)))
    TrSu2Sd = mp.re(mat3_tr(mat3_mul(Su2, Sd)))
    TrSd2Su = mp.re(mat3_tr(mat3_mul(Sd2, Su)))

    inv16 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
    inv16_2 = inv16 * inv16
    I3 = mat3_eye()

    # ---- Gauge Couplings ----
    if mode == "sm":
        b1_1, b2_1, b3_1 = rat(41, 10), rat(-19, 6), mp.mpf(-7)
    else:
        b1_1, b2_1, b3_1 = rat(21, 5), mp.mpf(-3), mp.mpf(-7)
    dg1 = b1_1 * g1_2 * g1 * inv16
    dg2 = b2_1 * g2_2 * g2 * inv16
    dg3 = b3_1 * g3_2 * g3 * inv16
    if include_2loop and mode != "sm":
        dg1 += (
            g1_2 * g1
            * (rat(104, 25) * g1_2 + rat(18, 5) * g2_2 + rat(44, 5) * g3_2 - rat(17, 10) * Tu - rat(1, 2) * Td - rat(3, 2) * Te)
            * inv16_2
        )
        dg2 += (
            g2_2 * g2
            * (rat(6, 5) * g1_2 + mp.mpf(8) * g2_2 + mp.mpf(12) * g3_2 - rat(3, 2) * Tu - rat(3, 2) * Td - rat(1, 2) * Te)
            * inv16_2
        )
        dg3 += (
            g3_2 * g3
            * (rat(11, 10) * g1_2 + rat(9, 2) * g2_2 - mp.mpf(26) * g3_2 - mp.mpf(2) * Tu - mp.mpf(2) * Td)
            * inv16_2
        )

    # ---- Quartics (arXiv:1503.08216 App. A, Type II, l5=0, gY^2 = 3/5 g1^2) ----
    l1_2 = l1 * l1
    l2_2 = l2 * l2
    l3_2 = l3 * l3
    l4_2 = l4 * l4
    mix_34 = mp.mpf(2) * l3_2 + mp.mpf(2) * l3 * l4 + l4_2

    bl1_1 = (
        rat(3, 4) * gY_4 + rat(3, 2) * gY_2 * g2_2 + rat(9, 4) * g2_4
        - mp.mpf(3) * gY_2 * l1 - mp.mpf(9) * g2_2 * l1
        + mp.mpf(12) * l1_2 + mp.mpf(4) * l3_2 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4_2
        - mp.mpf(12) * TrSd2 - mp.mpf(4) * TrSe2 + (mp.mpf(12) * Td + mp.mpf(4) * Te) * l1
    )
    bl2_1 = (
        rat(3, 4) * gY_4 + rat(3, 2) * gY_2 * g2_2 + rat(9, 4) * g2_4
        - mp.mpf(3) * gY_2 * l2 - mp.mpf(9) * g2_2 * l2
        + mp.mpf(12) * l2_2 + mp.mpf(4) * l3_2 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4_2
        - mp.mpf(12) * TrSu2 + mp.mpf(12) * Tu * l2
    )
    bl3_1 = (
        rat(3, 4) * gY_4 - rat(3, 2) * gY_2 * g2_2 + rat(9, 4) * g2_4
        - (mp.mpf(3) * gY_2 + mp.mpf(9) * g2_2) * l3
        + (l1 + l2) * (mp.mpf(6) * l3 + mp.mpf(2) * l4) + mp.mpf(4) * l3_2 + mp.mpf(2) * l4_2
        - mp.mpf(12) * TrSuSd + (mp.mpf(6) * Td + mp.mpf(6) * Tu + mp.mpf(2) * Te) * l3
    )
    bl4_1 = (
        mp.mpf(3) * gY_2 * g2_2 - (mp.mpf(3) * gY_2 + mp.mpf(9) * g2_2) * l4
        + mp.mpf(2) * l1 * l4 + mp.mpf(2) * l2 * l4 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4_2
        + mp.mpf(12) * TrSuSd + (mp.mpf(6) * Td + mp.mpf(6) * Tu + mp.mpf(2) * Te) * l4
    )

    dl1 = bl1_1 * inv16
    dl2 = bl2_1 * inv16
    dl3 = bl3_1 * inv16
    dl4 = bl4_1 * inv16

    if include_2loop and mode != "sm":
        gY_6 = gY_4 * gY_2
        g2_6 = g2_4 * g2_2
        # Bosonic 2-loop quartics
        def bl12_bos(la):
            return (
                rat(-131, 8) * gY_6 - rat(191, 8) * gY_4 * g2_2 - rat(101, 8) * gY_2 * g2_4 + rat(291, 8) * g2_6
                + gY_4 * (rat(217, 8) * la + mp.mpf(5) * l3 + rat(5, 2) * l4)
                + gY_2 * g2_2 * (rat(39, 4) * la + mp.mpf(5) * l4)
                + g2_4 * (rat(-51, 8) * la + mp.mpf(15) * l3 + rat(15, 2) * l4)
                + gY_2 * (mp.mpf(18) * la * la + mp.mpf(8) * l3_2 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4_2)
                + g2_2 * (mp.mpf(54) * la * la + mp.mpf(6) * ((mp.mpf(2) * l3 + l4) ** 2))
                - mp.mpf(78) * (la ** 3)
                - la * (mp.mpf(20) * l3_2 + mp.mpf(20) * l3 * l4 + mp.mpf(12) * l4_2)
                - mp.mpf(16) * (l3 ** 3) - mp.mpf(24) * l3_2 * l4 - mp.mpf(32) * l3 * l4_2 - mp.mpf(12) * (l4 ** 3)
            )

        bl1_2 = (
            bl12_bos(l1)
            + gY_4 * (rat(5, 2) * Td - rat(25, 2) * Te)
            + gY_2 * g2_2 * (mp.mpf(9) * Td + mp.mpf(11) * Te)
            - g2_4 * (rat(9, 2) * Td + rat(3, 2) * Te)
            + gY_2 * (rat(8, 3) * TrSd2 - mp.mpf(8) * TrSe2 + rat(25, 6) * Td * l1 + rat(25, 2) * Te * l1)
            + g2_2 * (rat(45, 2) * Td * l1 + rat(15, 2) * Te * l1)
            - g3_2 * (mp.mpf(64) * TrSd2 - mp.mpf(80) * Td * l1)
            + mp.mpf(60) * TrSd3 + mp.mpf(12) * TrSd2Su + mp.mpf(20) * TrSe3
            - (mp.mpf(3) * TrSd2 + mp.mpf(9) * TrSuSd + TrSe2) * l1
            - mp.mpf(72) * Td * l1_2 - mp.mpf(12) * Tu * mix_34 - mp.mpf(24) * Te * l1_2
        )
        bl2_2 = (
            bl12_bos(l2)
            - rat(19, 2) * gY_4 * Tu + mp.mpf(21) * gY_2 * g2_2 * Tu - rat(9, 2) * g2_4 * Tu
            + gY_2 * (rat(-16, 3) * TrSu2 + rat(85, 6) * Tu * l2)
            + rat(45, 2) * g2_2 * Tu * l2
            - g3_2 * (mp.mpf(64) * TrSu2 - mp.mpf(80) * Tu * l2)
            + mp.mpf(12) * TrSu2Sd + mp.mpf(60) * TrSu3
            - (mp.mpf(9) * TrSuSd + mp.mpf(3) * TrSu2) * l2
            - (mp.mpf(12) * Td + mp.mpf(4) * Te) * mix_34 - mp.mpf(72) * Tu * l2_2
        )
        bl3_2 = (
            rat(-131, 8) * gY_6 + rat(101, 8) * gY_4 * g2_2 + rat(11, 8) * gY_2 * g2_4 + rat(291, 8) * g2_6
            + gY_4 * (rat(15, 4) * (l1 + l2) + rat(197, 8) * l3 + rat(5, 2) * l4)
            - gY_2 * g2_2 * (rat(5, 2) * (l1 + l2) - rat(11, 4) * l3 + mp.mpf(3) * l4)
            + g2_4 * (rat(45, 4) * (l1 + l2) - rat(111, 8) * l3 + rat(15, 2) * l4)
            + gY_2 * ((l1 + l2) * (mp.mpf(12) * l3 + mp.mpf(4) * l4) + mp.mpf(2) * l3_2 - mp.mpf(2) * l4_2)
            + g2_2 * ((l1 + l2) * (mp.mpf(36) * l3 + mp.mpf(18) * l4) + mp.mpf(6) * ((l3 - l4) ** 2))
            - (l1_2 + l2_2) * (mp.mpf(15) * l3 + mp.mpf(4) * l4)
            - (l1 + l2) * (mp.mpf(36) * l3_2 + mp.mpf(16) * l3 * l4 + mp.mpf(14) * l4_2)
            - mp.mpf(12) * (l3 ** 3) - mp.mpf(4) * l3_2 * l4 - mp.mpf(16) * l3 * l4_2 - mp.mpf(12) * (l4 ** 3)
            # Fermionic Type II
            + gY_4 * (rat(5, 4) * Td - rat(19, 4) * Tu - rat(25, 4) * Te)
            - gY_2 * g2_2 * (rat(9, 2) * Td + rat(21, 2) * Tu + rat(11, 2) * Te)
            - g2_4 * (rat(9, 4) * Td + rat(9, 4) * Tu + rat(3, 4) * Te)
            + gY_2 * (rat(-4, 3) * TrSuSd + (rat(25, 12) * Td + rat(85, 12) * Tu + rat(25, 4) * Te) * l3)
            + g2_2 * (rat(45, 4) * Td + rat(45, 4) * Tu + rat(15, 4) * Te) * l3
            + g3_2 * (-mp.mpf(64) * TrSuSd + mp.mpf(40) * (Td + Tu) * l3)
            + mp.mpf(36) * TrSd2Su + mp.mpf(36) * TrSu2Sd
            + (rat(-27, 2) * TrSd2 + mp.mpf(15) * TrSuSd - rat(27, 2) * TrSu2 - rat(9, 2) * TrSe2) * l3
            - (mp.mpf(6) * Td * l1 + mp.mpf(6) * Tu * l2 + mp.mpf(2) * Te * l1) * (mp.mpf(6) * l3 + mp.mpf(2) * l4)
            - (mp.mpf(6) * Td + mp.mpf(6) * Tu + mp.mpf(2) * Te) * (mp.mpf(2) * l3_2 + l4_2)
        )
        bl4_2 = (
            rat(-73, 2) * gY_4 * g2_2 - mp.mpf(14) * gY_2 * g2_4
            + rat(157, 8) * gY_4 * l4
            + gY_2 * g2_2 * (mp.mpf(5) * (l1 + l2) + mp.mpf(2) * l3 + rat(51, 4) * l4)
            - rat(231, 8) * g2_4 * l4
            + gY_2 * (mp.mpf(4) * (l1 + l2 + l3) * l4 + mp.mpf(8) * l4_2)
            + g2_2 * (mp.mpf(36) * l3 * l4 + mp.mpf(18) * l4_2)
            - mp.mpf(7) * (l1_2 + l2_2) * l4 - (l1 + l2) * (mp.mpf(40) * l3 * l4 + mp.mpf(20) * l4_2)
            - mp.mpf(28) * l3_2 * l4 - mp.mpf(28) * l3 * l4_2
            # Fermionic Type II
            + gY_2 * g2_2 * (mp.mpf(9) * Td + mp.mpf(21) * Tu + mp.mpf(11) * Te)
            + gY_2 * (rat(4, 3) * TrSuSd + (rat(25, 12) * Td + rat(85, 12) * Tu + rat(25, 4) * Te) * l4)
            + g2_2 * (rat(45, 4) * Td + rat(45, 4) * Tu + rat(15, 4) * Te) * l4
            + g3_2 * (mp.mpf(64) * TrSuSd + mp.mpf(40) * (Td + Tu) * l4)
            - mp.mpf(24) * TrSu2Sd - mp.mpf(24) * TrSd2Su
            - rat(27, 2) * TrSd2 * l4 - TrSuSd * (mp.mpf(24) * l3 + mp.mpf(33) * l4)
            - rat(27, 2) * TrSu2 * l4 - rat(9, 2) * TrSe2 * l4
            - (mp.mpf(12) * Td * l1 + mp.mpf(12) * Tu * l2 + mp.mpf(4) * Te * l1) * l4
            - (mp.mpf(12) * Td + mp.mpf(12) * Tu + mp.mpf(4) * Te) * (mp.mpf(2) * l3 * l4 + l4_2)
        )
        dl1 += bl1_2 * inv16_2
        dl2 += bl2_2 * inv16_2
        dl3 += bl3_2 * inv16_2
        dl4 += bl4_2 * inv16_2

    # ---- Yukawa Matrices (1-loop + 2-loop Type-II 2HDM, arXiv:1503.08216 App. A) ----
    if mode == "sm":
        c_cross = rat(-3, 2)
        Tu_leg = mp.mpf(3) * Tu + mp.mpf(3) * Td + Te
        Td_leg = Tu_leg
    else:
        c_cross = rat(1, 2)
        Tu_leg = mp.mpf(3) * Tu
        Td_leg = mp.mpf(3) * Td + Te

    M_u1 = mat3_add(
        mat3_scale(Tu_leg - (rat(17, 20) * g1_2 + rat(9, 4) * g2_2 + mp.mpf(8) * g3_2), I3),
        mat3_add(mat3_scale(rat(3, 2), Su), mat3_scale(c_cross, Sd)),
    )
    M_d1 = mat3_add(
        mat3_scale(Td_leg - (rat(1, 4) * g1_2 + rat(9, 4) * g2_2 + mp.mpf(8) * g3_2), I3),
        mat3_add(mat3_scale(rat(3, 2), Sd), mat3_scale(c_cross, Su)),
    )
    M_e1 = mat3_add(
        mat3_scale(Td_leg - (rat(9, 4) * g1_2 + rat(9, 4) * g2_2), I3),
        mat3_scale(rat(3, 2), Se),
    )
    dYu = mat3_scale(inv16, mat3_mul(M_u1, Yu))
    dYd = mat3_scale(inv16, mat3_mul(M_d1, Yd))
    dYe = mat3_scale(inv16, mat3_mul(M_e1, Ye))

    if include_2loop and mode != "sm":
        q_mix = l3_2 + l3 * l4 + l4_2
        # beta_{Yu}^{(2)} (GUT g1^2)
        cu_scalar = (
            rat(1267, 600) * g1_4 - rat(9, 20) * g1_2 * g2_2 + rat(19, 15) * g1_2 * g3_2
            - rat(21, 4) * g2_4 + mp.mpf(9) * g2_2 * g3_2 - mp.mpf(108) * g3_4
            + rat(3, 2) * l2_2 + q_mix
            + (rat(17, 8) * g1_2 + rat(45, 8) * g2_2 + mp.mpf(20) * g3_2) * Tu
            - rat(27, 4) * TrSu2 - rat(9, 4) * TrSuSd
        )
        cu_Su = rat(223, 80) * g1_2 + rat(135, 16) * g2_2 + mp.mpf(16) * g3_2 - rat(27, 4) * Tu - mp.mpf(6) * l2
        cu_Sd = (
            rat(-41, 240) * g1_2 + rat(33, 16) * g2_2 + rat(16, 3) * g3_2
            - rat(9, 4) * Td - rat(3, 4) * Te - mp.mpf(2) * l3 + mp.mpf(2) * l4
        )
        M_u2 = mat3_scale(cu_scalar, I3)
        M_u2 = mat3_add(M_u2, mat3_scale(cu_Su, Su))
        M_u2 = mat3_add(M_u2, mat3_scale(cu_Sd, Sd))
        M_u2 = mat3_add(M_u2, mat3_scale(rat(3, 2), Su2))
        M_u2 = mat3_add(M_u2, mat3_scale(rat(-1, 4), Sd2))
        M_u2 = mat3_add(M_u2, mat3_scale(rat(-1, 4), SuSd))
        dYu = mat3_add(dYu, mat3_scale(inv16_2, mat3_mul(M_u2, Yu)))

        # beta_{Yd}^{(2)} (GUT g1^2)
        cd_scalar = (
            rat(-113, 600) * g1_4 - rat(27, 20) * g1_2 * g2_2 + rat(31, 15) * g1_2 * g3_2
            - rat(21, 4) * g2_4 + mp.mpf(9) * g2_2 * g3_2 - mp.mpf(108) * g3_4
            + rat(3, 2) * l1_2 + q_mix
            + (rat(5, 8) * g1_2 + rat(45, 8) * g2_2 + mp.mpf(20) * g3_2) * Td
            + (rat(15, 8) * g1_2 + rat(15, 8) * g2_2) * Te
            - rat(27, 4) * TrSd2 - rat(9, 4) * TrSuSd - rat(9, 4) * TrSe2
        )
        cd_Sd = (
            rat(187, 80) * g1_2 + rat(135, 16) * g2_2 + mp.mpf(16) * g3_2
            - rat(27, 4) * Td - rat(9, 4) * Te - mp.mpf(6) * l1
        )
        cd_Su = (
            rat(-53, 240) * g1_2 + rat(33, 16) * g2_2 + rat(16, 3) * g3_2
            - rat(9, 4) * Tu - mp.mpf(2) * l3 + mp.mpf(2) * l4
        )
        M_d2 = mat3_scale(cd_scalar, I3)
        M_d2 = mat3_add(M_d2, mat3_scale(cd_Sd, Sd))
        M_d2 = mat3_add(M_d2, mat3_scale(cd_Su, Su))
        M_d2 = mat3_add(M_d2, mat3_scale(rat(3, 2), Sd2))
        M_d2 = mat3_add(M_d2, mat3_scale(rat(-1, 4), Su2))
        M_d2 = mat3_add(M_d2, mat3_scale(rat(-1, 4), SdSu))
        dYd = mat3_add(dYd, mat3_scale(inv16_2, mat3_mul(M_d2, Yd)))

        # beta_{Ye}^{(2)} (GUT g1^2)
        ce_scalar = (
            rat(1449, 200) * g1_4 + rat(27, 20) * g1_2 * g2_2 - rat(21, 4) * g2_4
            + rat(3, 2) * l1_2 + q_mix
            + (rat(5, 8) * g1_2 + rat(45, 8) * g2_2 + mp.mpf(20) * g3_2) * Td
            + (rat(15, 8) * g1_2 + rat(15, 8) * g2_2) * Te
            - rat(27, 4) * TrSd2 - rat(9, 4) * TrSuSd - rat(9, 4) * TrSe2
        )
        ce_Se = (
            rat(387, 80) * g1_2 + rat(135, 16) * g2_2
            - rat(27, 4) * Td - rat(9, 4) * Te - mp.mpf(6) * l1
        )
        M_e2 = mat3_scale(ce_scalar, I3)
        M_e2 = mat3_add(M_e2, mat3_scale(ce_Se, Se))
        M_e2 = mat3_add(M_e2, mat3_scale(rat(3, 2), Se2))
        dYe = mat3_add(dYe, mat3_scale(inv16_2, mat3_mul(M_e2, Ye)))

    # ---- Soft Scalar Squared Masses (Martin hep-ph/9709356 Eqs. 6.5.24-6.5.30, Ma=A0=0) ----
    S_tr = (
        mHu2 - mHd2
        + mp.re(mat3_tr(MQ2)) - mp.re(mat3_tr(ML2))
        - mp.mpf(2) * mp.re(mat3_tr(Mu2)) + mp.re(mat3_tr(Md2)) + mp.re(mat3_tr(Me2))
    )
    YuMu2Yud = mat3_mul(mat3_mul(Yu, Mu2), Yu_dag)
    YdMd2Ydd = mat3_mul(mat3_mul(Yd, Md2), Yd_dag)
    YeMe2Yed = mat3_mul(mat3_mul(Ye, Me2), Ye_dag)
    YudMQ2Yu = mat3_mul(mat3_mul(Yu_dag, MQ2), Yu)
    YddMQ2Yd = mat3_mul(mat3_mul(Yd_dag, MQ2), Yd)
    YedML2Ye = mat3_mul(mat3_mul(Ye_dag, ML2), Ye)
    Hu_R = mat3_mul(Yu_dag, Yu)
    Hd_R = mat3_mul(Yd_dag, Yd)
    He_R = mat3_mul(Ye_dag, Ye)

    tr_Xu = mp.re(mHu2 * Tu + mat3_tr(mat3_mul(MQ2, Su)) + mat3_tr(YuMu2Yud))
    tr_Xd = mp.re(mHd2 * Td + mat3_tr(mat3_mul(MQ2, Sd)) + mat3_tr(YdMd2Ydd))
    tr_Xe = mp.re(mHd2 * Te + mat3_tr(mat3_mul(ML2, Se)) + mat3_tr(YeMe2Yed))

    dmHu2 = (mp.mpf(6) * tr_Xu + rat(3, 5) * g1_2 * S_tr) * inv16
    dmHd2 = (mp.mpf(6) * tr_Xd + mp.mpf(2) * tr_Xe - rat(3, 5) * g1_2 * S_tr) * inv16

    dMQ2 = mat3_add(
        mat3_add(mat3_mul(MQ2, Su), mat3_mul(Su, MQ2)),
        mat3_add(mat3_scale(mp.mpf(2), YuMu2Yud), mat3_scale(mp.mpf(2) * mHu2, Su)),
    )
    dMQ2 = mat3_add(
        dMQ2,
        mat3_add(
            mat3_add(mat3_mul(MQ2, Sd), mat3_mul(Sd, MQ2)),
            mat3_add(mat3_scale(mp.mpf(2), YdMd2Ydd), mat3_scale(mp.mpf(2) * mHd2, Sd)),
        ),
    )
    dMQ2 = mat3_scale(inv16, mat3_add(dMQ2, mat3_scale(rat(1, 5) * g1_2 * S_tr, I3)))

    dMu2 = mat3_add(
        mat3_scale(mp.mpf(2), mat3_add(mat3_mul(Mu2, Hu_R), mat3_mul(Hu_R, Mu2))),
        mat3_add(mat3_scale(mp.mpf(4), YudMQ2Yu), mat3_scale(mp.mpf(4) * mHu2, Hu_R)),
    )
    dMu2 = mat3_scale(inv16, mat3_add(dMu2, mat3_scale(rat(-4, 5) * g1_2 * S_tr, I3)))

    dMd2 = mat3_add(
        mat3_scale(mp.mpf(2), mat3_add(mat3_mul(Md2, Hd_R), mat3_mul(Hd_R, Md2))),
        mat3_add(mat3_scale(mp.mpf(4), YddMQ2Yd), mat3_scale(mp.mpf(4) * mHd2, Hd_R)),
    )
    dMd2 = mat3_scale(inv16, mat3_add(dMd2, mat3_scale(rat(2, 5) * g1_2 * S_tr, I3)))

    dML2 = mat3_add(
        mat3_add(mat3_mul(ML2, Se), mat3_mul(Se, ML2)),
        mat3_add(mat3_scale(mp.mpf(2), YeMe2Yed), mat3_scale(mp.mpf(2) * mHd2, Se)),
    )
    dML2 = mat3_scale(inv16, mat3_add(dML2, mat3_scale(rat(-3, 5) * g1_2 * S_tr, I3)))

    dMe2 = mat3_add(
        mat3_scale(mp.mpf(2), mat3_add(mat3_mul(Me2, He_R), mat3_mul(He_R, Me2))),
        mat3_add(mat3_scale(mp.mpf(4), YedML2Ye), mat3_scale(mp.mpf(4) * mHd2, He_R)),
    )
    dMe2 = mat3_scale(inv16, mat3_add(dMe2, mat3_scale(rat(6, 5) * g1_2 * S_tr, I3)))

    return (dg1, dg2, dg3, dl1, dl2, dl3, dl4, dYu, dYd, dYe, dmHu2, dmHd2, dMQ2, dMu2, dMd2, dML2, dMe2)


def state_lincomb(s0, c1, k1, c2, k2):
    out = []
    for idx in range(len(s0)):
        if idx in (7, 8, 9, 12, 13, 14, 15, 16):
            A = s0[idx]
            B = k1[idx]
            C = k2[idx]
            out.append([[A[i][j] + c1 * B[i][j] + c2 * C[i][j] for j in range(3)] for i in range(3)])
        else:
            out.append(s0[idx] + c1 * k1[idx] + c2 * k2[idx])
    return tuple(out)


def state_diff_norm(a, b):
    mx = mp.mpf(0)
    for idx in range(len(a)):
        if idx in (7, 8, 9, 12, 13, 14, 15, 16):
            for i in range(3):
                for j in range(3):
                    d = abs(a[idx][i][j] - b[idx][i][j])
                    if d > mx:
                        mx = d
        else:
            d = abs(a[idx] - b[idx])
            if d > mx:
                mx = d
    return mx


def integrate_gl4(state0, t_end, nsteps, mode="2hdm2"):
    """
    Disjoint Implicit 2-Stage 4th-Order Gauss-Legendre (GL4) ODE Integrator.
    a11=a22=1/4, a12=1/4-sqrt(3)/6, a21=1/4+sqrt(3)/6, b1=b2=1/2.
    """
    sq3_6 = mp.sqrt(mp.mpf(3)) / mp.mpf(6)
    a11 = rat(1, 4)
    a12 = rat(1, 4) - sq3_6
    a21 = rat(1, 4) + sq3_6
    a22 = rat(1, 4)
    h = mp.mpf(t_end) / mp.mpf(nsteps)
    ha11, ha12, ha21, ha22 = h * a11, h * a12, h * a21, h * a22
    hb = h * rat(1, 2)
    tol = pow10(-(mp.mp.dps - 4))

    y = state0
    stab_all = True
    min_dflat = mp.mpf(1000)
    t_ewsb_u = None
    t_ewsb_d = None

    for step_idx in range(1, nsteps + 1):
        t_prev = h * mp.mpf(step_idx - 1)
        t_curr = h * mp.mpf(step_idx)
        mHu_prev = y[10]
        mHd_prev = y[11]
        f_prev = rge_rhs_2hdm_type2_soft(y, include_2loop=True, mode=mode)
        k1 = f_prev
        k2 = f_prev
        for _ in range(30):
            y1 = state_lincomb(y, ha11, k1, ha12, k2)
            y2 = state_lincomb(y, ha21, k1, ha22, k2)
            k1_new = rge_rhs_2hdm_type2_soft(y1, include_2loop=True, mode=mode)
            k2_new = rge_rhs_2hdm_type2_soft(y2, include_2loop=True, mode=mode)
            err = max(state_diff_norm(k1_new, k1), state_diff_norm(k2_new, k2))
            k1, k2 = k1_new, k2_new
            if err < tol:
                break
        y_next = state_lincomb(y, hb, k1, hb, k2)
        # Re-symmetrize Hermitian soft masses cleanly against numerical noise
        y_list = list(y_next)
        for idx in (12, 13, 14, 15, 16):
            y_list[idx] = mat3_sym_herm(y_list[idx])
        y = tuple(y_list)

        # Check all 4 vacuum stability inequalities at EVERY step t in [-35, 0)
        l1, l2, l3, l4 = y[3], y[4], y[5], y[6]
        if l1 <= 0 or l2 <= 0:
            stab_all = False
            dflat = mp.mpf(-1)
        else:
            sql12 = mp.sqrt(l1 * l2)
            m3 = l3 + sql12
            dflat = l3 + l4 + sql12
            if m3 <= 0 or dflat <= 0:
                stab_all = False
        if dflat < min_dflat:
            min_dflat = dflat

        # Cubic Hermite zero-crossing interpolation for t_EWSB_u and t_EWSB_d
        mHu_curr = y[10]
        mHd_curr = y[11]
        if t_ewsb_u is None and mHu_prev > 0 and mHu_curr <= 0:
            f_curr = rge_rhs_2hdm_type2_soft(y, include_2loop=True, mode=mode)
            d0 = f_prev[10] * h
            d1 = f_curr[10] * h
            # Solve cubic Hermite H(s) = 0 on s in [0, 1] via bisection + Newton
            lo, hi = mp.mpf(0), mp.mpf(1)
            for _ in range(50):
                s = rat(1, 2) * (lo + hi)
                s2 = s * s
                s3 = s2 * s
                val = (
                    (mp.mpf(2) * s3 - mp.mpf(3) * s2 + mp.mpf(1)) * mHu_prev
                    + (s3 - mp.mpf(2) * s2 + s) * d0
                    + (-mp.mpf(2) * s3 + mp.mpf(3) * s2) * mHu_curr
                    + (s3 - s2) * d1
                )
                if val > 0:
                    lo = s
                else:
                    hi = s
            t_ewsb_u = t_prev + rat(1, 2) * (lo + hi) * h
        if t_ewsb_d is None and mHd_prev > 0 and mHd_curr <= 0:
            f_curr = rge_rhs_2hdm_type2_soft(y, include_2loop=True, mode=mode)
            d0 = f_prev[11] * h
            d1 = f_curr[11] * h
            lo, hi = mp.mpf(0), mp.mpf(1)
            for _ in range(50):
                s = rat(1, 2) * (lo + hi)
                s2 = s * s
                s3 = s2 * s
                val = (
                    (mp.mpf(2) * s3 - mp.mpf(3) * s2 + mp.mpf(1)) * mHd_prev
                    + (s3 - mp.mpf(2) * s2 + s) * d0
                    + (-mp.mpf(2) * s3 + mp.mpf(3) * s2) * mHd_curr
                    + (s3 - s2) * d1
                )
                if val > 0:
                    lo = s
                else:
                    hi = s
            t_ewsb_d = t_prev + rat(1, 2) * (lo + hi) * h

    return y, stab_all, min_dflat, t_ewsb_u, t_ewsb_d


def run_guardrail4_benchmarks():
    """
    Independent Guardrail 4 verification:
      1. Chowdhury-Eberhardt (arXiv:1503.08216 App. A) exact SymPy + 55-digit check
         on all 3 Yukawas (beta_yt, beta_yb, beta_ytau) + gauge + quartics.
      2. Martin (hep-ph/9709356 Eqs. 6.5.24-6.5.30) 7-equation soft-mass benchmark.
      3. Opposite Xing-Zhou d|V_cb|/dt sign in Type-II 2HDM vs SM.
    """
    mp.mp.dps = 55
    # Arbitrary non-trivial rational benchmark test point (strictly 0 of 19!)
    g1 = rat(7, 13)
    g2 = rat(5, 9)
    g3 = rat(11, 10)
    yt = rat(9, 10)
    yb = rat(4, 11)
    ytau = rat(3, 17)
    l1 = rat(1, 7)
    l2 = rat(2, 11)
    l3 = rat(3, 19)
    l4 = rat(-2, 13)

    def diag3(v):
        z = mp.mpc(0)
        return [[z, z, z], [z, z, z], [z, z, mp.mpc(v)]]

    mHu2 = rat(5, 7)
    mHd2 = rat(11, 13)
    mQ = rat(17, 19)
    mu = rat(13, 11)
    md = rat(23, 29)
    mL = rat(7, 5)
    me = rat(31, 23)
    state = (
        g1, g2, g3, l1, l2, l3, l4,
        diag3(yt), diag3(yb), diag3(ytau),
        mHu2, mHd2, diag3(mQ), diag3(mu), diag3(md), diag3(mL), diag3(me),
    )
    rhs = rge_rhs_2hdm_type2_soft(state, include_2loop=True, mode="2hdm2")
    inv16 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
    inv16_2 = inv16 * inv16

    # Independent direct transcription of Chowdhury-Eberhardt arXiv:1503.08216 App. A
    # in SM hypercharge gY^2 = (3/5) g1^2!
    gY2 = rat(3, 5) * g1 * g1
    g22 = g2 * g2
    g32 = g3 * g3
    Yt2, Yb2, Ytau2 = yt * yt, yb * yb, ytau * ytau
    ce_yt_1 = (-(rat(17, 12) * gY2 + rat(9, 4) * g22 + mp.mpf(8) * g32) + rat(1, 2) * Yb2 + rat(9, 2) * Yt2) * yt
    ce_yt_2 = (
        rat(1267, 216) * gY2 * gY2 - rat(3, 4) * gY2 * g22 + rat(19, 9) * gY2 * g32
        - rat(21, 4) * g22 * g22 + mp.mpf(9) * g22 * g32 - mp.mpf(108) * g32 * g32
        + rat(3, 2) * l2 * l2 + l3 * l3 + l3 * l4 + l4 * l4
        + gY2 * (rat(-41, 144) * Yb2 + rat(131, 16) * Yt2)
        + g22 * (rat(33, 16) * Yb2 + rat(225, 16) * Yt2)
        + g32 * (rat(16, 3) * Yb2 + mp.mpf(36) * Yt2)
        - rat(5, 2) * Yb2 * Yb2 - rat(5, 2) * Yb2 * Yt2 - rat(3, 4) * Yb2 * Ytau2
        - mp.mpf(12) * Yt2 * Yt2 - mp.mpf(2) * Yb2 * l3 + mp.mpf(2) * Yb2 * l4 - mp.mpf(6) * Yt2 * l2
    ) * yt
    ce_yb_1 = (-(rat(5, 12) * gY2 + rat(9, 4) * g22 + mp.mpf(8) * g32) + rat(9, 2) * Yb2 + rat(1, 2) * Yt2 + Ytau2) * yb
    ce_yb_2 = (
        rat(-113, 216) * gY2 * gY2 - rat(9, 4) * gY2 * g22 + rat(31, 9) * gY2 * g32
        - rat(21, 4) * g22 * g22 + mp.mpf(9) * g22 * g32 - mp.mpf(108) * g32 * g32
        + l3 * l3 + l3 * l4 + l4 * l4
        + gY2 * (rat(79, 16) * Yb2 - rat(53, 144) * Yt2 + rat(25, 8) * Ytau2)
        + g22 * (rat(225, 16) * Yb2 + rat(33, 16) * Yt2 + rat(15, 8) * Ytau2)
        + g32 * (mp.mpf(36) * Yb2 + rat(16, 3) * Yt2)
        - mp.mpf(12) * Yb2 * Yb2 - rat(5, 2) * Yb2 * Yt2 - rat(9, 4) * Yb2 * Ytau2
        - rat(5, 2) * Yt2 * Yt2 - rat(9, 4) * Ytau2 * Ytau2
        - mp.mpf(6) * Yb2 * l1 - mp.mpf(2) * Yt2 * l3 + mp.mpf(2) * Yt2 * l4 + rat(3, 2) * l1 * l1
    ) * yb
    ce_ytau_1 = (-(rat(15, 4) * gY2 + rat(9, 4) * g22) + mp.mpf(3) * Yb2 + rat(5, 2) * Ytau2) * ytau
    ce_ytau_2 = (
        rat(161, 8) * gY2 * gY2 + rat(9, 4) * gY2 * g22 - rat(21, 4) * g22 * g22
        + l3 * l3 + l3 * l4 + l4 * l4
        + gY2 * (rat(25, 24) * Yb2 + rat(179, 16) * Ytau2)
        + g22 * (rat(45, 8) * Yb2 + rat(165, 16) * Ytau2)
        + mp.mpf(20) * g32 * Yb2
        - rat(27, 4) * Yb2 * Yb2 - rat(9, 4) * Yb2 * Yt2 - rat(27, 4) * Yb2 * Ytau2
        - mp.mpf(3) * Ytau2 * Ytau2 - mp.mpf(6) * Ytau2 * l1 + rat(3, 2) * l1 * l1
    ) * ytau

    err_yt = abs(mp.re(rhs[7][2][2]) - (ce_yt_1 * inv16 + ce_yt_2 * inv16_2))
    err_yb = abs(mp.re(rhs[8][2][2]) - (ce_yb_1 * inv16 + ce_yb_2 * inv16_2))
    err_ytau = abs(mp.re(rhs[9][2][2]) - (ce_ytau_1 * inv16 + ce_ytau_2 * inv16_2))
    ce_max_err = max(err_yt, err_yb, err_ytau)

    # Exact SymPy symbolic identity verification for CE App. A GUT conversion!
    sg1, sg2, sg3, syt, syb, sytau, sl1, sl2, sl3, sl4 = sp.symbols("g1 g2 g3 yt yb ytau l1 l2 l3 l4")
    sgY2 = sp.Rational(3, 5) * sg1 ** 2
    sym_u_diff = sp.simplify(
        (sp.Rational(1267, 600) * sg1 ** 4 - sp.Rational(9, 20) * sg1 ** 2 * sg2 ** 2
         + sp.Rational(19, 15) * sg1 ** 2 * sg3 ** 2 + (sp.Rational(17, 8) + sp.Rational(223, 80)) * sg1 ** 2 * syt ** 2
         - sp.Rational(41, 240) * sg1 ** 2 * syb ** 2)
        - (sp.Rational(1267, 216) * sgY2 ** 2 - sp.Rational(3, 4) * sgY2 * sg2 ** 2
           + sp.Rational(19, 9) * sgY2 * sg3 ** 2 + sp.Rational(131, 16) * sgY2 * syt ** 2
           - sp.Rational(41, 144) * sgY2 * syb ** 2)
    )
    sym_d_diff = sp.simplify(
        (sp.Rational(-113, 600) * sg1 ** 4 - sp.Rational(27, 20) * sg1 ** 2 * sg2 ** 2
         + sp.Rational(31, 15) * sg1 ** 2 * sg3 ** 2 + (sp.Rational(5, 8) + sp.Rational(187, 80)) * sg1 ** 2 * syb ** 2
         - sp.Rational(53, 240) * sg1 ** 2 * syt ** 2 + sp.Rational(15, 8) * sg1 ** 2 * sytau ** 2)
        - (sp.Rational(-113, 216) * sgY2 ** 2 - sp.Rational(9, 4) * sgY2 * sg2 ** 2
           + sp.Rational(31, 9) * sgY2 * sg3 ** 2 + sp.Rational(79, 16) * sgY2 * syb ** 2
           - sp.Rational(53, 144) * sgY2 * syt ** 2 + sp.Rational(25, 8) * sgY2 * sytau ** 2)
    )
    sym_e_diff = sp.simplify(
        (sp.Rational(1449, 200) * sg1 ** 4 + sp.Rational(27, 20) * sg1 ** 2 * sg2 ** 2
         + sp.Rational(5, 8) * sg1 ** 2 * syb ** 2 + (sp.Rational(15, 8) + sp.Rational(387, 80)) * sg1 ** 2 * sytau ** 2)
        - (sp.Rational(161, 8) * sgY2 ** 2 + sp.Rational(9, 4) * sgY2 * sg2 ** 2
           + sp.Rational(25, 24) * sgY2 * syb ** 2 + sp.Rational(179, 16) * sgY2 * sytau ** 2)
    )
    sym_exact = bool(sym_u_diff == 0 and sym_d_diff == 0 and sym_e_diff == 0)

    # Martin hep-ph/9709356 Eqs. 6.5.24-6.5.30 (7 equations, Ma=A0=0, nonzero S)
    S_ref = mHu2 - mHd2 + (mQ - mL - mp.mpf(2) * mu + md + me)
    Xt = mp.mpf(2) * Yt2 * (mHu2 + mQ + mu)
    Xb = mp.mpf(2) * Yb2 * (mHd2 + mQ + md)
    Xtau = mp.mpf(2) * Ytau2 * (mHd2 + mL + me)
    ref_soft = [
        (mp.mpf(3) * Xt + rat(3, 5) * g1 * g1 * S_ref) * inv16,
        (mp.mpf(3) * Xb + Xtau - rat(3, 5) * g1 * g1 * S_ref) * inv16,
        (Xt + Xb + rat(1, 5) * g1 * g1 * S_ref) * inv16,
        (mp.mpf(2) * Xt - rat(4, 5) * g1 * g1 * S_ref) * inv16,
        (mp.mpf(2) * Xb + rat(2, 5) * g1 * g1 * S_ref) * inv16,
        (Xtau - rat(3, 5) * g1 * g1 * S_ref) * inv16,
        (mp.mpf(2) * Xtau + rat(6, 5) * g1 * g1 * S_ref) * inv16,
    ]
    got_soft = [
        rhs[10], rhs[11],
        mp.re(rhs[12][2][2]), mp.re(rhs[13][2][2]), mp.re(rhs[14][2][2]),
        mp.re(rhs[15][2][2]), mp.re(rhs[16][2][2]),
    ]
    martin_errs = [abs(g - r) for g, r in zip(got_soft, ref_soft)]
    martin_max_err = max(martin_errs)

    # Opposite Xing-Zhou d|V_cb|/dt sign (Type-II 2HDM vs SM)
    # Construct simple hierarchical Yu (diagonal) and Yd (rotated by 2-3 angle theta=1/10)
    th = rat(1, 10)
    cth, sth = mp.cos(th), mp.sin(th)
    Yu_xz = [[mp.mpc(rat(1, 100)), mp.mpc(0), mp.mpc(0)],
             [mp.mpc(0), mp.mpc(rat(1, 10)), mp.mpc(0)],
             [mp.mpc(0), mp.mpc(0), mp.mpc(1)]]
    R23 = [[mp.mpc(1), mp.mpc(0), mp.mpc(0)],
           [mp.mpc(0), mp.mpc(cth), mp.mpc(sth)],
           [mp.mpc(0), mp.mpc(-sth), mp.mpc(cth)]]
    Dd_xz = [[mp.mpc(rat(1, 200)), mp.mpc(0), mp.mpc(0)],
             [mp.mpc(0), mp.mpc(rat(1, 50)), mp.mpc(0)],
             [mp.mpc(0), mp.mpc(0), mp.mpc(rat(1, 2))]]
    Yd_xz = mat3_mul(R23, Dd_xz)
    Ye_xz = diag3(rat(1, 5))
    I3 = mat3_eye()
    st_xz = (
        rat(1, 2), rat(1, 2), rat(1, 2), rat(1, 10), rat(1, 10), rat(1, 40), rat(-1, 8),
        Yu_xz, Yd_xz, Ye_xz, mp.mpf(1), mp.mpf(1), I3, I3, I3, I3, I3,
    )
    _, Uu0 = svd_left_real_split(Yu_xz)
    _, Ud0 = svd_left_real_split(Yd_xz)
    Vcb0 = abs(mat3_mul(mat3_dag(Uu0), Ud0)[1][2])
    st_2hdm, _, _, _, _ = integrate_gl4(st_xz, mp.mpf(-5), 20, mode="2hdm2")
    st_sm, _, _, _, _ = integrate_gl4(st_xz, mp.mpf(-5), 20, mode="sm")
    _, Uu1 = svd_left_real_split(st_2hdm[7])
    _, Ud1 = svd_left_real_split(st_2hdm[8])
    Vcb_2hdm = abs(mat3_mul(mat3_dag(Uu1), Ud1)[1][2])
    _, Uu2 = svd_left_real_split(st_sm[7])
    _, Ud2 = svd_left_real_split(st_sm[8])
    Vcb_sm = abs(mat3_mul(mat3_dag(Uu2), Ud2)[1][2])
    # Running downward t: 0 -> -5:
    # In SM: d|Vcb|/dt < 0 => |Vcb(-5)| > |Vcb(0)|
    # In 2HDM-II: d|Vcb|/dt > 0 => |Vcb(-5)| < |Vcb(0)|
    xz_opposite = bool(Vcb_2hdm < Vcb0 and Vcb_sm > Vcb0)

    return {
        "CE_1503_08216": {
            "err_beta_yt": fmt(err_yt, 10),
            "err_beta_yb": fmt(err_yb, 10),
            "err_beta_ytau": fmt(err_ytau, 10),
            "max_err": fmt(ce_max_err, 10),
            "sympy_exact_identity": sym_exact,
            "pass_lt_1e38": bool(ce_max_err < pow10(-38) and sym_exact),
        },
        "Martin_9709356_7eq": {
            "max_err": fmt(martin_max_err, 10),
            "errs": [fmt(e, 8) for e in martin_errs],
            "pass_lt_1e38": bool(martin_max_err < pow10(-38)),
        },
        "XingZhou_Vcb_sign": {
            "Vcb_UV": fmt(Vcb0, 20),
            "Vcb_2HDM2_t_m5": fmt(Vcb_2hdm, 20),
            "Vcb_SM_t_m5": fmt(Vcb_sm, 20),
            "opposite_sign_verified": xz_opposite,
        },
        "all_pass": bool(ce_max_err < pow10(-38) and sym_exact and martin_max_err < pow10(-38) and xz_opposite),
    }


def clenshaw_curtis_nodes_weights(N):
    """Exact Clenshaw-Curtis quadrature on [-1, 1] with N+1 nodes (N even)."""
    # Nodes x_k = cos(k pi / N), weights via exact trigonometric cosine sum
    xs = [mp.cos(mp.mpf(k) * mp.pi / mp.mpf(N)) for k in range(N + 1)]
    ws = []
    for k in range(N + 1):
        th_k = mp.mpf(k) * mp.pi / mp.mpf(N)
        s = mp.mpf(1)
        for j in range(1, N // 2 + 1):
            b = mp.mpf(1) if (2 * j == N) else mp.mpf(2)
            s -= b * mp.cos(mp.mpf(2 * j) * th_k) / mp.mpf(4 * j * j - 1)
        c = mp.mpf(1) if (k == 0 or k == N) else mp.mpf(2)
        ws.append(c * s / mp.mpf(N))
    return xs, ws


def compute_curved_dirac_G_s12(tau, C_val, B_val):
    """
    Disjoint Clenshaw-Curtis polar quadrature + 4th-order Suzuki-Yoshida symplectic
    ODE on the exact Voronoi cell of E_tau \\ {0} (splitting at exact Voronoi angular
    vertices so every face is C^infinity!).
    Computes:
      - Gauss-Bonnet Area = int_{E_tau} e^{2 phi} d^2 z  (exact = 2 pi)
      - Curved spin-1/2 Dirac Kahler metric G_{s=1/2} = diag(g4, g2, g3) matching
        BL = [QJ, QI, QK] <-> (theta_4, theta_2, theta_3), where
          g_nu = int_{E_tau} |theta_nu(z, tau)|^2 exp(-2 pi (Im z)^2 / y) e^{+phi(z)} d^2 z.
    """
    mp.mp.dps = 26
    y = mp.im(tau)
    _, E2_val = eta_and_E2_pentagonal(tau)
    wp4 = make_wp_div4_theta1(tau, E2_val)
    aa, bb = frobenius_coeffs(tau, B_val, 10)

    # 4th-order Suzuki-Yoshida 5-stage weights (max|w| = 0.658)
    r3 = mp.power(mp.mpf(4), rat(1, 3))
    s4 = mp.mpf(1) / (mp.mpf(4) - r3)
    m4 = mp.mpf(1) - mp.mpf(4) * s4
    W4 = [s4, s4, m4, s4, s4]

    def step_ray(M, z, dz):
        u1, u2, v1, v2 = M
        zc = z
        for w in W4:
            h = dz * w
            h2 = h / mp.mpf(2)
            u1 += h2 * v1
            u2 += h2 * v2
            zc += h2
            qv = wp4(zc) + B_val
            v1 -= h * qv * u1
            v2 -= h * qv * u2
            u1 += h2 * v1
            u2 += h2 * v2
            zc += h2
        return (u1, u2, v1, v2)

    def ephi(M):
        u1, u2, _, _ = M
        D = mp.re(mp.mpf(2) * C_val * u1 * mp.conj(u1) - u1 * mp.conj(u2) - u2 * mp.conj(u1))
        return mp.mpf(2) / D

    # Exact Voronoi cell half-planes Re(z conj(w)) <= |w|^2 / 2
    short_vecs = []
    for m in range(-2, 3):
        for n in range(-2, 3):
            if m != 0 or n != 0:
                short_vecs.append(mp.mpf(m) * tau + mp.mpf(n))

    def rmax_dir(th):
        e = mp.exp(mp.mpc(0, 1) * th)
        rm = mp.mpf(1000)
        for w in short_vecs:
            proj = mp.re(e * mp.conj(w))
            if proj > pow10(-14):
                cand = (abs(w) ** 2) / (mp.mpf(2) * proj)
                if cand < rm:
                    rm = cand
        return rm

    # Compute exact Voronoi vertices in upper half-plane theta in [0, pi] (by z -> -z symmetry!)
    # Intersections of pairs of perpendicular bisectors that satisfy ALL Voronoi inequalities
    verts_th = [mp.mpf(0), mp.pi]
    tol_v = pow10(-10)
    for i in range(len(short_vecs)):
        w1 = short_vecs[i]
        a1, b1 = mp.re(w1), mp.im(w1)
        c1 = rat(1, 2) * (a1 * a1 + b1 * b1)
        for j in range(i + 1, len(short_vecs)):
            w2 = short_vecs[j]
            a2, b2 = mp.re(w2), mp.im(w2)
            det = a1 * b2 - a2 * b1
            if abs(det) < pow10(-10):
                continue
            c2 = rat(1, 2) * (a2 * a2 + b2 * b2)
            vx = (c1 * b2 - c2 * b1) / det
            vy = (a1 * c2 - a2 * c1) / det
            if vy < -tol_v:
                continue
            vz = mp.mpc(vx, vy)
            inside = True
            for w in short_vecs:
                if mp.re(vz * mp.conj(w)) > rat(1, 2) * (abs(w) ** 2) + tol_v:
                    inside = False
                    break
            if inside:
                ang = mp.atan2(vy, vx)
                if ang < 0:
                    ang = mp.mpf(0)
                if ang > mp.pi:
                    ang = mp.pi
                verts_th.append(ang)
    verts_th.sort()
    uniq_th = [verts_th[0]]
    for ang in verts_th[1:]:
        if ang - uniq_th[-1] > pow10(-6):
            uniq_th.append(ang)
    # Also split any wide face > pi/3 into 2 sub-panels for extra angular accuracy (e.g. tall rectangle!)
    panels = []
    for k in range(len(uniq_th) - 1):
        a_t, b_t = uniq_th[k], uniq_th[k + 1]
        n_sub = max(1, int(mp.ceil((b_t - a_t) / (mp.pi / mp.mpf(4)))))
        dt = (b_t - a_t) / mp.mpf(n_sub)
        for s in range(n_sub):
            panels.append((a_t + mp.mpf(s) * dt, a_t + mp.mpf(s + 1) * dt))

    def theta_z(ca, cb, z):
        # Evaluate theta[ca, cb](z, tau) quickly
        s = mp.mpc(0)
        nmax = int(mp.ceil(mp.sqrt(mp.mpf(55) / (mp.pi * y)))) + 3
        for n in range(-nmax, nmax + 1):
            nc = mp.mpf(n) + ca
            s += mp.exp(mp.mpc(0, 1) * mp.pi * tau * nc * nc + mp.mpc(0, 2) * mp.pi * nc * (z + cb))
        return s

    rcut = rat(1, 1000)
    # Exact analytic inner disk r < rcut:
    # Area_inner = 2 pi / (-ln(rcut) + C_val)
    area = mp.mpf(2) * mp.pi / (-mp.log(rcut) + C_val)
    # Spin-1/2 inner disk: int_0^rcut 2 pi |theta_nu(0)|^2 / (-ln r + C_val) dr
    # Substitute u = -ln r + C => r = e^{C - u}, dr = -e^{C-u} du => e^C E_1(-ln(rcut) + C)
    u_cut = -mp.log(rcut) + C_val
    inner_rad = mp.exp(C_val) * mp.e1(u_cut)
    chars_bl = ((mp.mpf(0), rat(1, 2)), (rat(1, 2), mp.mpf(0)), (mp.mpf(0), mp.mpf(0)))  # (t4, t2, t3)
    g_diag = [mp.mpf(2) * mp.pi * (abs(theta_z(ca, cb, mp.mpc(0))) ** 2) * inner_rad for ca, cb in chars_bl]

    # Clenshaw-Curtis on each smooth angular panel (theta in [0, pi], multiplied by 2 by z -> -z symmetry!)
    cc_x_th, cc_w_th = clenshaw_curtis_nodes_weights(10)
    cc_x_r, cc_w_r = clenshaw_curtis_nodes_weights(16)

    for th_a, th_b in panels:
        mid_t = rat(1, 2) * (th_a + th_b)
        half_t = rat(1, 2) * (th_b - th_a)
        for xt, wt in zip(cc_x_th, cc_w_th):
            th = mid_t + half_t * xt
            w_theta = mp.mpf(2) * half_t * wt  # factor 2 for [pi, 2pi] via z -> -z symmetry
            e_th = mp.exp(mp.mpc(0, 1) * th)
            rm = rmax_dir(th)
            s0 = mp.log(rcut)
            s1 = mp.log(rm)
            mid_s = rat(1, 2) * (s0 + s1)
            half_s = rat(1, 2) * (s1 - s0)
            # CC nodes go from +1 to -1; sort ascending in s so ray marches smoothly outward!
            r_nodes = sorted([(mid_s + half_s * xr, half_s * wr) for xr, wr in zip(cc_x_r, cc_w_r)], key=lambda p: p[0])
            M = eval_frobenius(rcut * e_th, aa, bb)
            r_cur = rcut
            for s_val, w_s in r_nodes:
                r_val = mp.exp(s_val)
                if r_val > r_cur:
                    # Adaptive substeps along ray for high ODE accuracy even at y=3.38
                    n_sub = max(1, int(mp.ceil((r_val - r_cur) / min(r_cur * rat(1, 2), rat(1, 6)))))
                    dr = (r_val - r_cur) / mp.mpf(n_sub)
                    for k in range(n_sub):
                        M = step_ray(M, (r_cur + mp.mpf(k) * dr) * e_th, dr * e_th)
                    r_cur = r_val
                ep = ephi(M)
                z = r_val * e_th
                wq = w_theta * w_s * r_val * r_val  # r dr dtheta = r^2 ds dtheta
                area += ep * ep * wq
                gauss = mp.exp(-mp.mpf(2) * mp.pi * (mp.im(z) ** 2) / y)
                for idx, (ca, cb) in enumerate(chars_bl):
                    tv = theta_z(ca, cb, z)
                    g_diag[idx] += (abs(tv) ** 2) * gauss * ep * wq

    gb_err = abs(area / (mp.mpf(2) * mp.pi) - mp.mpf(1))
    # Normalize G so mean diagonal = 1 (purely cosmetic: overall scale cancels in max sigma_3 = 1!)
    g_mean = (g_diag[0] + g_diag[1] + g_diag[2]) / mp.mpf(3)
    g_norm = [g / g_mean for g in g_diag]
    aniso = (max(g_norm) - min(g_norm)) / g_mean if g_mean > 0 else mp.mpf(1)
    # Build diagonal 3x3 matrix G and G^{-1/2}
    G_mat = [[mp.mpc(g_norm[i]) if i == j else mp.mpc(0) for j in range(3)] for i in range(3)]
    Gmhalf = [[mp.mpc(mp.mpf(1) / mp.sqrt(g_norm[i])) if i == j else mp.mpc(0) for j in range(3)] for i in range(3)]
    return {
        "area_over_2pi": area / (mp.mpf(2) * mp.pi),
        "gauss_bonnet_err": gb_err,
        "g_raw": g_diag,
        "g_norm": g_norm,
        "anisotropy": aniso,
        "G": G_mat,
        "G_mhalf": Gmhalf,
    }


def build_sector_higgs_basis(tau, L2_val, m_int, n_int, qL, qR, frame_c):
    """Build the 3 Higgs basis matrices [A_0, A_1, A_2] for [QI, QJ, QK] at point (m/30, n/30)."""
    QI, QJ, QK, EPS, BL, EDUAL = frame_c
    _, _, _, eta3 = S_coeffs_frame_c(tau)
    y = mp.im(tau)
    sqy = mp.sqrt(y)
    twopi_eta3 = mp.mpf(2) * mp.pi * eta3
    ap = (qL + qR) * 2 * m_int
    bp = (qL + qR) * 2 * n_int
    am = (qL - qR) * 2 * m_int
    bm = (qL - qR) * 2 * n_int
    ef = mp.exp(mp.mpc(0, -2) * mp.pi * rat(qL * m_int, 30))
    kappas = {"1": mp.mpc(0, -1) * ef, "i": mp.mpc(-1), "j": -ef, "k": mp.mpc(0, 1)}
    shifts = {"1": (30, 30), "i": (30, 0), "j": (0, 30), "k": (0, 0)}
    Mw = mp.matrix(2, 2)
    for s in ("1", "i", "j", "k"):
        sa, sb = shifts[s]
        csa, csb = ap + sa, bp + sb
        dsa, dsb = am + sa, bm + sb
        if (csa % 60 == 30 and csb % 60 == 30) or (dsa % 60 == 30 and dsb % 60 == 30):
            continue
        thc = theta_char(rat(csa, 60), rat(csb, 60), tau)
        thd = theta_char(rat(dsa, 60), rat(dsb, 60), tau)
        Rs = kappas[s] * thc * thd / twopi_eta3
        al = rat((csa - 30) % 60, 60)
        be = rat((csb - 30) % 60, 60)
        fu = F_u_kronecker(al, be, tau)
        th0, dth0 = theta_char(al + rat(1, 2), be + rat(1, 2), tau, True)
        a0 = dth0 / th0
        cval = (
            fu + mp.pi * mp.log(y) - mp.mpf(2) * mp.pi * (mp.euler + mp.log(mp.pi))
            - mp.pi * (abs(a0) ** 2) * mp.exp(-mp.mpf(2) * L2_val)
        )
        arg = mp.mpf(2) * mp.pi * L2_val + cval
        wt = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
        Mw += (wt * Rs) * EDUAL[s]
    basis = []
    for Qm in (QI, QJ, QK):
        A = mat3_zero()
        for ai in range(3):
            for bi in range(3):
                P = BL[ai].T * EPS * Qm * BL[bi]
                A[ai][bi] = sqy * (
                    P[0, 0] * Mw[0, 0] + P[0, 1] * Mw[0, 1] + P[1, 0] * Mw[1, 0] + P[1, 1] * Mw[1, 1]
                )
        basis.append(A)
    return basis


def combine_higgs(h_vec, basis):
    out = mat3_zero()
    for k in range(3):
        hk = h_vec[k]
        Ak = basis[k]
        for i in range(3):
            for j in range(3):
                out[i][j] += hk * Ak[i][j]
    return out


def optimize_dynamic_v4_ferro(Au, Ad, Ae, h_stat):
    """
    Minimize E(h_u, h_d) = V_4(h_u, h_d) - (1/4)|V_4(S^can)| |h_u^dag h_d|^2
    on S^5 x S^5 via multi-start Riemannian projected gradient descent with exact
    Wirtinger gradients and Armijo backtracking line search.
    """
    def vec_norm(h):
        return mp.sqrt(sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in h))

    def vec_unit(h):
        n = vec_norm(h)
        return [c / n for c in h]

    def vec_dot(a, b):
        return sum(mp.conj(a[k]) * b[k] for k in range(3))

    def tr_H2(Y):
        H = mat3_mul(mat3_dag(Y), Y)
        return mp.re(mat3_tr(mat3_mul(H, H)))

    def v4_pure(hu, hd):
        Yu = combine_higgs(hu, Au)
        Yd = combine_higgs(hd, Ad)
        Ye = combine_higgs(hd, Ae)
        return -(mp.mpf(3) * tr_H2(Yu) + mp.mpf(3) * tr_H2(Yd) + tr_H2(Ye))

    hs = vec_unit(h_stat)
    v4_stat_abs = abs(v4_pure(hs, hs))
    lam_f = rat(1, 4) * v4_stat_abs

    def energy_and_rgrad(hu, hd):
        Yu = combine_higgs(hu, Au)
        Yd = combine_higgs(hd, Ad)
        Ye = combine_higgs(hd, Ae)
        Hu = mat3_mul(mat3_dag(Yu), Yu)
        Hd = mat3_mul(mat3_dag(Yd), Yd)
        He = mat3_mul(mat3_dag(Ye), Ye)
        e_v4 = -(mp.mpf(3) * mp.re(mat3_tr(mat3_mul(Hu, Hu))) + mp.mpf(3) * mp.re(mat3_tr(mat3_mul(Hd, Hd))) + mp.re(mat3_tr(mat3_mul(He, He))))
        ov = vec_dot(hu, hd)
        ov2 = mp.re(ov) * mp.re(ov) + mp.im(ov) * mp.im(ov)
        E = e_v4 - lam_f * ov2

        # Exact Wirtinger gradient 2 * dE / d(h^*):
        # For f(h) = -Nc Tr((Y^dag Y)^2), df = -4 Nc Re Tr(Y^dag Y Y^dag dY)
        # => 2 df/d(h_k^*) = -4 Nc Tr(A_k^dag Y Y^dag Y) = -4 Nc Tr(A_k^dag (Y H))
        YuHu = mat3_mul(Yu, Hu)
        YdHd = mat3_mul(Yd, Hd)
        YeHe = mat3_mul(Ye, He)
        gu = []
        gd = []
        for k in range(3):
            # Tr(A^dag B) = sum_{ij} conj(A_ij) B_ij
            t_u = sum(mp.conj(Au[k][i][j]) * YuHu[i][j] for i in range(3) for j in range(3))
            t_d = sum(mp.conj(Ad[k][i][j]) * YdHd[i][j] for i in range(3) for j in range(3))
            t_e = sum(mp.conj(Ae[k][i][j]) * YeHe[i][j] for i in range(3) for j in range(3))
            # d(-lam_f |hu^dag hd|^2)/d(hu^*) = -lam_f * conj(ov) * hd  => 2x = -2 lam_f conj(ov) hd
            # Wait: ov = hu^dag hd => ov^* = hd^dag hu => d(|ov|^2)/d(hu^*) = ov^* * hd!
            gu.append(mp.mpf(-12) * t_u - mp.mpf(2) * lam_f * mp.conj(ov) * hd[k])
            gd.append(mp.mpf(-12) * t_d - mp.mpf(4) * t_e - mp.mpf(2) * lam_f * ov * hu[k])

        # Project onto tangent space of S^5 x S^5: g_T = g - Re(h^dag g) h
        ru = mp.re(vec_dot(hu, gu))
        rd = mp.re(vec_dot(hd, gd))
        gu_T = [gu[k] - ru * hu[k] for k in range(3)]
        gd_T = [gd[k] - rd * hd[k] for k in range(3)]
        return E, gu_T, gd_T

    # 12 diverse deterministic starts (strictly float-free!)
    I_m = mp.mpc(0, 1)
    starts = [
        (hs, hs),
        ([mp.mpc(1), mp.mpc(0), mp.mpc(0)], [mp.mpc(1), mp.mpc(0), mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1), mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(0), mp.mpc(1)], [mp.mpc(0), mp.mpc(0), mp.mpc(1)]),
        ([mp.mpc(1), mp.mpc(1), mp.mpc(0)], [mp.mpc(1), mp.mpc(1), mp.mpc(0)]),
        ([mp.mpc(1), mp.mpc(0), mp.mpc(1)], [mp.mpc(1), mp.mpc(0), mp.mpc(1)]),
        ([mp.mpc(0), mp.mpc(1), mp.mpc(1)], [mp.mpc(0), mp.mpc(1), mp.mpc(1)]),
        ([mp.mpc(1), I_m, mp.mpc(1)], [mp.mpc(1), I_m, mp.mpc(1)]),
        ([mp.mpc(1), -I_m, mp.mpc(1)], [mp.mpc(1), -I_m, mp.mpc(1)]),
        ([mp.mpc(1), mp.mpc(1), mp.mpc(1)], [mp.mpc(1), mp.mpc(-1), I_m]),
        ([mp.mpc(2), mp.mpc(-1) + I_m, mp.mpc(1) - mp.mpf(2) * I_m], [mp.mpc(1), mp.mpc(2) + I_m, mp.mpc(-1)]),
        ([mp.mpc(-1) + I_m, mp.mpc(3), mp.mpc(1) + I_m], [mp.mpc(2) - I_m, mp.mpc(1), mp.mpc(2) + I_m]),
    ]

    best_E = None
    best_hu = None
    best_hd = None
    best_gnorm = None
    for hu0, hd0 in starts:
        hu = vec_unit(hu0)
        hd = vec_unit(hd0)
        E, gu, gd = energy_and_rgrad(hu, hd)
        alpha = mp.mpf(1) / (mp.mpf(1) + v4_stat_abs)
        for _ in range(180):
            gn2 = sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in gu) + sum(
                mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in gd
            )
            gn = mp.sqrt(gn2)
            if gn < pow10(-15) * (mp.mpf(1) + v4_stat_abs):
                break
            # Armijo backtracking with retraction onto S^5 x S^5
            step = alpha
            accepted = False
            for _ls in range(30):
                hu_try = vec_unit([hu[k] - step * gu[k] for k in range(3)])
                hd_try = vec_unit([hd[k] - step * gd[k] for k in range(3)])
                E_try, gu_try, gd_try = energy_and_rgrad(hu_try, hd_try)
                if E_try <= E - pow10(-4) * step * gn2:
                    hu, hd, E, gu, gd = hu_try, hd_try, E_try, gu_try, gd_try
                    alpha = step * rat(3, 2)
                    accepted = True
                    break
                step *= rat(1, 2)
            if not accepted:
                break
        gn_final = mp.sqrt(
            sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in gu)
            + sum(mp.re(c) * mp.re(c) + mp.im(c) * mp.im(c) for c in gd)
        )
        if best_E is None or E < best_E:
            best_E = E
            best_hu = hu
            best_hd = hd
            best_gnorm = gn_final

    overlap = abs(vec_dot(best_hu, best_hd))
    return best_hu, best_hd, best_E, best_gnorm, overlap


def extract_ckm_and_pmns_obs(Yu_ir, Yd_ir, Ye_ir, Ynu_1w, Ynu_2w, g3_ir, mHu2_ir, mHd2_ir, soft_mats):
    su, Uu = svd_left_real_split(Yu_ir)
    sd, Ud = svd_left_real_split(Yd_ir)
    se, Ue = svd_left_real_split(Ye_ir)
    V = mat3_mul(mat3_dag(Uu), Ud)
    V12 = abs(V[0][1])
    V23 = abs(V[1][2])
    V13 = abs(V[0][2])
    J_signed = mp.im(V[0][1] * V[1][2] * mp.conj(V[0][2]) * mp.conj(V[1][1]))
    Jcp = abs(J_signed)

    min_sf = None
    for M in soft_mats:
        evs, _ = herm3_eig_real_split(M)
        for ev in evs:
            if min_sf is None or ev < min_sf:
                min_sf = ev

    MQ2, Mu2, Md2, ML2, Me2 = soft_mats
    S_ir = (
        mHu2_ir - mHd2_ir
        + mp.re(mat3_tr(MQ2)) - mp.re(mat3_tr(ML2))
        - mp.mpf(2) * mp.re(mat3_tr(Mu2)) + mp.re(mat3_tr(Md2)) + mp.re(mat3_tr(Me2))
    )

    # Piece 3: Autonne-Takagi PMNS for M_R in {I_3, sym(Ynu(1w)), sym(Ynu(2w))}
    I3 = mat3_eye()
    MR_1w = mat3_scale(rat(1, 2), mat3_add(Ynu_1w, mat3_T(Ynu_1w)))
    MR_2w = mat3_scale(rat(1, 2), mat3_add(Ynu_2w, mat3_T(Ynu_2w)))
    pmns = {}
    for mr_name, MR in (("I3", I3), ("sym_Ynu_1w", MR_1w), ("sym_Ynu_2w", MR_2w)):
        MR_inv = mat3_inv(MR)
        kappa = mat3_mul(mat3_mul(Ynu_1w, MR_inv), mat3_T(Ynu_1w))
        mnu, Unu, rec_err, unit_err = autonne_takagi_real_split(kappa)
        Upmns = mat3_mul(mat3_dag(Ue), Unu)
        s13_2 = abs(Upmns[0][2]) ** 2
        c13_2 = mp.mpf(1) - s13_2
        s12_2 = (abs(Upmns[0][1]) ** 2) / c13_2 if c13_2 > 0 else mp.mpf(0)
        s23_2 = (abs(Upmns[1][2]) ** 2) / c13_2 if c13_2 > 0 else mp.mpf(0)
        Jnu_s = mp.im(Upmns[0][1] * Upmns[1][2] * mp.conj(Upmns[0][2]) * mp.conj(Upmns[1][1]))
        dm21 = mnu[1] * mnu[1] - mnu[0] * mnu[0]
        dm31 = mnu[2] * mnu[2] - mnu[0] * mnu[0]
        r_dm = dm21 / dm31 if dm31 > 0 else mp.mpf(0)
        pmns[mr_name] = {
            "s12_sq": s12_2,
            "s23_sq": s23_2,
            "s13_sq": s13_2,
            "Jcp_nu": abs(Jnu_s),
            "dm21_over_dm31": r_dm,
            "m_ratios": [mnu[0] / mnu[2], mnu[1] / mnu[2], mp.mpf(1)] if mnu[2] > 0 else [mp.mpf(0)] * 3,
            "takagi_rec_err": rec_err,
            "takagi_unit_err": unit_err,
        }

    return {
        "yt_over_g3": su[2] / g3_ir,
        "mb_over_mtau": sd[2] / se[2],
        "u23": su[1] / su[2],
        "d23": sd[1] / sd[2],
        "e23": se[1] / se[2],
        "u13": su[0] / su[2],
        "d13": sd[0] / sd[2],
        "e13": se[0] / se[2],
        "V12": V12,
        "V23": V23,
        "V13": V13,
        "Jcp": Jcp,
        "Jcp_signed": J_signed,
        "std_ckm": bool(V12 > V23 and V23 > V13),
        "m_Hu2_IR": mHu2_ir,
        "m_Hd2_IR": mHd2_ir,
        "min_sf": min_sf,
        "S_IR": S_ir,
        "pmns": pmns,
    }


def make_cayley_unitary(seed_int):
    """
    Disjoint Haar-like unitary via Cayley transform U = (I - i A)(I + i A)^{-1}
    of deterministic pseudo-random Hermitian A = A^dag (strictly float-free!).
    """
    state = seed_int

    def next_rat():
        nonlocal state
        state = (state * 6364136223846793005 + 1442695040888963407) & ((1 << 64) - 1)
        # Signed rational in [-2, 2]
        v = (state % 20001) - 10000
        return rat(v, 5000)

    A = mat3_zero()
    for i in range(3):
        A[i][i] = mp.mpc(next_rat(), 0)
        for j in range(i + 1, 3):
            c = mp.mpc(next_rat(), next_rat())
            A[i][j] = c
            A[j][i] = mp.conj(c)
    I3 = mat3_eye()
    iA = mat3_scale(mp.mpc(0, 1), A)
    num = mat3_sub(I3, iA)
    den_inv = mat3_inv(mat3_add(I3, iA))
    U = mat3_mul(num, den_inv)
    assert mat3_frob(mat3_sub(mat3_mul(mat3_dag(U), U), I3)) < pow10(-25)
    return U


def run_rp3(vacua_data, frame_c):
    # 1. Guardrail 4 literature benchmarks
    g4_bench = run_guardrail4_benchmarks()

    # 2. Curved spin-1/2 Dirac Kahler metric G_{s=1/2} at all 3 vacua
    g_s12_all = {}
    gb_all_ok = True
    for vname in ("omega", "tau_FILQ1", "tau_tot_70"):
        vd = vacua_data[vname]
        gd = compute_curved_dirac_G_s12(vd["tau"], vd["C"], vd["B"])
        gb_ok = bool(gd["gauss_bonnet_err"] < pow10(-3))
        gb_all_ok = gb_all_ok and gb_ok
        g_s12_all[vname] = gd
    omega_iso_ok = bool(g_s12_all["omega"]["anisotropy"] < pow10(-3))

    # 3. Pieces 2 & 3 at ALL 3 vacua & ALL 3 branches (dps = 36)
    mp.mp.dps = 36
    # UV D-term boundary in Branco/CE normalization at g1=g2=g3=1/2:
    g_uv = rat(1, 2)
    g2_2_uv = g_uv * g_uv
    gY_2_uv = rat(3, 5) * g_uv * g_uv
    l1_D = (g2_2_uv + gY_2_uv) / mp.mpf(4)  # 1/10
    l2_D = l1_D                             # 1/10
    l3_D = (g2_2_uv - gY_2_uv) / mp.mpf(4)  # 1/40
    l4_D = -g2_2_uv / mp.mpf(2)             # -1/8
    uv_dflat = l3_D + l4_D + mp.sqrt(l1_D * l2_D)
    assert abs(uv_dflat) < pow10(-35)

    branches_out = {}
    piece2_pass = True
    piece3_pass = True
    saved_for_haar = None

    for vname in ("omega", "tau_FILQ1", "tau_tot_70"):
        tau_v = vacua_data[vname]["tau"]
        L2_v = vacua_data[vname]["L2"]
        c0, c1, c2, _ = S_coeffs_frame_c(tau_v)
        h_stat = [c0, c1, c2]
        nrm_s = mp.sqrt(sum(abs(x) ** 2 for x in h_stat))
        h_stat_u = [x / nrm_s for x in h_stat]

        # Canonical mark w = (4/15, 1/30) => (8/30, 1/30); 2w = (8/15, 1/15) => (16/30, 2/30)
        Au_raw = build_sector_higgs_basis(tau_v, L2_v, 8, 1, 1, -4, frame_c)
        Ad_raw = build_sector_higgs_basis(tau_v, L2_v, 8, 1, 1, 2, frame_c)
        Ae_raw = build_sector_higgs_basis(tau_v, L2_v, 8, 1, -3, 6, frame_c)
        Anu1_raw = build_sector_higgs_basis(tau_v, L2_v, 8, 1, -3, 0, frame_c)
        Anu2_raw = build_sector_higgs_basis(tau_v, L2_v, 16, 2, -3, 0, frame_c)

        Gmhalf = g_s12_all[vname]["G_mhalf"]

        def apply_curv(basis):
            return [mat3_mul(mat3_mul(Gmhalf, A), Gmhalf) for A in basis]

        Au_curv = apply_curv(Au_raw)
        Ad_curv = apply_curv(Ad_raw)
        Ae_curv = apply_curv(Ae_raw)
        Anu1_curv = apply_curv(Anu1_raw)
        Anu2_curv = apply_curv(Anu2_raw)

        # Optimize DynamicV4_ferro_CURVED_s12 in canonical-kinetic ordering!
        hu_opt, hd_opt, e_opt, gnorm_opt, ov_opt = optimize_dynamic_v4_ferro(Au_curv, Ad_curv, Ae_curv, h_stat_u)

        branch_specs = [
            ("Static_FLAT", h_stat_u, h_stat_u, Au_raw, Ad_raw, Ae_raw, Anu1_raw, Anu2_raw, None),
            ("Static_CURVED_s12", h_stat_u, h_stat_u, Au_curv, Ad_curv, Ae_curv, Anu1_curv, Anu2_curv, None),
            (
                "DynamicV4_ferro_CURVED_s12",
                hu_opt,
                hd_opt,
                Au_curv,
                Ad_curv,
                Ae_curv,
                Anu1_curv,
                Anu2_curv,
                {"E_opt": e_opt, "rgrad_norm": gnorm_opt, "hu_hd_overlap": ov_opt},
            ),
        ]

        branches_out[vname] = {}
        for bname, hu, hd, Au_b, Ad_b, Ae_b, Anu1_b, Anu2_b, dyn_meta in branch_specs:
            Yu0 = combine_higgs(hu, Au_b)
            Yd0 = combine_higgs(hd, Ad_b)
            Ye0 = combine_higgs(hd, Ae_b)
            Ynu1_0 = combine_higgs(hu, Anu1_b)
            Ynu2_0 = combine_higgs(hu, Anu2_b)

            # Overall UV normalization max_f sigma_3(Y_f) = 1
            su0, _ = svd_left_real_split(Yu0)
            sd0, _ = svd_left_real_split(Yd0)
            se0, _ = svd_left_real_split(Ye0)
            smax = max(su0[2], sd0[2], se0[2])
            inv_smax = mp.mpf(1) / smax
            Yu_uv = mat3_scale(inv_smax, Yu0)
            Yd_uv = mat3_scale(inv_smax, Yd0)
            Ye_uv = mat3_scale(inv_smax, Ye0)
            Ynu1_uv = mat3_scale(inv_smax, Ynu1_0)
            Ynu2_uv = mat3_scale(inv_smax, Ynu2_0)

            I3 = mat3_eye()
            st0 = (
                g_uv, g_uv, g_uv, l1_D, l2_D, l3_D, l4_D,
                Yu_uv, Yd_uv, Ye_uv,
                mp.mpf(1), mp.mpf(1), I3, I3, I3, I3, I3,
            )
            st_ir, stab_ok, min_df, t_ewsb_u, t_ewsb_d = integrate_gl4(st0, mp.mpf(-35), 80, mode="2hdm2")
            obs = extract_ckm_and_pmns_obs(
                st_ir[7], st_ir[8], st_ir[9], Ynu1_uv, Ynu2_uv,
                st_ir[2], st_ir[10], st_ir[11], st_ir[12:17],
            )

            # Step-halving n=80 vs n=160 check on Static_CURVED_s12 at every vacuum (and all branches at tau_tot_70!)
            sh_err = None
            if bname == "Static_CURVED_s12" or vname == "tau_tot_70":
                st_ir_160, _, _, _, _ = integrate_gl4(st0, mp.mpf(-35), 160, mode="2hdm2")
                sh_err = state_diff_norm(st_ir, st_ir_160)
                if sh_err >= pow10(-6):
                    piece2_pass = False

            if vname == "tau_tot_70" and bname == "Static_CURVED_s12":
                saved_for_haar = (st0, Ynu1_uv, Ynu2_uv, obs)

            # Verify Piece 2 & 3 branch gates
            if not stab_ok or obs["min_sf"] <= 0 or abs(obs["S_IR"]) >= pow10(-25):
                piece2_pass = False
            for mr_d in obs["pmns"].values():
                if mr_d["takagi_rec_err"] >= pow10(-25) or mr_d["takagi_unit_err"] >= pow10(-25):
                    piece3_pass = False

            b_entry = {
                "stab_all_steps": stab_ok,
                "min_dflat_margin": fmt(min_df, 15),
                "step_halving_err_80_vs_160": fmt(sh_err, 10),
                "yt_over_g3": fmt(obs["yt_over_g3"], 20),
                "mb_over_mtau": fmt(obs["mb_over_mtau"], 20),
                "u23": fmt(obs["u23"], 20),
                "d23": fmt(obs["d23"], 20),
                "e23": fmt(obs["e23"], 20),
                "u13": fmt(obs["u13"], 20),
                "d13": fmt(obs["d13"], 20),
                "e13": fmt(obs["e13"], 20),
                "V12": fmt(obs["V12"], 20),
                "V23": fmt(obs["V23"], 20),
                "V13": fmt(obs["V13"], 20),
                "Jcp": fmt(obs["Jcp"], 20),
                "Jcp_signed": fmt(obs["Jcp_signed"], 20),
                "std_ckm": obs["std_ckm"],
                "m_Hu2_IR": fmt(obs["m_Hu2_IR"], 20),
                "m_Hd2_IR": fmt(obs["m_Hd2_IR"], 20),
                "t_EWSB_u": fmt(t_ewsb_u, 18),
                "t_EWSB_d": fmt(t_ewsb_d, 18),
                "min_sf": fmt(obs["min_sf"], 20),
                "S_IR": fmt(obs["S_IR"], 10),
                "EWSB_u_triggered": bool(obs["m_Hu2_IR"] < 0 and obs["min_sf"] > 0),
                "EWSB_d_triggered": bool(obs["m_Hd2_IR"] < 0 and obs["min_sf"] > 0),
                "pmns": {
                    mr_k: {
                        "s12_sq": fmt(mr_v["s12_sq"], 20),
                        "s23_sq": fmt(mr_v["s23_sq"], 20),
                        "s13_sq": fmt(mr_v["s13_sq"], 20),
                        "Jcp_nu": fmt(mr_v["Jcp_nu"], 20),
                        "dm21_over_dm31": fmt(mr_v["dm21_over_dm31"], 20),
                        "m_ratios": [fmt(x, 18) for x in mr_v["m_ratios"]],
                        "takagi_rec_err": fmt(mr_v["takagi_rec_err"], 8),
                        "takagi_unit_err": fmt(mr_v["takagi_unit_err"], 8),
                    }
                    for mr_k, mr_v in obs["pmns"].items()
                },
            }
            if dyn_meta is not None:
                b_entry["dynamic_v4_opt"] = {
                    "E_opt": fmt(dyn_meta["E_opt"], 20),
                    "rgrad_norm": fmt(dyn_meta["rgrad_norm"], 10),
                    "hu_hd_overlap": fmt(dyn_meta["hu_hd_overlap"], 20),
                }
            branches_out[vname][bname] = b_entry

    # Check radiative EWSB triggered at all 3 vacua and m_Hu^2 crossing first at tau_tot_70
    ewsb_all_vacua = all(
        branches_out[vn]["Static_CURVED_s12"]["EWSB_u_triggered"] for vn in ("omega", "tau_FILQ1", "tau_tot_70")
    )
    t_u_70 = branches_out["tau_tot_70"]["Static_CURVED_s12"]["t_EWSB_u"]
    t_d_70 = branches_out["tau_tot_70"]["Static_CURVED_s12"]["t_EWSB_d"]
    u_crosses_first_70 = bool(
        t_u_70 is not None and (t_d_70 is None or mp.mpf(t_u_70) > mp.mpf(t_d_70))
    )

    # 4. Guardrail 3: 10-trial Cayley-transform Haar U(3)^5 x U(3)_{nu_R} scrambling
    st_ref, Ynu1_ref, Ynu2_ref, obs_ref = saved_for_haar
    MR_2w_ref = mat3_scale(rat(1, 2), mat3_add(Ynu2_ref, mat3_T(Ynu2_ref)))
    max_haar_drift = mp.mpf(0)
    trial_drifts = []
    for tr in range(10):
        base_seed = 918273645 + tr * 104729
        UQ = make_cayley_unitary(base_seed + 1)
        Uu = make_cayley_unitary(base_seed + 2)
        Ud = make_cayley_unitary(base_seed + 3)
        UL = make_cayley_unitary(base_seed + 4)
        Ue = make_cayley_unitary(base_seed + 5)
        UnuR = make_cayley_unitary(base_seed + 6)

        Yu_sc = mat3_mul(mat3_mul(UQ, st_ref[7]), mat3_dag(Uu))
        Yd_sc = mat3_mul(mat3_mul(UQ, st_ref[8]), mat3_dag(Ud))
        Ye_sc = mat3_mul(mat3_mul(UL, st_ref[9]), mat3_dag(Ue))
        Ynu1_sc = mat3_mul(mat3_mul(UL, Ynu1_ref), mat3_dag(UnuR))
        MR2_sc = mat3_mul(mat3_mul(mat3_conj(UnuR), MR_2w_ref), mat3_dag(UnuR))
        MQ2_sc = mat3_mul(mat3_mul(UQ, st_ref[12]), mat3_dag(UQ))
        Mu2_sc = mat3_mul(mat3_mul(Uu, st_ref[13]), mat3_dag(Uu))
        Md2_sc = mat3_mul(mat3_mul(Ud, st_ref[14]), mat3_dag(Ud))
        ML2_sc = mat3_mul(mat3_mul(UL, st_ref[15]), mat3_dag(UL))
        Me2_sc = mat3_mul(mat3_mul(Ue, st_ref[16]), mat3_dag(Ue))

        st_sc0 = (
            st_ref[0], st_ref[1], st_ref[2], st_ref[3], st_ref[4], st_ref[5], st_ref[6],
            Yu_sc, Yd_sc, Ye_sc, st_ref[10], st_ref[11],
            MQ2_sc, Mu2_sc, Md2_sc, ML2_sc, Me2_sc,
        )
        st_sc_ir, _, _, _, _ = integrate_gl4(st_sc0, mp.mpf(-35), 80, mode="2hdm2")
        # Extract observables with the scrambled MR2_sc
        su_s, Uu_s = svd_left_real_split(st_sc_ir[7])
        sd_s, Ud_s = svd_left_real_split(st_sc_ir[8])
        se_s, Ue_s = svd_left_real_split(st_sc_ir[9])
        V_s = mat3_mul(mat3_dag(Uu_s), Ud_s)
        J_s = abs(mp.im(V_s[0][1] * V_s[1][2] * mp.conj(V_s[0][2]) * mp.conj(V_s[1][1])))
        min_sf_s = min(min(herm3_eig_real_split(M)[0]) for M in st_sc_ir[12:17])
        kappa_s = mat3_mul(mat3_mul(Ynu1_sc, mat3_inv(MR2_sc)), mat3_T(Ynu1_sc))
        mnu_s, Unu_s, _, _ = autonne_takagi_real_split(kappa_s)
        Upm_s = mat3_mul(mat3_dag(Ue_s), Unu_s)
        s13_s = abs(Upm_s[0][2]) ** 2
        c13_s = mp.mpf(1) - s13_s
        s12_s = (abs(Upm_s[0][1]) ** 2) / c13_s
        s23_s = (abs(Upm_s[1][2]) ** 2) / c13_s
        Jnu_s = abs(mp.im(Upm_s[0][1] * Upm_s[1][2] * mp.conj(Upm_s[0][2]) * mp.conj(Upm_s[1][1])))
        rdm_s = (mnu_s[1] ** 2 - mnu_s[0] ** 2) / (mnu_s[2] ** 2 - mnu_s[0] ** 2)

        ref_pm = obs_ref["pmns"]["sym_Ynu_2w"]
        checks = [
            abs(su_s[2] / st_sc_ir[2] - obs_ref["yt_over_g3"]),
            abs(sd_s[2] / se_s[2] - obs_ref["mb_over_mtau"]),
            abs(su_s[1] / su_s[2] - obs_ref["u23"]),
            abs(sd_s[1] / sd_s[2] - obs_ref["d23"]),
            abs(se_s[1] / se_s[2] - obs_ref["e23"]),
            abs(abs(V_s[0][1]) - obs_ref["V12"]),
            abs(abs(V_s[1][2]) - obs_ref["V23"]),
            abs(abs(V_s[0][2]) - obs_ref["V13"]),
            abs(J_s - obs_ref["Jcp"]),
            abs(st_sc_ir[10] - obs_ref["m_Hu2_IR"]),
            abs(st_sc_ir[11] - obs_ref["m_Hd2_IR"]),
            abs(min_sf_s - obs_ref["min_sf"]),
            abs(s12_s - ref_pm["s12_sq"]),
            abs(s23_s - ref_pm["s23_sq"]),
            abs(s13_s - ref_pm["s13_sq"]),
            abs(Jnu_s - ref_pm["Jcp_nu"]),
            abs(rdm_s - ref_pm["dm21_over_dm31"]),
        ]
        tdrift = max(checks)
        trial_drifts.append(tdrift)
        if tdrift > max_haar_drift:
            max_haar_drift = tdrift

    haar_pass = bool(max_haar_drift < pow10(-25))
    rg3_pass = bool(g4_bench["all_pass"] and gb_all_ok and omega_iso_ok)
    rg4_pass = bool(piece2_pass and ewsb_all_vacua and u_crosses_first_70 and abs(uv_dflat) < pow10(-35))
    rg5_pass = bool(piece3_pass and haar_pass)

    rp3_out = {
        "guardrail4_benchmarks": g4_bench,
        "curved_dirac_G_s12": {
            vn: {
                "area_over_2pi": fmt(gd["area_over_2pi"], 15),
                "gauss_bonnet_err": fmt(gd["gauss_bonnet_err"], 10),
                "g_raw": [fmt(x, 18) for x in gd["g_raw"]],
                "g_norm": [fmt(x, 18) for x in gd["g_norm"]],
                "anisotropy": fmt(gd["anisotropy"], 10),
            }
            for vn, gd in g_s12_all.items()
        },
        "UV_dflat_boundary": {
            "l1_D": fmt(l1_D, 15),
            "l2_D": fmt(l2_D, 15),
            "l3_D": fmt(l3_D, 15),
            "l4_D": fmt(l4_D, 15),
            "dflat_value": fmt(uv_dflat, 10),
        },
        "branches": branches_out,
        "ewsb_u_crosses_first_at_tau_tot_70": u_crosses_first_70,
        "guardrail3_cayley_haar_10_trials": {
            "num_trials": 10,
            "max_drift": fmt(max_haar_drift, 10),
            "trial_drifts": [fmt(d, 8) for d in trial_drifts],
            "pass_lt_1e25": haar_pass,
        },
        "RG3_pass": rg3_pass,
        "RG4_pass": rg4_pass,
        "RG5_pass": rg5_pass,
    }
    return rp3_out, saved_for_haar


# ============================================================================
# MODULE RP4: 6/6 PLANTED NEGATIVE CONTROLS (RPF1-RPF6) & REFEREE GATES
# ============================================================================

def run_rp4(filq_vacua, saved_for_haar, frame_c, pts_288):
    mp.mp.dps = 36
    tau_gen = mp.mpc(rat(137, 1000), rat(1213, 1000))

    # RPF1: Drop -3/(pi y) from E2_hat -> breaks S-invariance of V_FILQ,1 (> 0.1)
    v_bad_0 = V_FILQ(tau_gen, 1, drop_nonhol=True)
    v_bad_S = V_FILQ(-mp.mpc(1) / tau_gen, 1, drop_nonhol=True)
    rpf1_rel = abs(v_bad_S - v_bad_0) / abs(v_bad_0)
    rpf1_pass = bool(rpf1_rel > rat(1, 10))

    # RPF2: Sub-critical V_FILQ,1 + 70 V_CW(1) at 1/2 + 4i -> < -10^9 cusp runaway
    tau_h4i = mp.mpc(rat(1, 2), mp.mpf(4))
    L2_h4i, _, _, _, _ = solve_L2_fd_covariant(tau_h4i, high_prec=False)
    vcw_h4i = eval_all288_potentials(tau_h4i, L2_h4i, pts_288, frame_c)["V_CW_1"]
    v_subcrit = V_FILQ(tau_h4i, 1) + mp.mpf(70) * vcw_h4i
    rpf2_pass = bool(v_subcrit < -pow10(9))

    # RPF3: Shift off tau_FILQ1^* by (+1/10, +1/10) -> dV > 0.01, |grad V| > 0.5
    tau_f1 = filq_vacua[1]
    v_f1_min = V_FILQ(tau_f1, 1)
    tau_pert = tau_f1 + mp.mpc(rat(1, 10), rat(1, 10))
    v_pert, gx_p, gy_p, _, _, _, _, _ = grad_hess_2d_fd4(
        lambda t: V_FILQ(t, 1), mp.re(tau_pert), mp.im(tau_pert), pow10(-8), pow10(-8)
    )
    dV_pert = v_pert - v_f1_min
    grad_pert = mp.hypot(gx_p, gy_p)
    rpf3_pass = bool(dV_pert > rat(1, 100) and grad_pert > rat(1, 2))

    # RPF4: Degenerate M_R = Y_nu^T Y_nu -> exact kappa_nu = I_3, spread < 1e-25, ||k - I_3||_F < 1e-25
    st_ref, Ynu1_ref, Ynu2_ref, _ = saved_for_haar
    MR_deg = mat3_mul(mat3_T(Ynu1_ref), Ynu1_ref)
    kappa_deg = mat3_mul(mat3_mul(Ynu1_ref, mat3_inv(MR_deg)), mat3_T(Ynu1_ref))
    frob_id = mat3_frob(mat3_sub(kappa_deg, mat3_eye()))
    s_deg, _, _, _ = autonne_takagi_real_split(kappa_deg)
    spread_deg = (s_deg[2] - s_deg[0]) / s_deg[2]
    rpf4_pass = bool(spread_deg < pow10(-25) and frob_id < pow10(-25))

    # RPF5: Broken contraction Y_nu^T M_R^{-1} Y_nu under Cayley Haar -> fails U(3)_L (> 0.5)
    MR_2w = mat3_scale(rat(1, 2), mat3_add(Ynu2_ref, mat3_T(Ynu2_ref)))
    kb_0 = mat3_mul(mat3_mul(mat3_T(Ynu1_ref), mat3_inv(MR_2w)), Ynu1_ref)
    sb_0, _, _, _ = autonne_takagi_real_split(kb_0)
    UL_bad = make_cayley_unitary(777111333)
    UnuR_bad = make_cayley_unitary(999222444)
    Ynu_bad = mat3_mul(mat3_mul(UL_bad, Ynu1_ref), mat3_dag(UnuR_bad))
    MR_bad = mat3_mul(mat3_mul(mat3_conj(UnuR_bad), MR_2w), mat3_dag(UnuR_bad))
    kb_sc = mat3_mul(mat3_mul(mat3_T(Ynu_bad), mat3_inv(MR_bad)), Ynu_bad)
    sb_sc, _, _, _ = autonne_takagi_real_split(kb_sc)
    rpf5_drift = max(abs(sb_sc[i] - sb_0[i]) / abs(sb_0[i]) for i in range(3) if sb_0[i] > 0)
    rpf5_pass = bool(rpf5_drift > rat(1, 2))

    # RPF6: Zeroing all Yukawas -> kills radiative EWSB (m_Hu^2 = m_Hd^2 = +1, no zero crossing)
    Z3 = mat3_zero()
    st_zero = (
        st_ref[0], st_ref[1], st_ref[2], st_ref[3], st_ref[4], st_ref[5], st_ref[6],
        Z3, Z3, Z3, mp.mpf(1), mp.mpf(1),
        mat3_eye(), mat3_eye(), mat3_eye(), mat3_eye(), mat3_eye(),
    )
    st_z_ir, _, _, tu_z, td_z = integrate_gl4(st_zero, mp.mpf(-35), 40, mode="2hdm2")
    rpf6_pass = bool(
        abs(st_z_ir[10] - mp.mpf(1)) < pow10(-25)
        and abs(st_z_ir[11] - mp.mpf(1)) < pow10(-25)
        and tu_z is None
        and td_z is None
    )

    all_rpf = bool(rpf1_pass and rpf2_pass and rpf3_pass and rpf4_pass and rpf5_pass and rpf6_pass)
    return {
        "RPF1_drop_nonhol_E2": {"S_rel_err": fmt(rpf1_rel, 15), "pass": rpf1_pass},
        "RPF2_subcritical_FILQ1_runaway": {"V_at_half_4i": fmt(v_subcrit, 20), "pass": rpf2_pass},
        "RPF3_off_minimum_shift": {
            "dV": fmt(dV_pert, 15),
            "grad_norm": fmt(grad_pert, 15),
            "pass": rpf3_pass,
        },
        "RPF4_degenerate_MR_YnuTYnu": {
            "frob_kappa_minus_I3": fmt(frob_id, 10),
            "spectral_spread": fmt(spread_deg, 10),
            "pass": rpf4_pass,
        },
        "RPF5_broken_contraction_haar": {"rel_drift": fmt(rpf5_drift, 15), "pass": rpf5_pass},
        "RPF6_zero_yukawa_kills_ewsb": {
            "m_Hu2_IR": fmt(st_z_ir[10], 20),
            "m_Hd2_IR": fmt(st_z_ir[11], 20),
            "t_EWSB_u": tu_z,
            "t_EWSB_d": td_z,
            "pass": rpf6_pass,
        },
        "all_6_rpf_pass": all_rpf,
    }


# ============================================================================
# MAIN ENTRYPOINT
# ============================================================================

def main():
    t_start = time.monotonic_ns()
    script_path = os.path.abspath(__file__)
    out_dir = os.path.dirname(script_path)
    out_json_path = os.path.join(out_dir, "referee_a2_p629_veff_modulus_v2_out.json")
    out_sha_path = os.path.join(out_dir, "OUTPUT_SHA256.txt")

    ast_audit = self_audit_ast(script_path)
    if not ast_audit["clean"]:
        raise RuntimeError(f"AST self-audit failed: {ast_audit}")

    t1 = time.monotonic_ns()
    rp1_out, filq_vacua = run_rp1()
    t2 = time.monotonic_ns()
    rp2_out, vacua_data, frame_c, pts_288 = run_rp2(filq_vacua)
    t3 = time.monotonic_ns()
    rp3_out, saved_for_haar = run_rp3(vacua_data, frame_c)
    t4 = time.monotonic_ns()
    rp4_out = run_rp4(filq_vacua, saved_for_haar, frame_c, pts_288)
    t5 = time.monotonic_ns()

    rg6_pass = bool(rp4_out["all_6_rpf_pass"] and ast_audit["clean"])
    gates = {
        "RG1": rp1_out["RG1_pass"],
        "RG2": rp2_out["RG2_pass"],
        "RG3": rp3_out["RG3_pass"],
        "RG4": rp3_out["RG4_pass"],
        "RG5": rp3_out["RG5_pass"],
        "RG6": rg6_pass,
    }
    gates_passed = sum(1 for v in gates.values() if v)
    rpf_passed = sum(
        1
        for k in (
            "RPF1_drop_nonhol_E2",
            "RPF2_subcritical_FILQ1_runaway",
            "RPF3_off_minimum_shift",
            "RPF4_degenerate_MR_YnuTYnu",
            "RPF5_broken_contraction_haar",
            "RPF6_zero_yukawa_kills_ewsb",
        )
        if rp4_out[k]["pass"]
    )

    payload = {
        "card": "AGY-002_A2-P629-VEFF-MODULUS",
        "role": "100% Blind Disjoint Cold-Room Zero-Trust Referee v2",
        "empirical_inputs_used": "0 of 19",
        "ast_audit": ast_audit,
        "disjoint_algorithms": {
            "eta_E2": "Euler pentagonal number theorem + exact log derivative 1 + 24 q P'(q)/P(q)",
            "wp": "Exact Jacobi theta_1 logarithmic derivative -d_z^2 ln theta_1(pi z, tau) - (pi^2/3) E2",
            "L2_fuchsian": "Explicit 6th-order Yoshida-Suzuki (15-stage) symplectic splitting + variational Newton + Frobenius match + Vandermonde extrapolation + FD cocycle",
            "linalg_and_takagi": "Real-split 6x6 symmetric mp.eigsy (zero mp.eigh / mp.svd_c)",
            "curved_G_s12": "Piecewise Voronoi Clenshaw-Curtis polar quadrature + 4th-order Suzuki-Yoshida symplectic ODE",
            "rge_integrator": "Implicit 2-stage 4th-order Gauss-Legendre (GL4) fixed-point integrator",
            "haar_scrambling": "10-trial Cayley-transform U = (I - i A)(I + i A)^{-1} over U(3)^5 x U(3)_{nu_R}",
        },
        "RP1": rp1_out,
        "RP2": rp2_out,
        "RP3": rp3_out,
        "RP4": rp4_out,
        "gates": gates,
        "gates_passed": gates_passed,
        "gates_total": 6,
        "rpf_passed": rpf_passed,
        "rpf_total": 6,
        "all_gates_pass": bool(gates_passed == 6),
        "timing_ms": {
            "RP1": (t2 - t1) // 1000000,
            "RP2": (t3 - t2) // 1000000,
            "RP3": (t4 - t3) // 1000000,
            "RP4": (t5 - t4) // 1000000,
            "total": (t5 - t_start) // 1000000,
        },
    }

    assert_no_json_floats(payload)
    json_bytes = (json.dumps(payload, indent=2, sort_keys=False) + "\n").encode("utf-8")
    with open(out_json_path, "wb") as fh:
        fh.write(json_bytes)

    # Re-parse serialized JSON to certify zero JSON floats on disk!
    parsed = json.loads(json_bytes.decode("utf-8"))
    assert_no_json_floats(parsed)

    out_sha = hashlib.sha256(json_bytes).hexdigest()
    with open(out_sha_path, "w", encoding="utf-8") as fh:
        fh.write(f"{out_sha}  referee_a2_p629_veff_modulus_v2_out.json\n")

    print(
        f"REFEREE_V2_DONE gates={gates_passed}/6 rpf={rpf_passed}/6 "
        f"total_ms={payload['timing_ms']['total']} out_sha256={out_sha}"
    )


if __name__ == "__main__":
    main()
