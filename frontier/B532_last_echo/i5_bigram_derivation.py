"""
B532-I5: Bigram-level core hierarchy verification.

The handoff claims 4 distinct core polynomials from bigram derivation:
  1. x^4 - 2x^3 - 5x^2 - 4x - 1  at ab, AB, bA
  2. x^2 - x - 1                    at Aa, Ba
  3. x^3 - x^2 - 2x - 1            at AA
  4. (x-2)(x+1)                     at aA

We compute: for each of the 7 allowed bigrams u, find the return words
to u in the fixed word, compute the induced substitution, and extract
the core polynomial (charpoly of the incidence matrix's nonzero block).

Two methods:
 A) Return-word induction in the LETTER sequence (B530 method)
 B) Return-word induction in the BIGRAM sequence (the "bigram derivation")
"""

import numpy as np
from collections import Counter, defaultdict
from sympy import Matrix, symbols, factor, Poly, eye

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}

def grow(letter, depth):
    word = letter
    for _ in range(depth):
        word = ''.join(SUB[c] for c in word)
    return word

def apply_sub(word):
    return ''.join(SUB[c] for c in word)


def return_word_induction_letter(word, factor_u):
    """Method A: return-word induction in the letter sequence."""
    # Find all occurrences of factor_u in word
    positions = []
    for i in range(len(word) - len(factor_u) + 1):
        if word[i:i+len(factor_u)] == factor_u:
            positions.append(i)

    if len(positions) < 3:
        return None, None, None

    # Extract return words: from position i to position j (next occurrence)
    # Return word = word[i:j+len(factor_u)] (includes both copies of factor_u)
    # NO: standard definition = word[i:j] (starts at u, ends BEFORE next u)
    return_words = []
    for k in range(len(positions) - 1):
        rw = word[positions[k]:positions[k+1]]
        return_words.append(rw)

    # Distinct return words
    distinct_rw = sorted(set(return_words))
    rw_to_idx = {rw: i for i, rw in enumerate(distinct_rw)}
    n_rw = len(distinct_rw)

    # Compute the induced substitution: apply sigma to each return word,
    # then parse the result as a concatenation of return words
    incidence = np.zeros((n_rw, n_rw), dtype=int)
    induced_images = {}

    for rw in distinct_rw:
        image = apply_sub(rw)
        # Parse image as concatenation of return words to factor_u
        # Find occurrences of factor_u in image
        img_positions = []
        for i in range(len(image) - len(factor_u) + 1):
            if image[i:i+len(factor_u)] == factor_u:
                img_positions.append(i)

        if len(img_positions) < 1:
            return None, None, None

        # The image must start at the first occurrence of factor_u
        # and the return words are between consecutive occurrences
        img_rws = []
        for k in range(len(img_positions) - 1):
            irw = image[img_positions[k]:img_positions[k+1]]
            img_rws.append(irw)
        # Last piece (from last occurrence to end): this is a prefix of a return word
        # In the standard framework, we handle this by noting that sigma(r_i)
        # decomposes exactly into return words when ω is the fixed point

        induced_images[rw] = img_rws

        # Count incidence
        rw_idx = rw_to_idx[rw]
        for irw in img_rws:
            if irw in rw_to_idx:
                incidence[rw_to_idx[irw], rw_idx] += 1
            else:
                # This return word doesn't appear in the original word's return words
                # This can happen at boundaries
                pass

    return distinct_rw, incidence, induced_images


