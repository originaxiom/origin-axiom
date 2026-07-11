"""
Movement XXX — listening to the primes: why 3, why 11, and whether they talk.

Three threads from the deep listening (movement XXV) left open:
  1. The mod-3 equidistribution: WHY is the running letter-sum uniform mod 3?
     Is it algebraically connected to the order-6 twist (ω = e^{2πi/3}) at the
     trace-zero point?
  2. The lag-2 sublattice: the BbB resonance shows the object hears its own σ-image
     boundaries at lag 2.  Is the lag-2 sublattice itself substitutive?
  3. The 3·11 interaction: does the tiling prime (11) talk to the twist prime (3)?

Listen, don't force.  Report the flat as faithfully as the rich.
No physics.  Gate conditions checked at the end.
"""
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from collections import Counter, defaultdict

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPHA = 'abAB'
M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


def word(n=163106):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


# =====================================================================
# THREAD 1: the mod-3 structure
# =====================================================================

def mod3_structure():
    """Why is the running letter-sum equidistributed mod 3?"""
    print("=" * 60)
    print("THREAD 1: the mod-3 structure")
    print("=" * 60)

    # The valuation: a=0, b=1, A=2, B=3
    val = {'a': 0, 'b': 1, 'A': 2, 'B': 3}

    # Image sums and their residues mod 3
    print("\nImage sums mod 3:")
    for c in ALPHA:
        s = sum(val[x] for x in SUB[c])
        print(f"  σ({c}) = {SUB[c]}: sum = {s}, mod 3 = {s % 3}")

    # M mod 3: what is its structure over F_3?
    M3 = sp.Matrix([[int(M[i, j]) % 3 for j in range(4)] for i in range(4)])
    print(f"\nM mod 3 =\n{M3}")
    cp3 = sp.Poly(M3.charpoly(), modulus=3)
    print(f"char poly mod 3: {cp3}")

    # Is x^4-2x^3-5x^2-4x-1 irreducible mod 3?
    x = sp.Symbol('x')
    f = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    roots_mod3 = [r for r in range(3) if f.subs(x, r) % 3 == 0]
    print(f"Roots mod 3: {roots_mod3} ({'irreducible' if not roots_mod3 else 'has roots'})")

    # Check irreducibility: no roots AND no degree-2 factor
    # x^4+x^3+x^2+2x+2 mod 3 — check against all degree-2 polys mod 3
    irred_deg2_mod3 = []
    for a1 in range(3):
        for a0 in range(3):
            q = sp.Poly(x**2 + a1*x + a0, x, modulus=3)
            if all(q.eval(r) % 3 != 0 for r in range(3)):
                irred_deg2_mod3.append(q)
    f_mod3 = sp.Poly(f, x, modulus=3)
    has_deg2_factor = False
    for q in irred_deg2_mod3:
        rem = sp.div(f_mod3, q, x, domain=sp.GF(3))[1]
        if rem.is_zero:
            has_deg2_factor = True
            print(f"  has degree-2 factor: {q}")
            break
    if not has_deg2_factor and not roots_mod3:
        print("  x^4-2x^3-5x^2-4x-1 is IRREDUCIBLE mod 3 → 3 is inert in Q(β)")

    # Order of M mod 3 in GL(4, F_3)
    Mk = sp.eye(4)
    for k in range(1, 200):
        Mk = (Mk * M3).applyfunc(lambda x: x % 3)
        if Mk == sp.eye(4):
            print(f"\n  Order of M mod 3: {k}")
            break
    else:
        print("\n  Order of M mod 3: > 200")

    # The internal cumsum residues within each image
    print("\nInternal cumsum residues mod 3 within each image:")
    for c in ALPHA:
        img = SUB[c]
        cs = [sum(val[img[j]] for j in range(i + 1)) for i in range(len(img))]
        for s0 in range(3):
            residues = sorted(set((s0 + v) % 3 for v in [0] + cs))
            print(f"  σ({c}), S₀≡{s0}: residues hit = {residues} "
                  f"({'all 3' if len(residues) == 3 else f'MISSING {set(range(3)) - set(residues)}'})")

    # Verify equidistribution empirically at scale
    u = word()
    cs = np.cumsum([val[c] for c in u])
    for m in (3, 6, 11, 33):
        counts = Counter(cs % m)
        maxdev = max(abs(counts[r] / len(cs) - 1 / m) for r in range(m))
        print(f"\n  Equidistribution mod {m}: max deviation = {maxdev:.6f} "
              f"({'UNIFORM' if maxdev < 0.01 else 'NOT uniform'})")

    return True


# =====================================================================
# THREAD 2: the lag-2 sublattice
# =====================================================================

