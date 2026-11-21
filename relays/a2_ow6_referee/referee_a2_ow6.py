r"""
Independent Cold-Room Zero-Trust Referee for Card AGY-002_A2-OW6 (and Erratum 1).

Hard Wall 1 Complete Verdict:
  - OW6-A: Analytic X_0(N) Im(tau) <= 1 ceiling theorem via Euler-pentagonal
           Dedekind eta, Eisenstein E_2 derivative cross-checked against 4-pt
           central differences, strict convexity d^2V_1/dy^2(iy) > 0, exact
           cosine inequality, and S-dual massive 4D KK Casimir V_4D(iy; M)
           via exact Chowla-Selberg / Poisson-resummed Bessel K_2 (and K_3)
           cross-checked against direct 2D dual lattice sums.
  - OW6-B: Twisted E[5] isogeny-kernel 1-loop potential via mpmath.jtheta(1),
           exact S-duality and Gamma_0(5) invariance, exact rational Raabe
           multiplication theorem (Erratum 1: -36 for 2H and 1H, +12 for
           fermions-only, verified numerically at y = 12 and y = 5), exact
           Fricke cancellation of charged fields, and fermions-only orbifold
           lock back to tau_*^{+-} = (+-2 + i)/5.
  - OW6-C: Covering-torus lift m in {8, 24, 40} via disjoint GL6 order-20
           extrapolated Fuchsian L_2(tau) solver and disjoint branch-cut-free
           mpmath.jtheta Yukawa evaluator with exact mod-Z^2-reduced centered
           torsion coordinates: E[5] exact e = d degeneracy, open-weave
           E[5] + E[6] Regime-4b zero-parameter splitting, 10-trial 45-dps
           Haar basis-scrambling gate across (Y_u, Y_d, Y_e), and exact
           Hierarchy-vs-CKM/CP trade-off certification.
  - OW6-D: 4/4 planted faults including Erratum 1 (PF-OW6-1..4).

Hygiene:
  - 0 of 19 empirical / PDG numbers.
  - 0 float or complex AST literals.
  - 0 frontier/ imports.
  - 0 hardcoded truth flags.
  - Cold-room built strictly from Card A2-OW6 + Erratum 1.
"""

import ast
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
                if "frontier" in alias.name or "a2_ow6" in alias.name or "verify_a2" in alias.name:
                    bad_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "frontier" in mod or "a2_ow6" in mod or "verify_a2" in mod:
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
        "hygiene_pass": (len(bad_literals) == 0 and len(bad_imports) == 0),
    }


# =============================================================================
# CORE MODULAR FUNCTIONS (EULER PENTAGONAL, EISENSTEIN, SL(2, Z) REDUCTION)
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
    """Reduce z in H to standard fundamental domain F_1; return (z_red, gamma)."""
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


def eta_pentagonal_direct_mp(tau):
    """Dedekind eta(tau) directly from Euler's pentagonal number theorem."""
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


def V1_pentagonal_mp(tau):
    """V_1(tau) = -ln(Im(tau) |eta(tau)|^4) via SL(2, Z) invariance + pentagonal eta."""
    tau_red, _ = reduce_to_F1_mp(tau)
    et = eta_pentagonal_direct_mp(tau_red)
    return -mp.log(mp.im(tau_red) * (abs(et) ** 4))


def V1_direct_no_reduce_mp(tau):
    """Direct V_1(tau) = -ln(Im(tau) |eta(tau)|^4) without SL(2,Z) reduction (for y >= 1/5)."""
    et = eta_pentagonal_direct_mp(tau)
    return -mp.log(mp.im(tau) * (abs(et) ** 4))


def eisenstein_e2_e4_e6_mp(tau):
    """Eisenstein series E_2(tau), E_4(tau), E_6(tau) directly from Lambert series."""
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


def dV1_dy_e2_mp(tau):
    """Exact analytic dV_1/dy(tau) = (pi/3) Re(E_2(tau)) - 1/Im(tau)."""
    e2, _, _ = eisenstein_e2_e4_e6_mp(tau)
    return (mp.pi / 3) * mp.re(e2) - 1 / mp.im(tau)


def fd4_1st_real(fn, x0, h):
    """4th-order central finite difference for first derivative of real function."""
    return (-fn(x0 + 2 * h) + 8 * fn(x0 + h) - 8 * fn(x0 - h) + fn(x0 - 2 * h)) / (12 * h)


def fd4_2nd_real(fn, x0, h):
    """4th-order central finite difference for second derivative of real function."""
    return (
        -fn(x0 + 2 * h) + 16 * fn(x0 + h) - 30 * fn(x0) + 16 * fn(x0 - h) - fn(x0 - 2 * h)
    ) / (12 * h * h)


# =============================================================================
# TASK OW6-A: ANALYTIC X_0(N) Im(tau) <= 1 CEILING & 4D MASSIVE KK CASIMIR
# =============================================================================

def besselk_half_int(nu_int, z):
    """Exact closed-form K_{nu_int - 1/2}(z) for nu_int in {2, 3}."""
    pref = mp.sqrt(mp.pi / (2 * z)) * mp.exp(-z)
    inv_z = 1 / z
    if nu_int == 2:
        # K_{3/2}(z) = sqrt(pi/(2z)) * exp(-z) * (1 + 1/z)
        return pref * (1 + inv_z)
    if nu_int == 3:
        # K_{5/2}(z) = sqrt(pi/(2z)) * exp(-z) * (1 + 3/z + 3/z^2)
        return pref * (1 + 3 * inv_z + 3 * inv_z * inv_z)
    return mp.besselk(mp.mpf(nu_int) - mp.mpf(1) / 2, z)


def V_kk_chowla_selberg_mp(y, M, nu=2):
    """
    S-dual massive KK Casimir potential (confining sign, normalized as
    M^nu * sum_{(w1,w2)!=(0,0)} K_nu(M * L_{w1,w2}) / L_{w1,w2}^nu)
    computed via exact 1D-Poisson-resummed Chowla-Selberg expansion.
    """
    tol = mp.mpf(10) ** (-mp.mp.dps + 4)
    sy = mp.sqrt(y)
    M_nu = M ** nu
    # w2 = 0, w1 != 0 piece (1D Bessel K_nu sum)
    s1 = mp.mpf(0)
    w1 = 1
    while True:
        L = mp.mpf(w1) / sy
        term = 2 * M_nu * mp.besselk(nu, M * L) / (L ** nu)
        s1 += term
        if term < tol and w1 > 5:
            break
        w1 += 1

    # w2 != 0 piece (1D Poisson-resummed in w1 -> exact elementary K_{nu - 1/2})
    s2 = mp.mpf(0)
    p = mp.mpf(2 * nu - 1) / 4
    pref = 2 * mp.sqrt(2 * mp.pi * y)
    four_pi2_y = 4 * (mp.pi ** 2) * y
    M2 = M * M
    w2 = 1
    while True:
        w2_2_y = (w2 * w2) * y
        arg0 = w2 * mp.sqrt(y * M2)
        row = pref * ((M2 / w2_2_y) ** p) * besselk_half_int(nu, arg0)
        n1 = 1
        while True:
            An = M2 + four_pi2_y * (n1 * n1)
            argn = w2 * mp.sqrt(y * An)
            tn = 2 * pref * ((An / w2_2_y) ** p) * besselk_half_int(nu, argn)
            row += tn
            if tn < tol:
                break
            n1 += 1
        s2 += row
        if row < tol and w2 > 3:
            break
        w2 += 1
    return s1 + s2


def V_kk_2d_dual_lattice_mp(y, M, nu=2, R_max=30):
    """Direct 2D Poisson-resummed Bessel K_nu dual lattice sum for cross-check."""
    s = mp.mpf(0)
    M_nu = M ** nu
    for w1 in range(-R_max, R_max + 1):
        w1_sq_div_y = mp.mpf(w1 * w1) / y
        for w2 in range(-R_max, R_max + 1):
            if w1 == 0 and w2 == 0:
                continue
            L2 = w1_sq_div_y + mp.mpf(w2 * w2) * y
            L = mp.sqrt(L2)
            s += mp.besselk(nu, M * L) / (L ** nu)
    return M_nu * s