def return_word_induction_bigram(word, target_bigram):
    """Method B: return-word induction in the BIGRAM sequence.

    Convert word to bigram sequence. Find return words (sequences of bigrams)
    to the target bigram. Compute the induced substitution using the bigram-level
    substitution.
    """
    # Build bigram sequence
    bigrams = [word[i]+word[i+1] for i in range(len(word)-1)]

    # Find positions of target_bigram in the bigram sequence
    positions = [i for i, bg in enumerate(bigrams) if bg == target_bigram]

    if len(positions) < 3:
        return None, None

    # Return words in bigram sequence: from position i to position j-1
    # (start at target, go until just before next target)
    return_words_bg = []
    for k in range(len(positions) - 1):
        rw = tuple(bigrams[positions[k]:positions[k+1]])
        return_words_bg.append(rw)

    distinct_rw = sorted(set(return_words_bg))
    rw_to_idx = {rw: i for i, rw in enumerate(distinct_rw)}
    n_rw = len(distinct_rw)

    # To compute the induced substitution, we need to know what happens
    # to each return word under sigma.
    # sigma acts on the LETTER word. When applied to the letter word,
    # each letter x at position i becomes sigma(x) at the corresponding position
    # in the image. The bigram sequence of the image word is different.

    # Instead: apply sigma to the original word, compute new bigram sequence,
    # find positions of target_bigram, extract new return words, and
    # express them as concatenations of old return words.

    image_word = apply_sub(word)
    image_bigrams = [image_word[i]+image_word[i+1] for i in range(len(image_word)-1)]

    image_positions = [i for i, bg in enumerate(image_bigrams) if bg == target_bigram]

    image_return_words = []
    for k in range(len(image_positions) - 1):
        rw = tuple(image_bigrams[image_positions[k]:image_positions[k+1]])
        image_return_words.append(rw)

    # Now: each original return word at position k in the original sequence
    # maps to some number of return words in the image sequence.
    # Build the incidence matrix by matching original positions to image positions.

    # Map from original return word index to image return words
    # We need the correspondence: original position k -> image position range

    # Original letter positions for each original return word:
    # Original rw at positions[k]:positions[k+1] in bigram seq
    # corresponds to letter positions positions[k]:positions[k+1]+1 in word

    # After applying sigma, letter position i maps to a range in the image word.
    # We need the position map.

    # Cumulative lengths of sigma(letter)
    cum_lengths = [0]
    for c in word:
        cum_lengths.append(cum_lengths[-1] + len(SUB[c]))

    # For each original return word (positions[k] to positions[k+1]-1 in bigram seq,
    # = letter positions positions[k] to positions[k+1] in word):
    # Its image in the image word starts at cum_lengths[positions[k]] and goes to
    # cum_lengths[positions[k+1]+1]-1 in the image word.
    # But we need to find how many target bigrams fall within this range in the
    # image bigram sequence.

    # Actually, let's simplify. The key relationship is:
    # The sequence of return words in the original = r_{i_1}, r_{i_2}, ...
    # Under sigma, this becomes r'_{j_1}, r'_{j_2}, ...
    # And sigma(r_{i_k}) = r'_{j_k} r'_{j_{k+1}} ... r'_{j_{k+m}} (a sequence of image return words)

    # To build the incidence matrix, we can just:
    # 1. Record the sequence of original return-word labels: seq_orig
    # 2. Record the sequence of image return-word labels: seq_image
    # 3. Find the parsing: each original rw maps to how many image rws

    # The parsing is determined by: original rw k covers letter positions [positions[k], positions[k+1]]
    # In the image, these letters map to image positions [cum_lengths[positions[k]], cum_lengths[positions[k+1]+1]-1]
    # But we need bigram positions, which are letter_pos to letter_pos+1.

    # Let me use a different approach. The image word = sigma(word).
    # The original bigram at position i in the original word corresponds to
    # letters word[i], word[i+1] at positions i, i+1.
    # In the image word, position i expands to cum_lengths[i]:cum_lengths[i+1].
    # The bigram at original position i (letters i,i+1) maps to:
    # image letters cum_lengths[i] to cum_lengths[i+1+1]-1 = cum_lengths[i+2]-1
    # But the bigrams in this range are those in the image word starting at positions
    # cum_lengths[i] through cum_lengths[i+2]-2.

    # This is getting complicated. Let me use a direct approach:
    # For each original return word, extract the corresponding letter subword,
    # apply sigma, and count target bigrams in the result.

    incidence = np.zeros((n_rw, n_rw), dtype=int)

    for k in range(len(positions) - 1):
        orig_rw = return_words_bg[k]
        orig_rw_idx = rw_to_idx[orig_rw]

        # Letter range for this return word
        letter_start = positions[k]
        letter_end = positions[k+1] + 1  # +1 because bigram at pos j involves letters j, j+1

        # Apply sigma to these letters
        subword = word[letter_start:letter_end]
        image_subword = apply_sub(subword)

        # Find target bigrams in image_subword
        img_bg_positions = []
        for j in range(len(image_subword) - 1):
            if image_subword[j] + image_subword[j+1] == target_bigram:
                img_bg_positions.append(j)

        # The return words in the image subword
        for m in range(len(img_bg_positions) - 1):
            irw = tuple(image_subword[j]+image_subword[j+1]
                       for j in range(img_bg_positions[m], img_bg_positions[m+1]))
            if irw in rw_to_idx:
                incidence[rw_to_idx[irw], orig_rw_idx] += 1

    return distinct_rw, incidence


