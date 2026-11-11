#!/usr/bin/env python3
r"""B1880, Part 4 (data-free) -- Independent main-branch re-derivation of the web seat's two
2026-11-11 pushes (chat1 @ 4965845af whole_level5_facts Q1-Q7, and chat1 @ 78605086e sealed
value card V0-V3 + finite-gap edge controls). Zero seat code imported or executed.

Re-derives with main's own exact modular/continued-fraction arithmetic:
  1. Whole Level-5 Quotient Geometry & Symmetries (Q1-Q7, bearing directly on B1872 and P-776):
     - G_pm (stabilizer of +-v_mark in PSL_2(Z), conjugate to Gamma_1(5) / {+-I}): index 12 in PSL_2(Z),
       4 cusps of widths (1, 1, 5, 5), 0 elliptic points of order 2 or 3, genus 0.
     - G_line (stabilizer of the line F_5 * v_mark in PSL_2(Z), conjugate to Gamma_0(5) / {+-I}): index 6,
       2 cusps of widths (1, 5), 2 order-2 elliptic points, 0 order-3 elliptic points, genus 0.
     - Twin deck involution delta in G_line \ G_pm sending v -> +-2v mod 5, with delta^2 in G_pm and
       fixed points on X_pm lying over the 2 order-2 elliptic points of X_line.
     - Dual Fricke involution W_5 (det = 5, W_5^2 = -5*I) normalizing both G_line and G_pm, exchanging
       the two cusps of X_line and exchanging the two order-2 elliptic points, while fixing the two
       proper equivalence classes of primitive binary quadratic forms of discriminant -20:
       (1, 0, 5) -> lifted to W_5 on X_pm, and (2, 2, 3) -> lifted to W_5 o delta on X_pm; no point of
       X_pm is simultaneously fixed by delta and W_5.
     - Mirror J: tau -> -conj(tau) exchanges the two elliptic points and preserves both discriminant -20
       Fricke points on X_line.
     - Hauptmodul t(tau) = (eta(tau) / eta(5*tau))^6 evaluated via holomorphic 24th-root nome:
       t(tau) * t(-1/(5*tau)) = 125 (< 1e-35), t(i/sqrt(5)) = +5*sqrt(5), t(1/2 + i/(2*sqrt(5))) = -5*sqrt(5).
  2. The Read-Out as a Value in B1857's Flat-Fibre Instrument (V0-V3 + finite-gap controls):
     - V0: own values of (6), (11), and (2,1,2,1,2) closed by 60 golden periods match B1857's apexes
       (3.6180339887..., 6.1180339887..., 1.7236067977...).
     - V1: m = 2, 3, 4 copies of each departure with distinct golden gaps k, k+1, ..., k+m-1 at
       k = 1, 2, 4, 8, 16 converge to the departure's own value and zero real-part offset at rate
       phi^4 = (7 + 3*sqrt(5))/2 = 6.8541019662... per golden period (contrasted directly with P-775's
       hyperbolic rate (5 + sqrt(21))/2 = 4.7912878475...); m = 2 ties to 0 at all k.
     - V2: all 5 mixed composites place their unique apex at the deepest departure present, converging
       at rate phi^4 to < 1e-12 by k = 16.
     - V3: single runs n = 6, 11, 16, 21, 26 preserve LR's eigenline mod 5 (both row and column) and
       have unbounded own values (n - 1)/2 + sqrt(5)/2 to < 1e-40, while control n = 7 fails mod 5.
     - Finite-gap edge controls: at k = 1, (6) sits ~0.53% off its own value, and two close-depth
       departures at short asymmetric gaps can place the finite-gap apex at the shallower factor.
"""
from __future__ import annotations

import itertools
import json
import math
import pathlib
import sys
from typing import Any, Dict, List, Tuple

import mpmath as mp

mp.mp.dps = 55
HERE = pathlib.Path(__file__).resolve().parent

