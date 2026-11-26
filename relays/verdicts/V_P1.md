# V_P1 — practice card P1 — ACCEPT

- seat code: fam1-v1-unset-05
- card: `relays/claims/practice/PRACTICE_P1.md` (main at ed9660a9d)
- expectation committed first: `relays/expectations/E_P1_P2.md`, commit 77407f88 (expected ACCEPT, with doubts to check)
- my script: `relays/verdicts/code/sm2_p1_orbits.py`, SHA-256 b5e027c12e27d5f54e3359024a6669ad2cf28b2af8d31c62cf9b11b4e9e95ba8,
  standard library only, run as `python3 relays/verdicts/code/sm2_p1_orbits.py` (exit 0)
- its output: `relays/verdicts/code/sm2_p1_orbits.out`, SHA-256 cdfaa06757f7d01c1fef915c6897611c87bad31b87900db917fa2c44ef7ada50
- my controls: the same script with `--moves L` and `--moves R` (outputs `sm2_p1_orbits_L.out`, `sm2_p1_orbits_R.out`), exit 1
- label: recomputed independently; expectations committed first

**Verdict: ACCEPT.** I recomputed the claim from its statement with code that shares nothing with the card's script. I did
not read or run B1993's `signs_posthoc.py`: I took the four moves from the card's failing control (`p1_control.py`, which
asserts they are B1993's), derived and checked their inverses myself, and enumerated the solutions by an elementary
reduction that I prove in the script's docstring rather than cite (K4): a zero entry forces (0,0,0), and a nonzero
solution has zero or two negative entries, so every one is a sign pattern applied to a positive solution, which I found by
brute force over 1 <= x <= y <= 3000. There are 70 positive solutions and 280 nonzero ones; the moves keep the equation
and are bijections; orbits, taken as connected components of the moves that land inside the box, are exactly two, of
sizes 70 and 210. The 70 is all-positive and contains (3,3,3); the 210 holds 70 of each of the three patterns with two
negative entries. The card's failure condition (a third orbit, or a 210 that does not mix) is not met. The control is
two-sided (K8): with L and L^-1 alone, or R and R^-1 alone, my code finds 96 orbits and the claim fails, so the instrument
can see a split. Scope (K9): the claim is for one box, |entries| <= 3000, and I checked only that box; nothing here says
the two-orbit picture holds for other boxes or unboxed. Note: the card itself does not define L and R; they are read
from its control script, and a card for the record should state them.

Decisive output:
```
moves: LR
positive solutions in the box: 70
nonzero solutions in the box: 280
orbits: 2 sizes: [70, 210]
  orbit of 70, contains True: sign patterns {(1, 1, 1): 70}
  orbit of 210, contains False: sign patterns {(-1, -1, 1): 70, (-1, 1, -1): 70, (1, -1, -1): 70}
RESULT: the card's claim holds
```
Controls: `--moves L` and `--moves R` each give `orbits: 96` and `RESULT: the card's claim does not hold`.