def run_task_ow6_a():
    mp.mp.dps = 60
    im = mp.mpc(0, 1)
    h_fd = mp.mpf(10) ** (-10)

    # 1. Cross-check Euler-pentagonal V_1 S-duality & E_2 analytic dV_1/dy vs 4-pt FD
    s_dual_ys = [Fraction(11, 10), Fraction(3, 2), Fraction(2, 1), Fraction(5, 1)]
    max_s_dual_err = mp.mpf(0)
    for yf in s_dual_ys:
        yv = mp.mpf(yf.numerator) / yf.denominator
        err = abs(V1_direct_no_reduce_mp(im * yv) - V1_direct_no_reduce_mp(im / yv))
        if err > max_s_dual_err:
            max_s_dual_err = err

    ys_grid = [Fraction(1, 1), Fraction(11, 10), Fraction(3, 2), Fraction(2, 1), Fraction(5, 1)]
    xs_grid = [
        Fraction(0, 1), Fraction(1, 7), Fraction(1, 4), Fraction(1, 3),
        Fraction(1, 2), Fraction(2, 3), Fraction(5, 6),
    ]
    max_e2_vs_fd_err = mp.mpf(0)
    for yf in ys_grid:
        yv = mp.mpf(yf.numerator) / yf.denominator
        for xf in xs_grid:
            xv = mp.mpf(xf.numerator) / xf.denominator
            dv_e2 = dV1_dy_e2_mp(xv + im * yv)
            dv_fd = fd4_1st_real(lambda yy: V1_direct_no_reduce_mp(xv + im * yy), yv, h_fd)
            err = abs(dv_e2 - dv_fd)
            if err > max_e2_vs_fd_err:
                max_e2_vs_fd_err = err

    # 2. Exact S-duality stationarity at tau = i
    dV1_dy_at_i_e2 = dV1_dy_e2_mp(im)
    dV1_dy_at_i_fd = fd4_1st_real(lambda yy: V1_direct_no_reduce_mp(im * yy), mp.mpf(1), h_fd)

    # 3. Strict convexity d^2 V_1 / dy^2(i y) > 0 for all y > 0
    convex_ys = [
        Fraction(1, 5), Fraction(1, 2), Fraction(1, 1),
        Fraction(11, 10), Fraction(3, 2), Fraction(2, 1), Fraction(5, 1),
    ]
    convex_records = []
    max_d2_series_vs_ram_err = mp.mpf(0)
    max_d2_series_vs_fd_err = mp.mpf(0)
    all_convex_pos = True
    tol_ser = mp.mpf(10) ** (-mp.mp.dps - 8)
    for yf in convex_ys:
        yv = mp.mpf(yf.numerator) / yf.denominator
        r = mp.exp(-2 * mp.pi * yv)
        ser = mp.mpf(0)
        n = 1
        rn = r
        while True:
            t = (n * n) * rn / ((1 - rn) ** 2)
            ser += t
            if t < tol_ser:
                break
            n += 1
            rn *= r
        d2_series = 1 / (yv * yv) + 16 * (mp.pi ** 2) * ser
        e2, e4, _ = eisenstein_e2_e4_e6_mp(im * yv)
        d2_ramanujan = 1 / (yv * yv) + (mp.pi ** 2 / 18) * mp.re(e4 - e2 * e2)
        d2_fd = fd4_2nd_real(lambda yy: V1_direct_no_reduce_mp(im * yy), yv, mp.mpf(10) ** (-8))
        err_ram = abs(d2_series - d2_ramanujan)
        err_fd = abs(d2_series - d2_fd)
        max_d2_series_vs_ram_err = max(max_d2_series_vs_ram_err, err_ram)
        max_d2_series_vs_fd_err = max(max_d2_series_vs_fd_err, err_fd)
        if not (d2_series > 0 and d2_ramanujan > 0 and d2_fd > 0):
            all_convex_pos = False
        convex_records.append({
            "y": f"{yf.numerator}/{yf.denominator}" if yf.denominator != 1 else str(yf.numerator),
            "d2V1_dy2_series": mp.nstr(d2_series, 30),
            "err_vs_ramanujan": mp.nstr(err_ram, 6),
            "err_vs_fd4": mp.nstr(err_fd, 6),
            "strictly_positive": bool(d2_series > 0),
        })

    # 4. Exact cosine inequality min_x dV_1/dy(x, y) == dV_1/dy(0, y) > 0 for y > 1
    #    and explicit X_0(N) positive-sum corollary check
    cos_ys = [Fraction(11, 10), Fraction(3, 2), Fraction(2, 1), Fraction(5, 1)]
    cos_records = []
    all_cos_ok = True
    max_divsum_err = mp.mpf(0)

    def sigma1(k):
        tot = 0
        d = 1
        while d * d <= k:
            if k % d == 0:
                tot += d
                if d * d != k:
                    tot += k // d
            d += 1
        return tot

    sigma_tbl = [0] + [sigma1(k) for k in range(1, 65)]
    for yf in cos_ys:
        yv = mp.mpf(yf.numerator) / yf.denominator
        base_d = dV1_dy_e2_mp(im * yv)
        min_excess = mp.mpf(10) ** 9
        r = mp.exp(-2 * mp.pi * yv)
        for num in range(1, 24):
            xv = mp.mpf(num) / 24
            dx = dV1_dy_e2_mp(xv + im * yv)
            excess = dx - base_d
            if excess < min_excess:
                min_excess = excess
            # Direct divisor-sum excess: 8 pi sum_{k>=1} sigma_1(k) r^k (1 - cos(2 pi k x))
            ds_sum = mp.mpf(0)
            rk = r
            for k in range(1, 65):
                t = sigma_tbl[k] * rk * (1 - mp.cos(2 * mp.pi * k * xv))
                ds_sum += t
                rk *= r
                if rk < tol_ser:
                    break
            ds_excess = 8 * mp.pi * ds_sum
            max_divsum_err = max(max_divsum_err, abs(excess - ds_excess))
        ok_y = bool(base_d > 0 and min_excess > 0)
        if not ok_y:
            all_cos_ok = False
        cos_records.append({
            "y": f"{yf.numerator}/{yf.denominator}" if yf.denominator != 1 else str(yf.numerator),
            "dV1_dy_at_x0": mp.nstr(base_d, 30),
            "min_excess_over_x_nonzero": mp.nstr(min_excess, 15),
            "strictly_positive_all_x": ok_y,
        })

    # Explicit X_0(N) positive combinations sum c_k V_1(d_k tau) at y > 1
    x0n_combos = [
        ("X0(2)_1_2", [(1, 1), (1, 2)]),
        ("X0(3)_1_3", [(1, 1), (1, 3)]),
        ("X0(5)_1_5", [(1, 1), (1, 5)]),
        ("X0(6)_1_2_3_6", [(1, 1), (2, 2), (3, 3), (1, 6)]),
        ("X0(10)_1_2_5_10", [(1, 1), (1, 2), (1, 5), (1, 10)]),
        ("X0(12)_1_2_3_4_6_12", [(1, 1), (1, 2), (1, 3), (1, 4), (1, 6), (1, 12)]),
    ]
    x0n_min_slope = mp.mpf(10) ** 9
    for _, terms in x0n_combos:
        for yf in [Fraction(11, 10), Fraction(3, 2), Fraction(2, 1)]:
            yv = mp.mpf(yf.numerator) / yf.denominator
            for num in [0, 1, 3, 5, 7]:
                xv = mp.mpf(num) / 11
                sl = sum(mp.mpf(ck) * dk * dV1_dy_e2_mp(dk * (xv + im * yv)) for ck, dk in terms)
                if sl < x0n_min_slope:
                    x0n_min_slope = sl

    # 5. S-dual massive 4D KK Casimir V_4D(i y; M) for M in {1/2, 1, 2, 5}
    #    Primary: nu = 2 (Bessel K_2); Cross-check: nu = 3 (Bessel K_3)
    #    plus direct 2D dual lattice sum cross-check at M = 5
    masses = [Fraction(1, 2), Fraction(1, 1), Fraction(2, 1), Fraction(5, 1)]
    h_kk = mp.mpf(10) ** (-9)
    kk_k2_records = []
    kk_k3_records = []
    kk_k2_ok = True
    kk_k3_ok = True
    max_kk_sdual_err = mp.mpf(0)

    # Cross-check Chowla-Selberg vs direct 2D dual lattice sum at M = 5, y = 6/5
    y_chk = mp.mpf(6) / 5
    cs_vs_2d_k2_err = abs(
        V_kk_chowla_selberg_mp(y_chk, mp.mpf(5), nu=2)
        - V_kk_2d_dual_lattice_mp(y_chk, mp.mpf(5), nu=2, R_max=32)
    )
    cs_vs_2d_k3_err = abs(
        V_kk_chowla_selberg_mp(y_chk, mp.mpf(5), nu=3)
        - V_kk_2d_dual_lattice_mp(y_chk, mp.mpf(5), nu=3, R_max=32)
    )

    for nu, recs, is_k2 in [(2, kk_k2_records, True), (3, kk_k3_records, False)]:
        for mf in masses:
            Mv = mp.mpf(mf.numerator) / mf.denominator
            fn = lambda yy: V_kk_chowla_selberg_mp(yy, Mv, nu=nu)
            sdual_err = abs(fn(mp.mpf(6) / 5) - fn(mp.mpf(5) / 6))
            max_kk_sdual_err = max(max_kk_sdual_err, sdual_err)
            d_at_1 = fd4_1st_real(fn, mp.mpf(1), h_kk)
            d_at_6_5 = fd4_1st_real(fn, mp.mpf(6) / 5, h_kk)
            d_at_2 = fd4_1st_real(fn, mp.mpf(2), h_kk)
            ok_m = bool(
                abs(d_at_1) < mp.mpf(10) ** (-8)
                and d_at_6_5 > 0
                and d_at_2 > 0
                and sdual_err < mp.mpf(10) ** (-40)
            )
            if is_k2 and not ok_m:
                kk_k2_ok = False
            if (not is_k2) and not ok_m:
                kk_k3_ok = False
            recs.append({
                "M": f"{mf.numerator}/{mf.denominator}" if mf.denominator != 1 else str(mf.numerator),
                "S_duality_err_at_6_5": mp.nstr(sdual_err, 6),
                "dV_dy_at_i": mp.nstr(d_at_1, 6),
                "dV_dy_at_6_5i": mp.nstr(d_at_6_5, 20),
                "dV_dy_at_2i": mp.nstr(d_at_2, 20),
                "pass": ok_m,
            })

    passed = bool(
        max_s_dual_err < mp.mpf(10) ** (-50)
        and max_e2_vs_fd_err < mp.mpf(10) ** (-30)
        and abs(dV1_dy_at_i_e2) < mp.mpf(10) ** (-45)
        and abs(dV1_dy_at_i_fd) < mp.mpf(10) ** (-30)
        and all_convex_pos
        and max_d2_series_vs_ram_err < mp.mpf(10) ** (-45)
        and max_d2_series_vs_fd_err < mp.mpf(10) ** (-20)
        and all_cos_ok
        and max_divsum_err < mp.mpf(10) ** (-45)
        and x0n_min_slope > 0
        and cs_vs_2d_k2_err < mp.mpf(10) ** (-45)
        and cs_vs_2d_k3_err < mp.mpf(10) ** (-45)
        and kk_k2_ok
        and kk_k3_ok
    )
    return {
        "mpmath_dps": 60,
        "V1_S_duality_max_err": mp.nstr(max_s_dual_err, 6),
        "dV1_dy_E2_vs_FD4_max_err": mp.nstr(max_e2_vs_fd_err, 6),
        "dV1_dy_at_i_E2": mp.nstr(dV1_dy_at_i_e2, 6),
        "dV1_dy_at_i_FD4": mp.nstr(dV1_dy_at_i_fd, 6),
        "d2V1_dy2_series_vs_ramanujan_err": mp.nstr(max_d2_series_vs_ram_err, 6),
        "d2V1_dy2_series_vs_FD4_err": mp.nstr(max_d2_series_vs_fd_err, 6),
        "strict_convexity_records": convex_records,
        "cosine_inequality_divisor_sum_err": mp.nstr(max_divsum_err, 6),
        "cosine_inequality_records": cos_records,
        "X0N_positive_combo_min_slope_y_gt_1": mp.nstr(x0n_min_slope, 15),
        "massive_4D_KK_Casimir": {
            "method": "exact_Chowla_Selberg_1D_Poisson_Bessel_K2_and_K3_with_2D_dual_lattice_crosscheck",
            "cs_vs_2d_lattice_err_K2_M5": mp.nstr(cs_vs_2d_k2_err, 6),
            "cs_vs_2d_lattice_err_K3_M5": mp.nstr(cs_vs_2d_k3_err, 6),
            "max_S_duality_err": mp.nstr(max_kk_sdual_err, 6),
            "K2_records": kk_k2_records,
            "K3_crosscheck_records": kk_k3_records,
        },
        "pass": passed,
    }


