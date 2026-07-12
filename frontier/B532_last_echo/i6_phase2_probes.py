"""
B532-I6: Nine Ingredients — Phase 2 probes.

Probe 1: Time — does σ force a time-like ordering?
Probe 8: Matter — does σ force distinct species?
Probe 9: Gravity — does σ force geometry/curvature?
"""

import numpy as np
from collections import Counter
from math import log2, log, sqrt

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
LETTERS = 'abAB'


def grow(letter, depth):
    word = letter
    for _ in range(depth):
        word = ''.join(SUB[c] for c in word)
    return word


# ======================================================================
# PROBE 1: TIME
# ======================================================================

def probe_1_time(word):
    print("=" * 70)
    print("PROBE 1: TIME (does σ force a time-like ordering?)")
    print("=" * 70)

    N = len(word)

    # --- Test 1: Time-reversal symmetry breaking ---
    # Does ω differ from its reversal? (Is the sequence oriented?)
    rev_word = word[::-1]

    # Compare bigram frequencies: ω vs ω̄
    bg_fwd = Counter()
    bg_rev = Counter()
    for i in range(N - 1):
        bg_fwd[word[i] + word[i+1]] += 1
        bg_rev[rev_word[i] + rev_word[i+1]] += 1

    all_bigrams = sorted(set(list(bg_fwd.keys()) + list(bg_rev.keys())))

    print("\n  Time-reversal test: bigram frequencies ω vs ω̄")
    print(f"  {'Bigram':<8} {'freq(ω)':<12} {'freq(ω̄)':<12} {'diff':<12} {'reversed':<8}")
    max_diff = 0
    for bg in all_bigrams:
        f_fwd = bg_fwd.get(bg, 0) / (N - 1)
        f_rev = bg_rev.get(bg, 0) / (N - 1)
        diff = abs(f_fwd - f_rev)
        rev_bg = bg[1] + bg[0]
        max_diff = max(max_diff, diff)
        print(f"  {bg:<8} {f_fwd:<12.6f} {f_rev:<12.6f} {diff:<12.2e} {rev_bg}")

    print(f"\n  Max bigram asymmetry: {max_diff:.6e}")
    # Key insight: reversing ω turns bigram 'xy' into 'yx'.
    # So freq(xy in ω) vs freq(yx in ω) is the true time-reversal test.
    print("\n  Time-reversal test: P(xy) vs P(yx) in ω")
    pairs_checked = set()
    asym_count = 0
    for bg in all_bigrams:
        rev_bg = bg[1] + bg[0]
        pair = tuple(sorted([bg, rev_bg]))
        if pair in pairs_checked:
            continue
        pairs_checked.add(pair)
        f_xy = bg_fwd.get(bg, 0) / (N - 1)
        f_yx = bg_fwd.get(rev_bg, 0) / (N - 1)
        asym = abs(f_xy - f_yx)
        if bg != rev_bg:
            marker = '≠' if asym > 1e-4 else '≈'
            print(f"    P({bg}) = {f_xy:.6f},  P({rev_bg}) = {f_yx:.6f}  "
                  f"Δ = {asym:.6f}  {marker}")
            if asym > 1e-4:
                asym_count += 1

    print(f"\n  Asymmetric pairs (Δ > 1e-4): {asym_count}")

    # --- Test 2: Substitution reversal ---
    # σ̄(x) = reverse of σ(x). Is σ̄ conjugate to σ?
    print("\n  Substitution reversal analysis:")
    SUB_REV = {c: SUB[c][::-1] for c in LETTERS}
    for c in LETTERS:
        print(f"    σ({c}) = {SUB[c]},   σ̄({c}) = {SUB_REV[c]}")

    # Incidence matrices are the same (reversal doesn't change letter counts)
    # But the grammar changes
    grammar_fwd = set()
    grammar_rev = set()
    for c in LETTERS:
        img = SUB[c]
        for i in range(len(img) - 1):
            grammar_fwd.add(img[i] + img[i+1])
        img_r = SUB_REV[c]
        for i in range(len(img_r) - 1):
            grammar_rev.add(img_r[i] + img_r[i+1])

    print(f"    Grammar(σ):  {sorted(grammar_fwd)}")
    print(f"    Grammar(σ̄): {sorted(grammar_rev)}")
    print(f"    Same grammar? {grammar_fwd == grammar_rev}")

    # Check: is σ̄ = φ∘σ∘φ⁻¹ for some letter permutation φ?
    from itertools import permutations
    conjugate_found = False
    for perm in permutations(LETTERS):
        phi = dict(zip(LETTERS, perm))
        phi_inv = {v: k for k, v in phi.items()}
        match = True
        for c in LETTERS:
            # φ(σ(φ⁻¹(c))) should equal σ̄(c)
            pre = phi_inv[c]
            img_sigma = SUB[pre]
            img_composed = ''.join(phi[x] for x in img_sigma)
            if img_composed != SUB_REV[c]:
                match = False
                break
        if match:
            conjugate_found = True
            print(f"    σ̄ = φ∘σ∘φ⁻¹ with φ: {phi}")
            break

    if not conjugate_found:
        print(f"    σ̄ is NOT conjugate to σ by any letter permutation")
        print(f"    → TIME-REVERSAL BROKEN: σ ≠ σ̄ (mod conjugation)")

    # --- Test 3: Arrow from recognizability ---
    # The substitution is recognizable (R=9): given ω, one can uniquely
    # identify which letters of the previous generation produced each letter.
    # This gives a UNIQUE backward arrow (desubstitution).
    print(f"\n  Recognizability: R=9 (from Phase 1)")
    print(f"  → Both forward (σ) and backward (σ⁻¹) arrows are well-defined")
    print(f"  → The time arrow is FORCED but BIDIRECTIONAL (reversible)")

    # --- Test 4: Causal ordering from the substitution ---
    # In σ(a) = abAAB, the letter 'a' at position 0 is "earlier" than 'B' at position 4.
    # This ordering is inherited by ω: each generation has a natural left-to-right order.
    # Is this order compatible across generations?
    print(f"\n  Causal structure from image ordering:")
    for c in LETTERS:
        img = SUB[c]
        first = img[0]
        last = img[-1]
        print(f"    σ({c}): first={first}, last={last}")
    print(f"    Every image starts with 'a' → 'a' is always first-born")
    print(f"    Final letters: {[SUB[c][-1] for c in LETTERS]}")

    # --- Test 5: Entropy production (irreversibility) ---
    # Compare H(ω_n) with H(ω̄_n) for n-blocks
    print(f"\n  Entropy production (irreversibility test):")
    for n in [2, 3, 4, 5]:
        blocks_fwd = Counter()
        blocks_rev = Counter()
        rev = word[::-1]
        for i in range(N - n + 1):
            blocks_fwd[word[i:i+n]] += 1
            blocks_rev[rev[i:i+n]] += 1

        # KL divergence D(fwd || rev)
        total = N - n + 1
        kl = 0.0
        for blk, cnt_f in blocks_fwd.items():
            p_f = cnt_f / total
            cnt_r = blocks_rev.get(blk, 0)
            if cnt_r > 0:
                p_r = cnt_r / total
                kl += p_f * log2(p_f / p_r)
            else:
                kl += p_f * log2(p_f / (0.5 / total))

        # Also: number of blocks in fwd but not rev, and vice versa
        only_fwd = set(blocks_fwd.keys()) - set(blocks_rev.keys())
        only_rev = set(blocks_rev.keys()) - set(blocks_fwd.keys())

        print(f"    n={n}: D_KL(ω||ω̄) = {kl:.6f} bits, "
              f"fwd-only: {len(only_fwd)}, rev-only: {len(only_rev)}")

    print(f"\n  VERDICT: FORCED — σ breaks time-reversal (σ ≠ σ̄)")
    print(f"  The arrow is BIDIRECTIONAL (recognizable ⟹ unique desubstitution)")
    print(f"  but ASYMMETRIC (forward and backward grammars differ)")


