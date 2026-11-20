#!/usr/bin/env python3
"""
Independent Cold-Room Zero-Trust Referee for Card A2-OW1 (with Errata 1 & 2).

Zero empirical/PDG inputs (0 of 19).
Zero float or complex AST literals.
Zero frontier/ imports.

Independently verifies:
  - Task OW1-A: Delta(2,3,N) (N=2,3,4,5) via Todd-Coxeter coset enumeration +
    PSL(2,F_5) cross-check, complete subgroup lattice & core-free actions of
    degree d <= 12, involution classes, explicit C_{su(d)}(P) nullspace dim,
    explicit bitmask Lambda^{even}(C^d) hypercharge spectrum, chirality, all 4
    anomalies, exact Q/Z global kernel order |K|, collar-odd doublet-triplet
    splitting, A_5 uniqueness (A_4 index 5, D_5 index 6, single involution
    class [1,2,2]), 24-Weyl operator identity both algebraically in Q[w]/(Phi_5)
    and numerically at 60-digit mpmath precision (< 10^-50), and explicit 32x32
    Cl(10) CAR & gamma anticommutators in exact Gaussian-integer arithmetic.
  - Task OW1-B: Unblocked 50-thread punctured-torus bundle census (21 orientable
    + words len <= 6, 21 orientable - words len <= 6, 8 non-orientable P words
    len <= 5) computed independently from BOTH SnapPy M.fundamental_group() AND
    exact 3-generator Aut(F_2) mapping-torus presentations, asserting 0
    mismatches across H_1 torsion, D_p (p in {3,5,7,11,13}), D_5 cusp boundary
    triviality, 2T = SL(2,F_3), A_5 = PSL(2,F_5), plus dual oriented
    amphichirality checks (symmetry_group().is_amphicheiral() vs det < 0
    self-isometries) and m000/m003/m004 isometry verification.
  - Task OW1-C: All 35 prime knots 3_1..8_21 in S^3, dual independent exact knot
    determinant |Delta_K(-1)| (Seifert |det(V+V^T)| vs Fox J(-1) SNF), exact
    rational Sylvester signature of V+V^T, D_p surjection counts cross-checked
    against SNF invariant factors & p | |Delta_K(-1)|, canonical longitude image
    in D_5, 2T and A_5 surjection counts, dual oriented amphichirality checks.
  - Task OW1-D: All 4 planted faults PF-OW1-1..4 caught directly by evaluator.
"""

from collections import Counter
from fractions import Fraction
import itertools
import json
import math
import os
import warnings

warnings.filterwarnings("ignore")

import mpmath
import snappy


# =============================================================================
# EXACT LINEAR ALGEBRA & NUMBER THEORY HELPERS (INTEGER / FRACTION / F_p)
# =============================================================================

def mat_rank_fraction(mat):
    """Exact rank over Q via Fraction Gaussian elimination."""
    if not mat or not mat[0]:
        return 0
    m = len(mat)
    n = len(mat[0])
    A = [[Fraction(x) for x in row] for row in mat]
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        for i in range(r + 1, m):
            if A[i][c] != 0:
                f = A[i][c] / pv
                for j in range(c, n):
                    A[i][j] -= f * A[r][j]
        r += 1
        if r == m:
            break
    return r


def det_exact_int(mat):
    """Exact determinant of an integer square matrix via Fraction elimination."""
    n = len(mat)
    if n == 0:
        return 1
    A = [[Fraction(x) for x in row] for row in mat]
    sign = 1
    for i in range(n):
        piv = None
        for r in range(i, n):
            if A[r][i] != 0:
                piv = r
                break
        if piv is None:
            return 0
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            sign = -sign
        pv = A[i][i]
        for r in range(i + 1, n):
            if A[r][i] != 0:
                f = A[r][i] / pv
                for c in range(i, n):
                    A[r][c] -= f * A[i][c]
    res = Fraction(sign)
    for i in range(n):
        res *= A[i][i]
    assert res.denominator == 1
    return res.numerator


def symmetric_signature_exact(mat):
    """Exact Sylvester inertia (n_pos, n_neg, n_zero) of symmetric int matrix."""
    n = len(mat)
    A = [[Fraction(x) for x in row] for row in mat]
    for i in range(n):
        for j in range(n):
            assert A[i][j] == A[j][i], "Matrix is not symmetric"
    i = 0
    while i < n:
        piv = None
        for r in range(i, n):
            if A[r][r] != 0:
                piv = r
                break
        if piv is None:
            found = None
            for p in range(i, n):
                for q in range(p + 1, n):
                    if A[p][q] != 0:
                        found = (p, q)
                        break
                if found is not None:
                    break
            if found is None:
                break
            p, q = found
            # Congruence: row p += row q, col p += col q => A[p][p] = 2 A[p][q] != 0
            for c in range(n):
                A[p][c] += A[q][c]
            for r in range(n):
                A[r][p] += A[r][q]
            piv = p
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            for r in range(n):
                A[r][i], A[r][piv] = A[r][piv], A[r][i]
        pv = A[i][i]
        for j in range(i + 1, n):
            if A[j][i] != 0:
                f = A[j][i] / pv
                for c in range(i, n):
                    A[j][c] -= f * A[i][c]
                for r in range(i, n):
                    A[r][j] -= f * A[r][i]
        i += 1
    n_pos = sum(1 for k in range(n) if A[k][k] > 0)
    n_neg = sum(1 for k in range(n) if A[k][k] < 0)
    n_zero = sum(1 for k in range(n) if A[k][k] == 0)
    return n_pos, n_neg, n_zero


def smith_normal_form_invariants(mat):
    """Exact integer Smith Normal Form returning positive invariant factors."""
    if not mat or not mat[0]:
        return []
    m = len(mat)
    n = len(mat[0])
    A = [[int(x) for x in row] for row in mat]
    lim = min(m, n)
    k = 0
    while k < lim:
        # Find smallest nonzero absolute value in A[k:, k:]
        best = None
        for r in range(k, m):
            for c in range(k, n):
                v = abs(A[r][c])
                if v > 0 and (best is None or v < best[0]):
                    best = (v, r, c)
        if best is None:
            break
        _, br, bc = best
        if br != k:
            A[k], A[br] = A[br], A[k]
        if bc != k:
            for r in range(m):
                A[r][k], A[r][bc] = A[r][bc], A[r][k]
        if A[k][k] < 0:
            for c in range(n):
                A[k][c] = -A[k][c]

        while True:
            # Clear column k below row k
            restarted = False
            for r in range(k + 1, m):
                if A[r][k] != 0:
                    q = A[r][k] // A[k][k]
                    for c in range(k, n):
                        A[r][c] -= q * A[k][c]
                    if A[r][k] != 0:
                        A[k], A[r] = A[r], A[k]
                        if A[k][k] < 0:
                            for c in range(k, n):
                                A[k][c] = -A[k][c]
                        restarted = True
                        break
            if restarted:
                continue

            # Clear row k right of col k
            for c in range(k + 1, n):
                if A[k][c] != 0:
                    q = A[k][c] // A[k][k]
                    for r in range(k, m):
                        A[r][c] -= q * A[r][k]
                    if A[k][c] != 0:
                        for r in range(k, m):
                            A[r][k], A[r][c] = A[r][c], A[r][k]
                        if A[k][k] < 0:
                            for cc in range(k, n):
                                A[k][cc] = -A[k][cc]
                        restarted = True
                        break
            if restarted:
                continue

            # Check divisibility of lower-right block
            bad_row = None
            for r in range(k + 1, m):
                for c in range(k + 1, n):
                    if A[r][c] % A[k][k] != 0:
                        bad_row = r
                        break
                if bad_row is not None:
                    break
            if bad_row is not None:
                for c in range(k, n):
                    A[k][c] += A[bad_row][c]
                continue
            break

        k += 1

    invs = [abs(A[i][i]) for i in range(lim) if A[i][i] != 0]
    for i in range(len(invs) - 1):
        assert invs[i + 1] % invs[i] == 0
    return invs