# =============================================================================
# TASK OW6-B: TWISTED E[5] KERNEL RUNAWAY & FERMIONS-ONLY ORBIFOLD LOCK
# =============================================================================

def B2_exact_fraction(x_frac):
    """Exact second Bernoulli polynomial B_2({x}) = u^2 - u + 1/6 with u = x mod 1 in [0, 1)."""
    u = x_frac % 1
    return u * u - u + Fraction(1, 6)


def V_kronecker_jtheta_direct_mp(a_frac, b_frac, tau):
    """
    Direct (NO SL(2, Z) reduction) Kronecker 2nd-limit potential via mpmath.jtheta(1):
      V_{(a,b)}(tau) = -ln|exp(i pi a^2 tau) * jtheta(1, pi*(a*tau + b), exp(i pi tau)) / eta(tau)|^2.
    Used for strictly non-circular S-duality, Gamma_0(5), and orbifold-lock verification.
    """
    af = a_frac % 1
    bf = b_frac % 1
    if af == 0 and bf == 0:
        return V1_direct_no_reduce_mp(tau)
    im = mp.mpc(0, 1)
    a_v = mp.mpf(af.numerator) / af.denominator
    b_v = mp.mpf(bf.numerator) / bf.denominator
    q_nome = mp.exp(im * mp.pi * tau)
    th1 = mp.jtheta(1, mp.pi * (a_v * tau + b_v), q_nome)
    et = eta_pentagonal_direct_mp(tau)
    val = mp.exp(im * mp.pi * a_v * a_v * tau) * th1 / et
    return -2 * mp.log(abs(val))


def V_kronecker_jtheta_mp(a_frac, b_frac, tau):
    """
    Modular Kronecker 2nd-limit potential V_{(a,b)}(tau) with F_1 reduction for very small Im(tau)
    (e.g. Im(-1/(5*12i)) = 1/60), cross-checked against V_kronecker_jtheta_direct_mp.
    """
    if mp.im(tau) >= mp.mpf(1) / 10:
        return V_kronecker_jtheta_direct_mp(a_frac, b_frac, tau)
    af = a_frac % 1
    bf = b_frac % 1
    if af == 0 and bf == 0:
        return V1_pentagonal_mp(tau)
    im = mp.mpc(0, 1)
    tau_red, g = reduce_to_F1_mp(tau)
    p, q_g, r, s = g
    a_red_f = (s * af - r * bf) % 1
    b_red_f = (-q_g * af + p * bf) % 1
    a_v = mp.mpf(a_red_f.numerator) / a_red_f.denominator
    b_v = mp.mpf(b_red_f.numerator) / b_red_f.denominator
    q_nome = mp.exp(im * mp.pi * tau_red)
    th1 = mp.jtheta(1, mp.pi * (a_v * tau_red + b_v), q_nome)
    et = eta_pentagonal_direct_mp(tau_red)
    val = mp.exp(im * mp.pi * a_v * a_v * tau_red) * th1 / et
    return -2 * mp.log(abs(val))


def V_kronecker_qprod_mp(a_frac, b_frac, tau):
    """Independent q-product evaluation of V_{(a,b)}(tau) (for direct cross-check vs jtheta)."""
    af = a_frac % 1
    bf = b_frac % 1
    if af == 0 and bf == 0:
        return V1_direct_no_reduce_mp(tau)
    im = mp.mpc(0, 1)
    a_v = mp.mpf(af.numerator) / af.denominator
    b_v = mp.mpf(bf.numerator) / bf.denominator
    y = mp.im(tau)
    q2 = mp.exp(2 * mp.pi * im * tau)
    z_exp = mp.exp(2 * mp.pi * im * (a_v * tau + b_v))
    z_inv = 1 / z_exp
    b2 = a_v * a_v - a_v + mp.mpf(1) / 6
    # From Jacobi triple product for theta_1(pi(a*tau+b), e^{i*pi*tau}) / eta(tau):
    # |e^{i*pi*a^2*tau} * th1 / eta|^2 = e^{-2*pi*B_2(a)*y} * |1 - z_exp|^2 * prod_{n>=1} |1 - q2^n z_exp|^2 |1 - q2^n z_inv|^2
    # Wait: check sign of z_exp when a in (0,1): |z_exp| = e^{-2*pi*a*y} < 1, so |1 - z_exp| -> 1!
    # Check a = 0: |1 - e^{2*pi*i*b}|^2 = 4 sin^2(pi*b)! Matches EXACTLY!
    acc = 2 * mp.pi * b2 * y - 2 * mp.log(abs(1 - z_exp))
    tol = mp.mpf(10) ** (-mp.mp.dps - 6)
    qn = q2
    n = 1
    while True:
        t1 = -2 * mp.log(abs(1 - qn * z_exp))
        t2 = -2 * mp.log(abs(1 - qn * z_inv))
        acc += t1 + t2
        if abs(t1) + abs(t2) < tol and n > 5:
            break
        qn *= q2
        n += 1
    return acc


def build_sm_multiplet_table(n_higgs):
    """
    Exact SM 6Y integer charges and signed real d.o.f. (+1 per real chiral fermion,
    -1 per real bosonic d.o.f.): 3 generations of 16 Weyl fermions (96 real),
    12 massless gauge bosons (24 real), and n_higgs complex SU(2) doublets (4*n_higgs real).
    """
    multiplets = [
        ("Q_L", 3 * 6 * 2, 1),       # +36 real, 6Y = +1
        ("u_R_c", 3 * 3 * 2, -4),    # +18 real, 6Y = -4
        ("d_R_c", 3 * 3 * 2, 2),     # +18 real, 6Y = +2
        ("L_L", 3 * 2 * 2, -3),      # +12 real, 6Y = -3
        ("e_R_c", 3 * 1 * 2, 6),     #  +6 real, 6Y = +6
        ("nu_R_c", 3 * 1 * 2, 0),    #  +6 real, 6Y =  0
    ]
    if n_higgs is not None:
        multiplets.append(("gauge_12", -12 * 2, 0))  # -24 real, 6Y = 0
        if n_higgs == 2:
            multiplets.append(("H_u", -4, 3))        # -4 real, 6Y = +3
            multiplets.append(("H_d", -4, -3))       # -4 real, 6Y = -3
        elif n_higgs == 1:
            multiplets.append(("H", -4, 3))          # -4 real, 6Y = +3
    return multiplets


def eval_Vker_explicit_mp(tau, multiplets, per_kernel_point=True):
    """Explicit sum over k in {1, 2, 3, 4} and every SM multiplet (zero algebraic shortcuts)."""
    # Cache distinct V_{(0, r/5)}(tau) values for r in 0..4 at this tau
    v_cache = {r: V_kronecker_jtheta_mp(Fraction(0), Fraction(r, 5), tau) for r in range(5)}
    tot = mp.mpf(0)
    for k in range(1, 5):
        for _, dof, q_charge in multiplets:
            r = (q_charge * k) % 5
            tot += dof * v_cache[r]
    return tot / 4 if per_kernel_point else tot


