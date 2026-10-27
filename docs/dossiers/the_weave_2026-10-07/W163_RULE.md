# W163 — the third opinion on main's B1755 (the six on the lines of order 13, 14, 15 and 20, this seat's test of the level-5 rung): the re-run, the χ² calibration on own code with two seed sets and a fresh one, the points and lines, the best rows on own instrument, and this seat's read of the per-line split (the rule, committed before the script)

The SM-derivation seat, 2026-10-27. Committed and pushed before the script that reads it exists. Nothing here is a
result.

> **Dated note (2026-10-27, before the script exists).** Two precisions, fixed after writing the script against
> main's files and before any run:
> - B1755's comparison.json stores, per class and menu, the mean fraction, the worst seed and the hit total, not each
>   seed's fraction (its compare.py, main()). So A1's "every per-seed fraction exact" and A2's "every per-seed fraction
>   equals comparison.json's exactly" are checked as those three numbers, exactly, per class. A2 also reports each
>   seed's own fraction.
> - FINDINGS prints order 14's fraction as 42.3%, to 0.1 points, so A2 checks it to 0.05 points, not 0.01.
>
> Nothing else changes.

## Why

- **Main's B1755** (sealed 2d6681208; census committed unread at aeaf72716, comparison at 3b9dda20d; read at S223)
  put B1749's 125 apex points on every line of exact order 13, 14, 15 and 20 (84 + 72 + 96 + 144 = 396; 49 500
  points), with B1741's instrument and measure unchanged and fresh seeds 1809–1828. The design was this seat's
  (§275); main set the decisive bar at 0.1%.
  - The decisive cell D held at the edge: on the orders 15 and 20 together 78 of 80 000 random hierarchies reach as
    low a χ²_six (the limit is 80); 4.94% on 13; 42.3% on 14. P1: 5.33.
  - Every line below the bar has α = 2/5, at four of ten offsets per order.
  - Main's referee: the cell does not separate the level-5 orders from any pool holding the order-15 α = 2/5 pair.
    The reading holds only through the slope. Not PASSED (r = 1.22 × 10⁻³, m = 40).
- **Main asks** (its handoff CC_TO_SM_2026-10-27_MAINS_PLAN_B1755_AND_THE_AGY_AUDIT.md, §2): "your third opinion,
  as W156 and W157 — reproduce, two seeds, and your read of the per-line split".
- **The plan** (`THE_NINETEEN_PLAN_2026-10-27.md`, adopted by the owner): every positive gets another seat's third
  opinion before any grade. Main's plan says the same.

## The objects

- **Main's committed files at 11ebe577b**, read with `git show`:
  - B1755's PREREGISTRATION, census.py, compare.py, census.jsonl, control.json, comparison.json, ARTIFACT_HASHES and
    FINDINGS;
  - every file its ARTIFACT_HASHES pins;
  - for C2, B1749's census.jsonl (pinned in W156: 667684c9…81d4), whose 266 lines sit at the same 125 points.
- **The pins,** computed from `git show` output for this rule:
  - census.jsonl sha256 2589220d…a6f8 (49 500 lines);
  - comparison.json f780fd37…dfb9;
  - control.json 19700264…21ee;
  - the instruments as ARTIFACT_HASHES states (census.py bd9f6aa5…, compare.py c96a47ae…).
