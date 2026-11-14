#!/usr/bin/env python3
"""
Standalone zero-trust verifier for Card X-SM2 (M16 & M17 on docs/seats/agy-exp.md):
  1. Part 1 — SM-C8: The Partner Test on B1441 Tier 1 (74 manifolds, 71 active entries <= 600 chars,
     486,754 non-split rank-2 modules, 1,109,760 joins of which 175,628 are non-vacuous).
     Exact F_p Fox calculus (with second prime cross-check on all |I|=2 modules and sampled entries,
     plus direct 2x2 matrix Fox derivative and contragredient V* = rho^{-T} cross-checks).
  2. Part 2 — SM-C10: Twisted Duality on the Tick Family M_1..M_6 (m000, m004, m025, m206, m407, s961).
     Exact free-group commutator parity, SnapPy cross-checks, sealed population (N in 2..6: 1,204 modules),
     extended m407 population at N = 22 (2,420 distinct-diagonal + 242 unipotent = 2,662 modules),
     transfer K4 to orientation double covers M_{2n}, and 50-digit mpmath common-point SU(2) family
     across all 46 roots of unity of orders dividing 1..12.
  3. Part 3 — SM-C11 (P-333): Standalone two-path F-CI cusp-isometry reader on o10_150729 (m003's
     five-ended companion), control L8a15 (+LLLR's three-ended companion), and the complete census of
     all 232 signed word states of lengths 2..10 (231 proper fixed-point companions).
  4. Eight planted-fault controls (P1_C8..P3_C8, P4_C10..P6_C10, P7_C11..P8_C11), all required to fire.

Zero imports from frontier/, src/, or any seat script. Zero measured physical quantities.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
import sys
import time
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

# Force pure-Python ground types in SymPy so python-flint never interferes with integer normal forms
os.environ["SYMPY_GROUND_TYPES"] = "python"

import mpmath as mp
import numpy as np
import snappy
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

mp.mp.dps = 55


# ============================================================================
# JSON HELPER & NUMBER-THEORY PRIMITIVES
# ============================================================================

def _json_default(obj: Any) -> Any:
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, Fraction):
        return f"{obj.numerator}/{obj.denominator}" if obj.denominator != 1 else str(obj.numerator)
    if isinstance(obj, sp.Integer):
        return int(obj)
    if isinstance(obj, (mp.mpf, mp.mpc)):
        return str(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def is_prime_int(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    d = 3
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True


def find_primes_1_mod_N(N: int, count: int = 2, start: int = 100_003) -> List[int]:
    step = max(N, 2)
    rem = start % step
    cand = start + (1 - rem) % step
    if cand < start:
        cand += step
    out: List[int] = []
    while len(out) < count:
        if is_prime_int(cand):
            out.append(cand)
        cand += step
    return out


def primitive_nth_root_mod_p(N: int, p: int) -> int:
    assert is_prime_int(p) and (p - 1) % max(N, 1) == 0
    if N <= 1:
        return 1
    n_rem = N
    pfacs: List[int] = []
    d = 2
    while d * d <= n_rem:
        if n_rem % d == 0:
            pfacs.append(d)
            while n_rem % d == 0:
                n_rem //= d
        d += 1
    if n_rem > 1:
        pfacs.append(n_rem)
    exp = (p - 1) // N
    for g in range(2, p):
        zeta = pow(g, exp, p)
        if pow(zeta, N, p) == 1 and all(pow(zeta, N // q, p) != 1 for q in pfacs):
            return zeta
    raise RuntimeError(f"No primitive {N}-th root mod {p}")


def lcm_list(vals: Sequence[int]) -> int:
    acc = 1
    for v in vals:
        acc = math.lcm(acc, abs(int(v)))
    return acc


# ============================================================================
# EXACT FINITE-FIELD LINEAR ALGEBRA (PURE INTEGER MOD p, ZERO SVD TOLERANCES)
# ============================================================================

def rref_mod_p(rows: List[List[int]], ncols: int, p: int) -> Tuple[List[List[int]], List[int]]:
    """In-place-safe RREF over F_p for small dense integer matrices; returns (rref_nonzero_rows, pivot_cols)."""
    A = [r[:] for r in rows]
    nrows = len(A)
    piv_cols: List[int] = []
    r_piv = 0
    for c in range(ncols):
        if r_piv >= nrows:
            break
        piv = -1
        for r in range(r_piv, nrows):
            if A[r][c] % p != 0:
                piv = r
                break
        if piv == -1:
            continue
        if piv != r_piv:
            A[r_piv], A[piv] = A[piv], A[r_piv]
        val = A[r_piv][c] % p
        if val != 1:
            inv_v = pow(val, p - 2, p)
            row_p = A[r_piv]
            for j in range(c, ncols):
                row_p[j] = (row_p[j] * inv_v) % p
        else:
            A[r_piv][c] = 1
        row_p = A[r_piv]
        for r in range(nrows):
            if r != r_piv:
                f = A[r][c] % p
                if f != 0:
                    row_r = A[r]
                    row_r[c] = 0
                    for j in range(c + 1, ncols):
                        if row_p[j]:
                            row_r[j] = (row_r[j] - f * row_p[j]) % p
        piv_cols.append(c)
        r_piv += 1
    return A[:r_piv], piv_cols


def rank_mod_p(rows: List[List[int]], ncols: int, p: int) -> int:
    """Fast exact Gaussian elimination rank over F_p."""
    if not rows or ncols == 0:
        return 0
    A = [r[:] for r in rows]
    nrows = len(A)
    r_piv = 0
    for c in range(ncols):
        if r_piv >= nrows:
            break
        piv = -1
        for r in range(r_piv, nrows):
            if A[r][c] % p != 0:
                piv = r
                break
        if piv == -1:
            continue
        if piv != r_piv:
            A[r_piv], A[piv] = A[piv], A[r_piv]
        inv_v = pow(A[r_piv][c] % p, p - 2, p)
        row_p = A[r_piv]
        for r in range(r_piv + 1, nrows):
            f = A[r][c] % p
            if f != 0:
                mul = (f * inv_v) % p
                row_r = A[r]
                row_r[c] = 0
                for j in range(c + 1, ncols):
                    if row_p[j]:
                        row_r[j] = (row_r[j] - mul * row_p[j]) % p
        r_piv += 1
    return r_piv


def nullspace_mod_p(rows: List[List[int]], ncols: int, p: int) -> List[List[int]]:
    """Deterministic basis of ker(A) subset F_p^ncols as list of vectors of length ncols."""
    rref_rows, piv_cols = rref_mod_p(rows, ncols, p)
    piv_set = set(piv_cols)
    free_cols = [c for c in range(ncols) if c not in piv_set]
    basis: List[List[int]] = []
    for fc in free_cols:
        vec = [0] * ncols
        vec[fc] = 1
        for idx, pc in enumerate(piv_cols):
            val = rref_rows[idx][fc] % p
            if val != 0:
                vec[pc] = (p - val) % p
        basis.append(vec)
    return basis


def rank_2col_mod_p(col0: Sequence[int], col1: Sequence[int], p: int) -> int:
    """Exact rank over F_p of an n x 2 matrix given by two column vectors."""
    n = len(col0)
    p0 = -1
    for i in range(n):
        if col0[i] % p != 0:
            p0 = i
            break
    if p0 == -1:
        return 1 if any((x % p) != 0 for x in col1) else 0
    inv0 = pow(col0[p0] % p, p - 2, p)
    scale = (col1[p0] * inv0) % p
    for i in range(n):
        if (col1[i] - scale * col0[i]) % p != 0:
            return 2
    return 1


def smith_nonneg(M: sp.Matrix) -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Smith normal form D = U * M * V over Z with D[i, i] >= 0 guaranteed."""
    D, U, V = smith_normal_decomp(M)
    D = D.copy()
    U = U.copy()
    lim = min(D.rows, D.cols)
    for i in range(lim):
        if int(D[i, i]) < 0:
            D.row_op(i, lambda v, _: -v)
            U.row_op(i, lambda v, _: -v)
    assert U * M * V == D
    return D, U, V


# ============================================================================
# PARSING SNAPPY PRESENTATIONS & EXACT ABELIAN CHARACTER ENUMERATION
# ============================================================================

def parse_snappy_word(word_str: str, gen_to_idx: Dict[str, int]) -> List[int]:
    """
    Parse SnapPy fundamental_group word into signed 1-based generator tokens:
      'a' -> +1, 'A' -> -1, etc.
    Handles both single-letter ('aBc') and any multi-char generator tokens if present.
    """
    if not word_str:
        return []
    out: List[int] = []
    for ch in word_str:
        low = ch.lower()
        assert low in gen_to_idx, f"Unknown generator char {ch!r} in {word_str!r}"
        idx1 = gen_to_idx[low] + 1
        out.append(idx1 if ch.islower() else -idx1)
    return out


def extract_presentation_data(M: "snappy.Manifold") -> Dict[str, Any]:
    G = M.fundamental_group()
    gens = list(G.generators())
    assert all(len(g) == 1 and g.islower() for g in gens), f"Unexpected generator format: {gens}"
    gen_to_idx = {g: i for i, g in enumerate(gens)}
    m = len(gens)
    rel_strs = list(G.relators())
    r = len(rel_strs)
    rel_words = [parse_snappy_word(w, gen_to_idx) for w in rel_strs]
    per_strs = list(G.peripheral_curves())
    c = len(per_strs)
    assert c == M.num_cusps()
    per_words: List[Tuple[List[int], List[int]]] = [
        (parse_snappy_word(mer, gen_to_idx), parse_snappy_word(lon, gen_to_idx))
        for (mer, lon) in per_strs
    ]
    # Abelianization matrix M_ab (r x m)
    M_ab = [[0] * m for _ in range(r)]
    for j, rw in enumerate(rel_words):
        for tok in rw:
            if tok > 0:
                M_ab[j][tok - 1] += 1
            else:
                M_ab[j][-tok - 1] -= 1
    sp_M = sp.Matrix(M_ab) if r > 0 else sp.zeros(0, m)
    if r > 0:
        D, U, V = smith_nonneg(sp_M)
        diag = [int(D[i, i]) for i in range(min(r, m))]
    else:
        D, U, V = sp.zeros(0, m), sp.eye(0), sp.eye(m)
        diag = []
    torsion_divs = sorted([d for d in diag if d > 1])
    snappy_tors = sorted([int(x) for x in M.homology().elementary_divisors() if int(x) > 1])
    assert torsion_divs == snappy_tors, f"SNF torsion {torsion_divs} != SnapPy {snappy_tors}"
    tors_exp = lcm_list(torsion_divs) if torsion_divs else 1
    return {
        "m": m,
        "r": r,
        "c": c,
        "gens": gens,
        "rel_words": rel_words,
        "per_words": per_words,
        "M_ab": M_ab,
        "D_diag": diag,
        "V_snf": [[int(V[i, j]) for j in range(m)] for i in range(m)],
        "torsion_divs": torsion_divs,
        "torsion_exponent": tors_exp,
    }


def count_characters_mod_N(pres: Dict[str, Any], N: int) -> int:
    m = pres["m"]
    diag = pres["D_diag"]
    prod = 1
    for k in range(m):
        dk = diag[k] if k < len(diag) else 0
        prod *= N if dk == 0 else math.gcd(dk, N)
    return prod


def enumerate_characters_mod_N(pres: Dict[str, Any], N: int) -> List[Tuple[int, ...]]:
    """
    Exact enumeration of Hom(H_1(P), Z/N Z), returning tuples e = (e_0, ..., e_{m-1}) in {0..N-1}^m
    with e = (0, ..., 0) guaranteed to be at index 0.
    """
    m = pres["m"]
    diag = pres["D_diag"]
    V = pres["V_snf"]
    M_ab = pres["M_ab"]
    ranges: List[List[int]] = []
    for k in range(m):
        dk = diag[k] if k < len(diag) else 0
        if dk == 0:
            ranges.append(list(range(N)))
        else:
            g = math.gcd(dk, N)
            step = N // g
            ranges.append([q * step for q in range(g)])
    chars: List[Tuple[int, ...]] = []
    for y in itertools.product(*ranges):
        e = tuple(sum(V[i][k] * y[k] for k in range(m)) % N for i in range(m))
        chars.append(e)
    # Sort with trivial character (0,...,0) first
    zero_t = (0,) * m
    chars = sorted(set(chars), key=lambda t: (0 if t == zero_t else 1, t))
    assert len(chars) == count_characters_mod_N(pres, N)
    assert chars[0] == zero_t
    # Verify M_ab * e == 0 mod N on all characters
    for e in chars:
        for row in M_ab:
            assert sum(row[k] * e[k] for k in range(m)) % N == 0
    return chars


# ============================================================================
# DIRECT 2x2 MATRIX FOX CALCULUS CROSS-CHECKER (ZERO-TRUST GUARDRAIL)
# ============================================================================

def mat2_mul_p(A: Tuple[int, int, int, int], B: Tuple[int, int, int, int], p: int) -> Tuple[int, int, int, int]:
    return (
        (A[0] * B[0] + A[1] * B[2]) % p,
        (A[0] * B[1] + A[1] * B[3]) % p,
        (A[2] * B[0] + A[3] * B[2]) % p,
        (A[2] * B[1] + A[3] * B[3]) % p,
    )


def mat2_inv_p(A: Tuple[int, int, int, int], p: int) -> Tuple[int, int, int, int]:
    det = (A[0] * A[3] - A[1] * A[2]) % p
    assert det != 0
    inv_d = pow(det, p - 2, p)
    return (
        (A[3] * inv_d) % p,
        (-A[1] * inv_d) % p,
        (-A[2] * inv_d) % p,
        (A[0] * inv_d) % p,
    )


