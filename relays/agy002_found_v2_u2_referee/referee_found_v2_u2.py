#!/usr/bin/env python3
"""Cold-Room Independent Zero-Trust Referee for Gate F-U2 (AGY-002_FOUND-V2-U2).

Strict Cold-Room & Guardrail compliance:
- Zero imports from frontier/, producer directories, or third-party linalg (no numpy/scipy).
- Pure stdlib + mpmath with independent numerical methods:
  * Section 0: AST zero-float/zero-complex-literal self-audit, SHA-256 custody checks,
    and Cauchy-Riemann Richardson-extrapolated RK4 shooting ODE solver for L_2(tau)
    with left-SL_2(Z) Gauss reduction and cusp limit pi + ln(pi) - 3 ln(2) for y >= 12.
  * Section 1: Exact SL_2(Z) RREF intertwiner + Dedekind eta quaternion Yukawa Y_{(1,2)}
    joined with W_5 Weil representations (m = 1 and m = 3) at tau_0 and tau_1 (dps = 45).
  * Section 2: Cyclic Hermitian Jacobi K_f^{-1/2} cross-checked with coupled Newton-Schulz
    (< 1e-30 at tau_0), Hestenes one-sided Jacobi SVD, 10-trial Haar SU(3)^5 scrambling
    invariance, T/S invariance, bulk tau_0 lepton-down separation, and y = 6 (dps = 85),
    y = 30 (dps = 180) cusp alignment and lepton-down separation for S (m = 1) and tilde_S (m = 3).
  * Section 3: Symmetric points tau = i and tau = rho (dps = 50) forced null mode verification.
  * Section 4: Planted fault controls PFU2-1..PFU2-5 (Card + Erratum exact bars).
"""

import ast
import hashlib
import json
import math
import pathlib
import sys
import time
import mpmath as mp


ALLOWED_IMPORT_ROOTS = {
    "ast",
    "hashlib",
    "json",
    "math",
    "mpmath",
    "pathlib",
    "sys",
    "time",
}


def mp_rat(p, q):
    """Exact mpmath rational p / q without float literals."""
    return mp.mpf(int(p)) / int(q)


def pow10_mp(k):
    """Exact mpmath power of ten 10**k without float literals."""
    return mp.mpf(int(10)) ** int(k)


def pow10_f(k):
    """Python float 10**k via integer exponentiation without float literals."""
    if int(k) >= 0:
        return int(10) ** int(k) / int(1)
    return int(1) / (int(10) ** int(-k))


def f_rat(p, q):
    """Python float p / q without float literals."""
    return int(p) / int(q)


def mp_j():
    """Imaginary unit i without complex literals."""
    return mp.mpc(int(0), int(1))


def fmt_mp(val, digits=20):
    """Format high-precision mpmath real/scalar cleanly."""
    return mp.nstr(val, int(digits))


# =============================================================================
# SECTION 0A: AST & SHA-256 CUSTODY VERIFICATION
# =============================================================================

