# W30 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed (most
were seen in the plan review). Nothing here is a result.

## Why this route

- **Step 4 of the owner's approved plan:** is an order-3 (qutrit) flux forced on the shared fibre?
- **Why it matters.**
  - Main's grade (GENESIS v1.28, S86) names what would finish the derivation: a forced complex structure on the gauge
    side, a bundle whose holonomy has complex representations.
  - The qubit's flux −1 is its own inverse. A qutrit flux ω is not.
  - W29 showed what a chosen ℤ₆ flux gives: an echo, not a derivation. This arc asks the prior question, whether
    anything forces the order-3 part at all.

## Weave or thread?

- **Weave-type.** Every cell takes all the moves together (L, R, the sign −I and the swap P, each named) on the shared
  fibre's own representations. The claims are about the common point, which every thread shares.
- **The rank-3 object is the question, not an input.** Whether the principle allows or forces it is what is read.

## The objects

- **The forced point:** a ↦ iZ, b ↦ iY (W2, W28). Its puncture [a, b] ↦ −1.
- **The qutrit pair:** A = C₃ = diag(1, ω, ω²) and B = S₃, the cyclic shift |k⟩ ↦ |k + 1⟩, with ω = e^{2πi/3}.
  - det A = det B = 1, so no scaling is needed (unlike W29's N = 6).
  - ABA⁻¹B⁻¹ = ω·1.
- **The moves on pairs:**
  - L: (A, B) ↦ (A, AB);
  - R: (A, B) ↦ (AB, B);
  - −I: (A, B) ↦ (A⁻¹, B⁻¹);
  - P: (A, B) ↦ (B, A);
  - P∘K: the swap with complex conjugation, (A, B) ↦ (B̄, Ā).
- **A move keeps a pair's class** when the intertwiner space {U : U A = φ(A) U, U B = φ(B) U} is non-zero.
- **The convention for "the moves"** (from W29's post hoc P3): the grammar's moves are L and R (GENESIS GM2). The sign
  (GENESIS GM5b, FK4) and the swap (GENESIS GM5c, FK3) are forks, and each is reported as its own cell.

## The cells

The script is `the_order_three_flux.py`, writing `.json` beside it.

- **Q1, the lemma (PROVED; a check of the code, which cannot fail).**
  - The forced point sends [a, b] to −1, of order 2. A homomorphism cannot raise an element's order, so in every
    representation of the forced point the puncture's holonomy has order at most 2.
  - The check: Sym^n ρ_Q for n = 0, …, 8, and χ_p ⊗ Sym^n for the three parities, send [a, b] to (−1)^n·1.
  - So no order-3 flux comes from the forced rank-2 data, by any construction from its representations.
- **Q2, the qutrit pairs (PROVED; checked).**
  - Pairs in SU(3) with commutator ω·1 form exactly one conjugacy class. A³ commutes with the irreducible pair, so it
    is scalar, and det 1 forces A³ = 1. The same holds for B.
  - Each of the nine centre twists (ω^i A, ω^j B) is conjugate to (A, B): intertwiner dimension 1.
- **Q3, the moves on the qutrit class (computed; the substantive cell).** For each of the nine twists:
  - L, R and −I keep the class: dimension 1, 27 cases.
  - The swap P sends it to the ω̄ class: dimension 0.
  - P∘K keeps it: dimension 1.
  - For contrast, on the qubit point P keeps the class (dimension 1), since −1 = (−1)⁻¹.
  - **The reading.** Under W2's definition (the common point is fixed by every move, the swap included), the qutrit
    point is a common point only if the swap is not a move, or acts with complex conjugation, the C-type bit (GENESIS
    GM5c, FK3; B1083).
- **Q4, the cusp condition in rank 3 (STATED as a choice).**
  - GENESIS GM4 makes the puncture parabolic. ω·1 is central, not parabolic, so the rank-2 condition has no rank-3
    form.
  - This arc uses "the puncture's holonomy is central" as the stand-in. It is a choice, stated here.
- **Q5, the moves on the qutrit's ℂ³ (computed).**
  - The lifts of L and R (normalised to det 1) have a projective image of order 24 (SL(2, 𝔽₃) ≅ 2T) and commutant 2,
    split 2 ⊕ 1.
  - The lift of (LR⁻¹L)² is a reflection, k ↦ 2 − k up to phases. The bare −I's lift is k ↦ −k.
  - With the bare −I added, the commutant is 1.
- **Q6, the record's order-3 structures (re-read; no new data).**
  - The odd-trace extension 2T is a thread object (W25), and its 3-cycle orientation flips at every tick (W26).
  - Mod 3 the fibre's puncture goes to −1; the order-3 part sits on the meridian, the thread's tick (sm:B1536's
    preregistration; B284; main's B1601).
  - B1280 (PROVED): order-3 central twists on the stable letter give N = 0.
  - B955 (π₁(m004) never maps onto 3^{1+2}) is a knot-group fact, H₁ = ℤ. The fibre has H₁ = ℤ², so B955 does not
    speak to it.
- **Q7, the verdict.**
  - An order-3 flux is **not forced.**
    - The forced data cannot produce one (Q1).
    - The rank-3 point exists and the grammar's moves keep it, but the swap sends it to its conjugate (Q3). So it is a
      common point only on one branch of the swap's fork (GENESIS GM5c, FK3).
    - Its cusp condition is a choice (Q4).
    - The record's order-3 structures live on threads or on the meridian (Q6).
  - **Allowed on a fork, not forced.**

## What each outcome means

- **As stated.** Step 4 closes. The qutrit flux the contemplation proposed is not forced by the principle. It would
  need the swap's fork resolved one way (not a move, or acting with conjugation) and a stated cusp condition in rank 3.
  Main's finishing condition (a forced complex structure on the gauge side) is not met this way.
- **Q3 different** (P keeps the class, or L or R does not). Then the swap's role changes, and the verdict is re-read
  before anything is written.
- **Q5's projective order not 24, or the commutant not 2.** The moves' action on the qutrit differs from SL(2, 𝔽₃)'s
  Weil representation. Record it.

## Seen before this was written

- **The plan review (2026-10-08, computed in memory and not committed), which is why most cells carry no prior:**
  - Q2's one class, and the nine twists conjugate by CⁱSʲ;
  - Q3's dimensions (L, R and −I: 1; P: 0; P∘K: 1, for all nine);
  - Q5's order 24, split 2 + 1, and the reflections k ↦ 2 − k and k ↦ −k;
  - commutant 1 with the bare −I (projective order 216).
- **By hand:** Q1's lemma; the qubit's P (W28, I2: the lift (iZ + iY)/√2).
- **The record:** W2, W25, W26, W28 and W29 (post hoc P3); B1280; B955; B1536; B284; main's B1601 and S86.