def lag2_sublattice():
    """Is the lag-2 (every-other-letter) sublattice substitutive?"""
    print("\n" + "=" * 60)
    print("THREAD 2: the lag-2 sublattice")
    print("=" * 60)

    u = word(60000)

    # Extract even-indexed and odd-indexed sublattices
    even = u[0::2]
    odd = u[1::2]

    print(f"\nWord length: {len(u)}")
    print(f"Even sublattice: length {len(even)}")
    print(f"Odd sublattice: length {len(odd)}")

    # Letter frequencies in each sublattice
    for name, sub in [("even", even), ("odd", odd)]:
        f = Counter(sub)
        total = sum(f.values())
        print(f"\n  {name} frequencies: " +
              ", ".join(f"{c}={f[c]/total:.4f}" for c in ALPHA))

    # Full-word frequencies for comparison
    f_full = Counter(u)
    total = sum(f_full.values())
    print(f"\n  full  frequencies: " +
          ", ".join(f"{c}={f_full[c]/total:.4f}" for c in ALPHA))

    # Is the even sublattice itself a fixed point of some substitution?
    # Check: for each letter c, what follows c in the even sublattice?
    # (i.e. what is the return word structure?)
    for name, sub in [("even", even)]:
        print(f"\n  {name} sublattice: digram structure")
        pairs = Counter(zip(sub, sub[1:]))
        for c in ALPHA:
            followers = {d: pairs.get((c, d), 0) for d in ALPHA}
            total_c = sum(followers.values())
            if total_c > 0:
                probs = {d: followers[d]/total_c for d in ALPHA if followers[d] > 0}
                print(f"    after {c}: {probs}")

    # Factor complexity of the even sublattice
    print(f"\n  Factor complexity of the even sublattice:")
    for n in range(1, 8):
        factors = set(even[i:i+n] for i in range(len(even) - n))
        print(f"    p({n}) = {len(factors)}")

    # Check if even sublattice has the SAME factor complexity as the full word
    print(f"\n  Factor complexity of the full word (for comparison):")
    for n in range(1, 8):
        factors = set(u[i:i+n] for i in range(len(u) - n))
        print(f"    p({n}) = {len(factors)}")

    # Return words to 'a' in the even sublattice
    a_pos = [i for i, c in enumerate(even) if c == 'a']
    if len(a_pos) > 2:
        rw = set(even[a_pos[i]:a_pos[i+1]] for i in range(min(len(a_pos)-1, 5000)))
        print(f"\n  Return words to 'a' in even sublattice: {len(rw)}")
        for w in sorted(rw, key=len)[:10]:
            print(f"    '{w}' (len {len(w)})")

    # The key question: does σ² (the square substitution) act on the even sublattice?
    # If the word is w = w_0 w_1 w_2 w_3 ..., even = w_0 w_2 w_4 ...
    # Under σ, w_i maps to σ(w_i) = a block of length |σ(w_i)|.
    # The even positions in σ(w) are NOT simply σ applied to the even positions of w
    # — the image lengths are variable (5,3,4,2) so the parity shifts.

    # But σ² doubles the word: positions in σ²(w) that came from even positions in w
    # are concentrated but not every-other.

    # Instead: check if the even sublattice is the image of some DERIVED substitution.
    # The derived substitution through every other position = the 2-block substitution.

    # The 2-block substitution: pairs (w_i, w_{i+1}) → pairs in σ(w)
    # ... this is getting complicated. Let me check numerically if even is a
    # substitution fixed point by looking at its incidence matrix.

    # If even is a fixed point of some 4-letter substitution τ, then the frequency
    # vector must be a left eigenvector of τ's incidence matrix with eigenvalue = growth.
    # The growth should be β (same as the full word) since even has half the letters.
    # But actually, under σ, the word grows by β, and the even sublattice might grow
    # by a different rate.

    # Let's check: at level k, the word has length L_k ≈ β^k.
    # The even sublattice has length L_k/2. Under σ, it becomes L_{k+1}/2 ≈ β·L_k/2.
    # So the even sublattice also grows by β. Same growth rate.

    # Now check: does the even sublattice of σ(w) = some substitution applied to even(w)?
    # Build σ(w) for a short word and extract even positions.
    test = 'a'
    for _ in range(4):
        test = ''.join(SUB[c] for c in test)

    even_test = test[0::2]
    # Apply σ again
    test2 = ''.join(SUB[c] for c in test)
    even_test2 = test2[0::2]

    print(f"\n  Even sublattice at level 4: '{even_test[:40]}...' (len {len(even_test)})")
    print(f"  Even sublattice at level 5: '{even_test2[:40]}...' (len {len(even_test2)})")

    # Check if even(σ(w)) is determined by even(w) alone
    # This would mean: for each letter c at position i in w, the contribution of σ(c)
    # to the even sublattice of σ(w) depends only on c and the parity of the starting
    # position of σ(c) in σ(w).

    # The starting parity of σ(c) depends on the CUMULATIVE image length of all
    # preceding letters — which depends on the letter sequence, not just the letter.
    # So the even sublattice of σ(w) is NOT a simple letter-by-letter function of w.

    # BUT: image lengths are 5,3,4,2. Their parities: 1,1,0,0 (odd,odd,even,even).
    # So a→5(odd), b→3(odd), A→4(even), B→2(even).
    # After image of a or b: parity FLIPS. After image of A or B: parity STAYS.
    # This means the "parity at the start of σ(c)" depends on how many a's and b's
    # precede c — equivalently, on (n_a + n_b) mod 2 of the prefix.

    # Since a,b are the LOWERCASE letters and A,B are the UPPERCASE letters,
    # this is the CASE PARITY of the prefix!

    # Interesting. Let me trace through.
    prefix_sums = []
    pos = 0
    w_short = test[:50]
    for c in w_short:
        prefix_sums.append(pos % 2)
        pos += len(SUB[c])

    # The even/odd split of images depends on case-parity of the prefix
    case_parity = [0]  # cumulative count of lowercase letters, mod 2
    for c in w_short[:-1]:
        case_parity.append((case_parity[-1] + (1 if c in 'ab' else 0)) % 2)

    print(f"\n  Parity of image-start position (first 30 letters):")
    print(f"    pos%2:       {prefix_sums[:30]}")
    print(f"    case_parity: {case_parity[:30]}")
    match = sum(1 for a, b in zip(prefix_sums, case_parity) if a == b)
    print(f"    match: {match}/{len(prefix_sums)} "
          f"({'EXACT' if match == len(prefix_sums) else 'mismatch'})")

    return True


