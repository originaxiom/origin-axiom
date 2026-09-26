# B1382 — THE SPIN BIT IS THE PARENT'S PIN TYPE: m004's two spin structures are exactly the pullbacks of the Gieseking manifold's Pin⁺ and Pin⁻ structures, one each — B1141's "the beat extends over exactly one spin structure" is true inside one Pin type (the one its W·W̄ = +A silently fixes: reflections lifting to involutions, Pin⁺), and R021's "one spin structure does not extend (as Pin⁻)" is the same lift seen from the other type; so the object does not assign the spin bit — it trades it for its parent's Pin type, and T-SPIN-PAYMENT's "assigned, not free" is re-graded (E1)

**Date:** 2026-09-26 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's rule, recorded the same evening —
*"our weakest spots are the cornerstone of next big breakthroughs, thats our program since day 0"* — applied to the entrance's
last fragile axiom, orientation (OPEN_LEADS sL-3, piece (ii): what the parent carries that the child cannot see); and the
residual B1175 queued on 2026-08-27 and nobody ran: identify codex R021's Pin⁻ image with B1141's beat-selected lift ("needs a
tangent-frame Pin⁻ lift + the holonomy-convention comparison") · **Status:** PROVED (exact over ℚ(ω), two seconds) ·
CORRECTION OF RECORD (T-SPIN-PAYMENT's reading; E1) · **Fence:** mathematics of spin and Pin structures; the physics dictionary
in §4 is cited and flagged, not derived · **Price:** the freedom ledger's spin bit goes back from 0 to 1 (relocated to the
parent's Pin type) — 0 of 19 unchanged · **Numbering:** B1382.

## 0. Seen from above

B1141 (2026-08-25, hostile-verified two-bench) took the freedom ledger's last free discrete bit — the choice between m004's two
SL(2, ℂ) lifts, its two spin structures — and showed that the Gieseking "beat" (the free orientation-reversing deck whose
quotient is the Gieseking manifold) extends over exactly one of them: the beat's intertwiner is one-dimensional, and the other
lift would need (λW₀)·conj(λW₀) = |λ|²A to equal −A. It concluded: the bit is **assigned, not free**. Two days later B1175
harvested codex R021 — the Gieseking's Pin⁻ structures all restrict to one spin structure of m004, "one of m004's spin structures
does not extend" — and recorded, with codex's own fence, that this "does not yet identify the constant image with B1141's
beat-selected sign lift", queuing the comparison. It was never run. It is run here, and it changes the reading.

## 1. Computed (`verification/pin_types.py`, exact arithmetic in ℚ(ω), ω² + ω + 1 = 0; record `pin_types_run.txt`)

The two double covers of Isom(H³) = PSL(2, ℂ) ⋊ ⟨c⟩ (c = complex conjugation, orientation-reversing):
G_ε = {(M, k) : M ∈ SL(2, ℂ), k ∈ {0, 1}}, (M₁, k₁)(M₂, k₂) = (M₁·conj^{k₁}(M₂)·ε^{k₁k₂}, k₁ + k₂), ε = ±1.

| | item | result |
|---|---|---|
| S1 | B1141's holonomy A = [[1,1],[0,1]], B = [[1,0],[−ω,1]]; relator `abABaBAbaB`; the beat a ↦ a, b ↦ b⁻¹aba⁻¹b | relator census R(±A, ±B) = +I, +I (equal signs), −I, −I (mixed) — the two lifts (A, B) and (−A, −B); the beat respects the relator; beat² = conjugation by a; word-length parity preserved |
| S2 | the intertwiner W·conj(g)·W⁻¹ = ρ(beat g) | exactly one-dimensional over ℚ(ω) (exact rank 3): **W = [[1, −ω], [0, 1]], det 1, W·W̄ = +A** — B1141's W₀ reproduced |
| S3 | the covers G_ε | associative, −I central; **a reflection through the point j lifts with square ε** (c itself and z ↦ ω²z̄ both checked) — so G_ε restricted to a point stabiliser O(3) is **Pin^ε(3)**: Pin⁺ = reflections lift to involutions (obstruction w₂), Pin⁻ = to elements of order 4 (obstruction w₂ + w₁²). Since the frame bundle of N = Γ\H³ is Γ\Isom(H³), a Pin^ε structure on N is a lift of Γ to G_ε — **this is the tangent-frame reading B1175 asked for** |
| S4 | **the table**: which spin lift extends (t ↦ (±W, c); t a t⁻¹ = a, t b t⁻¹ = beat(b), relator, t² = a) | **B1141's lift (a ↦ +A): into G₊ (Pin⁺) EXTENDS, into G₋ (Pin⁻) does not. The other lift (a ↦ −A): into G₊ does not, into G₋ (Pin⁻) EXTENDS.** The three conjugation-type relations hold in all four cases; only the square t² = a discriminates: (λW, c)² = (ε|λ|²·W·W̄, 0) = (ε·A, 0) must equal (±A, 0) |
| S5 | the Gieseking manifold's topology | H₁ = ℤ (and H₁(m004) = ℤ); χ(core) = ½χ(Klein-bottle cusp) = 0 ⇒ dim H₂(N; ℤ/2) = 0 ⇒ w₂ = w₁² = 0: **two Pin⁺ and two Pin⁻ structures**, each type a torsor over H¹(N; ℤ/2) = ℤ/2; p* = 0 on H¹(−; ℤ/2) (a = b = 2t, R021), so each type restricts to a single spin structure — and S4 shows the two images differ |
| S6 | the two lifts by their cusp traces (meridian a; longitude `bABaaBAb`, found by search) | B1141's lift: (tr μ, tr λ) = **(2, −2)** — B921-6's ρ₁; the other: **(−2, −2)** — ρ₂ |

## 2. The theorem

**Theorem.** Let N be the Gieseking manifold and p: m004 → N its orientation double cover. Both Pin types exist on N, two
structures each, and pullback identifies them with m004's two spin structures: **the Pin⁺ structures pull back to ρ₁ (tr μ = +2,
B1141's lift) and the Pin⁻ structures to ρ₂ (tr μ = −2).** Neither spin structure extends as both types.

*Proof.* Existence and count: S5. Pullback constant on each type: p* = 0 on H¹(−; ℤ/2). Which: a Pin^ε structure is a lift of
π₁(N) = ⟨π₁(m004), t | t g t⁻¹ = beat(g), t² = a⟩ to G_ε; the lift of t is (λW, c) with W the unique intertwiner (S2) and λ² = 1
(det 1); the relations t a t⁻¹ = a and t b t⁻¹ = beat(b) hold for either sign of the lift of π₁(m004) because the beat preserves
word-length parity; the relation t² = a reads ε·A = σ·A for the lift a ↦ σA — so σ = ε. ∎ (Equivalently, by counting: each
τ-invariant spin structure carries exactly two lifts ±τ̃ of the deck, of one square; four Pin structures in two types force the
two spin structures to carry opposite types.)

## 3. What this changes in the record

1. **T-SPIN-PAYMENT is re-graded (E1, a sign chosen implicitly and read as forced).** B1141's computation stands to the digit.
   Its reading does not: writing the self-consistency as W·W̄ = +(lift of t²) *is* the choice ĉ² = +1, i.e. Pin⁺. Allow the other
   double cover and the other spin structure extends. **The object does not assign the spin bit; it identifies it with its
   parent's Pin type** — a ℤ/2 the object does not fix. The freedom ledger's spin bit (THE_ROAD's "priced 1 bit → 0") is back to
   **1 bit, relocated** from "which lift" to "which Pin type".
2. **R021 and B1141 reconciled.** R021's "one of m004's spin structures does not extend to the Gieseking" is B1141's own
   selected lift (ρ₁), which does not extend *as Pin⁻*; R021's constant Pin⁻ image is ρ₂. The two were never in conflict and were
   never the same statement: they select opposite lifts because they fix opposite Pin types. B1175's queued residual is closed.
3. **T-SP2-SEAT** (SP-2: the beat closes on the fermion-capable 27 "over the selected lift") inherits the re-grading: its lift is
   selected given Pin⁺.

## 4. The physics reading — cited and flagged, not derived

In the standard dictionary for putting fermions on unorientable manifolds (Witten, *Fermion path integrals and topological
phases*, Rev. Mod. Phys. 88 (2016); Kapustin–Thorngren–Turzillo–Wang, JHEP 2015), a theory whose time reversal satisfies
**T² = (−1)^F lives on Pin⁺ manifolds**, and T² = 1 on Pin⁻ — the 3+1-dimensional class-DIII topological superconductor is
classified by Ω₄^{Pin⁺} = ℤ/16. So **the lift B1141 selected is the one Kramers fermions — T² = (−1)^F, the Standard Model's —
would require**, *if* the Gieseking manifold's orientation reversal is read as the Euclidean reflection that continues to time
reversal (N × ℝ inherits the Pin type of N). That identification is the unproved step, and sign conventions for Pin± differ
between communities (here: Pin⁺ = reflections lift to involutions, the convention with obstruction w₂). What the reading would
say, if it holds: the spin bit is not free and not the object's — it is **bought by the physical fact that fermions are
Kramers**, through the parent. That is the sL-3 door this arc opens, not a result it claims.

> **Qualified 2026-09-26 (B1383; E1).** The reading above holds in one role of the deck only — the parent itself a background ("N × ℝ inherits the Pin type of N" fixed that role silently). Where the deck is instead part of the 4d CP/T on the oriented carrier, the same dictionary selects the *other* lift ρ₂; on B1104's mapping torus the lift is tied to the double tick's periodicity. And "T² = (−1)^F, the Standard Model's" asserted a T the SM does not have (J ≠ 0): the correct statement is that the SM's CP, whenever it is a (gauged, spontaneously broken) symmetry, is Pin⁺ — forced by three generations. The Pin type is thereby bought by physics; the spin bit now sits in the deck's role. `frontier/B1383_the_spin_bit_is_the_square_of_the_deck`.

## 5. For main (relayed, not applied)

B1141, T-SPIN-PAYMENT, T-SP2-SEAT and the freedom-ledger count (THE_ROAD's "1 bit → 0") need the qualifier "given the Pin⁺
convention"; B1175's residual can be closed with S3–S4 here; and the paper, wherever it says the spin structure is selected by
the object, should say it is identified with the parent's Pin type.

## 6. Caveats

The computation is exact (ℚ(ω)); SnapPy is used only for H₁ and the orientation cover. The identification of G_ε with the
tangent-frame Pin^ε uses the standard fact that Isom(H³) acts simply transitively on orthonormal frames, so Fr(N) = Γ\Isom(H³);
the Pin± naming follows the convention stated in S3. Nothing here touches the spin structures' other banked properties (B921-6's
Dirac-spectrum distinction, T-LIFTBIT's pair-invisibility). The physics dictionary in §4 is cited, with its identification step
open. 0 of 19.

## Verification

`verification/pin_types.py` (S1–S6, two seconds). Lock: `tests/test_b1382_the_spin_bit_is_the_parents_pin_type.py`.

**Sources.** B1141 (T-SPIN-PAYMENT), B1145 (T-SP2-SEAT), B1175 (codex R021 and the queued residual), B921-6 (ρ₁, ρ₂), B1234,
B1380 (orientation as the last fragile axiom), OPEN_LEADS sL-3; Kirby–Taylor, *Pin structures on low-dimensional manifolds*
(1990); Witten (2016); Kapustin–Thorngren–Turzillo–Wang (2015).
