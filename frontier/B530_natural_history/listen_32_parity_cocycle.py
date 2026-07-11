"""
Movement XXX (continued) — the parity cocycle.

Listen_31 found: image-start parity = case-parity of the prefix, EXACTLY.
Lowercase (a,b) flip parity (odd images 5,3); uppercase (A,B) preserve (even images 4,2).

This defines a ℤ/2 cocycle on the substitution. Follow it:
  (a) Derive the augmented substitution on 8 letters {c₀, c₁ : c ∈ {a,b,A,B}}
      where the subscript is the parity state.
  (b) Compute ITS growth matrix and char poly — what does the ℤ/2 see?
  (c) Project the fixed point: even-indexed positions are exactly the
      parity-0 sublattice of the augmented substitution.
  (d) Check if the BbB resonance (lag-2 = straddling σ-image seams) is
      explained by this ℤ/2 structure.
  (e) Where does 19 come from?  (new prime at period 6)
"""
import numpy as np
import sympy as sp
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = 'abAB'
M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


def is_lower(c):
    return c in 'ab'


# =====================================================================
# (a) The augmented substitution
# =====================================================================

def augmented_substitution():
    """
    Augment each letter c with a parity bit p ∈ {0,1}.
    State (c, p): after emitting letter c, the case-parity becomes p' = p ⊕ is_lower(c).
    Under σ, the letter c maps to its image σ(c). The parity at each position
    within the image is determined by the running case-parity.

    The augmented substitution τ maps (c, p) → the sequence of (letter, parity)
    pairs produced by σ(c) starting from parity state p.
    """
    print("=" * 60)
    print("(a) The augmented substitution")
    print("=" * 60)

    # Augmented alphabet: index = letter_index * 2 + parity
    # 0: a₀, 1: a₁, 2: b₀, 3: b₁, 4: A₀, 5: A₁, 6: B₀, 7: B₁
    aug_alpha = []
    for c in ALPHA:
        for p in range(2):
            aug_alpha.append(f"{c}{p}")

    aug_sub = {}
    for c in ALPHA:
        img = SUB[c]
        for p_start in range(2):
            p = p_start
            result = []
            for letter in img:
                result.append(f"{letter}{p}")
                if is_lower(letter):
                    p = 1 - p
            key = f"{c}{p_start}"
            aug_sub[key] = ''.join(result)

    print("\nAugmented substitution τ:")
    for key in aug_alpha:
        print(f"  τ({key}) = {aug_sub[key]}")

    # Incidence matrix (8×8)
    n = 8
    M_aug = sp.zeros(n, n)
    for j, key in enumerate(aug_alpha):
        img = aug_sub[key]
        # Parse the image: pairs of (letter, digit)
        for k in range(0, len(img), 2):
            letter = img[k]
            parity = int(img[k+1])
            idx = ALPHA.index(letter) * 2 + parity
            M_aug[idx, j] += 1

    print(f"\nIncidence matrix of τ (8×8):")
    print(M_aug)

    # Char poly
    x = sp.Symbol('x')
    cp = M_aug.charpoly(x)
    print(f"\nChar poly: {cp.as_expr()}")
    factored = sp.factor(cp.as_expr())
    print(f"Factored: {factored}")

    # Eigenvalues
    evs = M_aug.eigenvals()
    print(f"\nEigenvalues:")
    for ev, mult in sorted(evs.items(), key=lambda x: -abs(complex(x[0]))):
        print(f"  {ev} (mult {mult})")

    # The char poly of M_aug should factor as char(M) · char(something)
    # since the augmented substitution "doubles" the original
    original_cp = M.charpoly(x)
    print(f"\nOriginal char poly: {original_cp.as_expr()}")

    # Divide to find the quotient
    q, r = sp.div(cp.as_expr(), original_cp.as_expr(), x)
    print(f"Quotient: {q}")
    print(f"Remainder: {r}")
    if r == 0:
        print("→ char(τ) = char(M) · quotient")
        qf = sp.factor(q)
        print(f"Quotient factored: {qf}")

    return aug_sub, aug_alpha, M_aug


# =====================================================================
# (b) The even sublattice as the parity-0 projection
# =====================================================================

