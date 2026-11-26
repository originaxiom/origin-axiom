# V_P2 — practice card P2 — REFUSE

- seat code: fam1-v1-unset-05
- card: `relays/claims/practice/PRACTICE_P2.md` (main at ed9660a9d)
- expectation committed first: `relays/expectations/E_P1_P2.md`, commit 77407f88 (expected REFUSE)
- my script: `relays/verdicts/code/sm2_p2_divisibility.py`, SHA-256 665e20548f6e18c36123eadf34506ce4a8b3fc4d13778f1f8d035a4b0281f7cd,
  standard library only, run as `python3 relays/verdicts/code/sm2_p2_divisibility.py` (exit 1: the claim does not hold)
- its output: `relays/verdicts/code/sm2_p2_divisibility.out`, SHA-256 a04bf6d78f5098a139696f6330e1008ed9ac2047cf2e4e0fa7b4993b28693dd6
- label: recomputed independently; expectations committed first

**Verdict: REFUSE.** The claim is false on its smallest instance: (3,3,3) solves x^2+y^2+z^2 = xyz (27 = 27), lies in the
box, and 3 is not divisible by 9, which is the card's own failure condition. My code, a plain triple loop over positive
entries (no quadratic formula) followed by every ordering and the four admissible sign patterns, finds the same 136
nonzero solutions as the card; every entry is divisible by 3, and every one of the 136 has an entry not divisible by 9
(the seven unordered positive solutions are (3,3,3), (3,3,6), (3,6,15), (3,15,39), (3,39,102), (3,102,267), (6,15,87)).
The card's decisive script reports True because its instrument tests `c * c % m == 0`, the square of the entry: 9 | c^2
holds exactly when 3 | c, so it measures divisibility by 3 and not by 9 (with `--modulus 3` it reports the same 136, True).
The failing control does not guard this (K8): replacing 9 by 7 makes the run fail, but it checks only that some modulus
breaks the test, not that the test measures the claim; it cannot see an estimator that measures the wrong quantity. What
the record could hold instead, if anyone wants it: "every entry is divisible by 3", which my output supports for this box.
I do not fix the card (K11).

Decisive output:
```
nonzero solutions in the box: 136
all entries divisible by 3: True
all squares of entries divisible by 9: True
all entries divisible by 9: False
solutions with an entry not divisible by 9: 136 of 136; the first: [(-3, -3, 3), (-3, 3, -3), (3, -3, -3)]
solutions with all entries divisible by 9: 0
RESULT: the card's claim does not hold
```
The card's own script, run once to confirm the diagnosis (reproduction, not my check): `DECISIVE: ... 136` and
`DECISIVE: every entry of every one is divisible by 9: True`, exit 0.

**Disclosure (K1).** Before writing my expectation I ran `git log` on main to check my base, and main's commit subject of
c9057968 describes P2 as "an instrument that measures the square of an entry". My expectation file says it was written
from the cards alone; that is not quite so, and I say it here. The refusal does not rest on that line: the counterexample
(3,3,3) and my own count decide it.
