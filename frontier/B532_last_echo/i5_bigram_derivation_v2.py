"""
B532-I5: Bigram core hierarchy — corrected return-word induction.

Uses the FULL word position mapping (σ_pos) to correctly decompose
σ(return_word) into image return words, handling boundary effects.
"""

import numpy as np
from collections import Counter
from sympy import Matrix, symbols, factor, Poly

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
SUB_LENGTHS = {c: len(SUB[c]) for c in 'abAB'}


def grow(letter, depth):
    word = letter
    for _ in range(depth):
        word = ''.join(SUB[c] for c in word)
    return word


def compute_cum_lengths(word):
    cum = [0]
    for c in word:
        cum.append(cum[-1] + SUB_LENGTHS[c])
    return cum


def return_word_induction_correct(word_k, word_k1, factor_u):
    """Correct return-word induction using position mapping.

    word_k: depth-k word (the word to extract return words from)
    word_k1: depth-(k+1) word = σ(word_k), longer
    factor_u: the factor to induce on (e.g., 'ab')
    """
    N_k = len(word_k)
    N_k1 = len(word_k1)
    fu_len = len(factor_u)

    # Find return words to factor_u in word_k
    positions_k = []
    for i in range(N_k - fu_len + 1):
        if word_k[i:i+fu_len] == factor_u:
            positions_k.append(i)

    if len(positions_k) < 3:
        return None, None, None

    # Return words in word_k
    return_words_k = []
    for k in range(len(positions_k) - 1):
        rw = word_k[positions_k[k]:positions_k[k+1]]
        return_words_k.append(rw)

    distinct_rw = sorted(set(return_words_k))
    rw_to_idx = {rw: i for i, rw in enumerate(distinct_rw)}
    n_rw = len(distinct_rw)

    # Cumulative image lengths: position i in word_k maps to cum[i] in word_k1
    cum = compute_cum_lengths(word_k)

    # Find return words to factor_u in word_k1
    positions_k1 = []
    for i in range(N_k1 - fu_len + 1):
        if word_k1[i:i+fu_len] == factor_u:
            positions_k1.append(i)

    # Build index: position in word_k1 -> return word index in word_k1
    # For each position positions_k1[j], the return word is word_k1[positions_k1[j]:positions_k1[j+1]]
    return_words_k1 = []
    for j in range(len(positions_k1) - 1):
        rw1 = word_k1[positions_k1[j]:positions_k1[j+1]]
        return_words_k1.append(rw1)

    # For each return word in word_k at position positions_k[k]:
    # Its image under σ maps to word_k1[cum[positions_k[k]]:cum[positions_k[k+1]]]
    # Find which return words of word_k1 fall within this range

    incidence = np.zeros((n_rw, n_rw), dtype=int)
    images = {}

    for k in range(len(positions_k) - 1):
        rw = return_words_k[k]
        rw_idx = rw_to_idx[rw]

        img_start = cum[positions_k[k]]
        img_end = cum[positions_k[k+1]]

        # Find return words of word_k1 that START within [img_start, img_end)
        img_rw_labels = []
        for j in range(len(positions_k1) - 1):
            if positions_k1[j] >= img_start and positions_k1[j] < img_end:
                irw = return_words_k1[j]
                if irw in rw_to_idx:
                    incidence[rw_to_idx[irw], rw_idx] += 1
                    img_rw_labels.append(rw_to_idx[irw])

        if rw not in images:
            images[rw] = img_rw_labels

    return distinct_rw, incidence, images