def even_sublattice_check(aug_sub, aug_alpha):
    """
    Generate the augmented fixed point starting from a₀, then project
    onto even-indexed positions. Compare with the even sublattice of the
    original word.
    """
    print("\n" + "=" * 60)
    print("(b) Even sublattice = parity-0 projection?")
    print("=" * 60)

    # Generate augmented fixed point
    u = 'a0'
    for _ in range(6):
        new = []
        for k in range(0, len(u), 2):
            key = u[k] + u[k+1]
            new.append(aug_sub[key])
        u = ''.join(new)
        if len(u) > 200000:
            break
    # u is a string of (letter,digit) pairs
    N = len(u) // 2

    # Extract the letter sequence (stripping parities)
    letters = ''.join(u[k] for k in range(0, len(u), 2))
    print(f"Augmented word length: {N}")
    print(f"First 40 letters: {letters[:40]}")

    # Generate original word
    w = 'a'
    while len(w) < N:
        w = ''.join(SUB[c] for c in w)
    w = w[:N]
    print(f"Original word first 40: {w[:40]}")
    print(f"Match: {letters[:N] == w[:N]}")

    # Extract parity-0 positions from the augmented word
    p0_letters = ''.join(u[k] for k in range(0, len(u), 2) if u[k+1] == '0')
    # Extract even-indexed positions from the original word
    even_letters = w[0::2]

    minlen = min(len(p0_letters), len(even_letters))
    print(f"\nParity-0 sublattice: {p0_letters[:50]}")
    print(f"Even sublattice:     {even_letters[:50]}")
    print(f"Match (first {minlen}): {p0_letters[:minlen] == even_letters[:minlen]}")

    if p0_letters[:minlen] != even_letters[:minlen]:
        # Check how many match
        matches = sum(1 for a, b in zip(p0_letters, even_letters) if a == b)
        print(f"  Character matches: {matches}/{minlen}")

    return True


# =====================================================================
# (c) The BbB resonance and the ℤ/2
# =====================================================================

def bbB_and_parity():
    """
    The BbB resonance: B at position i, b at i+1, B at i+2 (3-point correlation).
    This straddles σ-image seams 100% of the time.

    Does the ℤ/2 cocycle explain WHY? B has even image (2), b has odd (3):
    - B preserves parity (even image)
    - b flips parity (odd image)
    - So BbB has parity pattern: p, p, p⊕1, p⊕1⊕1=p
    - The parity at B₁ is p, at b is p, at B₂ is p⊕1⊕1 = p.
    Wait: the parity AFTER B (image len 2, even) is same. After b (image len 3, odd)
    flips. After B₂ is... the parity of the START of B₂'s image = the parity after b.

    The question is: does the BbB pattern force a seam-straddling configuration?
    """
    print("\n" + "=" * 60)
    print("(c) BbB resonance and the ℤ/2 cocycle")
    print("=" * 60)

    # Image lengths and their parities
    img_lens = {c: len(SUB[c]) for c in ALPHA}
    print(f"Image lengths: {img_lens}")
    print(f"Parity of image lengths: { {c: img_lens[c] % 2 for c in ALPHA} }")

    # For BbB = (B, b, B) at positions (i, i+1, i+2):
    # Position of B₁ in σ(w) starts at some even/odd position.
    # B₁'s image is "aA" (length 2).
    # b's image starts immediately after B₁'s image, at offset +2.
    # b's image is "aAB" (length 3).
    # B₂'s image starts at offset +2+3 = +5 from B₁'s start.
    # Total positions covered: 2 + 3 + 2 = 7 positions in σ(w).

    # The KEY: in σ(w), the BbB pattern at positions (i, i+1, i+2) maps to
    # the block σ(B)σ(b)σ(B) = "aA" + "aAB" + "aA" = "aAaABaA" (7 chars).
    # The BOUNDARY between σ(B) and σ(b) is at position i·len + 2,
    # and between σ(b) and σ(B₂) at position i·len + 5.
    # These are INTERNAL to the 7-character block — they ARE σ-image seams.

    # So BbB always straddles seams because the 3 letters in BbB map to 3
    # ADJACENT σ-images, and by definition the boundaries between them are seams.
    # This is true for ANY 3-letter pattern — it's not specific to BbB!

    # What IS specific to BbB is that it's a RESONANCE (high 3-point correlation).
    # Why BbB specifically? Let me check which 3-letter patterns have high 3-point
    # correlation.

    w = 'a'
    while len(w) < 100000:
        w = ''.join(SUB[c] for c in w)
    w = w[:100000]

    # 3-point correlations: count all 3-grams
    trigrams = Counter(w[i:i+3] for i in range(len(w)-2))
    total = sum(trigrams.values())

    # Expected from independent letter frequencies
    freqs = Counter(w)
    f = {c: freqs[c] / len(w) for c in ALPHA}

    print(f"\nLetter frequencies: {', '.join(f'{c}={f[c]:.4f}' for c in ALPHA)}")

    # Forbidden 2-grams (from the substitution structure)
    digrams = Counter(w[i:i+2] for i in range(len(w)-1))
    d_total = sum(digrams.values())
    print(f"\nDigram frequencies (relative to independence):")
    for c1 in ALPHA:
        for c2 in ALPHA:
            dig = c1 + c2
            obs = digrams.get(dig, 0) / d_total
            exp = f[c1] * f[c2]
            if obs > 0:
                ratio = obs / exp
                print(f"  {dig}: obs={obs:.4f}, exp={exp:.4f}, ratio={ratio:.2f}")
            else:
                print(f"  {dig}: FORBIDDEN")

    print(f"\nHighest 3-gram enrichments (obs/expected from digram model):")
    enrichments = []
    for tri, count in trigrams.items():
        obs = count / total
        exp_indep = f[tri[0]] * f[tri[1]] * f[tri[2]]
        if exp_indep > 0:
            enrichments.append((tri, obs / exp_indep, obs, count))

    enrichments.sort(key=lambda x: -x[1])
    for tri, ratio, obs, count in enrichments[:15]:
        print(f"  {tri}: enrichment={ratio:.2f}× (count={count})")

    print(f"\nBbB specifically:")
    if 'BbB' in trigrams:
        obs = trigrams['BbB'] / total
        exp = f['B'] * f['b'] * f['B']
        print(f"  count={trigrams['BbB']}, obs={obs:.5f}, exp={exp:.5f}, ratio={obs/exp:.2f}×")

    # The parity pattern through BbB:
    # B (uppercase, preserves parity) → parity stays p
    # b (lowercase, flips parity) → parity becomes p⊕1
    # B (uppercase, preserves parity) → parity stays p⊕1
    # So the BbB pattern maps (p) → (p, p, p⊕1): the third letter is at OPPOSITE parity.
    # For BbB to appear, the b must be at the same parity as the first B,
    # and the second B at the opposite parity.

    # This means BbB links a B at parity p to a B at parity p⊕1 — it CROSSES
    # the parity boundary. This is the structural content of "straddling a seam":
    # the seam is the parity flip caused by the lowercase b.

    print(f"\n  Parity pattern through BbB: p → p → p⊕1")
    print(f"  BbB crosses the parity boundary (the b flips it)")
    print(f"  Every BbB links a B at one parity to a B at the other")
    print(f"  The 'seam' IS the parity flip — the ℤ/2 cocycle gives it a name")

    return True


