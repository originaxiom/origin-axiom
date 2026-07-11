"""
Movement XXX (continued) — Galois group correction and the two fields.

Listen_33 found: the resolvent cubic of x^4-2x^3-5x^2-4x-1 has a rational
root y=-3/2.  Standard Galois theory:
  - resolvent has rational root  →  Gal ⊆ D_4
  - disc = -400 < 0  →  Gal ⊄ A_4
  - quartic irreducible  →  4 | |Gal|
  - ⇒  Gal = D_4  (order 8)

Earlier sessions stated S_4.  Was that banked? Check and correct.

Also: the parity factor's two real roots sum to ≈ 1.62 ≈ φ.
Is this exactly the golden ratio?
"""
import sympy as sp
import numpy as np

x = sp.Symbol('x')

f_orig = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
f_par = x**4 - 2*x**3 - x**2 - 1

M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


# =====================================================================
# (a) Verify D_4: check no prime ≤ 200 gives a (1)(3) splitting
# =====================================================================

def check_splitting_all_primes():
    """
    If Gal = D_4, no prime should give a (linear)(irreducible cubic) factorization.
    If Gal = S_4, about 1/3 of primes should give this pattern.
    Check systematically.
    """
    print("=" * 60)
    print("(a) Checking for (1)(3) splitting — D_4 vs S_4 test")
    print("=" * 60)

    primes = list(sp.primerange(2, 200))
    count_13_orig = 0
    count_13_par = 0
    total = 0

    for p in primes:
        # Original: x^4-2x^3-5x^2-4x-1 mod p
        roots_orig = [r for r in range(p) if (r**4 - 2*r**3 - 5*r**2 - 4*r - 1) % p == 0]
        roots_par = [r for r in range(p) if (r**4 - 2*r**3 - r**2 - 1) % p == 0]

        if len(roots_orig) == 1:
            # Has exactly 1 root mod p — could be (1)(3) or (1)(1)(2)
            # Check: divide out the linear factor and test if the cubic is irreducible
            r = roots_orig[0]
            # f / (x - r) mod p
            coeffs = [1, -2 - r, None, None]
            # Synthetic division of x^4-2x^3-5x^2-4x-1 by (x-r) mod p
            c = [1, -2, -5, -4, -1]
            q = [0]*4
            q[0] = c[0]  # = 1
            q[1] = (c[1] + r*q[0]) % p
            q[2] = (c[2] + r*q[1]) % p
            q[3] = (c[3] + r*q[2]) % p
            # remainder: (c[4] + r*q[3]) % p should be 0
            # The cubic is q[0]*x^3 + q[1]*x^2 + q[2]*x + q[3]
            cubic_roots = [s for s in range(p) if (q[0]*s**3 + q[1]*s**2 + q[2]*s + q[3]) % p == 0]
            if len(cubic_roots) == 0:
                count_13_orig += 1
                print(f"  ORIGINAL: (1)(3) at p={p}, root={r}, cubic [{q[0]},{q[1]},{q[2]},{q[3]}]")

        if len(roots_par) == 1:
            r = roots_par[0]
            c = [1, -2, -1, 0, -1]
            q = [0]*4
            q[0] = c[0]
            q[1] = (c[1] + r*q[0]) % p
            q[2] = (c[2] + r*q[1]) % p
            q[3] = (c[3] + r*q[2]) % p
            cubic_roots = [s for s in range(p) if (q[0]*s**3 + q[1]*s**2 + q[2]*s + q[3]) % p == 0]
            if len(cubic_roots) == 0:
                count_13_par += 1
                if count_13_par <= 5:
                    print(f"  PARITY:   (1)(3) at p={p}, root={r}")

        total += 1

    print(f"\n  Primes tested: {total}")
    print(f"  Original (1)(3) count: {count_13_orig} → {'D_4 CONFIRMED' if count_13_orig == 0 else 'S_4'}")
    print(f"  Parity   (1)(3) count: {count_13_par} → {'D_4' if count_13_par == 0 else f'S_4 (expected ~{total//3})'}")


# =====================================================================
# (b) Sum of real roots of the parity factor
# =====================================================================

