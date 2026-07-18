# B675 follow-on — THE BRONZE EXACT CERTIFICATION (2026-07-18)

Upgrades the banked Part-4 bronze result (b675_hcusp.py / FINDINGS.md,
"corroborated, not certified") to **CERTIFIED**.

Artifacts: `bronze_certification.py` (the full exact chain, runnable,
standalone) + `bronze_cert_output.txt` (its run log, ~80 s).

## What is now CERTIFIED (exact end-to-end)

Object: the bronze member (metallic m = 3), triangulations
`b++LLLRRR` (6 tetrahedra) and census `s464` (6 tetrahedra); cusp
shape τ in the SnapPy **default peripheral basis**, SnapPea kernel
convention τ = conj(l/m).

1. **The exact derivation chain.** The gluing + completeness rows are
   exact integer data of the triangulation. Elimination over ℚ
   (rational linear solves + sympy resultants + gcd — no floats in the
   chain) yields the shape field K = ℚ[t]/(p₈),
   p₈ = 4t⁸ − t⁷ + t⁶ − 4t⁵ − 2t⁴ − 2t³ + 12t² − 9t + 2 (irreducible;
   t = z₁). All six shapes are expressed in K and **all 8 original
   gluing/completeness equations are re-verified EXACTLY in K**.
2. **The geometric root is certified, not assumed.** Rigorous rational
   rectangle arithmetic on sympy's Sturm-based root isolation shows
   exactly one root of p₈ has all six Im zᵢ > 0 (its conjugate is the
   all-negative mirror). A positively oriented exact solution of
   gluing + completeness is a complete finite-volume hyperbolic
   structure; by Mostow it IS the geometric structure of the manifold.
   Root selection is thereby **discharged exactly** — no numeric trust
   remains.
3. **The cusp development is exact.** SnapPy's arithmetic-generic
   ComplexCuspCrossSection is run on exact K-elements, using the
   triangulation's own peripheral-curve data (= the default basis);
   `check_cusp_development_exactly()` passes (every horotriangle side
   gluing matches in K).
4. **The minimal polynomials.** By resultant (exact):
   minpoly(τ) = minpoly(ξ) = **192X⁸ + 112X⁶ + 20X⁴ + 21X² + 7**,
   irreducible ⇒ **[ℚ(τ):ℚ] = 8**;
   minpoly(u) with u = −ξ² = **192u⁴ − 112u³ + 20u² − 21u + 7**,
   irreducible ⇒ [ℚ(u):ℚ] = 4, [ℚ(τ):ℚ(u)] = 2. The octic is EVEN
   and equals quartic(−X²) identically. The y-octic
   192y⁸ − 112y⁶ + 20y⁴ − 21y² + 7 (y = Im τ) is also irreducible.
5. **Re τ = 0 EXACTLY.** u = −ξ² is exactly a quartic root (algebra);
   rigorous rectangles pin it to the unique compatible root, which is
   the positive real root in
   [1471922150465/4063729767616, 1246750789426/3442069469631]
   (≈ 0.362209653357071). Hence ξ² is exactly a negative real, so
   τ = i·√u exactly. (The quartic has exactly 2 real roots,
   Sturm-exact.)
6. **Galois group S₄ EXACTLY.** Quartic irreducible; resolvent cubic
   X³ − (5/48)X² − (21/256)X − 1015/110592 irreducible over ℚ;
   disc = −72460795904 = −2²⁴·7·617 < 0, not a rational square
   ⇒ Gal ∈ {A₄, S₄} minus A₄ ⇒ **S₄**. Independent witness
   (Dedekind, exact mod-p factorization): 3-cycle at p = 11,
   transposition at p = 47, plus transitivity ⇒ S₄. Corroboration:
   sympy galois_group (order 24, non-abelian). Disc primes {2, 7, 617}
   confirmed.
7. **Kronecker–Weber deafness input.** Every subfield of a cyclotomic
   field is abelian over ℚ; ℚ(u) has Galois closure of degree 24 (S₄),
   so ℚ(u) — and a fortiori ℚ(τ) ⊇ ℚ(u) — lies in **no cyclotomic
   field**. The H-CUSP "no stage family at any rank hears bronze"
   input is certified.
8. **The second triangulation (census s464), independently.** Same
   exact pipeline (its elimination needs a genuine 2-stage resultant
   cascade; its shape field is ℚ[s]/(2s⁸ − 9s⁷ + 12s⁶ − 2s⁵ − 2s⁴ −
   4s³ + s² − s + 4), the REVERSE of p₈). minpoly(u′) =
   **7u⁴ − 21u³ + 20u² − 112u + 192** = x⁴·q(1/x) exactly (the
   reversed quartic), Re τ′ = 0 exactly, and **u·u′ = 1 EXACTLY at
   root level**: 1/u′ is exactly a quartic root (reversal identity)
   and its exact interval isolates the same real root u was pinned to.

## Where numerics appear (and why they are not load-bearing)

- **Branch/factor selection during elimination** (symmetric-locus
  branch for b++LLLRRR; vanishing-factor choices; the univariate's
  geometric factor) is numerics-GUIDED (~45-digit evaluation), then
  **discharged** by the exact in-K verification of all 8 original
  equations plus the exact positivity certification (items 1–2).
- **Corroboration prints** against SnapPy double/HP values (~1e-13,
  0.0 at double for the root match) are reporting only.
- The rectangle/pinning arguments use exact rational interval
  arithmetic on rigorous isolation boxes refined to 1e-25 — interval
  width affects only decidability, not correctness; all decisions
  closed at the first refinement level.

## What remains OUTSIDE this certificate (stated honestly)

- SnapPy's combinatorial triangulation data (gluing rows, peripheral
  curves, the Mcomplex transfer) and sympy's factorization/resultant/
  root-isolation correctness are trusted as instruments.
- The identification "b++LLLRRR ≅ s464" (SnapPy `identify()`, banked
  in B675) is NOT re-derived here; none of the certified statements
  depends on it — each triangulation is certified standalone, and
  u·u′ = 1 is a certified relation between the two numbers.
- Classical theorems used as theorems: Thurston's gluing/completeness
  construction, Mostow rigidity, the quartic resolvent classification,
  Dedekind's theorem, Kronecker–Weber.

## Status flip for the banked arc

FINDINGS.md Part-4 status "corroborated, not certified" →
**CERTIFIED** (this cell). The banked quartic, octic, S₄, disc primes
{2, 7, 617}, [ℚ(τ):ℚ] = 8, purely-imaginary τ, and u′ = 1/u are all
confirmed EXACTLY — no correction to any banked value was needed.
