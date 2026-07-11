"""
Movement XXX (continued) — image detection and the parity factor.

Key realization from listen_32: the lag-2 BbB pattern at positions (i, i+2, i+4)
forces the intermediate letters: w[i..i+4] = BabAB (since B→a, a→b, b→A, A→B
are all forced/allowed transitions and b→A is the ONLY successor).

But BabAB = trailing_B + σ(A). So every lag-2 BbB occurrence = the object
hearing "the image of A at a seam." Verify this, then follow the parity factor.
"""
import numpy as np
import sympy as sp
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = 'abAB'
M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


def word(n=163106):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


# =====================================================================
# (a) BbB at lag 2 = "B + σ(A)" at every image boundary
# =====================================================================

def verify_BbB_image_detection():
    """
    Every lag-2 BbB occurrence in the fixed-point word should correspond to
    the pattern BabAB, which is exactly [trailing B of previous image][σ(A)=abAB].
    Verify by:
    1. Confirming all lag-2 BbB instances have w[i:i+5] = BabAB
    2. Confirming these sit at σ-image boundaries
    """
    print("=" * 60)
    print("(a) BbB at lag 2 = image detection")
    print("=" * 60)

    # Work at a level where we can track image boundaries
    level = 7
    u = 'a'
    for _ in range(level):
        u = ''.join(SUB[c] for c in u)

    print(f"Word length: {len(u)}")

    # Find all lag-2 BbB occurrences
    lag2_BbB = []
    for i in range(len(u) - 4):
        if u[i] == 'B' and u[i+2] == 'b' and u[i+4] == 'B':
            lag2_BbB.append(i)

    print(f"Lag-2 BbB occurrences: {len(lag2_BbB)}")

    # Check what the full 5-letter window looks like
    windows = Counter(u[i:i+5] for i in lag2_BbB)
    print(f"Windows at lag-2 BbB sites:")
    for w, c in windows.most_common():
        print(f"  '{w}': {c}")

    # Now track σ-image boundaries at the previous level
    # The word at level k is σ(w_{k-1}). Image boundaries are at positions
    # cumsum(|σ(c)| for c in w_{k-1}).
    w_prev = 'a'
    for _ in range(level - 1):
        w_prev = ''.join(SUB[c] for c in w_prev)

    boundaries = set()
    pos = 0
    for c in w_prev:
        boundaries.add(pos)
        pos += len(SUB[c])

    print(f"\nImage boundaries: {len(boundaries)} (from {len(w_prev)} letters at level {level-1})")

    # For each lag-2 BbB at position i, check if position i+1 is an image boundary
    # (since BabAB has the boundary after B, at position i+1 where σ(A)=abAB starts)
    boundary_hits = sum(1 for i in lag2_BbB if (i+1) in boundaries)
    print(f"\nlag-2 BbB at position i with (i+1) as image boundary: {boundary_hits}/{len(lag2_BbB)}")
    if boundary_hits == len(lag2_BbB):
        print("→ EVERY lag-2 BbB sits at a σ-image boundary (B|abAB)")

    # What letter in w_prev generates the image starting at i+1?
    prev_letter_counts = Counter()
    pos = 0
    for c in w_prev:
        if pos in {i+1 for i in lag2_BbB}:
            prev_letter_counts[c] += 1
        pos += len(SUB[c])

    print(f"\nLetter in w_{{k-1}} whose image starts at the BbB boundary:")
    for c, cnt in prev_letter_counts.most_common():
        print(f"  {c}: {cnt}  (σ({c}) = {SUB[c]})")
    if len(prev_letter_counts) == 1 and 'A' in prev_letter_counts:
        print("→ EVERY lag-2 BbB detects σ(A) = abAB at a seam")

    # Also check: what letter PRECEDES the A in w_prev?
    pos = 0
    prev_of_A = Counter()
    for idx, c in enumerate(w_prev):
        if pos in {i+1 for i in lag2_BbB}:
            if idx > 0:
                prev_of_A[w_prev[idx-1]] += 1
        pos += len(SUB[c])

    print(f"\nLetter preceding A in w_{{k-1}} (i.e., the image ending in B):")
    for c, cnt in prev_of_A.most_common():
        print(f"  {c}: {cnt}  (σ({c}) = {SUB[c]}, ends in '{SUB[c][-1]}')")

    return True


