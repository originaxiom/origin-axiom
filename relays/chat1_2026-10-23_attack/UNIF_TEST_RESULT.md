# THE UNIFICATION-SCALE TEST — the result

chat1 (the web seat), 2026-10-27. Rule `UNIF_TEST_RULE.md` (sealed at ef08144e1 and pushed before the script); script
`unif_test.py` (031bbacde, committed before its run). Every output was committed before it was read:
- C0 4b0b19d4a; C1 a53347f7f; the store 1e2556df8; C2 2af7f4986. C2 was read after its commit and before any row was
  read: its outcome was relayed in 9f19b76b7 (2026-10-24, 19:51; the scan began at 19:39), and its arm-G failure was
  restated in the ledger declaration 8cc6dd1a8 (at 8 of 28 chunks), three days before the rows' commit;
- the rows and the calibration summary 8e136d06d. The scan ran in seven parts, resuming from its chunks: parts 1–6 each
  stopped at a chunk boundary before the sandbox's two-hour limit, and part 7 wrote the last chunk and the outputs (logs
  7af025eee, 1fe049d02, 67c1f9c03, de54e2ce6, df03bf834, b12eb9def, 8e136d06d). The session paused between part 3 (2026-10-25, 00:34) and part 4 (2026-10-27, 16:31); the chunks
  were unchanged;
- the calibration: arm Z 58b8c0cc5, arm G ac26599e0. Neither ran. Each arm's H1′ failed, and the script's own gate then
  skips the calibration;
- the cells 7bc4a0818;
- the read-outs after the cells (labelled, no grade): 3a4ef5c67.

How the grade is read under the joint look ledger was declared before any cell existed (8cc6dd1a8). The cells were read
once, after their commit. Checked read-only by a referee before sending. 0 of 19.

## The answer

**Arm Z, against the M_Z targets: a negative, as sealed.**
- The declared two-stage search found no direction bringing the nine below 21.67 on any of the 5 280 rows of the 264
  lines away from the look's two lines. The lowest is 29.15, on (2/5, 1/5) at 0.225 + 2.275i, L₂ (χ²_six 2.79 there).
- Its power is measured. C2Z met 71 of 72 planted rows, so the per-row miss rate's exact two-sided 95% upper end is 7.5%.
  C3Z holds, and C3′Z holds on 19 mirror pairs below 50, every one agreeing within 1%.

**Arm G, against the unification-scale targets: no reading.** The lowest on the 264 lines is 29.94, on (2/5, 1/5) at
0.225 + 3.175i, L_max. But C2G failed (65 of 72), so by the rule H1′G's failure is not read as a negative.

**On the look's lines (reported, not graded; the rule calls them near-foreknown at Z):**
- at Z, two rows of (2/5, 0) are below both bars: 17.06 and 17.22 (χ²_six 1.27 and 0.96), at 0.225 + 2.275i and
  0.275 + 2.275i, L₂ — the line where the A1 look found 17.26 (at 0.5625 + 2.1i), 0.38 and 0.34 away from that row.
  The grid's nearest row to the look's rows, (2/5, 3/5) at 0.275 + 2.275i, L₂, gives 44.34 at Z;
- at G nothing is below 21.67 on any line (the lowest is 23.30, also on (2/5, 0)).

