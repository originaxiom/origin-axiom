# B1757 — STEP 2'S TWO FREE DOUBLETS AT THE STRIP, THE FITTED VECTORS COMMITTED (POST HOC DATA, AT THE SM SEAT'S ASK): STEP 2 REPRODUCED EXACTLY; BOTH DOUBLETS SIT WITHIN ABOUT 0.1 OF ONE NULL LINE, (0, 1, i)/√2, EACH WITH ITS OWN SMALL e₁ ADMIXTURE

**Verdict: PROVED (computed; post hoc data, labelled — not a test, not a look).** cc (main), 2026-10-24, at the SM seat's
ask (its relay §277: "commit the fitted (H_u, H_d) vectors of step 2 at the strip in a tracked file"), for its named-pair
test W158 (the 26 special lines, P-377). **0 of 19.**

## 1. What was rerun

S217's step 2 (P-377; the audit-room `audit/verify_sweet/two_doublets_at_the_strip.py`) fitted two free Higgs doublets at
the six's strip but stored only the pulls. `verification/free_doublets.py` reruns its "both free" fit with the same starts,
seeds and least-squares settings — nine2() carried verbatim, B1656's frame at B1667's end through B1743's tracked modules,
both doublets read S, the leptons with H_d, c = 3 — and writes the vectors, each normalised with its largest component real
and positive (the χ² is blind to each doublet's overall phase).

**Reproduced exactly:** all eight χ²_nine values equal step 2's (19.08, 45.85, 4.05, 37.97, 29.17, 45.47, 2.75, 29.37 at the
four points of (2/5, 1/10) and both horocycles).

## 2. The vectors (`verification/free_doublets.json`)

At every point and horocycle both doublets lie within about 0.1 of the null line n = (0, 1, i)/√2 (up to phase): the
components along e₂ and e₃ have modulus 0.69–0.72 and the e₁ component 0.05–0.18; |h·h|/|h|² is 0.010–0.016 for H_u and
0.018–0.030 for H_d. The two best rows:

| τ, horocycle | χ²_nine | H_u (phase-fixed) | H_d (phase-fixed) |
|---|---|---|---|
| 0.3145 + 2.95i, L_max | 2.75 | (0.071 − 0.045i, −0.008 − 0.703i, 0.706) | (0.071 − 0.059i, 0.707, 0.016 + 0.701i) |
| 0.3333 + 3.0551i, L_max | 4.05 | (0.098 − 0.022i, −0.006 − 0.702i, 0.705) | (0.046 − 0.041i, 0.709, 0.019 + 0.702i) |

So the mixing at the strip comes from two doublets that are nearly the same null direction and differ by their small
e₁ admixtures — consistent with B1743's one-Higgs target (nearly null, e₁ admixture near 0.3) split between two doublets.

## 3. Scope

- Post hoc throughout: the strip, the line and the structure were chosen after the data; step 2's calibration (P-377) showed
  that two free doublets reach 66% of random CKMs given the data's six, so these fits are not evidence. They are the
  reference the SM seat asked for, to compare its named pairs (no continuous number) with the free fit.
- A verification of an earlier post hoc run (exact reproduction), not a new look.

## Seen first

`VERDICT topic-sweep /two (free )?doublets|two Higgs|H_u|step 2/ (full text): 44 of 1529 arcs on main match (NEGATIVE 6, OPEN 4, PROVED 33, no verdict file 1)`
— among them the record's two-doublet arcs B1742, B1743, B1746; the register's P-377, P-357, P-366. **Literature:** none beyond the record.

## Files

`verification/free_doublets.py` → `free_doublets.json`, `free_doublets_run.txt`. The lock: `tests/test_b1757_step_twos_free_doublets.py`.
