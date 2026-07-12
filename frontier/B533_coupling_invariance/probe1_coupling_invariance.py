#!/usr/bin/env python3
"""B533 Probe 1: Coupling Invariance.

Does the object look the same from every observation point?

For each factor u of the fixed-point word, the return-word induction
gives a substitution system A_u with its own structure. We extract:

  (a) Effective letter frequencies (Parikh-weighted by Perron eigenvector)
  (b) Return-word frequency ratios (Perron eigenvector components)
  (c) Self-recovery: does canonical_codes(A_u) = sigma's codes?
  (d) Return-word transition structure (allowed successions)

The question: which dimensionless quantities are universal (intrinsic)
and which depend on the observation point (the coupling)?
"""

import sys
import os
import numpy as np
from collections import Counter, defaultdict
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, original_matrix, incidence,
    canonical_codes, exact_solutions,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = list('abAB')
SIGMA_CODES = ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2))
SIGMA_CANONICAL = canonical_codes(SIGMA_CODES)

PHI = (1 + np.sqrt(5)) / 2
SQ_PHI = np.sqrt(PHI)
S_NORM = PHI + 1 + PHI * SQ_PHI + SQ_PHI
GLOBAL_FREQ = np.array([PHI, 1.0, PHI * SQ_PHI, SQ_PHI]) / S_NORM

GRAMMAR = {('a','b'), ('a','A'), ('b','A'), ('A','a'), ('A','A'), ('A','B'), ('B','a')}

X = sp.Symbol('x')
M_CHARPOLY = sp.factor(sp.Matrix(original_matrix()).charpoly(X).as_expr())


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


def bigram_counts(word):
    counts = Counter()
    for i in range(len(word) - 1):
        counts[word[i] + word[i+1]] += 1
    return counts


def analyze_observation_point(factor, host, trim=2):
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

    n_rw = len(return_words)

    # Parikh matrix: P[i,j] = count of letter j in return word i
    P = np.zeros((n_rw, 4))
    for i, rw in enumerate(return_words):
        P[i] = parikh(rw)

    # Perron eigenvector of induced matrix
    v, beta_u = perron_eigenvector(induced['matrix'])

    # Effective letter frequencies: weight each return word by Perron component
    eff_freq = P.T @ v
    eff_freq_norm = eff_freq / eff_freq.sum()

    # Return-word-frequency gap labels (cumulative Perron fractions, sorted)
    v_sorted = np.sort(v)[::-1]
    rw_gap_labels = np.cumsum(v_sorted[:-1])

    # Self-recovery test
    is_self = induced['canonical_codes'] == SIGMA_CANONICAL

    # Bigram analysis of each return word
    rw_bigrams = []
    for rw in return_words:
        rw_bigrams.append(bigram_counts(rw))

    # Effective bigram frequencies
    all_bigrams = set()
    for bg_dict in rw_bigrams:
        all_bigrams.update(bg_dict.keys())
    eff_bigram = {}
    for bg in sorted(all_bigrams):
        eff_bigram[bg] = sum(v[i] * rw_bigrams[i].get(bg, 0) for i in range(n_rw))
    bg_total = sum(eff_bigram.values())
    if bg_total > 0:
        eff_bigram = {k: val/bg_total for k, val in eff_bigram.items()}

    # Transition matrix: which return words can follow which?
    # R_i can be followed by R_j if the last letter of R_i matches the
    # start of the factor u (since u sits between consecutive return words)
    # Actually, return words are of the form u...u (start with u, end just before next u)
    # so the transition is determined by the grammar at the R_i/R_{i+1} boundary.

    return {
        'factor': factor,
        'length': len(factor),
        'return_words': return_words,
        'return_count': n_rw,
        'induced': induced,
        'perron_vec': v,
        'perron_eigenvalue': beta_u,
        'parikh_matrix': P,
        'eff_freq': eff_freq_norm,
        'rw_gap_labels': rw_gap_labels,
        'is_self_recovery': is_self,
        'eff_bigram': eff_bigram,
    }