- **The own code** (W157's, loaded unchanged and re-pointed where it can be):
  - W142's direct-sum χ² and σ, W138's draws, census loader and own instrument, W156's apex code;
  - an own enumeration of the lines of exact order 13, 14, 15 and 20 up to sign, written again.

  The script imports nothing of B1755's, B1749's, B1741's or B1726's code. The one exception is main's compare.py,
  which A1 runs in a temporary tree.

## Weave or thread

**A check of main's census on lines of four orders at the apexes of every primitive thread word of length 12.** The
positive sits on one slope of lines and a strip of τ: **a thread-and-frame result**, not a weave result. The claims are
about main's code, census and statements, about the frame's strip, and about the lines' arithmetic.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** census.jsonl, comparison.json and control.json match the pins. census.jsonl has 49 500 distinct (line, Re τ, Im τ) at 125 distinct points. Every file ARTIFACT_HASHES pins matches | 95% |
| A1 | **The re-run.** Main's compare.py, run once in a temporary tree at 11ebe577b, exits 0 and reproduces comparison.json: every cell identical, every per-seed fraction exact, every number to 10⁻¹⁰ relative (the comparison's own tolerance is 10⁻¹⁰; W157's A1 lesson) | 85% |
| A2 | **The χ² calibration on own code** (direct sums; the seat's menu; seeds 1809–1828, 4 000 targets each; own draws). For each class (13, 14, 15, 20, and 15 and 20) every per-seed fraction equals comparison.json's exactly, and the minima agree to 10⁻¹⁰ relative. On 15 and 20: the minimum 5.33 (to 0.01) with 78 of 80 000; on 13 4.94% and on 14 42.3% (each to 0.01 points); on 15 alone 30 of 80 000. χ²_nine under the seat's menu on 15 and 20 is 148.9 (to 0.5). Two seed sets reported apart: 1809–1818 and 1819–1828, 40 000 targets each, and seeds 1809 and 1828 alone | 80% |
| A2f | **A fresh seed set** (seeds 1829–1848, 80 000 more targets, the same own draws; a re-estimate of the Monte-Carlo spread, not a new look at the data, and B1755's sealed result stands on its own seeds). On 15 and 20 at most 0.1% are as low; on 13 and on 14 each more than 1% | 50% |
| A3 | **The points.** The 125 points of census.jsonl are exactly W156's own rebuild of B1749's apexes (Re τ and Im τ to 10⁻⁹) | 95% |
| A4 | **The lines.** The own enumeration gives 84, 72, 96 and 144 lines of exact order 13, 14, 15 and 20, equal to the census's line set in order. The lines of slope 2/5 (α = 3/5 stored as 2/5): none of order 13 or 14, ten of order 15 (b = k/15, 3 ∤ k) and ten of order 20 (b odd/20) | 95% |
| B0 | **The own instrument's controls at the best row** (0.5 + 3.0619i on (2/5, 14/15), L_max). The T-step image (τ + 1, (2/5, 8/15)) and the relabelling b → b + 1 (the same w) keep every ratio and ∣V∣ to 10⁻⁸ in log and J to 10⁻⁸ relative. The mirror image lies on (2/5, 2/3), equal in every ratio and ∣V∣ to 10⁻⁸ in log, with J flipped | 85% |
| B1 | **The rows on the own instrument.** The best row and its mirror, the best row of order 20 (on (2/5, 7/20) or its mirror (2/5, 1/4)), and the next three by χ²_six under the seat's menu. Every stored ratio and ∣V∣ above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative where ∣J∣ > 10⁻¹⁰ | 75% |
| C1 | **The rows below the bar** (own direct sums, the seat's menu). Every row of B1755's census with χ²_six below 16.75 lies on one of FINDINGS' eight lines, (2/5, b) with b ∈ {2/3, 14/15, 1/3, 4/15, 7/20, 1/4, 9/20, 3/20}, on L_max, at apex heights in [2.9, 3.2]. Read-out: their number, readings, c and heights | 75% |
| C2 | **This seat's read of the per-line split** (post hoc on per-line minima seen in FINDINGS; the rows' positions unseen). (i) **Exact.** On a line of slope α the frame depends on (τ, b) only through τ and w = ατ + b, and B1724's T-law identifies (τ, w) with (τ + 1, w); so on the slope-2/5 lines the six is one function F(x, y, u) of x = Re τ mod 1, y = Im τ and u = Re w mod 1. At each order (15, 20) the ten slope-2/5 lines form two T-law classes of five, and FINDINGS' four passing lines are two per class, the mirror exchanging the classes. (ii) **The prediction across orders.** At each of the 125 points the slope-2/5 rows of orders 10 (B1749's census), 15 and 20 sample F(x, y, ·) at 25 values of u. Interpolating log χ²_six linearly and periodically in u from the other two orders predicts each line's minimum over the points. From orders 10 and 15, the order-20 lines predicted below 16.75 are exactly FINDINGS' four (7/20, 1/4, 9/20, 3/20); from orders 10 and 20, the order-15 lines predicted below are exactly its four (2/3, 14/15, 1/3, 4/15) | (i) 95%; (ii) 35% each |
| C2r | **The ranks** (the same interpolation): the Spearman correlation between predicted and FINDINGS' per-line minima over the ten slope-2/5 lines is at least 0.6 at order 20 and at order 15 | 55% |
| C3 | **The referee's pools** (own code, the seat's menu, seeds 1809–1828). The orders 13, 14 and 15 pooled: 0.096% (to 0.01 points). Order 15 alone: 0.0375% (30 hits) | 80% |
| R | **Read-outs** (no prediction): the passing rows' positions (x, y, u), and 5u + 3x mod 1 at each (two best rows on record lie at ±1/6, below); the per-line minima reproduced; the halves' and the fresh set's hit counts | — |

## What the outcomes mean (fixed now)

- **A0 to A4, B and C1 hold.** B1755's numbers are reproduced by main's code and by a second code. Its points and
  lines are the stated ones, and its best rows reproduce on a second instrument. D's 78 of 80 000 stands as computed.
- **A2f.** Either way it measures the edge, and grades nothing. **Holds:** D also holds on 80 000 fresh targets.
  **Fails:** D's holding depends on the seed set, as main's "a fresh seed set could flip it" says. B1755's sealed
  verdict is unchanged either way (the audit lane's guard: an earlier outcome is kept, not replaced).
- **C2 (ii) holds** (both orders predicted). The per-line split is the sampling of one smooth function F(x, y, u) by
  the 125 points. A slope-2/5 line passes when some point puts (x, u) in F's valley at the strip's height. So "four
  of ten offsets" is not a property of the offset alone. It is a property of the pair (point, line). An offset rule
  must then be a rule on u relative to x and y: a relation between the line and τ, the pair that W162's rule names.
- **C2 (ii) fails.** F varies on a finer scale in u than the orders' samples (about 0.13 apart) resolve, or the split
  carries structure beyond the sampling. Main's statement of the offset question stands as main wrote it.
- **This seat's opinion (fixed now).** If A1, A2, B1, C1 and C3 hold, this seat agrees with main's scope:
  - the level-5 rung's prediction (this seat's own, §275) holds only through the slope: the orders that pass are those
    that contain slope-2/5 lines, and the 13/14 half was nearly certain once the slope was known;
  - the result is ungraded, a READING, as main banks it;
  - the look count: A0–A4, B, C1 and C3 are verifications, not new looks; A2f re-estimates the measure; C2 is a post
    hoc view of the same data and counts as a look for any later test it informs.
- **Any other cell fails:** the failure is the finding, and it is diagnosed before anything else is said.

## What stays out

- New frame values at new points: none is computed, except B0's three control images (equalities, not looks).
- B1755's nine beyond A2's minimum; the random-subset read-out beyond C3's pools; the offset question itself, which is
  main's (its plan's division); W162, a separate arc whose output is not read here.

## Seen before the rule (disclosed)

- **Read on main:**
  - B1755's PREREGISTRATION and FINDINGS in full (the cells, the per-line minima, the best row, the referee's pools,
    the grade);
  - census.py and compare.py in full; ARTIFACT_HASHES;
  - the handoff CC_TO_SM_2026-10-27_MAINS_PLAN_B1755_AND_THE_AGY_AUDIT.md;
  - this seat's earlier finding that main's and the agy branch's B1755 census and comparison files are byte-identical
    (§287, §291).
- **Read for the pins:** census.jsonl's line count and sha256, its rows' keys, its 125 points with Re τ in [0, 0.984]
  and Im τ in [2.010, 3.582], and 20 points in [2.9, 3.2]. No frame value in it was read.
- **The web seat's facts** (its relay of 2026-10-27 on P-389, read before this rule): on the (2/5, k/10) lines the
  T-step and b → b ± 1 leave the mass ratios unchanged to 3 × 10⁻¹⁰ and J to 3 × 10⁻¹⁴ (its e20c and e20d).
- **A two-point observation, by hand, from FINDINGS' and B1753's best rows.** With u = Re w = (2/5)Re τ + b:
  - B1753's best row (1/3 + 3.037i on (2/5, 1/10)) has 5u + 3x = 7/6 + 1, so 1/6 mod 1;
  - B1755's best row (1/2 + 3.062i on (2/5, 14/15)) has 5u + 3x = 43/6, also 1/6 mod 1;
  - their mirrors give −1/6.

  5u + 3x mod 1 is a class invariant under the T-law. Since all five members of a class share it at a point, it
  cannot decide the split by itself. It enters only as a read-out.
- **Not run:** no script exists. No value of comparison.json, control.json, census_run.txt or compare_run.txt beyond
  what FINDINGS prints was read.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