def audit_self_ast(script_path):
    """Verify 0 float/complex AST literals and 0 disallowed imports in self."""
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_literals = []
    complex_literals = []
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals.append((getattr(node, "lineno", int(0)), repr(node.value)))
            elif isinstance(node.value, complex):
                complex_literals.append((getattr(node, "lineno", int(0)), repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_roots.add(node.module.split(".")[0])
            else:
                imported_roots.add("<relative>")
    disallowed = sorted(imported_roots - ALLOWED_IMPORT_ROOTS)
    assert len(float_literals) == 0, f"Found float AST literals: {float_literals}"
    assert len(complex_literals) == 0, f"Found complex AST literals: {complex_literals}"
    assert len(disallowed) == 0, f"Found disallowed imports: {disallowed}"
    return {
        "float_literal_count": len(float_literals),
        "complex_literal_count": len(complex_literals),
        "imported_roots": sorted(imported_roots),
        "disallowed_imports": disallowed,
        "ast_clean": True,
    }


def verify_sha256_manifest(manifest_path, repo_root):
    """Read ONLY the SHA-256 hex digest line and check raw bytes on disk."""
    text = manifest_path.read_text(encoding="utf-8").strip()
    parts = text.split()
    assert len(parts) >= 2, f"Malformed SHA256 file: {manifest_path}"
    expected_hex = parts[0].lower()
    target_rel = parts[1]
    assert len(expected_hex) == 64, f"Unexpected hex length in {manifest_path}"
    target_path = repo_root / target_rel
    assert target_path.is_file(), f"Missing target for {manifest_path}: {target_rel}"
    actual_hex = hashlib.sha256(target_path.read_bytes()).hexdigest().lower()
    assert actual_hex == expected_hex, f"SHA mismatch for {target_rel}"
    return {
        "manifest": str(manifest_path.relative_to(repo_root)),
        "target": target_rel,
        "sha256_prefix": actual_hex[:16],
        "sha256": actual_hex,
        "matched": actual_hex == expected_hex,
    }


# =============================================================================
# SECTION 0B: INDEPENDENT RK4 SHOOTING SOLVER FOR L_2(tau) + SL_2(Z) REDUCTION
# =============================================================================

def precompute_wp_qseries(tau, extra_guard=6):
    """Precompute q-series coefficients of Weierstrass wp(z; tau) and E_4."""
    j = mp_j()
    pi = mp.pi
    q = mp.exp(int(2) * j * pi * tau)
    coeffs = []
    qm = q
    pi2 = pi * pi
    e4 = mp.mpc(int(1))
    tol = pow10_mp(-(mp.mp.dps + int(extra_guard)))
    m = int(1)
    while abs(qm) > tol and m <= 120:
        t = qm / (int(1) - qm)
        coeffs.append((int(2) * pi * m, int(8) * pi2 * m * t))
        e4 += int(240) * (m ** 3) * t
        m += int(1)
        qm *= q
    return coeffs, pi2 / int(3), (pi ** 4 / int(15)) * e4


def eval_wp_qseries(z, coeffs, pi2_3):
    """Evaluate Weierstrass wp(z; tau) cleanly for |Im z| < Im tau."""
    pi = mp.pi
    s = (pi / mp.sin(pi * z)) ** 2 - pi2_3
    for twopi_m, c_m in coeffs:
        s += c_m * (int(1) - mp.cos(twopi_m * z))
    return s


def rk4_half_period_once(c_val, coeffs, pi2_3, g4_3, half_p, n_geo, n_lin):
    """Integrate w'' + (c + 1/4 wp(z)) w = 0 from z=0 to half_p using Frobenius + log-s RK4 + linear z RK4."""
    dir_t = half_p / abs(half_p)
    z0 = pow10_mp(-5) * dir_t
    z0_sq = z0 * z0
    z0_4 = z0_sq * z0_sq
    a1 = -c_val / int(4)
    a2 = (c_val * c_val / int(4) - g4_3 / int(4)) / int(16)
    b1 = c_val / int(4)
    b2 = -(int(8) * a2 + c_val * b1) / int(16)
    sqz = mp.sqrt(z0)
    lnz0 = mp.log(z0)
    u1 = sqz * (int(1) + a1 * z0_sq + a2 * z0_4)
    u1p = (mp_rat(1, 2) + mp_rat(5, 2) * a1 * z0_sq + mp_rat(9, 2) * a2 * z0_4) / sqz
    u2 = u1 * lnz0 + sqz * (b1 * z0_sq + b2 * z0_4)
    u2p = u1p * lnz0 + u1 / z0 + (mp_rat(5, 2) * b1 * z0_sq + mp_rat(9, 2) * b2 * z0_4) / sqz

    r0 = abs(z0)
    rm = abs(half_p) / int(4)
    sm = mp.log(rm / r0)
    hs = sm / int(n_geo)
    hs2 = hs / int(2)
    s = mp.mpf(int(0))
    y0_1, y1_1, y0_2, y1_2 = u1, z0 * u1p, u2, z0 * u2p

    def pot_s(sv):
        zv = z0 * mp.exp(sv)
        return (zv * zv) * (c_val + eval_wp_qseries(zv, coeffs, pi2_3) / int(4))

    p_start = pot_s(s)
    for _ in range(int(n_geo)):
        p_mid = pot_s(s + hs2)
        p_end = pot_s(s + hs)
        k1 = (y1_1, y1_1 - p_start * y0_1, y1_2, y1_2 - p_start * y0_2)
        st2 = (y0_1 + hs2 * k1[0], y1_1 + hs2 * k1[1], y0_2 + hs2 * k1[2], y1_2 + hs2 * k1[3])
        k2 = (st2[1], st2[1] - p_mid * st2[0], st2[3], st2[3] - p_mid * st2[2])
        st3 = (y0_1 + hs2 * k2[0], y1_1 + hs2 * k2[1], y0_2 + hs2 * k2[2], y1_2 + hs2 * k2[3])
        k3 = (st3[1], st3[1] - p_mid * st3[0], st3[3], st3[3] - p_mid * st3[2])
        st4 = (y0_1 + hs * k3[0], y1_1 + hs * k3[1], y0_2 + hs * k3[2], y1_2 + hs * k3[3])
        k4 = (st4[1], st4[1] - p_end * st4[0], st4[3], st4[3] - p_end * st4[2])
        y0_1 += (hs / int(6)) * (k1[0] + int(2) * k2[0] + int(2) * k3[0] + k4[0])
        y1_1 += (hs / int(6)) * (k1[1] + int(2) * k2[1] + int(2) * k3[1] + k4[1])
        y0_2 += (hs / int(6)) * (k1[2] + int(2) * k2[2] + int(2) * k3[2] + k4[2])
        y1_2 += (hs / int(6)) * (k1[3] + int(2) * k2[3] + int(2) * k3[3] + k4[3])
        s += hs
        p_start = p_end

    zm = z0 * mp.exp(sm)
    u1, u1p, u2, u2p = y0_1, y1_1 / zm, y0_2, y1_2 / zm
    hz = (half_p - zm) / int(n_lin)
    hz2 = hz / int(2)
    z = zm

    def pot_z(zv):
        return c_val + eval_wp_qseries(zv, coeffs, pi2_3) / int(4)

    p_start = pot_z(z)
    for _ in range(int(n_lin)):
        p_mid = pot_z(z + hz2)
        p_end = pot_z(z + hz)
        k1 = (u1p, -p_start * u1, u2p, -p_start * u2)
        k2 = (u1p + hz2 * k1[1], -p_mid * (u1 + hz2 * k1[0]), u2p + hz2 * k1[3], -p_mid * (u2 + hz2 * k1[2]))
        k3 = (u1p + hz2 * k2[1], -p_mid * (u1 + hz2 * k2[0]), u2p + hz2 * k2[3], -p_mid * (u2 + hz2 * k2[2]))
        k4 = (u1p + hz * k3[1], -p_end * (u1 + hz * k3[0]), u2p + hz * k3[3], -p_end * (u2 + hz * k3[2]))
        u1 += (hz / int(6)) * (k1[0] + int(2) * k2[0] + int(2) * k3[0] + k4[0])
        u1p += (hz / int(6)) * (k1[1] + int(2) * k2[1] + int(2) * k3[1] + k4[1])
        u2 += (hz / int(6)) * (k1[2] + int(2) * k2[2] + int(2) * k3[2] + k4[2])
        u2p += (hz / int(6)) * (k1[3] + int(2) * k2[3] + int(2) * k3[3] + k4[3])
        z += hz
        p_start = p_end
    return u1, u1p, u2, u2p


def rk4_half_period_rich(c_val, coeffs, pi2_3, g4_3, half_p, n_geo_base, n_lin_base):
    """Fourth-to-sixth order Richardson extrapolation of RK4 half-period values."""
    v1 = rk4_half_period_once(c_val, coeffs, pi2_3, g4_3, half_p, n_geo_base, n_lin_base)
    v2 = rk4_half_period_once(c_val, coeffs, pi2_3, g4_3, half_p, int(2) * n_geo_base, int(2) * n_lin_base)
    return tuple((int(16) * b - a) / int(15) for a, b in zip(v1, v2))


def solve_l2_rk4_unreduced(tau, c_guess=None):
    """Solve accessory parameter c and compute L_2(tau) unreduced via Cauchy-Riemann Newton + Richardson RK4."""
    j = mp_j()
    pi = mp.pi
    coeffs, pi2_3, g4_3 = precompute_wp_qseries(tau)
    if c_guess is None:
        c_guess = (pi * pi) / int(12)
    cr, ci = mp.re(c_guess), mp.im(c_guess)
    len_scale_B = max(int(1), int(mp.ceil(abs(tau))))
    for phase, n_step, tolp in [("coarse", int(80), pow10_mp(-9)), ("rich", int(200), pow10_mp(-13))]:
        n_lin_A = n_step
        n_lin_B = n_step * len_scale_B
        for _ in range(10):
            c = cr + j * ci
            if phase == "coarse":
                a1, a1p, a2, a2p = rk4_half_period_once(c, coeffs, pi2_3, g4_3, mp.mpf(int(1)) / int(2), n_step, n_lin_A)
                b1, b1p, b2, b2p = rk4_half_period_once(c, coeffs, pi2_3, g4_3, tau / int(2), n_step, n_lin_B)
            else:
                a1, a1p, a2, a2p = rk4_half_period_rich(c, coeffs, pi2_3, g4_3, mp.mpf(int(1)) / int(2), n_step, n_lin_A)
                b1, b1p, b2, b2p = rk4_half_period_rich(c, coeffs, pi2_3, g4_3, tau / int(2), n_step, n_lin_B)
            fA = a1 * a1p
            fB = b1 * b1p
            rA, rB = mp.im(fA), mp.im(fB)
            err = mp.sqrt(rA * rA + rB * rB)
            if err < tolp:
                if phase == "rich":
                    wA = abs(a1 * a2p - a1p * a2 - int(1))
                    wB = abs(b1 * b2p - b1p * b2 - int(1))
                    lA = pi - mp.re(a2 * a1p + a1 * a2p) / (int(2) * mp.re(fA))
                    lB = pi - mp.re(b2 * b1p + b1 * b2p) / (int(2) * mp.re(fB))
                    return c, lA, lB, wA, wB, err
                break
            h = pow10_mp(-7) if phase == "coarse" else pow10_mp(-9)
            if phase == "coarse":
                ar1, ar1p, _, _ = rk4_half_period_once(c + h, coeffs, pi2_3, g4_3, mp.mpf(int(1)) / int(2), n_step, n_lin_A)
                br1, br1p, _, _ = rk4_half_period_once(c + h, coeffs, pi2_3, g4_3, tau / int(2), n_step, n_lin_B)
            else:
                ar1, ar1p, _, _ = rk4_half_period_rich(c + h, coeffs, pi2_3, g4_3, mp.mpf(int(1)) / int(2), n_step, n_lin_A)
                br1, br1p, _, _ = rk4_half_period_rich(c + h, coeffs, pi2_3, g4_3, tau / int(2), n_step, n_lin_B)
            dfA = (ar1 * ar1p - fA) / h
            dfB = (br1 * br1p - fB) / h
            # Holomorphic Cauchy-Riemann Jacobian for Im(f(c))
            j00, j01 = mp.im(dfA), mp.re(dfA)
            j10, j11 = mp.im(dfB), mp.re(dfB)
            det = j00 * j11 - j01 * j10
            cr -= (j11 * rA - j01 * rB) / det
            ci -= (-j10 * rA + j00 * rB) / det
    raise RuntimeError(f"RK4 L_2 shooting did not converge at tau={tau}")


def l2_gauss_rk4(tau):
    """Evaluate L_2(tau) using exact left-SL_2(Z) Gauss reduction + exact cusp limit for y >= 12."""
    acc = mp.mpf(int(0))
    t = mp.mpc(tau)
    cusp_const = mp.pi + mp.log(mp.pi) - int(3) * mp.log(int(2))
    eps_unit = pow10_mp(-22)
    for _ in range(64):
        n_shift = int(mp.nint(mp.re(t)))
        t -= n_shift
        if mp.im(t) >= mp.mpf(int(12)):
            return cusp_const + acc, t, True
        if abs(t) < mp.mpf(int(1)) - eps_unit:
            acc -= mp.log(abs(t))
            t = -mp.mpf(int(1)) / t
        else:
            break
    _, lA, lB, _, _, _ = solve_l2_rk4_unreduced(t)
    assert abs(lA - lB) < pow10_mp(-9), f"Gauss A/B mismatch: {abs(lA - lB)}"
    return lA + acc, t, False


# =============================================================================
# LINEAR ALGEBRA PRIMITIVES (CYCLIC JACOBI, NEWTON-SCHULZ, HESTENES SVD, RREF)
# =============================================================================

def mp_nullspace(A):
    """Exact high-precision RREF right-nullspace solver."""
    tol = pow10_mp(-(mp.mp.dps - int(22)))
    m, n = A.rows, A.cols
    M = mp.matrix(A)
    piv_cols = []
    r = int(0)
    for c in range(n):
        if r >= m:
            break
        best_r = r
        best_v = abs(M[r, c])
        for rr in range(r + int(1), m):
            av = abs(M[rr, c])
            if av > best_v:
                best_v = av
                best_r = rr
        if best_v <= tol:
            continue
        if best_r != r:
            for cc in range(c, n):
                M[r, cc], M[best_r, cc] = M[best_r, cc], M[r, cc]
        piv = M[r, c]
        for cc in range(c, n):
            M[r, cc] /= piv
        for rr in range(m):
            if rr != r and abs(M[rr, c]) > tol:
                fac = M[rr, c]
                for cc in range(c, n):
                    M[rr, cc] -= fac * M[r, cc]
        piv_cols.append(c)
        r += int(1)
    free_cols = [c for c in range(n) if c not in piv_cols]
    vecs = []
    for fc in free_cols:
        v = mp.zeros(n, int(1))
        v[fc] = mp.mpf(int(1))
        for rr, pc in enumerate(piv_cols):
            v[pc] = -M[rr, fc]
        vecs.append(v)
    return vecs


def cyclic_jacobi_eigh(H):
    """Cyclic Hermitian Jacobi eigensolver (NOT mp.eighe!). Returns ascending eigenvalues and U."""
    n = H.rows
    tol = pow10_mp(-(mp.mp.dps - int(8)))
    A = mp.matrix(H)
    for i in range(n):
        A[i, i] = mp.re(A[i, i])
        for k in range(i + int(1), n):
            avg = (A[i, k] + mp.conj(A[k, i])) / int(2)
            A[i, k] = avg
            A[k, i] = mp.conj(avg)
    V = mp.eye(n)
    tiny_floor = pow10_mp(-int(2) * mp.mp.dps)
    for _ in range(90):
        off = sum(abs(A[p, q]) for p in range(n) for q in range(p + int(1), n))
        diag_sum = sum(abs(A[i, i]) for i in range(n)) + int(1)
        if off <= tol * diag_sum:
            break
        for p in range(n):
            for q in range(p + int(1), n):
                apq = A[p, q]
                mag = abs(apq)
                if mag <= tol * mp.sqrt(abs(A[p, p] * A[q, q]) + tiny_floor):
                    continue
                app = mp.re(A[p, p])
                aqq = mp.re(A[q, q])
                tau_j = (aqq - app) / (int(2) * mag)
                if tau_j >= int(0):
                    t = int(1) / (tau_j + mp.sqrt(int(1) + tau_j * tau_j))
                else:
                    t = -int(1) / (-tau_j + mp.sqrt(int(1) + tau_j * tau_j))
                c = int(1) / mp.sqrt(int(1) + t * t)
                s = t * c
                u = apq / mag
                su = s * u
                suc = s * mp.conj(u)
                for k in range(n):
                    if k == p or k == q:
                        continue
                    akp, akq = A[k, p], A[k, q]
                    nkp = c * akp - suc * akq
                    nkq = su * akp + c * akq
                    A[k, p] = nkp
                    A[p, k] = mp.conj(nkp)
                    A[k, q] = nkq
                    A[q, k] = mp.conj(nkq)
                cross = int(2) * c * s * mag
                A[p, p] = c * c * app - cross + s * s * aqq
                A[q, q] = s * s * app + cross + c * c * aqq
                A[p, q] = mp.mpc(int(0))
                A[q, p] = mp.mpc(int(0))
                for k in range(n):
                    vkp, vkq = V[k, p], V[k, q]
                    V[k, p] = c * vkp - suc * vkq
                    V[k, q] = su * vkp + c * vkq
    evals = [mp.re(A[i, i]) for i in range(n)]
    order = sorted(range(n), key=lambda idx: evals[idx])
    Vs = mp.matrix(n, n)
    for cn, co in enumerate(order):
        for r in range(n):
            Vs[r, cn] = V[r, co]
    return [evals[idx] for idx in order], Vs


def inv_sqrt_jacobi(H):
    """Compute Hermitian K^{-1/2} via cyclic Hermitian Jacobi rotations."""
    ev, V = cyclic_jacobi_eigh(H)
    assert ev[0] > mp.mpf(int(0)), f"Non-positive Hermitian eigenvalue: {ev[0]}"
    return V * mp.diag([int(1) / mp.sqrt(e) for e in ev]) * V.H, ev


def inv_sqrt_newton_schulz(H):
    """Independent cross-check of K^{-1/2} via coupled Newton-Schulz iteration."""
    n = H.rows
    tr = mp.re(sum(H[i, i] for i in range(n)))
    Y = H / tr
    Z = mp.eye(n)
    i3 = int(3) * mp.eye(n)
    tol = pow10_mp(-(mp.mp.dps - int(8)))
    for _ in range(150):
        t_mat = (i3 - Z * Y) / int(2)
        yn = Y * t_mat
        zn = t_mat * Z
        if mp.mnorm(zn - Z) <= tol * mp.mnorm(zn):
            Z = zn
            break
        Y, Z = yn, zn
    return Z / mp.sqrt(tr)


def hestenes_svd(M):
    """One-sided Hestenes Jacobi SVD directly on M (avoids Y*Y^H squaring)."""
    n = M.rows
    tol = pow10_mp(-(mp.mp.dps - int(8)))
    A = mp.matrix(M)
    V = mp.eye(n)
    norm_a = mp.sqrt(sum(abs(A[r, c]) ** 2 for r in range(n) for c in range(n)))
    for _ in range(50):
        conv = True
        for p in range(n):
            for q in range(p + int(1), n):
                app = mp.re(sum(mp.conj(A[k, p]) * A[k, p] for k in range(n)))
                aqq = mp.re(sum(mp.conj(A[k, q]) * A[k, q] for k in range(n)))
                apq = sum(mp.conj(A[k, p]) * A[k, q] for k in range(n))
                mag = abs(apq)
                thr = tol * (mp.sqrt(app * aqq) + norm_a * (mp.sqrt(app) + mp.sqrt(aqq)) * tol + norm_a * norm_a * tol)
                if mag <= thr:
                    continue
                conv = False
                tau_j = (aqq - app) / (int(2) * mag)
                if tau_j >= int(0):
                    t = int(1) / (tau_j + mp.sqrt(int(1) + tau_j * tau_j))
                else:
                    t = -int(1) / (-tau_j + mp.sqrt(int(1) + tau_j * tau_j))
                c = int(1) / mp.sqrt(int(1) + t * t)
                s = t * c
                u = apq / mag
                su = s * u
                suc = s * mp.conj(u)
                for k in range(n):
                    akp, akq = A[k, p], A[k, q]
                    A[k, p] = c * akp - suc * akq
                    A[k, q] = su * akp + c * akq
                    vkp, vkq = V[k, p], V[k, q]
                    V[k, p] = c * vkp - suc * vkq
                    V[k, q] = su * vkp + c * vkq
        if conv:
            break
    norms = [mp.sqrt(mp.re(sum(mp.conj(A[k, i]) * A[k, i] for k in range(n)))) for i in range(n)]
    order = sorted(range(n), key=lambda idx: -norms[idx])
    sig = [norms[idx] for idx in order]
    U = mp.matrix(n, n)
    Vs = mp.matrix(n, n)
    zero_thr = norm_a * pow10_mp(-(mp.mp.dps - int(6)))
    for cn, co in enumerate(order):
        sc = norms[co]
        for r in range(n):
            Vs[r, cn] = V[r, co]
            U[r, cn] = (A[r, co] / sc) if sc > zero_thr else mp.mpc(int(0))
    return sig, U, Vs


def frob_norm(A):
    """Frobenius norm of an mpmath matrix."""
    return mp.sqrt(mp.re(sum(abs(A[i, l]) ** 2 for i in range(A.rows) for l in range(A.cols))))


def max_abs_diff_mat(A, B):
    """Max entrywise absolute difference between two mpmath matrices."""
    return max(abs(A[i, l] - B[i, l]) for i in range(A.rows) for l in range(A.cols))


# =============================================================================
# REPRESENTATION & MODULAR YUKAWA BUILDER (PURE MPMATH AT ACTIVE DPS)
# =============================================================================

def mp_kron(A, B):
    """Kronecker tensor product of mpmath matrices."""
    rA, cA = A.rows, A.cols
    rB, cB = B.rows, B.cols
    M = mp.zeros(rA * rB, cA * cB)
    for ia in range(rA):
        for ja in range(cA):
            a = A[ia, ja]
            if a == 0:
                continue
            for ib in range(rB):
                for jb in range(cB):
                    M[ia * rB + ib, ja * cB + jb] = a * B[ib, jb]
    return M


def build_intertwiner_basis():
    """Build exact SL_2(Z) intertwiner basis on (2_S3'_e8 + 1_e0) x (2_S3'_e16 + 1'_e16)."""
    j = mp_j()
    pi = mp.pi
    s3 = mp.sqrt(int(3))
    irreps = {
        "1": (mp.matrix([[int(1)]]), mp.matrix([[int(1)]])),
        "1'": (mp.matrix([[int(-1)]]), mp.matrix([[int(-1)]])),
        "2_S3'": (
            mp.matrix([[int(1), int(0)], [int(0), int(-1)]]),
            mp.matrix([[-mp_rat(1, 2), s3 / int(2)], [s3 / int(2), mp_rat(1, 2)]]),
        ),
    }
    Tq = mp.matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, j, 0], [0, 0, 0, j]])
    Sq = mp.matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, -1]])

    def sym_ts(d):
        dim = int(d) + int(1)
        T = mp.zeros(dim, dim)
        S = mp.zeros(dim, dim)
        p2 = mp.sqrt(int(2)) ** int(d)
        for idx, k in enumerate(range(int(d), int(-1), int(-1))):
            T[idx, idx] = j ** (int(d) - k)
            for a in range(k + int(1)):
                for b in range(int(d) - k + int(1)):
                    S[idx, int(d) - (a + b)] += math.comb(k, a) * math.comb(int(d) - k, b) * ((-1) ** (int(d) - k - b))
            for cc in range(dim):
                S[idx, cc] /= p2
        return T, S

    blocks = []
    for r in range(7):
        sT, sS = sym_ts(int(6) - r)
        blocks.append((r, mp.exp(j * pi * r / int(12)) * mp_kron(sT, Tq), mp_kron(sS, Sq)))

    def solve_block(nA, nB, k_exp):
        TA, SA = irreps[nA]
        TB, SB = irreps[nB]
        LT = mp.exp(j * pi * k_exp / int(12)) * mp_kron(TA, TB)
        LS = mp_kron(SA, SB)
        mdim = LT.rows
        da, db = TA.rows, TB.rows
        sols = []
        for r, WrT, WrS in blocks:
            wdim = WrT.rows
            E = mp.zeros(int(2) * mdim * wdim, mdim * wdim)
            for i in range(mdim):
                for l in range(mdim):
                    for p in range(wdim):
                        for q in range(wdim):
                            v1 = (LT[i, l] if p == q else int(0)) - (WrT[q, p] if i == l else int(0))
                            v2 = (LS[i, l] if p == q else int(0)) - (WrS[q, p] if i == l else int(0))
                            row = i * wdim + p
                            col = l * wdim + q
                            if v1 != 0:
                                E[row, col] = v1
                            if v2 != 0:
                                E[mdim * wdim + row, col] = v2
            vecs = mp_nullspace(E)
            if vecs:
                sols.append((r, da, db, wdim, vecs))
        return sols

    Ls = [("2_S3'", int(8)), ("1", int(0))]
    Rs = [("2_S3'", int(16)), ("1'", int(16))]
    terms = []
    r_off = int(0)
    for nL, kL in Ls:
        dL = irreps[nL][0].rows
        c_off = int(0)
        for nR, kR in Rs:
            dR = irreps[nR][0].rows
            k_tot = (kL + kR) % int(24)
            for r, da, db, wdim, vecs in solve_block(nL, nR, k_tot):
                for vi, v in enumerate(vecs):
                    # Skip linear-identity duplicate v4 in (2_S3', 2_S3', r=0) of r=6 q_2
                    if nL == "2_S3'" and nR == "2_S3'" and r == 0 and vi == 4:
                        continue
                    terms.append((r_off, da, c_off, db, r, wdim, v))
            c_off += dR
        r_off += dL
    assert len(terms) == 8, f"Expected 8 intertwiner basis elements, got {len(terms)}"
    return terms


