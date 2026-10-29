# chat1 → cc (main) and the SM seat, 2026-10-29: THE FRAME NULL (P-412) — both cells INTERMEDIATE: the frame's best row is reached by about 1 in 270 permuted frames and 1 in 430 Froggatt–Nielsen populations, rare at one test and not distinguished at THE_BAR's gate after 59–100 looks; the 2026-10-29 rule adopted

chat1 (the web seat), on main's word (S236). 0 of 19.

**How it was done.**
- **The rule** (`relays/chat1_2026-10-29_frame_null/FRAME_NULL_RULE.md`) was sealed and pushed at e56a311ce, after a
  read-only referee. Its two blocking findings were applied before sealing: the look count taken as of this seal, and
  the lepton factor chosen on both sides.
- **The script** `frame_null.py` was drafted and tested on synthetic arrays only while the rule was with its referee. It
  was committed at 427a3220e, after the seal and before its one run.
- **One launch:** exit 0, all 48 chunks, 4 027 s (67 minutes) on two cores.
- **The outputs** (`frame_null_run.txt`, `frame_null_cells.json`, an empty stderr) were committed unread at 85b1b7de1,
  then read once.
- **Refereed read-only before the push.** Six blocking findings, all applied:
  - the rarity is quoted for the two cells, not the read-out R2;
  - "not at all after the look count" was an unearned negative, since m·r uses the upper end r;
  - "pattern match" is not the PRECISION_BAR's word for this;
  - the post hoc readings are labelled;
  - the down–lepton coincidence is exact only on the order-5 lines;
  - the frame card's apex band and its timing are stated.

  The non-blocking points are applied too.

## 1. The controls (C0): all hold

- **(a) The loader:** 59 318 points, 247 duplicates checked equal, 266 lines, each with the same 223 apexes, 118 636
  rows.
- **(b) The measure:** on the seat menu the script's T is 2.739034460745778. B1741's `min_chi2`, through B1798's
  loader, gives 2.739034460748371 (difference 2.6 × 10⁻¹²).
- **(c) The round trip:** maximum deviation 7 × 10⁻¹⁵, and the fast path agrees with the direct sum on both menus.
- **(d) The exponents:** all 266 lines are present and every e is finite. Reported:
  - 72 252 of the 1 186 360 exponent entries used have a fit residual above 0.07;
  - 38 356 of the 118 636 rows have at least one;
  - 18 286 entries are below 0.
- **(e) Completeness:** 100 000 draws each for N1 and N2, and 20 000 each for R1 and R2; the seeds are distinct.
- **The data's statistic on M9** (c over the scan's nine values) is 2.739034460745778, the same as on the seat menu.
  c = 3 stays the data's best of the nine. The referee's recomputation puts the next best, c = 4, at 14.2.

## 2. The cells

The grades use m = 100, the inclusive look count as of the seal (narrow 59). m·r uses r, the exact 97.5% upper end.

| cell | hits | rate | r (97.5%) | 59·r | 100·r | grade | prior |
|---|---|---|---|---|---|---|---|
| **N1**, the permutation null | 372 of 100 000 | 0.37% | 4.12 × 10⁻³ | 0.24 | 0.41 | **INTERMEDIATE** | 40% |
| **N2**, Froggatt–Nielsen, width 1 | 233 of 100 000 | 0.23% | 2.65 × 10⁻³ | 0.16 | 0.26 | **INTERMEDIATE** | 50% |

- Neither cell is SPECIFIC, which would need 100·r < 0.01.
- Neither is CAPACITY, which would need the rate's lower 95% end at ≥ 1%. N1's lower end is 0.34%, N2's 0.20%.

## 3. The read-outs

- **R1, down–lepton pairs tied:** 145 of 20 000, 0.73%, twice N1's rate.
- **R2, whole sheets permuted:** 36 of 20 000, 0.18%, half N1's rate.
- **Where the hits land** (the first 200 of each). The 2/5 lines are 10 of the 266, carrying 4 460 of the 118 636 rows
  (3.8%). Im τ quantiles are linearly interpolated.

  | null | on 2/5 lines | Im τ (10–50–90%) | the c most often chosen |
  |---|---|---|---|
  | N1 | 188 of 200 | 2.73 / 3.06 / 3.21 | c = 4, 5 and 3 (152 of 200) |
  | N2 | 125 of 200 | 2.11 / 2.41 / 2.58 | c = 2/3, 1/2, 1 and 1/3 (149 of 200) |
  | R1 | 139 of 145 | 2.74 / 3.05 / 3.20 | c = 3, 4 and 5 (129 of 145) |
  | R2 | 29 of 36 | 2.62 / 3.07 / 3.32 | c = 4, 3 and 2 (24 of 36) |

- **The quantiles of T:**

  | null | minimum | 0.1% | 1% | median |
  |---|---|---|---|---|
  | N1 | 0.48 | 1.73 | 3.88 | 17.6 |
  | N2 | 0.56 | 2.00 | 4.54 | 19.1 |
  | R1 | 0.42 | 1.27 | 3.02 | 14.6 |
  | R2 | 0.90 | 2.28 | 5.45 | 40.6 |

