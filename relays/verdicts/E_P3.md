# Expectation, practice card P3 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-27. Read: the card `relays/claims/practice/PRACTICE_P3.md`, its decisive script and its control. Nothing else
of the record. No code run yet.*

- **The claim** is that every positive solution with entries ≤ 3000 (13 unordered) has an entry 3, that is, every
  Markov triple with entries ≤ 1000 contains a 1.
- **Reading the decisive script:** its decisive flag `ok` is computed over `near`, the triples within two moves of
  (1, 1, 1), not over all the solutions it counts. So the script's "True" does not test the claim as stated.
- **By hand:** Markov triples such as (2, 5, 29), (5, 13, 194), (2, 29, 169), (5, 29, 433) and (2, 169, 985) contain no 1.
  If they lie in the box, the solutions (6, 15, 87) and others have no entry equal to 3.
- **Expectation:** the count of 13 is right (70%), and the claim fails, with several solutions lacking an entry 3:
  **90%**. Verdict expected: REFUSE.