def direct_2x2_cohomology_mod_p(
    m: int,
    rel_words: List[List[int]],
    per_words: List[Tuple[List[int], List[int]]],
    gen_mats: List[Tuple[int, int, int, int]],
    p: int,
    klein_bottle_cusp: bool = False,
) -> Dict[str, Any]:
    """
    Completely independent direct 2x2 matrix Fox-calculus evaluator for ANY GL_2(F_p)
    representation (upper-triangular, lower-triangular contragredient rho^{-T}, or twisted).
    Uses block ordering (u_1(g_0..g_{m-1}), u_2(g_0..g_{m-1})).
    """
    inv_mats = [mat2_inv_p(G, p) for G in gen_mats]

    def fox_word(w: List[int]) -> Tuple[Tuple[int, int, int, int], List[List[int]]]:
        # Returns (holonomy_2x2, 2 x 2m Fox Jacobian in block coord ordering)
        P = (1, 0, 0, 1)
        J = [[0] * (2 * m), [0] * (2 * m)]
        for tok in w:
            if tok > 0:
                k = tok - 1
                eff = P
                P = mat2_mul_p(P, gen_mats[k], p)
                J[0][k] = (J[0][k] + eff[0]) % p
                J[0][m + k] = (J[0][m + k] + eff[1]) % p
                J[1][k] = (J[1][k] + eff[2]) % p
                J[1][m + k] = (J[1][m + k] + eff[3]) % p
            else:
                k = -tok - 1
                P = mat2_mul_p(P, inv_mats[k], p)
                eff = P
                J[0][k] = (J[0][k] - eff[0]) % p
                J[0][m + k] = (J[0][m + k] - eff[1]) % p
                J[1][k] = (J[1][k] - eff[2]) % p
                J[1][m + k] = (J[1][m + k] - eff[3]) % p
        return P, J

    J_rel: List[List[int]] = []
    for rw in rel_words:
        hol, Jr = fox_word(rw)
        assert hol == (1, 0, 0, 1), f"Relator holonomy != I_2: {hol}"
        J_rel.append(Jr[0])
        J_rel.append(Jr[1])

    # Global coboundary d0_P (2m x 2)
    col0 = [0] * (2 * m)
    col1 = [0] * (2 * m)
    for k in range(m):
        G = gen_mats[k]
        col0[k] = (G[0] - 1) % p
        col1[k] = G[1] % p
        col0[m + k] = G[2] % p
        col1[m + k] = (G[3] - 1) % p
    b_dim = rank_2col_mod_p(col0, col1, p)
    h0_P = 2 - b_dim
    U_Z = nullspace_mod_p(J_rel, 2 * m, p)
    z_dim = len(U_Z)
    h1_P = z_dim - b_dim

    # Peripheral data per cusp
    h0_per_list: List[int] = []
    h1_per_list: List[int] = []
    B_per_blocks: List[List[List[int]]] = []
    R_Z_blocks: List[List[List[int]]] = []
    for (mw, lw) in per_words:
        M_i, Jm = fox_word(mw)
        L_i, Jl = fox_word(lw)
        # Rows in order: w_1(mu), w_1(lam), w_2(mu), w_2(lam)
        R_i = [Jm[0], Jl[0], Jm[1], Jl[1]]
        # Peripheral coboundary d0_{T_i} (4 x 2)
        c0 = [(M_i[0] - 1) % p, (L_i[0] - 1) % p, M_i[2] % p, L_i[2] % p]
        c1 = [M_i[1] % p, L_i[1] % p, (M_i[3] - 1) % p, (L_i[3] - 1) % p]
        b_i = rank_2col_mod_p(c0, c1, p)
        h0_i = 2 - b_i
        if not klein_bottle_cusp:
            # Commutator mu * lam * mu^-1 * lam^-1 = 1: (I - L) w_mu + (M - I) w_lam = 0
            assert mat2_mul_p(M_i, L_i, p) == mat2_mul_p(L_i, M_i, p)
            d1_rows = [
                [(1 - L_i[0]) % p, (M_i[0] - 1) % p, (-L_i[1]) % p, M_i[1] % p],
                [(-L_i[2]) % p, M_i[2] % p, (1 - L_i[3]) % p, (M_i[3] - 1) % p],
            ]
        else:
            # Klein bottle t * lam * t^-1 * lam = 1: (I - L^-1) w_t + (M + L^-1) w_lam = 0
            invL = mat2_inv_p(L_i, p)
            assert mat2_mul_p(M_i, L_i, p) == mat2_mul_p(invL, M_i, p)
            d1_rows = [
                [(1 - invL[0]) % p, (M_i[0] + invL[0]) % p, (-invL[1]) % p, (M_i[1] + invL[1]) % p],
                [(-invL[2]) % p, (M_i[2] + invL[2]) % p, (1 - invL[3]) % p, (M_i[3] + invL[3]) % p],
            ]
        z_i = 4 - rank_mod_p(d1_rows, 4, p)
        h1_i = z_i - b_i
        h0_per_list.append(h0_i)
        h1_per_list.append(h1_i)
        B_per_blocks.append([c0, c1])  # 2 columns of length 4
        # Compute R_i * U_Z^T -> z_dim columns of length 4
        rz_cols: List[List[int]] = []
        for u in U_Z:
            rz_cols.append([sum(R_i[row_idx][q] * u[q] for q in range(2 * m)) % p for row_idx in range(4)])
        R_Z_blocks.append(rz_cols)

    c_cnt = len(per_words)
    # Build (4c x (2c + z_dim)) stacked matrix as rows over (2c + z_dim) columns (or transpose since rank(A) == rank(A^T)!)
    # Using transpose: rows are spanning vectors in F_p^{4c}!
    b_rows_4c: List[List[int]] = []
    for i in range(c_cnt):
        for col_vec in B_per_blocks[i]:
            full_v = [0] * (4 * c_cnt)
            full_v[4 * i : 4 * (i + 1)] = col_vec
            b_rows_4c.append(full_v)
    rz_rows_4c: List[List[int]] = []
    for u_idx in range(z_dim):
        full_v = [0] * (4 * c_cnt)
        for i in range(c_cnt):
            full_v[4 * i : 4 * (i + 1)] = R_Z_blocks[i][u_idx]
        rz_rows_4c.append(full_v)

    rk_B = rank_mod_p(b_rows_4c, 4 * c_cnt, p)
    assert rk_B == sum(2 - h0 for h0 in h0_per_list)
    rk_BR = rank_mod_p(b_rows_4c + rz_rows_4c, 4 * c_cnt, p)
    dim_A = rk_BR - rk_B
    n_int = h1_P - dim_A
    return {
        "h0": h0_P,
        "h1": h1_P,
        "h0_per": sum(h0_per_list),
        "h1_per": sum(h1_per_list),
        "h0_per_list": h0_per_list,
        "h1_per_list": h1_per_list,
        "dim_A": dim_A,
        "n_int": n_int,
        "J_rel": J_rel,
    }


# ============================================================================
# PART 1: SM-C8 — THE PARTNER TEST ON B1441 TIER 1 (74 MANIFOLDS, 71 ACTIVE)
# ============================================================================

def build_b1441_population() -> List[Tuple[str, "snappy.Manifold"]]:
    pop: List[Tuple[str, "snappy.Manifold"]] = []
    roots = ["m004", "m003", "m009", "m010"]
    root_counts: Dict[str, int] = {}
    for rname in roots:
        M_root = snappy.Manifold(rname)
        cnt = 0
        for deg in range(2, 7):
            covs = M_root.covers(deg)
            for idx, C in enumerate(covs):
                if C.num_cusps() >= 2:
                    pop.append((f"{rname}_deg{deg}_{idx}", C))
                    cnt += 1
        root_counts[rname] = cnt
    assert [root_counts[r] for r in roots] == [11, 7, 24, 27], f"Unexpected cover counts: {root_counts}"
    for named in ["m202", "s959", "o10_150726", "m129", "m125"]:
        pop.append((named, snappy.Manifold(named)))
    assert len(pop) == 74
    return pop


def project_cusp_cohomology_mod_p(
    alpha_m: int,
    alpha_l: int,
    beta_m: int,
    beta_l: int,
    zm: int,
    zl: int,
    p: int,
) -> Tuple[int, int, int, Optional[List[List[int]]], Optional[List[List[int]]]]:
    """
    Exact peripheral cohomology H^0(T_i; V), H^1(T_i; V), projection Pi_i : Z^1(T_i; V) -> F_p^{h_i}
    with ker(Pi_i) = B^1(T_i; V), and image S_i = Pi_i(iota(Z^1(T_i; alpha))) as spanning vectors in F_p^{h_i}.
    Computed directly from d^0_{T_i} and d^1_{T_i} (Guardrail 2: zero literal flags).
    """
    zm_b = (zm * beta_m) % p
    zl_b = (zl * beta_l) % p
    c0 = [(alpha_m - 1) % p, (alpha_l - 1) % p, 0, 0]
    c1 = [zm_b, zl_b, (beta_m - 1) % p, (beta_l - 1) % p]
    b_i = rank_2col_mod_p(c0, c1, p)
    h0_i = 2 - b_i

    d1_r0 = [(1 - alpha_l) % p, (alpha_m - 1) % p, (-zl_b) % p, zm_b]
    d1_r1 = [0, 0, (1 - beta_l) % p, (beta_m - 1) % p]
    rk_d1 = rank_2col_mod_p(d1_r0, d1_r1, p)
    z_i = 4 - rk_d1
    h1_i = z_i - b_i
    if h1_i == 0:
        return h0_i, 0, 0, None, None

    # Build explicit quotient projection Pi_i : F_p^4 -> F_p^{h1_i} vanishing on B^1(T_i; V)
    # and injective on Z^1(T_i; V) / B^1(T_i; V):
    if b_i == 0:
        # M_i = L_i = I_2 => B^1 = 0, Z^1 = F_p^4, h1_i = 4
        assert h1_i == 4
        Pi = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    else:
        assert b_i == 1 and h1_i == 2
        vB = c0 if any(x != 0 for x in c0) else c1
        Z_basis = nullspace_mod_p([d1_r0, d1_r1], 4, p)
        assert len(Z_basis) == 3
        # Pick 2 vectors w1, w2 from Z_basis completing vB to a basis of Z^1 (dim 3)
        basis_3 = [vB]
        for u in Z_basis:
            if rank_mod_p(basis_3 + [u], 4, p) > len(basis_3):
                basis_3.append(u)
                if len(basis_3) == 3:
                    break
        assert len(basis_3) == 3
        # Invert 3x4 row basis on its 3 pivot columns so Pi * vB = (0, 0), Pi * w1 = (1, 0), Pi * w2 = (0, 1)
        _, piv3 = rref_mod_p(basis_3, 4, p)
        assert len(piv3) == 3
        # Solve 3x3 matrix M3[col_a, row_b] = basis_3[row_b][piv3[col_a]]
        aug = [
            [basis_3[0][piv3[0]], basis_3[1][piv3[0]], basis_3[2][piv3[0]], 1, 0, 0],
            [basis_3[0][piv3[1]], basis_3[1][piv3[1]], basis_3[2][piv3[1]], 0, 1, 0],
            [basis_3[0][piv3[2]], basis_3[1][piv3[2]], basis_3[2][piv3[2]], 0, 0, 1],
        ]
        rref_aug, piv_aug = rref_mod_p(aug, 6, p)
        assert piv_aug == [0, 1, 2]
        # Coordinates (coeff of w1, coeff of w2) are rows 1 and 2 of M3^{-1} applied to x[piv3]!
        Pi = [[0, 0, 0, 0], [0, 0, 0, 0]]
        for q_idx, pc in enumerate(piv3):
            Pi[0][pc] = rref_aug[1][3 + q_idx] % p
            Pi[1][pc] = rref_aug[2][3 + q_idx] % p
        # Sanity check: Pi * vB == 0
        assert sum(Pi[0][q] * vB[q] for q in range(4)) % p == 0
        assert sum(Pi[1][q] * vB[q] for q in range(4)) % p == 0

    # Image S_i of Z^1(T_i; alpha) in F_p^{h1_i}:
    if alpha_m == 1 and alpha_l == 1:
        # Z^1(T_i; alpha) = span(e_0, e_1) in F_p^4
        raw_S = [[Pi[r_i][0] for r_i in range(h1_i)], [Pi[r_i][1] for r_i in range(h1_i)]]
        S_rref, _ = rref_mod_p(raw_S, h1_i, p)
        dim_S = len(S_rref)
        S_vecs = S_rref
    else:
        # Z^1(T_i; alpha) = B^1(T_i; alpha) = span(c0) subset B^1(T_i; V), verify Pi * c0 == 0!
        assert all(sum(Pi[r_i][q] * c0[q] for q in range(4)) % p == 0 for r_i in range(h1_i))
        dim_S = 0
        S_vecs = []

    return h0_i, h1_i, dim_S, Pi, S_vecs


