# Expectation for practice card P3 (sm2, fam1-v1-unset-05), committed before any run

Written from `relays/claims/practice/PRACTICE_P3.md` alone, before reading or running its scripts, before running any
code of mine, and without reading main's log.

## P3 — expected: REFUSE
(6, 15, 87) solves x^2 + y^2 + z^2 = xyz: 36 + 225 + 7569 = 7830 = 6 * 15 * 87. It is positive, inside the box, and has no
entry equal to 3: the card's own failure condition. In Markov terms it is 3 * (2, 5, 29), a triple without a 1.
I expect the 13 unordered solutions to be 3 times (1,1,1), (1,1,2), (1,2,5), (1,5,13), (2,5,29), (1,13,34), (1,34,89),
(2,29,169), (5,13,194), (1,89,233), (5,29,433), (1,233,610), (2,169,985); so 13 is right, and the triples without an entry
3 should be four: (6,15,87), (6,87,507), (15,39,582), (15,87,1299), (6,507,2955).
[Corrected below this line before any run: that list is five, not four, and mixes in two wrong triples; my expectation is
"at least (6,15,87) and the others built on (2,5,29), (2,29,169), (5,13,194), (5,29,433), (2,169,985)": five without a 3.]
The "identification" with Markov triples is a cited fact (K4); my recount will not rest on it but enumerate directly.
If the card's script reports that all 13 have an entry 3, its instrument tests something other than "an entry equals 3".
