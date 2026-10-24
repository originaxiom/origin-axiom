# W157 — the third opinion on main's B1753 (the six on the five-ality lines): the re-run, the χ² calibration on own code, the apex points and their freshness, the lines, the best rows on own instrument, the line classes under B1724's T-law, the restriction priced on B1749's census, and the sensitivity (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1753** (sealed 33b197340; census committed unread at 26c714d8a, comparison at e5a942a98; read at S220)
  put τ at the 223 distinct apex points of the primitive thread words of length 13 with apex height in [2.0, 3.6],
  on the 48 of B1713's 266 lines whose order is divisible by 5 (orders 5 and 10), with B1741's instrument and measure
  unchanged and fresh seeds 1789–1808. The rule was stated before the run from B1728's law: 6Y mod 5 is the SU(5)
  multiplet label.
  - The decisive cell P2 held: 7 of 80 000 random hierarchies (0.009%) reach as low a χ²_six under the seat's menu.
    P1: 2.74.
  - Main's referee found the line rule mostly a pick. Every simple order rule, and every random 48-line subset, that
    contains the order-10 lines (2/5, 1/10) and (2/5, 1/2) passes; none without them does. The outcome was foreknown,
    and the look count is fragile (51–52 under the ledger's definition, 68 inclusive). A fair null, in which each
    random target may choose its line class, falls back toward the all-lines rarity. Main banks it ungraded, as a
    READING, and names the open question P-384: what selects the line class (2/5, odd/10).
- **Main asks, as for W145 and W156** (its handoff CC_TO_SM_2026-10-24_B1753_AND_THE_LITERATURE.md, §1):
  - reproduce on this seat's code and instrument;
  - two seeds independently;
  - the freshness;
  - this seat's opinion of the line rule (a genuine restriction or a disguised pick) and of the look count.

  THE_BAR's grade waits for it.
- **The owner's word:** "lets do themall" (2026-10-24), which named main's asks among the work.

## The objects

- **Main's committed files at 0c9d60a5f**, read with `git show`:
  - B1753's PREREGISTRATION, census.py, compare.py, census.jsonl, control.json, comparison.json, ARTIFACT_HASHES and
    FINDINGS;
  - every file its ARTIFACT_HASHES pins;
  - for C3, B1749's census.jsonl (pinned in W156: 667684c9…81d4).
- **The pins,** computed from `git show` output for this rule:
  - census.jsonl sha256 c7f58dce…0c69 (10 704 lines);
  - comparison.json 8074b69b…7b47;
  - control.json 865bb71c…1154;
  - the instruments as ARTIFACT_HASHES states (census.py 7afe5a05…, compare.py 4ebaccfa…).
- **The own code** (W156's, loaded unchanged and re-pointed where it can be):
  - W142's direct-sum χ² and σ, W138's draws, census loader and own instrument (`own_point`), W140's 266 lines;
  - W156's apex code (primitive necklaces, axis semicircles of the rotations and their S-conjugates, run-length
    Lagrange values).

  The script imports nothing of B1753's, B1749's, B1741's or B1726's code. The one exception is main's compare.py,
  which A1 runs in a temporary tree.

## Weave or thread

**A check of main's census over the apexes of every primitive thread word of length 13, on the lines of orders 5 and
10.** The input set spans the threads, but the positive sits on one class of lines and a strip of τ: **a
thread-and-frame result**, not a weave result. The claims are about main's code, census and statements, about the
frame's strip, and about the lines' classes, which are exact arithmetic.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** census.jsonl, comparison.json and control.json match the pins. census.jsonl has 10 704 distinct (line, Re τ, Im τ). Every file ARTIFACT_HASHES pins matches | 95% |
| A1 | **The re-run.** Main's compare.py, run once in a temporary tree at 0c9d60a5f, exits 0 and reproduces comparison.json: every cell identical, every per-seed fraction exact, every number to 10⁻¹⁰ relative. (W156's A1 failed as worded at 2.3 × 10⁻¹² against 10⁻¹², the environment's last digits; the bar is 10⁻¹⁰ for that reason) | 90% |
| A2 | **The χ² calibration on own code** (direct sums; the seat, covariant and free menus; seeds 1789–1808, 4 000 targets each; own draws). Every per-seed fraction equals comparison.json's exactly, and the minima agree to 10⁻¹⁰ relative. The seat's minimum is 2.74 (to 0.01), with 7 of 80 000 (worst seed 1 of 4 000, 13 seeds at 0). χ²_nine under the seat's menu is 183 (to 0.5), and both nine minima (seat; the Standard Model's reading) equal comparison.json's to 10⁻⁶ relative. Seeds 1789 and 1808 are reported apart | 85% |
| A3 | **The apex points on own code.** (i) Control: for each of B1720's 121 stored class words the own height equals the stored Im τ to 10⁻⁹, and the stored Re τ mod 1 is one of the word's own top points. (ii) There are 630 primitive necklaces of length 13, and 446 have height in [2.0, 3.6]. (iii) census.jsonl has 223 distinct points. For every word it lists at a point, the own height equals the point's Im τ to 10⁻⁹ and the point's Re τ mod 1 is one of the word's top points. The words it lists are exactly the 446 | 80% |
| A3f | **The freshness on own code.** None of the 223 lies within 10⁻⁶ of any top point of any primitive word of length 2 to 12 with height in [2.0, 3.6], under Re τ mod 1 and the mirror Re τ ↦ −Re τ. Read-outs: the mirror pairs among the 223 (main's referee: 129 independent mirror orbits, so 94 pairs) and the nearest older top point (main's referee: 0.0148 from a B1749 point) | 90% |
| A4 | **The lines.** At every apex census.jsonl's line indices are exactly the 48 indices k of B1713's order (W138's `own_lines`) whose line has order divisible by 5. They are W140's lines of order 5 (12) and 10 (36) up to sign. Main's lines() equals `own_lines` in order | 90% |
| B0 | **The own instrument's controls at the best six-row.** Residues match the re-implemented bilinear to 10⁻¹⁰ relative, and W96's J1 holds to 10⁻¹⁰‖Y‖³. At the best row, B1724's T-law image keeps J (to 10⁻⁸ relative) and the mirror image flips it (relative difference 2 to 10⁻⁸), with every ratio and ∣V∣ equal to 10⁻⁸ in log | 85% |
| B1 | **The rows on the own instrument.** The rows: the best six-row (0.3333 + 3.0368i on (2/5, 1/10), L_max), its mirror (0.6667 + 3.0368i on (2/5, 1/2)), the best by the largest factor (0.6 + 3.0397i on (2/5, 1/2)), and the next four by χ²_six under the seat's menu. Every stored ratio and ∣V∣ above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative where ∣J∣ > 10⁻¹⁰ | 75% |
| B2 | **The two named rows from own values.** At the χ²-best row: χ²_six 2.74 (to 10⁻³ relative of the stored row's), the pulls to 10⁻³, and D = 10.75 (to 0.01; main's referee's value at this row). At the row best by the largest factor: model over measured 1.17, 0.90, 1.15, 1.06, 1.08, 0.97 in the targets' order (c/t, u/t, s/b, d/b, μ/τ, e/τ), each to 0.005, and D = 10.92 (to 0.01; the value R7 reads) | 75% |
| C1 | **The rows below the bar (own direct sums, the seat's menu).** Every row of B1753's census with χ²_six below 16.75 lies on (2/5, 1/10) or (2/5, 1/2), on L_max, with (S̃, S, S) and c = 3, at apex heights in [2.90, 3.20]. Read-out: their number and heights | 85% |
| C2 | **The line classes (exact; own code).** (i) Under B1724's T-law, (τ, (α, b)) ~ (τ + 1, (α, b − α)), with lines up to sign, the 48 lines fall into 12 classes: of order 5, sizes 1, 1, 5, 5; of order 10, sizes 1, 1, 2, 2, 5, 5, 10, 10. The 266 lines fall into 64 classes. (ii) In B1753's census and in B1749's (all 266 lines), every row below the bar lies in one class, {(2/5, b) : b = 1/10, 3/10, 1/2, 7/10, 9/10}. (iii) With the charges 6Y = (Q 1, u −4, d 2, L −3, e 6, H 3), the α-twist ∣6Y α∣ (mod 1, reduced to [0, ½]) in that class is 2/5 on Q, u and e (SU(5)'s 10) and 1/5 on d, L and H (the 5̄ and the 5). The twist (6Y α, 6Y b) has order 10 on the doublets (Q, L, H) and order 5 on the singlets, on every line of the class. Multiplying the line by 3, a unit mod 10, maps the class to {(1/5, b) : b odd/10}, where the α-twists are exchanged (1/5 on the 10, 2/5 on the 5̄ and the 5). Read-out (post hoc): the minimum χ²_six per class in both censuses, ranked | 90% |
| C3 | **The restriction priced on B1749's census** (own code, the seat's menu, B1749's seeds 1769–1788, data and random targets restricted to the same lines; main's post hoc pricing reproduced). All 266 lines: 3.57 and 16 of 80 000 (W156). The 48 lines of orders 5 and 10: 3.57 and 2 of 80 000. Order 10 alone: 3.57 and 1 of 80 000. Order 5 alone: 20.78 (to 0.01), and 0.19% (to 0.02 points). Read-out: orders divisible by 2 | 75% |
| D1 | **Sensitivity** (labelled; the seat's menu; seeds 1789–1808; own code), against main's referee. c = 1 alone: minimum χ²_six 154.2 (to 1%), and a fraction of 19.1% (to 1.5 points). Read-outs, with no prediction: allowance 0.05; a uniform σ of 0.10; the lepton factor over {1, …, 5} | 75% |

## What the outcomes mean (fixed now)

- **A0 to A4, B and C1 hold.** B1753's minimum and calibration are reproduced by main's code and by a second code.
  Its points are the stated fresh apexes, its lines the stated 48, and its best rows reproduce on a second
  instrument. 2.74 and 0.009% stand as computed.
- **C2 and C3 hold.** The line rule's content is one class of lines.
  - On both censuses the good rows sit in one T-law class of 12 among the five-ality lines (64 among all), the class
    (2/5, odd/10).
  - Restricting to the 48 lines cuts the random hits by 8 on B1749's points. A null that lets each random target
    choose its order rule returns to the all-lines rarity, since the rules' union is every line.
  - So "divisible by 5" does not select; the class does.
- **This seat's opinion (fixed now).** If A1, A2, B1, C1, C2 and C3 hold, this seat agrees with main's scope:
  - **The line rule.** The five-ality rule is structure, but as a test of a principle it is a pick in effect.
    - The structure: 6Y mod 5 is the SU(5) label, and a rule by order is the most the weave could ever supply, since
      the weave sees a line's order, never the line (W140; the reading of §275).
    - Why a pick: the data choose one class of the 12. What remains is three discrete choices, none forced by
      anything on record:
      - that the α-direction carries SU(5)'s centre alone: α of order 5, not 0, ½ or of order 10;
      - which power of it: the 10 at 2/5, against its partner under the unit 3, where the 5̄ and the 5 are at 2/5;
      - that the line has order 10 (the doublets' twists of order 10), not 5.
    - Under R1 the level-5 rung is one rung among four (N = 2, 3, 4, 5). Restricting to it alone is a thread-type
      choice of rung, not a weave rule.
    - P-384 is then sharpened: what selects the class (2/5, odd/10) is what selects these three choices.
  - **The look count.** This seat agrees with the ledger's definition: sealed decisive cells, and the post hoc scans
    that informed a later test. W145, W156 and this W157 are verifications, not new looks. C3 reproduces main's
    order5_restriction row, already in the ledger. C2's per-class read-out is a post hoc view of the same data; it
    counts as a look for any later test it informs.
  - **The grade.** With the fair null the break-even is near 10 looks (main's referee), below any count on record (28
    listed, 51–52 completed). So the result is ungraded, a READING. The nine fail, and c = 3 and the reading rule
    stay by hand.
- **C2 (ii) fails.** If good rows sit in more than one class, the line rule may carry more than one pick. That is the
  finding, diagnosed before anything else is said.
- **C3 fails.** If the restriction's price on B1749's points differs from main's post hoc pricing, either main's
  disclosure or this seat's code is wrong. That is diagnosed first.
- **Any other cell fails:** the failure is the finding, and it is diagnosed before anything else is said.

## What stays out

- New frame values at new points: no point outside B1753's and B1749's censuses is computed, except the two control
  images of B0 (equalities, not looks).
- B1753's nine beyond A2's minima; the fair null on B1753's own points over all 266 lines, which would need new
  frame values (main's referee estimates 0.06–0.09%); P-384 itself, beyond C2's arithmetic; the frame itself.

## Seen before the rule (disclosed)

- **Read on main:**
  - B1753's PREREGISTRATION and FINDINGS in full (its best rows, the referee's table, D at the two rows, the grade);
  - census.py in full and compare.py's first 80 lines (the loader and the cells);
  - ARTIFACT_HASHES;
  - the handoffs CC_TO_SM_2026-10-24_B1753_AND_THE_LITERATURE.md and
    CC_TO_SM_2026-10-24_W154_THE_HOLOMORPHIC_RESULT_AND_THE_LADDER_CLAUSE.md;
  - docs/LOOK_LEDGER.md;
  - chat1's e16 commit message (B1713's indices 149, 150, 153 = (2/5, 1/10), (2/5, 3/10), (2/5, 9/10); 12 order-5
    and 36 order-10 lines).
- **Two stale docstrings in main's instruments, seen while reading them.** They are not cells, and they change no
  computation:
  - census.py's apexes() says "words of length 12", but its code takes necklaces of length 13;
  - compare.py's _load says the row count asserted is 33 250, but its code asserts POINTS = 10 704.
- **Not read:** no value of census.jsonl, comparison.json, control.json, census_run.txt or compare_run.txt beyond what
  FINDINGS prints. Their sha256 and line counts were computed from `git show` output.
- **By hand:**
  - the count of primitive necklaces of length 13, (2¹³ − 2)/13 = 630;
  - the T-law classes: a line (α, b) moves along a class of size the order of α in ℚ/ℤ, except that α ∈ {0, ½} gives
    sizes 1 and 2 under the sign. This gives C2 (i)'s sizes, and the 64 as the cusp counts of Γ₁(N) for N = 1 to 12
    (1, 2, 2, 3, 4, 4, 6, 6, 8, 8, 10, 10);
  - C2 (iii)'s twists.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.