def eval_Vker_fricke_sym_mp(tau, multiplets, per_kernel_point=True):
    """V_ker(tau) + V_ker(-1 / (5 * tau))."""
    return (
        eval_Vker_explicit_mp(tau, multiplets, per_kernel_point=per_kernel_point)
        + eval_Vker_explicit_mp(-1 / (5 * tau), multiplets, per_kernel_point=per_kernel_point)
    )


def run_task_ow6_b():
    mp.mp.dps = 60
    im = mp.mpc(0, 1)

    # 1. Cross-check jtheta Kronecker formula vs independent infinite q-product
    t_qchk = mp.mpf(3) / 11 + im * mp.mpf(7) / 10
    qprod_errs = []
    for af, bf in [(Fraction(0), Fraction(1, 5)), (Fraction(1, 5), Fraction(0)), (Fraction(2, 5), Fraction(3, 5))]:
        err = abs(V_kronecker_jtheta_mp(af, bf, t_qchk) - V_kronecker_qprod_mp(af, bf, t_qchk))
        qprod_errs.append(err)
    max_qprod_err = max(qprod_errs)

    # 2. Exact S-duality: |V_{(0, 1/5)}(-1/tau) - V_{(1/5, 0)}(tau)| < 10^-35 (strictly direct, no SL(2,Z) reduction)
    s_test_pts = [
        mp.mpf(3) / 11 + im * mp.mpf(7) / 10,
        mp.mpf(-3) / 14 + im * mp.mpf(3) / 10,
        mp.mpf(-1) / 5 + im * mp.mpf(2) / 5,
    ]
    max_s_dual_err = mp.mpf(0)
    for t in s_test_pts:
        err = abs(
            V_kronecker_jtheta_direct_mp(Fraction(0), Fraction(1, 5), -1 / t)
            - V_kronecker_jtheta_direct_mp(Fraction(1, 5), Fraction(0), t)
        )
        if err > max_s_dual_err:
            max_s_dual_err = err

    # 3. Exact Gamma_0(5) invariance & Fricke charged-field cancellation identity
    m_2H = build_sm_multiplet_table(2)
    m_1H = build_sm_multiplet_table(1)
    m_F = build_sm_multiplet_table(None)

    max_gamma05_err = mp.mpf(0)
    max_T_err = mp.mpf(0)
    max_fricke_const_err = mp.mpf(0)
    for t in s_test_pts:
        g5_t = t / (5 * t + 1)
        for mults in (m_2H, m_1H, m_F):
            err_g5 = abs(eval_Vker_explicit_mp(g5_t, mults) - eval_Vker_explicit_mp(t, mults))
            err_T = abs(eval_Vker_explicit_mp(t + 1, mults) - eval_Vker_explicit_mp(t, mults))
            max_gamma05_err = max(max_gamma05_err, err_g5)
            max_T_err = max(max_T_err, err_T)
        # Verify exact Fricke identity: sum_{k=1}^4 (V_{(0,k/5)}(t) + V_{(0,k/5)}(-1/(5t))) == -2 ln 5
        s_charged = sum(
            V_kronecker_jtheta_mp(Fraction(0), Fraction(k, 5), t)
            + V_kronecker_jtheta_mp(Fraction(0), Fraction(k, 5), -1 / (5 * t))
            for k in range(1, 5)
        )
        max_fricke_const_err = max(max_fricke_const_err, abs(s_charged + 2 * mp.log(5)))

    # 4. Exact rational Raabe multiplication identity (Erratum 1)
    raabe_target = Fraction(-4, 5) * B2_exact_fraction(Fraction(0))
    raabe_checks = {}
    raabe_all_exact = True
    for q_val in (1, 2, 3, 4):
        lhs = sum(B2_exact_fraction(Fraction(q_val * k, 5)) for k in range(1, 5))
        eq = (lhs == raabe_target)
        if not eq:
            raabe_all_exact = False
        raabe_checks[str(q_val)] = {
            "sum_B2": f"{lhs.numerator}/{lhs.denominator}",
            "target_minus_4_5_B2_0": f"{raabe_target.numerator}/{raabe_target.denominator}",
            "exact_match": eq,
        }

    # Exact rational cusp slopes summed explicitly over all multiplets and k = 1..4
    def exact_cusp_slope_fraction(multiplets):
        total = Fraction(0)
        for k in range(1, 5):
            for _, dof, q_charge in multiplets:
                # Per kernel point: V_{(0, qk/5)}(iy) ~ 2*B_2(0)*pi*y
                # Fricke dual: V_{(0, qk/5)}(-1/(5*iy)) = V_{(qk/5, 0)}(5*iy) ~ 5 * 2*B_2(qk/5)*pi*y
                s_term = 2 * B2_exact_fraction(Fraction(0)) + 10 * B2_exact_fraction(Fraction(q_charge * k, 5))
                total += dof * s_term
        return total / 4

    slope_2H_exact = exact_cusp_slope_fraction(m_2H)
    slope_1H_exact = exact_cusp_slope_fraction(m_1H)
    slope_F_exact = exact_cusp_slope_fraction(m_F)

    # 5. Numerical asymptotic slope verification at y = 12 (and y = 5)
    #    Model-independent log-eliminating operator: (f'(y) + y f''(y)) / pi
    #    and explicit log-subtracted operator: (f'(y) + 2 * n_neut / y) / pi
    h_sl = mp.mpf(10) ** (-8)
    slope_num_records = {}
    all_slopes_match_y12 = True
    for label, mults, n_neut, ex_frac in [
        ("SM_2H", m_2H, -18, slope_2H_exact),
        ("SM_1H", m_1H, -18, slope_1H_exact),
        ("fermions_only", m_F, 6, slope_F_exact),
    ]:
        ex_mp = mp.mpf(ex_frac.numerator) / ex_frac.denominator
        rec_y = {}
        for y_int in (5, 12):
            yv = mp.mpf(y_int)
            fn = lambda yy: eval_Vker_fricke_sym_mp(im * yy, mults, per_kernel_point=True)
            fp = fd4_1st_real(fn, yv, h_sl)
            fpp = fd4_2nd_real(fn, yv, h_sl)
            sl_logelim = (fp + yv * fpp) / mp.pi
            sl_logsub = (fp + 2 * mp.mpf(n_neut) / yv) / mp.pi
            sl_raw = fp / mp.pi
            err_logelim = abs(sl_logelim - ex_mp)
            err_logsub = abs(sl_logsub - ex_mp)
            if y_int == 12 and not (err_logelim < mp.mpf(10) ** (-6) and err_logsub < mp.mpf(10) ** (-6)):
                all_slopes_match_y12 = False
            rec_y[f"y_{y_int}"] = {
                "raw_dV_d_pi_y": mp.nstr(sl_raw, 15),
                "log_eliminated_slope": mp.nstr(sl_logelim, 25),
                "log_subtracted_slope": mp.nstr(sl_logsub, 25),
                "err_log_eliminated": mp.nstr(err_logelim, 6),
                "err_log_subtracted": mp.nstr(err_logsub, 6),
            }
        slope_num_records[label] = {
            "exact_rational_slope": f"{ex_frac.numerator}/{ex_frac.denominator}" if ex_frac.denominator != 1 else str(ex_frac.numerator),
            "n_neutral_real_dof": n_neut,
            "numerical": rec_y,
        }

    # Individual twisted component slope V_{(k/5, 0)}(i * 12) vs exact 2 B_2(k/5)
    indiv_k_max_err = mp.mpf(0)
    for k in (1, 2):
        fk = lambda yy: V_kronecker_jtheta_mp(Fraction(k, 5), Fraction(0), im * yy)
        sl_k = fd4_1st_real(fk, mp.mpf(12), h_sl) / mp.pi
        b2_k = 2 * B2_exact_fraction(Fraction(k, 5))
        err_k = abs(sl_k - mp.mpf(b2_k.numerator) / b2_k.denominator)
        if err_k > indiv_k_max_err:
            indiv_k_max_err = err_k

    # 6. Fermions-only 4-pt Fricke-symmetrized orbifold lock at tau_*^{+-} = (+-2 + i)/5
    def grad_hess_4pt(fn, t_pt, h_step):
        f0 = fn(t_pt)
        fxp1 = fn(t_pt + h_step)
        fxm1 = fn(t_pt - h_step)
        fxp2 = fn(t_pt + 2 * h_step)
        fxm2 = fn(t_pt - 2 * h_step)
        fyp1 = fn(t_pt + im * h_step)
        fym1 = fn(t_pt - im * h_step)
        fyp2 = fn(t_pt + 2 * im * h_step)
        fym2 = fn(t_pt - 2 * im * h_step)
        gx = (-fxp2 + 8 * fxp1 - 8 * fxm1 + fxm2) / (12 * h_step)
        gy = (-fyp2 + 8 * fyp1 - 8 * fym1 + fym2) / (12 * h_step)
        hxx = (-fxp2 + 16 * fxp1 - 30 * f0 + 16 * fxm1 - fxm2) / (12 * h_step * h_step)
        hyy = (-fyp2 + 16 * fyp1 - 30 * f0 + 16 * fym1 - fym2) / (12 * h_step * h_step)
        hxy = (
            fn(t_pt + h_step + im * h_step)
            - fn(t_pt + h_step - im * h_step)
            - fn(t_pt - h_step + im * h_step)
            + fn(t_pt - h_step - im * h_step)
        ) / (4 * h_step * h_step)
        tr = hxx + hyy
        diff = hxx - hyy
        rad = mp.sqrt(diff * diff / 4 + hxy * hxy)
        lmin = tr / 2 - rad
        lmax = tr / 2 + rad
        det_h = hxx * hyy - hxy * hxy
        return {
            "val": f0,
            "gx": gx,
            "gy": gy,
            "grad_norm": mp.hypot(gx, gy),
            "hxx": hxx,
            "hxy": hxy,
            "hyy": hyy,
            "trace_H": tr,
            "lambda_min": lmin,
            "lambda_max": lmax,
            "det_H": det_h,
        }

    fn_F_4pt = lambda t: eval_Vker_fricke_sym_mp(t, m_F, per_kernel_point=False)
    h_opt = mp.mpf(10) ** (-10)
    tau_p = mp.mpc(2, 1) / 5
    tau_m = mp.mpc(-2, 1) / 5
    tau_sad = im / mp.sqrt(5)

    st_p = grad_hess_4pt(fn_F_4pt, tau_p, h_opt)
    st_m = grad_hess_4pt(fn_F_4pt, tau_m, h_opt)
    st_sad = grad_hess_4pt(fn_F_4pt, tau_sad, h_opt)
    depth_gap_4pt = st_sad["val"] - st_p["val"]
    depth_gap_per_pt = depth_gap_4pt / 4
    trace_1200_err = abs(st_p["trace_H"] - 1200)

    passed = bool(
        max_qprod_err < mp.mpf(10) ** (-45)
        and max_s_dual_err < mp.mpf(10) ** (-35)
        and max_gamma05_err < mp.mpf(10) ** (-30)
        and max_T_err < mp.mpf(10) ** (-30)
        and max_fricke_const_err < mp.mpf(10) ** (-45)
        and raabe_all_exact
        and slope_2H_exact == Fraction(-36)
        and slope_1H_exact == Fraction(-36)
        and slope_F_exact == Fraction(12)
        and all_slopes_match_y12
        and indiv_k_max_err < mp.mpf(10) ** (-6)
        and st_p["grad_norm"] < mp.mpf(10) ** (-30)
        and st_m["grad_norm"] < mp.mpf(10) ** (-30)
        and st_p["lambda_min"] > 0
        and st_p["det_H"] > 0
        and st_m["lambda_min"] > 0
        and st_m["det_H"] > 0
        and st_sad["grad_norm"] < mp.mpf(10) ** (-30)
        and st_sad["det_H"] < 0
        and depth_gap_4pt > 20
        and trace_1200_err < mp.mpf(10) ** (-15)
    )
    return {
        "mpmath_dps": 60,
        "jtheta_vs_qprod_max_err": mp.nstr(max_qprod_err, 6),
        "S_duality_max_err": mp.nstr(max_s_dual_err, 6),
        "Gamma0_5_invariance_max_err": mp.nstr(max_gamma05_err, 6),
        "T_invariance_max_err": mp.nstr(max_T_err, 6),
        "fricke_charged_constant_identity_err": mp.nstr(max_fricke_const_err, 6),
        "raabe_identity_checks": raabe_checks,
        "raabe_all_exact": raabe_all_exact,
        "cusp_slopes": slope_num_records,
        "individual_twisted_slope_y12_max_err": mp.nstr(indiv_k_max_err, 6),
        "fermions_only_orbifold_lock": {
            "tau_plus": "(2 + i)/5",
            "tau_minus": "(-2 + i)/5",
            "V_4pt_at_tau_plus": mp.nstr(st_p["val"], 30),
            "V_4pt_at_tau_minus": mp.nstr(st_m["val"], 30),
            "V_4pt_at_saddle_i_over_sqrt5": mp.nstr(st_sad["val"], 30),
            "grad_norm_4pt_tau_plus": mp.nstr(st_p["grad_norm"], 6),
            "grad_norm_4pt_tau_minus": mp.nstr(st_m["grad_norm"], 6),
            "grad_norm_4pt_saddle": mp.nstr(st_sad["grad_norm"], 6),
            "hess_tau_plus_lambda_min": mp.nstr(st_p["lambda_min"], 20),
            "hess_tau_plus_lambda_max": mp.nstr(st_p["lambda_max"], 20),
            "hess_tau_plus_det": mp.nstr(st_p["det_H"], 20),
            "hess_tau_plus_trace_err_vs_1200": mp.nstr(trace_1200_err, 6),
            "hess_saddle_det": mp.nstr(st_sad["det_H"], 20),
            "depth_gap_4pt_vs_i_over_sqrt5": mp.nstr(depth_gap_4pt, 25),
            "depth_gap_per_kernel_pt": mp.nstr(depth_gap_per_pt, 25),
        },
        "pass": passed,
    }


