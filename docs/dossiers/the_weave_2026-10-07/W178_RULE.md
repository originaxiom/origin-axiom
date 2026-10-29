# W178 — the six's exponents at the cusp, exactly: W174's frame six on every census line up to Im τ = 48, in working precision with W177's norms, and W174's S0 and S1 settled (the rule, committed before the script)

The SM-derivation seat, 2026-10-29, at the owner's "all u reccomend" (this seat's item 4, its second half).
Committed and pushed before the script that reads it exists. Nothing here is a result.

## Why

- **W174's S0 failed.** On 46 of 179 resolved lines the six's exponents had not converged by Im τ = 6.
- **Its S1 was read on local exponents.** "No forced cusp pattern carries the six" was tested on the exponents at
  Im τ 3–6. 54 lines were not tested at all, because a ratio fell below double precision's 10⁻¹² floor.
- **W177 made the kernel norms exact and fast.** It also found a slow first correction on some kernels: 24.9 at
  Im τ = 6 for λ₊ = 1/22, on the slope-2/11 lines.
- **This arc** computes W174's six exactly at heights up to 48 on every census line, and settles S0 and S1 on the
  cusp exponents.

## The frame (fixed now)

- **W174's six, as W162's point computes them.** The frame is B1656's:
  - the residues (W93's closed form times κ);
  - the kernel norms c_s;
  - the Higgs DR;
  - the readings (S̃, S, S) for up, down and leptons;
  - L_max held at its Im τ = 4 value (W162's stated choice);
  - u_s = √(2πL + c_s)·R_s, zero where 2πL + c_s ≤ 0;
  - Y from W93's coupling, and the six as the logarithms of its singular values' ratios.
- **Every piece in working precision.** The residues, κ and DR are computed in mpmath at the working precision (DR by
  `T8.higgs_DR`'s formula, with its truncations set by the precision). The norms come from W177's series and the
  singular values from mpmath.
- **The one change.** Above Im τ = 6 the record's absolute residue cut is not applied. (The cut sets u_s = 0 where
  |R_s| ≤ 10⁻¹²; it is main's rule, as W162 applies it.)
  - It is a double-precision device. At large heights its absolute threshold removes the channels whose exponents
    are the question.
  - At Im τ 3–6 the six are computed with the cut, for the tie. At Im τ = 6 they are computed both ways, as a
    read-out.

## The computation (fixed now)

- **Lines:** all 266 census lines (`T8.own_lines`), at Re τ = 1/8 and 3/8.
- **The tie:** Im τ ∈ {3, 4, 5, 6}, with the cut.
- **The ladder:** Im τ ∈ {6, 8, 12, 16, 24, 32, 48}, without the cut.
- **Precision.** Each point is computed at p₁ = 40 + ⌈8πy/ln 10⌉ digits and at p₂ = p₁ + 60.
  - A feature (one ln ratio) is **resolved** when the two agree within 10⁻⁶.
  - It is **zero at working precision** when at both it lies within 30 digits of that precision's floor.
  - Otherwise the point is repeated once at 2p₁ and 2p₂. A feature that is still neither is **unresolved**.
  - Every status is counted.
- **The exponents.** e_i(y₁, y₂) = −[ln r_i(y₂) − ln r_i(y₁)]/(2π(y₂ − y₁)) on consecutive ladder heights. The
  cusp pattern is e(32, 48).
- **The skeleton test** is W174's, unchanged: `interval` on the six, read once through `T8.targets`, with s shared and
  the tolerance ln 3. A line with a zero channel fails it, as in W174. The read-out's null uses W174's draws (seed
  1740174, 20 000 draws).
- Four worker processes. A failed task is kept and counted.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| T0 | **The tie.** With the cut, at Im τ 3–6, every feature W174 stored above ln 10⁻⁸ agrees with this instrument within 10⁻⁶, on every line at both Re τ | 85% |
| T1 | **Convergence (W174's S0 settled).** On every line whose six are resolved at every ladder height at both Re τ, \|e(32, 48) − e(24, 32)\| ≤ 0.005 for all six, and the two Re τ give cusp patterns within 0.005 | 70% |
| T2 | **W174's S1 at the cusp.** No line's cusp pattern passes W174's skeleton test, at either Re τ | 75% |
| R | **Read-outs** (no predictions): per line and Re τ, the six at every ladder height with their status, the local exponents, the cusp pattern, the intercepts at 48, and the difference from W174's local pattern; the counts of zero channels and unresolved features; the lines not converged; the ten closest to passing; the null pass rate of the cusp patterns; the features the cut changes at Im τ = 6; per line, W174's S0 status beside the slowest kernel's min(λ₊, λ₋) (0 for an integer λ); the lines whose W174 pattern differs from the cusp pattern by more than 0.02 | — |

## What the outcomes mean (fixed now)

- **T0 holds:** the instrument is W174's frame, computed exactly.
- **T0 fails:** the instrument differs from W174's. The misses are named, and T1 and T2 stand for this instrument
  only. The cause is found before anything else is read.
- **T1 holds:** W174's S0 is settled. Every resolved line's six have cusp exponents, read exactly, and the failure at
  Im τ = 6 was pre-asymptotic.
- **T1 fails on some lines:** their exponents still drift between Im τ 24 and 48. They are named, with their slowest
  kernel rate. Their e(32, 48) is still tested in T2, and flagged as not a limit.
- **T2 holds:** W174's S1 stands at the cusp on every census line, now including the lines W174 could not resolve. No
  cusp pattern the frame forces carries the six with one shared small parameter and coefficients within a factor 3.
- **T2 fails:** a line's cusp pattern passes. The null decides, as in W174: at 5% or more it is the menu's capacity;
  below 5% it is the record's first skeleton match, and the next arc's sealed target.

## Weave or thread

- **neither (a frame census over every census line at the cusp).** The frame is B1656's, as in W174. The lines are all
  266, none picked.

## What stays out

- ω and B1691's skeleton: W174's S2 and S3 stand.
- Other readings and horocycles, L above Im τ = 4 (held, as in W162), and the CKM.

## Looks

- One look at the six, counted: T2 reads them once, through `T8.targets`, as W174 did. No line is selected for a later
  fit.

## Seen before the rule (disclosed)

- **The read-only map of W174's construction and its probe** (disclosed in W177's rule). The probe computed the six at
  large Im τ on five lines, in mixed precision. It found:
  - convergence toward (0.3, 0.8, 0.2, 0.55, 0.2, 0.55) on two slope-2/5 lines;
  - convergence toward (3/8, 7/8, 1/8, 1/2, 1/8, 5/8) on (3/8, 1/2);
  - drift on (2/11, 5/11) and (1/6, 0) at Im τ = 20.
- **W177's output:** the cusp limits, and the size of the first correction on the grid's four λ classes.
- **W174's stored output, read in recording W177:** the 46 unconverged lines, and the slope-2/11 lines' convergence
  measures (0.017–0.027).
- **Mental arithmetic while designing this rule.** λ was worked out on the slopes of several unconverged lines: 2/11,
  4/11, 5/11, 1/11, 3/10, 1/7, 2/7, 3/8, 4/9, 1/6 and 1/2. Each had a kernel with a small min(λ₊, λ₋) or an integer λ.
  It was not tabulated; the R read-out tabulates it on every line.
- **A timing call of this script's draft,** on (1/3, 1/4) at Re τ = 1/8 and Im τ = 48, 24 and 6.
  - It took 4.0, 1.2 and 0.6 s per point.
  - It printed each feature's status, not its value. One feature was zero at working precision at all three
    heights, under the draft's first zero test (below 10^{−0.8p}).
  - That test was then changed to the one above, because it would have called a real exponent above about 3.2 zero.
- **Not computed:** no six at any ladder height read as a value, no exponent, no skeleton test and no null.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
