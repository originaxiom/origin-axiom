# PRACTICE CARD — P1: the 280 nonzero integer solutions of x² + y² + z² = xyz with entries of size at most 3000 form exactly two orbits of L, R and their inverses within the box: the 70 positive ones from (3, 3, 3), and one orbit of 210 that mixes three sign patterns, each with two negative entries

*A practice card for the banking seats (main, 2026-11-26; P-885). It is not a claim card and the intake does not take it.
Its answer is sealed by main and opened after both banking seats have filed.*

```
- card id: practice P1
- seat code: fam1-v1-unset-01
- kind: computation
- scope: frame: no frame: the moves L, R, L^-1, R^-1 on integer solutions of x^2 + y^2 + z^2 = xyz; object: the orbits of the nonzero solutions with |entries| <= 3000, moving within the box; reach: single (one box); hypotheses: exact integer arithmetic
- identifications: none
- touches: none
- effect: adds — none (practice)
- imports: none
- premises on main: B1993 (its signs_posthoc.py, run unchanged)
- decisive script: relays/claims/practice/p1_two_orbits.py, depends on the standard library, run as python3 relays/claims/practice/p1_two_orbits.py
- decisive lines: the 2 lines it prints marked "DECISIVE:"
- failing control: python3 relays/claims/practice/p1_control.py (the moves cut to L and L^-1 alone)
- second computation: none
- what would make it fail: a third orbit among the nonzero solutions, or an orbit of 210 that does not mix the patterns
```
