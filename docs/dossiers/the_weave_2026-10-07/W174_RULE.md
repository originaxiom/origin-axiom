# W174 — THE RIDDLE, item 4, the skeleton census: does any forced exponent pattern on record, with one shared small parameter and coefficients of order one, carry the six? (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **THE RIDDLE** (NOTE, "Reading: THE RIDDLE"; relay §316), program item 4. It is also the owner's goal of 2026-10-21:
  a forced integer pattern and one weave constant.
- **What W173 found** (relay §319). At the best rows the fit is carried by the chosen point. The first generation
  needs prefactors of 4.6 to 51 over the frame's local exponents. Local exponents at Im τ ≈ 3 are not the forced ones,
  though. The forced ones are the asymptotic exponents at the cusp, and the residual-charge exponents at ω.
- **The question here** is the skeleton's own. Take every forced pattern on record. Allow one small parameter shared by
  the three sectors, as one fibre requires, and coefficients within a factor 3. Can the pattern carry the six?
  - If none can, no choice of point works, and the problem is upstream: the dictionary or the charges.
  - If one can, it is the target, and its small parameter is the one number left.

## The data's side (fixed now)

- The six are the record's targets, read once: ln(m₂/m₃) and ln(m₁/m₃) for up, down and leptons. The source is
  B1741's file, through `T8.targets`. No lepton factor is applied, since a factor within 3 is inside the tolerance.
- **The skeleton test.** A pattern gives exponents n_i ≥ 0 for the six in units of one small parameter's logarithm
  s < 0. Some patterns carry a stated forced factor g_i(s), such as B1691's Im τ. The test passes if there is an s
  with |d_i − n_i s − ln g_i(s)| ≤ ln 3 for all six. This is an intersection of six intervals, solved exactly; the
  Im τ factor is handled by a fine scan in s.
- A pattern with n_i = 0 for a feature passes that feature only if |d_i| ≤ ln 3. A massless channel (m₁ ≡ 0) fails.

## The forced patterns (the menu, fixed now)

- **A, the cusp in the record's frame, on every census line.**
  - The frame is B1656's, as W162 runs it (`the_census_window.py`'s point): own residues and norms, Higgs DR, the
    readings (S̃, S, S), L_max held at its Im τ = 4 value above 4 (W162's stated choice), and W162's whole-term theta
    series.
  - For each of the 266 lines, the six at Im τ = 3, 4, 5 and 6, at Re τ = 1/8 and 3/8.
  - **The precision floor.** The ratios come from a double-precision SVD, so a ratio below 10⁻¹² is not resolved. Such
    a value is flagged and not used.
  - **The exponents.** The local exponent between two heights is e_i = −Δf_i/(2π Δy). The pattern n_i is the
    exponent from 5 to 6 where both values are above the floor, else from 4 to 5, else from 3 to 4, flagged by which.
    In units of s = −2π Im τ the pattern is n_i = e_i, with s shared by the sectors.
  - The forced intercepts P_i = f_i(y) + 2π y n_i, at the top height used, are recorded as a read-out. The test
    leaves the coefficients free within ln 3.
  - Lines with a massless channel (a ratio at the floor at every height) fail the test.
  - A line passes if its pattern passes at either Re τ. Both are reported.
- **B, the cusp with a covariant Higgs** (main's B1691, PROVED). In every sector m₂/m₃ ∝ ∣q∣^½ and m₁/m₃ ∝ Im τ·∣q∣.
  With s = −2π Im τ that is n = (½, 1) in every sector, with g = Im τ on m₁/m₃.
- **C, the point ω** (B1691's table by k mod 6, and W68's pairings). Per sector, one pattern (p₂, p₁) for
  (m₂/m₃, m₁/m₃) in powers of δ = ∣τ − ω∣, from the menu (1, 1), (2, 3), (1, 2) and (2, 4). The patterns with a massless
  or unhierarchical generation are left out, since they fail by construction. All 64 assignments of a pattern to each
  sector are tested, with δ shared.
- **C′, ω with forced coefficients** (W118's double ratios for the (1, 2) pairings). It is not recomputed: W118 found
  no forced double ratio in the down or lepton window. It is cited as the coefficient-level answer.
- **Out:** i (no forced pattern at i is on record; named open), other readings and horocycles, and the CKM.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| S0 | **The instrument and convergence.** On at least 90% of the lines whose six are above the floor at Im τ = 6, the exponents from (4, 5) and from (5, 6) agree to 0.02, and those at Re τ = 1/8 and 3/8 agree to 0.02 | 60% |
| S1 | **The cusp in the frame (decisive for A).** No census line's asymptotic pattern passes the skeleton test | 55% |
| S2 | **B1691's covariant skeleton.** It fails the test: one ∣q∣ cannot give the three sectors' m₂/m₃ within a factor 3 each | 97% |
| S3 | **ω.** None of the 64 assignments passes the test with one shared δ | 50% |
| S4 | **Capacity, if anything passes.** For each menu (A, C) where the data pass, at least 5% of 20 000 random sixes also pass. The random sixes are the data shifted by independent U(−2, 2) per feature, redrawn while a sector has m₁ > m₂ or a ratio above 1 (seed 1740174). If nothing passes, S4 is read out with no prediction | 70% |
| R | **Read-outs** (no predictions): the data's own ratios ln(m₁/m₃)/ln(m₂/m₃) per sector and the ratios of the sectors' ln(m₂/m₃); per line the asymptotic n_i, the forced intercepts P_i, and the least worst-feature excess over ln 3 with its s; the lines and assignments closest to passing; the null pass rates for A and C, and for B on the first 2000 draws | — |

## What the outcomes mean (fixed now)

- **S1, S2 and S3 hold** (nothing passes): no forced exponent pattern on record carries the six with one shared small
  parameter and coefficients of order one.
  - No choice of point can repair this, since the pattern is what the point cannot change.
  - The problem is upstream: in the dictionary (which fields carry which sections) or in the charges themselves.
  - THE RIDDLE then has its sharpest form. The symmetric principle delivers patterns, and the data's pattern is not
    among them.
- **Some pattern passes:**
  - with S4 failing (the null passes below 5%): that pattern is the record's first skeleton match, and its small
    parameter is the one number left. It becomes the next arc's target, sealed;
  - with S4 holding (the null passes at 5% or more): the pass is the menu's capacity, not a skeleton.
- **S0 fails:** the exponents have not converged by Im τ = 6 on too many lines. S1 is then read on the converged
  lines only, the others are named, and whether the forced asymptotic pattern differs from the height-6 one stays
  open.

## Weave or thread

- A frame census over every census line and every forced pattern on record at the cusp and at ω. It is a frame result,
  not a weave result: the frame is B1656's, and the patterns are the frame's.

## Looks (charter viii)

- One look at the six, counted. The six are read once, and the test selects no line for any later fit.

## Seen before the rule (disclosed)

- W173's output: the local exponents and intercepts at the rows (Im τ ≈ 3), and the down quark's first-generation
  prefactor of 43–51.
- Main's B1691 (FINDINGS read today) and its addenda: the covariant exponents, the free section coefficients, and ω's
  table.
- **The data's m₂/m₃ spread, by arithmetic.** Up and leptons differ by a factor of about 16, more than the 9 two
  factors of 3 allow. So S2's outcome is known by hand, and its prior says so.
- **Mental arithmetic on menu C was begun and stopped** before any verdict, when it was seen to be the cell's test.
  S3's prior is set without it.
- Not computed: no asymptotic exponent on any line, no menu-A or menu-C test, and no null.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