| cell | statement | prior G | G | prior Z | Z |
| --- | --- | --- | --- | --- | --- |
| H1′ | some test row on the 264 lines below 21.67 | 30% | **fails**: lowest 29.94 | 35% | **fails**: lowest 29.15 |
| H2′ | some test row's optimum on the 264 lines below both bars | 25% | **fails** | 30% | **fails** |
| H3, H3′, H3′_BAR, H3″_BAR | the calibration's cells | 70/25/12/8% | not run (H1′ failed) | 75/30/15/10% | not run (H1′ failed) |
| H4 | a row below both bars with D within 10.58 ± 0.33 | 8% | **fails**: no row below both bars | 10% | **fails**: the two rows below both bars have D = 9 (order 5) |
| H5 | \|J\| within a factor 3 at the lowest row below both bars on the 264 lines | 10% | not graded: no such row | 10% | not graded: no such row |
| H6 | m_b/m_τ within a factor 1.25 at the lowest such row on the 250 lines | 15% | not graded: no such row | 8% | not graded: no such row |
| C0 | the model, J, \|V\|, the χ² paths, the targets, the sets' relations, the searches' repeatability | 99% | **holds** (5.9 × 10⁻¹³ at worst) | | |
| C1 | the store against `coupling()` at five points | 95% | **holds** (4.7 × 10⁻¹⁶) | | |
| C2 | power: at or below the planted χ² on at least 68 of 72 | 85% | **fails**: 65 (upper end 19.0%) | 85% | **holds**: 71 (upper end 7.5%) |
| C3 | R4 at the optima of the 100 mirror pairs, to 10⁻⁸ in ln | 95% | **holds** (1.1 × 10⁻¹⁰) | 95% | **holds** (6.2 × 10⁻¹¹) |
| C3′ | every mirror pair with a minimum below 50 agrees within 1% | 75% | **holds**: 13 of 13 (all pairs: 94 of 100; stage B on one side only: none) | 75% | **holds**: 19 of 19 (all pairs: 100 of 100; stage B on one side only: none) |

**What it means, in the rule's fixed words:**
- **Arm Z:** "H1′X fails, with C2X and C3′X holding: the declared two-stage search found no direction bringing the nine
  below 21.67 on any of the 5 280 rows of the 264 lines, with a per-row miss rate on planted rows of at most C2X's stated
  bound; a negative for A1 against X's targets on these rows, with the stage-B gate's limit stated under the search."
  C2Z's bound is 7.5%, on planted rows. **The stage-B gate's limit, in the rule's words:** stage B (`search_v3`) runs only
  where stage A's minimum is below 150, so "a row whose stage-A minimum is 150 or more while some direction lies below
  21.67 would be missed; no measurement excludes it". C2 does not exercise the gate: the largest stage-A minimum on a
  planted row was 25.5 at Z. (A labelled post hoc read-out of the committed rows: on the 264 lines at Z, stage B ran on 93
  rows and lowered the minimum on 55, by at most 7.9; the other 5 187 rows ended stage A at 150.9 or above.)
- **Arm Z, on the look's lines:** "H2′X fails while H2X holds: below both bars only on the look's lines; not a new row."
- **Arm G:** "C2X fails: a failure of H1′X is not read as a negative."
- **Across the arms:** cases (a)–(c) need an arm to meet the first outcome bullet, and neither does. Case (d) needs H1′ to
  fail in both arms with C2 and C3′ holding in both, and C2G failed. So no cross-arm reading applies; what stands is arm
  Z's negative.
- **Against THE HOLOMORPHIC READING TEST:** "a negative is claimed only from arm Z (its search's power is measured, the
  other's C2 failed)". The two agree: neither finds a row below 21.67 away from the look's lines (that test's lowest
  there was 33.98).
- **Under the joint look ledger,** as declared before any cell (8cc6dd1a8, item 5): "Negatives are not affected. A
  negative under the rule (arm Z, with C2Z and C3′Z) needs no Bonferroni factor." And, as its item 6 asks: under each
  of its readings (24, 28 or 35–36 looks) and under main's count (Review 70: "every reading is above 27"), nothing is
  graded PASSED, because the calibration did not run.

**The cells' other read-outs** (the rule asks for them):
- **The H1′ rows' ranks:** by grid minimum on the 264 lines, 38th at Z and 3rd at G; by calibration-grid minimum among
  the eligible rows, 111th and 304th. So the coarse calibration grid, had the calibration run, would not have priced the
  H1′ row.
- **The coarse price that the calibration would have refined:** the data's best calibration-grid minimum is 179.9 at G
  (6% of set 1 and 24% of set 2 at or below it) and 106.3 at Z (4% and 17.7%).