def main():
    x = symbols('x')

    # Generate words at two consecutive depths
    DEPTH = 7
    word_k = grow('a', DEPTH)
    word_k1 = grow('a', DEPTH + 1)
    print(f"word_k: depth={DEPTH}, length={len(word_k)}")
    print(f"word_k1: depth={DEPTH+1}, length={len(word_k1)}")

    # Verify word_k1 = σ(word_k)
    assert word_k1 == ''.join(SUB[c] for c in word_k), "word_k1 != σ(word_k)"
    print("Verified: word_k1 = σ(word_k)")

    # Allowed bigrams
    bigram_counts = Counter()
    for i in range(len(word_k) - 1):
        bigram_counts[word_k[i] + word_k[i+1]] += 1
    BIGRAMS = sorted(bigram_counts.keys())
    print(f"\nAllowed bigrams: {BIGRAMS}")

    # User's claimed core polynomials
    claims = {
        'ab': 'x^4-2x^3-5x^2-4x-1',
        'AB': 'x^4-2x^3-5x^2-4x-1',
        'bA': 'x^4-2x^3-5x^2-4x-1',
        'Aa': 'x^2-x-1',
        'Ba': 'x^2-x-1',
        'AA': 'x^3-x^2-2x-1',
        'aA': '(x-2)(x+1)',
    }

    claim_polys = {
        'x^4-2x^3-5x^2-4x-1': x**4 - 2*x**3 - 5*x**2 - 4*x - 1,
        'x^2-x-1': x**2 - x - 1,
        'x^3-x^2-2x-1': x**3 - x**2 - 2*x - 1,
        '(x-2)(x+1)': (x-2)*(x+1),
    }

    print("\n" + "=" * 70)
    print("CORRECTED return-word induction (full position mapping)")
    print("=" * 70)

    results = {}
    for bg in BIGRAMS:
        distinct_rw, incidence, images = return_word_induction_correct(word_k, word_k1, bg)
        if distinct_rw is None:
            print(f"\n  {bg}: insufficient data")
            continue

        n = len(distinct_rw)
        M_sym = Matrix(incidence.tolist())
        cp = Poly(M_sym.charpoly(x), x)
        cp_factored = factor(cp.as_expr())

        # Extract core: factor out x^k
        cp_expr = cp.as_expr()
        core = cp_expr
        zero_power = 0
        while core.subs(x, 0) == 0:
            core = Poly(core, x).quo(Poly(x, x)).as_expr()
            zero_power += 1

        # Compute eigenvalues for reference
        eigvals = np.linalg.eigvals(incidence.astype(float))
        eigvals = sorted(eigvals, key=lambda z: -abs(z))
        pf_eigenvalue = max(abs(e) for e in eigvals)

        print(f"\n  {bg}: {n} return words")
        for i, rw in enumerate(distinct_rw):
            rw_display = rw[:20] + '...' if len(rw) > 20 else rw
            print(f"    rw{i}: {rw_display} (len {len(rw)})")
        if images:
            for rw, img in images.items():
                rw_display = rw[:12] + '..' if len(rw) > 12 else rw
                print(f"    σ({rw_display}) -> [{','.join(str(i) for i in img)}]")
        print(f"    Incidence matrix:")
        for row in incidence:
            print(f"      {row}")
        print(f"    Charpoly: {cp.as_expr()}")
        print(f"    Factored: {cp_factored}")
        print(f"    Core (x^{zero_power} factored out): {core}")
        print(f"    PF eigenvalue: {pf_eigenvalue:.6f}")

        # Check against user claim
        claimed = claims.get(bg, '?')
        claimed_poly = claim_polys.get(claimed)
        if claimed_poly is not None:
            match = Poly(core, x) == Poly(claimed_poly, x)
            print(f"    Claimed core: {claimed}")
            print(f"    MATCH: {'YES ✓' if match else 'NO ✗'}")
            if not match:
                print(f"    (got {core} vs expected {claimed_poly})")
        else:
            print(f"    No claim to check")

        results[bg] = {
            'n_rw': n,
            'incidence': incidence,
            'charpoly': cp_factored,
            'core': core,
            'zero_power': zero_power,
            'pf_eigenvalue': pf_eigenvalue,
        }

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'Bigram':<8} {'#RW':<5} {'Core polynomial':<30} {'PF λ':<10} {'Claimed':<30} {'Match':<6}")
    print("-" * 95)
    for bg in BIGRAMS:
        if bg not in results:
            continue
        r = results[bg]
        claimed = claims.get(bg, '?')
        claimed_poly = claim_polys.get(claimed)
        match = ''
        if claimed_poly is not None:
            match = '✓' if Poly(r['core'], x) == Poly(claimed_poly, x) else '✗'
        print(f"  {bg:<6} {r['n_rw']:<5} {str(r['core']):<30} {r['pf_eigenvalue']:<10.4f} {claimed:<30} {match}")

    # Check: do the same core polynomials group together?
    print("\n  Core polynomial grouping:")
    groups = {}
    for bg in BIGRAMS:
        if bg not in results:
            continue
        core_str = str(results[bg]['core'])
        if core_str not in groups:
            groups[core_str] = []
        groups[core_str].append(bg)
    for core_str, bgs in sorted(groups.items(), key=lambda x: -len(x[1])):
        print(f"    {core_str}: {bgs}")


if __name__ == '__main__':
    main()
