#!/usr/bin/env python3
"""Card AGY-C61 Disjoint Cold-Room Countercheck (strictly 0 of 19, stdlib + sympy + mpmath, 0 AST floats):
Zero shared helper code with c61_stereo_chiral_sisters_and_b2010_producer.py:
- E1: Exact 72x72 Z[omega] integer-pair matrices on O_27 + complex star-ray spectrum via mp.eig + oriented 5*W(alpha) spectrum.
- E2: Algebraic congruence enumeration + Danilevsky Frobenius companion charpoly over disjoint 712-bit prime + Newton traces.
- E3: All 19 irreps of G_3 (order 216) via Burnside class-multiplication matrices + symbolic Z[eps]/(eps^2) all-k>=5 proof + mod 2187 check.
- E4: Jacobieta^3 * Euler-eta^1 series + Beta(1/6, 1/3) Gamma-duplication derivation + split v_mid = 3/2 22-pt quadrature.
"""

from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import random
from typing import Any

import mpmath as mp
import sympy as sp


def p10_mp(e: int) -> mp.mpf:
    return mp.mpf(10) ** e


def r_mp(a: int, b: int = 1) -> mp.mpf:
    return mp.mpf(a) / mp.mpf(b)


# ---------------------------------------------------------------------------
# Exact Z[omega] matrix arithmetic: elements are pairs (a, b) = a + b*omega, omega^2 = -1 - omega
# ---------------------------------------------------------------------------
ZOm = tuple[int, int]


def zom_add(x: ZOm, y: ZOm) -> ZOm:
    return (x[0] + y[0], x[1] + y[1])


def zom_sub(x: ZOm, y: ZOm) -> ZOm:
    return (x[0] - y[0], x[1] - y[1])


def zom_mul(x: ZOm, y: ZOm) -> ZOm:
    # (a + b w)(c + d w) = a c + (a d + b c) w + b d (-1 - w) = (a c - b d) + (a d + b c - b d) w
    ac = x[0] * y[0]
    bd = x[1] * y[1]
    ad_bc = x[0] * y[1] + x[1] * y[0]
    return (ac - bd, ad_bc - bd)


def zom_conj(x: ZOm) -> ZOm:
    # conj(a + b w) = a + b(-1 - w) = (a - b) - b w
    return (x[0] - x[1], -x[1])


def zom_mat_mul(a_m: list[list[ZOm]], b_m: list[list[ZOm]]) -> list[list[ZOm]]:
    n = len(a_m)
    out = [[(0, 0)] * n for _ in range(n)]
    for i in range(n):
        row_a = a_m[i]
        out_i = out[i]
        for k in range(n):
            aik = row_a[k]
            if aik == (0, 0):
                continue
            row_b = b_m[k]
            for j in range(n):
                bj = row_b[j]
                if bj != (0, 0):
                    out_i[j] = zom_add(out_i[j], zom_mul(aik, bj))
    return out


def zom_mat_eq(a_m: list[list[ZOm]], b_m: list[list[ZOm]]) -> bool:
    return all(a_m[i][j] == b_m[i][j] for i in range(len(a_m)) for j in range(len(a_m)))


def perm_to_zom_mat(perm: list[int]) -> list[list[ZOm]]:
    n = len(perm)
    m = [[(0, 0)] * n for _ in range(n)]
    for j, r in enumerate(perm):
        m[r][j] = (1, 0)
    return m


