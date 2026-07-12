#!/usr/bin/env python3
"""B533 Probe 2: The Five Types.

Probe 1 found 5 distinct Perron eigenvector types across 34 observation
points. This probe examines:

  (a) The algebraic structure of each type's Perron vector
  (b) What property of the factor u determines its type
  (c) Whether the 5 types relate to known structural features
  (d) The exact dimensionless ratios within each type
  (e) Convergence: does the type classification stabilize with host depth?
"""

import sys
import os
import numpy as np
from collections import defaultdict
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, original_matrix, canonical_codes,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = list('abAB')
SIGMA_CODES = ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2))
SIGMA_CANONICAL = canonical_codes(SIGMA_CODES)
X = sp.Symbol('x')

PHI = (1 + np.sqrt(5)) / 2
SQ_PHI = np.sqrt(PHI)


def parikh(word):
    return np.array([word.count(c) for c in 'abAB'], dtype=float)


def perron_eigenvector(matrix_sp):
    M = np.array(matrix_sp.tolist(), dtype=float)
    eigenvalues, eigenvectors = np.linalg.eig(M)
    idx = np.argmax(np.abs(eigenvalues.real))
    v = eigenvectors[:, idx].real
    if np.any(v < 0):
        v = -v
    return v / v.sum(), eigenvalues[idx].real


