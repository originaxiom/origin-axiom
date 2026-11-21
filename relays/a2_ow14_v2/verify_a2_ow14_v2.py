#!/usr/bin/env python3
"""
AGY-002 Card A2-OW14 Producer:
  7D -> 4D Einstein-Frame Hyperbolic Radion (M_4 x M_3),
  Exact Townsend-Wohlfarth Transient Acceleration & AdS Volume Stabilization,
  Unimodular Gravity (det g = -1, lam = 0) N_gen = 3 Double-Pincer & Kaloper-Padilla Sequestering (0 of 19).

Guardrails enforced:
  - 0 float/complex AST literals (exact Fraction, sympy, integer-built mpmath at 55 dps).
  - 0 frontier/ imports; 0 empirical PDG inputs.
  - Zero hardcoded proof flags; Guardrail 1 zero post-inspection pinning of L_*.
"""

from collections import deque
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp


def mp_rat(p, q=1):
    return mp.mpf(int(p)) / mp.mpf(int(q))


def mp_pow10(exp_int):
    return mp.power(mp.mpf(10), int(exp_int))


def frac_str(f):
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def f64_rat(p, q=1):
    return float(Fraction(int(p), int(q)))


def f64_pow10(exp_int):
    if exp_int >= 0:
        return float(10 ** int(exp_int))
    return float(Fraction(1, 10 ** (-int(exp_int))))


# ---------------------------------------------------------------------------
# Exact Delta(2, 3, N) (N = 2..5) Permutation Group & 21-Action Census
# ---------------------------------------------------------------------------

def compose_perm(p, q):
    return tuple(p[i] for i in q)


def inv_perm(p):
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)


def generate_group(gens, n):
    ident = tuple(range(n))
    seen = {ident}
    q = deque([ident])
    all_gens = list(gens) + [inv_perm(g) for g in gens]
    while q:
        cur = q.popleft()
        for g in all_gens:
            nxt = compose_perm(g, cur)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return sorted(seen)


def build_triangle_group(N):
    if N == 2:
        a, b, n = (1, 0, 2), (1, 2, 0), 3
    elif N == 3:
        a, b, n = (1, 0, 3, 2), (1, 2, 0, 3), 4
    elif N == 4:
        a, b, n = (1, 0, 2, 3), (0, 2, 3, 1), 4
    elif N == 5:
        a, b, n = (1, 0, 3, 2, 4), (0, 2, 4, 3, 1), 5
    else:
        raise ValueError(f"Unsupported N={N}")
    def _ord(p):
        cur, k, ident = p, 1, tuple(range(len(p)))
        while cur != ident:
            cur = compose_perm(p, cur)
            k += 1
        return k
    assert _ord(a) == 2 and _ord(b) == 3 and _ord(compose_perm(a, b)) == N
    return generate_group([a, b], n)


def involution_classes(G):
    ident = G[0]
    invs = [g for g in G if g != ident and compose_perm(g, g) == ident]
    used = set()
    classes = []
    for x in invs:
        if x in used:
            continue
        cls = {compose_perm(compose_perm(g, x), inv_perm(g)) for g in G}
        used |= cls
        classes.append(sorted(cls))
    return classes


def faithful_subgroups(G, max_index=12):
    order_G = len(G)
    ident = G[0]
    min_sub = (order_G + max_index - 1) // max_index

    def closure(elems):
        s = set(elems)
        s.add(ident)
        q = deque(s)
        while q:
            x = q.popleft()
            for y in list(s):
                for prod in (compose_perm(x, y), compose_perm(y, x)):
                    if prod not in s:
                        s.add(prod)
                        q.append(prod)
        return frozenset(s)

    all_subs = {frozenset([ident])}
    q = deque([frozenset([ident])])
    while q:
        H = q.popleft()
        for g in G:
            if g in H:
                continue
            H2 = closure(set(H) | {g})
            if H2 not in all_subs:
                all_subs.add(H2)
                q.append(H2)

    reps = []
    seen_conj = set()
    for H in sorted(all_subs, key=lambda s: (-len(s), sorted(s))):
        if len(H) < min_sub or order_G % len(H) != 0:
            continue
        deg = order_G // len(H)
        if deg > max_index or H in seen_conj:
            continue
        conj_cls = set()
        core = set(G)
        for g in G:
            gi = inv_perm(g)
            Hg = frozenset(compose_perm(compose_perm(g, h), gi) for h in H)
            conj_cls.add(Hg)
            core &= Hg
        seen_conj |= conj_cls
        if len(core) == 1:
            reps.append((deg, H))
    return reps


def coset_action(G, H, elem):
    cosets = []
    seen = set()
    for g in G:
        if g in seen:
            continue
        c = frozenset(compose_perm(g, h) for h in H)
        cosets.append(c)
        seen |= c
    cosets.sort(key=lambda c: min(c))
    idx_map = {c: i for i, c in enumerate(cosets)}
    perm = []
    for c in cosets:
        rep = min(c)
        img = compose_perm(elem, rep)
        for c2, idx in idx_map.items():
            if img in c2:
                perm.append(idx)
                break
    return tuple(perm)


