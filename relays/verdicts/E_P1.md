# Expectation, practice card P1 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-27. Read: the card `relays/claims/practice/PRACTICE_P1.md`, its decisive script and its control (for the
definition of the moves only). Nothing else of the record. No code run yet.*

- **Reasoning before the run.** x² + y² + z² = xyz is three times Markov's equation, so its positive solutions are
  (3a, 3b, 3c) with a² + b² + c² = 3abc. Flipping the signs of two entries preserves the equation, so each positive
  solution has three companions with two negative entries. The moves send sign patterns to sign patterns (a move after
  a flip equals a flip after the move, with the flip carried along), so each orbit of the companions maps onto a
  positive orbit by taking absolute values.
- **What can go wrong:** the restriction "moving within the box" can cut an orbit in two; the 210 may split into three
  orbits of 70 (one per pattern) if the moves never change which entry is positive; or the counts may be off.
- **Expectation:** the card holds (280 nonzero solutions; two orbits within the box; sizes 70 and 210; the 210 mixing the
  three patterns): **60%**. The likeliest fault, if any, is the split of the 210 by pattern: 25%. A count error: 15%.