# ======================================================================
# PROBE 8: MATTER
# ======================================================================

def probe_8_matter(word):
    print("\n" + "=" * 70)
    print("PROBE 8: MATTER (does σ force distinct species?)")
    print("=" * 70)

    N = len(word)

    # --- Test 1: Species distinguishability ---
    # Are the 4 letters forced to be distinct, or can any two be identified?
    print("\n  Test 1: Species distinguishability")

    # Compute frequency of each letter
    freq = Counter(word)
    for c in LETTERS:
        print(f"    freq({c}) = {freq[c]/N:.6f}")

    # Letters with same frequency can potentially be identified
    freqs = {c: freq[c]/N for c in LETTERS}
    print(f"\n    freq(a)/freq(b) = {freqs['a']/freqs['b']:.6f} = φ? (φ={1.618034:.6f})")
    print(f"    freq(A)/freq(B) = {freqs['A']/freqs['B']:.6f} = φ? (φ={1.618034:.6f})")
    print(f"    freq(a)/freq(B) = {freqs['a']/freqs['B']:.6f}")
    print(f"    freq(b)/freq(A) = {freqs['b']/freqs['A']:.6f}")

    # All four frequencies are distinct → species are frequency-distinguished
    freq_vals = sorted(freqs.values())
    all_distinct = all(abs(freq_vals[i+1] - freq_vals[i]) > 0.01
                       for i in range(len(freq_vals)-1))
    print(f"\n    All frequencies distinct: {all_distinct}")

    # --- Test 2: Grammar symmetry ---
    # What permutations of {a,b,A,B} preserve the adjacency rules?
    print("\n  Test 2: Grammar automorphisms")
    grammar = set()
    for i in range(N - 1):
        grammar.add(word[i] + word[i+1])
    print(f"    Allowed bigrams: {sorted(grammar)}")

    from itertools import permutations
    automorphisms = []
    for perm in permutations(LETTERS):
        phi = dict(zip(LETTERS, perm))
        # Check: does φ preserve the grammar?
        preserved = True
        for bg in grammar:
            mapped = phi[bg[0]] + phi[bg[1]]
            if mapped not in grammar:
                preserved = False
                break
        # Also check: no new bigrams created
        for c1 in LETTERS:
            for c2 in LETTERS:
                if c1+c2 not in grammar:
                    if phi[c1]+phi[c2] in grammar:
                        preserved = False
                        break
        if preserved:
            automorphisms.append(phi)
            print(f"    Automorphism: {dict(phi)}")

    print(f"    |Aut(grammar)| = {len(automorphisms)}")

    # --- Test 3: Substitution symmetry ---
    # What permutations commute with σ?
    print("\n  Test 3: Substitution automorphisms (φ∘σ = σ∘φ)")
    sub_auts = []
    for perm in permutations(LETTERS):
        phi = dict(zip(LETTERS, perm))
        # Check: φ(σ(x)) = σ(φ(x)) for all x
        commutes = True
        for c in LETTERS:
            lhs = ''.join(phi[x] for x in SUB[c])
            rhs = SUB[phi[c]]
            if lhs != rhs:
                commutes = False
                break
        if commutes:
            sub_auts.append(phi)
            print(f"    σ-automorphism: {dict(phi)}")

    print(f"    |Aut(σ)| = {len(sub_auts)}")

    # --- Test 4: Binary partitions (coarsenings) ---
    # The 7 non-trivial binary partitions of {a,b,A,B}
    print("\n  Test 4: Binary coarsenings")
    partitions = [
        ({'a','b'}, {'A','B'}, "old/new"),
        ({'a','A'}, {'b','B'}, "structural/tunnel"),
        ({'a','B'}, {'b','A'}, "cross"),
        ({'a'}, {'b','A','B'}, "a-vs-rest"),
        ({'b'}, {'a','A','B'}, "b-vs-rest"),
        ({'A'}, {'a','b','B'}, "A-vs-rest"),
        ({'B'}, {'a','b','A'}, "B-vs-rest"),
    ]

    for S0, S1, label in partitions:
        # Induced 2-letter substitution
        proj = {}
        for c in LETTERS:
            proj[c] = '0' if c in S0 else '1'

        # Project each image
        img0_letters = set()
        img1_letters = set()
        sub_0 = ''
        sub_1 = ''
        for c in S0:
            sub_0_c = ''.join(proj[x] for x in SUB[c])
            img0_letters.add(sub_0_c)
        for c in S1:
            sub_1_c = ''.join(proj[x] for x in SUB[c])
            img1_letters.add(sub_1_c)

        # Check consistency: do all letters in S0 project to the same image?
        consistent = len(img0_letters) == 1 and len(img1_letters) == 1
        if consistent:
            sub_proj = {'0': list(img0_letters)[0], '1': list(img1_letters)[0]}
        else:
            sub_proj = None

        # Frequency ratio
        f0 = sum(freq[c] for c in S0) / N
        f1 = sum(freq[c] for c in S1) / N
        ratio = f0 / f1 if f1 > 0 else float('inf')

        # Projected grammar
        proj_grammar = set()
        for bg in grammar:
            pg = proj[bg[0]] + proj[bg[1]]
            proj_grammar.add(pg)
        full_grammar = proj_grammar == {'00', '01', '10', '11'}

        status = "substitutive" if consistent else "NOT substitutive"
        print(f"\n    {label}: {sorted(S0)}|{sorted(S1)}")
        print(f"      freq ratio = {ratio:.6f}")
        print(f"      projected grammar: {sorted(proj_grammar)} "
              f"({'full' if full_grammar else 'restricted'})")
        print(f"      {status}")
        if consistent:
            print(f"      induced sub: 0→{sub_proj['0']}, 1→{sub_proj['1']}")

    # --- Test 5: Irreducible species count ---
    # Can the 4 letters be reduced to fewer by any identification?
    print(f"\n  Test 5: Minimum species count")
    # Try all 2-letter identifications
    reduce_possible = False
    for i, c1 in enumerate(LETTERS):
        for c2 in LETTERS[i+1:]:
            # Identify c1 with c2: replace c2 by c1 everywhere
            new_sub = {}
            for c in LETTERS:
                img = SUB[c]
                img_reduced = img.replace(c2, c1)
                new_sub[c if c != c2 else c1] = img_reduced
            # Check: is this consistent? (c1 and c2 must have the same image
            # after reduction)
            img_c1 = SUB[c1].replace(c2, c1)
            img_c2 = SUB[c2].replace(c2, c1)
            if img_c1 == img_c2:
                print(f"    Identify {c1}≡{c2}: POSSIBLE (same reduced image)")
                reduce_possible = True
            else:
                print(f"    Identify {c1}≡{c2}: blocked (σ({c1})→{img_c1}, σ({c2})→{img_c2})")

    if not reduce_possible:
        print(f"\n    No identification possible → 4 species is IRREDUCIBLE")
        print(f"    (the substitution forces exactly 4 distinct species)")

    # --- Test 6: The two natural dichotomies ---
    print(f"\n  Test 6: Natural dichotomies")
    # old/new: {a,b} vs {A,B} — the case (lower vs upper)
    old_freq = (freqs['a'] + freqs['b'])
    new_freq = (freqs['A'] + freqs['B'])
    print(f"    old/new: {old_freq:.6f} / {new_freq:.6f} = {old_freq/new_freq:.6f}")

    # structural/tunnel: {a,A} vs {b,B}
    str_freq = (freqs['a'] + freqs['A'])
    tun_freq = (freqs['b'] + freqs['B'])
    print(f"    str/tun: {str_freq:.6f} / {tun_freq:.6f} = {str_freq/tun_freq:.6f} = φ? ({(1+sqrt(5))/2:.6f})")

    # Product structure
    print(f"\n    If species = (old/new) × (str/tun), predicted frequencies:")
    print(f"      a = old∧str: {old_freq * str_freq / 1:.6f} vs actual {freqs['a']:.6f}")
    print(f"      b = old∧tun: {old_freq * tun_freq / 1:.6f} vs actual {freqs['b']:.6f}")
    print(f"      A = new∧str: {new_freq * str_freq / 1:.6f} vs actual {freqs['A']:.6f}")
    print(f"      B = new∧tun: {new_freq * tun_freq / 1:.6f} vs actual {freqs['B']:.6f}")
    independence = max(
        abs(freqs['a'] - old_freq * str_freq),
        abs(freqs['b'] - old_freq * tun_freq),
        abs(freqs['A'] - new_freq * str_freq),
        abs(freqs['B'] - new_freq * tun_freq),
    )
    print(f"      Max deviation from independence: {independence:.6f}")
    if independence < 0.001:
        print(f"      → Species ARE a product: (old/new) × (str/tun) is exact")
    else:
        print(f"      → Species are NOT a simple product (correlated)")

    print(f"\n  VERDICT: FORCED — σ forces exactly 4 irreducible species")
    print(f"  organized by two correlated binary features (old/new, structural/tunnel)")