# =====================================================================
# THREAD 3: the 3·11 interaction
# =====================================================================

def three_eleven_interaction():
    """Does the tiling prime (11) talk to the twist prime (3)?"""
    print("\n" + "=" * 60)
    print("THREAD 3: the 3·11 interaction")
    print("=" * 60)

    # The two primes and their sources:
    # 11 = H¹ torsion = |det(M-I)| = |N(1-β)|  (the tiling)
    # 3 = the twist (order 6 at trace-zero, mod-3 equidistribution)

    # M mod 11 and M mod 3: what are their structures?
    for p in [3, 11]:
        Mp = sp.Matrix([[int(M[i, j]) % p for j in range(4)] for i in range(4)])
        # Order of M mod p
        Mk = sp.eye(4)
        order = None
        for k in range(1, 500):
            Mk = (Mk * Mp).applyfunc(lambda x: x % p)
            if Mk == sp.eye(4):
                order = k
                break
        det_p = int(M.det()) % p
        print(f"\n  M mod {p}: det = {det_p}, order = {order}")

    # M mod 33 = M mod (3·11)
    M33 = sp.Matrix([[int(M[i, j]) % 33 for j in range(4)] for i in range(4)])
    Mk = sp.eye(4)
    order33 = None
    for k in range(1, 2000):
        Mk = (Mk * M33).applyfunc(lambda x: x % 33)
        if Mk == sp.eye(4):
            order33 = k
            break
    print(f"\n  M mod 33 (= mod 3·11): order = {order33}")

    # By CRT, order(M mod 33) = lcm(order(M mod 3), order(M mod 11))
    from math import gcd
    def lcm(a, b): return a * b // gcd(a, b)

    # Get the orders again
    M3 = sp.Matrix([[int(M[i, j]) % 3 for j in range(4)] for i in range(4)])
    M11 = sp.Matrix([[int(M[i, j]) % 11 for j in range(4)] for i in range(4)])
    ord3, ord11 = None, None
    Mk = sp.eye(4)
    for k in range(1, 500):
        Mk = (Mk * M3).applyfunc(lambda x: x % 3)
        if Mk == sp.eye(4):
            ord3 = k
            break
    Mk = sp.eye(4)
    for k in range(1, 2000):
        Mk = (Mk * M11).applyfunc(lambda x: x % 11)
        if Mk == sp.eye(4):
            ord11 = k
            break

    print(f"\n  order(M mod 3) = {ord3}")
    print(f"  order(M mod 11) = {ord11}")
    if ord3 and ord11:
        print(f"  lcm({ord3}, {ord11}) = {lcm(ord3, ord11)}")
        if order33:
            print(f"  order(M mod 33) = {order33}")
            if order33 == lcm(ord3, ord11):
                print("  → CRT holds: 3 and 11 are INDEPENDENT (no interaction)")
            else:
                print("  → CRT FAILS: 3 and 11 INTERACT!")

    # The Smith normal form of M-I over Z already told us the torsion is Z/11 (no Z/3).
    # Check: is there Z/3 torsion in any other homological object?
    # Smith normal form of M^T - I (same torsion):
    S = smith_normal_form(M.T - sp.eye(4), domain=sp.ZZ)
    print(f"\n  Smith(M^T - I) = diag({S[0,0]}, {S[1,1]}, {S[2,2]}, {S[3,3]})")

    # Smith of M^2 - I (period-2 orbits)
    S2 = smith_normal_form(M**2 - sp.eye(4), domain=sp.ZZ)
    print(f"  Smith(M^2 - I) = diag({S2[0,0]}, {S2[1,1]}, {S2[2,2]}, {S2[3,3]})")
    d2 = abs(int((M**2 - sp.eye(4)).det()))
    print(f"  |det(M^2 - I)| = {d2} = {sp.factorint(d2)}")

    # Smith of M^3 - I (period-3 orbits)
    S3 = smith_normal_form(M**3 - sp.eye(4), domain=sp.ZZ)
    print(f"  Smith(M^3 - I) = diag({S3[0,0]}, {S3[1,1]}, {S3[2,2]}, {S3[3,3]})")
    d3 = abs(int((M**3 - sp.eye(4)).det()))
    print(f"  |det(M^3 - I)| = {d3} = {sp.factorint(d3)}")

    # Smith of M^6 - I (period-6 orbits — the order of the twist!)
    S6 = smith_normal_form(M**6 - sp.eye(4), domain=sp.ZZ)
    print(f"  Smith(M^6 - I) = diag({S6[0,0]}, {S6[1,1]}, {S6[2,2]}, {S6[3,3]})")
    d6 = abs(int((M**6 - sp.eye(4)).det()))
    print(f"  |det(M^6 - I)| = {d6} = {sp.factorint(d6)}")

    # The N(1-β^k) = |det(M^k - I)| = the product of (1-β^k)(1-h^k)|1-γ^k|^2
    # k=1: 11.  k=2: ?  k=3: ?  k=6: ?
    # If 3 shows up in the k=3 or k=6 torsion, it means 3 appears in the
    # norm of (1-β^3) or (1-β^6) — the period-3/6 fixed-point count.
    # That would be the algebraic signature of 3 interacting with the object.

    return True


