# SM-C13 — the lepton rows at level 5: what in the record's structure separates leptons from down quarks?

*Card of the SM seat, 2026-11-14, offered by main (M30) and taken. Committed and pushed, with its expectations, before
anything of it is computed. Data-free. **Only equalities and relative differences between sectors are written**: no
output of the frame (no ratio, no mixing modulus) is printed or saved, and nothing is set beside a measured number.*

## 1. The question, and what the structure says before any run

- **The degeneracy.** In the read-out on the whole (B1924, B1928, P-845), a sector's couplings are B1724's frame. A
  field of six-times-hypercharge q is twisted by q·w, where w = aτ + b is the reading line.
  - At level 5, w has order 5, so the frame sees q mod 5.
  - For the leptons, (6Y_L, 6Y_e) = (−3, 6) ≡ (2, 1). For the down quarks, (6Y_Q, 6Y_d) = (1, 2). The pair is the same
    one, swapped, so the lepton coupling is the down coupling transposed.
- **The derivation behind the card** (written before any run).
  - The transposition pairs L with d and e with Q, and 6Y_L − 6Y_d = −5 and 6Y_e − 6Y_Q = +5. Both differences are odd
    multiples of 5.
  - So any ingredient that sees q mod 2 together with q mod 5, that is q mod 10, separates the sectors. The order 5 by
    itself cannot.
  - The record already has such an ingredient. At odd ticks the frame's matter exists only twisted by the orientation
    (B1926; SM-C10): a field of charge q carries the character's sign (−1)^q on the tick, so the tick parity reads
    q mod 2.
  - Hypothesis H: the lepton rows are separated from the down rows exactly by the tick's parity, read at a point of
    order 10 over the mark.

## 2. What is computed

The frame is main's own (B1724's covariance.frame, with B1656's channel norm through B1723), imported unchanged from a
checkout of main. It is read at B1724's four moduli TAUS, with both ends (L_max and L_2 from B1667's column), and in all
three readings of the Higgs (S, S̃ = εS*εᵀ, S*).

- **X1, order 5 with one reading for all sectors.** At the mark (2/5, 4/5) and at five other points of order 5, for
  every τ, end and reading, the lepton outputs equal the down outputs (the relative difference stays below 10⁻⁹).
  This is the degeneracy restated.
- **X2, the readings.**
  - For all 9 pairs (lepton reading, down reading): whether the lepton outputs differ from the down outputs.
  - The Standard Model's own assignment gives the down and lepton sectors the same Higgs and the up sector its
    conjugate. That is one of the diagonal pairs, so X2 separates only with mixed pairs: an assignment that respects
    neither SU(5)'s multiplets nor the Standard Model's Higgs.
- **X3, other orders.** At B1724's lines of order 3, 7, 8, 10, 10 and 11: whether the lepton outputs differ from the
  down outputs.
- **X4, the tick's parity (hypothesis H).** At the four points of order 10 whose double is the mark (w/2 plus each
  half-period): whether the lepton outputs differ from the down outputs.
- **X5, colour.** Whether any ingredient of the frame depends on colour. This is code inspection: the frame's sector
  data are SIXY and SECT only.

## 3. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| X1 | lepton = down at every order-5 point, τ, end and reading | 97% |
| X2 | equal on the 3 diagonal pairs; different on some mixed pair | 80% |
| X3 | different at every line of order other than 5 | 85% |
| X4 | different at all four points of order 10 over the mark (H) | 85% |
| X5 | no ingredient of the frame carries colour | 95% |

## 4. The outcomes

- **The NEGATIVE part, if X1 holds:** with one reading for every sector, nothing in the frame at order 5 separates the
  leptons from the down quarks.
  - The second computation is the algebraic proof of § 1, independent of the numerics.
  - Under main's rule (M26), it stays PROVISIONAL until a seat of another family recomputes it.
- **The separators:** whichever of X2, X3 and X4 separate, named with where they do.
  - H is supported if X4 holds and plant P2 below restores the equality. Then the tick's parity is a structural
    candidate for the lepton rows.
  - H fails if X4 does not hold.
- **Colour:** reported as present or absent (X5). If it is absent, separating by colour needs an ingredient that the
  frame does not have.

## 5. Controls that must fail if the work is broken

- **P1 (positive control):** the lepton charges replaced by the down charges transposed, (6Y_L, 6Y_e) := (2, 1). The
  equality must hold everywhere, at every order.
- **P2 (the parity plant):** the lepton charges shifted by 5, to (2, 1) mod 10 exactly, which removes the odd
  difference. At the points of order 10 over the mark the equality must return. If it does not, X4's separation is not
  the parity's.
- **P3:** a sector compared with itself must read 0 difference, as a check of the instrument.

## 6. Files

relays/sm_c13/, with its script, output and run. The page is relays/SM_C13_THE_LEPTON_ROWS.md.