# =====================================================================
# (b) The 5-letter pattern: which σ-images produce which 5-grams at seams?
# =====================================================================

def seam_pentagram():
    """
    At every σ-image boundary, the 5-letter window centered on the seam
    is determined by the trailing letters of σ(c₁) and the leading letters
    of σ(c₂). Enumerate all possible seam 5-grams.
    """
    print("\n" + "=" * 60)
    print("(b) Seam 5-grams")
    print("=" * 60)

    # Trailing letters (last 2) and leading letters (first 3) of each image
    for c in ALPHA:
        img = SUB[c]
        print(f"  σ({c}) = {img}: tail-2 = '{img[-2:]}', head-3 = '{img[:3]}'")

    print(f"\nAll possible seam 5-grams (tail-2 of σ(c₁) + head-3 of σ(c₂)):")
    seam_5grams = set()
    for c1 in ALPHA:
        for c2 in ALPHA:
            tail = SUB[c1][-2:]
            head = SUB[c2][:3]
            gram = tail + head
            seam_5grams.add(gram)
            # Check if this digram c1→c2 is allowed at the level-above word
            # The allowed digrams are the same as the substitution's combinatorics
            # c1 can be followed by c2 at level k-1 iff c1c2 is an allowed digram
            is_allowed = gram  # just print all
            print(f"  σ({c1})·σ({c2}): '{gram}'")

    print(f"\nTotal distinct seam 5-grams: {len(seam_5grams)}")
    for g in sorted(seam_5grams):
        has_BbB = (g[0] == 'B' and g[2] == 'b' and g[4] == 'B') or \
                  (len(g) >= 5 and any(g[i]=='B' and g[i+2]=='b' for i in range(len(g)-2) if i+4 < len(g) and g[i+4]=='B'))
        marker = " ← contains lag-2 BbB" if 'B' in g and 'b' in g else ""
        print(f"    '{g}'{marker}")

    return True


# =====================================================================
# (c) Number theory of the parity factor x^4 - 2x^3 - x^2 - 1
# =====================================================================

