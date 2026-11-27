# Verdict, practice card P3 — REFUSE

*Banking seat V1, fam1-v1-unset-04, 2026-11-27. Expectation committed first (`relays/verdicts/E_P3.md`). Read: the card,
its decisive script and its control. Nothing else of the record.*

**REFUSE.** This seat's own code, sharing nothing with the card's script, finds every positive solution in the box
directly from the quadratic in z, with no move tree. The count is right: 13 solutions without regard to order. The claim
does not hold: 5 of the 13 have no entry equal to 3, namely (6, 15, 87), (6, 87, 507), (15, 39, 582), (15, 87, 1299) and
(6, 507, 2955), which are 3 times the Markov triples (2, 5, 29), (2, 29, 169), (5, 13, 194), (5, 29, 433) and (2, 169, 985).
The decisive script reports "True" because its flag is computed over `near`, the triples within two Vieta moves of
(1, 1, 1), and not over the 13 solutions it counts. Its decisive line therefore tests a different, smaller set than the
card states, and the control (an entry equal to 6, which (3, 3, 3) lacks) cannot detect that, since it fails on the near set
too. The claim is contradicted by recomputation, not merely unreproduced, so the verdict is REFUSE, not RETURN.

- own script: `relays/verdicts/v_p3_own.py`, SHA-256 98ddfa0b02929a15, run as `python3 -B relays/verdicts/v_p3_own.py 3000`
- its output: `relays/verdicts/v_p3_own_out.txt`, SHA-256 216e43404a3b14db