def fixed_gaussian_coeffs():
    """Parameter-free canonical Gaussian integer couplings on the 8 basis terms (0 of 19)."""
    j = mp_j()
    norm_weights = [int(6), int(1), int(6), int(1), int(12), int(4), int(1), int(7)]
    gauss_weights = [
        mp.mpc(int(2), int(0)),
        mp.mpc(int(0), int(0)),
        -j,
        -int(2) * j,
        mp.mpc(int(0), int(0)),
        j,
        j,
        mp.mpc(int(1), int(0)),
    ]
    return [g * nw for g, nw in zip(gauss_weights, norm_weights)]


def dedekind_eta(tau):
    """Full Dedekind eta(tau) = exp(i pi tau / 12) prod_{m >= 1}(1 - q^m)."""
    j = mp_j()
    pi = mp.pi
    q = mp.exp(int(2) * j * pi * tau)
    res = mp.exp(j * pi * tau / int(12))
    prod_val = mp.mpc(int(1))
    qm = q
    tol = pow10_mp(-(mp.mp.dps + int(8)))
    for _ in range(1, 500):
        prod_val *= (int(1) - qm)
        qm *= q
        if abs(qm) < tol:
            break
    return res * prod_val


def theta_char(a, b, z, tau):
    """Jacobi theta[a, b](z, tau) truncated cleanly below working dps."""
    j = mp_j()
    pi = mp.pi
    y = mp.im(tau)
    n_max = int(mp.sqrt((mp.mp.dps + int(20)) * mp.log(int(10)) / (pi * y))) + int(6)
    s = mp.mpc(int(0))
    for n in range(-n_max, n_max + int(1)):
        na = n + a
        s += mp.exp(j * pi * tau * (na * na) + int(2) * j * pi * na * (z + b))
    return s


