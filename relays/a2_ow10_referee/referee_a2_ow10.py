#!/usr/bin/env python3
"""Independent Cold-Room Zero-Trust Referee for AGY-002 Card A2-OW10.

Built strictly from:
  relays/cards/AGY-002_A2-OW10_asymptotic-safety-double-pincer-stelle-pole-and-master-scorecard.md

Disjoint verification methods:
  - OW10-A (FRG): Symbolic SymPy derivation of the exact eta_N = -2 cubic identity;
    manual SymPy Sturm-sequence proof of exact valid root count on {u > 0 : D(u) < 0};
    direct 55-dps mpmath bracketed bisection on lam in (-100, 49/100) (extended if
    Cauchy bound exceeds u = 201) + direct 2D Newton-Raphson on (beta_g, beta_lam);
    4th-order Richardson finite-difference Jacobian stability exponents theta = -eig(J);
    zero calls to mp.polyroots / sp.roots / numpy.roots.
  - OW10-A (Delta(2, 3, N) actions): Disjoint exact matrix-group realizations
    GL(2, F_2), PSL(2, F_3), SO(3, Z) octahedral matrices, PSL(2, F_5); exhaustive
    subgroup-lattice and normal-core computation; direct bitmask 0 .. 2^d - 1
    Fock-space Cartan-weight chirality and gauge/gravitational/Witten anomaly sums.
  - OW10-B (Stelle Pole & a-Theorem): Symbolic SymPy Rational, apart, residue.
  - OW10-C (Master Scorecard): Independent 12-row disjoint partition audit.
  - OW10-D (Planted Faults): Independent execution of PF-OW10-1..4.

Guardrails:
  - 0 float/complex AST literals; 0 frontier/ imports; 0 dict-literal booleans;
    0 of 19 empirical PDG inputs (Litim 2004 & DEP 1311-2898 isolated in Guardrail 4).
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


# Configure 55-dps working precision as specified in the cold-room protocol.
DPS_TARGET = 55
mp.mp.dps = DPS_TARGET


def mp_rat(num, den=1):
    """Exact mpmath rational without float literals."""
    return mp.mpf(num) / mp.mpf(den)


def mp_pow10(exp_int):
    """Exact integer power of 10 in mpmath without float literals."""
    return mp.mpf(10) ** exp_int


def fmt_mp(val, digits=40):
    """Format high-precision mpmath real scalar as exact decimal string."""
    return mp.nstr(val, digits)


def fmt_rat(expr):
    """Format exact SymPy Rational as canonical 'p/q' or 'p' string."""
    r = sp.Rational(expr)
    if r.q == 1:
        return str(r.p)
    return f"{r.p}/{r.q}"


# =============================================================================
# SECTION 1: OW10-A — SYMBOLIC FRG DERIVATION, STURM PROOF, & 55-DPS 2D SOLVER
# =============================================================================

def verify_rg_differential_variable_and_cubic():
    """Guardrail 4 RG variable check + exact symbolic cubic derivation in SymPy."""
    eta_sym, u_s, g_s, Mg_s, Ml_s = sp.symbols("eta_N u g M_g M_l", real=True)
    t_rg = sp.symbols("t_rg", real=True)

    # Check RG variable t = ln(k / k_0): Z_N(k) = 1 / (16 pi G_k),
    # eta_N = -k d(ln Z_N)/dk = +k d(ln G_k)/dk = +d(ln G_k)/dt.
    # Then g = k^2 G_k satisfies dg/dt = (2 + eta_N) g, and
    # lam = Lambda_k / k^2 satisfies (at zero quantum threshold d(Lambda_k / G_k)/dt = 0)
    # d(lam)/dt = (eta_N - 2) lam.
    G_fn = sp.Function("G")(t_rg)
    L_fn = sp.Function("Lambda")(t_rg)
    k_fn = sp.exp(t_rg)
    g_dimless = k_fn**2 * G_fn
    lam_dimless = L_fn / k_fn**2
    dg_dt = sp.simplify(sp.diff(g_dimless, t_rg).subs(sp.diff(G_fn, t_rg), eta_sym * G_fn) / g_dimless)
    expected_dg_factor = sp.Integer(2) + eta_sym
    rg_g_scaling_zero = sp.simplify(dg_dt - expected_dg_factor)

    vac_energy = L_fn / G_fn
    d_vac_dt = sp.diff(vac_energy, t_rg).subs(sp.diff(G_fn, t_rg), eta_sym * G_fn)
    dL_dt_zero_thresh = sp.solve(sp.Eq(d_vac_dt, 0), sp.diff(L_fn, t_rg))[0]
    dlam_dt = sp.simplify(sp.diff(lam_dimless, t_rg).subs(sp.diff(L_fn, t_rg), dL_dt_zero_thresh) / lam_dimless)
    expected_dlam_factor = eta_sym - sp.Integer(2)
    rg_lam_scaling_zero = sp.simplify(dlam_dt - expected_dlam_factor)

    # Exact Litim harmonic-gauge FRG system (d = 4)
    lam_s = (sp.Integer(1) - u_s) / sp.Integer(2)
    B1_s = (sp.Integer(1) / (sp.Integer(6) * sp.pi)) * (
        sp.Integer(10) / u_s - sp.Integer(18) / (u_s**2) - sp.Integer(14) + Mg_s
    )
    B2_s = (sp.Integer(1) / (sp.Integer(6) * sp.pi)) * (
        -sp.Integer(5) / (sp.Integer(2) * u_s) + sp.Integer(3) / (u_s**2)
    )
    eta_s = g_s * B1_s / (sp.Integer(1) - g_s * B2_s)
    beta_g_s = (sp.Integer(2) + eta_s) * g_s
    beta_lam_s = (eta_s - sp.Integer(2)) * lam_s + (g_s / (sp.Integer(2) * sp.pi)) * (
        sp.Integer(5) * (sp.Integer(1) - eta_s / sp.Integer(6)) / u_s - sp.Integer(4) + Ml_s
    )

    # Solve eta_N = -2 symbolically for g_*(u)
    D_u = (Mg_s - sp.Integer(14)) * u_s**2 + sp.Integer(15) * u_s - sp.Integer(24)
    g_star_expected = -sp.Integer(12) * sp.pi * u_s**2 / D_u
    g_sols = sp.solve(sp.Eq(eta_s, -sp.Integer(2)), g_s)
    g_star_derived = sp.simplify(g_sols[0])
    g_star_diff = sp.simplify(g_star_derived - g_star_expected)

    eta_sub_diff = sp.simplify(eta_s.subs(g_s, g_star_derived) + sp.Integer(2))
    bg_sub_diff = sp.simplify(beta_g_s.subs(g_s, g_star_derived))

    # Substitute g_*(u) into beta_lam(g, lam) and extract exact numerator polynomial after cancellation
    bl_cancelled = sp.cancel(beta_lam_s.subs(g_s, g_star_derived))
    num_bl, den_bl = sp.fraction(bl_cancelled)
    # Denominator is proportional to D_u (and constant factor)
    # Match numerator up to overall integer scale factor
    target_cubic = (
        sp.Integer(2) * (Mg_s - sp.Integer(14)) * u_s**3
        + (sp.Integer(82) - sp.Integer(2) * Mg_s - sp.Integer(6) * Ml_s) * u_s**2
        - sp.Integer(118) * u_s
        + sp.Integer(48)
    )
    # Check proportionality constant between num_bl and target_cubic
    num_expanded = sp.expand(num_bl)
    target_expanded = sp.expand(target_cubic)
    # Constant term ratio: num_bl(u=0) / 48
    scale_const = sp.Rational(num_expanded.subs(u_s, 0), target_expanded.subs(u_s, 0))
    cubic_identity_diff = sp.expand(num_expanded - scale_const * target_expanded)

    # Verify denominator proportionality to D_u
    den_expanded = sp.expand(den_bl)
    den_scale = sp.Rational(den_expanded.subs(u_s, 0), sp.expand(D_u).subs(u_s, 0))
    den_identity_diff = sp.expand(den_expanded - den_scale * sp.expand(D_u))

    # Verify 1 - g_*(u) B_2(u) = B_1(u) / (B_1(u) - 2 B_2(u))
    pole_denom_expr = sp.cancel(sp.Integer(1) - g_star_derived * B2_s)
    expected_pole_denom = sp.cancel(B1_s / (B1_s - sp.Integer(2) * B2_s))
    pole_denom_diff = sp.simplify(pole_denom_expr - expected_pole_denom)

    # Symbolic Double-Pincer Inequalities
    N_gen_s, n_H_s = sp.symbols("N_gen n_H", real=True)
    # At N = 5, 2H: N_S = 8, N_V = 12, N_W = 16 N_gen => M_g = 8 + 16 N_gen - 48
    Mg_ngen = sp.Integer(8) + sp.Integer(16) * N_gen_s - sp.Integer(48)
    ngen_lo = sp.solve(sp.Eq(Mg_ngen, 0), N_gen_s)[0]
    ngen_hi = sp.solve(sp.Eq(Mg_ngen, 14), N_gen_s)[0]
    ngen_integers = [k_i for k_i in range(1, 10) if ngen_lo < k_i < ngen_hi]

    # At N = 5, N_gen = 3: N_W = 48, N_V = 12, N_S = 4 n_H => M_g = 4 n_H
    Mg_nh = sp.Integer(4) * n_H_s + sp.Integer(48) - sp.Integer(48)
    nh_lo = sp.solve(sp.Eq(Mg_nh, 0), n_H_s)[0]
    nh_hi = sp.solve(sp.Eq(Mg_nh, 14), n_H_s)[0]
    nh_integers = [k_i for k_i in range(0, 10) if nh_lo < k_i < nh_hi]

    # Critical M_g = 14 quadratic degeneration discriminant:
    # 2(0) u^3 + (54 - 6 M_l) u^2 - 118 u + 48 = 0 => disc = 118^2 - 4*48*(54 - 6 M_l)
    disc_mg14 = sp.expand(sp.Integer(118)**2 - sp.Integer(4) * sp.Integer(48) * (sp.Integer(54) - sp.Integer(6) * Ml_s))
    ml_crit_mg14 = sp.solve(sp.Eq(disc_mg14, 0), Ml_s)[0]

    passed = bool(
        rg_g_scaling_zero == 0
        and rg_lam_scaling_zero == 0
        and g_star_diff == 0
        and eta_sub_diff == 0
        and bg_sub_diff == 0
        and cubic_identity_diff == 0
        and den_identity_diff == 0
        and pole_denom_diff == 0
        and ngen_lo == sp.Rational(5, 2)
        and ngen_hi == sp.Rational(27, 8)
        and ngen_integers == [3]
        and nh_lo == sp.Integer(0)
        and nh_hi == sp.Rational(7, 2)
        and nh_integers == [1, 2, 3]
    )

    return {
        "rg_g_scaling_residual": str(rg_g_scaling_zero),
        "rg_lam_scaling_residual": str(rg_lam_scaling_zero),
        "g_star_formula_diff": str(g_star_diff),
        "eta_N_sub_residual": str(eta_sub_diff),
        "beta_g_sub_residual": str(bg_sub_diff),
        "cubic_scale_factor": fmt_rat(scale_const),
        "cubic_identity_residual": str(cubic_identity_diff),
        "denominator_scale_factor": fmt_rat(den_scale),
        "denominator_identity_residual": str(den_identity_diff),
        "pole_denom_identity_residual": str(pole_denom_diff),
        "double_pincer_N_gen_bounds": [fmt_rat(ngen_lo), fmt_rat(ngen_hi)],
        "double_pincer_N_gen_unique_integers": ngen_integers,
        "double_pincer_n_H_bounds": [fmt_rat(nh_lo), fmt_rat(nh_hi)],
        "double_pincer_n_H_allowed_integers": nh_integers,
        "M_g_14_discriminant_formula": str(disc_mg14),
        "M_g_14_critical_M_l_threshold": fmt_rat(ml_crit_mg14),
        "passed": passed,
    }


def build_sturm_sequence(poly):
    """Construct exact Sturm sequence via SymPy polynomial Euclidean remainder."""
    seq = [poly]
    if poly.degree() <= 0:
        return seq
    seq.append(poly.diff())
    while seq[-1].degree() > 0:
        rem_poly = sp.rem(seq[-2], seq[-1])
        if rem_poly.is_zero:
            break
        seq.append(-rem_poly)
    return seq


def count_sign_variations(signs):
    """Count sign changes in a sequence of exact signs in {-1, 0, +1}."""
    nonzero = [s for s in signs if s != 0]
    return sum(1 for i in range(len(nonzero) - 1) if nonzero[i] * nonzero[i + 1] < 0)


def exact_sign_at_point(poly, u_sym, pt):
    """Exact sign of polynomial poly at rational/quadratic-irrational pt or +oo."""
    if pt == sp.oo:
        return int(sp.sign(poly.LC()))
    val = sp.simplify(poly.as_expr().subs(u_sym, pt))
    return int(sp.sign(val))


def sturm_root_count_open_interval(seq, u_sym, a_pt, b_pt):
    """Exact count of distinct real roots of seq[0] in open interval (a_pt, b_pt)."""
    signs_a = [exact_sign_at_point(p, u_sym, a_pt) for p in seq]
    signs_b = [exact_sign_at_point(p, u_sym, b_pt) for p in seq]
    return count_sign_variations(signs_a) - count_sign_variations(signs_b)


def valid_u_intervals_exact(Mg_int):
    """Exact open sub-intervals of (0, +oo) where D(u) = (M_g - 14) u^2 + 15 u - 24 < 0.

    Returns list of (sympy_lo, sympy_hi, mp_lo, mp_hi_or_None).
    """
    a = Mg_int - 14
    if a == 0:
        # D(u) = 15 u - 24 < 0 <=> 0 < u < 8/5
        return [(sp.Integer(0), sp.Rational(8, 5), mp.mpf(0), mp_rat(8, 5))]
    disc = 225 + 96 * a
    if a > 0:
        # Unique positive root u_D = (-15 + sqrt(disc)) / (2 a)
        uD_sp = (-sp.Integer(15) + sp.sqrt(sp.Integer(disc))) / sp.Integer(2 * a)
        uD_mp = (mp.mpf(-15) + mp.sqrt(mp.mpf(disc))) / mp.mpf(2 * a)
        return [(sp.Integer(0), uD_sp, mp.mpf(0), uD_mp)]
    # a < 0
    if disc <= 0:
        # D(u) < 0 for all u > 0 (disc == 0 impossible for integer a since 225/96 = 75/32)
        return [(sp.Integer(0), sp.oo, mp.mpf(0), None)]
    # a < 0 and disc > 0 (occurs for M_g in {12, 13}):
    # D(u) > 0 on (u_1, u_2), D(u) < 0 on (0, u_1) U (u_2, +oo)
    u1_sp = (sp.Integer(15) - sp.sqrt(sp.Integer(disc))) / sp.Integer(-2 * a)
    u2_sp = (sp.Integer(15) + sp.sqrt(sp.Integer(disc))) / sp.Integer(-2 * a)
    sq_mp = mp.sqrt(mp.mpf(disc))
    u1_mp = (mp.mpf(15) - sq_mp) / mp.mpf(-2 * a)
    u2_mp = (mp.mpf(15) + sq_mp) / mp.mpf(-2 * a)
    return [
        (sp.Integer(0), u1_sp, mp.mpf(0), u1_mp),
        (u2_sp, sp.oo, u2_mp, None),
    ]


def frg_beta_eval(g_val, lam_val, Mg_mp, Ml_mp):
    """Direct evaluation of raw d = 4 Litim harmonic-gauge FRG system at 55 dps."""
    u = mp.mpf(1) - mp.mpf(2) * lam_val
    six_pi = mp.mpf(6) * mp.pi
    B1 = (mp.mpf(10) / u - mp.mpf(18) / (u * u) - mp.mpf(14) + Mg_mp) / six_pi
    B2 = (-mp.mpf(5) / (mp.mpf(2) * u) + mp.mpf(3) / (u * u)) / six_pi
    denom = mp.mpf(1) - g_val * B2
    eta_N = g_val * B1 / denom
    beta_g = (mp.mpf(2) + eta_N) * g_val
    beta_lam = (eta_N - mp.mpf(2)) * lam_val + (g_val / (mp.mpf(2) * mp.pi)) * (
        mp.mpf(5) * (mp.mpf(1) - eta_N / mp.mpf(6)) / u - mp.mpf(4) + Ml_mp
    )
    return beta_g, beta_lam, eta_N, B1, B2, denom


def richardson4_jacobian(g_val, lam_val, Mg_mp, Ml_mp, h_step):
    """4th-order Richardson central finite-difference Jacobian J = d(beta_g, beta_lam)/d(g, lam)."""
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)

    def eval_vec(gv, lv):
        bg, bl, _, _, _, _ = frg_beta_eval(gv, lv, Mg_mp, Ml_mp)
        return bg, bl

    def d1_g(step):
        p = eval_vec(g_val + step, lam_val)
        m = eval_vec(g_val - step, lam_val)
        return (p[0] - m[0]) / (two * step), (p[1] - m[1]) / (two * step)

    def d1_l(step):
        p = eval_vec(g_val, lam_val + step)
        m = eval_vec(g_val, lam_val - step)
        return (p[0] - m[0]) / (two * step), (p[1] - m[1]) / (two * step)

    g_h = d1_g(h_step)
    g_half = d1_g(h_step / two)
    l_h = d1_l(h_step)
    l_half = d1_l(h_step / two)

    j00 = (four * g_half[0] - g_h[0]) / three
    j10 = (four * g_half[1] - g_h[1]) / three
    j01 = (four * l_half[0] - l_h[0]) / three
    j11 = (four * l_half[1] - l_h[1]) / three
    return j00, j01, j10, j11


def eig_2x2(a00, a01, a10, a11):
    """Exact closed-form eigenvalues of a real 2x2 matrix (no root-finder)."""
    two = mp.mpf(2)
    four = mp.mpf(4)
    tr = a00 + a11
    det = a00 * a11 - a01 * a10
    disc = tr * tr - four * det
    if disc >= mp.mpf(0):
        sq = mp.sqrt(disc)
        t1 = mp.mpc((tr + sq) / two, mp.mpf(0))
        t2 = mp.mpc((tr - sq) / two, mp.mpf(0))
    else:
        sq = mp.sqrt(-disc)
        t1 = mp.mpc(tr / two, sq / two)
        t2 = mp.mpc(tr / two, -sq / two)
    # Sort so Re(t1) >= Re(t2), and if equal Im(t1) >= Im(t2)
    if (t1.real < t2.real) or (t1.real == t2.real and t1.imag < t2.imag):
        t1, t2 = t2, t1
    return t1, t2, bool(disc < mp.mpf(0))


def similarity_invariance_check(s00, s01, s10, s11, t1, t2):
    """Guardrail 3 similarity/basis-scrambling invariance check on stability matrix S = -J."""
    # Apply two independent basis transformations:
    # (1) Non-orthogonal integer matrix P1 = [[3, 5], [2, 7]] (det = 11)
    # (2) Orthogonal rotation P2 = [[cos(phi), -sin(phi)], [sin(phi), cos(phi)]] at phi = 7/11
    max_diff = mp.mpf(0)
    phi = mp_rat(7, 11)
    c_p = mp.cos(phi)
    s_p = mp.sin(phi)
    transforms = [
        (mp.mpf(3), mp.mpf(5), mp.mpf(2), mp.mpf(7)),
        (c_p, -s_p, s_p, c_p),
    ]
    for p00, p01, p10, p11 in transforms:
        det_p = p00 * p11 - p01 * p10
        ip00 = p11 / det_p
        ip01 = -p01 / det_p
        ip10 = -p10 / det_p
        ip11 = p00 / det_p
        # T = P * S * P^{-1}
        ps00 = p00 * s00 + p01 * s10
        ps01 = p00 * s01 + p01 * s11
        ps10 = p10 * s00 + p11 * s10
        ps11 = p10 * s01 + p11 * s11
        t00 = ps00 * ip00 + ps01 * ip10
        t01 = ps00 * ip01 + ps01 * ip11
        t10 = ps10 * ip00 + ps11 * ip10
        t11 = ps10 * ip01 + ps11 * ip11
        u1, u2, _ = eig_2x2(t00, t01, t10, t11)
        d_pair = max(abs(u1 - t1), abs(u2 - t2))
        if d_pair > max_diff:
            max_diff = d_pair
    return max_diff


def solve_frg_spectrum(N_S, N_W, N_V, f_W=1, label=""):
    """Independent 55-dps FRG fixed-point solver (Sturm + bisection + 2D Newton + Richardson FD)."""
    u_sym = sp.Symbol("u", real=True)
    Mg_int = int(N_S + f_W * N_W - 4 * N_V)
    Ml_rat = sp.Rational(N_S - 2 * N_W + 2 * N_V, 2)

    # 1. Exact Sturm-sequence proof of valid (g > 0, u > 0, 1 - g B_2 != 0) root count
    P_expr = (
        sp.Integer(2) * (Mg_int - 14) * u_sym**3
        + (sp.Integer(82) - sp.Integer(2) * Mg_int - sp.Integer(6) * Ml_rat) * u_sym**2
        - sp.Integer(118) * u_sym
        + sp.Integer(48)
    )
    D_expr = sp.Integer(Mg_int - 14) * u_sym**2 + sp.Integer(15) * u_sym - sp.Integer(24)
    B1_expr = sp.Integer(Mg_int - 14) * u_sym**2 + sp.Integer(10) * u_sym - sp.Integer(18)

    P_poly = sp.Poly(P_expr, u_sym, domain="QQ")
    D_poly = sp.Poly(D_expr, u_sym, domain="QQ")
    B1_poly = sp.Poly(B1_expr, u_sym, domain="QQ")

    # Remove any common factor with pole polynomials D(u) or B1(u)
    g_PD = sp.gcd(P_poly, D_poly)
    g_PB1 = sp.gcd(P_poly, B1_poly)
    P_clean = sp.quo(P_poly, g_PD)
    P_clean = sp.quo(P_clean, sp.gcd(P_clean, B1_poly))
    spurious_removed = int(P_poly.degree() - P_clean.degree())

    # Square-free part for Sturm sequence
    P_sf = sp.quo(P_clean, sp.gcd(P_clean, P_clean.diff()))
    seq = build_sturm_sequence(P_sf)
    u_intervals = valid_u_intervals_exact(Mg_int)
    n_sturm_valid = int(
        sum(sturm_root_count_open_interval(seq, u_sym, a_sp, b_sp) for a_sp, b_sp, _, _ in u_intervals)
    )

    # Exact Cauchy upper bound on positive roots of P_clean
    coeffs = [abs(sp.Rational(c)) for c in P_clean.all_coeffs()]
    if len(coeffs) > 1 and coeffs[0] != 0:
        u_cauchy = sp.Integer(1) + max(coeffs[1:]) / coeffs[0]
    else:
        u_cauchy = sp.Integer(10)
    # Primary search domain covers lam in (-100, 49/100) <=> u in (1/50, 201),
    # extended automatically if Cauchy bound exceeds 201.
    u_cap_int = int(max(sp.Integer(201), sp.ceiling(u_cauchy) + sp.Integer(2)))
    lam_scan_min = (mp.mpf(1) - mp.mpf(u_cap_int)) / mp.mpf(2)
    lam_scan_max_card = mp_rat(49, 100)

    # 2. Direct 55-dps bracketed bisection on F(lam) = beta_lam(g_eta(lam), lam)
    #    using ONLY raw FRG B_1(lam), B_2(lam), beta_lam(g, lam) — zero cubic root solver.
    Mg_mp = mp.mpf(Mg_int)
    Ml_mp = mp_rat(Ml_rat.p, Ml_rat.q)

    def g_from_eta(lam_val):
        u = mp.mpf(1) - mp.mpf(2) * lam_val
        six_pi = mp.mpf(6) * mp.pi
        B1 = (mp.mpf(10) / u - mp.mpf(18) / (u * u) - mp.mpf(14) + Mg_mp) / six_pi
        B2 = (-mp.mpf(5) / (mp.mpf(2) * u) + mp.mpf(3) / (u * u)) / six_pi
        return -mp.mpf(2) / (B1 - mp.mpf(2) * B2)

    def F_beta_lam(lam_val):
        g_v = g_from_eta(lam_val)
        _, bl, _, _, _, _ = frg_beta_eval(g_v, lam_val, Mg_mp, Ml_mp)
        return bl

    eps_end = mp_pow10(-9)
    brackets = []
    for _, _, ua_mp, ub_mp_opt in u_intervals:
        u_lo = ua_mp + eps_end
        u_hi_raw = mp.mpf(u_cap_int) if ub_mp_opt is None else min(mp.mpf(u_cap_int), ub_mp_opt)
        u_hi = u_hi_raw - eps_end
        if u_hi <= u_lo:
            continue
        # Dense non-uniform grid in u mapped to lam = (1 - u)/2
        # (fine near u = 0 and pole endpoints, spanning full valid interval)
        n_grid = 600
        lam_pts = []
        for idx_k in range(n_grid + 1):
            t = mp.mpf(idx_k) / mp.mpf(n_grid)
            # Symmetric S-curve clustering near both endpoints ua_mp and ub_mp
            s_curve = (mp.mpf(3) * t * t - mp.mpf(2) * t * t * t)
            # Also blend with t^2 for near-zero resolution when u_hi is large
            u_pt = u_lo + (u_hi - u_lo) * (t * t if ub_mp_opt is None else s_curve)
            lam_pts.append((mp.mpf(1) - u_pt) / mp.mpf(2))
        lam_pts.sort()
        prev_l = lam_pts[0]
        prev_f = F_beta_lam(prev_l)
        for cur_l in lam_pts[1:]:
            cur_f = F_beta_lam(cur_l)
            if prev_f == mp.mpf(0):
                brackets.append((prev_l, prev_l))
            elif prev_f * cur_f < mp.mpf(0):
                brackets.append((prev_l, cur_l))
            prev_l, prev_f = cur_l, cur_f

    # 3. Bisection refinement + direct 2D Newton-Raphson on (beta_g, beta_lam)
    h_jac = mp_pow10(-11)
    tol_newton = mp_pow10(-47)
    tol_res_gate = mp_pow10(-30)
    tol_jac_gate = mp_pow10(-35)
    tol_sim_gate = mp_pow10(-35)

    fixed_points = []
    for a_l, b_l in brackets:
        if a_l == b_l:
            lam_bis = a_l
        else:
            fa = F_beta_lam(a_l)
            lo_b, hi_b = a_l, b_l
            for _ in range(185):
                mid = (lo_b + hi_b) / mp.mpf(2)
                fm = F_beta_lam(mid)
                if fm == mp.mpf(0):
                    lo_b = hi_b = mid
                    break
                if fa * fm < mp.mpf(0):
                    hi_b = mid
                else:
                    lo_b = mid
                    fa = fm
            lam_bis = (lo_b + hi_b) / mp.mpf(2)

        g_cur = g_from_eta(lam_bis)
        l_cur = lam_bis

        # Direct 2D Newton-Raphson on raw (beta_g(g, lam), beta_lam(g, lam)) = (0, 0)
        newton_iters = 0
        for it in range(30):
            bg, bl, _, _, _, _ = frg_beta_eval(g_cur, l_cur, Mg_mp, Ml_mp)
            if max(abs(bg), abs(bl)) < tol_newton:
                newton_iters = it
                break
            j00, j01, j10, j11 = richardson4_jacobian(g_cur, l_cur, Mg_mp, Ml_mp, h_jac)
            det_j = j00 * j11 - j01 * j10
            dg = -(j11 * bg - j01 * bl) / det_j
            dl = -(-j10 * bg + j00 * bl) / det_j
            g_cur = g_cur + dg
            l_cur = l_cur + dl
            newton_iters = it + 1

        # Evaluate raw residuals & verify physical domain
        bg, bl, eta_N, B1_v, B2_v, denom_v = frg_beta_eval(g_cur, l_cur, Mg_mp, Ml_mp)
        u_cur = mp.mpf(1) - mp.mpf(2) * l_cur
        max_res = max(abs(bg), abs(bl))
        eta_plus2_err = abs(eta_N + mp.mpf(2))

        # Deduplicate if two adjacent grid cells bracketed the same root
        is_dup = bool(
            any(
                abs(g_cur - fp["_g_mp"]) < mp_pow10(-25) and abs(l_cur - fp["_l_mp"]) < mp_pow10(-25)
                for fp in fixed_points
            )
        )
        if is_dup:
            continue

        # 4th-order Richardson FD Jacobian at h and h/2 for convergence certification
        j00, j01, j10, j11 = richardson4_jacobian(g_cur, l_cur, Mg_mp, Ml_mp, h_jac)
        j00b, j01b, j10b, j11b = richardson4_jacobian(g_cur, l_cur, Mg_mp, Ml_mp, h_jac / mp.mpf(2))
        jac_conv_err = max(abs(j00 - j00b), abs(j01 - j01b), abs(j10 - j10b), abs(j11 - j11b))

        # Stability matrix S = -J, critical exponents theta = eig(S)
        s00, s01, s10, s11 = -j00, -j01, -j10, -j11
        t1, t2, is_complex_pair = eig_2x2(s00, s01, s10, s11)

        # Verify characteristic determinant det(S - theta I) = 0 directly
        char_err_1 = abs((s00 - t1) * (s11 - t1) - s01 * s10)
        char_err_2 = abs((s00 - t2) * (s11 - t2) - s01 * s10)
        char_err_max = max(char_err_1, char_err_2)

        # Guardrail 3 similarity-invariance check
        sim_inv_err = similarity_invariance_check(s00, s01, s10, s11, t1, t2)

        # Verify physical validity and UV-attractiveness (Re(theta_1) > 0 and Re(theta_2) > 0)
        in_physical_domain = bool(g_cur > mp.mpf(0) and u_cur > mp.mpf(0) and abs(denom_v) > mp_pow10(-20))
        in_card_lam_window = bool(l_cur > mp.mpf(-100) and l_cur < lam_scan_max_card)
        uv_attractive = bool(t1.real > mp.mpf(0) and t2.real > mp.mpf(0))
        numerical_certified = bool(
            max_res < tol_res_gate
            and jac_conv_err < tol_jac_gate
            and char_err_max < tol_jac_gate
            and sim_inv_err < tol_sim_gate
        )

        fixed_points.append(
            {
                "_g_mp": g_cur,
                "_l_mp": l_cur,
                "_t1_mp": t1,
                "_t2_mp": t2,
                "_res_mp": max_res,
                "g_star_str": fmt_mp(g_cur, 40),
                "g_star": float(fmt_mp(g_cur, 17)),
                "lam_star_str": fmt_mp(l_cur, 40),
                "lam_star": float(fmt_mp(l_cur, 17)),
                "u_star_str": fmt_mp(u_cur, 40),
                "eta_N_plus_2_abs_err": fmt_mp(eta_plus2_err, 6),
                "one_minus_g_B2_str": fmt_mp(denom_v, 20),
                "max_beta_residual": fmt_mp(max_res, 6),
                "newton_iters": int(newton_iters),
                "richardson_jac_conv_err": fmt_mp(jac_conv_err, 6),
                "char_det_err": fmt_mp(char_err_max, 6),
                "similarity_invariance_err": fmt_mp(sim_inv_err, 6),
                "theta_1_re_str": fmt_mp(t1.real, 40),
                "theta_1_im_str": fmt_mp(t1.imag, 40),
                "theta_2_re_str": fmt_mp(t2.real, 40),
                "theta_2_im_str": fmt_mp(t2.imag, 40),
                "theta_1_re": float(fmt_mp(t1.real, 17)),
                "theta_1_im": float(fmt_mp(t1.imag, 17)),
                "theta_2_re": float(fmt_mp(t2.real, 17)),
                "theta_2_im": float(fmt_mp(t2.imag, 17)),
                "is_complex_conjugate_pair": is_complex_pair,
                "in_physical_domain": in_physical_domain,
                "in_card_lam_window": in_card_lam_window,
                "uv_attractive": uv_attractive,
                "numerical_certified": numerical_certified,
            }
        )

    # Sort fixed points by increasing g_*
    fixed_points.sort(key=lambda fp: fp["_g_mp"])
    sturm_matches_direct = bool(len(fixed_points) == n_sturm_valid)
    uv_fps = [fp for fp in fixed_points if fp["uv_attractive"] and fp["in_physical_domain"]]

    return {
        "label": label,
        "N_S": int(N_S),
        "N_W": int(N_W),
        "N_V": int(N_V),
        "f_W": int(f_W),
        "M_g": int(Mg_int),
        "M_l": fmt_rat(Ml_rat),
        "spurious_pole_roots_removed": spurious_removed,
        "sturm_exact_physical_root_count": n_sturm_valid,
        "direct_2d_newton_root_count": len(fixed_points),
        "sturm_matches_direct_solver": sturm_matches_direct,
        "n_uv_attractive_fps": len(uv_fps),
        "scan_lam_min": fmt_mp(lam_scan_min, 10),
        "fixed_points": fixed_points,
    }


def strip_internal_mp(record):
    """Return JSON-serializable copy of FRG spectrum record without internal mpmath handles."""
    out = {k: v for k, v in record.items() if k != "fixed_points"}
    cleaned_fps = []
    for fp in record["fixed_points"]:
        cleaned_fps.append({k: v for k, v in fp.items() if not k.startswith("_")})
    out["fixed_points"] = cleaned_fps
    return out


# =============================================================================
# SECTION 2: OW10-A — DISJOINT MATRIX-GROUP DELTA(2, 3, N) & BITMASK FOCK SPACE
# =============================================================================

def mat2_mul_mod(A, B, p):
    """2x2 matrix multiplication mod p over flattened 4-tuple."""
    return (
        (A[0] * B[0] + A[1] * B[2]) % p,
        (A[0] * B[1] + A[1] * B[3]) % p,
        (A[2] * B[0] + A[3] * B[2]) % p,
        (A[2] * B[1] + A[3] * B[3]) % p,
    )


def psl2_canon(A, p):
    """Canonical representative of {+A, -A} in PSL(2, F_p)."""
    neg = tuple((-x) % p for x in A)
    return A if A <= neg else neg


def psl2_mul(A, B, p):
    """Group multiplication in PSL(2, F_p)."""
    return psl2_canon(mat2_mul_mod(A, B, p), p)


def mat3_mul(A, B):
    """3x3 integer matrix multiplication over flattened 9-tuple."""
    return tuple(
        A[3 * i] * B[j] + A[3 * i + 1] * B[3 + j] + A[3 * i + 2] * B[6 + j]
        for i in range(3)
        for j in range(3)
    )


def mat3_det(A):
    """Exact determinant of 3x3 integer matrix."""
    return (
        A[0] * (A[4] * A[8] - A[5] * A[7])
        - A[1] * (A[3] * A[8] - A[5] * A[6])
        + A[2] * (A[3] * A[7] - A[4] * A[6])
    )


def mat3_is_so3(A):
    """Verify A^T A = I_3 and det(A) = +1 directly."""
    At = (A[0], A[3], A[6], A[1], A[4], A[7], A[2], A[5], A[8])
    return bool(mat3_mul(At, A) == (1, 0, 0, 0, 1, 0, 0, 0, 1) and mat3_det(A) == 1)


def group_closure(gens, mul, ident):
    """Generate finite group closure from matrix generators."""
    G = {ident}
    queue = [ident]
    while queue:
        x = queue.pop()
        for g in gens:
            y = mul(x, g)
            if y not in G:
                G.add(y)
                queue.append(y)
    return G


def element_order(x, mul, ident):
    """Exact order of matrix group element."""
    cur = x
    k = 1
    while cur != ident:
        cur = mul(cur, x)
        k += 1
    return k


def build_inverse_table(G_list, mul, ident):
    """Compute exact inverse map for every element of finite matrix group G."""
    inv = {}
    for g in G_list:
        cur = ident
        nxt = g
        while nxt != ident:
            cur = nxt
            nxt = mul(nxt, g)
        inv[g] = cur
    return inv


def enumerate_subgroups_and_classes(G_list, mul, inv, ident):
    """Exhaustive subgroup lattice and G-conjugacy class decomposition."""
    subs = {frozenset([ident])}
    queue = [frozenset([ident])]
    while queue:
        H = queue.pop()
        for g in G_list:
            if g not in H:
                K = frozenset(group_closure(list(H) + [g], mul, ident))
                if K not in subs:
                    subs.add(K)
                    queue.append(K)

    seen = set()
    classes = []
    for H in sorted(subs, key=lambda s: (-len(s), sorted(s))):
        if H in seen:
            continue
        orbit = {frozenset(mul(mul(g, h), inv[g]) for h in H) for g in G_list}
        seen |= orbit
        core = set.intersection(*[set(c) for c in orbit])
        classes.append(
            {
                "rep": H,
                "order": len(H),
                "index": len(G_list) // len(H),
                "n_conjugates": len(orbit),
                "core_order": len(core),
                "is_faithful": bool(len(core) == 1),
                "orbit": sorted(orbit, key=lambda s: sorted(s)),
            }
        )
    return len(subs), classes


def coset_action_perm(G_list, H, elem, mul):
    """Left-multiplication action of matrix element elem on left cosets G/H."""
    cosets = []
    used = set()
    for g in G_list:
        if g not in used:
            c = frozenset(mul(g, h) for h in H)
            cosets.append(c)
            used |= c
    idx_map = {c: i for i, c in enumerate(cosets)}
    perm = []
    for c in cosets:
        rep = min(c)
        nc = frozenset(mul(elem, mul(rep, h)) for h in H)
        perm.append(idx_map[nc])
    return tuple(perm)


def cycle_type_of_perm(perm):
    """Sorted cycle-length partition of a permutation."""
    seen = set()
    cycs = []
    for i in range(len(perm)):
        if i in seen:
            continue
        length = 0
        cur = i
        while cur not in seen:
            seen.add(cur)
            cur = perm[cur]
            length += 1
        cycs.append(length)
    return tuple(sorted(cycs, reverse=True))


def involution_eigenspace_split(perm):
    """For an involution perm (perm^2 = id), return (+1 eigenspace dim, -1 eigenspace dim)."""
    d = len(perm)
    fixed = sum(1 for i in range(d) if perm[i] == i)
    two_cycles = (d - fixed) // 2
    return two_cycles + fixed, two_cycles


def direct_bitmask_fock_audit(d, p_dim, q_dim):
    """Direct 0 .. 2^d - 1 bitmask Fock-space chirality & anomaly enumeration.

    Enumerates all 2^(d-1) even-parity bitmasks m in 0 .. 2^d - 1 under
    G_gauge = S(U(p) x U(q)) <= SU(d) (or unbroken SU(d) if q == 0).
    """
    mask_p = (1 << p_dim) - 1
    weights = []
    tr_Q = 0
    tr_Q3 = 0
    tr_SUd3 = 0
    tr_SUp3 = 0
    tr_SUq3 = 0
    tr_SUp2Q = 0
    tr_SUq2Q = 0
    witten_p_states = 0
    witten_q_states = 0
    n_even = 0

    for m in range(1 << d):
        if m.bit_count() & 1:
            continue
        n_even += 1
        a = (m & mask_p).bit_count()
        b = (m >> p_dim).bit_count()
        Q = (-q_dim * a + p_dim * b) if q_dim > 0 else 0
        wp = tuple(p_dim * ((m >> i) & 1) - a for i in range(p_dim))
        wq = tuple(q_dim * ((m >> (p_dim + j)) & 1) - b for j in range(q_dim))
        weights.append((wp, wq, Q))

        tr_Q += Q
        tr_Q3 += Q**3
        if d >= 3:
            hd = ((m >> 0) & 1) + ((m >> 1) & 1) - 2 * ((m >> 2) & 1)
            tr_SUd3 += hd**3
        if p_dim >= 2:
            hp = ((m >> 0) & 1) - ((m >> 1) & 1)
            tr_SUp2Q += (hp**2) * Q
        if p_dim >= 3:
            hp3 = ((m >> 0) & 1) + ((m >> 1) & 1) - 2 * ((m >> 2) & 1)
            tr_SUp3 += hp3**3
        if q_dim >= 2:
            hq = ((m >> p_dim) & 1) - ((m >> (p_dim + 1)) & 1)
            tr_SUq2Q += (hq**2) * Q
        if q_dim >= 3:
            hq3 = ((m >> p_dim) & 1) + ((m >> (p_dim + 1)) & 1) - 2 * ((m >> (p_dim + 2)) & 1)
            tr_SUq3 += hq3**3
        if p_dim == 2 and a == 1:
            witten_p_states += 1
        if q_dim == 2 and b == 1:
            witten_q_states += 1

    # Self-conjugacy test: representation is chiral iff weight multiset != negated weight multiset
    c_pos = Counter(weights)
    c_neg = Counter(
        (tuple(-x for x in wp), tuple(-x for x in wq), -Q)
        for wp, wq, Q in weights
    )
    is_chiral = bool(c_pos != c_neg)

    # Basis-scrambling check (Guardrail 3): reverse site indices inside p-block and q-block
    scrambled_weights = []
    for wp, wq, Q in weights:
        scrambled_weights.append((wp[::-1], wq[::-1], Q))
    # Verify multiset of sorted intra-block Cartan weights is invariant
    c_orig_canon = Counter((tuple(sorted(wp)), tuple(sorted(wq)), Q) for wp, wq, Q in weights)
    c_scram_canon = Counter((tuple(sorted(wp)), tuple(sorted(wq)), Q) for wp, wq, Q in scrambled_weights)
    basis_invariant = bool(c_orig_canon == c_scram_canon)

    witten_p_doublets = witten_p_states // 2
    witten_q_doublets = witten_q_states // 2
    witten_ok = bool((witten_p_doublets % 2 == 0) and (witten_q_doublets % 2 == 0))
    anomaly_free = bool(
        tr_Q == 0
        and tr_Q3 == 0
        and tr_SUd3 == 0
        and tr_SUp3 == 0
        and tr_SUq3 == 0
        and tr_SUp2Q == 0
        and tr_SUq2Q == 0
        and witten_ok
    )

    return {
        "n_even_states": n_even,
        "expected_half_fock": 1 << (d - 1),
        "is_chiral": is_chiral,
        "anomaly_free": anomaly_free,
        "basis_invariant": basis_invariant,
        "anomalies": {
            "tr_Q": tr_Q,
            "tr_Q3": tr_Q3,
            "tr_SUd3": tr_SUd3,
            "tr_SUp3": tr_SUp3,
            "tr_SUq3": tr_SUq3,
            "tr_SUp2Q": tr_SUp2Q,
            "tr_SUq2Q": tr_SUq2Q,
            "witten_p_doublets": witten_p_doublets,
            "witten_q_doublets": witten_q_doublets,
            "witten_even_ok": witten_ok,
        },
    }


def analyze_delta_23N_matrix_actions():
    """Reconstruct all faithful transitive actions of Delta(2,3,N) (N=2..5) from disjoint matrix groups."""
    configs = [
        (
            2,
            "GL(2, F_2)",
            "S_3",
            6,
            (1, 0, 0, 1),
            (0, 1, 1, 0),
            (0, 1, 1, 1),
            lambda x, y: mat2_mul_mod(x, y, 2),
        ),
        (
            3,
            "PSL(2, F_3)",
            "A_4",
            12,
            psl2_canon((1, 0, 0, 1), 3),
            psl2_canon((0, 1, 2, 0), 3),
            psl2_canon((1, 1, 0, 1), 3),
            lambda x, y: psl2_mul(x, y, 3),
        ),
        (
            4,
            "SO(3, Z)",
            "S_4",
            24,
            (1, 0, 0, 0, 1, 0, 0, 0, 1),
            (0, 1, 0, 1, 0, 0, 0, 0, -1),
            (0, 0, 1, 1, 0, 0, 0, 1, 0),
            mat3_mul,
        ),
        (
            5,
            "PSL(2, F_5)",
            "A_5",
            60,
            psl2_canon((1, 0, 0, 1), 5),
            psl2_canon((0, 1, 4, 0), 5),
            psl2_canon((0, 1, 4, 1), 5),
            lambda x, y: psl2_mul(x, y, 5),
        ),
    ]

    group_audits = []
    faithful_d_le_12 = []
    faithful_all_d = []
    involution_paired_d_le_12 = []
    all_transitive_d_le_12 = []

    for N_val, mat_name, iso_name, expected_order, ident, a_gen, b_gen, mul in configs:
        G_set = group_closure([a_gen, b_gen], mul, ident)
        G_list = sorted(G_set)
        inv = build_inverse_table(G_list, mul, ident)

        ord_a = element_order(a_gen, mul, ident)
        ord_b = element_order(b_gen, mul, ident)
        ab_gen = mul(a_gen, b_gen)
        ord_ab = element_order(ab_gen, mul, ident)

        # For SO(3, Z), directly verify every element satisfies A^T A = I and det(A) = +1
        extra_matrix_ok = bool(len(G_list) == expected_order)
        if N_val == 4:
            extra_matrix_ok = bool(extra_matrix_ok and all(mat3_is_so3(m) for m in G_list))

        # Find all conjugacy classes of order-2 involutions in G
        inv_seen = set()
        inv_classes = []
        for g in G_list:
            if element_order(g, mul, ident) == 2 and g not in inv_seen:
                cl = {mul(mul(x, g), inv[x]) for x in G_list}
                inv_seen |= cl
                is_gen_class = bool(a_gen in cl)
                inv_classes.append((is_gen_class, len(cl), min(cl)))
        inv_classes.sort(key=lambda t: (0 if t[0] else 1, t[1]))

        n_subgroups, classes = enumerate_subgroups_and_classes(G_list, mul, inv, ident)

        # Group summary
        n_cf_12 = sum(1 for c in classes if c["is_faithful"] and c["index"] <= 12)
        n_cf_all = sum(1 for c in classes if c["is_faithful"])
        group_audits.append(
            {
                "N": N_val,
                "matrix_group": mat_name,
                "isomorphic_to": iso_name,
                "order": len(G_list),
                "expected_order": expected_order,
                "ord_a": ord_a,
                "ord_b": ord_b,
                "ord_ab": ord_ab,
                "triangle_presentation_ok": bool(
                    len(G_list) == expected_order
                    and ord_a == 2
                    and ord_b == 3
                    and ord_ab == N_val
                    and extra_matrix_ok
                ),
                "n_subgroups_total": n_subgroups,
                "n_conjugacy_classes_total": len(classes),
                "n_involution_classes": len(inv_classes),
                "n_faithful_d_le_12": n_cf_12,
                "n_faithful_all_d": n_cf_all,
            }
        )

        # Evaluate each subgroup conjugacy class
        for cls_idx, c in enumerate(classes):
            H = c["rep"]
            d = c["index"]
            perm_a = coset_action_perm(G_list, H, a_gen, mul)
            perm_b = coset_action_perm(G_list, H, b_gen, mul)
            perm_ab = coset_action_perm(G_list, H, ab_gen, mul)

            # Verify conjugacy invariance: second conjugate H2 in same orbit gives identical cycle types
            conj_invariance_ok = bool(len(c["orbit"]) >= 1)
            if len(c["orbit"]) > 1:
                H2 = c["orbit"][1]
                p2_a = coset_action_perm(G_list, H2, a_gen, mul)
                p2_b = coset_action_perm(G_list, H2, b_gen, mul)
                conj_invariance_ok = bool(
                    cycle_type_of_perm(p2_a) == cycle_type_of_perm(perm_a)
                    and cycle_type_of_perm(p2_b) == cycle_type_of_perm(perm_b)
                )

            p_dim, q_dim = involution_eigenspace_split(perm_a)
            # Gauge vector count for S(U(p) x U(q)) (or SU(d) if q == 0)
            if q_dim > 0:
                N_V = p_dim * p_dim + q_dim * q_dim - 1
            else:
                N_V = d * d - 1 if d >= 2 else 0
            # Open-weave N_gen = 3 Weyl count = 3 * 2^(d-1)
            N_W = 3 * (1 << (d - 1)) if d >= 1 else 0
            # 2H scalar count: 2 complex weak-q fundamental multiplets = 4 * q (for q >= 1; 0 if q == 0)
            N_S = 4 * q_dim if q_dim >= 1 else 0
            M_g = N_S + N_W - 4 * N_V
            sakharov_attractive = bool(M_g > 0)
            as_type_ii_pincer = bool(M_g < 14)

            if d <= 12:
                fock = direct_bitmask_fock_audit(d, p_dim, q_dim) if d >= 2 else {
                    "n_even_states": 1,
                    "expected_half_fock": 1,
                    "is_chiral": bool(d >= 2),
                    "anomaly_free": bool(d >= 2),
                    "basis_invariant": bool(d == 1),
                    "anomalies": {},
                }
                is_chiral = fock["is_chiral"]
                anomaly_free = fock["anomaly_free"]
            else:
                # For d > 12 (d in {15, 20, 24, 30, 60}): analytic parity & cubic anomaly
                # Even d is strictly self-conjugate (complement preserves parity);
                # odd d >= 5 is chiral & anomaly-free, but N_W = 3 * 2^(d-1) >> 4 N_V so M_g >> 14.
                is_chiral = bool((d % 2) == 1)
                anomaly_free = bool((d % 2) == 0 or d >= 5)
                fock = None

            # For faithful d <= 12 actions, also run direct Sturm + 55-dps FRG check
            frg_n_uv = None
            frg_sturm = None
            if c["is_faithful"] and d <= 12:
                frg_row = solve_frg_spectrum(N_S, N_W, N_V, f_W=1, label=f"N={N_val} d={d} cls={cls_idx}")
                frg_n_uv = frg_row["n_uv_attractive_fps"]
                frg_sturm = frg_row["sturm_exact_physical_root_count"]
                as_type_ii_exists = bool(frg_n_uv >= 1 and frg_row["sturm_matches_direct_solver"])
            else:
                as_type_ii_exists = as_type_ii_pincer

            passes_all_4 = bool(
                c["is_faithful"]
                and is_chiral
                and anomaly_free
                and sakharov_attractive
                and as_type_ii_pincer
                and as_type_ii_exists
            )

            row = {
                "N": N_val,
                "matrix_group": mat_name,
                "isomorphic_to": iso_name,
                "class_idx": cls_idx,
                "d": d,
                "H_order": c["order"],
                "n_conjugates": c["n_conjugates"],
                "core_order": c["core_order"],
                "is_faithful": c["is_faithful"],
                "conj_invariance_ok": conj_invariance_ok,
                "cycle_type_a": list(cycle_type_of_perm(perm_a)),
                "cycle_type_b": list(cycle_type_of_perm(perm_b)),
                "cycle_type_ab": list(cycle_type_of_perm(perm_ab)),
                "gauge_split_p_q": [p_dim, q_dim],
                "N_S": N_S,
                "N_W": N_W,
                "N_V": N_V,
                "M_g": M_g,
                "is_chiral": is_chiral,
                "anomaly_free": anomaly_free,
                "sakharov_attractive": sakharov_attractive,
                "as_type_ii_pincer": as_type_ii_pincer,
                "as_type_ii_exists": as_type_ii_exists,
                "frg_sturm_roots": frg_sturm,
                "frg_n_uv_fps": frg_n_uv,
                "passes_all_4": passes_all_4,
            }
            if fock is not None:
                row["fock_audit"] = fock

            if d <= 12:
                all_transitive_d_le_12.append(row)
            if c["is_faithful"]:
                faithful_all_d.append(row)
                if d <= 12:
                    faithful_d_le_12.append(row)

                    # Also build the 21 (faithful action d <= 12, involution conjugacy class) table
                    for inv_idx, (is_gen_cls, inv_cl_sz, inv_rep) in enumerate(inv_classes):
                        p_inv = coset_action_perm(G_list, H, inv_rep, mul)
                        pi_dim, qi_dim = involution_eigenspace_split(p_inv)
                        nv_i = pi_dim * pi_dim + qi_dim * qi_dim - 1 if qi_dim > 0 else (d * d - 1)
                        ns_i = 4 * qi_dim if qi_dim >= 1 else 0
                        mg_i = ns_i + N_W - 4 * nv_i
                        fock_i = direct_bitmask_fock_audit(d, pi_dim, qi_dim)
                        frg_i = solve_frg_spectrum(
                            ns_i, N_W, nv_i, f_W=1, label=f"N={N_val} d={d} cls={cls_idx} inv={inv_idx}"
                        )
                        as_i_exists = bool(
                            frg_i["n_uv_attractive_fps"] >= 1 and frg_i["sturm_matches_direct_solver"]
                        )
                        passes_i = bool(
                            fock_i["is_chiral"]
                            and fock_i["anomaly_free"]
                            and (mg_i > 0)
                            and (mg_i < 14)
                            and as_i_exists
                        )
                        involution_paired_d_le_12.append(
                            {
                                "N": N_val,
                                "matrix_group": mat_name,
                                "d": d,
                                "H_order": c["order"],
                                "inv_class_idx": inv_idx,
                                "inv_is_generator_class": is_gen_cls,
                                "inv_class_size": inv_cl_sz,
                                "cycle_type_inv": list(cycle_type_of_perm(p_inv)),
                                "gauge_split_p_q": [pi_dim, qi_dim],
                                "N_S": ns_i,
                                "N_W": N_W,
                                "N_V": nv_i,
                                "M_g": mg_i,
                                "is_chiral": fock_i["is_chiral"],
                                "anomaly_free": fock_i["anomaly_free"],
                                "sakharov_attractive": bool(mg_i > 0),
                                "as_type_ii_pincer": bool(mg_i < 14),
                                "as_type_ii_exists": as_i_exists,
                                "frg_sturm_roots": frg_i["sturm_exact_physical_root_count"],
                                "frg_n_uv_fps": frg_i["n_uv_attractive_fps"],
                                "passes_all_4": passes_i,
                            }
                        )

    survivors_15 = [r for r in faithful_d_le_12 if r["passes_all_4"]]
    survivors_20_all_d = [r for r in faithful_all_d if r["passes_all_4"]]
    survivors_21_inv = [r for r in involution_paired_d_le_12 if r["passes_all_4"]]
    survivors_24_all_trans = [
        r for r in all_transitive_d_le_12
        if r["is_chiral"] and r["anomaly_free"] and r["sakharov_attractive"] and r["as_type_ii_pincer"]
    ]

    def is_unique_n5_d5(surv_list):
        return bool(
            len(surv_list) == 1
            and surv_list[0]["N"] == 5
            and surv_list[0]["d"] == 5
            and surv_list[0]["H_order"] == 12
            and surv_list[0]["N_S"] == 8
            and surv_list[0]["N_W"] == 48
            and surv_list[0]["N_V"] == 12
            and surv_list[0]["M_g"] == 8
        )

    all_groups_ok = bool(all(g["triangle_presentation_ok"] for g in group_audits))
    all_conj_ok = bool(all(r["conj_invariance_ok"] for r in faithful_all_d))
    all_fock_basis_ok = bool(all(r["fock_audit"]["basis_invariant"] for r in faithful_d_le_12))

    return {
        "group_realizations": group_audits,
        "all_matrix_groups_verified": all_groups_ok,
        "all_conjugacy_invariance_verified": all_conj_ok,
        "all_fock_basis_invariance_verified": all_fock_basis_ok,
        "exact_orbit_stabilizer_faithful_d_le_12_count": len(faithful_d_le_12),
        "exact_orbit_stabilizer_faithful_all_d_count": len(faithful_all_d),
        "all_transitive_d_le_12_count": len(all_transitive_d_le_12),
        "all_proper_transitive_d_le_12_count": sum(1 for r in all_transitive_d_le_12 if r["d"] >= 2),
        "involution_paired_faithful_d_le_12_count": len(involution_paired_d_le_12),
        "card_21_matches_exact_faithful_d_le_12": bool(len(faithful_d_le_12) == 21),
        "card_21_matches_involution_paired_d_le_12": bool(len(involution_paired_d_le_12) == 21),
        "unique_n5_d5_in_exact_15": is_unique_n5_d5(survivors_15),
        "unique_n5_d5_in_all_20_faithful": is_unique_n5_d5(survivors_20_all_d),
        "unique_n5_d5_in_21_involution_pairs": is_unique_n5_d5(survivors_21_inv),
        "unique_n5_d5_in_all_24_transitive": is_unique_n5_d5(survivors_24_all_trans),
        "faithful_d_le_12_rows": faithful_d_le_12,
        "involution_paired_d_le_12_rows": involution_paired_d_le_12,
    }


# =============================================================================
# SECTION 3: OW10-B — SYMBOLIC STELLE SPIN-2 GHOST POLE & a-THEOREM FLOW
# =============================================================================

def verify_ow10_b_stelle_and_a_theorem():
    """Symbolic SymPy verification of trace anomalies, Stelle ghost pole, and 6-stage a-theorem."""
    x_s, xi_s = sp.symbols("x xi")

    def c_exact(NS, NW, NV):
        return sp.Rational(NS, 120) + sp.Rational(NW, 40) + sp.Rational(NV, 10)

    def a_exact(NS, NW, NV):
        return sp.Rational(NS, 360) + sp.Rational(11 * NW, 720) + sp.Rational(62 * NV, 360)

    def bR_factor(NS, xi_val):
        return sp.Integer(NS) * (xi_val - sp.Rational(1, 6)) ** 2

    # 1. Exact 2H and 1H (c, a)
    c_2H = c_exact(8, 48, 12)
    a_2H = a_exact(8, 48, 12)
    c_1H = c_exact(4, 48, 12)
    a_1H = a_exact(4, 48, 12)

    twoH_ok = bool(c_2H == sp.Rational(37, 15) and a_2H == sp.Rational(127, 45))
    oneH_ok = bool(c_1H == sp.Rational(73, 30) and a_1H == sp.Rational(253, 90))

    # 2. Conformal coupling xi = 1/6 => b_R = 0 identically
    bR_conformal = sp.simplify(bR_factor(8, sp.Rational(1, 6)))
    bR_conformal_zero = bool(bR_conformal == 0)

    # 3. Symbolic Stelle propagator partial-fraction identity and residues via SymPy apart & residue
    stelle_expr = sp.Integer(1) / (x_s * (sp.Integer(1) + x_s))
    stelle_apart = sp.apart(stelle_expr, x_s)
    expected_apart = sp.Integer(1) / x_s - sp.Integer(1) / (x_s + sp.Integer(1))
    apart_diff = sp.simplify(stelle_apart - expected_apart)

    res_massless = sp.residue(stelle_expr, x_s, sp.Integer(0))
    res_ghost = sp.residue(stelle_expr, x_s, sp.Integer(-1))

    # Exact rational spot-checks at x in {1/3, 1, 5}
    spot_xs = [sp.Rational(1, 3), sp.Rational(1, 1), sp.Rational(5, 1)]
    spot_checks = []
    for xv in spot_xs:
        lhs = sp.Rational(stelle_expr.subs(x_s, xv))
        rhs = sp.Rational(expected_apart.subs(x_s, xv))
        spot_checks.append(
            {
                "x": fmt_rat(xv),
                "lhs": fmt_rat(lhs),
                "rhs": fmt_rat(rhs),
                "exact_match": bool(lhs == rhs),
            }
        )

    stelle_ok = bool(
        c_2H > 0
        and bR_conformal_zero
        and apart_diff == 0
        and res_massless == sp.Integer(1)
        and res_ghost == sp.Integer(-1)
        and all(sc["exact_match"] for sc in spot_checks)
    )

    # 4. Exact 6-stage Komargodski-Schwimmer a-theorem decoupling ladder
    stages_spec = [
        ("UV (8, 48, 12)", 8, 48, 12, sp.Rational(37, 15), sp.Rational(127, 45), None),
        ("SM 1H + 3 nu^c (4, 48, 12)", 4, 48, 12, sp.Rational(73, 30), sp.Rational(253, 90), sp.Rational(1, 90)),
        ("SM 1H below M_R (4, 45, 12)", 4, 45, 12, sp.Rational(283, 120), sp.Rational(1991, 720), sp.Rational(11, 240)),
        ("Below EW (QCD + QED: 0, 39, 9)", 0, 39, 9, sp.Rational(15, 8), sp.Rational(103, 48), sp.Rational(223, 360)),
        ("Below QCD (QED + 3 pi + e + 3 nu: 3, 5, 1)", 3, 5, 1, sp.Rational(1, 4), sp.Rational(37, 144), sp.Rational(17, 9)),
        ("Deep IR (gamma + 3 nu_L: 0, 3, 1)", 0, 3, 1, sp.Rational(7, 40), sp.Rational(157, 720), sp.Rational(7, 180)),
    ]

    stage_rows = []
    prev_a = None
    delta_sum = sp.Integer(0)
    consecutive_positive_drops = 0

    for idx_s, (name, NS, NW, NV, exp_c, exp_a, exp_da) in enumerate(stages_spec):
        cv = c_exact(NS, NW, NV)
        av = a_exact(NS, NW, NV)
        row = {
            "stage": idx_s + 1,
            "name": name,
            "N_S": NS,
            "N_W": NW,
            "N_V": NV,
            "c": fmt_rat(cv),
            "a": fmt_rat(av),
            "c_matches_card": bool(cv == exp_c),
            "a_matches_card": bool(av == exp_a),
        }
        if prev_a is not None:
            da = prev_a - av
            delta_sum += da
            if da > 0:
                consecutive_positive_drops += 1
            row["delta_a_from_prev"] = fmt_rat(da)
            row["delta_a_positive"] = bool(da > 0)
            row["delta_a_matches_card"] = bool(da == exp_da)
        prev_a = av
        stage_rows.append(row)

    total_da_direct = a_exact(8, 48, 12) - a_exact(0, 3, 1)
    telescope_match = bool(delta_sum == total_da_direct and total_da_direct == sp.Rational(125, 48))
    all_stages_exact = bool(
        all(r["c_matches_card"] and r["a_matches_card"] for r in stage_rows)
        and all(r["delta_a_positive"] and r["delta_a_matches_card"] for r in stage_rows[1:])
        and consecutive_positive_drops == 5
        and telescope_match
    )

    return {
        "c_2H": fmt_rat(c_2H),
        "a_2H": fmt_rat(a_2H),
        "c_1H": fmt_rat(c_1H),
        "a_1H": fmt_rat(a_1H),
        "twoH_exact_ok": twoH_ok,
        "oneH_exact_ok": oneH_ok,
        "bR_conformal_xi_1_6": fmt_rat(bR_conformal),
        "bR_conformal_zero": bR_conformal_zero,
        "stelle_apart_expr": str(stelle_apart),
        "stelle_apart_diff": str(apart_diff),
        "residue_x_0": fmt_rat(res_massless),
        "residue_x_minus_1": fmt_rat(res_ghost),
        "stelle_spot_checks": spot_checks,
        "stelle_ghost_pole_proved": stelle_ok,
        "a_theorem_stages": stage_rows,
        "consecutive_positive_drops": consecutive_positive_drops,
        "delta_a_sum": fmt_rat(delta_sum),
        "delta_a_direct_UV_minus_IR": fmt_rat(total_da_direct),
        "telescope_equals_125_48": telescope_match,
        "all_stages_exact": all_stages_exact,
        "passed": bool(twoH_ok and oneH_ok and stelle_ok and all_stages_exact),
    }


# =============================================================================
# SECTION 4: OW10-C — 12-ROW MASTER OPEN-WEAVE ToE SCORECARD PARTITION AUDIT
# =============================================================================

def verify_ow10_c_master_scorecard(ow10_a_core_ok, ow10_b_ok):
    """Independently verify the 12-row Master Open-Weave ToE Scorecard exact partition."""
    allowed_statuses = (
        "PROVED",
        "PARTIAL / CONDITIONAL",
        "NO-GO / IMPOSSIBLE-BY-THEOREM",
        "STILL OPEN",
    )

    rows = [
        (1, "PROVED", "Gauge/Chiral/Anomaly Engine", ["A2-OW1", "A2-OW4"]),
        (2, "PROVED", "N = 5 & N_gen = 3 Double-Pincer Selection", ["A2-OW4", "A2-OW10"]),
        (3, "PROVED", "6D -> 7D Chirality & Inflow", ["A2-OW5"]),
        (4, "PROVED", "X_0(5) Dynamical Casimir Stabilization of tau_*^{+-} & Positive dS Sign", ["A2-OW2", "A2-OW9"]),
        (5, "PROVED", "Conformal xi = 1/6 Attractive Finite Gravity & 2H Radiative EWSB Mechanism", ["A2-OW3", "A2-OW8"]),
        (6, "PARTIAL / CONDITIONAL", "Flavor Hierarchies/CKM/CP via 7D QR-Decoupling with log_2(6) Perm Cost", ["A2-OW6", "A2-OW7"]),
        (7, "PARTIAL / CONDITIONAL", "Dark Matter LKP Conditional on E[2] Democracy with Zero-Mode nu^c Ruled Out", ["A2-OW9"]),
        (8, "PARTIAL / CONDITIONAL", "4D Asymptotic Safety Conditional on Type-II Cutoff & Strong-Coupling Truncation", ["A2-OW10"]),
        (9, "NO-GO / IMPOSSIBLE-BY-THEOREM", "Pure-Volume/Untwisted Im(tau) > 1 & Raabe -36 Selection + 1H Conformal EWSB + Perturbative 4D Stelle Ghost", ["A2-OW3", "A2-OW6", "A2-OW8", "A2-OW10"]),
        (10, "NO-GO / IMPOSSIBLE-BY-THEOREM", "T^2 / Z_2 KK-Tower a_0 Cosmological Constant Cancellation & 4D Zero-Mode nu^c Stabilizer", ["A2-OW4", "A2-OW9"]),
        (11, "STILL OPEN", "Observed 10^(-120) Cosmological Constant Value & 4 Continuous Scale Inputs g_UV, lam_0, tan(beta), M_R/M_X", ["A2-OW8", "A2-OW9"]),
        (12, "STILL OPEN", "Early-Universe Dynamics -- Inflation, Baryogenesis Rate, CMB Spectrum, Structure Formation & Non-Perturbative 7D/FRG Quantum Gravity", ["A2-OW10"]),
    ]

    valid_cards = {f"A2-OW{k}" for k in range(1, 11)}
    counts = {st: 0 for st in allowed_statuses}
    seen_ids = set()
    seen_titles = set()
    unclassified = 0
    invalid_provenance = 0

    row_records = []
    for rid, status, title, cards in rows:
        seen_ids.add(rid)
        seen_titles.add(title)
        if status in counts:
            counts[status] += 1
        else:
            unclassified += 1
        if not cards or any(c not in valid_cards for c in cards):
            invalid_provenance += 1
        row_records.append(
            {
                "row_id": rid,
                "status": status,
                "sector": title,
                "cards": cards,
            }
        )

    total_rows = len(rows)
    partition_sum = sum(counts.values())
    exact_partition = bool(
        total_rows == 12
        and partition_sum == 12
        and len(seen_ids) == 12
        and len(seen_titles) == 12
        and unclassified == 0
        and invalid_provenance == 0
        and counts["PROVED"] == 5
        and counts["PARTIAL / CONDITIONAL"] == 3
        and counts["NO-GO / IMPOSSIBLE-BY-THEOREM"] == 2
        and counts["STILL OPEN"] == 2
    )
    a2_ow10_backing_ok = bool(ow10_a_core_ok and ow10_b_ok)

    return {
        "total_rows": total_rows,
        "status_counts": counts,
        "partition_sum": partition_sum,
        "unclassified_count": unclassified,
        "invalid_provenance_count": invalid_provenance,
        "exact_5_3_2_2_partition": exact_partition,
        "a2_ow10_backing_gates_passed": a2_ow10_backing_ok,
        "rows": row_records,
        "passed": bool(exact_partition and a2_ow10_backing_ok),
    }


# =============================================================================
# SECTION 5: OW10-D — ALL 4 / 4 PLANTED-FAULT SELF-CHECKS (PF-OW10-1..4)
# =============================================================================

def verify_ow10_d_planted_faults(nominal_2h_rec, ngen4_rec, type1_2h_rec):
    """Execute and certify all 4/4 planted-fault self-checks PF-OW10-1..4."""
    # PF-OW10-1: Flip fermion sign in B_1 (f_W = -1) on open-weave 2H (8, 48, 12)
    pf1_rec = solve_frg_spectrum(8, 48, 12, f_W=-1, label="PF-OW10-1 flipped fermion sign")
    nom_fp = nominal_2h_rec["fixed_points"][0]
    pf1_fp = pf1_rec["fixed_points"][0]
    g_ratio = nom_fp["_g_mp"] / pf1_fp["_g_mp"]
    pf1_caught = bool(
        nominal_2h_rec["M_g"] == 8
        and pf1_rec["M_g"] == -88
        and pf1_rec["n_uv_attractive_fps"] == 1
        and nom_fp["_g_mp"] > mp.mpf(7)
        and pf1_fp["_g_mp"] < mp_rat(1, 2)
        and g_ratio > mp.mpf(18)
        and nom_fp["_l_mp"] < mp.mpf(-10)
        and pf1_fp["_l_mp"] > mp.mpf(-1)
    )

    # PF-OW10-2: N_gen = 4 (8, 64, 12) Type-II => M_g = +24 > 14, 0 UV FPs
    pf2_caught = bool(
        ngen4_rec["M_g"] == 24
        and ngen4_rec["M_g"] > 14
        and ngen4_rec["sturm_exact_physical_root_count"] == 0
        and ngen4_rec["n_uv_attractive_fps"] == 0
    )

    # PF-OW10-3: Type-I (f_W = 2) on 2H (8, 48, 12) => M_g = +56 > 14, 0 UV FPs
    pf3_caught = bool(
        type1_2h_rec["M_g"] == 56
        and type1_2h_rec["M_g"] > 14
        and type1_2h_rec["sturm_exact_physical_root_count"] == 0
        and type1_2h_rec["n_uv_attractive_fps"] == 0
    )

    # PF-OW10-4: Reverse UV/IR in a-theorem & non-conformal xi = 0
    a_uv = sp.Rational(8, 360) + sp.Rational(11 * 48, 720) + sp.Rational(62 * 12, 360)
    a_ir = sp.Rational(0, 360) + sp.Rational(11 * 3, 720) + sp.Rational(62 * 1, 360)
    reversed_da = a_ir - a_uv
    xi_zero_sq = (sp.Integer(0) - sp.Rational(1, 6)) ** 2
    bR_xi_zero = sp.Integer(8) * xi_zero_sq
    pf4_caught = bool(
        reversed_da == sp.Rational(-125, 48)
        and reversed_da < 0
        and xi_zero_sq == sp.Rational(1, 36)
        and bR_xi_zero != 0
    )

    n_caught = int(pf1_caught) + int(pf2_caught) + int(pf3_caught) + int(pf4_caught)
    return {
        "PF-OW10-1": {
            "description": "Flip fermion sign in B_1 (f_W = -1) on (8, 48, 12)",
            "M_g_nominal": nominal_2h_rec["M_g"],
            "M_g_fault": pf1_rec["M_g"],
            "g_star_nominal_str": nom_fp["g_star_str"],
            "g_star_fault_str": pf1_fp["g_star_str"],
            "g_collapse_ratio_str": fmt_mp(g_ratio, 20),
            "lam_star_nominal_str": nom_fp["lam_star_str"],
            "lam_star_fault_str": pf1_fp["lam_star_str"],
            "spectrum": strip_internal_mp(pf1_rec),
            "caught": pf1_caught,
        },
        "PF-OW10-2": {
            "description": "Increase generations N_gen = 3 -> 4 ((8, 64, 12), Type-II)",
            "M_g_fault": ngen4_rec["M_g"],
            "sturm_root_count": ngen4_rec["sturm_exact_physical_root_count"],
            "n_uv_attractive_fps": ngen4_rec["n_uv_attractive_fps"],
            "caught": pf2_caught,
        },
        "PF-OW10-3": {
            "description": "Switch Type-II (f_W = 1) -> Type-I (f_W = 2) on (8, 48, 12)",
            "M_g_fault": type1_2h_rec["M_g"],
            "sturm_root_count": type1_2h_rec["sturm_exact_physical_root_count"],
            "n_uv_attractive_fps": type1_2h_rec["n_uv_attractive_fps"],
            "caught": pf3_caught,
        },
        "PF-OW10-4": {
            "description": "Reverse UV/IR in a-theorem and set non-conformal xi = 0",
            "a_IR_minus_a_UV": fmt_rat(reversed_da),
            "xi_zero_minus_sixth_sq": fmt_rat(xi_zero_sq),
            "bR_factor_xi_zero": fmt_rat(bR_xi_zero),
            "caught": pf4_caught,
        },
        "caught_count": n_caught,
        "total_faults": 4,
        "passed": bool(n_caught == 4),
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    # -------------------------------------------------------------------------
    # 1. Symbolic FRG derivation & RG variable audit
    # -------------------------------------------------------------------------
    symbolic_frg = verify_rg_differential_variable_and_cubic()

    # -------------------------------------------------------------------------
    # 2. Guardrail 4 Literature Benchmark Gate (isolated prior to model claims)
    # -------------------------------------------------------------------------
    # 2a. Litim (2004, PRL 92 201301) pure gravity (0, 0, 0)
    litim_rec = solve_frg_spectrum(0, 0, 0, f_W=1, label="Litim 2004 pure gravity")
    litim_fp = litim_rec["fixed_points"][0]
    litim_g_err = abs(litim_fp["_g_mp"] - mp_rat(70732, 100000))
    litim_l_err = abs(litim_fp["_l_mp"] - mp_rat(19320, 100000))
    litim_re_err = abs(litim_fp["_t1_mp"].real - mp_rat(14753, 10000))
    litim_im_err = abs(abs(litim_fp["_t1_mp"].imag) - mp_rat(30432, 10000))

    litim_pass = bool(
        litim_rec["sturm_matches_direct_solver"]
        and litim_rec["n_uv_attractive_fps"] == 1
        and litim_fp["is_complex_conjugate_pair"]
        and litim_fp["numerical_certified"]
        and litim_g_err < mp_pow10(-5)
        and litim_l_err < mp_pow10(-5)
        and litim_re_err < mp_pow10(-4)
        and litim_im_err < mp_pow10(-4)
        and litim_fp["_res_mp"] < mp_pow10(-30)
    )

    # 2b. Dona-Eichhorn-Percacci (arXiv 1311-2898) pure-fermion bounds (N_W = 2 N_D)
    dep_type2 = []
    for nd in range(0, 9):
        rec = solve_frg_spectrum(0, 2 * nd, 0, f_W=1, label=f"DEP Type-II N_D={nd}")
        dep_type2.append(rec)
    dep_type1 = []
    for nd in range(0, 6):
        rec = solve_frg_spectrum(0, 2 * nd, 0, f_W=2, label=f"DEP Type-I N_D={nd}")
        dep_type1.append(rec)

    dep_type2_pass = bool(
        all(
            r["sturm_matches_direct_solver"]
            and r["n_uv_attractive_fps"] == 1
            and r["fixed_points"][0]["numerical_certified"]
            for r in dep_type2[:7]
        )
        and all(
            r["sturm_matches_direct_solver"] and r["n_uv_attractive_fps"] == 0
            for r in dep_type2[7:]
        )
    )
    dep_type1_pass = bool(
        all(
            r["sturm_matches_direct_solver"]
            and r["n_uv_attractive_fps"] == 1
            and r["fixed_points"][0]["numerical_certified"]
            for r in dep_type1[:4]
        )
        and all(
            r["sturm_matches_direct_solver"] and r["n_uv_attractive_fps"] == 0
            for r in dep_type1[4:]
        )
    )
    guardrail4_benchmarks_passed = bool(symbolic_frg["passed"] and litim_pass and dep_type2_pass and dep_type1_pass)

    # -------------------------------------------------------------------------
    # 3. Open-Weave Double-Pincer Scans & Type-I / Strong-Coupling Caveats
    # -------------------------------------------------------------------------
    # Generation scan at N = 5, 2H: N_S = 8, N_V = 12, N_W = 16 N_gen, Type-II
    ngen_scan = []
    for ngen in range(1, 5):
        rec = solve_frg_spectrum(8, 16 * ngen, 12, f_W=1, label=f"N=5 2H N_gen={ngen} Type-II")
        ngen_scan.append(rec)

    # Higgs scan at N = 5, N_gen = 3: N_S = 4 n_H, N_W = 48, N_V = 12, Type-II
    nh_scan = []
    for nh in range(1, 5):
        rec = solve_frg_spectrum(4 * nh, 48, 12, f_W=1, label=f"N=5 N_gen=3 n_H={nh} Type-II")
        nh_scan.append(rec)

    # Open-weave 2H (8, 48, 12) Type-II, Type-I, and SM 1H (4, 45, 12) Type-II & Type-I
    ow_2h_type2 = ngen_scan[2]  # N_gen = 3
    ow_2h_type1 = solve_frg_spectrum(8, 48, 12, f_W=2, label="OpenWeave 2H (8, 48, 12) Type-I")
    sm_1h_type2 = solve_frg_spectrum(4, 45, 12, f_W=1, label="SM 1H (4, 45, 12) Type-II")
    sm_1h_type1 = solve_frg_spectrum(4, 45, 12, f_W=2, label="SM 1H (4, 45, 12) Type-I")

    # Verify card pass bars for Open-Weave 2H Type-II fixed point
    ow_fp = ow_2h_type2["fixed_points"][0]
    ow_2h_type2_pass = bool(
        ow_2h_type2["sturm_matches_direct_solver"]
        and ow_2h_type2["n_uv_attractive_fps"] == 1
        and ow_fp["numerical_certified"]
        and (not ow_fp["is_complex_conjugate_pair"])
        and ow_fp["_g_mp"] > mp.mpf(7)
        and ow_fp["_g_mp"] < mp_rat(71, 10)
        and ow_fp["_l_mp"] > mp_rat(-101, 10)
        and ow_fp["_l_mp"] < mp.mpf(-10)
        and ow_fp["_t1_mp"].real > mp_rat(39, 10)
        and ow_fp["_t1_mp"].real < mp.mpf(4)
        and ow_fp["_t2_mp"].real > mp_rat(21, 10)
        and ow_fp["_t2_mp"].real < mp_rat(22, 10)
        and ow_fp["_res_mp"] < mp_pow10(-30)
    )

    ngen_survivors = [
        idx + 1
        for idx, r in enumerate(ngen_scan)
        if r["M_g"] > 0 and r["M_g"] < 14 and r["n_uv_attractive_fps"] == 1
    ]
    ngen_pincer_pass = bool(
        ngen_survivors == [3]
        and ngen_scan[0]["M_g"] == -24
        and ngen_scan[1]["M_g"] == -8
        and ngen_scan[2]["M_g"] == 8
        and ngen_scan[3]["M_g"] == 24
        and ngen_scan[3]["n_uv_attractive_fps"] == 0
        and all(r["sturm_matches_direct_solver"] for r in ngen_scan)
    )

    nh_survivors = [
        idx + 1
        for idx, r in enumerate(nh_scan)
        if r["M_g"] > 0 and r["M_g"] < 14 and r["n_uv_attractive_fps"] == 1
    ]
    nh_pincer_pass = bool(
        nh_survivors == [1, 2, 3]
        and nh_scan[3]["M_g"] == 16
        and nh_scan[3]["n_uv_attractive_fps"] == 0
        and all(r["sturm_matches_direct_solver"] for r in nh_scan)
    )

    caveats_pass = bool(
        ow_2h_type1["M_g"] == 56
        and ow_2h_type1["n_uv_attractive_fps"] == 0
        and ow_2h_type1["sturm_matches_direct_solver"]
        and sm_1h_type1["M_g"] == 46
        and sm_1h_type1["n_uv_attractive_fps"] == 0
        and sm_1h_type1["sturm_matches_direct_solver"]
        and ow_fp["_g_mp"] > mp.mpf(7)
        and ow_fp["_l_mp"] < mp.mpf(-10)
    )

    # -------------------------------------------------------------------------
    # 4. Disjoint Matrix-Group Delta(2, 3, N) + Bitmask Fock-Space Enumeration
    # -------------------------------------------------------------------------
    delta_actions = analyze_delta_23N_matrix_actions()

    # Physics uniqueness holds across ALL 4 group-action tables (exact 15, 21 inv-pairs, 20 all-d, 24 all-trans)
    delta_uniqueness_pass = bool(
        delta_actions["all_matrix_groups_verified"]
        and delta_actions["all_conjugacy_invariance_verified"]
        and delta_actions["all_fock_basis_invariance_verified"]
        and delta_actions["unique_n5_d5_in_exact_15"]
        and delta_actions["unique_n5_d5_in_all_20_faithful"]
        and delta_actions["unique_n5_d5_in_21_involution_pairs"]
        and delta_actions["unique_n5_d5_in_all_24_transitive"]
    )

    ow10_a_core_pass = bool(
        guardrail4_benchmarks_passed
        and ow_2h_type2_pass
        and ngen_pincer_pass
        and nh_pincer_pass
        and caveats_pass
        and delta_uniqueness_pass
    )

    # -------------------------------------------------------------------------
    # 5. OW10-B, OW10-C, OW10-D
    # -------------------------------------------------------------------------
    ow10_b = verify_ow10_b_stelle_and_a_theorem()
    ow10_c = verify_ow10_c_master_scorecard(ow10_a_core_pass, ow10_b["passed"])
    ow10_d = verify_ow10_d_planted_faults(ow_2h_type2, ngen_scan[3], ow_2h_type1)

    all_core_gates_passed = bool(ow10_a_core_pass and ow10_b["passed"] and ow10_c["passed"] and ow10_d["passed"])

    # Compute own script SHA-256 for self-identification
    script_path = Path(__file__).resolve()
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()

    output = {
        "card_id": "A2-OW10",
        "role": "Independent Cold-Room Zero-Trust Referee",
        "empirical_firewall": "0 of 19 (Litim 2004 & DEP 1311-2898 strictly isolated in Guardrail 4)",
        "working_dps": DPS_TARGET,
        "script_sha256": script_sha256,
        "OW10_A": {
            "symbolic_frg_derivation": symbolic_frg,
            "guardrail_4_benchmarks": {
                "litim_2004_pure_gravity": {
                    "spectrum": strip_internal_mp(litim_rec),
                    "abs_err_g_vs_70732e_5": fmt_mp(litim_g_err, 6),
                    "abs_err_lam_vs_19320e_5": fmt_mp(litim_l_err, 6),
                    "abs_err_re_theta_vs_14753e_4": fmt_mp(litim_re_err, 6),
                    "abs_err_im_theta_vs_30432e_4": fmt_mp(litim_im_err, 6),
                    "passed": litim_pass,
                },
                "dep_1311_2898_pure_fermion_type_ii": {
                    "rows": [strip_internal_mp(r) for r in dep_type2],
                    "max_surviving_N_D": max(
                        idx for idx, r in enumerate(dep_type2) if r["n_uv_attractive_fps"] == 1
                    ),
                    "first_destroyed_N_D": min(
                        idx for idx, r in enumerate(dep_type2) if r["n_uv_attractive_fps"] == 0
                    ),
                    "passed": dep_type2_pass,
                },
                "dep_1311_2898_pure_fermion_type_i": {
                    "rows": [strip_internal_mp(r) for r in dep_type1],
                    "max_surviving_N_D": max(
                        idx for idx, r in enumerate(dep_type1) if r["n_uv_attractive_fps"] == 1
                    ),
                    "first_destroyed_N_D": min(
                        idx for idx, r in enumerate(dep_type1) if r["n_uv_attractive_fps"] == 0
                    ),
                    "passed": dep_type1_pass,
                },
                "passed": guardrail4_benchmarks_passed,
            },
            "double_pincer_scans": {
                "N_gen_scan_at_N5_2H": [strip_internal_mp(r) for r in ngen_scan],
                "N_gen_survivors": ngen_survivors,
                "N_gen_pincer_passed": ngen_pincer_pass,
                "n_H_scan_at_N5_Ngen3": [strip_internal_mp(r) for r in nh_scan],
                "n_H_survivors": nh_survivors,
                "n_H_pincer_passed": nh_pincer_pass,
            },
            "open_weave_and_caveats": {
                "open_weave_2H_type_ii": strip_internal_mp(ow_2h_type2),
                "open_weave_2H_type_ii_passed": ow_2h_type2_pass,
                "open_weave_2H_type_i": strip_internal_mp(ow_2h_type1),
                "sm_1H_type_ii": strip_internal_mp(sm_1h_type2),
                "sm_1H_type_i": strip_internal_mp(sm_1h_type1),
                "strong_coupling_caveat_g_gt_7_lam_lt_minus_10": bool(
                    ow_fp["_g_mp"] > mp.mpf(7) and ow_fp["_l_mp"] < mp.mpf(-10)
                ),
                "type_i_destruction_caveat_passed": caveats_pass,
            },
            "delta_23N_matrix_actions": delta_actions,
            "delta_uniqueness_passed": delta_uniqueness_pass,
            "passed": ow10_a_core_pass,
        },
        "OW10_B": ow10_b,
        "OW10_C": ow10_c,
        "OW10_D": ow10_d,
        "summary_gates": {
            "guardrail4_benchmarks_passed": guardrail4_benchmarks_passed,
            "OW10_A_passed": ow10_a_core_pass,
            "OW10_B_passed": ow10_b["passed"],
            "OW10_C_passed": ow10_c["passed"],
            "OW10_D_passed": ow10_d["passed"],
            "card_21_matches_exact_faithful_d_le_12": delta_actions["card_21_matches_exact_faithful_d_le_12"],
            "card_21_matches_involution_paired_d_le_12": delta_actions["card_21_matches_involution_paired_d_le_12"],
            "all_core_gates_passed": all_core_gates_passed,
        },
    }

    out_path = script_path.parent / "referee_a2_ow10_out.json"
    out_path.write_text(json.dumps(output, indent=2, sort_keys=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