def evaluate_sm_c8_entry_at_prime(
    entry_idx: int,
    name: str,
    pres: Dict[str, Any],
    N: int,
    chars: List[Tuple[int, ...]],
    p: int,
    run_direct_crosscheck: bool = True,
) -> Dict[str, Any]:
    """
    Evaluate all non-split rank-2 modules V(ell, alpha, z) and non-vacuous joins (P, V, T_i)
    on a single active manifold entry P in exact arithmetic over F_p.
    """
    m = pres["m"]
    r = pres["r"]
    c = pres["c"]
    rel_words = pres["rel_words"]
    per_words = pres["per_words"]
    all_words: List[List[int]] = list(rel_words)
    for mw, lw in per_words:
        all_words.append(mw)
        all_words.append(lw)
    W_cnt = len(all_words)
    assert W_cnt == r + 2 * c

    K = len(chars)
    char_to_idx = {e: idx for idx, e in enumerate(chars)}
    zeta = primitive_nth_root_mod_p(N, p)

    # Precompute character values & group subtraction table (alpha - ell) mod N
    chi_vals = [[pow(zeta, ek, p) for ek in e] for e in chars]
    chi_invs = [[pow(zeta, (-ek) % N, p) for ek in e] for e in chars]
    char_sub = [[0] * K for _ in range(K)]
    for i_a, ea in enumerate(chars):
        for i_b, eb in enumerate(chars):
            diff = tuple((ea[k] - eb[k]) % N for k in range(m))
            char_sub[i_a][i_b] = char_to_idx[diff]

    # Flatten word steps for vectorized coupling computation
    step_word: List[int] = []
    step_gen: List[int] = []
    step_sign: List[int] = []
    for w_idx, w in enumerate(all_words):
        for tok in w:
            step_word.append(w_idx)
            step_gen.append(abs(tok) - 1)
            step_sign.append(1 if tok > 0 else -1)
    L_tot = len(step_word)

    # Group step indices by (w_idx, gen_k) with signs
    steps_by_wg: List[List[List[Tuple[int, int]]]] = [[[] for _ in range(m)] for _ in range(W_cnt)]
    for s_idx in range(L_tot):
        steps_by_wg[step_word[s_idx]][step_gen[s_idx]].append((s_idx, step_sign[s_idx]))

    # Precompute J1[chi] (W_cnt x m), peripheral holonomies per_hol[chi] (2c), and B_eff[chi, s_idx] (K x L_tot)
    J1_all: List[List[List[int]]] = [[[0] * m for _ in range(W_cnt)] for _ in range(K)]
    per_hol: List[List[int]] = [[1] * (2 * c) for _ in range(K)]
    B_eff = np.zeros((K, max(L_tot, 1)), dtype=np.int64)

    for chi in range(K):
        vals = chi_vals[chi]
        invs = chi_invs[chi]
        s_cursor = 0
        for w_idx, w in enumerate(all_words):
            cur = 1
            row_J = J1_all[chi][w_idx]
            for tok in w:
                if tok > 0:
                    k = tok - 1
                    eff = cur
                    cur = (cur * vals[k]) % p
                    row_J[k] = (row_J[k] + eff) % p
                else:
                    k = -tok - 1
                    cur = (cur * invs[k]) % p
                    eff = cur
                    row_J[k] = (row_J[k] - eff) % p
                B_eff[chi, s_cursor] = eff
                s_cursor += 1
            if w_idx < r:
                assert cur == 1, f"Character {chi} failed relator {w_idx} on {name}"
            else:
                per_hol[chi][w_idx - r] = cur

    # Enumerate non-trivial characters ell with h^1(P; ell) >= 1 and build cocycle lists
    ell_cocycles: List[Tuple[int, int, List[List[int]]]] = []  # (ell, h1_ell, list_of_z)
    h1_ell_hist: Counter = Counter()
    for ell in range(1, K):
        J1_rel_ell = J1_all[ell][:r]
        Z1_ell = nullspace_mod_p(J1_rel_ell, m, p)
        v_cob = [(chi_vals[ell][k] - 1) % p for k in range(m)]
        assert any(x != 0 for x in v_cob)
        # Quotient Z1_ell by span(v_cob)
        cur_span = [v_cob]
        H1_basis: List[List[int]] = []
        for u in Z1_ell:
            if rank_mod_p(cur_span + [u], m, p) > len(cur_span):
                cur_span.append(u)
                H1_basis.append(u)
        h1_ell = len(H1_basis)
        assert h1_ell == len(Z1_ell) - 1
        if h1_ell == 0:
            continue
        h1_ell_hist[h1_ell] += 1
        if h1_ell == 1:
            cocs = [H1_basis[0]]
        else:
            # Basis + 2 deterministic non-collinear combinations seeded solely from (entry_idx, ell)
            cocs = list(H1_basis)
            seed_bytes = hashlib.sha256(f"X-SM2:{entry_idx}:{ell}".encode("utf-8")).digest()
            w1 = [1 + ((seed_bytes[q % 32] + 17 * q) % 97) for q in range(h1_ell)]
            w2 = [1 + ((seed_bytes[(q + 11) % 32] + 31 * (q + 1)) % 89) for q in range(h1_ell)]
            if all((w1[q] * w2[0] - w2[q] * w1[0]) % p == 0 for q in range(h1_ell)):
                w2[-1] = (w2[-1] + 1) % p
                if w2[-1] == 0:
                    w2[-1] = 2
            comb1 = [sum(w1[q] * H1_basis[q][k] for q in range(h1_ell)) % p for k in range(m)]
            comb2 = [sum(w2[q] * H1_basis[q][k] for q in range(h1_ell)) % p for k in range(m)]
            assert rank_mod_p([v_cob, comb1, comb2], m, p) == 3
            cocs.append(comb1)
            cocs.append(comb2)
        ell_cocycles.append((ell, h1_ell, cocs))

    # Counters for this entry
    n_modules = 0
    n_joins_total = 0
    n_joins_vacuous = 0
    n_joins_nonvac = 0
    index_hist: Counter = Counter()
    d_ord_hist: Counter = Counter()
    leak_hist: Counter = Counter()
    d_ord_nonzero_no_leak = 0
    split_I2_count = 0
    split_I2_D_hist: Counter = Counter()
    split_eigen_count = 0
    split_eigen_D_hist: Counter = Counter()

    c1_fails = 0
    c2_fails = 0
    c3a_fails = 0
    c3b_fails = 0
    s_perp_fails = 0
    b1438_form_fails = 0

    p1_c8_fails = 0
    p2_c8_fails = 0
    p3_c8_fails = 0

    direct_checks_done = 0
    witnesses_absI2: List[Tuple[int, int, List[int], int]] = []
    sampled_records: List[Tuple[int, int, List[int], int, int, int]] = []

    for ell, h1_ell, cocs in ell_cocycles:
        vals_ell = chi_vals[ell]
        invs_ell = chi_invs[ell]
        alphas = [a for a in range(1, K) if a != ell]

        for z_idx, z_vec in enumerate(cocs):
            # Walk all words once to record eff_z[s_idx] and peripheral z(mu_i), z(lam_i)
            eff_z = np.zeros(max(L_tot, 1), dtype=np.int64)
            z_per = [0] * (2 * c)
            s_cursor = 0
            for w_idx, w in enumerate(all_words):
                cur_e = 1
                cur_z = 0
                for tok in w:
                    if tok > 0:
                        k = tok - 1
                        ez = cur_z
                        cur_z = (cur_z + cur_e * z_vec[k]) % p
                        cur_e = (cur_e * vals_ell[k]) % p
                        eff_z[s_cursor] = ez
                    else:
                        k = -tok - 1
                        inv_e = invs_ell[k]
                        cur_z = (cur_z - ((cur_e * inv_e) % p) * z_vec[k]) % p
                        cur_e = (cur_e * inv_e) % p
                        eff_z[s_cursor] = cur_z
                    s_cursor += 1
                if w_idx < r:
                    assert cur_z == 0 and cur_e == 1
                else:
                    z_per[w_idx - r] = cur_z

            # Compute C_all[beta, w_idx, k] for all beta in 0..K-1 via vectorized dot products!
            C_all = np.zeros((K, W_cnt, m), dtype=np.int64)
            for w_idx in range(W_cnt):
                for k in range(m):
                     pairs_sg = steps_by_wg[w_idx][k]
                     if not pairs_sg:
                         continue
                     idxs = [pr[0] for pr in pairs_sg]
                     sgns = np.array([pr[1] for pr in pairs_sg], dtype=np.int64)
                     weights = (sgns * eff_z[idxs]) % p
                     if np.any(weights):
                         C_all[:, w_idx, k] = (B_eff[:, idxs] @ weights) % p
            C_list = C_all.tolist()

            # Compute per-alpha module cohomology data for this (ell, z_vec) batch
            batch_data: Dict[int, Dict[str, Any]] = {}
            for alpha in alphas:
                beta = char_sub[alpha][ell]
                assert beta != 0

                # Build J2_rel (2r x 2m)
                J1_a = J1_all[alpha]
                J1_b = J1_all[beta]
                C_b = C_list[beta]
                J2_rel: List[List[int]] = []
                for j in range(r):
                    J2_rel.append(J1_a[j] + C_b[j])
                for j in range(r):
                    J2_rel.append(([0] * m) + J1_b[j])

                U_Z = nullspace_mod_p(J2_rel, 2 * m, p)
                z_dim = len(U_Z)

                # Global coboundary d0_P (2m x 2)
                c0_P = [(chi_vals[alpha][k] - 1) % p for k in range(m)] + ([0] * m)
                c1_P = [(z_vec[k] * chi_vals[beta][k]) % p for k in range(m)] + [
                    (chi_vals[beta][k] - 1) % p for k in range(m)
                ]
                b_dim = rank_2col_mod_p(c0_P, c1_P, p)
                h0_P = 2 - b_dim
                h1_P = z_dim - b_dim

                # Direct 2x2 Fox & contragredient rho^{-T} cross-check on first 3 modules per entry
                if run_direct_crosscheck and direct_checks_done < 3:
                    gen_mats = [
                        (
                            chi_vals[alpha][k],
                            (z_vec[k] * chi_vals[beta][k]) % p,
                            0,
                            chi_vals[beta][k],
                        )
                        for k in range(m)
                    ]
                    dc = direct_2x2_cohomology_mod_p(m, rel_words, per_words, gen_mats, p)
                    # Also test explicit contragredient rho_V(g)^{-T} without basis change J!
                    dual_mats_raw = []
                    for G in gen_mats:
                        invG = mat2_inv_p(G, p)
                        dual_mats_raw.append((invG[0], invG[2], invG[1], invG[3]))
                    dc_dual_raw = direct_2x2_cohomology_mod_p(m, rel_words, per_words, dual_mats_raw, p)
                    direct_checks_done += 1
                else:
                    dc = None
                    dc_dual_raw = None

                # Peripheral cohomology & projections per cusp
                h0_dP = 0
                h1_dP = 0
                cusp_info: List[Optional[Dict[str, Any]]] = [None] * c
                active_cusps: List[int] = []
                offsets: Dict[int, Tuple[int, int]] = {}
                H_dP_cur = 0

                # Pre-transpose U_Z for fast dot products: U_Z is z_dim vectors of length 2m
                for i in range(c):
                    am = per_hol[alpha][2 * i]
                    al = per_hol[alpha][2 * i + 1]
                    bm = per_hol[beta][2 * i]
                    bl = per_hol[beta][2 * i + 1]
                    zm = z_per[2 * i]
                    zl = z_per[2 * i + 1]
                    h0_i, h1_i, dim_Si, Pi_i, S_vecs = project_cusp_cohomology_mod_p(
                        am, al, bm, bl, zm, zl, p
                    )
                    h0_dP += h0_i
                    h1_dP += h1_i
                    if h1_i == 0:
                        continue
                    assert Pi_i is not None and S_vecs is not None
                    # Build 4 x 2m restriction matrix R_i:
                    R_i = [
                        J1_a[r + 2 * i] + C_b[r + 2 * i],
                        J1_a[r + 2 * i + 1] + C_b[r + 2 * i + 1],
                        ([0] * m) + J1_b[r + 2 * i],
                        ([0] * m) + J1_b[r + 2 * i + 1],
                    ]
                    # Pi_R_i = Pi_i (h1_i x 4) * R_i (4 x 2m) -> (h1_i x 2m)
                    Pi_R_i = [
                        [sum(Pi_i[row_a][q] * R_i[q][col_b] for q in range(4)) % p for col_b in range(2 * m)]
                        for row_a in range(h1_i)
                    ]
                    # M_i_rows: z_dim vectors of length h1_i (each global Z^1 basis vector restricted to F_p^{h1_i})
                    M_i_vecs = [
                        [sum(Pi_R_i[row_a][col_b] * u[col_b] for col_b in range(2 * m)) % p for row_a in range(h1_i)]
                        for u in U_Z
                    ]
                    active_cusps.append(i)
                    offsets[i] = (H_dP_cur, H_dP_cur + h1_i)
                    H_dP_cur += h1_i
                    cusp_info[i] = {
                        "h0_i": h0_i,
                        "h1_i": h1_i,
                        "dim_Si": dim_Si,
                        "S_vecs": S_vecs,
                        "M_i_vecs": M_i_vecs,
                        "am": am,
                        "al": al,
                        "bm": bm,
                        "bl": bl,
                        "zm": zm,
                        "zl": zl,
                    }

                assert H_dP_cur == h1_dP
                # Build stacked restriction vectors M_res_vecs: z_dim vectors in F_p^{H_dP}
                if H_dP_cur == 0:
                    dim_AV = 0
                    M_res_vecs: List[List[int]] = []
                else:
                    M_res_vecs = []
                    for u_idx in range(z_dim):
                        vec: List[int] = []
                        for i in active_cusps:
                            vec.extend(cusp_info[i]["M_i_vecs"][u_idx])  # type: ignore[index]
                        M_res_vecs.append(vec)
                    dim_AV = rank_mod_p(M_res_vecs, H_dP_cur, p)
                n_V = h1_P - dim_AV

                if dc is not None:
                    assert (h0_P, h1_P, h0_dP, h1_dP, dim_AV, n_V) == (
                        dc["h0"],
                        dc["h1"],
                        dc["h0_per"],
                        dc["h1_per"],
                        dc["dim_A"],
                        dc["n_int"],
                    )

                # Conditioned counts at every non-vacuous cusp i
                n_zero_Si_map: Dict[int, int] = {}
                n_free_Si_map: Dict[int, int] = {}
                n_free_rand_map: Dict[int, int] = {}
                split_I2_quot_map: Dict[int, int] = {}
                split_eigen_D_map: Dict[int, int] = {}

                for i in active_cusps:
                    ci = cusp_info[i]
                    assert ci is not None
                    h1_i = ci["h1_i"]
                    dim_Si = ci["dim_Si"]
                    S_vecs = ci["S_vecs"]
                    M_i_vecs = ci["M_i_vecs"]
                    lo, hi = offsets[i]

                    # 1. n(V | free elsewhere, S_i):
                    if dim_Si == 0:
                        rk_f = rank_mod_p(M_i_vecs, h1_i, p)
                        n_free_Si_map[i] = h1_P - rk_f
                    elif dim_Si == h1_i:
                        n_free_Si_map[i] = h1_P
                    else:
                        rk_f = rank_mod_p(S_vecs + M_i_vecs, h1_i, p)
                        n_free_Si_map[i] = h1_P + dim_Si - rk_f

                    # 2. n(V | 0 elsewhere, S_i):
                    if dim_Si == 0:
                        n_zero_Si_map[i] = n_V
                    elif dim_Si == h1_i:
                        # Drop slice [lo:hi] from M_res_vecs
                        rem_len = H_dP_cur - h1_i
                        if rem_len == 0:
                            n_zero_Si_map[i] = h1_P
                        else:
                            rem_vecs = [v[:lo] + v[hi:] for v in M_res_vecs]
                            n_zero_Si_map[i] = h1_P - rank_mod_p(rem_vecs, rem_len, p)
                    else:
                        emb_S: List[List[int]] = []
                        for sv in S_vecs:
                            ev = [0] * H_dP_cur
                            ev[lo:hi] = sv
                            emb_S.append(ev)
                        rk_z = rank_mod_p(emb_S + M_res_vecs, H_dP_cur, p)
                        n_zero_Si_map[i] = h1_P + dim_Si - rk_z

                    # 3. Plant P2_C8 helper: deterministic non-canonical line L_rand in F_p^{h1_i}
                    # Make sure L_rand != S_vecs: pick vector (1, c_rand, ...) outside S_vecs if dim_Si < h1_i
                    c_seed = (1 + (37 * entry_idx + 101 * alpha + 13 * ell + 7 * i + 3 * z_idx) % (p - 3)) % p
                    if c_seed == 0:
                        c_seed = 2
                    rand_line = [0] * h1_i
                    rand_line[0] = 1
                    rand_line[1] = c_seed
                    if dim_Si == 1 and rank_mod_p(S_vecs + [rand_line], h1_i, p) == 1:
                        rand_line[1] = (rand_line[1] + 1) % p
                    rk_rand = rank_mod_p([rand_line] + M_i_vecs, h1_i, p)
                    n_free_rand_map[i] = h1_P + 1 - rk_rand

                    # 4. Original card split-torus D where V|_{T_i} splits:
                    # (a) Trivial I_2 on T_i (am=al=bm=bl=1, zm=zl=0 => h1_i == 4, Pi_i == I_4):
                    if h1_i == 4:
                        # sub = span(e_0, e_1), quotient = span(e_2, e_3)
                        emb_Q = []
                        for q_coord in (2, 3):
                            ev = [0] * H_dP_cur
                            ev[lo + q_coord] = 1
                            emb_Q.append(ev)
                        n_zero_Q = h1_P + 2 - rank_mod_p(emb_Q + M_res_vecs, H_dP_cur, p)
                        split_I2_quot_map[i] = n_zero_Si_map[i] - n_zero_Q
                    # (b) Distinct eigencharacters on T_i ((am,al) != (bm,bl)):
                    if (ci["am"], ci["al"]) != (ci["bm"], ci["bl"]):
                        # Canonical eigenlines E_alpha (sub) and E_beta (lifting quotient):
                        if ci["bm"] == 1 and ci["bl"] == 1:
                            # E_alpha has H^1=0, E_beta has H^1 = H^1(T_i; V) (all on T_i, 0 elsewhere)
                            rem_len = H_dP_cur - h1_i
                            n_zero_Ebeta = (
                                h1_P
                                if rem_len == 0
                                else h1_P - rank_mod_p([v[:lo] + v[hi:] for v in M_res_vecs], rem_len, p)
                            )
                            split_eigen_D_map[i] = n_zero_Si_map[i] - n_zero_Ebeta
                        else:
                            # E_alpha has H^1 = H^1(T_i; V), E_beta has H^1 = 0
                            split_eigen_D_map[i] = n_zero_Si_map[i] - n_V

                batch_data[alpha] = {
                    "beta": beta,
                    "h0": h0_P,
                    "h1": h1_P,
                    "h0_dP": h0_dP,
                    "h1_dP": h1_dP,
                    "dim_A": dim_AV,
                    "n_int": n_V,
                    "cusp_info": cusp_info,
                    "n_zero_Si": n_zero_Si_map,
                    "n_free_Si": n_free_Si_map,
                    "n_free_rand": n_free_rand_map,
                    "split_I2_D": split_I2_quot_map,
                    "split_eigen_D": split_eigen_D_map,
                    "dc_dual_raw": dc_dual_raw,
                }

            # Pair every module V = V(ell, alpha, z) with its dual V* = V(ell, ell - alpha, z)
            for alpha in alphas:
                alpha_star = char_sub[ell][alpha]
                dV = batch_data[alpha]
                dVs = batch_data[alpha_star]
                if dV["dc_dual_raw"] is not None:
                    raw = dV["dc_dual_raw"]
                    assert (dVs["h0"], dVs["h1"], dVs["h0_dP"], dVs["h1_dP"], dVs["dim_A"], dVs["n_int"]) == (
                        raw["h0"],
                        raw["h1"],
                        raw["h0_per"],
                        raw["h1_per"],
                        raw["dim_A"],
                        raw["n_int"],
                    )

                n_modules += 1
                n_joins_total += c

                # Control C1: dim A_V + dim A_V* == h^1(dP; V)
                if dV["dim_A"] + dVs["dim_A"] != dV["h1_dP"]:
                    c1_fails += 1
                # Plant P3_C8: 2 dim A_V == h^1(dP; V)
                if 2 * dV["dim_A"] != dV["h1_dP"]:
                    p3_c8_fails += 1

                # Control C2: [h1(V*) - h0(V*)] - [h1(V) - h0(V)] == dim A_V* - h0(dP; V*)
                lhs_c2 = (dVs["h1"] - dVs["h0"]) - (dV["h1"] - dV["h0"])
                rhs_c2 = dVs["dim_A"] - dVs["h0_dP"]
                if lhs_c2 != rhs_c2:
                    c2_fails += 1

                # Control C3a: n(V | 0) - n(V* | all) == -h0(dP; V) + h0(V) - h0(V*)
                # Note n(V* | all) = h1(P; V*)!
                if (dV["n_int"] - dVs["h1"]) != (-dV["h0_dP"] + dV["h0"] - dVs["h0"]):
                    c3a_fails += 1

                # Record index I(V) = n(V) - n(V*) and B1438 form h1(V*) - h1(V)
                idx_I = dV["n_int"] - dVs["n_int"]
                if idx_I != (dVs["h1"] - dV["h1"]):
                    b1438_form_fails += 1
                index_hist[idx_I] += 1

                if abs(idx_I) >= 2:
                    witnesses_absI2.append((ell, alpha, z_vec, idx_I))
                if len(sampled_records) < 8:
                    sampled_records.append((ell, alpha, z_vec, dV["h1"], dV["dim_A"], idx_I))

                # Joins (P, V, T_i)
                for i in range(c):
                    ci_V = dV["cusp_info"][i]
                    ci_Vs = dVs["cusp_info"][i]
                    if ci_V is None:
                        assert ci_Vs is None
                        n_joins_vacuous += 1
                        continue
                    assert ci_Vs is not None
                    n_joins_nonvac += 1
                    h1_Ti = ci_V["h1_i"]
                    assert h1_Ti == ci_Vs["h1_i"]
                    dim_Si = ci_V["dim_Si"]
                    dim_Sis = ci_Vs["dim_Si"]
                    if dim_Si + dim_Sis != h1_Ti:
                        s_perp_fails += 1

                    nV_0_Si = dV["n_zero_Si"][i]
                    nVs_0_Sis = dVs["n_zero_Si"][i]
                    nVs_all_Sis = dVs["n_free_Si"][i]

                    d_ord = nV_0_Si - nVs_0_Sis
                    d_dim = dim_Si - dV["h0_dP"] + dV["h0"] - dVs["h0"]
                    leak_i = nVs_all_Sis - nVs_0_Sis

                    # Control C3b: n(V | 0, S_i) - n(V* | all, S*_i) == d_dim  <=>  d_ord == d_dim + leak_i
                    if (nV_0_Si - nVs_all_Sis) != d_dim or d_ord != (d_dim + leak_i):
                        c3b_fails += 1

                    d_ord_hist[d_ord] += 1
                    leak_hist[leak_i] += 1
                    if d_ord != 0 and leak_i == 0:
                        d_ord_nonzero_no_leak += 1

                    # Plant P1_C8: V in place of V* in C3b
                    nV_all_Si = dV["n_free_Si"][i]
                    if (nV_0_Si - nV_all_Si) != (dim_Si - dV["h0_dP"]):
                        p1_c8_fails += 1

                    # Plant P2_C8: non-canonical line in place of S*_i in C3b
                    if (nV_0_Si - dVs["n_free_rand"][i]) != d_dim:
                        p2_c8_fails += 1

                    if i in dV["split_I2_D"]:
                        split_I2_count += 1
                        split_I2_D_hist[dV["split_I2_D"][i]] += 1
                    if i in dV["split_eigen_D"]:
                        split_eigen_count += 1
                        split_eigen_D_hist[dV["split_eigen_D"][i]] += 1

    return {
        "name": name,
        "cusps": c,
        "N": N,
        "K_chars": K,
        "prime_p": p,
        "h1_ell_hist": {str(k): v for k, v in sorted(h1_ell_hist.items())},
        "all_h1_ell_le_1": all(k <= 1 for k in h1_ell_hist.keys()),
        "n_modules": n_modules,
        "n_joins_total": n_joins_total,
        "n_joins_vacuous": n_joins_vacuous,
        "n_joins_nonvac": n_joins_nonvac,
        "index_hist": {str(k): v for k, v in sorted(index_hist.items())},
        "max_abs_I": max((abs(k) for k in index_hist.keys()), default=0),
        "d_ord_hist": {str(k): v for k, v in sorted(d_ord_hist.items())},
        "leak_hist": {str(k): v for k, v in sorted(leak_hist.items())},
        "has_positive_leak": any(k > 0 and v > 0 for k, v in leak_hist.items()),
        "d_ord_nonzero_no_leak": d_ord_nonzero_no_leak,
        "split_I2_count": split_I2_count,
        "split_I2_D_hist": {str(k): v for k, v in sorted(split_I2_D_hist.items())},
        "split_eigen_count": split_eigen_count,
        "split_eigen_D_hist": {str(k): v for k, v in sorted(split_eigen_D_hist.items())},
        "c1_fails": c1_fails,
        "c2_fails": c2_fails,
        "c3a_fails": c3a_fails,
        "c3b_fails": c3b_fails,
        "s_perp_fails": s_perp_fails,
        "b1438_form_fails": b1438_form_fails,
        "p1_c8_fails": p1_c8_fails,
        "p2_c8_fails": p2_c8_fails,
        "p3_c8_fails": p3_c8_fails,
        "witnesses_absI2": witnesses_absI2,
        "sampled_records": sampled_records,
    }


