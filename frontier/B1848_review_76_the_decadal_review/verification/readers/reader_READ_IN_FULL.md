# Review 76 — the reader's full read of B1845, B1846 and B1847 (seeded by the anchor 264fa6d98)

*An independent reader, a fresh-context subagent spawned by main and told to read skeptically. It edited no tracked
file. Its report is reproduced below with its must-fix and optional lists, followed by main's disposition. Main
verified every must-fix item at source before applying it. The reader computed and looked up no measured value.*

## The reader's verdicts

- **All three arcs HOLD WITH NOTES.**
- **All three test files pass:** B1845 3, B1846 5, B1847 7.
- **No number from a run that failed its own checks is used anywhere** (a git grep for the failed tube values found
  none in any tracked file).

## Must-fix, and main's disposition

| # | the reader's note | main's check | applied |
|---|---|---|---|
| B1846 #2 | T2's consequence overstated. The systole aaBa has θ constant to 1.7e-11, so its length measure pushes forward to an atom: a metric-canonical point at the tube | verified (step5 tube_spread 1.7e-11; the shortest geodesic is unique, multiplicity 1) | FINDINGS §§ 2 and 6, the verdict, P-726, the LAW_MAP row and main's memory corrected with dated notes. The metric supplies a point (the systole) and a weight (ρ), both at the tube |
| B1846 #3 | the verdict's 1.74 / 0.78 are Rcut 10; the body's are 1.75 / 0.81 | verified | the verdict corrected |
| B1846 #5 | "2.21 and then 2.07 per period" not in the cited file | verified (the file has k = 0, 1, 3, 5) | `tube_lengths.py` committed: 2.209, 2.065, 2.037, 2.031, 2.030 |
| B1846 #6 | "the tube stays at 0.185" cites a file with no lengths | verified | `tube_lengths_run.txt` committed; citation fixed |
| B1847 #2 | the two deep-grid logs uncommitted | verified (written after 7493091a9) | committed and cited in § 5, with the UNTRUSTED run's det E − 1 = 3.1e-2 |
| B1847 #4 | "three grids", two committed | verified | `gen_m004_40_run.txt` committed (re-run, identical to the session's value) |
| B1847 #5 | `sphere_complete.py` output missing; the script needs an uncommitted cache | verified | output committed; both scripts now rebuild their setup when no cache is present |
| B1847 #6 | the floor values uncommitted; the 0.33 / 0.787 sentence contradicts itself | verified | `exc_s0.25_full_run.txt` and `exc_s0.5_full_run.txt` committed; the sentence reworded |
| B1845 #3 | "17 %" is the 41-point sample; the exact fraction 2·acosh(h/2)/ℓ is 14.9 % | verified | FINDINGS and verdict corrected |

## Optional, and main's disposition

- **Applied:**
  - B1846 #4: "second sampling" in the verdict.
  - B1846 #7: the citations.
  - B1846 #8: the θ-normalisation wording.
  - B1846 #13: the vacuous rho2 lock, replaced by the run's |φ_Y − φ_0.9Y|.
  - B1847 #7: the excursion's interpolated-floor offset disclosed; Re ½ at 6e-6 and 7e-7; det E − 1 = 2.8e-4.
  - B1847 #9: "two meshings".
  - B1847 #10: the forced levels "asserted, numerically to about 1e-5"; the loop's closure a consistency check.
  - B1847 #11: 3.5e-9 and 1.8e-8.
  - B1847 #13 and B1846: the reflection locus written as Re τ ∈ {0, ½} or |τ| = 1.
- **Recorded, not applied** (do not affect a conclusion):
  - B1845 #1, #2, #4, #8: an exact Re printout; an argument for all m; a second N; a T-class enumeration output.
  - B1846 #9, #11, #12, #14: the χ² printouts; the tetrahedron 2.5σ; the old R10 script; the k → ∞ extrapolation.
  - B1847 #3: re-run the s = ¼ cross-check with the committed code. The m004 re-run with it reproduced exactly.

## The reader's report (verbatim summary of its conclusions)

- **B1845: HOLD WITH NOTES.**
  - "Re τ = ½ exactly" holds exactly, in rationals, for k = 0..20.
  - "fixes RL's eigenline iff k ≡ 0 mod 5" holds for k ≤ 20.
  - The arclength fraction is 14.9 %, not 17 %.
  - The § 4 table matches to 2 decimals.
  - The S-reduction convention holds to 1e-3.
  - The two apex methods are independent and agree to 12 digits.
- **B1846: HOLD WITH NOTES.**
  - T1's proof is complete for the energy measure. It assumes θ's minimal-growth cusp expansion and its existence on a
    cusped manifold; Eells–Sampson is cited for the compact case only.
  - T2's proof is complete for the volume pushforward. Its stated consequences overreach: the systole is a
    counterexample.
  - The numbers match their outputs, except the slips listed above.
- **B1847: HOLD WITH NOTES.**
  - The tube failure is disclosed consistently everywhere.
  - The controls and the Richardson limits recompute.
  - +0.57 % and +16 % check.
  - The Kashaev 46 + 2√5 re-derived by hand.
  - The general mesher's committed outputs predate the committed code, but m004 reproduces exactly with the current code.
