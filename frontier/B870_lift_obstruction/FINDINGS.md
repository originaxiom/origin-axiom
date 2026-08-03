# B870 — G7 closed: the object is lift-unobstructed at EVERY prime; the sister's obstruction group turns on exactly at 5

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — a referee-queue control arc; exact finite computations throughout.

## 1. The theorem, and why it is two lines

For a 2-generator 1-relator group whose relator is not a proper power, the presentation
2-complex is aspherical (Lyndon), so group cohomology = cellular cohomology; with trivial
coefficients A the only nonzero differential is the AUGMENTED Fox derivative row — the relator's
exponent sums (e_a, e_b) — giving

**H²(π₁; A) = A / gcd(e_a, e_b)·A,  H¹(π₁; A) = Hom(H₁; A).**

Both presentations from SnapPy, both relators certified not-proper-powers, both H₁ readings
cross-checked against SnapPy's homology (m004: ℤ; m003: ℤ ⊕ ℤ/5).

| manifold | relator | (e_a, e_b) | gcd | H²(π₁; ℤ/n) |
|---|---|---|---|---|
| **m004** (the object) | aaabABBAb | (1, 0) | **1** | **0 for every n** |
| **m003** (the sister) | abAAbabbb | (0, 5) | **5** | 0 unless 5 \| n; **ℤ/5 at n = 5** |

## 2. What it answers (G7)

- **E₆'s center ℤ/3**: H²(π₁(m004); ℤ/3) = 0 — **every flat E₆/ℤ₃ structure on the object lifts
  to E₆.** No obstruction exists to a full-group holonomy.
- **The SM's ℤ/6 (B862)**: H²(π₁(m004); ℤ/6) = 0 — the global-form quotient S(U(3)×U(2)) meets
  **no lift obstruction on the object**, at either of its primes.
- The vanishing is **structural, not prime-by-prime luck**: gcd(e_a, e_b) = 1 kills H²(π₁; A)
  for **every** coefficient group A at once. (This is the knot-complement fact H₂ = 0,
  Ext(ℤ, A) = 0 in presentation form; the UCT reading and the Fox reading agree.)
- **Prior art named:** the p = 2 ancestor is Culler's lifting theorem (PSL(2,ℂ) → SL(2,ℂ)
  holonomy lifts for hyperbolic 3-manifolds); for knot complements it follows from exactly this
  vanishing. The E₆/ℤ₃ and ℤ/6 statements are the same mechanism at the cascade's own centers.

## 3. The lift-ambiguity torsor

Where lifts exist their count is a torsor under H¹(π₁; Z) = Hom(H₁; Z): **3 lifts** through the
ℤ/3 center, **6 lifts** through the ℤ/6. The lift is never unique and never obstructed — the
object supplies a free, discrete choice. This is the measurement-as-torsor motif (B707's
arithmetic-CS meeting point: H¹ = torsor = measurement) appearing at the global-form layer —
recorded as an observation with the banked cross-reference, not as a new mechanism.

## 4. The object/sister split at 5

The sister is unobstructed at the atom's prime (H²(m003; ℤ/3) = 0) but carries **obstruction
group ℤ/5 at p = 5** — the first place in the program a nonzero central-lift obstruction group
appears, and it appears on the sister, at the golden prime. Stated precisely and no further:
**a nonzero obstruction GROUP means obstructed bundles are possible, not that any given flat
bundle is obstructed** — evaluating the class of an actual m003 representation is a separate
computation, not done here. The resonance with the two-ended structure (the ℚ(√5)/E₈ end) is
flagged as an observation, unweighted.

## 5. What this arc does NOT establish

- The bridge from "flat bundle on the object lifts" to "the SM gauge group's global form" is the
  framework's object→observer bridge — **not established here**; this arc computes the
  object-side cohomology any such bridge would consume.
- No claim about which lift the object "chooses": the torsor has no distinguished point here.
- Boundary-decorated refinements (rel-∂ cohomology, where Chern–Simons levels live) are a
  different computation — H²(M, ∂M) is NOT computed by this arc.

`tests/test_b870_lift_obstruction.py`