def psi2_level2(tau, u, v):
    """Standard level-2 theta doublet psi_2(tau, u, v) with torsion shift (u, v)."""
    j = mp_j()
    pi = mp.pi
    z = int(2) * (u - tau * v)
    pref = mp.exp(int(2) * j * pi * tau * (v * v))
    return mp.matrix([
        [pref * theta_char(mp.mpf(int(0)), mp.mpf(int(0)), z, int(2) * tau)],
        [pref * theta_char(mp_rat(1, 2), mp.mpf(int(0)), z, int(2) * tau)],
    ])


def eval_w4_blocks(tau, ac, bc, mul_r=2):
    """Evaluate covariant W_4 quaternion tensor product across weight/eta blocks r = 0..6."""
    u = mp_rat(ac, 5)
    v = mp_rat(bc, 5)
    M = psi2_level2(tau, u, v) * psi2_level2(tau, int(mul_r) * u, int(mul_r) * v).T
    p = psi2_level2(tau, mp.mpf(int(0)), mp.mpf(int(0)))
    e = dedekind_eta(tau)
    p0, p1 = p[0], p[1]
    qv = [M[0, 0] + M[1, 1], M[0, 0] - M[1, 1], M[0, 1] + M[1, 0], M[0, 1] - M[1, 0]]
    blocks = []
    for r in range(7):
        d = int(6) - r
        er = e ** r
        vec = []
        for k in range(d, int(-1), int(-1)):
            pk = er * (p0 ** k) * (p1 ** (d - k))
            for qvc in qv:
                vec.append(pk * qvc)
        blocks.append(vec)
    return blocks


def parity_eigenbasis_w5():
    """Unitary change of basis from Z_5 to W_3^+ (+) W_2^- (even/odd parity subspaces)."""
    U5 = mp.zeros(5, 5)
    is2 = int(1) / mp.sqrt(int(2))
    U5[0, 0] = mp.mpf(int(1))
    U5[1, 1] = is2
    U5[4, 1] = is2
    U5[2, 2] = is2
    U5[3, 2] = is2
    U5[1, 3] = is2
    U5[4, 3] = -is2
    U5[2, 4] = is2
    U5[3, 4] = -is2
    return U5


def weil_dm_table():
    """Precompute D_m(a_c, b_c) in W_3^+ (+) W_2^- basis for m = 1 (2x^2/5) and m = 3 (x^2/5)."""
    j = mp_j()
    pi = mp.pi
    z5 = mp.exp(int(2) * j * pi / int(5))
    U5 = parity_eigenbasis_w5()
    U5H = U5.H
    table = {int(1): {}, int(3): {}}
    for mc in (int(1), int(3)):
        kk = int(2) if mc == int(1) else int(1)
        for ac in range(-2, 3):
            for bc in range(-2, 3):
                if ac == 0 and bc == 0:
                    continue
                W = mp.zeros(5, 5)
                for x in range(5):
                    W[(x + bc) % int(5), x] = z5 ** ((kk * ac * bc + int(2) * kk * ac * x) % int(5))
                table[mc][(ac, bc)] = U5H * W * U5
    return table