# =====================================================================
# THREAD 1b: the mod-3 equidistribution — the algebraic mechanism
# =====================================================================

def mod3_mechanism():
    """Why mod 3 specifically? Check mod p for all small primes."""
    print("\n" + "=" * 60)
    print("THREAD 1b: equidistribution mod p — what's special about 3?")
    print("=" * 60)

    u = word()
    val = {'a': 0, 'b': 1, 'A': 2, 'B': 3}
    cs = np.cumsum([val[c] for c in u])

    print("\nEquidistribution of running letter-sum mod p:")
    for p in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
        counts = Counter(cs % p)
        maxdev = max(abs(counts[r] / len(cs) - 1 / p) for r in range(p))
        status = "UNIFORM" if maxdev < 0.005 else ("~uniform" if maxdev < 0.02 else "NOT uniform")
        print(f"  mod {p:2d}: max dev = {maxdev:.5f}  {status}")

    # Is it uniform mod ALL p? Or only special ones?
    # If it's uniform mod ALL p, that means the cumulative sum is equidistributed
    # in Z — which would mean val(w_i) is equidistributed mod p for all p.
    # That's a strong statement about the letter frequencies.

    # The letter frequencies are f_a ≈ 0.272, f_b ≈ 0.168, f_A ≈ 0.346, f_B ≈ 0.214
    # The expected mean of val is 0·f_a + 1·f_b + 2·f_A + 3·f_B = f_b + 2f_A + 3f_B
    # ≈ 0.168 + 0.692 + 0.642 = 1.502

    phi = (1 + np.sqrt(5)) / 2
    sqphi = np.sqrt(phi)
    norm = phi + 1 + phi*sqphi + sqphi
    fa, fb, fA, fB = phi/norm, 1/norm, phi*sqphi/norm, sqphi/norm
    mean_val = fb + 2*fA + 3*fB
    print(f"\n  Expected mean of val = {mean_val:.6f}")
    print(f"  Is mean_val rational? {mean_val}")

    # The mean val determines what mod p can be equidistributed.
    # For uniform distribution mod p, the mean val times N should cover all residues.
    # More precisely, the Weyl/Birkhoff equidistribution theorem says it's about
    # the irrationality of the mean relative to 1/p.

    return True


if __name__ == "__main__":
    mod3_structure()
    mod3_mechanism()
    lag2_sublattice()
    three_eleven_interaction()