def parity_real_root_sum():
    """Is the sum of the two real roots of x^4-2x^3-x^2-1 exactly φ?"""
    print("\n" + "=" * 60)
    print("(b) Sum of real roots of the parity factor")
    print("=" * 60)

    roots = sp.solve(f_par, x)
    real_roots = [r for r in roots if sp.im(r) == 0]
    complex_roots = [r for r in roots if sp.im(r) != 0]

    print(f"Real roots: {[sp.nsimplify(r, rational=False) for r in real_roots]}")
    print(f"  numerical: {[float(r.evalf()) for r in real_roots]}")

    s_real = sum(real_roots)
    s_real_simplified = sp.simplify(s_real)
    s_real_num = float(s_real.evalf())
    phi = (1 + sp.sqrt(5)) / 2

    print(f"\nSum of real roots: {s_real_simplified}")
    print(f"  numerical: {s_real_num:.10f}")
    print(f"  φ = {float(phi.evalf()):.10f}")
    print(f"  difference: {abs(s_real_num - float(phi.evalf())):.2e}")

    if abs(s_real_num - float(phi.evalf())) < 1e-8:
        # Check exactly
        check = sp.simplify(s_real - phi)
        print(f"  Exact check s - φ = {check}")
        if check == 0:
            print("  → Sum of real roots IS exactly φ!")
        else:
            print(f"  → Not exactly φ (simplified diff: {check})")
    else:
        print("  → NOT φ")

    # Product of real roots
    p_real = sp.prod(real_roots)
    p_real_num = float(p_real.evalf())
    print(f"\nProduct of real roots: {p_real_num:.10f}")
    print(f"  -1/φ = {-1/float(phi.evalf()):.10f}")

    # Sum and product of complex roots
    if complex_roots:
        s_complex = sum(complex_roots)
        p_complex = sp.prod(complex_roots)
        print(f"\nSum of complex roots: {sp.simplify(s_complex)}")
        print(f"  numerical: {complex(s_complex.evalf())}")
        print(f"Product of complex roots (= |γ|²): {float(sp.re(p_complex.evalf())):.10f}")

    # If real roots sum to φ and all roots sum to 2, complex roots sum to 2-φ = 1/φ
    print(f"\nIf s_real = φ: s_complex = 2-φ = 1/φ = {1/float(phi.evalf()):.10f}")

    # Factor x^4-2x^3-x^2-1 over Q(√5)
    print("\nFactoring x^4-2x^3-x^2-1 over Q(√5):")
    sqrt5 = sp.sqrt(5)

    # (x^2 - s_r·x + p_r)(x^2 - s_c·x + p_c)
    # s_r + s_c = 2
    # If s_r = φ = (1+√5)/2, then s_c = (3-√5)/2
    sr = (1 + sqrt5) / 2
    sc = (3 - sqrt5) / 2
    # p_r + p_c + s_r·s_c = -1
    # p_r·p_c = -1
    # s_r·s_c = (1+√5)(3-√5)/4 = (3-√5+3√5-5)/4 = (-2+2√5)/4 = (√5-1)/2 = 1/φ
    sr_sc = sp.simplify(sr * sc)
    print(f"  s_r = {sr}, s_c = {sc}")
    print(f"  s_r · s_c = {sr_sc}")

    # p_r + p_c = -1 - s_r·s_c = -1 - (√5-1)/2 = -(1+√5)/2 = -φ
    # p_r · p_c = -1
    # So p_r, p_c are roots of t^2 + φ·t - 1 = 0
    t = sp.Symbol('t')
    quad = t**2 + phi*t - 1
    print(f"  Quadratic for p_r, p_c: {quad}")
    p_roots = sp.solve(quad, t)
    print(f"  p_r, p_c = {[sp.simplify(r) for r in p_roots]}")
    p_roots_num = [float(r.evalf()) for r in p_roots]
    print(f"  numerical: {p_roots_num}")

    # Verify: construct the factorization and expand
    for pr, pc in [(p_roots[0], p_roots[1]), (p_roots[1], p_roots[0])]:
        f_test = (x**2 - sr*x + pr) * (x**2 - sc*x + pc)
        f_test_exp = sp.expand(f_test)
        diff = sp.simplify(f_test_exp - f_par)
        if diff == 0:
            print(f"\n  FACTORIZATION VERIFIED:")
            print(f"    (x² - {sr}·x + {sp.simplify(pr)}) · (x² - {sc}·x + {sp.simplify(pc)})")
            break
    else:
        print("  Factorization NOT verified")


# =====================================================================
# (c) The splitting field and √(-3)
# =====================================================================

