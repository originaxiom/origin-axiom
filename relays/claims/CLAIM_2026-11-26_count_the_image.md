# CLAIM CARD — frame A's map to the six descends through none of its five named choices; joint image dimension 5

- seat, branch, commit: SM seat, this seat's branch (as on its page on main), the commit that adds this card
- kind: computation (negative for descent). First sealed run VOID by its own plant rule (SM-R612); the re-sealed run
  with a stated zero floor (SM-R612b) holds every plant and all twelve expectations, and confirms the reading
- touches: P-612, P-418, P-355; scoreboard codes A01, A02, A03, A04, A07, A09, A10
- effect: conditions — A01-A10's pricing: each discrete choice's image equals its menu (offset 10, ends 7, Higgs 3); the
  continuous choices' joint image has dimension 5; D = c^2 descends through tau, the end and the Higgs on the base line
  wherever D is defined
- imports: none (main's frozen-row instrument B1842 and B1840's ends, unchanged)
- premises on main: B1842, B1838, B1726, B1691, B1667, B1840, B1789, B1232 (T-COUNT-THE-IMAGE), P-355, B1834
- decisive script (re-sealed, SM-R612b): relays/sm_r612b/run.py, SHA-256 0d0edb642ce9dcbb, depends on numpy, mpmath
  and main's checkout (argv[1]), run as `python3 -B run.py MAIN_CHECKOUT > r612b_run.txt`, output SHA-256
  4fc024f64d7b32f4 (results json 818985ccd5cf839e); CONFIRMS: all plants within bounds, X1-X12 hold at three moduli
- void run, kept on record (SM-R612): relays/sm_r612/run.py, SHA-256 a0ae72658d25a97e, output SHA-256
  94db89885cb0a3bc; PL5 (T-law at delta = inf) failed as sealed (0.87-1.8) from logs of numerical-zero masses; post
  hoc relays/sm_r612/posthoc_numerical_zeros.py, SHA-256 f0c63edc330be995, output SHA-256 1c2d9c9cc48d6a96
- second computation: none yet
- already on main?: `grep -il "count the image" frontier/*/FINDINGS.md` on main: B1232 only (the retired P^3 case);
  B1831's reader table row 237 says it was never applied to the input count
- what would make it fail: PL2 (a 1e-4 planted channel change) must register NON-CONSTANT, and PL5 (the T-law) must hold
  on its defined outputs; in SM-R612b both did (2.7-3.1e-3; 1.4-2.8e-14)