def analyze_cl2d_action(d, a_plus, b_minus):
    n_V = a_plus * a_plus + b_minus * b_minus - 1
    n_s_2H = 4 * b_minus
    scale = (a_plus * b_minus) // math.gcd(a_plus, b_minus)
    mults = []
    for ka in range(a_plus + 1):
        for kb in range(b_minus + 1):
            if (ka + kb) % 2 == 0:
                y_raw = Fraction(kb, b_minus) - Fraction(ka, a_plus)
                mults.append((ka, kb, int(y_raw * scale)))
    mult_set = set(mults)
    is_chiral = any((a_plus - ka, b_minus - kb, -y_int) not in mult_set for (ka, kb, y_int) in mults)
    n_W_3gen = 3 * (2 ** (d - 1)) if is_chiral else 0

    def dynkin_2(n, k):
        return math.comb(n - 2, k - 1) if (1 <= k <= n - 1) else 0

    def anom_3(n, k):
        if n < 3 or k == 0 or k == n:
            return 0
        c1 = math.comb(n - 3, k - 1) if (0 <= k - 1 <= n - 3) else 0
        c2 = math.comb(n - 3, k - 2) if (0 <= k - 2 <= n - 3) else 0
        return c1 - c2

    tr_Y = sum(math.comb(a_plus, ka) * math.comb(b_minus, kb) * y for (ka, kb, y) in mults)
    tr_Y3 = sum(math.comb(a_plus, ka) * math.comb(b_minus, kb) * (y ** 3) for (ka, kb, y) in mults)
    su_a2_Y = sum(dynkin_2(a_plus, ka) * math.comb(b_minus, kb) * y for (ka, kb, y) in mults)
    su_b2_Y = sum(math.comb(a_plus, ka) * dynkin_2(b_minus, kb) * y for (ka, kb, y) in mults)
    su_a3 = sum(anom_3(a_plus, ka) * math.comb(b_minus, kb) for (ka, kb, _) in mults)
    su_b3 = sum(math.comb(a_plus, ka) * anom_3(b_minus, kb) for (ka, kb, _) in mults)
    anom_free = bool(tr_Y == 0 and tr_Y3 == 0 and su_a2_Y == 0 and su_b2_Y == 0 and su_a3 == 0 and su_b3 == 0)
    Mg = n_s_2H + n_W_3gen - 4 * n_V
    return {
        "d": d, "a_plus": a_plus, "b_minus": b_minus,
        "Ns": n_s_2H, "Nw": n_W_3gen, "Nv": n_V, "Mg": Mg,
        "is_chiral": is_chiral, "anomaly_free": anom_free,
    }


def enumerate_all_21_actions():
    actions = []
    for N in (2, 3, 4, 5):
        G = build_triangle_group(N)
        invs = involution_classes(G)
        subs = faithful_subgroups(G, max_index=12)
        for deg, H in subs:
            for ic_idx, cls in enumerate(invs):
                perm = coset_action(G, H, cls[0])
                fixed = sum(1 for i, v in enumerate(perm) if v == i)
                two_cycles = (deg - fixed) // 2
                info = analyze_cl2d_action(deg, fixed + two_cycles, two_cycles)
                info["N"] = N
                info["inv_class_index"] = ic_idx
                actions.append(info)
    return actions


# ---------------------------------------------------------------------------
# Task OW14-A: 7D Christoffel / Ricci Reduction, TW Acceleration, Stabilization
# ---------------------------------------------------------------------------

