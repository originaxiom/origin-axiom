# B1083 — THE ORIGIN TORSOR, TYPED CORRECTLY: the arrow was never a torsor bit

**Date:** 2026-08-19 · **Verdict: PROVED (typing correction to banked content + two new exact facts)**
**Provenance:** the outside bench's session handoff (an independent hostile-verification
session over the programme; its certificates re-ran green on this bench), item V.1/V.4/V.5;
THE CORRECTION RE-DERIVED INDEPENDENTLY on this bench with fresh code before banking
(integrate-don't-merge; verify-incoming-results).

## 1. The typing correction (amends THE FORCED AND THE FREE §0)

§0 as banked typed the founding K₄-torsor as "reversal(=arrow) + swap(=chirality)". The
outside bench caught the mislabel and this bench re-derived it from scratch:

- The four Fibonacci-type rules {a→ab, a→ba, b→ab-side variants} form ONE free transitive
  K₄-orbit under reversal-conjugation and swap-conjugation (orbit size exactly 4 — rebuilt
  here, own code).
- **Every one of the four orbit points is a FORWARD (positive) substitution.** No K₄
  element inverts the dynamics. Reversal-conjugation of a→ab, b→a gives a→ba, b→a —
  another forward rule, not an inverse. **Reversal is a PARITY bit (P-type, reading
  direction); swap is the C-type bit; THE ARROW IS NOT ON THE TORSOR AT ALL.**
- **The arrow's true home: monoid non-surjectivity.** On the positive monoid the rule is
  injective and not surjective — the word `bb` has NO preimage (verified exhaustively to
  length 8 here; `aaa` HAS one: σ(bbb)=aaa, the outside bench's own error #6, confirmed).
  Some configurations are initial-only: an intrinsic arrow, unspendable, structural.
- The corrected ledger: **two spendable bits (C, P) + one unspendable structure (T = the
  positivity of the register).** The torsor spends choices; the arrow was never a choice.

## 2. The tick (M² = RL) and the Gieseking purchase

- **det M = −1** (the Breath ℤ/2 pulse, as banked) and **M² = [[2,1],[1,1]] = RL exactly**
  — the single tick squares to the figure-eight monodromy (trace 3, t²−3t+1). Re-derived
  here, own code, exact.
- CITED (standard 3-manifold facts, not re-proved here): the one-tick mapping torus is the
  Gieseking manifold — non-orientable, one ideal tetrahedron, volume ≈ 1.0149; its
  orientation double cover is m004. **The object is the double tick.** Consequence, typed:
  on the one-tick object chirality cannot be POSED (non-orientable); the second tick buys
  orientability and pays amphichirality — the deck involution restoring orientation is the
  one that swaps the hands. **Orientability and amphichirality arrive in the same
  purchase, at tick two.**

## 3. What this corrects and what it feeds

The §0 amendment is applied in docs/THE_FORCED_AND_THE_FREE.md (dated, in place, the
original typing preserved in strikethrough context). The corrected typing feeds the
closing-inventory count (the arrow row was never a spendable closing) and the Breath
reading (det = −1 is the tick's own signature, not a torsor bit's). The recurrence of
C-like and P-like free bits at every level (frame classes, closings, hands) is inheritance
from the first act; the arrow is inherited differently — as the register's positivity,
present at every level as non-invertibility, never as a choice.

**Locks:** tests/test_b1083_origin_torsor.py (the orbit, the positivity, the bb-preimage
exhaustion, M²=RL, det −1). Certificates from the source session (origin_torsor.py 8/8,
heartbeat.py 9/9) re-ran green here; this bench's own re-derivation is the banked evidence.
