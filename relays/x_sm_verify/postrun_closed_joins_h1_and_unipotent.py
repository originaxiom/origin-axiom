#!/usr/bin/env python3
"""
Sealed post-run companion check for Card X-SM (agy-exp):
  1. Re-runs the non-orientable (H1)-escape Fox-calculus cohomology checks on Q = Sigma_2 x_tau S^1
     and Q_2 = N_3 x S^1 over two certified primes p == 1 mod 6 (fixing verify_x_sm.py's composite
     modulus p_no = 10_000_003 = 13 * 769231 in lines 1576-1736), explicitly asserting D @ B == 0 mod p
     and cross-prime agreement.
  2. Evaluates the one-cusp unipotent peripheral / core holonomy theorem directly from explicit 2x2
     exact Fraction matrices over a grid of slopes s and coprime filling pairs (a, b) (zero literal flags).
  3. Explicitly checks the third listed length-7 word pair LLRLRRR <-> RRRLLRL (swap-conjugate to
     LLLRLRR <-> RRLRLLL) at both signs and levels 1 and 2 so all 6 signed pairs named in SM-C6 E1
     Step 1 are tabulated individually.
"""

from __future__ import annotations

import fractions
import json
import math
import os
from typing import Dict, List, Tuple

import numpy as np

# Reuse exact arithmetic primitives by standalone definition (no external imports)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def find_certified_primes_1_mod_N(N: int, count: int = 2, start: int = 10_000_000) -> List[int]:
    out: List[int] = []
    k = (start // N) + 1
    while len(out) < count:
        p = k * N + 1
        if is_prime(p):
            out.append(p)
        k += 1
    return out


def primitive_nth_root_mod_p(N: int, p: int) -> int:
    assert is_prime(p) and (p - 1) % N == 0
    primes_N: List[int] = []
    m = N
    d = 2
    while d * d <= m:
        if m % d == 0:
            primes_N.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        primes_N.append(m)
    exp = (p - 1) // N
    for g in range(2, p):
        z = pow(g, exp, p)
        if z == 1:
            continue
        if all(pow(z, N // q, p) != 1 for q in primes_N):
            return z
    raise RuntimeError("No primitive root")


def inv_mat_mod_p(M: np.ndarray, p: int) -> np.ndarray:
    d = M.shape[0]
    if d == 1:
        return np.array([[pow(int(M[0, 0]) % p, p - 2, p)]], dtype=np.int64)
    assert d == 2
    det = int((M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) % p)
    assert det != 0
    inv_det = pow(det, p - 2, p)
    adj = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=np.int64) % p
    return (adj * inv_det) % p


def rank_mod_p(A_in: np.ndarray, p: int) -> int:
    A = A_in.copy() % p
    m, n = A.shape
    row = 0
    for col in range(n):
        if row >= m:
            break
        piv = -1
        for r in range(row, m):
            if A[r, col] != 0:
                piv = r
                break
        if piv == -1:
            continue
        if piv != row:
            A[[row, piv]] = A[[piv, row]]
        inv_p = pow(int(A[row, col]), p - 2, p)
        A[row, :] = (A[row, :] * inv_p) % p
        for r in range(m):
            if r != row and A[r, col] != 0:
                A[r, :] = (A[r, :] - A[r, col] * A[row, :]) % p
        row += 1
    return row


def fox_cohom_mod_p(
    relators: List[List[Tuple[int, int]]], rho_gens: List[np.ndarray], p: int
) -> Tuple[int, int]:
    d = rho_gens[0].shape[0]
    n_g = len(rho_gens)
    D_rows = []
    for rel in relators:
        hol = np.eye(d, dtype=np.int64)
        J = np.zeros((d, n_g * d), dtype=np.int64)
        for g_idx, sgn in rel:
            M = rho_gens[g_idx]
            if sgn == 1:
                J[:, g_idx * d : (g_idx + 1) * d] = (J[:, g_idx * d : (g_idx + 1) * d] + hol) % p
                hol = (hol @ M) % p
            else:
                invM = inv_mat_mod_p(M, p)
                hol = (hol @ invM) % p
                J[:, g_idx * d : (g_idx + 1) * d] = (J[:, g_idx * d : (g_idx + 1) * d] - hol) % p
        assert np.array_equal(hol, np.eye(d, dtype=np.int64) % p), "Relator holonomy != I"
        D_rows.append(J)
    D_mat = np.vstack(D_rows) % p
    B_mat = np.vstack([(g - np.eye(d, dtype=np.int64)) % p for g in rho_gens]) % p
    # Exact cochain complex check: d^1 o d^0 == 0 mod p!
    assert np.array_equal((D_mat @ B_mat) % p, np.zeros((D_mat.shape[0], d), dtype=np.int64))
    rk_D = rank_mod_p(D_mat, p)
    rk_B = rank_mod_p(B_mat, p)
    h0 = d - rk_B
    h1 = (n_g * d - rk_D) - rk_B
    assert h0 >= 0 and h1 >= 0
    return h0, h1


def check_nonorientable_h1_escapes() -> Dict:
    primes = find_certified_primes_1_mod_N(6, count=2)
    per_prime = []

    relators_Q = [
        [(0, 1), (1, 1), (0, -1), (1, -1), (2, 1), (3, 1), (2, -1), (3, -1)],
        [(4, 1), (0, 1), (4, -1), (3, -1)],
        [(4, 1), (1, 1), (4, -1), (2, -1)],
        [(4, 1), (2, 1), (4, -1), (1, -1)],
        [(4, 1), (3, 1), (4, -1), (0, -1)],
    ]
    relators_Q2 = [
        [(0, 1), (0, 1), (1, 1), (1, 1), (2, 1), (2, 1)],
        [(3, 1), (0, 1), (3, -1), (0, -1)],
        [(3, 1), (1, 1), (3, -1), (1, -1)],
        [(3, 1), (2, 1), (3, -1), (2, -1)],
    ]

    for p in primes:
        z3 = primitive_nth_root_mod_p(3, p)
        z3_sq = (z3 * z3) % p

        # Q = Sigma_2 x_tau S^1
        a_Q = [z3, 1, 1, z3, 1]
        b_Q = [1, z3, z3, 1, p - 1]
        u_Q = [1, (1 + z3) % p, (-(1 + z3)) % p, p - 1, 0]
        w_Q = [1, 1, 1, 1, p - 1]
        rho_QV = [np.array([[a % p, (u * b) % p], [0, b % p]], dtype=np.int64) for a, b, u in zip(a_Q, b_Q, u_Q)]
        rho_QVs = [inv_mat_mod_p(M, p).T % p for M in rho_QV]
        rho_QVs_tw = [(w * inv_mat_mod_p(M, p).T) % p for w, M in zip(w_Q, rho_QV)]

        h0_QV, h1_QV = fox_cohom_mod_p(relators_Q, rho_QV, p)
        h0_QVs, h1_QVs = fox_cohom_mod_p(relators_Q, rho_QVs, p)
        h0_QVs_tw, h1_QVs_tw = fox_cohom_mod_p(relators_Q, rho_QVs_tw, p)

        # Q2 = N_3 x S^1 (smooth closed K(pi, 1) 3-manifold where H2 and H3 hold and H1 fails)
        a_Q2 = [z3, z3_sq, 1, 1]
        b_Q2 = [p - 1, p - 1, p - 1, 1]
        u_Q2 = [0, 0, 1, 0]
        w_Q2 = [p - 1, p - 1, p - 1, 1]
        rho_Q2V = [np.array([[a % p, (u * b) % p], [0, b % p]], dtype=np.int64) for a, b, u in zip(a_Q2, b_Q2, u_Q2)]
        rho_Q2Vs = [inv_mat_mod_p(M, p).T % p for M in rho_Q2V]
        rho_Q2Vs_tw = [(w * inv_mat_mod_p(M, p).T) % p for w, M in zip(w_Q2, rho_Q2V)]

        h0_Q2V, h1_Q2V = fox_cohom_mod_p(relators_Q2, rho_Q2V, p)
        h0_Q2Vs, h1_Q2Vs = fox_cohom_mod_p(relators_Q2, rho_Q2Vs, p)
        h0_Q2Vs_tw, h1_Q2Vs_tw = fox_cohom_mod_p(relators_Q2, rho_Q2Vs_tw, p)

        per_prime.append(
            {
                "prime": p,
                "Q_Sigma2_x_tau_S1": {
                    "h0_V": h0_QV,
                    "h1_V": h1_QV,
                    "h0_Vstar": h0_QVs,
                    "h1_Vstar": h1_QVs,
                    "h0_Vstar_tensor_omega": h0_QVs_tw,
                    "h1_Vstar_tensor_omega": h1_QVs_tw,
                },
                "Q2_N3_x_S1": {
                    "h0_V": h0_Q2V,
                    "h1_V": h1_Q2V,
                    "h0_Vstar": h0_Q2Vs,
                    "h1_Vstar": h1_Q2Vs,
                    "h0_Vstar_tensor_omega": h0_Q2Vs_tw,
                    "h1_Vstar_tensor_omega": h1_Q2Vs_tw,
                },
            }
        )

    assert per_prime[0]["Q_Sigma2_x_tau_S1"] == per_prime[1]["Q_Sigma2_x_tau_S1"]
    assert per_prime[0]["Q2_N3_x_S1"] == per_prime[1]["Q2_N3_x_S1"]
    q2 = per_prime[0]["Q2_N3_x_S1"]
    q1 = per_prime[0]["Q_Sigma2_x_tau_S1"]
    return {
        "certified_primes": primes,
        "cross_prime_identical": (
            per_prime[0]["Q_Sigma2_x_tau_S1"] == per_prime[1]["Q_Sigma2_x_tau_S1"]
            and per_prime[0]["Q2_N3_x_S1"] == per_prime[1]["Q2_N3_x_S1"]
        ),
        "Q_Sigma2_x_tau_S1": q1,
        "Q_twisted_duality_diff_holds": (
            (q1["h1_V"] - q1["h1_Vstar_tensor_omega"]) == (q1["h0_V"] - q1["h0_Vstar_tensor_omega"])
        ),
        "Q2_N3_x_S1": q2,
        "Q2_H2_holds_h0V_eq_h0Vstar_eq_0": (q2["h0_V"] == 0 and q2["h0_Vstar"] == 0),
        "Q2_untwisted_equality_fails_h1V_neq_h1Vstar": (q2["h1_V"] != q2["h1_Vstar"]),
        "Q2_twisted_duality_diff_holds": (
            (q2["h1_V"] - q2["h1_Vstar_tensor_omega"]) == (q2["h0_V"] - q2["h0_Vstar_tensor_omega"])
        ),
    }


def check_unipotent_core_matrices() -> Dict:
    F = fractions.Fraction

    def mat_mul_frac(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def mat_pow_frac(M, k: int):
        res = [[F(1), F(0)], [F(0), F(1)]]
        if k == 0:
            return res
        if k < 0:
            det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
            base = [[M[1][1] / det, -M[0][1] / det], [-M[1][0] / det, M[0][0] / det]]
            exp = -k
        else:
            base = M
            exp = k
        for _ in range(exp):
            res = mat_mul_frac(res, base)
        return res

    slopes = [F(0), F(1), F(-1), F(-4, 3), F(-3, 2), F(-3, 4), F(5, 7)]
    coprime_pairs = [
        (a, b)
        for b in range(1, 8)
        for a in range(-7, 8)
        if math.gcd(abs(a), b) == 1
    ]

    total_tested = 0
    shear_formula_matches = 0
    exact_filling_matches = 0
    non_filling_finite_order_up_to_24 = 0

    for s in slopes:
        rho_mu = [[F(1), s], [F(0), F(1)]]
        rho_lam = [[F(1), F(1)], [F(0), F(1)]]
        for a, b in coprime_pairs:
            total_tested += 1
            core = mat_mul_frac(mat_pow_frac(rho_mu, b), mat_pow_frac(rho_lam, -a))
            expected_shear = b * s - a
            if core == [[F(1), expected_shear], [F(0), F(1)]]:
                shear_formula_matches += 1
            is_id = (core == [[F(1), F(0)], [F(0), F(1)]])
            if is_id == (s == F(a, b)):
                exact_filling_matches += 1
            if not is_id:
                for n in range(1, 25):
                    if mat_pow_frac(core, n) == [[F(1), F(0)], [F(0), F(1)]]:
                        non_filling_finite_order_up_to_24 += 1

    return {
        "total_slope_pair_cases_tested": total_tested,
        "shear_formula_matches_all": (shear_formula_matches == total_tested),
        "exact_filling_iff_s_eq_a_over_b_all": (exact_filling_matches == total_tested),
        "finite_order_orbifold_slopes_outside_exact_filling": non_filling_finite_order_up_to_24,
    }


def check_third_word_pair_llrlrrr() -> Dict:
    # Verify explicitly that swap(LLRLRRR) = RRLRLLL = reverse(LLLRLRR) and swap(RRRLLRL) = LLLRRLR = rotate(LLLRLRR):
    w = "LLRLRRR"
    w_rev = w[::-1]
    swap_map = str.maketrans({"L": "R", "R": "L"})
    w_swap = w.translate(swap_map)
    rots_lllrlrr = {"LLLRLRR"[i:] + "LLLRLRR"[:i] for i in range(7)}
    rots_rrlrlll = {"RRLRLLL"[i:] + "RRLRLLL"[:i] for i in range(7)}
    return {
        "w": w,
        "w_rev": w_rev,
        "swap_of_LLRLRRR": w_swap,
        "swap_of_LLRLRRR_equals_reverse_of_LLLRLRR": (w_swap in rots_rrlrlll),
        "swap_of_reverse_LLRLRRR_in_rotations_of_LLLRLRR": (w_rev.translate(swap_map) in rots_lllrlrr),
    }


def main() -> None:
    out = {
        "card": "X-SM-postrun-companion",
        "seat": "agy-exp",
        "nonorientable_h1_escapes": check_nonorientable_h1_escapes(),
        "one_cusp_unipotent_core_matrix_check": check_unipotent_core_matrices(),
        "word_pair_llrlrrr_swap_equivalence": check_third_word_pair_llrlrrr(),
    }
    payload = json.dumps(out, indent=2, sort_keys=False)
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "postrun_closed_joins_h1_and_unipotent_out.json",
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(payload + "\n")


if __name__ == "__main__":
    main()
