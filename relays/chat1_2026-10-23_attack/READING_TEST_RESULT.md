# THE READING TEST — the result

chat1 (the web seat), 2026-10-24. Rule `READING_TEST_RULE.md` (sealed, committed and pushed at d58a4dbdb before the
script); `reading_test.py` committed at 4f2b00054 before its run; C0 5c5238b63; the store and C1 e3e2da385; C2
4c5cb8bd2; the rows f835579b1 (part 1 log f1159aa5e); the cells 3247a5f53; each committed before it was read. Post hoc
script a8da38e4c, its output 4c77106ac; read-out script 0ac7cccd8, its output e702d82a0 (`reading_test_readouts.json`).
A read-only referee checked this note before it was committed. 0 of 19.

**Disclosed:** the scan ran into the sandbox's two-hour limit on one job after its 3 600-row checkpoint
(`reading_test_scan_run_part1.txt`). `--resume` (c2067c1bd, added after launch) finished the remaining 736 rows from that
checkpoint (`reading_test_scan_run_part2.txt`): rows 1–3 600 come from 4f2b00054's code and 3 601–4 336 from c2067c1bd's,
whose `scan_row` is identical; the resume asserted the checkpoint's job order. Everything below the cells table is a
read-out; §4 is post hoc and labelled.

## 1. Controls

| control | result | holds |
| --- | --- | --- |
| C0 | Lemma A's identity symbolic; Lemma A′'s identity to 1.2 × 10⁻¹⁵, largest ‖u‖/m₃ 1.23 (≤ √3); the vectorised model equal to `inverse_higgs.nine` to 9.6 × 10⁻¹³ | yes |
| C1 | the store against `coupling()` at the first five points: 4.2 × 10⁻¹⁶ | yes |
| C2 | power: the search met or beat the planted near-solution's χ² on **34 of 36** rows, exactly the threshold. The misses: a near-conic direction (\|h·h\| 0.15), where the search stopped at 12.7 against a planted 8.1 (exact targets: 27.4, where the planted χ² is 0 — above the bar), and a uniform one (\|h·h\| 0.66), at 27.5 against 9.3 (exact targets: 13.7 against 0). Read-outs: with exact targets 33 of 36 recovered to χ² ≤ 0.1 and 34 to ≤ 2.167; against the bar rather than the planted value, 35 of 36 noisy and 35 of 36 exact-target searches ended below 21.67 | yes, with no margin |
| C3 | the 80 mirror pairs' minima agree within 1% on **80 of 80** (largest deviation 0.03%) | yes |

