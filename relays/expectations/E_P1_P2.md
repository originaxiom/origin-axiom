# Expectations for practice cards P1 and P2 (sm2, fam1-v1-unset-05), committed before any run

Written from the two cards alone (`relays/claims/practice/PRACTICE_P1.md`, `PRACTICE_P2.md`), before reading or running
their scripts and before running any code of mine.

Background I bring: if x^2 + y^2 + z^2 = xyz has a nonzero integer solution then 3 divides each entry, and (x/3, y/3, z/3)
solves the Markov equation a^2 + b^2 + c^2 = 3abc. The product xyz equals a positive sum of squares, so a nonzero solution
has zero or two negative entries: four sign patterns, each holding the same number of solutions.

## P2 — expected: REFUSE
(3, 3, 3) is a solution (27 = 27) inside the box, and 3 is not divisible by 9. So the claim "all three entries divisible by
9" should be false, and the card's own failure condition is met by its smallest instance. I expect my recount to find the
136 solutions, all with entries divisible by 3, and many (at least those built on the Markov numbers 1, 2, 5, 13, 29, 34, 89)
with entries not divisible by 9. If the card's script reports 136 of 136 divisible by 9, its instrument is not measuring
what the claim says (for example testing an entry's square, or 3 | x, in place of 9 | x).
What would change my mind: a definition of "divisible" or of the solution set in the script that differs from the card's
words; then RETURN, not ACCEPT.

## P1 — expected: ACCEPT, with doubts to check
- 280 = 4 x 70 fits four sign patterns of 70 each, if there are 70 ordered positive solutions with entries <= 3000, i.e.
  ordered Markov triples with entries <= 1000. I expect my count to give 70; if not, REFUSE.
- The card does not define L and R. I will take their definition from the script, as the claim's specification only, and
  write my own code. Vieta flips alone keep the sign pattern; moves that also permute coordinates can mix patterns. Whether
  the negative patterns merge into one orbit of 210 and the positive pattern stays alone depends on that definition.
- Moving "within the box" could split an orbit if a path must leave the box; on the Markov tree the path to the root only
  descends, so I expect no splitting, but I will check.
- What would make me REFUSE: a third orbit, an orbit of 210 lying in one sign pattern, a count other than 70/210/280, or
  moves that are not invertible on the set (then "orbit" is ill-defined). RETURN if the moves cannot be read unambiguously.