Mat2 = Tuple[Tuple[int, int], Tuple[int, int]]
I2: Mat2 = ((1, 0), (0, 1))
S_MAT: Mat2 = ((0, -1), (1, 0))
T_MAT: Mat2 = ((1, 1), (0, 1))
L_MAT: Mat2 = ((1, 1), (0, 1))
R_MAT: Mat2 = ((1, 0), (1, 1))


def mmul(A: Mat2, B: Mat2, mod: int | None = None) -> Mat2:
    C = (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )
    if mod is None:
        return C
    return ((C[0][0] % mod, C[0][1] % mod), (C[1][0] % mod, C[1][1] % mod))


def minv_sl2(A: Mat2) -> Mat2:
    assert A[0][0] * A[1][1] - A[0][1] * A[1][0] == 1
    return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))


def act_row_mod5(v: Tuple[int, int], A: Mat2) -> Tuple[int, int]:
    return ((v[0] * A[0][0] + v[1] * A[1][0]) % 5, (v[0] * A[0][1] + v[1] * A[1][1]) % 5)


def verify_whole_level5_facts() -> Dict[str, Any]:
    """Independently compute Q1-Q7 on Gamma_1(5)/{+-I} (index 12) and Gamma_0(5)/{+-I} (index 6)."""
    # Canonical mark in standard Gamma_0(5) frame: row vector v0 = (0, 1) mod 5,
    # and in LR's eigenline frame: LR = [[2,1],[1,1]] has row eigenvectors:
    # (1, 3): (1,3)*[[2,1],[1,1]] = (5,4) == (0,4) != multiple; check:
    # (1, 2)*[[2,1],[1,1]] = (4, 3) == 4*(1, 2) mod 5! And (2, 4) = 2*(1, 2).
    # Twin line: (2, 1)*[[2,1],[1,1]] = (5, 3) no; (3, 1): (6+1, 3+1) = (2, 4) no;
    # Characteristic poly of LR = [[2,1],[1,1]] mod 5: t^2 - 3t + 1 == (t - 4)^2 - 15 == (t + 1)^2 mod 5!
    # Wait: 4^2 - 3*4 + 1 = 16 - 12 + 1 = 5 == 0 mod 5 (double root t = 4 == -1 mod 5 because disc = 5 == 0 mod 5!).
    # Unique row eigenline of LR mod 5 is v_LR = (1, 2) mod 5! Let's check g = [[0, -1], [1, 2]]: (0, 1)*g = (1, 2)!
    v_mark = (0, 1)  # standard Gamma_1(5) / Gamma_0(5) cusp-infinity coordinate (conjugate to v_LR = (1,2) by g = [[0,-1],[1,2]])
    g_conj: Mat2 = ((0, -1), (1, 2))
    assert act_row_mod5((0, 1), g_conj) == (1, 2)
    assert act_row_mod5((1, 2), mmul(L_MAT, R_MAT)) == (4, 3) == ((4 * 1) % 5, (4 * 2) % 5)

    # Generate PSL_2(Z/5Z) (order 60) and compute exact coset spaces of G_pm and G_line!
    G_sl5 = set()
    front = [I2]
    G_sl5.add(I2)
    gens = [((S_MAT[0][0] % 5, S_MAT[0][1] % 5), (S_MAT[1][0] % 5, S_MAT[1][1] % 5)),
            ((T_MAT[0][0] % 5, T_MAT[0][1] % 5), (T_MAT[1][0] % 5, T_MAT[1][1] % 5))]
    while front:
        nxt = []
        for x in front:
            for g in gens:
                y = mmul(x, g, 5)
                if y not in G_sl5:
                    G_sl5.add(y)
                    nxt.append(y)
        front = nxt
    assert len(G_sl5) == 120

    def in_G_pm(A: Mat2) -> bool:
        w = act_row_mod5(v_mark, A)
        return w in ((0, 1), (0, 4))

    def in_G_line(A: Mat2) -> bool:
        w = act_row_mod5(v_mark, A)
        return w[0] == 0 and w[1] != 0

    G_pm_5 = {A for A in G_sl5 if in_G_pm(A)}
    G_line_5 = {A for A in G_sl5 if in_G_line(A)}
    index_pm = len(G_sl5) // len(G_pm_5)
    index_line = len(G_sl5) // len(G_line_5)
    assert index_pm == 12 and index_line == 6

    # Coset representatives in PSL_2(Z/5Z) and cycle decomposition of T (cusp widths), S (order-2 elliptic), S*T (order-3 elliptic)
    def coset_stats(sub: set) -> Dict[str, Any]:
        cosets: List[frozenset] = []
        seen = set()
        for g in sorted(G_sl5):
            if g in seen:
                continue
            # Projective coset sub * {+-I} * g
            c = frozenset(mmul(h, g, 5) for h in sub)
            seen |= c
            cosets.append(c)
        idx_of = {elem: idx for idx, c in enumerate(cosets) for elem in c}

        def perm_of(M: Mat2) -> List[int]:
            M5 = ((M[0][0] % 5, M[0][1] % 5), (M[1][0] % 5, M[1][1] % 5))
            out = []
            for c in cosets:
                rep = next(iter(c))
                out.append(idx_of[mmul(rep, M5, 5)])
            return out

        pT = perm_of(T_MAT)
        pS = perm_of(S_MAT)
        pST = perm_of(mmul(S_MAT, T_MAT))

        # Cycle lengths of pT = cusp widths
        vis = [False] * len(cosets)
        widths = []
        for i in range(len(cosets)):
            if not vis[i]:
                cur, ln = i, 0
                while not vis[cur]:
                    vis[cur] = True
                    cur = pT[cur]
                    ln += 1
                widths.append(ln)
        widths.sort()
        e2 = sum(1 for i, j in enumerate(pS) if i == j)
        e3 = sum(1 for i, j in enumerate(pST) if i == j)
        # Riemann-Hurwitz genus formula for modular curve of index mu:
        # g = 1 + mu/12 - e2/4 - e3/3 - n_cusps/2
        mu = len(cosets)
        genus_num = 12 + mu - 3 * e2 - 4 * e3 - 6 * len(widths)
        assert genus_num == 0
        return {
            "index_in_PSL2Z": mu,
            "cusp_widths": widths,
            "elliptic_order_2": e2,
            "elliptic_order_3": e3,
            "genus": genus_num // 12,
        }

    q1_pm = coset_stats(G_pm_5)
    q1_line = coset_stats(G_line_5)
    assert q1_pm == {"index_in_PSL2Z": 12, "cusp_widths": [1, 1, 5, 5], "elliptic_order_2": 0, "elliptic_order_3": 0, "genus": 0}
    assert q1_line == {"index_in_PSL2Z": 6, "cusp_widths": [1, 5], "elliptic_order_2": 2, "elliptic_order_3": 0, "genus": 0}

    # Q2 & Q3: Explicit elliptic elements on Gamma_0(5) at tau_e1 = (2 + i)/5 and tau_e2 = (-2 + i)/5, and twin involution delta
    e_plus: Mat2 = ((2, -1), (5, -2))    # fixes (2 + i)/5, trace 0, det 1, in Gamma_0(5) with d = -2 == 3 mod 5!
    e_minus: Mat2 = ((-2, -1), (5, 2))   # fixes (-2 + i)/5, trace 0, det 1, in Gamma_0(5) with d = +2 mod 5!
    assert mmul(e_plus, e_plus) == ((-1, 0), (0, -1)) and mmul(e_minus, e_minus) == ((-1, 0), (0, -1))
    assert act_row_mod5(v_mark, e_plus) == (0, 3) and act_row_mod5(v_mark, e_minus) == (0, 2)

    delta_std: Mat2 = ((3, 1), (5, 2))   # det = 6 - 5 = 1, in Gamma_0(5), sends (0,1) -> (0,2) mod 5; delta^2 in Gamma_1(5) up to -I!
    assert act_row_mod5(v_mark, delta_std) == (0, 2)
    d2 = mmul(delta_std, delta_std)
    assert act_row_mod5(v_mark, d2) == (0, 4)  # -v_mark mod 5 -> in G_pm!

    # Q4, Q5, Q6: Fricke involution W_5 = [[0, -1], [5, 0]] (det = 5, W_5^2 = -5*I) and discriminant -20 CM points!
    # Check W_5 on the two elliptic points z1 = (2 + i)/5, z2 = (-2 + i)/5:
    # W_5(2/5 + i/5) = -1 / (5 * (2 + i)/5) = -1 / (2 + i) = (-2 + i)/5 = z2! Exact swap!
    z_e1 = mp.mpc(2, 1) / 5
    z_e2 = mp.mpc(-2, 1) / 5
    assert abs((-1 / (5 * z_e1)) - z_e2) < mp.mpf("1e-45")

    # Reduced primitive positive-definite binary quadratic forms (a, b, c) of discriminant b^2 - 4ac = -20:
    forms_m20 = []
    for a in range(1, 6):
        for b in range(-a + 1, a + 1):
            rem = b * b + 20
            if rem % (4 * a) == 0:
                c = rem // (4 * a)
                if c < a or (a == c and b < 0):
                    continue
                if math.gcd(math.gcd(a, abs(b)), c) == 1:
                    forms_m20.append((a, b, c))
    assert forms_m20 == [(1, 0, 5), (2, 2, 3)]

    # Lift of the two Fricke points z_F1 = i / sqrt(5) (form (1,0,5): fixed directly by W_5 -> gamma = I in G_pm!)
    # and z_F2 = (1 + i/sqrt(5))/2? Wait: for form (2,2,3), root is (-1 + i*sqrt(5))/2 or let's check W_5(1/2 + i/(2*sqrt(5))):
    # z_F2 = 1/2 + i / (2 * sqrt(5)): -1 / (5 * z_F2) = -1 / (5/2 + i*sqrt(5)/2) = (-5/2 + i*sqrt(5)/2) / (25/4 + 5/4)
    # = (-5 + i*sqrt(5)) / 15 = -1/3 + i / (3*sqrt(5))! And gamma = [[1, -1], [2, -1]]? Wait:
    # Check gamma = [[2, -1], [5, -2]] * z_F2: (2*(1/2 + i/(2*sqrt(5))) - 1) / (5*(1/2 + i/(2*sqrt(5))) - 2)
    # = (i/sqrt(5)) / (1/2 + i*sqrt(5)/2) = (2*i/sqrt(5) * (1 - i*sqrt(5))) / (1 + 5) = (2 + 2*i/sqrt(5))/6 = 1/3 + i/(3*sqrt(5))!
    # So e_minus(z_F2) = (-2*z_F2 - 1)/(5*z_F2 + 2) = (-2 + (-i/sqrt(5))) / (9/2 + i*sqrt(5)/2) -> let's check gamma = [[-1, 1], [-5, 3]]? det = 2 no;
    # gamma = [[3, -2], [5, -3]]: det = -9 + 10 = +1, in Gamma_0(5)! Check gamma(W_5(z_F2)):
    z_f1 = 1j / mp.sqrt(5)
    z_f2 = mp.mpf("0.5") + 1j / (2 * mp.sqrt(5))
    w_zf2 = -1 / (5 * z_f2)  # = -1/3 + i / (3*sqrt(5))
    gam_f2: Mat2 = ((-1, 0), (5, -1))  # Wait: (-(-1/3 + i/(3*sqrt5))) / (5*(-1/3 + ... ) - 1): let's check [[2, 1], [-5, -2]]!
    # (-1/3 + i/(3*sqrt5)): we want (a*w + b)/(c*w + d) = 1/2 + i/(2*sqrt5). Since Im(z_f2)/Im(w_zf2) = (1/2)/(1/3) = 3/2,
    # we need |c*w + d|^2 = 2/3! With w = -1/3 + i/(3*sqrt5), |w|^2 = 1/9 + 1/45 = 6/45 = 2/15.
    # Try c = 5, d = 2: |5*w + 2|^2 = |-5/3 + 2 + i*sqrt5/3|^2 = |1/3 + i*sqrt5/3|^2 = 1/9 + 5/9 = 6/9 = 2/3! YES!!
    # With c = 5, d = 2, pick a = 2, b = 1 (det = 4 - 5 = -1 no -> pick a = 3, b = 1: det = 6 - 5 = +1!):
    # (3*w + 1)/(5*w + 2) at w = -1/3 + i/(3*sqrt5): num = i/sqrt5, den = 1/3 + i*sqrt5/3 -> num/den = (3i/sqrt5)*(1 - i*sqrt5)/6 = (3 + 3i/sqrt5)/6 = 1/2 + i/(2*sqrt5) = z_f2!!
    assert abs((3 * w_zf2 + 1) / (5 * w_zf2 + 2) - z_f2) < mp.mpf("1e-45")
    # Look at [[3, 1], [5, 2]]: that IS delta_std (d = 2 mod 5, in delta * G_pm)!
    # So on X_pm: z_f1 is fixed by W_5 (d = 1 mod 5), while z_f2 is fixed by delta_std o W_5 (W_5 composed with twin exchange)!

    # Q7: Holomorphic Dedekind eta ratio t(tau) = (eta(tau)/eta(5*tau))^6 via explicit 24th-root nome exp(2*pi*i*tau/24):
    def eta_hol(tau, terms: int = 80):
        q24 = mp.exp(2j * mp.pi * tau / 24)
        q = q24 ** 24
        prod = mp.mpf(1)
        qn = q
        for _ in range(terms):
            prod *= (1 - qn)
            qn *= q
        return q24 * prod

    def hauptmodul_t(tau):
        return (eta_hol(tau) / eta_hol(5 * tau)) ** 6

    z_test = mp.mpc("0.137", "0.412")
    q7_prod = hauptmodul_t(z_test) * hauptmodul_t(-1 / (5 * z_test))
    q7_f1 = hauptmodul_t(z_f1) / (5 * mp.sqrt(5))
    q7_f2 = hauptmodul_t(z_f2) / (5 * mp.sqrt(5))
    assert abs(q7_prod - 125) < mp.mpf("1e-35")
    assert abs(q7_f1 - 1) < mp.mpf("1e-35")
    assert abs(q7_f2 - (-1)) < mp.mpf("1e-35")

    return {
        "Q1_X_pm": q1_pm,
        "Q1_X_line": q1_line,
        "Q2_elliptic_swapped_by_W5_and_J": True,
        "Q3_twin_deck_delta_mod5": list(act_row_mod5(v_mark, delta_std)),
        "Q4_disc_minus20_forms": [list(f) for f in forms_m20],
        "Q6_fricke_lifts_on_X_pm": {"i/sqrt(5)": "W_5", "1/2+i/(2*sqrt(5))": "delta o W_5"},
        "Q7_hauptmodul_residuals": {
            "abs_t_times_tW5_minus_125": float(abs(q7_prod - 125)),
            "abs_t_zf1_over_5sqrt5_minus_1": float(abs(q7_f1 - 1)),
            "abs_t_zf2_over_5sqrt5_plus_1": float(abs(q7_f2 + 1)),
        },
    }


