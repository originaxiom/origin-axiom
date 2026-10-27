# W164 — the third opinion on main's B1786 (the slope principle out of sample, the lines of order 25 and 30): the calibration on own code with main's seeds and fresh ones, the class-choosing null on own code, the points and lines, the best rows on own instrument, and this seat's read of the offset pairs (the rule, committed before the script)

The SM-derivation seat, 2026-10-27. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1786** (sealed 11ebe577b; census 4b5d8c602 and comparison c31c4d0e1, each committed unread; read at S225)
  put B1749's 125 apex points on every line of exact order 25 and 30 (300 + 288 = 588; 73 500 points). It used B1741's
  instrument and measure unchanged, with fresh seeds 1829–1868 (160 000 targets).
  - The decisive cell D held as sealed: on the 30 slope-2/5 lines, 8 of 160 000 random hierarchies reach as low a
    χ²_six (3.005), and no line of any other slope has a row below 16.75. The slope 1/10 bottoms out at 919, the rest at
    103.
  - Main's referee: under the class-choosing null, in which random targets may choose their own slope class, m·r is
    0.0112 at m = 41 and 0.0199 at 73. **Not PASSED; it sits on the gate.**
  - Twelve of the 30 lines carry the six, in pairs b ↔ 3/5 − b, the record's mirror.
- **Main asks** (its handoff CC_TO_SM_AND_CHAT1_2026-10-27_B1786_THE_SLOPE_OUT_OF_SAMPLE.md, §1): "your third opinion,
  as W157 and W163. Reproduce on your own instrument with your own seeds. Please also give your read of the offset pairs
  (which offsets carry the six)". THE_BAR asks for a third opinion before any grade.
- **The plan** (`THE_NINETEEN_PLAN_2026-10-27.md`, adopted by the owner): every positive gets another seat's third
  opinion before any grade.

## The objects

- **Main's committed files at 8ca002cd1**, read with `git show`:
  - B1786's PREREGISTRATION, FINDINGS, census.py, compare.py, census.jsonl.gz, census.jsonl.sha256, control.json,
    comparison.json and ARTIFACT_HASHES;
  - every file ARTIFACT_HASHES pins;
  - for C2, B1749's and B1755's census.jsonl (pinned in W156 and W163).
- **The pins,** computed from `git show` output for this rule:
  - census.jsonl.gz sha256 5acb140b…b3bf9;
  - census.jsonl.sha256 9ceece3a…de974, whose content pins the decompressed census;
  - comparison.json 6da87499…a1cb; control.json 4ad1c0a9…b7ac;
  - the instruments as ARTIFACT_HASHES states (census.py b1fb5c87…, compare.py d38205f7…).
- **The own code:** W163's and W157's, loaded unchanged (W142's direct-sum χ² and σ, W138's draws, census loader and own
  instrument, W156's apex code), and an own enumeration of the lines of exact order 25 and 30, written again.
- **No re-run of main's compare.py.** Main asks for own instrument and own seeds. Main's referee already recomputed the
  counts in independent code. W163's re-run took 47 minutes, and two of its launches were lost to container restarts.
- **One pass per seed.** For every target and every one of the 26 slope classes present at orders 25 and 30, the least
  χ²_six over the class's rows (the seat's menu, both horocycles; own direct sums, own draws). Every count below is
  read from these minima:
  - main's seeds 1829–1868 (160 000);
  - fresh seeds 1869–1928 (240 000), of which 1869–1908 serve A2f.
- **Resumable.** Each seed's minima are saved to a cache outside the repository as soon as the seed is done. A restart
  resumes from the saved seeds. The minima are deterministic, so a resumed run computes what one run would.

## Weave or thread

