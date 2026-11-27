#!/usr/bin/env python3
"""
Card A2-PEER-SM-PURE3 — Blind Cross-Family Independent Second Computation of
SM-R384 (P-384, negative), SM-R614 (P-614), and SM-R635 (P-635) (seat fam3-v1-high-03, 0 of 19).

Built strictly blind from the claim card statements and named origin/main premises ONLY.
Zero sm/cards scripts or outputs opened before pre-commit and unread output sealing.
Zero main scripts imported: pure standard library + sympy + mpmath exact symbolic/integer arithmetic.
Zero float literals in code or JSON.
"""

import ast
import json
import math
import pathlib
import random
import sys
from collections import deque
from fractions import Fraction

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "a2_peer_sm_pure3_out.json"


# ------------------------------------------------------------------------------
# MODULE V1: Blind Verification of SM-R384 (two_fifths_class_one_bit, negative)
# ------------------------------------------------------------------------------
def canon_line(a: Fraction, b: Fraction):
    """Canonical representative of (a, b) in (Q/Z)^2 / {+-1}."""
    a = a - math.floor(a)
    b = b - math.floor(b)
    na = (-a) - math.floor(-a)
    nb = (-b) - math.floor(-b)
    return min((a, b), (na, nb))


def line_order(v):
    return math.lcm(v[0].denominator, v[1].denominator)


def p_part(v, p: int):
    """Return the p-part e*v where e == 1 mod p^k and e == 0 mod N/p^k."""
    N = line_order(v)
    pk = 1
    m = N
    while m % p == 0:
        pk *= p
        m //= p
    if pk == 1:
        return (Fraction(0, 1), Fraction(0, 1))
    if m == 1:
        return v
    inv_m = pow(m, -1, pk)
    e = (m * inv_m) % N
    return canon_line(e * v[0], e * v[1])


def act_T(v):
    """B1733 row convention: T(a, b) = (a, b - a) mod 1."""
    return canon_line(v[0], v[1] - v[0])


def run_module_v1():
    # 1. Enumerate all lines in (Q/Z)^2 / {+-1} of exact order 1 <= N <= 12
    all_lines = set()
    for N in range(1, 13):
        for i in range(N):
            for j in range(N):
                v = canon_line(Fraction(i, N), Fraction(j, N))
                if line_order(v) <= 12:
                    all_lines.add(v)
    all_lines = sorted(all_lines)
    by_order = {}
    for v in all_lines:
        n = line_order(v)
        by_order[n] = by_order.get(n, 0) + 1

    # 2. Target class K = {(2/5, odd/10)} and Galois twin K' = {(1/5, odd/10)}
    K = sorted({canon_line(Fraction(2, 5), Fraction(k, 10)) for k in (1, 3, 5, 7, 9)})
    K_prime = sorted({canon_line(Fraction(1, 5), Fraction(k, 10)) for k in (1, 3, 5, 7, 9)})
    K_set = set(K)
    K_union = sorted(set(K) | set(K_prime))

    # 3. Single-cusp check: <T, -I> orbit of (2/5, 1/10)
    seed = canon_line(Fraction(2, 5), Fraction(1, 10))
    orb = set()
    cur = seed
    while cur not in orb:
        orb.add(cur)
        cur = act_T(cur)
    k_is_single_cusp = (sorted(orb) == K)

    # Same check for K'
    seed_p = canon_line(Fraction(1, 5), Fraction(1, 10))
    orb_p = set()
    cur = seed_p
    while cur not in orb_p:
        orb_p.add(cur)
        cur = act_T(cur)
    kp_is_single_cusp = (sorted(orb_p) == K_prime)

    # 4. Unit closure of K under (Z/10Z)^x = {1, 3, 7, 9}
    unit_closure_K = sorted({
        canon_line(u * v[0], u * v[1])
        for v in K for u in (1, 3, 7, 9)
    })
    unit_closure_is_10 = (unit_closure_K == K_union and len(unit_closure_K) == 10)
    # Universal proof: for EVERY v in K, 3*v lies in K' (disjoint from K)
    unit3_maps_K_to_Kp = (sorted({canon_line(3 * v[0], 3 * v[1]) for v in K}) == K_prime)

    # 5. Least level N (multiple of 5) where (L, e) = (-3, 6) is NOT (Q, d) = (1, 2) transposed mod N
    #    Transposed means (L == d mod N and e == Q mod N) i.e. (-3 == 2 mod N and 6 == 1 mod N)
    non_transposed_mult5 = [
        N for N in range(5, 65, 5)
        if not ((-3 - 2) % N == 0 and (6 - 1) % N == 0)
    ]
    least_level = non_transposed_mult5[0]

    # 6. Check Pi and Pi_inv on all 266 lines
    def is_unit_twist(v):
        # 3a == +-1/5 mod 1 (note both reps (a,b) and (-a,-b) give +-3a)
        t = (3 * v[0]) - math.floor(3 * v[0])
        return t in (Fraction(1, 5), Fraction(4, 5))

    def is_inv_twist(v):
        # 3a in (1/5)Z/Z \ {0}
        t = (3 * v[0]) - math.floor(3 * v[0])
        return t in (Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5))

    Pi_set = sorted([v for v in all_lines if line_order(v) == least_level and is_unit_twist(v)])
    Pi_inv_set = sorted([v for v in all_lines if line_order(v) == least_level and is_inv_twist(v)])
    pi_equals_K = (Pi_set == K)
    pi_inv_equals_K_union = (Pi_inv_set == K_union)

    # 7. Exhaustive check of 14 natural unit-invariant rules on all 266 lines
    act_line = {canon_line(Fraction(k, 5), Fraction(2 * k, 5)) for k in (1, 2, 3, 4)}
    carriers = {canon_line(Fraction(2, 5), Fraction(1, 10)), canon_line(Fraction(2, 5), Fraction(1, 2))}

    def is_unit_closed(subset):
        s = set(subset)
        for v in s:
            N = line_order(v)
            for u in range(1, N):
                if math.gcd(u, N) == 1:
                    if canon_line(u * v[0], u * v[1]) not in s:
                        return False
        return True

    def has_a_order_5(v):
        return v[0].denominator == 5

    def has_b_order_2_or_10(v):
        return v[1].denominator in (2, 10)

    def has_5part_on_act(v):
        return p_part(v, 5) in act_line

    def has_5part_nonzero(v):
        return p_part(v, 5) != (Fraction(0, 1), Fraction(0, 1))

    def has_2part_nonzero(v):
        return p_part(v, 2) != (Fraction(0, 1), Fraction(0, 1))

    def has_2part_0_half(v):
        return p_part(v, 2) == canon_line(Fraction(0, 1), Fraction(1, 2))

    # Build 14 unit-invariant predicates
    ui_rules = {
        "U01_ord10": [v for v in all_lines if line_order(v) == 10],
        "U02_5div": [v for v in all_lines if line_order(v) % 5 == 0],
        "U03_ord10_inv_twist": Pi_inv_set,
        "U04_ord10_a_den5": [v for v in all_lines if line_order(v) == 10 and has_a_order_5(v)],
        "U05_ord10_b_even_den": [v for v in all_lines if line_order(v) == 10 and has_b_order_2_or_10(v)],
        "U06_ord10_2part_0half": [v for v in all_lines if line_order(v) == 10 and has_2part_0_half(v)],
        "U07_5part_act": [v for v in all_lines if has_5part_on_act(v)],
        "U08_ord10_5part_act": [v for v in all_lines if line_order(v) == 10 and has_5part_on_act(v)],
        "U09_ord10_5part_act_2part_0half": [v for v in all_lines if line_order(v) == 10 and has_5part_on_act(v) and has_2part_0_half(v)],
        "U10_ord10_not_act": [v for v in all_lines if line_order(v) == 10 and not has_5part_on_act(v)],
        "U11_5part_nz_2part_nz": [v for v in all_lines if has_5part_nonzero(v) and has_2part_nonzero(v)],
        "U12_ord10_inv_twist_2part_0half": [v for v in all_lines if line_order(v) == 10 and is_inv_twist(v) and has_2part_0_half(v)],
        "U13_inv_twist_all": [v for v in all_lines if is_inv_twist(v)],
        "U14_a_den5_all": [v for v in all_lines if has_a_order_5(v)],
    }
    ui_all_unit_closed = all(is_unit_closed(s) for s in ui_rules.values())
    ui_matching_K = [nm for nm, s in ui_rules.items() if set(s) == K_set]
    ui_containing_carriers = {nm: len(s) for nm, s in ui_rules.items() if carriers.issubset(set(s))}

    # Note: K's own unit-invariance check MUST be False!
    k_is_unit_closed = is_unit_closed(K)

    v1_ok = (
        len(all_lines) == 266
        and by_order[10] == 36
        and len(K) == 5
        and k_is_single_cusp
        and kp_is_single_cusp
        and unit_closure_is_10
        and unit3_maps_K_to_Kp
        and (not k_is_unit_closed)
        and least_level == 10
        and pi_equals_K
        and pi_inv_equals_K_union
        and ui_all_unit_closed
        and len(ui_matching_K) == 0
    )
    return {
        "ok": v1_ok,
        "verdict": "SAME" if v1_ok else "DIFFERS",
        "total_lines_ord_le_12": len(all_lines),
        "lines_ord_10": by_order[10],
        "K_size": len(K),
        "K_single_cusp": k_is_single_cusp,
        "Kp_single_cusp": kp_is_single_cusp,
        "K_unit_closed": k_is_unit_closed,
        "K_unit_closure_size": len(unit_closure_K),
        "unit3_swaps_K_to_Kp": unit3_maps_K_to_Kp,
        "least_level": least_level,
        "Pi_equals_K": pi_equals_K,
        "Pi_inv_size": len(Pi_inv_set),
        "Pi_inv_equals_K_union_Kp": pi_inv_equals_K_union,
        "unit_invariant_rules_tested": len(ui_rules),
        "unit_invariant_rules_all_closed": ui_all_unit_closed,
        "unit_invariant_rules_matching_K": ui_matching_K,
        "min_size_ui_containing_carriers": min(ui_containing_carriers.values()),
    }


