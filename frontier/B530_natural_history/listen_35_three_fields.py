"""
Movement XXX (final listening pass) — the three fields.

The listening found three algebraically independent number-theoretic layers:

  1. GROWTH:   Q(√5) + D_4 → char poly factors over Q(√5) into two quadratics
               β·h = -φ, γγ̄ = 1/φ.  Splitting field = Q(√(2+√5), i), degree 8.
               disc = -400 = -2^4·5^2.

  2. PARITY:   Q(i√89) + S_4 → parity factor x^4-2x^3-x^2-1.
               disc = -1424 = -2^4·89. Splitting field degree 24.
               The shadow has BIGGER Galois group than the original.

  3. TWIST:    Q(√(-3)) → SL(2,C) character variety at trace-zero.
               cube roots of unity, the order-6 twist.

This script verifies the factorization over Q(√5) and computes what each
field layer governs in the object's dynamics.
"""
import sympy as sp
import numpy as np

x = sp.Symbol('x')
sqrt5 = sp.sqrt(5)
phi = (1 + sqrt5) / 2

f_orig = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


# =====================================================================
# (a) Verify the Q(√5) factorization of the char poly
# =====================================================================

def verify_golden_factorization():
    """
    The char poly x^4-2x^3-5x^2-4x-1 factors over Q(√5) as:
      (x^2 - (1+√5)x - φ)(x^2 + (√5-1)x + 1/φ)
    where φ = (1+√5)/2.  Verify this exactly.
    """
    print("=" * 60)
    print("(a) Factorization over Q(√5)")
    print("=" * 60)

    q1 = x**2 - (1 + sqrt5)*x - phi
    q2 = x**2 + (sqrt5 - 1)*x + 1/phi

    product = sp.expand(q1 * q2)
    diff = sp.simplify(product - f_orig)

    print(f"q1 = x² - (1+√5)x - φ")
    print(f"q2 = x² + (√5-1)x + 1/φ")
    print(f"q1·q2 = {product}")
    print(f"f_orig = {f_orig}")
    print(f"Difference: {diff}")
    print(f"→ {'EXACT MATCH' if diff == 0 else 'MISMATCH'}")

    # The structural content:
    # q1 has roots β ≈ 3.676, h ≈ -0.440 (both real)
    # q2 has roots γ, γ̄ ≈ -0.618 ± 0.486i (complex conjugate pair)

    # β + h = 1+√5 = 2φ
    # β · h = -φ
    # γ + γ̄ = -(√5-1) = 1-√5 = -2/φ
    # γ · γ̄ = 1/φ

    print(f"\nRoot sums and products:")
    print(f"  β + h = 1+√5 = 2φ ≈ {float(2*phi):.6f}")
    print(f"  β · h = -φ ≈ {float(-phi):.6f}")
    print(f"  γ + γ̄ = 1-√5 = -2/φ ≈ {float(1-sqrt5):.6f}")
    print(f"  γ · γ̄ = 1/φ ≈ {float(1/phi):.6f}")

    # The golden ratio appears at EVERY level of this factorization.
    # β = φ + √(1+φ) = φ + √φ³ (since 1+φ = φ² and √φ² = φ, so actually
    #   β = 1/2 + √5/2 + √(2+√5) = φ + √(1+2/√5+√5)... let me just verify)

    beta_expr = phi + sp.sqrt(phi**3)
    beta_val = float(beta_expr.evalf())
    beta_actual = float(sp.solve(q1, x)[1].evalf())  # larger root
    print(f"\n  β = φ + √(φ³)? {beta_val:.6f} vs actual {beta_actual:.6f} → {'YES' if abs(beta_val-beta_actual)<1e-6 else 'NO'}")

    beta_expr2 = phi + sp.sqrt(1 + phi)
    beta_val2 = float(beta_expr2.evalf())
    print(f"  β = φ + √(1+φ) = φ + √(φ²) = φ + φ = 2φ? {beta_val2:.6f} → {'YES' if abs(beta_val2-beta_actual)<1e-6 else 'NO'}")

    # Actually: 1+φ = φ², so √(1+φ) = √(φ²) = φ... no, 1+φ = φ² is correct
    # (φ² = φ+1). So √(1+φ) = √(φ²) = φ (taking positive root). But then
    # β = φ + φ = 2φ ≈ 3.236. But β ≈ 3.676. So β ≠ 2φ.

    # Let me compute correctly: from q1 = x² - 2φx - φ = 0,
    # x = (2φ ± √(4φ² + 4φ))/2 = φ ± √(φ² + φ) = φ ± √(φ+1+φ) = φ ± √(2φ+1)
    # 2φ+1 = 1+√5+1 = 2+√5. So β = φ + √(2+√5).
    beta_check = phi + sp.sqrt(2 + sqrt5)
    beta_check_val = float(beta_check.evalf())
    print(f"  β = φ + √(2+√5) ≈ {beta_check_val:.6f} vs actual {beta_actual:.6f}")
    print(f"  → {'EXACT' if abs(beta_check_val-beta_actual)<1e-10 else 'mismatch'}")

    # And h = φ - √(2+√5) (the other root of q1)
    h_check = phi - sp.sqrt(2 + sqrt5)
    h_val = float(h_check.evalf())
    h_actual = float(sp.solve(q1, x)[0].evalf())
    print(f"  h = φ - √(2+√5) ≈ {h_val:.6f} vs actual {h_actual:.6f}")

    # For γ: from q2 = x² - (1-√5)x + 1/φ = 0,
    # x = ((1-√5) ± √((1-√5)² - 4/φ))/2
    # (1-√5)² = 6-2√5. 4/φ = 4·2/(1+√5) = 8/(1+√5) = 8(√5-1)/4 = 2(√5-1) = 2√5-2.
    # (1-√5)² - 4/φ = 6-2√5 - 2√5+2 = 8-4√5 = 4(2-√5).
    # 2-√5 ≈ 2-2.236 = -0.236 < 0. So the discriminant is negative → complex roots ✓.
    # γ = ((1-√5) + i√(4(√5-2)))/2 = (1-√5)/2 + i√(√5-2)
    #   = -1/φ + i√(√5-2)

    gamma_expr = -(1/phi) + sp.I * sp.sqrt(sqrt5 - 2)
    gamma_val = complex(gamma_expr.evalf())
    # Get actual complex roots
    gamma_actual = [complex(r.evalf()) for r in sp.solve(q2, x) if sp.im(r) != 0]
    print(f"\n  γ = -1/φ + i√(√5-2) ≈ {gamma_val}")
    print(f"  actual complex roots: {gamma_actual}")

    return True


