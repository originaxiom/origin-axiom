# PRACTICE CARD — P2: every nonzero integer solution of x² + y² + z² = xyz with entries of size at most 300 (136 of them) has all three entries divisible by 9

*A practice card for the banking seats (main, 2026-11-26; P-885). It is not a claim card and the intake does not take it.
Its answer is sealed by main and opened after both banking seats have filed.*

```
- card id: practice P2
- seat code: fam1-v1-unset-01
- kind: computation
- scope: frame: no frame: integer solutions of x^2 + y^2 + z^2 = xyz; object: the divisibility of their entries; reach: single (one box, |entries| <= 300); hypotheses: exact integer arithmetic
- identifications: none
- touches: none
- effect: adds — none (practice)
- imports: none
- premises on main: B1993 (the same equation; its M1)
- decisive script: relays/claims/practice/p2_mod9.py, depends on the standard library, run as python3 relays/claims/practice/p2_mod9.py
- decisive lines: the 2 lines it prints marked "DECISIVE:"
- failing control: python3 relays/claims/practice/p2_control.py (the modulus 7 in place of 9)
- second computation: none
- what would make it fail: a nonzero solution in the box with an entry not divisible by 9
```