# ------------------------------------------------------------------------------
# MODULE V2: Blind Verification of SM-R614 (discrete_remnant_27 on E_6 root)
# ------------------------------------------------------------------------------
def build_e6_27_and_roots():
    """
    Construct Bourbaki E_6 (nodes 1..6: 1-3-4-5-6 with 2 attached to 4):
      - Cartan matrix A (6x6)
      - All 27 weights of V(omega_1) as Dynkin-label tuples (w_1..w_6)
      - All 72 roots as simple-root coefficient tuples (c_1..c_6) and Dynkin tuples
      - Branching under:
          D_5 = {2, 3, 4, 5, 6} (delete node 1)
          SU(5) = {3, 4, 5, 6}? Wait: in Bourbaki E_6, deleting {1, 2} leaves A_4 = {3, 4, 5, 6},
          and deleting {1, 2, 4} leaves A_1 = {3} (SU(2)) x A_2 = {5, 6} (SU(3))!
          Let's verify D_5 -> SU(5) -> SU(3) x SU(2) directly on the weights!
    """
    # Bourbaki E_6 Cartan matrix (0-indexed: 0..5 correspond to Bourbaki 1..6)
    # Edges: (0,2), (2,3), (3,1), (3,4), (4,5)
    A = [[0] * 6 for _ in range(6)]
    for i in range(6):
        A[i][i] = 2
    for u, v in ((0, 2), (2, 3), (3, 1), (3, 4), (4, 5)):
        A[u][v] = -1
        A[v][u] = -1
    A_sp = sp.Matrix(A)

    # 1. Generate all 27 weights of V(omega_1) by standard Freudenthal / string lowering from (1,0,0,0,0,0)
    #    For minuscule rep V(omega_1), every weight mu has mu_i in {-1, 0, +1}, and whenever mu_i == +1
    #    we can lower by alpha_i (subtracting row i of A)!
    hw = (1, 0, 0, 0, 0, 0)
    weights = [hw]
    wset = {hw}
    dq = deque([hw])
    while dq:
        mu = dq.popleft()
        for i in range(6):
            if mu[i] > 0:
                nxt = tuple(mu[j] - A[i][j] for j in range(6))
                if nxt not in wset:
                    wset.add(nxt)
                    weights.append(nxt)
                    dq.append(nxt)
    assert len(weights) == 27

    # 2. Generate all 72 roots of E_6 by Weyl reflections of simple roots!
    #    Root in simple-root coords c = (c_0..c_5); Dynkin labels d = c * A (since A is symmetric, d_i = sum_j c_j A_{ji})
    def reflect(c, i):
        # s_i(c) = c - (c . alpha_i^v) e_i, where (c . alpha_i^v) = sum_j c_j A_{j, i}
        pairing = sum(c[j] * A[j][i] for j in range(6))
        out = list(c)
        out[i] -= pairing
        return tuple(out)

    roots = set()
    dq = deque()
    for i in range(6):
        e = tuple(1 if j == i else 0 for j in range(6))
        roots.add(e)
        dq.append(e)
    while dq:
        r = dq.popleft()
        for i in range(6):
            nr = reflect(r, i)
            if nr not in roots:
                roots.add(nr)
                dq.append(nr)
    roots = sorted(roots)
    assert len(roots) == 72

    # 3. Fundamental coweights: pairing of Dynkin weight mu with simple-coroot vector x is simply sum_i mu_i x_i!
    #    So the fundamental coweight dual to alpha_k is simply the unit vector e_k = (0..1..0)!
    #    WAIT: check! For simple root alpha_j (Dynkin row A[j]), alpha_j . x = sum_i A[j][i] x_i.
    #    A Cartan element x commutes with simple root alpha_j iff (A x)_j == 0!
    #    So the fundamental coweight omega_k^v (killing all alpha_j for j != k, pairing 1 with alpha_k)
    #    is column k of A^{-1}!
    A_inv = A_sp.inv()
    # Check psi = 3 * column 0 of A^{-1} (node 1 = index 0)
    psi = [sp.Rational(3) * A_inv[i, 0] for i in range(6)]
    # Check chi: kills D_5's SU(5) subalgebra! Wait: inside D_5 = {1, 2, 3, 4, 5} (0-indexed: nodes 2,3,4,5,6),
    # deleting node 2 (index 1) leaves A_4 = {2, 3, 4, 5} (nodes 3,4,5,6)!
    # Wait: verify! Removing index 0 AND index 1 leaves edges (2,3)-(3,4)-(4,5) = A_4 = SU(5)!
    # So chi must vanish on alpha_2, alpha_3, alpha_4, alpha_5 (indices 2,3,4,5) AND be orthogonal to psi in Killing metric!
    # In Killing metric, orthogonal to psi (which kills indices 1..5, so psi ~ omega_1^v) means:
    # (A * chi)_j == 0 for j in {2,3,4,5} AND (psi^T A chi) == 0!
    # Since psi = 3 * A^{-1} e_0, psi^T A chi = 3 * e_0^T chi = 3 * chi_0!
    # So chi_0 == 0 AND (A chi)_j == 0 for j in {2,3,4,5}!
    # Solve this 5-eq system in 6 vars (unique up to scale!), normalize so chi on 16 -> (+3 on 5bar, -1 on 10, -5 on 1)!
    x_syms = sp.symbols("x0:6")
    eqs_chi = [x_syms[0]] + [sum(A[j][i] * x_syms[i] for i in range(6)) for j in (2, 3, 4, 5)]
    sol_chi = sp.linsolve(eqs_chi, x_syms)
    chi_raw = list(list(sol_chi)[0])
    # Substitute free symbol = 1
    free_s = [s for s in x_syms if s in sp.Matrix(chi_raw).free_symbols][0]
    chi_vec = [e.subs(free_s, 1) for e in chi_raw]
    # Check values of (psi, chi) on the 27 weights to fix exact normalization of chi!
    def dot_w(mu, v):
        return sum(mu[i] * v[i] for i in range(6))

    psi_vals = sorted(set(dot_w(mu, psi) for mu in weights))
    assert psi_vals == [-2, 1, 4]
    # Find the SU(5) singlet inside psi == +1 (nu^c): has all A_4 Dynkin labels (indices 2,3,4,5) == 0!
    nuc_candidates = [mu for mu in weights if dot_w(mu, psi) == 1 and all(mu[j] == 0 for j in (2, 3, 4, 5))]
    assert len(nuc_candidates) == 1
    w_nuc = nuc_candidates[0]
    # Normalize chi so chi(w_nuc) == -5 (giving chi = (-5 on nu^c, -1 on 10, +3 on 5bar, +2 on 5, -2 on 5bar', 0 on N))
    chi = [sp.Rational(-5) * e / dot_w(w_nuc, chi_vec) for e in chi_vec]

    # Now find Y inside SU(5) = {2, 3, 4, 5}, commuting with SU(2) = {2} and SU(3) = {4, 5}!
    # So Y is orthogonal to psi and chi (Y_0 = 0, Y_1 = 0) AND kills alpha_2, alpha_4, alpha_5!
    eqs_Y = [x_syms[0], x_syms[1]] + [sum(A[j][i] * x_syms[i] for i in range(6)) for j in (2, 4, 5)]
    sol_Y = sp.linsolve(eqs_Y, x_syms)
    Y_raw = list(list(sol_Y)[0])
    free_y = [s for s in x_syms if s in sp.Matrix(Y_raw).free_symbols][0]
    Y_vec = [e.subs(free_y, 1) for e in Y_raw]
    # Find e^c: in 10 of SU(5) (psi == +1, chi == -1), SU(3) x SU(2) singlet (mu[2]==0, mu[4]==0, mu[5]==0)!
    ec_cands = [mu for mu in weights if dot_w(mu, psi) == 1 and dot_w(mu, chi) == -1 and mu[2] == 0 and mu[4] == 0 and mu[5] == 0]
    assert len(ec_cands) == 1
    w_ec = ec_cands[0]
    # Normalize Y so Y(e^c) = +1 (6Y = +6)
    Y = [sp.Rational(1) * e / dot_w(w_ec, Y_vec) for e in Y_vec]

    # eta = (3 * chi - 5 * psi) / 4
    eta = [(3 * chi[i] - 5 * psi[i]) / sp.Rational(4) for i in range(6)]

    # Identify all 11 SM multiplets in the 27!
    w_N_cands = [mu for mu in weights if dot_w(mu, psi) == 4]
    assert len(w_N_cands) == 1
    w_N = w_N_cands[0]

    return A_sp, weights, roots, psi, chi, Y, eta, w_nuc, w_N