def verify_single_module_at_second_prime(
    pres: Dict[str, Any],
    N: int,
    e_ell: Tuple[int, ...],
    e_alpha: Tuple[int, ...],
    z_p1: List[int],
    p1: int,
    p2: int,
) -> Optional[int]:
    """
    When h^1(P; ell) == 1, recompute I(V) = n(V) - n(V*) independently at second prime p2!
    (When h^1(P; ell) == 1, the unique non-split ray [z] in P(H^1(P; ell)) is canonical and
    independent of the prime p!)
    Returns I(V) at p2 if h^1(P; ell) == 1 at p2, else recomputes over a basis of H^1(P; ell) at p2
    and returns max |I| seen.
    """
    m = pres["m"]
    r = pres["r"]
    rel_words = pres["rel_words"]
    per_words = pres["per_words"]
    zeta2 = primitive_nth_root_mod_p(N, p2)
    e_beta = tuple((e_alpha[k] - e_ell[k]) % N for k in range(m))
    e_alpha_s = tuple((e_ell[k] - e_alpha[k]) % N for k in range(m))
    e_beta_s = tuple((-e_alpha[k]) % N for k in range(m))

    ell_v = [pow(zeta2, ek, p2) for ek in e_ell]
    ell_inv = [pow(zeta2, (-ek) % N, p2) for ek in e_ell]
    J1_rel: List[List[int]] = []
    for rw in rel_words:
        cur = 1
        row = [0] * m
        for tok in rw:
            if tok > 0:
                k = tok - 1
                row[k] = (row[k] + cur) % p2
                cur = (cur * ell_v[k]) % p2
            else:
                k = -tok - 1
                cur = (cur * ell_inv[k]) % p2
                row[k] = (row[k] - cur) % p2
        J1_rel.append(row)
    Z1 = nullspace_mod_p(J1_rel, m, p2)
    v_cob = [(ell_v[k] - 1) % p2 for k in range(m)]
    cur_span = [v_cob]
    H1_b: List[List[int]] = []
    for u in Z1:
        if rank_mod_p(cur_span + [u], m, p2) > len(cur_span):
            cur_span.append(u)
            H1_b.append(u)
    assert len(H1_b) >= 1

    def eval_I(z2: List[int]) -> int:
        av = [pow(zeta2, ek, p2) for ek in e_alpha]
        bv = [pow(zeta2, ek, p2) for ek in e_beta]
        asv = [pow(zeta2, ek, p2) for ek in e_alpha_s]
        bsv = [pow(zeta2, ek, p2) for ek in e_beta_s]
        mats_V = [(av[k], (z2[k] * bv[k]) % p2, 0, bv[k]) for k in range(m)]
        mats_Vs = [(asv[k], (z2[k] * bsv[k]) % p2, 0, bsv[k]) for k in range(m)]
        dV = direct_2x2_cohomology_mod_p(m, rel_words, per_words, mats_V, p2)
        dVs = direct_2x2_cohomology_mod_p(m, rel_words, per_words, mats_Vs, p2)
        assert dV["n_int"] - dVs["n_int"] == dVs["h1"] - dV["h1"]
        return dV["n_int"] - dVs["n_int"]

    if len(H1_b) == 1:
        return eval_I(H1_b[0])
    # Try basis + 2 combinations at p2
    cands = list(H1_b) + [
        [sum(H1_b[q][k] for q in range(len(H1_b))) % p2 for k in range(m)],
        [sum((q + 1) * H1_b[q][k] for q in range(len(H1_b))) % p2 for k in range(m)],
    ]
    vals = [eval_I(z2) for z2 in cands]
    return max(vals, key=lambda x: abs(x))


