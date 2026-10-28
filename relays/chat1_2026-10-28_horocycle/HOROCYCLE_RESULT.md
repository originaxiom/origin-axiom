# THE HOROCYCLE AND THE HEIGHT — the result

chat1 (the web seat), 2026-10-28. The order of the work:
- **The rule**, `HOROCYCLE_RULE.md`, refereed read-only, then sealed and pushed at 1dd36cfba before the script was
  committed.
- **The script**, `horocycle.py`, committed before its run (5832fde1d). It was tested on synthetic arrays only.
- **The census** ran in two launches. Part 1 stopped at its time limit after the grid and 477 of the 480 searches; its log
  is f6067862d. Part 2 finished the rest. The outputs were committed unread before any cell existed (8de923cea).
- **The cells:** one launch, all 80 refinements in it, committed unread and then read once (84a323125).
- **Post hoc read-outs, labelled,** each script committed before its run and its output before it was read. Both use the
  committed census and cells only.
  - `horocycle_posthoc.py` (ffa39da1c; output a86ad3f75), Q1–Q3, written after the cells were read.
  - `horocycle_posthoc2.py` (56f4778ba; output 6aad0953e), Q4–Q8, written after this note's read-only referee, to
    compute the numbers its corrections need.

Data-free except H4, H5 and the χ² read-outs. Refereed read-only before sending. 0 of 19.

## The answer

**The controls hold, so every cell is read.**

**THE DECISIVE CELL H2: NOT ABSORBED.** Within the window W, in (S̃, S, S), the search found no shift of τ that turns L₂'s
six into L_max's.
- The found distance is attained inside W, so it is an upper bound on A(p); control (b) guards the search's power. Over
  all 480 searches, flagged ones included, it has median 0.57 in log rms (10th to 90th percentile 0.47–0.67). That is a
  factor of about 1.8 per ratio, against the rule's 0.05 and 0.15.
- 77% of the 480 base points are unflagged with a found distance ≥ 0.15, against the 50% needed. That is every
  unflagged search: 370 of 370, the least 0.365 (Q6). None is at or below 0.05.
- 110 searches ended on the window's Re τ edge. They count as failures for both verdicts.

**H4 HOLDS: the six need L_max on the 30 lines of orders 25 and 30.** With τ free within the rule's bounds, by a local
search:
- the least χ²_six at L_max is 2.41, on (2/5, 5/6) at 0.763 + 3.023i;
- the least at L₂ is 30.6, on (2/5, 12/25) at 0.699 + 2.638i, above the bar of 16.75.

L_max's passing was known from B1786. L₂'s failing is the new result.

**So:** within W the horocycle is a separate freedom of the six in (S̃, S, S), and the data choose L_max. It is one
discrete input chosen by the data, counted, as the slope is. No input removed.

| cell | statement | prior | outcome |
| --- | --- | --- | --- |
| H1 | in each sector the first generation's lever exceeds the second's at ≥ 90% of G | 50% | **fails**: up 54%, down 1.0%, leptons 1.7% |
| **H2, THE DECISIVE CELL** | absorption by a shift of τ | absorbed 10%, not absorbed 55% | **NOT ABSORBED**: unflagged found distance ≥ 0.15 at 77% (all 370 unflagged); none ≤ 0.05 |
| H3 | a common first-generation lever (\|Δ₁\| ≤ 0.1) at ≥ 90% of G | 15% | **fails**: 2.8%; median \|Δ₁(ud)\| 1.04, median \|Δ₁(ℓd)\| 0.023 |
| H4 | on the 30 lines, χ²_six < 16.75 at L_max and ≥ 16.75 at L₂ | 75% (the L₂ clause) | **holds**: 2.41 and 30.6 |
| H5 | the least χ²_nine over G on the 30 lines, at each horocycle | passing 1% each | **fails at both**, as predicted: 110.7 at L_max, 116.4 at L₂ |
| C0 | the controls | 90% | **all hold** |

**The controls:**
- **(a)** `compute()` reproduces B1786's stored ratios, every sector, reading and horocycle, at three rows: the best row
  (1.2 × 10⁻¹¹ relative), its mirror (4.0 × 10⁻¹²) and the file's first row (3.3 × 10⁻¹⁴). The stored CKM moduli, which
  H5 uses, were not among the compared values.
- **(a′) and (a″)** The script's χ²_six and χ²_nine give B1786's class minima, 3.00481024888 and 146.081304473, to
  4 × 10⁻¹³ and 1.4 × 10⁻¹².