# =====================================================================
# (d) Where does 19 come from?
# =====================================================================

def prime_19():
    """Period-6 torsion introduces the prime 19. Track its source."""
    print("\n" + "=" * 60)
    print("(d) Where does 19 come from?")
    print("=" * 60)

    # |det(M^k - I)| for k = 1,...,12
    for k in range(1, 13):
        Mk = M**k - sp.eye(4)
        d = abs(int(Mk.det()))
        f = sp.factorint(d)
        print(f"  |det(M^{k:2d} - I)| = {d:12d} = {f}")

    # The norm N(1 - β^k) = |det(M^k - I)|.
    # These are related to the dynamical zeta function of the substitution.
    # The prime factorization tells us which primes appear in the dynamics at period k.
    x = sp.Symbol('x')
    beta = sp.Rational(2, 1) + sp.sqrt(sp.Rational(5, 1))  # approx, not exact
    # Actually β is a root of x^4-2x^3-5x^2-4x-1, not 2+√5.
    # Let me compute N(1-β^6) symbolically.

    # The product (1-β₁^6)(1-β₂^6)(1-β₃^6)(1-β₄^6) where β_i are the 4 roots
    # = Res(x^4-2x^3-5x^2-4x-1, (1-y)^4 - ...) → complicated
    # Better: det(M^6 - I) directly.

    # M^6 eigenvalues are β^6, h^6, |γ|^6·e^{±6iθ}
    # where β ≈ 4.079, h ≈ 0.245, γ ≈ -0.662 ± 0.563i

    evals = M.eigenvals()
    print(f"\nEigenvalues of M:")
    for ev in evals:
        v = complex(ev)
        print(f"  {ev} ≈ {v:.6f}")

    # Compute |1 - λ^6| for each eigenvalue
    print(f"\n|1 - λ^6| for each eigenvalue:")
    prod = sp.Integer(1)
    for ev in evals:
        val = 1 - ev**6
        val_n = complex(val)
        print(f"  |1 - ({ev})^6| ≈ {abs(val_n):.4f}")
        prod *= val
    prod_val = complex(prod)
    print(f"\nProduct = {abs(prod_val):.4f} (should be 3344)")

    # The Galois group acts on these. The product decomposes as
    # N(1-β^6) · N(1-γ^6) where N is the norm from the respective fields.
    # β lives in the quartic field, so N(1-β^6) = product of all four conjugates.
    # But wait, β and h are real, γ,γ̄ are complex conjugate.
    # N(1-β^6) = (1-β^6)(1-h^6)(1-γ^6)(1-γ̄^6) = det(M^6-I) = ±3344.

    # The prime 19: does it appear because β^6 ≡ 1 mod some prime above 19?
    # In the ring of integers of ℚ(β), 19 divides N(1-β^6) means β^6 ≡ 1 mod
    # some prime ideal above 19. This means M has a period-6 orbit mod 19.

    M19 = sp.Matrix([[int(M[i, j]) % 19 for j in range(4)] for i in range(4)])
    M19_6 = sp.eye(4)
    for _ in range(6):
        M19_6 = (M19_6 * M19).applyfunc(lambda x: x % 19)
    print(f"\nM^6 mod 19:")
    print(M19_6)
    # Check if M^6 - I ≡ 0 mod 19 (i.e., if 19 | det(M^6-I))
    d6_19 = int((M19_6 - sp.eye(4)).det()) % 19
    print(f"det(M^6 - I) mod 19 = {d6_19}")

    # Order of M mod 19
    Mk = sp.eye(4)
    for k in range(1, 500):
        Mk = (Mk * M19).applyfunc(lambda x: x % 19)
        if Mk == sp.eye(4):
            print(f"Order of M mod 19 = {k}")
            break

    # Char poly mod 19
    cp19 = sp.Poly(M.charpoly(), modulus=19)
    print(f"Char poly mod 19: {cp19}")
    roots19 = [r for r in range(19)
               if (r**4 - 2*r**3 - 5*r**2 - 4*r - 1) % 19 == 0]
    print(f"Roots mod 19: {roots19}")

    return True