def run_part1_sm_c8() -> Dict[str, Any]:
    t0 = time.time()
    pop = build_b1441_population()
    cusp_dist_74 = Counter(M.num_cusps() for _, M in pop)
    assert dict(cusp_dist_74) == {2: 54, 3: 15, 4: 3, 5: 1, 6: 1}

    skipped_entries: List[Dict[str, Any]] = []
    entry_summaries: List[Dict[str, Any]] = []

    tot_modules = 0
    tot_joins = 0
    tot_vacuous = 0
    tot_nonvac = 0
    tot_d_ord = Counter()
    tot_leak = Counter()
    tot_d_ord_no_leak = 0
    tot_I_hist = Counter()
    tot_split_I2 = 0
    tot_split_I2_D = Counter()
    tot_split_eigen = 0
    tot_split_eigen_D = Counter()

    tot_c1_fails = 0
    tot_c2_fails = 0
    tot_c3a_fails = 0
    tot_c3b_fails = 0
    tot_sperp_fails = 0
    tot_b1438_fails = 0
    tot_p1_fails = 0
    tot_p2_fails = 0
    tot_p3_fails = 0

    entries_with_leak = 0
    entries_with_leak_excl_m129_m125 = 0
    tot_leak_nonzero_excl_m129_m125 = 0
    carriers_absI2: List[str] = []
    carriers_absI2_all_leak = True
    entries_h1_line_only = 0
    second_prime_absI2_checked = 0
    second_prime_absI2_confirmed = 0
    second_prime_h1line_mismatches = 0

    for entry_idx, (name, M) in enumerate(pop):
        pres = extract_presentation_data(M)
        N = max(pres["torsion_exponent"], 2)
        K = count_characters_mod_N(pres, N)
        if K > 600:
            skipped_entries.append({"name": name, "cusps": pres["c"], "N": N, "K_chars": K})
            continue
        chars = enumerate_characters_mod_N(pres, N)
        primes = find_primes_1_mod_N(N, count=2, start=100_003)
        p1, p2 = primes[0], primes[1]

        res = evaluate_sm_c8_entry_at_prime(entry_idx, name, pres, N, chars, p1, run_direct_crosscheck=True)

        # Second-prime cross-check on all |I| >= 2 witnesses (or per-carrier representative set) & line-only entries
        if res["max_abs_I"] >= 2:
            carriers_absI2.append(name)
            if not res["has_positive_leak"]:
                carriers_absI2_all_leak = False
            # Verify witnesses at p2
            seen_pairs: Set[Tuple[int, int]] = set()
            max_I_p2 = 0
            for ell, alpha, z_vec, idx_p1 in res["witnesses_absI2"]:
                if (ell, alpha) in seen_pairs and len(seen_pairs) >= 12:
                    continue
                seen_pairs.add((ell, alpha))
                idx_p2 = verify_single_module_at_second_prime(
                    pres, N, chars[ell], chars[alpha], z_vec, p1, p2
                )
                assert idx_p2 is not None
                second_prime_absI2_checked += 1
                max_I_p2 = max(max_I_p2, abs(idx_p2))
            if max_I_p2 >= 2:
                second_prime_absI2_confirmed += 1

        if res["all_h1_ell_le_1"]:
            entries_h1_line_only += 1
            for ell, alpha, z_vec, _, _, idx_p1 in res["sampled_records"]:
                idx_p2 = verify_single_module_at_second_prime(
                    pres, N, chars[ell], chars[alpha], z_vec, p1, p2
                )
                if idx_p2 != idx_p1:
                    second_prime_h1line_mismatches += 1

        tot_modules += res["n_modules"]
        tot_joins += res["n_joins_total"]
        tot_vacuous += res["n_joins_vacuous"]
        tot_nonvac += res["n_joins_nonvac"]
        for k_s, v in res["d_ord_hist"].items():
            tot_d_ord[int(k_s)] += v
        for k_s, v in res["leak_hist"].items():
            tot_leak[int(k_s)] += v
        tot_d_ord_no_leak += res["d_ord_nonzero_no_leak"]
        for k_s, v in res["index_hist"].items():
            tot_I_hist[int(k_s)] += v
        tot_split_I2 += res["split_I2_count"]
        for k_s, v in res["split_I2_D_hist"].items():
            tot_split_I2_D[int(k_s)] += v
        tot_split_eigen += res["split_eigen_count"]
        for k_s, v in res["split_eigen_D_hist"].items():
            tot_split_eigen_D[int(k_s)] += v

        tot_c1_fails += res["c1_fails"]
        tot_c2_fails += res["c2_fails"]
        tot_c3a_fails += res["c3a_fails"]
        tot_c3b_fails += res["c3b_fails"]
        tot_sperp_fails += res["s_perp_fails"]
        tot_b1438_fails += res["b1438_form_fails"]
        tot_p1_fails += res["p1_c8_fails"]
        tot_p2_fails += res["p2_c8_fails"]
        tot_p3_fails += res["p3_c8_fails"]

        if res["has_positive_leak"]:
            entries_with_leak += 1
            if name not in ("m129", "m125"):
                entries_with_leak_excl_m129_m125 += 1
        if name not in ("m129", "m125"):
            tot_leak_nonzero_excl_m129_m125 += sum(
                v for k_s, v in res["leak_hist"].items() if int(k_s) > 0
            )

        # Strip raw cocycle arrays before saving compact summary
        res_clean = {k: v for k, v in res.items() if k not in ("witnesses_absI2", "sampled_records")}
        res_clean["n_absI2_modules"] = len(res["witnesses_absI2"])
        entry_summaries.append(res_clean)

    tot_leak_nonzero = sum(v for k, v in tot_leak.items() if k > 0)
    tot_d_ord_nonzero = sum(v for k, v in tot_d_ord.items() if k != 0)
    d_ord_symmetric = all(tot_d_ord[k] == tot_d_ord[-k] for k in tot_d_ord.keys())
    d_ord_sum = sum(k * v for k, v in tot_d_ord.items())

    # Root-group breakdown of |I|=2 carriers
    carriers_by_root = Counter()
    for cname in carriers_absI2:
        root_tag = cname.split("_")[0]
        carriers_by_root[root_tag] += 1

    assert tot_c1_fails == 0 and tot_c2_fails == 0 and tot_c3a_fails == 0 and tot_c3b_fails == 0
    assert tot_sperp_fails == 0 and tot_b1438_fails == 0
    assert tot_p1_fails > 0 and tot_p2_fails > 0 and tot_p3_fails > 0

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "total_population_manifolds": len(pop),
        "cusp_distribution_74": {str(k): v for k, v in sorted(cusp_dist_74.items())},
        "active_entries": len(entry_summaries),
        "skipped_entries_count": len(skipped_entries),
        "skipped_entries": skipped_entries,
        "total_modules": tot_modules,
        "total_joins": tot_joins,
        "vacuous_joins": tot_vacuous,
        "non_vacuous_joins": tot_nonvac,
        "controls_all_zero_failures": {
            "C1_fails": tot_c1_fails,
            "C2_fails": tot_c2_fails,
            "C3a_fails": tot_c3a_fails,
            "C3b_fails": tot_c3b_fails,
            "S_perp_fails": tot_sperp_fails,
            "B1438_index_form_fails": tot_b1438_fails,
        },
        "d_ord_nonzero_joins": tot_d_ord_nonzero,
        "d_ord_hist": {str(k): v for k, v in sorted(tot_d_ord.items())},
        "d_ord_pm_symmetric": d_ord_symmetric,
        "d_ord_signed_sum": d_ord_sum,
        "leak_nonzero_joins": tot_leak_nonzero,
        "leak_nonzero_joins_excl_m129_m125": tot_leak_nonzero_excl_m129_m125,
        "leak_hist": {str(k): v for k, v in sorted(tot_leak.items())},
        "d_ord_nonzero_no_leak_joins": tot_d_ord_no_leak,
        "entries_with_positive_leak": entries_with_leak,
        "entries_with_positive_leak_excl_m129_m125": entries_with_leak_excl_m129_m125,
        "index_I_hist_all_modules": {str(k): v for k, v in sorted(tot_I_hist.items())},
        "carriers_absI2_count": len(carriers_absI2),
        "carriers_absI2": carriers_absI2,
        "carriers_absI2_by_root": dict(carriers_by_root),
        "carriers_absI2_all_have_leak": carriers_absI2_all_leak,
        "entries_all_h1_ell_le_1_count": entries_h1_line_only,
        "second_prime_absI2_pairs_checked": second_prime_absI2_checked,
        "second_prime_absI2_carriers_confirmed": second_prime_absI2_confirmed,
        "second_prime_h1_line_mismatches": second_prime_h1line_mismatches,
        "split_I2_joins": tot_split_I2,
        "split_I2_D_hist": {str(k): v for k, v in sorted(tot_split_I2_D.items())},
        "split_eigen_joins": tot_split_eigen,
        "split_eigen_D_hist": {str(k): v for k, v in sorted(tot_split_eigen_D.items())},
        "plants": {
            "P1_C8_V_for_Vstar_fails": tot_p1_fails,
            "P2_C8_random_line_fails": tot_p2_fails,
            "P3_C8_untwisted_half_dim_fails": tot_p3_fails,
        },
        "per_entry_summaries": entry_summaries,
    }


# ============================================================================
# PART 2: SM-C10 — TWISTED DUALITY ON THE TICK FAMILY M_1 .. M_6
# ============================================================================

def free_reduce(word: Sequence[int]) -> List[int]:
    out: List[int] = []
    for tok in word:
        if out and out[-1] == -tok:
            out.pop()
        else:
            out.append(tok)
    return out


def free_inv(word: Sequence[int]) -> List[int]:
    return [-tok for tok in reversed(word)]


def tick_phi_power(n: int) -> Tuple[List[int], List[int]]:
    """
    Tick automorphism phi(x) = y x, phi(y) = x on F_2 = <x=1, y=2>, iterated n times.
    Returns (phi^n(x), phi^n(y)) as reduced words in {+-1, +-2}.
    """
    wx = [1]
    wy = [2]
    for _ in range(n):
        inv_x = free_inv(wx)
        inv_y = free_inv(wy)
        # Substitute x -> y x = [2, 1], y -> x = [1] inside current words?
        # Wait: phi(w) applies phi to each generator in w! Let's check:
        # At n=1: wx = [1] -> phi(x) = [2, 1]; wy = [2] -> phi(y) = [1].
        # At n=2: phi([2, 1]) = phi(y) phi(x) = [1, 2, 1]; phi([1]) = [2, 1]!
        # Check commutator [x, y] = x y x^-1 y^-1 = [1, 2, -1, -2]:
        #   n=1: [2, 1] + [1] + [-1, -2] + [-1] = [2, 1, -2, -1] = [x, y]^-1!
        #   n=2: [1, 2, 1] + [2, 1] + [-1, -2, -1] + [-1, -2] = [1, 2, -1, -2] = [x, y]!
        new_wx: List[int] = []
        for tok in wx:
            if tok == 1:
                new_wx.extend([2, 1])
            elif tok == -1:
                new_wx.extend([-1, -2])
            elif tok == 2:
                new_wx.append(1)
            elif tok == -2:
                new_wx.append(-1)
        new_wy: List[int] = []
        for tok in wy:
            if tok == 1:
                new_wy.extend([2, 1])
            elif tok == -1:
                new_wy.extend([-1, -2])
            elif tok == 2:
                new_wy.append(1)
            elif tok == -2:
                new_wy.append(-1)
        wx = free_reduce(new_wx)
        wy = free_reduce(new_wy)
    return wx, wy


def build_tick_presentation(n: int) -> Tuple[List[List[int]], List[Tuple[List[int], List[int]]], List[int]]:
    """
    Presentation of M_n = <x=1, y=2, t=3 | t x t^-1 phi^n(x)^-1 = 1, t y t^-1 phi^n(y)^-1 = 1>,
    with peripheral generators (t = [3], lambda = [x, y] = [1, 2, -1, -2]).
    """
    px, py = tick_phi_power(n)
    # Verify phi^n([x, y]) == [x, y]^((-1)^n) in F_2!
    comm_img = free_reduce(px + py + free_inv(px) + free_inv(py))
    expected_comm = [1, 2, -1, -2] if (n % 2 == 0) else [2, 1, -2, -1]
    assert comm_img == expected_comm, f"Commutator check failed at n={n}: {comm_img} != {expected_comm}"

    r1 = free_reduce([3, 1, -3] + free_inv(px))
    r2 = free_reduce([3, 2, -3] + free_inv(py))
    per = [([3], [1, 2, -1, -2])]
    return [r1, r2], per, comm_img