def build_yukawa_and_operator(tau, terms, coeffs, dm_table, mc=1, mul_r=2, phased=True):
    """Build Y_table, Y_{base}, S_{ph}, O_3/O_2 blocks, 15x15 O_m, and Fock metrics G_{3,2}^{L,R}."""
    j = mp_j()
    pi = mp.pi
    z5 = mp.exp(int(2) * j * pi / int(5))
    et = dedekind_eta(tau)
    denom_hat = int(2) * pi * (et ** 3)
    denom = denom_hat * denom_hat
    Yt = {}
    for ac in range(-2, 3):
        for bc in range(-2, 3):
            bvs = [[val / denom for val in blk] for blk in eval_w4_blocks(tau, ac, bc, mul_r=mul_r)]
            Y = mp.zeros(3, 3)
            for bi, (rO, da, cO, db, r, wdim, v) in enumerate(terms):
                cw = coeffs[bi]
                if cw == 0:
                    continue
                b = bvs[r]
                for i in range(da):
                    for l in range(db):
                        s = mp.mpc(int(0))
                        base = (i * db + l) * wdim
                        for w in range(wdim):
                            vc = v[base + w]
                            if vc != 0:
                                s += vc * b[w]
                        Y[rO + i, cO + l] += cw * s
            Yt[(ac, bc)] = Y

    O3_b = [[mp.zeros(3, 3) for _ in range(3)] for _ in range(3)]
    O2_b = [[mp.zeros(3, 3) for _ in range(2)] for _ in range(2)]
    O_full = mp.zeros(15, 15)
    Y0 = Yt[(0, 0)]
    Sph = mp.zeros(3, 3)
    for ac in range(-2, 3):
        for bc in range(-2, 3):
            if ac == 0 and bc == 0:
                continue
            ph = (z5 ** ((-ac * bc) % int(5))) if phased else mp.mpc(int(1))
            Yw = ph * Yt[(ac, bc)]
            Sph += Yw
            D = dm_table[int(mc)][(ac, bc)]
            for a in range(3):
                for b in range(3):
                    dab = D[a, b]
                    if dab != 0:
                        O3_b[a][b] += dab * Yw
            for a in range(2):
                for b in range(2):
                    dab = D[int(3) + a, int(3) + b]
                    if dab != 0:
                        O2_b[a][b] += dab * Yw
            for i in range(3):
                for l in range(3):
                    yval = Yw[i, l]
                    if yval == 0:
                        continue
                    for a in range(5):
                        for b in range(5):
                            if D[a, b] != 0:
                                O_full[i * int(5) + a, l * int(5) + b] += yval * D[a, b]

    G3L = sum(O3_b[a][b] * O3_b[a][b].H for a in range(3) for b in range(3))
    G3R = sum(O3_b[a][b].H * O3_b[a][b] for a in range(3) for b in range(3))
    G2L = sum(O2_b[a][b] * O2_b[a][b].H for a in range(2) for b in range(2))
    G2R = sum(O2_b[a][b].H * O2_b[a][b] for a in range(2) for b in range(2))
    return {
        "Y_table": Yt,
        "base_w0": Y0,
        "phased_sum": Sph,
        "O3_blocks": O3_b,
        "O2_blocks": O2_b,
        "O_full": O_full,
        "G3L": G3L,
        "G2L": G2L,
        "G3R": G3R,
        "G2R": G2R,
    }


def compute_fock_metrics(bundle):
    """Gate F-U1 covariant Kahler metrics K_f from (G_3, G_2)."""
    G3L, G2L = bundle["G3L"], bundle["G2L"]
    G3R, G2R = bundle["G3R"], bundle["G2R"]
    return {
        "QL": G3L + G2L,
        "LL": int(3) * G3L + G2L,
        "uR": int(2) * G3R,
        "dR": int(2) * G3R + int(2) * G2R,
        "eR": int(2) * G2R,
    }


def extract_observables(bundle, scrambled_unitaries=None):
    """Compute physical Y_f^{phys}, singular value ratios r_u, r_d, r_e, |V_CKM|, and |U_u^H V_u|."""
    K = compute_fock_metrics(bundle)
    if scrambled_unitaries is not None:
        UQL, ULL, UuR, UdR, UeR = scrambled_unitaries
        KQL, _ = inv_sqrt_jacobi(UQL * K["QL"] * UQL.H)
        KLL, _ = inv_sqrt_jacobi(ULL * K["LL"] * ULL.H)
        KuR, _ = inv_sqrt_jacobi(UuR * K["uR"] * UuR.H)
        KdR, _ = inv_sqrt_jacobi(UdR * K["dR"] * UdR.H)
        KeR, _ = inv_sqrt_jacobi(UeR * K["eR"] * UeR.H)
    else:
        KQL, _ = inv_sqrt_jacobi(K["QL"])
        KLL, _ = inv_sqrt_jacobi(K["LL"])
        KuR, _ = inv_sqrt_jacobi(K["uR"])
        KdR, _ = inv_sqrt_jacobi(K["dR"])
        KeR, _ = inv_sqrt_jacobi(K["eR"])

    out = {}
    for tag in ("base_w0", "phased_sum"):
        Yh = bundle[tag]
        if scrambled_unitaries is not None:
            Yu_hol = UQL * Yh * UuR.H
            Yd_hol = UQL * Yh * UdR.H
            Ye_hol = ULL * Yh * UeR.H
        else:
            Yu_hol, Yd_hol, Ye_hol = Yh, Yh, Yh
        Yu = KQL * Yu_hol * KuR
        Yd = KQL * Yd_hol * KdR
        Ye = KLL * Ye_hol * KeR
        su, Uu, Vu = hestenes_svd(Yu)
        sd, Ud, _ = hestenes_svd(Yd)
        se, _, _ = hestenes_svd(Ye)
        V = Uu.H * Ud
        aV = mp.matrix([[abs(V[a, b]) for b in range(3)] for a in range(3)])
        min_v_diag = min(aV[i, i] for i in range(3))
        out[tag] = {
            "su": su,
            "sd": sd,
            "se": se,
            "ru": [su[1] / su[0], su[2] / su[0]],
            "rd": [sd[1] / sd[0], sd[2] / sd[0]],
            "re": [se[1] / se[0], se[2] / se[0]],
            "aV": aV,
            "min_V_diag": min_v_diag,
            "UuH_Vu_abs": mp.matrix([[abs((Uu.H * Vu)[a, b]) for b in range(3)] for a in range(3)]),
            "Yu": Yu,
            "Yd": Yd,
            "Ye": Ye,
        }
    return out


def make_haar_generator(seed_int):
    """Deterministic mpmath Haar SU(3)-like unitary generator via MGS QR on complex Gaussian entries."""
    state = [int(seed_int)]
    mod64 = int(2) ** int(64)

    def rand_unit():
        state[0] = (int(6364136223846793005) * state[0] + int(1442695040888963407)) % mod64
        return (mp.mpf(state[0]) + mp_rat(1, 2)) / mp.mpf(mod64)

    def randn_c():
        u1, u2 = rand_unit(), rand_unit()
        u3, u4 = rand_unit(), rand_unit()
        r1 = mp.sqrt(-int(2) * mp.log(u1))
        r2 = mp.sqrt(-int(2) * mp.log(u3))
        return mp.mpc(r1 * mp.cos(int(2) * mp.pi * u2), r2 * mp.sin(int(2) * mp.pi * u4))

    def haar_u(n=3):
        A = mp.matrix([[randn_c() for _ in range(n)] for _ in range(n)])
        Q = mp.matrix(n, n)
        for k in range(n):
            v = mp.matrix([[A[r, k]] for r in range(n)])
            for i in range(k):
                qi = mp.matrix([[Q[r, i]] for r in range(n)])
                proj = (qi.H * v)[0, 0]
                v -= proj * qi
            nv = mp.sqrt(sum(abs(v[r, 0]) ** 2 for r in range(n)))
            for r in range(n):
                Q[r, k] = v[r, 0] / nv
        return Q

    return haar_u


# =============================================================================
# MAIN REFEREE PIPELINE (SECTIONS 0..4)
# =============================================================================