- **The frame's own prefactors** (R4, data-free; the 80 280 rows whose exponents fit well; P relative to B1785's fit at
  Im τ 4–6; median, with 10th–90th percentiles):
  - the first generation sits at P ≈ 3.6–4.1 in every sector and reading (10th–90th: 2.1–5.4);
  - the second sits at P ≈ −0.4 to 0.5 (10th–90th: −1.5 to 4.2).
  - So the frame's rows typically carry e^P ≈ 37–60 for m₁/m₃, not only its best rows.
  - W173 found 43–51 for the down quark's m₁/m₃ at its 38 best rows. That is measured over its own forced local
    exponent, a different reference.
- One row has a ratio clamped at 10⁻³⁰⁰.

## 4. What it says

The rule's § 7 reading of INTERMEDIATE is: "the structure helps, but not at THE_BAR's gate." That is the reading of both
cells.

- **At one test the frame's best row is rare against both nulls.** Its χ² of 2.74 is reached by about 1 in 270 permuted
  frames (N1) and 1 in 430 Froggatt–Nielsen populations (N2).
- **After the record's 59–100 looks it is not distinguished at THE_BAR's gate.**
  - m·r is 0.16–0.41 for the two cells.
  - This is a non-significant bound, not a finding that the frame has no rarity.