def enumerate_tick_characters_union(
    n: int, N_orders: Sequence[int]
) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Enumerate all characters chi = (e_x, e_y, e_t) in (Z/N_lcm Z)^3 of H_1(M_n)
    whose order divides AT LEAST ONE N in N_orders, represented over N_lcm = lcm(2, *N_orders)
    (including 2 so orientation character w = (0, 0, N_lcm//2) always lives in the same ambient group!).
    """
    N_amb = lcm_list([2] + list(N_orders))
    # Abelianized J = [[1, 1], [1, 0]] on row (e_x, e_y):
    # phi(x) = y x => chi(phi(x)) = e_x + e_y; phi(y) = x => chi(phi(y)) = e_x!
    J = np.array([[1, 1], [1, 0]], dtype=np.int64)
    Jn = np.linalg.matrix_power(J, n)
    d00, d01 = int(Jn[0, 0] - 1), int(Jn[0, 1])
    d10, d11 = int(Jn[1, 0]), int(Jn[1, 1] - 1)

    valid_set: Set[Tuple[int, int, int]] = set()
    for N_sub in N_orders:
        scale = N_amb // N_sub
        for ax in range(N_sub):
            for ay in range(N_sub):
                if (ax * d00 + ay * d10) % N_sub == 0 and (ax * d01 + ay * d11) % N_sub == 0:
                    for at in range(N_sub):
                        valid_set.add(((ax * scale) % N_amb, (ay * scale) % N_amb, (at * scale) % N_amb))
    chars = sorted(valid_set, key=lambda t: (0 if t == (0, 0, 0) else 1, t))
    return N_amb, chars


def evaluate_tick_family_modules_mod_p(
    n: int,
    N_amb: int,
    allowed_pairs: List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]],
    p: int,
    include_unipotent: bool = False,
    wrong_chi2: Optional[Tuple[int, int, int]] = None,
) -> Dict[str, Any]:
    """
    Exact F_p Fox-calculus evaluation of K1, K2, K4, g_w, g_0, interior class index n(V) - n(V* tensor w),
    and planted faults P4_C10, P5_C10, P6_C10 on M_n (and double cover M_{2n} when n is odd).
    """
    rel_n, per_n, _ = build_tick_presentation(n)
    is_odd = (n % 2 == 1)
    if is_odd:
        rel_2n, per_2n, _ = build_tick_presentation(2 * n)
    else:
        rel_2n, per_2n = [], []

    zeta = primitive_nth_root_mod_p(N_amb, p)
    half_N = N_amb // 2
    w_char = (0, 0, half_N) if is_odd else (0, 0, 0)

    # Group pairs by ell = (alpha - beta) mod N_amb
    pairs_by_ell: Dict[Tuple[int, int, int], List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]] = defaultdict(list)
    for alpha, beta in allowed_pairs:
        if not include_unipotent and alpha == beta:
            continue
        ell = tuple((alpha[k] - beta[k]) % N_amb for k in range(3))  # type: ignore[assignment]
        pairs_by_ell[ell].append((alpha, beta))

    n_modules = 0
    n_record_like = 0
    k1_fails = 0
    k2_fails = 0
    k4_fails = 0
    gw_neq_g0 = 0
    gw_hist = Counter()
    g0_hist = Counter()
    int_index_hist = Counter()
    ell_t_values = Counter()
    c_lambda_nonzero = 0

    p4_untwisted_fails = 0
    p5_wrong_twist_fails = 0
    p6_unweighted_transfer_fails = 0

    for ell, ab_list in sorted(pairs_by_ell.items()):
        # Compute H^1(M_n; ell)
        ell_v = [pow(zeta, ek, p) for ek in ell]
        ell_inv = [pow(zeta, (-ek) % N_amb, p) for ek in ell]
        J1_rel: List[List[int]] = []
        for rw in rel_n:
            cur = 1
            row = [0, 0, 0]
            for tok in rw:
                if tok > 0:
                    k = tok - 1
                    row[k] = (row[k] + cur) % p
                    cur = (cur * ell_v[k]) % p
                else:
                    k = -tok - 1
                    cur = (cur * ell_inv[k]) % p
                    row[k] = (row[k] - cur) % p
            assert cur == 1
            J1_rel.append(row)
        Z1 = nullspace_mod_p(J1_rel, 3, p)
        v_cob = [(ell_v[k] - 1) % p for k in range(3)]
        if any(x != 0 for x in v_cob):
            cur_span = [v_cob]
            H1_b: List[List[int]] = []
            for u in Z1:
                if rank_mod_p(cur_span + [u], 3, p) > len(cur_span):
                    cur_span.append(u)
                    H1_b.append(u)
        else:
            # ell == (0, 0, 0): unipotent case! B^1 = 0, H^1 = Z^1
            H1_b = Z1

        if not H1_b:
            continue
        assert len(H1_b) == 1, f"Expected h^1(M_{n}; ell) <= 1, got {len(H1_b)} at ell={ell}"
        z_vec = H1_b[0]

        # Evaluate z(lambda) where lambda = [1, 2, -1, -2]
        cur_e = 1
        cur_z = 0
        for tok in [1, 2, -1, -2]:
            if tok > 0:
                k = tok - 1
                cur_z = (cur_z + cur_e * z_vec[k]) % p
                cur_e = (cur_e * ell_v[k]) % p
            else:
                k = -tok - 1
                inv_e = ell_inv[k]
                cur_z = (cur_z - ((cur_e * inv_e) % p) * z_vec[k]) % p
                cur_e = (cur_e * inv_e) % p

        for alpha, beta in ab_list:
            n_modules += 1
            if alpha[2] == 0 and beta[2] == 0:
                n_record_like += 1
            ell_t_sign = 1 if ell[2] == 0 else (-1 if ell[2] == half_N else 999)
            ell_t_values[ell_t_sign] += 1
            if cur_z != 0:
                c_lambda_nonzero += 1

            av = [pow(zeta, ek, p) for ek in alpha]
            bv = [pow(zeta, ek, p) for ek in beta]
            wv = [pow(zeta, ek, p) for ek in w_char]

            mats_V = [(av[k], (z_vec[k] * bv[k]) % p, 0, bv[k]) for k in range(3)]
            # Contragredient V* = rho_V^{-T} directly!
            mats_Vs = []
            for G in mats_V:
                invG = mat2_inv_p(G, p)
                mats_Vs.append((invG[0], invG[2], invG[1], invG[3]))
            mats_Vw = [((G[0] * wv[k]) % p, (G[1] * wv[k]) % p, (G[2] * wv[k]) % p, (G[3] * wv[k]) % p) for k, G in enumerate(mats_V)]
            mats_Vsw = [((G[0] * wv[k]) % p, (G[1] * wv[k]) % p, (G[2] * wv[k]) % p, (G[3] * wv[k]) % p) for k, G in enumerate(mats_Vs)]

            dV = direct_2x2_cohomology_mod_p(3, rel_n, per_n, mats_V, p, klein_bottle_cusp=is_odd)
            dVs = direct_2x2_cohomology_mod_p(3, rel_n, per_n, mats_Vs, p, klein_bottle_cusp=is_odd)
            dVsw = direct_2x2_cohomology_mod_p(3, rel_n, per_n, mats_Vsw, p, klein_bottle_cusp=is_odd)

            # K1: dim A_V + dim A_(V* tensor w) == h^1(dM_n; V)
            if dV["dim_A"] + dVsw["dim_A"] != dV["h1_per"]:
                k1_fails += 1
            # K2: [h1(V*w) - h0(V*w)] - [h1(V) - h0(V)] == dim A_(V*w) - h0(dM_n; V*w)
            if ((dVsw["h1"] - dVsw["h0"]) - (dV["h1"] - dV["h0"])) != (dVsw["dim_A"] - dVsw["h0_per"]):
                k2_fails += 1

            gw = dVsw["h1"] - dV["h1"]
            g0 = dVs["h1"] - dV["h1"]
            gw_hist[gw] += 1
            g0_hist[g0] += 1
            if gw != g0:
                gw_neq_g0 += 1
            int_index_hist[dV["n_int"] - dVsw["n_int"]] += 1

            # Plant P4_C10: untwisted V* in place of V* tensor w in K1 or K2
            p4_bad_k1 = (dV["dim_A"] + dVs["dim_A"] != dV["h1_per"])
            p4_bad_k2 = (((dVs["h1"] - dVs["h0"]) - (dV["h1"] - dV["h0"])) != (dVs["dim_A"] - dVs["h0_per"]))
            if p4_bad_k1 or p4_bad_k2:
                p4_untwisted_fails += 1

            # Plant P5_C10: wrong order-2 twist w' = w * chi2
            if wrong_chi2 is not None:
                w_bad = [pow(zeta, (w_char[k] + wrong_chi2[k]) % N_amb, p) for k in range(3)]
                mats_Vs_bad = [
                    ((G[0] * w_bad[k]) % p, (G[1] * w_bad[k]) % p, (G[2] * w_bad[k]) % p, (G[3] * w_bad[k]) % p)
                    for k, G in enumerate(mats_Vs)
                ]
                dVs_bad = direct_2x2_cohomology_mod_p(3, rel_n, per_n, mats_Vs_bad, p, klein_bottle_cusp=is_odd)
                bad1 = (dV["dim_A"] + dVs_bad["dim_A"] != dV["h1_per"])
                bad2 = (((dVs_bad["h1"] - dVs_bad["h0"]) - (dV["h1"] - dV["h0"])) != (dVs_bad["dim_A"] - dVs_bad["h0_per"]))
                if bad1 or bad2:
                    p5_wrong_twist_fails += 1

            # K4 & Plant P6_C10 on odd n: transfer to orientation double cover M_{2n}
            if is_odd:
                dVw = direct_2x2_cohomology_mod_p(3, rel_n, per_n, mats_Vw, p, klein_bottle_cusp=True)
                t_sq = mat2_mul_p(mats_V[2], mats_V[2], p)
                mats_2n = [mats_V[0], mats_V[1], t_sq]
                d2n = direct_2x2_cohomology_mod_p(3, rel_2n, per_2n, mats_2n, p, klein_bottle_cusp=False)
                if dV["h1"] + dVw["h1"] != d2n["h1"]:
                    k4_fails += 1
                if 2 * dV["h1"] != d2n["h1"]:
                    p6_unweighted_transfer_fails += 1

    return {
        "n": n,
        "prime_p": p,
        "n_modules": n_modules,
        "n_record_like": n_record_like,
        "k1_fails": k1_fails,
        "k2_fails": k2_fails,
        "k4_fails": k4_fails,
        "gw_neq_g0": gw_neq_g0,
        "gw_hist": {str(k): v for k, v in sorted(gw_hist.items())},
        "g0_hist": {str(k): v for k, v in sorted(g0_hist.items())},
        "interior_twisted_index_hist": {str(k): v for k, v in sorted(int_index_hist.items())},
        "ell_t_values": {str(k): v for k, v in sorted(ell_t_values.items())},
        "c_lambda_nonzero": c_lambda_nonzero,
        "p4_untwisted_fails": p4_untwisted_fails,
        "p5_wrong_twist_fails": p5_wrong_twist_fails,
        "p6_unweighted_transfer_fails": p6_unweighted_transfer_fails,
    }


def mp_rank(A_rows: List[List[mp.mpc]], tol: float = 1e-35) -> int:
    """55-digit mpmath Gaussian elimination rank with partial pivoting."""
    if not A_rows or not A_rows[0]:
        return 0
    M = [[mp.mpc(x) for x in r] for r in A_rows]
    nrows = len(M)
    ncols = len(M[0])
    r_piv = 0
    thresh = mp.mpf(tol)
    for c in range(ncols):
        if r_piv >= nrows:
            break
        best_r = max(range(r_piv, nrows), key=lambda r: abs(M[r][c]))
        if abs(M[best_r][c]) <= thresh:
            continue
        if best_r != r_piv:
            M[r_piv], M[best_r] = M[best_r], M[r_piv]
        piv_val = M[r_piv][c]
        for r in range(r_piv + 1, nrows):
            if abs(M[r][c]) > thresh:
                fac = M[r][c] / piv_val
                M[r][c] = mp.mpc(0)
                for j in range(c + 1, ncols):
                    M[r][j] -= fac * M[r_piv][j]
        r_piv += 1
    return r_piv


def evaluate_su2_common_point_family() -> Dict[str, Any]:
    """
    55-digit mpmath Fox cohomology of the common-point SU(2) x mu_d family on M_1..M_6:
      x -> i, y -> j, g = (1 + i + j - k)/2 in SU(2) carrying phi(x)=yx, phi(y)=x,
      across all 46 roots of unity c of order dividing d in {1, ..., 12}.
    Evaluates BOTH parameterizations:
      (A) literal t -> c * g^n;
      (B) power t -> (c * g)^n = c^n * g^n.
    """
    I_m = mp.matrix([[1, 0], [0, 1]])
    q_i = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]])
    q_j = mp.matrix([[0, 1], [-1, 0]])
    q_k = q_i * q_j
    g_su2 = (I_m + q_i + q_j - q_k) / 2
    inv_g = (I_m - q_i - q_j + q_k) / 2
    assert mp.norm(g_su2 * q_i * inv_g - (-q_k)) < mp.mpf("1e-48")
    assert mp.norm(g_su2 * q_j * inv_g - q_i) < mp.mpf("1e-48")

    # Enumerate all 46 distinct roots of unity of order d in 1..12 as exact fractions k/d in [0, 1)
    root_fracs: Set[Fraction] = set()
    for d in range(1, 13):
        for k in range(d):
            root_fracs.add(Fraction(k, d))
    sorted_fracs = sorted(root_fracs)
    assert len(sorted_fracs) == 46

    def fox_mp_2x2(n: int, mats: List[mp.matrix]) -> Dict[str, int]:
        rel_n, per_n, _ = build_tick_presentation(n)
        is_odd = (n % 2 == 1)
        invs = [mp.inverse(G) for G in mats]

        def walk_w(w: List[int]) -> Tuple[mp.matrix, List[List[mp.mpc]]]:
            P = mp.matrix([[1, 0], [0, 1]])
            J = [[mp.mpc(0)] * 6 for _ in range(2)]
            for tok in w:
                if tok > 0:
                    k = tok - 1
                    eff = P
                    P = P * mats[k]
                    J[0][k] += eff[0, 0]
                    J[0][3 + k] += eff[0, 1]
                    J[1][k] += eff[1, 0]
                    J[1][3 + k] += eff[1, 1]
                else:
                    k = -tok - 1
                    P = P * invs[k]
                    eff = P
                    J[0][k] -= eff[0, 0]
                    J[0][3 + k] -= eff[0, 1]
                    J[1][k] -= eff[1, 0]
                    J[1][3 + k] -= eff[1, 1]
            return P, J

        J_rel: List[List[mp.mpc]] = []
        for rw in rel_n:
            hol, Jr = walk_w(rw)
            assert mp.norm(hol - I_m) < mp.mpf("1e-45")
            J_rel.extend(Jr)
        d0_rows = [
            [mats[0][0, 0] - 1, mats[1][0, 0] - 1, mats[2][0, 0] - 1, mats[0][1, 0], mats[1][1, 0], mats[2][1, 0]],
            [mats[0][0, 1], mats[1][0, 1], mats[2][0, 1], mats[0][1, 1] - 1, mats[1][1, 1] - 1, mats[2][1, 1] - 1],
        ]
        for r_i in range(4):
            for c_i in range(2):
                assert abs(sum(J_rel[r_i][q] * d0_rows[c_i][q] for q in range(6))) < mp.mpf("1e-44")
        b_dim = mp_rank(d0_rows)
        z_dim = 6 - mp_rank(J_rel)
        h0 = 2 - b_dim
        h1 = z_dim - b_dim

        mw, lw = per_n[0]
        M_i, _ = walk_w(mw)
        L_i, _ = walk_w(lw)
        d0_per = [
            [M_i[0, 0] - 1, L_i[0, 0] - 1, M_i[1, 0], L_i[1, 0]],
            [M_i[0, 1], L_i[0, 1], M_i[1, 1] - 1, L_i[1, 1] - 1],
        ]
        b_per = mp_rank(d0_per)
        if not is_odd:
            d1_per = [
                [1 - L_i[0, 0], M_i[0, 0] - 1, -L_i[0, 1], M_i[0, 1]],
                [-L_i[1, 0], M_i[1, 0], 1 - L_i[1, 1], M_i[1, 1] - 1],
            ]
        else:
            invL = mp.inverse(L_i)
            d1_per = [
                [1 - invL[0, 0], M_i[0, 0] + invL[0, 0], -invL[0, 1], M_i[0, 1] + invL[0, 1]],
                [-invL[1, 0], M_i[1, 0] + invL[1, 0], 1 - invL[1, 1], M_i[1, 1] + invL[1, 1]],
            ]
        h0_per = 2 - b_per
        h1_per = (4 - mp_rank(d1_per)) - b_per
        return {"h0": h0, "h1": h1, "h0_per": h0_per, "h1_per": h1_per}

    out_c_gn: Dict[str, Any] = {}
    out_cg_pow_n: Dict[str, Any] = {}
    all_per_zero = True
    all_gaps_zero = True

    for n in range(1, 7):
        gn = g_su2 ** n
        is_odd = (n % 2 == 1)
        nonzero_c_gn = []
        nonzero_cg_pow_n = []
        for fr in sorted_fracs:
            theta = 2 * mp.pi * mp.mpf(fr.numerator) / mp.mpf(fr.denominator)
            c_val = mp.expj(theta)
            w_sign = -1 if is_odd else 1

            # Mode A: t -> c * g^n, contragredient V* = rho^{-T} explicitly!
            mats_V = [q_i, q_j, c_val * gn]
            mats_Vs = [mp.inverse(G).T for G in mats_V]
            mats_Vsw = [mats_Vs[0], mats_Vs[1], w_sign * mats_Vs[2]]
            dV = fox_mp_2x2(n, mats_V)
            dVs = fox_mp_2x2(n, mats_Vs)
            dVsw = fox_mp_2x2(n, mats_Vsw)
            if dV["h0_per"] != 0 or dV["h1_per"] != 0 or dVsw["h0_per"] != 0 or dVsw["h1_per"] != 0:
                all_per_zero = False
            if dVsw["h1"] != dV["h1"] or dVs["h1"] != dV["h1"]:
                all_gaps_zero = False
            if dV["h1"] > 0:
                nonzero_c_gn.append({"c_turn": str(fr), "h1_V": dV["h1"], "h1_Vs": dVs["h1"], "h1_Vsw": dVsw["h1"]})

            # Mode B: t -> (c * g)^n = c^n * g^n
            cn = c_val ** n
            mats_Vb = [q_i, q_j, cn * gn]
            mats_Vsb = [mp.inverse(G).T for G in mats_Vb]
            mats_Vswb = [mats_Vsb[0], mats_Vsb[1], w_sign * mats_Vsb[2]]
            dV_b = fox_mp_2x2(n, mats_Vb)
            dVs_b = fox_mp_2x2(n, mats_Vsb)
            dVsw_b = fox_mp_2x2(n, mats_Vswb)
            if dV_b["h0_per"] != 0 or dV_b["h1_per"] != 0:
                all_per_zero = False
            if dVsw_b["h1"] != dV_b["h1"] or dVs_b["h1"] != dV_b["h1"]:
                all_gaps_zero = False
            if dV_b["h1"] > 0:
                nonzero_cg_pow_n.append({"c_turn": str(fr), "h1_V": dV_b["h1"], "h1_Vs": dVs_b["h1"], "h1_Vsw": dVsw_b["h1"]})

        out_c_gn[f"M_{n}"] = nonzero_c_gn
        out_cg_pow_n[f"M_{n}"] = nonzero_cg_pow_n

    return {
        "n_roots_per_n": len(sorted_fracs),
        "all_peripheral_cohomology_zero": all_per_zero,
        "all_gaps_gw_and_g0_zero": all_gaps_zero,
        "nonzero_h1_for_t_eq_c_gn": out_c_gn,
        "nonzero_h1_for_t_eq_cg_pow_n": out_cg_pow_n,
    }


def run_part2_sm_c10() -> Dict[str, Any]:
    t0 = time.time()
    # 1. SnapPy cyclic cover & homology cross-checks on M_1..M_6
    base_m000 = snappy.Manifold("b-+R")
    vol_m000 = float(base_m000.volume())
    expected_names = {1: "m000", 2: "m004", 3: "m025", 4: "m206", 5: "m407", 6: "s961"}
    expected_fibre_orders = {1: 1, 2: 1, 3: 4, 4: 5, 5: 11, 6: 16}

    k3_checks: List[Dict[str, Any]] = []
    for n in range(1, 7):
        covs = base_m000.covers(n, cover_type="cyclic")
        assert len(covs) == 1
        Mn = covs[0]
        target = snappy.Manifold(expected_names[n])
        is_iso = bool(Mn.is_isometric_to(target))
        orient = bool(Mn.is_orientable())
        assert orient == (n % 2 == 0)
        vol_ratio = float(Mn.volume()) / vol_m000
        assert abs(vol_ratio - n) < 1e-9

        # Compare presentation H_1 with SnapPy H_1
        rel_n, _, _ = build_tick_presentation(n)
        M_ab = [[0, 0, 0], [0, 0, 0]]
        for j, rw in enumerate(rel_n):
            for tok in rw:
                if tok > 0:
                    M_ab[j][tok - 1] += 1
                else:
                    M_ab[j][-tok - 1] -= 1
        D_snf, _, _ = smith_nonneg(sp.Matrix(M_ab))
        pres_tors = sorted([int(D_snf[i, i]) for i in range(2) if int(D_snf[i, i]) > 1])
        snappy_tors = sorted([int(x) for x in Mn.homology().elementary_divisors() if int(x) > 1])
        assert pres_tors == snappy_tors
        fibre_ord = 1
        for d in pres_tors:
            fibre_ord *= d
        assert fibre_ord == expected_fibre_orders[n]

        # Orientation double cover check for odd n
        if n % 2 == 1:
            dcov = Mn.orientation_cover()
            M_2n = base_m000.covers(2 * n, cover_type="cyclic")[0]
            orient_cov_ok = bool(dcov.is_isometric_to(M_2n))
            assert orient_cov_ok
        else:
            orient_cov_ok = True

        k3_checks.append({
            "n": n,
            "expected_name": expected_names[n],
            "is_isometric_to_named": is_iso,
            "is_orientable": orient,
            "volume_over_m000": round(vol_ratio, 9),
            "torsion_invariants": pres_tors,
            "fibre_torsion_order": fibre_ord,
            "orientation_double_cover_matches_M_2n": orient_cov_ok,
        })

    # 2. Sealed population (orders dividing N in {2, 3, 4, 5, 6}, alpha != beta) at two independent primes
    sealed_results: Dict[str, Any] = {}
    tot_sealed_modules = 0
    for n in range(1, 7):
        N_amb, chars = enumerate_tick_characters_union(n, [2, 3, 4, 5, 6])
        # Valid pairs (alpha != beta) sharing at least one N in {2..6}
        N_amb_set_by_N: List[Set[Tuple[int, int, int]]] = []
        for N_sub in [2, 3, 4, 5, 6]:
            _, c_sub = enumerate_tick_characters_union(n, [N_sub])
            # Rescale c_sub to N_amb
            N_sub_amb = lcm_list([2, N_sub])
            sc = N_amb // N_sub_amb
            N_amb_set_by_N.append({((c[0] * sc) % N_amb, (c[1] * sc) % N_amb, (c[2] * sc) % N_amb) for c in c_sub})
        pair_set: Set[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = set()
        for cset in N_amb_set_by_N:
            clist = sorted(cset)
            for a in clist:
                for b in clist:
                    if a != b:
                        pair_set.add((a, b))
        pairs = sorted(pair_set)
        primes = find_primes_1_mod_N(N_amb, count=2, start=100_003)
        wrong_chi2 = (N_amb // 2, 0, 0) if n == 3 else None
        r_p1 = evaluate_tick_family_modules_mod_p(n, N_amb, pairs, primes[0], include_unipotent=False, wrong_chi2=wrong_chi2)
        r_p2 = evaluate_tick_family_modules_mod_p(n, N_amb, pairs, primes[1], include_unipotent=False, wrong_chi2=wrong_chi2)
        assert {k: v for k, v in r_p1.items() if k != "prime_p"} == {k: v for k, v in r_p2.items() if k != "prime_p"}
        r_p1["second_prime_p2"] = primes[1]
        r_p1["two_prime_exact_match"] = True
        sealed_results[f"M_{n}_{expected_names[n]}"] = r_p1
        tot_sealed_modules += r_p1["n_modules"]

    # 3. Extended m407 (n = 5) population at N = 22 (distinct-diagonal 2420 + unipotent 242 = 2662)
    N_m407, chars_m407 = enumerate_tick_characters_union(5, [22])
    assert N_m407 == 22 and len(chars_m407) == 242
    pairs_m407_distinct = [(a, b) for a in chars_m407 for b in chars_m407 if a != b]
    pairs_m407_unip = [(a, a) for a in chars_m407]
    primes_22 = find_primes_1_mod_N(22, count=2, start=100_003)

    m407_dist_p1 = evaluate_tick_family_modules_mod_p(5, 22, pairs_m407_distinct, primes_22[0], include_unipotent=False)
    m407_dist_p2 = evaluate_tick_family_modules_mod_p(5, 22, pairs_m407_distinct, primes_22[1], include_unipotent=False)
    assert {k: v for k, v in m407_dist_p1.items() if k != "prime_p"} == {k: v for k, v in m407_dist_p2.items() if k != "prime_p"}

    m407_unip_p1 = evaluate_tick_family_modules_mod_p(5, 22, pairs_m407_unip, primes_22[0], include_unipotent=True)
    m407_unip_p2 = evaluate_tick_family_modules_mod_p(5, 22, pairs_m407_unip, primes_22[1], include_unipotent=True)
    assert {k: v for k, v in m407_unip_p1.items() if k != "prime_p"} == {k: v for k, v in m407_unip_p2.items() if k != "prime_p"}

    # 4. Common-point SU(2) family across all 46 roots of unity (d | 1..12)
    su2_res = evaluate_su2_common_point_family()

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "K3_object_checks": k3_checks,
        "sealed_total_modules": tot_sealed_modules,
        "sealed_by_n": sealed_results,
        "m407_N22_distinct_diagonal": m407_dist_p1,
        "m407_N22_unipotent": m407_unip_p1,
        "su2_common_point_family": su2_res,
        "plants": {
            "P4_C10_m025_untwisted_fails": sealed_results["M_3_m025"]["p4_untwisted_fails"],
            "P4_C10_m407_untwisted_fails": m407_dist_p1["p4_untwisted_fails"],
            "P4_C10_even_n_untwisted_fails": (
                sealed_results["M_4_m206"]["p4_untwisted_fails"] + sealed_results["M_6_s961"]["p4_untwisted_fails"]
            ),
            "P5_C10_m025_wrong_twist_fails": sealed_results["M_3_m025"]["p5_wrong_twist_fails"],
            "P6_C10_m025_unweighted_transfer_fails": sealed_results["M_3_m025"]["p6_unweighted_transfer_fails"],
        },
    }


# ============================================================================
# PART 3: SM-C11 (P-333) — FIVE-ENDED COMPANION o10_150729 & LENGTH-10 CENSUS
# ============================================================================

def is_even_perm(perm: Sequence[int]) -> bool:
    n = len(perm)
    inv_cnt = 0
    for i in range(n):
        pi = perm[i]
        for j in range(i + 1, n):
            if pi > perm[j]:
                inv_cnt += 1
    return (inv_cnt % 2) == 0


def perm_closure(gens: Sequence[Tuple[int, ...]], n: int) -> Set[Tuple[int, ...]]:
    ident = tuple(range(n))
    seen: Set[Tuple[int, ...]] = {ident}
    queue = [ident]
    glist = list(set(gens))
    while queue:
        cur = queue.pop()
        for g in glist:
            nxt = tuple(g[cur[i]] for i in range(n))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def reduce_gl2z_shape_is_hexagonal(z_raw: complex, tol: float = 1e-6) -> Tuple[bool, Tuple[float, float]]:
    """Reduce cusp shape z in C \\ R modulo GL(2, Z) into fundamental domain and test z ~ 1/2 + i sqrt(3)/2."""
    z = complex(z_raw)
    if z.imag < 0:
        z = z.conjugate()
    for _ in range(200):
        n_shift = round(z.real)
        z = z - n_shift
        if abs(z) < 1.0 - 1e-11:
            z = -1.0 / z
        else:
            break
    hex_pos = complex(0.5, 0.5 * math.sqrt(3.0))
    hex_neg = complex(-0.5, 0.5 * math.sqrt(3.0))
    is_hex = min(abs(z - hex_pos), abs(z - hex_neg)) < tol
    return is_hex, (round(z.real, 9), round(z.imag, 9))


def read_fci_from_isometries(
    M: "snappy.Manifold", isos: Sequence[Any], check_shapes: bool = True
) -> Dict[str, Any]:
    c = M.num_cusps()
    total_isos = len(isos)
    orient_pres = 0
    orient_rev = 0
    all_perms: Set[Tuple[int, ...]] = set()
    pos_perms: Set[Tuple[int, ...]] = set()
    cusp_fix_vals = Counter()
    plant_detX_vals = Counter()
    ends_with_three: Set[int] = set()

    for iso in isos:
        imgs = tuple(int(x) for x in iso.cusp_images())
        cmaps = iso.cusp_maps()
        dets = [int(X[0, 0]) * int(X[1, 1]) - int(X[0, 1]) * int(X[1, 0]) for X in cmaps]
        assert len(set(dets)) == 1 and dets[0] in (1, -1)
        det_sign = dets[0]
        all_perms.add(imgs)
        for X in cmaps:
            plant_detX_vals[abs(int(X[0, 0]) * int(X[1, 1]) - int(X[0, 1]) * int(X[1, 0]))] += 1

        if det_sign == 1:
            orient_pres += 1
            pos_perms.add(imgs)
            for j in range(c):
                if imgs[j] == j:
                    Xj = cmaps[j]
                    det_minus_I = (int(Xj[0, 0]) - 1) * (int(Xj[1, 1]) - 1) - int(Xj[0, 1]) * int(Xj[1, 0])
                    val = abs(det_minus_I)
                    cusp_fix_vals[val] += 1
                    if val == 3:
                        ends_with_three.add(j)
        else:
            orient_rev += 1

    # Verify group closure on ends
    if len(all_perms) <= 2000:
        assert perm_closure(list(all_perms), c) == all_perms
        assert perm_closure(list(pos_perms), c) == pos_perms

    orbit_0 = {p[0] for p in all_perms}
    transitive_all = (len(orbit_0) == c)
    transitive_pos = (len({p[0] for p in pos_perms}) == c) if pos_perms else False
    pos_all_even = all(is_even_perm(p) for p in pos_perms)

    hex_flags: List[bool] = []
    reduced_shapes: List[Tuple[float, float]] = []
    if check_shapes:
        for s in M.cusp_info("shape"):
            ih, rz = reduce_gl2z_shape_is_hexagonal(complex(s))
            hex_flags.append(ih)
            reduced_shapes.append(rz)

    return {
        "cusps": c,
        "total_isometries": total_isos,
        "orient_preserving_isometries": orient_pres,
        "orient_reversing_isometries": orient_rev,
        "end_perm_group_order_all": len(all_perms),
        "end_perm_group_order_pos": len(pos_perms),
        "pos_perms_all_even": pos_all_even,
        "transitive_on_ends_all": transitive_all,
        "transitive_on_ends_pos": transitive_pos,
        "cusp_fixing_abs_det_X_minus_I": {str(k): v for k, v in sorted(cusp_fix_vals.items())},
        "ends_with_three": sorted(ends_with_three),
        "has_three_somewhere": len(ends_with_three) > 0,
        "has_three_on_every_end": len(ends_with_three) == c,
        "all_cusps_hexagonal": all(hex_flags) if hex_flags else False,
        "hexagonal_cusp_count": sum(1 for x in hex_flags if x),
        "reduced_cusp_shapes_sample": reduced_shapes[:5],
        "plant_abs_det_X_hist": {str(k): v for k, v in sorted(plant_detX_vals.items())},
    }


def fci_read_two_paths(M: "snappy.Manifold", check_shapes: bool = True) -> Dict[str, Any]:
    """Run BOTH SnapPy isometry paths independently and assert complete agreement."""
    MC = M.copy()
    isos_path1 = None
    for attempt in range(6):
        try:
            isos_path1 = MC.is_isometric_to(MC, return_isometries=True)
            break
        except RuntimeError:
            MC.randomize()
    assert isos_path1 is not None, "is_isometric_to failed after retries"

    MC2 = M.copy()
    isos_path2 = None
    for attempt in range(6):
        try:
            sg = MC2.symmetry_group()
            isos_path2 = sg.isometries()
            break
        except RuntimeError:
            MC2.randomize()
    assert isos_path2 is not None, "symmetry_group().isometries() failed after retries"

    r1 = read_fci_from_isometries(MC, isos_path1, check_shapes=check_shapes)
    r2 = read_fci_from_isometries(MC2, isos_path2, check_shapes=check_shapes)

    for key in (
        "cusps",
        "total_isometries",
        "orient_preserving_isometries",
        "orient_reversing_isometries",
        "end_perm_group_order_all",
        "end_perm_group_order_pos",
        "pos_perms_all_even",
        "transitive_on_ends_all",
        "cusp_fixing_abs_det_X_minus_I",
        "has_three_somewhere",
        "has_three_on_every_end",
    ):
        assert r1[key] == r2[key], f"Two-path mismatch on {key}: {r1[key]} vs {r2[key]}"
    r1["two_path_agreement"] = True
    return r1


def enumerate_word_states_lengths_2_to_10() -> Tuple[List[Tuple[int, str, int]], Dict[int, int]]:
    """
    Enumerate all 232 signed word states of lengths 2..10 (B1454 G4):
      aperiodic strings in {L, R}^L with both letters present, modulo cyclic rotation and {L <-> R} swap,
      paired with signs +1 and -1.
    Returns (list of (sign, canonical_word, trace_phi), counts_by_length).
    """
    states: List[Tuple[int, str, int]] = []
    counts_by_len: Dict[int, int] = {}

    def abel_trace(sign: int, w: str) -> int:
        m00, m01, m10, m11 = 1, 0, 0, 1
        for ch in w:
            if ch == "L":
                m01, m11 = m00 + m01, m10 + m11
            else:
                m00, m10 = m00 + m01, m10 + m11
        if sign < 0:
            m00, m11 = -m00, -m11
        return m00 + m11

    for L in range(2, 11):
        seen_classes: Set[str] = set()
        for bits in itertools.product("LR", repeat=L):
            w = "".join(bits)
            if "L" not in w or "R" not in w:
                continue
            # Check aperiodicity (primitive word)
            is_periodic = False
            for d in range(1, L):
                if L % d == 0 and w == w[:d] * (L // d):
                    is_periodic = True
                    break
            if is_periodic:
                continue
            rots = [w[i:] + w[:i] for i in range(L)]
            swapped = "".join("R" if ch == "L" else "L" for ch in w)
            rots_sw = [swapped[i:] + swapped[:i] for i in range(L)]
            canon = min(rots + rots_sw)
            seen_classes.add(canon)
        sorted_cls = sorted(seen_classes)
        counts_by_len[L] = 2 * len(sorted_cls)
        for w in sorted_cls:
            for sgn in (1, -1):
                states.append((sgn, w, abel_trace(sgn, w)))

    expected_by_len = {2: 2, 3: 2, 4: 4, 5: 6, 6: 10, 7: 18, 8: 32, 9: 56, 10: 102}
    assert counts_by_len == expected_by_len, f"State count mismatch: {counts_by_len}"
    assert len(states) == 232
    return states, counts_by_len


def build_fixed_point_companion(M: "snappy.Manifold", expected_deg: int) -> "snappy.Manifold":
    """
    Construct the canonical fixed-point companion cover of once-punctured torus bundle M
    from the finite abelian quotient Q = H_1(M) / im H_1(dM).
    """
    G = M.fundamental_group()
    gens = list(G.generators())
    gen_to_idx = {g: i for i, g in enumerate(gens)}
    m = len(gens)
    rels = [parse_snappy_word(w, gen_to_idx) for w in G.relators()]
    mer_w, lon_w = G.peripheral_curves()[0]
    all_rel_words = rels + [parse_snappy_word(mer_w, gen_to_idx), parse_snappy_word(lon_w, gen_to_idx)]

    # Build m x len(all_rel_words) integer relation column matrix B
    B = [[0] * len(all_rel_words) for _ in range(m)]
    for j, rw in enumerate(all_rel_words):
        for tok in rw:
            if tok > 0:
                B[tok - 1][j] += 1
            else:
                B[-tok - 1][j] -= 1
    D, U, _ = smith_nonneg(sp.Matrix(B))
    # U * B * V = D => Q = Z^m / im(B) ~= oplus_i Z / D[i,i] Z via x -> (U x) mod diag(D)
    invs = [int(D[i, i]) for i in range(m)]
    assert all(d >= 1 for d in invs), f"Infinite quotient factor in companion: {invs}"
    deg = 1
    for d in invs:
        deg *= d
    assert deg == expected_deg, f"Companion degree {deg} != |2 - tr phi| = {expected_deg}"
    if deg == 1:
        return M.copy()

    active_rows = [(i, invs[i]) for i in range(m) if invs[i] > 1]
    moduli = [d for _, d in active_rows]
    # Image of each generator e_k under U mod moduli
    gen_imgs = [
        tuple(int(U[row_i, k]) % d for row_i, d in active_rows)
        for k in range(m)
    ]
    # Verify all relators + peripheral curves map to 0 in Q
    for j in range(len(all_rel_words)):
        for idx_f, (_, d) in enumerate(active_rows):
            assert sum(B[k][j] * gen_imgs[k][idx_f] for k in range(m)) % d == 0

    elems = list(itertools.product(*(range(d) for d in moduli)))
    assert len(elems) == deg
    elem_to_id = {el: idx for idx, el in enumerate(elems)}

    perms: List[List[int]] = []
    for k in range(m):
        gk = gen_imgs[k]
        perm_k = [
            elem_to_id[tuple((el[a] + gk[a]) % moduli[a] for a in range(len(moduli)))]
            for el in elems
        ]
        perms.append(perm_k)
    assert len(perm_closure([tuple(p) for p in perms], deg)) == deg

    C = M.cover(perms)
    assert C.num_cusps() == expected_deg, f"Companion cusps {C.num_cusps()} != {expected_deg}"
    return C


def run_part3_sm_c11() -> Dict[str, Any]:
    t0 = time.time()
    # Part 1: o10_150729 and control L8a15
    M_o10 = snappy.Manifold("o10_150729")
    M_l10n113 = snappy.Manifold("L10n113")
    assert M_o10.is_isometric_to(M_l10n113)
    res_o10 = fci_read_two_paths(M_o10, check_shapes=True)
    # Confirm A_5 (order 60, all even permutations on 5 elements) and S_5 (order 120 on 5 elements)
    res_o10["pos_action_is_A5"] = (
        res_o10["cusps"] == 5
        and res_o10["end_perm_group_order_pos"] == 60
        and res_o10["pos_perms_all_even"]
    )
    res_o10["full_action_is_S5"] = (
        res_o10["cusps"] == 5 and res_o10["end_perm_group_order_all"] == 120
    )

    # Check m003 companion is isometric to o10_150729, and +LLLR companion is isometric to L8a15
    comp_m003 = build_fixed_point_companion(snappy.Manifold("b--LR"), expected_deg=5)
    assert comp_m003.is_isometric_to(M_o10)

    M_lllr = snappy.Manifold("b++LLLR")
    comp_lllr = build_fixed_point_companion(M_lllr, expected_deg=3)
    M_L8a15 = snappy.Manifold("L8a15")
    assert comp_lllr.is_isometric_to(M_L8a15)
    res_L8a15 = fci_read_two_paths(M_L8a15, check_shapes=True)

    # Plant P8_C11: build +LLLR cover from trivial character group (degree 1) and test |2 - tr phi| = 3 gate
    triv_cov_lllr = M_lllr.cover([[0] for _ in M_lllr.fundamental_group().generators()])
    p8_deg_gate_failed = (triv_cov_lllr.num_cusps() != 3)

    # Part 2: Complete census of all 232 signed word states of lengths 2..10
    states, counts_by_len = enumerate_word_states_lengths_2_to_10()
    census_rows: List[Dict[str, Any]] = []
    companions_with_three: List[str] = []
    all_cusp_fix_values_other = Counter()
    companions_with_two: List[str] = []
    proper_companions_count = 0
    all_deg_and_cusps_match = True
    all_transitive = True
    max_ends = 0

    for sgn, w, tr_phi in states:
        label = ("+" if sgn > 0 else "-") + w
        bcode = ("b++" if sgn > 0 else "b--") + w
        M_st = snappy.Manifold(bcode)
        exp_deg = abs(2 - tr_phi)
        if exp_deg > 1:
            proper_companions_count += 1
        C_st = build_fixed_point_companion(M_st, expected_deg=exp_deg)
        if C_st.num_cusps() != exp_deg:
            all_deg_and_cusps_match = False
        max_ends = max(max_ends, C_st.num_cusps())

        fci = fci_read_two_paths(C_st, check_shapes=(exp_deg <= 12))
        if not fci["transitive_on_ends_all"]:
            all_transitive = False
        if fci["has_three_somewhere"]:
            companions_with_three.append(label)
        vals_dict = {int(k): v for k, v in fci["cusp_fixing_abs_det_X_minus_I"].items()}
        if 2 in vals_dict:
            companions_with_two.append(label)
        if label != "-LR":
            for k, v in vals_dict.items():
                all_cusp_fix_values_other[k] += v

        census_rows.append({
            "state": label,
            "word_length": len(w),
            "trace_phi": tr_phi,
            "ends": C_st.num_cusps(),
            "total_isometries": fci["total_isometries"],
            "orient_preserving_isometries": fci["orient_preserving_isometries"],
            "transitive_on_ends": fci["transitive_on_ends_all"],
            "cusp_fixing_values": fci["cusp_fixing_abs_det_X_minus_I"],
            "has_three": fci["has_three_somewhere"],
        })

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "part1_o10_150729": res_o10,
        "part1_m003_companion_isometric_to_o10_150729": True,
        "part1_LLLR_companion_isometric_to_L8a15": True,
        "part1_control_L8a15": res_L8a15,
        "part2_state_counts_by_length": {str(k): v for k, v in sorted(counts_by_len.items())},
        "part2_total_states": len(states),
        "part2_proper_companions": proper_companions_count,
        "part2_max_ends": max_ends,
        "part2_all_degree_and_cusps_equal_abs_2_minus_tr": all_deg_and_cusps_match,
        "part2_all_isometry_groups_transitive_on_ends": all_transitive,
        "part2_companions_carrying_three": companions_with_three,
        "part2_companions_carrying_two": companions_with_two,
        "part2_cusp_fixing_values_outside_m003": {
            str(k): v for k, v in sorted(all_cusp_fix_values_other.items())
        },
        "plants": {
            "P7_C11_abs_det_X_on_o10_150729": res_o10["plant_abs_det_X_hist"],
            "P7_C11_erased_three": ("3" not in res_o10["plant_abs_det_X_hist"]),
            "P8_C11_trivial_cover_LLLR_cusps": triv_cov_lllr.num_cusps(),
            "P8_C11_degree_gate_fired": p8_deg_gate_failed,
        },
        "census_rows": census_rows,
    }


# ============================================================================
# MAIN ENTRYPOINT
# ============================================================================

def main() -> None:
    t_start = time.time()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "verify_x_sm2_out.json")

    part1 = run_part1_sm_c8()
    part2 = run_part2_sm_c10()
    part3 = run_part3_sm_c11()

    plants_all = {
        "P1_C8_fired": part1["plants"]["P1_C8_V_for_Vstar_fails"] > 0,
        "P2_C8_fired": part1["plants"]["P2_C8_random_line_fails"] > 0,
        "P3_C8_fired": part1["plants"]["P3_C8_untwisted_half_dim_fails"] > 0,
        "P4_C10_fired": (
            part2["plants"]["P4_C10_m025_untwisted_fails"] > 0
            and part2["plants"]["P4_C10_m407_untwisted_fails"] > 0
            and part2["plants"]["P4_C10_even_n_untwisted_fails"] == 0
        ),
        "P5_C10_fired": part2["plants"]["P5_C10_m025_wrong_twist_fails"] > 0,
        "P6_C10_fired": part2["plants"]["P6_C10_m025_unweighted_transfer_fails"] > 0,
        "P7_C11_fired": bool(part3["plants"]["P7_C11_erased_three"]),
        "P8_C11_fired": bool(part3["plants"]["P8_C11_degree_gate_fired"]),
    }
    assert all(plants_all.values()), f"A planted fault control failed to fire: {plants_all}"

    payload = {
        "card": "X-SM2",
        "seat": "agy-exp",
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "planted_controls_summary": plants_all,
        "planted_controls_fired_count": sum(1 for v in plants_all.values() if v),
        "part1_sm_c8": part1,
        "part2_sm_c10": part2,
        "part3_sm_c11": part3,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=_json_default)
        f.write("\n")


if __name__ == "__main__":
    main()