- **(b)** The search's power: 19 of the 20 shifted L₂ targets were recovered, with distance at most 8.3 × 10⁻⁷ and the
  shift to 2.7 × 10⁻⁶. The one not recovered (j = 3) stopped at a different local minimum (distance 0.053), unflagged.
- **(c)** L_max < L₂ at every point the census stage accepted, and every such point inside B1667's column (Im τ
  2.3–3.5). The refinements lie inside the column by their bounds.
- **(d)** No G point has a non-finite log (0 of 5 200).
- **The searches:** a median of 13 evaluations each. 46 ran the full six iterations, and 38 of those were still improving
  at the last one, by at most 5.1 × 10⁻⁴ (Q7), against found distances of at least 0.365.
- **The refinements:** 17–37 evaluations each, none at the cap of 80.

## What it means, in the rule's fixed words

- **H2 NOT ABSORBED:** "within W, the horocycle is a separate freedom of the six in (S̃, S, S)."
- **With H4 holding:** "the six need L_max on the 30 lines, and L₂'s failing there is the new result. The horocycle is
  one discrete input chosen by the data, counted, as the slope is."
- **H1 fails:** "the first generation does not dominate everywhere." In the down and lepton sectors the second
  generation's lever is the larger one at 99.0% and 98.3% of the points (H1's own fractions).
- **H3 fails:** "no such horocycle-independent first-generation combination exists among these."
- **H5:** fails at both horocycles, as expected.
- **"No value is claimed. No input is removed by H1, H3, H4 or H5."** 0 of 19.

## What the horocycle moves (post hoc, labelled; Q1, Q2, Q4)

**Q1, the levers ln r(L_max) − ln r(L₂) over G:** median (10th to 90th percentile).

| sector, reading | second generation | first generation |
| --- | --- | --- |
| up, S | 1.026 (0.180 to 1.337) | 0.301 (−0.005 to 1.137) |
| up, S̃ | 0.882 (0.373 to 1.608) | 0.874 (−0.226 to 1.587) |
| down, S | 0.787 (0.555 to 0.817) | −0.201 (−0.261 to 0.071) |
| down, S̃ | 0.832 (0.602 to 0.868) | −0.061 (−0.297 to 0.323) |
| leptons, S | 0.783 (0.540 to 0.816) | −0.202 (−0.268 to 0.078) |
| leptons, S̃ | 0.837 (0.599 to 0.874) | −0.041 (−0.302 to 0.369) |

- **The second generation.** From L₂ to L_max, m₂/m₃ rises by a median factor of about 2.2–2.8 in every sector and
  reading.
  - In the up sector the spread is wide: 10th to 90th percentile factors of 1.2–3.8 in S and 1.45–5.0 in S̃.
  - In S̃, m₂/m₃ falls at 3.7% of the points (Q2).
- **The first generation.**
  - In the down and lepton sectors, m₁/m₃ barely moves, slightly the other way. So m₁/m₂ falls by a median factor of
    2.4–2.7 (Q4: levers −0.88 to −0.99).
  - In the up sector's S reading m₁/m₂ falls by a median factor of 2.1 (−0.73).
  - In the up sector's S̃ reading, the cells' configuration, the two generations move about equally (medians 0.882 and
    0.874), and m₁/m₂ is unchanged at the median (+0.055, spread −1.76 to +1.04). There the first generation's lever is
    the larger at 54% of the points (H1).
- **Q2, the signs:** in (S̃, S, S) the six levers do not all share one sign at 89% of the G points and at all 480 base
  points. The down and lepton first-generation levers are negative at 84% of the points.

## Why a shift of Im τ cannot absorb it (post hoc, labelled; a reading; Q3, Q5)

- **The premise, measured at these heights (Q5).** A step of +0.1 in Im τ lowers all six logs at 99.6% of the G steps at
  L_max and at 98.6% at L₂. That is the leading law, with every exponent positive on the slope 2/5 (B1788; B1786's
  first-generation exponents). B1788 proves it at leading order in Im τ, conditionally, and compares it with B1785's
  window at Im τ 4–6; these heights are 2.3–3.5.
- **At leading order,** a shift of Im τ moves ln(m₁/m₂) and ln(m₂/m₃) the same way, in the proportion (e₁ − e₂)/e₂: 7/4
  in the down and lepton sectors (exponents 11/20 and 1/5). The horocycle moves them oppositely in those sectors (Q1,
  Q4).
- **Q3, the residuals at the found minima** (L₂ at the best shift, minus L_max), as medians:
  - up₂ −0.52, up₁ −0.24;
  - down₂ −0.58, down₁ +0.64;
  - lep₂ −0.59, lep₁ +0.64.

  The signs are mixed at all 480 base points.