C2 passed at its threshold with no margin (a 95% interval for the per-row rate is 81–99%; the disclosed dry run on
TWO_HIGGS's rows met 36 of 36). Both misses ended tens of units above the planted χ², not hundreds: at most a factor 3
with noisy targets, and 27.4 and 13.7 with exact targets, one of them above the bar.

## 2. The cells

| cell | statement | prior | result |
| --- | --- | --- | --- |
| **S1** | no row of the 4 256 has a minimum χ²_nine below 21.67 | 92% | **holds**: the lowest minimum is **1 045.4** |
| **S1′** | no row below 100 | 85% | **holds** |
| S4 | every row's optimum in a failure branch (\|V_ud\| < 0.5 or \|V_cb\| > 0.5) | 80% | **fails** on 15 rows |
| S5 | every row's optimum excluded by Lemma A or Lemma B | 60% | **fails** on 82 rows |

- **S1 and S1′.** No degenerate rows, no non-finite minima, no row below 500. Quantiles of the 4 256 minima: 1% 1 204,
  5% 1 343, median 2 280. **At every row's optimum the CKM's share of χ² alone exceeds the bar** (smallest 368, median
  1 188); that share does not involve c or the leptons, but it is the share at the c = 3 optimum, not a bound over
  directions, so S1 stays conditional on c = 3. The lowest rows are the structure THE_NEXT_ATTACK §2.5 found on
  TWO_HIGGS's grid: (2/5, 7/10) at 0.6354 + 3.3521i, L₂, χ²_nine 1 045.4, with |V_us| and |V_ub| within 2.5% of the data,
  |V_ud| 0.973 and |V_cb| 23.9 times the data (the 2-3 block exchanged); χ²_six there 73.
- **S4 fails** on 15 rows on ten order-12 lines ((1/6, b), (1/3, b), (0, 1/12), (0, 5/12)), where the optimum gives up
  the masses (χ²_six 86 000–106 000; far from null, |h·h| ≥ 0.98) and keeps a roughly aligned CKM (|V_ud| ≥ 0.98,
  |V_cb| 0.066–0.44 — inside its bar on (0, 5/12) at 0.6354 + 2.1146i, L₂). Lemma A's branches are not exhaustive there.
  Every row is listed in `reading_test_readouts.json` ("S4 rows": line, τ, horocycle, χ²_nine, χ²_six, |h·h|, |V_ud|,
  |V_cb|, α_u3 − α_d3 and the χ² terms above 21.67).
- **S5 fails** on 82 rows (order 12: 34, 8: 16, 11: 9, 10: 8, 4: 7, 9: 6, 7: 2): 9 of them are S4's rows; 4 more are
  order-12 optima far from null with |V_cb| 0.60–0.73; 69 have the 2-3 block exchanged (|V_cb| 0.90–0.97) between
  heaviest states equally far from real (|α_u3 − α_d3| ≤ 0.0675), where Lemma B is silent — for example (0, 5/11) at
  0.6354 + 2.5271i, L₂, χ²_nine 1 349, |V_ud| 0.99, |V_cb| 0.94, and the (1/8, b) rows with |V_ud| 0.41–0.63 and |V_cb|
  0.93–0.97. The 7 order-4 rows among them sit inside Lemma A′'s tube (|h·h| ≤ 2 × 10⁻⁴), which excludes them exactly.
  Every row is listed in `reading_test_readouts.json` ("S5 rows", with its class). Of the other 4 174 optima, Lemma B
  excludes 1 402 alone, Lemma A 16 alone, and both 2 756.

## 3. Read-outs (`reading_test_readouts.json` unless marked)

- **The failure branches** (THE_NEXT_ATTACK §1.6): |V_ud| < 0.5 at 2 992 optima, |V_cb| > 0.5 at 4 049, both at 2 800,
  neither at 15 (S4).
- **By line order** (lowest minimum): order 10 1 045, 5 1 049, 9 1 127, 7 1 196, 1 1 224, 2 1 225, 6 1 230, 3 1 253,
  8 1 265, 11 1 287, **12 62 661**, **4 198 750**. By α (the five lowest of 24): 2/5 1 045, 2/9 1 127, 3/7 1 196,
  0 1 214, 1/2 1 230.
- **By τ and horocycle:** 1 198 / 1 195 / 1 175 / 1 045 at Im τ 2.11 / 2.53 / 2.94 / 3.35; 1 049 at Re τ 0.1146 and
  1 045 at 0.6354; L₂ 1 045, L_max 1 185.
- **How much of CP² the exact bounds exclude** (`reading_test_cells.json`; the 4 000 random directions per row, uniform on
  CP²): Lemma B a median 78.6% of them per row, Lemma A 0.08%, either 78.6% (smallest 59%); the lowest χ²_nine among
  random directions that neither bound excludes, over all rows, is 1 495.
- The refinement lowered the grid's minimum on 3 941 of the 4 256 rows.

## 4. Post hoc (labelled): a denser search

`reading_test_posthoc.py` (a8da38e4c, committed before its run, after the cells were read; output 4c77106ac): the same
search with eight times the directions (t on 1 600 points, 32 phases, 16 000 random) and all 26 record starts. Its grid
does not contain the sealed one (a different t lattice and random seed).

- **On 80 rows of the scan** (the 40 lowest and 40 more, seed 2024) it agreed with the sealed minima to 0.1% on 77
  (lower on 42 of them, by at most 0.098%; higher on 12; equal on 23) and lowered three, by 5.5%, 1.1% and 0.2% (rows at
  1 947, 2 118 and 73 772). The 40 lowest rows agree within 0.016%; the lowest minimum stays 1 045.4.
- **On C2's two missed planted rows it failed too:** 18.1 and 26.6 against the planted 8.1 and 9.3 (exact targets 26.2
  and 12.0, against 0); on the first it ended higher than the sealed search (12.7). Both searches leave these planted
  near-solutions 5–27 units above the planted value, not hundreds: the measured weakness is real and of this kind.

## 5. What it means (as the rule fixed it)

- **S1 holds, with C2 and C3.** On every flat line of order ≤ 12, at these eight τ and both horocycles, with c = 3, the
  declared search — with the power C2 measured — found no Higgs direction that lets the Standard Model's one-doublet
  reading reach the nine's bar. Near the null conic Lemma A′ excludes it exactly; elsewhere the claim is the search's.
  If main's identification of S̃ with H̃ holds, this points to (it does not show) a flavour sector that cannot be read
  with one doublet and needs two Higgs directions with equal (holomorphic) readings, the structure of a type-II
  two-doublet model or the MSSM's — a structural pointer, not a value, no number of the 19. The next step is then
  THE_NEXT_ATTACK's step 3 (the Higgs pair from a stated rule).
  *Read-outs beside it:* the measured power is about 94% per planted near-solution (34 of 36); the lowest minimum is 48
  times the bar.
- **S4 fails.** Some optima sit outside both branches (§2); Lemma A's branches are not exhaustive there.
- **S5 fails.** Some optima fail the bar for another reason (§2: S4's order-12 rows that give up the masses, four more
  order-12 rows far from null, and 69 rows whose 2-3 exchange happens between heaviest states equally far from real);
  every row is reported in the read-outs.
- **Reach.** Conditional on the frame as main built it (B1736's scalar part zero, a pure Higgs direction), the eight τ,
  the two horocycles, c = 3, the comparison at M_Z and the identification of the readings with H and H̃ (P-295 records
  another reading). Between the sampled τ nothing is claimed.

## 6. Next (a proposal, not the rule's fixed next step)

The rule names THE_NEXT_ATTACK's step 3, the Higgs pair from a stated rule. With the owner's word (2026-10-24, "lets do
it! go for it") chat1 runs first the one structure the reconnaissance left open: one holomorphic direction read the same
in every sector (A1: 17.26 on four mirror pairs of TWO_HIGGS's grid, post hoc), as THE HOLOMORPHIC READING TEST — sealed
on another fresh grid, with a calibration against random targets through the same search.

0 of 19.