# =====================================================================
# (b) What each field layer governs
# =====================================================================

def field_layers():
    """
    Catalog what each of the three number fields governs in the object.
    """
    print("\n" + "=" * 60)
    print("(b) The three field layers")
    print("=" * 60)

    print("""
  LAYER 1 — GROWTH (the golden field Q(√5))
    disc = -400 = -2⁴·5²
    Galois = D₄ (order 8)
    Splitting field = Q(√(2+√5), i) of degree 8
    Governs:
      - Perron root β = φ + √(2+√5) ≈ 3.676 (the growth rate)
      - The contraction h = φ - √(2+√5) ≈ -0.440
      - Complex pair γ = -1/φ + i√(√5-2) (|γ| ≈ 0.786)
      - Letter frequencies (Perron eigenvector, lives in Q(β))
      - Gap labels (the rank-4 quasicrystal module)
      - Diffraction peaks (golden Bragg family)
      - Factor complexity (3n+1)
      - The 7 allowed digrams
    Key structural fact: char poly factors into two QUADRATICS over Q(√5)
      → the Perron root is only quadratic over the golden field, not quartic.
    """)

    print("""
  LAYER 2 — PARITY (the 89 field Q(√(-89)))
    disc = -1424 = -2⁴·89
    Galois = S₄ (order 24)
    Splitting field of degree 24
    Governs:
      - Parity Perron root β₂ ≈ 2.47 (the parity expansion rate)
      - The ℤ/2 case-parity cocycle (lowercase flip, uppercase preserve)
      - The BbB resonance at lag 2 (= σ(A) detection at image boundaries)
      - The 6 seam 5-grams
      - The even sublattice's higher complexity (p(n) ≈ 7n vs 3n+1)
    Key structural fact: the parity has BIGGER Galois group (S₄ vs D₄)
      → the shadow is more complex than the original.
    """)

    print("""
  LAYER 3 — TWIST (the Eisenstein field Q(√(-3)))
    Governs:
      - The order-6 twist at the trace-zero point (κ = tr[A,B] = 0)
      - Cube roots of unity ω = e^{2πi/3}
      - The H6 two-ended arithmetic (one end of the "two-ended" structure)
    Source: SL(2,C) character variety, NOT the substitution's char poly
    Key structural fact: Q(√(-3)) is NOT in the splitting field of the char poly
      → the twist comes from representation theory, not dynamics.
    """)

    print("""
  INDEPENDENCE:
    - Q(√5) ∩ Q(√(-89)) = Q  (different discriminants, no shared quadratic)
    - Q(√5) ∩ Q(√(-3))  = Q  (√3 ∉ Q(√5))
    - Q(√(-89)) ∩ Q(√(-3)) = Q  (89 ≡ 2 mod 3, so Q(√(-89)) ≠ Q(√(-3)))
    The three fields are pairwise linearly disjoint over Q.
    The object sits at the junction of three independent arithmetic worlds.
    """)

    return True


# =====================================================================
# (c) The full arithmetic content of the growth matrix
# =====================================================================