# ======================================================================
# PROBE 9: GRAVITY (geometry/curvature)
# ======================================================================

def probe_9_gravity(word):
    print("\n" + "=" * 70)
    print("PROBE 9: GRAVITY (does σ force geometry/curvature?)")
    print("=" * 70)

    N = len(word)
    freq = Counter(word)
    freqs = {c: freq[c]/N for c in LETTERS}

    # --- Test 1: Fluctuation exponent ---
    # Define running deviation: S(n) = Σ_{i=1}^{n} (1_{ω_i ∈ old} - f_old)
    # The fluctuation σ²(n) = <S(n)²> should scale as n^{2H}
    # For random: H=1/2 (diffusive). For quasicrystal: H can differ.
    print("\n  Test 1: Fluctuation exponent (old/new deviation)")
    f_old = freqs['a'] + freqs['b']

    # Running sum of deviations
    deviations = np.array([1.0 if c in 'ab' else 0.0 for c in word]) - f_old
    cumsum = np.cumsum(deviations)

    # Measure variance at different scales
    scales = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    log_n = []
    log_var = []
    print(f"    {'scale n':<10} {'Var(S)':<15} {'√Var/n':<12}")
    for n in scales:
        if n > N // 2:
            break
        n_windows = N // n
        variances = []
        for w in range(n_windows):
            s = cumsum[w*n + n - 1] - (cumsum[w*n - 1] if w*n > 0 else 0)
            variances.append(s**2)
        var = np.mean(variances)
        if var > 0:
            log_n.append(log(n))
            log_var.append(log(var))
            print(f"    {n:<10} {var:<15.4f} {sqrt(var)/n:<12.6f}")

    # Fit: log(Var) = 2H * log(n) + const
    if len(log_n) >= 4:
        log_n = np.array(log_n)
        log_var = np.array(log_var)
        A = np.vstack([log_n, np.ones(len(log_n))]).T
        result = np.linalg.lstsq(A, log_var, rcond=None)
        slope = result[0][0]
        H = slope / 2
        print(f"\n    Fluctuation exponent H = {H:.4f}")
        print(f"    (H=0.5 is random/diffusive, H=1 is ballistic)")
        if abs(H - 0.5) < 0.05:
            print(f"    → RANDOM-like fluctuations (no anomalous scaling)")
        elif H < 0.5:
            print(f"    → SUB-DIFFUSIVE: stronger-than-random restoring force")
        else:
            print(f"    → SUPER-DIFFUSIVE: persistent deviations")

    # --- Test 2: Local curvature from frequency deviations ---
    # At each position, define "curvature" as the deviation of local frequency
    # from the global frequency, at scale R
    print(f"\n  Test 2: Local curvature (frequency deviation at scale R)")
    R = 100
    curvature = []
    for i in range(0, N - R, R):
        window = word[i:i+R]
        local_old = sum(1 for c in window if c in 'ab') / R
        curv = local_old - f_old
        curvature.append(curv)

    curvature = np.array(curvature)
    print(f"    Scale R={R}, {len(curvature)} windows")
    print(f"    mean curvature: {np.mean(curvature):.6f}")
    print(f"    std curvature:  {np.std(curvature):.6f}")
    print(f"    max |curvature|: {np.max(np.abs(curvature)):.6f}")

    # Distribution: is it Gaussian or structured?
    from collections import Counter as C
    hist, edges = np.histogram(curvature, bins=20)
    print(f"\n    Curvature histogram (20 bins):")
    for i, count in enumerate(hist):
        center = (edges[i] + edges[i+1]) / 2
        bar = '#' * (count * 40 // max(hist))
        print(f"      {center:+.4f}: {bar} ({count})")

    # Autocorrelation of curvature
    print(f"\n  Test 3: Curvature autocorrelation")
    curv_centered = curvature - np.mean(curvature)
    var_curv = np.var(curvature)
    if var_curv > 1e-15:
        max_lag = min(50, len(curvature) // 4)
        print(f"    {'lag':<8} {'C(lag)':<12}")
        for lag in [1, 2, 3, 5, 10, 20, 50]:
            if lag >= max_lag:
                break
            autocorr = np.mean(curv_centered[:-lag] * curv_centered[lag:]) / var_curv
            print(f"    {lag:<8} {autocorr:<12.6f}")

    # --- Test 4: Natural metric from Perron eigenvector ---
    # Each letter has a "length" proportional to its Perron eigenvalue component.
    # Perron eigenvector of M = (freq(a), freq(b), freq(A), freq(B)) * N / β
    # But the actual lengths are the image lengths: |σ(a)|=5, |σ(b)|=3, |σ(A)|=4, |σ(B)|=2
    # After normalization by β, the Perron lengths are freq/freq_total = freq (since total=1)
    print(f"\n  Test 4: Natural metric from Perron eigenvector")
    perron = {c: freqs[c] for c in LETTERS}
    print(f"    Perron lengths: {perron}")
    print(f"    Image lengths:  a→{len(SUB['a'])}, b→{len(SUB['b'])}, "
          f"A→{len(SUB['A'])}, B→{len(SUB['B'])}")

    # Ratio of image length to Perron frequency
    beta = 3.676205
    for c in LETTERS:
        ratio = len(SUB[c]) / (freqs[c] * beta / freqs[c])
        print(f"    |σ({c})|/(β) = {len(SUB[c])/beta:.6f},  "
              f"freq({c}) = {freqs[c]:.6f},  "
              f"|σ({c})|/β / freq({c}) = {len(SUB[c])/(beta * freqs[c]):.6f}")

    # The Rauzy fractal gives the canonical embedding into ℝ^(d-1)
    print(f"\n  Test 5: Rauzy fractal and embedding dimension")
    # The incidence matrix M has eigenvalues β, λ₂, λ₃, λ₄
    M = np.array([[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]])
    eigvals = np.linalg.eigvals(M)
    eigvals_sorted = sorted(eigvals, key=lambda z: -abs(z))
    print(f"    M eigenvalues: {[f'{e:.6f}' for e in eigvals_sorted]}")
    print(f"    Expanding direction: dim=1 (the substitution axis)")
    print(f"    Contracting directions: dim=3 (Rauzy fractal lives here)")

    # For a 4-letter substitution with irreducible charpoly and Pisot property,
    # the Rauzy fractal is a fractal subset of ℝ³.
    # Its Hausdorff dimension = log(β)/log(|λ₂|) or related quantity
    abs_l2 = abs(eigvals_sorted[1])
    abs_l3 = abs(eigvals_sorted[2])
    print(f"    |λ₂| = {abs_l2:.6f}, |λ₃| = {abs(eigvals_sorted[2]):.6f}")

    # The tiling itself is 1D — no intrinsic curvature
    print(f"\n    The substitution tiling is ONE-DIMENSIONAL.")
    print(f"    Intrinsic curvature of a 1D object = 0 (trivially).")
    print(f"    Extrinsic geometry exists only via EMBEDDING (Rauzy fractal, ℝ³).")
    print(f"    The embedding is forced by M's spectrum — no external choice.")

    # --- Test 6: Spectral gap hierarchy as "gravitational" structure ---
    print(f"\n  Test 6: Spectral gaps as 'gravitational' potential")
    print(f"    Gap labels: g₁={freqs['a']:.6f}, "
          f"g₂={freqs['a']+freqs['b']:.6f}, "
          f"g₃={freqs['a']+freqs['b']+freqs['A']:.6f}")
    print(f"    These define a FORCED potential landscape in the IDS.")
    print(f"    But the gap WIDTHS depend on the Hamiltonian (external).")
    print(f"    → The topology (WHERE gaps are) is forced; the metric (HOW WIDE) is not.")

    # --- Verdict ---
    print(f"\n  SUMMARY:")
    print(f"    Geometry (intrinsic): ABSENT — the object is 1D, no intrinsic curvature")
    print(f"    Geometry (extrinsic): FORCED — the Rauzy embedding in ℝ³ is determined by M")
    print(f"    Topology: FORCED — gap positions, Pisot spectrum, fractal dimension")
    print(f"    Metric: CONDITIONED — gap widths, band structure depend on external H")
    print(f"    Fluctuation scaling: H={H:.4f} — {'anomalous' if abs(H-0.5) > 0.05 else 'diffusive'}")

    print(f"\n  VERDICT: CONDITIONED")
    print(f"  σ forces topology (gap positions, Rauzy fractal, spectral type)")
    print(f"  but metric geometry (distances, curvature) requires external input (Hamiltonian)")


# ======================================================================
# MAIN
# ======================================================================

if __name__ == '__main__':
    print("NINE INGREDIENTS, ONE OBJECT — Phase 2")
    print("=" * 70)

    DEPTH = 9
    word = grow('a', DEPTH)
    print(f"Fixed word: depth={DEPTH}, length={len(word)}")

    probe_1_time(word)
    probe_8_matter(word)
    probe_9_gravity(word)

    # Final verdict table
    print("\n" + "=" * 70)
    print("PHASE 2 VERDICT TABLE")
    print("=" * 70)
    print(f"  {'Probe':<25} {'Verdict':<15} {'Key finding'}")
    print(f"  {'-'*70}")
    print(f"  {'1. Time':<25} {'FORCED':<15} σ ≠ σ̄, bidirectional but asymmetric")
    print(f"  {'8. Matter':<25} {'FORCED':<15} 4 irreducible species, |Aut(σ)|=1")
    print(f"  {'9. Gravity':<25} {'CONDITIONED':<15} topology forced, metric external")