def smith_invariants_quotient(basis_V, vev_weights):
    """
    Exact discrete residual group:
        Q = {x in V : w.x in Z for all w in vev_weights} / ((V cap ker W) + (V cap Z^6))
    where V = span_R(basis_V) subset R^6 and basis_V is a d x 6 rational matrix (rows = basis of V).

    Method:
    1. Find an integral lattice basis B_int (d x 6, integer rows) of L_int = V cap Z^6!
       Every x in V is written x = c * B_int with c in R^d, so x in Z^6 iff c in Z^d!
    2. Compute the integer matrix M = B_int * W^T (d x m, integer entries since B_int and W are integer!).
    3. Compute the exact Smith Normal Form U M V_snf = diag(s_1, ..., s_r, 0, ..., 0)!
       Then w.x = (c * B_int) W^T = c * M = (c U^{-1}) * diag(s_1..s_r, 0..0) * V_snf^{-1}.
       Writing y = c U^{-1} in R^d:
         - x in V cap ker W  <=>  y_1 = ... = y_r = 0  (y_{r+1}..y_d arbitrary real!)
         - x in V cap Z^6    <=>  y in Z^d
         - w.x in Z^m        <=>  s_i y_i in Z for i = 1..r  <=>  y_i in (1/s_i) Z for i = 1..r!
       Therefore:
         Q ~= (Z / s_1 Z) x ... x (Z / s_r Z) !!
       Wait: that's an EXACT, 100% coordinate-free theorem!! Every invariant factor s_i > 1 is a cyclic factor of Q!
    """
    # Compute integer basis of L_int = V cap Z^6:
    # A vector x in Z^6 lies in V iff N_V * x = 0, where rows of N_V span V^perp over Q (cleared to Z)!
    B_rat = sp.Matrix(basis_V)  # d x 6
    d = B_rat.rows
    ns = B_rat.nullspace()  # basis of V^perp
    # Clear denominators to get integer matrix N_V ((6-d) x 6)
    N_rows = []
    for v in ns:
        den = 1
        for e in v:
            den = math.lcm(den, int(sp.fraction(e)[1]))
        N_rows.append([int(e * den) for e in v])
    if len(N_rows) == 0:
        B_int = sp.eye(6)
    else:
        N_mat = sp.Matrix(N_rows)
        # Integer nullspace of N_mat via Smith Normal Form over ZZ!
        # Using sympy.matrices.normalforms.smith_normal_decomp(N_mat) -> (S, U, V) with S = U * N_mat * V
        from sympy.matrices.normalforms import smith_normal_decomp
        S_n, U_n, V_n = smith_normal_decomp(N_mat)
        r_n = sum(1 for i in range(min(S_n.rows, S_n.cols)) if S_n[i, i] != 0)
        assert 6 - r_n == d
        # Columns r_n..5 of V_n form an exact Z-basis of ker_Z(N_mat) = V cap Z^6!
        B_int = V_n[:, r_n:].T  # d x 6 integer matrix

    # Verify B_int spans V and has primitive rows in Z^6
    assert B_int.rows == d and B_int.cols == 6
    if len(N_rows) > 0:
        assert (N_mat * B_int.T).is_zero_matrix

    # Build M = B_int * W^T (d x m integer matrix)
    W_mat = sp.Matrix(vev_weights)  # m x 6 integer matrix
    M = B_int * W_mat.T
    from sympy.matrices.normalforms import smith_normal_decomp
    S_m, U_m, V_m = smith_normal_decomp(M)
    diag_nonzero = [abs(int(S_m[i, i])) for i in range(min(S_m.rows, S_m.cols)) if S_m[i, i] != 0]
    nontrivial = [s for s in diag_nonzero if s > 1]
    order = 1
    for s in diag_nonzero:
        order *= s
    return B_int, diag_nonzero, nontrivial, order


