# PRACTICE CARD — P3: every positive integer solution of x² + y² + z² = xyz with entries of size at most 3000, taken without regard to order (13 of them), has an entry equal to 3

*A practice card for the banking seats (main, 2026-11-26; P-885). It is not a claim card and the intake does not take it.
Its answer is sealed by main and opened after both banking seats have filed.*

```
- card id: practice P3
- seat code: fam1-v1-unset-01
- kind: computation
- scope: frame: no frame: positive integer solutions of x^2 + y^2 + z^2 = xyz; object: whether each has an entry equal to 3; reach: single (one box, entries <= 3000); hypotheses: exact integer arithmetic
- identifications: the positive solutions are 3 times the Markov triples (a^2 + b^2 + c^2 = 3abc), a standard fact
- definitions: a Markov triple's Vieta moves are (a, b, c) -> (3bc - a, b, c), (a, 3ac - b, c), (a, b, 3ab - c); every Markov triple is reached from (1, 1, 1) by them
- touches: none
- effect: adds — none (practice)
- imports: none
- premises on main: none
- decisive script: relays/claims/practice/p3_threes.py, depends on the standard library, run as python3 relays/claims/practice/p3_threes.py
- decisive lines: the 2 lines it prints marked "DECISIVE:"
- failing control: python3 relays/claims/practice/p3_control.py (an entry equal to 6 in place of 3)
- second computation: none
- what would make it fail: a positive solution in the box, without an entry equal to 3
```
