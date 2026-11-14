# SM-C13 — the lepton rows at level 5: the tick's parity separates them; nothing at order 5 can

*The SM seat, 2026-11-14. Card `relays/cards/SM_C13_the-lepton-rows-at-level-5.md`, sealed and pushed at 4b8d157c0
before the run (M30). Main at af79e2e27. The frame is main's (B1724, B1723), imported unchanged. **Only differences
between sectors are written**: no output of the frame is printed or saved, and nothing is set beside a measured
number.*

## The answer

- **At order 5, with one Higgs reading for every sector, nothing in the frame separates the leptons from the down
  quarks.** That is the NEGATIVE part, and it is PROVISIONAL until a seat of another family recomputes it (M26's rule).
  - The algebra: the line of order 5 sees six-times-hypercharge only mod 5. The lepton pair (−3, 6) ≡ (2, 1) is the
    down pair (1, 2) swapped, so Y_lep = Y_downᵀ.
  - The numerics: at six points of order 5, four moduli, both ends and all three readings, the largest relative
    difference is 3.4 × 10⁻¹² at five points, and 1.2 × 10⁻⁹ at one, (0, 1/5).
  - At that point the positive control, exactly equal by construction, shows the same 1.2 × 10⁻⁹. That is the
    instrument's floor there. It is just above the card's bar of 10⁻⁹, which was set too tight; said below.
- **The tick's parity separates them** (hypothesis H, supported).
  - At the three points of order 10 whose double is the mark, the lepton outputs differ from the down outputs on every
    modulus, end and reading. The smallest relative difference is 2 × 10⁻².
  - At the fourth half, which has order 5, they are equal.
  - **The plant:** with the lepton charges shifted by 5, to (2, 1), the equality returns at the order-10 points, to
    10⁻¹².
  - So the separation is exactly the odd difference: 6Y_L − 6Y_d = −5 and 6Y_e − 6Y_Q = +5.
  - The record's odd-tick matter exists only twisted by the orientation, with the sign (−1)^q on the tick (B1926;
    SM-C10). It reads q mod 2, which is the bit that order 5 lacks.

## The four candidates, each tested

| candidate (M30) | result |
|---|---|
| a Higgs reading that differs between the sectors | **separates**, on all 6 mixed pairs (smallest difference 2.8 × 10⁻²). But both the Standard Model's assignment (down and lepton share a Higgs) and SU(5)'s (d^c and L share the 5̄) give the two sectors the same reading. So a mixed pair is a choice the record does not make, not structure |
| the colour multiplicity | **absent:** neither of the frame's sources carries any colour ingredient (code inspection: 0 tokens). Separating by colour needs an ingredient the frame does not have |
| the orientation-twisted modules at odd ticks | **separates, through the charge's parity:** order 10 = 5 × 2 over the mark, with the plant as above. Of the four, this is the only one the record already carries |
| points of another order | **separates** at every other order on B1724's lines: 3, 7, 8, 10 and 11 (smallest difference 2 × 10⁻² to 0.6) |

## What it means

- **Minimal SU(5)'s relation is what the read-out at level 5 must give.** It sees the hypercharge mod 5, which is
  constant on SU(5)'s multiplets. So "the lepton rows equal the down rows" is not a fault of the read-out; it is its
  level.
- **The record already contains the missing bit.** The lepton–down degeneracy is broken by the parity of 6Y. The
  record's own odd ticks carry exactly that parity, since their matter exists only twisted by (−1)^q.
- **A read-out that sees the tick's parity** would read at order 10 = 5 × 2. That could mean threads of the det −1
  act, or the mark's order-10 halves. It would have lepton rows of its own, not copied from the down rows.
  - Whether the read-out on the whole should include them is main's question.
  - This seat proposes it as SM-C13b: define the read-out at the mark's order-10 halves, or on threads with an odd
    number of ticks, by B1928's average, and compute its lepton rows. No value is set beside a measured number.
- **Not claimed:** that the separated lepton rows are right. Nothing here is compared with anything measured.

## Deviations and slips, said

- **The bar of 10⁻⁹ for "equal" was below the instrument's floor at one point.** At (0, 1/5) the order-5 equality,
  the diagonal reading pairs and the positive control all read 1.2 × 10⁻⁹. So three booleans read false. Every other
  point is at most 3.4 × 10⁻¹², and the smallest separation anywhere is 2 × 10⁻².
- **The card's X4 said "four points of order 10".** Halving is a bijection on points of order 5, so one of the four
  halves, (1/5, 2/5), has order 5. It served as a control and read equal. The other three have order 10.
- **The card's X3 listed "10, 10".** The run used B1724's five lines of order other than 5, with orders 3, 7, 8, 10
  and 11.
- **P1 and P2 are the same computation** (lepton charges (2, 1)). It serves both controls.

## Files

`relays/sm_c13/run_c13.py`, `relays/sm_c13/c13_results.json` (differences only) and `relays/sm_c13/RUN.txt`.
