r"""
Independent Cold-Room Zero-Trust Referee for Card A2-OW2 (and Errata 1, 2, 3).

Pre-registered open-flute 1-loop effective action across all finite rungs
N in {1, 2, 3, 4, 5} and non-finite control rungs N in {6, 7, 8, 9, 10, 11, 13},
spontaneous mirror/CP breaking, Shimura/H11 algebraic bridge, Gate F-U2 24-pt
Yukawa Jarlskog CP violation with independent GL6 Fuchsian L_2(tau) ODE solver,
50-digit mpmath Haar basis-scrambling gate, and 4 planted faults (PF-OW2-1..4).

Hygiene:
  - 0 of 19 empirical / PDG numbers.
  - 0 float or complex AST literals.
  - 0 frontier/ imports.
  - Built strictly from Card A2-OW2 + Errata 1-3 + Card A2-WG96 Erratum 2.
"""

import ast
import cmath
import hashlib
import json
import math
import os
import random
import time
from fractions import Fraction

import mpmath as mp


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
                if "frontier" in alias.name or "a2_ow2" in alias.name:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "frontier" in mod or "a2_ow2" in mod:
                bad_imports.append(mod)
    sha = hashlib.sha256(src.encode("utf-8")).hexdigest()
    manifest_path = os.path.join(os.path.dirname(script_path), "SCRIPT_SHA256.txt")
    manifest_match = None
    manifest_sha = None
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as mf:
            line = mf.read().strip().split()
            if line:
                manifest_sha = line[0]
                manifest_match = (manifest_sha == sha)
    return {
        "script_sha256": sha,
        "manifest_sha256": manifest_sha,
        "manifest_match": manifest_match,
        "float_or_complex_ast_literals": bad_literals,
        "float_or_complex_literal_count": len(bad_literals),
        "forbidden_imports": bad_imports,
        "forbidden_import_count": len(bad_imports),
        "hygiene_pass": (len(bad_literals) == 0 and len(bad_imports) == 0),
    }


# =============================================================================
# NUMBER-THEORETIC & SL(2, Z) HELPERS
# =============================================================================

def egcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def sl2_mul(g1, g2):
    a1, b1, c1, d1 = g1
    a2, b2, c2, d2 = g2
    return (a1 * a2 + b1 * c2, a1 * b2 + b1 * d2, c1 * a2 + d1 * c2, c1 * b2 + d1 * d2)


def sl2_inv(g):
    a, b, c, d = g
    return (d, -b, -c, a)


def sl2_act_mp(g, z):
    a, b, c, d = g
    return (a * z + b) / (c * z + d)


def sl2_act_c(g, z):
    a, b, c, d = g
    return (a * z + b) / (c * z + d)


def reduce_to_F1_mp(z):
    """Reduce z in H to standard fundamental domain F_1, returning (z_red, gamma) with gamma*z = z_red."""
    g = (1, 0, 0, 1)
    cur = z
    for _ in range(200):
        x = mp.re(cur)
        k = int(mp.floor(x + mp.mpf(1) / 2))
        if k != 0:
            cur = cur - k
            g = sl2_mul((1, -k, 0, 1), g)
        n2 = mp.re(cur) ** 2 + mp.im(cur) ** 2
        if n2 < 1 - mp.mpf(10) ** (-mp.mp.dps + 6):
            cur = -1 / cur
            g = sl2_mul((0, -1, 1, 0), g)
        else:
            break
    x = mp.re(cur)
    k = int(mp.floor(x + mp.mpf(1) / 2))
    if k != 0:
        cur = cur - k
        g = sl2_mul((1, -k, 0, 1), g)
    return cur, g


def reduce_to_F1_c(z):
    """Fast complex-float64 SL(2, Z) reduction to F_1 returning (z_red, gamma)."""
    g = (1, 0, 0, 1)
    cur = z
    half = 1 / 2
    tol = 1 - 1 / (10 ** 12)
    for _ in range(200):
        k = math.floor(cur.real + half)
        if k != 0:
            cur = complex(cur.real - k, cur.imag)
            g = sl2_mul((1, -k, 0, 1), g)
        n2 = cur.real * cur.real + cur.imag * cur.imag
        if n2 < tol:
            cur = -1 / cur
            g = sl2_mul((0, -1, 1, 0), g)
        else:
            break
    k = math.floor(cur.real + half)
    if k != 0:
        cur = complex(cur.real - k, cur.imag)
        g = sl2_mul((1, -k, 0, 1), g)
    return cur, g