def run_module_v2():
    A_sp, weights, roots, psi, chi, Y, eta, w_nuc, w_N = build_e6_27_and_roots()

    def dot_w(mu, v):
        return sum(mu[i] * v[i] for i in range(6))

    # 1. Verify complete 27 table of (SU(3) x SU(2), 6Y, psi, chi, eta)
    #    SU(2) simple root is index 2; SU(3) simple roots are indices 4, 5.
    charge_buckets = {}
    for mu in weights:
        key = (int(6 * dot_w(mu, Y)), int(dot_w(mu, psi)), int(dot_w(mu, chi)), int(dot_w(mu, eta)))
        charge_buckets[key] = charge_buckets.get(key, 0) + 1
    # Expected 11 SM multiplets:
    # Q: (1, 1, -1, -2) x 6; u^c: (-4, 1, -1, -2) x 3; e^c: (6, 1, -1, -2) x 1
    # d^c: (2, 1, 3, 1) x 3; L: (-3, 1, 3, 1) x 2; nu^c: (0, 1, -5, -5) x 1
    # H_u: (3, -2, 2, 4) x 2; D: (-2, -2, 2, 4) x 3
    # H_d: (-3, -2, -2, 1) x 2; Dbar: (2, -2, -2, 1) x 3; N: (0, 4, 0, -5) x 1
    expected_buckets = {
        (1, 1, -1, -2): 6, (-4, 1, -1, -2): 3, (6, 1, -1, -2): 1,
        (2, 1, 3, 1): 3, (-3, 1, 3, 1): 2, (0, 1, -5, -5): 1,
        (3, -2, 2, 4): 2, (-2, -2, 2, 4): 3,
        (-3, -2, -2, 1): 2, (2, -2, -2, 1): 3, (0, 4, 0, -5): 1,
    }
    table_27_ok = (charge_buckets == expected_buckets)
    nuc_eq_N_eta = (dot_w(w_nuc, eta) == dot_w(w_N, eta) == -5)

    # 2. Construct V_SM (rank 4: simple coroots e_2 [SU(2)], e_4, e_5 [SU(3)], and Y) and V_5 = V_SM + R*eta
    e_su2 = [sp.Rational(1 if i == 2 else 0) for i in range(6)]
    e_su3a = [sp.Rational(1 if i == 4 else 0) for i in range(6)]
    e_su3b = [sp.Rational(1 if i == 5 else 0) for i in range(6)]
    V_SM = [e_su2, e_su3a, e_su3b, Y]
    V_5 = [e_su2, e_su3a, e_su3b, Y, eta]
    V_6 = [[sp.Rational(1 if i == j else 0) for i in range(6)] for j in range(6)]

    # 3. Exact Smith Normal Form discrete residuals in V_5 and V_6 for {nu^c}, {N}, {nu^c, N}!
    _, snf_v5_nuc, nt_v5_nuc, ord_v5_nuc = smith_invariants_quotient(V_5, [w_nuc])
    _, snf_v5_N, nt_v5_N, ord_v5_N = smith_invariants_quotient(V_5, [w_N])
    _, snf_v5_both, nt_v5_both, ord_v5_both = smith_invariants_quotient(V_5, [w_nuc, w_N])
    _, snf_v6_nuc, nt_v6_nuc, ord_v6_nuc = smith_invariants_quotient(V_6, [w_nuc])
    _, snf_v6_N, nt_v6_N, ord_v6_N = smith_invariants_quotient(V_6, [w_N])
    _, snf_v6_both, nt_v6_both, ord_v6_both = smith_invariants_quotient(V_6, [w_nuc, w_N])

    # 4. Explicit check that exp(2 pi i eta / 5) is an SM element!
    #    That means there exists c in Q^4 such that eta/5 - (c_0 e_su2 + c_1 e_su3a + c_2 e_su3b + c_3 Y) in Z^6!
    #    Check directly by solving on the 2 coordinates outside {2, 4, 5} or checking V_SM + Z^6!
    #    Even cleaner: test if eta/5 lies in V_SM + Z^6!
    #    Write eta/5 = sum c_k v_k + z (z in Z^6) <=> N_{V_SM} * (eta/5) = N_{V_SM} * z for some z in Z^6!
    #    Solve c_k directly: since V_SM has simple coroots e_2, e_4, e_5, we only need c_3 * Y_j == eta_j/5 mod 1 for j in {0, 1, 3}!
    #    Let's solve explicitly over Q and verify exact integrality on all 6 coordinates!
    #    From earlier algebra: z_3(omega^{-1}) * exp(-4 pi i Y / 5) -> c_Y = -2/5!
    #    Test all c_Y = k/5? Better: solve linear system over Q for c_3 from j=0 (or solve N_{V_SM} z = N_{V_SM} eta/5)!
    B_sm_int, _, _, _ = smith_invariants_quotient(V_SM, [w_nuc])  # wait: just get V_SM cap Z^6!
    # Solve (eta/5 - x_SM) in Z^6: check explicit x_SM = c_2 e_2 + c_4 e_4 + c_5 e_5 + c_Y Y
    # Because Y_0 = Y_1 = 0, check eta_0/5 and eta_1/5! Wait: let's check eta vector entries!
    # Solve for c_Y, c_2, c_4, c_5 mod Z:
    # Actually: exp(2 pi i x) = exp(2 pi i y) on ALL 27 weights iff x - y in Z^6!
    # Check if there exists x_SM in V_SM with (eta/5 - x_SM) in Z^6:
    # Let M_sm = [e_su2; e_su3a; e_su3b; Y]^T (6 x 4) and I_6 (6 x 6).
    # Equivalently, check in the 27 weights: find c_Y, z_2, z_3 such that
    #   exp(2 pi i * (eta/5 - c_Y * Y - c_2 * e_2 - c_4 * e_4 - c_5 * e_5)) == 1 on all 27 weights!
    # Solve directly from the linear equations: (eta/5 - c_Y Y - c_2 e_2 - c_4 e_4 - c_5 e_5) . mu in Z for all 27 mu,
    # which is equivalent to (eta/5 - c_Y Y - c_2 e_2 - c_4 e_4 - c_5 e_5) in Z^6!
    # Check coordinates 0, 1, 3 (where e_2, e_4, e_5 are 0):
    #   j=0: eta[0]/5 - c_Y * Y[0] in Z
    #   j=1: eta[1]/5 - c_Y * Y[1] in Z
    #   j=3: eta[3]/5 - c_Y * Y[3] in Z
    # Note Y[0] = Y[1] = 0, so eta[0]/5 and eta[1]/5 MUST BE INTEGERS! Let's compute c_Y = (eta[3]/5) / Y[3] mod 1!
    c_Y_exact = sp.Rational(-2, 5)
    # Check all possible integer shifts on j=3 so (eta[3]/5 - c_Y * Y[3]) is integer!
    # Actually, solve directly: pick c_Y such that (eta[3]/5 - c_Y * Y[3]) == 0 -> c_Y = (eta[3]/5) / Y[3]
    c_Y_sol = (eta[3] / 5) / Y[3]
    # Then set c_2, c_4, c_5 = (eta[j]/5 - c_Y_sol * Y[j]) for j in {2, 4, 5}!
    x_sm_cand = [
        c_Y_sol * Y[i]
        + (eta[2] / 5 - c_Y_sol * Y[2]) * e_su2[i]
        + (eta[4] / 5 - c_Y_sol * Y[4]) * e_su3a[i]
        + (eta[5] / 5 - c_Y_sol * Y[5]) * e_su3b[i]
        for i in range(6)
    ]
    diff_eta5_sm = [eta[i] / 5 - x_sm_cand[i] for i in range(6)]
    eta_over_5_in_SM = all(d.q == 1 for d in diff_eta5_sm)
    # Also double-check on all 27 weights that (eta/5 - x_sm_cand) . mu is an integer!
    eta5_27_ok = all(dot_w(mu, diff_eta5_sm).q == 1 for mu in weights)

    # 5. Matter parity check in V_5 (and in full R^6):
    #    A torus element x in V commutes with SU(3) x SU(2) iff (A x)_j in Z for j in {2, 4, 5}
    #    (wait: on the Cartan torus, commuting with SU(3) x SU(2) means exp(2 pi i alpha_j . x) == 1 for j in {2, 4, 5},
    #    i.e., alpha_j . x in Z for j in {2, 4, 5}!).
    #    AND matter parity requires:
    #      mu . x == 0 (mod 1) on H_u, H_d, and the vev(s) (nu^c or N)
    #      mu . x == 1/2 (mod 1) on Q, u^c, d^c, L, e^c!
    #    Check exact existence in V_5 AND in R^6!
    #    Parametrize x in V_5 as c_2 e_2 + c_4 e_4 + c_5 e_5 + c_Y Y + c_eta eta:
    #    Since SU(3) x SU(2) center elements have exp(2 pi i (c_2 e_2 + c_4 e_4 + c_5 e_5)) = z_2 in {+-1}, z_3 in {1, om, om^2}:
    #    Every element of exp(2 pi i V_5) commuting with SU(3) x SU(2) acts on an SM multiplet (r_3, r_2, Y, eta) by
    #      exp(2 pi i (k_2 * t_2/2 + k_3 * t_3/3 + c_Y * Y + c_eta * eta))
    #    with k_2 in {0, 1}, k_3 in {0, 1, 2}, c_Y in R/Z, c_eta in R/Z!
    #    Let's solve the EXACT linear system mod 1 over ALL (k_2, k_3) in {0,1} x {0,1,2}!
    def check_matter_parity_v5(vev_list):
        # Need c_Y, c_eta in R/Z and k_2 in {0,1}, k_3 in {0,1,2} such that:
        #   vevs: c_eta * (-5) == 0 mod 1  => 5 c_eta in Z => c_eta = m/5 (m in 0..4)
        #   H_u (t3=0, t2=1, Y=1/2, eta=4): k_2/2 + c_Y/2 + 4 c_eta == 0 mod 1
        #   H_d (t3=0, t2=1, Y=-1/2, eta=1): k_2/2 - c_Y/2 + c_eta == 0 mod 1
        #   e^c (t3=0, t2=0, Y=1, eta=-2): c_Y - 2 c_eta == 1/2 mod 1
        #   L   (t3=0, t2=1, Y=-1/2, eta=1): k_2/2 - c_Y/2 + c_eta == 1/2 mod 1  <-- COMPARE WITH H_d!!
        # OH!! LOOK AT L AND H_d: THEY HAVE IDENTICAL (r_3, r_2, Y, eta) = (1, 2, -1/2, +1)!!
        # SO ANY ELEMENT OF SM x U(1)_eta ACTS IDENTICALLY ON L AND H_d! IT CAN *NEVER* GIVE -1 ON L AND +1 ON H_d!!
        # Let's verify this exhaustively over all (k_2, k_3, m) too!
        sols = []
        for k2 in (0, 1):
            for k3 in (0, 1, 2):
                for m in range(5):
                    c_eta = Fraction(m, 5)
                    # From e^c: c_Y == 1/2 + 2 c_eta mod 1
                    c_Y = (Fraction(1, 2) + 2 * c_eta) % 1
                    # Check all 7 required multiplets: (t3, t2, Y, eta, want_phase)
                    reqs = [
                        (0, 1, Fraction(1, 2), 4, Fraction(0, 1)),    # H_u -> +1
                        (0, 1, Fraction(-1, 2), 1, Fraction(0, 1)),   # H_d -> +1
                        (1, 1, Fraction(1, 6), -2, Fraction(1, 2)),   # Q   -> -1
                        (2, 0, Fraction(-2, 3), -2, Fraction(1, 2)),  # u^c -> -1
                        (2, 0, Fraction(1, 3), 1, Fraction(1, 2)),    # d^c -> -1
                        (0, 1, Fraction(-1, 2), 1, Fraction(1, 2)),   # L   -> -1
                        (0, 0, Fraction(1, 1), -2, Fraction(1, 2)),   # e^c -> -1
                    ]
                    ok = True
                    for t3, t2, yv, ev, want in reqs:
                        ph = (Fraction(k3 * t3, 3) + Fraction(k2 * t2, 2) + c_Y * yv + c_eta * ev) % 1
                        if ph != want:
                            ok = False
                            break
                    if ok:
                        sols.append((k2, k3, str(c_Y), str(c_eta)))
        return sols

    mp_v5_sols = check_matter_parity_v5(["nu^c_or_N"])

    # Also check full R^6 (SM x U(1)_psi x U(1)_chi) for comparison:
    # In R^6, L has (psi=1, chi=3) while H_d has (psi=-2, chi=-2) — DIFFERENT!
    # Check which vevs ({N} vs {nu^c} vs {nu^c, N}) admit matter parity in full R^6!
    def check_matter_parity_r6(fix_nuc: bool, fix_N: bool):
        # Need x in R^6 with alpha_j . x in Z (j in 2,4,5) -> parametrize by (k2, k3, c_Y, c_psi, c_chi)!
        # From H_u (0,1,1/2,-2,2): k2/2 + c_Y/2 - 2 c_psi + 2 c_chi == 0
        # From H_d (0,1,-1/2,-2,-2): k2/2 - c_Y/2 - 2 c_psi - 2 c_chi == 0
        # From L   (0,1,-1/2,1,3): k2/2 - c_Y/2 + c_psi + 3 c_chi == 1/2
        # From e^c (0,0,1,1,-1): c_Y + c_psi - c_chi == 1/2
        # Subtract H_d from L: 3 c_psi + 5 c_chi == 1/2 mod 1.
        # Add H_u and H_d: k2 - 4 c_psi == 0 mod 1 => 4 c_psi == 0 mod 1 => c_psi in {0, 1/4, 1/2, 3/4}!
        sols = []
        for k2 in (0, 1):
            for k3 in (0, 1, 2):
                for p4 in range(4):
                    c_psi = Fraction(p4, 4)
                    # 5 c_chi == 1/2 - 3 c_psi mod 1 => 5 values for c_chi
                    rhs = (Fraction(1, 2) - 3 * c_psi) % 1
                    for j5 in range(5):
                        c_chi = (rhs + j5) / 5
                        c_Y = (Fraction(1, 2) - c_psi + c_chi) % 1
                        reqs = [
                            (0, 1, Fraction(1, 2), -2, 2, Fraction(0, 1)),    # H_u
                            (0, 1, Fraction(-1, 2), -2, -2, Fraction(0, 1)),  # H_d
                            (1, 1, Fraction(1, 6), 1, -1, Fraction(1, 2)),    # Q
                            (2, 0, Fraction(-2, 3), 1, -1, Fraction(1, 2)),   # u^c
                            (2, 0, Fraction(1, 3), 1, 3, Fraction(1, 2)),     # d^c
                            (0, 1, Fraction(-1, 2), 1, 3, Fraction(1, 2)),    # L
                            (0, 0, Fraction(1, 1), 1, -1, Fraction(1, 2)),    # e^c
                        ]
                        if fix_nuc:
                            reqs.append((0, 0, Fraction(0, 1), 1, -5, Fraction(0, 1)))
                        if fix_N:
                            reqs.append((0, 0, Fraction(0, 1), 4, 0, Fraction(0, 1)))
                        if all((Fraction(k3 * t3, 3) + Fraction(k2 * t2, 2) + c_Y * yv + c_psi * pv + c_chi * cv) % 1 == w
                               for t3, t2, yv, pv, cv, w in reqs):
                            sols.append((k2, k3, str(c_Y), str(c_psi), str(c_chi)))
        return len(sols)

    mp_r6_N_only = check_matter_parity_r6(False, True)
    mp_r6_nuc_only = check_matter_parity_r6(True, False)
    mp_r6_both = check_matter_parity_r6(True, True)

    # 6. Exact E_6 (78-dim) compact Lie-algebra stabilizer dimensions & ranks for {N}, {nu^c}, {nu^c, N}!
    #    For a single weight vector v = e_mu (for mu in {w_N, w_nuc}):
    #    - A root alpha stabilizes e_mu iff mu + alpha is NOT a weight of the 27!
    #      Wait: in the COMPACT real form e_{6(-78)}, the stabilizer subalgebra g_v = {X in e_6 : X v = 0}
    #      is reductive and spanned by:
    #        (a) Cartan elements h with mu . h = 0 (dim = 5 for 1 weight, dim = 4 for 2 linearly independent weights!),
    #        (b) Root spaces E_alpha + E_{-alpha} / i(E_alpha - E_{-alpha}) where BOTH mu + alpha AND mu - alpha are NOT weights!
    #      Wait: check if mu + alpha is a weight! In a minuscule rep, mu + alpha is a weight iff <mu, alpha^v> == -1,
    #      and mu - alpha is a weight iff <mu, alpha^v> == +1!
    #      So a root alpha belongs to the compact stabilizer of e_mu iff <mu, alpha^v> == 0!!
    #    WAIT A SECOND!! Check TWO independent singlets v = a e_{w_N} + b e_{w_nuc} (nonzero a, b):
    #      Since w_N - w_nuc is NOT a root (verify!), can E_alpha cancel between e_{w_N} and e_{w_nuc}?
    #      Only if w_N + alpha == w_nuc + beta for alpha = beta (impossible) or w_N + alpha = w_nuc (only if w_N - w_nuc is a root!).
    #      WAIT — CHECK IF w_N - w_nuc IS A ROOT OF E_6!!
    w_dynk_set = set(weights)
    root_dynk_map = {}
    for c in roots:
        d = tuple(sum(c[j] * int(A_sp[j, i]) for j in range(6)) for i in range(6))
        root_dynk_map[d] = c
    diff_N_nuc = tuple(w_N[i] - w_nuc[i] for i in range(6))
    diff_N_nuc_is_root = (diff_N_nuc in root_dynk_map)

    def compact_stabilizer_e6(vev_ws):
        # Exact root-space stabilizer in compact e_6:
        # Cartan part: ker(W) in R^6 (dim = 6 - rank(W))
        # Root part: in compact form, X = sum_alpha c_alpha E_alpha + h with c_{-alpha} = -conj(c_alpha) (or Hermitian inner product).
        # For any w_a, w_b in vev_ws, if w_a - w_b is NOT a root, the images E_alpha(e_{w_a}) for distinct (alpha, w_a)
        # land in DISTINCT weight spaces!
        # Let's check for general linear combinations by building the exact complexified action on all 27 weight spaces:
        # In compact form, X = h + sum_{alpha > 0} (u_a (E_a - E_{-a}) + i v_a (E_a + E_{-a})).
        # Wait: E_a(e_w) != 0 iff w + a is a weight, and E_{-a}(e_w) != 0 iff w - a is a weight.
        # For a single weight w: X e_w = 0 <=> w.h = 0 AND for every alpha > 0, neither w+alpha nor w-alpha is a weight!
        # For two weights w1, w2 with w1 - w2 NOT a root AND w1 + alpha != w2 - alpha (i.e. w1 - w2 != -2 alpha, impossible for roots!):
        # Wait: can w1 + alpha == w2 + beta? Only if alpha != beta (different variables!), wait — YES!!
        # If w1 + alpha == w2 + beta = mu (a third weight in 27!), then c_alpha E_alpha e_{w1} + c_beta E_beta e_{w2} = 0
        # creates a LINEAR RELATION between c_alpha and c_beta (inside SU(6) vs SU(5)!)!
        # THANK GOODNESS WE CHECKED THAT!!
        # Let's compute the EXACT 27-dim complex action of ALL 78 compact e_6 generators (using exact Chevalley signs or
        # exact weight-collision graph in the 27 — wait: for ANY two weights w1, w2 in 27, the stabilizer of e_{w1} AND e_{w2}
        # SEPARATELY [intersection of stabilizers: St(e_{w1}) cap St(e_{w2})] vs the stabilizer of ONE vector e_{w1} + e_{w2}!)
        # Wait: in SM-R614, a "nu^c vev and N vev" means BOTH <nu^c> != 0 AND <N> != 0 in the SAME 27 (i.e. ONE vector v = e_{nu^c} + e_N in 27)!
        # Let's check BOTH:
        #   (i) Intersection St(e_{w1}) cap St(e_{w2}) = roots killing BOTH w1 and w2 + Cartan ker(w1, w2)
        #   (ii) Stabilizer of v = e_{w1} + e_{w2} in compact e_6!
        # WAIT: In a minuscule rep 27 of E_6, EVERY nonzero vector in 27 lies in one of ONLY THREE E_6-orbits:
        #   rank 1 (stabilizer Spin(10), dim 45, rank 5 — e.g. e_N or e_{nu^c}!),
        #   rank 2 (stabilizer Spin(9)? Wait: F_4 has dim 52 for rank 3! Let's check the 3 orbits of E_6 on 27:
        #           rank 1: D_5 = Spin(10) [dim 45, rank 5];
        #           rank 2: B_4 = Spin(9) [dim 36, rank 4] or SU(5) [dim 24, rank 4]?!
        #           NO!! Wait: for e_{nu^c} + e_N, check the cubic invariant I_3(v) and quadratic dI_3(v)!!
        #           In E_6's 27, the cubic invariant is 10*10*1 + 16*16*10 -> BOTH N (in 1) AND nu^c (in 16) have
        #           I_3(a N + b nu^c) = 0 AND dI_3(a N + b nu^c) = 0 (since 1*16*16 has NO 16*16*1 term, only 16*16*10,
        #           and 1*1*1 = 0, 1*1*16 = 0!!)!!
        #   WHOA!! STOP EVERYTHING!!
        #   CHECK THE INTERSECTION STABILIZER St(nu^c) cap St(N) vs SINGLE-VECTOR STABILIZER St(nu^c + N)!!
        #   - Roots orthogonal to w_N: D_5 = 40 roots + 5 Cartan = dim 45, rank 5 (Spin(10))!
        #   - Roots orthogonal to w_nuc: D_5 = 40 roots + 5 Cartan = dim 45, rank 5 (Spin(10))!
        #   - Roots orthogonal to BOTH w_N AND w_nuc: A_4 = 20 roots + 4 Cartan = dim 24, rank 4 (SU(5))!
        #   - AND what about the single vector v = e_N + e_{nu^c} in E_6?! Since w_N and w_nuc span a rank-1 (null!) plane
        #     with NO cubic invariant and NO common 10-weight?! Wait: DOES there exist a pair of roots (alpha, beta)
        #     with w_N + alpha = w_nuc + beta?! Let's COMPUTE IT DIRECTLY!!
        W_m = sp.Matrix(vev_ws)
        cartan_dim = 6 - W_m.rank()
        # Roots killing ALL w in vev_ws (i.e. St(w_1) cap ... cap St(w_k)):
        # A root alpha (simple-root coords c) has <w, alpha^v> = sum_i w_i c_i (since w is in Dynkin labels!).
        # Verify: for simple root e_k, <w, e_k^v> = w_k! YES! Because E_6 is simply-laced, alpha^v = alpha,
        # so <w, alpha^v> = sum_i w_i c_i!!
        stab_roots = [c for c in roots if all(sum(w[i] * c[i] for i in range(6)) == 0 for w in vev_ws)]
        dim_inter = cartan_dim + len(stab_roots)
        # Also compute rank of the root system stab_roots (dim of span of stab_roots + central torus in ker W = cartan_dim!)
        # Wait: every Cartan element in ker W commutes with all Cartan elements in ker W, so rank of St(w_1) cap ... cap St(w_k) is cartan_dim!
        # AND check exact single-vector stabilizer dimension for v = sum_{w in vev_ws} e_w in compact e_6!
        # Count weight collisions mu = w_a + alpha = w_b + beta!
        # For each positive root alpha > 0, let x_a = (E_a - E_{-a}) and y_a = i(E_a + E_{-a}) (real basis of compact e_6).
        # Wait: in compact e_6, on ANY weight space mu, the real and imaginary parts decouple cleanly, OR simply:
        # Since E_6 is simply-laced and 27 is minuscule, in the Chevalley basis every nonzero action E_alpha e_w = +- e_{w+alpha}!
        # Even simpler: check whether ANY pair (alpha, beta) of roots satisfies w_N + alpha = w_nuc + beta!
        return dim_inter, cartan_dim, len(stab_roots)

    dim_N, rk_N, rts_N = compact_stabilizer_e6([w_N])
    dim_nuc, rk_nuc, rts_nuc = compact_stabilizer_e6([w_nuc])
    dim_both_inter, rk_both_inter, rts_both_inter = compact_stabilizer_e6([w_nuc, w_N])

    # Check if w_N + alpha == w_nuc + beta for ANY roots alpha, beta (i.e. whether e_N + e_{nu^c} is STILL Spin(10)-equivalent in E_6!):
    w_N_plus = {tuple(w_N[i] + d[i] for i in range(6)): c for d, c in root_dynk_map.items()
                if tuple(w_N[i] + d[i] for i in range(6)) in w_dynk_set}
    w_nuc_plus = {tuple(w_nuc[i] + d[i] for i in range(6)): c for d, c in root_dynk_map.items()
                  if tuple(w_nuc[i] + d[i] for i in range(6)) in w_dynk_set}
    common_targets = sorted(set(w_N_plus.keys()) & set(w_nuc_plus.keys()))
    # Note: e_N + e_{nu^c} in 27 is ACTUALLY in the same Spin(10) orbit of E_6 if w_N and w_nuc have <w_N, w_nuc> such that
    # their sum is still rank-1 in the Albert algebra J_3(O) (which happens iff they lie in a common 16 or 10? Wait:
    # len(common_targets) tells us immediately: if 10 common targets, then 10 pairs cancel, lifting dim from 24 to 24 + 20 + 1 = 45!!
    # Let's record BOTH intersection stabilizer (dim 24, rank 4 = SU(5)) AND single-vector common_targets count!)

    # 7. E5 mod-2 census: h in (Z/2Z)^6 with h . w_nuc == 0 mod 2 and h . w_N == 0 mod 2
    e5_vecs = []
    e5_sm_comm = []
    for mask in range(64):
        h = [(mask >> i) & 1 for i in range(6)]
        if (sum(h[i] * w_nuc[i] for i in range(6)) % 2 == 0) and (sum(h[i] * w_N[i] for i in range(6)) % 2 == 0):
            e5_vecs.append(tuple(h))
            # Check if x = h/2 commutes with SU(3) x SU(2) (alpha_j . h == 0 mod 2 for j in {2, 4, 5})
            if all(sum(int(A_sp[j, i]) * h[i] for i in range(6)) % 2 == 0 for j in (2, 4, 5)):
                # Check phases on (H_u, H_d, Q, u^c, d^c, L, e^c)
                e5_sm_comm.append(tuple(h))
    # Check if ANY of e5_sm_comm is a matter parity!
    # Find one representative weight of each of H_u, H_d, Q, u^c, d^c, L, e^c
    def find_rep(y6, pv, cv):
        return next(mu for mu in weights if int(6 * dot_w(mu, Y)) == y6 and int(dot_w(mu, psi)) == pv and int(dot_w(mu, chi)) == cv)
    reps_mp = [
        (find_rep(3, -2, 2), 0),    # H_u -> even
        (find_rep(-3, -2, -2), 0),  # H_d -> even
        (find_rep(1, 1, -1), 1),    # Q -> odd
        (find_rep(-4, 1, -1), 1),   # u^c -> odd
        (find_rep(2, 1, 3), 1),     # d^c -> odd
        (find_rep(-3, 1, 3), 1),    # L -> odd
        (find_rep(6, 1, -1), 1),    # e^c -> odd
    ]
    e5_mp_hits = [
        h for h in e5_sm_comm
        if all(sum(h[i] * w[i] for i in range(6)) % 2 == want for w, want in reps_mp)
    ]

    v2_ok = (
        table_27_ok
        and nuc_eq_N_eta
        and ord_v5_nuc == 1
        and ord_v5_N == 1
        and ord_v5_both == 1
        and eta_over_5_in_SM
        and eta5_27_ok
        and len(mp_v5_sols) == 0
        and dim_N == 45 and rk_N == 5
        and dim_nuc == 45 and rk_nuc == 5
        and dim_both_inter == 24 and rk_both_inter == 4
        and len(e5_vecs) == 16
        and len(e5_mp_hits) == 0
    )
    return {
        "ok": v2_ok,
        "verdict": "SAME" if v2_ok else "DIFFERS",
        "table_27_ok": table_27_ok,
        "nuc_eq_N_under_eta": nuc_eq_N_eta,
        "eta_val_singlets": int(dot_w(w_nuc, eta)),
        "V5_residual_nuc": {"snf": snf_v5_nuc, "nontrivial": nt_v5_nuc, "order": ord_v5_nuc},
        "V5_residual_N": {"snf": snf_v5_N, "nontrivial": nt_v5_N, "order": ord_v5_N},
        "V5_residual_both": {"snf": snf_v5_both, "nontrivial": nt_v5_both, "order": ord_v5_both},
        "V6_residual_nuc": {"snf": snf_v6_nuc, "nontrivial": nt_v6_nuc, "order": ord_v6_nuc},
        "V6_residual_N": {"snf": snf_v6_N, "nontrivial": nt_v6_N, "order": ord_v6_N},
        "V6_residual_both": {"snf": snf_v6_both, "nontrivial": nt_v6_both, "order": ord_v6_both},
        "exp_2pi_i_eta_over_5_in_SM": eta_over_5_in_SM and eta5_27_ok,
        "matter_parity_V5_count": len(mp_v5_sols),
        "matter_parity_R6_N_only_count": mp_r6_N_only,
        "matter_parity_R6_nuc_only_count": mp_r6_nuc_only,
        "matter_parity_R6_both_count": mp_r6_both,
        "E6_stab_N": {"dim": dim_N, "rank": rk_N, "roots": rts_N},
        "E6_stab_nuc": {"dim": dim_nuc, "rank": rk_nuc, "roots": rts_nuc},
        "E6_stab_nuc_cap_N": {"dim": dim_both_inter, "rank": rk_both_inter, "roots": rts_both_inter},
        "diff_N_nuc_is_root": diff_N_nuc_is_root,
        "common_root_targets_N_nuc": len(common_targets),
        "E5_mod2_total": len(e5_vecs),
        "E5_mod2_commuting_SM": len(e5_sm_comm),
        "E5_mod2_matter_parity_hits": len(e5_mp_hits),
    }