# =============================================================================
# DISJOINT GL6 ORDER-20 FUCHSIAN L_2(tau) SOLVER & JTHETA YUKAWA EVALUATOR
# =============================================================================

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


def make_weierstrass_wp_jtheta(tau):
    """Weierstrass wp(z; 1, tau) via -d^2/dz^2 ln theta_1(pi z, q) - (pi^2/3) E_2(tau)."""
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


def gl6_tableau():
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
    """Independent 3-stage GL6 + order-20 extrapolation + Frobenius puncture matching for L_2(tau)."""
    wp = make_weierstrass_wp_jtheta(tau)
    glc = gl6_tableau()
    pos_re = (mp.re(tau) > 0)
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
    return {
        "L2": L2_val,
        "c_star": c_star,
        "lambda_parabolic": lam,
        "w_check": w_chk,
        "im_mBh_err": im_mBh,
    }


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
    """Disjoint branch-cut-free mpmath.jtheta evaluation of c_3(tau) and denom_hat(tau)."""
    im = mp.mpc(0, 1)
    et = eta_pentagonal_direct_mp(tau)
    denom_hat = 2 * mp.pi * (et ** 3)
    e2, _, _ = eisenstein_e2_e4_e6_mp(tau)
    q = mp.exp(im * mp.pi * tau)
    # Branch-cut-free phase correction for q^(1/4) in jtheta(2, 0, q)
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
    """Disjoint branch-cut-free mpmath.jtheta(3) evaluation of X_0, X_1."""
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
    """f_u via spectral series and a_0 via disjoint mpmath.jtheta(1, ..., derivative=1)."""
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


def center_mod_N(r, N, half_pos=True):
    """Map integer r mod N to centered representative in (-N/2, N/2] (or [-N/2, N/2))."""
    m = r % N
    if half_pos:
        return m if 2 * m <= N else m - N
    return m if 2 * m < N else m - N