def splitting_field_analysis():
    """
    Original: splitting field = Q(√(2+√5), i), degree 8, Galois = D_4.
    Contains √5 and i. Does NOT contain √(-3) = i√3.
    For √(-3) ∈ splitting field, need √3 ∈ Q(√(2+√5)).
    Q(√(2+√5)) has unique quadratic subfield Q(√5).
    √3 ∉ Q(√5). So √(-3) ∉ splitting field.

    Verify this chain. Where does Q(√(-3)) actually come from in the object?
    """
    print("\n" + "=" * 60)
    print("(c) Does the splitting field contain √(-3)?")
    print("=" * 60)

    # The splitting field of f_orig
    # Roots: β = 1/2 + √5/2 + √(2+√5), h = 1/2 + √5/2 - √(2+√5),
    #         γ = 1/2 - √5/2 + i√(√5-2), γ̄ conjugate

    sqrt5 = sp.sqrt(5)
    alpha = sp.sqrt(2 + sqrt5)

    beta = sp.Rational(1, 2) + sqrt5/2 + alpha
    h = sp.Rational(1, 2) + sqrt5/2 - alpha

    print(f"β = {beta}")
    print(f"h = {h}")
    print(f"β + h = {sp.simplify(beta + h)}")  # should be 1 + √5
    print(f"β · h = {sp.simplify(beta * h)}")  # should be -φ

    # Check β·h
    bh = sp.expand(beta * h)
    bh_simp = sp.simplify(bh)
    print(f"β·h simplified: {bh_simp}")

    # The quadratic subfield of Q(α) = Q(√(2+√5)):
    # α² = 2+√5, so √5 = α²-2 ∈ Q(α). Thus Q(√5) ⊂ Q(α).
    # Is there another quadratic subfield? Q(α)/Q has degree 4 (minpoly x⁴-4x²-1).
    # The subfield lattice: Q ⊂ Q(√5) ⊂ Q(α), and Q ⊂ Q(α²-2) = Q(√5).
    # No other quadratic subfield.

    # √3 in Q(√5)? Q(√5) = {a + b√5 : a,b ∈ Q}. (a+b√5)² = a²+5b²+2ab√5.
    # For this to equal 3: 2ab = 0 and a²+5b² = 3.
    # ab=0 → a=0 or b=0.
    # b=0: a²=3, a=√3 ∉ Q. a=0: 5b²=3, b=√(3/5) ∉ Q.
    # So √3 ∉ Q(√5), confirming √(-3) ∉ Q(α,i).

    print(f"\n√3 ∉ Q(√5): verified (no rational a,b with (a+b√5)² = 3)")
    print(f"⇒ √(-3) ∉ Q(√(2+√5), i) = splitting field of f_orig")
    print(f"⇒ Q(√(-3)) is NOT in the splitting field of the char poly")

    # Then where does √(-3) come from in the object?
    # It comes from the trace-zero point of the SL(2,C) character variety.
    # At κ = tr([A,B]) = 0, the eigenvalues of the monodromy are cube roots of ±1,
    # which involve ω = e^{2πi/3} = (-1+√(-3))/2.
    # This is a property of SL(2,C) representation theory, not of the substitution.

    print(f"\nThe √(-3) comes from the SL(2,C) character variety at the trace-zero")
    print(f"point, NOT from the substitution's char poly or its splitting field.")
    print(f"The two arithmetic ends share Q(√5) but are algebraically independent")
    print(f"beyond it: one generates Q(√(2+√5), i), the other generates Q(√(-3)).")

    # What is the smallest field containing BOTH?
    # Q(√5, √(2+√5), i, √(-3)) = Q(√(2+√5), i, √3)
    # [Q(√(2+√5),i) : Q] = 8, [Q(√3) : Q] = 2
    # Is √3 ∈ Q(√(2+√5), i)? No (proven above).
    # So [Q(√(2+√5), i, √3) : Q] = 16.
    # Galois group: D_4 × Z/2 (semi-direct product if they interact,
    #               direct product if independent).

    print(f"\nThe joint field: Q(√(2+√5), i, √3)")
    print(f"  degree = 16 = 8 × 2 (√3 independent of the char poly's splitting field)")
    print(f"  Galois group = D_4 × Z/2 (direct product, since the fields are linearly disjoint)")

    return True


# =====================================================================
# (d) Where S_4 was stated — check for prior claims
# =====================================================================

def prior_s4_check():
    """Check if S_4 was claimed in banked results that need correction."""
    print("\n" + "=" * 60)
    print("(d) S_4 vs D_4: what needs correcting?")
    print("=" * 60)

    print("Earlier listening movements stated 'Galois group S_4'.")
    print("The resolvent cubic test shows Gal = D_4 (resolvent has rational root y=-3/2).")
    print("")
    print("Impact assessment:")
    print("  - The H6 finding (two-ended arithmetic) remains valid:")
    print("    the splitting field contains Q(√5) and i; Q(√(-3)) comes from")
    print("    the character variety, not the char poly. The 'two-endedness'")
    print("    is REAL but the ends are MORE independent than S_4 would imply.")
    print("  - D_4 ⊂ S_4: the Galois symmetry is SMALLER than stated.")
    print("    This means the char poly has MORE structure (it factors over")
    print("    Q(√5) into two quadratics, which S_4 wouldn't allow).")
    print("  - The factorization over Q(√5) is a structural relationship")
    print("    between the Perron root and the golden ratio — the object's")
    print("    growth rate is QUADRATIC over Q(√5), not quartic.")

    return True


if __name__ == "__main__":
    check_splitting_all_primes()
    parity_real_root_sum()
    splitting_field_analysis()
    prior_s4_check()