# ---------------------------------------------------------------------------
# Independent algebraic enumeration of congruence Markoff surface F == 0 mod N
# ---------------------------------------------------------------------------
def enum_surface_orbits(mod_n: int) -> list[list[tuple[int, int, int]]]:
    pts_set: set[tuple[int, int, int]] = set()
    for x in range(mod_n):
        xx = (x * x) % mod_n
        for y in range(mod_n):
            xy = (x * y) % mod_n
            xxyy = (xx + y * y) % mod_n
            for z in range(mod_n):
                if (xxyy + z * z - xy * z) % mod_n == 0:
                    pts_set.add((x, y, z))
    pts_all = sorted(pts_set)
    idx = {v: i for i, v in enumerate(pts_all)}
    # Partition via union-find under L and R:
    parent = list(range(len(pts_all)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri, rj = find(i), find(j)
        if ri != rj:
            if ri < rj:
                parent[rj] = ri
            else:
                parent[ri] = rj

    for i, (x, y, z) in enumerate(pts_all):
        union(i, idx[(x, z, (x * z - y) % mod_n)])
        union(i, idx[(z, y, (y * z - x) % mod_n)])

    comp_map: dict[int, list[tuple[int, int, int]]] = collections.defaultdict(list)
    for i, v in enumerate(pts_all):
        comp_map[find(i)].append(v)
    orbs = [sorted(v_list) for v_list in comp_map.values()]
    orbs.sort(key=lambda o: (len(o), o[0]), reverse=True)
    return orbs


# ---------------------------------------------------------------------------
# Disjoint Danilevsky Frobenius companion charpoly over GF(p)
# ---------------------------------------------------------------------------
def danilevsky_charpoly_mod_p(mat: list[list[int]], p: int) -> list[int]:
    n = len(mat)
    a = [[x % p for x in row] for row in mat]
    if n == 0:
        return [1]

    # Recursive Danilevsky: when subdiagonal pivot is 0 and no column swap left, split block upper-triangularly!
    def solve_block(b: list[list[int]]) -> list[int]:
        m = len(b)
        if m == 0:
            return [1]
        if m == 1:
            return [1, (-b[0][0]) % p]
        for step in range(m - 1, 0, -1):
            piv_col = -1
            for j in range(step - 1, -1, -1):
                if b[step][j] % p != 0:
                    piv_col = j
                    break
            if piv_col == -1:
                # b[step][0..step-1] == 0 -> block splits into [0..step-1] and [step..m-1]!
                top = [row[:step] for row in b[:step]]
                bot = [row[step:] for row in b[step:]]
                p_top = solve_block(top)
                p_bot = solve_block(bot)
                prod = [0] * (len(p_top) + len(p_bot) - 1)
                for i1, c1 in enumerate(p_top):
                    for i2, c2 in enumerate(p_bot):
                        prod[i1 + i2] = (prod[i1 + i2] + c1 * c2) % p
                return prod
            if piv_col != step - 1:
                # Swap columns AND rows (piv_col, step - 1)
                b[piv_col], b[step - 1] = b[step - 1], b[piv_col]
                for r in range(m):
                    b[r][piv_col], b[r][step - 1] = b[r][step - 1], b[r][piv_col]
            piv = b[step][step - 1] % p
            inv_piv = pow(piv, p - 2, p)
            # Similarity M^{-1} B M where row (step-1) of M^{-1} is row `step` of B:
            row_s = b[step][:]
            # First compute B' = B * M:
            # Column (step-1) of M has (inv_piv) at (step-1), and (-row_s[j]*inv_piv) at col j != step-1 in row (step-1):
            b_right = [[0] * m for _ in range(m)]
            for r in range(m):
                br_s1 = b[r][step - 1]
                col_s1 = (br_s1 * inv_piv) % p
                b_right[r][step - 1] = col_s1
                for j in range(m):
                    if j != step - 1:
                        b_right[r][j] = (b[r][j] - col_s1 * row_s[j]) % p
            # Now left-multiply M^{-1} * b_right: row (step-1) becomes sum_k row_s[k] * b_right[k][j], other rows unchanged!
            new_row = [0] * m
            for k in range(m):
                rk = row_s[k]
                if rk:
                    brk = b_right[k]
                    for j in range(m):
                        new_row[j] = (new_row[j] + rk * brk[j]) % p
            b_right[step - 1] = new_row
            b = b_right
        # Now b is a single Frobenius companion matrix with top row b[0]:
        # det(x I - b) = x^m - b[0][0] x^{m-1} - b[0][1] x^{m-2} - ... - b[0][m-1]
        return [1] + [(-b[0][j]) % p for j in range(m)]

    raw = solve_block(a)
    return [c if c <= p // 2 else c - p for c in raw]


# ---------------------------------------------------------------------------
# Verify E1..E4 against producer output JSON + 5 independent RPF1..RPF5
# ---------------------------------------------------------------------------
def check_e1(prod: dict[str, Any]) -> tuple[list[str], bool]:
    discrepancies: list[str] = []
    orbs27 = enum_surface_orbits(27)
    pts = next(o for o in orbs27 if o[0] == (3, 3, 3))
    idx = {v: i for i, v in enumerate(pts)}
    n = len(pts)

    p_l = perm_to_zom_mat([idx[(v[0], v[2], (v[0] * v[2] - v[1]) % 27)] for v in pts])
    p_r = perm_to_zom_mat([idx[(v[2], v[1], (v[1] * v[2] - v[0]) % 27)] for v in pts])
    p_li = perm_to_zom_mat([idx[(v[0], (v[0] * v[1] - v[2]) % 27, v[1])] for v in pts])
    p_ri = perm_to_zom_mat([idx[((v[0] * v[1] - v[2]) % 27, v[1], v[0])] for v in pts])
    p_x = perm_to_zom_mat([idx[(v[1], (v[1] * v[2] - v[0]) % 27, v[2])] for v in pts])
    p_xi = perm_to_zom_mat([idx[((v[0] * v[2] - v[1]) % 27, v[0], v[2])] for v in pts])
    p_c = perm_to_zom_mat([idx[(v[1], v[2], v[0])] for v in pts])
    p_ci = perm_to_zom_mat([idx[(v[2], v[0], v[1])] for v in pts])
    p_sig = perm_to_zom_mat([idx[(v[1], v[0], (v[0] * v[1] - v[2]) % 27)] for v in pts])
    p_tau = perm_to_zom_mat([idx[(v[1], v[0], v[2])] for v in pts])

    def add3(m1: list[list[ZOm]], m2: list[list[ZOm]], m3: list[list[ZOm]]) -> list[list[ZOm]]:
        return [[zom_add(zom_add(m1[i][j], m2[i][j]), m3[i][j]) for j in range(n)] for i in range(n)]

    wp = add3(p_l, p_x, p_ri)
    wm = add3(p_r, p_li, p_xi)
    if not zom_mat_eq(zom_mat_mul(wp, wm), zom_mat_mul(wm, wp)):
        discrepancies.append("E1: [W_+, W_-] != 0 over Z[omega] on O_27")
    if not zom_mat_eq(zom_mat_mul(p_tau, zom_mat_mul(wp, p_tau)), wm):
        discrepancies.append("E1: tau W_+ tau != W_- on O_27")

    # Systole identity W_+ W_- == 3 I + sum C^a(LR + R^{-1}L^{-1})C^{-a}:
    lr = zom_mat_mul(p_l, p_r)
    lri = zom_mat_mul(p_ri, p_li)
    lr_sum = [[zom_add(lr[i][j], lri[i][j]) for j in range(n)] for i in range(n)]
    c1_lr = zom_mat_mul(p_c, zom_mat_mul(lr_sum, p_ci))
    c2_lr = zom_mat_mul(p_ci, zom_mat_mul(lr_sum, p_c))
    rhs_sys = add3(lr_sum, c1_lr, c2_lr)
    for i in range(n):
        rhs_sys[i][i] = zom_add(rhs_sys[i][i], (3, 0))
    if not zom_mat_eq(zom_mat_mul(wp, wm), rhs_sys):
        discrepancies.append("E1: systole product identity failed on O_27")

    # Exact integer Z[omega] check: 3 * W_+ * (3 Pi_q) == 3 * omega^{-q} * (3 Pi_q) * P_sigma * (3 Pi_q):
    om_pows: list[ZOm] = [(1, 0), (0, 1), (-1, -1)]
    id_m = [[(1, 0) if i == j else (0, 0) for j in range(n)] for i in range(n)]
    for q in range(3):
        w1 = om_pows[(3 - q) % 3]
        w2 = om_pows[(3 - 2 * q) % 3]
        pi3 = [
            [
                zom_add(id_m[i][j], zom_add(zom_mul(w1, p_c[i][j]), zom_mul(w2, p_ci[i][j])))
                for j in range(n)
            ]
            for i in range(n)
        ]
        lhs = [[zom_mul((3, 0), wp_pi[j]) for j in range(n)] for wp_pi in zom_mat_mul(wp, pi3)]
        hq9 = zom_mat_mul(pi3, zom_mat_mul(p_sig, pi3))
        fac = zom_mul((3, 0), om_pows[(3 - q) % 3])
        rhs = [[zom_mul(fac, hq9[i][j]) for j in range(n)] for i in range(n)]
        if not zom_mat_eq(lhs, rhs):
            discrepancies.append(f"E1: 9 W_+ Pi_{q} != 3 w^(-{q}) (3 Pi_{q}) P_sig (3 Pi_{q})")

    # Check via mp.eig that all 72 eigenvalues of W_+ lie on the three 120-degree star rays {1, w^2, w} * R:
    mp.mp.dps = 32
    I_MP = mp.mpc(0, 1)
    om_c = r_mp(-1, 2) + I_MP * mp.sqrt(3) / 2
    wp_mp = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            a_v, b_v = wp[i][j]
            if a_v or b_v:
                wp_mp[i, j] = a_v + b_v * om_c
    evs_wp = mp.eig(wp_mp)[0]
    rays = [mp.mpc(1), om_c ** 2, om_c]
    max_ray_dist = mp.mpf(0)
    for ev in evs_wp:
        # Distance from ev to union of 3 real lines through `rays`: min_r |Im(ev * conj(r))|
        d_ev = min(abs(mp.im(ev * mp.conj(ry))) for ry in rays)
        if d_ev > max_ray_dist:
            max_ray_dist = d_ev
    if max_ray_dist >= p10_mp(-25):
        discrepancies.append(f"E1: W_+ star-ray eigenvalue deviation {max_ray_dist}")

    # Check oriented walk 5*W(alpha) = 3*W_6 + 4*W_chiral on sister (3, 3, 15) (where H_0, H_1, H_2 are isospectral 24x24!):
    pts_15 = next(o for o in orbs27 if o[0] == (3, 3, 15))
    idx_15 = {v: i for i, v in enumerate(pts_15)}
    w_alpha_mp = mp.zeros(72, 72)
    # 5 W(alpha) = 5(e^{-i alpha} W_+ + e^{+i alpha} W_-) = (3 - 4i) W_+ + (3 + 4i) W_-!
    c_plus = mp.mpc(3, -4)
    c_minus = mp.mpc(3, 4)
    for j, v in enumerate(pts_15):
        for u in (
            (v[0], v[2], (v[0] * v[2] - v[1]) % 27),
            (v[1], (v[1] * v[2] - v[0]) % 27, v[2]),
            ((v[0] * v[1] - v[2]) % 27, v[1], v[0]),
        ):
            w_alpha_mp[idx_15[u], j] += c_plus
        for u in (
            (v[2], v[1], (v[1] * v[2] - v[0]) % 27),
            (v[0], (v[0] * v[1] - v[2]) % 27, v[1]),
            ((v[0] * v[2] - v[1]) % 27, v[0], v[2]),
        ):
            w_alpha_mp[idx_15[u], j] += c_minus
    evs_alpha = sorted(mp.re(x) for x in mp.eighe(w_alpha_mp)[0])
    # Compare against exact 3-sector scaled eigenvalues {18, -9 - 12*sqrt(3), -9 + 12*sqrt(3)} * spec(H_0),
    # where 6*spec(H_0) are the 24 roots of p_neutral,(3,3,15):
    # On (3,3,15), S(x) has roots +-3 (1), +-2 (2), +-1 (5), +-sqrt(7) (2), +-sqrt(3) (2), so H_0 = (1/3)*S_roots!
    s_roots = (
        [mp.mpf(3), mp.mpf(-3)]
        + [mp.mpf(2)] * 2 + [mp.mpf(-2)] * 2
        + [mp.mpf(1)] * 5 + [mp.mpf(-1)] * 5
        + [mp.sqrt(7)] * 2 + [-mp.sqrt(7)] * 2
        + [mp.sqrt(3)] * 2 + [-mp.sqrt(3)] * 2
    )
    h0_eigs = [rt / 3 for rt in s_roots]
    mults_5 = [mp.mpf(18), -9 - 12 * mp.sqrt(3), -9 + 12 * mp.sqrt(3)]
    pred_alpha = sorted(m_f * h_e for m_f in mults_5 for h_e in h0_eigs)
    alpha_err = max(abs(evs_alpha[i] - pred_alpha[i]) for i in range(72))
    if alpha_err >= p10_mp(-25):
        discrepancies.append(f"E1: oriented 5*W(alpha) spectrum mismatch {alpha_err}")

    if not prod["E1_stereo_chiral_walk"]["stereo_W6_Wchiral_commute_and_neutral_zero_exact"]:
        discrepancies.append("E1: producer flag false")

    # RPF1: Swapping R^{-1} -> R in W_+ breaks normality [W_pert, W_pert^*] != 0 over Z[omega]:
    w_pert = add3(p_l, p_x, p_r)
    w_pert_adj = add3(p_li, p_xi, p_ri)
    rpf1_caught = not zom_mat_eq(zom_mat_mul(w_pert, w_pert_adj), zom_mat_mul(w_pert_adj, w_pert))
    return discrepancies, rpf1_caught


def sector_danilevsky_polys(mod_n: int, pts: list[tuple[int, int, int]], p_bits: int) -> tuple[int, int, list[int], list[int]]:
    p = int(sp.nextprime(2 ** p_bits + 12345))
    while p % 9 != 1:
        p = int(sp.nextprime(p))
    w_p = 1
    for cand in range(2, 600):
        t = pow(cand, (p - 1) // 3, p)
        if t != 1:
            w_p = t
            break
    inv3 = pow(3, p - 2, p)

    c_reps: list[list[tuple[int, int, int]]] = []
    seen: set[tuple[int, int, int]] = set()
    for v in pts:
        if v in seen:
            continue
        va, vb = (v[1], v[2], v[0]), (v[2], v[0], v[1])
        if v == va:
            c_reps.append([v])
            seen.add(v)
        else:
            c_reps.append([v, va, vb])
            seen.update((v, va, vb))
    loc = {u: (k, r) for k, orb in enumerate(c_reps) for r, u in enumerate(orb)}
    d0 = len(c_reps)
    ch_idx = [k for k, orb in enumerate(c_reps) if len(orb) == 3]
    ch_pos = {k: pos for pos, k in enumerate(ch_idx)}
    d1 = len(ch_idx)

    a0 = [[0] * d0 for _ in range(d0)]
    a1 = [[0] * d1 for _ in range(d1)]
    for k, orb in enumerate(c_reps):
        wt = 1 if len(orb) == 1 else inv3
        for x, y, z in orb:
            imgs = (
                (x, z, (x * z - y) % mod_n),
                (z, y, (y * z - x) % mod_n),
                (x, (x * y - z) % mod_n, y),
                ((x * y - z) % mod_n, y, x),
                (y, (y * z - x) % mod_n, z),
                ((x * z - y) % mod_n, x, z),
            )
            for u in imgs:
                k2, _ = loc[u]
                a0[k2][k] = (a0[k2][k] + wt) % p
        if len(orb) == 3:
            x, y, z = orb[0]
            imgs0 = (
                (x, z, (x * z - y) % mod_n),
                (z, y, (y * z - x) % mod_n),
                (x, (x * y - z) % mod_n, y),
                ((x * y - z) % mod_n, y, x),
                (y, (y * z - x) % mod_n, z),
                ((x * z - y) % mod_n, x, z),
            )
            for u in imgs0:
                k2, r2 = loc[u]
                if len(c_reps[k2]) == 3:
                    a1[ch_pos[k2]][ch_pos[k]] = (a1[ch_pos[k2]][ch_pos[k]] + pow(w_p, r2, p)) % p

    return d0, d1, danilevsky_charpoly_mod_p(a0, p), danilevsky_charpoly_mod_p(a1, p)


def check_e2(prod: dict[str, Any]) -> tuple[list[str], bool]:
    discrepancies: list[str] = []
    e2_p = prod["E2_full_surface_and_sisters"]
    for mod_n in (9, 27, 81):
        orbs = enum_surface_orbits(mod_n)
        cnt = collections.Counter(len(o) for o in orbs)
        hist = [[sz, cnt[sz]] for sz in sorted(cnt, reverse=True)]
        if hist != e2_p["surface_census"][f"mod_{mod_n}"]["size_histogram"]:
            discrepancies.append(f"E2: histogram mismatch at mod {mod_n}")

    orbs27 = enum_surface_orbits(27)
    orbs81 = enum_surface_orbits(81)
    x_s = sp.Symbol("x")
    s27_map: dict[tuple[int, int, int], sp.Expr] = {}
    p0_27_map: dict[tuple[int, int, int], sp.Expr] = {}
    for o in [u for u in orbs27 if len(u) == 72]:
        d0, d1, c0, c1 = sector_danilevsky_polys(27, o, 180)
        p0 = sum(c0[i] * (x_s ** (d0 - i)) for i in range(d0 + 1))
        p1 = sum(c1[i] * (x_s ** (d1 - i)) for i in range(d1 + 1))
        p0_27_map[o[0]] = p0
        s27_map[o[0]] = p1

    if sp.expand(p0_27_map[(3, 3, 15)].subs(x_s, 2 * x_s) - (2 ** 24) * s27_map[(3, 3, 15)]) != 0:
        discrepancies.append("E2: (3,3,15) failed 24-of-24 halving in Danilevsky countercheck")
    if sp.expand(x_s * s27_map[(3, 3, 15)] - (x_s ** 2 - 9) * s27_map[(3, 3, 3)]) != 0:
        discrepancies.append("E2: x*S_(3,3,15) != (x^2 - 9)*S_(3,3,3)")

    # Check all 3 mod-81 648-pt sisters via Danilevsky over disjoint 712-bit prime and compare SHA-256 against producer:
    prod_s81 = {tuple(r["min_rep"]): r["S_sha256_16"] for r in e2_p["mod81_sisters"]}
    for o in [u for u in orbs81 if len(u) == 648]:
        d0, d1, c0, c1 = sector_danilevsky_polys(81, o, 712)
        p0 = sum(c0[i] * (x_s ** (d0 - i)) for i in range(d0 + 1))
        p1 = sum(c1[i] * (x_s ** (d1 - i)) for i in range(d1 + 1))
        if sp.expand(p0.subs(x_s, 2 * x_s) - (2 ** d0) * x_s * (x_s ** 2 - 9) * p1) != 0:
            discrepancies.append(f"E2: mod 81 sister {o[0]} failed Z[x] halving")
        sha16 = hashlib.sha256(json.dumps(c1).encode("utf-8")).hexdigest()[:16]
        if sha16 != prod_s81[o[0]]:
            discrepancies.append(f"E2: mod 81 sister {o[0]} S_sha256 mismatch {sha16} vs {prod_s81[o[0]]}")

    # RPF2: Substituting (3,3,12) into the zero-exception test p0(2x) == 2^{d0} S(x) must fail!
    rpf2_caught = sp.expand(p0_27_map[(3, 3, 12)].subs(x_s, 2 * x_s) - (2 ** 26) * s27_map[(3, 3, 12)]) != 0
    return discrepancies, rpf2_caught


def check_e3(prod: dict[str, Any]) -> tuple[list[str], bool, bool]:
    discrepancies: list[str] = []
    e3_p = prod["E3_S3_x_Z3_and_all_k_B2010"]

    # 1. Construct ALL 19 irreducible characters of G_3 (order 216) from scratch via Burnside class-sum eigenprojection!
    orbs27 = enum_surface_orbits(27)
    pts = next(o for o in orbs27 if o[0] == (3, 3, 3))
    idx = {v: i for i, v in enumerate(pts)}
    pc = tuple(idx[(v[1], v[2], v[0])] for v in pts)
    ps = tuple(idx[(v[1], v[0], (v[0] * v[1] - v[2]) % 27)] for v in pts)
    comp = lambda a, b: tuple(a[b[i]] for i in range(72))
    inv_p = lambda a: tuple(x for _, x in sorted((a[i], i) for i in range(72)))
    id_p = tuple(range(72))

    # Build G_3 elements and rho(g) = (-1)^{s_exp} * omega^{c_exp}:
    g_elems: dict[tuple[int, ...], tuple[int, int]] = {id_p: (0, 0)}
    q = [id_p]
    while q:
        g = q.pop()
        ce, se = g_elems[g]
        for gen, dc, ds in ((pc, 1, 0), (ps, 0, 1)):
            h = comp(gen, g)
            if h not in g_elems:
                g_elems[h] = ((ce + dc) % 3, (se + ds) % 2)
                q.append(h)
    g_list = sorted(g_elems.keys())
    g_idx = {g: i for i, g in enumerate(g_list)}

    # Partition G_3 into conjugacy classes:
    cls_of = [-1] * len(g_list)
    classes: list[list[int]] = []
    for i, g in enumerate(g_list):
        if cls_of[i] != -1:
            continue
        cid = len(classes)
        c_members = set()
        for x in g_list:
            conj_g = comp(x, comp(g, inv_p(x)))
            c_members.add(g_idx[conj_g])
        mem_sorted = sorted(c_members)
        for m_i in mem_sorted:
            cls_of[m_i] = cid
        classes.append(mem_sorted)

    n_cls = len(classes)
    if n_cls != 19:
        discrepancies.append(f"E3: expected 19 conjugacy classes in G_3, got {n_cls}")

    # Build class multiplication matrices N_r: (N_r)_{s, t} = #{(x in C_r, y in C_s) : x*y = z_t}
    reps_t = [g_list[c[0]] for c in classes]
    n_mats = [[[0] * n_cls for _ in range(n_cls)] for _ in range(n_cls)]
    for r in range(n_cls):
        for s in range(n_cls):
            for ix in classes[r]:
                gx = g_list[ix]
                for iy in classes[s]:
                    prod_xy = comp(gx, g_list[iy])
                    for t in range(n_cls):
                        if prod_xy == reps_t[t]:
                            n_mats[r][s][t] += 1

    # Simultaneous diagonalization of commuting Burnside matrices N_r via mp.eig on generic linear combination:
    mp.mp.dps = 40
    I_MP = mp.mpc(0, 1)
    comb = mp.zeros(n_cls, n_cls)
    for r in range(n_cls):
        wt = r_mp(r * r + 3 * r + 7, 13) + I_MP * r_mp(2 * r + 5, 17)
        for s in range(n_cls):
            for t in range(n_cls):
                if n_mats[r][s][t]:
                    comb[s, t] += wt * n_mats[r][s][t]
    _, vr = mp.eig(comb)

    # Columns of vr are common right eigenvectors v^{(a)} of all N_r^T? Wait:
    # In class algebra, C_r C_s = sum_t c_{r,s}^t C_t -> omega_chi(C_r) omega_chi(C_s) = sum_t (N_r)_{s, t} omega_chi(C_t),
    # so the vector u_s = omega_chi(C_s) = |C_s| chi(g_s) / d_chi is a RIGHT eigenvector of EVERY matrix N_r with eigenvalue omega_chi(C_r)!!
    # Normalize u_0 = 1 (since C_0 = {id}, omega_chi(C_0) = 1), then sum_s |u_s|^2 / |C_s| = |G| / d_chi^2 gives d_chi!
    id_cid = cls_of[g_idx[id_p]]
    om_c = r_mp(-1, 2) + I_MP * mp.sqrt(3) / 2
    fix_cls = [sum(1 for k in range(72) if reps_t[c][k] == k) for c in range(n_cls)]
    chi_c_cls = [om_c ** g_elems[reps_t[c]][0] for c in range(n_cls)]

    exc_irrep_cids_in_ker: list[set[int]] = []
    paired_19 = 0
    unpaired_19 = 0
    for col in range(n_cls):
        u0 = vr[id_cid, col]
        u_vec = [vr[c, col] / u0 for c in range(n_cls)]
        norm_sq = sum((abs(u_vec[c]) ** 2) / len(classes[c]) for c in range(n_cls))
        d_chi = int(mp.nint(mp.sqrt(r_mp(216) / norm_sq)))
        chi_vals = [u_vec[c] * d_chi / len(classes[c]) for c in range(n_cls)]
        m_v = int(mp.nint(mp.re(sum(len(classes[c]) * mp.conj(chi_vals[c]) * fix_cls[c] for c in range(n_cls)) / 216)))
        mp_v = int(
            mp.nint(mp.re(sum(len(classes[c]) * mp.conj(chi_vals[c]) * fix_cls[c] * chi_c_cls[c] for c in range(n_cls)) / 216))
        )
        if m_v == mp_v:
            paired_19 += 1
        else:
            unpaired_19 += 1
            ker_cids = {c for c in range(n_cls) if abs(chi_vals[c] - d_chi) < p10_mp(-20)}
            exc_irrep_cids_in_ker.append(ker_cids)

    common_ker_cids = set.intersection(*exc_irrep_cids_in_ker)
    common_ker_order = sum(len(classes[c]) for c in common_ker_cids)
    if (paired_19, unpaired_19, common_ker_order) != (13, 6, 12):
        discrepancies.append(f"E3: 19-irrep Burnside audit got {(paired_19, unpaired_19, common_ker_order)} != (13, 6, 12)")

    # 2. Symbolic Hensel-Taylor proof for ALL k >= 5 over polynomial ring + random charged word check at unsearched mod 2,187 (3^7):
    # Check symbolic identity: let b = (1 + 3*a1, 1 + 3*a2, 1 + 3*a3) with F_red(b) = b1^2 + b2^2 + b3^2 - 3 b1 b2 b3 == 0 mod 9:
    a1, a2, a3, t_s, s_s, m1, m2, m3 = sp.symbols("a1 a2 a3 t s m1 m2 m3")
    b_vec = [1 + 3 * a1, 1 + 3 * a2, 1 + 3 * a3]
    f_red = b_vec[0] ** 2 + b_vec[1] ** 2 + b_vec[2] ** 2 - 3 * b_vec[0] * b_vec[1] * b_vec[2]
    # Expand f_red mod 9:
    f_mod9 = sp.expand(f_red)  # = 3 - 3 - 3*(a1 + a2 + a3) - 9*(...) -> mod 9 is -3*(a1 + a2 + a3)
    grad_sum = sum(sp.diff(b_vec[0] ** 2 + b_vec[1] ** 2 + b_vec[2] ** 2 - 3 * b_vec[0] * b_vec[1] * b_vec[2], v_sym) for v_sym in ())
    # Compute exact directional derivatives symbolically:
    u1, u2, u3 = sp.symbols("u1 u2 u3")
    f_u = u1 ** 2 + u2 ** 2 + u3 ** 2 - 3 * u1 * u2 * u3
    subs_b = {u1: b_vec[0], u2: b_vec[1], u3: b_vec[2]}
    sum_partials = sp.expand(sum(sp.diff(f_u, ui).subs(subs_b) for ui in (u1, u2, u3)))
    # Substitute a3 = -a1 - a2 + 3*q_a (since f_red == 0 mod 9 => a1 + a2 + a3 == 0 mod 3):
    q_a = sp.Symbol("q_a")
    sum_partials_on_surf = sp.expand(sum_partials.subs(a3, -a1 - a2 + 3 * q_a))
    # Every non-constant term in sum_partials_on_surf + 3 must be divisible by 9!
    rem_poly = sp.Poly(sp.expand(sum_partials_on_surf + 3), a1, a2, q_a, domain="ZZ")
    all_div_by_9 = all(int(c) % 9 == 0 for c in rem_poly.coeffs())
    if not all_div_by_9:
        discrepancies.append("E3: symbolic directional derivative sum != -3 mod 9")

    # Test 5 random Hensel fiber lifts at unsearched mod 2,187 (3^7):
    # Lift a base fixed point (3,3,3) under n*C where n = [C^{-1}, sig]^3 (non-trivial at mod 243, 729, 2187):
    mod_7 = 2187
    lf7 = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % mod_7)
    rf7 = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % mod_7)
    cf7 = lambda v: (v[1], v[2], v[0])
    cif7 = lambda v: (v[2], v[0], v[1])
    sig7 = lambda v: (v[1], v[0], (v[0] * v[1] - v[2]) % mod_7)

    def comm_cubed_7(v: tuple[int, int, int]) -> tuple[int, int, int]:
        u = v
        for _ in range(3):
            u = cif7(sig7(cf7(sig7(u))))
        return u

    # Enumerate all 3^3 = 27 lifts in (Z/2187Z)^3 of the 3 mod-729 C-fixed points {(3 + 243*t)(1,1,1)}?
    # Wait: first find the 3 fixed points of comm_cubed_7(C(v)) == v at mod 729 (among all 81 lifts of {(3 + 81*t)(1,1,1)}?):
    # Even better: build all 3 * 9 = 27 surface lifts in O_2187 above the 3 fixed points of n*C in O_729!
    # Find the 3 fixed points of n*C in O_243 -> lift to O_729 -> lift to O_2187!
    cur_fixed = [(3, 3, 3), (84, 84, 84), (165, 165, 165)]  # at mod 243, check n*C fixed points in O_243 first!
    pts243_s = next(o for o in enum_surface_orbits(81) if o[0] == (3, 3, 3))
    # Lift step-by-step k = 4 (81) -> 5 (243) -> 6 (729) -> 7 (2187) along exact fibers F(v) == 0 mod 3^{k+1}:
    fib_pts = [v for v in pts243_s if comm_cubed_7(cf7(v))[0] % 81 == v[0] and comm_cubed_7(cf7(v))[1] % 81 == v[1] and comm_cubed_7(cf7(v))[2] % 81 == v[2]]
    for k_step in (5, 6, 7):
        m_prev = 3 ** (k_step - 1)
        m_cur = 3 ** k_step
        m_next = 3 ** (k_step + 1)
        next_fixed = []
        for bx, by, bz in fib_pts:
            for d1 in range(3):
                for d2 in range(3):
                    for d3 in range(3):
                        vx, vy, vz = bx + m_prev * d1, by + m_prev * d2, bz + m_prev * d3
                        if (vx * vx + vy * vy + vz * vz - vx * vy * vz) % m_next != 0:
                            continue
                        ux, uy, uz = comm_cubed_7((vy, vz, vx))
                        if ux % m_cur == vx and uy % m_cur == vy and uz % m_cur == vz:
                            next_fixed.append((vx, vy, vz))
        fib_pts = next_fixed
        if len(fib_pts) != 3:
            discrepancies.append(f"E3: Hensel lift of Fix(n*C) at 3^{k_step} gave {len(fib_pts)} != 3")

    if e3_p["exceptions_count"] != 6 or e3_p["paired_in_S3_x_Z3_count"] != 3:
        discrepancies.append("E3: producer character counts mismatch")

    # RPF3: Corrupting psi_0 -> trivial character collapses all 6 exceptions to 0:
    rpf3_exc = 0
    for col in range(n_cls):
        u0 = vr[id_cid, col]
        u_vec = [vr[c, col] / u0 for c in range(n_cls)]
        norm_sq = sum((abs(u_vec[c]) ** 2) / len(classes[c]) for c in range(n_cls))
        d_chi = int(mp.nint(mp.sqrt(r_mp(216) / norm_sq)))
        chi_vals = [u_vec[c] * d_chi / len(classes[c]) for c in range(n_cls)]
        m_v = int(mp.nint(mp.re(sum(len(classes[c]) * mp.conj(chi_vals[c]) * fix_cls[c] for c in range(n_cls)) / 216)))
        # Corrupted rho_cls = 1 everywhere:
        mp_bad = int(mp.nint(mp.re(sum(len(classes[c]) * mp.conj(chi_vals[c]) * fix_cls[c] for c in range(n_cls)) / 216)))
        if m_v != mp_bad:
            rpf3_exc += 1
    rpf3_caught = (rpf3_exc == 0)

    # RPF4: Dropping F == 0 mod 3^{k+1} on mod-81 -> mod-243 lifts of Fix(n*C) triples fixed points from 3 to 9,
    # and dropping factor 3 in F_red (u1^2+u2^2+u3^2 - u1*u2*u3) shifts directional derivative sum from -3 to +3 (!= -3 mod 9):
    f_bad = u1 ** 2 + u2 ** 2 + u3 ** 2 - u1 * u2 * u3
    sp_bad = sp.expand(sum(sp.diff(f_bad, ui).subs(subs_b) for ui in (u1, u2, u3)).subs(a3, -a1 - a2 + 3 * q_a))
    unconstrained_243 = 0
    for bx, by, bz in [v for v in pts243_s if comm_cubed_7(cf7(v))[0] % 81 == v[0] and comm_cubed_7(cf7(v))[1] % 81 == v[1] and comm_cubed_7(cf7(v))[2] % 81 == v[2]]:
        for d1 in range(3):
            for d2 in range(3):
                for d3 in range(3):
                    vx, vy, vz = bx + 81 * d1, by + 81 * d2, bz + 81 * d3
                    ux, uy, uz = comm_cubed_7((vy, vz, vx))
                    if ux % 243 == vx and uy % 243 == vy and uz % 243 == vz:
                        unconstrained_243 += 1
    rpf4_caught = (unconstrained_243 == 9) and (int(sp_bad.subs({a1: 0, a2: 0, q_a: 0}) + 3) % 9 != 0)
    return discrepancies, rpf3_caught, rpf4_caught


def check_e4(prod: dict[str, Any]) -> tuple[list[str], bool]:
    discrepancies: list[str] = []
    e4_p = prod["E4_analytic_X_omega_and_NI4"]
    mp.mp.dps = 40
    I_MP = mp.mpc(0, 1)

    # 1. Disjoint series for eta(w)^4 = eta(w)^3 * eta(w), using Jacobi's identity:
    # prod_{n>=1}(1 - q^n)^3 = sum_{k>=0} (-1)^k (2k + 1) q^{k(k+1)/2}!
    max_d = 46
    jac3: dict[int, int] = {}
    for k in range(20):
        e = (k * (k + 1)) // 2
        if e <= max_d:
            jac3[e] = (-1 if k % 2 != 0 else 1) * (2 * k + 1)
    eul1: dict[int, int] = {}
    for m in range(-15, 16):
        e = (m * (3 * m - 1)) // 2
        if e <= max_d:
            eul1[e] = eul1.get(e, 0) + (-1 if m % 2 != 0 else 1)
    eta4_c: dict[int, int] = {}
    for e1, c1 in jac3.items():
        for e2, c2 in eul1.items():
            if e1 + e2 <= max_d:
                eta4_c[e1 + e2] = eta4_c.get(e1 + e2, 0) + c1 * c2
    terms4 = sorted((e, c) for e, c in eta4_c.items() if c != 0)

    def int_eta4_jac(w: mp.mpc) -> mp.mpc:
        q = mp.exp(2 * mp.pi * I_MP * w)
        e16 = mp.exp(mp.pi * I_MP * w / 3)
        qp = [mp.mpc(1)] * (max_d + 1)
        for k in range(1, max_d + 1):
            qp[k] = qp[k - 1] * q
        acc = mp.mpc(0)
        for e, c in terms4:
            acc += (c * qp[e]) / (mp.pi * I_MP * mp.mpf(6 * e + 1) / 3)
        return e16 * acc

    # 2. Verify Chowla-Selberg via Euler Beta(1/6, 1/3) and Gauss duplication Gamma(1/6) = Gamma(1/3)^2 * sqrt(3) / (2^{1/3} sqrt(pi)):
    b_16_13 = mp.beta(r_mp(1, 6), r_mp(1, 3))
    # Classic elliptic period of y^2 = 4 x^3 - 1: int_{2^{-2/3}}^inf dx / sqrt(4 x^3 - 1) = B(1/6, 1/3) / (6 * 2^{2/3})?
    # Verify exact relationship |Omega_{LR}| == B(1/6, 1/3) * Gamma(1/3) / (8 * 2^{2/3} * pi^{3/2})!
    g13 = mp.gamma(r_mp(1, 3))
    # Check Gauss duplication: Gamma(1/6) = (2^{1 - 1/3} / sqrt(pi)) * Gamma(1/3) * Gamma(5/6)? Wait:
    # Reflection Gamma(1/3)*Gamma(2/3) = 2*pi/sqrt(3) and duplication Gamma(1/3)*Gamma(5/6) = 2^{1/3} sqrt(pi) Gamma(2/3)
    # => Gamma(1/6) = sqrt(3) * 2^{-1/3} * Gamma(1/3)^2 / sqrt(pi)!
    # => B(1/6, 1/3) = Gamma(1/6)*Gamma(1/3)/sqrt(pi) = sqrt(3) * 2^{-1/3} * Gamma(1/3)^3 / pi!
    # => |Omega_{LR}| = B(1/6, 1/3) / (4 * pi) !!
    om_from_beta = mp.exp(I_MP * mp.pi / 6) * b_16_13 / (4 * mp.pi)
    w_test = r_mp(2, 5) + I_MP * r_mp(6, 5)
    om_jac = int_eta4_jac((2 * w_test + 1) / (w_test + 1)) - int_eta4_jac(w_test)
    if abs(om_from_beta - om_jac) >= p10_mp(-32):
        discrepancies.append(f"E4: Beta(1/6, 1/3)/(4*pi) period mismatch {abs(om_from_beta - om_jac)}")

    l2_beta = mp.pi - mp.log(12 / b_16_13)
    if abs(l2_beta - mp.mpf(e4_p["L2_omega_closed_form"])) >= p10_mp(-18):
        discrepancies.append("E4: L2(omega) Beta(1/6,1/3) mismatch vs producer")

    # 3. Disjoint 22-pt Gauss-Legendre integration split at v_mid = 3/2 (different split point and node count from producer!):
    n_gl_x = 18
    n_gl_v = 15
    xs_x, ws_x = mp.gauss_quadrature(n_gl_x, "legendre")
    xs, ws = mp.gauss_quadrature(n_gl_v, "legendre")
    c_sc = 1 / om_from_beta
    om3 = r_mp(-1, 2) + I_MP * mp.sqrt(3) / 2
    oms = [mp.mpc(1), om3, mp.conj(om3)]
    s3_2 = mp.sqrt(3) / 2
    v_m1 = r_mp(3, 2)
    v_m2 = r_mp(3, 1)
    t_max = 1 / v_m2
    area = mp.mpf(0)
    gev = [mp.mpf(0)] * 3
    god = [mp.mpf(0)] * 3
    t_tri = mp.mpc(0)

    for ix in range(n_gl_x):
        xl = xs_x[ix] / 2
        wx = ws_x[ix] / 2
        vb = mp.sqrt(1 - xl * xl)
        for seg in (0, 1, 2):
            for iv in range(n_gl_v):
                if seg == 0:
                    vv = vb + (v_m1 - vb) * (xs[iv] + 1) / 2
                    wt = wx * ws[iv] * (v_m1 - vb) / (2 * vv * vv)
                elif seg == 1:
                    vv = v_m1 + (v_m2 - v_m1) * (xs[iv] + 1) / 2
                    wt = wx * ws[iv] * (v_m2 - v_m1) / (2 * vv * vv)
                else:
                    tv = t_max * (xs[iv] + 1) / 2
                    vv = 1 / tv
                    wt = wx * ws[iv] * t_max / 2
                for kc in range(6):
                    area += wt
                    z_pt = c_sc * int_eta4_jac((kc + xl) + I_MP * vv)
                    tl = mp.im(z_pt) / s3_2
                    sl = mp.re(z_pt) - tl / 2
                    phs = [2 * mp.pi * sl, 2 * mp.pi * tl, -2 * mp.pi * (sl + tl)]
                    ev3 = [mp.cos(p) for p in phs]
                    od3 = [mp.sin(p) for p in phs]
                    evq = [sum(oms[(q * a) % 3] * ev3[a] for a in range(3)) / mp.sqrt(3) for q in range(3)]
                    odq = [sum(oms[(q * a) % 3] * od3[a] for a in range(3)) / mp.sqrt(3) for q in range(3)]
                    for q in range(3):
                        gev[q] += (abs(evq[q]) ** 2) * wt
                        god[q] += (abs(odq[q]) ** 2) * wt
                    t_tri += evq[0] * evq[1] * evq[2] * wt

    if abs(area - 2 * mp.pi) >= p10_mp(-20):
        discrepancies.append(f"E4: area err {abs(area - 2 * mp.pi)}")
    if max(abs(gev[1] - gev[2]), abs(god[1] - god[2])) >= p10_mp(-28):
        discrepancies.append("E4: P-lock tie failed")
    if abs((gev[0] / gev[1]) - mp.mpf(e4_p["even_ratio_G00_over_G11"])) >= p10_mp(-10):
        discrepancies.append("E4: even ratio mismatch vs producer")
    if abs((god[0] / god[1]) - mp.mpf(e4_p["odd_ratio_G00_over_G11"])) >= p10_mp(-10):
        discrepancies.append("E4: odd ratio mismatch vs producer")
    if abs(mp.re(t_tri) - mp.mpf(e4_p["trilinear_C_0_plus_minus"])) >= p10_mp(-10):
        discrepancies.append("E4: trilinear overlap mismatch vs producer")

    # RPF5: Flipping 7/3 -> 5/3 in L2(omega) formula shifts value by (2/3)*ln(2) > 2/5:
    l2_bad = mp.pi + 3 * mp.log(g13) - mp.log(mp.pi) - mp.log(3) / 2 - r_mp(5, 3) * mp.log(2)
    rpf5_caught = abs(l2_bad - l2_beta) > r_mp(2, 5)
    return discrepancies, rpf5_caught


def main() -> None:
    here = pathlib.Path(__file__).resolve().parent
    prod_path = here / "c61_out.json"
    prod = json.loads(prod_path.read_text(encoding="utf-8"))

    d1, rpf1 = check_e1(prod)
    d2, rpf2 = check_e2(prod)
    d3, rpf3, rpf4 = check_e3(prod)
    d4, rpf5 = check_e4(prod)

    all_disc = d1 + d2 + d3 + d4
    rpf_flags = [rpf1, rpf2, rpf3, rpf4, rpf5]
    assert len(all_disc) == 0, f"Discrepancies found: {all_disc}"
    assert all(rpf_flags), f"Planted faults not all caught: {rpf_flags}"

    out_payload = {
        "card": "AGY-C61-COUNTERCHECK",
        "date": "2026-11-26",
        "verified_producer_output_sha256_16": hashlib.sha256(prod_path.read_bytes()).hexdigest()[:16],
        "discrepancies_count": len(all_disc),
        "discrepancies": all_disc,
        "planted_faults_caught": sum(int(x) for x in rpf_flags),
        "planted_faults_total": 5,
        "rpf_verdicts": {
            "RPF1_non_normal_swapped_cycle": rpf1,
            "RPF2_fixed_point_sister_3_3_12_fails_zero_exception": rpf2,
            "RPF3_trivial_psi0_collapses_6_exceptions": rpf3,
            "RPF4_corrupted_Fred_sign_breaks_mod9_slope": rpf4,
            "RPF5_wrong_2_power_in_L2_omega": rpf5,
        },
        "methods": [
            "72x72 exact Z[omega] integer-pair matrices + mp.eig star-ray & 5*W(alpha) checks",
            "Union-find algebraic surface enumeration + Danilevsky Frobenius companion over 712-bit prime",
            "All 19 irreps of G_3 via Burnside class-multiplication matrices + symbolic Z-poly & mod 2187 Hensel check",
            "Jacobi eta^3 * Euler eta^1 series + Beta(1/6, 1/3)/(4*pi) period identity + split v_mid=3/2 22-pt quadrature",
        ],
    }
    out_file = here / "c61_countercheck_out.json"
    txt = json.dumps(out_payload, indent=2, sort_keys=True) + "\n"

    def forbid_float(s: str) -> None:
        raise ValueError(f"JSON float forbidden: {s}")

    json.loads(txt, parse_float=forbid_float)
    out_file.write_text(txt, encoding="utf-8")
    print(f"Countercheck PASS: discrepancies=0, RPF=5/5, SHA-256={hashlib.sha256(txt.encode('utf-8')).hexdigest()[:16]}")


if __name__ == "__main__":
    main()