def parity_factor_number_theory():
    """
    The parity factor from the augmented substitution: x⁴ - 2x³ - x² - 1.
    Investigate its discriminant, Galois group, splitting field.
    Compare with the original: x⁴ - 2x³ - 5x² - 4x - 1.
    """
    print("\n" + "=" * 60)
    print("(c) Number theory of the parity factor")
    print("=" * 60)

    x = sp.Symbol('x')
    f_orig = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    f_par = x**4 - 2*x**3 - x**2 - 1

    # Roots (numerical)
    r_orig = [complex(r) for r in sp.solve(f_orig, x)]
    r_par = [complex(r) for r in sp.solve(f_par, x)]
    print(f"Original roots: {[f'{r:.6f}' for r in sorted(r_orig, key=lambda z: -abs(z))]}")
    print(f"Parity roots:   {[f'{r:.6f}' for r in sorted(r_par, key=lambda z: -abs(z))]}")

    # Discriminants
    d_orig = sp.discriminant(f_orig, x)
    d_par = sp.discriminant(f_par, x)
    print(f"\nDiscriminant of original: {d_orig} = {sp.factorint(int(d_orig))}")
    print(f"Discriminant of parity:   {d_par} = {sp.factorint(int(d_par))}")

    # Resolvent cubic (for Galois group determination)
    # For x^4 + px^2 + qx + r, the resolvent cubic is y^3 - py^2 - 4ry + (4pr - q^2)
    # First depress the quartic: x = t + 1/2 for x^4-2x^3-x^2-1
    t = sp.Symbol('t')
    f_par_dep = sp.Poly(f_par.subs(x, t + sp.Rational(1, 2)), t)
    print(f"\nDepressed parity quartic: {f_par_dep.as_expr()}")
    coeffs = f_par_dep.all_coeffs()
    print(f"  Coefficients: {coeffs}")

    # The standard resolvent cubic for t^4 + pt^2 + qt + r is:
    # y^3 - py^2 - 4ry + (4pr - q^2)
    # Depressed form: t^4 + p*t^2 + q*t + r
    # From coeffs: [1, 0, p, q, r] (monic, no t^3 term)
    # coeffs[0]=1, coeffs[1]=0 (no t^3), coeffs[2]=p, coeffs[3]=q, coeffs[4]=r
    p_val = coeffs[2]
    q_val = coeffs[3]
    r_val = coeffs[4]
    print(f"  p = {p_val}, q = {q_val}, r = {r_val}")

    y = sp.Symbol('y')
    resolvent = y**3 - p_val*y**2 - 4*r_val*y + (4*p_val*r_val - q_val**2)
    print(f"\nResolvent cubic: {sp.expand(resolvent)}")
    disc_res = sp.discriminant(resolvent, y)
    print(f"Resolvent discriminant: {disc_res}")

    # If resolvent disc is a perfect square → Galois = A4 or V4 or Z4
    # If resolvent disc < 0 → complex roots → S4
    # If resolvent irreducible over Q → S4 or A4
    # If resolvent has a rational root → Galois ⊆ D4

    res_roots_Q = sp.solve(resolvent, y, domain=sp.QQ)
    print(f"Rational roots of resolvent: {res_roots_Q}")

    # Factorization of the resolvent
    res_factored = sp.factor(resolvent)
    print(f"Resolvent factored: {res_factored}")

    # Also do the same for the original polynomial
    f_orig_dep = sp.Poly(f_orig.subs(x, t + sp.Rational(1, 2)), t)
    print(f"\nDepressed original quartic: {f_orig_dep.as_expr()}")
    coeffs_o = f_orig_dep.all_coeffs()
    p_o, q_o, r_o = coeffs_o[2], coeffs_o[3], coeffs_o[4]
    resolvent_o = y**3 - p_o*y**2 - 4*r_o*y + (4*p_o*r_o - q_o**2)
    print(f"Original resolvent cubic: {sp.expand(resolvent_o)}")
    disc_res_o = sp.discriminant(resolvent_o, y)
    print(f"Original resolvent discriminant: {disc_res_o}")

    res_roots_o = sp.solve(resolvent_o, y, domain=sp.QQ)
    print(f"Rational roots of original resolvent: {res_roots_o}")
    res_factored_o = sp.factor(resolvent_o)
    print(f"Original resolvent factored: {res_factored_o}")

    # Prime splitting in the parity factor
    print(f"\nPrime splitting in x^4-2x^3-x^2-1:")
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        roots_p = [r for r in range(p) if (r**4 - 2*r**3 - r**2 - 1) % p == 0]
        n_roots = len(roots_p)
        # Check for degree-2 factors
        has_quad = False
        for a1 in range(p):
            for a0 in range(p):
                # Check if x^2+a1*x+a0 divides f mod p
                # Use polynomial division
                # f = (x^2+a1*x+a0)(x^2+b1*x+b0) mod p
                # = x^4 + (a1+b1)x^3 + (a0+b0+a1*b1)x^2 + (a0*b1+a1*b0)x + a0*b0
                # Match: a1+b1 ≡ -2, a0+b0+a1*b1 ≡ -1, a0*b1+a1*b0 ≡ 0, a0*b0 ≡ -1 mod p
                b1 = (-2 - a1) % p
                b0 = (-1 - a0 - a1*b1) % p
                if (a0*b1 + a1*b0) % p == 0 and (a0*b0) % p == (-1) % p:
                    has_quad = True
                    break
            if has_quad:
                break
        if n_roots == 4:
            split_type = "splits completely"
        elif n_roots == 0 and not has_quad:
            split_type = "inert (irreducible)"
        elif n_roots == 0 and has_quad:
            split_type = "2+2"
        elif n_roots == 1:
            split_type = "1+3 or 1+1+2"
        elif n_roots == 2 and has_quad:
            split_type = "1+1+2 or 2+2"
        elif n_roots == 2:
            split_type = "1+1+2"
        elif n_roots == 3:
            split_type = "1+1+1+1 (3 found)"
        else:
            split_type = f"{n_roots} roots"
        print(f"  p={p:2d}: {n_roots} roots mod p, quad factor: {'yes' if has_quad else 'no'} → {split_type}")

    # The key question: do the original and parity factors share the SAME
    # splitting field, or different ones?
    # Compare: which primes split differently in the two fields?
    print(f"\nComparing splitting behavior (original vs parity):")
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        r_o = len([r for r in range(p) if (r**4 - 2*r**3 - 5*r**2 - 4*r - 1) % p == 0])
        r_p = len([r for r in range(p) if (r**4 - 2*r**3 - r**2 - 1) % p == 0])
        same = "SAME" if r_o == r_p else "DIFF"
        print(f"  p={p:2d}: orig has {r_o} roots, parity has {r_p} roots  [{same}]")

    return True


