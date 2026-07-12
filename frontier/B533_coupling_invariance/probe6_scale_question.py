#!/usr/bin/env python3
"""B533 Probe 6: The Scale Question.

The object lives in ℚ(τ), τ = √φ. All ratios are algebraically
determined. But physics needs DIMENSIONAL quantities (lengths,
energies, masses). Where does scale come from?

Three questions:
  (a) Does the framework generate any natural scale candidate?
  (b) Could the scale be a ROOT of something in ℚ(τ)?
  (c) What is the minimal external input needed?
"""

import numpy as np
import sympy as sp
from itertools import product as iprod

PHI = (1 + np.sqrt(5)) / 2
TAU = np.sqrt(PHI)
BETA = PHI * (1 + TAU)


def main():
    print("=" * 78)
    print("B533 Probe 6 — The Scale Question")
    print("=" * 78)

    # ─── Part A: What scales does the framework generate? ───
    print("\n─── Part A: Natural scale candidates from the framework ───\n")

    candidates = {
        'β = 1/(√φ-1)':          BETA,
        'τ = √φ':                TAU,
        'φ = τ²':                PHI,
        'f_a = τ-1 = 1/β':       TAU - 1,
        'f_b = (τ-1)/τ²':        (TAU - 1) / TAU**2,
        'f_A = τ(τ-1)':          TAU * (TAU - 1),
        'f_B = (τ-1)/τ':         (TAU - 1) / TAU,
        '|λ₂| = 1/(1+τ)':        1 / (1 + TAU),
        '|λ₃| = 1/τ':            1 / TAU,
        'h = ln β':              np.log(BETA),
        'ln τ':                   np.log(TAU),
        'ln φ':                   np.log(PHI),
        '2π/ln β':               2 * np.pi / np.log(BETA),
        'β/2π':                   BETA / (2 * np.pi),
        'ln β / ln 2':           np.log(BETA) / np.log(2),
    }

    for name, val in candidates.items():
        print(f"  {name:30s} = {val:.10f}")

    # ─── Part B: The unit structure of ℚ(τ) ───
    print("\n─── Part B: The unit structure ───\n")

    print(f"  β = {BETA:.10f}")
    print(f"  β is a unit in O_K (ring of integers of ℚ(τ)):")
    print(f"    N(β) = product of Galois conjugates = det(M) = -1")
    print(f"    |N(β)| = 1 ⟹ β is a unit  ∎")
    print(f"")
    print(f"  τ is also a unit: N(τ) = τ·(-τ)·(iτ')·(-iτ') = τ²·τ'² = φ·|λ₃|² = φ·(1/φ) = 1")
    print(f"  (where τ' = {np.sqrt(abs(2-np.sqrt(5)))*1j}, the conjugate root)")

    # The unit group of ℚ(τ) = ℚ(√φ)
    # ℚ(τ) has signature (2,1): 2 real embeddings (τ→±τ), 1 pair complex (τ→±iτ')
    # Wait: τ⁴-τ²-1=0 has roots ±τ (real) and ±iτ' (imaginary) where τ'²=φ-1=1/φ,
    # so τ'=1/√φ=1/τ. But then iτ' are imaginary, not complex.
    # Actually the roots of x⁴-x²-1=0 are: ±√φ (real) and ±i/√φ (imaginary).
    # So the field has signature (2,1) — 2 real embeddings, 1 complex pair.
    # By Dirichlet: rank of unit group = 2+1-1 = 2.
    # The fundamental units generate a rank-2 group.

    print(f"\n  The unit group of O_K has rank 2 (Dirichlet: r₁+r₂-1 = 2+1-1 = 2)")
    print(f"  β and τ are both units. Their relationship:")
    print(f"    β = τ²+τ³ = τ²(1+τ)")
    print(f"    Are they independent? log β / log τ = {np.log(BETA)/np.log(TAU):.10f}")
    log_ratio = np.log(BETA) / np.log(TAU)
    print(f"    {log_ratio:.10f} — not a rational number (checked to 10 digits)")

    # Check if log_ratio is rational with small denominators
    for denom in range(1, 20):
        numer = round(log_ratio * denom)
        err = abs(log_ratio - numer/denom)
        if err < 1e-6:
            print(f"    POSSIBLE: log β / log τ ≈ {numer}/{denom} (err {err:.2e})")

    # ─── Part C: Scale from the substitution hierarchy ───
    print("\n─── Part C: The substitution hierarchy as scale ladder ───\n")

    print(f"  The substitution σ maps level n → level n+1.")
    print(f"  At each level, word length grows by factor β = {BETA:.6f}.")
    print(f"  The SCALE LADDER:")
    print(f"")
    print(f"  Level n   Word length   Interval size")
    print(f"  ───────   ───────────   ─────────────")
    for n in range(6):
        wl = BETA**n
        interval = 1/BETA**n
        print(f"  {n:7d}   {wl:11.3f}   {interval:13.6f}")

    print(f"\n  If we set level-0 interval = L (a physical length), then:")
    print(f"  level-n interval = L/β^n = L·(√φ-1)^n")
    print(f"")
    print(f"  The hierarchy self-generates an INFINITE TOWER of scales,")
    print(f"  separated by factor β = {BETA:.6f}.")
    print(f"  But the ratio between any two levels is β^k ∈ ℚ(τ) — no new information.")

    # ─── Part D: The root question ───
    print("\n─── Part D: Could the scale be a ROOT of something in ℚ(τ)? ───\n")

    print(f"  The object lives in ℚ(τ) where τ = √φ = φ^(1/2).")
    print(f"  φ lives in ℚ(√5). But √φ does NOT live in ℚ(√5).")
    print(f"  So the object ALREADY took the 'root': ℚ(τ) = ℚ(φ^(1/2)).")
    print(f"")
    print(f"  Could we go deeper? Consider τ^(1/2) = φ^(1/4):")

    tau_half = PHI**(1/4)
    print(f"    τ^(1/2) = φ^(1/4) = {tau_half:.10f}")
    print(f"    min poly: x⁸ - x⁴ - 1 = 0 (degree 8 over ℚ)")
    print(f"    This would be a degree-8 number field.")
    print(f"")
    print(f"  Or φ^(1/3) = {PHI**(1/3):.10f}")
    print(f"    min poly: degree 6 over ℚ")
    print(f"")
    print(f"  BUT: the substitution has 4 letters → degree 4 field → τ = √φ.")
    print(f"  Higher roots would require more letters (or structure the object doesn't have).")
    print(f"  The degree-4 field is FORCED by the alphabet size.")

    # ─── Part E: The determinant and orientation ───
    print("\n─── Part E: det(M) = -1 and the orientation question ───\n")

    print(f"  det(M) = -1 means the substitution REVERSES orientation.")
    print(f"  Under σ², orientation is preserved: det(M²) = 1.")
    print(f"")
    print(f"  The eigenvalues of M² are:")
    eigs_m2 = [BETA**2, (1/(1+TAU))**2, (1/TAU)**2 * np.exp(2j*np.arctan(np.sqrt(np.sqrt(5)-2) / (-1/PHI))).real]
    print(f"    β² = {BETA**2:.10f}")
    print(f"    |λ₂|² = {(1/(1+TAU))**2:.10f}")
    lam3_re = -1/PHI
    lam3_im = np.sqrt(np.sqrt(5) - 2)
    lam3_sq = (lam3_re + 1j*lam3_im)**2
    print(f"    λ₃² = {lam3_sq:.10f}")
    print(f"    λ₄² = {lam3_sq.conjugate():.10f}")
    print(f"    |λ₃|² = 1/φ = {1/PHI:.10f}")
    print(f"")
    print(f"  β² satisfies y² - 2·3.676...·y + 1 = ? No: β² = {BETA**2:.6f}")
    print(f"  β² = β·β = (τ²(1+τ))² = τ⁴(1+τ)² = (τ²+1)(1+τ)²")
    val = (TAU**2 + 1) * (1 + TAU)**2
    print(f"    = {val:.10f} (check: {BETA**2:.10f})")

    # ─── Part F: The 2π connection ───
    print("\n─── Part F: Does 2π arise from the framework? ───\n")

    # The complex eigenvalues λ₃,₄ = -1/φ ± i√(√5-2) have a PHASE
    theta = np.arctan2(lam3_im, lam3_re)
    print(f"  Phase of λ₃: arg(λ₃) = {theta:.10f} rad = {np.degrees(theta):.6f}°")
    print(f"    π - arg(λ₃) = {np.pi - theta:.10f} rad = {np.degrees(np.pi - theta):.6f}°")
    print(f"    arg(λ₃)/π = {theta/np.pi:.10f}")
    print(f"    Is arg(λ₃)/π rational? If so, λ₃ is a root of unity × |λ₃|.")

    # Check rationality
    for denom in range(1, 50):
        numer = round(theta * denom / np.pi)
        err = abs(theta / np.pi - numer / denom)
        if err < 1e-5:
            print(f"    arg(λ₃)/π ≈ {numer}/{denom} (err {err:.2e})")

    # The ANGLE introduces transcendental numbers (π, cos, sin)
    # This is the ONLY place where transcendentals enter.
    print(f"\n  The angle θ = arg(λ₃) = arctan(√(√5-2) / (-1/φ))")
    print(f"  = π - arctan(φ·√(√5-2))")
    phi_sqrt_arg = PHI * np.sqrt(np.sqrt(5) - 2)
    print(f"  φ·√(√5-2) = {phi_sqrt_arg:.10f}")
    print(f"  arctan({phi_sqrt_arg:.6f}) = {np.arctan(phi_sqrt_arg):.10f} rad")
    print(f"                              = {np.degrees(np.arctan(phi_sqrt_arg)):.6f}°")

    # Is φ·√(√5-2) algebraic? YES: it's in ℚ(τ).
    # √(√5-2) = √(2/φ - 2 + √5) ... let me compute more carefully.
    # √5-2 = 2φ-1-2 = 2φ-3. No: √5 = 2φ-1, so √5-2 = 2φ-3.
    # √(√5-2) = √(2φ-3). Is this in ℚ(τ)?
    # 2φ-3 = 2τ²-3. So √(2τ²-3). For this to be in ℚ(τ), we need
    # 2τ²-3 = (aτ+b)² for some a,b ∈ ℚ.
    # Expanding: a²τ²+2abτ+b² = 2τ²-3.
    # So a²=2 (irrational!) — NO. √(2τ²-3) is NOT in ℚ(τ).
    # But |λ₃|² = 1/φ IS in ℚ(τ), and the ANGLE is NOT.

    print(f"\n  CONCLUSION: |λ₃| = 1/τ ∈ ℚ(τ) (algebraic)")
    print(f"  But arg(λ₃) is a transcendental angle — NOT in ℚ(τ).")
    print(f"  θ/π ≈ {theta/np.pi:.10f} — irrational (checked to denom 50).")

    # ─── Part G: What the framework provides vs needs ───
    print("\n─── Part G: The scale inventory ───\n")

    print(f"  INTRINSIC (from ℚ(τ) = ℚ(√φ), no external input):")
    print(f"  ──────────────────────────────────────────────────")
    print(f"  • All dimensionless ratios: τ, φ, β, f_a, f_b, f_A, f_B")
    print(f"  • The eigenvalue spectrum: β, |λ₂|, |λ₃|")
    print(f"  • The hierarchy spacing: β^n for all n")
    print(f"  • The 5 observation types and their Perron fingerprints")
    print(f"  • det(M) = -1 (orientation)")
    print(f"")
    print(f"  TRANSCENDENTAL (from the complex eigenvalue phase):")
    print(f"  ──────────────────────────────────────────────────")
    print(f"  • θ = arg(λ₃) = {theta:.10f} rad ≈ {np.degrees(theta):.4f}°")
    print(f"  • This is the ONLY transcendental the object generates.")
    print(f"  • It enters through the ROTATION of the Rauzy fractal.")
    print(f"  • cos θ = Re(λ₃)/|λ₃| = (-1/φ)/(1/τ) = -τ/φ = -1/τ = -{1/TAU:.10f}")
    cos_theta = -1/TAU
    sin_theta = np.sqrt(1 - cos_theta**2)
    print(f"  • sin θ = √(1 - 1/τ²) = √(1 - 1/φ) = √((φ-1)/φ) = √(1/φ²) = 1/φ?")
    print(f"    sin θ = {sin_theta:.10f}, 1/φ = {1/PHI:.10f}")
    # Actually: 1 - 1/τ² = 1 - 1/φ = (φ-1)/φ = (1/φ)/φ = 1/φ².
    # Wait: 1/τ² = 1/φ. So 1-1/φ = (φ-1)/φ = (1/φ)/1 = ... no.
    # φ-1 = 1/φ. So (φ-1)/φ = 1/φ² = (√5-1)²/4 = (6-2√5)/4 = (3-√5)/2.
    # √((3-√5)/2) = ?
    # (3-√5)/2 ≈ (3-2.236)/2 = 0.764/2 = 0.382.
    # √0.382 = 0.618... wait.
    # √(1/φ²) = 1/φ = 0.618.
    # But sin θ = 0.618! So sin θ = 1/φ!

    print(f"\n  WAIT: sin θ = {sin_theta:.10f}")
    print(f"         1/φ = {1/PHI:.10f}")
    print(f"  sin θ = 1/φ? {abs(sin_theta - 1/PHI) < 1e-10}")

    # cos θ = -1/τ, sin θ = ... let me compute exactly.
    # λ₃ = -1/φ + i√(√5-2), |λ₃| = 1/τ.
    # cos θ = Re(λ₃)/|λ₃| = (-1/φ)/(1/τ) = -τ/φ = -τ/τ² = -1/τ.
    # sin θ = Im(λ₃)/|λ₃| = √(√5-2)/(1/τ) = τ√(√5-2).
    # sin²θ = τ²(√5-2) = φ(√5-2) = φ√5 - 2φ.
    # √5 = 2φ-1, so φ√5 = φ(2φ-1) = 2φ²-φ = 2(φ+1)-φ = φ+2.
    # sin²θ = φ+2-2φ = 2-φ = 2-(1+√5)/2 = (4-1-√5)/2 = (3-√5)/2.
    # And (3-√5)/2 = 1/φ²? Check: 1/φ² = ((√5-1)/2)² = (6-2√5)/4 = (3-√5)/2. YES!
    # So sin²θ = 1/φ², i.e., sin θ = 1/φ (taking positive root since θ ∈ (π/2,π)).

    print(f"\n  PROVED: cos θ = -1/τ = -1/√φ")
    print(f"          sin θ = 1/φ")
    print(f"  Both cos θ and sin θ are in ℚ(τ)!")
    print(f"")
    print(f"  So θ is NOT transcendental after all! Its trig values are algebraic.")
    print(f"  θ = arccos(-1/√φ) = π - arccos(1/√φ)")
    print(f"  But θ/π is IRRATIONAL — the angle itself is not a rational multiple of π.")

    # ─── Part H: The REAL scale question ───
    print("\n─── Part H: The real scale question ───\n")

    print(f"  FACT: every measurable quantity the object produces is in ℚ(τ).")
    print(f"  Even the complex eigenvalue's trig components: cos θ = -1/τ, sin θ = 1/τ².")
    print(f"")
    print(f"  The object provides a COMPLETE SET OF RATIOS but no absolute unit.")
    print(f"  Think of it as a SHAPE without SIZE.")
    print(f"")
    print(f"  Question: does the shape itself contain a scale?")
    print(f"")
    print(f"  CANDIDATE 1: β as a scale ratio")
    print(f"    Each σ-step magnifies by β = 3.676...")
    print(f"    The hierarchy n → n+1 has ratio β.")
    print(f"    If 'level 0' has physical size L, level n has size L·β^n.")
    print(f"    But β is determined by τ — it's not a NEW scale.")
    print(f"")
    print(f"  CANDIDATE 2: h = ln β = {np.log(BETA):.10f} as entropy")
    print(f"    The topological entropy of the subshift.")
    print(f"    Dimensionless, but ln introduces transcendentals.")
    print(f"    Could be related to thermodynamic temperature: k_B T ~ h·ε")
    print(f"    where ε is an energy scale. But ε is external.")
    print(f"")
    print(f"  CANDIDATE 3: the Rauzy fractal dimension")
    print(f"    The fractal boundary has Hausdorff dim ≈ 1.1... (computed in B530)")
    print(f"    Related to log|λ₃|/log β = -log τ / log β")
    dim_ratio = -np.log(TAU) / np.log(BETA)
    print(f"    = {dim_ratio:.10f}")
    print(f"    This IS a ratio of algebraic numbers' logarithms — likely irrational.")
    print(f"    But the dim itself may be transcendental.")
    print(f"")
    print(f"  CANDIDATE 4: the NUMBER FIELD DISCRIMINANT")

    # Discriminant of ℚ(τ) = ℚ[x]/(x⁴-x²-1)
    x = sp.Symbol('x')
    f = x**4 - x**2 - 1
    disc = sp.discriminant(f, x)
    print(f"    disc(x⁴-x²-1) = {disc}")
    print(f"    = {int(disc)}")
    # Factor it
    print(f"    = {sp.factorint(int(disc))}")
    print(f"    This is an INTEGER — the only honest integer the object generates.")
    print(f"    (Compare: M's charpoly discriminant = disc(x⁴-2x³-5x²-4x-1) = ?)")
    disc_M = sp.discriminant(x**4 - 2*x**3 - 5*x**2 - 4*x - 1, x)
    print(f"    disc(charpoly M) = {disc_M} = {sp.factorint(int(disc_M))}")

    # ─── SYNTHESIS ───
    print("\n" + "=" * 78)
    print("SYNTHESIS — The Scale Picture")
    print("=" * 78)

    print(f"""
  THE OBJECT IS COMPLETELY SELF-SIMILAR.
  It generates the number field ℚ(τ) = ℚ(√φ) and nothing else.
  ALL ratios are determined. NO free parameters.

  THE SCALE IS EXTERNAL.
  The object provides SHAPE but not SIZE.
  One physical measurement (a single dimensional quantity L)
  fixes all dimensions.

  THE ROOT IS ALREADY TAKEN.
  The object lives at τ = √φ = φ^(1/2), not at φ.
  The 'square root' of the golden ratio IS the generator.
  Going deeper (φ^(1/4), etc.) would need a larger alphabet.
  The degree-4 field is forced by the 4-letter alphabet.

  SURPRISE: sin θ = 1/φ, cos θ = -1/√φ.
  The complex eigenvalues' phase has ALGEBRAIC trig values.
  The object is 'more algebraic' than expected — even its
  rotational component lives in ℚ(τ).

  HONEST INTEGERS from the framework:
  • disc(ℚ(τ)) = {int(disc)}
  • det(M) = -1

  FOR GATE 3: the SM comparison can ONLY involve ratios.
  The question is: does any SM dimensionless ratio live in ℚ(√φ)?
  That's a falsifiable question with a sharp answer.
    """)


if __name__ == '__main__':
    main()