def eval_yukawa_EN_mp(
    tau, L2_val, N, q_L, q_R, ec_list, C_ten, c_3, denom_hat,
    reduce_coords=True, half_pos=True, average_by_torsion_count=True, fu_cache=None
):
    """
    Evaluate E[N] (N^2 - 1 nonzero torsion points) Weil-phased boundary-torus Yukawa
    operator using disjoint mpmath.jtheta routines and exact mod-Z^2-reduced centered
    torsion coordinates. Normalized by 1/(N^2 - 1) when average_by_torsion_count=True.
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
    if fu_cache is None:
        fu_cache = {}
    Y_sum = mp.matrix(3, 3)

    for a in range(N):
        for b in range(N):
            if a == 0 and b == 0:
                continue
            if reduce_coords:
                wL0 = Fraction(center_mod_N(q_L * a, N, half_pos), N)
                wL1 = Fraction(center_mod_N(q_L * b, N, half_pos), N)
                wR0 = Fraction(center_mod_N(q_R * a, N, half_pos), N)
                wR1 = Fraction(center_mod_N(q_R * b, N, half_pos), N)
            else:
                a_c = center_mod_N(a, N, half_pos)
                b_c = center_mod_N(b, N, half_pos)
                wL0 = Fraction(q_L * a_c, N)
                wL1 = Fraction(q_L * b_c, N)
                wR0 = Fraction(q_R * a_c, N)
                wR1 = Fraction(q_R * b_c, N)

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

    if average_by_torsion_count:
        return Y_sum / (N * N - 1)
    return Y_sum


def singular_values_sorted_mp(Y):
    """Exact sorted singular values (s3 >= s2 >= s1) and left eigenbasis U_L of Y Y^H."""
    H = Y * Y.H
    ev, U_raw = mp.eighe(H)
    idx = sorted(range(3), key=lambda i: mp.re(ev[i]), reverse=True)
    lams = [max(mp.mpf(0), mp.re(ev[i])) for i in idx]
    svs = [mp.sqrt(x) for x in lams]
    U = mp.matrix([[U_raw[r, idx[c]] for c in range(3)] for r in range(3)])
    r23 = svs[1] / svs[0] if svs[0] > 0 else mp.mpf(0)
    r13 = svs[2] / svs[0] if svs[0] > 0 else mp.mpf(0)
    r12 = svs[2] / svs[1] if svs[1] > 0 else mp.mpf(0)
    return {"svs": svs, "lams": lams, "U": U, "H": H, "r23": r23, "r13": r13, "r12": r12}


def extract_flavor_observables_mp(Yu, Yd, Ye):
    """Extract (u, d, e) singular-value ratios, |V_CKM|, J_CP, and J_det_norm."""
    su = singular_values_sorted_mp(Yu)
    sd = singular_values_sorted_mp(Yd)
    se = singular_values_sorted_mp(Ye)

    Hu, Hd = su["H"], sd["H"]
    comm = Hu * Hd - Hd * Hu
    det_comm = mp.det(comm)
    tr_u = mp.re(Hu[0, 0] + Hu[1, 1] + Hu[2, 2])
    tr_d = mp.re(Hd[0, 0] + Hd[1, 1] + Hd[2, 2])
    J_det_raw = mp.im(det_comm)
    J_det_re_err = abs(mp.re(det_comm))
    J_det_norm = J_det_raw / ((tr_u ** 3) * (tr_d ** 3))

    # Ascending physical generation ordering: 0 = 1st gen (lightest), 1 = 2nd gen, 2 = 3rd gen (heaviest)
    Uu_asc = mp.matrix([[su["U"][r, 2 - c] for c in range(3)] for r in range(3)])
    Ud_asc = mp.matrix([[sd["U"][r, 2 - c] for c in range(3)] for r in range(3)])
    V = Uu_asc.H * Ud_asc
    V_abs = [[abs(V[r, c]) for c in range(3)] for r in range(3)]
    J_CP = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))
    lu, ld = su["lams"], sd["lams"]
    Delta_u = (lu[0] - lu[1]) * (lu[0] - lu[2]) * (lu[1] - lu[2])
    Delta_d = (ld[0] - ld[1]) * (ld[0] - ld[2]) * (ld[1] - ld[2])
    J_CP_from_det = abs(J_det_raw / (2 * Delta_u * Delta_d)) if (Delta_u != 0 and Delta_d != 0) else mp.mpf(0)
    J_CP_id_err = abs(abs(J_CP) - J_CP_from_det)

    rel_23_split = abs(se["r23"] - sd["r23"]) / max(se["r23"], sd["r23"]) if max(se["r23"], sd["r23"]) > 0 else mp.mpf(0)
    rel_13_split = abs(se["r13"] - sd["r13"]) / max(se["r13"], sd["r13"]) if max(se["r13"], sd["r13"]) > 0 else mp.mpf(0)
    abs_ed_diff = max(abs(se["r23"] - sd["r23"]), abs(se["r12"] - sd["r12"]))
    return {
        "u": su,
        "d": sd,
        "e": se,
        "V_abs": V_abs,
        "V_us": V_abs[0][1],
        "V_cb": V_abs[1][2],
        "V_ub": V_abs[0][2],
        "V_ts": V_abs[2][1],
        "J_CP": J_CP,
        "J_det_norm": J_det_norm,
        "J_det_re_err": J_det_re_err,
        "J_CP_identity_err": J_CP_id_err,
        "rel_23_split_e_d": rel_23_split,
        "rel_13_split_e_d": rel_13_split,
        "max_abs_ed_diff": abs_ed_diff,
    }


def random_haar_u3_mp(rng):
    """Exact Mezzadri Haar random U(3) matrix in current mp.mp.dps (zero float literals)."""
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

    Q = mp.matrix(3, 3)
    for k in range(3):
        v = [Z[r, k] for r in range(3)]
        for _ in range(2):
            for j in range(k):
                dot = sum(mp.conj(Q[r, j]) * v[r] for r in range(3))
                v = [v[r] - dot * Q[r, j] for r in range(3)]
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
        for r in range(3):
            Q[r, k] = v[r] / nrm
    return Q


def run_haar_gate_3sector_mp(Yu, Yd, Ye, seed, n_trials=10, dps_haar=45):
    """
    Mandatory Guardrail 3: 10-trial random Haar U(3) basis-scrambling gate at 45 dps
    with independent (U_L, U_{R,u}, U_{R,d}, U_{R,e}) across (Y_u, Y_d, Y_e).
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps_haar
    Yu_h = mp.matrix([[mp.mpc(Yu[r, c]) for c in range(3)] for r in range(3)])
    Yd_h = mp.matrix([[mp.mpc(Yd[r, c]) for c in range(3)] for r in range(3)])
    Ye_h = mp.matrix([[mp.mpc(Ye[r, c]) for c in range(3)] for r in range(3)])
    base = extract_flavor_observables_mp(Yu_h, Yd_h, Ye_h)
    rng = random.Random(seed)

    max_unitarity_err = mp.mpf(0)
    max_ratio_drift = mp.mpf(0)
    max_V_drift = mp.mpf(0)
    max_JCP_drift = mp.mpf(0)
    max_Jdet_drift = mp.mpf(0)

    for _ in range(n_trials):
        UL = random_haar_u3_mp(rng)
        URu = random_haar_u3_mp(rng)
        URd = random_haar_u3_mp(rng)
        URe = random_haar_u3_mp(rng)
        for U in (UL, URu, URd, URe):
            dI = U.H * U - mp.eye(3)
            uerr = mp.sqrt(sum(abs(dI[r, c]) ** 2 for r in range(3) for c in range(3)))
            if uerr > max_unitarity_err:
                max_unitarity_err = uerr
        obs = extract_flavor_observables_mp(UL * Yu_h * URu.H, UL * Yd_h * URd.H, UL * Ye_h * URe.H)
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
        "max_haar_unitarity_err": mp.nstr(max_unitarity_err, 6),
        "max_ratio_drift": mp.nstr(max_ratio_drift, 6),
        "max_V_abs_drift": mp.nstr(max_V_drift, 6),
        "max_J_CP_drift": mp.nstr(max_JCP_drift, 6),
        "max_J_det_norm_drift": mp.nstr(max_Jdet_drift, 6),
        "max_overall_drift": mp.nstr(max_all, 6),
        "pass": bool(max_unitarity_err < mp.mpf(10) ** (-38) and max_all < mp.mpf(10) ** (-30)),
    }


# =============================================================================
# TASK OW6-C: COVERING-TORUS m in {8, 24, 40}, E[5] vs E[5]+E[6], HAAR & TRADE-OFF
# =============================================================================

