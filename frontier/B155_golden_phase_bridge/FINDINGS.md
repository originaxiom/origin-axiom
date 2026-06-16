# B155 — the "golden × phase" spectral bridge at n=4

**Date:** 2026-06-16. **Status:** EXACT (symbolic, sympy — all checks pass). Standalone linear
algebra / arithmetic of a single integer 4×4 matrix; **no Origin-core claim**; proven core P1–P16
untouched. Nothing promotes to `../../CLAIMS.md`. Reproducer: `golden_phase_bridge.py` (pure sympy).
Ledger: V148.

**Provenance:** distilled from an external-review note (Result C) and an AI-assisted cross-session
synthesis (the "Ω" history-enumeration program), then **independently re-derived here** before banking
(verify-don't-trust: a cross-session claim is corroboration, not validation). The matrix `M_g` is the
n=4 object at which two strands of the program meet — this repo's trace-map / metallic tower (the
figure-eight monodromy enters as the "golden" rational summand) and the Ω positive-shear family
`R_{a,m}` (whose reciprocal char poly passes through the same point).

## Result

> **A single integer matrix `M_g ∈ SL(4,ℤ)` realizes "figure-eight monodromy × order-6 phase" as a
> rational block structure.** Its characteristic polynomial factors as the figure-eight monodromy
> trace polynomial (the *golden* factor, real/Anosov) times the primitive 6th cyclotomic polynomial
> (the *phase* factor, finite order), it splits over ℚ into the two companion blocks, it carries an
> invariant symmetric form of signature **(1,3)** with discriminant **−15 = disc ℚ(√5)·disc ℚ(√−3)**,
> and it glues the two invariant planes over ℤ with cokernel **(ℤ/2)²**.

`M_g = [[1,1,0,0],[0,1,1,0],[1,1,1,1],[1,1,0,1]]`, `det M_g = 1`.

| invariant | value | meaning | rigor |
|---|---|---|---|
| char poly | `(x²−3x+1)(x²−x+1) = x⁴−4x³+5x²−4x+1` | golden × phase | **exact** |
| golden factor | `x²−3x+1`, disc **5** | figure-eight monodromy trace poly (tr 3, root φ², real ⇒ Anosov) | **exact** |
| phase factor | `x²−x+1 = Φ₆`, disc **−3** | primitive 6th roots of unity (\|root\|=1 ⇒ finite order 6) | **exact** |
| rational form | `P⁻¹M_gP = [[2,1],[1,1]] ⊕ [[0,1],[−1,1]]` | genuine ℚ-block split (not just a χ factorization) | **exact** (same invariant factors) |
| `M_g` derogatory? | no (min poly = char poly) | ⇒ any matrix with this χ is **ℚ-conjugate** to `M_g` | **exact** |
| glue group | `(ℤ/2)²` (sublattice index 4, SNF `diag(1,1,2,2)`) | integral glue of the two invariant planes inside ℤ⁴ | **exact** |
| glue is class-specific | block-diagonal form (same χ) has **trivial** glue | the `(ℤ/2)²` is a GL(4,ℤ)-class invariant, **not** forced by the spectral type | **exact** |
| invariant form | signature **(1,3)**, det ≡ **−15** mod squares | `disc ℚ(√5)·disc ℚ(√−3)` — monodromy field × cyclotomic field | **exact** |

## What this is — and is not

**Is:** a *static / spectral* arithmetic coincidence, correctly scoped. The n=4 GL(4,ℤ)-class of `M_g`
carries the figure-eight monodromy as a rational summand alongside an order-6 phase, with a definite
inertia (1,3) and a definite glue (ℤ/2)². It is the cleanest "two canonical objects meet at n=4"
statement in the program.

**Is not:**
- **Not** a dynamical embedding. The figure-eight trace map preserves no quadratic form (only the cubic
  Fricke–Vogt κ); its only linear shadow is the 2×2 toral monodromy. The bridge is structure, not a
  mechanism. (External note §5, [symbolic-exact negative].)
- **Not** physics. The signature (1,3) is **algebraic inertia of a bilinear form** — *not* spacetime,
  *not* a Lorentzian metric, *not* time. See `## Firewall`.

## B206 = Ω₄ : the unification, honestly scoped

The Ω program's positive-shear family `R_{a,m} ∈ SL(4,ℤ)` has reciprocal char poly
`x⁴ − a x³ + (2a−2m−4) x² − a x + 1` and invariant form of signature (1,3) on its live cone — the
*same* shape as `M_g`. Matching char polys forces `a=4`, then `2a−2m−4 = 5 ⇒ m = −1/2`, a **half-integer**.

So the "B206 = Ω₄" unification is at the level of the **shared canonical object**: the same
golden × phase characteristic polynomial, the same signature (1,3), and (since `M_g` is nonderogatory)
the same ℚ-conjugacy class. The integer Ω lattice `{R_{a,m} : a,m ∈ ℤ}` *passes through this canonical
χ only at the half-integer point* `m = −1/2` — i.e. the two programs meet at a shared invariant, not at
a common integer lattice point. This is the honest statement; the earlier shorthand "same matrix two
ways" overstates it.

## Firewall

- **signature (1,3) = algebraic inertia** of a symmetric bilinear form. It is the sign pattern of
  eigenvalues, basis-dependent up to the inertia class. It is **NOT** spacetime, a metric, or time.
- No physical claim. The connection to the Ω "non-cancellation" motivation is firewalled motivation,
  not derivation. Nothing here touches `CLAIMS.md`.

## Reproduction

`python frontier/B155_golden_phase_bridge/golden_phase_bridge.py` — pure sympy, ~1 s, prints PASS for
every line: char poly factorization and the two field discriminants (5, −3); the rational block split
via matching invariant factors; nonderogatory ⇒ ℚ-conjugacy; the (ℤ/2)² glue as the sublattice index
plus the block-diagonal trivial-glue control (representative-specificity); the invariant form's
signature (1,3) and discriminant −15 mod squares; and the Ω₄ match at `a=4, m=−1/2`.
