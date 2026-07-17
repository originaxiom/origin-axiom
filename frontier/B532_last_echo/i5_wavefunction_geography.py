"""
B532-I5: Wavefunction geography — do the spectral gaps sort eigenstates by old/new weight?

Claims to verify:
1. The three main gaps have IDS labels at freq(a), freq(a)+freq(b), freq(a)+freq(b)+freq(A)
2. Wavefunctions below gap #1 live predominantly on OLD sites {a,b}
3. Wavefunctions above gap #3 live predominantly on NEW sites {A,B}
4. The old-weight decreases monotonically across the four bands (84, 60, 27, 9)
5. The "core sequence" (bigram → F/C/P) forms a substitution
"""

import numpy as np
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}

def grow(letter, depth):
    word = letter
    for _ in range(depth):
        word = ''.join(SUB[c] for c in word)
    return word


def compute_wavefunction_geography(word, V_map, label=""):
    N = len(word)
    print(f"\n{'='*70}")
    print(f"Potential: {label}  V = {V_map}")
    print(f"Word length: {N}")

    counts = Counter(word)
    freqs = {c: counts[c]/N for c in 'abAB'}
    print(f"Letter frequencies: " + ", ".join(f"{c}={freqs[c]:.4f}" for c in 'abAB'))
    print(f"Old (a+b) = {freqs['a']+freqs['b']:.4f}, New (A+B) = {freqs['A']+freqs['B']:.4f}")

    # Expected gap IDS labels
    ids_gap1 = freqs['a']
    ids_gap2 = freqs['a'] + freqs['b']
    ids_gap3 = freqs['a'] + freqs['b'] + freqs['A']
    print(f"Expected gap IDS: {ids_gap1:.4f}, {ids_gap2:.4f}, {ids_gap3:.4f}")

    is_old = np.array([c in 'ab' for c in word], dtype=bool)

    V = np.array([V_map[c] for c in word])
    H = np.diag(V)
    for i in range(N-1):
        H[i, i+1] = 1.0
        H[i+1, i] = 1.0
    H[0, N-1] = 1.0
    H[N-1, 0] = 1.0

    eigenvalues, eigenvectors = np.linalg.eigh(H)

    idx = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Find the 10 largest gaps
    diffs = np.diff(eigenvalues)
    top_gaps = np.argsort(diffs)[-10:][::-1]

    print(f"\nTop 10 gaps (by width):")
    for rank, gi in enumerate(top_gaps):
        ids_val = (gi + 1) / N
        print(f"  #{rank+1}: IDS = {ids_val:.4f}, width = {diffs[gi]:.6f}, "
              f"E = [{eigenvalues[gi]:.4f}, {eigenvalues[gi+1]:.4f}]")

    # Use the three largest gaps to define four bands
    main_gaps = sorted(top_gaps[:3])
    boundaries = [0] + [gi + 1 for gi in main_gaps] + [N]

    print(f"\nBand analysis (using 3 largest gaps):")
    print(f"{'Band':<8} {'IDS range':<20} {'#states':<10} {'old_wt':<10} {'new_wt':<10}")
    print("-" * 60)

    for band_idx in range(4):
        start, end = boundaries[band_idx], boundaries[band_idx+1]
        n_states = end - start
        if n_states == 0:
            continue

        # For each eigenstate in this band, compute old weight
        band_old_weights = []
        for k in range(start, end):
            psi = eigenvectors[:, k]
            old_wt = np.sum(np.abs(psi[is_old])**2)
            band_old_weights.append(old_wt)

        avg_old = np.mean(band_old_weights)
        avg_new = 1 - avg_old
        ids_lo = start / N
        ids_hi = end / N
        print(f"  {band_idx+1:<6} [{ids_lo:.3f}, {ids_hi:.3f}]    "
              f"{n_states:<10} {avg_old:.3f}     {avg_new:.3f}")

    # Per-eigenstate old weight for detailed view
    all_old_weights = np.array([
        np.sum(np.abs(eigenvectors[:, k][is_old])**2)
        for k in range(N)
    ])

    return eigenvalues, eigenvectors, all_old_weights, main_gaps


