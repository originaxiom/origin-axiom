# FINDINGS — the register test (PREREG sha256 85df26a8…, sealed before computing)
web seat (chat1), 2026-10-06. Frame: F-MC entrance (the 2T door). Objects: m000, m004, m004's levels M1–M4.
Reach: single (two states). Nothing to CLAIMS; Gate 5 untouched.

## Seen first (record sweep)
B1234 (squaring ⇒ orientation double cover ⇒ amphichiral ⇒ the eight walls; 48 = 48 surjections; open question: does
dropping the squaring break the tools?), B469 (the orientation character as "the residue"; BR2 family Gieseking theorem),
B605, 28dbd73f (every orientation double cover amphichiral, 250/250), sm:B1382/sm:B1383 (spin bit = the parent's Pin type,
then the deck's role), B868 (θ linear vs c antilinear), GENESIS v1.11 §3–§5, FK2, FK12.

## Results
| | prediction | outcome |
|---|---|---|
| P1 | m000's k-cover orientable iff k even; 2n-cover ≅ M_n; torsion = abs(1 − tr((LP)^k) + (−1)^k) | **PASS**, k = 1…8. Even levels are m004, M2, M3, M4. Odd levels (non-orientable, never computed) have torsion 1, 4, 11, 29; level 3 is Z/2 + Z/2 + Z. |
| P2a | 48 surjections onto 2T on m000, on ker w (Reidemeister–Schreier), on m004 | **PASS**: 48 / 48 / 48 |
| P2b | restriction 2-to-1, fibres {ρ, ρ⊗w}; exactly 24 of m004's extend | **PASS** |
| P2c | the non-extendable 24: deck = the OUTER automorphism (ω ↔ ω̄) | **KILLED: 0 of 24.** The registered alternative holds in **24 of 24**: the deck is inner-conjugate, and the extension is blocked only by a central sign, A² = −ψ(t²). |
| P3 | Shapiro: dim H¹(m004;V) = dim H¹(m000;V) + dim H¹(m000;V⊗w) | **PASS**, all 48 give (0,0,0); controls non-vacuous (trivial V: 2,0,2; unipotent V: 1,0,1). |

## Exploratory (NOT sealed — re-seal before banking)
m004's single Z/2 character χ (which separates its two spin structures, sm:B1382) moves every one of the 48 to the other half:
**the sign obstruction on the 2T door is the spin bit.** Half of m004's door descends to m000 as a 2T representation, half
only with a central twist (into SL(2,3)·⟨i⟩ ⊂ GL(2,F9)), exchanged by χ — B1382's Pin pattern, found independently at the
arithmetic entrance. Which half is the Pin⁺ one is not determined here.

## What it means, at its scope
- On this frame and these two states, **m004 = m000 + one bit, exactly**, and the bit appears as a central sign, not as a
  Galois swap. The register does not touch the field arithmetic: no ω ↔ ω̄ anywhere. Consistent with B1234 cell 3 (the route
  to E6 does not need the squaring) and with FK12's "two signs, not one" (the register is not c, the antilinear bit).
- B1234's open question, on this frame: **dropping the squaring does not break the tools** — Reidemeister–Schreier, Fox calculus
  and the 2T door all run on m000 with the orientation twist w.
- The prediction that would have made the register a Galois/chirality selector failed. Recorded as a kill.

## Next, each to be sealed first
1. Seal and re-run the exploratory spin-bit identification; decide which half is Pin⁺ against sm:B1382's cusp-trace lifts.
2. m000's odd levels (non-orientable, torsion 1, 4, 11, 29) in the class-index frame — never computed.
3. The same test on the metallic parents LᵐP (B469 BR2), for the base rate.

---
# ADDENDUM — PREREG 2 (sha256 34082da5…, sealed before computing)
| | prediction | outcome |
|---|---|---|
| R1 | P2 with the other transversal (t = b): 24 / 24 / 0, and m004's Z/2 character swaps 48 of 48 | **PASS.** The spin-bit identification is now SEALED, not exploratory: on the 2T door the register's sign obstruction is the spin bit. |
| R2 | the deck acts as complex conjugation c (ρ∘τ ≅ ρ̄): invisible at the ramified prime 3, Frobenius at inert primes, swap at split primes | **PASS** at all 11 primes ≤ 31 on Riley's exact representation (relation exact over Z[ω] and mod every p; controls: tr(xy) = 2 − ω ∉ Z). |
| R3 | the paper's Scope 7.2: no surjection onto A5 | **CONFIRMED**: 0 by enumeration; Riley mod 2 has image of order 10 in SL(2,F4) ≅ A5 — dihedral, the Fox 5-colouring (knot determinant 5). |

## What it means
- **The measurer's bit is complex conjugation c**, the generator of Gal(ℚ(√−3)/ℚ) — the "Galois sheet" GENESIS §7 already names
  among the closings. Prime by prime it acts by the textbook decomposition-group law.
- **The E6 door sits at the one prime where c is invisible on the residue field.** That is why P2c's Galois-swap prediction
  died, why only a central sign survives at the door, and why B1234 cell 3 holds (the arithmetic route to E6 does not need
  the squaring): the 2T door cannot see the register.
- **Correction of PREREG-1 FINDINGS and of the web seat's message of 2026-10-06 16:00:** "the register is not c" and "it adds a
  sign, not a hand" were drawn from the ramified prime alone. Globally the register is c; at the door it reduces to the sign.

## Scope and genericity (GENESIS §6)
frame: F-MC entrance and its prime-by-prime analogues; object: m004 / m000; reach: single. The prime law is GENERIC — it holds
for any arithmetic manifold over an imaginary quadratic field with an orientation-reversing isometry. What is specific is only
that the root's door is at its field's unique ramified prime (F-MC's own premise). Nothing here selects a hand: c is seen,
not chosen.