def run_referee():
    t_start = time.time()
    script_path = pathlib.Path(__file__).resolve()
    referee_dir = script_path.parent
    repo_root = referee_dir.parent.parent

    # -------------------------------------------------------------------------
    # SECTION 0: AST, SHA CUSTODY, AND INDEPENDENT RK4 L_2 UNIFORMISATION
    # -------------------------------------------------------------------------
    print("[Section 0] AST zero-float/zero-complex scan & SHA-256 custody checks...", flush=True)
    ast_report = audit_self_ast(script_path)
    self_sha_manifest = referee_dir / "SCRIPT_SHA256.txt"
    assert self_sha_manifest.is_file(), f"Missing {self_sha_manifest}"
    sha_manifests = {
        "referee_script": verify_sha256_manifest(self_sha_manifest, repo_root),
        "producer_v1_script": verify_sha256_manifest(repo_root / "relays/agy002_found_v2_u2/SCRIPT_SHA256.txt", repo_root),
        "producer_v2_script": verify_sha256_manifest(repo_root / "relays/agy002_found_v2_u2_v2/SCRIPT_SHA256.txt", repo_root),
        "producer_v2_output": verify_sha256_manifest(repo_root / "relays/agy002_found_v2_u2_v2/OUTPUT_SHA256.txt", repo_root),
    }

    mp.mp.dps = int(32)
    j = mp_j()
    tau_0 = mp_rat(13, 100) + j * mp_rat(17, 10)
    t_rk4 = time.time()
    c0, l0_A, l0_B, w0_A, w0_B, e0 = solve_l2_rk4_unreduced(tau_0)
    _, lT_A, lT_B, wT_A, wT_B, _ = solve_l2_rk4_unreduced(tau_0 + int(1), c0)
    _, lS_A, lS_B, wS_A, wS_B, _ = solve_l2_rk4_unreduced(-mp.mpf(int(1)) / tau_0, (tau_0 * tau_0) * c0)
    assert abs(l0_A - l0_B) < pow10_mp(-10), f"|l0_A - l0_B|={abs(l0_A - l0_B)}"
    l0 = l0_A
    lT = lT_A
    lS = lS_A
    rk4_T_err = abs(lT - l0)
    rk4_S_err = abs(lS - (l0 + mp.log(abs(tau_0))))
    rk4_bar = pow10_mp(-11)
    assert rk4_T_err < rk4_bar, f"Unreduced RK4 T error {rk4_T_err} >= 1e-11"
    assert rk4_S_err < rk4_bar, f"Unreduced RK4 S error {rk4_S_err} >= 1e-11"

    l_red_T, t_red_T, cusp_T = l2_gauss_rk4(tau_0 + int(1))
    l_red_S, t_red_S, cusp_S = l2_gauss_rk4(-mp.mpf(int(1)) / tau_0)
    tau_cusp12 = mp_rat(13, 100) + j * int(12)
    l_cusp12, _, is_cusp12 = l2_gauss_rk4(tau_cusp12)
    tau_cusp30_inv = -mp.mpf(int(1)) / (mp_rat(13, 100) + j * int(30))
    l_cusp30_inv, t_cusp30_red, is_cusp30 = l2_gauss_rk4(tau_cusp30_inv)
    cusp_exact = mp.pi + mp.log(mp.pi) - int(3) * mp.log(int(2))
    assert abs(l_red_T - l0) < rk4_bar
    assert abs(l_red_S - (l0 + mp.log(abs(tau_0)))) < rk4_bar
    assert is_cusp12 and abs(l_cusp12 - cusp_exact) < pow10_mp(-25)
    assert is_cusp30 and abs(l_cusp30_inv - (cusp_exact + mp.log(abs(mp_rat(13, 100) + j * int(30))))) < pow10_mp(-25)

    sec0_out = {
        "ast_audit": ast_report,
        "sha256_custody": sha_manifests,
        "rk4_L2_tau0": fmt_mp(l0, 18),
        "rk4_AB_diff_tau0": float(abs(l0_A - l0_B)),
        "rk4_wronskian_errs_tau0": [float(w0_A), float(w0_B)],
        "rk4_unreduced_T_err": float(rk4_T_err),
        "rk4_unreduced_S_err": float(rk4_S_err),
        "gauss_cusp12_limit": fmt_mp(l_cusp12, 18),
        "gauss_S_cusp30_err": float(abs(l_cusp30_inv - (cusp_exact + mp.log(abs(mp_rat(13, 100) + j * int(30)))))),
        "rk4_elapsed_s": int(round(time.time() - t_rk4)),
        "pass": True,
    }
    print(f"[Section 0 PASS] L2(tau0)={fmt_mp(l0, 16)} T_err={float(rk4_T_err):.2e} S_err={float(rk4_S_err):.2e}", flush=True)

    # -------------------------------------------------------------------------
    # SECTION 1: P-874(1) / W-P1b WEIL-CLASS SEPARATION ON O_m(tau) (dps = 45)
    # -------------------------------------------------------------------------
    mp.mp.dps = int(45)
    j = mp_j()
    terms_45 = build_intertwiner_basis()
    coeffs_45 = fixed_gaussian_coeffs()
    dm_45 = weil_dm_table()
    tau_0 = mp_rat(13, 100) + j * mp_rat(17, 10)
    tau_1 = mp_rat(31, 100) + j * mp_rat(6, 5)

    sec1_out = {}
    bundles_bulk = {}
    for pname, tp in [("tau_0", tau_0), ("tau_1", tau_1)]:
        bundles_bulk[pname] = {}
        norm_sq_ev = {}
        sec1_pt = {}
        for mc in (int(1), int(3)):
            b_0 = build_yukawa_and_operator(tp, terms_45, coeffs_45, dm_45, mc=mc)
            b_T = build_yukawa_and_operator(tp + int(1), terms_45, coeffs_45, dm_45, mc=mc)
            b_S = build_yukawa_and_operator(-mp.mpf(int(1)) / tp, terms_45, coeffs_45, dm_45, mc=mc)
            bundles_bulk[pname][mc] = (b_0, b_T, b_S)
            Of = b_0["O_full"]
            off32 = max(
                abs(Of[i * int(5) + a, l * int(5) + b])
                for i in range(3)
                for l in range(3)
                for a in range(3)
                for b in range(3, 5)
            )
            off23 = max(
                abs(Of[i * int(5) + a, l * int(5) + b])
                for i in range(3)
                for l in range(3)
                for a in range(3, 5)
                for b in range(3)
            )
            off_norm = max(off32, off23)
            ev0, _ = cyclic_jacobi_eigh(Of * Of.H)
            evT, _ = cyclic_jacobi_eigh(b_T["O_full"] * b_T["O_full"].H)
            evS, _ = cyclic_jacobi_eigh(b_S["O_full"] * b_S["O_full"].H)
            sv0 = [mp.sqrt(max(e, mp.mpf(int(0)))) for e in ev0]
            svT = [mp.sqrt(max(e, mp.mpf(int(0)))) for e in evT]
            svS = [mp.sqrt(max(e, mp.mpf(int(0)))) for e in evS]
            dT = max(abs(svT[k] - sv0[k]) / sv0[k] for k in range(15))
            dS = max(abs(svS[k] / abs(tp) - sv0[k]) / sv0[k] for k in range(15))
            assert off_norm < pow10_mp(-25), f"{pname} m={mc} off-diag {off_norm}"
            assert dT < pow10_mp(-20), f"{pname} m={mc} dT {dT}"
            assert dS < pow10_mp(-20), f"{pname} m={mc} dS {dS}"

            e3_raw, _ = cyclic_jacobi_eigh(b_0["G3L"])
            e2_raw, _ = cyclic_jacobi_eigh(b_0["G2L"])
            s3_norm = [mp.sqrt(e) / mp.sqrt(e3_raw[-1]) for e in e3_raw]
            s2_norm = [mp.sqrt(e) / mp.sqrt(e2_raw[-1]) for e in e2_raw]
            norm_sq_ev[mc] = (s3_norm, s2_norm)
            sec1_pt[f"m{mc}"] = {
                "offdiag_3_2": fmt_mp(off_norm, 8),
                "sv15_T_drift": fmt_mp(dT, 8),
                "sv15_S_scaled_drift": fmt_mp(dS, 8),
            }
        dG3 = max(abs(norm_sq_ev[1][0][k] - norm_sq_ev[3][0][k]) for k in range(3))
        dG2 = max(abs(norm_sq_ev[1][1][k] - norm_sq_ev[3][1][k]) for k in range(2))
        assert dG3 > mp_rat(1, 20), f"{pname} dG3={dG3}"
        assert dG2 > mp_rat(1, 4), f"{pname} dG2={dG2}"
        sec1_pt["dG3_L_diff"] = float(dG3)
        sec1_pt["dG2_L_diff"] = float(dG2)
        sec1_out[pname] = sec1_pt
        print(f"[Section 1 {pname} PASS] dG3={float(dG3):.4f} (>0.05) dG2={float(dG2):.4f} (>0.25)", flush=True)

    # -------------------------------------------------------------------------
    # SECTION 2: FOCK KINETIC DRESSING, JACOBI VS NEWTON-SCHULZ, HAAR & CUSPS
    # -------------------------------------------------------------------------
    print("[Section 2] Jacobi vs Newton-Schulz, T/S invariance, 10-trial Haar SU(3)^5, cusps y=6,30...", flush=True)
    # Cross-check cyclic Jacobi vs coupled Newton-Schulz at tau_0
    K_t0 = compute_fock_metrics(bundles_bulk["tau_0"][1][0])
    ns_diffs = {}
    for kname, Hk in K_t0.items():
        Kj, _ = inv_sqrt_jacobi(Hk)
        Kns = inv_sqrt_newton_schulz(Hk)
        df = frob_norm(Kj - Kns)
        assert df < pow10_mp(-30), f"Jacobi vs NS mismatch on {kname}: {df}"
        ns_diffs[kname] = fmt_mp(df, 8)

    obs_bulk = {}
    sec2_bulk_out = {}
    for pname in ("tau_0", "tau_1"):
        sec2_bulk_out[pname] = {}
        obs_bulk[pname] = {}
        for mc in (int(1), int(3)):
            b_0, b_T, b_S = bundles_bulk[pname][mc]
            ob0 = extract_observables(b_0)
            obT = extract_observables(b_T)
            obS = extract_observables(b_S)
            obs_bulk[pname][mc] = ob0
            pt_rec = {}
            for tag in ("base_w0", "phased_sum"):
                dT = max(
                    max(abs(obT[tag][rk][i] - ob0[tag][rk][i]) for rk in ("ru", "rd", "re") for i in range(2)),
                    max_abs_diff_mat(obT[tag]["aV"], ob0[tag]["aV"]),
                )
                dS = max(
                    max(abs(obS[tag][rk][i] - ob0[tag][rk][i]) for rk in ("ru", "rd", "re") for i in range(2)),
                    max_abs_diff_mat(obS[tag]["aV"], ob0[tag]["aV"]),
                )
                assert dT < pow10_mp(-20), f"{pname} m={mc} {tag} T drift {dT}"
                assert dS < pow10_mp(-20), f"{pname} m={mc} {tag} S drift {dS}"
                sep = abs(ob0[tag]["re"][0] - ob0[tag]["rd"][0])
                if pname == "tau_0" and mc == 1:
                    assert sep > mp_rat(1, 2), f"tau_0 m=1 {tag} |re23-rd23|={sep} <= 1/2"
                pt_rec[tag] = {
                    "T_drift": fmt_mp(dT, 8),
                    "S_drift": fmt_mp(dS, 8),
                    "abs_re23_minus_rd23": float(sep),
                }
            sec2_bulk_out[pname][f"m{mc}"] = pt_rec

    # 10-trial Haar SU(3)^5 scrambling invariance at tau_0 and tau_1 (m=1, 3)
    haar_gen = make_haar_generator(int(20261119))
    max_haar_drift = mp.mpf(int(0))
    for pname in ("tau_0", "tau_1"):
        for mc in (int(1), int(3)):
            b_0 = bundles_bulk[pname][mc][0]
            ob0 = obs_bulk[pname][mc]
            for _ in range(10):
                unitaries = tuple(haar_gen(3) for _ in range(5))
                obs_s = extract_observables(b_0, scrambled_unitaries=unitaries)
                for tag in ("base_w0", "phased_sum"):
                    d = max(
                        max(abs(obs_s[tag][rk][i] - ob0[tag][rk][i]) for rk in ("ru", "rd", "re") for i in range(2)),
                        max_abs_diff_mat(obs_s[tag]["aV"], ob0[tag]["aV"]),
                    )
                    if d > max_haar_drift:
                        max_haar_drift = d
    assert max_haar_drift < pow10_mp(-25), f"10-trial Haar SU(3)^5 drift {max_haar_drift}"
    print(f"[Section 2 bulk PASS] Jacobi-vs-NS max<{ns_diffs['QL']} Haar10={fmt_mp(max_haar_drift, 6)}", flush=True)

    # Cusp y = 6 (dps = 85) and y = 30 (dps = 180) for both S (m=1) and tilde_S (m=3)
    cusp_out = {}
    for label, y_val, dps_val in [("cusp_y6", int(6), int(85)), ("cusp_y30", int(30), int(180))]:
        mp.mp.dps = dps_val
        j = mp_j()
        terms_c = build_intertwiner_basis()
        coeffs_c = fixed_gaussian_coeffs()
        dm_c = weil_dm_table()
        tau_c = mp_rat(13, 100) + j * y_val
        label_rec = {}
        for rname, mc in [("S", int(1)), ("tilde_S", int(3))]:
            b_c = build_yukawa_and_operator(tau_c, terms_c, coeffs_c, dm_c, mc=mc)
            ob_c = extract_observables(b_c)
            r_rec = {}
            for tag in ("base_w0", "phased_sum"):
                min_v = ob_c[tag]["min_V_diag"]
                one_minus_v = int(1) - min_v
                sep_23 = abs(ob_c[tag]["re"][0] / ob_c[tag]["rd"][0] - int(1))
                sep_13 = abs(ob_c[tag]["re"][1] / ob_c[tag]["rd"][1] - int(1))
                if y_val == 6:
                    assert min_v > mp_rat(999, 1000), f"{label} {rname} {tag} min_V={min_v}"
                    assert sep_23 > mp_rat(1, 5), f"{label} {rname} {tag} sep23={sep_23}"
                else:
                    assert one_minus_v < pow10_mp(-12), f"{label} {rname} {tag} 1-minV={one_minus_v}"
                    if rname == "S":
                        assert sep_23 > mp_rat(3, 5), f"{label} S {tag} sep23={sep_23}"
                    else:
                        assert sep_13 > mp_rat(3, 10), f"{label} tilde_S {tag} sep13={sep_13}"
                r_rec[tag] = {
                    "min_V_diag": fmt_mp(min_v, 20),
                    "one_minus_min_V": fmt_mp(one_minus_v, 8),
                    "rel_sep_23": float(sep_23),
                    "rel_sep_13": float(sep_13),
                }
            label_rec[rname] = r_rec
        cusp_out[label] = label_rec
        print(f"[Section 2 {label} PASS] S_1-minV={cusp_out[label]['S']['phased_sum']['one_minus_min_V']} "
              f"S_sep23={cusp_out[label]['S']['phased_sum']['rel_sep_23']:.4f} "
              f"tS_sep13={cusp_out[label]['tilde_S']['phased_sum']['rel_sep_13']:.4f}", flush=True)

    # -------------------------------------------------------------------------
    # SECTION 3: P-874(2) / W-L1 SYMMETRIC POINTS tau = i AND tau = rho (dps = 50)
    # -------------------------------------------------------------------------
    mp.mp.dps = int(50)
    j = mp_j()
    terms_50 = build_intertwiner_basis()
    coeffs_50 = fixed_gaussian_coeffs()
    dm_50 = weil_dm_table()
    sec3_out = {}
    for sname, tp in [("i", j), ("rho", -mp_rat(1, 2) + j * mp.sqrt(int(3)) / int(2))]:
        b_sym = build_yukawa_and_operator(tp, terms_50, coeffs_50, dm_50, mc=int(1))
        ob_sym = extract_observables(b_sym)
        sv_y0, _, _ = hestenes_svd(b_sym["base_w0"])
        sv_sph, _, _ = hestenes_svd(b_sym["phased_sum"])
        hol_ratios = {
            "Y_base": sv_y0[2] / sv_y0[0],
            "S_ph": sv_sph[2] / sv_sph[0],
        }
        for tag in ("base_w0", "phased_sum"):
            hol_ratios[f"Yu_{tag}"] = ob_sym[tag]["su"][2] / ob_sym[tag]["su"][0]
            hol_ratios[f"Yd_{tag}"] = ob_sym[tag]["sd"][2] / ob_sym[tag]["sd"][0]
            hol_ratios[f"Ye_{tag}"] = ob_sym[tag]["se"][2] / ob_sym[tag]["se"][0]
        for kname, rval in hol_ratios.items():
            assert rval < pow10_mp(-30), f"Section 3 {sname} {kname} sigma3/sigma1={rval}"
        sep_y0 = abs(ob_sym["base_w0"]["rd"][0] - ob_sym["base_w0"]["re"][0])
        sep_sph = abs(ob_sym["phased_sum"]["rd"][0] - ob_sym["phased_sum"]["re"][0])
        assert sep_y0 > mp_rat(3, 5) and sep_sph > mp_rat(3, 5), f"Section 3 {sname} sep=({sep_y0},{sep_sph})"
        sec3_out[sname] = {
            "max_sigma3_over_sigma1": fmt_mp(max(hol_ratios.values()), 8),
            "per_matrix_sigma3_over_sigma1": {k: fmt_mp(v, 8) for k, v in hol_ratios.items()},
            "abs_rd23_minus_re23_base_w0": float(sep_y0),
            "abs_rd23_minus_re23_phased_sum": float(sep_sph),
        }
        print(f"[Section 3 tau={sname} PASS] max(s3/s1)={sec3_out[sname]['max_sigma3_over_sigma1']} "
              f"|rd23-re23|=({float(sep_y0):.4f}, {float(sep_sph):.4f})", flush=True)

    # -------------------------------------------------------------------------
    # SECTION 4: FIVE PLANTED FAULT CONTROLS (PFU2-1 .. PFU2-5) AT dps = 50
    # -------------------------------------------------------------------------
    tau_0 = mp_rat(13, 100) + j * mp_rat(17, 10)
    b_t0 = build_yukawa_and_operator(tau_0, terms_50, coeffs_50, dm_50, mc=int(1))
    b_t0_T = build_yukawa_and_operator(tau_0 + int(1), terms_50, coeffs_50, dm_50, mc=int(1))
    b_t0_S = build_yukawa_and_operator(-mp.mpf(int(1)) / tau_0, terms_50, coeffs_50, dm_50, mc=int(1))

    # PFU2-1: Omitting zeta_5^{-ab} relative 15-SV T-drift on O_1^{nophase} > 1/5
    b_np0 = build_yukawa_and_operator(tau_0, terms_50, coeffs_50, dm_50, mc=int(1), phased=False)
    b_npT = build_yukawa_and_operator(tau_0 + int(1), terms_50, coeffs_50, dm_50, mc=int(1), phased=False)
    ev_np0, _ = cyclic_jacobi_eigh(b_np0["O_full"] * b_np0["O_full"].H)
    ev_npT, _ = cyclic_jacobi_eigh(b_npT["O_full"] * b_npT["O_full"].H)
    sv_np0 = [mp.sqrt(max(e, mp.mpf(int(0)))) for e in ev_np0]
    sv_npT = [mp.sqrt(max(e, mp.mpf(int(0)))) for e in ev_npT]
    pfu1_drift = max(abs(sv_npT[k] - sv_np0[k]) / sv_np0[k] for k in range(15))
    assert pfu1_drift > mp_rat(1, 5), f"PFU2-1 failed: {pfu1_drift}"

    # PFU2-2: Frame C (1, -4) up coupling T^5 drift > 1/20
    b_14_0 = build_yukawa_and_operator(tau_0, terms_50, coeffs_50, dm_50, mc=int(1), mul_r=int(-4), phased=True)
    b_14_5 = build_yukawa_and_operator(tau_0 + int(5), terms_50, coeffs_50, dm_50, mc=int(1), mul_r=int(-4), phased=True)
    ob_14_0 = extract_observables(b_14_0)["phased_sum"]
    ob_14_5 = extract_observables(b_14_5)["phased_sum"]
    pfu2_ru_drift = max(abs(ob_14_5["ru"][k] - ob_14_0["ru"][k]) for k in range(2))
    sv_14_0, _, _ = hestenes_svd(b_14_0["phased_sum"])
    sv_14_5, _, _ = hestenes_svd(b_14_5["phased_sum"])
    pfu2_sph_drift = max(abs(sv_14_5[k] - sv_14_0[k]) / sv_14_0[k] for k in range(3))
    assert pfu2_ru_drift > mp_rat(1, 20) and pfu2_sph_drift > mp_rat(1, 20), f"PFU2-2 failed: ru={pfu2_ru_drift}, sph={pfu2_sph_drift}"

    # PFU2-3: Linear trace (T_3, T_2) collapses |r_e - r_d| < (1/10)^25
    T3 = sum(b_t0["O3_blocks"][a][a] for a in range(3))
    T2 = sum(b_t0["O2_blocks"][a][a] for a in range(2))
    G3L_lin = T3 * T3.H
    G2L_lin = T2 * T2.H
    G3R_lin = T3.H * T3
    G2R_lin = T2.H * T2
    KQL_lin, _ = inv_sqrt_jacobi(G3L_lin + G2L_lin)
    KLL_lin, _ = inv_sqrt_jacobi(int(3) * G3L_lin + G2L_lin)
    KdR_lin, _ = inv_sqrt_jacobi(int(2) * G3R_lin + int(2) * G2R_lin)
    KeR_lin, _ = inv_sqrt_jacobi(int(2) * G2R_lin)
    sd_lin, _, _ = hestenes_svd(KQL_lin * b_t0["base_w0"] * KdR_lin)
    se_lin, _, _ = hestenes_svd(KLL_lin * b_t0["base_w0"] * KeR_lin)
    rd_lin = [sd_lin[1] / sd_lin[0], sd_lin[2] / sd_lin[0]]
    re_lin = [se_lin[1] / se_lin[0], se_lin[2] / se_lin[0]]
    pfu3_diff = max(abs(re_lin[k] - rd_lin[k]) for k in range(2))
    assert pfu3_diff < pow10_mp(-25), f"PFU2-3 failed: {pfu3_diff}"

    # PFU2-4: Direct off-diagonal sum_{c_a != c'_a} symmetrized Hermitian (without + G_{3,L}) breaks r_u T/S invariance > 1/5
    def ru_offdiag_colour(bun):
        M_L = sum(
            bun["O3_blocks"][a][b] * bun["O3_blocks"][ap][b].H
            for a in range(3)
            for ap in range(3)
            if a != ap
            for b in range(3)
        )
        G3L_off = (M_L + M_L.H) / int(2)
        KQL_bad, _ = inv_sqrt_jacobi(G3L_off + bun["G2L"])
        KuR_ok, _ = inv_sqrt_jacobi(int(2) * bun["G3R"])
        su_bad, _, _ = hestenes_svd(KQL_bad * bun["base_w0"] * KuR_ok)
        return [su_bad[1] / su_bad[0], su_bad[2] / su_bad[0]]

    ru_off_0 = ru_offdiag_colour(b_t0)
    ru_off_T = ru_offdiag_colour(b_t0_T)
    ru_off_S = ru_offdiag_colour(b_t0_S)
    pfu4_dT = max(abs(ru_off_T[k] - ru_off_0[k]) for k in range(2))
    pfu4_dS = max(abs(ru_off_S[k] - ru_off_0[k]) for k in range(2))
    pfu4_max = max(pfu4_dT, pfu4_dS)
    assert pfu4_max > mp_rat(1, 5), f"PFU2-4 failed: max={pfu4_max}"

    # PFU2-5: Single-matrix left-right overlap |U_u^H V_u| shifts by > 1/10 under random Haar U_{R,u}
    ob_t0_ref = extract_observables(b_t0)["base_w0"]
    KQL_t0, _ = inv_sqrt_jacobi(b_t0["G3L"] + b_t0["G2L"])
    haar_50 = make_haar_generator(int(998877))
    pfu5_shift = mp.mpf(int(0))
    for _ in range(5):
        UuR_rand = haar_50(3)
        KuR_rand, _ = inv_sqrt_jacobi(UuR_rand * (int(2) * b_t0["G3R"]) * UuR_rand.H)
        Yu_rot = KQL_t0 * (b_t0["base_w0"] * UuR_rand.H) * KuR_rand
        _, Uur, Vur = hestenes_svd(Yu_rot)
        uv_abs_rot = mp.matrix([[abs((Uur.H * Vur)[a, b]) for b in range(3)] for a in range(3)])
        sh = max_abs_diff_mat(uv_abs_rot, ob_t0_ref["UuH_Vu_abs"])
        if sh > pfu5_shift:
            pfu5_shift = sh
    assert pfu5_shift > mp_rat(1, 10), f"PFU2-5 failed: {pfu5_shift}"

    pfu_out = {
        "PFU2_1_nophase_rel_T_drift": float(pfu1_drift),
        "PFU2_2_frameC_1_minus4_T5_ru_drift": float(pfu2_ru_drift),
        "PFU2_2_frameC_1_minus4_T5_Sph_drift": float(pfu2_sph_drift),
        "PFU2_3_linear_trace_T3_plus_T2_norm": fmt_mp(frob_norm(T3 + T2), 8),
        "PFU2_3_linear_trace_re_minus_rd": fmt_mp(pfu3_diff, 8),
        "PFU2_4_offdiag_colour_dT": float(pfu4_dT),
        "PFU2_4_offdiag_colour_dS": float(pfu4_dS),
        "PFU2_4_offdiag_colour_max_drift": float(pfu4_max),
        "PFU2_5_haar_URu_UuH_Vu_shift": float(pfu5_shift),
        "all_5_planted_faults_triggered": True,
    }
    print(f"[Section 4 PFU2-1..5 PASS] PFU1={float(pfu1_drift):.3f} PFU2=({float(pfu2_ru_drift):.3f},{float(pfu2_sph_drift):.3f}) "
          f"PFU3={fmt_mp(pfu3_diff,4)} PFU4={float(pfu4_max):.3f} PFU5={float(pfu5_shift):.3f}", flush=True)

    result = {
        "gate": "AGY-002_FOUND-V2-U2",
        "role": "cold_room_independent_referee",
        "policy": "0 of 19",
        "total_elapsed_s": int(round(time.time() - t_start)),
        "section_0": sec0_out,
        "section_1": sec1_out,
        "section_2": {
            "jacobi_vs_newton_schulz_tau0": ns_diffs,
            "bulk": sec2_bulk_out,
            "haar_10_trial_max_drift": fmt_mp(max_haar_drift, 8),
            "cusps": cusp_out,
        },
        "section_3": sec3_out,
        "section_4_planted_faults": pfu_out,
        "all_assertions_passed": True,
    }

    out_path = referee_dir / "referee_found_v2_u2_out.json"
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"ALL REFEREE CHECKS PASSED. Output sealed to {out_path.name}", flush=True)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--ast-only":
        report = audit_self_ast(pathlib.Path(__file__).resolve())
        print(json.dumps(report, indent=2))
        sys.exit(0)
    run_referee()
