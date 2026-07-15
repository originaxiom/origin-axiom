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

---

## Part 2b (2026-07-15, HONEST PARTIAL — the machinery banked, the values QUARANTINED)

**The derivation gate OPENED:** the T∘H evaluation formula for the
alternating 3-form on the amalgam is derived and implemented
(`b637_threeform.py`): H³(π) ≅ coker(H²(sides) → H²(T²)) by the
graph-of-groups sequence; Y = S₁(z_T) − S₂(z_T′) with S = ω∘H₂, H the
recursive equivariant bar-vs-Fox homotopy; Ψ₂ from van Kampen
certificates (beam search + exact free-group replay verification — the
peripheral commutator has AREA 2: [λ,μ] = (u₁ r u₁⁻¹)(u₂ r⁻¹ u₂⁻¹),
`certificate.json`).

**What is VERIFIED:** δS = ω exactly on six cells including certificate
paths and peripheral cells (`part2b_stage1_output.txt`, D3); cocycle
consistency across the peripheral identification (D1); res-ω equality
across sides (D2); section independence of the assembled value (G-C).

**What FAILED — the sealed gates working as designed:** the class-level
gates (coboundary invariance in every slot, antisymmetry under
transpositions) FAIL (`part2b_stage2_output.txt`), so stage-1's
"10/10 nonzero" table is NOT class-level data and is QUARANTINED —
banked only as machinery output, carrying no mathematical claim. The
diagnostics (`b637_diag.py`, `b637_diag2.py`) localize the defect:
**δS′ = ω′ fails for coboundary-shifted cocycle inputs on the same cell
where the unshifted identity holds (E2), and the shift moves only
side-1 cells (E1)** — an input-dependent implementation defect in the
S-evaluator, not a gap in the derivation (the invariance is forced
mathematically: H²(side; ℂ) = 0 and ∂z_T ⊗ ℤ = 0). The minimal failing
case is recorded; the repair continues with it as the unit test.

**The honest state of the 3-form question:** OPEN. Existence/vanishing
of the alternating cubic on the nine h¹ = 5 doubles awaits the repaired
evaluator (or an independent second route). Nothing about the 3-form's
values is claimed. Per the sealed prereg, the outcome branches remain:
≡ 0 (the honest kill) / nonzero (a new invariant) — undecided.

---

## Part 2b RESOLVED (2026-07-15, the repair iteration): THE ALTERNATING CUBIC 3-FORM IS NONZERO — the discovery branch fires

**The repair (two real bugs, both found by formal machinery):**

1. **The Φ₂ correction-cell prefix** (`rel_chain`/`Phi2_fr`): the
   corrected relator chain's correction is −p_{i−1}·[ℓ⁻¹|ℓ] — the
   prefix BEFORE the inverse letter. My part-2b transcription used p_i
   (the prefix including it). Provable one-word bug:
   ∂([p|ℓ⁻¹] − p[ℓ⁻¹|ℓ]) = −pℓ⁻¹[ℓ] + telescope = exactly the Fox
   pattern. (B632's cell-2 cup implementation had it RIGHT — which is
   why the audit's 162-check verification passed there; the error was
   re-introduced in this arc's re-transcription.)
2. **The H₁ equivariant extension** in the literal verification machine
   (early coefficient folding vs H₁(k[w]) = k·H₁([w])).

Both were exposed by `b637_chainmachine.py` — the literal ℤΓ-chain
machine (normalized bar complex; s, ∂, Φ, Ψ as chain operations; a
GLOBAL fp-keyed section) whose formal gates now verify
**∂₃H₂ = id − Φ₂Ψ₂ − H₁∂₂ exactly on all tested cells** and full
formal δS−ω cancellation on trivial-certificate cells. (The formal
residual on certificate-bearing cells is expected — δS = ω is a
functional identity on cocycle inputs there, verified in 27-dim.)

**After the one-word fix, ALL CLASS-LEVEL GATES PASS**
(`part2b_stage2_fixed_output.txt`): coboundary invariance in all three
slots, antisymmetry under both transpositions, section independence.
Stage-1's quarantined table is confirmed as bug artifact (the old
nonzero Y[012] is truly 0).

**THE RESULT (exact, ℚ(√−3) = ℚ(ω), class-level):** the alternating
cubic 3-form Λ³H¹(D;27) → ℂ is **NONZERO on every computed
mirror-coupled double** — the sealed prereg's DISCOVERY branch:

- unbent weld: 6/10 components nonzero; m = 5, 7, 11: 6/10;
  **m = 1: 7/10** (the m=1 bend switches on Y[024]).
- **The bend-independent core:** Y[023] = −7983360/13 + 2661120/13·ω′
  and Y[123] = (221760/13)·ω′ are IDENTICAL across none/5/7/11 (ω′ the
  √−3-part unit); Y[034], Y[124] = (2/3)·ω′ at 5/7/11.
- **The bend-sensitive component:** Y[234] varies over ~20 orders of
  magnitude with the bend — the one slot that hears the dial.
- **The zero pattern:** Y[01k] = 0 for all k at none/5/7/11 — classes
  0 and 1 (the coker-δ⁰ pair) never couple jointly except under the
  m = 1 bend.

Normalization caveat (declared in the prereg): individual magnitudes
depend on the basis representatives; the invariant content is the
zero pattern, the identities across bends, and nonvanishing itself.
NO SM number appears anywhere; any physics reading of this invariant
requires L91's typed functor first (Gate 5 stands).

**Remaining for the complete Lane-3 close (queued):** the same
10-component table on the four D_φ involution doubles (their peripheral
pairs = the φ-words; fresh certificates), and cc2's cell-3a
cross-adjudication when it lands.

---

## Cross-adjudication: cc2's cell-3 packet (verified on receipt, 2026-07-15)

- **The three-pipeline agreement is complete on the plain weld double:**
  cc2's independent amalgam-Fox run (their stage 1, all gates green)
  gives h⁰(D;27) = 1, h¹(D;27) = 5 — identical to this arc's part-1
  table and the audit's reproducer. Their kernel structure (Z¹ dim 31,
  coboundary rank 26) matches ours exactly.
- **Their "h¹ = 3" belongs to a FIFTH manifold**, not a discrepancy:
  the conj∘θ-TWISTED double (glued through the amphichiral involution
  composed with the diagram involution on the representation side) —
  parity-clean structure: θ-even blocks double (h¹ = 2 each), θ-odd
  do not (1 each); h¹(D;e₆) = 10; h¹(D;27) = 3. Added to the
  TERMINOLOGY table as **D_conjθ(M)**. Their prereg self-correction
  (the two gluings had been conflated) is the same lesson as audit
  Gate 2, honestly recorded on their side.
- **The bonus identification:** every H¹ direction of the twisted
  double bends the cusp by ONE universal slope = −2√−3 = the cusp
  modulus itself — B357/B598's universal boundary ratio now has a
  geometric name (the cusp shape).
- **Their stage 2 delivers the complementary invariant on the plain
  double:** the vev-paired 5×5 class-level form — ANTISYMMETRIC (as
  the corrected typing demands), rank 4, one kernel class, exact
  ℚ(√−3) values (their blind bank). Their 2-form and this arc's
  3-form are the chord's two class-level cubic-family invariants,
  produced by independent machinery.