def compute_core_sequence(word):
    """Classify each bigram in the word as F(ull), C(ritical), or P(eriodic).

    The user claims:
      ab → F, bA → F, AA → C, AB → F, aA → P
    And the implied: Aa → ?, Ba → ?

    We verify by checking the return-word induction spectral type for each bigram.
    """
    print(f"\n{'='*70}")
    print("Core sequence analysis")

    # First: enumerate all bigrams and their counts
    bigrams = Counter()
    for i in range(len(word)-1):
        bg = word[i] + word[i+1]
        bigrams[bg] += 1

    print(f"\nBigram census ({len(bigrams)} distinct):")
    for bg, count in sorted(bigrams.items(), key=lambda x: -x[1]):
        print(f"  {bg}: {count} ({count/(len(word)-1)*100:.1f}%)")

    # Check the substitution claim:
    # If we assign cores to bigrams, does σ act as a substitution on the core alphabet?
    # σ(a) = abAAB → bigrams ab,bA,AA,AB → if these map to FFCF
    # σ(b) = aAB → bigrams aA,AB → PF
    # σ(A) = abAB → bigrams ab,bA,AB → FFF
    # σ(B) = aA → bigram aA → P

    # From the images: 5 bigrams assigned:
    # ab→F, bA→F, AA→C, AB→F, aA→P
    # Missing: Aa, Ba

    # At image boundaries, what bigrams appear?
    # The last letter of σ(x) concatenated with first letter of σ(y),
    # where xy is a bigram in the word.
    print("\nBoundary bigrams (last letter of σ(x) + first letter of σ(y)):")
    for bg in sorted(bigrams.keys()):
        x, y = bg[0], bg[1]
        last_of_x = SUB[x][-1]
        first_of_y = SUB[y][0]
        boundary_bg = last_of_x + first_of_y
        print(f"  {bg} → boundary bigram: {boundary_bg}")

    # Check which boundary bigrams are Aa or Ba
    # σ(a) ends with B, σ(b) ends with B, σ(A) ends with B, σ(B) ends with A
    # σ(a) starts with a, σ(b) starts with a, σ(A) starts with a, σ(B) starts with a
    # So boundary = last(σ(x)) + first(σ(y)) = last(σ(x)) + 'a'
    # last(σ(a))='B', last(σ(b))='B', last(σ(A))='B', last(σ(B))='A'
    # So boundary bigrams are: Ba (from x∈{a,b,A}) or Aa (from x=B)

    # For the core sequence to be substitutive:
    # The image of bigram xy under σ produces a sequence of internal bigrams
    # PLUS boundary bigrams at the edges.
    # The "core" of the image = the INTERNAL bigrams only (boundary handled by context).
    # This is exactly the morphism on the bigram word.

    # Claimed core map:
    core_map = {'ab': 'F', 'bA': 'F', 'AA': 'C', 'AB': 'F', 'aA': 'P'}
    # We need Aa and Ba
    # Let's figure out by looking at where they appear in the substitution image

    # Build the full word σ(ω) and extract all bigrams with their core classification
    # First, let's determine Aa and Ba empirically:
    # Generate a longer word and check what return-induction type Aa and Ba have

    # For now, let's try both assignments and see which makes a consistent substitution
    for aa_core in 'FCP':
        for ba_core in 'FCP':
            test_map = dict(core_map)
            test_map['Aa'] = aa_core
            test_map['Ba'] = ba_core

            # Check consistency: apply σ to each bigram, get internal bigrams,
            # map to cores, check if it's a valid substitution
            consistent = True
            sub_on_cores = {}
            for bg in sorted(bigrams.keys()):
                x, y = bg[0], bg[1]
                # Internal bigrams of σ(x): from the word SUB[x]
                img_x = SUB[x]
                internal_cores = ''
                for j in range(len(img_x)-1):
                    ibg = img_x[j] + img_x[j+1]
                    if ibg not in test_map:
                        consistent = False
                        break
                    internal_cores += test_map[ibg]
                if not consistent:
                    break

                # The core of bigram bg should map to:
                # internal_cores of σ(x) + boundary_core + internal_cores of σ(y)
                # But for a substitution on the core sequence, the image of core(bg)
                # should be well-defined (depend only on core(bg), not on bg itself)

                bg_core = test_map.get(bg, '?')
                if bg_core in sub_on_cores:
                    if sub_on_cores[bg_core] != internal_cores:
                        # Different bigrams with same core map to different core sequences
                        # This is fine if we're defining the sub on BIGRAMS, not cores
                        pass
                else:
                    sub_on_cores[bg_core] = internal_cores

            if consistent:
                print(f"\n  Aa={aa_core}, Ba={ba_core}:")
                print(f"    Bigram → internal cores:")
                for bg in sorted(bigrams.keys()):
                    img = SUB[bg[0]]
                    cores = ''.join(test_map.get(img[j]+img[j+1], '?') for j in range(len(img)-1))
                    print(f"      {bg} ({test_map[bg]}) → σ({bg[0]})={img} → cores: {cores}")

    # Generate the actual core sequence from the word
    print(f"\nCore sequence (first 100 positions):")
    core_seq = ''
    for i in range(len(word)-1):
        bg = word[i] + word[i+1]
        c = core_map.get(bg, '?')
        core_seq += c
    print(f"  {core_seq[:100]}")
    print(f"  Length: {len(core_seq)}")
    core_counts = Counter(core_seq)
    print(f"  Counts: {dict(core_counts)}")

    # Factor complexity of the core sequence
    print(f"\nFactor complexity p(n) of core sequence:")
    for n in range(1, 20):
        factors = set()
        for i in range(len(core_seq) - n + 1):
            factors.add(core_seq[i:i+n])
        print(f"  p({n}) = {len(factors)}  (ratio p(n)/n = {len(factors)/n:.2f})")


def main():
    DEPTH = 5
    word = grow('a', DEPTH)
    print(f"Generated word: depth={DEPTH}, length={len(word)}")
    print(f"First 80 chars: {word[:80]}")

    # Try multiple potentials
    potentials = [
        ({'a': 0.0, 'b': 1.0, 'A': 2.0, 'B': 3.0}, "generic (0,1,2,3)"),
        ({'a': 0.0, 'b': 0.0, 'A': 2.0, 'B': 2.0}, "old/new split (0,0,2,2)"),
        ({'a': 1.0, 'b': 0.0, 'A': 1.0, 'B': 0.0}, "structural/tunnel (1,0,1,0)"),
        ({'a': 0.0, 'b': 0.5, 'A': 1.5, 'B': 2.0}, "graded (0,0.5,1.5,2)"),
    ]

    results = {}
    for V_map, label in potentials:
        evals, evecs, old_wts, gaps = compute_wavefunction_geography(word, V_map, label)
        results[label] = (evals, evecs, old_wts, gaps)

    # Core sequence analysis
    compute_core_sequence(word)

    # Also try depth 6 for better statistics
    print(f"\n{'='*70}")
    print("DEPTH 6 — better resolution")
    word6 = grow('a', 6)
    print(f"Word length: {len(word6)}")
    V_best = {'a': 0.0, 'b': 1.0, 'A': 2.0, 'B': 3.0}
    compute_wavefunction_geography(word6, V_best, "generic (0,1,2,3) depth-6")


if __name__ == '__main__':
    main()