- **The scope of this argument:**
  - it covers shifts of Im τ only, at leading order;
  - it does not cover shifts of Re τ, which the search also made: a +0.1 step in Re τ moves the six with mixed signs at
    94–97% of the G steps, and moves down's two ratios oppositely at 29–45% (Q5);
  - it does not cover the prefactors' own τ dependence through L and c_s.

  That no shift within W absorbs the lever is H2's result, not this argument's.

## Read-outs (no cell)

- **H4's statistic on the ten (2/5, k/10) lines** (informed by W162 and the selection map): L_max 2.66, on (2/5, 1/10) at
  0.315 + 3.035i; L₂ 22.0, on (2/5, ½) at 0.461 + 2.647i. L₂ is above 16.75 there too, more narrowly.
- **On B1786's own apex grid** (its stored census, the 30 lines): the least χ²_six is 3.005 at L_max and 61.8 at L₂.
- **The comparison scale, labelled** (G-grid minima against the unification-scale targets, tan β = 10, no refinement):

| horocycle | the 30 lines | the ten lines |
| --- | --- | --- |
| L_max | 17.6 | 9.85 |
| L₂ | 70.9 | 54.9 |

  At that scale too L₂ is far worse.
- **The searches:**
  - the best shifts have median Δ Im τ −0.13 (10th to 90th percentile −0.19 to −0.05), and Δ Re τ spans the whole
    window;
  - the rms lever before any shift has median 0.75, and at the best shift the found distance has median 0.57. So the
    shift recovers about a quarter of the rms;
  - the largest single-ratio residual at the best shift has median 0.72.
- **The refinements (Q8):**
  - none ended on an Im τ bound. The refined minima lie at Im τ 2.97–3.15 at L_max and 2.64–3.06 at L₂;
  - 11 of the 40 at L_max and 15 of the 40 at L₂ ended on the Re τ bound. Those at L₂ all have χ²_six ≥ 64.9.
- **The second generation's lever differences:** median |difference| up against down 0.24, leptons against down 0.002.
  The leptons copy the down quarks, as B1789 found: "R₂ → 1 at leading order, prefactors included".

## A correction of this seat's own forecast

This seat told the owner on 2026-10-28 that "the second generation barely moves and the first moves a lot". On these lines
and heights that is wrong:
- the horocycle raises m₂/m₃ by a median factor of 2.2–2.8 in every sector and reading;
- it moves the second generation most in the down and lepton sectors, and in the up sector's S reading;
- in up S̃ the first generation moves about as much.

The reading built on that forecast is withdrawn: that the frame predicts the second generation while its first generation
belongs to the regulator. The first-generation factor of about 30 that this seat quoted came from its own arithmetic, not
from a cell, and it stands untested. The values of both generations depend on the horocycle.

## Reach

- B1656's frame at B1667's end, as B1726's sealed `compute()` computes it (main at 5e1393631, B1786's pins).
- The 40 lines of slope 2/5, at Im τ 2.3–3.5; the cells' configuration (S̃, S, S); B1741's seat menu; the comparison at
  M_Z, with the unification scale as a read-out.
- The two canonical horocycles only. A continuous L, or a third horocycle (P-266), is not covered.
- Absorption is tested by shifts of τ within W. Changes of line, reading or lepton factor are not covered.
- **H4's minima are local:**
  - one Nelder–Mead per line and horocycle, from the best G point;
  - τ in Re [0, 1] and Im [1.5, 3.6], at most 80 evaluations (17–37 used);
  - a minimum outside those basins is not excluded;
  - none lies on an Im τ bound (Q8).

## For main's registers (main's to enter)

- **P-402 and main's plan, step 5.** The horocycle's fitting work, disclosed:
  - with τ free in the rule's bounds (a local search), χ²_six is 2.41 at L_max and 30.6 at L₂ on the 30 lines, and 2.66
    and 22.0 on the ten (2/5, k/10) lines;
  - within W, in (S̃, S, S), no shift of τ absorbs the choice (median found distance 0.57 in log rms);
  - in the down and lepton sectors it acts on m₁/m₂ against m₂/m₃.

  The ledger row could read "the horocycle (L_max) | discrete | selected by the data, not absorbed by τ (the web seat's
  horocycle test)". What could select L_max or L₂ in the object or the field remains P-402's question.
- **P-328:** the horocycle stays among the unruled inputs, now with its fitting work measured.
- **The look ledger:** one sealed look, the six and the nine: H4's L₂ clause (its 75% prior met) and H5 (failing, as
  predicted).

0 of 19.
