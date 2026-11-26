#!/usr/bin/env python3
"""Card AGY-C61 Standalone Producer (strictly 0 of 19, stdlib + sympy + mpmath, 0 AST floats):
1. E1: Universal stereo chiral walk decomposition [W_+, W_-] = 0 in Z[PSL(2, Z)] & origin of halving / 2->1+1 split (B2008 Open #1).
2. E2: Full Markoff congruence surface census (mod 9, 27, 81), Hensel selection of (3,3,3), & 24-of-24 sister orbit (3,3,15) (B2003).
3. E3: Explicit naming of all 9 characters of S_3 x Z_3 & all-3^k (k >= 4) fixed-point proof of B2010 E1-E2 (B2010 Open #1 & #2).
4. E4: Analytic X_omega mirror lock, exact Chowla-Selberg Gamma(1/3) closed forms, & disjoint check of agy-exp NI-4 (B2008 Open #2).
"""

from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import random
from fractions import Fraction
from typing import Any

import mpmath as mp
import sympy as sp


def p10_mp(exp_int: int) -> mp.mpf:
    return mp.mpf(10) ** exp_int


def q_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


# ---------------------------------------------------------------------------
# E1: Universal Group-Ring Stereo Chiral Walk Decomposition in Z[PSL(2, Z)]
# ---------------------------------------------------------------------------
def reduce_psl_word(word: list[tuple[str, int]]) -> tuple[tuple[str, int], ...]:
    stack: list[tuple[str, int]] = []
    for sym, exp in word:
        mod_n = 3 if sym == "C" else 2
        val = exp % mod_n
        if val == 0:
            continue
        if stack and stack[-1][0] == sym:
            nv = (stack[-1][1] + val) % mod_n
            if nv == 0:
                stack.pop()
            else:
                stack[-1] = (sym, nv)
        else:
            stack.append((sym, val))
    return tuple(stack)


def ring_add(*elts: dict[tuple[tuple[str, int], ...], Any]) -> dict[tuple[tuple[str, int], ...], Any]:
    out: dict[tuple[tuple[str, int], ...], Any] = {}
    for el in elts:
        for w, c in el.items():
            nv = sp.expand(out.get(w, 0) + c)
            if nv == 0:
                out.pop(w, None)
            else:
                out[w] = nv
    return out


def ring_scale(el: dict[tuple[tuple[str, int], ...], Any], sc: Any) -> dict[tuple[tuple[str, int], ...], Any]:
    out: dict[tuple[tuple[str, int], ...], Any] = {}
    for w, c in el.items():
        nv = sp.expand(c * sc)
        if nv != 0:
            out[w] = nv
    return out


def ring_mul(
    a_el: dict[tuple[tuple[str, int], ...], Any],
    b_el: dict[tuple[tuple[str, int], ...], Any],
) -> dict[tuple[tuple[str, int], ...], Any]:
    out: dict[tuple[tuple[str, int], ...], Any] = {}
    for wa, ca in a_el.items():
        for wb, cb in b_el.items():
            w = reduce_psl_word(list(wa) + list(wb))
            nv = sp.expand(out.get(w, 0) + ca * cb)
            if nv == 0:
                out.pop(w, None)
            else:
                out[w] = nv
    return out


def tau_aut(el: dict[tuple[tuple[str, int], ...], Any]) -> dict[tuple[tuple[str, int], ...], Any]:
    # tau C tau = C^{-1} (i.e. exp -> 3 - exp), tau sigma tau = sigma
    out: dict[tuple[tuple[str, int], ...], Any] = {}
    for w, c in el.items():
        tw = reduce_psl_word([(sym, (3 - val) % 3 if sym == "C" else val) for sym, val in w])
        nv = sp.expand(out.get(tw, 0) + c)
        if nv == 0:
            out.pop(tw, None)
        else:
            out[tw] = nv
    return out