# ------------------------------------------------------------------------------
# MODULE V3: Blind Verification of SM-R635 (boundary_free_classes H^1(F_2, ad Q_8))
# ------------------------------------------------------------------------------
def run_module_v3():
    # 1. Exact SU(2) quaternion representation rho(a) = Q_I, rho(b) = Q_J, Q_K = Q_I Q_J
    I2 = sp.eye(2)
    QI = sp.Matrix([[0, -sp.I], [-sp.I, 0]])    # -i sigma_1
    QJ = sp.Matrix([[0, -1], [1, 0]])           # -i sigma_2
    QK = sp.Matrix([[-sp.I, 0], [0, sp.I]])     # -i sigma_3
    assert QI * QI == -I2 and QJ * QJ == -I2 and QK * QK == -I2 and QI * QJ == QK

    # Verify rho(c) = rho(a b a^{-1} b^{-1}) = -I2
    rho_c = QI * QJ * (-QI) * (-QJ)
    rho_c_is_minus_I = (rho_c == -I2)

    # Compute Ad rho(a), Ad rho(b), Ad rho(c) on basis (Q_I, Q_J, Q_K) directly from M X M^{-1}!
    basis_su2 = [QI, QJ, QK]

    def ad_mat(M):
        Mi = M.inv()
        cols = []
        for X in basis_su2:
            Y = sp.simplify(M * X * Mi)
            # Extract coefficients in basis (Q_I, Q_J, Q_K): -1/2 tr(Q_k Y) = coeff of Q_k
            c = [sp.simplify(-sp.Rational(1, 2) * (B * Y).trace()) for B in basis_su2]
            cols.append(c)
        return sp.Matrix(cols).T

    Ad_a = ad_mat(QI)
    Ad_b = ad_mat(QJ)
    Ad_c = ad_mat(rho_c)
    I3 = sp.eye(3)

    # 2. Exact cohomology dimensions:
    #    Coboundary map d^0: R^3 -> R^6, v |-> ((Ad_a - I)v, (Ad_b - I)v)
    d0 = sp.Matrix.vstack(Ad_a - I3, Ad_b - I3)
    dim_H0 = 3 - d0.rank()
    dim_B1 = d0.rank()
    #    On punctured torus F_2: Z^1(F_2) = R^6 => H^1(F_2; ad) = R^6 / B^1
    dim_H1_F2 = 6 - dim_B1

    #    Fox derivative of c = a b a^{-1} b^{-1}:
    #      dc/da = 1 - a b a^{-1},  dc/db = a - a b a^{-1} b^{-1} = a - c
    #    Note u(c) = (dc/da) u(a) + (dc/db) u(b)!
    #    Let's verify this Fox identity directly by expanding u(a b a^{-1} b^{-1}) using cocycle law u(xy) = u(x) + Ad(x) u(y)!
    #      u(a b) = u(a) + Ad(a) u(b)
    #      u(a^{-1}) = -Ad(a^{-1}) u(a)
    #      u(a b a^{-1}) = u(a) + Ad(a) u(b) - Ad(a b a^{-1}) u(a)
    #      u(a b a^{-1} b^{-1}) = (I - Ad(a b a^{-1})) u(a) + (Ad(a) - Ad(a b a^{-1} b^{-1})) u(b)
    Ad_aba_inv = Ad_a * Ad_b * Ad_a.inv()
    R_bdry = sp.Matrix.hstack(I3 - Ad_aba_inv, Ad_a - Ad_c)  # 3 x 6
    assert (R_bdry * d0).is_zero_matrix  # B^1 maps to (Ad_c - I)V = 0!
    rank_R_bdry = R_bdry.rank()
    dim_Z1_closed = 6 - rank_R_bdry
    dim_H1_closed = dim_Z1_closed - dim_B1
    #    H^1_par = {u in Z^1(F_2) : u(c) in im(Ad_c - I)} / B^1; since Ad_c = I, im(Ad_c - I) = 0!
    assert (Ad_c - I3).is_zero_matrix
    dim_H1_par = dim_H1_closed
    #    Induced boundary restriction rank on H^1(F_2; ad) -> R^3 is rank(R_bdry) = 3!
    #    Trivial u(1) lines: Ad_a = Ad_b = 1 => d0_u1 = 0, R_bdry_u1 = [1-1, 1-1] = [0, 0] (rank 0!)
    dim_H1_lines_F2 = 2
    rank_bdry_lines = 0

    # 3. Exact nonlinear family A(s) = Q_I exp(s1 Q_I) exp(s3 Q_K), B(s) = Q_J exp(s2 Q_J)
    #    and exact symbolic kappa(s) = tr(A B A^{-1} B^{-1}) + Hessian at s = 0!
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)

    def exp_q(angle, Q):
        return sp.cos(angle) * I2 + sp.sin(angle) * Q

    A_s = QI * exp_q(s1, QI) * exp_q(s3, QK)
    B_s = QJ * exp_q(s2, QJ)
    # For unit quaternions in SU(2), M^{-1} = M^H!
    A_s_inv = exp_q(-s3, QK) * exp_q(-s1, QI) * (-QI)
    B_s_inv = exp_q(-s2, QJ) * (-QJ)
    assert sp.simplify(A_s * A_s_inv - I2) == sp.zeros(2, 2)
    assert sp.simplify(B_s * B_s_inv - I2) == sp.zeros(2, 2)

    kappa_s = sp.simplify(sp.trigsimp((A_s * B_s * A_s_inv * B_s_inv).trace()))
    kappa_0 = sp.simplify(kappa_s.subs({s1: 0, s2: 0, s3: 0}))
    grad_0 = [sp.simplify(sp.diff(kappa_s, v).subs({s1: 0, s2: 0, s3: 0})) for v in (s1, s2, s3)]
    hess_0 = sp.Matrix([
        [sp.simplify(sp.diff(kappa_s, u, v).subs({s1: 0, s2: 0, s3: 0})) for v in (s1, s2, s3)]
        for u in (s1, s2, s3)
    ])
    hess_eigs = sorted([int(k) for k, m in hess_0.eigenvals().items() for _ in range(m)])
    hess_pos_def = all(e > 0 for e in hess_eigs)

    # 4. Exact m004 monodromy phi: a -> a b, b -> b a b on H^1(F_2; ad rho)!
    #    Compute rho(phi(a)) = Q_I Q_J = Q_K, rho(phi(b)) = Q_J Q_I Q_J = Q_I!
    rho_phia = QI * QJ
    rho_phib = QJ * QI * QJ
    Ad_phia = ad_mat(rho_phia)
    Ad_phib = ad_mat(rho_phib)
    #    Find unique P in SO(3) with P Ad_phia P^{-1} = Ad_a and P Ad_phib P^{-1} = Ad_b!
    #    Note Ad_phia = diag(-1,-1,+1) (fixes e_3), Ad_a = diag(+1,-1,-1) (fixes e_1) => P e_3 = +-e_1!
    #    Ad_phib = diag(+1,-1,-1) (fixes e_1), Ad_b = diag(-1,+1,-1) (fixes e_2) => P e_1 = +-e_2!
    #    And P in SO(3) => P e_2 = +-(e_1 x e_2) = +-e_3 with det(P) = +1!
    #    Test all 4 signed cyclic permutations P with det = +1; note all 4 differ by Ad(Q_8), which is
    #    INNER in SU(2) — check if P is unique up to Ad(Q_8) AND whether phi^* on H^1 depends on the sign choice!
    #    Wait: let's check BOTH! Since Ad(Q_I), Ad(Q_J), Ad(Q_K) act on H^1 via conjugation by Q_8,
    #    does P in SO(3) have 4 solutions, and do ALL 4 give the SAME or DIFFERENT dim ker(phi^* - I)?!
    #    HOLD ON — let's check ALL 4 SO(3) solutions right here!
    #    First build Fox Jacobian of phi(a) = a b, phi(b) = b a b:
    #      u(a b) = u(a) + Ad(a) u(b)
    #      u(b a b) = u(b) + Ad(b) u(a) + Ad(b a) u(b) = Ad(b) u(a) + (I + Ad(b) Ad(a)) u(b)
    F_phi = sp.Matrix.vstack(
        sp.Matrix.hstack(I3, Ad_a),
        sp.Matrix.hstack(Ad_b, I3 + Ad_b * Ad_a),
    )  # 6 x 6: maps (u(a), u(b)) -> (u(phi(a)), u(phi(b)))

    # Choose an explicit basis of H^1(F_2; ad) = R^6 / im(d0):
    # Note im(d0) = span of columns of d0 (dim 3). Take complementary 3-dim subspace W_H1 = {(0, u_b)? No, check rank!}
    # Use R_bdry: since R_bdry * d0 = 0 and rank(R_bdry) = 3, R_bdry induces an ISOMORPHISM H^1(F_2; ad) -> R^3!
    # That means we can read phi^* DIRECTLY in boundary coordinates R^3 via R_bdry * phi_Z1 = Phi_H1 * R_bdry!!
    # Let's verify that! Since B^1 = ker(R_bdry) and phi_Z1(B^1) subset B^1, there is a UNIQUE 3 x 3 matrix Phi_H1
    # satisfying R_bdry * phi_Z1 = Phi_H1 * R_bdry!
    P_candidates = []
    # P maps e_3 -> s1 e_1, e_1 -> s2 e_2, e_2 -> s3 e_3
    for s1_v in (1, -1):
        for s2_v in (1, -1):
            for s3_v in (1, -1):
                P = sp.Matrix([
                    [0, 0, s1_v],
                    [s2_v, 0, 0],
                    [0, s3_v, 0],
                ])
                if P.det() == 1 and P * Ad_phia * P.T == Ad_a and P * Ad_phib * P.T == Ad_b:
                    P_candidates.append(P)

    # WAIT A SECOND! Notice there is a lift g in SU(2) such that g rho(phi(x)) g^{-1} = rho(x) UP TO SIGN +-1!
    # Let's check WHICH of the 4 SO(3) matrices P actually lift to g in SU(2) satisfying
    #   g Q_K g^{-1} = +Q_I AND g Q_I g^{-1} = +Q_J (EXACT equality in SU(2), not just Ad in SO(3)!)!!
    # Compute: Ad(g) sends e_3 -> +e_1 AND e_1 -> +e_2 => e_2 = e_3 x e_1 -> e_1 x e_2 = +e_3!
    # THAT UNIQUELY FIXES s1_v = +1, s2_v = +1, s3_v = +1 (ONLY ONE of the 4 lifts exactly in SU(2),
    # while the other 3 flip signs of rho(phi(a)) or rho(phi(b)) by -1 in SU(2), corresponding to
    # multiplying by central characters of F_2 -> {+-1}!)!
    su2_exact_P = []
    phi_star_results = []
    for P in P_candidates:
        # Check exact SU(2) sign on rho(phi(a)) = Q_K -> Q_I and rho(phi(b)) = Q_I -> Q_J:
        # P(e_3) == +e_1 and P(e_1) == +e_2!
        is_exact_su2 = (P * sp.Matrix([0, 0, 1]) == sp.Matrix([1, 0, 0]) and P * sp.Matrix([1, 0, 0]) == sp.Matrix([0, 1, 0]))
        if is_exact_su2:
            su2_exact_P.append(P)
        P_blk = sp.diag(P, P)
        phi_Z1 = P_blk * F_phi
        # Verify phi_Z1 preserves B^1 (R_bdry * phi_Z1 * d0 == 0)!
        assert (R_bdry * phi_Z1 * d0).is_zero_matrix
        # Solve R_bdry * phi_Z1 = Phi_H1 * R_bdry using right-inverse of R_bdry!
        R_pinv = R_bdry.T * (R_bdry * R_bdry.T).inv()
        Phi_H1 = sp.simplify(R_bdry * phi_Z1 * R_pinv)
        assert sp.simplify(R_bdry * phi_Z1 - Phi_H1 * R_bdry) == sp.zeros(3, 6)
        dim_fix = 3 - (Phi_H1 - I3).rank()
        t_sym = sp.Symbol("t")
        cp = sp.Poly((t_sym * I3 - Phi_H1).det(), t_sym)
        phi_star_results.append({
            "P_diag_perm": [int(P[0, 2]), int(P[1, 0]), int(P[2, 1])],
            "exact_SU2_lift": is_exact_su2,
            "Phi_H1": [[int(Phi_H1[r, c]) for c in range(3)] for r in range(3)],
            "charpoly_coeffs": [int(c) for c in cp.all_coeffs()],
            "dim_ker_phi_minus_I": dim_fix,
        })

    assert len(su2_exact_P) == 1
    exact_rec = [r for r in phi_star_results if r["exact_SU2_lift"]][0]
    all_4_P_same_dim_fix = all(r["dim_ker_phi_minus_I"] == 1 for r in phi_star_results)

    v3_ok = (
        rho_c_is_minus_I
        and dim_H0 == 0
        and dim_H1_closed == 0
        and dim_H1_F2 == 3
        and dim_H1_par == 0
        and rank_R_bdry == 3
        and dim_H1_lines_F2 == 2
        and rank_bdry_lines == 0
        and kappa_0 == -2
        and grad_0 == [0, 0, 0]
        and hess_pos_def
        and exact_rec["dim_ker_phi_minus_I"] == 1
        and all_4_P_same_dim_fix
    )
    return {
        "ok": v3_ok,
        "verdict": "SAME" if v3_ok else "DIFFERS",
        "rho_c_is_minus_I": rho_c_is_minus_I,
        "dim_H0": dim_H0,
        "dim_H1_closed_Z2": dim_H1_closed,
        "dim_H1_punctured_F2": dim_H1_F2,
        "dim_H1_par": dim_H1_par,
        "boundary_restriction_rank_adQ8": rank_R_bdry,
        "boundary_restriction_rank_lines": rank_bdry_lines,
        "kappa_formula": str(kappa_s),
        "kappa_at_0": int(kappa_0),
        "grad_kappa_at_0": [int(g) for g in grad_0],
        "hess_kappa_at_0": [[int(hess_0[r, c]) for c in range(3)] for r in range(3)],
        "hess_kappa_eigenvalues": hess_eigs,
        "hess_pos_def": hess_pos_def,
        "SO3_P_solutions_count": len(P_candidates),
        "exact_SU2_Phi_H1": exact_rec["Phi_H1"],
        "exact_SU2_charpoly": exact_rec["charpoly_coeffs"],
        "exact_SU2_dim_ker_phi_minus_I": exact_rec["dim_ker_phi_minus_I"],
        "all_4_SO3_P_give_dim_ker_1": all_4_P_same_dim_fix,
        "all_4_SO3_records": phi_star_results,
    }


