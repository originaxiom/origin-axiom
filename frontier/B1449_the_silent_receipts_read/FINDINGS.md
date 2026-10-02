# B1449 — THE SILENT RECEIPTS, READ: fourteen tracked run logs that record a failure no arc acknowledged, opened one by one — three are not failures, five are acknowledged in other words, five are first attempts or stale, and one contradicts a banked number

cc, 2026-10-02. Lead L227 (B1425, 2026-09-18): of 1 458 tracked receipts 47 carry a failure marker and 15 of those
were *silent* — neither the file's name nor its arc's FINDINGS mentions a failure. One was repaired at the time;
"the work is to open the other 14". The lead ages on 2026-10-09 (Review 58, R58-3). **Verdict: PROVED** (the
fourteen read and classified; two computations re-run).

## The fourteen

| receipt | class | what it is |
|---|---|---|
| B771 `cells/W3-084/output.txt`, `cells/W4-084r/output.txt` | **not a failure** | the marker is the line `FAILED GATES: []`, an empty list |
| B771 `cells/W3-149r/output.txt` | **not a failure** | the word is prose about a negative control behaving as it should; the file ends `ALL CHECKS PASS` |
| B639 `b639_output.txt`, `b639_stage2_output.txt` | acknowledged | the gate that fails *is* the arc's NEGATIVE result, stated as its first finding |
| B1302 `sm_b1282_sibling_germ_rerun.txt` | acknowledged | the SM seat's script asserts on main's bench; the arc says so in its own words and re-derives the census |
| B771 `cells/OI-150/output.txt` | acknowledged | ends `SOME CHECKS FAILED`; the wave records it as report-lost and re-ran it |
| B498 `wild_hunt_results.txt` | acknowledged in substance | ends in a crash on the third word, which the arc records as "the resultant vanishes identically — named gap"; note added |
| B477 `context_log.txt` | incidental | a script run from the wrong directory; nothing rests on it; note added |
| B485 `conj_log.txt` | incidental | a first elimination attempt that crashed; the later attempts are beside it; note added |
| B670 `b2_run_log.txt` | incidental | a first run that crashed at step 3; `b2_run2_log.txt` beside it completes; note added |
| B764 `output.txt` | incidental | a correction attempted twice in one file, the second completing; note added |
| **B469 `octic_log.txt`** | **stale receipt; claim reproduced** | see §1 |
| **B771 `cells/W2-270/output.txt`** | **load-bearing** | see §2 |

Record: `verification/receipts_read.json`.

## 1. A decisive test whose only receipt was a crash

B469's "decisive cell" states that for s464 the generators (a, c) form a fibre basis (κ = −2) and that tr(ac)
satisfies the octic to 2·10⁻¹², which is what places the geometric character on the swapped component. The only
receipt of that test on disk is a `TypeError`, and the tracked `octic_test.py` raises the same error today: it
converts a SnapPy matrix entry to a multiprecision number in a way this bench's versions refuse.

With that one line changed (`verification/octic_test_fixed.py`, receipt `octic_test_fixed_run.txt`):

    tr(ac): |octic| = 2.1e-12        tr(aC): |octic| = 1.4e-12        tr(a): |octic| = 312
    kappa(a, c) = -2.00000000

**The claim is what the arc says.** The receipt was stale and the script does not run as tracked; both are now
said in B469's FINDINGS, and the tracked script is left as it was run (the record of what was run is not edited).

## 2. The one that contradicts a banked number

B530's Movement XXXIII banks a gap-slope ratio: *"slope₁/slope₂ at depth 9: 1.204 … converged but unidentified"*,
with slope₁ ≈ 0.183. B771's cell W2-270 exists to reproduce it and its receipt shows it does not: slope₁ = 0.1916
and ratio 1.2575 at depth 9, gates G1 and G3 FAIL. Two waves later the same question was closed (W4-270r,
RESOLVED-B, verified by re-run at the time): **the ratio is fit-protocol dependent — 1.148 with the first gap's
curvature in ε removed, 1.256 on the straight line through the origin** — because one gap's width is curved in ε
and the other's is not. B771 recorded that. B530, which carries the number, was never corrected.

Corrected now by addendum (`frontier/B530_natural_history/ADDENDUM_2026-10-02_…`): "1.204" and "converged" are
withdrawn; the movement's negative — the ratio is not √(1/φ² + 1) — stands and is stronger, the candidate missing
both readings by more than three times the noise. Error class E53.

## What it means

- **The lead's worry was half right.** A receipt contradicting its arc was among the fourteen — one of them. The
  other thirteen are a detector reading the word FAILED, results that are negative by design, and first attempts
  left beside their successes.
- **Two rules come out of it.** A failure marker in a receipt's *last line* is a different thing from one in its
  body, and the sweep should say which; and a script whose only receipt is a crash should be re-run before its
  arc is cited. The second would have found B469's in June.
- **Not done:** the sweep's detector is not changed here (its three false positives are recorded); the other 32
  receipts with a marker, which name their failure, were not re-read.

## Verification

`verification/receipts_read.json` (the fourteen, with the class and the action for each),
`octic_test_fixed.py` + `octic_test_fixed_run.txt`. Lock: `tests/test_b1449_silent_receipts.py`.