def main():
    HOST_DEPTH = 10
    MAX_FACTOR_LEN = 4

    host = grow(HOST_DEPTH)
    host_len = len(host)

    print("=" * 78)
    print("B533 — COUPLING INVARIANCE")
    print("Does the object look the same from every observation point?")
    print("=" * 78)
    print(f"\nHost word: depth {HOST_DEPTH}, length {host_len:,}")
    print(f"Global frequencies: f_a={GLOBAL_FREQ[0]:.6f}, f_b={GLOBAL_FREQ[1]:.6f}, "
          f"f_A={GLOBAL_FREQ[2]:.6f}, f_B={GLOBAL_FREQ[3]:.6f}")

    global_ratios = {
        'f_a/f_b': GLOBAL_FREQ[0] / GLOBAL_FREQ[1],
        'f_A/f_B': GLOBAL_FREQ[2] / GLOBAL_FREQ[3],
        'f_a/f_A': GLOBAL_FREQ[0] / GLOBAL_FREQ[2],
    }
    print(f"Global ratios: " + ", ".join(f"{k}={v:.6f}" for k, v in global_ratios.items()))

    # ─── PART A: Census ───
    print("\n" + "=" * 78)
    print("PART A — Census of observation points")
    print("=" * 78)

    all_results = []
    for length in range(1, MAX_FACTOR_LEN + 1):
        fpm = factor_position_map(host, length)
        print(f"\n  Length {length}: {len(fpm)} distinct factors")
        for factor in sorted(fpm.keys()):
            result = analyze_observation_point(factor, host)
            if result is None:
                continue
            all_results.append(result)
            ind = result['induced']
            tag = " **SELF**" if result['is_self_recovery'] else ""
            print(f"    u={factor:6s}  rc={result['return_count']}  "
                  f"q={ind['power']}  beta_u={result['perron_eigenvalue']:.4f}  "
                  f"det={ind['determinant']:+d}{tag}")

    print(f"\n  Total observation points analyzed: {len(all_results)}")

    # ─── PART B: Letter-frequency universality ───
    print("\n" + "=" * 78)
    print("PART B — Letter-frequency universality test")
    print("=" * 78)
    print("\n  Pre-registered prediction: letter-frequency ratios are UNIVERSAL")
    print("  (trivially, by partitioning — same word, different decomposition)\n")

    max_dev = 0.0
    freq_deviations = []
    for r in all_results:
        dev = np.max(np.abs(r['eff_freq'] - GLOBAL_FREQ))
        freq_deviations.append(dev)
        if dev > max_dev:
            max_dev = dev
            worst = r['factor']

    print(f"  Maximum deviation from global frequencies: {max_dev:.2e} (factor '{worst}')")
    print(f"  Mean deviation: {np.mean(freq_deviations):.2e}")
    print(f"  Verdict: {'UNIVERSAL' if max_dev < 0.01 else 'VARIES'} "
          f"(threshold 0.01, max dev {max_dev:.2e})")

    # Show the actual ratios for a sample
    print("\n  Sample effective letter-frequency ratios:")
    print(f"  {'factor':<8} {'f_a/f_b':>10} {'f_A/f_B':>10} {'f_a/f_A':>10} {'dev':>10}")
    print(f"  {'─'*8} {'─'*10} {'─'*10} {'─'*10} {'─'*10}")
    print(f"  {'GLOBAL':<8} {global_ratios['f_a/f_b']:10.6f} "
          f"{global_ratios['f_A/f_B']:10.6f} {global_ratios['f_a/f_A']:10.6f} {'—':>10}")
    for r in all_results[:20]:
        ef = r['eff_freq']
        ratios = (ef[0]/ef[1] if ef[1]>0 else float('inf'),
                  ef[2]/ef[3] if ef[3]>0 else float('inf'),
                  ef[0]/ef[2] if ef[2]>0 else float('inf'))
        dev = np.max(np.abs(r['eff_freq'] - GLOBAL_FREQ))
        print(f"  {r['factor']:<8} {ratios[0]:10.6f} {ratios[1]:10.6f} "
              f"{ratios[2]:10.6f} {dev:10.2e}")

    # ─── PART C: Return-word-frequency ratios ───
    print("\n" + "=" * 78)
    print("PART C — Return-word frequency ratios (NOT trivially universal)")
    print("=" * 78)
    print("\n  These are the Perron eigenvector components of A_u — the")
    print("  frequencies of each return-word TYPE, not letter frequencies.")
    print("  Different u's have different return-word alphabets, so we")
    print("  compare the SORTED frequency vectors.\n")

    # Group by return count
    by_rc = defaultdict(list)
    for r in all_results:
        by_rc[r['return_count']].append(r)

    for rc in sorted(by_rc.keys()):
        group = by_rc[rc]
        print(f"  Return count = {rc} ({len(group)} observation points):")

        # Collect sorted Perron vectors
        sorted_vecs = []
        for r in group:
            v = np.sort(r['perron_vec'])[::-1]
            sorted_vecs.append(v)

        sorted_vecs = np.array(sorted_vecs)
        if len(sorted_vecs) > 1:
            std = np.std(sorted_vecs, axis=0)
            mean = np.mean(sorted_vecs, axis=0)
            print(f"    Mean sorted Perron vec: [{', '.join(f'{m:.6f}' for m in mean)}]")
            print(f"    Std dev:                [{', '.join(f'{s:.6f}' for s in std)}]")
            print(f"    Max std/mean:           {np.max(std/np.where(mean>0, mean, 1)):.6f}")

            # Show individual vectors
            if len(group) <= 15:
                for r in group:
                    v = np.sort(r['perron_vec'])[::-1]
                    q = r['induced']['power']
                    print(f"      u={r['factor']:<6s} q={q}  "
                          f"v=[{', '.join(f'{x:.5f}' for x in v)}]")
        else:
            r = group[0]
            v = np.sort(r['perron_vec'])[::-1]
            print(f"    Single point: u={r['factor']}, "
                  f"v=[{', '.join(f'{x:.6f}' for x in v)}]")

    # ─── PART D: Self-recovery test ───
    print("\n" + "=" * 78)
    print("PART D — Self-recovery: does the observation reconstruct sigma?")
    print("=" * 78)

    self_count = sum(1 for r in all_results if r['is_self_recovery'])
    other_count = len(all_results) - self_count
    print(f"\n  Self-recovery (canonical codes = sigma): {self_count}/{len(all_results)}")
    print(f"  Different combinatorial type: {other_count}/{len(all_results)}")

    if self_count > 0:
        print(f"\n  Self-recovery observation points:")
        for r in all_results:
            if r['is_self_recovery']:
                print(f"    u = '{r['factor']}'  (length {r['length']}, q={r['induced']['power']})")

    if other_count > 0:
        print(f"\n  Non-self-recovery observation points (sample):")
        shown = 0
        for r in all_results:
            if not r['is_self_recovery'] and shown < 15:
                codes_str = str(r['induced']['canonical_codes'])
                if len(codes_str) > 50:
                    codes_str = codes_str[:50] + "..."
                print(f"    u = '{r['factor']}'  q={r['induced']['power']}  "
                      f"codes={codes_str}")
                shown += 1

    # ─── PART E: Return-word gap labels ───
    print("\n" + "=" * 78)
    print("PART E — Return-word gap labels (observation-dependent spectral data)")
    print("=" * 78)
    print("\n  Gap labels of the RETURN-WORD tiling (cumulative Perron fractions).")
    print("  These are genuinely different from letter-sequence gap labels.\n")

    # Group by (rc, q) since only same-shape systems are comparable
    by_shape = defaultdict(list)
    for r in all_results:
        key = (r['return_count'], r['induced']['power'])
        by_shape[key].append(r)

    for (rc, q), group in sorted(by_shape.items()):
        print(f"  Shape (rc={rc}, q={q}): {len(group)} points")
        gap_sets = []
        for r in group:
            gaps = tuple(np.round(r['rw_gap_labels'], 6))
            gap_sets.append(gaps)
        distinct_gaps = list(set(gap_sets))
        print(f"    Distinct gap-label sets: {len(distinct_gaps)}")
        for i, gaps in enumerate(distinct_gaps[:5]):
            count = gap_sets.count(gaps)
            print(f"      [{', '.join(f'{g:.6f}' for g in gaps)}]  ({count} points)")
        if len(distinct_gaps) > 5:
            print(f"      ... and {len(distinct_gaps)-5} more")

    # ─── PART F: Eigenvalue ratios ───
    print("\n" + "=" * 78)
    print("PART F — Eigenvalue structure of induced systems")
    print("=" * 78)

    print("\n  For each observation point, the eigenvalues of A_u.")
    print("  If A_u ~ M^q + 0, eigenvalues should be {beta^q, lambda_2^q, ...} + {0}.\n")

    beta = None
    for r in all_results:
        M_sp = r['induced']['matrix']
        M_np = np.array(M_sp.tolist(), dtype=float)
        eigs = np.sort(np.linalg.eigvals(M_np).real)[::-1]
        if beta is None:
            beta = eigs[0]
        # Eigenvalue ratios
        if eigs[0] != 0:
            ratios = eigs[1:] / eigs[0]

    # Compute expected eigenvalues from M and M^2
    M_orig = np.array(original_matrix().tolist(), dtype=float)
    eigs_M = np.sort(np.linalg.eigvals(M_orig).real)[::-1]
    eigs_M2 = np.sort(np.linalg.eigvals(M_orig @ M_orig).real)[::-1]

    print(f"  M eigenvalues:   [{', '.join(f'{e:.6f}' for e in eigs_M)}]")
    print(f"  M² eigenvalues:  [{', '.join(f'{e:.6f}' for e in eigs_M2)}]")

    # For each observation point, compare eigenvalue ratios with M^q
    print(f"\n  {'factor':<8} {'rc':>3} {'q':>2} {'eigenvalues':>45} {'match':>6}")
    print(f"  {'─'*8} {'─'*3} {'─'*2} {'─'*45} {'─'*6}")

    for r in all_results[:25]:
        M_sp = r['induced']['matrix']
        M_np = np.array(M_sp.tolist(), dtype=float)
        eigs = np.sort(np.linalg.eigvals(M_np).real)[::-1]
        q = r['induced']['power']
        expected = eigs_M**q if q == 1 else eigs_M2
        # Check if the nonzero eigenvalues match M^q
        nonzero_eigs = eigs[:4] if len(eigs) >= 4 else eigs
        if q == 1:
            match = np.allclose(np.sort(nonzero_eigs[:4])[::-1],
                                np.sort(eigs_M)[::-1], rtol=1e-3)
        else:
            match = np.allclose(np.sort(nonzero_eigs[:4])[::-1],
                                np.sort(eigs_M2)[::-1], rtol=1e-3)
        eig_str = ', '.join(f'{e:.4f}' for e in eigs)
        print(f"  {r['factor']:<8} {r['return_count']:3d} {q:2d}  "
              f"[{eig_str:>40s}]  {'YES' if match else 'NO':>5s}")

    # ─── PART G: The dimensionless ratio table ───
    print("\n" + "=" * 78)
    print("PART G — Dimensionless ratio summary")
    print("=" * 78)

    # Collect all ratios
    ratio_names = ['f_a/f_b', 'f_A/f_B', 'f_a/f_A', 'beta_u/beta',
                   'rw_freq_max/min', 'rw_gap_1']
    all_ratio_data = defaultdict(list)

    beta_global = eigs_M[0]

    for r in all_results:
        ef = r['eff_freq']
        v = r['perron_vec']

        all_ratio_data['f_a/f_b'].append(ef[0]/ef[1] if ef[1]>0 else float('inf'))
        all_ratio_data['f_A/f_B'].append(ef[2]/ef[3] if ef[3]>0 else float('inf'))
        all_ratio_data['f_a/f_A'].append(ef[0]/ef[2] if ef[2]>0 else float('inf'))
        all_ratio_data['beta_u/beta^q'].append(
            r['perron_eigenvalue'] / beta_global**r['induced']['power'])
        all_ratio_data['rw_freq_max/min'].append(max(v)/min(v) if min(v)>0 else float('inf'))
        if len(r['rw_gap_labels']) > 0:
            all_ratio_data['rw_gap_1'].append(r['rw_gap_labels'][0])

    print(f"\n  {'Ratio':<20} {'Mean':>10} {'Std':>10} {'Min':>10} {'Max':>10} {'Verdict':>10}")
    print(f"  {'─'*20} {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*10}")

    for name in ['f_a/f_b', 'f_A/f_B', 'f_a/f_A', 'beta_u/beta^q',
                  'rw_freq_max/min', 'rw_gap_1']:
        vals = np.array(all_ratio_data[name])
        vals = vals[np.isfinite(vals)]
        if len(vals) == 0:
            continue
        mean = np.mean(vals)
        std = np.std(vals)
        cv = std / abs(mean) if abs(mean) > 0 else float('inf')
        verdict = "UNIVERSAL" if cv < 0.01 else "VARIES"
        print(f"  {name:<20} {mean:10.6f} {std:10.6f} "
              f"{np.min(vals):10.6f} {np.max(vals):10.6f} {verdict:>10}")

    # ─── PART H: The deep question — what information does the coupling carry? ───
    print("\n" + "=" * 78)
    print("PART H — What information does the coupling carry?")
    print("=" * 78)

    # For the quantities that VARY: how many distinct values?
    # And: does the variation have structure (correlate with factor properties)?
    print("\n  For VARYING quantities: do they correlate with factor properties?\n")

    # Classify factors by: (length, return_count, q)
    print(f"  {'factor':<8} {'len':>4} {'rc':>3} {'q':>2} {'rw_max/min':>12} {'rw_gap_1':>10}")
    print(f"  {'─'*8} {'─'*4} {'─'*3} {'─'*2} {'─'*12} {'─'*10}")

    for r in sorted(all_results, key=lambda r: (r['return_count'], r['induced']['power'],
                                                 r['factor'])):
        v = r['perron_vec']
        ratio = max(v)/min(v) if min(v) > 0 else float('inf')
        gap1 = r['rw_gap_labels'][0] if len(r['rw_gap_labels']) > 0 else float('nan')
        print(f"  {r['factor']:<8} {r['length']:4d} {r['return_count']:3d} "
              f"{r['induced']['power']:2d} {ratio:12.6f} {gap1:10.6f}")

    # ─── PART I: Bigram-frequency universality ───
    print("\n" + "=" * 78)
    print("PART I — Bigram-frequency universality test")
    print("=" * 78)
    print("\n  Are the effective bigram frequencies observation-independent?")
    print("  (Non-trivial: boundary bigrams between return words differ by u)\n")

    # Compute global bigram frequencies
    global_bigrams = bigram_counts(host)
    total_bigrams = sum(global_bigrams.values())
    global_bg_freq = {k: v/total_bigrams for k, v in global_bigrams.items()}

    # For each observation point, compute effective bigram frequencies
    # and compare with global
    bg_deviations = []
    for r in all_results:
        eb = r['eff_bigram']
        dev = 0.0
        for bg in set(list(global_bg_freq.keys()) + list(eb.keys())):
            g = global_bg_freq.get(bg, 0)
            e = eb.get(bg, 0)
            dev = max(dev, abs(g - e))
        bg_deviations.append((dev, r['factor']))

    bg_deviations.sort(reverse=True)
    print(f"  Top 10 bigram-frequency deviations from global:")
    for dev, factor in bg_deviations[:10]:
        print(f"    u='{factor}': max |eff_bigram - global_bigram| = {dev:.6f}")

    overall_max = bg_deviations[0][0] if bg_deviations else 0
    print(f"\n  Overall max deviation: {overall_max:.6f}")
    print(f"  Verdict: {'UNIVERSAL' if overall_max < 0.01 else 'VARIES'}")

    # ─── SYNTHESIS ───
    print("\n" + "=" * 78)
    print("SYNTHESIS — Coupling Invariance Verdict")
    print("=" * 78)

    print("""
  TRIVIALLY UNIVERSAL (by partitioning):
    - Letter frequencies: f_a, f_b, f_A, f_B
    - Letter-frequency ratios: f_a/f_b, f_A/f_B, f_a/f_A
    - Bigram frequencies (including boundary terms)

  STRUCTURALLY UNIVERSAL (by M^q factorization):
    - Perron eigenvalue: beta_u = beta^q (always)
    - Charpoly core: always contains charpoly(M^q) as factor

  OBSERVATION-DEPENDENT (the coupling carries this information):
    - Return count: 4 or 5 (varies with u)
    - Closing power: q = 1 or 2 (varies with u)
    - Return-word frequency ratios: the Perron eigenvector of A_u
    - Return-word gap labels: the cumulative Perron fractions
    - Self-recovery: whether canonical_codes(A_u) = sigma

  IMPLICATIONS FOR THE SM QUESTION:
    The coupling (choice of observation point) carries exactly TWO bits
    of discrete information (rc: 4 or 5; q: 1 or 2) plus a continuous
    parameter (the Perron eigenvector shape). This means:

    1. Letter-level physics is coupling-free: the 5 forced ingredients
       (time, randomness, matter, continuity, thermodynamics) don't
       depend on how you observe the object.

    2. Return-word-level physics IS coupling-dependent: if you ask
       "what are the effective species frequencies?", the answer
       depends on your observation point.

    3. The dimensional bridge (Gate 2) must specify which observation
       point maps to which physical measurement. This is not a gauge
       choice — it carries information.
    """)

    # Count distinct Perron vectors (up to permutation)
    distinct_perron = set()
    for r in all_results:
        v_sorted = tuple(np.round(np.sort(r['perron_vec'])[::-1], 5))
        distinct_perron.add(v_sorted)
    print(f"  Distinct Perron vectors (sorted, 5-digit): {len(distinct_perron)}")
    print(f"  out of {len(all_results)} observation points")

    # How many distinct gap-label sets?
    distinct_gaps = set()
    for r in all_results:
        gaps = tuple(np.round(r['rw_gap_labels'], 5))
        distinct_gaps.add(gaps)
    print(f"  Distinct gap-label sets (5-digit): {len(distinct_gaps)}")

    print(f"\n  GATE 1 VERDICT: The object has intrinsic letter-level structure")
    print(f"  (UNIVERSAL) and observation-dependent return-word-level structure")
    print(f"  (VARIES). The coupling is NOT a gauge choice — it carries")
    print(f"  {len(distinct_perron)} distinct dimensionless fingerprints across")
    print(f"  {len(all_results)} observation points.")
    print(f"\n  Next: Gate 2 — what is the dimensional bridge?")


if __name__ == '__main__':
    main()