def main():
    DEPTH = 7
    word = grow('a', DEPTH)
    N = len(word)
    print(f"Fixed word: depth={DEPTH}, length={N}")

    # The 7 allowed bigrams
    bigram_counts = Counter()
    for i in range(N - 1):
        bigram_counts[word[i] + word[i+1]] += 1

    BIGRAMS = sorted(bigram_counts.keys())
    print(f"\nAllowed bigrams ({len(BIGRAMS)}): {BIGRAMS}")
    for bg in BIGRAMS:
        print(f"  {bg}: {bigram_counts[bg]} ({bigram_counts[bg]/(N-1)*100:.1f}%)")

    x = symbols('x')

    # ================================================================
    # METHOD A: Return-word induction in letter sequence
    # ================================================================
    print("\n" + "=" * 70)
    print("METHOD A: Return-word induction in LETTER sequence (B530 method)")
    print("=" * 70)

    for bg in BIGRAMS:
        distinct_rw, incidence, images = return_word_induction_letter(word, bg)
        if distinct_rw is None:
            print(f"\n  {bg}: insufficient data")
            continue

        n = len(distinct_rw)
        M_sym = Matrix(incidence.tolist())
        cp = Poly(M_sym.charpoly(x), x)
        cp_factored = factor(cp.as_expr())

        print(f"\n  {bg}: {n} return words, matrix {n}x{n}")
        print(f"    Return words: {[rw[:15]+'...' if len(rw)>15 else rw for rw in distinct_rw]}")
        print(f"    Incidence matrix:\n{incidence}")
        print(f"    Charpoly: {cp.as_expr()}")
        print(f"    Factored: {cp_factored}")

    # ================================================================
    # METHOD B: Return-word induction in bigram sequence
    # ================================================================
    print("\n" + "=" * 70)
    print("METHOD B: Return-word induction in BIGRAM sequence")
    print("=" * 70)

    for bg in BIGRAMS:
        distinct_rw, incidence = return_word_induction_bigram(word, bg)
        if distinct_rw is None:
            print(f"\n  {bg}: insufficient data")
            continue

        n = len(distinct_rw)
        M_sym = Matrix(incidence.tolist())
        cp = Poly(M_sym.charpoly(x), x)
        cp_factored = factor(cp.as_expr())

        print(f"\n  {bg}: {n} return words (bigram-level), matrix {n}x{n}")
        for i, rw in enumerate(distinct_rw):
            print(f"    rw{i}: {'.'.join(rw[:5])}{'...' if len(rw)>5 else ''} (len {len(rw)})")
        print(f"    Incidence matrix:\n{incidence}")
        print(f"    Charpoly: {cp.as_expr()}")
        print(f"    Factored: {cp_factored}")

    # ================================================================
    # METHOD C: Bigram derivation via DIRECT substitution on bigram alphabet
    # ================================================================
    print("\n" + "=" * 70)
    print("METHOD C: Derived substitution matrices restricted by bigram")
    print("=" * 70)

    # The bigram morphism: for each bigram xy, its image under sigma is
    # the sequence of bigrams in sigma(x).first(sigma(y))
    def bigram_image(bg):
        x, y = bg[0], bg[1]
        w = SUB[x] + SUB[y][0]
        return tuple(w[i]+w[i+1] for i in range(len(w)-1))

    # Build the 7x7 incidence matrix
    bg_idx = {bg: i for i, bg in enumerate(BIGRAMS)}
    M7 = np.zeros((7, 7), dtype=int)
    for bg in BIGRAMS:
        img = bigram_image(bg)
        for ibg in img:
            M7[bg_idx[ibg], bg_idx[bg]] += 1

    print("Full 7x7 bigram incidence matrix:")
    print(f"  Order: {BIGRAMS}")
    print(M7)

    M7_sym = Matrix(M7.tolist())
    cp7 = Poly(M7_sym.charpoly(x), x)
    print(f"Charpoly: {cp7.as_expr()}")
    print(f"Factored: {factor(cp7.as_expr())}")

    # For each bigram, extract the "orbit closure" submatrix
    # The orbits under the bigram substitution:
    print("\nBigram orbits under the bigram morphism:")
    for bg in BIGRAMS:
        orbit = set()
        frontier = {bg}
        while frontier:
            new = set()
            for b in frontier:
                if b not in orbit:
                    orbit.add(b)
                    img = bigram_image(b)
                    for ibg in img:
                        if ibg not in orbit:
                            new.add(ibg)
            frontier = new
        print(f"  {bg}: orbit = {sorted(orbit)} (size {len(orbit)})")

    # ================================================================
    # METHOD D: Per-bigram "restriction" — keep only bigrams reachable
    # from this one in the images, project out duplicates
    # ================================================================
    print("\n" + "=" * 70)
    print("METHOD D: Column-space reduction per bigram equivalence class")
    print("=" * 70)

    # The rows ab=aA (identical images); Aa=AA=AB (identical images)
    # Representatives: ab, bA, Aa, Ba
    # Reduced 4x4 system on representatives:
    reps = ['ab', 'bA', 'Aa', 'Ba']
    rep_idx = {r: i for i, r in enumerate(reps)}

    # Collapse rule: ab→ab, aA→ab, bA→bA, Aa→Aa, AA→Aa, AB→Aa, Ba→Ba
    collapse = {'ab': 'ab', 'aA': 'ab', 'bA': 'bA', 'Aa': 'Aa', 'AA': 'Aa', 'AB': 'Aa', 'Ba': 'Ba'}

    M4 = np.zeros((4, 4), dtype=int)
    for bg in BIGRAMS:
        img = bigram_image(bg)
        col = rep_idx[collapse[bg]]
        for ibg in img:
            row = rep_idx[collapse[ibg]]
            M4[row, col] += 1

    # But we need to be careful: bigrams that collapse should have their
    # contributions summed, not just one representative taken.
    # Actually, since ab and aA have IDENTICAL images, their columns in the
    # collapsed matrix are the same. And since Aa=AA=AB have identical images,
    # their columns are also the same.

    # So the collapsed matrix just uses one column per equivalence class.
    # But we need to check: is this collapse well-defined?

    print("Representatives: ab, bA, Aa, Ba")
    print(f"Collapse: {collapse}")

    # Recompute: for each representative, its image in terms of representatives
    for rep in reps:
        img = bigram_image(rep)
        collapsed_img = [collapse[ibg] for ibg in img]
        print(f"  {rep} -> {'.'.join(collapsed_img)}")

    M4_sym = Matrix(M4.tolist())
    cp4 = Poly(M4_sym.charpoly(x), x)
    print(f"\n4x4 collapsed matrix:")
    print(M4)
    print(f"Charpoly: {cp4.as_expr()}")
    print(f"Factored: {factor(cp4.as_expr())}")

    # ================================================================
    # TARGET CHECK: what matrices have the user's claimed charpolys?
    # ================================================================
    print("\n" + "=" * 70)
    print("TARGET: user's claimed core polynomials")
    print("=" * 70)

    targets = {
        'ab,AB,bA': 'x^4-2x^3-5x^2-4x-1',
        'Aa,Ba': 'x^2-x-1',
        'AA': 'x^3-x^2-2x-1',
        'aA': '(x-2)(x+1)'
    }
    for bgs, poly_str in targets.items():
        print(f"  {bgs}: {poly_str}")

    # Check: the product of all claimed polys
    p1 = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    p2 = x**2 - x - 1
    p3 = x**3 - x**2 - 2*x - 1
    p4 = (x-2)*(x+1)
    product = p1 * p2 * p3 * p4
    print(f"\nProduct degree: {Poly(product, x).degree()} (sum 4+2+3+2 = 11)")
    print(f"If these are charpolys of independent matrices, total dimension = 11")
    print(f"But we have 7 bigrams (7x7 matrix) or 4 equivalence classes (4x4 matrix)")
    print(f"=> these can't all be independent sub-blocks of one matrix")

    # Maybe each bigram gets its OWN characteristic polynomial from its
    # own return-word system. Let me check the eigenvalues:
    print(f"\nEigenvalue check:")
    for name, p in [('quartic (ab,AB,bA)', p1), ('fibonacci (Aa,Ba)', p2),
                     ('cubic (AA)', p3), ('periodic (aA)', p4)]:
        roots = np.roots([float(c) for c in Poly(p, x).all_coeffs()])
        roots = sorted(roots, key=lambda z: -abs(z))
        print(f"  {name}: PF eigenvalue = {max(abs(r) for r in roots):.6f}")


if __name__ == '__main__':
    main()
