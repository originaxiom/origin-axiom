# B1625 — THE SM SEAT'S CORRECTIONS TO B1620 TAKEN (W42–W45): TM1 under T̄ ⊗ T only and TM2 under T ⊗ T; the frame named "all of G flavour"; the PMNS fit predicate made strict; the 13 unreduced in every frame on record; the weave's own surface reads index 0 (W45, registered under FK11)

**Verdict: PROVED** (a correction and harvest arc). cc (main), 2026-10-09. Every correction was checked on B1620's own
stored data before it was taken. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /TM1|TM2|trimaximal|fit predicate|frame where c|W4[2-5]/: 7 of 1397 arcs on main match (NEGATIVE 3, PROVED 4)`
— B1612, B1613 (P10), B1620 and B1621; the SM seat's relay §42–§47 and its dossier W42–W45 @ `f81a8fbaf`; the audit
lane's fit-acceptance point. **Literature:** none new (the trimaximal patterns TM1 and TM2 are standard).

## 1. What was wrong on main, and what was checked

| the seat's point | checked on main | taken |
|---|---|---|
| TM1 is allowed under T̄ ⊗ T only; under T ⊗ T the family is TM2 (W43: 0 of 576 pairs carry a TM1 column) | B1620's two T ⊗ T families fix the column (⅓, ⅓, ⅓), with block sums ⅓ and ⅔ in every row: TM2. Under T̄ ⊗ T the (3, 2) pairs fix (⅓, ⅓, ⅓) and the (3, 8) and (6, 8) pairs fix (⅔, ⅙, ⅙) | yes: B1620's addendum, P10's note, GENESIS v1.36, the theorem row, the write-up and its page |
| B1620's frame is "all of G is flavour", not W24's (there only c is flavour, and nothing is constrained) | B1620 computed every subgroup of G as flavour | yes |
| the PMNS fit predicate was lenient (up to a half-width outside the 3σ ranges) | `fit()` accepted a score ≤ 1, where the score is the excursion in half-widths; the four (8, 8) rows score 0.0707 | yes: strict "inside"; the four (8, 8) rows relabelled outside, and the (2, 8) dimension-3 rows reached with the seat's witnesses; the minimum stays 2 |
| the rank estimator can add a spurious rank near a degeneracy | the CKM bound uses the block test, which is sample-free | noted; the PMNS minimum is the seat's modal rank too |
| "the weave is exactly symmetric at every τ" (the seat's own phrase, withdrawn at its §42.5) | used in the write-up's "Why" paragraph | replaced: at a given τ only the parity grading survives |

## 2. What the seat adds (registered)

- **W44:** the CKM needs a four-dimensional family under every tensor in every frame on record. **The weave's symmetry
  reduces none of the 13 without a frame.** Where c is gauge, Sym² T allows one lepton relation (a fixed entry 1/√2 or
  ½, for example sin²θ₂₃ ≈ 0.511): a second lepton relation on record, besides TM1 and TM2.
- **W45:** on the weave's own surface M₁,₂, the four-dimensional Dirac operator twisted by 𝕎 (odd spin structure, weight
  3/2, given Λ, canonical cusp condition) has index 0 for both hands. A chiral three there is exactly one unit of end
  data at the cusp. Recorded on GENESIS v1.36 under FK11, with that scope; its question is FK10's.
- **W42:** a thread's own H¹ reads the rule's word through its letter counts and breaks the grading only democratically.
  It is now a candidate in the write-up's question 5.

## 3. Disclosed

- The seat's verifications (W42) and computations (W44's c-gauge frame, W45) were read, not re-run on main.
- The corrected texts keep their earlier wording visible through dated notes (B1620's addendum, P10's correction line,
  the theorem row's "[Corrected …]", GENESIS's [v1.36] markers). The landing logs of S98–S101 are history and stay as
  written.
- The mislabel is filed as an E65 instance (ERROR_LEDGER), together with the lenient predicate.

**Credit:** the SM seat (W42–W45, relay §42–§47), and the audit lane for the fit-acceptance point.

## 4. Files

`adoption/amend.py` (GENESIS v1.35 → v1.36, against `received/GENESIS_v1_35_main.md`); the lock
`verification/test_b1625_the_seats_corrections_taken.py`.
