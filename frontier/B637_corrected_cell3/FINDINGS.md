# B637 — the corrected cell 3, part 1: the dimension table CONFIRMED by the amalgam-Fox route

**Date: 2026-07-15. Status: part 1 BANKED (prereg 99815a48…, sealed
before running). Mathematics only; Gate 5 standing.**

## Part 1 results (`b637_dimension_table.py`, `part1_output.txt`; exact over ℚ(ω))

- **The weld gluing exists constructively:** the SL(2)-level peripheral
  intertwiner space for (μ ↦ μ, λ ↦ λ⁻¹) against the conjugate rep is
  2-dimensional with an invertible representative of det 1; its lift
  through the principal embedding (Bruhat factorization; h_pr diagonal,
  all 27-weights even) satisfies BOTH peripheral gates exactly in
  GL(27).
- **The control passed first:** trivial coefficients give h⁰ = 1,
  h¹ = 1 (b₁(D) = 1 — matching B591-M4's "ordinary H₁ = ℤ").
- **THE DIMENSION TABLE, all seven registered predictions CONFIRMED**
  by this pipeline (4-generator amalgam presentation, Fox calculus,
  108-dim cochains — method-disjoint from the audit's matched-pair
  M–V route):

      none: h⁰ = 1, h¹(D;27) = 5
      m=1:  h⁰ = 1, h¹ = 5
      m=4:  h⁰ = 0, h¹ = 2   (the full-E₆ chiral bend)
      m=5:  h⁰ = 1, h¹ = 5
      m=7:  h⁰ = 1, h¹ = 5
      m=8:  h⁰ = 0, h¹ = 2   (the full-E₆ chiral bend)
      m=11: h⁰ = 1, h¹ = 5

  Consequences re-confirmed: at the chiral bends Λ³H¹ = 0 (no 3-form
  exists — the audit's kill stands on two disjoint pipelines) and
  H⁰(D;27) = 0 (no global invariant section). The bends' peripherality
  (step7's banked dial-slot facts) verified in-run: every bend
  preserves both peripheral gates.
- Two of the three coordinated pipelines now agree everywhere; cc2's
  cell-3a (the matched-pair route) is the third — adjudication row
  open until it lands.

## Part 2 (queued; the wakeup carries it)

The alternating cubic 3-form Λ³H¹(D;27) → ℂ at the five h¹ = 5 doubles
(10 components each) — requires the degree-3 evaluation machinery on
the closed amalgam (the derivation gate: a partial free resolution to
degree 3 or the M–V localization formula, validated on the trivial-
coefficient control before the 27 runs). The honest-kill and discovery
branches are locked in the prereg.

## Lock

tests/test_b637_part1.py: fast (prereg hash; the banked table lines;
the prediction arithmetic), OA_SLOW (the full rerun).

---

## Part 2a (2026-07-15, same arc): ALL FOUR D₄ GLUINGS ARE COMPATIBLE — four more h¹ = 5 doubles

The four B605 orientation-reversing families (two glides, two order-4),
each with its banked exact SL(2,K) intertwiner, lifted through the
principal embedding (the p = 0 Bruhat corner handled via the Weyl
element; signs die on the 27 — all principal weights even):

- **Every family passes BOTH peripheral gates exactly in GL(27)**
  (μ-gate and λ-gate: ρ(x) = side₂(φ(x)) for x = a and the certified
  longitude) — the banked 27 local system GLUES through all four
  involutions (contrast: the −A₁ weld is incompatible, B635).
- **All four doubles D_φ(M): h⁰(D;27) = 1, h¹(D;27) = 5** (trivial
  controls b₁(D_φ) = 1 each). With part 1's weld doubles, the h¹
  jump locus now reads: h¹ = 5 on the conjugation weld (unbent and
  odd-bent m ∈ {1,5,7,11}) AND on all four involution gluings;
  h¹ = 2 exactly at the full-E₆ chiral bends m = 4, 8.
- NINE compatible doubles total; all nine with h¹ ≥ 3 carry a
  10-dimensional Λ³H¹ — the alternating cubic 3-form's domain (part
  2b, behind the degree-3 derivation gate).

`b637_d4_gluings.py`, `part2a_output.txt`; lock extended.