def run_task_ow6_c():
    mp.mp.dps = 55
    ec_list, C_ten = build_fu2_coupling_tensor()
    l2_cache = {}

    # Independent L_2(tau) S-transformation law check without reduction:
    # L_2(-1/tau) == L_2(tau) + ln|tau| at tau = 1/5 + i
    tau_s = mp.mpc(1, 0) / 5 + mp.mpc(0, 1)
    r_sa = solve_L2_F1_gl6(tau_s)
    r_sb = solve_L2_F1_gl6(-1 / tau_s)
    L2_S_law_err = abs(r_sb["L2"] - (r_sa["L2"] + mp.log(abs(tau_s))))

    # Regime-4b zero-parameter open-weave weights from A2-OW5:
    # lambda(t, +1) = (t + sqrt(t^2 - 4)) / 2
    lam_3 = (3 + mp.sqrt(5)) / 2
    lam_4 = (4 + mp.sqrt(12)) / 2
    w_3 = lam_3 ** (-4)
    w_4 = 4 * (lam_4 ** (-4))

    sectors = {"u": (1, -4), "d": (1, 2), "e": (-3, 6)}
    tau_base = mp.mpc(2, 1) / 5
    cover_levels = [8, 24, 40]

    e5_only_results = {}
    ow_results = {}
    haar_results = {}
    stored_for_pf = {}

    max_e5_ed_deg = mp.mpf(0)
    max_ode_wchk = mp.mpf(0)
    max_JCP_id_err = mp.mpf(0)
    e6_half_sign_invariance_err = None

    for m in cover_levels:
        tau_m = m * tau_base
        L2_m, base_m = solve_L2_any_gl6(tau_m, l2_cache)
        max_ode_wchk = max(max_ode_wchk, base_m["w_check"])
        c3_m, den_m = compute_c3_denom_jtheta_mp(tau_m)
        fu_cache_m = {}

        Y5 = {}
        Y6 = {}
        for sec, (qL, qR) in sectors.items():
            Y5[sec] = eval_yukawa_EN_mp(
                tau_m, L2_m, 5, qL, qR, ec_list, C_ten, c3_m, den_m,
                reduce_coords=True, half_pos=True, average_by_torsion_count=True, fu_cache=fu_cache_m,
            )
            Y6[sec] = eval_yukawa_EN_mp(
                tau_m, L2_m, 6, qL, qR, ec_list, C_ten, c3_m, den_m,
                reduce_coords=True, half_pos=True, average_by_torsion_count=True, fu_cache=fu_cache_m,
            )

        if m == 8:
            # Verify half-integer centering choice (+1/2 vs -1/2) on E[6] is invariant
            Y6_d_neg = eval_yukawa_EN_mp(
                tau_m, L2_m, 6, 1, 2, ec_list, C_ten, c3_m, den_m,
                reduce_coords=True, half_pos=False, average_by_torsion_count=True, fu_cache=fu_cache_m,
            )
            Y6_e_neg = eval_yukawa_EN_mp(
                tau_m, L2_m, 6, -3, 6, ec_list, C_ten, c3_m, den_m,
                reduce_coords=True, half_pos=False, average_by_torsion_count=True, fu_cache=fu_cache_m,
            )
            obs_pos = extract_flavor_observables_mp(
                w_3 * Y5["u"] + w_4 * Y6["u"], w_3 * Y5["d"] + w_4 * Y6["d"], w_3 * Y5["e"] + w_4 * Y6["e"]
            )
            Y6_u_neg = eval_yukawa_EN_mp(
                tau_m, L2_m, 6, 1, -4, ec_list, C_ten, c3_m, den_m,
                reduce_coords=True, half_pos=False, average_by_torsion_count=True, fu_cache=fu_cache_m,
            )
            obs_neg = extract_flavor_observables_mp(
                w_3 * Y5["u"] + w_4 * Y6_u_neg, w_3 * Y5["d"] + w_4 * Y6_d_neg, w_3 * Y5["e"] + w_4 * Y6_e_neg
            )
            e6_half_sign_invariance_err = max(
                abs(obs_pos["d"]["r23"] - obs_neg["d"]["r23"]),
                abs(obs_pos["e"]["r23"] - obs_neg["e"]["r23"]),
                abs(obs_pos["J_CP"] - obs_neg["J_CP"]),
            )
            stored_for_pf["m8"] = {
                "tau": tau_m,
                "L2": L2_m,
                "c3": c3_m,
                "den": den_m,
                "Y5": Y5,
                "Y6": Y6,
                "w_3": w_3,
                "w_4": w_4,
            }

        # 1. Taped-flute E[5] alone
        obs_5 = extract_flavor_observables_mp(Y5["u"], Y5["d"], Y5["e"])
        max_e5_ed_deg = max(max_e5_ed_deg, obs_5["max_abs_ed_diff"])
        e5_only_results[str(m)] = {
            "m": m,
            "tau": f"({2 * m} + {m}i)/5",
            "L2": mp.nstr(L2_m, 35),
            "r23_u": mp.nstr(obs_5["u"]["r23"], 20),
            "r13_u": mp.nstr(obs_5["u"]["r13"], 20),
            "r23_d": mp.nstr(obs_5["d"]["r23"], 20),
            "r13_d": mp.nstr(obs_5["d"]["r13"], 20),
            "r23_e": mp.nstr(obs_5["e"]["r23"], 20),
            "r13_e": mp.nstr(obs_5["e"]["r13"], 20),
            "max_abs_ed_diff": mp.nstr(obs_5["max_abs_ed_diff"], 6),
            "J_CP": mp.nstr(obs_5["J_CP"], 25),
            "J_det_norm": mp.nstr(obs_5["J_det_norm"], 25),
        }

        # 2. Open-weave Regime-4b E[5] + E[6]
        Yu_ow = w_3 * Y5["u"] + w_4 * Y6["u"]
        Yd_ow = w_3 * Y5["d"] + w_4 * Y6["d"]
        Ye_ow = w_3 * Y5["e"] + w_4 * Y6["e"]
        obs_ow = extract_flavor_observables_mp(Yu_ow, Yd_ow, Ye_ow)
        max_JCP_id_err = max(max_JCP_id_err, obs_ow["J_CP_identity_err"])

        # 3. Mandatory Guardrail 3: 10-trial 45-dps Haar gate across (Y_u, Y_d, Y_e)
        haar_m = run_haar_gate_3sector_mp(Yu_ow, Yd_ow, Ye_ow, seed=2026112100 + m, n_trials=10, dps_haar=45)
        haar_results[str(m)] = haar_m

        ow_results[str(m)] = {
            "m": m,
            "tau": f"({2 * m} + {m}i)/5",
            "Im_tau": mp.nstr(mp.im(tau_m), 10),
            "r23_u": mp.nstr(obs_ow["u"]["r23"], 25),
            "r13_u": mp.nstr(obs_ow["u"]["r13"], 25),
            "r12_u": mp.nstr(obs_ow["u"]["r12"], 25),
            "r23_d": mp.nstr(obs_ow["d"]["r23"], 25),
            "r13_d": mp.nstr(obs_ow["d"]["r13"], 25),
            "r12_d": mp.nstr(obs_ow["d"]["r12"], 25),
            "r23_e": mp.nstr(obs_ow["e"]["r23"], 25),
            "r13_e": mp.nstr(obs_ow["e"]["r13"], 25),
            "r12_e": mp.nstr(obs_ow["e"]["r12"], 25),
            "rel_23_split_e_d": mp.nstr(obs_ow["rel_23_split_e_d"], 25),
            "rel_13_split_e_d": mp.nstr(obs_ow["rel_13_split_e_d"], 25),
            "V_abs": [[mp.nstr(obs_ow["V_abs"][r][c], 20) for c in range(3)] for r in range(3)],
            "V_us_12": mp.nstr(obs_ow["V_us"], 20),
            "V_cb_23": mp.nstr(obs_ow["V_cb"], 20),
            "V_ub_13": mp.nstr(obs_ow["V_ub"], 20),
            "V_ts_32": mp.nstr(obs_ow["V_ts"], 20),
            "J_CP": mp.nstr(obs_ow["J_CP"], 30),
            "J_det_norm": mp.nstr(obs_ow["J_det_norm"], 30),
            "J_CP_identity_err": mp.nstr(obs_ow["J_CP_identity_err"], 6),
        }

    # Verify all pass bars explicitly from computed mpmath values (zero hardcoded flags)
    o8, o24, o40 = ow_results["8"], ow_results["24"], ow_results["40"]
    v8_us, v8_ts = mp.mpf(o8["V_us_12"]), mp.mpf(o8["V_ts_32"])
    v24_us, v24_ts = mp.mpf(o24["V_us_12"]), mp.mpf(o24["V_ts_32"])
    v40_us, v40_ts = mp.mpf(o40["V_us_12"]), mp.mpf(o40["V_ts_32"])

    split_ok = bool(
        mp.mpf(o8["rel_23_split_e_d"]) > mp.mpf(45) / 100
        and mp.mpf(o24["rel_23_split_e_d"]) > mp.mpf(97) / 100
        and mp.mpf(o40["rel_23_split_e_d"]) > mp.mpf(99) / 100
    )
    jcp_nonzero_ok = bool(
        abs(mp.mpf(o8["J_CP"])) > mp.mpf(3) / 10000
        and abs(mp.mpf(o24["J_CP"])) > mp.mpf(10) ** (-17)
        and abs(mp.mpf(o40["J_CP"])) > mp.mpf(10) ** (-29)
    )
    tradeoff_m8_ok = bool(
        v8_us > mp.mpf(9) / 100
        and v8_ts > mp.mpf(9) / 100
        and abs(mp.mpf(o8["J_CP"])) > mp.mpf(3) / 10000
        and mp.mpf(o8["r23_u"]) > mp.mpf(1) / 10
        and mp.mpf(o8["r23_d"]) > mp.mpf(1) / 10
        and mp.mpf(o8["r23_e"]) > mp.mpf(1) / 10
    )
    tradeoff_m24_ok = bool(
        mp.mpf(o24["r13_u"]) < mp.mpf(10) ** (-5)
        and mp.mpf(o24["r13_d"]) < mp.mpf(10) ** (-5)
        and mp.mpf(o24["r13_e"]) < mp.mpf(10) ** (-5)
        and v24_us < mp.mpf(1) / 100
        and v24_ts < mp.mpf(1) / 100
        and abs(mp.mpf(o24["J_CP"])) < mp.mpf(10) ** (-15)
    )
    tradeoff_m40_ok = bool(
        mp.mpf(o40["r13_u"]) < mp.mpf(10) ** (-10)
        and mp.mpf(o40["r13_d"]) < mp.mpf(10) ** (-10)
        and mp.mpf(o40["r13_e"]) < mp.mpf(10) ** (-10)
        and v40_us < mp.mpf(2) / 1000
        and v40_ts < mp.mpf(2) / 1000
        and abs(mp.mpf(o40["J_CP"])) < mp.mpf(10) ** (-27)
    )
    haar_all_ok = all(haar_results[str(m)]["pass"] for m in cover_levels)

    passed = bool(
        L2_S_law_err < mp.mpf(10) ** (-25)
        and max_ode_wchk < mp.mpf(10) ** (-25)
        and max_e5_ed_deg < mp.mpf(10) ** (-35)
        and e6_half_sign_invariance_err < mp.mpf(10) ** (-40)
        and max_JCP_id_err < mp.mpf(10) ** (-25)
        and split_ok
        and jcp_nonzero_ok
        and haar_all_ok
        and tradeoff_m8_ok
        and tradeoff_m24_ok
        and tradeoff_m40_ok
    )

    return {
        "L2_solver_method": "disjoint_3stage_GL6_order20_extrapolation_jtheta_wp_plus_Frobenius",
        "yukawa_method": "disjoint_branch_cut_free_mpmath_jtheta_with_mod_Z2_centered_torsion_average",
        "L2_S_transformation_law_err": mp.nstr(L2_S_law_err, 6),
        "max_L2_ode_wronskian_err": mp.nstr(max_ode_wchk, 6),
        "weights": {
            "lambda_3_plus1": mp.nstr(lam_3, 30),
            "lambda_4_plus1": mp.nstr(lam_4, 30),
            "w_3": mp.nstr(w_3, 30),
            "w_4": mp.nstr(w_4, 30),
        },
        "E5_only_max_ed_degeneracy_err": mp.nstr(max_e5_ed_deg, 6),
        "E6_half_integer_centering_invariance_err": mp.nstr(e6_half_sign_invariance_err, 6),
        "max_J_CP_det_identity_err": mp.nstr(max_JCP_id_err, 6),
        "E5_only_by_m": e5_only_results,
        "open_weave_E5_plus_E6_by_m": ow_results,
        "haar_scrambling_3sector_by_m": haar_results,
        "hierarchy_vs_ckm_tradeoff_checks": {
            "splitting_bars_pass": split_ok,
            "jcp_nonzero_bars_pass": jcp_nonzero_ok,
            "m8_large_mixing_shallow_mass_pass": tradeoff_m8_ok,
            "m24_multi_decade_hierarchy_suppressed_ckm_pass": tradeoff_m24_ok,
            "m40_deep_hierarchy_tiny_ckm_pass": tradeoff_m40_ok,
        },
        "pass": passed,
    }, stored_for_pf, l2_cache, ec_list, C_ten