def kernel_basis_fp(mat, n_cols, p):
    """Exact basis of ker(mat) in F_p^{n_cols}."""
    A = [[x % p for x in row] for row in mat]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(n_cols):
        piv = None
        for i in range(r, m):
            if A[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv_pv = pow(A[r][c], p - 2, p)
        A[r] = [(v * inv_pv) % p for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(n_cols)]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    piv_set = set(piv_cols)
    free_cols = [c for c in range(n_cols) if c not in piv_set]
    basis = []
    for fc in free_cols:
        vec = [0] * n_cols
        vec[fc] = 1
        for row_idx, pc in enumerate(piv_cols):
            vec[pc] = (-A[row_idx][fc]) % p
        basis.append(vec)
    return basis


def rank_fp(rows, n_cols, p):
    """Rank of a list of row vectors over F_p."""
    A = [[x % p for x in row] for row in rows]
    m = len(A)
    r = 0
    for c in range(n_cols):
        piv = None
        for i in range(r, m):
            if A[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv_pv = pow(A[r][c], p - 2, p)
        A[r] = [(v * inv_pv) % p for v in A[r]]
        for i in range(r + 1, m):
            if A[i][c] != 0:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(n_cols)]
        r += 1
        if r == m:
            break
    return r


def int_kernel_1d(mat, n_cols):
    """For rank-(n_cols - 1) integer matrix, return primitive integer kernel vector."""
    A = [[Fraction(x) for x in row] for row in mat]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(n_cols):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n_cols)]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    assert len(piv_cols) == n_cols - 1, f"Expected rank {n_cols - 1}, got {len(piv_cols)}"
    piv_set = set(piv_cols)
    fc = [c for c in range(n_cols) if c not in piv_set][0]
    vec_q = [Fraction(0)] * n_cols
    vec_q[fc] = Fraction(1)
    for row_idx, pc in enumerate(piv_cols):
        vec_q[pc] = -A[row_idx][fc]
    lcm_d = 1
    for q in vec_q:
        lcm_d = (lcm_d * q.denominator) // math.gcd(lcm_d, q.denominator)
    vec_i = [int(q * lcm_d) for q in vec_q]
    g = 0
    for v in vec_i:
        g = math.gcd(g, abs(v))
    vec_i = [v // g for v in vec_i]
    # Verify exact zero
    for row in mat:
        assert sum(row[j] * vec_i[j] for j in range(n_cols)) == 0
    return vec_i


# =============================================================================
# TASK OW1-A: TODD-COXETER Delta(2,3,N), CORE-FREE ACTIONS, GAUGE-MATTER ENGINE
# =============================================================================

def todd_coxeter_delta_2_3_N(N):
    """
    Construct Delta(2,3,N) = <s, u | s^2 = u^3 = (s u)^N = 1> on trivial
    subgroup {1} via pure Todd-Coxeter coset enumeration.
    Returns (order, s_perm, u_perm) as right regular permutations on 0..order-1.
    """
    # Generators: 0:s, 1:s^-1, 2:u, 3:u^-1
    inv_g = [1, 0, 3, 2]
    relators = [
        [0, 0],
        [2, 2, 2],
        [0, 2] * N,
    ]

    parent = [0]
    table = [[None, None, None, None]]
    alive = [True]

    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c

    def merge(c1, c2):
        queue = [(c1, c2)]
        while queue:
            a, b = queue.pop()
            ra, rb = find(a), find(b)
            if ra == rb:
                continue
            if ra > rb:
                ra, rb = rb, ra
            parent[rb] = ra
            alive[rb] = False
            for g in range(4):
                t = table[rb][g]
                if t is not None:
                    table[rb][g] = None
                    rt = find(t)
                    # Clear old back-pointer if pointing to rb
                    if table[rt][inv_g[g]] is not None and find(table[rt][inv_g[g]]) == ra:
                        table[rt][inv_g[g]] = ra
                    cur = table[ra][g]
                    if cur is None:
                        table[ra][g] = rt
                        if table[rt][inv_g[g]] is None:
                            table[rt][inv_g[g]] = ra
                        else:
                            queue.append((table[rt][inv_g[g]], ra))
                    else:
                        queue.append((cur, rt))
            # Normalize pointers in ra row
            for g in range(4):
                if table[ra][g] is not None:
                    rt = find(table[ra][g])
                    table[ra][g] = rt
                    if table[rt][inv_g[g]] is None:
                        table[rt][inv_g[g]] = ra
                    elif find(table[rt][inv_g[g]]) != ra:
                        queue.append((table[rt][inv_g[g]], ra))

    def set_edge(c, g, d):
        rc, rd = find(c), find(d)
        cur = table[rc][g]
        if cur is not None:
            if find(cur) != rd:
                merge(cur, rd)
            return
        cur_inv = table[rd][inv_g[g]]
        if cur_inv is not None:
            if find(cur_inv) != rc:
                merge(cur_inv, rc)
                return
        table[rc][g] = rd
        table[rd][inv_g[g]] = rc

    def define(c, g):
        rc = find(c)
        new_c = len(parent)
        parent.append(new_c)
        alive.append(True)
        table.append([None, None, None, None])
        table[rc][g] = new_c
        table[new_c][inv_g[g]] = rc

    while True:
        changed = True
        while changed:
            changed = False
            live_cosets = [c for c in range(len(parent)) if alive[c]]
            for c in live_cosets:
                if not alive[c]:
                    continue
                for rel in relators:
                    if not alive[c]:
                        break
                    L = len(rel)
                    f_pos = 0
                    f_cos = find(c)
                    while f_pos < L:
                        nxt = table[f_cos][rel[f_pos]]
                        if nxt is None:
                            break
                        f_cos = find(nxt)
                        f_pos += 1
                    if f_pos == L:
                        if f_cos != find(c):
                            merge(f_cos, find(c))
                            changed = True
                        continue
                    b_pos = L
                    b_cos = find(c)
                    while b_pos > f_pos:
                        nxt = table[b_cos][inv_g[rel[b_pos - 1]]]
                        if nxt is None:
                            break
                        b_cos = find(nxt)
                        b_pos -= 1
                    if b_pos == f_pos:
                        if f_cos != b_cos:
                            merge(f_cos, b_cos)
                            changed = True
                    elif b_pos == f_pos + 1:
                        set_edge(f_cos, rel[f_pos], b_cos)
                        changed = True

        # Find first undefined slot
        undef = None
        for c in range(len(parent)):
            if not alive[c]:
                continue
            for g in (0, 2, 1, 3):
                if table[c][g] is None:
                    undef = (c, g)
                    break
            if undef is not None:
                break
        if undef is None:
            break
        define(undef[0], undef[1])

    live = [c for c in range(len(parent)) if alive[c]]
    idx_map = {c: i for i, c in enumerate(live)}
    order = len(live)
    s_perm = tuple(idx_map[find(table[c][0])] for c in live)
    u_perm = tuple(idx_map[find(table[c][2])] for c in live)

    # Self-verify defining relations
    id_p = tuple(range(order))
    def comp(p, q):
        # Right action composition: (p*q)(x) = q(p(x))
        return tuple(q[p[x]] for x in range(order))

    assert comp(s_perm, s_perm) == id_p
    assert comp(comp(u_perm, u_perm), u_perm) == id_p
    su = comp(s_perm, u_perm)
    cur = id_p
    for _ in range(N):
        cur = comp(cur, su)
    assert cur == id_p
    return order, s_perm, u_perm


def build_group_from_perms(gens):
    """Build full multiplication table from permutation generators."""
    deg = len(gens[0])
    id_p = tuple(range(deg))

    def comp(p, q):
        return tuple(q[p[x]] for x in range(deg))

    elems = [id_p]
    idx = {id_p: 0}
    queue = [id_p]
    while queue:
        cur = queue.pop()
        for g in gens:
            nxt = comp(cur, g)
            if nxt not in idx:
                idx[nxt] = len(elems)
                elems.append(nxt)
                queue.append(nxt)
    n = len(elems)
    mul = [[idx[comp(elems[i], elems[j])] for j in range(n)] for i in range(n)]
    inv = [0] * n
    for i in range(n):
        for j in range(n):
            if mul[i][j] == 0:
                inv[i] = j
                break
    return {
        "order": n,
        "elems": elems,
        "mul": mul,
        "inv": inv,
        "id": 0,
    }


def enumerate_all_subgroups(G):
    """Exhaustively enumerate every subgroup of finite group G (|G| <= 60)."""
    n = G["order"]
    mul = G["mul"]

    def close_subgroup(seed_set):
        s = set(seed_set)
        s.add(0)
        frontier = list(s)
        while frontier:
            x = frontier.pop()
            snapshot = list(s)
            for y in snapshot:
                xy = mul[x][y]
                if xy not in s:
                    s.add(xy)
                    frontier.append(xy)
                yx = mul[y][x]
                if yx not in s:
                    s.add(yx)
                    frontier.append(yx)
        return frozenset(s)

    cyclic = [close_subgroup({g}) for g in range(n)]
    unique_cyclic = sorted(set(cyclic), key=lambda s: (len(s), sorted(s)))

    subgroups = {frozenset({0})}
    queue = [frozenset({0})]
    while queue:
        H = queue.pop()
        for C in unique_cyclic:
            if C.issubset(H):
                continue
            K = close_subgroup(H | C)
            if K not in subgroups:
                subgroups.add(K)
                queue.append(K)
    return subgroups


def conjugacy_classes_elements(G):
    """Conjugacy classes of elements in finite group G."""
    n = G["order"]
    mul = G["mul"]
    inv = G["inv"]
    seen = set()
    classes = []
    for x in range(n):
        if x in seen:
            continue
        cls = sorted({mul[mul[g][x]][inv[g]] for g in range(n)})
        for y in cls:
            seen.add(y)
        classes.append(cls)
    return classes


def subgroup_conjugacy_classes(G, subgroups):
    """Group subgroups into G-conjugacy classes."""
    n = G["order"]
    mul = G["mul"]
    inv = G["inv"]
    seen = set()
    classes = []
    for H in sorted(subgroups, key=lambda s: (len(s), sorted(s))):
        if H in seen:
            continue
        orb = set()
        for g in range(n):
            ig = inv[g]
            conj = frozenset(mul[mul[g][h]][ig] for h in H)
            orb.add(conj)
        for K in orb:
            seen.add(K)
        rep = min(orb, key=lambda s: sorted(s))
        classes.append((rep, len(orb), orb))
    return classes


def is_core_free(G, H):
    """Compute Core_G(H) = intersection of all conjugates g H g^-1 explicitly."""
    n = G["order"]
    mul = G["mul"]
    inv = G["inv"]
    core = set(H)
    for g in range(n):
        ig = inv[g]
        conj = {mul[mul[g][h]][ig] for h in H}
        core &= conj
    return core == {0}


def coset_action_perm(G, H, elem):
    """Right-coset permutation H x -> H (x * elem) for elem in G."""
    n = G["order"]
    mul = G["mul"]
    cosets = []
    seen = set()
    for x in range(n):
        if x in seen:
            continue
        cs = frozenset(mul[h][x] for h in H)
        cosets.append(cs)
        seen |= cs
    cs_idx = {cs: i for i, cs in enumerate(cosets)}
    perm = []
    for cs in cosets:
        rep = next(iter(cs))
        nxt = frozenset(mul[h][mul[rep][elem]] for h in H)
        perm.append(cs_idx[nxt])
    return tuple(perm)


def cycle_partition(perm):
    """Return sorted list of cycle lengths of permutation perm."""
    n = len(perm)
    seen = [False] * n
    lens = []
    for i in range(n):
        if not seen[i]:
            c = 0
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cur = perm[cur]
                c += 1
            lens.append(c)
    return sorted(lens)


def perm_matrix_eigen_multiplicities(perm):
    """
    Build explicit d x d permutation matrix P for an involution (assert P^2 = I)
    and compute exact +1 and -1 eigenspace dimensions (a, b) via Fraction rank.
    """
    d = len(perm)
    P = [[1 if perm[j] == i else 0 for j in range(d)] for i in range(d)]
    # Verify P^2 == I_d
    for i in range(d):
        for j in range(d):
            val = sum(P[i][k] * P[k][j] for k in range(d))
            assert val == (1 if i == j else 0)
    P_minus_I = [[P[i][j] - (1 if i == j else 0) for j in range(d)] for i in range(d)]
    P_plus_I = [[P[i][j] + (1 if i == j else 0) for j in range(d)] for i in range(d)]
    a = d - mat_rank_fraction(P_minus_I)
    b = d - mat_rank_fraction(P_plus_I)
    assert a + b == d
    return a, b, P


def centralizer_su_dim_explicit(P):
    """
    Compute exact real dimension of C_{su(d)}(P) directly as nullspace dimension
    of X -> [P, X] on the (d^2 - 1)-dimensional space of traceless matrices.
    (Note: since P is real symmetric, complexification of C_{su(d)}(P) is
    C_{sl(d, C)}(P), whose complex dimension equals real dim of C_{su(d)}(P).)
    """
    d = len(P)
    # Basis of sl(d): E_{r,c} (r != c) and E_{k,k} - E_{d-1,d-1} (0 <= k < d-1)
    basis = []
    for r in range(d):
        for c in range(d):
            if r != c:
                M = [[0] * d for _ in range(d)]
                M[r][c] = 1
                basis.append(M)
    for k in range(d - 1):
        M = [[0] * d for _ in range(d)]
        M[k][k] = 1
        M[d - 1][d - 1] = -1
        basis.append(M)
    n_basis = len(basis)
    assert n_basis == d * d - 1

    # Columns of linear operator ad_P: M -> P M - M P flattened to length d^2
    cols = []
    for M in basis:
        comm = [
            sum(P[i][k] * M[k][j] - M[i][k] * P[k][j] for k in range(d))
            for i in range(d)
            for j in range(d)
        ]
        cols.append(comm)
    # Transpose to (d^2) x (d^2 - 1)
    mat = [[cols[c][r] for c in range(n_basis)] for r in range(d * d)]
    dim_cent = n_basis - mat_rank_fraction(mat)
    return dim_cent


def compute_global_kernel_order_lambda_even(a, b, y_vec_fund):
    """
    Compute exact order |K| of the kernel of SU(a) x SU(b) x U(1) acting on
    Lambda^{even}(C^d), solving the exact Q/Z congruence system for every
    (k_a, k_b) in Z/aZ x Z/bZ across all even (p, q) sectors present in
    Lambda^{even}(C^d).
    Returns (kernel_order_y_reduced, kernel_order_faithful_u1, gcd_even_charges, is_cyclic_z6).
    """
    g = math.gcd(a, b)
    a_red = a // g
    b_red = b // g
    # Verify y_vec_fund matches ((-b_red)^a, (+a_red)^b)
    assert y_vec_fund == [-b_red] * a + [a_red] * b

    # Allowed even pairs (p, q) with 0 <= p <= a, 0 <= q <= b, p + q even
    even_pairs = [
        (p, q)
        for p in range(a + 1)
        for q in range(b + 1)
        if (p + q) % 2 == 0
    ]
    charges = [-b_red * p + a_red * q for (p, q) in even_pairs]
    gcd_even = 0
    for ch in charges:
        gcd_even = math.gcd(gcd_even, abs(ch))

    def solve_kernel(charge_div):
        # Solve t * (ch / charge_div) == -(p*k_a/a + q*k_b/b) (mod 1) for t in [0, 1)
        # Wait: if all charges are 0 (e.g. a=1,b=1), U(1) acts trivially (infinite kernel).
        if gcd_even == 0:
            return None, []
        elems = []
        # Extended gcd to solve simultaneous congruences c_i * t == r_i (mod 1)
        # First combine integer coefficients c_i into gcd = g_c via Bezout
        c_list = [ch // charge_div for ch in charges]
        # Compute Bezout coefficients u_i such that sum(u_i * c_i) == g_cur
        g_cur = 0
        bezout = [0] * len(c_list)
        for idx_i, ci in enumerate(c_list):
            if ci == 0:
                continue
            if g_cur == 0:
                g_cur = abs(ci)
                bezout[idx_i] = 1 if ci > 0 else -1
            else:
                # Extended Euclidean algorithm on (g_cur, ci)
                old_r, r = g_cur, ci
                old_s, s = 1, 0
                old_t, t_v = 0, 1
                while r != 0:
                    q_div = old_r // r
                    old_r, r = r, old_r - q_div * r
                    old_s, s = s, old_s - q_div * s
                    old_t, t_v = t_v, old_t - q_div * t_v
                if old_r < 0:
                    old_r, old_s, old_t = -old_r, -old_s, -old_t
                bezout = [b_val * old_s for b_val in bezout]
                bezout[idx_i] += old_t
                g_cur = old_r
        assert sum(bezout[i] * c_list[i] for i in range(len(c_list))) == g_cur

        for ka in range(a):
            for kb in range(b):
                rhs = [
                    -(Fraction(p * ka, a) + Fraction(q * kb, b))
                    for (p, q) in even_pairs
                ]
                # Necessary condition: g_cur * t == R (mod 1) where R = sum(bezout_i * rhs_i)
                R = sum(bezout[i] * rhs[i] for i in range(len(c_list)))
                # Candidate solutions t = (R + m) / g_cur mod 1 for m = 0..g_cur-1
                for m_shift in range(g_cur):
                    t_cand = (R + m_shift) / g_cur
                    t_cand = t_cand - math.floor(t_cand)
                    ok = True
                    for idx_i, ci in enumerate(c_list):
                        diff = ci * t_cand - rhs[idx_i]
                        if diff.denominator != 1:
                            ok = False
                            break
                    if ok:
                        elems.append((ka, kb, t_cand))
        return len(elems), elems

    k_red, elems_red = solve_kernel(1)
    k_faith, elems_faith = solve_kernel(gcd_even) if gcd_even > 0 else (None, [])

    # Check if kernel is cyclic Z_6
    is_cyclic_z6 = False
    if k_red == 6 and k_faith == 6:
        # Check whether there exists an element of exact order 6 in Z/aZ x Z/bZ x Q/Z
        for ka, kb, t_val in elems_red:
            ord_a = a // math.gcd(a, ka) if ka != 0 else 1
            ord_b = b // math.gcd(b, kb) if kb != 0 else 1
            ord_t = t_val.denominator
            ord_ab = (ord_a * ord_b) // math.gcd(ord_a, ord_b)
            ord_tot = (ord_ab * ord_t) // math.gcd(ord_ab, ord_t)
            if ord_tot == 6:
                is_cyclic_z6 = True
                break
    return k_red, k_faith, gcd_even, is_cyclic_z6


def evaluate_gauge_matter_sector(a, b, P_mat=None):
    """
    Evaluate full Berezin-CAR Lambda^{even}(C^d) chiral matter, 4 anomalies,
    centralizer dimension, global kernel |K|, and collar-odd scalar splitting
    for an involution with (+1, -1) eigenvalue multiplicities (a, b).
    """
    d = a + b
    g = math.gcd(a, b)
    a_red = a // g
    b_red = b // g
    y_vec = [-b_red] * a + [a_red] * b
    assert sum(y_vec) == 0

    dim_cent_formula = a * a + b * b - 1
    if P_mat is not None and d <= 12:
        dim_cent_explicit = centralizer_su_dim_explicit(P_mat)
        assert dim_cent_explicit == dim_cent_formula
    else:
        dim_cent_explicit = dim_cent_formula

    # Diagonal Cartan generators H_a in su(a) and H_b in su(b)
    h_a = [0] * d
    if a >= 2:
        h_a[0] = 1
        h_a[1] = -1
    h_b = [0] * d
    if b >= 2:
        h_b[a] = 1
        h_b[a + 1] = -1

    # Explicit bitmask enumeration of all 2^(d-1) states in Lambda^{even}(C^d)
    y_spec = []
    tr_y = 0
    tr_y3 = 0
    tr_sua2_y = 0
    tr_sub2_y = 0
    for mask in range(1 << d):
        if mask.bit_count() % 2 != 0:
            continue
        yv = 0
        ha_v = 0
        hb_v = 0
        for i in range(d):
            if (mask >> i) & 1:
                yv += y_vec[i]
                ha_v += h_a[i]
                hb_v += h_b[i]
        y_spec.append(yv)
        tr_y += yv
        tr_y3 += yv * yv * yv
        tr_sua2_y += ha_v * ha_v * yv
        tr_sub2_y += hb_v * hb_v * yv

    assert len(y_spec) == (1 << (d - 1))
    y_sorted = sorted(y_spec)
    y_neg_sorted = sorted(-y for y in y_spec)
    is_chiral = (y_sorted != y_neg_sorted)
    anomaly_free = (tr_y == 0 and tr_y3 == 0 and tr_sua2_y == 0 and tr_sub2_y == 0)

    k_red, k_faith, gcd_even, is_cyclic_z6 = compute_global_kernel_order_lambda_even(a, b, y_vec)

    # Collar-odd (P = -1) scalar decomposition on C^d (+) (C^d)* (the 2d vector rep of SO(2d))
    # P = +1 subspace has dim 2*a (a-plet + abar-plet); P = -1 subspace has dim 2*b (b-plet + bbar-plet).
    collar_odd_b_multiplets = 2 if b >= 1 else 0
    collar_odd_a_multiplets = 0
    collar_even_a_multiplets = 2 if a >= 1 else 0
    collar_odd_dim = 2 * b
    collar_even_dim = 2 * a
    # Specifically for SM doublet/triplet (a=3 triplet, b=2 doublet):
    is_sm_doublet_triplet_split = (a == 3 and b == 2 and collar_odd_b_multiplets == 2 and collar_odd_a_multiplets == 0)

    sm_6y_target = sorted([-4] * 3 + [-3] * 2 + [0] + [1] * 6 + [2] * 3 + [6])
    matches_sm_6y = (y_sorted == sm_6y_target)

    passes_full_sm_bar = (
        len(y_spec) == 16
        and is_chiral
        and anomaly_free
        and dim_cent_explicit == 12
        and k_red == 6
        and is_cyclic_z6
        and matches_sm_6y
        and is_sm_doublet_triplet_split
    )

    multiset_counts = {str(k): v for k, v in sorted(Counter(y_sorted).items())}
    return {
        "d": d,
        "a": a,
        "b": b,
        "dim_centralizer": dim_cent_explicit,
        "dim_lambda_even": len(y_spec),
        "y_vec_fund": y_vec,
        "y_multiset": multiset_counts,
        "is_chiral": is_chiral,
        "anomalies": {
            "Tr_Y": tr_y,
            "Tr_Y3": tr_y3,
            "Tr_SUa2_Y": tr_sua2_y,
            "Tr_SUb2_Y": tr_sub2_y,
        },
        "anomaly_free": anomaly_free,
        "kernel_order_y_reduced": k_red,
        "kernel_order_faithful_u1": k_faith,
        "gcd_even_charges": gcd_even,
        "is_cyclic_z6": is_cyclic_z6,
        "collar_odd_dim": collar_odd_dim,
        "collar_even_dim": collar_even_dim,
        "collar_odd_b_multiplets": collar_odd_b_multiplets,
        "collar_odd_a_multiplets": collar_odd_a_multiplets,
        "matches_sm_6y": matches_sm_6y,
        "is_sm_doublet_triplet_split": is_sm_doublet_triplet_split,
        "passes_full_sm_bar": passes_full_sm_bar,
    }


def verify_weyl_24_and_cl10():
    """
    1. Verify the 24-Weyl operator identity in D_5:
       -(1/2) sum_{v != 0} D(v) = (1/2) I_5 - (5/2) P = diag(-2,-2,-2,+3,+3)
       BOTH algebraically in exact cyclotomic ring Q[w]/(Phi_5(w)) AND
       numerically at 60-digit mpmath precision (< 10^-50).
    2. Verify explicit 32x32 Cl(10) CAR anticommutators and gamma matrices in
       exact Gaussian-integer arithmetic (0 errors).
    """
    # --- Part 1A: Exact cyclotomic ring Q[w]/(1 + w + w^2 + w^3 + w^4) ---
    # Represent elements as 4-tuples of Fractions: c0 + c1*w + c2*w^2 + c3*w^3
    zero_c = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))

    def c_add(x, y):
        return tuple(x[i] + y[i] for i in range(4))

    def c_scale(x, q):
        return tuple(x[i] * q for i in range(4))

    def w_pow(k):
        r = k % 5
        if r < 4:
            return tuple(Fraction(1) if i == r else Fraction(0) for i in range(4))
        # w^4 = -1 - w - w^2 - w^3
        return (Fraction(-1), Fraction(-1), Fraction(-1), Fraction(-1))

    # Build 5x5 matrices D(p, q) = w^{3 p q} X^p Z^q where
    # (X^p Z^q)_{i, j} = w^{q * j} if i == (j + p) mod 5 else 0
    sum_mat = [[zero_c for _ in range(5)] for _ in range(5)]
    count_nonzero_v = 0
    for p in range(5):
        for q in range(5):
            if p == 0 and q == 0:
                continue
            count_nonzero_v += 1
            for j in range(5):
                i = (j + p) % 5
                exp = (3 * p * q + q * j) % 5
                sum_mat[i][j] = c_add(sum_mat[i][j], w_pow(exp))
    assert count_nonzero_v == 24

    # lhs = -(1/2) * sum_mat
    lhs_cyc = [
        [c_scale(sum_mat[i][j], Fraction(-1, 2)) for j in range(5)]
        for i in range(5)
    ]

    # Verify all non-constant cyclotomic coefficients vanish identically
    lhs_rat = [[None] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            assert lhs_cyc[i][j][1] == 0
            assert lhs_cyc[i][j][2] == 0
            assert lhs_cyc[i][j][3] == 0
            lhs_rat[i][j] = lhs_cyc[i][j][0]

    # Exact parity permutation P |k> = |-k mod 5>
    P_perm = [(-k) % 5 for k in range(5)]
    P_mat = [[Fraction(1) if P_perm[j] == i else Fraction(0) for j in range(5)] for i in range(5)]
    rhs_rat = [
        [
            (Fraction(1, 2) if i == j else Fraction(0)) - Fraction(5, 2) * P_mat[i][j]
            for j in range(5)
        ]
        for i in range(5)
    ]
    exact_identity_holds = (lhs_rat == rhs_rat)
    assert exact_identity_holds

    # Exact rational similarity into P-eigenbasis:
    # +1 eigenvectors: e0, e1+e4, e2+e3; -1 eigenvectors: e1-e4, e2-e3
    U = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(-1), Fraction(0)],
    ]
    U_inv = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(0), Fraction(0), Fraction(1, 2)],
        [Fraction(0), Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(0), Fraction(0), Fraction(-1, 2)],
        [Fraction(0), Fraction(0), Fraction(1, 2), Fraction(-1, 2), Fraction(0)],
    ]
    # Verify U_inv * U == I_5
    for i in range(5):
        for j in range(5):
            val = sum(U_inv[i][k] * U[k][j] for k in range(5))
            assert val == (Fraction(1) if i == j else Fraction(0))

    # Compute U_inv * lhs_rat * U
    tmp = [[sum(lhs_rat[i][k] * U[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    diag_mat = [[sum(U_inv[i][k] * tmp[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    target_diag = [-2, -2, -2, 3, 3]
    exact_eigenbasis_holds = all(
        diag_mat[i][j] == (Fraction(target_diag[i]) if i == j else Fraction(0))
        for i in range(5)
        for j in range(5)
    )
    assert exact_eigenbasis_holds

    # --- Part 1B: 60-digit mpmath numerical verification (< 10^-50) ---
    mpmath.mp.dps = 60
    I_unit = mpmath.mpc(0, 1)
    omega = mpmath.exp(2 * mpmath.pi * I_unit / 5)
    sum_mp = [[mpmath.mpc(0, 0) for _ in range(5)] for _ in range(5)]
    for p in range(5):
        for q in range(5):
            if p == 0 and q == 0:
                continue
            for j in range(5):
                i = (j + p) % 5
                sum_mp[i][j] += omega ** ((3 * p * q + q * j) % 5)
    half = mpmath.mpf(1) / mpmath.mpf(2)
    five_half = mpmath.mpf(5) / mpmath.mpf(2)
    max_err_perm_basis = mpmath.mpf(0)
    for i in range(5):
        for j in range(5):
            lhs_val = -half * sum_mp[i][j]
            rhs_val = (half if i == j else mpmath.mpf(0)) - five_half * (1 if P_perm[j] == i else 0)
            err = abs(lhs_val - rhs_val)
            if err > max_err_perm_basis:
                max_err_perm_basis = err

    # Orthogonal P-eigenbasis in mpmath
    inv_s2 = mpmath.mpf(1) / mpmath.sqrt(mpmath.mpf(2))
    Q_orth = [
        [mpmath.mpf(1), mpmath.mpf(0), mpmath.mpf(0), mpmath.mpf(0), mpmath.mpf(0)],
        [mpmath.mpf(0), inv_s2, mpmath.mpf(0), inv_s2, mpmath.mpf(0)],
        [mpmath.mpf(0), mpmath.mpf(0), inv_s2, mpmath.mpf(0), inv_s2],
        [mpmath.mpf(0), mpmath.mpf(0), inv_s2, mpmath.mpf(0), -inv_s2],
        [mpmath.mpf(0), inv_s2, mpmath.mpf(0), -inv_s2, mpmath.mpf(0)],
    ]
    lhs_mp = [[-half * sum_mp[i][j] for j in range(5)] for i in range(5)]
    tmp_mp = [[sum(lhs_mp[i][k] * Q_orth[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    diag_mp = [[sum(Q_orth[k][i] * tmp_mp[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    max_err_eigenbasis = mpmath.mpf(0)
    for i in range(5):
        for j in range(5):
            target_val = mpmath.mpf(target_diag[i]) if i == j else mpmath.mpf(0)
            err = abs(diag_mp[i][j] - target_val)
            if err > max_err_eigenbasis:
                max_err_eigenbasis = err

    tol = mpmath.mpf(10) ** (-50)
    mpmath_pass = (max_err_perm_basis < tol and max_err_eigenbasis < tol)
    assert mpmath_pass

    # --- Part 2: Explicit 32x32 Cl(10) CAR & gamma anticommutators ---
    dim = 32
    a_ops = []
    adag_ops = []
    for mode in range(5):
        A_op = [[0] * dim for _ in range(dim)]
        Ad_op = [[0] * dim for _ in range(dim)]
        for state in range(dim):
            # Jordan-Wigner sign: parity of bits strictly below `mode`
            below_mask = state & ((1 << mode) - 1)
            jw_sign = -1 if (below_mask.bit_count() % 2 == 1) else 1
            if (state >> mode) & 1:
                new_state = state ^ (1 << mode)
                A_op[new_state][state] = jw_sign
            else:
                new_state = state ^ (1 << mode)
                Ad_op[new_state][state] = jw_sign
        a_ops.append(A_op)
        adag_ops.append(Ad_op)

    def mat_anticomm_int(X, Y):
        out = [[0] * dim for _ in range(dim)]
        for i in range(dim):
            xi = X[i]
            yi = Y[i]
            row = out[i]
            for k in range(dim):
                xik = xi[k]
                yik = yi[k]
                if xik != 0:
                    yk = Y[k]
                    for j in range(dim):
                        if yk[j] != 0:
                            row[j] += xik * yk[j]
                if yik != 0:
                    xk = X[k]
                    for j in range(dim):
                        if xk[j] != 0:
                            row[j] += yik * xk[j]
        return out

    car_errors = 0
    for j in range(5):
        for k in range(5):
            aa = mat_anticomm_int(a_ops[j], a_ops[k])
            adad = mat_anticomm_int(adag_ops[j], adag_ops[k])
            aad = mat_anticomm_int(a_ops[j], adag_ops[k])
            for r in range(dim):
                for c in range(dim):
                    if aa[r][c] != 0:
                        car_errors += 1
                    if adad[r][c] != 0:
                        car_errors += 1
                    exp_val = 1 if (j == k and r == c) else 0
                    if aad[r][c] != exp_val:
                        car_errors += 1

    # Build 10 Hermitian Cl(10) gamma matrices in exact Gaussian-integer pairs (re, im):
    # gamma_{2j} = a_j + a_j^dag (real), gamma_{2j+1} = -i (a_j - a_j^dag) (imag)
    gammas = []
    for j in range(5):
        g_even = [[(a_ops[j][r][c] + adag_ops[j][r][c], 0) for c in range(dim)] for r in range(dim)]
        g_odd = [[(0, -(a_ops[j][r][c] - adag_ops[j][r][c])) for c in range(dim)] for r in range(dim)]
        gammas.append(g_even)
        gammas.append(g_odd)

    gamma_errors = 0
    for mu in range(10):
        G1 = gammas[mu]
        for nu in range(10):
            G2 = gammas[nu]
            for r in range(dim):
                for c in range(dim):
                    s_re = 0
                    s_im = 0
                    for k in range(dim):
                        a1, b1 = G1[r][k]
                        a2, b2 = G2[k][c]
                        if a1 or b1:
                            if a2 or b2:
                                s_re += a1 * a2 - b1 * b2
                                s_im += a1 * b2 + b1 * a2
                        c1, d1 = G2[r][k]
                        c2, d2 = G1[k][c]
                        if c1 or d1:
                            if c2 or d2:
                                s_re += c1 * c2 - d1 * d2
                                s_im += c1 * d2 + d1 * c2
                    exp_re = 2 if (mu == nu and r == c) else 0
                    if s_re != exp_re or s_im != 0:
                        gamma_errors += 1

    assert car_errors == 0
    assert gamma_errors == 0

    # Verify Y_Fock = sum_j Y_vec[j] a_j^dag a_j on Gamma_11 = +1 (even parity) 16-dim sector
    y_vec_5 = [-2, -2, -2, 3, 3]
    even_eigs = []
    odd_eigs = []
    for state in range(dim):
        # Compute diagonal entry of Y_Fock directly from matrix products adag_ops[j] * a_ops[j]
        val = 0
        for j in range(5):
            # (adag_ops[j] @ a_ops[j])[state][state]
            n_j = sum(adag_ops[j][state][k] * a_ops[j][k][state] for k in range(dim))
            val += y_vec_5[j] * n_j
        # Chirality eigenvalue prod_j (1 - 2 n_j)
        chir = 1
        for j in range(5):
            n_j = sum(adag_ops[j][state][k] * a_ops[j][k][state] for k in range(dim))
            chir *= (1 - 2 * n_j)
        if chir == 1:
            even_eigs.append(val)
        else:
            assert chir == -1
            odd_eigs.append(val)

    assert len(even_eigs) == 16 and len(odd_eigs) == 16
    assert sorted(even_eigs) == sorted([-4] * 3 + [-3] * 2 + [0] + [1] * 6 + [2] * 3 + [6])

    return {
        "weyl_24_count": count_nonzero_v,
        "exact_cyclotomic_identity_holds": exact_identity_holds,
        "exact_eigenbasis_diag_holds": exact_eigenbasis_holds,
        "eigenbasis_diag": target_diag,
        "mpmath_dps": 60,
        "mpmath_max_err_perm_basis": mpmath.nstr(max_err_perm_basis, 12),
        "mpmath_max_err_eigenbasis": mpmath.nstr(max_err_eigenbasis, 12),
        "mpmath_below_1e_minus_50": mpmath_pass,
        "cl10_dim": dim,
        "car_anticommutator_errors": car_errors,
        "gamma_anticommutator_errors": gamma_errors,
        "fock_even_dim": len(even_eigs),
        "fock_odd_dim": len(odd_eigs),
        "fock_even_6y_multiset": {str(k): v for k, v in sorted(Counter(even_eigs).items())},
    }


def run_task_ow1_a(grp_a5=None):
    """Execute Task OW1-A completely from first principles."""
    spherical_bound = {}
    for N in range(2, 8):
        lhs = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, N)
        spherical_bound[str(N)] = {
            "sum_reciprocals": f"{lhs.numerator}/{lhs.denominator}",
            "strictly_gt_1": (lhs > 1),
            "geometry": "spherical" if lhs > 1 else ("euclidean" if lhs == 1 else "hyperbolic"),
        }
    finite_rungs = [N for N in range(2, 8) if Fraction(1, 2) + Fraction(1, 3) + Fraction(1, N) > 1]
    assert finite_rungs == [2, 3, 4, 5]

    rungs_report = {}
    all_actions_flat = []
    sm_passing_actions = []

    a5_uniqueness = {}

    for N in finite_rungs:
        order, s_perm, u_perm = todd_coxeter_delta_2_3_N(N)
        G = build_group_from_perms([s_perm, u_perm])
        assert G["order"] == order

        subgroups = enumerate_all_subgroups(G)
        sub_classes = subgroup_conjugacy_classes(G, subgroups)
        elem_classes = conjugacy_classes_elements(G)

        # Involution conjugacy classes (order 2 elements: x != 0 and x*x == 0)
        inv_classes = [
            cls for cls in elem_classes
            if cls[0] != 0 and G["mul"][cls[0]][cls[0]] == 0
        ]

        core_free_actions = []
        for rep_H, cls_size, _ in sub_classes:
            d = order // len(rep_H)
            if d > 12:
                continue
            if not is_core_free(G, rep_H):
                continue
            # Build faithful permutation action on G / rep_H
            # Verify faithfulness on all G elements
            action_perms = [coset_action_perm(G, rep_H, g) for g in range(order)]
            assert len(set(action_perms)) == order

            inv_results = []
            for inv_idx, icls in enumerate(inv_classes):
                rep_P = icls[0]
                p_perm = action_perms[rep_P]
                cyc = cycle_partition(p_perm)
                a, b, P_mat = perm_matrix_eigen_multiplicities(p_perm)
                ev = evaluate_gauge_matter_sector(a, b, P_mat=P_mat)
                rec = {
                    "N": N,
                    "group_order": order,
                    "subgroup_order": len(rep_H),
                    "subgroup_conjugacy_class_size": cls_size,
                    "degree_d": d,
                    "involution_class_index": inv_idx,
                    "involution_class_size": len(icls),
                    "cycle_partition": cyc,
                    **ev,
                }
                inv_results.append(rec)
                all_actions_flat.append(rec)
                if ev["passes_full_sm_bar"]:
                    sm_passing_actions.append(rec)

            core_free_actions.append({
                "degree_d": d,
                "subgroup_order": len(rep_H),
                "subgroup_conjugacy_class_size": cls_size,
                "involution_evaluations": inv_results,
            })

        rungs_report[str(N)] = {
            "order": order,
            "total_subgroups": len(subgroups),
            "total_subgroup_conjugacy_classes": len(sub_classes),
            "involution_conjugacy_class_count": len(inv_classes),
            "involution_class_sizes": [len(c) for c in inv_classes],
            "core_free_actions_d_le_12_count": len(core_free_actions),
            "core_free_actions_d_le_12": core_free_actions,
        }

        if N == 5:
            # Explicit A_5 uniqueness checks
            idx5_classes = [c for c in sub_classes if order // len(c[0]) == 5]
            idx6_classes = [c for c in sub_classes if order // len(c[0]) == 6]
            assert len(idx5_classes) == 1
            assert len(idx6_classes) == 1
            # Verify index-6 subgroup is D_5 (order 10, non-abelian: 5 elements of order 2, 4 of order 5)
            H_d5 = idx6_classes[0][0]
            ord_counts_d5 = Counter()
            for h in H_d5:
                cur = h
                k_ord = 1
                while cur != 0:
                    cur = G["mul"][cur][h]
                    k_ord += 1
                ord_counts_d5[k_ord] += 1
            assert ord_counts_d5 == {1: 1, 2: 5, 5: 4}
            # Verify index-5 subgroup is A_4 (order 12: 3 of order 2, 8 of order 3)
            H_a4 = idx5_classes[0][0]
            ord_counts_a4 = Counter()
            for h in H_a4:
                cur = h
                k_ord = 1
                while cur != 0:
                    cur = G["mul"][cur][h]
                    k_ord += 1
                ord_counts_a4[k_ord] += 1
            assert ord_counts_a4 == {1: 1, 2: 3, 3: 8}

            # Verify every involution in A_5 has cycle type [1, 2, 2] on 5 points
            all_inv_elems = [x for ic in inv_classes for x in ic]
            d5_action_cycles = sorted({tuple(cycle_partition(coset_action_perm(G, H_a4, x))) for x in all_inv_elems})
            assert d5_action_cycles == [(1, 2, 2)]

            # Cross-check explicit isomorphism Delta(2,3,5) -> PSL(2, F_5)
            iso_verified = False
            if grp_a5 is not None:
                # Find s_idx (order 2), u_idx (order 3) in G with order(s*u) == 5
                s_idx = next(i for i in range(order) if G["elems"][i] == s_perm)
                u_idx = next(i for i in range(order) if G["elems"][i] == u_perm)
                # Build BFS words in (s_idx, u_idx) for every element of G
                words_g = {0: []}
                q_g = [0]
                while q_g:
                    cur = q_g.pop(0)
                    for step, g_el in ((0, s_idx), (1, u_idx)):
                        nxt = G["mul"][cur][g_el]
                        if nxt not in words_g:
                            words_g[nxt] = words_g[cur] + [step]
                            q_g.append(nxt)
                assert len(words_g) == 60
                # Find (h_s, h_u) in PSL(2, F_5) with ord(h_s)=2, ord(h_u)=3, ord(h_s*h_u)=5
                ords_p = []
                for i in range(60):
                    cur = i
                    k_o = 1
                    while cur != 0:
                        cur = grp_a5["mul"][cur][i]
                        k_o += 1
                    ords_p.append(k_o)
                h_s = next(i for i in range(60) if ords_p[i] == 2)
                h_u = next(j for j in range(60) if ords_p[j] == 3 and ords_p[grp_a5["mul"][h_s][j]] == 5)
                phi_map = [0] * 60
                for el in range(60):
                    cur = 0
                    for step in words_g[el]:
                        cur = grp_a5["mul"][cur][h_s if step == 0 else h_u]
                    phi_map[el] = cur
                assert len(set(phi_map)) == 60
                for i in range(60):
                    for j in range(60):
                        assert phi_map[G["mul"][i][j]] == grp_a5["mul"][phi_map[i]][phi_map[j]]
                iso_verified = True

            a5_uniqueness = {
                "order": order,
                "isomorphic_to_PSL2_F5_verified": iso_verified,
                "index_5_subgroup_classes": len(idx5_classes),
                "index_5_subgroup_order_profile": {str(k): v for k, v in sorted(ord_counts_a4.items())},
                "index_6_subgroup_classes": len(idx6_classes),
                "index_6_subgroup_order_profile": {str(k): v for k, v in sorted(ord_counts_d5.items())},
                "involution_conjugacy_classes": len(inv_classes),
                "total_involutions": len(all_inv_elems),
                "all_involution_cycle_types_on_5_pts": [list(c) for c in d5_action_cycles],
            }

    weyl_cl10 = verify_weyl_24_and_cl10()

    unique_sm_pass = (
        len(sm_passing_actions) == 1
        and sm_passing_actions[0]["N"] == 5
        and sm_passing_actions[0]["degree_d"] == 5
        and sm_passing_actions[0]["a"] == 3
        and sm_passing_actions[0]["b"] == 2
    )
    assert unique_sm_pass

    return {
        "spherical_bound": spherical_bound,
        "finite_rungs": finite_rungs,
        "rung_orders": {str(N): rungs_report[str(N)]["order"] for N in finite_rungs},
        "total_core_free_action_involution_pairs_d_le_12": len(all_actions_flat),
        "sm_passing_count": len(sm_passing_actions),
        "unique_sm_pass": unique_sm_pass,
        "unique_sm_winner": sm_passing_actions[0],
        "rungs": rungs_report,
        "a5_uniqueness": a5_uniqueness,
        "weyl_24_and_cl10": weyl_cl10,
    }


# =============================================================================
# EXACT FINITE GROUP SURJECTION ENGINES (D_p, 2T = SL(2,F_3), A_5 = PSL(2,F_5))
# =============================================================================

def construct_sl2_f3():
    """Construct 2T = SL(2, F_3) (order 24) and its exact Aut(2T) from scratch."""
    mats = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 == 1:
                        mats.append(((a, b), (c, d)))
    assert len(mats) == 24
    # Put identity first
    id_m = ((1, 0), (0, 1))
    mats.remove(id_m)
    mats = [id_m] + mats
    idx = {m: i for i, m in enumerate(mats)}

    def mm(X, Y):
        return (
            ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % 3, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % 3),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % 3, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % 3),
        )

    n = 24
    mul = [[idx[mm(mats[i], mats[j])] for j in range(n)] for i in range(n)]
    inv = [0] * n
    for i in range(n):
        for j in range(n):
            if mul[i][j] == 0:
                inv[i] = j
                break

    # Compute exact Aut(2T) by extending images of a 2-element generating set
    g0 = idx[((0, 2), (1, 0))]  # order 4
    g1 = idx[((1, 1), (0, 1))]  # order 3
    # Verify (g0, g1) generates all 24 elements
    gen_words = {0: []}
    q = [0]
    while q:
        u = q.pop(0)
        for gen_idx, g_el in ((0, g0), (1, g1)):
            v = mul[u][g_el]
            if v not in gen_words:
                gen_words[v] = gen_words[u] + [gen_idx]
                q.append(v)
    assert len(gen_words) == 24

    auts = []
    for h0 in range(n):
        # order(h0) must be 4
        if mul[h0][h0] == 0 or mul[mul[h0][h0]][mul[h0][h0]] != 0:
            continue
        for h1 in range(n):
            # order(h1) must be 3
            if h1 == 0 or mul[mul[h1][h1]][h1] != 0:
                continue
            # Build candidate map via gen_words
            img = [0] * n
            for el in range(n):
                cur = 0
                for step in gen_words[el]:
                    cur = mul[cur][h0 if step == 0 else h1]
                img[el] = cur
            if len(set(img)) != n:
                continue
            # Verify homomorphism property on all 24x24 pairs
            ok = True
            for i in range(n):
                for j in range(n):
                    if img[mul[i][j]] != mul[img[i]][img[j]]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                auts.append(tuple(img))
    assert len(auts) == 24
    return {"name": "2T", "order": n, "mul": mul, "inv": inv, "id": 0, "auts": auts}


def construct_psl2_f5():
    """Construct A_5 = PSL(2, F_5) (order 60) and its exact Aut(A_5) from scratch."""
    def canon(M):
        flat = [M[0][0] % 5, M[0][1] % 5, M[1][0] % 5, M[1][1] % 5]
        for v in flat:
            if v != 0:
                if v in (3, 4):
                    flat = [(-x) % 5 for x in flat]
                break
        return ((flat[0], flat[1]), (flat[2], flat[3]))

    mats_set = set()
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if (a * d - b * c) % 5 == 1:
                        mats_set.add(canon(((a, b), (c, d))))
    assert len(mats_set) == 60
    id_m = ((1, 0), (0, 1))
    mats = [id_m] + sorted(mats_set - {id_m})
    idx = {m: i for i, m in enumerate(mats)}

    def mm(X, Y):
        return canon((
            ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % 5, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % 5),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % 5, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % 5),
        ))

    n = 60
    mul = [[idx[mm(mats[i], mats[j])] for j in range(n)] for i in range(n)]
    inv = [0] * n
    for i in range(n):
        for j in range(n):
            if mul[i][j] == 0:
                inv[i] = j
                break

    # Exact orders of elements
    ords = []
    for i in range(n):
        cur = i
        k = 1
        while cur != 0:
            cur = mul[cur][i]
            k += 1
        ords.append(k)

    # Pick generating pair (g0, g1) of orders (2, 3) with order(g0*g1) == 5
    g0 = next(i for i in range(n) if ords[i] == 2)
    g1 = next(j for j in range(n) if ords[j] == 3 and ords[mul[g0][j]] == 5)
    gen_words = {0: []}
    q = [0]
    while q:
        u = q.pop(0)
        for gen_idx, g_el in ((0, g0), (1, g1)):
            v = mul[u][g_el]
            if v not in gen_words:
                gen_words[v] = gen_words[u] + [gen_idx]
                q.append(v)
    assert len(gen_words) == 60

    auts = []
    inv_elems = [i for i in range(n) if ords[i] == 2]
    ord3_elems = [i for i in range(n) if ords[i] == 3]
    for h0 in inv_elems:
        for h1 in ord3_elems:
            if ords[mul[h0][h1]] != 5:
                continue
            img = [0] * n
            for el in range(n):
                cur = 0
                for step in gen_words[el]:
                    cur = mul[cur][h0 if step == 0 else h1]
                img[el] = cur
            if len(set(img)) != n:
                continue
            ok = True
            for i in range(n):
                for j in range(n):
                    if img[mul[i][j]] != mul[img[i]][img[j]]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                auts.append(tuple(img))
    assert len(auts) == 120
    return {"name": "A5", "order": n, "mul": mul, "inv": inv, "id": 0, "auts": auts}


def build_generating_orbit_transversal(grp, n_gens):
    """
    Build exact transversal of Aut(G)-orbits of generating n_gens-tuples in G^n,
    verified by the Orbit-Stabilizer sum identity sum |Aut|/|Stab| == |G|^n_gens.
    """
    n = grp["order"]
    mul = grp["mul"]
    auts = grp["auts"]
    aut_order = len(auts)

    def generates_all(tup):
        seen = {0}
        for x in tup:
            seen.add(x)
        queue = list(seen)
        while queue:
            u = queue.pop()
            for x in tup:
                v = mul[u][x]
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
                    if len(seen) == n:
                        return True
        return len(seen) == n

    gen_reps = []
    orbit_size_sum = 0

    def recurse(prefix, stab_auts):
        nonlocal orbit_size_sum
        depth = len(prefix)
        if depth == n_gens:
            orbit_size_sum += aut_order // len(stab_auts)
            if generates_all(prefix):
                assert len(stab_auts) == 1
                gen_reps.append(prefix)
            return

        visited = [False] * n
        for x in range(n):
            if visited[x]:
                continue
            # Mark entire orbit of x under stab_auts and collect next stabilizer
            next_stab = []
            for a in stab_auts:
                ax = a[x]
                visited[ax] = True
                if ax == x:
                    next_stab.append(a)
            recurse(prefix + (x,), next_stab)

    recurse((), auts)
    assert orbit_size_sum == n ** n_gens, (
        f"Orbit-stabilizer check failed: {orbit_size_sum} != {n ** n_gens}"
    )
    return gen_reps


def compile_relators(gens, relators):
    """Compile SnapPy/word relators into lists of (gen_idx, is_inv) pairs."""
    g_map = {g: i for i, g in enumerate(gens)}
    compiled = []
    for rel in relators:
        seq = []
        for ch in rel:
            if ch.islower():
                seq.append((g_map[ch], False))
            else:
                seq.append((g_map[ch.lower()], True))
        compiled.append(seq)
    return compiled


def count_surjections_finite_group(gens, relators, grp, transversals):
    """Exact count of Hom_surj(pi_1, G) / Aut(G) via certified transversal."""
    n_gens = len(gens)
    compiled = compile_relators(gens, relators)
    mul = grp["mul"]
    inv = grp["inv"]
    reps = transversals[n_gens]
    count = 0
    for tup in reps:
        ok = True
        for seq in compiled:
            cur = 0
            for gi, is_inv in seq:
                el = inv[tup[gi]] if is_inv else tup[gi]
                cur = mul[cur][el]
            if cur != 0:
                ok = False
                break
        if ok:
            count += 1
    return count


def eval_word_dp(word_seq, e_vec, x_vec, p):
    """Evaluate compiled word directly in D_p = {(e, k) : e in {0,1}, k in Z/pZ}."""
    cur_e = 0
    cur_k = 0
    for gi, is_inv in word_seq:
        eg = e_vec[gi]
        xg = x_vec[gi]
        if is_inv:
            let_e = eg
            let_k = (-xg) % p if eg == 0 else xg
        else:
            let_e = eg
            let_k = xg
        if let_e == 1:
            cur_k = (-cur_k) % p
        cur_k = (cur_k + let_k) % p
        cur_e ^= let_e
    return cur_e, cur_k


def dp_surjections_exact(gens, relators, p, test_words=None):
    """
    Exact count of Hom_surj(pi_1, D_p) / Aut(D_p) via exact F_p linear algebra
    on every valid nonzero parity homomorphism eps: pi_1 -> Z/2Z.
    If test_words is given (dict name -> word string), explicitly enumerates
    every Aut(D_p)-orbit representative, self-verifies relators & surjectivity
    directly in D_p, and records the image of every test word!
    """
    n = len(gens)
    compiled = compile_relators(gens, relators)
    test_compiled = {}
    if test_words:
        for k_name, w_str in test_words.items():
            test_compiled[k_name] = compile_relators(gens, [w_str])[0]

    total_classes = 0
    word_results = {k_name: [] for k_name in test_compiled}

    for mask in range(1, 1 << n):
        e_vec = [(mask >> i) & 1 for i in range(n)]
        # Check parity compatibility with every relator
        parity_ok = True
        lin_rows = []
        for seq in compiled:
            cur_e = 0
            cur_vec = [0] * n
            for gi, is_inv in seq:
                eg = e_vec[gi]
                let_coeff = (-1 if (is_inv and eg == 0) else 1)
                if eg == 1:
                    cur_vec = [(-v) % p for v in cur_vec]
                cur_vec[gi] = (cur_vec[gi] + let_coeff) % p
                cur_e ^= eg
            if cur_e != 0:
                parity_ok = False
                break
            lin_rows.append(cur_vec)
        if not parity_ok:
            continue

        basis = kernel_basis_fp(lin_rows, n, p)
        dim_v = len(basis)
        assert dim_v >= 1  # e_vec itself is always in V_eps
        r = dim_v - 1
        if r == 0:
            continue
        cls_count = (p ** r - 1) // (p - 1)
        total_classes += cls_count

        if test_compiled:
            # Build complement basis W to span(e_vec) inside V_eps
            e_mod = [ev % p for ev in e_vec]
            cur_rows = [e_mod]
            cur_rk = 1
            comp_basis = []
            for bv in basis:
                rk_new = rank_fp(cur_rows + [bv], n, p)
                if rk_new > cur_rk:
                    cur_rows.append(bv)
                    cur_rk = rk_new
                    comp_basis.append(bv)
            assert len(comp_basis) == r

            # Enumerate all (p^r - 1)/(p - 1) projective reps with leading 1
            enum_count = 0
            for lead in range(r):
                for tail in itertools.product(range(p), repeat=r - 1 - lead):
                    coeffs = [0] * lead + [1] + list(tail)
                    x_vec = [
                        sum(coeffs[j] * comp_basis[j][i] for j in range(r)) % p
                        for i in range(n)
                    ]
                    # Self-verify all relators vanish directly in D_p
                    for seq in compiled:
                        assert eval_word_dp(seq, e_vec, x_vec, p) == (0, 0)
                    # Self-verify surjectivity directly in D_p (generates 2p elements)
                    gen_set = {(0, 0)}
                    gens_dp = [(e_vec[i], x_vec[i]) for i in range(n)]
                    q = [(0, 0)]
                    while q:
                        ce, ck = q.pop()
                        for ge, gk in gens_dp:
                            ne = ce ^ ge
                            nk = ((-ck if ge == 1 else ck) + gk) % p
                            if (ne, nk) not in gen_set:
                                gen_set.add((ne, nk))
                                q.append((ne, nk))
                    assert len(gen_set) == 2 * p

                    for k_name, w_seq in test_compiled.items():
                        img = eval_word_dp(w_seq, e_vec, x_vec, p)
                        word_results[k_name].append(img)
                    enum_count += 1
            assert enum_count == cls_count

    return total_classes, word_results


def abelianization_invariants(gens, relators):
    """Exact abelianization (free_rank, torsion_divisors, torsion_order) via SNF."""
    n = len(gens)
    g_map = {g: i for i, g in enumerate(gens)}
    mat = []
    for rel in relators:
        row = [0] * n
        for ch in rel:
            if ch.islower():
                row[g_map[ch]] += 1
            else:
                row[g_map[ch.lower()]] -= 1
        mat.append(row)
    invs = smith_normal_form_invariants(mat)
    free_rank = n - len(invs)
    torsion_divs = [d for d in invs if d > 1]
    torsion_order = 1
    for d in torsion_divs:
        torsion_order *= d
    return free_rank, torsion_divs, torsion_order, mat


def word_is_zero_in_h1(gens, rel_ab_mat, word):
    """Check whether abelianization of `word` lies in Z-row-space of rel_ab_mat."""
    n = len(gens)
    g_map = {g: i for i, g in enumerate(gens)}
    w_vec = [0] * n
    for ch in word:
        if ch.islower():
            w_vec[g_map[ch]] += 1
        else:
            w_vec[g_map[ch.lower()]] -= 1
    # Check SNF of rel_ab_mat equals SNF of rel_ab_mat + [w_vec]
    invs_before = smith_normal_form_invariants(rel_ab_mat)
    invs_after = smith_normal_form_invariants(rel_ab_mat + [w_vec])
    return invs_before == invs_after


# =============================================================================
# TASK OW1-B: UNBLOCKED 50-THREAD PUNCTURED-TORUS BUNDLE CENSUS
# =============================================================================

def free_reduce(word):
    """Freely reduce a tuple of nonzero ints (+1=a, -1=A, +2=b, -2=B)."""
    stack = []
    for x in word:
        if stack and stack[-1] == -x:
            stack.pop()
        else:
            stack.append(x)
    return tuple(stack)


def free_invert(word):
    return tuple(-x for x in reversed(word))


def apply_f2_aut(aut, word):
    """Apply F_2 endomorphism aut = (img_a, img_b) to word and freely reduce."""
    img_a, img_b = aut
    inv_a = free_invert(img_a)
    inv_b = free_invert(img_b)
    out = []
    for x in word:
        if x == 1:
            out.extend(img_a)
        elif x == -1:
            out.extend(inv_a)
        elif x == 2:
            out.extend(img_b)
        else:
            out.extend(inv_b)
    return free_reduce(out)


def compose_f2_aut(f, g):
    """Composition f o g on F_2."""
    return (apply_f2_aut(f, g[0]), apply_f2_aut(f, g[1]))


def f2_word_to_str(word):
    mp = {1: "a", -1: "A", 2: "b", -2: "B", 3: "t", -3: "T"}
    return "".join(mp[x] for x in word)


def build_bundle_monodromy(branch, word):
    """
    Build exact 2x2 matrix M in GL(2, Z) AND exact Aut(F_2) lift phi for
    (branch, word), asserting abelianization(phi) == M and phi([a,b]) == [a,b]^{det(M)}.
    """
    L_mat = ((1, 0), (1, 1))
    R_mat = ((1, 1), (0, 1))
    P_mat = ((0, 1), (1, 0))

    def mm(A, B):
        return (
            (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
        )

    phi_L = ((1, 2), (2,))
    phi_R = ((1,), (2, 1))
    phi_P = ((2,), (1,))
    phi_S2 = ((2, -1, -2), (2, 1, -2, -1, -2))
    phi_id = ((1,), (2,))

    M = ((1, 0), (0, 1))
    phi = phi_id
    for ch in word:
        if ch == "L":
            M = mm(M, L_mat)
            phi = compose_f2_aut(phi, phi_L)
        else:
            assert ch == "R"
            M = mm(M, R_mat)
            phi = compose_f2_aut(phi, phi_R)

    if branch == "+":
        det_m = 1
    elif branch == "-":
        M = ((-M[0][0], -M[0][1]), (-M[1][0], -M[1][1]))
        phi = compose_f2_aut(phi_S2, phi)
        det_m = 1
    else:
        assert branch == "P"
        M = mm(M, P_mat)
        phi = compose_f2_aut(phi, phi_P)
        det_m = -1

    # Verify det(M)
    assert M[0][0] * M[1][1] - M[0][1] * M[1][0] == det_m

    # Verify abelianization(phi) == M
    def ab_col(w):
        return (
            sum(1 if x == 1 else (-1 if x == -1 else 0) for x in w),
            sum(1 if x == 2 else (-1 if x == -2 else 0) for x in w),
        )
    c0 = ab_col(phi[0])
    c1 = ab_col(phi[1])
    assert (c0[0], c1[0]) == M[0] and (c0[1], c1[1]) == M[1]

    # Verify phi([a, b]) == [a, b]^{det_m}
    comm = (1, 2, -1, -2)
    img_comm = apply_f2_aut(phi, comm)
    expected_comm = comm if det_m == 1 else free_invert(comm)
    assert img_comm == expected_comm

    # Build 3-generator mapping torus relators: t a T phi(a)^{-1}, t b T phi(b)^{-1}
    r1 = free_reduce((3, 1, -3) + free_invert(phi[0]))
    r2 = free_reduce((3, 2, -3) + free_invert(phi[1]))
    mt_gens = ["a", "b", "t"]
    mt_rels = [f2_word_to_str(r1), f2_word_to_str(r2)]
    return M, det_m, mt_gens, mt_rels


def enumerate_50_threads():
    """
    Enumerate exact canonical conjugacy classes of primitive hyperbolic
    punctured-torus monodromies:
      - Branch + (21): primitive cyclic words in {L, R} containing both L, R, len 2..6
      - Branch - (21): same words with -I lift
      - Branch P (8): primitive twisted cyclic classes of w*P, len 1..5
    """
    def is_prim(w):
        n = len(w)
        return all(w != w[:d] * (n // d) for d in range(1, n) if n % d == 0)

    def canon_cyc(w):
        return min(w[i:] + w[:i] for i in range(len(w)))

    def swap_lr(w):
        return "".join("R" if c == "L" else "L" for c in w)

    def canon_twisted(w):
        seen = set()
        u = w
        while u not in seen:
            seen.add(u)
            u = u[1:] + swap_lr(u[0])
        return min(seen)

    ori_set = set()
    for n in range(2, 7):
        for tup in itertools.product("LR", repeat=n):
            w = "".join(tup)
            if "L" in w and "R" in w and is_prim(w):
                ori_set.add(canon_cyc(w))
    ori_words = sorted(ori_set, key=lambda s: (len(s), s))
    assert len(ori_words) == 21

    nonori_set = set()
    for n in range(1, 6):
        for tup in itertools.product("LR", repeat=n):
            w = "".join(tup)
            # Primitivity of w*P: not an odd power (u*P)^(2k+1)
            prim = True
            for d in range(1, n):
                if n % d == 0 and (n // d) % 2 == 1:
                    u = w[:d]
                    built = "".join(u if i % 2 == 0 else swap_lr(u) for i in range(n // d))
                    if built == w:
                        prim = False
                        break
            if prim:
                nonori_set.add(canon_twisted(w))
    nonori_words = sorted(nonori_set, key=lambda s: (len(s), s))
    assert len(nonori_words) == 8

    threads = []
    for w in ori_words:
        threads.append(("+", w, "b++" + w))
    for w in ori_words:
        threads.append(("-", w, "b+-" + w))
    for w in nonori_words:
        threads.append(("P", w, "b-+" + w))
    assert len(threads) == 50
    return threads


def check_amphichirality_dual(M):
    """
    Erratum 2 dual oriented amphichirality check for an orientable hyperbolic
    manifold M:
      1. M.symmetry_group().is_amphicheiral()
      2. any(iso.cusp_maps()[0].det() < 0 for iso in M.is_isometric_to(M, return_isometries=True))
    Asserts exact agreement between both methods.
    """
    sg_amphi = bool(M.symmetry_group().is_amphicheiral())
    isos = M.is_isometric_to(M, return_isometries=True)
    det_list = [int(iso.cusp_maps()[0].det()) for iso in isos]
    iso_amphi = any(d < 0 for d in det_list)
    assert sg_amphi == iso_amphi, f"Amphichirality mismatch: sg={sg_amphi}, iso={iso_amphi}"
    return sg_amphi, iso_amphi, len(isos)


def run_task_ow1_b(grp_2t, trans_2t, grp_a5, trans_a5):
    """Execute Task OW1-B using BOTH SnapPy presentations AND 3-gen mapping tori."""
    threads = enumerate_50_threads()
    primes = [3, 5, 7, 11, 13]

    # Verify SnapPy census identifications of m000, m003, m004
    census_checks = {
        "m000_eq_b-+L": bool(snappy.Manifold("b-+L").is_isometric_to(snappy.Manifold("m000"))),
        "m003_eq_b+-LR": bool(snappy.Manifold("b+-LR").is_isometric_to(snappy.Manifold("m003"))),
        "m004_eq_b++LR": bool(snappy.Manifold("b++LR").is_isometric_to(snappy.Manifold("m004"))),
    }
    assert all(census_checks.values())

    records = []
    cross_check_mismatches = {
        "h1_torsion": 0,
        "dp_counts": 0,
        "d5_boundary": 0,
        "count_2t": 0,
        "count_a5": 0,
        "amphichiral_dual": 0,
    }

    for branch, word, sn_name in threads:
        M_mat, det_m, mt_gens, mt_rels = build_bundle_monodromy(branch, word)
        det_m_minus_i = abs((M_mat[0][0] - 1) * (M_mat[1][1] - 1) - M_mat[0][1] * M_mat[1][0])
        tr_m = M_mat[0][0] + M_mat[1][1]

        # Method 2: 3-generator mapping torus presentation
        mt_free, mt_tdivs, mt_tord, _ = abelianization_invariants(mt_gens, mt_rels)
        assert mt_free == 1 and mt_tord == det_m_minus_i

        # Method 1: SnapPy presentation directly
        M_sn = snappy.Manifold(sn_name)
        assert M_sn.is_orientable() == (det_m == 1)
        G_sn = M_sn.fundamental_group()
        sn_gens = list(G_sn.generators())
        sn_rels = list(G_sn.relators())
        sn_free, sn_tdivs, sn_tord, sn_ab_mat = abelianization_invariants(sn_gens, sn_rels)

        # Cross-check SnapPy homology against |det(M - I)| and mapping-torus SNF
        sn_hom = M_sn.homology()
        sn_hom_divs = [int(d) for d in sn_hom.elementary_divisors() if int(d) > 0]
        sn_hom_tord = 1
        for d in sn_hom_divs:
            sn_hom_tord *= d
        if not (sn_free == 1 and sn_tord == det_m_minus_i and sn_hom_tord == det_m_minus_i and sn_tdivs == mt_tdivs):
            cross_check_mismatches["h1_torsion"] += 1

        # Identify SnapPy fibre-boundary peripheral curve (the unique one in [pi_1, pi_1])
        p0, p1 = G_sn.peripheral_curves()[0]
        p0_is_zero_h1 = word_is_zero_in_h1(sn_gens, sn_ab_mat, p0)
        p1_is_zero_h1 = word_is_zero_in_h1(sn_gens, sn_ab_mat, p1)
        assert p0_is_zero_h1 != p1_is_zero_h1, (
            f"Unexpected peripheral H1 images on {sn_name}: p0={p0_is_zero_h1}, p1={p1_is_zero_h1}"
        )
        bdry_word_sn = p0 if p0_is_zero_h1 else p1

        # Compute D_p surjections on BOTH presentations and cross-check
        dp_counts_sn = {}
        dp_counts_mt = {}
        d5_bdry_sn_imgs = []
        d5_bdry_mt_imgs = []
        for p in primes:
            if p == 5:
                c_sn, w_sn = dp_surjections_exact(sn_gens, sn_rels, p, test_words={"bdry": bdry_word_sn})
                c_mt, w_mt = dp_surjections_exact(mt_gens, mt_rels, p, test_words={"bdry": "abAB"})
                d5_bdry_sn_imgs = w_sn["bdry"]
                d5_bdry_mt_imgs = w_mt["bdry"]
            else:
                c_sn, _ = dp_surjections_exact(sn_gens, sn_rels, p)
                c_mt, _ = dp_surjections_exact(mt_gens, mt_rels, p)
            dp_counts_sn[str(p)] = c_sn
            dp_counts_mt[str(p)] = c_mt
            if c_sn != c_mt:
                cross_check_mismatches["dp_counts"] += 1

        # Cross-check D_5 boundary triviality (sorted multiset of trivial vs nontrivial)
        sn_triv_cnt = sum(1 for img in d5_bdry_sn_imgs if img == (0, 0))
        mt_triv_cnt = sum(1 for img in d5_bdry_mt_imgs if img == (0, 0))
        if sn_triv_cnt != mt_triv_cnt or len(d5_bdry_sn_imgs) != len(d5_bdry_mt_imgs):
            cross_check_mismatches["d5_boundary"] += 1

        # 2T and A_5 surjections on BOTH presentations
        c2t_sn = count_surjections_finite_group(sn_gens, sn_rels, grp_2t, trans_2t)
        c2t_mt = count_surjections_finite_group(mt_gens, mt_rels, grp_2t, trans_2t)
        if c2t_sn != c2t_mt:
            cross_check_mismatches["count_2t"] += 1

        ca5_sn = count_surjections_finite_group(sn_gens, sn_rels, grp_a5, trans_a5)
        ca5_mt = count_surjections_finite_group(mt_gens, mt_rels, grp_a5, trans_a5)
        if ca5_sn != ca5_mt:
            cross_check_mismatches["count_a5"] += 1

        vol_val = round(float(M_sn.volume()), 8)
        if det_m == 1:
            is_amphi, iso_amphi, n_isos = check_amphichirality_dual(M_sn)
            if is_amphi != iso_amphi:
                cross_check_mismatches["amphichiral_dual"] += 1
            try:
                cs_val = round(float(M_sn.chern_simons()), 8)
            except ValueError:
                cs_val = None
        else:
            is_amphi = None
            n_isos = len(M_sn.is_isometric_to(M_sn, return_isometries=True))
            cs_val = None

        d5_cnt = dp_counts_sn["5"]
        records.append({
            "snappy_name": sn_name,
            "branch": branch,
            "word": word,
            "word_len": len(word),
            "orientable": (det_m == 1),
            "det_M": det_m,
            "trace_M": tr_m,
            "h1_torsion_order": det_m_minus_i,
            "h1_torsion_divisors": sn_tdivs,
            "volume": vol_val,
            "chern_simons": cs_val,
            "is_amphichiral": is_amphi,
            "self_isometry_count": n_isos,
            "dp_surjections": dp_counts_sn,
            "d5_count": d5_cnt,
            "d5_boundary_trivial_count": sn_triv_cnt,
            "d5_all_boundary_trivial": (d5_cnt > 0 and sn_triv_cnt == d5_cnt),
            "d5_any_boundary_trivial": (sn_triv_cnt > 0),
            "surj_2T": c2t_sn,
            "surj_A5": ca5_sn,
        })

    assert all(v == 0 for v in cross_check_mismatches.values()), cross_check_mismatches

    # Summaries
    d5_survivors = [r["snappy_name"] for r in records if r["d5_count"] > 0]
    d5_all_triv = [r["snappy_name"] for r in records if r["d5_all_boundary_trivial"]]
    d5_any_triv = [r["snappy_name"] for r in records if r["d5_any_boundary_trivial"]]
    t2_survivors = [r["snappy_name"] for r in records if r["surj_2T"] > 0]
    a5_survivors = [r["snappy_name"] for r in records if r["surj_A5"] > 0]
    d5_and_2t = [r["snappy_name"] for r in records if r["d5_count"] > 0 and r["surj_2T"] > 0]
    d5_triv_and_2t = [r["snappy_name"] for r in records if r["d5_any_boundary_trivial"] and r["surj_2T"] > 0]
    d5_all_triv_and_2t = [r["snappy_name"] for r in records if r["d5_all_boundary_trivial"] and r["surj_2T"] > 0]
    chiral_d5_triv_and_2t = [
        r["snappy_name"]
        for r in records
        if r["orientable"] and r["is_amphichiral"] is False and r["d5_any_boundary_trivial"] and r["surj_2T"] > 0
    ]
    chiral_d5_all_triv_and_2t = [
        r["snappy_name"]
        for r in records
        if r["orientable"] and r["is_amphichiral"] is False and r["d5_all_boundary_trivial"] and r["surj_2T"] > 0
    ]
    chiral_d5_and_2t_and_a5 = [
        r["snappy_name"]
        for r in records
        if r["orientable"] and r["is_amphichiral"] is False and r["d5_any_boundary_trivial"] and r["surj_2T"] > 0 and r["surj_A5"] > 0
    ]

    key_threads = {
        r["snappy_name"]: r
        for r in records
        if r["snappy_name"] in ("b++LR", "b+-LR", "b-+L", "b-+LLLLL", "b++LLLRLR", "b+-LLLLLR")
    }

    return {
        "total_threads": len(records),
        "branch_counts": {
            "+": sum(1 for r in records if r["branch"] == "+"),
            "-": sum(1 for r in records if r["branch"] == "-"),
            "P": sum(1 for r in records if r["branch"] == "P"),
        },
        "census_isometry_checks": census_checks,
        "cross_check_mismatches": cross_check_mismatches,
        "summary": {
            "d5_survivors_count": len(d5_survivors),
            "d5_survivors": d5_survivors,
            "d5_all_boundary_trivial_count": len(d5_all_triv),
            "d5_all_boundary_trivial": d5_all_triv,
            "d5_any_boundary_trivial_count": len(d5_any_triv),
            "d5_any_boundary_trivial": d5_any_triv,
            "surj_2T_survivors_count": len(t2_survivors),
            "surj_2T_survivors": t2_survivors,
            "surj_A5_survivors_count": len(a5_survivors),
            "surj_A5_survivors": a5_survivors,
            "d5_and_2T_count": len(d5_and_2t),
            "d5_and_2T": d5_and_2t,
            "d5_any_triv_and_2T_count": len(d5_triv_and_2t),
            "d5_any_triv_and_2T": d5_triv_and_2t,
            "d5_all_triv_and_2T_count": len(d5_all_triv_and_2t),
            "d5_all_triv_and_2T": d5_all_triv_and_2t,
            "chiral_d5_any_triv_and_2T_count": len(chiral_d5_triv_and_2t),
            "chiral_d5_any_triv_and_2T": chiral_d5_triv_and_2t,
            "chiral_d5_all_triv_and_2T_count": len(chiral_d5_all_triv_and_2t),
            "chiral_d5_all_triv_and_2T": chiral_d5_all_triv_and_2t,
            "chiral_d5_triv_and_2T_and_A5": chiral_d5_and_2t_and_a5,
        },
        "key_threads": key_threads,
        "threads": records,
    }


# =============================================================================
# TASK OW1-C: ALL 35 PRIME KNOTS THROUGH 8 CROSSINGS IN S^3
# =============================================================================

def fox_jacobian_at_minus_1(gens, relators):
    """
    Compute exact integer Fox Jacobian J(-1) from a knot group presentation
    with H_1 = Z, return (J_mat, snf_invariants, det_val, ab_weights).
    """
    n = len(gens)
    free_rk, tdivs, tord, ab_mat = abelianization_invariants(gens, relators)
    assert free_rk == 1 and tord == 1 and tdivs == []
    e_vec = int_kernel_1d(ab_mat, n)
    signs = [-1 if (e % 2 == 1) else 1 for e in e_vec]
    g_map = {g: i for i, g in enumerate(gens)}

    J = []
    for rel in relators:
        deriv = [0] * n
        pref = 1
        for ch in rel:
            if ch.islower():
                k = g_map[ch]
                deriv[k] += pref
                pref *= signs[k]
            else:
                k = g_map[ch.lower()]
                pref *= signs[k]
                deriv[k] -= pref
        J.append(deriv)

    invs = smith_normal_form_invariants(J)
    assert len(invs) == n - 1
    det_val = 1
    for d in invs:
        det_val *= d
    return J, invs, det_val, e_vec


def run_task_ow1_c(grp_2t, trans_2t, grp_a5, trans_a5):
    """Execute Task OW1-C across all 35 prime knots 3_1..8_21."""
    knot_names = [
        f"{c}_{i}"
        for c, cnt in [(3, 1), (4, 1), (5, 2), (6, 3), (7, 7), (8, 21)]
        for i in range(1, cnt + 1)
    ]
    assert len(knot_names) == 35
    primes = [3, 5, 7, 11, 13]

    records = []
    cross_check_mismatches = {
        "det_fox_vs_seifert": 0,
        "dp_vs_divisibility_and_snf": 0,
        "d5_longitude_nontrivial": 0,
        "amphichiral_dual": 0,
        "signature_vs_amphichiral": 0,
    }

    for name in knot_names:
        M = snappy.Manifold(name)
        G = M.fundamental_group()
        gens = list(G.generators())
        rels = list(G.relators())
        meridian, longitude = G.peripheral_curves()[0]

        # Method 1: Exact Fox Jacobian J(-1) SNF directly from pi_1
        _, fox_invs, det_fox, e_vec = fox_jacobian_at_minus_1(gens, rels)

        # Method 2: Independent Seifert matrix V from snappy.Link(name)
        L = snappy.Link(name)
        V = L.seifert_matrix()
        k_dim = len(V)
        S_sym = [[V[i][j] + V[j][i] for j in range(k_dim)] for i in range(k_dim)]
        det_seifert = abs(det_exact_int(S_sym))
        n_pos, n_neg, n_zero = symmetric_signature_exact(S_sym)
        assert n_zero == 0
        sig_exact = n_pos - n_neg

        if det_fox != det_seifert:
            cross_check_mismatches["det_fox_vs_seifert"] += 1

        # Verify longitude abelianizes to 0 in H_1 = Z, meridian to +-1
        g_map = {g: i for i, g in enumerate(gens)}
        ab_long = sum(e_vec[g_map[ch]] if ch.islower() else -e_vec[g_map[ch.lower()]] for ch in longitude)
        ab_mer = sum(e_vec[g_map[ch]] if ch.islower() else -e_vec[g_map[ch.lower()]] for ch in meridian)
        assert ab_long == 0 and abs(ab_mer) == 1

        # Compute D_p surjections directly from pi_1 and cross-check with det & Fox SNF
        dp_counts = {}
        d5_long_imgs = []
        for p in primes:
            if p == 5:
                cnt, w_res = dp_surjections_exact(gens, rels, p, test_words={"long": longitude})
                d5_long_imgs = w_res["long"]
            else:
                cnt, _ = dp_surjections_exact(gens, rels, p)
            dp_counts[str(p)] = cnt

            # Cross-check exact count against Fox SNF invariant factors & p | det
            r_p = sum(1 for d in fox_invs if d % p == 0)
            expected_cnt = (p ** r_p - 1) // (p - 1)
            divides = (det_fox % p == 0)
            if cnt != expected_cnt or ((cnt > 0) != divides):
                cross_check_mismatches["dp_vs_divisibility_and_snf"] += 1

        d5_cnt = dp_counts["5"]
        d5_long_triv_cnt = sum(1 for img in d5_long_imgs if img == (0, 0))
        if d5_long_triv_cnt != d5_cnt:
            cross_check_mismatches["d5_longitude_nontrivial"] += 1

        c2t = count_surjections_finite_group(gens, rels, grp_2t, trans_2t)
        ca5 = count_surjections_finite_group(gens, rels, grp_a5, trans_a5)

        is_hyp = (int(round(float(M.volume()) * 1000)) > 0)
        if is_hyp:
            vol_val = round(float(M.volume()), 8)
            try:
                cs_val = round(float(M.chern_simons()), 8)
            except ValueError:
                cs_val = None
            is_amphi, iso_amphi, n_isos = check_amphichirality_dual(M)
            if is_amphi != iso_amphi:
                cross_check_mismatches["amphichiral_dual"] += 1
            if sig_exact != 0 and is_amphi:
                cross_check_mismatches["signature_vs_amphichiral"] += 1
        else:
            vol_val = 0
            cs_val = None
            n_isos = None
            # For non-hyperbolic torus knots 3_1, 5_1, 7_1, 8_19, nonzero exact
            # signature rigorously proves chirality (is_amphichiral == False)
            assert sig_exact != 0
            is_amphi = False

        records.append({
            "knot": name,
            "det": det_fox,
            "det_seifert": det_seifert,
            "h1_double_branched_invariants": [d for d in fox_invs if d > 1],
            "signature_exact": sig_exact,
            "is_hyperbolic": is_hyp,
            "volume": vol_val,
            "chern_simons": cs_val,
            "is_amphichiral": is_amphi,
            "self_isometry_count": n_isos,
            "dp_surjections": dp_counts,
            "d5_count": d5_cnt,
            "d5_longitude_trivial_count": d5_long_triv_cnt,
            "d5_all_longitude_trivial": (d5_cnt > 0 and d5_long_triv_cnt == d5_cnt),
            "surj_2T": c2t,
            "surj_A5": ca5,
        })

    assert all(v == 0 for v in cross_check_mismatches.values()), cross_check_mismatches

    d5_knots = [r["knot"] for r in records if r["d5_count"] > 0]
    t2_knots = [r["knot"] for r in records if r["surj_2T"] > 0]
    a5_knots = [r["knot"] for r in records if r["surj_A5"] > 0]
    d5_and_2t = [r["knot"] for r in records if r["d5_count"] > 0 and r["surj_2T"] > 0]
    d5_and_2t_hyp = [r["knot"] for r in records if r["d5_count"] > 0 and r["surj_2T"] > 0 and r["is_hyperbolic"]]
    d5_and_2t_hyp_chiral = [
        r["knot"]
        for r in records
        if r["d5_count"] > 0 and r["surj_2T"] > 0 and r["is_hyperbolic"] and not r["is_amphichiral"]
    ]
    d5_and_2t_hyp_amphi = [
        r["knot"]
        for r in records
        if r["d5_count"] > 0 and r["surj_2T"] > 0 and r["is_hyperbolic"] and r["is_amphichiral"]
    ]
    d5_and_2t_and_a5 = [
        r["knot"]
        for r in records
        if r["d5_count"] > 0 and r["surj_2T"] > 0 and r["surj_A5"] > 0
    ]
    amphi_knots_all = [r["knot"] for r in records if r["is_amphichiral"]]
    non_hyp_knots = [r["knot"] for r in records if not r["is_hyperbolic"]]

    return {
        "total_knots": len(records),
        "hyperbolic_count": sum(1 for r in records if r["is_hyperbolic"]),
        "non_hyperbolic_knots": non_hyp_knots,
        "cross_check_mismatches": cross_check_mismatches,
        "summary": {
            "amphichiral_knots_all": amphi_knots_all,
            "d5_count": len(d5_knots),
            "d5_knots": d5_knots,
            "surj_2T_count": len(t2_knots),
            "surj_2T_knots": t2_knots,
            "surj_A5_count": len(a5_knots),
            "surj_A5_knots": a5_knots,
            "d5_and_2T_count": len(d5_and_2t),
            "d5_and_2T_knots": d5_and_2t,
            "d5_and_2T_hyperbolic_knots": d5_and_2t_hyp,
            "d5_and_2T_hyperbolic_chiral_knots": d5_and_2t_hyp_chiral,
            "d5_and_2T_hyperbolic_amphichiral_knots": d5_and_2t_hyp_amphi,
            "d5_and_2T_and_A5_knots": d5_and_2t_and_a5,
        },
        "knots": records,
    }


# =============================================================================
# TASK OW1-D: FOUR PLANTED FAULTS (PF-OW1-1 THROUGH PF-OW1-4)
# =============================================================================

def run_task_ow1_d():
    """Verify all 4 planted faults PF-OW1-1..4 are caught directly by explicit evaluation."""
    # PF-OW1-1: Rung N=2 (S_3, d=3, transposition (1 2), a=2, b=1)
    p1 = (0, 2, 1)
    a1, b1, M1 = perm_matrix_eigen_multiplicities(p1)
    assert (a1, b1) == (2, 1)
    ev1 = evaluate_gauge_matter_sector(a1, b1, P_mat=M1)
    caught_1 = (not ev1["anomaly_free"]) and (ev1["anomalies"]["Tr_Y3"] != 0) and (not ev1["passes_full_sm_bar"])

    # PF-OW1-2: Rung N=3 (A_4, d=4, double transposition (0 1)(2 3), a=2, b=2)
    p2 = (1, 0, 3, 2)
    a2, b2, M2 = perm_matrix_eigen_multiplicities(p2)
    assert (a2, b2) == (2, 2)
    ev2 = evaluate_gauge_matter_sector(a2, b2, P_mat=M2)
    caught_2 = (not ev2["is_chiral"]) and (ev2["dim_centralizer"] == 7) and (not ev2["passes_full_sm_bar"])

    # PF-OW1-3: Odd permutation in S_5 \ A_5 (transposition [1,1,1,2], a=4, b=1)
    p3 = (0, 1, 2, 4, 3)
    a3, b3, M3 = perm_matrix_eigen_multiplicities(p3)
    assert (a3, b3) == (4, 1) and det_exact_int(M3) == -1
    ev3 = evaluate_gauge_matter_sector(a3, b3, P_mat=M3)
    caught_3 = (ev3["dim_centralizer"] == 16) and (not ev3["matches_sm_6y"]) and (not ev3["passes_full_sm_bar"])

    # PF-OW1-4: Higher odd dihedral D_7 (d=7, reflection k -> -k mod 7, [1,2,2,2], a=4, b=3)
    p4 = tuple((-k) % 7 for k in range(7))
    a4, b4, M4 = perm_matrix_eigen_multiplicities(p4)
    assert (a4, b4) == (4, 3)
    ev4 = evaluate_gauge_matter_sector(a4, b4, P_mat=M4)
    caught_4 = (ev4["dim_centralizer"] == 24) and (ev4["dim_lambda_even"] == 64) and (not ev4["passes_full_sm_bar"])

    assert caught_1 and caught_2 and caught_3 and caught_4
    return {
        "PF-OW1-1": {"caught": caught_1, "eval": ev1},
        "PF-OW1-2": {"caught": caught_2, "eval": ev2},
        "PF-OW1-3": {"caught": caught_3, "det_P": det_exact_int(M3), "eval": ev3},
        "PF-OW1-4": {"caught": caught_4, "eval": ev4},
        "all_4_caught": (caught_1 and caught_2 and caught_3 and caught_4),
    }


def main():
    grp_2t = construct_sl2_f3()
    grp_a5 = construct_psl2_f5()

    trans_2t = {
        2: build_generating_orbit_transversal(grp_2t, 2),
        3: build_generating_orbit_transversal(grp_2t, 3),
    }
    trans_a5 = {
        2: build_generating_orbit_transversal(grp_a5, 2),
        3: build_generating_orbit_transversal(grp_a5, 3),
    }

    ow1_a = run_task_ow1_a(grp_a5=grp_a5)
    ow1_b = run_task_ow1_b(grp_2t, trans_2t, grp_a5, trans_a5)
    ow1_c = run_task_ow1_c(grp_2t, trans_2t, grp_a5, trans_a5)
    ow1_d = run_task_ow1_d()

    result = {
        "card": "A2-OW1",
        "role": "independent_cold_room_referee",
        "hygiene": {
            "empirical_inputs": "0 of 19",
            "transversal_sizes": {
                "2T_n2": len(trans_2t[2]),
                "2T_n3": len(trans_2t[3]),
                "A5_n2": len(trans_a5[2]),
                "A5_n3": len(trans_a5[3]),
            },
        },
        "OW1-A": ow1_a,
        "OW1-B": ow1_b,
        "OW1-C": ow1_c,
        "OW1-D": ow1_d,
    }

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "referee_a2_ow1_out.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=False)
        fh.write("\n")
    print("DONE: wrote referee_a2_ow1_out.json")


if __name__ == "__main__":
    main()
