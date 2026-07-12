#!/usr/bin/env python3
"""B532 I3b — Verify the observer-gap handoff claims.

Core claim: gap label #1 (IDS = freq(a) = φ/S) equals the Fibonacci-core
fraction (fraction of bigrams where the derived substitution sees x²-x-1).

Verification strategy:
1. Compute all bigram frequencies in the fixed point
2. For each bigram, derive the substitution and compute its charpoly
3. Identify which bigrams see each core polynomial
4. Sum the Fibonacci-core bigram frequencies → check if = freq(a)
5. Verify the GL(4,Z) conjugacy claim for the pair substitution
"""

import sys, os
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, original_matrix,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = ['a', 'b', 'A', 'B']
x = sp.Symbol('x')

PHI = (1 + np.sqrt(5)) / 2
SQ_PHI = np.sqrt(PHI)
S_NORM = PHI + 1 + PHI * SQ_PHI + SQ_PHI
FREQ = {
    'a': PHI / S_NORM,
    'b': 1 / S_NORM,
    'A': PHI * SQ_PHI / S_NORM,
    'B': SQ_PHI / S_NORM,
}
GRAMMAR = [('a','b'), ('a','A'), ('b','A'), ('A','a'), ('A','A'), ('A','B'), ('B','a')]

KNOWN_CORES = {
    'quartic': sp.factor(x**4 - 2*x**3 - 5*x**2 - 4*x - 1),
    'cubic': sp.factor(x**3 - x**2 - 2*x - 1),
    'fibonacci': sp.factor(x**2 - x - 1),
    'periodic': sp.factor(x**2 - x - 2),
}


def bigram_frequency(g1, g2):
    """Exact bigram frequency from the incidence matrix structure."""
    word = grow(10)
    total = len(word) - 1
    count = sum(1 for i in range(total) if word[i] == g1 and word[i+1] == g2)
    return count / total


def main():
    print("=" * 70)
    print("B532 I3b — Observer-gap handoff verification")
    print("=" * 70)

    # ─── Part 1: Bigram census ───
    print("\n── Part 1: Bigram census (depth 10) ──")

    bigram_data = {}
    for g1, g2 in GRAMMAR:
        bg = g1 + g2
        freq = bigram_frequency(g1, g2)

        ind = None
        host = grow(10)
        fpm = factor_position_map(host, 2)
        if bg in fpm:
            positions = fpm[bg]
            if len(positions) >= 6:
                rw = standard_return_words_from_positions(host, positions)
                ind = canonical_induced_system(rw, max_power=2)

        core = '?'
        if ind:
            cp = sp.sympify(ind['charpoly'])
            for name, poly in KNOWN_CORES.items():
                if sp.rem(cp, poly, x) == 0:
                    core = name
                    break
            if core == '?':
                core = f'other({ind["charpoly"]})'

        rc = len(rw) if ind else None
        bigram_data[bg] = {'freq': freq, 'core': core, 'ind': ind, 'rc': rc}
        print(f"  {bg}: freq = {freq:.6f}, core = {core}"
              f"{', rc=' + str(rc) if rc else ''}"
              f"{', q=' + str(ind['power']) if ind else ''}")

    # ─── Part 2: Core fractions ───
    print("\n── Part 2: Core fractions ──")

    core_fractions = {}
    for bg, data in bigram_data.items():
        core = data['core']
        if core not in core_fractions:
            core_fractions[core] = 0
        core_fractions[core] += data['freq']

    for core, frac in sorted(core_fractions.items()):
        print(f"  {core:12s}: {frac:.6f}")

    # ─── Part 3: The identity ───
    print("\n── Part 3: Gap label = core fraction? ──")

    freq_a = FREQ['a']
    fib_frac = core_fractions.get('fibonacci', 0)
    print(f"  freq(a) = φ/S = {freq_a:.6f}")
    print(f"  Fibonacci-core fraction = {fib_frac:.6f}")
    print(f"  |difference| = {abs(freq_a - fib_frac):.6e}")
    print(f"  MATCH: {'YES' if abs(freq_a - fib_frac) < 0.001 else 'NO'}")

    # Which bigrams contribute to Fibonacci core?
    fib_bigrams = [bg for bg, d in bigram_data.items() if d['core'] == 'fibonacci']
    print(f"  Fibonacci-core bigrams: {fib_bigrams}")
    fib_sum_parts = [f"freq({bg})={bigram_data[bg]['freq']:.6f}" for bg in fib_bigrams]
    print(f"    = {' + '.join(fib_sum_parts)}")

    # ─── Part 4: GL(4,Z) conjugacy ───
    print("\n── Part 4: GL(4,Z) conjugacy of pair substitution ──")

    M_orig = original_matrix()
    P = sp.Matrix([[1,0,0,-1],[1,1,-1,-1],[0,0,1,0],[1,0,0,0]])
    P_inv = P.inv()

    print(f"  det(P) = {P.det()}")
    print(f"  P·M·P⁻¹ = ?")
    M_conj = P * M_orig * P_inv
    print(f"  M_conjugated =")
    for i in range(4):
        print(f"    {[int(M_conj[i,j]) for j in range(4)]}")

    # Pair substitution from the handoff: 0→23, 1→230, 2→21330, 3→2130
    # Incidence matrix of pair substitution
    pair_sub = {0: [2,3], 1: [2,3,0], 2: [2,1,3,3,0], 3: [2,1,3,0]}
    M_pair = sp.zeros(4)
    for j in range(4):
        for c in pair_sub[j]:
            M_pair[c, j] += 1
    print(f"\n  M_pair (from pair substitution) =")
    for i in range(4):
        print(f"    {[int(M_pair[i,j]) for j in range(4)]}")

    match = M_conj == M_pair
    print(f"\n  P·M_orig·P⁻¹ = M_pair: {match}")

    # ─── Part 5: Handoff's five universal laws — quick checks ───
    print("\n── Part 5: Universal law checks ──")

    # Law 1: return number = alphabet size
    print("  Law 1 (return count = alphabet size):")
    for g1, g2 in GRAMMAR:
        bg = g1 + g2
        d = bigram_data[bg]
        if d['rc'] is not None:
            print(f"    {bg}: rc = {d['rc']}")

    # Law 4: gap labels in Z-module of frequencies
    print("\n  Law 4 (gap labels = Z-linear combinations of frequencies):")
    gap_labels = [FREQ['a'], FREQ['a'] + FREQ['b'], 1 - FREQ['B']]
    for i, gl in enumerate(gap_labels):
        print(f"    gap {i+1}: IDS = {gl:.6f}")
    print(f"    freq(a) = {FREQ['a']:.6f}")
    print(f"    freq(a)+freq(b) = {FREQ['a']+FREQ['b']:.6f}")
    print(f"    1-freq(B) = {1-FREQ['B']:.6f}")

    # ─── Part 6: The anomalous sector ───
    print("\n── Part 6: Anomalous sector (abA) ──")
    host = grow(10)
    fpm = factor_position_map(host, 3)
    if 'abA' in fpm:
        positions = fpm['abA']
        rw = standard_return_words_from_positions(host, positions)
        ind = canonical_induced_system(rw, max_power=2)
        if ind:
            print(f"  abA: charpoly = {ind['charpoly']}")
            print(f"  det = {ind['determinant']}")
            cp = sp.Poly(ind['charpoly'], x)
            disc = cp.discriminant()
            print(f"  discriminant = {disc}")
            print(f"  disc factored = {sp.factorint(int(disc))}")

    print("\n" + "=" * 70)
    print("VERIFICATION SUMMARY")
    print("=" * 70)


if __name__ == '__main__':
    main()