def analyze_point(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 2 * trim + 2:
        return None
    return_words = standard_return_words_from_positions(host, positions, trim=trim)
    if len(return_words) < 2:
        return None
    induced = canonical_induced_system(return_words, max_power=2)
    if induced is None:
        return None
    v, beta = perron_eigenvector(induced['matrix'])
    P = np.zeros((len(return_words), 4))
    for i, rw in enumerate(return_words):
        P[i] = parikh(rw)
    eff = P.T @ v
    eff = eff / eff.sum()
    return {
        'factor': factor,
        'return_words': return_words,
        'return_count': len(return_words),
        'induced': induced,
        'perron_vec': v,
        'beta': beta,
        'eff_freq': eff,
        'parikh_matrix': P,
        'is_self': induced['canonical_codes'] == SIGMA_CANONICAL,
    }


def type_key(v, precision=4):
    return tuple(np.round(np.sort(v)[::-1], precision))


def main():
    print("=" * 78)
    print("B533 Probe 2 — The Five Types")
    print("=" * 78)

    # ─── Collect all observation points at depth 10 ───
    host10 = grow(10)
    results = []
    for length in range(1, 5):
        fpm = factor_position_map(host10, length)
        for factor in sorted(fpm.keys()):
            r = analyze_point(factor, host10)
            if r:
                results.append(r)

    # ─── Cluster by Perron eigenvector type ───
    types = defaultdict(list)
    for r in results:
        key = type_key(r['perron_vec'])
        types[key].append(r)

    print(f"\nTotal observation points: {len(results)}")
    print(f"Distinct types: {len(types)}")

    # ─── PART A: Detailed profile of each type ───
    print("\n" + "=" * 78)
    print("PART A — Type profiles")
    print("=" * 78)

    type_list = sorted(types.items(), key=lambda kv: -len(kv[1]))

    for i, (key, group) in enumerate(type_list):
        print(f"\n  TYPE {i+1}: {len(group)} observation points")
        print(f"  Perron vector (sorted): [{', '.join(f'{k:.6f}' for k in key)}]")
        print(f"  Return count: {group[0]['return_count']}")
        print(f"  Self-recovery: {sum(r['is_self'] for r in group)}/{len(group)}")

        # Factors in this type
        factors = [r['factor'] for r in group]
        print(f"  Factors: {', '.join(factors)}")

        # Effective letter frequencies
        eff = group[0]['eff_freq']
        print(f"  Eff. letter freq: a={eff[0]:.6f}, b={eff[1]:.6f}, "
              f"A={eff[2]:.6f}, B={eff[3]:.6f}")

        # Dimensionless ratios
        if eff[1] > 0 and eff[3] > 0:
            print(f"  f_a/f_b = {eff[0]/eff[1]:.6f} (global: {PHI:.6f})")
            print(f"  f_A/f_B = {eff[2]/eff[3]:.6f} (global: {PHI:.6f})")
            print(f"  f_a/f_A = {eff[0]/eff[2]:.6f} (global: {1/SQ_PHI:.6f})")

        # Return-word details
        print(f"  Return words (from first factor '{factors[0]}'):")
        r0 = group[0]
        for j, rw in enumerate(r0['return_words']):
            pk = parikh(rw)
            print(f"    R_{j}: {rw:20s}  |R|={len(rw):2d}  "
                  f"Parikh=({int(pk[0])},{int(pk[1])},{int(pk[2])},{int(pk[3])})")

        # Perron vector (unsorted, in return-word order)
        v = r0['perron_vec']
        print(f"  Perron vec (rw order): [{', '.join(f'{x:.6f}' for x in v)}]")

        # Gap labels
        v_sorted = np.sort(v)[::-1]
        gaps = np.cumsum(v_sorted[:-1])
        print(f"  Gap labels: [{', '.join(f'{g:.6f}' for g in gaps)}]")

        # Canonical codes
        print(f"  Canonical codes: {r0['induced']['canonical_codes']}")

    # ─── PART B: What determines the type? ───
    print("\n" + "=" * 78)
    print("PART B — What property of u determines its type?")
    print("=" * 78)

    # Hypothesis 1: the type depends on the LAST LETTER of u
    print("\n  Hypothesis 1: type depends on the last letter of u")
    for i, (key, group) in enumerate(type_list):
        last_letters = [r['factor'][-1] for r in group]
        counter = defaultdict(int)
        for ll in last_letters:
            counter[ll] += 1
        print(f"    Type {i+1}: last letters = {dict(counter)}")

    # Hypothesis 2: the type depends on the FIRST letter of u
    print("\n  Hypothesis 2: type depends on the first letter of u")
    for i, (key, group) in enumerate(type_list):
        first_letters = [r['factor'][0] for r in group]
        counter = defaultdict(int)
        for fl in first_letters:
            counter[fl] += 1
        print(f"    Type {i+1}: first letters = {dict(counter)}")

    # Hypothesis 3: the type depends on the first BIGRAM of u (or its last bigram)
    print("\n  Hypothesis 3: type depends on the last bigram of u")
    for i, (key, group) in enumerate(type_list):
        last_bigrams = []
        for r in group:
            f = r['factor']
            if len(f) >= 2:
                last_bigrams.append(f[-2:])
            else:
                last_bigrams.append(f)
        counter = defaultdict(int)
        for lb in last_bigrams:
            counter[lb] += 1
        print(f"    Type {i+1}: last bigrams = {dict(counter)}")

    # Hypothesis 4: the type depends on which BOUNDARY bigram u creates
    # When u appears between two return words, the boundary bigram is
    # (last letter of prev return word) + (first letter of u)
    # and (last letter of u) + (first letter of next return word)
    print("\n  Hypothesis 4: type depends on boundary bigram structure")
    print("    (the bigram at the u-boundary: last_of_u + first_after_u)")
    for i, (key, group) in enumerate(type_list):
        # Each return word starts with u. So the boundary is:
        # end of R_j (which is just before the next u) → start of u
        # But the "end of R_j" is the last letter before the next occurrence of u
        # Since R_j = u || (stuff) || (just before next u),
        # the boundary bigram is (last letter before u) + u[0]
        # For the start: u ends, then the rest of the return word begins.
        # Return word = word[pos_k : pos_{k+1}] where pos_k, pos_{k+1} are
        # consecutive positions of u in the host word.
        # So R starts with u and ends just before the next u.
        # The boundary between R_j and R_{j+1} is just u itself!
        # So the "coupling bigram" is determined by u's internal structure.
        pass

    # Hypothesis 5: the type depends on how u sits in the substitution images
    print("\n  Hypothesis 5: where does u appear in σ(a), σ(b), σ(A), σ(B)?")
    images = {g: SUB[g] for g in ALPHA}
    for i, (key, group) in enumerate(type_list):
        print(f"    Type {i+1}:")
        for r in group[:3]:  # Show first 3 factors per type
            f = r['factor']
            appearances = []
            for g in ALPHA:
                img = images[g]
                pos = img.find(f)
                if pos >= 0:
                    loc = "START" if pos == 0 else ("END" if pos + len(f) == len(img) else f"pos={pos}")
                    appearances.append(f"σ({g})@{loc}")
            if appearances:
                print(f"      u='{f}' appears in: {', '.join(appearances)}")
            else:
                print(f"      u='{f}' does NOT appear in any σ-image")

    # ─── PART C: Algebraic structure of Perron vectors ───
    print("\n" + "=" * 78)
    print("PART C — Algebraic structure of the 5 Perron vectors")
    print("=" * 78)

    # For each type, try to identify the Perron eigenvector algebraically
    # using sympy exact eigenvalues
    for i, (key, group) in enumerate(type_list):
        r0 = group[0]
        M_sp = r0['induced']['matrix']
        print(f"\n  Type {i+1} (rc={r0['return_count']}):")
        print(f"    Matrix:")
        for row_idx in range(M_sp.rows):
            row = [int(M_sp[row_idx, j]) for j in range(M_sp.cols)]
            print(f"      {row}")

        # Exact charpoly
        cp = M_sp.charpoly(X)
        print(f"    Charpoly: {sp.factor(cp.as_expr())}")

        # Exact eigenvalues
        eigenvals = M_sp.eigenvals()
        print(f"    Eigenvalues (exact):")
        for ev, mult in eigenvals.items():
            print(f"      {ev} (mult {mult})")

        # Exact Perron eigenvector
        beta_exact = max(eigenvals.keys(), key=lambda e: complex(e).real)
        nullspace = (M_sp - beta_exact * sp.eye(M_sp.rows)).nullspace()
        if nullspace:
            v_exact = nullspace[0]
            # Normalize
            v_sum = sum(v_exact)
            v_norm = [sp.simplify(vi / v_sum) for vi in v_exact]
            print(f"    Perron eigenvector (exact, normalized):")
            for j, vi in enumerate(v_norm):
                print(f"      v_{j} = {vi}")

            # Check: are components expressible in terms of phi, sqrt(phi)?
            # Try to compute ratios
            if len(v_norm) >= 2:
                for j in range(1, len(v_norm)):
                    ratio = sp.simplify(v_norm[0] / v_norm[j])
                    print(f"      v_0/v_{j} = {ratio}")

    # ─── PART D: Convergence test ───
    print("\n" + "=" * 78)
    print("PART D — Convergence: do types stabilize with depth?")
    print("=" * 78)

    for depth in [8, 9, 10, 11]:
        host = grow(depth)
        type_count = defaultdict(int)
        total = 0
        for length in range(1, 4):
            fpm = factor_position_map(host, length)
            for factor in sorted(fpm.keys()):
                r = analyze_point(factor, host)
                if r:
                    key = type_key(r['perron_vec'])
                    type_count[key] += 1
                    total += 1
        print(f"  Depth {depth}: {total} points, {len(type_count)} types")
        for key in sorted(type_count.keys(), key=lambda k: -type_count[k]):
            print(f"    [{', '.join(f'{k:.4f}' for k in key)}]: {type_count[key]} points")

    # ─── PART E: The 5 gap-label sets ───
    print("\n" + "=" * 78)
    print("PART E — The 5 gap-label sets: do they relate to known quantities?")
    print("=" * 78)

    known = {
        'phi': PHI,
        '1/phi': 1/PHI,
        'sqrt_phi': SQ_PHI,
        '1/sqrt_phi': 1/SQ_PHI,
        'f_a': 0.272020,
        'f_b': 0.168117,
        'f_A': 0.346014,
        'f_B': 0.213849,
        'f_a+f_b': 0.440137,
        'f_a+f_b+f_A': 0.786151,
        '|lambda_2|': 0.440137,
        '|lambda_3|': 0.618034,
        'beta': 3.676205,
    }

    for i, (key, group) in enumerate(type_list):
        v_sorted = np.array(key)
        gaps = np.cumsum(v_sorted[:-1])
        print(f"\n  Type {i+1} gap labels: [{', '.join(f'{g:.6f}' for g in gaps)}]")
        for j, g in enumerate(gaps):
            matches = []
            for name, val in known.items():
                if abs(g - val) < 1e-4:
                    matches.append(f"{name}={val:.6f}")
            if matches:
                print(f"    gap_{j+1} = {g:.6f} ≈ {', '.join(matches)}")
            else:
                print(f"    gap_{j+1} = {g:.6f} (no match to known constants)")

        # Also check the Perron components themselves
        print(f"    Components: [{', '.join(f'{k:.6f}' for k in key)}]")
        for j, c in enumerate(key):
            matches = []
            for name, val in known.items():
                if abs(c - val) < 1e-4:
                    matches.append(f"{name}={val:.6f}")
            if matches:
                print(f"      v_{j} = {c:.6f} ≈ {', '.join(matches)}")

    # ─── SYNTHESIS ───
    print("\n" + "=" * 78)
    print("SYNTHESIS — The Five Types")
    print("=" * 78)


if __name__ == '__main__':
    main()
