# W156 — the third opinion on main's B1749 (the six at fresh apexes): the re-run, the χ² calibration on own code, the apex points and their freshness on own code, the best rows on own instrument, the strip, its width on own instrument, and the sensitivity (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1749** (sealed 32f29ad98; census committed unread at 53ab50676, comparison at 537662002; read at S217)
  put τ at the 125 distinct apex points of the 238 primitive thread words of length 12 with apex height in [2.0, 3.6],
  on all 266 lines, with B1741's instrument and measure unchanged and fresh seeds 1769–1788.
  - The decisive cell P2 held: 0.02% of random hierarchies reach as low a χ²_six under the seat's menu (worst seed
    0.08%). P1: 3.57 < 16.75.
  - Main's referee found the good rows form one strip, Im τ 2.96–3.11 on the order-10 lines (2/5, b), which random
    125-point sets in the band find 99.7% of the time. Main banks the scope "a property of B1656's frame on its strip,
    with c = 3 and the seat's reading, not evidence that the thread rule selects τ".
- **Main asks, as for W145** (its handoff of 2026-10-24, §1): reproduce on this seat's code and instrument; two seeds
  independently; the freshness; and an opinion on the scope. THE_BAR's grade waits for it.
- **The owner's word:** "lets do themall" (2026-10-24), which named main's asks among the work.

## The objects

- **Main's committed files at f3038f81b**, read with `git show`:
  - B1749's PREREGISTRATION, census.py, compare.py, census.jsonl, control.json, comparison.json, posthoc_read.py and
    FINDINGS;
  - every file its ARTIFACT_HASHES pins (B1741's compare.py and census.jsonl, B1726's census.py and census.jsonl,
    b1656_funcs and its dependencies, B1667's cusp file, B1720's thread_geometry.py, the two data files).
- **The pins,** computed from `git show` output for this rule: census.jsonl sha256 667684c9…81d4 (33 250 lines),
  comparison.json 6d91c69d…a005c, control.json bf2740c5…99cc; the rest as ARTIFACT_HASHES states.