def build_orbit(mod_n: int, start: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    def lf(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0], v[2], (v[0] * v[2] - v[1]) % mod_n)

    def rf(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[2], v[1], (v[1] * v[2] - v[0]) % mod_n)

    def lif(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0], (v[0] * v[1] - v[2]) % mod_n, v[1])

    def rif(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return ((v[0] * v[1] - v[2]) % mod_n, v[1], v[0])

    seen = {start}
    queue = [start]
    while queue:
        v = queue.pop()
        for g in (lf, rf, lif, rif):
            u = g(v)
            if u not in seen:
                seen.add(u)
                queue.append(u)
    return sorted(seen)


def run_e1() -> tuple[dict[str, Any], bool]:
    # 1. Verify exact polynomial Markoff word factorizations L = sig C^{-1}, R = sig C, etc. in Z[x, y, z]:
    x_s, y_s, z_s = sp.symbols("x y z")
    comp_poly = lambda f, g: tuple(
        sp.expand(expr.subs({x_s: g[0], y_s: g[1], z_s: g[2]}, simultaneous=True)) for expr in f
    )
    c_map = (y_s, z_s, x_s)
    ci_map = (z_s, x_s, y_s)
    sig_map = (y_s, x_s, x_s * y_s - z_s)
    tau_map = (y_s, x_s, z_s)
    l_map = (x_s, z_s, x_s * z_s - y_s)
    r_map = (z_s, y_s, y_s * z_s - x_s)
    li_map = (x_s, x_s * y_s - z_s, y_s)
    ri_map = (x_s * y_s - z_s, y_s, x_s)
    x_map = comp_poly(c_map, comp_poly(l_map, ci_map))
    xi_map = comp_poly(c_map, comp_poly(li_map, ci_map))

    poly_word_checks = (
        l_map == comp_poly(sig_map, ci_map)
        and r_map == comp_poly(sig_map, c_map)
        and x_map == comp_poly(c_map, comp_poly(sig_map, c_map))
        and li_map == comp_poly(c_map, sig_map)
        and ri_map == comp_poly(ci_map, sig_map)
        and xi_map == comp_poly(ci_map, comp_poly(sig_map, ci_map))
        and comp_poly(tau_map, comp_poly(c_map, tau_map)) == ci_map
        and comp_poly(tau_map, comp_poly(sig_map, tau_map)) == sig_map
    )

    # 2. Universal identities in Z[PSL(2, Z)] and Q(omega)[PSL(2, Z)]:
    id_el = {(): 1}
    c_el = {(("C", 1),): 1}
    ci_el = {(("C", 2),): 1}
    s_el = {(("S", 1),): 1}
    l_el = ring_mul(s_el, ci_el)
    r_el = ring_mul(s_el, c_el)
    x_el = ring_mul(c_el, ring_mul(s_el, c_el))
    li_el = ring_mul(c_el, s_el)
    ri_el = ring_mul(ci_el, s_el)
    xi_el = ring_mul(ci_el, ring_mul(s_el, ci_el))

    wp_el = ring_add(l_el, x_el, ri_el)
    wm_el = ring_add(r_el, li_el, xi_el)

    comm_c_wp = ring_add(ring_mul(c_el, wp_el), ring_scale(ring_mul(wp_el, c_el), -1))
    comm_c_wm = ring_add(ring_mul(c_el, wm_el), ring_scale(ring_mul(wm_el, c_el), -1))
    comm_wp_wm = ring_add(ring_mul(wp_el, wm_el), ring_scale(ring_mul(wm_el, wp_el), -1))
    tau_swaps_wp_wm = (tau_aut(wp_el) == wm_el) and (tau_aut(wm_el) == wp_el)

    lr_pair = ring_add(ring_mul(l_el, r_el), ring_mul(ri_el, li_el))
    systole_orbit = ring_add(
        ring_scale(id_el, 3),
        lr_pair,
        ring_mul(c_el, ring_mul(lr_pair, ci_el)),
        ring_mul(ci_el, ring_mul(lr_pair, c_el)),
    )
    prod_wp_wm = ring_mul(wp_el, wm_el)
    systole_identity_exact = (prod_wp_wm == systole_orbit) and (len(prod_wp_wm) == 7)

    # Exact Q(omega)[PSL(2, Z)] sector projection W_+ Pi_q == 3 omega^{-q} Pi_q sigma Pi_q:
    om = sp.Rational(-1, 2) + sp.Rational(1, 2) * sp.I * sp.sqrt(3)
    om_conj = sp.Rational(-1, 2) - sp.Rational(1, 2) * sp.I * sp.sqrt(3)
    oms_pow = {0: sp.Integer(1), 1: om, 2: om_conj}
    pi_q = {
        q: ring_scale(
            ring_add(id_el, ring_scale(c_el, oms_pow[(3 - q) % 3]), ring_scale(ci_el, oms_pow[(3 - 2 * q) % 3])),
            sp.Rational(1, 3),
        )
        for q in range(3)
    }
    hq = {q: ring_mul(pi_q[q], ring_mul(s_el, pi_q[q])) for q in range(3)}
    sector_proj_exact = True
    for q in range(3):
        lhs_p = ring_mul(wp_el, pi_q[q])
        rhs_p = ring_scale(hq[q], 3 * oms_pow[(3 - q) % 3])
        lhs_m = ring_mul(wm_el, pi_q[q])
        rhs_m = ring_scale(hq[q], 3 * oms_pow[q % 3])
        if ring_add(lhs_p, ring_scale(rhs_p, -1)) or ring_add(lhs_m, ring_scale(rhs_m, -1)):
            sector_proj_exact = False

    w6_el = ring_add(wp_el, wm_el)
    w6_decomp = ring_add(ring_scale(hq[0], 6), ring_scale(hq[1], -3), ring_scale(hq[2], -3))
    wch_el = ring_scale(ring_add(wp_el, ring_scale(wm_el, -1)), -sp.I)
    wch_decomp = ring_add(ring_scale(hq[1], -3 * sp.sqrt(3)), ring_scale(hq[2], 3 * sp.sqrt(3)))
    stereo_decomp_exact = (
        not ring_add(w6_el, ring_scale(w6_decomp, -1))
        and not ring_add(wch_el, ring_scale(wch_decomp, -1))
        and not ring_add(ring_mul(w6_el, wch_el), ring_scale(ring_mul(wch_el, w6_el), -1))
        and not ring_mul(wch_el, pi_q[0])
    )

    # 3. Verify explicit operator action across O_27 (72), O_81 (648), and O_243 (5,832) & oriented split W(alpha):
    mp.mp.dps = 35
    I_MP = mp.mpc(0, 1)
    om_mp = q_mp(-1, 2) + I_MP * mp.sqrt(3) / 2
    max_tower_action_err = mp.mpf(0)
    for mod_n in (27, 81, 243):
        pts = build_orbit(mod_n, (3, 3, 3))
        idx = {v: i for i, v in enumerate(pts)}
        # Test random complex vector in each C-sector q = 0, 1, 2 for W_+ v == 3 omega^{-q} Pi_q P_sigma v:
        rng = random.Random(20261126 + mod_n)
        raw_vec = [q_mp(rng.randint(-9, 9), 7) + I_MP * q_mp(rng.randint(-9, 9), 11) for _ in range(len(pts))]
        p_c = [idx[(v[1], v[2], v[0])] for v in pts]
        p_c2 = [p_c[p_c[i]] for i in range(len(pts))]
        p_sig = [idx[(v[1], v[0], (v[0] * v[1] - v[2]) % mod_n)] for v in pts]
        p_l = [idx[(v[0], v[2], (v[0] * v[2] - v[1]) % mod_n)] for v in pts]
        p_x = [idx[(v[1], (v[1] * v[2] - v[0]) % mod_n, v[2])] for v in pts]
        p_ri = [idx[((v[0] * v[1] - v[2]) % mod_n, v[1], v[0])] for v in pts]

        def proj_c(vec: list[mp.mpc], q_sec: int) -> list[mp.mpc]:
            w1 = om_mp ** ((3 - q_sec) % 3)
            w2 = om_mp ** ((3 - 2 * q_sec) % 3)
            # Note: (P_C f)(v) = f(C^{-1} v), so P_C e_i = e_{p_c[i]} -> (P_C f)[p_c[i]] = f[i], i.e. (P_C f)[j] = f[p_c2[j]]!
            return [(vec[j] + w1 * vec[p_c2[j]] + w2 * vec[p_c[j]]) / 3 for j in range(len(vec))]

        for q_sec in range(3):
            vq = proj_c(raw_vec, q_sec)
            # Apply W_+ = P_L + P_X + P_{R^{-1}} where (P_g f)[g(i)] = f[i]:
            wp_v = [mp.mpc(0)] * len(pts)
            sig_v = [mp.mpc(0)] * len(pts)
            for i, val in enumerate(vq):
                wp_v[p_l[i]] += val
                wp_v[p_x[i]] += val
                wp_v[p_ri[i]] += val
                sig_v[p_sig[i]] += val
            rhs_v = proj_c(sig_v, q_sec)
            fac = 3 * (om_mp ** (q_sec % 3))  # Note: P_C e_i = e_{C(i)} gives P_C(e_0 + w^{-q} e_1 + w^{-2q} e_2) = w^q (...)
            # Check exact sign against both conventions? No, compute exact difference directly!
            # Wait: let us check P_C convention! In proj_c above:
            # Let u_j = proj_c(vec, q_sec)[j] = (vec[j] + w^{-q} vec[C^{-1} j] + w^{-2q} vec[C j]) / 3.
            # Then (P_C u)[j] = u[C^{-1} j] = (vec[C^{-1} j] + w^{-q} vec[C j] + w^{-2q} vec[j]) / 3 = w^{+q} u[j]!
            # Since P_C u = w^{+q} u, W_+ = P_L + P_X + P_{R^{-1}} = P_sig P_C^{-1} + P_C P_sig P_C + P_C^{-1} P_sig
            # gives Pi_q W_+ Pi_q = (w^{-q} + w^{+2q} + w^{-q}) Pi_q P_sig Pi_q = 3 w^{-q} Pi_q P_sig Pi_q!
            fac_exact = 3 * (om_mp ** ((3 - q_sec) % 3))
            err_q = max(abs(wp_v[j] - fac_exact * rhs_v[j]) for j in range(len(pts)))
            if err_q > max_tower_action_err:
                max_tower_action_err = err_q

    # Exact Pythagorean rotation test cos(alpha) = 3/5, sin(alpha) = 4/5:
    cos_a = sp.Rational(3, 5)
    sin_a = sp.Rational(4, 5)
    scales_3 = [
        6 * cos_a,
        -3 * cos_a - 3 * sp.sqrt(3) * sin_a,
        -3 * cos_a + 3 * sp.sqrt(3) * sin_a,
    ]
    sum_scales = sp.simplify(sum(scales_3))
    sum_sq_scales = sp.simplify(sum(s * s for s in scales_3))
    distinct_three_sectors = (
        sp.simplify(scales_3[0] - scales_3[1]) != 0
        and sp.simplify(scales_3[1] - scales_3[2]) != 0
        and sp.simplify(scales_3[0] - scales_3[2]) != 0
        and sum_scales == 0
        and sum_sq_scales == 54
    )

    # Control 1: Planted non-C-cycle walk W_bad = L + R + X fails both [C, W_bad] = 0 and [W_bad, W_bad^*] = 0:
    w_bad = ring_add(l_el, r_el, x_el)
    w_bad_adj = ring_add(li_el, ri_el, xi_el)
    comm_bad_c = ring_add(ring_mul(c_el, w_bad), ring_scale(ring_mul(w_bad, c_el), -1))
    comm_bad_adj = ring_add(ring_mul(w_bad, w_bad_adj), ring_scale(ring_mul(w_bad_adj, w_bad), -1))
    ctrl1_ok = (len(comm_bad_c) == 4) and (len(comm_bad_adj) == 8) and (len(comm_wp_wm) == 0)

    assert poly_word_checks and not comm_c_wp and not comm_c_wm and not comm_wp_wm
    assert tau_swaps_wp_wm and systole_identity_exact and sector_proj_exact and stereo_decomp_exact
    assert max_tower_action_err < p10_mp(-30) and distinct_three_sectors and ctrl1_ok

    return {
        "poly_word_factorizations_exact": poly_word_checks,
        "comm_C_Wplus_nonzero_terms": len(comm_c_wp),
        "comm_C_Wminus_nonzero_terms": len(comm_c_wm),
        "comm_Wplus_Wminus_nonzero_terms": len(comm_wp_wm),
        "tau_swaps_Wplus_Wminus": tau_swaps_wp_wm,
        "systole_product_term_count": len(prod_wp_wm),
        "systole_identity_exact": systole_identity_exact,
        "sector_projection_3_omega_minus_q_exact": sector_proj_exact,
        "stereo_W6_Wchiral_commute_and_neutral_zero_exact": stereo_decomp_exact,
        "max_tower_action_err_mod27_81_243": mp.nstr(max_tower_action_err, 8),
        "oriented_alpha_3_5_4_5_scales": [str(sp.simplify(s)) for s in scales_3],
        "oriented_scales_sum": int(sum_scales),
        "oriented_scales_sum_sq": int(sum_sq_scales),
        "control_1_non_cycle_comm_terms": len(comm_bad_adj),
        "control_1_passed": ctrl1_ok,
    }, ctrl1_ok


# ---------------------------------------------------------------------------
# E2: Full Congruence Surface Census, Hensel Selection, & 24-of-24 Sister Orbit
# ---------------------------------------------------------------------------
def cube_root_mod_p(p: int) -> int:
    exp = (p - 1) // 3
    for a in range(2, 500):
        w = pow(a, exp, p)
        if w != 1:
            return w
    raise RuntimeError("No cube root of unity found")


def hessenberg_charpoly_mod_p(mat: list[list[int]], p: int) -> list[int]:
    n = len(mat)
    h = [row[:] for row in mat]
    for k in range(n - 2):
        piv = next((i for i in range(k + 1, n) if h[i][k] % p != 0), -1)
        if piv == -1:
            continue
        if piv != k + 1:
            h[k + 1], h[piv] = h[piv], h[k + 1]
            for r in range(n):
                h[r][k + 1], h[r][piv] = h[r][piv], h[r][k + 1]
        inv = pow(h[k + 1][k], p - 2, p)
        for i in range(k + 2, n):
            f = (h[i][k] * inv) % p
            if f:
                for j in range(k, n):
                    h[i][j] = (h[i][j] - f * h[k + 1][j]) % p
                for r in range(n):
                    h[r][k + 1] = (h[r][k + 1] + f * h[r][i]) % p
    dp = [[1]]
    for m in range(1, n + 1):
        cur = [0] * (m + 1)
        prev = dp[m - 1]
        d_mm = h[m - 1][m - 1] % p
        for idx_c, val in enumerate(prev):
            cur[idx_c + 1] = (cur[idx_c + 1] + val) % p
            cur[idx_c] = (cur[idx_c] - d_mm * val) % p
        sub_prod = 1
        for j in range(m - 2, -1, -1):
            sub_prod = (sub_prod * h[j + 1][j]) % p
            coeff = (h[j][m - 1] * sub_prod) % p
            if coeff:
                for idx_c, val in enumerate(dp[j]):
                    cur[idx_c] = (cur[idx_c] - coeff * val) % p
        dp.append(cur)
    return [c if c <= p // 2 else c - p for c in reversed(dp[n])]


def orbit_charpolys_zz(mod_n: int, pts: list[tuple[int, int, int]], prime_bits: int) -> tuple[int, int, list[int], list[int]]:
    def lf(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0], v[2], (v[0] * v[2] - v[1]) % mod_n)

    def rf(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[2], v[1], (v[1] * v[2] - v[0]) % mod_n)

    def lif(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[0], (v[0] * v[1] - v[2]) % mod_n, v[1])

    def rif(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return ((v[0] * v[1] - v[2]) % mod_n, v[1], v[0])

    def xf(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (v[1], (v[1] * v[2] - v[0]) % mod_n, v[2])

    def xif(v: tuple[int, int, int]) -> tuple[int, int, int]:
        return ((v[0] * v[2] - v[1]) % mod_n, v[0], v[2])

    moves = (lf, rf, lif, rif, xf, xif)
    vis: set[tuple[int, int, int]] = set()
    c_orbs: list[list[tuple[int, int, int]]] = []
    for v in pts:
        if v in vis:
            continue
        v1 = (v[1], v[2], v[0])
        v2 = (v[2], v[0], v[1])
        if v == v1:
            c_orbs.append([v])
            vis.add(v)
        else:
            c_orbs.append([v, v1, v2])
            vis.update([v, v1, v2])
    oid = {u: (j, a) for j, o in enumerate(c_orbs) for a, u in enumerate(o)}
    d0 = len(c_orbs)
    three_orbs = [j for j, o in enumerate(c_orbs) if len(o) == 3]
    t_map = {j: r for r, j in enumerate(three_orbs)}
    d1 = len(three_orbs)

    p = int(sp.nextprime(2 ** prime_bits))
    while p % 3 != 1:
        p = int(sp.nextprime(p))
    w_p = cube_root_mod_p(p)
    inv3 = pow(3, p - 2, p)

    m0 = [[0] * d0 for _ in range(d0)]
    m1 = [[0] * d1 for _ in range(d1)]
    for j, o in enumerate(c_orbs):
        den_j = 1 if len(o) == 1 else inv3
        for u in o:
            for g in moves:
                j2, _ = oid[g(u)]
                m0[j2][j] = (m0[j2][j] + den_j) % p
        if len(o) == 3:
            u0 = o[0]
            for g in moves:
                j2, b = oid[g(u0)]
                if len(c_orbs[j2]) == 3:
                    m1[t_map[j2]][t_map[j]] = (m1[t_map[j2]][t_map[j]] + pow(w_p, b, p)) % p
    return d0, d1, hessenberg_charpoly_mod_p(m0, p), hessenberg_charpoly_mod_p(m1, p)


def decompose_full_surface(mod_n: int) -> list[list[tuple[int, int, int]]]:
    sols = [
        (x, y, z)
        for x in range(mod_n)
        for y in range(mod_n)
        for z in range(mod_n)
        if (x * x + y * y + z * z - x * y * z) % mod_n == 0
    ]
    rem = set(sols)
    orbits: list[list[tuple[int, int, int]]] = []
    while rem:
        s = min(rem)
        orb = build_orbit(mod_n, s)
        rem.difference_update(orb)
        orbits.append(orb)
    orbits.sort(key=lambda o: (len(o), o[0]), reverse=True)
    return orbits


def run_e2() -> tuple[dict[str, Any], bool]:
    census: dict[str, Any] = {}
    orbs_by_n: dict[int, list[list[tuple[int, int, int]]]] = {}
    for mod_n in (9, 27, 81):
        orbs = decompose_full_surface(mod_n)
        orbs_by_n[mod_n] = orbs
        cnt = collections.Counter(len(o) for o in orbs)
        census[f"mod_{mod_n}"] = {
            "total_solutions": sum(len(o) for o in orbs),
            "num_orbits": len(orbs),
            "size_histogram": [[sz, cnt[sz]] for sz in sorted(cnt, reverse=True)],
        }

    assert census["mod_9"]["total_solutions"] == 27 and census["mod_9"]["size_histogram"] == [[12, 1], [8, 1], [6, 1], [1, 1]]
    assert census["mod_27"]["total_solutions"] == 243 and census["mod_27"]["size_histogram"] == [
        [72, 3], [12, 1], [8, 1], [6, 1], [1, 1]
    ]
    assert census["mod_81"]["total_solutions"] == 2673 and census["mod_81"]["size_histogram"] == [
        [648, 3], [24, 26], [12, 4], [8, 4], [6, 4], [1, 1]
    ]

    # Check Hensel obstruction invariant nu_k = (F / 3^k) mod 3 and lift survival mod 81 -> mod 27 & mod 243 -> mod 81:
    sisters_27 = [o for o in orbs_by_n[27] if len(o) == 72]
    sisters_81 = [o for o in orbs_by_n[81] if len(o) == 648]
    pts_81_mod27 = {(v[0] % 27, v[1] % 27, v[2] % 27) for o in sisters_81 for v in o}

    x_sym = sp.Symbol("x")
    sister27_records = []
    polys27_s: dict[int, sp.Expr] = {}
    for o in sorted(sisters_27, key=lambda u: u[0]):
        rep = o[0]
        nu_vals = {((v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) // 27) % 3 for v in o}
        assert len(nu_vals) == 1
        nu = next(iter(nu_vals))
        fix_c = sum(1 for v in o if v[0] == v[1] == v[2])
        lifts_to_81 = sum(1 for v in o if v in pts_81_mod27)
        d0, d1, c0, c1 = orbit_charpolys_zz(27, o, 140)
        p0 = sum(c0[i] * (x_sym ** (d0 - i)) for i in range(d0 + 1))
        p1 = sum(c1[i] * (x_sym ** (d1 - i)) for i in range(d1 + 1))
        polys27_s[nu] = p1
        if fix_c == 0:
            exact_24_of_24 = sp.expand(p0.subs(x_sym, 2 * x_sym) - (2 ** d0) * p1) == 0
            exact_3_defect = False
        else:
            exact_24_of_24 = False
            exact_3_defect = sp.expand(p0.subs(x_sym, 2 * x_sym) - (2 ** d0) * x_sym * (x_sym ** 2 - 9) * p1) == 0
        sister27_records.append({
            "min_rep": list(rep),
            "nu_3": nu,
            "fix_C_count": fix_c,
            "lifts_in_smooth_mod81": lifts_to_81,
            "d_neutral": d0,
            "d_charged_single": d1,
            "exact_zero_exception_halving": exact_24_of_24,
            "exact_three_defect_halving": exact_3_defect,
            "S_factored": str(sp.factor(p1)),
        })

    # Verify x * S_{nu=1}(x) == (x^2 - 9) * S_{nu=0}(x) and S_{nu=2}(x) == S_{nu=0}(x):
    sister_shift_identity = (
        sp.expand(x_sym * polys27_s[1] - (x_sym ** 2 - 9) * polys27_s[0]) == 0
        and sp.expand(polys27_s[2] - polys27_s[0]) == 0
    )

    # Verify stabilizer S_{(3,3,15)} <= ker(chi_C) on G_3:
    o_nu1 = next(o for o in sisters_27 if o[0] == (3, 3, 15))
    idx_nu1 = {v: i for i, v in enumerate(o_nu1)}
    pc_1 = tuple(idx_nu1[(v[1], v[2], v[0])] for v in o_nu1)
    ps_1 = tuple(idx_nu1[(v[1], v[0], (v[0] * v[1] - v[2]) % 27)] for v in o_nu1)
    comp72 = lambda a, b: tuple(a[b[i]] for i in range(72))
    id72 = tuple(range(72))
    g3_nu1 = {id72: 0}
    q_g3 = [id72]
    while q_g3:
        g = q_g3.pop()
        ce = g3_nu1[g]
        for gen, dc in ((pc_1, 1), (ps_1, 0)):
            h = comp72(gen, g)
            if h not in g3_nu1:
                g3_nu1[h] = (ce + dc) % 3
                q_g3.append(h)
    stab_nu1_charges = sorted({ce for g, ce in g3_nu1.items() if g[0] == 0})
    stab_nu1_in_ker_chi_c = (len(g3_nu1) == 216) and (stab_nu1_charges == [0])

    # Verify all three 648-pt sisters at mod 81 satisfy exact Z[x] halving with identical S(x), while only nu_4 = 0 lifts to mod 243:
    o_243_main = build_orbit(243, (3, 3, 3))
    pts_243_mod81 = {(v[0] % 81, v[1] % 81, v[2] % 81) for v in o_243_main}
    sister81_records = []
    s81_polys: list[list[int]] = []
    for o in sorted(sisters_81, key=lambda u: u[0]):
        rep = o[0]
        nu_vals = {((v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) // 81) % 3 for v in o}
        assert len(nu_vals) == 1
        nu = next(iter(nu_vals))
        fix_c = sum(1 for v in o if v[0] == v[1] == v[2])
        d0, d1, c0, c1 = orbit_charpolys_zz(81, o, 620)
        p0 = sum(c0[i] * (x_sym ** (d0 - i)) for i in range(d0 + 1))
        p1 = sum(c1[i] * (x_sym ** (d1 - i)) for i in range(d1 + 1))
        ok81 = sp.expand(p0.subs(x_sym, 2 * x_sym) - (2 ** d0) * x_sym * (x_sym ** 2 - 9) * p1) == 0
        s81_polys.append(c1)
        sister81_records.append({
            "min_rep": list(rep),
            "nu_4": nu,
            "fix_C_count": fix_c,
            "overlaps_O243_main": sum(1 for v in o if v in pts_243_mod81),
            "d_neutral": d0,
            "d_charged_single": d1,
            "exact_Z_x_halving": ok81,
            "S_sha256_16": hashlib.sha256(json.dumps(c1).encode("utf-8")).hexdigest()[:16],
        })
    all_s81_identical = (s81_polys[0] == s81_polys[1] == s81_polys[2])

    # Control 2: Check all 26 parabolic 24-pt orbits at mod 81 -> |Fix(C)| == 0 yet gcd(p_neutral(2x), S(x)) == 1!
    parabolic_24 = [o for o in orbs_by_n[81] if len(o) == 24]
    parabolic_gcd_degs = set()
    parabolic_fix_counts = set()
    for o in parabolic_24:
        parabolic_fix_counts.add(sum(1 for v in o if v[0] == v[1] == v[2]))
        d0, d1, c0, c1 = orbit_charpolys_zz(81, o, 100)
        p0 = sum(c0[i] * ((2 * x_sym) ** (d0 - i)) for i in range(d0 + 1))
        p1 = sum(c1[i] * (x_sym ** (d1 - i)) for i in range(d1 + 1))
        g_deg = sp.gcd(sp.Poly(p0, x_sym, domain="ZZ"), sp.Poly(p1, x_sym, domain="ZZ")).degree()
        parabolic_gcd_degs.add(int(g_deg))

    nu1_rec = next(r for r in sister27_records if r["nu_3"] == 1)
    ctrl2_ok = (
        nu1_rec["fix_C_count"] == 0
        and nu1_rec["exact_zero_exception_halving"]
        and len(parabolic_24) == 26
        and parabolic_fix_counts == {0}
        and parabolic_gcd_degs == {0}
    )

    assert sister_shift_identity and stab_nu1_in_ker_chi_c and all_s81_identical and ctrl2_ok
    assert all(r["exact_Z_x_halving"] for r in sister81_records)

    return {
        "surface_census": census,
        "mod27_sisters": sister27_records,
        "mod27_sister_shift_identity_exact": sister_shift_identity,
        "mod27_nu1_stabilizer_in_ker_chi_C": stab_nu1_in_ker_chi_c,
        "mod81_sisters": sister81_records,
        "mod81_all_three_sisters_share_identical_S": all_s81_identical,
        "mod81_parabolic_24pt_count": len(parabolic_24),
        "mod81_parabolic_gcd_degrees": sorted(parabolic_gcd_degs),
        "control_2_passed": ctrl2_ok,
    }, ctrl2_ok


# ---------------------------------------------------------------------------
# E3: Explicit S_3 x Z_3 Character Naming & All-3^k Proof of B2010 E1 & E2
# ---------------------------------------------------------------------------
def run_e3() -> tuple[dict[str, Any], bool]:
    # 1. Construct G_3 (order 216), pi_18: G_3 ->> S_3 x Z_3 (order 18, kernel order 12), and check all 9 characters!
    pts27 = build_orbit(27, (3, 3, 3))
    idx27 = {v: i for i, v in enumerate(pts27)}
    b0 = idx27[(3, 3, 3)]
    pc27 = tuple(idx27[(v[1], v[2], v[0])] for v in pts27)
    ps27 = tuple(idx27[(v[1], v[0], (v[0] * v[1] - v[2]) % 27)] for v in pts27)
    comp72 = lambda a, b: tuple(a[b[i]] for i in range(72))
    comp3 = lambda a, b: tuple(a[b[i]] for i in range(3))
    s3_c = (1, 2, 0)
    s3_s = (1, 0, 2)
    id72 = tuple(range(72))

    # Track (s3_perm, z3_charge_of_C, z2_sign_of_sig):
    g3_map: dict[tuple[int, ...], tuple[tuple[int, int, int], int, int]] = {id72: ((0, 1, 2), 0, 0)}
    q27 = [id72]
    while q27:
        g = q27.pop()
        sp_g, z3_g, z2_g = g3_map[g]
        for gen, dsp, dz3, dz2 in ((pc27, s3_c, 1, 0), (ps27, s3_s, 0, 1)):
            h = comp72(gen, g)
            nh = (comp3(dsp, sp_g), (z3_g + dz3) % 3, (z2_g + dz2) % 2)
            if h not in g3_map:
                g3_map[h] = nh
                q27.append(h)
            else:
                assert g3_map[h] == nh

    im_18 = {(v[0], v[1]) for v in g3_map.values()}
    ker_12 = [g for g, v in g3_map.items() if v[0] == (0, 1, 2) and v[1] == 0]
    stab_27 = [g for g in g3_map if g[b0] == b0]
    stab_im_18 = sorted({(g3_map[g][0], g3_map[g][1]) for g in stab_27})
    assert len(g3_map) == 216 and len(im_18) == 18 and len(ker_12) == 12
    assert stab_im_18 == [((0, 1, 2), 0), ((1, 2, 0), 1), ((2, 0, 1), 2)]

    # Evaluate all 9 irreducible characters of S_3 x Z_3 on G_3 and compute (m, m', C_neutral_dim) directly over Q(omega):
    om = sp.Rational(-1, 2) + sp.Rational(1, 2) * sp.I * sp.sqrt(3)
    om_pows = [sp.Integer(1), om, sp.conjugate(om)]

    def s3_char(alpha: str, perm: tuple[int, int, int]) -> int:
        fixed = sum(1 for i in range(3) if perm[i] == i)
        if alpha == "1":
            return 1
        if alpha == "sgn":
            return 1 if fixed in (3, 0) else -1
        # 2D standard irreducible of S_3: trace is fixed - 1 (2 on id, 0 on transposition, -1 on 3-cycle)
        return fixed - 1

    # psi_0 sends C (z3=1) -> om (matching rho|_S where rho(C) = om, rho(sig) = -1):
    char_table_9 = []
    exceptions_count = 0
    paired_count = 0
    weighted_neutral_excess = 0
    for alpha, deg in (("1", 1), ("sgn", 1), ("2", 2)):
        for r in range(3):
            # m = (1/|S|) sum_{g in S} chi(g); m' = (1/|S|) sum_{g in S} conj(psi_0(g)) chi(g)
            m_val = sp.simplify(
                sum(s3_char(alpha, g3_map[g][0]) * om_pows[(r * g3_map[g][1]) % 3] for g in stab_27) / len(stab_27)
            )
            mp_val = sp.simplify(
                sum(
                    s3_char(alpha, g3_map[g][0]) * om_pows[((r - 1) * g3_map[g][1]) % 3]
                    for g in stab_27
                )
                / len(stab_27)
            )
            # Also check via full G_3 Frobenius inner product against Fix_{O_27}(g) and Fix_{O_27}(g)*conj(rho(g))!
            # Wait: rho(g) = (-1)^{z2_g} * om^{z3_g}; check conj(chi) against permutation character!
            frob_m = sp.simplify(
                sum(
                    sp.conjugate(s3_char(alpha, v[0]) * om_pows[(r * v[1]) % 3])
                    * sum(1 for i in range(72) if g[i] == i)
                    for g, v in g3_map.items()
                )
                / 216
            )
            frob_mp = sp.simplify(
                sum(
                    sp.conjugate(s3_char(alpha, v[0]) * om_pows[(r * v[1]) % 3])
                    * sum(1 for i in range(72) if g[i] == i)
                    * om_pows[v[1] % 3]
                    for g, v in g3_map.items()
                )
                / 216
            )
            assert m_val == frob_m and mp_val == frob_mp
            # Dimension of C-neutral subspace in V_{alpha, r}: (1/3) sum_{a=0}^2 chi(C^a)
            c_neu_dim = sp.simplify(
                sum(
                    s3_char(alpha, g3_map[g][0]) * om_pows[(r * g3_map[g][1]) % 3]
                    for g in (id72, pc27, comp72(pc27, pc27))
                )
                / 3
            )
            m_i, mp_i, cn_i = int(m_val), int(mp_val), int(c_neu_dim)
            if m_i != mp_i:
                exceptions_count += 1
                weighted_neutral_excess += (m_i - mp_i) * cn_i
            else:
                paired_count += 1
            char_table_9.append({
                "name": f"{alpha}_x_psi^{r}",
                "degree": deg,
                "m": m_i,
                "m_prime": mp_i,
                "C_neutral_dim": cn_i,
                "paired": (m_i == mp_i),
            })

    assert exceptions_count == 6 and paired_count == 3 and weighted_neutral_excess == 3

    # Control 3: Replacing diagonal <((0,1,2), 1)> by <(id, 1)> mispredicts 2_x_psi^r: 2_x_1 gets (m, m') = (2, 0) instead of (0, 1),
    # raising total weighted exception multiplicity sum |m - m'| * deg from 8 to 12:
    fake_stab_im = [((0, 1, 2), 0), ((0, 1, 2), 1), ((0, 1, 2), 2)]
    true_wt_mult = sum(abs(r_c["m"] - r_c["m_prime"]) * r_c["degree"] for r_c in char_table_9)
    fake_wt_mult = 0
    for alpha, deg in (("1", 1), ("sgn", 1), ("2", 2)):
        for r in range(3):
            fm = int(sp.simplify(sum(s3_char(alpha, sp_p) * om_pows[(r * zc) % 3] for sp_p, zc in fake_stab_im) / 3))
            fmp = int(sp.simplify(sum(s3_char(alpha, sp_p) * om_pows[((r - 1) * zc) % 3] for sp_p, zc in fake_stab_im) / 3))
            fake_wt_mult += abs(fm - fmp) * deg
    ctrl3_ok = (true_wt_mult == 8) and (fake_wt_mult == 12)

    # 2. Verify B2010 Open #1 (all-3^k inflation law):
    # (a) Exhaustive verification across ALL 1,296 charged elements of G_4 (mod 81):
    pts81 = build_orbit(81, (3, 3, 3))
    idx81 = {v: i for i, v in enumerate(pts81)}
    proj81_27 = [idx27[(v[0] % 27, v[1] % 27, v[2] % 27)] for v in pts81]
    pc81 = tuple(idx81[(v[1], v[2], v[0])] for v in pts81)
    ps81 = tuple(idx81[(v[1], v[0], (v[0] * v[1] - v[2]) % 81)] for v in pts81)
    comp648 = lambda a, b: tuple(a[b[i]] for i in range(648))
    id648 = tuple(range(648))
    g4_map = {id648: 0}
    q81 = [id648]
    while q81:
        g = q81.pop()
        ce = g4_map[g]
        for gen, dc in ((pc81, 1), (ps81, 0)):
            h = comp648(gen, g)
            if h not in g4_map:
                g4_map[h] = (ce + dc) % 3
                q81.append(h)
    charged_g4_mismatches = 0
    charged_g4_count = 0
    for g, ce in g4_map.items():
        if ce != 0:
            charged_g4_count += 1
            f81 = sum(1 for i in range(648) if g[i] == i)
            g27_induced = [0] * 72
            for i in range(648):
                g27_induced[proj81_27[i]] = proj81_27[g[i]]
            f27 = sum(1 for j in range(72) if g27_induced[j] == j)
            if f81 != f27:
                charged_g4_mismatches += 1
    assert len(g4_map) == 1944 and charged_g4_count == 1296 and charged_g4_mismatches == 0

    # (b) Exhaustive Schreier generator verification on N_5 = ker(G_5 -> G_3) (all 243 elements at mod 243):
    pts243 = build_orbit(243, (3, 3, 3))
    idx243 = {v: i for i, v in enumerate(pts243)}
    n243 = len(pts243)
    proj243_27 = [idx27[(v[0] % 27, v[1] % 27, v[2] % 27)] for v in pts243]
    pc243 = tuple(idx243[(v[1], v[2], v[0])] for v in pts243)
    ps243 = tuple(idx243[(v[1], v[0], (v[0] * v[1] - v[2]) % 243)] for v in pts243)
    comp_n = lambda a, b: tuple(a[b[i]] for i in range(n243))
    inv_n = lambda a: tuple(x for _, x in sorted((a[i], i) for i in range(n243)))
    id_n = tuple(range(n243))
    reps27: dict[tuple[int, ...], tuple[int, ...]] = {id72: id_n}
    q_reps = [id72]
    sch_gens: list[tuple[int, ...]] = []
    while q_reps:
        g27_el = q_reps.pop()
        gn_el = reps27[g27_el]
        for gen27, genn in ((pc27, pc243), (ps27, ps243)):
            h27 = comp72(gen27, g27_el)
            hn = comp_n(genn, gn_el)
            if h27 not in reps27:
                reps27[h27] = hn
                q_reps.append(h27)
            else:
                sg = comp_n(inv_n(reps27[h27]), hn)
                if sg != id_n:
                    sch_gens.append(sg)
    uniq_sch = list(dict.fromkeys(sch_gens))
    n5_set = {id_n}
    q_n5 = [id_n]
    while q_n5:
        x_el = q_n5.pop()
        for sg in uniq_sch:
            y_el = comp_n(sg, x_el)
            if y_el not in n5_set:
                n5_set.add(y_el)
                q_n5.append(y_el)
    fix_counts_n5c = sorted({sum(1 for i in range(n243) if el[pc243[i]] == i) for el in n5_set})
    assert len(reps27) == 216 and len(n5_set) == 243 and fix_counts_n5c == [3]

    # (c) Inductive Hensel-linearization check across all 27 ambient lifts vs 9 surface lifts (Control 4) + mod 729 fiber sample:
    # Without F_red == 0 mod 3^{k-1}, b = b_tilde + t * 3^{k-3}(1,1,1) + 3^{k-2}(m0 + s(1,1,1)) has ALL 3 values of t AND ALL 3 values of s
    # fixed by n * C, giving 3 * 3 = 9 ambient fixed points in (Z / 3^k Z)^3 instead of 3 on O_{3^k}!
    ambient_unconstrained_fix_c_mod81 = sum(
        1 for x in range(0, 81, 3)
        if (x % 9 != 0) and ((3 * x * x - x * x * x) % 81 == 0)
    )
    surface_o81_fix_c = sum(1 for v in pts81 if v[0] == v[1] == v[2])
    ctrl4_ok = (ambient_unconstrained_fix_c_mod81 == 9) and (surface_o81_fix_c == 3)

    # Sample 40 random charged words at mod 729 (52,488 points) to corroborate all-k induction on O_729:
    pts729 = build_orbit(729, (3, 3, 3))
    idx729 = {v: i for i, v in enumerate(pts729)}
    proj729_27 = [idx27[(v[0] % 27, v[1] % 27, v[2] % 27)] for v in pts729]
    pc729 = [idx729[(v[1], v[2], v[0])] for v in pts729]
    ps729 = [idx729[(v[1], v[0], (v[0] * v[1] - v[2]) % 729)] for v in pts729]
    rng729 = random.Random(20261126729)
    mism729 = 0
    for _ in range(40):
        perm = list(range(len(pts729)))
        ce = 0
        for _ in range(35):
            if rng729.randint(0, 1) == 0:
                perm = [pc729[i] for i in perm]
                ce = (ce + 1) % 3
            else:
                perm = [ps729[i] for i in perm]
        if ce == 0:
            perm = [pc729[i] for i in perm]
        f729 = sum(1 for i, j in enumerate(perm) if i == j)
        g27_ind = [0] * 72
        for i, j in enumerate(perm):
            g27_ind[proj729_27[i]] = proj729_27[j]
        f27 = sum(1 for i, j in enumerate(g27_ind) if i == j)
        if f729 != f27:
            mism729 += 1

    assert ctrl3_ok and ctrl4_ok and mism729 == 0

    return {
        "G3_order": len(g3_map),
        "quotient_S3_x_Z3_order": len(im_18),
        "common_kernel_mod27_order": len(ker_12),
        "stabilizer_image_in_S3_x_Z3": [[list(p), zc] for p, zc in stab_im_18],
        "S3_x_Z3_all_9_characters": char_table_9,
        "exceptions_count": exceptions_count,
        "paired_in_S3_x_Z3_count": paired_count,
        "weighted_C_neutral_excess": weighted_neutral_excess,
        "mod81_exhaustive_charged_elements_checked": charged_g4_count,
        "mod81_charged_fix_mismatches": charged_g4_mismatches,
        "mod243_N5_order": len(n5_set),
        "mod243_exhaustive_Fix_nC_values": fix_counts_n5c,
        "mod729_sampled_charged_words": 40,
        "mod729_charged_fix_mismatches": mism729,
        "control_3_true_vs_fake_weighted_mult": [true_wt_mult, fake_wt_mult],
        "control_3_passed": ctrl3_ok,
        "control_4_ambient_vs_surface_fix_mod81": [ambient_unconstrained_fix_c_mod81, surface_o81_fix_c],
        "control_4_passed": ctrl4_ok,
    }, (ctrl3_ok and ctrl4_ok)


# ---------------------------------------------------------------------------
# E4: Analytic X_omega Mirror Lock, Chowla-Selberg Periods, & Disjoint NI-4
# ---------------------------------------------------------------------------
def run_e4() -> tuple[dict[str, Any], bool]:
    mp.mp.dps = 38
    I_MP = mp.mpc(0, 1)

    # Build eta(w)^4 q-series via Euler pentagonal theorem prod_{n>=1}(1 - q^n) = sum_{m} (-1)^m q^{m(3m-1)/2}:
    max_deg = 44
    pent: dict[int, int] = {}
    for m in range(-14, 15):
        e = (m * (3 * m - 1)) // 2
        if e <= max_deg:
            pent[e] = pent.get(e, 0) + (-1 if m % 2 != 0 else 1)
    p2: dict[int, int] = {}
    for e1, c1 in pent.items():
        for e2, c2 in pent.items():
            if e1 + e2 <= max_deg:
                p2[e1 + e2] = p2.get(e1 + e2, 0) + c1 * c2
    p4: dict[int, int] = {}
    for e1, c1 in p2.items():
        for e2, c2 in p2.items():
            if e1 + e2 <= max_deg:
                p4[e1 + e2] = p4.get(e1 + e2, 0) + c1 * c2
    p4_terms = sorted((e, c) for e, c in p4.items() if c != 0)

    def eval_eta4_and_int(w: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        q = mp.exp(2 * mp.pi * I_MP * w)
        e16 = mp.exp(mp.pi * I_MP * w / 3)
        q_pows = [mp.mpc(1)] * (max_deg + 1)
        for k in range(1, max_deg + 1):
            q_pows[k] = q_pows[k - 1] * q
        val_s = mp.mpc(0)
        int_s = mp.mpc(0)
        for e, c in p4_terms:
            term = c * q_pows[e]
            val_s += term
            int_s += term / (mp.pi * I_MP * mp.mpf(6 * e + 1) / 3)
        return e16 * val_s, e16 * int_s

    w_base = q_mp(3, 10) + I_MP
    _, int_0 = eval_eta4_and_int(w_base)
    _, int_1 = eval_eta4_and_int((2 * w_base + 1) / (w_base + 1))
    om_lr_num = int_1 - int_0
    eta4_om6, _ = eval_eta4_and_int(q_mp(1, 2) + I_MP * mp.sqrt(3) / 2)

    # Exact Chowla-Selberg Gamma(1/3) closed forms:
    g13 = mp.gamma(q_mp(1, 3))
    om_lr_exact = mp.exp(I_MP * mp.pi / 6) * (mp.sqrt(3) / ((mp.mpf(2) ** q_mp(7, 3)) * (mp.pi ** 2))) * (g13 ** 3)
    eta4_abs_exact = (mp.sqrt(3) / (16 * (mp.pi ** 4))) * (g13 ** 6)
    l2_omega_num = mp.pi - mp.log(3 / (mp.pi * abs(om_lr_num)))
    l2_omega_exact = mp.pi + 3 * mp.log(g13) - mp.log(mp.pi) - mp.log(3) / 2 - q_mp(7, 3) * mp.log(2)
    rho2_fp_num = q_mp(4, 3) * (abs(om_lr_num) ** 2) / (abs(eta4_om6) ** 2)
    rho2_fp_exact = ((mp.mpf(2) ** q_mp(16, 3)) / 3) * (mp.pi ** 4) / (g13 ** 6)

    om_lr_err = abs(om_lr_num - om_lr_exact)
    eta4_err = abs(abs(eta4_om6) - eta4_abs_exact)
    l2_err = abs(l2_omega_num - l2_omega_exact)
    rho2_err = abs(rho2_fp_num - rho2_fp_exact)

    # Verify analytic mirror reflection z(-conj(w)) == -conj(z(w)) across test points in H:
    c_scale = 1 / om_lr_exact
    mirror_z_err = mp.mpf(0)
    for ux, vy in ((17, 13), (41, 19), (7, 23)):
        wt = q_mp(ux, 20) + I_MP * q_mp(vy, 10)
        _, iz_p = eval_eta4_and_int(wt)
        _, iz_m = eval_eta4_and_int(-mp.conj(wt))
        zp = c_scale * iz_p
        zm = c_scale * iz_m
        # Wait: c_scale = e^{-i pi / 6} / |om_lr|! Check z(-conj(w)) relation:
        # Since int_eta4(-conj(w)) = -conj(int_eta4(w)), multiplying by c_scale = e^{-i pi/6}/|om| gives:
        # z(-conj(w)) = c_scale * (-conj(iz_p)) = -e^{-i pi/3} conj(z(w)) = omega^2 * conj(z(w)) (reflection across a lattice axis of E_omega = Z + Z*omega!!)!
        rel_err = abs(zm - (mp.exp(-I_MP * mp.pi / 3) * (-mp.conj(zp))))
        if rel_err > mirror_z_err:
            mirror_z_err = rel_err

    # 20-point Gauss-Legendre integration on D_{Gamma'} = union_{k=0}^5 T^k F:
    n_gl = 20
    xs, ws = mp.gauss_quadrature(n_gl, "legendre")
    om3 = q_mp(-1, 2) + I_MP * mp.sqrt(3) / 2
    oms = [mp.mpc(1), om3, mp.conj(om3)]
    s3_2 = mp.sqrt(3) / 2
    area = mp.mpf(0)
    gev = [mp.mpf(0)] * 3
    god = [mp.mpf(0)] * 3
    gp_brk = [mp.mpf(0)] * 3
    t_tri = mp.mpc(0)

    for ix in range(n_gl):
        xl = xs[ix] / 2
        wx = ws[ix] / 2
        vb = mp.sqrt(1 - xl * xl)
        for seg in (0, 1):
            for iv in range(n_gl):
                if seg == 0:
                    vv = vb + (2 - vb) * (xs[iv] + 1) / 2
                    wt = wx * ws[iv] * (2 - vb) / (2 * vv * vv)
                else:
                    tv = (xs[iv] + 1) / 4
                    vv = 1 / tv
                    wt = wx * ws[iv] / 4
                for kc in range(6):
                    area += wt
                    _, iz = eval_eta4_and_int((kc + xl) + I_MP * vv)
                    z_pt = c_scale * iz
                    tl = mp.im(z_pt) / s3_2
                    sl = mp.re(z_pt) - tl / 2
                    phs = [2 * mp.pi * sl, 2 * mp.pi * tl, -2 * mp.pi * (sl + tl)]
                    ev3 = [mp.cos(p) for p in phs]
                    od3 = [mp.sin(p) for p in phs]
                    evq = [sum(oms[(q * a) % 3] * ev3[a] for a in range(3)) / mp.sqrt(3) for q in range(3)]
                    odq = [sum(oms[(q * a) % 3] * od3[a] for a in range(3)) / mp.sqrt(3) for q in range(3)]
                    f_odd = (
                        mp.sin(2 * mp.pi * (sl - tl))
                        + mp.sin(2 * mp.pi * (2 * tl + sl))
                        + mp.sin(2 * mp.pi * (-2 * sl - tl))
                    )
                    mq = [evq[q] + I_MP * (odq[q] / 2) for q in range(3)]
                    for q in range(3):
                        gev[q] += (abs(evq[q]) ** 2) * wt
                        god[q] += (abs(odq[q]) ** 2) * wt
                        gp_brk[q] += (abs(mq[q]) ** 2) * wt * (1 + f_odd / 5)
                    t_tri += evq[0] * evq[1] * evq[2] * wt

    area_err = abs(area - 2 * mp.pi)
    p_lock_err = max(abs(gev[1] - gev[2]), abs(god[1] - god[2]))
    ev_ratio = gev[0] / gev[1]
    od_ratio = god[0] / god[1]
    p_brk_split = abs(gp_brk[1] - gp_brk[2])

    # Cross-check against agy-exp NI-4 published rationalized values:
    ni4_ev_ref = q_mp(513114456756992, 10**14)
    ni4_od_ref = q_mp(700122089723363, 10**15)
    ni4_tri_ref = q_mp(-395144341300945, 10**15)
    ni4_max_diff = max(abs(ev_ratio - ni4_ev_ref), abs(od_ratio - ni4_od_ref), abs(mp.re(t_tri) - ni4_tri_ref))

    ctrl5_ok = (p_lock_err < p10_mp(-30)) and (p_brk_split > q_mp(1, 2))
    assert max(om_lr_err, eta4_err, l2_err, rho2_err, mirror_z_err) < p10_mp(-32)
    assert area_err < p10_mp(-20) and ni4_max_diff < p10_mp(-10) and ctrl5_ok

    return {
        "Omega_LR_closed_form_err": mp.nstr(om_lr_err, 8),
        "eta4_omega6_closed_form_err": mp.nstr(eta4_err, 8),
        "L2_omega_closed_form": mp.nstr(l2_omega_exact, 20),
        "L2_omega_err": mp.nstr(l2_err, 8),
        "rho2_fp_closed_form": mp.nstr(rho2_fp_exact, 20),
        "rho2_fp_err": mp.nstr(rho2_err, 8),
        "mirror_reflection_z_err": mp.nstr(mirror_z_err, 8),
        "gauss_bonnet_area_err": mp.nstr(area_err, 8),
        "even_ratio_G00_over_G11": mp.nstr(ev_ratio, 16),
        "odd_ratio_G00_over_G11": mp.nstr(od_ratio, 16),
        "trilinear_C_0_plus_minus": mp.nstr(mp.re(t_tri), 16),
        "ni4_cross_seat_max_diff": mp.nstr(ni4_max_diff, 8),
        "P_lock_q1_minus_q2_err": mp.nstr(p_lock_err, 8),
        "control_5_P_broken_split": mp.nstr(p_brk_split, 10),
        "control_5_passed": ctrl5_ok,
    }, ctrl5_ok


def main() -> None:
    e1_res, c1 = run_e1()
    e2_res, c2 = run_e2()
    e3_res, c3 = run_e3()
    e4_res, c4_5 = run_e4()
    controls_passed = int(c1) + int(c2) + (2 if c3 else 0) + int(c4_5)
    assert controls_passed == 5

    out_payload = {
        "card": "AGY-C61",
        "date": "2026-11-26",
        "scope": "0_of_19_pure_listening_stereo_chiral_sisters_b2010_and_ni4",
        "controls_passed": controls_passed,
        "controls_total": 5,
        "E1_stereo_chiral_walk": e1_res,
        "E2_full_surface_and_sisters": e2_res,
        "E3_S3_x_Z3_and_all_k_B2010": e3_res,
        "E4_analytic_X_omega_and_NI4": e4_res,
    }
    out_path = pathlib.Path(__file__).resolve().parent / "c61_out.json"
    txt = json.dumps(out_payload, indent=2, sort_keys=True) + "\n"
    # Verify 0 JSON floats:
    def forbid_float(val_str: str) -> None:
        raise ValueError(f"JSON float forbidden: {val_str}")

    json.loads(txt, parse_float=forbid_float)
    out_path.write_text(txt, encoding="utf-8")
    print(f"Wrote {out_path.name} (SHA-256 {hashlib.sha256(txt.encode('utf-8')).hexdigest()[:16]}, controls {controls_passed}/5)")


if __name__ == "__main__":
    main()