**A check of main's census on lines of two orders at the apexes of every primitive thread word of length 12.** The
positive sits on one slope and a strip of τ: **a thread-and-frame result.** The claims are about main's code, census and
statements, about the frame's strip, and about the lines' arithmetic.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** census.jsonl.gz, census.jsonl.sha256, comparison.json and control.json match the pins, and the decompressed census matches census.jsonl.sha256. It has 73 500 distinct (line, Re τ, Im τ) at 125 points. Every file ARTIFACT_HASHES pins matches | 95% |
| A2 | **The calibration on own code, main's seeds** (1829–1868). For each of main's classes (slope 2/5, slope 1/10, the rest, all) the mean fraction, the worst seed and the hits equal comparison.json's exactly (the seat's menu), and the minima agree to 10⁻¹⁰ relative. On the slope 2/5: 3.005 (to 0.001) and 8 of 160 000. The slope 1/10's minimum is 919 and the rest's 103 (each to 1). Read-out: the seed halves 1829–1848 and 1849–1868 apart | 80% |
| A2f | **Fresh seeds** (1869–1908, 160 000). On the slope 2/5 at most 0.1% of random hierarchies reach 3.005 or below (D's first half; its second half is a property of the data) | 90% |
| C3 | **The class-choosing null on own code** (fresh seeds 1869–1928, 240 000). The fraction of targets for which some slope class reaches 3.005 or below while every other class stays at 16.75 or above lies within 2.5 binomial σ of main's referee's 2.62 × 10⁻⁴, that is in [1.79, 3.45] × 10⁻⁴. Read-outs: the fraction for which any class reaches 3.005 (the referee: 4.18 × 10⁻⁴), and the share of those events on the slope 2/5 (the referee: 11%) | 80% |
| A3 | **The points.** The 125 points are W156's own rebuild of B1749's apexes, and equal B1749's census points | 95% |
| A4 | **The lines.** The own enumeration gives 300 and 288 lines of exact order 25 and 30, 26 slope classes, and the census rows carry these lines. Slope 2/5: 20 at order 25 (b = k/25, 5 ∤ k) and 10 at order 30 (gcd(k, 6) = 1). Slope 1/10: 20 at order 30 | 95% |
| B0 | **Controls at the best row** (0.2692 + 3.0375i on (2/5, 23/30), L_max). The T-step image and b → b + 1 keep every ratio and ∣V∣ to 10⁻⁸ in log and J to 10⁻⁸ relative. The mirror image lies on (2/5, 5/6) at 0.7308 + 3.0375i, equal to 10⁻⁸, with J flipped | 85% |
| B1 | **The rows on own instrument.** The best row, its mirror, and the next four by χ²_six (the seat's menu) reproduce every stored ratio and ∣V∣ above 10⁻¹⁰ to 10⁻⁶ in log, and J to 10⁻⁵ relative | 80% |
| C1 | **The rows below the bar.** Every row of B1786's census with χ²_six below 16.75 lies on a slope-2/5 line at one of FINDINGS' twelve offsets (order 25: b = 3, 4, 11, 12, 17, 19, 21, 23 over 25; order 30: 1/6, 13/30, 23/30, 5/6), at apex heights in [2.9, 3.2]. Read-out: their number, horocycles, readings and c | 85% |
| C2 | **The offset pairs.** (i) **Exact:** the record's mirror sends (2/5, b) at Re τ = x to (2/5, 3/5 − b) at 1 − x (the mirror −b, then one T-step), so the twelve lines are six mirror pairs. (ii) **The points (prediction):** every apex point that carries a row below the bar at orders 25 or 30 also carries one on a slope-2/5 line at orders 10, 15 or 20 (B1749's and B1755's censuses) | (i) 95%; (ii) 70% |
| R | **Read-outs** (no prediction): at each apex point that carries a row below the bar at any order, the six over u = Re w from every slope-2/5 line of orders 10, 15, 20, 25 and 30 (55 values per point); the passing rows' (x, y, u) | — |

## What the outcomes mean (fixed now)

- **A0–A4, B and C1 hold.** B1786's numbers are reproduced by a second code with its own draws. Its points and lines
  are the stated ones, and its best rows reproduce on a second instrument. 8 of 160 000 stands as computed.
- **A2f holds:** D's specificity also holds on fresh targets. It re-estimates the measure; main's sealed verdict is
  unchanged either way.
- **C3 holds:** main's referee's class-choosing fraction is reproduced by an independent code with fresh draws. The
  grade then stays where the referee put it, on the gate at m = 41 and failing at m = 73, so not PASSED.
  **C3 fails:** the fraction differs. That is diagnosed before anything else is said, since it decides the grade.
- **C2 (ii) holds:** at orders 25 and 30 the six live at the same apex points as at the lower orders. With W163's fine
  structure in Re w, the offsets that carry the six are those that put Re w into the narrow valleys at those points.
  The offset question becomes "where are the valleys in Re w at the strip's points". **C2 (ii) fails:** new points
  carry the six at the new orders, and the valleys move with the order's sampling.
- **This seat's opinion (fixed now).** If A2, B1, C1 and C3 hold, this seat agrees with main's scope: a selection by
  the data, stable out of sample, not a derivation; ungraded, a READING. The look count: A0–A4, B, C1 and C3 are
  verifications; A2f re-estimates the measure; C2 (ii) and the read-outs are a look for any later test they inform.
- **Any other cell fails:** the failure is the finding, and it is diagnosed before anything else is said.

## What stays out

- A re-run of main's compare.py; the nine beyond the read-outs; the random-subset control; the other forms of the
  class-choosing null (the class chosen as the data chose it); new frame values at new points, except B0's three control
  images.

## Seen before the rule (disclosed)

- **Read on main:**
  - B1786's PREREGISTRATION and FINDINGS in full (the cells, the best row, the twelve offsets, the mirror pairs, the
    referee's nulls and the grade);
  - compare.py's first 80 lines (its classes and loader); ARTIFACT_HASHES;
  - the handoff CC_TO_SM_AND_CHAT1_2026-10-27_B1786_THE_SLOPE_OUT_OF_SAMPLE.md.
- **From W163's read-out:** B1749's census has a row below the bar at 0.2692 + 3.0375i (3.62 on (2/5, 1/10)), the apex
  of B1786's best row. So C2 (ii) is known to hold at that point.
- **By hand:** the 588 lines, their 26 slope classes and the 30 slope-2/5 offsets; the mirror as −b followed by one
  T-step.
- **Not read:** no value of census.jsonl.gz, comparison.json, control.json, census_run.txt, compare_run.txt,
  compare_run_interrupted.txt or the referee's outputs beyond what FINDINGS prints.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read. A resumed run after a restart is the same run, and is disclosed.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