- **The own code** (W145's, unchanged where it can be):
  - W142's direct-sum χ² and σ; W138's draws, census loader and own instrument (`own_point`); W141's Smith rule;
    W140's 266 lines;
  - for the apexes, own code: the primitive necklaces of length n over {L, R} (rotation classes, both letters
    present); for each word, the axis semicircles ((a − d)/2c, √(t² − 4)/(2|c|)) of the matrices of all its rotations
    and of their conjugates by S; the word's height is the largest radius, checked against the run-length Lagrange
    value over 2 computed independently, and its top points are the centers (Re τ mod 1) of every semicircle of that
    radius.
  The script imports nothing of B1749's, B1741's or B1726's code, except main's compare.py, which A1 runs in a
  temporary tree.

## Weave or thread

**A check of main's census over the apexes of every primitive thread word of length 12.** The input set spans the
threads, but the positive sits on a strip of τ on two mirror lines: **a thread-and-frame result**, not a weave result.
The claims are about main's code, census and statements, and about the frame's strip.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** census.jsonl, comparison.json and control.json match the pins; census.jsonl has 33 250 distinct (line, Re τ, Im τ); every file ARTIFACT_HASHES pins matches | 95% |
| A1 | **The re-run.** Main's compare.py, run once in a temporary tree at f3038f81b, exits 0 and reproduces comparison.json: every cell identical, every per-seed fraction exact, every minimum to 10⁻¹² relative | 85% |
| A2 | **The χ² calibration on own code** (direct sums; the seat, covariant and free menus; seeds 1769–1788, 4 000 targets each; own draws). Every per-seed fraction equals comparison.json's exactly, the minima agree to 10⁻¹⁰ relative, and χ²_nine is 191.84 (seat) and 1 278.85 (the Standard Model's reading) to 10⁻⁶ relative. Seeds 1769 and 1788, the two main's referee recomputed, are reported apart | 85% |
| A3 | **The apex points on own code.** (i) Control: for each of B1720's 121 stored class words the own height equals the stored Im τ to 10⁻⁹, and the stored Re τ mod 1 is one of the word's own top points. (ii) There are 335 primitive necklaces of length 12, and 238 have height in [2.0, 3.6]. (iii) census.jsonl has 125 distinct points; for every word it lists at a point, the own height equals the point's Im τ to 10⁻⁹ and the point's Re τ mod 1 is one of the word's top points; and the words it lists are exactly the 238 | 80% |
| A3f | **The freshness on own code.** None of the 125 lies within 10⁻⁶ of any top point of any primitive word of length 2 to 11 with height in [2.0, 3.6], under Re τ mod 1 and the mirror Re τ ↦ −Re τ. Read-out: the number of mirror pairs among the 125 (main's referee: 51 pairs and singles, about 74 independent) | 90% |
| A4 | **The lines.** census.jsonl's line indices are 0–265 at every apex, and its lines are W140's 266 up to sign | 90% |
| B0 | **The own instrument's controls at the best six-row.** Residues match the re-implemented bilinear to 10⁻¹⁰ relative and W96's J1 holds to 10⁻¹⁰‖Y‖³. At the best row, B1724's T-law image keeps J (to 10⁻⁸ relative) and the mirror image flips it (relative difference 2 to 10⁻⁸), with every ratio and ∣V∣ equal to 10⁻⁸ in log | 85% |
| B1 | **The rows on the own instrument:** the best six-row (0.3333 + 3.0551i on (2/5, 1/10), L_max), its mirror (0.6667 + 3.0551i on (2/5, 1/2)), the best by the largest factor (0.6053 + 3.0259i on (2/5, 1/2)) and the next four by χ²_six under the seat's menu. Every stored ratio and ∣V∣ above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative where ∣J∣ > 10⁻¹⁰ | 75% |
| B2 | **The best six-row from own values:** χ²_six 3.57 to 10⁻³ relative of the stored row's, the pulls to 10⁻³, and D = 10.94 to 10⁻³ relative | 75% |
| C1 | **The strip in the census (own direct sums).** Exactly 12 rows have χ²_six below 16.75 under the seat's menu, all on the lines (2/5, 1/10) and (2/5, 1/2), all on L_max, all with (S̃, S, S) and c = 3, at apex heights 2.961–3.119 | 85% |
| C2 | **The strip's width on own instrument.** Along the line (2/5, 1/10) at Re τ = 0.1, 0.3, …, 4.9 (by B1724's T-law, (τ, (2/5, b)) ~ (τ + 1, (2/5, b − 2/5)), so this covers all five lines (2/5, b), b ≡ 1/10 mod 2/5, at the residues 0.1, 0.3, 0.5, 0.7, 0.9 of Re τ mod 1), Im τ from 2.0 to 3.6 in steps of 0.02, L_max, the seat's menu. The points with χ²_six < 16.75 form, at each Re τ where any exist, one interval in Im τ inside [2.80, 3.30]; every such Re τ lies in [0, 2] (C1's two lines); at least four of the five residues are covered by some line. With p the covered fraction of [0, 1) × [2.0, 3.6] (a point counts if any of the five lines is below the bar there), 1 − (1 − p)^125 ≥ 0.99: a random 125-point set in the band reaches the bar almost surely | 70% |
| D1 | **Sensitivity** (labelled; the seat's menu; seeds 1769–1788; own code), against main's referee: allowance 0.05: minimum χ²_six 5.09 to 1%; uniform σ 0.10: minimum 7.72 to 1%, fraction at most 0.1%; the lepton factor over {1, …, 5}: fraction at most 0.1%; c = 1 alone: minimum 125.8 to 1% | 75% |

## What the outcomes mean (fixed now)

- **A0 to A4, B and C1 hold.** B1749's χ² minimum and calibration are reproduced by main's code and by a second
  code, its points are the stated fresh apexes, and its best rows reproduce on a second instrument. 3.57 and 0.02%
  stand as computed, on fresh points.
- **C1 and C2 hold.** The good rows are one strip of the frame, about Im τ ≈ 3.0 on the T-orbit of (2/5, 1/10), which
  almost any point set in the band reaches. So the specificity belongs to the frame's strip, given c = 3 and the
  seat's reading. The thread rule is not tested by it.
- **D1 holds.** The match survives a 5% allowance and a uniform σ, and rests on c = 3.
- **This seat's opinion (fixed now).** If A1, A2, B1, C1 and C2 hold, this seat agrees with main's scope:
  - B1741's six-ratio specificity replicates on fresh points (p ≈ 2 × 10⁻⁴), as a property of B1656's frame on its
    Im τ ≈ 3.0 strip on the order-10 lines (2/5, b), with c = 3 and the reading rule, both by hand;
  - it is not evidence that the thread rule selects τ, and the nine fail at the strip's best row (∣V_ud∣ 0.115);
  - the mirror pair on the strip carries both signs of J, so the strip fixes no CP sign (B1750);
  - it is a value-level READING of a region of τ, bankable as that and no more. What fixes Im τ ≈ 3.03 is P-373's
    question, the open one.
- **C2 fails.** If the strip covers the band too little for random sets to find it, the thread rule may carry
  information after all: the finding, diagnosed before anything else is said.
- **Any other cell fails:** the failure is the finding, and it is diagnosed before anything else is said.

## What stays out

- B1749's nine beyond A2's minima; the web seat's tests; P-373 itself (whether the level-5 structure singles out
  these lines), which is the next arc; the frame itself.

## Seen before the rule (disclosed)

- **Read on main:** B1749's PREREGISTRATION and FINDINGS in full (its best rows, its referee's table, the strip's
  heights, the scope); census.py's and compare.py's headers and loaders; posthoc_read.py's header; ARTIFACT_HASHES; the
  handoff CC_TO_SM_2026-10-24_B1749_THE_THIRD_OPINION_ASKED.md.
- **Seen by accident while checking timing:** compare_run.txt's last three lines (six|free 3.18 and 0.0024; nine|seat
  191.84 and 0.0306; nine|sm 1 278.85 and 0.1899).
- **Not read:** no value of census.jsonl, comparison.json or control.json beyond what FINDINGS and those lines print.
  Their sha256 was computed from `git show` output.
- **Read on main for the apex rule:** B1720's thread_geometry.py, its necklaces, runs, lagrange and representative
  (rotation classes; the Lagrange value from the run lengths; a breadth-first search over conjugates that keeps the
  first semicircle of the largest radius, so a word with two tops of equal height gets one of them).
- **By hand:** the count of primitive necklaces of length 12, (2¹² − 2⁶ − 2⁴ + 2²)/12 = 335; the T-orbit
  b ≡ 1/10 mod 2/5, under which (2/5, 1/2) at Re τ is (2/5, 1/10) at Re τ + 1; the C2 estimate (FINDINGS' 12 rows at
  Re τ 0.12–0.86 on both lines put the strip on (2/5, 1/10) at Re τ in about [0.1, 1.9]; a width of about 0.15 in Im τ
  gives p near 0.09, and 1 − 0.91¹²⁵ is 1 to many digits). A first draft of this cell asked for the strip at 15 of
  the 25 values of Re τ along one line; the estimate above gives about 10, and the cell was reworded per residue
  before the commit.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