def build_gamma0_cosets(N):
    r"""
    Construct exact right coset representatives Gamma_0(N) \ SL(2, Z)
    via P^1(Z / N Z), with exact HNF affine reduction parameters (alpha_k, beta_k)
    satisfying f(N * gamma_k(z)) = f(alpha_k * z + beta_k).
    """
    if N == 1:
        cosets = [(1, 0, 0, 1)]
    else:
        units = [u for u in range(1, N) if math.gcd(u, N) == 1]
        seen = set()
        cosets = []
        for c0 in range(N):
            for d0 in range(N):
                if math.gcd(math.gcd(c0, d0), N) != 1:
                    continue
                canon = min(((u * c0) % N, (u * d0) % N) for u in units)
                if canon in seen:
                    continue
                seen.add(canon)
                C, D = canon
                # Lift (C, D) mod N to coprime integers (C, D_lift)
                if C == 0:
                    C_lift, D_lift = 0, 1
                else:
                    D_lift = D
                    while math.gcd(C, D_lift) != 1:
                        D_lift += N
                    C_lift = C
                # Solve A * D_lift - B * C_lift = 1
                g, u_bez, v_bez = egcd(D_lift, C_lift)
                assert g == 1
                A_lift = u_bez
                B_lift = -v_bez
                assert A_lift * D_lift - B_lift * C_lift == 1
                cosets.append((A_lift, B_lift, C_lift, D_lift))

    # Verify pairwise distinctness and right-action closure under T and S
    def coset_id(mat):
        _, _, c, d = mat
        if N == 1:
            return (0, 0)
        units_local = [u for u in range(1, N) if math.gcd(u, N) == 1]
        return min(((u * (c % N)) % N, (u * (d % N)) % N) for u in units_local)

    ids = [coset_id(g) for g in cosets]
    assert len(set(ids)) == len(cosets)
    id_to_idx = {cid: idx for idx, cid in enumerate(ids)}
    T_mat = (1, 1, 0, 1)
    S_mat = (0, -1, 1, 0)
    closure_ok = True
    for g in cosets:
        if coset_id(sl2_mul(g, T_mat)) not in id_to_idx:
            closure_ok = False
        if coset_id(sl2_mul(g, S_mat)) not in id_to_idx:
            closure_ok = False
    assert closure_ok

    # Compute exact HNF affine reduction for N * gamma_k(z):
    # M_k = [[N*a, N*b], [c, d]], p = gcd(N, c), q = N // p
    # U_k = [[u, v], [-c//p, N*a//p]] with u*(N*a//p) + v*(c//p) = 1
    # U_k * M_k = [[p, r_k], [0, q]] -> alpha_k = p / q = p^2 / N, beta_k = r_k / q = p * r_k / N
    affine_info = []
    for (a, b, c, d) in cosets:
        p = math.gcd(N, c)
        q = N // p
        g_bez, u_bez, v_bez = egcd((N * a) // p, c // p)
        assert g_bez == 1
        r_raw = u_bez * N * b + v_bez * d
        r_k = r_raw % q
        # Verify U_k * M_k == [[p, r_k], [0, q]] after left shift
        shift = (r_raw - r_k) // q
        u_adj = u_bez - shift * (-c // p)
        v_adj = v_bez - shift * ((N * a) // p)
        assert u_adj * ((N * a) // p) + v_adj * (c // p) == 1
        assert u_adj * (N * a) + v_adj * c == p
        assert u_adj * (N * b) + v_adj * d == r_k
        assert (-c // p) * (N * a) + ((N * a) // p) * c == 0
        assert (-c // p) * (N * b) + ((N * a) // p) * d == q
        affine_info.append({
            "gamma": (a, b, c, d),
            "p": p,
            "q": q,
            "r": r_k,
            "alpha_num": p * p,
            "alpha_den": N,
            "beta_num": p * r_k,
            "beta_den": N,
        })
    return cosets, affine_info, id_to_idx


def psi_index(N):
    """Dedekind psi(N) = [SL(2,Z) : Gamma_0(N)] = N * prod_{p|N}(1 + 1/p)."""
    m = N
    res = N
    d = 2
    while d * d <= m:
        if m % d == 0:
            while m % d == 0:
                m //= d
            res = (res // d) * (d + 1)
        d += 1
    if m > 1:
        res = (res // m) * (m + 1)
    return res


def shimura_elliptic_counts(N):
    """
    Compute (nu_2(N), nu_3(N), H11_minus1_is_square) BOTH by direct modular congruence
    counting and by Shimura's exact prime-factor product formulas, asserting exact match.
    """
    nu2_direct = sum(1 for x in range(N) if (x * x + 1) % N == 0)
    nu3_direct = sum(1 for x in range(N) if (x * x + x + 1) % N == 0)
    h11_direct = (nu2_direct > 0)

    # Prime factors of N
    m = N
    primes = []
    d = 2
    while d * d <= m:
        if m % d == 0:
            primes.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        primes.append(m)

    if N % 4 == 0:
        nu2_shim = 0
    else:
        nu2_shim = 1
        for p in primes:
            if p == 2:
                leg = 0
            elif p % 4 == 1:
                leg = 1
            else:
                leg = -1
            nu2_shim *= (1 + leg)

    if N % 9 == 0:
        nu3_shim = 0
    else:
        nu3_shim = 1
        for p in primes:
            if p == 3:
                leg = 0
            elif p % 3 == 1:
                leg = 1
            else:
                leg = -1
            nu3_shim *= (1 + leg)

    assert nu2_direct == nu2_shim
    assert nu3_direct == nu3_shim
    return {
        "N": N,
        "mu_N": psi_index(N),
        "H11_minus1_is_square_mod_N": h11_direct,
        "nu_2": nu2_direct,
        "nu_3": nu3_direct,
        "shimura_formula_exact_match": (nu2_direct == nu2_shim and nu3_direct == nu3_shim),
    }


# =============================================================================
# MODULAR FUNCTIONS (MPMATH HIGH PRECISION & FAST FLOAT64)
# =============================================================================

def eta_mp(tau):
    """Dedekind eta(tau) in current mp.mp.dps using Euler pentagonal theorem on reduced F_1 or direct."""
    q = mp.exp(2 * mp.pi * mp.mpc(0, 1) * tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 6)
    # Pentagonal expansion: prod_{m>=1}(1 - q^m) = 1 + sum_{k>=1} (-1)^k (q^{k(3k-1)/2} + q^{k(3k+1)/2})
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
    return mp.exp(mp.pi * mp.mpc(0, 1) * tau / 12) * s


def e2_e4_e6_mp(tau):
    """Evaluate E_2(tau), E_4(tau), E_6(tau) to current mp.mp.dps."""
    q = mp.exp(2 * mp.pi * mp.mpc(0, 1) * tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 6)
    s2 = mp.mpc(0)
    s4 = mp.mpc(0)
    s6 = mp.mpc(0)
    qm = q
    m = 1
    while True:
        inv = qm / (1 - qm)
        m2 = m * m
        s2 += m * inv
        s4 += (m2 * m) * inv
        s6 += (m2 * m2 * m) * inv
        if abs(qm) * (m2 * m2 * m) < tol:
            break
        qm *= q
        m += 1
    return 1 - 24 * s2, 1 + 240 * s4, 1 - 504 * s6


def f_val_grad_hess_mp(w):
    """
    Evaluate f(w) = -ln(Im(w) |eta(w)|^4) and its exact Wirtinger/real gradient and 2x2 Hessian
    in current mp.mp.dps by reducing w to F_1 first for rapid convergence everywhere in H.
    """
    wt, g = reduce_to_F1_mp(w)
    _, _, c, d = g
    cw_d = c * w + d
    y = mp.im(w)
    yt = mp.im(wt)
    et = eta_mp(wt)
    f_val = -mp.log(yt * (abs(et) ** 4))

    e2t, e4t, _ = e2_e4_e6_mp(wt)
    pi = mp.pi
    # On wt:
    # df/dwt = i/(2*yt) - (i*pi/6)*E2(wt)
    # d^2f/dwt^2 = -1/(4*yt^2) + (pi^2/36)*(E2(wt)^2 - E4(wt))
    df_wt = mp.mpc(0, 1) / (2 * yt) - (mp.mpc(0, 1) * pi / 6) * e2t
    d2f_wt = -mp.mpf(1) / (4 * yt * yt) + (pi * pi / 36) * (e2t * e2t - e4t)

    # Pull back by wt = (a*w + b)/(c*w + d), dwt/dw = (c*w + d)^(-2), d^2wt/dw^2 = -2*c*(c*w + d)^(-3)
    inv_cwd = 1 / cw_d
    inv_cwd2 = inv_cwd * inv_cwd
    df_w = inv_cwd2 * df_wt
    d2f_w = (inv_cwd2 * inv_cwd2) * d2f_wt - 2 * c * (inv_cwd2 * inv_cwd) * df_wt

    fx = 2 * mp.re(df_w)
    fy = -2 * mp.im(df_w)
    A = mp.mpf(1) / (2 * y * y)
    B = 2 * d2f_w
    fxx = A + mp.re(B)
    fyy = A - mp.re(B)
    fxy = -mp.im(B)
    return f_val, df_w, (fx, fy), (fxx, fxy, fyy)


def V_N_full_mp(tau, N):
    """Exact V_N(tau) = (pi/2)*(f(tau) + f(N*tau)), Wirtinger dV/dtau, real grad, and 2x2 Hessian."""
    f1, df1, g1, h1 = f_val_grad_hess_mp(tau)
    f2, df2, g2, h2 = f_val_grad_hess_mp(N * tau)
    hp = mp.pi / 2
    val = hp * (f1 + f2)
    dw = hp * (df1 + N * df2)
    vx = hp * (g1[0] + N * g2[0])
    vy = hp * (g1[1] + N * g2[1])
    N2 = N * N
    vxx = hp * (h1[0] + N2 * h2[0])
    vxy = hp * (h1[1] + N2 * h2[1])
    vyy = hp * (h1[2] + N2 * h2[2])
    tr = vxx + vyy
    diff = vxx - vyy
    rad = mp.sqrt(diff * diff / 4 + vxy * vxy)
    lmin = tr / 2 - rad
    lmax = tr / 2 + rad
    det = vxx * vyy - vxy * vxy
    return {
        "val": val,
        "dw": dw,
        "grad": (vx, vy),
        "grad_norm": mp.sqrt(vx * vx + vy * vy),
        "hess": (vxx, vxy, vyy),
        "lambda_min": lmin,
        "lambda_max": lmax,
        "det_H": det,
        "lap_hyp": (mp.im(tau) ** 2) * (vxx + vyy),
    }


def g_coset_full_mp(z, aff):
    """Exact g_k(z) = V_N(gamma_k z) = (pi/2)*(f(z) + f(alpha_k*z + beta_k)) in mpmath."""
    alpha = mp.mpf(aff["alpha_num"]) / mp.mpf(aff["alpha_den"])
    beta = mp.mpf(aff["beta_num"]) / mp.mpf(aff["beta_den"])
    w = alpha * z + beta
    f1, _, g1, h1 = f_val_grad_hess_mp(z)
    f2, _, g2, h2 = f_val_grad_hess_mp(w)
    hp = mp.pi / 2
    a2 = alpha * alpha
    val = hp * (f1 + f2)
    gx = hp * (g1[0] + alpha * g2[0])
    gy = hp * (g1[1] + alpha * g2[1])
    hxx = hp * (h1[0] + a2 * h2[0])
    hxy = hp * (h1[1] + a2 * h2[1])
    hyy = hp * (h1[2] + a2 * h2[2])
    tr = hxx + hyy
    diff = hxx - hyy
    rad = mp.sqrt(diff * diff / 4 + hxy * hxy)
    return {
        "val": val,
        "grad": (gx, gy),
        "grad_norm": mp.sqrt(gx * gx + gy * gy),
        "hess": (hxx, hxy, hyy),
        "lambda_min": tr / 2 - rad,
        "lambda_max": tr / 2 + rad,
    }


def f_val_grad_hess_c(w):
    """Fast float64 f(w), real gradient, and 2x2 Hessian via SL(2, Z) reduction to F_1."""
    wt, g = reduce_to_F1_c(w)
    _, _, c, d = g
    cw_d = c * w + d
    y = w.imag
    yt = wt.imag
    pi = math.pi
    q = cmath.exp(complex(0, 2 * pi) * wt)
    # Pentagonal eta on F_1 (|q| <= exp(-pi*sqrt(3)) ~ 0.0043 -> 4 terms give machine precision)
    s_eta = complex(1, 0)
    for k in range(1, 7):
        e1 = (k * (3 * k - 1)) // 2
        e2 = (k * (3 * k + 1)) // 2
        term = (q ** e1) + (q ** e2)
        if k % 2 == 1:
            s_eta -= term
        else:
            s_eta += term
    # |eta(wt)|^4 = exp(-pi*yt/3) * |s_eta|^4
    abs_s = abs(s_eta)
    f_val = (pi * yt) / 3 - math.log(yt) - 4 * math.log(abs_s)

    # E2 and E4 on F_1 (12 terms > float64 machine precision)
    s2 = complex(0, 0)
    s4 = complex(0, 0)
    qm = q
    for m in range(1, 14):
        inv = qm / (1 - qm)
        s2 += m * inv
        s4 += (m * m * m) * inv
        qm *= q
    e2t = 1 - 24 * s2
    e4t = 1 + 240 * s4

    df_wt = complex(0, 1 / (2 * yt)) - complex(0, pi / 6) * e2t
    d2f_wt = -1 / (4 * yt * yt) + (pi * pi / 36) * (e2t * e2t - e4t)

    inv_cwd = 1 / cw_d
    inv_cwd2 = inv_cwd * inv_cwd
    df_w = inv_cwd2 * df_wt
    d2f_w = (inv_cwd2 * inv_cwd2) * d2f_wt - 2 * c * (inv_cwd2 * inv_cwd) * df_wt

    fx = 2 * df_w.real
    fy = -2 * df_w.imag
    A = 1 / (2 * y * y)
    B = 2 * d2f_w
    fxx = A + B.real
    fyy = A - B.real
    fxy = -B.imag
    return f_val, fx, fy, fxx, fxy, fyy


def g_coset_c(z, alpha, beta):
    """Fast float64 g_k(z) = (pi/2)*(f(z) + f(alpha*z + beta)), grad, Hessian."""
    w = complex(alpha * z.real + beta, alpha * z.imag)
    f1, gx1, gy1, hxx1, hxy1, hyy1 = f_val_grad_hess_c(z)
    f2, gx2, gy2, hxx2, hxy2, hyy2 = f_val_grad_hess_c(w)
    hp = math.pi / 2
    a2 = alpha * alpha
    val = hp * (f1 + f2)
    gx = hp * (gx1 + alpha * gx2)
    gy = hp * (gy1 + alpha * gy2)
    hxx = hp * (hxx1 + a2 * hxx2)
    hxy = hp * (hxy1 + a2 * hxy2)
    hyy = hp * (hyy1 + a2 * hyy2)
    tr = hxx + hyy
    diff = hxx - hyy
    rad = math.hypot(diff / 2, hxy)
    return val, gx, gy, hxx, hxy, hyy, tr / 2 - rad, tr / 2 + rad


# =============================================================================
# RIGOROUS CLOSED-FORM ANALYTIC BOUNDS ON ||H_f||_2 AND ||D^3 f||_op
# =============================================================================

def f_M2_M3_disk_bound_mp(wc, rw):
    """
    100% rigorous closed-form analytic upper bounds (M2, M3) on
    sup_{w in B(wc, rw)} ||H_f(w)||_2 and sup_{w in B(wc, rw)} ||D^3 f(w)||_op
    in high-precision mpmath. Returns None if disk is too wide for a single SL(2,Z) chart.
    """
    vmin = mp.im(wc) - rw
    if vmin <= 0:
        return None
    _, g = reduce_to_F1_mp(wc)
    _, _, c, d = g
    D0 = abs(c * wc + d)
    ac = abs(c)
    Dmin = D0 - ac * rw
    Dmax = D0 + ac * rw
    if Dmin <= 0:
        return None
    yt_min = vmin / (Dmax * Dmax)
    if yt_min <= mp.mpf(1) / 4:
        return None
    pi = mp.pi
    r = mp.exp(-2 * pi * yt_min)
    omr = 1 - r
    B_e2 = 1 + 24 * r / (omr ** 3)
    B_e2p = 48 * pi * r * (1 + r) / (omr ** 5)
    B_e2pp = 96 * pi * pi * r * (1 + r) * (1 + 4 * r + r * r) / (omr ** 7)
    B1 = mp.mpf(1) / (2 * yt_min) + (pi / 6) * B_e2
    B2 = mp.mpf(1) / (4 * yt_min * yt_min) + (pi / 6) * B_e2p
    B3 = mp.mpf(1) / (4 * (yt_min ** 3)) + (pi / 6) * B_e2pp
    invD = 1 / Dmin
    invD2 = invD * invD
    invD3 = invD2 * invD
    invD4 = invD2 * invD2
    C2 = B2 * invD4 + 2 * ac * B1 * invD3
    C3 = B3 * (invD4 * invD2) + 6 * ac * B2 * (invD4 * invD) + 6 * (ac * ac) * B1 * invD4
    M2 = mp.mpf(1) / (2 * vmin * vmin) + 2 * C2
    M3 = mp.mpf(5) / (2 * (vmin ** 3)) + 2 * C3
    return M2, M3


def g_M2_M3_disk_bound_mp(zc, rz, aff):
    alpha = mp.mpf(aff["alpha_num"]) / mp.mpf(aff["alpha_den"])
    beta = mp.mpf(aff["beta_num"]) / mp.mpf(aff["beta_den"])
    b1 = f_M2_M3_disk_bound_mp(zc, rz)
    if b1 is None:
        return None
    b2 = f_M2_M3_disk_bound_mp(alpha * zc + beta, alpha * rz)
    if b2 is None:
        return None
    hp = mp.pi / 2
    a2 = alpha * alpha
    a3 = a2 * alpha
    return hp * (b1[0] + a2 * b2[0]), hp * (b1[1] + a3 * b2[1])


def f_M2_M3_disk_bound_c(wc, rw):
    """Fast float64 closed-form analytic upper bounds (M2, M3) with conservative 1001/1000 factor."""
    vmin = wc.imag - rw
    if vmin <= 0:
        return None
    _, g = reduce_to_F1_c(wc)
    _, _, c, d = g
    D0 = abs(c * wc + d)
    ac = abs(c)
    Dmin = D0 - ac * rw
    Dmax = D0 + ac * rw
    if Dmin <= 0:
        return None
    yt_min = vmin / (Dmax * Dmax)
    if yt_min <= 1 / 4:
        return None
    pi = math.pi
    r = math.exp(-2 * pi * yt_min)
    omr = 1 - r
    B_e2 = 1 + 24 * r / (omr ** 3)
    B_e2p = 48 * pi * r * (1 + r) / (omr ** 5)
    B_e2pp = 96 * pi * pi * r * (1 + r) * (1 + 4 * r + r * r) / (omr ** 7)
    B1 = 1 / (2 * yt_min) + (pi / 6) * B_e2
    B2 = 1 / (4 * yt_min * yt_min) + (pi / 6) * B_e2p
    B3 = 1 / (4 * (yt_min ** 3)) + (pi / 6) * B_e2pp
    invD = 1 / Dmin
    invD2 = invD * invD
    invD3 = invD2 * invD
    invD4 = invD2 * invD2
    C2 = B2 * invD4 + 2 * ac * B1 * invD3
    C3 = B3 * (invD4 * invD2) + 6 * ac * B2 * (invD4 * invD) + 6 * (ac * ac) * B1 * invD4
    sf = 1001 / 1000
    M2 = sf * (1 / (2 * vmin * vmin) + 2 * C2)
    M3 = sf * (5 / (2 * (vmin ** 3)) + 2 * C3)
    return M2, M3


def g_M2_M3_disk_bound_c(zc, rz, alpha, beta):
    b1 = f_M2_M3_disk_bound_c(zc, rz)
    if b1 is None:
        return None
    b2 = f_M2_M3_disk_bound_c(complex(alpha * zc.real + beta, alpha * zc.imag), alpha * rz)
    if b2 is None:
        return None
    hp = math.pi / 2
    a2 = alpha * alpha
    a3 = a2 * alpha
    return hp * (b1[0] + a2 * b2[0]), hp * (b1[1] + a3 * b2[1])


# =============================================================================
# EXACT DECIDABLE FINITE-INTEGER GAMMA_0(N) EQUIVALENCE SOLVER
# =============================================================================

def gamma0_equiv_decidable(tau1, tau2, N, tol_eq=None):
    """
    Exact exhaustive finite-integer decision procedure for:
      exists gamma = [[a, b], [c, d]] in Gamma_0(N) with gamma(tau1) == tau2.
    Because Im(gamma(tau1)) = y1 / |c*tau1 + d|^2 = y2 forces
      (c*x1 + d)^2 + (c*y1)^2 = y1 / y2,
    we have the strict finite bound 0 <= c <= floor(1 / sqrt(y1*y2)) + 1 with N | c.
    Returns (is_equiv, best_gamma_or_None, best_residual, c_bound, candidates_checked, all_equivs).
    """
    if tol_eq is None:
        tol_eq = mp.mpf(10) ** (-35)
    x1, y1 = mp.re(tau1), mp.im(tau1)
    x2, y2 = mp.re(tau2), mp.im(tau2)
    ratio = y1 / y2
    # Add safety margin + 2 for finite-bound exhaustiveness
    c_max = int(mp.floor(1 / mp.sqrt(y1 * y2))) + 2
    best_dist = mp.mpf(10) ** 9
    best_gamma = None
    all_equivs = []
    checked = 0
    for c in range(0, c_max + 1, N):
        rem = ratio - (c * y1) ** 2
        if rem < -mp.mpf(1) / 4:
            continue
        rad = mp.sqrt(max(mp.mpf(0), rem + mp.mpf(1) / 4))
        d_lo = int(mp.floor(-c * x1 - rad)) - 1
        d_hi = int(mp.ceil(-c * x1 + rad)) + 1
        for d in range(d_lo, d_hi + 1):
            if c == 0:
                if d != 1:
                    continue
            else:
                if math.gcd(c, d) != 1:
                    continue
            checked += 1
            # Bezout a0*d - b0*c = 1
            g_bez, u_bez, v_bez = egcd(d, c)
            if g_bez != 1:
                continue
            a0, b0 = u_bez, -v_bez
            w0 = (a0 * tau1 + b0) / (c * tau1 + d)
            k = int(mp.nint(mp.re(tau2 - w0)))
            a = a0 + k * c
            b = b0 + k * d
            assert a * d - b * c == 1 and c % N == 0
            w = (a * tau1 + b) / (c * tau1 + d)
            dist = abs(w - tau2)
            if dist < best_dist:
                best_dist = dist
                best_gamma = (a, b, c, d)
            if dist < tol_eq:
                all_equivs.append(((a, b, c, d), dist))
    is_equiv = (len(all_equivs) > 0)
    return {
        "is_equiv": is_equiv,
        "best_gamma": list(best_gamma) if best_gamma is not None else None,
        "min_dist": best_dist,
        "c_bound": c_max,
        "candidates_checked": checked,
        "all_equivs": [(list(g), d) for (g, d) in all_equivs],
    }


def elliptic_order_gamma0(tau, N):
    """Exact stabilizer order in PSL(2, Z) cap (Gamma_0(N) / {+-I}) using decidable solver."""
    res = gamma0_equiv_decidable(tau, tau, N)
    max_ord = 1
    nontrivial = []
    for g, _ in res["all_equivs"]:
        a, b, c, d = g
        if (a, b, c, d) in [(1, 0, 0, 1), (-1, 0, 0, -1)]:
            continue
        tr = abs(a + d)
        if tr == 0:
            ord_g = 2
        elif tr == 1:
            ord_g = 3
        else:
            ord_g = 1
        if ord_g > max_ord:
            max_ord = ord_g
        nontrivial.append({"gamma": g, "abs_trace": tr, "order": ord_g})
    return max_ord, nontrivial


# =============================================================================
# TASK OW2-A: BEREZIN SIGN THEOREM & KRONECKER FIRST LIMIT FORMULA
# =============================================================================

def run_task_ow2_a():
    mp.mp.dps = 70
    # 1. Explicit dense positive-definite 5x5 complex Hermitian matrix A = B^H B + I_5
    # Exact Gaussian-integer entries (stored as (re, im) int pairs for exact Grassmann arithmetic)
    B_gi = [
        [(1, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
        [(0, 1), (2, 0), (0, 0), (-1, 0), (0, 0)],
        [(0, 0), (0, -1), (1, 0), (1, 0), (0, 1)],
        [(1, 0), (0, 0), (0, 1), (2, 0), (-1, 0)],
        [(0, 0), (1, 0), (0, 0), (0, -1), (1, 0)],
    ]

    def gi_mul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def gi_add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def gi_conj(x):
        return (x[0], -x[1])

    n = 5
    A_gi = [[(0, 0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = (1, 0) if i == j else (0, 0)
            for k in range(n):
                acc = gi_add(acc, gi_mul(gi_conj(B_gi[k][i]), B_gi[k][j]))
            A_gi[i][j] = acc

    # Check exact Hermiticity A == A^H
    herm_err = 0
    for i in range(n):
        for j in range(n):
            cj = gi_conj(A_gi[j][i])
            if A_gi[i][j] != cj:
                herm_err += 1

    # Exact Leibniz determinant over all 5! = 120 permutations
    def perm_sign(p):
        inv = 0
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if p[i] > p[j]:
                    inv += 1
        return -1 if (inv % 2 == 1) else 1

    def all_perms(arr):
        if len(arr) <= 1:
            yield tuple(arr)
            return
        for i in range(len(arr)):
            rest = arr[:i] + arr[i + 1:]
            for p in all_perms(rest):
                yield (arr[i],) + p

    det_leibniz = (0, 0)
    for p in all_perms(list(range(n))):
        sgn = perm_sign(p)
        prod = (sgn, 0)
        for i in range(n):
            prod = gi_mul(prod, A_gi[i][p[i]])
        det_leibniz = gi_add(det_leibniz, prod)
    assert det_leibniz[1] == 0 and det_leibniz[0] > 0
    exact_det_int = det_leibniz[0]

    # Bosonic Gaussian integral via 10x10 real symmetric positive-definite matrix M
    M_real = mp.matrix(2 * n, 2 * n)
    A_mp = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            ar, ai = A_gi[i][j]
            A_mp[i, j] = mp.mpc(ar, ai)
            M_real[i, j] = mp.mpf(ar)
            M_real[i, n + j] = mp.mpf(-ai)
            M_real[n + i, j] = mp.mpf(ai)
            M_real[n + i, n + j] = mp.mpf(ar)

    evals_A, _ = mp.eighe(A_mp)
    lambda_min_A = min(mp.re(ev) for ev in evals_A)
    L_chol = mp.cholesky(M_real)
    # Z_B = (1 / pi^n) * prod_{k=0}^{2n-1} (sqrt(pi) / L_{kk}) = 1 / prod L_{kk}
    prod_L = mp.mpf(1)
    for k in range(2 * n):
        prod_L *= L_chol[k, k]
    Z_B = (mp.sqrt(mp.pi) ** (2 * n)) / (prod_L * (mp.pi ** n))
    V_B = -mp.log(Z_B)
    det_mp = mp.mpf(exact_det_int)
    boson_Z_err = abs(Z_B - 1 / det_mp)
    boson_V_err = abs(V_B - mp.log(det_mp))

    # Fermionic Grassmann Berezin integral Method 1:
    # Full 2^10 = 1024-dim exterior algebra Lambda(psi_0, psibar_0, ..., psi_4, psibar_4)
    # Generator indices: psi_k -> bit 2*k, psibar_k -> bit 2*k + 1.
    # Element Q = -sum_{i,j} A_{ij} (psibar_i ^ psi_j).
    # Compute Q^{^5} / 5! explicitly and extract coefficient of top form bitmask (1<<10)-1.
    def wedge_pair_sign(mask1, mask2):
        # Number of swaps to move set bits of mask1 past smaller set bits of mask2
        swaps = 0
        m1 = mask1
        while m1:
            lsb = m1 & -m1
            swaps += bin(mask2 & (lsb - 1)).count("1")
            m1 ^= lsb
        return -1 if (swaps % 2 == 1) else 1

    def ext_mul(poly1, poly2):
        out = {}
        for m1, c1 in poly1.items():
            for m2, c2 in poly2.items():
                if (m1 & m2) != 0:
                    continue
                sgn = wedge_pair_sign(m1, m2)
                prod = gi_mul(c1, c2)
                if sgn == -1:
                    prod = (-prod[0], -prod[1])
                m = m1 | m2
                if m in out:
                    nv = gi_add(out[m], prod)
                    if nv == (0, 0):
                        del out[m]
                    else:
                        out[m] = nv
                else:
                    if prod != (0, 0):
                        out[m] = prod
        return out

    Q_poly = {}
    for i in range(n):
        for j in range(n):
            ar, ai = A_gi[i][j]
            if ar == 0 and ai == 0:
                continue
            # -A_{ij} * (psibar_i ^ psi_j)
            bit_pb = 1 << (2 * i + 1)
            bit_p = 1 << (2 * j)
            sgn = wedge_pair_sign(bit_pb, bit_p)
            coef = (-sgn * ar, -sgn * ai)
            mask = bit_pb | bit_p
            prev = Q_poly.get(mask, (0, 0))
            nv = gi_add(prev, coef)
            if nv == (0, 0):
                Q_poly.pop(mask, None)
            else:
                Q_poly[mask] = nv

    Q_pow = {0: (1, 0)}
    for _ in range(n):
        Q_pow = ext_mul(Q_pow, Q_poly)
    top_mask = (1 << (2 * n)) - 1
    top_coef = Q_pow.get(top_mask, (0, 0))
    fact_n = math.factorial(n)
    assert top_coef[0] % fact_n == 0 and top_coef[1] == 0
    Z_F_full1024 = top_coef[0] // fact_n

    # Fermionic Grassmann Berezin integral Method 2:
    # Explicit 2^5 = 32-dim exterior product wedge_{i=0}^4 (sum_j A_{ij} psi_j)
    w_poly = {0: (1, 0)}
    for i in range(n):
        row_poly = {}
        for j in range(n):
            if A_gi[i][j] != (0, 0):
                row_poly[1 << j] = A_gi[i][j]
        w_poly = ext_mul(w_poly, row_poly)
    top5 = w_poly.get((1 << n) - 1, (0, 0))
    assert top5[1] == 0
    Z_F_ext32 = top5[0]

    V_F = -mp.log(mp.mpf(Z_F_full1024))
    fermion_V_err = abs(V_F - (-mp.log(det_mp)))

    # 2. Kronecker First Limit Formula: -E'(tau, 0) == ln(4 * pi^2 * y * |eta(tau)|^4)
    # Verified at 4 diverse test points by TWO independent methods:
    #   Method 1: Pure 2D Mellin / Jacobi-theta lattice sum (SL(2,Z)-manifest, no Fourier/Bessel!)
    #   Method 2: Direct Chowla-Selberg Bessel-K series E(tau, s) Cauchy-differentiated at s = 0!
    test_taus = [
        ("i", mp.mpc(0, 1)),
        ("rho", mp.mpc(-1, 0) / 2 + mp.mpc(0, 1) * mp.sqrt(3) / 2),
        ("3/11+7/5i", mp.mpc(3, 0) / 11 + mp.mpc(0, 7) / 5),
        ("-2/7+9/10i", mp.mpc(-2, 0) / 7 + mp.mpc(0, 9) / 10),
    ]

    def eisenstein_chowla_selberg(tau, s):
        x = mp.re(tau)
        y = mp.im(tau)
        pi = mp.pi
        t1 = 2 * mp.zeta(2 * s) * (y ** s)
        t2 = 2 * mp.sqrt(pi) * (mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s)) * mp.zeta(2 * s - 1) * (y ** (1 - s))
        pref = 8 * (pi ** s) * mp.sqrt(y) / mp.gamma(s)
        acc = mp.mpc(0)
        nu = s - mp.mpf(1) / 2
        tol = mp.mpf(10) ** (-mp.mp.dps - 5)
        for nn in range(1, 150):
            # sigma_{1-2s}(nn)
            sig = mp.mpc(0)
            for d in range(1, nn + 1):
                if nn % d == 0:
                    sig += mp.mpf(d) ** (1 - 2 * s)
            term = sig * (mp.mpf(nn) ** nu) * mp.besselk(nu, 2 * pi * nn * y) * mp.cos(2 * pi * nn * x)
            acc += term
            if abs(pref * term) < tol:
                break
        return t1 + t2 + pref * acc

    kronecker_checks = []
    max_mellin_err = mp.mpf(0)
    max_cs_err = mp.mpf(0)
    for label, tau in test_taus:
        y = mp.im(tau)
        et = eta_mp(tau)
        rhs = mp.log(4 * (mp.pi ** 2) * y * (abs(et) ** 4))

        # Method 1: 2D Mellin lattice sum
        # Reduce tau to F_1 for fastest lattice sum (since a_{mn} = pi |m*tau+n|^2 / y is SL(2,Z)-invariant!)
        tau_r, _ = reduce_to_F1_mp(tau)
        yr = mp.im(tau_r)
        s_mellin = mp.mpf(0)
        B_lat = 18
        for m in range(-B_lat, B_lat + 1):
            for nn in range(-B_lat, B_lat + 1):
                if m == 0 and nn == 0:
                    continue
                a = mp.pi * (abs(m * tau_r + nn) ** 2) / yr
                if a < 180:
                    s_mellin += mp.exp(-a) / a + mp.gammainc(0, a)
        neg_Ep_mellin = 1 + mp.euler + mp.log(mp.pi) - s_mellin
        err_mellin = abs(neg_Ep_mellin - rhs)
        if err_mellin > max_mellin_err:
            max_mellin_err = err_mellin

        # Method 2: Direct Chowla-Selberg Cauchy contour integral on |s| = 1/100 (M = 24 points)
        r_c = mp.mpf(1) / 100
        M_c = 24
        cs_sum = mp.mpc(0)
        for k in range(M_c):
            sk = r_c * mp.exp(2 * mp.pi * mp.mpc(0, 1) * k / M_c)
            cs_sum += eisenstein_chowla_selberg(tau, sk) / sk
        Ep_cs = mp.re(cs_sum / M_c)
        neg_Ep_cs = -Ep_cs
        err_cs = abs(neg_Ep_cs - rhs)
        if err_cs > max_cs_err:
            max_cs_err = err_cs

        kronecker_checks.append({
            "label": label,
            "rhs_ln_4pi2_y_eta4": mp.nstr(rhs, 40),
            "mellin_err": mp.nstr(err_mellin, 6),
            "chowla_selberg_cauchy_err": mp.nstr(err_cs, 6),
        })

    # 3. Confining sign theorem check (n_F > n_B vs n_F < n_B)
    # V_eff(tau; n_F, n_B) = -((n_F - n_B)/2) * ln(y |eta(tau)|^4) = ((n_F - n_B)/2) * f(tau)
    ys_check = [2, 4, 8, 16]
    f_vals_y = [f_val_grad_hess_mp(mp.mpc(0, yv))[0] for yv in ys_check]
    fermion_dom_vals = [mp.mpf(96 - 24) / 2 * fv for fv in f_vals_y]
    boson_dom_vals = [mp.mpf(24 - 96) / 2 * fv for fv in f_vals_y]
    fermion_confining = all(fermion_dom_vals[i + 1] > fermion_dom_vals[i] for i in range(len(ys_check) - 1))
    boson_deconfining = all(boson_dom_vals[i + 1] < boson_dom_vals[i] for i in range(len(ys_check) - 1))
    lap_f = (mp.mpf(2) ** 2) * (f_val_grad_hess_mp(mp.mpc(1, 0) / 3 + mp.mpc(0, 2))[3][0]
                                + f_val_grad_hess_mp(mp.mpc(1, 0) / 3 + mp.mpc(0, 2))[3][2])

    tol_35 = mp.mpf(10) ** (-35)
    tol_50 = mp.mpf(10) ** (-50)
    passed = (
        herm_err == 0
        and lambda_min_A > 0
        and boson_Z_err < tol_50
        and boson_V_err < tol_50
        and Z_F_full1024 == exact_det_int
        and Z_F_ext32 == exact_det_int
        and fermion_V_err < tol_50
        and max_mellin_err < tol_35
        and max_cs_err < tol_35
        and fermion_confining
        and boson_deconfining
        and abs(lap_f - 1) < tol_50
    )
    return {
        "matrix_type": "dense_5x5_complex_hermitian_BHB_plus_I",
        "hermiticity_exact_err": herm_err,
        "lambda_min_A": mp.nstr(lambda_min_A, 15),
        "exact_det_A_leibniz": exact_det_int,
        "Z_B_err_vs_inv_det": mp.nstr(boson_Z_err, 6),
        "V_B_err_vs_plus_ln_det": mp.nstr(boson_V_err, 6),
        "Z_F_full_1024dim_exterior": Z_F_full1024,
        "Z_F_32dim_exterior": Z_F_ext32,
        "Z_F_exact_match_plus_det": (Z_F_full1024 == exact_det_int and Z_F_ext32 == exact_det_int),
        "V_F_err_vs_minus_ln_det": mp.nstr(fermion_V_err, 6),
        "kronecker_checks": kronecker_checks,
        "max_mellin_kronecker_err": mp.nstr(max_mellin_err, 6),
        "max_chowla_selberg_kronecker_err": mp.nstr(max_cs_err, 6),
        "fermion_dom_confining": fermion_confining,
        "boson_dom_deconfining": boson_deconfining,
        "hyperbolic_laplacian_f_at_test": mp.nstr(lap_f, 40),
        "pass": passed,
    }


# =============================================================================
# TASK OW2-B & OW2-C: GLOBAL MINIMIZATION, CERTIFIED BnB, CP & FRICKE ANALYSIS
# =============================================================================

def newton_polish_coset_mp(z_init, aff, max_iter=35):
    """65-digit mpmath Newton polish for stationary point of g_k(z)."""
    z = z_init
    for _ in range(max_iter):
        info = g_coset_full_mp(z, aff)
        gx, gy = info["grad"]
        if info["grad_norm"] < mp.mpf(10) ** (-58):
            return z, info
        hxx, hxy, hyy = info["hess"]
        det = hxx * hyy - hxy * hxy
        if abs(det) < mp.mpf(10) ** (-50):
            break
        dx = -(hyy * gx - hxy * gy) / det
        dy = -(-hxy * gx + hxx * gy) / det
        step = mp.hypot(dx, dy)
        if step > mp.mpf(1) / 5:
            scale = (mp.mpf(1) / 5) / step
            dx *= scale
            dy *= scale
        z = mp.mpc(mp.re(z) + dx, mp.im(z) + dy)
        if mp.im(z) <= mp.mpf(1) / 20:
            break
    return z, g_coset_full_mp(z, aff)


def newton_polish_tau_mp(tau_init, N, max_iter=35):
    """65-digit mpmath Newton polish directly on V_N(tau)."""
    tau = tau_init
    for _ in range(max_iter):
        info = V_N_full_mp(tau, N)
        gx, gy = info["grad"]
        if info["grad_norm"] < mp.mpf(10) ** (-58):
            return tau, info
        hxx, hxy, hyy = info["hess"]
        det = hxx * hyy - hxy * hxy
        if abs(det) < mp.mpf(10) ** (-50):
            break
        dx = -(hyy * gx - hxy * gy) / det
        dy = -(-hxy * gx + hxx * gy) / det
        step = mp.hypot(dx, dy)
        if step > mp.mpf(1) / (5 * max(1, N)):
            scale = (mp.mpf(1) / (5 * max(1, N))) / step
            dx *= scale
            dy *= scale
        tau = mp.mpc(mp.re(tau) + dx, mp.im(tau) + dy)
        if mp.im(tau) <= mp.mpf(1) / (100 * max(1, N)):
            break
    return tau, V_N_full_mp(tau, N)


def newton_polish_coset_c(z_init, alpha, beta, max_iter=25):
    """Fast float64 Newton polish on g_k(z)."""
    z = z_init
    for _ in range(max_iter):
        val, gx, gy, hxx, hxy, hyy, lmin, _ = g_coset_c(z, alpha, beta)
        gn = math.hypot(gx, gy)
        if gn < 1 / (10 ** 12):
            return z, val, gn, lmin
        det = hxx * hyy - hxy * hxy
        if abs(det) < 1 / (10 ** 18):
            break
        dx = -(hyy * gx - hxy * gy) / det
        dy = -(-hxy * gx + hxx * gy) / det
        step = math.hypot(dx, dy)
        if step > 1 / 5:
            scale = (1 / 5) / step
            dx *= scale
            dy *= scale
        z = complex(z.real + dx, z.imag + dy)
        if z.imag <= 1 / 10:
            break
    val, gx, gy, hxx, hxy, hyy, lmin, _ = g_coset_c(z, alpha, beta)
    return z, val, math.hypot(gx, gy), lmin


def analytic_cusp_cutoff_mp(V_upper):
    """
    Non-circular elementary proof of cusp cutoff Y_cut:
    For all w in H, f(w) >= f_lb := 1 + ln(pi/3) - 4*r0/(1-r0) where r0 = exp(-pi*sqrt(3)).
    For all z = x + i*y in F_1 with y >= 1,
      phi(y) := (pi/3)*y - ln(y) - 4*exp(-2*pi*y)/(1 - exp(-2*pi*y))
    is strictly increasing and satisfies f(z) >= phi(y), so
      g_k(z) = (pi/2)*(f(z) + f(alpha_k z + beta_k)) >= (pi/2)*(phi(y) + f_lb).
    Choose integer Y_cut >= 2 such that (pi/2)*(phi(Y_cut) + f_lb) > V_upper + 1/10.
    """
    pi = mp.pi
    r0 = mp.exp(-pi * mp.sqrt(3))
    f_lb = 1 + mp.log(pi / 3) - 4 * r0 / (1 - r0)
    Y = 2
    while True:
        y = mp.mpf(Y)
        ry = mp.exp(-2 * pi * y)
        phi_y = (pi / 3) * y - mp.log(y) - 4 * ry / (1 - ry)
        lb_V = (pi / 2) * (phi_y + f_lb)
        if lb_V > V_upper + mp.mpf(1) / 10:
            return Y, f_lb, lb_V
        Y += 1


def find_global_minima_level(N, n_x=36, n_y=54):
    r"""
    Search all mu(N) cosets of Gamma_0(N) \ SL(2, Z) on [-1/2, 1/2] x [sqrt(3)/2, Y_cut(N)],
    polish all candidate minima to 65-digit mpmath precision, close under mirror and Fricke,
    and deduplicate modulo Gamma_0(N) using the exact decidable finite-integer solver.
    """
    mp.mp.dps = 70
    cosets, affine_info, id_to_idx = build_gamma0_cosets(N)
    # Initial valid upper bound from mirror-Fricke point i/sqrt(N)
    V_seed = V_N_full_mp(mp.mpc(0, 1) / mp.sqrt(N), N)["val"]
    Y_cut, f_lb, lb_at_Ycut = analytic_cusp_cutoff_mp(V_seed)
    y_lo = math.sqrt(3) / 2
    y_hi = float(Y_cut)

    cand_taus_f64 = []
    best_grid_val = float(V_seed)
    for k, aff in enumerate(affine_info):
        alpha = aff["alpha_num"] / aff["alpha_den"]
        beta = aff["beta_num"] / aff["beta_den"]
        xs = [-1 / 2 + i / n_x for i in range(n_x + 1)]
        ys = [y_lo + j * (y_hi - y_lo) / n_y for j in range(n_y + 1)]
        grid = [[0 for _ in range(n_x + 1)] for _ in range(n_y + 1)]
        for j, yv in enumerate(ys):
            for i, xv in enumerate(xs):
                val = g_coset_c(complex(xv, yv), alpha, beta)[0]
                grid[j][i] = val
                if val < best_grid_val:
                    best_grid_val = val
        # Collect all local grid minima (including boundary) plus 8 lowest points per coset
        pts = []
        for j in range(n_y + 1):
            for i in range(n_x + 1):
                v = grid[j][i]
                is_loc = True
                for dj in (-1, 0, 1):
                    for di in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        jj, ii = j + dj, i + di
                        if 0 <= jj <= n_y and 0 <= ii <= n_x:
                            if grid[jj][ii] < v:
                                is_loc = False
                                break
                    if not is_loc:
                        break
                if is_loc:
                    pts.append((v, xs[i], ys[j]))
        # Also include lowest 8 grid nodes
        flat = [(grid[j][i], xs[i], ys[j]) for j in range(n_y + 1) for i in range(n_x + 1)]
        flat.sort(key=lambda t: t[0])
        for item in flat[:8]:
            pts.append(item)
        # Fast float64 Newton polish
        seen_c = []
        for _, xv, yv in pts:
            zp, vp, gnp, lminp = newton_polish_coset_c(complex(xv, yv), alpha, beta)
            if gnp < 1 / (10 ** 8) and lminp > 0 and vp <= best_grid_val + 1 / 5:
                if all(abs(zp - prev) > 1 / (10 ** 5) for prev in seen_c):
                    seen_c.append(zp)
                    tau_c = sl2_act_c(aff["gamma"], zp)
                    cand_taus_f64.append((vp, tau_c, k, zp))

    # Refine every promising candidate in 65-digit mpmath!
    cand_taus_f64.sort(key=lambda t: t[0])
    min_v_f64 = cand_taus_f64[0][0]
    polished = []
    for vp, tau_c, k, zp in cand_taus_f64:
        if vp > min_v_f64 + 1 / 20:
            continue
        aff = affine_info[k]
        z_mp, info_z = newton_polish_coset_mp(mp.mpc(zp.real, zp.imag), aff)
        if info_z["grad_norm"] < mp.mpf(10) ** (-48) and info_z["lambda_min"] > 0:
            tau_mp = sl2_act_mp(aff["gamma"], z_mp)
            tau_mp, info_t = newton_polish_tau_mp(tau_mp, N)
            if info_t["grad_norm"] < mp.mpf(10) ** (-48) and info_t["lambda_min"] > 0:
                polished.append((tau_mp, info_t))

    # Close candidates under mirror (-conj) and Fricke (-1/(N*tau)) so no partner can ever be missed
    expanded = list(polished)
    for tau_mp, _ in polished:
        for alt in (-mp.conj(tau_mp), -1 / (N * tau_mp), 1 / (N * mp.conj(tau_mp))):
            t_p, info_p = newton_polish_tau_mp(alt, N)
            if info_p["grad_norm"] < mp.mpf(10) ** (-48) and info_p["lambda_min"] > 0:
                expanded.append((t_p, info_p))

    V_min = min(info["val"] for _, info in expanded)
    # Recompute tight Y_cut using true V_min
    Y_cut, f_lb, lb_at_Ycut = analytic_cusp_cutoff_mp(V_min)

    # Filter to global minima within 10^-30 of V_min and deduplicate modulo Gamma_0(N)
    tol_glob = mp.mpf(10) ** (-30)
    distinct = []
    for tau_mp, info in expanded:
        if info["val"] - V_min > tol_glob:
            continue
        is_dup = False
        for d_tau, _ in distinct:
            if gamma0_equiv_decidable(tau_mp, d_tau, N)["is_equiv"]:
                is_dup = True
                break
        if not is_dup:
            # Canonicalize representative: shift Re(tau) into (-1/2, 1/2] via T^k in Gamma_0(N)
            k_sh = int(mp.floor(mp.re(tau_mp) + mp.mpf(1) / 2))
            if k_sh != 0:
                tau_mp = tau_mp - k_sh
                info = V_N_full_mp(tau_mp, N)
            distinct.append((tau_mp, info))

    # Sort deterministically by (Re(tau), Im(tau))
    distinct.sort(key=lambda pair: (float(mp.re(pair[0])), float(mp.im(pair[0]))))

    # Analyze CP mod Gamma_0(N), Fricke W_N action, and elliptic stabilizer order
    minima_records = []
    for idx, (tau_mp, info) in enumerate(distinct):
        cp_res = gamma0_equiv_decidable(-mp.conj(tau_mp), tau_mp, N)
        w_tau = -1 / (N * tau_mp)
        fricke_fixes = gamma0_equiv_decidable(w_tau, tau_mp, N)["is_equiv"]
        fricke_exchanges_cp = gamma0_equiv_decidable(w_tau, -mp.conj(tau_mp), N)["is_equiv"]
        # Identify exact index of CP image and Fricke image among distinct minima
        cp_img_idx = None
        fricke_img_idx = None
        for jdx, (other_tau, _) in enumerate(distinct):
            if cp_img_idx is None and gamma0_equiv_decidable(-mp.conj(tau_mp), other_tau, N)["is_equiv"]:
                cp_img_idx = jdx
            if fricke_img_idx is None and gamma0_equiv_decidable(w_tau, other_tau, N)["is_equiv"]:
                fricke_img_idx = jdx
        ell_ord, ell_stabs = elliptic_order_gamma0(tau_mp, N)
        minima_records.append({
            "index": idx,
            "tau_re": mp.nstr(mp.re(tau_mp), 45),
            "tau_im": mp.nstr(mp.im(tau_mp), 45),
            "V_val": mp.nstr(info["val"], 45),
            "grad_norm": mp.nstr(info["grad_norm"], 6),
            "lambda_min_H": mp.nstr(info["lambda_min"], 20),
            "lambda_max_H": mp.nstr(info["lambda_max"], 20),
            "det_H": mp.nstr(info["det_H"], 20),
            "cp_conserved_mod_Gamma0N": cp_res["is_equiv"],
            "cp_gamma": cp_res["best_gamma"] if cp_res["is_equiv"] else None,
            "cp_min_dist": mp.nstr(cp_res["min_dist"], 10),
            "cp_c_bound": cp_res["c_bound"],
            "cp_image_index": cp_img_idx,
            "fricke_fixes_vacuum": fricke_fixes,
            "fricke_exchanges_cp_pair": fricke_exchanges_cp,
            "fricke_image_index": fricke_img_idx,
            "elliptic_order": ell_ord,
            "elliptic_stabilizers": ell_stabs,
        })

    cp_broken = any(not rec["cp_conserved_mod_Gamma0N"] for rec in minima_records)
    return {
        "N": N,
        "mu_N": len(cosets),
        "cosets": cosets,
        "affine_info": affine_info,
        "id_to_idx": id_to_idx,
        "V_min_mp": V_min,
        "Y_cut": Y_cut,
        "f_lb": f_lb,
        "lb_at_Ycut": lb_at_Ycut,
        "distinct_taus": [pair[0] for pair in distinct],
        "minima_records": minima_records,
        "cp_broken_mod_Gamma0N": cp_broken,
    }


def certify_global_bnb_level(N, level_data):
    """
    Independent certified global Branch-and-Bound over 100% of X_0(N) for finite rung N.
    Covers [-1/2, 1/2] x [sqrt(3)/2, Y_cut(N)] across ALL mu(N) cosets.
    Uses:
      1. Exact domain check against |z| >= 1 (F_1 lower arc)
      2. Certified strictly convex minimum balls B(z_*, r_ball) verified in 65-digit mpmath
         where lambda_min(H(z_*)) - M_3(B(z_*, r_ball)) * r_ball > 0
      3. Rigorous 2nd/3rd-order Taylor-Hessian value pruning
      4. Rigorous gradient-monotonicity pruning (|grad(zc)| - M_2(B)*r > 0)
      5. Rigorous negative-curvature Hessian pruning (lambda_min(H(zc)) + M_3(B)*r < 0)
    """
    mp.mp.dps = 70
    cosets = level_data["cosets"]
    affine_info = level_data["affine_info"]
    id_to_idx = level_data["id_to_idx"]
    V_min_mp = level_data["V_min_mp"]
    Y_cut = level_data["Y_cut"]
    distinct_taus = level_data["distinct_taus"]

    def coset_id_local(mat):
        _, _, c, d = mat
        if N == 1:
            return (0, 0)
        units_local = [u for u in range(1, N) if math.gcd(u, N) == 1]
        return min(((u * (c % N)) % N, (u * (d % N)) % N) for u in units_local)

    # Collect ALL representatives z_* in [-1/2, 1/2] x [sqrt(3)/2, Y_cut] (including boundary
    # arcs and corners of F_1!) across all mu(N) cosets for every global minimum tau_*.
    T = (1, 1, 0, 1)
    Ti = (1, -1, 0, 1)
    S = (0, -1, 1, 0)
    short_words = [
        (1, 0, 0, 1), T, Ti, S,
        sl2_mul(S, T), sl2_mul(S, Ti),
        sl2_mul(T, S), sl2_mul(Ti, S),
        sl2_mul(T, sl2_mul(S, T)), sl2_mul(Ti, sl2_mul(S, Ti)),
        sl2_mul(S, sl2_mul(T, S)), sl2_mul(S, sl2_mul(Ti, S)),
        sl2_mul(T, sl2_mul(S, Ti)), sl2_mul(Ti, sl2_mul(S, T)),
    ]

    coset_balls = [[] for _ in range(len(cosets))]
    y_min_F1_mp = mp.sqrt(3) / 2
    pad_mp = mp.mpf(1) / 50

    for tau_star in distinct_taus:
        z0, g_red = reduce_to_F1_mp(tau_star)
        # g_red * tau_star = z0 => tau_star = g_red^{-1} * z0
        g_base = sl2_inv(g_red)
        for w_mat in short_words:
            # z_rep = w_mat * z0 => tau_star = (g_base * w_mat^{-1}) * z_rep
            z_rep = sl2_act_mp(w_mat, z0)
            if abs(mp.re(z_rep)) > mp.mpf(1) / 2 + pad_mp:
                continue
            if mp.im(z_rep) < y_min_F1_mp - pad_mp or mp.im(z_rep) > Y_cut + pad_mp:
                continue
            if abs(z_rep) < 1 - pad_mp:
                continue
            g_tot = sl2_mul(g_base, sl2_inv(w_mat))
            k = id_to_idx[coset_id_local(g_tot)]
            aff = affine_info[k]
            z_pol, info_z = newton_polish_coset_mp(z_rep, aff)
            if info_z["grad_norm"] > mp.mpf(10) ** (-48):
                continue
            if abs(info_z["val"] - V_min_mp) > mp.mpf(10) ** (-35):
                continue
            if any(abs(z_pol - b["z_mp"]) < mp.mpf(10) ** (-20) for b in coset_balls[k]):
                continue
            # Certify maximal strictly convex ball radius r_ball in 65-digit mpmath!
            lmin = info_z["lambda_min"]
            assert lmin > 0
            r_hi = mp.mpf(1) / 8
            r_lo = mp.mpf(0)
            best_r = mp.mpf(0)
            best_M3 = None
            best_margin = None
            # First shrink r_hi until valid bound exists
            while r_hi > mp.mpf(10) ** (-8):
                bnds = g_M2_M3_disk_bound_mp(z_pol, r_hi, aff)
                if bnds is not None and lmin - bnds[1] * r_hi > lmin / 5:
                    best_r = r_hi
                    best_M3 = bnds[1]
                    best_margin = lmin - bnds[1] * r_hi
                    r_lo = r_hi
                    break
                r_hi /= 2
            # Refine upper end by binary search
            r_top = min(mp.mpf(1) / 8, r_hi * 2)
            for _ in range(18):
                r_mid = (r_lo + r_top) / 2
                bnds = g_M2_M3_disk_bound_mp(z_pol, r_mid, aff)
                if bnds is not None and lmin - bnds[1] * r_mid > lmin / 5:
                    best_r = r_mid
                    best_M3 = bnds[1]
                    best_margin = lmin - bnds[1] * r_mid
                    r_lo = r_mid
                else:
                    r_top = r_mid
            # Require certified radius > 0 and Newton-Kantorovich uniqueness margin
            # |grad(z_pol)| / best_margin << best_r
            nk_shift = info_z["grad_norm"] / best_margin if best_margin and best_margin > 0 else mp.mpf(1)
            ball_ok = (best_r > mp.mpf(10) ** (-5) and best_margin > 0 and nk_shift < best_r / 1000)
            coset_balls[k].append({
                "coset_index": k,
                "z_mp": z_pol,
                "z_c": complex(float(mp.re(z_pol)), float(mp.im(z_pol))),
                "r_ball_mp": best_r,
                "r_ball_f": float(best_r) * (999 / 1000),
                "lambda_min": lmin,
                "M3_bound": best_M3,
                "convexity_margin": best_margin,
                "grad_norm": info_z["grad_norm"],
                "certified": ball_ok,
            })

    # Run certified Branch-and-Bound across ALL mu(N) cosets over [-1/2, 1/2] x [sqrt(3)/2, Y_cut]
    V_best_f = float(V_min_mp)
    eps_margin = 1 / (10 ** 10)
    y_lo_f = math.sqrt(3) / 2
    y_hi_f = float(Y_cut)
    max_depth = 22

    total_boxes = 0
    pruned_domain = 0
    pruned_ball = 0
    pruned_value = 0
    pruned_grad = 0
    pruned_hess = 0
    uncertified_boxes = []
    max_depth_reached = 0

    for k, aff in enumerate(affine_info):
        alpha = aff["alpha_num"] / aff["alpha_den"]
        beta = aff["beta_num"] / aff["beta_den"]
        balls_k = coset_balls[k]
        # Initial partition into well-proportioned squares (aspect ~ 1)
        nx0 = 4
        ny0 = max(4, int(math.ceil(4 * (y_hi_f - y_lo_f))))
        stack = []
        dx0 = 1 / nx0
        dy0 = (y_hi_f - y_lo_f) / ny0
        for j in range(ny0):
            y0 = y_lo_f + j * dy0
            y1 = y0 + dy0
            for i in range(nx0):
                x0 = -1 / 2 + i * dx0
                x1 = x0 + dx0
                stack.append((x0, x1, y0, y1, 0))

        while stack:
            x0, x1, y0, y1, depth = stack.pop()
            total_boxes += 1
            if depth > max_depth_reached:
                max_depth_reached = depth

            # 1. Domain prune: entire box strictly below unit circle |z| < 1
            xmax_abs = max(abs(x0), abs(x1))
            if xmax_abs * xmax_abs + y1 * y1 < 1 - 1 / (10 ** 12):
                pruned_domain += 1
                continue

            xc = (x0 + x1) / 2
            yc = (y0 + y1) / 2
            hx = (x1 - x0) / 2
            hy = (y1 - y0) / 2
            rz = math.hypot(hx, hy)
            zc = complex(xc, yc)

            # 2. Certified convex ball containment check
            in_ball = False
            for b in balls_k:
                if abs(zc - b["z_c"]) + rz <= b["r_ball_f"]:
                    in_ball = True
                    break
            if in_ball:
                pruned_ball += 1
                continue

            # 3. Evaluate exact center value/grad/Hessian and rigorous M2, M3 bounds
            bnds = g_M2_M3_disk_bound_c(zc, rz, alpha, beta)
            if bnds is not None:
                M2, M3 = bnds
                val, gx, gy, hxx, hxy, hyy, lmin, _ = g_coset_c(zc, alpha, beta)
                gn = math.hypot(gx, gy)

                # 3a. 3rd-order Taylor-Hessian value lower bound
                quad_lb = 0 if lmin >= 0 else (lmin * rz * rz) / 2
                val_lb3 = val - gn * rz + quad_lb - (M3 * (rz ** 3)) / 6
                val_lb2 = val - gn * rz - (M2 * rz * rz) / 2
                val_lb = max(val_lb2, val_lb3)
                if val_lb > V_best_f + eps_margin:
                    pruned_value += 1
                    continue

                # 3b. Gradient-monotonicity prune (global min of smooth V_N on H has grad == 0)
                if gn - M2 * rz > eps_margin:
                    pruned_grad += 1
                    continue

                # 3c. Strict non-positive curvature prune (min requires lambda_min >= 0)
                if lmin + M3 * rz < -eps_margin:
                    pruned_hess += 1
                    continue

            if depth >= max_depth:
                uncertified_boxes.append((k, x0, x1, y0, y1))
                continue

            # Subdivide along longer side (or quad-split)
            if hx >= hy:
                xm = (x0 + x1) / 2
                stack.append((x0, xm, y0, y1, depth + 1))
                stack.append((xm, x1, y0, y1, depth + 1))
            else:
                ym = (y0 + y1) / 2
                stack.append((x0, x1, y0, ym, depth + 1))
                stack.append((x0, x1, ym, y1, depth + 1))

    all_balls = [b for bl in coset_balls for b in bl]
    all_balls_ok = (len(all_balls) > 0 and all(b["certified"] for b in all_balls))
    return {
        "Y_cut": Y_cut,
        "f_lb": mp.nstr(level_data["f_lb"], 15),
        "V_lower_bound_at_Ycut": mp.nstr(level_data["lb_at_Ycut"], 15),
        "total_boxes_visited": total_boxes,
        "pruned_domain": pruned_domain,
        "pruned_convex_ball": pruned_ball,
        "pruned_value": pruned_value,
        "pruned_gradient": pruned_grad,
        "pruned_hessian": pruned_hess,
        "uncertified_box_count": len(uncertified_boxes),
        "max_depth_reached": max_depth_reached,
        "certified_convex_balls_count": len(all_balls),
        "min_ball_radius": mp.nstr(min(b["r_ball_mp"] for b in all_balls), 10) if all_balls else "0",
        "all_convex_balls_certified": all_balls_ok,
        "bnb_certified": (len(uncertified_boxes) == 0 and all_balls_ok),
    }


def run_task_ow2_b():
    mp.mp.dps = 70
    # 1. Verify Gamma_0(N), Fricke W_N, mirror invariances, affine HNF identity,
    #    exact Wirtinger gradient, Hessian, and hyperbolic Laplacian across N = 1..5.
    test_pts = [
        mp.mpc(1, 0) / 7 + mp.mpc(0, 11) / 9,
        mp.mpc(-3, 0) / 13 + mp.mpc(0, 7) / 8,
        mp.mpc(4, 0) / 17 + mp.mpc(0, 13) / 10,
    ]
    inv_checks = {}
    max_inv_err = mp.mpf(0)
    max_fd_err = mp.mpf(0)
    max_lap_err = mp.mpf(0)
    max_hnf_err = mp.mpf(0)

    for N in range(1, 6):
        _, affine_info, _ = build_gamma0_cosets(N)
        err_gamma0 = mp.mpf(0)
        err_fricke = mp.mpf(0)
        err_mirror = mp.mpf(0)
        err_hnf = mp.mpf(0)
        err_fd = mp.mpf(0)
        err_lap = mp.mpf(0)
        g_T = (1, 1, 0, 1)
        g_L = (1, 0, N, 1)
        g_prod = sl2_mul(g_T, sl2_mul(g_L, g_T))
        for tau in test_pts:
            v0 = V_N_full_mp(tau, N)
            for g in (g_T, g_L, g_prod):
                vg = V_N_full_mp(sl2_act_mp(g, tau), N)
                err_gamma0 = max(err_gamma0, abs(vg["val"] - v0["val"]))
            vw = V_N_full_mp(-1 / (N * tau), N)
            err_fricke = max(err_fricke, abs(vw["val"] - v0["val"]))
            vm = V_N_full_mp(-mp.conj(tau), N)
            err_mirror = max(err_mirror, abs(vm["val"] - v0["val"]))
            err_lap = max(err_lap, abs(v0["lap_hyp"] - mp.pi))
            # Check exact HNF affine reduction on every coset
            for aff in affine_info:
                v_dir = V_N_full_mp(sl2_act_mp(aff["gamma"], tau), N)["val"]
                v_aff = g_coset_full_mp(tau, aff)["val"]
                err_hnf = max(err_hnf, abs(v_dir - v_aff))
            # Check exact Wirtinger formula dV/dtau = i*pi/(2y) - (i*pi^2/12)*(E2(tau) + N*E2(N*tau))
            e2_1, _, _ = e2_e4_e6_mp(tau)
            e2_N, _, _ = e2_e4_e6_mp(N * tau)
            dw_card = mp.mpc(0, 1) * mp.pi / (2 * mp.im(tau)) - (mp.mpc(0, 1) * (mp.pi ** 2) / 12) * (e2_1 + N * e2_N)
            err_fd = max(err_fd, abs(v0["dw"] - dw_card))
            # 4th-order central finite differences for gradient and Hessian (h = 10^-6 at dps=70 -> < 10^-22 err)
            h = mp.mpf(10) ** (-6)
            vx_p1 = V_N_full_mp(tau + h, N)["val"]
            vx_m1 = V_N_full_mp(tau - h, N)["val"]
            vx_p2 = V_N_full_mp(tau + 2 * h, N)["val"]
            vx_m2 = V_N_full_mp(tau - 2 * h, N)["val"]
            vy_p1 = V_N_full_mp(tau + mp.mpc(0, 1) * h, N)["val"]
            vy_m1 = V_N_full_mp(tau - mp.mpc(0, 1) * h, N)["val"]
            vy_p2 = V_N_full_mp(tau + mp.mpc(0, 2) * h, N)["val"]
            vy_m2 = V_N_full_mp(tau - mp.mpc(0, 2) * h, N)["val"]
            gx_fd = (-vx_p2 + 8 * vx_p1 - 8 * vx_m1 + vx_m2) / (12 * h)
            gy_fd = (-vy_p2 + 8 * vy_p1 - 8 * vy_m1 + vy_m2) / (12 * h)
            hxx_fd = (-vx_p2 + 16 * vx_p1 - 30 * v0["val"] + 16 * vx_m1 - vx_m2) / (12 * h * h)
            hyy_fd = (-vy_p2 + 16 * vy_p1 - 30 * v0["val"] + 16 * vy_m1 - vy_m2) / (12 * h * h)
            vpp = V_N_full_mp(tau + mp.mpc(1, 1) * h, N)["val"]
            vpm = V_N_full_mp(tau + mp.mpc(1, -1) * h, N)["val"]
            vmp = V_N_full_mp(tau + mp.mpc(-1, 1) * h, N)["val"]
            vmm = V_N_full_mp(tau + mp.mpc(-1, -1) * h, N)["val"]
            hxy_fd = (vpp - vpm - vmp + vmm) / (4 * h * h)
            err_fd = max(
                err_fd,
                abs(gx_fd - v0["grad"][0]),
                abs(gy_fd - v0["grad"][1]),
                abs(hxx_fd - v0["hess"][0]),
                abs(hyy_fd - v0["hess"][2]),
                abs(hxy_fd - v0["hess"][1]),
            )
        max_inv_err = max(max_inv_err, err_gamma0, err_fricke, err_mirror)
        max_fd_err = max(max_fd_err, err_fd)
        max_lap_err = max(max_lap_err, err_lap)
        max_hnf_err = max(max_hnf_err, err_hnf)
        inv_checks[str(N)] = {
            "gamma0_inv_err": mp.nstr(err_gamma0, 6),
            "fricke_inv_err": mp.nstr(err_fricke, 6),
            "mirror_inv_err": mp.nstr(err_mirror, 6),
            "hnf_affine_err": mp.nstr(err_hnf, 6),
            "grad_hess_fd_err": mp.nstr(err_fd, 6),
            "lap_hyp_err_vs_pi": mp.nstr(err_lap, 6),
        }

    # 2. Certified Global Branch-and-Bound across ALL five finite rungs N = 1, 2, 3, 4, 5
    rungs = {}
    total_uncertified = 0
    all_balls_ok = True
    max_grad_all = mp.mpf(0)
    n5_exact_cm_err = None

    for N in range(1, 6):
        ldata = find_global_minima_level(N, n_x=36, n_y=54)
        bnb = certify_global_bnb_level(N, ldata)
        total_uncertified += bnb["uncertified_box_count"]
        if not bnb["all_convex_balls_certified"]:
            all_balls_ok = False
        for rec in ldata["minima_records"]:
            gn = mp.mpf(rec["grad_norm"])
            if gn > max_grad_all:
                max_grad_all = gn
        if N == 5:
            # Verify against exact algebraic CM/orbifold points (+-2 + i)/5
            cm_p = mp.mpc(2, 1) / 5
            cm_m = mp.mpc(-2, 1) / 5
            d_p = min(gamma0_equiv_decidable(t, cm_p, 5)["min_dist"] for t in ldata["distinct_taus"])
            d_m = min(gamma0_equiv_decidable(t, cm_m, 5)["min_dist"] for t in ldata["distinct_taus"])
            n5_exact_cm_err = max(d_p, d_m)
        rungs[str(N)] = {
            "N": N,
            "mu_N": ldata["mu_N"],
            "V_min": mp.nstr(ldata["V_min_mp"], 45),
            "n_distinct_global_minima": len(ldata["minima_records"]),
            "cp_broken_mod_Gamma0N": ldata["cp_broken_mod_Gamma0N"],
            "minima": ldata["minima_records"],
            "bnb": bnb,
        }

    tol_50 = mp.mpf(10) ** (-50)
    tol_14 = mp.mpf(10) ** (-14)
    passed = (
        max_inv_err < tol_50
        and max_hnf_err < tol_50
        and max_lap_err < tol_50
        and max_fd_err < tol_14
        and total_uncertified == 0
        and all_balls_ok
        and max_grad_all < tol_50
        and n5_exact_cm_err is not None
        and n5_exact_cm_err < tol_50
    )
    return {
        "invariance_and_calculus_checks": inv_checks,
        "max_invariance_err": mp.nstr(max_inv_err, 6),
        "max_hnf_affine_err": mp.nstr(max_hnf_err, 6),
        "max_grad_hess_fd_err": mp.nstr(max_fd_err, 6),
        "max_laplacian_err": mp.nstr(max_lap_err, 6),
        "total_uncertified_boxes": total_uncertified,
        "all_convex_balls_certified": all_balls_ok,
        "max_grad_at_all_minima": mp.nstr(max_grad_all, 6),
        "N5_match_to_exact_pm2_plus_i_over_5_err": mp.nstr(n5_exact_cm_err, 6),
        "rungs": rungs,
        "pass": passed,
    }


def run_task_ow2_c(ow2_b_data):
    mp.mp.dps = 70
    control_levels = [6, 7, 8, 9, 10, 11, 13]
    controls = {}
    max_grad_ctrl = mp.mpf(0)
    all_pd = True

    for N in control_levels:
        ldata = find_global_minima_level(N, n_x=40, n_y=60)
        for rec in ldata["minima_records"]:
            gn = mp.mpf(rec["grad_norm"])
            if gn > max_grad_ctrl:
                max_grad_ctrl = gn
            if mp.mpf(rec["lambda_min_H"]) <= 0:
                all_pd = False
        controls[str(N)] = {
            "N": N,
            "mu_N": ldata["mu_N"],
            "Y_cut": ldata["Y_cut"],
            "V_min": mp.nstr(ldata["V_min_mp"], 45),
            "n_distinct_global_minima": len(ldata["minima_records"]),
            "cp_broken_mod_Gamma0N": ldata["cp_broken_mod_Gamma0N"],
            "minima": ldata["minima_records"],
        }

    # Build complete H11 / Shimura (nu_2, nu_3) algebraic bridge table across N in {1..13}
    bridge_table = []
    for N in range(1, 14):
        alg = shimura_elliptic_counts(N)
        if N <= 5:
            r = ow2_b_data["rungs"][str(N)]
            cp_brk = r["cp_broken_mod_Gamma0N"]
            n_min = r["n_distinct_global_minima"]
            ell_ords = sorted(set(m["elliptic_order"] for m in r["minima"]))
            fricke_ex = any(m["fricke_exchanges_cp_pair"] for m in r["minima"])
            v_min_str = r["V_min"]
        elif str(N) in controls:
            r = controls[str(N)]
            cp_brk = r["cp_broken_mod_Gamma0N"]
            n_min = r["n_distinct_global_minima"]
            ell_ords = sorted(set(m["elliptic_order"] for m in r["minima"]))
            fricke_ex = any(m["fricke_exchanges_cp_pair"] for m in r["minima"])
            v_min_str = r["V_min"]
        else:
            cp_brk = None
            n_min = None
            ell_ords = None
            fricke_ex = None
            v_min_str = None
        bridge_table.append({
            "N": N,
            "is_finite_triangle_rung": (N <= 5),
            "mu_N": alg["mu_N"],
            "H11_minus1_is_square_mod_N": alg["H11_minus1_is_square_mod_N"],
            "nu_2": alg["nu_2"],
            "nu_3": alg["nu_3"],
            "V_min": v_min_str,
            "n_distinct_global_minima": n_min,
            "cp_broken_mod_Gamma0N": cp_brk,
            "min_elliptic_orders": ell_ords,
            "fricke_exchanges_cp_pair": fricke_ex,
        })

    passed = (max_grad_ctrl < mp.mpf(10) ** (-45) and all_pd)
    return {
        "control_rungs": controls,
        "max_grad_controls": mp.nstr(max_grad_ctrl, 6),
        "all_control_minima_positive_definite": all_pd,
        "algebraic_bridge_table": bridge_table,
        "pass": passed,
    }


# =============================================================================
# TASK OW2-D: INDEPENDENT GL6 FUCHSIAN L_2(tau) SOLVER & GATE F-U2 YUKAWA CP
# =============================================================================

def exact_gl6_extrap_weights(n_seq):
    """Exact rational weights canceling h^6, h^8, ..., h^(4+2K) for symmetric 3-stage GL6."""
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


def make_weierstrass_wp_fast(tau):
    """High-precision Weierstrass wp(z; 1, tau) via fast theta_1 Chebyshev-angle recurrence."""
    e2, _, _ = e2_e4_e6_mp(tau)
    pi = mp.pi
    c_e2 = (pi * pi / 3) * e2
    tol = mp.mpf(10) ** (-mp.mp.dps - 55)
    coefs = []
    for n in range(0, 100):
        coef = ((-1) ** n) * mp.exp(pi * mp.mpc(0, 1) * tau * ((n + mp.mpf(1) / 2) ** 2))
        k = 2 * n + 1
        kpi = k * pi
        coefs.append((kpi, kpi * kpi, 2 * coef))
        if n > 4 and abs(coef) < tol:
            break
    im_t = mp.im(tau)

    def wp(z):
        k_shift = int(mp.nint(mp.im(z) / im_t))
        if k_shift != 0:
            z = z - k_shift * tau
        arg1 = pi * z
        s1 = mp.sin(arg1)
        c1 = mp.cos(arg1)
        s2 = 2 * s1 * c1
        c2 = 2 * c1 * c1 - 1
        sk, ck = s1, c1
        t0 = mp.mpc(0)
        t1 = mp.mpc(0)
        t2 = mp.mpc(0)
        for kpi, kpi2, c2f in coefs:
            t0 += c2f * sk
            t1 += c2f * kpi * ck
            t2 -= c2f * kpi2 * sk
            sk, ck = sk * c2 + ck * s2, ck * c2 - sk * s2
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


def gl6_tableau():
    """Exact 3-stage 6th-order symplectic Gauss-Legendre Runge-Kutta Butcher tableau."""
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
    """Integrate U'' + (wp/4 + c) U = 0 (and variational d/dc system if need_dc) by 3-stage GL6."""
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
                dr1 = [dU1 + dz * c_nodes[i] * dV1 - dz2 * sum(A2[i][k] * Us1[k] for k in range(3)) for i in range(3)]
                dr2 = [dU2 + dz * c_nodes[i] * dV2 - dz2 * sum(A2[i][k] * Us2[k] for k in range(3)) for i in range(3)]
                dUs1, dUs2 = solve3x3_two_rhs(M, dr1, dr2)
                dVs1 = [dV1 - dz * sum(A[i][k] * (qs[k] * dUs1[k] + Us1[k]) for k in range(3)) for i in range(3)]
                dVs2 = [dV2 - dz * sum(A[i][k] * (qs[k] * dUs2[k] + Us2[k]) for k in range(3)) for i in range(3)]
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
    r"""
    Independent GL6 + order-20 rational extrapolation + exact Frobenius puncture-matching
    solver for the length-2 horocycle cutoff L_2(tau) on E_tau \ {0} for tau in F_1.
    Uses exact conjugate contour geometry under tau -> -conj(tau) (no mirror caching).
    """
    wp = make_weierstrass_wp_fast(tau)
    glc = gl6_tableau()
    pos_re = (mp.re(tau) > 0)
    # Conjugate contour geometry: for Re(tau)>0 integrate in w = -z so contour for tau is
    # exact complex conjugate of contour for -conj(tau) (even symmetry wp(-z) = wp(z)).
    if pos_re:
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
        f = [mp.im(M1[0, 0] + M1[1, 1]), mp.im(MB[0, 0] + MB[1, 1]), mp.im((M1 * MB)[0, 0] + (M1 * MB)[1, 1])]
        J = [[mp.im(dtA), mp.re(dtA)], [mp.im(dtB), mp.re(dtB)], [mp.im(dtAB), mp.re(dtAB)]]
        return f, J

    # Stage 1: fast single n=6 GL6 Gauss-Newton
    cr = (mp.pi ** 2) / 12
    ci = mp.mpf(0)
    for _ in range(10):
        c_val = mp.mpc(cr, ci)
        HA, dHA = gl6_chain_integrate(preA_m[1], c_val, glc, True)
        HB, dHB = gl6_chain_integrate(preB_m[1], c_val, glc, True)
        M1, dM1 = half_to_full_monodromy(HA, dHA)
        MB, dMB = half_to_full_monodromy(HB, dHB)
        f = [mp.im(M1[0, 0] + M1[1, 1]), mp.im(MB[0, 0] + MB[1, 1]), mp.im((M1 * MB)[0, 0] + (M1 * MB)[1, 1])]
        if max(abs(x) for x in f) < mp.mpf(10) ** (-11):
            break
        dtA = dM1[0, 0] + dM1[1, 1]
        dtB = dMB[0, 0] + dMB[1, 1]
        dAB = dM1 * MB + M1 * dMB
        dtAB = dAB[0, 0] + dAB[1, 1]
        J = [[mp.im(dtA), mp.re(dtA)], [mp.im(dtB), mp.re(dtB)], [mp.im(dtAB), mp.re(dtAB)]]
        cr, ci = gn_step(cr, ci, f, J)

    # Stage 2: medium order-12 GL6 extrapolation
    for _ in range(4):
        c_val = mp.mpc(cr, ci)
        f, J = get_f_J_m(c_val)
        if max(abs(x) for x in f) < mp.mpf(10) ** (-26):
            break
        cr, ci = gn_step(cr, ci, f, J)

    # Stage 3: fine order-20 GL6 extrapolation using frozen medium Jacobian
    preA_f = precompute_gl6_chains(segs_A, wp, n_seq_f, glc)
    preB_f = precompute_gl6_chains(segs_B, wp, n_seq_f, glc)
    _, J_ref = get_f_J_m(mp.mpc(cr, ci))
    for _ in range(3):
        c_val = mp.mpc(cr, ci)
        HA, _ = gl6_extrap_eval(preA_f, w_f, c_val, glc, False)
        HB, _ = gl6_extrap_eval(preB_f, w_f, c_val, glc, False)
        M1, _ = half_to_full_monodromy(HA, [0, 0, 0, 0])
        MB, _ = half_to_full_monodromy(HB, [0, 0, 0, 0])
        f = [mp.im(M1[0, 0] + M1[1, 1]), mp.im(MB[0, 0] + MB[1, 1]), mp.im((M1 * MB)[0, 0] + (M1 * MB)[1, 1])]
        if max(abs(x) for x in f) < mp.mpf(10) ** (-58):
            break
        cr, ci = gn_step(cr, ci, f, J_ref)

    c_star = mp.mpc(cr, ci)
    HA, _ = gl6_extrap_eval(preA_f, w_f, c_star, glc, False)
    HB, _ = gl6_extrap_eval(preB_f, w_f, c_star, glc, False)
    M1, _ = half_to_full_monodromy(HA, [0, 0, 0, 0])
    MB, _ = half_to_full_monodromy(HB, [0, 0, 0, 0])

    # Conjugate (m1, mB) into SL(2, R) with parabolic commutator P upper-triangular
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

    # Dyadic inward integration z0 -> zs (|zs| <= 1/10)
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

    # Exact 48-term Frobenius expansion at zs around puncture z = 0
    _, e4, e6 = e2_e4_e6_mp(tau)
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
    slope_err = abs(-slope - mp.mpc(0, 1) * lam / (2 * mp.pi))
    return {
        "L2": L2_val,
        "c_star": c_star,
        "lambda_parabolic": lam,
        "w_check": w_chk,
        "slope_err": slope_err,
        "im_mBh_err": im_mBh,
    }


def solve_L2_any_gl6(tau, cache=None):
    """
    Evaluate L_2(tau) for any tau in H using SL(2, Z) Horocycle covariance:
      L_2(gamma * tau) = L_2(tau) + ln|c*tau + d|  =>  L_2(tau) = L_2(tau_red) - ln|c*tau + d|.
    Note: cache keys strictly on exact tau_red (NEVER collapses +x with -x!).
    """
    tau_red, g = reduce_to_F1_mp(tau)
    _, _, c, d = g
    key = (mp.nstr(mp.re(tau_red), 55), mp.nstr(mp.im(tau_red), 55))
    if cache is not None and key in cache:
        base = cache[key]
    else:
        base = solve_L2_F1_gl6(tau_red)
        if cache is not None:
            cache[key] = base
    L2_val = base["L2"] - mp.log(abs(c * tau + d))
    return L2_val, base, tau_red, g


def build_fu2_coupling_tensor():
    """
    Build exact Gate F-U2 quaternion Clifford basis and rank-4 coupling tensor C[qi, si, a, b]
    from Card A2-WG96 Erratum 2 (S reading):
      blocks = [Q_J, Q_I, Q_K], q_S = [Q_I, Q_J, Q_K], EPS = Q_J, units = [I_2, Q_I, Q_J, Q_K].
    """
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
    # Verify exact biorthogonality <ec_list[t], edual[a]>_H == delta_{ta}
    for t in range(4):
        for a in range(4):
            assert abs(frob(ec_list[t], edual[a]) - (1 if t == a else 0)) < mp.mpf(10) ** (-60)

    C = [[[[mp.mpc(0) for _ in range(3)] for _ in range(3)] for _ in range(4)] for _ in range(3)]
    for qi in range(3):
        for si in range(4):
            for a in range(3):
                for b in range(3):
                    mat = (blocks[a].T) * EPS * q_S[qi] * blocks[b]
                    C[qi][si][a][b] = frob(mat, edual[si])
    return ec_list, C


def theta_and_dot_mp(alpha_f, beta_f, tau):
    """Evaluate theta(alpha, beta | tau) and dot{theta}(alpha, beta | tau) dynamically to mp.mp.dps."""
    alpha = mp.mpf(alpha_f.numerator) / mp.mpf(alpha_f.denominator)
    beta = mp.mpf(beta_f.numerator) / mp.mpf(beta_f.denominator)
    pi = mp.pi
    i_pi_tau = mp.mpc(0, 1) * pi * tau
    two_pi_i_b = mp.mpc(0, 2) * pi * beta
    tol = mp.mpf(10) ** (-mp.mp.dps - 8)
    th = mp.mpc(0)
    dth = mp.mpc(0)
    # Sum outward from n = 0
    for k in range(0, 200):
        ns = [0] if k == 0 else [k, -k]
        max_t = mp.mpf(0)
        for nn in ns:
            na = nn + alpha
            na2 = na * na
            term = mp.exp(i_pi_tau * na2 + two_pi_i_b * na)
            th += term
            dth += (na2 / 2) * term
            at = abs(term) * (1 + na2)
            if at > max_t:
                max_t = at
        if k > 4 and max_t < tol:
            break
    return th, dth


def compute_c3_and_denom_mp(tau):
    et = eta_mp(tau)
    denom_hat = 2 * mp.pi * (et ** 3)
    e2, _, _ = e2_e4_e6_mp(tau)
    th2, dth2 = theta_and_dot_mp(Fraction(1, 2), Fraction(0), tau)
    th4, dth4 = theta_and_dot_mp(Fraction(0), Fraction(1, 2), tau)
    th3, dth3 = theta_and_dot_mp(Fraction(0), Fraction(0), tau)
    im = mp.mpc(0, 1)
    R_h = [-(th2 * th2) / denom_hat, -(th4 * th4) / denom_hat, (im * th3 * th3) / denom_hat]
    dN_h = [-(2 * th2 * dth2) / denom_hat, -(2 * th4 * dth4) / denom_hat, (2 * im * th3 * dth3) / denom_hat]
    c_3 = [dN_h[k] - (e2 / 12) * R_h[k] for k in range(3)]
    return c_3, denom_hat


def eval_X0_X1_mp(alpha_f, beta_f, tau):
    alpha = mp.mpf(alpha_f.numerator) / mp.mpf(alpha_f.denominator)
    beta = mp.mpf(beta_f.numerator) / mp.mpf(beta_f.denominator)
    pi = mp.pi
    c_tau = mp.mpc(0, 2) * pi * tau
    c_beta = mp.mpc(0, 2) * pi * beta
    tol = mp.mpf(10) ** (-mp.mp.dps - 8)
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    # Center integer summation around -round(alpha)
    n0 = -int(mp.nint(alpha))
    for k in range(0, 200):
        ns = [n0] if k == 0 else [n0 + k, n0 - k]
        max_t = mp.mpf(0)
        for nn in ns:
            val = nn + alpha
            t0 = mp.exp(c_tau * (val * val) + c_beta * val)
            vh = val + mp.mpf(1) / 2
            t1 = mp.exp(c_tau * (vh * vh) + c_beta * val)
            s0 += t0
            s1 += t1
            at = max(abs(t0), abs(t1))
            if at > max_t:
                max_t = at
        if k > 4 and max_t < tol:
            break
    return s0, s1


def eval_fu_a0_mp(u_a_f, u_b_f, tau):
    r"""Exact high-precision f_u and a_0 for characteristic shift (u_a, u_b) in [0, 1)^2 \ {(0,0)}."""
    pi = mp.pi
    x = mp.re(tau)
    y = mp.im(tau)
    q = mp.exp(mp.mpc(0, 2) * pi * tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 8)
    u_a = mp.mpf(u_a_f.numerator) / mp.mpf(u_a_f.denominator)
    u_b = mp.mpf(u_b_f.numerator) / mp.mpf(u_b_f.denominator)

    def w_term(s_val):
        ws = mp.exp(mp.mpc(0, 2) * pi * (s_val * x + u_b) - 2 * pi * abs(s_val) * y)
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
    nu = mp.mpf(nu_f.numerator) / mp.mpf(nu_f.denominator)
    Bm_f = (-u_b_f) % 1
    Bm = mp.mpf(Bm_f.numerator) / mp.mpf(Bm_f.denominator)
    w_z = nu * tau - Bm
    sum_a0 = mp.mpc(0)
    im2 = mp.mpc(0, 2)
    for m in range(1, 1000):
        t = (mp.exp(im2 * pi * m * (tau + w_z)) - mp.exp(im2 * pi * m * (tau - w_z))) / (im2 * (1 - (q ** m)))
        sum_a0 += t
        if m > 4 and abs(t) < tol:
            break
    a_0 = pi * mp.cot(pi * w_z) + 4 * pi * sum_a0 + im2 * pi * nu
    return f_u, a_0


def eval_gate_fu2_24pt_sector(tau, L2_val, q_L, q_R, ec_list, C_ten, c_3, denom_hat):
    r"""
    Evaluate bare 24-point Weil-phased Gate F-U2 operator:
      Y_f(tau) = sum_{(a,b) in (Z/5)^2 \ {(0,0)}} zeta_5^{-a*b} Y(tau, L_2(tau); q_L*w_{a,b}, q_R*w_{a,b})
    with centered coordinates a_c, b_c in {-2, -1, 0, 1, 2} and exact rational shifts.
    """
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

    # Precompute f_u, a_0 cache on exact rational (u_a, u_b) mod 1 for this tau
    fu_cache = {}
    Y_sum = mp.matrix(3, 3)

    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            a_c = a if a <= 2 else a - 5
            b_c = b if b <= 2 else b - 5
            wL0 = Fraction(q_L * a_c, 5)
            wL1 = Fraction(q_L * b_c, 5)
            wR0 = Fraction(q_R * a_c, 5)
            wR1 = Fraction(q_R * b_c, 5)

            ax_f, bx_f = wL0, 2 * wL1
            ay_f, by_f = wR0, 2 * wR1
            X0x, X1x = eval_X0_X1_mp(ax_f, bx_f, tau)
            X0y, X1y = eval_X0_X1_mp(ay_f, by_f, tau)
            bx = mp.mpf(bx_f.numerator) / mp.mpf(bx_f.denominator)
            by = mp.mpf(by_f.numerator) / mp.mpf(by_f.denominator)
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
                        fu_cache[key] = eval_fu_a0_mp(ua_f, ub_f, tau)
                    f_u, a_0 = fu_cache[key]
                    rad = base_const + f_u - pi * (abs(a_0) ** 2) * exp_m2L2
                    u_ch[si] = mp.sqrt(rad) * R_ch[si]

            phi_ab = mp.exp(mp.mpc(0, 2) * pi * ((-a * b) % 5) / 5)
            for ia in range(3):
                for ib in range(3):
                    entry = mp.mpc(0)
                    for qi in range(3):
                        for si in range(4):
                            cc = C_ten[qi][si][ia][ib]
                            if cc != 0:
                                entry += c_3[qi] * u_ch[si] * cc
                    Y_sum[ia, ib] += phi_ab * entry

    return Y_sum


def extract_cp_observables_mp(Yu, Yd):
    """
    Extract exact singular values, |V_ij|, basis-invariant Jarlskog commutator determinant
      J_det_norm = Im(det([H_u, H_d])) / (Tr(H_u)^3 * Tr(H_d)^3),
    and normalized J_CP in current mp.mp.dps.
    """
    Hu = Yu * Yu.H
    Hd = Yd * Yd.H
    comm = Hu * Hd - Hd * Hu
    det_comm = mp.det(comm)
    tr_u = mp.re(Hu[0, 0] + Hu[1, 1] + Hu[2, 2])
    tr_d = mp.re(Hd[0, 0] + Hd[1, 1] + Hd[2, 2])
    J_det_raw = mp.im(det_comm)
    J_det_re_err = abs(mp.re(det_comm))
    J_det_norm = J_det_raw / ((tr_u ** 3) * (tr_d ** 3))

    # Diagonalize H_u and H_d in descending order of eigenvalues
    ev_u, Uu_raw = mp.eighe(Hu)
    ev_d, Ud_raw = mp.eighe(Hd)
    idx_u = sorted(range(3), key=lambda i: mp.re(ev_u[i]), reverse=True)
    idx_d = sorted(range(3), key=lambda i: mp.re(ev_d[i]), reverse=True)
    lu = [max(mp.mpf(0), mp.re(ev_u[i])) for i in idx_u]
    ld = [max(mp.mpf(0), mp.re(ev_d[i])) for i in idx_d]
    su = [mp.sqrt(x) for x in lu]
    sd = [mp.sqrt(x) for x in ld]
    Uu = mp.matrix(3, 3)
    Ud = mp.matrix(3, 3)
    for col in range(3):
        for row in range(3):
            Uu[row, col] = Uu_raw[row, idx_u[col]]
            Ud[row, col] = Ud_raw[row, idx_d[col]]

    V = Uu.H * Ud
    V_abs = [[abs(V[i, j]) for j in range(3)] for i in range(3)]

    deg_tol = mp.mpf(10) ** (-25)
    gap_u = min((su[0] - su[1]) / su[0], (su[1] - su[2]) / su[0]) if su[0] > 0 else mp.mpf(0)
    gap_d = min((sd[0] - sd[1]) / sd[0], (sd[1] - sd[2]) / sd[0]) if sd[0] > 0 else mp.mpf(0)
    is_deg = (gap_u < deg_tol or gap_d < deg_tol)

    if is_deg:
        J_CP = mp.mpf(0)
        J_CP_identity_err = abs(J_det_norm)
    else:
        J_CP = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))
        Delta_u = (lu[0] - lu[1]) * (lu[0] - lu[2]) * (lu[1] - lu[2])
        Delta_d = (ld[0] - ld[1]) * (ld[0] - ld[2]) * (ld[1] - ld[2])
        J_CP_from_det = abs(J_det_raw / (2 * Delta_u * Delta_d))
        J_CP_identity_err = abs(abs(J_CP) - J_CP_from_det)

    ru = [su[1] / su[0], su[2] / su[0]] if su[0] > 0 else [mp.mpf(0), mp.mpf(0)]
    rd = [sd[1] / sd[0], sd[2] / sd[0]] if sd[0] > 0 else [mp.mpf(0), mp.mpf(0)]
    return {
        "su": su,
        "sd": sd,
        "ru": ru,
        "rd": rd,
        "V_abs": V_abs,
        "Uu": Uu,
        "Ud": Ud,
        "is_degenerate": is_deg,
        "min_gap_u": gap_u,
        "min_gap_d": gap_d,
        "J_det_raw": J_det_raw,
        "J_det_re_err": J_det_re_err,
        "J_det_norm": J_det_norm,
        "J_CP": J_CP,
        "J_CP_identity_err": J_CP_identity_err,
    }


def random_haar_u3_mp(rng):
    """Exact Mezzadri (2007) Haar random U(3) matrix in current mp.mp.dps (zero float literals)."""
    two128 = 1 << 128

    def std_normal_mp():
        u1 = mp.mpf(rng.randrange(1, two128)) / mp.mpf(two128)
        u2 = mp.mpf(rng.randrange(1, two128)) / mp.mpf(two128)
        rad = mp.sqrt(-2 * mp.log(u1))
        ang = 2 * mp.pi * u2
        return rad * mp.cos(ang), rad * mp.sin(ang)

    Z = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            x, y = std_normal_mp()
            Z[r, c] = mp.mpc(x, y)

    # Modified Gram-Schmidt QR with diagonal phase normalization R_{kk} / |R_{kk}|
    Q = mp.matrix(3, 3)
    R = mp.matrix(3, 3)
    for k in range(3):
        v = [Z[r, k] for r in range(3)]
        for j in range(k):
            dot = sum(mp.conj(Q[r, j]) * v[r] for r in range(3))
            R[j, k] = dot
            v = [v[r] - dot * Q[r, j] for r in range(3)]
        # Re-orthogonalize once for full working precision
        for j in range(k):
            dot2 = sum(mp.conj(Q[r, j]) * v[r] for r in range(3))
            R[j, k] += dot2
            v = [v[r] - dot2 * Q[r, j] for r in range(3)]
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
        R[k, k] = nrm
        for r in range(3):
            Q[r, k] = v[r] / nrm
    # Note: R[k,k] > 0 already; to match Mezzadri exactly, apply random unit phase per column
    # from original Z diagonal (or note QR with R_kk > 0 on isotropic Ginibre IS exact Haar!)
    return Q


def run_haar_scrambling_mp(Yu, Yd, seed, n_trials=10, dps_haar=50):
    """Mandatory Guardrail 3: 10-trial random Haar unitary basis-scrambling in 50-digit mpmath."""
    old_dps = mp.mp.dps
    mp.mp.dps = dps_haar
    Yu_h = mp.matrix([[mp.mpc(Yu[r, c]) for c in range(3)] for r in range(3)])
    Yd_h = mp.matrix([[mp.mpc(Yd[r, c]) for c in range(3)] for r in range(3)])
    base = extract_cp_observables_mp(Yu_h, Yd_h)
    rng = random.Random(seed)

    max_unitarity_err = mp.mpf(0)
    max_ratio_drift = mp.mpf(0)
    max_V_drift = mp.mpf(0)
    max_Jdet_drift = mp.mpf(0)
    max_JCP_drift = mp.mpf(0)

    for _ in range(n_trials):
        UL = random_haar_u3_mp(rng)
        URu = random_haar_u3_mp(rng)
        URd = random_haar_u3_mp(rng)
        for U in (UL, URu, URd):
            diff_I = U.H * U - mp.eye(3)
            uerr = mp.sqrt(sum(abs(diff_I[r, c]) ** 2 for r in range(3) for c in range(3)))
            if uerr > max_unitarity_err:
                max_unitarity_err = uerr
        Yu_t = UL * Yu_h * URu.H
        Yd_t = UL * Yd_h * URd.H
        obs = extract_cp_observables_mp(Yu_t, Yd_t)
        for k in range(2):
            max_ratio_drift = max(max_ratio_drift, abs(obs["ru"][k] - base["ru"][k]), abs(obs["rd"][k] - base["rd"][k]))
        for r in range(3):
            for c in range(3):
                max_V_drift = max(max_V_drift, abs(obs["V_abs"][r][c] - base["V_abs"][r][c]))
        max_Jdet_drift = max(max_Jdet_drift, abs(obs["J_det_norm"] - base["J_det_norm"]))
        max_JCP_drift = max(max_JCP_drift, abs(obs["J_CP"] - base["J_CP"]))

    mp.mp.dps = old_dps
    max_all = max(max_ratio_drift, max_V_drift, max_Jdet_drift, max_JCP_drift)
    return {
        "n_trials": n_trials,
        "mpmath_dps": dps_haar,
        "max_haar_unitarity_err": mp.nstr(max_unitarity_err, 6),
        "max_ratio_drift": mp.nstr(max_ratio_drift, 6),
        "max_V_abs_drift": mp.nstr(max_V_drift, 6),
        "max_J_det_norm_drift": mp.nstr(max_Jdet_drift, 6),
        "max_J_CP_drift": mp.nstr(max_JCP_drift, 6),
        "max_overall_drift": mp.nstr(max_all, 6),
        "pass": (max_unitarity_err < mp.mpf(10) ** (-40) and max_all < mp.mpf(10) ** (-12)),
    }


def run_task_ow2_d():
    mp.mp.dps = 70
    ec_list, C_ten = build_fu2_coupling_tensor()
    l2_cache = {}

    # Independent verification of our GL6 L_2(tau) solver:
    # Check asymptotic L_2(5i) vs pi + ln(pi) - 3*ln(2) and S-law on tau = 1/3 + 3/2 i
    tau_s_test = mp.mpc(1, 0) / 3 + mp.mpc(0, 3) / 2
    L2_t1, b_t1, _, _ = solve_L2_any_gl6(tau_s_test, l2_cache)
    # Solve -1/tau_s_test directly WITHOUT reduction via S-inversion on a fresh call to test S-law!
    # Wait: -1/tau_s_test has Im = 0.635 < sqrt(3)/2; reduce_to_F1 applies S once back to tau_s_test,
    # so instead test S-law by evaluating directly at S(1/2 + i) = (-2 + 4i)/5? No, test directly at
    # tau_a = 1/5 + i (|tau_a| = sqrt(26)/5 > 1) and tau_b = -1/tau_a = (-5 + 25i)/26 -> solve tau_b directly!
    tau_S_a = mp.mpc(1, 0) / 5 + mp.mpc(0, 1)
    res_Sa = solve_L2_F1_gl6(tau_S_a)
    res_Sb = solve_L2_F1_gl6(-1 / tau_S_a)
    L2_S_law_err = abs(res_Sb["L2"] - (res_Sa["L2"] + mp.log(abs(tau_S_a))))

    tau_p = mp.mpc(2, 1) / 5
    tau_m = mp.mpc(-2, 1) / 5
    multiples = [1, 5, 8, 15, 24, 25]
    results_m = {}
    stored_Y = {}
    max_mirror_L2_err = mp.mpf(0)
    max_mirror_Jdet_err = mp.mpf(0)
    max_mirror_JCP_err = mp.mpf(0)
    max_ode_wchk = mp.mpf(0)

    for m in multiples:
        tp = m * tau_p
        tm = m * tau_m
        L2p, base_p, _, _ = solve_L2_any_gl6(tp, l2_cache)
        L2m, base_m, _, _ = solve_L2_any_gl6(tm, l2_cache)
        max_ode_wchk = max(max_ode_wchk, base_p["w_check"], base_m["w_check"])
        dL2 = abs(L2p - L2m)
        if dL2 > max_mirror_L2_err:
            max_mirror_L2_err = dL2

        c3_p, den_p = compute_c3_and_denom_mp(tp)
        Yu_p = eval_gate_fu2_24pt_sector(tp, L2p, 1, -4, ec_list, C_ten, c3_p, den_p)
        Yd_p = eval_gate_fu2_24pt_sector(tp, L2p, 1, 2, ec_list, C_ten, c3_p, den_p)
        obs_p = extract_cp_observables_mp(Yu_p, Yd_p)

        c3_m, den_m = compute_c3_and_denom_mp(tm)
        Yu_m = eval_gate_fu2_24pt_sector(tm, L2m, 1, -4, ec_list, C_ten, c3_m, den_m)
        Yd_m = eval_gate_fu2_24pt_sector(tm, L2m, 1, 2, ec_list, C_ten, c3_m, den_m)
        obs_m = extract_cp_observables_mp(Yu_m, Yd_m)

        if m in (8, 24):
            stored_Y[m] = (Yu_p, Yd_p)

        d_Jdet = abs(obs_p["J_det_norm"] + obs_m["J_det_norm"])
        d_JCP = abs(obs_p["J_CP"] + obs_m["J_CP"])
        max_mirror_Jdet_err = max(max_mirror_Jdet_err, d_Jdet)
        max_mirror_JCP_err = max(max_mirror_JCP_err, d_JCP)

        results_m[str(m)] = {
            "m": m,
            "tau_plus": f"({2 * m} + {m}i)/5",
            "Re_tau_plus": mp.nstr(mp.re(tp), 10),
            "Im_tau_plus": mp.nstr(mp.im(tp), 10),
            "L2_plus": mp.nstr(L2p, 40),
            "L2_minus": mp.nstr(L2m, 40),
            "L2_mirror_diff": mp.nstr(dL2, 6),
            "L2_ode_w_check": mp.nstr(max(base_p["w_check"], base_m["w_check"]), 6),
            "L2_ode_im_mBh": mp.nstr(max(base_p["im_mBh_err"], base_m["im_mBh_err"]), 6),
            "is_degenerate": obs_p["is_degenerate"],
            "su_ratios": [mp.nstr(x, 25) for x in obs_p["ru"]],
            "sd_ratios": [mp.nstr(x, 25) for x in obs_p["rd"]],
            "V_abs": [[mp.nstr(obs_p["V_abs"][r][c], 20) for c in range(3)] for r in range(3)],
            "J_det_norm_plus": mp.nstr(obs_p["J_det_norm"], 35),
            "J_det_norm_minus": mp.nstr(obs_m["J_det_norm"], 35),
            "J_det_mirror_sum_err": mp.nstr(d_Jdet, 6),
            "J_CP_plus": mp.nstr(obs_p["J_CP"], 35),
            "J_CP_minus": mp.nstr(obs_m["J_CP"], 35),
            "J_CP_mirror_sum_err": mp.nstr(d_JCP, 6),
            "J_CP_det_identity_err": mp.nstr(obs_p["J_CP_identity_err"], 6),
            "J_det_re_err": mp.nstr(obs_p["J_det_re_err"], 6),
        }

    # Pure-imaginary control tau = 5i
    tau_5i = mp.mpc(0, 5)
    L2_5i, base_5i, _, _ = solve_L2_any_gl6(tau_5i, l2_cache)
    c3_5i, den_5i = compute_c3_and_denom_mp(tau_5i)
    Yu_5i = eval_gate_fu2_24pt_sector(tau_5i, L2_5i, 1, -4, ec_list, C_ten, c3_5i, den_5i)
    Yd_5i = eval_gate_fu2_24pt_sector(tau_5i, L2_5i, 1, 2, ec_list, C_ten, c3_5i, den_5i)
    obs_5i = extract_cp_observables_mp(Yu_5i, Yd_5i)
    asymp_L2 = mp.pi + mp.log(mp.pi) - 3 * mp.log(2)

    ctrl_5i = {
        "tau": "5i",
        "L2": mp.nstr(L2_5i, 40),
        "L2_infty_asymptotic": mp.nstr(asymp_L2, 40),
        "L2_5i_minus_asymptotic": mp.nstr(L2_5i - asymp_L2, 15),
        "L2_ode_w_check": mp.nstr(base_5i["w_check"], 6),
        "su_ratios": [mp.nstr(x, 25) for x in obs_5i["ru"]],
        "sd_ratios": [mp.nstr(x, 25) for x in obs_5i["rd"]],
        "J_det_norm": mp.nstr(obs_5i["J_det_norm"], 35),
        "J_CP": mp.nstr(obs_5i["J_CP"], 35),
    }

    # Mandatory Guardrail 3: 10-trial random Haar unitary basis-scrambling in 50-digit mpmath at m=8 and m=24
    haar_8 = run_haar_scrambling_mp(stored_Y[8][0], stored_Y[8][1], seed=2026112008, n_trials=10, dps_haar=50)
    haar_24 = run_haar_scrambling_mp(stored_Y[24][0], stored_Y[24][1], seed=2026112024, n_trials=10, dps_haar=50)

    tol_50 = mp.mpf(10) ** (-50)
    m1_zero = abs(mp.mpf(results_m["1"]["J_det_norm_plus"])) < tol_50
    m5_zero = abs(mp.mpf(results_m["5"]["J_det_norm_plus"])) < tol_50
    m8_nonzero = abs(mp.mpf(results_m["8"]["J_CP_plus"])) > mp.mpf(10) ** (-35)
    m15_nonzero = abs(mp.mpf(results_m["15"]["J_CP_plus"])) > mp.mpf(10) ** (-35)
    m24_nonzero = abs(mp.mpf(results_m["24"]["J_CP_plus"])) > mp.mpf(10) ** (-35)
    m25_zero = abs(mp.mpf(results_m["25"]["J_det_norm_plus"])) < tol_50
    c5i_zero = abs(obs_5i["J_det_norm"]) < tol_50

    passed = (
        L2_S_law_err < mp.mpf(10) ** (-25)
        and max_ode_wchk < mp.mpf(10) ** (-25)
        and max_mirror_L2_err < tol_50
        and max_mirror_Jdet_err < tol_50
        and max_mirror_JCP_err < tol_50
        and m1_zero
        and m5_zero
        and m8_nonzero
        and m15_nonzero
        and m24_nonzero
        and m25_zero
        and c5i_zero
        and haar_8["pass"]
        and haar_24["pass"]
    )
    return {
        "L2_solver_method": "independent_3stage_GL6_order20_extrapolation_plus_Frobenius_matching",
        "L2_S_transformation_law_err": mp.nstr(L2_S_law_err, 6),
        "max_L2_ode_wronskian_err": mp.nstr(max_ode_wchk, 6),
        "max_mirror_L2_err": mp.nstr(max_mirror_L2_err, 6),
        "max_mirror_J_det_norm_err": mp.nstr(max_mirror_Jdet_err, 6),
        "max_mirror_J_CP_err": mp.nstr(max_mirror_JCP_err, 6),
        "multiples": results_m,
        "pure_imaginary_control_5i": ctrl_5i,
        "m25_J_det_is_zero": m25_zero,
        "haar_scrambling_m8": haar_8,
        "haar_scrambling_m24": haar_24,
        "pass": passed,
    }, stored_Y[8]


# =============================================================================
# TASK OW2-E: FOUR PLANTED FAULTS (PF-OW2-1 THROUGH PF-OW2-4)
# =============================================================================

def run_task_ow2_e(Yu_m8, Yd_m8):
    mp.mp.dps = 65
    # PF-OW2-1: Bosonic sign flip -V_5(tau) has Delta_hyp = -pi < 0 and diverges to -infty as y -> infty
    tau_t = mp.mpc(1, 0) / 7 + mp.mpc(0, 6) / 5
    info_t = V_N_full_mp(tau_t, 5)
    bos_lap = -info_t["lap_hyp"]
    ys = [1, 2, 4, 8, 16]
    bos_vals = [-V_N_full_mp(mp.mpc(0, yv), 5)["val"] for yv in ys]
    monotone_down = all(bos_vals[i + 1] < bos_vals[i] for i in range(len(ys) - 1))
    pf1_caught = (bos_lap < 0 and abs(bos_lap + mp.pi) < mp.mpf(10) ** (-50) and monotone_down and bos_vals[-1] < -50)

    # PF-OW2-2: Mirror-line stationary point tau = i / sqrt(5) on X_0(5) is a saddle (det H < 0)
    tau_sad = mp.mpc(0, 1) / mp.sqrt(5)
    info_sad = V_N_full_mp(tau_sad, 5)
    info_min5 = V_N_full_mp(mp.mpc(2, 1) / 5, 5)
    pf2_caught = (
        info_sad["grad_norm"] < mp.mpf(10) ** (-50)
        and info_sad["det_H"] < 0
        and info_sad["lambda_min"] < 0
        and info_sad["lambda_max"] > 0
        and info_sad["val"] > info_min5["val"]
    )

    # PF-OW2-3: Target-injected potential V_cheat(tau) = |tau - (2+i)/5|^2 fails Gamma_0(5) invariance
    tau_star = mp.mpc(2, 1) / 5
    def V_cheat(t):
        return abs(t - tau_star) ** 2
    t_chk = mp.mpc(3, 0) / 11 + mp.mpc(0, 4) / 7
    drift_T = abs(V_cheat(t_chk + 1) - V_cheat(t_chk))
    drift_g5 = abs(V_cheat(t_chk / (5 * t_chk + 1)) - V_cheat(t_chk))
    pf3_caught = (drift_T > mp.mpf(1) / 10 and drift_g5 > mp.mpf(1) / 10)

    # PF-OW2-4: Unphysical single-matrix left-right overlap V_u^H U_u fails 10-trial Haar scrambling
    mp.mp.dps = 50
    Yu_h = mp.matrix([[mp.mpc(Yu_m8[r, c]) for c in range(3)] for r in range(3)])

    def lr_overlap_abs(Y):
        ev_L, UL_r = mp.eighe(Y * Y.H)
        ev_R, VR_r = mp.eighe(Y.H * Y)
        iL = sorted(range(3), key=lambda i: mp.re(ev_L[i]), reverse=True)
        iR = sorted(range(3), key=lambda i: mp.re(ev_R[i]), reverse=True)
        UL = mp.matrix([[UL_r[r, iL[c]] for c in range(3)] for r in range(3)])
        VR = mp.matrix([[VR_r[r, iR[c]] for c in range(3)] for r in range(3)])
        O = VR.H * UL
        return [[abs(O[r, c]) for c in range(3)] for r in range(3)]

    base_O = lr_overlap_abs(Yu_h)
    rng = random.Random(2026112099)
    max_lr_drift = mp.mpf(0)
    for _ in range(10):
        UL = random_haar_u3_mp(rng)
        UR = random_haar_u3_mp(rng)
        Yt = UL * Yu_h * UR.H
        Ot = lr_overlap_abs(Yt)
        for r in range(3):
            for c in range(3):
                d = abs(Ot[r][c] - base_O[r][c])
                if d > max_lr_drift:
                    max_lr_drift = d
    pf4_caught = (max_lr_drift > mp.mpf(1) / 10)

    return {
        "PF_OW2_1_bosonic_sign_flip": {
            "bosonic_hyperbolic_laplacian": mp.nstr(bos_lap, 20),
            "bosonic_values_at_iy": [mp.nstr(v, 15) for v in bos_vals],
            "monotone_runaway_to_minus_infty": monotone_down,
            "caught": pf1_caught,
        },
        "PF_OW2_2_mirror_saddle_i_over_sqrt5": {
            "grad_norm": mp.nstr(info_sad["grad_norm"], 6),
            "V_saddle": mp.nstr(info_sad["val"], 25),
            "V_min5": mp.nstr(info_min5["val"], 25),
            "lambda_min_H": mp.nstr(info_sad["lambda_min"], 20),
            "lambda_max_H": mp.nstr(info_sad["lambda_max"], 20),
            "det_H": mp.nstr(info_sad["det_H"], 20),
            "caught": pf2_caught,
        },
        "PF_OW2_3_target_injected_potential": {
            "drift_under_T": mp.nstr(drift_T, 15),
            "drift_under_gamma5": mp.nstr(drift_g5, 15),
            "caught": pf3_caught,
        },
        "PF_OW2_4_unphysical_LR_overlap_haar": {
            "max_drift_10_trials": mp.nstr(max_lr_drift, 15),
            "caught": pf4_caught,
        },
        "all_4_caught": (pf1_caught and pf2_caught and pf3_caught and pf4_caught),
        "pass": (pf1_caught and pf2_caught and pf3_caught and pf4_caught),
    }


# =============================================================================
# MAIN DRIVER
# =============================================================================

def main():
    t_start = time.time()
    script_path = os.path.abspath(__file__)
    out_path = os.path.join(os.path.dirname(script_path), "referee_a2_ow2_out.json")

    sec0 = audit_script_hygiene(script_path)
    t0 = time.time()
    secA = run_task_ow2_a()
    tA = time.time()
    secB = run_task_ow2_b()
    tB = time.time()
    secC = run_task_ow2_c(secB)
    tC = time.time()
    secD, (Yu_8, Yd_8) = run_task_ow2_d()
    tD = time.time()
    secE = run_task_ow2_e(Yu_8, Yd_8)
    tE = time.time()

    all_pass = (
        sec0["hygiene_pass"]
        and secA["pass"]
        and secB["pass"]
        and secC["pass"]
        and secD["pass"]
        and secE["pass"]
    )
    payload = {
        "card": "AGY-002_A2-OW2",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_firewall": "0 of 19",
        "section_0_custody_and_hygiene": sec0,
        "task_OW2_A": secA,
        "task_OW2_B": secB,
        "task_OW2_C": secC,
        "task_OW2_D": secD,
        "task_OW2_E": secE,
        "timings_seconds": {
            "OW2_A": round(tA - t0, 3),
            "OW2_B": round(tB - tA, 3),
            "OW2_C": round(tC - tB, 3),
            "OW2_D": round(tD - tC, 3),
            "OW2_E": round(tE - tD, 3),
            "total": round(tE - t_start, 3),
        },
        "overall_pass": all_pass,
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
    print("WROTE:", out_path)
    print("OVERALL_PASS:", all_pass)
    print("TIMINGS:", payload["timings_seconds"])


if __name__ == "__main__":
    main()