- **Rows below 15.09 / 21.67 / 50 / 100:** at Z 0 / 2 / 36 / 77 on all lines and 0 / 0 / 23 / 58 on the 264; at G
  0 / 0 / 26 / 58 and 0 / 0 / 12 / 41. The quantiles of χ²_nine at 1 / 5 / 50%: Z 71.6 / 295 / 1 374; G 93.2 / 372 /
  2 063.
- **Rows above 10⁷:** one at Z, (1/2, 1/3) at 0.225 + 2.875i, L₂. It is a recomputation artifact of the read-out (the
  search's minimum there is 2.6 × 10⁵), not a row whose outputs vanish identically.

**chat1's additions (labelled readings after the cells):**
- **The two arms on the same rows.** On the 264 lines χ²_nine is higher at G than at Z on most rows (quantiles 10/50/90%
  of G − Z: 106, 603, 3 102; G lower on 88 of 5 280). On the 23 rows where either arm is below 50, the median of G − Z is
  +6.1 and G is lower on 7. So on these rows the unification-scale targets do not suit A1 better than the M_Z targets.
  This is a read-out, and arm G's search failed its power control (C2G, 65 of 72). By the rule, the arms also differ in
  their inputs' edition and in σ (arm G's is smaller for m_u/m_t and the down ratios), so "a difference between the arms
  is a difference between the targets, not of scale alone".
- **By order (Z):** the lowest χ²_nine is on order 5 (17.06, the look's line), then order 10 (42.4), 9 (67.8), 11 (120)
  and 8 (191); order 7 gives 649, order 12 59 402, and orders 1–4 and 6 more than 2 × 10⁵.
- **At the H1′ rows** (both on the order-5 line (2/5, 1/5)) D = 9 exactly and m_b/m_τ = 1, the order-5 lines' known
  values. |J| there is 4.8 × 10⁻⁶ at Z and 2.1 × 10⁻⁶ at G, against targets of 3.08 × 10⁻⁵ and 2.61 × 10⁻⁵; m_t/m_b is
  1.67 and 1.62.
- **The b–τ equality** holds on the 16 lines of orders 1, 2 and 5 to 1.1 × 10⁻¹⁴. Against the targets, m_b/m_τ = 1 is 1.31
  times arm G's 0.761 and 0.61 times arm Z's 1.642.
- **The read-outs (after the cells, no grade):** arm G's twenty lowest rows (on all 266 lines, the look's included),
  searched again at tan β 5, 30 and 50, at η = 0. None falls below 21.67: the lowest is 23.86 at tan β 5, 24.26 at 30 and
  27.98 at 50, against 23.30 at the arm's tan β 10. So on these twenty rows the arm's choice of tan β is not what keeps
  them above the bar.

**What follows:** the rule's next step after a positive (a rule that fixes h, the plan's C-1) is not triggered. The
two-direction route that this seat's earlier relays said would wait for this result is not started: under the owner's
approved plan this seat waits for main's word on the checking pass for B1786 and on P-323. The Higgs sector's next steps
are held by the SM seat (its stage 3) and main (its step 3 and P-357, P-366).

**Reach**, the rule's sentence (with "by hand" added, and C2's power holding at Z only): conditional on the frame as main
built it (B1736's scalar part zero), the 266 lines, the ten τ, the two horocycles, c = 3 by hand, each arm's targets (for G
one published running at tan β 10, η = 0, M_SUSY = 3 TeV), the reading S, and the declared search with C2's measured
power. Between the sampled τ nothing is claimed.

**For the look ledger (main's to enter):** proposed as the outcome cell of the ledger's existing row for this test (row
1381, "the nine at M_GUT and M_Z", running): NEGATIVE as sealed at arm Z; no reading at arm G (its power control failed
before the scan began: 2af7f4986; 8cc6dd1a8 item 4). Counted as the rule counted it: two looks, one per arm, arm G's
target the nine at M_GUT.

0 of 19.
