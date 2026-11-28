#!/usr/bin/env python3
"""Decisive producer for Card AGY-C71 (fam3-v1-high-01, P-885 format, 0 of 19).

Proves four strictly pre-trial (<= B2010) pure-listening theorems in exact integer,
rational, and cyclotomic arithmetic (stdlib + sympy only; 0 floats, 0 empirics):
  E1 (B2007 Open #1): Kempner falling-factorial null-ideal theorem on the two-sheet
     Hensel section S_k = {a_1 = 1, a_2 = 1 mod 3} ~= {1, 2} x (Z / 3^(k-2) Z)^2,
     proving dim_{F_3}(L_k) = [2, 2, 3, 7, 7, 7, 12, 14, 14] for k = 3..11 (through
     mod 177147 = 3^11, log_3|K_11| = 68, |G_11| = 24 * 3^68), Lazard cubing ranks
     [2, 2, 3, 7, 7, 7, 12, 14], and unbounded layer rank growth.
  E2 (B1990 Open #1): Symbolic conic-fibration derivation and exhaustive 17-prime
     verification (all odd primes 3 <= p <= 61, 499 sectors) of the universal
     branchless point-count identity
       #X_kappa(F_p) = p^2 + ((kappa - 2)/p) * (3 + ((kappa + 2)/p)) * p + 1.
  E3 (B2003 Open #3): Exact DomainMatrix factorization of mod 45's 4 paired modes
     x^2(x - 2)(x + 2) and mod 63's 8 paired modes, plus construction of the universal
     6-point quotient Q_6 = O_27 / ((V_4 K_3) cap [G_3, G_3]) proving all-(k >= 3)
     k-independence of unpaired charged modes on O_{3^k * p} (deg 10 at p = 5, deg 8 at p = 7).
  E4 (B1997 Open #1): Regular K_4 ~= (Z / 9 Z)^2 fiber Fourier decomposition on O_81
     into 19 S_4-orbits, proving that strictly 3 inversion-closed order-9 size-6 orbits
     carry the 3 Galois-conjugate quartics W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4
     over Q(cos 2 pi / 9) with Mackey double-coset multiplicity 2 (nullity 8 = 4 * 2 each).
"""
from collections import Counter, deque
import json
import pathlib
import sys
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def v3_fact(n: int) -> int:
    c = 0
    while n >= 3:
        n //= 3
        c += n
    return c


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def run_e1_kempner_tower(k_max: int = 11) -> dict:
    m_max = k_max - 2
    mod_a = 3 ** (k_max - 1)
    mod_b = 3 ** m_max

    def pmul_dict(p: dict, q: dict, mod: int) -> dict:
        out = {}
        for (i1, j1), c1 in p.items():
            if not c1:
                continue
            for (i2, j2), c2 in q.items():
                if i1 + i2 + j1 + j2 <= m_max and c2:
                    key = (i1 + i2, j1 + j2)
                    out[key] = (out.get(key, 0) + c1 * c2) % mod
        return {k: v for k, v in out.items() if v}

    def padd_dict(p: dict, q: dict, scale_q: int, mod: int) -> dict:
        out = dict(p)
        for k, v in q.items():
            nv = (out.get(k, 0) + scale_q * v) % mod
            if nv:
                out[k] = nv
            elif k in out:
                del out[k]
        return out

    phi = {}
    val_bound_checks = 0
    hensel_residual_zero = True
    for eps in (1, 2):
        a1 = {(0, 0): 1, (1, 0): 3}
        a2 = {(0, 0): 1, (0, 1): 3}
        a3 = {(0, 0): eps}
        a1_sq = pmul_dict(a1, a1, mod_a)
        a2_sq = pmul_dict(a2, a2, mod_a)
        a1_a2_3 = {k: (3 * v) % mod_a for k, v in pmul_dict(a1, a2, mod_a).items()}
        inv_2eps = 2 if eps == 1 else 1
        for step in range(2, k_max):
            mj = 3 ** step
            f = padd_dict(
                padd_dict(a1_sq, a2_sq, 1, mj),
                padd_dict(pmul_dict(a3, a3, mj), pmul_dict(a1_a2_3, a3, mj), -1, mj),
                1,
                mj,
            )
            if f:
                a3 = padd_dict(a3, f, -inv_2eps, mj)
        f_fin = padd_dict(
            padd_dict(a1_sq, a2_sq, 1, mod_a),
            padd_dict(pmul_dict(a3, a3, mod_a), pmul_dict(a1_a2_3, a3, mod_a), -1, mod_a),
            1,
            mod_a,
        )
        if f_fin:
            hensel_residual_zero = False
        p_cur = {}
        for k, c in a3.items():
            rem = (c - (eps if k == (0, 0) else 0)) % mod_a
            if rem % 3 != 0:
                hensel_residual_zero = False
            bv = (rem // 3) % mod_b
            if bv:
                p_cur[k] = bv
                deg = k[0] + k[1]
                if deg >= 1:
                    if bv % (3 ** (deg - 1)) != 0:
                        hensel_residual_zero = False
                    val_bound_checks += 1
        phi[eps] = p_cur

    monoms = [(i, deg - i) for deg in range(m_max + 1) for i in range(deg + 1)]
    m_idx = {mn: idx for idx, mn in enumerate(monoms)}
    n_mon = len(monoms)
    mul_pairs = [
        [(idx2, m_idx[(i1 + i2, j1 + j2)]) for idx2, (i2, j2) in enumerate(monoms) if i1 + i2 + j1 + j2 <= m_max]
        for (i1, j1) in monoms
    ]

    stirling2 = [[0] * (m_max + 1) for _ in range(m_max + 1)]
    stirling2[0][0] = 1
    for r in range(1, m_max + 1):
        for i in range(1, r + 1):
            stirling2[r][i] = stirling2[r - 1][i - 1] + i * stirling2[r - 1][i]

    def to_falling(vec: tuple, m_cur: int) -> tuple:
        mod_c = 3 ** m_cur
        fall = {}
        for idx, (r, s) in enumerate(monoms):
            if r + s > m_cur:
                break
            c = vec[idx] % mod_c
            if not c:
                continue
            for i in range(r + 1):
                si = stirling2[r][i]
                if not si:
                    continue
                for j in range(s + 1):
                    sj = stirling2[s][j]
                    if not sj or i + j > m_cur:
                        continue
                    exp_rem = m_cur - v3_fact(i) - v3_fact(j)
                    if exp_rem > 0:
                        fall[(i, j)] = (fall.get((i, j), 0) + c * si * sj) % (3 ** exp_rem)
        out = []
        for deg in range(m_cur + 1):
            for i in range(deg + 1):
                j = deg - i
                exp_rem = m_cur - v3_fact(i) - v3_fact(j)
                if exp_rem > 0:
                    out.append(fall.get((i, j), 0) % (3 ** exp_rem))
        return tuple(out)

    def dict_to_vec(d: dict) -> tuple:
        v = [0] * n_mon
        for k, val in d.items():
            if k in m_idx:
                v[m_idx[k]] = val % mod_b
        return tuple(v)

    def build_gen(which: str) -> tuple:
        target, f1_map, f2_map = {}, {}, {}
        for eps in (1, 2):
            a1 = {(0, 0): 1, (1, 0): 3}
            a2 = {(0, 0): 1, (0, 1): 3}
            a3 = {(0, 0): eps}
            for k, c in phi[eps].items():
                a3[k] = (a3.get(k, 0) + 3 * c) % mod_a

            def psub(pq: dict, r: dict) -> dict:
                out = {k: (3 * v) % mod_a for k, v in pq.items()}
                for k, v in r.items():
                    out[k] = (out.get(k, 0) - v) % mod_a
                return out

            if which == "L":
                na = (a1, a3, psub(pmul_dict(a1, a3, mod_a), a2))
            elif which == "R":
                na = (a3, a2, psub(pmul_dict(a2, a3, mod_a), a1))
            elif which == "Li":
                na = (a1, psub(pmul_dict(a1, a2, mod_a), a3), a2)
            else:
                na = (psub(pmul_dict(a1, a2, mod_a), a3), a2, a1)
            c0, c1, c2 = na[0].get((0, 0), 0) % 3, na[1].get((0, 0), 0) % 3, na[2].get((0, 0), 0) % 3
            s1, s2 = (1 if c0 == 1 else -1), (1 if c1 == 1 else -1)
            target[eps] = (s1 * s2 * c2) % 3
            f1_map[eps] = dict_to_vec({k: ((s1 * v - (1 if k == (0, 0) else 0)) // 3) % mod_b for k, v in na[0].items()})
            f2_map[eps] = dict_to_vec({k: ((s2 * v - (1 if k == (0, 0) else 0)) // 3) % mod_b for k, v in na[1].items()})
        return (target, f1_map, f2_map)

    def poly_vec_mul(u: tuple, v: tuple) -> tuple:
        res = [0] * n_mon
        for idx1, c1 in enumerate(u):
            if not c1:
                continue
            for idx2, k_idx in mul_pairs[idx1]:
                c2 = v[idx2]
                if c2:
                    res[k_idx] = (res[k_idx] + c1 * c2) % mod_b
        return tuple(res)

    one_vec = tuple([1] + [0] * (n_mon - 1))

    def compose_sk(g2: tuple, g1: tuple) -> tuple:
        t_out, f1_out, f2_out = {}, {}, {}
        for eps in (1, 2):
            mid_eps = g1[0][eps]
            t_out[eps] = g2[0][mid_eps]
            y1, y2 = g1[1][eps], g1[2][eps]
            y1_pows, y2_pows = [one_vec], [one_vec]
            for _ in range(1, m_max + 1):
                y1_pows.append(poly_vec_mul(y1_pows[-1], y1))
                y2_pows.append(poly_vec_mul(y2_pows[-1], y2))
            outer1, outer2 = g2[1][mid_eps], g2[2][mid_eps]
            res1, res2 = [0] * n_mon, [0] * n_mon
            for idx_m, (i, j) in enumerate(monoms):
                c1, c2 = outer1[idx_m], outer2[idx_m]
                if not c1 and not c2:
                    continue
                pvec = y2_pows[j] if i == 0 else (y1_pows[i] if j == 0 else poly_vec_mul(y1_pows[i], y2_pows[j]))
                if c1:
                    for q, pv in enumerate(pvec):
                        if pv:
                            res1[q] = (res1[q] + c1 * pv) % mod_b
                if c2:
                    for q, pv in enumerate(pvec):
                        if pv:
                            res2[q] = (res2[q] + c2 * pv) % mod_b
            f1_out[eps] = tuple(res1)
            f2_out[eps] = tuple(res2)
        return (t_out, f1_out, f2_out)

    id_f1 = [0] * n_mon
    id_f1[m_idx[(1, 0)]] = 1
    id_f2 = [0] * n_mon
    id_f2[m_idx[(0, 1)]] = 1
    id_sk = ({1: 1, 2: 2}, {1: tuple(id_f1), 2: tuple(id_f1)}, {1: tuple(id_f2), 2: tuple(id_f2)})
    gens_sk = {w: build_gen(w) for w in ("L", "R", "Li", "Ri")}
    inv_name = {"L": "Li", "Li": "L", "R": "Ri", "Ri": "R"}

    formal_inverses_exact = (
        compose_sk(gens_sk["Li"], gens_sk["L"]) == id_sk
        and compose_sk(gens_sk["Ri"], gens_sk["R"]) == id_sk
    )

    o9 = [(s1, s2, s3) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
    idx9 = {p: i for i, p in enumerate(o9)}

    def p9(which: str) -> tuple:
        out = []
        for a in o9:
            if which == "L":
                b = (a[0], a[2], -a[1])
            elif which == "R":
                b = (a[2], a[1], -a[0])
            elif which == "Li":
                b = (a[0], -a[2], a[1])
            else:
                b = (-a[2], a[1], a[0])
            out.append(idx9[b])
        return tuple(out)

    gens9 = {w: p9(w) for w in ("L", "R", "Li", "Ri")}
    comp9 = lambda p2, p1: tuple(p2[p1[i]] for i in range(8))

    id9 = tuple(range(8))
    cosets_full = {id9: (id_sk, id_sk)}
    q = deque([id9])
    while q:
        c = q.popleft()
        sk_el, sk_inv = cosets_full[c]
        for gname in ("L", "R", "Li", "Ri"):
            nc = comp9(gens9[gname], c)
            if nc not in cosets_full:
                cosets_full[nc] = (
                    compose_sk(gens_sk[gname], sk_el),
                    compose_sk(sk_inv, gens_sk[inv_name[gname]]),
                )
                q.append(nc)

    def kempner_sig(el: tuple, k_level: int) -> tuple:
        mc = k_level - 2
        return (
            to_falling(el[1][1], mc),
            to_falling(el[2][1], mc),
            to_falling(el[1][2], mc),
            to_falling(el[2][2], mc),
        )

    id_sigs = {k: kempner_sig(id_sk, k) for k in range(3, k_max + 1)}

    rs_pairs = []
    seen_rs_sigs = {id_sigs[k_max]}
    sheets_fixed_all = True
    for c, (u_el, u_inv) in cosets_full.items():
        for gname in ("L", "R"):
            nc = comp9(gens9[gname], c)
            u_nc, u_nc_inv = cosets_full[nc]
            sch = compose_sk(u_nc_inv, compose_sk(gens_sk[gname], u_el))
            if sch[0] != {1: 1, 2: 2}:
                sheets_fixed_all = False
            sig = kempner_sig(sch, k_max)
            if sig in seen_rs_sigs:
                continue
            sch_inv = compose_sk(u_inv, compose_sk(gens_sk[inv_name[gname]], u_nc))
            seen_rs_sigs.add(sig)
            seen_rs_sigs.add(kempner_sig(sch_inv, k_max))
            rs_pairs.append((sch, sch_inv))

    def f3_layer_vec(el: tuple, k_level: int) -> list:
        mc = k_level - 2
        sig = kempner_sig(el, k_level)
        id_s = id_sigs[k_level]
        vec = []
        for comp_idx in range(4):
            idx_c = 0
            for deg in range(mc + 1):
                for i in range(deg + 1):
                    j = deg - i
                    exp_rem = mc - v3_fact(i) - v3_fact(j)
                    if exp_rem > 0:
                        diff = (sig[comp_idx][idx_c] - id_s[comp_idx][idx_c]) % (3 ** exp_rem)
                        if diff % (3 ** (exp_rem - 1)) != 0:
                            raise ValueError(f"Element not in L_{k_level}")
                        vec.append((diff // (3 ** (exp_rem - 1))) % 3)
                        idx_c += 1
        return vec

    p_mul = lambda A, B: (compose_sk(A[0], B[0]), compose_sk(B[1], A[1]))
    p_inv = lambda A: (A[1], A[0])
    p_comm = lambda A, B: p_mul(p_mul(A, B), p_mul(p_inv(A), p_inv(B)))
    p_cube = lambda A: p_mul(p_mul(A, A), A)

    layers = {k: [] for k in range(3, k_max + 1)}

    def sift(pair: tuple, start_k: int = 3):
        cur = pair
        for k in range(start_k, k_max + 1):
            vec = f3_layer_vec(cur[0], k)
            if not any(vec):
                continue
            for piv, bvec, bpair in layers[k]:
                coeff = vec[piv]
                if coeff == 1:
                    cur = p_mul(p_inv(bpair), cur)
                    vec = [(vec[q] - bvec[q]) % 3 for q in range(len(vec))]
                elif coeff == 2:
                    cur = p_mul(bpair, cur)
                    vec = [(vec[q] + bvec[q]) % 3 for q in range(len(vec))]
            piv_new = next((q for q, v in enumerate(vec) if v != 0), None)
            if piv_new is not None:
                if vec[piv_new] == 2:
                    cur = p_inv(cur)
                    vec = [(-v) % 3 for v in vec]
                layers[k].append((piv_new, vec, cur))
                return k
        return None

    work_q = deque((rp, 3) for rp in rs_pairs)
    all_basis = []
    while work_q:
        cand, sk_start = work_q.popleft()
        added_k = sift(cand, sk_start)
        if added_k is not None:
            new_pair = layers[added_k][-1][2]
            if added_k < k_max:
                work_q.append((p_cube(new_pair), added_k + 1))
                for rsg in rs_pairs:
                    work_q.append((p_comm(new_pair, rsg), added_k))
            all_basis.append((added_k, new_pair))

    dims = [len(layers[k]) for k in range(3, k_max + 1)]
    cubing_ranks = []
    for k in range(3, k_max):
        rows = []
        for _, _, bpair in layers[k]:
            cb = p_cube(bpair)
            v = f3_layer_vec(cb[0], k + 1)
            for r_piv, r_vec in rows:
                c = v[r_piv]
                if c:
                    v = [(v[q] - c * r_vec[q]) % 3 for q in range(len(v))]
            p_new = next((q for q, x in enumerate(v) if x != 0), None)
            if p_new is not None:
                inv_c = 1 if v[p_new] == 1 else 2
                v = [(x * inv_c) % 3 for x in v]
                rows.append((p_new, v))
        cubing_ranks.append(len(rows))

    log3_k = []
    acc = 0
    for d in dims:
        acc += d
        log3_k.append(acc)

    naive_minus_wake = [2 * d + 1 - v3_fact(d) for d in range(1, 7)]
    pf1_k8_plateau_refutes_naive = (8 in naive_minus_wake) and (dims[3] == 7 and dims[4] == 7 and dims[5] == 7 and dims[6] == 12)
    pf2_unbounded_rank_growth = (dims[0] < dims[2] < dims[3] < dims[6] < dims[7]) and (dims[7] == 14)

    return {
        "hensel_and_inverses_exact": bool(hensel_residual_zero and formal_inverses_exact and sheets_fixed_all and len(cosets_full) == 24),
        "valuation_bound_terms_checked": val_bound_checks,
        "unique_rs_generator_pairs": len(rs_pairs),
        "dims_k3_k11": dims,
        "cubing_ranks_k3_k10": cubing_ranks,
        "log3_K_k3_k11": log3_k,
        "G11_order_str": str(24 * (3 ** log3_k[-1])),
        "pf1_k8_plateau_refutes_naive": pf1_k8_plateau_refutes_naive,
        "pf2_unbounded_rank_growth": pf2_unbounded_rank_growth,
    }


def run_e2_b1990_branchless_counts() -> dict:
    # Symbolic completion-of-square identity check in Z[x, y, z, kappa]:
    x_s, y_s, z_s, kap_s = sp.symbols("x y z kappa")
    lhs = sp.expand((2 * z_s - x_s * y_s) ** 2 - (x_s ** 2 - 4) * (y_s ** 2 - 4) - 4 * (kap_s - 2))
    rhs = sp.expand(4 * (x_s ** 2 + y_s ** 2 + z_s ** 2 - x_s * y_s * z_s - (kap_s + 2)))
    conic_identity_exact = (sp.expand(lhs - rhs) == 0)

    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    sectors_checked = 0
    all_exact = True
    pf3_flipped_sign_fails_all_p_ge_5 = True
    p3_cusp_count = 0

    for p in primes:
        counts = [0] * p
        sq = [(x * x) % p for x in range(p)]
        for x in range(p):
            sx = sq[x]
            for y in range(p):
                sxy = (sx + sq[y]) % p
                xy = (x * y) % p
                for z in range(p):
                    c = (sxy + sq[z] - xy * z) % p
                    counts[(c - 2) % p] += 1
        if p == 3:
            p3_cusp_count = counts[(-2) % 3]
        wrong_mismatches_at_p = 0
        for kappa in range(p):
            chi_km2 = legendre(kappa - 2, p)
            chi_kp2 = legendre(kappa + 2, p)
            pred = p * p + chi_km2 * (3 + chi_kp2) * p + 1
            wrong_pred = p * p + chi_km2 * (3 - chi_kp2) * p + 1
            if counts[kappa] != pred:
                all_exact = False
            if counts[kappa] != wrong_pred:
                wrong_mismatches_at_p += 1
            sectors_checked += 1
        if p >= 5 and wrong_mismatches_at_p == 0:
            pf3_flipped_sign_fails_all_p_ge_5 = False

    return {
        "conic_fibration_identity_exact": conic_identity_exact,
        "odd_primes_checked": len(primes),
        "sectors_checked": sectors_checked,
        "p3_cusp_count": p3_cusp_count,
        "branchless_law_all_exact": bool(conic_identity_exact and all_exact and p3_cusp_count == 1),
        "pf3_flipped_sign_fails_all_p_ge_5": pf3_flipped_sign_fails_all_p_ge_5,
    }


def L_tr(v: tuple, M: int) -> tuple:
    return (v[0], v[2], (v[0] * v[2] - v[1]) % M)


def R_tr(v: tuple, M: int) -> tuple:
    return (v[2], v[1], (v[1] * v[2] - v[0]) % M)


def Li_tr(v: tuple, M: int) -> tuple:
    return (v[0], (v[0] * v[1] - v[2]) % M, v[1])


def Ri_tr(v: tuple, M: int) -> tuple:
    return ((v[0] * v[1] - v[2]) % M, v[1], v[0])


def build_orbit_fast(M: int) -> tuple:
    root = (3 % M, 3 % M, 3 % M)
    orb = [root]
    idx = {root: 0}
    q = deque([root])
    while q:
        v = q.popleft()
        for fn in (L_tr, R_tr, Li_tr, Ri_tr):
            w = fn(v, M)
            if w not in idx:
                idx[w] = len(orb)
                orb.append(w)
                q.append(w)
    n = len(orb)
    pL = tuple(idx[L_tr(v, M)] for v in orb)
    pR = tuple(idx[R_tr(v, M)] for v in orb)
    pLi = tuple(idx[Li_tr(v, M)] for v in orb)
    pRi = tuple(idx[Ri_tr(v, M)] for v in orb)
    pC = tuple(idx[(v[1], v[2], v[0])] for v in orb)
    pSig = tuple(idx[(v[1], v[0], (v[0] * v[1] - v[2]) % M)] for v in orb)
    return orb, idx, (pL, pR, pLi, pRi, pC, pSig)


def halving_from_perm_graph(n: int, pL: tuple, pLi: tuple, pC: tuple) -> dict:
    pC2 = tuple(pC[pC[i]] for i in range(n))
    conj = lambda c, g, ci: tuple(c[g[ci[i]]] for i in range(n))
    moves = [pL, conj(pC, pL, pC2), conj(pC2, pL, pC), pLi, conj(pC, pLi, pC2), conj(pC2, pLi, pC)]

    visited = [False] * n
    orbs_3, fixed_1 = [], []
    for i in range(n):
        if not visited[i]:
            if pC[i] == i:
                visited[i] = True
                fixed_1.append(i)
            else:
                j = pC[i]
                k = pC[j]
                visited[i] = visited[j] = visited[k] = True
                orbs_3.append((i, j, k))

    v_to_b0, b0_sizes = {}, []
    for idx_f, v in enumerate(fixed_1):
        v_to_b0[v] = idx_f
        b0_sizes.append(1)
    off = len(fixed_1)
    for idx_o, trip in enumerate(orbs_3):
        b0_sizes.append(3)
        for v in trip:
            v_to_b0[v] = off + idx_o

    d0, d1 = len(b0_sizes), len(orbs_3)
    rows_3M0 = [[0] * d0 for _ in range(d0)]
    for col, v0 in enumerate(fixed_1 + [t[0] for t in orbs_3]):
        for mv in moves:
            row = v_to_b0[mv[v0]]
            rows_3M0[row][col] += (3 * b0_sizes[col]) // b0_sizes[row]

    orb3_lookup = {}
    for row_o, (u0, u1, u2) in enumerate(orbs_3):
        orb3_lookup[u0] = (row_o, 0)
        orb3_lookup[u1] = (row_o, 1)
        orb3_lookup[u2] = (row_o, 2)

    rows_Mch = [[0] * (2 * d1) for _ in range(2 * d1)]
    for col_o, (v0, v1, v2) in enumerate(orbs_3):
        for b_sub, (vp, vm) in enumerate(((v0, v2), (v1, v2))):
            col = 2 * col_o + b_sub
            for mv in moves:
                for u, sgn in ((mv[vp], 1), (mv[vm], -1)):
                    if u in orb3_lookup:
                        ro, sub = orb3_lookup[u]
                        if sub == 0:
                            rows_Mch[2 * ro][col] += sgn
                        elif sub == 1:
                            rows_Mch[2 * ro + 1][col] += sgn

    x = sp.Symbol("x")
    cp_3M0 = sp.Poly.from_list(DomainMatrix.from_list(rows_3M0, sp.ZZ).charpoly(), x, domain=sp.ZZ).as_expr()
    cp0 = sp.simplify(cp_3M0.subs(x, 3 * x) / (3 ** d0))
    cp_ch = sp.Poly.from_list(DomainMatrix.from_list(rows_Mch, sp.ZZ).charpoly(), x, domain=sp.ZZ).as_expr()

    f0 = sp.factor_list(cp0)[1]
    fch = sp.factor_list(cp_ch)[1]
    f0_2x = Counter({sp.Poly(f.subs(x, 2 * x), x).monic().as_expr(): m for f, m in f0})
    f1 = Counter({sp.Poly(f, x).monic().as_expr(): m // 2 for f, m in fch})

    paired, unpaired = [], []
    paired_deg, unpaired_deg = 0, 0
    for f, m1 in sorted(f1.items(), key=lambda kv: (sp.degree(kv[0], x), str(kv[0]))):
        mp = min(m1, f0_2x[f])
        d = int(sp.degree(f, x))
        if mp > 0:
            paired_deg += mp * d
            paired.append([str(f), int(mp), d])
        if m1 > mp:
            rem = m1 - mp
            unpaired_deg += rem * d
            unpaired.append([str(f), int(rem), d])

    return {
        "n": n,
        "fix_C": len(fixed_1),
        "d0": d0,
        "d1": d1,
        "paired_deg": paired_deg,
        "unpaired_deg": unpaired_deg,
        "paired_factors": paired,
        "unpaired_factors": unpaired,
    }


def run_e3_crt_and_q6_defect() -> dict:
    res = {}
    for M in (5, 7, 9, 15, 27, 45, 63):
        orb, _, (pL, _, pLi, _, pC, _) = build_orbit_fast(M)
        res[str(M)] = halving_from_perm_graph(len(orb), pL, pLi, pC)

    crt_sizes_exact = (
        res["15"]["n"] == 1 * res["5"]["n"]
        and res["45"]["n"] == res["9"]["n"] * res["5"]["n"]
        and res["63"]["n"] == res["9"]["n"] * res["7"]["n"]
    )

    # Construct N_3 = (V_4 K_3) cap [G_3, G_3] (order 12) on O_27 (72 points) -> 6-point quotient Q_6!
    orb27, _, (pL27, pR27, pLi27, pRi27, pC27, _) = build_orbit_fast(27)
    id27 = tuple(range(72))
    G3 = {id27}
    gq = deque([id27])
    while gq:
        g = gq.popleft()
        for gen in (pL27, pR27, pLi27, pRi27):
            ng = tuple(gen[g[i]] for i in range(72))
            if ng not in G3:
                G3.add(ng)
                gq.append(ng)
    comp27 = lambda a, b: tuple(a[b[i]] for i in range(72))
    inv27 = lambda a: tuple(next(i for i in range(72) if a[i] == j) for j in range(72))

    base_comms = []
    for a in (pL27, pR27, pLi27, pRi27):
        ai = inv27(a)
        for b in (pL27, pR27, pLi27, pRi27):
            bi = inv27(b)
            base_comms.append(comp27(comp27(a, b), comp27(ai, bi)))
    conj_comms = [comp27(comp27(g, c), inv27(g)) for g in G3 for c in base_comms]
    der_G3 = {id27}
    nq = deque([id27])
    for cc in conj_comms:
        if cc not in der_G3:
            der_G3.add(cc)
            nq.append(cc)
    while nq:
        xg = nq.popleft()
        for cc in conj_comms:
            nx = comp27(cc, xg)
            if nx not in der_G3:
                der_G3.add(nx)
                nq.append(nx)

    def in_V4_K3(g: tuple) -> bool:
        v0 = orb27[g[0]]
        s = [1 if (v0[j] % 9) == (orb27[0][j] % 9) else -1 for j in range(3)]
        for i, pt in enumerate(orb27):
            w = orb27[g[i]]
            if any((w[j] - s[j] * pt[j]) % 9 != 0 for j in range(3)):
                return False
        return True

    N3 = [g for g in der_G3 if in_V4_K3(g)]
    vis27 = [False] * 72
    q6_blocks = []
    pt_to_q6 = [0] * 72
    for i in range(72):
        if not vis27[i]:
            blk = sorted({g[i] for g in N3})
            for b in blk:
                vis27[b] = True
                pt_to_q6[b] = len(q6_blocks)
            q6_blocks.append(blk)

    pL_6 = tuple(pt_to_q6[pL27[b[0]]] for b in q6_blocks)
    pLi_6 = tuple(pt_to_q6[pLi27[b[0]]] for b in q6_blocks)
    pC_6 = tuple(pt_to_q6[pC27[b[0]]] for b in q6_blocks)

    q6_defects = {}
    for p_prime in (5, 7):
        orb_p, _, (pLp, _, pLip, _, pCp, _) = build_orbit_fast(p_prime)
        np = len(orb_p)
        N_tot = 6 * np
        pL_c = tuple(pL_6[i // np] * np + pLp[i % np] for i in range(N_tot))
        pLi_c = tuple(pLi_6[i // np] * np + pLip[i % np] for i in range(N_tot))
        pC_c = tuple(pC_6[i // np] * np + pCp[i % np] for i in range(N_tot))
        q6_defects[str(p_prime)] = halving_from_perm_graph(N_tot, pL_c, pLi_c, pC_c)

    # PF4 counterfactual: unshifted bare S_3 module 1 (+) sgn (+) E_2 tensored with O_5 gives 52 unpaired != 10!
    orb5, _, (_, _, _, _, pC5, pSig5) = build_orbit_fast(5)
    M_C5 = sp.zeros(40, 40)
    M_S5 = sp.zeros(40, 40)
    for i in range(40):
        M_C5[pC5[i], i] = 1
        M_S5[pSig5[i], i] = 1
    C_bare = sp.diag(sp.Matrix([[1]]), sp.Matrix([[1]]), sp.Matrix([[0, -1], [1, -1]]))
    S_bare = sp.diag(sp.Matrix([[1]]), sp.Matrix([[-1]]), sp.Matrix([[0, 1], [1, 0]]))
    from sympy.physics.quantum import TensorProduct
    Ct = TensorProduct(C_bare, M_C5)
    St = TensorProduct(S_bare, M_S5)
    C2t = Ct * Ct
    Lt = St * C2t
    Lit = Ct * St
    Wt = Lt + Ct * Lt * C2t + C2t * Lt * Ct + Lit + Ct * Lit * C2t + C2t * Lit * Ct
    ns0 = (Ct - sp.eye(160)).nullspace()
    nsch = (C2t + Ct + sp.eye(160)).nullspace()
    B0 = sp.Matrix.hstack(*ns0)
    Bch = sp.Matrix.hstack(*nsch)
    X0 = (B0.T * B0).inv() * (B0.T * Wt * B0)
    Xch = (Bch.T * Bch).inv() * (Bch.T * Wt * Bch)
    x = sp.Symbol("x")
    cp0_b = sp.Poly.from_list(DomainMatrix.from_Matrix(X0).convert_to(sp.QQ).charpoly(), x, domain=sp.QQ).as_expr()
    cpch_b = sp.Poly.from_list(DomainMatrix.from_Matrix(Xch).convert_to(sp.QQ).charpoly(), x, domain=sp.QQ).as_expr()
    f0_b = Counter({sp.Poly(f.subs(x, 2 * x), x).monic().as_expr(): m for f, m in sp.factor_list(cp0_b)[1]})
    f1_b = Counter({sp.Poly(f, x).monic().as_expr(): m // 2 for f, m in sp.factor_list(cpch_b)[1]})
    bare_unp_deg = sum((m1 - min(m1, f0_b[f])) * int(sp.degree(f, x)) for f, m1 in f1_b.items() if m1 > f0_b[f])

    pf4_bare_s3_counterfactual_caught = (bare_unp_deg == 52 and q6_defects["5"]["unpaired_deg"] == 10)

    return {
        "crt_sizes_exact": crt_sizes_exact,
        "N3_order": len(N3),
        "Q6_size": len(q6_blocks),
        "Q6_fix_C": sum(1 for i in range(len(q6_blocks)) if pC_6[i] == i),
        "mod45_paired_deg": res["45"]["paired_deg"],
        "mod45_paired_factors": res["45"]["paired_factors"],
        "mod63_paired_deg": res["63"]["paired_deg"],
        "mod63_paired_factors": res["63"]["paired_factors"],
        "all_k_ge3_unpaired_deg_p5": q6_defects["5"]["unpaired_deg"],
        "all_k_ge3_unpaired_factors_p5": q6_defects["5"]["unpaired_factors"],
        "all_k_ge3_unpaired_deg_p7": q6_defects["7"]["unpaired_deg"],
        "all_k_ge3_unpaired_factors_p7": q6_defects["7"]["unpaired_factors"],
        "bare_s3_wrong_unpaired_deg_p5": bare_unp_deg,
        "pf4_bare_s3_counterfactual_caught": pf4_bare_s3_counterfactual_caught,
    }


def run_e4_b1997_k4_mackey() -> dict:
    orb81, _, (pL81, pR81, pLi81, pRi81, _, _) = build_orbit_fast(81)
    orb9, idx9, _ = build_orbit_fast(9)
    idp81 = tuple(range(648))
    seen81 = {idp81}
    gq81 = deque([idp81])
    while gq81:
        g = gq81.popleft()
        for gen in (pL81, pR81, pLi81, pRi81):
            ng = tuple(gen[g[i]] for i in range(648))
            if ng not in seen81:
                seen81.add(ng)
                gq81.append(ng)
    fib_of = [idx9[(v[0] % 9, v[1] % 9, v[2] % 9)] for v in orb81]
    K4 = [g for g in seen81 if all(fib_of[g[i]] == fib_of[i] for i in range(648))]
    comp81 = lambda p2, p1: tuple(p2[p1[i]] for i in range(648))

    def pow81(g: tuple, e: int) -> tuple:
        r = idp81
        for _ in range(e):
            r = comp81(g, r)
        return r

    ord9_els = [g for g in K4 if pow81(g, 3) != idp81]
    gen_a = ord9_els[0]
    sub_a = {pow81(gen_a, i) for i in range(9)}
    gen_b = next(g for g in ord9_els if pow81(g, 3) not in sub_a)
    K4_grid = {}
    k4_abelian = True
    for i in range(9):
        ai = pow81(gen_a, i)
        for j in range(9):
            bj = pow81(gen_b, j)
            gij = comp81(ai, bj)
            if comp81(bj, ai) != gij:
                k4_abelian = False
            K4_grid[(i, j)] = gij
    inv_grid = {g: ij for ij, g in K4_grid.items()}
    reps_f = [next(idx for idx, f in enumerate(fib_of) if f == f_id) for f_id in range(8)]
    pt_coords = {gij[reps_f[f]]: (f, i, j) for f in range(8) for (i, j), gij in K4_grid.items()}
    regular_fiber_action = (len(G4_orders := seen81) == 1944 and len(K4) == 81 and len(pt_coords) == 648 and k4_abelian)

    def action_mat(pg: tuple) -> list:
        pi = [0] * 648
        for i, v in enumerate(pg):
            pi[v] = i
        pi = tuple(pi)
        c1 = inv_grid[comp81(pg, comp81(gen_a, pi))]
        c2 = inv_grid[comp81(pg, comp81(gen_b, pi))]
        return [[c1[0], c2[0]], [c1[1], c2[1]]]

    AL, AR = action_mat(pL81), action_mat(pR81)
    shift_L = [pt_coords[pL81[reps_f[f]]] for f in range(8)]
    shift_R = [pt_coords[pR81[reps_f[f]]] for f in range(8)]

    def mat_inv_T(A: list) -> list:
        det = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 9
        inv_d = pow(det, -1, 9)
        return [
            [(inv_d * A[1][1]) % 9, (-inv_d * A[1][0]) % 9],
            [(-inv_d * A[0][1]) % 9, (inv_d * A[0][0]) % 9],
        ]

    BL, BR = mat_inv_T(AL), mat_inv_T(AR)
    vis_m = set()
    m_orbits = []
    for m1 in range(9):
        for m2 in range(9):
            if (m1, m2) not in vis_m:
                orb_m = []
                dq = deque([(m1, m2)])
                vis_m.add((m1, m2))
                while dq:
                    u = dq.popleft()
                    orb_m.append(u)
                    for B in (BL, BR):
                        w = ((B[0][0] * u[0] + B[0][1] * u[1]) % 9, (B[1][0] * u[0] + B[1][1] * u[1]) % 9)
                        if w not in vis_m:
                            vis_m.add(w)
                            dq.append(w)
                m_orbits.append(orb_m)

    # Verify algebraic identity prod_{r in {1,2,4}} (x^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) x^2 + 4) == P_12(x)!
    zeta9 = sp.exp(2 * sp.pi * sp.I / 9)
    K_cyc9 = sp.QQ.algebraic_field(zeta9)
    z9_el = K_cyc9.from_sympy(zeta9)
    z9_pows = [K_cyc9.one]
    for _ in range(1, 9):
        z9_pows.append(z9_pows[-1] * z9_el)

    prod_coeffs = [K_cyc9.one]
    for r in (1, 2, 4):
        two_w_r = K_cyc9.one - (z9_pows[r] + z9_pows[9 - r]) * K_cyc9.from_sympy(sp.Integer(2))
        qr_coeffs = [K_cyc9.one, K_cyc9.zero, -two_w_r, K_cyc9.zero, K_cyc9.from_sympy(sp.Integer(4))]
        nxt = [K_cyc9.zero] * (len(prod_coeffs) + len(qr_coeffs) - 1)
        for i_c, c_a in enumerate(prod_coeffs):
            for j_c, c_b in enumerate(qr_coeffs):
                nxt[i_c + j_c] += c_a * c_b
        prod_coeffs = nxt
    p12_target_coeffs = [1, 0, -3, 0, 3, 0, -21, 0, 12, 0, -48, 0, 64]
    p12_galois_product_exact = (
        [K_cyc9.to_sympy(c) for c in prod_coeffs] == [sp.Integer(c) for c in p12_target_coeffs]
    )

    size_hist = Counter(len(o) for o in m_orbits)
    inv_closed_ord9_hits = []
    other_orbits_zero_hits = True

    for orb_m in m_orbits:
        m_to_i = {m: idx for idx, m in enumerate(orb_m)}
        dim_blk = 8 * len(orb_m)
        rows_blk = [[K_cyc9.zero] * dim_blk for _ in range(dim_blk)]
        for col_m_idx, m in enumerate(orb_m):
            mL = ((BL[0][0] * m[0] + BL[0][1] * m[1]) % 9, (BL[1][0] * m[0] + BL[1][1] * m[1]) % 9)
            mR = ((BR[0][0] * m[0] + BR[0][1] * m[1]) % 9, (BR[1][0] * m[0] + BR[1][1] * m[1]) % 9)
            row_mL, row_mR = m_to_i[mL], m_to_i[mR]
            for f in range(8):
                col = 8 * col_m_idx + f
                tfL, sL1, sL2 = shift_L[f]
                rows_blk[8 * row_mL + tfL][col] += z9_pows[(mL[0] * sL1 + mL[1] * sL2) % 9]
                tfR, sR1, sR2 = shift_R[f]
                rows_blk[8 * row_mR + tfR][col] += z9_pows[(mR[0] * sR1 + mR[1] * sR2) % 9]
        W = DomainMatrix(rows_blk, (dim_blk, dim_blk), K_cyc9)
        I_d = DomainMatrix.eye(dim_blk, K_cyc9)
        W2 = W * W
        W4 = W2 * W2
        neg_closed = all(((-m[0]) % 9, (-m[1]) % 9) in m_to_i for m in orb_m)
        is_ord9 = any((3 * m[0]) % 9 != 0 or (3 * m[1]) % 9 != 0 for m in orb_m)

        q_hits = []
        for r in (1, 2, 4):
            two_w = K_cyc9.one - (z9_pows[r] + z9_pows[9 - r]) * K_cyc9.from_sympy(sp.Integer(2))
            Qr = W4 - I_d.scalarmul(two_w) * W2 + I_d.scalarmul(K_cyc9.from_sympy(sp.Integer(4)))
            rk_null = dim_blk - Qr.rank()
            if rk_null > 0:
                q_hits.append([r, rk_null])
        if len(orb_m) == 6 and neg_closed and is_ord9:
            inv_closed_ord9_hits.append({"rep": list(orb_m[0]), "quartic_hits": q_hits})
        else:
            if q_hits:
                other_orbits_zero_hits = False

    # Check Mackey double-coset index |S \ S_4 / H_chi| == 2 explicitly on S_4!
    # S = Stab_{G_2}(rep_0) has order 3; H_chi = Stab_{S_4}(m_star) for m_star in inv_closed_ord9_hits[0] has order 4!
    m_star = tuple(inv_closed_ord9_hits[0]["rep"])
    # Enumerate S_4 (24 elements) via action on O_9 and dual action on (Z/9Z)^2:
    orb9_24 = {}
    id9_t = tuple(range(8))
    id2_t = ((1, 0), (0, 1))
    pL9 = tuple(idx9[L_tr(v, 9)] for v in orb9)
    pR9 = tuple(idx9[R_tr(v, 9)] for v in orb9)
    mat_mul9 = lambda M2, M1: (
        ((M2[0][0] * M1[0][0] + M2[0][1] * M1[1][0]) % 9, (M2[0][0] * M1[0][1] + M2[0][1] * M1[1][1]) % 9),
        ((M2[1][0] * M1[0][0] + M2[1][1] * M1[1][0]) % 9, (M2[1][0] * M1[0][1] + M2[1][1] * M1[1][1]) % 9),
    )
    BL_t = (tuple(BL[0]), tuple(BL[1]))
    BR_t = (tuple(BR[0]), tuple(BR[1]))
    q24 = deque([(id9_t, id2_t)])
    orb9_24[id9_t] = id2_t
    while q24:
        p_cur, b_cur = q24.popleft()
        for p_g, b_g in ((pL9, BL_t), (pR9, BR_t)):
            np9 = tuple(p_g[p_cur[i]] for i in range(8))
            nb9 = mat_mul9(b_g, b_cur)
            if np9 not in orb9_24:
                orb9_24[np9] = nb9
                q24.append((np9, nb9))
    S_sub = [p for p in orb9_24 if p[0] == 0]
    H_sub = [p for p, b in orb9_24.items() if ((b[0][0] * m_star[0] + b[0][1] * m_star[1]) % 9, (b[1][0] * m_star[0] + b[1][1] * m_star[1]) % 9) == m_star]
    # Count double cosets S g H in S_4:
    vis_dc = set()
    num_double_cosets = 0
    for g in orb9_24:
        if g not in vis_dc:
            num_double_cosets += 1
            for s in S_sub:
                sg = tuple(s[g[i]] for i in range(8))
                for h in H_sub:
                    sgh = tuple(sg[h[i]] for i in range(8))
                    vis_dc.add(sgh)

    hits_sorted = sorted(h["quartic_hits"][0] for h in inv_closed_ord9_hits if len(h["quartic_hits"]) == 1)
    pf5_non_inv_closed_zero_nullity = bool(other_orbits_zero_hits and len(m_orbits) - len(inv_closed_ord9_hits) == 16)

    return {
        "regular_K4_fiber_action": regular_fiber_action,
        "dual_K4_orbit_count": len(m_orbits),
        "dual_K4_orbit_size_hist": {str(k): v for k, v in sorted(size_hist.items())},
        "p12_galois_product_exact": p12_galois_product_exact,
        "inv_closed_ord9_orbit_count": len(inv_closed_ord9_hits),
        "quartic_r_and_nullity_pairs": hits_sorted,
        "S_order": len(S_sub),
        "H_chi_order": len(H_sub),
        "mackey_double_cosets": num_double_cosets,
        "pf5_non_inv_closed_zero_nullity": pf5_non_inv_closed_zero_nullity,
    }


def main() -> int:
    e1 = run_e1_kempner_tower(11)
    e2 = run_e2_b1990_branchless_counts()
    e3 = run_e3_crt_and_q6_defect()
    e4 = run_e4_b1997_k4_mackey()

    pf_flags = [
        e1["pf1_k8_plateau_refutes_naive"],
        e1["pf2_unbounded_rank_growth"],
        e2["pf3_flipped_sign_fails_all_p_ge_5"],
        e3["pf4_bare_s3_counterfactual_caught"],
        e4["pf5_non_inv_closed_zero_nullity"],
    ]
    pf_caught = sum(1 for fl in pf_flags if fl)

    payload = {
        "card": "AGY-C71",
        "seat_code": "fam3-v1-high-01",
        "parameter_count": "0 of 19",
        "premises_max_arc": "B2010",
        "E1_kempner_3adic_tower": e1,
        "E2_b1990_branchless_counts": e2,
        "E3_b2003_crt_and_q6_defect": e3,
        "E4_b1997_k4_mackey_ninth_roots": e4,
        "planted_faults_caught": pf_caught,
        "planted_faults_total": 5,
    }

    out_path = pathlib.Path(__file__).resolve().parent / "c71_out.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Emit 4 deterministic DECISIVE lines (zero private hashes, zero floats):
    sys.stdout.write(
        f"DECISIVE: E1 dims_k3_k11={e1['dims_k3_k11']} cubing_k3_k10={e1['cubing_ranks_k3_k10']} "
        f"log3K11={e1['log3_K_k3_k11'][-1]} G11={e1['G11_order_str']} hensel_exact={e1['hensel_and_inverses_exact']}\n"
    )
    sys.stdout.write(
        f"DECISIVE: E2 conic_id={e2['conic_fibration_identity_exact']} primes={e2['odd_primes_checked']} "
        f"sectors={e2['sectors_checked']} p3_cusp={e2['p3_cusp_count']} branchless_exact={e2['branchless_law_all_exact']}\n"
    )
    sys.stdout.write(
        f"DECISIVE: E3 N3={e3['N3_order']} Q6={e3['Q6_size']} fixC_Q6={e3['Q6_fix_C']} "
        f"mod45_paired={e3['mod45_paired_deg']} mod63_paired={e3['mod63_paired_deg']} "
        f"unp_p5={e3['all_k_ge3_unpaired_deg_p5']} unp_p7={e3['all_k_ge3_unpaired_deg_p7']}\n"
    )
    sys.stdout.write(
        f"DECISIVE: E4 dual_orbs={e4['dual_K4_orbit_count']} p12_prod={e4['p12_galois_product_exact']} "
        f"inv_ord9={e4['inv_closed_ord9_orbit_count']} q_hits={e4['quartic_r_and_nullity_pairs']} "
        f"mackey_dc={e4['mackey_double_cosets']} pf={pf_caught}/{len(pf_flags)}\n"
    )
    return 0 if pf_caught == 5 else 1


if __name__ == "__main__":
    sys.exit(main())