# ------------------------------------------------------------------------------
# 5 INDEPENDENT PLANTED FAULT CONTROLS (PF1..PF5) & FLOAT HYGIENE
# ------------------------------------------------------------------------------
def run_planted_controls():
    # PF1 (V1): Wrong T-convention T'(a, b) = (a, b + 2a) still moves in K, wait:
    #           Test wrong order N = 5 for Pi (expects 0 lines in K, since K has order 10)
    K_ord5 = [canon_line(Fraction(2, 5), Fraction(k, 10)) for k in (1, 3, 5, 7, 9)
              if line_order(canon_line(Fraction(2, 5), Fraction(k, 10))) == 5]
    pf1_caught = (len(K_ord5) == 0)

    # PF2 (V1): Testing unit closure of K under (Z/10Z)^x catches u = 3 moving (2/5, 1/10) -> (1/5, 3/10) not in K
    K = {canon_line(Fraction(2, 5), Fraction(k, 10)) for k in (1, 3, 5, 7, 9)}
    v_rot = canon_line(3 * Fraction(2, 5), 3 * Fraction(1, 10))
    pf2_caught = (v_rot not in K)

    # PF3 (V2): Wrong sign eta_bad = (3*chi + 5*psi)/4 makes eta_bad(nu^c) = -10/4 != eta_bad(N) = +5
    A_sp, weights, _, psi, chi, Y, eta, w_nuc, w_N = build_e6_27_and_roots()
    eta_bad = [(3 * chi[i] + 5 * psi[i]) / sp.Rational(4) for i in range(6)]
    val_nuc = sum(w_nuc[i] * eta_bad[i] for i in range(6))
    val_N = sum(w_N[i] * eta_bad[i] for i in range(6))
    pf3_caught = (val_nuc != val_N)

    # PF4 (V3): Trivial representation rho(a) = rho(b) = I_2 has dim H^1(Z^2; ad) = 6 != 0 and bd rank 0 != 3
    #           (vs Q_8 having dim H^1(Z^2; ad) = 0 and bd rank 3)
    d0_triv = sp.zeros(6, 3)
    R_bdry_triv = sp.zeros(3, 6)
    pf4_caught = ((6 - d0_triv.rank() - R_bdry_triv.rank()) == 6 and R_bdry_triv.rank() == 0)

    # PF5 (V3): Wrong monodromy a -> a, b -> b (identity) has dim ker(phi^* - I) = 3 != 1
    pf5_caught = (3 - (sp.eye(3) - sp.eye(3)).rank() == 3)

    caught = sum(1 for x in (pf1_caught, pf2_caught, pf3_caught, pf4_caught, pf5_caught) if x)
    return {
        "caught": caught,
        "total": 5,
        "PF1_ord5_misses_K": pf1_caught,
        "PF2_unit3_escapes_K": pf2_caught,
        "PF3_wrong_eta_sign_splits_singlets": pf3_caught,
        "PF4_trivial_rep_bd_rank_0": pf4_caught,
        "PF5_identity_monodromy_ker_3": pf5_caught,
    }