# =====================================================================
# (e) What the ℤ/2 says about the Perron eigenvector
# =====================================================================

def parity_perron():
    """
    The augmented substitution splits the 4-dim Perron space into
    two 4-dim spaces (one per parity). What is the Perron eigenvector
    of the augmented matrix? Is it (v, v) (symmetric) or something else?
    """
    print("\n" + "=" * 60)
    print("(e) Perron structure of the augmented substitution")
    print("=" * 60)

    # We need the augmented incidence matrix from (a)
    aug_sub = {}
    for c in ALPHA:
        img = SUB[c]
        for p_start in range(2):
            p = p_start
            result = []
            for letter in img:
                result.append(f"{letter}{p}")
                if is_lower(letter):
                    p = 1 - p
            aug_sub[f"{c}{p_start}"] = ''.join(result)

    aug_alpha = [f"{c}{p}" for c in ALPHA for p in range(2)]

    n = 8
    M_aug = np.zeros((n, n))
    for j, key in enumerate(aug_alpha):
        img = aug_sub[key]
        for k in range(0, len(img), 2):
            letter = img[k]
            parity = int(img[k+1])
            idx = ALPHA.index(letter) * 2 + parity
            M_aug[idx, j] += 1

    evals, evecs = np.linalg.eig(M_aug)
    idx = np.argmax(np.abs(evals))
    beta_aug = evals[idx]
    perron = np.abs(evecs[:, idx])
    perron /= perron.sum()

    print(f"Perron eigenvalue of augmented M: {beta_aug:.6f}")
    print(f"Perron eigenvector (normalized):")
    for i, name in enumerate(aug_alpha):
        print(f"  {name}: {perron[i]:.6f}")

    # Compare with the original Perron vector (each doubled)
    evals_orig, evecs_orig = np.linalg.eig(np.array(M, dtype=float))
    idx_orig = np.argmax(np.abs(evals_orig))
    perron_orig = np.abs(evecs_orig[:, idx_orig])
    perron_orig /= perron_orig.sum()

    print(f"\nOriginal Perron vector:")
    for i, c in enumerate(ALPHA):
        print(f"  {c}: {perron_orig[i]:.6f}")

    print(f"\nParity-0 vs parity-1 frequencies in the augmented Perron:")
    for i, c in enumerate(ALPHA):
        p0 = perron[2*i]
        p1 = perron[2*i + 1]
        print(f"  {c}: p0={p0:.6f}, p1={p1:.6f}, ratio={p0/(p1+1e-15):.4f}")

    # If p0 ≈ p1 for each letter, the ℤ/2 is "invisible" in the Perron eigenvector
    # (the two parities have equal weight).
    # If p0 ≠ p1, the parity cocycle selects a preferred parity for each letter.

    return True


if __name__ == "__main__":
    aug_sub, aug_alpha, M_aug_sym = augmented_substitution()
    even_sublattice_check(aug_sub, aug_alpha)
    bbB_and_parity()
    prime_19()
    parity_perron()
