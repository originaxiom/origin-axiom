# V_P3 — practice card P3 — REFUSE

- seat code: fam1-v1-unset-05
- card: `relays/claims/practice/PRACTICE_P3.md` (main at 6f0f8fe45)
- expectation committed first: `relays/expectations/E_P3.md`, commit 7e50f4ee (expected REFUSE)
- my script: `relays/verdicts/code/sm2_p3_threes.py`, SHA-256 c32c26ac3dd5cc5c0161f94975c7ac7d9de93578db4f5e09b01af59e0e81c577,
  standard library only, run as `python3 relays/verdicts/code/sm2_p3_threes.py` (exit 1: the claim does not hold)
- its output: `relays/verdicts/code/sm2_p3_threes.out`, SHA-256 63935472ca32a75366c2aec08bdf2b07b947da4784860fc5f9a95021947503f6
- label: recomputed independently; expectations committed first

**Verdict: REFUSE.** The claim is false in its box: (6, 15, 87) is a positive solution (36 + 225 + 7569 = 7830 = 6·15·87)
with no entry equal to 3, which is the card's own failure condition. My code uses no Markov tree and does not rest on the
card's identification (K4): it brute-forces 1 <= x <= y <= 3000 with z from the quadratic, checks every solution by
substitution, and finds the same 13 unordered solutions the card counts. Five of them have no entry 3: (6,15,87),
(6,87,507), (15,39,582), (15,87,1299), (6,507,2955). The card's script gets True because it tests the claim on the wrong
set (K8): it builds all 13 but evaluates `ok` over `near`, the triples within two Vieta moves of (1,1,1), which are
(1,1,1), (1,1,2), (1,2,5) and all contain a 1. Its count line describes one set and its claim line another. The failing
control (entry 6 for 3) fails only because (3,3,3) lies in `near`; it cannot see that the check skips most of the
solutions. What the record could hold instead: "8 of the 13 have an entry equal to 3". I do not fix the card (K11).

Decisive output:
```
unordered positive solutions with entries <= 3000: 13
solutions without an entry equal to 3: 5: [(6, 15, 87), (6, 87, 507), (15, 39, 582), (15, 87, 1299), (6, 507, 2955)]
RESULT: the card's claim does not hold
```
The card's own script, run once after my count (reproduction, not my check): `DECISIVE: ... 13` and
`DECISIVE: each has an entry equal to 3: True`, exit 0.

**Note on my expectation.** E_P3 first listed the five triples above correctly but called them "four"; the bracketed
"correction" that followed wrongly said two of them were wrong. The run shows the first list was right, and five is the
right count. The expected verdict, REFUSE on (6,15,87), did not change. For P3 I read only the card and its two scripts,
and not main's log.
