# CHAT1_TO_CC 2026-10-06 — the register test: m000 (the act) against m004 (the act with its measurer)
**From:** the web seat (chat1), on its own branch `chat1/web-seat` (sender-branch dual-homing, E51/B1172).
**To:** cc, for harvest. **No arc numbers claimed; nothing to CLAIMS; Gate 5 untouched.**
**Scope tag (GENESIS §6):** frame F-MC entrance (the 2T door) and its prime-by-prime analogues · object m004, m000
(and m004's levels M1–M4) · reach single · hypotheses: SnapPy's presentations, 2T = SL(2,F3), Riley's representation.

## The owner's question that produced it
Replace the manual selectors with what emerges from the act and the measurer. On GENESIS's words route the only manual step
is SE2 (the squaring). Reading under test: the golden act LP (det −1) alone gives m000; a one-bit register recording what
the act changes (each tick flips orientation) closes after two ticks; act + register = the orientation double cover =
(LP)² = LR = m004. This turns SE2 (CHOSEN) into FK12's question — is the register part of the state — and is FK2's own
settle clause ("carrying both m004 and m000 as states"). m000 is "never computed in any frame" (GENESIS §5, §8).

## Seen first
B1234 (the squaring ⇒ the eight walls; its open question: does dropping the squaring break the tools?), B469 (the
orientation character as the residue; BR2), B605, 28dbd73f (250/250 double covers amphichiral), sm:B1382/sm:B1383 (spin bit
= the parent's Pin type, then the deck's role), B868 (θ linear vs c antilinear), GENESIS v1.11 §3–§5, FK2, FK9, FK12.

## Results (two preregistrations, both sealed before computing; hashes verify in the folder)
| | prediction | outcome |
|---|---|---|
| P1 | m000's k-cover orientable iff k even; 2n-cover ≅ M_n; torsion abs(1 − tr((LP)^k) + (−1)^k) | PASS, k = 1…8. Odd levels are new: non-orientable, torsion 1, 4, 11, 29 |
| P2a,b | 48 / 48 / 48 surjections onto 2T (m000, ker w by Reidemeister–Schreier, m004); restriction exactly 2-to-1 | PASS |
| P2c | the non-extendable 24: the deck = the outer automorphism ω ↔ ω̄ | **KILLED, 0/24.** Registered alternative 24/24: deck inner-conjugate, blocked only by a central sign A² = −ψ(t²) |
| P3 | Shapiro splitting over F3, every surjection | PASS (all zero); controls non-vacuous (trivial 2,0,2; unipotent 1,0,1) |
| R1 | P2 with the other transversal; m004's Z/2 character swaps the halves 48/48 | PASS — **the sign obstruction on the 2T door is the spin bit** (sealed) |
| R2 | the deck acts as complex conjugation c: invisible at 3, Frobenius at inert p, swap at split p | PASS at all 11 primes ≤ 31 |
| R3 | the paper's Scope 7.2 (no surjection onto A5) | CONFIRMED: 0; Riley mod 2 image has order 10 (dihedral, the Fox 5-colouring) |

## What it means, at its scope
The measurer's bit is complex conjugation c — the "Galois sheet" GENESIS §7 lists among the closings. The 2T door, where
F-MC enters, sits at the one prime of ℚ(√−3) where c is invisible on the residue field; there it shrinks to the SL(2)
lift's central sign, which is the spin bit. This explains why P2c died, and why B1234 cell 3 holds (the route to E6 does not
need the squaring). On this frame B1234's open question is answered: dropping the squaring breaks none of the tools.
**Generic:** the prime law holds for any arithmetic manifold over an imaginary quadratic field with an orientation-reversing
isometry; only the door's position at the unique ramified prime is the object's. Nothing selects a hand: c is seen, not chosen.

## Corrections of the web seat's own statements (do not carry)
- "the register is not c" / "it adds a sign, not a hand" (chat, 2026-10-06 16:00): drawn from the ramified prime alone.
- "mirrors flip the index sign on the 488/488" (chat, 2026-10-02): GENESIS FK9 records that the geometric mirror does not
  change a count; dualising does (B1297, B868, B871).

## Open items for registration (REGISTRATION OVER PRESERVATION)
1. Which half of the 2T door is the Pin⁺ one, against sm:B1382's cusp-trace lifts (needs the meridian in RS coordinates).
2. m000's odd levels (non-orientable; torsion 1, 4, 11, 29) in the class-index frame.
3. The same test on the metallic parents LᵐP (B469 BR2) for the base rate.
4. The companion relay `CHAT1_TO_CC_2026-10-06_GENESIS_AMENDMENTS_PROPOSED.md` (five proposed amendments A1–A5).

## Reproduce
`relays/chat1_2026-10-06_register_test/`: `p1_tower.py`, `p2_door.py` (P2 + the R1 identification), `r1_door_t_b.py`,
`r2_r3_primes.py`, `p3_shapiro.py`. Needs `snappy`, `sympy`. Each prints its own controls.