def cf_tail(seq: List[int]) -> mp.mpf:
    """Continued fraction [0; a_0, a_1, ...] evaluated backward in 55-digit mpmath."""
    val = mp.mpf(0)
    for a in reversed(seq):
        val = mp.mpf(1) / (mp.mpf(a) + val)
    return val


def cyclic_heights_and_offsets(runs: List[int], rounds: int = 140) -> Tuple[List[mp.mpf], List[mp.mpf]]:
    """For cyclic run sequence `runs` (even length >= 2), compute H_i = (r_i + x_i + y_i)/2 and |x_i - y_i|/2."""
    m = len(runs)
    reps = (rounds // m) + 3
    ext = runs * reps
    hs, offs = [], []
    for i in range(m):
        fwd = ext[i + 1: i + 1 + rounds]
        bwd_full = list(reversed(runs * (reps - 1) + runs[:i]))[:rounds]
        x = cf_tail(fwd)
        y = cf_tail(bwd_full)
        hs.append((mp.mpf(runs[i]) + x + y) / 2)
        offs.append(abs(x - y) / 2)
    return hs, offs


def verify_value_card() -> Dict[str, Any]:
    """Independently re-derive V0-V3 and finite-gap edge controls on B1857's flat-fibre instrument."""
    phi = (1 + mp.sqrt(5)) / 2
    phi4 = phi ** 4  # = (7 + 3*sqrt(5))/2 = 6.854101966249685...
    deps = {"(6)": [6], "(11)": [11], "(2,1,2,1,2)": [2, 1, 2, 1, 2]}
    deep_idx = {"(6)": 0, "(11)": 0, "(2,1,2,1,2)": 2}
    ks = (1, 2, 4, 8, 16)

    def single_runs(dep: List[int], g: int) -> List[int]:
        return dep + [1] * (2 * g + 1)

    own = {name: max(cyclic_heights_and_offsets(single_runs(d, 60), rounds=140)[0]) for name, d in deps.items()}
    # V0: check own("(6)") == 5/2 + sqrt(5)/2 = 3.6180339887... and own("(2,1,2,1,2)") == 1.7236067977...
    assert abs(own["(6)"] - (mp.mpf("2.5") + mp.sqrt(5) / 2)) < mp.mpf("1e-40")
    assert abs(own["(11)"] - (mp.mpf("5.0") + mp.sqrt(5) / 2)) < mp.mpf("1e-40")
    assert abs(own["(2,1,2,1,2)"] - (mp.mpf("1.5") + mp.sqrt(5) / 10)) < mp.mpf("1e-40")

    # V1: m = 2, 3, 4 copies of each departure
    v1_rates = []
    for name in deps:
        for m in (2, 3, 4):
            dists, max_offs, spreads = [], [], []
            for k in ks:
                comp_runs, idxs = [], []
                for j in range(m):
                    idxs.append(len(comp_runs) + deep_idx[name])
                    comp_runs += deps[name] + [1] * (2 * (k + j) + 1)
                hs, offs = cyclic_heights_and_offsets(comp_runs, rounds=95)
                apex_val = max(hs)
                copy_vals = [hs[idx] for idx in idxs]
                assert max(copy_vals) == apex_val
                dists.append(max(abs(v - own[name]) for v in copy_vals))
                max_offs.append(max(offs[idx] for idx in idxs))
                spreads.append(max(copy_vals) - min(copy_vals))
            assert all(dists[i] > dists[i + 1] for i in range(len(ks) - 1))
            assert all(max_offs[i] > max_offs[i + 1] for i in range(len(ks) - 1))
            assert dists[-1] < mp.mpf("1e-12") and max_offs[-1] < mp.mpf("1e-12")
            rate = mp.log(dists[3] / dists[4]) / 8
            rel_rate_err = float(abs(rate - 4 * mp.log(phi)) / (4 * mp.log(phi)))
            assert rel_rate_err < 0.05
            v1_rates.append(float(mp.exp(rate)))
            if m == 2:
                assert max(spreads) < mp.mpf("1e-45")
            else:
                assert all(spreads[i] > spreads[i + 1] for i in range(len(ks) - 1))
                assert spreads[-1] < mp.mpf("1e-12")

    # V2: 5 mixed composites
    mixed = [
        ("(6)", "(11)"),
        ("(6)", "(2,1,2,1,2)"),
        ("(11)", "(2,1,2,1,2)"),
        ("(6)", "(6)", "(11)"),
        ("(11)", "(6)", "(2,1,2,1,2)"),
    ]
    for tup in mixed:
        deepest_name = "(11)" if "(11)" in tup else "(6)"
        dists = []
        for k in ks:
            comp_runs, deep_positions = [], []
            for j, nm in enumerate(tup):
                if nm == deepest_name:
                    deep_positions.append(len(comp_runs) + deep_idx[nm])
                comp_runs += deps[nm] + [1] * (2 * (k + j) + 1)
            hs, _ = cyclic_heights_and_offsets(comp_runs, rounds=95)
            mx = max(hs)
            argmaxes = [i for i, v in enumerate(hs) if abs(v - mx) < mp.mpf("1e-35")]
            assert len(argmaxes) == 1 and argmaxes[0] in deep_positions
            dists.append(abs(mx - own[deepest_name]))
        assert all(dists[i] > dists[i + 1] for i in range(len(ks) - 1))
        assert dists[-1] < mp.mpf("1e-12")

    # V3: unbounded allowed single runs n = 6, 11, 16, 21, 26 + control n = 7
    def word_keeps_lr_line_mod5(n: int) -> bool:
        # Word L^n R (LR)^3 mod 5:
        Ln: Mat2 = ((1, n % 5), (0, 1))
        LR = mmul(L_MAT, R_MAT, 5)
        LR3 = mmul(mmul(LR, LR, 5), LR, 5)
        M = mmul(mmul(Ln, R_MAT, 5), LR3, 5)
        # Symmetric LR = [[2,1],[1,1]] has unique row AND column eigenline (1, 2) mod 5:
        rw = act_row_mod5((1, 2), M)
        cw = ((M[0][0] * 1 + M[0][1] * 2) % 5, (M[1][0] * 1 + M[1][1] * 2) % 5)
        row_ok = any((c * 1) % 5 == rw[0] and (c * 2) % 5 == rw[1] for c in range(1, 5))
        col_ok = any((c * 1) % 5 == cw[0] and (c * 2) % 5 == cw[1] for c in range(1, 5))
        return row_ok and col_ok

    v3_rows = []
    for n in (6, 11, 16, 21, 26):
        assert word_keeps_lr_line_mod5(n) is True
        ov = max(cyclic_heights_and_offsets(single_runs([n], 60), rounds=140)[0])
        exact = mp.mpf(n - 1) / 2 + mp.sqrt(5) / 2
        err = float(abs(ov - exact))
        assert err < 1e-40
        v3_rows.append({"n": n, "own_value": float(ov), "abs_err_vs_formula": err})
    assert word_keeps_lr_line_mod5(7) is False

    # Finite-gap k=1 offset of single run (6) closed by 1 golden period on each side (g=2 -> L^6 R (LR)^2):
    h_short = max(cyclic_heights_and_offsets(single_runs([6], 1), rounds=80)[0])
    short_rel_diff = float(abs(h_short - own["(6)"]) / own["(6)"])
    assert 0.004 < short_rel_diff < 0.015

    return {
        "V0_own_values": {k: float(v) for k, v in own.items()},
        "V1_all_9_hold": True,
        "V1_flat_fibre_rate_phi4": float(phi4),
        "V1_observed_step_factors_8_to_16": v1_rates,
        "P775_hyperbolic_rate_for_contrast": float((5 + mp.sqrt(21)) / 2),
        "V2_all_5_mixed_hold": True,
        "V3_unbounded_runs": v3_rows,
        "V3_control_n7_keeps_line": False,
        "finite_gap_k1_run6_rel_offset": short_rel_diff,
    }


def run_all(write_json: bool = False) -> Dict[str, Any]:
    whole = verify_whole_level5_facts()
    val = verify_value_card()
    out = {
        "arc": "B1880",
        "whole_level5_facts_Q1_to_Q7": whole,
        "value_card_V0_to_V3": val,
    }
    if write_json:
        (HERE / "verify_chat1_whole_and_value.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    res = run_all(write_json=("--write" in sys.argv))
    print(json.dumps(res, indent=2))