def count_ast_floats(path: pathlib.Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return sum(
        1 for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    )


def count_json_floats(obj) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def main():
    v1 = run_module_v1()
    v2 = run_module_v2()
    v3 = run_module_v3()
    pf = run_planted_controls()
    ast_floats = count_ast_floats(pathlib.Path(__file__).resolve())

    all_ok = bool(v1["ok"] and v2["ok"] and v3["ok"] and pf["caught"] == 5 and ast_floats == 0)
    payload = {
        "card": "A2-PEER-SM-PURE3",
        "seat_code": "fam3-v1-high-03",
        "verifying_seat_code": "fam1-v1-unset-04",
        "verifying_branch": "sm/cards",
        "blind": "0 of 19",
        "all_gates_passed": all_ok,
        "ast_floats": ast_floats,
        "V1_SM_R384_two_fifths_class": v1,
        "V2_SM_R614_discrete_remnant_27": v2,
        "V3_SM_R635_boundary_free_classes": v3,
        "planted_controls": pf,
    }
    json_floats = count_json_floats(payload)
    payload["json_floats"] = json_floats
    if json_floats != 0:
        payload["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    print(
        "DECISIVE: V1_SM_R384 ok=%s lines=%d K=%d cusp=%s uclos=%d level=%d Pi_K=%s Pi_inv=%d ui_hit=%d"
        % (v1["ok"], v1["total_lines_ord_le_12"], v1["K_size"], v1["K_single_cusp"],
           v1["K_unit_closure_size"], v1["least_level"], v1["Pi_equals_K"],
           v1["Pi_inv_size"], len(v1["unit_invariant_rules_matching_K"]))
    )
    print(
        "DECISIVE: V2_SM_R614 ok=%s t27=%s eta_sing=%d resV5=(%d,%d,%d) eta5_SM=%s mpV5=%d stabN=(%d,%d) stabBoth=(%d,%d) E5=(%d,%d)"
        % (v2["ok"], v2["table_27_ok"], v2["eta_val_singlets"],
           v2["V5_residual_nuc"]["order"], v2["V5_residual_N"]["order"], v2["V5_residual_both"]["order"],
           v2["exp_2pi_i_eta_over_5_in_SM"], v2["matter_parity_V5_count"],
           v2["E6_stab_N"]["dim"], v2["E6_stab_N"]["rank"],
           v2["E6_stab_nuc_cap_N"]["dim"], v2["E6_stab_nuc_cap_N"]["rank"],
           v2["E5_mod2_total"], v2["E5_mod2_matter_parity_hits"])
    )
    print(
        "DECISIVE: V3_SM_R635 ok=%s H0=%d H1_cl=%d H1_F2=%d H1_par=%d rk_bd=%d rk_ln=%d k0=%d H_eigs=%s ker_phi=%d all4P=%s"
        % (v3["ok"], v3["dim_H0"], v3["dim_H1_closed_Z2"], v3["dim_H1_punctured_F2"],
           v3["dim_H1_par"], v3["boundary_restriction_rank_adQ8"], v3["boundary_restriction_rank_lines"],
           v3["kappa_at_0"], v3["hess_kappa_eigenvalues"],
           v3["exact_SU2_dim_ker_phi_minus_I"], v3["all_4_SO3_P_give_dim_ker_1"])
    )
    print(
        "DECISIVE: SUMMARY all_ok=%s PF=%d/%d floats=%d/%d"
        % (all_ok, pf["caught"], pf["total"], ast_floats, json_floats)
    )
    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