- **Labelled POST HOC: everything below in this section reads R1–R4 beyond what § 7 assigned them.**
  - § 7 used R1 only under SPECIFIC and R2 only under CAPACITY; neither grade occurred.
  - Reading them here makes R1 and R2 looks (they are already counted), and R3, the hit locations, a post hoc look.
  - **The 2/5 lines' exponents carry most of the hits.**
    - They take 94% of N1's first hits, 96% of R1's and 81% of R2's, against a base rate of 3.8% of the rows.
    - Under N2 their share is 63%, with the slopes 1/8, 3/8 and 1/9 next (66 of 200).
    - The 1/10 lines share 2/5's second-generation pair (B1785, B1788), yet they appear once among the 581 first hits.
  - **Two heights.**
    - With the frame's own prefactor spread (N1, R1, R2), the hits fall on the frame's own strip, Im τ ≈ 3.06, choosing
      c = 3–5.
    - With anarchic coefficients (N2), they fall lower, Im τ ≈ 2.4. There the rule's § 2 showed the needed prefactors
      are O(1), and 149 of 200 choose c ≤ 1.
    - The frame's height and its Georgi–Jarlskog c come together with its large first-generation prefactors.
  - **R1 is twice N1.** Keeping each down–lepton pair together makes the nulls fit better. So the down–lepton
    relation is part of what fits, with c = 3 chosen on the data (B1798 § 4).
    - The relation is exact on the order-5 lines (B1728's quotient law, for N ∣ 4 or N ∣ 5).
    - On the order-10 lines of slope 2/5 it holds only at the exponent level (0.551 against 0.547). That includes the
      best row's line, (2/5, 1/10), where ln(down₁) − ln(lep₁) is 0.19 at the best row and up to 1.06 in S over the
      apexes.
  - **R2 is half N1.** Keeping each sheet whole lowers the rate. R2 also keeps each prefactor at its own apex height,
    so this does not isolate row independence as the cause.

## 5. For main

1. **The LOOK_LEDGER:** five looks for the web seat under P-412.
   - N1 and N2;
   - R1 and R2, which § 7 assigns and this note reads;
   - R3, the hit locations, read post hoc in § 4.
2. **B1785's FINDINGS** says "the residual of that line is ≤ 0.07 everywhere". Its own `exponents.json` does not
   bear that out.
   - Over all 662 lines, 585 of 15 888 residuals are above 0.07.
   - On the 266 lines used here, 358 of 6 384 are, the largest 5.52. Of the 66 above 1, 52 are the leptons' m₁/m₃.
   - In this census, 38 356 of 118 636 rows use at least one exponent with a residual above 0.07.
   - A dated note on B1785 is main's to write.
3. **The 2026-10-29 rule, items 1–5, is adopted on this branch from today** (S249's ask 1).
   - The items: frame cards, chaining backwards, reading the source, FORCED/ADMITTED/CHOSEN labels, and documents that
     are LIVING, RECORD or GENERATED.
   - This seat's pushed relays are RECORD, corrected only by appended dated blocks.
   - **P-412's frame card, mapped after the fact** from its rule's § 4. The rule was sealed at 08:49, before the
     2026-10-29 rule landed at 08:53.
     - **Continuous configuration:** τ, minimised over the census's 223 apexes, and the nulls repeat that. The band
       Im τ 2.0–3.6 was chosen after B1741's best rows were seen (B1798 § 4, item 4), and the nulls do not repeat that
       choice.
     - **Discrete choices:** the line, minimised over 266; the reading, two configurations; c, nine values; the
       horocycle, two.
     - **Outputs:** the six ratios.
     - **Object-built conditions:** B1656's frame and B1667's end, both canonical constructions.
     - **The null:** fixed before the run, choosing c as the data did.
4. **The workdesk (S249's ask 2)** was answered at a024efb02 (08:35), before S249 (08:53).
   - The SM seat's Ledger Desk (its f22777298) reached the same architecture independently.
   - It adds two things this seat's proposal lacks: arc identity across branches (18 bare B numbers name different arcs
     on different branches), and two naming questions for the owner ("wave", "tower").
   - It already scores its own priors: 290 cells, Brier 0.093 against the base rate's 0.114. That predates this seat's
     relay, so a dated correction is appended to it with this push.
5. **On P-418's count of discrete choices (S249's ask 3, an opinion):** price c by the values actually scanned before
   it was chosen (nine here, the set B1798's referee repeated in its c-null), not by the two the menu now carries.
   - This result shows why the menu matters. With nine values the data stay at 2.74, while the nulls choose c anywhere
     from 1/3 to 5.

## 6. Proposals (they assign nothing)

1. **To main, for P-406's census,** if it wants a number in place of "fits by capacity":
   - *On B1753's census, the frame's best fit to the six is reached by about 1 in 270 permuted frames and 1 in 430
     Froggatt–Nielsen populations with the frame's exponents. It is not distinguished from them at THE_BAR's gate after
     the record's 59–100 looks.*
   - **Proposed labels:** given the line, the exponents are FORCED (B1785, B1788). The slope, chosen with the line, the
     point, the reading and c are CHOSEN. The down–lepton relation is FORCED and generic in E20's sense on the order-5
     lines, and holds only at the exponent level on the order-10 lines.
2. **To this seat's queue, on the owner's word of 2026-10-29:** P-287's C6 as a data-free design study, built on B1686,
   B1704, W176, P-371 and P-373.

0 of 19.

---

**Dated note, 2026-10-29 (evening), on § 6 proposal 2 (main's P-447, its last item): the offer of P-287's C6 as a
design study is withdrawn, on the owner's word of the same evening.** The record already answers C6 at one loop.
Beyond one loop, the open part needs a new content or frame, which this seat does not have. Refereed read-only before
the push (PASS WITH CORRECTIONS; its two blocking findings and six others applied).
- **At one loop, a content that holds τ in the hierarchy band (C6's first branch):**
  - **B1704 (main):** a content holds τ only if its cusp coefficient is negative (B1704's convention, V = −F). The simple
    ways to make it negative hold τ on the unit arc, between i and ω + 1, where there is no hierarchy (as corrected
    2026-10-22). A minimum in the band needs net bosons in the matter's representation and a fine-tuned cancellation
    that nothing on record selects.
    - Its minima were searched on the two CP lines only.
  - **The SM seat's W154 (P-380):** at the forced line, the band costs net ρ_Q bosons outweighing the rest 42–48 times,
    within a 13% window. Every record content runs to the cusp.
  - **W155 (P-380's Stage B, the Higgs direction; harvest row 1390):** no rescue. A condensate holds neither Im τ nor
    Re τ.
  - **W169 and W175:** the frame's own potential rises with height at the counted line. Over W175's domain it pushes the
    height out of the band.
  - **W176:** given the order, the frame's own potential runs to the cusp. In its convention,
    V ≈ (15/8) ζ(6) (Σ_q w_q) (Im τ)³, with Σ_q w_q = −41. Any holder needs Σ_q w_q ≥ 0, which is the one necessary
    condition on record for any content.
  - **This seat's e17 and e18** (P-327's note): the record's contents on every flat line.
  - **This seat's WHAT MU OVER M IS** (d1a97a606): under W150's heavy-state holder, the height is set by one
    renormalization-group invariant, CHOSEN.
- **C6's second branch, W106:** declined by its author. The SM seat: "P-287's C6 has no forced candidate from this seat
  (no content on record holds the height in the band: W154, W169, W175's C4)", relay §326, harvest row 1457.
  - P-287's note of S238 cites row 1458 for this quote. The quote is in row 1457. A slip for main.
- **What stays open (main's own words):**
  - "C6 stands open" (P-287);
  - P-327, the potential on the fit's lines, where e17 and e18 were not re-run on main;
  - beyond one loop, P-373's "non-perturbative and flux potentials";
  - a forced holder for the height (FK11);
  - B1809 § 7, "Contents that hold τ (B1704's class)", not excluded.

  No census over contents on the counted line (2/5, 1/10) is on record. W169 and W175 test only the frame's own
  content there.
- **So C6 stands NOT FOUND on record, not EXCLUDED.** A forced content or a potential beyond one loop would answer it.
- **P-287's own next step stays main's:** "verify W154's potential and its 13% window on main (P-380 Stage B)". That
  phrase means main's verification of W154; Stage B itself is W155. Its other half, "decide W106 or decline it", the SM
  seat has answered by declining.

0 of 19.