# =============================================================================
# TASK OW6-D: FOUR PLANTED FAULTS (PF-OW6-1 THROUGH PF-OW6-4 WITH ERRATUM 1)
# =============================================================================

def run_task_ow6_d(stored_for_pf, l2_cache, ec_list, C_ten):
    mp.mp.dps = 55
    im = mp.mpc(0, 1)

    # PF-OW6-1: Flipping Berezin sign (-V_1) yields d(-V_1)/dy < 0 at tau = 2i
    slope_neg_V1_2i = -dV1_dy_e2_mp(2 * im)
    slope_neg_V1_2i_fd = fd4_1st_real(lambda yy: -V1_direct_no_reduce_mp(im * yy), mp.mpf(2), mp.mpf(10) ** (-10))
    pf1_caught = bool(
        slope_neg_V1_2i < 0
        and slope_neg_V1_2i_fd < 0
        and abs(slope_neg_V1_2i - slope_neg_V1_2i_fd) < mp.mpf(10) ** (-30)
    )

    # PF-OW6-2: Omitting mod-Z^2 reduction on E[5] wrap-around coordinates at m = 8
    #           falsely breaks e = d degeneracy by > 1/10
    m8 = stored_for_pf["m8"]
    Yd_unred = eval_yukawa_EN_mp(
        m8["tau"], m8["L2"], 5, 1, 2, ec_list, C_ten, m8["c3"], m8["den"],
        reduce_coords=False, half_pos=True, average_by_torsion_count=True,
    )
    Ye_unred = eval_yukawa_EN_mp(
        m8["tau"], m8["L2"], 5, -3, 6, ec_list, C_ten, m8["c3"], m8["den"],
        reduce_coords=False, half_pos=True, average_by_torsion_count=True,
    )
    sd_un = singular_values_sorted_mp(Yd_unred)
    se_un = singular_values_sorted_mp(Ye_unred)
    unred_r23_diff = abs(se_un["r23"] - sd_un["r23"])
    unred_rel_23_split = unred_r23_diff / max(se_un["r23"], sd_un["r23"])
    pf2_caught = bool(unred_r23_diff > mp.mpf(1) / 10 and unred_rel_23_split > mp.mpf(1) / 10)

    # PF-OW6-3: Setting w_4 = 0 (E[5] only) collapses e != d splitting to < 10^-35
    w3 = m8["w_3"]
    Yu_w4z = w3 * m8["Y5"]["u"]
    Yd_w4z = w3 * m8["Y5"]["d"]
    Ye_w4z = w3 * m8["Y5"]["e"]
    obs_w4z = extract_flavor_observables_mp(Yu_w4z, Yd_w4z, Ye_w4z)
    pf3_caught = bool(
        obs_w4z["max_abs_ed_diff"] < mp.mpf(10) ** (-35)
        and obs_w4z["rel_23_split_e_d"] < mp.mpf(10) ** (-35)
    )

    # PF-OW6-4 (Erratum 1):
    #   - Imaginary-axis control tau = 5i on reduced E[5]: |J_CP| < 10^-40 and |J_det_norm| < 10^-40
    #   - Non-trivial Gauss-phase point tau = 2 + i on reduced E[5]: |J_CP| > 1/100
    tau_5i = 5 * im
    L2_5i, _ = solve_L2_any_gl6(tau_5i, l2_cache)
    c3_5i, den_5i = compute_c3_denom_jtheta_mp(tau_5i)
    fc_5i = {}
    Yu_5i = eval_yukawa_EN_mp(tau_5i, L2_5i, 5, 1, -4, ec_list, C_ten, c3_5i, den_5i, True, True, True, fc_5i)
    Yd_5i = eval_yukawa_EN_mp(tau_5i, L2_5i, 5, 1, 2, ec_list, C_ten, c3_5i, den_5i, True, True, True, fc_5i)
    Ye_5i = eval_yukawa_EN_mp(tau_5i, L2_5i, 5, -3, 6, ec_list, C_ten, c3_5i, den_5i, True, True, True, fc_5i)
    obs_5i = extract_flavor_observables_mp(Yu_5i, Yd_5i, Ye_5i)

    tau_2pi = mp.mpc(2, 1)
    L2_2pi, _ = solve_L2_any_gl6(tau_2pi, l2_cache)
    c3_2pi, den_2pi = compute_c3_denom_jtheta_mp(tau_2pi)
    fc_2pi = {}
    Yu_2pi = eval_yukawa_EN_mp(tau_2pi, L2_2pi, 5, 1, -4, ec_list, C_ten, c3_2pi, den_2pi, True, True, True, fc_2pi)
    Yd_2pi = eval_yukawa_EN_mp(tau_2pi, L2_2pi, 5, 1, 2, ec_list, C_ten, c3_2pi, den_2pi, True, True, True, fc_2pi)
    Ye_2pi = eval_yukawa_EN_mp(tau_2pi, L2_2pi, 5, -3, 6, ec_list, C_ten, c3_2pi, den_2pi, True, True, True, fc_2pi)
    obs_2pi = extract_flavor_observables_mp(Yu_2pi, Yd_2pi, Ye_2pi)

    pf4_caught = bool(
        abs(obs_5i["J_CP"]) < mp.mpf(10) ** (-40)
        and abs(obs_5i["J_det_norm"]) < mp.mpf(10) ** (-40)
        and abs(obs_2pi["J_CP"]) > mp.mpf(1) / 100
    )

    all_4 = bool(pf1_caught and pf2_caught and pf3_caught and pf4_caught)
    return {
        "PF_OW6_1_berezin_sign_flip_2i": {
            "d_minus_V1_dy_at_2i_E2": mp.nstr(slope_neg_V1_2i, 25),
            "d_minus_V1_dy_at_2i_FD4": mp.nstr(slope_neg_V1_2i_fd, 25),
            "caught": pf1_caught,
        },
        "PF_OW6_2_unreduced_E5_spurious_ed_split_m8": {
            "unreduced_r23_d": mp.nstr(sd_un["r23"], 20),
            "unreduced_r23_e": mp.nstr(se_un["r23"], 20),
            "abs_r23_diff": mp.nstr(unred_r23_diff, 20),
            "rel_r23_split": mp.nstr(unred_rel_23_split, 20),
            "caught": pf2_caught,
        },
        "PF_OW6_3_w4_zero_collapses_ed_split_m8": {
            "max_abs_ed_diff": mp.nstr(obs_w4z["max_abs_ed_diff"], 6),
            "rel_23_split_e_d": mp.nstr(obs_w4z["rel_23_split_e_d"], 6),
            "caught": pf3_caught,
        },
        "PF_OW6_4_erratum1_imaginary_axis_cp_control": {
            "tau_5i_L2": mp.nstr(L2_5i, 35),
            "tau_5i_J_CP": mp.nstr(obs_5i["J_CP"], 10),
            "tau_5i_J_det_norm": mp.nstr(obs_5i["J_det_norm"], 10),
            "tau_2_plus_i_L2": mp.nstr(L2_2pi, 35),
            "tau_2_plus_i_J_CP": mp.nstr(obs_2pi["J_CP"], 25),
            "tau_2_plus_i_J_det_norm": mp.nstr(obs_2pi["J_det_norm"], 25),
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
    out_path = os.path.join(os.path.dirname(script_path), "referee_a2_ow6_out.json")

    sec0 = audit_script_hygiene(script_path)
    t0 = time.time()
    secA = run_task_ow6_a()
    tA = time.time()
    secB = run_task_ow6_b()
    tB = time.time()
    secC, stored_pf, l2_cache, ec_list, C_ten = run_task_ow6_c()
    tC = time.time()
    secD = run_task_ow6_d(stored_pf, l2_cache, ec_list, C_ten)
    tD = time.time()

    all_pass = bool(
        sec0["hygiene_pass"]
        and secA["pass"]
        and secB["pass"]
        and secC["pass"]
        and secD["pass"]
    )
    payload = {
        "card": "AGY-002_A2-OW6_plus_ERRATUM-1",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_firewall": "0 of 19",
        "section_0_custody_and_hygiene": sec0,
        "task_OW6_A": secA,
        "task_OW6_B": secB,
        "task_OW6_C": secC,
        "task_OW6_D": secD,
        "timings_seconds": {
            "OW6_A": round(tA - t0, 3),
            "OW6_B": round(tB - tA, 3),
            "OW6_C": round(tC - tB, 3),
            "OW6_D": round(tD - tC, 3),
            "total": round(tD - t_start, 3),
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