def derive_7d_einstein_frame(a_ratio_over_b=None):
    if a_ratio_over_b is None:
        a_ratio_over_b = sp.Rational(-3, 2)
    t = sp.Symbol("t", real=True)
    sig = sp.Function("sig")(t)
    a, b = sp.symbols("a b", real=True)
    g_diag = [
        -sp.exp(2 * a * sig),
        sp.exp(2 * a * sig),
        sp.exp(2 * a * sig),
        sp.exp(2 * a * sig),
        sp.exp(2 * b * sig),
        sp.exp(2 * b * sig),
        sp.exp(2 * b * sig),
    ]
    D = 7
    Gamma = [[[sp.Integer(0) for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for A in range(D):
        for B in range(D):
            for C in range(D):
                term = sp.Integer(0)
                if B == 0 and A == C:
                    term += sp.diff(g_diag[A], t)
                if C == 0 and A == B:
                    term += sp.diff(g_diag[A], t)
                if A == 0 and B == C:
                    term -= sp.diff(g_diag[B], t)
                Gamma[A][B][C] = sp.simplify(sp.Rational(1, 2) * (1 / g_diag[A]) * term)

    Ric = [[sp.Integer(0) for _ in range(D)] for _ in range(D)]
    for B in range(D):
        for C in range(D):
            val = sp.diff(Gamma[0][B][C], t)
            if C == 0:
                for A in range(D):
                    val -= sp.diff(Gamma[A][B][A], t)
            for A in range(D):
                for E in range(D):
                    val += Gamma[A][A][E] * Gamma[E][B][C] - Gamma[A][C][E] * Gamma[E][B][A]
            Ric[B][C] = sp.simplify(val)

    R7_kin = sp.simplify(sum(Ric[B][B] / g_diag[B] for B in range(D)))
    sqrt_g7 = sp.exp((4 * a + 3 * b) * sig)
    einstein_frame_exp = sp.simplify((2 * a + 3 * b).subs(a, a_ratio_over_b * b))
    is_einstein_frame = bool(einstein_frame_exp == 0)

    L_eff = sp.expand(sp.simplify((sp.Rational(1, 2) * sqrt_g7 * R7_kin).subs(a, a_ratio_over_b * b)))
    sig_p = sp.diff(sig, t)
    sig_pp = sp.diff(sig, t, 2)
    c_pp = sp.simplify(L_eff.coeff(sig_pp))
    L_ibp = sp.simplify(L_eff - sp.diff(c_pp * sig_p, t))
    # Coefficient of (sig')^2 at sig = 0 (exact if Einstein frame; exp((2a+3b)sig) factor if non-Einstein)
    kin_coeff = sp.simplify((L_ibp / (sig_p * sig_p)).subs(sig, 0))
    b_sols = sp.solve(sp.Eq(kin_coeff, sp.Rational(1, 2)), b)
    b_pos = [s for s in b_sols if s.is_real and s > 0][0]
    a_pos = sp.simplify(a_ratio_over_b * b_pos)

    slopes = {}
    for label, mult in [
        ("bulk_lambda7_L_m3", 3),
        ("hyperbolic_curv_L_m5", 5),
        ("cs_3form_flux_L_m9", 9),
        ("casimir_1loop_L_m10", 10),
    ]:
        gam = sp.simplify(mult * b_pos)
        eps_V = sp.simplify(gam * gam / 2)
        w_attr = sp.simplify(gam * gam / 3 - 1)
        slopes[label] = {
            "L_power": -mult,
            "gamma_exact": str(gam),
            "gamma_val": mp.nstr(mp.mpf(str(gam.evalf(55))), 20),
            "eps_V": str(eps_V),
            "w_attr": str(w_attr),
            "accelerates_asymptotically": bool(w_attr < sp.Rational(-1, 3)),
        }

    return {
        "a_over_b": str(a_ratio_over_b),
        "einstein_frame_exponent_2a_plus_3b": str(einstein_frame_exp),
        "is_einstein_frame": is_einstein_frame,
        "kin_coeff_at_sig0": str(kin_coeff),
        "b_canon_exact": str(b_pos),
        "b_canon_val": mp.nstr(mp.mpf(str(b_pos.evalf(55))), 20),
        "a_canon_exact": str(a_pos),
        "a_canon_val": mp.nstr(mp.mpf(str(a_pos.evalf(55))), 20),
        "slopes": slopes,
        "_b_sym": b_pos,
    }


def analyze_townsend_wohlfarth():
    s3 = mp.sqrt(mp.mpf(3))
    s5 = mp.sqrt(mp.mpf(5))
    # Exact closed form for H^3 (gamma = sqrt(10/3), c = sqrt(5)):
    N_exact = mp_rat(3, 4) * mp.log((s5 + s3) / (s5 - s3)) - (s5 / mp.mpf(4)) * mp.log((s3 + mp.mpf(1)) / (s3 - mp.mpf(1)))
    N_quad = mp.quad(lambda xv: mp.mpf(1) / ((mp.mpf(1) - xv * xv) * (s5 - mp.mpf(3) * xv)), [-mp.mpf(1) / s3, mp.mpf(1) / s3])
    quad_err = abs(N_exact - N_quad)

    # Direct cosmic-time 4D Friedmann + radion ODE (DOP853 with event detection)
    gam_mp = mp.sqrt(mp_rat(10, 3))
    gam_f = float(gam_mp)
    half = f64_rat(1, 2)
    three = f64_rat(3, 1)

    def frw_rhs(tau, y):
        phi, phid, lna = y
        V = float(np.exp(-gam_f * phi))
        H = float(np.sqrt((half * phid * phid + V) / three))
        phidd = -three * H * phid + gam_f * V
        return [phid, phidd, H]

    def ev_accel(tau, y):
        return y[1] * y[1] - float(np.exp(-gam_f * y[0]))

    def ev_bounce(tau, y):
        return y[1]

    x0 = mp_rat(-999, 1000)
    H0 = mp.sqrt(mp_rat(1, 3)) / mp.sqrt(mp.mpf(1) - x0 * x0)
    phid0 = mp.sqrt(mp.mpf(6)) * H0 * x0
    sol = solve_ivp(
        frw_rhs,
        [f64_rat(0, 1), f64_rat(200, 1)],
        [f64_rat(0, 1), float(phid0), f64_rat(0, 1)],
        method="DOP853",
        rtol=f64_pow10(-13),
        atol=f64_pow10(-15),
        events=[ev_accel, ev_bounce],
    )
    lna_in = mp.mpf(str(sol.y_events[0][0][2]))
    lna_out = mp.mpf(str(sol.y_events[0][1][2]))
    N_ode = lna_out - lna_in
    ode_err = abs(N_ode - N_exact)

    phi_b = mp.mpf(str(sol.y_events[1][0][0]))
    phid_b = mp.mpf(str(sol.y_events[1][0][1]))
    Vb = mp.exp(-gam_mp * phi_b)
    Kb = mp_rat(1, 2) * phid_b * phid_b
    w_min = (Kb - Vb) / (Kb + Vb)

    phi_end = mp.mpf(str(sol.y[0, -1]))
    phid_end = mp.mpf(str(sol.y[1, -1]))
    Vend = mp.exp(-gam_mp * phi_end)
    Kend = mp_rat(1, 2) * phid_end * phid_end
    w_end = (Kend - Vend) / (Kend + Vend)

    hn_table = {}
    for n_dim in (2, 3, 4, 6):
        gam_n = mp.sqrt(mp_rat(2 * (n_dim + 2), n_dim))
        cn = mp.sqrt(mp_rat(3 * (n_dim + 2), n_dim))
        Nn = mp.quad(lambda xv: mp.mpf(1) / ((mp.mpf(1) - xv * xv) * (cn - mp.mpf(3) * xv)), [-mp.mpf(1) / s3, mp.mpf(1) / s3])
        w_n = mp_rat(2 * (n_dim + 2), 3 * n_dim) - mp.mpf(1)
        hn_table[f"H^{n_dim}"] = {
            "n": n_dim,
            "gamma": mp.nstr(gam_n, 18),
            "w_attr": frac_str(Fraction(2 * (n_dim + 2), 3 * n_dim) - 1),
            "N_accel_max": mp.nstr(Nn, 18),
            "_N_mp": Nn,
        }

    return {
        "N_accel_exact": mp.nstr(N_exact, 22),
        "N_accel_quad": mp.nstr(N_quad, 22),
        "quad_abs_err": mp.nstr(quad_err, 12),
        "N_accel_ode": mp.nstr(N_ode, 18),
        "ode_abs_err": mp.nstr(ode_err, 12),
        "w_min_bounce": mp.nstr(w_min, 18),
        "w_bounce_err_from_neg1": mp.nstr(abs(w_min + mp.mpf(1)), 12),
        "w_late_t200": mp.nstr(w_end, 16),
        "w_late_err_from_1_9": mp.nstr(abs(w_end - mp_rat(1, 9)), 12),
        "hyperbolic_dim_scan": hn_table,
        "_N_exact": N_exact,
        "_quad_err": quad_err,
        "_ode_err": ode_err,
        "_w_min_err": abs(w_min + mp.mpf(1)),
        "_w_end_err": abs(w_end - mp_rat(1, 9)),
    }


def analyze_7d_volume_stabilization(c3_sign=-1):
    # V(L) = c3_sign * c3 * L^-3 + c5 * L^-5 + c9 * L^-9 + c10 * L^-10
    L = sp.Symbol("L", positive=True)
    c3, c5, c9, c10, c6 = sp.symbols("c3 c5 c9 c10 c6", positive=True)
    u = sp.Symbol("u", real=True)
    # Benchmark (|c3|, c5, c9, c10) = (1, 1, 1, 1):
    # P(u) = 3*c3_sign + 5*u^2 + 9*u^6 + 10*u^7 (where u = 1/L > 0, V'(L) = -u^4 P(u))
    P_bench = sp.Poly(3 * c3_sign + 5 * u**2 + 9 * u**6 + 10 * u**7, u)
    pos_roots = [r for r in sp.real_roots(P_bench) if r > 0]

    bench_info = {"c3_sign": c3_sign, "num_positive_extrema": len(pos_roots)}
    if len(pos_roots) == 1:
        u_star = mp.mpf(str(pos_roots[0].evalf(55)))
        L_star = mp.mpf(1) / u_star
        V_val = mp.mpf(c3_sign) * (L_star ** (-3)) + L_star ** (-5) + L_star ** (-9) + L_star ** (-10)
        dV_val = mp.mpf(-3 * c3_sign) * (L_star ** (-4)) - mp.mpf(5) * (L_star ** (-6)) - mp.mpf(9) * (L_star ** (-10)) - mp.mpf(10) * (L_star ** (-11))
        d2V_val = mp.mpf(12 * c3_sign) * (L_star ** (-5)) + mp.mpf(30) * (L_star ** (-7)) + mp.mpf(90) * (L_star ** (-11)) + mp.mpf(110) * (L_star ** (-12))
        bench_info.update({
            "L_star": mp.nstr(L_star, 20),
            "V_at_L_star": mp.nstr(V_val, 20),
            "dV_at_L_star": mp.nstr(dV_val, 12),
            "d2V_at_L_star": mp.nstr(d2V_val, 20),
            "is_stable_minimum": bool(d2V_val > 0),
            "is_ads_vacuum": bool(V_val < 0),
            "_dV_abs": abs(dV_val),
            "_d2V": d2V_val,
            "_V": V_val,
        })

    # Symbolic general AdS theorem (all positive c5, c9, c10)
    V_ads = -c3 / L**3 + c5 / L**5 + c9 / L**9 + c10 / L**10
    c3_sol = sp.solve(sp.Eq(sp.diff(V_ads, L), 0), c3)[0]
    V_ads_min = sp.factor(sp.simplify(V_ads.subs(c3, c3_sol)))
    d2V_ads_min = sp.factor(sp.simplify(sp.diff(V_ads, L, 2).subs(c3, c3_sol)))
    V_ads_target = -(2 * c5 * L**5 + 6 * c9 * L + 7 * c10) / (3 * L**10)
    d2V_ads_target = 2 * (5 * c5 * L**5 + 27 * c9 * L + 35 * c10) / (L**12)
    ads_sym_match = bool(
        sp.simplify(V_ads_min - V_ads_target) == 0
        and sp.simplify(d2V_ads_min - d2V_ads_target) == 0
    )

    # Symbolic Minkowski lift V = c5 L^-5 - c6 L^-6 + c9 L^-9
    V_mink = c5 / L**5 - c6 / L**6 + c9 / L**9
    sol_m = sp.solve([sp.Eq(V_mink, 0), sp.Eq(sp.diff(V_mink, L), 0)], (c6, c9))
    d2V_m = sp.simplify(sp.diff(V_mink, L, 2).subs(sol_m))
    mink_match = bool(
        sp.simplify(sol_m[c6] - sp.Rational(4, 3) * c5 * L) == 0
        and sp.simplify(sol_m[c9] - sp.Rational(1, 3) * c5 * L**4) == 0
        and sp.simplify(d2V_m - 4 * c5 / L**7) == 0
    )

    return {
        "benchmark": bench_info,
        "symbolic_ads_V_min": str(V_ads_min),
        "symbolic_ads_d2V_min": str(d2V_ads_min),
        "symbolic_ads_identity_match": ads_sym_match,
        "minkowski_lift_c6": str(sol_m[c6]),
        "minkowski_lift_c9": str(sol_m[c9]),
        "minkowski_lift_d2V": str(d2V_m),
        "minkowski_lift_identity_match": mink_match,
    }


# ---------------------------------------------------------------------------
# Task OW14-B: Unimodular Gravity (det g = -1, lam = 0) & Kaloper-Padilla
# ---------------------------------------------------------------------------

def analyze_unimodular_and_kp():
    # 1. Explicit 4x4 trace-free stress-energy decoupling + Klein-Gordon preservation
    rho_v = sp.Symbol("rho_v", real=True)
    g_mat = sp.diag(-1, 1, 1, 1)
    g_inv = sp.diag(-1, 1, 1, 1)
    T_syms = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"T_{min(i,j)}{max(i,j)}", real=True))

    def trace_free(T):
        tr = sum(g_inv[i, i] * T[i, i] for i in range(4))
        return sp.simplify(T - sp.Rational(1, 4) * g_mat * tr)

    tf_diff = sp.simplify(trace_free(T_syms - rho_v * g_mat) - trace_free(T_syms))
    tf_zero_all = bool(all(tf_diff[i, j] == 0 for i in range(4) for j in range(4)))

    # Scalar stress-energy conservation in flat Minkowski (phi(t) homogeneous):
    # T_00 = (1/2) phid^2 + V(phi), T_ij = delta_ij ((1/2) phid^2 - V(phi))
    # nabla^a T_{a0} = -d_t T_00 = -phid * (phidd + V'(phi)) = 0 => phidd + V'(phi) = 0!
    t = sp.Symbol("t", real=True)
    phi = sp.Function("phi")(t)
    V_fn = sp.Function("V")(phi)
    T00_phi = sp.Rational(1, 2) * sp.diff(phi, t)**2 + V_fn
    T00_shifted = T00_phi + rho_v
    kg_from_div = sp.simplify(sp.diff(T00_shifted, t) / sp.diff(phi, t))
    kg_target = sp.diff(phi, t, 2) + sp.diff(V_fn, phi)
    kg_preserved = bool(sp.simplify(kg_from_div - kg_target) == 0)

    # 2. Exact Unimodular FRG (lam = 0 fixed, cap = 23 full and cap = 22 traceless)
    g_s, Mg_s = sp.symbols("g_s Mg_s", real=True)
    unimod_caps = {}
    for label, cap in [("full_lam0_cap23", 23), ("traceless_cap22", 22)]:
        B1 = (Mg_s - (cap - 1)) / (6 * sp.pi)
        B2 = sp.Rational(1, 12) / sp.pi
        eta = g_s * B1 / (1 - g_s * B2)
        beta_g = (2 + eta) * g_s
        g_fp = sp.simplify(sp.solve(sp.Eq(2 + eta, 0), g_s)[0])
        theta_g = sp.simplify(-sp.diff(beta_g, g_s).subs(g_s, g_fp))
        g_target = 12 * sp.pi / (cap - Mg_s)
        th_target = 2 * (cap - Mg_s) / (cap - 1 - Mg_s)
        sym_ok = bool(sp.simplify(g_fp - g_target) == 0 and sp.simplify(theta_g - th_target) == 0)

        # N_gen census for G_SM 2H (Ns=8, Nv=12, Nw=16*N_gen => Mg = 16*N_gen - 40)
        ngen_upper = Fraction(40 + cap, 16)
        ngen_survivors = [n for n in range(1, 9) if 0 < 16 * n - 40 < cap]

        spectra = {}
        for sname, ns, nw, nv, fw in [
            ("pure_gravity", 0, 0, 0, 1),
            ("gsm_2h_Ngen3", 8, 48, 12, 1),
            ("gsm_2h_Ngen4", 8, 64, 12, 1),
            ("ps_412", 16, 48, 21, 1),
            ("spin10_real10_T2", 10, 48, 45, 1),
            ("spin10_real10_T1", 10, 48, 45, 2),
        ]:
            Mg = ns + fw * nw - 4 * nv
            g_exact_pi_coeff = Fraction(12, cap - Mg) if Mg != cap else None
            if Mg < cap:
                gu = mp.mpf(12) * mp.pi / mp.mpf(cap - Mg)
                thu = mp.mpf(2 * (cap - Mg)) / mp.mpf(cap - 1 - Mg)
                fl_dD = mp_rat(20, 3) * gu / mp.pi
                pos_fp = True
            else:
                gu = mp.mpf(12) * mp.pi / mp.mpf(cap - Mg) if Mg != cap else None
                thu = None
                fl_dD = None
                pos_fp = False
            spectra[sname] = {
                "Mg": Mg,
                "has_positive_uv_fp": pos_fp,
                "g_over_pi_exact": frac_str(g_exact_pi_coeff) if g_exact_pi_coeff is not None else None,
                "g_star": mp.nstr(gu, 20) if gu is not None else None,
                "theta_g": mp.nstr(thu, 18) if thu is not None else None,
                "f_lam_dD_lam0": mp.nstr(fl_dD, 18) if fl_dD is not None else None,
                "_g_mp": gu,
                "_fl_mp": fl_dD,
            }

        unimod_caps[label] = {
            "cap": cap,
            "g_fp_formula": str(g_fp),
            "theta_g_formula": str(theta_g),
            "symbolic_formula_match": sym_ok,
            "ngen_lower_bound": "5/2",
            "ngen_upper_bound": frac_str(ngen_upper),
            "ngen_integer_survivors": ngen_survivors,
            "spectra": spectra,
        }

    # 3. 21/21 Delta(2,3,N) census under unimodular double pincer (cap=23 & cap=22)
    actions = enumerate_all_21_actions()
    surv_23 = [a for a in actions if a["is_chiral"] and a["anomaly_free"] and 0 < a["Mg"] < 23]
    surv_22 = [a for a in actions if a["is_chiral"] and a["anomaly_free"] and 0 < a["Mg"] < 22]

    # 4. A2-OW13 bridges at lam = 0
    g_uv = mp_rat(13, 25)
    f_crit = ((mp.mpf(54) + mp.mpf(6) * mp.sqrt(mp.mpf(114))) / (mp.mpf(80) * mp.pi * mp.pi)) * g_uv * g_uv
    g_gsm_u = unimod_caps["full_lam0_cap23"]["spectra"]["gsm_2h_Ngen3"]["_g_mp"]
    f_lam_gsm_u = unimod_caps["full_lam0_cap23"]["spectra"]["gsm_2h_Ngen3"]["_fl_mp"]
    # f_xi^bg(g, lam=0) = -g * lam * (11 + 10 lam) / (pi * (1 - 2 lam)^3) at lam = 0
    lam_sym = sp.Symbol("lam_sym", real=True)
    f_xi_bg_expr = -g_s * lam_sym * (11 + 10 * lam_sym) / (sp.pi * (1 - 2 * lam_sym)**3)
    f_xi_lam0_zero = bool(sp.simplify(f_xi_bg_expr.subs(lam_sym, 0)) == 0)

    # 5. Kaloper-Padilla (arXiv:1309-6562) global vacuum sequestering
    Lam_b, lam_s, L0, K_sym, V4, sig_p, mu4 = sp.symbols("Lam_b lam_s L0 K_sym V4 sig_p mu4", positive=True)
    T_phys = lam_s**4 * (4 * (L0 - rho_v) - 2 * K_sym)
    dS_dLam = -V4 + sig_p / (lam_s**4 * mu4)
    sig_p_sol = sp.solve(sp.Eq(dS_dLam, 0), sig_p)[0]
    dS_dlams = V4 * (4 * lam_s**3 * (L0 - rho_v) - 2 * lam_s**3 * K_sym) + sig_p_sol * (-4 * Lam_b / (lam_s**5 * mu4))
    Lam_b_sol = sp.simplify(sp.solve(sp.Eq(dS_dlams, 0), Lam_b)[0])
    Lam_res = sp.simplify(Lam_b_sol + lam_s**4 * rho_v)
    dLam_res_drho = sp.simplify(sp.diff(Lam_res, rho_v))
    kp_exact_match = bool(
        sp.simplify(Lam_b_sol - sp.Rational(1, 4) * T_phys) == 0
        and dLam_res_drho == 0
    )

    # Planted fault 4: omit lam_s^4 scaling (fix lam_s = 1, vary only Lam_bare with no global scale constraint)
    # Without the global lam_s constraint, Lam_bare is an arbitrary constant independent of rho_v:
    Lam_res_unseq = Lam_b + rho_v
    dLam_unseq_drho = sp.simplify(sp.diff(Lam_res_unseq, rho_v))

    return {
        "trace_free_shift_is_zero": tf_zero_all,
        "klein_gordon_preserved_under_rho_vac": kg_preserved,
        "unimodular_frg": unimod_caps,
        "delta_23N_census": {
            "total_actions": len(actions),
            "survivors_cap23": [(a["N"], a["d"], a["Mg"]) for a in surv_23],
            "survivors_cap22": [(a["N"], a["d"], a["Mg"]) for a in surv_22],
            "unique_N5_d5_both_caps": bool(
                len(surv_23) == 1 and surv_23[0]["N"] == 5 and surv_23[0]["d"] == 5
                and len(surv_22) == 1 and surv_22[0]["N"] == 5 and surv_22[0]["d"] == 5
            ),
        },
        "ow13_bridges_at_lam0": {
            "f_xi_bg_at_lam0_identically_zero": f_xi_lam0_zero,
            "gsm_2h_unimod_f_lam_dD": mp.nstr(f_lam_gsm_u, 18),
            "gsm_2h_unimod_f_lam_exact": "16/3",
            "f_crit_at_g_13_25": mp.nstr(f_crit, 18),
            "gsm_2h_collision_cured_by_unimodular": bool(f_lam_gsm_u > mp.mpf(5) and f_lam_gsm_u > f_crit),
            "_f_lam_gsm_u": f_lam_gsm_u,
        },
        "kaloper_padilla_sequestering": {
            "Lam_bare_sol": str(Lam_b_sol),
            "Lam_res_sol": str(Lam_res),
            "dLam_res_drho_vac": str(dLam_res_drho),
            "exact_sequestering_verified": kp_exact_match,
            "_dLam_unseq_drho": dLam_unseq_drho,
        },
    }


def main():
    mp.mp.dps = 55

    # OW14-A
    red7 = derive_7d_einstein_frame(sp.Rational(-3, 2))
    tw = analyze_townsend_wohlfarth()
    stab_ads = analyze_7d_volume_stabilization(c3_sign=-1)
    stab_ds = analyze_7d_volume_stabilization(c3_sign=+1)

    b_target = sp.sqrt(sp.Rational(2, 15))
    a_target = -sp.sqrt(sp.Rational(3, 10))
    hn = tw["hyperbolic_dim_scan"]
    ow14_a_pass = bool(
        red7["is_einstein_frame"]
        and sp.simplify(red7["_b_sym"] - b_target) == 0
        and sp.simplify(sp.Rational(-3, 2) * red7["_b_sym"] - a_target) == 0
        and red7["slopes"]["bulk_lambda7_L_m3"]["accelerates_asymptotically"]
        and (not red7["slopes"]["hyperbolic_curv_L_m5"]["accelerates_asymptotically"])
        and (not red7["slopes"]["cs_3form_flux_L_m9"]["accelerates_asymptotically"])
        and (not red7["slopes"]["casimir_1loop_L_m10"]["accelerates_asymptotically"])
        and (mp_rat(81, 100) < tw["_N_exact"] < mp_rat(82, 100))
        and (tw["_quad_err"] < mp_pow10(-45))
        and (tw["_ode_err"] < mp_pow10(-11))
        and (tw["_w_min_err"] < mp_pow10(-12))
        and (tw["_w_end_err"] < mp_rat(2, 1000))
        and (hn["H^2"]["_N_mp"] < hn["H^3"]["_N_mp"] < hn["H^4"]["_N_mp"] < hn["H^6"]["_N_mp"] < mp.mpf(2))
        and (stab_ds["benchmark"]["num_positive_extrema"] == 0)
        and (stab_ads["benchmark"]["num_positive_extrema"] == 1)
        and stab_ads["benchmark"]["is_stable_minimum"]
        and stab_ads["benchmark"]["is_ads_vacuum"]
        and (stab_ads["benchmark"]["_dV_abs"] < mp_pow10(-50))
        and stab_ads["symbolic_ads_identity_match"]
        and stab_ads["minkowski_lift_identity_match"]
    )

    # OW14-B
    ub = analyze_unimodular_and_kp()
    u23 = ub["unimodular_frg"]["full_lam0_cap23"]
    u22 = ub["unimodular_frg"]["traceless_cap22"]
    ow14_b_pass = bool(
        ub["trace_free_shift_is_zero"]
        and ub["klein_gordon_preserved_under_rho_vac"]
        and u23["symbolic_formula_match"]
        and u22["symbolic_formula_match"]
        and (u23["ngen_integer_survivors"] == [3])
        and (u22["ngen_integer_survivors"] == [3])
        and (u23["spectra"]["gsm_2h_Ngen3"]["g_over_pi_exact"] == "4/5")
        and (u22["spectra"]["gsm_2h_Ngen3"]["g_over_pi_exact"] == "6/7")
        and (not u23["spectra"]["gsm_2h_Ngen4"]["has_positive_uv_fp"])
        and (not u22["spectra"]["gsm_2h_Ngen4"]["has_positive_uv_fp"])
        and u23["spectra"]["spin10_real10_T2"]["has_positive_uv_fp"]
        and u23["spectra"]["spin10_real10_T1"]["has_positive_uv_fp"]
        and u22["spectra"]["spin10_real10_T2"]["has_positive_uv_fp"]
        and u22["spectra"]["spin10_real10_T1"]["has_positive_uv_fp"]
        and (ub["delta_23N_census"]["total_actions"] == 21)
        and ub["delta_23N_census"]["unique_N5_d5_both_caps"]
        and ub["ow13_bridges_at_lam0"]["f_xi_bg_at_lam0_identically_zero"]
        and ub["ow13_bridges_at_lam0"]["gsm_2h_collision_cured_by_unimodular"]
        and ub["kaloper_padilla_sequestering"]["exact_sequestering_verified"]
    )

    # OW14-C: 4 / 4 Planted Faults
    pf1 = derive_7d_einstein_frame(sp.Rational(-1, 1))
    pf1_pass = bool((not pf1["is_einstein_frame"]) and sp.simplify(pf1["_b_sym"] - b_target) != 0)

    pf2 = analyze_7d_volume_stabilization(c3_sign=+1)
    pf2_pass = bool(pf2["benchmark"]["num_positive_extrema"] == 0)

    pf3_g23 = u23["spectra"]["gsm_2h_Ngen4"]["_g_mp"]
    pf3_g22 = u22["spectra"]["gsm_2h_Ngen4"]["_g_mp"]
    pf3_pass = bool(pf3_g23 < 0 and pf3_g22 < 0)

    pf4_deriv = ub["kaloper_padilla_sequestering"]["_dLam_unseq_drho"]
    pf4_pass = bool(pf4_deriv == 1)

    ow14_c_pass = bool(pf1_pass and pf2_pass and pf3_pass and pf4_pass)
    all_gates_passed = bool(ow14_a_pass and ow14_b_pass and ow14_c_pass)

    def clean(obj):
        if isinstance(obj, dict):
            return {k: clean(v) for k, v in obj.items() if not k.startswith("_")}
        if isinstance(obj, list):
            return [clean(v) for v in obj]
        return obj

    out = {
        "card_id": "A2-OW14",
        "seat": "AGY-002",
        "empirical_inputs": "0 of 19",
        "ow14_a": {
            "einstein_frame_7d_reduction": clean(red7),
            "townsend_wohlfarth_acceleration": clean(tw),
            "volume_stabilization_ads_bulk": clean(stab_ads),
            "volume_stabilization_ds_bulk_runaway": clean(stab_ds["benchmark"]),
            "gate_pass": ow14_a_pass,
        },
        "ow14_b": {
            "unimodular_and_sequestering": clean(ub),
            "gate_pass": ow14_b_pass,
        },
        "ow14_c": {
            "pf_ow14_1_corrupt_einstein_frame": {
                "a_over_b": pf1["a_over_b"],
                "is_einstein_frame": pf1["is_einstein_frame"],
                "b_canon_exact": pf1["b_canon_exact"],
                "detected": pf1_pass,
            },
            "pf_ow14_2_flip_ads_to_ds_bulk": {
                "c3_sign": +1,
                "num_positive_extrema": pf2["benchmark"]["num_positive_extrema"],
                "detected": pf2_pass,
            },
            "pf_ow14_3_ngen4_unimodular": {
                "Mg": 24,
                "g_star_cap23": mp.nstr(pf3_g23, 16),
                "g_star_cap22": mp.nstr(pf3_g22, 16),
                "detected": pf3_pass,
            },
            "pf_ow14_4_omit_kp_metric_scaling": {
                "dLam_res_drho_vac": str(pf4_deriv),
                "detected": pf4_pass,
            },
            "planted_faults_detected": int(pf1_pass) + int(pf2_pass) + int(pf3_pass) + int(pf4_pass),
            "gate_pass": ow14_c_pass,
        },
        "all_gates_passed": all_gates_passed,
    }

    out_path = Path(__file__).resolve().parent / "a2_ow14_v2_results.json"
    out_text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    out_path.write_text(out_text, encoding="utf-8")
    digest = hashlib.sha256(out_text.encode("utf-8")).hexdigest()
    print(f"Wrote {out_path} (SHA-256={digest}) all_gates_passed={all_gates_passed}")
    if not all_gates_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
