# R21 — B1234 "A6 built the walls": two residual checks

Verdict: **MATCH** (both cells), with one VACUITY note on the CS sub-check.

## Blind-first record
Read before coding: `results.json` (cell1: 40/40 covers amphichiral, base 6/200 = 3.0%;
cell2: gieseking non-orientable, cover is m004, vol_ratio 2.0) and FINDINGS.md lines 25-35
(slice named only as "orientable 1-cusped census manifolds", 200). Code written and run
(`r21.py`) before opening `a6_built_the_walls.py`. Opened afterwards: it uses
`OrientableCuspedCensus(cusps=1)[:200]` with `symmetry_group().is_amphicheiral()` — same slice
and the orientation-aware test, matching my independent choice.

## (a) Control base rate
Slice: first 200 members of `OrientableCuspedCensus(cusps=1)`, test `symmetry_group().is_amphicheiral()`.
- **Mine: 6 / 200 = 3.0%** — m003, m004, m135, m136, m206, m207. No test failures.
- Banked: 6 / 200 = 3.0%. **MATCH.**
- Alt slice (first 200 of the full orientable census, any cusp count): 7/200 (adds m203). Sensitivity only.
- Planted positive: m003, m004 both flagged amphichiral by the test and appear in the count.
- The base rate uses the orientation-aware test, so it is not tainted by the orientation-blind
  instrument that affected the 112-family count elsewhere.

## (b) Cell 2 as results.json asserts it
Cell 2 asserts: m000 (Gieseking) non-orientable, orientation double cover isometric to m004, volume
ratio 2. Mine: is_orientable()=False, orientation_cover().is_isometric_to(m004)=True, ratio
1.9999999999999996. **MATCH.** (Volume ratio is true by construction; the isometry check is the
only non-vacuous part.)

Extra sub-check per cell brief (CS mod 1/2 on covers of m004, degrees 2..5, all covers snappy
enumerates: 1,1,2,4 covers): every cover has CS = 0.0. Consistent with "2-torsion (in fact 0)".
**VACUITY note:** CS(cover) = deg*CS(base) mod 1 and CS(m004)=0, so this could not have failed;
it is a consequence of CS(m004)=0, not independent evidence. Two of the four degree-5 covers are
NOT amphichiral despite CS=0: CS = 0 mod 1/2 does not imply amphichirality, only the converse.

## Gate 5
No measured SM values used. Files: r21.py, r21_results.json.
