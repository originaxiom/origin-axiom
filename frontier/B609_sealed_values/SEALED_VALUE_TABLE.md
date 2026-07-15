# B609 — THE SEALED VALUE TABLE (Phase 2 of the Listening Campaign)

**Computed under the sealed prereg (sha256 0bcc2ad4…, #979). Every
Phase-2 value is in this file; its SHA-256 enters the hash ledger in the
same bank. NO comparison to any measured quantity has been computed;
Branch 3 requires its own seal + the seat-4-approved null model.**

## E1 — the Killing-class mixing fractions (exact rationals; full table in `e1_output.txt`)

Block V(m=4): wt+8: {(0,0,1): 1/4, (0,1,1): 1/4, (1,0,1): 1/4, (1,1,1): 1/4}
· wt+6: {(0,0,1): 1/10, (0,1,1): 4/5, (1,0,1): 1/10}
· wt+4: {(0,0,1): 4/13, (1,0,0): 9/26, su3: 9/26}
· wt+2: {(1,0,0): 25/58, su2: 2/29, su3: 1/2}

Block V(m=8): wt+16: {(1,1,2): 1} · wt+14: {(0,1,2): 1/2, (1,1,2): 1/2}
· wt+12: {(0,1,2): 1/2, (1,1,2): 1/2} · wt+10: {(0,1,1): 1/2, (1,1,1): 1/2}
· wt+8: {(0,0,1): 121/692, (0,1,1): 225/692, (1,0,1): 121/692, (1,1,1): 225/692}
· wt+6: {(0,0,1): 121/274, (0,1,1): 16/137, (1,0,1): 121/274}
· wt+4: {(0,0,1): 16/65, (1,0,0): 49/130, su3: 49/130}
· wt+2: {(1,0,0): 9/50, su2: 8/25, su3: 1/2}

Gates: E1-a (all lines sum to 1) PASS; E1-b (the tip pure (1,1,2)) PASS.

## E2 — the amplitude components (declared bookkeeping: amplitude × the responding line's fractions)

The responding lines are the bending tops: V₄'s wt+8 and V₈'s wt+16.
- c₄ = N₄(1+√−3): components N₄(1+√−3)/4 in EACH of (0,0,1), (0,1,1),
  (1,0,1), (1,1,1).
- c₈ = N₈(1−√−3): the single component N₈(1−√−3) in (1,1,2).
- h₃ (golden, via the sealed bijection m=4↔u₃): h₃/4 per the same four
  classes; h₆ (m=8↔u₆): h₆ in (1,1,2).
- The E₆₂ amplitudes: no channel↔line map was ever sealed beyond golden;
  recorded as bookkeeping under BOTH candidate assignments (each
  amplitude × the m=4 quarters, and × the m=8 tip), with the rank-1
  third channel UNMAPPED (outcome B).

## E3 — the spectral hearing amplitudes (full listing in `e3_output.txt`)

GATES (pre-determined, all green): κ=4: dim 1, amplitude −1 exactly, REAL
(the unit tone is chirality-deaf); κ=5, 10: traces 1/φ, spectra
conjugation-closed; κ=7, 13: traces 0 (the trace law).

THE NEW VALUES:
- **κ=7 (dim 6):** char poly = λ⁶+λ⁴+λ²+1 = (λ²+1)(λ⁴+1) (coefficients
  integer to 1e-9): the spectrum is the 8th roots of unity minus ±1:
  {±i, e^{±iπ/4}, e^{±3iπ/4}}, each simple.
- **κ=13 (dim 30):** all-integer palindromic char poly (coefficients
  1,0,1,0,0,0,0,−2,0,−2,…,1 to 1e-9); all 30 eigenvalues on 28th-root
  angles (multiples of π/14, none at ±1), multiplicities 1–2;
  conjugation-closed.

## E4 — the extended norm table

- Every new κ=7 and κ=13 eigenvalue: |λ|² = 1 (to 1e-9; the integer
  char polys support exact roots of unity — best-effort tier per the
  prereg).
- PRE-SEALED anchors restated: N(h₃) = 1/5 (golden), ∏|amp|² = 1/49
  (E₆₂); minpoly(h₃) = 5x⁴+5x³+1.

## Exploratory observations (NO Phase-2 status; no verdict weight)

1. **Finite-order off golden:** the odd hearing form appears to be
   finite-order (roots of unity, |λ| = 1) at κ = 4, 7, 13 and NON-unitary
   exactly at the golden multiples (|h₃|² = (5−√5)/10 ≠ 1 at κ=5) — the
   chirality with magnitude lives only where the golden trace fires.
   Law-candidate for a future prereg'd cell (κ ∈ 8, 9, 11, 12 scan).
2. **The half-su(3) shallow lines:** both blocks' wt+2 lines carry
   EXACTLY 1/2 on su(3)-roots. The V₄ top is EXACTLY uniform (1/4 × 4).
3. The κ=7 spectrum order (8 = κ+1) and the κ=13 angle grid (28 = 2(κ+1))
   suggest a 2(κ+1)-clock — B596-adjacent, unexplored.