# =====================================================================
# (d) The product of the two char polys — what is x^8-4x^7-2x^6+8x^5+11x^4+8x^3+6x^2+4x+1?
# =====================================================================

def product_polynomial():
    """
    char(τ) = (x⁴-2x³-5x²-4x-1)(x⁴-2x³-x²-1) = x⁸-4x⁷-2x⁶+8x⁵+11x⁴+8x³+6x²+4x+1
    Is this reciprocal? What's its structure?
    """
    print("\n" + "=" * 60)
    print("(d) The product polynomial")
    print("=" * 60)

    x = sp.Symbol('x')
    f = (x**4 - 2*x**3 - 5*x**2 - 4*x - 1) * (x**4 - 2*x**3 - x**2 - 1)
    f_exp = sp.expand(f)
    print(f"Product: {f_exp}")

    # Check reciprocality: f(x) = x^8 * f(1/x)?
    coeffs = sp.Poly(f_exp, x).all_coeffs()
    print(f"Coefficients: {coeffs}")
    print(f"Reversed:     {coeffs[::-1]}")
    if coeffs == coeffs[::-1]:
        print("→ RECIPROCAL (palindromic)")
    else:
        print("→ NOT reciprocal")

    # Check individual factors for reciprocality
    f1 = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    f2 = x**4 - 2*x**3 - x**2 - 1
    c1 = sp.Poly(f1, x).all_coeffs()
    c2 = sp.Poly(f2, x).all_coeffs()
    print(f"\nOriginal coeffs:  {c1}, reversed: {c1[::-1]}")
    print(f"Parity coeffs:    {c2}, reversed: {c2[::-1]}")

    # f1: [1, -2, -5, -4, -1]. reversed: [-1, -4, -5, -2, 1]. x^4·f1(1/x) = -x^4-4x^3-5x^2-2x+1 ≠ f1
    # f2: [1, -2, -1, 0, -1]. reversed: [-1, 0, -1, -2, 1]. x^4·f2(1/x) = -x^4-x^2-2x+1 ≠ f2
    # Neither is reciprocal on its own.

    # But the product... coeffs [1,-4,-2,8,11,8,-2,-4,1] reversed = [1,-4,-2,8,11,8,-2,-4,1].
    # Wait: let me check.
    # x^8 - 4x^7 - 2x^6 + 8x^5 + 11x^4 + 8x^3 - 2x^2 - 4x + 1? Let me verify.

    # Actually recompute carefully:
    print(f"\nProduct expanded term by term:")
    p = sp.Poly(f_exp, x)
    for i in range(9):
        coeff = p.nth(8-i)
        print(f"  x^{8-i}: {coeff}")

    return True


if __name__ == "__main__":
    verify_BbB_image_detection()
    seam_pentagram()
    parity_factor_number_theory()
    product_polynomial()
