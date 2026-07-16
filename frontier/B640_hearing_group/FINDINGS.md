# B640 — THE HEARING-GROUP THEOREM VERIFIED (with two scope corrections)

**Date: 2026-07-16. Prereg 3e000b72 (sealed first). Chat-2's handoff
verified on banked machinery (B629's 80-dps stage builder; residuals
~1e-61). Mathematics only. Chat-2 credited; their two self-caught
corrections recorded; two further scope corrections found here.**

## CONFIRMED (the theorem, parts I–V — at class-table strength)

- **The mechanism:** the θ-odd plane is invariant under the untwisted
  weld letters (residuals 1e-61); C|odd = −I exactly, so
  M_odd = −ρ with ρ a genuine 2-dim unitary rep.
- **The group:** |im ρ| = 360; det ρ = ω^{#L−#R mod 3} (0/60 failures);
  |ker det| = 120 with the EXACT 2I order profile
  {1:1, 2:1, 3:20, 4:30, 5:24, 6:20, 10:24} and unique involution;
  **the conjugacy-class equation [1,1,12,12,12,12,20,20,30] = SL(2,5)
  exactly** (the class-table-level check this seat added);
  im ρ ≅ 2I × ℤ/3.
- **The golden character (class-level):** the histogram
  {+2:1, −2:1, ±1:20 each, 0:30, ±φ:12 each, ±1/φ:12 each} — the
  2-dim golden irrep, zero unidentified traces.
- **The headline: tr ρ(RL) = −1/φ** (45+ digits; = the banked
  B584/B587 value — the hearing character of the monodromy).
- **THE ORDER RECONCILIATION (retires the apparent B619 conflict):**
  ord(ρ(R)) = ord(ρ(L)) = ord(T) = 15; ord(ρ(RL)) = 10 (= B584's
  banked rotation); ord(M_odd(RL)) = 5 (= B601's B_odd);
  **ord(W(RL)) on the FULL 6-dim stage = 20 (= B619's banked "ord =
  20")** — four banked/claimed orders, four distinct operators, all
  correct simultaneously.
- **The silent witnesses:** LLRLRR, LLRRLR, LRLLRR all tone-zero; the
  real-ear amplitudes have Re ≈ 1e-61 (purely imaginary, as the
  prediction class demands; LLRLRR is fully silent for the test ear).
- **The hyperbolic-heard-as-elliptic principle stands:** the Anosov
  monodromy's hearing is the order-10/order-5 pentagon rotation.

## CORRECTED (parts VI–VII: the tone law's scope)

**The scalar-symmetric-part law is NOT universal over the 360:** it
FAILS on 232/360 elements. Under the strict law (Sym Re M_odd = c·I),
the conforming set is ≈ the det = 1 sector, with **9 distinct tones
(all in the golden set, 9/9 identified) and 34 silences** — not the
handoff's 16 tones / 90 silences, which mixed a different per-element
tone definition into the twisted sectors. The correct twisted-sector
tone statement is a registered refinement for chat-2 (the det = ω^{±1}
sectors need their own law; the halved-cosine claim is plausible but
not what the symmetric-part law gives). The witnesses and the
prediction class SURVIVE (they are det = 1).

## The citation (R7)

**Ng–Schauenburg** (the congruence-subgroup theorem for modular
categories: the kernel of the modular SL(2,ℤ)-representation is a
congruence subgroup of level N = ord(T)) — [CITED-KNOWN], with the
projective-vs-linear caveat. Here ord(T) = 15 exactly, and the image
structure fits the factorization through SL(2,ℤ/15) ≅ SL(2,3)×SL(2,5):
2I = SL(2,5) faithful, the SL(2,3) factor collapsing to its
abelianization ℤ/3 = the det/twist — |image| = 360 = 120·3 consistent
with |SL(2,15)| = 2880 (index 8 = the collapsed SL(2,3)-part).

## The McKay placement (registered, not banked as derivation)

2I is E₈'s McKay partner; the banked two-ended theorem (B247–B261)
gives the placement candidate: the holonomy lives at the E₆/ℚ(√−3)
end, the HEARING GROUP is the finite shadow of the E₈/ℚ(√5) end —
(what the object is, how it is heard) = (E₆-end, McKay-E₈-shadow).
Registered as a lead; a derivation would need the two-ends machinery
to produce 2I structurally, not by coincidence of golden objects.

## The instrument note

The first run used float64 stage matrices inside 60-digit arithmetic
and produced garbage (2044 pseudo-elements) — caught immediately by
the gates (the profile check failed); rewired to the banked 80-dps
builder. Controls before values, once again.