def arithmetic_content():
    """Compute the complete arithmetic data of M."""
    print("\n" + "=" * 60)
    print("(c) Complete arithmetic data of the growth matrix")
    print("=" * 60)

    print(f"M = {M.tolist()}")
    print(f"det(M) = {M.det()}")
    print(f"tr(M) = {M.trace()}")
    print(f"char poly = {f_orig}")

    # Field discriminant vs polynomial discriminant
    # Polynomial discriminant: -400
    # Number field Q(β) has discriminant...
    # For Q(β) where β is root of x⁴-2x³-5x²-4x-1:
    # Use the formula: disc(K) divides disc(f).
    # disc(f) = -400. disc(K) | -400.
    # Since f is a Pisot polynomial (one root > 1, rest inside unit circle),
    # the field Q(β) is a quartic number field.

    # The D₄ Galois group means the splitting field has degree 8 = |D₄|.
    # But Q(β) itself has degree 4. The splitting field = Q(β, γ) has degree 8.

    # Subfields of Q(β):
    # Q ⊂ Q(√5) ⊂ Q(β)
    # [Q(√5) : Q] = 2, [Q(β) : Q(√5)] = 2

    print(f"\nSubfield tower: Q ⊂ Q(√5) ⊂ Q(β)")
    print(f"  [Q(√5) : Q] = 2")
    print(f"  [Q(β) : Q(√5)] = 2 (β is root of x²-(1+√5)x-φ over Q(√5))")

    # Ring of integers: since disc(f) = -400 and [Q(β):Q] = 4,
    # the ring of integers O_K contains Z[β] as a subring of index |disc(f)|/|disc(K)|.

    # Norm and trace of β:
    # N(β) = β·h·γ·γ̄ = product of all roots = constant term = -1
    # Tr(β) = β+h+γ+γ̄ = 2 (second coefficient, negated)

    print(f"\n  N(β) = {f_orig.subs(x, 0) * (-1)**4} = {(-1)**4 * (-1)} = -1")
    print(f"  Tr(β) = 2")

    # The tiling prime 11:
    # 11 = |det(M-I)| = N(1-β)
    # x⁴-2x³-5x²-4x-1 evaluated at x=1: 1-2-5-4-1 = -11
    # So N(1-β) = (-1)⁴ · f(1) = -11 → |N(1-β)| = 11
    print(f"\n  Tiling prime: 11 = |N(1-β)| = |f(1)| = {abs(int(f_orig.subs(x, 1)))}")

    # The prime 29:
    # 29 appears at period 4: |det(M⁴-I)| = 319 = 11·29
    # f evaluated at primitive 4th root of unity: N(1-β⁴) = |det(M⁴-I)| = 319
    print(f"  Period-4 prime: 29 (|N(1-β⁴)| = 319 = 11·29)")

    # The prime 89:
    # 89 = disc(parity factor) / 16
    # Also: |det(M⁸-I)| = 28391 = 11·29·89
    print(f"  Parity prime: 89 (disc of parity factor = -2⁴·89)")
    print(f"  Also: |N(1-β⁸)| = 28391 = 11·29·89")

    # Is 89 related to 2+√5?
    # (2+√5)⁴ = (2+2.236)⁴ ≈ 4.236⁴ ≈ 321.99. Not 89.
    # φ⁸ = ((1+√5)/2)⁸. φ ≈ 1.618, φ⁸ ≈ 46.98. Not 89.
    # 89 is prime. 89 = 8·11 + 1 = 88+1. 89 ≡ 4 mod 5. 89 ≡ 2 mod 3.

    # The key period for 89: smallest k with 89 | |det(M^k-I)|
    # is k=8. And the parity factor's disc involves 89.
    # Is there a deeper connection?

    # Check: the parity factor x⁴-2x³-x²-1.
    # Its constant term is -1 (same as original).
    # Its discriminant -1424 = -16·89.
    # 89 = 1424/16 = (disc of parity) / (power of 2).

    # The connection between the parity factor and period 8:
    # The augmented substitution has char poly = f_orig · f_par.
    # M_aug^8 - I has determinant that involves both sets of eigenvalues.
    # The factor |det(M_par^8 - I)| = product of |1 - λᵢ⁸| for eigenvalues of f_par.
    # Since one of f_par's roots (≈ -0.845) has (-0.845)⁸ ≈ 0.271, close to...
    # not obviously connected.

    # Actually: 89 is a RAMIFIED prime in the parity field Q(β₂).
    # Since disc(f_par) = -2⁴·89, the prime 89 ramifies in the number field Q(β₂).
    # And 89 first appears in the period-8 dynamical zeta function |N(1-β⁸)|.
    # The connection is: β⁸ ≡ 1 mod (prime above 89), which means the parity
    # eigenvalue β₂ has period 8 modulo 89 (or its ramified ideal).

    f_par = x**4 - 2*x**3 - x**2 - 1
    # Check: does β₂ ≡ something special mod 89?
    # β₂ is a root of f_par. f_par mod 89: roots?
    roots_89 = [r for r in range(89) if (r**4 - 2*r**3 - r**2 - 1) % 89 == 0]
    print(f"\n  Roots of parity factor mod 89: {roots_89}")
    # If 89 ramifies, there might be repeated roots
    for r in roots_89:
        deriv = (4*r**3 - 6*r**2 - 2*r) % 89
        print(f"    f'({r}) mod 89 = {deriv} ({'RAMIFIED' if deriv == 0 else 'not ramified'})")

    return True


if __name__ == "__main__":
    verify_golden_factorization()
    field_layers()
    arithmetic_content()
